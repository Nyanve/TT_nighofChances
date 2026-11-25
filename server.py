"""Spolu: shared money for flatmates and friends. Run: python3 server.py"""
import json
import os
import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).parent
DB = os.environ.get("DB_PATH", str(ROOT / "spolu.db"))
MAX_BODY = 8_000_000  # resized phone photo as a data URL is well under this

# Allowed answers per hypothesis-test event; anything else is rejected.
CHOICES = {
    "jtbd": ["Splitting a receipt with friends", "Sharing rent with flatmates", "Group trip", "Just curious"],
    "pain_freq": ["Never", "Sometimes", "Often", "All the time"],
    "pain_annoy": ["1", "2", "3", "4", "5"],
    "fake_door_click": ["click"],
    "visit": ["new"],  # first visit per device, denominator for the fake-door rate
}

DEMO_RECEIPT = {
    "merchant": "Lidl (sample receipt)",
    "items": [
        {"name": "Rožok 10x", "price": 1.20},
        {"name": "Mlieko 1,5% 1l", "price": 0.99},
        {"name": "Kuracie prsia 500g", "price": 4.49},
        {"name": "Cestoviny Penne", "price": 1.29},
        {"name": "Pivo Zlatý Bažant 6x", "price": 5.94},
        {"name": "Čipsy", "price": 1.79},
        {"name": "Banány 1kg", "price": 1.15},
    ],
    "total": 16.85,
    "demo": True,
}

RECEIPT_SCHEMA = {
    "type": "object",
    "properties": {
        "merchant": {"type": "string"},
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"name": {"type": "string"}, "price": {"type": "number"}},
                "required": ["name", "price"],
                "additionalProperties": False,
            },
        },
        "total": {"type": "number"},
    },
    "required": ["merchant", "items", "total"],
    "additionalProperties": False,
}


def db():
    con = sqlite3.connect(DB)
    con.execute("CREATE TABLE IF NOT EXISTS events (kind TEXT NOT NULL, value TEXT NOT NULL, ts TEXT DEFAULT CURRENT_TIMESTAMP)")
    return con


def save_event(kind, value):
    if kind == "signup":
        if not (isinstance(value, str) and "@" in value and len(value) <= 254):
            raise ValueError("bad email")
    elif value not in CHOICES.get(kind, ()):
        raise ValueError("bad event")
    with db() as con:
        con.execute("INSERT INTO events (kind, value) VALUES (?, ?)", (kind, value))


def results():
    out = {k: dict.fromkeys(v, 0) for k, v in CHOICES.items()}
    with db() as con:
        for kind, value, n in con.execute("SELECT kind, value, COUNT(*) FROM events WHERE kind != 'signup' GROUP BY kind, value"):
            out[kind][value] = n
        out["signup"] = con.execute("SELECT COUNT(*) FROM events WHERE kind = 'signup'").fetchone()[0]
    return out


def scan(data_url):
    """Read a receipt photo with Claude. No photo (sample button) or no API key: demo receipt."""
    if not data_url or not os.environ.get("ANTHROPIC_API_KEY"):
        return DEMO_RECEIPT
    header, _, b64 = data_url.partition(",")
    media = header.removeprefix("data:").removesuffix(";base64")
    if media not in ("image/jpeg", "image/png", "image/webp", "image/gif") or not b64:
        raise ValueError("not an image")

    import anthropic  # only needed for real scans: pip install anthropic

    client = anthropic.Anthropic()
    response = client.beta.messages.create(
        model="claude-opus-5-5",
        max_tokens=16000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        output_config={"format": {"type": "json_schema", "schema": RECEIPT_SCHEMA}},
        messages=[{"role": "user", "content": [
            {"type": "image", "source": {"type": "base64", "media_type": media, "data": b64}},
            {"type": "text", "text": "This is a shop receipt. List every purchased item with its final price in EUR "
                                     "(after any discount on that item). Skip subtotals, VAT lines and payment lines. "
                                     "total is the amount paid. Keep item names as printed."},
        ]}],
    )
    if response.stop_reason == "refusal":
        raise ValueError("could not read this receipt")
    return json.loads(next(b.text for b in response.content if b.type == "text"))


class Handler(BaseHTTPRequestHandler):
    def send(self, code, body, ctype="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/api/results":
            return self.send(200, results())
        if path in ("/", "/results"):  # /results is the hidden dashboard, same page
            page = (ROOT / "index.html").read_bytes().replace(b"/*CHOICES*/null", json.dumps(CHOICES).encode())
            return self.send(200, page, "text/html; charset=utf-8")
        self.send(404, {"error": "not found"})

    def do_POST(self):
        size = int(self.headers.get("Content-Length") or 0)
        if size > MAX_BODY:
            return self.send(413, {"error": "too large"})
        try:
            body = json.loads(self.rfile.read(size))
            if self.path == "/api/event":
                save_event(body.get("kind"), body.get("value"))
                return self.send(200, {"ok": True})
            if self.path == "/api/scan":
                return self.send(200, scan(body.get("image", "")))
            self.send(404, {"error": "not found"})
        except (ValueError, AttributeError) as e:  # json errors are ValueError too
            self.send(400, {"error": str(e)})
        except Exception as e:  # Claude API/network failure: tell the user instead of hanging the UI
            self.log_error("scan failed: %r", e)
            self.send(502, {"error": "Scan failed, try again or split manually"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Spolu on http://localhost:{port}  (results: /results)")
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()

"""Run: python3 test_server.py"""
import json
import os
import tempfile
import threading
import urllib.error
import urllib.request

os.environ["DB_PATH"] = os.path.join(tempfile.mkdtemp(), "test.db")
os.environ.pop("ANTHROPIC_API_KEY", None)  # scan must fall back to the demo receipt
import server

srv = server.ThreadingHTTPServer(("127.0.0.1", 0), server.Handler)
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{srv.server_port}"


def post(path, body):
    req = urllib.request.Request(base + path, json.dumps(body).encode(), {"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, json.load(e)


assert post("/api/event", {"kind": "pain_freq", "value": "Often"})[0] == 200
assert post("/api/event", {"kind": "signup", "value": "a@b.sk"})[0] == 200
assert post("/api/event", {"kind": "pain_freq", "value": "<script>"})[0] == 400
assert post("/api/event", {"kind": "signup", "value": "not-an-email"})[0] == 400
assert post("/api/event", {"kind": "anything", "value": "x"})[0] == 400

r = json.load(urllib.request.urlopen(base + "/api/results"))
assert r["pain_freq"]["Often"] == 1 and r["signup"] == 1 and r["jtbd"]["Group trip"] == 0, r

code, receipt = post("/api/scan", {"image": "data:image/jpeg;base64,AAAA"})
assert code == 200 and receipt["demo"] and receipt["items"], receipt

page = urllib.request.urlopen(base + "/results").read().decode()
assert "/*CHOICES*/" not in page and '"pain_freq"' in page
print("ok")

# Idea: Spolu (working name, Slovak for "together")

Shared money for flatmates and friend groups, inside the bank app.

## Ideas

### 1. Scan & split receipts
- Scan a receipt and the items get read off it
- Tag who had what: tap a friend on each item, or split evenly 2/3/N ways
- Each friend gets a payment request they can pay in one tap

### 2. Rent pact
- One person pays the landlord; the flatmates set up a pact in the app: amount, share each, payday
- Everyone accepts it once, then each share moves automatically every month
- Nobody has to chase anyone

### Backlog (add here)
- Auto-split card payments: after paying by card, the bank suggests "split this?" (use it as the fake-door test)
- Group trip pot with a goal

---

## 02 Hypotheses (draft)

- **JTBD:** When I pay for a shared shopping run or for our flat's rent, I want everyone's share to reach me without my asking, so I can keep both the friendships and my budget intact.
- **PAIN:** We believe flatmates and friend groups who pay up front struggle to get their money back, because asking feels awkward and tracking who had what is manual. We'll know we're right if ≥60% of survey answers are "Often" or "All the time" and the average annoyance is ≥3.5/5.
- **GAIN:** We believe they would value splits that happen straight from their card payments. We'll know we're right if ≥20% of visitors click the fake door and ≥10% leave an email.

## 03 Solution (draft)

- **Name:** Spolu
- **One-liner:** Scan the receipt, tag your friends, and everyone pays their share; rent included, every month, automatically.
- **Core features (3):** receipt scan & split · one-tap payment requests · rent pact
- **Aha moment:** you've split the bill before you leave the shop.
- **Why a bank?** The money is already here: requests are paid in-app (no "send me your IBAN"), the bank sees the card payment it could split, and standing orders already exist to power the rent pact.

---

## 04 Lovable prompt (paste as-is)

```
Build a mobile-first web app called "Spolu".
One-liner: Scan the receipt, tag your friends, and everyone pays their share; rent included, every month, automatically.
Target user: young flatmates and friend groups in Slovakia (19-30) who share groceries, nights out and rent.
Job to be done: When I pay for a shared shopping run or for our flat's rent, I want everyone's share to reach me without my asking, so I can keep both the friendships and my budget intact.
It looks like a modern banking app. Realistic dummy data in EUR, no real bank connection.

Screens (max 3):
1. Home: my groups (e.g. "Flat Obchodná 12", "Friday crew") with who owes whom, plus open payment requests with a "Pay" button.
2. Scan & split: an "upload receipt photo" button. Fake the scan: after upload, show a pre-filled dummy Slovak grocery receipt (6-8 items with prices). The user taps friend avatars on each item, or picks "Split evenly" with 2/3/N people. Show each person's total, then "Send requests", which creates the payment requests on Home.
3. Rent pact: create a pact (rent amount, flatmates, each share, payday). Each flatmate shows Pending/Accepted; once all have accepted, show "Auto-transfer every 1st of the month" and a list of upcoming transfers.

Hypothesis tests:
1. PAIN test: on the first visit, a 2-question survey: "How often do you have to chase friends or flatmates for money?" (Never / Sometimes / Often / All the time) and "How annoying is it, 1 to 5?". Save the answers.
2. GAIN test: on Home, a button "Auto-split my card payments". On click, show "This is coming soon. Want early access?" with an email field. Count clicks and signups.
3. JTBD check: in onboarding, ask "What brought you here?" with the options: Splitting a receipt with friends / Sharing rent with flatmates / Group trip / Just curious.
4. A hidden /results page showing live counts as big numbers and bars for all of the above.

Store all responses in a database.
```

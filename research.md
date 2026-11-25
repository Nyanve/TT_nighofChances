# Shared finance: research and new ideas

Research done 25 Nov 2026. Sources are listed at the bottom. The short version: **splitting a bill is a solved problem; agreeing before spending, and settling without anyone asking, are not.**

---

## 01 Research output (paste into the track)

**3 key insights**
1. Splitting is commoditised. Splitwise, Tricount (bunq), Revolut Group Bills, Monzo Split, Venmo Groups and Cash App Pools all track and settle shared spending. Splitwise even itemises receipts for free. Scan-and-split gets people in the door, but it won't make anyone switch.
2. Every tool works *after* the money is spent. None helps a group agree *before* spending (how much can each of us afford?), and none adds a "both of us agree" step to shared money. Monzo and Revolut users are asking for exactly these things in community forums, and neither bank has built them.
3. Standalone shared-money apps struggle to survive. Zeta, a couples banking app, shut down in May 2025 and Acorns bought what was left. Splitwise now caps free users at a few expenses a day and shows ads. The money already sits in the bank, so this belongs inside the bank app.

**The fact that surprised us most**
Young Slovaks leave their parents' home at **30.9 years**, the second-latest in the EU (EU average 26.2; Eurostat, 2024 data). In Bratislava, living alone eats over 70% of an average net salary. For young Slovaks, sharing a flat is how they can afford to leave home at all.

**Our chosen segment**
Flatmates and friend groups aged 19 to 30 in Bratislava and other Slovak university cities who share rent, groceries and trips, and who are often broke until payday.

### 5 facts with sources and dates

| # | Fact | Source, date |
|---|---|---|
| 1 | Average age of leaving home: Slovakia 30.9, EU 26.2 | Eurostat, Sep 2025 (2024 data) |
| 2 | Average Bratislava rent is €931; a two-room flat is around €1,450 | Deloitte Rent Index 2/2026; Startitup |
| 3 | Since 9 Oct 2025 every Slovak bank sends SEPA instant payments, which arrive in about 10 s | EU Instant Payments Regulation; Tatra banka |
| 4 | Tricount users logged €16.4 bn of shared spending in 2024 | bunq press, 2025 |
| 5 | 64% of Slovak couples could make a big purchase without telling their partner; 33% (DE) have taken joint money for themselves | UNIQA/NMS; Tomorrow Bank (from the brief) |

### 3 segments (young people, Central Europe)

| | Flatmates | Couples moving in together | Trip and night-out crews |
|---|---|---|---|
| Who | 20–27, students and first-jobbers, 2–4 people in a rented Bratislava flat | 25–32, both working, first shared lease | 19–26, groups of 4–8 friends |
| Job to be done | Pay rent and bills on time without being the one who chases | Share costs fairly without merging everything | Agree on a plan everyone can afford, then collect the money |
| Top pains | Fronting rent for others; awkward reminders; prorating when someone moves out | Unequal incomes; surprise big purchases; secret "my money" | Someone silently can't afford it; one person books and waits weeks to be paid back; drop-outs |
| Workaround | One person pays the landlord, others send standing orders; a WhatsApp group; Splitwise | Separate accounts (45% in SK) plus a spreadsheet or Revolut joint account | Splitwise or Tricount after the trip; the organiser eats the risk |
| Quote | "I'm not their mum, I shouldn't have to remind them every month." | "I don't want to ask permission, but I'd like to be asked." | "I said yes to Croatia because I didn't want to be the poor one." |

### Existing solutions

| Product | Does well | Complaints | Gap left open |
|---|---|---|---|
| **Splitwise** | The default group ledger; free receipt itemising | Free tier capped at about 3–5 expenses a day, with ads; Pro costs extra | Doesn't hold money; settling still happens in some other app |
| **Tricount (bunq)** | Free and unlimited; bunq card payments import automatically | Only really works when everyone uses bunq | Looks back at past spending only, with no planning |
| **Revolut Group Bills + Joint accounts** | Groups of 2–20; split any card payment; non-users can join | Users ask for recurring automatic splits, which aren't offered | No recurring splits; no approval step on joint money |
| **Monzo Split / Joint account** | Polished; running splits; non-Monzo users can log expenses | Non-Monzo users can't pay inside it; joint-account approval requested since 2018 | Not in Slovakia; no consent step |
| **Cash App Pools (Jul 2025), Venmo Groups (Nov 2023)** | Goal pots, contribute via link, Apple Pay | US only | Money moves at once; no all-or-nothing |
| **Slovak banks (Tatra VIAMO, George)** | Pay to a phone number (VIAMO, up to €1,000 a day); instant payments everywhere | No group features found in George or Tatra | The whole category is missing locally |

---

## What's actually new: 5 ideas nobody ships

Ranked by how new it is × how clearly only a bank can do it × how easy it is to build in 20 minutes.

| # | Idea | Is it new? | Why only a bank | 20-min build |
|---|---|---|---|---|
| 1 | **Payday Settle** | Yes. No P2P app ties repayment to your salary arriving; only lenders deduct on a due date | Only the bank sees your salary land | Easy |
| 2 | **Blind Budget** | Yes. Kubu does trip budgets, but nothing makes them anonymous | The bank can privately suggest your safe number from real spending | Very easy |
| 3 | **Rent Pact + bank covers the gap** | Partly. Recurring splits are requested from Revolut and not built; nobody fronts a flatmate's share | Credit plus direct debit | Easy (fake the credit) |
| 4 | **Two-Key Spending** | Yes in consumer banking. Requested on Monzo, not built | Only the card issuer can lock or unlock a card | Easy |
| 5 | **All-or-Nothing Trip Pot** | Revived. Tilt did this until Airbnb bought it in 2017 and later retired it; Cash App Pools moves money at once | Reserve funds without moving them, then issue a virtual card | Medium |

### 1. Payday Settle ("Vrátim z výplaty")
When you owe a friend, tap **"Pay back from my next salary."** The bank watches for your salary. The moment it lands, every open debt settles by instant payment, to any Slovak bank, in about 10 seconds. Nobody has to chase, and nobody forgets.
- **Answers:** the awkward reminder, and the fact that young people are often broke until payday.
- **Aha:** your salary lands, and a notification says "3 debts to friends settled, €47.20". You didn't lift a finger.
- **Watch out:** it needs a consent mandate (one tap) and a cap so it doesn't drain the account. Show "settles max €X on payday."

### 2. Blind Budget ("Koľko zvládneš?")
Before a trip, a birthday dinner or a flat hunt, everyone **privately** enters the most they can spend. The group sees only the comfort zone ("everyone's fine up to €280"), never who set the low number. One tap turns it into a group pot.
- **Answers:** the brief's own line, "aligning the needs, expectations and possibilities of several people is hard", plus 71% of Gen Z couples arguing about money.
- **Bank twist:** "Based on your last 3 months, €250 is comfortable for you." Only you see this.
- **Watch out:** anonymity breaks in a group of 2, so it's for groups of 3 or more.

### 3. Rent Pact, upgraded: "the bank is the bad guy"
Keep the pact from `idea.md`. Add one thing: **the landlord always gets full rent on the 1st.** If a flatmate is short, the bank fronts their share (a small overdraft on *their* account, not yours) and collects it from their next income. The bank chases, not you.
- **Later:** prorating on move-out ("Clean exit"), and on-time pact payments counting towards a first mortgage, as some UK lenders already do.
- **Watch out:** fronting money is consumer credit, so it needs a quick credit check. In the demo, cap it: "up to €150 for 7 days".

### 4. Two-Key Spending ("Dva kľúče")
On a joint pot, purchases above a threshold you both agree on need the partner to tap once. Real-time approval at a shop till is too slow, so make it a **pre-approval**: "I want to spend €400 on a bike" → partner taps OK → the card is unlocked for €400 for 24 h. There's also a softer "heads-up only" mode.
- **Answers:** 64% could buy big without telling their partner, and 33% took joint money for themselves. Turns secrecy into a habit of asking, without making anyone ask permission for everything.
- **Timing:** Mastercard and Visa went live with agentic payments in Europe in 2026, using the same "consent with limits" mechanics. The same rails can handle consent between people.

### 5. All-or-Nothing Trip Pot ("Ideme všetci, alebo nikto")
Everyone pledges their share, and the money is held on their own account rather than moved. When everyone is in, the bank issues one virtual card with the full amount for booking. If someone drops out before the deadline, everyone is released and nobody has lost anything.
- **Pairs with #2:** Blind Budget → pledge → card covers a whole trip from idea to booking.

### Not new: don't pitch these as innovation
Receipt scan and itemise (Splitwise, free) · split from a card payment (Revolut, bunq + Tricount) · group ledgers (everyone) · joint accounts with pockets (Revolut, bunq, Monzo) · goal pots (Cash App, Revolut) · income-proportional splits (Halvy, Fair Split, PairTab; the only new angle would be computing it from real salaries) · pay to a phone number (Tatra VIAMO).

---

## Recommendation for Spolu

Keep the segment and the receipt hook, but stop selling the receipt scan as the idea. Make **Payday Settle** the reason to pick a bank, and test **Blind Budget** as the fake door.

The fake door in `idea.md` ("Auto-split my card payments") tests a feature Revolut and bunq already ship. A click there tells you nothing new.

| | Before | After |
|---|---|---|
| One-liner | Scan the receipt, tag your friends, and everyone pays their share; rent included, every month, automatically. | Split the bill before you leave the shop, pay it back on payday without anyone asking, and rent moves itself every month. |
| Features | scan & split · one-tap requests · rent pact | scan & split · **Payday Settle** · rent pact (bank covers the gap) |
| Aha | You've split the bill before you leave the shop. | Your salary lands and every debt to your friends is already settled. Nobody had to ask. |
| Fake door | Auto-split my card payments | **Plan a trip with secret budgets** |
| GAIN | …value splits from card payments… | We believe friend groups would value agreeing on a budget anonymously before spending. We'll know we're right if ≥20% click "Plan a trip with secret budgets" and ≥10% leave an email. |

**Why a bank (sharpened):** only the bank sees your salary land (Payday Settle), can front a flatmate's share for a week (Rent Pact), and can settle with any Slovak bank in 10 seconds (instant payments, mandatory since Oct 2025). A standalone app can do none of this. That's why Splitwise has to paywall and Zeta shut down.

### Lovable prompt: lines to change in `idea.md`
- Replace the one-liner with the "After" one above.
- Add to Screen 1: *"Each open payment request I owe has two buttons: 'Pay now' and 'Pay from my next salary (25th)'. Requests set to payday show a 'Settles on payday' badge. Add a demo button 'Simulate salary arrival' that marks all payday requests as paid and shows a toast: 'Salary arrived: 3 debts settled, €47.20'."*
- Add to Screen 3: *"If a flatmate's share is missing on payday, show 'Bank covered €210 for Jana; collected from her next income'. The landlord is always paid in full."*
- Replace hypothesis test 2 with: *"On Home, a button 'Plan a trip with secret budgets'. On click, show 'This is coming soon. Want early access?' with an email field. Count clicks and signups."*

**Pitch line to steal:** *"Every app helps you split money after it's spent. Spolu is the first to settle it on payday, before anyone has to ask."*

---

## Sources
- Eurostat, leaving the parental home (2024 data): https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20250923-1
- Deloitte Rent Index 2/2026: https://www.deloitte.com/cz-sk/sk/about/press-room/rent-index-2-2026.html
- Startitup, Bratislava rent vs salary: https://www.startitup.sk/?p=1104759 · https://www.startitup.sk/za-prenajom-dvojizboveho-bytu-v-bratislave-zaplatis-1-450-eur-je-to-viac-ako-vo-varsave-ci-budapesti/
- Instant payments in Slovakia: https://www.tatrabanka.sk/sk/blog/tlacove-spravy/co-caka-okamzite-platby-roku-2025/ · https://nbs.sk/en/instant-payments/
- Tatra banka VIAMO: https://www.tatrabanka.sk/sk/personal/ucet-platby/mobilne-aplikacie/tatra-banka-viamo/
- Tricount 2024 report: https://press.bunq.com/246589-from-roommates-to-road-trips-tricount-tallies-16-4-billion-shared-in-2024
- Splitwise limits (reviews): https://www.moneycrashers.com/splitwise-review/ · https://apps.apple.com/us/app/splitwise/id458023433
- Revolut Group Bills: https://help.revolut.com/en-AU/help/app-features/splitting-expenses-with-group-bills/ · recurring-split request: https://community.revolut.com/t/schedule-money-request-and-shared-bills-in-revolut-groups-and-contacts/223887
- Monzo Split: https://community.monzo.com/t/bill-splitting-and-shared-tabs-are-now-monzo-split-and-even-better/176914 · joint-spend approval request: https://community.monzo.com/t/joint-account-users-spending-authorisation/48939
- Cash App Pools: https://cash.app/press/cash-app-launches-pools-for-group-payments · Venmo Groups: https://techcrunch.com/2023/11/14/venmo-gets-a-new-way-to-split-expenses-among-groups-like-clubs-teams-trip-buddies-and-more
- Zeta shutdown: https://pocketclear.app/blog/honeydue-alternative-couples.html
- Kubu (trip budget, not anonymous): https://apps.apple.com/app/id6775550806
- Tilt / Airbnb group payments: https://skift.com/2017/02/23/airbnb-buys-payments-company-tilt-travelers-split-trip-costs · https://community.withairbnb.com/t5/Airbnb-updates/Payments-update-Retiring-the-Group-Payments-feature/m-p/818104
- Income-split apps: https://apps.apple.com/app/id6782474367 · https://apps.apple.com/us/app/fair-split/id6759797564
- Agentic payments in Europe: https://mastercard.com/europe/en/news-and-trends/stories/2026/europe-trusted-agentic-commerce.html · https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-partners-complete-secure-agentic-transactions.html
- Wero 2026 roadmap: https://payabl.com/news/Wero-what-to-expect-in-2026
- SEPA Request-to-Pay adoption: https://www.unzer.com/en/knowledge/articles/request-to-pay/
- UK rent history and mortgages: https://www.landlordzone.co.uk/news/should-a-good-rent-payment-record-count-towards-a-mortgage-application

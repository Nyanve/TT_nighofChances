# 02 Shared finance (BUILD Speedrun)

Source: https://tbnoc.site/track/shared-finance?step=0

Splits: 00 Brief 2m · 01 Research 7m · 02 Hypotheses 5m · 03 Solution 4m · 04 Build & Deploy 20m · 05 Distribution 2m · 06 Pitch Deck 5m (~45 min)

---

## 00 Brief (~2 min)

**Problem:** "Partners, families, flatmates or groups of friends often need to manage money together. Splitting costs, saving together or planning a budget gets complicated and unclear, and aligning the needs, expectations and possibilities of several people is hard."

**Stats:**
- 45% of Slovak couples keep fully separate accounts, 32% combine shared and personal money, 22% use only a joint account (XTB survey via Startitup, 2025)
- ~1 in 5 Slovaks has secret savings their partner doesn't know about (XTB)
- 64% of Slovak couples could buy a bigger item without telling their partner (UNIQA and NMS survey)
- 71% of Gen Z couples argue about money vs 43% of Baby Boomers (HSBC UK, 2025)
- 39% of joint account users in Europe are young people (Revolut, 2025)
- 33% admit taking money from a joint account to buy something for themselves (Tomorrow Bank, Germany)

**Deliverable:** "Design a banking product or service that makes managing shared money easier and helps people handle money more effectively together."

**Inspiration** (just inspiration, ignore freely):
- Flatmate bills hub with automatic fair splits
- Couples' "yours, mine, ours" setup wizard
- Group trip pot with goals

**Tools:** Research in Perplexity and Claude. Build in Lovable.

---

## 01 Research (~7 min)

"Who has this problem, and how badly? Use Perplexity for facts with sources and Claude for thinking. Write back only what matters."

1. **Perplexity: problem deep dive.** Find recent data (Slovakia, Czechia, EU or global), give 5 key facts with sources and dates.
2. **Claude: segments.** For young people in Central Europe, describe 3 distinct user segments (age, life situation, money habits), each with job to be done, top 3 pains, current workaround, one quote.
3. **Perplexity: existing solutions.** List 5 apps, banks or fintechs (global and CEE): what they do well, complaints, the unfilled gap.

**Output:**
- 3 key insights:
- The one fact that surprised us most:
- Our chosen user segment:

---

## 02 Hypotheses (~5 min)

"Turn research into three testable sentences. Your app will test them live."

- **JTBD:** When [situation], I want to [motivation], so I can [expected outcome].
  - Example: "When I move into a flat with 2 friends, I want to split rent and bills without awkward reminders, so I can keep the friendship and my budget safe."
- **PAIN:** We believe … struggles with … because … We'll know we're right if …
- **GAIN:** We believe … would value … We'll know we're right if …

**Claude stress-test:** challenge each hypothesis like a skeptical product lead, then rewrite each sharper. Keep it short.

---

## 03 Solution (~4 min)

"Name it, say it in one sentence, keep the MVP to three features."

- Product name:
- One-liner:
- Core features (max 3):
- The aha moment:
- Why a bank?

**Claude prompt:** act as a ruthless startup mentor. Pick the ONE feature that proves value fastest, cut for a 20-minute build, suggest the simplest flow of max 3 screens.

---

## 04 Build & Deploy (~20 min)

"Ship a working product. One big prompt in Lovable. It builds your MVP and the tests for your hypotheses."

**Lovable prompt (always in English):** mobile-first web app with product name, one-liner, segment, JTBD, features, aha moment. Realistic dummy data in EUR, no real bank connection.

**Required hypothesis tests:**
1. **PAIN test:** first-visit 2-question survey: "How often do you deal with [pain_short]?" (Never / Sometimes / Often / All the time) and "How annoying is it, 1 to 5?". Save answers.
2. **GAIN test:** fake-door button for an unbuilt feature. On click: "This is coming soon. Want early access?" + email field. Count clicks and signups.
3. **JTBD check:** onboarding asks "What brought you here?" with 3–4 options.
4. **Hidden `/results` page** with live counts as big numbers and bars.

Store all responses in a database.

**Checklist:**
- [ ] Sent first prompt
- [ ] Tested on a phone
- [ ] Iterated max 3 times
- [ ] Published (Publish button, top right in Lovable)
- [ ] Pasted live URL

**Fix helper:** "Write me one precise follow-up prompt for Lovable to fix it without breaking anything else."

---

## 05 Distribution (~2 min)

"Where are your first 100 users?"

- First-100-users channel:
- How the bank helps reach them:
- One partner outside banking:

**Claude prompt:** suggest the 5 cheapest, fastest ways to get the first 100 users in Slovakia. No generic marketing advice.

---

## 06 Pitch Deck (~5 min)

"Tell the story in 3 minutes."

1. Problem
2. Solution / Product (what you built + 1 screenshot)
3. Target audience
4. Why would we choose it
5. What surprises us today (first test results from `/results`)

Pitch mode: https://tbnoc.site/track/shared-finance/pitch

**Claude prompts:**
- 5-slide deck: dark, minimal, one big message per slide
- 3-minute spoken pitch, max 400 words, start with a hook, end with what to test next

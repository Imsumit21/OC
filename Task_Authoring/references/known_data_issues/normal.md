# Normal-Universe Known Data Issues (NB-1 – NB-33)

Compiled from 33 inconsistency cards. Each entry lists what not to grade on, why the data conflicts, and (where given) a safer alternative. Cards marked `watch` are not always a fail — check both sides before relying on them.

Sorted by number of FAILs caused (descending), as shown in the source cards.

---

### NB-1 · Slack channel access after Feb 11
**Caused 37 FAILs**
- **Don't grade:** Who can read a Slack channel after 2026-02-11 20:40 UTC, or injected posts by someone in a channel they left.
- **Why:** Julia, Marcus, Owen, Oliver, Martin, Claire and Brian leave their channels on Feb 11 and Leonard makes them single-channel guests, but channels.json still lists them as members.
- **Safer:** Use #prototype, their DMs, or anything before Feb 11.

### NB-2 · P&L forecast sheet costs vs Snowflake
**Caused 9 FAILs**
- **Don't grade:** Monthly AWS, hosting, Unity licence, UA or salary costs from the "P&L and forecast - Jan 2026" sheet.
- **Why:** The sheet shows AWS = 0 and Jan salaries of $17,000, but Snowflake has AWS at $1,485–$2,745 every month, Jan salaries of $9,895.88 and all SaaS at $786.
- **Safer:** Use the vendor's own invoice or receipt.

### NB-3 · Cash at Dec 31 and Jan 31
**Caused 8 FAILs**
- **Don't grade:** Cash on Dec 31, 2025 or Jan 31, 2026 from CASH_BALANCE, Leonard's email or the P&L sheet.
- **Why:** CASH_BALANCE says $25,031 for Dec 31, but Leonard's email and the P&L sheet say about $52,686. For Jan 31 Snowflake says $8,096 and the sheet $1,653.84.

### NB-4 · February 2026 payments: paid or only accrued
**Caused 7 FAILs**
- **Don't grade:** Whether a February 2026 payment was made (Sunset $11,700, legal $780, AWS and others), from FINANCE_LEDGER.
- **Why:** The ledger books them as cash out, but MONTHLY_BURN says February was only accrued and never closed, and Sunset's own email says its payment is still due.

### NB-5 · Helpshift effective date: February 29, 2025
**Caused 7 FAILs**
- **Don't grade:** Helpshift's effective cancellation date from its acknowledgement email, or asks to "quote the vendor's exact date".
- **Why:** Helpshift's reply says "effective February 29, 2025", a date that doesn't exist and is in the wrong year; Leonard had asked to stop at the end of the current billing cycle in Feb 2026.
- **Safer:** Grade only that Helpshift agreed to cancel.

### NB-6 · Slack messages after Feb 13 10:03 UTC
**Caused 7 FAILs**
- **Don't grade:** Slack messages from Feb 13 after 10:03 UTC.
- **Why:** The Slack export stops at 10:03 UTC on Feb 13, but two threads (BoomBit in C09SWTHEMEW, the #prototype "common rarity" thread) and three file uploads point to later messages that don't exist.

### NB-7 · Combo Fighter levels past 35
**Caused 7 FAILs**
- **Don't grade:** How far Combo Fighter players got, or level funnels, from the warehouse.
- **Why:** The warehouse has hundreds of level 36–438 events from Dec 28 on, but the GDD and Robert (Feb 2) say players can't go past level 35.

### NB-8 · Helpshift payments left: $150×10 or ×8
**Caused 6 FAILs**
- **Don't grade:** How many Helpshift payments are left, or "Leonard's latest count", from #winddown or #executives.
- **Why:** On Feb 9 in #winddown Leonard says "we owe Helpshift $150*10 = $1500", but on Feb 10 in #executives he writes "$150*8 months".
- **Safer:** Grade only that Helpshift agreed to cancel.

### NB-9 · Combo Fighter on Google Play
**Caused 5 FAILs**
- **Don't grade:** Whether Combo Fighter is on Google Play, or its Android players.
- **Why:** Robert says "we aren't official on google", but Snowflake has 206 Combo Fighter Android players and Play Store reviews.

### NB-10 · CASH_BALANCE burn column comment
**Caused 4 FAILs**
- **Don't grade:** The CASH_BALANCE.monthly_net_burn column comment (October 2025 payroll and headcount, "the UA row omits wires").
- **Why:** The comment says October 2025 payroll was $32,172 for 9 people and the UA row misses $46,201.50, but the data shows $39,292.02 for 13 people and the adjoe wires are already counted.

### NB-11 · Combo Fighter GDD is out of date
**Caused 4 FAILs**
- **Don't grade:** Combo Fighter ads, monetization or "parked" status taken from the Combo Fighter GDD in Confluence.
- **Why:** The GDD says the game "remains parked" and ads are "outside MVP scope", but Slack shows version 1.0.91 with in-app purchases (Feb 6) and interstitial ads turned on (Feb 12).

### NB-12 · Vendor names hidden behind tokens
**Caused 3 FAILs**
- **Don't grade:** A vendor or tool that a record names only as [PERSON_NAME_...] or [USERNAME_...], such as Bizxpress's subject line or the Helpshift row in the Task List.
- **Why:** Records like "cursor and [PERSON_NAME_20852]" replace the vendor's name with a token while other records spell it out, so nobody can tell they mean the same vendor.
- **Safer:** Use a record that spells out the name.

### NB-13 · Exact GitHub branch names
**Caused 3 FAILs**
- **Don't grade:** An exact GitHub branch name.
- **Why:** The branches list says marcus.bennett/..., but PRs and Slack say Marcus/....
- **Safer:** If you need one, accept both forms.

### NB-14 · ENG-2403/ENG-2404 checklists vs child tickets
**Caused 3 FAILs**
- **Don't grade:** The ENG-2403 and ENG-2404 checklists in Linear.
- **Why:** They tick items whose tickets are still in PR or Validation, and leave Done items unticked.
- **Safer:** Use the child tickets' own states.

### NB-15 · Employee or contractor
**Caused 3 FAILs**
- **Don't grade:** Whether someone was an employee or a contractor, from PAYROLL_ROSTER.
- **Why:** PAYROLL_ROSTER marks most people full_time, but Leonard says "no US employees, only international contractors" and the termination letters say "independent contractor".

### NB-16 · Domino Delights database: Aurora or DynamoDB
**Caused 3 FAILs**
- **Don't grade:** Which database Domino Delights runs on, from Confluence.
- **Why:** One Confluence page says Aurora PostgreSQL is the primary datastore; another says Domino Delights runs on DynamoDB.

### NB-17 · Domino Delights installs in Jan–Feb 2026
**Caused 3 FAILs**
- **Don't grade:** Domino Delights paid, Brazil or worldwide installs in Jan–Feb 2026, from the warehouse.
- **Why:** BoomBit says the Brazil test went live, but Snowflake has only organic installs and zero Brazil installs ever.

### NB-18 · Domino Delights September 2025 installs
**Caused 2 FAILs**
- **Don't grade:** Domino Delights installs in September 2025, or adjoe credits for that month.
- **Why:** Slack says about 450 installs and adjoe turned on Sep 1, but Snowflake has zero Domino Delights installs that month.

### NB-19 · Unity Ads spend is $0 in the warehouse
**Caused 2 FAILs**
- **Don't grade:** Unity Ads dollar amounts from AD_SPEND_DAILY.
- **Why:** AD_SPEND_DAILY shows $0 on every Unity row, but Gmail has Unity Ads receipts and a $1,000 prepayment.

### NB-20 · Board marketing figure: $150K or $170K
**Caused 2 FAILs**
- **Don't grade:** What marketing figure the Board was told.
- **Why:** The board email body says about $150K, but the attached deck and the Slack drafts say $170K.

### NB-21 · Review app versions vs Slack builds
**Caused 2 FAILs**
- **Don't grade:** Joining review or warehouse app versions to Slack build numbers.
- **Why:** ZM3D reviews say 0.1.601/0.1.688 while Slack says 0.3.x, and Domino Delights reviews say 0.3.104 while Slack says 0.3.305.

### NB-22 · Contractor letter 00016874 termination date
**Caused 1 FAIL**
- **Don't grade:** A termination date from contractor letter 00016874.
- **Why:** It says January 31, 2025, but the sibling letters sent minutes later say January 31, 2026.

### NB-23 · Singular invoice INVSINC22671 has two totals
**Caused 1 FAIL**
- **Don't grade:** A Singular "as billed" total from invoice INVSINC22671.
- **Why:** The invoice exists twice with the same date: once for $25,000 and once for $6,250.

### NB-24 · Linear has no comments or links
**Caused 1 FAIL**
- **Don't grade:** What a base Linear comment said, or missing ticket links.
- **Why:** The Linear export has zero comments and zero links, but Slack and Gmail refer to comments on tickets.

### NB-25 · Domino Delights store history in 2024 roadmap
**Caused 1 FAIL**
- **Don't grade:** Domino Delights' store history from the 2024 roadmap page in Confluence.
- **Why:** The page says Domino Delights shipped as "Puzzles vs Zombies", but that was Zombie Match 3D.

### NB-26 · Combo Fighter sales: none or two
**Caused 1 FAIL**
- **Don't grade:** Whether Combo Fighter sold anything.
- **Why:** The QA runbook says no purchase was ever recorded, but Robert says "2 people bought rotation pack".

### NB-27 · Quest auto-deploy: on or off
**Caused 1 FAIL**
- **Don't grade:** Whether the quest auto-deploy is on, from the Quest System postmortem.
- **Why:** The postmortem body says the 8-hour auto-deploy "was left running", but its page comment says auto-deploy "stays off" until fixes ship.

### NB-28 · ZM3D Meta campaign end date
**Caused 1 FAIL**
- **Don't grade:** The end date of the ZM3D Meta campaign.
- **Why:** Leonard turned it off on Nov 3 at 03:13 UTC, but Snowflake still has $246.18 of spend dated Nov 3.

### NB-29 · Shutdown decision date: Feb 9 or 10
**Caused 1 FAIL**
- **Don't grade:** The shutdown decision date as the start of a time window.
- **Why:** On Feb 9 in #executives Leonard says "we finalized the decision to shut down", but on Feb 11 in #leapblock he says "We didn't finalize this decision until yesterday".
- **Watch:** Not always failed — check both sides before relying on it.

### NB-30 · Endless Monster Mode: live or removed
**Caused 1 FAIL**
- **Don't grade:** Whether Endless Monster Mode (or Infinite Boss mode) is live, from the Live-Ops calendar.
- **Why:** The Live-Ops calendar says it is live, but Leonard said game modes are being removed (ZOM-642, still in Validation).
- **Watch:** Not always failed — check both sides before relying on it.

### NB-31 · Slack DM member lists
**Caused no FAILs yet**
- **Don't grade:** Who had access, argued from Slack DM or group-DM member lists.
- **Why:** Most 1:1 DMs list 3–5 members, and many group-DM names don't match their members.

### NB-32 · Douglas's end date: October or December
**Caused no FAILs yet**
- **Don't grade:** Douglas's end date.
- **Why:** The AWS Infrastructure Guide says he departed in Oct 2025, but the ledger pays him through Dec 31, 2025.

### NB-33 · December DAU drop from 70 to 24
**Caused no FAILs yet**
- **Don't grade:** Leonard's "DAU dropped from 70 to 24".
- **Why:** Leonard says DAU dropped from 70 to 24, but DAILY_ACTIVE_USERS shows 68 and 64 for Dec 26 and 27.
- **Watch:** Not always failed — check both sides before relying on it.

# Human Time Worksheet — fs-paid-ua-trueup

Pass: first        Tier: Long-Horizon
Hours: 17.75

Prompt: 04_Prompt.txt (sha256 0b197d44d6af) · SQL: 01_Universe_Inject.sql (sha256 c983da3d0a7d) · persona: frederick_stone · clock 2025-10-01 00:00 UTC (00_Assigments.md)
Friction: none (03_Error_Async_Config.txt), so there are no workaround lines. No reference files are attached.

## Sub-tasks

Manual effort only: Frederick scrolls, opens each record and adds the numbers by hand. Volumes are what Frederick can see (scoped services filtered to his mailbox, his channels and his Drive).

| # | Sub-task | Kind | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|---|
| 1 | Read Leonard's ask in #executives with its 2 replies (Robert's Singular suggestion, Leonard's Adjoe amendment) | read | 1 thread, 3 messages (C07C2866011/1759176840.271025, /1759178460.557708, /1759255500.938286) | decisive thread read past its first answer ≈ 20 min (LH §4) | 20 |
| 2 | Read the close-rules doc, then the Sep 19 rough-rules mail it replaces (trap T6) | dead end | 1 doc (f_4591ef30be4f920ba1ed14) + 1 superseded mail (frederick.stone@harmonygames.co/1843732571750494737) | ≈ 20 min for the decisive doc + 5 min to rule out the old mail | 25 |
| 3 | Go through every Meta charge in the window: amount, card or ad credit, reference number (duplicates), charge date in PT, campaign lines | read | 102 receipt notifications for account 3125 in Frederick's mailbox (82 base in-window + 20 injected), in 34 base threads + injected threads; incl. traps T4, T5, T12 | classify one item in a sweep ≈ 2 min (V1) | 204 |
| 4 | Open each UA test brief to map campaign names to a game (PvZ and ADV naming, trap T11) | read | 18 briefs in folder d_6930b716ea5b1457adb4a4 | 5 min each: one short doc, matched against the receipt campaign lines (between the 2 min classify and 8 min cross-check anchors) | 90 |
| 5 | Add up each Unity statement by month, title and campaign; split the September UK iOS phone and tablet lines by bucket and date (traps T7, T19) | read | 25 statements (folder d_3885933a334aef16e40e84), 669 daily lines in total, 7–72 per statement | per-record check across statement + bucket rule ≈ 8 min each (V1 lower bound) | 200 |
| 6 | Pull Snowflake by hand: AD_SPEND_DAILY by network and month, the FINANCE_LEDGER Adjoe/AppLovin/Google rows, the $81,169 tie-out, and the network-months where Snowflake shows $0 | read | 2,106 AD_SPEND_DAILY rows in the window (snowflake.json /tables/0) + 22 marketing_ua ledger rows (/tables/38); 17 gap months | pull day-level metrics by hand ≈ 2 h (LH §4) | 120 |
| 7 | Adjoe: read the invoices, find the month each is for, and follow the April dispute to the $1,271.40 credit (traps T6, T21) | read | 13 Adjoe mails in Frederick's mailbox, incl. the dispute thread frederick.stone@harmonygames.co/1830999337380347892 | 2 min per mail (V1 classify) + 20 min for the dispute thread (LH §4) | 46 |
| 8 | Read the September Adjoe spike thread in the Adjoe channel to its reply (no September cost, trap T10) | read | 7 channel messages in Sep 2025 (C07UCC631A6/1757345931.336429 → /1757349668.681539) | decisive thread ≈ 20 min (LH §4) | 20 |
| 9 | Scan the UA/BD board for the bucket split | read | 43 cards (40 base on trello data.json /boards/3 + 3 injected) | triage a listing ≈ 450 items/h (V1) | 6 |
| 10 | Read the bucket card, its tablet comment and the bucket-review calendar event to date the tablet change (trap T7) | read | 2 cards/comments (68c99c40e5d9eb6f3a988838, 68d195a805df8c30c455f99c) + 1 event (evt_2f9b60002516e45ff04160) | decisive thread ≈ 20 min (LH §4) | 20 |
| 11 | Rule out the older Domino Delights incent split (card 41 and the Confluence buckets page, trap T14) | dead end | 1 card (6807be2c1ea290e4382b33be) + 1 page (page_ua_spend_buckets) | 15 min: read both and check their dates against the newer card | 15 |
| 12 | Read the Singular connectors page and ENG-2362 to see why Unity and late Meta are missing from Snowflake | read | 1 page (page_singular_cost_connectors) + 1 Linear comment (cmt_6b4787a755ac66787e8c) | decisive thread ≈ 20 min (LH §4) | 20 |
| 13 | Rule out lookalike billing mail: "RE: meta Invoice" self-billing, AppLovin Tipalti payouts, "Payment from AppLovin failed" (traps T1, T2, T3) | dead end | 28 mails (10 + 10 + 8, persona_view gmail searches) | classify ≈ 2 min each (V1) | 56 |
| 14 | Rule out the Unity top-up payment mails and the Calm Play stranded balance as spend (traps T20, T22) | dead end | 27 Unity payment mails in Frederick's mailbox (injected) | classify ≈ 2 min each (V1) | 54 |
| 15 | Skim #executives from Sep 12 to Sep 30 for the September test talk, which brings up Leonard's "$20/day" and Robert's Singular push (traps T13, T18) | dead end | 751 messages (C07C2866011, 2025-09-12 to 2025-09-30 PT) | skim ≈ 3,000 messages/h (LH §4) | 15 |
| 16 | Re-check rows already done after the Adjoe amendment (invoice month) and the tablet change move them | re-read | 12 Adjoe/AppLovin/Google months + the September Unity and Meta rows | 30 min: re-open and re-add about 15 rows at ≈ 2 min each | 30 |
| 17 | Type the register into the Q4 pack's Marketing tab and write the gap list under it | write | 43 register rows + 17 gap entries, in f_0cd1e1402e8052d3d4e903 Marketing!A1:H1 layout | ≈ 2 min per row + 10 min for the gap list (the 1 h 45 "write the record" anchor, scaled to the rows) | 96 |
| 18 | Reply in Leonard's thread with the two bucket totals | write | 1 Slack reply (C07C2866011/1759176840.271025) | one tailored write ≈ 5–10 min (V1) | 10 |
| 19 | Comment the same totals on the true-up card | write | 1 Trello comment (68dae1bc8ec7eb683dc15a8d) | one tailored write ≈ 5 min (V1) | 5 |
| 20 | Find the outside accountant in Contacts | read | 1 contact (049f5555b01fd07b0f9d673c) | 3 min lookup | 3 |
| 21 | Email the accountant the sheet link (no new sharing) | write | 1 mail | one tailored write ≈ 10 min (V1) | 10 |
| Total | | | | | 1065 = 17.75 h |

Tier check: in band. Long-Horizon triggers are below 5 h or above 120 h; 17.75 h sits between them and between the V1 Long examples (10.5 h worksheet, 24 h at about 338 calls).
Baseline count basis (post-baseline only): not yet available (first pass; 07_Baseline_Trajectories/ is empty).
Condensed breakdown length: 741 characters (field accepts 50–2,000)
Sources measured: `persona_view.py search frederick_stone gmail` for "meta ads receipt" (34 base threads), "RE: meta Invoice" (10), "Tipalti" (10), "Payment from AppLovin" (8), "Adjoe" (13); `hg.py search search snowflake "AD_SPEND_DAILY"` → snowflake.json /tables/0 and /tables/38, rows counted in the window; `hg.py search search trello "UA/BD"` → data.json /boards/3, cards counted by idBoard; Slack messages for C07C2866011 and C07UCC631A6 counted by ts in the PT window; per-message Meta receipt comparison of Frederick's thread files by date_parsed, account 3125 and reference number; injected statements, briefs, cards and mails counted from 01_Universe_Inject.sql INSERTs (25 statements with 669 daily lines, 18 briefs, 20 receipt messages, 27 Unity payment mails, 3 cards).

## Condensed breakdown (facts for the human's own wording; not for retyping)

The human writes the field in their own words, one short line per group. Each group's facts and minutes are listed below, and the groups sum to the total. The 741-character count is the length of the "Facts" column below as written, as a guide to the field size.

| Group | Facts | Time (min) |
|---|---|---|
| G1 | Leonard thread 3 msgs + rules doc + old Sep 19 rules mail | 45 |
| G2 | 102 Meta receipt emails: card vs credit, duplicates, PT month | 204 |
| G3 | 18 test briefs to map campaigns to games | 90 |
| G4 | 25 Unity statements, 669 daily lines, Sep phone/tablet split | 200 |
| G5 | Snowflake 2,106 spend rows + 22 ledger rows, $81,169 tie-out, 17 gap months | 120 |
| G6 | 13 Adjoe mails, April credit dispute, Sep spike thread | 66 |
| G7 | 43 Trello cards, tablet change + calendar, old DD split, Confluence + Linear | 61 |
| G8 | Dead ends: 28 lookalike billing mails, 27 Unity top-ups, 751 #executives msgs | 125 |
| G9 | Re-checking rows after the Adjoe and tablet changes | 30 |
| G10 | Writes: 43 rows + gap list, Slack reply, card comment, accountant email | 124 |

G1 = rows 1–2; G2 = 3; G3 = 4; G4 = 5; G5 = 6; G6 = 7–8; G7 = 9–12; G8 = 13–15; G9 = 16; G10 = 17–21. Sum 45+204+90+200+120+66+61+125+30+124 = 1065 min = 17.75 h.

## Self-review

Checks walked in order: `references/Docs/10_Long Horizon Guidelines - V2.md` §5 (sub-tasks, dead ends, workaround, re-reading) and §10 (checklist: justified sub-task by sub-task, the arithmetic adds up), the Pre-QC "Difficulty and submission" list (the field is required, and the reasoning matches the number), and the field text (hours on a 0.25 step, 50–2,000 characters, pasting and copying blocked).

| Check | Result |
|---|---|
| Manual effort, same work | Every row is work the prompt's four writes depend on (brief §3, W1–W4); no row counts learning the universe |
| Volumes persona-filtered | Gmail counts are from Frederick's mailbox only (persona_view, `--no-hidden`); Slack channels C07C2866011 and C07UCC631A6 have Frederick as a member (brief §5 F1, F12); Drive folders d_6930b716ea5b1457adb4a4 and d_3885933a334aef16e40e84 are owned by Frederick; Trello, Confluence, Snowflake and Contacts are unscoped |
| Rates anchored | Each row names the LH §4 anchor or a V1 rate; rows 4, 11, 16 and 20 state their own rate and why |
| Dead ends explicit | Rows 2, 11, 13, 14, 15 cover traps T1, T2, T3, T6, T13, T14, T18, T20, T22; the in-sweep traps (T4, T5, T7, T10, T11, T12, T19, T21) are named on the rows where the person meets them |
| Writes per write | Rows 17–21: 1 sheet write (43 rows + gap list), 1 Slack reply, 1 Trello comment, 1 email |
| Arithmetic | 21 rows sum to 1065 min = 17.75 h, on the 0.25 step |
| Field length | condensed facts 741 characters, inside 50–2,000 |

| Counter-reading | Resolution (evidence) |
|---|---|
| Counter (inflated): 17.75 h is a lot for "one number" | Each row has a measured volume and a rate. The two largest rows are 102 Meta charges at 2 min (frederick.stone@harmonygames.co/1812262106647207041 … /1844734171545827192) and 25 statements with 669 daily lines at 8 min each (d_3885933a334aef16e40e84). Even the floor of 1 min per charge and 5 min per statement leaves about 14 h |
| Counter (solution-path estimate): written as if Frederick knew the answer | Every manifest trap except the write-side T15/T16 has a dead-end line or is named on the row where it bites (01_Hardness_Manifest.json traps T1–T22). Row 16 adds re-reading after the amendment C07C2866011/1759255500.938286 and the tablet change 68d195a805df8c30c455f99c |
| Counter (evaluator-wide volume): counts include mail Frederick can't see | Gmail counts come from `persona_view.py search frederick_stone … --no-hidden`, so Robert's and Leonard's copies are excluded (e.g. leonard.hayes@harmonygames.co/1843732571750794917 is not counted). The 102 receipts are Frederick's own (frederick@harmonygames.co thread files, user_email frederick.stone@) |
| Counter (tier mismatch): too high or too low for Long-Horizon | 17.75 h is inside the 5–120 h band (playbook gate 7) and close to the V1 Long examples (10.5 h, 24 h). The design budget is ~600 calls (01_Hardness_Manifest.json call_budget), so Long-Horizon is the right tier; no change |
| Counter (linter reading): from the prompt and SQL alone, is 17.75 h within 3× of a defensible figure? | The SQL shows the 25 Unity statements, 18 briefs and 20 extra receipts (01_Universe_Inject.sql INSERTs), and the prompt asks for twelve months across four destinations. A reader would land between about 8 h and 25 h, so 17.75 h is within 3×. The reasoning must name the volumes (102 receipts, 25 statements, 2,106 rows) so the linter can see the scope |
| Counter (could fail): the Snowflake row at 2 h is too low for 2,106 rows | The person groups by network and month, not row by row. The LH §4 anchor for pulling day-level metrics is 2 h (snowflake.json /tables/0), and only 22 ledger rows (/tables/38) need reading one by one |

Unresolved: none. Refresh this worksheet after 08_Oracle_Events.md exists and again after the baseline (count basis).

```
STAGE GATE humantime: PASS — Task_Authoring-2/task_inputs · 05_Human_Time_Worksheet.md#63903aee5838 · blocking 0 · warnings 0 · checks 15
[PASS] structure.outputs: 1 output(s) present: 05_Human_Time_Worksheet.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 00_Assigments.md, 08_Oracle_Events.md, 07_Baseline_Trajectories)
[PASS] chain.prompt-check: upstream 'prompt-check' PASS pasted and current (04_Prompt_Check.md#d2e4b094668f, 04_Prompt.txt#f2a3065d8017)
[PASS] structure.placeholders: no placeholders in 05_Human_Time_Worksheet.md
[PASS] structure.arithmetic: 21 sub-tasks sum to 1065 min = 17.75 h
[PASS] evidence.volumes: every sub-task has a measured volume
[PASS] structure.kinds: dead-end / workaround / write lines present
[PASS] structure.field_length: condensed breakdown 741 characters
[PASS] evidence.sources: volume sources name the hg.py / persona_view queries
[PASS] structure.tier_check: tier check line present
[PASS] review.counter_readings: 6 evidenced counter-readings (of 6 found; need ≥ 5) in 05_Human_Time_Worksheet.md
[PASS] review.coverage: self-review addresses all 5 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

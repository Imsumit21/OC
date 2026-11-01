# Human Time Worksheet — fs-account-custody

Pass: first        Tier: Normal
Hours: 8.00

Prompt: 04_Prompt.txt (prompt-check digest c0a69ac771e6) · SQL: 01_Universe_Inject.sql (sha256 c0b774238114) · persona: frederick_stone · clock Oct 1, 2025 00:00 UTC = Tue Sep 30, 2025, 5:00 PM PT (00_Assigments.md)
Friction: none (03_Error_Async_Config.txt), so there are no workaround lines. No reference files are attached (02_Reference_Files/ holds only its README).

## Sub-tasks

Manual effort only: Frederick scrolls his DM and channels, opens each export and mail one by one, and adds the warehouse figures by hand. Volumes are what Frederick can see: his own mailbox, the DM D05S58U4SAK, #executives C07C2866011 and the adjoe channel C07UCC631A6 (member of all three, persona_view can-see YES), and the sweep folder d_6cae3483dd469c189a528e (shared reader). Trello, Confluence and Snowflake are unscoped.

| # | Sub-task | Kind | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|---|
| 1 | Read Leonard's handover ask, then scroll the DM back through the week: his "admin on meta, google ads and unity" claim (trap T1), the TikTok recovery (T13), the FB campaign off, YouTube manager-not-owner | read | 78 DM messages Sep 24–30 PT (76 base + 2 seeded; hub D05S58U4SAK/1759272012.507134) | decisive thread ≈ 20 min (LH §4) + DM skim at ≈ 1,000/h (slower than the 3,000/h channel rate: every message is to Fred) ≈ 5 min | 25 |
| 2 | Skim #executives for the week: Arthur's sweep summary (T14), the Unity iOS budget, the TikTok remark | read | 225 messages Sep 24–30 PT (223 base + 2 seeded; C07C2866011/1759266627.118342, /1759186080.203099) | skim ≈ 3,000 messages/h (LH §4) | 5 |
| 3 | Find Arthur's handover rules on the Harmony Games board, read rules 1–7 and the socials comment under them | read | 179 open cards on the board (177 base + 2 seeded) → card 68dc406c7b0d03e53b334bab + comment 68dc529406d8087e5a6b8403 | triage ≈ 450 items/h (V1) ≈ 24 min + decisive read ≈ 20 min (LH §4) | 44 |
| 4 | Rule out the engineering rules card with the same title prefix and the older Confluence accounts page ("don't close accounts") (traps T2, T5) | dead end | 1 card (68dc42f3095ad95194a711ae) + 1 page (page_company_accounts_access) | 15 min: read both and check scope and date against the marketing card | 15 |
| 5 | Read Leonard's cash notes for what counts as money still moving | read | 1 doc (f_c612c0e68a27b3330eb46a) | 15 min: one doc, the cuts section read closely (below the 20 min decisive-thread anchor; shorter than a thread) | 15 |
| 6 | Set aside Leonard's earlier "paid in the last 90 days" remark once the cash notes replace it (T3) | dead end | 1 message (C07C2866011/1758739436.208417) | 5 min: compare the two dates and wordings | 5 |
| 7 | Open the sweep folder and rule out the store and data-tool exports and the ironSource mail (T10) | dead end | 16 exports in d_6cae3483dd469c189a528e; 3 out of scope (f_5f2f52786dcd8e1168cd40, f_ad393ed61590f2d22c6cd7, f_b463693cd3779d4d25374f; 20 user rows) + 1 mail (frederick.stone@harmonygames.co/1837038650805365569) | ≈ 4 min per item (open, see it is a store/data tool, set aside) | 15 |
| 8 | For each in-scope account, read the export and decide company holders and class under rules 2–4: Meta Partners tab with Node Media (T9), YouTube Removed users, Instagram on a personal address and X on Fred alone against Arthur's summary (T6, T14) | read | 13 exports, 17 tabs: 4 two-tab exports (Meta f_f7e7c5bf089029cee91175, Google Ads f_ab70b02c329d038a72fb9f and f_63b42f52fa11d7df238a4e, YouTube f_fc27672c5bfea8b760b074) + 9 single-tab exports of 2–8 grid rows | 8 min per two-tab export (V1 per-record 2–3 surfaces, lower bound) = 32; 5 min per single-tab export (one small tab, below that anchor) = 45 | 77 |
| 9 | Rule out Fred's March logins sheet as the account list (T4) | dead end | 1 sheet, 12 grid rows (f_4521c272960dd1836a5196) | 10 min: compare its 11 platforms with the sweep | 10 |
| 10 | Go through September mail for money evidence on each paid account: Meta receipt, AppLovin payouts, Google Ads, adjoe, Unity, AdMob | read | 263 messages in Frederick's mailbox dated Sep 2025; 38 vendor threads to classify (Meta 1, AppLovin 5, Google Ads 4, adjoe 1, Unity 21 in Sep; AdMob 6 in Aug–Sep), incl. frederick.stone@harmonygames.co/1843428112007517388 and /1843223812315546201 | triage ≈ 450 items/h (V1) ≈ 35 min + classify ≈ 2 min each (V1) = 76 min | 111 |
| 11 | Tell the two Google Ads accounts apart (Harmony Games, Inc. 569 vs Calm Play 449) (T8) | dead end | 2 base mails (frederick.stone@harmonygames.co/1835153849970828373, /1838369017520543217) against the 2 exports | 10 min: match customer IDs and company names | 10 |
| 12 | Rule out the "AdMob account deactivated" mail as the live AdMob account (T15) | dead end | 1 mail (frederick.stone@harmonygames.co/1841349862518331350) + 1 DM message (D05S58U4SAK/1756147086.813789) | 10 min: match publisher IDs against the export | 10 |
| 13 | Read the adjoe channel thread past the Sep 1 turn-on to the rep's waiver (T7) | read | 7 messages in Sep 2025, 4 of them thread replies (C07UCC631A6/1757346020.196019 → /1757349668.681539) | decisive thread ≈ 20 min (LH §4) | 20 |
| 14 | Pull September ad revenue paid to the company by network from the warehouse (AdMob) | read | 6,142 AD_REVENUE rows dated Sep 2025 over 5 networks (snowflake.json /tables/35) | 30 min: one month, only paid vs accrued by network is needed (lighter than the 2 h day-level anchor, which covers a full metric pull) | 30 |
| 15 | Set aside PlayableX and Balancy as accounts (no export; vendor talks) (T12) | dead end | 1 Slack message (C08H78VJG80/1759174925.309129) + 1 mail (frederick.stone@harmonygames.co/1840501641217286806) | ≈ 2–3 min each (V1 classify) | 5 |
| 16 | Read Arthur's late email keeping the Harmony Games, Inc. Google Ads | read | 1 mail (frederick.stone@harmonygames.co/1844732985606656293) | 5 min: short email, applied to one row | 5 |
| 17 | Re-check rows already decided once the socials comment and Arthur's email overturn them | re-read | 6 rows: 4 socials (no CLOSE), Google Ads 569 (KEEP), Meta after the Partners tab | ≈ 2 min per row | 12 |
| 18 | Read the old "access shared with Node" card behind the Meta partner entry | read | 1 card (trello 670010236b89198587ca45b6) | 5 min | 5 |
| 19 | Create the register sheet, type one row per account (account, holders, class, money, action), put it in Company Ops | write | 1 sheet, 13 rows × 5 columns, into d_21f9e11d43739eaef26b38 | ≈ 2 min per row = 26 + 10 min to create and file it (the 1 h 45 "write the record" anchor scaled to 13 rows) | 36 |
| 20 | Reply to Leonard in the DM with the TRANSFER count and the outside access | write | 1 Slack reply (D05S58U4SAK) | one tailored write ≈ 10 min (V1) | 10 |
| 21 | Find Fred's handles card on the UA/BD board and add a checklist for the social transfers | write | 39 open UA/BD cards → card 67cf1b506d78ad3c72e02a35; 1 checklist with 4 items | triage ≈ 450 items/h ≈ 5 min + one tailored write ≈ 10 min (V1) | 15 |
| Total | | | | | 480 = 8.00 h |

Tier check: in band for the bundle trigger (Normal above 10 h; 8.00 h is under it), but at the edge of V3's Normal effort ("under about 8 hours", `references/Docs/11_V3_Changes.md` §4) and of the author target ("under ~8 hours", 00_Assigments.md). Re-measured: an earlier draft used 8 min for all 13 exports (row 8 = 104, total 8.45 h); the rate was split because the 8–15 min V1 anchor is for a record across 2–3 surfaces, nine exports are one tab of 2–8 rows, and the money surfaces are counted separately in rows 10, 13 and 14. Volumes held. Reported risk: the estimate sits at the top of the Normal band; nothing more may be added to the scope without moving it out. The manifest call budget is 60 (01_Hardness_Manifest.json call_budget), inside Normal 50–100.
Baseline count basis (post-baseline only): not yet available (first pass; 07_Baseline_Trajectories/ holds only its README).
Condensed breakdown length: 563 characters (field accepts 50–2,000)
Sources measured: `persona_view.py search frederick_stone gmail … --no-hidden` for "meta ads receipt" (34 threads, 1 in Sep), "AppLovin" (64, 5 in Sep), "Google Ads" (46, 4), "adjoe" (13, 1), "Unity" (378, 21), "AdMob" (18, 6 in Aug–Sep); Frederick's Sep 2025 mailbox count (263 messages, frederick@harmonygames.co thread files by date_parsed); `persona_view.py can-see frederick_stone` YES for D05S58U4SAK, C07C2866011, C07UCC631A6 and his mailbox; Slack messages counted by ts in the PT window in messages/D05S58U4SAK/2025-09.json, C07C2866011/2025-09.json, C07UCC631A6/2025-09.json; `hg.py search search trello "Lock up social handles"` → data.json /cards/671, cards counted by idBoard (Harmony Games 177, UA/BD 39); `hg.py search search snowflake "AD_REVENUE"` → snowflake.json /tables/35, rows counted where date starts 2025-09; seeded exports, tabs and grid rows counted from 01_Universe_Inject.sql gsheets.sheets_sheets INSERTs (21 tabs, 17 in scope); seeded Slack messages (4) and Trello cards (2) from the same SQL.

## Condensed breakdown (facts for the human's own wording; not for retyping)

The human writes the field in their own words, one short line per group. The 563-character count is the length of the "Facts" column below as written, as a guide to the field size.

| Group | Facts | Time (min) |
|---|---|---|
| G1 | Leonard's DM, 78 msgs that week incl. his admin claim | 25 |
| G2 | #executives skim 225 msgs, Arthur's summary, 90-day remark | 10 |
| G3 | 179-card board to the rules card + comment; eng card, old Confluence page ruled out | 59 |
| G4 | Cash notes money rule + Arthur's Google Ads email | 20 |
| G5 | 13 exports / 17 tabs for holders and class; 3 out-of-scope exports, March sheet | 102 |
| G6 | 263 Sep mails, 38 vendor threads for money; two Google Ads, old AdMob | 131 |
| G7 | adjoe thread, 6,142 Sep revenue rows, Node card, PlayableX/Balancy | 60 |
| G8 | Re-check 6 rows after the comment and email | 12 |
| G9 | Writes: 13-row sheet in Company Ops, DM reply, 4-item checklist | 61 |

G1 = row 1; G2 = 2, 6; G3 = 3, 4; G4 = 5, 16; G5 = 7, 8, 9; G6 = 10, 11, 12; G7 = 13, 14, 15, 18; G8 = 17; G9 = 19, 20, 21. Sum 25+10+59+20+102+131+60+12+61 = 480 min = 8.00 h.

## Self-review

Checks walked in order: `references/Docs/10_Long Horizon Guidelines - V2.md` §5 (sub-tasks, dead ends, workaround, re-reading) and §10 (justified sub-task by sub-task, the arithmetic adds up), the Pre-QC "Difficulty and submission" list (field required, reasoning total equals the number), the field text (0.25 step, 50–2,000 characters, pasting and copying blocked), and V3 §4 (the estimate must fit the assigned tier).

| Check | Result |
|---|---|
| Manual effort, same work | Every row feeds one of the three writes in the brief §4 (register, DM reply, checklist); no row counts learning the universe |
| Volumes persona-filtered | Gmail counts are Frederick's mailbox only (`--no-hidden`); the three Slack containers are YES for frederick_stone; the sweep exports are shared reader to him (dossier §9.1); Trello, Confluence, Snowflake unscoped |
| Rates anchored | Each row names an LH §4 anchor or a V1 rate; rows 1, 5, 7, 8, 14 and 16 state their own rate and why |
| Dead ends explicit | Rows 4, 6, 7, 9, 11, 12, 15 cover T2, T3, T4, T5, T8, T10, T12, T15; T1, T6, T7, T9, T13, T14 are named on rows 1, 2, 8 and 13 where the person meets them; T11 (reuse the handles card) is row 21 |
| Writes per write | Rows 19–21: 1 sheet (13 rows) filed in Company Ops, 1 Slack reply, 1 checklist with 4 items |
| Arithmetic | 21 rows sum to 480 min = 8.00 h, on the 0.25 step; groups G1–G9 sum to the same 480 |
| Field length | condensed facts 563 characters, inside 50–2,000 |

| Counter-reading | Resolution (evidence) |
|---|---|
| Counter (inflated): 8 h is a lot for 13 small exports and three writes | The two largest rows are the money sweep (263 Sep mails in frederick.stone@harmonygames.co, 38 vendor threads at 2 min, row 10) and the 13 exports (row 8, f_f7e7c5bf089029cee91175 … f_2cecf2f81045ec401feb61). The exports are small, so row 8 already uses 5 min for single-tab exports instead of the 8 min V1 floor. Even at 1 min per thread and 4 min per export the total stays near 6.5 h |
| Counter (solution-path estimate): written as if Fred knew where the rules and evidence were | Rows 3 and 21 count the board triage (179 and 39 cards, trello data.json /cards by idBoard) before the rules and handles cards are found; row 10 counts the full Sep mailbox before the receipts; every manifest trap T1–T15 has a dead-end line or is named on its row (01_Hardness_Manifest.json traps); row 17 adds re-reading after comment 68dc529406d8087e5a6b8403 and email frederick.stone@harmonygames.co/1844732985606656293 |
| Counter (evaluator-wide volume): counts include mail or channels Fred can't see | Gmail counts come from `persona_view.py search frederick_stone … --no-hidden` and Frederick's own thread files; Leonard's and Arthur's copies of Arthur's email are not counted. D05S58U4SAK/1758922541.613439, C07C2866011/1759186080.203099 and C07UCC631A6/1757349668.681539 are can-see YES (membership of the im, #executives and the adjoe channel) |
| Counter (tier mismatch): 8.00 h is at the top of Normal, and an earlier draft read 8.45 h | V3 §4 gives Normal "under about 8 hours"; the bundle trigger is above 10 h (playbook gate 7), so no trigger fired. The rate split in row 8 is explained in the Tier check line and would stand at any tier (the V1 8–15 min anchor covers 2–3 surfaces, nine exports are one tab). The call budget of 60 (01_Hardness_Manifest.json call_budget) fits Normal, so the scope and tier agree; the edge risk is reported, the number is not tuned further |
| Counter (linter reading): from the prompt and SQL alone, is 8 h within 3× of a defensible figure? | The prompt asks for every marketing and UA account with holder, money and action, a Sheet, a DM reply and any follow-up from Arthur's rules; the SQL shows 17 seeded spreadsheets with 21 tabs, the rules card and comment, the cash notes doc and Arthur's email (01_Universe_Inject.sql INSERTs). A reader would land between about 4 h and 12 h, so 8 h is within 3×. The reasoning must name the 13 accounts, the 263 September mails and the warehouse rows so the linter sees the money check |
| Counter (could fail): the warehouse row at 30 min is too low for 6,142 rows | Only September paid revenue by network is needed (snowflake.json /tables/35: 5 networks, paid vs accrued_unpaid), not a day-level pull; the AdMob answer is a yes/no on paid revenue. 30 min is stated with its reason |

Unresolved: none. Refresh this worksheet after 08_Oracle_Events.md exists and again after the baseline (count basis).

```
STAGE GATE humantime: PASS — Task_Authoring-2/task_inputs · 05_Human_Time_Worksheet.md#80a406224b96 · blocking 0 · warnings 0 · checks 15
[PASS] structure.outputs: 1 output(s) present: 05_Human_Time_Worksheet.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 00_Assigments.md, 08_Oracle_Events.md, 07_Baseline_Trajectories)
[PASS] chain.prompt-check: upstream 'prompt-check' PASS pasted and current (04_Prompt_Check.md#df246be8bb09, 04_Prompt.txt#c0a69ac771e6)
[PASS] structure.placeholders: no placeholders in 05_Human_Time_Worksheet.md
[PASS] structure.arithmetic: 21 sub-tasks sum to 480 min = 8.0 h
[PASS] evidence.volumes: every sub-task has a measured volume
[PASS] structure.kinds: dead-end / workaround / write lines present
[PASS] structure.field_length: condensed breakdown 563 characters
[PASS] evidence.sources: volume sources name the hg.py / persona_view queries
[PASS] structure.tier_check: tier check line present
[PASS] review.counter_readings: 6 evidenced counter-readings (of 6 found; need ≥ 5) in 05_Human_Time_Worksheet.md
[PASS] review.coverage: self-review addresses all 5 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

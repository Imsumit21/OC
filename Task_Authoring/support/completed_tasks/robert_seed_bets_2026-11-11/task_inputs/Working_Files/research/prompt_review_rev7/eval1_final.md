# PROMPT EVALUATION REPORT

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
Universe: `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450`

### Task: Cost-to-build and revenue page per bet for Leonard's angel calls, with the Payee history pass and a #winddown reply
### Assigned Persona: Robert - Co-founder & Creative Director (robert@harmonygames.co)
### Assigned Business Function: Executive
### Assigned Competency: Finance
### Assigned Task Skill: Analysis and synthesis
### Assigned Horizon: Long Horizon

Inputs: `inputs/04_Prompt.txt` sha256 `d0cb08476d234f3246dea8cd6595cea03f16ec4c5ea9d57a99fa12074fd25631`; `inputs/01_Universe_Inject.sql` sha256 `40f90385e31e099d28a10e483f0a94490a34096c87f08c4ca35c97c3f311d37c`; `inputs/00_Task_Assigned_Inputs.md`.

---

### Injection Gate
- State: CURRENT by hash match to `out/eval0.md` (`hg_injection_gate.py` not run; see Evidence limits)
- Reviewed SQL sha256: `40f90385e31e099d28a10e483f0a94490a34096c87f08c4ca35c97c3f311d37c`  Eval 0 verdict: PASS, COMPLETE (A 5, B 5, C 5), `injection-static-v2`
- Eval 0 findings on records this prompt depends on: none. Its limits (snapshot columns not covered, Lauren Brooks contract PDF unreadable) change no value, set, order, recipient or destination; ENG-2455 states her bucket directly

---

## What the prompt requires (independently derived)

Incorporation chain: prompt "He laid out how he wants it counted and how it should look" and "Work through the Payee history project in Linear the way he wants" point at Leonard's Slack (#winddown C0ADGSZKR3R, fa707da5..., f5b759f3...) which names the doc "Angel note: how to count the money" (f_6feda53b...) and "the layout of my Angel note working sheet" (f_3304033...). Both are shared with robert@ in SQL.

Required writes (all from the prompt plus the doc):
1. New Google Sheet in Robert's Drive, layout of `Angel note working` (Payee, Name on the bank, Bucket, Domino Delights, ZM, Combo Fighter, Company, Note), 22 payee lines, shared with Leonard and Arthur Blake.
2. All 22 Linear issues ENG-2438..ENG-2459 moved to Done.
3. A comment on each issue whose figure differs from the notices, before the Done move: 5 issues (ENG-2439, ENG-2442, ENG-2447, ENG-2450, ENG-2459).
4. One Slack reply in #winddown: cost to build per bet, brought in per bet (no Combo Fighter revenue), what changes on the deck, the sheet link. No deck write (Leonard: "I'll update it myself").

### Ground-truth ledger (computed, base notices + SQL overlay)

Source: 329 `SVB Payment Notification: Payment Processed` emails across 3 mailboxes = 132 unique payments (Robert holds all 132; `Payment Reference` dedupe). USD by bet: DD 984,888.21 / ZM 608,820.50 / CF 73,685.61 (matches Leonard's quick numbers in `Angel note working` and the deck's $985K/$609K/$74K). Plus 1 BGN payment.

Adjustments, each with its authority:

| Payee (issue) | Notices | Line | Why (record, Robert-visible) |
|---|---:|---:|---|
| Leapblock LTD (ENG-2439) | 374,654.00 | **407,944.00** | Doc: "If someone we paid closes out their file with us and tells us what they received, that beats the notices for them." Leapblock's accountant closure in #leapblock (SQL 6312d121, EMPLOYEE_0024): "2023 (from 13 Sep, the first one 33,290) 104,868; 2024 232,726; 2025 62,950; 2026 7,400. Total 407,944 over 30 wires". Notices are 29 wires: 2023 71,578 / 2024 232,726 / 2025 62,950 / 2026 7,400. Only the 13 Sep 2023 $33,290 is missing (Payment Awaiting Approval email in Robert's mail, threads/00001577 "Amount: 33,290.00 USD Transaction Date: Sep 13 2023"). DD +33,290 |
| BANCO DE AMERICA / MotMot (ENG-2442) | 41,088.00 | **37,056.00** | Doc: "Take a notice as paid unless one of us has said the money came back." Leonard #admin_foundersonly (SQL a1488189): "that Apr 2024 wire to the account ending 8605 came back to us. Blake had the wrong number, he re-sent it to 3341". Base corroboration C04UEQVDVB7 2024-04: "money returned to us because Blake put the wrong account number". Re-send to 3341 on 2024-04-05 $4,032 stays |
| JPMorgan ***3203 (ENG-2450) | 4,000.00 | **0** no bucket | Arthur's email (Gmail, SQL, robert copy): "the $4,000 to JPMorgan ***3203 on the SVB notices in Aug 2024 was me. That was our own Chase account ... So it never left the company." Doc: "Money we moved between our own accounts isn't spending, no bucket for that. Every payee keeps its line, even at zero." |
| Private Entrepreneur / Oleg (ENG-2459) | 125.00 | **0** Marketing | Leonard's comment on ENG-2459: "that wire came back the same day, I'd already re-sent it through payoneer". Doc: re-send "goes in only if a receipt for it reached your mail". Robert's mail holds only `Dixelar sent you a payment request` (threads/00004614, 00007150, "Dixelar is requesting a payment of 125.00 USD", "Pay Now"). No receipt. Actual receipts ("Thanks for your payment to Dixelar", 126.25 USD) are in Leonard's mailbox only |
| Lucas (ENG-2447) | 6,450.00 | **13,975.00** | Doc: "If we paid a contractor some other way, it goes in only if a receipt for it reached your mail, at the amount sent, not the fee." Five Western Union transfers in Robert's mail, each with "Lucas received the money you sent" and Transfer amount: 1,075 (2024-06-03, 00005198), 1,075 (06-17, 00005351), 1,075 (06-29, 00005490), 2,150 (07-23, 00005963), 2,150 (08-23, 00006330) = 7,525. Fee 0.00 / 0.99 excluded (Billing Summary in 00005184 etc.) |

Lines (USD, DD / ZM / CF, bucket):

| Issue | Payee | Bucket | DD | ZM | CF | Company | Key evidence |
|---|---|---|---:|---:|---:|---:|---|
| ENG-2438 | Deel, Inc. ***8380 | Build | 530,736.14 | 434,185.44 | 50,425.61 | | Doc "Everything on Deel counts as team" |
| ENG-2439 | Leapblock LTD | Build | 337,594.00 | 59,250.00 | 11,100.00 | | statement + notices |
| ENG-2440 | Eveline Art S.R.L. | Build | 45,941.50 | 36,070.00 | 11,160.00 | | "Marcus's art" |
| ENG-2441 | Adjoe GMBH | Marketing | | 46,201.50 | | | "incent UA" |
| ENG-2442 | BANCO / MotMot | Build | 28,128.00 | 8,928.00 | | | engineer on our team; 8605 out |
| ENG-2443 | Singular Labs | Company | | | | 31,250.00 | "attribution tool, not one game" |
| ENG-2444 | PERSON_4419 LLC (Node Media) | Marketing | 16,428.57 | | | | Robert's mail: Google Ads manager link (00007026), "Fwd: PERSON_4419_NAME Invoices for Sept, Oct, and Nov" with "ad spend" and "creative concepts" (00008689) |
| ENG-2445 | TYZ Law Group | Company | | | | 7,500.00 | "lawyers" |
| ENG-2446 | [PERSON_7200] trademark filings | Company | | | | 7,175.00 | "trademark filings" |
| ENG-2447 | Lucas | Build | 13,975.00 | | | | "mini games dev"; #founders 2024-06-14 "build it as a mini game as well in our game" |
| ENG-2448 | AppLovin | Marketing | | 6,085.56 | | | "past due UA bills" |
| ENG-2449 | Graham Porter | Build | | 5,000.00 | | | "art director for a month" |
| ENG-2450 | JPMorgan ***3203 | none | 0 | | | | own account |
| ENG-2451 | CREATIVE X TEKNOLOJi | Marketing | | 3,750.00 | | | "playable ad for our UA" |
| ENG-2452 | M [PERSON_0056] JP | Company | | | | 3,200.00 | "the website" |
| ENG-2453 | Nathan Price | Build | 2,368.00 | | | | "animation job, coins and chests" |
| ENG-2454 | Martin Walsh ***3801 | Company | | | | BGN 1,999.00 | "paid him direct for his laptop" (equipment, not added to USD) |
| ENG-2455 | [PERSON_7249] Brooks (Lauren) | Marketing | | 500.00 | 1,000.00 | | "she's marketing, not build" |
| ENG-2456 | Ozhan | Build | | 1,000.00 | | | "2D animation"; #art_outsourcing C08FG9924R2 in-game zombies |
| ENG-2457 | [PERSON_9100] | Build | 600.00 | | | | "UX job on the dominoes game" |
| ENG-2458 | [PERSON_0054] [PERSON_0131] | Company | | | | 500.00 | "4X proposal, not one of the three games" |
| ENG-2459 | Oleg | Marketing | 0 | | | | wire back; no receipt in Robert's mail |

Bet boundaries were checked at the edges: no payment on Jan 8/9 2025 (closest Jan 2 and Jan 15) or Nov 23/24 2025 (Nov 12 and Dec 1).

**Cost to build:** DD **959,342.64**, ZM **544,433.44**, CF **72,685.61**. (Marketing DD 16,428.57 / ZM 56,537.06 / CF 1,000; Company 49,625 + BGN 1,999.) Sum check: USD notices 1,667,394.32 + 40,815 adds - 8,157 zeros = 1,700,052.32 = Build 1,576,461.69 + Marketing 73,965.63 + Company 49,625.00 (recomputed).

**Brought in:** REVENUE_DAILY `total_revenue_usd`, 2023-11-01..2026-02-09, summed by `game_id` (grain note in the column comment followed): DD **12,331.25**, ZM **11.99**, CF left off (11.75 recorded; doc "Leave Combo Fighter's revenue off for now, on the page, on the deck and when you tell me"). REVENUE_DAILY_V2 gives the same per-title totals.

**Deck changes for the reply:** slide 3 "$985K/$609K/$74K" -> $959K/$544K/$73K; slide 4 "to fill in" -> DD $12.3K, ZM $12, CF left off.

---

## Phase 1: Prompt Structure & Persona

**Persona:** PASS. Robert is a co-founder and Leonard tagged him: "you know what each of these people did better than I do, can you own it?" (Slack fa707da5). The remit is plausible for a co-founder on a wind-down.

**Assigned Competency:** PASS. Finance: cost per product against lifetime revenue, built from bank notices.

**Assigned Task Skill:** PASS. Analysis and Synthesis: notices weighed against a payee close-out, returned wires, receipts and a warehouse table.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS.
- Stale fact: the sheet and deck quick numbers ($985K / $609K / $74K). Newer facts: Leapblock's close-out, Arthur's Chase email, the returned wires. A notice-first path meets the quick numbers first.
- Data seeding: PASS. Six sentences, 109 words; counting rules, buckets and cutoffs live in the doc, Slack and Linear.

**Naturalness:** PASS. No document formatting, polished connectives, enumerated specs or staged errors. Sentence lengths 31/6/13/16/12/31.

| Pattern | Status |
|---------|--------|
| Command List | PASS. Only order marker is "When you're done", from Leonard's own "when you're done tell me here" |
| Bolt-On | PASS. Deleting S5 removes the Linear work the doc asks for; S2 is the delegation of S1, not an unrelated ask |
| Pre-Solving | PASS. No figure, cause, returned wire or bucket rule stated |
| Tool Mention | PASS. "Drive", "Linear", "#winddown" are natural references; no catalog name, MCP server or "tool" |

Diversity: sheet creation and share, a 22-issue state pass with conditional comments, and a Slack reply. Not a single-post task. Category: Founders / Exec / Strategy.

---

## Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5)

Hand-built in the §2.1 format. `hg_prompt_checks.py render-ugt` was not run because the brief bars writing to `Evals/`.

| Candidate interpretation | Prompt/source authority | Material actions and outputs | Resolved or genuinely ambiguous? |
|---|---|---|---|
| Reading A, best-supported | Prompt S3/S5 incorporate Leonard's doc and Slack. Doc: "that beats the notices for them"; "unless one of us has said the money came back"; "only if a receipt for it reached your mail, at the amount sent, not the fee"; "Leave Combo Fighter's revenue off" | Build DD 959,342.64 / ZM 544,433.44 / CF 72,685.61; revenue DD 12,331.25 / ZM 11.99, CF off. New sheet, 22 lines, shared with Leonard and Arthur Blake. 22 issues Done, 5 "why" comments first. One #winddown reply with link. No deck write | Best-supported |
| Reading B, strongest alternative | Notices as the last word, from Doc "Go by the bank" and "Anything paid out of Chase isn't in here", plus prompt "each bet ... brought in" | Build DD 951,817.64 if Western Union is excluded as Chase-funded (DD 918,527.64 with Leapblock also left at the notices), and Combo Fighter's 11.75 reported | Ruled out: every difference is killed by a quoted sentence or record in the fork list under Deep Recheck |

Five checks. Newer source: Arthur's email and Leonard's reply (Feb 13) settle ENG-2450's earlier tentative note. Authority: S3/S5 point at the doc and Slack. Source identity: the doc's "one of us" is the three founders ("so the three of us say the same thing"), and the payee close-out is from Leapblock's contact in #leapblock. Scope: each rule was applied per payee over 22 issues. Same result: not the same under A and B, so B had to be killed, and it was. No both-fair figure.

Census of the open rules, all over Robert's view, keyword-based (see Evidence limits):
- "said the money came back": the 8605 wire and Oleg's wire only. Eval 0's full Gmail scan finds exactly two returned wires in the base, the same two.
- "closes out their file": Leapblock only.
- "some other way, receipt in your mail": 5 Western Union transfers to Lucas only. Each is two mails on one MTCN. Payoneer in Robert's mail is two payment requests.
- Non-USD: Martin's BGN 1,999 only.
- Payee set: 23 notice accounts onto 22 issues, none unmatched either way.
- Awaiting/Scheduled with no Processed match: Leapblock's $33,290 only (328 of 329 such mails parsed; P1 independently reports the same).
- Bet edges: nearest payments Jan 2 and Jan 15, Nov 12 and Dec 1, so no cutoff edge changes a figure.

**Feasibility:** PASS (5). Supported paths in catalog: Gmail, Slack, GDocs/GSheets/GSlides reads; `gsheets_create_spreadsheet`, `gsheets_values_update`, `gdrive_share_file`; `linear_update_issue`, `linear_create_comment`; `slack_send_message`; `snowflake_execute_query`. No unsupported format. Dimensional: `game_id` and notice Transaction Date present. Numeric observability: notice amounts, WU Transfer Amount and Billing Summary are plain text; `total_revenue_usd` at source precision.

**Persona ACL Reachability:** PASS (5). All 132 notices, 5 WU receipts, Payoneer requests, Arthur's email and the Node Media mail are in Robert's mailbox. `persona_view can-see robert slack` YES on C0ADGSZKR3R, C04UEQVDVB7, C05URGU759U, C04UTBZL6AX, C08FG9924R2, C06MXPL9536, D07H86MV4DN. Doc, sheet and deck are shared with him. Linear and Snowflake are unscoped. Leonard's SVB CSV and his Wire Returned mails are hidden from Robert and not needed.

**Truthfulness:** PASS (5).

| Claim | Record | Result |
|---|---|---|
| "On Thursday" | fa707da5, 2026-02-13T01:23:41Z = Thu Feb 12 17:23 Pacific; Robert and Leonard `timezone` America/Los_Angeles | True in the persona's zone (DR1) |
| "#winddown" | C0ADGSZKR3R name "winddown" | True |
| "one straight page on what each bet cost us to build and what it brought in" | fa707da5 near verbatim | True |
| "his angel calls on Tuesday" | fa707da5 "the angel calls on tuesday"; GCal start 2026-02-17T17:00Z | True |
| "how he wants it counted and how it should look" | "in the doc I just wrote"; "use the layout of my Angel note working sheet" | True |
| "share it with him and Blake" | "share it with Blake and me"; one Blake in Contacts | True |
| "Payee history project in Linear" | linear_projects 0742c172, name "Payee history" | True |
| "the draft deck" | "Note to angels (draft)" | True |
| Shutdown / departed-person premises | Wind-down work by the three founders kept on | True |

**Tool Use & Cross-service:** PASS (5). Gmail (notices, WU, Arthur) sets figures. Linear sets buckets and the Oleg return, and takes writes. Slack sets Leapblock and 8605, and takes the reply. GDocs sets the rules. Snowflake sets revenue. Dropping any one changes the answer.

**Investigation + Action:** PASS (5).

**Clarity & Specificity:** PASS (5). One write set under every reading tested. No "I'll X" delegation.

**Contrived / Unnatural:** PASS (5). No trap hint, hidden destination, audit form, if-chain, opaque ID or exact timestamp; at most one register trigger.

**Alignment with Today's Date:** PASS (5). Thursday Feb 12 and Tuesday Feb 17 are consistent with the clock; the angel calls are a future plan.

**Originality:** N/A, no samples supplied.

---

## Phase 3: Universe Feasibility

**Data Existence:** PASS (5). All entities verified and retrievable through cataloged tools.

**Cross-Service Coherence:** PASS (5).
- Inconsistencies in task-touched data: None.
- Injection SQL considered: Yes, sha 40f90385...
- Static integrity evidence: REUSED from `out/eval0.md` checks A, B, C on the same SQL hash; prompt-specific sources checked directly.
- Checked: Linear comments before Slack before Arthur's email; Leapblock's years sum to 407,944 and tie to 29 notices plus $33,290; quick numbers reproduce from notices to the cent; message authors are channel members; Leapblock message 08:37Z is before the 10:03Z Slack end (NB-6); Node invoices sum to 16,428.57.
- Snowflake (synthetic, task-read): iap + ad = total on all 2,284 rows; table comment's peak days reproduce (159.03, 1.99, 0.73); REVENUE_DAILY_V2 matches per title.
- Prompt-specific sources, access and configuration: supported. No friction configuration supplied.

---

## Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score | Justification |
|-----------|--------------|-------|---------------|
| Prompt | Unique Ground Truth | 5 | Two-reading table above; every fork killed by a quote |
| Prompt | Feasibility | 5 | All asks have supported paths and data |
| Prompt | Persona ACL Reachability | 5 | Every required scoped read visible to Robert |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | One write set |
| Prompt | Contrived / Unnatural | 5 | Plain delegation over seeded rules |
| Prompt | Alignment with Today's Date | 5 | Consistent with the clock |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | No tight or loose error |
| Prompt | Tool Use & Cross-service | 5 | Each service changes a graded fact |
| Prompt | Investigation + Action | 5 | Investigation feeds the writes |
| Prompt | Coherence (Bolt-on) | 5 | No unrelated ask |
| Prompt | Persona | 5 | Asked by name, plausible remit |
| Prompt | Business Function | 5 | Founders / Exec / Strategy |
| Prompt | Assigned Competency | 5 | Finance |
| Prompt | Assigned Task Skill | 5 | Analysis and Synthesis |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three load-bearing; short trigger |
| Universe | Data Exists | 5 | Retrievable |
| Universe | Cross-Service Coherence | 5 | None found; Eval 0 PASS on the same hash |

### Issues Found

None at any severity that lowers a score.

### Recommended Improvements

No fix is required. One optional edit, and five items for later stages:

1. Optional: remove "On Thursday" from S1, leaving "In #winddown Leonard asked me for one straight page on ...". Checked under deep_recheck step 5: it adds no value, id or lock-in. The current wording is correct, so this only removes a literal-UTC reading, and it changes the prompt bytes, so the review would need a re-run.
2. For `/rubric` (from P1; each fails only if a row locks one side): share role and sheet title are unstated; a thread reply or a top-level post both meet "tell me here"; BGN 1,999 may sit in the Note or Company cell if unsummed; deck figures may be $K or exact; the revenue line's position on the page is open.

---

## Deep Recheck

Passes: P1, P2, P3, P4, run separately by the coordinator and reported blind to this review. Their model and effort are not stated in the pass files.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 6 sentences, doc's 10 paragraphs, 2 Slack messages, 22 issues, 60 comments | 0 | 0 |
| P2 | 5 sentences as counted by that pass, 124 INSERT and 2 UPDATE | 1 advisory | 0 |
| P3 | 6 sentences, Leonard's claims | 0 | 0 |
| P4 | 6 sentences | 1 referral | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P2, P4 (P3 checked it true) | "On Thursday in #winddown Leonard asked me" | Slack fa707da5, 2026-02-13T01:23:41Z | date-slip / Truthfulness | Truthfulness | REJECTED | Robert-readable: `slack/users.json` Robert and Leonard `"timezone": "America/Los_Angeles"`, so the post is Thu Feb 12 17:23; the seeded invite to Robert reads "(PST)". P4's "no record states one" is wrong. `Evals/ENVIRONMENT.md`: "If the Pacific date and the UTC date are different, accept either." One matching post, so no order, window or count changes |

Records opened at this step: ENVIRONMENT.md lines 154-157; `[ORG_NAME_0354]` as SVB ("[ORG_NAME_0354], a division of First-Citizens Bank & Trust Company" in threads/00001355, "*Bank Name:* [ORG_NAME_0354]" in 00000484); [PERSON_NAME_36400] on all five WU receipts; D04UP2L3E3S 2025-05 #396; Robert's mail for Revolut (newsletters only).

Effect on verdict: unchanged.

Fork list (all settled; none open):
- F1: Leapblock line | 407,944 | 374,654 | Settled by: Doc "that beats the notices for them"; #leapblock 6312d121 "Total 407,944 over 30 wires".
- F2: The $33,290 wire | DD, in scope | outside SVB or Chase | Settled by: Awaiting Approval 00001577 "Analysis Checking ***0100 ... Amount: 33,290.00 USD Transaction Date: Sep 13 2023".
- F3: Banco 8605 $4,032 | out | counted | Settled by: a1488189 "came back to us".
- F4: Oleg SVB wire | $0 | $125 | Settled by: ENG-2459 "that wire came back the same day".
- F5: Oleg Payoneer | not counted | $125 or $250 | Settled by: Doc "only if a receipt"; 00004614/00007150 "requesting a payment of 125.00 USD ... Pay Now".
- F6: "your mail" | Robert's | any founder's | Settled by: fa707da5 "<@Robert> ... can you own it? how I want it counted is in the doc".
- F7: Western Union | counted | not on notices | Settled by: Doc "If we paid a contractor some other way".
- F8: WU amount | 7,525 | 7,528.96 | Settled by: Doc "at the amount sent, not the fee".
- F9: WU out of Chase | no | yes | Settled by: receipts "MASTERCARD ending in 4655"; 00002502 "[ORG_NAME_0354] MasterCard® account ending in 4655", with that token SVB's in 00001355 and 00000484.
- F10: JPM ***3203 | $0, no bucket | contractor advance | Settled by: Arthur "our own Chase account ... So it never left the company"; Leonard "ah that's the one I couldn't place".
- F11: Lucas bucket | Build | Company | Settled by: ENG-2447 "mini games dev"; #founders "build it as a mini game as well in our game".
- F12: Node Media (ENG-2444) bucket | Marketing | Company or Build | Settled by: Doc "agencies"; 00008689 "your ad spend exceeds $100,000".
- F13: Singular | Company | Marketing | Settled by: ENG-2443 "attribution tool, not one game".
- F14: Ozhan | Build | Marketing | Settled by: #art_outsourcing "help us with the 2D animation"; in-game zombie work in Unity.
- F15: Graham Porter | Build | Company | Settled by: ENG-2449 "art director for a month".
- F16: Martin | Company, BGN | Build ZM, converted | Settled by: ENG-2454 "his laptop"; Doc "equipment", "stays in its own currency".
- F17: ***3139 $500 | Company | excluded as own pay | Settled by: ENG-2458 "not one of the three games"; surname token [0131] against Robert's [0085].
- F18: Brooks | Marketing | Build | Settled by: ENG-2455 "so she's marketing, not build".
- F19: Combo Fighter revenue | omitted | reported | Settled by: Doc "on the page, on the deck and when you tell me".
- F20: Revenue table | REVENUE_DAILY | REVENUE_DAILY_V2 | Same result: per-title totals are equal.
- F21: Deck write | none | edit | Settled by: f5b759f3 "I'll update it myself".
- F22: "Why" comments | 5 issues | all or none | Settled by: Doc "If your figure isn't what the notices add up to, say why on the issue first".

Platform defects: none.

### FINAL VERDICT: PASS

Score: 5

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE (local review)

Evaluator model: Opus 5.5 (claude-opus-5-5)

Next action: Run the portal /prompt; this local result is not a portal result.

Evidence limits:
- `hg_injection_gate.py`, `prompt_check_record.json`, `render-ugt` and `hg_write_output.py` were not run, because the brief bars `hg_store_input.py` and writes to `Evals/`. The gate state rests on the hash match to `out/eval0.md`.
- Absence claims are keyword scans, so an anonymized sender with none of the terms would be missed. The Slack "recall" and "laptop" queries hit their limits; neither is the sole basis for a settled fork.
- Tool return rendering is not observed; the catalog has no return schemas.
- Docs: Prompt Writing, Unique Ground Truth, Common Errors and the QC form's Prompt and Universe rows were read; Overall Task Flow, Persona ACL, Universe and Tools, Example Task and the QC spec sheets were read in part or by keyword. Extracted with PDFKit and stdlib.
- Corrections to the Phase 1-4 draft: it claimed a Revolut census and `persona_view` results on #founders and #art_outsourcing that had not yet been run, and it called the census complete. All three are corrected here; the checks have now been run and came back clean.

**Lowest Dimension:** None below 5.

**Summary:** Every required figure, bucket and write resolves to one outcome from records Robert can open, and the 22 forks tested each have a quoted settlement. Eval 0 passed on the same SQL hash and the four passes left no open fail-level finding; the one Thursday item was rejected on Robert-readable timezone records. No fix is required.

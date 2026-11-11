# Surface adjudication: rev6 precheck run

Run: `06_PreCheck_Trajectory/trajectory.json`, sha fc4e4ed2. All event numbers are 0-based. Surface: `Working_Files/01_Gradable_Surface.json`, 29 slots, weight 91.

## Result

| Score | Weight | Share |
|---|---|---|
| (a) Tool raw | 35 / 91 | 38.46% |
| (b) Hand-corrected against our truth | 75 / 91 | 82.42% |
| (c) If 963,374.64 is correct (no MotMot return) | 91 / 91 | 100.00% |

Under (b) four slots fail, all from one cause: the run did not find that the bank returned the $4,032 MotMot wire. The tool's 38.5% is mostly decoder and surface error. It failed 15 slots the run earned and passed one the run did not (C1).

Every write succeeded. Sheet 463 returned `updatedRange Sheet1!A1:H28`. Shares 465 and 467 returned role `writer` for leonard.hayes@ and arthur.blake@. Comments 473-479 and all 22 Done updates 483-525 returned without error. Slack 532 returned ok, ts 1771027929.000000, channel C0ADGSZKR3R. The `writes.json` sheet payload equals the raw event 463 input. `writes.json` drops `reply_broadcast: true` from event 532, so it understates where the reply landed.

Sheet cell references below are 1-based: A Payee, B bank name, C Bucket, D Domino Delights, E ZM, F Combo Fighter, G Company, H Note. Row 1 is the header, rows 2-23 are the 22 payees, row 24 is blank, rows 25-28 are totals.

## 1. All 29 slots

"Key miss" means the row exists but its Payee cell is not the exact surface key. "Dropped" means the Payee cell has a comma, so `key_regex` rejects the row and the decoder never sees it.

| Slot | Wt | Hand | Tool | Deciding cell or text | Why the tool differs |
|---|---|---|---|---|---|
| X1 MotMot net | 5 | FAIL | FAIL | D5 = 32160, truth 28128. H5: "11 wires across two accounts; none reported back." | Agrees, but the row was also dropped (comma), so the tool never read the value |
| X3 Lucas | 5 | PASS | FAIL | D6 = 13975, truth 13975 | Key miss: "Lucas (mini games dev)" |
| X4 Leapblock | 5 | PASS | FAIL | D3 = 337594, truth 337594 | Dropped: "Leapblock (Martin & Victor, saga map crew)" |
| X5 JPMorgan out | 5 | PASS | FAIL | C23 = "None (own accounts)", D-G23 all 0, B23 = "JPMorgan [PERSON_NAME_4503] ***3203" | Key miss: "Our own Chase account", plus alias gap (section 2) |
| X6 Node Media | 5 | PASS | FAIL | C11 = Marketing | Key miss: "Node Media (UA agency)" |
| X8 Lauren Brooks | 5 | PASS | FAIL | C15 = Marketing | Key miss: "Brooks (Telegram paid UA)" |
| X9 Martin BGN | 3 | PASS | FAIL | G22 = "BGN 1,999", out of G27 = 49625 | Key miss: "Martin (laptop)"; the value is an accepted alias |
| B1 DD build | 5 | FAIL | FAIL | D25 = 963374.64; regex wants 959,342 | Agrees |
| B2 ZM build | 5 | PASS | PASS | E25 = 544433.44 | |
| B3 CF build | 5 | PASS | PASS | F25 = 72685.61 | |
| B4 Company line | 3 | PASS | PASS | G27 = 49625 | |
| V1 DD revenue | 3 | PASS | PASS | D28 = 12331.25 | |
| V2 ZM revenue | 3 | PASS | PASS | E28 = 11.99 | |
| S1 Deel | 3 | PASS | FAIL | D2 = 530736.14 | Key miss: "Deel (team monthly runs)" |
| S2 Eveline Art | 3 | PASS | FAIL | D4 = 45941.5 | Dropped: "Marcus (Eveline Art, art)" |
| S3 Graham Porter | 1 | PASS | FAIL | E10 = 5000 | Dropped: "Graham Porter (art director, May 2025)" |
| S4 Adjoe | 1 | PASS | FAIL | C12 = Marketing | Key miss: "Adjoe (incent UA test)" |
| S5 Trademark lawyer | 3 | PASS | FAIL | G19 = 7175, B19 = "[PERSON_NAME_7200] ***7393", same bank name as truth | Key miss: "Trademark filings" |
| S6 Build rows | 1 | PASS | FAIL | 9 Build payee rows (rows 2-10) | Tool counted 4: 3 surviving payees plus total row 25 |
| C1 MotMot reason | 3 | FAIL | PASS | No comment on ENG-2442 at all | False pass: regex matched "came back" in the Oleg comment, ENG-2459, event 477 |
| C2 Lucas reason | 3 | PASS | PASS | ENG-2447, event 475: "Western Union" | |
| C3 Leapblock reason | 3 | PASS | PASS | ENG-2439, event 473: "33,290" | |
| C4 JPMorgan reason | 3 | PASS | PASS | ENG-2450, event 479: "Chase" | |
| R1 reply DD | 3 | FAIL | FAIL | Reply: "Domino Delights: $963,374.64" | Agrees |
| R2 reply deck | 3 | PASS | PASS | Reply: "Cost slide: $985K / $609K / $74K -> $963K / $544K / $73K" and the "Brought in" slide line | Agrees; caveat in section 2 |
| D1 in Robert's Drive | 1 | PASS | FAIL | Result 455: `owners: ["robert@harmonygames.co"]`; no move | Decoder reads only an explicit parent (section 2) |
| D2 shared with Leonard | 1 | PASS | FAIL | Result 466: leonard.hayes@, role writer | Surface wants `reader`; no one asked for it |
| D3 reply links sheet | 1 | PASS | PASS | Reply carries the sheet URL | |
| D4 reply in #winddown | 1 | PASS | FAIL | Call 532: thread_ts 1770945859.212469, `reply_broadcast: true`; result 533: channel C0ADGSZKR3R | Surface pins the other message |

Totals: 16 disagreements. 15 are tool FAIL / hand PASS (43 weight). One is tool PASS / hand FAIL (C1, 3 weight).

## 2. The contested slots

### X1, B1, R1, C1: true miss, one cause

Method, Leonard's doc: "Take a notice as paid unless one of us has said the money came back."

The evidence exists and the founders said it, in #admin_foundersonly (C04UEQVDVB7):

- 1712331142.975829, Leonard: "This wire didn't go through"
- 1712331372.614469, Blake: "thats the motmot one?"
- 1712331718.859679, Blake: "I think I messed up the bank account number. Fixed up and resubmitted the payment."
- 1712901800.684259, Leonard: "this is money returned to us because Blake put the wrong account number to pay up [PERSON_NAME_24716] and bank returned our money"

The notices fit. There is a $4,032 Processed notice to ***8605 on Apr 2, 2024 (thread 00004088) and a $4,032 notice to ***3341 on Apr 5, 2024 (thread 00004124). ***8605 appears on that one notice only.

The run saw the pair in its own listing at event 159 and wrote "two accounts" on the row. It looked for returns only in Gmail (event 205), and read the founders' channel only for Aug 2024 windows (events 357 and 370). Its Slack "wires" search was limited to after 2025-12-01 (event 267). H5's "none reported back" is unsupported and false.

The platform /hardness report accepts 963,374.64 as right (its R11) and says there is no returned-wire message in Robert's mail. That is true of the mail. It did not check Slack, so it does not rebut the truth.

### C1: surface defect that hid part of the miss

Slot title: "reason on the MotMot issue". Selector: `text comments <regex>`, with no issue binding. The tool passes it on Oleg's comment, "the May 2024 wire came back the same day". Method: "If your figure isn't what the notices add up to, say why on the issue first." The run wrote nothing on ENG-2442 and moved it to Done (event 491). True fail, tool false pass.

### X5: decoder defect plus surface defect

Method: "Money we moved between our own accounts isn't spending, no bucket for that. Every payee keeps its line, even at zero." C23 = "None (own accounts)" is exactly that, and the row stays at zero. Two separate things block the tool:

- Key miss on the row label.
- The alias list accepts "None" and "Own account" but `compare` needs an exact normalized match, so "noneownaccounts" is DIFFERENT. I confirmed X5 still fails after only the keys are fixed.

The same alias list accepts a blank cell, which is too loose (section 5).

### X9: decoder only

Method: "Anything not paid in dollars stays in its own currency next to the line. Don't add it to a dollar total." G22 = "BGN 1,999", which the yes_no list accepts for "1,999.00 BGN". G27 stays 49625. The only defect is the key miss on "Martin (laptop)".

### S1-S5: decoder only

Each value or bucket matches truth. Causes are in the table above: S1, S4 and S5 are key misses; S2 and S3 are dropped on the comma. S5 is identifiable only through column B, which the decoder never uses as a fallback.

### S6: decoder defect

The slot wants 9 payees in Build, and the sheet has exactly 9. The tool's 4 is Deel, Lucas, Ozhan and the totals row "Cost to build (Build lines)". Six Build rows are dropped on commas (Leapblock, Marcus, MotMot, Nathan, UX, Graham). With keys fixed the tool counts 10, because the totals row still counts.

### D1: decoder defect first, surface pin second

Prompt: "Build that page as a sheet in my Drive." Leonard: "keep yours in your drive and share it with Blake and me."

`d_9f7ba94f7526d54d8482ba` is Robert's Drive root: name "robert@harmonygames.co", `parents: []`, owner robert. So the slot is aimed at the right place. But `_register_parent` (surface_grader.py:686) only reads `parentId`, `folderId` or a later move, and `gsheets_create_spreadsheet` has no parent parameter (catalog: `title`, `initialSheetTitle`, `driveFileId`). The natural tool can never satisfy the slot without a no-op `gdrive_move_file`; a planted no-op move flips it to PASS.

The pin to one folder would also wrongly fail a subfolder of Robert's Drive, which the prompt allows.

### D2: surface defect

Prompt: "share it with him and Blake." Leonard: "share it with Blake and me." No role is named. Leonard's own doc and working sheet give Robert and Blake `writer` (SQL lines 8 and 10), so writer is the local norm. `share_reader` (surface_grader.py:962) also has no recipient check; see section 5.

### D4: surface defect

Prompt: "reply to him in #winddown". Leonard's second message, 1770945859.212469, says "when you're done tell me here what each bet cost and brought in and what changes on the deck". The surface cites "the ask: tell me here" but pins the first message, 1770945821.640039, which does not contain that sentence.

Both are top-level (`thread_parent_id` NULL). The run threaded on the message that actually asked and broadcast to the channel. A thread on either message or a channel post are all fair. The tool can see only one.

### R2: PASS, with a weak selector

Prompt: "what changes on the draft deck". Leonard: "what changes on the deck, I'll update it myself". Deck slide: "What each bet cost to build: Domino Delights $985K, ZM $609K, Combo Fighter $74K"; next slide "What each brought in: to fill in". The reply covers both slides and leaves Combo Fighter off.

Its DD figure, $963K, should be $959K, but that is the MotMot cause already charged at X1, B1, R1 and C1. The slot title only requires saying the figures change. If R2 is read strictly as needing all three correct cost figures, (b) becomes 72 / 91 = 79.12%.

The regex is `[Dd]eck` alone: a planted reply "I did not touch the deck" passes.

## 3. Scores

Weights check: X 33, B 18, V 6, S 12, C 12, R 6, D 4 = 91.

**(a) Tool raw.** Passed: B2 5, B3 5, B4 3, V1 3, V2 3, C1 3, C2 3, C3 3, C4 3, R2 3, D3 1 = 35. 35 / 91 = 38.46%. A read-only replay gave the same 35.

**(b) Hand-corrected.** Tool 35. Add the 15 corrected slots: X3 5, X4 5, X5 5, X6 5, X8 5, X9 3, S1 3, S2 3, S3 1, S4 1, S5 3, S6 1, D1 1, D2 1, D4 1 = 43. Subtract C1 3. 35 + 43 - 3 = 75. 75 / 91 = 82.42%. Failed weight: X1 5 + B1 5 + C1 3 + R1 3 = 16; 91 - 16 = 75.

**(c) 963,374.64 taken as correct.** X1 passes (D5 = 32160 would be right), B1 and R1 pass. C1 falls away: MotMot's figure would equal its notices, and the method asks for a comment only "If your figure isn't what the notices add up to". 75 + 5 + 5 + 3 + 3 = 91. 91 / 91 = 100.00%. If C1 were still counted as failed, 88 / 91 = 96.70%.

The unfixed tool under (c) would move only B1 and R1: 35 + 5 + 3 = 43 / 91 = 47.25%.

**(d) Failed slots under (b), by root cause.**

| Root cause | Slots | Weight |
|---|---|---|
| Missed founders' Slack note that the $4,032 wire to ***8605 was returned | X1 (row), B1 (total), R1 (reply), C1 (no reason on the issue) | 16 |

One independent cause. The Done on ENG-2442 and the $963K on the deck line are the same cascade.

**Replay cross-check.** I re-graded a scratch copy of the run's calls through the unmodified grader:

- Labels mapped to truth keys: 69 / 91, failing X1, X5, B1, S6, R1, D1, D2, D4.
- Plus totals rows with Bucket blanked: 70 / 91 (S6 fixed).
- Plus JPMorgan Bucket "None": 75 / 91, failing X1, B1, R1, D1, D2, D4.

That last 75 matches (b) by coincidence: the tool still fails D1, D2 and D4 (-3) and still passes C1 (+3).

## 4. The run's own arithmetic

Sheet rows sum to its totals exactly:

| Group | Domino Delights | ZM | Combo Fighter | Company |
|---|---|---|---|---|
| Build, 9 rows | 963,374.64 | 544,433.44 | 72,685.61 | |
| Marketing, 6 rows | 16,428.57 | 56,537.06 | 1,000.00 | |
| Company, 6 rows | | | | 49,625 + BGN 1,999 |

Marketing and Company totals hold against truth. Bridge from Leonard's quick pass:

- DD: 984,888.21 + 33,290 + 7,525 - 4,000 - 125 - 16,428.57 - 41,775 (company by date) = 963,374.64
- ZM: 608,820.50 - 56,537.06 - 7,850 = 544,433.44
- CF: 73,685.61 - 1,000 = 72,685.61

With the return, DD is 963,374.64 - 4,032 = 959,342.64.

Against truth on all 22 payees and five columns, the only real value error is MotMot D5. The other differences are Martin's "BGN 1,999" (accepted form), JPMorgan's bucket text, and truth carrying game-column allocations for Company payees (for example Singular 25,000 / 6,250) where the sheet has 0. The method puts Company money in the Company column, and no slot reads those cells, so that last one is a truth-file note, not a run error.

The arithmetic is clean. Other inconsistencies:

1. H5 "none reported back" is false, as above.
2. H25 sources the build total as "SVB Payment Processed notices", but the total also holds Leapblock's no-notice $33,290 and Western Union's $7,525. Rows 3 and 6 disclose them.
3. The reply's heading says each listed item "is explained on its Linear issue", but it lists Node Media and there is no comment on ENG-2444. No comment was owed, since its figure equals the notices. Node Media is also not a difference from the notices, only a bucket call.
4. The reply's deck sentence explains the drop only by removing marketing and company. The +33,290, +7,525, -4,000 and -125 are in the next section, so there is no single bridge.

## 5. Idle and wrong-answer exposure

**Idle agent:** grading an empty run gives 0 / 91. No slot passes with no writes and no answer.

**Plausible wrong answers that pass.** Items marked (probed) were confirmed on planted runs through the unmodified grader.

| Slot | Wrong answer that passes | Status |
|---|---|---|
| X5 | JPMorgan Bucket blank with $4,000 still in DD: blank is an accepted alias and the slot reads only Bucket | probed |
| X6, X8, S4 | Right bucket, wrong amount: they read only Bucket | by selector |
| R1 | "$0.96M" on a 963K basis: third regex alternative | probed |
| R2 | Any reply containing "deck" | probed |
| C1 | Any comment on any issue with "came back" or "return" | happened in this run; probed |
| C2, C4 | One Lucas comment "Western Union transfers" passes both (`[Tt]ransfer`) | probed |
| C3 | "statement" or "33,290" on any issue | by selector |
| D2 | Reader share to a stranger on the file | probed |
| D4 | Reply "ok" on the pinned thread; the channel is not checked (`thread_match`) | probed for content; channel by code |
| S6 | 8 Build payees plus a Build-labelled totals row | probed |
| B1-B4, V1, V2 | The exact number anywhere in the sheet, including a Note | by selector |

## 6. Defects confirmed

**Decoder (`trajectory_ledger.py` / `surface_grader.py`):**

1. Whole-cell key equality. `_keyed_rows` keys rows by the entire cell (trajectory_ledger.py:655) and the field check needs `k in srows` (surface_grader.py:1041). Free-text labels never match. Hits X3, X5, X6, X8, X9, S1, S4, S5. The sheet's Name-on-the-bank column is the obvious fallback and is unused.
2. `_keyed_rows` uses `fullmatch` on `key_regex` (trajectory_ledger.py:653), so a comma drops the row. Hits X1, X4, S2, S3 and the S6 count.
3. Totals rows count as payee rows. They match `key_regex` and carry a class in Bucket, so `written_classes` (surface_grader.py:755) counts them. Hits S6.
4. `_register_parent` treats no explicit parent as wrong (surface_grader.py:686), while the Sheets create tool cannot take one. Hits D1.

**Surface (`01_Gradable_Surface.json`):**

5. `key_regex` character class omits the comma (line 49). This is the data side of defect 2.
6. X5 alias list lacks the descriptive form and accepts a blank.
7. D2 `share_reader` demands a role no one asked for and binds no recipient.
8. D4 pins the wrong message, against its own "tell me here" reason.
9. D1 pins one folder id where the prompt says only "my Drive".
10. C1-C4 text selectors are not bound to the issue. C1 false-passed here.
11. R1's `0.96M` alternative and R2's bare `[Dd]eck` accept wrong answers.

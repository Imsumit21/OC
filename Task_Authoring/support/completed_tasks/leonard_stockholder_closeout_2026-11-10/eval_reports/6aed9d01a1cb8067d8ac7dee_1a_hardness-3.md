# HARDNESS REPORT (Eval 1A, Opus observed)

- Attempt: 6aed9d01a1cb8067d8ac7dee (chat review, new run after the injection SQL changed)
- Actual review date: 2026-11-08
- Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
- Assignment (platform record): Leonard Hayes, Co-founder & Creative Director · Executive · Finance · Authoring · long-horizon · difficulty mode medium
- authority_contract: prompt-incorporation-v1
- The earlier hardness report (score 2, run `f059ce83…`, SQL revision 3) is history only. This review does not reuse its score or requirement map.

## 1. Inputs and provenance

| Input | Source | SHA-256 |
|---|---|---|
| Prompt | `Evals/task_inputs/04_Prompt.txt` (712 B) | `424c70d34fdfba5e323649f44e4c228d3b3694d2196fc2891d6d55f5fb1407a2` |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` revision 6 (111,997 B; proposed overlay, not executed; Eval 0 PASS on this hash) | `9b02cc8f34a91f69c6faf607f5578d25b52e10c6115a0cddf99a180f4d8b5bfb` |
| Run | `Evals/task_inputs/opus/trajectory.json` (uploaded as "trajectory-run-1 (2).json", 4,178,574 B) | `0a5cba6f3e2c907dd58ec3c1cb88efbd53277b4907a18fce7049b52599edfdff` |
| Universe | `Universe_Normal` (`hg4-2026-08-31` v37); `Evals/references/universes/normal/universe_manifest.json` | `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |

- **Model:** 349 assistant events are `claude-opus-5-5` (2 `<synthetic>`); init model `claude-opus-5-5[1m]`; Claude Code 2.1.280; session 8ab161d4-3134-448b-803c-5b5b88ae4545; `subtype: success`, `terminal_reason: completed`, 202 turns. Confirmed Opus.
- **Task match / hint status:** the export has no initial user-prompt event (it starts with the init event and the Agent's first tool call). The match is shown by behavior. The run opens Linear project "Holder records" (`ec2ea957-…`), the close-out notes doc `f_a37b403d5200d4f0a31d31`, ENG-2438–2463, the #winddown list thread `1770934638.035469` and the KPMG thread `1857029474983245439`. It produces exactly the prompt's seven deliverables and leaves only the holder notes unsent. The only other user-text events are six context-compaction summaries inside the two sub-agents, restating the Agent's own sub-agent briefs ("Research only"). No hints, extra rules or answer text. Treated as unhinted, same task.
- **Source match:** the run read SQL-revision-6 records: Calvin's Feb 3 forward of the Carta extension (SQL line 112), the Feb 12 "Harmony" mail to Husnu Akin (line 120), the bounce for PERSON_3140_EMAIL (line 108), the #winddown family/Covered replies (lines 57–59, read at event 25) and the Sunset and KPMG threads. So the run environment carried the current overlay.

## 2. Requirement map (expected vs observed)

Requirements come from the prompt plus the sources it tells the Agent to follow: the close-out notes doc, the Linear project description and, through them, the #winddown draft and thread replies, the update outline, Sunset's intake email and KPMG's request and clarification. Facts come from persona-visible records (Leonard's mailbox, his Drive, Slack conversations he belongs to, Linear).

| # | Requirement (source) | Expected | Observed (trajectory event) | Outcome |
|---|---|---|---|---|
| R1 | Holder sheet: finish "Holder list (draft)", one row per issue, founders only in totals (notes; Sunset email) | 26 rows with label, holding today (vested for options), last day; totals; counts by label; directors; preferred vote | Sheet `f_5ecaa967db3adcfa440b09` cleared and rewritten (ev. 744–746), 26 rows, totals, counts, directors and vote; renamed "Holder list" | MET as a structure; content defects under R3, R4, R6, R7 |
| R2 | Carta is the record; a line whose last day passed holds nothing (notes) | ES-2, ES-5, ES-6, ES-16, ES-17 → Nothing; **Calvin ES-3 live** (Carta update: last day Feb 20, 2026, SQL line 112) | Five lines Nothing/Canceled with "why" comments (ev. 855–881); Calvin 4,408 vested, Feb 20 | MET (Calvin trap passed) |
| R3 | Holdings per Carta (notes "Each note says what they hold"; Sunset "what each holds today") | Advisor-angels hold seed shares **plus** an option: ENG-2440 50,865 + ES-8 30,518; ENG-2447 25,432 + ES-9 61,038; ENG-2449 25,432 + ES-10 6,104; ENG-2446 25,432 + ES-11 6,104 (disclosure schedule `threads/leonard@harmonygames.co_1773160163779741845.json` /messages/1; Carta notice `…_1782897835407336831.json` /messages/0 "ES-9 … for Husnu Matthew Collins … ES-11 … for PERSON_3941_NAME"; SQL line 116 ES-8/ES-10). Check: 50,865+30,518 = 81,383 and 25,432+6,104 = 31,536, the Nov 2024 figures | ENG-2440 "ES-8 81,383 options", ENG-2449 "ES-10 31,536 options" (no shares); ENG-2446 31,536 shares and ENG-2447 86,470 shares (no options). Final response: "I couldn't find grants ES-9 or ES-11"; sheet note claims a false 9,155-share gap "to reconcile in Carta" | **MATERIAL_FAIL** (cause A) |
| R4 | Told = direct, delivered written message about the closing from one of the three founders (notes) | Already told: Griffin funds (Feb 9 to partner), ENG-2447 (Feb 12 "Harmony" to Husnu Akin), **ENG-2446 (Robert's Feb 12 "we're closing the company" to PERSON_3941_EMAIL, cc Leonard; SQL line 102)**; ENG-2457 not told (bounce) | Griffin, ENG-2447 Already told ✓; ENG-2457 Closing and last day, draft to issue email ✓. **ENG-2446 labeled Closing, Todo, extra draft (ev. 799, 838).** The run looked for "told" only in Leonard's own sent mail (`in:sent after:2026/02/08`, ev. 393), so it never saw Robert's message | MET for 4 traps; **MATERIAL_FAIL for ENG-2446** (cause C) |
| R5 | Family rule (#winddown reply, SQL lines 57–59): one note to whoever handles it for a family covers the other lines, marked Covered; the note says what each holds | PERSON_2260 (ENG-2443) sent Leonard all three family investors (Patrick Lewis, himself, [27652]) on Jun 30, 2023 (`…_1770141224265557526.json` /messages/1). ENG-2444/2445 Covered and Done with why; ENG-2443 note lists all three holdings | Run read the rule (ev. 25) but never found the family list; final response says "I couldn't confirm any angel family, so no lines are marked Covered". Drafts went to ENG-2445 and to Patrick (ENG-2444); the ENG-2443 note gives only its own 25,432; ENG-2444/2445 Todo | **MATERIAL_FAIL** (cause D) |
| R6 | KPMG reply-all, as of Dec 31, 2025: (1) shares by class **showing what each fund holds**; (2) option lines with total; (3) shares + options; (4) events (KPMG request + clarification, SQL lines 77, 83) | (1) Common 6,000,000; Seed 3,051,879: Griffin II 2,662,255, Side Fund 84,438 (`…_1771880236343640719.json` /messages/0); (2) 16 lines incl. ES-8 30,518, ES-9 61,038, ES-10 6,104, ES-11 6,104; total 243,757; (3) 9,295,636; (4) no financing, winding down | Sent twice (ev. 890 reply-all, ev. 899 resend with CCs). (1) Seed 3,051,879 ✓ but **no fund split** ("we will confirm the split … separately"); (2) ES-8 81,383, ES-10 31,536, ES-9/ES-11 missing, total **252,912**; (3) **9,304,791**; (4) ✓ | **MATERIAL_FAIL**: items 2–3 (cause A), item 1 (cause B); sent, so it can't be quietly fixed |
| R7 | Sheet totals and counts (Sunset email; notes "counts go by rows") | Options outstanding today from correct lines; counts Nothing 5 / Already told 5 / Covered 2 / Closing 5 / Last day 5 / Closing and last day 4 | Options 173,269 (built on wrong advisor lines); counts Closing 9 / Already told 3 / no Covered | MATERIAL_FAIL, knock-on of A, C, D (and the excluded ENG-2440 item, §5) |
| R8 | Holder notes as Gmail drafts, unsent, one per person owed; holding, closing if not told, last day; unanswered holding questions answered (notes) | 14 drafts; Claire's Feb 12 equity question answered | 17 drafts (ev. 771–805), none sent. Employee and Calvin/[0051]/[0068]/Oliver drafts correct; Claire's answers her question ✓. Wrong: ENG-2440/2449 holdings; extra drafts to ENG-2445, ENG-2446 and Patrick; ENG-2443 family note incomplete | MET for 11; failures counted under A, C, D |
| R9 | Linear states and "why" comments (project description) | Todo 14, Done 7, Canceled 5 | Todo 17, Done 4, Canceled 5 (ev. 812–863); why-comments on every non-note issue | Wrong: ENG-2444, 2445, 2446 (A/C/D knock-ons); ENG-2440 excluded; ENG-2442 confounded (§5) |
| R10 | Order: earliest last day goes first; #winddown reply under the list (notes) | Calvin first (Feb 20), then [0051] (Feb 21) | Thread reply on `1770934638.035469` (ev. 892) names Calvin first, then [0051]; its counts repeat R7's errors | MET (order); counts are a knock-on |
| R11 | Griffin heads-up: reply-all on the partner's Feb 12 Board position mail, asking for the preferred vote (notes) | Reply-all asking for the vote on the dissolution | Reply-all on `1856958794180374704` (ev. 888) asking for the preferred vote | MET |
| R12 | Investor letter from the #winddown draft, outline sections, close-out folder, shared with Robert (notes) | Updated letter, five outline sections | Doc created (ev. 760), moved to `d_601064334a0b493022fe83` (ev. 762), shared with Robert (ev. 764); follows the outline | MET |
| R13 | Sharing (notes + #winddown "the sheet goes to you as well as Robert") | Sheet → Robert and Arthur; letter → Robert | Ev. 754, 756, 764 | MET |
| R14 | Seed total: go by the ledger (Jan 14 thread reply, SQL line 48) | 3,051,879, not 3,051,882 or the pro forma's figure | 3,051,879 in sheet and KPMG | MET |
| R15 | Final response | Accurate summary | Accurate about what it did; openly flags the gaps it couldn't resolve (ES-9/ES-11, fund split, family) | MET (flagging doesn't repair the sent KPMG figures) |

## 3. Grouped failures and independent causes

- **A. Advisor-angel holdings wrong (never found the 2023 disclosure schedule or the ES-9/ES-11 Carta notice; read the Nov 2024 totals as one security).** Deciding records: `threads/leonard@harmonygames.co_1773160163779741845.json` /messages/1 (30,518 / 61,038 / 6,104 / 6,104) and `…_1782897835407336831.json` /messages/0 (ES-9 → Husnu Matthew Collins, ES-11 → PERSON_3941). Both are in Leonard's own mailbox. Affects 4 sheet rows, the ENG-2440/2449 drafts, the options total, the false "9,155 to reconcile" note and KPMG items 2 and 3, which were sent.
- **B. Griffin per-fund split missing from the KPMG reply.** KPMG item 1 asks "showing what each fund holds". The split (2,662,255 / 84,438) is in Leonard's Jul 2023 closing mail `…_1771880236343640719.json`. The run's "Side Fund" search (ev. 575) returned newsletters, and it deferred the split. Smaller cause: one line of one sent deliverable.
- **C. ENG-2446 already told by Robert, missed.** Deciding record: SQL line 102 (Robert → PERSON_3941_EMAIL, cc Leonard, Feb 12 23:41Z, "we're closing the company"). Wrong label, Todo instead of Done, and an extra holder note to someone already told.
- **D. Family rule not applied.** The rule was read, but the family list (`…_1770141224265557526.json`) was never found. ENG-2444/2445 should be Covered/Done and the ENG-2443 note should state all three holdings. Instead there were two extra notes and two wrong Linear states.

Four independent causes (different records and decisions; a run could make any one without the others).

## 4. Correct work and usability

The run passed the task's headline traps: Calvin's Carta extension (goes first), the bounced ENG-2457 letter, the Husnu Akin alias for ENG-2447 and the ledger seed total. All 14 employee option lines (vested amounts, last days, labels, notes) are right, and so are the five lapsed lines with why-comments, Claire's unanswered question, the Griffin heads-up, the investor letter, sharing, the #winddown order and KPMG item 4. About 19 of 26 sheet rows are fully right. The sheet and drafts are usable after correcting the advisor rows, the ENG-2446 row and the family rows. The KPMG confirmation needs a corrected re-send.

## 5. Task/environment defects, exclusions and unassessed scope

- **ENG-2440 "told" status: UNASSESSED, excluded.** The expected "Already told" rests on Leonard's Feb 9 message in `D04UC0UEN2V` ("shut down the company we decided"). That conversation lists 5 members (`channels.json` /410), and linking its Slack user `PERSON_3335_SLACK_ID` (no name or email in `users.json` /34) to ENG-2440 depends on anonymized name tokens that don't match ([PERSON_NAME_6550] / [PERSON_NAME_0090] / [PERSON_NAME_0089]). Treating ENG-2440 as not told is a reasonable reading. Its holdings error still counts under A.
- **ENG-2442 merged into Patrick Lewis: confounded, excluded from the failed share.** The base data puts the address `patrick@harmonygames.co` on both the Istanbul family investor and a Solsten "patrick" who signs with PERSON_0693_EMAIL (`…_1770053656612413311.json` /messages/9). That is an anonymization collision. Merging the two contradicts "one issue per holder", but the collision invites it. It is not listed in the known-data-issues list.
- KPMG sent twice (the first reply-all dropped the CCs): minor, same figures.
- Advisor vesting start dates aren't visible. The full-grant treatment matches both the expected answer and KPMG's rule, so it isn't scored.

## 6. Narrow miss, failure pattern, tool calls

- **Narrow miss: NO.** 4 independent causes (A, B, C, D). Failed share ≈ 30%, resting on about 70 core items (26 rows, 14 drafts, 26 Linear states, sheet totals and counts, KPMG items 1–4, 3 sends, letter), weighted with KPMG and holdings above Linear states. Difficulty mode medium, loss 15%.
- **Failure-pattern risk: NO.** Traps, each with its share of the weighted answer and this run's result: advisor holdings (A) ≈ 18%, wrong; ledger seed total ≈ 6%, right; Calvin extension ≈ 7%, right; family/Covered (D) ≈ 7%, wrong; ENG-2457 bounce ≈ 4%, right; Husnu Akin alias ≈ 4%, right; Robert told ENG-2446 (C) ≈ 4%, wrong; Griffin split (B) ≈ 3%, wrong; ENG-2440 DM ≈ 4%, excluded; Claire's question ≈ 2%, right. Largest ≈ 18% (under 30%).
- **Tool calls: 219** (201 by the main agent, 18 by sub-agents; both count). Task type long-horizon, minimum 100, 90% threshold 90. Not under 90% of the minimum.

## 7. Score rationale

Score **4 (Hard, NON-FAIL)**. Four genuine retrieval and synthesis failures need correction across the sheet (7 rows, totals, counts), the drafts (2 wrong holdings, 3 extra notes, 1 incomplete family note), Linear (3 states) and an already-sent KPMG confirmation with wrong option lines, wrong totals and no fund split. Why not 3: the fix isn't bounded to one item. It spans every deliverable that reports holdings, and the external auditor already has wrong figures. Why not 5: the central decisions are mostly right (the headline traps, all employee lines, the order, the lapsed lines, the letter and the Griffin heads-up), so much of the core result stays usable.

### FINAL VERDICT: NON-FAIL
Assessment version: model-aware-v3
Assessed model: Opus
Assessment mode: OPUS_OBSERVED
Score: 4
Execution status: COMPLETE
Difficulty: Hard
Gate decision: PROCEED
Gate reason: OBSERVED_OPUS_FAILURE
Evaluator model: Claude Opus 5.5 (claude-opus-5-5), standard effort
Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
Next action: Proceed with dependent authoring (/oe, /rubric); keep the observed failure evidence. Consider settling the ENG-2440 told evidence with a record that names the holder directly.
Evidence limits: One run only; no average-score or repeatability claim. The export has no initial prompt event (task match shown by behavior). ENG-2440 told status was not scored, and the ENG-2442 merge is confounded by a base-data address collision.

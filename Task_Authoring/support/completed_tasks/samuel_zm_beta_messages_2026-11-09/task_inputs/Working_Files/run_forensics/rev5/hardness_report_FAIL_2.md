## HARDNESS EVALUATION REPORT (Opus observed)

### Task: Samuel works through Leonard's Sep 30 DM: a Go/Hold/Drop call on every PNs Beta row and every filed phone-message ask, a new sheet and one-page note in his Drive folder, ticket comments and moves, new tickets, a Go checklist on the push notifications card, emails to askers, and the counts back in the DM

### FINAL VERDICT: FAIL
Assessment version: model-aware-v3
Assessed model: Opus
Assessment mode: OPUS_OBSERVED
Score: 2
Execution status: COMPLETE
Difficulty: Easy
Gate decision: HOLD
Gate reason: INSUFFICIENT_DIFFICULTY
Evaluator model: Claude Opus 5.5 (claude-opus-5-5), default effort
Next action: Add a second, independent trap in a different part of the task, get a new unhinted Opus run and send /hardness again.
Evidence limits: One run only; no average-score or repeatability claim.
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

**Why Easy:** this run's only miss was one cause (it never opened ZOM-542 or ZOM-556, so it missed the two phone-message asks Brian and Julia left as comments on those tickets), and it got about 90% of the task right. The baseline averages six runs, and runs that avoid this one miss score above the Medium limit (85%). Add a second, independent trap in a different part of the task (another item, source or decision), get a new unhinted Opus run and send /hardness again. See the [hardness guide, Part 8](/?guide=hardness#part-8-if-the-run-comes-back-too-easy).

### Provenance

| Input | Path | SHA-256 |
|---|---|---|
| Prompt (rev 6) | Evals/task_inputs/04_Prompt.txt | 22df2abfec652efab31a87a9cfb74b77632113a98dae00225368f31f29b66ae9 |
| Task details | Evals/task_inputs/00_Task_Assigned_Inputs.md | 600dce16d3f6923ea292ae60c066293120b5e82f0d46a81d142d8a51fdeacb26 |
| Injection SQL (rev 5) | Evals/task_inputs/01_Universe_Inject.sql | c40a78a9db79b113d51c059b0e097d4b87a94361c24d9723321f64d002da1d16 |
| Opus run ("trajectory-run-1 (5).json") | Evals/task_inputs/opus/trajectory.json | 36dde045066c46dc943c0a776edd2e97dd009343d1d7324107abec3189c3182f |
| Reference files | none (the prompt references no attachment) | N/A |

- Model: `claude-opus-5-5[1m]` (system init `model`; result `modelUsage.canonicalModel: claude-opus-5-5`). Session e0cfa0c6-c82d-4993-be4c-0ca672fa5311. Result `subtype: success`, `terminal_reason: completed`, 189 turns, no sub-agents.
- Unhinted: the first user message is a tool result; the run starts from the persona's own Slack profile and finds Leonard's DM itself. No hint text in the export. The run's task matches the saved prompt (DM D06L58XCVKK, the PN sheet, DES-314, the card and the folder all line up).
- Universe: Universe_SynthCut (hg4-synth-sep30cut v16), manifest `Evals/references/universes/synthcut/universe_manifest.json`. The run's tool results show the SQL overlay applied (DES-313…346, the injected Leonard DM, the rule doc f_dc45e0e5a8b8635c1b82b2).
- Assignment: Long-horizon, difficulty mode Medium (loss 15%, baseline limit 85%).
- Evidence contract: stage-evidence-v1. Reused evidence: the worked answer in `Evals/task_inputs/reports/1_prompt.md` (same prompt and SQL hashes). Every fact that decides this score was re-checked against the SQL and the run (the ZOM comments at SQL lines 294–298, the audience comments, and each write payload).

### Requirement map (authority_contract: prompt-incorporation-v1)

The prompt incorporates Leonard's Sep 30 DM ("has the whole job in it ... do all of it"), and the DM incorporates the "Beta message rule" doc ("make a call on each one using the message rule doc"). The rule doc points to Vincent's QA note, Robert's permission-ask call and the ZM ROADMAP board ("unless the roadmap says otherwise" → card 79 comment). No unincorporated policy was used.

| # | Requirement | Expected | Observed (run location) | Outcome |
|---|---|---|---|---|
| R1 | Scope: every PNs Beta row + every filed phone-message ask | 35 messages: 14 sheet rows + 19 DES asks + 2 comment asks (ZOM-542 cmt_f1b8a109dfa70cdc4565, Brian, daily Boss Arena attempts refill; ZOM-556 cmt_2b519285937e7fa79453, Julia, gift-streak reset reminder) | 33 messages. It never opened ZOM-542 or ZOM-556. ZOM-556 came up in its own `linear_list_issues` "notification push PN reminder" search (#56), and DES-338 relates to it, but the run didn't follow it. The final reply says "I found no asks on Trello cards; they were all on tickets." | MATERIAL_FAIL |
| R2 | Calls on the 33 covered messages | Go: DES-315/316/317. Drop: DES-324/325/326/327/344/345/346. Hold: DES-313, 318–323, 328–343 with the named test | All 33 calls and failed tests match (sheet payload #106; comments #118–#150) | MET |
| R3 | Trap: Finish first mission, test 4 (permission ask after level 20) | Hold, test 4 | Hold, test 4 (Robert's Sep 29 post read at #63–#64) | MET |
| R4 | Trap: Plague Race, test 6 (Vincent's correction: iOS store build never arrived) | Hold, test 6 | Hold, test 6 | MET |
| R5 | Trap: Weekly Leaderboard reset, test 5 (counts 7 days from leaving) | Hold, test 5 | Hold, test 5 | MET |
| R6 | Trap: Win & Collect row already has a ticket under another name | Use DES-313, no duplicate | Used DES-313, no new ticket | MET |
| R7 | Trap: Lapsed 14 days already covered | Drop, naming Lapsed 7 days | Drop, names DES-317 | MET |
| R8 | Sheet in Samuel's folder, 7 columns, Audience from the ask, headline and string change only for Go rows | Folder d_caafeec2804b3a67ce46aa | Created (#105–#106), moved to the folder (#108). Columns exact. Every audience matches the ask comment. Go headlines: Full Ammo Reloaded! 🔫 / The Horde Is Growing… 🧟‍♂️ / Your Squad Needs You Back (string change Yes, DES-347) | MET for the rows written; 2 rows missing (R1) |
| R9 | One-page note | Sep 15 cohort D1/D7 per platform (iOS 31.65/9.28, Android 37.86/10.68); lapsed day 1, 7, 14, 21, 28; client-scheduled Holds DES-318/319/320 with reason | All present and correct (#109–#111). Count line says Hold 23 (R1 knock-on) | MET (count knock-on under R1) |
| R10 | Call comment on every ticket and move it | Drop → Canceled; Go unchanged; Hold → Backlog unassigned (card 79 overrides the rule doc's Todo) | 33 comments. 7 Canceled, 23 Backlog with assignee null, Go untouched (#151–#180) | MET |
| R11 | New tickets: one per ask with no ticket (no duplicates), plus a string ticket for a changed Go headline | 3 under DES-314: the 2 comment asks and the Lapsed 7 days string ticket | String ticket DES-347 under DES-314 (#103). No tickets for the 2 comment asks | MATERIAL_FAIL (same cause as R1) |
| R12 | Go checklist on the push notifications card | 3 Go items on card 6851a769c65dc0017a227bb7 | Checklist with the 3 Go items (#114–#117) | MET |
| R13 | Email each asker except Leonard about their asks | 7 emails (Brian, Robert, Oliver, Julia, Owen, Calvin, Martin) | 7 emails sent (#181–#187). Brian's leaves out his ZOM-542 ask and Julia's leaves out her ZOM-556 ask | MINOR_GAP, knock-on of R1 |
| R14 | Counts in the same DM | Go 3, Hold 25, Drop 7 in D06L58XCVKK | Posted "Go 3, Hold 23, Drop 7" to D06L58XCVKK (#188) | MATERIAL_FAIL (same cause as R1) |
| R15 | Final response | Summary of the work | Accurate about what it did; repeats Hold 23 | Knock-on of R1 |

Output capability: every write used a cataloged tool and got a successful result (SUPPORTED). No task or environment defect affected the run. One extra, unrequested write: it shared both files read-only with the whole harmonygames.co domain (#112, #113). It isn't scored and doesn't change any graded result.

### Grouped failures and independent causes

- **Cause 1 (the only one): it missed the two comment asks on ZOM-542 and ZOM-556.** The DM asks for "every ask for a new phone message that's been filed on a ticket or a card". Two asks are comments on Zombie Match bug tickets, not DES children. Each is tied to a DES ask by a relation (ZOM-542 ↔ DES-330, ZOM-556 ↔ DES-338). Knock-ons: 2 missing sheet rows (Hold, test 3), 2 missing Hold tickets under DES-314, the wrong Hold count in the DM, sheet, note and final reply (23 instead of 25), and incomplete emails to Brian and Julia.
- Independent causes: **1**.

**Narrow miss: YES.** 1 independent cause. Failed share about 10%, from a weighted core of about 190 points: 35 message calls ×3, 35 ticket comments/moves ×1, 3 new tickets ×3, DM counts ×5, note parts 11, 7 emails ×2, checklist 3, sheet/note placement 6. Wrong: 2 calls (6), DM counts (5), 2 new tickets (6), 2 ticket writes (2), 2 partial emails (2) = 21 points, about 11%. Rounded to 10% because the email misses are partial. Difficulty mode Medium, loss 15%. 10% is below 15%, so the score is 2.

**Failure-pattern risk: NO.** Traps, each trap's share of the weighted answer, and whether this run got it right:
1. Hold tickets → Backlog unassigned (card 79 overrides the rule doc's Todo): about 13% (25 ticket moves). Right.
2. Comment asks on ZOM-542 / ZOM-556 (items outside the DES-314 filter): about 11%. Wrong.
3. Lapsed 7 days headline correction → string ticket DES-347: about 5%. Right.
4. Win & Collect already covered by DES-313 (alias, no duplicate): about 4%. Right.
5. Finish first mission, test 4 (Robert's permission-ask call): about 3%. Right.
6. Plague Race, test 6 (Vincent's Sep 29 iOS correction): about 3%. Right.
7. Weekly Leaderboard reset, test 5 (PR #248 note: counts from leaving): about 3%. Right.
8. Lapsed 14 days covered by the weekly repeat (Drop, not Hold): about 2%. Right.
9. Test 1 drops via the roadmap (Hourly Coins in Backlog, Axe Arena and rewarded ads moved to Oct 21, Domino-only events): about 6%. Right.

Largest trap share: about 13%, under 30%.

**Tool calls: 188** (188 by the main agent, 0 by sub-agents). Task type Long-Horizon, minimum 100. Not under 90% of the minimum (90).

### Correct work and usability

Everything else is right. Every call and failed test on the 33 messages it covered is correct, including all the decoys (Plague Race's iOS correction, the level-20 permission ask, the leaderboard's wrong day, the Win & Collect alias, the day-14 coverage, the roadmap moves). The Backlog-unassigned Hold rule is applied to all 23 Hold tickets. The note's retention figures and lapsed schedule are exact. The string ticket, checklist, comments and emails are right. The result is usable after a small fix: add two rows, two tickets, two email lines and correct the count.

### Score rationale

The band table alone would give 3: one consequential failure that needs a bounded correction, with substantial correct work. The narrow-miss rule applies, though. Every material failure traces to one independent cause, and the failed share (about 10%) is below the Medium loss (15%), so the score is **2 (Easy, FAIL, HOLD)**. Runs that find the two comment asks would score close to 100%. Runs that miss them would still score about 90%, above the 85% limit. Score 1 doesn't fit because the miss is real, consequential and comes from a discoverable record (ZOM-556 showed up in the run's own search results).

### Task/environment defects

None found. The tools worked, the overlay was present, and both missed asks were discoverable (base tickets ZOM-542 at linear/data.json /issues/3617 and ZOM-556 at /issues/3632, injected comments and relations at SQL lines 294–298).

### Unassessed scope

None material. The sheet and note were judged from the exact write payloads and successful results.

### Suggested revisions (advice; from the hardness guide, Part 8 and Part 3)

Opus got every per-ticket decoy right, so don't add more traps of the kind it already beat (more per-ticket corrections in Arthur's or Vincent's comments). Ideas for a second, independent trap in another part of the task:
- **Item outside the obvious filter, on Trello** (Part 3, 7): the DM says "a ticket or a card", and this run checked cards but found none. A phone-message ask in a comment on a ZM ROADMAP card (not the push notifications card) would rest on a different record than the ZOM comments.
- **Work someone already did** (Part 3, 9): for example, a record showing one Go message is already ticked or already on a checklist, so creating it again is the error.
- **A correction somewhere else that changes a number** (Part 3, 2 and 4): for example, a later warehouse note or a Slack correction that changes which cohort week or platform split the note should use. Snowflake can't be changed by injection, so base the correction on records that agree with it.
Don't spell any rule out in the prompt (Part 8).

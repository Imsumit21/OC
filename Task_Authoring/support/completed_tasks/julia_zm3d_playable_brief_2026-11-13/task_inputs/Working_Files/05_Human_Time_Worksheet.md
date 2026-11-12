# Human Time Worksheet — julia_zm3d_playable_brief

Pass: post-baseline refresh        Tier: Long-Horizon
Universe: synth-cut · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Hours: 19.00

Basis:
- The work 04_Prompt.txt asks for (sha256 33c721d60945): do everything Frederick's Sep 30 message asks, which covers a brief, a hand-off list with a state for every line of the pack, ticket moves and comments for the lines that are owed, sharing, the count for each state, and the two links.
- The work is done by hand in Julia's own accounts: no search, scripts or AI.
- Counts come from rev2 (01_Universe_Inject.sql 7d1f2aaeb29c, solver/truth.json): 96 lines, Delivered 8, Ready 39, Owed 49. The person does not start out knowing where anything is.
- Friction: none (03_Error_Async_Config.txt), so there is no workaround line.
- Rows computed as volume × rate are rounded to the nearest 5 minutes (the rates are approximate); the others are stated estimates.
- Refresh inputs: 08_Oracle_Events.md (130 events: 49 moves, 49 comments, 8 shares, 2 messages, the sheet and the brief) and the six rev2 baseline runs in 07_Baseline_Trajectories (12_Difficulty_Stats.txt).
- What changed from the first pass: the hours did not (19.00 then, 19.00 now). One row changed kind: the pull-request check was a read and is now a dead end, because no Oracle Event and no criterion uses a pull request, while 5 of 6 baseline runs still went to the repository; its minutes are unchanged. Counts that differ from the first pass: #zombie-match3d 69 then, 76 now; #zm-animations 66 then, 68 now; DM with Robert 287 then, 288 now; DM with Brian 37 then, 39 now. The first pass cut some windows on UTC days; this pass cuts every window on Pacific days.

| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|
| Read the request, Frederick's DM and his hand-off notes | read | 3 records: prompt 246 chars, DM 789 chars, notes 2180 chars with 3 state tests | careful read: the tests are applied to every line | 30 |
| Read Brian's pack list row by row | read | 96 rows, 5 columns | about half a minute per row | 45 |
| Skim Slack where the playable and its assets are discussed | read | 1005 messages: the PlayableX channel (all of it) 198, #zombie-design 292, #zombie-art 34, #zombie-match3d 76, #zm-animations 68, DM with Frederick (Sep) 4, DM with Robert 288, DM with Brian 39; 6 seeded (Julia is a member of each) | ≈ 3,000 messages/h (worked-example skim anchor) | 20 |
| Read the vendor's threads past their apparent end: formats and asset list, the pause and the new start, the first playable's sound exchange | read | 3 threads in a channel of 198 messages (119 of them from March and April) | ≈ 20 min each (decisive-thread anchor) | 60 |
| Open each pack ticket, read Brian's note, apply the three tests | read | 97 tickets (the pack ticket and 96 children), 96 notes | 3 min each: one ticket, one short note (below the 8 to 15 min anchor, which is for 2 to 3 surfaces) | 290 |
| List Julia's Drive for the notes, the pack list, the deck and anything else about the pack | read | 191 files (28 owned, 158 shared, 5 seeded) | ≈ 450 items/h | 25 |
| Read Calvin's sound sources sheet and Brian's log of the outgoing folder against the tickets | read | 8 sheet rows, 4 dated log lines | 15 min for both | 15 |
| Read the design page and its comments for the tray and the loss rule; the reference-level deck | read | 1 page, 2 comments, 4 slides | 20 min | 20 |
| Find the kickoff hold and its attendees, and the vendor's intake address | read | 1 event with 4 attendees, 1 contact | 10 min | 10 |
| T1 Thursday's exports look ready until a colleague's post is read against the vendor's format rule | dead end | 12 tickets, 1 post, 1 rule message | ≈ 20 min (decisive-thread anchor) | 20 |
| T2 Friday's bathroom files look ready until Robert's note | dead end | 12 tickets, 1 DM message | 15 min | 15 |
| T3 three recoloured models: Owed on Robert's post until the log says they went again | dead end | 3 tickets, Robert's post, the log entry | 15 min | 15 |
| T7 the zipped instruments: the folder log says the zip will not unpack | dead end | 8 tickets, 1 log line | 10 min | 10 |
| T4 two sounds are not ours to pass on | dead end | 2 tickets, 2 sheet rows | 10 min | 10 |
| T18 the pull requests since the first zip, checked for the recoloured models | dead end | 22 pull requests created 22 to 30 Sep | ≈ 40 min (worked-example PR anchor) | 40 |
| T18 other objects named in the recolour pull requests | dead end | 3 object names checked against 96 lines | 5 min | 5 |
| T5 the board's eight: the first list against a later reply under another post | dead end | 2 posts, 1 thread of 3 messages | ≈ 20 min (decisive-thread anchor) | 20 |
| T8, T12 stale start dates and the first playable's format rule | dead end | 3 dates, 2 rule messages | 5 min each pair | 10 |
| T9 the six-slot proposal on the design page | dead end | 2 comments | 5 min | 5 |
| T10, T16 the zombie pack 'not exported correctly', the duck and the rocket launcher | dead end | 3 vendor messages, 2 tickets | 5 min each | 15 |
| T11, T17 Leonard's Playable Kickoff card and his Playable Feedback doc | dead end | 1 card, 1 doc | 5 min each | 10 |
| T13, T14, T15 the board on the reference-level deck and earlier board ideas | dead end | 1 slide, 3 messages | 10 min | 10 |
| T19 object tickets with the same titles as pack lines | dead end | 51 tickets under one parent | ≈ 450 items/h, then 3 opened | 10 |
| T6 board set for the lines that are not board items | dead end | 12 lines | 5 min | 5 |
| Go back over the lines each later statement overturns: state, what is owed, who has it | re-read | 39 lines (12 + 12 + 3 + 2 + 8 states, 2 board-set cells) | 2 min each | 80 |
| Type the hand-off list | write | 1 sheet, 96 rows × 7 columns | 1.25 min per row | 120 |
| Write the brief | write | 1 doc, 10 required facts | 60 min | 60 |
| Move each Owed line's ticket to Todo and write its comment | write | 49 state changes, 49 comments | 3 min per ticket (comments repeat within a group) | 145 |
| Share both files | write | 2 files × 4 recipients = 8 shares | 1 min each | 10 |
| Send Frederick the count for each state; post both links in the vendor channel | write | 2 messages | 5 min each | 10 |
| Total |  |  |  | 1140 = 19.00 h |

Tier check: in band (Long-Horizon ≈ 12–24 h; 19.00 h). No trigger.
- Reads 515 min, dead ends 200 min, re-reading 80 min, writes 345 min.
- The manifest's call budget is 252; most of the hours are 96 manual decisions, a 96-row sheet typed by hand and 98 per-ticket writes, which an agent makes in far fewer minutes each.
Baseline count basis (post-baseline only): no golden run, so the average of the six completed runs, 220 counted calls (196 to 244), against the Long-Horizon tier of 100 to 500+. In band, the same tier the hours give.

Condensed breakdown (one line per sub-task group, facts only; the screen text is in the task slot 05_Human_Time.md, built from this table by the same script):
- Rules and list: the message, the notes, 96 pack-list rows 75 min
- Slack: skim 1005 messages at 3,000/h, 3 vendor threads read through 80 min
- 96 tickets, one note each, 3 min each 290 min
- Drive listing 191 files, sound sheet, folder log 40 min
- Design page, deck, kickoff hold, contact 30 min
- 15 dead ends: notes that look ready, 22 pull requests, the first board list, stale dates, look-alike tickets and card 200 min
- Re-deciding 39 overturned lines 80 min
- Sheet of 96 rows and the brief 180 min
- 49 ticket moves with comments, 8 shares, 2 messages 165 min
- Total 1,140 min = 19.00 h

Condensed breakdown length: 599 characters (field accepts 50–2,000)
Screen text in 05_Human_Time.md: one paragraph, 1608 characters, hours 19.00; its sub-task minutes add to 1,140.

Sources measured: hg.py and persona_view.py, listed here, all run again in this pass.
- hg.py search search slack '17' --key ts with --file messages/CHANNEL/MONTH.json for every month file of C08H78VJG80, C090N54TG79, C08R8CHB0QL, C0880U9751A, C09ATAJ220H, D05SD5QLG94, D05GU6L0XFH, D076RBM29JS; windows are Pacific days (22 Sep 00:00 PT to 1 Oct 00:00 PT; September for the DM with Frederick; the whole PlayableX channel). Scan complete for each.
- persona_view.py can-see julia_lawson slack for those eight conversations (YES for each); persona_view.py reach julia_lawson: Drive owned 28, shared 158.
- hg.py search search github '2025-09-' --pointer /pull_requests --key created_at (70 in September, 22 created 22 to 30 Sep); hg.py search search linear ZOM-97 --key parent_id (51).
- 01_Universe_Inject.sql rows (rev2), parsed with tools/base_check.parse_sql, never run: 97 Design-team tickets, 96 notes, 6 Slack messages, 5 Drive files, 1 sheet of 96 rows.
- Raw figures: humantime_gen/out/volumes.json (this pass); plan/out/humantime_volumes.json holds the first pass and was used only to report differences.

## Self-review

Checked in order against `10_Long Horizon Guidelines - V2.md` §5 and §10, the Pre-QC list and the field's own text.

| Area | Counter-reading | Evidence that resolves it | Verdict |
|---|---|---|---|
| Inflated | Three minutes for each of 96 tickets and 147 minutes of ticket writes are padding. | each line has its own ticket and note (DES-314 to DES-409) and every Owed line needs a move and a comment (hand-off notes f_8c1d0bca1d1d5fde4c5008); the six baseline runs each read 96 or 97 ticket comment lists, one per line (run-1 to run-6 in run_forensics/rev2/baseline/summary.json); the per-record rate is below the 8 to 15 min anchor because there is one surface, and the reason is stated on the row | holds |
| Solution-path estimate | The table assumes the person already knows where the later statements are, and the pull-request check is not on the Oracle path at all. | every manifest trap T1 to T19 has a dead-end line (15 rows, 200 min), and the places are found by the skim and listing rows: 1005 messages, 191 Drive files (C0880U9751A/1758906517.912099, f_faf4d7c167d14a1127dcc3). The 22 pull requests are counted as a dead end, not as required reading: 08_Oracle_Events.md never opens one, and 5 of 6 baseline runs still did | holds |
| Evaluator-wide volume | The Slack and Drive counts could be universe-wide, not Julia's. | only conversations she is a member of are counted (persona_view can-see YES for all eight, e.g. C08H78VJG80, C0880U9751A, D05GU6L0XFH); Drive is her owned and shared files from persona_view reach, plus the seeded files shared with her (f_8c1d0bca1d1d5fde4c5008); counts stop at 1 Oct 00:00 PT | holds |
| Tier mismatch | 19.00 h could sit outside Long-Horizon, or the baseline could show a different tier than the hours. | 12 to 24 h is the band and 19.00 h is inside it; the baseline average is 220 counted calls, lowest 196 (12_Difficulty_Stats.txt), inside the Long-Horizon tier as well; no trigger, nothing tuned | holds |
| Linter reading | From a 46-word prompt and the SQL alone, 19 hours could look more than three times too high. | the SQL shows 97 tickets with 96 notes under DES-313 and a 96-row list (f_956e60ec7f2f7977d98934); the screen text in 05_Human_Time.md names those volumes, the 49 ticket writes and the dead ends in plain words, with no internal ids | holds; the reasoning names the volumes |
| Unlisted work | All six baseline runs searched mail (4, 1, 1, 2, 2, 1 calls for run-1 to run-6), so a mail sweep is missing from the table. | no Oracle Event reads mail and no manifest trap sits there; adding a line would count work the prompt does not require (gate 1 of the playbook), so none is added and the hours are not stretched | holds; counter-reading recorded |

Every volume was measured in this run (sources above); the first-pass figures were leads only. The sum was recomputed by the generator (1140 min) and both character counts were taken from the text as written. The screen text is one paragraph, as in the completed tasks, and is checked by the generator: 50 to 2,000 characters, its sub-task minutes add to the total, no banned phrase and no internal id. Unresolved: none.

```
STAGE GATE humantime: PASS — Task_Authoring/task_inputs · 05_Human_Time_Worksheet.md#3af26b40477d · 04_Prompt.txt#33c721d60945 · 00_Assigments.md#82494197a841 · 08_Oracle_Events.md#5395e0f081a0 · 07_Baseline_Trajectories#5008a5ea4eae · 12_Difficulty_Stats.txt#6d15f1b10721 · __context__#3246c54345b9 · __assignment__#70579cebc8fc · __policy__#dc4ab5df3cdd · __gate_policy__#1747d7aa5ab8 · __review__#b62863bc4291 · blocking 0 · warnings 1 · checks 19
[PASS] assignment.v3_context: Julia Lawson / Product Manager; hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 05_Human_Time_Worksheet.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 00_Assigments.md, 08_Oracle_Events.md, 07_Baseline_Trajectories, 12_Difficulty_Stats.txt)
[PASS] chain.prompt-check: upstream 'prompt-check' PASS pasted and current (04_Prompt_Check.md#122488ae4ff9, 04_Prompt.txt#33c721d60945, 04_Prompt_Writing_Brief.md#d732d0390c8d, __context__#3246c54345b9, __assignment__#70579cebc8fc, __policy__#dc4ab5df3cdd, __gate_policy__#1747d7aa5ab8, __review__#f555a5b9a0f7)
[PASS] structure.placeholders: no placeholders in 05_Human_Time_Worksheet.md
[PASS] structure.arithmetic: 30 sub-tasks sum to 1140 min = 19.0 h
[PASS] evidence.volumes: every sub-task has a measured volume
[PASS] structure.kinds: dead-end / workaround / write lines present
[PASS] structure.field_length: condensed breakdown 599 characters
[PASS] evidence.sources: volume sources name the hg.py / persona_view queries
[PASS] structure.tier_check: tier check line present
[PASS] review.counter_readings: 6 evidenced counter-readings (of 6 found; need ≥ 5) in 05_Human_Time_Worksheet.md
[PASS] review.coverage: self-review addresses all 5 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[WARN] task.folder: the task folder is the bare default `task_inputs`: give each task its own folder (`Task_Authoring/task_inputs<Label>`) and pass it to every command, so two tasks never share one [first-pass check in warn mode: reported, not blocking]
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

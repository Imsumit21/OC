# 01a Hardening Report — julia-zm3d-playable-brief (rev1)

Generated 2026-11-12 · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · universe manifest Evals/references/universes/synthcut/universe_manifest.json

## 1 · Mode, inputs and run validity

MODE B: forensics on seven Opus 5.5 runs of rev1, the platform pre-check and the six baseline rollouts. The formal Mode B request (Working_Files/mode_b_request.json) is the provisional pre-check kind, because no rubric or verifier exists yet; the six baseline runs are graded on the gradable surface as a design check (playbook B3d) and are labelled as such everywhere below.

Inputs read: 00_Assigments.md, 01_Universe_Inject.sql (rev1, sha256 78465cd474f8; the platform ran the same statements without the four header comment lines, sha256 3a76797fbde1), 01_Grounding_Dossier.md, 01_Hardness_Manifest.json, 01_Gradable_Surface.json, solver/solver.py, 03_Error_Async_Config.txt (Friction: none), 04_Prompt.txt, 06_PreCheck_Trajectory/trajectory-run-1.json, 07_Baseline_Trajectories/trajectory-run-1.json to trajectory-run-6.json, eval_reports (/injection PASS, /prompt PASS, /hardness NON-FAIL), 08_Oracle_Events.md (a local draft, not submitted).
Inputs missing: 10_Baseline_Verifier_Results.md and 09_Rubrics.json are empty and 12_Difficulty_Stats.txt does not exist, so there are no gate numbers of record; section 2 gives the surface grader's design check instead. Section 7 has no judge text to open.

The quoted /hardness report carries `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)`.

Run validity (trajectory_ledger.py; each run BOUND to rev1 as the sole revision, on seeded content seen in its results):

| Run | Export sha256 | Events | Counted calls | Model | Status | Mixed model | Result events after the final answer |
|---|---|---|---|---|---|---|---|
| precheck | 5b6f86829075 | 847 | 237 | claude-opus-5-5 | completed | False | events 840 and 846 acknowledge background timers only |
| run-1 | 930af86a99db | 708 | 244 | claude-opus-5-5 | completed | False | none |
| run-2 | 3f967a26bccf | 784 | 271 | claude-opus-5-5 | completed | False | none |
| run-3 | 5f4dfb7dc8d1 | 648 | 259 | claude-opus-5-5 | completed | False | none |
| run-4 | 677724e281cb | 644 | 245 | claude-opus-5-5 | completed | False | none |
| run-5 | 9ea0678e2792 | 648 | 234 | claude-opus-5-5 | completed | False | none |
| run-6 | 8526ee2cb238 | 765 | 272 | claude-opus-5-5 | completed | False | none |

Every message of every run is Opus 5.5; no fallback, no compaction gap. The exports carry no user prompt; each run's first calls search for Frederick's message of 30 Sep, which matches the saved prompt. Each run is bound to rev1 on seeded content found in its own results (trajectory_ledger: BOUND).

## 2 · Gate status (design check on the gradable surface; no verifier yet)

`python3 -B Task_Authoring/tools/surface_grader.py --task-dir Task_Authoring/task_inputs` on the six baseline runs (coverage 195 of 195 weight; the rubric and verifier remain the grading of record):

```text
  V3 (hard): pass_at_1 PASS 2/6 full passes; 2/6 completed = 33% | avg_weighted_pass_rate FAIL 81.8% (6 completed; 0 errored excluded) | per_rollout_sd PASS 0.171 (sample 0.187; unweighted 0.150) | failure_patterns PASS 3 pattern(s); largest 50% of 4 failing (pair
      provenance: errored_runs PASS 0 errored, 6 completed of 6 | horizon PASS golden run(s): 271, 272 | baseline_models PASS all 6 rollout slots have claude-opus-5-5 provenance
```

| Run | Score on the surface | Failed slots | Corrected |
|---|---|---|---|
| precheck | 61.0% | X1, X4, X1b, X4b, X6, X9, X16, X17, X13, X14, A1, A2, W1, W2, W4, K1, K4, B1 | 61.0% |
| run-1 | 53.3% | X2, X4, X5, X2b, X4b, X5b, X7, X9, X10, X11, X11b, X12, X17, A1, A2, W1, W2, K2, K4, K5, B6 | 53.3% |
| run-2 | 100.0% | none | 100.0% |
| run-3 | 92.3% | X13, X14, B1 | 92.3% |
| run-4 | 72.8% | X1, X1b, X6, X16, X13, X14, A1, A2, W1, W2, W4, K1, B1 | 72.8% |
| run-5 | 72.3% | X1, X1b, X6, X16, X13, X14, A1, A2, W1, W2, W4, K1, B1, D4 | 72.8% (D4 corrected) |
| run-6 | 100.0% | none | 100.0% |

Six-run average 81.8% raw, 81.9% corrected, against a cap of under 70%: the average gate fails by about 12 points. Full passes 2 of 6 (run-2, run-6); population SD 0.171; three failure patterns. The pre-check (61.0%) is not part of the six.
Correction: D4 on run-5. Its eight share calls give no role and the tool returns role reader (run-5 event 455, result event 456), so the list was shared for viewing; the decoder reads a missing role argument as a failure. Clean average: 81.9%; no failure is CONFOUNDED.
Mechanism weight share: 150 of 195 weight (76.9%) depends on a mechanism; 133 (68.2%) failed in at least one baseline run. By node: EXPORT 26, ARTHOLD 28, REVISED 18, AUDIO 28, PICKS 15, ZIP 23, shared counts 12.
Concentration: no single node drives the failures; the losses came from EXPORT (2 runs), PICKS (3), and one run that missed ARTHOLD, AUDIO and ZIP together.

## 3 · Predicted /hardness band

Pre-check: the platform's /hardness is on file: NON-FAIL, score 4, three independent causes (ASCII note, outgoing-folder doc, board swap), 253 calls.
Baseline, for the run closest to the median (run-4, 72.8%), by the procedure of Evals/1A_Hardness_Eval.md:

| Requirement | Result in run-4 | Citation |
|---|---|---|
| Find and follow the ask, the notes, the pack list and the 96 notes | MET | run-4 events 7, 18, 20, 27 |
| Brief: the eight on the board | MATERIAL_FAIL: Dynamite, not Bow (PICKS) | run-4 event 443 |
| Brief: scenario, zombies, tray, loss, sound, music, start date | MET | run-4 event 443 |
| List: 96 rows, seven columns | MET | run-4 event 440 |
| List: the 12 Thursday saves | MATERIAL_FAIL: Ready, not Owed (EXPORT) | run-4 event 440 |
| List: bathroom, colour versions, instruments, sounds, not-exported lines | MET | run-4 events 347, 265, 313, 315 |
| Tickets: Owed lines to Todo with a comment | MATERIAL_FAIL as a cascade: 40 of 52 | run-4 writes.json |
| Counts to Frederick | MATERIAL_FAIL as a cascade: 8 / 48 / 40 | run-4 event 632 |
| Shares and the channel post | MET | run-4 event 634 |

Two independent causes (EXPORT, PICKS); nothing CONFOUNDED. Predicted band 4: the wrong lines carry into the tickets, both counts and the brief, so the correction runs across the result. It is not 3 because more than one deliverable needs correcting; it is not 5 because the delivery is complete and 82 of the 96 rows are right. Runs 2 and 6 would be HOLD (everything right) and run-3 a 3 (the swap only): the task does not hold its difficulty from run to run.

## 4 · Designed-difficulty register

One row per designed node; counts are over the seven runs. A miss is cited by the event of the sheet write that carries the wrong value, a find by the event whose result first returned the deciding record.

| Node | Deciding record | Verdict counts | Missed in (run · event of the write) | Found in (run · event · call) | v2 failure kind |
|---|---|---|---|---|---|
| EXPORT | C0880U9751A/1758906517.912099 | LANDED 3 · LEAKED 4 of 7 | precheck · event 528; run-4 · event 440; run-5 · event 452 | run-1 · event 284 (slack_search_public_and_private query=from:<@EMPLOYEE_0002_SLACK_ID>, filter_date_after=2025-09-24); run-2 · event 424 (slack_search_public_and_private query=saved out); run-3 · event 304 (slack_search_public_and_private query=export after:2025-09-24); run-6 · event 259 (slack_conversations_history channel_id=C0880U9751A, oldest=1758672000) | retrieval miss where it landed; where it leaked, the post was returned by an author search, by the note's own words ('saved out'), by 'export', or by the channel history |
| ARTHOLD | D05HMBQUC8Z/1759148152.833779 | LANDED 1 · LEAKED 6 of 7 | run-1 · event 555 | precheck · event 322 (slack_search_public_and_private query=from:<@EMPLOYEE_0009_SLACK_ID> after:2025-09-23); run-2 · event 466 (slack_search_public_and_private query=from:<@EMPLOYEE_0009_SLACK_ID>, after=1758800000); run-3 · event 284 (slack_search_public_and_private query=from:<@EMPLOYEE_0009_SLACK_ID> after:2025-09-22); run-4 · event 347 (slack_search_public_and_private query=after:2025-09-24, channel_types=mpim,im); run-5 · event 270 (slack_search_public_and_private query=from:<@EMPLOYEE_0009_SLACK_ID>, filter_date_after=2025-09-23); run-6 · event 478 (slack_conversations_search_messages filter_users_from=EMPLOYEE_0009_SLACK_ID, filter_date_after=2025-09-24) | first_read: the persona's own DM, returned by a search for the author's recent messages |
| REVISED | C090N54TG79/1759189466.554739 | LEAKED 7 of 7 | none | precheck · event 80 (Bash {"command": "cd /home/agent/.claude/projects/-app/e936e530-3944-4fec-9299-e7462bf05722/too); run-1 · event 512 (slack_read_channel channel_id=C090N54TG79, oldest=1758578000); run-2 · event 306 (slack_search_public_and_private query=color, after=1758672000); run-3 · event 268 (slack_read_channel channel_id=C090N54TG79, oldest=1758800000); run-4 · event 265 (Bash {"command": "cd /home/agent/.claude/projects/-app/c4d1f766-4530-4bc8-9183-1b7605275bf7/too); run-5 · event 298 (slack_read_channel channel_id=C090N54TG79, oldest=1758672000); run-6 · event 281 (Bash {"command": "python3 -I -c \"\nimport json,sys\nd=json.load(open(sys.argv[1]));r=json.load) | same_container: a root post in the channel read for the picks |
| AUDIO | f_b2387e31d46d3a7b3fa2a9 | LANDED 1 · LEAKED 6 of 7 | run-1 · event 555 | precheck · event 434 (gsheets_values_get spreadsheetId=f_b2387e31d46d3a7b3fa2a9, range=Sources); run-2 · event 410 (gdrive_read_sheet_range spreadsheetId=f_b2387e31d46d3a7b3fa2a9); run-3 · event 335 (gdrive_read_sheet_range spreadsheetId=f_b2387e31d46d3a7b3fa2a9); run-4 · event 315 (gdrive_read_file fileId=f_b2387e31d46d3a7b3fa2a9); run-5 · event 387 (gdrive_read_sheet_range spreadsheetId=f_b2387e31d46d3a7b3fa2a9); run-6 · event 424 (gdrive_read_sheet_range spreadsheetId=f_b2387e31d46d3a7b3fa2a9) | rule stated in the notes and a sheet named with the obvious noun: a lookup |
| PICKS | C08R8CHB0QL/1758922879.243189 | LANDED 4 · LEAKED 3 of 7 | precheck · event 528; run-3 · event 409; run-4 · event 440; run-5 · event 452 | run-1 · event 321 (slack_read_thread channel_id=C08R8CHB0QL, message_ts=1758904025.123869); run-2 · event 345 (slack_conversations_replies channel_id=C08R8CHB0QL, thread_ts=1758904025.123869); run-6 · event 314 (slack_read_thread channel_id=C08R8CHB0QL, message_ts=1758904025.123869) | thread reply under a parent that names no pick; found only by opening the thread |
| ZIP | f_faf4d7c167d14a1127dcc3 | LANDED 2 · LEAKED 5 of 7 | precheck · event 528; run-1 · event 555 | run-2 · event 412 (gdocs_get_document_text documentId=f_faf4d7c167d14a1127dcc3); run-3 · event 337 (gdocs_get_document_text documentId=f_faf4d7c167d14a1127dcc3); run-4 · event 313 (gdocs_get_document_text documentId=f_faf4d7c167d14a1127dcc3); run-5 · event 389 (gdocs_get_document_text documentId=f_faf4d7c167d14a1127dcc3); run-6 · event 422 (gdocs_get_document_text documentId=f_faf4d7c167d14a1127dcc3) | a query made for another unit carried it: full-text 'sound' lists the log beside Calvin's sheet |

Controls: all 42 control trials HELD (no rule was over-applied to a line it does not cover). Channels: 11 FAILED, 31 HELD, the same runs and nodes as above. Ledger: 126 dispositioned records appended (42 verdicts, 42 controls, 42 channels); the eleven that record a miss are hev_1aed400b1fe29c09, hev_1cd895730771b18c, hev_2958daf8a0c7e467, hev_569fc4c1516d7ad8, hev_6d6043bdb38afe82, hev_71a6baa04eac16dc, hev_7ea5d40849e1fba6, hev_8a7b7025355e7f46, hev_b9649b0938ea7397, hev_ee03757b1a09e15a, hev_f5b8ed8da503655b.

## 5 · Per-rollout ledgers

Full ledgers: Working_Files/run_forensics/rev1/ (calls.jsonl, writes.json, briefs.json per run); reach of each deciding record: Working_Files/hardening_gen/out/reach.json; write payloads: hardening_gen/out/payloads.json. The pre-check delegated its 32 ticket writes to one sub-agent on the same model; no baseline run used a brief.

| Run | Counted calls | Hub (event of first read) | Deciding records read (event) | Deciding records never returned | What it wrote | Score |
|---|---|---|---|---|---|---|
| precheck | 237 | ask 4, notes 50, pack list 54, pack ticket 74 | ARTHOLD 322, REVISED 80, AUDIO 434 | EXPORT, PICKS, ZIP | sheet event 528: Delivered 8, Ready 56, Owed 32; eight with Dynamite; 32 moves, 32 comments, 8 shares; DM counts 8/56/32 | 61.0% |
| run-1 | 244 | ask 7, notes 30, pack list 34, pack ticket 41 | EXPORT 284, REVISED 512, PICKS 321 | ARTHOLD, AUDIO, ZIP | sheet event 555: Delivered 8, Ready 58, Owed 30; eight with Bow; 30 moves, 30 comments, 8 shares; DM counts 8/58/30 | 53.3% |
| run-2 | 271 | ask 11, notes 44, pack list 48, pack ticket 59 | EXPORT 424, ARTHOLD 466, REVISED 306, AUDIO 410, PICKS 345, ZIP 412 | none | sheet event 536: Delivered 8, Ready 36, Owed 52; eight with Bow; 52 moves, 52 comments, 8 shares; DM counts 8/36/52 | 100.0% |
| run-3 | 259 | ask 4, notes 22, pack list 28, pack ticket 39 | EXPORT 304, ARTHOLD 284, REVISED 268, AUDIO 335, ZIP 337 | PICKS | sheet event 409: Delivered 8, Ready 36, Owed 52; eight with Dynamite; 52 moves, 52 comments, 8 shares; DM counts 8/36/52 | 92.3% |
| run-4 | 245 | ask 7, notes 18, pack list 20, pack ticket 27 | ARTHOLD 347, REVISED 265, AUDIO 315, ZIP 313 | EXPORT, PICKS | sheet event 440: Delivered 8, Ready 48, Owed 40; eight with Dynamite; 40 moves, 40 comments, 8 shares; DM counts see payloads.json | 72.8% |
| run-5 | 234 | ask 8, notes 18, pack list 22, pack ticket 28 | ARTHOLD 270, REVISED 298, AUDIO 387, ZIP 389 | EXPORT, PICKS | sheet event 452: Delivered 8, Ready 48, Owed 40; eight with Dynamite; 40 moves, 40 comments, 8 shares; DM counts see payloads.json | 72.3% |
| run-6 | 272 | ask 7, notes 17, pack list 22, pack ticket 30 | EXPORT 259, ARTHOLD 478, REVISED 281, AUDIO 424, PICKS 314, ZIP 422 | none | sheet event 518: Delivered 8, Ready 36, Owed 52; eight with Bow; 52 moves, 52 comments, 8 shares; DM counts 8/36/52 | 100.0% |

Review coverage: every call was classified by the tools; I reviewed the queued register write of each run (events precheck 528, run-1 555, run-2 536, run-3 409, run-4 440, run-5 452, run-6 518), the first call that returned each deciding record (42 cells of the reach table), every search and channel read of every run (the per-tool lists behind section 8), all 13 failed calls, and the brief, sheet, share, ticket and Slack payloads of every run. Not reviewed call by call: the 96 comment-list calls and the 60 to 104 ticket writes of each run, which were checked as sets against the payload summary.

## 6 · Friction, tool defects and horizon

Friction: none configured (03_Error_Async_Config.txt), none met.
Tool errors: precheck event 16 Bash; run-1 event 2 slack_search_public_and_private; run-2 event 2 slack_search_public_and_private, event 8 Bash; run-3 event 258 slack_read_channel; run-4 event 2 slack_search_public_and_private, event 262 Bash, event 294 slack_search_public_and_private, event 344 slack_conversations_search_messages; run-5 event 2 slack_search_public_and_private; run-6 event 2 slack_search_public_and_private, event 248 slack_search_public_and_private. Six are Slack searches by a display name that did not resolve ('user_not_found': 'Frederick', 'Claire'), three are shell calls to jq, which the run's sandbox lacks, and two are dropped connections (ECONNRESET, run-3 event 258, run-4 event 344). Each was followed by another form of the call (run-3 repeated the read at event 267; run-4 found Claire's DM at event 347 with the next search); none hid a deciding record or changed an outcome.
Unconfigured tool defects: none found. Slack search returns thread replies and caps a query at the newest results: a search for Robert's messages since 24 Sep with limit 50 (run-1 event 276) returns 50 messages from Mon Sep 29 10:50 PM PT onward and not his Fri Sep 26 reply, which is why author sweeps find Marcus and Claire and not Robert's 26 Sep reply.
Horizon: counted calls 234 to 272 across the six baseline runs and 237 on the pre-check; the two full-pass runs are at 271 and 272. Every run is above 130. The volume comes from the 96 note reads and 60 to 104 ticket writes; nothing was blocked or repeated.

## 7 · Verifier sanity

No verifier output exists, so there is no judge text to compare. In its place every failed slot of every run was confirmed against the write payload (hardening_gen/out/payloads.json): the sheet states are 8/56/32 (precheck), 8/58/30 (run-1), 8/48/40 (run-4 and run-5) and 8/36/52 (run-2, run-3, run-6), and the Board set of Bow and Dynamite matches the PICKS column of the register. One decoder defect: D4 on run-5 (section 2). For the rubric stage: a share that gives no role is a view share when the tool returns reader.

## 8 · Why Opus passed

`python3 -B Task_Authoring/tools/hardness_v2_check.py --task-dir Task_Authoring/task_inputs`:

```text
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md
  CLEAN      SAME_PLACE      5 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 3 requirements: {'R2': ['EXPORT', 'REVISED', 'AUDIO'], 'R3': ['ARTHOLD', 'ZIP'], 'R4': ['PICKS']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   6 of 6 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

The static check is clean, and the runs still averaged 82%: the traps are well formed, but four of the six deciding records sit where Opus 5.5 looks as a matter of routine. What the seven runs do after reading the 96 notes:

| Habit | Runs (of 7) | What it exposes |
|---|---|---|
| Read #zombie-design from about 24 Sep | 6 (run-2 found the post with a Slack search for 'color') | Robert's new-colours post: REVISED arrives with the hub |
| Search Slack for the author's recent messages | Claire 6, Brian 3, Robert 2, Marcus 1, Calvin 2 | ARTHOLD; EXPORT once. A high-volume author is cut by the result limit, a low-volume one is not |
| Keyword sweeps in Slack: FBX, sound, music, font, ASCII or binary, library, outgoing, colour | FBX 7, sound 7, ASCII or binary 4, outgoing 3, export 1, 'saved out' 1 | EXPORT in two runs, through the note's own wording |
| Full-text Drive search for 'sound' | 5 (the pre-check searched 'Universal Sound') | AUDIO in six runs, and with it ZIP in five |
| Read #zombie-art and open the bow thread | read 5, opened 3 | PICKS |
| Read #zombie-match3d | 2 | EXPORT |
| Search Drive for the outgoing folder | 0 | nothing: no run looked for the log by its own name |
| Open Trello | 0 | the kickoff-card decoy was never met |
| Open GitHub pull requests | 1 | the pull request behind the colour versions was not needed |

Per settled trap, the v2 failure kind is in the register's last column. Genuine capability: in every run the whole hub chain and the 96 note reads, the loss rule and the 7-slot tray against the decoys, the music rule from April, the four recipients, and only true Owed tickets moved (30 to 52 of them); Claire's Turkish in all six runs that read it.
Heavy rows (weight 5) that passed in all six baseline runs: X3, X3b, X8. Those tied to a mechanism are X3, X3b, X8 (REVISED): the rebuilds below must not add more rows of this kind.

## 9 · Purge list (proposed; S0r decides)

| Node | Evidence | Proposal |
|---|---|---|
| REVISED as a retrieval unit (budget unit C1) | leaked in 7 of 7 runs, each from the channel read for the picks (run-1 event 512, run-6 event 281); the pull request it was budgeted on was opened by one run (run-1 event 333) and decided nothing | rebuild as a completion note elsewhere (RP-REVISED), or drop from the budget |
| The Turkish wording of ARTHOLD | no run hesitated on it (precheck event 322, run-3 event 284) | purge as a difficulty; it goes with RP-ARTHOLD |
| The Trello kickoff-card decoy | opened by no run (0 Trello calls in 7 runs) | keep as realism, count no difficulty on it |

## 10 · Proposed rebuilds (v2 moves; S0r decides)

Each proposal moves or rewords a deciding record; none adds a line, a row, a rule, a step or a sentence to the prompt. Details and evidence: Working_Files/mode_b_request.json (repairs RP-ARTHOLD, RP-ZIP, RP-REVISED, RP-EXPORT).

| Repair | Node | v2 move | What changes | Found now (7 runs) | Habit it would sit behind |
|---|---|---|---|---|---|
| RP-ARTHOLD | ARTHOLD | correction out of the obvious place | the UV redo is stated in a record a search by Claire's name does not return, for example by Robert in his DM with Julia; Claire's DM row goes | 6 | reading Julia's DM with Robert (1 run) or a date sweep of her DMs (2 runs) |
| RP-ZIP | ZIP | decouple from another unit's query | the folder log says 'The sound files.' without the word 'sound' (for example 'The .wav exports.') | 5, all through the AUDIO query | a Drive search for the outgoing folder (0 runs so far; 3 runs searched Slack for it) |
| RP-REVISED | REVISED | A25 completion note elsewhere | the folder log records that Claire re-sent the three recoloured items on Tue 30 Sep and that they open and look right; the three lines become Ready; counts 8 / 39 / 49 | 7 (as Owed) | the same log as RP-ZIP |
| RP-EXPORT | EXPORT | remove the echo of the original | Marcus's post keeps its place and loses the words of the note it corrects | 4 | channel history (2 runs) or a search for Marcus (1 run) |

Unchanged: PICKS (a live coin flip, 3 of 7 found) and AUDIO (a lookup, kept as realism).
Expected effect, UNCALIBRATED: `python3 -B Task_Authoring/task_inputs/Working_Files/hardening_gen/simulate.py` draws six runs 20,000 times on the gradable surface, each unit found independently with the rate shown (rates are counts from the seven runs, or the share of runs that showed the habit that would reach a moved record). It reproduces rev1 at 78% against the 82% observed.

```text
rev1 as measured                   avg 0.781 [0.709, 0.854] P(avg<70%) 0.08 SD 0.122 P(SD in band) 0.74 P(all gates) 0.05 P(log rows fail in all 6) 0.00
rebuilt, central                   avg 0.532 [0.457, 0.609] P(avg<70%) 1.00 SD 0.125 P(SD in band) 0.70 P(all gates) 0.69 P(log rows fail in all 6) 0.26
rebuilt, finds more                avg 0.613 [0.526, 0.700] P(avg<70%) 0.90 SD 0.143 P(SD in band) 0.82 P(all gates) 0.71 P(log rows fail in all 6) 0.05
rebuilt, finds less                avg 0.470 [0.409, 0.537] P(avg<70%) 1.00 SD 0.103 P(SD in band) 0.50 P(all gates) 0.48 P(log rows fail in all 6) 0.53
three moves, central               avg 0.604 [0.538, 0.670] P(avg<70%) 0.97 SD 0.108 P(SD in band) 0.56 P(all gates) 0.53 P(log rows fail in all 6) 0.26
three moves, finds more            avg 0.670 [0.597, 0.744] P(avg<70%) 0.70 SD 0.121 P(SD in band) 0.68 P(all gates) 0.44 P(log rows fail in all 6) 0.05
three moves, finds less            avg 0.553 [0.497, 0.610] P(avg<70%) 1.00 SD 0.094 P(SD in band) 0.39 P(all gates) 0.38 P(log rows fail in all 6) 0.53
ARTHOLD relocation only            avg 0.689 [0.617, 0.761] P(avg<70%) 0.58 SD 0.118 P(SD in band) 0.66 P(all gates) 0.34 P(log rows fail in all 6) 0.00
```

Rates used: rev1 EXPORT 4/7, ARTHOLD 6/7, REVISED 7/7, AUDIO 6/7, PICKS 3/7, ZIP 5/7. Rebuilt central: EXPORT 3/7 (the two runs that found the post only through its echo of the note lose it), ARTHOLD 0.30, the folder log 0.20 (no run searched Drive for the folder; three searched Slack for it), AUDIO and PICKS unchanged. 'Finds more' and 'finds less' move those three rates up and down.
Reading: the four moves together are the only option whose P(all gates) holds near 0.5 or better at both ends; one relocation alone is a coin flip on the average and 0.34 on all gates. The risks for S0r to weigh: the folder log would decide eleven lines (ZIP and REVISED), a concentration; in the central case there is a 26% chance that no run opens it, and its rows then fail in all six runs and need all-fail justifications (fair: the log is shared with Julia and named by the notes); and the SD sits near the 0.1 floor in every option, so EXPORT is only reworded and PICKS is left alone.
budget_outcome on the pre-check:

```text
BUDGET OUTCOME: NO-GO
[PASS] precheck.trajectory: precheck: 253 tool calls, 5 results spilled to a file
[FAIL] precheck.budget_outcome: NO-GO: anchor A2 (D05HMBQUC8Z/1759148152.833779) was opened at step 127 (event 321) by slack_search_public_and_private (its id came back in the result); 1 of 4 variance units opened. Do not spend the baseline: the budget does not hold on this revision
[WARN] precheck.hand_review: hand dispositions are needed for A2 (expected not opened, opened at step 127) and for no other unit
BUDGET OUTCOME (stop-rule): PASS
[PASS] precheck.stop_rule: 1 NO-GO pre-check(s) on design D2 of 1 logged (stop at 2)
```

The tool asks for one relocation per NO-GO. The baseline and the simulation show that one is not enough (ARTHOLD alone: E[average] 0.69, P(all gates) 0.34), so the set above is put to S0r as a redesign under a new design id, not as a patch.

## 11 · Routing (proposed; S0r decides)

Universe changes, with the facts each would change (for the prompt, Oracle Event and rubric checks that follow):

| Change | Records | Facts that change |
|---|---|---|
| RP-ARTHOLD | remove slack row D05HMBQUC8Z/1759148152.833779; add one message from Robert in D05GU6L0XFH on Mon 29 Sep | the deciding record and its author; the 12 bathroom lines stay Owed with Claire |
| RP-ZIP | body text of gdocs f_faf4d7c167d14a1127dcc3 | none in the truth; the log's wording |
| RP-REVISED | one more sentence in the Tue 30 Sep entry of the same doc | Cactus Plant, Chainsaw and Cone become Ready; Delivered 8, Ready 39, Owed 49; Owed by person Brian 27, Claire 18, Calvin 3, Martin 1; 49 ticket moves and comments; the surface slots X3, X3b, X8 and K3 change |
| RP-EXPORT | text of slack row C0880U9751A/1758906517.912099 | none in the truth; the post's wording |

Prompt-side defects: none found. The prompt names the message, Julia's Drive and the PlayableX channel and nothing else; /prompt passed it with every dimension at 5, and no run read it as naming a source or a cause.
Routed observations: for /create-oe-writing, the drafted events describe rev1 and have to be regenerated on the next revision; a blind completeness pass also read the five tool-less 'work out' events as non-actions, so their conclusions belong on the read and write events. For /create-rubric-writing: accept a share without a role argument (the tool grants reader), the links as a post or a thread reply, and the counts as a message or a reply.

## 12 · Self-review

Walked Evals/1A_Hardness_Eval.md sections 3 to 5 against this report. Every verdict below was counter-read for a tool, fairness, verifier or run cause; every deciding record was re-verified in this run, the seeded ones from the SQL statements and the base ones through tools/hg.py (oe_gen/base_read.py: slack/messages/C090N54TG79/2025-09.json/813, slack/messages/C08R8CHB0QL/2025-09.json/252); the surface grades were re-run after the last input change and the write payloads were searched for each designed value. The neighbouring band is argued in the last row. No replacement wording for the prompt, an Oracle Event or a criterion is quoted here.

| Verdict | Counter-reading | Evidence that resolves it | Result |
|---|---|---|---|
| EXPORT · LANDED (precheck, run-4, run-5) | Tool: the searches these runs made could have failed to return a post that matches | none of their queries matches the post ('FBX', 'ASCII', 'outgoing', 'zip', 'playable'); precheck event 315, run-4 events 249 and 325, run-5 events 252 and 418. The post exists (SQL L58) and run-6 event 259 shows the plain channel history returns it | LANDED stands (retrieval, not tool) |
| EXPORT · LEAKED (run-1, 2, 3, 6) | The trap was never live: the note's own words return the correction | true for run-2 event 424 ('saved out') and run-3 event 304 ('export'): a lexical echo, routed as RP-EXPORT; run-1 event 284 and run-6 event 259 are an author search and a channel read, which are fair finds | LEAKED stands; partly a wording leak |
| ARTHOLD · LANDED (run-1) | Run: run-1 might have been cut short before it could look | run-1 is complete (708 events, 244 counted calls); it searched by Robert, Marcus, Calvin and Brian (events 276, 283, 423, 425) and read #zombie-art, never Claire's messages or DM | LANDED stands |
| ARTHOLD · LEAKED (6 runs) | The trap was never live: the correction is in the first place anyone looks | six runs reached it by a search for Claire's messages or her DM history (precheck event 322, run-2 466, run-3 284, run-4 347, run-5 270, run-6 478); budget_outcome calls the anchor opened | LEAKED stands; the anchor is exposed and is routed as RP-ARTHOLD |
| REVISED · LEAKED (7 runs) | The trap was never live | the deciding post is a root message in #zombie-design; six runs read it in the channel history (precheck event 80, run-1 512, run-3 268, run-4 265, run-5 298, run-6 281) and run-2 by a search for 'color' (event 306); re-read through hg.py as slack/messages/C090N54TG79/2025-09.json/813 | FALSE as a retrieval unit: goes to the purge and rebuild lists |
| AUDIO · LANDED (run-1) | Tool: a Drive search for the sheet could have failed | run-1 searched Drive for 'sfx', 'brief', 'hand-off', 'playable' and 'pack' (events 21 to 23, 380, 430) and never for 'sound'; the same search returns the sheet in six runs (run-2 event 406) | LANDED stands |
| AUDIO · LEAKED (6 runs) | The trap was never live: the notes state the rule | the notes say 'Anything from a library or a bought pack stays here' and the sheet's title holds the noun every run searched (precheck event 434, run-3 335) | LEAKED stands; kept as realism, no rebuild proposed |
| PICKS · LANDED (precheck, run-3, run-4, run-5) | Fairness: a reply that names no item could be read two ways | the reply sits under Julia's bow post and says 'in the 8 in place of the last one on my list'; the 25 Sep list ends with Dynamite (SQL L60, SQL L61); /prompt settled the fork as F8 and F9; precheck event 349 and run-5 event 294 show the parent came back with its replies unopened | LANDED stands |
| PICKS · LEAKED (run-1, 2, 6) | The trap was never live | each of the three opened the thread on purpose after reading the channel (run-1 event 321, run-2 345, run-6 314); four runs did not | LEAKED stands: a live coin flip |
| ZIP · LANDED (precheck, run-1) | Fairness: nothing points at the log | the notes' Ready rule and the eight ticket notes name the outgoing folder, and the doc is titled for it and shared with Julia (SQL L15, SQL L20); /hardness counted the miss as genuine (cause C2) | LANDED stands |
| ZIP · LEAKED (5 runs) | The trap was never live: a bulk call carried the answer | all five listed the log with one full-text Drive search for 'sound' made for the sound question (run-2 event 406, run-3 333, run-4 307, run-5 384, run-6 419): the log says 'The sound files.' (SQL L20) | LEAKED by coupling with AUDIO; routed as RP-ZIP |
| Band (median run, run-4) | Neighbouring band: 3 instead of 4, because run-4's error is one group of 12 lines and one swapped item, a bounded correction | the correction still touches the sheet (12 rows and 2 cells), 12 tickets, the counts in the DM and the brief's eight (run-4 events 440, 443, 632), the same spread that /hardness scored 4 on the pre-check | 4 kept; 3 is the neighbour |

Not done: the pre-check posterior forecast (playbook step 5). The six-run baseline already exists and measures what the forecast would predict; the next forecast is pre-registered on the next revision at /create-injection.
Unresolved: none. The find rates in section 10 are estimates from seven runs, not measurements of the next revision.

```
STAGE GATE hardening: PASS — Task_Authoring/task_inputs · 01a_Hardening_Report.md#35998ca41fd6 · 01_Universe_Inject.sql#78465cd474f8 · 01_Hardness_Manifest.json#8c8a0c3ff108 · 00_Assigments.md#82494197a841 · 01_Grounding_Dossier.md#fe8923840c79 · 06_PreCheck_Trajectory#f48743e23ac9 · 07_Baseline_Trajectories#52a8413624b9 · 10_Baseline_Verifier_Results.md#e3b0c44298fc · __context__#3246c54345b9 · __assignment__#70579cebc8fc · __policy__#dc4ab5df3cdd · __gate_policy__#435bafd56991 · __review__#b62863bc4291 · blocking 0 · warnings 2 · checks 22
[PASS] assignment.v3_context: Julia Lawson / Product Manager; hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#78465cd474f8, 01_Hardness_Manifest.json#8c8a0c3ff108, 01_Grounding_Dossier.md#fe8923840c79, solver/solver.py#99a47385c0c9, 01c_Dispositions.json#04fab53986de, 01c_Preflight_Report.json#d23ddd0c21c1, 00_Assigments.md#82494197a841, 01_Scenario_Design.md#77f01f2b2933, 01_Hardness_Manifest.draft.json#facbd65efa7f, 01_Gradable_Surface.json#f8dbc02d039b, __context__#3246c54345b9, __assignment__#70579cebc8fc, __policy__#dc4ab5df3cdd, __gate_policy__#1f62b72f1b1d, __review__#b62863bc4291)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 6/6 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 12 evidenced counter-readings (of 12 found; need ≥ 12) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] readiness.mode_b: PROVISIONAL_SINGLE_PRECHECK: current structured diagnosis
[WARN] task.folder: the task folder is the bare default `task_inputs`: give each task its own folder (`Task_Authoring/task_inputs<Label>`) and pass it to every command, so two tasks never share one [first-pass check in warn mode: reported, not blocking]
[WARN] precheck.budget_outcome: pre-check against the budget: NO-GO — anchor(s) opened: ['A2']. Repair with one relocation of the exposed record (playbook 01a step 1b), not added rows or prompt rules
[PASS] precheck.stop_rule: 1 failed pre-check(s) on design D2; the stop rule applies at 2
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 · Next steps

1. /create-scenario --revise takes the four repairs as the design delta (new design id), revises the mechanism portfolio, the budget and the gradable surface, and records the dispositions of the verdicts above.
2. /create-injection implements the revision as rev2 and re-runs every injection gate and the coherence sweep; then /injection and /prompt on the platform with the unchanged prompt.
3. /create-prompt-writing check, /create-humantime and /create-oe-writing are re-attested or regenerated on rev2; then one pre-check and, on a GO, the six-run baseline.


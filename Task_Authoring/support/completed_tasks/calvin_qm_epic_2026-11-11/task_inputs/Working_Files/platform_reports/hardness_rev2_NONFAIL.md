## HARDNESS EVALUATION REPORT (Opus observed)

### Task: Turn the ZOM-543 Queue Manager ticket into an epic from Vincent's home-screen flow pass, build a shared stock-take sheet and a numbers slide, and DM Brian the five numbers
### Assigned Persona: Calvin Price - Game Engineer (Unity VFX)
### Assigned Task Type: long-horizon (difficulty mode: hard)

### FINAL VERDICT: NON-FAIL
Assessment version: model-aware-v3
Assessed model: Opus
Assessment mode: OPUS_OBSERVED
Score: 3
Execution status: COMPLETE
Difficulty: Hard
Gate decision: PROCEED
Gate reason: OBSERVED_OPUS_FAILURE
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (runtime does not report a named level)
Next action: Proceed with dependent authoring; retain the observed failure evidence (rows 12, 13, 32, 38 and tickets ZOM-571, ZOM-572, ZOM-581 and the row-38 sub-issue). Consider the advisory under "Suggested revisions": this run's failed share is small.
Evidence limits: One run only; no average-score or repeatability claim. The export does not embed the original user prompt text; task/source match is established from behaviour (see Provenance).

---

### Provenance

| Item | Value |
|---|---|
| Stage / mode | /hardness, chat review, attempt 6aed9d01e894b802ca6d6d03, review date 2026-11-10 |
| Universe | Universe_SynthCut (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Prompt | `Evals/task_inputs/04_Prompt.txt` sha256 `edefd55c0ff5b150f9f757e2b0c123215fac99b89d8cbc1a7e319caab2a4bcc3` |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md` sha256 `0baaee66afd5965a9259775f953c7e3ca97776e8846f91aa04ffdbd8c676b3a6` (Task Type long-horizon, Difficulty Mode hard) |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` sha256 `ee46405a157d6eb3423da8b51c4f2f42164b60409dc4d82c74b8c770938ec5e8` (revision 6; proposed overlay, not executed) |
| Run | Uploaded `Run1_trajectory (2).json`, saved as `Evals/task_inputs/opus/trajectory.json` sha256 `a77a6d7f93c8cca59ca209b86d72741c34a38a124e2944d9e16cdd46434df9ff` (replaces the earlier run `7276d2d9…`); session `75199365-…`, 484 events, `result.subtype: success`, `terminal_reason: completed`, 171 turns |
| Model | init `model: claude-opus-5-5[1m]`; every assistant message `claude-opus-5-5`; `modelUsage.canonicalModel: claude-opus-5-5` → **Opus** |
| Unhinted | No hint text anywhere in the export; discovery is organic (Slack profile, Queue Manager search, Brian's DM, ZOM-543 comments, Vincent's sheet, Arthur's doc, #builds, GitHub PR list). Treated as unhinted. |
| Task/source match | The prompt string is not embedded in the stream-json export. The run carries out exactly the saved prompt's deliverables (children and report lines under ZOM-543, a stock-take sheet in Calvin's "ZM queue manager" folder shared with the invite, a slide in the "ZM queue manager" deck, a DM to Brian in D0770ET6WBW) and reads records only the revision-6 SQL contains: the "as it stands today" note, Arthur's "A pass stands until…" line, row 18 "again Android #2013" and the ZOM-576 / ZOM-582 comments ("Still the same on iOS Internal 1757"). So this SQL version was live in the run. |
| Reference files | None referenced by the prompt |

authority_contract: prompt-incorporation-v1. The prompt incorporates Brian's request ("set it all up as he asked"; "He messaged me about it yesterday"). Brian's DM points to his note on ZOM-543 (`comment_faaa7924…`, SQL line 213), which sets the report set, the three statuses, the line/state rules, the child rule, the review list, the sheet tabs and the slide. The note brings in Arthur's rule doc ("ZM builds and QA passes", `f_6d0326fa006b136f1bbf82`) and "the agenda of Thursday's review" by name. Nothing else adds obligations.

---

### Ground truth (evaluator-derived from base + overlay; matches the current /prompt review's outcome A)

- **Passed 12** (rows 3, 5, 7, 17, 22, 23, 24, 26, 27, 31, 33, 35); **Waiting on QA 6** (rows 1, 2, 13, 18, 25, 38); **Waiting on a fix 21** (rows 4, 6, 8, 9, 10, 11, 12, 14, 15, 16, 19, 20, 21, 28, 29, 30, 32, 34, 36, 37 + Marcus's glow DM); **Areas clear 1** (Zombie Lane); **Review list 6** (rows 6, 8, 36, 15, 18, 19).
- Ticket states: ZOM-571 (row 12) **In Validation → Todo**; ZOM-581 (row 32) **In Validation → Todo**; ZOM-572 (row 13) **Todo → In Validation**; ZOM-576 stays In Validation. New sub-issues: 12 Done, **4 In Validation** (rows 1, 2, 25, 38), 3 Todo (rows 9, 29, Marcus).
- Deciding records for the rows this run got wrong:
  - Row 12: Arthur's review comment on #472 (`harmonygames-Games/match3d#472#rc_1`, SQL line 164): "Flow sheet has the season pass icon restart against this PR. That one isn't in this diff, the two Collect & Win ones are. Needs its own PR." The same text is in #zombie-prs (`C093LEZGF6J`, SQL line 85) and in Calvin's inbox as a GitHub review notification (SQL line 157).
  - Row 32: Arthur's review comment on #475 (`#475#rc_1`, SQL line 169): "Don't see the pack sound stop anywhere in here. Still needs doing." Mirrored in #zombie-prs (SQL line 88) and Calvin's inbox (SQL line 159).
  - Rows 13 and 38: Oliver's comment on merged #473 (`#473#c_2`, SQL line 172, 2025-09-30 15:42Z): "For the flow list: this also has the fix for the pass start popup coming back after every level and for the pass bar filling before the tokens land." Mirrored in #zombie-prs (SQL line 82). #473 `base_ref main`, `merged_at 2025-09-30T15:41:20Z` (GitHub `data.json` `/pull_requests/2378`). Neither row has been re-tested since.
- Vincent's legend (`f_d3a1aa5976285aac98ffda`): "Fix: the PR the dev told me it went into. Blank if nobody told me." So the Fix column is hearsay, and the note's "a fix for it is in main" needs the PR evidence.

---

### Requirement map (expected vs observed)

| # | Requirement | Observed (trajectory call #) | Outcome |
|---|---|---|---|
| R1 | 10 children under ZOM-543, same team, no assignee | #87–96 `linear_create_issue` → ZOM-585…594, `parentId ZOM-543`, no assignee, all ok | MET |
| R2 | Child Done if Clear, Todo if Open | Zombie Lane (ZOM-591) Done, other nine Todo | MET |
| R3 | Report scope: 38 rows + teammate DM bugs since 09-26; no Vincent chats, Oliver exceptions or parked blocker | 39 reports = 38 rows + Marcus's glow (#147) | MET |
| R4 | Branch-build passes don't count (rows 1, 2, 25) | #1718 found to be a QueueManager branch build; rows Waiting on QA; sub-issues #139, #140, #152 In Validation | MET |
| R5 | A pass reopened by a later main-build sighting (rows 9, 29); older-build sighting does not reopen (row 27) | Rows 9, 29 Waiting on a fix (Submission #135); row 27 Passed | MET |
| R6 | Row 18: "again" before #472 merged → Waiting on QA | ZOM-576 note (#127/#138) cites #2013 built before the 15:53Z merge; stays In Validation | MET |
| R7 | Row 34: still there on #1757 after #475 merged → Waiting on a fix | ZOM-582 note (#136) | MET |
| R8 | **Rows 12 and 32: the fix is not in the PR the sheet names (Arthur's reviews) → Waiting on a fix; ZOM-571 and ZOM-581 to Todo** | Never called `github_get_pull_request_reviews` / `_comments` (only #57 `search_repositories`, #58 `list_pull_requests`). Sheet Status "Waiting on QA" with Why "Fix in #472 (main Sep 30). Not re-tested on a main build yet." (#161); ZOM-571 note "Waiting on QA … State In Validation already matches" (#123); ZOM-581 note likewise (#135). No state change. | **MATERIAL_FAIL (cause A)** |
| R9 | **Rows 13 and 38: fix in merged #473 per Oliver → Waiting on QA; ZOM-572 to In Validation; row-38 sub-issue In Validation** | Row 13 sheet Status "Waiting on a fix", Why "Not re-tested. No fix in main." (#161); ZOM-572 note "Waiting on a fix … State Todo already matches" (#124); row-38 sub-issue "Pass progress bar fills before the tokens arrive" created **Todo** (#146) | **MATERIAL_FAIL (cause B)** |
| R10 | Remaining 31 row statuses | All match the ground truth | MET |
| R11 | Existing tickets moved under their child with a status/why note; mismatched states fixed | 20 re-parented (#97–116), 20 notes (#117–138; ZOM-576 noted twice). Three required state changes not made (see R8, R9) | MET for moves/notes; state fixes counted under R8/R9 |
| R12 | Rows with a ticket under another name (rows 11, 20) | ZOM-556, ZOM-560 used | MET |
| R13 | New sub-issues: report as title, no priority, no assignee, state by status | 19 created (#139–157), titles = reports, no priority/assignee; states 12 Done / 3 In Validation / 4 Todo (row 38 wrong, see R9) | MET apart from R9 |
| R14 | Review list = not-Passed reports in areas on the current agenda (Trello card: Collect & Win, Level-end rewards) | 6 rows flagged Yes; final response explains the Sep 30 card change | MET |
| R15 | Sheet in the ZM queue manager folder; Reports tab (Report, Area, Status, Ticket, Review list, Why) and Areas tab (Area, Status, Open reports) | Created, moved to `d_36cdb0374c4aad3b8bf741` (#159), both tabs written (#161, #162). Areas open counts 3/3/3/5/3/3/0/1/4/2 all correct (the four wrong rows are not-Passed either way) | MET (row cells under R8/R9) |
| R16 | Shared with everyone on the review invite | Reader shares to Leonard, Brian, Arthur, Julia, Vincent (#163–167) | MET |
| R17 | One slide with the five numbers in the queue manager deck | #169 `gslides_batch_update` on `f_637e63ae6c1b4a7eb016aa`: 12 / 6 / 21 / 1 of 10 / 6 | MET |
| R18 | DM Brian the five numbers | #170 `slack_send_message` to D0770ET6WBW, ok: 12 / 6 / 21 / 1 / 6 | MET (numbers correct only because the two swaps cancel; see below) |
| R19 | Final response | Accurate account of the writes, but it states "None of the 20 needed a state change", which repeats causes A and B | MET apart from the propagated error |

No write failed. All required capabilities (Linear create/update/comment, Drive create/move/share, Sheets write, Slides batch update, Slack send) succeeded: SUPPORTED. The GitHub read tools that would have settled R8/R9 (`github_get_pull_request_reviews`, `github_get_pull_request_comments`, `github_pull_request_read`) were in the run's tool list and never called. The same facts were also in #zombie-prs and in Calvin's Gmail inbox.

---

### Failures, causes and counts

- **Cause A: Arthur's PR review comments not read** (`#472#rc_1`, `#475#rc_1`). The run kept Vincent's Fix column as true for rows 12 and 32. Affected outputs: 2 sheet Status/Why cells, 2 ticket notes, 2 missed state changes (ZOM-571, ZOM-581 left In Validation).
- **Cause B: Oliver's comment on merged #473 not read** (`#473#c_2`). The run treated blank-Fix rows 13 and 38 as having no fix in main. Affected outputs: 2 sheet Status/Why cells, the ZOM-572 note and its missed state change (left Todo), and the row-38 sub-issue created Todo instead of In Validation.
- **Independent causes: 2.** They rest on different records (two review comments by Arthur on #472/#475 vs a PR comment by Oliver on #473), and the errors go in opposite directions. A run could make one without the other: the sheet points to #472/#475 for rows 12/32, but nothing on the sheet points to #473 for rows 13/38, so a run that checks the cited PRs would fix A and still miss B.
- **Why the headline numbers survived:** A moves two reports from Fix to QA and B moves two from QA to Fix, so 6 / 21 come out right by coincidence. All four rows are not-Passed either way, and their areas (Season Pass, Card packs) are not on the review agenda, so areas clear, the open counts and the review list are also unaffected. The per-report lines, which are the operational output QA works from, are wrong. QA would re-test row 12 on #472 builds that don't contain the fix and skip rows 13/38, which are ready to test.
- **Narrow miss: NO.** Independent causes 2, so the narrow-miss rule does not apply. Failed share ≈ 10% of about 60 weighted core items (39 report statuses with their sheet lines, 20 moves/notes/state fixes, 19 new sub-issues, 10 children, sheet tabs, 5 shares, slide, 5 DM numbers): 4 of 39 statuses and 4 Linear states wrong, while all five headline numbers, the children, area statuses and review list are right. Difficulty mode hard, loss 30%.
- **Failure-pattern risk: NO.** Traps (this run's result):
  - T1 branch-build rule: Arthur's doc + #builds #1718 + Calvin–Vincent DM (rows 1, 2, 25; flips Boss Arena to Clear and three headline numbers if missed) ≈ 20%, right
  - T2 reopen on a later main build: Submission #135 sightings (rows 9, 29) ≈ 8%, right
  - T3 Arthur's reviews: fix not in #472/#475 (rows 12, 32 + two state changes) ≈ 6%, **wrong**
  - T4 Oliver's claim on merged #473 (rows 13, 38 + one state change + one new-issue state) ≈ 6%, **wrong**
  - T5 row 18 re-test before the #472 merge (status, ZOM-576 state, QA/fix counts) ≈ 7%, right
  - T6 row 27 sighting on an older build (Android #2006 vs iOS #1745) ≈ 6%, right
  - T7 the agenda on Leonard's updated Trello card vs Brian's earlier DM (review-list number + 6 cells) ≈ 8%, right
  - T8 Marcus's DM bug in scope; Vincent's chats and Oliver's exceptions out ≈ 4%, right
  - T9 ZOM-556/ZOM-560 under other names ≈ 3%, right
  Largest trap share ≈ 20% (T1), below 30%.
- **Tool calls: 170** (170 main agent, 0 sub-agent; both count). Task type long-horizon, minimum 100; not under 90% (90). No tool-call adjustment.

### Correct work and usability

Most of the result is correct and usable: all 10 children with the right states, 20 moves with notes, 19 correctly scoped sub-issues with no priority or assignee, 35 of 39 statuses (including the branch-build, reopen, pre-merge and older-build traps), the right review agenda, both sheet tabs with correct area counts, the five shares, the slide and the DM with the right five numbers. The fix is bounded: 4 sheet rows, 4 ticket notes, 3 existing-ticket states and 1 new-ticket state.

### Task/environment defects

None that affected the run. The deciding records were reachable through cataloged GitHub reads and were also mirrored in #zombie-prs and Calvin's inbox (the /prompt review confirmed Calvin can see them).

### Unassessed scope

None material. The prompt text is not embedded in the export (see Provenance).

### Score rationale

Band 3 (Hard, NON-FAIL): two independent, genuine model failures. The run trusted the Fix column instead of the PR evidence, and that made four report statuses, three existing-ticket states and one new-ticket state wrong. Each is a consequential error in the per-report lines Brian asked for, not a cosmetic one. The correction is bounded and the core work stays usable.
- Not band 2: there are two independent causes, so the narrow-miss rule does not apply, and the defects are wrong core decisions, not minor ones.
- Not band 4: the five headline numbers, children, area statuses, review list, sheet structure, shares, slide and DM are all correct, so substantial correction across the result is not needed.

### Suggested revisions (advice only; do not change this score)

This run's failed share (≈ 10%) is well under hard mode's 30% loss, and the two missed traps only touch a few rows each. That is because their errors cancel out in the headline numbers. If the other baseline runs behave like this one, the average could still sit above the 70% limit. To widen the margin:
1. Make the PR-evidence traps reach a headline number. Today the A and B swaps cancel exactly (2 out of QA, 2 into QA). For example, if one of Arthur's "not in this diff" rows sat in a review-agenda area (Collect & Win or Level-end), the review list or an area's Clear/Open status would also depend on it, so the trap shows up in two places in the answer (Failure patterns guide, 5. Write the rubric so each trap shows up on two criteria).
2. Add a third independent trap in another part of the task with its own deciding record, for example a fix PR merged into a feature branch rather than main, or a later revert of a fix (Hardness guideline, Part 3. What beats Opus 5.5).
Any change to the SQL needs /injection, /prompt and /hardness again, in that order, with a new unhinted Opus run.

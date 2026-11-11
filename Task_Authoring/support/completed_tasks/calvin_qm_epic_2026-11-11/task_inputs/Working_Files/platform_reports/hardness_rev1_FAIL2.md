## HARDNESS EVALUATION REPORT (Opus observed)

### Task: Turn the ZOM-543 Queue Manager ticket into an epic from Vincent's home-screen flow pass, build a shared stock-take sheet and a numbers slide, and DM Brian the five numbers
### Assigned Persona: Calvin Price - Game Engineer (Unity VFX)
### Assigned Task Type: long-horizon (difficulty mode: hard)

### FINAL VERDICT: FAIL
Assessment version: model-aware-v3
Assessed model: Opus
Assessment mode: OPUS_OBSERVED
Score: 2
Execution status: COMPLETE
Difficulty: Easy
Gate decision: HOLD
Gate reason: INSUFFICIENT_DIFFICULTY
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (runtime does not report a named level)
Next action: Revise the task so a second, independent deciding fact is no longer signposted by Brian's ZOM-543 note (see "Suggested revisions"), get a new unhinted Opus run, and send /hardness again.
Evidence limits: One run only; no average-score or repeatability claim. The export does not embed the original user prompt text; task/source match is established from behaviour (see Provenance).

---

### Provenance

| Item | Value |
|---|---|
| Stage / mode | /hardness, chat review, attempt 6aed9d01e894b802ca6d6d03, review date 2026-11-10 |
| Universe | Universe_SynthCut (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Prompt | `Evals/task_inputs/04_Prompt.txt` sha256 `edefd55c0ff5b150f9f757e2b0c123215fac99b89d8cbc1a7e319caab2a4bcc3` |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md` sha256 `0baaee66afd5965a9259775f953c7e3ca97776e8846f91aa04ffdbd8c676b3a6` (Task Type long-horizon, Difficulty Mode hard) |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` sha256 `d39581558af42f0a6764db03b1f3cbf90b297f2c70853dd7a8c38ef6e42af089` (proposed overlay; not executed) |
| Run | Uploaded `Run1_trajectory.json`, saved as `Evals/task_inputs/opus/trajectory.json` sha256 `7276d2d934afd1449eb9d6e05e27644ee7defeaff18f42e3c71cd6693203cb01`; session `b9e41f4f-…`, 506 events, `result.subtype: success`, `terminal_reason: completed`, 181 turns |
| Model | init `model: claude-opus-5-5[1m]`; all 234 assistant messages `claude-opus-5-5`; `modelUsage.canonicalModel: claude-opus-5-5` → **Opus** |
| Unhinted | No hint text anywhere in the export; discovery is organic (opens with Slack profile, "Queue Manager" search, Brian DM, ZOM-543 comments, then hunts for Arthur's rule through Confluence/Slack/Gmail/Drive before finding the doc at call 74). Treated as unhinted. |
| Task/source match | The prompt string is not embedded in the stream-json export. The run executes exactly the saved prompt's deliverables (epic children + report lines in Linear, stock-take sheet in Calvin's "ZM queue manager" folder shared with the invite, slide in the "ZM queue manager" deck, DM to Brian in D0770ET6WBW) and reads the injected records (Brian's ZOM-543 comment, Vincent's flow-pass sheet `f_cb40955893624e1acb8500`, ZOM-567…584, Arthur's review comments on #472/#475, Oliver's #473 comment, the Submission #135 come-backs, Trello card 80), so the SQL overlay was live in the run. |
| Reference files | None referenced by the prompt |

authority_contract: prompt-incorporation-v1. The prompt incorporates Brian's request ("set it all up as he asked"; "He messaged me about it yesterday"). Brian's DM (`446ba456…`, 2025-09-30 20:40Z) points to "a note on the ticket about how I want it", i.e. his ZOM-543 comment `comment_faaa7924…` (2025-09-30 20:25Z). That chain incorporates the note's rules; Arthur's rule doc and Leonard's review card are incorporated by the note by name. Nothing else adds obligations.

---

### Ground truth (evaluator-derived from base + overlay)

Build branches (#builds `C05433XK267`, Jenkins posts): iOS Internal #1698 and **#1718 = `[PERSON]/QueueManager` (branch)**, #1746 = `AnimatedIcons` (branch); #1713, #1727, #1745 (09-29 16:19Z), #1750 (09-30 01:55Z), #1754, #1757, Android #1974, #1984, #2006, #2010, #2013, Submission #129 and **#135 (09-30 20:13Z)** are all `main`.
PRs (GitHub `data.json` `/pull_requests`): #465 merged 09-25 22:15Z, #472 merged 09-30 15:53Z, #473 (Oliver's) merged 09-30 15:41Z, #475 merged 09-30 16:09Z.
"ok, chat" rows 1, 2, 25: Vincent–Calvin DM `D06UPGF5PQV`, Calvin 09-25 16:29Z "Match 3D iOS Internal - #1718 already tested", Vincent 17:15Z "Looks ok to me … Boss arena as well" → pass on a branch build, does not count (Arthur, "ZM builds and QA passes" `f_6d0326fa006b136f1bbf82`).
Come-backs: Vincent thread reply `b156fdcd…` in #zombie-bugs (Submission #135, row 9); Robert `eca2df16…` in #zombie-match3d (Submission #135, row 29). #135 is newer than #1745/#1750.
Review contradictions: Arthur on #472 (`#472#rc_1`) → row 12 not in the diff; Arthur on #475 (`#475#rc_1`) → row 32 not in.
Dev claim on merged PR: Oliver `#473#c_2` → rows 13 and 38.
DMs to Calvin since 09-26 from others: only Marcus's glow report (`806f4a67…`, `bb5dd875…`) is a home-screen bug; Owen/EMPLOYEE_0032/Brian/Marcus base DMs are not bug reports.
Review card: Trello card 80 latest desc "Collect & Win, Level-end rewards" (updated 09-30 17:22Z; the earlier 09-29 Brian DM and first invite say Daily Gift).
Existing tickets under other names: ZOM-556 (row 11), ZOM-560 (row 20).

Expected: **Passed 12** (rows 3, 5, 7, 17, 22, 23, 24, 26, 27, 31, 33, 35); **Waiting on QA 6** (1, 2, 13, 18, 25, 38); **Waiting on a fix 21** (the other 20 rows + Marcus's glow); **Areas clear 1** (Zombie Lane); **Review list 6** (Level-end 6, 8, 36; Collect & Win 15, 18, 19). Open reports per area: Tutorials 3, Level-end 3, Daily Gift 3, Season Pass 5, Collect & Win 3, Win Streak 3, Zombie Lane 0, Boss Arena 1, Endless 4, Card packs 2 (sum 27 = 6 + 21).

---

### Requirement map (expected vs observed)

| # | Requirement | Observed (trajectory) | Outcome |
|---|---|---|---|
| R1 | 10 children under ZOM-543, same team, no assignee | `linear_create_issue` ×10 → ZOM-585…594, `parentId ZOM-543`, team_ZOM, no assignee; all succeeded | MET |
| R2 | Child state Done if Clear, Todo if Open | Zombie Lane ZOM-591 Done; other nine Todo | MET |
| R3 | Report scope: 38 sheet rows + teammate DM bugs since 09-26, no Vincent chats, no Oliver skip exceptions, no parked input blocker | 39 reports = 38 rows + Marcus glow; nothing extra | MET |
| R4 | Branch-build passes don't count (rows 1, 2, 25) | Found #1718 = QueueManager branch; rows → Waiting on QA (In Validation) | MET |
| R5 | Come-backs on a later build (rows 9, 29) | Both → Waiting on a fix, cites Submission #135 built later | MET |
| R6 | Review says fix not in PR (rows 12, 32) | ZOM-571 and ZOM-581 → Waiting on a fix, state In Validation → Todo | MET |
| R7 | No-PR rows fixed by a dev's merged PR (rows 13, 38) | ZOM-572 Todo → In Validation; new ZOM-602 In Validation | MET |
| R8 | Remaining row statuses | All 39 statuses match the ground truth | MET |
| R9 | Existing tickets: move under child + note with status and why; fix mismatched states | 20 tickets re-parented (`linear_update_issue`), 20 status/why comments, two state fixes (R6) and one (R7) | MET |
| R10 | Rows with a ticket under another name use it (rows 11, 20) | ZOM-556, ZOM-560 used | MET |
| R11 | New sub-issues: report as title, state by status, no priority, no assignee | 19 created (ZOM-595…613); results show `priority 0 / No priority`, no assignee | MET |
| R12 | Review list = not-Passed reports in the areas on Leonard's (latest) card | Used Collect & Win + Level-end; 6 rows flagged Yes | MET |
| R13 | Sheet in Calvin's ZM queue manager folder; tab Reports (Report, Area, Status, Ticket, Review list, Why); tab Areas (Area, Status, Open reports) | Created in `d_36cdb0374c4aad3b8bf741`; both tabs and columns present; 39 report rows | MET (Areas tab cell: see R14) |
| R14 | Areas tab values | Statuses all right; **Tutorials "Open reports" = 4, should be 3** (rows 1, 2, 4). The run's own Reports tab marks rows 3 and 35 Passed, so the Areas tab is internally inconsistent (sum 28 ≠ 6 + 21). Same wrong "4 of 5" in child ZOM-585's description. | MINOR_GAP |
| R15 | Share with everyone on the review invite (Leonard too) | Reader shares to Brian, Leonard, Arthur, Julia, Vincent (Calvin owns) | MET |
| R16 | One slide with the five numbers in the queue manager deck | `gslides_batch_update` on `f_637e63ae6c1b4a7eb016aa`: one slide, 12 / 6 / 21 / 1 / 6 | MET |
| R17 | DM Brian the five numbers in their DM | `slack_send_message` to D0770ET6WBW, ok: 12 / 6 / 21 / 1 / 6 | MET |
| R18 | Final response | Accurate summary of writes, numbers and judgement calls | MET |

No write failed (only errors: oversize tool outputs and one `user_not_found` search, all recovered).

---

### Failures, causes and counts

- **MATERIAL_FAIL outcomes:** none. **Independent causes behind material failures:** 0.
- **Minor gap:** one wrong count (Tutorials open reports 4 vs 3) in the Areas tab and child description; the five headline numbers, every status and every Linear state are correct.
- **Narrow miss: NO** – no MATERIAL_FAIL outcomes, so the narrow-miss rule does not apply; the score comes from the band table (only minor defects). Independent causes 0; failed share ≈ 1–2% of about 60 weighted core items (39 report statuses, 10 children, 20 moves/notes, 19 new tickets, sheet tabs, 5 shares, slide, 5 DM numbers); difficulty mode hard, loss 30%.
- **Failure-pattern risk: NO.** Traps (all got right by this run):
  - T1 branch-build rule, Arthur doc + #builds #1718 + DM (rows 1, 2, 25; flips Boss Arena to Clear and three numbers if missed) ≈ 15%
  - T2 come-backs on Submission #135 (rows 9, 29) ≈ 8%
  - T3 review says fix not in #472/#475 (rows 12, 32 + two state changes) ≈ 8%
  - T4 Oliver's claim on merged #473 (rows 13, 38) ≈ 7%
  - T5 Leonard's updated Trello card vs the earlier "daily gift" DM/invite (review-list number + 6 cells) ≈ 8%
  - T6 Marcus DM bug in scope, Vincent chats/Oliver exceptions out (one report + counts) ≈ 4%
  - T7 ZOM-556/ZOM-560 under other names (two tickets) ≈ 4%
  Largest trap share ≈ 15%, below 30%.
- **Tool calls: 180** (180 main agent, 0 sub-agent; both count). Task type long-horizon, minimum 100; not under 90% (90). No tool-call adjustment.

### Correct work and usability

The result is fully usable as delivered: every status, every Linear state and parent, all 19 new tickets, the shares, the slide and Brian's DM are correct. Only one Areas-tab cell needs a one-character fix.

### Task/environment defects

None that affected the run. All required capabilities (Linear create/update/comment, Drive create/share, Sheets write, Slides batch update, Slack send) succeeded: SUPPORTED.

### Unassessed scope

None material. Prompt text not embedded in the export (see Provenance).

### Score rationale

Band 2 (Easy, FAIL): the run met every core requirement and every trap; the one defect is a minor, local count in a secondary column. Band 1 would also be defensible (no meaningful defect), so the run sits at the easy end; band 3 is not supported because there is no consequential failure needing correction.

Why the task came out easy: Brian's ZOM-543 note writes out the deciding rules next to the request: "Vincent's Fix column is only what he was told at the time, so check the PR … if the review on it says a fix is not in there, it is not" (T3), "A row with no PR in the sheet counts as merged too if the dev wrote on a merged PR of theirs" (T4), "stays passed unless somebody says later, on a build made after that one, that it is back" (T2), "Vincent sometimes writes a row for something that already has a ticket under another name" (T7). Each line tells the agent which check to run, so each trap turns into a lookup. That is the pattern the hardness guide (Part 8) warns about: a task with its rules written into the request.

### Suggested revisions (advice only)

1. Move rule lines out of Brian's note into separate dated records the agent has to find, rather than deleting them (a rule nothing in the data settles becomes a fork). For example, keep "Waiting on QA: the fix is merged" in the note but drop "if the review on it says a fix is not in there", so Arthur's review comments on #472/#475 have to be connected without a pointer; put the "dev wrote on a merged PR" convention in a #zombie-prs or Arthur message instead of the note.
2. Add a timing trap the data already supports: the "on a build made after that one" clause. Android #2006 (09-29 15:39Z) is older than iOS Internal #1745 (09-29 16:19Z), so a come-back reported on #2006 for a row passed on #1745 should leave it Passed. Today both come-backs are on #135, which is clearly later.
3. Add a "done with a missing piece" item, for example a dev's fix claim on a PR that is merged but into a feature branch rather than main, or a later revert of a fix.
Then get a new unhinted Opus run and send /hardness again. If the injection changes, rerun /injection, /prompt and /hardness in that order.

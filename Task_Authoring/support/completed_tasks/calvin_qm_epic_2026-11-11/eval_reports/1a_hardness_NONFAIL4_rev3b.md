## HARDNESS EVALUATION REPORT (Opus observed)

### Task: Turn the ZOM-543 Queue Manager ticket into an epic from Vincent's home-screen flow pass, build a shared stock-take sheet and a numbers slide, and DM Brian the five numbers
### Assigned Persona: Calvin Price - Game Engineer (Unity VFX)
### Assigned Task Type: long-horizon (difficulty mode: hard)

### FINAL VERDICT: NON-FAIL
Assessment version: model-aware-v3
Assessed model: Opus
Assessment mode: OPUS_OBSERVED
Score: 4
Execution status: COMPLETE
Difficulty: Hard
Gate decision: PROCEED
Gate reason: OBSERVED_OPUS_FAILURE
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (runtime does not report a named level)
Next action: Proceed with dependent authoring (/oe, then /rubric); keep the observed failure evidence (rows 6, 12, 13, 14, 15, 32, 37, 38; tickets ZOM-568, ZOM-571, ZOM-572, ZOM-573, ZOM-574, ZOM-581, ZOM-584 and the row-38 sub-issue; the 7 / 22 numbers on the slide and in the DM).
Evidence limits: One run only; no average-score or repeatability claim. The export does not embed the prompt text; the task/source match is shown from behaviour (see Provenance). The run is consistent with SQL revision 8 or 9: the only revision-9 changes (SQL lines 157, 164, 169: code hunks and one email snippet) were never read by the run and do not change the expected answer.

---

### Provenance

| Item | Value |
|---|---|
| Stage / mode | /hardness, chat review, attempt 6aed9d01e894b802ca6d6d03, review date 2026-11-10 |
| Universe | Universe_SynthCut (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Prompt | `Evals/task_inputs/04_Prompt.txt` sha256 `edefd55c0ff5b150f9f757e2b0c123215fac99b89d8cbc1a7e319caab2a4bcc3` |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md` sha256 `0baaee66afd5965a9259775f953c7e3ca97776e8846f91aa04ffdbd8c676b3a6` (Task Type long-horizon, Difficulty Mode hard) |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` sha256 `479b8441f52e739e786eb1ef35043153f87b15f473bb72e683634e2dac1d02e9` (revision 9; proposed overlay, not executed) |
| Run | Uploaded `Run1_trajectory (3).json`, saved as `Evals/task_inputs/opus/trajectory.json` sha256 `b0b79aacdc25c6b8e760861f745e68bd5d3c3f8c0de1474f9f047c6b4d33199c` (replaces run `a77a6d7f…`); session `ef93e003-…`, 489 events, `subtype: success`, `terminal_reason: completed`, 168 turns |
| Model | init `model: claude-opus-5-5[1m]`; all 222 assistant messages `claude-opus-5-5`; `modelUsage.canonicalModel: claude-opus-5-5`, so the run is **Opus** |
| Unhinted | No hint, rubric or oracle text in the export (the only "golden" matches are base Slack/Linear text about golden frames). Discovery is organic: Slack profile, Brian's DM, the ZOM-543 comment, Vincent's sheet and legend, Arthur's doc, #builds, Linear comments. Treated as unhinted. |
| Task/source match | The run carries out the saved prompt's deliverables (children and report lines under ZOM-543, a sheet in "ZM queue manager" shared with the invite list, a slide in the ZM queue manager deck, a DM in D0770ET6WBW). It read records that exist only in the later SQL versions: ZOM-583 to ZOM-586 (#52, #109) and Samuel's ZOM-585 comment "Got this again on Android Submission 135, so #472 did not sort it." (#54, SQL line 275). |
| Reference files | None referenced by the prompt |

authority_contract: prompt-incorporation-v1. The prompt incorporates Brian's request ("set it all up as he asked"; "He messaged me about it yesterday"). His DM points to his ZOM-543 note (`comment_faaa7924…`, SQL line 217), which sets the report scope, the three statuses ("Waiting on QA: not passed, and a fix for it is in main that QA has not tried on a main build yet"), the ticket line and state rules, the child rule, the review list, the sheet tabs and the slide. The note pulls in Arthur's rule doc ("ZM builds and QA passes", `f_6d0326fa006b136f1bbf82`, SQL line 23) and "the agenda of Thursday's review" by name. Nothing else adds obligations.

evidence_contract: stage-evidence-v1. The expected outcome is REUSED from the current /prompt review (`1_prompt.md` sha256 `6e31ce8d…`, UGT outcome A), which read the same prompt, assignment, SQL `479b8441…` and universe. The deciding records for every row this run got wrong were checked NEW (below).

---

### Ground truth (REUSED from /prompt outcome A; deciding records checked NEW)

- **Passed 10** (rows 3, 5, 7, 22, 23, 26, 27, 31, 33, 35); **Waiting on QA 9** (rows 1, 2, 6, 13, 14, 18, 25, 37, 38); **Waiting on a fix 20** (rows 4, 8, 9, 10, 11, 12, 15, 16, 17, 19, 20, 21, 24, 28, 29, 30, 32, 34, 36 + Marcus's glow DM); **Areas clear 0**; **Review list 7** (rows 6, 8, 36, 15, 17, 18, 19).
- Ticket states: ZOM-571, ZOM-574, ZOM-581, ZOM-585 to **Todo**; ZOM-568, ZOM-572, ZOM-573, ZOM-584 to **In Validation**; ZOM-576 stays In Validation. Base/SQL states checked: 571, 574, 581, 585 In Validation; 568, 572, 573, 584 Todo (SQL lines 176-214). New sub-issues: 10 Done, 4 In Validation (rows 1, 2, 25, 38), 3 Todo (rows 9, 29, Marcus).
- Deciding records (NEW checks):
  - **Rows 12 and 15:** Arthur's review comment on #472 (`harmonygames-Games/match3d#472#rc_1`, SQL line 164, 2025-09-30 15:53:40Z): "Flow sheet has the season pass icon restart and the event bar starting under the gift popup against this PR. Neither is in this diff. The other two Collect & Win ones are. Those two need their own PR." Mirrored in #zombie-prs (SQL line 85) and in Calvin's Gmail (SQL line 157).
  - **Row 32:** Arthur's review comment on #475 (`#475#rc_1`, SQL line 169): "Don't see the pack sound stop anywhere in here. Still needs doing." Mirrored in #zombie-prs (SQL line 88) and Gmail (SQL line 159).
  - **Rows 13, 14, 37, 38:** Oliver's comment on #473 (`#473#c_2`, SQL line 172, 2025-09-30 15:42:10Z): "For the flow list, this also has four fixes: the pass start popup coming back after every level, the pass bar filling before the tokens land, the claim animation playing twice after the shop, and the freezer popup opening behind the pass popup." Mirrored in #zombie-prs (SQL line 82). #473 is `base_ref main`, `merged_at 2025-09-30T15:41:20Z` (GitHub `data.json` `/pull_requests/2378`). None of the four rows has a re-test.
  - **Row 6:** the #472 body update (SQL line 165): "Implement Win&Collect into Queue Manager (this also holds the pre-level panel until the level-end coins have landed)". #472 is `base_ref main`, `merged_at 2025-09-30T15:53:04Z` (`/pull_requests/2377`). Row 6 has no re-test. This is the only record of that fix (SQL grep: "pre-level panel" appears only in the sheet row, ZOM-568 and the #472 body).
- Vincent's legend (`f_d3a1aa5976285aac98ffda`, SQL line 21): "Fix: the PR the dev told me it went into. Blank if nobody told me." So the sheet's Fix column is hearsay in both directions: a filled cell can be wrong and a blank cell does not mean no fix.

---

### Requirement map (expected vs observed)

| # | Requirement | Observed (trajectory call #) | Outcome |
|---|---|---|---|
| R1 | 10 children under ZOM-543, same team, no assignee | #84-93 `linear_create_issue` → ZOM-587…596, `parentId ZOM-543`, no assignee | MET |
| R2 | Child Done if Clear, Todo if Open (none Clear) | All ten created Todo | MET |
| R3 | Report scope: 38 rows + teammate DM bugs since 09-26; no Vincent chats, Oliver exceptions or parked blocker | 39 reports = 38 rows + Marcus's glow (#146, sheet row 39) | MET |
| R4 | Branch-build passes don't count (rows 1, 2, 25 on iOS #1718, QueueManager branch) | Rows Waiting on QA; sub-issues #138, #139, #149 In Validation | MET |
| R5 | Passes reopened by a later main-build sighting (rows 9, 17, 24, 29 via Submission #135); older-build sighting does not reopen (row 27) | Rows 9, 17, 24, 29 Waiting on a fix; ZOM-585 set to Todo (#104); row 27 Passed | MET |
| R6 | Row 18: "again" on #2013, built before the #472 merge → Waiting on QA | ZOM-576 note (#127); stays In Validation | MET |
| R7 | Row 34: still there on #1757 after #475 merged → Waiting on a fix | ZOM-582 note (#137) | MET |
| R8 | **Rows 12, 15, 32: Arthur says the fix is not in the PR the sheet names → Waiting on a fix; ZOM-571, ZOM-574, ZOM-581 to Todo** | Never read any PR review (no `github_get_pull_request_reviews`/review-comment call; only issue comments on #465/#472/#475, #45-47). Sheet rows 12, 15, 32 "Waiting on QA", Why "Fix #472/#475 merged to main 9/30; not yet re-tested" (#158); notes say Waiting on QA (#122, #125, #136); no state change | **MATERIAL_FAIL (cause A)** |
| R9 | **Rows 13, 14, 37, 38: fixes in merged #473 per Oliver → Waiting on QA; ZOM-572, ZOM-573, ZOM-584 to In Validation; row-38 sub-issue In Validation** | #473 never opened (no tool result in the run contains it). Rows "Waiting on a fix", Why "No fix reported; not re-tested" (#158); notes (#123, #124, #131) say Waiting on a fix, states left Todo; row-38 sub-issue created **Todo** (#145) | **MATERIAL_FAIL (cause B)** |
| R10 | **Row 6: fix in merged #472 per its body → Waiting on QA; ZOM-568 to In Validation** | #472 PR record never read (only #475, #43). Row 6 "Waiting on a fix", "No fix reported" (#158); ZOM-568 note (#117), state left Todo | **MATERIAL_FAIL (cause C)** |
| R11 | Remaining 31 row statuses | All match the ground truth | MET |
| R12 | Existing tickets moved under their child with a status/why note; mismatched states fixed | 22 re-parented (#94-115), 22 notes (#116-137). Seven required state changes not made (R8-R10) | MET for moves/notes; state errors counted under R8-R10 |
| R13 | Rows 11 and 20 use the existing ZOM-556 / ZOM-560 | Used (#99, #107, #121, #129) | MET |
| R14 | New sub-issues: report as title, no priority, no assignee, state by status | 17 created (#138-154); 10 Done, 3 In Validation, 4 Todo; row 38 wrong (R9) | MET apart from R9 |
| R15 | Review list = not-Passed reports in agenda areas (Trello card: Collect & Win, Level-end rewards) | 7 rows flagged Yes (6, 8, 15, 17, 18, 19, 36) | MET |
| R16 | Sheet in the ZM queue manager folder; Reports and Areas tabs with the named columns | Created (#155), moved to `d_36cdb0374c4aad3b8bf741` (#156), both tabs written (#158, #159). Area statuses and open counts 3/3/3/5/4/3/1/1/4/2 all correct | MET (row cells under R8-R10) |
| R17 | Shared with everyone on the review invite | Leonard, Brian, Arthur, Julia, Vincent (#160-164) | MET |
| R18 | **Slide with the five numbers** | #166 on `f_637e63ae6c1b4a7eb016aa`: 10 / **7** / **22** / 0 of 10 / 7 | **2 of 5 numbers wrong** (propagated from A-C) |
| R19 | **DM Brian the five numbers** | #167 to D0770ET6WBW, ok: 10 / **7** / **22** / 0 / 7 | **2 of 5 numbers wrong** (propagated) |
| R20 | Final response | Accurate account of the writes, repeats 7 / 22; says "23 existing tickets" were moved (22 were) | MINOR_GAP (miscount) plus propagated error |

No write failed. All required capabilities (Linear create/update/comment, Drive create/move/share, Sheets write, Slides batch update, Slack send) succeeded: SUPPORTED. The reads that would have settled R8-R10 (`github_get_pull_request` for #472/#473, `github_get_pull_request_reviews`, `github_get_issue_comments` on #473) were in the run's tool list; the run used `github_get_pull_request` on #475 and `github_get_issue_comments` on three PRs, so the path was in reach. The same facts were also in #zombie-prs (`C093LEZGF6J`, which the run found in #33 but never read) and in Calvin's Gmail.

---

### Failures, causes and counts

- **Cause A: Arthur's PR review comments not read** (`#472#rc_1`, `#475#rc_1`). The run took Vincent's Fix column at face value for rows 12, 15 and 32. Affected: 3 sheet rows, 3 ticket notes, 3 missed state changes (ZOM-571, ZOM-574, ZOM-581 left In Validation). Grouped as one cause because both are the same missed read (PR reviews); counting them separately would only raise the count.
- **Cause B: Oliver's comment on merged #473 not read** (`#473#c_2`). The run treated blank-Fix rows 13, 14, 37, 38 as having no fix. Affected: 4 sheet rows, 3 ticket notes and missed state changes (ZOM-572, ZOM-573, ZOM-584 left Todo), and the row-38 sub-issue created Todo instead of In Validation.
- **Cause C: the #472 body's extra fix not read** (SQL line 165). Row 6 treated as having no fix. Affected: 1 sheet row, the ZOM-568 note and its missed state change.
- **Independent causes: 3.** They rest on different records (review comments vs a comment on a different PR vs a PR body), and a run could make any one without the others: reading Arthur's reviews does not show #473, and the #472 body is a separate field from its reviews.
- **Propagation to the headline numbers:** A moves 3 reports into QA and B + C move 5 out, so Waiting on QA is 7 instead of 9 and Waiting on a fix is 22 instead of 20. Both wrong numbers went to Brian on the slide and in the DM. Passed (10), areas clear (0) and the review list (7) are right because all eight rows are not-Passed either way and rows 6 and 15 sit on the review list in both readings.
- **Narrow miss: NO.** Independent causes 3, so the narrow-miss rule does not apply. Failed share ≈ 20% of about 60 weighted core items (39 report statuses with their sheet lines, 22 moves/notes/state fixes, 17 new sub-issues, 10 children, sheet tabs, 5 shares, slide, 5 headline numbers in two places): 8 of 39 statuses, 7 of 22 existing-ticket states and notes, 1 of 17 new-issue states, and 2 of 5 headline numbers on both the slide and the DM wrong. Difficulty mode hard, loss 30%.
- **Failure-pattern risk: NO.** Traps (this run's result, share of the weighted answer if missed):
  - T1 branch-build rule: Arthur's doc + #builds #1718 (rows 1, 2, 25; flips Boss Arena to Clear and three headline numbers) ≈ 18%, right
  - T2 reopen on a later main build: Submission #135 sightings (rows 9, 17, 24, 29; ZOM-585 state; Zombie Lane Clear; review list) ≈ 15%, right
  - T3 Arthur's reviews: fix not in #472/#475 (rows 12, 15, 32; three state changes; QA/fix numbers) ≈ 10%, **wrong**
  - T4 Oliver's four fixes on merged #473 (rows 13, 14, 37, 38; three state changes; one new-issue state; QA/fix numbers) ≈ 12%, **wrong**
  - T5 the #472 body's pre-level panel fix (row 6; ZOM-568 state) ≈ 4%, **wrong**
  - T6 row 18 re-test before the #472 merge ≈ 5%, right
  - T7 row 27 sighting on an older build (Android #2006 vs iOS #1745) ≈ 4%, right
  - T8 agenda on Leonard's updated Trello card vs Brian's earlier DM (review list) ≈ 8%, right
  - T9 Marcus's DM bug in scope; Vincent's chats and Oliver's exceptions out ≈ 4%, right
  - T10 rows 11/20 under ZOM-556/ZOM-560 ≈ 3%, right
  Largest trap share ≈ 18% (T1), below 30%.
- **Tool calls: 167** (167 main agent, 0 sub-agent; both count). Task type long-horizon, minimum 100; not under 90% (90). No tool-call adjustment.

### Correct work and usability

Much of the result is right and usable: all 10 children with the right states, 22 moves with notes, the 17 correctly scoped sub-issues with no priority or assignee, 31 of 39 statuses (including the branch-build, four reopen, pre-merge re-test and older-build traps), the right agenda and review list, both sheet tabs with correct area statuses and counts, the five shares, and 3 of the 5 headline numbers.

### Task/environment defects

None that affected the run. The deciding records are reachable through cataloged GitHub reads and are mirrored in #zombie-prs and Calvin's inbox (the /prompt review confirmed Calvin can see them).

### Unassessed scope

None material. The prompt text is not embedded in the export (see Provenance).

### Score rationale

Band 4 (Hard, NON-FAIL): three independent, genuine model failures. The run trusted Vincent's Fix column (filled and blank cells alike) instead of the PR evidence, which made 8 of 39 report statuses wrong, left 7 existing tickets in the wrong state, created one sub-issue in the wrong state, and put two wrong headline numbers (7 waiting on QA, 22 waiting on a fix) on the slide and in the DM to Brian. Fixing it means touching every deliverable: 8 sheet rows, 8 ticket notes and states, the slide and a corrected DM.
- Not band 3: the correction is not limited to one part of the output. It runs through the sheet, Linear, the slide and the message Brian asked for, and two of the five numbers he wanted are wrong.
- Not band 5: the central structure is right and usable (children, moves, sharing, review list, areas clear, Passed count, 31 of 39 statuses), so the result is not invalidated.

### Suggested revisions (advice only; they do not change this score)

None needed for hardness. This run missed three independent PR-evidence traps and got the rule traps right, so failures should split across runs. Keep the rubric scoring each trap in two places (the row status and its ticket state or headline number) so runs that miss different traps stay distinguishable (Failure patterns guide, 5. Write the rubric so each trap shows up on two criteria).

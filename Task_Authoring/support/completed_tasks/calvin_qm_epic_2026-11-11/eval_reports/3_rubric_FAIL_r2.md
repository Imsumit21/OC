## RUBRIC EVALUATION REPORT

### Task: Turn the Queue Manager ticket (ZOM-543) into an epic, build and share the stock-take sheet, add the numbers slide, and report the five numbers to Brian
### Persona: Calvin Price - Game Engineer (Unity VFX)
### Total Rubrics: 184 (Outcome: 183, Process: 1)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## Fix List

Your 98 new and edited rows use exactly the titles and weights of last run's checked fixes, and every value in them matches the records. Two things remain, both small edits. Both fixes came back clean from a full check round (mark: **checked**, 1 round).

**1. R28, R34, R36, R38, R40, R43, R58, R64: the evidence Reject clause adds a parent condition the title doesn't have (Major, overly specific).** Each title grades only the state ("sets ZOM-568 … to the state In Validation"). Your rewritten evidence also rejects the row when the ticket is "not under a child of ZOM-543". That puts the move back into the state row: one parent miss would then fail both the move row and the state row. Keep the titles. In each row's evidence, replace the Reject sentence with:
- R28: Reject: ZOM-568 left in its old state or set to another state (where ZOM-568 sits is graded by its own move row, not here).
- R34: Reject: ZOM-571 left in its old state or set to another state (where ZOM-571 sits is graded by its own move row, not here).
- R36: Reject: ZOM-572 left in its old state or set to another state (where ZOM-572 sits is graded by its own move row, not here).
- R38: Reject: ZOM-573 left in its old state or set to another state (where ZOM-573 sits is graded by its own move row, not here).
- R40: Reject: ZOM-574 left in its old state or set to another state (where ZOM-574 sits is graded by its own move row, not here).
- R43: Reject: ZOM-585 left in its old state or set to another state (where ZOM-585 sits is graded by its own move row, not here).
- R58: Reject: ZOM-581 left in its old state or set to another state (where ZOM-581 sits is graded by its own move row, not here).
- R64: Reject: ZOM-584 left in its old state or set to another state (where ZOM-584 sits is graded by its own move row, not here).
(checked)

**2. R113: weight 3 → 5 (one level off).** Creating the sub-issue for Marcus Bennett's report means pulling his DM into scope through the note's DM sentence and confirming that no ticket already holds it. R67, R138 and R142 weight that same join at 5. Keep the title. Set the weight to 5 and the justification to: "Multi-source: the note's scope sentence joined with Marcus's 1:1 chat outside the sheet, plus the area read from his wording." (checked)

---

### Phase 1: Structural Validation
- Five-field completeness: 184 of 184
- Category distribution: Outcome 183, Process 1 (R184)
- Requirement coverage: 201 of 201 required outcomes covered (Coverage ratio from the scorer: 184/184)
- Run mode: DELTA. 74 locked, 12 locked-checked-fix, 33 edited, 65 new, 13 removed rows.

### Phase 2: Per-Rubric Quality
| Row | Issue | Type | Severity |
|---|---|---|---|
| R28, R34, R36, R38, R40, R43, R58, R64 | Evidence Reject clause narrows acceptance with a parent condition the title doesn't state | overly_specific | Major |
| R113 | Weight 3; the work is a multi-source join (expected 5) | weight review | Criteria Weights, one level off |

Atomicity: every target row grades one result. R13 and R131 are the volume rows of two template groups of writes (the 10 child creates and the 17 sub-issue creates), and R148 is the volume row of the review-list spot checks. Create rows R112–R128 grade the title and parent of one created issue (one record).
Over-specificity triage: all target titles are valid; the 8 state rows are overly specific through their evidence only.
Code checks (`hg_rubric_lint.py`):
- `exact_state` on R14–R23: VALUE search done; the child state is a Linear field, so there is no plain-word variant.
- `count_claim` on R157–R166: COUNT search done; every area's list holds.
- `deliverable_claim` on R144–R146: SUPPORTED, because Linear returns issue URLs.
- `count_bundle` on locked R138 and R154: exempt, since each is the volume row of a Reports or Areas spot-check group.

### Phase 3: Set-Level Quality
- Coverage gaps: none. Each of the following has its own rows: the 10 creates and their states, the 17 sub-issue creates and states, the 22 moves, the 22 status notes plus 22 reasons, the 8 state changes, the sheet (folder, tabs, rows, sampled columns, area counts), the 5 shares, the slide, the DM numbers and the ordering row.
- Process audit: 1 of 1 valid (R184, message after the writes).
- Duplicates / overlap / cascade groups: none scored. The 8 state rows' parent condition sits only in their evidence and is scored as overly specific.
- Spot-check groups:
  - Status: 5 samples
  - Ticket: 3
  - Review list: 3, plus volume row R148
  - Why: 2
  - Area status: 2
  - Child template: 2, plus volume row R13
  - Sub-issue template: 2, plus volume row R131
  - Every group is within the cap of 5 and has its volume row (R138 and R154 for the sheet tabs).

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 8 | 4.3% | any | FAIL |
| Moderate | 0 | 0% | any | PASS |
| Minor | 0 | 0% | ≥ 5% | PASS |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 1 | Major overly_specific on 8 rows |
| Criteria Weights | 4 | 1 of 184 rows (0.5%) one level off (R113), none two levels off |
| Rubric Category Balance | 5 | 183 Outcome rows |
| Process Rubrics | 5 | R184 valid; no ordering check missing |
| Agent-Centric Phrasing | 5 | Every title starts with "The Agent" and names no tool |
| Negative Criteria | 5 | Every row fails an idle Agent |
| Predicted All-Fail gate | PASS | No row predicted to fail every run |

**Lowest Sub-Dimension:** Overall Rubric Quality - 1 - eight rows' evidence rejects a run the title accepts.
**Summary:** The rubric is now structurally sound: one row per write, every count bundle gone, and every value verified against the sheet, tickets, PRs and #builds. It fails only because the rewritten evidence on the 8 state rows adds back the parent check. Fixing those 8 Reject sentences and R113's weight leaves no open finding.

### Issues Found
| # | Row | Issue | Severity | Type |
|---|---|---|---|---|
| 1 | R28, R34, R36, R38, R40, R43, R58, R64 | Evidence rejects "not under a child of ZOM-543", which the title doesn't require | Major | overly_specific |
| 2 | R113 | Weight 3, expected 5 | Weights | weight review |

### Recommended Fixes
1. R28, R34, R36, R38, R40, R43, R58, R64: replace the evidence Reject sentence as in the Fix List. Mark: checked, 1 round. Passed `fixcheck`, lint and R1–R7 on the changed rows and their siblings (move rows R29, R35, R37, R39, R41, R44, R59, R65; reason rows R71, R79, R81, R83, R85, R89, R105, R111). The opposite-pair test passed: every one of the 8 tickets starts in a state other than its target, so "left in its old state" still rejects an idle run, and the row doesn't become broad.
2. R113: weight 5 with the new justification. Mark: checked, 1 round. Same checks, with siblings R67, R138, R142 and R147.

## Changes Since Last Run

- Rows: 74 locked, 12 locked-checked-fix, 33 edited, 65 new, 0 re-checked, 13 removed (the old count rows, the bundled move/state rows and the old open-count rows, all replaced by their checked fixes).
- Previous findings now fixed:
  - All count bundles: old R1, R66, R71 and R86.
  - All 22 move-and-state bundles.
  - The prefix-only child titles.
  - The open-count rows' list alternative.
  - R90 and R91 at old weights.
  - All 65 missing outcomes: 10 child states, 19 moves, 22 reasons, 15 sub-issue parents and titles, the Area and Ticket samples, and the slide review-list number.
- Your 98 target rows copy the checked titles and weights exactly. The rewritten justification and evidence are correct, apart from the Reject sentence on the 8 state rows.
- Dismissals: none recorded.
- New scored findings: the 8 state rows (evidence) and R113 (weight).

### Notes for QM (not scored)
- R138 ("exactly 39 reports") and R154 ("exactly 10 areas") trip the new `count_bundle` lint. Both are the volume rows of the Reports-tab and Areas-tab spot-check groups, which the rule exempts. Their COUNT searches found no other item: 38 sheet rows plus Marcus's DM, and the ten areas of Brian's note.
- The COUNT searches for the locked open-count rows (R157, R159–R162, R165) found every list complete. For example, the Endless intro report is open because Android Submission 135 saw it again (C08R27X0EAH/1759268652.552719), and the Boss Arena tutorial report is open because its ok was on feature-branch build #1718 (C05433XK267/1758817549.151639).

### Worth a look (not scored)
These are evidence and justification tidy-ups. None changes what a grader accepts, because each Accept clause repeats the title word for word.
- Reject lists that don't name every wrong answer:
  - R148: "6 or 8 marked rows" leaves out a wrong report among 7.
  - R153: "an empty Why cell" leaves out a wrong reason.
  - R158 and R166: only "another number" is named.
  - R114–R128: "under another child" leaves out "straight under ZOM-543". R112 and R113 already say it.
  - Move rows: "no parent or under another child".
  - R14–R23: only "Done" is named.
  - R1–R10: only "a bug report title" is named.
  - You can extend each list, or end it with "or anything else the title rejects" (R6).
- R69 and similar reason rows: the justification "the reason read from the sheet row's blank cells" understates the work. You still have to check the merged PRs, as R153's justification says. Weight 3 is right (R4).
- Comment-reason evidence reads "(report 4, row of f_cb40955893624e1acb8500)", where "row of" is missing its number. "row N" means the sheet's "#" column, which is one less than the spreadsheet row because of the header. Writing "report #N" avoids the confusion (R2).
- R12 evidence: "without no assignee" should read "with an assignee".
- R91 (optional): the title's "any wording with that meaning" already covers "QA has not re-tested it on a main build since #472 merged". You may add that wording to the parenthesis to remove any doubt (R1).

### Rejected findings
- R5 on R148 (overly broad because the 7 reports aren't named): rejected under QC Appendix B3. Acceptance may come from sibling titles, and R158 and R161 list exactly the 3 Level-end and 4 Collect & Win reports that are not Passed. A run that marks row 7 instead of row 17 marks a report R158 doesn't list.
- R1 on R91 (rejects "fix in merged #472, QA hasn't tried a main build since"): rejected. The record quote doesn't support the claim. The title says "(any wording with that meaning)", and "QA has not tried a main build since the merge" carries that meaning: the last re-test predates the merge. Kept as an optional wording note above.
- R6 on the Reject lists of R1–R23, R29–R65 moves, R114–R128, R148, R153, R158 and R166 ("note accepts more than the title"): rejected. Each evidence Accept clause equals the title, and a short Reject list accepts nothing the title rejects. Kept as tidy-ups above.
- R2 on "row N" and "report N, row of" citations: rejected as `incorrect`, because every cited value is right. Kept as tidy-ups above.
- R4 (round 1) on R147, weight 3 → 5: rejected under Eval 3 §2.12, which weights the work for the atomic result. R147 grades the Area value, which is read from Marcus's wording. Whether his report has a row at all is R138's result (weight 5).
- R4 on the R69-family justifications: not a weight change (weight 3 stays). Kept as a tidy-up.

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7, Opus 5.5 (claude-opus-5-5), each blind to the main review, on the 98 target rows (R4 against all rows, R3 whole-rubric coverage). Then one fix-check round of R1–R7 on the 9 changed rows and their 20 sibling rows.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 101 | 9 | 8 |
| R2 | 98 | 2 | 0 |
| R3 | 98 (+184 coverage) | 0 | 0 |
| R4 | 98 vs 184 | 2 | 1 |
| R5 | 103 | 1 | 0 |
| R6 | 98 | 15 | 8 (same as R1) |
| R7 | 98 | 0 | 0 |
| Fix round 1 (R1–R7) | 29 each | 1 (R4) | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1–DR8 | R1, R6 | "Reject: ZOM-568 in another state, or ZOM-568 not under a child of ZOM-543." (same on R34, R36, R38, R40, R43, R58, R64) | Brian's note comment_faaa792418a942cd40be046d8d217a7d: "If its state does not match the status, put Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix" | 2.7 pattern 4 | overly_specific, Major | CONFIRMED | Title grades the state only; the parent is the move row's result |
| DR9 | R1 | R91 "(any wording with that meaning)" | harmonygames-Games/match3d#472#rc_1: "The other two Collect & Win ones are." | 2.7 | overly_specific | REJECTED | The alternative carries the title's meaning |
| DR10 | R4 | R113 weight 3 | D05U73FNDDL/1759252212.611349; R67, R138, R142 at weight 5 | 2.12 | weight 3 → 5 | CONFIRMED | Same multi-source join as its siblings |
| DR11 | R4 | R69 J "the reason read from the sheet row's blank cells" | PR #473 comment c_2 lists four fixes for blank-Fix rows | 2.12 | justification text | REJECTED (note) | Weight stays 3; tidy-up |
| DR12 | R5 | R148 "every marked row a report that is not Passed …" | Trello card 68daad83bacf52c6ea7e1593 | 2.7 B11 | overly_broad | REJECTED | Sibling titles R158 and R161 define the 7 (QC B3) |
| DR13–DR19 | R6 | Reject lists on R148, R153, R158/R166, R114–R128, moves, R14–R23, R1–R10 | rubric evidence fields | 2.1 | not_self_contained | REJECTED (notes) | Accept clause equals the title; nothing accepted beyond it |
| DR20–DR21 | R2 | "row 6 of f_cb40955893624e1acb8500", "(report 4, row of …)" | sheet grid "#" column | 2.3 | incorrect | REJECTED (notes) | Values right; wording tidy-up |
| FR1 | R4 (fix round) | R147 weight 3 | D05U73FNDDL/1759252212.611349 | 2.12 | weight 3 → 5 | REJECTED | The atomic result is the Area value; inclusion is R138's result |

Effect on verdict: the confirmed DR1–DR8 make Overall Rubric Quality fail (score 1). The confirmed DR10 puts Criteria Weights at NON-FAIL 4.

Platform defects: none

### FINAL VERDICT: FAIL
Score: 1
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: f03edcef10225ce45b409e57608dfa9ff10f8032c6bd9eabeff65a5d60b91bd8
Review context SHA-256: fd93ab7d54ec7d9c228005c7928a32c10d95ce8d941ac32453eb3b70e89b3285
Scoring record SHA-256: 27733e54f611b888dff5ca76e1579015d31e4697146e8093c78a3399dab70d40
Eval version: task-quality-v1
Eval release SHA-256: 95724d0c10e93f280590a039482b3866a70e2d40ada2c074afcdbdb043725f9e
Gate tier: localized
Coverage ratio: 184/184
Repairs: See findings (R28, R34, R36, R38, R40, R43, R58, R64, R113)
Evaluator model: Opus 5.5 (claude-opus-5-5)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Next action: Apply the two checked fixes in the Fix List (8 evidence Reject sentences, R113 weight and justification), save the rubric and run /rubric again.
Evidence limits: None

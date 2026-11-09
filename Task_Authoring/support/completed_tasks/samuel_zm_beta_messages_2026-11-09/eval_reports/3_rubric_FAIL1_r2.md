## RUBRIC EVALUATION REPORT

### Task: Beta phone-message calls for Zombie Match (calls sheet, one-page note, ticket comments and moves, new tickets, checklist, asker emails, counts DM)
### Persona: Samuel Turner - Game Designer
### Total Rubrics: 149 (Outcome: 148, Process: 1)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## Fix List

Copy each fix as written. Row numbers are your current rubric's. Applying them gives a 152-row rubric: two rows deleted, one row added back, and four rows each split in two. Every fix marked checked passed lint, fixcheck and all seven check passes (R1–R7) on the changed rows and their sibling rows. R21 needs your own rewrite.

- **R21** — the closed list of names for the covering message leaves out the client's own name for it (the "Weekly reminder batch", `WeeklyReminderTitle`) and Leonard's "the weekly one". **This row needs your own rewrite.** Four check rounds couldn't settle it. A bare "weekly batch" also fits the client's Weekly Leaderboard batch, which fires on day 14 too and is a Hold. A closed list keeps missing valid names. An open "any wording that identifies Lapsed 7 days (DES-317)" rule leaves that borderline to the judge, and its "that another message already covers it" clause can fail a cell that just names Lapsed 7 days next to Drop. Your rewrite should: accept the bare name Lapsed 7 days / DES-317 in that cell (with or without "covered by"); accept the client's `WeeklyReminderTitle` batch and its headline "They’ve Taken Over… Can You Stop Them?"; and make clear that naming the Weekly Leaderboard batch (DES-320, "Weekly Rankings Reset!") does not count. (revised after check, 4 rounds, needs your own rewrite)
- **R24** — weight 5 is one level high. The row reads test 2 off one comment that states it outright ("it would have to go out from the server"), the same work as R26 (weight 3). Locating the ask is graded by R3, R34 and R114, and the same ask row's Audience cell (R31) is weight 1.
  Fix: weight 3; justification "Interpretation: test 2 read against the asker's own note on ZOM-563 that it would have to go out from the server." (checked, 1 round)
- **R104, R105** — together with R106 they form one cascade: R106's 30 is exactly R104's 24 plus R105's 6, so one missed or extra move fails two count rows. R106 has to stay, because it is the only guard against moving tickets that must stay put (the rule doc's "Go tickets stay as they are"; parent DES-314 is open).
  Fix: delete R104 and R105. Keep R106 unchanged as the one state-change count and guard. Add back, right after R98, "The Agent moves DES-319 (Plague Race) from Done to Backlog" (Outcome, weight 5; justification "Multi-source: the move rests on the test 6 failure and on the roadmap card that overrides Todo."; evidence citing Vincent's Slack "so scratch iOS", the Fix TECH ISSUES card and DES-319 state Done). With it, all four Done "Ready" Hold tickets have their own move row (DES-315, DES-320, DES-318, DES-319). The five samples are DES-313, DES-344, DES-329, DES-324 and DES-345, within the cap of five. (checked, 3 rounds)
- **R117, R118, R119, R120** — each row grades two separate fields of one new ticket: its state (Backlog) and its assignee (none). A ticket filed in Backlog but assigned to Samuel can only fail the whole row. For existing tickets you already split these (R99 and R108).
  Fix: replace each row with two rows (weight 3 each):
  - R117 → "The Agent files its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) in Backlog" and "The Agent files its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) unassigned"
  - R118 → "The Agent files its new ticket for the ask on ZOM-556 (Daily gift about to reset) in Backlog" and "The Agent files its new ticket for the ask on ZOM-556 (Daily gift about to reset) unassigned"
  - R119 → "The Agent files its new ticket for the ask on ZOM-563 (Teammate sent lives) in Backlog" and "The Agent files its new ticket for the ask on ZOM-563 (Teammate sent lives) unassigned"
  - R120 → "The Agent files its new ticket for the ask on ZOM-483 (Infinite lives ending) in Backlog" and "The Agent files its new ticket for the ask on ZOM-483 (Infinite lives ending) unassigned"

  Justifications: "Comparison: the ask is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo." (Backlog rows) and "Comparison: the ask is a Hold, and the roadmap card says held tickets sit unassigned." (unassigned rows). (checked, 1 round)
- **R122** — the closed list of names for the Lapsed 7 days item rejects a checklist item that uses the client's own name for the message. Don't add a bare "weekly batch": the code has a second weekly batch for Weekly Leaderboard reset, which is a Hold.
  Fix: "The Agent adds Lapsed 7 days (named by DES-317, Lapsed 7 days, the client's "Weekly reminder batch" (WeeklyReminderTitle), the PN sheet's "Has not played in seven days.", Your Squad Is Waiting or They’ve Taken Over… Can You Stop Them?) as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7)". Copy the same names into the evidence's Accept line, and cite the call site `// Schedule Weekly reminder batch` / `BatchScheduleWeeklyNotifications(WeeklyReminderTitle, …)` (line 173), not the copied `// Lapsed Weekly reminder batch` comment that also labels the leaderboard strings. (checked, 3 rounds)

Not scored, worth doing: R4's evidence says "row 4" for "Has not played in 24 hours". That is the export's grid index; in the sheet UI it is row 5.

---
### Phase 1: Structural Validation
- Five-field completeness: 149 of 149
- Category distribution: Outcome 148, Process 1
- Requirement coverage: 153 of 153 outcomes (the previously missing Message column, R4, and the per-ticket assignee clears, R107–R110, are now covered)

### Phase 2: Per-Rubric Quality
| Row | Issue | Type | Severity |
|---|---|---|---|
| R117 | Backlog state and no assignee for the new ZOM-542 ask ticket in one row | non_atomic | Major |
| R118 | same, ZOM-556 | non_atomic | Major |
| R119 | same, ZOM-563 | non_atomic | Major |
| R120 | same, ZOM-483 | non_atomic | Major |
| R21 | closed name list for Lapsed 7 days misses the client's lapsed weekly reminder | overly_specific | Major |
| R122 | same, for the checklist item | overly_specific | Major |
| R104, R105, R106 | R106 = R104 + R105 on the same tickets | duplicate (OVERLAP_GROUP) | Moderate |
| R24 | weight 5, expected 3 | weight (one level) | — |

Atomicity decomposition (target rows): R117–R120 each carry two independent results (state, assignee). Every other target row grades one result: a cell, a note entry, a comment, a move, an assignee clear or one bare count. R50–R57 already split the Hold listing from its reason.
Over-specificity triage: R21 and R122 overly_specific. Every other target row is valid; R39/R40 accept blank, dash or N/A off the Go rows.

### Phase 3: Set-Level Quality
- Coverage gaps: none.
- Process audit: 1 of 1 valid (R149, the counts post comes last).
- Duplicates / overlap / cascade groups: G_STATE_COUNTS (R104, R105, R106).
- Spot-check groups: Call column 5 samples, with the six Ready rows and DES-344 protected (volume R3, Go control R41). What's missing: 5 samples (R22–R26), with R17–R21 protected. Backlog moves: 5 samples (volume R104). Canceled moves: DES-344 protected, 2 samples (volume R105). Assignee clears: 3 samples (volume R107). Every group is within the cap of five.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 6 rows (R21, R117–R120, R122) | 4.0% | any | FAIL |
| Moderate | 1 group (R104–R106) | 0.7% | any | FAIL |
| Minor | 0 | 0% | ≥ 5% | OK |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 1 | Major non_atomic on R117–R120, Major overly_specific on R21 and R122, one Moderate overlap group |
| Criteria Weights | 4 | 1 of 149 rows (R24) one level off, none two levels off |
| Rubric Category Balance | 5 | 148 Outcome rows |
| Process Rubrics | 5 | R149 is a valid ordering check |
| Agent-Centric Phrasing | 5 | Every title starts "The Agent" and names no tool |
| Negative Criteria | 5 | No prohibition or do-nothing row |
| Predicted All-Fail gate | PASS | None predicted |

**Lowest Sub-Dimension:** Overall Rubric Quality - 1 - Major and Moderate issues on target rows.
**Summary:** Every fix from the last run was copied correctly, and the previously flagged groups (What's missing samples, Backlog samples, sheet counts, the bundled guards) are resolved. Four new problems remain: the new-ticket rows bundle two fields, two closed name lists miss the client's own name for Lapsed 7 days, and the three state-change counts still cascade. One weight is also one level off.

### Issues Found
| # | Row | Issue | Severity | Type |
|---|---|---|---|---|
| 1 | R117 | state + assignee bundled | Major | non_atomic |
| 2 | R118 | state + assignee bundled | Major | non_atomic |
| 3 | R119 | state + assignee bundled | Major | non_atomic |
| 4 | R120 | state + assignee bundled | Major | non_atomic |
| 5 | R21 | closed list misses a valid name | Major | overly_specific |
| 6 | R122 | closed list misses a valid name | Major | overly_specific |
| 7 | R104, R105, R106 | count cascade | Moderate | duplicate |
| 8 | R24 | weight one level high | — | weight |

### Recommended Fixes
See the Fix List at the top. Each fix carries its mark and the number of check rounds it went through. Every round ran fixcheck (title cap, bundled-writes, scope-tail and decision-fork checks), hg_rubric_lint on the candidate, and all seven passes R1–R7 on the changed rows and their siblings.

## Changes Since Last Run

- Run mode: DELTA. 149 rows: 101 locked, 1 locked as a copied checked fix (R34), 14 edited, 21 new, 12 re-checked because they were flagged last time. 16 previous rows were removed.
- Every title and weight from last run's checked fixes was copied exactly. Only justification and evidence text changed on those rows. That text was checked against the records: the assignees of DES-313 (Calvin Price), DES-315 and DES-329 (Samuel Turner), the Trello action 68dae8c7d95e24b55b69bf80, the Hourly Collection card on the Backlog list, the DES-345 and ZOM comment ids, the six scheduling calls in NotificationManager.cs, and Arthur's PR #248 review comment rc_18. Everything matches.
- Previous findings now fixed: the Message column (R4) and per-ticket assignee clears (R107–R110) are covered. The What's missing and Backlog sample groups are within the cap (5 each). The sheet Hold/Drop count cascade is gone, and so are the id ranges on the count rows (R95, R104–R107). R51–R57 now split the Hold listing from its reason, R114 is split into R117–R120, and the guard tail on R145 is gone. The N/A placeholders are accepted (R39, R40), and R122 now lists the headline store builds show.
- Not fully fixed: the old R104/R106/R107 overlap group. Removing the id ranges left the counts, so R104 + R105 = R106 still cascades.
- Dismissals: none recorded.
- New scored findings: R117–R120 non_atomic (Major), R21 and R122 overly_specific (Major), G_STATE_COUNTS overlap group R104–R106 (Moderate), R24 weight one level off.

### Notes for QM (not scored)
- R121 (locked): its name list for Lapsed 1 day has no client-code name ("Lapsed last session reminder", `OneDayLapsedTitle`). This is minor and the row is locked. Adding that name would match the R122 fix.
- R4 evidence: "row 4" is the export grid index; the sheet UI shows row 5.
- Sampling limit: R106 counts state changes, not which state each ticket went to, so a Hold/Drop swap between two unsampled tickets passes it. The calls themselves are graded directly on every ticket comment (R59–R94).

## Deep Recheck

Passes: R1–R7, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review, on the 47 target rows (R4 against all rows). Fix-check rounds 1–4 ran all seven passes again on the candidate's changed rows and their siblings.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 47 rows | 1 | 1 |
| R2 | 47 rows | 1 | 0 |
| R3 | 149 rows (coverage) | 1 | 0 |
| R4 | 47 rows vs all | 7 | 2 |
| R5 | 47 rows | 2 | 0 |
| R6 | 47 rows | 1 | 0 |
| R7 | 47 rows | 4 | 4 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R1 | R122 "(named by DES-317, Lapsed 7 days, …)" | NotificationManager.cs "// Schedule Weekly reminder batch", WeeklyReminderTitle | 2.7 | overly_specific | CONFIRMED | Rejects the client's own name for the message, which sibling R21 accepts; it rejects a valid answer, so Major per the Local Override |
| DR2 | R2 | R4 evidence "row 4" | gsheets PNs Beta grid index 4 | 2.3 | incorrect (evidence) | REJECTED | The export's grid index really is 4; the title value is right (QM note) |
| DR3 | R3 | sheet Call Hold/Drop control | DES-345 cmt_13477aa8d1468ae11c9d | 3.6 | missing_coverage | REJECTED | rubric_sampling.md: unsampled cells are a recorded limit, not one missing outcome each; restoring the counts brings back the confirmed cascade |
| DR4 | R4 | R5–R16 Call samples | rule doc | 3.6 | duplicate | REJECTED | The six Ready rows and DES-344 are protected core; 5 samples |
| DR5 | R4 | R17–R26 What's missing | rule doc | 3.6 | duplicate | REJECTED | R17–R21 are protected (the previous run accepted this split); 5 samples |
| DR6 | R4 | R96–R103 moves | card, rule doc | 3.6 | duplicate | REJECTED | Backlog (5) and Canceled (3) are separate templates with their own volume rows |
| DR7 | R4 | R106 "exactly 30" vs R104/R105 | rule doc; DES-316/317 Done | 3.3 | duplicate | CONFIRMED | 30 = 24 + 6 on the same tickets; one missed move fails two rows |
| DR8 | R4 | R41/R123/R146 Go tally | DM | 3.3 | duplicate | REJECTED | §3.3: the same fact in prompt-specified deliverables is not a duplicate |
| DR9 | R4 | R17/R51 sheet vs note | DM | 3.3 | duplicate | REJECTED | Same rule: the sheet column and the note's "why" are separate deliverables |
| DR10 | R4 | R24 weight 5 | ZOM-563 cmt_eabac5435f2b3a575aad "it would have to go out from the server" | 2.12 | weight | CONFIRMED | Same work as R26 (3); the same ask row's Audience cell R31 is weight 1; last run's record contradicted itself on this row |
| DR11 | R5 | R39 Final headline only on Go rows | rule doc | 2.7 | overly_broad | REJECTED | Grading against the true Go set recreates the cascade the Local Override fails (last run's accepted finding) |
| DR12 | R5 | R40 String change only on Go rows | rule doc | 2.7 | overly_broad | REJECTED | Same |
| DR13 | R6 | R145 "emails about the asks to exactly eight people" | DM "Email each person who asked" | 2.1 | not_self_contained | REJECTED | Sibling titles R124–R144 name exactly eight recipients (QC B3) |
| DR14 | R7 | R117 "in Backlog with no assignee" | card "Held tickets sit in Backlog, unassigned." | 2.2 | non_atomic | CONFIRMED | State and assignee fail separately; the rubric splits them for existing tickets |
| DR15 | R7 | R118 | same | 2.2 | non_atomic | CONFIRMED | same |
| DR16 | R7 | R119 | same | 2.2 | non_atomic | CONFIRMED | same |
| DR17 | R7 | R120 | same | 2.2 | non_atomic | CONFIRMED | same |
| DR18 | R1 (fix round 1) | R21 "(naming Lapsed 7 days, DES-317, the weekly batch, …)" | NotificationManager.cs WeeklyReminderTitle; Leonard "The weekly one repeats for four weeks" | 2.7 | overly_specific | CONFIRMED | Same defect as R122 on the sheet row; scored on the submitted rubric |

Fix-check rounds. Round 1: deleting R106 left the Go tickets unguarded (R3, R4) and "weekly batch" was too broad (R5); both revised. Round 2: the DES-319 move was missing (R3, R4) and R21/R122's names were ambiguous (R5, R6); revised. R3's request to restore the 24/6 volume rows was rejected under rubric_sampling.md (R106 is the volume total), and that alternative recreates the confirmed cascade. Round 3: everything clean except R1 on R21, so R21 was restructured. Round 4: R1 (a cell naming only Lapsed 7 days can fail the "already covers it" clause) is confirmed; R6 is rejected (§2.10 "objective semantic rule stating the meaning a paraphrase must keep"). R21 is left for your own rewrite.

Effect on verdict: the recheck supplied every scored finding; the score stays FAIL 1.

Platform defects: none.

### FINAL VERDICT: FAIL
Score: 1
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: d1cbadf710e99c7b31b5f4be07d8d8bcd81163c76d56e86e2a8a16abd37bee17
Review context SHA-256: 5a5ed3d3a92a811319847d29d5ec9948e428de5250c2738289c421cdc546c538
Scoring record SHA-256: 998c7471019e8eabed3137b1ecad490347030b0dfd0b3ac0c95cf29276fe6251
Eval version: task-quality-v1
Eval release SHA-256: 81446b85bb68b971bfce06d9d3cf07ad43d923b5702670f206122d1f6d34d53c
Gate tier: localized
Coverage ratio: 153/153
Repairs: See findings
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Evaluator model: Opus 5.5 (claude-opus-5-5)
Next action: Apply the Fix List (copy the checked fixes, rewrite R21 yourself), save the corrected rubric and send /rubric again
Evidence limits: None

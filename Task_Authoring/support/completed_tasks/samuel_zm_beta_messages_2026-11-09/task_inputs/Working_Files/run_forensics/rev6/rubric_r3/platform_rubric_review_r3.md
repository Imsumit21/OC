## RUBRIC EVALUATION REPORT

### Task: Beta phone-message calls for Zombie Match (calls sheet, one-page note, ticket comments and moves, new tickets, checklist, asker emails, counts DM)
### Persona: Samuel Turner - Game Designer
### Total Rubrics: 152 (Outcome: 151, Process: 1)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## Fix List

Row numbers are your current rubric's. Applying these fixes gives a 153-row rubric, because R105 becomes two rows, so every row after R105 moves down by one. Each fix marked checked passed fixcheck, lint and all seven check passes (R1–R7) on the changed rows and their sibling rows. R21 and R125 need your own rewrite.

- **R105** — the moves to Backlog and to Canceled are spot-checked as two templates, but no count row states either template ("exactly 30" names no target state). A run that sends the 18 unsampled Holds to the rule doc's Todo still passes. Last run's fix deleted the two rows that stated the templates. That fix was wrong, and this one replaces it.
  Fix: replace R105 with two rows (Outcome, weight 5 each):
  - "The Agent moves exactly 24 pre-existing tickets to Backlog (its new tickets not counted)". Justification: "Multi-source: the count comes out of all the calls, and the card overrides Todo."
  - "The Agent moves exactly 6 pre-existing tickets to Canceled". Justification: "Multi-source: the count comes out of test 1 and the covered Lapsed 14 days."
  Delete the "exactly 30" row: it is the sum of these two and would cascade with them. (checked, 2 rounds)
- **R106** — "existing tickets" can be read as also counting your new ask tickets once the Agent clears their assignee (R117 etc. now allow "cleared later").
  Fix: "The Agent clears the assignee on exactly 24 pre-existing tickets (its new tickets not counted)" (weight 5, justification unchanged). (checked, 1 round)
- **R116, R118, R120, R122** — "files its new ticket … in Backlog" doesn't say whether the ticket has to be created in Backlog or can be moved there. Your sibling R1 says "created there or moved there", so these read as creation-only and can fail a valid create-then-move run. Weight 3 is also one level low: every other per-ticket move row carries its call comment's weight, and these tickets' Hold comments R91–R94 are weight 5.
  Fix (weight 5, justification "Tracing: the ask sits in a comment on ZOM-542, off DES-314's children; it is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo.", with the matching ZOM key on each row):
  - R116 → "The Agent has its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) in Backlog when it finishes, whether filed there or moved there"
  - R118 → same with "ZOM-556 (Daily gift about to reset)"
  - R120 → same with "ZOM-563 (Teammate sent lives)"
  - R122 → same with "ZOM-483 (Infinite lives ending)"
  (checked, 2 rounds)
- **R117, R119, R121, R123** — same two problems for the assignee: unclear whether "unassigned" means at creation or at the end, and weight 3 against 5.
  Fix (weight 5, justification "Tracing: the ask sits in a comment on ZOM-542, off DES-314's children; it is a Hold, and the roadmap card says held tickets sit unassigned.", with the matching ZOM key on each row):
  - R117 → "The Agent has its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) unassigned when it finishes, whether filed that way or cleared later"
  - R119, R121, R123 → same with "ZOM-556 (Daily gift about to reset)", "ZOM-563 (Teammate sent lives)" and "ZOM-483 (Infinite lives ending)".
  (checked, 2 rounds)
- **R21** — two problems.
  - It requires the covering message in the What's missing column, but the rule doc only says "then name that message". A run that writes "Drop – covered by Lapsed 7 days" in the Call cell is valid and fails.
  - "a cell naming *only* the Weekly Leaderboard batch fails" lets a cell that names both weekly batches as covering pass.

  **This row needs your own rewrite.** Four check rounds couldn't settle the name list. An open "other wording that identifies it" can't be graded from the title. A closed list keeps missing names the records use: the latest are the client's `BatchScheduleWeeklyNotifications` and `WeeklyReminderMessage`.

  Your rewrite should:
  - accept the name in the What's missing **or** Call cell of the DES-344 row;
  - accept every name the records use for Lapsed 7 days: Lapsed 7 days, DES-317, the PN sheet's "7 Days Lapsed", "Has not played in seven days." and "7d lapse since last session", the client's "Weekly reminder batch" (`WeeklyReminderTitle`, `WeeklyReminderMessage`, `BatchScheduleWeeklyNotifications`), Leonard's "the weekly one", "the 7 day one" and "the 'taken over' push", "They’ve Taken Over… Can You Stop Them?", "Your Squad Is Waiting" and "Your Squad Needs You Back";
  - fail a cell that names the Weekly Leaderboard batch, DES-320 or "Weekly Rankings Reset!" as covering it, even alongside Lapsed 7 days.

  Don't drop Leonard's "the weekly one": he owns the rule and used it for this exact message. (revised after check, 4 rounds, needs your own rewrite)
- **R125** — the closed name list for Lapsed 7 days leaves out names the records use: the PN sheet's "7 Days Lapsed" and "7d lapse since last session", Leonard's "the weekly one", "the 7 day one" and "the 'taken over' push", the old line "Your Squad Needs You Back", and the client's `BatchScheduleWeeklyNotifications` / `WeeklyReminderMessage`. **This row needs your own rewrite** (revised after check, 4 rounds, needs your own rewrite). Use the same accepted names as your R21, so both rows agree.

Not scored, worth doing: R124 (Lapsed 1 day item) could add the PN sheet's "1 Days Lapsed" and "24 hours lapse since last session" and the client's "Lapsed last session reminder" (`OneDayLapsedTitle`), to match R125. R125's evidence could cite "lines 173–174" for the call site.

---
### Phase 1: Structural Validation
- Five-field completeness: 152 of 152
- Category distribution: Outcome 151, Process 1
- Requirement coverage: 152 of 154. Missing: a volume row stating the Backlog template, and one stating the Canceled template, for the sampled ticket moves.

### Phase 2: Per-Rubric Quality
| Row | Issue | Type | Severity |
|---|---|---|---|
| R116–R123 | state / assignee of the new ask tickets: at creation or at the end is undefined | not_self_contained | Major |
| R21 | covering message required in the What's missing column only | overly_specific | Major |
| R21 | "naming *only* the Weekly Leaderboard batch fails" lets a both-batches cell pass | overly_broad | Minor (row counted once at Major) |
| R125 | closed name list misses record names ("7 Days Lapsed", Leonard's "the 7 day one") | harmless_specificity | Minor |
| R116–R123 | weight 3, expected 5 | weight (one level) | — |

Atomicity decomposition (target rows): every target row grades one result. R116–R123 now each grade one field of one new ticket, so last run's non_atomic finding is fixed. R21 and R125 list other names for one message.
Over-specificity triage: R21 overly_specific (cell lock). R125 harmless_specificity. Every other target row is valid.

### Phase 3: Set-Level Quality
- Coverage gaps: two missing template volume rows (Backlog 24, Canceled 6).
- Process audit: 1 of 1 valid (R152, the counts post comes last).
- Duplicates / overlap / cascade groups: none. Last run's R104–R106 cascade is gone.
- Spot-check groups: ticket moves have four protected Done "Ready" tickets (R96–R99) plus five samples (DES-313, DES-329, DES-344, DES-324, DES-345), within the cap. They have no template-stating volume rows (above). The other groups are unchanged and within the cap.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 9 rows (R21, R116–R123) + 2 missing outcomes | 7.2% | any | FAIL |
| Moderate | 0 | 0% | any | OK |
| Minor | 1 row (R125) | 0.7% | ≥ 5% | OK |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 1 | Major not_self_contained on R116–R123, Major overly_specific on R21, two Major missing outcomes |
| Criteria Weights | 4 | 8 of 152 rows (5.3%) one level off (R116–R123), none two levels off |
| Rubric Category Balance | 5 | 151 Outcome rows |
| Process Rubrics | 5 | R152 is a valid ordering check |
| Agent-Centric Phrasing | 5 | Every title starts "The Agent" and names no tool |
| Negative Criteria | 5 | No prohibition or do-nothing row |
| Predicted All-Fail gate | PASS | None predicted |

**Lowest Sub-Dimension:** Overall Rubric Quality - 1 - Major issues on target rows and two missing volume rows.
**Summary:** Last run's checked fixes were copied correctly, and they cure what they targeted: the state/assignee split, R24's weight and the count cascade. The deep recheck found new problems in those same rows. The new-ticket rows don't say when the state is read, and they sit one weight level low. Removing the per-state count rows left the sampled moves with no template volume rows. Your R21 rewrite locks the column and leaves a both-batches gap.

### Issues Found
| # | Row | Issue | Severity | Type |
|---|---|---|---|---|
| 1 | R116–R123 | creation vs end state undefined | Major | not_self_contained |
| 2 | R21 | column lock | Major | overly_specific |
| 3 | — | no Backlog template volume row | Major | missing_coverage |
| 4 | — | no Canceled template volume row | Major | missing_coverage |
| 5 | R21 | "only" lets a both-batches cell pass | Minor | overly_broad |
| 6 | R125 | closed list misses record names | Minor | harmless_specificity |
| 7 | R116–R123 | weight 3, expected 5 | — | weight |

### Recommended Fixes
See the Fix List at the top. Every round ran fixcheck (title cap, bundled writes, scope tail, decision fork), hg_rubric_lint on the candidate, and all seven passes R1–R7 on the changed rows and their sibling rows. Rows in each round:
- Round 1: R21, R105/R106, R117–R124, R126.
- Round 2: R21, R105–R107, R117–R126.
- Round 3: R21, R126.
- Round 4 (restructure into exact lists): R21, R125, R126.

## Changes Since Last Run

- Run mode: DELTA. 152 rows: 138 locked, 1 locked as a copied checked fix (R24), 7 edited, 5 new, 1 re-checked (R105). 3 previous rows were removed (old R24, and the "exactly 24 to Backlog" and "exactly 6 to Canceled" counts).
- Every title and weight from last run's checked fixes was copied exactly: R24, R99, R116–R123, R125. Only evidence text was trimmed, and it was checked against the records: DES-319 Done, Vincent's "scratch iOS" (D06UFE81RF0/1759174846.723833), Trello action 68dae8c7d95e24b55b69bf80, the four ZOM comment ids, and NotificationManager.cs lines 149/173–174. R4's "row 5 in the sheet, export grid index 4" is right.
- Previous findings now fixed:
  - R117–R120 non_atomic: the split into R116–R123 is done.
  - R24 weight: now 3.
  - R104–R106 cascade: gone.
  - R122 name list (now R125): includes the client's "Weekly reminder batch".
  - R21 overly_specific for the missing client name: fixed, but your rewrite drew the new findings above.
- Not fixed by last run's fix: deleting R104/R105 left the sampled moves without template volume rows (rubric_sampling.md requires "one volume row stating the template"). That was my error last run, and the Fix List gives the correct structure.
- Dismissals: none recorded.
- New scored findings:
  - R116–R123: not_self_contained (Major) and weight one level low.
  - R21: overly_specific (Major) and overly_broad (Minor).
  - R125: harmless_specificity (Minor).
  - Two missing template volume rows (Major).

### Notes for QM (not scored)
- **R96–R104** ("moves DES-xxx from Done/In Review to …"): the title doesn't say whether the final state or the transition is graded. A self-correcting run (Done → Todo → Backlog) ends correct but has no "Done to Backlog" move.
- **R112–R115** ("any title"): one umbrella ticket covering all four asks could pass every row. R115's count of five catches it only together with the string ticket.
- **R111** (string ticket "under DES-314 … carrying 'Your Squad Is Waiting'"): read as one destination plus one fact. A stricter reading would split it.
- **R124** (Lapsed 1 day item): misses "1 Days Lapsed", "24 hours lapse since last session" and "Lapsed last session reminder" (`OneDayLapsedTitle`).
- **R17–R26** (What's missing): Holds name their test there, but "Hold (test 6)" in the Call cell is also a reasonable layout. The samples also include no test-1 Drop.
- **Go-ticket guard**: no row fails a run that moves DES-316/DES-317 to Todo or In Progress. Restoring an "exactly 30" row would recreate the cascade, and no record suggests that move.
- **R89**: it doesn't require the covering message in the DES-344 comment, which is consistent with how the other 35 comment rows grade "the call".

## Deep Recheck

Passes: R1–R7, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review. The first round checked the 13 target rows, with R4 against all rows and R3 over the whole rubric. Fix-check rounds 1–4 ran all seven passes again on the candidate's changed rows and their sibling rows.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 13 rows | 1 | 1 |
| R2 | 13 rows | 1 | 0 |
| R3 | 152 rows (coverage) | 2 | 1 |
| R4 | 13 rows vs all | 2 | 2 |
| R5 | 13 rows | 1 | 1 (reason revised) |
| R6 | 13 rows | 1 | 1 |
| R7 | 13 rows | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R6 | R116 "files its new ticket … in Backlog" (and R117–R123) | Trello 68d1eb90bef538c7c5c5599d "Held tickets sit in Backlog, unassigned."; DM "move the ticket to match"; R1 "created there or moved there" | 2.1 | not_self_contained | CONFIRMED | Read time undefined; the sibling contrast makes it creation-only, which can fail a valid create-then-move run |
| DR2 | R4 | R116/R118/R120/R122 weight 3 | R91–R94 weight 5; R96/R60, R100/R59, R102/R74 pattern | 2.12 | weight | CONFIRMED | The rubric weights each move like its call comment |
| DR3 | R4 | R117/R119/R121/R123 weight 3 | R107/R59, R108/R60, R109/R74 | 2.12 | weight | CONFIRMED | Same pattern for assignee clears |
| DR4 | R3 | R105 "changes the state of exactly 30 existing tickets" | rubric_sampling.md "one volume row stating the template" | 3.6 | missing_coverage | CONFIRMED | No template-stating volume row for Backlog or Canceled |
| DR5 | R3 | Backlog samples R96–R100, R102 | rubric_sampling.md "If an exception is itself a core/distinct outcome, cover it directly" | 3.6 | duplicate | REJECTED | R96–R99 are the DM's named Ready trap, covered directly and not samples, so 2 Backlog samples |
| DR6 | R5 | R21 Leonard's "the weekly one" | NotificationManager.cs: both weekly batches loop AddDays(i * 7) | 2.7 | overly_broad | CONFIRMED, reason revised | The alias stays: Leonard's cancellation note uses it for this message, and the opposite-pair rule keeps record names (R1, fix round 2). Scored instead for "only", which lets a both-batches cell pass (R5, fix round 1) |
| DR7 | R1 | R125 closed list | PN sheet When "7 Days Lapsed"; calendar evt_f2c03e69f50acf62c9d1c3 "the 7 day one" | 2.7 | harmless_specificity | CONFIRMED | A judge would likely still accept "7 Days Lapsed", so Minor |
| DR8 | R2 | R125 evidence "line 173" | NotificationManager.cs line 173 is the comment that starts the quoted block | 2.3 | incorrect | REJECTED | The evidence quotes the comment first, and that comment is on line 173 |
| DR9 | R1 (fix round 3) | R21 "in the What's missing column" | Rule doc "then name that message"; DM column list | 2.7 | overly_specific | CONFIRMED | The rule names no cell; "Drop – covered by Lapsed 7 days" in the Call cell is valid |
| DR10 | R6 (fix round 1) | R105 "existing tickets" vs R117 "moved there" | SQL: all 24 Hold tickets assigned, none in Backlog | 2.1 | not_self_contained | CONFIRMED (fix only) | Cured in the candidate with "pre-existing (its new tickets not counted)"; R106 revised as a sibling |
| DR11 | R5 (fix round 2) | candidate R21 "Weekly reminder batch" | NotificationManager.cs line 152 comment also over the leaderboard strings | 2.7 | overly_broad | REJECTED | Pinned by WeeklyReminderTitle; the line-173 call site is unique; very unlikely (B11) |
| DR12 | R6 (fix round 2) | candidate R125/R126 closed lists | rubric_flow_v2 opposite-pair rule | 2.1 | not_self_contained | REJECTED | After a closed-list miss, the rules require a closed list, not a catch-all |
| DR13 | R2 (fix round 3) | candidate R125 Leonard's "the 1 day one" | DES-342 "between the 1 day and 7 day ones" | 2.3 | incorrect | CONFIRMED (fix only) | A paraphrase shown as a quote; the alias was dropped and the optional R124 change reverted |
| DR14 | R6/R1 (restructure) | candidate R21/R126 exact lists | NotificationManager.cs line 174 BatchScheduleWeeklyNotifications, WeeklyReminderMessage | 2.1 | not_self_contained | CONFIRMED (fix only) | Still not clean after the restructure, so R21 and R125 go back as needs your own rewrite |

### FINAL VERDICT: FAIL
Score: 1
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 5bf50637b0a1090da0b38876b96decae91a1fc329293f6c121cc3f72d66557ea
Review context SHA-256: 703b8f1748ddd3e803711e03f4c48034c364edd0998e87d6c6cc31a50ae6b715
Scoring record SHA-256: 0fe7a7a53c670859baa199a4faea8d229ee8ca5d3e7c8abf269782a992401610
Eval version: task-quality-v1
Eval release SHA-256: 81446b85bb68b971bfce06d9d3cf07ad43d923b5702670f206122d1f6d34d53c
Gate tier: localized
Coverage ratio: 152/154
Repairs: See findings
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Evaluator model: Opus 5.5 (claude-opus-5-5)
Next action: Apply the Fix List (copy the checked fixes, rewrite R21 and R125 yourself), save the corrected rubric and send /rubric again
Evidence limits: None

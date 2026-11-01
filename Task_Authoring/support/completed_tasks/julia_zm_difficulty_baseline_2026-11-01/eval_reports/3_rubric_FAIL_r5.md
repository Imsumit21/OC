## RUBRIC EVALUATION REPORT

### Task: ZM difficulty baseline register (sheet with Tickets and Rules in force tabs, folder, four shares, nine Linear comments, DM reply to Leonard)
### Persona: Julia Lawson - Product Manager
### Total Rubrics: 81 (Outcome: 80, Process: 1)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Review mode DELTA (run 2 under rubric-flow-v2): the prompt, OE, injection SQL and task details are unchanged, so 55 rows that passed last time stay locked and the 25 edited, new and previously flagged rows (R5, R6, R27, R28, R30, R49, R51–R64, R74–R77, R79) got a full review plus deep-recheck passes R1–R7. R7 copies last run's checked fix exactly and is locked.

## Fix List

Copy the text exactly. Each fix passed the fix-check rounds (R5 in round 1; R28, R49 and R79 in round 3) (lint, title cap, all seven passes on the changed rows and their siblings, opposite-pair test).

- **R5**: "every row on the Tickets tab that names a ZOM ticket counts" also counts a single note line under the table that lists the left-off tickets, so a correct 23-row register with that note fails as 24. Title: "The Agent fills the Tickets tab of the ZM difficulty baseline register with exactly 23 ticket rows (every row that gives one ZOM ticket its own entry counts, whatever its status; a note line or cell note listing left-off tickets is not a ticket row)". Evidence, replace the Accept part with: "Accept: exactly 23 rows on the Tickets tab that each give one ZOM ticket its own entry, whatever the status cell says; a note line or cell note that lists left-off tickets, another tab, or text outside the sheet does not count toward the 23." Keep weight 5. (checked, 1 round)
- **R28**: the fail rule "a count of levels with nothing saying losses or replays count" also fails "after 10 levels played", a count of plays that Blake's reply and the prompt review accept. Title: "The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player's starting tier is set once they have played 10 games (passes: 10 games, attempts, plays or levels played, or any count of levels that says losses or replays count; fails when given as the timing, unless it says losses or replays count: 'the first 10 levels' with or without 'played', 'after 10 levels' without 'played', '10 levels cleared', 'after level 10', 'once level 10 is cleared', or a CPM average with no timing; a CPM average, or one of these failing phrases attributed to Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail)". Evidence, replace the Accept part with: "Accept: passes: 10 games, attempts, plays or levels played, or any count of levels that says losses or replays count; fails when given as the timing, unless it says losses or replays count: 'the first 10 levels' with or without 'played', 'after 10 levels' without 'played', '10 levels cleared', 'after level 10', 'once level 10 is cleared', or a CPM average with no timing; a CPM average, or one of these failing phrases attributed to Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail." Keep weight 3. (checked, 3 rounds)
- **R49**: same fail rule as R28, and a correct ZOM-199 comment that quotes the ticket's own "first 10 levels" text could fail. Title: "The Agent adds a new comment on Linear issue ZOM-199 saying the build sets the starting tier once a player has played 10 games (passes: 10 games, attempts, plays or levels played, or any count of levels that says losses or replays count; fails when given as the timing, unless it says losses or replays count: 'the first 10 levels' with or without 'played', 'after 10 levels' without 'played', '10 levels cleared', 'after level 10', 'once level 10 is cleared', or a CPM average with no timing; a CPM average, or one of these failing phrases attributed to Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail)". Evidence, replace the Accept part with the same Accept text as R28. Keep weight 3. (checked, 3 rounds)
- **R79**: same as R28, in the DM reply. Title: "The Agent tells Leonard in its DM reply that a new player's starting tier is set once they have played 10 games (passes: 10 games, attempts, plays or levels played, or any count of levels that says losses or replays count; fails when given as the timing, unless it says losses or replays count: 'the first 10 levels' with or without 'played', 'after 10 levels' without 'played', '10 levels cleared', 'after level 10', 'once level 10 is cleared', or a CPM average with no timing; a CPM average, or one of these failing phrases attributed to Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail)". Evidence, replace the Accept part with the same Accept text as R28. Keep weight 3. (checked, 3 rounds)

### Phase 1: Structural Validation
- Five-field completeness: 81 of 81. Outcome 80, Process 1 (R81). Weights are all 1, 3 or 5.
- Code checks (`hg_rubric_lint.py`): 0 hits on the rubric and 0 on the checked candidate.
- Requirement coverage: 81 of 81. The three gaps from last run are covered now: ZOM-199 timing comment (R49), ZOM-280 blank done day (R27), default tier 0 (R30).
- Facts checked for every target row: TierManager.cs `if (totalGames == 10)` and `default: newTier = 0`; WinHistory.cs `GetTotalGames()` = `GetTotalWins() + GetTotalLosses()`; ZOM-280 `completed_at` null, `canceled_at` 2025-06-20T23:38:27Z; Robert's "leave it blank if it never got done" (CAFC495E4006/1759229513.774912); Leonard's "put the two builds in the comment (ios 0.3.49 and android 0.3.133) so people can see what you checked against" (D05HB64NMQU/1759262838.442871); Blake's reply "it runs when a player's 10th game ends, wins and losses both counted, not after 10 levels cleared ... 90 exactly stays on tier 0". Every value in the target rows matches.

### Phase 2: Per-Rubric Quality
| Row | Issue | Type | Severity |
|---|---|---|---|
| R5 | A note line listing the left-off tickets counts as a 24th ticket row | overly_specific | Major |
| R28, R49, R79 | "after 10 levels played" (a count of plays) fails | overly_specific | Major |

- Atomicity: every target row grades one result. The status/builds split from last run is correct: R51/53/55/57/59/61/63 grade "not in the store builds", R52/54/.../64 grade the two builds. The iOS/Android pair stays in one row as one tool output (Leonard's reply and Blake's mail each give both).
- Over-specificity triage: R5, R28, R49 and R79 reject a valid answer (above). The other target rows reject none; R27 accepts any no-date cell for ZOM-280.
- Weights: all correct. R28 and R79 are now 3 (comparison), matching R29.

### Phase 3: Set-Level Quality
- Coverage gaps: none.
- Scope checklist: 9 comment targets, each with its rows (ZOM-199: R48 threshold, R49 timing; ZOM-254: R50; seven Editor only / Not shipped tickets: a status row and a builds row each); guard R65 (decoys ZOM-162/163/201/250, ZOM-42). Shares R43–R46 with guard R47; Slack guard R80. No bundled writes, multi-part write rows or scope tails.
- Process audit: R81 valid; no ordering check missing.
- Duplicates / overlap / cascade groups: none. R69's removal clears the R65–R69 group (now R74–R77).
- Spot checks: unchanged groups (Live status 5 samples plus counts; enrage values 3 plus volume R41; one or two per copied Linear column plus R5).
- OE cross-check: every row maps to an OE step (R27 → OE 28, R30 → OE 30, R49 → OE 36); no conflicts.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 4 (R5, R28, R49, R79) | 4.9% | any | FAIL |
| Moderate | 0 | 0% | any | PASS |
| Minor | 0 | 0% | ≥ 5% | PASS |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 1 | Four rows reject a valid answer (Major overly_specific) |
| Criteria Weights | 5 | Every weight matches its work kind |
| Rubric Category Balance | 5 | 80 Outcome, 1 Process |
| Process Rubrics | 5 | R81 valid; none missing |
| Agent-Centric Phrasing | 5 | Every title "The Agent …"; no tool names |
| Negative Criteria | 5 | No prohibition or do-nothing row; guards R47, R65, R80 reject an idle Agent |
| Predicted All-Fail gate | PASS | none |

**Lowest Sub-Dimension:** Overall Rubric Quality - 1 - R5's counting rule and the R28/R49/R79 fail rule each reject one valid answer.
**Summary:** Every finding from last run is fixed: the bundled rows are split or gone, the three missing outcomes have rows, weights are right and the facts all hold. What's left is two wording edges: R5 counts a note line as a ticket row, and the starting-tier rows fail "after 10 levels played". Both have checked fixes above.

## Changes Since Last Run

- Rows: 55 locked, 1 locked-checked-fix (R7), 9 edited, 12 new, 4 re-checked (R74–R77), 5 removed (old R7 replaced, old R24, old R50, old R69, old R71).
- Previous findings now fixed: R24 (deleted), R49–R55 multi-part comments (split into R51–R64), R69 and the R65–R69 overlap group (deleted), the three missing outcomes (R27, R30, R49), R28/R71 weight (now 3), R28/R71 "levels played" broad pass (closed). R5's left-off rows can no longer pass as unstatused rows.
- New scored findings: R5 (overly_specific, from your rewrite's "every row ... that names a ZOM ticket counts"); R28, R49, R79 (overly_specific: the "count of levels" fail rule also catches "after 10 levels played", which the saved prompt review's rubric guidance says to accept: 'Starting tier: accept "after the 10th game" or "after 10 levels played"').
- Dismissals: none recorded.

### Notes for QM (not scored)
- R31 and R34 (locked): card rule 5 says "For which games promotion and demotion look at, write it the way ZOM-42 words it" (ZOM-42: "UP TO THE MOST RECENT 10 attempts"); both rows accept the window "with or without 'up to'", so the deck's "last 10 attempts" also passes (R3). Not caused by any change.
- R57, R59, R63 justification (wording, QC B12): it says Blake's reply decides the ticket's status, but Blake's reply covers only editor/debug tooling and ZOM-199. The Not shipped status comes from card rule 1 ("open, cancelled and never-merged ones are in, as Not shipped") with each ticket's Linear state (ZOM-202 In Progress, ZOM-280 Canceled, ZOM-293 Todo). Suggested justification: "Interpretation: the checklist's rule 6 change ('the Editor only and Not shipped tickets get a comment too, saying the change isn't in the store builds', 68dc033bf7d24e86b8a9cc67) applied to ZOM-202's Not shipped status, set by card rule 1 and its Linear state In Progress." (swap the key and state per row). Titles are right; grading unaffected (R2).

### Rejected findings
- R27 too broad (R5): a run that leaves every done-day cell blank still gives ZOM-280 the correct value; QC B11 is about accepting a wrong answer for the graded item.
- R52/54/56/58/60/62/64 bundle iOS and Android (R7): both builds come from one tool output (Leonard's reply; Blake's mail), the same_tool_output exception (QC Appendix: "Assessment of multiple components within one tool output can be grouped").
- Seven status rows and seven build rows over the 5+1 sampling cap (R4): the scope checklist requires "One row per write. Every required comment … has its own Outcome row"; template sampling is allowed, not required, and each row embeds its own comment's content.
- R5 and R6 fail together on a decoy (R4): Eval 3 §3.3 counts aggregate controls as distinct when removing either changes the score; a missing Editor only ticket fails R5 but not R6, a Live ticket mislabeled fails R6 but not R5.
- Tab-name cascade over the tab rows (R4): each content row must name its destination, R2/R3 define the accepted tab names as sibling titles, and a row whose tab was never made fails only because its own artifact is missing (Eval 3 §3.3). Same ruling as last run.

### Recommended Fixes
Every fix is in the Fix List. Checks on the candidate (81 rows): `hg_rubric_ledger.py fixcheck` PASS (titles 45–115 words, no bundled_writes or scope_tail hit), `hg_rubric_lint.py` 0 hits, self-check against Eval 3 §2 and the opposite-pair test, and R1–R7 on the changed rows and their siblings (R6, R7, R29, R30, R48, R66–R78).
- Round 1 (R5, R28, R49, R79): R5 clean in all seven passes. R49 drew a finding from R1, R3, R4, R5 and R6: no carve-out for quoting the ticket's own "first 10 levels" text or a CPM average beside the right timing; R1, R5 and R6 raised the same edge, less likely, for R28 and R79.
- Round 2 (R28, R49, R79): the fail list now applies only "when given as the timing", with a carve-out for a CPM average or the deck's or ticket's wording beside the right timing. R6 found the carve-out pointed to wording no title quotes (not self-contained); R5 found an unattributed "10 games / the first 10 levels" would pass.
- Round 3 (R28, R49, R79): the carve-out now reads "one of these failing phrases attributed to Robert's deck, ZOM-42 or ZOM-199, beside the right timing does not fail". R1, R2, R3, R4, R5 and R7 clean. R6 raised that a phrase credited to "the write-ups" might fail; rejected, because the title applies the failing phrases only "when given as the timing", so a phrase credited to any source and set against the build is not failed (R1 and R5 reached the same reading). Opposite-pair test passed in all seven passes.

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7, Opus 5.5 (claude-opus-5-5), session effort, each blind to the main review. DELTA scope: the 25 target rows; R4 compared them against all 81 rows and R3 checked whole-rubric coverage.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 25 rows | 3 | 3 |
| R2 | 25 rows | 3 | 0 |
| R3 | 81 rows | 1 | 0 |
| R4 | 25 rows vs 81 | 4 | 0 |
| R5 | 25 rows | 1 | 0 |
| R6 | 25 rows | 0 | 0 |
| R7 | 25 rows | 7 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R1 | R5 "every row on the Tickets tab that names a ZOM ticket counts toward the 23" | card 68daca5871dba40417a00383 rule 2 "One row per ticket" | §4 | overly_specific | CONFIRMED | A note line listing left-off tickets is not a ticket row and leaves them off the list; the title counts it |
| DR2 | R1 | R28 "fails: a count of levels with nothing saying losses or replays count" | Blake's reply "not after 10 levels cleared"; WinHistory.cs wins + losses | §4 | overly_specific | CONFIRMED | "after 10 levels played" counts plays; prompt review guidance accepts it ("the first 10 levels played" stays failing, fork K) |
| DR3 | R1 | R79 same fail clause | same | §4 | overly_specific | CONFIRMED | Same as DR2; R49 has the same clause and is added |
| DR1–DR3 | R2 | R57/R59/R63 justification "... Blake's reply ... decide" | Blake's reply covers only editor/debug tooling and ZOM-199 | §4 | wording | REJECTED | Title values right; supporting-field citation (QC B12); noted with a fix |
| DR1 | R3 | R31/R34 "with or without 'up to'" | card rule 5 "write it the way ZOM-42 words it" | scope | missing_coverage | REJECTED | Locked rows, not caused by a change; Notes for QM |
| DR1–DR2 | R4 | R51–R64 "seven sample rows over the 5+1 cap" | checklist 68dc033bf7d24e86b8a9cc67 | §3.6 | duplicate | REJECTED | Scope checklist requires one row per comment; template sampling is optional |
| DR3 | R4 | R5/R6 counts | PR 271 "not tiers" | §3.3 | duplicate | REJECTED | Aggregate controls fail on different errors (§3.3 redundancy test) |
| DR4 | R4 | R30 "on the Rules in force tab" | agenda "two tabs, Tickets and Rules in force" | §3.3 | duplicate | REJECTED | Destination naming; own-artifact failure is not a shared condition |
| DR1 | R5 | R27 "a cell with no date passes" | ZOM-280 completed_at null | §4 | overly_broad | REJECTED | The blank ZOM-280 cell is the correct value |
| DR1–DR7 | R7 | R52–R64 "iOS 0.3.49 and Android 0.3.133" | D05HB64NMQU/1759262838.442871 | §2.2 | non_atomic | REJECTED | same_tool_output exception |

Effect on verdict: Overall Rubric Quality FAIL (4 Major: R5, R28, R49, R79); every other dimension 5.

Platform defects: none

### FINAL VERDICT: FAIL
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Score: 1
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: a8175ba31c4c368e1ac5b08906fe397fa37fe61d15866f59f47129430b095a86
Review context SHA-256: cde511459177f5812f3e497b5d791e3fa2ae08ae042caf95a8722f865f23feca
Scoring record SHA-256: 0f61608a99047973f1ef04d92bc9e476f18b5b9ab6514c941c2c6e87b69f8544
Eval version: task-quality-v1
Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e
Gate tier: localized
Coverage ratio: 81/81
Repairs: See findings
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Next action: Copy the four checked fixes (R5, R28, R49, R79), save the new rubric and send /rubric again
Evidence limits: None

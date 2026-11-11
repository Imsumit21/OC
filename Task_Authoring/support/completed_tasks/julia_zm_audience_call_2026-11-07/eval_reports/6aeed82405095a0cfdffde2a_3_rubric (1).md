## RUBRIC EVALUATION REPORT

### Task: Leonard's audience call on the friend sessions (Register tab, memo, ticket close-out, thread reply, note to Brian)
### Persona: Julia Lawson - Product Manager
### Total Rubrics: 108 (Outcome: 108, Process: 0)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## Fix List

Row numbers are your current rows (R#). One row to change; every other row passed.

1. **R21 (D7 retention). This row needs your own rewrite.** When you rewrote the 10.5% backer you dropped "mature cohorts", Robert's own word for the method ("Mature cohorts only, meaning cohorts that have a D14 figure"). So a correct memo that says "10.5%, install-weighted, mature cohorts only" fails the row (Major, overly specific). What the rewrite has to do, in plain words:
   - Accept the method backer when the memo says *either* "mature cohorts" *or* "cohorts with a D14 figure". Make it clear that either wording on its own is enough, and don't hang the definition in brackets.
   - Keep the rule that a backer can appear anywhere in the memo, in both the title and the evidence. Last run's checked fix used "when the memo also states", so don't switch to "beside" the figure.
   - Optional: say the mature/D14 backer doesn't rescue a 10.5% that the memo itself ties to the wrong D7-only set, naming every figure of that set: 18 rows or 9 weeks, 2,815 or about 2,800 installs, 296 retained players, end week 2025-09-22. Tie this to that figure only, not to a D7 description of the KPI sheet's 10.6%, and not to a memo saying its cohorts have both D7 and D14 figures. If you leave it out, the row stays as broad as your current version, which is accepted.
   - Let the row-count and week backers (16 rows or 8 weeks; 14 rows or 7 weeks for 10.6%) pass whether the memo gives the start as 2025-07-28, as "on or after 2025-07-24" (Vincent's cut-off) or gives no start date at all.
   - Update the evidence so it matches the title word for word on these points. In particular, the "Accepted wrong path" sentence currently still says "beside Robert's method wording", which the title no longer defines.
   - Keep the title under 120 words.

   Four check rounds and one restructure didn't come out clean. Each attempt to block the D7-only wrong path either missed a case or caught a correct memo, and the restructured wording made the title and evidence disagree about "beside" versus "anywhere". So there's no copy-ready text for this row.

## Phase 1: Structural Validation
- Precheck: reviewable; five fields on all 108 rows.
- Code checks (lint): R1 `count_claim`/`count_bundle` (R1 is the Register spot-check group's one volume row, exempt; COUNT search found no 83rd session); R107/R108 `raw_user_id` (both titles accept Brian by name; VALUE search ACCEPTED); R108 `absence_acceptance` ("even without naming the tutorial and level order separately" only relaxes wording inside an affirmative stop message, not an absence; no finding).
- Category distribution: Outcome 108, Process 0 (no ordering the final state can't show).
- Requirement coverage: 108 of 108 required outcomes.

## Phase 2: Per-Rubric Quality (target rows)
| Row | Issue | Type | Severity |
|---|---|---|---|
| R21 | 10.5% backer list rejects Robert's "mature cohorts" wording | overly_specific | Major |

Checked and clean:
- **R25–R104 (80 ticket close-outs):** every Done/Canceled state matches the log note ("counted goes to Done, not counted goes to Canceled") and the verified counted set: 43 Done, 37 Canceled. Every cited notes doc, build, relation, contact job, phone comment, Slack ts and Gmail id was matched to the injected record for that ticket.
- **R10, R11 (Owen's Sep 28 sessions):** now one destination (the added Register row) plus one fact (counted). The audience/stars coupling from last run is gone because no sibling row grades those cells.
- **R17, R18, R19, R22, R23, R24 (memo):** casual 103.5/27 = 3.833, RPG 63/18 = 3.5, gap 0.333, counts 27 and 18 all recomputed from the tickets plus Owen's mail; R17 now rejects a memo that offers casual lead and another call as alternatives.
- **R106, R108:** affirmative hold / stop wording, destination named.

Atomicity: every target row grades one result. Over-specificity: R21 overly_specific; all others valid.

## Phase 3: Set-Level Quality
- Coverage: all five writes the prompt asks for have rows: Register (volume row R1 plus 5 verdict and 5 reason samples, one audience and one stars sample, Owen's two sessions direct), memo (R16–R24), 80 ticket close-outs (one row each), thread reply (R105–R106), Brian (R107–R108).
- Duplicates / overlap / cascade: none. The R1/R19/R21 cascade group from last run is gone.
- Spot-check groups: verdict 5 (R2, R5, R7, R12, R13), reason 5 (R3, R4, R6, R8, R9), audience 1 (R14), stars 1 (R15); R1 volume.
- Weights: all match their work kind (multi-source joins 5; R14, R15, R16, R105, R107 lookups 1).

## Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 1 (R21) | 0.9% | any | FAIL |
| Moderate | 0 | 0% | any | — |
| Minor | 0 | 0% | ≥ 5% | — |

## Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 2 | One Major (R21) on 1 of 108 rows; any Major fails |
| Criteria Weights | 5 | Every weight matches its work kind |
| Rubric Category Balance | 5 | 108 Outcome rows |
| Process Rubrics | 5 | No Process row needed |
| Agent-Centric Phrasing | 5 | Every title opens with "The Agent" and names no tool |
| Negative Criteria | 5 | No prohibition or do-nothing row |
| Predicted All-Fail gate | PASS | No row predicted to fail every run |

**Lowest Sub-Dimension:** Overall Rubric Quality - 2 - R21's backer list rejects a correct 10.5% in Robert's wording.
**Summary:** The rewrite fixed every structural problem from last run: no count bundles, one row per ticket, Owen's rows unbundled, memo figures widened, Brian's id in the titles, weights corrected. All facts check out. One wording narrowing in R21 is the only defect.

## Changes Since Last Run
- Rows: 108 (11 locked, 2 locked-checked-fix, 20 edited, 74 new, 1 re-checked; 8 previous rows removed).
- Previous findings now fixed: count bundles (old R2, R3, R4, R7, R9 and the old R19/R21 Register totals, R29–R31) removed; 75 missing ticket close-outs added (all 80 tickets now have a row); R15/R16 rewritten as R10/R11 (verdict only); R17/R18/R27/R36 weights now 5 (R12, R13, R20 and the ticket rows); memo call widened and tightened (R17); 3.83, 3.5 and 10.47%/10.59% renderings accepted (R18, R19, R21); memo counts and gap added (R22–R24); Brian's Slack id now in R107/R108; R1's cascade group gone.
- Dismissals: none recorded.
- New scored finding: R21 overly_specific (Major), from your rewrite of checked fix 9.

### Notes for QM (not scored)
- R24's title does not say which side the 0.33 gap favours; a run that misses both the Kadıköy and coaching exclusions but finds Owen's mail gets RPG 4.163 against casual 3.833, also 0.33. Two independent trap misses plus an exact numeric coincidence, so treated as very unlikely; adding "(casual ahead)" would close it.
- R22/R23: a run that skips the Contacts job lookup and misses Owen's late mail also lands on 27 casual / 18 RPG. Two independent misses (recorded as very unlikely last run too); R18/R19 catch those runs.
- OE 39 also lists 82 / 45 / 37 session totals for the memo; no row grades them (your call, as last run).
- R17's justification says "missing any one block flips" the call; true per exclusion class or source, not per single player (missing only ZOM-598 or only ZOM-622 leaves a 0.25+ gap). Wording only.

### Rejected findings
- R7-DR1/DR2 (R10/R11 "adds a row … and marks it counted" not atomic): Eval 3 §2.2 decision rule, "The destination of one write plus one fact it must state → one result." The added row is the destination, counted the one fact; the verdict cannot exist without the row.
- R3-DR1/DR2 (re-run notes on the 13 dev-build drops; tickets for Owen's two sessions): prompt-incorporation-v1, settled in your /prompt report: Robert's DM and the late-form ticket step are not incorporated, so "the OEs and rubric must not require them". Not a fork: the tickets' close-out state is settled by the log note.
- R5-DR1 (R24 gap direction), R5-DR2/DR3 (R22/R23 count coincidences): deep_recheck R5, "Do not flag a wrong answer that is very unlikely"; each needs two independent trap misses. Moved to Notes for QM.
- R1-DR2/DR3 (R18's 3.8 and R24's 0.3 accepted only with a backer): bare 3.8 also matches 3.79 (Owen's mail missed) and bare 0.3 matches 0.254/0.268 (one contacts exclusion missed), both plausible single misses; rubric_flow_v2's opposite-pair rule ("the fix must satisfy both at once") is met by the backer condition, which is the checked fix from last run.
- R2-DR1 (R17 justification "missing any one block flips it"): the justification says "block", and every exclusion block or source does flip the call by the pass's own numbers; kept as a wording note.

### Recommended Fixes
- Fix 1 (R21): revised after check; needs your own rewrite. Round 1 (backer "mature cohorts (cohorts with a D14 figure)"): fixcheck and lint clean; R4, R7 clean; R6, R2, R3 found the bracket ambiguous and the evidence stale; R1 found the backer still required install weighting; R5 found a D7-filter run calling its cohorts "mature" now passed. Round 2 ("mature cohorts or cohorts with a D14 figure … unless the memo filters cohorts on D7"): R2–R5, R7 clean; R1 and R6 found the D7 clause also fails a correct memo with both D7 and D14 figures. Round 3 ("fails beside a stated D7 filter used instead of D14"): R2, R4, R6, R7 clean; R1 found it could catch a D7 description of the KPI sheet's 10.6%; R5 found a D7-filter run that never names its filter but lists its own numbers still passed; R3's mislabelled-filter case rejected (that memo states a wrong method). Round 4 (restructure, exception tied to the mature/D14 backer and the D7 path's own numbers): R3, R4, R7 clean; R6 found the new "beside" wording disagrees with the evidence's "anywhere in the memo"; R5 found the D7-set list left out 9 weeks, about 2,800 installs and 296 retained; R1 found the window backers tied only to "from 2025-07-28"; R2 clean apart from PLATFORM:FD-3785.

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7, Opus 5.5 (claude-opus-5-5), each blind to the main review, on the 95 target rows (R4 against all rows). DELTA run: F2/F3 do not run.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 95 | 3 | 1 |
| R2 | 95 | 1 | 0 |
| R3 | 108 | 2 | 0 |
| R4 | 95 | 0 | 0 |
| R5 | 89 | 3 | 0 |
| R6 | 95 | 0 | 0 |
| R7 | 95 | 2 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R1 | R21 "10.5% passes when the memo also states install weighting over cohorts with a D14 figure" | C090N54TG79/1759167008.881274 "Mature cohorts only, meaning cohorts that have a D14 figure" | Overly specific | overly_specific | CONFIRMED | Robert's own term is not on the backer list; the checked fix had it |
| DR2 | R1 | R18 "3.8 passes only when the memo also states … 27 … or … 103.5" | Tickets + Owen's mail, 103.5/27 | Overly specific | overly_specific | REJECTED | Opposite-pair: bare 3.8 matches 3.79 (Owen missed) |
| DR3 | R1 | R24 "0.3 passes only when …" | Same | Overly specific | overly_specific | REJECTED | Bare 0.3 matches 0.254/0.268 single-miss paths |
| DR1 | R2 | R17 justification "missing any one block flips it" | Contacts 038b5eb5…, 0810fb82…; deck "A gap under 0.25" | Incorrect | incorrect | REJECTED | True per block; wording note |
| DR1 | R3 | Re-run notes on ZOM-577–586, 632, 637, 645 | D05GU6L0XFH/1758913471.205816 "put a re-run note on it" | Coverage | missing_coverage | REJECTED | Not incorporated (prompt-incorporation-v1, /prompt report) |
| DR2 | R3 | Tickets for Owen's two sessions | Log note "gets a ticket and a log row" | Coverage | missing_coverage | REJECTED | Not incorporated |
| DR1 | R5 | R24 "as 0.33" | Kadıköy + Claire stars | Overly broad | overly_broad | REJECTED | Two independent misses; Notes for QM |
| DR2-3 | R5 | R22 "27 casual", R23 "18 RPG" | Contacts 0810fb82…, 038b5eb5…; Owen's mail | Overly broad | overly_broad | REJECTED | Two independent misses; Notes for QM |
| DR1-2 | R7 | R10/R11 "adds a row … and marks it counted" | Owen's mail; contacts | Atomic | non_atomic | REJECTED | Destination plus one fact (Eval 3 §2.2) |

Fix-check: R21's fix ran 4 rounds (3 plus 1 after a restructure) with lint, the title cap and all seven passes each round; it did not come back clean, so it is marked "needs your own rewrite" (see Recommended Fixes).

Effect on verdict: FAIL. The confirmed R1-DR1 finding was added to the scoring record before it was saved: Overall Quality 2, all other dimensions 5.

Platform defects: PLATFORM:FD-3785 (USER_COHORT_RETENTION's 2025-09-15 D14 and 2025-09-22 D7 cells are filled before their windows close). R21 follows Robert's literal "cohorts that have a D14 figure" rule and accepts both 10.47% and 10.59%, so it has no effect on the score.

### FINAL VERDICT: FAIL
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Score: 2
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 08cb9d32477be77fe84977eb26a9082ac543aa96f29866b1198072206ab20338
Review context SHA-256: 2937e0e870b32c0108a39ff844a29ee846a3a6247859f13f6b80170b24891404
Scoring record SHA-256: 29fa692d9b8f3f7d6f581f3fdd0aa810d12d593508fe9d479ac1ad9cafa29a8f
Eval version: task-quality-v1
Eval release SHA-256: 95724d0c10e93f280590a039482b3866a70e2d40ada2c074afcdbdb043725f9e
Gate tier: localized
Coverage ratio: 108/108
Repairs: R21
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Next action: Rewrite R21 yourself following the Fix List, update the rubric in your Outlier task, and send /rubric again
Evidence limits: Static universe plus the injection SQL overlay (not executed); USER_COHORT_RETENTION read through the registered extract, not loaded whole.

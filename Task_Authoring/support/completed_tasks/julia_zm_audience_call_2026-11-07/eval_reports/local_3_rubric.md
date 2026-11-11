## RUBRIC EVALUATION REPORT

### Task: Julia Lawson, ZM friend-session audience call (Register, memo, ticket close-out, reply to Leonard, note to Brian)
### Persona: Julia Lawson - Product Manager
### Total Rubrics: 108 (Outcome: 108, Process: 0)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Run mode: DELTA (run 22). Locked: 104 rows plus R20 (a copied checked fix). Target rows: R10, R11, R21 (the run-21 fixes, marked revised after check). Rules: local release ccaebe69 with the portal-parity rules (portal-v95724d0c).
Inputs: rubric `Evals/task_inputs/09_Rubrics.json` (7cef2632...), prompt c3da944d, SQL rev9 3a98aa36, OE rev4 7f0aa81e.

## Fix List

No scored findings; nothing to fix. Optional wording points are under Notes for QM.

---

### Phase 1-3 summary
- Five fields 108/108; all Outcome; lint: R1 count_bundle exempt (the one Register volume row), R108 absence_acceptance check only (relaxes wording inside an affirmative stop message; no finding). Longest title R21, 110 words.
- Coverage 108/108 (R3 none): one row per ticket for all 80 close-outs (43 Done, 37 Canceled); Register volume row, 5 verdict and 5 reason samples, Owen's two late sessions direct; every memo number behind the call; reply and Brian rows.
- Target rows: R1 none (no valid answer fails), R2 none (every figure in R21 recomputed; Owen's mail and contacts match R10/R11), R3 none, R4 none confirmed, R5 none confirmed, R6 none confirmed, R7 none.
- Fact review: every title number, date and id bound to the reviewer extract with no mismatch.
- Final-reply test ACCEPT; predicted all-fail none; OE cross-check: every row maps.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 0 | 0% | any | PASS |
| Moderate | 0 | 0% | any | PASS |
| Minor | 0 | 0% | >= 5% | PASS |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 5 | No open defect after the deep recheck |
| Criteria Weights | 5 | 103 multi-source rows at 5, 5 single-service lookups at 1 |
| Rubric Category Balance | 5 | 108 Outcome rows |
| Process Rubrics | 5 | None needed |
| Agent-Centric Phrasing | 5 | All "The Agent ..."; no tool names |
| Negative Criteria | 5 | No prohibition; every row fails an idle Agent |
| Predicted All-Fail gate | PASS | None |

**Lowest Sub-Dimension:** none below 5.
**Summary:** The run-21 fixes hold: R10/R11 now find Owen Baker's added Register row by the same rule in title and evidence, and R21's recorded paths are correct. Every pass is clean on the target rows; the locked rows carry their run-21 clean results.

## Changes Since Last Run
- Rows: 104 locked, 1 locked-checked-fix (R20), 3 edited (R10, R11, R21), 0 new, 0 re-checked, 0 removed.
- Previous findings now fixed: R10, R11 not_self_contained (locator in the title, row by row); R20 overly_specific (open list); R21 evidence path wording.
- Dismissals: none recorded.
- New scored findings: none.

### Notes for QM (not scored)
- R10/R11: the title says "a new ticket of hers/his", the evidence "a new ZOM ticket"; the two differ only for a ticket created outside the ZOM team that also carries the wrong audience and stars (two misses). Adding "ZOM" to the titles would align the wording.
- R10/R11: one merged added row holding both of Owen's sessions ("casual / RPG", "5 / 1.5") would pass both rows; it goes against the Register's "one row per session" header and Owen's numbered list (very unlikely). Requiring one audience in the fallback would close it.
- R21: the D7-filter path (10.5142%) and the KPI path from the 2025-07-21 week (10.5454%) pass as 10.5% with "mature cohorts" or the row/week counts. Both are recorded as accepted wrong paths: the portal's run-2 Fix List required these backers and accepted this breadth, and blocking them fails a correct 10.5% in Robert's words. The two-miss path (D7 filter plus the 2025-07-21 week, 10.4845%) is very unlikely.
- R107 passes a message to Brian that gives a go-ahead; it is the write row and R108 its content row (Eval 3 §3.3).

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review, on target rows R10, R11, R21 (R3 whole rubric, R4 against all rows).

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 3 rows | 0 | 0 |
| R2 | 3 rows | 0 | 0 |
| R3 | whole rubric | 0 | 0 |
| R4 | 3 rows vs all | 1 | 0 |
| R5 | 3 rows | 4 | 0 |
| R6 | 3 rows | 2 | 0 |
| R7 | 3 rows | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| R4-DR1 | R4 | R1 "exactly 82 session rows" with R10/R11 "adds a row" | Owen's mail 1844324114366762178 | §3.3 | duplicate | REJECTED | R1 counts rows, R10/R11 grade the verdict (82 rows with Owen's rows not counted passes R1, fails both); a missed mail is a shared root cause; portal run 2 found no group |
| R5-DR1 | R5 | R21 "10.5% passes when the memo also states anywhere any one of: mature cohorts" | USER_COHORT_RETENTION d7 filter: 18 rows, 10.5142% | §2.8 | overly_broad | REJECTED | Portal run-2 Fix List required the mature-cohorts backer and accepted this breadth; opposite pair (a correct 10.5% in Robert's words must pass); recorded in evidence |
| R5-DR2 | R5 | R21 "16 cohort rows, 8 weeks" | KPI sheet from 2025-07-21: 16 rows, 10.5454% | §2.8 | overly_broad | REJECTED | Portal required start-free row/week backers; recorded in evidence |
| R5-DR3 | R5 | R21 "mature cohorts" | D7 filter from 2025-07-21: 20 rows, 10.4845% | §2.8 | overly_broad | REJECTED | Two independent misses: Notes for QM |
| R5-DR4 | R5 | R10/R11 "marked casual or 5 stars" | Register header "one row per session" | §2.8 | overly_broad | REJECTED | Very unlikely (merged row against the header and Owen's numbered list): Notes for QM |
| R6-DR1 | R6 | R10 "a new ticket of hers" vs evidence "a new ZOM ticket of hers" | R10 fields | §2.1 | not_self_contained | REJECTED | No verdict differs without two misses (non-ZOM ticket and wrong audience and stars): Notes for QM |
| R6-DR2 | R6 | R11 same | R11 fields | §2.1 | not_self_contained | REJECTED | Same |

Effect on verdict: none; the provisional PASS 5 stands.

Platform defects: PLATFORM:FD-3785 (USER_COHORT_RETENTION 2025-09-15 D14 cells filled before the window closes; R21 accepts both fair figures, so no score effect).

### FINAL VERDICT: PASS
Score: 5
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 7cef263232d2159ef0c162593a97b2c63d7f7d1686fb6d4e5e1055b22adeed47
Review context SHA-256: 4b85dbfbda3e77e8417682341414ad09d857504e5b06b64bb42e5c128d3a58ef
Scoring record SHA-256: 8137da06254dd2d0d1df89508c1e280257d6f9f79a02e7d8df2aed7968ce2a9b
Eval version: task-quality-v1
Eval release SHA-256: ccaebe69c370fb8a5aaebf9ffff2c0b60933e4d97e3e4de4c003850d1cf033df
Gate tier: none
Coverage ratio: 108/108
Repairs: None
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Evaluator model: Opus 5.5 (claude-opus-5-5)
Next action: Upload 09_Rubrics.json to the portal and run /rubric there
Evidence limits: None

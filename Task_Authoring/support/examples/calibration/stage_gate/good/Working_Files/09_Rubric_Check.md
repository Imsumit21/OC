# 09 Rubric Check — stage-gate-fixture
Checked 2026-10-04 · Criteria 5 (builder minimum 5: ok) · Plan 2026-10-04
JSON field map: criterion=`criterion` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass
Readiness for /rubric: NON-FAIL-RISK — a prediction only; /rubric gives the verdict

## Coverage

| Plan row / requirement | Criteria | Covered / gap |
|---|---|---|
| P1 | C1 | covered (omission and wrong folder rejected) |
| P2 | C2 | covered |
| P3 | C3 | covered |
| P4 | C4 | covered (Canceled tickets inside the set rejected) |
| P5 | C5 | covered (hub estimate rejected) |

Unauthorized criteria: none

## Findings

| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |
|---|---|---|---|---|---|---|---|
| 1 | C3 | "posts the schedule location in #winddown" | 3_Rubrics_Eval.md 2.7 | the # prefix is a wording preference the prompt never set; it rejects no valid answer | P3 / F1 | harmless_specificity | Minor |

## Overlap groups · Spot-check groups · Predicted all-fail

| Group / row | Members / basis | Shared condition / reason |
|---|---|---|
| none | — | no shared acceptance condition |

## Dimensions

| Dimension | Count / % | Threshold | Status |
|---|---|---|---|
| Overall Rubric Quality | 1 Minor = 20% | Minor ≥ 5% is NON-FAIL; > 20% fails | NON-FAIL-RISK |
| Criteria Weights | 0 off | ≥ 15% two-level | PASS |
| Category Balance | 5 Outcome | zero Outcome fails | PASS |
| Process Rubrics | 0 | 2+ invalid | PASS |
| Agent-Centric Phrasing | 0 | 1+ fails | PASS |
| Negative Criteria | 0 | 1+ fails | PASS |
| Predicted all-fail | 0 | 1+ fails (harness tolerance 0; /rubric fails at 2+) | PASS |

## Self-review

| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |
|---|---|---|---|---|
| C1 | clear | a wrong folder passes | the title names d_cc3e90160f490686039986 | none |
| C2 | clear | the decoy hub claim passes | the title names the 0.3.309 defect (F2) | none |
| C3 | clear | a DM passes | the title names #winddown (C0ADGSZKR3R) | none |
| C4 | clear | Canceled tickets are a valid inclusion | prompt says still open (04_Prompt.txt) | none |
| C5 | clear | the hub estimate passes | the title names the tracker total from F5 (ENG-2280), re-verified via hg.py | none |

Unresolved: none.

```
STAGE GATE rubric-check: PASS — Task_Authoring/support/local_search/cache/stage_gate_selftest/gen · 09_Rubric_Check.md#6c86c1af6201 · 09_Rubrics.json#6784183f92d6 · blocking 0 · warnings 0 · checks 17
[PASS] structure.outputs: 1 output(s) present: 09_Rubric_Check.md
[PASS] structure.inputs: 2 input(s) present: 09_Rubrics.json, 09_Rubric_Writing_Plan.md
[PASS] structure.fresh: every output newer than its inputs (09_Rubrics.json, 09_Rubric_Writing_Plan.md)
[PASS] chain.rubric-writing: upstream 'rubric-writing' PASS pasted and current (09_Rubric_Writing_Plan.md#1685f5279950)
[PASS] structure.sections: 5 required sections present and non-empty (09_Rubric_Check.md)
[PASS] structure.placeholders: no placeholders in 09_Rubric_Check.md
[PASS] structure.criteria_count: header Criteria 5 vs 09_Rubrics.json 5
[PASS] evidence.quoted_spans: 1 quoted span(s) verified as exact substrings of 09_Rubrics.json
[PASS] structure.issue_types: every finding uses a /rubric issue type
[PASS] structure.dimensions: dimension table has 7/7+ rows
[PASS] structure.readiness: readiness line present
[PASS] validity.rubric: binary validity gate clean: no incorrect, unauthorized, unobservable, contradictory, uncovered or predicted all-fail item
[PASS] boundary.replacement+criterion+prompt_phrases: human-only boundary clean in 09_Rubric_Check.md (replacement, criterion, prompt_phrases)
[PASS] review.counter_readings: 5 evidenced counter-readings (of 5 found; need ≥ 5) in 09_Rubric_Check.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```








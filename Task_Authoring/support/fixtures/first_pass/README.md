# First-pass backtest fixtures (plan section 5, item 2)

Cases the first-pass checks were backtested on, kept so a later change to a check can be re-scored on the same cases.
Paths inside each case are relative to `Task_Authoring/support/completed_tasks/<task>/task_inputs/`.

| File | What it is | Re-run |
|---|---|---|
| `path_exposure_cases.json` | 108 deciding records from 10 archived tasks, each labelled by whether the platform runs opened it (≥ 0.8 of runs leaked, ≤ 0.2 landed, otherwise mixed), with the evidence for the label | `python3 -B Task_Authoring/tools/path_exposure.py backtest --units Task_Authoring/support/fixtures/first_pass/path_exposure_cases.json` |
| `path_exposure_backtest_2026-11-11.md` | The result on 2026-11-11: path_exposure against `hardness_v2_check` and `trap_liveness`, per case | — |

Other first-pass backtests read the archives directly and live in the tools' own tests:
`tools/test_platform_delta_lint.py` (no false alarm on platform-passed rubrics while the rule was in force),
`tools/test_first_pass_controls.py` (C4 clean on every archived prompt check), `tools/test_assignment_fit.py`
(the four plan outcomes; set `ASSIGNMENT_FIT_REAL=1`), `tools/test_carrier_backfill.py` (the stored find-rate table
rebuilds to the same bytes), `tools/test_difficulty_budget.py` and `tools/test_rubric_skeleton.py`.

The carrier units behind `references/carrier_find_rates.json` are in `references/carrier_backfill_units.json`.

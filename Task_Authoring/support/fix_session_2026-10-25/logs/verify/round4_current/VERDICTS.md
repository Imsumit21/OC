# Final verification of the P1 tree (2026-10-29): 8 tiers on this exact tree

Tree: the working tree after the last edit (`tools/surface_grader.py` long-bullet declaration; `tools/node_verdicts.py`
declared-count reconciliation + no-detail case; `tools/hardness_forecast.py` raw landing-pair counters; `scripts/
f1_protocol.py` raw-counter f9 + canonical pooled SE/budget revalidation). Bundles rebuilt from this tree by
`build_verify_diffs.py` + `build_verify_bundles.py`; artifacts by `build_round4_artifacts.py`.

| Bundle | Tier | Verdict | Verified by | Review |
|---|---|---|---|---|
| code_g1 | code | **FAIL** | openai/gpt-6.1-sol#max | Surviving: a colon-delimited count (`Review not approved:2`) is discarded (colon excluded from the tail-count boundary); further prose shapes remain unhandled. Previous rounds' findings (multi-line groups, guards, tables, bullets, dates) are fixed. |
| code_h1 | code | **FAIL** | openai/gpt-6.1-sol#max | Surviving: a FAILED channel's declared HELD count can be satisfied by failed details (`max(observed,held)` before subtracting both populations), so a missing held decision can be attributed as known; the declared-count undo also discards held provenance and so is killed by an earlier assertion. |
| code_f1 | code | **FAIL** | openai/gpt-6.1-sol#max | Surviving: `f9` still falls back to `round(reported_probability * n)` when the raw counter is missing/malformed; scalar assertions keep unexpected cached `cells` fields; `--summarize` in place raises `SameFileError`; pooled dispatch on exact assertions can read cached fields. Raw-counter integrity and full field rebuilding are not fail-closed. |
| code_misc | code | **PASS** | openai/gpt-6.1-sol#max | V1, M5, M7, WT, E2E and the task-1 surface: no concrete defect. The round-3 contradictory finding is resolved. |
| redteam_grading | redteam | **FAIL** | openai/gpt-6.1-sol#max | Surviving: a tab-separated ATX heading (`###\t...`) is treated as a table row; an ordered-list declaration (`1. Late (1): ...`) is treated as table data; inline-code bare key lines are dropped; a two-digit year (`October 25, 26`) and a sprint number (`sprint 2`) can override the stated count. |
| redteam_attribution | redteam | **FAIL** | openai/gpt-6.1-sol#max | Surviving: failed details satisfying a declared held count; duplicate detail identities padding coverage of a different missing slot; a detail-free HELD trial reporting `deciding_model_unknown=False`. |
| redteam_forecast | redteam | **FAIL** | openai/gpt-6.1-sol#max | Surviving: partially covering briefs leave active batch members unreachable; f9 accepts contradictory raw counters and a rounded-report fallback; summary retains forged parent fields and contradictory production fields; `f7`/`f7_shared` evidence is a rounded pseudo-count. |
| methodology | methodology | **FAIL** (fallback: anthropic hold timeout) | openai/gpt-6.1-sol#max | The scoped fixture result is credible (m=39, z=3.6558, analytic variances, post-hoc correction disclosed), but the claims that acceptance is rebuilt from sufficient raw statistics and is fail-closed are stronger than the code (f7/f7_shared pseudo-counts, f9 fallback, cached parent fields). |

**P1 is NOT closed.** Every FAIL is a concrete finding on this tree; none is a credentials/hold UNKNOWN.

## Local acceptance on this same tree (all PASS)
- suite 14/14, shared-cache fingerprint 0 differences, linked folders unchanged (`logs/p1_suite_round16.log`).
- E2E 14/14 (`logs/e2e/e2e_round22.log`).
- falsify_g1 PASS (`logs/g1/falsify_g1.round16.txt`), falsify_h1 PASS with 40+ isolated undos
  (`logs/h1/falsify_h1.round39.txt`), protocol self-test and falsify runner self-test PASS.
- rev13 reproduction 0 differences in both views (`logs/final4/rev13_truth.txt`, `rev13_solver.txt`); rev14 failed
  sets exactly of record (`logs/final4/rev14_grades.txt`).
- c05: 0 item differences, exactly the 2 documented landed-key seed differences (`logs/final4/c05.txt`).
- V1 PASS; priors unchanged (A17 Beta(2.5705,2.8544), A15 Beta(2.1429,3.1714)/Beta(2.7143,2.6),
  A7 Beta(1.4524,2.2381)); `references/mechanism_priors.json` untouched.
- Task 1 `surface.gradeable`: PASS, 30/30 (`logs/final4/task1_surface_gradeable.txt`).
- F1 protocol: 12/13 ids PASS at seeds 1/2/3 at 20,000 draws (36/36 seed-level tests), f6 ABSENT by design,
  `production_path_ok=true`, `acceptance_complete=true` (`logs/f1/protocol4/seed{1,2,3}/result.json`,
  `f1_acceptance/summary.json`); `--summarize` rebuilds every assertion from sufficient statistics under the current
  gate (targets, analytic variances, budgets) and re-derives the three production checks.
- Frozen rev13/rev14 SHA256SUMS verified before and after every run; shared-cache fingerprint 0 differences.

## What this means
The grader, attribution, forecast and F1-protocol rows are substantially hardened (each fix carries a planted case
and a falsification undo; no real grade moved). They have not reached an independent PASS: the residual findings above
are real, and the F1 claim must be weakened (or the remaining raw-statistics/field-rebuild gaps closed) before a PASS
can be claimed. The honest F1 status is **engine implemented; acceptance complete for the 12 executable ids
(f6 chain ABSENT and unvalidated); replay FAIL withdrawn; no calibration** — a scoped implementation-consistency
result, not predictive validation.

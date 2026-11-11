# Gates, miss rates and odds: SQL rev7, baseline batch 2 (2026-11-10)

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Universe manifest: `Evals/references/universes/normal/universe_manifest.json`.

## 1. What was graded

- Six exports in `07_Baseline_Trajectories/` (sha256 2a1f55cb, 51ac633c, c75ecefb, 3d8d7793, 51c7ddfc, 7c7de591), all
  bound to rev7 (`40f90385e31e`) by discriminating content, all `claude-opus-5-5`, all completed (`../summary.json`).
- Verifier copy `10_Baseline_Verifier_Results.md` (sha256 62e1a5af… by the stage gate's digest), 73 rows per run, graded on
  `09_Rubrics.json` 923f89f3ac9c (73 rows, weight 165).
- Each verifier `Run #N` block names the spreadsheet its run created; that id occurs in exactly one export
  (`../verifier_binding.json`, verdict BOUND). Run #N is export run-N for all six.

## 2. Gates on the verifier results

Computed by `difficulty_stats.py` on the bound verifier results (see section 6 for a tool fix made on the way);
output in `../difficulty_stats.txt`, matrix in `../matrix.json`.

| Run | Counted calls | Weighted pass | Failed rows |
|---|---|---|---|
| run-1 | 125 | 87.3% | R7, R25, R32, R58, R68 |
| run-2 | 125 | 80.6% | R7, R8, R25, R32, R33, R58, R68, R69 |
| run-3 | 123 | 87.3% | R8, R25, R33, R58, R69 |
| run-4 | 116 | 87.3% | R8, R25, R33, R58, R69 |
| run-5 | 132 | 84.2% | R8, R12, R25, R33, R58, R69 |
| run-6 | 140 | 87.3% | R8, R25, R33, R58, R69 |

| Gate | Value | Rule | Verdict |
|---|---|---|---|
| Errored runs | 0 of 6 | at most 2 | PASS |
| Full passes | 0 of 6 | fewer than 5 | PASS |
| Average weighted pass | 85.7% | Easy: under 90% | PASS |
| Spread (population SD) | 0.025 | 0.1 to 0.3 | **FAIL** |
| Failure patterns | 3 patterns; largest 4 of 6 failing runs (67%) | at least 2; largest at most 50% | **FAIL** |
| Horizon | mean 127 counted calls | Long Horizon, at least 100 | PASS |
| Model | all six Opus 5.5 | Opus 5.5 | PASS |

Patterns (same pattern unless two runs differ on two or more rows): {run-3, run-4, run-5, run-6}, {run-1}, {run-2}.
Run-5 differs from runs 3, 4 and 6 on one row only (R12), so it joins them. All-fail rows: R25 and R58.

## 3. The rows behind each decision

| Decision | Rows it flips on its own | Weight | Shared rows |
|---|---|---|---|
| OFF (Lucas, Western Union) | R8, R33, R69 | 11 | R25, R58 (10) |
| RET (MotMot, returned wire) | R7, R32, R68 | 11 | R25, R58 (10) |
| CORR (JPMorgan, own account) | R9, R10, R34, R70 | 16 | R25, R58 when the 4,000 lands in Build |
| ORPH (Leapblock close-out) | R6, R31, R67 | 11 | R25, R58 |
| ALIAS (Node Media bucket) | R12 | 5 | none when the wrong bucket is Company |
| OLEG | R11, R35, R71 | 7 | R25, R58 when 125 lands in Build (it is Marketing) |

The Domino Delights total on the sheet (R25) and in the reply (R58) fail whenever any Domino Delights build figure
is wrong. Every run missed OFF or RET, so both rows failed six times. A run that misses only OFF and a run that
misses only RET lose the same 21 points and score the same 87.3%.

Worst reachable score with every decision above missed: 1 − 71/165 = 57.0%. With the two decisions that carried
this batch (OFF, RET) and ALIAS: 1 − 37/165 = 77.6%. The largest spread a batch can show between 77.6% and 100% is
0.112 (three runs at each end), so the spread band is out of reach for these runs' failure modes.

## 4. Miss rates on rev7 (13 runs)

Batch 1 was the first six-run baseline on rev7 (2026-11-09). Its exports and verifier copy were replaced by batch 2;
its tool ledgers and decoded writes are kept in `../../../baseline_rev7/r1..r6/` with each export's sha256. The table
is a hand reading of those sheet writes (`r*/writes.json`), not a verifier result. The pre-check is the rev7 run the
platform /hardness report scored 3 (`plateform_reports/6aeed82596dcfe103f9f74d9_1a_hardness-5.md`, export sha256 d5db6810).

| Run | RET (MotMot DD) | OFF (Lucas DD) | CORR (JPMorgan) | ALIAS (Node Media) | ORPH |
|---|---|---|---|---|---|
| batch 1 r1 | 28,128 right | 6,450 missed | 0 right | Marketing right | right |
| batch 1 r2 | right | missed | right | Company missed | right |
| batch 1 r3 | right | missed | right | right | right |
| batch 1 r4 | 32,160 missed | 13,975 right | 4,000 in Build missed | Company missed | right |
| batch 1 r5 | right | 13,975 right | right | Company missed | right |
| batch 1 r6 | right | missed | right | right | right |
| pre-check | right | missed | right | right | right |
| batch 2 run-1 | 32,160 missed | 13,975 right | right | right | right |
| batch 2 run-2 | missed | missed | right | right | right |
| batch 2 run-3 | right | missed | right | right | right |
| batch 2 run-4 | right | missed | right | right | right |
| batch 2 run-5 | right | missed | right | Company missed | right |
| batch 2 run-6 | right | missed | right | right | right |
| **Missed** | **3 of 13 (23%)** | **10 of 13 (77%)** | **1 of 13 (8%)** | **4 of 13 (31%)** | **0 of 13** |

Batch 1 by the same pattern rule: {r1, r2, r3, r6} miss OFF (r2 also the one ALIAS row), r4 and r5 stand alone.
Largest pattern 4 of 6 again. Both batches fail the pattern rule the same way.

Three runs found the Western Union receipts (batch 1 r4, r5; batch 2 run-1). Two of those three missed the MotMot
return, against one of the ten that did not find them. Thirteen runs are too few to call that a dependence.

## 5. Odds for a fresh batch (advisory, UNCALIBRATED)

`gate_odds.py` in this folder, 200,000 simulated batches per line, independent misses at the stated rates.

| Case | Pattern rule | Average under 90% | Pattern, average and full-pass gates together | Spread 0.1 to 0.3 |
|---|---|---|---|---|
| Observed rates, rubric as is | 35% | 89% | 32% | 1.5% |
| Observed rates, Node Media line graded on two cells | 68% | 92% | 65% | 2.6% |
| CORR missed 40%, others observed | 73% | 98% | 72% | 6.4% |
| CORR missed 40% and Node Media on two cells | 90% | 99% | 89% | 8.6% |
| OFF missed 50%, others observed | 58% | 56% | 34% | 3.4% |
| RET missed 50%, others observed | 60% | 98% | 59% | 1.8% |

Readings:
- Re-running rev7 unchanged clears the pattern rule about one batch in three. Two batches have now failed it.
- Making OFF easier to find helps the pattern rule and pushes the average to the cap: at a 50% miss rate the
  average clears 90% in about half the batches.
- The lever is a second and third decision that are missed often enough, on rows of their own. CORR owns the
  most weight (16) and is missed 8% of the time. ALIAS is missed 31% of the time and owns one row.
- No case reaches the spread band.

## 6. Tool defect met on the way, and its fix

`difficulty_stats.py --build` first refused the verifier copy: 23 of the 73 titles carry the platform's escaped
brackets (`\[PERSON_NAME_36400\]`) and `norm_title` did not strip them, so those rows did not bind to
`09_Rubrics.json` (the same defect is recorded in `learnings` sections 62 and 69). The numbers were first computed
with that one normalisation patched in memory. The user then approved the fix on 2026-11-10: `norm_title` now strips
`\[` and `\]` (two added lines in `Task_Authoring/tools/difficulty_stats.py`). The tool's self-test and the 21 unit
tests in `test_difficulty_v3` and `test_mode_b_report` pass, all 73 rows bind, each run's header count matches its
rows, and the rebuilt matrix and gate table are identical to the in-memory run.

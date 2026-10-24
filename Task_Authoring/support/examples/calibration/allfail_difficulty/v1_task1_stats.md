| Rollout | Counted tool calls | Raw / harness / blocked / repeats | Weighted pass (platform) | Failed rubrics (platform) |
|---|---|---|---|---|
| run-1 | 390 | 406 / 15 / 0 / 1 | 60.0% | R5, R6, R7, R8, R9, R10, R16, R34, R35, R36, R37, R44 |
| run-2 | 446 | 487 / 21 / 1 / 19 | 50.0% | R5, R6, R7, R8, R9, R10, R16, R21, R22, R23, R24, R25, R26, R31, R44 |
| run-3 | 325 | 348 / 19 / 0 / 4 | 76.7% | R5, R21, R34, R35, R36, R37, R44 |
| run-4 | 596 | 624 / 25 / 1 / 2 | 30.0% | R3, R5, R6, R7, R8, R9, R10, R16, R21, R22, R23, R24, R25, R26, R33, R34, R35, R36, R37, R44, R47 |
| run-5 | 330 | 347 / 16 / 0 / 1 | 86.7% | R34, R35, R36, R37 |
| run-6 | 379 | 412 / 28 / 2 / 3 | 46.7% | R6, R7, R8, R9, R10, R22, R23, R24, R25, R26, R31, R34, R35, R36, R37, R44 |

| Gate | Value | Rule | Verdict |
|---|---|---|---|
| errored_runs | 0 errored of 6 | <= 2 errored (3+ = Fail) | PASS |
| pass_at_1 | 0/6 = 0% | <= 50% (<= 3 of 6) | PASS |
| avg_weighted_pass_rate | 58.3% | < 75% (Evals); QC Spec V2 alone < 90% | PASS |
| per_rollout_sd | 0.189 (sample 0.207; unweighted 0.114) | 0.1-0.3 (population SD of per-rollout weighted pass rates) | PASS |
| failure_patterns | 6 pattern(s); largest 17% of 6 failing (pairwise reading 17%) | >= 2 patterns (differ on >= 2 rubrics); largest <= 50% | PASS |
| horizon | average of completed rollouts: 411 | normal tier 50-100 | NON-FAIL (Borderline Horizon — above the tier) |

Failure patterns (single-linkage, same pattern if they differ on <= 1 rubric):
- Pattern 1: run-1
- Pattern 2: run-2
- Pattern 3: run-3
- Pattern 4: run-4
- Pattern 5: run-5
- Pattern 6: run-6
- Pairwise reading (largest set all within 1 rubric of each other): run-1
All-fail rubrics (completed rollouts, platform view): none
Blocking gates: none

# 01c Preflight Report — PASS

Revision r1; SQL `07dc66233f21`, solver `b7821de8e59b`, surface `4d64882efe5f`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 2/2 recorded | yes |
| Geometry U (S5b′) | V2 U 0.750 PASS | yes |
| Geometry margin L_max | {'V2': 'OK'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | not run | no |

## Mutants
- `rule:stale_count` KILLED (flipped weight 3) — live: KILLED: ablating the rule flips S1 (weight 3, direct)
- `intervention:rule:stale_count` load-bearing — live: removing the hub post changes only the defect-list row, inside the node's closure

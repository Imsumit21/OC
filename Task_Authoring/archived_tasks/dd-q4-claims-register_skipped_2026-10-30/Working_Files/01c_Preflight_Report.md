# 01c Preflight Report — PASS

Revision r1; SQL `bc3abbdfb1d8`, solver `880e65cd119b`, surface `ed7f0476e12c`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 34/34 recorded | yes |
| Geometry U (S5b′) | V3 U 0.851 UNVERIFIED | yes |
| Geometry margin L_max | {'V3': 'OK'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:M1_status` KILLED (flipped weight 42) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `rule:M2_flag` KILLED (flipped weight 19) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `rule:M3_live_standard` KILLED (flipped weight 8) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `rule:M4_wording` KILLED (flipped weight 20) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `rule:M5_scope` KILLED (flipped weight 7) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `rule:M6_conflict` KILLED (flipped weight 10) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `rule:M7_counts` KILLED (flipped weight 12) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `degrade:over:all-not-live` KILLED (flipped weight 37) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `degrade:over:all-testing` KILLED (flipped weight 26) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `degrade:over:engineering-page-rejects` WEAK (flipped weight 3) — weak-accepted: the over-application is a control trial and flips only the LIVE aggregate; accepted as a weak control, not a separate loss channel
- `degrade:over:all-in-testing` KILLED (flipped weight 6) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `degrade:over:all-out-of-scope` KILLED (flipped weight 40) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `degrade:over:all-conflict` KILLED (flipped weight 5) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `degrade:over:count-runs` KILLED (flipped weight 6) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `degrade:slip:claims` KILLED (flipped weight 27) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `degrade:skip:pr` KILLED (flipped weight 19) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `degrade:skip:scope` KILLED (flipped weight 7) — live: the ablation flips a weighted direct slot; the mechanism is load-bearing
- `intervention:rule:M1_status` load-bearing — live: removing the node's deciding record changes the solver output; the node is load-bearing
- `intervention:rule:M2_flag` load-bearing — live: removing the node's deciding record changes the solver output; the node is load-bearing
- `intervention:rule:M3_live_standard` load-bearing — live: removing the node's deciding record changes the solver output; the node is load-bearing
- `intervention:rule:M4_wording` load-bearing — live: removing the node's deciding record changes the solver output; the node is load-bearing
- `intervention:rule:M5_scope` no-injected-records — solver-gap: C11's deciding record is a base Confluence page, so the intervention has no injected record to remove; the rule is still live in the mutation table
- `intervention:rule:M6_conflict` load-bearing — live: removing the node's deciding record changes the solver output; the node is load-bearing
- `intervention:rule:M7_counts` load-bearing — live: removing the node's deciding record changes the solver output; the node is load-bearing
- `intervention:degrade:over:all-not-live` no-injected-records — solver-gap: the operator is solver-internal; the intervention has no injected record to remove, so it is not a record-liveness test
- `intervention:degrade:over:all-testing` no-injected-records — solver-gap: the operator is solver-internal; the intervention has no injected record to remove, so it is not a record-liveness test
- `intervention:degrade:over:engineering-page-rejects` no-injected-records — solver-gap: the operator is solver-internal; the intervention has no injected record to remove, so it is not a record-liveness test
- `intervention:degrade:over:all-in-testing` no-injected-records — solver-gap: the operator is solver-internal; the intervention has no injected record to remove, so it is not a record-liveness test
- `intervention:degrade:over:all-out-of-scope` no-injected-records — solver-gap: the operator is solver-internal; the intervention has no injected record to remove, so it is not a record-liveness test
- `intervention:degrade:over:all-conflict` no-injected-records — solver-gap: the operator is solver-internal; the intervention has no injected record to remove, so it is not a record-liveness test
- `intervention:degrade:over:count-runs` no-injected-records — solver-gap: the operator is solver-internal; the intervention has no injected record to remove, so it is not a record-liveness test
- `intervention:degrade:slip:claims` no-injected-records — solver-gap: the operator is solver-internal; the intervention has no injected record to remove, so it is not a record-liveness test
- `intervention:degrade:skip:pr` no-injected-records — solver-gap: the operator is solver-internal; the intervention has no injected record to remove, so it is not a record-liveness test
- `intervention:degrade:skip:scope` no-injected-records — solver-gap: the operator is solver-internal; the intervention has no injected record to remove, so it is not a record-liveness test

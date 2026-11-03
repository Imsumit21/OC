# 01c Preflight Report — PASS

Revision rev1; SQL `b2bfda86002c`, solver `b3baca60e7a3`, surface `c052ab4dedcb`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 30/30 recorded | yes |
| Geometry U (S5b′) | V3 U 0.884 PASS | yes |
| Geometry margin L_max | {'V3': 'OK'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:DONE1` KILLED (flipped weight 5) — live: flips M1 (Paul soft-circled) and the committed totals; signing-notice absence plus the nudge decide it
- `rule:INPUT` KILLED (flipped weight 5) — live: flips M3 (Anton committed); Anton's Sep 24 mail is the deciding record
- `rule:DONE2` KILLED (flipped weight 5) — live: flips AC1 (Dentsu build access); ZOM-567 comment decides it
- `rule:CORR` KILLED (flipped weight 5) — live: flips ST1 (Sciplay status); Robert's thread reply decides it
- `rule:ALIAS` KILLED (flipped weight 5) — live: flips ST2 (Hiro Capital status); Edith Vane's mail + contact decide it
- `rule:FILT` KILLED (flipped weight 10) — live: flips ST3/ST4 (Homa, Brightwater on the register)
- `rule:FOLLOW` SURVIVED (flipped weight 0) — solver-gap: the keep-warm writes are graded by write-content slots KW1/KW2 (trello_create_check_item text), which the solver does not express; the rule is load-bearing on the card comment (intervention load-bearing)
- `degrade:done1_over` KILLED (flipped weight 5) — live: control Anton: over-applying the signature test moves M3
- `degrade:input_over` KILLED (flipped weight 5) — live: control Paul: an invented revision moves M1
- `degrade:done2_over` KILLED (flipped weight 3) — live: control T-Accelerate: over-applying moves AC2
- `degrade:corr_over` KILLED (flipped weight 5) — live: control Dentsu: reading every quiet thread as passed moves AC1 (status no longer In talks)
- `degrade:alias_over` SURVIVED (flipped weight 0) — weak-accepted: control Makers Fund is not a sampled slot; over-application shows only in the volume/status counts, which are not graded per firm (sampling limit of 5)
- `degrade:filt_over` KILLED (flipped weight 3) — live: control T-Accelerate: splitting PXLite off moves AC2
- `degrade:follow_over` SURVIVED (flipped weight 0) — solver-gap: over-adding Dentsu to keep-warm shows only in the checklist writes (KW text slots), not a solver-read slot
- `degrade:filt_miss` KILLED (flipped weight 10) — live: channel degrade for Homa / Brightwater: moves ST3/ST4
- `intervention:rule:DONE1` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:INPUT` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:DONE2` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:CORR` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:ALIAS` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:FILT` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:FOLLOW` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:degrade:done1_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:input_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:done2_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:corr_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:alias_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:filt_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:follow_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:filt_miss` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove

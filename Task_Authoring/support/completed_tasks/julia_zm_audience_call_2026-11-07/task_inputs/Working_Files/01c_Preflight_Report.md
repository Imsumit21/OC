# 01c Preflight Report — PASS

Revision rev7; SQL `3a98aa36aadd`, solver `c5cb9c1fd1f2`, surface `d1ce8485d03c`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 32/32 recorded | yes |
| Geometry U (S5b′) | V3 U 0.980 PASS | yes |
| Geometry margin L_max | {'V3': 'UNSUPPORTED'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:R_K1` KILLED (flipped weight 10) — live: ablation flips the 13 sessions of Claire's gathering back to counted (S-K1a on the solver view, S-G1); the text slots it also moves (S-K1b, S-H1, S-G2, S-DEC, S-BRIAN, S-ST1, S-ST2) are not read by the tool.
- `rule:R_K3` KILLED (flipped weight 15) — live: ablation drops the 13 Samsung sessions (S-K3a, S-K3b, S-G1); two-sided in rev7: the natural reading now excludes, the matrix includes.
- `rule:R_K4` KILLED (flipped weight 10) — live: ablation flips Brian's 9 sessions back to counted (S-K4a, S-G1).
- `rule:R_K5` KILLED (flipped weight 10) — live: ablation flips the 13 build-1943 sessions back to counted (S-K5a, S-G1).
- `rule:R_G` KILLED (flipped weight 15) — live: ablation flips ZOM-598 and ZOM-622 back to counted (S-Ga, S-Gb, S-G1).
- `rule:R_T` WEAK (flipped weight 5) — weak-accepted: WEAK on the solver view: the two late sessions have no ticket key the register can be keyed on in advance, so the tool sees only S-G1; their declared slots S-Ta and S-Tb (weight 5 each, text on linear_create_issue) are write-content slots the tool does not read.
- `rule:R_F` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: moves the rerun field on 13 sessions and no solver-read slot; its only effect is the declared 3-weight text slot S-F1. Side channel, weight not raised.
- `rule:R_D` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: moves panel_mean 3.33 to 3.1; only the 3-weight text slot S-D1 reads it. Context value by design.
- `rule:R_E` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: moves retention_d7 10.47 to 9.09; only the 3-weight text slot S-E1 reads it. Context value by design.
- `degrade:over:K1_all_sessions_that_day` KILLED (flipped weight 8) — live: over-application to the other Sep 26 sessions; flips the control S-O2 and S-G1.
- `degrade:over:K3_all_android` KILLED (flipped weight 18) — live: over-application of the device gate to every non-iPhone session; flips S-O1 (ZOM-643, Pixel 8a) and S-G1; in rev7 it also flips S-K3a/S-K3b.
- `degrade:over:K4_any_group_nickname` WEAK (flipped weight 5) — weak-accepted: WEAK: moves ZOM-626/627 and only S-G1 reads them (at most 5 samples per group); the count still catches it.
- `degrade:over:K5_all_android` KILLED (flipped weight 18) — live: over-application of the store-builds clause to every Android build; flips S-O1, S-K3a, S-K3b and S-G1.
- `degrade:over:G_any_tech_job` WEAK (flipped weight 5) — weak-accepted: WEAK: moves ZOM-590 and ZOM-633 (non-games technical-sounding jobs) and only S-G1 reads them; the count catches it.
- `degrade:over:F_rerun_all_notcounted` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: re-run notes on every not-counted ticket; only the presence slot S-F1 reads the notes, by design.
- `degrade:slip:verdict` KILLED (flipped weight 46) — live: the scale channel: one wrong row moves direct verdict slots and S-G1.
- `intervention:rule:R_K1` load-bearing — live: load-bearing: removing the rule's deciding records changes only keys in its own closure.
- `intervention:rule:R_K3` escaped — live: escaped, declared coupling: the deciding set includes the gate Doc f_748d26e760e54651eaa0d8, which also carries the store-builds clause (H-GATE governs R2 and R3 in the manifest), so removing it moves the build-1943 sessions too; the matrix records alone stay in R_K3's closure.
- `intervention:rule:R_K4` load-bearing — live: load-bearing: removing the rule's deciding records changes only keys in its own closure.
- `intervention:rule:R_K5` load-bearing — live: load-bearing: removing the rule's deciding records changes only keys in its own closure.
- `intervention:rule:R_G` load-bearing — live: load-bearing: removing the rule's deciding records changes only keys in its own closure.
- `intervention:rule:R_T` load-bearing — live: load-bearing: removing the rule's deciding records changes only keys in its own closure.
- `intervention:rule:R_F` load-bearing — live: load-bearing: removing the rule's deciding records changes only keys in its own closure.
- `intervention:rule:R_D` load-bearing — live: load-bearing: removing the rule's deciding records changes only keys in its own closure.
- `intervention:rule:R_E` load-bearing — live: load-bearing: removing the rule's deciding records changes only keys in its own closure.
- `intervention:degrade:over:K1_all_sessions_that_day` no-injected-records — live: no-injected-records is expected: a degrade is a reading error, not a record; inert by design.
- `intervention:degrade:over:K3_all_android` no-injected-records — live: no-injected-records is expected: a degrade is a reading error, not a record; inert by design.
- `intervention:degrade:over:K4_any_group_nickname` no-injected-records — live: no-injected-records is expected: a degrade is a reading error, not a record; inert by design.
- `intervention:degrade:over:K5_all_android` no-injected-records — live: no-injected-records is expected: a degrade is a reading error, not a record; inert by design.
- `intervention:degrade:over:G_any_tech_job` no-injected-records — live: no-injected-records is expected: a degrade is a reading error, not a record; inert by design.
- `intervention:degrade:over:F_rerun_all_notcounted` no-injected-records — live: no-injected-records is expected: a degrade is a reading error, not a record; inert by design.
- `intervention:degrade:slip:verdict` no-injected-records — live: no-injected-records is expected: a degrade is a reading error, not a record; inert by design.

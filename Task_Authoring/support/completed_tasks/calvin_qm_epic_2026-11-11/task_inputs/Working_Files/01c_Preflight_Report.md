# 01c Preflight Report — PASS

Revision rev1; SQL `479b8441f52e`, solver `337c6a63f446`, surface `e2392bcc269e`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 48/48 recorded | yes |
| Geometry U (S5b′) | V3 U 0.893 PASS | yes |
| Geometry margin L_max | {'V3': 'OK'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:BRANCH` KILLED (flipped weight 15) — live: flips B1, B2, B3: the three ok, chat rows are Waiting on QA only because the #builds post shows #1718 was built from a feature branch and Arthur's doc counts main builds only
- `rule:INLINE` KILLED (flipped weight 15) — live: flips I1 and I4: the two rows are Waiting on a fix only through Arthur's review comments on #472 and #475
- `rule:REOPEN` KILLED (flipped weight 15) — live: flips R1: Vincent's thread reply is the only record that takes the pass off the gift row
- `rule:BACK` KILLED (flipped weight 10) — live: flips K1B: Robert's channel post is the only record that takes the pass off the Endless row
- `rule:ELSE` KILLED (flipped weight 25) — live: flips E1 and E2: Oliver's line on #473 is the only record that says the two fixes are merged
- `rule:FILT` KILLED (flipped weight 10) — live: flips F1 and F3: Marcus's DM is the only record of the icon glow report
- `rule:ALIAS` KILLED (flipped weight 10) — live: flips A1 and A2: Vincent's notes on ZOM-556 and ZOM-560 are what tie the two rows to tickets under other words
- `rule:GATE` KILLED (flipped weight 10) — live: flips G1 and G2: the changed card moves Daily Gift off the review and Level-end rewards onto it
- `degrade:branch_over` KILLED (flipped weight 10) — live: K6 and K7 read it: un-passing a row whose ok was on a main build flips a control
- `degrade:inline_over` KILLED (flipped weight 5) — live: K8 reads it: dropping #472 from the Collect & Win panel row flips a control
- `degrade:reopen_over` KILLED (flipped weight 5) — weak-accepted: no direct slot grades the two nr controls (rows 7 and 27); they are declared controls read per run by node_verdicts, and the passed count V1 moves in the writes
- `degrade:back_over` SURVIVED (flipped weight 0) — weak-accepted: no direct slot grades the two Zombie Lane ok controls; K9 (Zombie Lane is Clear) is a write_content slot that moves with them, which the mutation view cannot read
- `degrade:else_over` KILLED (flipped weight 3) — weak-accepted: K2 (weight 1) reads the pass claim animation row; the over-application also moves V2 and V3 in the reply, which the mutation view cannot read
- `degrade:filt_over` SURVIVED (flipped weight 0) — weak-accepted: the chat remark is off the list: an extra row moves V3 and V7 in the writes; no direct slot can read a row that should not exist
- `degrade:alias_over` SURVIVED (flipped weight 0) — weak-accepted: no direct slot grades the Ticket cell of rows 1 and 38; the Ticket column is sampled where the mechanism lands (A1, A2) and on K13
- `degrade:gate_over` SURVIVED (flipped weight 0) — weak-accepted: no direct slot grades the review flag of the two Win Streak and Endless controls; the review count V4 moves in the reply, which the mutation view cannot read
- `degrade:miss_branch` KILLED (flipped weight 15) — live: the channel operator gives BRANCH's members their natural reading: the same slots as the rule's own ablation, and the failure the forecast samples
- `degrade:miss_inline` KILLED (flipped weight 15) — live: the channel operator gives INLINE's members their natural reading: the same slots as the rule's own ablation, and the failure the forecast samples
- `degrade:miss_reopen` KILLED (flipped weight 15) — live: the channel operator gives REOPEN's members their natural reading: the same slots as the rule's own ablation, and the failure the forecast samples
- `degrade:miss_back` KILLED (flipped weight 10) — live: the channel operator gives BACK's members their natural reading: the same slots as the rule's own ablation, and the failure the forecast samples
- `degrade:miss_else` KILLED (flipped weight 25) — live: the channel operator gives ELSE's members their natural reading: the same slots as the rule's own ablation, and the failure the forecast samples
- `degrade:miss_filt` KILLED (flipped weight 10) — live: the channel operator gives FILT's members their natural reading: the same slots as the rule's own ablation, and the failure the forecast samples
- `degrade:miss_alias` KILLED (flipped weight 10) — live: the channel operator gives ALIAS's members their natural reading: the same slots as the rule's own ablation, and the failure the forecast samples
- `degrade:miss_gate` KILLED (flipped weight 10) — live: the channel operator gives GATE's members their natural reading: the same slots as the rule's own ablation, and the failure the forecast samples
- `intervention:rule:BRANCH` load-bearing — live: removing BRANCH's deciding record changes its members: the record is load-bearing as designed
- `intervention:rule:INLINE` load-bearing — live: removing INLINE's deciding record changes its members: the record is load-bearing as designed
- `intervention:rule:REOPEN` load-bearing — live: removing REOPEN's deciding record changes its members: the record is load-bearing as designed
- `intervention:rule:BACK` load-bearing — live: removing BACK's deciding record changes its members: the record is load-bearing as designed
- `intervention:rule:ELSE` load-bearing — live: removing ELSE's deciding record changes its members: the record is load-bearing as designed
- `intervention:rule:FILT` load-bearing — live: removing FILT's deciding record changes its members: the record is load-bearing as designed
- `intervention:rule:ALIAS` load-bearing — live: removing ALIAS's deciding record changes its members: the record is load-bearing as designed
- `intervention:rule:GATE` load-bearing — live: removing GATE's deciding record changes its members: the record is load-bearing as designed
- `intervention:degrade:branch_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:inline_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:reopen_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:back_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:else_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:filt_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:alias_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:gate_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:miss_branch` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:miss_inline` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:miss_reopen` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:miss_back` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:miss_else` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:miss_filt` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:miss_alias` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:miss_gate` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected

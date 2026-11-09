# 01c Preflight Report — PASS

Revision rev1; SQL `6d162cfd1032`, solver `a1ac742c0f47`, surface `095a6e4fc9df`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 38/38 recorded | yes |
| Geometry U (S5b′) | V3 U 0.837 PASS | yes |
| Geometry margin L_max | {'V3': 'UNSUPPORTED'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:DONE` KILLED (flipped weight 5) — live: flips X1 and with it the sheet, ticket and approval reading: Arthur's inline comment is what moves the row off Go. The client source carries the same day, so a close reader needs no comment; kept as a second route
- `rule:CORR` KILLED (flipped weight 5) — live: flips X3: the final line only exists in Leonard's note on the copy check
- `rule:DEP` KILLED (flipped weight 5) — live: flips X5: the row is a Hold only through the join of the trigger, the ask point and the reach test
- `rule:QA` KILLED (flipped weight 5) — live: flips X7: Vincent's DM reply is the only record that withdraws the iPhone pass
- `rule:PULL` KILLED (flipped weight 5) — live: flips K1: Vincent's channel post is the only record that takes his pass off Lives recharged
- `rule:ALIAS` KILLED (flipped weight 5) — live: flips X9: the row's ticket is under another name outside the parent
- `rule:FILT` KILLED (flipped weight 20) — live: flips X11, X12, X11b and X12b: all four asks sit in comments on tickets about other things
- `rule:BUILT` KILLED (flipped weight 5) — live: flips X15: the ask reads as new work until the batch is read as covering day 14. The source carries it too; the cancel mail is the ● carrier the rule reads
- `rule:FOLLOW` SURVIVED (flipped weight 0) — solver-gap: the ticket state is graded from the linear_update_issue payloads (X18, X19, X19b are write_content), which the solver's rows do not reach, so no direct slot moves; the failure is real and the intervention below shows the freeze comment is load-bearing
- `degrade:done_over` KILLED (flipped weight 4) — live: K2 reads it: over-applying the day test to Lapsed 1 day flips a control
- `degrade:corr_over` WEAK (flipped weight 1) — weak-accepted: no slot grades Lapsed 1 day's headline, so this over-application is only visible in the plan row; K10 keeps one headline control on Lapsed 1 day. Not worth a new slot: the surface already has a headline sample
- `degrade:dep_over` KILLED (flipped weight 4) — live: K2 reads it: over-applying the reach test to Lapsed 1 day flips a control
- `degrade:qa_over` KILLED (flipped weight 10) — weak-accepted: no direct slot grades Lapsed 7 days' Call, so this over-application shows through its headline and string slots; it is a declared control read per run by node_verdicts
- `degrade:pull_over` KILLED (flipped weight 4) — live: K2 reads it: taking Lapsed 1 day off the Go list flips a control
- `degrade:alias_over` SURVIVED (flipped weight 0) — weak-accepted: no slot grades Season Pass start's Ticket column; the Ticket column is sampled on the Win & Collect row, where the mechanism lands, and adding a control slot would not change any decision
- `degrade:filt_over` SURVIVED (flipped weight 0) — weak-accepted: the red dot is off the plan: V1 (register_keys_exact, a delivery slot) catches an extra row, and delivery slots never count in the mutation view
- `degrade:built_over` SURVIVED (flipped weight 0) — weak-accepted: no slot grades Lapsed 30 days' call; it is a declared control read per run by node_verdicts, not a graded row
- `degrade:follow_over` SURVIVED (flipped weight 0) — weak-accepted: K12 greps the Canceled update on Axe Arena in the writes, which the solver cannot read; the operator is live in the ticket-state field only
- `degrade:ch_miss` KILLED (flipped weight 55) — live: the channel operator moves every designed member; it is the failure the forecast samples
- `intervention:rule:DONE` load-bearing — live: removing DONE's deciding record changes its member: the record is load-bearing as designed
- `intervention:rule:CORR` no-injected-records — live: the tool finds rows by id and a gcal row is keyed by event_id, so it reports no injected records; rule:CORR above is KILLED, and removing the event leaves the Sep 29 line, so the record is load-bearing
- `intervention:rule:DEP` load-bearing — live: removing DEP's deciding record changes its member: the record is load-bearing as designed
- `intervention:rule:QA` load-bearing — live: removing QA's deciding record changes its member: the record is load-bearing as designed
- `intervention:rule:PULL` load-bearing — live: removing PULL's deciding record changes its member: the record is load-bearing as designed
- `intervention:rule:ALIAS` load-bearing — live: removing ALIAS's deciding record changes its member: the record is load-bearing as designed
- `intervention:rule:FILT` load-bearing — live: removing FILT's deciding record changes its member: the record is load-bearing as designed
- `intervention:rule:BUILT` load-bearing — live: removing BUILT's deciding record changes its member: the record is load-bearing as designed
- `intervention:rule:FOLLOW` load-bearing — live: removing FOLLOW's deciding record changes its member: the record is load-bearing as designed
- `intervention:degrade:done_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:corr_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:dep_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:qa_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:pull_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:alias_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:filt_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:built_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:follow_over` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected
- `intervention:degrade:ch_miss` no-injected-records — live: a degrade operator acts on no injected record of its own, so there is nothing to remove: expected

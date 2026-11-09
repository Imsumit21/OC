# 01c Preflight Report — PASS

Revision rev2; SQL `f6eb3512dffa`, solver `92f94f353626`, surface `7e68f34657e8`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 50/50 recorded | yes |
| Geometry U (S5b′) | V3 U 0.640 PASS | yes |
| Geometry margin L_max | {'V3': 'OK'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:DONE` WEAK (flipped weight 5) — live: WEAK only because the tool counts VQ_Oakline as an aggregate slot; the rule also moves banked (B_PA, K_r_banked, write slots the tool can't read). Arthur's reply is the only record that says the wire came back
- `rule:CORR` KILLED (flipped weight 13) — live: KILLED: flips A_adv_PB, V12_Tallwater, VQ_Tallwater; the calendar note is the only record of the $40,000
- `rule:ALIAS` KILLED (flipped weight 5) — live: KILLED: flips S_out_PC; the Kestrel post joined through the signature and Contacts is the only route to Withdrawn
- `rule:FILT` KILLED (flipped weight 26) — live: KILLED: flips six slots on Copperleaf and Redwood, and the first pick falls to Sunfold
- `rule:EXC` KILLED (flipped weight 10) — live: KILLED: flips S_out_PD and S_out_PJ, and the first pick goes to Northglow at $126,000
- `rule:INPUT` KILLED (flipped weight 10) — live: KILLED: flips A_com_PE and V12_Sunfold, and the first pick goes to Sunfold at $90,000
- `rule:DATE` WEAK (flipped weight 10) — live: WEAK only because Q4 cash slots are aggregates: flips VQ_Harbor and VQ_Wavecrest, weight 5 each; ESG's note is the only record of Nov 14
- `rule:FOLLOW` WEAK (flipped weight 0) — live: WEAK in the tool's terms: it moves group organic_note, read by the write-content slots W_1, W_2, W_3 and W_count, which the tool can't read
- `degrade:done_over` WEAK (flipped weight 3) — weak-accepted: control trial: reads the returned wire onto Tallwater; flips VQ_Tallwater (aggregate) only, which is all a control needs to show
- `degrade:corr_over` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: Harbor Lane's Advance cell has no slot, its value and Q4 cash don't move. Kept: the operator is live for node_verdicts, and a slot here would add an always-pass row
- `degrade:alias_over` KILLED (flipped weight 11) — live: KILLED: withdrawing Wavecrest flips S_live_PG, V12_Wavecrest, VQ_Wavecrest
- `degrade:filt_over` WEAK (flipped weight 0) — weak-accepted: control trial: adding Homa changes the population, read by S_total (register_keys_exact), a delivery slot the tool doesn't flip
- `degrade:exc_over` KILLED (flipped weight 13) — live: KILLED: ruling Sunfold out flips A_com_PE, V12_Sunfold, VQ_Sunfold
- `degrade:input_over` WEAK (flipped weight 3) — weak-accepted: control trial: flips V12_Oakline (aggregate) only
- `degrade:date_over` WEAK (flipped weight 3) — weak-accepted: control trial: flips VQ_Sunfold (aggregate) only; net 45 from Nov 14 is Dec 29, still in Q4
- `degrade:follow_over` WEAK (flipped weight 0) — weak-accepted: control trial: an extra note to Oakline is a write the drafts slots can see; the tool reads group membership only
- `degrade:ch_done` WEAK (flipped weight 5) — live: the channel behind rule DONE: Oakline's $10,000 stays banked, Q4 cash 20,000
- `degrade:ch_corr` KILLED (flipped weight 13) — live: KILLED: Tallwater keeps $60,000
- `degrade:ch_alias` KILLED (flipped weight 5) — live: KILLED: Moonrail stays Live
- `degrade:ch_filt1` KILLED (flipped weight 13) — live: KILLED: Copperleaf never reaches the model
- `degrade:ch_filt2` KILLED (flipped weight 13) — live: KILLED: Redwood never reaches the model
- `degrade:ch_exc` KILLED (flipped weight 10) — live: KILLED: Northglow and Pinegrove stay Live
- `degrade:ch_input` KILLED (flipped weight 10) — live: KILLED: Sunfold keeps 50,000 installs
- `degrade:ch_date` WEAK (flipped weight 10) — live: the channel behind rule DATE: net-60 advances look like Q4 money; flips VQ_Harbor and VQ_Wavecrest
- `degrade:ch_follow` WEAK (flipped weight 0) — live: the channel behind rule FOLLOW: no organic notes are drafted; read by write-content slots
- `intervention:rule:DONE` load-bearing — live: load-bearing: dropping Arthur's reply puts the $10,000 back in banked
- `intervention:rule:CORR` no-injected-records — weak-accepted: no-injected-records is a tool limit: difficulty_mutation indexes rows by id, and a gcal row is keyed event_id. Checked by hand: with the event row removed the solver gives Tallwater advance 60000, value 60000, Q4 60000
- `intervention:rule:ALIAS` load-bearing — live: load-bearing: dropping the Kestrel post leaves Moonrail Live
- `intervention:rule:FILT` load-bearing — live: load-bearing: dropping Robert's reply loses Copperleaf
- `intervention:rule:EXC` load-bearing — live: load-bearing: dropping the term sheet removes the offer; the rights text sits in the sheet itself
- `intervention:rule:INPUT` load-bearing — live: load-bearing: dropping the card comment puts Sunfold back at 50,000
- `intervention:rule:DATE` load-bearing — live: load-bearing: dropping ESG's note puts signing back to Oct 31
- `intervention:rule:FOLLOW` load-bearing — live: load-bearing: dropping the standing line removes the notes
- `intervention:degrade:done_over` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:corr_over` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:alias_over` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:filt_over` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:exc_over` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:input_over` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:date_over` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:follow_over` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:ch_done` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:ch_corr` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:ch_alias` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:ch_filt1` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:ch_filt2` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:ch_exc` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:ch_input` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:ch_date` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it
- `intervention:degrade:ch_follow` no-injected-records — weak-accepted: no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it

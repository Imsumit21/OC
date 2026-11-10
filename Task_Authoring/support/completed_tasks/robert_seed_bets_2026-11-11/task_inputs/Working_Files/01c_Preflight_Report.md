# 01c Preflight Report — PASS

Revision rev1; SQL `40f90385e31e`, solver `4c9f139f4940`, surface `32bb28690128`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 30/30 recorded | yes |
| Geometry U (S5b′) | V3 U 0.714 PASS | yes |
| Geometry margin L_max | {'V3': 'OK'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:RET` KILLED (flipped weight 5) — live: KILLED: flips X1. Its natural reading moves: MotMot paid 37,056.00 -> 41,088.00; B1 959,342.64 -> 963,374.64. Its declared text slots (B1, C1, R1) are graded from the writes and out of this measure.
- `rule:OFF` KILLED (flipped weight 5) — live: KILLED: flips X3. Its natural reading moves: Lucas paid 13,975.00 -> 6,450.00; B1 959,342.64 -> 951,817.64. Its declared text slots (B1, C2, R1) are graded from the writes and out of this measure.
- `rule:ORPH` KILLED (flipped weight 5) — live: KILLED: flips X4. Its natural reading moves: Leapblock paid 407,944.00 -> 374,654.00; B1 959,342.64 -> 926,052.64. Its declared text slots (B1, C3, R1) are graded from the writes and out of this measure.
- `rule:CORR` KILLED (flipped weight 6) — live: KILLED: flips X5, S6. Its natural reading moves: JPMorgan paid 0.00 -> 4,000.00; bucket Not a cost -> Build; B1 959,342.64 -> 963,342.64. Its declared text slots (B1, C4, R1) are graded from the writes and out of this measure.
- `rule:ALIAS` KILLED (flipped weight 6) — live: KILLED: flips X6, S6. Its natural reading moves: Node Media paid unchanged at 16,428.57; bucket Marketing -> Build; B1 959,342.64 -> 975,771.21. Its declared text slots (B1, R1) are graded from the writes and out of this measure.
- `rule:CLASS` KILLED (flipped weight 6) — live: KILLED: flips X8, S6. Its natural reading moves: Lauren Brooks paid unchanged at 1,500.00; bucket Marketing -> Build; B2 544,433.44 -> 544,933.44; B3 72,685.61 -> 73,685.61. Its declared text slots (B2, B3) are graded from the writes and out of this measure.
- `rule:CURR` KILLED (flipped weight 4) — live: KILLED: flips X9, S6. Its natural reading moves: Martin Walsh paid 0.00 -> 1,999.00; bucket Company -> Build; B2 544,433.44 -> 546,432.44. Its declared text slots (B2) are graded from the writes and out of this measure.
- `degrade:ret_over` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: flips no slot. Over-application operator on Leapblock (treats the two Leapblock $3,700 wires of Aug 2025 as one returned and one re-sent). Controls measure over-application and are reported as control trials, never as landings, so it is deliberately not a designed loss
- `degrade:off_over` WEAK (flipped weight 1) — weak-accepted: WEAK: flips S3. Over-application operator on Graham Porter (adds the card-paid ZM animator with no receipt). Controls measure over-application and are reported as control trials, never as landings, so it is deliberately not a designed loss
- `degrade:orph_over` WEAK (flipped weight 0) — weak-accepted: WEAK: flips no slot. Over-application operator on Eveline Art (counts Awaiting and Scheduled notices as payments for other payees). Controls measure over-application and are reported as control trials, never as landings, so it is deliberately not a designed loss
- `degrade:corr_over` WEAK (flipped weight 0) — weak-accepted: WEAK: flips no slot. Over-application operator on Singular (drops another one-off wire as an internal transfer). Controls measure over-application and are reported as control trials, never as landings, so it is deliberately not a designed loss
- `degrade:alias_over` WEAK (flipped weight 1) — weak-accepted: WEAK: flips S6. Over-application operator on Adjoe, Leapblock (moves a studio such as Leapblock into Marketing). Controls measure over-application and are reported as control trials, never as landings, so it is deliberately not a designed loss
- `degrade:class_over` WEAK (flipped weight 1) — weak-accepted: WEAK: flips S6. Over-application operator on Graham Porter (moves a build contractor such as Graham Porter into Marketing). Controls measure over-application and are reported as control trials, never as landings, so it is deliberately not a designed loss
- `degrade:curr_over` WEAK (flipped weight 0) — weak-accepted: WEAK: flips no slot. Over-application operator on Lauren Brooks (treats a dollar wire as foreign). Controls measure over-application and are reported as control trials, never as landings, so it is deliberately not a designed loss
- `degrade:ch_miss` KILLED (flipped weight 34) — live: KILLED: flips X1, X3, X4, X5, X6, X8, X9, S6, putting each channel member (JPMorgan, Lauren Brooks, Leapblock, Lucas, Martin Walsh, MotMot, Node Media) on its rule's natural reading
- `intervention:rule:RET` load-bearing — weak-accepted: load-bearing through the solver's presence gate only: removing the 4 note(s) on the issue changes MotMot and flips X1, inside the closure. The fact that decides the row is base (the Apr 2024 Slack notes), fixed in the solver, which an in-memory SQL edit can't remove; a run could still reach it by name without the note
- `intervention:rule:OFF` load-bearing — weak-accepted: load-bearing through the solver's presence gate only: removing the 3 note(s) on the issue changes Lucas and flips X3, inside the closure. The fact that decides the row is base (the five Western Union receipts), fixed in the solver, which an in-memory SQL edit can't remove; a run could still reach it by name without the note
- `intervention:rule:ORPH` load-bearing — live: load-bearing: the solver reads the amount or the account from this seeded row's text; removing it changes Leapblock and flips X4, inside the closure, and no base record restores it
- `intervention:rule:CORR` load-bearing — live: load-bearing: the solver reads the amount or the account from this seeded row's text; removing it changes JPMorgan and flips X5, S6, inside the closure, and no base record restores it
- `intervention:rule:ALIAS` load-bearing — weak-accepted: load-bearing through the solver's presence gate only: removing the 2 note(s) on the issue changes Node Media and flips X6, S6, inside the closure. The fact that decides the row is base (Node's invoice mail), fixed in the solver, which an in-memory SQL edit can't remove; a run could still reach it by name without the note
- `intervention:rule:CLASS` load-bearing — weak-accepted: load-bearing through the solver's presence gate only: removing the 3 note(s) on the issue changes Lauren Brooks and flips X8, S6, inside the closure. The fact that decides the row is base (her contract), fixed in the solver, which an in-memory SQL edit can't remove; a run could still reach it by name without the note
- `intervention:rule:CURR` load-bearing — weak-accepted: load-bearing through the solver's presence gate only: removing the 2 note(s) on the issue changes Martin Walsh and flips X9, S6, inside the closure. The fact that decides the row is base (the BGN notice and the laptop note), fixed in the solver, which an in-memory SQL edit can't remove; a run could still reach it by name without the note
- `intervention:degrade:ret_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:off_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:orph_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:corr_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:alias_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:class_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:curr_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ch_miss` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records

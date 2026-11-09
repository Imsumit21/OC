# 01c Preflight Report — PASS

Revision rev9; SQL `ea5b542897c8`, solver `c2eca0f97c62`, surface `6d9cd388cdbb`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 32/32 recorded | yes |
| Geometry U (S5b′) | V3 U 0.828 PASS | yes |
| Geometry margin L_max | {'V3': 'OK'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:INLINE` WEAK (flipped weight 0) — live: WEAK on direct slots by construction: INLINE is graded on write content (I1 to I4 and V4), which the grader decodes and geometry counts as flippable; Arthur's inline comments are the only records that a popup was left out of #1905 and #1908
- `rule:REPLY` KILLED (flipped weight 13) — live: KILLED: flips a direct slot of weight 3 or more; Brian's Dec 1 reply under the gems post is the only record that the shop icons came back
- `rule:BACK` KILLED (flipped weight 13) — live: KILLED: flips a direct slot of weight 3 or more; Marcus's Dec 3 DM is the only record that the Tavern frame went again
- `rule:FOLLOW` SURVIVED (flipped weight 0) — live: SURVIVED on direct slots by construction: FOLLOW is graded on write content (O1 to O3), which the grader decodes and geometry counts as flippable; Brian's comment on the UI optimization card is the only statement of the closing rule
- `rule:GONE` KILLED (flipped weight 18) — live: KILLED: flips a direct slot of weight 3 or more; the removal is read from base records (C09SWTHEMEW/1764659626.614679, f_948768f5a462e7037d17c9, C9CA62B5180A/1765927876.696389); no seeded record carries it
- `rule:LINE` KILLED (flipped weight 13) — live: KILLED: flips a direct slot of weight 3 or more; the open state of #1913 is base data (harmonygames-Games/GameOfDominoes#1913), so nothing seeded carries it
- `rule:ELSE` KILLED (flipped weight 21) — live: KILLED: flips a direct slot of weight 3 or more; flicker rests on base commits and #builds; Brian's Dec 8 DM is the only closing record for music and acid
- `rule:ALIAS` KILLED (flipped weight 15) — live: KILLED: flips a direct slot of weight 3 or more; Vincent's mail and his note on ENG-2363 are the only ties from the two lines to their tickets
- `degrade:ch_miss` KILLED (flipped weight 56) — live: KILLED: the channel-miss operator puts each channel member on its rule's natural reading; it flips the direct slots of every rule except INLINE and FOLLOW, which are write-content
- `degrade:inline_over` WEAK (flipped weight 0) — weak-accepted: WEAK: over-application operator on its control, ENG-2417 and ENG-2432 (their state is graded through K9 and K12, write-content samples). Controls are reported as control trials, never landings, and are deliberately not weighted
- `degrade:reply_over` WEAK (flipped weight 8) — weak-accepted: WEAK: over-application operator on its control, the Purple bg line (it feeds V1 and V5). Controls are reported as control trials, never landings, and are deliberately not weighted
- `degrade:back_over` WEAK (flipped weight 8) — weak-accepted: WEAK: over-application operator on its control, the character frames line (it feeds V1 and V5). Controls are reported as control trials, never landings, and are deliberately not weighted
- `degrade:gone_over` KILLED (flipped weight 8) — weak-accepted: KILLED: over-application operator on its control, the team navigation line (K7). Controls are reported as control trials, never landings, and are deliberately not weighted
- `degrade:line_over` KILLED (flipped weight 11) — weak-accepted: KILLED: over-application operator on its control, the treasure button post (F3). Controls are reported as control trials, never landings, and are deliberately not weighted
- `degrade:else_over` KILLED (flipped weight 11) — weak-accepted: KILLED: over-application operator on its control, the mega tile post (F1). Controls are reported as control trials, never landings, and are deliberately not weighted
- `degrade:alias_over` KILLED (flipped weight 8) — weak-accepted: KILLED: over-application operator on its control, the team navigation line (K7). Controls are reported as control trials, never landings, and are deliberately not weighted
- `intervention:rule:INLINE` load-bearing — live: LOAD-BEARING: removing the rule's seeded deciding record from an in-memory copy of the SQL moves the member to its natural reading, with no change outside the closure
- `intervention:rule:REPLY` load-bearing — live: LOAD-BEARING: removing the rule's seeded deciding record from an in-memory copy of the SQL moves the member to its natural reading, with no change outside the closure
- `intervention:rule:BACK` load-bearing — live: LOAD-BEARING: removing the rule's seeded deciding record from an in-memory copy of the SQL moves the member to its natural reading, with no change outside the closure
- `intervention:rule:FOLLOW` load-bearing — live: LOAD-BEARING: removing the rule's seeded deciding record from an in-memory copy of the SQL moves the member to its natural reading, with no change outside the closure
- `intervention:rule:GONE` no-injected-records — redundant: no-injected-records: the removal is read from base records (C09SWTHEMEW/1764659626.614679, f_948768f5a462e7037d17c9, C9CA62B5180A/1765927876.696389); no seeded record carries it; the sampled key has no seeded deciding record, by design
- `intervention:rule:LINE` no-injected-records — redundant: no-injected-records: the open state of #1913 is base data (harmonygames-Games/GameOfDominoes#1913), so nothing seeded carries it; the sampled key has no seeded deciding record, by design
- `intervention:rule:ELSE` load-bearing — live: LOAD-BEARING: removing the rule's seeded deciding record from an in-memory copy of the SQL moves the member to its natural reading, with no change outside the closure
- `intervention:rule:ALIAS` load-bearing — live: LOAD-BEARING: removing the rule's seeded deciding record from an in-memory copy of the SQL moves the member to its natural reading, with no change outside the closure
- `intervention:degrade:ch_miss` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:inline_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:reply_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:back_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:gone_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:line_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:else_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:alias_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records

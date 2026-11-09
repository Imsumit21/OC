# 01c Preflight Report — PASS

Revision rev2; SQL `65b7c3ec814b`, solver `8e27e3fd952d`, surface `4ffde3a42aaf`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 62/62 recorded | yes |
| Geometry U (S5b′) | V3 U 0.782 PASS | yes |
| Geometry margin L_max | {'V3': 'OK'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:ADV` KILLED (flipped weight 20) — live: KILLED: graded through its direct slots and the write-content slots K1, K8, P1, A1, NC_Deepak, B2, which geometry counts; the Due Diligence advisor table and the term sheet are the only records that take advisor options out of the merged lines
- `rule:LETTER` KILLED (flipped weight 16) — live: KILLED: graded through its direct slots and the write-content slots C_DATE, N_Vincent, N_Oliver, which geometry counts; only joining the six letters to the eight Feb 12 Carta entries shows the two with no letter
- `rule:TOLD` KILLED (flipped weight 16) — live: KILLED: graded through its direct slots and the write-content slots C_FIRST, LC_Seg, LC_Neb, which geometry counts; Leonard's Feb 9 DM and Robert's seeded reply are the only records that two angels were told
- `rule:ASOF` SURVIVED (flipped weight 0) — live: SURVIVED: graded through its direct slots and the write-content slots A1, A2, AL_*, which geometry counts; KPMG's seeded mail fixes the date; the notices' effective dates give the figures
- `rule:FAM` KILLED (flipped weight 6) — live: KILLED: graded through its direct slots and the write-content slots F1, F2, F3, N_COUNT, which geometry counts; the seeded reply under the Feb 12 list is the only record of the family rule
- `rule:BOARD` SURVIVED (flipped weight 0) — live: SURVIVED: graded through its direct slots and the write-content slots B1, B2, L6, G2, which geometry counts; the two resignation mails decide the board
- `rule:ASK` SURVIVED (flipped weight 0) — live: SURVIVED: graded through its direct slots and the write-content slots Q1, which geometry counts; Claire's group DM is the only record of the question
- `rule:BOUNCE` KILLED (flipped weight 8) — live: KILLED: graded through its direct slots and the write-content slots C_DATE, which geometry counts; the seeded delivery failure in Owen's letter thread is the only record that his letter never reached him
- `rule:ALIAS` KILLED (flipped weight 8) — live: KILLED: graded through its direct slots and the write-content slots C_FIRST, LC_Col, which geometry counts; Leonard's seeded Feb 12 mail to Akin is the only record that Collins was told
- `rule:EXT` KILLED (flipped weight 8) — live: KILLED: graded through its direct slots and the write-content slots P1, P_first, N_Calvin, D6, N_COUNT, which geometry counts; Calvin's seeded forward of Carta's Jan 23 update is the only record of ES-3's Feb 20 last day
- `degrade:adv_over` WEAK (flipped weight 2) — weak-accepted: WEAK: over-application on its control ENG-2441 and ENG-2442; controls measure over-application and are not weighted as landings
- `degrade:letter_over` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: over-application on its control ENG-2450 and ENG-2460; controls measure over-application and are not weighted as landings
- `degrade:told_over` KILLED (flipped weight 6) — weak-accepted: KILLED: over-application on its control ENG-2448; controls measure over-application and are not weighted as landings
- `degrade:asof_over` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: over-application on its control ENG-2455; controls measure over-application and are not weighted as landings
- `degrade:fam_over` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: over-application on its control ENG-2442; controls measure over-application and are not weighted as landings
- `degrade:board_over` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: over-application on its control SUMMARY; controls measure over-application and are not weighted as landings
- `degrade:ask_over` WEAK (flipped weight 1) — weak-accepted: WEAK: over-application on its control ENG-2461; controls measure over-application and are not weighted as landings
- `degrade:bounce_over` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: over-application on its control ENG-2456; controls measure over-application and are not weighted as landings
- `degrade:ext_over` WEAK (flipped weight 1) — weak-accepted: WEAK: over-application on its control ENG-2454; controls measure over-application and are not weighted as landings
- `degrade:alias_over` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: over-application on its control ENG-2449; controls measure over-application and are not weighted as landings
- `degrade:live_miss` KILLED (flipped weight 7) — live: KILLED: the channel puts a member on its natural reading; where no direct slot reads the field, the write-content slots do
- `degrade:ch_adv` KILLED (flipped weight 20) — live: KILLED: the channel puts a member on its natural reading; where no direct slot reads the field, the write-content slots do
- `degrade:ch_letter` KILLED (flipped weight 16) — live: KILLED: the channel puts a member on its natural reading; where no direct slot reads the field, the write-content slots do
- `degrade:ch_told` KILLED (flipped weight 16) — live: KILLED: the channel puts a member on its natural reading; where no direct slot reads the field, the write-content slots do
- `degrade:ch_asof` SURVIVED (flipped weight 0) — live: SURVIVED: the channel puts a member on its natural reading; where no direct slot reads the field, the write-content slots do
- `degrade:ch_fam` KILLED (flipped weight 6) — live: KILLED: the channel puts a member on its natural reading; where no direct slot reads the field, the write-content slots do
- `degrade:ch_board` SURVIVED (flipped weight 0) — live: SURVIVED: the channel puts a member on its natural reading; where no direct slot reads the field, the write-content slots do
- `degrade:ch_ask` SURVIVED (flipped weight 0) — live: SURVIVED: the channel puts a member on its natural reading; where no direct slot reads the field, the write-content slots do
- `degrade:ch_bounce` KILLED (flipped weight 8) — live: KILLED: the channel puts a member on its natural reading; where no direct slot reads the field, the write-content slots do
- `degrade:ch_ext` KILLED (flipped weight 8) — live: KILLED: the channel puts a member on its natural reading; where no direct slot reads the field, the write-content slots do
- `degrade:ch_alias` KILLED (flipped weight 8) — live: KILLED: the channel puts a member on its natural reading; where no direct slot reads the field, the write-content slots do
- `intervention:rule:ADV` no-injected-records — live: no-injected-records: ADV is decided by base records; the Due Diligence advisor table and the term sheet are the only records that take advisor options out of the merged lines
- `intervention:rule:LETTER` load-bearing — live: load-bearing: removing the rule's injected deciding record flips its members to the natural reading, and nothing outside its closure changed
- `intervention:rule:TOLD` load-bearing — live: load-bearing: removing the rule's injected deciding record flips its members to the natural reading, and nothing outside its closure changed
- `intervention:rule:ASOF` load-bearing — live: load-bearing: removing the rule's injected deciding record flips its members to the natural reading, and nothing outside its closure changed
- `intervention:rule:FAM` load-bearing — live: load-bearing: removing the rule's injected deciding record flips its members to the natural reading, and nothing outside its closure changed
- `intervention:rule:BOARD` load-bearing — live: load-bearing: removing the rule's injected deciding record flips its members to the natural reading, and nothing outside its closure changed
- `intervention:rule:ASK` load-bearing — live: load-bearing: removing the rule's injected deciding record flips its members to the natural reading, and nothing outside its closure changed
- `intervention:rule:BOUNCE` load-bearing — live: load-bearing: removing the rule's injected deciding record flips its members to the natural reading, and nothing outside its closure changed
- `intervention:rule:ALIAS` load-bearing — live: load-bearing: removing the rule's injected deciding record flips its members to the natural reading, and nothing outside its closure changed
- `intervention:rule:EXT` load-bearing — live: load-bearing: removing the rule's injected deciding record flips its members to the natural reading, and nothing outside its closure changed
- `intervention:degrade:adv_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:letter_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:told_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:asof_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:fam_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:board_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ask_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:bounce_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ext_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:alias_over` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:live_miss` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ch_adv` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ch_letter` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ch_told` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ch_asof` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ch_fam` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ch_board` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ch_ask` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ch_bounce` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ch_ext` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ch_alias` no-injected-records — redundant: no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records

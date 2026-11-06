# 01c Preflight Report — PASS

Revision rev4; SQL `f1a290ced176`, solver `f8392ca56fc2`, surface `ecfd436788e5`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 30/30 recorded | yes |
| Geometry U (S5b′) | V3 U 0.870 PASS | yes |
| Geometry margin L_max | {'V3': 'OK'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:CORR` KILLED (flipped weight 8) — live: KILLED: flips G2 (DD decision) and V1 and the write-content slots C2, C3, R2, R3, R4, R6; Arthur's DM reply is the only record of the trimmed $140
- `rule:AUTH` KILLED (flipped weight 11) — live: KILLED: flips G2, G3 and V1 and the write-content slots C3, R4, R6, R7; only REVENUE_DAILY gives January income per game
- `rule:FILT` WEAK (flipped weight 3) — live: WEAK on direct slots by construction: FILT is graded through the plan and reply text (C1, L1, R2, R3, write_content slots the grader decodes; geometry counts them as flippable) and V1 (the LLC row count); the campaign is in no list; Leonard's status and the channel history are its only records
- `rule:COMPLETE` KILLED (flipped weight 8) — live: KILLED: flips I1 (Metabase decision) and V1 and the write-content slots R2, R3; Arthur's mail is the only record of the $248 he carries
- `rule:DONE` SURVIVED (flipped weight 0) — live: SURVIVED on direct slots by construction: DONE is graded through the plan and reply text (C3, R6, write_content slots the grader decodes; geometry counts them as flippable); the App Store notice is the only record that the support build did not ship
- `rule:DATE` SURVIVED (flipped weight 0) — live: SURVIVED on direct slots by construction: DATE is graded through the plan and reply text (C4, C5, write_content slots the grader decodes; geometry counts them as flippable); the card's own-deadline rule, the base layer.ai access-date post and (rev4) Leonard's reply under it (C09UHHN6PFZ/1770923700.470906, the only record that CF's concept art is there) set the layer.ai step
- `rule:STACKS` SURVIVED (flipped weight 0) — live: SURVIVED on direct slots by construction: STACKS is graded through the plan and reply text (P1, R2, R3, write_content slots the grader decodes; geometry counts them as flippable); Arthur's Jenkins email (robert@harmonygames.co/1856982378087295205) is the only record of what CF's account bills now ($62, over the ENG-2445 note's ~$95)
- `degrade:corr_over` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: over-application operator on its control member, Combo Fighter backend and auth stacks (AWS) (P1 reads its $62 in the plan text). Controls measure over-application and are reported as control trials (OVER-APPLIED / HELD) in node_verdicts, never as landings; they are deliberately not weighted
- `degrade:auth_over` WEAK (flipped weight 4) — weak-accepted: WEAK: over-application operator on its control member, Combo Fighter (G1). Controls measure over-application and are reported as control trials (OVER-APPLIED / HELD) in node_verdicts, never as landings; they are deliberately not weighted
- `degrade:filt_over` WEAK (flipped weight 3) — weak-accepted: WEAK: over-application operator on its control member, Unity Ads balance and Playable vendor (no slot of their own; they enter V1 and R1). Controls measure over-application and are reported as control trials (OVER-APPLIED / HELD) in node_verdicts, never as landings; they are deliberately not weighted
- `degrade:complete_over` WEAK (flipped weight 0) — weak-accepted: WEAK: over-application operator on its control member, Build machines (no slot; a Founder row changes no aggregate the surface reads). Controls measure over-application and are reported as control trials (OVER-APPLIED / HELD) in node_verdicts, never as landings; they are deliberately not weighted
- `degrade:done_over` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: over-application operator on its control member, Helpshift (I4 reads only its decision). Controls measure over-application and are reported as control trials (OVER-APPLIED / HELD) in node_verdicts, never as landings; they are deliberately not weighted
- `degrade:stacks_over` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: over-application operator on its control member, Domino Delights production account (AWS) (C2 reads its $140 in the plan text). Controls measure over-application and are reported as control trials (OVER-APPLIED / HELD) in node_verdicts, never as landings; they are deliberately not weighted
- `degrade:date_over` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: over-application operator on its control member, AppsFlyer (P3 reads its cost, not its date). Controls measure over-application and are reported as control trials (OVER-APPLIED / HELD) in node_verdicts, never as landings; they are deliberately not weighted
- `degrade:ch_miss` KILLED (flipped weight 13) — live: KILLED: the channel-miss operator puts each channel member on its rule's natural reading (DD/ZM keys, the campaign, Metabase/dbt/GitHub, DD support, layer.ai/GitHub dates, CF's stacks); it flips G2, G3, I1, V1 and the write-content slots
- `intervention:rule:CORR` load-bearing — live: LOAD-BEARING: removing the rule's injected deciding record from an in-memory copy of the SQL flips its members to the natural reading; nothing outside the node's closure changed (no escape)
- `intervention:rule:AUTH` load-bearing — live: LOAD-BEARING: removing the rule's injected deciding record from an in-memory copy of the SQL flips its members to the natural reading; nothing outside the node's closure changed (no escape)
- `intervention:rule:FILT` load-bearing — live: LOAD-BEARING: removing the rule's injected deciding record from an in-memory copy of the SQL flips its members to the natural reading; nothing outside the node's closure changed (no escape)
- `intervention:rule:COMPLETE` load-bearing — live: LOAD-BEARING: removing the rule's injected deciding record from an in-memory copy of the SQL flips its members to the natural reading; nothing outside the node's closure changed (no escape)
- `intervention:rule:DONE` load-bearing — live: LOAD-BEARING: removing the rule's injected deciding record from an in-memory copy of the SQL flips its members to the natural reading; nothing outside the node's closure changed (no escape)
- `intervention:rule:DATE` load-bearing — live: LOAD-BEARING: removing the rule's injected deciding record from an in-memory copy of the SQL flips its members to the natural reading; nothing outside the node's closure changed (no escape)
- `intervention:rule:STACKS` load-bearing — live: LOAD-BEARING: removing the rule's injected deciding record from an in-memory copy of the SQL flips its members to the natural reading; nothing outside the node's closure changed (no escape)
- `intervention:degrade:corr_over` no-injected-records — redundant: no-injected-records: a degrade operator models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:auth_over` no-injected-records — redundant: no-injected-records: a degrade operator models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:filt_over` no-injected-records — redundant: no-injected-records: a degrade operator models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:complete_over` no-injected-records — redundant: no-injected-records: a degrade operator models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:done_over` no-injected-records — redundant: no-injected-records: a degrade operator models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:stacks_over` no-injected-records — redundant: no-injected-records: a degrade operator models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:date_over` no-injected-records — redundant: no-injected-records: a degrade operator models a run's reading error and has no deciding record of its own; the rule interventions cover the records
- `intervention:degrade:ch_miss` no-injected-records — redundant: no-injected-records: a degrade operator models a run's reading error and has no deciding record of its own; the rule interventions cover the records

# 01c Preflight Report — PASS

Revision rev1; SQL `69db98aed17f`, solver `ce489e02535a`, surface `1c83028e4346`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 38/38 recorded | yes |
| Geometry U (S5b′) | V3 U 0.840 PASS | yes |
| Geometry margin L_max | {'V3': 'UNSUPPORTED'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:DONE1` SURVIVED (flipped weight 0) — live: flips G1 (Paul's group: New investor vs In talks); Leonard's Sep 29 nudge, the missing Completed notice and his #executives signed note C07C2866011/1758911700.336170 decide it
- `rule:INPUT` KILLED (flipped weight 5) — live: flips M3 (Anton's amount on the send list); Leonard's Sep 24 DM D05S58U4SAK/1758731100.281734 (and his Sep 26 'Anton signed the 25 one') is the deciding record
- `rule:DONE2` KILLED (flipped weight 20) — live: flips AC1 and AC2 (Dentsu and T-Accelerate build access); rev6: Arthur's Sep 30 #zombie-match3d post C0880U9751A/1759274400.518306 decides both against the ZOM-567 log
- `rule:CORR` KILLED (flipped weight 5) — live: flips ST1 (Sciplay's group: Keep warm vs In talks); Robert's #executives thread reply C07C2866011/1759248360.377105 decides it
- `rule:ALIAS` KILLED (flipped weight 5) — live: flips ST2 (Hiro Capital's group: Keep warm vs Awaiting reply); Edith Vane's mail + contact decide it
- `rule:FILT` KILLED (flipped weight 15) — live: flips ST3/ST4 (Homa, Brightwater on the send list)
- `rule:FOLLOW` SURVIVED (flipped weight 0) — solver-gap: rev9: the checklist writes (a checklist per group, one item per firm or angel) are graded by write-content slot CL1 (trello_create_check_item text), which the solver does not express; the rule is load-bearing on the card comments (intervention load-bearing)
- `rule:DUP` SURVIVED (flipped weight 0) — solver-gap: rev9: NCsoft's follow-up outcome (comment on Leonard's open To Do card 68c99e98737744bd966aed24 'F/up with Anel after the engine deep dive' instead of a new card) is graded by delivery slot AN1 (trello_card) and the rubric's exact follow-up set; the solver's Follow-up field changes but no field selector can read a Trello write; load-bearing on the To Do card and Leonard's Sep 29 comment 68db03b86054eff7e8e92474
- `rule:BOOKED` SURVIVED (flipped weight 0) — solver-gap: rev9: Dentsu (base Oct 1 meeting evt_3671b9a924ccba550e51fa) and Makers Fund (seeded Oct 8 call evt_6b2e94d0c17a3f58e9d2b1 'Michael Cheung and Leonard Hayes', Makers' partner on f_48247af79428823c3cac92) get no follow-up card; an extra card is an absence check the text selectors cannot express (sample_from_regex has no lookahead), so the rubric's exact follow-up set grades it; load-bearing on the Makers event and Leonard's Sep 29 comment
- `degrade:done1_over` KILLED (flipped weight 8) — live: control Anton: over-applying the signature test moves him to In talks, flipping G2
- `degrade:input_over` SURVIVED (flipped weight 0) — live: control Paul: an invented revision moves M1 (Paul's amount)
- `degrade:done2_over` SURVIVED (flipped weight 0) — weak-accepted: rev6 control NCsoft (in talks, never added): over-applying the done log gives NCsoft iOS access, which no slot samples (access slots are AC1 Dentsu and AC2 T-Accelerate, both now DONE2 mechanism slots); the over-application is visible only in the unsampled register cells, a sampling limit like alias_over
- `degrade:corr_over` KILLED (flipped weight 5) — live: control Dentsu: reading a quiet in-talks firm as passed after a pitch makes it Keep warm and drops its build access, moving AC1
- `degrade:alias_over` SURVIVED (flipped weight 0) — weak-accepted: control Makers Fund is not a sampled slot; over-application shows only in the volume/status counts, which are not graded per firm (sampling limit of 5)
- `degrade:filt_over` KILLED (flipped weight 5) — live: control T-Accelerate: splitting PXLite off makes T-Accelerate 'Not contacted this round', which drops its build access cell, moving AC2
- `degrade:follow_over` SURVIVED (flipped weight 0) — solver-gap: over-adding Dentsu to Keep warm shows only in the checklist writes (trello_create_check_item, write-content slot CL1 and the rubric), not a solver-read slot
- `degrade:dup_over` SURVIVED (flipped weight 0) — weak-accepted: control GFR Fund (in talks, no To Do card): commenting on an unrelated open To Do card (Playable Kickoff) instead of making GFR's card removes the GFR card, which write-content slot FU1 reads; the solver field change is not a field selector
- `degrade:booked_over` SURVIVED (flipped weight 0) — weak-accepted: control BBQ Capital (awaiting reply, nothing booked after Sep 30): skipping its card is read by write-content slot FU2 (trello_create_card text 'BBQ'); the solver field change is not a field selector
- `degrade:filt_miss` KILLED (flipped weight 15) — live: channel degrade for Homa / Brightwater: moves ST3/ST4
- `intervention:rule:DONE1` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:INPUT` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:DONE2` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:CORR` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:ALIAS` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:FILT` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:FOLLOW` load-bearing — live: load-bearing: removing the deciding seeded records changes the solver output
- `intervention:rule:DUP` load-bearing — live: load-bearing: removing the seeded record changes the Follow-up truth
- `intervention:rule:BOOKED` load-bearing — live: load-bearing: removing the seeded record changes the Follow-up truth
- `intervention:degrade:done1_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:input_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:done2_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:corr_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:alias_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:filt_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:follow_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:dup_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:booked_over` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove
- `intervention:degrade:filt_miss` no-injected-records — live: degrade operators model run behaviour, not injected records; nothing to remove

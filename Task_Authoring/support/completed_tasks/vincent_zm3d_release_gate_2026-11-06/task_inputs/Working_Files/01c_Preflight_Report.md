# 01c Preflight Report — PASS

Revision rev2; SQL `5a8d995238f3`, solver `f7a6aeed38d8`, surface `e3001f0c8fa4`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 34/34 recorded | yes |
| Geometry U (S5b′) | V3 U 0.889 PASS | yes |
| Geometry margin L_max | {'V3': 'OK'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:R_DONE_BUILD` KILLED (flipped weight 5) — live: KILLED: the Done-means-in-build reading turns ZOM-569 FIXED / in candidate and flips S01 and T01 (weight 10); the cut evidence is Android #2028 starting 21:36Z with the fix, after both submission jobs started (18:43Z / 18:45Z), under Arthur's build doc f_a038a576ca8db6955fae95
- `rule:R_DONE_SERVER` KILLED (flipped weight 5) — live: KILLED: the approved-merged-and-rolled-out-means-live reading turns ZOM-567 FIXED / server - live and flips S03 and T02; rev2's deciding record is Arthur's inline review comment on match3d-backend#36 (harmonygames-Games/match3d-backend#36#rc_1, 22:35Z, after Douglas's 22:01Z rollout DM): the chest rows the grant reads are still dev-only, so the fix is not live
- `rule:R_CORRECTION` KILLED (flipped weight 10) — live: KILLED: Done-plus-older-pass reading turns ZOM-435 and ZOM-473 FIXED and flips S05, S07 and T03; the re-tests sit on a Trello card comment (68dc63484a5b2d0a869e758f) and in a Turkish DM (D0770ET1HV2/1759267800.858041)
- `rule:R_ALIAS` KILLED (flipped weight 5) — live: KILLED: without mapping the Puzzles vs Zombies session notes to ZOM-562 the call stays KNOWN ISSUE and S09 / T04 flip
- `rule:R_FILTER` KILLED (flipped weight 30) — live: KILLED: the team ZOM + label Bug scope drops every non-Bug and other-team row (25 weight incl. S11, S12, S13, S28, S29 and V01); the Sep 22 tab and Vincent's 'Bug tickets only this time' post support the old scope
- `rule:R_COMPLETION` KILLED (flipped weight 8) — live: KILLED: the open-means-broken reading makes ZOM-563 KNOWN ISSUE and ZOM-564 BLOCKER, flipping S14 and S24
- `rule:R_SYMPTOM_NOTE` KILLED (flipped weight 5) — live: KILLED: the description-only reading keeps ZOM-293 NO CALL and flips S30 and T07; the deciding record is Vincent's Jul 3 comment cmt_zom293_1 (what goes wrong: the boosters picked for the retry are charged and gone after the tier-change reload)
- `rule:R_OLD_NOTE` KILLED (flipped weight 10) — live: KILLED: the text-and-latest-check reading keeps ZOM-458 and ZOM-535 KNOWN ISSUE and flips S31, S32, T06 and T08; the deciding record is Brian's Sep 29 message in the QA group DM (D0770ET1HV2/1759160460.731000) with how bad each one is
- `degrade:over:every-done-not-in-build` KILLED (flipped weight 9) — live: KILLED: over-applying the cut to the controls ZOM-506 / ZOM-557 / ZOM-561 (fixes merged before 18:43Z) flips S25-S27, so an agent that over-learns the trap is penalised
- `degrade:over:every-server-fix-not-live` KILLED (flipped weight 5) — live: KILLED: over-applying the not-live rule to ZOM-563 (deployed and confirmed on prod in D079SNE2TL4) flips S14
- `degrade:over:every-done-came-back` KILLED (flipped weight 6) — live: KILLED: treating every Done fix as failing again flips the control slots S25 / S26 (ZOM-506, ZOM-557 pass in Vincent's Sep 30 check)
- `degrade:over:map-every-refill-report-to-562` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: the over-application moves ZOM-504 (ungraded control) only; accepted because the graded ZOM-562 row and the register keys are unaffected and adding a weighted ZOM-504 slot would add a sample slot only to grade a control
- `degrade:over:every-non-bug-is-defect` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: moves the ungraded controls ZOM-565 / ZOM-566 / ART-790; the NO CALL samples S28 (ZOM-513) and S29 (ZOM-387) are graded instead, and they are not in the operator's member set; accepted
- `degrade:over:every-in-progress-ships` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: moves ZOM-534 / ZOM-544 (ungraded controls); accepted, the graded completion rows are ZOM-563 / ZOM-564
- `degrade:over:every-vague-ticket-is-a-bug` SURVIVED (flipped weight 0) — weak-accepted: SURVIVED: moves the ungraded controls ZOM-311 / ZOM-130 (bare tool and feature tickets) only; accepted, the graded rows are ZOM-293 (S30, T07) and the NO CALL samples S28 / S29, and a weighted control slot would only grade a control
- `degrade:over:every-cosmetic-is-worse` KILLED (flipped weight 3) — live: KILLED: escalating every cosmetic known issue flips the sample S22 (ZOM-481, a lingering health bar, level finishes), so an agent that over-learns R_OLD_NOTE is penalised
- `degrade:slip:comments` KILLED (flipped weight 6) — live: KILLED: a run that calls tickets from label and description instead of their QA comments flips S20 (ZOM-559) and S24 (ZOM-564); this is the per-record comment channel
- `intervention:rule:R_DONE_BUILD` load-bearing — live: load-bearing: removing cmt_zom569_1 / the H1 doc changes ZOM-569
- `intervention:rule:R_DONE_SERVER` load-bearing — live: load-bearing: removing Arthur's inline review comment on #36 changes ZOM-567 (rev1's #zombie-ops withdrawal is gone in rev2)
- `intervention:rule:R_CORRECTION` load-bearing — live: load-bearing: removing the Trello re-test or Brian's DM changes ZOM-435 / ZOM-473
- `intervention:rule:R_ALIAS` load-bearing — live: load-bearing: removing the vendor mail or the Contacts entry changes ZOM-562
- `intervention:rule:R_FILTER` load-bearing — live: load-bearing: removing Leonard's rules doc narrows the scope to Bug-labelled ZOM tickets
- `intervention:rule:R_COMPLETION` load-bearing — live: load-bearing: removing Brian's iOS #50 re-test on ZOM-564 changes its call (ZOM-563 rests on base DMs)
- `intervention:rule:R_SYMPTOM_NOTE` load-bearing — live: load-bearing: removing cmt_zom293_1 returns ZOM-293 to NO CALL
- `intervention:rule:R_OLD_NOTE` load-bearing — live: load-bearing: removing Brian's Sep 29 message returns ZOM-458 and ZOM-535 to KNOWN ISSUE
- `intervention:degrade:over:every-done-not-in-build` no-injected-records — redundant: no-injected-records: an over-application operator has no deciding records of its own
- `intervention:degrade:over:every-server-fix-not-live` no-injected-records — redundant: no-injected-records: an over-application operator has no deciding records of its own
- `intervention:degrade:over:every-done-came-back` no-injected-records — redundant: no-injected-records: an over-application operator has no deciding records of its own
- `intervention:degrade:over:map-every-refill-report-to-562` no-injected-records — redundant: no-injected-records: an over-application operator has no deciding records of its own
- `intervention:degrade:over:every-non-bug-is-defect` no-injected-records — redundant: no-injected-records: an over-application operator has no deciding records of its own
- `intervention:degrade:over:every-in-progress-ships` no-injected-records — redundant: no-injected-records: an over-application operator has no deciding records of its own
- `intervention:degrade:over:every-vague-ticket-is-a-bug` no-injected-records — redundant: no-injected-records: an over-application operator has no deciding records of its own
- `intervention:degrade:over:every-cosmetic-is-worse` no-injected-records — redundant: no-injected-records: an over-application operator has no deciding records of its own
- `intervention:degrade:slip:comments` no-injected-records — redundant: no-injected-records: the channel degrade is a reading slip, not a record

# F1 replay: original criterion withdrawn (post-hoc amendment)

Recorded 2026-10-26, after the 3-seed replay (`logs/f1/f1_replay_round3.log`).

## Result under the original criterion

**F1 replay (B): FAIL.** Variant B bracketed the observed 4-run average (89.9%) in **0 of 15 views on every seed**;
r3 was bracketed in 15/15. The original criterion was fixed at 20:14 on 2026-10-25, before the multi-seed runs, and is
reported unchanged.

## Amendment (reason independent of the result)

r1, r2 and r6 are mixed-model runs: they contain Opus 5 decisions after a fallback. Their scores are therefore not a
valid target for an Opus 4.8 forecast. The correction excludes **all three** from the target set whatever they scored;
it is not a selection of convenient runs. It supplies **no replacement validation**: no run in this replay is
V3-valid, and the corrected target is diagnostic only.

## Consequences

- Replays are diagnostic, never a gate (see the corrected protocol).
- No calibration claim is made from any replay.
- The original FAIL stays in the record beside the amendment.

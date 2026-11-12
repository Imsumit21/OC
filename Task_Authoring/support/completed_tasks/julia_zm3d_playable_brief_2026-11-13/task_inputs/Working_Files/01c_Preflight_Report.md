# 01c Preflight Report — PASS

Revision rev2; SQL `7d1f2aaeb29c`, solver `3fb11113479e`, surface `bfc0af31ecfd`. Probabilistic parts are UNCALIBRATED and advisory.

| Part | Status | Blocking |
|---|---|---|
| Solver contract (S4b) | PASS | yes |
| Gradable surface validation | PASS | yes |
| Mutation dispositions (S5b) | 26/26 recorded | yes |
| Geometry U (S5b′) | V3 U 0.797 PASS | yes |
| Geometry margin L_max | {'V3': 'OK'} | no |
| Liveness dispositions (S5c) | 0 missing | no |
| Forecast (S5e) | recorded | no |

## Mutants
- `rule:EXPORT` KILLED (flipped weight 21) — live: KILLED: ablating EXPORT flips X1, X1b and X16 (Refrigerator and Retro TV state, Refrigerator owner) and the write-content X6, W4, K1; the solver reads 'the text kind' from Marcus's post row (C0880U9751A/1758906517.912099)
- `rule:ARTHOLD` KILLED (flipped weight 26) — live: KILLED: ablating ARTHOLD flips X2, X2b, X11, X11b (Bathtub and Iron state and owner) and X7, K2; the solver reads the bathroom sentence from Robert's note row (D05GU6L0XFH/1759178332.042459)
- `rule:REVISED` KILLED (flipped weight 21) — live: KILLED: ablating REVISED flips X3, X3b and X8 (Cactus Plant, Cone and Chainsaw state) from Ready to Owed and both counts; the solver reads 'the cone again with the new colours' from Brian's log of the outgoing folder (f_faf4d7c167d14a1127dcc3)
- `rule:AUDIO` KILLED (flipped weight 21) — live: KILLED: ablating AUDIO flips X5 and X12 (Rocket sound state and owner) and X10, K5, B6; the solver reads the 'no' cells of Calvin's grid (f_b2387e31d46d3a7b3fa2a9)
- `rule:PICKS` KILLED (flipped weight 10) — live: KILLED: ablating PICKS flips X13 and X14 (Bow and Dynamite board set) and B1; the solver reads 'in place of the last one on my list' from Robert's reply row (C08R8CHB0QL/1758922879.243189)
- `rule:ZIP` KILLED (flipped weight 21) — live: KILLED: ablating ZIP flips X4 and X17 (Cello state and owner) and X9, K4; the solver reads "won't unpack" from Brian's log of the outgoing folder (f_faf4d7c167d14a1127dcc3)
- `degrade:export_over` KILLED (flipped weight 9) — live: KILLED: over-applying EXPORT to its control flips C1 (Rolling Pin state), a sampled control row, and both counts
- `degrade:art_over` WEAK (flipped weight 6) — weak-accepted: WEAK: the control Desk Lamp is not a sampled row, so over-application shows only in the Owed and Ready counts (A1, A2). Accepted: the state_join group already holds five samples (two joins, a REVISED-free control, a self-stated Owed line and Rolling Pin); the counts catch it
- `degrade:revised_over` KILLED (flipped weight 9) — live: KILLED: over-applying the re-send to Fly Zapper (a line waiting on Claire's FBX) flips C2 (Fly Zapper state), a sampled control row, and both counts
- `degrade:audio_over` WEAK (flipped weight 6) — weak-accepted: WEAK: the control Success sound is not a sampled row; over-application moves only the counts. Accepted: B6 (the brief's sound section) names only the rocket and explosion cues, and the counts catch a third held cue
- `degrade:picks_over` KILLED (flipped weight 3) — live: KILLED: dropping Grenade from the eight flips C4 (Grenade board set), a sampled control row
- `degrade:zip_over` WEAK (flipped weight 6) — weak-accepted: WEAK: the control Music Keyboard is not a sampled row; over-application moves only the counts. Accepted: its note says Mon 29 Sep and not zipped, and the counts catch it
- `degrade:ch_miss` KILLED (flipped weight 96) — live: KILLED: a missed deciding record leaves the channel's members at their natural reading, which flips every sampled state, owner and board-set row of that rule
- `intervention:rule:EXPORT` load-bearing — live: load-bearing: removing Marcus's post row (C0880U9751A/1758906517.912099) sends the twelve project-saved lines back to Ready
- `intervention:rule:ARTHOLD` load-bearing — live: load-bearing: removing Robert's note row (D05GU6L0XFH/1759178332.042459) sends the twelve bathroom lines back to Ready
- `intervention:rule:REVISED` load-bearing — live: load-bearing: removing Brian's log (f_faf4d7c167d14a1127dcc3) sends the three recoloured lines back to Owed (Robert's base post stands alone) and, through ZIP, the eight instruments back to Ready
- `intervention:rule:AUDIO` load-bearing — live: load-bearing: removing Calvin's sheet rows (f_b2387e31d46d3a7b3fa2a9) sends the two cues back to Ready
- `intervention:rule:PICKS` load-bearing — live: load-bearing: removing Robert's reply row (C08R8CHB0QL/1758922879.243189) puts the dynamite back in the eight
- `intervention:rule:ZIP` load-bearing — live: load-bearing: removing Brian's log (f_faf4d7c167d14a1127dcc3) sends the eight instruments back to Ready
- `intervention:degrade:export_over` no-injected-records — live: no-injected-records: an over-application or missed-record operator is a way of reading the records, not a record; nothing to remove
- `intervention:degrade:art_over` no-injected-records — live: no-injected-records: an over-application or missed-record operator is a way of reading the records, not a record; nothing to remove
- `intervention:degrade:revised_over` no-injected-records — live: no-injected-records: an over-application or missed-record operator is a way of reading the records, not a record; nothing to remove
- `intervention:degrade:audio_over` no-injected-records — live: no-injected-records: an over-application or missed-record operator is a way of reading the records, not a record; nothing to remove
- `intervention:degrade:picks_over` no-injected-records — live: no-injected-records: an over-application or missed-record operator is a way of reading the records, not a record; nothing to remove
- `intervention:degrade:zip_over` no-injected-records — live: no-injected-records: an over-application or missed-record operator is a way of reading the records, not a record; nothing to remove
- `intervention:degrade:ch_miss` no-injected-records — live: no-injected-records: an over-application or missed-record operator is a way of reading the records, not a record; nothing to remove

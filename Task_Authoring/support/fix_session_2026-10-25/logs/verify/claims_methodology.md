# Claims for the methodology review, round 2 (P1: H2 priors, F1 forecast channels, M6 batches)

Every claim below is what I will write in the P1 report. Nothing stronger is claimed. [O] = observed in the logs
named, [I] = inference, [D] = a design decision. Round-1 corrections (A7 unchanged, the observation-collapse rule,
the rate units, the replay caveats, the exact sampler) are applied; the round-2 replay numbers are marked where they
replace the round-1 ones.

## C1. H2 priors: the counting rule, not a calibrated value

Claim: `hardness_ledger.priors` counts **one trial per (task, revision, run, family)** for verdict records. Aggregate
`observation` records declare no run ids, so the records of one (task, revision, family) collapse to one trial set:
`T = max(landed + not_landed)` (a confounded run is neither a landing nor a trial), `landed = max(landed)`,
`not_landed = T - landed` — a **lower bound** assuming the records' runs overlap maximally. An "upper" view
(`landed = min(T, sum(landed))` at the same `T = max counted`) is reported beside every prior that has such a group.
Both are **assumption-conditional sensitivity bounds**, not intervals established by the records: equal
`counts.runs` does not establish common run identities, and a pair of records with equal counts can be realised by
*disjoint* counted subsets (two trials, two landings) that the implemented upper view misses — a known limitation,
open, not claimed as fixed. Records that declare different `counts.runs` are refused, never merged. Each task's evidence is discounted by the Kish design
effect `1 + (m - 1) * rho` over its `m` **trials** (not weighted trials), with `rho = 0.5` an explicit, overridable
assumption. Record weights scale the evidence afterwards, so at `rho = 1` a task is worth one trial times its weight.

Evidence [O]:
- A17 (claude-opus-4-8), all tasks, 40 trials: `rho = 0` Beta(15, 9), mean 0.625, n_eff 22; `rho = 0.5`
  Beta(2.5705, 2.8544), mean 0.4738, n_eff 3.4249; `rho = 1` Beta(1.8833, 2.1167), mean 0.47, n_eff 2.0. Per task at
  rho 0.5: library:FE-6a7e 0.9677 (30 trials, deff 15.5), library:NF2 0.8571 (6, 3.5), season_pass 1.6 (4, 2.5).
  The pre-H2 rule gave Beta(15, 17), mean 0.469, n_eff 30. [I] The near-identical mean is a cancellation: collapsing
  12 season_pass verdict records into 4 trials raises it to 0.625 at rho 0, and the design effect on the 30-run
  library brings it back to 0.474 at rho 0.5 (0.47 at rho 1). rho moves the location, not only the width.
- A15: before Beta(1.9825, 3.4538), mean 0.3647, n_eff 3.4363; after lower Beta(2.1429, 3.1714), mean 0.4032,
  n_eff 3.3143, upper Beta(2.7143, 2.6), mean 0.5108. A7 is unchanged at Beta(1.4524, 2.2381): its confounded run was
  already excluded by the old rule and is still neither a landing nor a trial.
- Criterion-2 view (`--exclude-task season_pass`): at rho 0 Beta(14, 6), mean 0.70, n_eff 18; at rho 0.5
  Beta(2.1705, 1.6544), mean 0.5674, n_eff 1.8249. [I] This view has no verdict records, so its whole shift comes from
  rho; at rho 0 it is the pre-session prior.
- Self-test planted cases: three rules of one family in one run = one trial; `rho` 0/0.5/1; at rho 1 a weighted task
  is one trial times its weight (0.5, not 1.0); overlapping observations contribute 6 trials, not 8 or 12; a confounded
  run is not a trial; differing `counts.runs` are refused with a reason; rho outside [0, 1] or non-finite is refused;
  the earlier weighted-trials design effect fails the self-test under falsification (`logs/h1/falsify_h1.final3.txt`).

Not claimed: that rho = 0.5 is the right correlation, or that the new prior is calibrated. It is one assumption
applied consistently; the priors remain labelled UNCALIBRATED. The direction of the effect is the claim: correlated
replicates no longer count as independent evidence, and the A17 prior widens accordingly (n_eff 30 -> 3.42).

## C2. F1 forecast: the simulator is correct; the model is not validated

Claim 2a (implementation, testable): the channel simulator reproduces the analytic values of the design within the
stated Monte Carlo tolerance [O] (`hardness_forecast --self-test`, `logs/p1_suite_final4.txt`; SE = sqrt(p(1-p)/n)):
- 40 independent members at e = 0.02: simulated P(any) 0.558 vs exact 1 - 0.98^40 = 0.554. 1500 baselines = 9000
  runs at a fixed rate; SE = sqrt(p(1-p)/9000) = 0.0052, so the 0.03 tolerance is about 5.8 SE (conservative; the
  earlier 0.013 SE treated n as the baseline count and is corrected here).
- 40 fully linked members (run latent): 0.023 vs exact 0.02. Same basis; SE 0.0015, tolerance 0.01 (~6.5 SE).
- Integration over the rate's Beta (Beta(2, 98)): 1 - E[(1-e)^40] = 0.494 < plug-in 0.554; simulated 0.494. The six
  runs of one baseline share the same rate draw, so the run indicators are not independent after integrating the rate
  out; the honest SE is the empirical SD of the 1500 per-baseline six-run means, not a binomial SE.
- A cancelling count: one false exclusion + one false inclusion passes the count slot while both member slots fail;
  and a cause shared across slots: 0.88 expected patterns vs 1.34 independent at the same marginal rate (800 draws
  per side, not 1500).
- A three-step chain through a non-key-local solver: 0.497 vs exact 1 - 0.9*0.8*0.7 = 0.496. 1500 baselines = 9000
  runs; SE 0.0053, tolerance 0.03 (~5.7 SE).
- The rate is counted in the unit the simulator draws (Q2): one trial per member, batch or run, per (revision, run);
  a member-latent record converts to a run trial (failed if any member failed) and a batch/member mix is refused
  (planted: the old code stamped every record with the last unit and pooled 81 member trials as 3 runs).

Claim 2b (the revision-14 replay): **the acceptance criterion is NOT met.** The criterion (fixed in the acceptance
script at 20:14, before any multi-seed run) was: variant B (every mechanism leaks: the current model under the
revision-14 session's zero-landing assumption, not its archived forecast) must bracket the observed baseline average
89.9 % and r3's 91.8 % in the 10-90 % band, in every scenario view. Over seeds 7, 8, 9 [O] (`logs/f1/f1_replay_final3.txt`;
the round-3 re-run after the round-2 code changes is in `logs/f1/f1_replay_round3.log`):
- B: E[average] 0.9572 +/- 0.0010 (band 0.929-0.983); the average is bracketed in **0/15 views in all 3 seeds**;
  r3 in 15/15.
- C (evidence-weighted posterior: 0.10/0.15/0.08): E[average] 0.919-0.942; average bracketed in 4/15, 6/15, 6/15;
  r3 15/15.
- A (ledger-prior variant with in-sample channel rates, 9 mechanisms): E[average] 0.675-0.863; average 1/15
  (correlated slip only); r3 6/15. "Out of sample" is NOT claimed for A: its channel rates use the evaluated runs, and
  the shared ledger contains season_pass evidence (rev10 and rev13), so the mechanism priors are not task-held-out
  either.
- No-channel baselines (final tree): B0 E[average] 1.000 (0/15, 0/15); C0 0.9573-0.9814 (1/15, r3 [12, 14, 13]/15);
  A0 0.6823-0.8812 (5/15 in every seed, r3 9/15).

What the replay does show, as description rather than validation: the declared channels lower the forecast by about
0.04 in the two conditional variants (B0 1.000 -> B 0.957; C0 0.957 -> C 0.919), moving B and C toward the observed
average, as expected by construction (the rates were fitted on these runs); they do not move A toward it (A
0.676-0.863 vs observed 0.899, and A's bracket count falls from A0's 4-5/15 to 1/15). With the evidence-weighted
mechanism rates (C) the 10-90 % band of the simulated average contains the observed 89.9 % in the whole-rule views
(*3) and in correlated shard:32, in every seed; it does not contain it for partial-extent landings (shard:14, slip).
These views were identified after seeing results: a post-hoc subset, not 15 independent experiments (in B the extent
has no effect when landing rates are zero), so no replication claim follows from the counts.

Caveats that bound every number here (all disclosed):
1. **No held-out data.** One task, four baseline runs; the channel rates are in-sample, fitted on the same four runs
   they are judged against. This is a consistency check, not validation.
2. **The seeds measure Monte Carlo noise only** (the largest per-view SD across seeds on the final tree is 0.0027,
   A correlated shard:32), not sampling uncertainty over tasks or
   runs. The real uncertainty is in the priors and rates, and it is not represented by the seed spread.
3. Three of the four baselines are mixed-model runs (Opus 5 writes after a fallback); the replay uses Opus 4.8 priors
   and the runs' scores as observed, without a validity correction.
4. Order of events: variant A was run once (seed 7) at 19:18 and missed; the criterion on B was written at 20:14 and
   the multi-seed runs started 20:27. So B was chosen after seeing A fail. B is not arbitrary - it is the revision-14
   session's own zero-landing ("slips only") assumption (Rev14_Precheck_Findings.md §7: 95.1 %, 91.5-98.0, and "the
   model misses a loss channel") - but the criterion was not pre-registered before any result was seen. B is a
   current conditional model that adopts the historical zero-landing assumption; it does not reproduce the archived
   forecast (which included random class slips, absent here: B0 = 1.000), so the 1.000 -> 0.957 comparison is a
   current-code channel ablation, not an improvement over the archived 95.1 %.
5. M1 (value_notes) is tracker-only and not modelled (its slots are NOT_SOLVER), so the forecast omits that loss [I].
6. Round 2 changed A's mechanism priors (A15) and the channel/unit accounting; B and C use explicit `--channel-rate`
   overrides and zero/explicit mechanism rates, so their forecasts are unchanged. All variants were re-run with seeds
   7-9 on the final tree with the 20:14 criterion unchanged (`f1_replay_round3.log`); B again brackets the average in
   0/15 views. A pass after a third look would be exploratory, not a confirmed pre-registration.
7. B's 0/15 comes from r2 alone: r1, r3 and r6 average about 94.5 %, inside B's 0.929-0.983 band, and B excludes r2's
   landings by construction. The aggregate average is pulled below the band by one run.
8. The observed 89.9 % is the mean of four runs (92.2, 76.1, 91.8, 99.6), while the band describes the simulated
   six-run baseline mean; the bracket is not an 80 % coverage test for a four-run mean. The r3 comparison is the
   single-run one; it is not a power calculation, and r3 also contributes to the rate fitting and the brief batches.
9. C's rates (0.10 / 0.15 / 0.08) are the revision-14 session's `posterior_evidence` design, not fitted here; its
   agreement with the runs is therefore not independent evidence about the channels. The three `--channel-rate`
   overrides (Beta(4,266), Beta(3,3), Beta(1,13)) use raw in-sample counts and **bypass the H2 design-effect
   discounting**: H2 covers mechanism verdict records, not these channel overrides, and the report does not present
   H2 as covering their uncertainty or clustering.
10. The superseded 7/15 C bracket count (batches views silently equalled whole before the briefs fix) is not cited.
11. The criterion is WITHDRAWN in the harness as well as in the prose: `f1_acceptance.py` now prints its result as
    ADVISORY, records `criterion_B_met` for the historical record, and exits 0; the recorded 0/3 run is kept in
    `logs/f1/f1_replay_round3.log`. Withdrawing it supplies no replacement validation and no calibration claim.

## C3. M6 batches

Claim: the `batches` extent misses whole brief batches at a per-batch rate chosen so the per-run landing probability
is unchanged (`b = 1 - (1 - theta)^(1/B)`, conditioned on at least one miss), with batches from `trajectory_ledger`
briefs (r3: 37 briefs, all 37 carry key lists, 34 distinct batches after de-duplication) [O]. The draw is exact: the
number of missed batches is a zero-truncated Binomial(B, b) sampled by inverse CDF (O(B), no rejection loop), and
the missed batches are a uniform choice of that many. A planted test at B = 34 and theta in {0.3, 0.005} (4000 draws
each) checks E[K] = B b / theta within 0.05 and each batch's marginal b / theta within 0.01 (3+ Monte Carlo SE); every
simulated run reuses r3's 34 brief batches. The older `0.304 vs 0.3` statistic counts only the outer landing decision,
so it is not a test of the batch vector's distribution and is no longer offered as one. Keyless briefs are refused
rather than silently producing empty batches (planted; falsified).

## What I am asking the reviewer to judge

1. Are C1's claims exactly what the arithmetic supports, with the lower/upper bound naming correct, the observation
   rule implemented rather than promised, and the assumption labelled (rather than the prior presented as calibrated)?
2. Does C2a's tolerance reasoning hold at the stated draw counts, and is the Q2 unit rule (member/batch/run,
   member->run conversion, batch mix refused) the right estimator for the simulator?
3. Is C2b honest and complete: criterion not met, the descriptive comparison clearly separated from validation, all
   ten caveats adequate, and no claim that the replay validates the model?
4. Is there any place where the numbers as reported would mislead a reader about accuracy or uncertainty?

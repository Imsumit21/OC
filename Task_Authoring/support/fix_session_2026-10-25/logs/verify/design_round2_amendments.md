# Round-2 design amendments (methodologist verdict, applied) + audit evidence on disk

The methodologist reviewed design_round2.md and returned FAIL with the corrections below. This file supersedes the
named rows of design_round2.md. Everything else in that file stands.

## Q1 (supersedes H1-2) — observation collapse, corrected rule

For each (task, revision, family) group of `observation` records:
- require every record in the group to declare the same `counts.runs`; otherwise REFUSE (error naming the group) —
  a merge across different run counts is not a trial set;
- `T = max(landed + not_landed)` over the group, `L = max(landed)`, `NL = T - L`, `weight = max(weight)`;
- `T` is the task's trial count for the design effect; `counts.confounded` is neither landing nor trial;
- the reported prior is the **lower bound** (runs assumed maximally overlapping). Report the upper bound (runs assumed
  disjoint: `L' = min(T, sum(landed))`, `NL' = T - L'`) beside it, per family, as
  `priors[family]["observation_bounds"] = {"lower": {...}, "upper": {...}}`.
- Not "conservative OR": the correct name is the lower bound of the OR under maximal overlap.
- Expected (to confirm with the tool): A15 lower Beta(2.14, 3.17) mean ≈ 0.40, upper Beta(2.71, 2.60) mean ≈ 0.51;
  A17 unchanged Beta(2.5705, 2.8544); A7 moves because its confounded run no longer counts as a non-landing.

## Q2 (supersedes F1-1) — rate units must match what the simulator draws

`channel_rate` counts one trial per unit of the channel's latent, per (revision, run):
- `member` latent: one trial per member (n = members, f = failed members) — current behaviour;
- `batch` latent: one trial per batch (n = batches, f = batches with at least one failed member);
- `run` latent and slots-only channels: one trial per run (n = 1, f = 1 if the channel failed in that run);
- controls: the rule's latent is the member latent unless declared otherwise (per-member trials, documented).
The design effect is over the task's distinct `(revision, run)` pairs in every case. `channel_report` reports, per
channel: the unit, n, f, n_eff and the rate at rho ∈ {0, 0.5, 1}.

## Q4 (supersedes M6-1) — exact conditional batch sampler

Before the first miss, batch i of B misses with probability `b / (1 - (1 - b)^(B - i + 1))`; after the first miss,
with probability `b`. No rejection loop. Planted test: at B = 34 and theta ∈ {0.3, 0.005}, compare the number of
missed batches with a zero-truncated Binomial(B, b) and each batch's marginal with `b / theta` (tolerances from the
Monte Carlo SE). State in the docstring and the report that every simulated run reuses r3's 34 brief batches.

## Q3 (supersedes the F1 wording) — replay labels and caveats

Variant A: "ledger-prior variant: mechanism priors from the shared ledger, which includes this task's revisions 10 and
13 (revision-held-out, not task-held-out); channel rates fitted on the four evaluated runs (in-sample)". Mark the
`rev14_replay_A_out_of_sample.*` artifacts and NOTES' "A out of sample" as superseded. Never carry "PARTIAL" into the
report: "criterion not met; descriptive only".
Caveats to add: (6) round-2 changes every variant's inputs, so re-run all variants with seeds 7-9 on the final tree
with the 20:14 criterion unchanged and show old and new side by side (a pass now is a third look, exploratory);
(7) B's 0/15 comes from r2 alone (r1/r3/r6 average ≈94.5 %, inside B's band) and B excludes r2's landings by
construction; (8) the observed 89.9 % is a 4-run mean while the band describes 6-run baselines — the bracket is not an
80 % coverage test (also simulate 4-run means); (9) state where C's 0.10/0.15/0.08 come from (if from these runs, C is
circular); (10) do not cite the superseded 7/15 C count (batches views silently equalled whole before the briefs fix).

## J1 (H1-9) — stated convention, known false negative

H1-9 stays as designed (attribute the class to r only when r's ablation reproduces the written class AND leaves every
other written column equal). Document it as a conservative convention that undercounts landings when an independent
slip sits in the same row; plant the verifier's case as a labelled known false negative; report every real key with a
class difference plus another differing column, before and after (including rev14 r2 SP-108/114 and rev13 run-4
SP-079). An absent column is unobserved, never "equal by default".

## J2 (G1 evidence) — the 12-run neutrality bar is necessary, not sufficient

Add to SA1: metamorphic planted cases on real payload shapes for each changed path, each with an expected-unchanged,
an expected-False and an expected-None case (split a description into replace + append; add an issue T-10 / ZOM-8010;
a readable register followed by an unreadable one; an unrelated share after the register). Report: the number of
`gradable:false` slots on the rev13 and rev14 surfaces (the audit says none); whether any real run names its issue in
a form the selector does not use (G1-7). Blind labels for the 9 reclassified tracker lines are not available in this
session: report them as an open item for the reviewer.

## J3 (claims wording) — applied

See claims_methodology.md: observation wording, A17 cancellation note (0.625 at rho = 0, 0.474 at rho = 0.5), the
criterion-2 view tagged [I] and shown to come from rho, B described as the current model under the zero-landing
assumption, "toward the observed average as expected by construction", and the post-hoc view subset labelled.

## Audit evidence (the three explore audits, consolidated)

Blast radius measured on the 12 real runs (rev13 7 runs + rev14 5 runs), from the explore reports:
- G1-1: no `gradable:false` slot on either surface; self-test only. G1-2/3/4/7: neutral by absence of the trigger
  (tracker_events empty in all 12; one register candidate per run; one content update per run; every issue id exactly
  ZOM-801). G1-5: 9 tracker lines reclassify, none inside a count/entry section; S40/S46 counts unchanged. G1-6:
  neutral only with "exclude the pattern itself" (a naive resolution flips 7 cells: pre S43/S44, r1 S44, r3 S43/S44,
  r6 S43/S44). G1-8/9/10/11: neutral (0 slot changes); moving the "false" test to the plain body would flip S67/R30 in
  all 12. G1-1/2/3/4/7 real-file blast radius: 0.
- H1-1..H1-9: no real number moves except H1-7 slots-only channel provenance (rev14 r3/r6 go-rule 0 -> 1; both runs
  remain v3-invalid) and H1-2 (A15 and A7 priors; A17 unchanged). H1-9's naive version would land SP-039 (rejected);
  the conditional version leaves it pending.
- misc/F1: message_models and .strip() (no real run has an empty or padded label); oracle_kit golden (no real task
  declares base_route yet); F1 rate units (changes the rev14 replay channels: member counts for scale:groups/control,
  one per run for tool_surface); M6 exact sampler (replay batches change distributionally, 34 batches).

# F1 status (current, 2026-10-28, fourth revision)

**Engine implemented; acceptance complete for the 12 ids a shipped channel can exercise; the chain path is
unvalidated (f6 has no chain channel to exercise); replay FAIL withdrawn; no calibration.**

## Protocol (pre-registered manifest, seeds 1/2/3 at 20,000 baselines)

- `scripts/f1_protocol.py` emits **all 13 manifest ids** once per seed with a status in {PASS, FAIL, STUB, ABSENT},
  the statistic, target, n, z (or exact binomial p), SE and the result. An id can never pass without a statistic.
- Gate: **m = 39 tests**, familywise alpha 0.01, Bonferroni **z_crit = 3.6558**
  (`NormalDist().inv_cdf(1 - 0.01/(2*39))`). m is fixed by the manifest as 13 ids × 3 seeds; the statistical tests
  actually run are 13 per seed (11 z assertions + f5's two exact-binomial zero cells), so m = 39 and the familywise
  error is NOMINALLY controlled at alpha (Bonferroni on normal tails, exact binomial for the zero cells; the normal
  tail is not a proven finite-sample bound). The gate is the 39 seed-level tests; the pooled comparisons are
  report-only and do not enter acceptance. f4, f8 and f10 are deterministic and use none of the alpha budget.
- **12 of 13 ids PASS at all three seeds** (36/36 seed-level tests) and pass pooled:
  f1_independent, f1_linked, f2_beta_n2, f3_scope, f4_cancel, f5_joint, f7_e2e, f7_sd, f7_shared, f8_geometry,
  f9_mechanisms, f10_fail_closed (`logs/f1/protocol4/seed{1,2,3}/result.json`, `f1_acceptance/summary.json`,
  `logs/f1/f1_protocol4_summary.txt`).
- **f6_chain is ABSENT**: no chain channel ships in any solver (`oracle_kit` supports the kind; the rev14 wrapper
  declares only `scale:groups` and `tool_surface:register`). The id is reported ABSENT with that reason and never
  counts as a pass; the chain path is therefore **unvalidated**. If a task ships a chain channel, f6 becomes
  executable and the gate must be re-run.
- **f7_shared's mean has no power against its named defect** (q drawn once per baseline or per run both give
  E[average] = 0.75) and **no gated spread statistic exists** for that shared-uniform construction; f7_sd tests the SD
  gate under a POINT rate and does not cover q-per-run. This is a known coverage gap, recorded in the manifest and
  the assertion, not a claimed power check.
- **Production-path tests** (always run, all PASS): a counted `hf._rate_draw` proves the channel rate is drawn **once
  per six-run baseline** (14 draws for 7 baselines × 2 channels, not 84; 7 vs 42 per channel); a sampled member subset
  reaches the solver as the channel's degrade (`Outcomes.of({("degrade","slip:a"): {"A-01"}})` fails exactly S1; the
  full set fails S1 and S2); and a known sampled singleton passes through `simulate()` unchanged for BOTH a member-latent
  and a run-latent member-bearing channel, failing exactly S1 and reporting it (a deterministic guard on the slot
  report, not a sampled comparison). f5's marginal comparison with `simulate()` is a report-only diagnostic.

## Variance correction (recorded, no draw re-run)

The first fourth-revision run (`logs/f1/protocol4_raw_binomial/`) used a binomial SE at n = draws for every
assertion, and at n = draws×6 for f9. Six runs of one baseline **share the baseline-scoped rate** (the property the
production-path test asserts), so that SE is not the analytic variance: for f9 it overstates precision by 1.5x
(pooled z −4.39, a false FAIL); for f7_e2e it understates it. The run of record (`logs/f1/protocol4/`) uses the exact
per-baseline variance of each average-over-six-runs statistic (`VAR_PER_BASELINE` in `f1_protocol.py`; derivation in
the comment: f7_e2e 1/128, f7_shared 1/36, f9 independent 31/432, f9 correlated 1/12); every Bernoulli-style
assertion keeps the binomial SE. The statistics are **identical** between the two runs (13/13 ids per seed: same
hits, same phat); only the SE and z of f7_e2e, f7_shared and f9 change. No target changed and no draw was re-run to
move a result. Seeds 1/2/3 had already been run once before this correction, so the correction is post hoc and is
disclosed as such; it was derived from the construction, not fitted to the outcome.

## Provenance

- `control:process_findings` and `tool_surface:register` are **session-local audited pools** built from
  `F1_PROVENANCE_AUDIT.txt` (35 JSON lines, **28 unique records**: 15 control / 13 unique, 10 channel / 5 unique,
  10 verdict; no record carries an id, so the body is hashed): control Beta(1, 4) (n=3, f=0) and tool_surface
  Beta(2, 1) (n=1, f=1), replacing the former disclosed overrides Beta(1, 13) and Beta(3, 3).
  `scale:groups` has no eligible `node_verdicts` record and stays a disclosed override Beta(4, 266); the harness
  prints per channel whether its rate is pooled or overridden.
- The pools are **in-sample** (r3 is one of the judged baselines) and the three control members in one run count as
  three trials only because the design effect is computed over runs: a consistency check, not validation.
- The audited ledger contains only control and channel records, so it is used for the channel pools and the
  provenance report; the mechanism priors and every protocol assertion use explicit priors/fixtures, never that
  ledger.
- The **replay** (`f1_acceptance.py`) keeps its recorded disclosed overrides (Beta(1,13), Beta(3,3), Beta(4,266));
  it is not re-fitted, so its numbers are unchanged and are not comparable to the protocol's audited pools.

## Replay (advisory and diagnostic only)

B 0/15, C 4/6/6, A 1/15, r3 15/15. The original criterion is recorded FAIL and withdrawn by amendment
(`F1_ACCEPTANCE_AMENDMENT.md`); `scripts/f1_acceptance.py` reports it as ADVISORY and exits 0. No replacement
validation is supplied, no run is V3-valid, no calibration claim, and no replay-fitted estimate is used for task 1.

## Guards added with the protocol

- `parse_rate` refuses inf/nan/1e400/zero/negative parameters and any finite shape above `MAX_BETA_PARAM` (1e9): the
  former code accepted inf and hung in `betavariate`, and a finite 1e308 shape overflows that sampler's internal
  2*alpha and hangs too. f10 probes both positions of the pair form, the finite-large boundary and the tiny-shape
  boundary, and computes its verdict (22 checks).
- `channel_rate` refuses `counts` with `failed > n` or `n < 0`.
- A run-unit rate is never adopted member-by-member: a channel with members and no declared latent refuses it.
- An all-dropped channel stays UNPARAMETERIZED with its exclusion reasons, never simulated at zero.
- `--summarize` REVALIDATES every saved assertion from its hits, n, canonical target, analytic variance and full cell
  set under the current manifest gate: a cached status, pass, z or SE is never trusted, and a materially altered
  result cannot be summarized into acceptance.
- The production-path checks are part of the gate: all three (one rate draw per baseline; subset-to-outcome mapping;
  a sampled singleton passing through `simulate()` unchanged) must exist and pass in every seed, or the seed exit and
  `acceptance_complete` fail.
- `simulate` reports every slot (including slots that never fail, at 0) and the top-25 dict is presentation only.

# Round-1 methodology verdict (recorded from the verify tool output; the raw JSON was not written to disk)

verdict: FAIL · verified_by: openai/gpt-6.1-sol#max · fallbacks: anthropic/claude-opus-5-5#max (session turn exceeded
its maximum hold time) · tier: methodology · bundle: logs/verify/bundle_methodology.txt

Judged: C1 H2 priors, C2a simulator fixtures, C2b revision-14 replay, C3 M6 batches. Summary of the verdict:
- The failed F1 acceptance result is reported correctly; the failure alone is not a reason to reject.
- Monte Carlo tolerances are adequate (≈4-7 SE for the supplied tests); the Beta-integrated test has one rate shared
  by six runs, still covered by 0.03.
- The H2 design-effect arithmetic is right and internally consistent (deff over unweighted trials; rho = 1 ⇒ one trial
  × weight; A17 contributions 0.9677 + 0.8571 + 1.6 = 3.4249; before Beta(15,17) ⇒ 30; after 3.4249).
Required corrections:
1. C1's categorical one-trial-per-(task, revision, run, family) claim was not implemented for aggregate observations
   (12 trials for two rules over the same six runs). Either restrict the claim or fix the path, and supply the A17
   record-level table and the falsification output.
2. "out-of-sample" for variant A is unsupported (in-sample channel rates; the ledger contains season_pass evidence);
   rename to "ledger-prior variant with in-sample channel rates" unless provenance establishes otherwise.
3. The historical "slips only" comparison needs a clearer scope (B adopts the zero-landing assumption; it does not
   reproduce the archived 95.1 % forecast, which included random class slips).
4. Channels do not improve agreement uniformly: scope "toward the observed runs" to B and C; A moves away.
5. The observed average is a 4-run mean while the band describes 6-run baselines; report that the bracket is not an
   80 % coverage test for a 4-run mean.
6. Supply untruncated fixture output (n, SE, tolerance per case); the shared-cause test asserts an ordering only.
7. C3: supply the 37 briefs / 34 batches evidence and the shards_for planted test; landing_rate_simulated counts the
   outer landing only; disclose or remove the rejection-sampler approximation.
8. Do not cite the superseded 7/15 C bracket count (batches views silently equalled whole before the briefs fix).

These corrections are applied in claims_methodology.md (A label, n_eff 1.82, B/C scoping, historical scope, sampler)
and in the round-2 design (observation collapse, exact sampler, replay re-run with seeds 7-9 on the final tree).

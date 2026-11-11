# 01b — Methodology review (difficulty-claim soundness) — scenario stage

Reviewer: GPT-6.1 Sol (`methodologist` subagent, session ses_e57ef5487ffenPmpF7WVqUfFe6), independent of the Claude
build lane. Read-only; independent arithmetic/sensitivity (20,000 six-run cohorts/case, 3 seeds reproduced the headline
at 0.511–0.520). **GO/NO-GO: NO-GO — insufficiently robust methodology to expect the real baseline gates to hold.**
**VERDICT: FAIL.**

This is the second of the two independent reviews the recorded RED TEAM FALLBACK (design §17) stands on; the first is
the adversarial pass in `01b_Redteam_Review.md`. Full text in the session transcript; findings and dispositions below.

## Findings and dispositions

| # | Sev | Finding (abridged) | Disposition |
|---|---|---|---|
| M1 | Major | One mechanism (`R_TECH_HOLD`) is assigned causally different failures (under-holding leagues vs over-holding Quests/Daily Login); loses 18/102 from one mechanism, contradicting the "≤15% per discovery" claim. | **ACCEPT — DONE** (same as red-team F3). Corrected attributions; re-forecast independent P(all)=0.500, correlated 0.580. Will correct the "≤15%" prose (scope is now the heaviest discovery at ~22%). |
| M2 | Major | 36/102 points rest on `Beta(1,1)=0.50` priors (A11 withdrawal, A19 lock, A3 review-flags, A13 quest-set) — **assumed, not measured** difficulty. At a 10% miss rate those four give E[avg] 79.1% (fails the 77% target), independent P(all)≈0.37. | **ACCEPT (core caution).** Keep the UNCALIBRATED label; publish pessimistic sensitivity cases in the self-review; do NOT read the flat prior as demonstrated hardness. This is the central reason the design is **borderline** and the key input to the direction decision below. |
| M3 | Major | The difficulty is retrieval-dependent; once the 3 carriers (review-flags 13pts, withdrawal 10pts, done-deploy 8pts) are retrieved, a thorough Opus may reconcile them → if all else solved, even mean miss rates give 86.1% E[avg]. Old 19-slot/67-wt geometry doesn't validate the 28-slot/102-wt surface. | **ACCEPT.** Binding risk = a strong/thorough Opus. Hardening (if chosen) must add reconciliation that survives complete retrieval, not concealment or weight inflation. The ultimate answer is the baseline, not this forecast. |
| M4 | Major | The joint pass is fragile: independent P(all)=0.50 at the knife-edge; reconstructed six-run SD ≈ 0.103 (≈52% of cohorts meet the 0.10–0.30 band); the `source` scenario doesn't test shared physical sources (every rule has a distinct `source` id); the real pattern gate is "largest pattern ≤ 50%", not just "≥ 2 patterns". | **ACCEPT.** Report each gate separately in the self-review; treat the SD band as the fragile gate; group genuinely shared retrieval sources when reasoning about diversity. Reinforces "borderline/fragile". |
| M5 | Major | Exceptions are authorized, but the *necessary-call lower bound* isn't established: dropping the 22 review-list calls → 112 (< both floors); notification mirrors another shortcut. | **PARTIAL ACCEPT** (same as red-team F6). Add the "no open review blocker" readiness clause to make the review reads necessary (certifying absence); recount; keep ≥130 honestly. Produce an efficient correct trajectory (the solver + pre-check, injection stage) to confirm counted calls. |
| M6 | Major | This is a design-stage forecast, not a result; no raw six-run Opus evidence, frozen protocol, 6×criterion matrix, counted-call reconciliation or score intervals. | **ACCEPT (inherent to the stage).** Hardness is measured at /create-difficulty (6 fresh unhinted Opus runs, frozen SQL/prompt/rubric/scorer, raw-preserving fairness corrections). Record the evidence-needed list for that stage; do not present simulation bands as empirical CIs. |
| M7 | Minor | Preregistration records hashes/seed 0/10k draws/cap 0.85/model, but omits full forecast JSON, invocation, dep versions, final SQL/solver; 550 assumed calls recorded. | **ACCEPT.** Archive the full forecast JSON + exact invocation + a frozen snapshot in the final pass; re-register after the corrected surface. |
| M8 | Minor | No actual temporal/prompt leakage established, but clearance is prospective (final seeds/prompt not yet written); the rulebook's proximity is a difficulty-neutralizer to watch. | **NOTE.** Planned seeds verified at the injection gate; the brief states rules, never a held/late beat — re-audit at prompt-writing for neutralization. |

## Methodologist's biggest risk to <85%
"A thorough Opus resolves the retrieval-dependent carriers, leaving too little genuine error weight; the forecast
currently relies substantially on unobserved 50%-mean priors and bundled failures." Matches the red-team conclusion.

---

## Round 2 — re-review of the hardened methodology (methodologist, ses_e579de9f3…) · GO/NO-GO: NO-GO as documented, repair the call-accounting first; "the forecast itself is now an honest, disclosed UNCALIBRATED scenario hypothesis worth testing."

| # | Finding | Disposition |
|---|---|---|
| 1 | Attribution repair sound; R_HOLD_SCOPE a distinct over-hold pattern (Beta(1,3)=0.25, not flat) | ACCEPT. Fixed the Zombie-Lane controls/decides metadata it flagged. |
| 2 | Four flat-prior mechanisms = 36/106 (34%); current-surface pessimistic ≈0.783/0.44 (not the old 0.79/0.37) | ACCEPT — FIXED. §18 corrected to 36/106 and ≈0.783/0.44 (≈0.825/0.35 at ×0.5); headline 0.658/0.520 reproduced. |
| 3 | 132/80 not a necessary floor (= redteam F4) | ACCEPT — FIXED. 128/79 honest; floor 128, requester re-confirmed. |
| 4 | SD is the fragile gate (~0.104); `source` scenario doesn't test shared physical sources | ACCEPT — documented §18. Over-hold raises joint pass 0.473→0.520, pattern-gate 0.986→0.992. |
| 5 | Exceptions legitimate; six-baseline measurement outstanding | ACCEPT (inherent to stage) — deferred to /create-difficulty. |

Biggest residual risk: a thorough Opus resolving the retrieval-dependent carriers (at 10% on the four flat mechanisms + scope/over-hold handled, E[avg] ≈ 0.854). Recorded as the binding risk; resolved at the baseline.

---

## Round 3 — re-review of the ENRICHED methodology (methodologist, ses_e56ff740e) · GO/NO-GO: NO-GO as documented, repair then run; "promising UNCALIBRATED scenario"

Independent sensitivity (150k six-run cohorts, seeds 17/41/89): design priors 0.6302 / P(all) 0.540; four-flat-at-10% 0.756 / 0.480; 0.5x 0.808 / 0.410. Dispositions:

| # | Finding | Disposition |
|---|---|---|
| 1 | R_INFRA_SCOPE bundles causally different mistakes across C01/C05/S07 | ACCEPT — FIXED. Narrowed to C01 (Plague Race) only; D11 addressables / ZOM-526 tokens are retrieval-context distractors, not graded. |
| 2 | "bigger haystack = 50% miss" is unsupported; flat priors 38/108 | ACCEPT — FIXED. Claim removed; §18 states more records can aid enumeration as much as burden it; tally ~33/108 (S11 single-route). |
| 3 | 130 floor doesn't depend on review reads (168 without); 150 "necessary" not defensible | ACCEPT. §18 reframed to workload estimate; floor confirmed at baseline. |
| 4 | R_INFRA_SCOPE vs R_HOLD_SCOPE share an over-conservatism latent; SD (0.106) is the binding gate | ACCEPT — documented; the two now flip DISJOINT beats (Plague Race vs Endless/ZL/SP). SD risk settled at baseline. |
| 5 | 48→decision ledger; don't manufacture columns | ACCEPT — dropped ZOM-484; kept honest restraint (R2/R11/R13 remain distractors, not columns). |
| 6 | S11 weight-5 sound; test alternative routes | ACCEPT — S11 single mechanism (AND-to-fail on the two routes). |

Honest post-repair forecast: E[avg] 0.660, P(all) 0.479 (independent) – 0.533 (correlated). Enrichment delivered length + honesty, not a difficulty increase (universe-capped). GO-worthy after repair; settled at /create-difficulty.

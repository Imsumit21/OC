# Revision 14 pre-registration: platform pre-check and six-run baseline (Opus 4.8)

> Written 2026-10-25, before any revision-14 run. Never edit this file. Its sha256 is recorded outside it, in the
> revision-14 handoff report and in `Task_Authoring/task_inputs/Working_Files/hardening_rev14/preregistration.sha256`.
>
> Evidence labels: **[O]** observed · **[D]** derived · **[I]** inference. Every forecast number below is
> **CONDITIONAL · UNCALIBRATED**: it is conditional on the assumed per-run landing rates p̂, which are theory-based,
> and no probe or run has calibrated them.

## 1. Frozen inputs
Paths are under `Task_Authoring/`. `Working_Files` is `task_inputs/Audit-Report/Working_Files`.

| Input | Path | sha256 |
|---|---|---|
| Revision-14 canonical SQL (with the local intake-marker line) | `task_inputs/01_Universe_Inject.sql` | `38781f13e65d09edd1d973ed009215f3270d0aa3ea40503b081b0ab5703471e0` |
| Revision-14 submission SQL (marker line removed only), for `/injection` and the platform | `task_inputs/Working_Files/01_Universe_Inject.comment-free.sql` | `b15b1102d4e99ee167a14101daf54b5e1a4bdd99d9f2c793fb9bb9928c8c3f8a` |
| Prompt, unchanged since revision 10 | `task_inputs/04_Prompt.txt` | `4f530d031be23b81defc5a44162e679861ed3be7fc9783a74963650f6ea05d55` |
| Final manifest | `task_inputs/Working_Files/01_Hardness_Manifest.json` | `d128687542ed5248b821831bd436d1dec10500da4f6e7d81acb663e964101210` |
| Draft manifest | `task_inputs/Working_Files/01_Hardness_Manifest.draft.json` | `b8cf71be9fa93bd6a0bbc6902d1b83018332a87b03e83f853dbdbc80a5f36d07` |
| Gradable surface (rubric blueprint, 71 slots, weight 255) | `task_inputs/Working_Files/01_Gradable_Surface.json` | `1fb8970f4cb6ae04402f6b4d525d5059ae543f4867513fe5825012a7fa1fe58b` |
| Oracle | `task_inputs/Working_Files/hardening_rev14/oracle.py` | `9bcfe650f52fb73868f34ff40cfdcbada41934e3587aa9241739b7028a2fea92` |
| Oracle dependency (prior solve, imported) | `task_inputs/Working_Files/hardening_analysis.py` | `43e098ea8c50c603f4e9bdaa222fdcb8a54e836a0b55502eb9be16db0977d5ef` |
| Oracle dependency (SQL parser, imported) | `tools/base_check.py` | `476901260b896fa6894fdce3ca98504a6752d31584e1b11e8d093b7bc29ebbe3` |
| Expected answers: READY 44 / WATCH 17 / HOLD 67 | `task_inputs/Working_Files/hardening_rev14/truth.json` | `412821ee4db3a7e1ed05ee02e02bef6f348f46640d4a3102c4e1fff355df2f94` |
| Forecast output | `task_inputs/Working_Files/hardening_rev14/forecast.json` | `70a1072bad97df6ecaf35673d83b28173e5d532557c67ce0d07ad29eee946ac7` |
| Forecast code | `task_inputs/Working_Files/hardening_rev14/forecast.py` | `b32638347626b033123af6654c2542153a343f04da6838c69ad58df66213e512` |
| Forecast design input (p̂, q, bases) | `task_inputs/Working_Files/hardening_rev14/design_B.json` | `118795b4912fe48c3932fe3a5754beb20b9fa27d45a015793f1dc94357042606` |
| Gate math (used by the forecast and the analysis) | `tools/difficulty_stats.py` | `933a550816f800a4c780d706b941ea2c626114577b8afb80eb77b23d3e0bab95` |
| Analysis entry point | `support/analysis/season_pass_runs_rev14.py` | `f3bc8ca8a9a161d1cb69de2dc865d26486084df3291a9a93ec9c1e521cc2691d` |
| Source interventions (not a model run) | `task_inputs/Working_Files/hardening_rev14/verification.json` | `4726b6ea58ca1ec6da4b615613fa72d160f58eb5e314738d01a149d122b531f7` |
| SQL builder | `task_inputs/Working_Files/hardening_rev14/build.py` | `ad20daacca1ad41e20893c7721dec2312e4e210b3619454b49d5d3e00a9be8d5` |

**Provenance.**
- The forecast and the surface both record SQL `38781f13…`, and the forecast records the surface sha256 `1fb8970f…`
  (checked 2026-10-25). **[O]**
- The entry point still reproduces revision 13 exactly on the frozen revision-13 inputs: per run 99.6, 91.6, 99.6,
  91.6, 79.7, 100.0 and 89.9 %, average 92.1 %, SD 0.068 (`hardening_rev14/rev13_check.recheck.json`). **[O]**
- With every revision-14 flag disabled, the oracle reproduces `hardening_rev12/truth.after.json` on the frozen
  revision-13 SQL with 0 field differences. **[O]**
- Stage gates on these bytes: scenario, injection, hardening, prompt-writing and prompt-check PASS (local; the pasted
  certificates in the stage artifacts). Model-provenance checks are N/A: V2 task on Opus 4.8. **[O]**

## 2. Design decision and deviations
- **Design B, the user's decision.** Designs A, B and C were built and forecast (`hardening_rev14/forecast_report.md`).
  None meets the session's §7.3 proceed conditions. On 2026-10-25 the user chose B ("go with B", "no probe go with
  theory", "go with best to get this task through"). So no probe ran, and every p̂ is theory-based. **[O]**
- **Proceed conditions missed by B.** At p̂: E[average] ≤ 62 % (B: 0.720 independent, 0.719 correlated); P(all four
  gates under both specs) ≥ 0.6 / ≥ 0.4 (B: 0.297 / 0.354). At 0.8 × p̂: E[average] < 70 % (B: 0.762). Met: every slot's
  all-fail probability ≤ 0.25 (max 0.179), and the structural all-fail check. **[D]**
- **Geometry deviation.** M1 carries 11.8 % of the surface weight, below the 12 % floor, because V3 sampling allows five
  spot checks plus one volume row. **[D]**
- **Corrections before certification.** Two of Owen Baker's note texts were fixed (SP-087 named a non-existent artifact
  prefix; SP-097's withdrawal gave a reason the records could not support), and the new #654 timeline events were put in
  time order. No value, rule or graded fact changed. **[O]**
- **Session deviation.** Earlier in this session some scratch files were briefly written under `/tmp` and then deleted;
  nothing outside `Task_Authoring/` is part of any frozen input. **[O]**

## 3. Mechanisms, p̂ and q
Per run: mechanism m is missed as a whole with probability p̂ ("lands"); otherwise each of its keys is missed
independently with probability q. Bases are in `design_B.json`.

| Mechanism | Deciding records | Graded facts | p̂ | q | Basis |
|---|---|---|---|---|---|
| M3 owner's final calls behind an explicit pointer (A14) | ZOM-801 description sentence; Arthur's comment `cmt_3f0ae94ca322f64d0929`; folder `d_d5a255766f6138166f7987` | SP-060, SP-116 HOLD (missing input); SP-089 READY; SP-111 WATCH; the folder; the Owner calls line; cascades | 0.30 | 0 | Every revision-13 run read the ZOM-801 description and none listed its comments **[O]**; the pointer is now in plain words, so landing needs the pointer skipped (about 0.1–0.2) or the calls dropped before the writes **[I]** |
| M1 value notes (A16) | Confluence `ver_page_season_pass_handoff_v5`; Owen Baker's six notes and four near-miss notes | five sampled members with both values; the exact count 6 | 0.45 | 0.10 | V7-T1: 5 of 6 Opus 4.8 runs resolved a conflict silently when asked to report it (Hardness_Mastery §11) **[O]**, discounted because Confluence is read in every run **[I]** |
| M2 process findings (A15, A6) | Control-tab Review history row; doc v2 delegation sentence; six review pairs; three controls | SP-030 WATCH; five sampled members listed; the exact count 6; READY/WATCH totals | 0.30 | 0.05 | V7-T1: 5 of 6 missed "CHANGES_REQUESTED then APPROVED" **[O]**, against 0 of 7 landings for this task's Control-tab review rules **[O]** |
| M4 confident claim met first (A1) | Robert's hub reply `C05433XK267/1771013700.000106` | SP-003, SP-005, SP-037, SP-083 HOLD; controls SP-009 READY, SP-019 HOLD; cascades | 0.15 | 0.05 | A1 pass@1 0 of 6 in the ML-selected task (model label uncertain) **[O]**, against 0 of 7 decoy and stale-summary landings on this task **[O]** |

## 4. Forecast model and output
**Model.**
- Base slips: N ~ Poisson(1) wrong register rows per run on random components, each changing the class with
  probability 0.5.
- The register is a native Sheet instead of a CSV at the revision-13 rate, 3/7.
- Exact oracle flips for every combination of whole-mechanism misses and for partial misses; aggregates (totals,
  group counts, key lists) are recomputed from each run's combined register.
- Two dependence scenarios: independent, and a Gaussian copula with latent ρ 0.3 between mechanism misses (achieved
  binary correlations 0.15–0.18).
- 5,000 six-run baselines per scenario through `difficulty_stats.compute()` under V2 and V3 Hard; seed 14.

**Output** (`forecast.json`), CONDITIONAL · UNCALIBRATED:

| Scenario | E[average] (10–90 %) | P(V3 avg < 70 %) | P(V2 avg < 75 %) | P(SD in band) | P(all four, V2) | P(all four, V3 Hard) | Max slot all-fail |
|---|---|---|---|---|---|---|---|
| independent, p̂ | 0.720 (0.641–0.799) | 0.365 | 0.684 | 0.772 | 0.547 | 0.297 | 0.177 (S46) |
| correlated, p̂ | 0.719 (0.624–0.810) | 0.382 | 0.660 | 0.864 | 0.601 | 0.354 | 0.179 (S46) |
| independent, 0.8 × p̂ | 0.762 (0.685–0.837) | 0.148 | 0.415 | 0.745 | 0.334 | 0.124 | 0.088 |
| correlated, 0.8 × p̂ | 0.762 (0.671–0.846) | 0.179 | 0.413 | 0.817 | 0.380 | 0.169 | 0.090 |

Pass@1 and failure-pattern gates hold in ≥ 99.7 % of simulated baselines. U, the largest achievable loss, is 0.702.
Break-even k for E[average] ≤ 70 %: 1.2 (independent), 1.1 (correlated); for ≤ 62 %: 1.6; no non-monotone step.

**Predicted gate outcome.** More likely than not to **fail** the V3 Hard average gate (P ≈ 0.63) and to **pass** all
four V2 gates (P ≈ 0.55–0.60). The binding gate is the six-run average. **[D]**

## 5. Scoring (fixed now)
- **Grading.** Run the entry point on each run's actual writes against `01_Gradable_Surface.json`. Its selectors are
  proxies; once the rubric and verifier exist, they are the grading of record. Anything that cannot be decoded
  deterministically is UNGRADED, never guessed, and coverage is reported.
- **Pre-check command** (workspace root):
  ```
  W=Task_Authoring/task_inputs/Working_Files
  python3 -I -B Task_Authoring/support/analysis/season_pass_runs_rev14.py \
    --sql Task_Authoring/task_inputs/01_Universe_Inject.sql --oracle-dir $W/hardening_rev14 \
    --slots $W/01_Gradable_Surface.json \
    --run pre=Task_Authoring/task_inputs/06_PreCheck_Trajectory/trajectory-run-1.json \
    --attribute owner_calls,value_notes,process_findings,claims,validation,receipt,review,journal,fixture_binding,acceptance,epoch_binding,history \
    --out $W/hardening_rev14/precheck_analysis.json
  ```
  For the baseline, add `--run r1=… --run r6=…` (all six; the V3 gate math rejects one to five baseline runs).
- **Gates.** `difficulty_stats.compute()` on the six baseline runs, under V2 and V3 Hard. Model provenance is reported
  separately: N/A: V2 task on Opus 4.8.
- **Mechanism landing.** A mechanism LANDED in a run if at least one of its graded facts fails and the entry point's
  attribution reproduces the difference by disabling that mechanism's flag, or (for the Owner calls line, the Value
  notes and Process findings lists, and the folder) the required item is absent. A landing is *whole* when all of the
  mechanism's direct facts fail together, otherwise *partial*. A mechanism whose deciding record never appears in the
  run's tool results is NOT-REACHED. A mechanism whose facts are all correct LEAKED.
- **Run validity.** A run with a `model_refusal_fallback` before the mechanism's decision is flagged; landings inside
  briefs written by the fallback model are reported but not counted as Opus 4.8 evidence (01a B0).

## 6. Predictions, made before any run
Each is a yes/no outcome with my confidence that it comes true. Score them with a Brier score after the runs.

| # | Prediction | Confidence | Basis |
|---|---|---|---|
| P1 | The pre-check lands at least one mechanism as a whole | 0.72 | **[D]** 0.771 independent, 0.678 correlated, from p̂ |
| P2 | The pre-check lands at least two mechanisms as a whole | 0.35 | **[D]** 0.347 independent, 0.354 correlated |
| P3 | Platform `/hardness` on the pre-check scores 3 or more | 0.60 | **[I]** Any whole landing is a wrong class, a missing required list or a misdirected save, i.e. consequential (P1); discounted for how `/hardness` weighs a single list |
| P4 | Six-run proxy average below 70 % (V3 Hard average gate) | 0.37 | **[D]** 0.365 / 0.382 |
| P5 | Six-run proxy average below 75 % (V2 average gate) | 0.67 | **[D]** 0.684 / 0.660 |
| P6 | All four V3 Hard gates pass on the proxy | 0.33 | **[D]** 0.297 / 0.354 |
| P7 | All four V2 gates pass on the proxy | 0.57 | **[D]** 0.547 / 0.601 |
| P8 | Per-run SD of the proxy scores in 0.10–0.30 | 0.82 | **[D]** 0.772 / 0.864 |
| P9 | M3 lands as a whole in at least one of the six baseline runs | 0.88 | **[D]** 1 − 0.7⁶ |
| P10 | M1 lands as a whole in at least one of the six baseline runs | 0.97 | **[D]** 1 − 0.55⁶ |
| P11 | M2 lands as a whole in at least one of the six baseline runs | 0.88 | **[D]** 1 − 0.7⁶ |
| P12 | M4 lands as a whole in at least one of the six baseline runs | 0.62 | **[D]** 1 − 0.85⁶ |
| P13 | Slot S46 (the exact Value notes count) does not fail in all six baseline runs | 0.82 | **[D]** P(all-fail) 0.177 / 0.179 |
| P14 | No mechanism lands as a whole in all six baseline runs | 0.99 | **[D]** largest p̂⁶ is 0.45⁶ = 0.008 |

## 7. After the runs
1. Score every prediction and report the Brier score.
2. Give each mechanism LANDED, LEAKED or NOT-REACHED per run, with event citations, and counter-read each landing for
   fairness, tool and run validity.
3. Recommend the baseline only if `/hardness` is 3 or more and at least two mechanisms landed genuinely; otherwise report
   why each one leaked and the smallest universe-side fix, and change nothing without the user's approval
   (Rev14_Session_Prompt.md §10).
4. Never tune the surface to the runs; only documented fairness or correctness repairs, re-graded.

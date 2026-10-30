# Revision 13 results: platform pre-check and six baseline runs

> Scored 2026-10-24 against `plans/Rev13_Preregistration.md` (sha256 `00f3de83…cabd`, unchanged). I wrote those
> predictions before seeing any of these runs; the runs themselves may already have been under way.
>
> **Run setup.** These are platform runs, not harness runs: Claude Code 2.1.280, cwd `/app`, SQL `f4f195a5…` (platform
> revision 26). Arm A therefore ran on the platform; arms B and C did not run.
>
> **Reference outputs** are in `task_inputs/Audit-Report/Working_Files/rev13_platform_runs/`: `probe_*.json`,
> `proxy_scores.json` and `attribution.json`. `probe_base-run-2.json` covers only 32 rows, because the probe doesn't read
> `gsheets_values_append`. `proxy_scores.json` has run-2's full register.
>
> Evidence labels as in the plan: **[O]** observed · **[D]** derived · **[I]** inference.

## 1. Verdict
Revision 13 is too easy for Opus 4.8.
- **Pre-check.** Platform `/hardness` gave score 2, HOLD (`Plateform_reports/6ad576cdef355e00e72cd8b2_1a_hardness.md`).
  **[O]**
- **Baseline.** Proxy grading of the six runs gives:
  - average 92.1 %;
  - per-run SD 0.068;
  - 1 of 6 full passes;
  - 5 failure patterns, the largest 20 %.

  The runs fail both V2 (< 75 %, SD ≥ 0.10) and V3 Hard (< 70 %) on the average and the spread. **[D]**
- **Proxy rubric.** The 49 retained rubric slots plus the 24 case facts from `hardening_rev12/coverage_plan.json`:
  73 slots, weight 237. They are encoded as `support/analysis/rev13_slots.json`, and
  `support/analysis/season_pass_runs.py` reproduces every number here.
  - Slots are graded from each run's actual writes, including delivery slots.
  - Unambiguous SHA prefixes count as matches.
  - Group-membership slots are compared with revision-13 truth.

## 2. Per run
| Run | Model | Counted calls | Cost | Register | Wrong rows | Class errors | Proxy | Cause of misses |
|---|---|---|---|---|---|---|---|---|
| Pre-check | Opus 4.8; Opus 5 wrote only the final summary | 578 | $167.96 | Sheet | 0 | 0 | 99.6 % | none |
| 1 | Opus 4.8 | 552 | $72.59 | CSV | 1 | 1 | 91.6 % | SP-043: receipt SHA written in the reviewed-artifact column |
| 2 | Opus 4.8 | 561 | $93.92 | Sheet | 0 | 0 | 99.6 % | none |
| 3 | mixed: Opus 5 main agent from event 987 | 553 | $189.97 | CSV | 3 | 1 | 91.6 % | billing history: SP-091/106/112 labels removed before the snapshot, reported as held |
| 4 | mixed: Opus 5 main agent from event 779 | 558 | $199.47 | CSV | 11 | 8 | 79.7 % | aborted- and diagnostic-run rule missing from Opus 5's briefs (10 keys); SP-079 wrong receipt |
| 5 | mixed: Opus 5 main agent from event 2,134 | 550 | $58.67 | CSV | 0 | 0 | 100 % | none (shortened, unambiguous SHAs) |
| 6 | Opus 4.8 | 558 | $68.78 | Sheet | 3 | 1 | 89.9 % | SP-037 acceptance epoch; SP-103/121 fields left blank |

All seven runs completed every write: reader share, slide, ZOM-801 append and state, Gmail reply to Arthur only, and the
Slack thread reply. **[O]**

## 3. Mechanisms
- **Landed, in one run each:**
  - **Aborted- and diagnostic-run rule:** run-4, 10 keys. The briefs that dropped it were written by the fallback model;
    the 12 briefs Opus 4.8 wrote stated it.
  - **Billing-label history at the snapshot:** run-3, 3 keys.
  - **Acceptance epoch:** run-6, 1 key (case H4). Its brief stated the rule.
- **Leaked in every run:** issue remap, own-package receipts, receipt journal (withdrawals, rollbacks, copies), fixture
  binding (combined and split), review lane, dismissal timing, ZOM-801 key lists, and the T39 export. None of the 55 rows
  where the export differs from truth appears in any register.
- **Never read:** ZOM-801 comments, in 0 of 7 runs.
- **Execution:** 3 of 7 runs delivered a native Sheet instead of a CSV, after the base64 upload failed or was avoided.

## 4. Pre-registration scorecard
| # | Prediction | Confidence | Outcome |
|---|---|---|---|
| P1 | Runs 2–7 fail V3 Hard | 0.90 | **True**: 92.1 %, SD 0.068 |
| P2 | Runs 2–7 fail V2 | 0.80 | **True** |
| P3 | No rule lands in 4 or more of 7 runs | 0.75 | **True**: at most 1 of 7 |
| P4 | T39 trusted in at most 2 of 7 runs | 0.65 | **True**: 0 of 7 |
| P5 | At least 3 of 7 runs have a landed rule | 0.60 | **True**: 3 (runs 3, 4, 6) |
| P6 | Partial landings come mostly from briefs that omit the rule | 0.60 | **False**: 1 of 3 (run-4); runs 3 and 6 had the rule in their briefs |
| P7 | Opus 5.5 lands no mechanism much more often | 0.70 | Not tested: arm C not run |
| P8 | Harness meets the calibration criterion | 0.60 | Not tested: arm B not run |

Brier score over the six scored predictions: 0.126. A constant 0.5 forecast scores 0.25.

## 5. Validity and evidence notes
- **Mixed-model runs.**
  - In runs 3, 4 and 5, a `model_refusal_fallback` event made `claude-opus-5[1m]` the main agent for the rest of the
    run. The event records `api_refusal_category: bio` and `scope: session`. Subagents stayed on Opus 4.8.
  - The pre-check had the same event, but only at the final summary.
  - No trigger is visible in the surrounding text. Under `01a` B0 these runs are complete but flagged, and run-4's
    landing is not Opus 4.8 evidence. **[O]**
- **Overwritten exports.** The revision-10 platform exports (the Oct 21 pre-check and the Oct 22 baseline) were replaced
  in `06_*` and `07_*`, and they aren't anywhere else on disk. Only their derived ledgers remain, in
  `Working_Files/hardening_rev11/`. **[O]**
- **File name.** The new pre-check is `06_PreCheck_Trajectory/trajectory-run-1.json`, but the stage and release gates
  look for `trajectory.json`. **[O]**
- **Stray file.** Run-2 left `__sp_probe_a.txt`, a test upload, in the destination folder. **[O]**

## 6. What this means
- **The plan holds.** This matches plan §15.6's row "Arm A fails and the rules leak as predicted": the diagnosis holds
  and the plan doesn't change.
- **Explicit rules don't create failures.** When Opus 4.8 runs uninterrupted, it executes them at about 99 % field
  accuracy, multi-step rules included. Adding more rules of this kind won't move the average. **[D]**
- **The gates need variance.** Mechanisms must land in some runs and not others, and each must carry real weight. **[D]**
  - A mechanism that lands in every run creates all-fail rows. The local tolerance is 0, and `/rubric` fails two or
    more.
  - A mechanism that never lands adds nothing.
- **The one measured blind spot** in this task is ZOM-801's comments: 0 of 7 runs read them. **[O]**

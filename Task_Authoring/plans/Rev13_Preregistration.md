# Revision 13 pre-registration: harness runs (test, calibration, model bridge)

> Written 2026-10-24, before any revision-13 harness run. Do not edit it after the first run starts; add corrections
> as a dated addendum at the end. Keep this file's sha256 somewhere outside it before running.
>
> Evidence labels as in the plan: **[O]** observed · **[D]** derived · **[I]** inference.

## 1. Frozen inputs
All paths are under `Task_Authoring/task_inputs/`.

| Input | Path | sha256 |
|---|---|---|
| Revision-13 SQL to apply in the harness: the bytes `/injection` and `/prompt` passed | `Audit-Report/Working_Files/01_Universe_Inject.comment-free.sql` | `f4f195a598ac0f36efd4acb5a4073de518024f171d5f1cc48b75d09d068dde2e` |
| Revision-13 canonical SQL (adds only the local intake-marker line) | `01_Universe_Inject.sql` | `fdfc7988e12bd6112dbe5b8961c2308c5227c41f742537f6da14155a5526ce40` |
| Prompt: the same bytes the platform baseline used | `04_Prompt.txt` | `4f530d031be23b81defc5a44162e679861ed3be7fc9783a74963650f6ea05d55` |
| Revision-13 final manifest | `Audit-Report/Working_Files/01_Hardness_Manifest.json` | `a46b9ec30eb13fb4fbeb87069ef61ee365d0a639099082ac0e3c447aa9a3a8a1` |
| Expected answers for revision 13: READY 50 / WATCH 11 / HOLD 67 | `Audit-Report/Working_Files/hardening_rev12/truth.after.json` | `f5cdbae57a5f7dfa89862d28b6c517d820c596cd1a0d9f61c890d826ec99c33d` |
| Proxy grading slots for revision 13: the retained rubric slots plus the 24 case facts | `Audit-Report/Working_Files/hardening_rev12/coverage_plan.json` | `382ae1e8564a6e07f7b1525e1cd12a607da7d4fcf56b744f71c7e299ad239a8d` |
| Calibration SQL: platform "revision 11" = local revision 10, the SQL of the platform baseline | `Audit-Report/Working_Files/hardening_rev11/before/01_Universe_Inject.comment-free.sql` | `a4a197db27724ca25c28d72be8bb73f369457401fd2a7cbe5d56adae2dd31ed1` |
| Expected answers for revision 10: READY 68 / WATCH 16 / HOLD 44 | `Audit-Report/Working_Files/hardening_rev11/truth.before.json` | `9e0bb39fc8d8719e985904919320f9172e9425b8c706b9fd7e4ff241391c092a` |
| Proxy grading slots for revision 10 | `Audit-Report/Working_Files/hardening_rev11/coverage_stress.json` | `4d50defb8fe2ea5ad4045d7f6437c02808042eac442a2f01c6690760def869e7` |

**Provenance.**
- **Revision 13.** `Plateform_reports/Latest_injection-report.md:14` and `Latest-prompt-report.md:22,41` both reviewed
  SQL `f4f195a5…`, and both reviews passed. **[O]**
- **Revision 13 expected answers.** `hardening_rev13/truth_preservation.json` reports 0 field differences from revision
  12's truth. **[O]**
- **Revision 10 SQL.** `02_hardness.md:19` and `01_OE_Report.md:8` record `a4a197db…`. `03_Injection.md:14` shows the
  next platform revision replacing it on Oct 24, so it was the platform's SQL across the Oct 22 baseline. **[D]**
- **Revision 10 expected answers.** Baseline runs 2–5 have no component-field differences from this truth
  (`Working_Files/01a_Hardening_Report.md:17-24`). **[O]**

## 2. Arms and storage
| Arm | SQL | Model | Runs | Purpose | Status |
|---|---|---|---|---|---|
| A | revision 13 | Opus 4.8 | 7: run 1 = pre-check, runs 2–7 = shadow baseline | the test; decides the Season Pass task | required |
| B | revision 10 | Opus 4.8 | 6 | harness calibration against the platform baseline on the same SQL | strongly recommended |
| C | revision 13 | Opus 5.5 | 7, same layout as A | model bridge for V3 / CB tasks | if your harness can run Opus 5.5 |

**Storage.** Never use `task_inputs/06_PreCheck_Trajectory/` or `07_Baseline_Trajectories/`: the implementation's
backtests read the platform exports there.
```
Task_Authoring/support/backtests/season_pass/runs/
  A_rev13_opus48/06_PreCheck_Trajectory/trajectory.json
  A_rev13_opus48/07_Baseline_Trajectories/trajectory-run-1.json … trajectory-run-6.json
  B_rev10_opus48/07_Baseline_Trajectories/trajectory-run-1.json … trajectory-run-6.json
  C_rev13_opus55/   same layout as A
  <arm>/run_info.json
```

Create the folders:
```sh
cd /Users/sumitkumar/Source/Outlier/OC/Task_Authoring/support/backtests/season_pass && mkdir -p runs/A_rev13_opus48/06_PreCheck_Trajectory runs/A_rev13_opus48/07_Baseline_Trajectories runs/B_rev10_opus48/07_Baseline_Trajectories runs/C_rev13_opus55/06_PreCheck_Trajectory runs/C_rev13_opus55/07_Baseline_Trajectories
```

**`run_info.json`, one per arm:**
```json
{"arm": "A", "harness": "<name>", "harness_version": "<version>", "model": "claude-opus-4-8",
 "sql_sha256": "<sha256 of the SQL actually applied>", "prompt_sha256": "4f530d03…",
 "settings": {"effort": "<value>", "subagents": "<allowed / off>"},
 "runs": [{"file": "06_PreCheck_Trajectory/trajectory.json", "started_utc": "…", "incident": null}]}
```

**Run rules:**
- Use fresh, independent sessions, with the same harness build and settings in every arm.
- Use the prompt text exactly as frozen. No hints.
- Export complete runs in the platform's format: the Claude Code stream-json event array, including the init event.
- Complete every run whatever the earlier runs show.
- Change nothing in section 1 until all arms finish.

## 3. Scoring (fixed now)
- **Grading.**
  - Decode each run's register and other writes.
  - Compare them with the arm's expected answers on its proxy slots.
  - Mark anything that can't be decoded deterministically UNGRADED, never guessed, and report coverage.
  - Once the rubric and verifier exist, they remain the grading of record.
- **Gates.** Run `difficulty_stats.compute()` on runs 2–7 of arms A and C, and on runs 1–6 of arm B.

  | View | Thresholds | Status |
  |---|---|---|
  | V2 | < 75 %, ≤ 3 full passes, SD 0.10–0.30, ≥ 2 patterns with the largest ≤ 50 %, either view blocks | This task's platform gate as you described it. To be confirmed |
  | V3 Hard | < 70 % corrected, < 5 full passes, same spread and pattern gates | Reported alongside V2 |

  Model provenance is reported separately: Opus 4.8 runs fail V3's Opus 5.5 requirement by design.
- **Mechanisms.**
  - For each run, record which rules' signature differences (the `differences` entries in the stress files) appear in
    its register.
  - A landed rule must have its deciding record in that run's tool results. Otherwise it is NOT-REACHED, or a tool
    defect.
- **Brief transmission.** For each landed rule, record whether it appears in the briefs of the subagents that handled
  the affected components.
- **Harness calibration (arm B).**
  - The harness counts as calibrated for this task if two things hold:
    - its proxy-graded average on revision 10 is within 10 points of the platform baseline's proxy-graded average on the
      same slots;
    - the same mechanisms land and leak as in the platform baseline.
  - If not, no harness result gates anything until the gap is explained.

## 4. Predictions, made before any run
Each prediction is a yes/no outcome with my confidence that it comes true. All are **[I]** unless a **[D]** basis is
given. Score them with a Brier score after the runs.

| # | Prediction | Confidence | Basis |
|---|---|---|---|
| P1 | Arm A runs 2–7 fail the V3 Hard gates | 0.90 | **[D]** Under the rev-12 stress model (whole-rule misses of the three rev-12 rules), 0 of 1,716 six-run combinations pass V3 Hard with either slot layout. Only T39 and partial misses are outside the model |
| P2 | Arm A runs 2–7 fail the V2 gates | 0.80 | **[D]** Same model: P(pass) is at most about 11 % with the 24 case slots (per-rule miss rate near 0.6), and under 1 % with the existing slots |
| P3 | No rule lands in 4 or more of arm A's 7 runs. The rules are validation, receipt withdrawal, review lane, fixture binding, journal, acceptance epoch, history, issue remap and snapshot labels | 0.75 | In the rev-10 baseline, explicit rules stated where the agent reads leaked 6/6 (T10, T15–17), and the remap and snapshot rules landed 1/6 |
| P4 | The T39 export is trusted in at most 2 of arm A's 7 runs. "Trusted" means at least 10 register values copied from it that contradict the governing records | 0.65 | It is a data dump with neutral headers, and the agent reads every record anyway: 93.6 % of calls are per-record reads |
| P5 | At least 3 of arm A's 7 runs have at least one landed rule | 0.60 | Roughly twice as many per-record rules as revision 10 must reach about 9 subagents. In revision 10, 2 of 6 runs had a landing |
| P6 | Where a rule lands on only part of the cohort, the affected subagents' briefs omit it in at least half of those cases | 0.60 | In rev-10 run 6, none of the 8 briefs carried the remap, and it was the only run that used the original issues |
| P7 | For every mechanism, arm C (Opus 5.5) lands it in at most 2 more runs than arm A (Opus 4.8) | 0.70 | Assumes the newer model is at least as capable on each mechanism. A violation marks a 5.5-specific lever |
| P8 | Arm B meets the calibration criterion in section 3 | 0.60 | Unknown harness. The main risks are the Claude Code version, subagent settings and search ranking |

## 5. After the runs
1. Score every prediction.
2. Apply the decision table in the plan (§15.6).
3. Record the results in the ledger with `source: independent-harness`, the model and the harness. Forecasts for
   revision 13 never use its own runs.

## Addenda
None yet.

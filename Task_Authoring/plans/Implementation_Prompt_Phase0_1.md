You are implementing Phases 0 and 1 of an approved plan in the HarmonyGames task-authoring bundle.

GOAL
Make the authoring skills produce tasks that Opus actually fails, validly, under the Hard gates: corrected six-run
average strictly below 70 %, per-run SD 0.10–0.30, at least 2 failure patterns with the largest at most 50 %, fewer
than 5 full passes. Cost is not a constraint; failure is the target.

WORKSPACE
Root: /Users/sumitkumar/Source/Outlier/OC. It contains Evals/, claude/, Task_Authoring/, HarmonyGames_GitHub/,
HarmonyGames_Gmail/ and HarmonyGames_Other_Services/. Run commands from this root.

READ FIRST, IN FULL, BEFORE WRITING CODE
1. Task_Authoring/plans/Fold_Hardening_Into_Scenario_And_Injection.md (revision 4). This is the source of truth.
   Implement section 10, Phases 0 and 1, exactly as specified in:
   - section 4: design;
   - section 4.2: what blocks and what is advisory;
   - section 5: forecast and geometry;
   - section 7: tool specs, including 7.9 (pre-check intake) and 7.10 (surface grader);
   - section 8: gate and spec changes;
   - section 14.7: the test protocol;
   - section 15: run order, Opus 4.8 vs Opus 5.5, and gates by spec version.
2. Task_Authoring/setup/GEN_EXECUTION.md: the write boundary (section 1), the numbers of record (section 3), the
   hardness targets (section 3a) and the stage gates (section 6b).
3. Playbooks in Task_Authoring/playbooks/: 01_Scenario_Design.md, 01_Universe_Injection.md, 01a_Hardening.md,
   09_Rubric_Writing.md, 12_Difficulty.md.
4. The SKILL.md files for create-scenario, create-injection, create-hardening and create-difficulty under
   Task_Authoring/skills/.
5. Task_Authoring/references/Hardness_Mastery.md (sections 0, 2.6 and 11) and
   Task_Authoring/references/Hardness_Manifest_Spec.md.
6. Task_Authoring/tools/: stage_gate.py, hardness_gate.py, difficulty_stats.py, base_check.py, persona_view.py,
   shortcut_probe.py, hg.py.

HARD CONSTRAINTS
- Write only inside Task_Authoring/.
  - Evals/, claude/ and the three HarmonyGames_* folders are read-only. Never run git inside them.
  - Never execute SQL. Never modify the base exports.
- Task_Authoring/task_inputs/ is an active task (Season Pass). Treat it as READ-ONLY fixtures.
  - Working_Files is a symlink to Task_Authoring/task_inputs/Audit-Report/Working_Files. Use that real path when a tool
    does not follow symlinks.
  - Write every derived backtest output under Task_Authoring/support/backtests/season_pass/.
- Keep /create-hardening. Do not run the removal checklist in section 9.
- Work additively. Add new tools and checks beside the existing ones, and change existing gate behaviour only as
  sections 4.2 and 8 specify.
  - Never weaken an existing gate or the extreme/normal profile floors (GEN_EXECUTION section 3a).
- Python stdlib only. Match the style of tools/hardness_gate.py and tools/difficulty_stats.py. Every new tool:
  - has --self-test and --task-dir;
  - is read-only on its inputs;
  - writes only to explicit output paths inside Task_Authoring/.
- One owner per interpretation. Reuse, never re-implement:
  - gate math: difficulty_stats.compute(), count_tool_calls(), parse_verifier();
  - SQL parsing: base_check.parse_sql();
  - ACL and universe access: tools/hg.py, persona_view.py, and shortcut_probe.py's SQL-overlay search.
- Never fabricate or estimate platform outputs.
  - Label every prediction UNCALIBRATED and advisory (section 4.2).
  - Season Pass backtests are development fixtures, not validation. Say so in every report.
- Never print or log API keys. Optional probes read PROBE_BASE_URL, PROBE_API_KEY and PROBE_MODEL from the environment
  only.
- Do not commit or push unless I ask. Leave changes in the working tree for review.
- If the plan and the code disagree, or a step needs a decision the plan does not make, stop and ask me. Do not silently
  change scope.

DECISIONS ALREADY MADE (DO NOT REOPEN)
1. Blind model probes are approved but optional. tools/judgment_probe.py can be deferred.
2. The empirical screen is my independent harness. For each new task I run 7 trajectories:
   - run 1 goes to 06_PreCheck_Trajectory/trajectory.json;
   - runs 2–7 go to 07_Baseline_Trajectories/trajectory-run-1.json through trajectory-run-6.json.
3. /create-hardening stays the single owner of MODE B forensics, rewired onto the shared tools. /create-scenario's S0r
   only consumes its output.
4. Blocking from day one:
   - the solver contract;
   - a written disposition for every mutation result;
   - geometry U <= 1 - cap;
   - verdict dispositions with revision binding;
   - red team ran, or an explicit fallback is recorded.

   Advisory, labelled UNCALIBRATED and pre-registered:
   - liveness flags (each needs a written disposition);
   - the forecast;
   - probes;
   - the pre-check intake.

MODELS AND SPEC VERSIONS (plan section 15)
- Season Pass is a V2 task run on Opus 4.8. The CBs' tasks are V3, run on Opus 5.5.
- Every ledger record carries model, harness (name and version) and source. Priors are computed per model; never pool
  across models.
- Cross-model use happens only through an explicit transfer record (section 15.4). Such forecasts print
  "TRANSFERRED · UNCALIBRATED".
- Gates follow the task's spec version:
  - V3: the difficulty_stats default view;
  - V2: its --legacy-v2 gates (< 75 %, at most 3 full passes, either view blocks).
- Report model provenance separately. A 4.8 run is never V3 evidence.
- Season Pass's 00_Task_Context.json says V3 / Hard / Opus 5.5. Until I confirm which gate the platform applies, report
  both views for it.

FIXTURES (updated 2026-10-24; all read-only)
- Revision 13: seven platform runs, Opus 4.8, SQL f4f195a5… (platform revision 26).
  - Use the frozen copy, Task_Authoring/support/backtests/season_pass/rev13/, verified by its SHA256SUMS. It holds the
    SQL, prompt, manifest, dossier, the seven runs and the reference outputs.
  - Do not use the task_inputs/ copies: a parallel session is building revision 14 there and will overwrite them.
  - The runs are runs/06_PreCheck_Trajectory/trajectory-run-1.json (pre-check) and
    runs/07_Baseline_Trajectories/trajectory-run-1.json … trajectory-run-6.json.
  - Scored in Task_Authoring/plans/Rev13_Results.md. The reference outputs your tools must reproduce are in
    reference/: probe_*.json, proxy_scores.json, attribution.json, attention_map.json.
  - probe_base-run-2.json covers only 32 rows (the probe ignores gsheets_values_append); proxy_scores.json has the full
    register.
  - Task_Authoring/support/analysis/season_pass_runs.py with rev13_slots.json reproduces every number in the results
    file. It is the interim reference implementation for surface_grader.py and the trajectory decoding: generalise it,
    don't fork its rules.
  - The frozen predictions are Task_Authoring/plans/Rev13_Preregistration.md. Never edit it.
- Revision 10: the platform exports were overwritten and are not on disk. Use only their derived ledgers in
  Working_Files/hardening_rev11/ (run-*.calls.json, *.ledger.md, *.writes.json, *.register.csv / *.register-rows.json,
  summary.json).
  - If I restore the raw exports, they will be under
    Task_Authoring/support/backtests/season_pass/runs/platform_rev10/.
- Harness arms A/B/C were not run. If I add harness runs later, they go under
  Task_Authoring/support/backtests/season_pass/runs/.
- Never write to task_inputs/06_PreCheck_Trajectory/ or task_inputs/07_Baseline_Trajectories/.

VERIFIED FACTS YOU CAN RELY ON
- Export format. Platform and harness exports are Claude Code stream-json event arrays:
  - an init event lists the tools (mcp__hg__* names) and the model;
  - assistant events carry tool_use blocks, and later events carry the matching tool_result blocks;
  - results are often JSON strings wrapped in {"result": ...} (see unpack() in Working_Files/hardening_intake.py);
  - large results may spill to files.
- Observed platform agent: Claude Code 2.1.280, claude-opus-4-8[1m]. About 550 counted calls per run, plus 9 to 105
  subagent (Agent) calls.
- Shapes your parsers must handle, all observed in the revision-13 runs:
  - registers written as a CSV through gdrive_create_file (base64), or as a native Sheet through gsheets_values_update
    plus gsheets_values_append;
  - ZOM-801 text sent either as "description" or as "patch": [{"op": "append", "text": …}];
  - several gslides_batch_update calls in one run;
  - artifact SHAs shortened to unambiguous prefixes;
  - group headings with their keys on the next line.
- Model fallback. A system event subtype "model_refusal_fallback" (api_refusal_category "bio", scope "session") makes
  claude-opus-5[1m] the main agent for the rest of a run; subagents stay on Opus 4.8. Seen in the pre-check (event
  5855, final summary only) and in runs 3, 4 and 5 (events 987, 779 and 2134). Record which model wrote each subagent
  brief.
- Across the 7 revision-10 exports (derived ledgers only) there are 3,891 MCP calls. Five per-record reads make up 93.6 %
  of them:
  linear_list_comments, github_get_pull_request_timeline, github_get_pull_request_reviews, github_get_issue_comments,
  github_pull_request_read.
- Subagent briefs that mention the issue remap, matched with the regex
  "control tab|control sheet|replacement issue|ZOM-80[2-5]" over Working_Files/hardening_rev11/run-*.calls.json:

  | Run | Briefs mentioning the remap |
  |---|---|
  | run-1 | 3/10 |
  | run-2 | 4/12 |
  | run-3 | 4/8 |
  | run-4 | 5/8 |
  | run-5 | 4/8 |
  | run-6 | 0/8 |
- difficulty_stats.compute(data) input:
  {"spec_version":"V3","difficulty_mode":"hard","task_type":"long-horizon","rubrics":[{"id","weight"}],
  "rollouts":[{"id","status":"completed","tool_calls":int,"results":{rubric_id: bool}}]}

  In out["gates"]:
  - the difficulty gates are pass_at_1, avg_weighted_pass_rate, per_rollout_sd and failure_patterns;
  - errored_runs, horizon and baseline_models are provenance gates.
- Ad hoc scripts to generalise, all under Working_Files/:
  - hardening_analysis.py, which provides solve(sql, new, disable);
  - hardening_intake.py;
  - hardening_rev11/precheck_probe.py;
  - hardening_rev11/coverage_stress.py, with its .json and .txt outputs;
  - hardening_rev12/oracle.py;
  - hardening_rev12/coverage.py, with coverage_plan.json (which records sql_sha256);
  - hardening_rev12/verify.py, with verification.json;
  - truth.before.json and truth.after.json, in both hardening_rev11/ and hardening_rev12/.
- SQL revisions:
  - revision 13 is support/backtests/season_pass/rev13/sql/01_Universe_Inject.sql (canonical fdfc7988…; submission
    copy 01_Universe_Inject.comment-free.sql, f4f195a5…). Its truth equals hardening_rev12/truth.after.json;
  - hardening_rev11/before/ holds revision 10, the SQL of the revision-10 platform baseline (comment-free a4a197db…).
    Its truth is hardening_rev11/truth.before.json;
  - hardening_rev12/before/ holds revision 11;
  - identify any other revision by the sql_sha256 recorded in a JSON output. If no stored SQL matches, report it and
    skip that check.
- Backtest ground truth: Working_Files/01a_Hardening_Report.md lines 55-69. The register:

  | Verdict | Nodes |
  |---|---|
  | FALSE | T1, T3, T5, T7, T8, T11, T12, T13 |
  | LEAKED 6/6 | T10, T15-17 |
  | CONFOUNDED | T20 |
  | LANDED | T4/T14 in run-1; T18/T19 in run-6 |

  Also Working_Files/12_difficulty_input.json: 59 rubric rows, 197 weight, raw average 84.69 %.
- Revision binding: each revision-13 run must bind to SQL f4f195a5… by content. The T39 export id
  f_ddbcc47ba64c9c00764727 appears in their results. The old revision-10 pre-check export no longer exists, so skip it.

WORK ORDER AND ACCEPTANCE CRITERIA
Before coding, reply with a short work plan (milestones mapped to plan sections) and wait for my OK.

Phase 0 — ownership merge and deterministic tools
1. tools/trajectory_ledger.py (section 7.7). Accept when, on the 7 revision-13 runs:
   - counted calls match difficulty_stats: 578, 552, 561, 553, 558, 550, 558 (pre-check, then runs 1–6);
   - decoded registers reproduce proxy_scores.json: 128 rows in every run, including run-2's appended rows;
   - every fallback event is found, and every call and subagent brief carries the model that made it;
   - ZOM-801 text is decoded from both "description" and "patch" writes.

   On the revision-10 derived ledgers (hardening_rev11/run-*.calls.json), the brief-transmission counts above are
   reproduced.
2. tools/hardness_ledger.py (section 7.6), seeded from the 01a register, Hardness_Mastery sections 11 and 0, and
   attribution.json for revision 13. Every seed is source-tagged. Revision-13 seeds carry source platform-precheck or
   platform-baseline and model claude-opus-4-8; runs 3–5 are flagged mixed-model with claude-opus-5. Accept when:
   - re-seeding is idempotent;
   - a conflicting record with the same id is rejected;
   - the priors query returns Beta parameters with their record ids.
3. tools/oracle_kit.py (section 7.1), plus the ported Season Pass solver as a reference fixture under
   support/backtests/season_pass/. Accept when it is deterministic and reproduces truth.before.json and
   truth.after.json on their SQL revisions.
4. tools/difficulty_mutation.py (section 7.2), plus the geometry bound U and L_max (section 5). Accept when it:
   - reproduces hardening_rev11/coverage_stress.json and hardening_rev12/coverage_plan.json exactly, on their SQL
     revisions;
   - reports U for revision 12.
5. tools/node_verdicts.py (section 7.7). Accept when, on the 7 revision-13 runs, it reproduces attribution.json with
   event citations:
   - run-4: the aborted- and diagnostic-run rule LANDED on 10 keys, flagged mixed-model, because the briefs that
     omitted the rule were written by claude-opus-5;
   - run-3: billing history LANDED on SP-091/106/112, flagged mixed-model;
   - run-6: acceptance epoch LANDED on SP-037, with the rule present in its brief;
   - run-1 SP-043 and run-4 SP-079 proposed as unattributed slips, never as a mechanism;
   - the T39 export LEAKED in 7 of 7 runs, and ZOM-801 comments NOT-READ in 7 of 7;
   - CONFOUNDED only ever flagged, never assigned.

   If the revision-10 raw exports are restored, also reproduce the 01a register (T4/T14 run-1, T18/T19 run-6, T20
   flagged).
6. The gradable-surface schema and its validator (section 4.3, and S6b in section 4.4).
7. Skill and spec edits:
   - playbook and SKILL.md edits (sections 2, 4.4, 4.5 and 4.6);
   - the new Hardness_Manifest_Spec fields;
   - MECHANISM_IDS += A22, A23 (section 8);
   - stage_gate.py check families, with good and bad fixtures;
   - updated self-test counts in GEN_EXECUTION.md.

   Accept when "python3 Task_Authoring/tools/stage_gate.py --self-test" and every tool's --self-test pass.

Phase 1 — advisory predictions and the test harness
8. tools/trap_liveness.py (section 7.3). Accept when, on hardening_rev11/before (revision 10), it flags at least 6 of
   the 8 FALSE nodes. Report every miss.
9. tools/hardness_forecast.py (section 5), with pre-registration records in the ledger and UNCALIBRATED labels. Accept
   when:
   - on revision 10, with Season Pass left out of the priors, P(all gates pass) < 0.2;
   - it reproduces the section 14.2 result: no six-run outcome passes all gates under the rev-12 stress model.
10. tools/surface_grader.py (section 7.10). Accept when, on the 7 revision-13 runs:
    - it reproduces proxy_scores.json slot by slot, or explains every difference;
    - it applies the same rules: unambiguous SHA prefixes match, membership slots are compared with the truth, and
      every slide update counts;
    - the gates give the six-run average 92.1 % and SD 0.068, failing under both V2 and V3 Hard.

    If the revision-10 raw exports are restored, also compare with 12_difficulty_input.json and list every disagreement.
    The platform verifier is known to have credited missing key lists in runs 3–5.
11. The pre-check intake (section 7.9), inside /create-hardening MODE B (pre-check).
12. A dry run of the section 14.7 protocol on revision 13:
    1. its design artifacts;
    2. a forecast frozen before you read any run output;
    3. the pre-check intake;
    4. the surface-graded six-run gates;
    5. a comparison report that reproduces Rev13_Results.md sections 2–4.

    Label it a wiring test, not validation: these results are already known.
13. Optional, only if everything above passes: tools/judgment_probe.py (section 7.4).
14. Model and spec-version handling (section 15). Accept when:
    - hardness_ledger.py rejects a record without model, harness or source;
    - hardness_forecast.py takes --model and refuses to mix models without a transfer record;
    - surface_grader.py and the gate step choose V2 or V3 from the task context, and print both for Season Pass.
15. Reproduce the pre-registration scorecard in Rev13_Results.md section 4 (P1–P6, Brier 0.126) with your tools, run
    from recorded file hashes. If I add harness runs for arms B or C, score P7 and P8 the same way.

FINAL REPORT
- Every file created or changed.
- Each acceptance criterion, with the exact command, its output and PASS or FAIL with numbers.
- Deviations from the plan, with reasons.
- Open issues.
- The exact commands I run for the section 14.7 test on a new task.

Use the plan's evidence labels: [O] observed, [D] derived, [I] inference. Never describe a backtest as validation.

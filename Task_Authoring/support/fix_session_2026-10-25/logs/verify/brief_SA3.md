# Brief SA3: forecast, oracle, labels (hardness_forecast, difficulty_mutation, oracle_kit, difficulty_stats)

Repository: /Users/sumitkumar/Source/Outlier/OC, bundle Task_Authoring/. You own exactly these files:
- Task_Authoring/tools/hardness_forecast.py
- Task_Authoring/tools/difficulty_mutation.py
- Task_Authoring/tools/oracle_kit.py
- Task_Authoring/tools/difficulty_stats.py
Do not edit any other file (not preflight_report.py, not the E2E driver, not the fixtures). If another file needs a
change, report it instead of making it.

Read first: Task_Authoring/support/fix_session_2026-10-25/logs/verify/design_round2.md (rows F1-1, F1-2, M6-1, M2-1,
M5-1, V1-1 and the shared interfaces) and logs/verify/round1/code_misc.md. Also read the current self-tests, because
every behaviour you change needs a planted case.

## Goal

- F1-1: `_rate_from_records` / `channel_rate` key a run on (revision, run), not run alone (two revisions both numbered
  run-1 currently collapse to R=1, so no design effect). Document the control-trial multiplicity explicitly and
  implement the methodologist's decision (see design Q2; if it says cluster formula, use
  deff = 1 + (mean members per run - 1) * rho for control records).
- F1-2: `--mechanisms` (forecast and exhaustive) and `difficulty_mutation geometry --mechanisms` refuse an element in
  `engine.channel_ops` with a clear error; the channel is reported as a channel, not a mechanism.
- M6-1: replace `_missed_batches`' rejection fallback with an exact conditional sampler (sample the batch set
  conditioned on at least one miss without rejections), or, if the methodologist accepts the bound, document it as a
  disclosed approximation. Keep the per-run landing probability exactly theta.
- M2-1: surface `U["bound_verdict"]` in the geometry check detail (preflight_report is not yours: report the one-line
  change needed there); `geometry_dispositions` treats a missing dispositions path as `{}`, not a traceback.
- M5-1: `oracle_kit.check_golden`: read every routed base id (even when some evidence ids are in the SQL index), fail
  when any routed id is absent after a complete scan, and fail on a non-zero `hg.py` exit or an incomplete scan (a
  routed record that cannot be read is not "unverified": it FAILs the blocking check). Unrouted evidence stays
  unverified. Update the docstring.
- V1-1: `message_models` collects an explicit-but-falsey model label (an assistant message with "model": "" or null
  must be UNKNOWN, not dropped); `model_id`/`classify_model` strip only the bracketed suffix (no general .strip()).

## Constraints

- Python 3 stdlib only. Never execute SQL. Frozen copies read-only. Never edit Task_Authoring/task_inputs/ or the
  shared ledger; never run git; never write a shared cache. Run every self-test ONLY as
  python3 -B Task_Authoring/tools/selftest_sandbox.py -- <tool>.py --self-test
  (from the workspace root); never run --self-test directly. oracle_kit's self-test auto-sandboxes; keep that.
- Keep the docstrings in step with the behaviour.
- Every fix gets a planted case; keep the summary lines accurate.

## Acceptance tests you must run and report

1. python3 -B Task_Authoring/tools/selftest_sandbox.py -- hardness_forecast.py --self-test
2. python3 -B Task_Authoring/tools/selftest_sandbox.py -- difficulty_mutation.py --self-test
3. python3 -B Task_Authoring/tools/selftest_sandbox.py -- oracle_kit.py --self-test
4. python3 -B Task_Authoring/tools/selftest_sandbox.py -- difficulty_stats.py --self-test
5. python3 -B Task_Authoring/tools/selftest_sandbox.py -- stage_gate.py --self-test  (127 cases must still pass;
   stage_gate consumes oracle_kit, difficulty_stats and difficulty_mutation)

## Report format (<= 60 lines)

- Files changed, finding ids implemented.
- Planted cases added (name + the failure it guards).
- Command outputs for acceptance 1-5 (the key line each).
- Any deviation, any cross-file need (e.g. the preflight_report one-liner), any disagreement with the audit/design.
- Labels [O]/[I].

# Brief SA1: grader fixes (surface_grader, gradable_surface, trajectory_ledger.table, build_fixtures)

Repository: /Users/sumitkumar/Source/Outlier/OC, bundle Task_Authoring/. You own exactly these files:
- Task_Authoring/tools/surface_grader.py
- Task_Authoring/tools/gradable_surface.py
- Task_Authoring/tools/trajectory_ledger.py (only table(), sheet_titles(), keyed_rows(), _col_index and their helpers)
- Task_Authoring/support/fixtures/surface_formats/build_fixtures.py
Do not edit any other file. If another file needs a change, report it instead of making it.

Read first: Task_Authoring/support/fix_session_2026-10-25/logs/verify/design_round2.md (your rows G1-1..G1-11 and
the shared interfaces) and Task_Authoring/support/fix_session_2026-10-25/logs/verify/round1/code_g1.md plus
redteam_grading.md (the findings). Also read the current surface_grader self-test (PLANTED_G1, _self_test) because
every behaviour you add needs a planted case, and the existing cases must keep passing except where the design says
they change.

## Goal

Implement G1-1..G1-11 exactly as the design states. Decisions already made (from the explore audit):
- G1-1: declared `gradable:false` slots join the gate matrix and the per-run score bounds as unknown cells; coverage
  stays metadata; `gradable_surface.from_revision14` must preserve a `gradable` flag. The existing self-test's
  `pass_at_1` value (currently "3/6") will become a bounds/INCOMPLETE form: update that assertion and add a planted
  case whose full-pass bounds disagree.
- G1-5: strict key-list grammar; the audit's 9 real lines change classification but none is in a count/entry section;
  the existing `_g1_bullet_key_list` result (4) must still hold.
- G1-6: resolve the expected pattern against known hashes EXCLUDING the pattern itself (the audit proved a naive
  resolution flips 7 real cells because the selector patterns themselves are in known_hex and one truth hash extends
  each 12-char pattern). Plant the audit's abbreviated-ambiguous case and keep `_g1_sha_prefix` {E:T,Y:F,W:F,Q:F}.
- G1-10: bind message_id/reply_all and thread_ts to the call's parameters; do NOT search the plain body for "false"
  (that would flip the delivery slots in all 12 runs).
- G1-11: use the decoded table's own file id / spreadsheet id; the share call must name it.

## Constraints

- Python 3 stdlib only. Never execute SQL. Frozen copies (support/backtests/season_pass/rev13, rev14) are read-only;
  never write into support/fixtures/surface_formats except through build_fixtures.py's own output files.
- Never edit Task_Authoring/task_inputs/, never run git, never write a shared cache (support/local_search,
  support/hardness_ledger). Run every self-test ONLY as:
  python3 -B Task_Authoring/tools/selftest_sandbox.py -- <tool>.py --self-test
  (from the workspace root). Never run a tool's --self-test directly.
- Keep the module docstrings in step with the behaviour (they are part of the deliverable).
- Every fix gets a planted case that fails under the old behaviour; extend PLANTED_G1 in surface_grader.py. Keep the
  self-test summary line accurate.

## Acceptance tests you must run and report

1. python3 -B Task_Authoring/tools/selftest_sandbox.py -- surface_grader.py --self-test
2. python3 -B Task_Authoring/tools/selftest_sandbox.py -- gradable_surface.py --self-test
3. python3 -B Task_Authoring/tools/selftest_sandbox.py -- trajectory_ledger.py --self-test
4. The frozen reproduction, which must show 0 differences / the exact failed-slot sets:
   S=Task_Authoring/support/backtests/season_pass; W=$S/rev13/working_files; F=Task_Authoring/support/fixtures/season_pass_rev13
   python3 -B Task_Authoring/tools/surface_grader.py --task-dir $F --truth $W/hardening_rev12/truth.after.json --compare $S/rev13/reference/proxy_scores.json --out /tmp/x.json
   (also with --solver $S/solver/solver.py --sql $F/01_Universe_Inject.sql instead of --truth)
   then the 5 rev14 runs (pre, r1, r2, r3, r6; --oracle-dir $S/rev14/working_files/hardening_rev14 --sql
   $S/rev14/sql/01_Universe_Inject.sql), output to a scratch path under Task_Authoring/support/scratch/ (never /tmp).
   Expected: 0 differences; V3 92.1 %, SD 0.068; rev14 failed sets exactly as in design_round2.md.
5. python3 -B Task_Authoring/support/fixtures/surface_formats/build_fixtures.py --check  (must rebuild byte-identical;
   if a real grading change is intended, the build must fail loudly rather than silently rewrite the fixtures — say so
   in your report).

## Report format (<= 60 lines)

- Files changed (one line each) and the finding ids implemented.
- Planted cases added (name + the failure it guards).
- Command outputs for acceptance 1-5 (the key line each).
- Any deviation from the design, any cross-file change you need, any place where the audit and the design disagree.
- Labels [O]/[I] where you state what you observed vs inferred.

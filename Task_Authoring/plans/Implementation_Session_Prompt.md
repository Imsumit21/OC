Read Task_Authoring/plans/Implementation_Prompt_Phase0_1.md in full and follow it. It names the plan
(Task_Authoring/plans/Fold_Hardening_Into_Scenario_And_Injection.md, revision 4) and holds the scope, the constraints
and the acceptance criteria. The instructions below are additions; where they conflict with that file, these win.

1. A parallel session is building Season Pass revision 14 in Task_Authoring/task_inputs/, using the existing tools,
   skills and playbooks. Until I tell you Season Pass is finished:
   - Build new tools in Task_Authoring/support/pending_tools/, not tools/. stage_gate.py hashes every tools/*.py into
     every certificate, so one new file there would invalidate revision 14's gates.
     - Locate the bundle by walking up to the folder that contains tools/difficulty_stats.py, so each tool works from
       both places.
     - --self-test must pass from pending_tools/.
   - Don't edit, rename or delete any existing file under Task_Authoring/.
   - Stage every edit to an existing file (stage_gate.py, hardness_gate.py, playbooks, skills, setup, references, Guide,
     README) as a complete proposed copy under Task_Authoring/support/pending_edits/, at the same relative path. List
     each one in pending_edits/README.md, with the reason and the tests it needs.
   - Criteria 7 and 11, and the parts of 12 that depend on them, are staged work now. Their acceptance runs later.
   - Until the move, a criterion naming tools/X.py means support/pending_tools/X.py.
   - Helper caches under support/local_search/ are shared with revision 14 and already built for this context.
     - Tools may create missing cache files there.
     - Don't delete, rebuild or refresh them, and don't run setup/local_search.py.
     - If a cache read fails, re-run the tool.
   - Run Python with -B throughout.
2. Fixtures: use only the frozen copy, Task_Authoring/support/backtests/season_pass/rev13/. Read its README.md and
   check its SHA256SUMS first. It now also holds:
   - the revision-10 grading chain (09_Rubrics.json, 10_Baseline_Verifier_Results.md, 12_difficulty_input.json and the
     rest);
   - the design artifacts;
   - copies of hardening_rev11/, hardening_rev12/, hardening_rev13/, injection_fix_20261024/ and hardening_analysis.py.

   Read nothing in task_inputs/ except Working_Files/hardening_intake.py, as text. Wherever the file names a
   Working_Files/ path, use the copy in rev13/working_files/. That includes the 01a register at lines 55–69 and
   12_difficulty_input.json.
3. Never run a historical script, not even the copies.
   - build.py, report.py, coverage.py, coverage_stress.py and verify.py write fixed paths and read the task's live SQL
     and rubric.
   - hardening_intake.py writes into hardening_rev11/ when imported.
   - Import only oracle.py, hardening_analysis.py and precheck_probe.py, with Task_Authoring/tools on sys.path, under
     python3 -B.
   - precheck_probe's CLI writes only inside task_inputs/, so call probe() as a library with the frozen SQL path.
   - Reproduce criterion 4's reference outputs with your own tools, comparing against the frozen files.
4. Outputs:
   - Write outputs under support/backtests/season_pass/, never inside rev13/.
   - If a check needs a task-shaped folder (stage-gate replay, criterion 12), assemble it by copying from rev13/ into
     support/fixtures/season_pass_rev13/.
   - Season Pass's pre-check is trajectory-run-1.json. Decision 2's trajectory.json applies to new tasks.
   - Criterion 12 is a retrospective wiring replay, because blindness can't be restored once you have read the runs.
     Its forecast uses only inputs that predate the revision-13 runs: the frozen design artifacts and
     Rev13_Preregistration.md. Say so in its report.
5. Build in this order, so revision 14's runs can be analysed with the new tools as early as possible:
   1. trajectory_ledger.py, node_verdicts.py, surface_grader.py, hardness_ledger.py;
   2. oracle_kit.py, difficulty_mutation.py and the geometry bound;
   3. trap_liveness.py and hardness_forecast.py.
6. Task_Authoring/support/analysis/season_pass_runs.py, with rev13_slots.json, is the tested reference for trajectory
   decoding and proxy grading: it reproduces Rev13_Results.md exactly, from the frozen copy alone. Port its logic
   rather than re-deriving it, and keep its outputs as regression fixtures. Don't edit it; the revision-14 session uses
   it.
7. When I say Season Pass is finished, in one step:
   - move pending_tools/ into tools/;
   - apply pending_edits/;
   - run every self-test;
   - complete criteria 7, 11 and 12.
8. Keep the work plan to one screen, and wait for my OK before coding, as the file says.

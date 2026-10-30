# Audit: fold-hardening Phases 0–1

You are auditing, not implementing. Another session built Phases 0 and 1 of the fold-hardening plan and reported every
acceptance criterion as PASS or STAGED. Establish independently:
- which of its claims are true;
- whether the tools do what the plan specifies;
- whether the staged move into `tools/` is safe.

Report what you find. Fix nothing.

## 0. Sources
- **Workspace.** The root is `/Users/sumitkumar/Source/Outlier/OC`. Read `Task_Authoring/setup/GEN_EXECUTION.md` §1
  first.
- **The contract.** Later documents win where they conflict:
  1. `Task_Authoring/plans/Fold_Hardening_Into_Scenario_And_Injection.md` (revision 4): the plan;
  2. `Task_Authoring/plans/Implementation_Prompt_Phase0_1.md`: scope, constraints, acceptance criteria 1–15;
  3. `Task_Authoring/plans/Implementation_Session_Prompt.md`: additions that override (2).
- **The claims.** `Task_Authoring/plans/Implementation_Phase0_1_Final_Report.md` is the session's final report,
  verbatim. Every sentence in it is a claim to check, not evidence.
- **The work, all under `Task_Authoring/`:**
  - `support/pending_tools/`: 10 tools;
  - `support/pending_edits/`: 16 staged copies of existing files, 5 new fixture files, `MANIFEST.json`, `README.md`,
    `apply_pending.py`, `check_staged_stage_gate.py`;
  - outputs under `support/backtests/season_pass/`, outside `rev13/`;
  - `support/fixtures/season_pass_rev13/`;
  - `support/hardness_ledger/ledger.jsonl`.
- **References the implementation did not write:**
  - the frozen `support/backtests/season_pass/rev13/` (`README.md`, and `SHA256SUMS` over 243 files);
  - `support/analysis/season_pass_runs.py` (sha256 `a6af913ea3d91706…`, modified 2026-10-24 22:26:19), with
    `rev13_slots.json` (`4a94b270afd3f29e…`) and its output `rev13_check.json` (`b2cbb57e3eb9e88d…`). It reproduces
    `plans/Rev13_Results.md`;
  - `plans/Rev13_Results.md` and `plans/Rev13_Preregistration.md`;
  - the live `tools/`, whose newest file is dated 2026-10-24 16:05:40.
- **Not the implementation's.** A session is working on Season Pass revision 14 right now. It owns:
  - everything in `task_inputs/`;
  - `plans/Rev14_*`;
  - `support/analysis/season_pass_runs_rev14.py` and `support/analysis/rev13_check.rev14.json`.

## 1. Rules
- **Write only in `Task_Authoring/support/audit/phase0_1/`.** Every re-run output goes there, never over the
  implementation's outputs. Don't write anywhere else, in particular not in `task_inputs/`, `tools/`, `plans/`,
  `support/pending_tools/`, `support/pending_edits/`, `support/backtests/`, `support/fixtures/`,
  `support/hardness_ledger/` or `support/analysis/`.
- **The move.** Never run `apply_pending.py --apply`. Read `apply_pending.py` first, and run its check-only mode only if
  the code shows that mode writes nothing.
- **Never run:**
  - the live `tools/stage_gate.py --self-test`, which deletes a scratch folder in the shared cache;
  - `setup/local_search.py`;
  - any historical script (`build.py`, `report.py`, `coverage*.py`, `verify.py`, `hardening_*.py`), not even from the
    copies.

  Never import `hardening_intake.py`.
- **The ledger.** Run ledger-writing commands (`seed`, `append`) only against a copy of `ledger.jsonl` in your folder.
  If a command can't be pointed at a copy, don't run it; audit it from the code.
- **Shared caches.** Don't delete, rebuild or refresh anything in `support/local_search/`. Record every file a run
  creates or re-stamps there.
- **Process.**
  - Use `python3 -B` for every run.
  - Never execute SQL, and never print API keys.
  - Never run git. Mark any claim that needs git UNVERIFIED and give the command I could run.
- **Load.** The revision-14 session shares this machine, so run the slow jobs (exhaustive enumeration, forecasts, the
  replay) one at a time.
  - If an output records a seed, re-run with that seed and require identical output.
  - If a full re-run would take more than about 30 minutes, run a reduced version and say so.
- **Labels.** Use [O] observed, [D] derived and [I] inference. A backtest is never validation.

## 2. Fingerprint first
- Before running anything, record path, size and sha256 for every file under `Task_Authoring/` except `task_inputs/`
  and your own folder.
- Do it again at the end and diff the two.
  - Explain every difference: your own runs, or the revision-14 session (its paths are listed in §0).
  - A difference you can't attribute is a finding.
- Check the frozen snapshot: `shasum -a 256 -c SHA256SUMS` in `rev13/` must report 243 OK.

## 3. Re-run every acceptance criterion
For each of criteria 1–15:
1. Reconstruct the exact command. Use the report's row, the tool's `--help`, and any command line recorded in the
   implementation's outputs.
2. Re-run it with outputs in your folder, and compare every number in the report's row with your output.
3. Check the evidence against the criterion's full text in `Implementation_Prompt_Phase0_1.md`. Does it meet the
   criterion, or only something narrower?
4. Give a verdict: CONFIRMED, DISCREPANCY (with numbers), PARTIAL, UNVERIFIED (say why) or STAGED (say what the move
   will test).

Cross-check against the independent references, not only against the implementation's own outputs:
- **Criteria 1 and 10.** Compare with `rev13_check.json` and `tools/difficulty_stats.count_tool_calls()`:
  - counted calls 578, 552, 561, 553, 558, 550 and 558;
  - per-run scores 99.6, 91.6, 99.6, 91.6, 79.7, 100.0 and 89.9 %;
  - average 92.1 %, SD 0.068.
- **Criterion 3.** Compare the truths by content with `rev13/working_files/hardening_rev11/truth.before.json` and
  `hardening_rev12/truth.after.json`, not just by the printed hash prefixes.
- **Criterion 4.** Run `cmp` yourself against the frozen `coverage_stress.json` and `coverage_plan.json`.
- **Criterion 5.** Compare with `rev13/reference/attribution.json` and Rev13_Results §3.
- **Criterion 9b.** Compare with the plan's §14.2 claim.
- **Criterion 15.** Compare P1–P6 and the Brier score with Rev13_Results §4 (Brier 0.126).

## 4. Is it real?
For every acceptance of the form "reproduces X":
- **Circularity.** Show from the code that the tool computes X from primary inputs (SQL, trajectories, manifests),
  and never reads X or anything derived from it outside an explicit compare step. Grep for reads of
  `proxy_scores.json`, `attribution.json`, `coverage_plan.json`, `coverage_stress.json`, `truth.*.json` and
  `Rev13_Results.md`.
- **Falsification.** On a scratch copy in your folder, plant one realistic change and confirm the output moves the
  right way, and only there:
  - change one register cell in a copy of a run → `trajectory_ledger` and `surface_grader` change that row and slot;
  - remove a fallback event → the model provenance changes;
  - change one seeded value in a copy of the SQL → the `oracle_kit` truth changes for that key's dependency closure
    only;
  - corrupt one planted defect's fixture → the self-test that claims to catch it fails.
- **Specificity.** For `trap_liveness`, count how many non-FALSE nodes it flags (LANDED, LEAKED, CONFOUNDED). If it
  flags nearly everything, criterion 8's "8 of 8" shows no discrimination; say so with numbers.
- **Self-tests.** For each tool's `--self-test`, and for `check_staged_stage_gate.py` (100 cases), list what is
  asserted. Flag tests that assert only "no exception", or that compare a value with itself. Confirm that the 13 planted
  defects (`gradable_surface`) and the 7 portfolio defects (`hardness_gate`) each fail when present.

## 5. Contract compliance (code review, with file:line evidence)
- **Tool shape.**
  - stdlib only;
  - `--self-test` and `--task-dir`;
  - read-only on inputs;
  - writes only to explicit paths inside `Task_Authoring/`;
  - self-tests use temp folders (your fingerprint diff checks this);
  - each tool finds the bundle by walking up, so it works from `pending_tools/` and from `tools/`.
- **One owner per interpretation.**
  - gate math through `difficulty_stats.compute()`, `count_tool_calls()` and `parse_verifier()`;
  - SQL through `base_check.parse_sql()`;
  - access through `hg.py`, `persona_view.py` and `shortcut_probe`.

  Flag every re-implementation.
- **Labels.**
  - every prediction is UNCALIBRATED and advisory;
  - backtests are labelled development fixtures;
  - a cross-model forecast is refused without a transfer record, and prints "TRANSFERRED · UNCALIBRATED" with one.
- **Ledger.**
  - Every record carries model, harness (name and version) and source.
  - Priors are per model and never pooled across models.
  - Check the counts (214 records: 198 seeds, 8 predictions, 6 outcomes, 2 retrospective forecasts).
  - Check that revision-13 seeds carry `claude-opus-4-8`, and that runs 3–5 are flagged mixed-model.
  - Assess open issue 6: within-run trials pooled as independent.
- **Spec versions.** Grades choose V2 or V3 from the task context and print both for Season Pass. An Opus 4.8 run is
  never V3 evidence.
- **The session-prompt additions:**
  - tools live in `pending_tools/`;
  - fixtures come only from the snapshot;
  - nothing in `task_inputs/` was read except `hardening_intake.py` as text: grep the outputs and code for
    `task_inputs/` paths;
  - no historical script was run: check `task_inputs/Audit-Report/Working_Files/hardening_rev1[123]/` for files
    modified after 2026-10-24 17:35;
  - `season_pass_runs.py` matches the hash in §0;
  - `tools/` is untouched:
    - for the staged files, compare the live hashes with each `base_sha256` in `pending_edits/MANIFEST.json`;
    - no other file in `tools/` may be newer than 2026-10-24 16:05:40.
- **Cache write.** The report says the live `persona_view.py` re-stamped `pv_gmail.json` and that its data is
  "identical to HEAD". That claim needs git, so mark it UNVERIFIED. Then check:
  - whether a stamp change makes `persona_view` rebuild the cache, which would put the live session at risk;
  - whether the staged self-tests or the move would do it again.

## 6. Staged edits and the move scripts
- **Diff and map.** Run `diff -u` on every staged copy against its live file. Map every hunk to the plan section that
  requires it (§2, §4.x, §5, §7, §8, §15), and list hunks with no basis in the plan.
- **No weakening.** Each of these is a finding unless §4.2 or §8 of the plan requires it:
  - a removed or relaxed check;
  - a lowered threshold;
  - a new skip or exemption path;
  - `block=False`;
  - a narrowed trigger.

  The GEN_EXECUTION §3a floors must be intact.
- **New blocking checks.** List each one with its trigger, and compare with the blocking list in §4.2: solver
  contract, a written disposition for every mutation result, geometry U ≤ 1 − cap, verdict dispositions with revision
  binding, red team run or fallback recorded. Anything else that blocks needed my decision; deviation 6 is one example.
- **Self-test counts.** GEN_EXECUTION's self-test counts must match the staged tests.
- **`apply_pending.py`.**
  - Does check-only write anything?
  - Does `--apply` verify base hashes, back up the live files, apply atomically and leave a way to undo?
  - What happens on a partial failure?
  - Is `MANIFEST.json` complete (21 files, 10 tools)?
- **`check_staged_stage_gate.py`.** Does it really run the staged `stage_gate.py` against the good and bad fixtures, in
  a temp folder? Do its 100 cases cover the new checks?

## 7. Deviations, open issues and criterion 9a
- **Deviations.** Classify each of the 12, citing the plan line it departs from:
  - (a) consistent with the plan's intent and needed;
  - (b) a scope or behaviour change that needed my decision, since the contract says stop and ask;
  - (c) should be reverted.
- **Open issues.** For each of the 10:
  - verify it, re-deriving any number;
  - rate its severity;
  - say whether it must be fixed before the move, before the next task, or can wait.

  Give open issue 10 (every task needs the new artifacts after the move) special weight.
- **Criterion 9a.** Read the plan's §5 and §14 and criterion 9's text, and recommend which scenario reading the
  criterion intends, citing the lines. Recommend; don't decide.

## 8. Generalization on revision 14 (read-only, report only)
The tools were developed and accepted on revision 13 alone. Revision 14's pre-check is the only data they haven't
seen.
- **Copy first.** Copy the revision-14 inputs the tools need into a task-shaped folder in your audit folder. Never
  move anything, and never write in `task_inputs/`. The inputs include:
  - SQL, prompt and assignment files;
  - `00_Task_Context.json` and the manifests;
  - `Working_Files/01_Gradable_Surface.json`;
  - `06_PreCheck_Trajectory/trajectory-run-1.json`.

  Where `plans/Rev14_Preregistration.md` records a hash, check the copy against it.
- **Run.** Run `trajectory_ledger` and `surface_grader` on the pre-check, and `node_verdicts` too if it can run without
  a new-format solver.
- **Compare.** If the revision-14 session has its own analysis (for example
  `Working_Files/hardening_rev14/precheck_analysis.json`), compare with it:
  - counted calls;
  - register rows and kind;
  - fallbacks;
  - ZOM-801 text;
  - slot results.
- **Classify.** Separate "format not supported yet" from "wrong result".
- **Key locality.** Open issue 5 says the revision-13 solver is not key-local (the report names SP-020, SP-033, SP-047
  and SP-063). If `hardening_rev14/` holds a forecast, check whether it composes per-key partial misses instead of
  solving each combination exactly.

Send nothing to the revision-14 session; report it to me.

## 9. Move impact
- **Season Pass in flight.** What would `apply_pending.py --apply` do to Season Pass while revision 14 is under way?
  - which certificates go stale (the gate-policy hash covers every `tools/*.py`);
  - which new artifacts each gate would then require (open issue 10);
  - whether Season Pass could still be certified after the move without rework.
- **Other tasks.** Find every other task folder with stage certificates in this workspace (outside `task_inputs/` and
  the examples), and say what the move breaks for each.
- **Before the move.** State the preconditions you would require, and a rollback procedure.

## 10. Report
Write `Task_Authoring/support/audit/phase0_1/AUDIT_REPORT.md`, then reply with:
1. **Verdict**, in one paragraph: READY TO MOVE once Season Pass is finished, READY AFTER FIXES, or NOT READY.
2. **Findings**, ranked blocking, high, medium, low. Each has its evidence (file:line, command, numbers) and the
   smallest fix.
3. **The criterion table:** each claim, your re-run, and the verdict.
4. **Deviations and open issues**, as classified, with the 9a recommendation.
5. **Generalization results** on revision 14.
6. **Move impact**, with preconditions and rollback.
7. **The fingerprint diff**, explained.
8. **Every command you ran**, and every file you wrote.

Before you finish, ask the oracle subagent to challenge your verdict and your three most severe findings. Include its
objections and your answers.

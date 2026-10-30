# Implementation Phases 0–1: final report (verbatim)

Pasted by the user on 2026-10-25 from the implementation session's final message. It is kept verbatim as the claims
under audit; it is not evidence. In the source, the paragraph "What the replay shows" ends mid-sentence ("… agreed with
the outcome. I").

```text
I have the full inventory. This was a long task, so here is the whole final report in the format you asked for. I'll keep it as tight as the detail allows.
Fold-hardening Phases 0–1: final report
Phases 0 and 1 are built, and all ten new tools pass their self-tests. Every edit to an existing file is staged, the move into tools/ is one command, and nothing in tools/ or task_inputs/ was touched. Everything below uses the Season Pass backtests, which are development fixtures, not validation: they prove the tools connect, not that they predict. Nothing is committed.
One question for you is at the end (criterion 9a).
Files created or changed
All files are under Task_Authoring/.
- New tools (support/pending_tools/, 10): trajectory_ledger, gradable_surface, surface_grader, hardness_ledger, oracle_kit, node_verdicts, difficulty_mutation, trap_liveness, hardness_forecast (forecast, exhaustive, score, compare) and preflight_report.
- Staged edits (support/pending_edits/): complete copies of 16 existing files.
- tools/stage_gate.py, tools/hardness_gate.py
- references/Hardness_Manifest_Spec.md
- the playbooks 01, 01_Universe_Injection, 01a, 09 and 12
- the four SKILL.md files, setup/GEN_EXECUTION.md, the Guide, and README.md (staged as _root/README.md)
- bad/cases.json
- New fixture files (also staged): five good-fixture files (surface, solver, dispositions, preflight .json and .md).
- Move support (not applied): MANIFEST.json, apply_pending.py, check_staged_stage_gate.py, and the index README.md.
- Outputs and fixtures:
- support/backtests/season_pass/ outside rev13/: solver/, mutation/, forecast/, liveness/, prereg/, verdicts/, grading/, surface/, run_forensics/, trajectory_ledger/, and replay/ (with REPLAY.md)
- support/fixtures/season_pass_rev13/: a task-shaped copy
- support/hardness_ledger/ledger.jsonl: 214 records, being 198 seeds, 8 predictions, 6 outcomes and 2 retrospective forecasts
- Not touched: tools/ (no source changed after 2026-10-24 16:05), task_inputs/, and the frozen rev13/ copy (SHA256SUMS: 0 failures over 243 files).
- One shared-cache write: the live persona_view.py, called during the staged gate self-test, re-stamped support/local_search/cache/pv_gmail.json. Its data is identical to HEAD; only _meta.built_utc and the source stamps changed. I deleted and rebuilt nothing.
Acceptance criteria
Variables: S=Task_Authoring/support/backtests/season_pass, W=$S/rev13/working_files, F=Task_Authoring/support/fixtures/season_pass_rev13, R12=$W/injection_fix_20261024/before/01_Universe_Inject.sql, P=Task_Authoring/support/pending_tools. All runs use python3 -B.
#	Command (abridged)	Result	Verdict
1	$P/trajectory_ledger.py --task-dir $F --sql rev13=… --out-dir $S/trajectory_ledger/rev13, plus --derived on hardening_rev11/*.calls.json with the remap --brief-regex	Counted calls 578/552/561/553/558/550/558; 128 rows in every run, run-2's appended rows included; fallbacks 5855/987/779/2134 found; every brief carries its writer model; ZOM-801 decoded from description (pre-check, runs 1–2) and patch (runs 3–6). Rev10: remap briefs 3/10, 4/12, 4/8, 5/8, 4/8, 0/8; 3,891 MCP calls over 54 tools; 911/911/781/781/259 (93.6 %); 62 Agent calls [O]	PASS
2	$P/hardness_ledger.py seed --season-pass $S/rev13; priors --model claude-opus-4-8 --exclude-task season_pass --family A17	Re-seed adds 0, 198 already present; a conflicting record is rejected (self-test); A17 is Beta(14, 6) with ids hev_60d93123c00ec34f and hev_6d1ca07557a0c7eb	PASS
3	$P/oracle_kit.py check --task-dir $F --solver $S/solver/solver.py --previous-sql $R12 --previous-truth …truth.after.json; truth per revision	Contract PASS (11 rules, deterministic); rev10 gives 9e0bb39f = truth.before.json; rev12 and rev13 give f5cdbae5 = truth.after.json	PASS
4	$P/difficulty_mutation.py stress/plan --spec … piped to cmp; geometry --sql $R12 --layout coverage_plan.json [--with-cases]	Both reproductions byte-identical (4d50defb…, 382ae1e8…). Rev12 U = 107/147 = 0.728 (existing slots) and 197/237 = 0.831 (with the 24 case facts); L_max 0.340 / 0.363 (WARN)	PASS
5	$P/node_verdicts.py --task-dir $F … --reference $S/rev13/reference/attribution.json	0 differences. run-4 validation LANDED on 10 keys, flagged mixed-model; run-3 billing labels on SP-091/106/112, flagged; run-6 SP-037 with the rule in its brief; SP-043 and SP-079 proposed as slips; T39 export LEAKED 7/7; ZOM-801 comments NOT-READ 7/7; CONFOUNDED only ever flagged	PASS
6	$P/gradable_surface.py --self-test; validate	Self-test ok (13 planted defects). The Season Pass surface fails sampling.limit (13 samples in one group), which is a finding about the proxy rubric	PASS
7	support/pending_edits/check_staged_stage_gate.py; every tool's --self-test	100 cases ok. The full hardness_gate.py --self-test reads base data, so it runs at the move; its in-process portfolio test catches 7 defects	STAGED; accepted at the move
8	$P/trap_liveness.py --manifest …hardening_rev11/before/… --verdicts $S/liveness/rev10_register_verdicts.json	8 of 8 FALSE nodes flagged, none missed	PASS (with a specificity issue, below)
9a	$P/hardness_forecast.py forecast … --exclude-task season_pass on rev10	P(all gates): V2 0.039–0.255, V3 0.003–0.231. Under 0.2 in 10 of 12 scenarios; the independent-whole and source-whole scenarios give 0.255 (V2) and 0.231 (V3)	depends on the scenario; see the question
9b	exhaustive --mechanisms fixture_binding,journal,acceptance	0 of 1,716 six-run outcomes pass V3 Hard, on both layouts	PASS
10	$P/surface_grader.py --task-dir $F --compare proxy_scores.json	0 slot differences; six-run average 92.1 %, SD 0.068; fails both V2 and V3 Hard	PASS
11	Pre-check intake, written into 01a MODE B (pre-check)	Ran on rev13 in the replay: bound to rev13, all mechanisms LEAKED, 99.6 %, call no-go	STAGED; ran end to end
12	$S/replay/REPLAY.md (prior forecast → intake → graded gates → compare)	All 7 per-run rows of Rev13_Results §2 exact (calls, cost, register, wrong rows, class errors, score); §3 and §4 reproduced	PASS as a wiring test
13	judgment_probe.py	Not built (optional)	—
14	ledger self-test; forecast --model claude-opus-5-5 --from-model claude-opus-4-8	A record without model, harness or source is rejected. The cross-model forecast is refused: "no transfer record". The grades print both V2 and V3	PASS
15	$P/hardness_forecast.py score --predictions $S/prereg/rev13_predictions.json	Hashes verified; P1–P6 = T, T, T, T, T, F; Brier 0.125833; P7 and P8 not tested	PASS
What the replay shows (a wiring test, not validation): the library priors overstate how often explicit-rule mechanisms land. Only 4 of 11 landing counts fall inside the prior forecast's 90 % intervals. The observed 92.1 % average falls inside the forecast band in 2 of 24 scenario-views. Both screens (the run-1 no-go call and the /hardness band of 2) agreed with the outcome. I
Deviations from the plan
 1. The solver is an injection output. Scenario declares the rules in mechanism_portfolio, rather than writing a solver skeleton. Otherwise injection would rewrite a scenario file and make the scenario certificate stale.
 2. Expected values and flipped_by go into the preflight report, not the surface (§4.3 says injection adds them to the surface). Same reason.
 3. surface.coverage is gate 17 in the rubric playbook, enforced through the existing §E box and validity.rubric, both tested on the fixture. §8 allows new gate checks only in scenario and injection.
 4. The revise checks copy st_hardening's run-step evidence and counter-reading minimum instead of taking them over, because decision 3 keeps that gate.
 5. Liveness rule placement checks every node on legacy manifests (the plan says A15 rules); with a portfolio, only A15 nodes are checked.
 6. Surface validation blocks at scenario. §4.2 doesn't list it; this was my choice.
 7. /create-hardening no longer writes SQL, following §2's owners (A6, B5–B6, gate 7). This is Phase 0 rewiring, not a §9 removal; I left the rest of the §9 reference list alone.
 8. Additions: compare and --freeze (both needed by §14.7), score reading difficulty_stats output, preflight_report.py, and the move script.
 9. Geometry U is now the per-record enumeration plus the exact whole-mechanism combinations. A key-locality check that skipped most configurations no longer licenses composition.
10. The rev13 replay used 1,000 draws (not 10,000) and --max-k 12 (not 8). The rev13 solver is not key-local, so every outcome is an exact full solve, which is slow.
11. references/mechanism_priors.json is generated at the move (write-priors), since writing it now would create a live file. The tools read the ledger directly.
12. The bundle README is staged as _root/README.md, because your index occupies pending_edits/README.md.
Open issues
 1. Criterion 9a's scenario (the question below).
 2. Liveness specificity is low. Flags also fire on LANDED nodes (T4, T18), on LEAKED nodes (T10, T15, T16) and on the CONFOUNDED T20.
 3. The receipt rule is EQUIVALENT (masked by the journal rule) and still needs a written disposition.
 4. P6 is False under both readings (text only: 1 of 3; text plus referenced file: 0 of 3).
 5. The rev13 solver is not key-local (two mismatches, on SP-020, SP-033, SP-047 and SP-063). The earlier rev13 "PASS" had checked only 4 of 36 configurations. Rev12 and rev10 are fully checked and clean, so those results stand.
 6. The ledger pools by family, so three A17 rules from one run count as three trials.
 7. Four rev13 runs auto-compacted (events 4872, 3134, 4029 and 3501); the tools flag this, and Rev13_Results doesn't mention it.
 8. Skipped for lack of data: the rev10 raw exports are missing, so the optional parts of criteria 5 and 10 were skipped; changes.json (08641123…) matches no stored SQL.
 9. I didn't run the live stage_gate.py --self-test. It deletes a scratch folder under support/local_search/cache/; the staged checker uses a temp folder instead.
10. After the move, every task needs the new artifacts. The injection gate (and through it the hardening and release gates) requires the solver, the dispositions and a current preflight.
The move, when you say Season Pass is finished
python3 -B Task_Authoring/support/pending_edits/apply_pending.py           # check only (currently: ready, 21 files, 10 tools)
python3 -B Task_Authoring/support/pending_edits/apply_pending.py --apply   # refuses if any live file changed since staging
Then I run the printed self-tests and complete criteria 7, 11 and 12 with the tools/ paths.
The §14.7 test on a new task
The full version is staged in the Guide. Set T=Task_Authoring/task_inputs and R=$T/Working_Files/run_forensics/<rev>.
1. Freeze before any run:
python3 -B Task_Authoring/tools/oracle_kit.py truth --task-dir $T --out $T/Working_Files/solver/truth.json
python3 -B Task_Authoring/tools/hardness_forecast.py forecast --task-dir $T --model <model> --task <task> --harness <harness> --freeze $T/04_Prompt.txt --freeze $T/Working_Files/01_Hardness_Manifest.json --freeze $T/Working_Files/solver/truth.json --preregister --out $T/Working_Files/01c_Forecast.json
python3 -B Task_Authoring/tools/preflight_report.py --task-dir $T --forecast $T/Working_Files/01c_Forecast.json
2. Run the 7 trajectories. Run 1 goes to 06_PreCheck_Trajectory/trajectory.json; runs 2–7 go to 07_Baseline_Trajectories/trajectory-run-1.json through trajectory-run-6.json.
3. Run 1 only, before opening runs 2–7. Disposition the proposals and append them before the posterior forecast:
python3 -B Task_Authoring/tools/trajectory_ledger.py --task-dir $T --run precheck=$T/06_PreCheck_Trajectory/trajectory.json --sql <rev>=$T/01_Universe_Inject.sql --prompt $T/04_Prompt.txt --source independent-harness --harness <harness> --out-dir $R
python3 -B Task_Authoring/tools/node_verdicts.py --task-dir $T --run precheck=$T/06_PreCheck_Trajectory/trajectory.json --source independent-harness --task <task> --ledger-out $R/precheck.proposals.jsonl --out $R/precheck.node_verdicts.json
python3 -B Task_Authoring/tools/surface_grader.py --task-dir $T --run precheck=$T/06_PreCheck_Trajectory/trajectory.json --out $R/precheck.surface_grades.json
python3 -B Task_Authoring/tools/hardness_ledger.py append <dispositioned>.jsonl
python3 -B Task_Authoring/tools/hardness_forecast.py forecast --task-dir $T --model <model> --task <task> --harness <harness> --freeze $T/04_Prompt.txt --freeze $T/Working_Files/01_Hardness_Manifest.json --freeze $T/Working_Files/solver/truth.json --preregister --out $R/precheck.posterior_forecast.json
Write down the go / no-go call and the /hardness-style band (1–5) now.
4. Runs 2–7, then all seven together:
python3 -B Task_Authoring/tools/trajectory_ledger.py --task-dir $T --sql <rev>=$T/01_Universe_Inject.sql --prompt $T/04_Prompt.txt --source independent-harness --harness <harness> --out-dir $R
python3 -B Task_Authoring/tools/surface_grader.py --task-dir $T --out $R/surface_grades.json
python3 -B Task_Authoring/tools/node_verdicts.py --task-dir $T --source independent-harness --task <task> --ledger-out $R/proposals.jsonl --out $R/node_verdicts.json
python3 -B Task_Authoring/tools/hardness_forecast.py compare --forecast prior=$T/Working_Files/01c_Forecast.json --forecast posterior=$R/precheck.posterior_forecast.json --verdicts $R/node_verdicts.json --grades $R/surface_grades.json --precheck-call <go|no-go> --old-band <1-5> --out $R/comparison.json --md $R/comparison.md
Question
Criterion 9a asks for "P(all gates pass) < 0.2 on revision 10". It holds in 10 of 12 scenarios but not in the whole-rule independent and source scenarios (0.255 under V2, 0.231 under V3). Which scenario should the criterion be judged on: all of them, the shard scenarios that match how batch misses happen, or one you name?
```

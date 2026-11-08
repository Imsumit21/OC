# Design and Mode B implementation evidence

Implementation audit, 2026-11-08. No task evaluation clock applies; no active task inputs were changed.

Owner: design specialist. Changes: `tools/design_readiness.py`, `tools/mode_b_report.py`, and their isolated unit suites. The advisory `hardness_v2_check.py` and `difficulty_stats.py` scoring/grouping algorithms were not changed by this specialist.

## Design review interface

`design_readiness.evaluate(stage, manifest, surface, review, *, sql_text='', prompt='', rubric=None, builder_rubric=None, task_dir, task_id, revision, difficulty_mode)` returns PASS/FAIL, blockers, deferred items and the existing advisory helper report. `input_hashes(...)` generates the exact applicable input map. The assignment's canonical difficulty mode overrides any review declaration. Stages are scenario, injection, prompt, rubric and baseline; common writing/check aliases are supported.

The review is schema version 1 with `task_id`, `revision`, `stage`, `reviewer`, `difficulty_mode`, `input_hashes`, `diversity_channels`, `mechanisms` and `dispositions`. Each mechanism refers to manifest and surface IDs. It records evidence for the plausible answer, decider and chronology, discovery path, changed outcome, independence counterfactual, actual natural retrieval, readability and paired outcomes. Evidence is a reason plus `evidence: [{path, sha256}]`; paths must resolve inside the selected task and current bytes must match. The test fixture in `tools/test_design_readiness.py:fixture` is an executable schema example.

Scenario may defer materialization/readability and actual natural retrieval to injection. Inaccessible evidence always blocks. Later stages require resolution. Absence of a particular trap family is not a universal rejection: substantive, evidenced not-applicable dispositions are accepted. Generic “reviewed” waivers fail. Prompt-stage semantic review is separate from lexical leakage detection. Two paired outcomes must already exist on the surface, have different facts, trace to incorporated intent and include both independent-pass counterexamples. Work-kind weights remain fixed; selected difficulty channels cannot be routine volume or decoys. Rubric coverage preserves direct required outcomes; only repetitive sample roles can be sampled out. Baseline additionally compares the reviewed rubric with the builder export. Forecast probabilities remain advisory.

Review inputs are stage-specific: scenario hashes manifest/surface; injection adds SQL; prompt adds prompt; rubric adds rubric; baseline adds builder export. Prompt content uses the existing stage-gate certificate normalization. Semantic review remains a human evidence judgment; structural validation does not claim to prove semantics automatically.

## Mode B interface

`mode_b_report.from_request(request, task_dir)` consumes task-relative `data_path`, `trajectories`, optional `verifier` and `receipt`; plus `task_id`, `revision`, `bundle_hash`, `diagnoses`, `repairs`, `correction_evidence` and `precheck`. It verifies the current bundle and rejects paths outside the selected task. The coordinator gate additionally binds canonical task/revision context.

CLI: `python3 -B Task_Authoring/tools/mode_b_report.py --task-dir <task> --request <task>/Working_Files/mode_b_request.json --out <task>/Working_Files/mode_b_report.json`.

Baseline reports call the actual verifier/export binder and compare matrix results, completion status, counted calls and models with the bound raw exports. They generate every weight-5 row across six slots; preserve raw and separately justified corrections; and reuse `difficulty_stats.compute` for exact failure sets and transitive groups. Error slots retain null scores. Causal diagnosis cites a bound export hash and an actual event quote. Repairs specify evidence placement, changed outcomes, scope reason, preserved discovery, owner and reruns. A volume-only difficulty repair rejects; a documented missing-data/fairness repair can add necessary scope. Mode B proposes, without rewriting another stage's artifacts.

Precheck reports do not require a final rubric or platform verifier. A `PRECHECK_EXPORT_REVIEW` receipt binds schema version 1, task/revision/bundle, export SHA, source matrix SHA, reviewer and hashed evidence. Provisional surface rows may be supplied, or omitted. One-run reports are explicitly `PROVISIONAL_SINGLE_PRECHECK`, with no six-run statistics or inferred failure rate.

## Executed checks

- `python3 -B -m unittest discover -s Task_Authoring/tools -p test_hardness_v2_check.py`: 28 tests, OK, one existing live-task test skipped.
- `python3 -B -m unittest discover -s Task_Authoring/tools -p test_design_readiness.py`: 15 tests, PASS.
- `python3 -B -m unittest discover -s Task_Authoring/tools -p test_mode_b_report.py`: 8 tests, PASS.

Coverage includes valid early/later stages, deferred-now-required evidence, inaccessible evidence, generic waivers, advisory low forecast, stale source/prompt, unrequested/duplicate outcomes, inflated work-kind weights, core-write coverage, builder drift, assignment-mode drift, cross-task references, real binding, raw-matrix tampering, justified/unjustified corrections, absent event quotes, repair classification and no-rubric precheck.

## Existing forecast fixture defect

The coordinator's broad self-test reported two forecast-control failures. To distinguish these from regressions, the original `HEAD:Task_Authoring/tools/stage_gate.py` was loaded in memory with its original `__file__`, then its `_prepare`, `_apply` and `run_stage` ran the two cases against temporary fixtures. Both original cases returned nonblocking WARN for `forecast.preregistered`: the “preregistered control” expects PASS but depends on an absent shared-ledger fixture record. No stage-gate file was edited for this reproduction.

Exact reproduction command body:

```python
import sys, types, subprocess, tempfile, json
from pathlib import Path
sys.path.insert(0, str(Path('Task_Authoring/tools').resolve()))
m = types.ModuleType('stage_gate_original')
m.__file__ = str(Path('Task_Authoring/tools/stage_gate.py').resolve())
sys.modules[m.__name__] = m
exec(compile(subprocess.check_output(['git', 'show', 'HEAD:Task_Authoring/tools/stage_gate.py'], text=True), m.__file__, 'exec'), m.__dict__)
cases = json.loads((m.FIXTURES / 'bad/cases.json').read_text())['cases']
with tempfile.TemporaryDirectory() as td:
    for case in cases:
        if case['name'].startswith('injection-forecast'):
            d = Path(td) / 'fixture'
            m._prepare(d, m.FIXTURES / 'good', case['stage'])
            for mutation in case['mutate']:
                m._apply(d, mutation)
            ctx = m.run_stage(case['stage'], d, 'lint', True)
            print(case['name'], [r for r in ctx.res if r['id'] == 'forecast.preregistered'])
```

Independent oracle acceptance is separate; these author tests do not constitute oracle approval.

"""Independent integration seams; all mutations stay in isolated fixtures."""
import sys
import tempfile
import unittest
import json
import hashlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import stage_gate as gate
import v3_artifact_checks as v3
import readiness_controls as controls
import stage_evidence as evidence
from test_design_readiness import fixture


class DependencyTests(unittest.TestCase):
    def test_directory_digest_covers_reference_routing(self):
        scratch = Path(__file__).resolve().parents[1] / 'support/scratch'
        scratch.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as td:
            root = Path(td)
            (root / 'one').mkdir()
            (root / 'one/data.txt').write_text('same evidence')
            before = gate.file_digest(root)
            (root / 'one').rename(root / 'two')
            self.assertNotEqual(before, gate.file_digest(root))

    def test_production_precheck_review_has_no_future_rubric_dependency(self):
        from test_mode_b_report import fixture as mode_fixture
        from design_readiness import digest
        from trajectory_ledger import binding_bundle_hash
        scratch = Path(__file__).resolve().parents[1] / 'support/scratch'
        scratch.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as td:
            root = Path(td)
            (root / 'Working_Files').mkdir()
            (root / controls.CONFIG).write_text(json.dumps({'schema_version': 1, 'revision': 'r1', 'injection': 'required'}))
            (root / '04_Prompt.txt').write_text('Report the requested decisions.')
            data, kwargs, _ = mode_fixture(root, precheck=True)
            data['rubrics'] = []
            data['rollouts'][0]['results'] = {}
            task_id = evidence.task_identity(root)
            bundle = binding_bundle_hash(root, stage='precheck')
            receipt = kwargs.pop('receipt')
            receipt.update(task_id=task_id, bundle_hash=bundle, source_matrix_sha256=digest(data))
            (root / 'receipt.json').write_text(json.dumps(receipt))
            (root / 'matrix.json').write_text(json.dumps(data))
            kwargs.pop('task_dir')
            kwargs.update(task_id=task_id, bundle_hash=bundle, receipt='receipt.json', data_path='matrix.json',
                          trajectories=[path.name for path in kwargs['trajectories']])
            (root / 'Working_Files/mode_b_request.json').write_text(json.dumps(kwargs))
            ctx = gate.Ctx('hardening', root)
            ctx.context = {'task_dir': str(root), 'task_identity': task_id, 'spec_version': 'V3',
                           'difficulty_mode': 'easy', 'task_type': 'normal'}
            self.assertEqual(controls.mode_b_review(ctx)['verdict'], 'PASS')
            (root / '09_Rubrics.json').write_text('[]')
            (root / '08_Oracle_Events.md').write_text('Later-stage artifact.')
            self.assertEqual(controls.mode_b_review(ctx)['verdict'], 'PASS')

    def test_existing_stage_graph_is_acyclic(self):
        done, visiting = set(), set()
        def visit(stage):
            self.assertNotIn(stage, visiting, f"cycle at {stage}")
            if stage in done:
                return
            visiting.add(stage)
            for upstream, _ in gate.STAGES[stage]["upstream"]:
                visit(upstream)
            visiting.remove(stage)
            done.add(stage)
        for stage in gate.STAGES:
            visit(stage)

    def test_rubric_plan_does_not_require_future_final_rows(self):
        checks = v3.check_evidence("rubric-writing", Path("unused"), {},
                                   lambda _: None, lambda *_: (False, "missing"), Path("unused"))
        self.assertEqual(checks, [])

    def test_certificate_text_does_not_change_content_identity(self):
        original = "# Design\n\n## Self-review\nEvidence checked.\n"
        pasted = original + "\n```\nSTAGE GATE scenario: PASS — fixture\n[PASS] check: verified\n```\n"
        self.assertEqual(gate.digest_text(original), gate.digest_text(pasted))

    def test_baseline_is_not_an_upstream_design_input(self):
        for stage in ("scenario", "injection"):
            spec = gate.STAGES[stage]
            for name in spec["inputs"] + spec["optional"] + spec.get("digest_extra", []):
                self.assertNotIn("Baseline", name)
                self.assertNotIn("difficulty", name)


class ReadinessTraversalTests(unittest.TestCase):
    def setUp(self):
        scratch = Path(__file__).resolve().parents[1] / 'support/scratch'
        scratch.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(prefix='readiness-traversal-', dir=scratch)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'Working_Files/hardness_reviews').mkdir(parents=True)
        (self.root / controls.CONFIG).write_text(json.dumps({'schema_version': 1, 'revision': 'r1', 'injection': 'required'}))
        self.ctx = gate.Ctx('scenario', self.root)
        self.ctx.v3 = True
        self.ctx.context = {'difficulty_mode': 'easy', 'context_hash': 'fixture-context',
                            'assignment_hash': 'fixture-assignment', 'policy_hash': 'fixture-policy',
                            'universe': {'key': 'synthcut'}}
        for stage in ('scenario', 'injection', 'prompt', 'rubric', 'baseline'):
            man, surface, review, kwargs = fixture(self.root, stage)
            review['task_id'] = evidence.task_identity(self.root)
            name = '01_Hardness_Manifest.draft.json' if stage == 'scenario' else '01_Hardness_Manifest.json'
            gate.slot_path(self.root, name).write_text(json.dumps(man))
            gate.slot_path(self.root, gate.SURFACE).write_text(json.dumps(surface))
            (self.root / f'Working_Files/hardness_reviews/{stage}.json').write_text(json.dumps(review))
            if kwargs['prompt']:
                (self.root / '04_Prompt.txt').write_text(kwargs['prompt'])
            if kwargs['rubric'] is not None:
                (self.root / '09_Rubrics.json').write_text(json.dumps(kwargs['rubric']))
        # Local review accepts an empty SQL string at this unit seam; ordinary
        # injection stage lint/volume tests remain separately mandatory.
        (self.root / '01_Universe_Inject.sql').write_text('')
        # This unit fixture models completed upstream gates; full semantic gate
        # acceptance is exercised separately. Required artifacts still must exist.
        for stage in controls.LOCAL_STAGES:
            for name in gate.STAGES[stage]['inputs'] + gate.STAGES[stage]['outputs']:
                path = gate.slot_path(self.root, name)
                if not path.exists():
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text('isolated stage artifact\n')
        self.ctx.executed_gate = True
        for stage in controls.LOCAL_STAGES:
            self.ctx.stage = stage
            self.ctx.res = [{'id': cid, 'status': 'PASS', 'locations': [], 'blocking': False}
                            for cid in ('structure.inputs', 'structure.outputs', 'readiness.context')]
            controls.attest(gate, self.ctx, 'isolated integration fixture')

    def test_local_completion_does_not_require_platform_or_runs(self):
        local = controls.readiness(gate, self.ctx, 'local')
        self.assertTrue(local['ready'], local)
        platform = controls.readiness(gate, self.ctx, 'platform')
        self.assertTrue(platform['local_build_ready'], platform)
        self.assertFalse(platform['ready'])

    def test_baseline_update_keeps_design_and_injection_current(self):
        (self.root / '07_Baseline_Trajectories').mkdir()
        (self.root / '07_Baseline_Trajectories/run-1.json').write_text('[]')
        for stage in ('scenario', 'injection'):
            self.assertEqual(controls.current_errors(gate, self.ctx, stage), [])

    def test_sql_change_invalidates_only_dependent_records(self):
        (self.root / '01_Universe_Inject.sql').write_text('-- new proposed data')
        self.assertEqual(controls.current_errors(gate, self.ctx, 'scenario'), [])
        self.assertTrue(controls.current_errors(gate, self.ctx, 'injection'))

    def test_reviewed_supporting_file_change_invalidates_readiness(self):
        (self.root / 'evidence.txt').write_text('changed deciding evidence')
        self.assertFalse(controls.readiness(gate, self.ctx, 'local')['ready'])

    def test_missing_required_artifact_cannot_be_attested_current(self):
        gate.slot_path(self.root, '01_Scenario_Design.md').unlink()
        self.assertFalse(controls.readiness(gate, self.ctx, 'local')['ready'])

    def test_unexecuted_context_cannot_publish_gate_attestation(self):
        self.ctx.executed_gate = False
        with self.assertRaises(ValueError):
            controls.attest(gate, self.ctx, 'not a gate run')

    def test_postbaseline_readiness_requires_actual_environment_run_association(self):
        from trajectory_ledger import binding_bundle_hash
        rubric = json.loads((self.root / '09_Rubrics.json').read_text())
        (self.root / 'Working_Files/09_Builder_Export.json').write_text(json.dumps(rubric))
        bundle = binding_bundle_hash(self.root, self.root / '09_Rubrics.json')
        folder = self.root / '07_Baseline_Trajectories'
        folder.mkdir()
        lines = ['Task ID: ' + evidence.task_identity(self.root), 'Revision: r1', 'Bundle SHA256: ' + bundle]
        for n in range(1, 7):
            path = folder / f'export-{7-n}.json'
            path.write_text(json.dumps([{'type': 'system', 'subtype': 'init', 'session_id': f'session-{n}'},
                                        {'type': 'result', 'subtype': 'success', 'session_id': f'session-{n}'}]))
            lines.extend([f'Run #{n}', 'Export SHA256: ' + hashlib.sha256(path.read_bytes()).hexdigest(),
                          'Decision\tPass\tobserved'])
        (self.root / '10_Baseline_Verifier_Results.md').write_text('\n'.join(lines))
        # Human-time policy explicitly refreshes its measured counts after baseline.
        self.ctx.stage = 'humantime'
        controls.attest(gate, self.ctx, 'isolated post-baseline human-time review')
        ref = {'path': 'evidence.txt', 'sha256': hashlib.sha256((self.root / 'evidence.txt').read_bytes()).hexdigest(),
               'reason': 'Reviewed isolated deployment and tool-read evidence.'}
        receipt = {'schema_version': 1, 'task_id': evidence.task_identity(self.root), 'revision': 'r1',
                   'universe': 'synthcut', 'bundle_hash': bundle, 'environment_id': 'fixture-env',
                   'environment_state_id': 'state-1', 'reviewer': 'fixture', 'reason': 'Checked state evidence.',
                   'injection': {'state': 'applied', 'sha256': hashlib.sha256(b'').hexdigest()},
                   'manual_changes': [], 'baseline_run_ids': [f'session-{n}' for n in range(1, 7)],
                   'evaluator_release': controls.policy_identity(gate)}
        for key in ('fresh_base', 'application', 'readability'):
            receipt[key] = {'environment_state_id': 'state-1', 'verified': True, 'evidence': [ref]}
        receipt['fresh_base']['source'] = 'base-universe'
        receipt['readability'].update(decisive_records=['M1-source', 'M2-source', 'M3-source'], tool_assumptions='fixture tools')
        target = self.root / 'Working_Files/Platform_Handoff.json'
        target.write_text(json.dumps(receipt))
        result = controls.readiness(gate, self.ctx, 'platform', post_baseline=True)
        self.assertTrue(result['ready'], result)
        receipt['baseline_run_ids'] = []
        target.write_text(json.dumps(receipt))
        result = controls.readiness(gate, self.ctx, 'platform', post_baseline=True)
        self.assertFalse(result['ready'], result)
        self.assertTrue(any('run identities' in error for error in result['errors']), result)


if __name__ == "__main__":
    unittest.main()

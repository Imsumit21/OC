"""Fresh verification probes for final grading and production Mode B requests.

Expectations derive from the plan: two surface slots must survive as independently
graded final outcomes; a bundle hash must not license changing actual rubric
weights or assigned policy in a separate matrix. All writes are isolated.
"""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import design_readiness as dr
import difficulty_stats as ds
import mode_b_report as mb
from trajectory_ledger import binding_bundle_hash
from test_design_readiness import fixture as design_fixture
from test_mode_b_report import fixture as mode_fixture


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class FreshDesignVerification(unittest.TestCase):
    def setUp(self):
        scratch = Path(__file__).resolve().parents[1] / 'support/scratch'
        scratch.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(prefix='verify-design-', dir=scratch)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()

    def test_final_pair_cannot_collapse_to_one_criterion(self):
        manifest, surface, review, kwargs = design_fixture(self.root, 'rubric')
        self.assertEqual(dr.evaluate('rubric', manifest, surface, review, **kwargs)['verdict'], 'PASS')
        review['coverage']['M1b'] = {'rubric_ids': ['M1a']}
        rejected = dr.evaluate('rubric', manifest, surface, review, **kwargs)
        self.assertEqual(rejected['verdict'], 'FAIL', rejected)
        self.assertTrue(any('independently covering final criteria' in e for e in rejected['blockers']))

    def test_each_side_needs_exclusive_final_coverage(self):
        manifest, surface, review, kwargs = design_fixture(self.root, 'rubric')
        review['coverage']['M1a'] = {'rubric_ids': ['M1a', 'M1b']}
        review['coverage']['M1b'] = {'rubric_ids': ['M1b']}
        self.assertEqual(dr.evaluate('rubric', manifest, surface, review, **kwargs)['verdict'], 'FAIL')

    def test_final_row_cannot_inflate_a_lookup_slot_weight(self):
        manifest, surface, review, kwargs = design_fixture(self.root, 'rubric')
        surface['slots'].append({'id': 'lookup', 'fact_id': 'lookup', 'weight': 1, 'work_kind': 'lookup',
                                 'work_reason': 'Read a supplied identifier.', 'role': 'core',
                                 'incorporating_span': 'Report the decisions.'})
        kwargs['rubric'].append({'id': 'lookup', 'title': 'Lookup', 'weight': 5})
        review['coverage']['lookup'] = {'rubric_ids': ['lookup']}
        review['input_hashes'] = dr.input_hashes('rubric', manifest, surface,
                                                prompt=kwargs['prompt'], rubric=kwargs['rubric'])
        result = dr.evaluate('rubric', manifest, surface, review, **kwargs)
        self.assertEqual(result['verdict'], 'FAIL', result)
        self.assertTrue(any('weight exceeds' in e for e in result['blockers']))
        kwargs['rubric'][-1]['weight'] = 1
        review['input_hashes'] = dr.input_hashes('rubric', manifest, surface,
                                                prompt=kwargs['prompt'], rubric=kwargs['rubric'])
        self.assertEqual(dr.evaluate('rubric', manifest, surface, review, **kwargs)['verdict'], 'PASS')

    def baseline(self):
        root = self.root
        (root / 'Working_Files').mkdir()
        folder = root / '07_Baseline_Trajectories'
        folder.mkdir()
        rubric = [{'title': 'First outcome', 'weight': 5, 'category': 'Outcome'},
                  {'title': 'Second outcome', 'weight': 5, 'category': 'Outcome'}]
        (root / '09_Rubrics.json').write_text(json.dumps(rubric))
        context = {'task_dir': str(root), 'task_identity': 'task-fixture', 'spec_version': 'V3',
                   'difficulty_mode': 'easy', 'difficulty_cap': .9, 'task_type': 'normal',
                   'assignment_hash': 'assignment', 'context_hash': 'context', 'policy_hash': 'policy'}
        bundle = binding_bundle_hash(root)
        blocks = ['Task ID: task-fixture', 'Revision: r1', 'Bundle SHA256: ' + bundle]
        paths = []
        for n in range(1, 7):
            path = folder / f'export-{n}.json'
            events = [{'type': 'assistant', 'message': {'model': 'claude-opus-5-5',
                       'content': [{'type': 'text', 'text': f'decision {n}'}]}},
                      {'type': 'result', 'subtype': 'success', 'session_id': f'actual-{n}'}]
            path.write_text(json.dumps(events))
            paths.append(path)
            blocks.extend([f'Run #{n}', 'Export SHA256: ' + sha(path),
                           'First outcome\t' + ('Pass' if n % 2 == 0 else 'Fail') + '\tobserved',
                           'Second outcome\t' + ('Pass' if n % 3 == 0 else 'Fail') + '\tobserved'])
        verifier = root / '10_Baseline_Verifier_Results.md'
        verifier.write_text('\n'.join(blocks))
        data, _ = ds.build(verifier, root / '09_Rubrics.json', folder, 'normal', context=context, revision='r1')
        data_path = root / 'Working_Files/matrix.json'
        data_path.write_text(json.dumps(data))
        proof = root / 'Working_Files/diagnosis.txt'
        proof.write_text('The dated deciding source changes the first outcome; the run retained the earlier state.')
        diagnosis = {'id': 'D1', 'mechanism': 'M1', 'observation': 'dominant_pattern',
                     'reason': 'Compared the write with dated authority.',
                     'evidence': [{'path': str(proof.relative_to(root)), 'sha256': sha(proof)}],
                     'trajectory_events': [{'run': 'run-1', 'event': 0, 'export_sha256': sha(paths[0]), 'quote': 'decision 1'}]}
        request = {'data_path': str(data_path.relative_to(root)), 'verifier': verifier.name,
                   'trajectories': [str(path.relative_to(root)) for path in paths],
                   'task_id': context['task_identity'], 'revision': 'r1', 'bundle_hash': bundle,
                   'diagnoses': [diagnosis]}
        return context, request, data, data_path

    def test_production_request_accepts_actual_bound_rows(self):
        context, request, data, _ = self.baseline()
        report = mb.from_request(request, self.root, context=context)
        self.assertEqual(report['verdict'], 'PASS', report['blockers'])
        self.assertEqual([row['weight'] for row in report['heavy_rows']], [5, 5])
        self.assertEqual(report['raw_matrix'], data)

    def test_production_request_rejects_weight_tampering(self):
        context, request, data, path = self.baseline()
        data['rubrics'][0]['weight'] = 1
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'rubric rows differ'):
            mb.from_request(request, self.root, context=context)

    def test_production_request_rejects_policy_downgrade(self):
        context, request, data, path = self.baseline()
        data['spec_version'] = 'V2'
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'disagrees with current assignment'):
            mb.from_request(request, self.root, context=context)

    def test_production_request_rejects_changed_assignment_mode(self):
        context, request, data, path = self.baseline()
        data['difficulty_mode'] = 'hard'
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'disagrees with current assignment'):
            mb.from_request(request, self.root, context=context)

    def test_production_correction_evidence_can_be_supplied_in_request(self):
        context, request, data, path = self.baseline()
        data['rollouts'][0]['judge_corrections'] = {'R1': True}
        path.write_text(json.dumps(data))
        request['correction_evidence'] = {'run-1:R1': copy.deepcopy(request['diagnoses'][0])}
        report = mb.from_request(request, self.root, context=context)
        self.assertEqual(report['verdict'], 'PASS', report['blockers'])
        self.assertIs(report['heavy_rows'][0]['runs'][0]['raw'], False)
        self.assertIs(report['heavy_rows'][0]['runs'][0]['corrected'], True)

    def test_repair_requires_real_outcomes_scope_difference_and_rerun_list(self):
        data, kwargs, proof = mode_fixture(self.root)
        repair = {**proof, 'id': 'repair', 'diagnosis': 'D1', 'original_placement': 'old record',
                  'proposed_change': 'move the governing evidence while retaining its pointer',
                  'affected_outcomes': ['NONEXISTENT'], 'scope_difference': {'reason_class': 'difficulty'},
                  'fair_discovery_path': 'same handoff pointer', 'required_reruns': 'none',
                  'artifact': 'universe', 'owner': 'create-scenario --revise'}
        kwargs['repairs'] = [repair]
        result = mb.build(data, **kwargs)
        self.assertEqual(result['verdict'], 'FAIL', result)
        for expected in ('scope/volume', 'change kind', 'affected outcome', 'bounded list'):
            self.assertTrue(any(expected in error for error in result['blockers']), expected)
        repair.update(affected_outcomes=['R1'], scope_difference={'reason_class': 'difficulty', 'rows_added': 0},
                      change_kind='evidence_placement', required_reruns=['scenario', 'injection', 'precheck', 'verifier', 'baseline'])
        self.assertEqual(mb.build(data, **kwargs)['verdict'], 'PASS')


if __name__ == '__main__':
    unittest.main()

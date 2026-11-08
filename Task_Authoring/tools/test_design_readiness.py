import copy
import hashlib
import tempfile
import unittest
from pathlib import Path
import design_readiness as dr
import hardness_v2_check as hv


def fixture(root, stage='scenario', mode='easy'):
    (root / 'evidence.txt').write_text('Concrete record excerpts; naturally returned records and persona reach proofs.')
    ref = {'path': 'evidence.txt', 'sha256': hashlib.sha256((root / 'evidence.txt').read_bytes()).hexdigest()}
    def proof(**extra):
        return {'reason': 'Source excerpt and counterfactual checked against the requested task.', 'evidence': [ref], **extra}
    ids = ['M' + str(i) for i in range(1, 5 if mode == 'hard' else 4)]
    man = {'difficulty_mode': mode, 'mechanism_portfolio': [{'id': m, 'mechanism': 'A15', 'requirement': m} for m in ids]}
    surface = {'slots': []}
    review = {'schema_version': 1, 'stage': stage, 'task_id': 'isolated', 'revision': 'r1', 'reviewer': 'reviewer',
              'difficulty_mode': mode, 'diversity_channels': ids, 'mechanisms': {}, 'dispositions': {}}
    for m in ids:
        slots = [m + 'a', m + 'b']
        for sid in slots:
            surface['slots'].append({'id': sid, 'fact_id': sid, 'weight': 5, 'work_kind': 'multi_source_reconciliation',
                                     'work_reason': 'reconcile authoritative correction', 'mechanisms': [m],
                                     'incorporating_span': 'Report the decisions.', 'role': 'core'})
        row = {k: proof() for k in ('initial_plausible_answer', 'deciding_evidence', 'authority_chronology', 'fair_discovery_path', 'changed_outcome', 'independent_operation')}
        row['deciding_evidence']['record_id'] = m + '-source'
        row['changed_outcome'].update(before='ready', after='hold')
        row['independent_operation']['others_solvable_if_missed'] = [i for i in ids if i != m]
        row.update(outcome_slots=slots, channel_kind='judgment',
                   outcome_pair=proof(slots=slots, left_pass_right_fail='first decision correct; second wrong', right_pass_left_fail='second decision correct; first wrong'))
        if stage == 'scenario':
            row['access'] = row['natural_retrieval'] = {'status': 'deferred', 'required_at': 'injection'}
        else:
            row['access'] = proof(status='verified')
            row['natural_retrieval'] = proof(query='list decisions', returned_ids=['old', m + '-source'], assessment='Cross-source chronology still required')
        review['mechanisms'][m] = row
    prompt = 'Report the decisions.' if stage in ('prompt', 'rubric', 'baseline') else ''
    rubric = [{'id': s['id'], 'title': s['id'], 'weight': 5} for s in surface['slots']] if stage in ('rubric', 'baseline') else None
    review['semantic_prompt_review'] = proof(leaks_solution=False)
    review['coverage'] = {s['id']: {'rubric_ids': [s['id']]} for s in surface['slots']}
    for finding in hv.run(man, '', prompt, surface)['flags']:
        review['dispositions'][finding['check'] + ':' + str(finding.get('node') or '-')] = proof(status='not_applicable')
    kw = {'prompt': prompt, 'rubric': rubric, 'builder_rubric': rubric if stage == 'baseline' else None,
          'task_dir': root, 'task_id': 'isolated', 'revision': 'r1', 'difficulty_mode': mode}
    review['input_hashes'] = dr.input_hashes(stage, man, surface, prompt=prompt, rubric=rubric, builder_rubric=kw['builder_rubric'])
    return man, surface, review, kw


class Readiness(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
    def tearDown(self):
        self.tmp.cleanup()
    def run_case(self, stage='scenario', mutate=None):
        man, surface, review, kw = fixture(self.root, stage)
        if mutate:
            mutate(man, surface, review, kw)
        return dr.evaluate(stage, man, surface, review, **kw)
    def test_design_valid_without_later_artifacts(self):
        rep = self.run_case()
        self.assertEqual(rep['verdict'], 'PASS', rep)
        self.assertEqual(len(rep['deferred']), 6)
    def test_valid_all_stages(self):
        for stage in dr.STAGES:
            rep = self.run_case(stage)
            self.assertEqual(rep['verdict'], 'PASS', rep)
    def test_deferred_becomes_required(self):
        rep = self.run_case('injection', lambda m,s,r,k: r['mechanisms']['M1'].update(access={'status': 'deferred', 'required_at':'injection'}))
        self.assertEqual(rep['verdict'], 'FAIL')
    def test_inaccessible_cannot_be_waived(self):
        rep = self.run_case(mutate=lambda m,s,r,k: r['mechanisms']['M1'].update(access={'status':'inaccessible', 'reason':'reviewed'}))
        self.assertEqual(rep['verdict'], 'FAIL')
    def test_generic_waiver_rejected(self):
        rep = self.run_case(mutate=lambda m,s,r,k: r['dispositions']['DONE_CHECK:-'].update(reason='reviewed'))
        self.assertEqual(rep['verdict'], 'FAIL')
    def test_probabilities_advisory(self):
        rep = self.run_case(mutate=lambda m,s,r,k: r.update(forecast={'p_all_gates':0.001}))
        self.assertEqual(rep['verdict'], 'PASS')
    def test_stale_source_rejected(self):
        rep = self.run_case(mutate=lambda m,s,r,k: (self.root/'evidence.txt').write_text('changed'))
        self.assertEqual(rep['verdict'], 'FAIL')
    def test_stale_prompt_rejected(self):
        rep = self.run_case('prompt', lambda m,s,r,k: k.update(prompt=k['prompt']+' New work.'))
        self.assertIn('stale or incomplete hardness review inputs', rep['blockers'])
    def test_unrequested_outcome_rejected(self):
        rep = self.run_case('prompt', lambda m,s,r,k: s['slots'][0].update(incorporating_span='Explain every decision.'))
        self.assertTrue(any('not requested' in x for x in rep['blockers']))
    def test_same_fact_in_two_destinations_not_a_pair(self):
        rep = self.run_case(mutate=lambda m,s,r,k: s['slots'][1].update(fact_id=s['slots'][0]['fact_id']))
        self.assertTrue(any('duplicate fact' in x for x in rep['blockers']))
    def test_weight_inflation_rejected(self):
        rep = self.run_case(mutate=lambda m,s,r,k: s['slots'][0].update(work_kind='lookup'))
        self.assertTrue(any('weight must follow' in x for x in rep['blockers']))
    def test_core_write_not_sampled_away(self):
        rep = self.run_case('rubric', lambda m,s,r,k: r['coverage']['M1a'].update(rubric_ids=[],status='sampled_out'))
        self.assertTrue(any('lacks coverage' in x for x in rep['blockers']))
    def test_builder_drift_blocks(self):
        rep = self.run_case('baseline', lambda m,s,r,k: k.update(builder_rubric=[]))
        self.assertTrue(any('builder export' in x for x in rep['blockers']))
    def test_assignment_hard_cannot_be_lowered_by_review(self):
        rep = self.run_case(mutate=lambda m,s,r,k: k.update(difficulty_mode='hard'))
        self.assertTrue(any('at least 4' in x for x in rep['blockers']))
    def test_cross_task_evidence_rejected(self):
        rep = self.run_case(mutate=lambda m,s,r,k: r['mechanisms']['M1']['initial_plausible_answer']['evidence'][0].update(path='../evidence.txt'))
        self.assertEqual(rep['verdict'], 'FAIL')

if __name__ == '__main__':
    unittest.main()

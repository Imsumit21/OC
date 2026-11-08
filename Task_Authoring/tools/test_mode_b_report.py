import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
import mode_b_report as mb
from design_readiness import digest


def fixture(root, precheck=False):
    proof_path = root/'proof.txt'
    proof_path.write_text('The observed decision is wrong because the governing dated source says hold.')
    proof = {'reason':'Compared requested output to governing dated decision and raw write.', 'evidence':[
        {'path':'proof.txt','sha256':hashlib.sha256(proof_path.read_bytes()).hexdigest()}]}
    paths, runs, blocks = [], [], ['Task ID: test', 'Revision: r1', 'Bundle SHA256: bundle']
    for i in range(1, 2 if precheck else 7):
        path = root/f'arbitrary-{i}.json'
        path.write_text(json.dumps([{'type':'assistant','message':{'model':'claude-opus-5-5','content':[{'type':'text','text':f'decision {i}'}]}},
                                   {'type':'result','subtype':'success','session_id':f's{i}'}]))
        paths.append(path)
        runs.append({'id':f'run-{i}','status':'completed','tool_calls':0,'models':['claude-opus-5-5'], 'model_source':str(path),
                     'results':{'R1':i%2 == 0, 'R2':i%3 == 0}})
        blocks.extend([f'Run #{i}', 'Export SHA256: '+hashlib.sha256(path.read_bytes()).hexdigest(),
                       'First outcome\t'+('Pass' if i%2 == 0 else 'Fail')+'\tobserved decision',
                       'Second outcome\t'+('Pass' if i%3 == 0 else 'Fail')+'\tobserved decision'])
    verifier = root/'verifier.txt'
    verifier.write_text('\n'.join(blocks))
    data = {'spec_version':'V3','difficulty_mode':'easy','task_type':'normal', 'rubrics':[
        {'id':'R1','title':'First outcome','weight':5},{'id':'R2','title':'Second outcome','weight':5}], 'rollouts':runs}
    diagnosis = {**copy.deepcopy(proof), 'id':'D1','mechanism':'M1','observation':'dominant_pattern','trajectory_events':[
        {'run':'run-1','event':0,'export_sha256':hashlib.sha256(paths[0].read_bytes()).hexdigest(),'quote':'decision 1'}]}
    kw = dict(verifier=verifier,trajectories=paths,task_id='test',revision='r1',bundle_hash='bundle',task_dir=root,diagnoses=[diagnosis],precheck=precheck)
    if precheck:
        kw['receipt'] = {**proof,'kind':'PRECHECK_EXPORT_REVIEW','schema_version':1,'task_id':'test','revision':'r1',
                         'bundle_hash':'bundle','export_sha256':hashlib.sha256(paths[0].read_bytes()).hexdigest(),
                         'source_matrix_sha256':digest(data),'reviewer':'oracle'}
        kw.pop('verifier')
    return data, kw, proof


class ModeB(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
    def tearDown(self): self.tmp.cleanup()
    def test_bound_baseline_and_raw_preserved(self):
        data,kw,_=fixture(self.root)
        before=copy.deepcopy(data)
        rep=mb.build(data,**kw)
        self.assertEqual(rep['verdict'],'PASS',rep['blockers'])
        self.assertEqual(data,before)
        self.assertEqual(rep['raw_matrix'],before)
        self.assertEqual(len(rep['heavy_rows'][0]['runs']),6)
        self.assertIn('platform',rep['patterns'])
    def test_raw_matrix_tampering_rejected(self):
        data,kw,_=fixture(self.root)
        data['rollouts'][0]['results']['R1']=True
        self.assertEqual(mb.build(data,**kw)['verdict'],'FAIL')
    def test_justified_correction_only_changes_corrected_view(self):
        data,kw,proof=fixture(self.root)
        data['rollouts'][0]['judge_corrections']={'R1':True}
        kw['correction_evidence']={'run-1:R1':proof}
        rep=mb.build(data,**kw)
        self.assertEqual(rep['verdict'],'PASS',rep['blockers'])
        row=rep['heavy_rows'][0]['runs'][0]
        self.assertIs(row['raw'],False)
        self.assertIs(row['corrected'],True)
    def test_unjustified_correction_rejected(self):
        data,kw,_=fixture(self.root)
        data['rollouts'][0]['judge_corrections']={'R1':True}
        self.assertEqual(mb.build(data,**kw)['verdict'],'FAIL')
    def test_stale_event_rejected(self):
        data,kw,_=fixture(self.root)
        kw['diagnoses'][0]['trajectory_events'][0]['quote']='made up'
        self.assertEqual(mb.build(data,**kw)['verdict'],'FAIL')
    def test_volume_only_difficulty_repair_rejected_but_fairness_allowed(self):
        data,kw,proof=fixture(self.root)
        repair={**proof,'id':'P1','diagnosis':'D1','original_placement':'old record','proposed_change':'add missing source',
                'affected_outcomes':['R1'],'scope_difference':{'reason_class':'difficulty','rows_added':1},'change_kind':'volume_only',
                'fair_discovery_path':'from handoff to governing rule','required_reruns':['scenario','injection'],
                'artifact':'universe','owner':'create-scenario --revise'}
        kw['repairs']=[repair]
        self.assertEqual(mb.build(data,**kw)['verdict'],'FAIL')
        repair['scope_difference']['reason_class']='fairness'
        self.assertEqual(mb.build(data,**kw)['verdict'],'PASS')
    def test_precheck_no_final_rubric_or_verifier(self):
        data,kw,_=fixture(self.root,True)
        data['rubrics']=[]
        data['rollouts'][0]['results']={}
        kw['receipt']['source_matrix_sha256']=digest(data)
        rep=mb.build(data,**kw)
        self.assertEqual(rep['verdict'],'PASS',rep['blockers'])
        self.assertEqual(rep['evidence_scope'],'PROVISIONAL_SINGLE_PRECHECK')
        self.assertIsNone(rep['statistics'])
        self.assertEqual(rep['patterns'],{})
    def test_changed_precheck_export_rejects(self):
        data,kw,_=fixture(self.root,True)
        kw['trajectories'][0].write_text('[]')
        with self.assertRaises(ValueError): mb.build(data,**kw)

if __name__=='__main__': unittest.main()

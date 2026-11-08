"""Isolated regression fixtures for stage evidence, identity and platform handoff."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import stage_evidence as se
import platform_handoff as ph
import trajectory_ledger as tl
import difficulty_stats as ds

SCRATCH = Path(__file__).resolve().parents[1] / 'support' / 'scratch'
SCRATCH.mkdir(parents=True, exist_ok=True)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=SCRATCH)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def args(self, stage='scenario'):
        return dict(stage=stage, revision='r1', inputs={'assignment':'a', 'design':'b'}, upstream={},
                    checks=[{'id':'review','outcome':'PASS','evidence_refs':['design']}], availability=[],
                    reviewer='independent reviewer', tool_identity='tool/v1', policy_identity='policy/v1')

    def test_acyclic_and_future_dependency_rejected(self):
        for stage in se.DEPENDENCIES:
            self.assertNotIn(stage, se.ancestors(stage))
        args = self.args()
        args['upstream'] = {'baseline':'future'}
        with self.assertRaisesRegex(ValueError, 'ancestor'):
            se.attest(self.root, **args)

    def test_immutable_idempotent_history_and_no_baseline_dependency(self):
        record = se.attest(self.root, **self.args())
        self.assertEqual(record, se.attest(self.root, **self.args()))
        # A baseline update is not a dependency of scenario and changes no current inputs.
        (self.root/'baseline.json').write_text('new batch')
        self.assertEqual([], se.validate(record, task_id=se.task_identity(self.root), stage='scenario',
                                        inputs=self.args()['inputs'], upstream={}))
        args = self.args(); args['inputs']['design'] = 'edited'
        replacement = se.attest(self.root, **args)
        self.assertEqual(replacement['supersedes'], record['evidence_id'])
        self.assertTrue((self.root/se.DIRECTORY/(record['evidence_id']+'.json')).exists())
        self.assertIn('STALE', ' '.join(se.validate(record, task_id=se.task_identity(self.root), stage='scenario',
                                                  inputs=args['inputs'], upstream={})))

    def test_early_stage_defers_then_requires_evidence(self):
        args = self.args()
        args['availability'] = [{'id':'sql','state':'deferred','required_at':'injection','reason':'not authored yet'}]
        record = se.attest(self.root, **args)
        self.assertEqual([], se.availability_errors(record['availability'], 'scenario'))
        self.assertTrue(se.availability_errors(record['availability'], 'injection'))
        self.assertTrue(se.availability_errors(record['availability'], 'rubric-check'))

    def test_not_applicable_and_cross_task(self):
        args = self.args(); args['availability'] = [{'id':'other','state':'not-applicable','reason':'mechanism not selected'}]
        record = se.attest(self.root, **args)
        self.assertTrue(se.validate(record,task_id='other',stage='scenario',inputs=args['inputs'],upstream={}))
        args['availability'][0]['reason']=''
        with self.assertRaises(ValueError): se.attest(self.root, **args)

    def test_self_certificate_normalization(self):
        from stage_gate import digest_text
        a='Actual design\n'
        b=a+'```\nSTAGE GATE scenario: PASS\n[PASS] check: result\n```\n'
        self.assertEqual(digest_text(a),digest_text(b))

    def test_legacy_and_evaluator_identity(self):
        self.assertIn('HISTORICAL_UNVERIFIED',se.validate({},task_id='a',stage='scenario',inputs={},upstream={})[0])
        self.assertEqual('REVIEW_REQUIRED', se.evaluator_compatibility('hash-a','hash-b')['status'])
        self.assertEqual('UNKNOWN',se.evaluator_compatibility('hash-a',None)['status'])
        self.assertEqual('MATCH',se.evaluator_compatibility('a','a')['status'])

    def test_local_readiness_is_independent(self):
        statuses={s:'CURRENT' for s in ('scenario','injection','prompt-check','oe-check','rubric-check')}
        self.assertTrue(se.readiness(statuses)['local_build_ready'])
        self.assertFalse(se.readiness(statuses)['platform_baseline_ready'])
        statuses['injection']='NOT_APPLICABLE'
        self.assertTrue(se.readiness(statuses,no_injection=True)['local_build_ready'])

    def test_output_symlink_escape(self):
        with tempfile.TemporaryDirectory() as outside:
            (self.root/'Working_Files').symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ValueError): se.attest(self.root,**self.args())


class BindingTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(dir=SCRATCH);self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.verifier=self.root/'verifier.txt'
        self.paths=[]
        for n in range(1,7):
            p=self.root/f'run-{n}.json'
            p.write_text(json.dumps([{'type':'system','subtype':'init','session_id':f'session-{n}','model':'claude-opus-5-5'},
                                    {'type':'result','subtype':'success','result':f'created item-{n}'}]))
            self.paths.append(p)
        self.verifier.write_text(''.join(f'Run #{n}\n1/1 criteria passed\nOutcome\tPass\tCreated item-{n}\n' for n in range(1,7)))
        self.source=self.root/'platform-export.txt'; self.source.write_text('reviewed export with session mapping')
        self.receipt=dict(schema_version=1,kind='VERIFIER_EXPORT_BINDING',task_id='task-a',revision='r1',bundle_hash='bundle',
                          verifier_sha256=tl.sha256_file(self.verifier),reviewer='Alice',reason='Compared created item identities',
                          evidence=[{'path':str(self.source),'sha256':tl.sha256_file(self.source),'reason':'original platform export'}],
                          runs=[{'number':n,'export_sha256':tl.sha256_file(p),'run_id':f'session-{n}',
                                 'comparison':{'reason':'created item and session agree','export_observation':f'created item-{n}',
                                               'verifier_observation':f'Created item-{n}'}} for n,p in enumerate(self.paths,1)])

    def bind(self,receipt=None):
        return tl.bind_verifier_exports(self.verifier,self.paths,task_id='task-a',revision='r1',bundle_hash='bundle',
                                       receipt=self.receipt if receipt is None else receipt,task_dir=self.root)

    def test_valid_batch_and_filename_shuffle(self):
        before=self.bind()
        self.assertEqual('BOUND', before['verdict'])
        a,b=self.paths[0].read_bytes(),self.paths[1].read_bytes()
        self.paths[0].write_bytes(b);self.paths[1].write_bytes(a)
        after=self.bind()
        self.assertEqual(self.paths[1],after['runs'][1])
        self.assertEqual(self.paths[0],after['runs'][2])

    def test_superseded_export_and_changed_verifier_rejected(self):
        self.paths[0].write_text('[]')
        with self.assertRaisesRegex(ValueError,'UNBOUND'): self.bind()
        self.verifier.write_text(self.verifier.read_text()+'change')
        with self.assertRaisesRegex(ValueError,'stale'): self.bind()

    def test_filename_alone_rejected(self):
        with self.assertRaisesRegex(ValueError,'UNBOUND'):
            tl.bind_verifier_exports(self.verifier,self.paths,task_id='task-a',revision='r1',bundle_hash='bundle')

    def test_review_requires_actual_evidence_and_observed_content(self):
        for mutate in ('hash','observation','reviewer'):
            receipt=copy.deepcopy(self.receipt)
            if mutate=='hash':receipt['evidence'][0]['sha256']='bad'
            if mutate=='observation':receipt['runs'][0]['comparison']['export_observation']='invented'
            if mutate=='reviewer':receipt['reviewer']=''
            with self.assertRaises(ValueError):self.bind(receipt)

    def test_inline_machine_ids_and_hash_binding(self):
        text='Task ID: task-a\nRevision: r1\nBundle SHA256: bundle\n'
        for n,p in enumerate(self.paths,1):
            text+=f'Run #{n}\nExport SHA256: {tl.sha256_file(p)}\nSession ID: session-{n}\nOutcome\tPass\tend state ID absent from export\n'
        self.verifier.write_text(text)
        bound=tl.bind_verifier_exports(self.verifier,self.paths,task_id='task-a',revision='r1',bundle_hash='bundle')
        self.assertEqual('BOUND',bound['verdict'])

    def test_generic_receipt_observations_cannot_remap(self):
        receipt=copy.deepcopy(self.receipt)
        for row in receipt['runs']:
            row['comparison']['export_observation']='type'
            row['comparison']['verifier_observation']='Pass'
        with self.assertRaisesRegex(ValueError,'discriminating'):self.bind(receipt)

    def test_v3_build_revalidates_saved_raw_results(self):
        root=self.root
        (root/'00_Assigments.md').write_text('fixture assignment')
        rubric=root/'09_Rubrics.json'
        rubric.write_text(json.dumps([{'title':'Outcome','weight':5,'category':'outcome'}]))
        canonical=root/'10_Baseline_Verifier_Results.md'
        self.verifier.rename(canonical); self.verifier=canonical
        trajectories=root/'07_Baseline_Trajectories';trajectories.mkdir()
        for p in self.paths:p.rename(trajectories/p.name)
        self.paths=list(sorted(trajectories.glob('*.json')))
        context={'task_dir':str(root),'task_identity':se.task_identity(root),'task_type':'normal',
                 'difficulty_mode':'hard','difficulty_cap':0.7,'assignment_hash':'a','policy_hash':'p','context_hash':'c'}
        self.receipt.update(task_id=context['task_identity'],bundle_hash=tl.binding_bundle_hash(root))
        matrix,_=ds.build(canonical,rubric,trajectories,'normal',context=context,binding_receipt=self.receipt,revision='r1')
        self.assertEqual('BOUND',ds.revalidate_binding(matrix,context)['verdict'])
        matrix['rollouts'][0]['judge_corrections']={'R1':False}
        with self.assertRaisesRegex(ValueError,'correction lacks'): ds.revalidate_binding(matrix,context)
        matrix['correction_evidence']={'run-1:R1':{'reason':'Verified grader applied wrong account',
            'evidence':[{'path':str(self.source),'sha256':tl.sha256_file(self.source)}]}}
        self.assertEqual('BOUND',ds.revalidate_binding(matrix,context)['verdict'])
        matrix['rollouts'][0]['results']['R1']=False
        with self.assertRaisesRegex(ValueError,'raw evidence'):ds.revalidate_binding(matrix,context)
        with self.assertRaisesRegex(ValueError,'revision'):
            ds.build(canonical,rubric,trajectories,'normal',context=context,binding_receipt=self.receipt)

    def test_legacy_wrong_batch_is_only_diagnostic(self):
        r=self.root/'rubric.json';r.write_text(json.dumps([{'title':'Outcome','weight':5,'category':'outcome'}]))
        trajectories=self.root/'trajs';trajectories.mkdir()
        for p in self.paths:(trajectories/p.name).write_bytes(p.read_bytes())
        result,_=ds.build(self.verifier,r,trajectories,'normal',spec_version='V2')
        self.assertEqual('HISTORICAL_UNVERIFIED',result['verifier_binding']['verdict'])


class PlatformTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(dir=SCRATCH);self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);p=self.root/'platform.txt';p.write_text('actual deployment and tool reads')
        section={'environment_state_id':'state1','verified':True,'evidence':[{'path':'platform.txt','sha256':tl.sha256_file(p),'reason':'observed state'}]}
        self.receipt={'schema_version':1,'task_id':'a','revision':'r1','universe':'synthcut','bundle_hash':'bundle',
                      'reviewer':'reviewer','reason':'checked live export','environment_id':'env','environment_state_id':'state1',
                      'injection':{'state':'not-used'},'fresh_base':dict(section,source='base-universe'),
                      'application':dict(section),'readability':dict(section,decisive_records=['item'],tool_assumptions=['catalog v1']),
                      'manual_changes':[],'baseline_run_ids':[]}
        self.args=dict(task_dir=self.root,task_id='a',revision='r1',universe='synthcut',sql_hash=None,bundle_hash='bundle')

    def test_no_injection_and_pre_baseline_are_valid(self):
        self.assertEqual([],ph.validate(self.receipt,**self.args))
        self.assertTrue(ph.validate(self.receipt,**self.args,run_ids=['actual-run']))
        self.receipt['baseline_run_ids']=['actual-run']
        self.assertEqual([],ph.validate(self.receipt,**self.args,run_ids=['actual-run']))

    def test_unknown_cross_task_stale_environment_and_evidence(self):
        self.assertTrue(ph.validate(None,**self.args))
        self.assertTrue(ph.validate(self.receipt,**dict(self.args,task_id='b')))
        self.receipt['readability']['environment_state_id']='other'
        self.assertTrue(ph.validate(self.receipt,**self.args))
        (self.root/'platform.txt').write_text('changed')
        self.assertTrue(ph.validate(self.receipt,**self.args))

if __name__=='__main__': unittest.main()

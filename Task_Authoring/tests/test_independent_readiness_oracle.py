"""Independent acceptance oracle derived from the two guides and reviewed plan.

No production implementation fixtures are imported; all writes are scratch-local.
"""
import copy
import hashlib
import json
import multiprocessing
import subprocess
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1] / 'tools'
sys.path.insert(0, str(TOOLS))
import difficulty_stats as ds
import stage_evidence as se
import stage_gate as sg
import platform_handoff as ph
import trajectory_ledger as tl
import task_context as tc
import design_readiness as dr
import hardness_v2_check as hv
from hardness_ledger import Ledger


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ledger_worker(path, task, verdict, barrier, queue):
    ledger = Ledger(path)
    barrier.wait(20)
    queue.put(ledger.append([dict(kind='verdict', task=task, revision='oracle-r1',
        source='platform-baseline', model='claude-opus-5-5', harness={'name':'oracle','version':'1'},
        epistemic='observed', run='session', node='decision', verdict=verdict)]))


class Oracle(unittest.TestCase):
    def setUp(self):
        scratch = TOOLS.parent / 'support/scratch'
        scratch.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix='independent-oracle-', dir=scratch)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_guide_pattern_examples_and_boundaries(self):
        cases = [([{'R12'}, {'R12','R20'}, {'R12'}, {'R12'}], False),
                 ([{'R5','R6'},{'R5','R6','R9','R10'},{'R9','R10'},{'R5','R6'}], True),
                 ([], False), ([{'a'}], False),
                 ([{'a','b'},{'c','d'},{'e','f'}], True),
                 ([{'a','b'}]*3 + [{'c','d'},{'e','f'}], False),
                 ([{'a','b'}]*3 + [{'c','d'}]*3, True),
                 ([{'a'}, {'a','b'}, {'a','b','c'}, {'x','y'}], False)]
        for failed, expected in cases:
            ids = sorted(set().union(*failed)) if failed else ['unused']
            rows = [{'id':str(i), 'tool_calls':120, 'results':{k:k not in f for k in ids}}
                    for i,f in enumerate(failed + [set()]*(6-len(failed)))]
            result = ds._gates(rows, [], 6, [{'id':i,'weight':1} for i in ids], 'long-horizon')
            self.assertEqual(result['gates']['failure_patterns']['verdict'] == 'PASS', expected)

    def test_stage_dag_and_self_stability(self):
        for name in se.DEPENDENCIES:
            self.assertNotIn(name, se.ancestors(name))
        text = '# Design\n## Self-review\nEvidence reviewed.\n'
        extra = '\n```\nSTAGE GATE scenario: PASS — fixture\n[PASS] a: evidence\n```\n'
        self.assertEqual(sg.digest_text(text), sg.digest_text(text + extra))
        self.assertNotIn('baseline', se.ancestors('scenario'))
        self.assertNotIn('baseline', se.ancestors('injection'))

    def record(self, **extra):
        args = dict(stage='scenario', revision='r1', inputs={'design':'abc'}, upstream={},
                    checks=[{'id':'review','outcome':'PASS'}], availability=[], reviewer='oracle',
                    tool_identity={'version':1}, policy_identity={'policy':'v3'})
        args.update(extra)
        return se.attest(self.root, **args)

    def test_immutable_idempotent_history_stale_and_deferred(self):
        original = self.record()
        self.assertEqual(self.record(), original)
        newer = self.record(inputs={'design':'changed'})
        self.assertEqual(newer['supersedes'], original['evidence_id'])
        self.assertTrue((self.root/se.DIRECTORY/(original['evidence_id']+'.json')).is_file())
        args = dict(task_id=se.task_identity(self.root),stage='scenario',inputs={'design':'abc'},upstream={})
        self.assertEqual(se.validate(original, **args), [])
        args['inputs'] = {'design':'changed'}
        self.assertTrue(se.validate(original, **args))
        availability = [{'id':'SQL source','state':'deferred','required_at':'injection','reason':'design precedes construction'}]
        self.assertEqual(se.availability_errors(availability,'scenario'), [])
        self.assertTrue(se.availability_errors(availability,'injection'))
        self.assertTrue(se.validate(None, **args))

    def test_evaluator_difference_is_review_not_authority(self):
        original = self.record()
        self.assertEqual(se.evaluator_compatibility('v1','v2')['status'],'REVIEW_REQUIRED')
        self.assertEqual(se.evaluator_compatibility('v2','v1')['status'],'REVIEW_REQUIRED')
        self.assertEqual(original['policy_identity'],{'policy':'v3'})

    def exports(self):
        paths=[]
        for n in range(1,7):
            path=self.root/f'arbitrary-{7-n}.json'
            path.write_text(json.dumps([{'type':'system','subtype':'init','session_id':f'S-{n}','model':'claude-opus-5-5'},
                {'type':'assistant','message':{'content':[{'type':'text','text':f'Created decision-{n}'}]}},
                {'type':'result','subtype':'success','session_id':f'S-{n}','is_error':False}]))
            paths.append(path)
        verifier=self.root/'verifier.txt'
        verifier.write_text('Task ID: task\nRevision: r2\nBundle SHA256: bundle\n'+''.join(
            f'Run #{n}\nSession ID: S-{n}\nExport SHA256: {sha(path)}\nPass\nRow\nEnd-state ticket-{n} exists.\n'
            for n,path in enumerate(paths,1)))
        return verifier,paths

    def test_vincent_style_binding_ignores_names_and_rejects_superseded(self):
        verifier,paths=self.exports()
        result=tl.bind_verifier_exports(verifier,paths[::-1],task_id='task',revision='r2',bundle_hash='bundle')
        self.assertEqual(result['runs'][1], paths[0])
        moved=[]
        for n,p in enumerate(paths):
            q=self.root/f'run-{(n+3)%6+1}.json'; p.rename(q); moved.append(q)
        result=tl.bind_verifier_exports(verifier,moved[::-1],task_id='task',revision='r2',bundle_hash='bundle')
        self.assertEqual(result['runs'][1], moved[0])
        moved[0].write_text(moved[0].read_text().replace('decision-1','superseded-decision'))
        with self.assertRaises(ValueError):
            tl.bind_verifier_exports(verifier,moved,task_id='task',revision='r2',bundle_hash='bundle')

    def test_reviewed_binding_requires_discriminating_run_observations(self):
        verifier,paths=self.exports()
        proof=self.root/'run-map.txt';proof.write_text('Independent review associated each created decision with corresponding end-state ticket.')
        receipt={'schema_version':1,'kind':'VERIFIER_EXPORT_BINDING','task_id':'task','revision':'r2','bundle_hash':'bundle',
                 'verifier_sha256':sha(verifier),'source':'reviewed-comparison','reviewer':'independent oracle',
                 'reason':'Reviewed write payload and verifier end state for each run.',
                 'evidence':[{'path':proof.name,'sha256':sha(proof),'reason':'Comparison ledger preserves source observations.'}],
                 'runs':[{'number':n,'export_sha256':sha(p),'comparison':{
                     'reason':'Created decision maps to observed ticket.', 'export_observation':f'Created decision-{n}',
                     'verifier_observation':f'End-state ticket-{n} exists.'}} for n,p in enumerate(paths,1)]}
        args={'task_id':'task','revision':'r2','bundle_hash':'bundle','task_dir':self.root,'receipt':receipt}
        self.assertEqual(tl.bind_verifier_exports(verifier,paths,**args)['verdict'],'BOUND')
        receipt['runs'][0]['comparison']['export_observation']='type'
        receipt['runs'][0]['comparison']['verifier_observation']='Run'
        with self.assertRaises(ValueError):tl.bind_verifier_exports(verifier,paths,**args)

    def test_filenames_and_task_context_are_insufficient(self):
        verifier,paths=self.exports()
        verifier.write_text('Run #1\nPass\nRow\nExisting ticket observed.\n')
        with self.assertRaises(ValueError):
            tl.bind_verifier_exports(verifier,paths,task_id='task',revision='r2',bundle_hash='bundle')

    def platform(self):
        proof=self.root/'platform.txt';proof.write_text('Fresh deployment E from base, final state Z; reads A/B; no manual edits.')
        refs=[{'path':'platform.txt','sha256':sha(proof),'reason':'Recorded deployment and reads match state Z.'}]
        rec=dict(schema_version=1,task_id='task',revision='r1',universe='synthcut',bundle_hash='bundle',
                 reviewer='oracle',reason='Evidence checked',environment_id='E',environment_state_id='Z',
                 injection={'state':'not-used','sha256':None},manual_changes=[],baseline_run_ids=[])
        for k in ('fresh_base','application','readability'):
            rec[k]={'verified':True,'environment_state_id':'Z','evidence':refs}
        rec['fresh_base']['source']='base-universe'
        rec['readability'].update(decisive_records=['A','B'],tool_assumptions=['reader v1'])
        args=dict(task_dir=self.root,task_id='task',revision='r1',universe='synthcut',sql_hash=None,bundle_hash='bundle')
        return rec,args

    def test_no_injection_pending_runs_and_postbaseline_association(self):
        rec,args=self.platform()
        self.assertEqual(ph.validate(rec,**args),[])
        self.assertTrue(ph.validate(None,**args))
        self.assertTrue(ph.validate(rec,**dict(args,task_id='other')))
        self.assertTrue(ph.validate(rec,**args,run_ids=['S-1']))
        rec['baseline_run_ids']=['S-1']
        self.assertEqual(ph.validate(rec,**args,run_ids=['S-1']),[])
        (self.root/'platform.txt').write_text('changed environment')
        self.assertTrue(ph.validate(rec,**args))

    def test_four_task_transactions_and_conflicts(self):
        context=multiprocessing.get_context('spawn')
        path=self.root/'shared-ledger.jsonl'
        barrier,queue=context.Barrier(4),context.Queue()
        workers=[context.Process(target=ledger_worker,args=(path,f'task-{i}','LANDED',barrier,queue)) for i in range(4)]
        for p in workers:p.start()
        results=[queue.get(timeout=30) for p in workers]
        for p in workers:p.join(30); self.assertEqual(p.exitcode,0)
        self.assertEqual(len(Ledger(path).records),4)
        self.assertTrue(all(len(r['added'])==1 for r in results))
        old=Ledger(path).records[0]
        self.assertEqual(len(Ledger(path).append([old])['present']),1)
        altered=dict(old,verdict='LEAKED')
        self.assertEqual(len(Ledger(path).append([altered])['rejected']),1)

    def design_fixture(self, stage='scenario'):
        # Distinct budget decisions for three regions, each with two requested figures.
        note = self.root/'decision-evidence.txt'
        note.write_text('West/East/North current dated policies; each correction changes its own budget and allocation. Search returns original and policy pointer; reviewer checked reach.')
        ref = {'path':note.name,'sha256':sha(note)}
        def proof(**extra):
            return {'reason':'Dated region authority and independent output comparison inspected.', 'evidence':[ref], **extra}
        mids=['west','east','north']
        man={'difficulty_mode':'medium','mechanism_portfolio':[{'id':m,'mechanism':'A15','requirement':m} for m in mids]}
        surface={'slots':[]}
        review={'schema_version':1,'stage':stage,'task_id':'oracle','revision':'r1','reviewer':'independent oracle',
                'difficulty_mode':'medium','diversity_channels':mids,'mechanisms':{},'dispositions':{}}
        prompt='Publish each region budget and allocation.'
        for mid in mids:
            slots=[mid+'-budget',mid+'-allocation']
            for sid in slots:
                surface['slots'].append({'id':sid,'fact_id':sid,'weight':5,'work_kind':'multi_source_reconciliation',
                    'work_reason':'reconcile dated region policy and resource record','mechanisms':[mid],
                    'incorporating_span':prompt,'role':'core'})
            row={key:proof() for key in ('initial_plausible_answer','deciding_evidence','authority_chronology','fair_discovery_path','changed_outcome','independent_operation')}
            row['deciding_evidence']['record_id']=mid+'-policy'
            row['changed_outcome'].update(before=10,after=8)
            row['independent_operation']['others_solvable_if_missed']=[m for m in mids if m!=mid]
            row.update(channel_kind='policy reconciliation',outcome_slots=slots,
                outcome_pair=proof(slots=slots,left_pass_right_fail='budget corrected but allocation uses old rule',right_pass_left_fail='allocation correct but budget uses stale input'))
            if stage=='scenario':
                row.update(access={'status':'deferred','required_at':'injection'},natural_retrieval={'status':'deferred','required_at':'injection'})
            else:
                row.update(access=proof(status='verified'),natural_retrieval=proof(query='region policy',returned_ids=[mid+'-policy'],assessment='initial summary does not decide updated allocation'))
            review['mechanisms'][mid]=row
        args={'task_dir':self.root,'task_id':'oracle','revision':'r1','difficulty_mode':'medium','prompt':prompt if stage!='scenario' else ''}
        for f in hv.run(man,'',args['prompt'],surface)['flags']:
            review['dispositions'][f['check']+':'+str(f.get('node') or '-')]=proof(status='not_applicable')
        review['semantic_prompt_review']=proof(leaks_solution=False)
        review['input_hashes']=dr.input_hashes(stage,man,surface,prompt=args['prompt'])
        return man,surface,review,args

    def test_design_early_stage_and_advisory_forecast(self):
        man,surface,review,args=self.design_fixture()
        review['forecast']={'p_all_gates':0.0}
        self.assertEqual(dr.evaluate('scenario',man,surface,review,**args)['verdict'],'PASS')
        self.assertFalse((self.root/'01_Universe_Inject.sql').exists())
        review['mechanisms']['west']['access']={'status':'inaccessible','reason':'reviewed'}
        self.assertEqual(dr.evaluate('scenario',man,surface,review,**args)['verdict'],'FAIL')

    def test_scope_duplicate_and_stale_evidence_reject(self):
        man,surface,review,args=self.design_fixture('prompt')
        self.assertEqual(dr.evaluate('prompt',man,surface,review,**args)['verdict'],'PASS')
        original=copy.deepcopy(surface)
        surface['slots'][0]['incorporating_span']='Explain every internal decision.'
        review['input_hashes']=dr.input_hashes('prompt',man,surface,prompt=args['prompt'])
        self.assertEqual(dr.evaluate('prompt',man,surface,review,**args)['verdict'],'FAIL')
        surface=copy.deepcopy(original);surface['slots'][1]['fact_id']=surface['slots'][0]['fact_id']
        review['input_hashes']=dr.input_hashes('prompt',man,surface,prompt=args['prompt'])
        self.assertEqual(dr.evaluate('prompt',man,surface,review,**args)['verdict'],'FAIL')
        surface=original;review['input_hashes']=dr.input_hashes('prompt',man,surface,prompt=args['prompt'])
        (self.root/'decision-evidence.txt').write_text('stale replacement')
        self.assertEqual(dr.evaluate('prompt',man,surface,review,**args)['verdict'],'FAIL')

    def test_attested_review_proof_change_invalidates_readiness(self):
        import readiness_controls as rc
        man,surface,review,args=self.design_fixture()
        review['task_id']=se.task_identity(self.root)
        working=self.root/'Working_Files';working.mkdir(exist_ok=True)
        (working/'hardness_reviews').mkdir()
        (working/'00_Readiness_Config.json').write_text(json.dumps({'schema_version':1,'revision':'r1','injection':'required'}))
        (working/'01_Hardness_Manifest.draft.json').write_text(json.dumps(man))
        (working/'01_Gradable_Surface.json').write_text(json.dumps(surface))
        (working/'hardness_reviews/scenario.json').write_text(json.dumps(review))
        (working/'01_Scenario_Design.md').write_text('Independent design')
        (self.root/'00_Assigments.md').write_text('Independent assignment')
        ctx=sg.Ctx('scenario',self.root);ctx.context={'difficulty_mode':'medium'}
        # No full gate is claimed here: directly exercise its saved-evidence consumer.
        with patch.object(sg,'virtual_digests',return_value={}):
            se.attest(self.root,stage='scenario',revision='r1',inputs=rc.inputs(sg,ctx,'scenario'),upstream={},
                checks=[{'id':cid,'outcome':'PASS'} for cid in ('structure.inputs','structure.outputs','readiness.context')],
                producer={'name':'stage_gate','stage':'scenario','rerun':'all','verdict':'PASS'},
                availability=[],reviewer='oracle',
                tool_identity=rc.tool_identity(sg,'scenario'),policy_identity=rc.policy_identity(sg))
            self.assertEqual(rc.current_errors(sg,ctx,'scenario'),[])
            (self.root/'07_Baseline_Trajectories').mkdir()
            (self.root/'07_Baseline_Trajectories/run.json').write_text('[]')
            self.assertEqual(rc.current_errors(sg,ctx,'scenario'),[])
            (self.root/'decision-evidence.txt').write_text('changed material proof')
            self.assertTrue(rc.current_errors(sg,ctx,'scenario'))

    def test_weight_and_required_write_coverage(self):
        man,surface,review,args=self.design_fixture('rubric')
        rubric=[{'id':slot['id'],'title':slot['id'],'weight':slot['weight']} for slot in surface['slots']]
        args['rubric']=rubric
        review['coverage']={slot['id']:{'rubric_ids':[slot['id']]} for slot in surface['slots']}
        review['input_hashes']=dr.input_hashes('rubric',man,surface,prompt=args['prompt'],rubric=rubric)
        self.assertEqual(dr.evaluate('rubric',man,surface,review,**args)['verdict'],'PASS')
        sid=surface['slots'][0]['id']
        review['coverage'][sid]={'status':'sampled_out','reason':'Sample only other regions','evidence':review['semantic_prompt_review']['evidence']}
        self.assertEqual(dr.evaluate('rubric',man,surface,review,**args)['verdict'],'FAIL')
        review['coverage'][sid]={'rubric_ids':[sid]}
        surface['slots'][0]['work_kind']='lookup'
        review['input_hashes']=dr.input_hashes('rubric',man,surface,prompt=args['prompt'],rubric=rubric)
        self.assertEqual(dr.evaluate('rubric',man,surface,review,**args)['verdict'],'FAIL')

    def test_generic_hardness_waiver_cannot_pass(self):
        man,surface,review,args=self.design_fixture()
        for disposition in review['dispositions'].values():disposition['reason']='reviewed'
        self.assertEqual(dr.evaluate('scenario',man,surface,review,**args)['verdict'],'FAIL')

    def mode_b_fixture(self):
        import mode_b_report as mb
        verifier,paths=self.exports()
        proof=self.root/'diagnosis.txt';proof.write_text('Region policy changed; first run repeated stale decision, evidence reviewed.')
        evidence={'reason':'Compared dated policy to actual first decision event.', 'evidence':[{'path':proof.name,'sha256':sha(proof)}]}
        blocks=['Task ID: task','Revision: r2','Bundle SHA256: bundle']
        runs=[]
        for n,path in enumerate(paths,1):
            results={'budget':n%2==0,'allocation':n%3==0}
            blocks.extend([f'Run #{n}',f'Export SHA256: {sha(path)}'])
            blocks.extend(f'{rid}\t'+('Pass' if passed else 'Fail')+'\tregion decision observed' for rid,passed in results.items())
            runs.append({'id':f'run-{n}','status':'completed','tool_calls':0,'results':results,
                         'models':['claude-opus-5-5'],'model_source':str(path)})
        verifier.write_text('\n'.join(blocks))
        data={'spec_version':'V3','difficulty_mode':'medium','task_type':'normal',
              'rubrics':[{'id':rid,'title':rid,'weight':5} for rid in ('budget','allocation')],'rollouts':runs}
        diagnosis={**copy.deepcopy(evidence),'id':'D','mechanism':'region-policy','observation':'dominant_pattern',
            'trajectory_events':[{'run':'run-1','export_sha256':sha(paths[0]),'event':1,'quote':'Created decision-1'}]}
        args={'verifier':verifier,'trajectories':paths,'task_id':'task','revision':'r2','bundle_hash':'bundle',
              'task_dir':self.root,'diagnoses':[diagnosis]}
        return data,args,evidence

    def test_mode_b_raw_corrections_and_actual_event(self):
        import mode_b_report as mb
        data,args,proof=self.mode_b_fixture()
        raw=copy.deepcopy(data)
        self.assertEqual(mb.build(data,**args)['verdict'],'PASS')
        data['rollouts'][0]['judge_corrections']={'budget':True}
        self.assertEqual(mb.build(data,**args)['verdict'],'FAIL')
        args['correction_evidence']={'run-1:budget':proof}
        report=mb.build(data,**args)
        self.assertEqual(report['verdict'],'PASS',report['blockers'])
        cell=report['heavy_rows'][0]['runs'][0]
        self.assertIs(cell['raw'],False);self.assertIs(cell['corrected'],True)
        self.assertEqual(data['rollouts'][0]['results'],raw['rollouts'][0]['results'])
        args['diagnoses'][0]['trajectory_events'][0]['event']=0
        self.assertEqual(mb.build(data,**args)['verdict'],'FAIL')

    def test_mode_b_allfail_cannot_hide_under_other_label(self):
        import mode_b_report as mb
        data,args,proof=self.mode_b_fixture()
        for run in data['rollouts']:run['results']['budget']=False
        text=args['verifier'].read_text().replace('budget\tPass','budget\tFail')
        args['verifier'].write_text(text)
        self.assertEqual(mb.build(data,**args)['verdict'],'FAIL')

    def test_error_slots_do_not_become_zero_scores(self):
        data,args,proof=self.mode_b_fixture()
        for run in data['rollouts'][-2:]:
            run['status']='errored';run.pop('results')
        before=copy.deepcopy(data)
        report=ds.compute(data)
        self.assertEqual(report['denominators']['completed_scores'],4)
        self.assertEqual(report['denominators']['errored_excluded'],2)
        self.assertEqual(data,before)

    def test_generic_import_cannot_claim_production_gate(self):
        request=dict(stage='scenario',revision='r1',inputs={'design':'abc'},upstream={},
            checks=[{'id':cid,'outcome':'PASS'} for cid in ('structure.inputs','structure.outputs','readiness.context')],
            availability=[],reviewer='importer',tool_identity={'version':1},policy_identity={'policy':'v3'},
            producer={'name':'stage_gate','stage':'scenario','rerun':'all','verdict':'PASS'})
        path=self.root/'import.json';path.write_text(json.dumps(request))
        result=subprocess.run([sys.executable,'-B',str(TOOLS/'stage_evidence.py'),'--task-dir',str(self.root),
                               '--record',str(path)],capture_output=True,text=True)
        record=se.latest(self.root,'scenario')
        self.assertTrue(result.returncode!=0 or not record or record.get('producer')!=request['producer'],
                        'generic import manufactured full-gate producer provenance')

    def test_precheck_identity_excludes_later_outputs_but_includes_references(self):
        prompt=self.root/'04_Prompt.txt';prompt.write_text('Prepare regional plan.\n')
        before=tl.binding_bundle_hash(self.root,stage='precheck')
        (self.root/'09_Rubrics.json').write_text('[]')
        (self.root/'08_Oracle_Events.md').write_text('Later oracle events.')
        self.assertEqual(before,tl.binding_bundle_hash(self.root,stage='precheck'))
        prompt.write_text(prompt.read_text()+'\n```\nSTAGE GATE prompt-check: PASS\n[PASS] example: checked\n```\n')
        self.assertEqual(before,tl.binding_bundle_hash(self.root,stage='precheck'))
        refs=self.root/'02_Reference_Files';refs.mkdir();(refs/'budget.csv').write_text('region,budget\nWest,8\n')
        after=tl.binding_bundle_hash(self.root,stage='precheck')
        self.assertNotEqual(before,after)
        (refs/'budget.csv').write_text('region,budget\nWest,9\n')
        self.assertNotEqual(after,tl.binding_bundle_hash(self.root,stage='precheck'))

    def test_evaluator_review_proof_must_be_substantive_and_fresh(self):
        proof=self.root/'release-review.txt';proof.write_text('Compared A/B release policies: only layout changed for this task.')
        review={'local':'A','reported':'B','compatible':True,'reviewer':'oracle','reason':'Compared applicable grading and policy requirements.',
                'evidence_refs':[{'path':proof.name,'sha256':sha(proof),'reason':'Exact release comparison.'}]}
        self.assertEqual(se.evaluator_compatibility('A','B',review,task_dir=self.root)['status'],'REVIEWED_COMPATIBLE')
        review['reason']='reviewed'
        self.assertEqual(se.evaluator_compatibility('A','B',review,task_dir=self.root)['status'],'REVIEW_REQUIRED')
        review['reason']='Compared applicable grading and policy requirements.'
        proof.write_text('Different release content')
        self.assertEqual(se.evaluator_compatibility('A','B',review,task_dir=self.root)['status'],'REVIEW_REQUIRED')

    def test_pair_must_survive_final_rubric_mapping(self):
        man,surface,review,args=self.design_fixture('rubric')
        rubric=[{'id':slot['id'],'title':slot['id'],'weight':slot['weight']} for slot in surface['slots']]
        args['rubric']=rubric
        review['coverage']={slot['id']:{'rubric_ids':[slot['id']]} for slot in surface['slots']}
        review['input_hashes']=dr.input_hashes('rubric',man,surface,prompt=args['prompt'],rubric=rubric)
        self.assertEqual(dr.evaluate('rubric',man,surface,review,**args)['verdict'],'PASS')
        review['coverage']['west-allocation']={'rubric_ids':['west-budget']}
        self.assertEqual(dr.evaluate('rubric',man,surface,review,**args)['verdict'],'FAIL')

    def test_production_mode_b_rejects_matrix_weight_and_policy_edits(self):
        import mode_b_report as mb
        data,args,proof=self.mode_b_fixture()
        (self.root/'09_Rubrics.json').write_text(json.dumps([{'title':r['title'],'weight':r['weight'],'category':'Outcome'} for r in data['rubrics']]))
        context={'task_dir':str(self.root),'task_identity':se.task_identity(self.root),'spec_version':'V3',
                 'difficulty_mode':'medium','difficulty_cap':.85,'task_type':'normal','assignment_hash':'a','context_hash':'c','policy_hash':'p'}
        bundle=tl.binding_bundle_hash(self.root)
        verifier=args['verifier']
        verifier.write_text(verifier.read_text().replace('Task ID: task','Task ID: '+context['task_identity']).replace('Bundle SHA256: bundle','Bundle SHA256: '+bundle))
        export_dir=self.root/'07_Baseline_Trajectories';export_dir.mkdir()
        exports=[]
        for path in args['trajectories']:
            new=export_dir/path.name;path.rename(new);exports.append(new)
        bound,_=ds.build(verifier,self.root/'09_Rubrics.json',export_dir,'normal',context=context,revision='r2')
        matrix=self.root/'matrix.json';matrix.write_text(json.dumps(bound))
        request={'data_path':matrix.name,'verifier':verifier.name,'trajectories':[str(p.relative_to(self.root)) for p in exports],
                 'task_id':context['task_identity'],'revision':'r2','bundle_hash':bundle,'diagnoses':args['diagnoses']}
        self.assertEqual(mb.from_request(request,self.root,context=context)['verdict'],'PASS')
        for key,value in [('weight',1),('spec_version','V2')]:
            changed=copy.deepcopy(bound)
            if key=='weight':changed['rubrics'][0][key]=value
            else:changed[key]=value
            matrix.write_text(json.dumps(changed))
            with self.assertRaises(ValueError):mb.from_request(request,self.root,context=context)

    def test_production_forensic_cli_confines_label_paths_and_outputs(self):
        other=self.root/'other-task';other.mkdir();(other/'00_Assigments.md').write_text('spec_version: V3')
        selected=self.root/'selected-task';selected.mkdir();(selected/'00_Assigments.md').write_text('spec_version: V3')
        events=[{'type':'system','subtype':'init','model':'claude-opus-5-5','session_id':'run'}, {'type':'result','subtype':'success','session_id':'run'}]
        for directory in (other,selected):(directory/'export.json').write_text(json.dumps(events))
        base=[sys.executable,'-B',str(TOOLS/'trajectory_ledger.py'),'--task-dir',str(selected),'--expected-model','claude-opus-5-5']
        cases=[(other/'export.json',selected/'output'),(selected/'export.json',other/'output')]
        for path,out in cases:
            result=subprocess.run(base+['--run','slot='+str(path),'--out-dir',str(out),'--json'],capture_output=True,text=True)
            self.assertNotEqual(result.returncode,0)
            self.assertFalse((out/'summary.json').exists())
        result=subprocess.run(base+['--run','slot='+str(selected/'export.json'),'--out-dir',str(selected/'output'),'--json'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertTrue((selected/'output/summary.json').exists())

    def test_repair_scope_outcomes_and_reruns_are_concrete(self):
        import mode_b_report as mb
        data,args,proof=self.mode_b_fixture()
        repair={**copy.deepcopy(proof),'id':'P','diagnosis':'D','original_placement':'Original region status summary',
                'proposed_change':'Place dated policy correction behind the linked policy record',
                'affected_outcomes':['budget'],'scope_difference':{'reason_class':'difficulty','rows_added':0},
                'change_kind':'evidence_placement','fair_discovery_path':'Existing summary points to region policy',
                'required_reruns':['scenario','injection'],'artifact':'universe','owner':'create-scenario --revise'}
        args['repairs']=[repair]
        self.assertEqual(mb.build(data,**args)['verdict'],'PASS')
        for field,bad in [('affected_outcomes',['INVENTED']),('scope_difference',{'reason_class':'difficulty'}),
                          ('required_reruns','none'),('change_kind','')]:
            wrong=copy.deepcopy(repair);wrong[field]=bad;args['repairs']=[wrong]
            self.assertEqual(mb.build(data,**args)['verdict'],'FAIL')
        wrong=copy.deepcopy(repair);wrong['change_kind']='volume_only';args['repairs']=[wrong]
        self.assertEqual(mb.build(data,**args)['verdict'],'FAIL')
        wrong['scope_difference']={'reason_class':'fairness','rows_added':1}
        self.assertEqual(mb.build(data,**args)['verdict'],'PASS')

    def test_mixed_task_inputs_reject(self):
        tasks=[]
        for n in range(4):
            task=self.root/f'task_inputs_{n}';task.mkdir();(task/'00_Assigments.md').write_text('spec_version: V3\n');tasks.append(task)
        with patch.dict(os.environ,{},clear=True),patch.object(tc,'BUNDLE',self.root):
            with self.assertRaises(ValueError):tc.select_task()
            self.assertEqual(tc.select_task(tasks[2]),tasks[2])
            with self.assertRaises(ValueError):tc.select_task(tasks[2],artifact_paths=[tasks[0]/'future.json'])

if __name__=='__main__':unittest.main()

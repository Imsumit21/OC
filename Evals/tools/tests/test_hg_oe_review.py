"""OE evidence/score contract regressions; no external model or workplace writes."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_oe_review as oe
import hg_eval_release as release
import hg_store_input as inputs
import hg_write_output as writer
from hg_report_contract import parse_result
from hg_rubric_loop import digest, review_context

PACKAGE = Path(__file__).resolve().parents[3]


def report(result):
    lines = ['### FINAL VERDICT: ' + result['verdict'], 'Execution status: ' + result['execution_status'],
             'Evaluator model: Opus 5.5 (claude-opus-5-5), xhigh effort', 'Next action: Review the supported findings', 'Evidence limits: ' + ('; '.join(result['unresolved']) or 'Static source verification')]
    for key, label in [('verdict_score','Score'),('completeness_score','Completeness score'),('accuracy_score','Accuracy score'),
                       ('review_policy','Review policy'),('reviewed_oe_sha256','Reviewed OE SHA-256'),
                       ('review_context_sha256','Review context SHA-256'),('oe_record_sha256','OE record SHA-256'),('path_feasibility','Path feasibility'),
                       ('task_solvability','Task solvability'),('prompt_follow_up','Prompt follow-up')]:
        if result.get(key) is not None: lines.append(label + ': ' + str(result[key]))
    lines += ['Eval version: ' + result['eval_release']['version'],
              'Eval release SHA-256: ' + result['eval_release']['manifest_sha256']]
    return '\n'.join(lines) + '\n'


class OEReviewTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        for name in ('REPOSITORY',):
            for module in (inputs, writer):
                scope = patch.object(module, name, self.root); scope.start(); self.addCleanup(scope.stop)
        bound_release = release.snapshot('oe')
        scope = patch.object(oe, 'snapshot', return_value=bound_release); scope.start(); self.addCleanup(scope.stop)
        inputs.save_input('prompt', content=b'Send an email to Chloe from Fatimah about a relocation proposal.')
        inputs.save_input('task-details', content=b'Fatimah, operations coordinator.')
        inputs.clear_input('injection', confirmed_unused=True)
        shutil.copytree(PACKAGE/'Evals/references/tools', self.root/'Evals/references/tools')
        self.data = self.root / 'contacts.json'
        self.data.write_text('{"Fatimah":"fatimah@example.test","Chloe":"chloe@example.test","proposal":"relocation"}')
        self.catalog = self.root / 'catalog.json'
        self.catalog.write_text('{"lookup":"Contacts lookup by name","send":"Gmail send from/to/subject/body"}')
        self.parts = ['Look up Fatimah and Chloe in Contacts; retrieve their email addresses.\n',
                      'Send the relocation proposal in Gmail from Fatimah to Chloe using those addresses.']
        inputs.save_input('oe', content=''.join(self.parts).encode())

    def source(self, sid, path, quote=None):
        raw = path.read_bytes()
        return dict(id=sid,path=str(path.relative_to(self.root)),sha256=digest(raw),quote=quote or raw.decode(),
                    visibility='VISIBLE', access='Synthetic fixture available to the assigned persona.')

    def record(self, missing_send=False):
        text = self.parts[0] if missing_send else ''.join(self.parts)
        if missing_send: inputs.save_input('oe', content=text.encode())
        record = {**oe.start(self.root), 'inventory_complete':True,'inventory_reason':'Lookup feeds the required email send.',
                  'sources':[self.source('P', self.root/'Evals/task_inputs/04_Prompt.txt'),self.source('D',self.data),self.source('T',self.catalog)],
                  'segments':[], 'steps':[], 'coverage':[]}
        cursor = 0
        for n, part in enumerate(self.parts[:1] if missing_send else self.parts, 1):
            sid='OE'+str(n)
            record['segments'].append(dict(start=cursor,end=cursor+len(part),quote=part,role='STEP',step_ids=[sid],reason='Supplied trajectory step.'))
            cursor+=len(part)
            checks={key:dict(result='VERIFIED',reason='Source and tool records establish the stated operation and values.',source_ids=['D','T']) for key in oe.FIELDS}
            if n==1: checks['dependencies']=dict(result='NOT_APPLICABLE',reason='First lookup uses the prompt names.')
            record['steps'].append(dict(id=sid,checks=checks,rubric_verification=dict(category='OUTCOME',reason='The sent email shows the correct people and proposal content.')))
        record['coverage']=[dict(id='R1',requirement='Discover the two contact addresses.',authority_chain=['P'],step_ids=['OE1'],result='COVERED',reason='Necessary discovery for sending the requested email.'),
                            dict(id='R2',requirement='Send the relocation email.',authority_chain=['P'],step_ids=[] if missing_send else ['OE2'],result='MISSING' if missing_send else 'COVERED',reason='The prompt expressly requests the send.')]
        def node(nid, step, tool, service, params, outputs):
            return dict(id=nid,step_ids=[step],oe_quote=self.parts[int(step[-1])-1],
                        mapping_reason='Descriptive lookup/send mapped to the actual bundled tool contract.',
                        mode='TOOL',depends_on=[],tool=tool,service=service,parameter_style='DESCRIPTIVE',
                        parameters=params,outputs=outputs)
        nodes=[node('fatimah','OE1','contacts_search_contacts','contacts',{'query':'Fatimah'},
                    {'email':dict(kind='SOURCE',source_id='D',pointer='/Fatimah')}),
               node('chloe','OE1','contacts_search_contacts','contacts',{'query':'Chloe'},
                    {'email':dict(kind='SOURCE',source_id='D',pointer='/Chloe')})]
        if not missing_send:
            nodes.append(node('send','OE2','gmail_send_message','gmail',
                              {'to':[{'$ref':'chloe.email'}], 'user_email':{'$ref':'fatimah.email'},
                               'body':'relocation proposal'}, {}))
        record['path_review']=dict(complete=True,reason='Maps all supplied contact lookup and send steps.',nodes=nodes,
            feasibility={field:dict(result='INCOMPLETE' if missing_send and field=='completion' else 'SUPPORTED',
                                    reason='Synthetic sources and persona establish the proposed path; absent send is recorded in coverage.' if missing_send else
                                           'Synthetic contact data, persona access and send capability cover the authorized email.',
                                    source_ids=['D','T']) for field in ('data_access','tool_capability','preconditions','completion')},
            runtime=dict(status='NOT_NEEDED',reason='Synthetic fixture has sufficient local evidence.'),upstream_blockers=[])
        record['format_review']=dict(checked=True,reason='Each step is numbered, names one action and its service, and gives the expected values.',findings=[])
        return record

    def validate(self, record=None):
        return oe.validate_record(self.root,json.dumps(record or self.record()))

    def test_complete_accurate_path_is_pass_5_5(self):
        result=self.validate()
        self.assertEqual((result['verdict'],result['completeness_score'],result['accuracy_score']),('PASS',5,5))

    def test_missing_send_fails_2_5(self):
        result=self.validate(self.record(missing_send=True))
        self.assertEqual((result['verdict'],result['completeness_score'],result['accuracy_score']),('FAIL',2,5))

    def test_wrong_service_parameter_identifier_and_data_fail(self):
        for field in ('tool_service','parameters','expected_data','dependencies'):
            record=self.record();record['steps'][1]['checks'][field]['result']='INACCURATE'
            result=self.validate(record)
            self.assertEqual((result['verdict'],result['completeness_score'],result['accuracy_score']),('FAIL',5,2))
            self.assertIn('OE2.'+field,result['inaccurate'])

    def test_proven_failure_survives_unresolved_evidence(self):
        record=self.record(missing_send=True);record['steps'][0]['checks']['expected_data']['result']='UNRESOLVED'
        result=self.validate(record)
        self.assertEqual((result['verdict'],result['verdict_score'],result['execution_status']),('FAIL',2,'PARTIAL'))

    def test_harmless_imprecision_has_separate_minor_category(self):
        record=self.record();record['steps'][1]['checks']['parameters']['result']='MINOR'
        result=self.validate(record)
        self.assertEqual((result['verdict'],result['accuracy_score']),('NON-FAIL',3))
        self.assertTrue(result['minor']);self.assertFalse(result['inaccurate'])

    def test_format_defect_is_non_fail_3_never_fail(self):
        record=self.record()
        record['format_review']['findings']=[dict(defect='MULTIPLE_ACTIONS',step_ids=['OE2'],quote=self.parts[1][:12],
                                                  reason='Two actions are packed into one OE.')]
        result=self.validate(record)
        self.assertEqual((result['verdict'],result['completeness_score'],result['accuracy_score']),('NON-FAIL',5,3))
        self.assertTrue(result['format_defects']);self.assertFalse(result['inaccurate'])

    def test_format_defect_does_not_soften_a_content_failure(self):
        record=self.record(missing_send=True)
        record['format_review']['findings']=[dict(defect='NO_NUMBER_OR_SERVICE',step_ids=['OE1'],quote=self.parts[0][:12],
                                                  reason='The step names no service.')]
        result=self.validate(record)
        self.assertEqual((result['verdict'],result['completeness_score'],result['accuracy_score']),('FAIL',2,3))

    def test_format_review_is_required_and_quotes_must_match(self):
        record=self.record();del record['format_review']
        with self.assertRaises(ValueError): self.validate(record)
        for bad in (dict(defect='STYLE',step_ids=['OE1'],quote=self.parts[0][:12],reason='x'),
                    dict(defect='JSON',step_ids=['OE1'],quote='not in the OE text',reason='x'),
                    dict(defect='JSON',step_ids=['OE9'],quote=self.parts[0][:12],reason='x')):
            record=self.record();record['format_review']['findings']=[bad]
            with self.assertRaises(ValueError): self.validate(record)

    def test_missing_material_parameter_is_completeness(self):
        record=self.record();record['steps'][1]['checks']['parameters']['result']='MISSING'
        result=self.validate(record)
        self.assertEqual((result['completeness_score'],result['accuracy_score']),(2,5))

    def test_read_step_can_be_verified_by_outcome(self):
        record=self.record();self.assertEqual(record['steps'][0]['rubric_verification']['category'],'OUTCOME')
        self.assertEqual(self.validate(record)['verdict'],'PASS')

    def test_process_requires_why_no_outcome(self):
        record=self.record();record['steps'][0]['rubric_verification']['category']='PROCESS'
        with self.assertRaisesRegex(ValueError,'why no Outcome'):self.validate(record)

    def test_unresolved_evidence_is_unscored_not_inaccurate(self):
        record=self.record();record['steps'][1]['checks']['expected_data']['result']='UNRESOLVED'
        result=self.validate(record)
        self.assertEqual((result['verdict'],result['verdict_score'],result['execution_status']),('NON-FAIL',None,'PARTIAL'))
        self.assertFalse(result['inaccurate'])

    def test_authoring_metadata_cannot_establish_accuracy_or_inaccuracy(self):
        for status in ('VERIFIED','INACCURATE'):
            record=self.record();record['sources'][1]['source_role']='AUTHORING_METADATA'
            record['steps'][1]['checks']['expected_data']['result']=status
            result=self.validate(record)
            self.assertIsNone(result['verdict_score']);self.assertFalse(result['inaccurate'])

    def test_oe_cannot_be_its_own_evidence(self):
        record=self.record();record['sources'][1]=self.source('D',self.root/oe.INPUT)
        self.assertIsNone(self.validate(record)['verdict_score'])

    def test_old_golden_is_not_an_oe_alias(self):
        inputs.clear_input('oe');inputs.save_input('golden',content=b'A correct final answer.')
        with self.assertRaises(ValueError):oe.start(self.root)

    def test_original_oe_upload_is_bound_without_conversion(self):
        f=self.root/'uploaded.txt';f.write_text(''.join(self.parts))
        inputs.save_input('source:oe',sources=[f]);record=self.record()
        self.assertIn('attachments/source/oe',record['oe_path']);self.assertEqual(self.validate(record)['verdict'],'PASS')

    def test_new_canonical_oe_wins_over_older_source_upload(self):
        f=self.root/'upload.txt';f.write_text('Old source')
        inputs.save_input('source:oe',sources=[f])
        inputs.save_input('oe',content=''.join(self.parts).encode())
        record=self.record()
        self.assertEqual(record['oe_path'],oe.INPUT.as_posix())
        self.assertEqual(self.validate(record)['verdict'],'PASS')

    def test_intake_requires_prompt_persona_and_injection_decision(self):
        for key in ('prompt','task-details','injection'):
            inputs.clear_input(key)
            with self.assertRaises(ValueError):oe.start(self.root)
            if key=='injection': inputs.clear_input(key,confirmed_unused=True)
            else: inputs.save_input(key,content=b'Supplied replacement')

    def test_binary_upload_requires_verified_extraction_and_preserves_original(self):
        f=self.root/'upload.docx';f.write_bytes(b'PK\xff\x00binary')
        inputs.save_input('source:oe',sources=[f])
        with self.assertRaisesRegex(ValueError,'verified text extraction'):oe.start(self.root)
        inputs.save_input('oe',content=''.join(self.parts).encode(),origin='Verified extraction of source:oe')
        self.assertEqual(oe.start(self.root)['oe_path'],oe.INPUT.as_posix())
        self.assertEqual((self.root/'Evals/task_inputs/attachments/source/oe/upload.docx').read_bytes(),f.read_bytes())

    def test_unpunctuated_or_5000_character_oe_is_not_automatically_corrupt(self):
        for raw in ('Look up the required record', 'x'*5000):
            inputs.save_input('oe',content=raw.encode())
            self.assertEqual(oe.start(self.root)['reviewed_oe_sha256'],digest(raw.encode()))

    def test_response_description_and_non_action_cap_at_non_fail(self):
        for role in ('RESPONSE_DESCRIPTION','NON_ACTION'):
            with self.subTest(role=role):
                record=self.record();record['segments'][1]['role']=role
                result=self.validate(record)
                self.assertEqual((result['verdict'],result['completeness_score']),('NON-FAIL',3))
                self.assertTrue(result['soft_defects'])

    def test_omitted_bad_step_cannot_bypass_inventory(self):
        record=self.record();record['segments'].pop()
        with self.assertRaisesRegex(ValueError,'all supplied text'):self.validate(record)

    def test_stale_prompt_or_oe_record_rejected(self):
        for key in ('prompt','oe'):
            record=self.record();inputs.save_input(key,content=b'Changed content')
            with self.assertRaisesRegex(ValueError,'stale binding'):self.validate(record)

    def test_changed_primary_source_quote_rejected(self):
        record=self.record();self.data.write_text('{"other":"value"}')
        with self.assertRaisesRegex(ValueError,'changed evidence'):self.validate(record)

    def test_saved_report_requires_exact_record_and_component_scores(self):
        record=self.record();result=writer.save_output('oe-review',json.dumps(record));text=report(result)
        self.assertEqual(writer.save_output('oe',text)['verdict'],'PASS')
        for a,b in [('Accuracy score: 5','Accuracy score: 3'),('OE record SHA-256: '+result['oe_record_sha256'],'OE record SHA-256: '+'0'*64)]:
            with self.assertRaises(ValueError):writer.save_output('oe',text.replace(a,b))

    def test_changed_review_archives_prior_report_and_preserves_input(self):
        record=self.record();raw=(self.root/oe.INPUT).read_bytes()
        result=writer.save_output('oe-review',json.dumps(record));writer.save_output('oe',report(result))
        record['steps'][1]['checks']['expected_data']['result']='INACCURATE'
        result=writer.save_output('oe-review',json.dumps(record));writer.save_output('oe',report(result))
        self.assertEqual((self.root/oe.INPUT).read_bytes(),raw)
        self.assertTrue(list((self.root/'Evals/task_inputs/reports/drafts/oe_history').glob('2_oe-*')))

    def test_oe_edit_invalidates_rubric_context(self):
        before=review_context(self.root)['sha256'];inputs.save_input('oe',content=b'Another path')
        self.assertNotEqual(before,review_context(self.root)['sha256'])

    def test_report_contract_allows_only_pass5_nonfail3_fail2(self):
        result=self.validate();text=report(result)
        for verdict,score in [('FAIL',1),('FAIL',2),('NON-FAIL',4)]:
            with self.assertRaises(ValueError):parse_result('oe',text.replace('FINAL VERDICT: PASS','FINAL VERDICT: '+verdict).replace('Score: 5','Score: '+str(score)))
        failed=report(self.validate(self.record(missing_send=True)))
        self.assertEqual(parse_result('oe',failed)['verdict'],'FAIL')

    def test_caller_supplied_score_cannot_override_record(self):
        record=self.record(missing_send=True);record.update(verdict='PASS',verdict_score=5)
        self.assertEqual(self.validate(record)['verdict_score'],2)

    def test_new_report_without_saved_evidence_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'Save oe-review'):writer.save_output('oe',report(self.validate()))

    def test_partial_and_blocked_without_fabricated_scores(self):
        for status in ('PARTIAL','BLOCKED'):
            text=f'### FINAL VERDICT: NON-FAIL\nExecution status: {status}\nNext action: Obtain evidence\nEvidence limits: OE input unavailable\n'
            self.assertIsNone(writer.save_output('oe',text)['verdict_score'])

    def test_release_inventory_distinguishes_current_and_historical_oe_reviews(self):
        result=writer.save_output('oe-review',json.dumps(self.record()))
        text=report(result);writer.save_output('oe',text)
        path=self.root/oe.REPORT
        self.assertEqual(release.classify_report(path,'oe')['classification'],'CURRENT_RELEASE')
        path.write_text(text.replace('Eval version: '+release.RELEASE,'Eval version: older-version'))
        self.assertEqual(release.classify_report(path,'oe')['classification'],'HISTORICAL_OR_UNBOUND')


class OEInstallerTests(unittest.TestCase):
    def setUp(self):
        tmp=tempfile.TemporaryDirectory();self.addCleanup(tmp.cleanup);self.root=Path(tmp.name)
        shutil.copytree(PACKAGE/'claude',self.root/'claude');(self.root/'Evals').mkdir();(self.root/'Evals/WORKFLOW.md').write_text('Fixture')
        spec=importlib.util.spec_from_file_location('oe_installer',self.root/'claude/install.py')
        self.installer=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.installer)

    def test_fresh_and_repeated_install_register_oe_without_golden(self):
        first=self.installer.install(self.root);second=self.installer.install(self.root)
        self.assertIn('oe',first['registered_skills']);self.assertNotIn('golden',first['registered_skills']);self.assertEqual(second['new_links'],0)

    def test_overlay_old_skill_is_not_registered_and_managed_link_retires(self):
        old=self.root/'claude/skills/golden';old.mkdir(exist_ok=True);(old/'SKILL.md').write_text('old')
        target=self.root/'.claude/skills';target.mkdir(parents=True);(target/'golden').symlink_to('../../claude/skills/golden')
        result=self.installer.install(self.root)
        self.assertEqual(result['retired_links'],['golden']);self.assertFalse((target/'golden').is_symlink());self.assertTrue((old/'SKILL.md').exists())

    def test_unowned_golden_is_preserved_and_install_does_not_partially_mutate(self):
        old=self.root/'.claude/skills/golden';old.mkdir(parents=True);(old/'custom').write_text('user')
        with self.assertRaisesRegex(ValueError,'not package-managed'):self.installer.install(self.root)
        self.assertEqual((old/'custom').read_text(),'user');self.assertFalse((old.parent/'oe').exists())

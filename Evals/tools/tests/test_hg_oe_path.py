"""OE path contract regressions, including a source-grounded delivery example.

These check helper behavior, not model accuracy, live actions or full task audits.
"""
import copy
import json
from pathlib import Path
import unittest

import test_hg_oe_review as fixture
from hg_oe_path import validate_path, task_fingerprints, type_matches, Symbol
from hg_review_evidence import EvidenceReader, sources
from hg_rubric_loop import digest
import hg_oe_review as oe
import hg_store_input as inputs
import hg_write_output as writer
from hg_report_contract import parse_result


class OEPathTests(unittest.TestCase):
    setUp = fixture.OEReviewTests.setUp
    source = fixture.OEReviewTests.source
    record = fixture.OEReviewTests.record
    validate = fixture.OEReviewTests.validate

    def path(self, record):
        reader=EvidenceReader(self.root)
        return validate_path(record['path_review'],record,reader,sources(reader,record['sources']),self.root,oe.context(self.root)['manifest'])

    def codes(self, result, key='inaccurate'):
        return {i['code'] for i in result[key]}

    def literal(self, payload):
        self.parts[1] += '\n' + json.dumps(payload)
        inputs.save_input('oe',content=''.join(self.parts).encode())
        record=self.record();node=record['path_review']['nodes'][-1]
        node.update(parameter_style='LITERAL',payload_quote=json.dumps(payload),parameters=payload)
        return record

    def add_source(self, record, sid, value, name=None):
        path=self.root/(name or sid+'.json');path.write_text(json.dumps(value))
        record['sources'].append(self.source(sid,path))
        return record['sources'][-1]

    def test_catalog_valid_path_supports_solvability(self):
        result=self.validate()
        self.assertEqual((result['path_feasibility'],result['task_solvability'],result['prompt_follow_up']),
                         ('SUPPORTED','SUPPORTED_BY_OE','NONE'))
        self.assertEqual(len(result['path_checks']['checks']),3)

    def test_qc_example_corpus_cannot_prove_new_task_facts_or_capability(self):
        for name in ('oracle_events_qc_cases.json', 'oracle_events_qc_examples.md'):
            for status in ('VERIFIED', 'INACCURATE'):
                record=self.record()
                path=self.root/'Evals/references/rules'/name
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_bytes((fixture.PACKAGE/'Evals/references/rules'/name).read_bytes())
                src=self.source('QC',path)
                src['source_role']='UNIVERSE_DATA'  # A misleading label cannot change provenance.
                record['sources'].append(src)
                record['steps'][0]['checks']['expected_data'].update(result=status,source_ids=['QC'])
                record['path_review']['nodes'][0]['outputs']['example_id']=dict(
                    kind='GENERATED',type='string',source_ids=['QC'],reason='Claims the old audit proves this tool capability.')
                result=self.validate(record)
                self.assertIsNone(result['verdict_score'])
                self.assertFalse(result['inaccurate'])
                self.assertEqual(result['task_solvability'],'NOT_ESTABLISHED')

    def test_wrong_service_is_broken_path_not_impossible_task(self):
        record=self.record();record['path_review']['nodes'][0]['service']='gmail'
        result=self.validate(record)
        self.assertEqual((result['accuracy_score'],result['path_feasibility'],result['task_solvability']),
                         (2,'BROKEN','NOT_ESTABLISHED'))
        self.assertEqual(result['prompt_follow_up'],'NONE')

    def test_unknown_tool_requires_alias_or_runtime_evidence(self):
        record=self.record();record['path_review']['nodes'][0]['tool']='unrecognized_new_tool'
        result=self.validate(record)
        self.assertIsNone(result['verdict_score']);self.assertFalse(result['inaccurate'])
        self.assertEqual(result['path_feasibility'],'UNRESOLVED')

    def test_wrong_parameter_name_and_type_are_detected(self):
        for params,code in [({'qurey':'Fatimah'},'UNKNOWN_PARAMETER'),({'query':17},'PARAMETER_TYPE'),
                            ({'query':'Fatimah','limit':True},'PARAMETER_TYPE')]:
            record=self.record();record['path_review']['nodes'][0]['parameters']=params
            self.assertIn(code,self.codes(self.path(record)))

    def test_descriptive_omission_of_api_scaffolding_not_automatic_defect(self):
        record=self.record();record['path_review']['nodes'][-1]['parameters']={}
        result=self.path(record)
        self.assertFalse(result['inaccurate']);self.assertFalse(result['unresolved'])
        self.assertEqual(result['checks'][-1]['descriptive_unlisted_inputs'],['to'])

    def test_literal_missing_required_argument_is_inaccurate(self):
        result=self.validate(self.literal({'body':'relocation proposal'}))
        self.assertIn('MISSING_CALL_ARGUMENT',self.codes(result['path_checks']))
        self.assertEqual(result['accuracy_score'],2)

    def test_literal_mapping_cannot_silently_repair_payload(self):
        record=self.literal({'body':'relocation proposal'});record['path_review']['nodes'][-1]['parameters']['to']=['chloe@example.test']
        with self.assertRaisesRegex(ValueError,'changed during reviewer mapping'):self.validate(record)

    def test_minor_descriptive_alias_preserves_minor_category(self):
        self.parts[0]+='Search term: Fatimah.\n';inputs.save_input('oe',content=''.join(self.parts).encode())
        record=self.record();self.add_source(record,'A',{'mapping':'In this descriptive instruction, Search term is the query, without changing the search.'})
        n=record['path_review']['nodes'][0];n['parameters']={'search_term':'Fatimah'}
        n['parameter_aliases']={'search_term':dict(canonical='query',oe_quote='Search term: Fatimah.',source_ids=['A'],reason='The described search term maps exactly to query; outcome unchanged.')}
        result=self.validate(record)
        self.assertEqual(result['accuracy_score'],3);self.assertTrue(result['minor']);self.assertFalse(result['inaccurate'])
        self.assertEqual(result['task_solvability'],'SUPPORTED_BY_OE')

    def test_exact_expected_value_is_compared_with_primary_source(self):
        self.parts[0]+='Fatimah address: "wrong@example.test".\n';inputs.save_input('oe',content=''.join(self.parts).encode())
        record=self.record();record['path_review']['nodes'][0]['outputs']['email'].update(expected='wrong@example.test',expected_quote='"wrong@example.test"')
        result=self.validate(record);self.assertIn('WRONG_EXPECTED_DATA',self.codes(result['path_checks']))
        self.assertEqual(result['accuracy_score'],2)

    def test_expected_value_needs_exact_quote_from_supplied_oe(self):
        record=self.record();record['path_review']['nodes'][0]['outputs']['email'].update(expected='fake',expected_quote='fake')
        with self.assertRaisesRegex(ValueError,'quote the actual OE'):self.validate(record)

    def test_downstream_changed_recipient_is_detected(self):
        record=self.record();n=record['path_review']['nodes'][-1]
        n['parameters']['to']=['elsewhere@example.test']
        n['input_bindings']=[dict(from_node='chloe',output='email',parameter_pointer='/to/0',reason='Recipient must be the discovered Chloe address.')]
        result=self.validate(record)
        self.assertIn('CHANGED_DOWNSTREAM_VALUE',self.codes(result['path_checks']));self.assertEqual(result['accuracy_score'],2)

    def test_downstream_same_recipient_and_nested_refs_are_valid(self):
        record=self.record();n=record['path_review']['nodes'][-1]
        n['input_bindings']=[dict(from_node='chloe',output='email',parameter_pointer='/to/0',reason='Recipient is the discovered address.')]
        self.assertEqual(self.validate(record)['verdict'],'PASS')

    def test_unavailable_output_does_not_cascade_to_wrong_value_or_type(self):
        for change in ('missing_output','unresolved','inaccessible'):
            record=self.record();nodes=record['path_review']['nodes'];out=nodes[0]['outputs']['email']
            if change=='missing_output':nodes[0]['outputs']={}
            elif change=='unresolved':nodes[0]['outputs']['email']={'kind':'UNRESOLVED','reason':'Data export incomplete.'}
            else:record['sources'][1]['visibility']='INACCESSIBLE'
            nodes[-1]['input_bindings']=[dict(from_node='fatimah',output='email',parameter_pointer='/user_email',reason='Same sender.')]
            result=self.path(record);self.assertTrue(result['unresolved']);self.assertFalse(result['inaccurate'])

    def test_unknown_producer_is_mapping_gap_not_authored_defect(self):
        record=self.record();record['path_review']['nodes'][-1]['parameters']['user_email']={'$ref':'omitted.email'}
        result=self.path(record)
        self.assertIn('UNKNOWN_DEPENDENCY',self.codes(result,'unresolved'));self.assertFalse(result['inaccurate'])

    def test_cycle_in_mapped_dependencies_is_inaccurate(self):
        record=self.record();record['path_review']['nodes'][0]['depends_on']=['send']
        result=self.validate(record);self.assertIn('DEPENDENCY_CYCLE',self.codes(result['path_checks']))
        self.assertEqual(result['task_solvability'],'NOT_ESTABLISHED')

    def test_independent_nodes_can_be_listed_in_different_order(self):
        record=self.record();record['path_review']['nodes'].reverse()
        self.assertEqual(self.validate(record)['verdict'],'PASS')

    def test_missing_or_incomplete_reviewer_mapping_cannot_pass(self):
        record=self.record();record.pop('path_review')
        with self.assertRaisesRegex(ValueError,'path_review is required'):self.validate(record)
        record=self.record();record['path_review']['nodes'].pop()
        with self.assertRaisesRegex(ValueError,'map every supplied step'):self.validate(record)
        record=self.record();record['path_review']['complete']=False
        self.assertIsNone(self.validate(record)['verdict_score'])

    def test_missing_required_action_is_incomplete_not_inaccurate(self):
        result=self.validate(self.record(missing_send=True))
        self.assertEqual((result['completeness_score'],result['accuracy_score'],result['path_feasibility'],result['task_solvability']),
                         (2,5,'INCOMPLETE','NOT_ESTABLISHED'))

    def test_each_feasibility_dimension_needs_evidence(self):
        for field in ('data_access','tool_capability','preconditions','completion'):
            record=self.record();record['path_review']['feasibility'][field].update(result='UNRESOLVED',reason='The required fact is unverified.')
            result=self.validate(record)
            self.assertIsNone(result['verdict_score']);self.assertEqual(result['task_solvability'],'NOT_ESTABLISHED')

    def blocked(self, record, field='tool_capability'):
        src=self.add_source(record,'BLOCK',{'policy':'This fixture has no supported delivery route for the requested email.'})
        record['path_review']['feasibility'][field]=dict(result='BLOCKED',source_ids=['BLOCK'],reason='A direct policy prohibits this requested operation.',
            evidence_check=dict(method='DIRECT',reason='Direct supported capability contradiction, not search absence.',source_id='BLOCK',positive_evidence='no supported delivery route'))
        return record

    def test_supported_blocker_is_diagnostic_and_does_not_edit_prompt(self):
        record=self.blocked(self.record());original=(self.root/'Evals/task_inputs/04_Prompt.txt').read_bytes()
        prompt_report=self.root/'Evals/task_inputs/reports/1_prompt.md';prompt_report.parent.mkdir(exist_ok=True);prompt_report.write_text('Existing prompt report remains as evaluated.')
        record['path_review']['upstream_blockers']=[dict(requirement_id='R2',feasibility_field='tool_capability',reason='The requested email cannot be sent under this fixture policy.',
            source_ids=['BLOCK'],all_authorized_routes_ruled_out=True,alternatives_reason='The stated policy rules out every delivery route; the explicit email ask does not authorize another communication medium.')]
        result=writer.save_output('oe-review',json.dumps(record));writer.save_output('oe',fixture.report(result))
        self.assertEqual((result['verdict'],result['task_solvability'],result['prompt_follow_up']),('FAIL','UPSTREAM_BLOCKER','REQUIRED'))
        self.assertEqual((self.root/'Evals/task_inputs/04_Prompt.txt').read_bytes(),original)
        self.assertEqual(prompt_report.read_text(),'Existing prompt report remains as evaluated.')

    def test_single_path_blocker_with_allowed_alternative_does_not_mark_task_impossible(self):
        result=self.validate(self.blocked(self.record()))
        self.assertEqual((result['task_solvability'],result['prompt_follow_up']),('NOT_ESTABLISHED','NONE'))

    def test_upstream_blocker_must_link_specific_supported_blocked_check(self):
        record=self.blocked(self.record());record['path_review']['upstream_blockers']=[dict(requirement_id='R2',feasibility_field='data_access',reason='Claim',source_ids=['BLOCK'],all_authorized_routes_ruled_out=True,alternatives_reason='Explanation')]
        with self.assertRaisesRegex(ValueError,'specific blocked'):self.validate(record)

    def test_unavailable_blocker_evidence_remains_unresolved(self):
        record=self.blocked(self.record());record['sources'][-1]['visibility']='UNRESOLVED'
        result=self.validate(record);self.assertIsNone(result['verdict_score']);self.assertFalse(result['inaccurate'])
        self.assertEqual(result['task_solvability'],'NOT_ESTABLISHED')

    def test_blocked_feasibility_requires_direct_or_complete_absence_evidence(self):
        record=self.blocked(self.record());record['path_review']['feasibility']['tool_capability'].pop('evidence_check')
        with self.assertRaisesRegex(ValueError,'scope-bound absence'):self.validate(record)

    def test_no_runtime_connection_not_a_failure_when_static_evidence_suffices(self):
        self.assertEqual(self.validate()['verdict'],'PASS')
        record=self.record();record['path_review']['runtime'].update(status='UNAVAILABLE',reason='A necessary access question cannot be settled locally and no runtime is connected.')
        self.assertIsNone(self.validate(record)['verdict_score'])

    def runtime_record(self):
        record=self.record();s=record['sources'][1]
        receipt=dict(effect='READ_ONLY',task_fingerprints=task_fingerprints(oe.context(self.root)['manifest']),
                     source_fingerprints={s['path']:s['sha256']},observation='Synthetic receipt; no runtime was actually invoked.')
        self.add_source(record,'RUN',receipt)
        record['path_review']['runtime']=dict(status='OBSERVED',reason='Contract fixture only.',effect='READ_ONLY',receipt_source_id='RUN',bound_source_ids=['D'])
        return record

    def test_matching_read_only_receipt_can_be_validated(self):
        self.assertEqual(self.validate(self.runtime_record())['verdict'],'PASS')

    def test_stale_persona_task_or_source_receipt_is_unresolved(self):
        for key in ('task_fingerprints','source_fingerprints','effect'):
            record=self.runtime_record();s=record['sources'][-1];p=self.root/s['path'];r=json.loads(p.read_text());r[key]='stale'
            p.write_text(json.dumps(r));record['sources'][-1]=self.source('RUN',p)
            result=self.validate(record);self.assertIsNone(result['verdict_score'])
            self.assertIn('STALE_RUNTIME_EVIDENCE',self.codes(result['path_checks'],'unresolved'))

    def test_reported_runtime_write_is_rejected(self):
        record=self.runtime_record();record['path_review']['runtime']['effect']='WRITE'
        with self.assertRaisesRegex(ValueError,'never executes workplace writes'):self.validate(record)

    def test_verified_runtime_schema_can_resolve_unknown_catalog_tool(self):
        record=self.record();node=record['path_review']['nodes'][0];node['tool']='contacts_search_current'
        self.add_source(record,'SCHEMA',dict(name='contacts_search_current',service='contacts',parameters={'query':{'type':'string','required':'required'}}))
        node['runtime_schema']=dict(source_id='SCHEMA',pointer='')
        self.assertEqual(self.validate(record)['verdict'],'PASS')

    def test_unavailable_schema_does_not_bypass_service_check(self):
        record=self.record();node=record['path_review']['nodes'][0];node['service']='gmail'
        self.add_source(record,'SCHEMA',{});record['sources'][-1]['visibility']='UNRESOLVED'
        node['runtime_schema']=dict(source_id='SCHEMA',pointer='')
        result=self.path(record);self.assertIn('WRONG_SERVICE',self.codes(result));self.assertTrue(result['unresolved'])

    def test_historical_v1_report_readable_but_not_current_publication(self):
        result=self.validate();text=fixture.report(result).replace('oracle-events-v2','oracle-events-v1')
        text='\n'.join(l for l in text.splitlines() if not l.startswith(('Path feasibility:','Task solvability:','Prompt follow-up:')))+'\n'
        self.assertEqual(parse_result('oe',text)['review_policy'],'oracle-events-v1')
        writer.save_output('oe-review',json.dumps(self.record()))
        with self.assertRaises(ValueError):writer.save_output('oe',text)

    def test_diagnostics_cannot_be_omitted_or_changed_to_unsupported_solvability(self):
        record=self.record();result=writer.save_output('oe-review',json.dumps(record));text=fixture.report(result)
        for changed in (text.replace('Task solvability: SUPPORTED_BY_OE\n',''),text.replace('Path feasibility: SUPPORTED','Path feasibility: BROKEN')):
            with self.assertRaises(ValueError):writer.save_output('oe',changed)

    def delivery(self, full_original=False):
        f=json.loads((fixture.PACKAGE/'Evals/tools/tests/fixtures/oe_delivery_397a.json').read_text())
        prompt=f['prompt'] if full_original else 'Constructed test request: send the supplied sample numbers to Michelle Carter on Slack.'
        inputs.save_input('prompt',content=prompt.encode());inputs.save_input('task-details',content=b'Constructed persona with Slack sending permission; source-grounded delivery slice only.')
        self.parts=['Look up Michelle Carter in Contacts, then find her Slack user using michelle.carter@harmonygames.co; expect "U1E2A024076".\n',
                    'Create a direct conversation with Michelle using that Slack user ID, then send the already-verified numbers to its resulting channel.']
        inputs.save_input('oe',content=''.join(self.parts).encode());record=self.record()
        self.add_source(record,'CONTACT',f['sources'][0]['value']);self.add_source(record,'SLACK',f['sources'][1]['value'])
        for sid in ('CONTACT','SLACK'):
            record['sources'][-2 if sid=='CONTACT' else -1]['access']='Source-grounded fixture; persona permission supplied by synthetic request setup, not inferred from the actual full task.'
        self.add_source(record,'CAPABILITY',{'operation':'Synthetic capability fixture: create direct conversation with user_ids; result supplies a channel identifier; sending to that channel delivers to its members.'})
        def n(nid,step,tool,service,params,out,depends=None):
            return dict(id=nid,step_ids=[step],oe_quote=self.parts[int(step[-1])-1],mapping_reason='Constructed delivery slice maps to catalog tools and actual Michelle identity records.',mode='TOOL',depends_on=depends or [],
                        tool=tool,service=service,parameter_style='DESCRIPTIVE',parameters=params,outputs=out)
        record['path_review']['nodes']=[
            n('contact','OE1','contacts_search_contacts','contacts',{'query':'Michelle Carter'},{'email':dict(kind='SOURCE',source_id='CONTACT',pointer='/email')}),
            n('slack','OE1','slack_search_users','slack',{'query':{'$ref':'contact.email'}},{'user':dict(kind='SOURCE',source_id='SLACK',pointer='/id',expected='U1E2A024076',expected_quote='"U1E2A024076"')}),
            n('dm','OE2','slack_create_conversation','slack',{'name':'Michelle Carter','is_im':True,'user_ids':[{'$ref':'slack.user'}]},
              {'channel':dict(kind='GENERATED',type='string',source_ids=['CAPABILITY'],reason='A new channel ID is produced, not hardcoded.')}),
            n('send','OE2','slack_send_message','slack',{'channel':{'$ref':'dm.channel'},'text':'Supplied sample numbers'}, {})]
        record['coverage']=[dict(id='DELIVERY',requirement='Send the supplied numbers to Michelle Carter on Slack.',authority_chain=['P'],step_ids=['OE1','OE2'],result='COVERED',reason='Narrow synthetic delivery task based on an actual identity record.')]
        record['path_review']['reason']='Delivery subpath only; other original task requirements are not established.'
        for step in record['steps']:
            step['rubric_verification']['reason']='Delivery to Michelle can be verified by the resulting sent message.'
            for c in step['checks'].values():
                if c['result']=='VERIFIED':c.update(source_ids=['CONTACT','SLACK','CAPABILITY'],reason='Constructed path using actual identity records and catalog tools; synthetic permission/capability fixture.')
        for c in record['path_review']['feasibility'].values():c.update(source_ids=['CONTACT','SLACK','CAPABILITY'],reason='This synthetic delivery request is limited to a known identity and provided payload.')
        if full_original:
            inj=inputs.save_input('injection',content=f['delivery_quote'].encode())
            record['sources'].append(self.source('I',self.root/'Evals/task_inputs/01_Universe_Inject.sql'))
            record['sources'][-1].update(incorporated_by='P',incorporation_reason='The prompt incorporates the Arthur DM; this fixture contains its delivery passage only.')
            record['coverage'][0].update(authority_chain=['P','I'],reason='Delivery is part of the incorporated DM; the rest of the original task was not assessed.')
            record['inventory_complete']=False;record['inventory_reason']='Only the delivery subpath is modeled, not the original financial analysis.'
            record.update(oe.start(self.root))
        return record

    def test_real_source_delivery_chain_uses_generated_channel_symbolically(self):
        result=self.validate(self.delivery())
        self.assertEqual(result['verdict'],'PASS');self.assertFalse(result['path_checks']['inaccurate'])

    def test_real_source_changed_michelle_recipient_detected(self):
        record=self.delivery();n=record['path_review']['nodes'][2];n['parameters']['user_ids']=['WRONG_USER']
        n['input_bindings']=[dict(from_node='slack',output='user',parameter_pointer='/user_ids/0',reason='DM must use the discovered Michelle ID.')]
        self.assertIn('CHANGED_DOWNSTREAM_VALUE',self.codes(self.path(record)))

    def test_generated_output_with_unavailable_capability_is_unresolved(self):
        record=self.delivery();record['sources'][-1]['visibility']='UNRESOLVED'
        result=self.path(record);self.assertTrue(result['unresolved']);self.assertFalse(result['inaccurate'])

    def test_invented_channel_does_not_equal_generated_channel(self):
        record=self.delivery();n=record['path_review']['nodes'][-1];n['parameters']['channel']='FAKE_CHANNEL'
        n['input_bindings']=[dict(from_node='dm',output='channel',parameter_pointer='/channel',reason='Send to the newly created conversation.')]
        self.assertIn('CHANGED_DOWNSTREAM_VALUE',self.codes(self.path(record)))

    def test_real_delivery_slice_cannot_claim_full_original_task_solved(self):
        result=self.validate(self.delivery(full_original=True))
        self.assertIsNone(result['verdict_score']);self.assertEqual(result['task_solvability'],'NOT_ESTABLISHED')

    def test_union_types_and_unknown_symbols(self):
        self.assertTrue(type_matches(Symbol('new','integer'),'string | number | null'))
        self.assertIsNone(type_matches(Symbol('unknown','unresolved'),'string'))
        self.assertFalse(type_matches(True,'integer'))

if __name__=='__main__':unittest.main()

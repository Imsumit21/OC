"""Assertion-inventory and legacy-record regressions, not automated NLP grading."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hg_rubric_assertions import validate_assertions
from hg_rubric_loop import digest, DRAFT, FINAL, POLICY, review_context
from hg_rubric_review import validate_record
import hg_store_input as inputs
import hg_write_output as writer
from test_hg_rubric_loop import review_record, review, assertion_inventory, golden_pass

DATA = json.loads((Path(__file__).parent/'fixtures/rubric_assertion_cases.json').read_text())
CASES = {c['id']: c for c in DATA['cases']}


class AssertionInventoryTests(unittest.TestCase):
    def setUp(self):
        self.case = copy.deepcopy(CASES['user1_split_begin_level'])

    def validate(self):
        return validate_assertions(self.case['assertion_inventory'],self.case['criterion'],self.case['atomicity'])

    def test_all_stated_boundaries(self):
        for case in DATA['cases']:
            with self.subTest(case=case['id']):
                pending=validate_assertions(case['assertion_inventory'],case['criterion'],case['atomicity'])
                if case['expected']=='CLEAR':
                    self.assertEqual(pending,[])
                else:
                    self.assertTrue(any(case['expected'] in p for p in pending),pending)

    def test_prior_approval_list_controls_follow_current_policy(self):
        fixtures = Path(__file__).parent / 'fixtures'
        for filename, label in [('rubric_case_expectations.json', 'R'),
                                ('rubric_atomicity_expectations.json', 'V5-06')]:
            with self.subTest(label=label):
                expected = json.loads((fixtures / filename).read_text())
                self.assertEqual(expected['expected'][label], 'ISSUE')
                case = CASES['legacy_' + label + '_approval_bundle']
                self.assertTrue(validate_assertions(case['assertion_inventory'],
                                                    case['criterion'], case['atomicity']))

    def test_multiple_assertions_cannot_clear_under_one_outcome_id(self):
        self.case=copy.deepcopy(CASES['user1_same_outcome_id'])
        self.assertEqual(len(self.case['atomicity']['outcome_ids']),1)
        self.assertTrue(any('multiple required assertions' in p for p in self.validate()))

    def test_collapsed_per_entity_property_still_needs_splitting(self):
        assertion=self.case['assertion_inventory']['assertions'][0]
        assertion['entities']=['begin_level','left_level','notification_permission']
        self.assertTrue(any('per-entity properties' in p for p in self.validate()))

    def test_implementation_list_cannot_use_identity_membership_exception(self):
        assertion=self.case['assertion_inventory']['assertions'][0]
        assertion['kind']='IDENTITY_SET'
        self.case['atomicity']['exception']=dict(kind='identity_only_set',reason='Claims one implemented-event list.')
        self.assertTrue(any('identity-only membership' in p for p in self.validate()))

    def test_required_result_in_evidence_is_not_hidden(self):
        a=self.case['assertion_inventory']['assertions'][0]
        a['field']='evidence'
        a['quote']=self.case['criterion']['evidence']
        self.assertTrue(any('hidden in a supporting field' in p for p in self.validate()))

    def test_supporting_history_requires_successful_omission_test(self):
        for result in ('REJECT','UNRESOLVED'):
            self.case=copy.deepcopy(CASES['user5_concise_repair'])
            self.case['assertion_inventory']['assertions'][1]['omission_test']['result']=result
            with self.subTest(result=result):
                self.assertTrue(any('extra acceptance requirement' in p for p in self.validate()))

    def test_unrequested_detail_is_removed_not_given_an_invented_outcome(self):
        self.case=copy.deepcopy(CASES['user2_unrequested_date'])
        self.assertTrue(any('UNREQUESTED_REQUIREMENT' in p for p in self.validate()))
        self.case['assertion_inventory']['assertions'][-1]['outcome_id']='status'
        with self.assertRaisesRegex(ValueError,'must not invent an outcome'):
            self.validate()

    def test_incomplete_and_unresolved_inventories_stay_open(self):
        self.case['assertion_inventory']['complete']=False
        self.assertTrue(any('incomplete' in p for p in self.validate()))
        a=self.case['assertion_inventory']['assertions'][0]
        a.update(role='UNRESOLVED',outcome_id=None,repair='Resolve whether the prompt requires this fact.')
        self.assertTrue(any('UNRESOLVED' in p for p in self.validate()))

    def test_quote_must_exist_in_exact_saved_field(self):
        self.case['assertion_inventory']['assertions'][0]['quote']='an invented requirement'
        with self.assertRaisesRegex(ValueError,'absent'):
            self.validate()

    def test_missing_or_malformed_inventory_rejected(self):
        for inventory in (None,{},dict(complete=True,reason='Checked',assertions=[])):
            with self.subTest(inventory=inventory), self.assertRaises(ValueError):
                validate_assertions(inventory,self.case['criterion'],self.case['atomicity'])
        for field,value in [('role','ONE_FINDING'),('entities',[]),('entities',['a','A']),('field',[]),('outcome_id','unknown')]:
            self.case=copy.deepcopy(CASES['user1_split_begin_level'])
            self.case['assertion_inventory']['assertions'][0][field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):self.validate()

    def test_missing_required_result_and_missing_outcome_cannot_clear(self):
        self.case['assertion_inventory']['assertions'][0]['role']='QUALIFIER'
        self.assertTrue(any('no independently required' in p for p in self.validate()))
        self.case=copy.deepcopy(CASES['user1_split_begin_level'])
        self.case['atomicity']['outcome_ids'].append('omitted')
        self.assertTrue(any('do not cover' in p for p in self.validate()))

    def test_relationship_requires_a_specific_conclusion(self):
        self.case=copy.deepcopy(CASES['one_comparison'])
        del self.case['assertion_inventory']['assertions'][0]['conclusion']
        with self.assertRaisesRegex(ValueError,'conclusion'):self.validate()

    def test_aggregate_requires_eligible_exception(self):
        self.case=copy.deepcopy(CASES['aggregate_control'])
        self.case['atomicity']['exception']=None
        self.assertTrue(any('narrow atomic exception' in p for p in self.validate()))


class AssertionRecordTests(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root=Path(temp.name)
        self.addCleanup(patch.stopall)
        patch.object(writer,'REPOSITORY',self.root).start()
        patch.object(inputs,'REPOSITORY',self.root).start()
        inputs.save_input('universe', content=b'2026-02-14\n')  # task date (hg_universe.py)
        self.prompt='Create a Linear issue reporting the implementation status of begin_level, left_level and notification_permission individually.'
        inputs.save_input('prompt',content=self.prompt.encode())
        inputs.save_input('golden',content=b'Fixture facts: begin_level, left_level and notification_permission are implemented.')
        inputs.save_input('task-details',content=b'Victor Barnes, Engineering, Retrieval, Normal')
        inputs.clear_input('injection',confirmed_unused=True)
        golden_pass(self.root, prompt=self.prompt.encode(), golden_text=b'Fixture facts: begin_level, left_level and notification_permission are implemented.', quote='implemented')

    def receipt(self, proposal):
        return dict(review_policy=POLICY, review_iteration=1,
                    reviewed_json_sha256=digest(proposal.encode()),
                    review_context_sha256=review_context(self.root)["sha256"])

    def record(self,receipt,proposal,events):
        record=review_record(receipt,proposal)
        record['sources'][0].update(sha256=digest(self.prompt.encode()),quote=self.prompt)
        for i,(req,row,event) in enumerate(zip(record['requirements'],record['rows'],events),1):
            req.update(authority=self.prompt,accepted_result='Implemented',output='New Linear issue',source_evidence='Supplied fixture golden: all three named events are implemented.')
            outcome=req['outcomes'][0]
            outcome.update(entity=event,property='implementation status',output='New Linear issue',accepted_result='Implemented')
            row.update(output='New Linear issue',source_evidence=req['source_evidence'])
            row['assertion_inventory']=assertion_inventory(json.loads(proposal)[i-1]['title'],[outcome])
            row['valid_case'].update(example=event+' is implemented.',reason='The requested event status is correct.')
            row['near_miss'].update(example=event+' is unbuilt.',reason='That reverses the stipulated implementation status.')
            row['atomicity']['reason']='One event status in this fixture.'
            row['atomicity']['independence_test'].update(example=event+' implemented versus unbuilt.',reason='This row owns one event status.')
            record['set_tests']['mutations'][i-1].update(example='Change only '+event+' to unbuilt.',reason='The row rejects the incorrect status.')
        record['set_tests']['valid_completion'].update(example='The new issue reports all three named events implemented.',reason='Each requested status is correct.')
        record['set_tests']['final_reply'].update(example='Created the issue: <link>.',authority='The prompt requests an issue, not a repeated status list.',reason='Artifact contains the required content; no independent recap requirement.')
        return record

    def test_original_bundle_is_flagged_and_split_record_clears_checks(self):
        bad=json.dumps([CASES['user1_same_outcome_id']['criterion']])
        receipt=self.receipt(bad)
        record=self.record(receipt,bad,['implemented events'])
        inventory=copy.deepcopy(CASES['user1_same_outcome_id']['assertion_inventory'])
        for assertion in inventory['assertions']:assertion['outcome_id']='Q1-O1'
        record['rows'][0]['assertion_inventory']=inventory
        result=validate_record(record,json.loads(bad),receipt,root=self.root)
        self.assertTrue(any('multiple required assertions' in p for p in result['review_open_items']))
        with self.assertRaisesRegex(ValueError,'block publication'):
            validate_record(record,json.loads(bad),receipt,root=self.root,publication=True)
        self.assertFalse((self.root/FINAL).exists())
        events=['begin_level','left_level','notification_permission']
        good_rows=copy.deepcopy([CASES['user1_split_'+event]['criterion'] for event in events])
        for criterion in good_rows:
            criterion['title']=criterion['title'].replace("The Agent's new Linear issue identifies", 'The Agent identifies in the new Linear issue')
        good=json.dumps(good_rows)
        receipt=self.receipt(good)
        result=validate_record(self.record(receipt,good,events),json.loads(good),receipt,root=self.root,publication=True)
        self.assertEqual(result['review_open_items'], [])
        self.assertFalse((self.root/FINAL).exists())
        self.assertEqual(len(json.loads(good)),3)

    def test_record_needs_inventory_and_rejects_v6_record(self):
        proposal=json.dumps([CASES['user1_split_begin_level']['criterion']])
        receipt=self.receipt(proposal)
        record=self.record(receipt,proposal,['begin_level'])
        for change in ('inventory','version'):
            bad=copy.deepcopy(record)
            if change=='inventory':del bad['rows'][0]['assertion_inventory']
            else:bad['format_version']=3
            with self.subTest(change=change),self.assertRaises(ValueError):
                validate_record(bad,json.loads(proposal),receipt,root=self.root)


if __name__=='__main__':unittest.main()

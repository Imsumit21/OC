import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

from hg_rubric_assertions import validate_assertions
from hg_coherent_record import verify_record_source
from hg_review_evidence import EvidenceReader
from hg_rubric_review import ATOMIC_EXCEPTIONS

class CoherentRecordTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        raw=json.dumps([dict(number=10,merged_at='2026-02-10')]).encode()
        (self.root/'source.json').write_bytes(raw)
        self.source=dict(id='S1',path='source.json',sha256=hashlib.sha256(raw).hexdigest(),
                         quote='2026-02-10',pointer='/0',visibility='VISIBLE')
        self.ex=dict(kind='coherent_record',record_kind='pull_request',source_id='S1',
                     entity='repo#10',fields=['number','merged_at'],reason='One selected PR record.')
        self.atomicity=dict(outcome_ids=['O1'],exception=self.ex)
        self.criterion=dict(title='The Agent reports PR #10 and merge date 2026-02-10.',
                            justification='Requested PR record.',evidence='Source JSON.')
        self.inv=dict(complete=True,reason='Both record attributes enumerated.',assertions=[
            dict(id='A1',field='title',quote='PR #10',reason='Selected PR identity.',role='REQUIRED_RESULT',
                 outcome_id='O1',kind='ENTITY_PROPERTY',entities=['repo#10'],property='number',source_id='S1'),
            dict(id='A2',field='title',quote='2026-02-10',reason='That PR merge date.',role='REQUIRED_RESULT',
                 outcome_id='O1',kind='ENTITY_PROPERTY',entities=['repo#10'],property='merged_at',source_id='S1')])

    def check(self):
        return validate_assertions(self.inv,self.criterion,self.atomicity)

    def test_pair_registered_and_clears(self):
        self.assertIn('coherent_record',ATOMIC_EXCEPTIONS)
        self.assertEqual(self.check(),[])

    def test_split_single_field_still_clears(self):
        for a in self.inv['assertions']:
            inv=dict(self.inv,assertions=[a])
            self.assertEqual(validate_assertions(inv,self.criterion,dict(outcome_ids=['O1'],exception=None)),[])

    def test_different_entities_rejected(self):
        self.inv['assertions'][1]['entities']=['repo#30'];self.assertTrue(self.check())

    def test_different_source_records_rejected(self):
        self.inv['assertions'][1]['source_id']='S2';self.assertTrue(self.check())

    def test_separate_outcomes_rejected(self):
        self.atomicity['outcome_ids']=['O1','O2']
        self.inv['assertions'][1]['outcome_id']='O2';self.assertTrue(self.check())

    def test_generic_same_source_is_not_an_exception(self):
        self.ex['kind']='same_source';self.assertTrue(self.check())

    def test_unrelated_property_rejected(self):
        self.ex['fields'][1]='release_approved'
        self.inv['assertions'][1]['property']='release_approved';self.assertTrue(self.check())

    def test_hidden_required_field_rejected(self):
        self.criterion['evidence']='Date 2026-02-10'
        self.inv['assertions'][1]['field']='evidence';self.assertTrue(self.check())

    def test_visible_record_source_resolves(self):
        verify_record_source(self.atomicity,EvidenceReader(self.root),{'S1':self.source})

    def test_array_container_is_not_one_record(self):
        self.source['pointer']=''
        with self.assertRaises(ValueError):verify_record_source(self.atomicity,EvidenceReader(self.root),{'S1':self.source})

    def test_missing_source_field_rejected(self):
        self.ex['fields'].append('not_present')
        with self.assertRaises(ValueError):verify_record_source(self.atomicity,EvidenceReader(self.root),{'S1':self.source})

    def test_stale_source_rejected(self):
        (self.root/'source.json').write_text('[{"number":30,"merged_at":"2026-02-10"}]')
        with self.assertRaises(ValueError):verify_record_source(self.atomicity,EvidenceReader(self.root),{'S1':self.source})

    def test_inaccessible_source_rejected(self):
        self.source['visibility']='INACCESSIBLE'
        with self.assertRaises(ValueError):verify_record_source(self.atomicity,EvidenceReader(self.root),{'S1':self.source})

if __name__=='__main__':unittest.main()

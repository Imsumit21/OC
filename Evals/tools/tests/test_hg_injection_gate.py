import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_store_input as store
import hg_injection_gate as gate


class InjectionGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.patch = patch.object(store, 'REPOSITORY', self.root)
        self.patch.start()

    def tearDown(self):
        self.patch.stop()
        self.temp.cleanup()

    def review(self, sql, verdict='PASS'):
        reports = self.root / store.INPUTS / 'reports'
        reports.mkdir(parents=True, exist_ok=True)
        manifest = {'stages': {'injection': {
            'review_version': 'injection-static-v2', 'reviewed_at': '2026-10-09T20:15Z',
            'inputs': {'injection': {'sha256': hashlib.sha256(sql).hexdigest()}}}}}
        (reports / 'input_manifest.json').write_text(json.dumps(manifest))
        (reports / '0_injection.md').write_text(f'## Report\n\n### FINAL VERDICT: {verdict}\n')

    def test_unanswered_question_is_not_gated(self):
        self.assertEqual(gate.gate()['state'], 'ASK')

    def test_no_injection_choice_skips_gate(self):
        store.clear_input('injection', confirmed_unused=True)
        self.assertEqual(gate.gate()['state'], 'NOT_USED')

    def test_sql_without_review_is_never_reviewed(self):
        store.save_input('injection', content=b'INSERT INTO t VALUES (1);')
        self.assertEqual(gate.gate()['state'], 'NEVER_REVIEWED')

    def test_reviewed_sql_is_current_and_reports_verdict(self):
        sql = b'INSERT INTO t VALUES (1);'
        store.save_input('injection', content=sql)
        self.review(sql, verdict='NON-FAIL')
        result = gate.gate()
        self.assertEqual(result['state'], 'CURRENT')
        self.assertEqual(result['injection_verdict'], 'NON-FAIL')

    def test_changed_sql_is_stale(self):
        self.review(b'INSERT INTO t VALUES (1);')
        store.save_input('injection', content=b'INSERT INTO t VALUES (2);')
        result = gate.gate()
        self.assertEqual(result['state'], 'STALE')
        self.assertNotEqual(result['current_sha256'], result['reviewed']['sha256'])

    def test_manifest_without_injection_stage_is_never_reviewed(self):
        store.save_input('injection', content=b'SELECT 1;')
        reports = self.root / store.INPUTS / 'reports'
        reports.mkdir(parents=True)
        (reports / 'input_manifest.json').write_text(json.dumps({'stages': {'prompt': {}}}))
        self.assertEqual(gate.gate()['state'], 'NEVER_REVIEWED')


if __name__ == '__main__':
    unittest.main()

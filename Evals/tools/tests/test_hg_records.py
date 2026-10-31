import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_records as records
from universe_fixture import routing, select


class RecordChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        (self.root / 'Evals/references').mkdir(parents=True)
        self.folder = self.root / 'Base/linear'
        self.folder.mkdir(parents=True)
        select(self.root).write_text(json.dumps(
            {'services': {'linear': {'path': 'Base/linear'}}}))
        (self.folder / 'source_manifest.json').write_text(json.dumps(
            {'files': [{'path': 'data.json'}]}))
        self.path = self.folder / 'data.json'
        self.path.write_text(json.dumps({'users': [{'id': 'U', 'name': 'Zoë'}],
                                        'issues': [{'id': 'A', 'number': 1, 'nested': {'id': 'B'}},
                                                   {'id': 'B', 'number': '1'}, {'id': 'A', 'number': True}],
                                        'comments': []}))
        self.old_root = records.h.ROOT
        records.h.ROOT = self.root

    def tearDown(self):
        records.h.ROOT = self.old_root
        self.temp.cleanup()

    def check(self, name, pointer, field='id', values=None):
        return {'id': name, 'service': 'linear', 'file': 'data.json',
                'pointer': pointer, 'field': field, 'values': values or ['A', 'B', 'missing']}

    def request(self):
        return {'checks': [self.check('users', '/users', values=['U']),
                           self.check('issues', '/issues'),
                           self.check('numbers', '/issues', 'number', [1]),
                           self.check('comments', '/comments')]}

    def test_one_read_complete_records_duplicates_and_exact_type(self):
        opens = []
        original = Path.open
        def counted(path, *args, **kwargs):
            if path == self.path:
                opens.append(path)
            return original(path, *args, **kwargs)
        with patch.object(Path, 'open', counted):
            result = records.run(self.request())
        self.assertEqual(len(opens), 1)
        self.assertEqual(result['files_read_this_call'], 1)
        self.assertTrue(result['scan_complete'])
        self.assertEqual(len(result['checks']['issues']['matches']), 3)
        match = result['checks']['numbers']['matches']
        self.assertEqual(len(match), 1)
        self.assertEqual(match[0]['pointer'], '/issues/0')
        self.assertEqual(match[0]['record']['nested'], {'id': 'B'})
        self.assertEqual(result['checks']['comments']['records_checked'], 0)

    def test_streaming_matches_loaded_results(self):
        self.assertEqual(records.run(self.request()), records.run(self.request(), threshold=0))

    def test_sharded_collection_keeps_all_collisions_and_missing_shard(self):
        (self.folder / 'a.json').write_text('[{"id":"A"}]')
        (self.folder / 'b.json').write_text('[{"id":"A"}]')
        (self.folder / 'source_manifest.json').write_text(json.dumps(
            {'files': [{'path': 'a.json'}, {'path': 'b.json'}]}))
        check = self.check('shards', '')
        check['file'] = '*.json'
        result = records.run({'checks': [check]})
        self.assertTrue(result['scan_complete'])
        self.assertEqual(len(result['checks']['shards']['matches']), 2)
        (self.folder / 'b.json').unlink()
        result = records.run({'checks': [check]})
        self.assertFalse(result['scan_complete'])
        self.assertEqual(len(result['checks']['shards']['matches']), 1)

    def test_missing_array_and_nonobject_record_remain_incomplete(self):
        for data in ({'users': []}, {'users': [], 'issues': [42], 'comments': []}):
            self.path.write_text(json.dumps(data))
            for threshold in (0, 10000):
                result = records.run(self.request(), threshold=threshold)
                self.assertFalse(result['scan_complete'])
                self.assertFalse(result['checks']['issues']['scan_complete'])

    def test_duplicate_keys_and_malformed_tail_never_certify_absence(self):
        for raw in ('{"users":[],"issues":[],"issues":[],"comments":[]}',
                    '{"users":[],"issues":[{"id":"A","id":"B"}],"comments":[]}',
                    '{"users":[],"issues":[],"comments":[]} garbage'):
            self.path.write_text(raw)
            for threshold in (0, 10000):
                self.assertFalse(records.run(self.request(), threshold=threshold)['scan_complete'])

    def test_missing_source_and_escaping_symlink(self):
        self.path.unlink()
        self.assertFalse(records.run(self.request())['scan_complete'])
        target = self.root / 'outside.json'
        target.write_text('{"users":[],"issues":[],"comments":[]}')
        self.path.symlink_to(target)
        self.assertFalse(records.run(self.request())['scan_complete'])

    def test_source_changes_and_next_call_reads_replacement(self):
        original = records.batch.fingerprint
        calls = []
        def changed(*args):
            calls.append(1)
            return original(*args) + str(len(calls))
        with patch.object(records.batch, 'fingerprint', changed):
            self.assertFalse(records.run(self.request())['scan_complete'])
        self.path.write_text('{"users":[],"issues":[],"comments":[]}')
        result = records.run(self.request())
        self.assertTrue(result['scan_complete'])
        self.assertEqual(result['checks']['issues']['matches'], [])

    def test_root_array_escaped_pointer_and_unknown_request_fields(self):
        self.path.write_text('[{"id":"A"}]')
        result = records.run({'checks': [self.check('root', '')]}, threshold=0)
        self.assertTrue(result['scan_complete'])
        self.assertEqual(result['checks']['root']['matches'][0]['pointer'], '/0')
        self.path.write_text('{"a/b~c":[{"id":"A"}]}')
        result = records.run({'checks': [self.check('escaped', '/a~1b~0c')]})
        self.assertTrue(result['scan_complete'])
        bad = self.request()
        bad['checks'][0]['limit'] = 1
        with self.assertRaises(ValueError):
            records.run(bad)


if __name__ == '__main__':
    unittest.main()

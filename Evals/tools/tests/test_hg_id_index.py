import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_search as h
import hg_id_index as idx
import hg_compact_index as compact
from universe_fixture import routing, select


class IdentityIndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.folder = self.root / 'Base'
        self.folder.mkdir()
        (self.root / 'Evals/references').mkdir(parents=True)
        self.universe = select(self.root)
        self.universe.write_text(json.dumps({'services': {'linear': {'path': 'Base'}}}))
        self.source = self.folder / 'data.json'
        self.source.write_text(json.dumps({'rows': [{'id': 'A', 'nested': {'id': 'B'}},
            {'id': 'AB'}, {'id': 'A'}, {'id': 1}, {'id': True}, {'id': '1'}, {'id': 'a'}], 'empty': []}))
        self.manifest = self.folder / 'source_manifest.json'
        self.refresh_manifest()
        self.patch = patch.object(h, 'ROOT', self.root)
        self.patch.start()

    def tearDown(self):
        self.patch.stop()
        self.temp.cleanup()

    def refresh_manifest(self):
        self.manifest.write_text(json.dumps({'files': [{'path': 'data.json',
            'sha256': hashlib.sha256(self.source.read_bytes()).hexdigest()}]}))

    def lookup(self, **kwargs):
        options = dict(service='linear', ids=['A', 'A', 'B', '1', 'missing'], file='data.json', pointer='/rows', key='id')
        options.update(kwargs)
        return h.batch_lookup(**options)

    def evidence(self, result):
        return {k: v for k, v in result.items() if k not in
                ('backend', 'files_read_this_call', 'source_bytes_hashed_this_call')}

    def test_exact_duplicate_type_and_coverage_parity_cold_and_warm(self):
        idx.package(h, 'linear', 'data.json')
        scan = self.lookup(no_cache=True)
        cold = self.lookup()
        warm = self.lookup()
        self.assertEqual(cold['backend'], 'verified-id-index')
        self.assertEqual(cold['source_bytes_hashed_this_call'], self.source.stat().st_size)
        self.assertEqual(warm['source_bytes_hashed_this_call'], 0)
        self.assertEqual(self.evidence(scan), self.evidence(cold))
        self.assertEqual(self.evidence(scan), self.evidence(warm))
        self.assertEqual(len(cold['matches']['A']), 2)
        self.assertEqual(cold['matches']['B'], [])

    def test_empty_array_absence_supported_but_missing_or_wrong_shape_falls_back(self):
        idx.package(h, 'linear', 'data.json')
        empty = self.lookup(pointer='/empty')
        self.assertEqual(empty['backend'], 'verified-id-index')
        self.assertTrue(empty['scan_complete'])
        self.assertEqual(empty['records_checked'], 0)
        self.assertFalse(self.lookup(pointer='/missing')['scan_complete'])
        self.assertFalse(self.lookup(pointer='/rows/0')['scan_complete'])

    def test_original_and_new_values_work_without_rebuilding_index(self):
        idx.package(h, 'linear', 'data.json')
        self.lookup()
        result = self.lookup(ids=['a', 'AB'])
        self.assertEqual(result['backend'], 'verified-id-index')
        self.assertEqual(result['source_bytes_hashed_this_call'], 0)
        self.assertEqual(len(result['matches']['a']), 1)

    def test_no_cache_and_unsupported_fields_use_fresh_scanner(self):
        idx.package(h, 'linear', 'data.json')
        self.assertEqual(self.lookup(no_cache=True)['backend'], 'batch-exact-id-scan')
        self.assertEqual(self.lookup(key='nested')['backend'], 'batch-exact-id-scan')

    def test_duplicate_keys_anywhere_and_malformed_tail_rejected_at_build(self):
        for raw in ('{"rows":[],"x":{"id":1,"id":2}}', '{"rows":[],"rows":[]}', '{"rows":[]}x'):
            self.source.write_text(raw)
            self.refresh_manifest()
            with self.assertRaises(ValueError):
                idx.package(h, 'linear', 'data.json')

    def test_changed_source_restored_mtime_invalidates_and_never_claims_absence(self):
        idx.package(h, 'linear', 'data.json')
        self.lookup()
        before = self.source.stat()
        self.source.write_text(self.source.read_text().replace('"A"', '"C"'))
        os.utime(self.source, ns=(before.st_atime_ns, before.st_mtime_ns))
        result = self.lookup()
        self.assertEqual(result['backend'], 'batch-exact-id-scan')
        self.assertEqual(result['matches']['A'], [])
        self.assertTrue(result['scan_complete'])

    def test_corrupt_artifact_and_manifest_fall_back(self):
        entry = idx.package(h, 'linear', 'data.json')
        path = self.universe.parent / 'id_indexes' / entry['path']
        path.write_text('{}')
        self.assertEqual(self.lookup()['backend'], 'batch-exact-id-scan')
        self.assertEqual(len(self.lookup()['matches']['A']), 2)

    def test_unindexed_new_shard_cannot_be_omitted_from_scope(self):
        idx.package(h, 'linear', 'data.json')
        self.lookup()
        extra = self.folder / 'extra.json'
        extra.write_text('{"rows":[{"id":"B"}]}')
        data = json.loads(self.manifest.read_text()); data['files'].append({'path': 'extra.json'})
        self.manifest.write_text(json.dumps(data))
        result = self.lookup(file='*.json')
        self.assertEqual(result['backend'], 'batch-exact-id-scan')
        self.assertEqual(result['files_completed'], 2)
        self.assertEqual(len(result['matches']['B']), 1)

    def test_source_change_during_index_read_is_detected(self):
        idx.package(h, 'linear', 'data.json')
        self.lookup()
        original = idx.load
        def changed(*args):
            result = original(*args)
            self.source.write_text(self.source.read_text().replace('"A"', '"C"'))
            return result
        with patch.object(idx, 'load', changed):
            with self.assertRaisesRegex(ValueError, 'changed during operation'):
                self.lookup()

    def test_missing_index_never_builds_during_lookup(self):
        result = self.lookup()
        self.assertEqual(result['backend'], 'batch-exact-id-scan')
        self.assertFalse((self.universe.parent / 'id_indexes').exists())

    def test_cache_directory_symlink_falls_back_without_writing_target(self):
        idx.package(h, 'linear', 'data.json')
        outside = self.root / 'outside'; outside.mkdir()
        (self.root / 'Evals/.cache/compact').rename(self.root / 'old-cache')
        (self.root / 'Evals/.cache/compact').symlink_to(outside, target_is_directory=True)
        result = self.lookup()
        self.assertEqual(result['backend'], 'batch-exact-id-scan')
        self.assertTrue(result['scan_complete'])
        self.assertEqual(list(outside.iterdir()), [])

    def test_pointers_are_escaped_and_arbitrary_service_names_supported(self):
        self.source.write_text('{"a/b~c":[{"id":"A"}]}')
        self.refresh_manifest()
        idx.package(h, 'linear', 'data.json')
        result = self.lookup(pointer='/a~1b~0c')
        self.assertEqual(result['matches']['A'][0]['pointer'], '/a~1b~0c/0/id')


if __name__ == '__main__':
    unittest.main()

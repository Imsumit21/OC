import importlib.util
import json
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import hg_search_batch

class ProductionLookup:
    @staticmethod
    def lookup(root, ids, service='slack', pattern='messages/*.json', key='id', no_cache=False,
               max_load_bytes=8*1024*1024, pointer=''):
        spec=importlib.util.spec_from_file_location('lookup_test_search', TOOLS/'hg_search.py')
        h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h);h.ROOT=Path(root).resolve()
        return hg_search_batch.lookup(h.batch_api(),service,list(ids),pattern,pointer,key,
                                      no_cache=no_cache,threshold=max_load_bytes)
p=ProductionLookup()


class ExactIDTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='hg-id-fixture-')
        self.root = Path(self.temp.name).resolve()
        (self.root / 'Evals/tools').mkdir(parents=True)
        (self.root / 'Evals/references').mkdir()
        for name in ['hg_search.py', 'hg_search_index.py', 'hg_search_batch.py', 'hg_compact_index.py']:
            shutil.copy2(TOOLS / name, self.root / 'Evals/tools' / name)
        self.folder = self.root / 'Base/slack'
        self.folder.mkdir(parents=True)
        (self.root / 'Evals/references/universe_manifest.json').write_text(
            json.dumps({'services': {'slack': {'path': 'Base/slack'}}}))
        self.files = []

    def tearDown(self):
        self.temp.cleanup()

    def source(self, name, data, raw=False):
        path = self.folder / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data if raw else json.dumps(data, ensure_ascii=False))
        if name not in [r['path'] for r in self.files]:
            self.files.append({'path': name})
        (self.folder / 'source_manifest.json').write_text(json.dumps({'files': self.files}))
        return path

    def run_lookup(self, ids=('A', 'B', 'missing'), **kwargs):
        return p.lookup(self.root, ids, **kwargs)

    def test_exact_identity_not_text_partial_or_nested_reference(self):
        self.source('messages/a.json', [
            {'id': 'A', 'text': 'B missing', 'nested': {'id': 'B'}},
            {'id': 'AB'}, {'id': 'a'}, {'id': 'B'}, {'id': 1}])
        result = self.run_lookup()
        self.assertTrue(result['scan_complete'])
        self.assertEqual(result['records_checked'], 5)
        self.assertEqual([x['pointer'] for x in result['matches']['A']], ['/0/id'])
        self.assertEqual([x['pointer'] for x in result['matches']['B']], ['/3/id'])
        self.assertEqual(result['matches']['missing'], [])

    def test_duplicate_IDs_across_files_keep_both_citations(self):
        self.source('messages/a.json', [{'id': 'A'}])
        self.source('messages/b.json', [{'id': 'A'}])
        result = self.run_lookup()
        self.assertEqual(len(result['matches']['A']), 2)
        self.assertEqual(result['files_completed'], 2)

    def test_cold_warm_and_forced_streaming_match(self):
        self.source('messages/a.json', [{'id': 'A', 'text': '😀'}, {'id': 'B'}])
        cold = self.run_lookup()
        warm = self.run_lookup()
        stream = self.run_lookup(no_cache=True, max_load_bytes=1)
        self.assertEqual(warm['backend'], 'query-cache')
        for key in ['matches', 'scan_complete', 'files_completed', 'records_checked', 'errors']:
            self.assertEqual(cold[key], warm[key])
            self.assertEqual(cold[key], stream[key])

    def test_changed_source_invalidates_even_when_mtime_restored(self):
        path = self.source('messages/a.json', [{'id': 'A'}])
        self.run_lookup()
        old = path.stat()
        self.source('messages/a.json', [{'id': 'B'}])
        os.utime(path, ns=(old.st_atime_ns, old.st_mtime_ns))
        result = self.run_lookup()
        self.assertEqual(result['backend'], 'batch-exact-id-scan')
        self.assertEqual(result['matches']['A'], [])
        self.assertEqual(len(result['matches']['B']), 1)

    def test_missing_file_invalidates_and_does_not_certify_absence(self):
        path = self.source('messages/a.json', [{'id': 'A'}])
        self.run_lookup()
        path.unlink()
        result = self.run_lookup()
        self.assertFalse(result['scan_complete'])
        self.assertTrue(result['errors'])

    def test_malformed_input_reports_partial(self):
        self.source('messages/a.json', [{'id': 'A'}])
        self.source('messages/b.json', '[{"id":"B"},', raw=True)
        result = self.run_lookup()
        self.assertFalse(result['scan_complete'])
        self.assertEqual(result['files_completed'], 1)
        self.assertEqual(len(result['matches']['A']), 1)

    def test_duplicate_JSON_keys_rejected_in_both_readers(self):
        self.source('messages/a.json', '[{"id":"A","id":"B"}]', raw=True)
        for threshold in (1, 8000000):
            result = self.run_lookup(no_cache=True, max_load_bytes=threshold)
            self.assertFalse(result['scan_complete'])
            self.assertIn('Duplicate JSON', result['errors'][0]['error'])

    def test_corrupt_query_cache_rebuilds(self):
        self.source('messages/a.json', [{'id': 'A'}])
        self.run_lookup()
        for path in (self.root / 'Evals/.cache/queries').glob('*.json'):
            path.write_text('broken')
        result = self.run_lookup()
        self.assertTrue(result['scan_complete'])
        self.assertEqual(result['backend'], 'batch-exact-id-scan')

    def test_unwritable_cache_location_still_completes_scan(self):
        self.source('messages/a.json', [{'id': 'A'}])
        (self.root / 'Evals/.cache').write_text('not a directory')
        result = self.run_lookup()
        self.assertTrue(result['scan_complete'])
        self.assertIn('cache_warning', result)

    def test_wrong_shape_and_empty_scope_not_complete(self):
        self.source('messages/a.json', {'id': 'A'})
        self.assertFalse(self.run_lookup()['scan_complete'])
        self.assertFalse(self.run_lookup(pattern='nothing/*.json')['scan_complete'])

    def test_nested_record_array_and_custom_key(self):
        self.source('messages/a.json', {'pack': {'children': [{'ticket': 'A'}, {'ticket': 'B'}]}})
        for threshold in (1, 8000000):
            result = self.run_lookup(pointer='/pack/children', key='ticket',
                                     max_load_bytes=threshold, no_cache=True)
            self.assertTrue(result['scan_complete'])
            self.assertEqual(result['records_checked'], 2)
            self.assertEqual(result['matches']['A'][0]['pointer'], '/pack/children/0/ticket')

    def test_cache_symlink_cannot_write_outside_workspace(self):
        self.source('messages/a.json', [{'id': 'A'}])
        with tempfile.TemporaryDirectory() as outside:
            (self.root/'Evals/.cache').mkdir()
            (self.root/'Evals/.cache/queries').symlink_to(outside, target_is_directory=True)
            result = self.run_lookup()
            self.assertTrue(result['scan_complete'])
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_manifest_change_invalidates_cached_absence(self):
        self.source('messages/a.json', [{'id': 'A'}])
        self.run_lookup()
        self.source('messages/b.json', [{'id': 'B'}])
        result = self.run_lookup()
        self.assertEqual(len(result['matches']['B']), 1)
        self.assertEqual(result['files_completed'], 2)

    def test_parallel_cache_writers_produce_valid_atomic_result(self):
        self.source('messages/a.json', [{'id': 'A'}] * 1000)
        ids = self.root / 'ids.json'
        ids.write_text('["A", "missing"]')
        command = [sys.executable, str(self.root/'Evals/tools/hg_search.py'), 'lookup', 'slack',
                   '--ids-file', str(ids), '--file', 'messages/*.json']
        workers = [subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                   for _ in range(3)]
        for worker in workers:
            out, err = worker.communicate(timeout=20)
            self.assertEqual(worker.returncode, 0, err)
            self.assertTrue(json.loads(out)['scan_complete'])
        result = self.run_lookup(ids=('A', 'missing'))
        self.assertEqual(result['backend'], 'query-cache')
        self.assertEqual(len(result['matches']['A']), 1000)


if __name__ == '__main__':
    unittest.main(verbosity=2)

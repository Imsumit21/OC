import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_records as records
from universe_fixture import routing, select


class CompleteRecordCacheTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.folder = self.root / 'Base/linear'
        self.folder.mkdir(parents=True)
        (self.root / 'Evals/references').mkdir(parents=True)
        self.universe = select(self.root)
        self.universe.write_text(json.dumps({'services': {'linear': {'path': 'Base/linear'}}}))
        self.manifest = self.folder / 'source_manifest.json'
        self.manifest.write_text(json.dumps({'files': [{'path': 'data.json', 'sha256': 'declared-A'}]}))
        self.source = self.folder / 'data.json'
        self.source.write_text('{"items":[{"id":"A","n":1},{"id":"A","n":true},{"id":"B","n":"1"}]}')
        self.request = {'checks': [{'id': 'records', 'service': 'linear', 'file': 'data.json',
                                   'pointer': '/items', 'field': 'id', 'values': ['A', 'missing']}]}
        self.old_root = records.h.ROOT
        records.h.ROOT = self.root

    def tearDown(self):
        records.h.ROOT = self.old_root
        self.temp.cleanup()

    def cached(self):
        return list((self.root / 'Evals/.cache/records').glob('*.json'))

    def assert_scan(self, result):
        self.assertEqual(result['backend'], 'grouped-record-scan')
        self.assertEqual(result['files_read_this_call'], 1)

    def assert_hit(self, result):
        self.assertEqual(result['backend'], 'record-query-cache')
        self.assertEqual(result['files_read_this_call'], 0)

    def test_fresh_reuse_preserves_complete_evidence_across_all_stages(self):
        first = records.run(self.request)
        self.assert_scan(first)
        self.assertEqual(len(first['checks']['records']['matches']), 2)
        for stage in ('injection', 'prompt', 'hardness', 'golden', 'oe', 'rubric'):
            with self.subTest(stage=stage):
                hit = records.run(self.request)
                self.assert_hit(hit)
                self.assertEqual(hit['checks'], first['checks'])
                self.assertEqual(hit['sources'], first['sources'])
                self.assertNotIn('verdict', hit)

    def test_same_size_replacement_restored_mtime_invalidates(self):
        records.run(self.request)
        before = self.source.stat()
        self.source.write_text(self.source.read_text().replace('"A"', '"C"'))
        os.utime(self.source, ns=(before.st_atime_ns, before.st_mtime_ns))
        self.assertEqual(before.st_size, self.source.stat().st_size)
        self.assertEqual(before.st_mtime_ns, self.source.stat().st_mtime_ns)
        self.assertNotEqual(before.st_ctime_ns, self.source.stat().st_ctime_ns)
        result = records.run(self.request)
        self.assert_scan(result)
        self.assertEqual(result['checks']['records']['matches'], [])

    def test_every_request_scope_field_invalidates_and_exact_types_preserved(self):
        records.run(self.request)
        for field, value in [('values', ['B']), ('file', '*.json'),
                             ('field', 'n'), ('pointer', '/missing')]:
            request = json.loads(json.dumps(self.request))
            request['checks'][0][field] = value
            self.assertEqual(records.run(request)['backend'], 'grouped-record-scan')
        self.request['checks'][0].update(field='n', values=[1])
        first = records.run(self.request)
        self.assertEqual(len(first['checks']['records']['matches']), 1)
        self.assertEqual(first['checks']['records']['matches'][0]['pointer'], '/items/0')
        self.assert_hit(records.run(self.request))
        self.request['checks'][0]['values'] = ['1']
        string_match = records.run(self.request)
        self.assert_scan(string_match)
        self.assertEqual(string_match['checks']['records']['matches'][0]['pointer'], '/items/2')

    def test_manifest_hash_and_universe_mapping_metadata_invalidate(self):
        records.run(self.request)
        self.manifest.write_text(self.manifest.read_text().replace('declared-A', 'declared-B'))
        result = records.run(self.request)
        self.assert_scan(result)
        self.assertEqual(result['sources'][0]['manifest_sha256'], 'declared-B')
        self.universe.write_text(self.universe.read_text() + '\n')
        self.assert_scan(records.run(self.request))

    def test_new_shard_invalidates_complete_scope(self):
        self.request['checks'][0]['file'] = '*.json'
        first = records.run(self.request)
        (self.folder / 'second.json').write_text('{"items":[{"id":"A"}]}')
        self.manifest.write_text(json.dumps({'files': [{'path': 'data.json'}, {'path': 'second.json'}]}))
        result = records.run(self.request)
        self.assertEqual(result['files_read_this_call'], 2)
        self.assertEqual(len(result['checks']['records']['matches']), 3)
        self.assertEqual(first['checks']['records']['files_completed'], 1)

    def test_helper_semantics_invalidate(self):
        records.run(self.request)
        original = records.helper_identity()
        with patch.object(records, 'helper_identity', return_value=original + [['test', 'changed']]):
            self.assert_scan(records.run(self.request))

    def test_malformed_duplicate_keys_and_missing_pointer_are_never_cached(self):
        for value in ('{"items":[{"id":"A","id":"B"}]}',
                      '{"items":[],"items":[]}', '{"items":[]} garbage',
                      '{"else":[]}', '{"items":[1]}'):
            for threshold in (0, 10000):
                self.source.write_text(value)
                result = records.run(self.request, threshold=threshold)
                self.assertFalse(result['scan_complete'])
                self.assertEqual(self.cached(), [])

    def test_corruption_bad_checksum_and_fake_complete_result_fall_back(self):
        records.run(self.request)
        path = self.cached()[0]
        for mode in ('json', 'checksum', 'incomplete', 'scope'):
            payload = json.loads(path.read_text())
            if mode == 'json':
                path.write_text('{broken')
            elif mode == 'checksum':
                payload['result']['checks']['records']['matches'] = []
                path.write_text(json.dumps(payload))
            else:
                if mode == 'incomplete':
                    payload['result']['scan_complete'] = False
                else:
                    payload['result']['checks']['records']['scope']['field'] = 'different'
                payload['checksum'] = records.batch.digest(payload['result'])
                path.write_text(json.dumps(payload))
            result = records.run(self.request)
            self.assert_scan(result)
            self.assertEqual(len(result['checks']['records']['matches']), 2)

    def test_source_changes_during_cache_read_cannot_return_stale_match(self):
        records.run(self.request)
        original = records.read_record_cache
        def changed(*args):
            saved = original(*args)
            self.source.write_text(self.source.read_text().replace('"A"', '"C"'))
            return saved
        with patch.object(records, 'read_record_cache', changed):
            result = records.run(self.request)
        self.assert_scan(result)
        self.assertEqual(result['checks']['records']['matches'], [])

    def test_no_cache_bypasses_read_and_write(self):
        self.assert_scan(records.run(self.request, no_cache=True))
        self.assertEqual(self.cached(), [])
        records.run(self.request)
        self.assert_scan(records.run(self.request, no_cache=True))

    def test_bounded_cache_evicts_results_without_changing_evidence(self):
        with patch.object(records, 'CACHE_MAX_BYTES', 1):
            result = records.run(self.request)
        self.assertTrue(result['scan_complete'])
        self.assertEqual(len(result['checks']['records']['matches']), 2)
        self.assertEqual(self.cached(), [])

    def test_cache_io_failure_preserves_complete_scan(self):
        with patch.object(records, 'cache_path', side_effect=OSError('read-only')):
            result = records.run(self.request)
        self.assert_scan(result)
        self.assertTrue(result['scan_complete'])

    def test_cache_directory_symlink_cannot_write_or_prune_other_files(self):
        target = self.root / 'unrelated'
        target.mkdir()
        retained = target / 'keep.json'
        retained.write_text('{"unrelated":true}')
        cache = self.root / 'Evals/.cache/records'
        cache.parent.mkdir()
        cache.symlink_to(target, target_is_directory=True)
        with patch.object(records, 'CACHE_MAX_BYTES', 1):
            result = records.run(self.request)
        self.assert_scan(result)
        self.assertTrue(result['scan_complete'])
        self.assertEqual(list(target.iterdir()), [retained])

    def test_same_raw_cache_contract_for_every_supported_service(self):
        services = ('contacts', 'gcal', 'gdocs', 'gdrive', 'github', 'gmail',
                    'gsheets', 'gslides', 'linear', 'slack', 'trello',
                    'confluence', 'snowflake')
        self.universe.write_text(json.dumps({'services': {
            service: {'path': 'Base/linear'} for service in services}}))
        for service in services:
            with self.subTest(service=service):
                request = json.loads(json.dumps(self.request))
                request['checks'][0]['service'] = service
                first = records.run(request)
                self.assert_scan(first)
                self.assertTrue(first['scan_complete'])
                self.assertEqual(len(first['checks']['records']['matches']), 2)
                hit = records.run(request)
                self.assert_hit(hit)
                self.assertEqual(first['checks'], hit['checks'])
                self.assertEqual(first['sources'], hit['sources'])

    def test_structured_routing_used_and_legacy_api_remains_supported(self):
        original = records.h.service_info
        with patch.object(records.h, 'structured_service_info',
                          side_effect=original, create=True) as structured:
            self.assert_scan(records.run(self.request, no_cache=True))
            structured.assert_called_once_with('linear')
        with patch.object(records.h, 'structured_service_info', None, create=True):
            self.assert_scan(records.run(self.request, no_cache=True))

    def test_compact_routing_helper_content_is_in_code_identity(self):
        helper = self.root / 'helpers'
        helper.mkdir()
        module_paths = [helper / name for name in ('hg_records.py', 'hg_search.py',
                                                 'hg_search_batch.py')]
        for path in module_paths:
            path.write_text('# helper\n')
        with patch.object(records, '__file__', str(module_paths[0])), \
             patch.object(records.h, '__file__', str(module_paths[1])), \
             patch.object(records.batch, '__file__', str(module_paths[2])):
            first = records.helper_identity()
            compact = helper / 'hg_compact_index.py'
            compact.write_text('# compact v1\n')
            second = records.helper_identity()
            self.assertNotEqual(first, second)
            self.assertEqual(second[-1][0], 'hg_compact_index.py')
            compact.write_text('# compact v2\n')
            self.assertNotEqual(second, records.helper_identity())

    def test_universe_manifest_change_while_parsed_is_not_cached_or_complete(self):
        records.run(self.request)
        before = self.cached()[0].read_bytes()
        original = records.h.manifest
        def changing():
            result = original()
            self.universe.write_text(self.universe.read_text() + '\n')
            return result
        with patch.object(records.h, 'manifest', changing), \
             patch.object(records.h, 'structured_service_info', None, create=True):
            try:
                result = records.run(self.request)
            except ValueError as error:
                self.assertIn('changed during operation', str(error))
            else:
                self.assert_scan(result)
                self.assertFalse(result['scan_complete'])
                self.assertIn('Source manifest changed',
                              result['checks']['records']['errors'][-1]['error'])
        self.assertEqual(self.cached()[0].read_bytes(), before)

    def test_source_manifest_change_while_parsed_is_not_cached_or_complete(self):
        records.run(self.request)
        original = records.h.service_info
        def changing(service):
            result = original(service)
            self.manifest.write_text(self.manifest.read_text() + '\n')
            return result
        with patch.object(records.h, 'structured_service_info', changing, create=True):
            result = records.run(self.request)
        self.assert_scan(result)
        self.assertFalse(result['scan_complete'])

    def test_manifest_change_during_cache_read_cannot_reuse_complete_scope(self):
        records.run(self.request)
        original = records.read_record_cache
        def changed(*args):
            saved = original(*args)
            self.manifest.write_text(self.manifest.read_text() + '\n')
            return saved
        with patch.object(records, 'read_record_cache', changed):
            result = records.run(self.request)
        self.assert_scan(result)
        self.assertFalse(result['scan_complete'])

    def test_remapped_service_reads_new_source_and_invalidates_old_scope(self):
        records.run(self.request)
        other = self.root / 'Base/replacement'
        other.mkdir()
        (other / 'source_manifest.json').write_text(self.manifest.read_text())
        (other / 'data.json').write_text('{"items":[{"id":"A","new":true}]}')
        self.universe.write_text(json.dumps({'services': {
            'linear': {'path': 'Base/replacement'}}}))
        result = records.run(self.request)
        self.assert_scan(result)
        self.assertEqual(result['checks']['records']['matches'][0]['record'],
                         {'id': 'A', 'new': True})
        self.assert_hit(records.run(self.request))

    def test_complete_empty_scope_is_cached_but_missing_file_is_not(self):
        self.source.write_text('{"items":[]}')
        result = records.run(self.request)
        self.assert_scan(result)
        self.assertTrue(result['scan_complete'])
        self.assertEqual(result['checks']['records']['records_checked'], 0)
        self.assert_hit(records.run(self.request))
        self.request['checks'][0]['file'] = 'missing.json'
        before = self.cached()
        result = records.run(self.request)
        self.assertFalse(result['scan_complete'])
        self.assertEqual(result['files_read_this_call'], 0)
        self.assertEqual(self.cached(), before)

    def test_entry_limit_skips_cache_without_truncating_result(self):
        with patch.object(records, 'CACHE_MAX_ENTRY_BYTES', 100):
            result = records.run(self.request)
        self.assertTrue(result['scan_complete'])
        self.assertEqual(len(result['checks']['records']['matches']), 2)
        self.assertEqual(self.cached(), [])

    def test_cache_entry_and_ancestor_symlinks_do_not_read_or_write_targets(self):
        external = self.root / 'unrelated'
        external.mkdir()
        keep = external / 'keep.json'
        keep.write_text('{"unrelated":true}')
        records.run(self.request)
        cached = self.cached()[0]
        cached.unlink()
        cached.symlink_to(keep)
        self.assert_scan(records.run(self.request))
        self.assertEqual(keep.read_text(), '{"unrelated":true}')
        cached.unlink()
        for path in cached.parent.glob('*.check'):
            path.unlink()
        cached.parent.rmdir()
        cached.parent.parent.rename(self.root / 'saved-cache')
        cached.parent.parent.symlink_to(external, target_is_directory=True)
        self.assert_scan(records.run(self.request))
        self.assertEqual(list(external.iterdir()), [keep])

    def test_cache_directory_swap_before_write_cannot_redirect_write(self):
        external = self.root / 'unrelated'
        external.mkdir()
        keep = external / 'keep.json'
        keep.write_text('{"unrelated":true}')
        original = records.write_record_cache
        def swapped(path, signature, result):
            path.parent.parent.mkdir(parents=True, exist_ok=True)
            path.parent.symlink_to(external, target_is_directory=True)
            original(path, signature, result)
        with patch.object(records, 'write_record_cache', swapped):
            result = records.run(self.request)
        self.assert_scan(result)
        self.assertTrue(result['scan_complete'])
        self.assertEqual(list(external.iterdir()), [keep])

    def test_cache_special_file_is_nonblocking_and_replaced_safely(self):
        path = records.cache_path(self.request, 32 * 1024 * 1024)
        path.parent.mkdir(parents=True)
        os.mkfifo(path)
        result = records.run(self.request)
        self.assert_scan(result)
        self.assertTrue(result['scan_complete'])
        self.assertTrue(path.is_file())
        self.assert_hit(records.run(self.request))

    def test_unsupported_safe_cache_apis_preserve_uncached_scan(self):
        for error in (AttributeError('O_NOFOLLOW'), NotImplementedError('dir_fd')):
            with self.subTest(error=type(error).__name__), \
                 patch.object(records, 'cache_directory', side_effect=error):
                result = records.run(self.request)
            self.assert_scan(result)
            self.assertTrue(result['scan_complete'])
            self.assertEqual(len(result['checks']['records']['matches']), 2)
            self.assertEqual(self.cached(), [])

    def test_renamed_reordered_values_reuse_exact_evidence(self):
        first = records.run(self.request)
        check = dict(self.request['checks'][0], id='renamed', values=['missing', 'A', 'A'])
        hit = records.run({'checks': [check]})
        self.assertEqual(hit['backend'], 'record-check-cache')
        self.assertEqual(hit['files_read_this_call'], 0)
        self.assertEqual(hit['checks']['renamed']['scope'], check)
        self.assertEqual(hit['checks']['renamed']['matches'], first['checks']['records']['matches'])
        self.assertEqual(hit['sources'], first['sources'])

    def test_added_check_only_scans_new_file_and_reordering_reuses_both(self):
        second = self.folder / 'second.json'
        second.write_text('{"items":[{"id":"B"}]}')
        self.manifest.write_text(json.dumps({'files': [{'path': 'data.json'}, {'path': 'second.json'}]}))
        records.run(self.request)
        extra = dict(self.request['checks'][0], id='second', file='second.json', values=['B'])
        request = {'checks': self.request['checks'] + [extra]}
        result = records.run(request)
        self.assertTrue(result['scan_complete'])
        self.assertEqual(result['files_read_this_call'], 1)
        self.assertEqual(result['checks_reused'], ['records'])
        self.assertEqual(len(result['checks']['second']['matches']), 1)
        reverse = records.run({'checks': list(reversed(request['checks']))})
        self.assertEqual(reverse['files_read_this_call'], 0)
        self.assertEqual(reverse['checks'], result['checks'])
        self.assertEqual(len(reverse['sources']), 2)

    def test_overlap_is_rejected_even_when_one_check_cached(self):
        self.source.write_text('{"items":[{"id":"A","nested":[]}]}')
        records.run(self.request)
        extra = dict(self.request['checks'][0], id='nested', pointer='/items/0/nested')
        with self.assertRaisesRegex(ValueError, 'Overlapping'):
            records.run({'checks': self.request['checks'] + [extra]})

    def test_mixed_scan_cannot_certify_cached_source_changed_during_scan(self):
        second = self.folder / 'second.json'
        second.write_text('{"items":[{"id":"B"}]}')
        self.manifest.write_text(json.dumps({'files': [{'path': 'data.json'}, {'path': 'second.json'}]}))
        records.run(self.request)
        extra = dict(self.request['checks'][0], id='second', file='second.json', values=['B'])
        original = records.at_pointer
        def changed(*args):
            self.source.write_text('{"items":[{"id":"C"}]}')
            return original(*args)
        with patch.object(records, 'at_pointer', changed):
            result = records.run({'checks': self.request['checks'] + [extra]})
        self.assertFalse(result['scan_complete'])
        self.assertFalse(result['checks']['records']['scan_complete'])
        self.assertIn('Cached source changed', result['checks']['records']['errors'][-1]['error'])

    def test_incomplete_check_does_not_prevent_reusing_independent_complete_check(self):
        extra = dict(self.request['checks'][0], id='missing', pointer='/missing')
        result = records.run({'checks': self.request['checks'] + [extra]})
        self.assertFalse(result['scan_complete'])
        hit = records.run({'checks': [dict(self.request['checks'][0], id='new')]})
        self.assertTrue(hit['scan_complete'])
        self.assertEqual(hit['files_read_this_call'], 0)

    def test_individual_symlink_and_corruption_fall_back_safely(self):
        records.run(self.request)
        path = next((self.root / 'Evals/.cache/records').glob('*.check'))
        path.write_text('broken')
        renamed = {'checks': [dict(self.request['checks'][0], id='renamed')]}
        self.assert_scan(records.run(renamed))
        external = self.root / 'keep.json'
        external.write_text('unchanged')
        path.unlink()
        path.symlink_to(external)
        self.assert_scan(records.run({'checks': [dict(self.request['checks'][0], id='again')]}))
        self.assertEqual(external.read_text(), 'unchanged')


if __name__ == '__main__':
    unittest.main()

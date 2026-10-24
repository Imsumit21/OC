import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import unittest
from unittest.mock import patch

import test_hg_compact_index as fixtures
import hg_search as h
import hg_compact_index as c
import hg_search_batch as b
import hg_get_many as g


class BatchReadTests(unittest.TestCase):
    setUp = fixtures.CompactTests.setUp
    tearDown = fixtures.CompactTests.tearDown
    args = fixtures.CompactTests.args
    prepare_portable = fixtures.AutomaticPackageTests.prepare_portable
    package = fixtures.AutomaticPackageTests.package

    def queries(self):
        return {'service': 'github', 'file': 'data.json', 'queries': [
            {'id': 'scoped', 'query': 'needle', 'pointer': '/rows/0'},
            {'id': 'limited', 'query': 'needle', 'pointer': '/rows/0', 'limit': 1},
            {'id': 'unicode', 'query': 'CAFÉ', 'pointer': '/rows/0/text'},
            {'id': 'absent', 'query': 'MISSING', 'pointer': '/rows/0'},
            {'id': 'key', 'query': 'B', 'pointer': '/rows/1', 'key': 'id'},
            {'id': 'case', 'query': 'NEEDLE', 'pointer': '/rows/0', 'case_sensitive': True}]}

    def assert_query_parity(self, request, result):
        for q in request['queries']:
            args = self.args(pointer=q.get('pointer', ''), query=q['query'],
                key=q.get('key'), limit=q.get('limit', 20),
                case_sensitive=q.get('case_sensitive', False))
            self.assertEqual(result['queries'][q['id']], h.scan_search(args))

    def reads(self):
        return {'items': [dict(id='a', service='github', file='data.json', pointer='/rows/0'),
                          dict(id='b', service='github', file='data.json', pointer='/rows/1')]}

    def cli(self, request, stdin=False):
        tools = self.root / 'Evals/tools'
        tools.mkdir(exist_ok=True)
        for name in ('hg_search.py', 'hg_compact_index.py', 'hg_search_batch.py',
                     'hg_search_index.py', 'hg_get_many.py'):
            shutil.copy2(Path(h.__file__).parent / name, tools / name)
        source = self.root / 'reads.json'
        source.write_text(json.dumps(request))
        return subprocess.run([sys.executable, str(tools/'hg_search.py'), 'get-many',
            '--request', '-' if stdin else str(source), '--progress', '--compact'],
            cwd=self.root.parent, input=json.dumps(request) if stdin else None,
            text=True, capture_output=True)

    def test_cli_works_from_another_directory_and_stdin(self):
        request = self.reads()
        expected = g.get_many(request)
        for stdin in (False, True):
            result = self.cli(request, stdin=stdin)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout), expected)

    def test_cli_reports_item_errors_with_nonzero_exit(self):
        request = self.reads()
        request['items'][1]['pointer'] = '/missing'
        result = self.cli(request)
        self.assertEqual(result.returncode, 1)
        payload = json.loads(result.stdout)
        self.assertFalse(payload['complete'])
        self.assertIn('text', payload['items']['a'])
        self.assertIn('error', payload['items']['b'])

    def test_cli_invalid_request_has_structured_stderr(self):
        result = self.cli({'items': []})
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, '')
        self.assertFalse(json.loads(result.stderr)['complete'])

    def test_indexed_queries_match_stream_including_completeness(self):
        c.build(h, 'github', 'data.json')
        r = self.queries()
        with patch.object(b, 'events', side_effect=AssertionError('Full scan used')):
            result = h.batch_search(r, no_cache=True)
        self.assertEqual(result['backend'], 'batch-compact-offset')
        self.assert_query_parity(r, result)


    def test_individual_reads_do_not_allocate_batch_node_map(self):
        c.build(h, 'github', 'data.json')
        original = c._load_file
        states = []
        def observe(*args):
            result = original(*args)
            states.append(c._OPERATIONS.get())
            return result
        with patch.object(c, '_load_file', observe):
            h.get(self.args(pointer='/rows/0'))
        self.assertFalse(states[0]['reuse_loads'])
        self.assertNotIn('node_maps', states[0])

    def test_large_deep_overlap_uses_one_shared_scan(self):
        self.path.write_text(json.dumps({'rows': [{'id': 'A', 'text': 'needle ' * 50000}, {'id': 'B', 'text': 'two'}]}))
        c.build(h, 'github', 'data.json')
        request = self.queries()
        with patch.object(c, 'search_existing', side_effect=AssertionError('Large repeated index scans')):
            with patch.object(b, 'events', wraps=b.events) as scan:
                result = h.batch_search(request, no_cache=True)
                self.assertEqual(scan.call_count, 1)
        self.assertEqual(result['backend'], 'batch-text-scan')
        self.assert_query_parity(request, result)

    def test_broad_batch_keeps_single_shared_scan(self):
        c.build(h, 'github', 'data.json')
        request = self.queries()
        for q in request['queries']:
            q['pointer'] = '/rows'
        with patch.object(c, 'search_existing', side_effect=AssertionError('Broad index route used')):
            with patch.object(b, 'events', wraps=b.events) as scan:
                result = h.batch_search(request, no_cache=True)
                self.assertEqual(scan.call_count, 1)
        self.assertEqual(result['backend'], 'batch-text-scan')
        self.assert_query_parity(request, result)

    def test_mixed_indexed_and_full_queries(self):
        c.build(h, 'github', 'data.json')
        r = self.queries()
        r['queries'].append({'id': 'unscoped', 'query': 'needle'})
        self.assert_query_parity(r, h.batch_search(r, no_cache=True))

    def test_duplicate_keys_preserved_in_search_and_first_get(self):
        self.path.write_text('{"rows":[{"text":"needle 1","text":"needle 2"}],"rows":[{"text":"needle 3"}]}')
        c.build(h, 'github', 'data.json')
        r = self.queries()
        self.assert_query_parity(r, h.batch_search(r, no_cache=True))
        reads = self.reads(); reads['items'] = reads['items'][:1]
        actual = g.get_many(reads)['items']['a']
        self.assertEqual({k:v for k,v in actual.items() if k != 'backend'}, h.scan_get(self.args(pointer='/rows/0')))

    def test_query_result_cache_preserved(self):
        c.build(h, 'github', 'data.json')
        first = h.batch_search(self.queries())
        again = h.batch_search(self.queries())
        self.assertEqual(again['backend'], 'query-cache')
        self.assertEqual(first['queries'], again['queries'])

    def test_changed_source_with_restored_mtime_is_not_reused(self):
        self.package()
        h.batch_search(self.queries())
        stat = self.path.stat()
        self.path.write_text(self.path.read_text().replace('needle', 'change'))
        os.utime(self.path, ns=(stat.st_atime_ns, stat.st_mtime_ns))
        actual = h.batch_search(self.queries())
        self.assertEqual(actual['backend'], 'batch-text-scan')
        self.assert_query_parity(self.queries(), actual)

    def test_source_changes_during_batch_are_not_certified(self):
        c.build(h, 'github', 'data.json')
        original = c.scoped_events
        def change(*args):
            yield from original(*args)
            self.path.write_text(self.path.read_text().replace('needle', 'change'))
        with patch.object(c, 'scoped_events', change):
            with self.assertRaises(ValueError):
                h.batch_search(self.queries(), no_cache=True)

    def test_get_many_text_citations_and_paging_match(self):
        c.build(h, 'github', 'data.json')
        reads = self.reads()
        reads['items'][0].update(offset=2, max_chars=7)
        out = g.get_many(reads)
        self.assertFalse(out['complete'])
        for item in reads['items']:
            actual = {k:v for k,v in out['items'][item['id']].items() if k != 'backend'}
            expected = h.scan_get(self.args(pointer=item['pointer'], offset=item.get('offset',0), max_chars=item.get('max_chars',12000)))
            self.assertEqual(actual, expected)

    def test_missing_read_returns_per_item_error(self):
        c.build(h, 'github', 'data.json')
        reads = self.reads(); reads['items'][1]['pointer'] = '/missing'
        out = g.get_many(reads)
        self.assertFalse(out['complete'])
        self.assertIn('text', out['items']['a'])
        self.assertIn('error', out['items']['b'])

    def test_verified_index_loaded_once_per_batch_and_never_across_calls(self):
        self.package()
        with patch.object(c, '_load_file', wraps=c._load_file) as load:
            g.get_many(self.reads())
            self.assertEqual(load.call_count, 1)
            g.get_many(self.reads())
            self.assertEqual(load.call_count, 2)

    def test_get_source_changes_inside_batch_are_not_certified(self):
        c.build(h, 'github', 'data.json')
        original = h.get
        def change(args):
            result = original(args)
            self.path.write_text(self.path.read_text().replace('needle', 'change'))
            return result
        with patch.object(h, 'get', change):
            with self.assertRaises(ValueError):
                g.get_many(self.reads())

    def test_corrupted_package_falls_back_to_current_sources(self):
        self.package()
        g.get_many(self.reads())
        self.artifact.write_text(self.artifact.read_text() + ' ')
        result = g.get_many(self.reads())
        self.assertTrue(result['complete'])
        self.assertEqual(result['items']['a']['backend'], 'stream')
        self.assertEqual(result['items']['a']['text'], h.scan_get(self.args(pointer='/rows/0'))['text'])

    def test_malformed_tail_fallback_keeps_incomplete_search(self):
        self.path.write_text('{"rows":[{"text":"needle"}], broken')
        out = h.batch_search(self.queries(), no_cache=True)
        self.assertFalse(out['queries']['scoped']['scan_complete'])
        self.assertTrue(out['queries']['scoped']['errors'])

    def test_read_validation_and_total_output_bound(self):
        for update in ({'offset':-1}, {'max_chars':0}, {'max_chars':True}, {'decode_base64':'yes'}, {'max_chars':600001}):
            request = self.reads(); request['items'][0].update(update)
            with self.assertRaises(ValueError): g.get_many(request)
        request = self.reads();request['items'][1]['id'] = 'a'
        with self.assertRaises(ValueError): g.get_many(request)


if __name__ == '__main__':
    unittest.main()

import base64
from contextlib import closing
import importlib.util
import io
import json
import os
from pathlib import Path
import sqlite3
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
spec = importlib.util.spec_from_file_location('search_under_test', TOOLS / 'hg_search.py')
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
import hg_search_index as cache


class IndexedSearchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.old_root, h.ROOT = h.ROOT, self.root
        self.folder = self.root / 'Base/gmail'
        self.folder.mkdir(parents=True)
        refs = self.root / 'Evals/references'
        refs.mkdir(parents=True)
        (refs / 'universe_manifest.json').write_text(json.dumps({'services': {'gmail': {'path': 'Base/gmail'}}}))
        self.records = []

    def tearDown(self):
        h.ROOT = self.old_root
        self.temp.cleanup()

    def source(self, name, data, raw=False):
        p = self.folder / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data if raw else json.dumps(data, ensure_ascii=False).encode())
        if name not in [r['path'] for r in self.records]:
            self.records.append({'path': name})
        self.save_manifest()
        return p

    def save_manifest(self):
        (self.folder / 'source_manifest.json').write_text(json.dumps({'files': self.records}))

    def search_args(self, query, **kw):
        args = dict(service='gmail', query=query, file=None, pointer='', key=None,
                    case_sensitive=False, limit=100, build_index=True)
        args.update(kw)
        return SimpleNamespace(**args)

    def read_args(self, pointer='', file='data.json', **kw):
        args = dict(service='gmail', file=file, pointer=pointer, offset=0,
                    max_chars=10000, decode_base64=False, build_index=True)
        args.update(kw)
        return SimpleNamespace(**args)

    def parity(self, args):
        expected = h.scan_search(args)
        result = h.search(args)
        self.assertIn(result['backend'], ('sqlite-trigram', 'sqlite-scan'), result)
        self.assertEqual({k: result[k] for k in expected}, expected)
        return result

    def test_literal_matching_filters_order_and_limits(self):
        self.source('b.json', {'rows': [{'id': 'ENG-123', 'text': 'Straße CAFÉ 😀 quote "abc" x%_y [xyz]'},
                                      {'id': 'ENG-124', 'text': 'after\x00needle'},
                                      {'id': 'a', 'text': 'line\nbreak'}],
                               'rows2': ['ENG-123'], 'a/b~c': {'value': 'escaped path'},
                               'nul\x00key': {'value': 'nested'}, 'bool': True, 'number': 1.25, 'nil': None})
        self.source('a.json', {'id': 'ENG-123', 'key_only_needle': 'different'})
        self.source('root/ignored.json', {'text': 'ENG-123'})
        for query in ['eng-12', 'ENG', '-12', '12', 'a', 'STRASSE', 'café', '😀', '"abc"',
                      'x%_y', '[xyz]', 'needle', 'after\x00needle', '\x00', 'line\nbreak',
                      'true', 'null', '1.25', 'key_only_needle', 'nonexistent']:
            with self.subTest(query=query):
                self.parity(self.search_args(query))
        for kw in [dict(file='b.json'), dict(pointer='/rows'), dict(pointer='/rows/0'),
                   dict(key='id'), dict(pointer='/a~1b~0c'), dict(pointer='/nul\x00key'),
                   dict(case_sensitive=True), dict(limit=1)]:
            args = self.search_args('ENG-123')
            for key, value in kw.items(): setattr(args, key, value)
            self.parity(args)
        self.parity(self.search_args('nested', pointer='/nul\x00key'))

    def test_gmail_raw_and_decoded_matching(self):
        text = 'Needle Straße café'
        encoded = base64.urlsafe_b64encode(text.encode()).decode()
        self.source('data.json', {'messages': [{'body': {'data': encoded}}, {'body': {'data': 'bad!'}}]})
        for query in ['NEEDLE', 'STRASSE', encoded[:5], 'café']:
            self.parity(self.search_args(query))
        args = self.read_args('/messages/0/body/data', decode_base64=True)
        self.assertEqual(h.get(args)['text'], text)

    def test_cached_search_never_reparses_unchanged_json(self):
        self.source('data.json', {'text': 'needle'})
        self.parity(self.search_args('needle'))
        with patch.object(h, 'Stream', side_effect=AssertionError('Unnecessary JSON scan')):
            found = h.search(self.search_args('needle'))
        self.assertEqual(len(found['matches']), 1)
        self.assertEqual(found['cache']['files_built'], 0)
        self.assertEqual(found['cache']['files_reused'], 1)

    def test_default_cold_search_and_get_do_not_build_indexes(self):
        self.source('data.json', {'text': 'needle'})
        result = h.search(self.search_args('needle', build_index=False))
        self.assertEqual(result['backend'], 'stream')
        self.assertEqual(h.get(self.read_args('/text', build_index=False))['text'], '"needle"')
        self.assertEqual(list((self.root/'Evals').rglob('*.sqlite3')), [])

    def test_default_reuses_current_index_without_becoming_writer(self):
        self.source('data.json', {'text': 'needle'})
        self.parity(self.search_args('needle'))
        # The existing writer's advisory lock does not prevent committed reads.
        with h.open_index(self.search_args('needle'), self.folder, self.records):
            with patch.object(h, 'Stream', side_effect=AssertionError('Unexpected source scan')):
                result = h.search(self.search_args('needle', build_index=False))
        self.assertIn(result['backend'], ('sqlite-trigram', 'sqlite-scan'))
        self.assertEqual(result['cache']['files_built'], 0)

    def test_default_stale_index_scans_without_rebuilding(self):
        self.source('data.json', {'text': 'oldneedle'})
        self.parity(self.search_args('oldneedle'))
        self.source('data.json', {'text': 'newneedle'})
        result = h.search(self.search_args('newneedle', build_index=False))
        self.assertEqual(result['backend'], 'stream')
        self.assertEqual(len(result['matches']), 1)

    def test_writer_contention_fallback_cooldown_and_explicit_recovery(self):
        self.source('data.json', {'text': 'needle'})
        with h.open_index(self.search_args('needle'), self.folder, self.records):
            result = h.search(self.search_args('needle'))
            self.assertEqual(result['backend'], 'stream')
            self.assertIn('locked', result['cache_warning'])
            with patch.object(h, 'open_index', side_effect=AssertionError('Repeated locked-cache attempt')):
                fallback = h.search(self.search_args('needle', build_index=False))
            self.assertEqual(fallback['matches'], result['matches'])
        h.build_index(SimpleNamespace(service='gmail', file=None, rebuild=False))
        result = h.search(self.search_args('needle', build_index=False))
        self.assertIn(result['backend'], ('sqlite-trigram', 'sqlite-scan'))
        self.assertNotIn('cache_warning', result)

    def test_direct_get_unicode_bom_crlf_escaped_keys_and_paging(self):
        data = {'padding': '€😀' * 40000, 'a/b~c': [{'text': 'café\r\nline', 'n': 1.2e-15}], 'empty': []}
        raw = b'\xef\xbb\xbf' + json.dumps(data, ensure_ascii=False, indent=2).replace('\n', '\r\n').encode()
        self.source('data.json', raw, raw=True)
        self.parity(self.search_args('café'))
        args = self.read_args('/a~1b~0c/0', max_chars=7)
        pieces = []
        starts = []
        original = h.Stream
        def observe(handle, **kwargs):
            starts.append(handle.tell())
            return original(handle, **kwargs)
        with patch.object(h, 'Stream', side_effect=observe):
            while True:
                got = h.get(args)
                self.assertEqual(got['backend'], 'sqlite-trigram' if cache_supports_fts() else 'sqlite-scan')
                pieces.append(got['text'])
                if not got['truncated']: break
                args.offset = got['next_offset']
        self.assertEqual(json.loads(''.join(pieces)), data['a/b~c'][0])
        self.assertTrue(all(offset > 200000 for offset in starts), starts)
        for pointer in ['', '/empty', '/a~1b~0c/0/n', '/padding']:
            args = self.read_args(pointer, max_chars=123)
            expected = h.scan_get(args)
            actual = h.get(args)
            self.assertEqual({k: actual[k] for k in expected}, expected)

    def test_offset_tracking_at_every_chunk_boundary(self):
        source = '{\r\n"€": ["😀", -1.2e-15, true, null], "last":{}}'
        for chunk in range(1, 20):
            stream = h.Stream(io.StringIO(source), chunk=chunk, track_offsets=True)
            for event, path, value in stream.events():
                if event == 'end': continue
                tail = source.encode()[stream.event_offset:].decode()
                decoded, _ = json.JSONDecoder().raw_decode(tail)
                expected = json.loads(source)
                for part in path: expected = expected[int(part)] if isinstance(expected, list) else expected[part]
                self.assertEqual(decoded, expected)

    def test_refresh_even_if_size_and_mtime_are_restored(self):
        p = self.source('data.json', {'text': 'oldneedle'})
        self.parity(self.search_args('oldneedle'))
        before = p.stat()
        self.source('data.json', {'text': 'newneedle'})
        os.utime(p, ns=(before.st_atime_ns, before.st_mtime_ns))
        self.assertEqual(len(self.parity(self.search_args('oldneedle'))['matches']), 0)
        self.assertEqual(len(self.parity(self.search_args('newneedle'))['matches']), 1)

    def test_file_addition_manifest_removal_and_missing_source(self):
        p = self.source('a.json', {'text': 'needle'})
        self.parity(self.search_args('needle'))
        self.source('b.json', {'text': 'needle'})
        self.assertEqual(len(self.parity(self.search_args('needle'))['matches']), 2)
        self.records = [r for r in self.records if r['path'] != 'a.json']
        self.save_manifest()
        result = self.parity(self.search_args('needle'))
        self.assertEqual([r['service_file'] for r in result['matches']], ['b.json'])
        with closing(sqlite3.connect(self.root / result['cache']['path'])) as db:
            self.assertEqual(db.execute("SELECT count(*) FROM files WHERE path='a.json'").fetchone()[0], 0)
        (self.folder/'b.json').unlink()
        result = h.search(self.search_args('needle'))
        self.assertFalse(result['scan_complete'])
        self.assertTrue(result['errors'])
        self.assertEqual(result['matches'], [])

    def test_malformed_changed_source_falls_back_without_stale_hits(self):
        self.source('data.json', {'text': 'oldneedle'})
        self.parity(self.search_args('oldneedle'))
        self.source('data.json', b'{"text":"newneedle", broken', raw=True)
        args = self.search_args('needle')
        expected = h.scan_search(args)
        actual = h.search(args)
        self.assertEqual({k: actual[k] for k in expected}, expected)
        self.assertEqual(actual['backend'], 'stream')
        self.assertNotIn('oldneedle', str(actual['matches']))

    def test_corrupt_cache_fallback_and_explicit_rebuild(self):
        self.source('data.json', {'text': 'needle'})
        result = self.parity(self.search_args('needle'))
        db_path = self.root / result['cache']['path']
        db_path.write_bytes(b'broken cache')
        result = h.search(self.search_args('needle'))
        self.assertEqual(result['backend'], 'stream')
        self.assertEqual(len(result['matches']), 1)
        h.build_index(SimpleNamespace(service='gmail', file=None, rebuild=True))
        self.parity(self.search_args('needle'))

    def test_unavailable_cache_and_explicit_scan(self):
        self.source('data.json', {'text': 'needle'})
        with patch.object(cache, 'SearchIndex', side_effect=OSError('read-only cache')):
            self.assertEqual(h.search(self.search_args('needle'))['backend'], 'stream')
            self.assertEqual(h.get(self.read_args('/text'))['text'], '"needle"')
        with patch.object(h, 'open_index', side_effect=AssertionError('Explicit scan must bypass cache')):
            args = self.search_args('needle', no_index=True)
            self.assertEqual(h.search(args)['backend'], 'stream')
            self.assertEqual(h.get(self.read_args('/text', no_index=True))['text'], '"needle"')

    def test_without_trigram_extension(self):
        self.source('data.json', {'text': 'Straße needle'})
        with patch.object(cache.SearchIndex, '_fts', return_value=False):
            result = self.parity(self.search_args('STRASSE'))
            self.assertEqual(result['backend'], 'sqlite-scan')
            self.assertEqual(len(result['matches']), 1)

    def test_failed_build_rolls_back_and_next_search_recovers(self):
        self.source('data.json', {'rows': ['needle'] * 600})
        with patch.object(cache.SearchIndex, '_insert', side_effect=OSError('interrupted build')):
            result = h.search(self.search_args('needle'))
            self.assertEqual(result['backend'], 'stream')
        for path in (self.root/'Evals/.cache/search').glob('*.sqlite3'):
            with closing(sqlite3.connect(path)) as db:
                self.assertEqual(db.execute('SELECT count(*) FROM files').fetchone()[0], 0)
        self.parity(self.search_args('needle'))

    def test_narrow_search_builds_only_selected_files(self):
        self.source('a.json', {'text': 'needle'})
        self.source('b.json', {'text': 'needle'})
        result = self.parity(self.search_args('needle', file='a.json'))
        with closing(sqlite3.connect(self.root/result['cache']['path'])) as db:
            self.assertEqual([r[0] for r in db.execute('SELECT path FROM files')], ['a.json'])

    def test_changed_source_during_read_discards_index_result(self):
        self.source('data.json', {'text': 'oldneedle'})
        self.parity(self.search_args('oldneedle'))
        original = cache.SearchIndex.matches
        def changing(index, *args):
            yield from original(index, *args)
            self.source('data.json', {'text': 'newneedle'})
        with patch.object(cache.SearchIndex, 'matches', changing):
            result = h.search(self.search_args('oldneedle'))
        self.assertEqual(result['backend'], 'stream')
        self.assertEqual(result['matches'], [])

    def test_manifest_traversal_and_symlinks_cannot_escape(self):
        self.source('data.json', {'text': 'needle'})
        outside = self.root/'outside.json'
        outside.write_text('{"text":"secret"}')
        (self.folder/'escape.json').symlink_to(outside)
        self.records.append({'path': 'escape.json'})
        self.save_manifest()
        result = h.search(self.search_args('secret'))
        self.assertEqual(result['matches'], [])
        self.assertTrue(result['errors'])
        with self.assertRaises(ValueError): h.get(self.read_args(file='../outside.json'))


def cache_supports_fts():
    with closing(sqlite3.connect(':memory:')) as db:
        try:
            db.execute("CREATE VIRTUAL TABLE probe USING fts5(text, tokenize='trigram case_sensitive 1')")
            return True
        except sqlite3.OperationalError:
            return False


if __name__ == '__main__':
    unittest.main()

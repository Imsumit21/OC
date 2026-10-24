import json, os, sys, tempfile, unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import hg_search as h
import hg_compact_index as c
class CompactTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name).resolve();self.folder=self.root/'Base';self.folder.mkdir()
  refs=self.root/'Evals/references';refs.mkdir(parents=True);(refs/'universe_manifest.json').write_text(json.dumps({'services':{'github':{'path':'Base'}}}))
  self.path=self.folder/'data.json';self.path.write_text('{"rows":[{"id":"A","text":"needle café"},{"id":"B","text":"needle two"}],"end":42}')
  self.manifest=self.folder/'source_manifest.json';self.manifest.write_text(json.dumps({'files':[{'path':'data.json','sha256':'declared'}]}))
  self.p=patch.object(h,'ROOT',self.root);self.p.start()
 def tearDown(self):self.p.stop();self.tmp.cleanup()
 def args(self,**kw):
  d=dict(service='github',file='data.json',pointer='/rows',query='needle',key=None,case_sensitive=False,limit=20,no_index=False,build_index=False,offset=0,max_chars=12000,decode_base64=False);d.update(kw);return SimpleNamespace(**d)
 def stripped(self,x):return {k:v for k,v in x.items() if k!='backend'}
 def test_scope_and_limit_parity(self):
  c.build(h,'github','data.json')
  for opts in ({},{'query':'absent'},{'pointer':'/rows/1'},{'pointer':'/rows/1/text'},{'limit':1},{'key':'id','query':'A'},{'query':'CAFÉ'},{'query':'CAFÉ','case_sensitive':True}):
   a=self.args(**opts);out=h.search(a);self.assertEqual(out['backend'],'compact-offset');self.assertEqual(self.stripped(out),h.scan_search(a))
 def test_get_paging(self):
  c.build(h,'github','data.json')
  for pointer in ('/rows','/rows/0','/rows/1/text'):
   for offset in (0,3,10):
    a=self.args(pointer=pointer,max_chars=12,offset=offset);self.assertEqual(self.stripped(h.get(a)),h.scan_get(a))
 def test_duplicates(self):
  self.path.write_text('{"rows":[{"text":"needle 1","text":"needle 2"}],"rows":[{"text":"needle 3"}]}');c.build(h,'github','data.json');a=self.args(pointer='/rows/0/text')
  self.assertEqual(self.stripped(h.search(a)),h.scan_search(a));self.assertEqual(len(h.search(a)['matches']),3);self.assertEqual(self.stripped(h.get(a)),h.scan_get(a))
 def test_bom_crlf_unicode_escapes(self):
  self.path.write_bytes(b'\xef\xbb\xbf'+json.dumps({'a/b~c':[{'text':'café needle'}]},ensure_ascii=False,indent=2).replace('\n','\r\n').encode());c.build(h,'github','data.json');a=self.args(pointer='/a~1b~0c/0/text')
  self.assertEqual(self.stripped(h.search(a)),h.scan_search(a));self.assertEqual(self.stripped(h.get(a)),h.scan_get(a))
 def test_source_change_restored_mtime(self):
  c.build(h,'github','data.json');st=self.path.stat();self.path.write_text(self.path.read_text().replace('needle','change'));os.utime(self.path,ns=(st.st_atime_ns,st.st_mtime_ns));a=self.args();self.assertIsNone(c.search_existing(h,a));self.assertEqual(h.search(a)['matches'],[])
 def test_corruption(self):
  c.build(h,'github','data.json');c.index_path(h,'github','data.json').write_text('{}');a=self.args();self.assertIsNone(c.search_existing(h,a));self.assertEqual(self.stripped(h.search(a)),h.scan_search(a))
 def test_malformed_tail(self):
  self.path.write_text(self.path.read_text()+' trailing')
  with self.assertRaises(ValueError):c.build(h,'github','data.json')
  self.assertFalse(h.search(self.args())['scan_complete'])
 def test_manifest_changed(self):
  c.structured_info(h,'github');st=self.manifest.stat();self.manifest.write_text(self.manifest.read_text().replace('data.json','gone.json'));os.utime(self.manifest,ns=(st.st_atime_ns,st.st_mtime_ns));self.assertEqual(c.structured_info(h,'github')[1][0]['path'],'gone.json')
 def test_change_during_read(self):
  c.build(h,'github','data.json');orig=c.scoped_events
  def change(*args):
   yield from orig(*args)
   self.path.write_text(self.path.read_text().replace('needle','change'))
  with patch.object(c,'scoped_events',change):self.assertIsNone(c.search_existing(h,self.args()))
 def test_absent_pointer(self):
  c.build(h,'github','data.json');a=self.args(pointer='/missing/0');self.assertEqual(self.stripped(h.search(a)),h.scan_search(a))
  with self.assertRaises(ValueError):h.get(a)
 def test_blob_read(self):
  (self.folder/'root').mkdir();(self.folder/'root/x.json').write_text('{"x":1}');self.manifest.write_text(json.dumps({'files':[{'path':'data.json'},{'path':'root/x.json'}]}));self.assertEqual(h.get(self.args(file='root/x.json',pointer='/x'))['text'],'1')
 def test_no_implicit_build(self):
  self.assertFalse(c.index_path(h,'github','data.json').exists());h.search(self.args());self.assertFalse(c.index_path(h,'github','data.json').exists())

 def test_large_manifest_cache_is_lossless_and_below_entry_limit(self):
  rows=[{'path':f'messages/{i}.json','bytes':i,'sha256':format(i,'064x'),
         'extra':{'unicode':'café', 'flag':True}} for i in range(15000)]
  packed=c.pack_manifest(rows)
  self.assertIn('files_zlib_base64',packed)
  self.assertLess(len(json.dumps(packed)),8*1024*1024)
  self.assertEqual(c.unpack_manifest(packed),rows)
 def test_compressed_manifest_corruption_and_expansion_are_rejected(self):
  import zlib,base64
  with self.assertRaises((ValueError,zlib.error)):c.unpack_manifest({'files_zlib_base64':'broken!'})
  raw=zlib.compress(b' '*100)
  with patch.object(c,'MANIFEST_MAX_DECODED',10):
   with self.assertRaises(ValueError):c.unpack_manifest({'files_zlib_base64':base64.b64encode(raw).decode()})
 def test_large_routing_cache_invalidates_on_manifest_edit(self):
  rows=[{'path':f'messages/{i}.json','bytes':i,'sha256':format(i,'064x')} for i in range(15000)]
  self.manifest.write_text(json.dumps({'files':rows}))
  self.assertEqual(c.structured_info(h,'github')[1],list(h.candidates(rows)))
  self.assertEqual(c.structured_info(h,'github')[1],list(h.candidates(rows)))
  rows.append({'path':'messages/new.json'})
  self.manifest.write_text(json.dumps({'files':rows}))
  self.assertEqual(c.structured_info(h,'github')[1],list(h.candidates(rows)))

class PortableTests(unittest.TestCase):
 setUp=CompactTests.setUp
 tearDown=CompactTests.tearDown
 args=CompactTests.args
 stripped=CompactTests.stripped
 def prepare_portable(self):
  import hashlib
  self.manifest.write_text(json.dumps({'files':[{'path':'data.json','sha256':hashlib.sha256(self.path.read_bytes()).hexdigest()}]}))
  c.build(h,'github','data.json');out=self.root/'index.json';self.artifact_hash=c.export_portable(h,'github','data.json',out)['artifact_sha256'];return out
 def test_move_and_import(self):
  import shutil
  out=self.prepare_portable()
  with tempfile.TemporaryDirectory() as relocated:
   other=Path(relocated).resolve();shutil.copytree(self.root/'Base',other/'Base');shutil.copytree(self.root/'Evals/references',other/'Evals/references')
   with patch.object(h,'ROOT',other):
    self.assertTrue(c.import_portable(h,out,self.artifact_hash)['complete']);self.assertEqual(h.search(self.args())['backend'],'compact-offset');self.assertEqual(self.stripped(h.search(self.args())),h.scan_search(self.args()))
 def test_portable_changed_source_rejected(self):
  out=self.prepare_portable();self.path.write_text(self.path.read_text().replace('needle','change'))
  with self.assertRaises(ValueError):c.import_portable(h,out,self.artifact_hash)
 def test_portable_corruption_rejected(self):
  out=self.prepare_portable();data=json.loads(out.read_text());data['payload']['data']['nodes'][0][1]+=1;out.write_text(json.dumps(data))
  with self.assertRaises(ValueError):c.import_portable(h,out,self.artifact_hash)
 def test_source_change_during_import(self):
  out=self.prepare_portable();original=c.content_sha256
  def change(path):
   digest=original(path);path.write_text(path.read_text().replace('needle','change'));return digest
  with patch.object(c,'content_sha256',change):
   with self.assertRaises(ValueError):c.import_portable(h,out,self.artifact_hash)

class ManifestRaceTests(unittest.TestCase):
 setUp=CompactTests.setUp
 tearDown=CompactTests.tearDown
 args=CompactTests.args
 def test_manifest_shard_added_during_scope_read(self):
  c.build(h,'github','data.json');original=c.scoped_events
  extra=self.folder/'extra.json';extra.write_text('{"rows":[{"text":"needle new"}]}')
  def change(*args):
   yield from original(*args)
   self.manifest.write_text(json.dumps({'files':[{'path':'data.json','sha256':'declared'},{'path':'extra.json'}]}))
  with patch.object(c,'scoped_events',change):
   self.assertIsNone(c.search_existing(h,self.args(file='*.json')))
  out=h.search(self.args(file='*.json'));self.assertTrue(out['scan_complete']);self.assertEqual(out['files_selected'],2);self.assertEqual(len(out['matches']),3)
 def test_universe_mapping_change_during_get(self):
  c.build(h,'github','data.json');original=c.scoped_events
  def change(*args):
   yield from original(*args)
   (self.root/'Evals/references/universe_manifest.json').write_text(json.dumps({'services':{'github':{'path':'Gone'}}}))
  with patch.object(c,'scoped_events',change):
   self.assertIsNone(c.search_existing(h,self.args()))

class AutomaticPackageTests(unittest.TestCase):
    setUp = CompactTests.setUp
    tearDown = CompactTests.tearDown
    args = CompactTests.args
    stripped = CompactTests.stripped
    prepare_portable = PortableTests.prepare_portable

    def package(self):
        import shutil
        artifact = self.prepare_portable()
        directory = self.root / 'Evals/references/search_indexes'
        directory.mkdir(parents=True)
        self.artifact = directory / 'github-data.json'
        shutil.copy2(artifact, self.artifact)
        self.package_manifest = directory / 'manifest.json'
        payload = json.loads(self.artifact.read_text())['payload']
        self.package_manifest.write_text(json.dumps({
            'version': c.PACKAGE_VERSION,
            'indexes': [{'service': 'github', 'file': 'data.json',
                         'path': self.artifact.name, 'sha256': self.artifact_hash,
                         'source_sha256': payload['source_sha256']}]}))
        c.index_path(h, 'github', 'data.json').unlink()

    def test_automatic_first_use_hashes_source_once_and_repeat_reuses(self):
        self.package()
        with patch.object(c, 'content_sha256', wraps=c.content_sha256) as hashing:
            first = h.search(self.args())
            again = h.search(self.args())
        self.assertEqual(first['backend'], 'compact-offset')
        self.assertEqual(again, first)
        self.assertEqual(sum(call.args[0] == self.path for call in hashing.call_args_list), 1)
        self.assertEqual(self.stripped(first), h.scan_search(self.args()))

    def test_automatic_get_paging_matches_stream(self):
        self.package()
        args = self.args(pointer='/rows/1/text', offset=3, max_chars=5)
        result = h.get(args)
        self.assertEqual(result['backend'], 'compact-offset')
        self.assertEqual(self.stripped(result), h.scan_get(args))

    def test_same_size_and_mtime_source_change_invalidates_import(self):
        self.package()
        self.assertEqual(h.search(self.args())['backend'], 'compact-offset')
        stat = self.path.stat()
        self.path.write_text(self.path.read_text().replace('needle', 'change'))
        os.utime(self.path, ns=(stat.st_atime_ns, stat.st_mtime_ns))
        result = h.search(self.args())
        self.assertEqual(result['backend'], 'stream')
        self.assertEqual(result['matches'], [])

    def test_source_mismatch_is_not_rehashed_until_binding_changes(self):
        self.package()
        self.path.write_text(self.path.read_text().replace('needle', 'change'))
        with patch.object(c, 'content_sha256', wraps=c.content_sha256) as hashing:
            self.assertEqual(h.search(self.args())['backend'], 'stream')
            self.assertEqual(h.search(self.args())['backend'], 'stream')
        self.assertEqual(sum(call.args[0] == self.path for call in hashing.call_args_list), 1)
        self.path.write_text(self.path.read_text().replace('change', 'needle'))
        self.assertEqual(h.search(self.args())['backend'], 'compact-offset')

    def test_artifact_pin_corruption_never_reads_source_hash(self):
        self.package()
        self.artifact.write_text(self.artifact.read_text() + ' ')
        with patch.object(c, 'content_sha256', wraps=c.content_sha256) as hashing:
            result = h.search(self.args())
        self.assertEqual(result['backend'], 'stream')
        self.assertFalse(any(call.args[0] == self.path for call in hashing.call_args_list))
        self.assertEqual(self.stripped(result), h.scan_search(self.args()))

    def test_pin_change_invalidates_existing_import(self):
        self.package()
        self.assertEqual(h.search(self.args())['backend'], 'compact-offset')
        package = json.loads(self.package_manifest.read_text())
        package['indexes'][0]['sha256'] = '0' * 64
        self.package_manifest.write_text(json.dumps(package))
        self.assertEqual(h.search(self.args())['backend'], 'stream')

    def test_package_manifest_change_during_read_discards_result(self):
        self.package()
        original = c.scoped_events
        def change(*args):
            yield from original(*args)
            self.package_manifest.write_text(self.package_manifest.read_text() + ' ')
        with patch.object(c, 'scoped_events', change):
            self.assertIsNone(c.search_existing(h, self.args()))

    def test_helper_bytes_change_revalidates_source_even_with_same_mtime(self):
        self.package()
        helper = self.root / 'helper.py'
        helper.write_text('version=1')
        api = h.compact_api()
        api.helper_paths = (helper,)
        with patch.object(h, 'compact_api', return_value=api):
            self.assertEqual(h.search(self.args())['backend'], 'compact-offset')
            stat = helper.stat()
            helper.write_text('version=2')
            os.utime(helper, ns=(stat.st_atime_ns, stat.st_mtime_ns))
            with patch.object(c, 'content_sha256', wraps=c.content_sha256) as hashing:
                self.assertEqual(h.search(self.args())['backend'], 'compact-offset')
            self.assertEqual(sum(call.args[0] == self.path for call in hashing.call_args_list), 1)

    def test_unwritable_cache_falls_back_without_source_writes(self):
        self.package()
        before = self.path.read_bytes()
        with patch.object(c, 'write_cache', return_value=None):
            self.assertEqual(h.search(self.args())['backend'], 'stream')
        self.assertEqual(self.path.read_bytes(), before)

    def test_explicit_no_index_never_imports(self):
        self.package()
        with patch.object(c, 'read_portable', side_effect=AssertionError('Unexpected import')):
            result = h.search(self.args(no_index=True))
        self.assertEqual(result['backend'], 'stream')
        self.assertFalse(c.index_path(h, 'github', 'data.json').exists())

    def test_explicit_build_keeps_existing_sqlite_behavior(self):
        self.package()
        with patch.object(c, 'read_portable', side_effect=AssertionError('Unexpected import')):
            result = h.search(self.args(build_index=True))
        self.assertTrue(result['backend'].startswith('sqlite'))
        self.assertFalse(c.index_path(h, 'github', 'data.json').exists())

    def test_malformed_payload_with_new_pin_falls_back(self):
        import hashlib
        self.package()
        value = json.loads(self.artifact.read_text())
        value['payload']['data']['nodes'][0][2] = self.path.stat().st_size + 1
        value['checksum'] = c.batch.digest(value['payload'])
        self.artifact.write_text(json.dumps(value))
        package = json.loads(self.package_manifest.read_text())
        package['indexes'][0]['sha256'] = hashlib.sha256(self.artifact.read_bytes()).hexdigest()
        self.package_manifest.write_text(json.dumps(package))
        self.assertEqual(h.search(self.args())['backend'], 'stream')

    def test_malformed_package_shape_falls_back(self):
        self.package()
        for value in ([], None, {"version": c.PACKAGE_VERSION, "indexes": [None]}):
            with self.subTest(value=value):
                self.package_manifest.write_text(json.dumps(value))
                result = h.search(self.args())
                self.assertEqual(result['backend'], 'stream')
                self.assertEqual(self.stripped(result), h.scan_search(self.args()))

    def test_duplicate_package_keys_fall_back(self):
        self.package()
        self.package_manifest.write_text('{"version":"a","version":"b","indexes":[]}')
        self.assertEqual(h.search(self.args())['backend'], 'stream')

    def test_incompatible_version_falls_back(self):
        self.package()
        package = json.loads(self.package_manifest.read_text())
        package['version'] = 'future-version'
        self.package_manifest.write_text(json.dumps(package))
        self.assertEqual(h.search(self.args())['backend'], 'stream')

    def test_corrupt_runtime_cache_reimports_valid_package(self):
        self.package()
        h.search(self.args())
        c.index_path(h, 'github', 'data.json').write_text('{}')
        result = h.search(self.args())
        self.assertEqual(result['backend'], 'compact-offset')
        self.assertEqual(self.stripped(result), h.scan_search(self.args()))

    def test_search_multiple_files_falls_back_for_unindexed_scope(self):
        self.package()
        h.search(self.args())
        extra = self.folder / 'extra.json'
        extra.write_text('{"rows":[{"text":"needle three"}]}')
        records = json.loads(self.manifest.read_text())
        records['files'].append({'path': 'extra.json'})
        self.manifest.write_text(json.dumps(records))
        result = h.search(self.args(file='*.json'))
        self.assertEqual(result['backend'], 'stream')
        self.assertEqual(result['files_selected'], 2)
        self.assertEqual(len(result['matches']), 3)
        self.assertTrue(result['scan_complete'])

    def test_blob_access_bypasses_structured_index(self):
        self.package()
        (self.folder / 'root').mkdir()
        (self.folder / 'root/artifact.txt').write_text('independent artifact')
        records = json.loads(self.manifest.read_text())
        records['files'].append({'path': 'root/artifact.txt'})
        self.manifest.write_text(json.dumps(records))
        folder, all_files = h.service_info('github')
        self.assertIn('root/artifact.txt', [item['path'] for item in all_files])
        self.assertEqual(h.safe_file(folder, 'root/artifact.txt').read_text(), 'independent artifact')

    def test_source_change_during_automatic_hash_is_not_certified(self):
        self.package()
        original = c.content_sha256
        def change(path):
            value = original(path)
            if path == self.path:
                path.write_text(path.read_text().replace('needle', 'change'))
            return value
        with patch.object(c, 'content_sha256', change):
            self.assertIsNone(c.search_existing(h, self.args()))
        self.assertEqual(h.search(self.args())['matches'], [])


if __name__ == '__main__':
    unittest.main()

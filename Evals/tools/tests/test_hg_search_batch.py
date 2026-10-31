import base64
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import importlib.util
import hg_search_batch as batch
from universe_fixture import routing, select

def helper(root):
    spec = importlib.util.spec_from_file_location('batch_test_search', TOOLS / 'hg_search.py')
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)
    h.ROOT = Path(root).resolve()
    return h

def search_many(root, request, **kwargs):
    return batch.search_many(helper(root).batch_api(), request, **kwargs)


class TextTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='hg-text-fixture-')
        self.root=Path(self.tmp.name).resolve()
        (self.root/'Evals/tools').mkdir(parents=True);(self.root/'Evals/references').mkdir()
        for name in ['hg_search.py','hg_search_index.py','hg_search_batch.py', 'hg_compact_index.py', 'hg_universe.py']:
            shutil.copy2(TOOLS/name,self.root/'Evals/tools'/name)
        self.folder=self.root/'Base/gmail';self.folder.mkdir(parents=True)
        select(self.root).write_text(json.dumps({'services':{'gmail':{'path':'Base/gmail'}}}))
        self.rows=[]

    def tearDown(self): self.tmp.cleanup()

    def source(self,name,data,raw=False):
        p=self.folder/name;p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(data if raw else json.dumps(data,ensure_ascii=False))
        if not any(r['path']==name for r in self.rows):self.rows.append({'path':name})
        (self.folder/'source_manifest.json').write_text(json.dumps({'files':self.rows}))
        return p

    def parity(self,queries,**opts):
        request={'service':'gmail','queries':queries}
        actual=search_many(self.root,request,no_cache=True,**opts)
        h=helper(self.root)
        for q in queries:
            args=SimpleNamespace(service='gmail',file=None,pointer=q.get('pointer',''),key=q.get('key'),
                query=q['query'],case_sensitive=q.get('case_sensitive',False),limit=q.get('limit',20))
            self.assertEqual(actual['queries'][q['id']],h.scan_search(args))
        return actual

    def test_literals_unicode_limits_keys_and_pointers(self):
        self.source('a.json',{'rows':[{'id':'ENG-123','text':'Straße CAFÉ x%_y quote "abc" 😀'},
            {'id':'ENG-124','text':'needle after\x00nul'}, {'text':'needle again'}],
            'a/b~c':{'from':'Arthur.Blake'},'number':1.25,'bool':True,'nil':None})
        self.source('b.json',{'text':'needle final'})
        self.source('root/ignored.json',{'text':'needle ignored'})
        queries=[{'id':str(i),'query':x,'limit':100} for i,x in enumerate(
            ['eng-12','STRASSE','café','x%_y','"abc"','😀','\x00','1.25','true','null','missing'])]
        queries += [{'id':'limit','query':'needle','limit':1},
                    {'id':'key','query':'eng','key':'id'},
                    {'id':'pointer','query':'arthur','pointer':'/a~1b~0c'},
                    {'id':'case','query':'CAFÉ','case_sensitive':True}]
        self.parity(queries)

    def test_decoded_gmail_and_raw_base64(self):
        text='The build machine: Straße café'
        encoded=base64.urlsafe_b64encode(text.encode()).decode().rstrip('=')
        self.source('a.json',{'messages':[{'body':{'data':encoded}},{'body':{'data':'bad!'}}]})
        result=self.parity([{'id':'decoded','query':'build machine'},
                           {'id':'unicode','query':'STRASSE'},
                           {'id':'raw','query':encoded[:8]}])
        self.assertEqual(result['queries']['decoded']['matches'][0]['encoding'],'base64url-utf8')

    def test_duplicate_keys_and_forced_streaming(self):
        self.source('a.json','{"text":"needle one","text":"needle two"}',raw=True)
        self.parity([{'id':'x','query':'needle'}])
        self.parity([{'id':'x','query':'needle'}],threshold=1)

    def test_malformed_tail_and_limit_parity(self):
        self.source('a.json','{"text":"needle", broken',raw=True)
        self.source('b.json',{'text':'needle'})
        self.parity([{'id':'all','query':'needle'},{'id':'limit','query':'needle','limit':1}])

    def test_cache_repeat_and_source_change(self):
        p=self.source('a.json',{'text':'oldneedle'})
        request={'service':'gmail','queries':[{'id':'x','query':'oldneedle'}]}
        old=search_many(self.root,request);cached=search_many(self.root,request)
        self.assertEqual(old['queries'],cached['queries'])
        self.assertEqual(cached['backend'],'query-cache')
        stat=p.stat();self.source('a.json',{'text':'newneedle'});os.utime(p,ns=(stat.st_atime_ns,stat.st_mtime_ns))
        fresh=search_many(self.root,request)
        self.assertEqual(fresh['backend'],'batch-text-scan')
        self.assertEqual(fresh['queries']['x']['matches'],[])

    def test_missing_source_and_corrupt_cache(self):
        p=self.source('a.json',{'text':'needle'})
        request={'service':'gmail','queries':[{'id':'x','query':'needle'}]}
        search_many(self.root,request)
        for cache in (self.root/'Evals/.cache/queries').glob('*.json'): cache.write_text('broken')
        self.assertEqual(search_many(self.root,request)['backend'],'batch-text-scan')
        p.unlink();result=search_many(self.root,request)['queries']['x']
        self.assertFalse(result['scan_complete']);self.assertTrue(result['errors'])

    def test_progress_is_separate_from_JSON_stdout(self):
        self.source('a.json',{'text':'needle'})
        request=self.root/'request.json';request.write_text(json.dumps({'service':'gmail','queries':[{'id':'x','query':'needle'}]}))
        run=subprocess.run([sys.executable,str(self.root/'Evals/tools/hg_search.py'),'search-many',
            '--request',str(request),'--no-cache','--progress'],capture_output=True,text=True)
        self.assertEqual(run.returncode,0,run.stderr)
        self.assertTrue(json.loads(run.stdout)['queries']['x']['matches'])
        self.assertIn('Scanning gmail',run.stderr)

    def test_source_removed_during_search_prevents_complete_result(self):
        self.source('a.json',{'text':'needle'})
        original=batch.events
        def removing(h,path,threshold):
            yield from original(h,path,threshold)
            path.unlink()
        with patch.object(batch,'events',removing):
            result=search_many(self.root,{'service':'gmail','queries':[{'id':'x','query':'needle'}]},no_cache=True)
        self.assertFalse(result['queries']['x']['scan_complete'])
        self.assertTrue(result['queries']['x']['errors'])

    def test_no_cache_write_location_falls_back(self):
        self.source('a.json',{'text':'needle'});(self.root/'Evals/.cache').write_text('file')
        result=search_many(self.root,{'service':'gmail','queries':[{'id':'x','query':'needle'}]})
        self.assertTrue(result['queries']['x']['scan_complete']);self.assertIn('cache_warning',result)

    def test_failed_initial_freshness_check_cannot_certify_coverage(self):
        self.source('a.json', {'text': 'needle'})
        with patch.object(batch, 'fingerprint', side_effect=[OSError('Source unavailable'), 'later-snapshot']):
            result = search_many(self.root, {'service': 'gmail', 'queries': [{'id': 'x', 'query': 'needle'}]})
        self.assertTrue(result['queries']['x']['matches'])
        self.assertFalse(result['queries']['x']['scan_complete'])
        self.assertTrue(result['queries']['x']['errors'])
        self.assertFalse(list((self.root / 'Evals/.cache/queries').glob('*.json')))


if __name__=='__main__':unittest.main(verbosity=2)

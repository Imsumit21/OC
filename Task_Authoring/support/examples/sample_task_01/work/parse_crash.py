import json,glob,re,collections,sys
rows=[]
for f in glob.glob('HarmonyGames_Gmail/Services_Data/gmail/threads/blake@*.json'):
    d=json.load(open(f))
    for m in d.get('messages',[]):
        s=m.get('subject') or ''
        if not s.startswith('Trending stability issues') and 'stability' not in s.lower(): continue
        b=(m.get("body") or "").replace("\r\n","\n")
        g=re.search(r'Firebase\n(.+?)•',b)
        game=g.group(1).strip() if g else '?'
        plat='Android' if 'Android' in s else ('iOS' if 'iOS' in s else '?')
        for mm in re.finditer(r'\n([^\n<]+)\n<https://console\.[^/]+/project/([^/]+)/crashlytics/app/([^/]+)/issues/([0-9a-f]{32})\?[^>]*>\n([^\n]+)\n([0-9.]+) \((\d+)\)(\d+) crash(?:es)?(\d+) users?',b):
            rows.append(dict(file=f.split('/')[-1],thread=d['id'],msgid=m.get('id'),date=m.get('date_parsed'),subject=s,game=game,plat=plat,method=mm.group(1).strip(),project=mm.group(2),app=mm.group(3),issue=mm.group(4),exc=mm.group(5).strip(),ver=mm.group(6),build=int(mm.group(7)),crashes=int(mm.group(8)),users=int(mm.group(9))))
json.dump(rows,open('Task_Authoring/support/examples/sample_task_01/work/crash_rows.json','w'),indent=0)
print(len(rows))
c=collections.Counter((r['game'],r['plat'],r['date'][:7]) for r in rows)
for k in sorted(c): print(k,c[k])

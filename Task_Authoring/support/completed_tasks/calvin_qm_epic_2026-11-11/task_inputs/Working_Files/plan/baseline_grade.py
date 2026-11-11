import json,re
T=json.load(open('Working_Files/solver/truth.json'))
C=json.load(open('Working_Files/run_forensics/rev3/baseline/calls.json'))
keys=list(T); norm=lambda s:re.sub(r'[^a-z0-9]','',str(s).lower())
rowno={k:i+1 for i,k in enumerate(keys)}
def match(title):
    n=norm(title)
    for k in keys:
        if norm(k)==n: return k
    for k in keys:
        if norm(k)[:25]==n[:25]: return k
    return None
for n in '123456':
    calls=C[n]; print('=== run',n)
    for c in calls:
        if c['name']=='gsheets_values_update':
            vals=c['input'].get('values'); 
            if isinstance(vals,str): vals=json.loads(vals)
            hdr=[str(x) for x in vals[0]]
            print(' sheet',c['input'].get('range'),hdr,len(vals)-1)
            if 'Report' in hdr[0] or 'Report' in hdr:
                si=[i for i,h in enumerate(hdr) if h.lower()=='status'][0]; ri=[i for i,h in enumerate(hdr) if 'review' in h.lower()][0]
                seen=set()
                for r in vals[1:]:
                    k=match(r[0])
                    if not k: print('  UNMATCHED',r[0]); continue
                    seen.add(k); t=T[k]
                    if norm(r[si])!=norm(t['Status']): print(f"  row{rowno[k]} STATUS {r[si]} (truth {t['Status']}) | {k[:50]}")
                    rv=norm(r[ri]) in('yes','y','true','x'); tv=norm(t['Review list'])=='yes'
                    if rv!=tv: print(f"  row{rowno[k]} REVIEW {r[ri]!r} (truth {t['Review list']})")
                for k in keys:
                    if k not in seen: print('  MISSING',rowno[k],k[:50])
            else:
                for r in vals[1:]: print('   ',r)
        if c['name']=='slack_send_message': print(' DM:',c['input'].get('channel') or c['input'].get('channel_id'),'|',str(c['input'].get('text'))[:600].replace('\n',' / '))
        if c['name']=='gslides_batch_update': print(' slide:',re.findall(r'"text": ?"([^"]{3,200})"',json.dumps(c['input']))[:12])

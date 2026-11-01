import json,sys,os,glob,re
WR=re.compile(r'(gmail_send|gmail_reply|gmail_create_draft|trello_add_comment|trello_create|linear_create_comment|linear_create_issue|gdrive|gsheets|sheets_|update_values|write|create_file|move|share|batch_update|append)',re.I)
d0=sys.argv[1]; out=sys.argv[2]
for f in sorted(glob.glob(d0+'/*.json')):
  n=re.search(r'run-(\d)',f).group(1)
  ev=json.load(open(f))
  res={}
  for e in ev:
    m=e.get('message') if isinstance(e,dict) else None
    if not m: continue
    c=m.get('content')
    if isinstance(c,list):
      for b in c:
        if b.get('type')=='tool_result':
          cc=b.get('content'); res[b.get('tool_use_id')]=json.dumps(cc)[:600]
  calls=[]
  for e in ev:
    m=e.get('message') if isinstance(e,dict) else None
    if not m or m.get('role')!='assistant': continue
    for b in m.get('content') or []:
      if isinstance(b,dict) and b.get('type')=='tool_use':
        nm=b['name']
        if WR.search(nm) and not re.search(r'read|get|search|list',nm.split('__')[-1],re.I):
          calls.append({'name':nm,'input':b['input'],'result':res.get(b['id'])})
  # final text
  last=''
  for e in ev:
    m=e.get('message') if isinstance(e,dict) else None
    if m and m.get('role')=='assistant':
      for b in m.get('content') or []:
        if isinstance(b,dict) and b.get('type')=='text': last=b['text']
  json.dump({'calls':calls,'final':last},open(f'{out}/run{n}.json','w'),indent=1)
  print(n,len(ev),[c['name'].split('__')[-1] for c in calls])

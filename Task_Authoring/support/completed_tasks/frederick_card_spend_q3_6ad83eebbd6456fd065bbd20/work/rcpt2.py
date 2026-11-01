import json,re,glob,os
from datetime import datetime,timezone
base='/home/sumit/Downloads/OC/OC/HarmonyGames_Gmail/Services_Data/gmail/threads'
R={};F={}
for p in glob.glob(base+'/*.json'):
    s=open(p,errors='ignore').read()
    if 'IDENTIFIER_3125' not in s: continue
    d=json.loads(s); ue=d.get('user_email','')
    for m in d.get('messages',[]):
        if 'receipt' not in (m.get('subject') or '').lower() or 'IDENTIFIER_3125' not in m.get('subject',''): continue
        dp=m.get('date_parsed','')
        try: dt=datetime.fromisoformat(dp).astimezone(timezone.utc)
        except: continue
        if not (datetime(2024,10,1,7,tzinfo=timezone.utc)<=dt<datetime(2025,10,1,7,tzinfo=timezone.utc)): continue
        b=m.get('body','')
        amt=re.search(r'Amount billed:\s*(\$[0-9,]+\.\d\d)',b); ref=re.search(r'Reference number:\s*(\S+)',b)
        k=(ref.group(1) if ref else None, amt.group(1) if amt else None)
        tgt=R if ue.startswith('robert') else F if ue.startswith('frederick') else None
        if tgt is not None: tgt.setdefault(k,[]).append((dt.isoformat()[:16],os.path.basename(p)))
sql=open('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/01_Universe_Inject.sql').read()
print('robert',len(R),'frederick',len(F))
tot=0
for k,v in sorted(R.items(),key=lambda x:x[1][0]):
    if k in F: continue
    insql=bool(k[0]) and k[0] in sql
    print(v[0][0],k,v[0][1],'IN_SQL' if insql else 'MISSING')
    if not insql and k[1]: tot+=float(k[1][1:].replace(',',''))
print('missing total',round(tot,2))

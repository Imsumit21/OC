import json,re,glob,os,sys
base='/home/sumit/Downloads/OC/OC/HarmonyGames_Gmail/Services_Data/gmail/threads'
def msgs(path):
    d=json.load(open(path))
    return d.get('user_email',''), d.get('messages',[])
R={};F={}
for p in glob.glob(base+'/*.json'):
    try: s=open(p,errors='ignore').read()
    except: continue
    if 'IDENTIFIER_3125' not in s: continue
    ue,ms=msgs(p)
    for m in ms:
        b=json.dumps(m); dt=m.get('date','')
        if 'IDENTIFIER_3125' not in b or not ('2024-10-01'<=dt<'2025-10-02'): continue
        if 'receipt' not in (m.get('subject') or '').lower(): continue
        amt=re.findall(r'\$[0-9,]+\.\d\d',b)
        ref=re.findall(r'Reference number[^A-Z0-9\[]{0,12}([A-Z0-9_\[\]-]{4,40})',b)
        key=(ref[0] if ref else None, amt[0] if amt else None)
        (R if ue.startswith('robert') else F if ue.startswith('frederick') else {}).setdefault(key,[]).append((dt,os.path.basename(p)))
sql=open('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/01_Universe_Inject.sql').read()
print('robert keys',len(R),'fred keys',len(F))
miss=[]
for k,v in sorted(R.items(),key=lambda x:x[1][0]):
    if k in F: continue
    insql = k[0] and k[0] in sql
    miss.append((v[0][0],k,v[0][1],insql))
for x in miss: print(x)

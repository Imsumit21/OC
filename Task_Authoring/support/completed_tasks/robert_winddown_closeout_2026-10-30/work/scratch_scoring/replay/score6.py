import pickle,json,re
res=pickle.load(open('graded.pkl','rb'))
RUB=json.load(open('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/Working_Files/09_Rubrics.draft_with_plan_ids.json'))
exec(open('../rubplan/draft.py').read().split("out = []")[0].replace("rows = json.load(open(sys.argv[1]))","rows=[]").replace("import json, sys","import json,sys"))
DONE={'ENG-2438','ENG-2439','ENG-2440','ENG-2459','ENG-2460','ENG-2461','ENG-2463'}; CANC={'ENG-2450','ENG-2454','ENG-2465','ENG-2466'}
def st(o,i):
    s=(o['states'].get(i) or '').lower()
    return {'completed':'done'}.get(s,s)
def has(t,*a): t=t.lower(); return any(re.search(x,t) for x in a)
tot={}
PASSN={}
for k,o in res.items():
    if k=='trajectory-run-1.json': continue
    got=0; W=0; fails=[]
    for r in RUB:
        P,t,w=r['P'],r['title'],r['weight']; W+=w; ok=True
        m=re.search(r'(ENG-\d+)',t); i=m.group(1) if m else None
        n=None
        for nm in sorted(ACC,key=len,reverse=True):
            if f"({nm})" in t or f" {nm} (ENG" in t or f" {nm} (added" in t: n=nm; break
        if ' the action ' in t: ok=o[('act',n)]
        elif ' the status ' in t: ok=o[('stat',n)]
        elif 'by-when date' in t: ok=o[('by',n)]
        elif 'as the owner' in t: ok=o[('own',n)] or k=='trajectory-run-3.json'
        elif 'a monthly cost of' in t: ok=o[('cost',n)]
        elif 'source of the Closed status' in t: ok=o[('stat',n)]
        elif P in ('P66','P67','P1','P2','P3'): ok= o.get(P,True) if P in ('P2','P3') else True
        elif 'shares' in t: ok=True
        elif t.startswith('The Agent sets Linear issue'):
            want='done' if i in DONE else 'canceled'; ok=st(o,i)==want
        elif P=='P82':
            ok = sum(1 for x in DONE|CANC if st(o,x) in ('done','canceled'))==11 and all(st(o,x) not in ('done','canceled') for x in o['states'] if x not in DONE|CANC)
        elif 'adds a new comment on Linear issue' in t:
            c=' '.join(o['comments'].get(i) or [])
            if 'confirmed closed' in t: ok = o[('stat',n)] if n else True
            elif 'Layer' in t: ok=o[('stat','Layer')]
            else: ok=True
        elif P=='P111': ok=len(o['comments'])>=28
        elif P in ('P112','P113','P114','P116'): ok=True
        elif P=='P115':
            s=o['slack'][-1].lower(); ok=bool(re.search(r'\*\*slack|\*slack|slack seats|2\. \*\*slack',s)) and not re.search(r'not a clash, just|worth a check, slack',s)
        PASSN.setdefault(P,0); PASSN[P]+= 1 if ok else 0
        if not ok: fails.append(P)
        got+= w if ok else 0
    tot[k]=got/W
    print(k, round(100*got/W,1), fails)
print('avg', round(100*sum(tot.values())/len(tot),1))

json.dump(PASSN,open('passn.json','w'))

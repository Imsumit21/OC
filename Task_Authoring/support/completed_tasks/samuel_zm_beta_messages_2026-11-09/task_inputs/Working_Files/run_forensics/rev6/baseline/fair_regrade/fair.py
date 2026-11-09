"""Fair per-item regrade of the rev6 baselines. Joins on the Ticket column, checks each item on its OWN ticket.
Advisory proxy only: the rubric + verifier remain the grading of record."""
import sys,json,re,collections,statistics,random
sys.path.insert(0,sys.argv[1]); sys.path.insert(0,'/home/sumit/Desktop/OC/Task_Authoring/tools')
from facts import *
import difficulty_stats as ds
RUNS=[f'run-{i}' for i in range(1,7)]
FA={l:facts(FILES[l]) for l in FILES}
S=json.load(open(f'{T}/Working_Files/01_Gradable_Surface.json'))
L7,L1,PR,LR,WK,FM,WC='DES-317','DES-316','DES-319','DES-315','DES-320','DES-318','DES-313'
def row(F,t): return F['rows'].get(t,{})
def call(F,t,v): return row(F,t).get('Call','').strip().lower()==v.lower()
def miss(F,t,rx): return bool(re.search(rx,row(F,t).get('Miss',''),re.I|re.S))
def cm(F,t,rx): return any(re.search(rx,b,re.I|re.S) for b in F['comments'].get(t,[]))
def st(F,t,s):
    u=F['upd'].get(t)
    if s=='unchanged': return u is None
    return bool(u) and str(u.get('state')).lower()==s.lower()
def un(F,t): u=F['upd'].get(t); return bool(u) and u.get('assignee') in(None,)
def aud(F,t,a): return re.sub(r'\W','',row(F,t).get('Aud','').lower())==re.sub(r'\W','',a.lower())
def newt(F,rx): return any(re.search(rx,(i.get('title','')+' '+i.get('description','')),re.I|re.S) for i in F['new'])
def titles(F,rx): return any(re.search(rx,i.get('title',''),re.I) for i in F['new'])
def note(F,rx): return bool(re.search(rx,F['note'],re.I|re.S))
def holdsec(F):
    m=re.search(r'(?is)(already (?:scheduled|schedules)[^\n]*hold.*)',F['note']); return m.group(1) if m else F['note']
def noteHold(F,rx,cut=r'(?i)\n\s*(?:\d[.)]\s*)?totals?\b|\n\s*\d[.)]\s*(?:the )?(?:calls|totals)'):
    h=re.split(cut,holdsec(F))[0]; return bool(re.search(rx,h,re.I))
def dm(F,rx): return bool(re.search(rx,F['dm'].replace('*',''),re.I))
def mail(F,addr): return any(addr in ' '.join(m.get('to') or []) for m in F['mails'])
def mailtxt(F,addr): return '\n'.join(str(m.get('body')) for m in F['mails'] if addr in ' '.join(m.get('to') or []))
def ladder(F):
    n=F['note']
    return all(re.search(rf'(?<!\d){d}(?!\d)',n) for d in (1,7,14,21,28)) and bool(re.search(r'(?i)day',n))
HOLD=r'\bhold\b'
FAIR={
'X1':lambda F:call(F,WK,'Hold'),'X2':lambda F:call(F,WK,'Hold') and miss(F,WK,r'wrong day|test 5|not tied|reset day'),
'X2b':lambda F:cm(F,WK,r'wrong day|test 5|not on .*reset|reset day'),'X1c':lambda F:st(F,WK,'Backlog'),
'X3':lambda F:'your squad is waiting' in row(F,L7).get('Head','').lower(),
'X4':lambda F:titles(F,r'Your Squad Is Waiting') or newt(F,r'Your Squad Is Waiting'),
'X16':lambda F:row(F,L7).get('Str','').strip().lower().startswith('yes'),
'X5':lambda F:call(F,FM,'Hold'),'X6':lambda F:miss(F,FM,r'permission|ask|reach'),
'X6b':lambda F:cm(F,FM,r'permission|our (own )?ask|reach'),'X6c':lambda F:st(F,FM,'Backlog'),
'X7':lambda F:call(F,PR,'Hold'),'X8':lambda F:call(F,PR,'Hold') and miss(F,PR,r'iphone|ios|both'),
'X8b':lambda F:cm(F,PR,HOLD) and cm(F,PR,r'timer|never showed|not seen|iphone|ios'),'X8c':lambda F:st(F,PR,'Backlog'),
'K1':lambda F:call(F,LR,'Hold'),'X21':lambda F:call(F,LR,'Hold') and miss(F,LR,r'iphone|ios|both|tick'),
'X21b':lambda F:cm(F,LR,HOLD) and cm(F,LR,r'0\.3\.49|tick|not seen'),'X21c':lambda F:st(F,LR,'Backlog'),
'X22':lambda F:noteHold(F,r'lives recharged'),
'X9':lambda F:row(F,WC).get('Ticket','').startswith('DES-313'),
'X10':lambda F:cm(F,WC,HOLD) and not titles(F,r'win\s*(&|and)\s*collect|collect\s*(&|and)\s*win'),
'X11':lambda F:False,'X12':lambda F:False,'X11b':lambda F:False,'X12b':lambda F:False,
'X13':lambda F:False,'X13b':lambda F:False,'X13c':lambda F:False,
'X15':lambda F:call(F,'DES-344','Drop'),'X15b':lambda F:miss(F,'DES-344',r'lapsed 7|weekly|cover'),
'X17':ladder,'X20':lambda F:noteHold(F,r'first mission'),
'X18':lambda F:st(F,'DES-321','Backlog'),'X19':lambda F:st(F,'DES-323','Backlog'),'X19b':lambda F:st(F,'DES-329','Backlog'),
'T1':lambda F:dm(F,r'\b(Go:? 2|2 Go)\b'),'T2':lambda F:dm(F,r'\b(Hold:? 28|28 Hold)\b'),'T3':lambda F:dm(F,r'\b(Drop:? 6|6 Drop)\b'),
'K2':lambda F:call(F,L1,'Go'),'K3':lambda F:call(F,'DES-327','Drop'),'K5':lambda F:call(F,'DES-324','Drop'),'K6':lambda F:call(F,'DES-322','Hold'),
'K9':lambda F:miss(F,'DES-335',r'server'),'K10':lambda F:'horde is growing' in row(F,L1).get('Head','').lower(),
'K11':lambda F:any(re.search(r'lapsed 1|horde',c,re.I) for c in F['checks']),'K12':lambda F:st(F,'DES-324','Canceled'),
'K13':lambda F:cm(F,'DES-321',HOLD),'K14':lambda F:aud(F,'DES-330','players past the arena unlock'),'K15':lambda F:aud(F,'DES-335','players in a race'),
'K16':lambda F:note(F,r'31[.](65|7|6).*9[.](28|3)'),'K17':lambda F:note(F,r'37[.](86|9).*10[.](68|7)'),
'K18':lambda F:mail(F,'robert@'),'K19':lambda F:mail(F,'douglas'),
'V1':lambda F:len(F['rows'])==36,'D1':lambda F:F['parents'].get(F['sheet'])==FOLDER,'D2':lambda F:F.get('dmch')=='D06L58XCVKK' and dm(F,r'\bGo\b'),
}
assert set(FAIR)==set(s['id'] for s in S['slots']),set(s['id'] for s in S['slots'])^set(FAIR)
def shapeA():
    return [dict(id=s['id'],weight=s['weight'],f=FAIR[s['id']]) for s in S['slots']]
ZOM=['Boss Arena attempts refilled','Daily gift about to reset','Teammate sent lives','Infinite lives ending']
TRAP={WK,L7,FM,PR,LR,WC,'DES-344'}
TESTRX={'not scheduled in the client':r"test 3|schedul",'needs a server send':r'test 2|server','cannot reach its players':r'test 4|reach|permission','fires on the wrong day':r'test 5|wrong day','not seen on both platforms':r'test 6|both|ios|iphone|tick'}
def per_call_rows():
    R=[]
    for k,v in ITEMS.items():
        t=v.get('Ticket')
        if t: R.append(dict(id=f'call:{t}',weight=5 if t in TRAP else 3,f=(lambda F,t=t,c=v['Call']:call(F,t,c))))
        else: R.append(dict(id=f'call:{k}',weight=5,f=lambda F:False))
    return R
def per_reason_rows():
    R=[]
    for k,v in ITEMS.items():
        t=v.get('Ticket'); m=v.get("What's missing")
        if not m: continue
        if t: R.append(dict(id=f'why:{t}',weight=5 if t in TRAP else 3,f=(lambda F,t=t,c=v['Call'],rx=TESTRX[m]:call(F,t,c) and miss(F,t,rx))))
        else: R.append(dict(id=f'why:{k}',weight=3,f=lambda F:False))
    return R
def per_aud_rows():
    R=[]
    for k,v in ITEMS.items():
        t=v.get('Ticket')
        R.append(dict(id=f'aud:{k}',weight=1,f=(lambda F,t=t,a=v['Audience']:aud(F,t,a)) if t else (lambda F:False)))
    return R
ASK={}
for k,v in ITEMS.items():
    for g in v.get('groups',[]):
        if g.startswith('asker_'): ASK.setdefault(g[6:],[]).append(k)
ADDR=dict(brian='brian.foster@',robert='robert@',oliver='oliver.brooks@',julia='julia.lawson@',owen='owen.baker@',calvin='calvin.price@',martin='martin.walsh@',douglas='douglas')
def per_mail_rows():
    R=[]
    for a,ks in ASK.items():
        for k in ks:
            t=ITEMS[k].get('Ticket'); c=ITEMS[k]['Call']
            def f(F,a=a,t=t,c=c):
                if not t: return False
                b=mailtxt(F,ADDR[a]); 
                return bool(re.search(rf'{t}\b[^\n]*\b{c}\b',b,re.I)) or bool(re.search(rf'\b{c}\b[^\n]*{t}\b',b,re.I))
            R.append(dict(id=f'mail:{a}:{k}',weight=3,f=f))
    return R
def other_rows():
    ids={'X3','X4','X16','K10','X2b','X6b','X8b','X21b','X1c','X6c','X8c','X21c','X18','X19','X19b','K12','K13','X9','X10','X13','X13b','X13c','X17','X20','X22','T1','T2','T3','K16','K17','K19','V1','D1','D2'}
    R=[dict(id=s['id'],weight=s['weight'],f=FAIR[s['id']]) for s in S['slots'] if s['id'] in ids]
    R.append(dict(id='note:plague',weight=5,f=lambda F:noteHold(F,r'plague race')))
    R.append(dict(id='note:leaderboard',weight=5,f=lambda F:noteHold(F,r'leaderboard')))
    R.append(dict(id='chk:lapsed7',weight=3,f=lambda F:any(re.search(r'lapsed 7',c,re.I) for c in F['checks'])))
    R.append(dict(id='chk:count2',weight=1,f=lambda F:len(F['checks'])==2))
    R.append(dict(id='new:gift',weight=3,f=lambda F:False))
    return R
def shapeB(): return per_call_rows()+[r for r in shapeA() if r['id'] not in{'X1','X5','X7','K1','K2','K3','K5','K6','X15','X11','X12','X11b','X12b'}]
def shapeC(): return per_call_rows()+per_reason_rows()+per_aud_rows()+per_mail_rows()+other_rows()
def grade(rows,labs=RUNS): return {l:{r['id']:bool(r['f'](FA[l])) for r in rows} for l in labs}
def score(rows,res): W=sum(r['weight'] for r in rows); return sum(r['weight'] for r in rows if res[r['id']])/W
def gates(rows,G):
    data=dict(spec_version='V3',difficulty_mode='medium',task_type='long-horizon',rubrics=[dict(id=r['id'],weight=r['weight'],valid=True) for r in rows],
      rollouts=[dict(id=l,status='completed',tool_calls=len(FA[l]['calls']),models=['claude-opus-5-5'],model_source='trajectory',results=G[l]) for l in G])
    return ds.compute(data)
if __name__=='__main__':
    for name,fn in (('A sealed 57-slot surface, fair',shapeA),('B per-message calls + sampled rest',shapeB),('C full per-target',shapeC)):
        rows=fn(); G=grade(rows); sc=[score(rows,G[l]) for l in RUNS]
        print(f"\n{name}: rows {len(rows)} weight {sum(r['weight'] for r in rows)}")
        print('  scores',[round(x*100,1) for x in sc],'mean',round(statistics.mean(sc)*100,1),'popSD',round(statistics.pstdev(sc),3),'sampleSD',round(statistics.stdev(sc),3))
        print('  precheck',round(score(rows,grade(rows,['precheck'])['precheck'])*100,1))
        d=gates(rows,G)
        try:
            v=d['views'] if 'views' in d else d
            print('  ',json.dumps(v)[:900])
        except Exception as e: print(e)

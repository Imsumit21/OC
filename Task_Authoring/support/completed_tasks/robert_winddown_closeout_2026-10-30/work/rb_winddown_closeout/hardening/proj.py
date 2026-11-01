"""Projection: per-write rubric model x 6 baseline runs x candidate hidden facts."""
import json,statistics as S,itertools
W='/home/sumit/Downloads/OC/OC/Task_Authoring-2/support/task_work/rb_winddown_closeout/'
T=json.load(open(W+'truth.json')); A=json.load(open(W+'accounts.json'))['accounts']
rows=[]  # (id, weight)
def r(i,w): rows.append((i,w))
for i in ('sheet','shareL','shareA'): r(i,1)
r('count28',5)
for a in ('add:ElevenLabs',): r(a,5)
for a in ('add:Meta','add:AppLovin','one:Intuit','off:iPostal','off:adjoe','off:Pond5','off:UnityAds'): r(a,3)
MULTI={'Gusto','Trello','BigQuery','dbt','GitHub','Metabase','Slack','Google Workspace','Linear','Figma'}
for x in T['rows']:
    a=x['account']
    r('act:'+a,5 if a in MULTI else 3)
    if x['action']=='Cancel': r('st:'+a,3)
    r('by:'+a,3)
for i in range(5): r(f'own:{i}',1)
r('own:vol',1)
for a in ('Singular','Carta','Linear','ElevenLabs','Meta Ads','Google Workspace','Unity','Docusign'): r('cost:'+a,3)
for i in ('tot1:sheet','tot2:sheet','tot1:reply','tot2:reply'): r(i,5)
for k in T['linear']['done']+T['linear']['canceled']: r('state:'+k,3)
for a in A: r('cmt:'+a['issue'],3)
r('guard:done',3); r('guard:canc',3)
r('thread',1); r('clash:slack',5); r('clash:google',5); r('clash:scope',3)
WT=dict(rows); TOT=sum(WT.values())
iss={x['account']:x['issue'] for x in T['rows']}
def flip(acc):  # a Cancel row that should be Closed (rule 5)
    k=iss.get(acc); f={'st:'+acc,'by:'+acc}
    if k and k.startswith('ENG'): f|={'state:'+k,'cmt:'+k,'guard:done'}
    return f
# observed failures on the CURRENT data (graded from the trajectories)
SAYWHERE={'st:Helpshift','st:Soundly','st:Zapier','st:Kapwing'}
base={1:flip('CodeRabbit')|{'clash:scope'},
      2:flip('CodeRabbit')|{'by:ElevenLabs'}|SAYWHERE,
      3:flip('CodeRabbit'),
      4:flip('CodeRabbit')|{'clash:scope','off:adjoe','count28'},
      5:flip('CodeRabbit')|{'off:iPostal','count28','tot1:sheet','tot1:reply','state:ENG-2466','cmt:ENG-2466','guard:canc'}|SAYWHERE,
      6:flip('CodeRabbit')|{'clash:scope'}}
EXTRA={}
def score(f):
    wt=dict(WT); wt.update(EXTRA); return 1-sum(wt.get(x,3) for x in f)/sum(wt.values())
def report(name,fails):
    sc=[score(fails[i]) for i in range(1,7)]
    print(f"{name:34} avg {S.mean(sc)*100:5.1f}%  sd {S.pstdev(sc):.3f}  runs "+' '.join(f'{x*100:4.1f}' for x in sc))
    return sc
print('rows',len(rows),'weight',TOT)
report('current data',base)
# candidate hidden facts: (rows they flip, runs predicted to MISS them)
SVB={'by:Intuit QuickBooks','by:Google Workspace','by:Slack','cmt:ENG-2460','cmt:ENG-2464','cmt:ENG-2465'}
C={'H1 Cursor Bugbot (GitHub PR)':(flip('Cursor'),{1,2,3,4,5,6}),
   'H2 Unity build-service bot (#builds)':(flip('Unity'),{2,3,4,5}),
   'H3 1Password app (#engineering-bots)':(flip('1Password'),{2,3,4,5}),
   'H4 AWS notice (Slack bot)':(flip('AWS'),{2,3,4,5}),
   'H5 AppLovin rep (#applovin_ shared)':(flip('AppLovin (UA)'),{2,3,4,5}),
   'H6 SVB card comment (Trello)':(SVB,{4,6}),
}
json.dump({'rows':rows,'base':{k:sorted(v) for k,v in base.items()},'cands':{k:[sorted(v[0]),sorted(v[1])] for k,v in C.items()}},open('model.json','w'),indent=1)
cum={i:set(base[i]) for i in base}
for name,(fl,miss) in C.items():
    for x in fl:
        if x not in WT: EXTRA[x]=3
    for i in miss: cum[i]|=fl
    report('+ '+name,cum)

import json,statistics as S
src=open('proj.py').read()
exec(src.split("print('rows'")[0])
exec('SVB=' + src.split('SVB=')[1].split('\n')[0])
TRIV=['ENG-2441','ENG-2442','ENG-2443','ENG-2444','ENG-2445','ENG-2446','ENG-2447','ENG-2450','ENG-2452','ENG-2453','ENG-2463','ENG-2472','ENG-2480','ENG-2481','ENG-2470','ENG-2471']
late=['Singular','AWS','Gusto','Layer','1Password','Meta Ads','Carta','Docusign','ElevenLabs']   # non-Closed Cancel rows left after H1/H2/H5
H7=set().union(*[{'by:'+a}|({'cmt:'+iss[a]} if iss.get(a,'').startswith('ENG') else set()) for a in late])|SVB
def run(name,cands):
    wt={k:v for k,v in WT.items() if not any(k.endswith(d) for d in TRIV)}
    fails={i:{x for x in base[i] if x in wt} for i in base}
    for fl,miss in cands.values():
        for x in fl: wt.setdefault(x,3)
        for i in miss: fails[i]|=fl
    tot=sum(wt.values()); sc=[1-sum(wt[x] for x in fails[i])/tot for i in range(1,7)]
    print(f"{name:52} rows {len(wt):3} avg {S.mean(sc)*100:5.1f}% sd {S.pstdev(sc):.3f} | "+' '.join(f'{x*100:4.1f}' for x in sc))
for lab,svbmiss,curmiss,apmiss in [('optimistic',{1,2,3,4,5,6},{2,3,4,5},{1,2,3,4,5,6}),('middle',{2,3,4,6},{2,3,4,5},{2,3,4,5,6}),('pessimistic',{4,6},{2,3,4,5},{2,3,4,5})]:
    c={'H1':(flip('Cursor'),curmiss),'H2':(flip('Unity'),{1,2,3,4,5,6}),'H5':(flip('AppLovin (UA)'),apmiss),'H67':(H7,svbmiss)}
    run(f'D-revised {lab}',c)

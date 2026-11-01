import json,statistics as S
src=open('proj.py').read()
exec(src.split("print('rows'")[0])
exec('SVB=' + src.split('SVB=')[1].split('\n')[0])
exec('C=' + src.split('C=')[1].split('json.dump')[0])
EXTRA={}
def run(name,drop,cands,show=True):
    wt={k:v for k,v in WT.items() if not any(k.endswith(d) for d in drop)}
    fails={i:{x for x in base[i] if x in wt} for i in base}
    for n,(fl,miss) in cands.items():
        for x in fl: wt.setdefault(x,3)
        for i in miss: fails[i]|=fl
    tot=sum(wt.values()); sc=[1-sum(wt[x] for x in fails[i])/tot for i in range(1,7)]
    if show: print(f"{name:44} rows {len(wt):3} avg {S.mean(sc)*100:5.1f}% sd {S.pstdev(sc):.3f} | "+' '.join(f'{x*100:4.1f}' for x in sc))
    return S.mean(sc)
# trivially-settled off-register issues (comment states the reason outright)
TRIV=['ENG-2441','ENG-2443','ENG-2444','ENG-2445','ENG-2446','ENG-2447','ENG-2450','ENG-2452','ENG-2453','ENG-2463','ENG-2472','ENG-2480','ENG-2481','ENG-2470','ENG-2471']
SVB=C['H6 SVB card comment (Trello)'][0]
# H7: SVB comment ALSO moves every non-Closed Cancel row charging after Feb 20 to Feb 19 (needs conventions rule 6 to cite SVB's deadline for Cancel rows)
late=['Singular','AWS','Gusto','Layer','Cursor','1Password','Meta Ads','AppLovin (UA)','Carta','Docusign','ElevenLabs']
H7=set().union(*[{'by:'+a}|({'cmt:'+iss[a]} if iss.get(a,'').startswith('ENG') else set()) for a in late])
full=dict(C)
run('A current scenario + H1-H6',[],full)
run('B drop 15 trivial issues + H1-H6',TRIV,full)
for miss in [{4,6},{2,4,6},{2,3,4,6}]:
    c=dict(full); c['H7 SVB covers Cancel rows']=(H7|SVB,miss); c.pop('H6 SVB card comment (Trello)')
    run(f'C A + H7 missed by runs {sorted(miss)}',[],c)
    run(f'D B + H7 missed by runs {sorted(miss)}',TRIV,c)

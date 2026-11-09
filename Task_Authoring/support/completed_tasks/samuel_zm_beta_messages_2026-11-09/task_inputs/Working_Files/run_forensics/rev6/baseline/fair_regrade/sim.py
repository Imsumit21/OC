import sys;sys.argv=['x',sys.argv[1]]
src=open(sys.argv[1]+'/fair.py').read().split("if __name__=='__main__':")[0]
exec(src)
import random
def tag(i):
    if i in('X3','X4') : return 'head'
    if i in('X7','X8','X8b','X8c','note:plague','call:DES-319','why:DES-319'): return 'plague'
    if i in('K1','X21','X21b','X21c','X22','call:DES-315','why:DES-315'): return 'lives'
    if i in('X1','X2','X2b','X1c','note:leaderboard','call:DES-320','why:DES-320'): return 'lead'
    if i in('X11','X12','X11b','X12b','X13','X13b','X13c','K19','V1','new:gift') or any(z in i for z in ZOM): return 'filt'
    return None
for name,fn in (('A',shapeA),('B',shapeB),('C',shapeC)):
    rows=fn(); G=grade(rows); d=gates(rows,G)
    v=d.get('views',d); 
    p=d['platform'] if 'platform' in d else v['platform']
    print('\n###',name,'keys',[k for k in p.keys()][:12])
    g=p.get('gates') or p
    for k in ('pass_at_1','avg_weighted_pass_rate','per_rollout_sd','failure_patterns','horizon','errored_runs','baseline_models'):
        x=g.get(k) if isinstance(g,dict) else None
        if x: print('  ',k,x.get('verdict'),'|',str(x.get('value'))[:120])
    print('   patterns:',p.get('patterns') or p.get('failure_patterns_detail') or '')
    for l in RUNS:
        f=[i for i,ok in G[l].items() if not ok]
        print('   ',l,'fails',len(f),'non-FILT:',[i for i in f if tag(i)!='filt'][:40])
    # invalid-FILT sensitivity
    keep=[r for r in rows if tag(r['id'])!='filt' and r['id'] not in('T2',)]
    G2=grade(keep); sc=[score(keep,G2[l]) for l in RUNS]
    print('   IF ZOM rows ruled invalid: mean',round(statistics.mean(sc)*100,1),'SD',round(statistics.pstdev(sc),3),[round(x*100,1) for x in sc], 'fullpass',sum(1 for l in RUNS if all(G2[l].values())))
# simulation of a re-run
def simulate(rows,rates,n=20000,seed=7,filt_mode='all'):
    rng=random.Random(seed); W=sum(r['weight'] for r in rows); tags=[(r['id'],r['weight'],tag(r['id'])) for r in rows]
    ok=sd_ok=av_ok=av80=all_ok=0; means=[];sds=[]
    for _ in range(n):
        sc=[];sigs=[]
        for k in range(6):
            miss={t for t,p in rates.items() if rng.random()>p}
            fails=set()
            for i,w,t in tags:
                if t and t in miss: fails.add(i)
            if miss&{'plague','lives','lead'}:
                fails|={i for i,w,t in tags if i=='T1'}
            if miss&{'plague','lives','lead','filt'}: fails|={i for i,w,t in tags if i=='T2'}
            sc.append(1-sum(w for i,w,t in tags if i in fails)/W); sigs.append(fails)
        m=statistics.mean(sc); s=statistics.pstdev(sc); means.append(m);sds.append(s)
        # patterns, single linkage on <=1 row differences
        par=list(range(6))
        def fd(x):
            while par[x]!=x: x=par[x]
            return x
        for a in range(6):
            for b in range(a+1,6):
                if len(sigs[a]^sigs[b])<=1: par[fd(a)]=fd(b)
        cnt=collections.Counter(fd(x) for x in range(6) if sigs[x])
        nf=sum(cnt.values()); pat=len(cnt)>=2 and (max(cnt.values())/nf<=0.5 if nf else False)
        fp=sum(1 for x in sigs if not x)
        a=m<0.85; b=0.1<=s<=0.3
        av_ok+=a; sd_ok+=b; av80+=(m<0.80); ok+=(a and pat and fp<5); all_ok+=(a and b and pat and fp<5)
    q=sorted(sds); qm=sorted(means)
    return dict(P_avg85=round(av_ok/n,3),P_avg80=round(av80/n,3),P_sd=round(sd_ok/n,3),P_v3=round(ok/n,3),P_all=round(all_ok/n,3),mean=round(statistics.mean(means)*100,1),sd_med=round(q[n//2],3),sd90=round(q[int(n*.9)],3))
obs=dict(head=2/7,plague=5/7,lives=6/7,lead=6/7,filt=0.0)
print('\n=== re-run on unchanged SQL (observed catch rates, 7 runs; FILT 0) and Laplace FILT 1/9')
for name,fn in (('A',shapeA),('B',shapeB),('C',shapeC)):
    rows=fn()
    print(name,'obs   ',simulate(rows,obs))
    print(name,'filt.11',simulate(rows,{**obs,'filt':1/9}))
print('\n=== what-if rev7: FILT catch 50% as a block')
for name,fn in (('A',shapeA),('B',shapeB),('C',shapeC)):
    rows=fn(); print(name,simulate(rows,{**obs,'filt':0.5}))
print('\n=== what-if rev7: FILT catch 30%, headline 50%')
for name,fn in (('A',shapeA),('B',shapeB),('C',shapeC)):
    rows=fn(); print(name,simulate(rows,{**obs,'filt':0.3,'head':0.5}))

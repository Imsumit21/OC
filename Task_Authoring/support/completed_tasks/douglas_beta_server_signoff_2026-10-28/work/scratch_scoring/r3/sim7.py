import itertools,statistics as st,sys,collections,random
sys.path.insert(0,'/home/sumit/Downloads/OC/OC/Task_Authoring-2/tools')
import difficulty_stats as ds
R=lambda a,b:set(range(a,b+1))
B={'B0':[{},{},{},{'T':1},{'T':1},{'C':1},{'T':1,'C':1}],
   'B1':[{'T':1,'P':R(37,48)},{'T':1,'P':R(38,41)},{},{'T':1},{'T':1},{'T':1,'C':1}],
   'B2':[{'T':1,'P':{54}},{},{'P':R(37,41)},{'P':R(37,42)},{},{},{'T':1,'C':1}]}
POOL=[h for runs in B.values() for h in runs]
def found(h,f):
    k,a=f
    return (k in h) if k in('T','C') else a in h.get('P',set())
Y0=['459','509','499','531','444','510']; N0=['336','392','503','518','550','435','557','256']
def rubric(D,h):
    # D: ticket -> (habit,kind) kind in flip (Y->N), keepN (truth N, looks Y), excl (truth: off register; looks in scope, N0 or Y0 or extra)
    r=[];allok=True
    for t in Y0+N0+['487','537','547','553']+[k for k in D if k.startswith('X')]:
        if t in D:
            hab,kind=D[t]; x=found(h,hab); allok&=x
            if kind=='flip' or kind=='keepN': r+=[('st'+t,5,x),('dl'+t,3,x),('mv'+t,1,x),('cm'+t,3,x)]
            elif kind=='incY': r+=[('st'+t,5,x)]
            elif kind=='incN': r+=[('st'+t,5,x),('dl'+t,3,x),('mv'+t,1,x),('cm'+t,3,x)]
            elif kind=='excl':
                r+=[('ex'+t,3,x)]
                if t in N0: r+=[('nomv'+t,3,x)]
        elif t in Y0: r.append(('st'+t,3,True))
        elif t in N0: r+=[('st'+t,3,True),('dl'+t,1,True),('mv'+t,1,True),('cm'+t,1,True)]
    r+=[('dmcount',3,allok),('folder',3,True),('share',3,True),('leo',1,True),('dm',1,True),('cols',1,True)]
    return r
def gates(D,s):
    rows=[rubric(D,h) for h in s]
    data={'task_type':'long-horizon','rubrics':[{'id':n,'weight':w,'valid':True} for n,w,_ in rows[0]],
          'rollouts':[{'id':f'run-{i+1}','status':'completed','tool_calls':200,'results':{n:p for n,_,p in r}} for i,r in enumerate(rows)]}
    sc=[sum(w for _,w,p in r if p)/sum(w for _,w,_ in r) for r in rows]
    return ds.compute(data)['gates'],sc
def evaluate(name,D,n=3000):
    random.seed(11)
    hist=[];ok=0
    for b,runs in B.items():
        for s in ([runs] if len(runs)==6 else [list(c) for c in itertools.combinations(runs,6)]):
            g,sc=gates(D,s); bad=[k for k,x in g.items() if not x['verdict'].startswith(('PASS','NON-FAIL')) and k!='horizon']
            hist.append((b,st.mean(sc),st.pstdev(sc),bad))
    hok=sum(1 for x in hist if not x[3])
    bo=0;fails=collections.Counter();avgs=[];sds=[]
    for _ in range(n):
        g,sc=gates(D,random.choices(POOL,k=6)); avgs.append(st.mean(sc)); sds.append(st.pstdev(sc))
        bad=[k for k,x in g.items() if not x['verdict'].startswith(('PASS','NON-FAIL')) and k!='horizon']
        bo+=not bad
        for k in bad: fails[k]+=1
    avgs.sort();sds.sort()
    print('%-44s hist %2d/15 | boot P=%.0f%% avg p10-p90 %.2f-%.2f sd p10 %.3f | fails %s'%(name,hok,100*bo/n,avgs[n//10],avgs[9*n//10],sds[n//10],{k:'%.0f%%'%(100*v/n) for k,v in fails.items()}))
T=('T',0);C=('C',0);P=lambda n:('P',n)
base={'547':(T,'excl'),'553':(T,'excl'),'487':(C,'keepN')}
evaluate('CUR (+537@46)',{**base,'537':(P(46),'keepN')})
evaluate('G1 T531,444 P336x@40 509@39 +537',{**base,'531':(T,'flip'),'444':(T,'flip'),'336':(P(40),'excl'),'509':(P(39),'flip'),'537':(P(46),'keepN')})
evaluate('G2 T531 P336x 509 459 +537',{**base,'531':(T,'flip'),'336':(P(40),'excl'),'509':(P(39),'flip'),'459':(P(38),'flip'),'537':(P(46),'keepN')})
evaluate('G3 T531,444 P336x 509 459 +537',{**base,'531':(T,'flip'),'444':(T,'flip'),'336':(P(40),'excl'),'509':(P(39),'flip'),'459':(P(38),'flip'),'537':(P(46),'keepN')})
evaluate('G4 T531,444 C499 P336x 509 +537',{**base,'531':(T,'flip'),'444':(T,'flip'),'499':(C,'flip'),'336':(P(40),'excl'),'509':(P(39),'flip'),'537':(P(46),'keepN')})
evaluate('G5 T531,444 C435x P336x 509 +537',{**base,'531':(T,'flip'),'444':(T,'flip'),'435':(C,'excl'),'336':(P(40),'excl'),'509':(P(39),'flip'),'537':(P(46),'keepN')})
evaluate('G6 T531 C435x P336x 509 +537',{**base,'531':(T,'flip'),'435':(C,'excl'),'336':(P(40),'excl'),'509':(P(39),'flip'),'537':(P(46),'keepN')})
evaluate('G7 T531,444 P336x 509 (537 dropped)',{**base,'531':(T,'flip'),'444':(T,'flip'),'336':(P(40),'excl'),'509':(P(39),'flip')})

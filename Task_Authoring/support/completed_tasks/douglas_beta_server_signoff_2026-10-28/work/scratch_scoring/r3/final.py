exec(open('/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/r3/sim7.py').read().split("T=('T',0)")[0])
T=('T',0);C=('C',0);P=lambda n:('P',n)
b={'547':(T,'excl'),'553':(T,'excl'),'487':(C,'keepN'),'537':(P(46),'keepN')}
L2={**b,'444':(T,'flip'),'X436':(T,'incN'),'531':(T,'flip'),'509':(P(39),'flip'),'459':(P(38),'flip')}
CUR={**b}
names={'B0':['pre','r1','r2','r3','r4','r5','r6'],'B1':['r1','r2','r3','r4','r5','r6'],'B2':['solo','r1','r2','r3','r4','r5','r6']}
for nm,D in (('CURRENT',CUR),('ROUND3',L2)):
    print('==',nm, 'rubric rows',len(rubric(D,{})),'total weight',sum(w for _,w,_ in rubric(D,{})))
    for bk,runs in B.items():
        for idx,s_ in enumerate([runs] if len(runs)==6 else [list(c) for c in itertools.combinations(runs,6)]):
            g,sc=gates(D,s_)
            print('  %s s%d avg %.3f sd %.3f pat %s | %s'%(bk,idx,st.mean(sc),st.pstdev(sc),g['failure_patterns']['value'][:40],' '.join('%.2f'%x for x in sc)))
evaluate('ROUND3',L2,n=5000)
evaluate('CURRENT',CUR,n=5000)
# per-run scores by habit vector
print('per-habit scores ROUND3:')
for h in [{},{'T':1},{'C':1},{'P':R(37,41)},{'T':1,'C':1},{'T':1,'P':R(37,48)},{'T':1,'P':R(38,41)}]:
    r=rubric(L2,h); print('  ',h if 'P' not in h else {**h,'P':'%d-%d'%(min(h['P']),max(h['P']))},'%.3f'%(sum(w for _,w,p in r if p)/sum(w for _,w,_ in r)))

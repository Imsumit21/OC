import itertools,statistics as st
# habit vectors: T thread, C conf comments, P = set of PRs whose inline comments were read
R=lambda a,b:set(range(a,b+1))
B={'B0':[{},{},{},{'T':1},{'T':1},{'C':1},{'T':1,'C':1}],
   'B1':[{'T':1,'P':R(37,48)},{'T':1,'P':R(38,41)},{},{'T':1},{'T':1},{'T':1,'C':1}],
   'B2':[{'T':1,'P':{54}},{},{'P':R(37,41)},{'P':R(37,42)},{},{},{'T':1,'C':1}]}
def norm(h):
    h=dict(h) if isinstance(h,dict) else {}
    return h
def found(h,fact):
    kind,arg=fact
    if kind=='T': return 'T' in h
    if kind=='C': return 'C' in h
    if kind=='P': return arg in h.get('P',set())
def rows(design,h):
    # design: dict name->(habit) ; A = exclusion fact (T)
    f={k:found(h,v) for k,v in design.items()}
    r=[]
    r.append(('rowset',5,f.get('A',True)))
    if 'A' in f: r.append(('excl',3,f['A']))
    r.append(('count',5,all(f.values())))
    flips=[k for k in f if k!='A']
    r.append(('list',3,all(f[k] for k in flips)))
    for k in flips: r+= [(k+'_N',3,f[k]),(k+'_todo',3,f[k])]
    r+= [('other_status',5,True),('other_todo',3,True),('folder',3,True),('share',3,True),('dmdest',1,True)]
    return r
def score(r): return sum(w for _,w,p in r if p)/sum(w for _,w,_ in r)
def patterns(fails):
    n=len(fails); parent=list(range(n))
    def F(i):
        while parent[i]!=i: i=parent[i]
        return i
    for i in range(n):
        for j in range(i+1,n):
            if len(fails[i]^fails[j])<=1: parent[F(i)]=F(j)
    from collections import Counter
    c=Counter(F(i) for i in range(n) if fails[i])
    return len(c),max(c.values())/n if c else 0
designs={
 'cur  A,B,537@46':{'A':('T',0),'B':('C',0),'D':('P',46)},
 'D_a  A,B,C@39,537@46':{'A':('T',0),'B':('C',0),'C':('P',39),'D':('P',46)},
 'D_b  A,B,C@39':{'A':('T',0),'B':('C',0),'C':('P',39)},
}
for name,ds in designs.items():
    print('##',name)
    for b,runs in B.items():
        samples=[runs] if len(runs)==6 else [list(c) for c in itertools.combinations(runs,6)]
        out=[]
        for s in samples:
            rs=[rows(ds,norm(h)) for h in s]; sc=[score(r) for r in rs]
            fails=[frozenset(n for n,_,p in r if not p) for r in rs]
            np_,big=patterns(fails)
            out.append((st.mean(sc),st.pstdev(sc),np_,big,[round(x,2) for x in sc]))
        for o in out: print('  ',b,'avg %.2f sd %.3f patterns %d largest %.0f%%'%o[:4],o[4])

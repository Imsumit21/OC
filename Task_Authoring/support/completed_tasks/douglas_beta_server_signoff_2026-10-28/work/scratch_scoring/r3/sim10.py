exec(open('/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/r3/sim7.py').read().split("T=('T',0)")[0])
T=('T',0);C=('C',0);P=lambda n:('P',n)
b={'547':(T,'excl'),'553':(T,'excl'),'487':(C,'keepN'),'537':(P(46),'keepN')}
J1={**b,'531':(T,'flip'),'444':(T,'flip'),'510':(T,'flip'),'509':(P(39),'flip'),'459':(P(38),'flip')}
evaluate('J1 T531,444,510 P509,459',J1)
evaluate('J2 T531,444,510 P509',{**b,'531':(T,'flip'),'444':(T,'flip'),'510':(T,'flip'),'509':(P(39),'flip')})
evaluate('J3 T531,444 P509,459',{**b,'531':(T,'flip'),'444':(T,'flip'),'509':(P(39),'flip'),'459':(P(38),'flip')})
# sensitivity: thread habit rate shifts. Flip T for some runs
import copy
def shifted(pool_mod,name,D):
    global POOL
    old=POOL; POOL=pool_mod; evaluate(name,D); POOL=old
allT=[dict(h,T=1) for h in POOL]
noT=[{k:v for k,v in h.items() if k!='T'} for h in POOL]
mixT=[ (dict(h,T=1) if i%2 else {k:v for k,v in h.items() if k!='T'}) for i,h in enumerate(POOL)]
shifted(allT,'J1 if every run reads thread',J1)
shifted(noT,'J1 if no run reads thread',J1)
noP=[{k:v for k,v in h.items() if k!='P'} for h in POOL]
shifted(noP,'J1 if no run reads inline comments',J1)
noC=[{k:v for k,v in h.items() if k!='C'} for h in POOL]
shifted(noC,'J1 if no run reads conf comments',J1)
print('--- P-rate sensitivity (inline comments on #38/#39 read by a share of runs, independent of other habits)')
import random as _r
for share in (0.3,0.5,0.7):
    rr=_r.Random(5); mod=[]
    for h in POOL:
        h2={k:v for k,v in h.items() if k!='P'}
        if rr.random()<share: h2['P']=R(37,48)
        mod.append(h2)
    shifted(mod,'J1 P share %.1f'%share,J1)
    shifted(mod,'J2 P share %.1f'%share,{**b,'531':(T,'flip'),'444':(T,'flip'),'510':(T,'flip'),'509':(P(39),'flip')})

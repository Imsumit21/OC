exec(open('/tmp/claude-1000/-home-sumit-Downloads-OC-OC/64ffea75-2ed7-4766-a065-99d4d43b34de/scratchpad/r3/sim7.py').read().split("T=('T',0)")[0])
T=('T',0);C=('C',0);P=lambda n:('P',n)
b={'547':(T,'excl'),'553':(T,'excl'),'487':(C,'keepN'),'537':(P(46),'keepN')}
evaluate('J1 T531,444,510 P509,459',{**b,'531':(T,'flip'),'444':(T,'flip'),'510':(T,'flip'),'509':(P(39),'flip'),'459':(P(38),'flip')})
evaluate('K1 T531,444,+X(Y) P509,459',{**b,'531':(T,'flip'),'444':(T,'flip'),'X1':(T,'incY'),'509':(P(39),'flip'),'459':(P(38),'flip')})
evaluate('K2 T531,444,+X(N) P509,459',{**b,'531':(T,'flip'),'444':(T,'flip'),'X1':(T,'incN'),'509':(P(39),'flip'),'459':(P(38),'flip')})
evaluate('K3 T531,444,+X(N) P509',{**b,'531':(T,'flip'),'444':(T,'flip'),'X1':(T,'incN'),'509':(P(39),'flip')})
evaluate('K4 T531,+X(N) P509,459',{**b,'531':(T,'flip'),'X1':(T,'incN'),'509':(P(39),'flip'),'459':(P(38),'flip')})
evaluate('K5 T531,444,+X1(N),+X2(Y) P509',{**b,'531':(T,'flip'),'444':(T,'flip'),'X1':(T,'incN'),'X2':(T,'incY'),'509':(P(39),'flip')})

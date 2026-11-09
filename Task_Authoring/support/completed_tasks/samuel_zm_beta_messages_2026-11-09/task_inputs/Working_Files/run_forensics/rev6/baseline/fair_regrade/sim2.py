import sys;sys.argv=['x',sys.argv[1]]
s=open(sys.argv[1]+'/sim.py').read()
exec(s.split("for name,fn in (('A',shapeA),('B',shapeB),('C',shapeC)):\n    rows=fn(); G=grade(rows); d=gates")[0])
exec('def simulate'+s.split('def simulate')[1].split("obs=dict(")[0])
calls={l:None for l in RUNS}
print('tools',[t for t in sorted(__import__('json').dumps(0))][:0])
scen={'all four at 50%, ZOM 0':dict(head=.5,plague=.5,lives=.5,lead=.5,filt=0.0),
      'all four at 50%, ZOM 25%':dict(head=.5,plague=.5,lives=.5,lead=.5,filt=.25),
      'all four at 40%, ZOM 0':dict(head=.4,plague=.4,lives=.4,lead=.4,filt=0.0)}
for k,v in scen.items():
    for name,fn in (('A',shapeA),('B',shapeB),('C',shapeC)):
        print(k,name,simulate(fn(),v,n=8000))

import json,glob,collections,re,sys
def walk(o,acc):
    if isinstance(o,dict):
        if o.get('type')=='tool_use' and o.get('name'): acc.append((o['name'],o.get('input',{})))
        for v in o.values(): walk(v,acc)
    elif isinstance(o,list):
        for v in o: walk(v,acc)
for d in sys.argv[1:]:
    fs=sorted(glob.glob(d+'/*.json'))
    print('==',d.split('completed_tasks/')[-1],len(fs))
    agg=collections.Counter(); runs=[]
    for f in fs:
        o=json.load(open(f)); acc=[]; walk(o,acc)
        c=collections.Counter(re.sub(r'^mcp__[^_]*__','',a) for a,_ in acc)
        runs.append((f,c,acc))
        agg.update(set(c))
    print(' total tool_use per run',[sum(v for n,v in c.items() if not re.match(r'(Bash|Read|Write|Edit|Task|Agent|Grep|Glob|TodoWrite)',n)) for _,c,_ in runs])
    for n,k in agg.most_common():
        print('   %-45s runs %d/%d calls %s'%(n,k,len(runs),[c.get(n,0) for _,c,_ in runs]))

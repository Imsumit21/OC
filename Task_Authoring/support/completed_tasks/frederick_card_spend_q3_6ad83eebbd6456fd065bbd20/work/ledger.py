import json,sys
ev=json.load(open(sys.argv[1]))
res={}
calls=[]
for i,e in enumerate(ev):
    m=e.get('message') or {}
    c=m.get('content')
    if not isinstance(c,list): continue
    for b in c:
        if b.get('type')=='tool_use': calls.append((i,b['id'],b['name'],b.get('input'),e.get('parent_tool_use_id')))
        if b.get('type')=='tool_result':
            cc=b.get('content'); 
            if isinstance(cc,list): cc=' '.join(x.get('text','') for x in cc if isinstance(x,dict))
            res[b['tool_use_id']]=(i,str(cc))
for i,tid,n,inp,par in calls:
    r=res.get(tid,(None,''))
    print(f"[{i}]{'(sub)' if par else ''} {n.replace('mcp__hg__','')} {json.dumps(inp)[:260]}\n    -> [{r[0]}] {r[1][:230]!r}")

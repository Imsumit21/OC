import json,glob,collections,sys,re
W=re.compile(r'(send|create|update|add|move|reply|delete|batch|append|copy|post|comment|check_item|insert|set)',re.I)
for f in sorted(glob.glob(sys.argv[1]+'/*.json')):
    d=json.load(open(f))
    c=collections.Counter(); writes=[]
    for e in d:
        if e.get('type')=='assistant':
            for b in e['message'].get('content',[]):
                if b.get('type')=='tool_use' and b['name'].startswith('mcp__hg__'):
                    n=b['name'][9:]; c[n]+=1
                    if W.search(n) and not n.startswith(('gmail_search','snowflake')) and 'list' not in n and 'get' not in n:
                        writes.append((n,json.dumps(b['input'])[:300]))
    res=[e for e in d if e.get('type')=='result']
    print('=====',f,'calls',sum(c.values()))
    print(dict(c.most_common(12)))
    for w in writes: print('  W',w[0],w[1])
    if res: print('  RESULT:',str(res[-1].get('result'))[:1500])

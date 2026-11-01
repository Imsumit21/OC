import json,sys,re
for f in sys.argv[1:]:
    ev=json.load(open(f)); print('=====',f, len(ev), 'last type', ev[-1].get('type'), ev[-1].get('subtype'), ev[-1].get('is_error'))
    gh=[]; 
    for i,e in enumerate(ev):
        if e.get('type')!='assistant': continue
        for c in e['message'].get('content',[]):
            if c.get('type')!='tool_use': continue
            nm=c['name']; a=json.dumps(c.get('input',{}))
            if 'github' in nm.lower(): gh.append((i,nm.split('__')[-1],a[:120]))
            if ('2459' in a) and ('linear' in nm.lower()):
                print(f'  ev{i} {nm.split("__")[-1]} {a[:300]}')
            if ('gsheets' in nm.lower() or 'sheet' in nm.lower()) and 'CodeRabbit' in a:
                m=re.search(r'\[\\?"CodeRabbit[^\]]*\]',a); print(f'  ev{i} {nm.split("__")[-1]} CR row: {m.group(0)[:300] if m else a[a.find("CodeRabbit")-10:a.find("CodeRabbit")+250]}')
            if 'slack' in nm.lower() and 'post' in nm.lower() and 'coderabbit' in a.lower():
                k=a.lower().find('coderabbit'); print(f'  ev{i} {nm.split("__")[-1]} reply: ...{a[k-100:k+150]}')
    print('  github calls:',len(gh)); 
    for g in gh[:12]: print('   ',g)
    cr=[i for i,e in enumerate(ev) if e.get('type')=='user' and 'pull request was not reviewed' in json.dumps(e)]
    print('  bot notice seen in tool results at events:',cr[:5])

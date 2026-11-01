import json,sys,re,glob
YES={'499','510'}
NO={'336','392','503','518','550','435','557','256','487','537','444','531','459','509','436'}
EXCL={'547','553'}
for f in sorted(glob.glob('*.json')):
    d=json.load(open(f)); calls=[]
    for e in d:
        if e.get('type')=='assistant':
            for c in e['message'].get('content',[]):
                if c.get('type')=='tool_use': calls.append((c['name'].replace('mcp__hg__',''),c['input']))
    n=[c[0] for c in calls]
    hab=dict(T='gmail_get_thread' in n, C=any('confluence' in x and 'comment' in x for x in n),
             P=sorted(str(i.get('pull_number',i.get('pullNumber'))) for x,i in calls if x=='github_get_pull_request_comments'),
             agent=n.count('Agent'))
    moved=[];cm=[]
    for x,i in calls:
        s=json.dumps(i)
        if x=='linear_update_issue': moved+=re.findall(r'ZOM-(\d+)',s)
        if x=='linear_create_comment': cm+=re.findall(r'ZOM-(\d+)',s)
    reg=' '.join(json.dumps(i) for x,i in calls if x in('gsheets_values_update','gdrive_create_file','gsheets_create_spreadsheet','gsheets_values_batch_update'))
    regk=set(re.findall(r'ZOM-(\d+)',reg))
    dm=' '.join(json.dumps(i) for x,i in calls if x=='slack_send_message')
    print('==',f,len(calls),hab)
    print('  moved',sorted(set(moved)),'missingN',sorted(NO-set(moved)),'wrongmove',sorted(set(moved)-NO))
    print('  reg keys',len(regk),'missing',sorted((NO|YES)-regk),'extra',sorted(regk-NO-YES))
    print('  DM',dm[:600])

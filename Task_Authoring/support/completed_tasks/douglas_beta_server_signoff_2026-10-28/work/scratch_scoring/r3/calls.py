import json,sys,re,os,glob
def from_traj(f):
    d=json.load(open(f)); out=[]
    for e in d:
        if e.get('type')=='assistant':
            for c in e['message'].get('content',[]):
                if c.get('type')=='tool_use': out.append((c['name'].replace('mcp__hg__',''),c['input']))
    return out
def from_ledger(f):
    out=[]
    for l in open(f):
        m=re.match(r'#\d+ ev\d+ (\S+) (.*)$',l.rstrip())
        if m:
            try: i=json.loads(m.group(2))
            except Exception: i={'_raw':m.group(2)}
            out.append((m.group(1),i))
    return out
runs={}
for k in ['pre','r1','r2','r3','r4','r5','r6']: runs['B0-'+k]=from_ledger(f'{sys.argv[1]}/ledgers/{k}.txt')
for f in ['/home/sumit/Downloads/trajectory-run-1 (2).json','/home/sumit/Downloads/trajectory-run-1 (3).json']: runs['B1?-'+os.path.basename(f)[-8:-5]]=from_traj(f)
runs['B2-solo']=from_traj('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/Run1_trajectory.json')
for i,f in enumerate(sorted(glob.glob('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/07_Baseline_Trajectories/*.json')),1): runs[f'B2-r{i}']=from_traj(f)
json.dump(runs,open(sys.argv[1]+'/r3/allcalls.json','w'))
def arg(i,*ks):
    for k in ks:
        if k in i: return str(i[k])
    return json.dumps(i)[:40]
for r,cs in runs.items():
    feat={}
    n=[x[0] for x in cs]
    feat['N']=len(cs)
    feat['thread']=sum(1 for x in n if x=='gmail_get_thread')
    feat['gmsg']=sum(1 for x in n if x=='gmail_get_message')
    feat['gsearch']=[arg(i,'query') for x,i in cs if x=='gmail_search_messages']
    feat['conf_cm']=sum(1 for x in n if 'confluence' in x and 'comment' in x)
    feat['conf']=[x for x in n if x.startswith('confluence')]
    feat['prc']=[arg(i,'pull_number','pullNumber') for x,i in cs if x=='github_get_pull_request_comments']
    feat['prb']=[arg(i,'pull_number','pullNumber') for x,i in cs if x=='github_get_pull_request']
    feat['lgi']=[arg(i,'id','issueId') for x,i in cs if x=='linear_get_issue']
    feat['trello']=[x for x in n if x.startswith('trello')]
    feat['slack']=[x+':'+arg(i,'channel_id','query')[:20] for x,i in cs if x.startswith('slack')]
    feat['drive']=[x+':'+arg(i,'range','fileId','query','file_id')[:25] for x,i in cs if x.startswith(('gdrive','gsheets','gdocs'))]
    feat['gcal']=[x+':'+arg(i,'query','event_id')[:25] for x,i in cs if x.startswith('gcal')]
    feat['other']=sorted(set(x for x in n if x.startswith('github') and x not in('github_get_issue_comments','github_get_pull_request_reviews','github_get_pull_request_comments','github_get_pull_request')))
    print('=====',r); 
    for k,v in feat.items(): print('  ',k,v)

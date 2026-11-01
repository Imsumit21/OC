import json,sys,glob,os
runs={}
for f in sorted(glob.glob('/home/sumit/Downloads/trajectory-run-*.json')):
    d=json.load(open(f))
    R={'sheet':[], 'states':{}, 'comments':{}, 'shares':[], 'slack':[], 'created_issues':[]}
    for e in d:
        if e.get('type')!='assistant': continue
        for b in e['message'].get('content',[]):
            if b.get('type')!='tool_use': continue
            n=b['name'].split('__')[-1]; i=b['input']
            if n=='gsheets_values_update': R['sheet'].append((i.get('range'),i.get('values')))
            elif n=='linear_update_issue': R['states'][i.get('id')]=i.get('state')
            elif n=='linear_create_comment': R['comments'].setdefault(i.get('issueId') or i.get('issue_id') or i.get('id'),[]).append(i.get('body'))
            elif n=='gdrive_share_file': R['shares'].append((i.get('emailAddress'),i.get('role')))
            elif n=='slack_send_message': R['slack'].append(i)
            elif n=='linear_create_issue': R['created_issues'].append(i)
    runs[os.path.basename(f)]=R
json.dump(runs,open('runs.json','w'),indent=1)
for k,R in runs.items():
    print(k, len(R['sheet']), R['states'], len(R['comments']), R['shares'], [ (s.get('thread_ts'), len(s.get('text',''))) for s in R['slack']])

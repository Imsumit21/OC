import json,glob,collections,re,sys
bases={'julia':'Task_Authoring/support/completed_tasks/julia_zm_difficulty_baseline_2026-11-01/task_inputs/07_Baseline_Trajectories',
'douglas':'Task_Authoring/support/completed_tasks/douglas_beta_server_signoff_2026-10-28/task_inputs/07_Baseline_Trajectories',
'bridge':'Task_Authoring/support/completed_tasks/frederick_bridge_pipeline_2026-11-03/task_inputs/07_Baseline_Trajectories'}
def walk(o,acc):
    if isinstance(o,dict):
        if o.get('type')=='tool_use' and o.get('name'): acc.append(o['name'])
        for v in o.values(): walk(v,acc)
    elif isinstance(o,list):
        for v in o: walk(v,acc)
keys=['linear_list_comments','github_get_pull_request_comments','github_get_pull_request_reviews','github_get_file_contents','github_search_code','slack_read_thread','slack_read_channel','slack_search','confluence_list_comments','confluence_get_page','confluence_search','gsheets_values_get','gsheets_get_spreadsheet','gcal_list_events','trello_get_card','trello_get_card_comments','trello_list_card_actions','gmail_get_thread','contacts','snowflake_execute_query','gdocs_get']
for k,d in bases.items():
    fs=sorted(glob.glob(d+'/*.json'))
    print('==',k,len(fs))
    runs=[]
    for f in fs:
        try:o=json.load(open(f))
        except Exception as e: print('bad',f,e); continue
        acc=[];walk(o,acc)
        c=collections.Counter(re.sub(r'^mcp__[^_]*__','',a) for a in acc)
        runs.append(c)
    tot=[sum(v for n,v in c.items() if not re.match(r'(Bash|Read|Write|Edit|Task|Agent|Grep|Glob|TodoWrite)',n)) for c in runs]
    print(' calls per run',tot)
    allk=collections.Counter()
    for c in runs: allk.update(c.keys())
    names=[n for n,_ in allk.most_common(60)]
    for n in names:
        if re.search(r'comment|review|file_contents|search_code|thread|read_channel|list_events|get_card|action|snowflake|confluence',n):
            print('  ',n,'runs',allk[n],'/',len(runs),'calls',[c.get(n,0) for c in runs])

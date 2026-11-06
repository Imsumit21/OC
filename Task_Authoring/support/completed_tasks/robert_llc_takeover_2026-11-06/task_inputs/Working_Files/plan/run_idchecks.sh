#!/usr/bin/env bash
# Full-collection collision lookups for every id the current SQL mints (outputs in plan/idcheck/).
cd "$(dirname "$0")/../../../.." || exit 2
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs
D=Task_Authoring/task_inputs/Working_Files/plan/idcheck; S=Task_Authoring/tools/hg.py
python3 - <<'PY'
import sys, json
sys.path.insert(0,'Task_Authoring/tools')
from base_check import parse_sql
xs=[x for x in parse_sql(open('Task_Authoring/task_inputs/01_Universe_Inject.sql').read()) if x['op']=='insert']
g=lambda t,k:[x['row'][k] for x in xs if x['table']==t]
W='Task_Authoring/task_inputs/Working_Files/plan/idcheck/'
sets={'slack':g('slack.slack_messages','id'),'gmail_msg':g('gmail.gmail_messages','id'),'gmail_thread':g('gmail.gmail_threads','id'),
 'gdrive':g('gdrive.drive_files','id'),'gcal':g('gcal.gcal_events','event_id'),'trello_card':g('trello.trello_cards','id'),
 'trello_action':g('trello.trello_actions','id'),'linear_issue':g('linear.linear_issues','id'),'linear_project':g('linear.linear_projects','id'),
 'github_pr':g('github.github_pull_requests','id'),'github_branch':g('github.github_branches','id'),'github_commit':g('github.github_commits','sha'),
 'github_event':g('github.github_timeline_events','id')}
for k,v in sets.items(): json.dump(v, open(W+k+'.json','w'))
PY
run(){ timeout 3000 python3 $S search lookup $1 --ids-file $D/$2.json --file "$3" ${4:+--pointer $4} ${5:+--key $5} --compact > $D/$2.out.json 2>$D/$2.err; }
run gdrive gdrive data.json /drive_files id; run gcal gcal data.json /events event_id; run trello trello_card data.json /cards id; run trello trello_action data.json /actions id
run linear linear_issue data.json /issues id; run linear linear_project data.json /projects id; run github github_pr data.json /pull_requests id
run github github_branch data.json /branches id; run github github_commit data.json /commits sha; run github github_event data.json /timeline_events id
run slack slack 'messages/*/*.json' "" id; run gmail gmail_msg 'threads/*.json' /messages id
python3 -c "import json;ids=json.load(open('$D/gmail_thread.json'));print('\n'.join(i.split('/',1)[1] for i in ids))" > $D/gmail_thread_nums.txt
for n in $(cat $D/gmail_thread_nums.txt); do timeout 400 python3 $S search search gmail "$n" --limit 5 --compact 2>/dev/null | python3 -c "
import json,sys;d=json.load(sys.stdin);print('$n', len(d.get('matches',[])), d.get('scan_complete', True), d.get('files_selected'), d.get('truncated'))"; done > $D/gmail_thread_search.txt
for f in $D/*.out.json; do python3 -c "import json;d=json.load(open('$f'));print('$f'.split('/')[-1], d.get('scan_complete'), d.get('records_checked'), sum(1 for v in (d.get('matches') or {}).values() if v), len(d.get('matches') or {}))"; done
cat $D/gmail_thread_search.txt

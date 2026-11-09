#!/usr/bin/env python3
"""Counts tool use across stored Opus baselines in support/completed_tasks. Run from the workspace root. Other tasks' runs,
so these are habits, not rates for this task; memory records that exposure moves between revisions."""
import json, glob, collections, re, os
base = 'Task_Authoring/support/completed_tasks'
def walk(o, acc):
    if isinstance(o, dict):
        if o.get('type') == 'tool_use' and o.get('name'): acc.append(o['name'])
        for v in o.values(): walk(v, acc)
    elif isinstance(o, list):
        for v in o: walk(v, acc)
used, nruns = collections.Counter(), 0
for d in sorted(os.listdir(base)):
    runs = []
    for f in sorted(glob.glob(f'{base}/{d}/task_inputs/07_Baseline_Trajectories/*.json')):
        try: o = json.load(open(f))
        except Exception: continue
        acc = []; walk(o, acc)
        c = collections.Counter(re.sub(r'^mcp__[^_]*__', '', a) for a in acc)
        runs.append(c); nruns += 1
        for k in c: used[k] += 1
    if runs:
        print(d[:36], len(runs), [sum(v for n, v in c.items() if not re.match(r'(Bash|Read|Write|Edit|Task|Agent|Grep|Glob|TodoWrite|ToolSearch)', n)) for c in runs])
print('runs', nruns)
for k in ['slack_read_thread','slack_read_channel','slack_search_public_and_private','slack_search_channels','linear_list_comments','linear_get_issue','github_get_pull_request_reviews','github_get_pull_request_comments','github_search_pull_requests','github_list_branches','github_compare_commits','trello_get_comments','trello_get_board_actions','gcal_list_events']:
    print(f'{k:36} {used.get(k,0):3} / {nruns}')

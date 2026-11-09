#!/usr/bin/env python3
"""Tool-level habits of stored Opus 5.5 baselines on persona-led inbox tasks (read-only over support/completed_tasks).
Design input for trap placement only; exposure moves between revisions (memory: baseline-signature-concentration)."""
import json, glob, collections, re
ROOT = 'Task_Authoring/support/completed_tasks/'
bases = {
    'q4_commitments (Frederick)': ROOT + 'frederick_q4_commitments_2026-11-05/task_inputs/07_Baseline_Trajectories',
    'bridge_pipeline (Frederick)': ROOT + 'frederick_bridge_pipeline_2026-11-03/task_inputs/07_Baseline_Trajectories',
    'llc_takeover (Robert)': ROOT + 'robert_llc_takeover_2026-11-06/task_inputs/07_Baseline_Trajectories',
}
def walk(o, acc):
    if isinstance(o, dict):
        if o.get('type') == 'tool_use' and o.get('name'):
            acc.append((o['name'], o.get('input') or {}))
        for v in o.values():
            walk(v, acc)
    elif isinstance(o, list):
        for v in o:
            walk(v, acc)
SKIP = r'(Bash|Read|Write|Edit|Task|Agent|Grep|Glob|TodoWrite|ToolSearch)'
for k, d in bases.items():
    runs = []
    for f in sorted(glob.glob(d + '/*.json')):
        try:
            o = json.load(open(f))
        except Exception as e:
            print('bad', f, e); continue
        acc = []; walk(o, acc)
        runs.append([(re.sub(r'^mcp__[^_]*__', '', n), i) for n, i in acc])
    print('==', k, 'runs', len(runs))
    print(' service calls per run', [sum(1 for n, _ in r if not re.match(SKIP, n)) for r in runs])
    names = collections.Counter()
    for r in runs:
        names.update({n for n, _ in r})
    for n, c in names.most_common(70):
        if re.match(SKIP, n):
            continue
        if re.search(r'gcal|contacts|thread|read_channel|search_messages|search_public|linear_|github|trello_get|trello_search|gmail_(list|search|get)|drive|gdocs|confluence|snowflake', n):
            print(f'   {n:42} runs {c}/{len(runs)} calls {[sum(1 for x, _ in r if x == n) for r in runs]}')

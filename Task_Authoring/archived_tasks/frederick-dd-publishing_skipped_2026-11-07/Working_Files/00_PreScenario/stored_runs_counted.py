#!/usr/bin/env python3
"""Counted calls, write/read split, per-row spread and scores of stored baselines on completed tasks.
Read-only over support/completed_tasks. Counted = tool_call_detail recorded by tools/difficulty_stats.py where stored."""
import glob, json, re, statistics, collections
ROOT = 'Task_Authoring/support/completed_tasks/'
T = {'card_spend (Long, medium)': 'frederick_card_spend_q3_6ad83eebbd6456fd065bbd20',
     'account_handover (Normal, medium)': 'frederick_account_handover_2026-10-26',
     'bridge_pipeline (Long, medium)': 'frederick_bridge_pipeline_2026-11-03',
     'q4_commitments (Long, easy)': 'frederick_q4_commitments_2026-11-05',
     'llc_takeover (Long, easy)': 'robert_llc_takeover_2026-11-06'}
WRITE = re.compile(r'(create|add_new|add_comment|add_member|send|reply|update|move|share|copy|delete|values_|append|batch_update|mark|label|archive)')
def walk(o, acc):
    if isinstance(o, dict):
        if o.get('type') == 'tool_use' and o.get('name'):
            acc.append((o['name'], o.get('input') or {}))
        for v in o.values():
            walk(v, acc)
    elif isinstance(o, list):
        for v in o:
            walk(v, acc)
for k, d in T.items():
    p = ROOT + d + '/task_inputs/'
    print('==', k)
    wr, rd = [], []
    for f in sorted(glob.glob(p + '07_Baseline_Trajectories/*.json')):
        acc = []
        walk(json.load(open(f)), acc)
        seen = set(); w = r = 0
        for n, i in acc:
            if not n.startswith('mcp__') or n.endswith('set_acting_user'):
                continue
            key = (n, json.dumps(i, sort_keys=True))
            if key in seen:
                continue
            seen.add(key)
            s = n.split('__')[-1]
            if WRITE.search(s) and not re.search(r'_(get|list|search|read)_', '_' + s):
                w += 1
            else:
                r += 1
        wr.append(w); rd.append(r)
    print('  writes', wr, ' reads', rd, ' sum', [a + b for a, b in zip(wr, rd)])
    try:
        d2 = json.load(open(p + 'Working_Files/12_difficulty_input.json'))
    except Exception as e:
        print('  no input json', e); continue
    rub = d2.get('rubrics') or []
    ros = [x for x in d2.get('rollouts', []) if x.get('status') == 'completed']
    print('  counted', [x.get('tool_calls') for x in ros])
    wt = {x['id']: x.get('weight', 1) for x in rub}
    tot = sum(wt.values()); fails = collections.Counter(); scores = []
    for ro in ros:
        res = ro.get('results') or {}
        lost = 0
        for i in wt:
            if res.get(i) is False:
                fails[i] += 1; lost += wt[i]
        scores.append(1 - lost / tot)
    n = len(ros)
    allp = sum(wt[i] for i in wt if fails[i] == 0); allf = sum(wt[i] for i in wt if fails[i] == n)
    mix = [i for i in wt if 0 < fails[i] < n]
    print(f'  rows {len(wt)} weight {tot}: always-pass {allp/tot:.1%}  mixed {sum(wt[i] for i in mix)/tot:.1%} ({len(mix)} rows)  always-fail {allf/tot:.1%}')
    print('  scores', [round(s * 100, 1) for s in scores], 'mean', round(statistics.mean(scores) * 100, 1), 'pSD', round(statistics.pstdev(scores), 3))

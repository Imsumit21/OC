#!/usr/bin/env python3
"""Cross-task table from the stored completed tasks (real Opus runs). Run from the workspace root.
Rubric shape and scores come from each 12_difficulty_input.json; reads and writes come from the baseline trajectories."""
import json, glob, os, re, statistics, collections
base = 'Task_Authoring/support/completed_tasks'
WRITE = re.compile(r'(create|add_new|add_comment|add_member|send|reply|update|move|share|copy|delete|values_|append|batch_update|mark|label|archive)')
def uses(o, acc):
    if isinstance(o, dict):
        if o.get('type') == 'tool_use' and str(o.get('name', '')).startswith('mcp__'): acc.append(o)
        for v in o.values(): uses(v, acc)
    elif isinstance(o, list):
        for v in o: uses(v, acc)
print(f"{'task':30} {'rows':>4} {'wt':>4} {'avg':>6} {'SD':>6} {'full':>4} {'allpass%':>8} {'mixed%':>7} {'allfail%':>8} {'counted':>10} {'writes':>9} {'reads':>9}")
for d in sorted(os.listdir(base)):
    f = f'{base}/{d}/task_inputs/Working_Files/12_difficulty_input.json'
    if not os.path.exists(f): f = f'{base}/{d}/task_inputs/12_difficulty_input.json'
    W, R = [], []
    for t in sorted(glob.glob(f'{base}/{d}/task_inputs/07_Baseline_Trajectories/*.json')):
        try: o = json.load(open(t))
        except Exception: continue
        acc = []; uses(o, acc)
        seen, w, r = set(), 0, 0
        for u in acc:
            if u['name'].endswith('set_acting_user'): continue
            key = (u['name'], json.dumps(u.get('input'), sort_keys=True))
            if key in seen: continue
            seen.add(key)
            n = u['name'].split('__')[-1]
            if WRITE.search(n) and not re.search(r'_(get|list|search|read)_', '_' + n): w += 1
            else: r += 1
        W.append(w); R.append(r)
    if not os.path.exists(f):
        print(f"{d[:30]:30} (no difficulty input)  writes {min(W) if W else '-'}-{max(W) if W else '-'} reads {min(R) if R else '-'}-{max(R) if R else '-'}"); continue
    j = json.load(open(f))
    rub = {r['id']: r['weight'] for r in j['rubrics']}
    T = sum(rub.values())
    runs = [r for r in j['rollouts'] if r.get('status') == 'completed' and r.get('results')]
    sc = [sum(rub[k] for k, v in r['results'].items() if v and k in rub) / T for r in runs]
    ap = sum(w for k, w in rub.items() if all(r['results'].get(k) for r in runs))
    af = sum(w for k, w in rub.items() if not any(r['results'].get(k) for r in runs))
    mx = T - ap - af
    cc = [r.get('tool_calls') for r in runs]
    full = sum(1 for s in sc if s >= .9999)
    print(f"{d[:30]:30} {len(rub):4} {T:4} {statistics.mean(sc):6.1%} {statistics.pstdev(sc):6.3f} {full:4} {ap/T:8.1%} {mx/T:7.1%} {af/T:8.1%} {str(min(cc))+'-'+str(max(cc)):>10} {str(min(W) if W else '-')+'-'+str(max(W) if W else '-'):>9} {str(min(R) if R else '-')+'-'+str(max(R) if R else '-'):>9}")

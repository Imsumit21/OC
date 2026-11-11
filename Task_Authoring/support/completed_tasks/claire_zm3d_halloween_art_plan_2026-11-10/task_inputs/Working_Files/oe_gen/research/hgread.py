#!/usr/bin/env python3
"""Read-only helper: full-record reads via hg.py search get-many, paging until complete."""
import json, os, subprocess, sys
ROOT = '/Users/sumit/Source/OC'
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR='Task_Authoring/task_inputsN2')
PY = os.path.expanduser('~/.local/bin/python3.12')

def hg(*args, stdin=None):
    p = subprocess.run([PY, '-B', 'Task_Authoring/tools/hg.py', 'search', *args], cwd=ROOT, env=ENV,
                       input=stdin, capture_output=True, text=True)
    try:
        return json.loads(p.stdout)
    except Exception:
        raise SystemExit(f'hg failed rc={p.returncode}: {p.stderr[-800:]} {p.stdout[:400]}')

def read_many(items, page=100000, batch_size=5):
    """items: [(service, file, pointer)] -> {(service,file,pointer): parsed json}"""
    out = {}
    state = {i: {'svc': s, 'file': f, 'ptr': p, 'off': 0, 'buf': []} for i, (s, f, p) in enumerate(items)}
    pending = list(state)
    while pending:
        batch, pending = pending[:batch_size], pending[batch_size:]
        req = {'items': [{'id': f'i{i}', 'service': state[i]['svc'], 'file': state[i]['file'],
                          'pointer': state[i]['ptr'], 'offset': state[i]['off'], 'max_chars': page} for i in batch]}
        r = hg('get-many', '--request', '-', '--compact', stdin=json.dumps(req))
        for i in batch:
            it = r['items'][f'i{i}']
            if it.get('error') or it.get('errors'):
                raise SystemExit(f"error on {state[i]}: {it}")
            state[i]['buf'].append(it['text'])
            if it.get('truncated'):
                state[i]['off'] = it['next_offset']
                pending.append(i)
    for i, st in state.items():
        out[(st['svc'], st['file'], st['ptr'])] = json.loads(''.join(st['buf']))
    return out

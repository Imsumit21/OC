#!/usr/bin/env python3
"""search-many through Task_Authoring/tools/hg.py; usage: sm.py <service> <fileglob> q1 [q2 ...]"""
import json, os, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), *[".."] * 4))
svc, glob, qs = sys.argv[1], sys.argv[2], sys.argv[3:]
lim = int(os.environ.get("SM_LIMIT", "40"))
req = {"service": svc, "file": glob, "queries": [{"id": f"q{i}", "query": q, "limit": lim} for i, q in enumerate(qs)]}
r = subprocess.run([sys.executable, os.path.join(ROOT, "Task_Authoring/tools/hg.py"), "search", "search-many", "--request", "-", "--compact"],
                   input=json.dumps(req), capture_output=True, text=True, cwd=ROOT,
                   env={**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"})
d = json.loads(r.stdout)
for i, q in enumerate(qs):
    res = d["queries"][f"q{i}"]
    ms = res.get("matches", [])
    print(f"== {q!r}: {len(ms)} matches{' (limit hit)' if len(ms) >= lim else ''}")
    for m in ms:
        print("  ", m.get("service_file"), m.get("pointer"), (m.get("text") or "")[:220].replace("\n", " | "))

#!/usr/bin/env python3
"""Measures the human-time volumes through hg.py search only and writes plan/out/humantime_volumes.json."""
import json, os, re, subprocess, collections
from datetime import datetime, timezone, timedelta
HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")
PT = timedelta(hours=-8)

def hg(service, query, *a):
    out, offset = [], 0
    r = subprocess.run(["python3", "Task_Authoring/tools/hg.py", "search", "search", service, query, "--limit", "200000", "--compact", *a], cwd=WS, env=ENV, capture_output=True, text=True, timeout=500)
    d = json.loads(r.stdout)
    return d

def ts_counts(ch):
    d = hg("slack", ".", "--file", f"messages/{ch}/*.json", "--key", "ts")
    t = sorted(float(m["text"]) for m in d["matches"])
    return t, d.get("scan_complete"), d.get("stop_reason")

def day(s):
    return datetime.strptime(s, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp() - PT.total_seconds()

res = {}
sql = open(os.path.join(WS, "Task_Authoring/task_inputs/01_Universe_Inject.sql")).read()
chans = {"canvas CE156FDFB428": ("CE156FDFB428", "2025-11-01", "2026-02-14"), "#god-bugs C05V5FNLB9V": ("C05V5FNLB9V", "2025-11-13", "2026-02-14"),
         "#builds C05433XK267": ("C05433XK267", "2025-11-01", "2026-02-14"), "sub-250 C09Q4S613CN": ("C09Q4S613CN", "2025-11-01", "2026-02-14"),
         "publishing C09SWTHEMEW": ("C09SWTHEMEW", "2025-12-01", "2026-02-14"), "bots C050WGU41HR": ("C050WGU41HR", "2025-11-01", "2026-02-14"),
         "Arthur DM D05S1S2AB5M": ("D05S1S2AB5M", "2026-02-01", "2026-02-14"), "Marcus DM D05USBTQY1F": ("D05USBTQY1F", "2025-11-01", "2026-02-14"),
         "Brian DM D07E9PSQB6W": ("D07E9PSQB6W", "2025-11-01", "2026-02-14")}
for name, (ch, a, b) in chans.items():
    t, done, why = ts_counts(ch)
    w = [x for x in t if day(a) <= x < day(b)]
    seeded = len(re.findall(rf"VALUES \('[0-9a-f]+', '[0-9.]+', '{ch}', 'message'", sql))
    res[name] = dict(total=len(t), window=f"{a}..{b} PT", in_window=len(w), seeded=seeded, scan_complete=done, stop=why, first=(datetime.fromtimestamp(t[0], timezone.utc).isoformat() if t else None), last=(datetime.fromtimestamp(t[-1], timezone.utc).isoformat() if t else None))
    print(name, res[name], flush=True)
json.dump(res, open(os.path.join(HERE, "out", "humantime_volumes.json"), "w"), indent=1)

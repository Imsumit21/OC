#!/usr/bin/env python3
"""Measures the human-time volumes through hg.py search only and writes plan/out/humantime_volumes.json."""
import json, os, re, subprocess
from datetime import datetime, timezone, timedelta
HERE = os.path.dirname(os.path.abspath(__file__)); WS = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")
def hg(service, query, *a):
    r = subprocess.run(["python3", "Task_Authoring/tools/hg.py", "search", "search", service, query, "--limit", "200000", "--compact", *a], cwd=WS, env=ENV, capture_output=True, text=True, timeout=500)
    return json.loads(r.stdout)
def day(s):  # PT midnight (PDT, UTC-7)
    return datetime.strptime(s, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp() + 7 * 3600
sql = open(os.path.join(WS, "Task_Authoring/task_inputs/01_Universe_Inject.sql")).read()
res = {}
A, B = "2025-09-15", "2025-10-01"
for name, ch in {"#builds": "C05433XK267", "#zombie-bugs": "C08R27X0EAH", "#zombie-match3d": "C0880U9751A", "#zombie-prs": "C093LEZGF6J",
                 "Brian DM": "D0770ET6WBW", "Vincent DM": "D06UPGF5PQV", "Marcus DM": "D05U73FNDDL", "Julia DM": "D05HYDTG5TJ"}.items():
    d = hg("slack", ".", "--file", f"messages/{ch}/*.json", "--key", "ts")
    t = sorted(float(m["text"]) for m in d["matches"])
    w = [x for x in t if day(A) <= x < day(B)]
    seeded = len(re.findall(rf"'{ch}'", sql.split("INSERT INTO trello")[0])) and sum(1 for c in sql.split("INSERT INTO ")[1:] if c.startswith("slack.slack_messages") and f"'{ch}'" in c)
    res[name] = dict(channel=ch, total=len(t), window=f"{A}..{B} PT", in_window=len(w), seeded=seeded, scan_complete=d.get("scan_complete"))
    print(name, res[name], flush=True)
d = hg("linear", "ZOM-", "--key", "identifier"); res["ZOM issues"] = dict(total=len(d["matches"]), scan_complete=d.get("scan_complete")); print("ZOM", res["ZOM issues"])
d = hg("github", "match3d#", "--key", "id", "--pointer", "/pull_requests"); ids = [m["parent_pointer"] for m in d["matches"]]
c = hg("github", "2025-09", "--key", "created_at", "--pointer", "/pull_requests"); rec = {m["parent_pointer"]: m["text"] for m in c["matches"]}
res["match3d PRs"] = dict(total=len(ids), opened_since_sep15=sum(1 for p in ids if rec.get(p, "") >= "2025-09-15"), scan_complete=d.get("scan_complete")); print("PRs", res["match3d PRs"])
d = hg("trello", "6851a6569f3bf818760632ab", "--key", "idBoard"); res["ZM ROADMAP cards"] = dict(total=len(d["matches"]), scan_complete=d.get("scan_complete")); print("cards", res["ZM ROADMAP cards"])
json.dump(res, open(os.path.join(HERE, "out", "humantime_volumes.json"), "w"), indent=1)

#!/usr/bin/env python3
"""Act-vs-defer search for the OE ledger (§C). Owen-scoped Slack and Gmail through persona_view search; Linear and Trello
through hg.py search (unscoped); the seeded SQL rows by text. Writes plan/oe_defer.json."""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
ENV = {**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"}
TERMS = ["hold off", "not yet", "don't move", "dont move", "wait for", "wait until", "on hold", "don't close", "leave it open", "don't file", "keep it open", "before you close"]
LIMIT = "3000"


def run(args):
    p = subprocess.run(args, cwd=WS, env=ENV, capture_output=True, text=True, timeout=1500)
    return json.loads(p.stdout) if p.stdout.strip().startswith("{") else {"error": p.stderr[-500:]}


out = {}
for svc in ("slack", "gmail"):
    for t in TERMS:
        d = run(["python3", "Task_Authoring/tools/persona_view.py", "search", "owen_baker", svc, t, "--json", "--limit", LIMIT])
        ms = d.get("visible") or []
        late = [m for m in ms if str(m.get("date") or "") >= "2026-02-12"]
        out[f"{svc}:{t}"] = {"visible": d.get("visible_total", len(ms)), "complete": "error" not in d, "hit_limit": len(ms) >= int(LIMIT),
                             "hidden_by_acl": d.get("hidden_by_acl"), "unverified": d.get("unverified"),
                             "feb_2026": [{"file": m.get("channel") or m.get("mailbox") or "", "pointer": m.get("id"), "text": (m.get("snippet") or m.get("subject") or "")[:300], "date": m.get("date")} for m in late][:40]}
for svc in ("linear", "trello"):
    for t in TERMS:
        d = run(["python3", "Task_Authoring/tools/hg.py", "search", "search", svc, t, "--limit", LIMIT])
        ms = d.get("matches") or []
        out[f"{svc}:{t}"] = {"visible": len(ms), "complete": d.get("scan_complete"), "hit_limit": len(ms) >= int(LIMIT),
                             "texts": [(m.get("service_file"), m.get("pointer"), (m.get("text") or "")[:200]) for m in ms][:60]}
sql = open(os.path.join(HERE, "..", "..", "01_Universe_Inject.sql")).read().lower()
out["sql"] = {t: sql.count(t) for t in TERMS}
json.dump(out, open(os.path.join(HERE, "oe_defer.json"), "w"), indent=1)
for k, v in out.items():
    if k == "sql":
        print("sql", v)
    else:
        print(k, v["visible"], "complete", v["complete"], "limit", v["hit_limit"], "feb", len(v.get("feb_2026", [])) if "feb_2026" in v else "-")

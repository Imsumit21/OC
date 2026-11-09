#!/usr/bin/env python3
"""For every search an OE names: Owen-visible base hits (persona_view search), seeded rows whose text carries the term, and where the
target sits among them, newest first. Writes plan/oe_locator_ranks.json."""
import json, os, subprocess, sys, re
HERE = os.path.dirname(os.path.abspath(__file__)); TI = os.path.dirname(os.path.dirname(HERE)); WS = os.path.dirname(os.path.dirname(TI))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql
ENV = {**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"}
ST = [x for x in parse_sql(open(os.path.join(TI, "01_Universe_Inject.sql")).read()) if x["op"] == "insert"]
Q = [("slack", "Memory Tile", "C09Q4S613CN/1764606918.318209"), ("slack", "Tavern", "D05USBTQY1F/1765452012.418229"), ("slack", "lives", "C09SWTHEMEW/1764659626.614679"),
     ("slack", "EconomyChanges", "C05433XK267/1765310004.760809"), ("slack", "flickering", "C09Q4S613CN/1766164222.418229"), ("slack", "music", "D07E9PSQB6W/1765206644.602119"),
     ("gmail", "vincent.parker", "owen.baker@harmonygames.co/1849333980856689601")]
out = []
for svc, q, target in Q:
    d = json.loads(subprocess.run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "search", "owen_baker", svc, q, "--json", "--limit", "5000"], cwd=WS, env=ENV, capture_output=True, text=True).stdout)
    vis = d.get("visible") or []
    tbl = {"slack": "slack.slack_messages", "gmail": "gmail.gmail_messages"}[svc]
    seeded = []
    for x in ST:
        r = x["row"]
        if x["table"] != tbl:
            continue
        blob = " ".join(str(v) for v in r.values())
        if q.casefold() in blob.casefold():
            sid = f"{r['channel_id']}/{r['ts']}" if svc == "slack" else r["thread_id"]
            date = r.get("created_at") or r.get("date")
            seeded.append({"id": sid, "date": str(date)[:10]})
    allh = [{"id": m.get("id"), "date": str(m.get("date"))[:10]} for m in vis] + seeded
    allh.sort(key=lambda h: h["date"], reverse=True)
    rank = next((i for i, h in enumerate(allh, 1) if h["id"] == target or str(h["id"]).startswith(target)), None)
    out.append({"service": svc, "query": q, "target": target, "base_visible": len(vis), "seeded_hits": len(seeded), "total": len(allh), "rank_newest_first": rank})
    print(svc, q, len(vis), len(seeded), rank)
json.dump(out, open(os.path.join(HERE, "oe_locator_ranks.json"), "w"), indent=1)

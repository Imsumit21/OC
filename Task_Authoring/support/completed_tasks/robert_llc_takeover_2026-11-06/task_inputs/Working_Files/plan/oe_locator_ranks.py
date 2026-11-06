#!/usr/bin/env python3
"""OE check: locator test. For each search an OE names, Robert's visible base hits (persona_view search) plus the seeded
rows whose text holds the query (SQL read as text, never executed); rank = position by date, newest first. Writes
plan/oe_locator_ranks.json."""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WS = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
ENV = {**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"}
sys.path.insert(0, os.path.join(WS, "Task_Authoring", "tools"))
from base_check import parse_sql
ST = [x for x in parse_sql(open(os.path.join(WS, "Task_Authoring/task_inputs/01_Universe_Inject.sql")).read()) if x["op"] == "insert"]
def seeded(svc, q):
    ql = q.lower(); out = []
    for x in ST:
        r = x["row"]
        if svc == "slack" and x["table"] == "slack.slack_messages":
            if ql in (r.get("text") or "").lower(): out.append((f"{r['channel_id']}/{r['ts']}", r["created_at"][:10]))
        if svc == "gmail" and x["table"] == "gmail.gmail_messages" and r["user_email"] == "robert@harmonygames.co":
            if ql in ((r.get("subject") or "") + " " + (r.get("body_text") or "")).lower(): out.append((r["id"], r["date"][:10]))
        if svc == "gdrive" and x["table"] == "gdrive.drive_files" and "robert@harmonygames.co" in (r.get("shared_with_emails_json") or "") + (r.get("owner_email") or ""):
            if ql in (r.get("name") or "").lower(): out.append((r["id"], r["created_time"][:10]))
    return out
Q = [("slack", "AWS bill", "D04V95AAAHW/1770952200.665739"), ("slack", "my card", "C09UHHN6PFZ/1770938400.370665"),
     ("slack", "layer.ai", "C09UHHN6PFZ/1770837702.167889"), ("slack", "calm play", "C04UEQVDVB7/1703492127.063049"),
     ("gmail", "split", "<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>"),
     ("gmail", "metabase", "<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>"),
     ("gmail", "jenkins", "<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>"),
     ("gmail", "Domino Delights", "<136285951.151027292.1770967800000@email.apple.com>"),
     ("gdrive", "ground rules", "f_1e468a9d69ea0f0a2001f5"), ("gdrive", "LLC", "f_d996e4c434ce160dc52596")]
res = []
for svc, q, target in Q:
    p = subprocess.run(["python3", "Task_Authoring/tools/persona_view.py", "search", "robert", svc, q, "--json", "--limit", "5000"], cwd=WS, env=ENV, capture_output=True, text=True, timeout=1500)
    d = json.loads(p.stdout)
    base = [(m.get("id"), str(m.get("date") or "")[:10]) for m in d.get("visible") or []]
    sd = seeded(svc, q)
    allh = sorted(set(base) | set(sd), key=lambda t: t[1], reverse=True)
    ids = [h[0] for h in allh]
    rank = next((i + 1 for i, h in enumerate(ids) if h and h.endswith(target)), None)
    res.append({"unverified": d.get("unverified"), "service": svc, "query": q, "target": target, "base_visible": d.get("visible_total"), "seeded_hits": len(sd), "rank_newest_first": rank,
                "total": len(allh), "top3": allh[:3]})
    print(f"{svc:6} {q!r:30} visible {d.get('visible_total')} seeded {len(sd)} total {len(allh)} rank {rank}")
json.dump(res, open(os.path.join(HERE, "oe_locator_ranks.json"), "w"), indent=1)

#!/usr/bin/env python3
"""sample_task_02 (iteration 6): Slack copies of every seeded PR conversation comment (GitHub Slack app mirror rule).

Inputs: the prc(...) calls in ../gen_sql.py (the 13 PR comments carried from sample_task_01) and base extracts taken
with tools/hg.py (mirror-channel months, PR titles) passed as JSON on the command line:
  python3 plan_mirrors.py <mirror_dump_dir> <prs.json>
Output: mirrors.json - one mirror reply per comment (channel, thread parent, ts, attachment) + parent reply_count/latest_reply.
Shape copied from base human-comment mirrors, e.g. C093LEZGF6J/2025-10.json /271 (match3d#486 "Not ready for merge").
"""
import bisect
import datetime as dt
import glob
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
dump_dir, prs_path = sys.argv[1], sys.argv[2]
CHANNEL = {"match3d": "C093LEZGF6J", "GameOfDominoes": "C050WGU41HR", "game-of-dominoes-backend": "C050WGU41HR"}
LOGIN = {"EMPLOYEE_0025_GITHUB_USERNAME": "arthur.blake", "EMPLOYEE_0003_GITHUB_USERNAME": "oliver.brooks",
         "PERSON_5877_GITHUB_USERNAME": "owen.baker", "EMPLOYEE_0004_GITHUB_USERNAME": "samuel.turner",
         "PERSON_0180_GITHUB_USERNAME": "brian.foster"}
LOGIN_VAR = {"AG": "EMPLOYEE_0025_GITHUB_USERNAME", "OG": "EMPLOYEE_0003_GITHUB_USERNAME", "P5877": "PERSON_5877_GITHUB_USERNAME"}

src = (HERE.parent / "gen_sql.py").read_text()
calls = re.findall(r'prc\(G \+ "([^"]+)", (\d+), (\d+), ([A-Za-z0-9_"]+), "([^"]+)",\n\s+"((?:[^"\\]|\\.)*)", (?:None|True)\)', src)
msgs = []
for f in glob.glob(dump_dir + "/mir_*.json"):
    msgs += json.loads(json.load(open(f))["text"])
prs = {p["id"]: p for p in json.loads(json.load(open(prs_path))["text"])}
pts = sorted((float(x["ts"]), int(m.group(1))) for x in msgs for a in (x.get("attachments") or [])
             for m in [re.search(r"issuecomment-(\d+)", a.get("pretext") or "")] if m)
existing_ts = {(x["channel"], x["ts"]) for x in msgs}


def comment_id(epoch):
    xs = [p[0] for p in pts]
    i = min(max(bisect.bisect_left(xs, epoch), 1), len(pts) - 1)
    (x0, y0), (x1, y1) = pts[i - 1], pts[i]
    return int(y0 + (y1 - y0) * (epoch - x0) / (x1 - x0))


out, parents = [], {}
for pr, n_c, n_ev, login, iso, body in calls:
    repo, num = pr.split("#")
    login = LOGIN_VAR.get(login, login.strip('"'))
    ch = CHANNEL[repo]
    url = f"https://github.com/harmonygames-Games/{repo}/pull/{num}"
    thread = [x for x in msgs if x["channel"] == ch and re.search(rf"/{repo}/pull/{num}\b", json.dumps(x.get("attachments") or []))
              and x.get("thread_ts") == x["ts"]]
    if not thread:
        out.append({"pr": pr, "skipped": "no mirror thread for this PR in the base (its base comments are not mirrored either)"})
        continue
    parent = thread[0]
    epoch = dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp()
    n = int(hashlib.sha256(pr.encode()).hexdigest(), 16)
    ts = f"{int(epoch) + 2 + n % 3}.{n % 900000 + 100000:06d}"
    assert (ch, ts) not in existing_ts
    title = prs["harmonygames-Games/" + pr]["title"]
    cid = comment_id(epoch)
    att = [{"color": "24292f", "fallback": f"[harmonygames-Games/{repo}] Comment on #{num}",
            "footer": f"<https://github.com/harmonygames-Games/{repo}|harmonygames-Games/{repo}>",
            "footer_icon": "https://slack.github.com/static/img/favicon-neutral.png", "id": 1, "mrkdwn_in": ["text"],
            "pretext": f"<{url}#issuecomment-{cid}|Comment> on pull request by <https://github.com/{LOGIN[login]}|{LOGIN[login]}>",
            "text": body.encode().decode("unicode_escape") if "\\" in body else body,
            "title": f"<{url}|#{num} {title}>", "ts": int(epoch)}]
    out.append({"pr": pr, "channel": ch, "ts": ts, "parent_ts": parent["ts"], "attachments": att, "comment_iso": iso})
    p = parents.setdefault((ch, parent["ts"]), {"channel": ch, "ts": parent["ts"], "reply_count": int(parent["reply_count"]),
                                                "latest_reply": parent.get("latest_reply")})
    p["reply_count"] += 1
    p["latest_reply"] = max([v for v in (p["latest_reply"], ts) if v], key=float)
(HERE / "mirrors.json").write_text(json.dumps({"replies": out, "parents": list(parents.values())}, indent=1))
print(len(calls), "PR comments;", sum(1 for o in out if "ts" in o), "mirrored;", [o["pr"] for o in out if "skipped" in o], "skipped")

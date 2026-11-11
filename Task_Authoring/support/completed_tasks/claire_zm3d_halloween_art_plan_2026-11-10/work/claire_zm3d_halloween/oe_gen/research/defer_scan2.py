#!/usr/bin/env python3
"""Second read-only sweep: extra topic terms and date literals (Claire Morgan, synth-cut).

argv[1] = scratch output directory. Same routing as defer_scan.py.
"""
import concurrent.futures as cf
import json
import os
import subprocess
import sys
from pathlib import Path

WS = Path("/Users/sumit/Source/OC")
PY = os.path.expanduser("~/.local/bin/python3.12")
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputsN2", PYTHONDONTWRITEBYTECODE="1")
OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
TERMS = ["marketing", "creative", "campaign", "unity ads", "retention campaign", "statics", "static", "ad statics",
         "Oct 10", "Oct 15", "Oct 17", "Oct 18", "Oct 12", "Oct 20", "Oct 24", "October 10", "October 15",
         "October 17", "October 18", "10 Oct", "15 Oct", "manual review", "Android US", "iOS UK",
         "Unity rep", "plan doc", "tracker", "ZM3D", "marcus", "julia", "icon", "store", "cadılar", "ertele",
         "reklam", "iptal"]
SCOPED = ["slack", "gmail", "gcal", "gdrive", "gdocs", "gslides", "gsheets"]
FILES = {"linear": "data.json", "trello": "data.json", "github": "data.json", "confluence": "confluence_working.json"}


def scoped(svc, term):
    r = subprocess.run([PY, "-B", "Task_Authoring/tools/persona_view.py", "search", "claire_morgan", svc, term,
                        "--limit", "500000", "--no-hidden", "--json"], capture_output=True, text=True, cwd=str(WS), env=ENV)
    try:
        return svc, term, json.loads(r.stdout)
    except ValueError:
        return svc, term, {"error": r.stderr[-800:], "visible": [], "visible_total": None}


def unscoped(svc):
    req = {"service": svc, "file": FILES[svc], "queries": [{"id": f"q{i}", "query": t, "limit": 200000} for i, t in enumerate(TERMS)]}
    p = OUT / f"req2_{svc}.json"
    p.write_text(json.dumps(req))
    r = subprocess.run([PY, "-B", "Task_Authoring/tools/hg.py", "search", "search-many", "--request", str(p), "--compact"],
                       capture_output=True, text=True, cwd=str(WS), env=ENV)
    d = json.loads(r.stdout)
    d["_terms"] = {f"q{i}": t for i, t in enumerate(TERMS)}
    (OUT / f"unscoped2_{svc}.json").write_text(json.dumps(d))
    return svc


res = {}
with cf.ThreadPoolExecutor(6) as ex:
    futs = [ex.submit(scoped, s, t) for s in SCOPED for t in TERMS]
    ufs = [ex.submit(unscoped, s) for s in FILES]
    for f in cf.as_completed(futs):
        s, t, d = f.result()
        res.setdefault(s, {})[t] = d
    for f in cf.as_completed(ufs):
        print("done", f.result(), flush=True)
(OUT / "scoped2.json").write_text(json.dumps(res))
rows = json.load(open(WS / "Task_Authoring/task_inputsN2/Working_Files/oe_gen/sql_rows.json"))
hits = {t: [] for t in TERMS}
for x in rows:
    blob = json.dumps(x, ensure_ascii=False).casefold()
    for t in TERMS:
        if t.casefold() in blob:
            hits[t].append({"line": x["line"], "op": x["op"], "table": x["table"]})
(OUT / "overlay2_hits.json").write_text(json.dumps(hits))
print("ok")

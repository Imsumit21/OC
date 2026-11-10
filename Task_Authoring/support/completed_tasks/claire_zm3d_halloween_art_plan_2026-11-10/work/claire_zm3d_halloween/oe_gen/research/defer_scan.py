#!/usr/bin/env python3
"""Read-only term sweep for the act-vs-defer and absence checks (Claire Morgan, synth-cut).

Scoped services go through persona_view.py search (only what Claire can see).
Unscoped services go through hg.py search search-many (complete scan, per-query limit).
Overlay rows are matched as data from sql_rows.json; SQL is never executed.
Raw results go to the directory given as argv[1] (a scratch directory, not the task folder).
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
ROWS = WS / "Task_Authoring/task_inputsN2/Working_Files/oe_gen/sql_rows.json"

DEFER = ["halloween", "defer", "hold off", "not yet", "wait", "as-is", "as is", "accept", "freeze",
         "pause", "postpone", "cancel", "on hold", "delay", "push back", "scrap"]
IDENT = ["ART-79", "ART-8", "couch boss", "couch alpha", "balloons alpha", "barrel alpha",
         "marketing2", "cheer 30p", "fastcouch", "alin2", "squirrelfail", "mrfluffernot",
         "cinematicTutorial", "tutorialCinematic", "marcus.bennett 9", "marcus.bennett 1",
         "marcus.bennett 4", "julia 1:1", "julia 4:5", "julia 9:16", "julia 16:9", "end card",
         "endcard", "GreenCouch", "Professional Mode", "sophie ocean", "live creative",
         "UA creative", "UA master", "app icon", "appicon", "ipad", "12.9", "screenshot",
         "store listing", "store page", "october ua", "seasonal", "pumpkin", "spooky"]
LEAVE = ["vacation", "out of office", "ooo", "on leave", "time off", "day off", "days off", "pto", "maternity",
         "paternity", "sick leave", "takes over", "cover for", "covering", "taking over", "away from"]
TERMS = DEFER + IDENT + LEAVE
SCOPED = ["slack", "gmail", "gcal", "gdrive", "gdocs", "gslides", "gsheets"]
UNSCOPED = ["linear", "trello", "confluence", "github", "contacts"]


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, cwd=str(WS), env=ENV)


def scoped(svc, term):
    r = run([PY, "-B", "Task_Authoring/tools/persona_view.py", "search", "claire_morgan", svc, term,
             "--limit", "500000", "--no-hidden", "--json"])
    try:
        d = json.loads(r.stdout)
    except ValueError:
        d = {"error": r.stderr[-800:], "visible": [], "visible_total": None}
    return svc, term, d


def unscoped(svc):
    req = {"service": svc, "queries": [{"id": f"q{i}", "query": t, "limit": 200000} for i, t in enumerate(TERMS)]}
    if svc in ("linear", "trello", "confluence", "github", "contacts"):
        req["file"] = {"contacts": "contacts.json"}.get(svc, "data.json")
    p = OUT / f"req_{svc}.json"
    p.write_text(json.dumps(req))
    r = run([PY, "-B", "Task_Authoring/tools/hg.py", "search", "search-many", "--request", str(p), "--compact"])
    try:
        d = json.loads(r.stdout)
    except ValueError:
        d = {"error": r.stderr[-800:], "stdout": r.stdout[:800]}
    d["_terms"] = {f"q{i}": t for i, t in enumerate(TERMS)}
    (OUT / f"unscoped_{svc}.json").write_text(json.dumps(d))
    return svc


def overlay():
    rows = json.load(open(ROWS))
    hits = {t: [] for t in TERMS}
    for x in rows:
        blob = json.dumps(x, ensure_ascii=False).casefold()
        for t in TERMS:
            if t.casefold() in blob:
                hits[t].append({"line": x["line"], "op": x["op"], "table": x["table"]})
    (OUT / "overlay_hits.json").write_text(json.dumps(hits))


def main():
    overlay()
    res = {}
    with cf.ThreadPoolExecutor(6) as ex:
        futs = [ex.submit(scoped, s, t) for s in SCOPED for t in TERMS]
        ufs = [ex.submit(unscoped, s) for s in UNSCOPED]
        for f in cf.as_completed(futs):
            s, t, d = f.result()
            res.setdefault(s, {})[t] = d
        for f in cf.as_completed(ufs):
            print("done", f.result(), flush=True)
    (OUT / "scoped.json").write_text(json.dumps(res))
    print("scoped done", flush=True)


if __name__ == "__main__":
    main()

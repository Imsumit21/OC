#!/usr/bin/env python3
"""Look up every minted id over its full base collection through tools/hg.py; outputs in plan/idcheck/."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TI = os.path.dirname(os.path.dirname(HERE))
WS = os.path.dirname(os.path.dirname(TI))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql
rows = [x for x in parse_sql(open(os.path.join(TI, "01_Universe_Inject.sql")).read()) if x["op"] == "insert"]
col = {}
for x in rows:
    col.setdefault(x["table"], []).append(x["row"])
PLAN = [("gdrive", "gdrive", "data.json", "/drive_files" , "id", [r["id"] for r in col["gdrive.drive_files"]]),
        ("gcal", "gcal", "data.json", "/events", "event_id", [r["event_id"] for r in col["gcal.gcal_events"]]),
        ("trello_card", "trello", "data.json", "/cards", "id", [r["id"] for r in col["trello.trello_cards"]]),
        ("trello_action", "trello", "data.json", "/actions", "id", [r["id"] for r in col["trello.trello_actions"]]),
        ("trello_checklist", "trello", "data.json", "/checklists", "id", [r["id"] for r in col["trello.trello_checklists"]]),
        ("trello_check_item", "trello", "data.json", "/check_items", "id", [r["id"] for r in col["trello.trello_check_items"]]),
        ("github_comment", "github", "data.json", "/pull_request_comments", "id", [r["id"] for r in col["github.github_pr_comments"]]),
        ("github_event", "github", "data.json", "/timeline_events", "id", [r["id"] for r in col["github.github_timeline_events"]]),
        ("github_rc", "github", "data.json", "/review_comments", "id", [r["id"] for r in col["github.github_review_comments"]])]
env = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")
for name, svc, f, ptr, key, ids in PLAN:
    p = os.path.join(HERE, "idcheck", name + ".json")
    json.dump(ids, open(p, "w"))
    r = subprocess.run(["python3", "Task_Authoring/tools/hg.py", "search", "lookup", svc, "--ids-file", p, "--file", f, "--pointer", ptr, "--key", key, "--compact"], cwd=WS, env=env, capture_output=True, text=True, timeout=280)
    open(os.path.join(HERE, "idcheck", name + ".out.json"), "w").write(r.stdout)
    try:
        d = json.loads(r.stdout)
        print(name, len(ids), "found", len(d.get("found") or d.get("matches") or []), "records", d.get("records_checked") or d.get("records_seen"), "scan_complete", d.get("scan_complete"), r.stderr[-120:])
    except Exception as e:
        print(name, "ERR", r.stdout[:200], r.stderr[-200:])

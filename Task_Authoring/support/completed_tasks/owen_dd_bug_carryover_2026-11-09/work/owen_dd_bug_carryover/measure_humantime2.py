#!/usr/bin/env python3
"""Second measurement pass: Linear, GitHub, Gmail, Trello and #god-bugs posts, through hg.py search only."""
import json, os, re, subprocess, collections
from datetime import datetime, timezone, timedelta
HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")
def hg(service, query, *a):
    r = subprocess.run(["python3", "Task_Authoring/tools/hg.py", "search", "search", service, query, "--limit", "200000", "--compact", *a], cwd=WS, env=ENV, capture_output=True, text=True, timeout=500)
    return json.loads(r.stdout)
res = {}
truth = json.load(open(os.path.join(HERE, "..", "solver", "truth.json")))
ids = hg("linear", "ENG-", "--key", "identifier", "--file", "data.json")
ptr = {m["parent_pointer"]: m["text"] for m in ids["matches"]}
state = {}
for s in ("Done", "Canceled", "Bugs", "Backlog", "Todo", "In Progress", "In Review", "Duplicate", "Triage"):
    for m in hg("linear", s, "--key", "state_id", "--file", "data.json")["matches"]:
        state[m["parent_pointer"]] = m["text"]
c = collections.Counter(state.get(p, "?") for p in ptr)
res["linear_eng_by_state"] = dict(c); res["linear_eng_total"] = len(ptr)
res["linear_eng_open"] = sum(v for k, v in c.items() if k not in ("Done", "Canceled", "Duplicate"))
par = hg("linear", "ENG-", "--key", "parent_id", "--file", "data.json")
tree = {"ENG-2401", "ENG-2403", "ENG-2404", "ENG-2405"}
kids = [ptr[m["parent_pointer"]] for m in par["matches"] if m["text"] in tree and m["parent_pointer"] in ptr]
kids = [k for k in kids if k not in tree]
res["ui_children"] = len(kids)
res["ui_child_states"] = dict(collections.Counter(state.get(p, "?") for p, i in ptr.items() if i in kids))
# GitHub: GameOfDominoes PRs opened from Nov 1, and UI pass PRs
pid = {m["parent_pointer"]: m["text"] for m in hg("github", "GameOfDominoes#", "--key", "id", "--file", "data.json", "--pointer", "/pull_requests")["matches"]}
cr = {}
for q in ("2025-11", "2025-12", "2026-01", "2026-02"):
    for m in hg("github", q, "--key", "created_at", "--file", "data.json", "--pointer", "/pull_requests")["matches"]:
        cr[m["parent_pointer"]] = m["text"]
res["dd_prs_total"] = len(pid)
res["dd_prs_since_nov1"] = sum(1 for p in pid if p in cr)
ui = hg("github", "UI Optimi", "--key", "title", "--file", "data.json", "--pointer", "/pull_requests")["matches"]
res["ui_prs"] = sum(1 for m in ui if m["parent_pointer"] in pid)
# Gmail: Owen's threads in the window
g = hg("gmail", "owen.baker@harmonygames.co/", "--file", "threads/*.json", "--key", "id")
tt = []
for m in g["matches"]:
    n = m["text"].split("/")[-1]
    if n.isdigit():
        tt.append((int(n) >> 20) / 1000)
a = datetime(2025, 11, 1, 8, tzinfo=timezone.utc).timestamp(); b = datetime(2026, 2, 14, tzinfo=timezone.utc).timestamp()
res["owen_gmail_ids"] = len(tt); res["owen_gmail_ids_window"] = sum(1 for t in tt if a <= t < b); res["gmail_scan"] = g.get("scan_complete")
sql = open(os.path.join(WS, "Task_Authoring/task_inputs/01_Universe_Inject.sql")).read()
res["gmail_seed_threads"] = len(re.findall(r"INSERT INTO gmail\.gmail_threads", sql))
# Trello: DD Product Roadmap board
t = hg("trello", "65eb4ec525346c8070ca638f", "--key", "idBoard", "--file", "data.json")
res["dd_board_trello_hits"] = len(t["matches"]); res["dd_board_pointers"] = dict(collections.Counter(m["pointer"].split("/")[1] for m in t["matches"]))
# #god-bugs after the canvas's last line
ev = [x for v in truth.values() if isinstance(v, dict) for x in v.get("evidence", {}).get("Outcome", []) if x.startswith("CE156FDFB428/")]
lines = [v for v in truth.values() if isinstance(v, dict) and v.get("Bug", "")[:1] in "☑☐"]
res["canvas_lines"] = len(lines)
last = 0
for v in lines:
    for x in v.get("evidence", {}).get("Outcome", []):
        if x.startswith("CE156FDFB428/"):
            last = max(last, float(x.split("/")[1]))
res["last_canvas_line_utc"] = datetime.fromtimestamp(last, timezone.utc).isoformat() if last else None
gb = hg("slack", ".", "--file", "messages/C05V5FNLB9V/*.json", "--key", "ts")["matches"]
th = {m["parent_pointer"]: m["text"] for m in hg("slack", ".", "--file", "messages/C05V5FNLB9V/*.json", "--key", "thread_ts")["matches"]}
sub = {}
for w in ("channel_join", "channel_leave", "bot_message", "channel_topic"):
    for m in hg("slack", w, "--file", "messages/C05V5FNLB9V/*.json", "--key", "subtype")["matches"]:
        sub[(m["file"], m["parent_pointer"])] = w
after = [m for m in gb if float(m["text"]) > last]
top = [m for m in after if m["parent_pointer"] not in th or th[m["parent_pointer"]] == m["text"]]
res["god_bugs_after_last_line"] = len(after)
res["god_bugs_top_level_after"] = len(top)
res["god_bugs_top_level_real"] = sum(1 for m in top if (m["file"], m["parent_pointer"]) not in sub)  # corrected in a later keyed pass: pointers repeat across month files, so key by (file, pointer)
json.dump(res, open(os.path.join(HERE, "out", "humantime_volumes2.json"), "w"), indent=1)
print(json.dumps(res)[:1500])

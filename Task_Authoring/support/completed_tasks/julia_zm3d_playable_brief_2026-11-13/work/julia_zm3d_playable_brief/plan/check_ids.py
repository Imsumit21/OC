#!/usr/bin/env python3
"""Collision check of every minted id against the base (tools/hg.py search lookup). Prints hits; exit 1 on any."""
import json, subprocess, sys, tempfile, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import design_model as M
ROOT = "/Users/sumitkumar/Source/Outlier/OC"
os.environ["TASK_AUTHORING_TASK_DIR"] = ROOT + "/Task_Authoring/task_inputs"
def lookup(service, ids, file, pointer=None, key=None):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, dir=ROOT + "/Task_Authoring/support/scratch") as f:
        json.dump(ids, f); name = f.name
    cmd = ["python3", ROOT + "/Task_Authoring/tools/hg.py", "search", "lookup", service, "--ids-file", name, "--file", file]
    if pointer: cmd += ["--pointer", pointer]
    if key: cmd += ["--key", key]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT); os.unlink(name)
    try: j = json.loads(r.stdout)
    except Exception: return {"error": (r.stderr or r.stdout)[-300:]}
    return j
S = M.SEED
checks = [
    ("linear issues", "linear", [M.PACK_TICKET] + [l["ticket"] for l in M.LINES if l["ticket"]], "data.json", "/issues", None),
    ("linear comments", "linear", [M.comment_id("note_" + l["name"]) for l in M.LINES if l["ticket"]], "data.json", "/comments", None),
    ("drive files", "gdrive", [S[k]["id"] for k in ("notes", "tracker", "deck", "c2_sheet", "c4_log")], "data.json", "/drive_files", None),
    ("gcal events", "gcal", [S["hold"]["id"]], "data.json", "/events", "event_id"),
    ("trello actions", "trello", [S["trello_note"]["id"]], "data.json", "/actions", None),
    ("contacts", "contacts", [S["contact"]["id"]], "contacts.json", "/contacts", "contact_id"),
]
slack = [S[k]["id"] for k in ("ask", "picks", "zpicks", "a1_post", "a2_dm", "c3_reply")]
bad = 0
for label, svc, ids, file, pointer, key in checks:
    j = lookup(svc, ids, file, pointer, key)
    m = j.get("matches") or {}
    n = sum(len(v) for v in m.values()) if isinstance(m, dict) else len(m)
    print(f"{label:16} ids {len(ids):3} hits {n} scan_complete={j.get('scan_complete')} {'ERROR ' + str(j.get('error'))[:200] if j.get('error') else ''}")
    bad += (n if isinstance(n, int) else 1) + (1 if j.get("error") else 0)
ids = [M.slack_id(*s.split("/")) for s in slack]
j = lookup("slack", ids, "messages/*.json")
m = j.get("matches") or {}
hits = sum(len(v) for v in m.values()) if isinstance(m, dict) else len(m)
print(f"{'slack message ids':16} ids {len(ids):3} hits {hits} scan_complete={j.get('scan_complete')} {str(j.get('error') or '')[:200]}")
print("minted slack:", dict(zip(slack, ids)))
sys.exit(1 if bad or hits else 0)

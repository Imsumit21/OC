#!/usr/bin/env python3
"""Whole-universe name census with a positive control. Reads through persona_view (all mailboxes and channels, hidden counted) and hg.py."""
import json, re, subprocess, os, sys
env = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True
import build_scenario as B
def pv(svc, q):
    r = subprocess.run(["python3", "Task_Authoring/tools/persona_view.py", "search", "frederick_stone", svc, q, "--limit", "1"], capture_output=True, text=True, env=env, timeout=170)
    m = re.search(r"visible hits=(\d+).*hidden by ACL=(\d+)", r.stdout)
    return (int(m[1]), int(m[2])) if m else None
def hg(svc, q):
    r = subprocess.run(["python3", "Task_Authoring/tools/hg.py", "search", "search", svc, q, "--limit", "3"], capture_output=True, text=True, env=env, timeout=170)
    try: return len(json.loads(r.stdout).get("matches", []))
    except Exception: return None
names = [m["key"].split()[0] for m in B.M if not m.get("base")] + ["Kestrel"]
people = sorted({p for m in B.M if m.get("person") for p in (m["person"][0] + " " + m["person"][1],)})
out = {"positive_control": {"Balancy": {"gmail": pv("gmail", "Balancy"), "slack": pv("slack", "Balancy")}, "Frederick Stone": {"contacts": hg("contacts", "Frederick"), "trello": hg("trello", "Frederick Stone")}}}
for q in names + people:
    out[q] = {"gmail": pv("gmail", q), "slack": pv("slack", q), "contacts": hg("contacts", q), "trello": hg("trello", q), "linear": hg("linear", q), "gdocs": hg("gdocs", q), "gcal": hg("gcal", q)}
    print(q, out[q], flush=True)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "name_census.json"), "w"), indent=1)

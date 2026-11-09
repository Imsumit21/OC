#!/usr/bin/env python3
"""Runs persona_view.py search for each brief §5 fact as owen_baker and saves the outputs in plan/sap/ (brief §5a)."""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")
Q = [("F1", "slack", "BoomBit sync"), ("F2", "gdocs", "carry-over notes"), ("F3", "linear", "UI Changes Master Ticket"), ("F4", "trello", "UI optimization"),
     ("F5", "slack", "train level backgrounds"), ("F6", "slack", "mega tile"), ("F7", "slack", "shop icons"), ("F8", "slack", "Tavern buttons"),
     ("F9", "slack", "no lives"), ("F10", "gdocs", "economy"), ("F11", "slack", "Win & Collect"), ("F12", "github", "Fixing window in tile dozer"),
     ("F13", "slack", "tile dozer window"), ("F14", "slack", "flickering"), ("F15", "slack", "acid"), ("F16", "slack", "bottom bar"),
     ("F17", "gmail", "sign in"), ("F18", "linear", "Sign-In Account"), ("F19", "linear", "stuck at splash"), ("F20", "github", "Mini-Games UI Optimization"),
     ("F21", "github", "Axe Arena - UI Optimization"), ("F22", "linear", "Season Pass - UI Optimization"), ("F23", "linear", "Daily Gift UI Optimization"),
     ("F24", "gslides", "UI optimization"), ("F25", "gsheets", "UI pass"), ("F26", "trello", "Screens checked"), ("F27", "gdocs", "bug list notes"),
     ("F28", "trello", "close-outs"), ("F29", "gcal", "bug review"), ("F30", "gdrive", "carry-over"), ("F31", "slack", "snow train"),
     ("F32", "slack", "navigation bar"), ("F33", "slack", "lives are not decreased"), ("F34", "slack", "published a new build"), ("F35", "slack", "sub-250")]
out = {}
for fid, svc, q in Q:
    a = ["python3", "Task_Authoring/tools/persona_view.py", "search", "owen_baker", svc, q, "--limit", "3"]
    if svc in ("slack", "gmail"):
        a.append("--no-hidden")
    try:
        r = subprocess.run(a, cwd=WS, env=ENV, capture_output=True, text=True, timeout=280)
        t = r.stdout
    except subprocess.TimeoutExpired:
        t = f"SEARCH {svc} {q!r} as owen_baker  scope: timed out after 280s\n"
    open(os.path.join(HERE, "sap", f"{fid}.txt"), "w").write(t)
    m = re.search(r"visible hits=(\d+).*?hidden by ACL=(\S+)", t)
    out[fid] = {"service": svc, "query": q, "visible": m.group(1) if m else "?", "hidden": m.group(2) if m else "?"}
    print(fid, svc, q, out[fid]["visible"], out[fid]["hidden"], flush=True)
json.dump(out, open(os.path.join(HERE, "sap", "summary.json"), "w"), indent=1)

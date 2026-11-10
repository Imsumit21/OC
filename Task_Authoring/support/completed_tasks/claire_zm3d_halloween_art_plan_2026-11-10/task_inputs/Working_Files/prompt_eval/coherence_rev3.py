#!/usr/bin/env python3
"""Coherence checks the prompt stage owns (Eval 1 §3.2) on the records rev3 added or moved. Reads the SQL as text and the base
through tools/hg.py and tools/persona_view.py; never executes SQL. Run from the workspace root:

    TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputsN2 python3 -B Task_Authoring/task_inputsN2/Working_Files/prompt_eval/coherence_rev3.py
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
ROOT = TASK.parents[1]
sys.path.insert(0, str(ROOT / "Task_Authoring" / "tools"))
from base_check import parse_sql  # noqa: E402

ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(TASK.relative_to(ROOT)))
HG = ROOT / "Task_Authoring" / "tools" / "hg.py"


def hg(*a):
    r = subprocess.run([sys.executable, "-B", str(HG), "search", *a], capture_output=True, text=True, cwd=str(ROOT), env=ENV, timeout=300)
    return json.loads(r.stdout)


rows = parse_sql((TASK / "01_Universe_Inject.sql").read_text())
msgs = [r["row"] for r in rows if r["op"] == "insert" and r["table"] == "slack.slack_messages"]
channels = {c["id"]: c for c in json.loads(hg("get", "slack", "--file", "channels.json", "--max-chars", "4000000")["text"])}
users = {u["id"]: u for u in json.loads(hg("get", "slack", "--file", "users.json", "--max-chars", "4000000")["text"])}


def utc(ts):
    return datetime.fromtimestamp(float(ts), timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


bad = 0
print("seeded Slack messages:", len(msgs))
for m in sorted(msgs, key=lambda x: float(x["ts"])):
    ch = channels[m["channel_id"]]
    u = m.get("user") or m.get("user_id")
    member = u in (ch.get("members") or [])
    parent = m.get("thread_ts_legacy") or m.get("thread_ts")
    order = "" if not parent or parent == m["ts"] or float(parent) < float(m["ts"]) else " REPLY BEFORE PARENT"
    bad += (not member) + bool(order)
    print(f'  {m["channel_id"]}/{m["ts"]} {utc(m["ts"])} #{ch.get("name")} author {(users.get(u) or {}).get("real_name", u)} member={member}{order}')
print("latest seeded Slack ts:", utc(max(float(m["ts"]) for m in msgs)), "| seed bound 2025-10-01T00:00:00Z")
for b in ("#1896", "#1935", "#1966", "#1452", "#1529"):
    d = hg("search", "slack", f"Android {b}", "--limit", "5") if False else hg("search", "slack", b, "--limit", "6")
    hits = [(m["file"].split("/messages/")[-1], m["text"][:90].replace("\n", " ")) for m in d["matches"]]
    print("base", b, len(hits), hits[:3])
print("VERDICT:", "PASS" if not bad else f"{bad} PROBLEM(S)")

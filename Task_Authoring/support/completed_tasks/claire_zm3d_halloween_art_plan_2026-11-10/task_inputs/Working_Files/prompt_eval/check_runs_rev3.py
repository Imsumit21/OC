#!/usr/bin/env python3
"""Mechanical runs behind 04_Prompt_Check.md for the unchanged prompt on rev3: prompt identity, tool-name scan, scripted-order
and first-person scans, every premise identifier looked up through tools/hg.py and the SQL, per-deliverable catalog check.
Writes prompt_eval/check_runs_rev3.txt. Read-only on the universe; never executes SQL. From the workspace root:

    TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputsN2 python3 -B Task_Authoring/task_inputsN2/Working_Files/prompt_eval/check_runs_rev3.py
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
ROOT = TASK.parents[1]
sys.path.insert(0, str(ROOT / "Task_Authoring" / "tools"))
from base_check import parse_sql  # noqa: E402

ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(TASK.relative_to(ROOT)))
TOOLS = ROOT / "Task_Authoring" / "tools"
out = []


def say(*a):
    out.append(" ".join(str(x) for x in a))


def tool(script, *a, timeout=300):
    r = subprocess.run([sys.executable, "-B", str(TOOLS / script), *a], capture_output=True, text=True, cwd=str(ROOT), env=ENV, timeout=timeout)
    return r.stdout


def get(service, file, pointer=None, n=4000000):
    args = ["search", "get", service, "--file", file, "--max-chars", str(n)] + (["--pointer", pointer] if pointer else [])
    return json.loads(json.loads(tool("hg.py", *args))["text"])


raw = (TASK / "04_Prompt.txt").read_bytes()
prompt = raw.decode()
say("## prompt identity")
say("bytes", len(raw), "words", len(prompt.split()), "sha256", hashlib.sha256(raw).hexdigest())
say("expected sha256 63d7c071... :", hashlib.sha256(raw).hexdigest().startswith("63d7c071"))

say("\n## C14 tool-name scan (catalog names, server words, parameter names as written)")
cat = json.loads((ROOT / "Evals/references/tools/catalog.json").read_text())
names = [t["name"] for t in cat]
hits = [n for n in names if re.search(rf"(?<![\w]){re.escape(n)}(?![\w])", prompt)]
say("catalog tools", len(names), "named in the prompt:", hits)
for w in ("MCP", "tool", "linear_", "gmail_", "slack_", "gdrive_", "gsheets_", "gdocs_", "trello_", "API", "function", "endpoint"):
    say(f"  {w!r}:", len(re.findall(rf"\b{re.escape(w)}", prompt, re.I)))
params = sorted({p for t in cat for p in ((t.get("parameters") or {}) if isinstance(t.get("parameters"), dict) else [])})
camel = [p for p in params if re.search(r"[A-Z_]", p) and re.search(rf"\b{re.escape(p)}\b", prompt)]
say("camelCase or snake_case parameter names in the prompt:", camel)

say("\n## C15 / C7 scans")
for w in ("First", "Then", "Finally", "next", "after that", "step"):
    say(f"  {w!r}:", len(re.findall(rf"\b{w}\b", prompt, re.I)))
say("  first-person action phrases:", re.findall(r"\bI(?:'ll|'m going to| need to| want to| will)\b[^.,]*", prompt), "| I'm:", re.findall(r"\bI'm [a-z]+", prompt))
say("  conditional words if/unless/but not/then also:", re.findall(r"\b(?:if|unless|but not|then also)\b", prompt, re.I))

say("\n## C17 premises")
rows = [r for r in parse_sql((TASK / "01_Universe_Inject.sql").read_text()) if r["op"] == "insert"]
ask = next(r["row"] for r in rows if r["table"] == "slack.slack_messages" and r["row"]["ts"] == "1759269913.882683")
say("ask:", ask["channel_id"], ask["ts"], "reply_count", ask.get("reply_count"), "mentions Claire:", "EMPLOYEE_0009_SLACK_ID" in ask["text"], "| text head:", ask["text"][:90].replace("\n", " "))
replies = [r["row"]["ts"] for r in rows if r["table"] == "slack.slack_messages" and (r["row"].get("thread_ts_legacy") or r["row"].get("thread_ts")) == "1759269913.882683" and r["row"]["ts"] != "1759269913.882683"]
say("seeded replies under the ask:", replies)
ch = {c["id"]: c for c in get("slack", "channels.json")}
for cid in ("C06DJBJL798", "C08R8CHB0QL", "C0880U9751A", "C09ATAJ220H", "C05KNDCHAAG"):
    c = ch[cid]
    say(f'channel {cid} #{c.get("name")} private={c.get("is_private")} members={len(c.get("members") or [])} Claire in={"EMPLOYEE_0009_SLACK_ID" in (c.get("members") or [])} purpose={str((c.get("purpose") or {}).get("value") if isinstance(c.get("purpose"), dict) else c.get("purpose"))[:50]!r}')
ev = next(r["row"] for r in rows if r["table"] == "gcal.gcal_events" and r["row"].get("calendar_id") == "claire.morgan@harmonygames.co")
att = json.loads(ev["attendees_json"])
say("review:", ev.get("event_id"), ev.get("summary"), ev.get("start_time") or ev.get("start_datetime") or ev.get("start_at"), "status", ev.get("status"), "description:", ev.get("description"))
say("attendees:", [(a["email"], a.get("responseStatus")) for a in att])
say("Julia on the review:", any("julia" in a["email"] for a in att))
lin = get("linear", "data.json", "/team_memberships")
for name, uid in (("Claire", "usr_7fe31e7ec8199618"), ("Marcus Bennett", "usr_c77c50cc15c5342d"), ("Julia Lawson", "usr_8140f09bf9f1b94c"), ("Martin Walsh", "usr_51f5f16d46e8cf55")):
    say(f"linear {name} {uid} in team_ART:", any(m["team_id"] == "team_ART" and m["user_id"] == uid for m in lin))
say("seeded ART tickets:", sum(1 for r in rows if r["table"] == "linear.linear_issues"), "comments:", sum(1 for r in rows if r["table"] == "linear.linear_comments"))

say("\n## C18 catalog: every write and read the path needs exists")
need = ["gdocs_create_document", "gsheets_create_spreadsheet", "gsheets_values_update", "gdrive_share_file", "linear_create_comment", "linear_update_issue",
        "linear_create_issue", "slack_send_message", "slack_read_channel", "slack_read_thread", "slack_search_public_and_private", "gmail_search_messages",
        "gmail_get_message", "trello_search", "trello_get_comments", "linear_list_comments", "linear_list_issues", "linear_list_users", "gdrive_search",
        "gdrive_list_folder", "gsheets_values_batch_get", "gdocs_get_document_text", "gslides_get_presentation_text", "gcal_get_event"]
say("missing from the catalog:", [n for n in need if n not in names], f"({len(need)} checked)")
calls = [json.loads(line) for line in (WF / "run_forensics/rev2/precheck/calls.jsonl").open()]
for n in ("gdrive_share_file", "linear_update_issue", "linear_create_comment", "linear_create_issue", "slack_send_message", "gsheets_create_spreadsheet", "gdocs_create_document"):
    cs = [c for c in calls if c["tool"].endswith(n)]
    say(f"rev2 pre-check {n}: {len(cs)} calls, {sum(1 for c in cs if c.get('error') or c.get('failed'))} failed")
say("share roles used:", sorted({c["input"].get("role") for c in calls if c["tool"].endswith("gdrive_share_file")}))

(HERE / "check_runs_rev3.txt").write_text("\n".join(out) + "\n")
print("\n".join(out))

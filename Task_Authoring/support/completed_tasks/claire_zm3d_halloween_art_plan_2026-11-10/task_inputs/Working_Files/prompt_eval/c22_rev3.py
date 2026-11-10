#!/usr/bin/env python3
"""Evidence for the C22 re-test: Leonard's base post against the seeded review. Reads the SQL as text and the base through
tools/hg.py; never executes SQL. Writes prompt_eval/c22_rev3.txt. From the workspace root:

    TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputsN2 python3 -B Task_Authoring/task_inputsN2/Working_Files/prompt_eval/c22_rev3.py
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
L, C = "leonard.hayes@harmonygames.co", "claire.morgan@harmonygames.co"
out = []


def say(*a):
    out.append(" ".join(str(x) for x in a))


def get(service, file, pointer=None):
    args = ["search", "get", service, "--file", file, "--max-chars", "400000000"] + (["--pointer", pointer] if pointer else [])
    r = subprocess.run([sys.executable, "-B", str(ROOT / "Task_Authoring/tools/hg.py"), *args], capture_output=True, text=True, cwd=str(ROOT), env=ENV)
    return json.loads(json.loads(r.stdout)["text"])


rows = [r for r in parse_sql((TASK / "01_Universe_Inject.sql").read_text()) if r["op"] == "insert"]
ev = next(r["row"] for r in rows if r["table"] == "gcal.gcal_events" and r["row"].get("calendar_id") == C)
att = {a["email"]: a.get("responseStatus") for a in json.loads(ev["attendees_json"])}
say("## the seeded review (Claire's copy)")
say("id", ev["event_id"], "| status", ev["status"], "| created", ev["created"], "| updated", ev["updated"], "| sequence", ev.get("sequence"))
say("start", ev["start_ts"], "| hangout_link present:", bool(ev.get("hangout_link")), "| Leonard's response:", att.get(L))
say("description:", ev["description"])
say("all 7 copies carry it:", sum(1 for r in rows if r["table"] == "gcal.gcal_events" and r["row"].get("description") == ev["description"]))

say("\n## Leonard's base post")
msgs = get("slack", "messages/C05KNDCHAAG/2025-10.json")
post = next(m for m in msgs if m["ts"] == "1759279503.256079")
at = datetime.fromtimestamp(float(post["ts"]), timezone.utc)
say("C05KNDCHAAG/1759279503.256079", at.strftime("%Y-%m-%dT%H:%M:%SZ"), "| text:", post["text"])
upd = datetime.strptime(ev["updated"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
say("post is after the event's last update by", at - upd, "| replies:", post.get("reply_count"))

say("\n## standing meetings on Claire's own calendar on the two days the post names (no end date on the series)")
events = get("gcal", "data.json", "/events")


def start(e):
    s = e.get("start") or {}
    return (s.get("dateTime") or s.get("date") or "") if isinstance(s, dict) else str(s)


def runs_on(e, day):
    rule = " ".join(e.get("rrule") or [])
    until = re.search(r"UNTIL=(\d{8})", rule)
    byday = re.search(r"BYDAY=([A-Z0-9,-]+)", rule)
    return bool(rule) and not (until and until.group(1) < "20251001") and bool(byday) and day in byday.group(1).split(",") and start(e)[:4] == "2025"


for day, name in (("WE", "Wed Oct 1"), ("TH", "Thu Oct 2")):
    series = {}
    for e in events:
        if e.get("calendar_id") == C and runs_on(e, day):
            series[e["summary"]] = max(series.get(e["summary"], ""), start(e)[:10])
    say(name, "series started in 2025:", sorted(series.items()))
inst = [(e["event_id"], start(e)[:16], e["summary"]) for e in events if e.get("calendar_id") == C and start(e)[:10] in ("2025-10-01", "2025-10-02")]
say("expanded instances on Claire's calendar for those two days:", inst)

say("\n## Leonard's calendar: did he change anything about the review, and is LA consistent")
say("Leonard's own base events Oct 1-2:", [(start(e)[:16], e.get("summary"), e.get("created")) for e in events if e.get("calendar_id") == L and start(e)[:10] in ("2025-10-01", "2025-10-02")])

say("\n## how the studio uses the phrase, and whether the trip is on record before the description")
for f, ptr in (("messages/D04UP2L3E3S/2024-07.json", "/117"), ("messages/C04UTBZL6AX/2024-04.json", "/590"), ("messages/C05TNSRRLLW/2023-10.json", "/15")):
    m = get("slack", f, ptr)
    say(f.split("/")[1] + "/" + m["ts"], m.get("user"), "|", m.get("text", "")[:150].replace("\n", " "))
r = subprocess.run([sys.executable, "-B", str(ROOT / "Task_Authoring/tools/hg.py"), "search", "search", "slack", "flying to LA", "--limit", "10"],
                   capture_output=True, text=True, cwd=str(ROOT), env=ENV)
hits = [m for m in json.loads(r.stdout)["matches"] if m["pointer"].endswith("/text")]
say("'flying to LA' in all of Slack:", len(hits), "hit(s):", [m["file"].split("/messages/")[-1] for m in hits])
say("seed bound 2025-10-01T00:00:00Z is before the post, so no seeded record can be dated after it")
(HERE / "c22_rev3.txt").write_text("\n".join(out) + "\n")
print("\n".join(out))

"""Print a Slack window through hg.py. Usage: slackdump.py <channel> <month> <from_utc> <to_utc> [maxchars]
Dates like 2025-09-23T00. Read-only; goes through Task_Authoring/tools/hg.py."""
import datetime as dt
import json
import subprocess
import sys

ch, month, a, b = sys.argv[1:5]
mx = int(sys.argv[5]) if len(sys.argv) > 5 else 260
o = subprocess.run(["python3", "Task_Authoring/tools/hg.py", "search", "get", "slack", "--file",
                    f"messages/{ch}/{month}.json", "--max-chars", "9000000"],
                   capture_output=True, encoding="utf8").stdout
rows = json.loads(json.loads(o)["text"])
print(len(rows), "rows")
for m in rows:
    t = dt.datetime.fromtimestamp(float(m["ts"]), dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    if a <= t <= b + "~":
        txt = m.get("text") or ""
        if not txt and m.get("attachments"):
            txt = "[att] " + (m["attachments"][0].get("fallback") or "")
        thr = m.get("thread_ts")
        print(t, m["ts"], (m.get("user") or "bot")[:13], f"rc{m.get('reply_count')}", f"th={thr}" if thr else "",
              "|", txt[:mx].replace("\n", " / "))

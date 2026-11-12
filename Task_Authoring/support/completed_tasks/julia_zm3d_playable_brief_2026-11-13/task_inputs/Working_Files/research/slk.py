#!/usr/bin/env python3
"""Read one Slack channel's month files through Task_Authoring/tools/hg.py and print compact lines (read-only).

usage: python3 slk.py <channel_id> <month[,month...]> [width=260] [regex]
  e.g. python3 slk.py C090N54TG79 2025-09 400
       python3 slk.py C0880U9751A 2025-09 300 'memory|model|texture'
Each line: UTC date time, ts, user (E#### = EMPLOYEE_####, P#### = PERSON_####), thread marker, files, text.
  [rN]   = thread root with N replies        ↳<ts> = reply under the thread root <ts>
A record pointer is <channel_id>/<ts>.
"""
import json, subprocess, sys, os, datetime, re
ROOT = "/Users/sumitkumar/Source/Outlier/OC"
os.environ["TASK_AUTHORING_TASK_DIR"] = ROOT + "/Task_Authoring/task_inputs"
def get(service, file):
    out = ""; off = 0
    while True:
        cmd = ["python3", ROOT + "/Task_Authoring/tools/hg.py", "search", "get", service, "--file", file]
        if off: cmd += ["--offset", str(off)]
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
        if r.returncode != 0:
            sys.stderr.write(r.stderr[-300:]); return None
        j = json.loads(r.stdout); out += j["text"]
        if j.get("truncated") and j.get("next_offset"): off = j["next_offset"]
        else: break
    return out
def main():
    chan = sys.argv[1]; months = sys.argv[2].split(","); width = int(sys.argv[3]) if len(sys.argv) > 3 else 260
    pat = re.compile(sys.argv[4], re.I) if len(sys.argv) > 4 else None
    for m in months:
        t = get("slack", f"messages/{chan}/{m}.json")
        if t is None: print("MISSING", chan, m); continue
        msgs = json.loads(t); msgs.sort(key=lambda x: float(x["ts"]))
        for x in msgs:
            txt = (x.get("text") or "").replace("\n", " ⏎ ")
            if pat and not pat.search(txt): continue
            d = datetime.datetime.fromtimestamp(float(x["ts"]), datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")
            u = (x.get("user") or "bot").replace("_SLACK_ID", "").replace("EMPLOYEE_", "E").replace("PERSON_", "P")
            th = ""
            if x.get("thread_ts") and x["thread_ts"] != x["ts"]: th = " ↳" + x["thread_ts"]
            elif x.get("reply_count"): th = f" [r{x['reply_count']}]"
            f = " 📎" + ",".join((ff.get("name") or ff.get("title") or "?")[:40] for ff in x.get("files", [])) if x.get("files") else ""
            print(f"{d} {x['ts']} {u}{th}{f}: {txt[:width]}")
main()

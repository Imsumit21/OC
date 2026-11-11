#!/usr/bin/env python3
"""Fetch one Slack channel-month through tools/hg.py and print a compact transcript.

Usage: slack_month.py <channel_id> <YYYY-MM> [--grep WORD] [--full]
Reads only through Task_Authoring/tools/hg.py (search get); caches the raw JSON under research/raw/.
"""
import json, os, subprocess, sys, datetime, re

ROOT = "/Users/sumitkumar/Source/Outlier/OC"
RAW = os.path.join(ROOT, "Task_Authoring/task_inputsS/Working_Files/research/raw")
NAMES = json.load(open(os.path.join(RAW, "slack_names.json")))


def fetch(ch, month):
    out = os.path.join(RAW, f"slack_{ch}_{month}.json")
    if os.path.exists(out):
        return json.load(open(out))
    env = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputsS")
    text, offset = "", 0
    while True:
        cmd = ["python3", "Task_Authoring/tools/hg.py", "search", "get", "slack", "--file",
               f"messages/{ch}/{month}.json", "--max-chars", "600000"]
        if offset:
            cmd += ["--offset", str(offset)]
        r = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, text=True)
        d = json.loads(r.stdout)
        text += d["text"]
        if not d.get("truncated"):
            break
        offset = d["next_offset"]
    msgs = json.loads(text)
    json.dump(msgs, open(out, "w"))
    return msgs


def main():
    ch, month = sys.argv[1], sys.argv[2]
    grep = None
    full = "--full" in sys.argv
    if "--grep" in sys.argv:
        grep = sys.argv[sys.argv.index("--grep") + 1].lower()
    msgs = fetch(ch, month)
    for m in sorted(msgs, key=lambda x: float(x.get("ts", 0))):
        t = m.get("text", "") or ""
        if grep and grep not in t.lower():
            continue
        ts = float(m["ts"])
        dt = datetime.datetime.utcfromtimestamp(ts).strftime("%m-%d %H:%MZ")
        who = NAMES.get(m.get("user"), m.get("user"))
        thr = m.get("thread_ts")
        tag = ""
        if thr and thr != m["ts"]:
            tag = f" [reply to {thr}]"
        elif m.get("reply_count"):
            tag = f" [thread {m.get('reply_count')} replies]"
        body = t if full else re.sub(r"\s+", " ", t)[:400]
        print(f"{m['ts']} {dt} {who}{tag}: {body}")


if __name__ == "__main__":
    main()

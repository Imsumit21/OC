#!/usr/bin/env python3
"""Read every message in Claire's visible Slack channels for the window (read-only).

Visible channel list comes from persona_view.py reach --json; message files are read with
hg.py search get, finishing every page. argv[1] = scratch output directory.
"""
import concurrent.futures as cf
import datetime as dt
import json
import os
import subprocess
import sys
from pathlib import Path

WS = Path("/Users/sumit/Source/OC")
PY = os.path.expanduser("~/.local/bin/python3.12")
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputsN2", PYTHONDONTWRITEBYTECODE="1")
OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
MONTHS = ("2025-09", "2025-10")


def hg(*a):
    r = subprocess.run([PY, "-B", "Task_Authoring/tools/hg.py", "search", *a], capture_output=True, text=True,
                       cwd=str(WS), env=ENV)
    return r


def read_file(path):
    text, off, pages = "", 0, 0
    while True:
        r = hg("get", "slack", "--file", path, "--offset", str(off), "--max-chars", "2000000", "--compact")
        d = json.loads(r.stdout)
        text += d["text"]
        pages += 1
        if not d.get("truncated"):
            return json.loads(text), pages
        off = d["next_offset"]


def main():
    r = subprocess.run([PY, "-B", "Task_Authoring/tools/persona_view.py", "reach", "claire_morgan", "--top", "400",
                        "--json"], capture_output=True, text=True, cwd=str(WS), env=ENV)
    reach = json.loads(r.stdout)
    sl = reach["services"]["slack"]
    chans = {c["id"]: c for c in sl["top_channels"]}
    if not chans:
        raise SystemExit("no channels in reach: " + json.dumps(sl)[:400])
    (OUT / "chans.json").write_text(json.dumps(chans))
    files = []
    for m in MONTHS:
        d = json.loads(hg("files", "slack", f"/{m}.json", "--limit", "5000", "--compact").stdout)
        assert not d.get("truncated")
        for x in d["matches"]:
            cid = x["path"].split("/")[1]
            if cid in chans:
                files.append(x["path"])
    msgs, stats = [], {}
    with cf.ThreadPoolExecutor(6) as ex:
        for path, (arr, pages) in zip(files, ex.map(read_file, files)):
            cid = path.split("/")[1]
            stats[path] = {"n": len(arr), "pages": pages}
            for i, m in enumerate(arr):
                msgs.append({"c": cid, "name": chans[cid].get("name"), "kind": chans[cid].get("kind"), "file": path,
                             "ptr": f"/{i}", "ts": m.get("ts"), "user": m.get("user"), "tt": m.get("thread_ts"),
                             "rc": m.get("reply_count"), "text": m.get("text") or "",
                             "files": [f.get("name") or f.get("title") for f in (m.get("files") or []) if isinstance(f, dict)],
                             "att": [" ".join(str(a.get(k) or "") for k in ("pretext", "title", "text", "fallback"))
                                     for a in (m.get("attachments") or []) if isinstance(a, dict)],
                             "sub": m.get("subtype")})
    (OUT / "msgs.json").write_text(json.dumps(msgs))
    (OUT / "stats.json").write_text(json.dumps(stats))
    print(len(files), "files", len(msgs), "messages")


if __name__ == "__main__":
    main()

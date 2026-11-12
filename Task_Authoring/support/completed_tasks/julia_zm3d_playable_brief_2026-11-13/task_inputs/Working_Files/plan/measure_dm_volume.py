#!/usr/bin/env python3
"""Count base Slack messages in a conversation for 22 to 30 Sep 2025 (UTC days) through tools/hg.py (read-only) and record
the count in out/humantime_volumes.json under slack.<channel>.windows['22 to 30 Sep']. Method: `hg.py search search slack 17
--key ts --file messages/<channel>/2025-09.json` (every ts starts with 17), the same as the worksheet's other windows; the
script first reproduces the count already recorded for Julia's DM with Claire (25) and refuses to write if it cannot, or if
the scan is incomplete. Usage: python3 -B measure_dm_volume.py D05GU6L0XFH"""
import datetime as D, json, os, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; TASK = HERE.parents[1]; ROOT = TASK.parents[1]
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(TASK))
A = D.datetime(2025, 9, 22, tzinfo=D.timezone.utc).timestamp(); B = D.datetime(2025, 10, 1, tzinfo=D.timezone.utc).timestamp()
def window(ch):
    p = subprocess.run([sys.executable, "-B", str(TASK.parent / "tools" / "hg.py"), "search", "search", "slack", "17", "--key", "ts",
                        "--file", f"messages/{ch}/2025-09.json", "--limit", "5000", "--compact"], capture_output=True, text=True, cwd=ROOT, env=ENV)
    d = json.loads(p.stdout)
    assert d.get("scan_complete") is True, (ch, "scan incomplete")
    ts = [float(m["text"]) for m in d["matches"]]
    return sum(1 for t in ts if A <= t < B), len(ts)
c, _ = window("D05HMBQUC8Z")
assert c == 25, f"cannot reproduce the recorded count of 25 for D05HMBQUC8Z (got {c})"
ch = sys.argv[1]
n, total = window(ch)
vp = HERE / "out" / "humantime_volumes.json"; vol = json.loads(vp.read_text())
e = vol["slack"].setdefault(ch, {"name": f"DM {ch}", "scan_complete": True, "error": None, "windows": {}})
e["windows"]["22 to 30 Sep"] = n; e["total_sep_2025"] = total
vp.write_text(json.dumps(vol, indent=1) + "\n")
print(f"{ch} 22 to 30 Sep: {n} (September {total}); check D05HMBQUC8Z = {c}")

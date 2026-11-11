"""Check every seeded Slack reply's thread_parent_id against a real row: a seeded row or the base row's own id field.
Read-only; base reads go through Task_Authoring/tools/hg.py records. Writes plan/out/parent_check.json."""
import datetime as dt
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import data as D

seeded = {(ch, ts): row for _k, ch, ts, row, _w, _t, _r in D.SLACK_ROWS}
seeded[(D.CH_PRS, D.PR["mirror_rc27"]["ts"])] = D.PR["mirror_rc27"]["row"]
replies = [(k, ch, root) for k, ch, _ts, _row, _w, _t, root in D.SLACK_ROWS if root]
replies.append(("mirror_rc27", D.CH_PRS, D.PR["mirror_rc27"]["root"]))

base_needed = sorted({(ch, root) for _k, ch, root in replies if (ch, root) not in seeded})
checks = []
for i, (ch, root) in enumerate(base_needed):
    month = dt.datetime.fromtimestamp(float(root), dt.timezone.utc).strftime("%Y-%m")
    checks.append({"id": f"r{i}", "service": "slack", "file": f"messages/{ch}/{month}.json", "pointer": "", "field": "ts",
                   "values": [root]})
req = HERE / "out" / "parent_check_req.json"
req.write_text(json.dumps({"checks": checks}))
env = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs", MSYS_NO_PATHCONV="1")
r = subprocess.run([sys.executable, "-B", "Task_Authoring/tools/hg.py", "records", "--request", str(req)], cwd=ROOT, env=env,
                   capture_output=True, text=True, encoding="utf8")
d = json.loads(r.stdout)
base = {}
for i, (ch, root) in enumerate(base_needed):
    c = d["checks"][f"r{i}"]
    m = c.get("matches") or []
    base[(ch, root)] = {"scan_complete": c.get("scan_complete"), "found": len(m),
                        "id_field": (m[0]["record"].get("id") if m else None), "has_id": bool(m and "id" in m[0]["record"])}

out = []
for k, ch, root in replies:
    minted = D.row_id(ch, root)
    if (ch, root) in seeded:
        real, src = seeded[(ch, root)], "seeded"
    else:
        b = base[(ch, root)]
        real, src = b["id_field"], f"base found={b['found']} has_id={b['has_id']} scan_complete={b['scan_complete']}"
    raw = (ch, root) in D.RAW_ROOTS
    # A raw-shape root has no id; the emitter must then key the parent on channel and ts, never a minted id.
    out.append({"key": k, "channel": ch, "root": root, "minted_parent": minted, "real_id": real, "source": src,
                "in_RAW_ROOTS": raw, "ok": real is not None and minted == real,
                "emitted_as": "subquery on channel_id and ts" if raw else "literal id"})
(HERE / "out" / "parent_check.json").write_text(json.dumps(out, indent=1), encoding="utf8")
for o in out:
    print("OK " if o["ok"] else "BAD", o["key"], o["channel"], o["root"], o["minted_parent"], "real", o["real_id"], o["source"],
          o["emitted_as"])
print("minted parent ids with no real row:", [o["key"] for o in out if not o["ok"]])
print("unhandled (bad and not emitted as subquery):", [o["key"] for o in out if not o["ok"] and not o["in_RAW_ROOTS"]])

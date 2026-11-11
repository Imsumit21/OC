"""Re-read the load-bearing base values through tools/hg.py records (GEN_EXECUTION 6a.3). Writes plan/out/reverify.txt."""
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
env = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs", MSYS_NO_PATHCONV="1")
req = HERE / "out" / "reverify_req.json"
req.write_text(json.dumps({"checks": [
    {"id": "zd", "service": "slack", "file": "messages/C090N54TG79/2025-09.json", "pointer": "", "field": "ts",
     "values": ["1758517286.431379", "1758581651.167799", "1758691397.679889", "1759165414.829399", "1759176983.189479"]},
    {"id": "builds", "service": "slack", "file": "messages/C05433XK267/2025-09.json", "pointer": "", "field": "ts",
     "values": ["1758803475.436309", "1758575557.575349"]},
    {"id": "rob", "service": "slack", "file": "messages/D05GU6L0XFH/2025-09.json", "pointer": "", "field": "ts", "values": ["1758901945.292269"]},
    {"id": "lin", "service": "linear", "file": "data.json", "pointer": "/issues", "field": "identifier", "values": ["ZOM-559", "ZOM-566"]},
    {"id": "pr", "service": "github", "file": "data.json", "pointer": "/pull_requests", "field": "number", "values": [476]},
]}))
r = subprocess.run([sys.executable, "-B", "Task_Authoring/tools/hg.py", "records", "--request", str(req)], cwd=ROOT, env=env,
                   capture_output=True, text=True, encoding="utf8")
d = json.loads(r.stdout)
L = ["Read through `hg.py records` in this session (scan_complete true on each check):", ""]
for cid, c in d["checks"].items():
    assert c.get("scan_complete") is True, cid
    for m in c.get("matches") or []:
        x = m["record"]
        if cid in ("zd", "builds", "rob"):
            att = x.get("attachments") or []
            text = str(x.get("text") or "") or str((att[0] if att else {}).get("fallback") or "") + " " + str((att[0] if att else {}).get("text") or "")
            ch = {"zd": "C090N54TG79", "builds": "C05433XK267", "rob": "D05GU6L0XFH"}[cid]
            L.append(f"- {ch}/{x.get('ts')}: reply_count {x.get('reply_count', 0)}, text starts {text[:110]!r}".replace("\n", " "))
        elif cid == "lin":
            L.append(f"- {x.get('identifier')}: state {x.get('state_id') or x.get('state')}, created {x.get('created_at')}")
        else:
            L.append(f"- {x.get('id')}: state {x.get('state')}, merged {x.get('merged')}, updated {x.get('updated_at')}")
(HERE / "out" / "reverify.txt").write_text("\n".join(L) + "\n", encoding="utf8")
print("\n".join(L))

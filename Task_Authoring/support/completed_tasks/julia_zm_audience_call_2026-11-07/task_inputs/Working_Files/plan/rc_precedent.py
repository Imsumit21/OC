"""Base precedent for a bot reply with no review row of its own, read through tools/hg.py records."""
import collections
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
env = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs", MSYS_NO_PATHCONV="1")
PRS = [f"harmonygames-Games/match3d#{n}" for n in (470, 466, 463, 460, 455)]
req = HERE / "out" / "rc_req.json"
req.write_text(json.dumps({"checks": [{"id": "rc", "service": "github", "file": "data.json", "pointer": "/review_comments", "field": "pr_id", "values": PRS},
                                      {"id": "rev", "service": "github", "file": "data.json", "pointer": "/reviews", "field": "pr_id", "values": PRS}]}))
r = subprocess.run([sys.executable, "-B", "Task_Authoring/tools/hg.py", "records", "--request", str(req)], cwd=ROOT, env=env, capture_output=True, text=True, encoding="utf8")
d = json.loads(r.stdout)
rc = [m["record"] for m in d["checks"]["rc"]["matches"]]
rev = [m["record"] for m in d["checks"]["rev"]["matches"]]
print(len(rc), collections.Counter(x.get("author_login") for x in rc), "replies", sum(1 for x in rc if x.get("in_reply_to_id")))
print([(x.get("id"), x.get("author_login"), x.get("state"), x.get("submitted_at")) for x in rev])
times = {str(x.get("submitted_at"))[:19] for x in rev}
rep = [x for x in rc if x.get("in_reply_to_id")]
print("replies whose second matches a review:", sum(1 for x in rep if str(x.get("created_at"))[:19] in times), "of", len(rep))
print(json.dumps(rep[:1])[:400])

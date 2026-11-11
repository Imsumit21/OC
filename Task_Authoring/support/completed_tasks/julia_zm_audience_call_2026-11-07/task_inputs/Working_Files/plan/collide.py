"""Minted-id collision check through tools/hg.py records (complete collection scans). Updates plan/out/ground.json lookup."""
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "Task_Authoring" / "tools"))
from base_check import parse_sql  # noqa: E402

env = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs", MSYS_NO_PATHCONV="1")
rows = [x for x in parse_sql((HERE.parents[1] / "01_Universe_Inject.sql").read_text(encoding="utf8")) if x["op"] == "insert"]


def col(t, f):
    return sorted({str(x["row"][f]) for x in rows if x["table"] == t})


checks = [
    ("gdrive /drive_files id", "gdrive", "/drive_files", "id", col("gdrive.drive_files", "id")),
    ("gdocs /docs_documents document_id", "gdocs", "/docs_documents", "document_id", col("gdocs.docs_documents", "document_id")),
    ("gcal /events event_id", "gcal", "/events", "event_id", col("gcal.gcal_events", "event_id")),
    ("gcal /events ical_uid", "gcal", "/events", "ical_uid", col("gcal.gcal_events", "ical_uid")),
    ("linear /issues identifier", "linear", "/issues", "identifier", col("linear.linear_issues", "id")),
    ("trello /cards id", "trello", "/cards", "id", col("trello.trello_cards", "id")),
    ("trello /actions id", "trello", "/actions", "id", col("trello.trello_actions", "id")),
    ("github /review_comments id", "github", "/review_comments", "id", col("github.github_review_comments", "id")),
    ("github /reviews id", "github", "/reviews", "id", col("github.github_reviews", "id")),
]
req = {"checks": [{"id": f"c{i}", "service": s, "file": "data.json", "pointer": p, "field": f, "values": v}
                  for i, (_, s, p, f, v) in enumerate(checks)]}
path = HERE / "out" / "collide_req.json"
path.write_text(json.dumps(req))
r = subprocess.run([sys.executable, "-B", "Task_Authoring/tools/hg.py", "records", "--request", str(path)], cwd=ROOT, env=env,
                   capture_output=True, text=True, encoding="utf8")
d = json.loads(r.stdout)
res = {}
for i, (name, _, _, _, v) in enumerate(checks):
    c = d["checks"][f"c{i}"]
    res[name] = {"ids": len(v), "scan_complete": c.get("scan_complete"), "found": len(c.get("matches") or [])}
g = json.loads((HERE / "out" / "ground.json").read_text(encoding="utf8"))
g["lookup"] = res
(HERE / "out" / "ground.json").write_text(json.dumps(g, ensure_ascii=False, indent=1), encoding="utf8")
print(json.dumps(res, indent=0))

"""Base reads for the dossier through tools/hg.py: voice samples (1.C), keyword hits (1.D), minted-id collisions (1.F).
Writes plan/out/ground.json. Run from the workspace root."""
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
OUT = HERE / "out"
HG = [sys.executable, "-B", "Task_Authoring/tools/hg.py"]


def run(args, stdin=None):
    r = subprocess.run(HG + args, cwd=ROOT, env=env, input=stdin, capture_output=True, text=True, encoding="utf8")
    try:
        return json.loads(r.stdout)
    except ValueError:
        return {"error": (r.stderr or r.stdout)[-400:], "rc": r.returncode}


res = {}
ids = {"Julia Lawson": "0005", "Leonard Hayes": "0038", "Robert": "0016", "Brian Foster": "0026", "Vincent Parker": "0012",
       "Arthur Blake": "0025", "Claire Morgan": "0009", "Marcus Bennett": "0002", "Oliver Brooks": "0003", "Owen Baker": "0021",
       "Samuel Turner": "0004", "Calvin Price": "0006", "Martin Walsh": "0033", "Douglas": "0031"}
vals = [f"EMPLOYEE_{v}_SLACK_ID" for v in ids.values()]
req = {"checks": [{"id": f"{c}_{m}", "service": "slack", "file": f"messages/{c}/{m}.json", "pointer": "", "field": "user", "values": vals}
                  for c in ("C0880U9751A", "C08R27X0EAH") for m in ("2025-09", "2025-08")]}
p = OUT / "voice_req.json"
p.write_text(json.dumps(req))
v = run(["records", "--request", str(p)])
samples = {}
for cid, c in (v.get("checks") or {}).items():
    for m in c.get("matches") or []:
        r = m.get("record") or {}
        t = str(r.get("text") or "")
        if 15 <= len(t) <= 140 and "<" not in t and "\n" not in t:
            samples.setdefault(m.get("value"), []).append([cid.split("_")[0], r.get("ts"), t])
res["voice"] = {k: x[:4] for k, x in samples.items()}

terms = ["stability gate", "audience read", "Kadıköy ekibi", "1943", "no phone in the loop", "Vision Bot", "friend session",
         "a small thing from Friday", "never went through a store", "install-weighted", "re-run note", "Friday at Claire"]
res["keywords"] = {}
for svc, f in (("slack", "messages/*/2025-0[89].json"), ("gmail", "threads/*.json"), ("gdocs", "data.json"), ("linear", "data.json"),
               ("github", "data.json"), ("trello", "data.json"), ("gcal", "data.json"), ("gslides", "data.json")):
    req = {"service": svc, "file": f, "queries": [{"id": f"q{i}", "query": t, "limit": 5} for i, t in enumerate(terms)]}
    p = OUT / "kw_req.json"
    p.write_text(json.dumps(req))
    d = run(["search", "search-many", "--request", str(p), "--compact"])
    res["keywords"][svc] = {}
    for i, t in enumerate(terms):
        q = (d.get("queries") or {}).get(f"q{i}") or {}
        hits = q.get("matches") or q.get("results") or []
        res["keywords"][svc][t] = {"hits": len(hits), "complete": q.get("scan_complete"), "limit": q.get("limit_reached"),
                                   "first": (hits[0].get("file", "") + " " + hits[0].get("pointer", "")) if hits else None,
                                   "err": d.get("error")}

sql = (HERE.parents[1] / "01_Universe_Inject.sql").read_text(encoding="utf8")
rows = [x for x in parse_sql(sql) if x["op"] == "insert"]
sets = {
    "gmail": ("threads/*.json", sorted({x["row"]["id"].split("/", 1)[1] for x in rows if x["table"] == "gmail.gmail_threads"})),
    "gdrive": ("data.json", sorted({x["row"]["id"] for x in rows if x["table"] == "gdrive.drive_files"})),
    "gcal": ("data.json", sorted({x["row"]["ical_uid"] for x in rows if x["table"] == "gcal.gcal_events"})),
    "trello": ("data.json", ["68dc0acf1815df76ed9b887d", "68dc0acf5d1c8e7ab2f04c19"]),
    "linear": ("data.json", sorted({x["row"]["id"] for x in rows if x["table"] in ("linear.linear_issues", "linear.linear_comments")})),
}
res["lookup"] = {}
for svc, (f, ids_) in sets.items():
    p = OUT / "ids.json"
    p.write_text(json.dumps(ids_))
    d = run(["search", "lookup", svc, "--ids-file", str(p), "--file", f])
    res["lookup"][svc] = {"ids": len(ids_), "scan_complete": d.get("scan_complete"), "found": d.get("found") or d.get("matches") and len(d["matches"]),
                          "keys": list(d)[:10], "err": d.get("error")}
(OUT / "ground.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf8")
print("done")

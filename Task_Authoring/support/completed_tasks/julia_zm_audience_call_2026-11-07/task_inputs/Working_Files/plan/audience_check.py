"""Recompute the audience table from the generated SQL rows, never from planned_records.

Each exclusion is read from the row that carries it: K1 from the workbook observer, K3 from the ticket comment,
K4 and K5 from the notes Doc. Run: python3 audience_check.py
"""
import itertools
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "Task_Authoring" / "tools"))
from base_check import parse_sql  # noqa: E402

SQL = ROOT / "Task_Authoring" / "task_inputs" / "01_Universe_Inject.sql"
TIE, MIN_N = 0.25, 6
rows = parse_sql(SQL.read_text(encoding="utf8"))


def rows_of(table):
    return [r["row"] for r in rows if r["op"] == "insert" and r["table"] == table]


log = next(r for r in rows_of("gsheets.sheets_sheets") if r["title"] == "Log")
grid = json.loads(log["grid_json"])
head, body = grid[0], grid[1:]
docs = {d["title"]: d["body_text"] for d in rows_of("gdocs.docs_documents")}
comments = {c["issue_id"]: c["body"] for c in rows_of("linear.linear_comments")}
issues = {i["id"]: i for i in rows_of("linear.linear_issues")}

sessions = []
for r in body:
    s = dict(zip(head, r))
    doc = docs[s["notes doc"]]
    device = comments[s["ticket"]]
    if s["observer"] == "Claire Morgan":
        group = "K1"
    elif re.search(r"Galaxy|SM-[A-Z]", device):
        group = "K3"
    elif "Relation: Kadıköy ekibi" in doc:
        group = "K4"
    elif "(1943)" in doc:
        group = "K5"
    else:
        group = "CLEAN"
    desc = issues[s["ticket"]]["description"]
    assert f"Stars: {s['stars']}" in desc and f"Stars: {s['stars']}" in doc, s["ticket"]
    assert f"Audience: {s['audience']}" in desc and f"Audience: {s['audience']}" in doc, s["ticket"]
    assert f"Session date: {s['session date']}" in desc and f"Session date: {s['session date']}" in doc, s["ticket"]
    sessions.append((group, s["audience"].lower(), float(s["stars"])))

assert len(sessions) == 60
groups = ["K1", "K3", "K4", "K5"]


def read(keep):
    pool = [x for x in sessions if x[0] == "CLEAN" or x[0] in keep]
    c = [x[2] for x in pool if x[1] == "casual"]
    r = [x[2] for x in pool if x[1] == "rpg"]
    return len(c), sum(c) / len(c), len(r), sum(r) / len(r)


for g in ["CLEAN"] + groups:
    ms = [x for x in sessions if x[0] == g]
    print(g, len(ms), {a: (sum(1 for x in ms if x[1] == a), round(sum(x[2] for x in ms if x[1] == a) / max(1, sum(1 for x in ms if x[1] == a)), 3))
                       for a in ("casual", "rpg")})
nc, mc, nr, mr = read([])
print(f"Truth: counted {nc + nr} | casual n={nc} mean {mc:.3f} | RPG n={nr} mean {mr:.3f} | casual leads by {mc - mr:.3f}")
assert nc + nr == 17 and nc >= MIN_N and nr >= MIN_N and mc - mr > TIE
past, worst = 0, 9.0
for k in range(1, 5):
    for keep in itertools.combinations(groups, k):
        a, b, c, d = read(keep)
        gap = d - b
        worst = min(worst, gap)
        past += gap > TIE
        print(f"  kept {'+'.join(keep):14s} casual {b:.3f} RPG {d:.3f} RPG gap {gap:.3f}")
print(f"Miss combinations past {TIE}: {past} of 15 | smallest wrong gap {worst:.3f}")
assert past == 15
print("AUDIENCE TABLE: PASS")

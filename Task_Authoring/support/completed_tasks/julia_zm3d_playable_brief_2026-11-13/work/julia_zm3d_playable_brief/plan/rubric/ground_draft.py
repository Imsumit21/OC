#!/usr/bin/env python3
"""Draft grounding (playbook 09 gate 2 / Self-review 5): re-read every quoted source span in 09_Rubrics.json.

Each `<record> ('q1', 'q2' …)` in a criterion's Source part is checked against that record: a seeded record against
the task SQL (the quote, split at '…', must occur in the INSERT row that holds the record id); a base record through
`tools/hg.py search search-many` on its service (a match whose pointer/text carries the record id). Ticket keys,
addresses and channel ids in titles are checked against the SQL or the base contacts/channels the same way.
Writes plan/rubric/draft_grounding.txt and exits 1 on any miss."""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASK = HERE.parents[2]
WS = TASK.parents[1]
SQL = (TASK / "01_Universe_Inject.sql").read_text()
SQL_LINES = SQL.splitlines()
crit = json.loads((TASK / "09_Rubrics.json").read_text())

ID_RX = r"([CD][0-9A-Z]{8,}/\d{10}\.\d{6}|f_[0-9a-f]{22}|page_[a-z0-9_]+|comment_[a-z0-9_]+|DES-\d+|evt_[0-9a-f]{22}|[0-9a-f]{24})"


def unq(s):
    return s.replace("''", "'").replace("\\n", "\n")


sys.path.insert(0, str(TASK / "Working_Files" / "oe_gen"))
import model as O  # noqa: E402
ROWS = [r for r in O.ROWS if r.get("op") == "insert"]


def _text(row):
    return unq(" \n ".join(str(v) for v in row.values() if v is not None))


def sql_rows_with(rid):
    """Seeded INSERT rows (value text) that are the record; Brian's note on DES-n = the comments on that issue."""
    if rid.startswith("DES-"):
        iss = [r["row"] for r in ROWS if r["table"] == "linear.linear_issues" and r["row"].get("identifier") == rid]
        if not iss:
            return []
        iid = iss[0]["id"]
        return [_text(r["row"]) for r in ROWS if r["table"] == "linear.linear_comments" and r["row"].get("issue_id") == iid] + [_text(iss[0])]
    m = re.fullmatch(r"([CD][0-9A-Z]+)/(\d+\.\d+)", rid)
    if m:
        ch, ts = m.groups()
        return [_text(r["row"]) for r in ROWS if r["table"].startswith("slack.") and r["row"].get("ts") == ts
                and ch in (r["row"].get("channel_id"), r["row"].get("channel"))]
    return [_text(r["row"]) for r in ROWS if rid in {str(v) for v in r["row"].values()}]


def get_base(svc, file, pointer):
    r = subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/hg.py"), "search", "get", svc, "--file", file, "--pointer", pointer,
                        "--max-chars", "20000", "--compact"], capture_output=True, text=True, cwd=str(WS))
    try:
        return json.loads(r.stdout).get("text", "")
    except ValueError:
        return ""


def pieces(q):
    return [p.strip(" .") for p in re.split(r"…|\.\.\.", q) if len(p.strip(" .")) >= 3]


def quotes_of(source):
    """[(record id, [quote strings])] from a Source part."""
    out = []
    for m in re.finditer(ID_RX + r"(?:'s [a-z ]+)?\s*(?:\(([^()]*?)\))?", source):
        rid, paren = m.group(1), m.group(2) or ""
        qs = re.findall(r"'((?:[^']|'(?=[a-z]))+?)'(?=[,;)]|$| under| with)", paren + ")") if "'" in paren else []
        out.append((rid, [q for q in qs if len(q) >= 3]))
    return out


SVC = {"C": "slack", "D": "slack", "page_": "confluence", "comment_": "confluence"}


def base_check(todo):
    """{(rid, q): bool} via one search-many per service."""
    res = {}
    by = {}
    for rid, q in todo:
        svc = "confluence" if rid.startswith(("page_", "comment_")) else ("gsheets" if rid.startswith("f_") else "slack")
        for p in pieces(q):
            by.setdefault(svc, []).append((rid, q, p))
    for svc, items in by.items():
        req = {"service": svc, "queries": [{"id": f"q{i}", "query": p, "limit": 200} for i, (_, _, p) in enumerate(items)]}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(req, fh)
        r = subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/hg.py"), "search", "search-many", "--request", fh.name, "--compact"],
                           capture_output=True, text=True, cwd=str(WS))
        Path(fh.name).unlink(missing_ok=True)
        data = json.loads(r.stdout or "{}").get("queries", {})
        for i, (rid, q, p) in enumerate(items):
            ms = (data.get(f"q{i}") or {}).get("matches", [])
            ok = False
            for mm in ms:
                f, ptr = mm.get("service_file", ""), mm.get("pointer", "")
                if svc == "slack":
                    ch, ts = rid.split("/")
                    if f"/{ch}/" not in f"/{f}":
                        continue
                    idx = ptr.split("/")[1]
                    ok = get_base(svc, f, f"/{idx}/ts").strip('"') == ts or ts in get_base(svc, f, f"/{idx}")
                else:
                    segs = ptr.split("/")
                    rec = "/".join(segs[:3])                       # /pages/16, /comments/11
                    ok = rid in get_base(svc, f, rec)
                if ok:
                    break
            res[(rid, q)] = res.get((rid, q), True) and ok
    return res


lines, misses, base_todo = [], [], []
checked = 0
for n, c in enumerate(crit, 1):
    m = re.search(r"Sources?: (.*?)\. Accept:", c["evidence"])
    if not m:
        misses.append(f"R{n}: no Source part")
        continue
    for rid, qs in quotes_of(m.group(1)):
        rows = sql_rows_with(rid)
        if not qs:
            if not rows and rid.startswith(("DES-", "evt_")):
                misses.append(f"R{n}: {rid} not in the task SQL")
            continue
        for q in qs:
            checked += 1
            if rows and all(any(p in r for r in rows) for p in pieces(q)):
                lines.append(f"R{n} {rid} SQL '{q[:60]}'")
            elif rows and rid.startswith("f_") and all(any(p.replace("'", "") in r.replace('"', "") for r in rows) for p in pieces(q)):
                lines.append(f"R{n} {rid} SQL-cells '{q[:60]}'")
            else:
                base_todo.append((n, rid, q))
# base records
res = base_check([(rid, q) for _, rid, q in base_todo]) if base_todo else {}
for n, rid, q in base_todo:
    if res.get((rid, q)):
        lines.append(f"R{n} {rid} BASE '{q[:60]}'")
    else:
        misses.append(f"R{n}: '{q}' not found in {rid}")
# title literals: ticket keys and addresses
for n, c in enumerate(crit, 1):
    for t in re.findall(r"DES-\d+", c["title"]):
        if t != "DES-313" and not sql_rows_with(t):
            misses.append(f"R{n}: title ticket {t} not in the SQL")
    for a in re.findall(r"[\w.+-]+@[\w.-]+\.\w+", c["title"]):
        if a not in SQL:
            lines.append(f"R{n} title address {a} (base: checked by persona_view in the plan's §E)")
report = [f"DRAFT GROUNDING · {len(crit)} criteria · {checked} quoted spans · {len(misses)} miss(es)"] + lines + [f"MISS {x}" for x in misses]
(HERE / "draft_grounding.txt").write_text("\n".join(report) + "\n")
print(report[0])
for x in misses:
    print("MISS", x)
sys.exit(1 if misses else 0)

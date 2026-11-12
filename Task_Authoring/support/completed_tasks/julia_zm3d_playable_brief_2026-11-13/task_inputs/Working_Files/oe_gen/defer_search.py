#!/usr/bin/env python3
"""Authority-aware defer search for the six write families (playbook 08, prep checklist 'Writes').
Scoped services through tools/persona_view.py search (persona ACL applied, --no-hidden); unscoped services through
tools/hg.py search; the seeded overlay through the SQL statements (never executed). Read-only on the universe.
Writes oe_gen/out/defer_search.json and prints the candidate population. Run from the workspace root."""
import json, os, re, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
TASK = HERE.parents[1]; ROOT = TASK.parents[1]; TOOLS = TASK.parent / "tools"
sys.path.insert(0, str(TOOLS))
from base_check import parse_sql
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(TASK))
SINCE = "2025-09-16"      # the day PlayableX set the first start date and the formats; nothing about this playable's hand-off is older
DEFER = ["hold off", "not yet", "wait", "defer", "freeze", "pause", "parked", "postpone", "as-is", "as is", "accept", "cancel", "on hold", "don't send", "do not send"]
TOPIC = ["playable", "PlayableX", "pack list", "hand-off", "DES-313", "brief"]
SCOPED = ["slack", "gmail", "gcal", "gdrive", "gdocs", "gsheets", "gslides"]
UNSCOPED = ["linear", "trello", "confluence", "github", "contacts"]
def pv(svc, q):
    p = subprocess.run([sys.executable, "-B", str(TOOLS / "persona_view.py"), "search", "julia_lawson", svc, q, "--limit", "1000000", "--no-hidden", "--json"],
                       capture_output=True, text=True, cwd=ROOT, env=ENV)
    try: return json.loads(p.stdout)
    except ValueError: return {"error": (p.stderr or p.stdout)[:300], "visible": [], "visible_total": None}
def hg(svc, q):
    p = subprocess.run([sys.executable, "-B", str(TOOLS / "hg.py"), "search", "search", svc, q, "--limit", "100000", "--compact"], capture_output=True, text=True, cwd=ROOT, env=ENV)
    try: return json.loads(p.stdout)
    except ValueError: return {"error": (p.stderr or p.stdout)[:300], "matches": []}
out = {"since": SINCE, "scoped": {}, "unscoped": {}, "seeded": {}}
calls = 0
for svc in SCOPED:
    for q in DEFER + TOPIC:
        r = pv(svc, q); calls += 1
        vis = r.get("visible") or []
        dated = [h for h in vis if (h.get("date") or "9999") >= SINCE] if svc in ("slack", "gmail", "gcal") else vis
        out["scoped"][f"{svc}|{q}"] = {"visible_total": r.get("visible_total"), "returned": len(vis), "complete": r.get("visible_total") == len(vis),
                                       "since": len(dated), "hits": dated if q in DEFER and svc in ("slack", "gmail", "gcal") else dated[:400], "error": r.get("error")}
        print(f"{svc:8} {q:14} total {r.get('visible_total')} returned {len(vis)} since {len(dated)}", r.get("error") or "")
for svc in UNSCOPED:
    for q in TOPIC + ["parked", "pause"]:
        r = hg(svc, q); calls += 1
        m = r.get("matches") or []
        out["unscoped"][f"{svc}|{q}"] = {"matches": len(m), "scan_complete": r.get("scan_complete"), "pointers": [x["pointer"] for x in m][:200],
                                         "texts": [x["text"][:300] for x in m][:200], "error": r.get("error")}
        print(f"{svc:8} {q:14} matches {len(m)} scan_complete {r.get('scan_complete')}", r.get("error") or "")
rows = parse_sql((TASK / "01_Universe_Inject.sql").read_text())
for q in DEFER:
    hits = []
    for r in rows:
        vals = (r.get("row") or r.get("set") or {})
        text = " ".join(str(v) for v in vals.values() if v is not None)
        if re.search(r"(?<!\w)" + re.escape(q) + r"(?!\w)", text, re.I):
            hits.append({"line": r["line"], "table": r["table"], "key": vals.get("id") or vals.get("document_id") or vals.get("event_id"), "snippet": text[max(0, text.lower().find(q.lower()) - 90): text.lower().find(q.lower()) + 110]})
    out["seeded"][q] = hits
    print(f"seeded   {q:14} rows {len(hits)}")
out["calls"] = calls
(HERE / "out" / "defer_search.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print("calls", calls)

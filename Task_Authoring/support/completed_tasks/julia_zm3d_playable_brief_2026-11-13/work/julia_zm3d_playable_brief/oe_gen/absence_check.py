#!/usr/bin/env python3
"""ABSENCE evidence check for the Delivered and Ready lines: nothing the persona can read says, after Brian's note, that
one of the 44 files no later record touches changed, is wrong or is being redone (rev2: the three recoloured lines are Ready
on Brian's log of Tue 30 Sep, so for them the check is that nothing after that entry names them). Scope: every Slack container the persona can open (persona_view
search, ACL applied) from Wed 24 Sep 2025 (the first zip) to the clock, plus every seeded row of the overlay.
Positive control: the same search finds the three statements that do exist (cactus/chainsaw/cones, the bathroom files, bow).
Writes oe_gen/out/absence_check.json. Read-only. Run from the workspace root."""
import json, os, re, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import model as O
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(O.TASK))
SINCE = "2025-09-24"
def pv(q):
    p = subprocess.run([sys.executable, "-B", str(O.TOOLS / "persona_view.py"), "search", O.PERSONA, "slack", q, "--limit", "1000000", "--no-hidden", "--json"],
                       capture_output=True, text=True, cwd=O.ROOT, env=ENV)
    try: return json.loads(p.stdout)
    except ValueError: return {"error": (p.stderr or p.stdout)[:300], "visible": [], "visible_total": None}
targets = [l["name"] for l in O.ABSENCE_TARGETS]
controls = ["cactus", "bathroom", "bow"]
RESENT_SINCE = "2025-09-30"     # the day of the log entry that records the re-send
out = {"since": SINCE, "targets": {}, "controls": {}, "seeded": {}, "resent_since": RESENT_SINCE, "resent": {}}
for name in targets + controls:
    r = pv(name)
    vis = r.get("visible") or []
    hits = [h for h in vis if (h.get("date") or "") >= SINCE]
    rec = {"visible_total": r.get("visible_total"), "returned": len(vis), "complete": r.get("visible_total") == len(vis), "since": len(hits),
           "hits": [{"id": h["id"], "date": h["date"], "channel": h.get("channel"), "snippet": h.get("snippet")} for h in hits], "error": r.get("error")}
    (out["controls"] if name in controls else out["targets"])[name] = rec
    print(f"{name:20} total {rec['visible_total']} since {rec['since']} complete {rec['complete']}", rec["error"] or "")
for l in O.members("C1"):
    r = pv(l["name"]); vis = r.get("visible") or []
    hits = [h for h in vis if (h.get("date") or "") >= RESENT_SINCE]
    out["resent"][l["name"]] = {"visible_total": r.get("visible_total"), "returned": len(vis), "complete": r.get("visible_total") == len(vis),
                                "since": len(hits), "hits": [{"id": h["id"], "date": h["date"], "snippet": h.get("snippet")} for h in hits]}
    print(f"re-sent {l['name']:14} total {r.get('visible_total')} since {RESENT_SINCE}: {len(hits)}")
for name in targets:
    hits = []
    for r in O.ROWS:
        vals = r.get("row") or r.get("set") or {}
        if r["table"] in ("linear.linear_issues", "linear.linear_comments", "gsheets.sheets_sheets"): continue   # the line's own ticket, note and list row
        text = " ".join(str(v) for v in vals.values() if v is not None)
        if re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", text, re.I): hits.append({"line": r["line"], "table": r["table"]})
    out["seeded"][name] = hits
(HERE / "out" / "absence_check.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")

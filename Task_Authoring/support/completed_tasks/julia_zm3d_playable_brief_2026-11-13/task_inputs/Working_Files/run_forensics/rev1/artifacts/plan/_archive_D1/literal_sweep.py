#!/usr/bin/env python3
"""Literal-value and wording sweep on the base (scenario S9): phrases the planned deciding records and hub texts use.
One batch per service through tools/hg.py; prints hit counts with scan coverage. Read-only."""
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
PHRASES = {
    "empty_shell": "empty shell", "old_unwrap": "old unwrap", "bought_pack": "bought pack", "comes_in_grey": "comes in grey",
    "instead_of_the_iron": "instead of the iron", "multi_select": "multi-select", "object_browser": "object browser",
    "handoff_notes": "hand-off notes", "pack_list": "pack list", "own_outright": "own outright", "outgoing_folder": "outgoing folder",
    "intake": "intake@", "redoing_the_uvs": "redoing the UVs", "source_sheet": "sound source",
}
SERVICES = sys.argv[1:] or ["linear", "gdocs", "gsheets", "gslides", "confluence", "trello", "github", "gcal", "contacts", "gmail", "slack"]
for svc in SERVICES:
    req = {"service": svc, "queries": [{"id": k, "query": v, "limit": 5} for k, v in PHRASES.items()]}
    r = subprocess.run([sys.executable, "-B", str(ROOT / "Task_Authoring/tools/hg.py"), "search", "search-many", "--request", "-", "--compact"],
                       input=json.dumps(req), capture_output=True, text=True, cwd=ROOT)
    try:
        d = json.loads(r.stdout)
    except ValueError:
        print(f"{svc}: ERROR {r.stderr.strip()[:200] or r.stdout[:200]}"); continue
    qs = d.get("queries", {})
    row = []
    for k in PHRASES:
        q = qs.get(k, {})
        n = len(q.get("matches", []))
        row.append(f"{k}={n}{'' if q.get('scan_complete', d.get('scan_complete')) else '?'}")
        for m in q.get("matches", [])[:2]:
            print(f"    {svc} {k}: {m.get('relative_file') or m.get('file')} {m.get('pointer')} | {str(m.get('excerpt') or m.get('snippet') or '')[:140]!r}")
    print(f"{svc}: scan_complete={d.get('scan_complete')} " + " ".join(row), flush=True)

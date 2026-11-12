#!/usr/bin/env python3
"""Natural-retrieval rehearsal on the injected universe (injection review evidence).

For each mechanism: the keyword searches a reader of the ask and the notes would try, run on the base as the persona
(tools/persona_view.py search, ACL applied) and on the injected rows of 01_Universe_Inject.sql (same match rule: the
query's words, case-insensitive, in the record's text fields). Printed per query: base hits the persona sees, injected
records returned, and whether the mechanism's deciding record is among them. Read-only; writes out/natural_retrieval_injection.txt."""
import json, re, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
ROOT = TASK.parents[1]
TOOLS = TASK.parent / "tools"
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(TOOLS))
import design_model as M
from base_check import parse_sql
S, B = M.SEED, M.BASE
rows = [r for r in parse_sql((TASK / "01_Universe_Inject.sql").read_text()) if r["op"] == "insert"]

TEXT = {"slack": [("slack.slack_messages", ("text",), lambda r: f"{r['channel_id']}/{r['ts']}")],
        "gdrive": [("gdrive.drive_files", ("name",), lambda r: r["id"]), ("gdocs.docs_documents", ("title", "body_text"), lambda r: r["document_id"]),
                   ("gsheets.sheets_spreadsheets", ("title",), lambda r: r.get("spreadsheet_id") or r.get("id")), ("gsheets.sheets_sheets", ("title", "grid_json"), lambda r: r["spreadsheet_id"]),
                   ("gslides.slides_presentations", ("title",), lambda r: r.get("presentation_id") or r.get("id"))],
        "gdocs": [("gdocs.docs_documents", ("title", "body_text"), lambda r: r["document_id"])],
        "gsheets": [("gsheets.sheets_spreadsheets", ("title",), lambda r: r.get("spreadsheet_id") or r.get("id")), ("gsheets.sheets_sheets", ("title", "grid_json"), lambda r: r["spreadsheet_id"])]}
def injected(service, query):
    words = [w for w in re.split(r"\s+", query.lower()) if w]
    out = []
    for table, fields, rid in TEXT[service]:
        for r in rows:
            if r["table"] != table: continue
            text = " ".join(str(r["row"].get(f) or "") for f in fields).lower()
            if all(w in text for w in words):
                i = rid(r["row"])
                if i not in out: out.append(i)
    return out
def base(service, query, limit=6):
    p = subprocess.run([sys.executable, "-B", str(TOOLS / "persona_view.py"), "search", "julia_lawson", service, query, "--limit", str(limit)],
                       capture_output=True, text=True, cwd=ROOT)
    lines = [l for l in p.stdout.splitlines() if l.strip()]
    head = next((l for l in lines if l.startswith("visible hits")), "visible hits=? (search failed: " + p.stderr.strip()[:120] + ")")
    hits = [l.strip()[:200] for l in lines if l.strip().startswith("{")]
    return head, hits

PLAN = [
 ("EXPORT", S["a1_post"]["id"], f"container read: slack_read_channel on #zombie-match3d ({M.MATCH3D_CH}) for 25 to 30 Sep returns it as a top-level message",
  [("slack", "fbx"), ("slack", "binary"), ("slack", "exporter"), ("slack", "saved out")]),
 ("ARTHOLD", S["a2_dm"]["id"], f"container read: slack_read_channel on Julia's DM with Claire ({M.DM_CLAIRE}) after 24 Sep returns it as the newest message",
  [("slack", "bathroom"), ("slack", "banyo"), ("slack", "uv")]),
 ("AUDIO", S["c2_sheet"]["id"], "file read: gsheets_values_get on the sheet returns the two 'no' rows",
  [("gdrive", "sound"), ("gsheets", "sound"), ("gdrive", "sources")]),
 ("PICKS", S["c3_reply"]["id"], f"thread read: slack_read_thread on Julia's bow post ({B['art_bow_root']}) returns it as the only reply by Robert after 26 Sep 16:27 UTC",
  [("slack", "dynamite"), ("slack", "bow"), ("slack", "in place of")]),
 ("ZIP", S["c4_log"]["id"], "file read: gdocs_get_document_text on the log returns the 30 Sep line",
  [("gdrive", "outgoing"), ("gdocs", "outgoing folder"), ("gdrive", "zip")]),
]
out = ["Natural-retrieval rehearsal on the injected universe (persona julia_lawson; base through persona_view.py search, injected rows through the SQL's text fields).",
       "A query returns an injected record when every word of the query is in its text. REVISED is base only: see natural_retrieval_revised.txt.", ""]
summary = {}
for mid, decider, read_path, queries in PLAN:
    out += [f"## {mid} · deciding record {decider}", read_path]
    summary[mid] = {"decider": decider, "queries": []}
    for service, q in queries:
        head, hits = base(service, q)
        inj = injected(service, q)
        found = decider in inj
        out += [f"$ search {service} \"{q}\"", f"  base: {head}"] + [f"    {h}" for h in hits[:3]] + [f"  injected records returned: {', '.join(inj) if inj else 'none'}",
                f"  deciding record returned: {'YES' if found else 'no'}"]
        summary[mid]["queries"].append({"service": service, "query": q, "base": head, "injected": inj, "returns_decider": found})
    out.append("")
(HERE / "out" / "natural_retrieval_injection.txt").write_text("\n".join(out) + "\n")
(HERE / "out" / "natural_retrieval_injection.json").write_text(json.dumps(summary, indent=1) + "\n")
for mid, v in summary.items():
    print(mid, [(q["query"], q["returns_decider"], len(q["injected"])) for q in v["queries"]])

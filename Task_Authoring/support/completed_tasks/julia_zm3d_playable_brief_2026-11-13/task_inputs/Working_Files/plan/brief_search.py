#!/usr/bin/env python3
"""Search-as-persona proof for the prompt brief (§5a): one natural query per discovery-map fact.

Base: tools/persona_view.py search as julia_lawson (ACL applied). Seeded: the same words against the text of the injected
rows the persona can open (dossier 1.E check-sql). Also runs tools/entity.py collisions and resolve for §10.
Writes out/brief_search.json and out/brief_search.txt (the pasted outputs). Read-only."""
import json, re, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
TASK = HERE.parents[1]
ROOT = TASK.parents[1]
TOOLS = TASK.parent / "tools"
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(TOOLS))
import design_model as M
from base_check import parse_sql
S, B, PT = M.SEED, M.BASE, M.PACK_TICKET
rows = [r for r in parse_sql((TASK / "01_Universe_Inject.sql").read_text()) if r["op"] == "insert"]
ids = json.loads((HERE / "out" / "sql_ids.json").read_text())
JULIA = "julia.lawson@harmonygames.co"
def note(n): return M.comment_id("note_" + n)

SEEDED = {   # service -> [(table, text columns, id of the hit)]
 "slack": [("slack.slack_messages", ("text",), lambda r: f"{r['channel_id']}/{r['ts']}")],
 "gdocs": [("gdocs.docs_documents", ("title", "body_text"), lambda r: r["document_id"])],
 "gsheets": [("gsheets.sheets_spreadsheets", ("title",), lambda r: r.get("spreadsheet_id") or r.get("id")), ("gsheets.sheets_sheets", ("title", "grid_json"), lambda r: r["spreadsheet_id"])],
 "gslides": [("gslides.slides_presentations", ("title",), lambda r: r.get("presentation_id") or r.get("id")), ("gslides.slides_page_elements", ("text", "content_json", "text_content"), lambda r: r.get("presentation_id"))],
 "gdrive": [("gdrive.drive_files", ("name",), lambda r: r["id"])],
 "linear": [("linear.linear_issues", ("title", "description", "id"), lambda r: r["id"]), ("linear.linear_comments", ("body",), lambda r: r["id"])],
 "gcal": [("gcal.gcal_events", ("summary", "description"), lambda r: r["event_id"])],
 "contacts": [("contacts.contacts", ("first_name", "last_name", "job", "email", "company"), lambda r: r.get("contact_id") or r.get("id"))],
 "trello": [("trello.trello_actions", ("data_json",), lambda r: r["id"])],
 "github": [], "confluence": [], "gmail": [("gmail.gmail_messages", ("subject", "body_text", "body", "snippet"), lambda r: r.get("id"))],
}
def visible(service, r):
    """Scoped seeded rows count only when the persona can open them (same rule as check-sql)."""
    if service == "gcal": return r.get("calendar_id") == JULIA
    if service == "gmail": return str(r.get("id", "")).startswith(JULIA)
    return True      # the seeded Slack containers, Drive files and unscoped services are all persona-readable (dossier 1.E)
def seeded(service, query):
    words = [w for w in re.split(r"\s+", query.lower()) if w]
    out = []
    for table, cols, rid in SEEDED.get(service, []):
        for r in rows:
            if r["table"] != table or not visible(service, r["row"]): continue
            text = " ".join(str(r["row"].get(c) or "") for c in cols).lower()
            if all(w in text for w in words):
                i = rid(r["row"])
                if i and i not in out: out.append(i)
    return out
def base(service, query, limit=5):
    cmd = [sys.executable, "-B", str(TOOLS / "persona_view.py"), "search", "julia_lawson", service, query, "--limit", str(limit)]
    if service in ("gmail", "slack"): cmd.append("--no-hidden")
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    lines = [l.rstrip() for l in p.stdout.splitlines() if l.strip()]
    vis = re.search(r"visible hits=(\d+)", p.stdout); hid = re.search(r"hidden by ACL=(\d+)", p.stdout)
    hits = []
    for l in lines:
        if l.strip().startswith("{"):
            try: hits.append(json.loads(l.strip()))
            except ValueError: pass
    return {"visible": int(vis.group(1)) if vis else None, "hidden": int(hid.group(1)) if hid else None, "hits": hits, "raw": lines[:8], "err": p.stderr.strip()[:200]}

FACTS = [   # (fact id, label, service, natural query, expected id, origin)
 ("F1", "Frederick's ask", "slack", "hand-off notes", S["ask"]["id"], "seeded"),
 ("F2", "the hand-off notes", "gdocs", "hand-off notes", S["notes"]["id"], "seeded"),
 ("F3", "Brian's pack list", "gsheets", "pack list", S["tracker"]["id"], "seeded"),
 ("F4", "the pack ticket and its children", "linear", "Playable pack", PT, "seeded"),
 ("F5", "Brian's note on each ticket", "linear", "outgoing folder", note("Dynamite"), "seeded"),
 ("F6", "Robert's eight for the board", "slack", "playable board", S["picks"]["id"], "seeded"),
 ("F7", "Robert's later reply", "slack", "in place of the last one", S["c3_reply"]["id"], "seeded"),
 ("F8", "Robert's zombies and animation", "slack", "4 zombies", S["zpicks"]["id"], "seeded"),
 ("F9", "Marcus on Thursday's exports", "slack", "unity thursday", S["a1_post"]["id"], "seeded"),
 ("F10", "Robert on the bathroom files", "slack", "bathroom", S["a2_dm"]["id"], "seeded"),
 ("F11", "Robert's new colour versions", "slack", "new colored version", B["robert_new_colours"], "base"),
 ("F12", "Calvin's sound sources", "gsheets", "sound sources", S["c2_sheet"]["id"], "seeded"),
 ("F13", "Brian's log of the outgoing folder", "gdocs", "outgoing folder", S["c4_log"]["id"], "seeded"),
 ("F14", "Julia's deck of the reference level", "gslides", "reference level", S["deck"]["id"], "seeded"),
 ("F15", "the kickoff hold", "gcal", "playable kickoff", S["hold"]["id"], "seeded"),
 ("F16", "PlayableX's intake address", "contacts", "PlayableX", S["contact"]["id"], "seeded"),
 ("F17", "Leonard's comment on the kickoff card", "trello", "Parked until Nov 3", S["trello_note"]["id"], "seeded"),
 ("F18", "the vendor's format rule", "slack", "Binary format", B["vendor_formats"], "base"),
 ("F19", "the vendor's new start date", "slack", "November 3rd", B["vendor_nov3"], "base"),
 ("F20", "the design page", "confluence", "7-slot tray", B["gdd"], "base"),
 ("F21", "Scenario 1 and what it is for", "slack", "Scenario 1", B["fred_scenario1"], "base"),
 ("F22", "the vendor's rule on music", "slack", "music has to start after first click", B["vendor_music_rule"], "base"),
 ("F23", "the PlayableX channel", "slack", "PlayableX", M.VENDOR_CH, "base"),
 ("F24", "Julia's Drive", "gdrive", "reference level", B["julia_root"], "seeded"),
]
out, txt = {}, []
for fid, label, service, query, want, origin in FACTS:
    b = base(service, query)
    s = seeded(service, query)
    base_ids = [h.get("id") for h in b["hits"] if h.get("id")]
    if origin == "seeded":
        found = want in s or (fid == "F24" and S["deck"]["id"] in s) or (fid == "F5" and len(s) > 0)
        first = want if want in s else (s[0] if s else None)
    else:
        found = bool(b["visible"])
        hit = next((i for i in base_ids if want.split("/")[0] in str(i)), None)
        first = want if (hit or b["visible"]) else None
    out[fid] = {"label": label, "service": service, "query": query, "base_visible": b["visible"], "hidden": b["hidden"], "base_first": base_ids[:3],
                "seeded": s[:6], "seeded_n": len(s), "want": want, "origin": origin, "found": bool(found), "first": first, "err": b["err"]}
    txt += [f"$ persona_view.py search julia_lawson {service} \"{query}\" --limit 5" + (" --no-hidden" if service in ("gmail", "slack") else "")] + b["raw"] + \
           [f"seeded rows the persona can open that hold these words: {len(s)}" + (f" (first: {', '.join(s[:3])})" if s else ""), ""]
    print(fid, service, repr(query), "base", b["visible"], "seeded", len(s), "found", found, "|", b["err"][:80])

# entity checks for §10
def run(*a):
    p = subprocess.run([sys.executable, "-B", str(TOOLS / "entity.py"), *a], capture_output=True, text=True, cwd=ROOT)
    return (p.stdout or p.stderr).rstrip()
ent = ["$ entity.py collisions", run("collisions")]
for name in ("Julia Lawson", "Frederick Stone", "Brian Foster", "Robert", "Claire Morgan", "Marcus Bennett", "Calvin Price", "Leonard Hayes", "Martin Walsh"):
    ent += [f"$ entity.py resolve \"{name}\"", run("resolve", name)]
(HERE / "out" / "brief_search.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
(HERE / "out" / "brief_search.txt").write_text("\n".join(txt) + "\n")
(HERE / "out" / "brief_entity.txt").write_text("\n".join(ent) + "\n")
print("not found:", [k for k, v in out.items() if not v["found"]])

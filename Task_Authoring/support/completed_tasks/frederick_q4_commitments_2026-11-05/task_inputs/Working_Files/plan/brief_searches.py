#!/usr/bin/env python3
"""Brief §5a: run each discovery fact's natural query as Frederick through tools/persona_view.py search (base data),
count the seeded rows Frederick can see that carry the query (the SQL overlay persona_view does not read), and record
the first visible hit. Writes plan/brief_searches.json and plan/brief_searches.txt (verbatim outputs)."""
import contextlib
import io
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
sys.path.insert(0, HERE)
from base_check import parse_sql  # noqa: E402
with contextlib.redirect_stdout(io.StringIO()):
    import build_scenario as B  # noqa: E402

FRED = "frederick.stone@harmonygames.co"
IDS = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
I, BASE, SL = B.IDS, B.BASE, IDS["slack_mid"]
STM = [x for x in parse_sql(open(os.path.join(TI, "01_Universe_Inject.sql")).read()) if x["op"] == "insert"]
FRED_SLACK = {B.EXEC, "D05S58U4SAK"}


def seeded_units(service):
    """(id, text) of seeded rows Frederick can see in a service."""
    out = []
    for x in STM:
        r, t = x["row"], x["table"]
        if service == "gmail" and t == "gmail.gmail_messages" and r["user_email"] == FRED:
            out.append((r["thread_id"], f"{r.get('subject')} {r.get('body_text')} {r.get('from_email')}"))
        elif service == "slack" and t == "slack.slack_messages" and r["channel_id"] in FRED_SLACK:
            out.append((f"{r['channel_id']}/{r['ts']}", r.get("text") or ""))
        elif service == "gdocs" and t == "gdocs.docs_documents":
            out.append((r["document_id"], f"{r['title']} {r['body_text']}"))
        elif service == "gdrive" and t == "gdrive.drive_files":
            out.append((r["id"], r["name"]))
        elif service == "gsheets" and t in ("gsheets.sheets_spreadsheets", "gsheets.sheets_sheets"):
            out.append((r["spreadsheet_id"], f"{r.get('title')} {r.get('grid_json')}"))
        elif service == "gslides" and t == "gslides.slides_page_elements":
            out.append((r["presentation_id"], r.get("text") or ""))
        elif service == "gcal" and t == "gcal.gcal_events" and r["calendar_id"] == FRED:
            out.append((r["event_id"], f"{r.get('summary')} {r.get('description')}"))
        elif service == "trello" and t in ("trello.trello_cards", "trello.trello_check_items"):
            out.append((r["id"], f"{r.get('name')} {r.get('desc')}"))
        elif service == "linear" and t in ("linear.linear_issues", "linear.linear_comments"):
            out.append((r.get("identifier") or r["id"], f"{r.get('title')} {r.get('description')} {r.get('body')}"))
        elif service == "contacts" and t == "contacts.contacts":
            out.append((r["contact_id"], f"{r.get('first_name')} {r.get('last_name')} {r.get('job')}"))
    return out


# (fid, service, natural query, id the row must reach)
Q = [
    ("F1", "gmail", "vendor and partner", I["hub_thread"]),
    ("F2", "gdocs", "runway guardrails", I["guardrails_doc"]),
    ("F3", "gdocs", "UA spend", I["ua_buckets_doc"]),
    ("F4", "gmail", "Signing and review", I["esg_thread"]),
    ("F5", "gdocs", "intake checklist", I["esg_checklist_doc"]),
    ("F6", "contacts", "ESG Law", I["esg_intake_contact"]),
    ("F7", "gdrive", "Q4 commitments", I["q4_folder"]),
    ("F8", "gdocs", "README - Q4 commitments", I["readme_doc"]),
    ("F9", "gsheets", "Q4 commitments", I["template_sheet"]),
    ("F10", "trello", "Keep-running", I["keep_card"]),
    ("F11", "trello", "night pager", IDS["keep_items"][2]),
    ("F12", "slack", "accept the terms", I["july_sign_note"]),
    ("F13", "slack", "runway guardrails", I["amendment_root"]),
    ("F14", "slack", "Maren", I["framewell_waiver_reply"]),
    ("F15", "slack", "Playtestcloud results are in", BASE["playtestcloud_root"]),
    ("F16", "slack", "Southeast Asia", I["lanternfly_dm"]),
    ("F17", "slack", "marketing tool", I["robert_cancel_all"]),
    ("F18", "slack", "indie showcase", IDS["spotlight_note"]),
    ("F19", "linear", "Nintendo", "ZOM-567"),
    ("F20", "gmail", "Nintendo", BASE["nintendo_ndareq"]),
    ("F21", "slack", "registered an account", BASE["fred_nintendo_post"]),
    ("F22", "gmail", "HG-2291", I["clipforge_notice_thread"]),
    ("F23", "gmail", "Clipforge", I["clipforge_thread"]),
    ("F24", "gcal", "UGC Studio", I["clipforge_kickoff"]),
    ("F25", "gsheets", "Vendor & partner tracker", I["tracker_sheet"]),
    ("F26", "gmail", "booth", I["pixel_thread"]),
    ("F27", "gcal", "Q4 commitments review", I["review_event"]),
    ("F28", "gcal", "Spotlight Fest", I["spotlight_call"]),
    ("F29", "gmail", "Balancy", BASE["balancy_thread"]),
    ("F30", "gmail", "Chinese Local Game publishing", BASE["rayking_thread"]),
    ("F31", "gmail", "Playable Factory", BASE["playable_factory_thread"]),
    ("F32", "gmail", "Nova Rewards", I["nova_thread"]),
    ("F33", "gdrive", "paperwork", IDS["paperwork_folder"]),
    ("F34", "gmail", "Motive Forge", I["motive_thread"]),
    ("F35", "gmail", "Spotlight Fest", I["spotlight_thread"]),
]
# one row per remaining seeded counterparty (thread search by company name)
NO_NAME_IN_MAIL = {"Soundvault", "Streamcast Talent", "Lingora", "Panelpulse", "Ascendo", "Wishwave", "Certwell", "Glyphworks", "Driftwood Audio"}
for m in B.M:
    k = m["key"]
    if m["decision"] == "out" or m.get("base") or k in ("Clipforge", "Pixel Harbor Events", "Motive Forge", "Spotlight Fest"):
        continue
    th = IDS["threads"].get(k)
    # nine counterparties never write their company name in mail (tokenized address, first-name signature): the name is
    # on the paper Frederick filed in Drive, so the natural search for them is the paper
    if k in NO_NAME_IN_MAIL:
        Q.append((f"C:{k}", "gdocs", k, IDS["papers"][k]))
    elif th:
        Q.append((f"C:{k}", "gmail", k.split(" ")[0] if k not in ("Orbit Store", "Driftwood Audio") else k, th))

res, raw = [], []
for fid, svc, q, want in Q:
    args = ["python3", "-B", "Task_Authoring/tools/persona_view.py", "search", "frederick_stone", svc, q, "--limit", "10"]
    if svc in ("gmail", "slack"):
        args.append("--no-hidden")
    p = subprocess.run(args, cwd=WS, capture_output=True, text=True, timeout=900)
    txt = (p.stdout + p.stderr).strip()
    raw.append(txt)
    jp = subprocess.run(args + ["--json"], cwd=WS, capture_output=True, text=True, timeout=900)
    try:
        jd = json.loads(jp.stdout)
    except ValueError:
        jd = {}
    hits = [h.get("id") for h in (jd.get("visible") or [])]
    nvis = jd.get("visible_total", len(hits))
    hidden = jd.get("hidden_by_acl", jd.get("hidden"))
    seeded = [i for i, t in seeded_units(svc) if q.lower() in (t or "").lower()]
    seeded_ids = sorted(set(seeded))
    if want in hits:
        first, how = want, f"YES (base, hit {hits.index(want) + 1} of {len(hits)})"
    elif want in seeded_ids or any(want.split('/')[-1] in s for s in seeded_ids):
        first, how = want, "YES (seeded; check-sql YES)" if svc not in ("trello", "linear", "contacts") else "YES (seeded; unscoped)"
    elif hits:
        first, how = hits[0], f"PARTIAL (base hits do not include {want})"
    else:
        first, how = None, "NO"
    res.append(dict(fid=fid, service=svc, query=q, want=want, base=nvis, seeded=len(seeded_ids),
                    hidden=hidden if svc not in ("gmail", "slack") else "n/a (--no-hidden)", first=first, found=how))
json.dump(res, open(os.path.join(HERE, "brief_searches.json"), "w"), indent=1)
open(os.path.join(HERE, "brief_searches.txt"), "w").write("\n\n".join(raw) + "\n")
for r in res:
    print(r["fid"], r["service"], repr(r["query"]), "base", r["base"], "seeded", r["seeded"], r["found"])

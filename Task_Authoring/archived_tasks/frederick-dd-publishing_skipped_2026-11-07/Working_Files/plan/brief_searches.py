#!/usr/bin/env python3
"""Brief §5a: run each discovery fact's natural query as Frederick through tools/persona_view.py search (base data), count the
seeded rows Frederick can see that carry the query (the SQL overlay persona_view doesn't read), and record the first visible hit.
Writes plan/brief_searches.json and plan/brief_searches.txt (verbatim outputs)."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TI = os.path.dirname(WF); WS = os.path.abspath(os.path.join(TI, "..", ".."))
sys.path.insert(0, os.path.join(TI, "..", "tools")); sys.path.insert(0, HERE)
from base_check import parse_sql  # noqa: E402
import brief_facts as BF  # noqa: E402
FRED = "frederick.stone@harmonygames.co"
STM = [x for x in parse_sql(open(os.path.join(TI, "01_Universe_Inject.sql")).read()) if x["op"] == "insert"]
SLACK = {"C07C2866011", "C096HFA5Z8W", "C069FF9Q57S", "D05S58U4SAK"}
def seeded_units(service):
    out = []
    for x in STM:
        r, t = x["row"], x["table"]
        if service == "gmail" and t == "gmail.gmail_messages" and r["user_email"] == FRED:
            out.append((r["thread_id"], f"{r.get('subject')} {r.get('body_text')} {r.get('from_email')} {r.get('to_json')}"))
        elif service == "slack" and t == "slack.slack_messages" and r["channel_id"] in SLACK:
            out.append((f"{r['channel_id']}/{r['ts']}", r.get("text") or ""))
        elif service == "gdocs" and t == "gdocs.docs_documents":
            out.append((r["document_id"], f"{r['title']} {r['body_text']}"))
        elif service == "gdrive" and t == "gdrive.drive_files":
            out.append((r["id"], r["name"]))
        elif service == "gsheets" and t in ("gsheets.sheets_spreadsheets", "gsheets.sheets_sheets"):
            out.append((r["spreadsheet_id"], f"{r.get('title')} {r.get('grid_json')}"))
        elif service == "gslides" and t == "gslides.slides_presentations":
            out.append((r["presentation_id"], r.get("title") or ""))
        elif service == "gcal" and t == "gcal.gcal_events" and r["calendar_id"] == FRED:
            out.append((r["event_id"], f"{r.get('summary')} {r.get('description')}"))
        elif service == "trello" and t == "trello.trello_cards":
            out.append((r["id"], f"{r.get('name')} {r.get('desc')}"))
        elif service == "contacts" and t == "contacts.contacts":
            out.append((r["contact_id"], f"{r.get('first_name')} {r.get('last_name')} {r.get('job')}"))
    return out
res, raw = [], []
ONLY = set(sys.argv[1:])
OLD = {r["fid"]: r for r in json.load(open(os.path.join(HERE, "brief_searches.json")))} if ONLY else {}
OLDRAW = open(os.path.join(HERE, "brief_searches.txt")).read().rstrip("\n").split("\n\n") if ONLY else []
for n, f in enumerate(BF.F):
    if ONLY and f[0] not in ONLY:
        res.append(OLD[f[0]]); raw.append(OLDRAW[n]); continue
    fid, svc, q, want = f[0], f[6], f[7], f[8]
    args = ["python3", "-B", "Task_Authoring/tools/persona_view.py", "search", "frederick_stone", svc, q, "--limit", "10"]
    if svc in ("gmail", "slack"):
        args.append("--no-hidden")
    txt = subprocess.run(args, cwd=WS, capture_output=True, text=True, timeout=900)
    raw.append((txt.stdout + txt.stderr).strip())
    jp = subprocess.run(args + ["--json"], cwd=WS, capture_output=True, text=True, timeout=900)
    try:
        jd = json.loads(jp.stdout)
    except ValueError:
        jd = {}
    vis = jd.get("visible") or []
    hits = [str(h.get("id") or "") for h in vis]
    nvis = jd.get("visible_total", len(hits))
    hidden = jd.get("hidden_by_acl", jd.get("hidden"))
    seeded = sorted({i for i, t in seeded_units(svc) if q.lower() in (t or "").lower()})
    blob = json.dumps(vis)
    if want in hits:
        first, how = want, f"YES (base, hit {hits.index(want) + 1} of {len(hits)})"
    elif want in seeded or any(want.split('/')[-1] in s for s in seeded):
        first, how = want, "YES (seeded; check-sql YES)" if svc not in ("trello", "linear", "contacts") else "YES (seeded; unscoped)"
    elif want in blob or want.split('/')[-1] in blob:
        first, how = want, "YES (base, in the visible hits)"
    elif hits:
        first, how = hits[0], f"PARTIAL (base hits do not include {want})"
    else:
        first, how = None, "NO"
    res.append(dict(fid=fid, service=svc, query=q, want=want, base=nvis, seeded=len(seeded), hidden=hidden if svc not in ("gmail", "slack") else "n/a (--no-hidden)", first=first, found=how))
    print(fid, svc, repr(q), "base", nvis, "seeded", len(seeded), how, flush=True)
json.dump(res, open(os.path.join(HERE, "brief_searches.json"), "w"), indent=1)
open(os.path.join(HERE, "brief_searches.txt"), "w").write("\n\n".join(raw) + "\n")

#!/usr/bin/env python3
"""Brief §5a: run each discovery fact's natural query as Robert through tools/persona_view.py search (base data), count
the seeded rows Robert can see that carry the query (the SQL overlay persona_view does not read), and record the first
visible hit. Writes plan/brief_searches.json and plan/brief_searches.txt (verbatim outputs)."""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402

ROB = "robert@harmonygames.co"
S = json.load(open(os.path.join(HERE, "sql_ids.json")))
I = json.load(open(os.path.join(HERE, "ids.json")))
IDS, BASE = I["IDS"], I["BASE"]
STM = [x for x in parse_sql(open(os.path.join(TI, "01_Universe_Inject.sql")).read()) if x["op"] == "insert"]
ROB_SLACK = {"D04UP2L3E3S", "D04V95AAAHW", "C09UHHN6PFZ", "C05433XK267", "C0ADGSZKR3R", "C07C2866011", "C04UEQVDVB7"}
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")


def seeded_units(service):
    out = []
    for x in STM:
        r, t = x["row"], x["table"]
        if service == "gmail" and t == "gmail.gmail_messages" and r["user_email"] == ROB:
            out.append((r["thread_id"], f"{r.get('subject')} {r.get('body_text')}"))
        elif service == "slack" and t == "slack.slack_messages" and r["channel_id"] in ROB_SLACK:
            out.append((f"{r['channel_id']}/{r['ts']}", f"{r.get('text') or ''} {r.get('attachments_json') or ''}"))
        elif service == "gdocs" and t == "gdocs.docs_documents" and (ROB in str(r.get("shared_with_emails_json")) or r.get("owner_email") == ROB):
            out.append((r["document_id"], f"{r['title']} {r['body_text']}"))
        elif service == "gsheets" and t == "gsheets.sheets_spreadsheets" and ROB in str(r.get("shared_with_emails_json")):
            out.append((r["spreadsheet_id"], r.get("title")))
        elif service == "gslides" and t == "gslides.slides_page_elements":
            out.append((r["presentation_id"], r.get("text") or ""))
        elif service == "gcal" and t == "gcal.gcal_events" and r["calendar_id"] == ROB:
            out.append((r["event_id"], f"{r.get('summary')} {r.get('description')}"))
        elif service == "trello" and t == "trello.trello_cards":
            out.append((r["id"], f"{r.get('name')} {r.get('desc') or r.get(chr(34) + 'desc' + chr(34))}"))
        elif service == "linear" and t in ("linear.linear_issues", "linear.linear_comments", "linear.linear_projects"):
            out.append((r.get("identifier") or r["id"], f"{r.get('name') or ''} {r.get('title') or ''} {r.get('description') or ''} {r.get('body') or ''}"))
        elif service == "github" and t == "github.github_pull_requests":
            out.append((r["id"], f"{r.get('title')} {r.get('body')}"))
    return out


L = S["linear"]
Q = [  # (fid, service, natural query, id the row must reach)
    ("F1", "slack", "LLC", S["slack"]["hub"]["locator"]),
    ("F2", "linear", "LLC take-over", IDS["project"]),
    ("F3", "gdocs", "ground rules", IDS["ground_rules"]),
    ("F4", "gdocs", "LLC notes", IDS["notes_doc"]),
    ("F5", "gsheets", "LLC 90 days", IDS["draft_sheet"]),
    ("F6", "gmail", "LLC money", S["gmail"]["split_mail"][ROB]["thread"]),
    ("F7", "trello", "LLC", IDS["trello_card"]),
    ("F8", "gcal", "LLC", S["gcal"][ROB]),
    ("F9", "slack", "prod account", S["slack"]["arthur_dm"]["locator"]),
    ("F10", "snowflake", "REVENUE_DAILY", "ANALYTICS.MONETIZATION.REVENUE_DAILY"),
    ("F11", "gmail", "metabase", S["gmail"]["arthur_mail"][ROB]["thread"]),
    ("F12", "slack", "meta campaigns", S["slack"]["vo_status"]["locator"]),
    ("F13", "gslides", "VO campaign", IDS["cf_deck"]),
    ("F14", "gmail", "noticed an issue", S["gmail"]["asc_notice"][ROB]["thread"]),
    ("F15", "linear", "player support", L["Domino Delights player support"]["issue"]),
    ("F16", "github", "Replace Helpshift", IDS["pr"]),
    ("F17", "slack", "DD iOS Submission", S["slack"]["builds_result"]["locator"]),
    ("F18", "slack", "calm play", BASE["calm_owned"]),
    ("F19", "linear", "Calm Play", L["Calm Play LLC"]["issue"]),
    ("F20", "slack", "access until March", BASE["layer_mar3"]),
    ("F21", "slack", "subscriptions", BASE["checklist"]),
    ("F22", "slack", "off Helpshift", BASE["helpshift_feb28"]),
    ("F23", "slack", "KubLLC", BASE["arthur_kub"]),
    ("F24", "slack", "lifestyle", BASE["lifestyle"]),
    ("F25", "slack", "auction", BASE["auction"]),
    ("F26", "confluence", "AWS Infrastructure Guide", "page_aws_infra"),
    ("F27", "linear", "backend and auth stacks", L["Combo Fighter backend and auth stacks (AWS)"]["issue"]),
    ("F28", "slack", "build machines", "C07C2866011/1770839126.382429"),
    ("F29", "slack", "Figma is good", BASE["figma_sep11"]),
    ("F30", "slack", "15K installs", BASE["appsflyer"]),
    ("F31", "slack", "$100 we have", BASE["unity_100"]),
    ("F32", "gmail", "jenkins", S["gmail"]["jenkins_mail"][ROB]["thread"]),
    ("F33", "slack", "layer.ai", S["slack"]["layer_reply"]["locator"]),
]

ONLY = set(filter(None, os.environ.get("ONLY", "").split(",")))
OLD = {r["fid"]: r for r in json.load(open(os.path.join(HERE, "brief_searches.json")))} if ONLY else {}
OLDRAW = open(os.path.join(HERE, "brief_searches.txt")).read().split("\n\n") if ONLY else []
res, raw = [], []
for n, (fid, svc, q, want) in enumerate(Q):
    if ONLY and fid not in ONLY:
        res.append(OLD[fid]); raw.append(OLDRAW[n] if n < len(OLDRAW) else ""); continue
    args = ["python3", "-B", "Task_Authoring/tools/persona_view.py", "search", "robert", svc, q, "--limit", "25" if fid in ("F21", "F24") else "10"]
    if svc in ("gmail", "slack"):
        args.append("--no-hidden")
    try:
        p = subprocess.run(args, cwd=WS, env=ENV, capture_output=True, text=True, timeout=1500)
        txt = (p.stdout + p.stderr).strip()
    except subprocess.TimeoutExpired:
        txt = f"SEARCH {svc} {q!r} as robert  scope: (timed out after 1500 s)"
    raw.append(txt)
    m = re.search(r"visible hits=(\d+)", txt)
    nvis = int(m.group(1)) if m else 0
    mh = re.search(r"hidden by ACL=(\S+)", txt)
    hidden = mh.group(1) if mh and svc not in ("gmail", "slack") else "n/a (--no-hidden)"
    ids = []
    for line in txt.splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                h = json.loads(line)
            except ValueError:
                continue
            hid = h.get("id") or h.get("pointer")
            if svc == "slack" and h.get("channel") and h.get("ts"):
                hid = f"{h['channel']}/{h['ts']}"
            ids.append(str(hid))
    seeded = sorted({i for i, t in seeded_units(svc) if q.lower() in (t or "").lower()})
    base_hit = any(want in x or x.endswith(want.split("/")[-1]) for x in ids) or (want in txt)
    if base_hit:
        first, how = want, "YES (base hit)"
    elif want in seeded:
        first, how = want, "YES (seeded; check-sql YES)" if svc not in ("trello", "linear", "github") else "YES (seeded; unscoped)"
    elif ids:
        first, how = ids[0], f"YES (base hits; target {want} reached by reading the hit's thread/table)" if svc in ("snowflake", "confluence") else f"PARTIAL (base hits do not include {want})"
    else:
        first, how = None, "NO"
    res.append(dict(fid=fid, service=svc, query=q, want=want, base=nvis, seeded=len(seeded), hidden=hidden, first=first, found=how))
    print(fid, svc, repr(q), "base", nvis, "seeded", len(seeded), how, flush=True)
json.dump(res, open(os.path.join(HERE, "brief_searches.json"), "w"), indent=1)
open(os.path.join(HERE, "brief_searches.txt"), "w").write("\n\n".join(raw) + "\n")

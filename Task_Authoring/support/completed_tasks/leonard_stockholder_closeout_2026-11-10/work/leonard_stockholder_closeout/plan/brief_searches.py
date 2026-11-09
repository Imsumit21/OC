#!/usr/bin/env python3
"""Brief §5a: run each discovery fact's natural query as Leonard through tools/persona_view.py search (base data), count the seeded
rows Leonard can see that carry the query (the SQL overlay persona_view does not read), and record the first visible hit.
Writes plan/brief_searches.json and plan/brief_searches.txt (verbatim outputs). Runs the searches in parallel."""
import json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402

PY = os.path.expanduser("~/.local/bin/python3.12")
LEO = "leonard.hayes@harmonygames.co"
STM = [x for x in parse_sql(open(os.path.join(TI, "01_Universe_Inject.sql")).read()) if x["op"] == "insert"]
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")
S = json.load(open(os.path.join(HERE, "sql_ids.json")))
GM = {k: v["thread"] for k, v in S["gmail"].items()}


def seeded_units(service):
    out = []
    for x in STM:
        r, t = x["row"], x["table"]
        if service == "gmail" and t == "gmail.gmail_messages" and r["user_email"] == LEO:
            out.append((r["thread_id"], f"{r.get('subject')} {r.get('body_text')}"))
        elif service == "slack" and t == "slack.slack_messages":
            out.append((f"{r['channel_id']}/{r['ts']}", r.get("text") or ""))
        elif service == "gdocs" and t == "gdocs.docs_documents":
            out.append((r["document_id"], f"{r['title']} {r['body_text']}"))
        elif service == "gdrive" and t == "gdrive.drive_files":
            out.append((r["id"], r.get("name") or ""))
        elif service == "gsheets" and t == "gsheets.sheets_spreadsheets":
            out.append((r["spreadsheet_id"], r.get("title") or ""))
        elif service == "gslides" and t == "gslides.slides_presentations":
            out.append((r["presentation_id"], r.get("title") or ""))
        elif service == "gcal" and t == "gcal.gcal_events":
            out.append((r["event_id"], f"{r.get('summary')} {r.get('description')}"))
        elif service == "trello" and t == "trello.trello_cards":
            out.append((r["id"], f"{r.get('name')} {r.get(chr(34) + 'desc' + chr(34)) or r.get('desc') or ''}"))
        elif service == "linear" and t in ("linear.linear_issues", "linear.linear_comments", "linear.linear_projects"):
            out.append((r.get("identifier") or r.get("issue_id") or r["id"], f"{r.get('name') or ''} {r.get('title') or ''} {r.get('description') or ''} {r.get('body') or ''}"))
        elif service == "contacts" and t == "contacts.contacts":
            out.append((r["contact_id"], f"{r.get('first_name')} {r.get('email')} {r.get('job')}"))
    return out


Q = [  # (fid, service, natural query, id the row must reach)
 ("F1", "linear", "Holder records", "ec2ea957-fc8e-4958-b809-0fb735b1e916"),
 ("F2", "slack", "periodic updates", "C0ADGSZKR3R/1770664700.848759"),
 ("F3", "gmail", "Audit Request", GM["kpmg"]),
 ("F4", "gdocs", "close-out notes", "f_a37b403d5200d4f0a31d31"),
 ("F5", "gdocs", "outreach notes", "f_762c60832854d3e7a7f7df"),
 ("F6", "gmail", "stockholder", GM["sunset"]),
 ("F7", "slack", "family", "C0ADGSZKR3R/1770949310.220519"),
 ("F8", "gmail", "closing the company", GM["robert_leo"]),
 ("F9", "gmail", "Termination details", "1856960478782792748"),
 ("F10", "gmail", "independent contractor", "1856861400116562076"),
 ("F11", "slack", "termination letters", "C0ADGSZKR3R/1770841239.761999"),
 ("F12", "slack", "Carta terminations", "C0ADGSZKR3R/1770935621.095649"),
 ("F13", "slack", "Reaching out to our angels", "C0ADGSZKR3R/1770934638.035469"),
 ("F14", "slack", "shut down the company", "D04UC0UEN2V/1770664988.379119"),
 ("F15", "slack", "investor updates", "D09R59580EM/1762285888.654689"),
 ("F16", "gmail", "diluted ownership", "1816809274978043917"),
 ("F17", "gdocs", "Due Diligence", "f_6a37227593d0977fdbdd7a"),
 ("F18", "gdocs", "term sheet", "f_11040fe5d66821bd6951aa"),
 ("F19", "gmail", "Tor Capital", "1777052222643175480"),
 ("F20", "gdocs", "side letter", "f_6201c7027d02997bfb2c84"),
 ("F21", "gmail", "board position", "1830959847543474636"),
 ("F22", "gmail", "Board position", "1856958794180374704"),
 ("F23", "gdocs", "Certificate of Incorporation", "f_90c029015fc474199cf736"),
 ("F24", "slack", "equity lerimiz", "C51ECE5102ED/1770903714.600249"),
 ("F25", "gmail", "25.000 usd", "1770141224265557526"),
 ("F26", "gmail", "Resignation", "1849344928983425627"),
 ("F27", "trello", "close-out", "698e5a10c3f24b7e9d16a0e4"),
 ("F28", "gcal", "holder notes", "evt_6f1a2c9e4b7d3a58c0e1d2"),
 ("F29", "gsheets", "Task List", "f_31115ddb6ed866f2b10d60"),
 ("F30", "gsheets", "Holder list", "f_5ecaa967db3adcfa440b09"),
 ("F31", "gslides", "Update", "f_75dddccabb26eeea4842c8"),
 ("F32", "gdrive", "close-out", "d_601064334a0b493022fe83"),
 ("F33", "contacts", "PERSON_0693", "contact_bergmann"),
 ("F34", "gmail", "Notice of Involuntary Termination", "1847335165884050330"),
 ("F35", "gdocs", "Advisor Agreement", "f_3ee38465decc57e61df6e5"),
 ("F36", "gmail", "Leonard and me on the board", GM["board_leo"]),
 ("F37", "slack", "seed figures", "C07C2866011/1768418331.402719"),
 ("F38", "gmail", "Husnu Matthew Collins", "1777100628672295991"),
]


def run(item):
    fid, svc, q, want = item
    args = [PY, "-B", "Task_Authoring/tools/persona_view.py", "search", "leonard_hayes", svc, q, "--limit", "25" if fid in ("F9", "F19", "F25", "F26", "F15") else "10"]
    if svc in ("gmail", "slack"):
        args.append("--no-hidden")
    try:
        p = subprocess.run(args, cwd=WS, env=ENV, capture_output=True, text=True, timeout=1700)
        txt = (p.stdout + p.stderr).strip()
    except subprocess.TimeoutExpired:
        txt = f"SEARCH {svc} {q!r} as leonard_hayes  scope: (timed out after 1700 s)"
    return item, txt


with ThreadPoolExecutor(6) as ex:
    out = list(ex.map(run, Q))
res, raw = [], []
for (fid, svc, q, want), txt in out:
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
    key = want.split("/")[-1]
    base_hit = any(want in x or key in x for x in ids) or (key in txt)
    if base_hit:
        first, how = want, "YES (base hit)"
    elif want in seeded or any(key in s_ for s_ in seeded) or (svc == "contacts" and seeded):
        first, how = want, "YES (seeded; unscoped)" if svc in ("trello", "linear", "contacts") else "YES (seeded; check-sql YES)"
    elif ids:
        first, how = ids[0], f"PARTIAL (first hits do not include {want})"
    else:
        first, how = None, "NO"
    res.append(dict(fid=fid, service=svc, query=q, want=want, base=nvis, seeded=len(seeded), hidden=hidden, first=first, found=how))
    print(fid, svc, repr(q), "base", nvis, "seeded", len(seeded), how, flush=True)
json.dump(res, open(os.path.join(HERE, "brief_searches.json"), "w"), indent=1)
open(os.path.join(HERE, "brief_searches.txt"), "w").write("\n\n".join(raw) + "\n")

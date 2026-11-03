#!/usr/bin/env python3
"""Search-as-persona proof for the brief: base competition (persona_view.py search, verbatim) + seeded hits Frederick
can see in the SQL overlay (case-insensitive substring over each visible seeded row). Read-only."""
import json, subprocess, sys
from pathlib import Path
WS = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(WS / "Task_Authoring/tools"))
from base_check import parse_sql
FRED = "frederick.stone@harmonygames.co"
SQL = (WS / "Task_Authoring/task_inputs/01_Universe_Inject.sql").read_text()
rows = [x for x in parse_sql(SQL) if x["op"] == "insert"]
FACTS = [   # (fact, label, service, natural query, deciding record)
 ("F1", "hub ask", "gmail", "board pre-read", "frederick.stone@harmonygames.co/1844724419788800011"),
 ("F2", "Oct 14 template (July decoy beside it)", "gdocs", "board pre-read", "f_3b9e61c04d7a52e8f1a6c2"),
 ("F3", "2025 game investor list", "gsheets", "Game Investor List", "f_48247af79428823c3cac92"),
 ("F4", "angel post", "slack", "Paul Heydon", "C07C2866011/1758303600.418207"),
 ("F5", "angels sheet", "gsheets", "Bridge angels", "f_6e1d93a0c4b72f85d39a0e"),
 ("F6", "Anton's amount mail", "gmail", "Anton", "frederick.stone@harmonygames.co/1844162278195200023"),
 ("F7", "DocuSign Completed (Anton)", "gmail", "docusign", "frederick.stone@harmonygames.co/1844354293432320031"),
 ("F8", "Paul's unsigned SAFE nudge", "gmail", "Paul Heydon", "frederick.stone@harmonygames.co/1844610859008000037"),
 ("F9", "Dentsu tester invites thread", "gmail", "PERSON_5221", "frederick.stone@harmonygames.co/1844294398771200045"),
 ("F10", "tester ticket", "linear", "tester", "ZOM-567"),
 ("F11", "Sciplay phone pass", "slack", "Sciplay", "C096HFA5Z8W/1759184040.552871"),
 ("F12", "SciPlay mail thread", "gmail", "SciPlay", "frederick.stone@harmonygames.co/1842285743246816270"),
 ("F13", "unnamed-firm pass mail", "gmail", "bridge", "frederick.stone@harmonygames.co/1844318935449600041"),
 ("F14", "Edith Vane contact", "contacts", "Edith", "e3a91c07d5b48f26a0c7e314"),
 ("F15", "Tuesday pitch call", "gcal", "Leonard Hayes", "evt_7d3e19b04a6c25f8e1b9a0"),
 ("F16", "Brightwater call", "gcal", "Leonard Hayes", "evt_2f86b0d4c9e17a35b64e0d"),
 ("F17", "Ilse Marrow contact", "contacts", "Ilse", "b72f0d6e19c3a84e5d21f9a0"),
 ("F18", "Brightwater follow-up", "gmail", "Ilse", "frederick.stone@harmonygames.co/1844276782694400053"),
 ("F19", "Homa invitation", "gmail", "PERSON_5173_NAME", "frederick.stone@harmonygames.co/1843169166284025277"),
 ("F20", "Homa call", "gcal", "Leonard Hayes", "evt_89381fe5a15b802c5652a9"),
 ("F21", "keep-warm rule card", "trello", "Existing Investor Update", "68c64270d660c977c4696986"),
 ("F22", "Board Deck card", "trello", "Board Deck", "68d8193cf451863621c88a2a"),
 ("F23", "draft board deck", "gslides", "Oct 14", "f_a47d0e2c95b18f63e2c0d5"),
 ("F24", "Board folder", "gdrive", "Board - Oct 14 2025", "d_5e8a1c3f9b07d2e64a1b93"),
 ("F25", "folder README", "gdocs", "README", "f_c61a0e93b7d24f58a2e917"),
 ("F26", "review event", "gcal", "Board pre-read review", "evt_9c41e7a2d05b38f6e1a7c4"),
 ("F27", "LVP pass", "gmail", "LVP", "frederick.stone@harmonygames.co/1842277743427687737"),
 ("F28", "T-accelerate recap", "gmail", "T-accelerate", "frederick.stone@harmonygames.co/1842283406259093714"),
 ("F29", "PXLite is T-accelerate", "gmail", "PXLite", "frederick.stone@harmonygames.co/1843978997950200606"),
 ("F30", "Karthic contact", "contacts", "Karthic", "5d0e8b31f7a29c64e1b0d3a8"),
 ("F31", "Robert's board mail", "gmail", "pipeline", "frederick.stone@harmonygames.co/1844623441920000059"),
 ("F32", "Arthur's aside", "slack", "pipeline", "C07C2866011/1759168800.117903"),
]
SVC_TABLES = {"gmail": ["gmail.gmail_messages"], "gdocs": ["gdocs.docs_documents"], "gsheets": ["gsheets.sheets_spreadsheets", "gsheets.sheets_sheets"],
              "slack": ["slack.slack_messages"], "linear": ["linear.linear_issues", "linear.linear_comments"], "contacts": ["contacts.contacts"],
              "gcal": ["gcal.gcal_events"], "trello": ["trello.trello_cards", "trello.trello_actions"], "gslides": ["gslides.slides_presentations"],
              "gdrive": ["gdrive.drive_files"]}
FRED_CH = {"C07C2866011", "C096HFA5Z8W"}


def visible(table, r):
    if table.startswith("gmail."):
        return r.get("user_email") == FRED
    if table.startswith("gcal."):
        return r.get("calendar_id") == FRED
    if table.startswith("slack."):
        return r.get("channel_id") in FRED_CH
    if table.split(".")[0] in ("gdrive", "gdocs", "gsheets", "gslides"):
        return r.get("owner_email") == FRED or FRED in str(r.get("shared_with_emails_json") or "")
    return True                       # trello, linear, contacts: unscoped


def key(table, r):
    for k in ("id", "document_id", "spreadsheet_id", "presentation_id", "event_id", "contact_id", "identifier"):
        if r.get(k):
            if table == "slack.slack_messages":
                return f"{r['channel_id']}/{r['ts']}"
            if table == "gmail.gmail_messages":
                return r["thread_id"]
            return r[k]
    return "?"


out_md, out_txt = [], []
for fid, label, svc, q, want in FACTS:
    cmd = [sys.executable, str(WS / "Task_Authoring/tools/persona_view.py"), "search", "frederick_stone", svc, q, "--limit", "15", "--no-hidden"]
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=str(WS)).stdout.strip()
    out_txt.append(res)
    first = res.splitlines()[1] if len(res.splitlines()) > 1 else ""
    import re
    m = re.search(r"visible hits=(\d+)", first)
    base = int(m.group(1)) if m else 0
    hid = re.search(r"hidden by ACL=(\S+)", first)
    seeded = [key(x["table"], x["row"]) for x in rows if x["table"] in SVC_TABLES[svc] and visible(x["table"], x["row"])
              and q.casefold() in json.dumps(x["row"], ensure_ascii=False).casefold()]
    seeded = list(dict.fromkeys(seeded))
    hit_ids = re.findall(r'"id": "([^"]+)"', res)
    rank = (hit_ids.index(want) + 1) if want in hit_ids else None
    in_seed = want in seeded
    found = "YES" if (in_seed or rank) else "NO"
    if in_seed:
        note = "seeded; check-sql YES" if svc in ("gmail", "gcal", "slack", "gdrive", "gdocs", "gsheets", "gslides") else "seeded; unscoped"
    elif rank:
        note = f"base, hit {rank} of {base}"
    else:
        note = "not in the shown hits"
    out_md.append(f"| {fid} {label} | {svc} | \"{q}\" | base {base}; seeded {len(seeded)} | {hid.group(1) if hid else '0'} | {want} | {found} ({note}) |")
P = Path(__file__).resolve().parent
(P / "search_rows.md").write_text("\n".join(out_md) + "\n")
(P / "search_out.txt").write_text("\n\n".join(out_txt) + "\n")
print("\n".join(out_md))

#!/usr/bin/env python3
"""Render Working_Files/01_Grounding_Dossier.md for the ZM3D Halloween art plan injection (rev1).

Tables that name records are generated from the SQL (tools/base_check.parse_sql), roster_final.json, ids.json and the
final manifest; tool outputs are re-run here and pasted verbatim. Hand-written analysis lives in this file and in
injection_gen/research/*.md. Never executes SQL; writes only the dossier.

    python3 -B Task_Authoring/task_inputsN2/Working_Files/injection_gen/build_dossier.py
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
ROOT = TASK.parents[1]
TOOLS = ROOT / "Task_Authoring" / "tools"
sys.path.insert(0, str(TOOLS))
from base_check import parse_sql  # noqa: E402

SQLP = TASK / "01_Universe_Inject.sql"
SQL = SQLP.read_text()
M = json.loads((WF / "01_Hardness_Manifest.json").read_text())
SG = WF / "scenario_gen"
FINAL = json.loads((SG / "roster_final.json").read_text())
R = FINAL["surfaces"]
BY = {r["key"]: r for r in R}
ARCH = FINAL["archived"]
I = json.loads((SG / "ids.json").read_text())["ids"]
T = json.loads((SG / "planned_texts.json").read_text())
CTX = json.loads((WF / "00_Task_Context.json").read_text())
RO = json.loads((SG / "rubric_only_facts.json").read_text())
TRUTH = json.loads((WF / "solver" / "truth.json").read_text())
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(TASK.relative_to(ROOT)))
REL = str(TASK.relative_to(ROOT))


def run(*args, timeout=900) -> str:
    p = subprocess.run([sys.executable, "-B", *map(str, args)], cwd=ROOT, env=ENV, capture_output=True, text=True,
                       timeout=timeout)
    return (p.stdout.rstrip() + ("\n" + p.stderr.rstrip() if p.stderr.strip() and not p.stdout.strip() else "")).rstrip()


def fence(t: str) -> str:
    return "```text\n" + t.rstrip() + "\n```"


def table(head, rows) -> str:
    out = ["| " + " | ".join(head) + " |", "| " + " | ".join("---" for _ in head) + " |"]
    out += ["| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in r) + " |" for r in rows]
    return "\n".join(out)


ASK, POINTER, EXPORT = I["slack_ask"]["locator"], I["slack_robert_pointer"]["locator"], I["slack_martin_export"]["locator"]
DM_ROOT, DM_REPLY = I["slack_dm_root"]["locator"], I["slack_dm_marcus_reply"]["locator"]
SHEET, DOC, DECK = I["sheet_live"], I["doc_release"], I["deck_seasonal"]["presentation"]
PLAN, DRAFT, QUOTE = I["gmail_fred_plan"], I["gmail_fred_draft"], I["gmail_vendor_quote"]
EVT, UID = I["gcal_review"]["evt_by_calendar"], I["gcal_review"]["ical_uid"]
F = I["folder_halloween"]
CARD, CARD_ACT, CARD_CMT, CONTACT = I["trello_card"], I["trello_card_create_action"], I["trello_comment"], I["contact_vendor"]
ADS = [r for r in R if r.get("ticket")]
STMTS = parse_sql(SQL)
SLACK_ID = {I[k]["row_id"]: I[k]["locator"] for k in ("slack_ask", "slack_robert_pointer", "slack_martin_export",
                                                     "slack_dm_root", "slack_dm_marcus_reply")}
CLAIRE = "claire.morgan@harmonygames.co"

# ------------------------------------------------------------------ tool outputs (re-run, pasted verbatim)
OUT = {
    "lint": run(TOOLS / "sql_lint.py", SQLP),
    "base": run(TOOLS / "base_check.py", SQLP),
    "claims": run(TOOLS / "base_claims.py", SQLP, "--task-dir", TASK),
    "fact": run(TOOLS / "fact_check.py", SQLP, "--manifest", WF / "01_Hardness_Manifest.json", "--no-leak"),
    "reach": run(TOOLS / "persona_view.py", "check-sql", "claire_morgan", SQLP, "--load-bearing", HERE / "load_bearing_ids.txt"),
    "gate": run(TOOLS / "hardness_gate.py", WF / "01_Hardness_Manifest.json", SQLP),
    "oracle": run(TOOLS / "oracle_kit.py", "check", "--task-dir", TASK),
}
_lint = json.loads(run(TOOLS / "hg.py", "lint", "--task-dir", TASK))
OUT["hglint"] = json.dumps({"tool": _lint.get("tool"), "version": _lint.get("version"), "sql": _lint.get("sql"),
                            "sha256": _lint.get("sha256"), "universe": _lint.get("universe"), "clock": _lint.get("clock"),
                            "counts": _lint.get("counts"), "flags": _lint.get("flags") or "none", "info": _lint.get("info")}, indent=1)
PRE = json.loads((WF / "01c_Preflight_Report.json").read_text())
FC_TXT = (WF / "01c_Forecast.txt").read_text() if (WF / "01c_Forecast.txt").exists() else ""
FC = json.loads((WF / "01c_Forecast.json").read_text())
HEV = (FC.get("preregistration") or {}).get("id")
VOICE = (HERE / "research" / "voice.md").read_text()
KEYW = (HERE / "research" / "keywords.md").read_text() if (HERE / "research" / "keywords.md").exists() else ""


def section_of(md: str, start_rx: str) -> str:
    """The body of a research file from the first line matching start_rx to the end (headings demoted)."""
    lines = md.splitlines()
    i = next((n for n, l in enumerate(lines) if re.search(start_rx, l)), 0)
    return "\n".join(l if not l.startswith("#") else "**" + l.lstrip("# ").strip() + "**" for l in lines[i:]).strip()


# ------------------------------------------------------------------ record ledger from the SQL
def element_of(table: str, row: dict) -> tuple:
    """(manifest element, carrier, reach path, discovery role) for one statement."""
    rid = row.get("id") or row.get("document_id") or row.get("spreadsheet_id") or row.get("presentation_id") or \
        row.get("event_id") or row.get("contact_id") or ""
    if table == "slack.slack_messages":
        loc = SLACK_ID.get(rid, rid)
        return {ASK: ("A1 / K9 K10 K13 K14 K17 / T2 T16", "●", "#zombie_marketing member", "first link (hub)"),
                POINTER: ("K3 (names H3)", "●", "#zombie-art member", "connecting"),
                EXPORT: ("K15 / T1 / CH1", "●", "#zombie-art member", "claim met first"),
                DM_ROOT: ("K16 / T3 (thread parent)", "●", "Claire's IM with Marcus", "connecting"),
                DM_REPLY: ("K16 / T3 T19 / CH4", "●", "Claire's IM with Marcus (thread reply)", "overturning evidence")}[loc]
    if table == "linear.linear_issues":
        a = next((x for x in ARCH if x["ticket"] == rid), None)
        if a:
            return ("T14 (archived library ticket)", "●", "Linear unscoped", "decoy")
        r = next(x for x in ADS if x["ticket"] == rid)
        el = "cohort K11" + (" / T6 CH7 (off the sheet)" if not r["on_sheet"] else "")
        return (el, "●", "Linear unscoped", "evidence + write target")
    if table == "linear.linear_comments":
        r = next(x for x in ADS if x["ticket"] == row["issue_id"])
        tag = {"couch alpha 50": "T9", "barrel marketing2 4:5": "T9", "balloons alpha 50 (1)": "T9",
               "boris fastcouch 9:16": "T8 CH2", "boris alin2 9:16": "T8", "marcus.bennett 9:16": "T8",
               "marcus portrait UA end card": "T17", "cheer fastcouch 4:5": "T19", "cheer fastcouch 9:16": "T3",
               "couch alpha 50 16:9": "T18", "balloons alpha 50 (1) 16:9": "T18"}.get(r["key"], "cohort evidence")
        return (f"K11 per-record ({tag})", "●", "Linear unscoped", "per-record evidence")
    if table == "gdrive.drive_files":
        if rid == F["root"]:
            return ("K12 (root)", "○ listing", "shared with Claire (writer)", "connecting")
        if rid == F["store"]:
            return ("K12 / T1 / CH1", "○ listing", "shared with Claire", "overturning evidence")
        if rid == F["ua"]:
            return ("K12 / T3 / CH4", "○ listing", "shared with Claire", "alternate path")
        if rid in I["files_store"]:
            return ("T1 (Halloween iPhone / Play export)", "○ name", "shared with Claire", "evidence")
        if rid in I["files_ua"]:
            return ("T3 (the two Halloween cuts)", "○ name", "shared with Claire", "alternate path")
        return ({SHEET: "H1 / K1 / K7 / K11", DOC: "H2 / K2", DECK: "H3 / K4"}[rid], "●", "shared with Claire (reader)",
                "authority")
    if table.startswith("gsheets."):
        return ("H1 / K1 (sheet tab)", "●", "shared with Claire", "authority")
    if table == "gdocs.docs_documents":
        return ("H2 / K2", "●", "shared with Claire", "authority")
    if table.startswith("gslides."):
        return ("H3 / K4 (deck)", "● element text", "shared with Claire", "authority")
    if table == "gmail.gmail_messages" or table == "gmail.gmail_threads":
        if QUOTE["msg"] in rid or QUOTE["thread"] == rid:
            return ("T7 / CH5 (vendor quote)", "●", "Claire's mailbox INBOX", "decoy")
        draft = rid in (DRAFT["copies"].values()) or DRAFT["msg"].split("/", 1)[1] in rid
        own = (row.get("user_email") or "") == CLAIRE
        el = "K6 / T4 (Sep 12 draft)" if draft else "H4 / K5 / T4 T18 (Sep 30 changes)"
        return (el + ("" if own else " · recipient copy"), "●", "Claire's mailbox INBOX" if own else "other mailbox (not read)",
                ("superseded version" if draft else "authority") if own else "companion copy")
    if table == "gcal.gcal_events":
        own = row.get("calendar_id") == CLAIRE
        return ("K8 (review deadline)" + ("" if own else " · attendee copy"), "● time fields", "Claire's calendar" if own
                else "attendee calendar", "destination deadline" if own else "companion copy")
    if table == "trello.trello_cards":
        return ("K7 (Halloween push card)", "●", "Trello unscoped", "connecting")
    if table == "trello.trello_actions":
        return ("K7 / T6 / CH7 (Julia's 4:5 static)" if rid == CARD_CMT else "K7 (card creation)", "●",
                "Trello unscoped", "overturning evidence" if rid == CARD_CMT else "companion")
    if table == "trello.trello_boards":
        return ("K7 companion (board activity)", "-", "Trello unscoped", "companion")
    if table == "contacts.contacts":
        return ("T7 / CH5 (vendor identity)", "○ job", "Contacts unscoped", "alias bridge")
    return ("?", "?", "?", "?")


ledger = []
for n, s in enumerate(STMTS, 1):
    row = s.get("row") or s.get("set") or {}
    where = s.get("where") or {}
    rid = (row.get("id") or row.get("document_id") or row.get("spreadsheet_id") or row.get("presentation_id")
           or row.get("event_id") or row.get("contact_id") or where.get("id") or "")
    shown = SLACK_ID.get(rid, rid)
    if s["table"] == "gsheets.sheets_sheets":
        shown = f"{rid}#{row.get('sheet_id')} ({row.get('title')})"
    elif s["table"] == "gslides.slides_pages":
        shown = f"{rid} / {row.get('object_id')}"
    elif s["table"] == "gslides.slides_page_elements":
        shown = f"{rid} / {row.get('object_id')}"
    el, car, reach, role = element_of(s["table"], {**row, **where, "id": rid})
    cont = {"slack.slack_messages": f"slack:{shown.split('/')[0]}" if "/" in shown else "slack",
            "linear.linear_comments": f"linear:{row.get('issue_id')}"}.get(s["table"], s["table"].split(".")[0])
    ledger.append([n, s["table"].split(".")[0], s["table"] + (" (update)" if s["op"] == "update" else ""), shown, cont, el,
                   car, reach, role])

# ------------------------------------------------------------------ document
doc = []
A = doc.append
latest = max(re.findall(r"20\d\d-\d\d-\d\dT\d\d:\d\d:\d\d", SQL.replace("2025-10-02T16", "")))
A(f"""# Grounding Dossier — claire-zm3d-halloween-art-plan · rev1 · contains no prompt, OE or criterion text

{CTX['universe']['clock_line']}. Seed bound {CTX['freeze_utc']}: every seeded created / sent / updated / ts value is at
or before it (latest seeded event: Frederick's Trello comment {CARD_CMT} at 2025-09-30T23:20:00Z). Only plan fields
are later: the review event's start and end (2025-10-02T16:00Z–16:30Z, {EVT[CLAIRE]}) and the dates the calendar doc
and the mails name.

Files: `01_Universe_Inject.sql` (generated by `Working_Files/injection_gen/gen_sql.py` from `scenario_gen/roster_final.json`,
`scenario_gen/planned_texts.json` and `scenario_gen/ids.json`), final manifest `Working_Files/01_Hardness_Manifest.json`
(`injection_gen/build_final_manifest.py`), solver `Working_Files/solver/solver.py` + `truth.json`, dispositions
`Working_Files/01c_Dispositions.json` (`injection_gen/write_dispositions.py`), preflight `Working_Files/01c_Preflight_Report.json`,
stored revision `Working_Files/run_forensics/rev1/01_Universe_Inject.sql`. Persona: Claire Morgan
(claire.morgan@harmonygames.co), Art Lead · Design · Long Horizon · medium · {CTX['universe']['label']}.

Design delta at this stage: none (`design_delta: []`). Scenario revision 02/02b (twelve more serving exports, campaigns
moved to the ticket comments, honest minimal budget 192 > the requester's 181) was taken back through `/create-scenario`
and its gate before this SQL was written (`01_Scenario_Design.md` section 13).
""")

A("""## 1.A Structural

Columns follow `references/universe_schema_live.json`; every NOT NULL column is supplied; the generated
`slack_messages.text_fts` / `gmail_messages.body_text_fts` columns are never written; `"references"`, `"index"`,
`"desc"` and every camelCase Trello column are quoted. Shapes were copied from real sibling records (the accepted
sibling SQL `Task_Authoring/task_inputsH/01_Universe_Inject.sql`, which passed `/injection` on the same universe).

""" + table(["Table", "Base location / count", "Timestamp format used", "Sibling record copied"], [
    ["slack.slack_messages", "slack messages/C06DJBJL798 (#zombie_marketing, private), messages/C08R8CHB0QL (#zombie-art, public), messages/D05V2N6PZNU (Claire–Marcus IM)", "ts `1759269913.882683`; created_at with the same micros", "C06DJBJL798/1756914854.743319 (Leonard's export ask, top-level); D05V2N6PZNU/1758270333.226649 (IM)"],
    ["linear.linear_issues / linear_comments", "linear data.json /issues (ART max ART-792, 597 ART issues); /comments: 0 base rows", "`2025-09-08T16:00:00Z` varchar ISO-Z", "ART-790 (Todo) / ART-792 (Team Epic): creator usr_175c0d7bc72ed244 Frederick, assignee Martin, team_ART, no labels"],
    ["gmail.gmail_threads / gmail_messages", "gmail threads/claire@harmonygames.co_*.json (846), frederick@ / leonard@ / marcus.bennett@ / martin.walsh@ files", "`2025-09-30T23:10:00Z`, internal_date ms, RFC 2822 Date header -0700", "frederick.stone@harmonygames.co/<CANf1NxdX_-=ufVrJRkObveGnt5gFc9BwveE1Phwxpp_8zfTrjA@mail.gmail.com> (from-name 'frederick stone')"],
    ["gcal.gcal_events", "gcal data.json /events (10,395 rows)", "start/end ts + start_json dateTime", "evt_bf2235816b35c5cc9577c7 shape (task_inputsH, one row per attendee calendar, self on the owner's copy)"],
    ["gdrive.drive_files", "gdrive data.json /drive_files (53,631)", "`2025-09-30T15:12:04Z`", "roots d_63fffeb4fab5233ed5bb73 (Leonard), d_175c0d7bc72ed244b944cb (Frederick), d_cc3e90160f490686039986 (Arthur), d_9f7ba94f7526d54d8482ba (Robert)"],
    ["gdocs.docs_documents", "gdocs data.json (595 documents)", "as Drive", "f_1265318f45054aaef57a4a shape (TITLE style run, 10-hex revision_id)"],
    ["gsheets.sheets_spreadsheets / sheets_sheets", "gsheets data.json", "as Drive", "f_3f40599bbc9095352d47ab shape (grid rows of strings, row_count 1000)"],
    ["gslides.slides_presentations / slides_pages / slides_page_elements", "gslides data.json (132 decks, BLANK layouts)", "as Drive", "f_b0809b6ca90ef8d44f391d shape (slide_<12hex>, el_<12hex>, 9144000 emu wide)"],
    ["trello.trello_cards / trello_actions / trello_boards (update)", "trello data.json (ZM ROADMAP 6851a6569f3bf818760632ab: 79 cards, max idShort 79, dateLastActivity 2025-09-30T17:09:07Z; list 6851a677e090018224fb8c7f 'Oct 21')", "`2025-09-30T22:00:00Z`; id = hex(unix seconds) + 16 hex", "68d1eb90bef538c7c5c559bc (createCard by PERSON_6094_TRELLO_USER_ID); 68655f93de2e202c2ad77a76 (commentCard data_json shape)"],
    ["contacts.contacts", "contacts contacts.json (170 rows)", "created_at/updated_at ISO-Z", "78f786dcee835fdfb72aba2a (external: first_name PERSON_n, last_name '', email PERSON_n_EMAIL, gender/status Unknown)"],
]) + "\n")

A("""## 1.B Entity table

""" + table(["Entity", "Canonical spelling / id", "Services (cited)", "Value", "Verdict"], [
    ["Claire Morgan", "claire.morgan@harmonygames.co · EMPLOYEE_0009_SLACK_ID · usr_7fe31e7ec8199618 · Trello 4bc5d398e54226f344ad3abc", "Slack, Linear, Gmail (claire@ file alias, I03), GCal, Drive", "persona; writes the plan, tracker, comments, assignments, tickets, reply", "AGREE"],
    ["Leonard Hayes", "leonard.hayes@harmonygames.co · EMPLOYEE_0038_SLACK_ID · usr_63fffeb4fab5233e · Trello PERSON_6094_TRELLO_USER_ID (fullName Leonard Hayes) · root d_63fffeb4fab5233ed5bb73", "Slack, Trello, GCal, Drive, Gmail", "requester (CEO, contacts 63fffeb4fab5233ed5bb73bf 'Co-founder & CEO')", "AGREE"],
    ["Frederick Stone", "frederick.stone@harmonygames.co · EMPLOYEE_0008_SLACK_ID · usr_175c0d7bc72ed244 · Trello 4b4a68fc0fec0b254e4f9d8e · root d_175c0d7bc72ed244b944cb", "Gmail (from-name 'frederick stone'), Linear (creator of ART-790 / ART-792), Sheets, Trello", "UA / marketing owner of the live creatives sheet and the October UA plan; SC-49 / SC-54 (founder status, pay) never graded", "AGREE"],
    ["Robert", "robert@harmonygames.co · EMPLOYEE_0016_SLACK_ID · usr_Robert · root d_9f7ba94f7526d54d8482ba", "Slack, Slides", "art director; owns the seasonal deck", "AGREE"],
    ["Martin Walsh", "martin.walsh@harmonygames.co · EMPLOYEE_0033_SLACK_ID · usr_51f5f16d46e8cf55 · root d_51f5f16d46e8cf55f5ee33", "Slack, Drive, Linear (assignee of ART-790 / ART-792)", "icon, store screens and stills (Leonard's Sep 3 export ask C06DJBJL798/1756914854.743319)", "AGREE"],
    ["Marcus Bennett", "marcus.bennett@harmonygames.co · EMPLOYEE_0002_SLACK_ID · usr_c77c50cc15c5342d · root d_c77c50cc15c5342d638ebb", "Slack (IM D05V2N6PZNU), Linear, Drive", "UA video and end cards (portrait end card C06DJBJL798/1753968186.965269)", "AGREE"],
    ["Marcus (lookalikes)", "Marcus Lee marcus.lee@harmonygames.co · usr_b501f018a4c5319f; Trello c48a210d5c5a4b59231c6873 'Marcus'", "Linear, Trello", "share the first name (trap_catalog P01 / P02); Leonard's ask writes bare 'Marcus'", "DISAGREE (pre-existing, documented: the video maker is the IM partner D05V2N6PZNU and the author of every UA cut)"],
    ["Arthur Blake", "arthur.blake@harmonygames.co · EMPLOYEE_0025_SLACK_ID · root d_cc3e90160f490686039986", "Docs", "owns the Q4 release calendar (CTO, contacts cc3e90160f49068603998654)", "AGREE"],
    ["Julia Lawson", "julia.lawson@harmonygames.co", "Slack (base statics post C06DJBJL798/1749223809.524999)", "maker of the June statics; writes nothing seeded", "AGREE"],
    ["KayKit vendor", "PERSON_6311_EMAIL / PERSON_6311_NAME · contact " + CONTACT + " (job 'Founder, KayKit')", "Gmail (quote " + QUOTE["msg"] + "), Contacts", "new external token (0 base hits, scratch/mint_checks.txt)", "AGREE (new identity)"],
    ["KayKit Halloween Bits", "match3d repo `Assets/ThirdParty/3D Characters/KayKit/Packs/Bits/KayKit - Halloween Bits (For Unity)`; Robert's 'Halloween pack' C0880U9751A/1738109783.735889", "GitHub, Slack", "the pack the quote offers is already owned (seat assignment mail in Arthur's base mailbox, Jan 20 2025)", "AGREE (designed alias, T7)"],
    ["Zombie swap build", "Android #1452 (#builds C05433XK267/1753820674.990309, Jul 29 20:24Z) / iOS 1232 (Robert C0880U9751A/1753820524.488479)", "Slack #builds, #zombie-match3d, Slides", "the deck's threshold; Android and iOS Internal numbers collide (iOS Internal #1452 exists, Aug 20) so every seeded text writes the platform word", "AGREE"],
    ["App name", "Puzzles vs Zombies → Zombie Match 3D (Jul 24); seeded text writes 'ZM3D' / 'ZM' only", "Slack, Sheets, Docs", "Dec 2024 cuts predate the rename (trap_catalog K02); surfaces keyed by creative name and ticket", "AGREE"],
    ["ZM ROADMAP list", "6851a677e090018224fb8c7f 'Oct 21'", "Trello", "the card sits in a list with no rename history (SC-13 avoided: not the 'BETA: Oct 10' list)", "AGREE"],
]) + "\n")

A("## 1.C Voice and realism\n\n" + section_of(VOICE, r"^## Speaker bullets") + "\n")
KEY_TABLE = "\n".join(l for l in KEYW.splitlines() if l.startswith("|"))
A("## 1.D Keyword\n\nHit counts from `search-many` scans per service (requests and raw results in "
  "`injection_gen/research/raw/`; notes on the noisiest terms in `injection_gen/research/keywords.md`). A term with 0 "
  "hits everywhere (scan_complete true) is a NEW TERM introduced by the seeded records named.\n\n" + KEY_TABLE + "\n")

reach_rows = [
    [ASK, "Slack private channel", "Claire in members of #zombie_marketing C06DJBJL798"],
    [POINTER, "Slack public channel", "Claire in members of #zombie-art C08R8CHB0QL"],
    [EXPORT, "Slack public channel", "#zombie-art member"],
    [DM_ROOT, "Slack IM", "Claire is a party to D05V2N6PZNU"],
    [DM_REPLY, "Slack IM (thread reply)", "same IM; the root's reply_count 1 / latest_reply point at it"],
    [SHEET, "Sheets / Drive", "shared with Claire (shared_with_emails_json, reader)"],
    [DOC, "Docs / Drive", "shared with Claire (reader)"],
    [DECK, "Slides / Drive", "shared with Claire (reader)"],
    [F["root"] + " / " + F["store"] + " / " + F["ua"], "Drive folders", "shared with Claire (writer)"],
    [", ".join(I["files_store"][:3]) + " (+8 more store files)", "Drive files", "shared with Claire"],
    [", ".join(I["files_ua"]), "Drive files", "shared with Claire"],
    [PLAN["msg"], "Gmail", "Claire's own mailbox, INBOX"],
    [DRAFT["msg"], "Gmail", "Claire's own mailbox, INBOX"],
    [QUOTE["msg"], "Gmail", "Claire's own mailbox, INBOX"],
    [EVT[CLAIRE], "GCal", "Claire's own calendar copy, self:true"],
    ["C06DJBJL798/1755114007.441789 (base, 30 s cut thread)", "Slack private channel", "#zombie_marketing member"],
    ["C06DJBJL798/1756914854.743319 (base, Sep 3 export ask)", "Slack private channel", "#zombie_marketing member"],
    ["C06DJBJL798/1753968186.965269 (base, portrait end card)", "Slack private channel", "#zombie_marketing member"],
    ["C0880U9751A/1738109783.735889, C0880U9751A/1753820524.488479 (base)", "Slack private channel", "Claire in members of #zombie-match3d"],
    ["C05433XK267/1753789877.590639, C05433XK267/1753820674.990309 (base #builds)", "Slack public channel", "Claire in members of #builds"],
    ["C08R8CHB0QL/1758121809.236839 (base, Halloween icon concept)", "Slack public channel", "#zombie-art member"],
]
A("""## 1.E Persona reach

Every scoped record a correct run needs is visible to claire_morgan. `persona_view.py check-sql claire_morgan
01_Universe_Inject.sql --load-bearing Working_Files/injection_gen/load_bearing_ids.txt` → verdict PASS (pasted below).
The NO rows are the recipient copies of Frederick's two mails in Leonard's, Marcus's, Martin's and Frederick's own
mailboxes: companions, never load-bearing. Linear (ART-793 … ART-854 and their comments), Trello
(""" + CARD + """ and its actions), Contacts (""" + CONTACT + """) and GitHub (the KayKit pack path) are unscoped.

""" + table(["Record", "Service class", "Visibility path"], reach_rows) + "\n\n" + fence(OUT["reach"]) + "\n")

A("""## 1.F Collision

Identity tokens first: one new external header token, PERSON_6311_EMAIL / PERSON_6311_NAME (0 hits in all three data
folders, `Working_Files/scratch/mint_checks.txt`); no other new identity. Every minted id was looked up over its full
collection with the record's own key and a positive control that must hit (`Working_Files/scratch/inj_collisions.txt`,
this session):

""" + table(["Minted id(s)", "Lookup (key) · positive control", "Result"], [
    [f"19 Drive rows: {SHEET}, {DOC}, {DECK}, {F['root']}, {F['store']}, {F['ua']}, 11 store files ({I['files_store'][0]} …), {', '.join(I['files_ua'])}", "gdrive data.json /drive_files (id) · d_63fffeb4fab5233ed5bb73", "scan_complete true, 53,631 records: control hit 1, seeded ids 0"],
    [f"7 GCal copies ({', '.join(list(EVT.values())[:2])} …)", "gcal data.json /events (event_id) · evt_00009bfb80dabb15aa5bb5", "scan_complete true, 10,395 records: control hit 1, seeded 0"],
    [UID, "gcal /events (ical_uid) · a58a8bb029ac801cd448630ad52461e3@hg4", "control hit 172 rows, seeded 0"],
    [f"{CARD} (card), {CARD_ACT}, {CARD_CMT} (actions)", "trello /cards (id) · 68d1eb90bef538c7c5c5599d; /actions (id) · 68d1eb90bef538c7c5c559bc", "803 cards / 5,252 actions: controls hit 1 each, seeded 0; first 8 hex = 2025-09-30T22:00:00Z / 23:20:00Z"],
    [CONTACT, "contacts contacts.json /contacts (contact_id) · 63fffeb4fab5233ed5bb73bf", "170 records: control hit 1, seeded 0"],
    [DECK, "gslides /slides_presentations (presentation_id) · f_0281d5b83f931db7fff2be", "132 records: control hit 1, seeded 0"],
    ["ART-793 … ART-854 (62)", "linear /issues (id) · ART-792", "3,687 records: control hit 1, seeded 0"],
    ["cmt_art793_1 … cmt_art854_2 (124 minted, 77 used)", "linear /comments (id)", "0 base comments: 0 hits"],
    [f"Slack {ASK}, {POINTER}, {EXPORT}, {DM_ROOT}, {DM_REPLY}", "the channel's monthly shard (ts) · C06DJBJL798/1749234411.792129 (scratch/mint_checks.txt)", "control hit, seeded 0"],
    ["11 Gmail thread ids (" + ", ".join(list(PLAN["copies"].values())[:2]) + " …) and Message-IDs " + ", ".join(x["msg"].split("/", 1)[1] for x in (PLAN, DRAFT, QUOTE)), "content scan of all 81,404 thread files (Gmail ids cannot use lookup, Ask_Carriers §6a); scratch/new_ids.txt", "0 hits for all 14; thread ids decode as (first message ms << 20) | 20 random bits, like base ids"],
]) + "\n")

A("""## 2 Record ledger

One row per INSERT or UPDATE in SQL order (parsed from the SQL with `tools/base_check.parse_sql`). Carrier ● = a
load-bearing carrier class under hard gate 7 (Linear comments verified ●, Ask_Carriers §6b; Slides element text, sheet
cells, doc body, mail body, Slack text, Trello comment text, GCal time fields); ○ = supporting (Drive file names in a
folder listing, the Contacts job field).

""" + table(["#", "service", "table", "id", "container", "manifest element", "carrier", "reach path", "discovery role"], ledger) + "\n")

A(f"""## 3 Findability and discovery order

""" + table(["Record", "Agent's likely query", "Term present", "Competing base hits", "Chain position"], [
    [ASK, "the message the prompt names; #zombie_marketing history (newest top-level post, Sep 30 22:05Z)", "\"halloween for ZM\", \"live creatives sheet\", \"ART ticket\"", "none newer in the channel before the clock", "first link (A1)"],
    [SHEET, "Drive / Sheets search \"live creatives\" (the ask: \"the live creatives sheet is what's running\")", "title \"ZM3D live creatives\"", "the Domino Delights capture sheet f_b5fb884dc96261846b6c2c on \"UA\" / \"capture\"", "authority H1 (K1)"],
    [DOC, "Drive / Docs search \"release calendar\" (the ask names it by owner)", "title \"ZM3D release calendar — Q4\"", "Confluence page_release_checklist on \"release\"", "authority H2 (K2)"],
    [POINTER, "#zombie-art read / Slack search \"seasonal\" (the ask: \"Robert has direction for seasonal art\")", "\"seasonal art direction for Q4 is in my deck\"", "Robert's 2024 Domino Delights Halloween asks C04V7N09LE7/1726011239.339499 on \"halloween\"", "connecting (K3)"],
    [DECK, "Slides / Drive search \"seasonal art direction\" (the pointer quotes the title)", "title \"Seasonal art direction — Q4 2025\"", "0", "authority H3 (K4)"],
    [PLAN["msg"], "Gmail search \"October UA plan\" / from:frederick (the ask: \"Frederick is sending his october UA plan tonight\")", "subject \"October UA plan - changes\"", "the Sep 12 draft " + DRAFT["msg"] + " in a separate thread", "authority H4 (K5)"],
    [CARD_CMT, "Trello search \"Halloween\" on ZM ROADMAP (the sheet's Read me: \"see the Halloween push card on the ZM roadmap\")", "card \"Halloween push - store + ads (Claire/Martin/Marcus)\"", "79 ZM ROADMAP cards, none Halloween", "overturning (T6 / K7)"],
    ["ART-793 … ART-854", "linear_list_issues on team ART (the sheet: \"Each Unity row links its ART ticket\")", "titles 'creative (format)', descriptions \"UA creative library: …\"", "597 base ART issues, none 'UA creative library'", "per-record evidence (K11)"],
    [F["store"], "Drive search \"halloween\" / the folder Martin names (\"exported to the halloween folder\")", "folder \"ZM3D Halloween 2025\" › \"Store\"", "Martin's base AppIconHalloween.png (Slack file) on \"halloween\"", "overturning (T1 / K12)"],
    [DM_REPLY, "Slack search \"halloween\" / from:marcus; the IM D05V2N6PZNU (the root shows reply_count 1)", "\"did the cheer fastcouch one, both 9:16 and 16:9\"", "0 'halloween' hits in the IM before Sep 26", "overturning (T3 / T19 / K16)"],
    [QUOTE["msg"], "Gmail search \"Halloween\" in Claire's mailbox", "subject \"Halloween props for Zombie Match 3D\"", "base KayKit purchase/seat mails are in Robert's and Arthur's mailboxes, not Claire's", "decoy (T7)"],
    [EVT[CLAIRE], "Calendar list for Thu Oct 2 (the ask: \"before thursday's review\")", "summary \"ZM3D Halloween review\"", "Claire's recurring Thursday meetings", "destination deadline (K8)"],
]) + f"""

Dynamic-change seeds (claim met first · overturned by · why met first · why decisive):

""" + table(["Trap", "Claim met first", "Overturned by", "Why met first", "Why decisive"], [
    ["T1", f"Martin: \"halloween store screens are exported\" {EXPORT}", f"the Store folder {F['store']}: Halloween iPhone 6.5 ×5 and Google Play ×6 files, no iPad 12.9 set", "#zombie-art is Claire's home channel; the post is the newest store news", "R2 / H1 Store tab lists the iPad set; a set with no Halloween version is a Halloween version to make"],
    ["T2", f"Leonard: \"maybe we swap the icon around the 24th?\" {ASK}", f"Arthur's calendar {DOC}: merge cut Thu Oct 16 12:00 PT, \"Anything that ships in the build has to be merged by then\"", "the ask is the first read", "the icon ships in the binary (Nov 6 clean-up 'icon and screenshots back to normal'; match3d ProjectSettings)"],
    ["T3", "the sheet lists both cheer fastcouch cuts as live; their first capture note says Android #1427", f"Marcus's IM reply {DM_REPLY} + UA masters {F['ua']} ({', '.join(I['files_ua'])})", "the sheet is the cohort list", "R7: what we already have is reused (deck: \"Reuse: it already has a seasonal version\")"],
    ["T4", f"Frederick's Sep 12 draft {DRAFT['msg']}: flight Oct 20-31, art due Fri Oct 17, all four campaigns", f"Frederick's Sep 30 changes {PLAN['msg']}: Android US tablet ends Oct 12, flight Oct 18-31, due Wed Oct 15", "the draft is the fuller plan and a search for 'October UA plan' returns both", "the changes mail names the draft ('the October plan I sent on the 12th') and says 'not the 17th'"],
    ["T5", "ART-774's Mar–Apr spec list (iPhone 6.5 / 5.5, three iPad sizes, Play phone + tablet)", f"the sheet's Store tab {SHEET} and Leonard's Sep 3 ask C06DJBJL798/1756914854.743319", "a Linear search for store screenshots returns ART-774", "the live sets are the three on the Store tab"],
    ["T9", f"ART-795's catalogue note cmt_art795_1 (\"Captured from Android #456 on Apr 7\")", "cmt_art795_2 (Sep 22: \"Re-captured … from Android #1935\")", "the first comment on the ticket", "the deck: \"If a later capture has replaced it, the newest capture is the one that counts\""],
    ["T19", f"Marcus's reply {DM_REPLY} (\"did the cheer fastcouch one\")", "ART-851 cmt_art851_1 (the 4:5 cut Sep 17 from the Sep 16 re-capture) — the reply names \"both 9:16 and 16:9\" only", "the reply is the completion note for the cut family", "only the two named cuts have Halloween versions"],
]) + f"""

Hidden authorities against their decoys: H1 `{SHEET}` is found by its own title words ("live creatives"); its
same-service decoy is the 2024 Domino Delights capture sheet `f_b5fb884dc96261846b6c2c` (another game). H2 `{DOC}` is
found by "release calendar"; the Confluence `page_release_checklist` is the undated generic gate. H3 `{DECK}` is found
through Robert's pointer `{POINTER}` and by its title; Robert's 2024 Domino Delights Halloween icon asks
`C04V7N09LE7/1726011239.339499` are the scope decoy. H4 `{PLAN['msg']}` is found by "October UA plan"; the same search
returns the superseded draft `{DRAFT['msg']}` (T4's older version).
""")

A(f"""## 4 Self-validation

""" + table(["QC category", "Tool-enforced", "Manual (cited evidence)"], [
    ["Missing Universe Data", "base_check Check A PASS", f"every deciding fact is a seeded or base record visible to Claire (1.E); the master note of {BY['marcus.bennett 9:16']['ticket']} points at the base thread C06DJBJL798/1755114007.441789, which Claire can read; no tool is killed (friction not configured at this stage)"],
    ["Temporal Field", "sql_lint, base_check Check C PASS", f"dates in text agree with the fields: Frederick's changes mail (2025-09-30T23:10Z) names 'the October plan I sent on the 12th' ({DRAFT['msg']}, 2025-09-12T17:40Z); Marcus's reply (Sep 29) follows Claire's Sep 26 note; every re-export (ART-851 … ART-854) follows its parent's re-capture comment; every catalogue comment is a minute after its ticket; the calendar doc (modified 22:40Z) is after the ask (22:05Z)"],
    ["Cross-service Referential", "base_check Check A PASS; fact_check PASS", f"every sheet Unity row names an existing ticket ART-793 … ART-854; the Read me names the Trello card that exists ({CARD}); Martin's 'halloween folder' is {F['root']}; Marcus's 'UA masters in the halloween folder' is {F['ua']} in it; the deck title Robert quotes matches {DECK}"],
    ["Quantitative / Reconciliation", "Slack reply counters (D05V2N6PZNU root reply_count 1, latest_reply = the reply ts); Trello badges comments 1", "no total or count is stated in any seeded text; the store sets' file counts (iPhone ×5, Play ×6) match the live sets' sizes"],
    ["State / Lifecycle", "Linear Todo ⇔ no started/completed stamps; Canceled ⇔ canceled_at on ART-836 … ART-839; no comment after a close", "serving tickets stay open and unassigned (Frederick's catalogue); the four archived ones are Canceled on their paused date and carry no comment"],
    ["Identifier / Format", "id formats checked (1.F); Slack id = sha256(channel|ts)[:32]", "emails copied from the base; one naming scheme per service; platform word on every build number (Android #… / iOS …)"],
    ["Semantic / Category", "—", "doc / deck / sheet titles match their content; the decoys state their own scope (Domino Delights; generic checklist)"],
    ["Other", "—", "voice per 1.C; no record states a call, a total or the plan"],
]) + "\n\nStatic lint:\n\n" + fence(OUT["lint"]) + """

sql_lint warning disposition: the 14 warnings are one class — the seven copies of the review event start / end on
Thu 2025-10-02 16:00–16:30Z, after the clock; disposition: allowed, a not-yet-happened future event (the deadline the
ask names), never a completed fact.

Base check (/injection Checks A + C):

""" + fence(OUT["base"]) + """

base_check warning disposition: the INT-11 warning (no invitation mail for the review) is declared in the manifest's
`integration_exceptions` (no_notify: Leonard put the review on the calendars at 22:10Z, right after his ask; base: 105 of
941 meetings with attendees have no invitation mail).

Base claims:

""" + fence(OUT["claims"]) + """

Eval injection lint (`tools/hg.py lint`, the eval's `hg_injection_lint.py`):

""" + fence(OUT["hglint"]) + """

Hardness gate (SQL mode):

""" + fence(OUT["gate"]) + """

Solver contract (`oracle_kit.py check`) and preflight:

""" + fence(OUT["oracle"]) + f"""

Preflight report `01c_Preflight_Report.json`: {PRE.get('verdict') or 'PASS'} · blocking {json.dumps(PRE.get('blocking') or {})} ·
geometry U {PRE.get('geometry', {}).get('U') if isinstance(PRE.get('geometry'), dict) else 'see report'} · pre-registered forecast
{HEV} (UNCALIBRATED, advisory).
""")

A("""## 5 Intended disagreements

""" + table(["Disagreement", "Why realistic", "What resolves it"], [
    [f"Martin says the Halloween store screens are exported ({EXPORT}); the Store folder has no Halloween iPad set ({F['store']})", "he exported the iPhone and Play sets first; the iPad set was never exported", "the folder listing against the Store tab (" + SHEET + ")"],
    [f"Leonard suggests swapping the icon around the 24th ({ASK}); the calendar's cut is Oct 16 ({DOC})", "a CEO's casual question before reading the release dates", "the calendar: anything that ships in the build is merged by Thu Oct 16 12:00 PT"],
    [f"Frederick's Sep 12 draft ({DRAFT['msg']}) vs his Sep 30 changes ({PLAN['msg']})", "he said he would confirm before month end and did", "the later mail names the earlier one and states the two changes"],
    ["the cheer fastcouch tickets' first capture note (Android #1427, Jul 28) vs Marcus's Halloween versions", "both were re-captured on Sep 16 (cmt_art808_2, cmt_art816_2) and Marcus dressed the re-capture", f"the newest comment + {DM_REPLY}"],
    ["the boris cuts' 'live since Sep 12' vs their tickets' Jul 28 capture (cmt_art840_1, cmt_art841_1)", "the Boris opening was added on Sep 11 to footage captured the day before the swap", "the deck's threshold Android #1452 / iOS 1232"],
    ["April catalogue notes vs September re-captures (cmt_art795_2, cmt_art805_2, cmt_art797_2)", "Marcus re-recorded three cuts on current builds in September", "the deck's newest-capture rule"],
    ["the portrait end card's Android #1450 render (cmt_art831_1) vs the Jul 29 swap", "#1450 succeeded at 11:51Z (C05433XK267/1753789877.590639), #1452 at 20:24Z (C05433XK267/1753820674.990309)", "the deck names Android #1452 / iOS 1232"],
    [f"the sheet as the list of what is running vs Julia's 4:5 static ({CARD_CMT}) and the portrait end card (ART-831)", "the sheet was last edited Sep 29; the static never made it on; the end card plays after every Android US phone video", "the ask's scope (\"everything players see\", \"every ad we're running\")"],
    [f"the vendor's 'Halloween Bits bundle' quote ({QUOTE['msg']}) vs the pack the studio owns", "an outreach mail selling a pack the studio already licensed (Jan 2025)", "contact " + CONTACT + " (Founder, KayKit) + the repo path + C0880U9751A/1738109783.735889"],
    ["Marcus's 'both 9:16 and 16:9' vs the cheer fastcouch 4:5 cut ART-851", "Marcus's trial pass (asked Sep 26, done Sep 29) dressed the two cuts he names; the 4:5 export of Sep 17 is a separate placement he did not dress", "the reply's exact set + the UA masters folder (two files)"],
]) + "\n")

A("""## 6 Constraints for the prompt brief

""" + table(["Anchor", "May be named (noun phrases only)", "Record"], [["A1", "Leonard's Halloween message; Leonard's Halloween ask", ASK]]) + f"""

- Never name: where the rules live (the live creatives sheet's comment rule, the release calendar, Robert's deck, the
  changes mail, the Trello card, the DM reply, the Store / UA masters folders) or what they say; any creative, ticket,
  build number, date or call; the vendor or the KayKit pack; Julia's 4:5 static or the portrait end card.
- Deadline: before Thursday's review (Thu Oct 2 2025, 16:00 UTC = 9:00 AM PT, {EVT[CLAIRE]}).
- Deliverable kinds: a plan doc and a tracker Claire owns, shared with the team; a comment on each ad's ART ticket;
  maker assignments; new tickets for new store art; one reply in Leonard's thread.
- Relative dates: the persona's today is Wed Oct 1 2025; Leonard asked "yesterday" (Tue Sep 30).
- Rubric-only facts for the rubric stage: {', '.join(f['id'] for f in RO)} (`scenario_gen/rubric_only_facts.json`).
""")

hf = [
    [ASK, "seeded", "A1: Leonard's ask (scope, owners, follow-through, the 24th, the review)", "leonard.hayes@harmonygames.co 2025-09-30T22:05:13Z", "#zombie_marketing member", "hub / destination", "no"],
    [POINTER, "seeded", "K3: Robert names his deck", "robert@harmonygames.co 2025-09-25T16:30:22Z", "#zombie-art member", "connecting", "no"],
    [EXPORT, "seeded", "T1: 'halloween store screens are exported'", "martin.walsh@harmonygames.co 2025-09-30T15:20:41Z", "#zombie-art member", "claim met first", "no"],
    [DM_ROOT, "seeded", "Claire asks Marcus for a trial pass", "claire.morgan@harmonygames.co 2025-09-26T07:40:09Z", "Claire's IM D05V2N6PZNU", "connecting", "no"],
    [DM_REPLY, "seeded", "T3 / T19: both cheer fastcouch cuts (9:16, 16:9) done", "marcus.bennett@harmonygames.co 2025-09-29T17:20:37Z", "Claire's IM D05V2N6PZNU", "overturning evidence", "no"],
    ["C0880U9751A/1758141269.804779", "base", "Leonard: '1.3.38 is out!' (the store sets' 'Live since Sep 17')", "Leonard 2025-09-17T20:34:29Z", "#zombie-match3d member", "evidence (Store tab dates)", "no"],
    [SHEET, "seeded", "H1: Read me / Store / Unity / Archive", "frederick.stone@harmonygames.co modified 2025-09-29T18:00:00Z", "shared with Claire", "authority", "no"],
    [DOC, "seeded", "H2: merge cut Thu Oct 16 12:00 PT; iOS screenshots with the Oct 17 submission; Play any day", "arthur.blake@harmonygames.co modified 2025-09-30T22:40:00Z", "shared with Claire", "authority", "no"],
    [DECK, "seeded", "H3: Android #1452 / iOS 1232 threshold; newest capture; music-baked masters; the four calls", "robert@harmonygames.co 2025-09-25T16:10:00Z", "shared with Claire", "authority", "no"],
    [DRAFT["msg"], "seeded", "T4 older version: flight Oct 20-31, due Fri Oct 17", "frederick.stone@harmonygames.co 2025-09-12T17:40:00Z", "Claire's INBOX", "superseded version", "no"],
    [PLAN["msg"], "seeded", "H4: Android US tablet ends Oct 12; flight Oct 18-31; due Wed Oct 15", "frederick.stone@harmonygames.co 2025-09-30T23:10:00Z", "Claire's INBOX", "authority", "no"],
    [QUOTE["msg"], "seeded", "T7: 'our Halloween Bits bundle … 39 USD'", "PERSON_6311_EMAIL 2025-09-24T14:00:00Z", "Claire's INBOX", "decoy", "no"],
    [EVT[CLAIRE], "seeded", "K8: ZM3D Halloween review Thu Oct 2 16:00–16:30Z", "leonard.hayes@harmonygames.co updated 2025-09-30T22:10:00Z", "Claire's calendar", "destination deadline", "no"],
    [F["root"], "seeded", "K12: ZM3D Halloween 2025 (Store, UA masters)", "leonard.hayes@harmonygames.co 2025-09-29T09:15:00Z", "shared with Claire", "connecting", "no"],
    [F["store"], "seeded", "T1: Halloween iPhone ×5, Google Play ×6, no iPad set", "martin.walsh@harmonygames.co files 2025-09-30T15:12Z", "shared with Claire", "overturning evidence", "no"],
    [F["ua"], "seeded", "T3: cheer_fastcouch_halloween_9x16.mp4, _16x9.mp4", "marcus.bennett@harmonygames.co 2025-09-29T17:05Z", "shared with Claire", "alternate path", "no"],
    ["ART-793 … ART-854", "seeded", "K11: 58 serving + 4 archived library tickets; comments carry campaigns, source build, master", "frederick.stone (catalogue), marcus.bennett (re-captures, exports) 2025-09-08 … 2025-09-25", "Linear unscoped", "per-record evidence + write target", "no"],
    [CARD, "seeded", "K7: Halloween push card (Oct 21 list)", "PERSON_6094_TRELLO_USER_ID (Leonard) 2025-09-30T22:00:00Z", "Trello unscoped", "connecting", "no"],
    [CARD_CMT, "seeded", "T6: Julia's 4:5 static still running on iOS UK, not on the sheet", "4b4a68fc0fec0b254e4f9d8e (Frederick) 2025-09-30T23:20:00Z", "Trello unscoped", "overturning evidence", "no"],
    [CONTACT, "seeded", "T7: PERSON_6311 — Founder, KayKit", "contacts 2025-09-24T14:05:00Z", "Contacts unscoped", "alias bridge", "no"],
    ["C06DJBJL798/1755114007.441789", "base", "the 30 s cut's master has the music baked in (thread replies)", "Frederick 2025-08-13", "#zombie_marketing member", "evidence (ART-809's master note points here)", "no"],
    ["C06DJBJL798/1756914854.743319", "base", "Leonard asks Martin to export iphone / ipad / gp", "Leonard 2025-09-03T15:54:14Z", "#zombie_marketing member", "evidence (T5)", "no"],
    ["C06DJBJL798/1753968186.965269", "base", "Marcus's portrait UA end card", "Marcus 2025-07-31", "#zombie_marketing member", "evidence (T6 / T17)", "no"],
    ["C0880U9751A/1753820524.488479", "base", "Robert: iOS 1232 zombie swap with the new background", "Robert 2025-07-29T20:22Z", "#zombie-match3d member", "evidence (CH2)", "no"],
    ["C05433XK267/1753789877.590639", "base", "#builds: Match3D Android #1450 success", "Jenkins 2025-07-29T11:51Z", "#builds member", "evidence (T17)", "no"],
    ["C05433XK267/1753820674.990309", "base", "#builds: Match3D Android #1452 success", "Jenkins 2025-07-29T20:24Z", "#builds member", "evidence (T17, the threshold)", "no"],
    ["C0880U9751A/1738109783.735889", "base", "Robert: 'we have the Halloween pack'", "Robert 2025-01-28", "#zombie-match3d member", "evidence (CH5)", "no"],
    ["C08R8CHB0QL/1758121809.236839", "base", "Martin's undecided Halloween icon concept", "Martin 2025-09-17", "#zombie-art member", "decoy (T13)", "no"],
    ["ART-774", "base", "store screenshot spec (Done 2025-04-15)", "2025-03-10", "Linear unscoped", "decoy (T5)", "no"],
    ["f_b5fb884dc96261846b6c2c", "base", "Domino Delights 'Video Capture Requests for UA'", "2024", "shared with Claire", "decoy (T10)", "no"],
    ["page_release_checklist", "base", "generic pre-submission gate, no dates", "Confluence", "Confluence unscoped", "decoy (T15)", "re-verify after regeneration"],
]
A("""## 7 Facts for the human

Every seeded or relied-on record (full ids). Recipient mail copies and attendee calendar copies are listed in the
ledger only. Per-ad facts (call, owner, due, campaigns, newest source, master) are in `Working_Files/solver/truth.json`
and `scenario_gen/roster_final.json`; counts from the solver: """ + ", ".join(f"{k} {v}" for k, v in sorted(Counter(v['call'] for v in TRUTH.values() if v.get('call')).items())) + f""" over {sum(1 for v in TRUTH.values() if v.get('call'))} serving surfaces (4 archived rows out of scope).

""" + table(["locator", "base/seeded", "fact / element", "actor / UTC", "reach path", "role", "re-verify?"], hf) + "\n")

fact_rows = [[f["key"], f["value"], f["kind"], ", ".join(f.get("must_appear_in", []) + [f"home {h}" for h in f.get("home_ids", [])]) or "wherever the key is mentioned"] for f in M["facts"]]
A("""## 8 Fact sheet

""" + table(["Key", "Value", "Kind", "Must appear in / home"], fact_rows) + "\n\n" + fence(OUT["fact"]) + """

fact_check warning disposition: the bare first names "Marcus", "Martin" and "Claire" appear in Leonard's ask, the
Trello card name and the vendor's greeting; disposition: kept — base Slack writes colleagues by first name, the video
maker is Claire's IM partner (D05V2N6PZNU) and every ticket description writes the full name (identity trap P01 / P02
is documented in 1.B).
""")

A("""## 9 Integrations and companions

""" + table(["Seeded service", "Integration (integrations.json)", "Companion", "Decision"], [
    ["slack", "INT-22", "Slack e-mail notification", "none: low base rate for private channels and IMs"],
    ["slack", "INT-13", "Google Drive Slack app share DM", "none: the seeded files are shared without a share DM (Claire has no Drive app DM in base)"],
    ["slack", "INT-06", "Jenkins #builds posts", "none: no build is seeded; base jobs C05433XK267/1753820674.990309 are cited"],
    ["gmail", "INT-11", "calendar invitation mails", "none: integration_exceptions no_notify for " + UID],
    ["gcal", "INT-11", "invitation / RSVP mails", "none (same exception); seven attendee rows, self on each owner's copy"],
    ["gdrive", "INT-13", "Drive share DMs", "none: optional companion omitted"],
    ["linear", "INT-04 / INT-05", "Linear Slack notices / mail digests", "none: comments only, no state change; digests are batched"],
    ["linear", "INT-03", "linear[bot] PR comment", "none: no PR is seeded"],
    ["trello", "INT-21", "Trello → Slack", "none: the integration does not exist"],
    ["gdocs / gsheets / gslides / contacts", "—", "no integration", "none (no companion exists)"],
]) + "\n")

A("""## 10 Touched-data census and coherence hazards

### Touched-data census

- Every serving surface: the 62 rows of `Working_Files/solver/truth.json` (store sets, icon, 58 ads) with their
  tickets ART-793 … ART-854, the 4 archived tickets ART-836 … ART-839, and the base posts they were cut from
  (`scenario_gen/roster_notes.md` §3, e.g. C06DJBJL798/1753968186.965269, C06DJBJL798/1755114007.441789).
- The threads around seeded records: the Claire–Marcus IM D05V2N6PZNU (Jul 10 – Sep 26 base messages), #zombie-art
  late September (C08R8CHB0QL/1758121809.236839), #zombie_marketing Aug–Sep (the 30 s cut thread, Sep 3 export ask).
- Rules and plans: the sheet, doc and deck; Frederick's two mails; the Trello card on ZM ROADMAP 6851a6569f3bf818760632ab;
  #builds Jul 29 (C05433XK267/1753789877.590639, C05433XK267/1753820674.990309); Robert's Jul 29 swap post
  C0880U9751A/1753820524.488479; ART-774; the match3d repo path for the KayKit pack; Confluence page_release_checklist.

### Hazard audit (coherence_hazards.json, synth-cut)

""" + table(["Hazard", "Category", "Records", "Disposition"], [
    ["T02", "temporal", "Claire's thread files", "each seeded Gmail thread holds one message; no seeded record joins a base thread"],
    ["T04", "temporal", "Linear issues completed before PRs", "none in scope: no seeded ticket is completed; ART-836 … ART-839 are Canceled on their paused date"],
    ["T06", "temporal", f"Trello card {CARD}", "card dateLastActivity = the comment time 2025-09-30T23:20:00Z; board bumped to the same time"],
    ["S03", "semantic", "Linear label vocabulary", "no label is set or read (empty label list)"],
    ["S04", "semantic", "GitHub display names", "no GitHub row is seeded"],
    ["R04", "cross-service referential", "Slack links to Google files", "excluded: no seeded Slack text links a Drive file; files are named by title (hazard_acknowledgements R04)"],
    ["R07", "cross-service referential", "GitHub ↔ #zombie-prs mirrors", "excluded: no PR is seeded (hazard_acknowledgements R07)"],
    ["R08", "cross-service referential", "invitations vs calendar rows", f"excluded: the review {UID} has no invitation mail by design (integration_exceptions; hazard_acknowledgements R08)"],
    ["Q01 / Q04", "quantitative", "Slack reply counters", f"the seeded IM root {DM_ROOT} carries reply_count 1, reply_users_count 1, latest_reply = the reply ts"],
    ["Q10", "quantitative", "copies of one message", f"Frederick's two mails: five byte-identical copies each ({PLAN['thread']} etc.)"],
    ["Q11", "quantitative", "calendar copies of one event", f"seven copies of {UID} differ only in calendar_id, event_id and self"],
    ["L05", "state/lifecycle", "ART-774 Done with a dated spec", "dated_claim: read for its Mar–Apr spec list only (hazard_acknowledgements L05)"],
    ["L08", "state/lifecycle", "open issues assigned to quiet people", "none in scope: every seeded ticket is unassigned; the assignees the run sets (Marcus, Martin) are active_sep_2025_quiet_in_oct"],
    ["L11 / L12", "state/lifecycle", "Trello list state", "the card sits in the open list 'Oct 21' with no checklist"],
    ["I03", "identifier/format", "mailbox file aliases", "ids use the full address (claire.morgan@…), files follow the alias"],
    ["I14 / I15", "identifier/format", "Drive owner tokens; name vs native title", "real owner emails; Drive names equal the native titles (no .xlsx / .docx suffix)"],
    ["I16", "identifier/format", "Trello ids vs dates", "every seeded Trello id carries its record second"],
]) + """

Known-data-issue cards touched (`references/known_data_issues/synthcut.md`): SC-11 / SC-12 / SC-23 (no spend figure is
seeded or graded; `snowflake.ANALYTICS` read for channels only), SC-13 (the card is in 'Oct 21', not the 'BETA: Oct 10'
list), SC-16 (ART-790 / ART-792 stay off the path), SC-36 (review attendees named explicitly, Victor Barnes not
invited), SC-49 / SC-54 (Frederick's founder status and pay never graded; he is active in Slack through 2025-09-30),
SC-58 (no monster roster name graded), SC-70 (times come from the doc and the mails, not Slack timezones).
""")

A(f"""## 11 Platform follow-ups

- Confirm in the Opus pre-check that `linear_list_comments` returns the seeded comments on ART-793 … ART-854 (verified
  carrier, Ask_Carriers §6b), that `gdrive_list_folder` on {F['store']} returns the file names, that
  `gslides_get_presentation` returns the element text of {DECK}, that `gsheets_values_batch_get` returns the four tabs of
  {SHEET}, and that `slack_read_thread` on {DM_ROOT} returns Marcus's reply.
- Drive media files carry metadata only (eval lint INFO): the task needs only their names.
- The conditional budget rows (DM read, draft read, contacts, icon settings, threshold post, read-backs) count 0 until a
  run shows them; the unconditional floor is 192 (call_budget_floor 181).
- Write targets: Claire creates and owns the plan doc and the tracker at run time; ART tickets are unscoped; confirm each
  write returns ok in the pre-check.
- Confluence `page_release_checklist` (decoy) to be re-verified after any regeneration.
""")

sr = (HERE / "self_review.md").read_text() if (HERE / "self_review.md").exists() else "## 12 Self-review\n"
A(sr)
(WF / "01_Grounding_Dossier.md").write_text("\n".join(doc).rstrip() + "\n")
print("wrote", WF / "01_Grounding_Dossier.md", len("\n".join(doc).splitlines()), "lines · ledger", len(ledger), "rows")

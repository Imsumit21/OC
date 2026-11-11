#!/usr/bin/env python3
"""Render Working_Files/01_Grounding_Dossier.md for the ZM3D Halloween art plan injection (rev3).

Tables that name records are generated from the SQL (tools/base_check.parse_sql), roster_final.json, ids.json and the
final manifest; tool outputs are re-run here and pasted verbatim. Hand-written analysis lives in this file and in
injection_gen/research/*.md: the Self-review is in this file, so edit it here, not in the .md. The same inputs give the
same bytes. The one thing kept from the file being replaced is the `stage_gate.py --paste` block, which only stage_gate
rewrites. Never executes SQL; writes only the dossier.

    python3 -B Task_Authoring/task_inputsN2/Working_Files/injection_gen/build_dossier.py
"""
from __future__ import annotations

import hashlib
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
TS = json.loads((SG / "ids.json").read_text())["timestamps"]
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
STORE_REPLY = I["slack_leonard_store_reply"]["locator"]
FRED_REVIEW, RECAP_NOTE = I["slack_fred_review_reply"]["locator"], I["slack_marcus_recapture"]["locator"]
TEST_POST, TEST_REVIEW = I["slack_marcus_test"]["locator"], I["slack_robert_test_reply"]["locator"]
TEST_ACK = I["slack_marcus_test_reply"]["locator"]
LEAVE_POST, LEAVE_REPLY = I["slack_martin_leave"]["locator"], I["slack_leonard_leave_reply"]["locator"]
INSTALLS_ROOT = "C0880U9751A/1759211437.306779"        # base: Robert, Sep 30, Unity fake installs
INSTALLS_ROOT_ID = hashlib.sha256(b"C0880U9751A|1759211437.306779").hexdigest()[:32]
PACKS_OLD = "C08R8CHB0QL/1754310794.907609"            # base: Marcus posts EndCard001.mp4, the packs "have the old zombies on it"
PACKS_NEW = "C08R8CHB0QL/1754316299.381419"            # base: Martin's new packs, after it
REFRESH_CARD = "68768a1501ae552dbee94b8a"              # base: Marketing Video Refresh card, ZM ROADMAP
ICON_REPLY, ICON_POST = I["slack_robert_icon_reply"]["locator"], "C08R8CHB0QL/1758121809.236839"
ICON_POST_ID = "9025d428af1f551a20e303c3acbc545b"
SHEET, DOC, DECK = I["sheet_live"], I["doc_release"], I["deck_seasonal"]["presentation"]
PLAN, DRAFT, QUOTE = I["gmail_fred_plan"], I["gmail_fred_draft"], I["gmail_vendor_quote"]
RESTART = I["gmail_fred_restart"]
EVT, UID = I["gcal_review"]["evt_by_calendar"], I["gcal_review"]["ical_uid"]
F = I["folder_halloween"]
CARD, CARD_ACT, CARD_CMT, CONTACT = I["trello_card"], I["trello_card_create_action"], I["trello_comment"], I["contact_vendor"]
PACKS_CMT = I["trello_logo_comment"]
ADS = [r for r in R if r.get("ticket")]
FLOOR = sum(b["calls"] for b in M["call_budget"] if not b.get("conditional_on"))
STMTS = parse_sql(SQL)
SLACK_ID = {I[k]["row_id"]: I[k]["locator"] for k in ("slack_ask", "slack_robert_pointer", "slack_martin_export", "slack_leonard_store_reply",
                                                     "slack_dm_root", "slack_dm_marcus_reply", "slack_robert_icon_reply",
                                                     "slack_fred_review_reply", "slack_marcus_recapture", "slack_marcus_test",
                                                     "slack_robert_test_reply", "slack_marcus_test_reply", "slack_martin_leave",
                                                     "slack_leonard_leave_reply")}
SLACK_ID[ICON_POST_ID] = ICON_POST
SLACK_ID[INSTALLS_ROOT_ID] = INSTALLS_ROOT
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
FC = json.loads((WF / "01c_Forecast.json").read_text())
HEV = (FC.get("preregistration") or {}).get("id")
FC_LINE = (f"Pre-registered forecast {HEV} (UNCALIBRATED, advisory)." if FC.get("sql_sha256") == hashlib.sha256(SQL.encode()).hexdigest() else
           f"`01c_Forecast.json` ({HEV}) was made on an earlier revision and says nothing about this SQL; no rev3 forecast is registered yet.")
_lintw = re.search(r"warnings:\s*(\d+)", OUT["lint"])
LINT_WARNINGS = _lintw.group(1) if _lintw else "?"
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
                I["slack_leonard_store_reply"]["locator"]: ("K18 (exported art needs no ticket)", "●", "#zombie-art member (thread reply)", "overturning evidence"),
                DM_ROOT: ("K16 / T3 (thread parent)", "●", "Claire's IM with Marcus", "connecting"),
                DM_REPLY: ("K16 / T3 T19 / CH4", "●", "Claire's IM with Marcus (thread reply)", "claim met first"),
                ICON_REPLY: ("T13 (Robert: concept not for the app icon)", "●", "#zombie-art member (thread reply)", "overturning evidence"),
                ICON_POST: ("T13 companion (base parent's reply counters)", "-", "#zombie-art member", "companion"),
                FRED_REVIEW: ("K19 / T20 / CH8 (Android US phone by Fri Oct 10)", "●", "#zombie-match3d member (thread reply)", "overturning evidence"),
                INSTALLS_ROOT: ("K19 companion (base root's reply counters)", "-", "#zombie-match3d member", "companion"),
                RECAP_NOTE: ("K20 / T9 / CH9 (three re-captures)", "●", "#zm-animations member", "overturning evidence"),
                TEST_POST: ("K21 / T3 (thread parent)", "●", "#zombie-art member", "connecting"),
                TEST_REVIEW: ("K21 / T3 / CH4 (Robert turns the test down)", "●", "#zombie-art member (thread reply)", "overturning evidence"),
                TEST_ACK: ("K21 / T3 (Marcus will redo both)", "●", "#zombie-art member (thread reply)", "evidence"),
                LEAVE_POST: ("K22 / T21 / CH10 (Julia takes the ad statics)", "●", "#company-internal member", "overturning evidence"),
                LEAVE_REPLY: ("K22 / T21 / CH10 (Leonard agrees)", "●", "#company-internal member (thread reply)", "overturning evidence")}[loc]
    if table == "linear.linear_issues":
        a = next((x for x in ARCH if x["ticket"] == rid), None)
        if a:
            return ("T14 (archived library ticket)", "●", "Linear unscoped", "decoy")
        if rid == "ART-792":
            return ("SC-22 repair (base screenshot epic's status counter)", "-", "Linear unscoped", "coherence repair")
        r = next(x for x in ADS if x["ticket"] == rid)
        el = "cohort K11" + (" / T6 CH7 (off the sheet)" if not r["on_sheet"] else "")
        return (el, "●", "Linear unscoped", "evidence + write target")
    if table == "linear.linear_comments":
        r = next(x for x in ADS if x["ticket"] == row["issue_id"])
        tag = {"couch alpha 50": "T9", "barrel marketing2 4:5": "T9", "balloons alpha 50 (1)": "T9",
               "boris fastcouch 9:16": "T8 CH2", "boris alin2 9:16": "T8", "marcus.bennett 9:16": "T8",
               "marcus portrait UA end card": "T17", "cheer fastcouch 4:5": "T19", "cheer fastcouch 9:16": "T3",
               "cheer fastcouch 16:9": "T3", "couch alpha 50 16:9": "T18", "balloons alpha 50 (1) 16:9": "T18",
               "squirrelfail landscape": "T22 CH11", "mrfluffernot landscape": "T22", "end card 001": "T23 CH12",
               "end card 16:9 from 001": "T23", "end card 1:1 from 001": "T23", "end card 4:5 from 001": "T23"}.get(r["key"], "cohort evidence")
        return (f"K11 per-record ({tag})", "●", "Linear unscoped", "per-record evidence")
    if table == "gdrive.drive_files":
        if rid == F["root"]:
            return ("K12 (root)", "○ listing", "shared with Claire (writer)", "connecting")
        if rid == F["store"]:
            return ("K12 / T1 / CH1", "○ listing", "shared with Claire", "overturning evidence")
        if rid == F["ua"]:
            return ("K12 / T3 / CH4", "○ listing", "shared with Claire", "claim met first")
        if rid in I["files_store"]:
            return ("T1 (Halloween iPhone / Play export)", "○ name", "shared with Claire", "evidence")
        if rid in I["files_ua"]:
            return ("T3 (Marcus's two test cuts)", "○ name", "shared with Claire", "claim met first")
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
            return ("T7 (vendor quote, plain distractor)", "●", "Claire's mailbox INBOX", "decoy")
        draft = rid in (DRAFT["copies"].values()) or DRAFT["msg"].split("/", 1)[1] in rid
        restart = rid in (RESTART["copies"].values()) or RESTART["msg"].split("/", 1)[1] in rid
        own = (row.get("user_email") or "") == CLAIRE
        el = ("K6 / T4 (Sep 12 draft)" if draft else "K23 / T22 / CH11 (Sep 29 restart)" if restart
              else "H4 / K5 / T4 T18 (Sep 30 changes)")
        return (el + ("" if own else " · recipient copy"), "●", "Claire's mailbox INBOX" if own else "other mailbox (not read)",
                ("superseded version" if draft else "overturning evidence" if restart else "authority") if own else "companion copy")
    if table == "gcal.gcal_events":
        own = row.get("calendar_id") == CLAIRE
        return ("K8 (review deadline)" + ("" if own else " · attendee copy"), "● time fields", "Claire's calendar" if own
                else "attendee calendar", "destination deadline" if own else "companion copy")
    if table == "trello.trello_cards":
        if rid == REFRESH_CARD:
            return ("K24 companion (base card's activity and comment badge)", "-", "Trello unscoped", "companion")
        return ("K7 (Halloween push card)", "●", "Trello unscoped", "connecting")
    if table == "trello.trello_actions":
        if rid == PACKS_CMT:
            return ("K24 / T23 / CH12 (the old zombies on the packs)", "●", "Trello unscoped", "overturning evidence")
        return ("K7 / T6 / CH7 (Julia's 4:5 static)" if rid == CARD_CMT else "K7 (card creation)", "●",
                "Trello unscoped", "overturning evidence" if rid == CARD_CMT else "companion")
    if table == "trello.trello_boards":
        return ("K7 companion (board activity)", "-", "Trello unscoped", "companion")
    if table == "contacts.contacts":
        return ("T7 (vendor identity)", "○ job", "Contacts unscoped", "context")
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
DELTA = "; ".join(f"{d['id']}: {d['change']}" for d in M["design_delta"])
A(f"""# Grounding Dossier — claire-zm3d-halloween-art-plan · rev3 · contains no prompt, OE or criterion text

{CTX['universe']['clock_line']}. Seed bound {CTX['freeze_utc']}: every seeded created / sent / updated / ts value is at
or before it (latest seeded event: Frederick's thread reply {FRED_REVIEW} at {I['slack_fred_review_reply']['at']}). Only plan fields
are later: the review event's start and end (2025-10-02T16:00Z–16:30Z, {EVT[CLAIRE]}) and the dates the calendar doc
and the mails name.

Files: `01_Universe_Inject.sql` (generated by `Working_Files/injection_gen/gen_sql.py` from `scenario_gen/roster_final.json`,
`scenario_gen/planned_texts.json` and `scenario_gen/ids.json`), final manifest `Working_Files/01_Hardness_Manifest.json`
(`injection_gen/build_final_manifest.py`), solver `Working_Files/solver/solver.py` + `truth.json`, dispositions
`Working_Files/01c_Dispositions.json` (`injection_gen/write_dispositions.py`), preflight `Working_Files/01c_Preflight_Report.json`,
stored revision `Working_Files/run_forensics/rev3/01_Universe_Inject.sql`. Persona: Claire Morgan
(claire.morgan@harmonygames.co), Art Lead · Design · Long Horizon · medium · {CTX['universe']['label']}.

Design delta at this stage: {len(M['design_delta'])} entries in `design_delta`, all taken through `/create-scenario --revise`
before this SQL was written (`01_Scenario_Design.md` section 14): {DELTA}.
""")

A("""## 1.A Structural

Columns follow `references/universe_schema_live.json`; every NOT NULL column is supplied; the generated
`slack_messages.text_fts` / `gmail_messages.body_text_fts` columns are never written; `"references"`, `"index"`,
`"desc"` and every camelCase Trello column are quoted. Shapes were copied from real sibling records (the accepted
sibling SQL `Task_Authoring/task_inputsH/01_Universe_Inject.sql`, which passed `/injection` on the same universe).

""" + table(["Table", "Base location / count", "Timestamp format used", "Sibling record copied"], [
    ["slack.slack_messages", "slack messages/C06DJBJL798 (#zombie_marketing, private), messages/C08R8CHB0QL (#zombie-art, public), messages/C0880U9751A (#zombie-match3d, private), messages/C09ATAJ220H (#zm-animations, private), messages/C05KNDCHAAG (#company-internal, private), messages/D05V2N6PZNU (Claire–Marcus IM)", "ts `1759269913.882683`; created_at with the same micros", "C06DJBJL798/1756914854.743319 (Leonard's export ask, top-level); D05V2N6PZNU/1758270333.226649 (IM); C05KNDCHAAG/1756717965.570179 (leave post)"],
    ["linear.linear_issues / linear_comments", "linear data.json /issues (ART max ART-792, 597 ART issues); /comments: 0 base rows", "`2025-09-08T16:00:00Z` varchar ISO-Z", "ART-790 (Todo) / ART-792 (Team Epic): creator usr_175c0d7bc72ed244 Frederick, assignee Martin, team_ART, no labels"],
    ["gmail.gmail_threads / gmail_messages", "gmail threads/claire@harmonygames.co_*.json (846), frederick@ / leonard@ / marcus.bennett@ / martin.walsh@ files", "`2025-09-30T23:10:00Z`, internal_date ms, RFC 2822 Date header -0700", "frederick.stone@harmonygames.co/<CANf1NxdX_-=ufVrJRkObveGnt5gFc9BwveE1Phwxpp_8zfTrjA@mail.gmail.com> (from-name 'frederick stone')"],
    ["gcal.gcal_events", "gcal data.json /events (10,395 rows)", "start/end ts + start_json dateTime", "evt_bf2235816b35c5cc9577c7 shape (task_inputsH, one row per attendee calendar, self on the owner's copy)"],
    ["gdrive.drive_files", "gdrive data.json /drive_files (53,631)", "`2025-09-30T15:12:04Z`", "roots d_63fffeb4fab5233ed5bb73 (Leonard), d_175c0d7bc72ed244b944cb (Frederick), d_cc3e90160f490686039986 (Arthur), d_9f7ba94f7526d54d8482ba (Robert)"],
    ["gdocs.docs_documents", "gdocs data.json (595 documents)", "as Drive", "f_1265318f45054aaef57a4a shape (TITLE style run, 10-hex revision_id)"],
    ["gsheets.sheets_spreadsheets / sheets_sheets", "gsheets data.json", "as Drive", "f_3f40599bbc9095352d47ab shape (grid rows of strings, row_count 1000)"],
    ["gslides.slides_presentations / slides_pages / slides_page_elements", "gslides data.json (132 decks, BLANK layouts)", "as Drive", "f_b0809b6ca90ef8d44f391d shape (slide_<12hex>, el_<12hex>, 9144000 emu wide)"],
    ["trello.trello_cards (insert, and update on base card 68768a1501ae552dbee94b8a) / trello_actions / trello_boards (update)", "trello data.json (ZM ROADMAP 6851a6569f3bf818760632ab: 79 cards, max idShort 79, dateLastActivity 2025-09-30T17:09:07Z; list 6851a677e090018224fb8c7f 'Oct 21')", "`2025-09-30T22:00:00Z`; id = hex(unix seconds) + 16 hex", "68d1eb90bef538c7c5c559bc (createCard by PERSON_6094_TRELLO_USER_ID); 68655f93de2e202c2ad77a76 (commentCard data_json shape)"],
    ["contacts.contacts", "contacts contacts.json (170 rows)", "created_at/updated_at ISO-Z", "78f786dcee835fdfb72aba2a (external: first_name PERSON_n, last_name '', email PERSON_n_EMAIL, gender/status Unknown)"],
]) + "\n")

A("""## 1.B Entity table

""" + table(["Entity", "Canonical spelling / id", "Services (cited)", "Value", "Verdict"], [
    ["Claire Morgan", "claire.morgan@harmonygames.co · EMPLOYEE_0009_SLACK_ID · usr_7fe31e7ec8199618 · Trello 4bc5d398e54226f344ad3abc", "Slack, Linear, Gmail (claire@ file alias, I03), GCal, Drive", "persona; writes the plan, tracker, comments, assignments, tickets, reply", "AGREE"],
    ["Leonard Hayes", "leonard.hayes@harmonygames.co · EMPLOYEE_0038_SLACK_ID · usr_63fffeb4fab5233e · Trello PERSON_6094_TRELLO_USER_ID (fullName Leonard Hayes) · root d_63fffeb4fab5233ed5bb73", "Slack, Trello, GCal, Drive, Gmail", "requester (CEO, contacts 63fffeb4fab5233ed5bb73bf 'Co-founder & CEO')", "AGREE"],
    ["Frederick Stone", "frederick.stone@harmonygames.co · EMPLOYEE_0008_SLACK_ID · usr_175c0d7bc72ed244 · Trello 4b4a68fc0fec0b254e4f9d8e · root d_175c0d7bc72ed244b944cb", "Gmail (from-name 'frederick stone'), Linear (creator of ART-790 / ART-792), Sheets, Trello", "UA / marketing owner of the live creatives sheet and the October UA plan; SC-49 / SC-54 (founder status, pay) never graded", "AGREE"],
    ["Robert", "robert@harmonygames.co · EMPLOYEE_0016_SLACK_ID · usr_Robert · root d_9f7ba94f7526d54d8482ba", "Slack, Slides", "art director; owns the seasonal deck", "AGREE"],
    ["Martin Walsh", "martin.walsh@harmonygames.co · EMPLOYEE_0033_SLACK_ID · usr_51f5f16d46e8cf55 · root d_51f5f16d46e8cf55f5ee33", "Slack, Drive, Linear (assignee of ART-790 / ART-792)", f"icon and store art (Leonard's Sep 3 export ask C06DJBJL798/1756914854.743319); out Oct 6-15, ad statics to Julia ({LEAVE_POST})", "AGREE"],
    ["Marcus Bennett", "marcus.bennett@harmonygames.co · EMPLOYEE_0002_SLACK_ID · usr_c77c50cc15c5342d · root d_c77c50cc15c5342d638ebb", "Slack (IM D05V2N6PZNU), Linear, Drive", "UA video and end cards (portrait end card C06DJBJL798/1753968186.965269)", "AGREE"],
    ["Marcus (lookalikes)", "Marcus Lee marcus.lee@harmonygames.co · usr_b501f018a4c5319f; Trello c48a210d5c5a4b59231c6873 'Marcus'", "Linear, Trello", "share the first name (trap_catalog P01 / P02); Leonard's ask writes bare 'Marcus'", "DISAGREE (pre-existing, documented: the video maker is the IM partner D05V2N6PZNU and the author of every UA cut)"],
    ["Arthur Blake", "arthur.blake@harmonygames.co · EMPLOYEE_0025_SLACK_ID · root d_cc3e90160f490686039986", "Docs", "owns the Q4 release calendar (CTO, contacts cc3e90160f49068603998654)", "AGREE"],
    ["Julia Lawson", "julia.lawson@harmonygames.co · EMPLOYEE_0005_SLACK_ID · usr_8140f09bf9f1b94c", "Slack (base statics post C06DJBJL798/1749223809.524999; named in " + LEAVE_POST + "), Linear (assignee set at run time)", "maker of the June statics; takes the six working ad statics; writes nothing seeded", "AGREE"],
    ["Vendor (quote sender)", "PERSON_6311_EMAIL / PERSON_6311_NAME · contact " + CONTACT + " (job 'Founder, KayKit')", "Gmail (quote " + QUOTE["msg"] + "), Contacts", "new external token (0 base hits, scratch/mint_checks.txt); T7 is a plain distractor, no rule rests on it", "AGREE (new identity)"],
    ["Zombie swap build", "Android #1452 (#builds C05433XK267/1753820674.990309, Jul 29 20:24Z) / iOS 1232 (Robert C0880U9751A/1753820524.488479)", "Slack #builds, #zombie-match3d, Slides", "the deck's threshold; Android and iOS Internal numbers collide (iOS Internal #1452 exists, Aug 20) so every seeded text writes the platform word", "AGREE"],
    ["App name", "Puzzles vs Zombies → Zombie Match 3D (Jul 24); seeded text writes 'ZM3D' / 'ZM' only", "Slack, Sheets, Docs", "Dec 2024 cuts predate the rename (trap_catalog K02); surfaces keyed by creative name and ticket", "AGREE"],
    ["ZM ROADMAP list", "6851a677e090018224fb8c7f 'Oct 21'", "Trello", "the card sits in a list with no rename history (SC-13 avoided: not the 'BETA: Oct 10' list)", "AGREE"],
]) + "\n")

# research/voice.md predates rev3: its one line on Frederick's Slack silence gives way to the rev3 rows, measured the same way
VOICE_OLD_ROW = "| — | Frederick | no Slack line seeded; Gmail 2025-09-12 17:40 / 2025-09-30 23:10, Trello 23:20 | 15:00–01:00 | inside |\n"
VOICE_REV3 = "".join(f"| {n} | {who} | {where} | {at} | {win} | inside |\n" for n, who, where, at, win in [
    ("6", "Marcus", "#zm-animations C09ATAJ220H", "2025-09-25 18:12", "10:00–20:00"),
    ("7", "Marcus", "#zombie-art C08R8CHB0QL", "2025-09-29 17:31", "10:00–20:00"),
    ("8", "Martin", "#company-internal C05KNDCHAAG", "2025-09-30 14:41", "08:00–16:00"),
    ("9", "Leonard", "#zombie-art C08R8CHB0QL (thread)", "2025-09-30 15:47", "15:00–02:00"),
    ("10", "Robert", "#zombie-art C08R8CHB0QL (thread)", "2025-09-30 16:05", "14:00–03:00"),
    ("11", "Marcus", "#zombie-art C08R8CHB0QL (thread)", "2025-09-30 16:21", "10:00–20:00"),
    ("12", "Leonard", "#company-internal C05KNDCHAAG (thread)", "2025-09-30 23:31", "15:00–02:00"),
    ("13", "Frederick", "#zombie-match3d C0880U9751A (thread)", "2025-09-30 23:42", "15:00–01:00"),
    ("—", "Frederick", "Gmail 2025-09-12 17:40 / 2025-09-29 23:48 / 2025-09-30 23:10, Trello 2025-09-26 17:40 and 2025-09-30 23:20", "as listed", "15:00–01:00")])
assert VOICE_OLD_ROW in VOICE
VOICE_REV3_NOTE = """Rev3 voice sources: Martin's vacation post follows his own base post C05KNDCHAAG/1756717965.570179 ("Hello Team! Reminding
that next week I'll be on vacation"); the named cover follows C05KNDCHAAG/1719394673.875309; Robert's review follows his
direct art notes (C08R8CHB0QL/1758211038.665909, "a bit too thick and distracting"); Frederick's reply answers the question
Robert put to him in C0880U9751A/1759211437.306779. Seeded at rev3 beyond the lists above: Marcus's test thread and
#zm-animations note, Robert's review, Martin's vacation post, Leonard's two thread replies, and Frederick's thread reply,
restart mail and packs comment."""
A("## 1.C Voice and realism\n\n" + section_of(VOICE.replace(VOICE_OLD_ROW, VOICE_REV3), r"^## Speaker bullets") + "\n\n" + VOICE_REV3_NOTE + "\n")
# research/keywords.md predates rev3: three rows change their seeded side, and the rev3 terms were scanned for this revision
KEY_FIX = {"| cheer fastcouch |": f"| cheer fastcouch | NEW TERM — 0 everywhere | DM reply; `f_dc5cf9e4250d433c1511ec`, `f_bcd34f98925e3f20d846ce`; Marcus's test post `{TEST_POST}` |",
           "| re-capture |": "| re-capture | slack 1 + github 1, same match3d#402 CodeRabbit comment (`review_comments/1074`, \"re-captures baselines\" = framerate, not video) · first `messages/C093LEZGF6J/2025-08.json#/453/attachments/0` | `ART-816`, `ART-851` comment bodies |",
           "| re-captured |": "| re-captured | NEW TERM — 0 everywhere | `ART-808` comment |"}
KEY_REV3 = [
    f"| manual review | NEW TERM — 0 in slack, gmail (Claire), gdocs, gsheets, gslides, gdrive, linear, trello, confluence | Frederick's reply `{FRED_REVIEW}` |",
    f"| old ua cuts | NEW TERM — 0 in the same nine | Marcus's note `{RECAP_NOTE}` |",
    f"| ad statics | slack 1, a substring of \"upload statics\" (`messages/C07C2866011/2024-10.json#/2874`, a channel Claire is not in) | `{LEAVE_POST}`, `{LEAVE_REPLY}` |",
    f"| on vacation | slack 19 in the 2025 shards (first `messages/C05KNDCHAAG/2025-08.json#/46`) · gdocs 2 · gsheets 1 | `{LEAVE_POST}` |",
    f"| retention restart | NEW TERM — 0 in the same nine | subject of `{RESTART['msg']}` |",
    f"| end card 001 | NEW TERM — 0 in the same nine (base writes `EndCard001.mp4`, `{PACKS_OLD}`) | `{PACKS_CMT}` |",
    f"| old zombies | slack 15 (first `messages/C07C2866011/2025-08.json#/100`; `{PACKS_OLD}` among them) · 0 in the other eight | `{PACKS_CMT}` |",
    f"| Marketing Video Refresh | trello 7 (`cards/750`, its actions) · 0 in the other eight | the card `{REFRESH_CARD}` that holds `{PACKS_CMT}` |",
    f"| July capture | NEW TERM — 0 in the same nine | Robert's review `{TEST_REVIEW}` |",
    f"| iOS UK tablet | NEW TERM — 0 in the same nine | `{RESTART['msg']}`; `ART-811` comments |",
    f"| fake installs | slack 1, the root `{INSTALLS_ROOT}` | the thread Frederick replies in, `{FRED_REVIEW}` |",
]
KEY_TABLE = "\n".join([next((v for k, v in KEY_FIX.items() if l.startswith(k)), l) for l in KEYW.splitlines() if l.startswith("|")] + KEY_REV3)
A("## 1.D Keyword\n\nHit counts from `search-many` scans per service (requests and raw results in "
  "`injection_gen/research/raw/`; notes on the noisiest terms in `injection_gen/research/keywords.md`; the rev3 terms at the "
  "end were scanned for this revision over the nine services they name, GitHub not searched). A term with 0 "
  "hits everywhere (scan_complete true) is a NEW TERM introduced by the seeded records named.\n\n" + KEY_TABLE + "\n")

reach_rows = [
    [ASK, "Slack private channel", "Claire in members of #zombie_marketing C06DJBJL798"],
    [POINTER, "Slack public channel", "Claire in members of #zombie-art C08R8CHB0QL"],
    [EXPORT, "Slack public channel", "#zombie-art member"],
    [DM_ROOT, "Slack IM", "Claire is a party to D05V2N6PZNU"],
    [DM_REPLY, "Slack IM (thread reply)", "same IM; the root's reply_count 1 / latest_reply point at it"],
    [ICON_REPLY, "Slack public channel (thread reply)", "#zombie-art member; the base parent C08R8CHB0QL/1758121809.236839 carries reply_count 1 after the UPDATE"],
    [STORE_REPLY, "Slack public channel (thread reply)", "#zombie-art member; the seeded root " + EXPORT + " carries reply_count 1"],
    [TEST_POST, "Slack public channel", "#zombie-art member; reply_count 2"],
    [TEST_REVIEW + ", " + TEST_ACK, "Slack public channel (thread replies)", "#zombie-art member; under " + TEST_POST],
    [FRED_REVIEW, "Slack private channel (thread reply)", "Claire in members of #zombie-match3d C0880U9751A; the base root " + INSTALLS_ROOT + " carries reply_count 5 after the UPDATE"],
    [RECAP_NOTE, "Slack private channel", "Claire in members of #zm-animations C09ATAJ220H"],
    [LEAVE_POST, "Slack private channel", "Claire in members of #company-internal C05KNDCHAAG; reply_count 1"],
    [LEAVE_REPLY, "Slack private channel (thread reply)", "#company-internal member; under " + LEAVE_POST],
    [SHEET, "Sheets / Drive", "shared with Claire (shared_with_emails_json, reader)"],
    [DOC, "Docs / Drive", "shared with Claire (reader)"],
    [DECK, "Slides / Drive", "shared with Claire (reader)"],
    [F["root"] + " / " + F["store"] + " / " + F["ua"], "Drive folders", "shared with Claire (writer)"],
    [", ".join(I["files_store"][:3]) + " (+8 more store files)", "Drive files", "shared with Claire"],
    [", ".join(I["files_ua"]), "Drive files", "shared with Claire"],
    [PLAN["msg"], "Gmail", "Claire's own mailbox, INBOX"],
    [DRAFT["msg"], "Gmail", "Claire's own mailbox, INBOX"],
    [RESTART["msg"], "Gmail", "Claire's own mailbox, INBOX"],
    [QUOTE["msg"], "Gmail", "Claire's own mailbox, INBOX"],
    [EVT[CLAIRE], "GCal", "Claire's own calendar copy, self:true"],
    ["C06DJBJL798/1755114007.441789 (base, 30 s cut thread)", "Slack private channel", "#zombie_marketing member"],
    ["C06DJBJL798/1756914854.743319 (base, Sep 3 export ask)", "Slack private channel", "#zombie_marketing member"],
    ["C06DJBJL798/1753968186.965269 (base, portrait end card)", "Slack private channel", "#zombie_marketing member"],
    ["C0880U9751A/1753820524.488479 (base)", "Slack private channel", "Claire in members of #zombie-match3d"],
    [PACKS_OLD + ", " + PACKS_NEW + " (base, EndCard001 and the new packs)", "Slack public channel", "#zombie-art member"],
    ["C05433XK267/1753789877.590639, C05433XK267/1753820674.990309 (base #builds)", "Slack public channel", "Claire in members of #builds"],
    ["C08R8CHB0QL/1758121809.236839 (base, Halloween icon concept)", "Slack public channel", "#zombie-art member"],
]
A("""## 1.E Persona reach

Every scoped record a correct run needs is visible to claire_morgan. `persona_view.py check-sql claire_morgan
01_Universe_Inject.sql --load-bearing Working_Files/injection_gen/load_bearing_ids.txt` → verdict PASS (pasted below).
The NO rows are the recipient copies of Frederick's three mails in Leonard's, Marcus's, Martin's and Frederick's own
mailboxes: companions, never load-bearing. Linear (ART-793 … ART-854 and their comments), Trello
(""" + CARD + """ and its actions, the comment """ + PACKS_CMT + """ on """ + REFRESH_CARD + """), Contacts (""" + CONTACT + """) and GitHub (the icon settings) are unscoped.

""" + table(["Record", "Service class", "Visibility path"], reach_rows) + "\n\n" + fence(OUT["reach"]) + "\n")

MSGID_CONTROL = "CANf1NxdX_-=ufVrJRkObveGnt5gFc9BwveE1Phwxpp_8zfTrjA"
MSGID_RESULT = "0 matching files for the five thread ids; Message-ID 0 hits over all 81,406 thread files, control hit"
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
    [f"cmt_art793_1 … cmt_art854_2 (124 minted, {sum(1 for x in STMTS if x['table'] == 'linear.linear_comments')} used)", "linear /comments (id)", "0 base comments: 0 hits"],
    [f"Slack {ASK}, {POINTER}, {EXPORT}, {DM_ROOT}, {DM_REPLY}", "the channel's monthly shard (ts) · C06DJBJL798/1749234411.792129 (scratch/mint_checks.txt)", "control hit, seeded 0"],
    [f"Slack {ICON_REPLY} (row 8ce7e9eec2958c799a1aa11e4249cddd)", "every Slack shard (ts and row id) · C08R8CHB0QL/1758121809.236839 (scratch/inj_collisions.txt)", "control hit, seeded 0"],
    ["11 Gmail thread ids (" + ", ".join(list(PLAN["copies"].values())[:2]) + " …) and Message-IDs " + ", ".join(x["msg"].split("/", 1)[1] for x in (PLAN, DRAFT, QUOTE)), "content scan of all 81,404 thread files (Gmail ids cannot use lookup, Ask_Carriers §6a); scratch/new_ids.txt", "0 hits for all 14; thread ids decode as (first message ms << 20) | 20 random bits, like base ids"],
    [f"Rev3 Slack {FRED_REVIEW}, {RECAP_NOTE}, {TEST_POST}, {TEST_REVIEW}, {TEST_ACK}, {LEAVE_POST}, {LEAVE_REPLY}, {STORE_REPLY}", f"every Slack shard (ts, `hg.py search search-many`) · {INSTALLS_ROOT}", "scan_complete true: control hit, seeded 0"],
    [f"Rev3 Trello {PACKS_CMT} (action)", "`hg.py records` on trello /actions (id) · 68d1eb90bef538c7c5c559bc", f"control hit 1, seeded 0; first 8 hex = {TS['trello_logo_comment']}"],
    ["Rev3 Gmail: 5 thread ids (" + ", ".join(list(RESTART["copies"].values())[:2]) + " …) and Message-ID " + RESTART["msg"].split("/", 1)[1], "`hg.py search files gmail <id>` per thread id (file names); `hg.py search search-many` over every thread file for the Message-ID · control " + MSGID_CONTROL, MSGID_RESULT],
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
    [DM_REPLY, "Slack search \"halloween\" / from:marcus; the IM D05V2N6PZNU (the root shows reply_count 1)", "\"did the cheer fastcouch one, both 9:16 and 16:9\"", "0 'halloween' hits in the IM before Sep 26", "claim met first (T3 / T19 / K16)"],
    [TEST_POST + " → " + TEST_REVIEW, "Slack search \"cheer fastcouch\" or a read of #zombie-art, then the thread (the root shows reply_count 2)", "\"quick test on cheer fastcouch, 9:16 and 16:9\"; the review never says halloween", "0 base hits on \"cheer fastcouch\"", "overturning (T3 / K21)"],
    [RECAP_NOTE, "Slack search on a creative's name (\"couch alpha 50\", \"barrel marketing2\", \"balloons alpha 50\") or a read of #zm-animations", "the three creative names as the sheet writes them", "NEW TERM \"old ua cuts\"", "overturning (T9 / K20)"],
    [FRED_REVIEW, "Slack search \"Unity\" / from:frederick; the fake-installs thread in #zombie-match3d (the root shows reply_count 5)", "\"any new ad going on Android US phone has to be with me by Fri Oct 10\"", "the thread's four base replies on fake installs", "overturning (T20 / K19)"],
    [LEAVE_POST + " + " + LEAVE_REPLY, "Slack search \"statics\" / \"julia\" / from:martin; a read of #company-internal", "\"takes the ad statics\"; \"julia on the ad statics\"", "the base leave posts in the channel (C05KNDCHAAG/1756717965.570179)", "overturning (T21 / K22)"],
    [RESTART["msg"], "Gmail search \"Unity\" / \"landscape\" / from:frederick in Claire's mailbox", "subject \"Unity retention restart\"; the two creative names", "0 'retention restart' hits in Claire's mailbox", "overturning (T22 / K23)"],
    [PACKS_CMT, "Trello search \"end card 001\" / the Marketing Video Refresh card (its title names Marcus and Frederick)", "\"end card 001 still has the old zombies on the packs\"", "the card's base actions on \"Marketing Video Refresh\"", "overturning (T23 / K24)"],
    [QUOTE["msg"], "Gmail search \"Halloween\" in Claire's mailbox", "subject \"Halloween props for Zombie Match 3D\"", "base KayKit purchase/seat mails are in Robert's and Arthur's mailboxes, not Claire's", "decoy (T7)"],
    [EVT[CLAIRE], "Calendar list for Thu Oct 2 (the ask: \"before thursday's review\")", "summary \"ZM3D Halloween review\"", "Claire's recurring Thursday meetings", "destination deadline (K8)"],
]) + f"""

Dynamic-change seeds (claim met first · overturned by · why met first · why decisive):

""" + table(["Trap", "Claim met first", "Overturned by", "Why met first", "Why decisive"], [
    ["T1", f"Martin: \"halloween store screens are exported\" {EXPORT}", f"the Store folder {F['store']}: Halloween iPhone 6.5 ×5 and Google Play ×6 files, no iPad 12.9 set", "#zombie-art is Claire's home channel; the post is the newest store news", "R2 / H1 Store tab lists the iPad set; a set with no Halloween version is a Halloween version to make"],
    ["T2", f"Leonard: \"maybe we swap the icon around the 24th?\" {ASK}", f"Arthur's calendar {DOC}: merge cut Thu Oct 16 12:00 PT, \"Anything that ships in the build has to be merged by then\"", "the ask is the first read", "the icon ships in the binary (Nov 6 clean-up 'icon and screenshots back to normal'; match3d ProjectSettings)"],
    ["T3", f"Marcus's IM reply {DM_REPLY} + UA masters {F['ua']} ({', '.join(I['files_ua'])}): both cheer fastcouch cuts done", f"Robert's review {TEST_REVIEW}: the July capture, the old background is still under it, it cannot ship; Marcus's {TEST_ACK}: will redo both from the Sep 16 capture", "the done claim and the file names carry the task's own keyword", "a test the art director turned down is not a seasonal version, so each cut is a Halloween version to make"],
    ["T4", f"Frederick's Sep 12 draft {DRAFT['msg']}: flight Oct 20-31, art due Fri Oct 17, all four campaigns", f"Frederick's Sep 30 changes {PLAN['msg']}: Android US tablet ends Oct 12, flight Oct 18-31, due Wed Oct 15", "the draft is the fuller plan and a search for 'October UA plan' returns both", "the changes mail names the draft ('the October plan I sent on the 12th') and says 'not the 17th'"],
    ["T20", f"Frederick's Sep 30 changes {PLAN['msg']}: every Halloween ad by Wed Oct 15", f"his thread reply {FRED_REVIEW}: any new ad going on Android US phone by Fri Oct 10; iOS UK stays on the 15th", "the mail is the source the ask names", "the reply is from the same owner, later, and says 'not the 15th'"],
    ["T21", f"Leonard: \"Martin has the icon and the stills\" {ASK}", f"Martin's post {LEAVE_POST} and Leonard's reply {LEAVE_REPLY}: Julia takes the ad statics, store art stays with Martin", "the ask is the first read", "the requester's own reply comes after the ask, so the correction lands last"],
    ["T22", f"the ticket notes on {BY['squirrelfail landscape']['ticket']} and {BY['mrfluffernot landscape']['ticket']}: iOS UK tablet and Android US tablet", f"Frederick's Sep 29 mail {RESTART['msg']}: both left off iOS UK tablet", "the ticket is the source the sheet's Read me names", "only Android US tablet remains, so his Sep 30 rule skips them"],
    ["T23", f"{BY['end card 001']['ticket']} cmt_art833_1: rendered from Android #1529, after the swap", f"Frederick's comment {PACKS_CMT} on {REFRESH_CARD}: the old zombies are still on the packs, so end card 001 and its 16:9, 1:1 and 4:5 cuts need a re-render", "the build passes the deck's rule", f"base agrees (Marcus {PACKS_OLD}, Martin's new packs {PACKS_NEW}), and the deck's Refresh first covers a re-render"],
    ["T5", "ART-774's Mar–Apr spec list (iPhone 6.5 / 5.5, three iPad sizes, Play phone + tablet)", f"the sheet's Store tab {SHEET} and Leonard's Sep 3 ask C06DJBJL798/1756914854.743319", "a Linear search for store screenshots returns ART-774", "the live sets are the three on the Store tab"],
    ["T9", f"ART-795's catalogue note cmt_art795_1 (\"Captured from Android #456 on Apr 7\")", f"Marcus's #zm-animations note {RECAP_NOTE} (\"couch alpha 50 on android #1935\")", "the ticket is the source the sheet's Read me names", "the deck: \"If a later capture has replaced it, the newest capture is the one that counts\""],
    ["T19", f"Marcus's reply {DM_REPLY} (\"did the cheer fastcouch one\")", "ART-851 cmt_art851_1 (the 4:5 cut Sep 17 from the Sep 16 re-capture) — the reply names \"both 9:16 and 16:9\" only", "the reply is the completion note for the cut family", "the 4:5 was never in the test, so it is a Halloween version to make"],
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
    ["Temporal Field", "sql_lint, base_check Check C PASS", f"dates in text agree with the fields: Frederick's changes mail (2025-09-30T23:10Z) names 'the October plan I sent on the 12th' ({DRAFT['msg']}, 2025-09-12T17:40Z); Marcus's reply (Sep 29) follows Claire's Sep 26 note and his test post follows it the same day; Robert's review (Sep 30 16:05Z) follows the test; Frederick's reply (23:42:18Z) follows his changes mail and says 'not the 15th'; Martin's post (14:41:26Z) is before the ask and Leonard's reply (23:31:47Z) after it; the restart mail (Sep 29 23:48Z) follows Leonard's 22:48Z budget post (base C07C2866011/1759186080.203099, context only, a channel Claire is not in) and says the campaigns went back on today; every catalogue comment is a minute after its ticket; the calendar doc (modified 22:40Z) is after the ask (22:05Z)"],
    ["Cross-service Referential", "base_check Check A PASS; fact_check PASS", f"every sheet Unity row names an existing ticket ART-793 … ART-854; the Read me names the Trello card that exists ({CARD}); Martin's 'halloween folder' is {F['root']}; Marcus's 'UA masters in the halloween folder' is {F['ua']} in it; the deck title Robert quotes matches {DECK}; Frederick's reply sits in the base thread {INSTALLS_ROOT}; the card comment sits on the base card {REFRESH_CARD}; its 'Martin's new packs' is {PACKS_NEW}, after Marcus's {PACKS_OLD}"],
    ["Quantitative / Reconciliation", f"Slack reply counters (D05V2N6PZNU root reply_count 1, latest_reply = the reply ts; {TEST_POST} 2; {LEAVE_POST} 1; base {INSTALLS_ROOT} 4 → 5); Trello badges comments 1 on both cards", "no total of ads or calls is stated in any seeded text (Marcus's '3 of the old ua cuts' is the three he names); the store sets' file counts (iPhone ×5, Play ×6) match the live sets' sizes"],
    ["State / Lifecycle", "Linear Done ⇔ started_at = created_at and completed_at = updated_at = the last comment; Canceled ⇔ canceled_at on ART-836 … ART-839; no comment after a close", "serving tickets are Done and unassigned (Frederick's catalogue of finished, live creatives); the four archived ones are Canceled on their paused date and carry no comment"],
    ["Identifier / Format", "id formats checked (1.F); Slack id = sha256(channel|ts)[:32]", "emails copied from the base; one naming scheme per service; platform word on every build number in the deck and the ticket notes (Android #… / iOS …); Marcus's note writes it once for its three numbers"],
    ["Semantic / Category", "—", "doc / deck / sheet titles match their content; the decoys state their own scope (Domino Delights; generic checklist)"],
    ["Other", "—", "voice per 1.C; no record states a call word, a total or the plan"],
]) + "\n\nStatic lint:\n\n" + fence(OUT["lint"]) + """

sql_lint warning disposition: the """ + LINT_WARNINGS + """ warnings are one class — the seven copies of the review event start / end on
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
geometry U {PRE.get('geometry', {}).get('U') if isinstance(PRE.get('geometry'), dict) else 'see report'}. {FC_LINE}
""")

A("""## 5 Intended disagreements

""" + table(["Disagreement", "Why realistic", "What resolves it"], [
    [f"Martin says the Halloween store screens are exported ({EXPORT}); the Store folder has no Halloween iPad set ({F['store']})", "he exported the iPhone and Play sets first; the iPad set was never exported", "the folder listing against the Store tab (" + SHEET + ")"],
    [f"Leonard suggests swapping the icon around the 24th ({ASK}); the calendar's cut is Oct 16 ({DOC})", "a CEO's casual question before reading the release dates", "the calendar: anything that ships in the build is merged by Thu Oct 16 12:00 PT"],
    [f"Frederick's Sep 12 draft ({DRAFT['msg']}) vs his Sep 30 changes ({PLAN['msg']})", "he said he would confirm before month end and did", "the later mail names the earlier one and states the two changes"],
    [f"Marcus's DM reply and the two files in UA masters ({DM_REPLY}, {F['ua']}) vs Robert's review ({TEST_REVIEW})", "Marcus's test sat on the July capture, though both cuts were re-captured on Sep 16 (cmt_art808_2, cmt_art816_2)", f"the review and Marcus's own reply {TEST_ACK}: both are redone from the Sep 16 capture"],
    [f"Frederick's Sep 30 mail, every Halloween ad by Wed Oct 15 ({PLAN['msg']}) vs his thread reply ({FRED_REVIEW})", "he spoke to the Unity rep that day and the mail does not carry it", "the reply: any new ad going on Android US phone by Fri Oct 10, iOS UK stays on the 15th"],
    [f"Leonard's split, Martin has the stills ({ASK}) vs Martin's vacation post ({LEAVE_POST})", "Leonard's ask keeps his standing split, and he answers Martin's post that evening", f"Leonard's reply {LEAVE_REPLY}, after the ask"],
    [f"the ticket notes on {BY['squirrelfail landscape']['ticket']} and {BY['mrfluffernot landscape']['ticket']} (both tablets) vs Frederick's restart mail ({RESTART['msg']})", "the notes were checked Sep 9, before the campaigns went back on", "the mail, then his Sep 30 rule on anything that only runs on Android US tablet"],
    [f"{BY['end card 001']['ticket']}'s Android #1529 render vs Frederick's card comment ({PACKS_CMT})", f"Marcus rendered end card 001 before Martin's new packs came in ({PACKS_OLD}, {PACKS_NEW})", "the comment, and the deck's Refresh first: re-capture, re-render or re-cut"],
    ["the boris cuts' 'live since Sep 12' vs their tickets' Jul 28 capture (cmt_art840_1, cmt_art841_1)", "the Boris opening was added on Sep 11 to footage captured the day before the swap", "the deck's threshold Android #1452 / iOS 1232"],
    [f"April catalogue notes (cmt_art795_1, cmt_art805_1, cmt_art797_1) vs Marcus's note ({RECAP_NOTE})", "Marcus re-recorded three cuts on current builds in September and said so in his own channel, not on Frederick's tickets", "the deck's newest-capture rule"],
    ["the portrait end card's Android #1450 render (cmt_art831_1) vs the Jul 29 swap", "#1450 succeeded at 11:51Z (C05433XK267/1753789877.590639), #1452 at 20:24Z (C05433XK267/1753820674.990309)", "the deck names Android #1452 / iOS 1232"],
    [f"the sheet as the list of what is running vs Julia's 4:5 static ({CARD_CMT}) and the portrait end card (ART-831)", "the sheet was last edited Sep 30 (the Read me pointer to the card), with no new rows; the static never made it on; the end card plays after every Android US phone video", "the ask's scope (\"everything players see\", \"every ad we're running\")"],
    [f"Martin's Sep 17 Halloween icon image ({ICON_POST}) vs an icon still to make", "a concept Martin floated 'for an app icon or an event' before the Halloween plan existed", f"Robert's reply {ICON_REPLY}: not for the app icon (too busy at that size); Leonard's Sep 30 ask still wants a Halloween icon"],
    ["Marcus's 'both 9:16 and 16:9' vs the cheer fastcouch 4:5 cut ART-851", "Marcus's trial pass (asked Sep 26, done Sep 29) dressed the two cuts he names; the 4:5 export of Sep 17 is a separate placement he did not dress", "the reply's exact set + the UA masters folder (two files); the 4:5 was never in the test"],
]) + "\n")

A("""## 6 Constraints for the prompt brief

""" + table(["Anchor", "May be named (noun phrases only)", "Record"], [["A1", "Leonard's Halloween message; Leonard's Halloween ask", ASK]]) + f"""

- Never name: where the rules live (the live creatives sheet's comment rule, the release calendar, Robert's deck, the
  changes mail, the restart mail, the Trello cards, the DM reply, Robert's review, Marcus's note, Frederick's thread
  reply, Martin's vacation post, the Store / UA masters folders) or what they say; any creative, ticket, build number,
  date or call; the vendor; Julia's 4:5 static or the portrait end card.
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
    [DM_REPLY, "seeded", "T3 / T19: both cheer fastcouch cuts (9:16, 16:9) done", "marcus.bennett@harmonygames.co 2025-09-29T17:20:37Z", "Claire's IM D05V2N6PZNU", "claim met first", "no"],
    [STORE_REPLY, "seeded", "K18: exported art needs no ticket", "leonard.hayes@harmonygames.co " + I["slack_leonard_store_reply"]["at"], "#zombie-art member", "evidence", "no"],
    [TEST_POST, "seeded", "K21: Marcus's quick test on cheer fastcouch", "marcus.bennett@harmonygames.co " + I["slack_marcus_test"]["at"], "#zombie-art member", "connecting", "no"],
    [TEST_REVIEW, "seeded", "T3 / CH4: Robert — the July capture, cannot ship", "robert@harmonygames.co " + I["slack_robert_test_reply"]["at"], "#zombie-art member", "overturning evidence", "no"],
    [TEST_ACK, "seeded", "T3: Marcus will redo both from the Sep 16 capture", "marcus.bennett@harmonygames.co " + I["slack_marcus_test_reply"]["at"], "#zombie-art member", "evidence", "no"],
    [RECAP_NOTE, "seeded", "T9 / CH9: three re-captures on Android #1935, #1896, #1966", "marcus.bennett@harmonygames.co " + I["slack_marcus_recapture"]["at"], "#zm-animations member", "overturning evidence", "no"],
    [FRED_REVIEW, "seeded", "T20 / CH8: any new ad on Android US phone by Fri Oct 10", "frederick.stone@harmonygames.co " + I["slack_fred_review_reply"]["at"], "#zombie-match3d member", "overturning evidence", "no"],
    [INSTALLS_ROOT, "base", "Robert's Unity fake-installs thread; reply_count 4 → 5 by the SQL", "Robert 2025-09-30", "#zombie-match3d member", "evidence (K19)", "no"],
    [LEAVE_POST, "seeded", "T21 / CH10: Martin out Oct 6-15, Julia takes the ad statics", "martin.walsh@harmonygames.co " + I["slack_martin_leave"]["at"], "#company-internal member", "overturning evidence", "no"],
    [LEAVE_REPLY, "seeded", "T21 / CH10: Leonard agrees", "leonard.hayes@harmonygames.co " + I["slack_leonard_leave_reply"]["at"], "#company-internal member", "overturning evidence", "no"],
    ["C0880U9751A/1758141269.804779", "base", "Leonard: '1.3.38 is out!' (the store sets' 'Live since Sep 17')", "Leonard 2025-09-17T20:34:29Z", "#zombie-match3d member", "evidence (Store tab dates)", "no"],
    [SHEET, "seeded", "H1: Read me / Store / Unity / Archive", "frederick.stone@harmonygames.co modified 2025-09-30T22:30:00Z", "shared with Claire", "authority", "no"],
    [DOC, "seeded", "H2: merge cut Thu Oct 16 12:00 PT; iOS screenshots with the Oct 17 submission; Play any day", "arthur.blake@harmonygames.co modified 2025-09-30T22:40:00Z", "shared with Claire", "authority", "no"],
    [DECK, "seeded", "H3: Android #1452 / iOS 1232 threshold; newest capture; music-baked masters; the four calls", "robert@harmonygames.co 2025-09-25T16:10:00Z", "shared with Claire", "authority", "no"],
    [DRAFT["msg"], "seeded", "T4 older version: flight Oct 20-31, due Fri Oct 17", "frederick.stone@harmonygames.co 2025-09-12T17:40:00Z", "Claire's INBOX", "superseded version", "no"],
    [PLAN["msg"], "seeded", "H4: Android US tablet ends Oct 12; flight Oct 18-31; due Wed Oct 15", "frederick.stone@harmonygames.co 2025-09-30T23:10:00Z", "Claire's INBOX", "authority", "no"],
    [RESTART["msg"], "seeded", "T22 / CH11: squirrelfail landscape and mrfluffernot landscape left off iOS UK tablet", "frederick.stone@harmonygames.co " + TS["gmail_fred_restart"], "Claire's INBOX", "overturning evidence", "no"],
    [QUOTE["msg"], "seeded", "T7: 'our Halloween Bits bundle … 39 USD'", "PERSON_6311_EMAIL 2025-09-24T14:00:00Z", "Claire's INBOX", "decoy", "no"],
    [EVT[CLAIRE], "seeded", "K8: ZM3D Halloween review Thu Oct 2 16:00–16:30Z", "leonard.hayes@harmonygames.co updated 2025-09-30T22:10:00Z", "Claire's calendar", "destination deadline", "no"],
    [F["root"], "seeded", "K12: ZM3D Halloween 2025 (Store, UA masters)", "leonard.hayes@harmonygames.co 2025-09-29T09:15:00Z", "shared with Claire", "connecting", "no"],
    [F["store"], "seeded", "T1: Halloween iPhone ×5, Google Play ×6, no iPad set", "martin.walsh@harmonygames.co files 2025-09-30T15:12Z", "shared with Claire", "overturning evidence", "no"],
    [F["ua"], "seeded", "T3: cheer_fastcouch_halloween_9x16.mp4, _16x9.mp4 (Marcus's test cuts)", "marcus.bennett@harmonygames.co 2025-09-29T17:05Z", "shared with Claire", "claim met first", "no"],
    ["ART-793 … ART-854", "seeded", "K11: 58 serving + 4 archived library tickets; comments carry campaigns, source build, master", "frederick.stone (catalogue), marcus.bennett (Sep 16 re-capture notes) 2025-09-08 … 2025-09-29", "Linear unscoped", "per-record evidence + write target", "no"],
    [CARD, "seeded", "K7: Halloween push card (Oct 21 list)", "PERSON_6094_TRELLO_USER_ID (Leonard) 2025-09-30T22:00:00Z", "Trello unscoped", "connecting", "no"],
    [CARD_CMT, "seeded", "T6: Julia's 4:5 static still running on iOS UK, not on the sheet", "4b4a68fc0fec0b254e4f9d8e (Frederick) 2025-09-30T23:20:00Z", "Trello unscoped", "overturning evidence", "no"],
    [PACKS_CMT, "seeded", f"T23 / CH12: end card 001 and its cuts still show the old zombies on the packs (card {REFRESH_CARD})", "4b4a68fc0fec0b254e4f9d8e (Frederick) " + TS["trello_logo_comment"], "Trello unscoped", "overturning evidence", "no"],
    [PACKS_OLD, "base", "Marcus posts EndCard001.mp4: 'the artwork on the packs … have the old zombies on it'", "Marcus 2025-08-04", "#zombie-art member", "evidence (T23)", "no"],
    [PACKS_NEW, "base", "Martin's new packs, after it", "Martin 2025-08-04", "#zombie-art member", "evidence (T23)", "no"],
    [CONTACT, "seeded", "T7: PERSON_6311 — Founder, KayKit", "contacts 2025-09-24T14:05:00Z", "Contacts unscoped", "context", "no"],
    ["C06DJBJL798/1755114007.441789", "base", "the 30 s cut's master has the music baked in (thread replies)", "Frederick 2025-08-13", "#zombie_marketing member", "evidence (ART-809's master note points here)", "no"],
    ["C06DJBJL798/1756914854.743319", "base", "Leonard asks Martin to export iphone / ipad / gp", "Leonard 2025-09-03T15:54:14Z", "#zombie_marketing member", "evidence (T5)", "no"],
    ["C06DJBJL798/1753968186.965269", "base", "Marcus's portrait UA end card", "Marcus 2025-07-31", "#zombie_marketing member", "evidence (T6 / T17)", "no"],
    ["C0880U9751A/1753820524.488479", "base", "Robert: iOS 1232 zombie swap with the new background", "Robert 2025-07-29T20:22Z", "#zombie-match3d member", "evidence (CH2)", "no"],
    ["C05433XK267/1753789877.590639", "base", "#builds: Match3D Android #1450 success", "Jenkins 2025-07-29T11:51Z", "#builds member", "evidence (T17)", "no"],
    ["C05433XK267/1753820674.990309", "base", "#builds: Match3D Android #1452 success", "Jenkins 2025-07-29T20:24Z", "#builds member", "evidence (T17, the threshold)", "no"],
    ["C08R8CHB0QL/1758121809.236839", "base", "Martin's Halloween icon concept ('for an app icon or an event'); reply counters bumped to 1 by the SQL", "Martin 2025-09-17T15:10:09Z", "#zombie-art member", "decoy (T13)", "no"],
    [ICON_REPLY, "seeded", "T13: Robert — 'not for the app icon, it gets too busy at that size'", "robert@harmonygames.co 2025-09-17T16:52:31Z", "#zombie-art member (thread reply)", "overturning evidence", "no"],
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
  late September (C08R8CHB0QL/1758121809.236839) and Aug 4 (C08R8CHB0QL/1754310794.907609), #zombie_marketing Aug–Sep (the
  30 s cut thread, Sep 3 export ask), the fake-installs thread C0880U9751A/1759211437.306779, #zm-animations September
  (C09ATAJ220H), #company-internal leave posts (C05KNDCHAAG/1756717965.570179).
- Rules and plans: the sheet, doc and deck; Frederick's three mails; the Trello card on ZM ROADMAP 6851a6569f3bf818760632ab
  and the base card 68768a1501ae552dbee94b8a; #builds Jul 29 (C05433XK267/1753789877.590639, C05433XK267/1753820674.990309);
  Robert's Jul 29 swap post C0880U9751A/1753820524.488479; ART-774; the match3d icon settings; Confluence
  page_release_checklist.

### Hazard audit (coherence_hazards.json, synth-cut)

""" + table(["Hazard", "Category", "Records", "Disposition"], [
    ["T02", "temporal", "Claire's thread files", "each seeded Gmail thread holds one message and joins no base thread"],
    ["T04", "temporal", "Linear issues completed before PRs", "none in scope: no seeded library ticket is tied to a PR; serving tickets are Done at their last comment and ART-836 … ART-839 are Canceled on their paused date"],
    ["T06", "temporal", f"Trello cards {CARD}, {REFRESH_CARD}", f"card dateLastActivity = the comment time 2025-09-30T23:20:00Z, board bumped to the same time; the base card moves 2025-08-20 → {TS['trello_logo_comment']}, its comment's time"],
    ["S03", "semantic", "Linear label vocabulary", "no label is set or read (empty label list)"],
    ["S04", "semantic", "GitHub display names", "no GitHub row is seeded"],
    ["R04", "cross-service referential", "Slack links to Google files", "excluded: no seeded Slack text links a Drive file; files are named by title (hazard_acknowledgements R04)"],
    ["R07", "cross-service referential", "GitHub ↔ #zombie-prs mirrors", "excluded: no PR is seeded (hazard_acknowledgements R07)"],
    ["R08", "cross-service referential", "invitations vs calendar rows", f"excluded: the review {UID} has no invitation mail by design (integration_exceptions; hazard_acknowledgements R08)"],
    ["Q01 / Q04", "quantitative", "Slack reply counters", f"the seeded IM root {DM_ROOT} carries reply_count 1, reply_users_count 1, latest_reply = the reply ts; the seeded roots {TEST_POST} (2) and {LEAVE_POST} (1) likewise; the base parent {ICON_POST} (row {ICON_POST_ID}) is bumped 0 → 1 with latest_reply = {ICON_REPLY.split('/')[1]}, and the base root {INSTALLS_ROOT} (row {INSTALLS_ROOT_ID}) 4 → 5 with latest_reply = {FRED_REVIEW.split('/')[1]}, one UPDATE each"],
    ["Q10", "quantitative", "copies of one message", f"Frederick's three mails: five byte-identical copies each ({PLAN['thread']}, {RESTART['thread']} etc.)"],
    ["Q11", "quantitative", "calendar copies of one event", f"seven copies of {UID} differ only in calendar_id, event_id and self"],
    ["L05", "state/lifecycle", "ART-774 Done with a dated spec", "dated_claim: read for its Mar–Apr spec list only (hazard_acknowledgements L05)"],
    ["L08", "state/lifecycle", "open issues assigned to quiet people", "none in scope: every seeded ticket is unassigned; the assignees the run sets (Marcus, Julia) are active_sep_2025_quiet_in_oct"],
    ["L11 / L12", "state/lifecycle", "Trello list state", f"the card sits in the open list 'Oct 21' with no checklist; the base card {REFRESH_CARD} stays where it is, open, with no list change"],
    ["I03", "identifier/format", "mailbox file aliases", "ids use the full address (claire.morgan@…), files follow the alias"],
    ["I14 / I15", "identifier/format", "Drive owner tokens; name vs native title", "real owner emails; Drive names equal the native titles (no .xlsx / .docx suffix)"],
    ["I16", "identifier/format", "Trello ids vs dates", "every seeded Trello id carries its record second"],
]) + """

Known-data-issue cards touched (`references/known_data_issues/synthcut.md`): SC-11 / SC-12 / SC-23 (no spend figure is
seeded or graded; `snowflake.ANALYTICS` read for channels only), SC-13 (the seeded card is in 'Oct 21', not the 'BETA: Oct 10'
list), SC-16 (ART-790 / ART-792 stay off the path), SC-22 (repaired on the path: base ART-792's
time_in_status_minutes 246277 exceeded its lifetime at the clock, 51,123 minutes since 2025-08-26T18:57:06Z; one
UPDATE sets it NULL like ART-774 / ART-790, updated_at untouched; 3,096 of 3,401 base issues carry the same artefact,
none other on this task's path), SC-36 (review attendees named explicitly, Victor Barnes not
invited), SC-49 / SC-54 (Frederick's founder status and pay never graded; he is active in Slack through 2025-09-30),
SC-58 (no monster roster name graded), SC-70 (times come from the doc and the mails, not Slack timezones).
""")

A(f"""## 11 Platform follow-ups

- Confirm in the Opus pre-check that `linear_list_comments` returns the seeded comments on ART-793 … ART-854 (verified
  carrier, Ask_Carriers §6b), that `gdrive_list_folder` on {F['store']} returns the file names, that
  `gslides_get_presentation` returns the element text of {DECK}, that `gsheets_values_batch_get` returns the four tabs of
  {SHEET}, and that `slack_read_thread` returns the seeded replies on {DM_ROOT}, {TEST_POST}, {LEAVE_POST} and the base
  root {INSTALLS_ROOT}, and that Trello returns the comment {PACKS_CMT} on the base card {REFRESH_CARD}.
- Drive media files carry metadata only (eval lint INFO): the task needs only their names.
- The conditional budget rows (DM read, draft read, contacts, icon settings, threshold post, read-backs) count 0 until a
  run shows them; the unconditional floor is {FLOOR} (call_budget_floor {M['volume_exception']['call_budget_floor']}).
- Write targets: Claire creates and owns the plan doc and the tracker at run time; ART tickets are unscoped; confirm each
  write returns ok in the pre-check.
- Confluence `page_release_checklist` (decoy) to be re-verified after any regeneration.
""")

CNT = Counter((x["table"], x["op"]) for x in STMTS)
N_INS, N_UPD = sum(v for (_, op), v in CNT.items() if op == "insert"), sum(v for (_, op), v in CNT.items() if op == "update")
N_SLACK, N_SLACK_UP = CNT[("slack.slack_messages", "insert")], CNT[("slack.slack_messages", "update")]
N_CMT, N_MAIL = CNT[("linear.linear_comments", "insert")], CNT[("gmail.gmail_messages", "insert")]
WALK = [
    ["Inventory", f"{N_SLACK} Slack + {N_SLACK_UP} UPDATE (two base parents' reply counters), 62 Linear issues + {N_CMT} comments + 1 UPDATE (base ART-792's status counter, SC-22), 19 Drive rows, 1 Docs, 1 + 4 Sheets, 1 + 4 + 8 Slides, {N_MAIL} + {N_MAIL} Gmail, 7 GCal, 1 Trello card + {CNT[('trello.trello_actions', 'insert')]} actions + 1 card UPDATE + 1 board UPDATE, 1 Contacts", "PASS", "sql_lint rows by schema (section 4)"],
    ["Check A", "references: channels C06DJBJL798 / C08R8CHB0QL / C0880U9751A / C09ATAJ220H / C05KNDCHAAG / D05V2N6PZNU exist with Claire a member; Linear users usr_175c0d7bc72ed244 / usr_c77c50cc15c5342d / usr_8140f09bf9f1b94c exist; team_ART exists; Drive parents (Leonard's root d_63fffeb4fab5233ed5bb73, Frederick's d_175c0d7bc72ed244b944cb, Arthur's d_cc3e90160f490686039986, Robert's d_9f7ba94f7526d54d8482ba) exist; Trello board 6851a6569f3bf818760632ab, list 6851a677e090018224fb8c7f and card " + REFRESH_CARD + " exist; members PERSON_6094_TRELLO_USER_ID / 4b4a68fc0fec0b254e4f9d8e exist", "PASS", "base_check Check A PASS; 1.B"],
    ["Check A", "uniqueness over the full collections (1.F): Drive, GCal, Trello, Contacts, Slack ts, Gmail thread and Message-IDs, Linear ids above ART-792", "PASS", "scratch/inj_collisions.txt (own key + positive control per collection), scratch/new_ids.txt; the rev3 rows of 1.F"],
    ["Check A", "ownership / membership / share identities: every Drive-family row shares with real addresses; Docs / Sheets / Slides sharing equals its drive_files row", "PASS", "gen_sql.py drive_row(); check-sql 1.E"],
    ["Check A", "ID contracts: Slack id = sha256(channel/ts)[:32] (asserted in gen_sql.py), f_ / d_ + 22 hex, evt_ + 22 hex, ical_uid 32 hex @hg4, Trello id = hex(record second) + 16 hex, Linear id = identifier", "PASS", "eval lint id_contract: no flag"],
    ["Check B", "structure: literal JSON in every `*_json` column (json.dumps), no generated column written, NOT NULL columns supplied, Linear text dates exactly YYYY-MM-DDTHH:MM:SSZ, state_history_json an empty JSON list", "PASS", "sql_lint 0 errors; eval lint generated_column / text_time_format / missing_required: no flag"],
    ["Check C", f"dates: every event timestamp ≤ 2025-10-01T00:00:00Z; replies after parents (D05V2N6PZNU/1759166437.080255 after D05V2N6PZNU/1758872409.023532, {TEST_REVIEW} after {TEST_POST}, {FRED_REVIEW} after {INSTALLS_ROOT}); comments after their issue's created_at; issue updated_at = the newest comment; Trello dateLastActivity = the comment time", "PASS", "sql_lint, base_check Check C PASS; gen_sql.py assert_seed()"],
    ["Check C", f"statuses and counts: Done tickets carry started_at = created_at and completed_at = updated_at = the last comment; Canceled ⇔ canceled_at (ART-836 … ART-839); reply_count 1 on the IM root, the export post and the vacation post, 2 on {TEST_POST}; 0 → 1 on the base parent C08R8CHB0QL/1758121809.236839 and 4 → 5 on the base root {INSTALLS_ROOT} (UPDATEs); Trello badges comments 1 on both cards", "PASS", "base_check Check C PASS"],
    ["Check C", "claimed updates and superseding records: the changes mail names the draft and is later; Frederick's reply is later than the changes mail; Marcus's note is later than the April captures; the restart mail is later than the Sep 9 ticket checks; Leonard's reply is later than the ask", "PASS", "01_Hardness_Manifest.json traps T4 / T9 / T20 / T21 / T22 version_records (chronology checked by hardness_gate)"],
]
CR = [
    ["temporal", "the catalogue notes on the Sep 8 tickets name tablet campaigns that only launched on Sep 9, so a Sep 8 record states a later fact", "cmt_art816_1 … cmt_art835_1 (\"Unity: iOS UK tablet, Android US tablet.\"); sheet 'Live since Sep 9' f_02b1968f5e882366fbb883", "holds: \"Unity: …\" is the planned routing Frederick catalogued the day before the Sep 9 launch; no comment claims an upload before Sep 9"],
    ["temporal", "Frederick's changes mail (Sep 30 23:10Z) is after Leonard's ask (22:05Z), so the ask cites a mail that does not yet exist", f"ask {ASK} (\"Frederick is sending his october UA plan tonight\"); {PLAN['msg']}", "holds: the ask announces it as future (\"tonight\"); the mail arrives an hour later, before the clock"],
    ["temporal", "the calendar doc was modified at 22:40Z, after the ask, so its Oct 16 cut may be a later edit the agent cannot date", f"{DOC} modified 2025-09-30T22:40:00Z", "holds: only the current body is relied on and it is before the seed bound; no earlier state is claimed"],
    ["temporal", "the re-export tickets ART-851 … ART-854 are dated the day they went live, after the Sep 12 batch, so the library looks back-filled", "cmt_art851_1 (2025-09-17T17:36Z) after cmt_art808_2 (Sep 16 re-capture); ART-854 created 2025-09-25T17:00Z", "holds: each export follows its source capture and its own ticket"],
    ["temporal", "Marcus's note (Sep 25) comes after the exports it should precede (ART-852 Sep 17, ART-853 Sep 23), so it reads out of order", f"{RECAP_NOTE}; cmt_art852_1, cmt_art853_1", "holds: the note reports past work ('re-recorded') and gives no date, so a later note about earlier captures is consistent"],
    ["temporal", "Martin's vacation post (14:41Z) is before the ask (22:05Z), so the ask's split is the later word", f"{LEAVE_POST}; ask {ASK}; reply {LEAVE_REPLY}", "holds: Leonard's own reply is at 23:31:47Z, after the ask, so the correction still lands last"],
    ["temporal", "the restart mail says the campaigns went back on 'today', and Sep 29 needs base backing", f"{RESTART['msg']} ({TS['gmail_fred_restart']}); base C07C2866011/1759186080.203099; base C0880U9751A/1759248267.162909", "holds: Leonard set the iOS budget back up at 22:48:00Z that day, an hour before the mail, and Frederick says in base on Sep 30 that only the retention campaigns run"],
    ["semantic / category", "\"Unity retention campaigns\" in the Read me might contradict base talk of UA campaigns", f"{SHEET} Read me; base C0880U9751A/1759248267.162909 (Frederick, Sep 30: \"We are only running the retention campaigns\")", "holds: the Read me matches Frederick's own Sep 30 wording"],
    ["semantic / category", "the archived tickets are Canceled while the sheet calls them \"paused\", two names for one state", "ART-836 (Canceled, canceled_at 2025-09-15T17:00:00Z, description \"Paused on Sep 15, see the Archive tab\")", "holds: a paused creative's library ticket closed as Canceled is the catalogue's normal state; it is a T14 control"],
    ["referential / cross-service", "Martin's export post says \"the halloween folder\" but the folder is owned by Leonard, so the reference may be read as a different folder", f"{EXPORT}; {F['root']} \"ZM3D Halloween 2025\" (owner Leonard, Martin writer)", "holds: the only Halloween folder shared with the team; Martin's files sit in its Store subfolder"],
    ["referential / cross-service", "Marcus's \"the halloween pack\" could be the in-game Halloween pack, not the KayKit asset pack", f"{DM_REPLY}; C0880U9751A/1738109783.735889 (Robert, Jan 28: \"we have the Halloween pack\")", "holds: both name the same studio-owned props pack, and no call depends on which it is"],
    ["referential / cross-service", "the vendor's sender token has no base footprint, so the identity rests on one injected row", f"contact {CONTACT} (job \"Founder, KayKit\"); base seat-assignment mails in Arthur's mailbox (blake@harmonygames.co_1821793728224896590)", "holds: the identity is a fresh external person, as the base handles vendors, and T7 is a plain distractor at rev3, so nothing rests on it"],
    ["quantitative / reconciliation", "the Store folder file counts (iPhone 5, Play 6) might not match the live sets the Store tab lists", f"{F['store']}; Leonard's Sep 3 export ask C06DJBJL798/1756914854.743319", "holds: no count is graded or stated; the names alone decide which set has a Halloween version"],
    ["quantitative / reconciliation", "Frederick's \"Still running on Unity …\" notes could disagree with his catalogue note on the same ticket", "cmt_art793_1 / cmt_art793_2 (both \"iOS UK phone, Android US phone\"); cmt_art811_2", f"holds: generated from one campaigns field per creative (roster_final.json); the one later change is the Sep 29 restart mail {RESTART['msg']}, which is T22 by design"],
    ["state / lifecycle", "a Done library ticket for a creative that still serves reads as finished, so a comment and an assignee on it look wrong", "ART-793 (Done, unassigned, \"UA creative library: …\")", "holds: the tickets are Frederick's catalogue of finished, running creatives, not work items; the run's assignment is the follow-through Leonard asks for"],
    ["state / lifecycle", "Frederick's pay ends in May per the ledger (SC-54), so he cannot be acting on Sep 30", "activity.json frederick.stone@harmonygames.co status active_sep_2025_quiet_in_oct, last Slack 2025-09-30 (C0880U9751A/1759248267.162909)", "holds: SC-54 is a \"don't grade\" card; Frederick posts in Slack the same day"],
    ["identifier / format", "Frederick's Message-IDs might not match his mail client's style", f"{PLAN['msg'].split('/', 1)[1]}; base frederick.stone@harmonygames.co/<CANf1NxdX_-=ufVrJRkObveGnt5gFc9BwveE1Phwxpp_8zfTrjA@mail.gmail.com>", "holds: the seeded ids use his CANf1Nx prefix and his lowercase from-name 'frederick stone'"],
    ["identifier / format", "iOS Internal #1452 exists (Aug 20), so a reader could take \"#1452\" for an iOS build", f"C05433XK267/1755696763.753209; deck {DECK} (\"Android #1452 / iOS 1232\")", f"holds: the deck and every ticket note write the platform word; Marcus's note {RECAP_NOTE} writes 'android' once for its three numbers, and none is a threshold"],
    ["other", "the twelve exports added in revision 02 could read as padding for the call count", "ART-843 … ART-854; scenario_gen/redteam_dispositions.md RT16", "holds: each is a separately serving placement with its own campaign note and source; two change their parent's call (ART-844 couch marketing2 30s 16:9, ART-849 julia 1:1 android tablet); judged not padding by the independent review"],
    ["other", "Leonard's ask (978 characters) is above his p99 length, so it reads as planted", f"ask {ASK}; conventions.json slack.per_person_hours_and_style leonard.hayes p99 672, max 11,397", "holds: a bulleted brief is his long-post style (base 1,901-char post C0880U9751A/1753402851.712119); tracked for /prompt"],
    ["intended disagreement — T1", "Martin's 'same comps as the live sets' could cover the iPad set even though no iPad file is in the folder (it might be elsewhere)", f"{EXPORT} ('exported to the halloween folder'); {F['store']} (Halloween iPhone ×5, Google Play ×6)", "holds: Martin names the folder; the folder has no iPad file; no other Halloween iPad file exists in Drive (gdrive search 'iPad' + 'Halloween': 0)"],
    ["intended disagreement — T2", "without \"the app icon\" named in the calendar, the icon's Oct 16 date is an unsupported inference", f"{DOC} (\"Anything that ships in the build …\"; \"Nov 6 submission: … icon and screenshots back to normal\"); match3d ProjectSettings", "holds: the icon ships in the app binary on both stores; the doc's own Nov 6 line treats the icon as a build item"],
    ["intended disagreement — T3", "Marcus made the files and said so, and Robert only commented on one version of them, so they could still be reused", f"{DM_REPLY}; {F['ua']}; {TEST_REVIEW} (\"We can't ship these\"); {TEST_ACK}", "holds: the art director says they cannot ship and Marcus agrees to redo both, so neither file is a seasonal version"],
    ["intended disagreement — T4", "the draft is the fuller plan, so the changes mail may be read as an addendum that keeps Oct 17", f"{PLAN['msg']} (\"not the 17th\")", "holds: the changes mail states the new date and why"],
    ["intended disagreement — T5", "ART-774's spec list could still be the store scope", "ART-774 (Done 2025-04-15); C06DJBJL798/1756914854.743319", "holds: Leonard's Sep 3 ask and the Store tab name the three live sets"],
    ["intended disagreement — T6", "Julia's 4:5 static's ticket names iOS UK phone, so the Trello comment is redundant or contradicts the sheet", f"ART-826 cmt_art826_1; Trello {CARD_CMT}", "holds: the ticket records routing, the card comment confirms it is still running and off the sheet; they agree"],
    ["intended disagreement — T8", "the boris cuts' \"Captured Jul 28\" may be footage from the swap day itself", "cmt_art840_1; C0880U9751A/1753820524.488479 (swap Jul 29 20:22Z)", "holds: Jul 28 is the day before the swap; Android #1427 (C05433XK267/2025-07.json#/1561) is the Jul 28 build"],
    ["intended disagreement — T9", "a note by Marcus in an animation channel is a side note, not the record of the creative", f"{RECAP_NOTE}; cmt_art795_1; deck {DECK} slide 2", "holds: the deck counts the newest capture and the note is by the person who recorded it"],
    ["intended disagreement — T17", "Android #1450 already had the new background, so the end card is current", "cmt_art831_1 (\"Rendered from Android #1450\"); C05433XK267/1753789877.590639 vs C05433XK267/1753820674.990309", "holds: the deck's line is the swap build Android #1452"],
    ["intended disagreement — T19", "Marcus's reply could cover every cheer fastcouch export, the 4:5 too", f"{DM_REPLY} (\"both 9:16 and 16:9\"); {F['ua']} (two files); ART-851", "holds: the reply and the folder name two cuts, Robert turned those down, and the 4:5 is a later export that was never in the test"],
    ["intended disagreement — T20", "the reply says 'every new Android creative', so it could reach Android US tablet too", f"{FRED_REVIEW} (\"any new ad going on Android US phone\"); {PLAN['msg']} (Android US tablet ends Oct 12)", "holds: the date is tied to Android US phone; the tablet campaign ends before the flight, so a cut on both tablets stays on the 15th with iOS UK"],
    ["intended disagreement — T21", "Martin's post covers Oct 6-15 only, so statics due after he is back would stay his", f"{LEAVE_POST}; {LEAVE_REPLY}; roster_final.json due", "holds: every working static is due Oct 10 or Oct 15, inside the window, and the icon and iPad set stay with Martin as the post says"],
    ["intended disagreement — T22", "the restart mail is about iOS retention, so it may not change a ticket's Unity routing", f"{RESTART['msg']}; cmt_art811_2 (checked Sep 9)", "holds: it names both cuts, says they stay on Android US tablet only, and is later than the ticket's check"],
    ["intended disagreement — T23", "Frederick says they can keep serving, so a Halloween version over the same render is fine", f"{PACKS_CMT}; {PACKS_OLD}; {PACKS_NEW}; deck {DECK}", "holds: the same comment says they need a re-render before anyone builds on them, base shows the new packs came after the render, and the deck's Refresh first covers a re-render"],
    ["intended disagreement — T13", "Robert's reply only criticises this concept's size, so the concept could still be the Halloween icon after a tweak (Reuse)", f"{ICON_REPLY} (\"not for the app icon, it gets too busy at that size. A Halloween icon should stay as simple as the one we have\"); deck {DECK} (\"Halloween version: dress it from the current art\")", "holds: the art director turns the concept down for the icon and asks for a simple icon like the current one, i.e. a Halloween version dressed from the current icon"],
    ["referential — ART-831 note", "Frederick's \"Not on the live creatives sheet yet\" on ART-831 contradicts the sheet's Read me (\"One row per creative serving\")", f"cmt_art831_2 (2025-09-29T17:40Z); sheet {SHEET} modified 2025-09-30T22:30:00Z", "holds: the note says the sheet is incomplete for this one card, the same kind of omission his Trello comment records for Julia's 4:5 static; nothing claims the sheet lists it. S0r declined dropping the sentence (`01_Scenario_Design.md` section 14)"],
    ["quantitative / temporal — SC-22 repair", "clearing ART-792's time_in_status_minutes edits a base record the task does not grade, so it reads as tampering", "ART-792 (Team Epic, created 2025-08-26T18:57:06Z, base value 246277 > 51,123 minutes of lifetime at the clock); ART-774 / ART-790 already NULL", "holds: the counter is a derived export artefact that runs to 2026-02-13 (SC-22); NULL is the in-distribution value (286 base issues), no state, date or text changes, and the record sits on the store-screenshot path a run meets"],
]
A(f"""## 12 Self-review

**Checks A–C walk** (`Evals/0_Injection_Quality_Eval.md`), every statement in `01_Universe_Inject.sql` ({N_INS} INSERT, {N_UPD}
UPDATE; no DELETE, no upsert):

""" + table(["Check", "Item", "Verdict", "Evidence"], WALK) + f"""

Lint dispositions: `hg.py lint` is pasted in section 4; its one INFO is accepted — the task reads the Drive media files'
names from a folder listing, never their bytes.

**Touched-data census** is in section 10 (every serving surface, the threads around the seeded records, the rules and
plans); each hazard id that intersects it is cited there against `coherence_hazards.json` with a disposition.

**Counter-readings** (strongest argument that each judgement should fail, and what resolves it):

""" + table(["#", "Category", "Counter-reading", "Evidence", "Verdict"], [[n, *row] for n, row in enumerate(CR, 1)]) + f"""

Re-verified facts (§6a.3): re-read from the base through `tools/hg.py` for rev3 — #builds Android #1450
(C05433XK267/1753789877.590639) and #1452 (C05433XK267/1753820674.990309); Robert's swap post C0880U9751A/1753820524.488479;
the 30 s cut thread C06DJBJL798/1755114007.441789; Leonard's Sep 3 export ask C06DJBJL798/1756914854.743319; Robert's
fake-installs root {INSTALLS_ROOT} (reply_count 4); Marcus's EndCard001 post {PACKS_OLD} and Martin's new packs {PACKS_NEW};
Martin's leave post C05KNDCHAAG/1756717965.570179; the cover precedent C05KNDCHAAG/1719394673.875309; the base card
{REFRESH_CARD} (dateLastActivity 2025-08-20, no comments); Claire's membership of every channel used (check-sql, 1.E).

Unresolved: {FC_LINE} Every forecast here is UNCALIBRATED, and the ledger holds only this task's records. R_BUILD_CUT flips
rubric-only facts, not surface slots. The rendering of Drive folder listings, Slides element text and IM thread replies was
seen at the rev2 pre-check; the new thread replies and the comment on the base Trello card are first confirmed at the next
one (section 11). Martin keeps the icon and the iPad set and is away Oct 6-15 while both are due by the Oct 16 12:00 PT cut.
""")
TARGET = WF / "01_Grounding_Dossier.md"
GATE_BLOCK = re.search(r"^```\nSTAGE GATE injection: .*?^```$", TARGET.read_text(), re.M | re.S) if TARGET.exists() else None
TARGET.write_text("\n".join(doc).rstrip() + "\n" + ("\n" + GATE_BLOCK.group(0) + "\n" if GATE_BLOCK else ""))
print("wrote", TARGET, len("\n".join(doc).splitlines()), "lines · ledger", len(ledger), "rows")

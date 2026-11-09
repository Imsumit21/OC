#!/usr/bin/env python3
"""Build 09_Rubrics.json, the V3 rubric_rows evidence and rows.json for the Leonard stockholder close-out.

Holder values come from oe/oe_data.py (asserted against the solver truth). Every quote in an evidence field is asserted
as a substring of its record here. The rubric text carries no em dash, no en dash and no local file reference."""
import json
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "oe"))
import oe_data as D  # noqa: E402
import oe_lib as L  # noqa: E402

WS = L.WS
GM = "Universe_Normal/Normal_HarmonyGames_Gmail/Services_Data/gmail/threads/leonard@harmonygames.co_%s.json"
SL = "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/slack/messages/%s/%s.json"
GD = "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/gdocs/data.json"
MB = "leonard.hayes@harmonygames.co/"
PROMPT = open(os.path.join(L.TI, "04_Prompt.txt"), encoding="utf-8").read()
OE_TEXT = open(os.path.join(L.TI, "08_Oracle_Events.md"), encoding="utf-8").read()
CONSENT = open(os.path.join(os.path.dirname(HERE), "oe", "consent_nov10_2023_exhibit_a.txt"), encoding="utf-8").read()
MAN = json.load(open(os.path.join(L.WF, "01_Hardness_Manifest.json"), encoding="utf-8"))
NODES = {m["id"]: " ".join(m["nodes"]) for m in MAN["mechanism_portfolio"]}
n = D.n

SP_SHEET = "the holder sheet and the investor letter in my close-out folder"
SP_LETTER = "with the letter worked up from my investor email draft in #winddown"
SP_NOTES = "the messages to holders as drafts in my Gmail"
SP_LINEAR = "the Linear issues"
SP_GRIFFIN = "the heads-up to Griffin"
SP_REPLY = "the reply in #winddown"
SP_KPMG = "an answer to KPMG's audit request for Griffin from yesterday"
SP_RULES = "Can you take care of all of it the way those lay it out?"
for sp in (SP_SHEET, SP_LETTER, SP_NOTES, SP_LINEAR, SP_GRIFFIN, SP_REPLY, SP_KPMG, SP_RULES):
    assert sp in PROMPT, sp

PROJ = "ec2ea957-fc8e-4958-b809-0fb735b1e916"
NOTES_ID = "f_a37b403d5200d4f0a31d31"
SHEET_ID = "f_5ecaa967db3adcfa440b09"
FOLDER_ID = "d_601064334a0b493022fe83"
OUTLINE_ID = "f_75dddccabb26eeea4842c8"
WD = "C0ADGSZKR3R"
LIST_TS = "1770934638.035469"
KPMG_T = "1857029474983245439"
BOARD_T = "1856958794180374704"
START = ("gdocs", NOTES_ID)  # the gate's record lookup reads the base export only, so a seeded Linear id cannot be a path step
VIA_NOTES = [START]


def path(*hops):
    return [{"service": s, "id": i} for s, i in hops]


def sql_ins(table, **ident):
    rows = [x["row"] for x in L.STMTS if x.get("table") == table and x["op"] == "insert" and all(x["row"].get(k) == v for k, v in ident.items())]
    assert len(rows) == 1, (table, ident, len(rows))
    return rows[0]


def S(service, rid, table, ident, column, rec_col, hops, why):
    row = sql_ins(table, **ident)
    return {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table, "identity": ident, "column": column,
            "source_value": row[column], "evidence_path": path(*hops), "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": rec_col,
                                  "rationale": f"Seeded {table} row; {rec_col} = {row[rec_col]} (before the freeze)."}}


_files = {}


def jload(p):
    if p not in _files:
        _files[p] = json.load(open(os.path.join(WS, p), encoding="utf-8"))
    return _files[p]


def B_mail(thread, idx, hops, why):
    p = GM % thread
    m = jload(p)["messages"][idx]
    return {"service": "gmail", "id": MB + thread, "source_file": p, "pointer": f"/messages/{idx}/body", "source_value": m["body"],
            "evidence_path": path(*hops, ("gmail", MB + thread)), "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_pointer": f"/messages/{idx}/date_parsed",
                                  "rationale": f"Base message dated {m['date_parsed']}, before the freeze; a sent mail does not change."}}


def B_slack(ch, ts, hops, why, field="text"):
    import datetime as _dt
    mon = _dt.datetime.fromtimestamp(float(ts), _dt.timezone.utc).strftime("%Y-%m")
    p = SL % (ch, mon)
    arr = jload(p)
    i = next(j for j, m in enumerate(arr) if m.get("ts") == ts)
    rid = f"{ch}/{ts}"
    return {"service": "slack", "id": rid, "source_file": p, "pointer": f"/{i}/{field}", "source_value": arr[i][field],
            "evidence_path": path(*hops, ("slack", rid)), "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_pointer": f"/{i}/ts",
                                  "rationale": f"Base Slack post, ts {ts}, before the freeze."}}


def B_doc(doc, idx, hops, why):
    d = jload(GD)["docs_documents"][idx]
    assert d["document_id"] == doc
    return {"service": "gdocs", "id": doc, "source_file": GD, "pointer": f"/docs_documents/{idx}/body_text", "source_value": d["body_text"],
            "evidence_path": path(*hops, ("gdocs", doc)), "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_pointer": f"/docs_documents/{idx}/modified_time",
                                  "rationale": f"Base document last modified {d['modified_time']}, before the freeze."}}


def mail_idx(thread, pat):
    msgs = jload(GM % thread)["messages"]
    hits = [i for i, m in enumerate(msgs) if pat in m["body"]]
    assert hits, (thread, pat)
    return hits[0]


def seeded_msg(thread, pat):
    rows = [x["row"] for x in L.STMTS if x.get("table") == "gmail.gmail_messages" and x["op"] == "insert" and x["row"]["thread_id"] == MB + thread and pat in x["row"]["body_text"]]
    assert rows, (thread, pat)
    return min(rows, key=lambda r: int(r["internal_date"]))


def SM(thread, pat, hops, why):
    r = seeded_msg(thread, pat)
    return S("gmail", MB + thread, "gmail.gmail_messages", {"id": r["id"]}, "body_text", "date", [*hops, ("gmail", MB + thread)], why)


# ---- records and quotes -----------------------------------------------------------------------------------------------
REC = {}
SQLN = L.squash(L.norm(L.SQL.replace("''", "'")).replace("\\n", " "))


def rec(key, label, source, *quotes):
    txt = L.squash(L.norm(str(source["source_value"]).replace("''", "'")))
    for q in quotes:
        assert L.squash(L.norm(q)) in txt, (key, q)
    REC[key] = {"label": label, "src": source, "quotes": quotes}


def note(key, label, *quotes):
    """A record cited only in the evidence text (its quotes are asserted against the injection SQL)."""
    for q in quotes:
        assert L.squash(L.norm(q)) in SQLN, (key, q)
    REC[key] = {"label": label, "src": None, "quotes": quotes}


def frag(key, *which):
    r = REC[key]
    qs = [r["quotes"][i] for i in which] if which else list(r["quotes"])
    return r["label"] + (" (" + "; ".join(f"'{q}'" for q in qs) + ")" if qs else "")


rec("project", f"the Holder records project {PROJ}",
    S("linear", PROJ, "linear.linear_projects", {"id": PROJ}, "description", "created_at", [START], "The prompt names the holder project in Linear."),
    "the sheet is what Sunset asked for", "Send KPMG's confirmation as a reply to all once the sheet is done.",
    "States once the sheet is done: Canceled where the line holds nothing; otherwise Todo where its own note is waiting for me, and Done where it isn't.",
    "On every issue with no note of its own, Canceled included, say why.", "one issue per holder on Carta")
rec("notes", f"Leonard's close-out notes {NOTES_ID}",
    S("gdocs", NOTES_ID, "gdocs.docs_documents", {"document_id": NOTES_ID}, "body_text", "modified_time", VIA_NOTES, "The prompt names the close-out notes doc."),
    "Finish my draft one in the folder rather than starting another.", "One row per issue on the sheet, and the counts go by rows.",
    "Carta is the record, over any date in the letters. If a line's last day has passed, it holds nothing.",
    "Told means a written message about the closing, sent to them directly and delivered, from one of the three of us (a post in a channel doesn't count); for a fund, its partner.",
    "the closing if they have not been told, their last day if they have one", "Each note says what they hold.",
    "Anything they asked about their holding that we never answered gets answered in their note",
    "Messages go to the email on each holder's issue.", "The three of us get no row, only the totals.",
    "Labels for the sheet: Nothing, Already told, Closing, Last day, Closing and last day.",
    "Share it and the letter with Robert", "notes ready for me by Tuesday, as Gmail drafts",
    "everything goes in the close-out folder, not the Wind Down one",
    "Griffin's partner gets a heads-up as a reply to all on their own Board position mail from Feb 12, asking for their vote as preferred holders on the dissolution. That one can go out once the sheet is done",
    "when the sheet is ready, reply under my list in #winddown and say who goes first", "Whoever's last day comes first goes first.",
    "the holder sheet comes first, the notes and everything else run off it", "bring it up to date as a letter I can send. the update outline has the sections")
rec("sheet", f"the spreadsheet {SHEET_ID} ('Holder list (draft)', in the folder {FOLDER_ID})",
    S("gsheets", SHEET_ID, "gsheets.sheets_spreadsheets", {"spreadsheet_id": SHEET_ID}, "title", "modified_time", [*VIA_NOTES, ("gsheets", SHEET_ID)], "The notes name the draft sheet in the close-out folder."))
rec("folder", f"the folder Stockholder close-out {FOLDER_ID}",
    S("gdrive", FOLDER_ID, "gdrive.drive_files", {"id": FOLDER_ID}, "name", "modified_time", [*VIA_NOTES, ("gdrive", FOLDER_ID)], "The notes name the close-out folder."))
rec("sunset", "Sunset's intake mail in thread 1857034369525983506",
    SM("1857034369525983506", "Before they st", VIA_NOTES, "The project says the sheet is what Sunset asked for; a search for Sunset's stockholder mail finds it."),
    "One line per holder of stock or options, with what each holds today (for options, what's vested) and any last day",
    "Total shares and options outstanding", "A count of holders by what each still needs to hear from you", "Directors in office, and who holds the preferred vote")
rec("kpmg", f"KPMG's request in thread {KPMG_T}",
    SM(KPMG_T, "Shares outstanding by class", [START], "The prompt names KPMG's audit request."),
    "1. Shares outstanding by class, showing what each fund holds.",
    "2. Each outstanding option line by holder, and their total, using each effective date as Carta shows it, regardless of when recorded.",
    "3. Shares outstanding plus those options, as one figure.", "4. Any financing or other significant event since that date.", "replying to all Recipients")
rec("kpmg2", f"KPMG's clarification in thread {KPMG_T}",
    SM(KPMG_T, "Two clarifications", [START], "It is the last message of the thread the prompt names."),
    "a line terminated on or before the as-of date counts only what had vested by its termination date", "For item 4, we need any new financing", "and whether the company is winding down")
rec("board", f"Robert's reply in the Board position thread {BOARD_T}",
    SM(BOARD_T, "That leaves Leonard", VIA_NOTES, "The notes name the Board position mail."), "That leaves Leonard and me on the board")
rec("calvin", "Calvin Price's forward of Carta's Jan 23 update in thread 1856121753612004097",
    SM("1856121753612004097", "extra", [START], "A mailbox search for the address on ENG-2452 finds it."),
    "Last day to exercise Feb. 20, 2026 (previously Jan. 24, 2026)")
rec("dsn", "the Delivery Status Notification in thread 1856860994291529096",
    SM("1856860994291529096", "wasn't delivered", [START], "It is in the thread of the Feb 11 letter to the address on ENG-2457."), "Your message wasn't delivered to PERSON_3140_EMAIL")
rec("robert_told", "Robert's Feb 12 mail in thread 1773963101399472184",
    SM("1773963101399472184", "hear this from me", [START], "A search for the address on ENG-2446 finds it."), "we're closing the company")
rec("akin_mail", "Leonard's Feb 12 mail to Husnu Akin in thread 1856961760270377901",
    SM("1856961760270377901", "Harmony is shutting", [START], "A search of Leonard's sent mail for the closing finds it."), "Harmony is shutting down")
rec("akin_tie", "Matthew Collins's Sep 9 2023 mail in thread 1776432843811839680",
    B_mail("1776432843811839680", 0, [START], "A search for 'and Akin' finds it; it comes from the address on ENG-2447."), "akin", "Hi PERSON_4337_NAME and Akin,")
rec("griffin_told", "Leonard's Feb 9 mail to Griffin's partner in thread 1856675475513544349",
    B_mail("1856675475513544349", 13, [START], "A search for the address on ENG-2438 finds it."), "decided to shut the company down")
rec("griffin_split", "the purchaser schedule in thread 1771880236343640719",
    B_mail("1771880236343640719", 0, [START], "A search for the Series Seed class finds it."), "2,662,255", "84,438")
rec("griffin_names", "the purchaser schedule as re-sent in thread 1771880236343640719",
    B_mail("1771880236343640719", 3, [START], "A search for the Series Seed class finds it."), "[ORGANIZATION_NAME_0151] II, L.P.", "[ORG_NAME_0153] II Side Fund, L.P.")
rec("schedule", "the disclosure schedule in thread 1773160163779741845",
    B_mail("1773160163779741845", 1, [START], "A search for the advisor total finds it."), "30,518 shares", "61,038 shares", "6,104 shares", "103,764 shares")
rec("digest", "Carta's Nov 20, 2023 digest in thread 1783169549554193375",
    SM("1783169549554193375", "accepted", [START], "A search for the option numbers the notices skip finds it."), "accepted  option grant ES-8", "accepted  option grant ES-10")
assert "1/24th monthly/no cliff" in CONSENT and "See Specific Vesting Start Dates in Carta" in CONSENT
_cidx = mail_idx("1782034095239486005", "please see execution copy of Board Consent")
rec("digest2", "Carta's Nov 17, 2023 digest in thread 1782897835407336831",
    B_mail("1782897835407336831", 0, [START], "A search for the option numbers the notices skip finds it."), "option grant ES-9", "Matthew Collins", "option grant ES-11")
rec("dm_size", "Leonard's DM D04UC0UEN2V/1693246524.896449",
    B_slack("D04UC0UEN2V", "1693246524.896449", [START], "It is in the DM a Slack search on the address on ENG-2440 finds."), "30518 shares / 103764 shares")
rec("tor_dm", "Leonard's DM D09R59580EM/1762285888.654689",
    B_slack("D09R59580EM", "1762285888.654689", [START], "A Slack search for the runway message finds it."), "running very low on cash")
_tidx = mail_idx("1782034095239486005", "Full Legal Name: [PERSON_NAME_2769]")
rec("es15_tie", "Leonard's Oct 18, 2024 option list in thread 1782034095239486005",
    B_mail("1782034095239486005", _tidx, [START], "A search for the address on ENG-2460 finds it."), "Full Legal Name: [PERSON_NAME_2769] [PERSON_NAME_0093]", "Email: PERSON_4243_EMAIL")


def hdr(key, label, thread, idx, *quotes):
    """A sender name from a base message's From header; the body records do not carry it."""
    frm = jload(GM % thread)["messages"][idx]["from"]
    for q in quotes:
        assert q in frm, (key, q, frm)
    REC[key] = {"label": label, "src": None, "quotes": quotes}


rec("digest_oct23", "Carta's Oct 23, 2024 digest in thread 1813700131573811805",
    B_mail("1813700131573811805", 0, [START], "A search for the option numbers the notices skip finds it."), "option grant ES-15", "Omer [PERSON_NAME_0092] [PERSON_NAME_0008]", "option grant ES-17", "[PERSON_NAME_0036] [PERSON_NAME_0005]")
rec("digest_es15", "Carta's digest in thread 1813881602779637554",
    B_mail("1813881602779637554", 0, [START], "A search for the option numbers the notices skip finds it."), "Ömer [PERSON_NAME_0093] accepted")
rec("mail_es15", "the holder's Jun 5, 2024 reply in thread 1801054030196213239",
    B_mail("1801054030196213239", 1, [START], "A search for the address on ENG-2460 finds it."), "[PERSON_NAME_45917] [PERSON_NAME_0093]")
hdr("from_es15", "the sender line in thread 1800824149233468611", "1800824149233468611", 0, "brian <PERSON_4243_EMAIL>")
rec("notice_es16", "Carta's notice for ES-16 in thread 1847333318158821452",
    B_mail("1847333318158821452", 0, [START], "A search for Carta's termination notices finds it; it names ES-16."), "EMPLOYEE_0032 [PERSON_NAME_0011]")
_t16 = mail_idx("1782034095239486005", "Full Legal Name: [PERSON_NAME_2768]")
rec("list_es16", "Leonard's Oct 18, 2024 option list in thread 1782034095239486005",
    B_mail("1782034095239486005", _t16, [START], "A search for the address on ENG-2461 finds it."), "[PERSON_NAME_0121]", "Full Legal Name: [PERSON_NAME_2768] [PERSON_NAME_0011]", "Email: cameron@harmonygames.co")
rec("mail_es16", "the holder's Aug 7, 2024 mail in thread 1805972621079109235",
    B_mail("1805972621079109235", 0, [START], "A search for the address on ENG-2461 finds it."), "[PERSON_NAME_0120]")
hdr("from_es16", "the sender line in thread 1805453551522119612", "1805453551522119612", 0, "PERSON_0031_NAME <cameron@harmonygames.co>")
hdr("from_es17", "the sender line in thread 1788274927802139924", "1788274927802139924", 0, "ryan <PERSON_2314_EMAIL>")
rec("letter_es17", "Leonard's letter in thread 1847335165884050330",
    B_mail("1847335165884050330", 0, [START], "A search of the holder's address finds it."), "34,409")
_widx = mail_idx("1774211155651873582", "me and my brothers")
rec("wire", "the wire thread 1774211155651873582", B_mail("1774211155651873582", _widx, [START], "It is in the mail a search on the family's addresses finds."), "me and my brothers")
rec("es12_dm", "Leonard's DM D05SDEQEK61/1770827705.815759", B_slack("D05SDEQEK61", "1770827705.815759", [START], "A search of Leonard's DMs with the holder finds it."), "I have some announcements to make")
note("draft_rows", f"Sheet1 of the spreadsheet {SHEET_ID}", "GRIFFIN GAMING PARTNERS", "2,746,693", "copied from the Nov 2024 list")
note("nomail_2452", "the comment on ENG-2452", "No mail with that address before Feb")
note("contact_collins", "the contact matthew.collins@harmonygames.co", "Investor and advisor (left the board May 2025)")
note("outline_holders", f"the update outline {OUTLINE_ID}", "Holders, per the Nov 2024 owner list")
note("outline_board", f"the update outline {OUTLINE_ID}", "Board, process, who is running the close")
note("outline_means", f"the update outline {OUTLINE_ID}", "Distributions, tax papers, your options")
note("outline_games", f"the update outline {OUTLINE_ID}", "What happens to the games and the IP")
note("outline_thanks", f"the update outline {OUTLINE_ID}", "Thank you")
rec("consent", "the board consent attached in thread 1782034095239486005, Exhibit A ('1/24th monthly/no cliff' for 30,518, 61,038, 6,104 and 6,104)",
    B_mail("1782034095239486005", _cidx, [START], "Leonard's mailbox; a search for the option issuances finds the thread and the attachment opens."), "please see execution copy of Board Consent")
rec("advisor_doc", "the advisor agreement f_3ee38465decc57e61df6e5",
    B_doc("f_3ee38465decc57e61df6e5", next(i for i, d in enumerate(jload(GD)["docs_documents"]) if d["document_id"] == "f_3ee38465decc57e61df6e5"), [START], "Shared with Leonard; a Docs search for the advisor agreement finds it."),
    "All shares shall vest on a pro rata basis monthly over a 2-year period.")
rec("dm_2440", "Leonard's Feb 9 DM D04UC0UEN2V/1770664988.379119",
    B_slack("D04UC0UEN2V", "1770664988.379119", [START], "A Slack search for the address on ENG-2440 finds the DM."), "shut down the company we decided")
rec("family", "the family list in thread 1770141224265557526",
    B_mail("1770141224265557526", 0, [START], "A search for the address on ENG-2445 finds it."), "patrick@harmonygames.co", "PERSON_2275_EMAIL")
rec("family_rule", f"Leonard's reply {WD}/1770949310.220519",
    S("slack", f"{WD}/1770949310.220519", "slack.slack_messages", {"ts": "1770949310.220519"}, "text", "created_at", [START, ("slack", f"{WD}/{LIST_TS}"), ("slack", f"{WD}/1770949310.220519")], "It is a reply under Leonard's list in #winddown."),
    "one note to whoever has always handled it for a family covers the rest of the family's lines", "that note says what each of them holds")
rec("covered_rule", f"Leonard's reply {WD}/1770949322.640149",
    S("slack", f"{WD}/1770949322.640149", "slack.slack_messages", {"ts": "1770949322.640149"}, "text", "created_at", [START, ("slack", f"{WD}/{LIST_TS}"), ("slack", f"{WD}/1770949322.640149")], "It is a reply under Leonard's list in #winddown."),
    "Mark those lines Covered on the sheet in place of a label, and count them that way")
rec("arthur_share", f"Leonard's reply {WD}/1770949351.317729",
    S("slack", f"{WD}/1770949351.317729", "slack.slack_messages", {"ts": "1770949351.317729"}, "text", "created_at", [START, ("slack", f"{WD}/{LIST_TS}"), ("slack", f"{WD}/1770949351.317729")], "It is a reply under Leonard's list in #winddown."),
    "the sheet goes to you as well as Robert")
rec("ledger_reply", "Leonard's reply C07C2866011/1768418331.402719",
    S("slack", "C07C2866011/1768418331.402719", "slack.slack_messages", {"ts": "1768418331.402719"}, "text", "created_at", [START, ("slack", "C07C2866011/1768418331.402719")], "A Slack search for the seed share count finds it."),
    "go by the ledger")
rec("term", "the Reset Financing Term Sheet f_11040fe5d66821bd6951aa",
    B_doc("f_11040fe5d66821bd6951aa", 40, [START], "A Docs search for 'ledger' finds it."),
    "Founder common: 6,000,000", "Series Seed Preferred (all non-founder investors): 3,051,879", "Options outstanding: 268,772")
rec("cert", "the certificate f_90c029015fc474199cf736",
    B_doc("f_90c029015fc474199cf736", 360, [START], "A Docs search for 'dissolve' finds it."), "the holders of a majority of the outstanding shares of Preferred Stock")
rec("recap", "Leonard's Feb 9 wind-down support request in thread 1856688113228112603",
    B_mail("1856688113228112603", mail_idx("1856688113228112603", "We are out of funds"), [START], "A search for 'out of funds' finds it."), "We are out of funds")
rec("draft", f"Leonard's investor email draft {WD}/1770664700.848759",
    B_slack(WD, "1770664700.848759", [START], "The prompt names the investor email draft in #winddown."),
    "Given our current runway of less than a month", "We are initiating an orderly wind-down process",
    "We will also evaluate what to do with the remaining IP and codebase", "Our priorities are to handle employee and contractor obligations properly",
    "we did not get the metrics", "we do not have the funding to continue operating", "meet tax and compliance requirements", "Sunset the products in a controlled way")
rec("sent", f"Leonard's post {WD}/1770841239.761999",
    B_slack(WD, "1770841239.761999", [START], "It is in the channel the prompt names."), "All termination letters are sent")
rec("license", f"Leonard's post {WD}/1770924424.711879",
    B_slack(WD, "1770924424.711879", [START], "It is in the channel the prompt names."), "data licensing", "we can own the entire IP")
rec("signed", f"the post {WD}/1770931777.561519",
    B_slack(WD, "1770931777.561519", [START], "It is in the channel the prompt names."), "wind down agreement and data agreement reviewed and signed with")
rec("insolvent", f"the Unity note {WD}/1770932147.282819",
    B_slack(WD, "1770932147.282819", [START], "It is in the channel the prompt names."), "the company is insolvent and we have no cash reserves left")
rec("helpshift", f"the post {WD}/1770789534.434749",
    B_slack(WD, "1770789534.434749", [START], "It is in the channel the prompt names."), "move domino delights and zombie match off Helpshift before Feb 28th")
rec("list", f"Leonard's list {WD}/{LIST_TS}",
    B_slack(WD, LIST_TS, [START], "It is in the channel the prompt names."), "Reaching out to our angels properly")
rec("claire_q", "Claire Morgan's message C51ECE5102ED/1770903714.600249",
    B_slack("C51ECE5102ED", "1770903714.600249", [START], "A search of Leonard's DMs for the equity question finds it."), "equity lerimiz")
# The outline row carries no timestamp column, so the letter rows cite the notes for the sections and the outline only in the evidence text.
OUTLINE_TXT = L.norm(str(sql_ins("gslides.slides_page_elements", object_id="el_b4a6a6d9a533")["text"]))
OUTLINE_TXT2 = L.norm(str(sql_ins("gslides.slides_page_elements", object_id="el_9dabe7a0ac53")["text"]))
OUTLINE_TXT3 = L.norm(str(sql_ins("gslides.slides_page_elements", object_id="el_453848aef60e")["text"]))
assert "Holders, per the Nov 2024 owner list" in OUTLINE_TXT.replace("\\n", "\n") and "Distributions, tax papers, your options" in OUTLINE_TXT2.replace("\\n", "\n") and "Thank you" in OUTLINE_TXT3
SQLNORM = L.squash(L.norm(L.SQL.replace("''", "'")))
assert L.squash("Investor and advisor (left the board May 2025)") in SQLNORM

CARTA_F = {"ENG-2450": "F12", "ENG-2451": "F13", "ENG-2452": "F14", "ENG-2453": "F15", "ENG-2454": "F16", "ENG-2455": "F17", "ENG-2456": "F18", "ENG-2457": "F19", "ENG-2458": "F20", "ENG-2459": "F21", "ENG-2460": "F22", "ENG-2461": "F23", "ENG-2462": "F24", "ENG-2463": "F25"}
for r in D.OPTION:
    k, tid = r[0], r[4]
    m = jload(GM % tid)["messages"][0]
    assert "Last day to" in m["body"], k
    grant = f"Granted {n(r[6])}"
    vest = f"Vested {n(r[7])}"
    last = "exercise " + r[9]
    rec(f"carta_{k}", f"Carta's notice for {r[3]} in thread {tid}", B_mail(tid, 0, [START], f"A search for Carta's termination notices finds it; it names {r[3]}."), grant, vest, last)

LETTER_THREADS = {}
ledger = open(os.path.join(L.WF, "08_OE_Writing_Ledger.md"), encoding="utf-8").read()
for t in set(re.findall(r"leonard\.hayes@harmonygames\.co/(18568\d+)", re.search(r"\| F27 \|.*", ledger).group(0))):
    p = GM % t
    if os.path.exists(os.path.join(WS, p)):
        m0 = jload(p)["messages"][0]
        if "shutting down" in m0["body"]:
            LETTER_THREADS[str(m0.get("to"))] = t
LT = {}
for k in ("ENG-2450", "ENG-2453", "ENG-2456", "ENG-2457", "ENG-2458", "ENG-2460"):
    t = next(v for a, v in LETTER_THREADS.items() if D.EMAIL[k] in a)
    LT[k] = t
    rec(f"letter_{k}", f"Leonard's Feb 11 letter in thread {t}", B_mail(t, 0, [START], "A search of the holder's address since Feb 1 finds it."), "The company is shutting down")
rec("letter_advice", f"Leonard's Feb 11 letter in thread {LT['ENG-2453']}", B_mail(LT["ENG-2453"], 0, [START], "A search of the holder's address since Feb 1 finds it."), "exercising is not recommended")

for k in D.ISSUES:
    row = sql_ins("linear.linear_issues", identifier=k)
    rec(f"issue_{k}", f"the issue {k}", S("linear", k, "linear.linear_issues", {"identifier": k}, "description", "created_at", [START, ("linear", k)], "One of the issues in the holder project the prompt names."), f"Email: {D.EMAIL[k]}")
    cm = [x["row"] for x in L.STMTS if x.get("table") == "linear.linear_comments" and x["op"] == "insert" and x["row"]["issue_id"] == k and "owner list" in x["row"]["body"]]
    if cm:
        rec(f"own_{k}", f"the owner-list comment on {k}", S("linear", k, "linear.linear_comments", {"id": cm[0]["id"]}, "body", "created_at", [START, ("linear", k)], "A comment on an issue in the holder project."), cm[0]["body"])

# Sidecar limits: seeded Linear records are not visible to the gate's lookup, and the certificate body exceeds its bounded read.
# They stay cited in the evidence text (their quotes are asserted above); the sidecar cites the other records of each row.
for _k, _v in REC.items():
    if _v["src"] is not None and _v["src"]["service"] == "linear":
        _v["src"] = None
REC["cert"]["src"] = None

# ---- rows -------------------------------------------------------------------------------------------------------------
R = []
KIND = {1: "lookup", 3: "interpretation", 5: "multi-source"}
LEAD = {1: "Lookup", 3: "Interpretation", 5: "Multi-source"}
BAD = re.compile(r"[—–]|\.sql\b|\.json\b|\.md\b|Working_Files|task_inputs|solver|truth\.|/Users/|SQL L\d+|\bsuch as\b|\be\.g\.|for example|\bOE \d|\bledger F|\bF\d{1,2}\b|gate \d|Brief", re.I)


def add(tag, t, w, fact, span, oe, fids, vals, acc, why, srcs, alt, valid, idle, dec="none", dist="none", amb="none", grp="none", ovl="none", slots=(), cat="Outcome", verify=None, final=None):
    src_objs, frs = [], []
    merged = {}
    for s in srcs:
        key, which = s if isinstance(s, tuple) else (s, ())
        merged.setdefault(key, []).append(which)
    for key, picks in merged.items():
        which = tuple(dict.fromkeys(i for p in picks for i in p)) if all(picks) else ()
        frs.append(frag(key, *which))
        o = REC[key]["src"]
        if o is not None and o not in src_objs:
            src_objs.append(o)
    if not src_objs:
        src_objs.append(REC["notes"]["src"])
    ev = "Sources: " + "; ".join(frs) + f". Accept: {acc}."
    just = f"{LEAD[w]}: {why}."
    R.append({"tag": tag, "t": t, "w": w, "kind": KIND[w], "why": why, "fact": fact, "span": span, "oe": list(oe), "fids": fids, "vals": vals, "verify": verify or t.replace("The Agent ", "", 1), "final": final or "the deliverable named in the title", "acc": [acc], "alt": alt,
              "just": just, "ev": ev, "dec": dec, "dist": dist, "valid": valid, "idle": idle, "amb": amb, "grp": grp, "ovl": ovl, "slots": list(slots), "cat": cat, "srcs": src_objs, "cand": len(R) + 1})


def nm(k):
    return D.TITLE[k]


def oe_for(pattern):
    m = re.search(pattern, OE_TEXT, re.M)
    assert m, pattern
    return f"OE {m.group(1)}"


OE_SHEET = "OE 39"
LABEL = {k: D.label(k) for k in D.ISSUES}
HOLD = {k: D.TRUTH[k] for k in D.ISSUES}
LASTD = {"ENG-2450": "March 31, 2026", "ENG-2452": "February 20, 2026", "ENG-2453": "March 31, 2026", "ENG-2456": "April 30, 2026", "ENG-2457": "April 30, 2026", "ENG-2458": "April 30, 2026", "ENG-2459": "February 21, 2026", "ENG-2460": "March 31, 2026", "ENG-2463": "April 30, 2026"}
MONTHS = {"February": "02", "March": "03", "April": "04"}
for k, v in LASTD.items():
    mo, dd, yy = v.replace(",", "").split()
    assert HOLD[k]["Last day"] == f"{yy}-{MONTHS[mo]}-{int(dd):02d}", (k, v, HOLD[k]["Last day"])
ADV = {"ENG-2440": ("ES-8", 30518, "81,383"), "ENG-2446": ("ES-11", 6104, "31,536"), "ENG-2447": ("ES-9", 61038, "86,470"), "ENG-2449": ("ES-10", 6104, "31,536")}
def TIE_W(k):
    return 3 if k == "ENG-2460" else 1


def TIE_F(k):
    return " F29" if k == "ENG-2460" else ""


def TIE_S(k):
    return ["es15_tie"] if k == "ENG-2460" else []


def TIE_WHY(k, base):
    return "Carta's notice names the holder by legal name, and Leonard's Oct 2024 option list ties that name to the address on ENG-2460" if k == "ENG-2460" else base


DIG = {"ENG-2440": ("digest", (0,)), "ENG-2449": ("digest", (1,)), "ENG-2446": ("digest2", (2,)), "ENG-2447": ("digest2", (0, 1))}
GRID = "`ENG-2438` `ENG-2463` `26`"
NOTE_OE = {"ENG-2441": 42, "ENG-2442": 43, "ENG-2443": 44, "ENG-2448": 45, "ENG-2449": 46, "ENG-2450": 47, "ENG-2452": 48, "ENG-2453": 49, "ENG-2456": 50, "ENG-2457": 51, "ENG-2458": 52, "ENG-2459": 53, "ENG-2460": 54, "ENG-2463": 55}
TOLD_F = {"ENG-2438": "F40", "ENG-2439": "F40", "ENG-2440": "F32", "ENG-2446": "F41", "ENG-2447": "F42 F43", "ENG-2444": "F44 F9", "ENG-2445": "F44 F9"}
# what decides each line's label and how much work that is
LBL_W = {"ENG-2451": 1, "ENG-2454": 1, "ENG-2455": 1, "ENG-2461": 1, "ENG-2462": 1,
         "ENG-2438": 3, "ENG-2439": 3, "ENG-2446": 5, "ENG-2440": 5, "ENG-2447": 5, "ENG-2444": 5, "ENG-2445": 5,
         "ENG-2441": 3, "ENG-2442": 3, "ENG-2443": 3, "ENG-2448": 3, "ENG-2449": 3,
         "ENG-2450": 3, "ENG-2453": 3, "ENG-2456": 3, "ENG-2458": 3, "ENG-2460": 5,
         "ENG-2452": 5, "ENG-2457": 5, "ENG-2459": 5, "ENG-2463": 5}
TOLDY = {
    "ENG-2438": ("Griffin's partner has Leonard's Feb 9 mail and the notes count a fund's partner", ["griffin_told", ("notes", (3,)), "issue_ENG-2438"], "F40 F4", "TOLD"),
    "ENG-2439": ("Griffin's partner has Leonard's Feb 9 mail and the notes count a fund's partner", ["griffin_told", ("notes", (3,)), "issue_ENG-2439"], "F40 F4", "TOLD"),
    "ENG-2440": ("a Slack search on the issue's address finds Leonard's Feb 9 DM about the shutdown, while the Feb 12 list shows the angels open", ["dm_2440", "list", ("notes", (3,)), "issue_ENG-2440"], "F32 F4 F8", "TOLD"),
    "ENG-2446": ("a search on the issue's address finds Robert's Feb 12 mail, with Leonard copied, while the Feb 12 list shows the angels open", ["robert_told", ("notes", (3,)), "issue_ENG-2446"], "F41 F4", "TOLD"),
    "ENG-2447": ("Leonard's Feb 12 mail went to Husnu Akin at an address not on the issue, and the issue's first name and old mail signed 'akin' from the issue's address tie that name to this holder", ["akin_mail", "akin_tie", ("notes", (3,)), "issue_ENG-2447"], "F42 F43 F4", "ALIAS"),
}
CLOSING = {
    "ENG-2441": ("no founder message since Feb 1 has the issue's address and the Feb 12 list shows the angels open", ["list", ("notes", (3,)), "issue_ENG-2441"], "F46 F4"),
    "ENG-2442": ("no founder message since Feb 1 has the issue's address and the Feb 12 list shows the angels open", ["list", ("notes", (3,)), "issue_ENG-2442"], "F46 F4"),
    "ENG-2443": ("no founder message since Feb 1 has the issue's address and the Feb 12 list shows the angels open", ["list", ("notes", (3,)), "issue_ENG-2443"], "F46 F4"),
    "ENG-2448": ("the latest Slack contact with TOR's partner is a November runway warning, which does not say the company is closing", ["tor_dm", "list", ("notes", (3,)), "issue_ENG-2448"], "F45 F46 F4"),
    "ENG-2449": ("no founder message since Feb 1 has the issue's address and the Feb 12 list shows the angels open", ["list", ("notes", (3,)), "issue_ENG-2449"], "F46 F4"),
}
FULL = {
    "ENG-2452": ("Carta's Oct 29 notice ended the line on Jan 24, but Calvin's forward of the Jan 23 update extends it to Feb 20, and no founder has written to him since", ["calvin", ("carta_ENG-2452", (2,)), ("notes", (2,))], "F14 F26 F27 F4", "EXT"),
    "ENG-2457": ("Leonard's Feb 11 letter looks sent, but the Delivery Status Notification in its thread shows it never arrived, and his February DM with this holder does not say the company is closing", [f"letter_ENG-2457", "dsn", "es12_dm", ("notes", (3,))], "F19 F27 F28 F4", "BOUNCE"),
    "ENG-2459": ("Leonard's 'All termination letters are sent' covers six letters, none to this holder, and a search of Gmail and his DMs finds no closing message", ["sent", ("notes", (3,)), "carta_ENG-2459"], "F21 F27 F8 F4", "LETTER"),
    "ENG-2463": ("Leonard's 'All termination letters are sent' covers six letters, none to this holder, and a search of Gmail and his DMs finds no closing message", ["sent", ("notes", (3,)), "carta_ENG-2463"], "F25 F27 F8 F4", "LETTER"),
}
DATE_NOTE = ["ENG-2450", "ENG-2453", "ENG-2456", "ENG-2458", "ENG-2460"]
NOTHING = ["ENG-2451", "ENG-2454", "ENG-2455", "ENG-2461", "ENG-2462"]
COVERED = ["ENG-2444", "ENG-2445"]

# -- sheet: the write and the volume row
add("sh_write", "The Agent writes the holder rows into the existing Holder list (draft) spreadsheet (f_5ecaa967db3adcfa440b09) in the Stockholder close-out folder", 1, "sheet.file", SP_SHEET, ["OE 5", "OE 6", OE_SHEET], "F4 F5 F6", "`f_5ecaa967db3adcfa440b09`",
    "a write of the holder rows to the spreadsheet f_5ecaa967db3adcfa440b09, on any tab; renaming the file is allowed", "the notes say to finish the draft sheet in the close-out folder rather than start another",
    ["sheet", ("notes", (0,))], "Any tab of the file and a rename pass.", "A values update on f_5ecaa967db3adcfa440b09", "No write to f_5ecaa967db3adcfa440b09 exists", final="Spreadsheet f_5ecaa967db3adcfa440b09", slots=["D1"])
OLD_LABELS = "one of the labels Nothing, Already told, Covered, Closing, Last day or Closing and last day, right or wrong"
OLD_MARK = 'marked "copied from the Nov 2024 list"'
OLD_WHY = "the old row is visible in Sheet1 of the draft, and the notes say to finish that draft with one row per issue"
OLD_CLEAR = "the old row is deleted or cleared; or any other sheet content is written over its holder name and figure"
OLD_FAIL = "Fails: the old row left as it is; only its Notes cell changed, with no ENG id or label"


def add_old(tag, holder, fig, reuse, acc, src):
    add(tag, f'The Agent deletes or clears the draft sheet\'s old row "{holder} {fig}" ({OLD_MARK}), writes other sheet content over its holder name and figure, or turns that row into {reuse}', 1, f"sheet.old_row.{tag}", SP_SHEET, ["OE 6", OE_SHEET], "F5 F6", "`copied from the Nov 2024 list`",
        acc, OLD_WHY, [src, ("notes", (0, 1, 9))], "Deleting, clearing, overwriting or reusing the row passes.", "A values update starting at the top of Sheet1 replaces the row", "No write to f_5ecaa967db3adcfa440b09 exists", final="Spreadsheet f_5ecaa967db3adcfa440b09")


add_old("old_griffin", "GRIFFIN GAMING PARTNERS", "2,746,693", f"the one row for either Griffin fund, or for both funds, by writing on it ENG-2438 or ENG-2439 or {OLD_LABELS}",
        f"{OLD_CLEAR}; or the row itself becomes the one row on the sheet for ENG-2438, for ENG-2439 or for both funds, with or without a separate row for the other fund (whether its names, labels and figures are right is graded by each fund's own share and label rows). {OLD_FAIL}; or kept beside separate rows of their own for both funds", "draft_rows")

# -- sheet: shares
SH_NAME = {"ENG-2438": "GRIFFIN GAMING PARTNERS II, L.P. (ENG-2438, or [ORGANIZATION_NAME_0151] II, L.P. as the purchaser schedule shows it)",
           "ENG-2439": "GRIFFIN GAMING PARTNERS II SIDE FUND, L.P. (ENG-2439, or [ORG_NAME_0153] II Side Fund, L.P. as the purchaser schedule shows it)"}
SH_FORM = "Series Seed, preferred or plain shares"
LEFTOVER = "a separate old draft row left on the sheet does not affect this row"
for k, val, w, dec, why, srcs, fids in [
    ("ENG-2438", 2662255, 3, "none", "the owner-list comment merges both funds, and the 2023 purchaser schedule splits them", ["griffin_split", "griffin_names", "own_ENG-2438", ("notes", (2,))], "F3 F37"),
    ("ENG-2439", 84438, 3, "none", "the owner-list comment merges both funds, and the 2023 purchaser schedule splits them", ["griffin_split", "griffin_names", "own_ENG-2439", ("notes", (2,))], "F3 F37"),
]:
    add(f"sh_sh_{k}", f"The Agent shows {SH_NAME[k]} holding {n(val)} Series Seed shares on its holder sheet (preferred or plain shares wording)", w, f"{k}.shares", SP_SHEET, [OE_SHEET, "OE 24", "OE 34"], fids, f"`{n(val)}`",
        f"the {k} row shows {n(val)} {SH_FORM}, under either of those two names for this fund; {LEFTOVER}", why, srcs, "Series Seed, preferred or plain shares wording passes.", f"The {k} row reads {n(val)}", "No holder sheet rows exist", slots=["K2" if k.endswith("38") else "K3"], final=f"Holder sheet row {k}")
for k, (es, opt, lst) in ADV.items():
    sl = {"ENG-2440": ("K5", 2), "ENG-2446": ("K6", 0), "ENG-2447": ("K4", 1), "ENG-2449": ("K7", 3)}[k][0]
    shares = HOLD[k]["Shares held now"]
    add(f"sh_sh_{k}", f"The Agent shows {nm(k)} ({k}) holding {n(shares)} Series Seed shares on its holder sheet (preferred or plain shares wording)", 5, f"{k}.shares", SP_SHEET, [OE_SHEET, "OE 19", "OE 20", "OE 34"], f"F3 F31 F33 F47", f"`{n(shares)}`",
        f"the {k} row shows {n(shares)} {SH_FORM}; {LEFTOVER}", f"the owner-list comment on {k} merges stock with the {es} option grant, and only the Carta grant digests and the disclosure schedule separate them", [f"own_{k}", "schedule", DIG[k]] + (["dm_size"] if k == "ENG-2440" else []) + [("notes", (2,))], "Series Seed, preferred or plain shares wording passes.", f"The {k} row reads {n(shares)} shares", "No holder sheet rows exist", dec=NODES["ADV"], dist="T1 owner-list merge", slots=[sl], final=f"Holder sheet row {k}")


def add_stock(k, sl=None):
    shares = HOLD[k]["Shares held now"]
    add(f"sh_sh_{k}", f"The Agent shows {nm(k)} ({k}) holding {n(shares)} Series Seed shares on its holder sheet (preferred or plain shares wording)", 1, f"{k}.shares", SP_SHEET, [OE_SHEET, "OE 3", "OE 34"], "F3 F47", f"`{n(shares)}`",
        f"the {k} row shows {n(shares)} {SH_FORM}", f"the owner-list comment on {k} gives the holding", [f"own_{k}"], "Series Seed, preferred or plain shares wording passes.", f"The {k} row reads {n(shares)} shares", "No holder sheet rows exist", slots=[sl] if sl else [], final=f"Holder sheet row {k}")


for k, sl in [("ENG-2448", "K13"), ("ENG-2441", "K14"), ("ENG-2442", "K15")]:
    add_stock(k, sl)

# -- sheet: options
for k, (es, opt, lst) in ADV.items():
    sl = "K8" if k == "ENG-2447" else f"ADVOPT_{k}"
    lower = f"a vested figure lower than {n(opt)} shown on that row fails"
    add(f"sh_op_{k}", f"The Agent shows {nm(k)} ({k}) holding {n(opt)} options on its holder sheet (with or without the word vested; {lower})", 5, f"{k}.options", SP_SHEET, [OE_SHEET, "OE 18", "OE 20", "OE 21", "OE 34"], "F31 F33 F34 F47", f"`{n(opt)}`",
        f"the {k} row shows {n(opt)} options, with or without the word vested; {lower}", f"the {es} grant is sized in the disclosure schedule and tied to this holder by Carta's digest; Exhibit A of the board consent vests it 1/24th monthly with no cliff and the grants date from Nov 2023, so 24 months have run, with no termination notice", ["schedule", DIG[k], "consent"] + (["dm_size"] if k == "ENG-2440" else []) + (["contact_collins"] if k == "ENG-2447" else []) + [("notes", (2,))], f"With or without the word vested passes; {lower}.", f"The {k} row reads {n(opt)} options", "No holder sheet rows exist", dec=NODES["ADV"], dist="T1 owner-list merge", slots=[sl] if sl == "K8" else [], final=f"Holder sheet row {k}")


def add_option(k, sl=None):
    v = HOLD[k]["Options now"]
    add(f"sh_op_{k}", f"The Agent shows {nm(k)} ({k}) holding {n(v)} options on its holder sheet (with or without the word vested)", TIE_W(k), f"{k}.options", SP_SHEET, [OE_SHEET, "OE 12", "OE 35"], f"{CARTA_F[k]} F48" + TIE_F(k), f"`{n(v)}`",
        f"the {k} row shows {n(v)} options, with or without the word vested", TIE_WHY(k, f"Carta's notice for {D.ES[k]} gives the vested count"), [(f"carta_{k}", (1,))] + TIE_S(k), "With or without the word vested passes.", f"The {k} row reads {n(v)}", "No holder sheet rows exist", slots=[sl] if sl else [], final=f"Holder sheet row {k}")


for k, sl in [("ENG-2450", "P_live_ES-1"), ("ENG-2453", "P_live_ES-4"), ("ENG-2456", "P_live_ES-7"), ("ENG-2457", "P_live_ES-12"), ("ENG-2458", "P_live_ES-13")]:
    add_option(k, sl)

# -- sheet: last days
add("sh_ld_ENG-2452", "The Agent shows February 20, 2026 as the last day for Calvin Price (ENG-2452) on its holder sheet (any date form; January 24, 2026 given as the last day fails, and naming it as the earlier, superseded last day passes)", 3, "ENG-2452.lastday", SP_SHEET, [OE_SHEET, "OE 12", "OE 14", "OE 35"], "F14 F26 F48", "`2026-02-20`",
    "the ENG-2452 row gives February 20, 2026, in any date form; January 24, 2026 given as the last day fails, and naming it as the earlier, superseded last day passes", "Carta's first notice says Jan 24, and only Calvin's forward of the Jan 23 update moves it to Feb 20", ["calvin", ("carta_ENG-2452", (2,)), ("notes", (2,))], "Any date form passes; January 24, 2026 as the last day fails.", "The ENG-2452 row reads Feb 20, 2026", "No holder sheet rows exist", dec=NODES["EXT"], dist="T24 stale Carta notice", slots=["P_first"], final="Holder sheet row ENG-2452")


def add_lastday(k):
    add(f"sh_ld_{k}", f"The Agent shows {LASTD[k]} as the last day for {nm(k)} ({k}) on its holder sheet (any date form)", TIE_W(k), f"{k}.lastday", SP_SHEET, [OE_SHEET, "OE 12", "OE 35"], f"{CARTA_F[k]} F48" + TIE_F(k), f"`{LASTD[k]}`",
        f"the {k} row gives {LASTD[k]}, in any date form", TIE_WHY(k, "Carta's notice gives the last day"), [(f"carta_{k}", (2,))] + TIE_S(k), "Any date form passes.", f"The {k} row reads {LASTD[k]}", "No holder sheet rows exist", final=f"Holder sheet row {k}")


for k in ("ENG-2459", "ENG-2450", "ENG-2456", "ENG-2457", "ENG-2460"):
    add_lastday(k)

# -- sheet: labels, all 26
LBLFAIL = {"ENG-2440": "Closing fails", "ENG-2446": "Closing fails", "ENG-2447": "Closing fails", "ENG-2448": "Already told fails", "ENG-2452": "Nothing fails", "ENG-2457": "Last day fails", "ENG-2459": "Last day fails", "ENG-2463": "Last day fails"}
for k in D.ISSUES:
    lab = LABEL[k]
    w = LBL_W[k]
    fail = LBLFAIL.get(k)
    tail = f"in any letter case; {fail}" if fail else "in any letter case"
    t = f'The Agent labels {nm(k)} ({k}) "{lab}" on its holder sheet ({tail})'
    if k in NOTHING:
        last = {"ENG-2451": "Nov. 1, 2024", "ENG-2454": "Jan. 24, 2026", "ENG-2455": "July 16, 2025", "ENG-2461": "Jan. 24, 2026", "ENG-2462": "Jan. 28, 2026"}[k]
        why, srcs, fids, dec = (f"Carta's notice puts the last day, {last}, before the clock, and the notes say such a line holds nothing", [(f"carta_{k}", (2,)), ("notes", (2,))], f"{CARTA_F[k]} F4", "none")
    elif k in TOLDY:
        why, srcs, fids, m = TOLDY[k]
        dec = NODES[m]
    elif k in COVERED:
        why, srcs, fids, dec = ("Leonard's reply under his list sets the family rule and the Covered label, and only the 2023 family mail shows who handles the family's lines", ["family_rule", "covered_rule", "family"], "F9 F44", NODES["FAM"])
    elif k in CLOSING:
        why, srcs, fids = CLOSING[k]
        dec = "none"
    elif k in FULL:
        why, srcs, fids, m = FULL[k]
        dec = NODES[m]
    else:
        why, srcs, fids, dec = ("Leonard's Feb 11 letter reached this holder about the closing, and Carta's notice gives a last day still ahead" + (", under a legal name that Leonard's Oct 2024 option list ties to this issue's address" if k == "ENG-2460" else ""), [f"letter_{k}", (f"carta_{k}", (2,))] + TIE_S(k) + [("notes", (3,))], f"{CARTA_F[k]} F27 F4" + TIE_F(k), "none")
    surf = {"ENG-2459": "C_ES14", "ENG-2463": "C_ES18", "ENG-2457": "C_ES12", "ENG-2452": "C_ES3", "ENG-2440": "C_SEG", "ENG-2446": "C_NEB", "ENG-2448": "C_TOR", "ENG-2447": "C_COL", "ENG-2444": "F4", "ENG-2445": "F5", "ENG-2451": "P_lapsed_ES2", "ENG-2454": "P_lapsed_ES5", "ENG-2455": "P_lapsed_ES6", "ENG-2461": "P_lapsed_ES16", "ENG-2462": "P_FRED"}.get(k)
    add(f"sh_lb_{k}", t, w, f"{k}.label", SP_SHEET, [OE_SHEET, "OE 36"], f"{fids} F49", f'`{lab}`',
        f'the {k} row carries the label "{lab}", in any letter case' + (f"; {fail}" if fail else ""), why, srcs, f"The label from the notes, in any case; another label fails.", f'The {k} row reads "{lab}"', "No holder sheet rows exist", dec=dec, grp=f"labels {lab}", slots=[surf] if surf else [], final=f"Holder sheet row {k}")

# -- sheet: totals, counts, board, vote, sharing
TOT_TAIL = "as that one total, or as 164,114 options shown apart from 9,051,879 shares, the shares given as one figure or as 6,000,000 common plus 3,051,879 Series Seed; another figure given as today's option or share total fails, including the term sheet's 268,772 options"
add("sh_tot_all", f"The Agent shows total shares and options outstanding of 9,215,993 on its holder sheet ({TOT_TAIL})", 5, "sheet.totals", SP_SHEET, [OE_SHEET, "OE 22", "OE 34", "OE 35"], "F35 F47 F48 F10 F12 F31", "`9,215,993` `9,051,879` `164,114`",
    f"the holder sheet shows total shares and options outstanding of 9,215,993, {TOT_TAIL}", "Sunset asks for one line of totals; the shares come from the term sheet and Leonard's reply to go by the ledger, and the options add nine live Carta lines, one of them extended, and the four fully vested advisor grants",
    [("sunset", (1,)), ("term", (0, 1, 2)), "ledger_reply", "calvin", "schedule", ("notes", (8,))], "One combined total, or shares and options shown apart, pass; another figure given as today's option or share total fails.", "A totals line reads 9,215,993", "No holder sheet rows exist", dec=NODES["ADV"] + " " + NODES["EXT"], dist="T8 stale option count", slots=["K1", "P1"], final="Holder sheet totals")
add_stock("ENG-2443")
for lab, cnt, sl in [("Nothing", 5, None), ("Already told", 5, None), ("Covered", 2, None), ("Closing", 5, "C_FIRST"), ("Last day", 5, "C_DATE"), ("Closing and last day", 4, None)]:
    add(f"sh_cnt_{lab.replace(' ', '_')}", f'The Agent shows a count of {cnt} holders labeled "{lab}" on its holder sheet', 3, f"sheet.count.{lab}", SP_SHEET, [OE_SHEET, "OE 36"], "F10 F49", f"`{cnt}`",
        f'the holder sheet gives {cnt} for "{lab}"', "Sunset asks for a count by what each holder still needs to hear, and the count tallies the sheet's rows by label",
        [("sunset", (2,)), ("notes", (1,))], "Any layout showing that count against that label passes.", f'A counts line reads {lab}: {cnt}', "No holder sheet rows exist", dec=NODES["TOLD"], slots=[sl] if sl else [], final="Holder sheet counts")
add("sh_directors", "The Agent names Leonard Hayes and Robert as the directors in office on its holder sheet (first names pass; listing PERSON_4337_NAME, Griffin's partner, as a director fails)", 1, "sheet.directors", SP_SHEET, [OE_SHEET, "OE 25", "OE 37"], "F38 F50 F10", "`Leonard` `Robert`",
    "the holder sheet names Leonard Hayes and Robert as the directors in office, first names passing; listing PERSON_4337_NAME, Griffin's partner, as a director fails", "Robert's reply in the Board position thread states who remains on the board", [("sunset", (3,)), "board"], "First names pass; PERSON_4337_NAME as a director fails.", "A directors line reads Leonard Hayes, Robert", "No holder sheet rows exist", dec=NODES["BOARD"], slots=["B1"], final="Holder sheet")
add("sh_vote", "The Agent names Griffin (as Griffin, as its two funds together, or as GRIFFIN GAMING PARTNERS II, L.P.; naming only GRIFFIN GAMING PARTNERS II SIDE FUND, L.P. fails) as holding the preferred vote on its holder sheet", 3, "sheet.vote", SP_SHEET, [OE_SHEET, "OE 26", "OE 37"], "F37 F39 F50 F10", "`Griffin`",
    "the holder sheet names Griffin as holding the preferred vote, as Griffin, as its two funds together, or as GRIFFIN GAMING PARTNERS II, L.P.; naming only GRIFFIN GAMING PARTNERS II SIDE FUND, L.P. fails", "the certificate needs a majority of the preferred, and Griffin's two funds hold 2,746,693 of 3,051,879", [("sunset", (3,)), "cert", "griffin_split"], "Griffin, both funds or the larger fund pass; only the Side Fund fails.", "A line reads Preferred vote: Griffin", "No holder sheet rows exist", dec=NODES["BOARD"], slots=["B2"], final="Holder sheet")
add("sh_share_robert", "The Agent shares its holder sheet with robert@harmonygames.co", 1, "share.sheet.robert", SP_SHEET, ["OE 40"], "F4", "`robert@harmonygames.co`", "the holder sheet is shared with robert@harmonygames.co, at any role", "the notes say to share the sheet with Robert", [("notes", (10,))], "Any role passes.", "A share on the sheet to robert@harmonygames.co", "No share exists", slots=["D2"], final="Sharing on the holder sheet")
add("sh_share_arthur", "The Agent shares its holder sheet with arthur.blake@harmonygames.co", 1, "share.sheet.arthur", SP_SHEET, ["OE 41"], "F9", "`arthur.blake@harmonygames.co`", "the holder sheet is shared with arthur.blake@harmonygames.co, at any role", "Leonard's reply under his list says the sheet goes to Arthur as well as Robert", ["arthur_share"], "Any role passes.", "A share on the sheet to arthur.blake@harmonygames.co", "No share exists", slots=["D4"], final="Sharing on the holder sheet")

# -- holder notes
for k in NOTE_OE:
    oe = f"OE {NOTE_OE[k]}"
    em = D.EMAIL[k]
    tail = "a draft only to another address, or one that also goes to another holder address named in these draft rows, fails" if k == "ENG-2457" else "a draft that also goes to another holder address named in these draft rows fails"
    add(f"n_w_{k}", f"The Agent saves an unsent Gmail draft of its own for {nm(k)} ({k}), addressed to {em}, the address on that issue ({tail})", 1, f"{k}.note", SP_NOTES, [oe, "OE 2"], f"F2 F4", f"`{em}`",
        f"an unsent Gmail draft of its own for the {k} holder, addressed to {em}, with any subject and body; {tail}", "the notes send each note to the email on the holder's issue, as a draft", [f"issue_{k}", ("notes", (7, 11))], "A draft is the only passing form; sending it fails.", f"A Gmail draft to {em}", "No Gmail draft exists", slots=[], final=f"Gmail draft to {em}")

for k in list(CLOSING) + list(FULL):
    oe = f"OE {NOTE_OE[k]}"
    if k in CLOSING:
        why, srcs, fids = CLOSING[k]
        w, dec = 3, "none"
    else:
        why, srcs, fids, m = FULL[k]
        w, dec = 5, NODES[m]
        if k == "ENG-2452":
            w, dec, why = 3, "none", "no founder has written to Calvin about the closing, so the notes' rule (the closing if they have not been told) puts it in his note"
            srcs = list(srcs) + ["nomail_2452", ("notes", (3,))]
    srcs2 = list(srcs) + [("notes", (4,))]
    surf = {"ENG-2459": "N_Vincent", "ENG-2463": "N_Oliver"}.get(k)
    add(f"n_cl_{k}", f"The Agent tells {nm(k)} ({k}) in its draft note that the company is closing (closing, shutting down or winding down; any wording with that meaning)", w, f"{k}.note.closing", SP_NOTES, [oe, "OE 36"], f"{fids} F49", "`closing`",
        f"the draft note to the {k} holder says the company is closing, shutting down or winding down, in any wording with that meaning", why, srcs2, "Any wording that says the company is closing passes.", "A note saying Harmony Games is winding down", "No Gmail draft exists", dec=dec, slots=[surf] if surf else [], final=f"Gmail draft for {k}")

for k in NOTE_OE:
    oe = f"OE {NOTE_OE[k]}"
    t = HOLD[k]
    if k in ADV:
        shares = t["Shares held now"]
        add(f"n_h_sh_{k}", f"The Agent states in its draft note to {nm(k)} ({k}) that they hold {n(shares)} Series Seed shares (preferred, stock or shares wording; 31,536 as shares fails)", 5, f"{k}.note.shares", SP_NOTES, [oe, "OE 34"], "F3 F31 F33 F47", f"`{n(shares)}`",
            f"the draft note to the {k} holder says they hold {n(shares)} shares; 31,536 as shares fails", "the owner-list comment merges stock with the ES-10 grant, and only the Carta digests and the disclosure schedule separate them", [f"own_{k}", "schedule", DIG[k], ("notes", (5,))], "Preferred, stock or shares wording passes; 31,536 as shares fails.", f"A note saying {n(shares)} shares", "No Gmail draft exists", dec=NODES["ADV"], slots=["NC_Deepak"], final=f"Gmail draft for {k}")
        add(f"n_h_op_{k}", f"The Agent states in its draft note to {nm(k)} ({k}) that they hold {n(ADV[k][1])} options (with or without the word vested)", 5, f"{k}.note.options", SP_NOTES, [oe, "OE 21", "OE 34"], "F31 F33 F34 F47", f"`{n(ADV[k][1])}`",
            f"the draft note to the {k} holder says they hold {n(ADV[k][1])} options, with or without the word vested", "the grant is sized in the disclosure schedule and tied to this holder by Carta's digest; Exhibit A of the board consent vests it 1/24th monthly with no cliff and the grants date from Nov 2023, so 24 months have run", ["schedule", DIG[k], "consent", ("notes", (5,))], "With or without the word vested passes.", f"A note saying {n(ADV[k][1])} options", "No Gmail draft exists", dec=NODES["ADV"], final=f"Gmail draft for {k}")
    elif t["Shares held now"]:
        v = t["Shares held now"]
        sl = {"ENG-2441": "NC_Schaeppi", "ENG-2442": "NC_Bergmann", "ENG-2448": "NC_Tor"}.get(k)
        add(f"n_h_{k}", f"The Agent states in its draft note to {nm(k)} ({k}) that they hold {n(v)} Series Seed shares (preferred, stock or shares wording)", 1, f"{k}.note.shares", SP_NOTES, [oe, "OE 3", "OE 34"], "F3 F47", f"`{n(v)}`",
            f"the draft note to the {k} holder says they hold {n(v)} shares", "the owner-list comment on the issue gives the holding", [f"own_{k}", ("notes", (5,))], "Preferred, stock or shares wording passes.", f"A note saying {n(v)} shares", "No Gmail draft exists", slots=[sl] if sl else [], final=f"Gmail draft for {k}")
    else:
        v = t["Options now"]
        add(f"n_h_{k}", f"The Agent states in its draft note to {nm(k)} ({k}) that they hold {n(v)} options (with or without the word vested)", TIE_W(k), f"{k}.note.options", SP_NOTES, [oe, "OE 12", "OE 35"], f"{CARTA_F[k]} F48" + TIE_F(k), f"`{n(v)}`",
            f"the draft note to the {k} holder says they hold {n(v)} options, with or without the word vested", TIE_WHY(k, f"Carta's notice for {D.ES[k]} gives the vested count"), [(f"carta_{k}", (1,))] + TIE_S(k) + [("notes", (5,))], "With or without the word vested passes.", f"A note saying {n(v)} options", "No Gmail draft exists", final=f"Gmail draft for {k}")

for k, v in LASTD.items():
    oe = f"OE {NOTE_OE[k]}"
    if k == "ENG-2452":
        add(f"n_ld_{k}", f"The Agent gives February 20, 2026 as the last day to exercise in its draft note to Calvin Price ({k}) (any date form; January 24, 2026 given as the last day fails, and naming it as the earlier, superseded last day passes)", 3, f"{k}.note.lastday", SP_NOTES, [oe, "OE 14"], "F14 F26 F48", "`2026-02-20`",
            f"the draft note to the {k} holder gives February 20, 2026 as the last day to exercise, in any date form; January 24, 2026 given as the last day fails, and naming it as the earlier, superseded last day passes", "Carta's first notice says Jan 24, and only Calvin's forward of the Jan 23 update moves it", ["calvin", ("carta_ENG-2452", (2,)), ("notes", (4,))], "Any date form passes; January 24, 2026 as the last day fails.", "A note saying Feb 20, 2026", "No Gmail draft exists", dec=NODES["EXT"], slots=["N_Calvin"], final=f"Gmail draft for {k}")
    else:
        sl = {"ENG-2450": "ND_ES-1", "ENG-2453": "ND_ES-4", "ENG-2456": "ND_ES-7", "ENG-2460": "ND_ES-15", "ENG-2458": "ND_ES-13"}.get(k)
        add(f"n_ld_{k}", f"The Agent gives {v} as the last day to exercise in its draft note to {nm(k)} ({k}) (any date form)", TIE_W(k), f"{k}.note.lastday", SP_NOTES, [oe, "OE 12"], f"{CARTA_F[k]} F48" + TIE_F(k), f"`{v}`",
            f"the draft note to the {k} holder gives {v} as the last day to exercise, in any date form", TIE_WHY(k, "Carta's notice gives the last day"), [(f"carta_{k}", (2,))] + TIE_S(k) + [("notes", (4,))], "Any date form passes.", f"A note saying {v}", "No Gmail draft exists", slots=[sl] if sl else [], final=f"Gmail draft for {k}")

add("n_claire", "The Agent answers Claire Morgan's (or Claire's) Feb 12, 2026 question in its draft note to her (ENG-2453), whether she has to do anything about her equity, by telling her that she is not required to do anything (saying exercising is optional passes; any wording with that meaning)", 5, "ENG-2453.note.answer", SP_NOTES, ["OE 49", "OE 17"], "F30 F4", "`equity`",
    "the draft note to Claire Morgan answers whether she has to do anything about her equity by telling her that she is not required to do anything, saying exercising is optional passing, in any wording with that meaning", "her equity question sits in a Turkish group DM, unanswered beside Leonard's reply to her other question, and the notes want it answered in her note", ["claire_q", ("notes", (6,)), "letter_advice"], "Not required, or exercising is optional, passes; a note that only gives the date fails.", "A note saying she doesn't need to do anything", "No Gmail draft exists", dec=NODES["ASK"], dist="T17 unanswered question", slots=["Q1"], final="Gmail draft for ENG-2453")
for k, sl, wnote in [("ENG-2444", "F1", 5), ("ENG-2445", "F2", 5)]:
    add(f"n_fam_{k}", f"The Agent states in its draft note to [PERSON_NAME_52949] (ENG-2443) that {nm(k)} ({k}) holds 25,432 Series Seed shares (preferred, stock or shares wording)", 5, f"{k}.familynote", SP_NOTES, ["OE 44", "OE 31"], "F9 F44 F3 F47", "`25,432`",
        f"the draft note to the ENG-2443 holder says {nm(k)} holds 25,432 shares", "Leonard's reply says the family note says what each line holds, and the 2023 family mail shows who handles the family and which lines are theirs", ["family_rule", ("family", (0 if k == "ENG-2444" else 1,)), f"own_{k}"], "Preferred, stock or shares wording passes.", "A family note listing both holdings", "No Gmail draft exists", dec=NODES["FAM"], dist="T14 shared first name", slots=[sl], final="Gmail draft for ENG-2443")

# -- letter
LET = "its investor letter"
add("l_doc", "The Agent creates a document in Drive holding the investor letter to Harmony Games's holders (a Google Doc or another document file)", 1, "letter.doc", SP_SHEET, ["OE 56"], "F4 F8", "`letter`", "a new document in Drive holding the investor letter, a Google Doc or another document file, under any title", "the prompt names the investor letter as a deliverable, and the notes call for a letter", [("notes", (17,))], "Any title and document type pass.", "A Doc titled Investor update", "No letter exists", final="Letter")
add("l_folder", f"The Agent places {LET} in the Stockholder close-out folder (d_601064334a0b493022fe83; the Wind Down folder fails)", 1, "letter.folder", SP_SHEET, ["OE 57", "OE 5"], "F4 F5", "`d_601064334a0b493022fe83`", "the letter is in the folder d_601064334a0b493022fe83, created there or moved there; the Wind Down folder fails", "the prompt says the close-out folder and the notes name it over the Wind Down one", ["folder", ("notes", (12,))], "Created in place or moved there both pass.", "The letter sits in the folder", "No letter exists", slots=["D3"], final="Letter parent folder")
add("l_share", f"The Agent shares {LET} with robert@harmonygames.co", 1, "share.letter.robert", SP_SHEET, ["OE 58"], "F4", "`robert@harmonygames.co`", "the letter is shared with robert@harmonygames.co, at any role", "the notes say to share the letter with Robert", [("notes", (10,))], "Any role passes.", "A share on the letter to robert@harmonygames.co", "No share exists", final="Sharing on the letter")
add("l_why", f"The Agent gives as the reason for closing in {LET} that the company's metrics did not reach a level that supports a viable business (any wording with that meaning)", 1, "letter.why", SP_LETTER, ["OE 56", "OE 8"], "F8", "`metrics`", "the letter gives as the reason for closing that the company's metrics did not reach a level that supports a viable business, in any wording with that meaning", "the draft states it directly", [("draft", (4,))], "Any wording with that meaning passes.", "A letter with the draft's reason", "No letter exists", final="Letter body")
add("l_insolvent", f"The Agent states in {LET} that the company is insolvent or out of cash (insolvent, no cash reserves or out of funds; only the draft's less than a month of runway fails)", 3, "letter.insolvent", SP_LETTER, ["OE 56", "OE 8"], "F8", "`insolvent`", "the letter says the company is insolvent, has no cash reserves or is out of funds; only the draft's less than a month of runway fails", "the draft's runway line is overtaken by Leonard's Feb 12 note in the channel", [("draft", (0,)), "insolvent"], "Insolvent, no cash or out of funds passes.", "A letter saying the company is insolvent", "No letter exists", final="Letter body")
add("l_sunset", f"The Agent states in {LET} that Sunset has been engaged, or the wind-down agreement with Sunset signed, to run the wind-down or dissolution (saying it is still only being prepared fails)", 3, "letter.sunset", SP_LETTER, ["OE 56", "OE 8", "OE 25"], "F8 F38", "`Sunset`", "the letter says Sunset has been engaged, or the wind-down agreement with Sunset signed, to run the wind-down or dissolution; saying it is still only being prepared fails", "the draft says the wind-down is being initiated, and a later post has the agreement signed", [("draft", (1,)), "signed", "outline_board"], "Engaged or signed passes; still only being prepared fails.", "A letter naming Sunset as engaged", "No letter exists", slots=["L2"], final="Letter body")
add("l_board", f"The Agent states in {LET} that the board is now Leonard Hayes and Robert (first names pass; a letter still listing PERSON_4337_NAME, Griffin's partner, as a director fails)", 1, "letter.board", SP_LETTER, ["OE 56", "OE 25"], "F38", "`Robert`", "the letter says the board is now Leonard Hayes and Robert, first names passing; a letter still listing PERSON_4337_NAME, Griffin's partner, as a director fails", "Robert's reply in the Board position thread states who remains, and the outline has a part on the board", ["board", "outline_board"], "First names pass; PERSON_4337_NAME as a director fails.", "A letter saying the board is Leonard and Robert", "No letter exists", dec=NODES["BOARD"], slots=["L6"], final="Letter body")
add_stock("ENG-2444")
add("l_dist", f"The Agent states in {LET} that holders should not expect a distribution (no money left for stockholders or no distribution expected; any wording with that meaning)", 3, "letter.distribution", SP_LETTER, ["OE 56", "OE 15"], "F7 F27 F8", "`distribution`", "the letter says holders should not expect a distribution, in any wording with that meaning", "the outline has a Distributions part, and the Feb 12 note says the company is insolvent", ["outline_means", "insolvent", "letter_advice"], "Any wording with that meaning passes.", "A letter saying no distribution is expected", "No letter exists", slots=["L3"], final="Letter body")
add("l_tax", f"The Agent tells holders in {LET} that the tax papers are still to come from the wind-down (tax documents, write-off paperwork or final returns; any wording with that meaning)", 3, "letter.tax", SP_LETTER, ["OE 56", "OE 8"], "F7 F8", "`tax`", "the letter says the tax papers, write-off paperwork or final returns are still to come from the wind-down, in any wording with that meaning", "the outline has a tax papers part, and the draft still has tax requirements to meet", ["outline_means", ("draft", (6,))], "Any wording with that meaning passes.", "A letter saying tax documents will follow", "No letter exists", slots=["L4"], final="Letter body")
add("l_options", f"The Agent tells holders in {LET} that exercising options is not recommended (any wording with that meaning)", 3, "letter.options", SP_LETTER, ["OE 56", "OE 15"], "F7 F27", "`exercise`", "the letter says exercising options is not recommended, in any wording with that meaning", "the outline has a part on options, and the Feb 11 letters give this advice because the shares are expected to have no value", ["outline_means", "letter_advice"], "Any wording with that meaning passes.", "A letter saying exercising is not recommended", "No letter exists", slots=["L8"], final="Letter body")
add("l_license", f"The Agent states in {LET} that the company's game-data agreement is a license (a data license or licensing agreement, with or without saying it is not a sale; saying the data was sold outright fails)", 3, "letter.license", SP_LETTER, ["OE 56", "OE 8"], "F8", "`license`", "the letter says the company's game-data agreement is a license, a data license or licensing agreement, with or without saying it is not a sale; saying the data was sold outright fails", "the draft says the IP is still to be evaluated for sale or other disposition, and later posts settle a licensing deal", [("draft", (2,)), ("license", (0,))], "A license in any wording passes; saying the data was sold outright fails.", "A letter saying the data was licensed", "No letter exists", slots=["L5"], final="Letter body")
add("l_ip", f"The Agent states in {LET} that the company keeps ownership of its IP (any wording with that meaning)", 3, "letter.ip", SP_LETTER, ["OE 56", "OE 8"], "F8", "`IP`", "the letter says the company keeps ownership of its IP, in any wording with that meaning", "the draft leaves the IP undecided, and Leonard's later post says the licensing keeps it", [("draft", (2,)), ("license", (1,))], "Any wording with that meaning passes.", "A letter saying the IP stays with the company", "No letter exists", final="Letter body")
add("l_team", f"The Agent states in {LET} that the team's termination letters have gone out or the team has been notified (any wording with that meaning)", 3, "letter.team", SP_LETTER, ["OE 56", "OE 8"], "F8", "`termination`", "the letter says the team's termination letters have gone out or the team has been notified, in any wording with that meaning", "the draft still lists employee and contractor obligations as a priority, and Leonard's later post says the termination letters are sent", [("draft", (3,)), "sent"], "Any wording with that meaning passes.", "A letter saying the team was notified Feb 11", "No letter exists", final="Letter body")
add("l_games", f"The Agent states in {LET} that the games are being shut down or wound down (any wording with that meaning)", 1, "letter.games", SP_LETTER, ["OE 56", "OE 7", "OE 8"], "F7 F8", "`games`", "the letter says the games are being shut down or wound down, in any wording with that meaning", "the outline has a part on what happens to the games, and the draft says it", ["outline_games", ("draft", (7,))], "Any wording with that meaning passes.", "A letter saying the games are being wound down", "No letter exists", final="Letter body")
add("l_thanks", f"The Agent closes {LET} with thanks to the holders (a thank-you in any wording)", 1, "letter.thanks", SP_LETTER, ["OE 56", "OE 7"], "F7 F8", "`thank`", "the letter ends with thanks to the holders, in any wording", "the outline's last part is Thank you", ["outline_thanks"], "Any wording passes.", "A letter that ends by thanking investors", "No letter exists", final="Letter body")

# -- Linear: one row per write
for k in D.ISSUES:
    st = HOLD[k]["State"]
    oe = oe_for(rf"^OE (\d+)  Move {k} to ")
    live_only = k in LASTD and k != "ENG-2452"
    if k in NOTHING:
        w, why, srcs, fids, dec = 1, "Carta's notice puts the last day before the clock, so the project rule makes the line Canceled", [(f"carta_{k}", (2,)), ("project", (2,))], f"{CARTA_F[k]} F1", "none"
    elif live_only:
        w, why, srcs, fids, dec = TIE_W(k), ("Carta's notice, under a legal name that Leonard's Oct 2024 option list ties to this issue's address, shows a last day still ahead, so the project rule makes the line Todo" if k == "ENG-2460" else "Carta's notice shows a last day still ahead, so a note is owed and the project rule makes the line Todo"), [(f"carta_{k}", (2,))] + TIE_S(k) + [("project", (2,))], f"{CARTA_F[k]} F1" + TIE_F(k), "none"
    elif k == "ENG-2452":
        w, why, srcs, fids, dec = 3, "Carta's first notice would make the line Canceled, and only Calvin's forward of the Jan 23 update keeps it live and Todo", ["calvin", ("project", (2,))], "F14 F26 F1", NODES["EXT"]
    elif k in TOLDY:
        why, srcs, fids, m = TOLDY[k]
        w, dec = LBL_W[k], NODES[m]
        srcs = list(srcs) + [("project", (2,))]
    elif k in COVERED:
        w, why, srcs, fids, dec = 5, "the family rule and the 2023 family mail make this a Covered line with no note of its own, so the project rule makes it Done", ["family_rule", "family", ("project", (2,))], "F9 F44 F1", NODES["FAM"]
    else:
        why, srcs, fids = CLOSING[k]
        w, dec = 3, "none"
        srcs = list(srcs) + [("project", (2,))]
    surf = {"ENG-2452": "LS_ES-3", "ENG-2455": "LS_ES-6", "ENG-2457": "LS_ES-12"}.get(k)
    add(f"st_{k}", f"The Agent moves {k} ({nm(k)}) to {st}", w, f"{k}.state", SP_LINEAR, [oe, "OE 36"], f"{fids} F49", f"`{st}`", f"the issue {k} ends in the state {st}", why, srcs, f"Only {st} passes.", f"{k} state {st}", f"{k} stays in Backlog", dec=dec, slots=[surf] if surf else [], final=f"Linear issue {k}")

REASON = {}
for k in NOTHING:
    REASON[k] = ("the line holds nothing (holds nothing, lapsed or expired; any wording with that meaning)", 1, "Carta's notice puts the last day before the clock", [(f"carta_{k}", (2,)), ("notes", (2,)), ("project", (3,))], f"{CARTA_F[k]} F1", "none")
for k, (why, srcs, fids, m) in TOLDY.items():
    REASON[k] = ("the holder has already been told about the closing (any wording with that meaning)", LBL_W[k], why, list(srcs) + [("project", (3,))], fids, NODES[m])
for k in COVERED:
    REASON[k] = ("the note to [PERSON_NAME_52949] on ENG-2443 covers this family line (the family note or the note to the brother who handles it; any wording with that meaning)", 5, "the family rule and the 2023 family mail make the ENG-2443 holder the one who handles the family's lines", ["family_rule", "family", "wire", ("project", (3,))], "F9 F44 F1", NODES["FAM"])
for k, (reason, w, why, srcs, fids, dec) in REASON.items():
    oe = oe_for(rf"^OE (\d+)  Comment on {k} ")
    surf = {"ENG-2440": "LC_Seg", "ENG-2447": "LC_Col", "ENG-2446": "LC_Neb", "ENG-2451": "LC_ES-2", "ENG-2454": "LC_ES-5", "ENG-2461": "LC_ES-16", "ENG-2444": "F3"}.get(k)
    add(f"cm_{k}", f"The Agent comments on {k} ({nm(k)}) that {reason}", w, f"{k}.reason", SP_LINEAR, [oe, "OE 36"], f"{fids} F49", "`reason`", f"a comment on {k} saying {reason}", why, srcs, "Any wording with that meaning passes; a comment giving another reason fails.", f"A comment on {k} giving that reason", f"No comment on {k}", dec=dec, slots=[surf] if surf else [], final=f"Linear comments on {k}")

# -- KPMG
K_ALL = "PERSON_3088_EMAIL, PERSON_4416_EMAIL, PERSON_2322_EMAIL and PERSON_2847_EMAIL"
KP = "its answer to KPMG"
add("k_send", f"The Agent sends {KP} in the thread of KPMG's GRIFFIN GAMING PARTNERS 2025 Audit Request (leonard.hayes@harmonygames.co/1857029474983245439) to {K_ALL} (as a reply to all, or with those four addresses on To and Cc)", 1, "kpmg.recipients", SP_KPMG, ["OE 97", "OE 11"], "F11", "`PERSON_3088_EMAIL` `PERSON_4416_EMAIL` `PERSON_2322_EMAIL` `PERSON_2847_EMAIL`", f"a sent message in that thread as a reply to all, or with {K_ALL} on To and Cc", "KPMG asks for a reply to all recipients, and the project repeats it", [("kpmg", (4,)), ("project", (1,))], "Reply to all, or the four addresses set by hand, pass; a draft fails.", "A reply to all on KPMG's message", "No message sent in the KPMG thread", slots=["A8"], final="Sent reply in thread 1857029474983245439")
add("k_common", f"The Agent reports 6,000,000 shares of common stock outstanding as of December 31, 2025 in {KP}", 1, "kpmg.common", SP_KPMG, ["OE 97", "OE 22"], "F35", "`6,000,000`", "the KPMG answer gives 6,000,000 shares of common stock outstanding as of December 31, 2025", "the term sheet states the founder common", [("term", (0,)), ("kpmg", (0,))], "Common or founder common wording passes.", "An answer saying Common: 6,000,000", "No message sent in the KPMG thread", slots=["A9"], final="KPMG answer")
add("k_seed", f"The Agent reports 3,051,879 Series Seed shares outstanding as of December 31, 2025 in {KP} (3,051,881 or 3,051,882 fails)", 3, "kpmg.seed", SP_KPMG, ["OE 97", "OE 22", "OE 34"], "F35 F47", "`3,051,879`", "the KPMG answer gives 3,051,879 Series Seed shares outstanding as of December 31, 2025; 3,051,881 or 3,051,882 fails", "the figure is in the term sheet, and Leonard's reply says to go by the ledger over the figures a couple of shares off", [("term", (1,)), "ledger_reply", ("kpmg", (0,))], "Series Seed or preferred wording passes; 3,051,881 or 3,051,882 fails.", "An answer saying Series Seed: 3,051,879", "No message sent in the KPMG thread", dec=NODES["ADV"], dist="T9 seed figures off by a couple of shares", final="KPMG answer")
for nm2, val, sl in [("GRIFFIN GAMING PARTNERS II, L.P. (or [ORGANIZATION_NAME_0151] II, L.P., as the purchaser schedule shows it)", 2662255, "A3"), ("GRIFFIN GAMING PARTNERS II SIDE FUND, L.P. (or [ORG_NAME_0153] II Side Fund, L.P., as the purchaser schedule shows it)", 84438, None)]:
    add(f"k_fund_{val}", f"The Agent reports that {nm2} holds {n(val)} shares in {KP}", 3, f"kpmg.fund.{val}", SP_KPMG, ["OE 97", "OE 24"], "F37", f"`{n(val)}`", f"the KPMG answer gives {nm2} {n(val)} shares", "the purchaser schedule gives the split, and the owner-list comments only have the merged figure", ["griffin_split", "griffin_names", ("kpmg", (0,))], "Fund name in any letter case, or the name the schedule shows, passes.", f"An answer saying {n(val)} for that fund", "No message sent in the KPMG thread", slots=[sl] if sl else [], final="KPMG answer")
add("k_total", f"The Agent reports 243,757 options outstanding as of December 31, 2025 in {KP} (164,114 or 268,772 fails)", 5, "kpmg.options_total", SP_KPMG, ["OE 97", "OE 38"], "F51 F12 F31 F11", "`243,757`", "the KPMG answer gives 243,757 options as of December 31, 2025; 164,114 or 268,772 fails", "the total applies KPMG's clarification to each Carta effective date across 16 lines, with the advisor grants from the disclosure schedule", [("kpmg2", (0,)), ("kpmg", (1,)), "schedule", ("carta_ENG-2451", (2,)), ("carta_ENG-2455", (2,))], "That total passes; today's 164,114 or the term sheet's 268,772 fails.", "An answer saying 243,757", "No message sent in the KPMG thread", dec=NODES["ASOF"] + " " + NODES["ADV"], dist="T12 today's count", slots=["A1"], final="KPMG answer")
add("k_combined", f"The Agent reports 9,295,636 as one figure for shares outstanding plus options outstanding as of December 31, 2025, in {KP}", 3, "kpmg.combined", SP_KPMG, ["OE 97", "OE 38"], "F51 F35", "`9,295,636`", "the KPMG answer gives 9,295,636 as one figure for shares outstanding plus options outstanding as of December 31, 2025", "the figure adds shares outstanding to the Dec 31 option count, which another row charges", [("kpmg", (2,)), ("term", (0, 1))], "That figure passes.", "An answer saying 9,295,636", "No message sent in the KPMG thread", dec=NODES["ASOF"], slots=["A2"], final="KPMG answer")
add_stock("ENG-2445")
KBY = "by holder name, with or without the ES number"
for es, k, val, fail, w, sl, srcs, fids, why, who in [
    ("ES-7", "ENG-2456", 22889, "12,875 fails", 3, "AL_ES-7", ["carta_ENG-2456", ("kpmg2", (0,))], "F18 F51", "the Jan 30, 2026 termination comes after the as-of date, so KPMG's rule counts the full grant", None),
    ("ES-15", "ENG-2460", 3391, "10,173 fails", 3, "AL_ES-15", ["carta_ENG-2460", ("kpmg2", (0,)), "es15_tie", ("digest_oct23", (0, 1)), "digest_es15", "mail_es15", "from_es15"], "F22 F29 F51", "the Dec 31, 2025 termination falls on the as-of date, so KPMG's rule counts only what had vested", "Brian Foster, Brian, [PERSON_NAME_0092], [PERSON_NAME_0093], [PERSON_NAME_2769] [PERSON_NAME_0093], Ömer [PERSON_NAME_0093], Omer [PERSON_NAME_0092] [PERSON_NAME_0008] or [PERSON_NAME_45917] [PERSON_NAME_0093], the names ENG-2460, Carta and Leonard's mail give the holder"),
    ("ES-16", "ENG-2461", 10384, "0 or a blank fails", 3, "AL_ES-16", ["carta_ENG-2461", ("kpmg2", (0,)), "issue_ENG-2461", "notice_es16", "list_es16", "mail_es16", "from_es16"], "F23 F51", "the line lapsed in January 2026, after the as-of date, so it still counts what had vested", "[PERSON_NAME_2768] [PERSON_NAME_0011], EMPLOYEE_0032 [PERSON_NAME_0011], PERSON_0031_NAME, [PERSON_NAME_0120] or [PERSON_NAME_0121], the names Carta and Leonard's mail give the holder, or Cameron, from the ENG-2461 address cameron@harmonygames.co"),
    ("ES-17", "ENG-2462", 34439, "34,409 fails", 3, None, ["carta_ENG-2462", "letter_es17", ("notes", (2,)), ("kpmg2", (0,)), ("digest_oct23", (2, 3)), "from_es17"], "F24 F51", "Carta's notice gives 34,439 and the notes make Carta the record over the letter's figure", "[PERSON_NAME_0038], [PERSON_NAME_0036] [PERSON_NAME_0005], [PERSON_NAME_0036] or Ryan, the names ENG-2462, Carta and Leonard's mail give the holder"),
    ("ES-9", "ENG-2447", 61038, "0 fails", 5, None, ["schedule", ("digest2", (0, 1)), "contact_collins", ("kpmg2", (0,))], "F31 F33 F51", "the grant is sized in the disclosure schedule and tied to the holder by Carta's digest, and with no termination by the as-of date KPMG's rule counts the full grant", None),
]:
    who = who or nm(k)
    add(f"k_line_{es}", f"The Agent reports {es} ({who}) at {n(val)} options as of December 31, 2025 in {KP} ({KBY}; {fail})", w, f"kpmg.line.{es}", SP_KPMG, ["OE 97", "OE 38"], fids, f"`{n(val)}`", f"the KPMG answer gives the {es} line, under {who}, {n(val)} options as of December 31, 2025, {KBY}; {fail}", why, srcs, f"Holder name, with or without the ES number, passes; {fail}.", f"An answer listing {es}: {n(val)}", "No message sent in the KPMG thread", grp="kpmg option lines", dec=NODES["ASOF"], slots=[sl] if sl else [], final="KPMG answer")
add("k_financing", f"The Agent reports in {KP} that there has been no new financing since December 31, 2025 (any wording with that meaning)", 3, "kpmg.financing", SP_KPMG, ["OE 97", "OE 23"], "F36 F11", "`financing`", "the KPMG answer says no new financing came in after December 31, 2025, in any wording with that meaning", "the Jan 22 reset never closed, and the Feb 9 wind-down request says the company is out of funds", ["recap", ("kpmg2", (1,)), ("kpmg", (3,))], "Any wording with that meaning passes.", "An answer saying no new financing", "No message sent in the KPMG thread", slots=["A7"], final="KPMG answer")
add("k_wind", f"The Agent reports in {KP} that the company is winding down (closing, dissolving or shutting down; any wording with that meaning)", 1, "kpmg.winding", SP_KPMG, ["OE 97", "OE 8"], "F11 F8", "`winding`", "the KPMG answer says the company is winding down, closing, dissolving or shutting down, in any wording with that meaning", "KPMG asks for any significant event, and the company's closing is the premise of the task", [("kpmg", (3,)), ("kpmg2", (2,)), "signed"], "Any wording with that meaning passes.", "An answer saying the company is winding down", "No message sent in the KPMG thread", slots=["A5"], final="KPMG answer")

# -- Griffin and the thread reply
add("g_send", "The Agent sends the heads-up to Griffin in the Board position thread (leonard.hayes@harmonygames.co/1856958794180374704) so that it reaches PERSON_4337_EMAIL and PERSON_2847_EMAIL (by a reply to all or by addressing both; a draft fails)", 1, "griffin.recipients", SP_GRIFFIN, ["OE 98", "OE 25"], "F38 F4", "`PERSON_4337_EMAIL` `PERSON_2847_EMAIL`", "a sent message in the Board position thread that reaches PERSON_4337_EMAIL and PERSON_2847_EMAIL, by a reply to all or by addressing both; a draft fails", "the notes name the partner's own Board position mail and a reply to all", [("notes", (13,)), "board"], "A reply to all or addressing both passes; a draft fails.", "A reply to all on the partner's Feb 12 mail", "No message sent in the Board position thread", slots=["G1"], final="Sent reply in the Board position thread")
add("g_vote", "The Agent asks Griffin's partner in its heads-up to Griffin for Griffin's vote as preferred holders on the dissolution (vote or consent; any wording with that meaning)", 1, "griffin.vote", SP_GRIFFIN, ["OE 98"], "F4", "`vote`", "the heads-up asks Griffin's partner for Griffin's vote or consent as preferred holders on the dissolution, in any wording with that meaning", "the notes spell out what the heads-up asks", [("notes", (13,))], "Vote or consent wording passes.", "A heads-up asking for the preferred vote", "No heads-up exists", slots=["G2"], final="Griffin heads-up")
add("r_thread", f"The Agent replies under Leonard's list in #winddown (message {WD}/{LIST_TS}), as a reply in that thread", 1, "reply.thread", SP_REPLY, ["OE 99", "OE 8"], "F8 F4", f"`{WD}/{LIST_TS}`", f"a sent reply in the thread of {WD}/{LIST_TS}", "the notes name the reply under the list", [("notes", (14,)), "list"], "Only a reply in that thread passes.", "A reply in the thread", "No message in #winddown", slots=["D5"], final="Slack thread reply")
add("r_first", "The Agent says in its reply under Leonard's list in #winddown that Calvin Price (or Calvin) is the holder whose note goes first ([PERSON_NAME_0051] going first fails)", 3, "reply.first", SP_REPLY, ["OE 99", "OE 37", "OE 14"], "F14 F26 F50", "`Calvin`", "the reply says Calvin Price, or Calvin, is the holder whose note goes first; [PERSON_NAME_0051] going first fails", "the notes put the earliest last day first, and only Calvin's forward of the Jan 23 update makes Feb 20 the earliest", [("notes", (15, 14)), "calvin"], "Calvin Price or Calvin passes; [PERSON_NAME_0051] going first fails.", "A reply saying Calvin Price goes first", "No reply exists", dec=NODES["EXT"], dist="T24 stale Carta notice", slots=["D6"], final="Slack thread reply")

# -- ordering (Process): one row for the sheet coming first
_first_other = "a holder note draft, the investor letter, a Linear state change or comment, the answer to KPMG, the heads-up to Griffin or the #winddown reply"
add("o_first", f"The Agent writes the holder rows to its holder sheet before its first other write ({_first_other}); later corrections to the sheet pass", 1, "order.sheet_first", SP_RULES, [OE_SHEET, "OE 42", "OE 56", "OE 59", "OE 60", "OE 97", "OE 98", "OE 99"], "F1 F4", "`before`", f"the holder rows are written to the holder sheet before the first other write ({_first_other}); later corrections to the sheet pass", "the records make the sheet come first, and no final state can show the order", [("project", (1, 2)), ("notes", (13, 14, 16))], "A later edit to the sheet is allowed once the holder rows came first.", "The sheet write is the earlier call", "No sheet write exists", cat="Process", final="Order of writes")

# -- sheet: the rest of the option and last-day columns
for k in ("ENG-2452", "ENG-2459", "ENG-2460", "ENG-2463"):
    add_option(k, {"ENG-2452": "P_live_ES-3", "ENG-2459": "P_live_ES-14", "ENG-2460": "P_live_ES-15", "ENG-2463": "P_live_ES-18"}[k])
for k in ("ENG-2453", "ENG-2458", "ENG-2463"):
    add_lastday(k)

# ---- checks -----------------------------------------------------------------------------------------------------------
for r in R:
    for f in ("t", "just", "ev"):
        m = BAD.search(r[f])
        assert not m, (r["tag"], f, m.group(0), r[f][:200])
    assert r["t"].startswith("The Agent "), r["t"]
    assert r["span"] in PROMPT
tags = [r["tag"] for r in R]
assert len(tags) == len(set(tags)), [t for t, c in Counter(tags).items() if c > 1]
titles = Counter(r["t"] for r in R)
assert max(titles.values()) == 1, [t for t, c in titles.items() if c > 1]
dup = [k for k, v in Counter(r["fact"] for r in R).items() if v >= 3]
assert not dup, dup

# -- the draft sheet's other old rows, one row each (appended so earlier row numbers stay put)
for tag, holder, fig in [("old_ENG-2462", "[PERSON_NAME_0038]", "127,162")]:
    note(tag, f"Sheet1 of the spreadsheet {SHEET_ID}", holder, fig, "copied from the Nov 2024 list")
    add_old(tag, holder, fig, f"ENG-2462's one row by writing on it its ENG id or {OLD_LABELS}",
            f"{OLD_CLEAR}; or the row itself becomes ENG-2462's one row on the sheet (whether its label is right is graded by the label row for ENG-2462; what it shows as held today is not graded here). {OLD_FAIL}; or kept beside a second row for that issue", tag)
for k, holder, fig in [("ENG-2447", "[PERSON_NAME_11362]", "86,470"), ("ENG-2440", "[PERSON_NAME_0089] [PERSON_NAME_25152]", "81,383"), ("ENG-2448", "TOR Capital Limited", "50,865"), ("ENG-2446", "PERSON_3941_NAME [PERSON_NAME_0127]", "31,536"), ("ENG-2449", "PERSON_1287_NAME", "31,536")]:
    tag = f"old_{k}"
    note(tag, f"Sheet1 of the spreadsheet {SHEET_ID}", holder, fig, "copied from the Nov 2024 list")
    add_old(tag, holder, fig, f"{k}'s one row by writing on it its ENG id or {OLD_LABELS}",
            f"{OLD_CLEAR}; or the row itself becomes that issue's one row on the sheet (whether its label and figure are right is graded by the holder's own label and share rows). {OLD_FAIL}; or kept beside a second row for that issue", tag)

# -- ENG-2462's holding today has no figure row of its own; one row decides it from a named cell
HELD_RULE = "judged only on that row's first filled cell among, in order, held today (any heading for what it holds or has now; the options one if split), vested, options, granted and shares: 0, N/A, lapsed, expired or other wording that it holds nothing now, with no option or share count there but 127,162 once granted or 34,439 once vested (34,409 fails); all blank passes; no such cell, or terminated alone, fails"
HELD_WHO = "[PERSON_NAME_0038] (ENG-2462, or [PERSON_NAME_0036] [PERSON_NAME_0005], [PERSON_NAME_0036] or Ryan)"
add("sh_held_ENG-2462", f"The Agent shows {HELD_WHO} holding nothing today on a row of its holder sheet (one such row is enough; a leftover draft row is not graded here), {HELD_RULE}", 1, "ENG-2462.held_today", SP_SHEET, [OE_SHEET, "OE 12", "OE 35"], "F24 F48", "`127,162` `34,439`",
    f"a row of the holder sheet for {HELD_WHO} shows the holder holding nothing today (one such row is enough; a leftover draft row is not graded here), {HELD_RULE}",
    "Carta's notice puts the last day, Jan. 28, 2026, before the clock, the notes say such a line holds nothing, and Sunset's list asks what each holder has today", [("sunset", (0,)), ("project", (0,)), ("notes", (2,)), "carta_ENG-2462", "letter_es17", ("digest_oct23", (3,)), "from_es17"], "Any wording that it holds nothing now passes on the deciding cell; other cells are not graded.", "A held-today cell reading Nothing on the ENG-2462 row", "No holder sheet rows exist", final="Holder sheet row ENG-2462")

# ---- outputs ----------------------------------------------------------------------------------------------------------
rubric = [{"title": r["t"], "category": r["cat"], "weight": r["w"], "justification": r["just"], "evidence": r["ev"]} for r in R]
out = os.path.join(L.TI, "09_Rubrics.json")
open(out, "w", encoding="utf-8").write(json.dumps(rubric, indent=1, ensure_ascii=False) + "\n")


def ahash(p):
    return subprocess.run([sys.executable, os.path.join(L.TA, "tools/stage_gate.py"), "--artifact-hash", p], capture_output=True, text=True, cwd=WS).stdout.strip()


ep = os.path.join(L.WF, "00_V3_Authoring_Evidence.json")
ev = json.load(open(ep, encoding="utf-8"))
ev["rubric_hash"] = ahash(out)
ev["prompt_hash"] = ahash(os.path.join(L.TI, "04_Prompt.txt"))
ev["rubric_rows"] = [{"criterion_id": f"C{i + 1}", "fact_id": r["fact"], "prompt_span": r["span"], "accepted_outcomes": r["acc"], "alternatives_review": r["alt"], "source_records": r["srcs"]} for i, r in enumerate(R)]
json.dump(ev, open(ep, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump([{k: v for k, v in r.items() if k != "srcs"} for r in R], open(os.path.join(HERE, "rows.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
tw = sum(r["w"] for r in R)
print(len(R), "rows; weight", tw, "; bands", {b: sum(1 for r in R if r["w"] == b) for b in (5, 3, 1)}, "; Process", sum(1 for r in R if r["cat"] == "Process"), "; hash", ev["rubric_hash"])

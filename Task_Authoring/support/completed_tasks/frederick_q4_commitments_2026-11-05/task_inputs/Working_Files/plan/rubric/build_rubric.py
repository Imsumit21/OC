#!/usr/bin/env python3
"""Build 09_Rubrics.json, the V3 rubric_rows evidence and rows.json (input to build_plan.py) for
frederick_q4_commitments (rev4). Every source value is read from its record here: seeded rows via
base_check.parse_sql (never executed), base records via hg.py get-many. Run from anywhere."""
import json
import subprocess
import sys
from pathlib import Path

WS = Path(__file__).resolve().parents[5]
TI = WS / "Task_Authoring/task_inputs"
WF = TI / "Working_Files"
sys.path.insert(0, str(WS / "Task_Authoring/tools"))
from base_check import parse_sql  # noqa: E402

SQL = parse_sql((TI / "01_Universe_Inject.sql").read_text())
CTX = json.loads((WF / "00_Task_Context.json").read_text())
ROOTS = CTX["source"]["paths"]
IDS = json.loads((WF / "plan/sql_ids.json").read_text())["ids"]
TRUTH = json.loads((WF / "solver/truth.json").read_text())
FID = json.loads((WF / "plan/oe_ledger_ids.json").read_text())["fid"]
NUM = json.loads((WF / "plan/oe_events_map.json").read_text())["num"]
FRED = "frederick.stone@harmonygames.co"
REVIEWER = "Claude (model-drafted under GEN_EXECUTION §2; for the human author's review)"
SNAP = ("The synth-cut snapshot is cut at the freeze (2025-09-30 23:59:59 PT); the record's own last change is before "
        "the freeze, so its exported content is its state at the freeze. ")


def sql_row(table, identity):
    rows = [x["row"] for x in SQL if x["table"] == table and x["op"] == "insert"
            and all(x["row"].get(k) == v for k, v in identity.items())]
    assert len(rows) == 1, (table, identity, len(rows))
    return rows[0]


def get_json(service, rel, pointer):
    req = {"items": [{"service": service, "file": rel, "id": "v", "pointer": pointer, "max_chars": 65536}]}
    out = subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/hg.py"), "search", "get-many", "--request", "-",
                          "--task-dir", str(TI)], input=json.dumps(req), capture_output=True, text=True, cwd=WS)
    item = json.loads(out.stdout)["items"]["v"]
    assert item.get("encoding") == "rendered-json" and item.get("truncated") is False, (rel, pointer, item)
    return json.loads(item["text"])


def path(*hops):
    return [{"service": s, "id": i} for s, i in hops]


def review(ids, why):
    return {"reviewer": REVIEWER, "rationale": why, "evidence_ids": ids}


def S_sql(service, rid, table, identity, column, rec_col, hops, why, semantics="fact", mutable=False, rev=None):
    row = sql_row(table, identity)
    src = {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table, "identity": identity,
           "column": column, "source_value": row[column], "evidence_path": path(*hops), "reachability_rationale": why,
           "temporal_evidence": {"value_semantics": semantics, "mutable_state": mutable, "recorded_at_column": rec_col,
                                 "rationale": f"Seeded {table} row; {rec_col} = {row[rec_col]} (before the freeze)."}}
    if mutable:
        src["temporal_evidence"]["state_at_freeze_review"] = rev
    return src


def S_json(service, rid, rel, pointer, rec_pointer, hops, why, mutable=False, rev=None):
    value = get_json(service, rel, pointer)
    recorded = get_json(service, rel, rec_pointer)
    src = {"service": service, "id": rid, "source_file": str((Path(ROOTS[service]) / rel).relative_to(WS)), "pointer": pointer,
           "source_value": value, "evidence_path": path(*hops), "reachability_rationale": why,
           "temporal_evidence": {"value_semantics": "fact", "mutable_state": mutable, "recorded_at_pointer": rec_pointer,
                                 "rationale": f"Base record; {rec_pointer} = {recorded} (before the freeze)."}}
    if mutable:
        src["temporal_evidence"]["state_at_freeze_review"] = rev
    return src


# ---- reusable sources --------------------------------------------------------------------------------------------
HUB_T = ("gmail", f"{FRED}/1844732913254784171")
GUARD = ("gdocs", "f_b98287f6f80fe431a71209")
README = ("gdocs", "f_846ddc38b2aab3d2ed3fcb")
FOLDER = ("gdrive", "d_80a8c04753ba82ba4ba6a5")
TEMPLATE = ("gsheets", "f_05f0a451b29b19a1c0b90f")
ESG_T = ("gmail", f"{FRED}/1844177063117059830")
CHECK = ("gdocs", "f_3b06917a41dd59308d890b")
REVIEW = ("gcal", "evt_fd469c29811879519c2c96")
BOARD = ("trello", "640643a3fd8f3ca308d9318e")
NOTICE_T = ("gmail", f"{FRED}/1843067564852153540")


def thread(k):
    return ("gmail", IDS["threads"][k])


s_hub = S_sql("gmail", HUB_T[1], "gmail.gmail_messages", {"id": IDS["msg"]["hub"]}, "body_text", "date", [HUB_T],
              "The prompt names Leonard's email from yesterday; it is the To copy in Frederick's inbox.")
s_guard = S_sql("gdocs", GUARD[1], "gdocs.docs_documents", {"document_id": GUARD[1]}, "body_text", "modified_time",
                [HUB_T, GUARD], "Leonard's email: 'Go by the runway guardrails doc for what we do with each one'; the doc is "
                "shared with Frederick.", mutable=True,
                rev=review([GUARD[1], HUB_T[1]], SNAP + "Leonard's Sep 30 email, later than the doc's 2025-09-26T18:00Z change, "
                           "points to it as the rules in force."))
s_readme = S_sql("gdocs", README[1], "gdocs.docs_documents", {"document_id": README[1]}, "body_text", "modified_time",
                 [HUB_T, FOLDER, README], "Leonard's email: 'the README in the folder has the columns'; it sits in "
                 "Frederick's Q4 commitments folder.", mutable=True,
                 rev=review([README[1], HUB_T[1]], SNAP + "Created 2025-09-30T22:40Z, 40 minutes before the email that points to it."))
s_folder = S_sql("gdrive", FOLDER[1], "gdrive.drive_files", {"id": FOLDER[1]}, "name", "modified_time", [FOLDER],
                 "The prompt names 'my Q4 commitments folder'; Frederick owns it.", mutable=True,
                 rev=review([FOLDER[1]], SNAP + "The folder name is what the prompt names."))
s_template = S_sql("gsheets", TEMPLATE[1], "gsheets.sheets_spreadsheets", {"spreadsheet_id": TEMPLATE[1]}, "title",
                   "modified_time", [HUB_T, FOLDER, README, TEMPLATE], "The README says to copy the header row from the "
                   "template sheet in the same folder.", mutable=True,
                   rev=review([TEMPLATE[1], README[1]], SNAP + "Created and last changed 2025-09-30T22:45Z."))
s_amend = S_sql("slack", "C07C2866011/1759166100.370044", "slack.slack_messages", {"id": "7e88911312fa9a969f0659a105af59a3"},
                "text", "created_at", [HUB_T, ("slack", "C07C2866011/1759166100.370044")],
                "Leonard's email points to 'the one change I posted in #executives on Monday'; Frederick is a member.")
s_esg = S_sql("gmail", ESG_T[1], "gmail.gmail_messages", {"id": IDS["msg"]["esg_note"]}, "body_text", "date", [HUB_T, ESG_T],
              "Leonard's email: 'Anything that needs signing goes the way ESG's note about signing says'; Frederick is cc.")
s_ack = S_sql("gmail", ESG_T[1], "gmail.gmail_messages", {"id": IDS["msg"]["esg_ack"]}, "body_text", "date", [HUB_T, ESG_T],
              "Leonard's reply under ESG's note, Frederick cc: cards on the founders' board To Do list, the intake checklist.")
s_check = S_sql("gdocs", CHECK[1], "gdocs.docs_documents", {"document_id": CHECK[1]}, "body_text", "modified_time",
                [HUB_T, ESG_T, CHECK], "Leonard's reply under ESG's note: 'what to include is in the intake checklist I "
                "shared'; shared with Frederick.", mutable=True,
                rev=review([CHECK[1], ESG_T[1]], SNAP + "Created 2025-09-25T16:20Z, ten minutes before Leonard's reply cites it."))
s_review = S_sql("gcal", REVIEW[1], "gcal.gcal_events", {"event_id": REVIEW[1], "calendar_id": FRED}, "start_ts", "created",
                 [HUB_T, GUARD, REVIEW], "Guardrails step 5: 'the January commitments review I'll put on our calendars'; the "
                 "event is on Frederick's calendar.", semantics="scheduled_event", mutable=True,
                 rev=review([REVIEW[1], GUARD[1]], SNAP + "Created 2025-09-29T18:00Z; a future meeting at the clock."))
s_board = S_json("trello", BOARD[1], "data.json", "/boards/1/name", "/boards/1/dateLastActivity", [HUB_T, GUARD, BOARD],
                 "The prompt names 'our Harmony Games board' (Trello is unscoped).", mutable=True,
                 rev=review([BOARD[1], GUARD[1]], SNAP + "Board name as exported at the freeze."))
s_notice = S_sql("gmail", NOTICE_T[1], "gmail.gmail_messages", {"id": IDS["msg"]["clipforge_notice"]}, "body_text", "date",
                 [HUB_T, thread("Clipforge"), NOTICE_T], "Billing notice in Frederick's inbox; the Clipforge paper names "
                 "workspace HG-2291 and Gmail search 'HG-2291' finds the notice.")
s_waiver = S_sql("slack", "C07C2866011/1758920520.674991", "slack.slack_messages", {"id": "9fb2d23420c7e01ca163571f4129c912"},
                 "text", "created_at", [HUB_T, thread("Framewell"), ("slack", "C07C2866011/1758920520.674991")],
                 "Thread reply in #executives (member); Slack search 'Maren' (Framewell's contact) finds it.")
s_lfdm = S_sql("slack", "D05S58U4SAK/1759174260.052645", "slack.slack_messages", {"id": "418a0a6d6c29b7b67ce0ffb270c78c1e"},
               "text", "created_at", [HUB_T, thread("Lanternfly Publishing"), ("slack", "D05S58U4SAK/1759174260.052645")],
               "Reply in Frederick's DM with Leonard; Slack search 'Southeast Asia' (from the Lanternfly deck) finds it.")
s_spnote = S_sql("slack", "C07C2866011/1758134460.899858", "slack.slack_messages", {"id": "fc2f69c06b333f6c54dfd63d455c3958"},
                 "text", "created_at", [HUB_T, thread("Spotlight Fest"), ("slack", "C07C2866011/1758134460.899858")],
                 "Robert's #executives post (member); Slack search 'indie showcase' finds it.")
NIN_REL = "threads/frederick@harmonygames.co_1842359398719557772.json"
s_nin = S_json("gmail", f"{FRED}/1842359398719557772", NIN_REL, "/messages/0/subject", "/messages/0/date_parsed",
               [HUB_T, ("gmail", f"{FRED}/1842359398719557772")], "Nintendo Developer Portal notice in Frederick's inbox; "
               "Gmail search 'Nintendo' finds it. The deciding comment is Arthur's on Linear ZOM-567 (cmt_c9a6660d81e067ad1de7, "
               "seeded, unscoped), named in the evidence; this base notice is the dated record the V3 check can resolve.")
BAL_REL = "threads/frederick@harmonygames.co_1840501641217286806.json"
s_bal = S_json("gmail", f"{FRED}/1840501641217286806", BAL_REL, "/messages/1/body", "/messages/1/date_parsed",
               [HUB_T, ("gmail", f"{FRED}/1840501641217286806")], "Base thread in Frederick's mailbox (Frederick on every "
               "message); Gmail search 'Balancy' finds it.")


def ask(k):
    ms = sorted([x["row"] for x in SQL if x["table"] == "gmail.gmail_messages" and x["op"] == "insert"
                 and x["row"].get("thread_id") == IDS["threads"][k] and x["row"].get("user_email") == FRED],
                key=lambda r: int(r["internal_date"]))
    return [m for m in ms if not m["from_email"].endswith("@harmonygames.co")][-1]


def s_co(k, column="body_text"):
    m = ask(k)
    return S_sql("gmail", IDS["threads"][k], "gmail.gmail_messages", {"id": m["id"]}, column, "date", [HUB_T, thread(k)],
                 f"The {k} thread in Frederick's inbox; Gmail search '{k.split()[0]}' finds it.")


def s_paper(k):
    pid = IDS["papers"][k]
    d = [x for x in SQL if x["table"] == "gdocs.docs_documents" and x["row"].get("document_id") == pid]
    if d:
        return S_sql("gdocs", pid, "gdocs.docs_documents", {"document_id": pid}, "body_text", "modified_time",
                     [HUB_T, ("gdrive", IDS["paperwork_folder"]), ("gdocs", pid)], f"{k}'s paper in Frederick's "
                     "paperwork folder (owner Frederick).", mutable=True,
                     rev=review([pid, IDS["paperwork_folder"]], SNAP + "Filed paper, unchanged since it was created."))
    return S_sql("gdrive", pid, "gdrive.drive_files", {"id": pid}, "name", "modified_time",
                 [HUB_T, ("gdrive", IDS["paperwork_folder"]), ("gdrive", pid)], f"{k}'s deck in Frederick's paperwork folder.",
                 mutable=True, rev=review([pid, IDS["paperwork_folder"]], SNAP + "Filed deck, unchanged since it was created."))


def P(k):
    return ask(k)["from_email"]


def oe(*keys):
    out = []
    for k in keys:
        if k.endswith("*"):
            out += [f"OE {NUM[x]}" for x in sorted(NUM, key=lambda x: NUM[x]) if x.startswith(k[:-1])]
        else:
            out.append(f"OE {NUM[k]}")
    return out


def F(*keys):
    return " ".join(FID[k] for k in keys)


SP_HUB = "Leonard's email yesterday puts the vendor and partner backlog on me this week."
SP_ALL = "Can you work through all of it, going by his email for what needs doing and how we decide each one?"
SP_LOG = "The log goes in my Q4 commitments folder"
SP_CARD = "the cards for anything that needs signing go on our Harmony Games board"
SP_REM = "For anything that comes back at the January review, put a reminder on my calendar for that day, one per company, so none of them get lost."
SP_REPLY = "When it's all done, reply to Leonard on his email with what he asked for."
REM_DATES = {"instant_utc": "2026-01-05T17:00:00Z", "utc": "2026-01-05", "pacific": "2026-01-05", "prompt_timezone": None,
             "accepted_dates": ["2026-01-05"]}
for s in (SP_HUB, SP_ALL, SP_LOG, SP_CARD, SP_REM, SP_REPLY):
    assert s in (TI / "04_Prompt.txt").read_text(), s

R = []


def row(**k):
    k.setdefault("dist", "—")
    k.setdefault("amb", "—")
    k.setdefault("grp", "—")
    k.setdefault("ovl", "—")
    R.append(k)


def log_row(tag, co, col, value, t, w, kind, why, fact, srcs, fids, oes, dec, ev, acc, alt, valid, dist="—", grp="G1 log rows"):
    row(tag=tag, t=t, w=w, kind=kind, why=why, fact=fact, span=SP_ALL, oe=oes, fids=fids, vals=f"`{co}` · {value}",
        verify=f"{co}'s log row, {col} column", final=f"Log sheet row for {co}, column {col}", acc=acc, alt=alt, srcs=srcs,
        just=f"{kind.capitalize()}: {why}.", ev=ev, dec=dec, grp=grp, dist=dist, valid=valid,
        idle=f"No log row for {co} (an idle Agent writes no log)")


# ================================================================ D1 · the log
row(tag="log_folder", t="The Agent saves the vendor and partner log as a Google Sheet in Frederick's Drive folder \"Q4 commitments\" "
    "(created there, copied there or moved there)", w=1, kind="lookup", why="direct: the prompt names the folder",
    fact="log_location", span=SP_LOG, oe=oe("folder", "w:create", "w:move"), fids=F("folder"),
    vals="`Q4 commitments` `d_80a8c04753ba82ba4ba6a5`", verify="Log sheet in Frederick's folder",
    final="Drive file parent d_80a8c04753ba82ba4ba6a5",
    acc=["a Google Sheet whose final parent is the Q4 commitments folder", "created there, copied there from the template, or moved there"],
    alt="A sheet left in My Drive or another folder fails; creating, copying or moving it into the folder is the same end state.",
    srcs=[s_folder], just="Lookup: the prompt names the folder ('The log goes in my Q4 commitments folder').",
    ev="Source: folder 'Q4 commitments' d_80a8c04753ba82ba4ba6a5 (owner Frederick). Accept: a Google Sheet whose final parent is "
       "that folder, whether created there, copied there from the template f_05f0a451b29b19a1c0b90f, or moved there.",
    dec="F7", valid="The template copied into the folder as 'Q4 commitments log'", idle="No log sheet in 'Q4 commitments'")
row(tag="log_header", t="The Agent's log sheet has the column headings Company, Contact, What's waiting, Decision, Answered by, "
    "What we told them and Next date, in that order (any letter case)", w=1, kind="lookup",
    why="direct: the README lists the seven columns and says to copy the template's header row", fact="log_header", span=SP_LOG,
    oe=oe("readme", "template", "w:rows"), fids=F("readme", "template"),
    vals="`Q4 commitments - template` · the seven README headings (Company, Contact, What's waiting, Decision, Answered by, What we told them, Next date)",
    verify="Log header row", final="Row 1 of the log sheet", acc=["the seven headings in this order, any letter case"],
    alt="A header copied from the template passes; renamed, dropped or reordered columns fail. The header is one record "
    "(components of one row copied from one template), not seven independent facts.", srcs=[s_readme, s_template],
    just="Lookup: the README in the folder lists the columns and says 'copy the header row from the template sheet'.",
    ev="Sources: README f_846ddc38b2aab3d2ed3fcb ('Company · Contact · What's waiting · Decision · Answered by · What we told "
       "them · Next date') and template sheet f_05f0a451b29b19a1c0b90f, tab 'Log'. Accept: those seven headings in that order, "
       "any letter case.", dec="F8", valid="Header copied from the template", idle="No log sheet, so no header row")
row(tag="log_rows", t="The Agent's log sheet has exactly 36 company rows below the header, one row per company", w=5,
    kind="multi-source", why="a volume count only the full audit produces: the 33 filed papers, Hootline, Balancy and Nintendo, "
    "against Leonard's scope and exclusions (the investors, Mattel, the ad networks, cold pitches)", fact="log_size", span=SP_ALL,
    oe=oe("papers", "sweep", "w:rows"), fids=F("hub", "papers") + " " + F("co:Hootline", "co:Balancy", "co:Nintendo"),
    vals="`36`", verify="Number of company rows in the log", final="Row count of the log sheet (header excluded)",
    acc=["36 company rows, one per company, in any order"],
    alt="34 rows (Nintendo and Balancy missing) or 37 (a look-alike such as Mattel or NCsoft added) fails. Two rows for one "
    "company count once.", srcs=[s_hub, s_folder],
    just="Multi-source: the 36 companies come from the paperwork folder (33 papers), Hootline's August thread, the base Balancy "
         "thread and Nintendo's portal notices with Linear ZOM-567, minus every look-alike Leonard's email excludes.",
    ev="Sources: Leonard's email (thread frederick.stone@harmonygames.co/1844732913254784171: 'anyone outside the investor work who "
       "has an offer, a trial, a quote, terms or an ask in front of us and that one of us has actually engaged with'), paperwork "
       "folder d_ffa3e6e473da7e6523614f (33 papers), Hootline thread frederick.stone@harmonygames.co/1839631800730308867, Balancy "
       "thread frederick.stone@harmonygames.co/1840501641217286806, Nintendo notice thread frederick.stone@harmonygames.co/1842359398719557772. "
       "Accept: exactly 36 company rows below the header.", dec="C1 C7 F13 F29 F51 F62", grp="G1 log rows (volume row)",
    dist="T: Mattel, NCsoft, Dentsu, Appodeal and the cold pitches stay off", valid="36 rows in any order",
    idle="No log sheet, so no rows")
log_row("nin_decision", "Nintendo", "Decision", "Sign", "The Agent's log gives Nintendo (its developer portal terms) the Decision "
        "\"Sign\"", 5, "multi-source", "the portal mail says registration completed, but Arthur's Linear comment on ZOM-567 says "
        "the Global ToS and NDA still needs an officer's acceptance at no fee (guardrails step 4)", "nintendo_decision",
        [s_nin, s_guard], F("co:Nintendo", "zom", "nin_mail"), oe("sweep", "co:Nintendo", "w:rows"), "C1 F20",
        "Sources: Linear ZOM-567 comment cmt_c9a6660d81e067ad1de7 by Arthur ('the Global ToS and NDA still needs our agreement "
        "approver to accept it'; 'no fee, no fixed term, no exclusivity'), Nintendo portal notice thread "
        "frederick.stone@harmonygames.co/1842359398719557772 ('Registration Completed'), guardrails f_b98287f6f80fe431a71209 "
        "step 4. Accept: Decision 'Sign' on the Nintendo row (also 'Nintendo Developer Portal').",
        ["Sign"], "End, Park or Answered fails; the README's word is 'Sign'.", "Nintendo / Sign / Next date 2025-10-15",
        dist="T: 'Registration Completed' and 'NDA Effective: 09/04/2025' look done")
log_row("fw_decision", "Framewell", "Decision", "Park", "The Agent's log gives Framewell the Decision \"Park\"", 5, "multi-source",
        "the order form bills $149/month from Nov 1, but Leonard's Sep 26 #executives thread reply says Maren will hold the Pro "
        "plan at no charge until Feb 1 with nothing to sign (guardrails step 5)", "framewell_decision", [s_waiver, s_co("Framewell")],
        F("co:Framewell", "waiver"), oe("co:Framewell", "waiver", "w:rows"), "C2 F22",
        "Sources: Leonard's thread reply C07C2866011/1758920520.674991 ('they'll hold it at no charge until Feb 1 with nothing to "
        "sign before then'), Framewell thread frederick.stone@harmonygames.co/1843618067251203081 (Maren Holt), order form "
        "f_fba21c2d5d4bbb02983961 ('Billing starts: Nov 1, 2025'). Accept: Decision 'Park' on the Framewell row.",
        ["Park"], "End (from the order form alone) fails.", "Framewell / Park / Next date 2026-01-05",
        dist="T: the order form's Nov 1 billing")
log_row("lf_decision", "Lanternfly Publishing", "Decision", "Answered", "The Agent's log gives Lanternfly Publishing the Decision "
        "\"Answered\"", 5, "multi-source", "the deck reads as a signing item, but Leonard's Sep 29 DM thread reply says he rang Wen "
        "and told them Southeast Asia waits until after the raise (guardrails step 1)", "lanternfly_decision",
        [s_lfdm, s_co("Lanternfly Publishing")], F("co:Lanternfly Publishing", "lf_dm"), oe("co:Lanternfly Publishing", "lf_dm", "w:rows"),
        "C3 F24", "Sources: Leonard's DM reply D05S58U4SAK/1759174260.052645 ('I rang Wen back on Saturday about their Southeast "
        "Asia deal and let them know Southeast Asia has to wait until after the raise'), Lanternfly thread "
        "frederick.stone@harmonygames.co/1842800807116855774 (Wen Halvorsen). Accept: Decision 'Answered' on the Lanternfly "
        "Publishing row (also 'Lanternfly').", ["Answered"], "Sign (from the deck's exclusive 2-year term) or Park fails.",
        "Lanternfly Publishing / Answered / Leonard", dist="T: Frederick's 'we'll take a look and get back to you' is a holding reply")
log_row("sp_decision", "Spotlight Fest", "Decision", "Answered", "The Agent's log gives Spotlight Fest the Decision \"Answered\"", 5,
        "multi-source", "Rina's thread asks for a $750 stand fee, but Robert's Sep 17 #executives post says he had the call about the "
        "Dec 5 indie showcase and let Rina know we're sitting it out (guardrails step 1)", "spotlight_decision",
        [s_spnote, s_co("Spotlight Fest")], F("co:Spotlight Fest", "sp_note"), oe("co:Spotlight Fest", "sp_note", "w:rows"), "C8 F25",
        "Sources: Robert's post C07C2866011/1758134460.899858 ('had the call about the Dec 5 indie showcase. we're sitting this one "
        "out this year, I let Rina know'), Spotlight Fest thread frederick.stone@harmonygames.co/1842712097588195482 (Rina "
        "Takeda). Accept: Decision 'Answered' on the Spotlight Fest row.", ["Answered"], "End (from the $750 fee) fails.",
        "Spotlight Fest / Answered / Robert")
log_row("lf_by", "Lanternfly Publishing", "Answered by", "Leonard", "The Agent's log records Leonard (Leonard or Leonard Hayes) in "
        "the Answered by column of the Lanternfly Publishing row", 5, "multi-source", "the answerer is named only in Leonard's DM "
        "thread reply, which calls the company 'Wen' and 'their Southeast Asia deal'", "lanternfly_answerer", [s_lfdm],
        F("lf_dm", "co:Lanternfly Publishing"), oe("lf_dm", "w:rows"), "C3 F24",
        "Source: Leonard's DM reply D05S58U4SAK/1759174260.052645 ('I rang Wen back on Saturday'). Accept: 'Leonard' or 'Leonard "
        "Hayes' in Answered by on the Lanternfly Publishing row, with or without the date (Sat Sep 27).",
        ["Leonard", "Leonard Hayes"], "A blank Answered by, or Frederick, fails.", "Answered by: Leonard (Sep 27)")
log_row("sp_by", "Spotlight Fest", "Answered by", "Robert", "The Agent's log records Robert in the Answered by column of the "
        "Spotlight Fest row", 5, "multi-source", "Robert's #executives post names Rina and the Dec 5 showcase, not the company; the "
        "Spotlight thread ties both to Spotlight Fest", "spotlight_answerer", [s_spnote], F("sp_note", "co:Spotlight Fest"),
        oe("sp_note", "w:rows"), "C8 F25",
        "Source: Robert's post C07C2866011/1758134460.899858 ('I let Rina know'). Accept: 'Robert' in Answered by on the "
        "Spotlight Fest row, with or without the date (Wed Sep 17).", ["Robert"], "A blank Answered by fails.",
        "Answered by: Robert (Sep 17)")
log_row("bal_by", "Balancy", "Answered by", "Leonard", "The Agent's log records Leonard (Leonard or Leonard Hayes) in the Answered by "
        "column of the Balancy row", 3, "interpretation", "one base thread: Leonard's Sep 11 'we'll circle back with you as soon "
        "as we get some bandwidth' is an answer that says later (guardrails step 1)", "balancy_answerer", [s_bal],
        F("co:Balancy"), oe("co:Balancy", "w:rows"), "F62",
        "Source: Balancy thread frederick.stone@harmonygames.co/1840501641217286806, Leonard, Thu Sep 11 2025 ('company priorities "
        "have shifted a bit for the next few months - we'll circle back with you as soon as we get some bandwidth'). Accept: "
        "'Leonard' or 'Leonard Hayes' in Answered by on the Balancy row.", ["Leonard", "Leonard Hayes"],
        "A missing Balancy row or a blank Answered by fails.", "Balancy / Answered / Leonard (Sep 11)")
log_row("mf_by", "Motive Forge", "Answered by", "Arthur", "The Agent's log records Arthur (Arthur or Arthur Blake) in the Answered "
        "by column of the Motive Forge row", 3, "interpretation", "one thread: Arthur's Sep 19 reply to Hugo already passed on the "
        "quote (guardrails step 1)", "motiveforge_answerer", [s_co("Motive Forge")], F("co:Motive Forge"),
        oe("co:Motive Forge", "w:rows"), "F63",
        "Source: Motive Forge thread frederick.stone@harmonygames.co/1843346276352084348, Arthur Blake, Fri Sep 19 2025 ('we're "
        "keeping the art in-house, so we'll pass on this one'). Accept: 'Arthur' or 'Arthur Blake' in Answered by on the Motive "
        "Forge row.", ["Arthur", "Arthur Blake"], "A blank Answered by fails.", "Motive Forge / Answered / Arthur (Sep 19)")
s_ar = S_sql("gmail", IDS["threads"]["Motive Forge"], "gmail.gmail_messages",
             {"id": [x["row"]["id"] for x in SQL if x["table"] == "gmail.gmail_messages" and x["row"].get("thread_id") == IDS["threads"]["Motive Forge"]
                     and x["row"].get("from_email") == "arthur.blake@harmonygames.co"][0]}, "body_text", "date",
             [HUB_T, thread("Motive Forge")], "Arthur's reply in the Motive Forge thread, Frederick cc.")
R[-1]["srcs"] = [s_ar]
log_row("nin_next", "Nintendo", "Next date", "2025-10-15", "The Agent's log gives Nintendo the Next date Oct 15, 2025 (any date "
        "form)", 5, "multi-source", "the date is only in Arthur's Linear comment ('It has to be accepted by Oct 15 or the request "
        "lapses'), read with the README's Sign rule (the date they need it by)", "nintendo_deadline", [s_nin, s_readme],
        F("zom", "readme"), oe("co:Nintendo", "w:rows"), "C1 F20",
        "Sources: Linear ZOM-567 comment cmt_c9a6660d81e067ad1de7 ('It has to be accepted by Oct 15 or the request lapses'), README "
        "f_846ddc38b2aab3d2ed3fcb ('for Sign, the date they need it by'). Accept: Oct 15, 2025 in any date form.",
        ["2025-10-15", "Oct 15, 2025", "10/15/2025"], "A blank Next date fails.", "Nintendo Next date 2025-10-15")
log_row("cf_next", "Clipforge", "Next date", "2025-10-15", "The Agent's log gives Clipforge the Next date Oct 15, 2025 (any date "
        "form)", 5, "multi-source", "the pilot agreement says free through Jan 15, 2026, but the Paylane notice moves the paid plan "
        "to Oct 16 and sets 'write to billing@paylane.io by Oct 15' (README: for End, the last day to cancel)", "clipforge_deadline",
        [s_notice, s_readme], F("co:Clipforge", "notice", "readme"), oe("co:Clipforge", "notice", "w:rows"), "C5 F27",
        "Sources: Paylane notice thread frederick.stone@harmonygames.co/1843067564852153540 ('the pilot now ends on Oct 15, 2025 and "
        "the Studio plan starts on Oct 16'; 'write to billing@paylane.io by Oct 15'), README f_846ddc38b2aab3d2ed3fcb ('for End, "
        "the last day to cancel or say no'). Accept: Oct 15, 2025 in any date form.",
        ["2025-10-15", "Oct 15, 2025"], "Jan 15, 2026 (the pilot agreement's date) fails.", "Clipforge / End / 2025-10-15",
        dist="T: the July tracker and the pilot agreement say free through Jan 15")
log_row("ph_next", "Pixel Harbor Events", "Next date", "2025-10-10", "The Agent's log gives Pixel Harbor Events the Next date Oct 10, "
        "2025 (any date form)", 3, "interpretation", "the June quote's deposit date is the last day to say no (README End rule); "
        "Frederick's 'I'll come back to you on this' is a holding reply", "pixelharbor_deadline", [s_paper("Pixel Harbor Events"), s_readme],
        F("co:Pixel Harbor Events", "readme"), oe("co:Pixel Harbor Events", "w:rows"), "C6 F34",
        "Sources: booth quote f_614f88a28a2f0cf1b88408 ('deposit $2,400 due by Oct 10, 2025 to hold the booth'), README "
        "f_846ddc38b2aab3d2ed3fcb. Accept: Oct 10, 2025 in any date form.", ["2025-10-10", "Oct 10, 2025"],
        "Oct 20 (the balance date) or Oct 24 (the event) fails.", "Pixel Harbor Events / End / 2025-10-10",
        dist="T: the June thread sits outside a recent-mail window")
log_row("pw_next", "Pingwise", "Next date", "2025-11-01", "The Agent's log gives Pingwise the Next date Nov 1, 2025 (any date form)",
        5, "multi-source", "Pingwise is Keep only because its paging is the keep-running card's 'night pager' (Trello); the Keep "
        "rule then takes the next billing date from the mail and terms", "pingwise_nextbill", [s_co("Pingwise"), s_board],
        F("co:Pingwise", "keepcard", "readme"), oe("keepcard", "co:Pingwise", "w:rows"), "C4 F10",
        "Sources: Pingwise thread frederick.stone@harmonygames.co/1844157874176168845 ('From Nov 1 the account moves to Team "
        "($29/month)'), keep-running card on board 640643a3fd8f3ca308d9318e ('the night pager for backend outages'), README "
        "('for Keep, when it next bills'). Accept: Nov 1, 2025 in any date form.", ["2025-11-01", "Nov 1, 2025"],
        "Oct 31 (the downgrade cut-off) fails.", "Pingwise / Keep / 2025-11-01", dist="T: 'night pager' names no vendor")
log_row("ph_told", "Pixel Harbor Events", "What we told them", "declined",
        "The Agent's log records in What we told them that Pixel Harbor Events was turned down (declined, said no or passed; any "
        "wording with that meaning)", 3, "interpretation", "the booth deposit fails the cash test (guardrails step 2), so the "
        "answer is a decline", "pixelharbor_answer", [s_paper("Pixel Harbor Events"), s_guard], F("co:Pixel Harbor Events", "guardrails"),
        oe("co:Pixel Harbor Events", "w:rows"), "C6 F34",
        "Sources: booth quote f_614f88a28a2f0cf1b88408 ('Price: $4,800; deposit $2,400 due by Oct 10, 2025'), guardrails "
        "f_b98287f6f80fe431a71209 step 2 ('say no, or cancel it in writing'). Accept: any wording that says we declined.",
        ["declined", "said no", "passed", "turned down"], "Parked, 'with Leonard or Arthur to sign' or a blank fails.",
        "What we told them: declined the booth", grp="G2 told column")
log_row("lf_told", "Lanternfly Publishing", "What we told them", "after the raise",
        "The Agent's log records in What we told them that Lanternfly Publishing was told Southeast Asia has to wait until after "
        "the raise (any wording with that meaning)", 5, "multi-source", "what Leonard told Wen is only in the DM thread reply",
        "lanternfly_answer", [s_lfdm], F("lf_dm"), oe("lf_dm", "w:rows"), "C3 F24",
        "Source: Leonard's DM reply D05S58U4SAK/1759174260.052645 ('let them know Southeast Asia has to wait until after the "
        "raise. we'll pick it up again in January'). Accept: any wording that the deal waits until after the raise, with or "
        "without 'January'.", ["after the raise", "until after the raise"], "'With our lawyers first' or a decline fails.",
        "What we told them: SE Asia waits until after the raise (Leonard, Sep 27)", grp="G2 told column")
log_row("sv_told", "Soundvault", "What we told them", "declined", "The Agent's log records in What we told them that Soundvault was "
        "turned down (declined, said no or passed; any wording with that meaning)", 3, "interpretation", "a licence paid in full "
        "on signature before Oct 15 fails the cash test (guardrails step 2)", "soundvault_answer", [s_paper("Soundvault"), s_guard],
        F("co:Soundvault", "guardrails"), oe("co:Soundvault", "w:rows"), "F36",
        "Sources: licence quote f_2686da1086bfcc2fba3f57 ('Price: $1,188, paid in full on signature'), guardrails "
        "f_b98287f6f80fe431a71209 step 2. Accept: any wording that says we declined.", ["declined", "said no", "passed"],
        "Parked or a blank fails.", "What we told them: declined the licence", grp="G2 told column")
log_row("kin_told", "Kinetic Arcade", "What we told them", "with our lawyers first",
        "The Agent's log records in What we told them that Kinetic Arcade was told its letter of intent goes to our lawyers (ESG) "
        "first", 5, "multi-source", "the LOI's 12-month exclusivity is an ESG trigger in ESG's note, and guardrails step 4 says to "
        "tell them it is with our lawyers first", "kinetic_answer", [s_esg, s_guard], F("co:Kinetic Arcade", "esg", "guardrails"),
        oe("co:Kinetic Arcade", "esg", "w:rows"), "F45 F4",
        "Sources: LOI f_6252955f500f81e3aacbef ('Exclusivity: 12 months from signature'), ESG note thread "
        "frederick.stone@harmonygames.co/1844177063117059830 ('Anything with an automatic renewal, exclusivity, a licence of your IP "
        "or a term over 12 months comes to us before anyone signs'), guardrails step 4 ('with our lawyers first when ESG has to see "
        "it'). Accept: counsel, lawyers, legal or ESG first.", ["with our lawyers first", "with counsel (ESG) first", "ESG review first"],
        "'With Leonard or Arthur to sign' without the lawyers fails.", "What we told them: with our lawyers (ESG) first",
        grp="G2 told column")
log_row("ww_told", "Wishwave", "What we told them", "declined", "The Agent's log records in What we told them that Wishwave was "
        "turned down (declined, said no or passed; any wording with that meaning)", 5, "multi-source", "the travel Wishwave books "
        "and bills counts as cash only after Leonard's Monday #executives change to the guardrails", "wishwave_answer",
        [s_amend, s_paper("Wishwave")], F("co:Wishwave", "amend"), oe("co:Wishwave", "amend", "w:rows"), "F3 F42",
        "Sources: Leonard's Monday post C07C2866011/1759166100.370044 ('travel and event costs count as cash even when a partner "
        "books them and bills us'), proposal f_54c2b4e172bb73a4a19845 ('travel and hotel for two, booked by Wishwave and invoiced "
        "at cost'). Accept: any wording that says we declined.", ["declined", "said no", "passed"],
        "Parked (from the doc's original travel rule) fails.", "What we told them: declined the expo push", grp="G2 told column",
        dist="T: the guardrails doc's own 'only when we book them ourselves'")

# ================================================================ D2 · written answers
ANSWERS = sorted(k for k, v in TRUTH.items() if "written_answer" in v["groups"])
assert len(ANSWERS) == 31
row(tag="ans_count", t="The Agent sends written answers to exactly 31 of the vendor and partner companies (each company counted once "
    "however many emails it gets; the cancellation to billing@paylane.io counts as Clipforge's)", w=5, kind="multi-source",
    why="a volume count only the full audit produces: everyone waiting gets an answer except the four already answered and the "
    "Nintendo portal", fact="answers_count", span=SP_HUB, oe=oe("guardrails", "w:paylane", "w:ans:*"), fids=F("hub", "guardrails"),
    vals="`31`", verify="Number of companies that received a written answer",
    final="Sent mails from Frederick's mailbox to company contacts", acc=["31 companies, each counted once"],
    alt="Writing again to Rina (Spotlight Fest), Wen (Lanternfly) or Balancy, or skipping Orbit Store's Mateo, fails.",
    srcs=[s_hub, s_guard],
    just="Multi-source: which 31 companies are waiting depends on every company's decision, including the four Answered ones "
         "settled in Slack and the base Balancy thread.",
    ev="Sources: Leonard's email thread frederick.stone@harmonygames.co/1844732913254784171 ('Everyone who is waiting to hear from "
       "us should get a written answer this week'), guardrails f_b98287f6f80fe431a71209 ('If one of us has already given them an "
       "answer, don't write to them again'; 'Portals and no-reply notices don't need one'). Accept: written answers reach "
       "exactly 31 companies.", dec="C3 C8 F2", grp="G3 written answers (volume row)", valid="31 replies on the company threads",
    idle="No email sent")
row(tag="cf_cancel", t="The Agent emails billing@paylane.io to cancel Clipforge's workspace HG-2291 before the Studio plan starts",
    w=5, kind="multi-source", why="the pilot agreement says to cancel 'to the billing address on your notice'; only the Paylane "
    "notice names billing@paylane.io and says replies to it aren't monitored", fact="clipforge_cancellation", span=SP_ALL,
    oe=oe("notice", "w:paylane"), fids=F("notice", "co:Clipforge"), vals="`billing@paylane.io` `HG-2291`",
    verify="Cancellation email to billing@paylane.io", final="Sent email to billing@paylane.io",
    acc=["a sent email to billing@paylane.io that cancels workspace HG-2291 or the Clipforge UGC Studio plan"],
    alt="A reply to the notice (not monitored) or only a reply to Priya fails as the cancellation.", srcs=[s_notice],
    just="Multi-source: the pilot agreement (Drive) points to 'the billing address on your notice', which only the Paylane notice "
         "(Gmail) gives.",
    ev="Source: Paylane notice thread frederick.stone@harmonygames.co/1843067564852153540 ('To cancel before the plan starts, write "
       "to billing@paylane.io by Oct 15. Replies to this email aren't monitored.'); pilot agreement f_8d0e0e3ae076b2f745e7e2. "
       "Accept: a sent email to billing@paylane.io cancelling workspace HG-2291 (UGC Studio).", dec="C5 F27",
    grp="G3 written answers", valid="A new email to billing@paylane.io cancelling HG-2291", idle="No email sent")
row(tag="cf_priya", t="The Agent tells Priya Raman (PERSON_9704_EMAIL) in writing that Harmony Games is ending the Clipforge pilot "
    "rather than carrying on", w=5, kind="multi-source", why="Priya asked to be told; the decision to end rests on the Paylane "
    "notice, a separate record", fact="clipforge_priya_answer", span=SP_HUB, oe=oe("co:Clipforge", "notice", "w:ans:Clipforge"),
    fids=F("co:Clipforge", "notice"), vals="`PERSON_9704_EMAIL`", verify="Answer to Priya", final="Sent email to PERSON_9704_EMAIL",
    acc=["a reply on Priya's thread or a new email to PERSON_9704_EMAIL saying we're ending the pilot or not continuing"],
    alt="Only the billing cancellation, with nothing to Priya, fails: her Sep 22 mail asks 'let me know here too'.",
    srcs=[s_co("Clipforge"), s_notice],
    just="Multi-source: Priya's ask is in her thread, and the answer (ending) follows from the Paylane notice.",
    ev="Sources: Clipforge thread frederick.stone@harmonygames.co/1837102635418059486, Priya Raman, Sep 22 ('If you're not carrying "
       "on after the pilot, let me know here too'); Paylane notice thread frederick.stone@harmonygames.co/1843067564852153540. "
       "Accept: a reply or new email to PERSON_9704_EMAIL that says the pilot ends.", dec="C5 F33", grp="G3 written answers",
    valid="A reply on Priya's thread: we're stopping after the pilot", idle="No email sent")
row(tag="ans_orbit", t="The Agent tells Mateo Rossi (PERSON_9719_EMAIL) in writing that Orbit Store's featuring agreement is with "
    "Leonard or Arthur to sign", w=3, kind="interpretation", why="the agreement is accepted in a partner portal, but Mateo writes "
    "himself and nudged on Sep 30, so the guardrails' Sign answer is owed to him", fact="orbit_answer", span=SP_HUB,
    oe=oe("co:Orbit Store", "w:ans:Orbit Store"), fids=F("co:Orbit Store", "guardrails"), vals="`PERSON_9719_EMAIL`",
    verify="Answer to Mateo", final="Sent email to PERSON_9719_EMAIL",
    acc=["a reply or new email to PERSON_9719_EMAIL saying it is with Leonard or Arthur (or either name) to sign or accept"],
    alt="Treating Orbit as a portal and writing nothing fails: the 'Portals and no-reply notices' line covers no-reply senders.",
    srcs=[s_co("Orbit Store"), s_guard],
    just="Interpretation: one thread read against guardrails step 4 ('Tell them it's with Leonard or Arthur to sign').",
    ev="Sources: Orbit Store thread frederick.stone@harmonygames.co/1843708664218314020, Mateo Rossi, Sep 30 ('gentle nudge on the "
       "featuring agreement, Oct 24 is the cut-off'); guardrails f_b98287f6f80fe431a71209 step 4. Accept: a reply or new email "
       "to PERSON_9719_EMAIL that says it is with Leonard or Arthur to sign or accept.", dec="F48", grp="G3 written answers",
    valid="A reply: Leonard or Arthur will accept it in the portal", idle="No email sent")

# ================================================================ D4 · ESG intake
row(tag="esg_count", t="The Agent sends exactly three agreement-intake emails to ESG Law intake (PERSON_2599_EMAIL), one per "
    "agreement", w=5, kind="multi-source", why="a volume count: only the agreements with an ESG trigger (exclusivity, a term over 12 "
    "months, a licence of our IP) go, and the template NDA and the already-answered Lanternfly deck do not",
    fact="esg_count", span=SP_ALL, oe=oe("esg", "esg_contact", "w:esg:*"), fids=F("esg", "checklist", "esg_contact"), vals="`3`",
    verify="Number of intake emails to ESG Law intake", final="Sent emails to PERSON_2599_EMAIL", acc=["three emails, one per agreement"],
    alt="A fourth email for Lanternfly Publishing or Playfuse fails; one combined email fails ('one email per agreement').",
    srcs=[s_esg, s_ack],
    just="Multi-source: the set rests on ESG's triggers (Gmail), each company's paper (Drive) and the Answered status of "
         "Lanternfly (Slack).",
    ev="Sources: ESG note thread frederick.stone@harmonygames.co/1844177063117059830 ('one email per agreement'; 'Mutual NDAs on our "
       "template don't need review'); ESG Law intake contact 9b0185e445572aeee9f27d35 (PERSON_2599_EMAIL). Accept: exactly three "
       "emails to PERSON_2599_EMAIL.", dec="C3 F4", grp="G4 ESG intake (volume row)", valid="Three separate intake emails",
    idle="No email sent")
row(tag="esg_lumen", t="The Agent emails ESG Law intake (PERSON_2599_EMAIL) about the Lumencloud Startup Program Agreement, giving "
    "its 36-month term", w=5, kind="multi-source", why="the 36-month term is the ESG trigger, and the checklist asks for the term",
    fact="esg_lumencloud", span=SP_ALL, oe=oe("co:Lumencloud", "checklist", "w:esg:Lumencloud"),
    fids=F("co:Lumencloud", "checklist", "esg"), vals="`PERSON_2599_EMAIL` `Lumencloud` `36 months`",
    verify="Lumencloud intake email", final="Sent email to PERSON_2599_EMAIL naming Lumencloud",
    acc=["an email to PERSON_2599_EMAIL about Lumencloud that states the 36-month term"],
    alt="An email that omits the term, or a Lumencloud card without the intake email, fails.", srcs=[s_check, s_paper("Lumencloud")],
    just="Multi-source: the paper's term (Drive) against ESG's trigger list (Gmail) and the checklist (Docs).",
    ev="Sources: agreement f_a227b14f03e12005fe8324 ('Term: 36 months from signature'), checklist f_3b06917a41dd59308d890b ('the "
       "term and any automatic renewal'). Accept: a sent email to PERSON_2599_EMAIL about Lumencloud that gives a 36-month term.",
    dec="F46 F5", grp="G4 ESG intake", valid="Intake email: Lumencloud, $25,000 credits, 36 months, by Oct 31",
    idle="No email sent")
row(tag="esg_bundle", t="The Agent emails ESG Law intake (PERSON_2599_EMAIL) about Bundlehouse's participation agreement, saying it "
    "licenses our game's name, logo and art", w=5, kind="multi-source", why="the IP licence is the ESG trigger, and the checklist asks "
    "for 'any exclusivity or licence of our IP'", fact="esg_bundlehouse", span=SP_ALL,
    oe=oe("co:Bundlehouse", "checklist", "w:esg:Bundlehouse"), fids=F("co:Bundlehouse", "checklist", "esg"),
    vals="`PERSON_2599_EMAIL` `Bundlehouse` · licence of the name, logo and art", verify="Bundlehouse intake email",
    final="Sent email to PERSON_2599_EMAIL naming Bundlehouse",
    acc=["an email to PERSON_2599_EMAIL about Bundlehouse that states the licence of the game's name, logo or art"],
    alt="An email that omits the licence fails.", srcs=[s_check, s_paper("Bundlehouse")],
    just="Multi-source: the deck's licence (Slides) against ESG's trigger list (Gmail) and the checklist (Docs).",
    ev="Sources: Bundlehouse deck f_9d1e0270574584de0eb92c ('Bundlehouse may use your game's name, logo and art in bundle "
       "marketing for 18 months'), checklist f_3b06917a41dd59308d890b ('any exclusivity or licence of our IP'). Accept: a sent "
       "email to PERSON_2599_EMAIL about Bundlehouse that states the licence.", dec="F47 F5", grp="G4 ESG intake",
    valid="Intake email: Bundlehouse, 18-month licence, by Nov 1", idle="No email sent")

# ================================================================ D3 · cards
row(tag="card_count", t="The Agent creates exactly seven new cards in the To Do list of the Harmony Games Trello board", w=5,
    kind="multi-source", why="a volume count: one card per company waiting on a signature, which needs every Sign decision "
    "(including Nintendo from Linear and excluding the already-answered Lanternfly)", fact="cards_count", span=SP_CARD,
    oe=oe("board", "w:card:*"), fids=F("board", "esg"), vals="`7` `640643a3fd8f3ca308d93195`",
    verify="Number of new cards in To Do", final="New cards in list 640643a3fd8f3ca308d93195", acc=["seven new cards in To Do"],
    alt="Six (Nintendo missing) or a card for Lanternfly Publishing instead of Nintendo still miscounts or misplaces; eight fails.",
    srcs=[s_ack, s_board],
    just="Multi-source: the Sign set joins Linear (Nintendo), Slack (Lanternfly answered) and each company's paper.",
    ev="Sources: Leonard's reply thread frederick.stone@harmonygames.co/1844177063117059830 ('anything waiting on Arthur or me to "
       "sign, put it on our founders' board To Do list'), board 640643a3fd8f3ca308d9318e, list To Do 640643a3fd8f3ca308d93195. "
       "Accept: exactly seven new cards in that list.", dec="C1 C3 F4", grp="G5 cards (volume row)",
    valid="Seven cards, one per Sign company", idle="No card created")
for tag, co, w, kind, why, fid, dec, extra in [
        ("card_nin", "Nintendo", 5, "multi-source", "Nintendo's Sign status comes only from Arthur's Linear comment on ZOM-567",
         F("co:Nintendo", "zom", "board"), "C1 F20", "Linear ZOM-567 comment cmt_c9a6660d81e067ad1de7 (an officer must accept the "
         "Global ToS and NDA by Oct 15)"),
        ("card_kin", "Kinetic Arcade", 3, "interpretation", "the LOI's 'Signature needed by Oct 20, 2025' read against guardrails "
         "step 4", F("co:Kinetic Arcade", "board"), "F45", "LOI f_6252955f500f81e3aacbef ('Signature needed by Oct 20, 2025')"),
        ("card_mark", "Markward", 5, "multi-source", "Leonard's Sep 25 reply replaces his July Slack note that Fred can accept "
         "small terms himself, and ESG's note covers click-through terms", F("co:Markward", "esg", "board"), "F49 F4",
         "ESG note thread frederick.stone@harmonygames.co/1844177063117059830 ('That includes click-through terms'; Leonard: "
         "'This replaces what I said in July')")]:
    row(tag=tag, t=f"The Agent creates a card in the To Do list of the Harmony Games Trello board with {co} in its title", w=w,
        kind=kind, why=why, fact=f"card_{co.split()[0].lower()}", span=SP_CARD, oe=oe(f"co:{co}", f"w:card:{co}"), fids=fid,
        vals=f"`{co}` `640643a3fd8f3ca308d93195`", verify=f"{co} card in To Do", final="Card in list 640643a3fd8f3ca308d93195",
        acc=[f"a card in To Do whose title names {co} (any letter case)"], alt="A card in Doing or Backlog, or a title without the "
        "company, fails.", srcs=[s_ack, s_board] if co != "Nintendo" else [s_nin, s_board],
        just=f"{kind.capitalize()}: {why}.", ev=f"Sources: {extra}; Leonard's reply under ESG's note ('with the company's name in "
        "the card title'); board 640643a3fd8f3ca308d9318e, To Do 640643a3fd8f3ca308d93195. Accept: a new card in To Do whose "
        f"title names {co}.", dec=dec, grp="G5 cards", valid=f"Card '{co} - sign' in To Do", idle="No card created",
        dist="T: Leonard's July 'accept the terms yourself' note" if co == "Markward" else "—")

# ================================================================ D5 · contacts
row(tag="ct_count", t="The Agent adds exactly 32 new contacts to Contacts", w=5, kind="multi-source",
    why="a volume count: one per company person not already in Contacts (Noor Haddad, Aiden Clarke and Leah Brennan already are; "
    "the Nintendo portal has no person), which needs the full company audit", fact="contacts_count", span=SP_HUB,
    oe=oe("contacts_check", "w:contact:*"), fids=F("readme", "contacts_existing"), vals="`32`", verify="Number of new contacts",
    final="New Contacts entries", acc=["32 new contacts"],
    alt="Adding Noor, Aiden or Leah again, or a portal sender, overcounts; missing Balancy's or Hootline's person undercounts.",
    srcs=[s_readme, s_hub],
    just="Multi-source: the set joins every company's thread with the existing Contacts entries and the README rule.",
    ev="Sources: Leonard's email ('Get each company's contact into Contacts'), README f_846ddc38b2aab3d2ed3fcb ('only add a person "
       "who isn't in Contacts already (portals and no-reply senders don't get one)'); existing contacts a6ebc7683d450b0017b8acf3, "
       "35a52a2e3c634972639806b5, 8a7605bdc08105137d87f5a7. Accept: exactly 32 new contacts.", dec="F75 F8",
    grp="G6 contacts (volume row)", valid="32 contacts with the company in the job field", idle="No contact added")
for tag, co, why in [("ct_hoot", "Hootline", "Hootline's person is in an August thread with no filed paper"),
                     ("ct_rev", "Reviewly", "Hana is the onboarding contact in the Reviewly trial thread")]:
    name = ask(co)["from_name"]
    row(tag=tag, t=f"The Agent adds {name} to Contacts with {co} in the job field", w=3, kind="interpretation",
        why=f"{why}; the README puts the company in the job field", fact=f"contact_{co.lower()}", span=SP_HUB,
        oe=oe(f"co:{co}", f"w:contact:{co}"), fids=F(f"co:{co}", "readme"), vals=f"`{name}` `{co}` `{P(co)}`",
        verify=f"{name} contact", final="Contacts entry", acc=[f"a new contact named {name} whose job field names {co}"],
        alt="A contact without the company in the job field fails; the email field is optional.", srcs=[s_co(co, "from_name"), s_readme],
        just=f"Interpretation: the person from the {co} thread with the README's job rule.",
        ev=f"Sources: {co} thread {IDS['threads'][co]} (from {name}, {P(co)}), README f_846ddc38b2aab3d2ed3fcb ('Put the company in "
           f"the job field'). Accept: a new contact {name} with {co} in the job field.", dec="C7 F51" if co == "Hootline" else "F37",
        grp="G6 contacts", valid=f"{name}, {P(co)}, job {co}", idle="No contact added")

# ================================================================ D6 · reminders
row(tag="rem_count", t="The Agent creates exactly 14 reminder events on Frederick's calendar dated Mon Jan 5, 2026, one per company",
    w=5, kind="multi-source", why="a volume count: the 12 Park companies plus the two 'later' answers (Lanternfly Publishing in "
    "Leonard's DM, Balancy in the base thread), on the review date from the calendar", fact="reminders_count", span=SP_REM,
    oe=oe("review", "w:rem:*"), fids=F("review", "guardrails"), vals="`14` `2026-01-05`", verify="Number of Jan 5 reminders",
    final="Events on Frederick's calendar on 2026-01-05", acc=["14 events on Jan 5, 2026, one per company, any time that day"],
    alt="One listing event, 11 events (Framewell, Lanternfly and Balancy missing) or a different day fails.", srcs=[s_review, s_guard],
    dates=REM_DATES,
    just="Multi-source: the returning set joins Slack (Framewell waiver, Lanternfly DM), the base Balancy thread and every Park "
         "decision, on the date from the calendar.",
    ev="Sources: review event evt_fd469c29811879519c2c96 ('Q4 commitments review', starts 2026-01-05T17:00Z = Mon Jan 5 9:00 AM "
       "PST), guardrails f_b98287f6f80fe431a71209 steps 1 and 5. Accept: exactly 14 events dated Jan 5, 2026, one per company.",
    dec="C2 C3 C7 F12", grp="G7 reminders (volume row)", valid="14 all-day events on Jan 5, 2026", idle="No event created")
for tag, co, src, fid, dec, why in [
        ("rem_fw", "Framewell", s_waiver, F("waiver", "review"), "C2 F22", "Framewell comes back only because of Leonard's waiver reply"),
        ("rem_lf", "Lanternfly Publishing", s_lfdm, F("lf_dm", "review"), "C3 F24", "Leonard's DM answer was later ('we'll pick it up "
         "again in January'), so it comes back at the review"),
        ("rem_hoot", "Hootline", s_co("Hootline"), F("co:Hootline", "review"), "C7 F51", "Hootline's promo is free until Jan 31, 2026 "
         "(Park); its thread is from August")]:
    row(tag=tag, t=f"The Agent creates a reminder event on Frederick's calendar dated Mon Jan 5, 2026 that names {co}", w=5,
        kind="multi-source", why=f"{why}; the date is the review on the calendar", fact=f"reminder_{co.split()[0].lower()}",
        span=SP_REM, oe=oe(f"w:rem:{co}") + (oe("waiver") if co == "Framewell" else oe("lf_dm") if co.startswith("Lantern") else oe("co:Hootline")),
        fids=fid, vals=f"`{co}` `2026-01-05`", verify=f"{co} reminder", final="Event on Frederick's calendar on 2026-01-05",
        acc=[f"an event on Jan 5, 2026 whose title or description names {co}"], alt="An event on another day, or one listing "
        "event for every company, fails this per-company row.", srcs=[src, s_review], dates=REM_DATES,
        just=f"Multi-source: {why}, and the review date comes from the calendar.",
        ev=f"Sources: {src['id']} (the record that brings {co} back), review event evt_fd469c29811879519c2c96 (Mon Jan 5, 2026). "
           f"Accept: an event dated Jan 5, 2026 on Frederick's calendar whose title or description names {co}.", dec=dec,
        grp="G7 reminders", valid=f"All-day event 'Q4 review: {co}' on Jan 5, 2026", idle="No event created")

# ================================================================ D7 · reply to Leonard
row(tag="reply_thread", t="The Agent replies to Leonard (leonard.hayes@harmonygames.co) on his Sep 30 email \"Vendor and partner "
    "stuff while I'm in LA\" (a reply or reply-all on that thread)", w=1, kind="lookup", why="direct: the prompt names the email",
    fact="reply_delivery", span=SP_REPLY, oe=oe("hub", "w:hub"), fids=F("hub"), vals="Leonard's address leonard.hayes@harmonygames.co · thread `1844732913254784171`",
    verify="Reply on the hub thread", final="Sent reply in thread frederick.stone@harmonygames.co/1844732913254784171",
    acc=["a reply or reply-all on that thread to leonard.hayes@harmonygames.co"],
    alt="A new email outside the thread or a draft fails: the prompt says 'reply to Leonard on his email'.", srcs=[s_hub],
    just="Lookup: the prompt names the email ('reply to Leonard on his email').",
    ev="Source: Leonard's email thread frederick.stone@harmonygames.co/1844732913254784171 ('Vendor and partner stuff while I'm in "
       "LA'). Accept: a sent reply or reply-all on that thread.", dec="F1", grp="—", valid="A reply on the thread",
    idle="No reply sent")
row(tag="reply_keep_count", t="The Agent's reply to Leonard names exactly three companies as what we're keeping", w=5,
    kind="multi-source", why="a volume count: Keep needs Arthur's Trello keep-running card matched to each company's mail "
    "(the night pager is Pingwise)", fact="reply_keep_count", span=SP_REPLY, oe=oe("keepcard", "w:hub"), fids=F("hub", "keepcard"),
    vals="`3`", verify="Number of kept companies in the reply", final="Keeping list in the reply",
    acc=["three companies named as kept"], alt="Two (Pingwise missed) or four fails.", srcs=[s_hub, s_board],
    just="Multi-source: the keep set joins the Trello card with three companies' Gmail threads.",
    ev="Sources: Leonard's email ('reply here with what we're keeping'), keep-running card on board 640643a3fd8f3ca308d9318e "
       "('Vaultline nightly DB backups', 'Certwell SSL cert for the API domain', 'the night pager for backend outages'). Accept: "
       "exactly three companies named as kept.", dec="C4 F10", grp="G8 reply keep list (volume row)",
    valid="Keeping: Vaultline, Certwell, Pingwise", idle="No reply sent")
row(tag="reply_pingwise", t="The Agent's reply to Leonard lists Pingwise among what we're keeping", w=5, kind="multi-source",
    why="the keep-running card says 'the night pager for backend outages', not Pingwise; Pingwise's mail ties its phone and SMS "
    "paging to it", fact="reply_pingwise", span=SP_REPLY, oe=oe("keepcard", "co:Pingwise", "w:hub"), fids=F("co:Pingwise", "keepcard"),
    vals="`Pingwise` · kept", verify="Pingwise in the keeping list", final="Keeping list in the reply",
    acc=["Pingwise named as kept"], alt="Pingwise listed as ended or parked fails.", srcs=[s_co("Pingwise"), s_board],
    just="Multi-source: the Trello card's alias resolved through Pingwise's Gmail thread.",
    ev="Sources: Pingwise thread frederick.stone@harmonygames.co/1844157874176168845 ('phone and SMS paging keep working for your "
       "on-call rota'), keep-running card on board 640643a3fd8f3ca308d9318e. Accept: Pingwise among the kept companies.",
    dec="C4 F10", grp="G8 reply keep list", valid="Keeping: Pingwise (the night pager)", idle="No reply sent",
    dist="T: 'night pager' names no vendor")
row(tag="reply_sign_count", t="The Agent's reply to Leonard names exactly seven companies as waiting on Arthur or Leonard to sign",
    w=5, kind="multi-source", why="a volume count over every Sign decision, including Nintendo from Linear and excluding the "
    "already-answered Lanternfly", fact="reply_sign_count", span=SP_REPLY, oe=oe("esg", "w:hub"), fids=F("hub", "esg"), vals="`7`",
    verify="Number of companies waiting to sign in the reply", final="Sign list in the reply",
    acc=["seven companies named as waiting to sign"], alt="Six or eight fails.", srcs=[s_hub, s_ack],
    just="Multi-source: the Sign set joins Linear, Slack and each company's paper.",
    ev="Sources: Leonard's email ('what's waiting on Arthur or me to sign'), Leonard's reply under ESG's note thread "
       "frederick.stone@harmonygames.co/1844177063117059830. Accept: exactly seven companies named as waiting to sign.",
    dec="C1 C3 F4", grp="G9 reply sign list (volume row)", valid="Waiting to sign: seven companies", idle="No reply sent")
row(tag="reply_markward", t="The Agent's reply to Leonard lists Markward among what's waiting on Arthur or Leonard to sign", w=5,
    kind="multi-source", why="Leonard's July Slack note would let Fred accept free terms himself; his Sep 25 reply under ESG's "
    "note replaces it and click-through terms need an officer", fact="reply_markward", span=SP_REPLY,
    oe=oe("co:Markward", "esg", "w:hub"), fids=F("co:Markward", "esg"), vals="`Markward` · waiting to sign", verify="Markward in the sign list",
    final="Sign list in the reply", acc=["Markward named as waiting to sign"],
    alt="Markward reported as accepted by Fred, or left out, fails.", srcs=[s_esg, s_co("Markward")],
    just="Multi-source: Markward's thread, ESG's note and the superseded July Slack note.",
    ev="Sources: ESG note thread frederick.stone@harmonygames.co/1844177063117059830 ('That includes click-through terms'; Leonard: "
       "'This replaces what I said in July'), Markward thread frederick.stone@harmonygames.co/1842802694553769659. Accept: "
       "Markward among the companies waiting to sign.", dec="F49 F4 F14", grp="G9 reply sign list", valid="Waiting to sign: Markward",
    idle="No reply sent", dist="T: the July 'under $500' note")

# ================================================================ Process · the reply comes last
ORDER = [("order_log", "log sheet writes", "creating, copying or moving the log sheet, or writing its rows", oe("w:create", "w:rows", "w:move")),
         ("order_answers", "written answers to the companies", "replies or new emails to the companies, billing@paylane.io included", oe("w:paylane", "w:ans:*")),
         ("order_esg", "ESG Law intake emails", "emails to ESG Law intake (PERSON_2599_EMAIL)", oe("w:esg:*")),
         ("order_cards", "new cards in the To Do list of the Harmony Games board", "creating cards in that list", oe("w:card:*")),
         ("order_contacts", "new contacts in Contacts", "adding contacts to Contacts", oe("w:contact:*")),
         ("order_reminders", "Jan 5, 2026 reminder events on Frederick's calendar", "creating events dated Jan 5, 2026 on that calendar", oe("w:rem:*"))]
for tag, what, kinds, oes in ORDER:
    row(tag=tag, t=f"The Agent sends its reply to Leonard only once its {what} are finished: {kinds} (at least one comes before the "
        "reply and none after it)", w=1, cat="Process", kind="lookup", why="one ordering condition read from the prompt's 'When it's all done, "
        f"reply to Leonard'; {what} are one write action", fact=tag, span=SP_REPLY, oe=oes + oe("w:hub"), fids=F("hub"),
        vals="`1844732913254784171` · prompt order: When it's all done", verify=f"Order: reply after the {what}", final=f"Order of the reply and the {what}",
        acc=[f"at least one of the {kinds} before the reply and none of them after it"],
        alt=f"A reply sent before any of the {kinds}, or any of them after the reply, fails.", srcs=[s_hub],
        just="Lookup: the prompt says 'When it's all done, reply to Leonard'; no Outcome row can show the order.",
        ev=f"Source: the prompt ('When it's all done, reply to Leonard on his email'); Leonard's email thread "
           f"frederick.stone@harmonygames.co/1844732913254784171. Accept: at least one of the {kinds} before the reply, and none "
           "after it.", dec="F1", grp="—", valid=f"{what.capitalize()} first, then the reply", idle="No reply sent")

# ================================================================ pre-/rubric review fixes (check mode, 2026-11-04)
# rows added for coverage the independent review found missing
row(tag="log_type", t="The Agent creates the vendor and partner log as a native Google Sheet", w=1, kind="lookup",
    why="direct: Leonard's email asks for 'a sheet' and the README says 'One sheet'", fact="log_type", span=SP_LOG,
    oe=oe("readme", "w:create"), fids=F("readme"), vals="`Google Sheet` · native", verify="Log file type",
    final="Drive file mimeType of the log", acc=["a native Google Sheet (created or copied from the template)"],
    alt="An uploaded xlsx or csv, or a Google Doc, fails.", srcs=[s_readme],
    just="Lookup: Leonard's email says 'Log it all in a sheet' and the README 'One sheet for the vendor and partner backlog'.",
    ev="Sources: Leonard's email thread frederick.stone@harmonygames.co/1844732913254784171 ('Log it all in a sheet'), README "
       "f_846ddc38b2aab3d2ed3fcb ('One sheet for the vendor and partner backlog, one row per company on it'). Accept: a native "
       "Google Sheet, created or copied from template f_05f0a451b29b19a1c0b90f.", dec="F8", valid="The template copied as a Google Sheet",
    idle="No log sheet exists")
row(tag="log_name", t="The Agent names the log sheet \"Q4 commitments log\" (any letter case or spacing)", w=1, kind="lookup",
    why="direct: one line in the folder README", fact="log_name", span=SP_LOG, oe=oe("readme", "w:create"), fids=F("readme"),
    vals="`Q4 commitments log`", verify="Log file name", final="Drive file name of the log",
    acc=["Q4 commitments log", "Q4 Commitments Log"], alt="Another name fails: the README fixes it ('Name it \"Q4 commitments log\"').",
    srcs=[s_readme], just="Lookup: the README says 'Name it \"Q4 commitments log\"'.",
    ev="Source: README f_846ddc38b2aab3d2ed3fcb ('Name it \"Q4 commitments log\"'). Accept: Q4 commitments log in any letter case or spacing.",
    dec="F8", valid="A sheet named 'Q4 commitments log'", idle="No log sheet exists")
for tag, co, say, acc, step, fact in [
        ("ans_certwell", "Certwell", "that Harmony Games is staying on and renewing Certwell's certificate for the API domain",
         "staying on, keeping or renewing the certificate", "3 ('Tell them we're staying')", "certwell_answer"),
        ("ans_retainly", "Retainly", "that Harmony Games will pick Retainly up in January",
         "picking it up or deciding in January", "5 ('Tell them we'll pick it up in January')", "retainly_answer"),
        ("ans_bundle", "Bundlehouse", "that Bundlehouse's participation agreement goes to Harmony Games's lawyers first, then to "
         "Leonard or Arthur to sign", "with our lawyers (counsel, legal or ESG) first, then Leonard or Arthur",
         "4 ('with our lawyers first when ESG has to see it')", "bundlehouse_answer")]:
    name = ask(co)["from_name"]
    row(tag=tag, t=f"The Agent tells {name} ({P(co)}) in writing {say}", w=5, kind="multi-source",
        why=f"the answer follows from {co}'s decision, which joins its thread and paper with the guardrails (step {step})",
        fact=fact, span=SP_HUB, oe=oe(f"co:{co}", f"w:ans:{co}"), fids=F(f"co:{co}", "guardrails"), vals=f"`{P(co)}` `{co}`",
        verify=f"Answer to {name}", final=f"Sent email to {P(co)}",
        acc=[f"a reply on the {co} thread or a new email to {P(co)} saying {acc}"],
        alt="A generic acknowledgement that states no decision fails.", srcs=[s_co(co), s_guard],
        just=f"Multi-source: the content of the answer is the decision, read from {co}'s thread and paper against the guardrails.",
        ev=f"Sources: {co} thread {IDS['threads'][co]} ({name}, {P(co)}), paper {IDS['papers'][co]}, guardrails "
           f"f_b98287f6f80fe431a71209 step {step}. Accept: a sent reply or new email to {P(co)} saying {acc}.",
        dec=FID[f"co:{co}"], grp="G3 written answers", valid=f"A reply to {name}: {acc}", idle="No email sent")
row(tag="rev_cancel", t="The Agent cancels the Reviewly trial in writing to Hana Kobayashi (PERSON_9708_EMAIL) before it moves to the "
    "paid Growth plan on Oct 20, 2025", w=5, kind="multi-source", why="the trial turns paid inside Oct 1 to Dec 31 (step 2) and the "
    "terms say to cancel 'in the app or by email to your onboarding contact', who is Hana", fact="reviewly_cancellation", span=SP_ALL,
    oe=oe("co:Reviewly", "w:ans:Reviewly"), fids=F("co:Reviewly", "guardrails"), vals="`PERSON_9708_EMAIL` `Reviewly`",
    verify="Reviewly cancellation", final="Sent email to PERSON_9708_EMAIL", acc=["a reply or new email to PERSON_9708_EMAIL that cancels the trial"],
    alt="A reply that only thanks Hana, or a decline that leaves the trial running, fails.", srcs=[s_paper("Reviewly"), s_co("Reviewly")],
    just="Multi-source: the trial terms (Drive) give the paid date and the cancel route; the thread (Gmail) names Hana as the "
         "onboarding contact; the guardrails say to cancel in writing.",
    ev="Sources: trial terms f_4bdfb8e0c47288087c7bba ('After the trial the account moves to Growth at $79/month on Oct 20, 2025 "
       "unless cancelled by Oct 19, 2025'; 'Cancel: in the app or by email to your onboarding contact'), Reviewly thread "
       "frederick.stone@harmonygames.co/1843712439092112354 (Hana Kobayashi, 'your onboarding contact'). Accept: a sent email to "
       "PERSON_9708_EMAIL that cancels the trial.", dec="F37 F2", grp="G3 written answers", valid="A reply to Hana cancelling the trial",
    idle="No email sent")
row(tag="esg_kinetic", t="The Agent sends ESG Law intake (PERSON_2599_EMAIL) an intake email of its own about Kinetic Arcade's letter "
    "of intent, giving its 12-month exclusivity for Japan and Korea", w=5, kind="multi-source",
    why="the exclusivity is the ESG trigger, and the checklist asks for 'any exclusivity or licence of our IP'", fact="esg_kinetic",
    span=SP_ALL, oe=oe("co:Kinetic Arcade", "checklist", "w:esg:Kinetic Arcade"), fids=F("co:Kinetic Arcade", "checklist", "esg"),
    vals="`PERSON_2599_EMAIL` `Kinetic Arcade` `12 months`", verify="Kinetic Arcade intake email",
    final="Sent email to PERSON_2599_EMAIL about Kinetic Arcade",
    acc=["an email to PERSON_2599_EMAIL about Kinetic Arcade alone that states the 12-month exclusivity"],
    alt="An email without the exclusivity, or one email covering several agreements, fails.", srcs=[s_check, s_paper("Kinetic Arcade")],
    just="Multi-source: the LOI's exclusivity (Drive) against ESG's trigger list (Gmail) and the checklist (Docs).",
    ev="Sources: LOI f_6252955f500f81e3aacbef ('Exclusivity: 12 months from signature for those territories'), checklist "
       "f_3b06917a41dd59308d890b ('any exclusivity or licence of our IP'). Accept: a sent email to PERSON_2599_EMAIL about Kinetic "
       "Arcade alone that gives the 12-month exclusivity.", dec="F45 F5", grp="G4 ESG intake", valid="Intake email: Kinetic Arcade, "
       "12-month exclusivity, Japan and Korea, by Oct 20", idle="No email sent")
row(tag="esg_lumen_date", t="The Agent gives Oct 31, 2025 as the date it is needed by (any date form) in its intake email to ESG Law "
    "intake (PERSON_2599_EMAIL) about Lumencloud", w=5, kind="multi-source", why="the checklist asks for 'the date they need it "
    "by', which only the agreement and Aiden's mail give", fact="esg_lumencloud_date", span=SP_ALL,
    oe=oe("co:Lumencloud", "checklist", "w:esg:Lumencloud"), fids=F("co:Lumencloud", "checklist"),
    vals="`PERSON_2599_EMAIL` `Lumencloud` `Oct 31, 2025`", verify="Needed-by date in the Lumencloud intake email",
    final="Sent email to PERSON_2599_EMAIL about Lumencloud", acc=["Oct 31, 2025 in any date form"],
    alt="An intake email without a needed-by date, or another date, fails.", srcs=[s_check, s_paper("Lumencloud")],
    just="Multi-source: the agreement's deadline (Drive) placed into the checklist's item (Docs) on the ESG email.",
    ev="Sources: agreement f_a227b14f03e12005fe8324 ('Sign by Oct 31, 2025 (cohort closes)'), checklist f_3b06917a41dd59308d890b "
       "('the date they need it by'). Accept: Oct 31, 2025 in any date form in the Lumencloud intake email.", dec="F46 F5",
    grp="G4 ESG intake", valid="Intake email: needed by Oct 31, 2025", idle="No email sent")

# title rewrites: the Agent plus an action (Agent-Centric), name forms in the title, one item per write
NAMEFORM = {"Nintendo": "Nintendo (or Nintendo Developer Portal)", "Lanternfly Publishing": "Lanternfly Publishing (or Lanternfly)",
            "Pixel Harbor Events": "Pixel Harbor Events (or Pixel Harbor)"}
TITLES = {
    "log_folder": "The Agent puts the vendor and partner log in Frederick's Drive folder \"Q4 commitments\" (created there, copied "
                  "there or moved there)",
    "log_header": "The Agent gives its log sheet the column headings Company, Contact, What's waiting, Decision, Answered by, What we "
                  "told them and Next date, in that order (any letter case)",
    "log_rows": "The Agent writes exactly 36 company rows below the header of its log sheet, one row per company",
    "nin_decision": f"The Agent gives {NAMEFORM['Nintendo']} the Decision \"Sign\" in its log sheet",
    "fw_decision": "The Agent gives Framewell the Decision \"Park\" in its log sheet",
    "lf_decision": f"The Agent gives {NAMEFORM['Lanternfly Publishing']} the Decision \"Answered\" in its log sheet",
    "sp_decision": "The Agent gives Spotlight Fest the Decision \"Answered\" in its log sheet",
    "lf_by": f"The Agent puts Leonard (or Leonard Hayes) in the Answered by column of the {NAMEFORM['Lanternfly Publishing']} row of its log sheet",
    "sp_by": "The Agent puts Robert in the Answered by column of the Spotlight Fest row of its log sheet",
    "bal_by": "The Agent puts Leonard (or Leonard Hayes) in the Answered by column of the Balancy row of its log sheet",
    "mf_by": "The Agent puts Arthur (or Arthur Blake) in the Answered by column of the Motive Forge row of its log sheet",
    "nin_next": f"The Agent gives {NAMEFORM['Nintendo']} the Next date Oct 15, 2025 (any date form) in its log sheet",
    "cf_next": "The Agent gives Clipforge the Next date Oct 15, 2025 (any date form) in its log sheet",
    "ph_next": f"The Agent gives {NAMEFORM['Pixel Harbor Events']} the Next date Oct 10, 2025 (any date form) in its log sheet",
    "pw_next": "The Agent gives Pingwise the Next date Nov 1, 2025 (any date form) in its log sheet",
    "ph_told": f"The Agent records in the What we told them column of its log sheet that {NAMEFORM['Pixel Harbor Events']} was "
               "turned down (declined, said no or passed; any wording with that meaning)",
    "lf_told": f"The Agent records in the What we told them column of its log sheet that {NAMEFORM['Lanternfly Publishing']} was "
               "told Southeast Asia has to wait until after the raise (any wording with that meaning)",
    "sv_told": "The Agent records in the What we told them column of its log sheet that Soundvault was turned down (declined, said "
               "no or passed; any wording with that meaning)",
    "kin_told": "The Agent records in the What we told them column of its log sheet that Kinetic Arcade was told its letter of "
                "intent goes to our lawyers first (counsel, legal or ESG)",
    "ww_told": "The Agent records in the What we told them column of its log sheet that Wishwave was turned down (declined, said no "
               "or passed; any wording with that meaning)",
    "cf_cancel": "The Agent emails billing@paylane.io to cancel Clipforge's UGC Studio plan on workspace HG-2291 before it starts "
                 "(naming the workspace, UGC Studio or Clipforge)",
    "ans_orbit": "The Agent tells Mateo Rossi (PERSON_9719_EMAIL) in writing that Orbit Store's featuring agreement is with Leonard "
                 "or Arthur to sign or accept",
    "esg_lumen": "The Agent sends ESG Law intake (PERSON_2599_EMAIL) an intake email of its own about the Lumencloud Startup Program "
                 "Agreement, giving its 36-month term",
    "esg_bundle": "The Agent sends ESG Law intake (PERSON_2599_EMAIL) an intake email of its own about Bundlehouse's participation "
                  "agreement, saying it licenses Harmony Games's IP (the game's name, logo and art, or our IP in general)",
    "card_nin": "The Agent creates a card in the To Do list of the Harmony Games Trello board with Nintendo as the only company in its title",
    "card_kin": "The Agent creates a card in the To Do list of the Harmony Games Trello board with Kinetic Arcade as the only company "
                "in its title",
    "card_mark": "The Agent creates a card in the To Do list of the Harmony Games Trello board with Markward as the only company in its title",
    "rem_fw": "The Agent creates a reminder event on Frederick's calendar dated Mon Jan 5, 2026 that names Framewell as its only "
              "company (in its title or description)",
    "rem_lf": f"The Agent creates a reminder event on Frederick's calendar dated Mon Jan 5, 2026 that names {NAMEFORM['Lanternfly Publishing']} "
              "as its only company (in its title or description)",
    "rem_hoot": "The Agent creates a reminder event on Frederick's calendar dated Mon Jan 5, 2026 that names Hootline as its only "
                "company (in its title or description)",
    "reply_keep_count": "The Agent names exactly three companies as what we're keeping in its reply to Leonard",
    "reply_pingwise": "The Agent lists Pingwise among what we're keeping in its reply to Leonard",
    "reply_sign_count": "The Agent names exactly seven companies as waiting on Arthur or Leonard to sign in its reply to Leonard",
    "reply_markward": "The Agent lists Markward among what's waiting on Arthur or Leonard to sign in its reply to Leonard",
}
BYTAG = {r["tag"]: r for r in R}
for tag, t in TITLES.items():
    BYTAG[tag]["t"] = t
for tag in ("bal_by", "mf_by", "ph_next", "ph_told", "sv_told", "ans_orbit", "card_kin", "ct_hoot", "ct_rev"):
    r = BYTAG[tag]
    r["w"], r["kind"] = 5, "multi-source"
    r["just"] = "Multi-source: " + r["just"].split(": ", 1)[1].rstrip(".") + ", joining the company's own records with the rule doc in another service."
for tag in ("rem_fw", "rem_lf", "rem_hoot"):
    BYTAG[tag]["acc"] = [a + ", as an event of its own for that company" for a in BYTAG[tag]["acc"]]
    BYTAG[tag]["alt"] = "One combined event listing several companies, or an event on another day, fails this per-company row."
for tag in ("card_nin", "card_kin", "card_mark"):
    BYTAG[tag]["alt"] = "One combined card naming several companies, a card in Doing or Backlog, or a title without the company, fails."

# ================================================================ platform /rubric round 1 (FAIL 1, 2026-11-05): the Fix List
# run_forensics/rev4/rubric_r1/platform_rubric_review_r1.md. Every row below follows the Fix List's text; the two rows it
# left for the author (Dana Whitfield's Pingwise answer, the Lumencloud cost line) are written here.
def thread_text(k):
    return "\n".join(x["row"]["body_text"] for x in SQL if x["table"] == "gmail.gmail_messages" and x["op"] == "insert"
                     and x["row"].get("thread_id") == IDS["threads"][k] and x["row"].get("user_email") == FRED)


def paper_text(k):
    pid = IDS["papers"][k]
    return "\n".join(str(x["row"].get(c) or "") for x in SQL if x["op"] == "insert" and pid in json.dumps(x["row"])
                     for c in ("body_text", "text", "name", "title"))


def q(text, s):
    assert s in text, s
    return s


GUARD_T = sql_row("gdocs.docs_documents", {"document_id": GUARD[1]})["body_text"]
CHECK_T = sql_row("gdocs.docs_documents", {"document_id": CHECK[1]})["body_text"]
README_T = sql_row("gdocs.docs_documents", {"document_id": README[1]})["body_text"]
ESG_TXT = sql_row("gmail.gmail_messages", {"id": IDS["msg"]["esg_note"]})["body_text"]
ON_HUB = "in its reply on Leonard's \"Vendor and partner stuff while I'm in LA\" email"
NO_MEANING = "any wording with that meaning"


def retitle(tag, t, **k):
    BYTAG[tag]["t"] = t
    BYTAG[tag].update(k)


# --- R1: the folder row no longer repeats the file-type check
retitle("log_folder", "The Agent puts the vendor and partner log in Frederick's Drive folder \"Q4 commitments\" (created there or "
        "moved there)", acc=["the Agent's log whose final parent is the Q4 commitments folder, created there or moved there"],
        ev="Source: folder 'Q4 commitments' d_80a8c04753ba82ba4ba6a5 (owner Frederick). Accept: the Agent's log whose final parent "
           "is that folder, whether created there or moved there.")
# --- weight 5 → 3: one rule applied to one thread or paper (interpretation)
for tag, just in [
        ("bal_by", "Interpretation: one base thread read against guardrails step 1; Leonard's Sep 11 'we'll circle back with you as "
                   "soon as we get some bandwidth' is an answer that says later."),
        ("mf_by", "Interpretation: one thread read against guardrails step 1; Arthur's Sep 19 reply to Hugo already passed on the quote."),
        ("ph_next", "Interpretation: the June quote's deposit date read as the last day to say no (README End rule); Frederick's 'I'll "
                    "come back to you on this' is a holding reply."),
        ("ph_told", "Interpretation: the booth quote's deposit before January fails the cash test (guardrails step 2), so the answer "
                    "is a decline."),
        ("sv_told", "Interpretation: a licence paid in full on signature before Oct 15 fails the cash test (guardrails step 2)."),
        ("ans_orbit", "Interpretation: one thread read against guardrails step 4 ('Tell them it's with Leonard or Arthur to sign'); "
                      "Mateo writes himself, so the portal line does not apply."),
        ("ans_retainly", "Interpretation: one thread read against guardrails step 5; the trial is free until Jan 12, so it is Park."),
        ("rev_cancel", "Interpretation: one paper read against guardrails step 2; the trial turns paid on Oct 20, and the terms say to "
                       "cancel by email to the onboarding contact, Hana."),
        ("card_kin", "Interpretation: the LOI's 'Signature needed by Oct 20, 2025' read against guardrails step 4.")]:
    BYTAG[tag].update(w=3, kind="interpretation", just=just)
# --- weight 5 → 1: a date or a contact read straight off one record
BYTAG["esg_lumen_date"].update(w=1, kind="lookup", just="Lookup: one date copied from the Lumencloud agreement ('Sign by Oct 31, "
                               "2025') into the intake email the checklist describes.")
for tag, co in (("ct_hoot", "Hootline"), ("ct_rev", "Reviewly")):
    name, em = ask(co)["from_name"], P(co)
    retitle(tag, f"The Agent adds {name} ({em}) to Contacts with {co} in the job field", w=1, kind="lookup",
            acc=[f"one new contact for {name} with the email {em} and {co} in the job field"],
            alt="A contact with no email, the wrong email or no company in the job field fails.",
            just=f"Lookup: the name and address come straight from the {co} thread; the README puts the company in the job field.",
            ev=f"Sources: {co} thread {IDS['threads'][co]} (from {name}, {em}), README f_846ddc38b2aab3d2ed3fcb ('Put the company in "
               f"the job field'). Accept: one new contact {name} with the email {em} and {co} in the job field.")
# --- R24, R25, R27, R28: titles and evidence say the same thing
BYTAG["cf_cancel"]["ev"] = ("Source: Paylane notice thread frederick.stone@harmonygames.co/1843067564852153540 ('To cancel before the "
                            "plan starts, write to billing@paylane.io by Oct 15. Replies to this email aren't monitored.'); pilot "
                            "agreement f_8d0e0e3ae076b2f745e7e2. Accept: a sent email to billing@paylane.io that cancels the plan, "
                            "naming workspace HG-2291, UGC Studio or Clipforge.")
retitle("cf_priya", "The Agent tells Priya Raman (PERSON_9704_EMAIL) in writing that Harmony Games is ending the Clipforge pilot "
        "(ending the pilot or not carrying on after it)",
        acc=["a reply on Priya's thread or a new email to PERSON_9704_EMAIL saying Harmony Games is ending the pilot or not carrying "
             "on after it"],
        alt="An email that only says the pilot ends (a fact, not our decision), or only the billing cancellation, fails.",
        ev="Sources: Clipforge thread frederick.stone@harmonygames.co/1837102635418059486, Priya Raman, Sep 22 ('If you're not "
           "carrying on after the pilot, let me know here too'); Paylane notice thread "
           "frederick.stone@harmonygames.co/1843067564852153540. Accept: a reply or new email to PERSON_9704_EMAIL saying Harmony "
           "Games is ending the pilot or not carrying on after it.")
for tag, co, say, acc, step in [
        ("ans_certwell", "Certwell", "Harmony Games is staying with Certwell for the API domain certificate (staying on, keeping it "
         "or confirming the renewal)", "Harmony Games is staying on, keeping the certificate or confirming the renewal",
         "3 ('Tell them we're staying.')"),
        ("ans_retainly", "Retainly", "Harmony Games will pick Retainly up in January (picking it up, revisiting it or deciding in "
         "January)", "Harmony Games will pick it up, revisit it or decide in January", "5 ('Tell them we'll pick it up in January')")]:
    name, em = ask(co)["from_name"], P(co)
    retitle(tag, f"The Agent tells {name} ({em}) in writing that {say}",
            acc=[f"a reply on the {co} thread or a new email to {em} saying {say}"],
            ev=f"Sources: {co} thread {IDS['threads'][co]} ({name}, {em}), paper {IDS['papers'][co]}, guardrails "
               f"f_b98287f6f80fe431a71209 step {step}. Accept: a sent reply or new email to {em} saying {say}.")
# --- R29 split: lawyers first (this row) and the signer (new row below)
name, em = ask("Bundlehouse")["from_name"], P("Bundlehouse")
retitle("ans_bundle", f"The Agent tells {name} ({em}) in writing that Bundlehouse's participation agreement goes to Harmony Games's "
        "lawyers first (counsel, legal or ESG)", acc=[f"a reply on the Bundlehouse thread or a new email to {em} saying Bundlehouse's "
        "participation agreement goes to Harmony Games's lawyers first (counsel, legal or ESG)"],
        just="Multi-source: the deck's IP licence (Slides) is an ESG trigger in ESG's note (Gmail), and guardrails step 4 says to "
             "tell them it is with our lawyers first.",
        ev=f"Sources: Bundlehouse thread {IDS['threads']['Bundlehouse']} ({name}, {em}), deck f_9d1e0270574584de0eb92c ('Bundlehouse "
           "may use your game's name, logo and art in bundle marketing for 18 months'), ESG note thread "
           "frederick.stone@harmonygames.co/1844177063117059830, guardrails f_b98287f6f80fe431a71209 step 4 ('with our lawyers first "
           f"when ESG has to see it'). Accept: a sent reply or new email to {em} saying Bundlehouse's participation agreement goes to "
           "Harmony Games's lawyers first (counsel, legal or ESG).")
# --- R31: one per agreement in the evidence
BYTAG["esg_count"]["ev"] = BYTAG["esg_count"]["ev"].replace("Accept: exactly three emails to PERSON_2599_EMAIL.",
                                                            "Accept: exactly three emails to PERSON_2599_EMAIL, one per agreement.")
assert "one per agreement." in BYTAG["esg_count"]["ev"]
# --- R32, R34, R35: '... about <agreement> alone', weight 1
ESG_TO = "in its intake email to ESG Law intake (PERSON_2599_EMAIL) about"
for tag, t, acc, just in [
        ("esg_lumen", f"The Agent gives the 36-month term {ESG_TO} the Lumencloud Startup Program Agreement alone",
         "the 36-month term (36 months or three years)", "Lookup: one term copied from the agreement ('Term: 36 months from signature')."),
        ("esg_bundle", "The Agent says the agreement licenses Harmony Games's IP (the game's name, logo and art, or our IP in general) "
         f"{ESG_TO} Bundlehouse's participation agreement alone", "that the agreement licenses our IP (name, logo and art, or IP in general)",
         "Lookup: one clause copied from the deck ('Bundlehouse may use your game's name, logo and art')."),
        ("esg_kinetic", f"The Agent gives the 12-month exclusivity {ESG_TO} Kinetic Arcade's letter of intent alone",
         "the 12-month exclusivity (12 months or one year)", "Lookup: one clause copied from the LOI ('Exclusivity: 12 months from "
         "signature').")]:
    co = {"esg_lumen": "Lumencloud", "esg_bundle": "Bundlehouse", "esg_kinetic": "Kinetic Arcade"}[tag]
    claim = t[len("The Agent "):t.index(" in its intake email")]
    retitle(tag, t, w=1, kind="lookup", acc=[f"an intake email to PERSON_2599_EMAIL about {co} alone in which the Agent {claim}"],
            alt="An email that omits it, or one email covering several agreements, fails.",
            just=just + " Which agreements go to ESG is graded by the volume row.",
            ev=BYTAG[tag]["ev"].split("Accept:")[0] + f"Accept: a sent intake email to PERSON_2599_EMAIL about {co} alone in which the "
               f"Agent {claim}.")
# --- R36, R40: the volume rows state the template
retitle("card_count", "The Agent creates exactly seven new cards in the To Do list of the Harmony Games Trello board, each with the "
        "name of the company it is for in its title", acc=["seven new cards in To Do, each naming its company in the title"],
        ev=BYTAG["card_count"]["ev"].replace("Accept: exactly seven new cards in that list.",
                                             "Accept: exactly seven new cards in that list, each with its company's name in the title."))
retitle("ct_count", "The Agent adds exactly 32 new contacts to Contacts, one per company (each company's contact), each with that "
        "person's company in the job field", acc=["32 new contacts, one per company, each with the company in the job field"],
        ev=BYTAG["ct_count"]["ev"].replace("Accept: exactly 32 new contacts.",
                                           "Accept: exactly 32 new contacts, one per company, each with that person's company in the job field."))
# --- R37–R39: a card of its own; R38 weight 3 (above)
for tag, co in (("card_nin", "Nintendo"), ("card_kin", "Kinetic Arcade"), ("card_mark", "Markward")):
    retitle(tag, f"The Agent creates a card of its own for {co} in the To Do list of the Harmony Games Trello board (its title names "
            f"{co} and no other company waiting to sign)",
            acc=[f"a new card in To Do whose title names {co} and no other company waiting to sign (ESG Law, Leonard or Arthur may appear)"],
            ev=BYTAG[tag]["ev"].split("Accept:")[0] + f"Accept: a new card in To Do whose title names {co} and no other company waiting "
               "to sign; a title that also names ESG Law, Leonard or Arthur passes.")
# --- R44–R46: a reminder of its own
for tag, co in (("rem_fw", "Framewell"), ("rem_lf", "Lanternfly Publishing"), ("rem_hoot", "Hootline")):
    nm = NAMEFORM.get(co, co)
    retitle(tag, f"The Agent creates a reminder event of its own for {nm} on Frederick's calendar dated Mon Jan 5, 2026 (naming {nm} "
            "and no other company from the vendor and partner backlog, in its title or description)",
            acc=[f"an event dated Jan 5, 2026 whose title or description names {nm} and no other backlog company"],
            ev=BYTAG[tag]["ev"].split("Accept:")[0] + f"Accept: an event dated Jan 5, 2026 on Frederick's calendar whose title or "
               f"description names {nm} and no other company from the backlog.")
# --- R48–R51: the reply rows name Leonard's thread (R47 removed below)
for tag, t in (("reply_keep_count", "The Agent names exactly three companies as what we're keeping"),
               ("reply_pingwise", "The Agent lists Pingwise among what we're keeping"),
               ("reply_sign_count", "The Agent names exactly seven companies as waiting on Arthur or Leonard to sign"),
               ("reply_markward", "The Agent lists Markward among what's waiting on Arthur or Leonard to sign")):
    retitle(tag, f"{t} {ON_HUB}", ev=BYTAG[tag]["ev"].replace("Accept: ", "Accept, in a sent reply or reply-all on thread "
                                                              "frederick.stone@harmonygames.co/1844732913254784171: "))

# --- new rows ---------------------------------------------------------------------------------------------------------
NEW = []


def add(**k):
    row(**k)
    NEW.append(k["tag"])


# log: five more samples (Decision Keep, Next date for a 'later' answer, Contact, What's waiting, when answered)
log_row("pw_decision", "Pingwise", "Decision", "Keep", "The Agent gives Pingwise the Decision \"Keep\" in its log sheet", 5,
        "multi-source", "the Team plan costs $29/month from Nov 1, but the keep-running card's 'night pager' is Pingwise's paging, "
        "the one exception to the cash test (guardrails step 3)", "pingwise_decision", [s_co("Pingwise"), s_board],
        F("co:Pingwise", "keepcard", "guardrails"), oe("keepcard", "co:Pingwise", "w:rows"), "C4 F10",
        "Sources: Pingwise thread frederick.stone@harmonygames.co/1844157874176168845 ('" + q(thread_text("Pingwise"), "phone and SMS "
        "paging keep working for your on-call rota") + "'), keep-running card on board 640643a3fd8f3ca308d9318e ('the night pager "
        "for backend outages'), guardrails f_b98287f6f80fe431a71209 step 3 ('" + q(GUARD_T, "The cash test has one exception") +
        "'). Accept: Decision 'Keep' on the Pingwise row.", ["Keep"], "End (from the $29/month) fails.", "Pingwise / Keep / 2025-11-01",
        dist="T: 'night pager' names no vendor")
NEW.append("pw_decision")
log_row("lf_next", "Lanternfly Publishing", "Next date", "2026-01-05", f"The Agent gives {NAMEFORM['Lanternfly Publishing']} the Next "
        "date Jan 5, 2026 (any date form) in its log sheet", 5, "multi-source", "Leonard's DM answer was later ('we'll pick it up "
        "again in January'), and the README gives 'later' answers the January review, whose date is on the calendar",
        "lanternfly_nextdate", [s_lfdm, s_review], F("lf_dm", "readme", "review"), oe("lf_dm", "readme", "review", "w:rows"), "C3 F24",
        "Sources: Leonard's DM reply D05S58U4SAK/1759174260.052645 ('we'll pick it up again in January'), README "
        "f_846ddc38b2aab3d2ed3fcb ('" + q(README_T, "for Park and for \"later\" answers, the January review") + "'), review event "
        "evt_fd469c29811879519c2c96 (starts 2026-01-05T17:00Z, Mon Jan 5 9:00 AM PST). Accept: Jan 5, 2026 in any date form.",
        ["2026-01-05", "Jan 5, 2026", "1/5/2026"], "A blank Next date, or Jan 31, fails.", "Lanternfly Publishing / Next date 2026-01-05")
R[-1]["dates"] = REM_DATES
NEW.append("lf_next")
log_row("rev_contact", "Reviewly", "Contact", "Hana Kobayashi", "The Agent puts Hana Kobayashi or her email PERSON_9708_EMAIL in the "
        "Contact column of the Reviewly row of its log sheet", 1, "lookup", "the contact is the sender of the Reviewly thread",
        "reviewly_contact", [s_co("Reviewly", "from_name")], F("co:Reviewly", "readme"), oe("co:Reviewly", "w:rows"), "F37",
        "Sources: Reviewly thread frederick.stone@harmonygames.co/1843712439092112354 (Hana Kobayashi, PERSON_9708_EMAIL: '" +
        q(thread_text("Reviewly"), "I'm Hana, your onboarding contact") + "'), README f_846ddc38b2aab3d2ed3fcb (the Contact column). "
        "Accept: Hana Kobayashi, Hana, or PERSON_9708_EMAIL in the Contact column of the Reviewly row.",
        ["Hana Kobayashi", "Hana", "PERSON_9708_EMAIL"], "A blank Contact cell fails.", "Reviewly / Contact: Hana Kobayashi")
NEW.append("rev_contact")
log_row("sv_waiting", "Soundvault", "What's waiting", "licence quote", "The Agent records in the What's waiting column of the "
        "Soundvault row of its log sheet Soundvault's licence quote (accepted: \"licence quote\", \"music licence\" or \"trailer pack "
        "quote\", in any wording)", 1, "lookup", "the open item is named on the filed paper", "soundvault_waiting",
        [s_paper("Soundvault")], F("co:Soundvault", "readme"), oe("co:Soundvault", "w:rows"), "F36",
        "Sources: Soundvault paper f_2686da1086bfcc2fba3f57 ('" + q(paper_text("Soundvault"), "Soundvault - Licence Quote - Harmony "
        "Games") + "'; '" + q(paper_text("Soundvault"), "Trailer music pack (40 tracks), annual licence") + "'), Soundvault thread "
        "frederick.stone@harmonygames.co/1842719647334876669. Accept: the licence quote, the music licence or the trailer pack quote, "
        "in any wording (licence or license).", ["licence quote", "music licence", "trailer pack quote"],
        "A blank What's waiting cell fails.", "Soundvault / What's waiting: trailer music licence quote")
NEW.append("sv_waiting")
log_row("mf_when", "Motive Forge", "any column", "2025-09-19", "The Agent records Sep 19, 2025 (any date form) as when Arthur answered "
        "Motive Forge's 3D art quote, in any column of the Motive Forge row of its log sheet", 3, "interpretation",
        "guardrails step 1 says to note who answered and when; Arthur's reply in the thread carries the date", "motiveforge_answered_on",
        [s_ar, s_guard], F("co:Motive Forge", "guardrails"), oe("co:Motive Forge", "w:rows"), "F63",
        "Sources: Motive Forge thread frederick.stone@harmonygames.co/1843346276352084348 (Arthur Blake, 2025-09-19T17:45Z = Fri Sep "
        "19, 10:45 AM PDT: '" + q(thread_text("Motive Forge"), "we're keeping the art in-house, so we'll pass on this one") + "'), "
        "guardrails f_b98287f6f80fe431a71209 step 1 ('" + q(GUARD_T, "Note who answered and when.") + "'). Accept: Sep 19, 2025 in "
        "any date form in any cell of the Motive Forge row.", ["2025-09-19", "Sep 19, 2025", "9/19/2025"],
        "No date on the Motive Forge row fails.", "Motive Forge / Answered by: Arthur, Sep 19")
R[-1]["just"] = "Interpretation: one thread read against guardrails step 1 ('Note who answered and when')."
NEW.append("mf_when")

# written answers: one row per recipient (rubric_flow_v2: content differs per target)
STEP = {2: ("2", q(GUARD_T, "say no, or cancel it in writing the way their paper or notice asks")),
        3: ("3", q(GUARD_T, "Tell them we're staying.")),
        4: ("4", q(GUARD_T, "Tell them it's with Leonard or Arthur to sign, and with our lawyers first when ESG has to see it.")),
        5: ("5", q(GUARD_T, "Tell them we'll pick it up in January"))}
END = [("ans_pixel", "Pixel Harbor Events", "Pixel Harbor Events' booth hold", 3, "I'm holding a 10x10 booth for Harmony Games"),
       ("ans_brightlane", "Brightlane Studio", "Brightlane Studio's creative retainer", 3, "We could start Oct 1."),
       ("ans_soundvault", "Soundvault", "Soundvault's trailer music licence", 3, "$1,188 paid up front when you sign"),
       ("ans_streamcast", "Streamcast Talent", "Streamcast Talent's November creator campaign", 3, "We take a 50% deposit when you book"),
       ("ans_lingora", "Lingora", "Lingora's store listing localization quote", 3, "12 languages for $2,640"),
       ("ans_panelpulse", "Panelpulse", "Panelpulse's Oct 14 player panel", 3, "It's $1,200 prepaid"),
       ("ans_ascendo", "Ascendo", "Ascendo's ASO retainer", 3, "$900/month starting Oct 1"),
       ("ans_wishwave", "Wishwave", "Wishwave's Seattle Indie Expo pre-registration push", 5, "you cover travel for two")]
PARK = [("ans_framewell", "Framewell", 5, "Pro starts Nov 1 at $149/month"),
        ("ans_hootline", "Hootline", 3, "keeps the account free until Jan 31, 2026"),
        ("ans_glyphworks", "Glyphworks", 3, "nothing is owed until you order"),
        ("ans_cloudlark", "Cloudlark", 3, "Nothing to do until you want to activate them."),
        ("ans_echohall", "Echohall", 3, "The free plan carries on as it is until then."),
        ("ans_pressbeam", "Pressbeam", 3, "you can book any time before launch"),
        ("ans_quillcraft", "Quillcraft", 3, "It's free through January, and pricing starts in February."),
        ("ans_tilecast", "Tilecast", 3, "a free pilot slot in February"),
        ("ans_benchmarkly", "Benchmarkly", 3, "The full set is a $300/month subscription from February"),
        ("ans_loopnote", "Loopnote", 3, "Your team trial is free until Feb 1."),
        ("ans_driftwood", "Driftwood Audio", 3, "The quote is good until Feb 28.")]


def answer(tag, co, say, acc, w, step, quote, why, srcs, fids, dec, extra="", alt="A generic acknowledgement that states no decision, "
           "or no email to this person, fails.", dist="—"):
    name, em = ask(co)["from_name"], P(co)
    kind = "multi-source" if w == 5 else "interpretation"
    n, sq = STEP[step]
    add(tag=tag, t=f"The Agent tells {name} ({em}) in writing that {say}", w=w, kind=kind, why=why, fact=f"{tag[4:]}_written_answer",
        span=SP_HUB, oe=oe(f"co:{co}", f"w:ans:{co}"), fids=fids, vals=f"`{em}` `{co}`", verify=f"Answer to {name}",
        final=f"Sent email to {em}", acc=[f"a reply on the {co} thread or a new email to {em} saying {say}"], alt=alt, srcs=srcs,
        just=f"{kind.capitalize()}: {why}.",
        ev=f"Sources: {co} thread {IDS['threads'][co]} ({name}, {em}: '{q(thread_text(co), quote)}'){extra}, guardrails "
           f"f_b98287f6f80fe431a71209 step {n} ('{sq}'). Accept: a sent reply on the {co} thread or a new email to {em} saying {say}.",
        dec=dec, grp="G3 written answers", valid=f"A reply to {name}: {acc}", idle="No email sent", dist=dist)


for tag, co, offer, w, quote in END:
    why = (f"the offer costs cash before January, so guardrails step 2 says to say no" if co != "Wishwave" else
           "the travel Wishwave books and bills counts as cash only after Leonard's Monday #executives change to the guardrails, "
           "so step 2 says to say no")
    srcs = [s_co(co), s_guard] if co != "Wishwave" else [s_co(co), s_amend]
    extra = (f", paper {IDS['papers'][co]}" if co != "Wishwave" else ", Leonard's Monday post C07C2866011/1759166100.370044 ('travel "
             "and event costs count as cash even when a partner books them and bills us')")
    answer(tag, co, f"Harmony Games is turning down {offer} (declining or saying no; {NO_MEANING})",
           f"Harmony Games is declining or saying no to {offer} ({NO_MEANING})", w, 2, quote, why, srcs,
           F(f"co:{co}", "guardrails") + (" " + F("amend") if co == "Wishwave" else ""), FID[f"co:{co}"] + (" F3" if co == "Wishwave" else ""),
           extra, alt="Parking it, a generic acknowledgement, or no email to this person fails.",
           dist="T: the guardrails doc's own 'only when we book them ourselves'" if co == "Wishwave" else "—")
for tag, co, w, quote in PARK:
    if co == "Framewell":
        why, srcs, extra = ("the order form bills from Nov 1, but Leonard's Sep 26 #executives thread reply says Maren holds Pro at no "
                            "charge until Feb 1, so step 5 applies", [s_co(co), s_waiver],
                            ", Leonard's thread reply C07C2866011/1758920520.674991 ('they'll hold it at no charge until Feb 1 with "
                            "nothing to sign before then')")
    else:
        why, srcs, extra = (f"{co}'s offer is free until January, so guardrails step 5 says to tell them we'll pick it up then",
                            [s_co(co), s_guard], f", paper {IDS['papers'][co]}" if co in IDS["papers"] else " (no filed paper)")
    answer(tag, co, f"Harmony Games will pick {co} up in January (picking it up, revisiting it or deciding in January)",
           "Harmony Games will pick it up, revisit it or decide in January", w, 5, quote, why, srcs,
           F(f"co:{co}", "guardrails") + (" " + F("waiver") if co == "Framewell" else ""), FID[f"co:{co}"] + (" C2 F22" if co == "Framewell" else ""),
           extra, alt="A decline, a generic acknowledgement, or no email to this person fails.",
           dist="T: the order form's Nov 1 billing" if co == "Framewell" else "—")
answer("ans_vaultline", "Vaultline", "Harmony Games is staying with Vaultline (keeping the nightly backups running)",
       "Harmony Games is staying with Vaultline or keeping the nightly backups running", 5, 3, "Can you confirm you want to keep them running?",
       "the $19/month renewal fails the cash test, but the nightly backups are on Arthur's keep-running card (guardrails step 3)",
       [s_co("Vaultline"), s_board], F("co:Vaultline", "keepcard", "guardrails"), "C4 F43",
       ", keep-running card on board 640643a3fd8f3ca308d9318e ('Vaultline nightly DB backups')",
       alt="Letting the backups stop, a generic acknowledgement, or no email to Mila fails.")
answer("ans_pingwise", "Pingwise", "Harmony Games is staying with Pingwise on the Team plan rather than dropping to the free plan ("
       f"staying on, going ahead with Team from Nov 1 or keeping the paging; {NO_MEANING})",
       "Harmony Games is staying with Pingwise on Team (staying on, going ahead with Team from Nov 1, or keeping the phone and SMS "
       "paging)", 5, 3, "If you'd rather drop back to the free plan, reply and I'll downgrade you before then.",
       "the Team plan's $29/month fails the cash test, but the keep-running card's 'night pager' is Pingwise's paging (guardrails "
       "step 3)", [s_co("Pingwise"), s_board], F("co:Pingwise", "keepcard", "guardrails"), "C4 F10",
       ", keep-running card on board 640643a3fd8f3ca308d9318e ('the night pager for backend outages')",
       alt="A reply asking to drop back to the free plan or to downgrade, a generic acknowledgement, or no email to Dana fails.",
       dist="T: 'night pager' names no vendor")
for tag, co, thing, kind_say, w, quote, why, srcs, fids, dec, extra in [
        ("ans_bundle_sign", "Bundlehouse", "Bundlehouse's participation agreement", "is with Leonard or Arthur to sign", 3,
         "The participation agreement needs signing by Nov 1.", "it costs nothing before January but needs a signature, so step 4 "
         "says to tell them it is with Leonard or Arthur to sign", [s_co("Bundlehouse"), s_guard], F("co:Bundlehouse", "guardrails"),
         "F47", ", deck f_9d1e0270574584de0eb92c"),
        ("ans_kin_lawyers", "Kinetic Arcade", "Kinetic Arcade's letter of intent", "goes to Harmony Games's lawyers first (counsel, "
         "legal or ESG)", 5, "It includes 12 months' exclusivity for those markets", "the LOI's 12-month exclusivity is an ESG trigger "
         "in ESG's note, and step 4 says to tell them it is with our lawyers first", [s_co("Kinetic Arcade"), s_esg],
         F("co:Kinetic Arcade", "esg", "guardrails"), "F45 F4", ", LOI f_6252955f500f81e3aacbef, ESG note thread "
         "frederick.stone@harmonygames.co/1844177063117059830 ('" + q(ESG_TXT, "exclusivity") + "')"),
        ("ans_kin_sign", "Kinetic Arcade", "Kinetic Arcade's letter of intent", "is with Leonard or Arthur to sign", 3,
         "We'd need it signed by Oct 20.", "the LOI costs nothing before January but needs a signature, so step 4 says to tell them it "
         "is with Leonard or Arthur to sign", [s_co("Kinetic Arcade"), s_guard], F("co:Kinetic Arcade", "guardrails"), "F45",
         ", LOI f_6252955f500f81e3aacbef"),
        ("ans_lumen_lawyers", "Lumencloud", "the Lumencloud Startup Program Agreement", "goes to Harmony Games's lawyers first "
         "(counsel, legal or ESG)", 5, "it's a 36-month term", "the agreement's 36-month term is an ESG trigger in ESG's note (a term "
         "over 12 months), and step 4 says to tell them it is with our lawyers first", [s_co("Lumencloud"), s_esg],
         F("co:Lumencloud", "esg", "guardrails"), "F46 F4", ", agreement f_a227b14f03e12005fe8324, ESG note thread "
         "frederick.stone@harmonygames.co/1844177063117059830 ('" + q(ESG_TXT, "a term over 12 months") + "')"),
        ("ans_lumen_sign", "Lumencloud", "the Lumencloud Startup Program Agreement", "is with Leonard or Arthur to sign", 3,
         "the credits start once it's signed", "the credits cost nothing before January but need a signature, so step 4 says to tell "
         "them it is with Leonard or Arthur to sign", [s_co("Lumencloud"), s_guard], F("co:Lumencloud", "guardrails"), "F46",
         ", agreement f_a227b14f03e12005fe8324"),
        ("ans_markward", "Markward", "Markward's free-tier terms", "are with Leonard or Arthur to accept", 5,
         "accept the terms in the dashboard", "Leonard's July Slack note would let Fred accept free terms himself, but his Sep 25 "
         "reply under ESG's note replaces it and click-through terms need an officer (step 4)", [s_co("Markward"), s_esg],
         F("co:Markward", "esg", "guardrails"), "F49 F4 F14", ", ESG note thread frederick.stone@harmonygames.co/1844177063117059830 ('"
         + q(ESG_TXT, "That includes click-through terms") + "')"),
        ("ans_playfuse", "Playfuse", "the Playfuse mutual NDA", "is with Leonard or Arthur to sign", 3,
         "Could someone on your side sign a mutual NDA?", "a mutual NDA on ESG's template needs no review but needs a signature, so "
         "step 4 says to tell them it is with Leonard or Arthur to sign", [s_co("Playfuse"), s_guard], F("co:Playfuse", "guardrails"),
         "F50", ", ESG note thread frederick.stone@harmonygames.co/1844177063117059830 ('" + q(ESG_TXT, "Mutual NDAs on our template "
         "don't need review") + "')")]:
    lawyers = "lawyers" in kind_say
    answer(tag, co, f"{thing} {kind_say}", ("it goes to our lawyers (counsel, legal or ESG) first" if lawyers else
           f"it {kind_say.replace('are with', 'is with')} (either name)"), w, 4, quote, why, srcs, fids,
           dec, extra, alt=("Only 'with Leonard or Arthur', a generic acknowledgement, or no email to this person fails." if lawyers else
                            "A generic acknowledgement, a decline, or no email to this person fails."),
           dist="T: Leonard's July 'accept the terms yourself' note" if co == "Markward" else "—")

# ESG intake checklist parts (one row per part per agreement, weight 1)
ESG_PARTS = [
    ("esg_lumen_cost", "Lumencloud", "The Agent says the Lumencloud Startup Program Agreement costs Harmony Games nothing, with or "
     f"without the credits condition (Cost: $0, no charges or free while the credits last; {NO_MEANING})", "that it costs nothing (with or without the $25,000 credits or the while-credits-last condition)",
     "No charges while credits last", q(CHECK_T, "what it costs us, if anything")),
    ("esg_lumen_signer", "Lumencloud", "The Agent names Leonard or Arthur (either or both) as who would sign it",
     "Leonard or Arthur (either or both) as the signer", "Sign by Oct 31, 2025", q(CHECK_T, "who would sign it (Leonard or Arthur)")),
    ("esg_kin_date", "Kinetic Arcade", "The Agent gives Oct 20, 2025 (any date form) as the date it is needed by",
     "Oct 20, 2025 in any date form as the needed-by date", "Signature needed by Oct 20, 2025", q(CHECK_T, "the date they need it by")),
    ("esg_kin_cost", "Kinetic Arcade", "The Agent says Kinetic Arcade's letter of intent has no fees for Harmony Games (no fees or "
     f"revenue share only; {NO_MEANING})", "that there are no fees to Harmony Games (no fees, no cost, or revenue share only)",
     "Model: revenue share, no fees to Harmony Games", q(CHECK_T, "what it costs us, if anything")),
    ("esg_kin_signer", "Kinetic Arcade", "The Agent names Leonard or Arthur (either or both) as who would sign it",
     "Leonard or Arthur (either or both) as the signer", "Signature needed by Oct 20, 2025", q(CHECK_T, "who would sign it (Leonard or Arthur)")),
    ("esg_bh_term", "Bundlehouse", "The Agent gives the licence term of 18 months", "the 18-month licence term (18 months or a year "
     "and a half)", "in bundle marketing for 18 months", q(CHECK_T, "the term and any automatic renewal")),
    ("esg_bh_date", "Bundlehouse", "The Agent gives Nov 1, 2025 (any date form) as the date it is needed by",
     "Nov 1, 2025 in any date form as the needed-by date", "by Nov 1, 2025", q(CHECK_T, "the date they need it by")),
    ("esg_bh_cost", "Bundlehouse", f"The Agent says Bundlehouse's participation agreement costs nothing to join (no cost to join, free "
     f"or revenue share only; {NO_MEANING})", "that it costs nothing to join (no cost, free, or revenue share only)", "No cost to join",
     q(CHECK_T, "what it costs us, if anything")),
    ("esg_bh_signer", "Bundlehouse", "The Agent names Leonard or Arthur (either or both) as who would sign it",
     "Leonard or Arthur (either or both) as the signer", "Sign the participation agreement", q(CHECK_T, "who would sign it (Leonard or Arthur)"))]
for tag, co, lead, _acc, pq, cq in ESG_PARTS:
    pid = IDS["papers"][co]
    acc = "the Agent " + lead[len("The Agent "):]
    add(tag=tag, t=f"{lead} {ESG_TO} {co} alone", w=1, kind="lookup",
        why=f"one checklist item filled from {co}'s own paper", fact=tag.replace("esg_", "esg_part_"), span=SP_ALL,
        oe=oe(f"co:{co}", "checklist", f"w:esg:{co}"), fids=F(f"co:{co}", "checklist"), vals=f"`PERSON_2599_EMAIL` `{co}`",
        verify=f"{co} intake email: {tag.split('_')[-1]}", final=f"Sent email to PERSON_2599_EMAIL about {co}",
        acc=[f"an intake email to PERSON_2599_EMAIL about {co} alone in which {acc}"],
        alt="An intake email without it, or one email covering several agreements, fails.", srcs=[s_check, s_paper(co)],
        just=f"Lookup: one checklist item ('{cq}') filled from {co}'s paper ('{q(paper_text(co), pq)}'). Which agreements go to ESG "
             "is graded by the volume row.",
        ev=f"Sources: {co} paper {pid} ('{pq}'), checklist f_3b06917a41dd59308d890b ('{cq}'). Accept: a sent intake email to "
           f"PERSON_2599_EMAIL about {co} alone in which {acc}.", dec=f"{FID['co:' + co]} F5", grp="G4 ESG intake",
        valid=f"Intake email about {co}: {acc}", idle="No email sent")

# contacts: a third sample
name, em = ask("Lanternfly Publishing")["from_name"], P("Lanternfly Publishing")
add(tag="ct_wen", t=f"The Agent adds {name} ({em}) to Contacts with {NAMEFORM['Lanternfly Publishing']} in the job field", w=1,
    kind="lookup", why="the name and address come straight from the Lanternfly thread; Lanternfly is Answered, and its person is still "
    "a company contact", fact="contact_lanternfly", span=SP_HUB, oe=oe("co:Lanternfly Publishing", "w:contact:Lanternfly Publishing"),
    fids=F("co:Lanternfly Publishing", "readme"), vals=f"`{name}` `{em}`", verify=f"{name} contact", final="Contacts entry",
    acc=[f"one new contact for {name} with the email {em} and Lanternfly Publishing (or Lanternfly) in the job field"],
    alt="A contact with no email, or no company in the job field, fails.", srcs=[s_co("Lanternfly Publishing", "from_name"), s_readme],
    just="Lookup: the name and address come straight from the Lanternfly thread; the README puts the company in the job field.",
    ev=f"Sources: Lanternfly thread {IDS['threads']['Lanternfly Publishing']} (from {name}, {em}: '" +
       q(thread_text("Lanternfly Publishing"), "Any news on the proposal?") + "'), README "
       f"f_846ddc38b2aab3d2ed3fcb ('Put the company in the job field'). Accept: one new contact {name} with the email {em} and "
       "Lanternfly Publishing or Lanternfly in the job field.", dec="C3 F31", grp="G6 contacts", valid=f"{name}, {em}, job Lanternfly Publishing",
    idle="No contact added")

# reply to Leonard: every member of both lists
KEEP_Q = {"Certwell": "Certwell SSL cert for the API domain", "Vaultline": "Vaultline nightly DB backups"}
for co in ("Certwell", "Vaultline"):
    add(tag=f"reply_{co.lower()}", t=f"The Agent lists {co} among what we're keeping {ON_HUB}", w=5, kind="multi-source",
        why=f"Keep needs Arthur's keep-running card on Trello matched to {co}'s mail; the renewal alone fails the cash test",
        fact=f"reply_{co.lower()}", span=SP_REPLY, oe=oe("keepcard", f"co:{co}", "w:hub"), fids=F(f"co:{co}", "keepcard"),
        vals=f"`{co}` · kept", verify=f"{co} in the keeping list", final="Keeping list in the reply", acc=[f"{co} named as kept"],
        alt=f"{co} listed as ended or parked, or left out, fails.", srcs=[s_co(co), s_board],
        just=f"Multi-source: the Trello keep-running card ('{KEEP_Q[co]}') read with {co}'s Gmail thread.",
        ev=f"Sources: {co} thread {IDS['threads'][co]}, keep-running card on board 640643a3fd8f3ca308d9318e ('{KEEP_Q[co]}'). Accept, "
           f"in a sent reply or reply-all on thread frederick.stone@harmonygames.co/1844732913254784171: {co} among the kept companies.",
        dec=f"C4 {FID['co:' + co]}", grp="G8 reply keep list", valid=f"Keeping: {co}", idle="No reply sent")
SIGN_ROWS = [("Nintendo", 5, "multi-source", "Nintendo's Sign status comes only from Arthur's Linear comment on ZOM-567; the portal "
              "mail says registration completed", [s_nin, s_ack], F("co:Nintendo", "zom"), "C1 F20",
              "Linear ZOM-567 comment cmt_c9a6660d81e067ad1de7 by Arthur ('the Global ToS and NDA still needs our agreement approver "
              "to accept it'), Nintendo portal notice thread frederick.stone@harmonygames.co/1842359398719557772"),
             ("Bundlehouse", 3, "interpretation", "one deck read against guardrails step 4", [s_co("Bundlehouse"), s_ack],
              F("co:Bundlehouse", "esg"), "F47", "Bundlehouse thread " + IDS["threads"]["Bundlehouse"] + " ('The participation "
              "agreement needs signing by Nov 1')"),
             ("Kinetic Arcade", 3, "interpretation", "one LOI read against guardrails step 4", [s_co("Kinetic Arcade"), s_ack],
              F("co:Kinetic Arcade", "esg"), "F45", "LOI f_6252955f500f81e3aacbef ('Signature needed by Oct 20, 2025')"),
             ("Lumencloud", 3, "interpretation", "one agreement read against guardrails step 4", [s_co("Lumencloud"), s_ack],
              F("co:Lumencloud", "esg"), "F46", "agreement f_a227b14f03e12005fe8324 ('Sign by Oct 31, 2025 (cohort closes)')"),
             ("Orbit Store", 3, "interpretation", "one thread read against guardrails step 4; the portal acceptance needs an "
              "authorised signatory", [s_co("Orbit Store"), s_ack], F("co:Orbit Store", "esg"), "F48",
              "Orbit Store thread " + IDS["threads"]["Orbit Store"] + " ('" + q(thread_text("Orbit Store"), "accepted in our partner "
              "portal by an authorised signatory of the company") + "')"),
             ("Playfuse", 3, "interpretation", "one thread read against guardrails step 4; the template NDA skips ESG but needs a "
              "signature", [s_co("Playfuse"), s_ack], F("co:Playfuse", "esg"), "F50",
              "Playfuse thread " + IDS["threads"]["Playfuse"] + " ('Could someone on your side sign a mutual NDA?')")]
for co, w, kind, why, srcs, fids, dec, src_txt in SIGN_ROWS:
    nm = NAMEFORM.get(co, co)
    slug = co.split()[0].lower()
    add(tag=f"reply_{slug}", t=f"The Agent lists {nm} among what's waiting on Arthur or Leonard to sign {ON_HUB}", w=w, kind=kind,
        why=why, fact=f"reply_sign_{slug}", span=SP_REPLY, oe=oe(f"co:{co}", "esg", "w:hub"), fids=fids,
        vals=f"`{co}` · waiting to sign", verify=f"{co} in the sign list", final="Sign list in the reply",
        acc=[f"{nm} named as waiting to sign"], alt=f"{co} reported as ended, parked or already accepted, or left out, fails.",
        srcs=srcs, just=f"{kind.capitalize()}: {why}.",
        ev=f"Sources: {src_txt}; Leonard's reply under ESG's note thread frederick.stone@harmonygames.co/1844177063117059830. Accept, "
           f"in a sent reply or reply-all on thread frederick.stone@harmonygames.co/1844732913254784171: {nm} among the companies "
           "waiting to sign.", dec=dec, grp="G9 reply sign list", valid=f"Waiting to sign: {co}", idle="No reply sent",
        dist="T: 'Registration Completed' and 'NDA Effective: 09/04/2025' look done" if co == "Nintendo" else "—")

# Process: one ordering row replaces the six
add(tag="order_reply", t="The Agent sends its reply to Leonard after all of its other writes for the task (the log sheet, the company "
    "answers, the ESG Law intake emails, the To Do cards, the new contacts and the Jan 5, 2026 reminders), with none of them after "
    "the reply", w=1, cat="Process", kind="lookup", why="one ordering condition read from the prompt's 'When it's all done, reply to "
    "Leonard'", fact="reply_order", span=SP_REPLY, oe=oe("w:create", "w:rows", "w:paylane", "w:ans:*", "w:esg:*", "w:card:*",
    "w:contact:*", "w:rem:*", "w:hub"), fids=F("hub"), vals="`1844732913254784171` · prompt order: When it's all done",
    verify="Order: reply after every other write", final="Order of the reply and the other writes",
    acc=["the reply on Leonard's thread comes after every other write the Agent makes for the task"],
    alt="Any log, answer, ESG, card, contact or reminder write after the reply fails.", srcs=[s_hub],
    just="Lookup: the prompt says 'When it's all done, reply to Leonard'; no Outcome row can show the order.",
    ev="Source: the prompt ('When it's all done, reply to Leonard on his email'); Leonard's email thread "
       "frederick.stone@harmonygames.co/1844732913254784171. Accept: the reply comes after all of the Agent's other writes (log sheet, "
       "company answers, ESG Law intake emails, To Do cards, new contacts, Jan 5, 2026 reminders), with none after it.", dec="F1",
    grp="—", valid="Every other write first, then the reply", idle="No reply sent")

BYTAG = {r["tag"]: r for r in R}
for t in ("reply_thread", "order_log", "order_answers", "order_esg", "order_cards", "order_contacts", "order_reminders"):
    del BYTAG[t]
ORDER_TAGS = [
    "log_folder", "log_type", "log_name", "log_header", "log_rows",
    "nin_decision", "fw_decision", "lf_decision", "sp_decision", "pw_decision", "rev_contact", "sv_waiting",
    "lf_by", "sp_by", "bal_by", "mf_by", "mf_when", "nin_next", "cf_next", "ph_next", "pw_next", "lf_next",
    "ph_told", "lf_told", "sv_told", "kin_told", "ww_told",
    "ans_count", "cf_cancel", "cf_priya", "ans_pixel", "ans_brightlane", "ans_soundvault", "ans_streamcast", "ans_lingora",
    "ans_panelpulse", "ans_ascendo", "ans_wishwave", "rev_cancel", "ans_certwell", "ans_vaultline", "ans_pingwise",
    "ans_orbit", "ans_bundle", "ans_bundle_sign", "ans_kin_lawyers", "ans_kin_sign", "ans_lumen_lawyers", "ans_lumen_sign",
    "ans_markward", "ans_playfuse", "ans_framewell", "ans_retainly", "ans_hootline", "ans_glyphworks", "ans_cloudlark",
    "ans_echohall", "ans_pressbeam", "ans_quillcraft", "ans_tilecast", "ans_benchmarkly", "ans_loopnote", "ans_driftwood",
    "esg_count", "esg_lumen", "esg_lumen_date", "esg_lumen_cost", "esg_lumen_signer", "esg_kinetic", "esg_kin_date",
    "esg_kin_cost", "esg_kin_signer", "esg_bundle", "esg_bh_term", "esg_bh_date", "esg_bh_cost", "esg_bh_signer",
    "card_count", "card_nin", "card_kin", "card_mark", "ct_count", "ct_hoot", "ct_rev", "ct_wen",
    "rem_count", "rem_fw", "rem_lf", "rem_hoot",
    "reply_keep_count", "reply_pingwise", "reply_certwell", "reply_vaultline", "reply_sign_count", "reply_markward",
    "reply_nintendo", "reply_bundlehouse", "reply_kinetic", "reply_lumencloud", "reply_orbit", "reply_playfuse",
    "order_reply"]
assert len(ORDER_TAGS) == 102 and sorted(ORDER_TAGS) == sorted(BYTAG), set(ORDER_TAGS) ^ set(BYTAG)
R[:] = [BYTAG[t] for t in ORDER_TAGS]

# ================================================================ platform /rubric round 2 (FAIL 1, 2026-11-05): five checked fixes
# run_forensics/rev4/rubric_r2/platform_rubric_review_r2.md — titles, weights, justifications and Accept lines copied exactly;
# every other row is locked and must stay byte-identical.
def accept(tag, text):
    BYTAG[tag]["ev"] = BYTAG[tag]["ev"].split("Accept:")[0] + "Accept: " + text


BYTAG["rev_contact"]["t"] = ("The Agent puts Hana Kobayashi (or Hana) or her email PERSON_9708_EMAIL in the Contact column of the Reviewly "
                             "row of its log sheet")
BYTAG["ans_orbit"].update(
    t="The Agent tells Mateo Rossi (PERSON_9719_EMAIL) in writing that Orbit Store's featuring agreement is with Leonard or Arthur to "
      "sign or accept (a reply that also repeats 'with our lawyers first when ESG has to see it' passes; a reply saying this agreement "
      "goes to our lawyers for review first fails, even if it also names Leonard or Arthur)", w=5, kind="multi-source")
accept("ans_orbit", "a sent reply on the Orbit Store thread or a new email to PERSON_9719_EMAIL saying the featuring agreement is with "
       "Leonard or Arthur to sign or accept, with or without the conditional 'with our lawyers first when ESG has to see it'; a reply "
       "saying the featuring agreement goes to our lawyers (counsel, legal or ESG) for review first fails, even if it also names "
       "Leonard or Arthur.")
BYTAG["ans_markward"].update(
    t="The Agent tells Leah Brennan (PERSON_9720_EMAIL) in writing that Markward's free-tier terms are with Leonard or Arthur to sign "
      "or accept (a reply that also repeats 'with our lawyers first when ESG has to see it' passes; a reply saying these terms go to "
      "our lawyers for review first fails, even if it also names Leonard or Arthur)", w=5)
accept("ans_markward", "a sent reply on the Markward thread or a new email to PERSON_9720_EMAIL saying Markward's free-tier terms are "
       "with Leonard or Arthur to sign or accept, with or without the conditional 'with our lawyers first when ESG has to see it'; a "
       "reply saying Markward's free-tier terms go to our lawyers (counsel, legal or ESG) for review first fails, even if it also "
       "names Leonard or Arthur.")
BYTAG["ans_playfuse"].update(
    t="The Agent tells Iris Navarro (PERSON_9721_EMAIL) in writing that the Playfuse mutual NDA is with Leonard or Arthur to sign (a "
      "reply that also mentions ESG's NDA template or repeats 'with our lawyers first when ESG has to see it' passes; a reply saying "
      "this NDA goes to our lawyers for review first fails, even if it also names Leonard or Arthur)", w=5, kind="multi-source",
    just="Multi-source: the NDA's 2-year term (Drive paper) would trip ESG's 'term over 12 months' trigger, but ESG's note (Gmail) says "
         "template NDAs need no review whatever their term, so step 4 says to tell them it is with Leonard or Arthur to sign.")
BYTAG["ans_playfuse"]["srcs"] = BYTAG["ans_playfuse"]["srcs"] + [s_paper("Playfuse"), s_esg]
assert q(paper_text("Playfuse"), "Term: 2 years") and q(ESG_TXT, "Mutual NDAs on our template don't need review, whatever their term.")
accept("ans_playfuse", "a sent reply on the Playfuse thread or a new email to PERSON_9721_EMAIL saying the Playfuse mutual NDA is with "
       "Leonard or Arthur to sign, with or without a mention of ESG's NDA template or the conditional 'with our lawyers first when ESG "
       "has to see it'; a reply saying this NDA goes to our lawyers (counsel, legal or ESG) for review first fails, even if it also "
       "names Leonard or Arthur.")
BYTAG["esg_lumen_date"]["t"] = ("The Agent gives Oct 31, 2025 (any date form) as the date it is needed by in its intake email to ESG Law "
                                "intake (PERSON_2599_EMAIL) about Lumencloud alone")
accept("esg_lumen_date", "a sent intake email to PERSON_2599_EMAIL about Lumencloud alone in which the Agent gives Oct 31, 2025 (any date "
       "form) as the date it is needed by.")
for tag in ("rev_contact", "ans_orbit", "ans_markward", "ans_playfuse", "esg_lumen_date"):
    BYTAG[tag]["acc"] = [BYTAG[tag]["ev"].split("Accept: ", 1)[1].rstrip(".")]

# ---- outputs ---------------------------------------------------------------------------------------------------
rubric = [{"title": r["t"], "category": r.get("cat", "Outcome"), "weight": r["w"], "justification": r["just"],
           "evidence": r["ev"]} for r in R]
(TI / "09_Rubrics.json").write_text(json.dumps(rubric, indent=1, ensure_ascii=False) + "\n")


def ahash(p):
    return subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/stage_gate.py"), "--artifact-hash", str(p)],
                          capture_output=True, text=True, cwd=WS).stdout.strip()


ev_path = WF / "00_V3_Authoring_Evidence.json"
ev = json.loads(ev_path.read_text())
ev["rubric_hash"] = ahash(TI / "09_Rubrics.json")
ev["prompt_hash"] = ahash(TI / "04_Prompt.txt")
ev["rubric_rows"] = []
for i, r in enumerate(R):
    e = {"criterion_id": f"C{i + 1}", "fact_id": r["fact"], "prompt_span": r["span"], "accepted_outcomes": r["acc"],
         "alternatives_review": r["alt"], "source_records": r["srcs"]}
    if "dates" in r:
        e["dates"] = r["dates"]
    ev["rubric_rows"].append(e)
ev_path.write_text(json.dumps(ev, indent=1, ensure_ascii=False) + "\n")
json.dump([{k: v for k, v in r.items() if k != "srcs"} for r in R], open(Path(__file__).with_name("rows.json"), "w"),
          indent=1, ensure_ascii=False)
print(len(R), "rows; weight", sum(r["w"] for r in R), "; bands", {b: sum(1 for r in R if r["w"] == b) for b in (5, 3, 1)},
      "; rubric_hash", ev["rubric_hash"])

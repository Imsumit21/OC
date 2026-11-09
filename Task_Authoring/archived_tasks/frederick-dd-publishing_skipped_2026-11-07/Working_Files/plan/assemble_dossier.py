#!/usr/bin/env python3
"""Assemble Working_Files/01_Grounding_Dossier.md (rev1) from the SQL rows, the final manifest, truth.json, the id maps and
the saved tool outputs in plan/ (each re-run on the final SQL first). Design text only: no prompt, Oracle Event or
criterion wording. Re-run after any SQL, manifest or solver change, then re-run the stage gate."""
import collections, contextlib, io, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
sys.path.insert(0, HERE)
from base_check import parse_sql  # noqa: E402
with contextlib.redirect_stdout(io.StringIO()):
    import build_scenario as B  # noqa: E402

SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
STM = parse_sql(SQL)
IDS = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
MAN = json.load(open(os.path.join(WF, "01_Hardness_Manifest.json")))
TR = json.load(open(os.path.join(WF, "solver", "truth.json")))
ROWS = TR.get("rows", TR)
sys.path.insert(0, os.path.join(WF, "solver"))
import solver as SV  # noqa: E402
AGG = SV.aggregates(ROWS)
FRED = "frederick.stone@harmonygames.co"
I, BASE, SL, MSG, EV = B.IDS, B.BASE, IDS["slack_mid"], IDS["msg"], IDS["events"]
M = {m["key"]: m for m in B.M}
term = B.term


def rd(name):
    return open(os.path.join(HERE, name)).read().rstrip()


def fence(text):
    return ["```", text, "```"]


L = []
A = L.append
ins = [x for x in STM if x["op"] == "insert"]
n_ins, n_upd = len(ins), len([x for x in STM if x["op"] == "update"])
by_table = collections.Counter(x["table"] for x in STM)
thread_member = {v: k for k, v in IDS["threads"].items()}
term_member = {term(k): k for k in B.TERM_DOCS}

ELEM, ROLE = collections.defaultdict(set), {}
for a in MAN["anchors"]:
    for x in (a["record"], a["locator"]):
        ELEM[x].add(a["id"]); ROLE[x] = "first link"
for f in MAN["ask_fragments"]:
    for x in f.get("seeded_ids") or []:
        ELEM[x].add(f["id"])
for h in MAN["authorities"]:
    for x in h.get("seeded_ids") or []:
        ELEM[x].add(h["id"]); ROLE.setdefault(x, "authority")
    for x in h.get("decoy_seeded_ids") or []:
        ELEM[x].add(h["id"] + " decoy"); ROLE[x] = "decoy"
for t in MAN["traps"]:
    for x in t.get("seeded_ids") or []:
        ELEM[x].add(t["id"])
    vr = t.get("version_records") or []
    for i, v in enumerate(vr):
        if v.get("id"):
            ELEM[v["id"]].add(t["id"]); ROLE[v["id"]] = "overturning" if i == len(vr) - 1 else "claim met first"
ROLE[I["dd_folder"]] = "write target (anchor A3)"
CARRIER = {"slack.slack_messages": "●", "gmail.gmail_messages": "●", "gmail.gmail_threads": "●", "gdocs.docs_documents": "●", "gdrive.drive_files": "●",
           "gsheets.sheets_spreadsheets": "●", "gsheets.sheets_sheets": "●", "gslides.slides_presentations": "●", "gslides.slides_pages": "●", "gslides.slides_page_elements": "●",
           "gcal.gcal_events": "● (summary, attendees, time; description ○)", "linear.linear_issues": "●", "linear.linear_comments": "● (§6b)", "trello.trello_cards": "●",
           "trello.trello_actions": "●", "trello.trello_boards": "●", "contacts.contacts": "● (email, job)"}


def rid_of(x):
    r = x.get("row") or {}
    t = x["table"]
    if t in ("gslides.slides_pages", "gslides.slides_page_elements"):
        return f"{r.get('presentation_id')}#{r.get('object_id')}"
    if t == "gsheets.sheets_sheets":
        return f"{r.get('spreadsheet_id')}#{r.get('title')}"
    for k in ("id", "event_id", "contact_id", "document_id", "spreadsheet_id", "presentation_id"):
        if r.get(k):
            return str(r[k])
    w = x.get("where") or {}
    return str(next(iter(w.values()), "?")) if isinstance(w, dict) else str(w)


def element_for(x, rid):
    e = set(ELEM.get(rid, set()))
    r = x.get("row") or {}
    th = r.get("thread_id") or (rid if x["table"].startswith("gmail") else None)
    if th:
        e |= ELEM.get(th, set())
        if th in thread_member:
            e.add(f"cohort: {thread_member[th]}")
    base = rid.split("#")[0]
    if base in term_member:
        e.add(f"cohort terms: {term_member[base]}")
    if base in ELEM and x["table"].startswith(("gslides", "gsheets", "gdrive", "gdocs")):
        e |= ELEM[base]
    return " / ".join(sorted(e)) or "companion"


def role_for(x, rid, elem):
    if x["op"] == "update":
        return "companion (counters / snippet)"
    r = x.get("row") or {}
    own = r.get("user_email") or r.get("calendar_id") or ""
    if own and not str(own).startswith(FRED) and x["table"] in ("gmail.gmail_messages", "gmail.gmail_threads", "gcal.gcal_events"):
        return "companion copy (another attendee's mailbox or calendar)"
    base = rid.split("#")[0]
    if rid in ROLE:
        return ROLE[rid]
    if base in ROLE:
        return ROLE[base]
    if "Invitation" in str(r.get("subject") or ""):
        return "companion (INT-11 invitation)"
    return "connecting (per-publisher evidence)" if "cohort" in elem else "connecting"


def reach_for(x):
    t, r = x["table"], x.get("row") or {}
    if t.startswith("gmail"):
        ref = str(r.get("user_email") or next(iter((x.get("where") or {"": ""}).values()), ""))
        return "Frederick's mailbox" if ref.startswith(FRED) else "other mailbox"
    if t == "gcal.gcal_events":
        return "Frederick's calendar (self)" if r.get("calendar_id") == FRED else "other calendar"
    if t.startswith("slack"):
        return "channel or DM member"
    if t.startswith(("gdrive", "gdocs", "gsheets", "gslides")):
        return "Drive owner or share"
    return "unscoped service"


A("# Grounding Dossier — frederick_dd_publishing · injection rev2 · contains no prompt, OE or criterion text")
A("")
A("SQL: `task_inputs/01_Universe_Inject.sql` (stored byte for byte in `Working_Files/run_forensics/rev2/01_Universe_Inject.sql`; rev1 and its platform reviews stay in `run_forensics/rev1/`), built by `Working_Files/plan/build_sql.py` from the certified design "
  "(`01_Scenario_Design.md`, draft manifest, surface); final manifest by `plan/build_final_manifest.py`; solver `Working_Files/solver/solver.py` (truth `solver/truth.json`); this file by `plan/assemble_dossier.py`. "
  "Universe synth-cut, seed bound 2025-10-01T00:00:00Z (Tue Sep 30 17:00 PT), eval clock 2025-10-01T07:00:00Z; Frederick's today is Wed Oct 1, 2025. "
  f"{n_ins} INSERT + {n_upd} UPDATE statements over 10 schemas. Every probability here is UNCALIBRATED.")
A("")
A("## 1.A Structural")
A("")
A("| Table | NOT NULL columns supplied (live schema) | Base location · sample ids | Format notes |")
A("|---|---|---|---|")
A(f"| gmail.gmail_threads / gmail_messages | id, user_email; id, thread_id, user_email, label_ids_json, internal_date, date | gmail/threads/frederick@harmonygames.co_1830012626042968381.json (thread_id {BASE['appodeal_thread']}) | mailbox-prefixed ids; Message-ID in the row id; CRLF bodies; to_json holds name and address strings |")
A(f"| slack.slack_messages | id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, attachments_json, created_at, metadata_json | slack/messages/C07C2866011/2025-09.json (root 330b95fd38236b4e7192e24f272685b4) | id = sha256(channel|ts)[:32]; replies carry thread_parent_id and thread_ts_legacy; root counters updated |")
A("| gdrive.drive_files / gdocs.docs_documents / gsheets / gslides | id, name, mime_type; document_id, title; spreadsheet_id, title; presentation_id, object_id | gdrive/data.json d_175c0d7bc72ed244b944cb (Frederick's root) | f_/d_ + 22 hex; style_runs_json covers the title line and headings |")
A("| gcal.gcal_events | event_id, calendar_id | gcal/data.json (10,395 events checked, plan/id_checks_sql.out.json) | one row per attendee calendar held by staff, self:true on the owner's copy; evt_ + 22 hex; ical_uid 32 hex @hg4 |")
A("| linear.linear_comments / linear_issues | comment id, issue_id, author_id, body, is_edited; issue updated_at | linear/data.json ENG-2362 (Todo, assignee Arthur) | lc_ + 24 hex; the base comments collection is empty (0 records), so the row follows Ask_Carriers §6b |")
A(f"| trello.trello_cards / trello_actions / trello_boards | id, name, idBoard, idList; id, type, date | trello/data.json board {B.UABD_BOARD} (UA/BD), list {B.BD_LIST} (BD Follow Up) | 24 hex with the action time in the first 8; idShort 41–43 after base max 40; badges match comment counts |")
A("| contacts.contacts | contact_id, first_name, last_name | contacts/contacts.json (170 contacts) | 24 hex ids; sparse like the base (job, email) |")
A("")
A("## 1.B Entity")
A("")
A("| Entity | Spelling used | Where it appears (cited) | Agreement |")
A("|---|---|---|---|")
A(f"| Frederick Stone | {FRED} (roster; base files use the frederick@ alias, I03) | slack EMPLOYEE_0008_SLACK_ID in C07C2866011; mailbox {I['hub_thread']}; Drive root d_175c0d7bc72ed244b944cb | AGREE |")
A(f"| Leonard Hayes | leonard.hayes@harmonygames.co | slack EMPLOYEE_0038_SLACK_ID ({BASE['rights_post']}); hub sender {MSG['hub']}; owner of {I['rule_doc']} | AGREE |")
A(f"| Robert | robert@harmonygames.co | slack EMPLOYEE_0016_SLACK_ID ({I['kestrel_post']}, {I['copperleaf_relay']}) | AGREE |")
A(f"| Arthur Blake | arthur.blake@harmonygames.co | linear usr_cc3e90160f490686 (ENG-2362, {I['eng2362_comment']}); slack EMPLOYEE_0025_SLACK_ID ({I['arthur_cash']}) | AGREE |")
A(f"| ESG Law | partner PERSON_2694 (base engagement {BASE['esg_engagement']}) | seeded note {MSG['esg_note']} | AGREE |")
A(f"| Appodeal | Appodeal | base {BASE['appodeal_thread']}, {BASE['appodeal_fwd']} | AGREE |")
A(f"| Rayking Game | Rayking Game | base {BASE['rayking_thread']}, {BASE['rayking_linkedin']}; seeded DM {I['rayking_dm']} | AGREE |")
A(f"| Homa, NCsoft, Tilting Point | as in the base | {BASE['homa_codev']}, {BASE['ncsoft_question']}, {BASE['tilting_ack']} | AGREE (named out of scope by {I['rule_doc']}) |")
for k in M:
    if M[k].get("base"):
        continue
    who = M[k].get("person")
    where = term(k) if k in B.TERM_DOCS else {"Copperleaf Games": SL["copperleaf_relay"], "Redwood Arcade": I["eng2362_comment"]}.get(k) or IDS["threads"].get(k)
    A(f"| {k} | {k}{' · ' + who[0] + ' ' + who[1] if who else ''} | {where} | AGREE (new entity; 0 base hits in plan/name_census.json) |")
A(f"| Kestrel Group | Kestrel | signature {IDS['threads']['Moonrail Studios']}, contact {I['anika_contact']}, post {I['kestrel_post']} | AGREE (new entity; its first-word hits are newsletter noise, plan/name_census.log) |")
A("")
A("Frederick's GitHub display name 'Ryan' (S04) is avoided: no GitHub record is touched. No roster person is renamed or re-titled.")
A("")
A("## 1.C Voice and realism")
A("")
A("Seeded speakers, each with its activity.json (synth-cut KB) status at the clock:")
A(f"- Leonard Hayes (leonard.hayes@harmonygames.co, EMPLOYEE_0038_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds dated Sep 25–30 2025 ({I['standing_line']}, {MSG['hub']}, {I['rule_doc']}).")
A(f"- Robert (robert@harmonygames.co, EMPLOYEE_0016_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds Sep 26 and Sep 29 2025 ({I['copperleaf_relay']}, {I['kestrel_post']}).")
A(f"- Arthur Blake (arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds Sep 26 and Sep 30 2025 ({I['arthur_analytics']}, {I['eng2362_comment']}, {I['arthur_cash']}).")
A(f"- Frederick Stone ({FRED}, EMPLOYEE_0008_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; his seeded outreach mail (May 6 to Sep 24), DM {I['rayking_dm']} and card comments {I['sunfold_comment']}, {I['oakline_card_comment']}.")
A("- External senders (each publisher's own address, plain names in the signature) and PERSON_2694_EMAIL (ESG partner, base) are not personas.")
A("")
A("Lengths and hours from conventions.json (synth-cut KB): slack.length_chars_by_channel_type private p50 51 / p90 156 / p99 615; the seeded lines run 95–290 characters, below p99. slack.per_person_hours_and_style core UTC windows: Arthur 15–01, and Leonard's and Robert's windows cover 15–02 and 16–04: every seeded post falls inside its author's window (Leonard 16:20Z; Robert 18:05Z, 20:15Z; Arthur 17:05Z, 18:32Z, 18:40Z). gmail.internal_subject_len_chars p50 42: 'DD publishing: what I need for Monday' is 37. gcal.duration_min p50 30: the three publisher calls are 30 minutes.")
A("")
A("Voice from real messages: Leonard's mail is full sentences signed 'Leonard'; Robert's Slack is short and blunt; Arthur states what he checked. Founders call Frederick 'Fred' in Slack and mail.")
A("")
A("## 1.D Keyword")
A("")
A("| Term | Hits / pointer | Note |")
A("|---|---|---|")
A(f"| \"Appodeal\" | base {BASE['appodeal_thread']} | waiting on us |")
A(f"| \"Rayking\" | base {BASE['rayking_thread']}, {BASE['rayking_linkedin']} | waiting on us; Frederick's Sep 4 message is an unsent draft |")
A(f"| \"ESG\" | base {BASE['esg_engagement']} (engagement); seeded {I['esg_thread']} | the licence date |")
A(f"| \"non-mobile\" | base {BASE['rights_post']}, {BASE['sync_doc']} | the rights position |")
A(f"| \"D30 ARPI\" | base {BASE['organic_arpi']} | the $0.50 figure |")
for t_, where in [("DD publishing", f"{I['dd_folder']}, {I['dd_card']}, {I['rule_doc']}, {I['hub_thread']}"), ("ground rules", I["rule_doc"]), ("outreach sheet", I["outreach_sheet"]), ("Licence paper timing", I["esg_thread"])]:
    A(f"| \"{t_}\" | NEW TERM — introduced in {where} | reached from the hub {I['hub_thread']} or its delegations |")
for k in M:
    if not M[k].get("base"):
        A(f"| \"{k}\" | NEW TERM — introduced in {IDS['threads'].get(k) or (SL['copperleaf_relay'] if k.startswith('Copper') else I['eng2362_comment'])} | 0 base hits (plan/name_census.json) |")
A("")
A("Name census with a positive control: plan/name_census.json counts every seeded company name over the base services; exact names are clean and the positive control Balancy is found. First-word counts ('Harbor', 'Redwood', 'Summit') overcount and are not used.")
A("")
A("## 1.E Persona reach")
A("")
A(f"Load-bearing ids written to `Working_Files/plan/load_bearing.txt` ({len(rd('load_bearing.txt').split())} ids, the services check-sql reads); output verbatim:")
A("")
L.extend(fence(rd("checksql.txt")))
A("")
A(f"- C07C2866011 — #executives, Frederick a member LB; seeded {I['kestrel_post']} and replies {I['copperleaf_relay']}, {I['arthur_cash']}.")
A(f"- C096HFA5Z8W — #bridge-pitch, Frederick a member LB; seeded reply {I['standing_line']}.")
A(f"- C069FF9Q57S — #analytics, Frederick a member; seeded pointer {I['arthur_analytics']}.")
A(f"- D05S58U4SAK — Frederick's DM with Leonard LB; seeded {I['rayking_dm']}.")
A(f"- Frederick's mailbox: the hub {I['hub_thread']}, the ESG thread {I['esg_thread']} and every publisher thread (Facts for the human) are INBOX or SENT copies in {FRED} LB.")
A(f"- Drive: {I['dd_folder']}, {I['outreach_sheet']}, {I['onepager_deck']} and {I['codev_doc']} are Frederick-owned; {I['rule_doc']} and every term sheet are shared with him LB.")
A(f"- Calendar: {I['pb_event']}, {I['harbor_event']}, {I['wavecrest_event']} and {I['monday_event']} are Frederick's own copies (self:true) LB.")
A(f"- Unscoped services (Linear, Trello, Contacts; check-sql doesn't read them, plan/load_bearing.txt leaves them out): ENG-2362, {I['eng2362_comment']}, {I['dd_card']}, {I['oakline_card']}, {I['sunfold_card']}, {I['sunfold_comment']}, {I['anika_contact']}. Frederick's reach on the UA/BD board is in `00_PreScenario/cansee_anchors.txt`.")
A(f"- No designed denial: denied_probes is empty; every load-bearing mail is Frederick's own copy ({I['hub_thread']}), and other people's mailbox and calendar copies are companions, never evidence.")
A("")
idc = json.load(open(os.path.join(HERE, "id_checks_sql.out.json")))["checks"]
sk = json.load(open(os.path.join(HERE, "slack_lookup.out.json")))
A("## 1.F Collision")
A("")
A("Every id the SQL mints was looked up over its full base collection (`tools/hg.py records --request plan/id_checks_sql.json`, `hg.py search lookup`):")
for k, c in idc.items():
    A(f"- {k}: {c.get('records_checked')} base records checked, scan_complete {c.get('scan_complete')}, {len(c.get('matches') or [])} matches (plan/id_checks_sql.out.json).")
A(f"- slack: the {len(sk['matches'])} seeded message ids over messages/*/*.json — {sk['files_completed']} of {sk['files_selected']} files, {sk['records_checked']} records, scan_complete {sk['scan_complete']}, {sum(len(v) for v in sk['matches'].values())} hits (plan/slack_lookup.out.json).")
A("- gmail: thread ids (mailbox/((ms << 20) + bits)) and RFC Message-IDs are minted per seeded time; base_check Check A (full-collection uniqueness through its base caches) PASS, see Self-review.")
A("- Body tokens: none minted. PERSON_2694 is reused only for the ESG partner.")
A("")
A("## Record ledger")
A("")
A("One row per SQL statement (inserts and the companion updates), in SQL order.")
A("")
A("| # | SQL line | Table | Id | Manifest element | Carrier | Reach | Discovery role |")
A("|---|---|---|---|---|---|---|---|")
for n, x in enumerate(STM, 1):
    rid = rid_of(x)
    el = element_for(x, rid)
    shown = f"ENG-2362 comment {rid}" if x["table"] == "linear.linear_comments" else rid
    A(f"| {n} | L{x['line']} | {x['table']}{' (UPDATE)' if x['op'] == 'update' else ''} | {shown} | {el} | {CARRIER.get(x['table'], '●')} | {reach_for(x)} | {role_for(x, rid, el)} |")
A("")
exec(open(os.path.join(HERE, "dossier_text.py")).read())
out = os.path.join(WF, "01_Grounding_Dossier.md")
open(out, "w").write("\n".join(L) + "\n")
print("wrote", out, len(L), "lines")

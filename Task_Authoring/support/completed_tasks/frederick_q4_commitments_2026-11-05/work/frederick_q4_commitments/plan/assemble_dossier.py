#!/usr/bin/env python3
"""Assemble Working_Files/01_Grounding_Dossier.md (rev4) from the SQL rows, the final manifest, truth.json, the id maps
and the saved tool outputs in plan/ (each re-run on the final SQL before this script). Design-only text: no prompt,
Oracle Event or criterion wording. Re-run after any SQL / manifest / solver change, then re-run the stage gate."""
import collections
import contextlib
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
TOOLS = os.path.join(TI, "..", "tools")
sys.path.insert(0, TOOLS)
sys.path.insert(0, HERE)
from base_check import parse_sql  # noqa: E402
with contextlib.redirect_stdout(io.StringIO()):
    import build_scenario as B  # noqa: E402

SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
STM = parse_sql(SQL)
IDS = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
MAN = json.load(open(os.path.join(WF, "01_Hardness_Manifest.json")))
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
TRUTH = TRUTH.get("rows", TRUTH)
SURF = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))
FRED = "frederick.stone@harmonygames.co"
I, BASE = B.IDS, B.BASE
SL = IDS["slack_mid"]


def rd(name):
    return open(os.path.join(HERE, name)).read().rstrip()


def fence(text):
    return ["```", text, "```"]


L = []
A = L.append

# ---------------------------------------------------------------- derived data
ins = [x for x in STM if x["op"] == "insert"]
n_ins, n_upd = len(ins), len([x for x in STM if x["op"] == "update"])
by_table = collections.Counter(x["table"] for x in STM)
msgs = [x["row"] for x in ins if x["table"] == "gmail.gmail_messages"]
msg_thread = {r["id"]: r["thread_id"] for r in msgs}
thread_member = {v: k for k, v in IDS["threads"].items()}
paper_member = {v: k for k, v in IDS["papers"].items()}
extra_threads = {I["nova_thread"]: "Nova Rewards", I["motive_thread"]: "Motive Forge", I["spotlight_thread"]: "Spotlight Fest",
                 I["clipforge_notice_thread"]: "Clipforge (Paylane notice)"}
M = {m["key"]: m for m in B.M}

ELEM = collections.defaultdict(set)
ROLE = {}
for a in MAN["anchors"]:
    for x in (a["record"], a["locator"]):
        ELEM[x].add(a["id"])
        ROLE[x] = "first link"
for f in MAN["ask_fragments"]:
    for x in f.get("seeded_ids") or []:
        ELEM[x].add(f["id"])
for h in MAN["authorities"]:
    for x in h.get("seeded_ids") or []:
        ELEM[x].add(h["id"])
        ROLE.setdefault(x, "authority")
    for x in h.get("decoy_seeded_ids") or []:
        ELEM[x].add(h["id"] + " decoy")
        ROLE[x] = "decoy"
for t in MAN["traps"]:
    for x in t.get("seeded_ids") or []:
        ELEM[x].add(t["id"])
    vr = t.get("version_records") or []
    for i, v in enumerate(vr):
        x = v.get("id")
        if x:
            ELEM[x].add(t["id"])
            ROLE[x] = "overturning" if i == len(vr) - 1 else "claim met first"
for k, v in IDS["threads"].items():
    ELEM[v].add(f"cohort: {k}")
for k, v in IDS["papers"].items():
    ELEM[v].add(f"cohort paper: {k}")
for tid, k in extra_threads.items():
    ELEM[tid].add(f"cohort: {k}")
for x in (I["q4_folder"], I["template_sheet"]):
    ROLE[x] = "write target"
ROLE[I["readme_doc"]] = "authority (log format) · write target folder"

CARRIER = {"slack.slack_messages": "●", "gmail.gmail_messages": "●", "gmail.gmail_threads": "●", "gdocs.docs_documents": "●",
           "gdrive.drive_files": "●", "gsheets.sheets_spreadsheets": "●", "gsheets.sheets_sheets": "●",
           "gslides.slides_presentations": "●", "gslides.slides_pages": "●", "gslides.slides_page_elements": "●",
           "gcal.gcal_events": "● (summary, attendees, time; description ○)", "linear.linear_issues": "●",
           "linear.linear_comments": "● (§6b)", "trello.trello_cards": "●", "trello.trello_actions": "●",
           "trello.trello_checklists": "●", "trello.trello_check_items": "●", "contacts.contacts": "● (email, job)"}


def rid_of(x):
    r = x.get("row") or {}
    for k in ("id", "event_id", "contact_id", "document_id", "spreadsheet_id", "presentation_id"):
        if r.get(k):
            v = str(r[k])
            if x["table"] in ("gslides.slides_pages", "gslides.slides_page_elements"):
                v = f"{r.get('presentation_id')}#{r.get('object_id') or r.get('page_id') or ''}"
            if x["table"] == "gsheets.sheets_sheets":
                v = f"{r.get('spreadsheet_id')}#{r.get('title')}"
            return v
    w = x.get("where") or {}
    return str(next(iter(w.values()), "?")) if isinstance(w, dict) else str(w)


def owner_of(x):
    r = x.get("row") or {}
    return r.get("user_email") or r.get("calendar_id") or ""


def element_for(x, rid):
    e = set(ELEM.get(rid, set()))
    t = x["table"]
    r = x.get("row") or {}
    if t == "gmail.gmail_messages":
        th = r.get("thread_id")
        e |= ELEM.get(th, set())
        if th in thread_member:
            e.add(f"cohort: {thread_member[th]}")
    base = rid.split("#")[0]
    if base in paper_member:
        e.add(f"cohort paper: {paper_member[base]}")
    if base in ELEM and t.startswith(("gslides", "gsheets", "gdrive", "gdocs")):
        e |= ELEM[base]
    if not e:
        e = {"companion"}
    return " / ".join(sorted(e))


def role_for(x, rid, elem):
    if x["op"] == "update":
        return "companion (counters / snippet)"
    own = owner_of(x)
    if own and not str(own).startswith(FRED) and x["table"] in ("gmail.gmail_messages", "gmail.gmail_threads", "gcal.gcal_events"):
        return "companion copy (another attendee's mailbox or calendar)"
    base = rid.split("#")[0]
    if rid in ROLE:
        return ROLE[rid]
    if base in ROLE:
        return ROLE[base]
    if x["table"] == "gmail.gmail_messages" and (x.get("row") or {}).get("thread_id") in ROLE:
        return ROLE[(x.get("row") or {}).get("thread_id")]
    if "Invitation" in str((x.get("row") or {}).get("subject") or ""):
        return "companion (INT-11 invitation)"
    if "cohort" in elem:
        return "connecting (per-company evidence)"
    return "connecting"


def reach_for(x):
    t, r = x["table"], x.get("row") or {}
    if not r:
        r = {"id": str(next(iter((x.get("where") or {}).values()), "")), "channel_id": B.EXEC, "calendar_id": FRED}
    if t.startswith("gmail"):
        return "Frederick's mailbox" if str(r.get("user_email") or r.get("id") or "").startswith(FRED) else "other mailbox"
    if t == "gcal.gcal_events":
        return "Frederick's calendar (self)" if r.get("calendar_id") == FRED else "other calendar"
    if t.startswith("slack"):
        return "#executives member" if r.get("channel_id") == B.EXEC else "DM member"
    if t.startswith(("gdrive", "gdocs", "gsheets", "gslides")):
        return "Drive owner or share"
    return "unscoped service"


# ---------------------------------------------------------------- header
A("# Grounding Dossier — frederick_q4_commitments · injection rev4 · contains no prompt, OE or criterion text")
A("")
A("SQL: `task_inputs/01_Universe_Inject.sql` (stored byte for byte in `Working_Files/run_forensics/rev4/01_Universe_Inject.sql`; rev1, rev2 and rev3, each passed by the platform /injection review, are kept with their reviews and truth in `run_forensics/rev1/`–`rev3/`, and rev3's Opus pre-check and /hardness review in `run_forensics/rev3/`), "
  "built by `Working_Files/plan/build_sql.py` from the certified design-2 (`01_Scenario_Design.md` 2c09f947100b, draft manifest "
  "84fea705bc87, surface abd340b2b96e); final manifest by `plan/build_final_manifest.py`; solver "
  "`Working_Files/solver/solver.py` (truth `solver/truth.json`); this file by `plan/assemble_dossier.py`. Universe synth-cut, "
  "seed bound 2025-10-01T00:00:00Z (Tue Sep 30 17:00 PT), eval clock 2025-10-01T07:00:00Z; Frederick's today is Wed Oct 1, 2025. "
  f"{n_ins} INSERT + {n_upd} UPDATE statements over 10 schemas. Every probability here is UNCALIBRATED.")
A("")

# ---------------------------------------------------------------- 1.A
A("## 1.A Structural")
A("")
A("| Table | NOT NULL columns supplied (live schema) | Base location · sample ids | Format notes |")
A("|---|---|---|---|")
A("| gmail.gmail_threads / gmail_messages | id, user_email; id, thread_id, user_email, label_ids_json, internal_date, date | gmail/threads/frederick@harmonygames.co_1840501641217286806.json (message thread_id frederick.stone@harmonygames.co/1840501641217286806) | thread id = mailbox/((ms << 20) + 20 bits); message id = mailbox/ + the RFC Message-ID in angle brackets; one copy per sender/recipient mailbox with SENT or INBOX labels; In-Reply-To / References on replies; thread snippet = newest message (UPDATE) |")
A(f"| slack.slack_messages | id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, attachments_json, created_at, metadata_json | slack/messages/C07C2866011/2025-09.json (root c41d37178fca394c135408d2b38e0879 = C07C2866011/1758513190.847889) | id = sha256(channel|ts)[:32]; a reply carries thread_ts + parent id, and its root's reply_count / reply_users_count / latest_reply are updated (Q01) |")
A("| gdrive.drive_files / gdocs.docs_documents / gsheets / gslides | id, name, mime_type; document_id, title; spreadsheet_id, title; presentation_id, object_id | gdrive/data.json d_175c0d7bc72ed244b944cb (Frederick's root) | f_/d_ + 22 hex; identical sharing on the Drive row and the native row; docs body_text with style_runs headings |")
A("| gcal.gcal_events | event_id, calendar_id | gcal/data.json (10,395 events checked, plan/id_checks_sql.out.json) | one row per attendee calendar, self:true on the owner's copy; evt_ + 22 hex; ical_uid 32 hex @hg4; future plan fields only for the Jan 5, 2026 review |")
A("| linear.linear_issues / linear_comments | id, title, priority, labels_json, links_json, relations_json, state_history_json, is_archived, created_at, updated_at; comment id, issue_id, author_id, body, is_edited | linear/data.json (3,687 issues; ZOM-566 is the newest) | id = identifier = ZOM-567; cmt_ + 20 hex; Todo, no lifecycle stamps |")
A("| trello.trello_cards / actions / checklists / check_items | id, name, idBoard, idList; id, type, date; id, name, idCard, idBoard; id, name, idChecklist | trello/data.json board 640643a3fd8f3ca308d9318e (founders' 'Harmony Games' board), card 688c4fa78031638f0804a994 | ids: first 8 hex = Unix seconds of the action (I16); full badges_json shape; createCard + addChecklistToCard actions |")
A("| contacts.contacts | contact_id, first_name, last_name | contacts/contacts.json (170 contacts) | 24 hex ids; sparse like the base (job, email) |")
A("")

# ---------------------------------------------------------------- 1.B
A("## 1.B Entity")
A("")
A("| Entity | Spelling used | Where it appears (cited) | Agreement |")
A("|---|---|---|---|")
A(f"| Frederick Stone | {FRED} (roster; base files use the frederick@ alias, I03) | slack EMPLOYEE_0008_SLACK_ID in C07C2866011; mailbox {I['hub_thread']}; Drive root d_175c0d7bc72ed244b944cb | AGREE |")
A(f"| Leonard Hayes | leonard.hayes@harmonygames.co | slack EMPLOYEE_0038_SLACK_ID ({SL['amendment_root']}, D05S58U4SAK/1759174260.052645); hub sender {IDS['msg']['hub']}; owner of {I['guardrails_doc']} | AGREE |")
A(f"| Robert | robert@harmonygames.co | slack EMPLOYEE_0016_SLACK_ID ({SL['robert_cancel_all']}, {SL['spotlight_note']}); organizer of evt_564a16d0f5f6598d0360d5 | AGREE |")
A(f"| Arthur Blake | arthur.blake@harmonygames.co | linear usr_cc3e90160f490686 (ZOM-567, cmt_c9a6660d81e067ad1de7); Trello creator of {I['keep_card']} | AGREE |")
A(f"| ESG Law | partner PERSON_2694 (base engagement {BASE['esg_engagement']}); intake PERSON_2599_EMAIL | seeded note {IDS['msg']['esg_note']}; contact 9b0185e445572aeee9f27d35; checklist {I['esg_checklist_doc']} | AGREE |")
A(f"| Nintendo (developer portal) | Nintendo | base {BASE['nintendo_ndareq']} (Global ToS & NDA Acceptance Required), {BASE['nintendo_regdone']} (Registration Completed), C07C2866011/1757011358.730529; seeded ZOM-567 | AGREE ('Global ToS & NDA' in the portal mail, 'Global ToS and NDA' in Arthur's comment) |")
A(f"| Balancy | Balancy | base {BASE['balancy_thread']} (PERSON_0527, Leonard's Sep 11 answer) | AGREE |")
A(f"| Playtestcloud | Playtestcloud | base root C07C2866011/1758513190.847889 (Leonard, Sep 21 PT / Sep 22 03:53 UTC) | AGREE (the Framewell waiver is a reply under it: {SL['framewell_waiver_reply']}) |")
A(f"| Clipforge / UGC Studio / workspace HG-2291 / Paylane | Clipforge (company), UGC Studio (product), HG-2291 (workspace), Paylane (its processor) | welcome {IDS['msg']['Clipforge:0']} ('workspace is set up (HG-2291)'); paper {IDS['papers']['Clipforge']}; kickoff evt_0a5e42c3aac62434ba2cfc; notice {IDS['msg']['clipforge_notice']} (no 'Clipforge' string) | DISAGREE (designed alias, one company; joined by HG-2291) |")
A(f"| Lanternfly Publishing | 'Lanternfly Publishing' (signature, deck); 'Lanternfly' short form | {IDS['threads']['Lanternfly Publishing']}, deck {IDS['papers']['Lanternfly Publishing']}, DM thread reply D05S58U4SAK/1759174260.052645 under Leonard's Sep 17 root D05S58U4SAK/1758151772.570449 (rev4: names Wen and 'their Southeast Asia deal', not the company) | AGREE (Wen Halvorsen signs the company's thread) |")
for k in [m["key"] for m in B.M if m["decision"] != "out" and m["key"] not in ("Nintendo", "Balancy", "Lanternfly Publishing", "Clipforge")]:
    th, pa = IDS["threads"].get(k), IDS["papers"].get(k)
    who = IDS["people"].get(k)
    where = ", ".join(x for x in (th, pa) if x)
    A(f"| {k} | {k}{' · ' + who[1] + ' (' + who[0] + ')' if who else ''} | {where} | AGREE (new entity; 0 base hits in plan/name_census.json) |")
for k, why, bid in [("Rayking Game", "boundary (T18)", BASE["rayking_thread"]), ("Playable Factory", "boundary (T11)", BASE["playable_factory_thread"]),
                    ("Gamesforum SF", "boundary", BASE["gamesforum_thread"]), ("InterCo Digital", "boundary", BASE["interco_thread"]),
                    ("Google partner check-in", "boundary (T12)", BASE["google_thread"]), ("Singular", "boundary (SC-39)", BASE["singular_renewal"]),
                    ("NCsoft", "boundary (T15)", BASE["ncsoft_report"]), ("Dentsu", "boundary", BASE["dentsu_thread"]),
                    ("Mattel", "boundary (SC-24, SC-55)", BASE["mattel_rfp_post"]), ("Nova Rewards", "boundary (T16)", I["nova_thread"])]:
    A(f"| {k} | {k} | {bid} | AGREE ({why}) |")
A("")
A("Frederick's GitHub display name 'Ryan' (S04) is avoided: no GitHub record is touched. No roster person is renamed or re-titled.")
A("")

# ---------------------------------------------------------------- 1.C
A("## 1.C Voice and realism")
A("")
A("Seeded speakers, each with its activity.json (synth-cut KB) status at the clock:")
A(f"- Leonard Hayes (leonard.hayes@harmonygames.co, EMPLOYEE_0038_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds dated Jul 22 and Sep 22–30 2025 (C07C2866011/1753207800.603298, C07C2866011/1759166100.370044, C07C2866011/1758920520.674991, D05S58U4SAK/1759174260.052645, hub {IDS['msg']['hub']}, docs {I['guardrails_doc']}, {I['readme_doc']}, {I['template_sheet']}).")
A(f"- Robert (robert@harmonygames.co, EMPLOYEE_0016_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds Sep 17 and Sep 25 2025 (C07C2866011/1758134460.899858, C07C2866011/1758819840.884370) and the Sep 17 call he organizes (evt_564a16d0f5f6598d0360d5).")
A(f"- Arthur Blake (arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds Aug 12 (keep-running card {I['keep_card']}) and Sep 23–25 2025 (ZOM-567, cmt_c9a6660d81e067ad1de7), plus Motive Forge's decline in {I['motive_thread']}.")
A(f"- Frederick Stone ({FRED}, EMPLOYEE_0008_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; his seeded replies (e.g. Lanternfly Sep 10 in {IDS['threads']['Lanternfly Publishing']}) and the July tracker {I['tracker_sheet']} predate the seed bound; quiet only after it.")
A("- External senders PERSON_9701_EMAIL–PERSON_9735_EMAIL (one per counterparty, plain names in the signature), PERSON_2694_EMAIL (ESG partner, base), PERSON_0527_EMAIL (Balancy, base only) and SVC_9701_EMAIL (Paylane notices) are not personas (no activity.json entry).")
A("")
A("Lengths, hours and titles from conventions.json (synth-cut KB): slack.length_chars_by_channel_type private p50 51 / p90 155 / p99 617 — the seeded #executives lines run 85–200 characters (the amendment is the longest at ~200, below p99) and the DM line ~150 (im); "
  "slack.per_person_hours_and_style — Leonard's core UTC window 15–02 (07–18 PT), Robert's 16–04, Arthur's 15–01: every seeded post falls inside its author's window (Leonard 17:15Z, 18:10Z, 19:31Z, 21:02Z; Robert 17:04Z, 18:41Z; Arthur 16:05Z, 18:20Z); "
  "gmail.internal_subject_len_chars p50 42 — the hub subject 'Vendor and partner stuff while I'm in LA' is 41; gcal.duration_min p50 30 — the Spotlight call is 30 minutes, the January review 45; "
  "linear.title_prefixes_by_team: most ZOM titles carry no prefix — 'Switch: order dev kits' follows the base's plain imperative titles.")
A("")
A("Voice from real messages: Leonard writes lower-case, run-on Slack lines ('we need to talk to more VCs', C096HFA5Z8W/1758564801.307569) and full-sentence mail signed 'Leonard'; Robert's Slack is short and blunt; Arthur's Linear text is matter-of-fact. The seeded lines keep those registers (S_AMEND, S_WAIVER, S_DM in plan/build_sql.py).")
A("")

# ---------------------------------------------------------------- 1.D
A("## 1.D Keyword")
A("")
A("| Term | Hits / pointer | Note |")
A("|---|---|---|")
A(f"| \"Nintendo\" | base {BASE['nintendo_ndareq']}, {BASE['nintendo_regdone']}, C07C2866011/1757011358.730529; seeded ZOM-567 | the comment cmt_c9a6660d81e067ad1de7 says 'the portal' and 'Global ToS and NDA' |")
A(f"| \"Balancy\" | base {BASE['balancy_thread']} | Leonard's in-thread answer |")
A(f"| \"Playtestcloud\" | base C07C2866011/1758513190.847889 | the root the Framewell reply sits under |")
A(f"| \"ESG\" | base {BASE['esg_engagement']} (engagement, Aug 27); seeded {I['esg_thread']}, {I['esg_checklist_doc']} | ESG Law intake contact 9b0185e445572aeee9f27d35 |")
A(f"| \"Rayking\" | base {BASE['rayking_thread']} | Frederick's Sep 4 'reply' is addressed to Leonard |")
for term, where in [("runway guardrails", I["guardrails_doc"]), ("keep-running", I["keep_card"]), ("night pager", IDS["keep_items"][2]),
                    ("HG-2291", f"{IDS['papers']['Clipforge']}, {IDS['msg']['Clipforge:0']}, evt_0a5e42c3aac62434ba2cfc, {IDS['msg']['clipforge_notice']}"),
                    ("Paylane / billing@paylane.io", IDS["msg"]["clipforge_notice"]), ("Q4 commitments", f"{I['q4_folder']}, {I['readme_doc']}, {I['template_sheet']}, evt_fd469c29811879519c2c96"),
                    ("intake checklist", I["esg_checklist_doc"]), ("UA spend buckets", I["ua_buckets_doc"]),
                    ("Vendor & partner tracker", I["tracker_sheet"]), ("Vendor & partner paperwork", IDS["paperwork_folder"]),
                    ("Spotlight Fest", f"{I['spotlight_thread']}, evt_564a16d0f5f6598d0360d5, C07C2866011/1758134460.899858")]:
    A(f"| \"{term}\" | NEW TERM — introduced in {where} | reached via the hub {I['hub_thread']} or its delegations |")
for k in [m["key"] for m in B.M if m["decision"] != "out" and not m.get("base") and m["key"] not in ("Lanternfly Publishing", "Clipforge", "Spotlight Fest")]:
    A(f"| \"{k}\" | NEW TERM — introduced in {IDS['threads'].get(k, '?')} | 0 base hits over 10 services (plan/name_census.json, complete scans) |")
A("")
A("Name census with a positive control: plan/name_census.json counts every seeded company name over gmail, slack, gdocs, gdrive, contacts, trello, gsheets, gslides, linear and gcal (scan_complete true, 0 hits each); the base names above are the positive controls (each returns its cited record).")
A("")

# ---------------------------------------------------------------- 1.E
A("## 1.E Persona reach")
A("")
A(f"Load-bearing ids (seeded and base) written to `Working_Files/plan/lb_ids.txt` ({len(open(os.path.join(HERE, 'lb_ids.txt')).read().split())} ids); output verbatim:")
A("")
L.extend(fence(rd("checksql.txt")))
A("")
A(f"- C07C2866011 — #executives, Frederick a member (EMPLOYEE_0008_SLACK_ID in members_json) LB; seeded posts {SL['july_sign_note']}, {SL['robert_cancel_all']}, {SL['spotlight_note']}, {SL['amendment_root']}, reply {SL['framewell_waiver_reply']}.")
A(f"- D05S58U4SAK — Frederick's DM with Leonard (im member) LB; seeded thread reply {SL['lanternfly_dm']} (D05S58U4SAK/1759174260.052645) under the base root c148cae9de21cd26027d8bbc89bb127c (D05S58U4SAK/1758151772.570449), whose counters the SQL updates.")
A(f"- Frederick's mailbox: the hub {I['hub_thread']}, ESG's thread {I['esg_thread']}, the notice {I['clipforge_notice_thread']} and every member thread (Facts for the human) are INBOX/SENT copies in {FRED} LB.")
A(f"- Drive: {I['q4_folder']} and {I['ua_buckets_doc']} are Frederick-owned; {I['guardrails_doc']}, {I['readme_doc']}, {I['template_sheet']} and {I['esg_checklist_doc']} are shared with him (shared_with_emails); the counterparties' papers are Frederick-owned copies he filed in {IDS['paperwork_folder']} LB.")
A("- Calendar: evt_fd469c29811879519c2c96 (January review), evt_564a16d0f5f6598d0360d5 (Spotlight call) and evt_0a5e42c3aac62434ba2cfc (kickoff) are Frederick's own copies (self:true) LB.")
A(f"- Unscoped (visible to all): ZOM-567, cmt_c9a6660d81e067ad1de7, {I['keep_card']}, {IDS['keep_items'][2]}, 9b0185e445572aeee9f27d35.")
A("- No designed denial: denied_probes is empty; other people's mailbox and calendar copies are companions, never evidence (the review is cited only by Frederick's copy evt_fd469c29811879519c2c96).")
A("")

# ---------------------------------------------------------------- 1.F
idc = json.load(open(os.path.join(HERE, "id_checks_sql.out.json")))["checks"]
A("## 1.F Collision")
A("")
A("Every id the SQL mints was looked up over its full base collection (`tools/hg.py records --request plan/id_checks_sql.json`, `hg.py search lookup`):")
for k, c in idc.items():
    A(f"- {k}: {c.get('records_checked')} base records checked, scan_complete {c.get('scan_complete')}, 0 matches (plan/id_checks_sql.out.json).")
A("- slack: the 7 seeded message ids over messages/*/*.json — 4,840 of 4,840 files, scan_complete true, 0 hits (plan/slack_lookup.out.json); the new Spotlight note fc2f69c06b333f6c54dfd63d455c3958 (C07C2866011/1758134460.899858) also 0 hits in the 16 #executives month files.")
A("- gmail: thread ids (mailbox/((ms << 20) + bits)) and RFC Message-IDs are minted per seeded time; base_check Check A (full-collection uniqueness through its base caches) PASS, see Self-review.")
A("- Header tokens: PERSON_9701–9735_EMAIL and SVC_9701_EMAIL are new identities (census in plan/token_census.txt); PERSON_2694 (ESG partner), PERSON_2599 (ESG intake) and PERSON_0527 (Balancy) are reused only for their own people.")
A("- Body tokens: none minted.")
A("")

# ---------------------------------------------------------------- record ledger
A("## Record ledger")
A("")
A("One row per SQL statement (inserts and the companion updates), in SQL order.")
A("")
A("| # | SQL line | Table | Id | Manifest element | Carrier | Reach | Discovery role |")
A("|---|---|---|---|---|---|---|---|")
for n, x in enumerate(STM, 1):
    rid = rid_of(x)
    el = element_for(x, rid)
    A(f"| {n} | L{x['line']} | {x['table']}{' (UPDATE)' if x['op'] == 'update' else ''} | {rid} | {el} | {CARRIER.get(x['table'], '●')} | "
      f"{reach_for(x)} | {role_for(x, rid, el)} |")
A("")

# ---------------------------------------------------------------- findability
A("## Findability and discovery-order proofs")
A("")
A(f"- Hub (A1) {IDS['msg']['hub']} in {I['hub_thread']}: Leonard → Frederick, Sep 30 23:20Z; the prompt names it ('Leonard's vendor and partner email'); a gmail search for 'vendor' or 'partner' returns it first (newest). First link.")
A(f"- Guardrails doc H1 {I['guardrails_doc']}: the hub names 'the runway guardrails doc'; a Drive/Docs search for 'runway guardrails' returns it; competing hit the UA buckets doc {I['ua_buckets_doc']} (Frederick's own, Sep 16, about UA spend: decoy_scope team) and Frederick's Sep 15 framing C07C2866011/1757961037.465799.")
A(f"- ESG note H2 {IDS['msg']['esg_note']} + Leonard's ack {IDS['msg']['esg_ack']} (thread {I['esg_thread']}): the hub names 'ESG's note about signing'; a gmail search for 'ESG' or 'signing' returns the thread; the competing first hit is Leonard's July Slack note {SL['july_sign_note']} (C07C2866011/1753207800.603298), which a Slack search for 'accept the terms' or 'sign' returns.")
A(f"- Keep-running card H3 {I['keep_card']} (checklist {IDS['keep_checklist']}): the guardrails name 'Arthur's keep-running list on our board'; trello search 'keep-running' returns the card; the decoy is the base card 688c4fa78031638f0804a994 'cancel browsestack if not used'.")
A(f"- T1 DONE: claim met first — the base portal mail {BASE['nintendo_regdone']} (Registration Completed, Sep 4) and Frederick's #executives post C07C2866011/1757011358.730529, returned by any 'Nintendo' search; overturned by Arthur's ZOM-567 comment cmt_c9a6660d81e067ad1de7 (Sep 25), reached by linear search 'Nintendo' (the issue description names the portal) and linear_list_comments; decisive because only the comment says the org account stays limited until an officer accepts the Global ToS and NDA (lapses Oct 15).")
A(f"- T2 CORR: claim met first — the order form {IDS['papers']['Framewell']} and quote thread {IDS['threads']['Framewell']} (Pro from Nov 1); overturned by Leonard's reply {SL['framewell_waiver_reply']} (Sep 26) under his Sep 21 PT Playtestcloud root C07C2866011/1758513190.847889; met first because the mail search hits the quote and channel history lists roots only; rev4: the reply names Maren (who signs the quote thread) and 'the Pro plan', not Framewell, so it is found by a Slack search for 'Maren' or 'Pro plan' or by opening the root's replies.")
A(f"- T3 COMPL: claim met first — Wen's unanswered Sep 22 'Any news on the proposal?' in {IDS['threads']['Lanternfly Publishing']}; overturned by Leonard's DM D05S58U4SAK/1759174260.052645 (Sep 29: called them back Saturday); found by a Slack search for 'Lanternfly' or by reading the DM.")
A(f"- T4 EXC: the notice {IDS['threads']['Pingwise']} says Team $29/month from Nov 1 (cash in window); the guardrails' Keep clause points at the card; the checklist item {IDS['keep_items'][2]} names the function ('the night pager for backend outages') and Pingwise's own paper {IDS['papers']['Pingwise']} names 'on-call alerting ... phone and SMS paging' — the join is by function, not by name.")
A(f"- T5 DATE: claim met first — the pilot agreement {IDS['papers']['Clipforge']} and the July tracker {I['tracker_sheet']} (free through Jan 15); overturned by the Paylane notice {IDS['msg']['clipforge_notice']} (Sep 12; workspace HG-2291, pilot ends Oct 15, cancel in writing to billing@paylane.io); a 'Clipforge' search does not return it (no company name); joined through HG-2291 in the welcome mail {IDS['msg']['Clipforge:0']} and the Jul 14 kickoff evt_0a5e42c3aac62434ba2cfc.")
A(f"- T6 FILT: Pixel Harbor's quote thread {IDS['threads']['Pixel Harbor Events']} is dated Jun 18 (outside a September search window); the hub's scope has no date limit; the paper {IDS['papers']['Pixel Harbor Events']} still asks a $2,400 deposit by Oct 10; found by a 'quote' / 'booth' / 'deposit' search without a date filter or by the July tracker {I['tracker_sheet']}.")
A(f"- T7 SIGN: the July note {SL['july_sign_note']} is met first by a Slack search; ESG's note and Leonard's Sep 25 ack ('This replaces what I said in July') overturn it; Markward's click-through {IDS['papers']['Markward']} therefore goes to an officer (card).")
A(f"- T8 review date: the guardrails say 'the January commitments review I'll put on our calendars' (Sep 26); the date is the review event evt_fd469c29811879519c2c96 (Mon Jan 5, 2026 17:00Z, created Sep 29) with its invitation {IDS['invites']['inv_review:' + FRED]}.")
A(f"- T9 AMEND: the guardrails' travel clause (only when we book them ourselves) is met first; the hub's 'one change I posted in #executives on Monday' points at {SL['amendment_root']} (C07C2866011/1759166100.370044, Mon Sep 29); Wishwave's paper {IDS['papers']['Wishwave']} has partner-booked travel.")
A(f"- Robert's cancel-all post {SL['robert_cancel_all']} (T10) is a non-authoritative instruction; Robert's Spotlight note {SL['spotlight_note']} (C07C2866011/1758134460.899858; rev4: 'the call about the Dec 5 indie showcase … I let Rina know') is found by a Slack search for 'showcase' or 'Rina', or by reading #executives for Sep 17. Hootline (rev4, T20) is found by an undated mail search ('promo', 'scheduler', 'Hootline') or a mailbox listing from early August: thread {IDS['threads']['Hootline']} has messages on Aug 5 and Aug 12 only and no filed paper.")
A("")

# ---------------------------------------------------------------- self-validation
A("## Self-validation")
A("")
A("| QC category | Tool-enforced (result) | Manual (evidence) |")
A("|---|---|---|")
A(f"| Missing Universe Data | check-sql PASS (1.E) | every deciding fact persona-readable: ZOM-567 comment cmt_c9a6660d81e067ad1de7, reply {SL['framewell_waiver_reply']}, DM D05S58U4SAK/1759174260.052645, checklist item {IDS['keep_items'][2]}, notice {IDS['msg']['clipforge_notice']}, June quote {IDS['threads']['Pixel Harbor Events']} |")
A(f"| Temporal Field | sql_lint 0 errors; base_check Check C PASS | text dates agree: the hub (Tue Sep 30) says 'the one change I posted in #executives on Monday' = {SL['amendment_root']} (Mon Sep 29); Leonard's DM (Mon Sep 29) says 'on Saturday' = Sep 27; the README (Sep 30 22:40Z) and template (22:45Z) predate the hub (23:20Z); the review event was created Sep 29 for Mon Jan 5, 2026 |")
A(f"| Cross-service Referential | base_check Check A PASS | one name and amount per company across thread, paper and Slack (Framewell $149/month in {IDS['papers']['Framewell']} and {IDS['msg']['Framewell:0']}; Pixel Harbor $2,400 by Oct 10 in {IDS['papers']['Pixel Harbor Events']} and {IDS['msg']['Pixel Harbor Events:0']}) |")
A("| Quantitative | reply counters updated on the Playtestcloud root c41d37178fca394c135408d2b38e0879 (reply_count 1, latest_reply 1758920520.674991); Trello badges match the checklist (4 items, 0 checked) | no figure is quoted against a base row; no totals are seeded |")
A(f"| State / Lifecycle | ZOM-567 Todo without stamps | the keep-running card {I['keep_card']} sits in Doing (not Done, so L12 does not apply); Nova's offer is withdrawn in its own thread {I['nova_thread']} |")
A("| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A); roster addresses in every seeded row (I03) |")
A(f"| Semantic / Category | — | titles match content ({I['guardrails_doc']}, {I['readme_doc']}, {I['keep_card']}, evt_fd469c29811879519c2c96) |")
A("| Other | — | voice per 1.C; no record states a decision, a total or the log |")
A("")

# ---------------------------------------------------------------- integrations
A("## Integrations and companions")
A("")
A("| Service | INT id | Companion | Decision |")
A("|---|---|---|---|")
A(f"| gcal | INT-11 | invitation mails | seeded: the January review (Frederick {IDS['invites']['inv_review:' + FRED]}, Robert, Arthur; Leonard organizes) and the Spotlight call (Frederick {IDS['invites']['inv_spotlight:' + FRED]}; Robert organizes); declared exception for the Jul 14 kickoff 24cbd5ab34e4c9c132384aae9cf0a03c@hg4 (integration_exceptions: no_notify — Frederick organizes, the only other attendee is external) |")
A("| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment / Slack DM / mail digest | none: ZOM-567 has no PR; Arthur creates, assigns and comments on his own issue (no notification to Frederick) |")
A(f"| gdrive | INT-13 | Drive Slack app share DM | none: the shared docs ({I['guardrails_doc']}, {I['readme_doc']}, {I['esg_checklist_doc']}) follow the base pattern of Leonard's shares to Frederick, which carry no Drive-app DM (e.g. f_17e6175e84e745f92b3415) |")
A("| slack | INT-22 | Slack e-mail notifications | none: Frederick's base mailbox holds 2 '[Slack] … sent you a message' threads in 4,656 (complete scan; frederick@harmonygames.co_1814459351624238255.json, frederick@harmonygames.co_1814909772684074125.json, both 2024) and none for D05S58U4SAK; the seeded posts carry no @mention |")
A(f"| trello | INT-21 | no Trello→Slack integration | none (the keep-running card {I['keep_card']} posts nowhere) |")
A("| gmail, gdocs, gsheets, gslides, contacts | not integration sources | — | none |")
A("")

# ---------------------------------------------------------------- touched-data census
A("## Touched-data census and coherence hazards")
A("")
A(f"Touched data: the hub {I['hub_thread']} and its copies; the guardrails doc {I['guardrails_doc']} and the UA decoy {I['ua_buckets_doc']}; ESG's thread {I['esg_thread']}, checklist {I['esg_checklist_doc']} and intake contact 9b0185e445572aeee9f27d35; "
  f"the Q4 folder {I['q4_folder']} with README {I['readme_doc']} and template {I['template_sheet']}; the July tracker {I['tracker_sheet']}; the founders' board 640643a3fd8f3ca308d9318e (keep-running card {I['keep_card']}, base card 688c4fa78031638f0804a994); "
  f"#executives C07C2866011 (Jul 22, Sep 4, Sep 15–29: base C07C2866011/1757011358.730529, C07C2866011/1757961037.465799, root C07C2866011/1758513190.847889 whose counters the SQL updates, C07C2866011/1756832039.396149); the DM D05S58U4SAK (Sep, including the base root D05S58U4SAK/1758151772.570449 whose counters the SQL updates); "
  f"ZOM-567; the Paylane notice {I['clipforge_notice_thread']}; the three calendar events; every member thread and paper (Facts for the human); and the base threads a correct run opens: {BASE['nintendo_ndareq']}, {BASE['nintendo_regdone']}, {BASE['balancy_thread']}, {BASE['rayking_thread']}, {BASE['playable_factory_thread']}, {BASE['gamesforum_thread']}, {BASE['interco_thread']}, {BASE['google_thread']}, {BASE['singular_renewal']}, {BASE['ncsoft_report']}, {BASE['dentsu_thread']}, {BASE['esg_engagement']}.")
A("")
A("Hazards from coherence_hazards.json:")
A(f"- temporal: T02 — every seeded thread is in chronological order (base_check Check C; e.g. {IDS['threads']['Lanternfly Publishing']}: Sep 9, Sep 10, Sep 22); T03 none in scope (every seeded date parses; RFC-2822 dates as in the base).")
A("- semantic: S04 (Frederick's GitHub 'Ryan') avoided — no GitHub record touched; S01–S03 none in scope — no Linear key is cited outside Linear and no label is written; the seeded contacts are counterparties with the company as job (9b0185e445572aeee9f27d35, a6ebc7683d450b0017b8acf3).")
A(f"- referential: R08 (invitation mails vs calendar) — every seeded meeting has its invitation copies (evt_fd469c29811879519c2c96, evt_564a16d0f5f6598d0360d5) except the declared no_notify kickoff 24cbd5ab34e4c9c132384aae9cf0a03c@hg4; R01 none in scope — ZOM-567 is cited only in Linear.")
A("- quantitative: Q01/Q02/Q03 — the seeded reply under C07C2866011/1758513190.847889 updates the root's reply_count 1, reply_users_count 1 and latest_reply 1758920520.674991 (companion UPDATE; hazard_acknowledgements Q01 dated_claim, the reply is an attributed dated claim); rev4: the seeded DM reply under D05S58U4SAK/1758151772.570449 (base c148cae9de21cd26027d8bbc89bb127c) updates that root's reply_count 1, reply_users_count 1 and latest_reply 1759174260.052645 (second Q01 acknowledgement); Q04 none in scope — every seeded Slack row carries reply_count / reply_users_count fields like the base.")
A("- state/lifecycle: L08 — ZOM-567 is assigned to Arthur (active at the clock per activity.json) and stays Todo because the officer step is pending (cmt_c9a6660d81e067ad1de7); L12 none in scope — the keep-running card is in Doing.")
A(f"- identifier/format: I03 — seeded rows use the roster address {FRED} (base thread files use the frederick@ alias); I16 — Trello ids encode their action time ({I['keep_card']} = 2025-08-12T16:05Z).")
A("")
A("Known data issues (references/known_data_issues/synthcut.md, read for every touched record; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):")
A(f"- SC-39 (Singular payment plan): Singular is off the log by the hub's exclusion; its renewal thread {BASE['singular_renewal']} is never read for a value.")
A(f"- SC-49 (founder count, Frederick's role): no founder count or status is graded; the role review rests on activity (C07C2866011/1757011358.730529, {BASE['balancy_thread']}).")
A("- SC-7 (channel membership): membership is used only for reach (C07C2866011, D05S58U4SAK), never graded.")
A(f"- SC-24 / SC-55 (Mattel contact, RFP deadline): Mattel is a boundary ('Leonard keeps it', C07C2866011/1756832039.396149); no Mattel person or date is graded.")
A("- SC-54 (Frederick's pay): FINANCE tables untouched.")
A("")

# ---------------------------------------------------------------- intended disagreements
A("## Intended disagreements")
A("")
A("| Claim met first | Overturning record | Why realistic | Resolution |")
A("|---|---|---|---|")
A(f"| Nintendo 'Registration Completed' ({BASE['nintendo_regdone']}, Sep 4) and Frederick's 'I registered an account' (C07C2866011/1757011358.730529) | Arthur's comment cmt_c9a6660d81e067ad1de7 on ZOM-567 (Sep 25): the org account stays limited until an officer accepts the Global ToS and NDA; lapses Oct 15 | portals finish sign-up before the legal step; the base Sep 4 mail {BASE['nintendo_ndareq']} already asked for ToS & NDA acceptance | Sign, card, next date Oct 15 |")
A(f"| Framewell order form, Pro billed from Nov 1 ({IDS['papers']['Framewell']}) | Leonard's reply {SL['framewell_waiver_reply']} (Sep 26): no charge until Feb 1 | vendors extend free periods by phone; founders mention it in passing | Park, revisit Jan 5 |")
A(f"| Wen's unanswered 'Any news?' (Sep 22, {IDS['threads']['Lanternfly Publishing']}) | Leonard's DM D05S58U4SAK/1759174260.052645 (Sep 29): he called them back on Saturday | a CEO answers a publisher by phone | Answered by Leonard, revisit Jan 5, no new reply |")
A(f"| Pilot free through Jan 15 (agreement {IDS['papers']['Clipforge']}; July tracker {I['tracker_sheet']}) | Paylane notice {IDS['msg']['clipforge_notice']} (Sep 12): cap reached, pilot ends Oct 15, $1,800/month from Oct 16 | pilots end early on a usage cap; processors notify by workspace id | End, cancel in writing by Oct 15 |")
A(f"| Leonard's July note: Frederick may accept small terms himself ({SL['july_sign_note']}) | ESG's note {IDS['msg']['esg_note']} and Leonard's ack {IDS['msg']['esg_ack']} ('This replaces what I said in July') | counsel tightens signing while raising | officer signs; card |")
A(f"| Guardrails: travel and event costs count only when we book them ({I['guardrails_doc']}, Sep 26) | Leonard's Sep 29 change {SL['amendment_root']}: they count even when a partner books them | founders amend rules in Slack | Wishwave End |")
A(f"| Robert: cancel every marketing tool ({SL['robert_cancel_all']}, Sep 25) | the guardrails doc (Sep 26, Leonard) decides per company | a co-founder vents before the CEO writes the rule | the guardrails apply; Robert's post decides nothing |")
A(f"| Frederick's July 31 tracker as the population ({I['tracker_sheet']}) | the hub's scope over the mail since June ({I['hub_thread']}) | a stale personal tracker | the scope rule decides; the tracker is a lead |")
A("")

# ---------------------------------------------------------------- constraints for the prompt brief
A("## Constraints for the prompt brief")
A("")
A("| Anchor | May be named (noun phrases only) | Record |")
A("|---|---|---|")
A(f"| A1 | Leonard's vendor and partner email; Leonard's email from yesterday | {I['hub_thread']} |")
A(f"| A2 | my Q4 commitments folder; the Q4 commitments folder | {I['q4_folder']} |")
A("")
A("Never name in the prompt: the guardrails doc's rules or location, ESG's note or its intake address, the keep-running card or its items, ZOM-567 or any Linear comment, Leonard's DM, Leonard's reply under the Playtestcloud post, the Sep 29 change, the Paylane notice or HG-2291, the January review event, Robert's Spotlight note, the July tracker, any company name, decision, date, amount or count. Deadlines: Frederick's today is Wed Oct 1, 2025; Leonard asks for written answers 'this week'. Deliverable kinds: one log sheet in the Q4 commitments folder, written answers and cancellations by mail, revisit reminders on the calendar, founders' board cards for signatures, ESG intake emails, Contacts entries, one reply on the hub thread.")
A("")

# ---------------------------------------------------------------- fact sheet
A("## Fact sheet")
A("")
A("| Key | Value | Kind | Home / must appear in |")
A("|---|---|---|---|")
for f in MAN["facts"]:
    where = ", ".join((f.get("home_ids") or []) + (f.get("must_appear_in") or []))
    A(f"| {f['key']} | {f['value']} | {f['kind']} | {where} |")
A("")
A("Clause facts use the `status` kind: the `name` kind's near-spelling scan flags the sub-windows of a correct multi-word mention (fact_check, verified on this SQL), so phrases are held to an exact match instead.")
A("")
L.extend(fence(rd("fact_check.txt")))
A("")
ag = collections.Counter(v["Decision"] for v in TRUTH.values() if v.get("Decision"))
grp = collections.Counter(g for v in TRUTH.values() for g in v.get("groups") or [])
A(f"Solver totals (`solver/truth.json`, sha256 273cbd92ab32c38e): {len(TRUTH)} companies looked at; {sum(ag.values())} on the log "
  f"(Answered {ag['Answered']}, End {ag['End']}, Keep {ag['Keep']}, Sign {ag['Sign']}, Park {ag['Park']}); written answers {grp['written_answer']}, "
  f"January revisits {grp['revisit']}, signature cards {grp['card']}, ESG intake emails {grp['esg']}, new contacts {grp['contact_add']}; "
  f"{len(TRUTH) - sum(ag.values())} off the log (boundary records).")
A("")

# ---------------------------------------------------------------- facts for the human
A("## Facts for the human")
A("")
A("| Locator | Base/seeded | Fact | Reach | Role |")
A("|---|---|---|---|---|")
rows_h = [
    (IDS["msg"]["hub"], "seeded", f"Leonard → Frederick, cc Robert, Arthur, 2025-09-30T23:20Z, subject 'Vendor and partner stuff while I'm in LA': scope rule, guardrails, the Monday change, ESG's note, answers this week, Contacts, log in the Q4 folder per the README, reply with what we keep and what waits on a signature (thread {I['hub_thread']})", "Frederick's INBOX", "authority (hub, anchor A1)"),
    (I["guardrails_doc"], "seeded", "Leonard, Sep 26 16:00Z, 'Runway guardrails - Q4 commitments': already answered → cash test Oct 1–Dec 31 (trials that convert count; travel only when we book) → Keep (Arthur's keep-running list) → Sign (ESG's note) → Park (January review); portals and no-reply notices need no answer", "shared with Frederick", "authority H1"),
    (I["ua_buckets_doc"], "seeded", "Frederick, Sep 16, 'UA spend buckets (Q4)': UA ad spend only", "Frederick owns", "decoy (H1, team scope)"),
    (IDS["msg"]["esg_note"], "seeded", f"ESG partner → Leonard, cc founders, 2025-09-24T20:05Z: only Leonard or Arthur accept terms; auto-renewal, exclusivity, IP licence or term > 12 months to ESG intake first, one email each; mutual NDAs on ESG's template need no review (thread {I['esg_thread']})", "Frederick's INBOX", "authority H2"),
    (IDS["msg"]["esg_ack"], "seeded", "Leonard, 2025-09-25T16:30Z: 'This replaces what I said in July'; cards on the founders' board To Do list with the company name; intake checklist shared", "Frederick's INBOX", "overturning (T7)"),
    (I["esg_checklist_doc"], "seeded", "ESG Law intake checklist (company, term/renewal, exclusivity/IP, cost, date needed, signer)", "shared with Frederick", "authority (ESG email content)"),
    ("9b0185e445572aeee9f27d35", "seeded", "Contacts: ESG Law intake, PERSON_2599_EMAIL", "unscoped", "write target address"),
    (I["readme_doc"], "seeded", "Leonard, Sep 30 22:40Z: one row per company, sheet 'Q4 commitments log', columns, Next date definitions, Contacts rule", "shared with Frederick", "authority (log format)"),
    (I["template_sheet"], "seeded", "header row Company · Contact · What's waiting · Decision · Answered by · What we told them · Next date", "shared with Frederick", "write target (copy)"),
    (I["q4_folder"], "seeded", "Frederick's 'Q4 commitments' folder (Sep 29)", "Frederick owns", "write target (anchor A2)"),
    (I["tracker_sheet"], "seeded", "Frederick's Jul 31 'Vendor & partner tracker' (Clipforge free through Jan 15; Pixel Harbor deposit Oct 10)", "Frederick owns", "stale summary (T14) · claim met first (T5)"),
    (I["keep_card"], "seeded", "Arthur, Aug 12, 'Keep-running list (don't cut)', Doing list, founders' board", "unscoped", "authority H3"),
    (IDS["keep_items"][2], "seeded", "check item 'the night pager for backend outages (whatever wakes me up at 3am)'", "unscoped", "overturning (T4)"),
    (SL["july_sign_note"], "seeded", "Leonard, 2025-07-22T18:10Z (C07C2866011/1753207800.603298): Frederick may accept terms under $500/year himself", "#executives member", "claim met first (T7)"),
    (SL["robert_cancel_all"], "seeded", "Robert, 2025-09-25T17:04Z (C07C2866011/1758819840.884370): cancel every marketing tool", "#executives member", "distractor (T10)"),
    (SL["spotlight_note"], "seeded", "Robert, 2025-09-17T18:41Z (C07C2866011/1758134460.899858): 'had the call about the Dec 5 indie showcase. we're sitting this one out this year, I let Rina know' (Rina Takeda invited us to the Spotlight Fest indie showcase on Dec 5)", "#executives member", "evidence (Spotlight Fest answered by Robert; T19)"),
    (SL["amendment_root"], "seeded", "Leonard, Mon 2025-09-29T17:15Z (C07C2866011/1759166100.370044): travel and event costs count as cash even when a partner books them", "#executives member", "overturning (T9)"),
    ("C07C2866011/1758513190.847889", "base", "Leonard, Sep 21 PT (Sep 22 03:53 UTC): Playtestcloud results (root; reply counters updated by the SQL)", "#executives member", "container of the T2 reply"),
    (SL["framewell_waiver_reply"], "seeded", "Leonard, 2025-09-26T21:02Z (C07C2866011/1758920520.674991), reply under the Playtestcloud root: 'Maren called me back about the Pro plan … no charge until Feb 1' (Maren Holt sends Framewell's Pro order form)", "#executives member", "overturning (T2)"),
    (SL["lanternfly_dm"], "seeded", "Leonard → Frederick, 2025-09-29T19:31Z (D05S58U4SAK/1759174260.052645), reply in the DM thread under his Sep 17 'we have no localization though': rang Wen back on Saturday about their Southeast Asia deal; Southeast Asia has to wait until after the raise; pick it up again in January", "DM member", "overturning (T3)"),
    ("ZOM-567", "seeded", "Arthur, Sep 23: 'Switch: order dev kits' (Frederick registered on the portal Sep 4)", "unscoped", "connecting (T1)"),
    ("cmt_c9a6660d81e067ad1de7", "seeded", "Arthur, 2025-09-25T18:20Z: org account limited until an officer accepts the Global ToS and NDA; lapses Oct 15", "unscoped", "overturning (T1)"),
    (IDS["msg"]["clipforge_notice"], "seeded", f"Paylane (SVC_9701_EMAIL) → Frederick, 2025-09-12T14:10Z: workspace HG-2291 (UGC Studio) pilot cap reached, pilot ends Oct 15, $1,800/month from Oct 16 unless cancelled in writing to billing@paylane.io by Oct 15 (thread {I['clipforge_notice_thread']})", "Frederick's INBOX", "overturning (T5)"),
    ("evt_0a5e42c3aac62434ba2cfc", "seeded", "Jul 14 16:00Z 'UGC Studio kickoff (workspace HG-2291)', Frederick organizer, Priya Raman attendee", "Frederick's calendar", "connecting (T5 join)"),
    ("evt_fd469c29811879519c2c96", "seeded", "Mon 2026-01-05 17:00–17:45Z 'Q4 commitments review', Leonard organizer, founders invited (created Sep 29)", "Frederick's calendar", "authority (revisit date, T8)"),
    (IDS["invites"]["inv_review:" + FRED], "seeded", "INT-11 invitation for the January review", "Frederick's INBOX", "companion"),
    ("evt_564a16d0f5f6598d0360d5", "seeded", "Wed 2025-09-17 18:00–18:30Z 'Spotlight Fest showcase call', Robert organizer, Frederick attendee; description 'Showcase slot call with Rina.' (rev4: no answer in the description)", "Frederick's calendar", "evidence (the call happened; the answer is in Robert's note)"),
    (IDS["invites"]["inv_spotlight:" + FRED], "seeded", "INT-11 invitation for the Spotlight call", "Frederick's INBOX", "companion"),
    (IDS["paperwork_folder"], "seeded", "Frederick's 'Vendor & partner paperwork' folder: his filed copies of each counterparty's paper, each created 10–15 minutes after the mail that sent it", "Frederick owns", "container"),
    (BASE["nintendo_ndareq"], "base", "Sep 4: Nintendo Developer Portal 'Global ToS & NDA Acceptance Required'", "Frederick's INBOX", "evidence (T1)"),
    (BASE["nintendo_regdone"], "base", "Sep 4: 'Registration Completed'", "Frederick's INBOX", "claim met first (T1)"),
    ("C07C2866011/1757011358.730529", "base", "Frederick, Sep 4: 'I registered an account for harmonygames.'", "#executives member", "claim met first (T1)"),
    (BASE["balancy_thread"], "base", "Leonard → Balancy (PERSON_0527), Sep 11: priorities shifted, we'll circle back", "Frederick's mailbox", "evidence (Balancy answered by Leonard, later)"),
    (BASE["rayking_thread"], "base", "Sep 4 forward: Frederick's 'reply' is addressed to Leonard (nothing reached Rayking)", "Frederick's mailbox", "boundary (T18)"),
    (BASE["playable_factory_thread"], "base", "cold pitch with an unanswered follow-up", "Frederick's mailbox", "boundary (T11)"),
    (BASE["google_thread"], "base", "Google partner check-in (ad network)", "Frederick's mailbox", "boundary (T12)"),
    (BASE["ncsoft_report"], "base", "NCsoft meeting report (strategic talks)", "Frederick's mailbox", "boundary (T15)"),
    (I["nova_thread"], "seeded", "Nova Rewards offer, withdrawn on Sep 23", "Frederick's INBOX", "boundary (T16)"),
]
for k in [m["key"] for m in B.M if m["decision"] != "out" and not m.get("base")]:
    m = M[k]
    t = TRUTH.get(k) or {}
    th, pa = IDS["threads"].get(k) or {"Motive Forge": I["motive_thread"], "Spotlight Fest": I["spotlight_thread"]}.get(k), IDS["papers"].get(k)
    who = IDS["people"].get(k)
    fact = f"{m['kind']}; {m['deciding']}"
    if th:
        rows_h.append((th, "seeded", f"{k} thread{' with ' + who[1] + ' (' + who[0] + ')' if who else ''}: {fact} → {t.get('Decision')}, next date {t.get('Next date') or '-'}",
                       "Frederick's mailbox", "evidence (cohort)"))
    if pa:
        rows_h.append((pa, "seeded", f"{k} paper ({m['paper']}): Frederick's filed copy of the paper the counterparty sent", "Frederick owns", "evidence (cohort paper)"))
for loc, bs, fact, reach, role in rows_h:
    A(f"| {loc} | {bs} | {fact.replace('|', '/')} | {reach} | {role} |")
A("")

# ---------------------------------------------------------------- platform review
A("## Platform /injection review of rev1 and the rev2 changes")
A("")
A("Attempt 6ae9909f707bc2aa0a7ed6e9 (`injection-static-v2`, stored in `run_forensics/rev1/platform_injection_review.md`) reviewed rev1 (sha256 9066997d79a3): FINAL VERDICT: PASS — Checks A, B and C PASS, lint 0 FAIL / 0 CHECK / 0 INFO, no demonstrated defects. Advisories and their disposition:")
A("- B-adv (gslides.slides_pages.notes, slides_page_elements.table_json and ordinal, linear.linear_comments.sequence not in the unverified snapshot): kept — the same four columns loaded in two submitted tasks whose baselines scored on seeded data (support/completed_tasks/frederick_card_spend_q3_6ad83eebbd6456fd065bbd20, julia_zm_difficulty_baseline_2026-11-01); every other column matches the snapshot.")
A(f"- C-adv 1 (the guardrails doc {I['guardrails_doc']}, Sep 26, cited the January review 'on our calendars' while evt_fd469c29811879519c2c96 was created Sep 29): FIXED in rev2 — the doc now says the review 'comes back at the January commitments review I'll put on our calendars', so it announces the review Leonard schedules three days later; K7's delegation quote follows (design_delta).")
A("- C-adv 2 (ZOM-567 created Sep 23 numbers after base issues created Sep 24–30; card idShort 456 created Aug 12 before base 452–455): kept — the issue must predate Arthur's Sep 25 comment, the base itself holds 6 ZOM inversions and neither field has an id contract; no record states an order.")
A(f"- C-adv 3 (vendor mails say 'attached' with empty attachments_meta_json): kept — the base does the same (ESG's engagement thread {BASE['esg_engagement']}: 'I've attached the complete set' with no attachment on any of its 3 messages); attachment bytes never reach the agent in HarmonyGames runs (Ask_Carriers §2.2), the Gmail attachment encoding is unverified (Ask_Carriers §7), and each paper is Frederick's filed copy in {IDS['paperwork_folder']}, created 10–15 minutes after its mail. Rewording to 'shared' was rejected: the vendors cannot share files Frederick owns.")
A(f"- C-adv 4 (Markward {IDS['papers']['Markward']} and Playfuse {IDS['papers']['Playfuse']} TITLE style runs shorter than the first line): FIXED in rev2 — every doc's TITLE run now covers its whole first line.")
A("Rev2 changes exactly three rows (the guardrails doc and the two papers); no trap, fact, answer or truth value changes (truth.json identical; `oracle_kit` regression against rev1 PASS).")
A("")
A("### Platform /injection review of rev2")
A("")
A(f"Attempt 6ae9909f707bc2aa0a7ed6e9, rev 4 on the platform (sha256 795bd191872d…b4713f, stored in `run_forensics/rev2/platform_injection_review.md`): FINAL VERDICT: PASS — the 3 changed rows checked fresh, Drive and Docs collisions re-run, the other 292 rows reused from the rev1 review under stage-evidence-v1; C-adv 1 and C-adv 4 confirmed resolved ('I'll put on our calendars' in {I['guardrails_doc']}; TITLE runs 0–43 and 0–56); B-adv, C-adv 2 and C-adv 3 remain advisories with the dispositions above. Next: /prompt, then /hardness, /oe and /rubric on this exact SQL.")
A("")
A(f"Platform load (changelog `public._changelog`, stored in `run_forensics/rev2/platform_changelog.json`): 295 operations in one transaction at 2026-11-03T19:55:26Z, per-table INSERT/UPDATE counts equal to the SQL (260 + 35) and every statement matched to its entry; the guardrails doc {I['guardrails_doc']} loaded with the rev2 wording; the four B-adv columns are present in the loaded rows (slides_pages.notes 7 rows, slides_page_elements.table_json and ordinal 14 rows, linear_comments.sequence on cmt_c9a6660d81e067ad1de7), so the snapshot advisory is settled by the live load.")
A("")

A("### Rev3: fork sweep at the prompt-brief stage")
A("")
A("Before the prompt brief, an independent agent read only Frederick-visible records (no solver, manifest or surface) and listed every value two careful readers could set differently (`Working_Files/plan/blind_fork_sweep.md`). Each unsettled fork was settled in a record, keeping the solver's truth (the Lanternfly told text is read from the DM, so `oracle_kit` regression against rev2 holds):")
A(f"- Scope: the hub now names PlayableX and Craftsman+ (UA-side vendors Frederick can see: base Slack C08H78VJG80, thread frederick.stone@harmonygames.co/1823332883409810377) with the ad networks and Singular on the UA budget call.")
A(f"- Cash test vs Park for pay-when-you-order offers: the guardrails {I['guardrails_doc']} now say an offer we would have to take up and pay for before January counts as cash, and Park covers offers we could still take up after that.")
A(f"- Framewell (CORR): Leonard's reply {SL['framewell_waiver_reply']} adds 'with nothing to sign before then' (no Sign reading).")
A(f"- Nintendo (DONE): Arthur's comment cmt_c9a6660d81e067ad1de7 reconciles the base 'NDA Effective: 09/04/2025' ({BASE['nintendo_regdone']}: Frederick is only the administrator; the agreement approver must be an officer), says the click-through has no fee, exclusivity or IP licence and can be ended by either side (no ESG trigger), gives 'accepted by Oct 15', and defers the kits until after the raise (no cash reading).")
A(f"- Lanternfly (COMPL): Leonard's DM D05S58U4SAK/1759174260.052645 now says Southeast Asia has to wait until after the raise (the base shows other publishing outreach and Kinetic Arcade's LOI stays a Sign row).")
A(f"- Plain noes, no 'later' reading: Robert's note {SL['spotlight_note']} drops 'maybe next year'; Arthur's Motive Forge reply in {I['motive_thread']} drops 'this quarter … for now'.")
A(f"- Dates: Brightlane and Ascendo follow-ups ask to confirm by Oct 1; Reviewly's terms {IDS['papers']['Reviewly']} say 'cancelled by Oct 19'; Playfuse's NDA {IDS['papers']['Playfuse']} says 'by Oct 8, 2025 (before our call that day)'.")
A(f"- ESG and signing: Markward's terms {IDS['papers']['Markward']} have no rolling term; Bundlehouse's deck {IDS['papers']['Bundlehouse']} and follow-up make joining a signed participation agreement; Playfuse's NDA is on ESG Law's mutual NDA template (the base 2023 HG template predates ESG).")
A(f"- Waiting to hear from us: Retainly, Benchmarkly and Driftwood Audio now ask a question; Markward's Leah asks whether to hold the setup.")
A(f"- Coherence: the UA buckets doc {I['ua_buckets_doc']} no longer says the real UA bucket is paused (base Unity bids moved on Sep 29–30); Brightlane's retainer no longer includes playable work; Nova's withdrawal drops 'back and forth'.")
A(f"- Second sweep on the first rev3 build (`plan/blind_fork_sweep_rev3.md`: its independent log matched the solver row for row, 36 rows): the guardrails' Sign step now says what to tell them ('with Leonard or Arthur to sign, and with our lawyers first when ESG has to see it'); Lumencloud's and Orbit Store's mails state the application and the call; Hootline's follow-up drops the annual-plan upsell; Certwell's notice says nothing new to sign; the Paylane notice says replies to the email aren't monitored (the billing address is); Priya's Sep 22 mail no longer reports videos after the cap; Tilecast's widget is an interactive demo widget (no 'playable' wording beside the UA doc).")
A("")
A("### Platform reviews of rev3 and the rev3 Opus pre-check")
A("")
A("- /injection on rev3 (platform rev 5, sha256 2176eb708f74, `run_forensics/rev3/platform_injection_review.md`): FINAL VERDICT: PASS; new minor advisory C-adv 3 (Lumencloud 'Thanks for applying' vs 'Apply by Oct 31') dispositioned as outcome-invariant (`run_forensics/rev3/platform_injection_dispositions.md`).")
A("- /prompt on rev3 (`run_forensics/rev3/platform_prompt_review.md`): PASS, Score 5 on every dimension; STEP 0.6 nearest neighbour 0.658 (distinct).")
A("- Opus 5.5 pre-check on rev3 (265 calls, `run_forensics/rev3/precheck/`) and /hardness (`run_forensics/rev3/platform_hardness_review.md`): FAIL, Score 2, HOLD (narrow miss: only Nintendo missed). The run searched Slack for every company name and for 'told'/'vendor', read the Leonard DM's newest roots and built its cohort from the Aug 15+ inbox, the paperwork folder and the July tracker (`01a_Hardening_Report.md` §5).")
A("")
A("### Rev4: after the rev3 Opus pre-check (design-2)")
A("")
A("Each change moves where an existing record sits or how it is worded; no record is added for volume, no truth value changes (truth.json identical in every field to rev3; `oracle_kit` regression against rev3 PASS):")
A(f"- CORR (T2): Leonard's reply {SL['framewell_waiver_reply']} names Maren and the Pro plan instead of Framewell and drops 'while we're on vendors' (the pre-check found it by 'Framewell' and 'vendor after:').")
A(f"- COMPL (T3): Leonard's Lanternfly answer {SL['lanternfly_dm']} is now a reply in the DM thread under his Sep 17 root 'we have no localization though' (D05S58U4SAK/1758151772.570449, counters updated), names Wen and 'their Southeast Asia deal' and says he let them know Southeast Asia has to wait until after the raise, and drops 'Lanternfly' and 'told' (it was the DM's newest root, found three ways).")
A(f"- NOTE (T19, new rule): Robert's note {SL['spotlight_note']} names the Dec 5 indie showcase and Rina instead of 'spotlight fest' and drops 'told'; the call's description (evt_564a16d0f5f6598d0360d5) is now 'Showcase slot call with Rina.', so the note is the only carrier of the answer.")
A(f"- WIN (T20, new rule): Hootline's ask moves from Sep 24 to Aug 12 and its filed paper (f_f7902fdbb11a8bbd623959) is dropped; the terms ($39/month after Jan 31 unless cancelled) move into the Aug 5 mail ({IDS['threads']['Hootline']}).")
A("- Solver: rules NOTE and WIN with their controls (Motive Forge, Wishwave; Quillcraft, Gamesforum SF) and over-application operators; SIGN's control moves from Hootline to Echohall. Gradable surface design-2 (scenario-owned): X20 replaces X7 in the decision group, X18/X19/X21 added, Answered by and Next date compare by word (issue_key), told patterns accept 'no', 'won't', 'said no', 'passed on'.")
A("- Blind fork sweep on the first rev4 build (`plan/blind_fork_sweep_rev4.md`, a fresh agent reading only Frederick-visible records): its independent log matched the solver row for row (36 rows; Answered 4, End 10, Keep 3, Sign 7, Park 12) and tied every alias to one company (Maren → Framewell, Wen → Lanternfly, the Dec 5 indie showcase and Rina → Spotlight Fest; Hootline in scope). Its three material open forks were settled in records, keeping the truth: the Lanternfly reply now says Leonard let them know (Answered, no Park email); Priya's Sep 22 mail asks to be told too if we are not carrying on (a written answer to Priya beside the Paylane cancellation); the README's Contacts line excludes portals and no-reply senders (no Nintendo contact). Two tightenings ride along: Arthur's ZOM-567 comment adds 'no fixed term' (no ESG trigger for Nintendo), and Lumencloud's agreement says 'Sign by Oct 31, 2025 (cohort closes)' (the rev3 platform C-adv 3). Its two cosmetic forks (timed vs all-day reminders; signer 'Leonard or Arthur') are accepted both ways in the brief.")
A("Rev4 needs the platform /injection review, then /prompt with the same prompt, before the next pre-check.")
A("")

# ---------------------------------------------------------------- platform follow-ups
A("## Platform follow-ups")
A("")
A("- ○ carrier: none load-bearing — rev4 removed the answer from the Spotlight call's description (evt_564a16d0f5f6598d0360d5); Robert's #executives note C07C2866011/1758134460.899858 is the ● carrier.")
A("- Linear comment cmt_c9a6660d81e067ad1de7 is ● (Ask_Carriers §6b, linear_list_comments); confirm it renders in the pre-check like any comment.")
A("- Forecast blind spot: in exact mode the forecast never fails write-content slots (cards, sends, events, replies, the told column, the report lists), so its E[avg] 0.738 is optimistic; the design-mode view (declared mechanisms) gives 0.655. The rev3 pre-check scored about 95 %, far above both rev3 forecasts; rev4's rates are re-estimated from that run (UNCALIBRATED).")
A("- No independent red team ran (REDTEAM_* unset; fallback recorded in the scenario design §13).")
A("")

# ---------------------------------------------------------------- self-review
A("## Self-review")
A("")
A("### Tool outputs (final SQL, verbatim)")
A("")
A("`tools/sql_lint.py`:")
L.extend(fence(rd("sql_lint.txt")))
A("")
A("sql_lint warning disposition (8 warnings, one class — on/after the clock): the four copies of the Jan 5, 2026 'Q4 commitments review' carry future start/end plan fields only; it is a not-yet-happened event created Sep 29 (before the seed bound), allowed as a deadline/plan field (Ask_Carriers clock rule); no event is treated as completed.")
A("")
A("`tools/base_check.py`:")
L.extend(fence(rd("base_check.txt")))
A("")
A("base_check (run with the final manifest): 0 warnings; the INT-11 exception for the Jul 14 kickoff 24cbd5ab34e4c9c132384aae9cf0a03c@hg4 is a declared note (no_notify: Frederick organizes; the only other attendee is external).")
A("")
A("`tools/base_claims.py`:")
L.extend(fence(rd("base_claims.txt")))
A("")
A("`tools/hardness_gate.py` (final manifest + SQL):")
L.extend(fence(rd("hardness_gate.txt").replace("\nexit 0", "")))
A("")
hg = json.load(open(os.path.join(HERE, "hglint.json")))
A(f"`tools/hg.py lint` (the eval's hg_injection_lint, base data, sha256 {hg['sha256'][:12]}): counts {hg.get('counts')}. LINT: no CHECK flag to disposition; no INFO.")
A("")
A("### Preflight (S4b–S5e)")
A("")
L.extend(fence(rd("oracle_check.txt")))
A("")
L.extend(fence(rd("mutate.txt").replace("missing []", "missing: none")))   # an empty list reads as a template slot to the gate
A("")
A("Mutation dispositions (`01c_Dispositions.json`, 42 of 42): DONE, CORR, COMPL, EXC, DATE, FILT, NOTE and ch_miss are live (KILLED); SIGN, AMEND and WIN are live (they flip only write-content or delivery slots — C10, P2, C11; X18, X21, V1 — which the direct-slot diagnosis does not read and geometry counts); the ten over-application operators are weak-accepted (they move only unslotted control rows — control trials, never landings); the eleven degrade interventions are redundant (no deciding record of their own); the ten rule interventions are live (load-bearing, no escape).")
A("Geometry: U = 0.812 (112/138) > 1 − 0.90 (Easy cap) — PASS; L_max UNSUPPORTED (ten rules exceed the exact-combination limit; advisory). Liveness: 23 flags (breadcrumb, order, one rule placement; T20 adds breadcrumb and order), each weak-accepted with its reason in `01c_Dispositions.json` (the hub's delegations are the fairness links; no flag names a deciding record).")
A("")
A("`tools/preflight_report.py --forecast 01c_Forecast.json`: PREFLIGHT: PASS — blocking solver_contract, surface_validation, mutation_dispositions and geometry_upper_bound all True; advisory geometry margin OK (V3), geometry bound PASS (V3), liveness dispositions missing: none, forecast recorded; report and .md bound by sha256 to the SQL, solver, surface, manifest and dispositions.")
A("")
fc = rd("forecast_injection.txt")
fid = [l for l in fc.splitlines() if "forecast record" in l][-1].split("'id': '")[1].split("'")[0]
A(f"Forecast (UNCALIBRATED, pre-registered `{fid}`, exact solver outcomes, disclosed mechanism rates re-estimated from the rev3 pre-check and bridge analogs; SIGN and AMEND at 0.05 left out of the exact combinations): "
  "E[avg] 0.738 [0.692, 0.783]; P(all four V3 gates) 0.061–0.511 across dependence scenarios. Its exact mode never fails a write-content slot, "
  "so every landed mechanism loses only its direct slots there. The design-mode view (the scenario's pre-registered `hev_da8a164703569b79`) counts the declared write-content "
  "consequences: E[avg] 0.655 [0.591, 0.719], P(all) 0.28–0.56. Replaying the rev3 pre-check's own behaviour on the design-2 surface scores 48.6 % (`plan/policy_scores_output.txt`). "
  "Both are model outputs, not measurements; the requester's targets (> 130 calls per run, average < 80 %) are checked on the Opus pre-check (rev3: 265 calls).")
A("")
A("### Changes made at this stage (and why)")
A("")
A("- Gradable surface: the five 'What we told them' slots (X13, X15, C5, C6, C11) use `reason_matches`, which `oracle_kit.py` cannot read as a solver value; they were reclassed `write_content` (graded from the written log, unchanged weights/keys/mechanisms) and X15's pattern now keys on the DM-only words, in a scenario-stage amendment re-certified by `stage_gate.py scenario` (design bb54cb161530, surface 3f1a7f7485cc; 01_Scenario_Design.md §12).")
A(f"- SQL: Lanternfly's signature and deck now carry 'Lanternfly Publishing' (the log key; no record named it in full); Robert's Sep 17 note {SL['spotlight_note']} carries Spotlight's answer in a ● carrier (the calendar description is ○).")
A(f"- Rev2 (after the platform /injection PASS on rev1): the guardrails doc announces the January review it cites (C-adv 1) and every doc's TITLE run covers its first line (C-adv 4); see 'Platform /injection review of rev1 and the rev2 changes'.")
A("- Rev4 (after the rev3 Opus pre-check, `01a_Hardening_Report.md`): the Framewell, Lanternfly and Spotlight corrections are de-named and the Lanternfly answer moves into a DM thread; Hootline moves outside the inbox-window/folder/tracker filter; rules NOTE and WIN are added; see 'Rev4: after the rev3 Opus pre-check'.")
A("- Manifest: design_delta lists the id normalisation (Slack 32-hex ids, Gmail message rows), the T5/T7/T17 placeholders, the anchor's message row and the four control members added for the over-application operators; no preflight {report, digest} is written into the manifest because `preflight_report.py` binds the manifest by sha256 (either direction makes one stale).")
A("")
A("### /injection Checks A–C walk")
A("")
A(f"- Inventory: {n_ins} INSERT, {n_upd} UPDATE, 0 DELETE, no upserts; tables {dict(sorted(by_table.items()))}. PASS.")
A("- Check A (references and IDs): every channel, user, issue, thread, calendar, board, list and folder resolves (base_check Check A PASS); in_reply_to and references point at seeded messages; uniqueness scoped to the full collections (1.F, complete scans, 0 hits); ownership, membership and shares give Frederick reach (check-sql PASS, 1.E). PASS.")
A("- Check B (structure): sql_lint 0 errors; every *_json column is literal JSON; NOT NULL columns supplied; generated *_fts columns never written; camelCase Trello columns quoted. PASS.")
A("- Check C (dates, parents, statuses, counts): all seeded timestamps ≤ 2025-10-01T00:00Z except the Jan 5 review's plan fields; replies after their parents (the Framewell reply 4 days after its root; the Lanternfly DM reply 12 days after its Sep 17 root); both roots' counters updated; ZOM-567 Todo without stamps; Trello badges match 4 items / 0 checked; the Sep 29 change and the Sep 25 ack each postdate what they supersede. PASS.")
A("")
A("### Touched-data census")
A("")
A("See 'Touched-data census and coherence hazards' above: six hazard categories covered (T02, S04, R08, Q01–Q03, L08/L12, I03/I16) and SC-7, SC-24, SC-39, SC-49, SC-54, SC-55 dispositioned.")
A("")
A("### Counter-readings")
A("")
A("| Category | Counter-reading (strongest argument it FAILS) | Evidence that resolves it | Verdict |")
A("|---|---|---|---|")
CR = [
    ("Temporal", f"the DM reply says 'on Saturday' but is dated Monday: the call date is ambiguous", f"D05S58U4SAK/1759174260.052645 is Mon Sep 29 19:31Z; Saturday = Sep 27, before it; the answer is dated by the reply, not graded by day", "holds"),
    ("Temporal", "the guardrails doc (Sep 26) cites a January review that is only put on the calendars on Sep 29 (a record citing something created after it; platform C-adv 1)", f"rev2: {I['guardrails_doc']} now says 'the January commitments review I'll put on our calendars'; evt_fd469c29811879519c2c96 is created Sep 29 by Leonard, as announced", "holds (fixed in rev2)"),
    ("Temporal", "the review event's start (Jan 5, 2026) is after the clock, so it 'already happened' in no record", "evt_fd469c29811879519c2c96 is a plan field created Sep 29 (sql_lint clock warnings dispositioned); nothing claims it happened", "holds"),
    ("Temporal", f"the hub's 'the one change I posted in #executives on Monday' could mean a Sep 22 post", f"{SL['amendment_root']} is Mon Sep 29 17:15Z; the only Leonard post about the guardrails; the hub is Tue Sep 30", "holds"),
    ("Semantic / Category", "the keep-running card is in Doing, so it reads as a task in progress rather than a standing list", f"{I['keep_card']} desc 'Stuff the live game needs to keep running. Ask me before cancelling any of it.'; the guardrails name it a list", "holds"),
    ("Semantic / Category", "'Lanternfly' and 'Lanternfly Publishing' could be two companies", f"one sender PERSON_9702_EMAIL signs 'Lanternfly Publishing' in {IDS['threads']['Lanternfly Publishing']}; the deck {IDS['papers']['Lanternfly Publishing']} uses the full name", "holds"),
    ("Cross-service Referential", "the Paylane notice never says Clipforge, so a reader may treat it as an unknown vendor", f"HG-2291 appears in the welcome mail {IDS['msg']['Clipforge:0']}, the pilot paper {IDS['papers']['Clipforge']} and the kickoff evt_0a5e42c3aac62434ba2cfc (fact 'Clipforge workspace', fact_check PASS)", "holds (designed join, T5)"),
    ("Cross-service Referential", "Arthur's comment says 'the portal' without naming Nintendo", "ZOM-567's description names the Nintendo developer portal and Frederick's Sep 4 registration (C07C2866011/1757011358.730529)", "holds"),
    ("Quantitative", "Pixel Harbor's deposit ($2,400) and price ($4,800) could be read as two amounts for one thing", f"{IDS['papers']['Pixel Harbor Events']}: price $4,800, deposit $2,400 by Oct 10, balance by Oct 20 (fact 'Pixel Harbor deposit' home rows only)", "holds"),
    ("Quantitative", "the Playtestcloud root's reply counters disagree with the export after the seeded reply (Q01)", "c41d37178fca394c135408d2b38e0879 UPDATE: reply_count 1, reply_users_count 1, latest_reply 1758920520.674991 (hazard_acknowledgements Q01)", "holds"),
    ("State / Lifecycle", "Nintendo's 'Registration Completed' and Arthur's 'limited account' contradict each other (two live statuses)", f"intended: the Sep 4 completion is of sign-up, the Sep 25 comment adds the pending officer step, and the base Sep 4 mail {BASE['nintendo_ndareq']} already asked for ToS & NDA acceptance", "holds (designed, T1)"),
    ("State / Lifecycle", "Framewell's order form (paid from Nov 1) and Leonard's waiver are two live answers", f"the waiver {SL['framewell_waiver_reply']} is a dated human claim (Sep 26) after the form (Sep 18); best unintended reading: a stale form nobody updated; resolved because Leonard reports the vendor's phone call and nothing later restores Nov 1", "holds (designed, T2)"),
    ("State / Lifecycle", "Lanternfly's open 'Any news?' contradicts 'already answered'", "Leonard's DM D05S58U4SAK/1759174260.052645 (Sep 29) postdates the Sep 22 follow-up; the guardrails' first step says not to write again", "holds (designed, T3)"),
    ("State / Lifecycle", "the pilot agreement (free to Jan 15) and the notice (ends Oct 15) are both current", f"the notice {IDS['msg']['clipforge_notice']} (Sep 12) cites the agreement's usage cap; the July tracker {I['tracker_sheet']} predates it; best unintended reading: a phishing-like notice — resolved by the HG-2291 workspace id and the processor named in the agreement", "holds (designed, T5)"),
    ("State / Lifecycle", "the July Slack note and ESG's rule disagree on who may accept terms", f"Leonard's ack {IDS['msg']['esg_ack']} says 'This replaces what I said in July' (Sep 25)", "holds (designed, T7)"),
    ("State / Lifecycle", "the guardrails' travel clause and the Sep 29 change are two live rules", f"{SL['amendment_root']} names 'one change to the runway guardrails doc'; the hub points at it", "holds (designed, T9)"),
    ("State / Lifecycle", "Robert's 'cancel every marketing tool' could be read as a founder decision that overrides the doc", f"{SL['robert_cancel_all']} (Sep 25) precedes Leonard's doc (Sep 26) and the hub delegates to the doc, not to Robert", "holds (designed, T10)"),
    ("State / Lifecycle", "the July tracker lists ended or stale entries as current", f"{I['tracker_sheet']} is dated Jul 31 ('Status (Jul 31)'); the hub's scope over the mail decides", "holds (designed, T14)"),
    ("Identifier / Format", "a seeded mail uses frederick.stone@ while base files use frederick@ (I03), so the mailbox may look split", "all seeded rows use the roster address, the same user_email as the base messages (thread_id frederick.stone@harmonygames.co/1840501641217286806)", "holds"),
    ("Other", "the designed disagreements read as silent system fields rather than dated human claims", f"each overturning record is an authored message with a date and a reason (cmt_c9a6660d81e067ad1de7, {SL['framewell_waiver_reply']}, D05S58U4SAK/1759174260.052645, {IDS['msg']['esg_ack']}, {SL['amendment_root']})", "holds"),
    ("Other", "Robert's Spotlight answer could be unreachable if the note's alias does not resolve", f"Robert's #executives note {SL['spotlight_note']} names the Dec 5 indie showcase and Rina; Rina Takeda's invitation {I['spotlight_thread']} is for the Spotlight Fest indie showcase on Dec 5 and the Sep 17 call (evt_564a16d0f5f6598d0360d5, Robert organizer) ties the date", "holds"),
    ("Semantic", "the de-named Framewell reply ('Maren … the Pro plan') could be read as another vendor's plan", f"Maren Holt is the sender of Framewell's Pro order form ({IDS['threads']['Framewell']}); no other seeded or base record names a Maren (hg.py search slack/gmail/contacts 'Maren': only 'gsmarena' substrings)", "holds"),
    ("Semantic", "the Lanternfly DM reply ('Wen … their Southeast Asia deal') could be about another publisher", f"Wen Halvorsen signs Lanternfly Publishing's Southeast Asia proposal thread ({IDS['threads']['Lanternfly Publishing']}); 'Halvorsen' and 'SEA deal' have no other hits; Kinetic Arcade's LOI is Japan/Korea", "holds"),
    ("State / Lifecycle", "Hootline with nothing after Aug 12 and no paper could be read as a dead sign-up, not a waiting item", f"Gemma's Aug 12 question is unanswered and the promo ends Jan 31 (thread {IDS['threads']['Hootline']}); the hub's scope has no date limit and counts a sign-up", "holds (designed, T20)"),
]
for c in CR:
    A(f"| {c[0]} | {c[1]} | {c[2]} | {c[3]} |")
A("")
A("People status: everyone a rule depends on is active at the clock (Leonard, Robert, Arthur per activity.json; ESG Law is external); no Snowflake roster or Confluence headcount line is touched.")
A("")
A("Unresolved: no independent red-team review (fallback recorded); the six channels' landing rates are analogs from the completed Frederick tasks (UNCALIBRATED); calendar-description rendering unverified (supporting only); the forecast's exact mode cannot see write-content consequences.")
A("")

out = os.path.join(WF, "01_Grounding_Dossier.md")
open(out, "w").write("\n".join(L) + "\n")
print("wrote", out, len(L), "lines")

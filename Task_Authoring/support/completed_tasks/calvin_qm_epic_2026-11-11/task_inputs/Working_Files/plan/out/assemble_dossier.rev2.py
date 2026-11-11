#!/usr/bin/env python3
"""Assemble Working_Files/01_Grounding_Dossier.md from the SQL rows, the final manifest, truth.json, the id maps and the saved
tool outputs in plan/out/inj/ (each re-run on the final SQL before this script, plan/run_checks.sh). No prompt, Oracle Event or
criterion wording. Re-run after any SQL, manifest or solver change, then re-run the stage gate."""
import collections, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
OUTD = os.path.join(HERE, "out", "inj")
sys.path.insert(0, os.path.join(TI, "..", "tools"))
sys.path.insert(0, os.path.join(WF, "solver"))
from base_check import parse_sql  # noqa: E402
import solver as SV  # noqa: E402
SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
STM = parse_sql(SQL)
IDS = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
SEED = json.load(open(os.path.join(HERE, "seed_text.json")))
ID = {k: v["id"] for k, v in SEED.items()}
AT = {k: v["at"] for k, v in SEED.items()}
MAN = json.load(open(os.path.join(WF, "01_Hardness_Manifest.json")))
EXTRA = json.load(open(os.path.join(HERE, "sweep_dispositions_inj.json"))) if os.path.exists(os.path.join(HERE, "sweep_dispositions_inj.json")) else {"changes": [], "counter": [], "sweep_rows": [], "unresolved": []}
SL, GH, TR, EVT, MAIL = IDS["slack_mid"], IDS["gh"], IDS["trello"], IDS["evt"], IDS["mail"]
CAL = "calvin.price@harmonygames.co"
state = SV.load_state(SQL)
ROWS = SV.solve(state)
AG = SV.aggregates(ROWS)
TOT = AG["totals"]
BDM, VDM, MDM, BUGS, ZM3D, PRS, BUILDS = "D0770ET6WBW", "D06UPGF5PQV", "D05U73FNDDL", "C08R27X0EAH", "C0880U9751A", "C093LEZGF6J", "C05433XK267"
PR = lambda n: f"harmonygames-Games/match3d#{n}"       # noqa: E731


def rd(name):
    return open(os.path.join(OUTD, name)).read().rstrip().replace("[]", "none")


L = []
A = L.append


def fence(t):
    L.extend(["```", t, "```"])


ins = [x for x in STM if x["op"] == "insert"]
n_ins, n_upd = len(ins), len([x for x in STM if x["op"] == "update"])
by_table = collections.Counter(x["table"] for x in STM)
ELEM = collections.defaultdict(set)
ROLE = {}
for a in MAN["anchors"]:
    ELEM[a["locator"]].add(a["id"])
    ROLE[a["locator"]] = "first link"
for f in MAN["ask_fragments"]:
    for x in f.get("seeded_ids") or []:
        ELEM[x].add(f["id"])
for h in MAN["authorities"]:
    for x in h.get("seeded_ids") or []:
        ELEM[x].add(h["id"])
        ROLE.setdefault(x, "authority")
    for x in h.get("decoy_seeded_ids") or []:
        ELEM[x].add(h["id"] + " decoy")
        ROLE.setdefault(x, "decoy")
for t in MAN["traps"]:
    for x in t.get("seeded_ids") or []:
        ELEM[x].add(t["id"])
    vr = t.get("version_records") or []
    for i, v in enumerate(vr):
        x = v.get("id")
        if x:
            ELEM[x].add(t["id"])
            ROLE[x] = "overturning" if i == len(vr) - 1 else "claim met first"
for k in ("reopen", "back"):
    ROLE[SL[k]] = "overturning"
for k in ("inline", "inline2", "else_pr", "alias_gift", "alias_streak"):
    ROLE[ID[k]] = "overturning"
ROLE[SL["filt_dm"]] = "connecting (report outside the sheet)"
COMPANION = {SL["hub_hello"]: "AN1 companion (greeting)", SL["filt_dm2"]: "T_FILT companion (second line)", SL["pass_start"]: "R1 context (the pass starts on the 26th)",
             SL["pass_tickets"]: "R4 context (tickets filed from the sheet)", SL["mirror_else"]: "T_ELSE companion (INT-01)", SL["mirror_inline"]: "T_INLINE companion (INT-01)",
             SL["mirror_inline2"]: "T_INLINE_PACK companion (INT-01)", GH["inline"]["review"]: "T_INLINE container", GH["inline2"]["review"]: "T_INLINE_PACK container",
             GH["inline"]["mail"]: "T_INLINE companion (INT-12)", GH["inline2"]["mail"]: "T_INLINE_PACK companion (INT-12)", PR(473) + "#ev_5": "T_ELSE companion (timeline)",
             TR["desc1"]: "T_GATE (first description)", TR["name2"]: "T_GATE (rename to Thursday)"}
TICKETS = IDS["tickets"]
COMMENT_OF = {c: k for k, cs in IDS["comments"].items() for c in cs}


def rid_of(x):
    r = x.get("row") or {}
    t = x["table"]
    if t in ("gslides.slides_pages", "gslides.slides_page_elements"):
        return f"{r.get('presentation_id')}#{r.get('object_id')}"
    if t == "gsheets.sheets_sheets":
        return f"{r.get('spreadsheet_id')}#{r.get('title')}"
    for k in ("id", "event_id", "document_id", "spreadsheet_id", "presentation_id"):
        if r.get(k):
            return str(r[k])
    w = x.get("where") or {}
    return str(next(iter(w.values()), "?")) if isinstance(w, dict) else str(w)


def element(x, rid):
    t, r = x["table"], x.get("row") or {}
    base = rid.split("#")[0]
    if ELEM.get(rid) or ELEM.get(base):
        return ", ".join(sorted(ELEM.get(rid) or ELEM.get(base)))
    if rid in COMPANION:
        return COMPANION[rid]
    if x["op"] == "update":
        return "companion (counters or updated_at of a base parent)"
    if t == "linear.linear_issues":
        return f"cohort (sheet row {TICKETS[rid]['row']}), T_STATE" if rid in TICKETS else "cohort"
    if t == "linear.linear_comments":
        return f"cohort evidence surface (comments of {COMMENT_OF.get(rid, '?')})"
    if t == "gcal.gcal_events":
        return "K7, T_SHARE (attendee copy)"
    if t.startswith("gmail."):
        return "K20 companion (INT-11 copy in another attendee's mailbox)" if r.get("user_email") != CAL else "K20, T_GATE, D_OLDINVITE"
    if t.startswith("gslides."):
        return "K19 (R9 write target)"
    if t == "trello.trello_actions":
        return "H2, T_GATE"
    return "cohort"


def reach(x):
    t, r = x["table"], x.get("row") or {}
    if t.startswith(("linear.", "github.", "trello.")):
        return "unscoped"
    if t == "slack.slack_messages":
        return "channel or DM member"
    if t.startswith("gmail."):
        return "own mailbox" if (r.get("user_email") or CAL) == CAL else "not Calvin's (companion copy)"
    if t == "gcal.gcal_events":
        return "own calendar" if r.get("calendar_id") == CAL else "attendee copy (companion)"
    return "owner" if r.get("owner_email") == CAL else "shared with Calvin"


def role(rid, el):
    if rid in ROLE:
        return ROLE[rid]
    if "companion" in el or "container" in el or "context" in el:
        return "connecting"
    if "write target" in el:
        return "write target"
    if "decoy" in el:
        return "decoy"
    return "connecting"


A("# Grounding Dossier — calvin_qm_epic · injection rev2 · contains no prompt, OE or criterion text")
A("")
A(f"Persona: Calvin Price <{CAL}>, Game Engineer (Unity VFX). Universe: synth-cut, clock 2025-10-01T07:00Z, seed bound 2025-10-01T00:00:00Z (Tue Sep 30 17:00 PT). SQL: {n_ins} INSERT, {n_upd} UPDATE, 10 schemas. Every base read at this stage went through `tools/hg.py`; one directory listing of the mail export's file names was made by mistake to learn the thread file naming and is disclosed in the Self-review.")
A("")
# ---------------------------------------------------------------- 1.A
A("## 1.A Structural")
A("")
A("Columns checked against `references/universe_schema_live.json`; NOT NULL columns marked !; shapes copied from the sibling records named here.")
A("")
A("| Table | Columns used (NOT NULL marked) | Location and sample ids | Notes |")
A("|---|---|---|---|")
for row in [
    ("slack.slack_messages", "id!, ts!, channel_id!, text, thread_parent_id, thread_ts_legacy, reply_count, attachments_json, created_at", f"messages/{BDM}/2025-09.json ({BDM}/1759173978.039839), messages/{BUGS}/2025-09.json ({BUGS}/1757939514.864549), messages/{PRS}/2025-09.json ({PRS}/1759247580.373799)", "id = the first 32 hex of the sha256 of channel, a pipe and ts; replies keep the root's id in thread_parent_id; GitHub-app copies have empty text and one attachment, as base copies do"),
    ("gmail.gmail_threads / gmail_messages", "id!, user_email!; id!, thread_id!, user_email!", f"threads/calvin@harmonygames.co_1842050583560498707.json (an invitation), threads/calvin@harmonygames.co_1844639618018823785.json (GitHub mails for {PR(472)}), threads/calvin@harmonygames.co_1844705205220700048.json ({PR(475)})", "thread id = (ms<<20)+bits; one row per mailbox copy; the two GitHub mails join the base PR threads and copy the base approval mails' From, To, Cc and Reply-To"),
    ("gdrive.drive_files / gdocs / gsheets / gslides", "id!, name!, mime_type!; document_id; spreadsheet_id; presentation_id", "gdrive data.json d_49b9dfa5208d400d9b3937, d_65c76e0b87aa7e9b84d1df, d_cc3e90160f490686039986 (the three owners' roots)", "f_ + 22 hex, folders d_; same id across Drive and the native row; identical sharing"),
    ("gcal.gcal_events", "event_id!, calendar_id!", f"gcal data.json evt_f0684c020204a8d22f7dc3 (Calvin's copy of Engineering Focused Weekly Planning)", "one row per attendee calendar, attendees sorted by email, self:true on the owner's copy, shared ical_uid"),
    ("linear.linear_issues / linear_comments", "id!, title!, priority!, labels_json!, links_json!, relations_json!, state_history_json!, is_archived!, created_at!, updated_at!; id!, issue_id!, author_id!, body!, is_edited!, created_at!, updated_at!", "linear data.json ZOM-556, ZOM-560, ZOM-566 (Vincent's and Brian's latest tickets)", "state_id holds the state name (Todo, In Validation); keys rise with filing time, ZOM-566 is the last base key (2025-09-30T16:26:02Z); the base has no comments"),
    ("trello.trello_cards / trello_actions / trello_boards (UPDATE)", "id!, name!, idBoard!, idList!; id, type, date, idMemberCreator, idBoard, idCard, data_json", "trello data.json cards 68c45c2bba569a224e81425d and 6851ab4165575ba2c16a6f05 (Backlog list), actions 68dc0eb3b933d6e0e75dad34, 68c45d98cdb68a952ccaa070", "an id's first 8 hex = its Unix seconds; one updateCard per changed field with the old value under old; idShort 80 is the board's next number (79 is its highest)"),
    ("github.github_reviews / github_review_comments / github_pr_comments / github_timeline_events", "id!, pr_id!, seq!; id!, pr_id!, seq!; id!, pr_id!; id!, pr_id!, event!", f"github data.json {PR(472)}#rev_1, {PR(465)}#rc_1, {PR(473)}#c_1, {PR(473)}#ev_4", "next ids rev_2, rc_1, c_2, ev_5; line, position and commit_id null as on every base review comment"),
]:
    A("| " + " | ".join(row) + " |")
A("")
# ---------------------------------------------------------------- 1.B
A("## 1.B Entity")
A("")
A("| Entity | Spelling used | Where it appears (cited) | Agreement |")
A("|---|---|---|---|")
for row in [
    ("Calvin Price", CAL, f"slack EMPLOYEE_0006_SLACK_ID in {BDM}/1759173608.518609; GitHub PERSON_0003_GITHUB_USERNAME, author of {PR(465)}, {PR(472)}, {PR(475)} (shown as calvin.price in {PRS}/1759185399.395419); Linear usr_49b9dfa5208d400d, assignee of ZOM-543; Drive root d_49b9dfa5208d400d9b3937", "AGREE"),
    ("Brian Foster", "brian.foster@harmonygames.co", f"slack EMPLOYEE_0026_SLACK_ID in {BDM}/1758808795.588519; Linear usr_fc22d5941b2aeb5c, creator of ZOM-543 and ZOM-566", "AGREE"),
    ("Vincent Parker", "vincent.parker@harmonygames.co", f"slack EMPLOYEE_0012_SLACK_ID in {VDM}/1758820544.160399; Linear usr_65c76e0b87aa7e9b, creator of ZOM-556 and ZOM-560; Drive root d_65c76e0b87aa7e9b84d1df", "AGREE"),
    ("Arthur Blake", "arthur.blake@harmonygames.co", f"GitHub EMPLOYEE_0025_GITHUB_USERNAME, {PR(472)}#rev_1 and {PR(475)}#rev_1 (shown as arthur.blake in {PRS}/1759247580.373799); slack EMPLOYEE_0025_SLACK_ID in {ZM3D}/1759189361.525409; Drive root d_cc3e90160f490686039986", "AGREE"),
    ("Leonard Hayes", "leonard.hayes@harmonygames.co", f"Trello PERSON_6094_TRELLO_USER_ID, actions 68dc0eb3b933d6e0e75dad34 and 68c451221ebabaf255a7d17f on ZM ROADMAP; slack EMPLOYEE_0038_SLACK_ID in {ZM3D}/1759182908.627389; sender 'leonard hayes' of base invitations", "AGREE"),
    ("Oliver Brooks", "oliver.brooks@harmonygames.co", f"GitHub EMPLOYEE_0003_GITHUB_USERNAME, author and merger of {PR(473)} (shown as oliver.brooks in {PRS}/1759246868.802449); slack EMPLOYEE_0003_SLACK_ID in {BUGS}/1759254098.279269; Linear usr_bdf01b53c6a92c5e", "AGREE"),
    ("Marcus Bennett", "marcus.bennett@harmonygames.co", f"slack EMPLOYEE_0002_SLACK_ID in {MDM}/1759156446.484629; the artist, one of three Marcuses in the roster, used only by Slack id", "AGREE"),
    ("Robert", "robert@harmonygames.co", f"slack EMPLOYEE_0016_SLACK_ID in {ZM3D}/1759187344.387499", "AGREE"),
    ("Owen Baker, Samuel Turner, Julia Lawson", "roster addresses", "Linear usr_4e13bd40cc73d0fc (assignee of ZOM-566), usr_caafeec2804b3a67 (assignee of ZOM-560); julia.lawson@harmonygames.co on base invitations (gmail threads/calvin@harmonygames.co_1842050583560498707.json)", "AGREE"),
    ("Collect & Win / Win&Collect / collect&win", f"Collect & Win in the sheet, the card and Brian's note; the PR title says Win&Collect ({PR(472)}), Brian's chat says collect&win ({BDM}/1758730948.999939)", f"{PR(472)}, {BDM}/1758730948.999939, Trello card 6851a7abf7876721472dba99 (Win and Collect)", "AGREE (one feature, base naming varies)"),
    ("Queue Manager", "ZOM-543 'Queue Manager'; Calvin's folder and deck 'ZM queue manager'", f"ZOM-543, {PR(465)}, Trello card 68c453cd0ff184d95550bc58", "AGREE"),
    ("Builds", "job name and number as in #builds: 'iOS Internal #1718', 'Android #1984', 'Android Submission #135'", f"{BUILDS}/1758817549.151639, {BUILDS}/1758838918.332289, {BUILDS}/1759263189.219529; Calvin's own form 'Match 3D iOS Internal - #1718' in {VDM}/1758817744.353289", "AGREE"),
    ("ZOM vs ENG keys", "only ZOM keys are seeded", "ENG-2069 (a Domino Delights queue ticket) is a decoy only", "AGREE"),
]:
    A("| " + " | ".join(row) + " |")
A("")
A("No roster person is renamed or re-titled. Thomas, Thomas Baker and Oscar Bennett do not appear; Frederick Stone's GitHub login is not used.")
A("")
# ---------------------------------------------------------------- 1.C
A("## 1.C Voice and realism")
A("")
A("Seeded speakers, each with its activity.json (synth-cut KB) status at the clock:")
for who, mail, what in [
    ("Brian Foster", "brian.foster@harmonygames.co", "the DM, the earlier line about the review, the note on ZOM-543, one ticket comment"),
    ("Vincent Parker", "vincent.parker@harmonygames.co", "the pass sheet and legend, 18 tickets and their first notes, the two ties, two DM lines, the thread reply"),
    ("Arthur Blake", "arthur.blake@harmonygames.co", "two inline review comments, the two build notes"),
    ("Leonard Hayes", "leonard.hayes@harmonygames.co", "the review card and its actions, the calendar event and its mails"),
    ("Oliver Brooks", "oliver.brooks@harmonygames.co", "the line on his own PR, two ticket replies"),
    ("Marcus Bennett", "marcus.bennett@harmonygames.co", "two DM lines"),
    ("Robert", "robert@harmonygames.co", "one channel post"),
    ("Owen Baker", "owen.baker@harmonygames.co", "two ticket replies"),
    ("Samuel Turner", "samuel.turner@harmonygames.co", "one ticket reply"),
    ("Calvin Price", CAL, "owner of the seeded folder and deck; no seeded message"),
]:
    A(f"- {who} ({mail}) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: {what}.")
A("- SLACK_BOT_0004_SLACK_ID — the GitHub Slack app (integrations.json INT-01), not a person; seeds: three comment copies in #zombie-prs.")
A("- SVC_0248_EMAIL — GitHub's notification sender (integrations.json INT-12), not a person; seeds: two mails in the base PR threads.")
A("")
A("Lengths and hours from conventions.json (synth-cut KB): slack.length_chars_by_channel_type and slack.per_person_hours_and_style. Core UTC windows: Brian 12–21, Vincent 10–19, Marcus 10–20, Robert 14–03, Arthur 15–01, Leonard 15–02, Oliver 14–01, Owen 15–00, Samuel 15–00. Every seeded record sits inside its author's window except Vincent's sheet save at 19:30Z, his line to Calvin at 19:33Z and his thread reply at 21:20Z; the base has him posting at 21:36Z on Sep 24 (the report behind sheet rows 1 and 2). linear.title_prefixes_by_team: ZOM titles carry no prefix, and Vincent's base titles are plain sentences (ZOM-556, ZOM-560). github.pr_title_patterns is not used: no PR is seeded. gcal.duration_min: 30 minutes, the base's most common length. gmail.internal_subject_len_chars is not used: the only seeded mails are system mails whose subjects follow integrations.json INT-11 and INT-12.")
A("")
A("Real messages used as voice references:")
for who, qs in [
    ("Brian Foster", [("We talked with [PERSON_NAME_0050], the input blocker is not a problem right now. Probably we need to check that after adding collect&amp;win to queuemanager", f"{BDM}/1758808795.588519"), ("When  users kills the app, they see coin animation again", f"{BDM}/1758808900.412489"), ("Hello! I don't have any time to test today. But I'll test it tomorrow", f"{BDM}/1759173857.856219")]),
    ("Vincent Parker", [("Looks ok to me", f"{VDM}/1758820544.160399"), ("Boss arena as well", f"{VDM}/1758820551.265839"), ("i think we should squeeze in the fix for that issue if it's an easy fix. annoying and players can see that for 10 times in a day if they make it that far.", f"{BUGS}/1757939514.864549")]),
    ("Marcus Bennett", [("ok so i pushed a modifications on the prefab on my branch, Marcus/EndlessMode_Vfx", f"{MDM}/1759156446.484629"), ("cuz i'm done with the bar itself", f"{MDM}/1759161289.715329"), ("hopefully we are not gona have any conflicts right?", f"{MDM}/1759161340.563009")]),
    ("Robert", [("Android", f"{ZM3D}/1759248076.284779"), ("I didn't look at it by pubs.", f"{ZM3D}/1759248130.580729")]),
    ("Arthur Blake", [("we haven't merged it yet. I'll let you know", f"{ZM3D}/1759189361.525409"), ("Seems important", f"{PR(390)}#rc_6"), ("This is intentional as I want it to simulate more when timescale is high.", f"{PR(395)}#rc_4")]),
    ("Oliver Brooks", [("will work on this asap", f"{BUGS}/1759254098.279269"), ("well, we'll see what happens after we move 2 or 3 features to Addressables", f"{BUGS}/1758919518.529979"), ("I can have a look and let you know", f"{ZM3D}/1758235859.966389")]),
    ("Leonard Hayes", [("I just released 0.3.49 on IOS", f"{ZM3D}/1759182908.627389")]),
    ("Samuel Turner", [("I added it to main. Please update your branch, and if it's not showing, restart Unity", f"{ZM3D}/1756928762.675329")]),
    ("Owen Baker", [("I created a doc for the endpoints I'm going to need for CollectAndWin event, please give it a look when you have a chance:", f"{ZM3D}/1756161484.791409")]),
]:
    A(f"- {who}: " + " · ".join(f'"{q}" ({p})' for q, p in qs))
A("")
A("Brian opens with a separate 'Hello!' line and writes plain full sentences; Marcus writes lower-case bursts; Vincent writes short status lines; Arthur's review comments are one or two short sentences. Vincent files tickets in bursts in the base (six between 14:44Z and 15:21Z on Sep 22, ZOM-556 to ZOM-561), so 18 tickets in two hours on Sep 30 follow his habit. No em dashes are used.")
A("")
# ---------------------------------------------------------------- 1.D
A("## 1.D Keyword")
A("")
A("| Term | Hits / pointer | Note |")
A("|---|---|---|")
for row in [
    ("\"Queue Manager\"", f"ZOM-543; {PR(465)}; Trello card 68c453cd0ff184d95550bc58", "the ticket the note sits on; ENG-2069 is the Domino Delights namesake (decoy)"),
    ("\"flow review\"", f"NEW TERM — introduced in {SL['gate_old']}, {ID['rev_card']}, {ID['invite_v1']}, {ID['event']}", "reached from Brian's DM ('Thursday's flow review', 'the review invite') and his note ('the agenda of Thursday's review')"),
    ("\"flow pass\"", f"NEW TERM — introduced in {ID['sheet']}", "reached from Brian's DM; a Drive or Sheets search on the words returns the sheet"),
    ("\"QA passes\"", f"NEW TERM — introduced in {ID['rule_doc']} and {ID['dd_doc']}", "reached from Brian's note; a Docs search returns both, the decoy differs on the game"),
    ("\"1718\"", f"{BUILDS}/1758817549.151639, {VDM}/1758817744.353289", "the build Calvin names in the chat; its #builds post gives the branch"),
    ("\"Submission 135\" / \"#135\"", f"{BUILDS}/1759263189.219529; seeded {SL['reopen']} and {SL['back']}", "the newer main build both later reports name"),
    ("\"pass icon\"", f"{VDM}/1758721951.996909 (Vincent, Sep 24, about the icon's VFX: decoy); seeded {SL['filt_dm']}, ZOM-571, {ID['inline']}", "three different things share the words; the sheet row is the restart, Marcus's report is the glow"),
    ("\"daily gift\"", "ZOM-556, ZOM-432", "ZOM-432 is the artwork frame (decoy); Vincent's tie is on ZOM-556"),
    ("\"freezer\"", "ZOM-560", "the abandoned pack ticket; Vincent's tie is on it"),
    ("\"Addressables\"", f"{PR(473)}; {BUGS}/1758919518.529979", "Oliver's merged PR; his seeded line is its second conversation comment"),
    ("\"stock-take\"", f"NEW TERM — introduced in {SL['hub']}", "Brian's word for the deliverable"),
]:
    A("| " + " | ".join(row) + " |")
A("")
# ---------------------------------------------------------------- 1.E
A("## 1.E Persona reach")
A("")
A("Load-bearing scoped ids written to `Working_Files/plan/load_bearing_scoped.txt`; output verbatim. Linear, Trello and GitHub are unscoped, so their ids are not in that list (Evals/references/persona/acl.md).")
A("")
fence(rd("checksql.txt"))
A("")
A(f"- {BDM} — Calvin's DM with Brian (im member) LB; seeded {SL['hub']} ({ID['hub']}) and {SL['gate_old']} ({ID['gate_old']}).")
A(f"- {MDM} — Calvin's DM with Marcus LB; seeded {SL['filt_dm']} ({ID['filt_dm']}).")
A(f"- {VDM} — Calvin's DM with Vincent LB; base {VDM}/1758817744.353289 and {VDM}/1758820544.160399.")
A(f"- {BUGS} — #zombie-bugs, Calvin a member LB; seeded reply {SL['reopen']} under {BUGS}/1757939514.864549.")
A(f"- {ZM3D} — #zombie-match3d, Calvin a member LB; seeded {SL['older']}, Robert's sighting on the older build Android #2006. The reply {SL['back']} sits under {BUGS}/1757467270.178829 in #zombie-bugs.")
A(f"- {BUILDS} — #builds, Calvin a member LB; base posts {BUILDS}/1758817549.151639 and {BUILDS}/1759263189.219529.")
A(f"- Calvin's mailbox LB: {ID['invite_v1']}, {ID['invite_v2']}.")
A(f"- Drive LB: {ID['sheet']}, {ID['legend']}, {ID['rule_doc']} and {ID['dd_doc']} are shared with Calvin; {ID['folder']} and {ID['deck']} are his own.")
A(f"- Calendar LB: {ID['event']} is Calvin's own copy (self:true).")
A(f"- Unscoped: ZOM-543 with Brian's note, ZOM-556, ZOM-560, ZOM-567 to ZOM-584, {PR(465)}, {PR(472)}, {PR(473)}, {PR(475)}, {ID['inline']}, {ID['inline2']}, {ID['else_pr']}, Trello card {ID['rev_card']}.")
A(f"- No designed denial for {ID['event']}: denied_probes is empty. The invitation copies in four other mailboxes and the five other calendar copies are companions, never evidence; the event and both mails are cited by Calvin's own copies.")
A("")
# ---------------------------------------------------------------- 1.F
A("## 1.F Collision")
A("")
A("base_check Check A compares every minted id against the full base collections (output in the Self-review, PASS). Scheme by service:")
A("- linear: ZOM-567 to ZOM-584: base ZOM ends at ZOM-566 (2025-09-30T16:26:02Z); 27 comment ids are comment_ + 32 hex and the base has 0 comments.")
A(f"- slack: {len(SL)} seeded (channel, ts) pairs: no base message in those channels at those ts (messages/{BDM}/2025-09.json, messages/{VDM}/2025-09.json, messages/{MDM}/2025-09.json, messages/{BUGS}/2025-09.json, messages/{ZM3D}/2025-09.json, messages/{PRS}/2025-09.json).")
A(f"- gmail: thread ids and calendar Message-IDs minted per seeded time and mailbox; the two GitHub review numbers 3285698310 and 3285755391 sit just under the base approvals' 3285702920 and 3285759222 in the same threads.")
A(f"- trello: card {ID['rev_card']} and actions {TR['create']}, {TR['desc1']}, {TR['name2']}, {TR['update']}: first 8 hex are each record's own seconds; idShort 80 is unused on board 6851a6569f3bf818760632ab.")
A(f"- drive/calendar: {ID['sheet']}, {ID['legend']}, {ID['rule_doc']}, {ID['dd_doc']}, {ID['deck']}, {ID['folder']}, {ID['event']}: sha-derived, 0 base hits (lookup run at the scenario stage, `plan/out/id_collisions.txt`, and Check A here).")
A(f"- github: {ID['inline']}, {ID['inline2']}, {GH['inline']['review']}, {GH['inline2']['review']}, {ID['else_pr']}, {PR(473)}#ev_5: base ids end at rev_1, no rc, c_1 and ev_4 on those PRs.")
A("- Header tokens: none minted; PERSON_6094_TRELLO_USER_ID, PERSON_6092_TRELLO_USERNAME, SLACK_BOT_0004_SLACK_ID, SVC_0248, SVC_3649, SVC_0613, SVC_5111 (with the alias each base approval mail carries) and SVC_0842 are the base tokens those records use. Body tokens: [PERSON_NAME_0043] is Julia's own token as base invitations in her mailbox end; [PERSON_NAME_0029] and [SOURCE_ORG_0001] are copied inside base PR titles and mail subjects.")
A("")
# ---------------------------------------------------------------- ledger
A("## Record ledger")
A("")
A("One row per SQL statement, in SQL order.")
A("")
A("| # | SQL line | Table | Id | Manifest element | Carrier | Reach | Discovery role |")
A("|---|---|---|---|---|---|---|---|")
CARRIER = {"gcal.gcal_events": "● (summary, attendees, time; description ○)", "linear.linear_comments": "● (§6b)"}
for n, x in enumerate(STM, 1):
    rid = rid_of(x)
    el = element(x, rid)
    A(f"| {n} | L{x['line']} | {x['table']}{' (UPDATE)' if x['op'] == 'update' else ''} | {rid}{' on ' + COMMENT_OF[rid] if rid in COMMENT_OF else ''} | {el} | {CARRIER.get(x['table'], '●')} | {reach(x)} | {role(rid, el)} |")
A("")
# ---------------------------------------------------------------- findability
A("## Findability and discovery-order proofs")
A("")
A(f"- Hub AN1 {SL['hub']} ({ID['hub']}): the newest message from Brian in Calvin's DM with him; first link. AN2 ZOM-543: found by its title; Brian's note is its only comment.")
A(f"- Authority H1 {ID['rule_doc']}: the note says 'Arthur's rule for QA passes'; a Docs or Drive search for 'QA passes' returns it and the decoy {ID['dd_doc']}, which differs on the game (Domino Delights hotfixes).")
A(f"- Authority H2 {ID['rev_card']}: the note says 'the agenda of Thursday's review'; a Trello search for 'flow review' returns it; decoys met first are Brian's own line {SL['gate_old']} in the anchor chat and the first invitation {ID['invite_v1']}.")
for t, s in [
    ("T_BRANCH", f"claim met first: 'ok, chat' on sheet rows 1, 2 and 25 with {VDM}/1758820544.160399; overturned by the branch on {BUILDS}/1758817549.151639 read against {ID['rule_doc']}; decisive because the legend sends the reader to the chat and the chat names the build"),
    ("T_INLINE", f"claim met first: Fix #472 on row 12, {PR(472)} merged, ZOM-571 In Validation; overturned by {ID['inline']}, also in Calvin's mailbox ({GH['inline']['mail']}) and in #zombie-prs ({SL['mirror_inline']})"),
    ("T_INLINE_PACK", f"claim met first: Fix #475 on row 32, {PR(475)} merged, ZOM-581 In Validation; overturned by {ID['inline2']}, also {GH['inline2']['mail']} and {SL['mirror_inline2']}"),
    ("T_REOPEN", f"claim met first: nr on a main build on row 9; overturned by {SL['reopen']} (Sep 30 21:20Z) under {BUGS}/1757939514.864549; found by Vincent's recent posts or the words 'Submission 135'"),
    ("T_BACK", f"claim met first: ok on a main build on row 29; overturned by {SL['back']} (Sep 30 21:44Z); found by the channel's recent history or 'endless'"),
    ("T_ELSE", f"claim met first: blank Fix cells on rows 13 and 38 and ZOM-572 in Todo; overturned by {ID['else_pr']} on {PR(473)}, also {SL['mirror_else']}"),
    ("T_FILT", f"the note's sentence about a bug told in a DM since the 26th; {SL['filt_dm']} is the only such report in Calvin's DMs from Sep 26 to 30"),
    ("T_ALIAS_GIFT / T_ALIAS_STREAK", f"claim met first: blank Ticket cells on rows 11 and 20; overturned by {ID['alias_gift']} on ZOM-556 and {ID['alias_streak']} on ZOM-560"),
    ("T_GATE", f"claim met first: {ID['invite_v1']} (Sep 29 16:05Z) and {SL['gate_old']} (Sep 29 16:41Z); overturned by {ID['rev_card_update']} (Sep 30 17:22Z) on card {ID['rev_card']}"),
]:
    A(f"- {t}: {s}.")
A("")
# ---------------------------------------------------------------- self-validation
A("## Self-validation")
A("")
A("| QC category | Tool-enforced (result) | Manual (evidence) |")
A("|---|---|---|")
A(f"| Missing Universe Data | check-sql PASS (1.E) | every deciding fact persona-readable: {ID['rule_doc']}, {BUILDS}/1758817549.151639, {ID['inline']}, {ID['inline2']}, {SL['reopen']}, {SL['back']}, {ID['else_pr']}, {SL['filt_dm']}, {ID['alias_gift']}, {ID['alias_streak']}, {ID['rev_card']} |")
A(f"| Temporal Field | sql_lint 0 errors; base_check Check C PASS | the sheet's last change (19:30Z) is after every build it cites ({BUILDS}/1759257787.502039 finished 18:43Z); both later reports follow {BUILDS}/1759263189.219529 (20:13Z); Arthur's comments follow his approvals {PR(472)}#rev_1 and {PR(475)}#rev_1; ZOM-567 to ZOM-584 follow ZOM-566 |")
A(f"| Cross-service Referential | base_check Check A PASS | the event's time and guests agree across six calendar rows and ten mails; each GitHub comment has its #zombie-prs copy, and Arthur's two also their mail in the base thread |")
A(f"| Quantitative | reply counters updated on five base parents | {BUGS}/1757939514.864549 goes from 11 replies to 12 and {BUGS}/1757467270.178829 from 4 to 5, repliers unchanged; the #zombie-prs parents gain one reply each; the sheet has 38 numbered rows |")
A("| State / Lifecycle | no seeded ticket is Done; In Validation tickets carry started_at | ZOM-571, ZOM-576 and ZOM-581 are In Validation because Vincent was told a merged PR had them; the card sits on an open list |")
A("| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A, 1.F) |")
A(f"| Semantic / Category | — | titles match content: {ID['sheet']}, {ID['legend']}, {ID['rule_doc']}, {ID['dd_doc']}, {ID['deck']}; the review card is a planning card on the roadmap board's Backlog list, next to other undated items |")
A("| Other | — | voice per 1.C; no record states a status, a count or the answer |")
A("")
# ---------------------------------------------------------------- integrations
A("## Integrations and companions")
A("")
A("| Service | INT id | Companion | Decision |")
A("|---|---|---|---|")
A(f"| github | INT-01 | Slack copy of each comment in #zombie-prs | seeded: {SL['mirror_inline']}, {SL['mirror_inline2']}, {SL['mirror_else']}, each a reply under its PR's opened message with the parent's counters updated; all three fall inside the match3d window, which ends 2025-09-30T22:33Z |")
A(f"| github | INT-12 | GitHub mail to the PR author | seeded for Arthur's two comments in the base threads: {GH['inline']['mail']}, {GH['inline2']['mail']}; none for {ID['else_pr']}, since Calvin's mailbox holds no thread for {PR(473)} |")
A("| github | INT-02, INT-23 | push notices, CodeRabbit | none: no commit and no bot comment is seeded |")
A("| linear | INT-03, INT-04, INT-05 | PR comment, Slack posts, mail digests | none: no PR names a seeded key; the base has no Slack post for ZOM-556 to ZOM-566 beyond links people paste; digests are aggregate |")
A(f"| gcal | INT-11 | invitation and update mails | seeded for {ID['event']}: {ID['invite_v1']} and {ID['invite_v2']} in Calvin's mailbox, and copies for Vincent, Brian, Julia and Arthur; none in the organizer's own mailbox |")
A(f"| gdrive | INT-13 | Drive share DMs and mails | none: Calvin's mailbox holds nine share notices in all and none after March 2025, so shares of {ID['sheet']} and {ID['rule_doc']} without a notice follow the base |")
A(f"| slack | INT-22 | Slack mail digests | none ({ID['hub']}) |")
A(f"| trello | INT-21 | none exists | none ({ID['rev_card']}) |")
A("| jenkins | INT-06 | #builds posts | none seeded: every build cited is a base post |")
A("| gdocs, gsheets, gslides | not integration sources | — | none |")
A("")
# ---------------------------------------------------------------- census
A("## Touched-data census and coherence hazards")
A("")
A(f"Touched data: {SL['hub']}, ZOM-543, {ID['sheet']} and its legend, tickets ZOM-556, ZOM-560, ZOM-567 to ZOM-584, decoys ZOM-432 and ENG-2069; {PR(465)}, {PR(472)}, {PR(473)}, {PR(475)} with their bodies, reviews, comments and timelines; #builds posts for the 16 builds the sheet and the chats name ({BUILDS}/1758817549.151639, {BUILDS}/1758737279.948339, {BUILDS}/1759173858.825639, {BUILDS}/1759263189.219529 and the twelve main builds in `solver/solver.py`); Calvin's DMs with Brian, Vincent, Marcus and Julia from Sep 23 to 30 ({BDM}/1758808795.588519, {VDM}/1758817744.353289, {MDM}/1759161394.516899, D05HYDTG5TJ/1756838837.147599); #zombie-bugs thread {BUGS}/1757939514.864549 and the tutorial skip thread {BUGS}/1758903616.346579; #zombie-match3d from Sep 29; the #zombie-prs threads {PRS}/1759185399.395419, {PRS}/1759246868.802449 and {PRS}/1759247948.371729; Calvin's GitHub mail threads for {PR(472)} and {PR(475)}; ZM ROADMAP's Backlog list 68c451221ebabaf255a7d16b and cards 68c453cd0ff184d95550bc58 and 6851a7abf7876721472dba99; Vincent's Bug Checklist canvas CF4EDAF93359/1759236624.010909 and the Collect & Win canvas C3DD99314033/1758897445.985019, which Brian's note leaves as they are.")
A("")
A("Hazards from coherence_hazards.json:")
A("- temporal: T01 — the two seeded reviews add no 'reviewed' timeline event, as base reviews' events carry no time or actor to copy; T06 — the card's dateLastActivity equals its last action, and the board's is moved to it; T02 not touched: no thread file is read for order.")
A("- semantic: S01 — no seeded record cites an ENG key for ZOM work; S02 — the epic's children stay in the ZOM team.")
A(f"- referential: R07 — every seeded GitHub comment has its #zombie-prs copy; R08 — both invitation mails have their calendar rows; R03 — the two GitHub mails keep the base threads' redacted subjects; R04 — no seeded text links a Google file.")
A(f"- quantitative: Q01, Q02, Q03 — the five base parents' reply_count, reply_users_count and latest_reply are updated with the seeded replies ({BUGS}/1757939514.864549, {BUGS}/1757467270.178829, {PRS}/1759185399.395419, {PRS}/1759246868.802449, {PRS}/1759247948.371729); Q11 — the six calendar copies agree field for field.")
A(f"- state/lifecycle: L09, L10 — {PR(473)} merged with no review and {PR(465)} with bot reviews only, which is base truth and not relied on beyond their merged state; L03 — statuses rest on Brian's rule, never on a ticket state as proof of shipping; L06 — ZOM-543 stays In Progress and no parent is Done over an open child; L08 — every seeded assignee is active at the clock.")
A("- identifier/format: I08 — the #zombie-prs copies show real logins (arthur.blake, oliver.brooks) while GitHub rows keep the tokens, as in the base; I09 — the copies keep the unredacted org as the base copies of these three PRs do; I16 — Trello ids encode their own time; I10 — no seeded Linear author uses an irregular user id.")
A("")
A("Known data issues (references/known_data_issues/synthcut.md; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):")
for c, why in [("SC-6", "no mail from Brian is seeded or read; his copy of the invitation is a companion sent by Leonard"),
               ("SC-7", "channel membership is used only for reach, never graded"),
               ("SC-13", "the BETA list and its name are not touched; the card is on Backlog and the review's date comes from the card and the invitation"),
               ("SC-14", "no card's complete flag is read; the Queue Manager card's tick is a decoy the statuses never use"),
               ("SC-15", "ZOM-521, ZOM-526 and ZOM-528 are not reports and not touched"),
               ("SC-16", "ZOM-564, ZOM-513, ZOM-514 and ZOM-563 are not reports; no ticket state is proof of shipping, and the three state changes follow the status worked out from the records"),
               ("SC-18", "PR #477 is not cited"),
               ("SC-19", "no telemetry version is matched to a build; branches come from #builds posts"),
               ("SC-22", "time_in_status_minutes is NULL on every seeded ticket and never read"),
               ("SC-38", "no Season Pass ship date is used; the Season Pass rows rest on re-tests and PRs"),
               ("SC-56", "no commit title is quoted; builds are matched by job and number"),
               ("SC-57", "no post in #zm-collect-win is seeded or required"),
               ("SC-67", "build #1621 is not cited"),
               ("SC-68", "Boss Arena rows rest on re-tests, not on when the mode reached production"),
               ("SC-70", "time zones come from the calendar and base invitation subjects, never from Slack")]:
    A(f"- {c}: {why}.")
A("")
# ---------------------------------------------------------------- disagreements
A("## Intended disagreements")
A("")
A("| Claim met first | Overturning record | Why realistic | Resolution |")
A("|---|---|---|---|")
for a, b, c, d in [
    (f"'ok, chat' on rows 1, 2 and 25 of {ID['sheet']} and Vincent's ok in {VDM}/1758820544.160399", f"the #builds post {BUILDS}/1758817549.151639 (a feature-branch build) read against {ID['rule_doc']}", "a tester says ok on the build the dev handed him", "Brian's note: a pass counts only on a build Arthur's rule counts"),
    (f"Fix #472 on row 12 and ZOM-571 In Validation", f"Arthur's review comment {ID['inline']}", "a tester writes down the PR he was told and the reviewer sees the diff", "the note asks whether a fix is in main; the reviewer says it is not in that PR"),
    (f"Fix #475 on row 32 and ZOM-581 In Validation", f"Arthur's review comment {ID['inline2']}", "same", "same"),
    (f"nr on row 9 of {ID['sheet']}", f"Vincent's reply {SL['reopen']}", "a tester mentions a relapse where he happens to be writing", "Arthur's note: a pass stands until somebody sees the bug again on a main build made after the one it passed on"),
    (f"ok on row 29 of {ID['sheet']}", f"Robert's post {SL['back']}", "a founder reports what he saw while playing the submission build", "same sentence"),
    ("blank Fix on rows 13 and 38, ZOM-572 Todo", f"Oliver's line {ID['else_pr']} on {PR(473)}", "a dev notes on his own PR what else it carries, and QA's list does not know", "the note asks whether a fix is in main; the dev says on his own merged PR that it is"),
    (f"Brian's line {SL['gate_old']} and the first invitation {ID['invite_v1']}: Collect & Win and Daily Gift, Friday", f"the changed card {ID['rev_card']} ({ID['rev_card_update']}) and {ID['invite_v2']}", "a review is moved and its agenda changed by its organizer", "the note names Leonard's review card"),
    (f"{ID['dd_doc']}: a pass on the dev's branch build is enough", f"{ID['rule_doc']}: for ZM only main builds count", "two notes by the same lead for two games", "the game: the task is ZM"),
]:
    A(f"| {a} | {b} | {c} | {d} |")
A("")
# ---------------------------------------------------------------- constraints
A("## Constraints for the prompt brief")
A("")
A("| Anchor | May be named (noun phrases only) | Record |")
A("|---|---|---|")
A(f"| AN1 | Brian's message from yesterday; Brian's DM | {SL['hub']} |")
A("| AN2 | the Queue Manager ticket; ZOM-543 | ZOM-543 |")
A("")
A("Never name in the prompt: Brian's note or any of its sentences, the pass sheet's legend, Arthur's doc, Leonard's card or Trello, the invitation mails, #builds or any build number, any PR number or review comment, Vincent's thread reply, Robert's post, Oliver's comment, Marcus or his report, ZOM-556 or ZOM-560, any status, count or area. Deliverable kinds: Linear child issues, sub-issues, moves, notes and state changes; one Google Sheet in Calvin's folder, shared; one slide in Calvin's deck; one Slack reply in Brian's DM. No deadline is graded; the review is on Thu Oct 2.")
A("")
# ---------------------------------------------------------------- fact sheet
A("## Fact sheet")
A("")
A("| Key | Value | Kind | Home / must appear in |")
A("|---|---|---|---|")
for f in MAN["facts"]:
    A(f"| {f['key']} | {f['value']} | {f['kind']} | {', '.join((f.get('home_ids') or []) + (f.get('must_appear_in') or []))} |")
A("")
fence(rd("fact_check.txt"))
A("")
A("Warning disposition: the value_drift warning compares the event's start (Thu Oct 2) with the first invitation's Fri Oct 3. That difference is the designed move of the review, recorded by the updated invitation and the changed card; every mailbox copy of each mail carries the same date.")
A("")
A(f"Solver totals (`solver/truth.json`): {TOT['reports']} reports ({len(state['sheet'])} sheet rows and 1 raised outside it): Passed {TOT['passed']}, Waiting on QA {TOT['waiting_on_qa']}, Waiting on a fix {TOT['waiting_on_a_fix']}; {TOT['clear_areas']} clear area of {len(AG['areas'])}; {TOT['review_list']} on the review list; {TOT['existing_tickets']} held by an existing ticket and {TOT['new_sub_issues']} new sub-issues; {TOT['state_changes']} existing tickets change state.")
A("")
A("| Area | Reports | Open | Status |")
A("|---|---|---|---|")
for a_, v in AG["areas"].items():
    A(f"| {a_} | {v['reports']} | {v['open']} | {v['status']} |")
A("")
A("| Report | Area | Status | Ticket | Review list | Ticket state (as found → to set) |")
A("|---|---|---|---|---|---|")
for k, v in ROWS.items():
    if v["Status"]:
        A(f"| {k} | {v['Area']} | {v['Status']} | {v['Ticket'] or 'new sub-issue'} | {v['Review list']} | {(v['Ticket state as found'] or '—')} → {v['Ticket state']} |")
A("")
# ---------------------------------------------------------------- facts for the human
A("## Facts for the human")
A("")
A("| Locator | Base/seeded | Fact | Reach | Role |")
A("|---|---|---|---|---|")
FH = [
    (SL["hub"], "seeded", f"Brian to Calvin, {AT['hub']} ({ID['hub']}): the ask, the sheet, the share, the slide and the five numbers to send back", "DM member", "anchor"),
    (ID["epic_note"] + " on ZOM-543", "seeded", f"Brian's note, {AT['epic_note']}: the ten areas, what counts as a report, the three statuses, the ticket rule, the state mapping, Clear and Open, the review list, the sheet's tabs and columns", "unscoped", "delegation"),
    (ID["sheet"], "seeded", f"Vincent's 'ZM home screen flow pass', 38 rows (#, Area, What happens, Found on, Ticket, Fix, Re-test), last changed {AT['sheet']}", "shared", "requirement, claims met first"),
    (ID["legend"], "seeded", f"Vincent's 'How to read my pass sheets', {AT['legend']}: ok, nr, again, 'ok, chat', and that Fix is the PR he was told", "shared", "format"),
    (ID["rule_doc"], "seeded", f"Arthur's 'ZM builds and QA passes', {AT['rule_doc']}: a QA pass only counts on a build of the main branch", "shared", "authority H1"),
    (ID["dd_doc"], "seeded", f"Arthur's 'DD hotfix builds and QA passes', {AT['dd_doc']}: a branch-build pass is enough for DD hotfixes", "shared", "decoy of H1"),
    (ID["rev_card"], "seeded", f"Leonard's card on ZM ROADMAP, Backlog list: 'ZM home screen flow review - Thu Oct 2', areas Collect & Win and Level-end rewards; changed {AT['rev_card_update']} (action {ID['rev_card_update']}); first version Fri Oct 3 with Collect & Win and Daily Gift", "unscoped", "authority H2"),
    (SL["gate_old"], "seeded", f"Brian to Calvin, {AT['gate_old']} ({ID['gate_old']}): Friday, collect&win and daily gift first", "DM member", "claim met first (T_GATE)"),
    (ID["invite_v1"], "seeded", f"Invitation from Leonard, {AT['invite_v1']}: Fri Oct 3, 12pm to 12:30pm CST; description names Collect & Win and Daily Gift", "own mailbox", "claim met first (T_GATE), decoy"),
    (ID["invite_v2"], "seeded", f"Updated invitation with note, {AT['invite_v2']}: Thu Oct 2, 12pm to 12:30pm CST; 'Moved up a day. Agenda is on the roadmap card, I changed it.'", "own mailbox", "evidence (T_GATE), recipient list"),
    (ID["event"], "seeded", "Calvin's copy of the event, Thu Oct 2 2025 18:00 to 18:30 UTC; attendees Leonard (organizer), Brian, Arthur, Julia, Vincent, Calvin", "own calendar", "recipient list (T_SHARE)"),
    (ID["inline"], "seeded", f"Arthur on {PR(472)}, {AT['inline']}: the season pass icon restart is not in this diff, only the Collect & Win wait", "unscoped", "overturning (T_INLINE)"),
    (ID["inline2"], "seeded", f"Arthur on {PR(475)}, {AT['inline2']}: the pack sound stop is nowhere in it", "unscoped", "overturning (T_INLINE_PACK)"),
    (ID["else_pr"], "seeded", f"Oliver on his own {PR(473)}, {AT['else_pr']}: it also has the fix for the pass start popup coming back and for the pass bar filling before the tokens land", "unscoped", "overturning (T_ELSE)"),
    (SL["mirror_inline"] + ", " + SL["mirror_inline2"] + ", " + SL["mirror_else"], "seeded", "the GitHub app's copies of those three comments in #zombie-prs, each under its PR's opened message", "channel member", "alternate path"),
    (SL["reopen"], "seeded", f"Vincent under {BUGS}/1757939514.864549, {AT['reopen']}: on Android Submission 135 the pass popup came up on top of the gift again", "channel member", "overturning (T_REOPEN)"),
    (SL["back"], "seeded", f"Robert under {BUGS}/1757467270.178829 in #zombie-bugs, {AT['back']}: on Android Submission 135 the home intro animation played again every time after Endless", "channel member", "overturning (T_BACK)"),
    (SL["filt_dm"], "seeded", f"Marcus to Calvin, {AT['filt_dm']}: on that day's main build the pass icon glow stays on after everything is claimed", "DM member", "report outside the sheet (T_FILT)"),
    (ID["alias_gift"] + " on ZOM-556", "seeded", f"Vincent, {AT['alias_gift']}: saw it again in his home screen pass on 1727, the day counter keeps going after a skipped day", "unscoped", "overturning (T_ALIAS_GIFT)"),
    (ID["alias_streak"] + " on ZOM-560", "seeded", f"Vincent, {AT['alias_streak']}: still there on Android 1984, the freezer from the abandoned pack never shows on home", "unscoped", "overturning (T_ALIAS_STREAK)"),
    ("ZOM-567 to ZOM-584", "seeded", "Vincent's 18 tickets of Sep 30 16:43Z to 18:44Z, one per sheet row with a key; ZOM-571, ZOM-576 and ZOM-581 In Validation, the rest Todo; each has his note and six have a reply", "unscoped", "evidence, write targets"),
    (ID["folder"], "seeded", "Calvin's folder 'ZM queue manager' in his Drive root", "owner", "write target"),
    (ID["deck"], "seeded", "Calvin's deck 'ZM queue manager', four slides, shared with Brian", "owner", "write target"),
    ("ZOM-543", "base", "Queue Manager, In Progress, assigned to Calvin, created by Brian 2025-09-15", "unscoped", "anchor, write target"),
    ("ZOM-556", "base", "'When the daily gift is skipped, it doesn't reset to 0.', Todo, Vincent, 2025-09-22", "unscoped", "evidence (T_ALIAS_GIFT)"),
    ("ZOM-560", "base", "'The abandoned pack win streak freezer reward is not granted.', Todo, Vincent, 2025-09-22", "unscoped", "evidence (T_ALIAS_STREAK)"),
    (f"{VDM}/1758817744.353289", "base", "Calvin to Vincent, Sep 25 16:29Z: 'Match 3D iOS Internal - #1718 already tested'", "DM member", "evidence (T_BRANCH)"),
    (f"{VDM}/1758820544.160399", "base", "Vincent, Sep 25 17:15Z: 'Looks ok to me', then 'Boss arena as well'", "DM member", "claim met first (T_BRANCH)"),
    (f"{BUILDS}/1758817549.151639", "base", "Match3D iOS Internal #1718, built from Calvin's QueueManager branch", "channel member", "overturning (T_BRANCH)"),
    (f"{BUILDS}/1759263189.219529", "base", "Match3D Android Submission #135, built from main, Sep 30 20:13Z", "channel member", "evidence (T_REOPEN, T_BACK)"),
    (PR(465), "base", "merged 2025-09-25T22:15:51Z; coin replay and queued tutorials", "unscoped", "evidence (rows 1, 2, 5, 25)"),
    (PR(472), "base", "merged 2025-09-30T15:53:04Z; the Collect & Win wait", "unscoped", "evidence (rows 12, 17, 18)"),
    (PR(473), "base", "Oliver's Addressables/sp, merged by him 2025-09-30T15:41:20Z", "unscoped", "evidence (rows 13, 38)"),
    (PR(475), "base", "merged 2025-09-30T16:09:15Z; card pack open and close flow", "unscoped", "evidence (rows 31, 32, 33)"),
    (f"{BDM}/1758808795.588519", "base", "Brian, Sep 25: the input blocker is not a problem right now", "DM member", "evidence (T_PARK)"),
    ("D05HYDTG5TJ/1756838837.147599", "base", "Julia's point about Calvin's tickets", "DM member", "evidence (T_FIELDS)"),
]
for r in FH:
    A("| " + " | ".join(r) + " |")
A("")
# ---------------------------------------------------------------- platform follow-ups
A("## Platform follow-ups")
A("")
A(f"- ○ carrier: the event's description ('Agenda is on the roadmap card.') is supporting only; the areas are on the card and the attendee list is in attendees_json. Nothing graded rests on a description.")
A(f"- Confirm in the pre-check that Slack tools return the attachment text of #builds posts (the branch of {BUILDS}/1758817549.151639) and of the #zombie-prs copies; Ask_Carriers says Slack tools return attachments.")
A("- Confirm that `linear_list_comments` returns the seeded notes and that no list call returns comments in bulk.")
A("- Confirm that `github_get_pull_request_comments` returns the two review comments and that the reviews list shows the COMMENTED review with an empty body.")
A("- Forecast blind spot: in exact mode the forecast never fails write-content slots, so its E[avg] overstates the pass rate; the design-mode view is reported beside it under Preflight.")
A("- Pre-check: confirm counted calls exceed 130 and that no run shows `model_refusal_fallback`.")
A("- No independent red team ran (REDTEAM_* unset; fallback recorded in the scenario design section 13); blind fork and coherence sweeps on this SQL are recorded below.")
A("")
# ---------------------------------------------------------------- self-review
A("## Self-review")
A("")
A("### Tool outputs (final SQL, verbatim)")
A("")
for f in ("sql_lint.txt", "base_check.txt", "base_claims.txt", "hardness_gate.txt"):
    fence(rd(f))
    A("")
A("hg.py lint: counts FAIL 0, CHECK 0, INFO 0; no CHECK line to disposition.")
A("")
A(f"sql_lint warning class 'on/after the clock' (12 lines, gcal.gcal_events start_ts and end_ts): the review is a meeting planned for Thu Oct 2 18:00Z, a not-yet-happened event; its created and updated stamps are Sep 29 and Sep 30, and nothing treats it as held.")
A("")
A("### Preflight (S4b–S5e)")
A("")
for f in ("oracle_kit.txt", "mutation.txt", "liveness.txt"):
    fence(rd(f))
    A("")
if os.path.exists(os.path.join(OUTD, "forecast_inj.txt")):
    fence(rd("forecast_inj.txt").replace("'rejected': []", "'rejected': none"))
    A("")
    A("Forecast, read with care (UNCALIBRATED): this exact view cannot fail write-content slots, which hold most of the weight, so its E[avg] is the optimistic end; the scenario-stage design view (`plan/out/forecast.txt`) and the requester-target model (`plan/policy_model_output.txt`) model the declared mechanisms over every slot. Only the pre-check can say which is closer.")
    A("")
A("Geometry: U passes the V3 cap and L_max clears the margin; the composed view counts direct slots only, while much of the weight is in write-content slots.")
A("")
A("### Changes made at this stage (and why)")
A("")
for d in MAN["design_delta"]:
    A(f"- {d['id']}: {d['change']}. {d['reason']}.")
A("- rev2 (after the platform /hardness FAIL 2 on rev1): Brian's note is cut back to plain definitions; the sentence that a later sighting ends a pass moved into Arthur's doc; Vincent's and Robert's come-backs are replies under their own older threads in #zombie-bugs; Robert's sighting on the older build Android #2006 is new; rows 18 and 34 carry a re-test before and after their fix merged. Design section 14 has the intake.")
for c in EXTRA.get("changes", []):
    A("- " + c)
A("")
A("### Blind sweeps on this SQL")
A("")
A("Two independent agents read only the SQL and the base through `tools/hg.py` (no design, manifest, solver or plan): a fork sweep that solved the task row by row (`plan/sweeps/fork_sweep_inj.md`) and a coherence sweep (`plan/sweeps/coherence_sweep_inj.md`). Dispositions:")
A("")
if EXTRA.get("sweep_rows"):
    A("| Finding | Source file | Disposition with evidence |")
    A("|---|---|---|")
    for row in EXTRA["sweep_rows"]:
        A("| " + " | ".join(row) + " |")
else:
    A("Pending at the time this dossier was assembled.")
A("")
A("### /injection Checks A–C walk")
A("")
A(f"- Inventory: {n_ins} INSERT, {n_upd} UPDATE, 0 DELETE, no upserts; tables {dict(by_table)}.")
A("- Check A (references and IDs): PASS: every channel, user, issue, PR, thread, calendar, board, list and folder resolves (base_check Check A); uniqueness over the full collections (1.F); ownership, membership and shares give Calvin reach (check-sql PASS).")
A("- Check B (structure): PASS: sql_lint 0 errors; every *_json column is literal JSON; NOT NULL columns supplied; generated *_fts columns never written; camelCase Trello columns and \"index\" quoted.")
A(f"- Check C (dates, parents, statuses, counts): PASS: every seeded timestamp is before 2025-10-01T00:00Z except the planned meeting's start and end; replies after their parents; four base parents' counters updated; In Validation tickets have started_at and no ticket is Done; the card's badges and dateLastActivity follow its actions; ZOM-543, ZOM-556 and ZOM-560 take their newest comment's time as updated_at.")
A("")
A("### Touched-data census")
A("")
A("See 'Touched-data census and coherence hazards' above: six hazard categories covered and SC-6, 7, 13, 14, 15, 16, 18, 19, 22, 38, 56, 57, 67, 68, 70 dispositioned.")
A("")
A("### Counter-readings")
A("")
A("| Category | Counter-reading (strongest argument it FAILS) | Evidence that resolves it | Verdict |")
A("|---|---|---|---|")
CR = [
    ("Temporal", "the sheet cites builds or PRs that did not exist when it was last saved", f"saved {AT['sheet']}; the newest build it cites is {BUILDS}/1759257787.502039 (18:43Z) and the newest PR {PR(475)} (opened 15:59Z)", "holds"),
    ("Temporal", "the later reports name a build that was not out yet", f"{BUILDS}/1759263189.219529 finished 20:13Z; {SL['reopen']} is 21:20Z and {SL['back']} 21:44Z, after an hour of play", "holds"),
    ("Temporal", "tickets ZOM-567 and up are dated before the base's last ticket", "ZOM-566 is 2025-09-30T16:26:02Z; ZOM-567 is 16:43Z and keys rise with time to ZOM-584 at 18:44Z", "holds"),
    ("Temporal", "Brian's DM says Thursday's review while the invitation says Friday", f"the card and the updated invitation {ID['invite_v2']} moved it to Thursday at 17:22Z to 17:24Z; the DM is 20:40Z", "holds"),
    ("Semantic / Category", "a review meeting does not belong on a roadmap board's Backlog list", "the list holds undated items Leonard keeps (cards 68c45c2bba569a224e81425d, 6851ab4165575ba2c16a6f05); Leonard runs this board alone (actions 68dc0eb3b933d6e0e75dad34)", "holds"),
    ("Semantic / Category", "'pass icon' means three things (the VFX remark, the restart, the glow)", f"the sheet row is the restart (ZOM-571), Marcus's report is the glow ({SL['filt_dm']}), and Vincent's Sep 24 remark {VDM}/1758721951.996909 is in his chat, which the note leaves out", "holds"),
    ("Cross-service Referential", "Arthur's comments contradict the base approval mails, which show no comment", f"they are separate COMMENTED reviews ({GH['inline']['review']}, {GH['inline2']['review']}) posted after the approvals and merges, each with its own mail in the same base thread", "holds"),
    ("Cross-service Referential", "the PR bodies say the fix is in", f"{PR(472)}'s body and walkthrough name only the Collect & Win wait and the reward VFX flow; {PR(475)}'s name the tap prompt, the close sequence and the last pack, never sound", "holds"),
    ("Cross-service Referential", "the Slack copies and the GitHub rows differ", "each copy carries the comment's text with & written as &amp;, the PR's title and the author's real login, as base copies do", "holds"),
    ("Quantitative", "the sheet's row count or the areas disagree with the note", f"38 numbered rows; the note lists ten areas and every row's Area is one of them", "holds"),
    ("Quantitative", "thread counters disagree after the seeded replies", "four UPDATEs set reply_count, reply_users_count and latest_reply on the base parents", "holds"),
    ("State / Lifecycle", "best argument the In Validation tickets are unintended: ZOM-571 and ZOM-581 say a fix is waiting for QA while the review says it is not in the PR", "the state is Vincent's dated claim from what he was told (his note on each ticket says so); Arthur's review is the PR's own record, and the note says the review wins", "holds (designed, T_INLINE, T_STATE)"),
    ("State / Lifecycle", "best argument the Todo on ZOM-572 is unintended: Oliver said the fix is merged an hour before Vincent filed it", "Vincent files from his sheet and does not read GitHub; the note makes the dev's line on his merged PR count", "holds (designed, T_ELSE)"),
    ("State / Lifecycle", "best argument rows 9 and 29 are unintended: the sheet says passed and a later message says it is back", "each later message names a newer main build and is by the tester or a founder; the note's own sentence resolves it", "holds (designed, T_REOPEN, T_BACK)"),
    ("State / Lifecycle", "best argument the 'ok, chat' rows are unintended: QA said ok and the dev considered it done", f"{BUILDS}/1758817549.151639 is a branch build and {ID['rule_doc']} says such a pass has to be done again after the merge; {PR(465)} merged later that day", "holds (designed, T_BRANCH)"),
    ("State / Lifecycle", "best argument the two review lists are unintended: Brian says Daily Gift, the card says Level-end rewards", "the card was changed a day after Brian's line by the review's organizer, the updated invitation says so, and Brian's later note defers to the card", "holds (designed, T_GATE)"),
    ("State / Lifecycle", "Leonard ticked the Queue Manager card on Sep 30, so the epic is finished", "the tick marks the feature as merged (68c453cd0ff184d95550bc58, 16:40Z); ZOM-543 is In Progress and Brian's DM, four hours later, asks for the stock-take", "holds"),
    ("Identifier / Format", "the GitHub mail ids and review numbers are invented", "they follow the base pattern and sit just under the approvals' numbers in the same threads", "holds"),
    ("Identifier / Format", "Julia's invitation subject ends with a name token", "base invitations in her mailbox end with ([PERSON_NAME_0043]) (threads/jlawson@harmonygames.co_1834845385842461999.json)", "holds"),
    ("People status", "a seeded speaker had left or was away", "activity.json: all nine seeded speakers are active_sep_2025_quiet_in_oct (1.C); no seeded record names Victor Barnes", "holds"),
    ("Other", "the notes on Vincent's tickets read as filler", "each is the per-ticket record Brian's note makes a reader check (whether a dev named a merged PR); two say a fix exists but no PR, which keeps those rows Waiting on a fix", "holds"),
    ("Other", "Brian's note reads as a rubric", "it is a lead's instruction on his own ticket in his words; it names no record's location, no build and no count", "holds"),
]
for row in CR + [tuple(x) for x in EXTRA.get("counter", [])]:
    A("| " + " | ".join(row) + " |")
A("")
UNRES = ["Whether Slack search indexes attachment text (the branch names in #builds, the #zombie-prs copies) is unverified until the pre-check.",
         "The under-60 % target rests on mechanisms whose landing rates are priors, not measurements (UNCALIBRATED).",
         "One directory listing of the mail export's thread file names was made outside `tools/hg.py` at this stage, to learn the naming; no record content was read that way and every fact was read through the helper."] + EXTRA.get("unresolved", [])
A("Unresolved: " + " ".join(UNRES))
A("")
open(os.path.join(WF, "01_Grounding_Dossier.md"), "w").write("\n".join(L) + "\n")
print("dossier", len("\n".join(L)), "chars", len(L), "lines")

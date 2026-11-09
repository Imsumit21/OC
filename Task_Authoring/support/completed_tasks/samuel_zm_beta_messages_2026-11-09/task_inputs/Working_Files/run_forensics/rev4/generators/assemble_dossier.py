#!/usr/bin/env python3
"""Assemble Working_Files/01_Grounding_Dossier.md from the SQL rows, the final manifest, truth.json, the id maps and the saved
tool outputs in plan/ (each re-run on the final SQL before this script, plan/run_checks.sh). No prompt, Oracle Event or
criterion wording. Re-run after any SQL, manifest or solver change, then re-run the stage gate."""
import collections, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402
SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
STM = parse_sql(SQL)
IDS = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
P = json.load(open(os.path.join(HERE, "ids.json")))
MAN = json.load(open(os.path.join(WF, "01_Hardness_Manifest.json")))
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
TRUTH = TRUTH.get("rows", TRUTH)
VOICE = json.load(open(os.path.join(HERE, "voice_quotes.json")))
EXTRA = json.load(open(os.path.join(HERE, "sweep_dispositions.json"))) if os.path.exists(os.path.join(HERE, "sweep_dispositions.json")) else {"changes": [], "counter": [], "rows": []}
I, BASE, T, Q, TK, M = P["ids"], P["base"], P["times"], P["quotes"], P["tickets"], P["members"]
SL = IDS["slack_mid"]
SAM = "samuel.turner@harmonygames.co"
QA_MSG = IDS["qa_msg"]


def rd(name):
    return open(os.path.join(HERE, name)).read().rstrip()


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
    ELEM[a["record"]].add(a["id"])
    ROLE[a["record"]] = "first link"
for f in MAN["ask_fragments"]:
    for x in f.get("seeded_ids") or []:
        ELEM[x].add(f["id"])
for h in MAN["authorities"]:
    for x in h.get("seeded_ids") or []:
        ELEM[x].add(h["id"])
        ROLE.setdefault(x, "authority")
for t in MAN["traps"]:
    for x in t.get("seeded_ids") or []:
        ELEM[x].add(t["id"])
    vr = t.get("version_records") or []
    for i, v in enumerate(vr):
        x = v.get("id")
        if x:
            ELEM[x].add(t["id"])
            ROLE[x] = "overturning" if i == len(vr) - 1 else "claim met first"
KEY_OF = {m["ticket"]: m["key"] for m in M if m["ticket"]}
AUD = {v: k for k, v in IDS["aud"].items()}
CARRIER = {"gcal.gcal_events": "● (summary, attendees, time, status; description ○)", "linear.linear_comments": "● (§6b)"}


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
    e = set(ELEM.get(rid, set()))
    t, r = x["table"], x.get("row") or {}
    if t == "linear.linear_issues" and rid in KEY_OF:
        e.add("cohort: " + KEY_OF[rid])
    if t == "linear.linear_issues" and rid == P["parent"]:
        e.add("K4 parent")
    if t == "linear.linear_comments":
        iss = r.get("issue_id")
        e.add("cohort: " + KEY_OF.get(iss, iss))
    if t == "linear.linear_team_memberships":
        e.add("write access for R6 on DES-314")
    if t == "linear.linear_teams":
        e.add("companion: team counter for R6")
    if x["op"] == "update" and t.startswith("slack"):
        e.add("companion: reply counters (Q01)")
    if x["op"] == "update" and t.startswith("trello"):
        e.add("companion: card badge and activity (T06)")
    if x["op"] == "update" and t == "linear.linear_issues":
        e.add("companion: relation back and updated_at")
    if t == "gmail.gmail_threads" or t.startswith("gslides") or t.startswith("gsheets") or t.startswith("gdocs") or t == "gdrive.drive_files":
        base = rid.split("#")[0]
        e |= ELEM.get(base, set())
    if rid in (IDS["invite_mail"], IDS["cancel_mail"]):
        e.add("T7 companion INT-11")
    if rid == IDS["arthur_mail"]:
        e.add("T1 companion INT-12")
    if t == "gmail.gmail_messages" and rid.endswith(QA_MSG.split("/", 1)[1]):
        e |= {"K8", "H2", "T4"}
    if t == "gmail.gmail_threads" and not e:
        e.add("thread row of the message below")
    if t == "gcal.gcal_events":
        e.add("T7")
    if rid == IDS["card_comment"]:
        e.add("K6")
    return ", ".join(sorted(e)) or "cohort"


def reach(x):
    t, r = x["table"], x.get("row") or {}
    if t.startswith(("linear", "trello", "github")):
        return "unscoped"
    if t.startswith("gmail"):
        return "persona mailbox" if r.get("user_email") == SAM else "sender's copy (companion, not evidence)"
    if t.startswith("gcal"):
        return "persona calendar" if r.get("calendar_id") == SAM else "organizer's copy (companion)"
    if t.startswith("slack"):
        return "persona in channel"
    return "shared with the persona"


def role(rid, el):
    if rid in ROLE:
        return ROLE[rid]
    if "companion" in el:
        return "companion"
    return "evidence"


# ---------------------------------------------------------------- header
A("# Grounding Dossier — samuel_zm_beta_messages · injection rev4 · contains no prompt, OE or criterion text")
A("")
A(f"Persona: Samuel Turner <{SAM}>, Game Designer. Universe: synth-cut, clock 2025-10-01T07:00Z, seed bound 2025-10-01T00:00:00Z (Tue Sep 30 17:00 PT). SQL: {n_ins} INSERT, {n_upd} UPDATE, 10 schemas.")
A("")
# ---------------------------------------------------------------- 1.A
A("## 1.A Structural")
A("")
A("Columns checked against `references/universe_schema_live.json`; NOT NULL columns marked !; shapes copied from the sibling records named here.")
A("")
A("| Table | Columns used (NOT NULL marked) | Location and sample ids | Notes |")
A("|---|---|---|---|")
A(f"| slack.slack_messages | id!, ts!, channel_id!, text, thread_parent_id, thread_ts_legacy, reply_count, created_at | messages/C08R8CHB0QL/2025-09.json ({BASE['martin_root']}), messages/D06UFE81RF0/2025-09.json ({BASE['android_2007_root']}) | id = the first 32 hex of the sha256 of channel, a pipe and ts; replies keep the root's id in thread_parent_id |")
A(f"| gmail.gmail_threads / gmail_messages | id!, user_email!; id!, thread_id!, user_email! | threads/samuel@harmonygames.co_1836006988541924555.json ({BASE['pr248_mail']}), threads/samuel@harmonygames.co_1831218752991293223.json | thread id = (ms<<20)+bits; one row per mailbox copy; GitHub and calendar mails copy those base messages' fields |")
A("| gdrive.drive_files / gdocs / gsheets / gslides | id!, name!, mime_type!; document_id; spreadsheet_id; presentation_id | gdrive data.json d_63fffeb4fab5233ed5bb73, d_65c76e0b87aa7e9b84d1df (owners' roots) | f_ + 22 hex; same id across Drive and the native row; identical sharing |")
A("| gcal.gcal_events | event_id!, calendar_id! | gcal data.json, Samuel's calendar samuel.turner@harmonygames.co | one row per attendee calendar, self:true on the owner's copy; status cancelled as on 1,033 base events |")
A("| linear.linear_issues / linear_comments / linear_team_memberships / linear_teams | id!, title!, priority!, labels_json!, links_json!, relations_json!, state_history_json!, is_archived!, created_at!, updated_at!; id!, issue_id!, author_id!, body!, is_edited!, created_at!, updated_at!; id!, team_id!, user_id!, created_at! | linear data.json DES-312, ZOM-542, ZOM-556; tmem_team_DES_usr_63fffeb4fab5233e | state_id holds the state name; state_history_json an empty JSON array on new issues; cmt_ + 20 hex (no base comments exist) |")
A(f"| trello.trello_actions / trello_cards (UPDATE) | id, type, date, idMemberCreator, idBoard, idCard, data_json | trello data.json {BASE['pn_card']}, {BASE['tech_card']}, action 6859879792d832a1e5c9f024 | id's first 8 hex = the action's Unix seconds; badges_json full shape |")
A(f"| github.github_review_comments / github_reviews | id!, pr_id!, seq! | github data.json {BASE['pr248']}#rc_17, {BASE['pr248']}#rev_6 | next id rc_18; diff_hunk is the real hunk from rc_16, the last revision before the comment, up to the commented line; line, position, commit_id null as on every base row |")
A("")
# ---------------------------------------------------------------- 1.B
A("## 1.B Entity")
A("")
A("| Entity | Spelling used | Where it appears (cited) | Agreement |")
A("|---|---|---|---|")
A(f"| Samuel Turner | {SAM} | slack EMPLOYEE_0004_SLACK_ID in {BASE['pns_sent']}; author of {BASE['pr248']}; Drive root {BASE['folder']}; Linear usr_caafeec2804b3a67 | AGREE |")
A(f"| Leonard Hayes | leonard.hayes@harmonygames.co | slack EMPLOYEE_0038_SLACK_ID in {BASE['pns_sent']}; Linear usr_63fffeb4fab5233e; Trello PERSON_6094_TRELLO_USER_ID; owner of {I['rule_doc']} | AGREE |")
A(f"| Vincent Parker | vincent.parker@harmonygames.co | slack EMPLOYEE_0012_SLACK_ID in {BASE['android_2007_root'].split('/')[0]}/1759164108.051389; Linear usr_65c76e0b87aa7e9b; owner of {IDS['qa_sheet']} | AGREE |")
A(f"| Robert | robert@harmonygames.co | slack EMPLOYEE_0016_SLACK_ID in {BASE['shove_to_20']}; Linear usr_Robert | AGREE |")
A(f"| Arthur Blake | arthur.blake@harmonygames.co | slack EMPLOYEE_0025_SLACK_ID in {BASE['no_push_yet']}; GitHub EMPLOYEE_0025_GITHUB_USERNAME, {BASE['pr248']}#rev_6; Linear usr_cc3e90160f490686 | AGREE |")
A(f"| Martin Walsh | martin.walsh@harmonygames.co | slack EMPLOYEE_0033_SLACK_ID in {BASE['martin_root']}; Linear usr_51f5f16d46e8cf55 | AGREE |")
A("| Brian Foster, Calvin Price, Julia Lawson, Oliver Brooks, Owen Baker | roster addresses | slack EMPLOYEE_0026, 0006, 0005, 0003, 0021 in C0880U9751A/1759189361.525409's channel members; Linear usr_fc22d5941b2aeb5c, usr_49b9dfa5208d400d, usr_8140f09bf9f1b94c, usr_bdf01b53c6a92c5e, usr_4e13bd40cc73d0fc | AGREE |")
A(f"| Zombie Match 3D | 'Zombie Match' on the sheet title, match3d in GitHub, zombie_match_3d in the warehouse | {BASE['pn_sheet']}, {BASE['pr248']}, wh USER_COHORT_RETENTION | AGREE |")
A(f"| Win & Collect / Collect & Win | row 7 says Win & Collect; DES-313 says Collect & Win | {BASE['pn_sheet']}, {BASE['liveops_page']} ('Same feature as Win & Collect on Domino Delights, under a different name'), {TK['Win & Collect start']} | DISAGREE (designed, T5) |")
A(f"| Boss Arena / Infinite HP Boss Mode | Boss Arena in Linear and tickets; the BETA list card says Infinite HP Boss Mode | ZOM-550, ZOM-553, ZOM-562; Trello BETA: Oct 10 list 6851a674975da1fe76e70d93 | AGREE (same feature, base naming) |")
A(f"| Daily gift / Daily Login / login calendar | ZOM-556 and ZOM-432 say daily gift; the card says Daily Login; row 12 says Login Calendar | ZOM-556, {BASE['pn_sheet']}, Trello July 18 list 6851a669fb9904d6d136b037 | AGREE (base naming, one feature) |")
A(f"| Endless, Zombie Lane, Plague Race | as on the live-ops page | {BASE['liveops_page']}, ZOM-517, ZOM-555, ZOM-459 | AGREE |")
A(f"| Axe Arena, Streak Fever, Nathan's Treasure Hunt | sheet rows; Domino Delights events on the live-ops page; Axe Arena card on Oct 21 | {BASE['liveops_page']}, {BASE['axe_card']}, {BASE['axe_postponed']} | AGREE |")
A(f"| Hourly Coins / Hourly Collection | row 2 says Hourly Coins; the Backlog card says Hourly Collection | {BASE['pn_sheet']}, {BASE['hourly_card']} | AGREE (one feature, Backlog) |")
A(f"| Rewarded Ads | ticket says rewarded ad; card on the Oct 21 list | {TK['Rewarded ad ready']}, Trello list 6851a677e090018224fb8c7f | AGREE |")
A(f"| Store builds | Android 0.3.127, iOS 0.3.40 | C0880U9751A/1758643365.607149 (Arthur, Sep 23: required versions) | AGREE |")
A("")
A("No roster person is renamed or re-titled. 'Nathan' appears only in the base feature name Nathan's Treasure Hunt, never as a person (fact_check warning dispositioned in the fact sheet).")
A("")
# ---------------------------------------------------------------- 1.C
A("## 1.C Voice and realism")
A("")
A("Seeded speakers, each with its activity.json (synth-cut KB) status at the clock:")
ACT = [("Leonard Hayes", "leonard.hayes@harmonygames.co", "hub, the line change, the freeze comment, the rule doc, the parent and row tickets"),
       ("Vincent Parker", "vincent.parker@harmonygames.co", "QA note, pass log, ticket comments, the DM reply"),
       ("Robert", "robert@harmonygames.co", "the ask decision, asks"), ("Arthur Blake", "arthur.blake@harmonygames.co", "inline comment, ticket notes"),
       ("Brian Foster", "brian.foster@harmonygames.co", "opinion post, asks"), ("Calvin Price", "calvin.price@harmonygames.co", "the Collect & Win ticket, an ask"),
       ("Julia Lawson", "julia.lawson@harmonygames.co", "asks"), ("Martin Walsh", "martin.walsh@harmonygames.co", "an ask"),
       ("Oliver Brooks", "oliver.brooks@harmonygames.co", "an ask"), ("Owen Baker", "owen.baker@harmonygames.co", "asks")]
for n, e, what in ACT:
    A(f"- {n} ({e}) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: {what}.")
A("")
A("Lengths and hours from conventions.json (synth-cut KB): slack.length_chars_by_channel_type private p50 51 / p90 156; the seeded one-liners run 60–180 characters and only the hub is long, as a request should be. slack.per_person_hours_and_style: Leonard's core UTC window 15–02, Robert's 14–03, Brian's 12–21, Vincent's 10–19. Every seeded post sits inside its author's window except Vincent's DM reply at 19:40Z, 40 minutes past it on a day he was still in that DM at 18:52Z (D06UFE81RF0/1759171978.790219). linear.states_by_team: DES has 1 In Review and 216 Done in the base; 26 In Review tickets is a visible rise, explained by a batch review under one parent.")
A("")
A("Real messages used as voice references:")
for n, qs in VOICE.items():
    if qs:
        A(f"- {n}: " + " · ".join(f"\"{t}\" ({i})" for i, t in qs))
A("")
A("Leonard writes plain, lower-stakes Slack and full sentences when asking for a deliverable; Arthur's ticket notes are one clause, lower case, as his base Slack is; Vincent's are short status lines. No seeded line is tidy prose in a casual channel, and no em dashes are used.")
A("")
# ---------------------------------------------------------------- 1.D
A("## 1.D Keyword")
A("")
A("| Term | Hits / pointer | Note |")
A("|---|---|---|")
for term, where, note in [
    ("PN sheet / Push Notifications Zombie Match", BASE["pn_sheet"], "found by title words; Leonard's Slack link uses a Google-native id (R04)"),
    ("Collect & Win", BASE["liveops_page"], "the name map; Linear search hits " + TK["Win & Collect start"]),
    ("Boss Arena", "ZOM-550, ZOM-553, ZOM-562", "the ask lives on ZOM-542 whose title says home screen"),
    ("daily gift", "ZOM-556, ZOM-432", "the ask is a comment on the bug"),
    ("permission", BASE["shove_to_20"] + ", " + BASE["variant_c_13"], "older dated claims met first; Robert's Sep 29 post is the latest"),
    ("rollover", BASE["pn_sheet"], "sheet rows; Arthur's comment " + I["arthur_inline"] + " and its mail in " + BASE["pr248_mail"]),
    ("NotificationManager", BASE["pr248"], "the client file; Arthur's ticket notes name it"),
    ("0.3.127", "C0880U9751A/1758643365.607149", "Arthur's required versions")]:
    A(f"| \"{term}\" | {where} | {note} |")
for term, where in [("message rule", I["rule_doc"]), ("Phone message checks", IDS["qa_sheet"]), ("Lapsed ladder review", I["ladder_review"]),
                    ("Beta readiness", I["deck"]), ("Beta player messages", P["parent"]), ("Your Squad Needs You Back", SL["corr_reply"]),
                    ("5-minute test build", SL["qa_reply"]), ("Held work", I["freeze_comment"])]:
    A(f"| \"{term}\" | NEW TERM — introduced in {where} | reached through the hub {SL['hub']} or its delegations |")
A("")
# ---------------------------------------------------------------- 1.E
A("## 1.E Persona reach")
A("")
A("Load-bearing scoped ids (seeded and base) written to `Working_Files/plan/load_bearing_scoped.txt`; output verbatim. Linear, Trello and GitHub are unscoped, so their ids are not in that list (Evals/references/persona/acl.md).")
A("")
fence(rd("checksql.txt"))
A("")
A(f"- {BASE['pns_sent'].split('/')[0]} — Samuel's DM with Leonard (im member) LB; seeded hub {SL['hub']} ({I['hub']}).")
A(f"- {BASE['android_2007_root'].split('/')[0]} — Samuel's DM with Vincent LB; seeded reply {SL['qa_reply']} under {BASE['android_2007_root']}.")
A(f"- C0880U9751A — #zombie-match3d, Samuel a member LB; seeded {SL['ask_decision']}, its reply {SL['ask_reply']}, {SL['brian_opinion']}.")
A(f"- C08R8CHB0QL — #zombie-art, Samuel a member LB; seeded reply {SL['corr_reply']} under {BASE['martin_root']}.")
A(f"- Samuel's mailbox LB: {QA_MSG}, the GitHub mail in {BASE['pr248_mail']}, {IDS['invite_mail']}, {IDS['cancel_mail']}.")
A(f"- Drive LB: {I['rule_doc']}, {I['deck']}, {IDS['qa_sheet']} are shared with Samuel; {BASE['pn_sheet']} is shared with him in the base; {BASE['folder']} is his root.")
A(f"- Calendar LB: {I['ladder_review']} is Samuel's own copy (self:true).")
A(f"- Unscoped: {P['parent']}, DES-313 to DES-346, ZOM-542, ZOM-556, {I['boss_ask']}, {I['gift_ask']}, {BASE['pn_card']}, {BASE['tech_card']}, {I['freeze_comment']}, {I['arthur_inline']}.")
A(f"- No designed denial: denied_probes is empty; other people's mailbox and calendar copies are companions, never evidence ({I['ladder_review']} is cited by Samuel's own copy).")
A("")
# ---------------------------------------------------------------- 1.F
A("## 1.F Collision")
A("")
A("base_check Check A compares every minted id against the full base collections (output in the Self-review, PASS). Scheme by service:")
A(f"- linear: DES-313 to DES-{P['last_ticket']}: base DES ends at DES-312 (linear data.json, 3,687 synth-cut issues read in full); {len(IDS['comments'])} issues carry cmt_ + 20 hex comment ids and the base has 0 comments.")
A(f"- slack: {len(SL)} seeded (channel, ts) pairs, ids {', '.join(SL.values())}: no base message in those channels at those ts (messages/C0880U9751A/2025-09.json, messages/C08R8CHB0QL/2025-09.json, messages/D06UFE81RF0/2025-09.json, messages/D06L58XCVKK/2025-09.json).")
A(f"- gmail: thread ids and RFC Message-IDs minted per seeded time; the GitHub message id {IDS['arthur_mail']} is a new review number between the base review mails 2963243580 and 2963696884.")
A(f"- trello: {I['freeze_comment']}, {IDS['card_comment']}: first 8 hex are the action's own seconds.")
A(f"- drive/calendar: {I['rule_doc']}, {I['deck']}, {IDS['qa_sheet']}, {I['ladder_review']}: sha-derived, 0 base hits.")
A(f"- github: {I['arthur_inline']} and {IDS['arthur_review']}: base ids on this PR end at rc_17 and rev_6.")
A("- Header tokens: none minted; PERSON_6094_TRELLO_USER_ID, SVC_0248, SVC_3649, SVC_0613, SVC_5111 and SVC_0842 are the base tokens those mails use. Body tokens: none minted.")
A("")
# ---------------------------------------------------------------- ledger
A("## Record ledger")
A("")
A("One row per SQL statement, in SQL order.")
A("")
A("| # | SQL line | Table | Id | Manifest element | Carrier | Reach | Discovery role |")
A("|---|---|---|---|---|---|---|---|")
for n, x in enumerate(STM, 1):
    rid = rid_of(x)
    el = element(x, rid)
    A(f"| {n} | L{x['line']} | {x['table']}{' (UPDATE)' if x['op'] == 'update' else ''} | {rid} | {el} | {CARRIER.get(x['table'], '●')} | {reach(x)} | {role(rid, el)} |")
A("")
# ---------------------------------------------------------------- findability
A("## Findability and discovery-order proofs")
A("")
A(f"- Hub A1 {SL['hub']} ({I['hub']}): the newest message in Leonard and Samuel's DM; the prompt names it; first link.")
A(f"- Rule doc H1 {I['rule_doc']}: the hub says 'the message rule doc'; a Docs or Drive search for 'message rule' returns it; decoy {BASE['gtm_beta_doc']} (GTM - Beta, Domino Delights 2024) differs on the game.")
A(f"- QA note H2 {QA_MSG}: the rule doc says 'his QA note'; Gmail search 'phone messages' or from Vincent returns it; decoy {BASE['release_page']} is the whole-build submission list.")
A(f"- Freeze H3 {I['freeze_comment']} on {BASE['tech_card']}: the rule doc says 'unless the roadmap says otherwise'; Trello search 'Held work' or reading the BETA list's comments; decoy {BASE['minor_bugs_card']} is for bug tickets.")
for t, s in [
    ("T1 DONE", f"claim met first: Status Ready on {BASE['pn_sheet']}, {TK['Weekly Leaderboard reset']} Done with Vincent's {I['weekly_qa']}, {BASE['pr248']}#rev_6 APPROVED; overturned by {I['arthur_inline']} (Jun 26) and the schedule in the same hunk; decisive because the rule's test 5 asks for the day and the row says rollover"),
    ("T2 CORR", f"claim met first: the June line on row 5 and {TK['Lapsed 7 days']}; overturned by {SL['corr_reply']} (Sep 29 18:05Z) under {BASE['martin_root']}; a search for 'taken over' finds it"),
    ("T3 DEP", f"claim met first: LIVE and Ready on row 6, Vincent's {I['ftue_qa']}; overturned by the join of the row's Level 20 trigger, the reach sentence in {I['rule_doc']} and {SL['ask_decision']}"),
    ("T4 QA", f"claim met first: {I['race_qa']} and {IDS['qa_sheet']}; overturned by {SL['qa_reply']} (Sep 29 19:40Z) under {BASE['android_2007_root']} with {QA_MSG}"),
    ("T5 ALIAS", f"claim met first: no child of {P['parent']} for row 7; overturned by {BASE['liveops_page']} and {TK['Win & Collect start']}"),
    ("T6 FILT", f"{TK['Boss Arena open']} relates to ZOM-542 and {TK['Daily chest ready']} to ZOM-556 in linear_list_issues; the asks are {I['boss_ask']} and {I['gift_ask']}"),
    ("T7 BUILT", f"claim met first: {TK['Lapsed 14 days']} reads as new; overturned by the batch in {BASE['pr248']} and {IDS['cancel_mail']}"),
    ("T8 FOLLOW", f"claim met first: the rule doc's last sentence; overturned by {I['freeze_comment']} (Sep 29, after the doc's Sep 26)"),
    ("T9", f"claim met first: {BASE['shove_to_20']}, {BASE['variant_c_13']}; overturned by {SL['ask_decision']}")]:
    A(f"- {t}: {s}.")
A("")
# ---------------------------------------------------------------- self-validation
A("## Self-validation")
A("")
A("| QC category | Tool-enforced (result) | Manual (evidence) |")
A("|---|---|---|")
A(f"| Missing Universe Data | check-sql PASS (1.E) | every deciding fact persona-readable: {I['arthur_inline']}, {SL['corr_reply']}, {SL['ask_decision']}, {SL['qa_reply']}, {I['boss_ask']}, {I['gift_ask']}, {IDS['cancel_mail']}, {I['freeze_comment']} |")
A(f"| Temporal Field | sql_lint 0 errors; base_check Check C PASS | {I['arthur_inline']} (Jun 26 20:58Z) precedes rev_6 and the merge; the rule doc (Sep 26) precedes the freeze (Sep 29) that amends it; the hub (Sep 30) is last |")
A(f"| Cross-service Referential | base_check Check A PASS | Arthur's required versions C0880U9751A/1758643365.607149 match {I['weekly_qa']}; DES-330/ZOM-542 and DES-338/ZOM-556 relate both ways |")
A(f"| Quantitative | reply counters and Trello badges updated | the deck's six equals the six Ready rows on {BASE['pn_sheet']}; {BASE['martin_root']} goes from 3 replies to 4 |")
A(f"| State / Lifecycle | six Done tickets have completed_at after their last comment | {P['parent']} stays In Progress with open children (L06 excluded); no comment on a closed ticket |")
A("| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A, 1.F) |")
A(f"| Semantic / Category | — | titles match content: {I['rule_doc']}, {IDS['qa_sheet']}, {I['ladder_review']}, {I['deck']} |")
A("| Other | — | voice per 1.C; no record states a call, a total or the plan |")
A("")
# ---------------------------------------------------------------- integrations
A("## Integrations and companions")
A("")
A("| Service | INT id | Companion | Decision |")
A("|---|---|---|---|")
A(f"| github | INT-01 | Slack copy of the inline comment | none: {I['arthur_inline']} (Jun 26) predates the match3d window that opens Jun 30 (integrations.json) |")
A(f"| github | INT-12 | GitHub mail to Samuel | seeded in the base PR thread: {IDS['arthur_mail']} |")
A("| github | INT-23 | CodeRabbit | none: a human comment |")
A(f"| linear | INT-03, INT-04, INT-05 | PR comment, Slack, mail notifications | none: the base has 0 Linear comments and no notification for them (Ask_Carriers §6b) |")
A(f"| gcal | INT-11 | invitation and cancellation mails | seeded for {I['ladder_review']}: {IDS['invite_mail']}, {IDS['cancel_mail']} |")
A(f"| gdrive | INT-13 | Drive share DMs | none: {I['rule_doc']} and {IDS['qa_sheet']} follow the base pattern of owner shares with no DM |")
A(f"| slack | INT-22 | Slack mail digests | none ({I['hub']}) |")
A(f"| trello | INT-21 | none exists | none ({I['freeze_comment']}) |")
A("| gdocs, gsheets, gslides, gmail | not integration sources | — | none |")
A("")
# ---------------------------------------------------------------- census
A("## Touched-data census and coherence hazards")
A("")
A(f"Touched data: {SL['hub']}, {I['rule_doc']}, {BASE['pn_sheet']} (all four tabs), {IDS['qa_sheet']}, {QA_MSG}, tickets DES-313 to DES-{P['last_ticket']}, ZOM-542, ZOM-556, ZOM-397, ZOM-366, ZOM-471, ZOM-539; ZM ROADMAP lists 6851a674975da1fe76e70d93, 6851a677e090018224fb8c7f, 68c451221ebabaf255a7d16b and cards {BASE['pn_card']}, {BASE['tech_card']}, {BASE['axe_card']}, {BASE['hourly_card']}; {BASE['pr248']} with its review comments; {BASE['liveops_page']}; the Sep 15 week of USER_COHORT_RETENTION; #zombie-bugs and #zombie-match3d around the ask point ({BASE['variant_c_13']}, {BASE['pushed_back']}, {BASE['all_local']}).")
A("")
A("Hazards from coherence_hazards.json:")
A(f"- temporal: T06 — both Trello comments update dateLastActivity (companions); T02 not touched: no thread file is read for order.")
A(f"- semantic: S01 — no row depends on ENG keys cited for ZOM work.")
A(f"- referential: R03 — no row reads a redacted GitHub subject; R04 — no row depends on a Google-native link; R07 — no #zombie-prs copy of {I['arthur_inline']}, declared under Integrations.")
A(f"- quantitative: Q01 — the seeded replies update the roots' reply_count, reply_users_count and latest_reply ({BASE['martin_root']}, {BASE['android_2007_root']}).")
A(f"- state/lifecycle: L06 — {P['parent']} is never Done; L03 — calls rest on the rule tests, never on a ticket state as proof of shipping; L08 — no seeded ticket is assigned to a quiet person.")
A(f"- identifier/format: I14 — the sheet's owner is a Resource id, so it is never a write target; I15 — the Drive name keeps .xlsx; I16 — Trello ids encode their action time.")
A("")
A("Known data issues (references/known_data_issues/synthcut.md; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):")
for c, why in [("SC-7", "channel lists: membership is used only for reach, never graded"), ("SC-13", "the list is named BETA: Oct 10: no date is graded, only 'on the BETA list'"),
               ("SC-14", "no complete flag is read"), ("SC-16", "no ticket state is proof of shipping; seeded DES tickets only"),
               ("SC-19", "no telemetry version matching; the store versions come from Arthur's Sep 23 post"), ("SC-28", "the note uses the warehouse's Sep 15 week, never the OKR page"),
               ("SC-36", "no invite or channel list is graded"), ("SC-38", "Season Pass rests on nothing being scheduled, never on a ship date"),
               ("SC-57", "no post in #zm-collect-win"), ("SC-68", "only 'in the beta' is used for Boss Arena, from the BETA list"), ("SC-70", "no timezone is graded")]:
    A(f"- {c}: {why}.")
A("")
# ---------------------------------------------------------------- disagreements
A("## Intended disagreements")
A("")
A("| Claim met first | Overturning record | Why realistic | Resolution |")
A("|---|---|---|---|")
DIS = [
    (f"Weekly Leaderboard reset Ready on {BASE['pn_sheet']}, {TK['Weekly Leaderboard reset']} Done, Vincent saw it ({I['weekly_qa']})", f"Arthur's inline comment {I['arthur_inline']} and the schedule in the hunk", "a reviewer approves with a caveat and the ticket closes on delivery alone", "rule test 5: the day matters"),
    (f"June line on row 5 and {TK['Lapsed 7 days']}", f"Leonard's reply {SL['corr_reply']}", "founders drop copy changes under whatever thread they are in", "the rule's latest-line sentence"),
    (f"LIVE and Ready on row 6; Vincent's {I['ftue_qa']}", f"{SL['ask_decision']} with the reach sentence in {I['rule_doc']}", "a message works on a device set up by hand and never reaches a real new player", "rule test 4"),
    (f"Vincent's pass {I['race_qa']} and {IDS['qa_sheet']}", f"Vincent's reply {SL['qa_reply']} with {QA_MSG}", "a tester corrects himself where he happens to be talking", "the later reply and the QA note"),
    (f"Row 7 with no child under {P['parent']}", f"{TK['Win & Collect start']} with {BASE['liveops_page']}", "a ticket filed before the batch, under the game's own name", "the hub's 'under whatever name'"),
    (f"{TK['Lapsed 14 days']} reads as new work", f"{BASE['pr248']} and {IDS['cancel_mail']}", "an ask from someone who has not read the schedule", "the rule's covered clause"),
    (f"The rule doc: Hold tickets go back to Todo ({I['rule_doc']})", f"Leonard's comment {I['freeze_comment']}", "a process rule amended where the roadmap lives", "the doc's own 'unless the roadmap says otherwise'"),
    (f"Robert's Jul 10 level 20 move, variant C's level 13 and Vincent's 'at the start of app' on iOS ({BASE['shove_to_20']}, {BASE['variant_c_13']}, {BASE['at_the_beginning']})", f"Robert's Sep 29 post {SL['ask_decision']} and Arthur's reply {SL['ask_reply']}", "an ask point that moved during testing, and a launch popup that Unity shows on its own", "the latest post; the reply explains the iOS popup"),
    (f"The deck's six Ready ({I['deck']}) and Brian's post ({SL['brian_opinion']})", f"The rule doc {I['rule_doc']}: neither status column decides", "summaries repeat a sheet nobody has revisited", "the rule"),
]
for a, b, c, d in DIS:
    A(f"| {a} | {b} | {c} | {d} |")
A("")
# ---------------------------------------------------------------- constraints
A("## Constraints for the prompt brief")
A("")
A("| Anchor | May be named (noun phrases only) | Record |")
A("|---|---|---|")
A(f"| A1 | Leonard's DM from yesterday; Leonard's DM | {SL['hub']} |")
A(f"| A2 | the Zombie Match PN sheet; the PN sheet | {BASE['pn_sheet']} |")
A(f"| A3 | my Drive folder | {BASE['folder']} |")
A("")
A("Never name in the prompt: the rule doc's tests or sentences, the QA note or the pass log, Robert's post, Leonard's reply under Martin's post, Vincent's DM reply, Arthur's inline comment, the freeze comment, the cancelled review, the off-parent tickets or Collect & Win, or any count.")
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
A("Warning disposition: DES-325's title and description name the base feature Nathan's Treasure Hunt (row 8 of the sheet), not the person; no person named Nathan acts in any seeded record.")
A("")
listed = {k: v for k, v in TRUTH.items() if v.get("Call")}
ag = collections.Counter(v["Call"] for v in listed.values())
A(f"Solver totals (`solver/truth.json`): {len(TRUTH)} keys looked at; {len(listed)} on the plan (Go {ag['Go']}, Hold {ag['Hold']}, Drop {ag['Drop']}); {len(TRUTH) - len(listed)} off the plan.")
A("")
# ---------------------------------------------------------------- facts for the human
A("## Facts for the human")
A("")
A("| Locator | Base/seeded | Fact | Reach | Role |")
A("|---|---|---|---|---|")
FH = [
    (SL["hub"], "seeded", f"Leonard to Samuel, {T['hub']}: the ask, the seven columns, the writes and the counts back", "DM member", "anchor"),
    (I["rule_doc"], "seeded", f"Leonard, {T['rule_doc']}: 'Beta message rule', six ordered tests and the Go, Drop and Hold definitions", "shared", "authority H1"),
    (QA_MSG, "seeded", f"Vincent to Samuel, Oliver, Owen, {T['qa_note']}: seen only counts on a store build; names the pass log", "mailbox", "authority H2"),
    (IDS["qa_sheet"], "seeded", "Vincent's Phone message checks: six built messages, the build of each pass; the race row gives iPhone and no iOS build; last changed 2025-09-24T15:00Z", "shared", "claim met first (T4)"),
    (I["freeze_comment"], "seeded", f"Leonard on {BASE['tech_card']}, {T['freeze']}: held work sits in Backlog, unassigned", "unscoped", "authority H3, overturning (T8)"),
    (SL["ask_decision"], "seeded", f"Robert in #zombie-match3d, {T['ask_decision']}: our own ask stays after level 20; the Unity popup at launch on iOS stays as it is", "channel member", "overturning (T9), evidence (T3)"),
    (SL["ask_reply"], "seeded", f"Arthur, reply under it, {T['ask_reply']}: the popup switches nothing on; NotificationManager only schedules once our own ask has run or the player switches it on from settings, on both platforms", "channel member", "evidence (T3)"),
    (SL["corr_reply"], "seeded", f"Leonard under {BASE['martin_root']}, {T['corr_reply']}: the new seven-day line", "channel member", "overturning (T2)"),
    (SL["qa_reply"], "seeded", f"Vincent under {BASE['android_2007_root']}, {T['qa_reply']}: the race iPhone pass was the test build; never arrived on the store build", "DM member", "overturning (T4)"),
    (I["arthur_inline"], "seeded", f"Arthur on {BASE['pr248']}, {T['arthur_inline']}: counts seven days from the last leave, not tied to the rollover", "unscoped", "overturning (T1)"),
    (BASE["pr248_mail"], "seeded row in a base thread", "GitHub mail of that comment, 2025-06-26T20:58Z, Message-ID review/2963610417", "mailbox", "companion"),
    (I["ladder_review"], "seeded", f"Cancelled 'Lapsed ladder review', Leonard and Samuel, updated {T['ladder_review']}", "own calendar", "evidence (T7)"),
    (IDS["cancel_mail"], "seeded", "Cancellation mail with Leonard's note: day 14 is already covered", "mailbox", "evidence (T7)"),
    (I["deck"], "seeded", f"Leonard's Beta readiness deck, {T['deck']}: six Ready", "shared", "decoy (T10)"),
    (SL["brian_opinion"], "seeded", f"Brian, {T['brian_opinion']}: send all the Ready ones", "channel member", "decoy (T12)"),
    (P["parent"], "seeded", "Leonard's parent ticket, 32 children", "unscoped", "evidence (K4)"),
    (TK["Win & Collect start"], "seeded", "Calvin's ticket, Sep 17, no parent, says Collect & Win", "unscoped", "evidence (T5)"),
    (I["boss_ask"], "seeded", f"Brian on ZOM-542, {T['boss_ask']}: the Boss Arena reminder ask", "unscoped", "evidence (T6)"),
    (I["gift_ask"], "seeded", f"Julia on ZOM-556, {T['gift_ask']}: the daily gift reminder ask", "unscoped", "evidence (T6)"),
    (I["ad_note"], "seeded", f"Leonard on {TK['Rewarded ad ready']}, {T['ad_note']}: he moved rewarded ads to Oct 21, they aren't in the beta (base action 68d1eb16ac8c64cf8165101d)", "unscoped", "evidence"),
    (BASE["pn_sheet"], "base", "PNs Beta tab: 14 rows, six Ready, last changed 2025-06-23T07:02:43Z", "shared", "evidence (K3)"),
    (BASE["pr248"], "base", "the client schedule: lives, first-mission, one day, the weekly batch of four, the weekly leaderboard batch, the daily race", "unscoped", "evidence (T1, T7)"),
    (BASE["liveops_page"], "base", "Collect & Win is Win & Collect under another name; Plague Race, Zombie Lane and Endless live; Axe Arena, Streak Fever and Nathan's Treasure Hunt are Domino Delights", "unscoped", "evidence (T5)"),
    (BASE["shove_to_20"], "base", "Robert, Jul 10: move the ask to level 20", "DM member", "claim met first (T9)"),
    (BASE["variant_c_13"], "base", "variant C asks at level 13", "channel member", "claim met first (T9)"),
    (BASE["axe_postponed"], "base", "Axe Arena postponed, Sep 22", "channel member", "evidence"),
    ("C0880U9751A/1758643365.607149", "base", "Arthur, Sep 23: required versions Android 0.3.127, iOS 0.3.40", "channel member", "evidence"),
    ("wh_USER_COHORT_RETENTION (ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION, snowflake.json /tables/10)", "base", "zombie_match_3d, week 2025-09-15: iOS D1 31.65, D7 9.28; Android D1 37.86, D7 10.68", "unscoped", "evidence (K17)"),
]
for r in FH:
    A("| " + " | ".join(r) + " |")
A("")
for row in EXTRA.get("rows", []):
    A(row)
# ---------------------------------------------------------------- platform follow-ups
A("## Platform follow-ups")
A("")
A(f"- ○ carrier: none load-bearing. The cancelled event {I['ladder_review']} has no description, as on every base event; {IDS['cancel_mail']} and the source carry the fact.")
A("- Relations on DES-330 and DES-338 must be seen rendering in linear_list_issues in the pre-check (B1 depends on it).")
A("- `linear_show_data` and the list query's scope are unverified: confirm in the pre-check that neither returns comments in bulk.")
A("- Forecast blind spot: in exact mode the forecast never fails write-content slots, so its E[avg] overstates the pass rate; the design-mode view is reported beside it under Preflight.")
A("- Pre-check: confirm counted calls exceed 130 per run and that no run shows `model_refusal_fallback`.")
A("- No independent red team ran (REDTEAM_* unset; fallback recorded in the scenario design §13; blind fork and coherence sweeps recorded below).")
A("")
# ---------------------------------------------------------------- self-review
A("## Self-review")
A("")
A("### Tool outputs (final SQL, verbatim)")
A("")
for f in ("sql_lint.txt", "base_check.txt", "base_claims.txt", "hardness_gate.txt"):
    fence(rd(f))
    A("")
A("hg.py lint: counts FAIL 0, CHECK 0, INFO 0; no CHECK line to disposition. sql_lint warnings: none.")
A("")
A("### Preflight (S4b–S5e)")
A("")
for f in ("oracle_kit.txt", "mutation.txt", "liveness.txt"):
    fence(rd(f))
    A("")
if os.path.exists(os.path.join(HERE, "forecast_inj.txt")):
    fence(rd("forecast_inj.txt").replace("'rejected': []", "'rejected': none"))
    A("")
    A("Forecast, read with care (UNCALIBRATED): this exact view cannot fail write-content slots, which hold 115 of the 183 weight, so its E[avg] of about 0.82 and its low P(all) are the optimistic end. The design view in `plan/forecast_output.txt`, which models the declared mechanisms over every slot, gives E[avg] 0.67 and P(all) 0.28 to 0.66. Only the pre-check can say which is closer. Rates are disclosed overrides sourced from stored runs.")
    A("")
A("Geometry: U passes the V3 cap; L_max is just under the margin and is advisory: the composed view counts direct slots only, while most of the task's weight is in write-content slots, which the design view models.")
A("")
A("### Changes made at this stage (and why)")
A("")
for d in MAN["design_delta"]:
    A(f"- {d['id']}: {d['change']}. {d['reason']}.")
A("- Scenario amendment, re-certified: Vincent's pass log joins T4 as its first gsheets version and the tenth injected schema, because it carries the build behind each pass, which test 6 needs; the count slots T1 and T3 moved to write_content because they read the DM, and oracle_kit cannot read a text selector as a solver value; Arthur's GitHub mail joins the base PR thread.")
for c in EXTRA.get("changes", []):
    A("- " + c)
A("")
A("### /injection Checks A–C walk")
A("")
A(f"- Inventory: {n_ins} INSERT, {n_upd} UPDATE, 0 DELETE, no upserts; tables {dict(by_table)}.")
A("- Check A (references and IDs): PASS: every channel, user, issue, thread, calendar, board, list and folder resolves (base_check Check A); uniqueness over the full collections (1.F); ownership, membership and shares give Samuel reach (check-sql PASS).")
A("- Check B (structure): PASS: sql_lint 0 errors; every *_json column is literal JSON; NOT NULL columns supplied; generated *_fts columns never written; camelCase Trello columns quoted.")
A(f"- Check C (dates, parents, statuses, counts): PASS: every seeded timestamp is before 2025-10-01T00:00Z; replies after their parents; both roots' counters updated; Done tickets have completed_at after their last comment and {P['parent']} stays open; Trello badges follow the comments.")
A("")
A("### Touched-data census")
A("")
A("See 'Touched-data census and coherence hazards' above: six hazard categories covered and SC-7, 13, 14, 16, 19, 28, 36, 38, 57, 68, 70 dispositioned.")
A("")
A("### Counter-readings")
A("")
A("| Category | Counter-reading (strongest argument it FAILS) | Evidence that resolves it | Verdict |")
A("|---|---|---|---|")
CR = [
    ("Temporal", "Vincent reports a seven-day message arriving on Sep 24 when the required store versions were set on Sep 23", f"{IDS['qa_sheet']} notes the phone date moved forward on the lapsed and weekly rows; C0880U9751A/1758643365.607149 fixes the versions", "holds"),
    ("Temporal", "the rule doc (Sep 26) refers to a QA note and a Robert decision that come later or earlier in confusing order", f"{QA_MSG} is Sep 15, before the doc; the doc says the ask is Robert's call and {SL['ask_decision']} (Sep 29) is his latest post, which the doc does not quote", "holds"),
    ("Temporal", f"Arthur's comment {I['arthur_inline']} predates the row it criticises being tracked", f"the comment is on the code in {BASE['pr248']}, Jun 26, before {BASE['pr248']}#rev_6 at 21:23:25Z; the sheet row existed from Jun 23 ({BASE['pn_sheet']})", "holds"),
    ("Semantic / Category", "Lapsed 7 days and the weekly reminder batch could be two messages, so 'covered' is unclear", f"the hunk in {I['arthur_inline']} shows one weekly batch with the sheet's headline; row 5 carries the same line", "holds"),
    ("Semantic / Category", "'In Review' on 26 DES tickets misdescribes tickets nobody has reviewed", f"Leonard's parent {P['parent']} asks for a call on each; they are in review for that call, and the rule sends them back", "holds"),
    ("Cross-service Referential", "Boss Arena is 'Infinite HP Boss Mode' on the board, so a ticket about Boss Arena may name another feature", "ZOM-550 and ZOM-553 use Boss Arena for that mode; the card is on the BETA: Oct 10 list", "holds"),
    ("Cross-service Referential", f"{SL['corr_reply']} sits in #zombie-art under a theme post, so it may not be a real decision", f"Leonard is the row's owner ({BASE['pns_sent']}) and the rule doc names the latest line he has called", "holds (designed, T2)"),
    ("Quantitative", "the deck's six could be read as six Go", f"{I['deck']} says six Ready on the sheet, and {BASE['pn_sheet']} has six Ready rows; the rule says neither status column decides", "holds"),
    ("Quantitative", f"{BASE['martin_root']}'s reply counters disagree with the export after the seeded reply", "UPDATE sets reply_count 4, reply_users_count 4 and the new latest_reply (Q01)", "holds"),
    ("State / Lifecycle", "six Done tickets contradict three of them being Holds", f"Done records that the code shipped and arrived on a device ({TK['Weekly Leaderboard reset']}, {TK['Plague Race']}, {TK['Finish first mission']}); the rule's tests ask more, and SC-16 says a ticket state is no proof", "holds (designed, T1, T3, T4)"),
    ("State / Lifecycle", f"best argument the race disagreement is unintended: {I['race_qa']} and {IDS['qa_sheet']} say passed while {SL['qa_reply']} says it never came through", "a dated human claim withdrawn by its own author five days later; the QA note states the standard", "holds (designed, T4)"),
    ("State / Lifecycle", f"best argument the freeze is unintended: the rule doc and {I['freeze_comment']} give two states for a Hold", "the doc says 'unless the roadmap says otherwise' and the comment is later, by the same author", "holds (designed, T8)"),
    ("State / Lifecycle", f"best argument the alias is unintended: {TK['Win & Collect start']} is a stray duplicate of a child that should exist", f"no child exists; the live-ops page {BASE['liveops_page']} maps the names; the ticket predates the parent", "holds (designed, T5)"),
    ("State / Lifecycle", f"best argument the Lapsed 14 ask is unintended: {TK['Lapsed 14 days']} has no note and could be a Hold", f"{IDS['cancel_mail']} and the batch settle it; the rule's Drop clause names covered messages", "holds (designed, T7)"),
    ("State / Lifecycle", f"best argument the first-mission Hold is unintended: {I['ftue_qa']} shows it arrives, so it reaches players", f"the rule's reach sentence says the settings toggle doesn't count, {SL['ask_decision']} keeps our own ask after level 20, and {SL['ask_reply']} says only that ask or the toggle schedules anything", "holds (designed, T3)"),
    ("State / Lifecycle", f"best argument the weekly Hold is unintended: {I['weekly_qa']} shows it arrives on both", "the rule's day test: the row says rollover and the code counts from the last leave", "holds (designed, T1)"),
    ("State / Lifecycle", f"best argument the headline change is unintended: {TK['Lapsed 7 days']} and {SL['corr_reply']} disagree", "the reply is later and by the row's owner; the rule takes the latest line he has called", "holds (designed, T2)"),
    ("State / Lifecycle", f"best argument the deck disagreement is unintended: {I['deck']} and the rule differ on what Ready means", "the deck repeats a sheet flag; the rule says neither status column decides", "holds (designed, T10)"),
    ("State / Lifecycle", f"best argument the ask-point disagreement is unintended: {BASE['at_the_beginning']} says iOS asks at launch while {SL['ask_decision']} says after level 20", f"both are true of different things: Arthur's Sep 23 post in #executives (C07C2866011/1758659424.324079) calls the launch prompt Unity's, and {SL['ask_reply']} says only our own ask switches messages on", "holds (designed, T9)"),
    ("Identifier / Format", f"the GitHub mail id {IDS['arthur_mail']} is invented", "it follows the base pattern and sits numerically between the two neighbouring review mails in the thread", "holds"),
    ("People status", "Victor Barnes or another leaver is named, or a seeded speaker had left", "activity.json: all ten seeded speakers are active at the clock (1.C); no seeded record names Victor", "holds"),
    ("Other", "the off-parent asks read as planted", f"{I['boss_ask']} and {I['gift_ask']} are one-line asks by a teammate on a ticket about the same feature, the way base work is discussed", "holds"),
]
for row in CR + [tuple(x) for x in EXTRA.get("counter", [])]:
    A("| " + " | ".join(row) + " |")
A("")
A("Unresolved: the reviewer of the scenario has not re-read the B5 fix; competency fit stays an open risk for /prompt (most writes are on Linear). Everything else above is closed.")
A("")
open(os.path.join(WF, "01_Grounding_Dossier.md"), "w").write("\n".join(L) + "\n")
print("dossier", len("\n".join(L)), "chars", len(L), "lines")

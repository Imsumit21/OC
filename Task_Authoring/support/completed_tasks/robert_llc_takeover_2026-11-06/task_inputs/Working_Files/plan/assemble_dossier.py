#!/usr/bin/env python3
"""Assemble Working_Files/01_Grounding_Dossier.md from the SQL rows, the final manifest, truth.json, the id maps and the
tool outputs saved by plan/run_checks.sh (re-run on the final SQL first). Design-only text: no prompt, Oracle Event or
criterion wording. Re-run after any SQL / manifest / solver change, then the stage gate."""
import collections, importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402

SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
STM = parse_sql(SQL)
S = json.load(open(os.path.join(HERE, "sql_ids.json")))
I = json.load(open(os.path.join(HERE, "ids.json")))
IDS, BASE, T, ISS = I["IDS"], I["BASE"], I["T"], I["issues"]
Q = json.load(open(os.path.join(HERE, "wording.json")))
C = json.load(open(os.path.join(HERE, "cohort.json")))
MAN = json.load(open(os.path.join(WF, "01_Hardness_Manifest.json")))
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
spec = importlib.util.spec_from_file_location("solver_mod", os.path.join(WF, "solver", "solver.py"))
SOLV = importlib.util.module_from_spec(spec)
spec.loader.exec_module(SOLV)
AGG = SOLV.aggregates(TRUTH)
TOT = AGG["totals"]
ROB, LEO, ART = "robert@harmonygames.co", "leonard.hayes@harmonygames.co", "arthur.blake@harmonygames.co"
SL = {k: v["id"] for k, v in S["slack"].items()}
SLOC = {k: v["locator"] for k, v in S["slack"].items()}
GM = {k: v[ROB]["message"] for k, v in S["gmail"].items() if ROB in v}
GT = {k: v[ROB]["thread"] for k, v in S["gmail"].items() if ROB in v}
LN = S["linear"]
EV_ROB = S["gcal"][ROB]


def rd(name):
    p = os.path.join(HERE, name)
    return open(p).read().rstrip() if os.path.exists(p) else f"({name} not produced yet)"


def fence(text):
    return ["```", text, "```"]


L = []
A = L.append
ins = [x for x in STM if x["op"] == "insert"]
n_ins, n_upd = len(ins), len([x for x in STM if x["op"] == "update"])

# ======================================================================== header
A("# Grounding Dossier — Robert · LLC take-over plan for Combo Fighter · injection rev4 · contains no prompt, OE or criterion text")
A("")
A("SQL: `task_inputs/01_Universe_Inject.sql` (stored byte for byte in `Working_Files/run_forensics/rev4/01_Universe_Inject.sql`. Earlier revisions are kept with their reviews, truth, solver, manifest and dossier: rev1 and rev2 in `run_forensics/rev1/` and `run_forensics/rev2/` (both passed /injection; rev2 failed /prompt, `run_forensics/rev2/1_prompt_FAIL_r2.md`), and rev3 in `run_forensics/rev3/` (passed /injection and /prompt at 5, failed /hardness at 2: `run_forensics/rev3/precheck/1a_hardness_FAIL_r3.md`, `Working_Files/01a_Hardening_Report.md`)), built by "
  "`Working_Files/plan/build_sql.py` from the certified design (`01_Scenario_Design.md`, draft manifest, surface) and the planned wording "
  "in `plan/wording.json`; final manifest by `plan/build_final_manifest.py`; solver `Working_Files/solver/solver.py` (truth `solver/truth.json`); "
  "this file by `plan/assemble_dossier.py`; every tool output below by `plan/run_checks.sh`. Universe normal (hg4-2026-08-31), seed bound and "
  "eval clock 2026-02-14T00:00:00Z (Fri Feb 13, 4:00 PM PT); Robert's today is Saturday Feb 14, 2026; the Slack export ends Feb 13 10:03 UTC "
  f"(NB-6) and every seeded Slack row is earlier. {n_ins} INSERT + {n_upd} UPDATE statements over 10 schemas (gdrive, gdocs, gsheets, gslides, "
  "slack, trello, gmail, gcal, github, linear). Snowflake and Confluence are read, never written. Every probability here is UNCALIBRATED.")
A("")

# ======================================================================== 1.A
A("## 1.A Structural")
A("")
A("| Table | NOT NULL columns supplied (live schema) | Base location · sample ids | Format notes |")
A("|---|---|---|---|")
A("| slack.slack_messages | id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, "
  "attachments_json, created_at, metadata_json | slack/messages/D04V95AAAHW/2026-02.json (root bc4bc3d0e2a0ea6ae92cb2a9712e8f76 = D04V95AAAHW/1770056235.480619); "
  "slack/messages/C05433XK267/2026-01.json /1236 (Jenkins job post 859c1e0166850fd72ed8d767ddf32fe7) | id = sha256(channel|ts)[:32]; ts 6 decimals; a reply "
  "carries thread_parent_id + thread_ts_legacy and its root's reply_count / reply_users_count / latest_reply are updated (Q01–Q03); Jenkins posts are "
  "SLACK_BOT_0005_SLACK_ID with text '' and one attachment (color, fallback, fields[0].value) |")
A("| gmail.gmail_threads / gmail_messages | id, user_email; id, thread_id, user_email | gmail threads/00014520.json (robert@harmonygames.co/1836972401494127045, "
  "App Store rejection); leonard.hayes@harmonygames.co/1855983949220444975 (dbt receipt) | thread id = mailbox/((ms << 20) + 20 bits); message id = mailbox/ + "
  "the RFC Message-ID; one copy per seeded mailbox (sender SENT, recipients INBOX); internal_date = date in ms; App Store mail from SVC_4131_EMAIL with the "
  "base labels (INBOX, CATEGORY_UPDATES, Label_ad4e31dc09, Label_aeb79a643f) |")
A("| gdrive.drive_files · gdocs.docs_documents · gsheets.sheets_spreadsheets / sheets_sheets · gslides.slides_presentations / pages / "
  "page_elements | id, name, mime_type; document_id, title; spreadsheet_id, title; spreadsheet_id, sheet_id, title; presentation_id, title; "
  "presentation_id, object_id; presentation_id, page_object_id, object_id | gdrive data.json /drive_files/0 (d_00003b5dc5d1e91bd4bd6f, parent "
  "d_63fffeb4fab5233ed5bb73 = Leonard's root); /drive_files/107 (parent d_9f7ba94f7526d54d8482ba = Robert's root); gslides f_0281d5b83f931db7fff2be "
  "(TEXT_BOX elements 9144000 × 5143500) | f_/d_ + 22 hex; identical owner and sharing on the Drive row and the native row; Docs body_text "
  "with TITLE / NORMAL_TEXT style runs; Google-native files carry no content_path |")
A("| gcal.gcal_events | event_id, calendar_id | gcal data.json (11,130 events, plan/idcheck/gcal.out.json) | one row per attendee calendar "
  "(self:true on the owner's copy), shared ical_uid 32 hex @hg4; evt_ + 22 hex; Mon Feb 16 18:00–18:45Z is a not-yet-happened event |")
A("| trello.trello_cards / trello_actions | id, name, idBoard, idList; id, type, date | trello data.json board 640643a3fd8f3ca308d9318e (449 cards, last idShort "
  "455; last activity 2025-11-12, card 688c4d14c312a27fa2747e40) | ids: first 8 hex = Unix seconds (I16); full badges_json shape; createCard action with "
  "board/card/list data |")
A("| github.github_pull_requests / branches / commits / pull_request_commits / timeline_events | id, repo_id, number; id, repo_id, name; sha, "
  "repo_id; id, pr_id, commit_sha; id, pr_id, event | github data.json /pull_requests/1046 (harmonygames-Games/GameOfDominoes#1916, merged by "
  "EMPLOYEE_0025_GITHUB_USERNAME, html_url null), /branches/981 (arthur.blake/boombitWithEcon), /timeline_events/4725–4726 (merged, closed) | "
  "PR id = repo#number; events #ev_n; commit sha 40 hex |")
A("| linear.linear_projects / linear_issues / linear_comments | id, team_id, name, priority, labels_json, links_json, is_archived, created_at, "
  "updated_at; id, title, priority, labels_json, links_json, relations_json, state_history_json, is_archived, created_at, updated_at; id, "
  "issue_id, author_id, body, is_edited, created_at, updated_at | linear data.json /issues/2377 (ENG-2437, newest ENG), /issues/509 (ART-705, "
  "state 'Backlog'), /projects (2 base projects) | id = identifier = ENG-2438…ENG-2474; state names as ids; Backlog carries no lifecycle stamp; "
  "comment ids comment_ + 32 hex (§6b ● carrier); linear_project_teams / _members are not writable (sql_lint) |")
A("")

# ======================================================================== 1.B
A("## 1.B Entity")
A("")
A("| Entity | Spelling used | Where it appears (cited) | Agreement |")
A("|---|---|---|---|")
ENT = [
    ("Robert", "robert@harmonygames.co · EMPLOYEE_0016_SLACK_ID · usr_Robert", f"C0ADGSZKR3R/1770839322.836779 (Soundly canceled); Drive root d_9f7ba94f7526d54d8482ba; deck {IDS['cf_deck']}", "AGREE"),
    ("Leonard Hayes", "leonard.hayes@harmonygames.co · EMPLOYEE_0038_SLACK_ID · usr_63fffeb4fab5233e · PERSON_6094_TRELLO_USER_ID", f"C0ADGSZKR3R/1770933601.686309; hub {SLOC['hub']}; ground rules {IDS['ground_rules']}; card {IDS['trello_card']}", "AGREE"),
    ("Arthur Blake ('Blake')", "arthur.blake@harmonygames.co · EMPLOYEE_0025_SLACK_ID · usr_cc3e90160f490686 · EMPLOYEE_0025_GITHUB_USERNAME", f"C0ADGSZKR3R/1770937232.664809 (KubLLC card); DM {SLOC['arthur_dm']}; PR {IDS['pr']}; Jenkins 'Arthur Blake' C05433XK267/1769619277.508249", "AGREE (I03: his base thread files use the blake@ alias)"),
    ("Sunset", "Sunset (the firm buying the data and running the sale)", "C0ADGSZKR3R/1770859962.210719; C07C2866011/1770839126.382429 (liquidates laptops, build machines)", "AGREE"),
    ("the LLC / KubLLC card", "the founders' LLC; Arthur's 'Kub card'", f"C0ADGSZKR3R/1770937232.664809 ('my KubLLC card'); Arthur's mail {GM['arthur_mail']} ('my Kub card')", "AGREE (short form)"),
    ("Calm Play LLC", "Calm Play LLC", f"C04UEQVDVB7/1701383740.580749 (fully owned by Harmony Games); C04UEQVDVB7/1703492127.063049; note {LN['Calm Play LLC']['comment']}", "DISAGREE (a stale suggestion the ground rules' vehicle sentence overrules; rev4: a control row, EXC purged)"),
    ("Combo Fighter", "Combo Fighter (CF)", f"C07C2866011/1770084297.911029; C09UHHN6PFZ/1770404397.819789; ENG-2438; deck {IDS['cf_deck']}", "AGREE"),
    ("Domino Delights", "Domino Delights (DD; repo GameOfDominoes)", f"C0ADGSZKR3R/1770789534.434749; snowflake tables/12 game_id domino_delights; ENG-2439; {IDS['pr']}", "AGREE"),
    ("Zombie Match 3D", "Zombie Match (ZM; 'Puzzles vs Zombies' until July 2025)", "C07C2866011/1752548116.304169 (transfer); confluence page_aws_infra (one account for dev and prod); ENG-2440", "AGREE"),
    ("BoomBit", "BoomBit (publishing test on DD)", "C09SWTHEMEW/1770725775.479449; C09SWTHEMEW/1770977006.104929 (test stopped Feb 13)", "AGREE"),
    ("VO campaign", "the CF VO campaign, $100/day", f"C09UHHN6PFZ/1770404397.819789, C09UHHN6PFZ/1770404445.795829, C07C2866011/1770489896.754049; status {SLOC['vo_status']}; deck {IDS['cf_deck']}", "DISAGREE (designed: 'both campaigns live' Feb 7 vs 'only the CF VO campaign' Feb 12)"),
    ("Metabase / dbt", "Metabase, dbt (dbt is [USERNAME_30019] in #winddown, NB-12)", f"C0ADGSZKR3R/1770933903.645709; C0ADGSZKR3R/1770937232.664809; dbt receipt leonard.hayes@harmonygames.co/1855983949220444975 ($100); mail {GM['arthur_mail']}", "AGREE (the seeded mail spells dbt out)"),
    ("GitHub", "GitHub team plan", f"C0ADGSZKR3R/1770933450.410449 (keep until data is sold, then transfer); mail {GM['arthur_mail']} ($48 now that copilot is off)", "AGREE"),
    ("Kapwing", "Kapwing ([PERSON_NAME_20852] in Arthur's #winddown line, NB-12)", f"C0ADGSZKR3R/1770933450.410449 ('Kapwing (Blake)'); C0ADGSZKR3R/1770937188.477219; notice blake@harmonygames.co_1856962040028188034.json; note {LN['Kapwing']['comment']}", "AGREE (the note spells it out)"),
    ("layer.ai", "layer.ai ('layer' in #winddown)", "C09UHHN6PFZ/1770837702.167889 (access until March 3rd); C0ADGSZKR3R/1770837793.168589", "AGREE"),
    ("Helpshift", "Helpshift", "C0ADGSZKR3R/1770789534.434749 (off DD and ZM before Feb 28th); checklist C0ADGSZKR3R/1770933450.410449", "AGREE (NB-5 date never used)"),
    ("Figma", "Figma", f"C0ADGSZKR3R/1770859313.592649 (good until September 11th); C0ADGSZKR3R/1770933601.686309; note {LN['Figma']['comment']}", "AGREE"),
    ("build machines", "the Android and Apple build machines", f"C04UEQVDVB7/1700755756.051439 (HG orders them, 2023); C07C2866011/1770839126.382429; note {LN['Build machines']['comment']}", "AGREE"),
    ("REVENUE_DAILY", "ANALYTICS.MONETIZATION.REVENUE_DAILY ('the warehouse's daily revenue table')", f"snowflake snowflake.json /tables/12; /tables/13 (REVENUE_DAILY_V2, same January sums); ground rules {IDS['ground_rules']}", "AGREE"),
    ("AWS guide", "AWS Infrastructure Guide (page_aws_infra)", f"confluence_working.json /pages/2 (Fargate Phoenix + Nakama ~$650/mo); note {LN['Zombie Match account (AWS)']['comment']}", "AGREE"),
    ("Jenkins DD iOS Submission", "DD iOS Submission #218", f"C05433XK267/1769619277.508249 (#216), C05433XK267 2026-01 /1238 (#217, last base job); seeded {SLOC['builds_start']}, {SLOC['builds_result']}", "AGREE"),
    ("PR #1917", "GameOfDominoes#1917 'Replace Helpshift with support email'", f"{IDS['pr']}; base #1916 = harmonygames-Games/GameOfDominoes#1916 (Dec 26, 2025); note {LN['Domino Delights player support']['comment']}", "AGREE (new; #1916 is the last base PR)"),
    ("LLC take-over project", "Linear project 'LLC take-over' (team_ENG) with ENG-2438…ENG-2474", f"{IDS['project']}; base max ENG-2437 (linear data.json /issues/2377)", "AGREE (new)"),
    ("founders' board", "Trello 'Harmony Games' board, To Do list", "640643a3fd8f3ca308d9318e, list 640643a3fd8f3ca308d93195; card " + IDS["trello_card"], "AGREE"),
    ("ground rules doc", f"'{S['titles']['ground_rules']}'", IDS["ground_rules"], "AGREE (new)"),
    ("notes doc", f"'{S['titles']['notes_doc']}'", IDS["notes_doc"], "DISAGREE (designed: superseded by the ground rules)"),
    ("draft sheet", f"'{S['titles']['draft_sheet']}'", IDS["draft_sheet"], "DISAGREE (designed: stale numbers, layout source)"),
    ("Robert's deck", f"'{S['titles']['deck']}'", IDS["cf_deck"], "AGREE"),
    ("Monday call", "'LLC: decide', Mon Feb 16 10:00–10:45 PT", f"{EV_ROB} (Robert's copy); {IDS['monday_evt']} (Leonard's)", "AGREE (new)"),
]
for e in ENT:
    A("| " + " | ".join(e) + " |")
A("")
A("Robert's Linear id is the base's 'usr_Robert' (I10); Arthur's GitHub login is the token EMPLOYEE_0025_GITHUB_USERNAME (I08). No roster person is renamed or re-titled; no new header token is minted (SVC_4131_EMAIL is App Store Connect's base sender).")
A("")

# ======================================================================== 1.C
A("## 1.C Voice and realism")
A("")
A("Seeded speakers, each with its activity.json (normal KB) status at the clock:")
A(f"- Leonard Hayes (leonard.hayes@harmonygames.co, EMPLOYEE_0038_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds the hub {SLOC['hub']} (Feb 13 05:40Z = Thu 21:40 PT), the #prototype status {SLOC['vo_status']} (Feb 12 23:20Z), 29 issue notes (Feb 13 00:24–01:16Z), the docs {IDS['ground_rules']} and {IDS['notes_doc']}, the draft {IDS['draft_sheet']}, the card {IDS['trello_card']}, the split mail {GM['split_mail']} and the Monday event; last base post C0ADGSZKR3R/1770937460.360699 (Feb 12 23:04Z).")
A(f"- Arthur Blake (arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds the DM reply {SLOC['arthur_dm']} (Feb 13 03:10Z = Thu 22:10 ET), 8 issue notes (Feb 13 00:55–01:37Z), the billing mail {GM['arthur_mail']} (02:35Z) and PR {IDS['pr']} (opened 18:05Z, merged 21:10Z Feb 12); last base post C0ADGSZKR3R/1770937232.664809 (Feb 12 23:00Z).")
A(f"- Robert (robert@harmonygames.co, EMPLOYEE_0016_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds only his Feb 8 deck {IDS['cf_deck']} (Robert's base #prototype posts run to C09UHHN6PFZ/1770923166.200169, Feb 12).")
A("- Bots and services (not personas, no activity.json entry): Jenkins SLACK_BOT_0005_SLACK_ID (base #builds poster, C05433XK267/1769619277.508249), App Store Connect SVC_4131_EMAIL (base INT-08 sender, threads/00014520.json).")
A("")
A("Lengths, hours and titles from conventions.json (normal KB): slack.length_chars_by_channel_type im p50 38 / p90 ~105 / p99 well above 600 — the hub (~610 characters) sits in the im tail like Leonard's long base DMs (D04UP2L3E3S/1770876340.333289 runs ~300) and his #winddown drafts (C0ADGSZKR3R/1770673717.808759); Arthur's DM reply (~120) and Leonard's #prototype reply (~150, private p90 155) are ordinary. "
  "slack.per_person_hours_and_style: Leonard's core 80% UTC window 15–02 and Arthur's 15–01; the #prototype status (23:20Z) and the issue notes (00:24–01:37Z) fall inside them, while the hub (05:40Z) and Arthur's DM (03:10Z) are late-evening posts in each author's 20% tail, like Leonard's base 05:58Z #winddown post C0ADGSZKR3R/1770789534.434749 in the same week. "
  "gmail.internal_subject_len_chars p50 42: 'LLC money' and 'billing moved to my card' are short like Leonard's base subjects; gcal.duration_min p50 30 / p75 45: the Monday call is 45 minutes; "
  "linear.title_prefixes_by_team ENG: titles with no prefix dominate — the issue titles are plain item names; github.pr_title_patterns 'free text' and branch_patterns 'name/description' — 'Replace Helpshift with support email' and arthur.blake/supportEmail follow them.")
A("")
A("Voice from real messages: Leonard writes lower-case, run-on Slack lines and fragments ('I'll keep Intuit for now', C0ADGSZKR3R/1770839688.408909; 'we have time for Carta renewal so I'm not gonna really touch that', C0ADGSZKR3R/1770932858.658179); Arthur is terse ('coderabbit is cancelled', C0ADGSZKR3R/1770936655.574079; 'cursor and [PERSON_NAME_20852] cancelled', C0ADGSZKR3R/1770937188.477219). The seeded notes and messages keep those registers; the docs are short plain-sentence notes like Leonard's base #winddown lists.")
A("")

# ======================================================================== 1.D
A("## 1.D Keyword")
A("")
A("| Term | Hits / pointer | Note |")
A("|---|---|---|")
KW = [
    ("\"Helpshift\"", "base C0ADGSZKR3R/1770789534.434749, C0ADGSZKR3R/1770673717.808759; seeded PR " + IDS["pr"], "Feb 28 comes from Leonard's line, not the vendor ack (NB-5)"),
    ("\"layer\" / \"layer.ai\"", f"base C09UHHN6PFZ/1770837702.167889, C0ADGSZKR3R/1770837793.168589; seeded reply {SLOC['layer_reply']} (rev4)", "access until March 3rd; the reply says CF's concept art is only there and asks Robert to pull it out"),
    ("\"jenkins\"", f"base #builds C05433XK267 Jenkins posts; seeded {GM['jenkins_mail']} (rev4) and Arthur's ENG-2446 note", "the email's second paragraph carries CF's account at $62 now"),
    ("\"KubLLC\" / \"Kub card\"", f"base C0ADGSZKR3R/1770937232.664809; seeded {GM['arthur_mail']}", "Arthur's own card"),
    ("\"Calm Play\"", f"base C04UEQVDVB7/1701383740.580749, C04UEQVDVB7/1703492127.063049; seeded {LN['Calm Play LLC']['comment']}", "an older-channel search returns the subsidiary posts"),
    ("\"VO campaign\" / \"campaign\"", f"base C09UHHN6PFZ/1770404397.819789, C07C2866011/1770489896.754049; seeded {SLOC['vo_status']}", "in no list; a #prototype or #executives read finds it"),
    ("\"REVENUE_DAILY\"", "snowflake snowflake.json /tables/12 (2,284 rows; January sums DD 183.11, CF 7.36, ZM 0.00)", "the ground rules call it 'the warehouse's daily revenue table'"),
    ("\"Fargate\" / \"Nakama\"", "confluence_working.json /pages/2", "the cost note behind ZM's hosting (Fargate ~$650 + Aurora ~$420)"),
    ("\"boombitWithEcon\"", "base C05433XK267 2026-01 /1237 (Blake/boombitWithEcon); github /branches/981 (arthur.blake/boombitWithEcon)", "NB-13 form difference; no branch is graded"),
    ("\"LLC ground rules\"", f"NEW TERM — introduced in {IDS['ground_rules']}", "reached via the hub ('the ground rules doc')"),
    ("\"LLC take-over\"", f"NEW TERM — introduced in {IDS['project']}", "reached via the hub ('the LLC project in linear')"),
    ("\"LLC: what we take from HG\"", f"NEW TERM — introduced in {IDS['trello_card']}", "reached via the ground rules ('the LLC card on our board')"),
    ("\"LLC 90 days (draft)\"", f"NEW TERM — introduced in {IDS['draft_sheet']}", "reached via the hub ('my draft from Tuesday')"),
    ("\"LLC notes\"", f"NEW TERM — introduced in {IDS['notes_doc']}", "reached by a Drive search for 'LLC' (the H1 decoy)"),
    ("\"LLC money\"", f"NEW TERM — introduced in {GM['split_mail']}", "reached via the hub ('I'll email you how we split the money')"),
    ("\"$140\" (DD prod account)", f"NEW TERM — introduced in {SLOC['arthur_dm']}", "a DM search for 'prod account' / 'Domino' / 'month' returns it"),
    ("\"$248\"", f"NEW TERM — introduced in {GM['arthur_mail']}", "a mail search for 'metabase' / 'dbt' / 'github' / 'billing' returns it"),
    ("\"$62\" (CF's account)", f"NEW TERM — introduced in {GM['jenkins_mail']} (rev4; ENG-2445's note now says ~$95)", "a mail search for 'jenkins', 'backend', 'AWS' or from:arthur returns it"),
    ("\"concept art\"", f"NEW TERM — introduced in {SLOC['layer_reply']} (rev4)", "a Slack search for 'layer.ai' returns the post it replies to"),
    ("\"without a mail account set up it does nothing\"", f"NEW TERM — introduced in {GM['asc_notice']}", "the App Store notice; a mail search for 'Domino Delights' or 'submission' returns it"),
    ("\"#218\" / \"Replace Helpshift with support email\"", f"NEW TERM — introduced in {SLOC['builds_result']}, {IDS['pr']}", "#builds and GitHub"),
    ("\"LLC: decide\"", f"NEW TERM — introduced in {EV_ROB}", "the Monday call"),
]
for k in KW:
    A("| " + " | ".join(k) + " |")
A("")
A("Base controls for the seeded searches: 'Domino' in D04V95AAAHW returns only base git-debugging messages before the seeded reply; 'Kub' returns only C0ADGSZKR3R/1770937232.664809 in base Slack; 'support email' has no base hit in Robert's mailbox (the base DD mails are TestFlight and review notices).")
A("")

# ======================================================================== 1.E
A("## 1.E Persona reach")
A("")
A(f"Load-bearing scoped ids (seeded and base) written to `Working_Files/plan/load_bearing_ids.txt` ({len(open(os.path.join(HERE, 'load_bearing_ids.txt')).read().split())} ids; Linear, GitHub, Trello, Snowflake and Confluence are unscoped); output verbatim:")
A("")
L.extend(fence(rd("checksql.txt")))
A("")
A(f"- D04UP2L3E3S — Robert's DM with Leonard (im, Robert in members) LB: the hub {SLOC['hub']} (row {SL['hub']}).")
A(f"- D04V95AAAHW — Robert's DM with Arthur (im) LB: Arthur's reply {SLOC['arthur_dm']} (row {SL['arthur_dm']}) under the base root D04V95AAAHW/1770056235.480619.")
A(f"- C09UHHN6PFZ — #prototype, Robert a member LB: Leonard's status {SLOC['vo_status']} (row {SL['vo_status']}) under C09UHHN6PFZ/1770404397.819789; base C09UHHN6PFZ/1770404445.795829, C09UHHN6PFZ/1770837702.167889, C09UHHN6PFZ/1770845002.610529.")
A(f"- C05433XK267 — #builds, Robert a member LB: Jenkins {SLOC['builds_start']}, {SLOC['builds_result']}.")
A("- C0ADGSZKR3R — #winddown, Robert a member LB: C0ADGSZKR3R/1770933450.410449, C0ADGSZKR3R/1770933601.686309, C0ADGSZKR3R/1770933903.645709, C0ADGSZKR3R/1770937232.664809, C0ADGSZKR3R/1770680984.725779, C0ADGSZKR3R/1770682219.100789, C0ADGSZKR3R/1770789534.434749, C0ADGSZKR3R/1770859313.592649, C0ADGSZKR3R/1770932709.222409.")
A("- C07C2866011 — #executives, Robert a member LB: C07C2866011/1770612982.268919, C07C2866011/1770850800.723979, C07C2866011/1770489896.754049; C04UEQVDVB7 (#admin_foundersonly) LB: C04UEQVDVB7/1701383740.580749, C04UEQVDVB7/1703492127.063049.")
A(f"- Robert's mailbox (INBOX copies, user_email robert@harmonygames.co) LB: {GM['split_mail']} (thread {GT['split_mail']}), {GM['arthur_mail']} (thread {GT['arthur_mail']}), {GM['asc_notice']} (thread {GT['asc_notice']}), invitation {GM['invite|' + ROB]}.")
A(f"- Drive: {IDS['ground_rules']}, {IDS['notes_doc']} and {IDS['draft_sheet']} are Leonard's, shared with Robert (shared_with_emails); {IDS['cf_deck']} is Robert's own; the write target is Robert's root d_9f7ba94f7526d54d8482ba LB.")
A(f"- Calendar: Robert's own copy {EV_ROB} (self:true) LB.")
A(f"- Unscoped (visible to all): the project {IDS['project']}, ENG-2438…ENG-2474 and their 37 notes, the card {IDS['trello_card']}, PR {IDS['pr']}, snowflake ANALYTICS.MONETIZATION.REVENUE_DAILY, confluence page_aws_infra.")
A(f"- No designed denial: denied_probes is empty; evidence is always Robert's own copy (for example {GM['split_mail']}), and Leonard's and Arthur's mailbox and calendar copies are companions, never evidence.")
A("")

# ======================================================================== 1.F
A("## 1.F Collision")
A("")
A("Every id the SQL mints was looked up over its full base collection (`tools/hg.py search lookup`, outputs in `plan/idcheck/`):")
for k, label in [("gdrive", "drive_files"), ("gcal", "events"), ("trello_card", "cards"), ("trello_action", "actions"), ("linear_issue", "issues"),
                 ("linear_project", "projects"), ("github_pr", "pull_requests"), ("github_branch", "branches"), ("github_commit", "commits"),
                 ("github_event", "timeline_events"), ("slack", "messages/*/*.json"), ("gmail_msg", "threads/*.json /messages")]:
    p = os.path.join(HERE, "idcheck", k + ".out.json")
    try:
        d = json.load(open(p))
        hits = sum(1 for v in (d.get("matches") or {}).values() if v)
        A(f"- {k} ({label}): {len(d.get('matches') or {})} ids, {d.get('records_checked')} base records checked, scan_complete {d.get('scan_complete')}, {hits} matches (plan/idcheck/{k}.out.json).")
    except (OSError, ValueError):
        A(f"- {k}: lookup output missing")
gts = [l.split() for l in rd("idcheck/gmail_thread_search.txt").splitlines() if l.strip()]
A(f"- gmail thread ids (single-object thread files cannot be array-looked-up): each of the {len(gts)} numeric thread ids searched over all mail — "
  f"{sum(1 for g in gts if g[1] == '0')} of {len(gts)} with 0 matches, scan_complete {all(g[2] == 'True' for g in gts)}, {gts[0][3] if gts else '?'} thread files each "
  "(plan/idcheck/gmail_thread_search.txt); base_check Check A full-collection uniqueness PASS.")
A("- Linear comment ids (comment_ + 32 hex) and Slides object ids (slide_/el_ + 12 hex) have no base rows to collide with (NB-24: the Linear export has no comments; gslides ids are per-presentation).")
A("- Slack (channel, ts) pairs: base_check Check A PASS on the four channels' month files; the hub ts 1770961200.890407 is the only D04UP2L3E3S message after Feb 12 16:36Z.")
A("- Header tokens: none minted (SVC_4131_EMAIL, SLACK_BOT_0005_SLACK_ID, EMPLOYEE_00NN ids are base identities used for their own people/services). Body tokens: '[PERSON_NAME_0054]' (Robert's greeting token in base App Store mail, threads/00014520.json) and a new '[IDENTIFIER_n]' submission id, as in the base template.")
A("")

# ======================================================================== record ledger
ELEM = collections.defaultdict(set)
for f in MAN["ask_fragments"]:
    for x in f.get("seeded_ids") or []:
        ELEM[x].add(f["id"])
for h in MAN["authorities"]:
    for x in h.get("seeded_ids") or []:
        ELEM[x].add(h["id"])
    for x in h.get("decoy_seeded_ids") or []:
        ELEM[x].add(h["id"] + " decoy")
for t in MAN["traps"]:
    for x in t.get("seeded_ids") or []:
        ELEM[x].add(t["id"])
    for v in t.get("version_records") or []:
        if v.get("id"):
            ELEM[v["id"]].add(t["id"])
for c in MAN["chains"]:
    for h in c["hops"]:
        ELEM[h["record"]].add(c["id"])
for m in C:
    if m.get("linear"):
        ELEM[m["linear"]].add("cohort: " + m["key"])
        ELEM[LN[m["key"]]["comment"]].add("cohort note: " + m["key"])
CARRIER = {"linear.linear_comments": "● (§6b)", "gcal.gcal_events": "● (summary, time, attendees; description ○)"}


def rid_of(x):
    r = x.get("row") or {}
    t = x["table"]
    if t in ("gslides.slides_pages", "gslides.slides_page_elements"):
        return f"{r['presentation_id']}#{r['object_id']}"
    if t == "gsheets.sheets_sheets":
        return f"{r['spreadsheet_id']}#{r['sheet_id']}"
    for k in ("id", "event_id", "document_id", "spreadsheet_id", "presentation_id", "sha"):
        if r.get(k):
            return str(r[k])
    return str(next(iter((x.get("where") or {}).values()), "?"))


def reach_of(x):
    r, t = x.get("row") or {}, x["table"]
    if t.startswith("gmail"):
        return "Robert's mailbox" if str(r.get("user_email", "")) == ROB else "other mailbox (companion)"
    if t == "gcal.gcal_events":
        return "Robert's calendar (self)" if r.get("calendar_id") == ROB else "other calendar (companion)"
    if t.startswith("slack"):
        return "member (" + str(r.get("channel_id") or "root UPDATE") + ")"
    if t.startswith(("gdrive", "gdocs", "gsheets", "gslides")):
        return "Drive owner or share"
    return "unscoped"


def role_of(x, rid, el):
    t, r = x["table"], x.get("row") or {}
    if x["op"] == "update":
        return "companion (root reply counters)"
    if t.startswith("gmail") and r.get("user_email") != ROB:
        return "companion copy"
    if t == "gcal.gcal_events" and r.get("calendar_id") != ROB:
        return "companion copy"
    if "Invitation" in str(r.get("subject") or ""):
        return "companion (INT-11 invitation)"
    if rid in (SL["hub"],):
        return "first link (anchor AN1)"
    if rid == IDS["project"]:
        return "first link (anchor AN2)"
    if any(e.endswith("decoy") for e in el):
        return "decoy"
    if any(e in ("H1", "H2", "H3") for e in el):
        return "authority"
    if rid in (SL["arthur_dm"], GM["arthur_mail"], GM["asc_notice"], SL["vo_status"], SL["layer_reply"], GM["jenkins_mail"]) or rid.split("#")[0] == IDS["cf_deck"]:
        return "overturning"
    if rid in (LN["Domino Delights production account (AWS)"]["comment"], LN["Metabase"]["comment"], LN["Calm Play LLC"]["comment"],
               LN["Domino Delights player support"]["comment"], LN["Combo Fighter backend and auth stacks (AWS)"]["comment"],
               LN["layer.ai"]["comment"], IDS["notes_doc"], IDS["draft_sheet"]):
        return "claim met first"
    if t == "linear.linear_issues":
        return "cohort record"
    if t == "linear.linear_comments":
        return "connecting (the item's own note)"
    return "connecting"


A("## Record ledger")
A("")
A("One row per SQL statement (inserts and the three companion updates), in SQL order.")
A("")
A("| # | SQL line | Table | Id | Pointer | Manifest element | Carrier | Reach | Discovery role |")
A("|---|---|---|---|---|---|---|---|---|")


def pointer_of(x, rid):
    r, t = x.get("row") or {}, x["table"]
    if t == "linear.linear_comments":
        return r["issue_id"]
    if t in ("linear.linear_projects", "linear.linear_issues"):
        return r.get("identifier") or "team_ENG"
    if t.startswith("github."):
        return IDS["pr"]
    if t == "slack.slack_messages" and x["op"] == "update":
        return rid
    return rid
for n, x in enumerate(STM, 1):
    rid = rid_of(x)
    r = x.get("row") or {}
    el = set(ELEM.get(rid, set())) | set(ELEM.get(rid.split("#")[0], set())) | set(ELEM.get(str(r.get("thread_id")), set()))
    if x["table"] == "slack.slack_messages":
        el |= ELEM.get(f"{r.get('channel_id')}/{r.get('ts')}", set())
    els = " / ".join(sorted(el)) or "companion"
    A(f"| {n} | L{x['line']} | {x['table']}{' (UPDATE)' if x['op'] == 'update' else ''} | {rid} | {pointer_of(x, rid)} | {els} | {CARRIER.get(x['table'], '●')} | "
      f"{reach_of(x)} | {role_of(x, rid, el)} |")
A("")

# ======================================================================== findability
A("## Findability and discovery-order proofs")
A("")
FIND = [
    f"Hub (AN1) {SLOC['hub']} (row {SL['hub']}): Leonard → Robert, Thu Feb 12 21:40 PT; the prompt names it ('Leonard's DM'); the newest message in D04UP2L3E3S. First link.",
    f"Project (AN2) {IDS['project']} 'LLC take-over': named by the hub ('the LLC project in linear'); linear_list_projects returns it; its 37 issues by linear_list_issues (titles and states only; no comment text in bulk, Ask_Carriers §6b).",
    f"Ground rules H1 {IDS['ground_rules']}: the hub names 'the ground rules doc'; a Drive search for 'ground rules' or 'LLC' returns it and the older decoy {IDS['notes_doc']} ('LLC notes', Feb 10: 'DD and ZM both come with CF. Servers about $1k a month'), which differs on the take test and the hosting figure.",
    "Warehouse H2 snowflake ANALYTICS.MONETIZATION.REVENUE_DAILY: the ground rules name 'the warehouse's daily revenue table'; snowflake_list_tables shows REVENUE_DAILY (and REVENUE_DAILY_V2, same January sums); the decoy is BoomBit's campaign update C09SWTHEMEW/1770725775.479449 (retention and installs for its own test: decoy_scope issuer).",
    f"Split email H3 {GM['split_mail']} (thread {GT['split_mail']}): the hub says 'I'll email you how we split the money'; a mail search for 'LLC' or 'split' returns it; the competing hit is Leonard's January pro forma cap table C07C2866011/1768417784.194359 (equity, not the LLC's running cost).",
    f"T1 CORR: claim met first — #winddown C0ADGSZKR3R/1770680984.725779 (~$1k) and C0ADGSZKR3R/1770682219.100789 (300), the notes doc and draft ({IDS['notes_doc']}, {IDS['draft_sheet']}) and Leonard's issue note {LN['Domino Delights production account (AWS)']['comment']}; overturned by Arthur's DM reply {SLOC['arthur_dm']} (Feb 13 03:10Z, $140 from March) under the Feb 2 git-debugging root D04V95AAAHW/1770056235.480619: met first because #winddown is read by every run and the DM reply is threaded under an unrelated root; decisive because the costing rule takes 'what it bills now, going by whoever runs it' (Arthur runs the AWS accounts).",
    f"T2 AUTH: the take test (ground rules) needs January income per game; only REVENUE_DAILY gives it (DD 183.11, ZM 0.00); Slack offers 'We make way less than $1K' (C0ADGSZKR3R/1770686243.781429), which decides nothing against $140.",
    f"T3/T16 FILT: the campaign is in no list (not in the project, the checklist or the keep list); C09UHHN6PFZ/1770404445.795829 ($100/day, Feb 6) and C07C2866011/1770489896.754049 (both live, Feb 7) are met in channel history; Leonard's status {SLOC['vo_status']} (Feb 12, a reply under the Feb 6 root) says only the VO campaign is still on, $100/day capped at $3,000 a month on his card till the end of Feb, moving to 'our new company's card from March' (rev4: no record that carries the campaign uses the project word the rev3 run searched first); Robert's deck {IDS['cf_deck']} carries the same $100/day line.",
    f"T4 COMPLETE: claim met first — Leonard's #winddown action items C0ADGSZKR3R/1770933903.645709 (~$300 for Metabase and dbt) and his issue note {LN['Metabase']['comment']} ('about $300 a month with dbt, more or less'); Arthur's #winddown line C0ADGSZKR3R/1770937232.664809 moves the payer; his mail {GM['arthur_mail']} (Feb 13 02:35Z) gives $248 carried through May; found by a mail search for any of the three tools.",
    f"T5 DONE: claim — Arthur's note {LN['Domino Delights player support']['comment']} ('done ... merged in #1917') and the merged PR {IDS['pr']}; overturned by the App Store notice {GM['asc_notice']} (Feb 13 07:30Z: the support option only opens an email draft and does nothing without a mail account — the support-email build's behaviour), tied to the support-email build by Jenkins {SLOC['builds_result']} (#218, 'Replace Helpshift with support email'); met first because the note sits on the issue and the notice among Robert's App Store mail. Rev4: the project description's Done rule ('Done if ... the LLC takes it and nothing is left to do on it') makes a missed notice flip ENG-2462 to Done instead of Todo with Arthur.",
    "Calm Play (control row; rev4 purged EXC, which the rev3 pre-check showed was never live): Leonard's note on ENG-2472 ('Calm Play could just be our LLC') is overruled by the ground rules' 'The LLC is the new one Blake and I are setting up for the three of us' and 'anything Harmony Games owns comes to it only through Sunset's sale'; C04UEQVDVB7/1701383740.580749 and C04UEQVDVB7/1703492127.063049 (2023: fully owned subsidiary) agree.",
    f"T7 DATE (rev4): Leonard's ENG-2454 note {LN['layer.ai']['comment']} says only 'cancelled it on the 11th', so the item reads as closed; C09UHHN6PFZ/1770837702.167889 (Feb 11: layer.ai access until March 3rd) and Leonard's reply under it {SLOC['layer_reply']} (Feb 12 19:15Z: '" + Q["layer_reply"].split("> ", 1)[1] + f"', the parent's thread fields updated) give the step and its owner; the card {IDS['trello_card']} keeps an item's own deadline (export by Mar 3) and the ground rules bring a game's art over. A Slack search for 'layer.ai' returns the post (the only Feb 2026 hit) and the thread. GitHub: the checklist C0ADGSZKR3R/1770933450.410449 (keep until the data is sold, then transfer).",
    f"T19 STACKS (rev4): claim met first — Arthur's ENG-2445 note {LN['Combo Fighter backend and auth stacks (AWS)']['comment']} (Feb 13 00:58Z: CF's own account about $95 a month on HG's AWS bill), read by every run that opens the issue comments; overturned by Arthur's email {GM['jenkins_mail']} (thread {GT['jenkins_mail']}, Feb 13 04:20Z, 'jenkins', to Robert, cc Leonard), second paragraph: he shut down the extra copy of CF's backend still running from the January redeploy, so CF's account bills $62 a month now. The costing rule takes what it bills now from whoever runs it. Found by a mail search for 'jenkins', 'backend', 'AWS' or Arthur's address, or by reading Robert's Feb 13 mail; its snippet covers only the first paragraph (the build boxes).",
    f"T10 split: the pro forma post C07C2866011/1768417784.194359 and the $25K post C07C2866011/1767730784.379929 are met by a 'split' or 'founders' search; the split email {GM['split_mail']} (Feb 13) is the rule.",
    f"T17 GitHub: C05KNDCHAAG/1770842137.835489 (Feb 11, repos to the LLC) is met first; the later checklist C0ADGSZKR3R/1770933450.410449 (Feb 12) keeps GitHub under HG until the data is sold (L13: dated claim).",
]
for f in FIND:
    A("- " + f)
A("")

# ======================================================================== self-validation
A("## Self-validation")
A("")
A("| QC category | Tool-enforced (result) | Manual (evidence) |")
A("|---|---|---|")
A(f"| Missing Universe Data | check-sql PASS (1.E) | every deciding fact persona-readable: {SLOC['arthur_dm']}, {GM['arthur_mail']}, {GM['asc_notice']}, {SLOC['vo_status']}, REVENUE_DAILY (unscoped), C04UEQVDVB7/1701383740.580749, C09UHHN6PFZ/1770837702.167889 |")
A(f"| Temporal Field | sql_lint 0 errors; base_check Check C PASS | text dates agree: the hub (Thu night) says 'my draft from Tuesday' = {IDS['draft_sheet']} (Tue Feb 10 10:30 PT) and 'Monday's call' = {EV_ROB} (Mon Feb 16); the deck (Feb 8) follows the campaign's creation (Feb 6); the project (23:24Z) and issues precede the card (23:42Z), which precedes the ground rules (23:46Z); the PR merges (21:10Z) before the build (21:40Z) and the store notice (Feb 13 07:30Z); every issue note follows its issue's created_at |")
A(f"| Cross-service Referential | base_check Check A PASS | one figure per item across services: $140 only in {SLOC['arthur_dm']}; $62 only in {LN['Combo Fighter backend and auth stacks (AWS)']['comment']}; $248 only in {GM['arthur_mail']} (fact_check --no-leak); #1917 in the note, the PR and the Jenkins change line |")
A("| Quantitative / Reconciliation | reply counters updated on D04V95AAAHW/1770056235.480619 and C09UHHN6PFZ/1770404397.819789 (reply_count 1, reply_users_count 1, latest_reply = the seeded ts) | $248 = 100 + 100 + 48 (Arthur's mail; base dbt receipt $100 leonard.hayes@harmonygames.co/1855983949220444975); $3,000 a month = the cap on $100/day in Leonard's status (C09UHHN6PFZ/1770404445.795829 for the daily budget); no total is seeded |")
A("| State / Lifecycle | the 37 issues are Backlog without stamps; the PR is closed + merged with merged and closed events | statuses agree with #winddown: cancelled Soundly, Cursor, CodeRabbit, Kapwing, Zapier, layer (C0ADGSZKR3R/1770839322.836779, C0ADGSZKR3R/1770937188.477219, C0ADGSZKR3R/1770936655.574079, C0ADGSZKR3R/1770933450.410449, C0ADGSZKR3R/1770837793.168589); kept Deel, Gusto, Intuit, Linear (C0ADGSZKR3R/1770933601.686309) |")
A("| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A); roster addresses in every seeded row; base tokens kept (usr_Robert I10, EMPLOYEE_0025_GITHUB_USERNAME I08) |")
A(f"| Semantic / Category | — | titles match content ({IDS['ground_rules']}, {IDS['trello_card']}, {IDS['project']}, {EV_ROB}); one name per item (the issue titles are the plan's item names) |")
A("| Other | — | voice per 1.C; no record states a decision, a total, a share or the plan |")
A("")

# ======================================================================== integrations
A("## Integrations and companions")
A("")
A("| Service | INT id | Companion | Decision |")
A("|---|---|---|---|")
A(f"| gcal | INT-11 | invitation mails | seeded for Robert ({GM['invite|' + ROB]}) and Arthur from Leonard, with all three calendar copies (R08 match) |")
A(f"| jenkins → slack | INT-06 | #builds job start + result posts | seeded as a pair for DD iOS Submission #218 ({SLOC['builds_start']}, {SLOC['builds_result']}); base builds continue to Feb 12 |")
A(f"| app store connect → gmail | INT-08 | review mail | the seeded notice {GM['asc_notice']} is itself the INT-08 family ('We noticed an issue with your submission.') |")
A(f"| github → slack | INT-01, INT-02, INT-20 | GitHub app mirror / push posts | none: the GameOfDominoes mirror window ends 2025-12-26 (integrations.json); declared in integration_exceptions for {IDS['pr']} |")
A(f"| github → gmail | INT-12 | notification mails | none (optional companion; Arthur opened and merged #1917 himself); declared |")
A("| coderabbit → github | INT-23 | CodeRabbit summary comment | none on #1917 (optional; CodeRabbit cancelled Feb 12 22:50Z, C0ADGSZKR3R/1770936655.574079); declared |")
A("| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment / Slack DM / digests | none: #1917 names no Linear key; the workspace went to guests Feb 11 (C09UHHN6PFZ/1770842566.250369) |")
A(f"| gdrive | INT-13 | Drive Slack-app share DM | none for {IDS['ground_rules']}, {IDS['notes_doc']}, {IDS['draft_sheet']}, {IDS['cf_deck']}; declared |")
A("| slack | INT-22 | Slack e-mail notifications | none (DMs between full members; no base notification mail for D04UP2L3E3S or D04V95AAAHW in Feb) |")
A(f"| trello | INT-21 | no Trello→Slack integration | none (the card {IDS['trello_card']} posts nowhere) |")
A("| gdocs, gsheets, gslides | none | Drive rows mirror every native file (owner, shared_with) | seeded |")
A("")

# ======================================================================== touched-data census
A("## Touched-data census and coherence hazards")
A("")
A(f"Touched data: the hub DM D04UP2L3E3S (Feb 12–13); Robert's DM with Arthur D04V95AAAHW (root D04V95AAAHW/1770056235.480619, counters updated); #prototype C09UHHN6PFZ (Feb 6–12: C09UHHN6PFZ/1770404397.819789 counters updated, C09UHHN6PFZ/1770404445.795829, C09UHHN6PFZ/1770837702.167889, C09UHHN6PFZ/1770842566.250369, C09UHHN6PFZ/1770845002.610529, C09UHHN6PFZ/1770844309.583109); "
  "#winddown C0ADGSZKR3R (Feb 9–12, every line a correct run reads: checklist, keep list, action items, cancellations); #executives C07C2866011 (Jan 6, Jan 14, Feb 3–11); #admin_foundersonly C04UEQVDVB7 (2023 Calm Play posts); #builds C05433XK267 (Jan 28 #216/#217, Feb 12); #boombit C09SWTHEMEW (Feb 10–13); "
  f"Robert's mailbox (the three seeded threads, the invitation, base App Store mail threads/00014520.json); the four Drive files; the founders' board 640643a3fd8f3ca308d9318e; the project and ENG-2438…ENG-2474; GameOfDominoes (#1916, branches/981, #1917); snowflake REVENUE_DAILY / REVENUE_DAILY_V2; confluence page_aws_infra; Arthur's mailbox only for the cross-check of Kapwing (blake@harmonygames.co_1856962040028188034.json) and the GitHub receipts.")
A("")
A("Hazards from coherence_hazards.json (normal KB):")
A("- temporal: T07 — no seeded #prototype message is dated Feb 13 (the status is Feb 12 23:20Z; rev4's layer.ai reply Feb 12 19:15Z, after the channel's last base message that day, /726 at 19:08Z) and none points at a missing artifact; T06 — the card's dateLastActivity equals its only action (createCard, Feb 12 23:42Z); T02 none in scope — every seeded mail thread has one message.")
A("- semantic: S04 — Arthur's GitHub login is the base token, no display name is written; S06 none in scope — no contact is created or edited.")
A("- referential: R04 — the hub names the docs in words, no Drive link (Google-native link ids never equal f_ ids); R07 — no PR comment is seeded on #1917, whose repo's mirror window ended Dec 26; R08 — the seeded invitation mails have their three calendar rows.")
A("- quantitative: Q01/Q02/Q03 — all three seeded thread replies update their roots' reply_count, reply_users_count and latest_reply (rev4 adds Leonard's layer.ai post bdb4f7af824ec3819acdf5fc3cc480ea); Q07 — the AWS figures quoted different ways (~$1k vs others) are the older versions of T1, overturned by Arthur's dated $140, and (rev4) CF's ~$95 on ENG-2445 is the older version of T19, overturned by Arthur's dated $62 (no base record states a CF account figure; base deploy notes D04UY3DQJE5 2026-01 show the CF backend on us-west-1 and then us-east-1); Q09 — REVENUE_DAILY and REVENUE_DAILY_V2 agree on the January sums (DD 183.11, CF 7.36, ZM 0.00); Q10/Q11 — the mailbox copies and calendar copies of each seeded message/event are identical.")
A("- state/lifecycle: L13 — C05KNDCHAAG/1770842137.835489 is cited only as a dated claim (hazard_acknowledgements L13 dated_claim) and the SQL modifies no L13 record; L08 none in scope — the seeded issues are unassigned; L09 — #1917 is merged without a review, like base GameOfDominoes merges (e.g. #1916's only review event has an empty actor, /timeline_events/4724).")
A("- identifier/format: I02 — every seeded Slack id is sha256(channel|ts)[:32]; I03 — Arthur's base thread files use the blake@ alias and every seeded row uses arthur.blake@harmonygames.co; I08/I10 — base tokens EMPLOYEE_0025_GITHUB_USERNAME and usr_Robert are kept; I16 — the Trello ids encode their action time (698e6728 = 2026-02-12T23:50Z).")
A("")
A("Known data issues (references/known_data_issues/normal.md, read for every touched record; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):")
NB = [
    ("NB-1", "only full members (Leonard, Robert, Arthur) post in #prototype and #winddown after Feb 11 20:40Z (rev4's layer.ai reply is Leonard's); nothing grades channel access"),
    ("NB-2", "no AWS or hosting figure comes from the P&L sheet or the ledger: DD's $140 and CF's $95 / $62 are Arthur's own statements about his accounts"),
    ("NB-5", "Helpshift's Feb 28 comes from Leonard's line C0ADGSZKR3R/1770789534.434749, never from the vendor's acknowledgement date"),
    ("NB-6", "every seeded Slack row is before Feb 13 10:03Z (latest: the hub at 05:40Z); BoomBit's stop C09SWTHEMEW/1770977006.104929 (10:03Z) is cited only as context"),
    ("NB-8", "no Helpshift payment count is used"),
    ("NB-9", "Combo Fighter's Android status is never graded"),
    ("NB-11", "the CF GDD is not used for ads or status"),
    ("NB-12", "dbt ([USERNAME_30019]) and Kapwing ([PERSON_NAME_20852]) are graded only from records that spell them out (Arthur's mail, his Kapwing note, the checklist)"),
    ("NB-13", "no branch name is graded (Jenkins 'Blake/boombitWithEcon' vs GitHub 'arthur.blake/boombitWithEcon')"),
    ("NB-15", "pay is out of scope by the ground rules ('Pay for anyone who stays on is a separate conversation')"),
    ("NB-16", "Arthur's DM names no database engine"),
    ("NB-19", "the Unity Ads balance comes from Leonard's line C09UHHN6PFZ/1770845002.610529, not AD_SPEND_DAILY"),
    ("NB-21", "no review version is joined to a build number"),
    ("NB-24", "every Linear comment the task relies on is seeded"),
    ("NB-26", "Combo Fighter's sales are not graded (its $7.36 January income only enters the AUTH over-application operator)"),
    ("NB-29", "no time window starts at the shutdown decision"),
    ("NB-31", "reach in the DMs is argued from the two founders' membership, never graded"),
]
for k, v in NB:
    A(f"- {k}: {v}.")
A("")

# ======================================================================== intended disagreements
A("## Intended disagreements")
A("")
A("| Claim met first | Overturning record | Why realistic | Resolution |")
A("|---|---|---|---|")
DIS = [
    (f"DD's production account ~$1k (C0ADGSZKR3R/1770680984.725779), 'easy to get to 300' (C0ADGSZKR3R/1770682219.100789), repeated in {LN['Domino Delights production account (AWS)']['comment']}, {IDS['notes_doc']}, {IDS['draft_sheet']}",
     f"Arthur's DM reply {SLOC['arthur_dm']} (Feb 13 03:10Z): down to $140 a month, what it bills from March", "the engineer trims the account and tells his co-founder in their DM", "DD hosting $140; DD passes the take test"),
    (f"Metabase + dbt ~$300 (C0ADGSZKR3R/1770933903.645709; {LN['Metabase']['comment']})", f"Arthur's mail {GM['arthur_mail']} (Feb 13 02:35Z): $248 on his Kub card, carried through May", "he moved the billing the night before and says so by mail", "Founder rows; Arthur's cash = a third less $248"),
    (f"Arthur's 'done ... merged in #1917' ({LN['Domino Delights player support']['comment']}) and the merged PR {IDS['pr']}", f"the App Store notice {GM['asc_notice']} (Feb 13 07:30Z) on build #218 ({SLOC['builds_result']})", "a merge is not a release; review rejects the build", "the support build still has to ship before Feb 28"),
    (f"'Calm Play could just be our LLC' ({LN['Calm Play LLC']['comment']})", f"the ground rules {IDS['ground_rules']} ('The LLC is the new one ...'); C04UEQVDVB7/1701383740.580749, C04UEQVDVB7/1703492127.063049 (2023: fully owned subsidiary of Harmony Games)", "a founder floats an old entity before the rules are written", "Calm Play stays with HG and Sunset's sale (control row in rev4)"),
    (f"CF's own account about $95 a month (Arthur's ENG-2445 note {LN['Combo Fighter backend and auth stacks (AWS)']['comment']}, 00:58Z)", f"Arthur's email {GM['jenkins_mail']} (04:20Z): the extra backend copy shut down, $62 a month now", "the engineer trims a second account the same night and mentions it while reporting the Jenkins move", "CF stacks $62 (rev4, T19)"),
    (f"'cancelled it on the 11th' (Leonard's ENG-2454 note {LN['layer.ai']['comment']})", f"C09UHHN6PFZ/1770837702.167889 (access until March 3rd) and Leonard's reply {SLOC['layer_reply']} (CF's concept art is only in layer.ai; Robert to pull it out)", "a cancelled tool still holds the only copy of some art", "Robert exports the art by Mar 3 (rev4, T7)"),
    ("'I will keep both campaigns live' (C07C2866011/1770489896.754049)", f"Leonard's status {SLOC['vo_status']} (Feb 12): only the CF VO campaign is still on", "the install campaign is paused a week later", "one campaign, $3,000 a month cap, on the LLC from March"),
    (f"'DD and ZM both come with CF. Servers about $1k a month' ({IDS['notes_doc']}, Feb 10)", f"the ground rules {IDS['ground_rules']} (Feb 12 23:40Z): the take test; cost at what it bills now", "notes from Monday replaced by a rules doc two days later", "ZM stays with HG; DD comes over"),
    (f"Leonard's draft rows ({IDS['draft_sheet']}, Feb 10): DD servers ~1000, Metabase + dbt ~300, Figma LLC", f"the later notes: {SLOC['arthur_dm']}, {GM['arthur_mail']}, {LN['Figma']['comment']}", "a Tuesday draft kept only for its layout", "the layout is kept, the numbers are not"),
    ("C05KNDCHAAG/1770842137.835489 (Feb 11: repos to the LLC)", "C0ADGSZKR3R/1770933450.410449 (Feb 12: keep GitHub under HG until the data is sold, then transfer)", "the plan firms up after the data deal", "the GitHub transfer waits for the data sale"),
    ("the January funding posts C07C2866011/1767730784.379929 and C07C2866011/1768417784.194359", f"Leonard's split email {GM['split_mail']} (Feb 13)", "an old equity discussion vs the LLC's running-cost rule", "a third each, carried costs count toward it"),
]
for d in DIS:
    A("| " + " | ".join(d) + " |")
A("")

# ======================================================================== constraints for the prompt brief
A("## Constraints for the prompt brief")
A("")
A("| Anchor | May be named (noun phrases only) | Record |")
A("|---|---|---|")
A(f"| AN1 | Leonard's DM; Leonard's message from Thursday night | {SLOC['hub']} |")
A(f"| AN2 | the LLC project in Linear; the LLC take-over project | {IDS['project']} |")
A("")
A("Never name in the prompt: the ground rules' contents (the take test, the costing rule, the vehicle rule, the window, pay), the warehouse or REVENUE_DAILY, the split rule, the Trello card or its moving rule, Arthur's DM or mail, the App Store notice, the Jenkins build, PR #1917, the VO campaign, Calm Play, layer.ai or CF's art, the Jenkins email or CF's stacks figure, any item, figure, decision, date, owner, share or count. Deadlines: Robert's today is Sat Feb 14, 2026; the call is Mon Feb 16 (Leonard's 'we decide on Monday's call'). Deliverable kinds: one plan sheet in Robert's Drive laid out like Leonard's draft and shared with Leonard and Arthur; a call (comment) and a state on each project issue; a new issue for anything the project lacks; one reply in Leonard's DM thread with what Robert would do and what it costs each founder a month.")
A("")

# ======================================================================== fact sheet
A("## Fact sheet")
A("")
A("| Key | Value | Kind | Home / must appear in |")
A("|---|---|---|---|")
for f in MAN["facts"]:
    where = ", ".join((f.get("home_ids") or []) + (f.get("must_appear_in") or []))
    A(f"| {f['key']} | {f['value']} | {f['kind']} | {where} |")
A("")
A("Clause facts use the `status` kind (exact match); amounts use `amount`. Output verbatim:")
A("")
L.extend(fence(rd("fact_check.txt")))
A("")
cls = AGG["classes"]
A(f"Solver totals (`solver/truth.json`): {len(TRUTH)} items; LLC {cls.get('LLC')}, Founder {cls.get('Founder')}, HG {cls.get('HG')}; LLC cash "
  f"${TOT['llc_cash_per_month']:,} a month (DD hosting 140 + CF stacks 62 + VO campaign 3,000); carried by Arthur ${TOT['carried_per_month'].get('Arthur', 0):,} "
  f"(Metabase 100 + dbt 100 + GitHub 48); monthly cost ${TOT['total_per_month']:,}; a third ${TOT['third']:,.2f}; cash each month: Leonard "
  f"${TOT['cash_shares_per_month']['Leonard']:,.2f}, Robert ${TOT['cash_shares_per_month']['Robert']:,.2f}, Arthur ${TOT['cash_shares_per_month']['Arthur']:,.2f}; "
  f"over March–May the LLC's cash is ${TOT['llc_cash_window']:,}.")
A("")

# ======================================================================== facts for the human
A("## Facts for the human")
A("")
A("| Locator | Base/seeded | Fact | Reach | Role |")
A("|---|---|---|---|---|")
H = [
    (SL["hub"], "seeded", f"Leonard → Robert, 2026-02-13T05:40Z ({SLOC['hub']}): the ask (decide what the LLC takes if Sunset can't sell it, March–May cost, who pays; the ground rules; the sheet like his Tuesday draft in Robert's Drive shared with Blake and him; a call on each issue; the split by email; reply here; Monday's call)", "DM member", "authority (hub, anchor AN1)"),
    (IDS["ground_rules"], "seeded", f"Leonard, {T['ground_rules']}, 'LLC ground rules (Combo Fighter and whatever else we take)': vehicle rule (HG-owned things through Sunset's sale; services move their billing), window Mar 1–May 31, the take test (January income from the warehouse's daily revenue table covers what its own hosting bills now, whatever we said before; CF either way; a game brings its accounts and player support), costing rule (what it bills now, by whoever runs it), keep/cancel decisions in #winddown stay decided, pay out of scope; only monthly bills, no one-offs or yearly fees, moves on the LLC card", "shared with Robert", "authority H1"),
    (IDS["notes_doc"], "seeded", f"Leonard, {T['notes_doc']}, 'LLC notes (Monday)': Calm Play could hold it; DD and ZM come with CF; servers about $1k a month", "shared with Robert", "decoy (H1, older version)"),
    (IDS["draft_sheet"], "seeded", "Leonard, 2026-02-10T18:30Z, 'LLC 90 days (draft)': header Item · Game · Decision · Monthly cost · Paid by · Next step · Owner · By; rows CF, DD servers (~1000, Blake: maybe 300), Metabase + dbt (~300), Figma", "shared with Robert", "layout source; stale numbers (T8)"),
    (IDS["cf_deck"], "seeded", f"Robert, {T['cf_deck']}, 'Combo Fighter: next 90 days': run the VO campaign at $100/day (~$3k a month) through May; no playables beyond the one in production until D1 is over 35%", "Robert owns", "evidence (campaign rate)"),
    (IDS["trello_card"], "seeded", f"Leonard, {T['trello_card']}, 'LLC: what we take from HG' (founders' board, To Do): Robert makes the call; whoever runs an item moves it; through Sunset's sale → when the sale closes; own deadline keeps it; everything else by March 1", "unscoped", "authority (dates and owners)"),
    (IDS["project"], "seeded", f"Leonard, {T['project']}, Linear project 'LLC take-over' (team_ENG): one issue per thing the LLC might take from HG or pay for; comment the call; Done if a founder pays it himself through May (even if HG still owns it) or if the LLC takes it and nothing is left to do; Todo (assign the mover) if the LLC takes it and something is still to do; Canceled if it stays with HG (rev4 wording)", "unscoped", "first link (anchor AN2); DONE's state flip"),
    ("ENG-2438", "seeded", "ENG-2438…ENG-2474: 37 candidate issues in Backlog, created 2026-02-12T23:25–23:37Z, each with one owner note (2026-02-13T00:24–01:37Z)", "unscoped", "cohort"),
    (LN["Domino Delights production account (AWS)"]["comment"], "seeded", "Leonard on ENG-2441: 'about $1k a month, Blake thinks he can get it to $300'", "unscoped", "claim met first (T1)"),
    (SL["arthur_dm"], "seeded", f"Arthur → Robert, 2026-02-13T03:10Z ({SLOC['arthur_dm']}), reply under the Feb 2 root D04V95AAAHW/1770056235.480619: Domino's prod account is down to $140 a month, one small task and the db at its floor; that's what it bills from March", "DM member", "overturning (T1)"),
    (LN["Combo Fighter backend and auth stacks (AWS)"]["comment"], "seeded", "Arthur on ENG-2445 (00:58Z): CF's own account (its auth and backend stacks) runs about $95 a month on HG's AWS bill; CF no longer calls ZM's phoenix api", "unscoped", "claim met first (T19)"),
    (GM["jenkins_mail"], "seeded", f"Arthur → Robert, cc Leonard, 2026-02-13T04:20Z, 'jenkins' (thread {GT['jenkins_mail']}): the Jenkins jobs moved to his own machine, the build boxes are HG's; second paragraph: the extra copy of CF's backend shut down, CF's own account bills $62 a month now, still on HG's AWS bill till March", "Robert's INBOX", "overturning (T19)"),
    (LN["Zombie Match account (AWS)"]["comment"], "seeded", "Arthur on ENG-2443: ZM's account still runs phoenix, its nakama and the aurora cluster, nobody trimmed it; it bills every month on HG's AWS bill", "unscoped", "evidence (ZM hosting)"),
    ("snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY", "base", "January 2026 SUM(total_revenue_usd): domino_delights 183.11 (IAP 68.84 + ads 114.27), combo_fighter 7.36, zombie_match_3d 0.00 (186 rows); REVENUE_DAILY_V2 agrees", "unscoped", "authority H2"),
    ("confluence:page_aws_infra", "base", "AWS guide (Dec 31, 2025): DD dev/prod accounts, ZM one account, analytics account; Fargate (Phoenix + Nakama) ~$650/mo", "unscoped", "evidence (ZM hosting)"),
    (LN["Metabase"]["comment"], "seeded", "Leonard on ENG-2447: about $300 a month with dbt, more or less", "unscoped", "claim met first (T4)"),
    ("C0ADGSZKR3R/1770937232.664809", "base", "Arthur, Feb 12 23:00Z: moving github, dbt and Metabase to his KubLLC card", "#winddown member", "connecting (T4)"),
    (GM["arthur_mail"], "seeded", f"Arthur → Robert, Leonard, 2026-02-13T02:35Z, 'billing moved to my card' (thread {GT['arthur_mail']}): Metabase $100 base, dbt $100, GitHub $48 team plan now that copilot is off, $248 a month, carried through May as his part", "Robert's INBOX", "overturning (T4)"),
    (GM["split_mail"], "seeded", f"Leonard → Robert, cc Arthur, 2026-02-13T06:10Z, 'LLC money' (thread {GT['split_mail']}): each of the three carries a third of the LLC's monthly cost March–May; what one already pays counts toward his third; put the three shares on the sheet per month", "Robert's INBOX", "authority H3"),
    (SL["vo_status"], "seeded", f"Leonard, 2026-02-12T23:20Z ({SLOC['vo_status']}), reply under C09UHHN6PFZ/1770404397.819789: only the CF VO campaign is still on (install one paused), $100/day capped at $3,000 a month, on his card till the end of Feb, moving to 'our new company's card from March' (rev4: no 'LLC', no 'barely billing')", "#prototype member", "overturning (T16) · campaign (T3)"),
    ("C09UHHN6PFZ/1770404445.795829", "base", "Leonard, Feb 6: VO campaign budget $100/day", "#prototype member", "evidence (T3)"),
    (LN["Domino Delights player support"]["comment"], "seeded", "Arthur on ENG-2462: done, support goes to the email address and Helpshift is out of DD (merged in #1917)", "unscoped", "claim (T5)"),
    (IDS["pr"], "seeded", "Arthur's PR 'Replace Helpshift with support email', opened 2026-02-12T18:05Z, merged 21:10Z into arthur.blake/boombitWithEcon", "unscoped", "claim support (T5)"),
    (SL["builds_result"], "seeded", f"Jenkins, 2026-02-12T21:49:30Z ({SLOC['builds_result']}): DD iOS Submission #218 on Blake/boombitWithEcon succeeded; change 'Replace Helpshift with support email' (start post {SLOC['builds_start']} at 21:40Z)", "#builds member", "connecting (T5)"),
    (GM["asc_notice"], "seeded", f"App Store Review → Robert, 2026-02-13T07:30Z, 'We noticed an issue with your submission.' (thread {GT['asc_notice']}): Domino Delights, Guideline 1.5 — the support option only opens an email draft and does nothing on a device without a mail account; asks for a support URL or another in-app contact", "Robert's INBOX", "overturning (T5)"),
    ("C0ADGSZKR3R/1770789534.434749", "base", "Leonard, Feb 11: Helpshift cancels without a hassle; DD and ZM must be off it before Feb 28th", "#winddown member", "evidence (the support deadline)"),
    (LN["Calm Play LLC"]["comment"], "seeded", "Leonard on ENG-2472: 'Calm Play could just be our LLC, it already has the Singular org and its own Apple team'", "unscoped", "stale claim (control row; EXC purged in rev4)"),
    ("C04UEQVDVB7/1701383740.580749", "base", "Nov 30, 2023: Calm Play is an LLC fully owned by Harmony Games (also C04UEQVDVB7/1703492127.063049, Dec 25, 2023)", "#admin_foundersonly member", "agrees with the ground rules (control)"),
    (LN["layer.ai"]["comment"], "seeded", "Leonard on ENG-2454 (00:37Z): 'cancelled it on the 11th' (rev4: no art caveat)", "unscoped", "claim met first (T7)"),
    ("C09UHHN6PFZ/1770837702.167889", "base", "Leonard, Feb 11: layer.ai cancelled, access until March 3rd (tags EMPLOYEE_0033); rev4 updates its thread fields", "#prototype member", "evidence (T7)"),
    (SL["layer_reply"], "seeded", f"Leonard, 2026-02-12T19:15Z ({SLOC['layer_reply']}), reply under it: '" + Q["layer_reply"] + "'", "#prototype member", "overturning (T7)"),
    ("C0ADGSZKR3R/1770933450.410449", "base", "Leonard, Feb 12 21:57Z: the subscription checklist (github: keep until the data is sold, then transfer; Slack down to 3; Google archive Feb 15; Kapwing, cursor, coderabbit Blake's)", "#winddown member", "evidence (T7, T17, controls)"),
    ("C0ADGSZKR3R/1770933601.686309", "base", "Leonard, Feb 12 22:00Z: keep Deel, Gusto, Intuit; Figma can't charge before renewal; Linear kept during transition", "#winddown member", "evidence (controls)"),
    (EV_ROB, "seeded", "Mon 2026-02-16 18:00–18:45Z 'LLC: decide' (Leonard organizer; Robert and Arthur invited; created 2026-02-13T05:45Z), Robert's copy", "Robert's calendar (self)", "destination (K11)"),
    (GM["invite|" + ROB], "seeded", "INT-11 invitation for the Monday call", "Robert's INBOX", "companion"),
]
for h in H:
    A("| " + " | ".join(h) + " |")
A("")

# ======================================================================== platform review of rev1
A("## Platform /injection review of rev1 and the rev2 changes")
A("")
A("rev1 (SQL sha256 7573eb1a6bca, attempt 6adfee3b47f7621feba5b96c) passed `injection-static-v2` with Checks A, B and C PASS and no demonstrated "
  "defect (`run_forensics/rev1/0_injection_PASS_r1.md`). Its advisories and what rev2 does with each:")
A(f"- A-1 (cosmetic): zero-length style run on the notes doc {IDS['notes_doc']}. Fixed in rev2: the doc is titled 'LLC notes (Monday)' and the note is its body (the one-line note had become a 155-character title).")
A("- A-2: branch arthur.blake/boombitWithEcon keeps its head after the #1917 merge; base-consistent (R05, base heads are not advanced). Kept.")
A(f"- A-3 (realism): Arthur's $140 reply {SLOC['arthur_dm']} sits under an unrelated Feb 2 root. Kept: it is the CORR trap's designed placement (thread-reply hiding).")
A(f"- A-4/A-5/A-6 (for /prompt): the App Store rejection {GM['asc_notice']} as the only reading of the support item; Calm Play's 'could' note against the ground rules {IDS['ground_rules']}; ZM's 'well over $1k a month' (rev2: 'it bills every month', no figure) against $0.00 January income. Each is settled by a later dated record and was re-tested by the second blind fork sweep (plan/sweep_dispositions.md).")
A("- A-7 (NB-13): no exact branch name is graded.")
A("")
A("rev2 (SQL sha256 edf1fd903611, the same attempt) passed `injection-static-v2` again with Checks A, B and C PASS and no demonstrated defect "
  "(`run_forensics/rev2/0_injection_PASS_r2.md`): A-1 resolved, A-2/A-3/A-5/A-7 reused, A-4 clearer (the rejection names the email-only support "
  "that #1917 shipped). Updated A-6: no injected record states ZM's hosting figure. The take-test call does not depend on it: ENG-2443 says the account "
  "bills every month, and ZM's January income in snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY is 0.00, so no bill is covered (for the prompt brief). "
  "The platform changelog export (`task_inputs/02_Changelog.json`) shows all 131 rev2 statements applied (129 INSERT, 2 UPDATE) with the rev2 wording.")
A("")
A("## Platform /prompt review of rev2 and the rev3 changes")
A("")
A("rev2 passed `injection-static-v2` a third time (`run_forensics/rev2/0_injection_PASS_r2_resubmit.md`), but the paired `/prompt` review "
  "(`run_forensics/rev2/1_prompt_FAIL_r2.md`, prompt sha256 ccd229a59a17) scored Unique Ground Truth and Clarity 2 and every other dimension 5. "
  "Dataset similarity passed (nearest 0.776, same scenario). Its decision sweep settled 35 of the 37 issues by record and matched solver/truth.json "
  "on every call, cost and share; three Linear writes had no settling record. rev3 settles each one with a dated record and leaves the prompt unchanged:")
A(f"- F1 (a new issue for the VO campaign): the project description said 'One issue per thing the LLC might take from HG', and the campaign is on Leonard's card, not HG's. rev3: the project {IDS['project']} reads 'One issue per thing the LLC might take from HG or pay for'. The LLC pays the campaign from March ({SLOC['vo_status']}), so the plan row needs an issue and the prompt's 'the project should match the sheet' asks for it.")
A(f"- F2 (ENG-2451 AppsFlyer assignee): the card's 'Whoever runs an item today moves it' named nobody for a new service. rev3: Leonard's note ends 'I'll set CF up on it', so the issue is assigned to Leonard.")
A(f"- F3 (ENG-2452 Google Analytics state): Arthur's mail said CF's BigQuery/Firebase 'are on the free tier' once the data is out, which read as a later move to the LLC. rev3: Leonard's note reads 'stays under HG until the data is extracted, nothing for the LLC to take or pay', and Arthur's mail {GM['arthur_mail']} says they 'cost nothing after that, so there's nothing there for the LLC'. The issue is Canceled.")
A("- Optional realism note (Eval 0 A-3, not scored): Arthur's $140 reply stays threaded under the Feb 2 root, the CORR trap's designed placement.")
A("A third blind fork sweep on the rev3 records (fresh agent, no answer key) reproduced the plan, the totals and every Linear write, and F1–F3 came back settled. Two readings it left open are settled in rev3 too: Arthur's ENG-2446 note adds 'so the LLC doesn't need them' (the build boxes, even if Sunset can't sell them), and Leonard's Helpshift note adds 'CF was never on it, its support is the contact on its store listing and that moves with the game' (no separate CF player-support line). The rest were already settled by records (plan/sweep_dispositions.md).")
A("")
A("## Platform /hardness review of rev3 and the rev4 changes")
A("")
A("rev3 passed `/injection` and `/prompt` (every dimension 5), but `/hardness` scored 2 (FAIL, too easy; `run_forensics/rev3/precheck/1a_hardness_FAIL_r3.md`). "
  "One platform Opus 5.5 run (168 counted calls) got about 96 % right. `/create-hardening` MODE B (`Working_Files/01a_Hardening_Report.md`) found these causes:")
A("- DONE landed but changed only wording: the store notice was fetched as a snippet.")
A("- DATE landed but was minor: the layer.ai date was never seen.")
A("- CORR, AUTH, FILT and COMPLETE leaked:")
A("  - the campaign record carried the project word the run searched first;")
A("  - the ground rules pointed the run to the owner and to the table;")
A("  - a base lead led to Arthur's mail.")
A("- EXC was never live.")
A("`/create-scenario --revise` (design-2, gate PASS) chose four Hardness v2 moves and one purge. This revision implements them and leaves the truth and the prompt unchanged:")
A(f"- RB1 (FILT): Leonard's status {SLOC['vo_status']} drops 'LLC' and 'barely billing': the campaign 'moves to our new company's card from March', 'so count it as its own line in what we pay each month'.")
A(f"- RB2 (DONE): the project description {IDS['project']} tests Done first, 'if one of us pays it himself through May (even if HG still owns it) or if the LLC takes it and nothing is left to do on it'. A missed store notice now flips ENG-2462 to Done instead of Todo with Arthur.")
A(f"- RB4 (DATE): ENG-2454's note is only 'cancelled it on the 11th'. The art and its owner move into Leonard's reply {SLOC['layer_reply']} under the base access-date post, with the parent's thread fields updated.")
A(f"- RB5 (STACKS, new): ENG-2445's note gives Arthur's ~$95 before his trim. His later email {GM['jenkins_mail']} ('jenkins', 04:20Z) says in its second paragraph that CF's account bills $62 now.")
A("- EXC purged: Calm Play is a control row decided by the ground rules. Dropping their vehicle sentence would have reopened a /prompt fork.")
A("")
A("Independent reviews before sealing:")
A("- An hg.py-only fallback red team of the design delta (`Working_Files/01b_Redteam_Fallback_rev4.md`) found four majors, all fixed before this SQL: the campaign's payer and state, GitHub Done vs Canceled, and 'barely billing' vs 'bills now'.")
A("- A blind fork sweep of the rev4 records is in 'Blind sweeps' below.")
A("")
# ======================================================================== platform follow-ups
A("## Platform follow-ups")
A("")
A(f"- ○ carriers: the Monday event's description ('{Q['monday_desc']}') is supporting only; nothing graded rests on it. Linear comments are ● (§6b), so no follow-up is needed for the 37 notes.")
A("- Snowflake and Confluence figures (REVENUE_DAILY January sums; the AWS guide's cost note) are re-verified after any data regeneration (`plan/run_checks.sh`, solver JAN_INCOME / ZM_HOSTING).")
A("- No call_budget row depends on an unverified behaviour.")
A("")

# ======================================================================== self-review
A("## Self-review")
A("")
A("### Tool outputs (final SQL, verbatim)")
A("")
A("`sql_lint.py`:")
L.extend(fence(rd("sql_lint.txt")))
A("sql_lint warning disposition (clock class, 6 warnings): the three copies of the Monday call start and end on Feb 16, after the clock — a not-yet-happened event (a deadline-type plan field, GEN_EXECUTION §0a), allowed.")
A("")
A("`hg.py lint` (the eval's hg_injection_lint, with base data):")
_hl = json.loads(rd("hg_lint.json")[rd("hg_lint.json").index("{"):])
L.extend(fence(f"hg_injection_lint (base data): counts {_hl.get('counts')}; flags: {len(_hl.get('flags') or [])}; info: {len(_hl.get('info') or [])}"))
A("LINT: counts FAIL 0, CHECK 0, INFO 0 — no CHECK to disposition (the earlier grader_language CHECK on the project description's 'Todo when' wording was fixed by rewording, see design_delta).")
A("")
A("`base_check.py`:")
L.extend(fence(rd("base_check.txt")))
A("`base_claims.py`:")
L.extend(fence(rd("base_claims.txt")))
A("`hardness_gate.py` (final manifest + SQL):")
L.extend(fence(rd("hardness_gate.txt")))
A("")
A("### Preflight (S4b–S5e)")
A("")
A("`oracle_kit.py check`:")
L.extend(fence(rd("oracle_kit.txt")))
A("`difficulty_mutation.py mutate` (tail) and `geometry`:")
mt = rd("mutation.txt").splitlines()
L.extend(fence("\n".join(mt[-40:])))
L.extend(fence(rd("geometry.txt")))
A("`trap_liveness.py` (SQL):")
L.extend(fence(rd("trap_liveness_sql.txt")))
A("`hardness_forecast.py forecast --preregister` (tail) and `preflight_report.py`:")
L.extend(fence("\n".join(rd("forecast.txt").splitlines()[-12:]).replace("[]", "(none)")))
L.extend(fence(rd("preflight.txt").replace("[]", "(none)")))
import re as _re
_fid = (_re.search(r"'id': '(hev_[0-9a-f]+)'", rd("forecast.txt")) or [None, "(not recorded)"])[1]
A(f"Forecast (UNCALIBRATED, advisory), two views.")
A(f"- Solver-based, exact: pre-registered for rev4 as {_fid}. Earlier records: rev3 hev_61e8a1a72c32da82, rev3 posterior after the pre-check hev_51611d00e3779d1d, rev2 hev_7365758e94d10201, rev1 hev_c47baade19a93a88. "
  "Its tail is above. It never fails write-content slots (51 of the 77 weight points: the plan and reply text and the new issue), so only the direct slots move.")
A("- Design view (plan/policy_scores.txt; design forecast hev_c2e614ebc388cb63): E[avg] is 64.4 % at the rev4 design rates (rho 0.30) and 84.4 % at 0.4x those rates. "
  "P(one run catches every trap) is about 0.035, and no pair of misses stays at or above 85 %.")
A("- Channel rates come from Opus 5.5 ledger records of each family, except CH-DATE: its family has one verdict record (hev_3d96146a0a8b19a5, the rev3 pre-check), so it carries a disclosed design rate of 0.55 (plan/policy_scores.py). CH-EXC is gone.")
A("")
A("Every mutation result, channel degrade, intervention and liveness flag has a written disposition in `Working_Files/01c_Dispositions.json`. "
  "preflight {report, digest} is not written back into the final manifest: the report binds the manifest by sha256, so writing its digest there "
  "would make the report stale (the archived bridge and Q4 tasks did the same).")
A("")
A("### Changes made at this stage (and why)")
A("")
for d in MAN.get("design_delta", []):
    A(f"- {d['id']}: {d['change']} — {d['reason']}")
A("- Earlier (rev1): scenario re-certified before this stage closed: surface V1 gained COMPLETE and EXC (the solver showed both move the LLC row count), controls and over-application operators became exact solver keys, channels became solver-shaped (scale, ch_miss), and the native wording (App Store template, deck line, project description, Jenkins texts) moved into the scenario builder; `stage_gate.py scenario` PASS re-pasted.")
A("")
A("### /injection Checks A–C walk")
A("")
A(f"- Inventory: {n_ins} INSERT, {n_upd} UPDATE (the three root counter updates), no DELETE, no upsert; every statement in the record ledger.")
A("- Check A (references, uniqueness, identities, id contracts): PASS — base_check Check A; every parent resolves (Slack roots bc4bc3d0e2a0ea6ae92cb2a9712e8f76, 73ec270a3d07eb8d8488384898be079e and bdb4f7af824ec3819acdf5fc3cc480ea, Drive roots d_63fffeb4fab5233ed5bb73 and d_9f7ba94f7526d54d8482ba, board 640643a3fd8f3ca308d9318e and list 640643a3fd8f3ca308d93195, team_ENG, Linear users usr_63fffeb4fab5233e / usr_Robert / usr_cc3e90160f490686, repo harmonygames-Games/GameOfDominoes, branch arthur.blake/boombitWithEcon); ids unique over full collections (1.F); one account per person per service.")
A("- Check B (structure, literal JSON, generated / NOT NULL columns): PASS — sql_lint 0 errors; no text_fts / body_text_fts; every *_json column holds literal JSON; Linear dates YYYY-MM-DDTHH:MM:SSZ; state_history_json an empty JSON array.")
A("- Check C (dates, parent/reply, statuses, counts, claimed updates, superseding records): PASS — base_check Check C; every seeded event before the seed bound except the Monday call (plan field); replies after their roots; issue notes after their issues; PR opened < merged < build < notice; superseding records are later than what they supersede (version_records sorted, hardness_gate PASS).")
A("")
A("### Touched-data census")
A("")
A("The census and its hazard dispositions are in 'Touched-data census and coherence hazards' above (all six categories; L13 acknowledged as dated_claim; 16 NB cards dispositioned).")
A("")
A("### Counter-readings")
A("")
A("| Category | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |")
A("|---|---|---|---|")
CR = [
    ("Temporal", "the hub cites 'my draft from Tuesday' and 'Monday's call', which could be the wrong days", f"draft {IDS['draft_sheet']} created Tue Feb 10 18:30Z; event {EV_ROB} Mon Feb 16 18:00Z, created Feb 13 05:45Z before the hub's split mail", "PASS"),
    ("Temporal", "the ground rules point at the Trello card and the card at the Linear project, which could postdate them", f"project {T['project']}, issues from {T['issue0']}, card {T['trello_card']}, ground rules {T['ground_rules']} (each after what it cites)", "PASS"),
    ("Temporal", "Robert's deck could predate the VO campaign it budgets", f"deck {IDS['cf_deck']} {T['cf_deck']}, after the campaign's creation C09UHHN6PFZ/1770404397.819789 (Feb 6) and Leonard's 'keep both campaigns live' C07C2866011/1770489896.754049", "PASS"),
    ("Temporal", "the App Store notice could be about the 19:56Z BoomBit build, not the support build", f"#218 starts 21:40Z after the merge (21:10Z) and its change line is the support change ({SLOC['builds_result']}); BoomBit's build C09SWTHEMEW/1770926214.816149 is about interstitials", "PASS"),
    ("Semantic / Category", "'Kub card' vs 'KubLLC card' could read as two cards", "C0ADGSZKR3R/1770937232.664809 ('my KubLLC card') and the mail's 'my Kub card' are the same author and payer", "PASS (short form)"),
    ("Semantic / Category", "'the warehouse's daily revenue table' could mean REVENUE_DAILY_V2 or AD_REVENUE", "snowflake /tables/12 vs /tables/13 give the same January sums; netting Apple's 30 % on IAP still leaves $162.46 > $140", "PASS"),
    ("Cross-service Referential", "the GitHub branch name differs between Jenkins and GitHub", "NB-13 pattern (C05433XK267 2026-01 /1237 vs github /branches/981); no branch is graded", "PASS (pre-existing, not graded)"),
    ("Cross-service Referential", "Arthur's $48 GitHub plan disagrees with base receipts of $86", "base receipts include Copilot $38; the mail says 'now that copilot is off' (gmail blake@harmonygames.co GitHub receipts)", "PASS"),
    ("Cross-service Referential", "Arthur's $48 GitHub plan disagrees with the Feb 3 receipt ($52 Team Plan + $38 Copilot)", "gmail threads/blake@harmonygames.co_1856132203079406675.json; the mail says 'back to the $48 team plan now that I dropped the extra seat and copilot is off' (Jan 3 receipt: $48)", "PASS"),
    ("Cross-service Referential", "Combo Fighter's client calls ZM's Phoenix API, so ZM's account staying with HG breaks CF", "confluence /pages/8 (Dec 31, 2025); Arthur's ENG-2445 note (Feb 13): CF's own account (auth and backend stacks; D04UY3DQJE5 2026-01 deploy notes; the note does not name Nakama, which Confluence says CF doesn't use) and 'CF stopped calling ZM's phoenix api'", "PASS"),
    ("Semantic / Category", "'VO campaign' could be read as a video campaign, or Leonard's status could ignore the Unity playable test", "VO = event/value optimization (C09UHHN6PFZ/1770404397.819789, C07C2866011/1770438169.228649); the status names only the Meta campaigns and says the Unity test uses up the $100 left there (C09UHHN6PFZ/1770845845.148039)", "PASS"),
    ("Quantitative", "the ZM hosting has no exact figure, so '$0 covers $0' could keep ZM", "Arthur's ENG-2443 note: phoenix, nakama and aurora untrimmed, billing every month on HG's AWS bill (HG's whole AWS line is $1,485 in Jan and Feb 2026, snowflake.FINANCE.EXPENSES.MONTHLY_BURN); any bill exceeds the 0.00 January income", "PASS"),
    ("Quantitative", "two live campaigns would make the line ~$6k", f"C07C2866011/1770489896.754049 is superseded by {SLOC['vo_status']} (only the VO campaign)", "PASS"),
    ("State / Lifecycle", "Kapwing 'cancelled' has no Robert-visible record (the checklist shows [-])", f"Arthur's note {LN['Kapwing']['comment']} matches Kapwing's notice blake@harmonygames.co_1856962040028188034.json (Feb 12 22:56Z) and C0ADGSZKR3R/1770937188.477219", "PASS"),
    ("State / Lifecycle", "the analytics pipeline being turned off conflicts with keeping Metabase for CF data", "CF's events go through Firebase (C07C2866011/1770298939.402129: 'the default in_app_purchase sent by Firebase'); the Firebase/BigQuery/dbt/Metabase stack (C04UEQVDVB7/1706816838.694319) is separate from the Kinesis/Glue account (page_aws_infra)", "PASS"),
    ("State / Lifecycle", "#1917 merged after the Feb 9 shutdown decision reads as work after the announcement (L13)", "hazard_acknowledgements L13 dated_claim; base Combo-Fighters#37 merges Feb 13; the support move is part of the wind-down (C0ADGSZKR3R/1770789534.434749)", "PASS"),
    ("Identifier / Format", "a hand-typed address or a changed id scheme", "eval lint FAIL 0 CHECK 0; sql_lint 0 errors; roster emails only; ids per 1.A; collisions 0 (1.F)", "PASS"),
    ("Identifier / Format", "usr_Robert breaks the usr_<16hex> scheme", "base Linear user id, I10 (linear data.json /users)", "PASS (pre-existing)"),
    ("People status", "Leonard or Arthur act after leaving channels (NB-1)", "both stay full members (C0ADGSZKR3R/1770842402.772039 'keep maybe the three of us'); activity.json active_feb_2026", "PASS"),
    ("Other", "a designed disagreement reads as two silent system fields", "each overturning record is a dated human message or a vendor notice (T1, T4, T5, T6, T16 in Intended disagreements)", "PASS"),
    ("Other (designed T1)", "best argument the $1k/$140 clash is an unintended inconsistency", f"Arthur's later DM {SLOC['arthur_dm']} says the account was trimmed ('down to $140 … one small task and the db at its floor'), after his own Feb 10 'I think I can get the cost down' (C0ADGSZKR3R/1770682200.870289)", "designed"),
    ("Other (designed T4)", "best argument the ~$300 vs $248 clash is unintended", f"Arthur's mail {GM['arthur_mail']} explains the drop (extra Metabase seats removed, Copilot off)", "designed"),
    ("Other (designed T5)", "best argument the done note vs the rejection is unintended", f"the rejection {GM['asc_notice']} is later and describes the email-draft support option that only the #218 build has; Jenkins #218 ties it to the change", "designed"),
    ("Other (control, rev4)", "best argument the Calm Play note is a fact, not a mistake, now that EXC is purged", f"the ground rules {IDS['ground_rules']} name 'the new one Blake and I are setting up'; C04UEQVDVB7/1701383740.580749 and C04UEQVDVB7/1703492127.063049 are explicit founders' records; the note says 'could', a suggestion", "PASS"),
    ("Temporal (rev4)", "the layer.ai reply could predate its root or show Robert ignoring a mention", f"{SLOC['layer_reply']} is Feb 12 19:15Z, a day after the root C09UHHN6PFZ/1770837702.167889 and after the channel's last base message that day (C09UHHN6PFZ 2026-02 /726, 19:08Z); the root's thread fields are updated", "PASS"),
    ("Temporal (rev4)", "the Jenkins email could contradict Arthur's own ENG-2446 note", f"the note (01:07Z) says he will move the jobs; the email {GM['jenkins_mail']} (04:20Z, 11:20pm ET) says he moved them 'tonight'; both say the boxes are HG's", "PASS"),
    ("Quantitative (rev4, designed T19)", "best argument $95 vs $62 is an unintended inconsistency", f"the same owner's later email {GM['jenkins_mail']} says why: the extra copy of CF's backend from the January redeploy was shut down; base deploy notes D04UY3DQJE5 2026-01 /18-/26 show two backend endpoints (us-west-1, then us-east-1)", "designed"),
    ("Semantic / Category (rev4)", "'our new company's card' could mean Sunset or Arthur's KubLLC", f"the ground rules {IDS['ground_rules']} call the LLC 'the new one Blake and I are setting up for the three of us'; Leonard's status {SLOC['vo_status']} says the campaign is on his card only till the end of Feb", "PASS"),
    ("State / Lifecycle (rev4)", "the new Done rule could make GitHub Canceled (HG owns the org) or the campaign Done (on Leonard's card)", f"the rule tests Done first and says 'pays it himself through May (even if HG still owns it)'; Arthur carries GitHub through May ({GM['arthur_mail']}); the campaign leaves Leonard's card in March ({SLOC['vo_status']}); red team RT4-2, RT4-4", "PASS"),
    ("Other (designed T7, rev4)", "best argument the art-export step is hidden, not discoverable", f"the reply {SLOC['layer_reply']} names 'layer.ai', @-mentions Robert and sits under the item's own access-date post (the only Feb 2026 'layer.ai' hit); the ground rules bring a game's art over", "designed"),
    ("Other (designed T16)", "best argument 'both campaigns' still holds", f"{SLOC['vo_status']} is five days later and says the install one is paused", "designed"),
    ("Other (designed notes/draft)", "best argument the notes doc or draft is the authority", f"the hub names 'the ground rules doc' and only the draft's layout; {IDS['ground_rules']} is two days newer", "designed"),
    ("Other (designed T17)", "best argument the repos move to the LLC now", "C0ADGSZKR3R/1770933450.410449 (a day later) keeps GitHub under HG until the data is sold", "designed"),
    ("Other (designed T10)", "best argument the January funding posts set the split", f"they are about equity before the shutdown; the split mail {GM['split_mail']} is the LLC's rule", "designed"),
]
for c in CR:
    A("| " + " | ".join(c) + " |")
A("")
A("Lazy-solver pass on the implemented records (first hits, no threads, bulk shortcuts, stop at the first conclusion): it reads the hub, "
  "#winddown and the project's issue list and notes; takes DD's hosting from the issue note (~$1k / $300, so DD fails the take test), Metabase + dbt "
  "at ~$300 as LLC cash, CF's stacks at the issue note's ~$95, layer.ai as closed, Arthur's 'done' as finished (ENG-2462 Done), every step by Mar 1, and never "
  "finds the campaign, the DM reply, Arthur's two mails, the layer.ai reply, the store notice or the warehouse. It scores 14.3 % on the rev4 surface "
  "(plan/policy_scores.txt, first policy); no implemented record hands it a deciding value (fact_check --no-leak PASS: $140, $62 and $248 each live only "
  "in their home rows).")
A("")
A("Re-verified this stage through hg.py (not carried from notes): REVENUE_DAILY January sums and the IAP/ads split; REVENUE_DAILY_V2; the AWS guide text; the App Store rejection template; Jenkins job numbering (#216, #217) and branch; PR #1916 and branches/981; Linear users and the newest ENG issue; Trello board, last idShort and member ids; the #winddown checklist, keep list and action items; #prototype Feb 11 lines; Leonard's $3,750 and $100 lines; the CF backend lines (C09UHHN6PFZ 2026-01 'I'll start backend', Feb 6 'Blake's backend').")
A("")
A("Blind sweeps (before sealing):")
A("- rev1: a fork sweep and a coherence sweep. Their dispositions, with base pointers, are in `Working_Files/plan/sweep_dispositions.md`.")
A("- rev2 and rev3: two more fork sweeps.")
A("- rev4: a fresh agent with no answer key, hg.py only, Robert-visible records, Linear writes first. It reproduced the solver independently:")
A("  - DD in at $183.11 against $140, ZM out;")
A("  - CF's stacks at $62 from Arthur's Jenkins email over his $95 note;")
A("  - ENG-2462 Todo/Arthur from the App Store notice;")
A("  - Metabase, dbt and GitHub Done;")
A("  - a new campaign issue, Todo/Leonard;")
A("  - $3,450 a month, $1,150 each, and Arthur $902.")
A("- What the rev4 sweep left open, and how each was handled:")
A("  - layer.ai's state (OPEN): fixed in two steps. The fourth sweep's fix ('the account itself just lapses') still left it open to a fifth, focused re-sweep run for the prompt check; "
  "the reply now ends 'the art goes with CF, there's nothing on the layer account for our new company to take, it just lapses', so the issue is Canceled and the export step stays on the sheet.")
A("  - The campaign's own row (WEAK): fixed with 'count it as its own line'.")
A("  - The Calm Play note dated after the rules (WEAK): fixed. It is now dated before them.")
A("  - DD support's By date (WEAK): the rubric accepts Feb 15–28.")
A("  - DD's assignee (WEAK): settled as in rev3.")
A("  - Its PR #1917 'merged=None' was a rendering artefact of its dump; the SQL inserts merged = true.")
A("- rev4, fifth sweep (2026-11-06, focused on the six items rev4 touched, fresh agent, no answer key): every value matched the solver; ENG-2454's state was the only OPEN fork "
  "(fixed above); GitHub, ENG-2462, CF stacks and the campaign were WEAK with a record beating each; Jenkins gets no line (`plan/sweep_dispositions.md`).")
A("- Before sealing the design: an independent fallback red team of the rev4 design delta (`01b_Redteam_Fallback_rev4.md`).")
A("")
A("Unresolved:")
A("- Opus 5.5 landing rates remain UNCALIBRATED priors (n_eff 1–4); one run per family at most for DONE and DATE.")
A("- The two forecast views disagree by construction (see above).")
A("- The rev4 sweep's fixes (layer.ai reply, campaign line, Calm Play note time) were not re-swept by a fresh agent; each is a one-sentence record change re-checked here through hg.py.")
A("")
open(os.path.join(WF, "01_Grounding_Dossier.md"), "w").write("\n".join(L) + "\n")
print("wrote 01_Grounding_Dossier.md", len("\n".join(L)), "chars")

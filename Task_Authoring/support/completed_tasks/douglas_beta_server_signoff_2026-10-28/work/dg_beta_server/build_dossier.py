"""Writes task_inputs/Working_Files/01_Grounding_Dossier.md from the minted ids, the SQL ids and the verbatim tool outputs."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SCR = pathlib.Path(sys.argv[1])          # scratch dir with out_*.txt
M = json.load(open(HERE / 'minted_ids.json'))
S = json.load(open(HERE / 'sql_ids.json'))
P = json.load(open(HERE / 'planned_text.json'))
COH = json.load(open(HERE / 'cohort.json'))


def out(name):
    return (SCR / name).read_text().rstrip('\n')


def s(k):
    return f"{M[k]['channel']}/{M[k]['ts']}"


DG = 'douglas@harmonygames.co'
GA, GL = f"{DG}/{M['G_AMEND']['message_id']}", S['gmail_threads']['G_LEO'][DG]   # GA: Arthur's reply inside Leonard's thread
CCO, CCA, AR = M['CC_OLI']['id'], M['CC_ART']['id'], M['RC_ART46']['id']
R38, R39 = M['RC_C38']['id'], M['RC_DG39']['id']   # hardening r3: inline review comments on #38 (ZOM-459) and #39 (ZOM-509)
H1, H1C, CL = M['T_H1CARD']['id'], M['T_H1CMT']['id'], M['T_CLIENTCARD']['id']
DOC, LOG, BETA, CQA = M['DOC_DEPLOYS']['id'], M['SHEET_DEPLOYLOG']['id'], M['FOLDER_BETA']['id'], M['FOLDER_CLIENTQA']['id']
FRZ = M['GCAL_FREEZE']['copies'][DG]
OK = f"C0880U9751A/{S['ok_reply']['ts']}"
PR = lambda n: M['PRS'][str(n)]
LN = {k: v for k, v in S['linear_comments'].items()}
IN = ["ZOM-459", "ZOM-509", "ZOM-336", "ZOM-392", "ZOM-503", "ZOM-518", "ZOM-499", "ZOM-531", "ZOM-537", "ZOM-444",
      "ZOM-487", "ZOM-550", "ZOM-435", "ZOM-557", "ZOM-510", "ZOM-256", "ZOM-436"]
ONPROD = {"ZOM-459": ("N", "#38 + plague race table import (dev)"), "ZOM-509": ("N", "#39 + trophy path copy table import (dev)"),
          "ZOM-336": ("N", "#40"), "ZOM-392": ("N", "#41"),
          "ZOM-503": ("N", "#42 + #52"), "ZOM-518": ("N", "#43"), "ZOM-499": ("Y", "#44"),
          "ZOM-531": ("N", "#45 + loadout table import (dev)"),
          "ZOM-537": ("N", "#46 + economy table import (dev)"), "ZOM-444": ("N", "#47 + analytics events table import (dev)"),
          "ZOM-436": ("N", "analytics events table import (dev)"),
          "ZOM-487": ("N", "#48 + boss arena HP table import (dev)"), "ZOM-550": ("N", "#50"),
          "ZOM-435": ("N", "#51"), "ZOM-557": ("N", "#54"), "ZOM-510": ("Y", "Zombie Lane rewards import (prod)"),
          "ZOM-256": ("N", "algo levels 2.0 level pack import (dev)")}
L = []
w = L.append

w("# Grounding Dossier — dg-beta-server-signoff (persona Douglas, Long Horizon, effective profile long)")
w("")
w("Implements `01_Scenario_Design.md` v2 (scenario gate PASS) as `task_inputs/01_Universe_Inject.sql`: INSERT-only rows over 10 "
  "schemas (gdrive, gdocs, gsheets, confluence, slack, trello, gmail, gcal, github, linear). Builders: "
  "`support/task_work/dg_beta_server/` (`mint_ids.py`, `build_sql.py`, `build_final_manifest.py`, `build_dossier.py`; ids in "
  "`minted_ids.json`, SQL keys in `sql_ids.json`). Clock 2025-10-01T00:00Z; latest seeded timestamp 2025-09-30T21:12:44Z "
  f"(Arthur's ask, {s('S_ASK')}). Revisions 5, 6 and 7 (§13) are hardening rounds 1, 2 and 3 "
  "(`01a_Hardening_Report.md`).")
w("")

# ---------------------------------------------------------------- 1.A
w("## 1.A Structural")
w("")
w("Columns from `references/universe_schema_live.json` (NOT NULL marked *); base counts and sample ids read from the exports.")
w("")
w("| Table | Columns used (NOT NULL *) | Base count · samples | Timestamp format / notes |")
w("|---|---|---|---|")
rows1a = [
    ("slack.slack_messages", "id*, ts*, channel_id*, type*, user_id, text*, thread_parent_id, thread_ts_legacy, reply_count*, reply_users_count*, latest_reply, is_activity_message*, reactions_json*, files_json*, attachments_json*, created_at*, metadata_json*",
     "687,230 · D079SNE2TL4/1759256193.859279, D05QQF7V404/1757975508.211599, C0880U9751A/1757618419.809199", "ts 6 decimals; id = sha256(channel|ts)[:32]; replies carry parent id + thread_ts_legacy (sample_task_01 shape)"),
    ("gmail.gmail_threads / gmail_messages", "id*, thread_id*, user_email*, label_ids_json, internal_date, date, subject, from_email, to_json, cc_json, body_text, headers_json, …",
     "88,726 thread files · douglas@harmonygames.co_1829035630999538536.json", "date ISO-Z, internal_date ms; ids are the mailbox plus the RFC Message-ID, and the mailbox plus the numeric thread id"),
    ("gcal.gcal_events", "event_id*, calendar_id*, summary, start_ts, end_ts, start_json, end_json, organizer_email, attendees_json, status, ical_uid, created, updated, sequence",
     "11,233 · evt_00009bfb80dabb15aa5bb5, evt_0006932921e100bf00418e", "one row per attendee calendar, self:true on the owner copy; ical_uid 32 hex@hg4"),
    ("gdrive.drive_files / gdocs.docs_documents / gsheets.*", "id*, name, mime_type, parents_json, owner_email, shared_with_emails_json, shared_roles_json, modified_time, created_time; docs body_text, style_runs_json; sheets grid_json",
     "53,866 drive · 633 docs · 398 sheets · f_00117462881159eceee63e, f_00c30de5acd0cf7656c140", "folders d_ + 22 hex, files f_ + 22 hex; same id in drive and docs/sheets rows"),
    ("trello.trello_cards / trello_actions", "id*, name, \"idBoard\", \"idList\", \"desc\", pos, \"idShort\", url, \"dateLastActivity\", badges_json; actions type, date, \"idMemberCreator\", data_json",
     "803 cards, 5,294 actions · 6851a7abf7876721472dba99 (BETA: Oct 10), 68d1eb90bef538c7c5c5599d", "ids = 8 hex unix seconds + 16 hex; idShort next free on ZM ROADMAP = 80 (max 79)"),
    ("confluence.confluence_pages / page_versions", "id*, space_id*, parent_id, title*, body*, body_format*, status*, version*, author_id, created_at*, updated_at*",
     "31 pages, 78 versions · page_cicd_pipeline, page_ops_home", "version 1 + one version row each"),
    ("github.github_pull_requests", "id*, repo_id*, number*, title, state, merged, author_login, merged_by_login, body, base_ref, head_ref, base_sha, head_sha, merge_commit_sha, created_at, updated_at, merged_at, closed_at, …",
     "2,629 · harmonygames-Games/match3d-backend#31, harmonygames-Games/match3d-backend#14", "match3d-backend base #1–#36; new #37–#54"),
    ("github.github_pr_comments / github_reviews / github_timeline_events", "comments id*, pr_id*, author_login, body, created_at; reviews id*, pr_id*, state, body, submitted_at, commit_id, seq*; timeline id*, pr_id*, event*, actor_login, created_at, data_json",
     "884 / 2,421 / 12,435 · match3d-backend#31#c_1, #31#rev_1, #31#ev_4", "ids are the PR id plus #c_n / #rev_n / #ev_n; CodeRabbit comment actor SVC_0321 on the timeline (I07)"),
    ("github.github_branches / github_commits / github_pull_request_commits", "branch id*, repo_id*, name*; commit sha*, repo_id*, message, authored_date, author_*; prc id*, pr_id*, commit_sha*, position",
     "2,011 / 12,687 / 15,938 · harmonygames-Games/match3d-backend:bot-names", "one branch, one commit, one PR-commit row per seeded PR"),
    ("linear.linear_comments / linear_issues", "id*, issue_id*, author_id*, parent_id, body*, is_edited*, created_at*, updated_at*, sequence; issues updated_at*",
     "0 comments / 3,852 issues · ZOM-503, ZOM-459", "cmt_ + 20 hex; varchar ISO-Z; comments before completed_at"),
]
for r in rows1a:
    w("| " + " | ".join(r) + " |")
w("")

# ---------------------------------------------------------------- 1.B
w("## 1.B Entity table")
w("")
w("| Entity | Canonical / ids | Services (cited) | Verdict |")
w("|---|---|---|---|")
for r in [
    ("Douglas (persona)", "douglas@harmonygames.co; Slack EMPLOYEE_0031_SLACK_ID; Linear usr_cd7849ec043ab3da; GitHub PERSON_5760_GITHUB_USERNAME", "D05QQF7V404/1757975508.211599; harmonygames-Games/match3d-backend#2", "AGREE"),
    ("Arthur Blake", "arthur.blake@harmonygames.co; EMPLOYEE_0025_SLACK_ID; usr_cc3e90160f490686; EMPLOYEE_0025_GITHUB_USERNAME; Trello 2162c1ba310341bf318f48b7; user_EMPLOYEE_0025", "D05QQF7V404/1757975508.211599; page_eng_home", "AGREE (\"Blake\" in Slack, D079SNE2TL4/1759164463.327349)"),
    ("Oliver Brooks", "oliver.brooks@harmonygames.co; EMPLOYEE_0003_SLACK_ID; usr_bdf01b53c6a92c5e", "C0880U9751A/1757618419.809199; ZOM-509", "AGREE (not Lauren Brooks)"),
    ("Vincent Parker", "vincent.parker@harmonygames.co; usr_65c76e0b87aa7e9b; EMPLOYEE_0012_GITHUB_USERNAME", "D079SNE2TL4/1759269524.769369; ZOM-503 creator", "AGREE"),
    ("match3d-backend contractor", "PERSON_2967_GITHUB_USERNAME / PERSON_2967_NAME / PERSON_2967_EMAIL", "harmonygames-Games/match3d-backend#14, #31", "AGREE (token only, P04)"),
    ("CodeRabbit", "PERSON_6026_GITHUB_USERNAME (timeline actor SVC_0321_GITHUB_USERNAME)", "harmonygames-Games/match3d-backend#31#c_1, #10#rev_1", "AGREE (I07 mirrored)"),
    ("match3d-backend vs match3d", "harmonygames-Games/match3d-backend (server) vs harmonygames-Games/match3d (client, mirrored to C093LEZGF6J)", "harmonygames-Games/match3d#438", "DISAGREE (designed lookalike, N02); every seed says match3d-backend"),
    ("ZOM-n vs ENG-n", "ZOM-503, ZOM-557 vs ENG-503, ENG-557", "linear ZOM-503", "AGREE (N01 noted)"),
    ("Beta", "ZM ROADMAP list 'BETA: Oct 10' (6851a674975da1fe76e70d93); page_zm_beta_oct10", "trello:6851a7abf7876721472dba99", "AGREE"),
    ("Prod deploys", "base deploy messages D079SNE2TL4/1757351863.576949, /1757449699.464389, /1758040504.640159, /1759256193.859279", "seeded prod: notes on #42/#44, #46, #48, #52", "AGREE (timeline built on them)"),
]:
    w("| " + " | ".join(r) + " |")
w("")

# ---------------------------------------------------------------- 1.C
w("## 1.C Voice and realism (speakers, activity, conventions)")
w("")
w("Lengths and hours from `references/universe_kb/conventions.json` (`slack.length_chars_by_channel_type`: DMs short, lowercase for "
  "Arthur; `slack.per_person_hours_and_style`: Douglas posts 15:00–03:59Z; `github.pr_title_patterns`: 'Area: change' as in "
  "match3d-backend#31 'Endless Monster Mode: Best score and fixes to weekly rankings'; `linear` comments one or two lines). Every "
  "seeded speaker with `status_at_clock` from `references/universe_kb/activity.json`:")
w("")
w("| Speaker | Email / id | activity.json status_at_clock | Seeded where | Real sample |")
w("|---|---|---|---|---|")
for r in [
    ("Arthur Blake", "arthur.blake@harmonygames.co", "activity: active_sep_2025", "DM ask, inline review comment on #46, freeze message, #50 thread reply, cards + comment, reply-all in Leonard's thread, gcal, Confluence page + comment reply, reviews", "D05QQF7V404/1758146982.108989 'Can we update required versions for ZM'"),
    ("Douglas", "douglas@harmonygames.co", "activity: active_sep_2025", "claim, #50 question, 'ok', doc, log, prod:/rollback: notes, reviews, inline review comment on #39, ZOM-537 comment", "D079SNE2TL4/1759164463.327349 'Ok, the deployment is done'"),
    ("Oliver Brooks", "oliver.brooks@harmonygames.co", "activity: active_sep_2025", "May claim, summary, post-here ask, Linear comments, client QA folder, ZM beta page QA comment", "C0880U9751A/1757618419.809199"),
    ("Leonard Hayes", "leonard.hayes@harmonygames.co", "activity: active_sep_2025", "go/no-go email (A2), ZOM-256 comment", "gmail:leonard@harmonygames.co_1842219327413774622.json"),
    ("Vincent Parker", "vincent.parker@harmonygames.co", "activity: active_sep_2025", "Linear QA comments, 'works on dev' on #51", "D079SNE2TL4/1759269524.769369 'Yep it works as expected'"),
    ("Owen Baker", "owen.baker@harmonygames.co", "activity: active_sep_2025", "ZOM-503 comment", "D05SG9H1CFM/1758919727.787169 (thread partner)"),
    ("Calvin Price", "calvin.price@harmonygames.co", "activity: active_sep_2025", "ZOM-499 and client comments", "ZOM-499 assignee"),
    ("Claire Morgan", "claire.morgan@harmonygames.co", "activity: active_sep_2025", "ZOM-336 and prop comments", "ZOM-336 assignee"),
    ("Samuel Turner", "samuel.turner@harmonygames.co", "activity: active_sep_2025", "client comments", "ZOM-470 assignee"),
    ("Marcus Bennett", "marcus.bennett@harmonygames.co", "activity: active_sep_2025", "VFX comments", "ZOM-464 assignee"),
    ("Brian Foster", "brian.foster@harmonygames.co", "activity: active_sep_2025", "ZOM-419 comment", "ZOM-419 assignee"),
    ("contractor / CodeRabbit", "PERSON_2967_EMAIL / SVC_0271_EMAIL (PERSON_6026_GITHUB_USERNAME)", "activity: not a person in activity.json (GitHub tokens)", "PR comments/reviews only (contractor: inline review comment on #38)", "harmonygames-Games/match3d-backend#31#c_1"),
]:
    w("| " + " | ".join(r) + " |")
w("")
w("Douglas's seeded times all fall in 15:00–03:59Z (his base posting window); the cut-day deploys (2025-08-25 11:52Z) and #43 "
  "(12:50Z) are the contractor's. Weekend items are the designed freeze weekend (Sep 27–28) and Sep 20 02:00Z (Friday evening in "
  "Douglas's time zone).")
w("")

# ---------------------------------------------------------------- 1.D
w("## 1.D Keyword / findability (base hit counts via `tools/hg.py search search <svc> <term>`)")
w("")
w("| Term | Service | Base hits | Disposition |")
w("|---|---|---|---|")
for term, svc, rec in [("beta sign-off", "trello", f"{H1}, {CL}"), ("sign-off", "trello", f"{H1}, {CL}"),
                       ("server freeze", "slack", f"{s('S_FREEZE_MON')}; gcal {FRZ}"),
                       ("go ahead on dev", "slack", s('S_ART_DEVONLY')), ("prod deploys", "gdocs", DOC),
                       ("deploy log", "gdrive", LOG), ("ZM Beta sign-off", "gdrive", f"{BETA}, {CQA}"),
                       ("server sign-off", "confluence", "page_dd_launch_server_signoff"), ("ZM beta", "confluence", "page_zm_beta_oct10"),
                       ("boss arena HP table", "confluence/gsheets", f"{CCA} and the deploy log {LOG}"),
                       ("economy table", "github/gsheets", f"{AR} (inline review comment) and the deploy log {LOG}"),
                       ("plague race table", "github/gsheets", f"{R38} (inline review comment) and the deploy log {LOG}"),
                       ("trophy path copy table", "github/gsheets", f"{R39} (inline review comment) and the deploy log {LOG}"),
                       ("analytics events table", "gmail/gsheets", f"{GA} (Arthur's reply-all) and the deploy log {LOG}"),
                       ("loadout table", "gmail/gsheets", f"{GA} (Arthur's reply-all) and the deploy log {LOG}"),
                       ("match3d-backend", "linear", "the 19 decisive + ~30 neutral Linear comments (e.g. " + LN['ZOM-503']['id'] + ")")]:
    w(f"| {term} | {svc} | 0 (scan_complete true) | NEW TERM — introduced in {rec}, reached via anchor A1 D05QQF7V404/1759266764.508127 |")
w("| prod: | github | 0 returned (scan_complete false: bounded) | NEW TERM — introduced in the seeded PR comments (e.g. harmonygames-Games/match3d-backend#44#c_2); a bounded miss proves nothing, but no base PR comment uses the keyword (base match3d-backend comments are CodeRabbit walkthroughs, match3d-backend#31#c_1) |")
w("")

# ---------------------------------------------------------------- 1.E
w("## 1.E Persona reach (scoped records)")
w("")
w("| Record | Service | Visibility path | LB |")
w("|---|---|---|---|")
for rec, svc, path in [
    (s('S_ASK'), "slack", "im D05QQF7V404 (Arthur, Douglas)"),
    (s('S_DG_CLAIM'), "slack", "im D05QQF7V404"),
    (s('S_FREEZE_MON'), "slack", "#zombie-match3d member"), (s('S_DG_ASK47'), "slack", "#zombie-match3d member"),
    (s('S_ART_DEVONLY'), "slack", "thread reply in #zombie-match3d"), (OK, "slack", "thread reply"),
    (s('S_OLIVER_SUM'), "slack", "#zombie-match3d member"), (s('S_OLIVER_POST'), "slack", "#zombie-match3d member"),
    (s('S_OLIVER_MERGED'), "slack", "#zombie-match3d member"),
    (GA, "gmail", "Douglas's own mailbox (INBOX), reply inside thread " + GL), (GL, "gmail", "Douglas's own mailbox (INBOX)"),
    (FRZ, "gcal", "Douglas's own calendar copy"), (DOC, "gdocs", "owner"), (LOG, "gsheets", "owner"),
    (BETA, "gdrive", "shared writer"), (CQA, "gdrive", "shared reader"),
    ("D079SNE2TL4/1759256193.859279", "slack", "im member (base)"), ("D079SNE2TL4/1759269524.769369", "slack", "im member (base)"),
    ("D079SNE2TL4/1757351863.576949", "slack", "im member (base)"), ("D079SNE2TL4/1757355159.852859", "slack", "im member (base)"),
    ("D079SNE2TL4/1757449699.464389", "slack", "im member (base)"), ("D079SNE2TL4/1758040504.640159", "slack", "im member (base)")]:
    w(f"| {rec} | {svc} | {path} | LB |")
w("")
w("Trello, Confluence, Linear and GitHub are unscoped (`Evals/references/persona/acl.md`). `persona_view.py check-sql douglas "
  "task_inputs/01_Universe_Inject.sql --load-bearing <ids>` (verbatim):")
w("")
w("```")
w(out('out_checksql.txt'))
w("```")
w("")
w("The NO rows are the sender's and cc's own mailbox copies (Arthur, Leonard); none is load-bearing. The two page comments "
  f"({CCO}, {CCA}) are Confluence rows, unscoped.")
w("")

# ---------------------------------------------------------------- 1.F
w("## 1.F Collision checks")
w("")
w("Identity tokens: no new person or token is introduced; PR authors use the base logins (PERSON_5760, PERSON_2967, "
  "EMPLOYEE_0025, EMPLOYEE_0012, PERSON_6026). Every minted id (172: Slack ids and ts, Trello, Drive, GCal, Linear comment, "
  "Gmail thread/Message-ID, Confluence page, 40-hex sha) was scanned as a fixed string over the full collections "
  "(`grep -rFl -f minted.txt HarmonyGames_Other_Services/Services_Data HarmonyGames_GitHub/Services_Data HarmonyGames_Gmail`): "
  "0 files hit. PR numbers harmonygames-Games/match3d-backend#37–#54 do not exist in the base (highest #36, post-clock). "
  "ZOM-n keys are base ids reused as references only.")
w("")
w("| Id class | Count | Sample | Base hits |")
w("|---|---|---|---|")
for r in [("Slack id / ts", "10", f"{M['S_ASK']['id']} / {M['S_ASK']['ts']}", "0"), ("Trello", "5", f"{H1}", "0"),
          ("Drive family", "4", f"{BETA}, {DOC}", "0"), ("GCal", "5", FRZ, "0"), ("Linear comment", "79", LN['ZOM-503']['id'], "0"),
          ("Gmail", "9 (3 threads, 6 Message-ID rows)", GA, "0"), ("Confluence", "4 (2 pages, 2 comments)", f"page_zm_beta_oct10, {CCA}", "0"),
          ("GitHub PR", "18", "harmonygames-Games/match3d-backend#37", "0")]:
    w("| " + " | ".join(r) + " |")
w("")

# ---------------------------------------------------------------- 2 ledger
w("## 2 Record ledger")
w("")
w("| # | Service · table | Id(s) | Container | Manifest element | Carrier | Reach | Discovery role |")
w("|---|---|---|---|---|---|---|---|")
led = [
    ("gdrive · drive_files", f"{BETA}", "Arthur's root d_cc3e90160f490686039986", "K13 destination", "●", "writer", "write target"),
    ("gdrive · drive_files", f"{CQA}", "Oliver's root d_bdf01b53c6a92c5e167c65", "T19 decoy", "●", "reader", "decoy"),
    ("gdrive+gdocs", DOC, "Douglas's root", "H2 / K5, K6, K8, K11", "●", "owner", "authority"),
    ("gdrive+gsheets (2 tabs)", LOG, "Douglas's root", "K7, K8; T6, T11; C9-C13 (plague race, trophy path copy, loadout, analytics events, economy and boss arena HP table imports, dev)", "●", "owner", "connecting"),
    ("confluence · pages+versions", "page_zm_beta_oct10", "space_OPS / page_ops_home", "K9", "●", "unscoped", "connecting"),
    ("confluence · pages+versions", "page_dd_launch_server_signoff", "space_OPS / page_ops_home", "T1 decoy (H1)", "●", "unscoped", "decoy"),
    ("confluence · comments ×2", f"{CCO} (Oliver, QA question), {CCA} (Arthur's reply)", "page_zm_beta_oct10", "K14; C9; T23", "●", "unscoped", "overturning reply"),
    ("slack · messages", s('S_ASK'), "D05QQF7V404", "A1 / K1 (plain message, reply_count 0)", "●", "im", "first link"),
    ("github · review_comments", AR, "match3d-backend#46, on Arthur's Approve", "K15; C10; T24", "●", "unscoped", "amendment (inline review comment)"),
    ("github · review_comments", R38, "match3d-backend#38, on the contractor's Approve", "K17; C12; T27", "●", "unscoped", "amendment (inline review comment)"),
    ("github · review_comments", R39, "match3d-backend#39, on Douglas's Approve", "K18; C13; T28", "●", "unscoped", "amendment (inline review comment)"),
    ("slack · messages", s('S_DG_CLAIM'), "D05QQF7V404", "T22", "●", "im", "claim met first"),
    ("slack · messages", s('S_FREEZE_MON'), "C0880U9751A", "T2 (oldest)", "●", "member", "claim met first"),
    ("slack · messages", f"{s('S_DG_ASK47')}, {s('S_ART_DEVONLY')}, {OK}", "C0880U9751A thread", "T8, C2", "●", "member", "claim + overturning reply"),
    ("slack · messages", s('S_OLIVER_SUM'), "C0880U9751A", "T4, T20, C1", "●", "member", "claim met first"),
    ("slack · messages", s('S_OLIVER_POST'), "C0880U9751A", "T16", "●", "member", "decoy"),
    ("slack · messages", s('S_OLIVER_MERGED'), "C0880U9751A", "T3 (oldest), H2 decoy", "●", "member", "decoy"),
    ("trello · cards+actions", f"{H1} (+ createCard {M['T_H1CREATE']['id']})", "6851a6569f3bf818760632ab / BETA: Oct 10", "H1 / K2", "●", "unscoped", "authority"),
    ("trello · actions", H1C, f"card {H1}", "K3 amendment", "●", "unscoped", "amendment"),
    ("trello · cards+actions", f"{CL} (+ {M['T_CLIENTCREATE']['id']})", "same list", "T7 decoy", "●", "unscoped", "decoy"),
    ("gmail · threads ×3 + messages ×3", GL, "Douglas INBOX (+ Arthur INBOX, Leonard SENT)", "A2 / K12", "●", "own mailbox", "first link"),
    ("gmail · messages ×3 (reply in the same threads)", GA, "Douglas INBOX (+ Leonard INBOX, Arthur SENT); In-Reply-To Leonard's message", "K4, K16 amendments; C6, C11; T25, T26", "●", "own mailbox", "amendment (thread reply)"),
    ("gcal · events ×5", ", ".join(M['GCAL_FREEZE']['copies'].values()), "5 attendee calendars", "K6; T2 (newest)", "● (start)", "own copy", "overturning"),
    ("github · pull_requests/branches/commits/prc ×18", "harmonygames-Games/match3d-backend#37 … #54", "match3d-backend", "K11; cohort surface 2/3", "●", "unscoped", "per-record"),
    ("github · pr_comments ×40", "harmonygames-Games/match3d-backend#37#c_1 … #54#c_3", "PRs", "prod:/rollback:/dev notes; CodeRabbit walkthroughs", "●", "unscoped", "per-record"),
    ("github · reviews ×37", "harmonygames-Games/match3d-backend#37#rev_1 … #54#rev_2", "PRs", "approval rule rows (C3, C8, T9, T21)", "●", "unscoped", "per-record"),
    ("github · timeline_events ×131", "harmonygames-Games/match3d-backend#37#ev_1 …", "PRs", "companions (commented/reviewed/merged/closed)", "—", "unscoped", "companion"),
    ("linear · comments ×79", f"{LN['ZOM-503']['id']} … (sql_ids.json linear_comments)", "73 cohort tickets + ZOM-461, ZOM-480, ZOM-479, ZOM-489", "cohort surface 1; K10", "● (§6b)", "unscoped", "per-record"),
    ]
for i, r in enumerate(led, 1):
    w(f"| {i} | " + " | ".join(r) + " |")
w("")

# ---------------------------------------------------------------- 3 findability
w("## 3 Findability and discovery-order proofs")
w("")
for rec, query, term, compet, pos in [
    (f"trello.trello_cards · {H1}", '"beta sign-off" via trello_search', "NEW TERM (0 base hits); card title 'Beta sign-off - server side'", f"1 competing seed ({CL}, same list)", "first link from A1"),
    (f"gdocs.docs_documents · {DOC}", '"prod deploys" / "match3d-backend" via gdocs_search_documents', "NEW TERM (0 base hits)", "0", "connecting (card rule 3)"),
    (f"gsheets · {LOG}", '"deploy log" via gdrive_search', "NEW TERM (0 base hits)", "0", "connecting (card rule 1, doc)"),
    (f"gcal · {FRZ}", "gcal_list_events Sep 22–30 on Douglas's calendar", "summary 'ZM beta - server freeze'", "Douglas has 12 events in Sep 2025 (reach census)", "terminal (freeze instant)"),
    ("confluence · page_zm_beta_oct10", '"ZM beta" via confluence_search', "NEW TERM (0 base hits)", "page_dd_launch_server_signoff on 'sign-off'", "connecting (card rule 6)"),
    (f"gmail · {GA}", f"gmail_get_thread on Leonard's thread {GL} (or a 'go/no-go' search, which returns both messages)", "subject 'Re: beta go/no-go thursday'; both points (547/553 off; the analytics events and loadout table imports)", "0 base mails on 'beta go/no-go'", "amendment (reply under the A2 message)"),
    (f"confluence.confluence_comments · {CCA}", "confluence_list_comments(page_zm_beta_oct10)", "reply to QA naming ZOM-487 and the boss arena HP table", "0 other comments on the page", "overturning reply (C9)"),
    (f"github.github_review_comments · {AR}", "inline review comments of #46 (github_get_pull_request_comments)", "'537 also needs the economy table import'", "inline comments also on #38 and #39 (other tickets)", "amendment (C10)"),
    (f"github.github_review_comments · {R38}", "inline review comments of #38 (github_get_pull_request_comments)", "'459 also needs the plague race table import'", "inline comments also on #39 and #46 (other tickets)", "amendment (C12)"),
    (f"github.github_review_comments · {R39}", "inline review comments of #39 (github_get_pull_request_comments)", "'509 needs that table imported on the backend too'", "inline comments also on #38 and #46 (other tickets)", "amendment (C13)"),
    (f"gmail · {GL}", '"go/no-go" via gmail_search_messages', "subject 'beta go/no-go thursday'", "0 base mails on 'beta go/no-go'", "first link (A2)"),
    (f"linear.linear_comments · {LN['ZOM-336']['id']}", "linear_list_comments(ZOM-336)", "per-record; no list/search returns comments (Ask_Carriers §6b)", "—", "per-record"),
]:
    w("```")
    w(f"Record:              {rec}")
    w(f"Agent's likely query: {query}")
    w(f"Term present:        {term}")
    w(f"Competing base hits: {compet}")
    w(f"Chain position:      {pos}")
    w("```")
w("")
w("**Discovery-order proofs (dynamic-change seeds).**")
w("")
w("| Claim met first | Overturned by | Why met first | Why decisive |")
w("|---|---|---|---|")
for r in [
    (s('S_FREEZE_MON') + " (Mon 29th)", f"{FRZ} (Fri 22:00Z, updated 2025-09-23T16:05Z)", "a Slack search 'freeze' returns it; Calendar is rarely opened (A13)", "decides whether #50's Sep 27 deploy needed Arthur's approval"),
    (s('S_OLIVER_SUM'), "harmonygames-Games/match3d-backend#54#c_3 (rollback Sep 28) and the PR records", "newest server-status message before the ask", "flips ZOM-557 and five more rows"),
    (s('S_DG_CLAIM'), "harmonygames-Games/match3d-backend#41#rev_2 (approval after the deploy); #51 dev note", "same DM as the ask", "flips ZOM-392, ZOM-435"),
    (s('S_DG_ASK47') + " (parent)", s('S_ART_DEVONLY') + " (reply)", "the parent names #50 and prod; the limit is in the reply (A14)", "ZOM-550"),
    (s('S_OLIVER_MERGED'), DOC, "Slack search 'merged'", "merged is not on prod"),
    ("page_dd_launch_server_signoff", f"{H1} → {H1C} → {GA}", "Confluence search 'server sign-off' returns it first", "imports in, ZOM-547/553 out"),
    (f"{GL} (Leonard's message, what a 'from:leonard' search returns)", f"{GA} (Arthur's reply-all under it)", "a sender search returns Leonard's message only; the reply needs the thread (A14)", "ZOM-547/553 out"),
    (f"{LN['ZOM-487']['id']} (ZOM-487: #48 only)", f"{CCA} (Arthur: the boss arena HP table import is part of it) + {LOG} (dev)", "the ticket comment is read per ticket; the page reply needs a comment read (A9)", "ZOM-487 N"),
    (f"{LN['ZOM-537']['id']} (ZOM-537: #46 only)", f"{AR} (Arthur: also the economy table import) + {LOG} (dev)", "the PR's conversation comments and review list don't carry it; inline review comments are a separate call (A14)", "ZOM-537 N"),
    (f"{LN['ZOM-444']['id']} (ZOM-444: #47 only), {LN['ZOM-531']['id']} (ZOM-531: #45 only), {LN['ZOM-436']['id']} (ZOM-436: QA device note)", f"{GA} second point (analytics events table import for ZOM-444 and ZOM-436, loadout table import for ZOM-531) + {LOG} (dev)", "a sender search returns Leonard's message only; the reply needs the thread (A14)", "ZOM-444, ZOM-531 N; ZOM-436 in, N"),
    (f"{LN['ZOM-459']['id']} (ZOM-459: #38 only)", f"{R38} (reviewer: also the plague race table import) + {LOG} (dev)", "inline review comments are a separate call (A14)", "ZOM-459 N"),
    (f"{LN['ZOM-509']['id']} (ZOM-509: #39 only)", f"{R39} (Douglas: also the trophy path copy table import) + {LOG} (dev)", "inline review comments are a separate call (A14)", "ZOM-509 N"),
    ("D079SNE2TL4/1759269524.769369 (Vincent: works as expected)", "harmonygames-Games/match3d-backend#52#rev_2 (contractor approval only) + the freeze", "Douglas's own DM, newest", "ZOM-503"),
]:
    w("| " + " | ".join(r) + " |")
w("")
w("**Hidden authorities.** H1 → `trello_search \"beta sign-off\"` returns " + H1 + " (and the client card " + CL + "); decoy "
  "page_dd_launch_server_signoff is reached by `confluence_search \"server sign-off\"` and differs on scope (Domino Delights) and on "
  "approval (Slack thumbs-up). H2 → `gdocs_search_documents \"prod deploys\"` returns " + DOC + "; decoy " + s('S_OLIVER_MERGED') +
  " is reached by a Slack search on 'merged' and differs on the decisive clause (merged = live).")
w("")

# ---------------------------------------------------------------- 4 self-validation
w("## 4 Self-validation")
w("")
w("| QC category | Tool-enforced (sql_lint / base_check) | Manual evidence |")
w("|---|---|---|")
for r in [
    ("Missing Universe Data", "—", "every needed fact seeded or base and persona-readable (1.E); reads via cataloged tools (`linear_list_comments`, `github_get_issue_comments`, `github_get_pull_request_reviews`, `gcal_list_events`)"),
    ("Temporal Field", "PASS (base_check Check C)", "text dates agree with fields: log rows = prod: comment times (harmonygames-Games/match3d-backend#46#c_2 20:29Z = log row '2025-09-09 20:29'); every Linear comment before its ticket's completed_at"),
    ("Cross-service Referential", "PASS (Check A)", "PR numbers in Linear comments and the email exist (#37–#54); Douglas's calendar copy carries the same ical_uid"),
    ("Quantitative / Reconciliation", "PASS", "deploy log rows agree with PR comments for every row the tab has (through Sep 10)"),
    ("State / Lifecycle", "PASS", "no ticket state changed; tickets closed before prod deploys by design (Done = verified on dev)"),
    ("Identifier / Format", "PASS", "ids follow base schemes (1.F); Gmail Message-ID form; GitHub #c_/#rev_/#ev_"),
    ("Semantic / Category", "—", "titles match content; 'match3d-backend' vs 'match3d' kept distinct (1.B)"),
    ("Other", "—", "no record states a conclusion; claims are dated human messages"),
]:
    w("| " + " | ".join(r) + " |")
w("")

# ---------------------------------------------------------------- 5 lazy solver
w("## 5 Lazy-solver pass on the implemented records")
w("")
for line in [
    f"- One Slack search ('server', 'prod') returns {s('S_OLIVER_SUM')} → everything on prod: 8 rows wrong (ZOM-557, ZOM-336, ZOM-435, ZOM-392, ZOM-518, ZOM-550, ZOM-503, ZOM-256).",
    f"- Card description only ({H1}) → no imports (ZOM-510, ZOM-256 missing) and ZOM-547/553 kept.",
    f"- Deploy log Prod deploys tab ({LOG}) as the record → ZOM-444, ZOM-499 read as not on prod; ZOM-392, ZOM-518 as on prod.",
    f"- Leonard's message only (get_message on {GL}) → ZOM-547/553 kept, ZOM-436 missing, ZOM-444 and ZOM-531 Y (18 rows, wrong counts); Arthur's reply {GA} is under it.",
    f"- #38 and #39 without their inline review comments → ZOM-459 and ZOM-509 Y; {R38} and {R39} add the plague race and trophy path copy table imports (dev).",
    f"- ZM beta page body only (no comment read) → ZOM-487 Y; {CCA} adds the boss arena HP table import (dev).",
    f"- #46 without its inline review comments → ZOM-537 Y; {AR} adds the economy table import (dev).",
    "- Unlinked Console & imports rows (plague race, trophy path copy, loadout, analytics events, economy and boss arena HP tables) name no ticket; a Linear search on 'boss arena' returns five Done tickets in the window (ZOM-487, ZOM-540, ZOM-547, ZOM-550, ZOM-553), and the two analytics tickets (ZOM-444, ZOM-436) say nothing about a table, so each link comes from the note that names it.",
    "- Comments without reviews → ZOM-392, ZOM-518, ZOM-550, ZOM-503 wrong (harmonygames-Games/match3d-backend#41#rev_2, #43, #50#rev_3, #52#rev_2).",
    f"- Parent of the #50 thread only ({s('S_DG_ASK47')}) → reads approval; the reply ({s('S_ART_DEVONLY')}) limits it to dev.",
    "- Bulk shortcuts: `linear_list_issues` returns no comments; no Slack mirror for match3d-backend; the Console & imports tab names no tickets; nothing lists the 17 tickets.",
]:
    w(line)
w("")

# ---------------------------------------------------------------- 6 intended disagreements
w("## 6 Intended disagreements")
w("")
w("| # | Disagreement | Why realistic | Resolved by |")
w("|---|---|---|---|")
IDIS = [
    (f"{s('S_FREEZE_MON')} says Monday 29th; {FRZ} says Fri 26 22:00Z", "freeze pulled in after QA asked for a frozen weekend (event description)", "the calendar event, updated Sep 23, newer and named in the doc"),
    (f"{s('S_OLIVER_SUM')} says all server fixes are on prod", "QA tested on prod Saturday morning, before #54's rollback, and did not check approvals", "PR comments/reviews (harmonygames-Games/match3d-backend#54#c_3 etc.)"),
    (f"{s('S_DG_CLAIM')} (Douglas: fix is out; seeds on prod since the 3rd)", "a developer's shorthand; #51 was on dev, #41's approval came later", "harmonygames-Games/match3d-backend#51#c_2 (dev), #41#rev_2 after #41#c_2"),
    (f"{s('S_OLIVER_MERGED')} (May: merged = live)", "true before match3d-backend#2 created prod", f"doc {DOC}"),
    ("page_dd_launch_server_signoff (DD launch rules)", "older rules for another game", f"card {H1} (ZM beta)"),
    (f"{LOG} Prod deploys tab stops on Sep 10", "a quick list Douglas stopped filling", "doc: the PR's prod: comment is the record"),
    ("D079SNE2TL4/1759256193.859279 + /1759269524.769369 (teams changes on prod, works)", "deployed during the freeze on the contractor's approval", "doc freeze clause; harmonygames-Games/match3d-backend#52#rev_2"),
    (f"{LN['ZOM-487']['id']} names #48 only; {CCA} adds the boss arena HP table import", "Vincent noted the PR when he closed the ticket; QA found the old HP values on prod on Sep 30", "Arthur's inline review comment (the rules' author, on his own Approve) + the deploy log (dev)"),
    (f"{LN['ZOM-537']['id']} names #46 only; {AR} adds the economy table import", "Douglas's own one-line note; the values also live in an imported table", "Arthur's inline review comment (the rules' author, on his own Approve) + the deploy log (dev)"),
    (f"{LN['ZOM-444']['id']} and {LN['ZOM-531']['id']} name one PR each; {LN['ZOM-436']['id']} is a QA device note; {GA} adds the analytics events and loadout table imports", "the closers noted the code change; the table imports were Douglas's later dev steps, which Arthur ties to the tickets before go/no-go", "Arthur's reply-all (the rules' author, Sep 30, newest) + the deploy log (dev)"),
    (f"{LN['ZOM-459']['id']} names #38 only; {R38} adds the plague race table import", "Arthur's one-line closing note; the reviewer flagged the table on the PR", "the reviewer's inline comment on #38 (on the Approve) + the deploy log (dev)"),
    (f"{LN['ZOM-509']['id']} names #39 only; {R39} adds the trophy path copy table import", "Oliver's closing note names the PR; Douglas left the import note on his own review", "Douglas's inline comment on #39 (on his Approve) + the deploy log (dev)"),
]
for i, r in enumerate(IDIS, 1):
    w(f"| {i} | " + " | ".join(r) + " |")
w("")

# ---------------------------------------------------------------- 7 constraints
w("## 7 Constraints for the prompt brief")
w("")
w("| Anchor | May be named (noun phrases only) | Record |")
w("|---|---|---|")
w(f"| A1 | Arthur's beta sign-off ask; Arthur's DM | slack {s('S_ASK')} |")
w(f"| A2 | Leonard's go/no-go email | gmail {GL} |")
w("")
w("Never name: the Trello card or board, the deploy doc, the deploy log, the calendar freeze, the Confluence pages, the folder, the "
  "cut time, the PR numbers, the ticket keys, the approval/rollback rules, the counts. Deadline: Thursday's go/no-go (Oct 2). "
  "Deliverable kinds: a register (sheet), a reply in the DM, ticket updates, the share for Leonard.")
w("")

# ---------------------------------------------------------------- 8 fact sheet
w("## 8 Fact sheet")
w("")
man = json.load(open(ROOT / 'task_inputs/Working_Files/01_Hardness_Manifest.json'))
w("| Key | Value | Kind | Home / must appear in |")
w("|---|---|---|---|")
for f in man['facts']:
    w(f"| {f['key']} | {f['value']} | {f['kind']} | {', '.join(f.get('home_ids', []))} |")
w("")
w("`python3 Task_Authoring/tools/fact_check.py task_inputs/01_Universe_Inject.sql --manifest Working_Files/01_Hardness_Manifest.json --no-leak` (verbatim):")
w("")
w("```")
w(out('out_fact.txt'))
w("```")
w("")

# ---------------------------------------------------------------- 9 facts for the human
w("## 9 Facts for the human")
w("")
w("### 9.1 Records")
w("")
w("| Locator | Base/seeded | Fact | Reach | Role | Re-verify? |")
w("|---|---|---|---|---|---|")
F = [
    (s('S_ASK'), "seeded", "Arthur 2025-09-30T21:12:44Z: " + P['S_ASK'] + " (plain message, no replies)", "im", "anchor A1", "no"),
    (AR, "seeded", "Arthur 2025-09-09T19:40:00Z, inline review comment on #46 (lib/zombies_game/economy.ex, with his Approve): " + P['RC_ART46'], "unscoped", "amendment (ZOM-537)", "no"),
    (R38, "seeded", "contractor 2025-08-25T09:20:00Z, inline review comment on #38 (lib/zombies_game/plague_race.ex, with the Approve): " + P['RC_C38'], "unscoped", "amendment (ZOM-459)", "no"),
    (R39, "seeded", "Douglas 2025-09-02T15:20:00Z, inline review comment on #39 (lib/zombies_game/trophy_path.ex, with his Approve): " + P['RC_DG39'], "unscoped", "amendment (ZOM-509)", "no"),
    (CCO, "seeded", "Oliver 2025-09-30T10:12Z on page_zm_beta_oct10: " + P['CC_OLI_BODY'], "unscoped", "QA question", "no"),
    (CCA, "seeded", "Arthur 2025-09-30T11:03Z, reply to " + CCO + ": " + P['CC_ART_BODY'], "unscoped", "amendment (ZOM-487)", "no"),
    (GL, "seeded", "Leonard 2025-09-30T20:15:03Z, cc Arthur, 'beta go/no-go thursday': share the register with him, comment access", "own mailbox", "anchor A2", "no"),
    (H1, "seeded", "Arthur 2025-09-29T17:20:41Z 'Beta sign-off - server side', rules 1–6", "unscoped", "authority H1", "no"),
    (H1C, "seeded", "Arthur 2025-09-30T15:05:27Z: " + P['H1_CMT'], "unscoped", "amendment", "no"),
    (GA, "seeded", "Arthur 2025-09-30T20:41:27Z, reply-all in Leonard's thread " + GL + " ('Re: beta go/no-go thursday'): ZOM-547 and ZOM-553 off the register, not counted; the analytics events table import is part of ZOM-444's and ZOM-436's server change, the loadout table import of ZOM-531's; both only on dev", "own mailbox", "amendment", "no"),
    (DOC, "seeded", "Douglas, created 2025-06-01T18:30Z, edited 2025-09-25T16:40Z: prod branch, prod:/rollback: comments, Approve by someone else before the deploy, Arthur's Approve inside the freeze", "owner", "authority H2", "no"),
    (FRZ, "seeded", "'ZM beta - server freeze' 2025-09-26T22:00Z–22:30Z, created 2025-09-22T14:02Z, updated 2025-09-23T16:05Z", "own copy", "freeze instant", "no"),
    (LOG, "seeded", "Prod deploys row 1 '2025-08-25 11:52 · beta prod cut'; tab stops 2025-09-10; Console & imports: plague race table dev 2025-08-26 10:30, plague race bot names console prod 2025-08-28 17:05, trophy path copy table dev 2025-09-02 18:05, Zombie Lane rewards import prod 2025-09-08 16:45, loadout table dev 2025-09-10 17:40, algo level pack dev 2025-09-11 16:30, analytics events table dev 2025-09-12 19:20, economy table dev 2025-09-16 14:20, boss arena HP table dev 2025-09-17 15:50", "owner", "cut + imports", "no"),
    ("page_zm_beta_oct10", "seeded", "Arthur 2025-09-29T17:15Z: sign-off folder 'ZM Beta sign-off'", "unscoped", "destination pointer", "no"),
    (BETA, "seeded", "'ZM Beta sign-off' (Arthur; Douglas, Oliver, Vincent writers)", "writer", "write target", "no"),
    (CQA, "seeded", "'ZM Beta sign-off - client QA' (Oliver)", "reader", "decoy", "no"),
    (CL, "seeded", "client sign-off card (In Validation, Aug 15)", "unscoped", "decoy", "no"),
    ("page_dd_launch_server_signoff", "seeded", "DD launch sign-off (May 2025)", "unscoped", "decoy", "no"),
    (s('S_FREEZE_MON'), "seeded", "Arthur 2025-09-19: freeze Monday the 29th", "member", "claim met first", "no"),
    (f"{s('S_DG_ASK47')} / {s('S_ART_DEVONLY')} / {OK}", "seeded", "Douglas asks to push #50 to prod; Arthur: go ahead on dev, PR review before prod; Douglas: ok", "member", "claim + reply", "no"),
    (s('S_OLIVER_SUM'), "seeded", "Oliver 2025-09-27T16:40Z: all server fixes since the cut on prod", "member", "claim met first", "no"),
    (s('S_DG_CLAIM'), "seeded", "Douglas 2025-09-22T20:10Z: trophy path fix out; algo seeds on prod since the 3rd", "im", "claim met first", "no"),
    (s('S_OLIVER_POST'), "seeded", "Oliver: post the list here too", "member", "decoy", "no"),
    (s('S_OLIVER_MERGED'), "seeded", "Oliver 2025-05-28: merged into main = live", "member", "decoy", "no"),
    ("D079SNE2TL4/1759256193.859279", "base", "Douglas 2025-09-30T18:16Z: updated prod with the latest teams/social changes", "im", "claim (= #52 prod:)", "no"),
    ("D079SNE2TL4/1759269524.769369", "base", "Vincent 2025-09-30T21:58Z: works as expected", "im", "claim", "no"),
]
for n in sorted(M['PRS'], key=int):
    pr = M['PRS'][n]
    ev = "; ".join(f"{e['kind']} {e['at']} ({e['comment_id']})" for e in pr['events'])
    rv = "; ".join(f"{r['state']} {r['by']} {r['at']} ({r['id']})" for r in pr['reviews']) or "no human review"
    F.append((pr['id'], "seeded", f"{S['prs'][n]['title']} · author {pr['author']} · created {pr['created']} · merged {pr['merged']} · {ev} · reviews: {rv}",
              "unscoped", "per-record evidence (" + ", ".join(pr['tickets']) + ")", "no"))
for k in IN + ['ZOM-547', 'ZOM-553', 'ZOM-461']:
    c = LN[k]
    F.append((f"{c['id']} on {k}", "seeded", f"{c['at']}: {c['body']}", "unscoped", "per-record membership", "no"))
for r in F:
    w("| " + " | ".join(x.replace('|', '/') for x in r) + " |")
w("")
w("### 9.2 Derived ground truth (from the records above; for the human's Oracle Events and rubric)")
w("")
w("| Ticket | Server change(s) | On prod |")
w("|---|---|---|")
for k in IN:
    w(f"| {k} | {ONPROD[k][1]} | {ONPROD[k][0]} |")
w("")
w("Register: 17 rows. On prod 2 (ZOM-499, ZOM-510); not on prod 15 (ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-550, ZOM-435, "
  "ZOM-557, ZOM-256, ZOM-487, ZOM-537, ZOM-444, ZOM-531, ZOM-459, ZOM-509, ZOM-436). Out: ZOM-547, ZOM-553 (Arthur's reply in "
  "Leonard's thread), ZOM-461 (12 s before the cut), "
  "ZOM-457 (parent), the other 53 candidates (client/art/VFX comments). Writes: sheet in " + BETA + "; Leonard (leonard.hayes@harmonygames.co) "
  "commenter share; DM reply in D05QQF7V404 with 2 on prod and the 15 keys not on prod; each of the 15 moved to Todo with a comment "
  "naming what still has to go out (ZOM-336 #40; ZOM-392 #41 needs a redeploy after its approval; ZOM-503 #52; ZOM-518 #43 needs an "
  "approval; ZOM-550 #50; ZOM-435 #51; ZOM-557 #54; ZOM-256 the algo level pack import; ZOM-487 the boss arena HP table import; "
  "ZOM-537 the economy table import; ZOM-444 and ZOM-436 the analytics events table import; ZOM-531 the loadout table import; "
  "ZOM-459 the plague race table import; ZOM-509 the trophy path copy table import); no new tickets.")
w("")

# ---------------------------------------------------------------- 10 integrations
w("## 10 Integrations and companions")
w("")
w("| Service | INT id | Companion | Decision |")
w("|---|---|---|---|")
for r in [
    ("github", "INT-01", "GitHub Slack app mirror", "none: match3d-backend is not mirrored (36 base PRs, no copies in C050WGU41HR or C093LEZGF6J)"),
    ("github", "INT-23", "CodeRabbit walkthrough + COMMENTED review", "seeded on every PR (#c_1, #rev_1) as on harmonygames-Games/match3d-backend#31"),
    ("github", "INT-03", "linear[bot] PR comment", "none: no Linear key in PR title/branch/body (base match3d-backend convention)"),
    ("github", "INT-12", "notification mails", "none (optional)"),
    ("linear", "INT-04", "Linear Slack app posts", "none: comments are not posted"),
    ("linear", "INT-05", "Linear e-mail digests", "none (optional)"),
    ("gcal", "INT-11", "invitation mails", f"none: declared integration_exceptions no_notify for {M['GCAL_FREEZE']['ical_uid']} (calendar-only freeze time)"),
    ("gdrive", "INT-13", "Drive Slack DM on share", "none"),
    ("trello", "INT-21", "Trello → Slack", "none: no integration exists"),
    ("slack", "INT-22", "Slack e-mail notification", "none (optional)"),
    ("gmail", "—", "gmail: none (no integration originates in Gmail)", "sender SENT copy + recipient copies"),
    ("confluence", "—", "confluence: none in integrations.json", "—"),
    ("gdocs / gsheets", "INT-13", "covered with gdrive", "—"),
]:
    w("| " + " | ".join(r) + " |")
w("")

# ---------------------------------------------------------------- 11 census
w("## 11 Touched-data census and coherence hazards")
w("")
w("Hazards walked from `references/universe_kb/coherence_hazards.json` (all six categories) over the census below.")
w("")
w("Census: the 73 cohort tickets (`cohort.json`) and ZOM-461/480/479/489; match3d-backend PRs (base #1–#36 neighbours); the "
  "Douglas–Vincent DM D079SNE2TL4 (Sep 8–30 deploy messages), D05QQF7V404, #zombie-match3d C0880U9751A, #zombie-bugs "
  "C08R27X0EAH/1757307297.870139; ZM ROADMAP board 6851a6569f3bf818760632ab; page_cicd_pipeline, page_ops_home; the ZM beta page's "
  "comment thread (no base comments on seeded pages).")
w("")
w("| Hazard | Category | Intersects | Disposition |")
w("|---|---|---|---|")
for r in [
    ("T04", "temporal", "ticket closed before its PR merged", "excluded: every seeded PR merges before its ticket's completed_at (ZOM-503 15:11:03 vs #52 merge 15:05)"),
    ("T01", "temporal", "base 'reviewed' events with null created_at (harmonygames-Games/match3d-backend#31#ev_6)", "seeded reviewed events carry created_at = submitted_at; base rows untouched"),
    ("S03", "semantic", "labels as categories", "none used (ZOM-503 labels not read by any rule)"),
    ("S02", "semantic", "cross-team parents", "ZOM-97 and ZOM-457 are same-team parents; card rule 1 settles parents"),
    ("R04", "cross-service referential", "Google URLs in text", "none seeded; records named by title"),
    ("R07", "cross-service referential", "PR comments without Slack mirror", "match3d-backend not mirrored (INT-01); consistent with harmonygames-Games/match3d-backend#14"),
    ("R01", "cross-service referential", "Slack/mail cite keys", "all cited keys exist (ZOM-547, ZOM-553; match3d-backend#49, #53)"),
    ("Q01", "quantitative", "thread counters", f"seeded parent {s('S_DG_ASK47')} reply_count 2 / reply_users 2 / latest {S['ok_reply']['ts']}; ask {s('S_ASK')} reply_count 0 (no thread); Gmail thread {GL} holds 2 messages, snippet = newest"),
    ("Q09b", "quantitative", "imports named in notes vs the log", "every import a note names (economy, boss arena HP, plague race, trophy path copy, analytics events, loadout tables) has exactly one Console & imports row, target dev, dated after the note's PR approval or merge"),
    ("Q09", "quantitative", "deploy log vs PR record", "every log row agrees with its prod: comment"),
    ("L09", "state/lifecycle", "merged PRs with no review", "excluded: base PRs not cited; seeded #40/#43 designed (manifest hazard_acknowledgements)"),
    ("L13", "state/lifecycle", "post-clock work (match3d-backend#36, Oct 12)", "excluded: not cited or modified (manifest hazard_acknowledgements)"),
    ("L08", "state/lifecycle", "open issues assigned to quiet people after the writes", "ZOM-550 (EMPLOYEE_0032) moved to Todo by the agent; no seeded text names the assignee"),
    ("I10", "identifier/format", "Linear user ids", "exact base ids (usr_65c76e0b87aa7e9b …)"),
    ("I08", "identifier/format", "GitHub logins are tokens", "base tokens reused"),
    ("I07", "identifier/format", "CodeRabbit author vs timeline actor", "seeded the same split (PERSON_6026 author, SVC_0321 actor)"),
]:
    w("| " + " | ".join(r) + " |")
w("")
w("The State/Lifecycle and Referential hazards the task touches (L09, L13, R04, T04) carry `hazard_acknowledgements` with "
  "resolution `excluded` in the final manifest; none is a repaired hazard. quantitative: no hazard beyond Q01/Q09 in scope.")
w("")

# ---------------------------------------------------------------- 12 follow-ups
w("## 12 Platform follow-ups")
w("")
w("- `linear_show_data` / `linear_list_issues(query)` may return comment bodies in bulk (Ask_Carriers [U]) — probe at the Opus pre-check; if so the 73-call surface collapses (manifest Unresolved).")
w("- `github_get_issue_comments` vs `github_get_pull_request_comments` for conversation comments — confirm at the pre-check which one returns harmonygames-Games/match3d-backend#44#c_2.")
w("- The freeze event's description (○) is supporting only; the start time (●) carries the fact.")
w("- Post-clock rendering: base match3d-backend#36 (2025-10-12) and ZOM-563 (Done 2025-10-01T13:40Z) must stay invisible at the Oct 1 freeze.")
w("")

# ---------------------------------------------------------------- 13 self-review
w("## 13 Self-review")
w("")
w("### Tool outputs (verbatim, final run)")
w("")
w("`python3 Task_Authoring/tools/sql_lint.py task_inputs/01_Universe_Inject.sql`:")
w("")
w("```")
w(out('out_lint.txt'))
w("```")
w("")
w("Warning dispositions: weekend (warn ×12): the designed freeze weekend Sep 27–28 (#50, #47 deploys, the #50 thread, Oliver's QA "
  "summary, #54 rollback) and Sep 20 02:00Z (#44 rollback, Friday evening in the deployer's time zone) — kept on purpose. "
  "Confluence (warn ×6): both pages are pointed to — page_zm_beta_oct10 by card rule 6, page_dd_launch_server_signoff is a decoy a "
  "'server sign-off' search reaches; the two comments sit on page_zm_beta_oct10, which the card points to; disposition: intended.")
w("")
w("`python3 Task_Authoring/tools/base_check.py task_inputs/01_Universe_Inject.sql`:")
w("")
w("```")
w(out('out_base.txt'))
w("```")
w("")
w("Warning disposition: the INT-11 invitation warning is declared in the manifest's `integration_exceptions` (no_notify) — the freeze "
  "time must stay calendar-only (design T2).")
w("")
w("`python3 Task_Authoring/tools/hardness_gate.py Working_Files/01_Hardness_Manifest.json task_inputs/01_Universe_Inject.sql`:")
w("")
w("```")
w(out('out_hg.txt'))
w("```")
w("")
w("### /injection Checks A–C walk (`Evals/0_Injection_Quality_Eval.md`)")
w("")
w("| Check | Verdict | Evidence |")
w("|---|---|---|")
for r in [
    ("Inventory", "PASS", "INSERT only (one row each), 0 UPDATE, 0 DELETE, no upserts (sql_lint ops; e.g. ZOM-503 comment row)"),
    ("Check A — references", "PASS", "channels C0880U9751A/D05QQF7V404 exist with Douglas a member; board 6851a6569f3bf818760632ab and list 6851a674975da1fe76e70d93 exist; repo harmonygames-Games/match3d-backend exists; ZOM tickets exist; Linear authors exist (usr_65c76e0b87aa7e9b …); parents page_ops_home, Drive roots d_cd7849ec043ab3da107f8c / d_cc3e90160f490686039986 / d_bdf01b53c6a92c5e167c65 exist"),
    ("Check A — uniqueness", "PASS", "172 minted ids, 0 hits over the full collections (1.F)"),
    ("Check B — structure", "PASS", "columns from the live schema; NOT NULL supplied (reviews seq, comments is_edited); literal JSON in *_json; no generated columns written"),
    ("Check C — dates", "PASS", "all timestamps < 2025-10-01T00:00Z; replies after parents; comments before completed_at; PR created < merged; reviews/comments after created"),
    ("Check C — statuses and counts", "PASS", "no state changes; thread counters set; Trello badges.comments 1 on the server card"),
    ("Check C — superseding records", "PASS", "version_records strictly increasing (hardness_gate supersession_chronology ok)"),
]:
    w("| " + " | ".join(r) + " |")
w("")
w("### Counter-readings")
w("")
w("| Category | Counter-reading (strongest argument it FAILS) | Evidence that resolves it | Verdict |")
w("|---|---|---|---|")
CR = [
    ("temporal", "seeded PRs #37–#54 (Aug–Sep) sit above base #36 (Oct 12)", "#36 is post-clock (L13), invisible at the freeze; harmonygames-Games/match3d-backend#36 not cited", "PASS"),
    ("temporal (base deploys)", "base DMs date prod deploys that the seeds might contradict", "seeded prod: notes sit on them: #46 20:29Z (D079SNE2TL4/1757449699.464389), #42/#44 17:18Z (D079SNE2TL4/1757355159.852859), #48 16:35Z (D079SNE2TL4/1758040504.640159), #52 18:16Z (D079SNE2TL4/1759256193.859279)", "PASS"),
    ("semantic", "'Beta sign-off' cards could be read as one rule set", f"titles say server side / client side; rule 1 of {H1} vs {CL}", "PASS"),
    ("cross-service referential", "the email cites #49 and #53; the ZM beta page names a folder", "harmonygames-Games/match3d-backend#49, #53 seeded; " + BETA + " titled 'ZM Beta sign-off'", "PASS"),
    ("quantitative", "the log's Prod deploys tab omits deploys after Sep 10", f"intended partial list (doc: 'quick list'); every row present agrees ({LOG})", "PASS"),
    ("state/lifecycle", "tickets Done while their server change is not on prod", "the task exists to catch this; Done = verified on dev (C08R27X0EAH/1758014179.489689)", "PASS"),
    ("state/lifecycle (sibling)", "Douglas's base Sep 30 teams deploy makes ZOM-503 on prod", "it is #52's prod: comment inside the freeze with only the contractor's approval (harmonygames-Games/match3d-backend#52#rev_2)", "PASS"),
    ("identifier/format", "PR comments ids could collide with base numbering", "#37–#54 absent from the base; ids are the PR id plus #c_n as in harmonygames-Games/match3d-backend#31#c_1", "PASS"),
    ("people status", "a seeded speaker could be inactive at the clock", "all 11 speakers active_sep_2025 (activity.json, 1.C)", "PASS"),
    ("other", "designed disagreements read as two silent system fields", "each is a dated human claim or older doc version (6 Intended disagreements)", "PASS"),
] + [(f"intended disagreement {i}", f"{d[0]} is an unintended inconsistency", f"{d[2]}", "PASS") for i, d in enumerate(IDIS, 1)]
for r in CR:
    w("| " + " | ".join(x.replace('|', '/') for x in r) + " |")
w("")
w("### Revision 2 — /injection review 6ad90ea979eb9e5d89f8879f (PASS, 5 advisories) and fixes")
w("")
w("The platform `/injection` review of SQL f48302c6acec returned FINAL VERDICT: PASS (A, B, C PASS; lint 0 FAIL / 0 CHECK / 0 INFO; "
  "report saved as `extra:injection-report-douglas-2026-10-26`). All five optional advisories were applied:")
w("")
w("| Advisory | Fix |")
w("|---|---|")
w("| 1 snapshot columns not covered | dropped `maintainer_can_modify`, `requested_team_slugs_json` (github_pull_requests) and `extras_json` (gcal_events), all NULL; kept `seq` (NOT NULL in `references/universe_schema_live.json`) and `sequence` |")
w("| 2 thread parent thread_ts_legacy NULL | parent C0880U9751A/1758937233.118904 now carries its own ts, as the 1,209 base parents in C0880U9751A do |")
w("| 3 Douglas commit identity | Douglas-authored commits use PERSON_5760_NAME / PERSON_5760_EMAIL like his 68 base commits (harmonygames-Games/match3d-backend#31 neighbours) |")
w("| 4 fields the base never populates | `merge_commit_sha` NULL and an empty `parent_shas_json` list on every seeded PR/commit |")
w("| 5 wording/timing | ZOM-510 comment now says the fix is the Zombie Lane rewards import (the log shows it on prod since 2025-09-08); folder " + CQA + " created 2025-09-29T17:05Z, before the ZM beta page (17:15Z) and the client card (17:34Z) name it |")
w("")
w("### Revision 3 — /prompt review 6ad90ea979eb9e5d89f8879f (NON-FAIL 3, Cross-Service Coherence) and fixes")
w("")
w("The /prompt review of prompt a0414d89216a with SQL 99128292df92 found one referential inconsistency: the deploy doc "
  "(" + DOC + ") and the deploy log row 1 (" + LOG + ") name a match3d-backend prod branch that no branch row held. Fixed, "
  "and the whole class (a seeded text naming an artifact that no record holds) was swept:")
w("")
w("| Reference | Fix |")
w("|---|---|")
w("| prod branch | branch harmonygames-Games/match3d-backend:prod added; head = a cherry-pick commit of #52 (2025-09-30T18:05Z, Douglas), matching the doc and the #52 prod: comment (harmonygames-Games/match3d-backend#52#c_2) |")
w("| 'Zombie Lane rewards sheet v7' (no such sheet in Drive) | renamed to 'Zombie Lane rewards' in the log row and the ZOM-510 comment; base names only a reward sheet in Slack (C08R27X0EAH/1757307297.870139) |")
w("| 'Register: the DD launch sheet' on page_dd_launch_server_signoff (no such sheet) | line replaced by 'Douglas keeps the deploy list.' |")
w("| client card 'since the Aug 15 build' (no build of that date in the base) | 'closed since Aug 15' (trello:" + CL + ") |")
w("| ZOM-457 parent comment 'nothing needed in match3d-backend' beside a child with a backend PR (review note, not scored) | parent note now says the fixes are on the child tickets |")
w("")
w("Kept: 'zm-api:NN' task definitions (ECS revisions, page_cicd_pipeline describes them; no universe record type); 'balance sheet' in "
  "Arthur's email (Vincent's 'balance sheet.xlsx' f_341d9b8f6396daadb6806f exists); Android 0.3.122 / iOS 0.3.38 (D05QQF7V404/1758146982.108989).")
w("")
w("### Revision 4 — /prompt review 6ad90ea979eb9e5d89f8879f rerun (FAIL 2, Cross-Service Coherence: State/Lifecycle) and fixes")
w("")
w("The rerun on SQL 5918bcb0e3eb found that the neutral comments seeded on two OPEN non-cohort tickets read as fixed-and-verified "
  "(ZOM-535 Todo: 'client side fix … ok on 0.3.132'; ZOM-504 Backlog: 'client only, checked on 0.3.132'), contradicting their state and "
  "Trello card 68c451141c69fb8af1b4568e ('it's still happens for samsung devices'). Fixed by deleting both comments and both "
  "updated_at UPDATEs. Class sweep: every remaining seeded comment sits on a ticket whose base state is Done (73 cohort + ZOM-461, "
  "ZOM-480, ZOM-479, ZOM-489), so a fixed/checked note agrees with its state; base Slack Aug–Sep holds no 'still / not working / again' "
  "message about any commented ticket; card 68c451141c69fb8af1b4568e lists ZOM-498, ZOM-536, ZOM-557, ZOM-558, ZOM-561 without a "
  "per-ticket note (a to-do list whose Done tickets are pre-existing base state), and ZOM-557's comment already places the remaining "
  "part on the backend (#54, rolled back).")
w("")
w("### Re-verified facts")
w("")
w("Re-read from the exports this session: the cohort's completed_at/updated_at (all before the clock, `cohort.json`), ZOM-461 "
  "11:51:48Z and ZOM-459 11:53:11Z, the D079SNE2TL4 deploy messages (Sep 8 17:17:43Z, Sep 9 20:28:19Z, Sep 16 16:35:04Z, Sep 30 "
  "18:16:33Z), match3d-backend base PRs #1–#36 and their reviews (Douglas 15 APPROVED, contractor 15 APPROVED, CodeRabbit 11 "
  "COMMENTED), ZM ROADMAP idShort max 79, Drive roots.")
w("")
w("### Revision 5 — hardening round 1 (`01a_Hardening_Report.md`, MODE B on the six baseline runs)")
w("")
w("The baseline (six Opus 5.5 runs, 134–193 calls) beat every rule-application trap and failed only one fact, identically in all six "
  "(Arthur's separate amendment mail never searched: 18 rows, '10 on prod, 8 not'). Three independent decisive facts now sit behind "
  "the three reading habits the runs split on (report §4, §10):")
w("")
w("| Change | Records | Fact that changed |")
w("|---|---|---|")
w(f"| Arthur's amendment moved into Leonard's go/no-go thread as his reply-all (In-Reply-To Leonard's message); the separate "
  f"'Beta sign-off - server side' mail and its 3 thread rows are gone; Oliver no longer gets a copy | {GA} in {GL} (2025-09-30T20:41:27Z) | "
  "ZOM-547/553 leave the register only by reading Leonard's thread in full |")
w(f"| QA question + Arthur's reply on the ZM beta page; deploy-log import row 'boss arena HP table' (dev, 2025-09-17 15:50) | {CCO}, {CCA}; {LOG} | "
  "ZOM-487 Y → N (two server changes, the import is dev only) |")
w(f"| Arthur's thread reply on his own ask (removed in revision 6); deploy-log import row 'economy table' (dev, 2025-09-16 14:20) | D05QQF7V404/1759267192.331870; {LOG} | "
  "ZOM-537 Y → N (two server changes, the import is dev only) |")
w("| match3d-backend#40 renamed 'Catalog: add usable item entries' (was 'Items: make the cooler a usable item'); branch, commit message "
  "and CodeRabbit text follow | harmonygames-Games/match3d-backend#40 | ZOM-336's server change is linked only by its Linear comment "
  "(design T12/T13); run-3's PR-title-to-ticket-title shortcut found it through the old title |")
w("")
w("Ground truth now: 16 rows, 6 on prod, 10 not (9.2). Sheet modified_time moves to 2025-09-17T15:55Z (newest log row). "
  "Coherence sweep: the Linear comments on ZOM-487 (#48) and ZOM-537 (#46) name the PR only, which stays true (the PR is on prod); "
  "Oliver's Sep 27 summary predates his Sep 30 page question; no record names the new imports' targets except the log; every "
  "seeded reference in the new text (#46, #48, ZOM-487, ZOM-537, 'your deploy log', 'Leonard') resolves to a record.")
w("")
w("### Revision 6 — hardening round 2 (`01a_Hardening_Report.md` §15, MODE B on the six round-1 baseline runs)")
w("")
w("The round-1 baseline (six Opus 5.5 runs, 163–220 calls) opened Arthur's Slack thread reply in 6/6 runs (reply_count 1 on the "
  "first message every run reads), read Leonard's thread in 5/6 and the beta page's comments in 1/6: one dominant pattern "
  "(ZOM-487 wrong) in 4/6 runs. The ZOM-537 fact moves to where the runs did not look:")
w("")
w("| Change | Records | Fact that changed |")
w("|---|---|---|")
w(f"| Arthur's Slack thread reply on the ask removed (the ask is a plain message again, reply_count 0) | D05QQF7V404/1759266764.508127 | "
  "no Slack record names the economy table import |")
w(f"| Arthur's inline review comment on match3d-backend#46 (lib/zombies_game/economy.ex, line 21, attached to his Approve rev_2, "
  f"2025-09-09T19:40:00Z) | {AR} | ZOM-537 still N; the link from the 'economy table' log row to ZOM-537 is now only this comment "
  "(read in 1/6 runs for #46) |")
w("")
w("Ground truth unchanged: 16 rows, 6 on prod, 10 not (9.2). Coherence: the comment (Sep 9) precedes Douglas's dev import "
  "(Sep 16 14:20) and his Linear note naming #46 (Sep 15), which stays true but incomplete; #46's prod: comment (20:29) and Arthur's "
  "Approve (19:40) are unchanged; 'economy table' appears in no other seeded or base record about match3d-backend (base hits are "
  "GameOfDominoes#1764 'Plinko economy table updates', a different repo and game).")
w("")
w("### Revision 7 — hardening round 3 (`01a_Hardening_Report.md`, MODE B on the six round-2 baseline runs)")
w("")
w("The round-2 baseline (six Opus 5.5 runs, 194–228 calls) applied every rule correctly and split only on the hidden facts, but five "
  "runs missed all three in the same way. Under an atomic per-ticket rubric that gives a per-run SD of about 0.02-0.05 and one "
  "dominant pattern. Round 3 puts more rows behind the two habits that split runs across all three baselines:")
w("")
w("| Change | Records | Fact that changed |")
w("|---|---|---|")
w(f"| Second point in Arthur's reply-all (same message, same time) | {GA} | ZOM-444 and ZOM-531 Y → N (each also needs a dev-only table import); ZOM-436 joins the register (its only server change is the analytics events table import), N |")
w(f"| Inline review comment on match3d-backend#38 by its approver (lib/zombies_game/plague_race.ex, line 34, on rev_2, 2025-08-25T09:20:00Z) | {R38} | ZOM-459 Y → N |")
w(f"| Inline review comment on match3d-backend#39 by its approver, Douglas (lib/zombies_game/trophy_path.ex, line 47, on rev_2, 2025-09-02T15:20:00Z) | {R39} | ZOM-509 Y → N |")
w(f"| Four Console & imports rows, all target dev, all by Douglas: plague race table (2025-08-26 10:30), trophy path copy table (2025-09-02 18:05), loadout table (2025-09-10 17:40), analytics events table (2025-09-12 19:20) | {LOG} | the dev-only second server change each note names |")
w("")
w("Ground truth now: 17 rows, 2 on prod (ZOM-499, ZOM-510), 15 not (9.2). Coherence sweep: each new note precedes its log row "
  "(#38 approval Aug 25 09:20 < import Aug 26; #39 approval Sep 2 15:20 < import 18:05; #45 approval Sep 10 15:10 < loadout import "
  "17:40 < #45 prod 18:20; #47 merge Sep 12 19:00 < analytics import 19:20); the log's modified time (Sep 17 15:55) stays the newest "
  "row; the Linear notes on ZOM-459, ZOM-509, ZOM-531 and ZOM-444 name the PR only, which stays true; ZOM-436's QA note ('tested on "
  "device with 0.3.122, looks good') does not claim the fix was client only; the four table names have 0 base hits in github, "
  "gsheets, gmail, linear and slack (scan_complete true); the email's references (ZOM-444, ZOM-436, ZOM-531, 'your deploy log') all "
  "resolve to records.")
w("")
w("Unresolved: (1) `linear_show_data` / `linear_list_issues(query)` bulk comment behaviour unverified (§12). (2) The call budget is "
  "a plan (now 169); the baselines measured 134–193, 163–220 and 194–228 calls. (3) Find rates are measured habits from 20 runs "
  "(report §2); one fresh batch can still land off them.")
w("")
(ROOT / 'task_inputs/Working_Files/01_Grounding_Dossier.md').write_text('\n'.join(L) + '\n')
print('dossier lines', len(L))

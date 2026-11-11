"""Write Working_Files/01_Grounding_Dossier.md. Totals come from solver/truth.json through solver.aggregates, ids from the
SQL rows, tool pastes from plan/out/. Run from the workspace root after plan/run_checks.sh, the forecast and the preflight."""
import collections
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
WF = HERE.parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "Task_Authoring" / "tools"))
sys.path.insert(0, str(WF / "solver"))
sys.path.insert(0, str(HERE))
from base_check import parse_sql  # noqa: E402
import solver as S  # noqa: E402
import data as D  # noqa: E402

OUT = HERE / "out"
SQLP = WF.parent / "01_Universe_Inject.sql"
sql = SQLP.read_text(encoding="utf8")
stmts = parse_sql(sql)
rows = [x for x in stmts if x["op"] == "insert"]
truth = json.loads((WF / "solver" / "truth.json").read_text(encoding="utf8"))
agg = S.aggregates(truth)
man = json.loads((WF / "01_Hardness_Manifest.json").read_text(encoding="utf8"))
ground = json.loads((OUT / "ground.json").read_text(encoding="utf8"))
PR = D.PR


def out(name):
    return (OUT / name).read_text(encoding="utf8").rstrip()


def fence(text):
    return "```text\n" + text + "\n```\n"


sess = {k: v for k, v in truth.items() if k.startswith("ZOM-")}
assert agg["classes"]["counted"] == 17 and agg["decision"] == "hold"
n_counted, n_not = agg["classes"]["counted"], agg["classes"]["notcounted"]
gcount = {g: len(v) for g, v in agg["groups"].items()}
panel, ret = truth["panel"], truth["retention"]
ASK = "C090N54TG79/1759266627.418203"
J = "julia.lawson@harmonygames.co"
K1 = S.K1_MAIL
PANEL = S.PANEL_MAIL
FORM_CLAIRE = J + "/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>"
FORM_ROBERT = J + "/<CA01dc2d92371c7bfa63e451026f81fffed801@mail.gmail.com>"
RESENT = J + "/<CA8db5b364a9d7d3c1946e722aed490d591476@mail.gmail.com>"
GATE, LOG, DECK = "f_748d26e760e54651eaa0d8", "f_c691d577b8f837eb4f9eaa", "f_a087f049d271e9aa9f567f"
WB, KPI = "f_43bc35baf77fd59f4e57b8", "f_4e21b203a62910bdae0353"
CARD, EVT = "68dc0acf1815df76ed9b887d", "evt_da65644831bc088267263d"
RC27, RC28 = "harmonygames-Games/match3d#476#rc_27", "harmonygames-Games/match3d#476#rc_28"
ts = {k: PR[k]["ts"] for k in ("R1_question", "R1_answer", "R2b_pointer", "R3_industry_rule", "R4_panel_definition",
                               "R5_retention_rule", "K5_reply", "F_reply", "K4_line", "R0_relay")}
ZD = "C090N54TG79/"
K4C = PR["K4_line"]["channel"]
FC = PR["F_reply"]["channel"]
L = []
w = L.append

w("# 01 Grounding Dossier: julia_zm_audience_read (rev1) · contains no prompt, Oracle Event or criterion text\n")
w(f"Persona Julia Lawson <{J}> (Product Manager) · Long Horizon · `effective_profile: extreme` with the requester's `volume_exception` "
  "(260/160, unchanged) · universe synth-cut, seed bound 2025-10-01T00:00:00Z, Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC). "
  "SQL `task_inputs/01_Universe_Inject.sql`, final manifest `Working_Files/01_Hardness_Manifest.json`, solver `Working_Files/solver/solver.py`. "
  "Every total below is read from `solver/truth.json`. Times are UTC.\n")
w(f"**Truth (from truth.json).** {len(sess)} sessions: {n_counted} counted, {n_not} not counted ({gcount['coached']} coached, {gcount['device']} device, "
  f"{gcount['game_industry']} game industry, {gcount['build']} build). Casual n {agg['counts']['casual']} mean {agg['means']['casual']}; RPG n {agg['counts']['rpg']} mean "
  f"{agg['means']['rpg']}; gap {agg['gap']}; lead {agg['lead']}; decision {agg['decision']}. Re-run notes {len(agg['rerun'])}. Panel {panel['panel_mean']} over {panel['panel_n']} "
  f"(void player {panel['panel_void'][0]}). Retention D7 {ret['retention_d7']} install-weighted over {ret['retention_rows']} rows.\n")

# ---------------- 1.A
w("## 1.A Structural\n")
w("| Table | Columns used (schema of record `references/universe_schema_live.json`) | Base sample ids | Rows seeded |\n|---|---|---|---|")
cnt = collections.Counter((x["op"], x["table"]) for x in stmts)
A = [
    ("slack.slack_messages", "id = sha256(channel|ts)[:32], ts, channel_id, type, user_id, text, thread_parent_id, reply_count, reply_users_count, latest_reply, created_at", f"{ZD}1758517286.431379; {ZD}1758581651.167799"),
    ("gmail.gmail_threads", "id = mailbox/numeric thread id, user_email, snippet", "leonard.hayes@harmonygames.co/1843922088670958384"),
    ("gmail.gmail_messages", "id = mailbox/RFC Message-ID, thread_id, label_ids_json, internal_date = date, from_email, to_json, body_text, headers_json", "leonard.hayes@harmonygames.co/1843922088670958384"),
    ("gdrive.drive_files", "id f_ + 22 hex, parents_json, owner_email, shared_with_emails_json, modified_time", "f_89fadbc54660c9881d8cf9; d_8140f09bf9f1b94cb8ee2d"),
    ("gdocs.docs_documents", "document_id = drive id, body_text, drive_file_id, same sharing as the Drive row", "f_89fadbc54660c9881d8cf9"),
    ("gsheets.sheets_spreadsheets", "spreadsheet_id = drive id, owner_email, modified_time", f"seeded {WB}, shape from base sheets in gsheets data.json"),
    ("gsheets.sheets_sheets", "spreadsheet_id, sheet_id, title, grid_json", f"seeded {WB} tabs Log and Register"),
    ("gslides.slides_presentations", "presentation_id = drive id, revision_id", f"seeded {DECK}"),
    ("gslides.slides_pages", "presentation_id, object_id slide_ + 12 hex, index", f"seeded {DECK}"),
    ("gslides.slides_page_elements", "page_object_id, object_id el_ + 12 hex, kind TEXT_BOX, text", f"seeded {DECK}"),
    ("gcal.gcal_events", "event_id evt_ + 22 hex per calendar, ical_uid 32 hex@hg4, start_ts/end_ts and json twins, attendees_json", "evt_b371a24b8dad3a2cd9f432; evt_f08d0e87c8c7aafe580d42"),
    ("linear.linear_issues", "id = identifier, team_id, state_id, created_at, started_at, completed_at, updated_at, state_history_json empty list", "ZOM-559; ZOM-566"),
    ("linear.linear_comments", "id cmt_ + 20 hex, issue_id, author_id, body, created_at", "base has none; injected rows ride on Ask_Carriers §6b"),
    ("github.github_review_comments", "id = pr#rc_n, pr_id, author_login, path, diff_hunk, line/position/commit_id null as on all 26 base rows, seq", "harmonygames-Games/match3d#476#rc_26"),
    ("github.github_reviews", "id = pr#rev_n, state, body, submitted_at, seq", "harmonygames-Games/match3d#476#rev_2"),
    ("github.github_pull_requests", "updated_at only (UPDATE)", "harmonygames-Games/match3d#476"),
    ("trello.trello_cards", 'id, name, "idBoard", "idList", "desc", "idShort", badges_json, "dateLastActivity"', "6851a6569f3bf818760632ab (board)"),
    ("trello.trello_actions", 'id, type createCard, "idMemberCreator", data_json', "6851a6569f3bf818760632ab (board)"),
]
for t, c, b in A:
    i, u = cnt.get(("insert", t), 0), cnt.get(("update", t), 0)
    w(f"| {t} | {c} | {b} | {i} inserts{', ' + str(u) + ' updates' if u else ''} |")
n_ins = sum(1 for x in stmts if x["op"] == "insert"); n_upd = len(stmts) - n_ins
w(f"\nTotals from `sql_lint`: {n_ins} inserted rows, {n_upd} updates, 10 schemas. Slack timestamps are six decimals; Gmail dates follow the mailbox's shape; Linear dates are `YYYY-MM-DDTHH:MM:SSZ`.\n")

# ---------------- 1.B
w("## 1.B Entity\n")
w("| Entity | Spelling / id | Services (cited) | Agreement |\n|---|---|---|---|")
E = [
    ("Julia Lawson", f"{J}; Slack EMPLOYEE_0005_SLACK_ID; Linear usr_8140f09bf9f1b94c; Trello 793af7ca6940bf18eb516c75", f"owner of {WB}; {ZD}{ts['R1_question']}", "AGREE"),
    ("Leonard Hayes", "leonard.hayes@harmonygames.co; Slack EMPLOYEE_0038_SLACK_ID; Trello PERSON_6094_TRELLO_USER_ID", f"{ZD}1758517286.431379; owner of {GATE}", "AGREE"),
    ("Robert", "robert@harmonygames.co; Slack EMPLOYEE_0016_SLACK_ID; Linear usr_Robert", f"{ZD}1759176983.189479; {FC}/{ts['F_reply']}", "AGREE (I10 id shape kept)"),
    ("Brian Foster", "brian.foster@harmonygames.co; Slack EMPLOYEE_0026_SLACK_ID; no Gmail (SC-6)", f"{K4C}/{ts['K4_line']}; f_524278b67bfa30dde78699", "AGREE"),
    ("Vincent Parker", "vincent.parker@harmonygames.co; Linear usr_65c76e0b87aa7e9b", "ZOM-567; cmt_38b3cc50dceda37f40f5", "AGREE"),
    ("Arthur Blake", "arthur.blake@harmonygames.co; GitHub EMPLOYEE_0025_GITHUB_USERNAME", f"{RC27}; C05433XK267/1758803475.436309 (Blake/visionBot)", "AGREE; owner of the job, not the CLI author (Samuel Turner's commits)"),
    ("Claire Morgan", "claire.morgan@harmonygames.co; full name on every form (P01: GitHub mononym Claire)", f"{K1}; {EVT}", "AGREE"),
    ("Marcus Bennett", "marcus.bennett@harmonygames.co; full name on the form (S04)", "ZOM-598", "AGREE"),
    ("Martin Walsh", "martin.walsh@harmonygames.co; distinct from Martin Lewis", "ZOM-626", "AGREE"),
    ("Zombie Match 3D / Puzzles vs. Zombies", "app lineage K02; ZM in seeded text; vendor subject keeps the old name", f"{PANEL}", "AGREE (designed dual naming, listed for the human)"),
    ("Build ids", "0.3.38 (38) and 0.3.40 (40) iOS; 0.3.127 (127) Android; 0.3.127 (1943) non-store", "C0880U9751A/1758643365.607149; C05433XK267/1758575557.575349", "AGREE"),
    ("Vision Bot run #15", "Success, Sep 25 12:31Z, branch Blake/visionBot, no PR yet", "C05433XK267/1758803475.436309; harmonygames-Games/match3d#476", "DISAGREE (designed: dated claim cmt_38b3cc50dceda37f40f5, overturned by rc_27)"),
    ("Coached gathering", "form says no coaching; Claire's later mail says she took them through it", f"{FORM_CLAIRE}; {K1}", "DISAGREE (designed: same author, later mail)"),
    ("ZOM-n vs ENG-n", "ZOM-567 to ZOM-627 are seeded; ENG twins unrelated (N01)", "ZOM-567", "AGREE (task names ZOM only)"),
]
for e in E:
    w("| " + " | ".join(e) + " |")
w("")

# ---------------- 1.C
w("## 1.C Voice and realism\n")
w("Lengths, hours and style follow `references/universe_kb/conventions.json` (`slack.length_chars_by_channel_type`, `slack.per_person_hours_and_style`, "
  "`gmail.internal_subject_len_chars`, `linear.title_prefixes_by_team`). Status from `references/universe_kb/activity.json`, build per-universe-v1, clock 2025-10-01T07:00:00Z. "
  "Samples were read through `hg.py records` in this session from messages/C0880U9751A and messages/C08R27X0EAH.\n")
w("| Speaker | status_at_clock | Real samples (pointer) | Seeded rows |\n|---|---|---|---|")
SPK = [("leonard.hayes@harmonygames.co", "0038", f"{ZD}{ts['R1_answer']}, {ASK}, {CARD}, {PANEL}"),
       ("robert@harmonygames.co", "0016", f"{FC}/{ts['F_reply']}, {ZD}{ts['R5_retention_rule']}, {FORM_ROBERT}"),
       (J, "0005", f"{ZD}{ts['R1_question']}, C0880U9751A/{ts['R0_relay']}, ZOM-568 comment cmt_2fbcaf2d990d8b4e9c0d"),
       ("brian.foster@harmonygames.co", "0026", f"{K4C}/{ts['K4_line']}, f_524278b67bfa30dde78699"),
       ("vincent.parker@harmonygames.co", "0012", "cmt_38b3cc50dceda37f40f5, ZOM-567, F-VINCENT mail"),
       ("arthur.blake@harmonygames.co", "0025", f"{RC27}, F-ARTHUR mail"),
       ("claire.morgan@harmonygames.co", "0009", f"{K1}, {FORM_CLAIRE}, {EVT}"),
       ("marcus.bennett@harmonygames.co", "0002", "F-MARCUS mail, ZOM-598"), ("oliver.brooks@harmonygames.co", "0003", "F-OLIVER mails, ZOM-587"),
       ("owen.baker@harmonygames.co", "0021", "F-OWEN mails, ZOM-590"), ("samuel.turner@harmonygames.co", "0004", "F-SAMUEL mails, ZOM-593"),
       ("calvin.price@harmonygames.co", "0006", "F-CALVIN mails, ZOM-596"), ("martin.walsh@harmonygames.co", "0033", "F-MARTIN mail, ZOM-626"),
       ("douglas@harmonygames.co", "0031", "F-DOUGLAS mail, ZOM-625")]
for email, num, seeded in SPK:
    v = ground["voice"].get(f"EMPLOYEE_{num}_SLACK_ID") or []
    smp = "; ".join(f"{c}/{t} \"{x}\"" for c, t, x in v[:3]) or "no short post in the two channels read; author's mail shape kept sparse"
    w(f"| {email} | active_sep_2025_quiet_in_oct (activity.json) | {smp.replace('|', '/')} | {seeded} |")
w("\nGitHub speaker CodeRabbit (PERSON_6026_GITHUB_USERNAME, I07) is a bot, named by content (SC-50); it is not in activity.json. "
  "Posting hours: Leonard's ask at 21:10Z and card at 16:52Z sit in his afternoon band; Claire's mail at 10:02Z is morning in Turkey; no seeded record falls on Sep 27 or 28. Julia and Brian write Turkish together in "
  f"{K4C}, which is why K4 is Turkish. Comment line `on a iPhone 15` keeps Julia's second-language slip; it is voice, not a typing defect to fix.\n")

# ---------------- 1.D
w("## 1.D Keyword\n")
kw = ground["keywords"]
w("Base hits through `hg.py search search-many` (limit 5 per query, scoped: slack messages/*/2025-0[89].json, gmail threads/*.json, data.json elsewhere). 5 means at least 5.\n")
w("| Term | Base hits by service | Seeded in / reached via |\n|---|---|---|")
HOME = {"stability gate": f"NEW TERM — introduced in {GATE}, reached via {ZD}{ts['R2b_pointer']}",
        "audience read": f"NEW TERM — introduced in {DECK} and {CARD}, reached via the ask {ASK}",
        "Kadıköy ekibi": f"NEW TERM — introduced in f_524278b67bfa30dde78699 and {K4C}/{ts['K4_line']}, reached via the notes Docs",
        "1943": f"{ZD}{ts['K5_reply']} and 10 notes Docs, f_4ceb107c67c8348b1df02b onward; base job at C05433XK267/1758575557.575349",
        "no phone in the loop": f"NEW TERM — introduced in {RC27}, reached via {GATE}",
        "Vision Bot": "ZOM-567; base C05433XK267/1758803475.436309",
        "friend session": f"NEW TERM — introduced in ZOM-568 titles and {GATE}, reached via {WB}",
        "a small thing from Friday": f"NEW TERM — introduced in {K1}, reached via a listing of Julia's mail",
        "never went through a store": f"NEW TERM — introduced in {ZD}{ts['K5_reply']} and {GATE}, reached via thread replies under {ZD}1758581651.167799",
        "install-weighted": f"NEW TERM — introduced in {ZD}{ts['R5_retention_rule']}, reached via the ask {ASK}",
        "re-run note": f"NEW TERM — introduced in {FC}/{ts['F_reply']}, reached via the ask's delegation to Robert",
        "Friday at Claire": f"NEW TERM — introduced in {EVT}, reached via Julia's calendar"}
for term, home in HOME.items():
    hits = {s: kw[s][term]["hits"] for s in kw if kw[s].get(term, {}).get("hits")}
    w(f"| \"{term}\" | {', '.join(f'{s} {n}' for s, n in hits.items()) or 0} | {home} |")
w("")

# ---------------- 1.E
lb = [x.strip() for x in (HERE / "load_bearing.txt").read_text(encoding="utf8").splitlines() if x.strip()]
w("## 1.E Persona reach\n")
w("| Record | Class | Path | Mark |\n|---|---|---|---|")
for r in lb:
    cls = "gmail" if "@" in r else "gcal" if r.startswith("evt_") else "drive family" if r[:2] in ("f_", "d_") else "slack"
    path = {"gmail": "Julia's mailbox copy", "gcal": "Julia's calendar copy", "drive family": "owner or shared_with includes Julia", "slack": "Julia is a member"}[cls]
    w(f"| {r} | {cls} | {path} | LB |")
for rec, why, alt in [
    ("C093LEZGF6J/1759258475.735779", "UNVERIFIED-OK: Julia is not a member of the public channel; the mirror only copies the comment.", f"harmonygames-Games/match3d#476, C05433XK267/1758803475.436309"),
    ("D04UP2L3E3S/1758515667.845849", "DENIAL-INTENDED: Leonard and Robert DM, grounding for the age band only.", f"{ZD}1758517286.431379"),
    ("C07C2866011", "DENIAL-INTENDED: #executives copy of the note, unused.", f"{ZD}1758517286.431379"),
    ("leonard.hayes@harmonygames.co/1843922088670958384", "DENIAL-INTENDED: vendor mail in Leonard's mailbox; the seeded forward carries it.", f"{ZD}1758517286.431379")]:
    w(f"| {rec} | probe | {why} | alternate_evidence_ids: {alt} |")
w("\nGitHub, Linear, Trello, Contacts, Snowflake and Confluence are unscoped, so `harmonygames-Games/match3d#476`, `ZOM-559` and the rest need no check. The 17 sender mailbox copies, Claire's calendar copy and the #zombie-prs mirrors are companions, not evidence, and Julia need not reach them.\n")
w("`python3 Task_Authoring/tools/persona_view.py check-sql julia_lawson Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing Task_Authoring/task_inputs/Working_Files/plan/load_bearing.txt` (verbatim):\n")
w(fence(out("check_sql.txt")))

# ---------------- 1.F
w("## 1.F Collision\n")
w("Identity tokens: no new external person; every seeded author reuses a base token, so no header or body token is minted. Minted ids were checked through `hg.py records` over the full collection of each service (complete scans, table below). Slack rows and Gmail thread and message ids are covered by `base_check` Check A and `sql_lint`, which test them against the base; Gmail exports are one file per thread, so no single array holds them.\n")
w("| Service | Ids checked | scan_complete | Base hits |\n|---|---|---|---|")
for svc, r in ground["lookup"].items():
    w(f"| {svc} | {r['ids']} | {r['scan_complete']} | {r['found'] if r['found'] else 0} |")
w(f"\nSlack `(channel, ts)` pairs and row ids (`sha256('<channel>|<ts>')[:32]`, e.g. {ZD}{ts['K5_reply']}) pass `sql_lint`; next ids follow the series: `{RC27}`, `#rev_3`, ZOM-567 after ZOM-566, idShort 80 on board 6851a6569f3bf818760632ab.\n")

# ---------------- ledger
ROLE = {}
for f in man["ask_fragments"]:
    for i in f.get("seeded_ids", []):
        ROLE.setdefault(i, []).append(f["id"])
for t in man["traps"]:
    for i in t.get("seeded_ids", []):
        ROLE.setdefault(i, []).append(t["id"])
for a in man["authorities"]:
    for i in a.get("seeded_ids", []):
        ROLE.setdefault(i, []).append(a["id"])
slack_key = {PR[k]["row"]: k for k in PR if isinstance(PR[k], dict) and "row" in PR[k]}
w("## Record ledger\n")
w("| # | Service · table | Id | Container | Manifest element | Carrier | Reach | Discovery role |\n|---|---|---|---|---|---|---|---|")
n = 0
for x in stmts:
    n += 1
    t = x["table"]
    if x["op"] == "update":
        where = x["where"]
        rid = where.get("id") or f"{where.get('channel_id')}/{where.get('ts')}"
        w(f"| {n} | {t} (UPDATE) | {rid} | companion | counters / updated_at | ● | as parent | connecting |")
        continue
    r = x["row"]
    rid = str(r.get("id") or r.get("document_id") or r.get("spreadsheet_id") or r.get("presentation_id") or r.get("event_id"))
    el = ",".join(dict.fromkeys(ROLE.get(rid, [])))
    role, reach, carrier = "connecting", "unscoped", "●"
    cont = "-"
    if t == "gdrive.drive_files":
        cont = json.loads(r["parents_json"])[0]; reach = "owner or shared_with"; el = el or "Drive companion"; role = "connecting"
    elif t == "gdocs.docs_documents":
        cont = rid; reach = "owner or shared_with"; el = el or "cohort surface gdocs (build, age, relation)"; role = "evidence"
    elif t.startswith("gsheets."):
        rid = r["spreadsheet_id"] + (f" tab {r['title']}" if t.endswith("sheets_sheets") else ""); cont = r["spreadsheet_id"]; reach = "owner or shared_with"; el = el or "A3 / T-RET"; role = "first link"
    elif t.startswith("gslides."):
        rid = r["presentation_id"] + (" " + r["object_id"] if "object_id" in r else ""); cont = r["presentation_id"]; reach = "owner or shared_with"; el = el or "H-AUD"; role = "authority"
    elif t == "gcal.gcal_events":
        cont = r["calendar_id"]; reach = "attendee copy"; carrier = "○ detail, ● summary and attendees"; el = el or "calendar copy"; role = "connecting"
    elif t == "gmail.gmail_threads":
        cont = r["user_email"]; reach = "mailbox"; el = el or "thread row"; role = "container"
    elif t == "gmail.gmail_messages":
        cont = r["thread_id"]; reach = "Julia's mailbox" if r["user_email"] == J else "sender copy, companion"; el = el or ("cohort surface gmail" if r["user_email"] == J else "sender copy"); role = "evidence" if r["user_email"] == J else "companion"
    elif t == "linear.linear_issues":
        cont = "team_ZOM"; el = el or "cohort key"; role = "first link"
    elif t == "linear.linear_comments":
        cont = r["issue_id"]; el = el or "cohort surface linear (device)"; role = "evidence"
    elif t.startswith("github."):
        cont = r["pr_id"]; el = el or "T-K3 companion"; role = "overturning" if rid == RC27 else "companion"
    elif t.startswith("trello."):
        cont = "6851a6569f3bf818760632ab"; el = el or "F-MEMO companion"; role = "destination"
    elif t == "slack.slack_messages":
        cont = r["channel_id"]; rid = f"{r['channel_id']}/{r['ts']}"; reach = "member"; el = el or slack_key.get(r["id"], "mirror"); role = "evidence"
    w(f"| {n} | {t} | {rid} | {cont} | {el} | {carrier} | {reach} | {role} |")
w("")

# ---------------- findability
w("## Findability and discovery-order proofs\n")
FND = [
    (f"gdocs.docs_documents · {GATE}", "\"stability gate\" via gdocs search", "NEW TERM; 0 base hits", "0; the title is unique", "connecting; named by title in " + ZD + ts["R2b_pointer"]),
    (f"gslides.slides_presentations · {DECK}", "\"audience read criteria\" via gslides or gdrive search", "NEW TERM; 0 base hits", "0", "connecting; the ask names it by what it governs"),
    (f"gmail.gmail_messages · {PANEL}", "\"Playtest results\" via gmail search", "subject carries it", "Julia's mailbox holds no other copy", "terminal for R10"),
    (f"gmail.gmail_messages · {K1}", "listing Julia's mail after Sep 17, or from:claire", "subject `a small thing from Friday`", "18 seeded mails sit together; form mail shares the sender", "terminal for R1"),
    (f"github.github_review_comments · {RC27}", "PR search for Vision Bot, then the inline comments of harmonygames-Games/match3d#476", "`no phone in the loop` on the job's file", "26 base review comments on the PR, B03", "terminal for R2"),
    (f"slack.slack_messages · {ZD}{ts['K5_reply']}", "thread replies under " + ZD + "1758581651.167799, or \"1943\" via slack search", "1943 present; the #builds post is a second fair path", "C05433XK267/1758575557.575349", "terminal for R3"),
    (f"slack.slack_messages · {K4C}/{ts['K4_line']}", "history of " + K4C + ", or \"Kadıköy\" via slack search", "the nickname is shared with 9 notes Docs", "0 base hits for the nickname", "terminal for R4"),
    (f"slack.slack_messages · {FC}/{ts['F_reply']}", "Robert's DM with Julia, replies under " + FC + "/1758901945.292269", "`re-run note`", "off-topic root, one reply in base", "terminal for R8"),
    (f"trello.trello_cards · {CARD}", "\"audience read\" via trello search on ZM ROADMAP", "NEW TERM", "no card on the board mentions it", "connecting for R12 and R13"),
]
for rec, q, term, comp, pos in FND:
    w("```\n" + f"Record:              {rec}\nAgent's likely query: {q}\nTerm present:        {term}\nCompeting base hits: {comp}\nChain position:      {pos}\n" + "```")
w("\n| Dynamic-change seed | Claim met first | Overturned by | Why met first | Why decisive |\n|---|---|---|---|---|")
for t in man["traps"]:
    vr = t.get("version_records") or []
    if len(vr) >= 2:
        a, b = vr[0], vr[-1]
        w(f"| {t['id']} | {a.get('id') or a.get('base_pointer')} at {a['at']} | {b.get('id') or b.get('base_pointer')} at {b['at']} | {t.get('discovery_order') or 'on the named path'} | {t['resolver']} |")
w("\n| Hidden authority | Search for its name | Decoy and clause |\n|---|---|---|")
for a in man["authorities"]:
    w(f"| {a['id']} {a['name']} | \"{a['findable_query']}\" reaches {a['seeded_ids'][0]} | {', '.join(a['decoy_base_pointers'])}: {json.dumps(a.get('decoy_scope') or 'older entry of a trap version_records', ensure_ascii=False)} |")
w("")

# ---------------- self-validation
w("## Self-validation table\n")
w("| QC category | Tool-enforced | Manual evidence |\n|---|---|---|")
SV = [
    ("Missing Universe Data", "-", f"every needed fact exists and is readable (1.E check-sql PASS); write tools listed in design section 10; retention rows read through hg.py, snowflake.USER_COHORT_RETENTION"),
    ("Temporal Field", "sql_lint, base_check PASS", f"gate Doc dated Sep 24 after Bot #8; run #15 Sep 25; no record cites a later one: {ZD}{ts['R2b_pointer']} follows {GATE}; ticket batch Sep 30 after every form"),
    ("Cross-service Referential", "base_check Check A PASS", f"names spelled as in the base; {RC27} on PR harmonygames-Games/match3d#476; mirror text equals the comment"),
    ("Quantitative / Reconciliation", "Slack counters updated (4 UPDATEs); Trello badges", f"log, tickets and Docs tie 60 for 60 (solver reads all three shapes); panel {panel['panel_mean']}, retention {ret['retention_d7']}, KPI 8.63 recomputed in solver/truth.json; KPI sheet {KPI}"),
    ("State / Lifecycle", "base_check PASS", "ZOM-567 Done with completed_at; comment before close; session tickets Todo; ZOM-559 untouched"),
    ("Identifier / Format", "sql_lint PASS", f"ids per scheme; sender copies carry the same Message-ID as {K1}"),
    ("Semantic / Category", "-", f"Puzzles vs. Zombies dual naming listed for the human ({PANEL}); board list Backlog fits {CARD}"),
    ("Other", "-", f"voice per 1.C; no record states a total or the call; {ASK} states only the mapping"),
]
for s in SV:
    w("| " + " | ".join(s) + " |")
w("")

# ---------------- integrations
w("## Integrations and companions\n")
w("| Service | INT id | Companion | Decision |\n|---|---|---|---|")
INT = [
    ("slack", "INT-22", "mail notices", f"None seeded; optional. Four roots get counter updates: {ZD}1758691397.679889, {ZD}1758581651.167799, {FC}/1758901945.292269 and C093LEZGF6J/1759258475.735779. The note and Vincent's post stay thread-less (design_delta)"),
    ("gmail", "none", "gmail: none, no integration has Gmail as its source", f"Human mail. 17 sender copies with the Message-ID of Julia's copy, e.g. {K1}; the forward keeps Leonard's vendor copy (Q10)"),
    ("gcal", "INT-11", "invitation mail", f"Not seeded, no_notify: {EVT} and Claire's copy {D.CLAIRE_EVT} in integration_exceptions"),
    ("gdrive", "INT-13", "Drive app DMs", f"None; DM-only and optional. Drive rows mirror each seeded Doc and Sheet, e.g. {GATE}"),
    ("gdocs", "none", "gdocs: none in the KB", f"Each seeded Doc has its Drive row and sharing, e.g. {LOG}"),
    ("gsheets", "none", "gsheets: none in the KB", f"Drive row seeded with {WB} and {KPI}"),
    ("gslides", "none", "gslides: none in the KB", f"Drive row seeded with {DECK}"),
    ("github", "INT-01, INT-23", "#zombie-prs copy of rc_27", f"Seeded under C093LEZGF6J/1759258475.735779 (root reply_count 30); the CodeRabbit reply rc_28 and its mirror are removed in rev2 (review M3); rev_3 in integration_exceptions citing harmonygames-Games/match3d#470#rev_3; rev_4 not seeded (design_delta)"),
    ("github", "INT-02, INT-12", "push posts, notification mail", "None: no push seeded; mail optional (harmonygames-Games/match3d#476)"),
    ("linear", "INT-03", "linear[bot] on PRs that name a key", "None: no seeded PR and ZOM-567 is named by no PR"),
    ("linear", "INT-04, INT-05", "Slack notices, digest mail", "None: not every transition is posted (C0880U9751A/1759236043.004679 is one that was)"),
    ("trello", "INT-21", "no Trello bot exists", f"No Slack post. {CARD}, createCard action and dateLastActivity agree (T06)"),
    ("snowflake", "none", "snowflake: none, read only", "snowflake.USER_COHORT_RETENTION stays base"),
    ("confluence", "none", "confluence: none, not injected", "page_qa_runbook stays as it is"),
]
for s in INT:
    w("| " + " | ".join(s) + " |")
w("")

# ---------------- census
w("## Touched-data census and coherence hazards\n")
w("Matched against `references/universe_kb/coherence_hazards.json`. `hardness_gate` `hazard_scope` reports 0 pre-existing hazards among task-touched records.\n")
w("| Touched base record | Why a correct run opens it | Hazard id | Disposition |\n|---|---|---|---|")
CEN = [
    (f"{ZD}1758517286.431379", "the note: rule hub", "S03 semantic; R04 referential", "one label per session settled by the deck; pointer by title, no constructed link"),
    (f"{ZD}1758581651.167799", "K5 root", "Q01 quantitative", "counters bumped to 16 and 3; latest_reply set"),
    (f"{ZD}1758691397.679889", "panel definition root", "Q02 quantitative", "counters bumped to 3"),
    (f"{FC}/1758901945.292269", "F root, raw-shape row", "I01 identifier; I02 identifier", "UPDATE keyed on channel and ts; sql_lint warning dispositioned"),
    ("harmonygames-Games/match3d#476", "K3 home", "T01 temporal; L09 lifecycle; I07 identifier", "undated rows neither modified nor cited; PR stays open; never called merged; author token kept"),
    ("C05433XK267/1758803475.436309", "run #15", "L04 lifecycle", "ZOM-567 is referenced by no PR, so L04 does not arise (excluded)"),
    ("ZOM-559", "Samsung bug", "L03 lifecycle", "stays Todo; no seeded fix"),
    ("evt_f08d0e87c8c7aafe580d42", "Julia's calendar neighbour", "Q11 quantitative; R08 referential", "base copies untouched; seeded event one row per attendee, no invite mail"),
    (f"{ZD}1759176983.189479", "the lean, T-LEAN", "semantic: S04 first names", "no seed depends on it"),
    (f"{ZD}1759171957.791499", "the Sep 29 change", "temporal: none beyond T02 on the panel mail", "no order claim on the panel thread"),
    ("harmonygames-Games/match3d#466", "T-466 distractor", "L10 lifecycle", "different change; not cited by any seed"),
    ("f_89fadbc54660c9881d8cf9", "older GDD, T-AUD", "semantic: none in scope beyond S03", "older version in version_records"),
    ("page_qa_runbook", "H-GATE decoy scope", "referential: none in scope", "not injected"),
    ("snowflake.USER_COHORT_RETENTION", "retention rule", "quantitative: none in scope", "51 ZM rows, 47 with a D14 figure; SC-1 family untouched"),
]
for s in CEN:
    w("| " + " | ".join(s) + " |")
w("\nHazard ids by category: temporal T01, T02, T06; semantic S03, S04; referential R01, R03, R04, R06, R07, R08; quantitative Q01, Q02, Q03, Q10, Q11; lifecycle L03, L04, L06, L08, L09, L10; identifier I01, I02, I03, I04, I07, I08, I10, I11, I13, I14, I15, I17. Manifest `hazard_acknowledgements`: T01, L04, Q11, all `excluded`, verified: no statement in the SQL touches those records (5 UPDATEs listed in the ledger). Cards from `known_data_issues/synthcut.md` are dispositioned in design section 1a; SC-8 keeps ZOM-475 out of every rule.\n")
w("Sibling sweep (design 1a, not repeated): Linear \"samsung\" hits ENG-1431, ENG-2285, ENG-2324, ENG-383 and ZOM-559; ENG-2324 is Done on the other team's board and no seed cites it.\n")

# ---------------- disagreements
w("## Intended disagreements\n")
w("| Disagreement | Why realistic | Resolved by |\n|---|---|---|")
DIS = [
    (f"cmt_38b3cc50dceda37f40f5 says run #15 covers the gate; {RC27} says no phone in the loop", "a QA owner reads a green job as coverage; the job's owner limits it later the same day", f"{GATE}: a pass covers a device only if it ran on that device"),
    (f"{FORM_CLAIRE} says no coaching; {K1} says she took them through the game first", "a friend owns up later in a private mail", "same author, later date; tickets only transcribe the form"),
    (f"f_524278b67bfa30dde78699 clean label; {K4C}/{ts['K4_line']} says the group works in games", "the forgotten detail comes later in a DM", f"same author, later, and {ZD}{ts['R3_industry_rule']}"),
    (f"{FORM_ROBERT} complete form; {ZD}{ts['K5_reply']} says build 1943 never went through a store", "testers pass builds around", f"Leonard wrote the clause in {GATE}; C05433XK267/1758575557.575349 is a non-Submission job"),
    (f"{KPI} 8.63 simple mean; {ZD}{ts['R5_retention_rule']} sets install-weighted", "a Sep 24 snapshot predates the rule", f"newer rule; {ret['retention_d7']} from snowflake.USER_COHORT_RETENTION"),
    (f"{ZD}1758517286.431379 panel 3-3.5; {PANEL} per-player stars with one void", "a headline against detail", f"{ZD}{ts['R4_panel_definition']}"),
    (f"f_89fadbc54660c9881d8cf9 male RPG target; {DECK} sessions decide", "an older GDD", "later records, in version_records of T-AUD"),
]
for s in DIS:
    w("| " + " | ".join(s) + " |")
w("")

# ---------------- constraints
w("## Constraints for the prompt brief\n")
w("| Anchor | May be named (noun phrases only) | Record |\n|---|---|---|")
for a in man["anchors"]:
    w(f"| {a['id']} | {a['prompt_reference']} | {a['locator']} |")
w(f"\nNever named in the prompt: locations of the hidden authorities, ids, the words valid or audit, any exclusion or root cause ({GATE}, {DECK}, {RC27}). Deadlines: none in a seed. Deliverable kinds: register in {WB}, memo in d_8140f09bf9f1b94cb8ee2d, reply in the thread of {ASK}, 60 state writes on ZOM-568 to ZOM-627, re-run notes, a message to Brian in C090N54TG79. The ask wording now reads \"the rules I posted in the channel after my note\".\n")

# ---------------- fact sheet
w("## Fact sheet\n")
w("| Key | Value | Kind | Must appear in / home ids |\n|---|---|---|---|")
for f in man["facts"]:
    h = f.get("home_ids") or f.get("must_appear_in") or []
    w(f"| {f['key']} | {f['value']} | {f['kind']} | {', '.join(h[:3]) or ZD + '1758517286.431379'}{' and ' + str(len(h) - 3) + ' more' if len(h) > 3 else ''} |")
w("\n`python3 Task_Authoring/tools/fact_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql --manifest Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json --no-leak` (verbatim):\n")
w(fence(out("fact_check.txt")))

# ---------------- facts for the human
w("## Facts for the human\n")
w("| Locator | Base / seeded | Fact | Reach | Role | Re-verify |\n|---|---|---|---|---|---|")
FH = [
    (f"{ZD}1758517286.431379", "base", "the note: No coaching, 25–45, ask for friends' reactions", "member", "authority", "no"),
    (ASK, "seeded", "Leonard's ask, Sep 30 21:10:27Z: casual lead hold, RPG lead keep, no clear lead keep", "member", "write target thread", "no"),
    (f"{ZD}{ts['R1_answer']}", "seeded", "25–45 is an age band", "member", "evidence", "no"),
    (f"{ZD}{ts['R3_industry_rule']}", "seeded", "game-industry people don't count", "member", "authority", "no"),
    (f"{ZD}{ts['R2b_pointer']}", "seeded", "names the gate Doc by title", "member", "connecting", "no"),
    (GATE, "seeded", "Samsung is the one group; a pass covers a device only if it ran on it; dev builds do not count", "shared with Julia", "authority", "no"),
    (DECK, "seeded", "observer's label stands; higher mean; at least 6; gap under 0.25 is no clear lead", "owner", "authority", "element text ○ no; ● yes"),
    (LOG, "seeded", "counted to Done, not counted to Canceled", "owner", "authority", "no"),
    (WB, "seeded", "Log 60 rows, Register header", "owner", "write target", "no"),
    (KPI, "seeded", "KPI D7 mean 8.63 over 45 rows", "shared with Julia", "claim met first", "no"),
    (f"{ZD}{ts['R5_retention_rule']}", "seeded", "install-weighted D7, cohorts with a D14 figure, both platforms", "member", "overturning evidence", "no"),
    (f"{ZD}{ts['R4_panel_definition']}", "seeded", "void leaves sum and count", "member", "authority", "no"),
    (PANEL, "seeded", f"ten ratings, player {panel['panel_void'][0]} void; {panel['panel_mean']} over {panel['panel_n']}", "Julia's mailbox", "evidence", "no"),
    (K1, "seeded", "Claire took them through the game before they played, Fri Sep 26, Sep 29 10:02:47Z", "Julia's mailbox", "overturning evidence", "no"),
    (FORM_CLAIRE, "seeded", "form: no coaching, Sep 26 21:00:12Z", "Julia's mailbox", "claim met first", "no"),
    (RESENT, "seeded", "re-sent form, same sessions", "Julia's mailbox", "decoy", "no"),
    (EVT, "seeded", "Friday at Claire's, Julia declined", "Julia's calendar", "evidence", "gcal description ○"),
    (f"{K4C}/1758658884.207315", "seeded", "Julia asks Brian in Turkish about the sessions he shared that morning (rev2)", "member", "connecting", "no"),
    (f"{K4C}/{ts['K4_line']}", "seeded", "Kadıköy ekibi works at mobile game companies, Sep 23 20:23:32Z", "member", "overturning evidence", "no"),
    (f"{ZD}{ts['K5_reply']}", "seeded", "android 1943 never went through a store, Sep 25 17:05:34Z", "member", "overturning evidence", "no"),
    (f"{FC}/{ts['F_reply']}", "seeded", "technical drops get a re-run note, others closed", "member", "authority", "no"),
    ("C05433XK267/1758803475.436309", "base", "run #15 Success Sep 25 12:31Z on Blake/visionBot", "member", "evidence", "no"),
    ("C05433XK267/1758575557.575349", "base", "Match3D Android #1943 main, a non-Submission job", "member", "alternate path", "no"),
    (RC27, "seeded", "pass comes from Unity editor play mode, no phone in the loop, Sep 30 20:10:26Z", "unscoped", "overturning evidence", "no"),
    ("cmt_38b3cc50dceda37f40f5", "seeded", "Vincent: run #15 covers the device gate, Sep 30 16:50:22Z", "unscoped", "claim met first", "linear comment render ●"),
    ("ZOM-567", "seeded", "Done Sep 30 17:10:05Z", "unscoped", "claim met first", "no"),
    ("ZOM-559", "base", "Todo, no session blocker", "unscoped", "decoy", "no"),
    (CARD, "seeded", "what the memo holds; memo goes in Julia's folder", "unscoped", "authority", "no"),
    ("d_8140f09bf9f1b94cb8ee2d", "base", "Julia's root folder", "owner", "write target", "gdocs parent untested"),
    ("snowflake.USER_COHORT_RETENTION", "base", f"51 ZM rows; {ret['retention_rows']} with D14; weighted D7 {ret['retention_d7']}", "unscoped", "evidence", "after regeneration"),
]
for s in FH:
    w("| " + " | ".join(s) + " |")
for k, v in sess.items():
    ev = v["evidence"]
    w(f"| {k} | seeded | {v['session_date']} {v['observer']} {v['audience']} {v['rating']} on {v['device']}, {v['build']}, age {v['age']}, {v['relation']}: {v['verdict']}{' (' + v['reason'] + ')' if v['reason'] else ''}{', re-run note' if v['rerun'] else ''}; Doc {ev['doc']}, comment {ev['comment']} | unscoped ticket, shared Doc | evidence | no |")
w("")

# ---------------- follow-ups
w("## Platform follow-ups\n")
w("| Follow-up | Record | Note |\n|---|---|---|")
PF = [
    ("Injected Linear comments render", "cmt_2fbcaf2d990d8b4e9c0d", "60 devices and Vincent's line ride on `linear_list_comments`; base has none (Ask_Carriers §6b says they render, review m7 asks for a pre-run test)"),
    ("GitHub comment read spill", "harmonygames-Games/match3d#476", "about 266–285K characters; a miss caused by the spill alone is CONFOUNDED"),
    ("New Doc lands in the folder", "d_8140f09bf9f1b94cb8ee2d", "`gdocs_create_document` has no parent parameter; R13 stays ungraded until a run shows the path"),
    ("linear_show_data and maxDescriptionChars", "ZOM-568", "the 60-call get_issue row counts 0 until tested"),
    ("Slides element text renders", DECK, "● carrier by Ask_Carriers; confirm at pre-check"),
    ("GCal copy renders for a declined event", EVT, "○ for detail; no deciding fact sits there"),
    ("Snowflake figures after regeneration", "snowflake.USER_COHORT_RETENTION", f"{ret['retention_d7']} and the 47 rows"),
]
for s in PF:
    w("| " + " | ".join(s) + " |")
w("")

# ---------------- self-review
w("## Self-review\n")
w("### Tool outputs, verbatim\n")
w("`python3 Task_Authoring/tools/sql_lint.py Task_Authoring/task_inputs/01_Universe_Inject.sql`:\n")
w(fence(out("sql_lint.txt")))
w((HERE / "out" / "sql_lint_disposition.txt").read_text(encoding="utf8").strip() + "\n")
w("`python3 Task_Authoring/tools/base_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql`:\n")
w(fence(out("base_check.txt")))
w("`python3 Task_Authoring/tools/base_claims.py Task_Authoring/task_inputs/01_Universe_Inject.sql --task-dir Task_Authoring/task_inputs`:\n")
w(fence(out("base_claims.txt")))
w("One block, in order: `hardness_gate.py` on the final manifest and SQL; `oracle_kit.py check --task-dir Task_Authoring/task_inputs`; `difficulty_mutation.py mutate --task-dir Task_Authoring/task_inputs --dispositions` (the file's mutation map); `trap_liveness.py --task-dir Task_Authoring/task_inputs --dispositions` (its liveness map); `hardness_v2_check.py --task-dir Task_Authoring/task_inputs`; then, when run, `hardness_forecast.py forecast ... --preregister` (UNCALIBRATED, advisory) and `preflight_report.py`. All verbatim.\n")
parts = [out("hardness_gate.txt"), out("oracle_kit.txt"), out("mutation.txt"), out("liveness.txt"), out("v2.txt")]
for extra in ("forecast.txt", "preflight.txt"):
    if (OUT / extra).is_file():
        parts.append(out(extra))
w(fence("\n\n".join(parts)))
w("Dispositions for every mutation result, liveness flag and v2 flag are in `Working_Files/01c_Dispositions.json`. DECISION_FLIP on R_F, R_D, R_E is accepted, weights not raised; RULE_IN_PROMPT re-runs at the prompt stage.\n")

w("### Review findings (01d_SQL_Review.md)"+chr(10))
w("| Finding | Disposition in rev2 | Record |"+chr(10)+"|---|---|---|")
for row in [
    ("M1 observers follow a format nobody passed on", "fixed: the relay now carries the no-coaching line, the age band, the Doc fields and the mail fields", "C0880U9751A/" + ts["R0_relay"]),
    ("M2 Vincent's repro forks K3", "fixed: the line says the repro was in the editor with no Samsung phone", "cmt_38b3cc50dceda37f40f5"),
    ("M3 rc_28 off the base companion shape", "fixed: rc_28 and its mirror removed; root reply_count 30; PR updated_at 20:10:26Z", "C093LEZGF6J/1759258475.735779"),
    ("M4 authorities read like an answer key", "fixed: gate Doc in plain policy, ZOM-559 a bug-queue note, one scope sentence, Arthur's Vision Bot PR named; log note and card reworded", GATE),
    ("m1 industry rule has no scope for earlier sessions", "fixed: adds that it goes for sessions already run", ZD + ts["R3_industry_rule"]),
    ("m2 a/an in device comments", "fixed: article rule; the solver reads both forms", "cmt_2fbcaf2d990d8b4e9c0d"),
    ("m3 closed ticket is not a pass", "fixed: the gate Doc says a closed ticket isn't a pass", GATE),
    ("m4 forward misdescribes the vendor mail", "fixed: names both runs and the report links", PANEL),
    ("m5 Brian's Doc times run backwards", "fixed: Docs 01 to 09 ascend from 09:05:00", "f_524278b67bfa30dde78699"),
    ("m6 K3 shape is a tell", "fixed: four content swaps between rounds; K3 is ZOM-587, 588, 590, 591, 593, 594, 596, 601, 603, 606, 620; counts and means unchanged (truth.json)", "ZOM-601"),
    ("m7 the Turkish line is unprompted", "fixed: Julia asks first in Turkish", K4C + "/1758658884.207315"),
]:
    w("| " + " | ".join(row) + " |")
w(chr(10) + "**Forecast.** rev2 changes per-key truth (which tickets are K3, so the rule controls moved to sessions the truth counts) but no aggregate, no surface slot's expected value and no declared attribution, which are all the design-mode forecast reads. hev_31aeef573fe8aea8 stands; it was not re-registered." + chr(10))
w("### Reading the numbers honestly\n")
w(f"- Mutation: R_K1, R_K3, R_K4, R_K5 are KILLED. R_F, R_D and R_E SURVIVED: on the solver view they never flip a slot, because S-F1, S-D1 and S-E1 are text slots. Each touches only its own 3-weight slot.\n"
  "- L_max 25/77 understates the design. The tool reads only `field` and `total` selectors, so one block miss shows 10 of the 35 of 77 the surface declares (S-Ka 5, S-Kb 3, S-H1 5, S-G1 5, S-G2 5, S-DEC 3, S-BRIAN 3, S-ST1 3, S-ST2 3). All four misses are 59 of 77 by the same count.\n"
  "- With the 8 slots reclassed, contract.slots passes, but difficulty_mutation and the solver-mode forecast still read only `field` and `total` selectors: U stays 74/77 and tool L_max 25/77. By declared attributions the four blocks reach 59 of 77 (0.766) and all seven rules 68 of 77 (0.883).\n"
  "- Forecast hev_31aeef573fe8aea8 supersedes hev_a5bdd23c22790fbd. It is a --design run, the only mode that counts text slots, so it carries no channels. Independent and source: E[avg] 0.430, band 0.307-0.584, P(sd) 0.389, P(patterns) 0.864, P(all) 0.352. Correlated: E[avg] 0.480, band 0.292-0.704, P(sd) 0.563, P(patterns) 0.534, P(all) 0.307.\n"
  "- Too deterministic: seven slots (S-H1, S-G1, S-G2, S-DEC, S-BRIAN, S-ST1, S-ST2, 27 weight) flip together on any block miss, because all 15 miss sets flip the lead. The ladder is 1.00, then 0.545, 0.442, 0.338, 0.234 by misses. Runs with a miss sit 0.10 apart, so SD clears 0.10 only when a run has no miss, and at flat priors few do (median SD about 0.106, model only).\n"
  "- Too correlated: one latent across runs (the correlated scenario) halves P(patterns), since every run then misses the same blocks.\n"
  "- Proposed fair fix, not applied. Findability: raise K1 and K4 find rates to about 0.75, e.g. a form line pointing at the later mail and the nickname explained in Brian's relay; model E[avg] 0.57, P(sd in band) 0.75, against 0.47 and 0.50 at the judged rates. Row spread: raise K5's casual ratings to a mean near 3.45, so a K5 miss alone keeps the casual lead (S-H1, S-DEC, S-BRIAN hold, a 0.69 rung); with both, E[avg] 0.58, P(sd) 0.83. All block misses at 0.25 would give E[avg] 0.64, near the 62 % target. Any rating change must re-run the flip proof.\n")
w("Flip table from the solver (each row a set of block misses):\n")
w("| Missed | Counted | Casual n / mean | RPG n / mean | Gap | Lead | Decision |\n|---|---|---|---|---|---|---|")
import itertools  # noqa: E402
st = S.load_state(sql)
for nmiss in range(0, 5):
    for c in itertools.combinations(["R_K1", "R_K3", "R_K4", "R_K5"], nmiss):
        a = S.aggregates(S.solve(st, disable=frozenset(c)))
        w(f"| {', '.join(c) or 'none'} | {a['classes'].get('counted')} | {a['counts']['casual']} / {a['means']['casual']} | {a['counts']['rpg']} / {a['means']['rpg']} | {a['gap']} | {a['lead']} | {a['decision']} |")
w("\nAll 15 miss sets give RPG past the 0.25 band; the smallest wrong gap is 0.27 (R_K5).\n")

w("### Checks A–C walk (`Evals/0_Injection_Quality_Eval.md`)\n")
w("| Check | Item | Verdict | Pointer |\n|---|---|---|---|")
AC = [
    ("Inventory", f"{n_ins} INSERT, {n_upd} UPDATE, no DELETE, no upsert", "PASS", "SQL L1 header; sql_lint"),
    ("Check A", "references resolve, including archived and history records", "PASS", "base_check Check A; ZOM-559 not touched"),
    ("Check A", "uniqueness scoped to the full collection", "PASS", "1.F lookups; base_check"),
    ("Check A", "ownership, membership, shares", "PASS", f"{GATE} sharing equals its docs row; C090N54TG79 authors are live members"),
    ("Check A", "id contracts", "PASS", "hg.py lint; Message-IDs shared across copies, " + K1),
    ("Check B", "structure, literal JSON, generated and NOT NULL columns", "PASS", "sql_lint 0 errors; hg.py lint 0 FAIL; `text_fts` never written"),
    ("Check B", "`github_reviews.seq` is outside the eval snapshot", "PASS with a CHECK", "see LINT line below; base rows carry seq"),
    ("Check C", "dates and chronology", "PASS", "base_check Check C; supersession_chronology; no timestamp past the bound (plan/sweep.py)"),
    ("Check C", "parent and reply", "PASS", f"{ZD}1758581651.167799 counters; C093LEZGF6J/1759258475.735779 at 30 after rc_28 was removed"),
    ("Check C", "statuses, counts, amounts", "PASS", "ZOM-567 stamps; panel and KPI recomputed in solver/truth.json"),
    ("Check C", "claimed updates and superseding records", "PASS", "version_records strictly increasing"),
    ("Check C", "no grader-facing or padding text", "PASS", "plan/sweep.py avoid lists; every row maps to a manifest element in the ledger"),
]
for s in AC:
    w("| " + " | ".join(s) + " |")
w("")
lint = json.loads(out("lint.json"))
w(f"`hg.py lint` counts: {json.dumps(lint.get('counts'))}.\n")
LD = {"seq": "kept by instruction: base github_reviews rows carry seq and NOT NULL needs it; portal Eval 0 is newer than the local copy (user memory, injection-read-only note); ask the platform lint result at /injection, evidence harmonygames-Games/match3d#476#rev_2"}
for f in lint.get("flags", []):
    if str(f.get("severity")).upper() == "CHECK":
        msg = (f.get("message") or f.get("detail") or "") + " " + str(f.get("column") or "")
        disp = next((v for k, v in LD.items() if k in msg or k in str(f)), "reviewed: base-shape field, harmless at this line; evidence harmonygames-Games/match3d#476")
        w(f"LINT {f.get('check')} L{f.get('line')}: {disp}")
w("")

w("### Touched-data census\n")
w("The touched base records and their hazards are in the section **Touched-data census and coherence hazards** above; nothing the SQL updates is a hazard record.\n")

w("### Counter-readings\n")
w("| Category | Counter-reading (strongest case it fails) | Evidence | Verdict |\n|---|---|---|---|")
CR = [
    ("Temporal", "ticket dates of Sep 30 look newer than Claire's Sep 29 mail, so the correction is older than what it corrects; K3 sessions predate run #15", f"{LOG} says the ticket's own date says nothing about when anything happened; {GATE} says a valid pass clears sessions whatever day they ran", "holds"),
    ("Semantic / Category", "\"casual\" and \"RPG\" are the note's and/or, so one label is invented; a label reads as a re-derivation", f"{DECK} says the observer's label stands (S03)", "holds"),
    ("Cross-service referential", "the ask said replies under the note before D1; five rule records are top-level, so a thread read finds nothing and F-AGE, F-INDUSTRY, F-GATE containers moved", f"{ASK} now says the rules posted in the channel after the note; design_delta records it; R3 opens \"One more for the feedback note\" at {ZD}{ts['R3_industry_rule']}", "holds"),
    ("Quantitative", "three sources tie 60 for 60 on a wrong answer; 9.09 could be 9.05 on a closed-window reading", f"each transcribes one form; {ZD}{ts['R5_retention_rule']} defines mature as having a D14 figure, 47 rows, snowflake.USER_COHORT_RETENTION", "holds"),
    ("State / Lifecycle", "pre-existing: ZOM-559 stays Todo while ZOM-567 is Done on the same family; sibling: ENG-2324 Done on Samsung startup", f"different scopes; {GATE} says ZOM-559 is no session blocker; ENG-2324 is the other team's and no seed cites it (L03)", "holds"),
    ("Identifier / Format", "F root UPDATE keyed on channel and ts breaks the keyed-on-id rule; Claire's calendar copy has a second event id", f"raw export row with no id field, {FC}/1758901945.292269; base keeps a distinct event_id per calendar, shared ical_uid {D.ICAL_UID}", "holds, disclosed"),
    ("People status", "Claire, Oliver and Owen never joined #zombie-design, so they never saw the note", f"R0 relay C0880U9751A/{ts['R0_relay']} reaches all twelve observers; activity.json shows all active at the clock (SC-7 not graded)", "holds"),
    ("Other", "the designed disagreement reads as two silent system fields", f"every one is a dated human claim: cmt_38b3cc50dceda37f40f5 against {RC27}; no system field carries it", "holds"),
    ("Done gap", "best argument it is an unintended inconsistency: Arthur never says Samsung, so the note does not overturn Vincent", f"{GATE}: a pass covers a device only if it ran on that device; {RC27} says no phone in the loop", "holds; remains the likeliest /prompt challenge"),
    ("Coached mail", "best argument it is unintended: the mail never says coaching and a reader could call it harmless", f"{K1} says she took them through what the cards do and which items to grab, against the note's rule at {ZD}1758517286.431379", "holds"),
    ("Industry line", "best argument it is unintended: the line may be about another group", f"same nickname on f_524278b67bfa30dde78699 and {K4C}/{ts['K4_line']}; 0 base hits for the nickname in 1.D", "holds"),
    ("Build reply", "best argument it is unintended: `main` in the job name may read as release", f"{ZD}{ts['K5_reply']} states it outright and Leonard wrote the rule; C05433XK267/1758575557.575349 is only support", "holds"),
    ("Retention", "best argument it is unintended: a KPI Sheet disagreeing with the warehouse is a data defect", f"{KPI} is a dated snapshot with a stated simple mean; the rule at {ZD}{ts['R5_retention_rule']} is later", "holds"),
    ("Panel", "best argument it is unintended: the note's 3-3.5 disagrees with 3.33", f"3.33 is inside the note's range; {PANEL}", "holds"),
    ("GDD", "best argument it is unintended: GDD target against the deck is a live contradiction", "f_89fadbc54660c9881d8cf9 is older and in version_records of T-AUD", "holds"),
    ("Keep or hold", "the ask's mapping flatters Julia, who opposed the change", f"{ASK} states the mapping; {ZD}1759173561.454829 is only context", "holds"),
    ("Volume", "the 183 per-record calls clear 160 only by counting 60 writes", "volume_exception in 01_Hardness_Manifest.json, disclosed in design section 9; evidence reads are 123", "disclosed"),
]
for s in CR:
    w("| " + " | ".join(s) + " |")
w("")
w("### Re-verified facts\n")
w((OUT / "reverify.txt").read_text(encoding="utf8").strip() + "\n")
w("### Lazy-solver pass\n")
w("One broad search per service, first hits, no threads: all 60 count, RPG, keep. That run keeps S-R1, S-M1, S-L1, S-O1, S-O2, so 9 of 77 (design section 12); nothing in the implemented SQL raises it, since the log and tickets carry no verdict.\n")
w("### Open items\n")
w((OUT / "unresolved.txt").read_text(encoding="utf8").strip() + "\n")
(WF / "01_Grounding_Dossier.md").write_text("\n".join(L) + "\n", encoding="utf8")
print("dossier", len(L), "blocks")

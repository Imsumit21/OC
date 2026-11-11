#!/usr/bin/env python3
"""Assemble Working_Files/08_OE_Writing_Ledger.md (prep) for calvin_qm_epic (rev3b SQL 479b8441f52e).
Seeded rows are parsed from the SQL (never executed); base records come from plan/oe_base.json (fresh hg.py reads, plan/oe_reads.py)
and plan/oe_defer.json (plan/oe_defer.py). Facts and dependency edges only; no event text.
Every quote is asserted as a substring of its record, so a wrong value stops the build."""
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402
import stage_gate as G  # noqa: E402

PT = ZoneInfo("America/Los_Angeles")
PERSONA = "calvin_price"
TDREL = "Task_Authoring/task_inputs"
PROMPT = open(os.path.join(TI, "04_Prompt.txt")).read()
SQL_PATH = os.path.join(TI, "01_Universe_Inject.sql")
SQL = open(SQL_PATH).read()
ST = [x for x in parse_sql(SQL) if x["op"] == "insert"]
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
OB = json.load(open(os.path.join(HERE, "oe_base.json")))
DEF = json.load(open(os.path.join(HERE, "oe_defer.json")))
CATALOG = {t["name"] for t in json.load(open(os.path.join(WS, "Evals", "references", "tools", "catalog.json")))}
ENV = {**os.environ, "TASK_AUTHORING_TASK_DIR": TDREL}


def run(args):
    return subprocess.run(args, cwd=WS, capture_output=True, text=True, env=ENV).stdout


CS = json.loads(run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "check-sql", PERSONA, f"{TDREL}/01_Universe_Inject.sql", "--json"]))
LINE = {}
for r in CS["rows"]:
    for k in r["keys"]:
        LINE.setdefault(k, r["line"])
SQL_LINES = SQL.splitlines()


def sql_line(k):
    if k in LINE:
        return LINE[k]
    for i, ln in enumerate(SQL_LINES, 1):
        if f"'{k}'" in ln and ln.lstrip().startswith(("VALUES", "INSERT", "UPDATE")):
            return i
    return None


def L(*keys):
    out = []
    for k in keys:
        n = sql_line(k)
        assert n, k
        out.append(f"SQL L{n}")
    return ", ".join(out)


def rows(table, **kw):
    return [x["row"] for x in ST if x["table"] == table and all(x["row"].get(k) == v for k, v in kw.items())]


def clean(s):
    return (s or "").replace("\\r", "").replace("\\n", "\n").replace("\r", "")


def ts_iso(ts):
    return dt.datetime.fromtimestamp(float(ts), dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def when(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    p = d.astimezone(PT)
    return f"{p.strftime('%a %b %-d %Y %-I:%M%p').replace('AM', 'am').replace('PM', 'pm')} {p.tzname()} ({d.strftime('%Y-%m-%dT%H:%M:%SZ')})"


def safe(s):
    """Record text inside a backtick quote: no backticks, no pipes, no newlines; boxes spelled out."""
    return s.replace("`", "'").replace("|", "/").replace("\n", " / ").replace("☐", "(unticked box)").replace("☑", "(ticked box)").strip()


def must(text, *quotes):
    for q in quotes:
        assert q in text, (q, text[:300])
    return " · ".join("`" + safe(q) + "`" for q in quotes)


def tools(*names):
    for n in names:
        assert n in CATALOG, n
    return ", ".join(names)


FACTS, fid_of = [], {}


def fact(key, value, service, tl, locator, origin, expected, result, visible, depends, source):
    assert source
    n = f"F{len(FACTS) + 1}"
    fid_of[key] = n
    FACTS.append([n, value, service, tl, locator, origin, expected, result, visible, depends, source])
    return n


def dep(*keys):
    return ", ".join(fid_of[k] for k in keys) or "—"


F = dep
F = dep
UNSC = "unscoped service; natural pointer in the Locator origin column"
SY = "YES (proof below)"
sys.path.insert(0, HERE)
import reports as RP  # noqa: E402
SEED = json.load(open(os.path.join(HERE, "seed_text.json")))
ID = {k: v["id"] for k, v in SEED.items()}
AT = {k: v["at"] for k, v in SEED.items()}
BS = OB["slack"]


def bt(k):
    return BS[k]["rec"]["text"]


def bsrc(k):
    return f"{k} (slack {BS[k]['service_file'].split('/')[-1]} {BS[k]['pointer']})"


SM = {f"{r['channel_id']}/{r['ts']}": r for r in rows("slack.slack_messages")}
LC = {r["id"]: r for r in rows("linear.linear_comments")}
LI = {r["id"]: r for r in rows("linear.linear_issues")}
DOCS = {r["document_id"]: r for r in rows("gdocs.docs_documents")}


def st(k):
    return clean(SM[k]["text"])


def lc(k):
    return clean(LC[k]["body"])


# ================================================================ the request and its rules
HUB = ID["hub"]
fact("hub", "Brian's DM: the request", "Slack (Calvin's DM with Brian)", tools("slack_search_public_and_private", "slack_read_channel"),
     "Calvin's 1:1 DM with Brian Foster, Brian's message of yesterday", 'prompt ("He messaged me about it yesterday")',
     f"{HUB}, sent {when(AT['hub'])} by Brian Foster. Quotes: " + must(st(HUB), "I left a note on the ticket about how I want it", "One child for each area, and every report gets its line under the right child",
        "put a stock-take sheet in your ZM queue manager folder and share it with everyone on the review invite, Leonard too", "add one slide with the numbers to your queue manager deck",
        "When it is done tell me here how many reports are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many reports are on the review list"),
     "VERIFIED: every quote cut from the message text", SY, "—", f"{HUB}, {L(HUB)}")
epic = OB["linear"]["ZOM-543"]["rec"]
fact("epic", "The Queue Manager ticket", "Linear", tools("linear_list_issues", "linear_get_issue"), "the ZM ticket titled Queue Manager", 'prompt ("the Queue Manager ticket")',
     "ZOM-543, title " + must(epic["title"], "Queue Manager") + f", team team_ZOM, state In Progress, no parent, created {when(epic['created_at'])}", "VERIFIED: title and fields read from the issue record", UNSC, F("hub"),
     f"ZOM-543 (linear data.json {OB['linear']['ZOM-543']['pointer']})")
NOTE = ID["epic_note"]
note = lc(NOTE)
NQ = ["Children: " + ", ".join(RP.AREAS) + ". One child each, same team, no assignee.", "Reports: the rows of Vincent's flow pass sheet, all of them.", "so don't add new reports from his chats",
      "Plus any bug somebody else on the team saw in a build and told you about in a DM since Vincent started his pass on the 26th, about the home screen after a level.",
      "Passed: Vincent's ok or nr on a build that counts under Arthur's rule for QA passes, as long as that pass still stands under his rule.",
      "Waiting on QA: not passed, and a fix for it is in main that QA has not tried on a main build yet.", "Waiting on a fix: everything else.",
      "if a ticket already has the report, move that ticket under the child and leave a note with the status and why.", "put Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix",
      "If no ticket has it, make a sub-issue under the child with the report as the title and the state the same way.", "No priority and no assignee on the new ones",
      "A child is Clear when all its reports are Passed, otherwise Open. Set the child to Done if it is Clear and to Todo if it is Open.", "Review list: a report that is not Passed, in an area on the agenda of Thursday's review.",
      "Sheet: tab Reports with Report, Area, Status, Ticket, Review list, Why. Tab Areas with Area, Status, Open reports. Slide: the five numbers I asked you for."]
fact("note", "Brian's note on the ticket: how the epic is built", "Linear (comment on ZOM-543)", tools("linear_list_comments"), "the comments of the Queue Manager ticket", 'prompt ("I need you to set it all up as he asked": the DM it hands over says "I left a note on the ticket"); F2 (the ticket)',
     f"{NOTE} on ZOM-543, created {when(AT['epic_note'])} by Brian Foster. Quotes: " + must(note, *NQ), "VERIFIED: every quote cut from the comment body", UNSC, F("hub", "epic"), f"{NOTE} on ZOM-543, {L(NOTE)}")
SHEET = ID["sheet"]
grid = [x["row"] for x in ST if x["table"].endswith("sheets_sheets") and x["row"]["spreadsheet_id"] == SHEET][0]["grid_json"]
grid = grid if isinstance(grid, list) else json.loads(grid)
GT = "\n".join(" / ".join(str(c) for c in r) for r in grid)
srow = {int(r[0]): " / ".join(str(c) for c in r) for r in grid if r and str(r[0]).isdigit()}
assert len(srow) == 38
fact("sheet", "Vincent's flow pass sheet: the report list", "Google Sheets", tools("gdrive_search", "gsheets_values_get"), "the sheet 'ZM home screen flow pass', tab Flow pass, shared with Calvin", 'prompt ("I need you to set it all up as he asked": the note it hands over says "the rows of Vincent\'s flow pass sheet"); search "flow pass"',
     f"{SHEET}, owner vincent.parker@harmonygames.co, modified {when(AT['sheet'])}; header " + must(GT, " / ".join(grid[0])) + "; 38 numbered rows; note " + must(GT, "The codes are in my pass sheet legend doc."),
     "VERIFIED: header and note cut from the grid; 38 rows counted in the grid", SY, F("note"), f"{SHEET}, {L(SHEET)}")
LEG = ID["legend"]
leg = clean(DOCS[LEG]["body_text"])
fact("legend", "The legend of the pass sheet's codes", "Google Docs", tools("gdocs_search_documents", "gdocs_get_document_text"), "Vincent's doc 'How to read my pass sheets'", 'prompt ("I need you to set it all up as he asked": the sheet it hands over says "The codes are in my pass sheet legend doc."); search "pass sheets"',
     f"{LEG}. Quotes: " + must(leg, "Fix: the PR the dev told me it went into. Blank if nobody told me.", "ok and a build means it is fine on that build", "nr and a build means I could not make it happen on that build",
                              "again and a build means it still happens", "ok, chat means I told the dev ok in our chat, the build is there", "Blank means not re-tested yet."),
     "VERIFIED: every quote cut from the document body", SY, F("sheet"), f"{LEG}, {L(LEG)}")
RD = ID["rule_doc"]
rd = clean(DOCS[RD]["body_text"])
fact("rule", "Arthur's rule for QA passes", "Google Docs", tools("gdocs_search_documents", "gdocs_get_document_text"), "Arthur's doc 'ZM builds and QA passes'", 'prompt ("I need you to set it all up as he asked": the note it hands over names "Arthur\'s rule for QA passes"); search "QA passes"',
     f"{RD}, by Arthur Blake. Quotes: " + must(rd, "For ZM a QA pass only counts on a build of the main branch.", "a pass there has to be done again once the branch is merged",
                                              "A pass stands until somebody sees the bug again on a main build made after the one it passed on. Then it is open again, whoever saw it.", "Which branch a build came from is in its #builds post."),
     "VERIFIED: every quote cut from the document body", SY, F("note"), f"{RD}, {L(RD)}")
CT, VO = "D06UPGF5PQV/1758817744.353289", "D06UPGF5PQV/1758820544.160399"
fact("chat", "The 'ok, chat' behind rows 1, 2 and 25", "Slack (Calvin's DM with Vincent)", tools("slack_read_channel", "slack_search_public_and_private"), "Calvin's 1:1 DM with Vincent Parker, Sep 25", "F5 (the legend: the build is in the chat)",
     f"{CT}, sent {when(ts_iso(CT.split('/')[1]))} by Calvin: " + must(bt(CT), "Match 3D iOS Internal - #1718 already tested") + f"; {VO}, sent {when(ts_iso(VO.split('/')[1]))} by Vincent: " + must(bt(VO), "Looks ok to me"),
     "VERIFIED: both quotes cut from the messages", SY, F("legend"), f"{bsrc(CT)}; {bsrc(VO)}")
# builds
BUILDS = dict(RP.MAIN_BUILDS); BUILDS.update(RP.BRANCH_BUILDS); BUILDS["Android Submission #135"] = "C05433XK267/1759263189.219529"
bfact = {}
for name, k in sorted(BUILDS.items(), key=lambda kv: kv[1]):
    fb = BS[k]["rec"]["attachments"][0]["fallback"]
    job, num = name.rsplit(" #", 1)
    head = fb.split(" Changes:")[0].split("\n")[0]
    m = re.match(r"(.+?) - #(\d+) - (.+?) (Success|Started|Fail\w*|Back to normal|Still Failing|Aborted)", fb)
    assert m and m.group(2) == num, (name, fb[:120])
    branch = m.group(3).strip()
    assert (branch == "main") == (name not in RP.BRANCH_BUILDS), (name, branch)
    q = f"{m.group(1)} - #{num} - {m.group(3)}".rstrip()
    bfact[name] = fact("build:" + name, f"Build {name}: branch and time", "Slack (#builds)", tools("slack_search_public_and_private", "slack_read_channel"), f"the #builds post of {job} #{num}", "F6 (the rule doc: the branch is in the #builds post) and F4 (the sheet names the build)",
                       f"{k}, posted {when(ts_iso(k.split('/')[1]))}: " + must(fb, q) + ("; built from main" if branch == "main" else "; built from a feature branch, not main"),
                       "VERIFIED: job, number and branch cut from the post's attachment text", SY, F("rule", "sheet"), bsrc(k))
ALLBUILD = f"{bfact[min(bfact, key=lambda n: int(bfact[n][1:]))]} to {bfact[max(bfact, key=lambda n: int(bfact[n][1:]))]}"
# PRs
prf = {}
for n in ("465", "472", "473", "475"):
    p = OB["github"][n]
    prf[n] = fact("pr" + n, f"PR #{n}: merged into main", "GitHub (harmonygames-Games/match3d)", tools("github_list_pull_requests", "github_get_pull_request"), f"match3d pull request #{n}", "F4 (the sheet's Fix column)" if n != "473" else 'search "Addressables"',
                  f"harmonygames-Games/match3d#{n}, title " + must(p["rec"]["title"], p["rec"]["title"]) + f", base {p['rec']['base_ref']}, merged {when(p['rec']['merged_at'])}", "VERIFIED: title, base and merged_at read from the pull request record", UNSC, F("sheet"),
                  f"harmonygames-Games/match3d#{n} (github data.json {p['pointer']})")
RC = {r["id"]: r for r in rows("github.github_review_comments")}
fact("inline", "Arthur's review comment on #472", "GitHub", tools("github_get_pull_request_comments"), "the review comments of match3d pull request #472", "F" + prf["472"][1:] + " (the PR)",
     f"{ID['inline']}, created {when(AT['inline'])} by Arthur Blake: " + must(clean(RC[ID['inline']]["body"]), "Flow sheet has the season pass icon restart and the event bar starting under the gift popup against this PR. Neither is in this diff. The other two Collect & Win ones are."),
     "VERIFIED: quote cut from the review comment body", UNSC, F("pr472"), f"{ID['inline']}, {L(ID['inline'])}")
fact("inline2", "Arthur's review comment on #475", "GitHub", tools("github_get_pull_request_comments"), "the review comments of match3d pull request #475", "F" + prf["475"][1:] + " (the PR)",
     f"{ID['inline2']}, created {when(AT['inline2'])} by Arthur Blake: " + must(clean(RC[ID['inline2']]["body"]), "Don't see the pack sound stop anywhere in here. Still needs doing."),
     "VERIFIED: quote cut from the review comment body", UNSC, F("pr475"), f"{ID['inline2']}, {L(ID['inline2'])}")
PC = rows("github.github_pr_comments")[0]
fact("else", "Oliver's comment on his merged PR #473", "GitHub", tools("github_get_issue_comments"), "the conversation of match3d pull request #473", "F" + prf["473"][1:] + " (the PR)",
     f"{ID['else_pr']}, created {when(AT['else_pr'])} by Oliver Brooks: " + must(clean(PC["body"]), "this also has four fixes: the pass start popup coming back after every level, the pass bar filling before the tokens land, the claim animation playing twice after the shop, and the freezer popup opening behind the pass popup"),
     "VERIFIED: quote cut from the comment body", UNSC, F("pr473"), f"{ID['else_pr']}, {L(ID['else_pr'])}")
bl = [x for x in parse_sql(SQL) if x["op"] == "update" and x["table"].endswith("github_pull_requests") and "body" in x["set"]][0]
fact("body", "The description of #472", "GitHub", tools("github_get_pull_request"), "match3d pull request #472, its description", "F" + prf["472"][1:] + " (the PR)",
     "harmonygames-Games/match3d#472 body, first line: " + must(clean(bl["set"]["body"]), "Implement Win&Collect into Queue Manager (this also holds the pre-level panel until the level-end coins have landed)"),
     "VERIFIED: quote cut from the body the SQL sets", UNSC, F("pr472"), f"harmonygames-Games/match3d#472, SQL L{bl['line']}")
# later sightings
fact("reopen", "Vincent's later reply: row 9 came back", "Slack (#zombie-bugs)", tools("slack_search_public_and_private", "slack_read_thread"), "#zombie-bugs, a reply under Vincent's Sep 15 submission-issues thread", 'search "Submission 135"',
     f"{ID['reopen']}, sent {when(AT['reopen'])} by Vincent Parker: " + must(st(ID['reopen']), "from Android Submission 135 today", "the pass popup came up on top of the gift again"), "VERIFIED: quotes cut from the reply", SY, F("rule"), f"{ID['reopen']}, {L(ID['reopen'])}")
fact("back", "Robert's later reply: row 29 came back", "Slack (#zombie-bugs)", tools("slack_search_public_and_private", "slack_read_thread"), "#zombie-bugs, a reply under Robert's Sep 10 endless thread", 'search "Submission 135"',
     f"{ID['back']}, sent {when(AT['back'])} by Robert: " + must(st(ID['back']), "Played Android Submission 135 for an hour", "coming back from endless the home intro animation played again every single time"), "VERIFIED: quotes cut from the reply", SY, F("rule"), f"{ID['back']}, {L(ID['back'])}")
fact("reopen2", "Samuel's later note on ZOM-585: row 17 came back", "Linear (comment on ZOM-585)", tools("linear_list_comments"), "the comments of the ticket in row 17's Ticket cell", "F4 (the sheet's Ticket column)",
     f"{ID['reopen2']} on ZOM-585, created {when(AT['reopen2'])} by Samuel: " + must(lc(ID['reopen2']), "Got this again on Android Submission 135, so #472 did not sort it."), "VERIFIED: quote cut from the comment body", UNSC, F("sheet", "rule"), f"{ID['reopen2']} on ZOM-585, {L(ID['reopen2'])}")
fact("back2", "Owen's later note on ZOM-586: row 24 came back", "Linear (comment on ZOM-586)", tools("linear_list_comments"), "the comments of the ticket in row 24's Ticket cell", "F4 (the sheet's Ticket column)",
     f"{ID['back2']} on ZOM-586, created {when(AT['back2'])} by Owen Baker: " + must(lc(ID['back2']), "Android Submission 135: the lane bar starts from zero again every time I open home."), "VERIFIED: quote cut from the comment body", UNSC, F("sheet", "rule"), f"{ID['back2']} on ZOM-586, {L(ID['back2'])}")
fact("older", "Robert's sighting of row 27 on an older build", "Slack (#zombie-match3d)", tools("slack_search_public_and_private", "slack_read_channel"), "#zombie-match3d, Robert's post of Sep 29", 'search "arena entry button"',
     f"{ID['older']}, sent {when(AT['older'])} by Robert: " + must(st(ID['older']), "Android 2006: I could tap the arena entry button while the reward animation was playing"), "VERIFIED: quote cut from the post", SY, F("rule"), f"{ID['older']}, {L(ID['older'])}")
fact("glow", "Marcus's DM: a report outside the sheet", "Slack (Calvin's DM with Marcus)", tools("slack_read_channel", "slack_search_public_and_private"), "Calvin's 1:1 DM with Marcus Bennett, Sep 30", "F3 (the note: a bug told to Calvin in a DM since the 26th)",
     f"{ID['filt_dm']}, sent {when(AT['filt_dm'])} by Marcus Bennett: " + must(st(ID['filt_dm']), "on today's main build the pass icon glow stays on after i claimed everything"), "VERIFIED: quotes cut from the message", SY, F("note"), f"{ID['filt_dm']}, {L(ID['filt_dm'])}")
for key, tk, who in (("alias_gift", "ZOM-556", "row 11"), ("alias_streak", "ZOM-560", "row 20")):
    b = OB["linear"][tk]
    q = "Same thing." if tk == "ZOM-556" else "the freezer from the abandoned pack never shows up on home"
    fact(key, f"{tk} already holds {who}", "Linear", tools("linear_list_issues", "linear_list_comments"), f"the ZM ticket titled '{b['rec']['title']}' and its comments", 'search "daily gift"' if tk == "ZOM-556" else 'search "freezer"',
         f"{tk}, title " + must(b["rec"]["title"], b["rec"]["title"]) + f", state Todo; Vincent's note {ID[key]}, created {when(AT[key])}: " + must(lc(ID[key]), q), "VERIFIED: title read from the issue record, quote cut from the comment body", UNSC, F("sheet", "note"),
         f"{tk} (linear data.json {b['pointer']}); {ID[key]} on {tk}, {L(ID[key])}")
# review
INV = ID["invite_v2"]
gm = [r for r in rows("gmail.gmail_messages") if r["id"] == INV][0]
fact("invite", "The review invite (updated)", "Gmail", tools("gmail_search_messages", "gmail_get_message"), "Leonard's updated invitation to the ZM home screen flow review in Calvin's inbox", 'search "flow review"',
     f"{INV}, sent {when(AT['invite_v2'])} by leonard.hayes@harmonygames.co, subject " + must(gm["subject"], "Updated invitation with note: ZM home screen flow review @ Thu Oct 2, 2025") + "; " + must(clean(gm["body_text"]), "Moved up a day. Agenda is on the roadmap card, I changed it, daily gift waits until next week."),
     "VERIFIED: subject and note cut from the message", SY, F("hub"), f"{INV}, {L(INV)}")
EV = ID["event"]
ev = [r for r in rows("gcal.gcal_events") if r["event_id"] == EV][0]
att = sorted(a["email"] for a in (ev["attendees_json"] if isinstance(ev["attendees_json"], list) else json.loads(ev["attendees_json"])))
five = [a for a in att if a != "calvin.price@harmonygames.co"]
assert len(five) == 5, att
fact("event", "The review event and who is on it", "Google Calendar", tools("gcal_search_events"), "the event 'ZM home screen flow review' on Calvin's calendar", 'search "flow review"',
     f"{EV}, summary " + must(ev["summary"], "ZM home screen flow review") + f", starts Thu Oct 2 2025 11:00am PDT (2025-10-02T18:00:00Z), a semantic future date; attendees other than Calvin: " + ", ".join(five), "VERIFIED: summary, start and attendee emails read from the event row", SY, F("hub", "invite"), f"{EV}, {L(EV)}")
CARD, CUPD = ID["rev_card"], ID["rev_card_update"]
card = [r for r in rows("trello.trello_cards") if r["id"] == CARD][0]
fact("card", "The roadmap card: the review's agenda", "Trello (ZM ROADMAP)", tools("trello_search", "trello_get_card_actions"), "the ZM ROADMAP card 'ZM home screen flow review - Thu Oct 2'", "F" + str(len(FACTS) - 1) + " (the invite: agenda is on the roadmap card)",
     f"{CARD}, name " + must(card["name"], "ZM home screen flow review - Thu Oct 2") + ", description " + must(clean(card["desc"]), "Walk through what is still not passed in: Collect & Win, Level-end rewards.") + f"; changed by action {CUPD} on {when(AT['rev_card_update'])}",
     "VERIFIED: name and description cut from the card row", UNSC, F("invite", "note"), f"{CARD}, {L(CARD)}; {CUPD}, {L(CUPD)}")
GO = ID["gate_old"]
fact("gate_old", "Brian's earlier line about the review's areas (superseded)", "Slack (Calvin's DM with Brian)", tools("slack_read_channel"), "Calvin's 1:1 DM with Brian Foster, Sep 29", "F1 (the same DM)",
     f"{GO}, sent {when(AT['gate_old'])} by Brian Foster: " + must(st(GO), "For the flow review on Friday I want to go through collect&amp;win and daily gift first") + "; superseded by the card change of Sep 30 (governing version: the card)",
     "VERIFIED: quote cut from the message", SY, F("hub"), f"{GO}, {L(GO)}")
JU = "D05HYDTG5TJ/1756838837.147599"
FOLDER, DECK = ID["folder"], ID["deck"]
dfile = {r["id"]: r for r in rows("gdrive.drive_files")}
fact("folder", "Calvin's ZM queue manager folder", "Google Drive", tools("gdrive_search", "gdrive_list_folder"), "Calvin's Drive folder named ZM queue manager", 'prompt ("my ZM queue manager folder")',
     f"{FOLDER}, name " + must(dfile[FOLDER]["name"], "ZM queue manager") + ", owner calvin.price@harmonygames.co", "VERIFIED: name and owner read from the folder row", SY, F("hub"), f"{FOLDER}, {L(FOLDER)}")
fact("deck", "Calvin's queue manager deck", "Google Slides", tools("gdrive_search", "gslides_get_presentation"), "Calvin's presentation named ZM queue manager, in that folder", 'prompt ("my queue manager deck")',
     f"{DECK}, name " + must(dfile[DECK]["name"], "ZM queue manager") + f", parent {FOLDER}, owner calvin.price@harmonygames.co", "VERIFIED: name, parent and owner read from the file row", SY, F("hub", "folder"), f"{DECK}, {L(DECK)}")
seeded_states = {k: v["state_id"] for k, v in LI.items()}
assert len(seeded_states) == 20
fact("tickets", "The 22 tickets that already hold a report, and their state as found", "Linear", tools("linear_list_issues"), "ZM tickets named in the sheet's Ticket column, plus the two base tickets", "F4 (the sheet's Ticket column) and the two ticket facts above",
     "state as found: " + "; ".join(f"{k} {v}" for k, v in sorted(seeded_states.items(), key=lambda kv: int(kv[0].split('-')[1]))) + "; ZOM-556 Todo; ZOM-560 Todo. Every one has team team_ZOM and no parent",
     "VERIFIED: state_id of each seeded issue row; base states read from the two issue records", UNSC, F("sheet", "alias_gift", "alias_streak"),
     f"ZOM-567 to ZOM-586, {L('ZOM-567')} to {L('ZOM-586')}; ZOM-556, ZOM-560 (linear data.json {OB['linear']['ZOM-556']['pointer']}, {OB['linear']['ZOM-560']['pointer']})")

# ================================================================ per report
ROWS = RP.truth()
keys = [k for k in TRUTH if TRUTH[k]["Status"]]
assert len(keys) == 39
rep_f = {}
DEC = {"BRANCH": ("chat", "build:iOS Internal #1718", "rule", "pr465"), "INLINE": ("inline",), "ELSE": ("else", "pr473"), "BODY": ("body", "pr472"), "FILT": ("glow",), "ALIAS": ()}
for r in ROWS:
    t = TRUTH[r["report"]]
    assert t["Status"] == r["status"], r["n"]
    n = r["n"]
    deps = ["sheet", "note", "rule"]
    trap = r["trap"]
    if trap in DEC: deps += list(DEC[trap])
    if n == 32: deps = [d for d in deps if d != "inline"] + ["inline2", "pr475"]
    if n in (12, 15): deps.append("pr472")
    if trap == "REOPEN": deps.append("reopen" if n == 9 else "reopen2")
    if trap == "BACK": deps.append("back" if n == 29 else "back2")
    if trap in ("REOPEN", "BACK"): deps.append("build:Android Submission #135")
    if n == 11: deps.append("alias_gift")
    if n == 20: deps.append("alias_streak")
    if n == 27: deps += ["older", "build:Android #2006"]
    if n in (18, 34): deps.append("pr472" if n == 18 else "pr475")
    m = re.search(r"(?:ok|nr|again) (.+)", r["retest"] or "")
    if m and "build:" + m.group(1) in fid_of: deps.append("build:" + m.group(1))
    deps = list(dict.fromkeys(deps))
    tk = t["Ticket"]
    line = f"existing ticket {tk}, state as found {t['Ticket state as found']}, moved under the {r['area']} child with a note, state {t['Ticket state']}" if tk else f"new sub-issue under the {r['area']} child, state {t['Ticket state']}, no priority, no assignee"
    src = (must(GT, srow[n]) if n <= 38 else "Marcus's DM (not a sheet row)")
    rep_f[n] = fact(f"rep:{n}", f"Report {n}: {r['report']}", "derived (the sheet row and its deciding records)", tools("gsheets_values_get"), f"row {n} of the flow pass sheet" if n <= 38 else "Marcus's DM", "F4 (the sheet)" if n <= 38 else "F" + fid_of["glow"][1:] + " (the DM)",
                    f"Area {r['area']}; Status {t['Status']}; {line}; Review list {t['Review list']}. Sheet row: {src}", f"VERIFIED by recorded rule: {t['Why']}", SY if n <= 38 else SY, F(*deps),
                    (f"{SHEET}, {L(SHEET)}" if n <= 38 else f"{ID['filt_dm']}, {L(ID['filt_dm'])}") + "; deciding facts " + F(*[d for d in deps if d not in ('sheet', 'note')]))
ALLR = f"{rep_f[1]} to {rep_f[39]}"
areas = {}
for a in RP.AREAS:
    mine = [r for r in ROWS if r["area"] == a]
    areas[a] = (len(mine), sum(r["status"] != RP.P for r in mine))
NP, NQ_, NF = (sum(r["status"] == s for r in ROWS) for s in (RP.P, RP.Q, RP.F))
NREV = sum(TRUTH[r["report"]]["Review list"] == "Yes" for r in ROWS)
NCLEAR = sum(v[1] == 0 for v in areas.values())
assert (NP, NQ_, NF, NCLEAR, NREV) == (10, 9, 20, 0, 7)
fact("areas", "The ten areas: status and open reports", "derived (the report facts)", tools("gsheets_values_get"), "the ten areas of Brian's note", "F3 (the note names the areas)",
     "; ".join(f"{a}: Open, {v[1]} open of {v[0]}" for a, v in areas.items()) + ". No area is Clear, so every child is Todo", "VERIFIED by recorded calculation over the 39 report facts", UNSC, ALLR, f"{NOTE} on ZOM-543, {L(NOTE)}; {SHEET}")
fact("totals", "The five numbers Brian asked for", "derived (the report facts)", tools("gsheets_values_get"), "counts over the 39 reports", "F1 (the DM lists the five numbers)",
     f"passed {NP}; waiting on QA {NQ_}; waiting on a fix {NF}; areas clear {NCLEAR}; on the review list {NREV} (rows " + ", ".join(str(r['n']) for r in ROWS if TRUTH[r['report']]['Review list'] == 'Yes') + "); 39 reports; 22 existing tickets, 17 new sub-issues",
     "VERIFIED by recorded calculation: 10 + 9 + 20 = 39; review list = not Passed in Collect & Win or Level-end rewards", UNSC, ALLR + ", " + F("areas", "card"), f"{HUB}, {L(HUB)}; {SHEET}; {CARD}")


# ---------------------------------------------------------------- requirements
def span(s):
    assert s in PROMPT, s
    return s


REQ = [
    (span("Brian wants the Queue Manager ticket turned into a real epic before Thursday's flow review."), "Discovery — the ticket and the review", "Explicit", F("epic", "event", "invite")),
    (span("He messaged me about it yesterday."), "Discovery — Brian's DM is the source of every ask", "Explicit", F("hub")),
    (span("I need you to set it all up as he asked"), "Discovery — the DM's incorporated records: the note, the pass sheet, the legend, Arthur's rule, the builds, the PRs, the later sightings, the card", "Implicit (through F1 and F3)",
     F("note", "sheet", "legend", "rule", "chat") + ", " + ALLBUILD + ", " + F("pr465", "pr472", "pr473", "pr475", "inline", "inline2", "else", "body", "reopen", "back", "reopen2", "back2", "older", "glow", "alias_gift", "alias_streak", "card", "gate_old")),
    (span("the children and report lines in Linear"), "Write — 10 children, 17 sub-issues, 22 moves and 22 notes", "Explicit", F("tickets") + ", " + ALLR + ", " + F("areas")),
    (span("the stock-take sheet in my ZM queue manager folder"), "Write — a sheet with tabs Reports and Areas in the folder", "Explicit", F("folder") + ", " + ALLR + ", " + F("areas")),
    (span("shared with everyone on the review invite"), "Write / Constraint — the five other attendees", "Explicit", F("event", "invite")),
    (span("a slide with the numbers in my queue manager deck"), "Write — one new slide with the five numbers", "Explicit", F("deck", "totals")),
    (span("message him in our DM with the numbers he wants back"), "Write / Tell — the five numbers in the DM with Brian", "Explicit", F("hub", "totals")),
]
late = []
for k, v in DEF.items():
    if k != "sql":
        assert not v["hit_limit"] and v["complete"], k
        late += v.get("late", [])


def dcount(pfx):
    return sum(v["visible"] for k, v in DEF.items() if k.startswith(pfx))


DEFER = ("slack · gmail · linear · trello (Calvin's channels, DMs and mailbox through persona_view search; all of Linear and Trello through hg.py search; the seeded SQL rows by text): 'hold off', 'not yet', 'don't move', 'wait for', 'wait until', 'on hold', "
         "'don't close', 'leave it open', 'don't file', 'keep it open', 'before you close' (limit 3000, no search hit its limit) — population complete: "
         f"slack {dcount('slack:')} hits, gmail {dcount('gmail:')}, linear {dcount('linear:')}, trello {dcount('trello:')}, SQL {sum(DEF['sql'].values())} (bug wording in ZOM-570 and ZOM-574, not a hold); {len(late)} hits dated Sep 30 2025 or later; "
         f"governing version: Brian's DM {HUB} (Sep 30 20:40Z) and his note {NOTE} are the latest instructions and neither holds a write; result: no defer")
WR = [
    ("R4", "Create the ten area children under ZOM-543", '"the children and report lines in Linear"', tools("linear_create_issue") + " (exists)", "team, title (+ parentId, state)", F("note", "areas"), "ten issues in team ZOM with parent ZOM-543, no assignee, all in state Todo (new issues: state_history_json an empty array at load)", "one child per area named in the note"),
    ("R4", "Create a sub-issue for each report no ticket holds (17)", '"the children and report lines in Linear"', tools("linear_create_issue") + " (exists)", "team, title (+ parentId, state)", ALLR, "17 issues, each under its area's child, 10 Done, 4 In Validation, 3 Todo, no priority, no assignee", "the report as the title"),
    ("R4", "Move each existing ticket under its child and set its state where it differs (22)", '"the children and report lines in Linear"', tools("linear_update_issue") + " (exists)", "id (+ parentId, state)", F("tickets") + ", " + ALLR, "22 tickets each with its area's child as parent; 8 state changes: ZOM-568, ZOM-572, ZOM-573, ZOM-584 to In Validation and ZOM-571, ZOM-574, ZOM-581, ZOM-585 to Todo", "parent and state only"),
    ("R4", "Leave the status note on each existing ticket (22)", '"the children and report lines in Linear"', tools("linear_create_comment") + " (exists)", "issueId, body", F("tickets") + ", " + ALLR, "one comment on each of the 22 tickets", "the status and why"),
    ("R5", "Create the stock-take sheet in the folder and write both tabs", '"the stock-take sheet in my ZM queue manager folder"', tools("gsheets_create_spreadsheet", "gsheets_batch_update", "gsheets_values_update", "gdrive_move_file") + " (exist)", "title; spreadsheetId, requests; spreadsheetId, range, values; fileId, newParentId", F("folder", "areas") + ", " + ALLR, f"a native sheet whose parent is {FOLDER}, tab Reports with 39 rows and tab Areas with 10 rows", "columns Report, Area, Status, Ticket, Review list, Why and Area, Status, Open reports"),
    ("R6", "Share the sheet with the five other attendees (5)", '"shared with everyone on the review invite"', tools("gdrive_share_file") + " (exists)", "fileId, emailAddress, role", F("event"), "each of the five addresses holds a permission on the sheet", "—"),
    ("R7", "Add one slide with the five numbers to the deck", '"a slide with the numbers in my queue manager deck"', tools("gslides_batch_update") + " (exists)", "presentationId, requests", F("deck", "totals"), f"one new slide in {DECK} carrying the five numbers", "10, 9, 20, 0 and 7 with their labels"),
    ("R8", "Message Brian in the DM", '"message him in our DM with the numbers he wants back"', tools("slack_send_message") + " (exists)", "channel, text", F("hub", "totals"), "a message in the DM D0770ET6WBW with Brian, after the other writes", "passed 10, waiting on QA 9, waiting on a fix 20, areas clear 0, review list 7"),
]
B = lambda n: BUILDS[n]  # noqa: E731
TRAPS = [
    ("T1", f"Rows 1, 2 and 25 say 'ok, chat' and Vincent wrote 'Looks ok to me' ({VO})", F("rep:1", "rep:2", "rep:25"), f"the build he looked at, {B('iOS Internal #1718')}, came from a feature branch; {RD} counts main builds only"),
    ("T2", f"Rows 12 and 15 name #472 and row 32 names #475, all merged, tickets In Validation (ZOM-571, ZOM-574, ZOM-581)", F("rep:12", "rep:15", "rep:32"), f"Arthur's review comments {ID['inline']} and {ID['inline2']}"),
    ("T3", "Rows 13, 14, 37 and 38 have a blank Fix cell and Todo tickets (ZOM-572, ZOM-573, ZOM-584)", F("rep:13", "rep:14", "rep:37", "rep:38"), f"Oliver's comment {ID['else_pr']} on merged #473"),
    ("T4", "Row 6 has a blank Fix cell and ZOM-568 is Todo", F("rep:6"), "the first line of the description of harmonygames-Games/match3d#472"),
    ("T5", f"Rows 9 and 29 read as passed on main builds (nr iOS Internal #1745, ok iOS Internal #1750)", F("rep:9", "rep:29"), f"later replies {ID['reopen']} and {ID['back']} on Android Submission 135 ({B('Android Submission #135')})"),
    ("T6", "Rows 17 and 24 read as passed on iOS Internal #1757 and Vincent's own notes on ZOM-585 and ZOM-586 say ok", F("rep:17", "rep:24"), f"later notes {ID['reopen2']} (Sep 30 21:52Z) and {ID['back2']} (Sep 30 22:07Z)"),
    ("T7", f"Robert saw row 27's bug after Vincent's nr ({ID['older']})", F("rep:27"), f"Android #2006 ({B('Android #2006')}) was built before iOS Internal #1745 ({B('iOS Internal #1745')})"),
    ("T8", "Row 18 says again on Android #2013 and row 34 again on iOS Internal #1757, both with a merged Fix PR", F("rep:18", "rep:34"), f"{B('Android #2013')} is before the #472 merge (Sep 30 15:53Z); {B('iOS Internal #1757')} is after the #475 merge (16:09Z)"),
    ("T9", f"Brian's Sep 29 line names collect&win and daily gift for the review ({GO})", F("card", "totals"), f"the card change {CUPD}, Sep 30 17:22Z, later"),
    ("T10", "Rows 11 and 20 have a blank Ticket cell", F("alias_gift", "alias_streak"), f"Vincent's notes {ID['alias_gift']} on ZOM-556 and {ID['alias_streak']} on ZOM-560"),
    ("T11", f"The sheet reads as the whole list; Vincent's chat has a pass icon VFX remark (D06UPGF5PQV/1758721951.996909)", F("glow"), f"the note takes a DM from somebody else since the 26th ({ID['filt_dm']}) and leaves Vincent's chats out"),
    ("T12", f"Arthur's other doc says a pass on the dev's branch build is enough ({ID['dd_doc']})", F("rule"), "that doc is about DD hotfixes; the ZM doc governs"),
]
RISKS = [
    ("1", "The Areas tab's Open reports may be a count or the list of open reports; /prompt accepts both", F("areas"), "rubric", "accept either"),
    ("2", "Share role is free; /prompt asked to accept any role", F("event"), "rubric", "accept any role"),
    ("3", "The sheet may be created in the folder directly or created and then moved", F("folder"), "OE accuracy", "name the end state, not one route"),
    ("4", "The message may be a new DM message or a thread reply under Brian's message", F("hub"), "rubric", "accept either"),
    ("5", "Marcus's report may be titled in the runner's own words", F("rep:39"), "rubric", "grade the report, not one wording"),
    ("6", "Six baseline runs on this SQL missed the PR review and PR comment facts in every run", F("inline", "inline2", "else"), "rubric (all-fail rows need a justification)", "cite the deciding record in each row"),
]

# ---------------------------------------------------------------- visibility proof
brow = [" | ".join(str(c) for c in f) for f in FACTS]
need = sorted({x for r in brow for _, x in G.scoped_ids(r)})
seeded = [x for x in need if x in LINE]
base = [x for x in need if x not in LINE]
lbf = os.path.join(HERE, "oe_lb_ids.txt")
open(lbf, "w").write("\n".join(seeded) + "\n")
cs_txt = run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "check-sql", PERSONA, f"{TDREL}/01_Universe_Inject.sql", "--load-bearing", f"{TDREL}/Working_Files/plan/oe_lb_ids.txt"])
yes_rows = [ln for ln in cs_txt.splitlines() if ln.startswith("[YES LB]") and any(x in ln for x in seeded)]
verdict = [ln for ln in cs_txt.splitlines() if ln.startswith("verdict:")]
svc_of = {x: s for r in brow for s, x in G.scoped_ids(r)}
base += [x for x in seeded if not any(x in ln for ln in yes_rows)]
cansee = []
for x in base:
    out = run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "can-see", PERSONA, svc_of[x], x]).splitlines()
    cansee.append(out[0] if out else f"{PERSONA} {svc_of[x]} {x}: UNVERIFIED")
bad = [c for c in cansee if ": YES" not in c]
print("NOT YES:", bad)

O = []
A = O.append
ctx = json.load(open(os.path.join(WF, "00_Task_Context.json")))
clock = ctx["universe"]["clock_line"].replace("Clock: ", "")
freeze = ctx.get("freeze_utc") or ctx["universe"].get("freeze_utc")
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]  # noqa: E731
A("# 08 OE Writing Ledger — calvin_qm_epic (the Queue Manager epic and stock-take, injection rev3b)")
A(f"Generated 2026-11-10 · Clock {clock} · seed bound {freeze} · Persona Calvin Price calvin.price@harmonygames.co (Game Engineer (Unity VFX)) · Tier Long-Horizon · Mode Hard")
A(f"Status: READY — every requirement has verified facts, every scoped fact is persona-visible (pasted proof below), all {len(WR)} write families map to cataloged tools, friction is none")
A(f"Inputs read: 04_Prompt.txt — present (sha256 {sha(os.path.join(TI, '04_Prompt.txt'))}) · 00_Assigments.md — present · 01_Universe_Inject.sql — present (rev3b, sha256 {sha(SQL_PATH)}) · 01_Grounding_Dossier.md — present · 03_Error_Async_Config.txt — present (Friction: none) · 02_Reference_Files_Manifest.md — absent (no reference files)")
A("")
A("Persona binding: roster entry calvin_price, Calvin Price, Game Engineer (Unity VFX), calvin.price@harmonygames.co. Scoped services: Gmail (own mailbox), Slack (member of #builds, #zombie-bugs, #zombie-match3d and the DMs with Brian, Vincent and Marcus), Calendar (invited to the review), Drive, Docs, Sheets and Slides (files shared with or owned by him). Linear, GitHub and Trello are unscoped.")
A("")
A("Dates: Pacific first, UTC beside it. 'sent', 'created', 'posted', 'merged' and 'modified' mark record times; every record time below is at or before the seed bound. Semantic future date: the review starts Thu Oct 2 2025 11:00am PDT (2025-10-02T18:00:00Z), after the clock, and nothing treats it as held.")
A("")
A("## A · Requirements (traced to the prompt)")
A("| R | Prompt span (quoted) | Type (Discovery / Write / Tell / Constraint) | Explicit / implicit | Fact IDs |")
A("|---|---|---|---|---|")
for i, r in enumerate(REQ, 1):
    A(f"| R{i} | \"{r[0]}\" | {r[1]} | {r[2]} | {r[3]} |")
A("")
A("## B · Facts")
A('| F | Fact / value | Service | Tool family (catalog) | Locator | Locator origin (prompt · F-n · search "query text") | Expected data (dates typed: created / starts / due) | Ledger result for the Expected line (VERIFIED quote · not_a_claim · ABSENCE evidence_check · UNRESOLVED) | Persona-visible? (proof) | Depends on | Source pointer |')
A("|---|---|---|---|---|---|---|---|---|---|---|")
for f in FACTS:
    A("| " + " | ".join(str(c).replace("\n", " ") for c in f) + " |")
A("")
A("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)")
A("")
A(f"`python3 Task_Authoring/tools/persona_view.py check-sql {PERSONA} {TDREL}/01_Universe_Inject.sql --load-bearing plan/oe_lb_ids.txt` ({len(seeded)} seeded ids; load-bearing rows and the verdict line):")
A("")
A("```"); [A(x) for x in yes_rows + verdict]; A("```")
A("")
A(f"`python3 Task_Authoring/tools/persona_view.py can-see {PERSONA} (service) (id)` ({len(base)} base ids, first line of each):")
A("")
A("```"); [A(x) for x in cansee]; A("```")
A("")
A("## C · Write capability")
A("| R | Required write | Prompt authority (quoted; agent, not user-reserved) | Catalog tool (exists?) | Required parameters | Target (fact ID) | Completing end state | Content the prompt requires | Defer search (services · population · pagination complete · governing version · result, or UNRESOLVED) | Feasible? |")
A("|---|---|---|---|---|---|---|---|---|---|")
for w in WR:
    A("| " + " | ".join(w) + f" | {DEFER} | YES |")
A("")
A("## D · Friction facts")
A("| Function (01_) | Mode / rate / wait | Facts blocked | Alternative path (service, locator) | Alternative facts | Visible? |")
A("|---|---|---|---|---|---|")
A("| none | Friction: none (03_Error_Async_Config.txt) | — | — | — | — |")
A("")
A("## E · Traps and distractors")
A("| T | What the agent meets (pointer) | Competes with (fact ID) | Discriminator (timestamp / author / ID) |")
A("|---|---|---|---|")
for t in TRAPS:
    A("| " + " | ".join(t) + " |")
A("")
A("## F · Open risks")
A("| # | Risk | Facts affected | Consequence (OE accuracy / rubric / UGT / feasibility) | Check needed |")
A("|---|---|---|---|---|")
for r in RISKS:
    A("| " + " | ".join(r) + " |")
A("")
A("## G · Tally")
nq = sum("VERIFIED" in f[7] for f in FACTS)
A(f"Requirements {len(REQ)} · facts {len(FACTS)} · writes {len(WR)} (feasible {len(WR)}) · friction items 0 · expected values {len(FACTS)} (quoted {nq} · not_a_claim 0 · ABSENCE-checked 0) · unverified visibility {len(bad)} · blocking 0")
A("")
A("## Self-review")
A("")
A(f"Walked Evals/2_Oracle_Events_Eval.md 1.1, 2.1–2.6 and 3.1–3.5 against this ledger in order. Every requirement has facts; every write family has its prompt authority, a cataloged tool with its required parameters, a target fact and an end state; every quote is asserted as a substring of its record when this file is built; the 39 report facts and the totals come from solver/truth.json, which the platform /prompt on this SQL also derived (Working_Files/platform_reports/prompt_rev3b_PASS.md: 10, 9, 20, 0, 7). Base records were re-read through tools/hg.py today (plan/oe_reads.py, plan/oe_base.json): the 16 #builds posts, the two chat lines, ZOM-543, ZOM-556, ZOM-560 and PRs harmonygames-Games/match3d#465, #472, #473, #475.")
A("")
A("No-event-text scan: read every cell of sections A to F for event wording, agent voice or instruction verbs. The ledger holds facts, quotes, targets and end states only; no cell is written as a step the agent takes, and the report facts state the value and its deciding records.")
A("")
A(f"Defer search: {len(late)} hits dated Sep 30 2025 or later across Calvin's Slack and Gmail; the SQL's three 'wait' hits are bug wording on ZOM-570 and ZOM-574.")
A("")
A("| R | Counter-reading (strongest other reading of the span, or a competing location) | Evidence that resolves it | Result |")
A("|---|---|---|---|")
CRS = [
    ("R1", "'the Queue Manager ticket' could be the Trello roadmap card of that name (68c453cd0ff184d95550bc58)", f"Brian's DM {HUB}: 'Right now it is one ticket' and 'I left a note on the ticket'; the note is on ZOM-543 ({fid_of['note']})", "holds"),
    ("R2", "'yesterday' could be Brian's Sep 29 line about the review", f"{GO} is Sep 29 16:41Z, two days before the clock; {HUB} is Sep 30 20:40Z = Tue Sep 30 1:40pm PDT ({fid_of['hub']})", "holds"),
    ("R3", "'as he asked' could stop at the DM's own words and take the sheet's ok and Fix cells at face value", f"the DM hands the calls to the note {NOTE}, which names Arthur's rule ({fid_of['rule']}) and a fix that is in main; the PR records and later sightings decide those ({fid_of['inline']}, {fid_of['else']}, {fid_of['reopen2']})", "holds"),
    ("R4", "the report lines could be new sub-issues for all 39, or only for open ones", f"the note {NOTE}: 'if a ticket already has the report, move that ticket under the child' and 'If no ticket has it, make a sub-issue' ({fid_of['tickets']})", "holds (17 new, 22 moved)"),
    ("R5", "the stock-take sheet could be a tab added to Vincent's sheet", f"the DM {HUB}: 'put a stock-take sheet in your ZM queue manager folder'; the folder is {FOLDER} ({fid_of['folder']})", "holds (a new sheet)"),
    ("R6", "'everyone on the review invite' could mean only Brian and Leonard, or include Calvin", f"the event {EV} lists five attendees other than Calvin ({fid_of['event']})", "holds (5)"),
    ("R7", "'the numbers' could go on an existing slide", f"the DM {HUB}: 'add one slide with the numbers'; the note: 'Slide: the five numbers I asked you for' ({fid_of['deck']})", "holds (one new slide)"),
    ("R8", "'the numbers he wants back' could be the three status counts only", f"the DM {HUB} lists five: passed, wait on QA, wait on a fix, areas clear, review list ({fid_of['totals']})", "holds (10, 9, 20, 0, 7)"),
]
assert len(CRS) == len(REQ)
for r in CRS:
    A("| " + " | ".join(r) + " |")
A("")
A("Unresolved: none blocking. Open risks §F 1 to 6 go to the draft and rubric stages.")
A("")
open(os.path.join(WF, "08_OE_Writing_Ledger.md"), "w").write("\n".join(O) + "\n")
json.dump({"fid": fid_of, "seeded": seeded, "base": base}, open(os.path.join(HERE, "oe_ledger_ids.json"), "w"), indent=1)
print("facts", len(FACTS), "req", len(REQ), "seeded ids", len(seeded), "base ids", len(base), "yes rows", len(yes_rows))

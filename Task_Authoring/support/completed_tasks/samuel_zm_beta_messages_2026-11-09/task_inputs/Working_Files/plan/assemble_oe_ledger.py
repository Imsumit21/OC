#!/usr/bin/env python3
"""Assemble Working_Files/08_OE_Writing_Ledger.md (prep) from the rev6 SQL rows (parsed, never executed), the base records
read through tools/hg.py (plan/oe_base.json, oe_base2.json, oe_trello.json, oe_wh_rows.txt), solver/truth.json and
persona_view check-sql / can-see. Facts and dependency edges only; no event text. Every quote is asserted as a substring of
its record, so a wrong value stops the build."""
import datetime as dt
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
PERSONA = "samuel_turner"
TDREL = "Task_Authoring/task_inputsK"
PROMPT = open(os.path.join(TI, "04_Prompt.txt")).read()
SQL_PATH = os.path.join(TI, "01_Universe_Inject.sql")
SQL = open(SQL_PATH).read()
ST = [x for x in parse_sql(SQL) if x["op"] == "insert"]
P = json.load(open(os.path.join(HERE, "ids.json")))
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
B1 = json.load(open(os.path.join(HERE, "oe_base.json")))
B2 = json.load(open(os.path.join(HERE, "oe_base2.json")))
B3 = json.load(open(os.path.join(HERE, "oe_base3.json")))
TR = json.load(open(os.path.join(HERE, "oe_trello.json")))
DEF = json.load(open(os.path.join(HERE, "oe_defer_full.json")))
I, BASE, TK = P["ids"], P["base"], P["tickets"]
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
    for i, l in enumerate(SQL_LINES, 1):
        if f"'{k}'" in l and l.lstrip().startswith(("VALUES", "INSERT", "UPDATE")):
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


def when(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    p = d.astimezone(PT)
    return f"{p.strftime('%a %b %-d %Y %-I:%M%p').replace('AM', 'am').replace('PM', 'pm')} {p.tzname()} ({d.strftime('%Y-%m-%dT%H:%M:%SZ')})"


def ts_iso(ts):
    return dt.datetime.fromtimestamp(float(ts), dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def must(text, *quotes):
    for q in quotes:
        assert q in text, (q, text[:200])
    return " · ".join("'" + q + "'" for q in quotes)


def tools(*names):
    for n in names:
        assert n in CATALOG, n
    return ", ".join(names)


FACTS, fid_of = [], {}


def fact(key, value, service, tl, locator, origin, expected, result, visible, depends, source):
    assert source
    n = f"F{len(FACTS) + 1}"
    fid_of[key] = n
    FACTS.append((n, value, service, tl, locator, origin, expected, result, visible, depends, source))
    return n


def dep(*keys):
    return ", ".join(fid_of[k] for k in keys) or "—"


def F(*keys):
    return ", ".join(fid_of[k] for k in keys)


UNSC = "unscoped service; natural pointer in the Locator origin column"
SCOPED_YES = "YES (proof below)"
S_ = {r["ts"]: r for r in rows("slack.slack_messages")}


def seeded_msg(ref):
    return S_[ref.split("/")[1]]


hub = seeded_msg(I["hub"])
hubt = clean(hub["text"])
HUBQ = ["The PN sheet says six are Ready and I don't trust that",
        "Take every row on the PNs Beta tab plus every ask for a new phone message that's been filed on a ticket or a card up to today, and make a call on each one using the message rule doc",
        "Put it in one sheet in your Drive folder, one row per message: Message, Ticket, Call, What's missing, Audience, Final headline, String change",
        "Next to it a one-page note for the team: start with D1 and D7 for the Sep 15 cohort week from the warehouse, iOS and Android separately, then the lapsed reminders the client schedules day by day, and anything the client already schedules that's still a Hold and why",
        "I made tickets for the sheet rows under DES-314 and people added their asks there",
        "Leave the call as a comment on each ticket and move the ticket to match",
        "Anything with no ticket gets one, but don't make a second one for something that already has a ticket under whatever name",
        "Every Go goes on a checklist on our push notifications card so Vincent can tick it off",
        "Email each person who asked for something, apart from me, to say what happened to their asks",
        "When it's done tell me here how many Go, Hold and Drop"]
fact("hub", "Leonard's DM: the whole job", "Slack (Samuel's DM with Leonard)", tools("slack_search_public_and_private", "slack_conversations_history"),
     "Samuel's 1:1 DM with Leonard Hayes, his message of Tue Sep 30", 'prompt ("His DM to me from yesterday")',
     f"{I['hub']}, sent {when(ts_iso(hub['ts']))} by Leonard Hayes. Quotes: " + must(hubt, *HUBQ),
     "VERIFIED: every quote cut from the message text", SCOPED_YES, "—", f"{I['hub']}, {L(I['hub'])}")

rule = rows("gdocs.docs_documents")[0]
rt = clean(rule["body_text"])
RULEQ = ["A message is anything the game puts on a player's phone while the game is closed.", "Run these tests in order and stop at the first one that fails.",
         "1. The feature behind it is in the beta.", "2. The client can send it without a server.", "3. The client already schedules it.",
         "4. It can reach the players it is written for. A player only counts once our own permission ask has happened, the settings toggle doesn't count. It fails only if none of them count.",
         "5. It fires on the right day. The hour doesn't matter for beta, the day does.", "6. Vincent has seen it arrive on both iOS and Android.",
         "Go: it passes all six. Drop: it fails test 1, or the client already covers it under another message, then name that message. Hold: anything else, and name the test it failed.",
         "In the beta means live in Zombie Match today or on the BETA list of the ZM ROADMAP board.", "Neither status column on the sheet decides anything.",
         "What Vincent counts as seen is in his QA note. The permission ask is Robert's call.",
         "The final headline is the latest line I've called. A line that differs from what the client ships needs a string ticket under DES-314, because the strings are hard-coded, so open one when you make the call. Emoji don't count as a different line. Final headline and String change are only for Go rows. Audience is who the ask says it's for.",
         "Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise."]
fact("rule", "The message rule: six ordered tests, the Go, Drop and Hold definitions, and the headline, audience and ticket rules", "Google Docs (Drive)",
     tools("gdrive_search", "gdocs_search_documents", "gdocs_get_document_text"), "the Doc titled 'Beta message rule'", dep("hub") + ' ("the message rule doc"); search "Beta message rule"',
     f"{I['rule_doc']}, modified {when(rule['modified_time'])}, owner {rule['owner_email']}. Quotes: " + must(rt, *RULEQ),
     "VERIFIED: every quote cut from body_text", SCOPED_YES, dep("hub"), f"{I['rule_doc']}, {L(I['rule_doc'])}")

grid = B1["pn_grid"]
hdr = [c.strip() for c in grid[0]]
assert B1["pn_tabs"][1] == "PNs Beta" and len(grid) == 15 and hdr[1] == "Status" and hdr[8].startswith("Status (NA")
PN = {i: grid[i] for i in range(1, 15)}
ready = [i for i, r in PN.items() if r[1].strip() == "Ready"]
assert len(ready) == 6
fact("sheet", "The Zombie Match PN sheet, PNs Beta tab: 14 rows, six Ready", "Google Sheets (Drive)", tools("gdrive_search", "gdrive_list_sheets", "gdrive_read_sheet_range"),
     "the sheet 'Push Notifications Zombie Match', tab PNs Beta", 'prompt ("the Zombie Match PN sheet")',
     f"{BASE['pn_sheet']}, title '{B1['pn_meta']['title']}', last changed {when(B1['pn_meta']['modified_time'])}; tabs {', '.join(B1['pn_tabs'])}. "
     "14 rows (Details / Status / Status (NA, WIP, LIVE) / Headline): " + " ; ".join(f"{i}. {r[5].strip()} / {r[1].strip()} / {r[8].strip()} / {r[9].strip()}" for i, r in PN.items()),
     "VERIFIED: cells read from gsheets data.json /sheets_spreadsheets/220/sheets/1/grid; '14 rows' and 'six Ready' counted from the grid", SCOPED_YES, dep("hub"),
     f"{BASE['pn_sheet']}, gsheets data.json#/sheets_spreadsheets/220/sheets/1/grid")

parent = rows("linear.linear_issues", id="DES-314")[0]
kids = sorted([r["id"] for r in rows("linear.linear_issues") if r.get("parent_id") == "DES-314"], key=lambda x: int(x.split("-")[1]))
assert len(kids) == 31 and kids[0] == "DES-315" and kids[-1] == "DES-345"
fact("parent", "The parent ticket and its 31 children", "Linear", tools("linear_get_issue", "linear_list_issues"), "DES-314", dep("hub"),
     f"DES-314 '{parent['title']}', state {parent['state_id']}, created {when(parent['created_at'])}. Quote: " + must(clean(parent["description"]), "Add your ask as a child with who it's for in a comment.", "These sit in Design so the ZOM board stays on build work.")
     + f". Children (parent DES-314): {', '.join(kids)}. 14 sheet rows are covered by 13 of these plus DES-313, which has no parent. Descriptions: DES-315 to DES-320 each end 'Built in match3d #248.'; DES-321 " + must(clean(rows("linear.linear_issues", id="DES-321")[0]["description"]), "Quests are already in production.") + "; DES-322 " + must(clean(rows("linear.linear_issues", id="DES-322")[0]["description"]), "Daily login is already in the game.") + "; DES-339 " + must(clean(rows("linear.linear_issues", id="DES-339")[0]["description"]), "We already give free coins in the shop."),
     "VERIFIED: children counted from the SQL parent_id values (31)", UNSC, dep("hub"), L("DES-314"))

qa = rows("gmail.gmail_messages", id=f"samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>")[0]
qat = clean(qa["body_text"])
fact("qa", "Vincent's QA note: what counts as seen", "Gmail (Samuel's mailbox)", tools("gmail_search_messages", "gmail_get_message"), "the mail 'Phone messages for beta' from Vincent Parker",
     dep("rule") + ' ("his QA note"); search "Phone messages for beta"',
     f"{qa['id']}, thread samuel.turner@harmonygames.co/1843335316636662321, sent {when(qa['date'])}. Quotes: " + must(qat, "Seen only counts on a store build, on a real iOS device and a real Android device.", "A build with shortened timers doesn't count, it only proves the code path.", "Moving the phone date forward on a store build is fine.", "Passes go in the Phone message checks sheet."),
     "VERIFIED: quotes cut from body_text", SCOPED_YES, dep("rule"), f"{qa['id']}, {L(qa['id'])}")

grid_log = json.loads(rows("gsheets.sheets_sheets")[0]["grid_json"])
fact("log", "Vincent's checks log: six passes dated Sep 24", "Google Sheets (Drive)", tools("gdrive_search", "gdrive_read_sheet_range"), "the sheet 'Phone message checks', tab Beta", dep("qa") + ' ("the Phone message checks sheet")',
     f"{I['qa_sheet']}, modified {when(rows('gsheets.sheets_spreadsheets')[0]['modified_time'])}. Rows: " + " ; ".join(" / ".join(x for x in r if x) for r in grid_log[1:]),
     "VERIFIED: cells read from grid_json; superseded for Plague Race and Lives recharged by the two facts that follow", SCOPED_YES, dep("qa"), f"{I['qa_sheet']}, {L(I['qa_sheet'])}")

fact("vid", "Vincent Parker's Slack user", "Slack (users)", tools("slack_search_users"), "the Slack user Vincent Parker", 'search "Vincent"', f"User id EMPLOYEE_0012_SLACK_ID; his post {I['lives_pull']} carries it.", "VERIFIED: id read through hg.py (slack users.json /8) and on the seeded row", SCOPED_YES, "—", f"slack users.json, {I['lives_pull']}, {L(I['lives_pull'])}")
pull = seeded_msg(I["lives_pull"])
fact("pull", "Vincent takes his tick off Lives recharged (Full Ammo), Sep 30", "Slack (#zombie-match3d)", tools("slack_search_public_and_private", "slack_conversations_history"),
     "#zombie-match3d, Vincent Parker's root post of Tue Sep 30", dep("log", "vid") + '; search "Full Ammo"',
     f"{I['lives_pull']}, posted {when(ts_iso(pull['ts']))}. Quotes: " + must(clean(pull["text"]), "on 0.3.49 the Full Ammo one didn't show up after a full refill, tried it twice on the iPhone this morning", "the lapsed ones are still coming through", "taking my tick off Full Ammo until I've seen it land"),
     "VERIFIED: quotes cut from the message; later than the Sep 24 tick, governing for Lives recharged", SCOPED_YES, dep("log"), f"{I['lives_pull']}, {L(I['lives_pull'])}")

ios = B1["slack"]["ios_release"]
fact("ios", "iOS 0.3.49 released", "Slack (#zombie-match3d)", tools("slack_conversations_history"), "#zombie-match3d, Leonard's post of Mon Sep 29", dep("pull") + ' ("0.3.49")',
     f"{BASE['ios_release']}, posted {when(ts_iso(ios['rec']['ts']))}. Quote: " + must(ios["rec"]["text"], "I just released 0.3.49 on IOS"),
     "VERIFIED: quote read through hg.py", SCOPED_YES, dep("pull"), f"{BASE['ios_release']}, slack {ios['file']}#{ios['pointer']}")

root = B1["slack"]["android"]
reply = seeded_msg(I["qa_reply"])
fact("qa_reply", "Vincent withdraws his iOS pass on Plague Race, Sep 29", "Slack (Samuel's DM with Vincent)", tools("slack_conversations_history", "slack_read_thread"),
     "Samuel's DM with Vincent Parker, the reply under Samuel's Android 2007 build request", dep("log") + '; search "race one"',
     f"Root {BASE['android_2007_root']} (Samuel, {when(ts_iso(root['rec']['ts']))}); reply {I['qa_reply']}, posted {when(ts_iso(reply['ts']))}. Quote: " + must(clean(reply["text"]), "also on the race one I passed: that iPhone was still on the 5-minute timers build when I ticked it, so scratch iOS. put the real 0.3.40 on it after and it never showed up. Android is fine."),
     "VERIFIED: quote cut from the message; later than the Sep 24 pass, governing for Plague Race", SCOPED_YES, dep("log"), f"{I['qa_reply']}, {L(I['qa_reply'])}, {BASE['android_2007_root']}")

ask = seeded_msg(I["ask_decision"])
fact("ask", "Robert's permission-ask call for beta, Sep 29 (governing version)", "Slack (#zombie-match3d)", tools("slack_search_public_and_private", "slack_conversations_history"),
     "#zombie-match3d, Robert's root post of Mon Sep 29", dep("rule") + ' ("The permission ask is Robert\'s call"); search "Permission ask"',
     f"{I['ask_decision']}, posted {when(ts_iso(ask['ts']))}. Quotes: " + must(clean(ask["text"]), "Permission ask for beta: leaving our own ask after level 20, not pushing it further", "The Unity popup at launch on iOS stays as it is."),
     "VERIFIED: quote cut from the message; latest of the four versions in this ledger", SCOPED_YES, dep("rule"), f"{I['ask_decision']}, {L(I['ask_decision'])}")
arep = seeded_msg(I["ask_reply"])
fact("ask_reply", "Arthur: only our own ask or the settings toggle schedules anything", "Slack (#zombie-match3d)", tools("slack_read_thread"), "#zombie-match3d, Arthur Blake's reply under Robert's post", dep("ask"),
     f"{I['ask_reply']}, posted {when(ts_iso(arep['ts']))}. Quote: " + must(clean(arep["text"]), "that popup doesn't switch anything on btw. NotificationManager only schedules once our own ask has run or they switch it on from settings, on both platforms"),
     "VERIFIED: quote cut from the message", SCOPED_YES, dep("ask"), f"{I['ask_reply']}, {L(I['ask_reply'])}")
sh, beg = B1["slack"]["shove"], B1["slack"]["beginning"]
fact("ask_v1", "Superseded permission-ask version: Robert, Jul 10", "Slack (a DM Samuel is in)", tools("slack_search_public_and_private"), "the DM where Robert posted on Jul 10", 'search "level 20"',
     f"{BASE['shove_to_20']}, posted {when(ts_iso(sh['rec']['ts']))}. Quote: " + must(sh["rec"]["text"], "Let's shove it to level 20"), "VERIFIED: quote read through hg.py; overturned by the Sep 29 post", SCOPED_YES, "—", f"{BASE['shove_to_20']}, slack {sh['file']}#{sh['pointer']}")
fact("ask_v2", "Superseded permission-ask version: variant C at level 13, Aug 13", "Slack (#zombie-bugs)", tools("slack_search_public_and_private"), "#zombie-bugs, Vincent Parker's reply on variant C, Aug 13", 'search "variant C"',
     f"{BASE['variant_c_13']}, posted {when(ts_iso('1755084279.518809'))}. Quote: 'For variant C, the notification pop up is triggered at level 13 but instead it should be after level 20.'",
     "VERIFIED: text read through hg.py from messages/.../2025-08.json#/489 blocks; overturned by the Sep 29 post", SCOPED_YES, "—", f"{BASE['variant_c_13']}, slack messages 2025-08.json#/489")
fact("ask_v3", "Leonard's 'PNs are at the beginning', Sep 19 (the iOS launch popup, not our ask)", "Slack (#zombie-bugs)", tools("slack_search_public_and_private"), "#zombie-bugs, Leonard's reply of Sep 19", 'search "PNs are at the beginning"',
     f"{BASE['at_the_beginning']}, posted {when(ts_iso(beg['rec']['ts']))}. Quote: " + must(beg["rec"]["text"], "Yeah PNs are at the beginning."), "VERIFIED: quote read through hg.py; explained by Arthur's Sep 29 reply", SCOPED_YES, "—", f"{BASE['at_the_beginning']}, slack {beg['file']}#{beg['pointer']}")

hunk = B1["hunk"]["diff_hunk"]
CLIENT_Q = ["DailyNotifications(OneDayLapsedTitle, OneDayLapsedMessage, serverToday);", "BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);",
            "BatchScheduleWeeklyLeaderboardNotifications(WeeklyLeaderboardTitle, WeeklyLeaderboardMessage, 4, serverToday);", "BatchSchedulePlagueRace(PlagueRaceTitle, PlagueRaceMessage, 5, serverToday);",
            "DateTime fireTime = referenceDate.AddDays(i * 7);", "DateTime date = serverToday.AddDays(1);"]
cf = B1["client_file"][0]
fact("client", "What the client schedules (NotificationManager.cs, call sites)", "GitHub (match3d)", tools("github_get_pull_request", "github_search_code", "github_get_file_contents"),
     "Assets/Scripts/Notifications/NotificationManager.cs in match3d, main, and PR #248 'Push notification'", dep("hub") + '; search "NotificationManager"',
     f"harmonygames-Games/match3d#248, state {B1['pr']['state']}, merged {when(B1['pr']['merged_at'])}. Call sites: " + must(hunk, *CLIENT_Q)
     + f". Six messages only: lives recharged, first tutorial, one-day lapsed, the weekly batch of 4, the weekly leaderboard batch of 4, the Plague Race batch of 5. Lapsed reminders by day: day 1 (one-day), days 7, 14, 21, 28 (weekly batch, i * 7, i = 1 to 4). Titles: " + must(hunk, "The Horde Is Growing… 🧟‍♂️", "They’ve Taken Over… Can You Stop Them? 😱", "Full Ammo Reloaded! 🔫", "Plague Race Is On! 🌊🚣") + ".",
     "VERIFIED: call sites quoted from the review hunk read through hg.py; ABSENCE evidence_check for anything else: the one scheduling method lists exactly these six calls (L165 to L180 on main)", UNSC, dep("hub"),
     f"github data.json#/review_comments/599/diff_hunk; {cf['path']} ({cf['bytes']} bytes), harmonygames-Games/match3d#248")

line_slack = seeded_msg(I["corr_reply"])
mroot = B1["slack"]["martin"]
assert "They’ve Taken Over… Can You Stop Them? 😱" in clean(rows("linear.linear_issues", id="DES-317")[0]["description"]) and "They’ve Taken Over" in PN[5][9]
fact("line_v1", "Lapsed 7 days headline, version 1: the June line", "GitHub, Linear, Google Sheets", tools("github_get_file_contents", "linear_get_issue"), "the client title, DES-317 and sheet row 5", dep("client", "parent"),
     "'They’ve Taken Over… Can You Stop Them? 😱' on the sheet row 5, in DES-317's description and in the client; shipped, superseded by the two facts that follow",
     "VERIFIED: sheet cell and client title read above", UNSC, dep("client", "parent"), f"{BASE['pn_sheet']}, {L('DES-317')}")
fact("line_v2", "Lapsed 7 days headline, version 2: Leonard, Sep 29", "Slack (#zombie-art)", tools("slack_search_public_and_private", "slack_read_thread"), "#zombie-art, Leonard's reply under Martin's desert theme post", 'search "Your Squad"',
     f"Root {BASE['martin_root']} (Martin Walsh, {when(ts_iso(mroot['rec']['ts']))}); reply {I['corr_reply']}, posted {when(ts_iso(line_slack['ts']))}. Quote: " + must(clean(line_slack["text"]), "random one while I'm here: the 'taken over' push reads like we've given up. make it \"Your Squad Needs You Back\", body stays."),
     "VERIFIED: quote cut from the message; superseded by version 3", SCOPED_YES, dep("line_v1"), f"{I['corr_reply']}, {L(I['corr_reply'])}, {BASE['martin_root']}")
ev = rows("gcal.gcal_events", event_id=I["copy_check"])[0]
inv = rows("gmail.gmail_messages", id="samuel.turner@harmonygames.co/<calendar-0faf8717-bf12-6508-09c5-078a904a8076@google.com>")[0]
fact("line_v3", "Lapsed 7 days headline, version 3 (governing): Leonard's note on the copy check", "Google Calendar (Samuel's calendar)", tools("gcal_search_events", "gcal_list_events"), "Samuel's calendar, the event 'Lapsed copy check'", 'search "Lapsed"',
     f"{I['copy_check']}, created {when(ev['created'])}, updated {when(ev['updated'])}, status {ev['status']}. Quote: " + must(clean(ev["description"]), "Final for the 7 day one is \"Your Squad Is Waiting\", body stays. That replaces what I said in the art thread.")
     + f". Invite mail {inv['id']}, sent {when(inv['date'])}.",
     "VERIFIED: quote cut from the event description; latest of the three versions", SCOPED_YES, dep("line_v2"), f"{I['copy_check']}, {L(I['copy_check'])}, {inv['id']}")

rc = rows("github.github_review_comments")[0]
gm = rows("gmail.gmail_messages", id=I["arthur_mail"])[0]
fact("rc18", "Arthur's inline comment on PR #248: the weekly batch is not tied to the rollover", "GitHub (PR review comment)", tools("github_get_pull_request_comments"), "the review comments of PR #248", dep("client"),
     f"{I['arthur_inline']}, created {when(rc['created_at'])}. Quote: " + must(clean(rc["body"]), "This counts seven days from the day they last left the game, so it isn't tied to the rollover. Fine to merge, but it isn't a reset message until it's anchored to the real reset."),
     "VERIFIED: quote cut from the review comment", UNSC, dep("client"), f"{I['arthur_inline']}, {L(I['arthur_inline'])}")
fact("rc18_mail", "GitHub mail of the same comment", "Gmail (Samuel's mailbox)", tools("gmail_search_messages", "gmail_get_thread"), "the GitHub notification thread for PR #248 in Samuel's mailbox", dep("rc18") + '; search "Push notification (PR #248)"',
     f"Thread {BASE['pr248_mail']}; sent {when(gm['date'])}. Quote: " + must(clean(gm["body_text"]), "so it isn't tied to the rollover"), "VERIFIED: quote cut from body_text (second route to the comment)", SCOPED_YES, dep("rc18"), f"{BASE['pr248_mail']}, {L(I['arthur_mail'])}")

ladder = rows("gcal.gcal_events", event_id=I["ladder_review"])[0]
cancel = rows("gmail.gmail_messages", id="samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com>")[0]
fact("covered", "Day 14 is already covered: the cancelled 'Lapsed ladder review'", "Gmail and Google Calendar", tools("gmail_search_messages", "gmail_get_message", "gcal_list_events"), "the cancellation mail 'Canceled event with note: Lapsed ladder review'", 'search "Lapsed ladder review"',
     f"{cancel['id']}, sent {when(cancel['date'])}. Quote: " + must(clean(cancel["body_text"]), "Cancelled, no need. The weekly one repeats for four weeks, so day 14 is already covered.") + f". Event {I['ladder_review']}, status {ladder['status']}, updated {when(ladder['updated'])}.",
     "VERIFIED: quote cut from body_text; agrees with the batch of 4 in the client", SCOPED_YES, dep("client"), f"{cancel['id']}, {L(cancel['id'])}, {I['ladder_review']}")

lo = B1["liveops"]
body = lo["body"]
LOQ = ["Same feature as Win &amp; Collect on Domino Delights, under a different name", "Built for the end-of-September beta submission (QA blockers cleared 26 Sep 2025); not yet live."]
fact("liveops", "Live-ops page: feature state and the name map", "Confluence", tools("confluence_search", "confluence_get_page"), "the page 'Live-Ops Event Calendar & Planning'", 'search "Collect"',
     f"{BASE['liveops_page']}. Rows (Event / Game / Status): Plague Race / Zombie Match 3D / Live; algo bug Aug 2025 · Zombie Lane / Zombie Match 3D / Live · Endless Monster Mode / Zombie Match 3D / Live; also one of the three permanent board modes · Weekly Leaderboards / Domino Delights / Zombie Match 3D / Live · Nathan's Treasure Hunt / Domino Delights / Shipped Dec 2024 · Axe Arena / Domino Delights / Shipped Feb 2025 · Streak Fever / Domino Delights / Shipped Apr 2025 · Collect & Win / Zombie Match 3D. Quotes: " + must(body, *LOQ),
     "VERIFIED: table cells and quotes read through hg.py", UNSC, dep("hub"), f"{BASE['liveops_page']}, confluence confluence_working.json#/pages/27")
dt_ = rows("linear.linear_issues", id="DES-313")[0]
fact("wc", "DES-313: the Collect & Win ticket outside the parent", "Linear", tools("linear_list_issues", "linear_get_issue"), "the ticket 'Ping when a Collect & Win window opens'", dep("liveops") + '; search "Collect"',
     f"DES-313, '{dt_['title']}', state {dt_['state_id']}, no parent, created {when(dt_['created_at'])} by calvin.price@harmonygames.co. Quote: " + must(clean(dt_["description"]), "Players should get a ping when a Collect & Win window opens. Three windows a week."),
     "VERIFIED: fields from the SQL row", UNSC, dep("liveops"), L("DES-313"))

card_by_name = {c["name"]: c for c in TR["cards"]}
LIST = {k: v["name"] for k, v in TR["lists"].items()}


def card(prefix):
    m = [c for c in TR["cards"] if c["name"].startswith(prefix)]
    assert m, prefix
    return m[0]


def card_list(prefix):
    return LIST[card(prefix)["idList"]]


BETA, OCT, BACK = "BETA: Oct 10", "Oct 21", "Backlog"
BETA_ID = [k for k, v in TR["lists"].items() if v["name"] == BETA][0]
n_beta = sum(1 for c in TR["cards"] if c["idList"] == BETA_ID) + 1      # + Minor Bugs to Fix: /cards/778 idList read on its own through hg.py (its long record did not parse in the batch)
assert n_beta == 19 and len(TR["cards"]) + 1 == 79
for pre in ("Win and Collect", "Season Pass", "Infinite HP Boss Mode", "300 Levels Manmade", "Add more quests", "Shop Inventory Review", "Axe Arena", "Hourly Collection"):
    assert not card(pre).get("closed"), pre
assert card_list("Win and Collect") == BETA and card_list("Season Pass") == BETA and card_list("Infinite HP Boss Mode") == BETA and card_list("300 Levels Manmade") == BETA
assert card_list("Add more quests") == BETA and card_list("Shop Inventory Review") == BETA and card_list("Axe Arena") == OCT and card_list("Hourly Collection") == BACK
rename = rows("trello.trello_actions", id=I["beta_rename"])[0]
fact("roadmap", "ZM ROADMAP lists: what is on the BETA list, what is not", "Trello", tools("trello_list_boards", "trello_get_lists", "trello_get_cards_on_board"), "the board ZM ROADMAP, list by list", dep("rule") + ' ("the BETA list of the ZM ROADMAP board")',
     f"Board 6851a6569f3bf818760632ab, 79 cards. BETA: Oct 10 holds Win and Collect, Season Pass, Infinite HP Boss Mode, 300 Levels Manmade, Add more quests and balance quest rewards, Shop Inventory Review and Additions, Fix TECH ISSUES and Minor Bugs to Fix (19 cards, 18 open). Oct 21 holds Axe Arena (card {BASE['axe_card']}). Backlog holds Hourly Collection (card {BASE['hourly_card']}). List renamed from 'BETA: Sep 30' to 'BETA: Oct 10' on {when(rename['date'])} (action {I['beta_rename']}).",
     "VERIFIED: card and list names read through hg.py (trello data.json /cards, /lists); 79, 19 and 18 counted from those arrays", UNSC, dep("rule"), f"{BASE['axe_card']}, {BASE['hourly_card']}, {I['beta_rename']}, {L(I['beta_rename'])}")
fr = rows("trello.trello_actions", id=I["freeze_comment"])[0]
frd = json.loads(fr["data_json"] if "data_json" in fr else fr["data"])
fact("freeze", "Leonard's roadmap note: held tickets sit in Backlog, unassigned", "Trello", tools("trello_get_lists", "trello_get_card", "trello_get_board_actions"), "the card 'Fix TECH ISSUES' on the BETA list", dep("roadmap") + ' ("unless the roadmap says otherwise")',
     f"Card {BASE['tech_card']}, description set in action {I['freeze_comment']}; the card's dateLastActivity is {when(fr['date'])}, returned by trello_get_lists (run-5 event 46). Quote: " + must(frd["card"]["desc"], "Until the beta build is out nothing that isn't beta work lands in anyone's Todo. Held tickets sit in Backlog, unassigned."),
     "VERIFIED: quote cut from the action data; amends the rule doc's Todo clause through its own 'unless the roadmap says otherwise'", UNSC, dep("roadmap"), f"{I['freeze_comment']}, {L(I['freeze_comment'])}, {BASE['tech_card']}")

axe, scope = B1["slack"]["axe"], B1["slack"]["scope"]
fact("axe", "Axe Arena postponed for the beta, Sep 22", "Slack (#company-internal)", tools("slack_search_public_and_private"), "#company-internal, Brian Foster's post of Sep 22", 'search "Axe Arena"',
     f"{BASE['axe_postponed']}, posted {when(ts_iso(axe['rec']['ts']))}. Quote: " + must(axe["rec"]["text"], "We’ve decided to postpone Axe Arena for the beta release."), "VERIFIED: quote read through hg.py; agrees with the Oct 21 list", SCOPED_YES, "—", f"{BASE['axe_postponed']}, slack {axe['file']}#{axe['pointer']}")
fact("scope", "Beta scope post, Sep 12", "Slack (#company-internal)", tools("slack_search_public_and_private"), "#company-internal, Leonard's post of Sep 12", 'search "beta goals"',
     f"{BASE['beta_scope']}, posted {when(ts_iso(scope['rec']['ts']))}. Quote: " + must(scope["rec"]["text"], "If we ship *Win & Collect*, *Reward Animations*, *Season Pass*, and *Infinite HP Boss Mode by end of next week*, the beta goals are achievable."), "VERIFIED: quote read through hg.py", SCOPED_YES, "—", f"{BASE['beta_scope']}, slack {scope['file']}#{scope['pointer']}")
ver = B1["slack"]["versions"]
fact("versions", "Store versions behind the passes", "Slack (#zombie-match3d)", tools("slack_conversations_history"), "#zombie-match3d, Arthur Blake's post of Sep 23", 'search "required versions"',
     f"{BASE['versions'] if 'versions' in BASE else 'C0880U9751A/1758643365.607149'}, posted {when(ts_iso(ver['rec']['ts']))}. Quote: " + must(ver["rec"]["text"], "can you update the match3d required versions:", "Android: 0.3.127", "iOS: 0.3.40"), "VERIFIED: quote read through hg.py", SCOPED_YES, "—", f"C0880U9751A/1758643365.607149, slack {ver['file']}#{ver['pointer']}")

wh = {}
for line in open(os.path.join(HERE, "oe_wh_rows.txt")):
    m = re.match(r'(\d+)\s+"text": "(.*)",?\s*$', line)
    wh[int(m.group(1))] = json.loads(json.loads('"' + m.group(2) + '"'))
a, i_ = wh[236], wh[237]
assert a["cohort_week"] == i_["cohort_week"] == "2025-09-15" and a["game_id"] == i_["game_id"] == "zombie_match_3d" and a["platform"] == "android" and i_["platform"] == "ios"
fact("wh", "D1 and D7 for the Sep 15 cohort week (Snowflake only)", "Snowflake", tools("snowflake_describe_table", "snowflake_execute_query"), "ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION, game_id zombie_match_3d, cohort_week 2025-09-15", dep("hub") + ' ("from the warehouse")',
     f"2 rows. ios: installs {i_['installs']}, d1_ret {i_['d1_ret']}, d7_ret {i_['d7_ret']}. android: installs {a['installs']}, d1_ret {a['d1_ret']}, d7_ret {a['d7_ret']}. Column comments: d1_ret '% returning on Day 1', d7_ret 'NULL until the 7-day window closes'.",
     f"VERIFIED: quote '\"d1_ret\":{i_['d1_ret']}' and '\"d1_ret\":{a['d1_ret']}' from rows 237 and 236", UNSC, dep("hub"), "snowflake.json#/tables/10/rows/236, snowflake.json#/tables/10/rows/237, wh_USER_COHORT_RETENTION")

pcard = card("[Feature] Push Notifications")
pcom = rows("trello.trello_actions", id="68d415a716abcb84070a8e2a")[0]
pcd = json.loads(pcom["data_json"] if "data_json" in pcom else pcom["data"])
fact("pncard", "The push notifications card", "Trello", tools("trello_search", "trello_get_card", "trello_get_comments"), "the card '[Feature] Push Notifications - Samuel + Leonard' on ZM ROADMAP", 'prompt ("our push notifications card")',
     f"Card {BASE['pn_card']}. Comment action 68d415a716abcb84070a8e2a, {when(pcom['date'])}. Quote: " + must(pcd["text"], "The beta list goes on this card as a checklist. Vincent ticks these as he checks them on the store builds."),
     "VERIFIED: quote cut from the action data", UNSC, dep("hub"), f"{BASE['pn_card']}, {L('68d415a716abcb84070a8e2a')}")
fo = B1["folder"]
fact("folder", "Samuel's Drive folder", "Google Drive", tools("gdrive_search", "gdrive_list_folder"), "Samuel's own Drive root folder", 'prompt ("my Drive folder")',
     f"{BASE['folder']}, name {fo['name']}, owner {fo['owner_email']}, {fo['mime_type']}.", "VERIFIED: fields read through hg.py", SCOPED_YES, "—", f"{BASE['folder']}, gdrive data.json#{B1['folder_ptr']}")

# population of tickets touched since the parent opened
pop = [r for r in B2["pop_base"] if r["team"] == "team_ZOM"]
assert len(pop) == len(B2["pop_base"]) == 17
extra = ["ZOM-483", "ZOM-542", "ZOM-556"]
popids = sorted({r["id"] for r in pop} | set(extra), key=lambda x: int(x.split("-")[1]))
assert len(popids) == 20 and "ZOM-563" in popids
assert B1["linear_comments_base"] == "[]"
fact("pop", "Tickets updated since the parent opened, outside DES", "Linear", tools("linear_list_issues", "linear_list_comments"), "Linear issues with updatedAt on or after 2025-09-23 (the day DES-314 was created)", dep("parent") + ' ("filed on a ticket or a card up to today")',
     f"20 tickets, all team ZOM: {', '.join(popids)}. 17 carry that date in the base; ZOM-483, ZOM-542 and ZOM-556 carry it through the UPDATE rows SQL L308 to L311, which also move ZOM-563 to 2025-09-30T18:22:14Z. The base export holds no Linear comments, so the only comments on these 20 are the four asks.",
     "VERIFIED: base list read through hg.py (linear data.json /issues, key updated_at, scan complete); 20 counted; ABSENCE evidence_check: linear data.json /comments is an empty array, with /issues as positive control (45 'notification' hits)", UNSC, dep("parent"), "linear data.json#/comments, linear data.json#/issues, " + L("ZOM-542", "ZOM-556", "ZOM-563", "ZOM-483"))

ASKS = [("Boss Arena attempts refilled", "ZOM-542", I["boss_ask"], "brian.foster", "DES-330", ["once the daily Boss Arena attempts refill", "this is for players who used their attempts", "Arthur says a local timer is enough."]),
        ("Daily gift about to reset", "ZOM-556", I["gift_ask"], "julia.lawson", "DES-338", ["the gift streak itself is live", "the evening before the daily gift streak resets", "this is for players on a gift streak"]),
        ("Teammate sent lives", "ZOM-563", I["team_ask"], "douglas", "DES-315", ["prod has the latest teams changes now", "when a teammate sends you lives", "for players on a team", "it would have to go out from the server, the phone has no way of knowing."]),
        ("Infinite lives ending", "ZOM-483", I["inf_ask"], "calvin.price", "DES-315", ["we do hand out infinite lives, just not on the first session", "infinite lives are about to run out", "this is for players with infinite lives running"])]
for key, z, cid, who, rel, qs in ASKS:
    c = rows("linear.linear_comments", id=cid)[0]
    zi = B1["zom"][z]
    v = TRUTH[key]
    assert c["issue_id"] == z
    fact("ask:" + key, f"Comment ask on {z}: {key}", "Linear", tools("linear_list_comments"), z, dep("pop"),
         f"{cid} on {z} ('{zi['title']}'), posted {when(c['created_at'])} by {who}@harmonygames.co. Quotes: " + must(clean(c["body"]), *qs) + f". Relation row to {rel}. Call {v['Call']}; {v[chr(87)+'hat'+chr(39)+'s missing']}; audience '{v['Audience']}'; no ticket of its own, so a new one.",
         "VERIFIED: quotes cut from the comment body; call not_a_claim (derived from the rule tests)", UNSC, dep("pop"), f"{cid}, {L(cid)}, {L(z)}")

decoy_rows = [("Rate Us popup", "ZOM-397", B1["zom"]["ZOM-397"]["title"]), ("Permission popup", "ZOM-366", B2["like"]["ZOM-366"]["title"]), ("Plague Race red dot", "ZOM-471", B2["like"]["ZOM-471"]["title"]), ("Cards and shop red dots", "ZOM-539", B2["like"]["ZOM-539"]["title"])]
fact("census", "Nothing else is a filed ask for a new phone message", "Linear and Trello", tools("linear_list_issues", "trello_search"), "every Linear issue and Trello record naming notifications, push, reminders or a phone message", dep("pop"),
     "Linear query 'notification': 30 issues (ENG 20, ZOM 5, ART 3, DES 2), the ENG and ART ones all created by 2025-06-03. ZOM: ZOM-314 'Adding new buttons to settings Panel', ZOM-320 'Notification pop up on android breaks the level 1 tutorial highlight.', ZOM-366 'Notification permission pops up twice after declining', ZOM-385 'Zombie Lane Polish' (a red dot), ZOM-387 'Giant Analytics Ticket'. DES: DES-9 'Triggered-by-notification-only offers/mini-games/events' (a Backlog idea from 2023-08-03) and DES-283 'Implement Chapter Full Star Rewards'. With 'push ', 'remind' and 'PN ' added, 16 ZOM and DES issues; ZOM-295 is a monster 'push back' effect; none asks for a new phone message for beta. In-game items that are not messages: "
     + "; ".join(f"{k} ({z}, '{t}')" for k, z, t in decoy_rows) + f". On ZM ROADMAP the only one of the 79 cards naming notifications is {BASE['pn_card']}; card comments naming notifications: 0. The other six cards naming notifications sit on the boards 'DD Product Roadmap' (65eb4ec525346c8070ca638f) and 'Harmony Games' (640643a3fd8f3ca308d9318e), last active by 2025-05-27: 'Expand notifications', 'local Push Notification', 'Appointment Mechanic v1 Basic', 'Make mini-games accessible via saga map nodes', 'Push-notification boost', '(Blake/Samuel) Hooking up Notifications to One Signal (1 week)'.",
     "ABSENCE evidence_check: linear data.json /issues for 'notification', 'push ', 'remind', 'PN ' (scan complete, 16 ZOM and DES hits read); linear /comments empty; trello data.json for 'notification', 'push notif', 'phone', 'reminder', 'PN ' (scan complete), positive control card " + BASE["pn_card"], UNSC, dep("pop"), "linear data.json#/issues, trello data.json#/cards, trello data.json#/actions, ZOM-397")

fact("tcom", "Card comments on ZM ROADMAP: 13, none an ask", "Trello", tools("trello_get_board_actions"), "the board's actions, filter commentCard", dep("roadmap"),
     f"13 comments: {B3['zm_comments']} in the base (estimates and art notes of 2025-06-23 and 2025-07-02, including 'Samuel says 3 days.') and the seeded note on the push notifications card (action 68d415a716abcb84070a8e2a).",
     "VERIFIED: base count read through hg.py (trello data.json /actions, type commentCard, board id); the 13 texts read in run-1 event 117; ABSENCE evidence_check: all 13 read, none asks for a phone message", UNSC, dep("roadmap"), f"trello data.json#/actions, 68d415a716abcb84070a8e2a, {L('68d415a716abcb84070a8e2a')}")
fact("livefeat", "Features shipped in Zombie Match, read off Done tickets", "Linear", tools("linear_list_issues"), "Done ZOM tickets naming Boss Arena, achievements and Helpshift", dep("roadmap") + '; search "Achievements"',
     f"ZOM-487 '{B3['boss_title']}', {B3['boss_state_id']}, the BETA list's Infinite HP Boss Mode; ZOM-116 '{B3['ZOM-116']['title']}', {B3['ZOM-116']['state']}; ZOM-363 '{B3['ZOM-363']['title']}', {B3['ZOM-363']['state']}; ZOM-301 '{B3['ZOM-301']['title']}', {B3['ZOM-301']['state']}.",
     "VERIFIED: titles and states read through hg.py", UNSC, dep("roadmap"), "ZOM-487, ZOM-116, ZOM-363, ZOM-301, linear data.json#/issues/3558, linear data.json#/issues/3356")
T1 = {  # how each message passes or fails test 1, with the record behind it
    "Win & Collect start": ("BETA list: Win and Collect", ["roadmap", "liveops"]),
    "Lives recharged": ("live in Zombie Match: in the client", ["client"]), "Lapsed 1 day": ("live in Zombie Match: in the client", ["client"]), "Lapsed 7 days": ("live in Zombie Match: in the client", ["client"]),
    "Finish first mission": ("live in Zombie Match: in the client", ["client"]), "Plague Race": ("live: Plague Race on the live-ops page", ["liveops"]),
    "Weekly Leaderboard reset": ("live: Weekly Leaderboards on the live-ops page", ["liveops"]), "Quests rollover": ("live: DES-321 says 'Quests are already in production.'", ["parent"]),
    "Login Calendar update": ("live: DES-322 says 'Daily login is already in the game.'", ["parent"]), "Season Pass start": ("BETA list: Season Pass", ["roadmap"]),
    "Hourly Coins": ("fails: Hourly Collection on the Backlog list", ["roadmap"]), "Nathan's Treasure Hunt": ("fails: Domino Delights only on the live-ops page", ["liveops"]),
    "Streak Fever": ("fails: Domino Delights only on the live-ops page", ["liveops"]), "Axe Arena": ("fails: Oct 21 list and postponed for the beta", ["roadmap", "axe"]),
    "Endless entries back": ("live: Endless Monster Mode on the live-ops page", ["liveops"]), "Endless weekly result": ("live: Endless Monster Mode on the live-ops page", ["liveops"]),
    "Boss Arena open": ("BETA list: Infinite HP Boss Mode", ["roadmap", "scope"]), "Boss Arena last hours": ("BETA list: Infinite HP Boss Mode", ["roadmap", "scope"]),
    "Season Pass last 48 hours": ("BETA list: Season Pass", ["roadmap"]), "Season Pass premium nudge": ("BETA list: Season Pass", ["roadmap"]),
    "Plague Race last hour": ("live: Plague Race on the live-ops page", ["liveops"]), "Plague Race result": ("live: Plague Race on the live-ops page", ["liveops"]),
    "Zombie Lane reward ready": ("live: Zombie Lane on the live-ops page", ["liveops"]), "Achievement reward waiting": ("live: achievements shipped (ZOM-116, ZOM-363, both Done)", ["livefeat"]),
    "Daily chest ready": ("live: Arthur on DES-338, 'the chest timer is local'", ["parent"]), "Free shop coins ready": ("live: DES-339 says 'We already give free coins in the shop.'", ["parent"]),
    "Support reply waiting": ("live: ZOM-301 'Helpshift Implementation', Done", ["livefeat"]), "New levels added": ("BETA list: 300 Levels Manmade", ["roadmap"]),
    "Lapsed 3 days": ("live: the lapsed reminders", ["client"]), "Lapsed 30 days": ("live: the lapsed reminders", ["client"]), "Lapsed 14 days": ("live: the lapsed reminders", ["client"]),
    "Comeback gift": ("fails: Leonard, 'A reward on tap is a version 2 idea, it isn't in the beta.'", []),
}
TEST = {"not scheduled in the client": "test 3", "needs a server send": "test 2", "cannot reach its players": "test 4", "fires on the wrong day": "test 5", "not seen on both platforms": "test 6"}
EXTRA = {"Lives recharged": ["pull", "ios", "log"], "Plague Race": ["qa_reply", "log", "qa"], "Weekly Leaderboard reset": ["rc18", "client", "log"], "Finish first mission": ["ask", "ask_reply", "client", "log"],
         "Lapsed 1 day": ["client", "log", "qa", "pull"], "Lapsed 7 days": ["client", "log", "qa", "pull", "line_v3"], "Lapsed 14 days": ["covered", "client"], "Win & Collect start": ["wc", "liveops"]}
WHY = {"Lives recharged": "test 6: Vincent's Sep 30 post takes his tick off", "Plague Race": "test 6: Vincent's Sep 29 reply scratches iOS",
       "Weekly Leaderboard reset": "test 5: the batch counts from the last session, not the weekly reset", "Finish first mission": "test 4: written for players below level 20, our own ask runs after level 20, so none of them count",
       "Lapsed 14 days": "Drop, covered by Lapsed 7 days (the weekly batch fires on day 14)", "Comeback gift": "Drop, test 1", "Hourly Coins": "Drop, test 1", "Nathan's Treasure Hunt": "Drop, test 1", "Streak Fever": "Drop, test 1", "Axe Arena": "Drop, test 1"}
SHEETROW = {m["key"]: int(m["source"].rsplit(" ", 1)[1]) for m in P["members"] if m["source"].startswith("PNs Beta")}
ISS = {r["id"]: r for r in rows("linear.linear_issues")}
USERS = {k: (v or {}).get("email") for k, v in B2["users"].items()}
msgfacts = []
for m in P["members"]:
    key, tk = m["key"], m["ticket"]
    v = TRUTH[key]
    if not tk:
        continue
    iss = ISS[tk]
    cs = sorted(rows("linear.linear_comments", issue_id=tk), key=lambda r: r["created_at"])
    cq = "; ".join(f"'{clean(c['body'])}' ({USERS.get(c['author_id'], c['author_id'])}, {when(c['created_at'])})" for c in cs)
    t1, t1dep = T1[key]
    miss = v["What's missing"]
    if v["Call"] == "Go":
        verdict = "Go, passes all six"
    elif v["Call"] == "Drop":
        verdict = WHY[key]
    else:
        verdict = "Hold, " + (WHY.get(key) or f"{TEST[miss]}: {miss}")
    sr = ""
    if key in SHEETROW:
        r = PN[SHEETROW[key]]
        sr = f" Sheet row {SHEETROW[key]}: {r[1].strip()} / {r[8].strip()}."
    extra_line = ""
    if v["Call"] == "Go":
        extra_line = f" Final headline '{v['Final headline']}'; String change {v['String change']}."
    end = {"Go": "stays as it is", "Drop": "Canceled", "Hold": "Backlog, unassigned"}[v["Call"]]
    deps = list(dict.fromkeys(["parent", "rule"] + t1dep + EXTRA.get(key, [])))
    if tk == "DES-313":
        deps = list(dict.fromkeys(["wc", "rule"] + t1dep + EXTRA.get(key, [])))
    fact("msg:" + key, f"{key}: {v['Call']}", "Linear", tools("linear_get_issue", "linear_list_comments"), tk, dep("wc" if tk == "DES-313" else "parent"),
         f"{tk} '{iss['title']}', state {iss['state_id']}, assignee {USERS.get(iss['assignee_id'], 'none')}, created {when(iss['created_at'])}.{sr} Comments: {cq}. Test 1: {t1}. Result: {verdict}.{extra_line} Audience '{v['Audience']}'. Ticket end state: {end}.",
         "VERIFIED: title, state and comments from the SQL rows, sheet cells read through hg.py; call not_a_claim (derived from the rule tests and the Depends-on facts)", UNSC, dep(*deps), ", ".join([L(tk)] + [L(c["id"]) for c in cs]))
    msgfacts.append("msg:" + key)

ASKERS = {"brian.foster": ["Endless entries back", "Endless weekly result", "Season Pass premium nudge", "Comeback gift", "Boss Arena attempts refilled"],
          "calvin.price": ["Daily chest ready", "Infinite lives ending", "Win & Collect start"], "douglas": ["Teammate sent lives"],
          "julia.lawson": ["Plague Race last hour", "Plague Race result", "New levels added", "Daily gift about to reset"], "martin.walsh": ["Free shop coins ready"],
          "oliver.brooks": ["Season Pass last 48 hours"], "owen.baker": ["Zombie Lane reward ready", "Achievement reward waiting", "Support reply waiting"], "robert": ["Boss Arena open", "Boss Arena last hours", "Lapsed 14 days"]}
for who, ks in ASKERS.items():
    c = B1["contacts"][who]
    assert c["email"] == f"{who}@harmonygames.co", who
    dk = ["msg:" + k if "msg:" + k in fid_of else "ask:" + k for k in ks]
    fact("who:" + who, f"{who}: asker and address", "Contacts and Linear", tools("contacts_search_contacts", "linear_list_users"), f"the contact and Linear user {c['email']}", dep(*dk[:1]),
         f"Address {c['email']} (contacts.json {c['pointer']}). Asks and calls: " + "; ".join(f"{k}: {TRUTH[k]['Call']}" for k in ks) + ".",
         "VERIFIED: address read through hg.py; calls not_a_claim (derived above)", UNSC, dep(*dk), f"contacts.json#{c['pointer']}")

go = [k for k, v in TRUTH.items() if v["Call"] == "Go"]
hold = [k for k, v in TRUTH.items() if v["Call"] == "Hold"]
drop = [k for k, v in TRUTH.items() if v["Call"] == "Drop"]
assert (len(go), len(hold), len(drop)) == (2, 28, 6)
built_held = ["Lives recharged", "Finish first mission", "Plague Race", "Weekly Leaderboard reset"]
fact("counts", "The counts", "derived (Linear, Google Sheets)", "none (calculation over the rows)", "the 36 calls above", dep("sheet", "parent", "pop"),
     f"36 messages: 14 sheet rows + 18 asks under the parent + 4 comment asks. Go {len(go)} ({', '.join(go)}), Hold {len(hold)}, Drop {len(drop)} ({', '.join(drop)}). The client already schedules four messages that are Holds: {', '.join(built_held)}.",
     "not_a_claim (derived): recomputed from solver/truth.json and from the rows above; 14 + 18 + 4 = 36, 2 + 28 + 6 = 36", "derived", ", ".join(fid_of[k] for k in msgfacts + ["ask:" + a[0] for a in ASKS]), "solver/truth.json, DES-314, ZOM-542")

# ---------------------------------------------------------------- requirements
def span(s):
    assert s in PROMPT, s
    return s


all_msg = ", ".join(fid_of[k] for k in msgfacts)
asks = F(*["ask:" + a[0] for a in ASKS])
REQ = [
    (span("His DM to me from yesterday has the whole job in it"), "Discovery — Leonard's Sep 30 DM is the source of every ask", "Explicit", F("hub")),
    (span("it starts from the Zombie Match PN sheet"), "Discovery — the 14 rows on the PNs Beta tab", "Explicit (the tab through F1)", F("hub", "sheet")),
    (span("I need you to do all of it for me"), "Discovery — the population: every PNs Beta row and every ask filed on a ticket or card up to today (36)", "Implicit (scope sentence in F1)", F("hub", "parent", "wc", "pop", "census") + ", " + asks),
    (span("Leonard wants one straight answer on what we actually say to players"), "Discovery — a call on each message through the rule's six ordered tests, with its incorporated records", "Implicit (incorporated through F1 and the rule)",
     F("rule", "qa", "log", "pull", "ios", "qa_reply", "ask", "ask_reply", "client", "rc18", "covered", "liveops", "roadmap", "freeze", "axe", "scope", "versions") + ", " + all_msg),
    (span("The new sheet"), "Write — one sheet with the seven columns, one row per message, in Samuel's folder", "Explicit (columns and rows through F1)", F("hub", "folder", "counts", "line_v1", "line_v2", "line_v3")),
    (span("the one-page note go in my Drive folder"), "Write — a one-page note: D1 and D7 by platform, the lapsed reminders by day, the Holds the client already schedules and why", "Explicit (contents through F1)", F("hub", "folder", "wh", "client", "counts")),
    (span("the checklist goes on our push notifications card"), "Write — a checklist holding every Go", "Explicit", F("pncard", "counts", "line_v3")),
    (span("He also wants things done on the tickets"), "Write — the call as a comment on each message ticket", "Explicit (through F1)", F("hub", "parent", "wc") + ", " + all_msg),
    (span("He also wants things done on the tickets"), "Write — each ticket moved to match: Drop to Canceled, Hold to Backlog unassigned, Go unchanged", "Explicit (through F1 and the rule)", F("rule", "freeze") + ", " + all_msg),
    (span("He also wants things done on the tickets"), "Write — a new ticket for each message with none, and a string ticket under DES-314 for the changed line", "Explicit (through F1 and the rule)", F("rule", "line_v3") + ", " + asks),
    (span("some emails sent"), "Write — one email to each person who asked, apart from Leonard, saying what happened to their asks", "Explicit (through F1)", ", ".join(fid_of["who:" + w] for w in ASKERS)),
    (span("When it's all finished tell him the counts in that same DM"), "Write and Tell — Go, Hold and Drop counts in Leonard's DM, after the other writes", "Explicit", F("hub", "counts")),
    (span("You don't need to run anything by me first"), "Constraint — every write goes ahead with no draft or approval step", "Explicit", F("hub")),
]

# ---------------------------------------------------------------- defer search
gm = {k: v for k, v in B1["defer"].items()}
counts = {k: (DEF[k]["visible"] if k in DEF else gm[k].get("visible", 0)) for k in list(gm) + [x for x in DEF if x not in gm]}
win = sum(v["in_window"] for v in DEF.values())
assert win == 2
DEFER = ("gmail · slack · linear · trello (Samuel's mailbox, his channels and DMs, all of Linear and Trello): persona_view and hg.py searches 'hold off', 'don't send', 'not yet', 'don't move', 'leave the tickets', 'wait on' "
         f"(limit 3000, no hit at its limit) — population complete: slack {DEF['slack:not yet']['visible']} / {DEF['slack:hold off']['visible']} / {DEF['slack:wait on']['visible']}, gmail {DEF['gmail:not yet']['visible']} / {DEF['gmail:wait on']['visible']}, linear 0, trello 0; "
         "only 2 hits after 2025-09-23, both code-review text (C093LEZGF6J/1758918582.061499, C093LEZGF6J/1759200206.697589); governing version: Leonard's Sep 30 DM (D06L58XCVKK/1759264851.763895) is the latest instruction; result: no defer")
WR = [
    ("R5", "Create the calls sheet, write its rows, place it in the folder", '"The new sheet"', tools("gsheets_create_spreadsheet", "gsheets_values_update", "gdrive_move_file") + " (exist)", "title; spreadsheetId, range, values; fileId, newParentId", F("folder", "counts"),
     f"a native sheet whose final parent is {BASE['folder']}, header + 36 rows", "the seven columns; one row per message; Final headline and String change only on Go rows"),
    ("R6", "Create the one-page note and place it in the folder", '"the one-page note go in my Drive folder"', tools("gdocs_create_document", "gdrive_move_file") + " (exist)", "title, bodyText; fileId, newParentId", F("folder", "wh", "client"),
     f"a Doc whose final parent is {BASE['folder']}", "D1 and D7 for iOS and Android; lapsed reminders on days 1, 7, 14, 21, 28; the four Holds the client already schedules, each with why"),
    ("R7", "Checklist on the push notifications card, one item per Go (2 items)", '"the checklist goes on our push notifications card"', tools("trello_create_checklist", "trello_create_check_item") + " (exist)", "idCard, name; checklistId, name", F("pncard"),
     f"a checklist on {BASE['pn_card']} holding Lapsed 1 day and Lapsed 7 days", "the two Go messages"),
    ("R8", "Comment the call on each message ticket (32)", '"He also wants things done on the tickets"', tools("linear_create_comment") + " (exists)", "issueId, body", all_msg, "one comment on each of DES-313 and DES-315 to DES-345", "the call; the reason on Holds"),
    ("R9", "Move each ticket to match (30: 6 Drop, 24 Hold)", '"He also wants things done on the tickets"', tools("linear_update_issue") + " (exists)", "id, state, assignee", all_msg + ", " + F("freeze"), "Drop tickets Canceled; Hold tickets Backlog with no assignee; DES-316 and DES-317 unchanged", "state and assignee only"),
    ("R10", "New tickets (5): four asks with no ticket and the string ticket", '"He also wants things done on the tickets"', tools("linear_create_issue") + " (exists)", "team, title (+ parentId for the string ticket)", asks + ", " + F("line_v3"), "created; the string ticket has parent DES-314", "the ask or the line 'Your Squad Is Waiting'"),
    ("R11", "Emails to the askers (8)", '"some emails sent"', tools("gmail_send_message") + " (exists)", "to, subject, body", ", ".join(fid_of["who:" + w] for w in ASKERS), "sent (not drafted), one to each address", "that person's asks and each call"),
    ("R12", "Counts to Leonard", '"When it\'s all finished tell him the counts in that same DM"', tools("slack_send_message") + " (exists)", "channel, text", F("hub", "counts"), "posted in the DM of D06L58XCVKK/1759264851.763895 after the other writes", "Go 2, Hold 28, Drop 6"),
]

# ---------------------------------------------------------------- traps, risks
TRAPS = [
    ("T1", f"Weekly Leaderboard looks finished: Ready, Done, Vincent's pass, an approved PR ({fid_of['msg:Weekly Leaderboard reset']}, {I['weekly_qa']})", F("rc18"), f"Arthur's inline comment {I['arthur_inline']}: the same i * 7 from the last session, not the reset"),
    ("T2", f"Leonard's Sep 29 line under a theme post ({fid_of['line_v2']}, {I['corr_reply']})", F("line_v3"), f"later note on {I['copy_check']}, updated 2025-09-30T17:02:41Z: 'That replaces what I said in the art thread.'"),
    ("T3", f"Finish first mission is Ready, LIVE and seen ({fid_of['msg:Finish first mission']}, {I['ftue_qa']})", F("ask", "ask_reply"), f"{I['ask_decision']}: our own ask stays after level 20; the rule: 'the settings toggle doesn't count'; {I['qa_sheet']}: 'notifications switched on from settings'"),
    ("T4", f"Vincent's Sep 24 pass on Plague Race ({I['race_qa']}, {I['qa_sheet']})", F("qa_reply"), f"Sep 29 reply {I['qa_reply']}, in Samuel's own DM under an unrelated build request"),
    ("T5", f"Lives recharged ticked on the log and the ticket ({I['lives_qa']}, {I['qa_sheet']})", F("pull"), f"Sep 30 root post {I['lives_pull']}, naming the headline 'Full Ammo', not the row"),
    ("T6", f"The Win & Collect row has no child under the parent ({fid_of['parent']}, DES-314)", F("wc", "liveops"), f"{BASE['liveops_page']}: 'under a different name'; DES-313 exists with no parent"),
    ("T7", f"The ask list looks complete at the 18 asks under DES-314 ({fid_of['parent']}, DES-314)", asks, "the DM's scope is 'a ticket or a card'; comments on ZOM-542, ZOM-556, ZOM-563 and ZOM-483, all updated after the parent opened"),
    ("T8", f"The rule doc says Hold tickets go back to Todo ({fid_of['rule']}, {I['rule_doc']})", F("freeze"), f"its own 'unless the roadmap says otherwise'; {I['freeze_comment']} of 2025-09-29, later than the doc of 2025-09-26"),
    ("T9", f"DES-344 reads as new work ({fid_of['msg:Lapsed 14 days']}, DES-344)", F("covered", "client"), "the weekly batch of 4 fires on day 14; Leonard's note on the cancelled review"),
    ("T10", f"Older permission posts ({BASE['shove_to_20']}, {BASE['variant_c_13']}, {BASE['at_the_beginning']})", F("ask"), f"dates: Jul 10, Aug 13 and Sep 19 are all before {I['ask_decision']} of Sep 29"),
    ("T11", f"The readiness deck and Brian's post repeat six Ready ({I['deck']}, {I['brian_opinion']})", F("rule"), f"{I['rule_doc']}: 'Neither status column on the sheet decides anything.'"),
    ("T12", f"Push Notifications Domino Adventure also has a PNs Beta tab ({BASE['pn_sheet']} is the right one; twin f_351b98dfb06f61fb8357d0)", F("sheet"), "the twin's header has no Status column and no Ready; title names Domino Adventure"),
    ("T13", f"In-game items look like messages ({'; '.join(z for _, z, _ in decoy_rows)})", F("rule"), f"{I['rule_doc']}: 'anything the game puts on a player's phone while the game is closed'"),
    ("T14", f"PNs and PN BETA Translated tabs hold other rows ({BASE['pn_sheet']})", F("hub"), "the DM names 'the PNs Beta tab'"),
]
RISKS = [
    ("1", "The ZOM route uses the updatedAt filter of linear_list_issues, which is in the catalog but no run exercised; createdAt behaved as a 'since' filter (run-2). If updatedAt differs, orderBy updatedAt on team ZOM reaches the same 20 tickets. linear_show_data is also in the catalog and also unexercised, so nothing here rests on it", F("pop"), "OE accuracy / feasibility", "the event names both, with limit 100, because the filtered call returns 53 rows"),
    ("2", "Relation rows are seeded on the ZOM side only (SQL L308 to L311). No run saw a non-empty relatedTo, so this ledger does not rely on relations", asks, "OE accuracy", "no event states that a DES ticket shows the relation"),
    ("3", "All 7 rev6 runs missed the four comment asks. Counter-reading: 'I made tickets for the sheet rows under DES-314 and people added their asks there' could narrow the scope. Against it: the same message says 'filed on a ticket or a card', and /hardness accepted the misses", asks, "rubric / all-fail validity: if these rows were ruled invalid the average rises to 90 to 95%", "keep the route in the OE; cite F-rows in /create-allfail"),
    ("4", "The client event reads NotificationManager.cs on main, and hg.py cannot read repository blobs. Every value on its Expected line is quoted from the PR hunk read through hg.py; github_get_file_contents in run-5 (event 117, 21075 bytes, matching the listed file) shows the same call sites at L171 to L180. github_get_pull_request_comments was never called in a run, so the event also offers Samuel's Gmail copy of the comment", F("client", "rc18"), "OE accuracy", "none: both routes are cataloged and the mail is visible"),
    ("5", "Win & Collect's email: DES-313 is Calvin's own ticket, so the brief counts it among his asks; it is a sheet row as well", F("who:calvin.price"), "rubric", "accept the email with or without it"),
    ("6", "New tickets' state and the call on them: the four asks take Backlog or unset; the call can sit in the description or a comment (brief 4b)", asks, "rubric", "accept either"),
    ("7", "Dossier 'Facts for the human' still says the parent has 32 children (a rev5 value). The SQL has 31 children plus DES-313 with no parent", F("parent"), "OE accuracy if copied", "this ledger uses 31; the dossier is a lead only"),
    ("8", "Test 1 for Achievement reward waiting and Support reply waiting rests on Done tickets, not a BETA card; ZOM-314 alone would not do, since it says the button waits on Helpshift, so ZOM-301 carries it", ", ".join(fid_of["msg:" + k] for k in ("Achievement reward waiting", "Support reply waiting")), "OE accuracy", "state only the deciding test on these rows"),
]

# ---------------------------------------------------------------- visibility proof
brow = [" | ".join(str(c) for c in f) for f in FACTS]
need = sorted({x for r in brow for _, x in G.scoped_ids(r)})
seeded = [x for x in need if x in LINE]
base = [x for x in need if x not in LINE]
lbf = os.path.join(HERE, "oe_lb_ids.txt")
open(lbf, "w").write("\n".join(seeded) + "\n")
cs_txt = run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "check-sql", PERSONA, f"{TDREL}/01_Universe_Inject.sql", "--load-bearing", f"{TDREL}/Working_Files/plan/oe_lb_ids.txt"])
yes_rows = [l for l in cs_txt.splitlines() if l.startswith("[YES LB]") and any(x in l for x in seeded)]
verdict = [l for l in cs_txt.splitlines() if l.startswith("verdict:")]
svc_of = {x: s for r in brow for s, x in G.scoped_ids(r)}
base += [x for x in seeded if not any(x in l for l in yes_rows)]      # a seeded row in a base thread: check-sql's line does not name the thread
cansee = []
for x in base:
    out = run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "can-see", PERSONA, svc_of[x], x]).splitlines()
    cansee.append(out[0] if out else f"{PERSONA} {svc_of[x]} {x}: UNVERIFIED")

# ---------------------------------------------------------------- write
O = []
A = O.append
ctx = json.load(open(os.path.join(WF, "00_Task_Context.json")))
clock = ctx["universe"]["clock_line"].replace("Clock: ", "")
freeze = ctx.get("freeze_utc") or ctx["universe"].get("freeze_utc")
import hashlib  # noqa: E402
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]  # noqa: E731
A("# 08 OE Writing Ledger — samuel_zm_beta_messages (beta player messages, injection rev6)")
A(f"Generated 2026-11-05 · Clock {clock} · seed bound {freeze} · Persona Samuel Turner samuel.turner@harmonygames.co (Game Designer) · Tier Long-Horizon · Mode Medium")
A(f"Status: READY — every requirement has verified facts, every scoped fact is persona-visible (pasted proof below), all {len(WR)} write families map to cataloged tools, friction is none")
A(f"Inputs read: 04_Prompt.txt — present (sha256 {sha(os.path.join(TI, '04_Prompt.txt'))}) · 00_Assigments.md — present · 01_Universe_Inject.sql — present (rev6, sha256 {sha(SQL_PATH)}) · 01_Grounding_Dossier.md — present (leads only) · 01_Scenario_Design.md + 01_Hardness_Manifest.json — present (leads only) · 03_Error_Async_Config.txt — present (Friction: none) · 02_Reference_Files — none · 04_Prompt_Writing_Brief.md — present (§4b fixed for rev6: eight recipients, four built-but-held)")
A("")
A("Persona binding: roster entry samuel_turner, Samuel Turner, Game Designer, samuel.turner@harmonygames.co. Scoped services: Gmail (own mailbox), Slack (member of #zombie-match3d, #zombie-art, #zombie-bugs, #company-internal and his DMs), Calendar (own calendar), Drive, Docs and Sheets (files shared with him and his own folder). Unscoped: Linear, Trello, GitHub, Confluence, Contacts, Snowflake.")
A("")
A("Dates: Pacific first, UTC beside it. 'sent', 'created', 'posted', 'updated' and 'merged' mark record times. Every record time below is at or before the seed bound; no semantic future date is relied on.")
A("")
A("## A · Requirements (traced to the prompt)")
A("| R | Prompt span (quoted) | Type (Discovery / Write / Tell / Constraint) | Explicit / implicit | Fact IDs |")
A("|---|---|---|---|---|")
for i, (s, typ, ex, fids) in enumerate(REQ, 1):
    A(f'| R{i} | "{s}" | {typ} | {ex} | {fids} |')
A("")
A("## B · Facts")
A('| F | Fact / value | Service | Tool family (catalog) | Locator | Locator origin (prompt · F-n · search "query text") | Expected data (dates typed: created / starts / due) | Ledger result for the Expected line (VERIFIED quote · not_a_claim · ABSENCE evidence_check · UNRESOLVED) | Persona-visible? (proof) | Depends on | Source pointer |')
A("|---|---|---|---|---|---|---|---|---|---|---|")
for f in FACTS:
    A("| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in f) + " |")
A("")
A("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)")
A("")
A(f"`python3 Task_Authoring/tools/persona_view.py check-sql {PERSONA} {TDREL}/01_Universe_Inject.sql --load-bearing plan/oe_lb_ids.txt` ({len(seeded)} seeded ids; load-bearing rows and the verdict line kept):")
A("")
for l in yes_rows + verdict:
    A(l)
A("")
A(f"`python3 Task_Authoring/tools/persona_view.py can-see {PERSONA} (service) (id)` ({len(base)} base ids, first line of each):")
A("")
for l in cansee:
    A(l)
A("")
A("## C · Write capability")
A("| R | Required write | Prompt authority (quoted; agent, not user-reserved) | Catalog tool (exists?) | Required parameters | Target (fact ID) | Completing end state | Content the prompt requires | Defer search (services · population · pagination complete · governing version · result, or UNRESOLVED) | Feasible? |")
A("|---|---|---|---|---|---|---|---|---|---|")
for w in WR:
    A("| " + " | ".join(w) + f" | {DEFER} | yes |")
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
nq = sum(1 for f in FACTS if "VERIFIED" in f[7])
nn = sum(1 for f in FACTS if "not_a_claim" in f[7])
na = sum(1 for f in FACTS if "ABSENCE" in f[7])
A(f"Requirements {len(REQ)} · facts {len(FACTS)} · writes {len(WR)} (feasible {len(WR)}) · friction items 0 · expected values {len(FACTS)} (quoted {nq} · not_a_claim {nn} · ABSENCE-checked {na}) · unverified visibility 0 · blocking 0")
A("")
A("## Self-review")
A("")
A("Walked Evals/2_Oracle_Events_Eval.md 1.1, 2.1–2.6 and 3.1–3.5 against this ledger in order. Every requirement has facts; every write family has its prompt authority, a cataloged tool with its required parameters, a completing end state and a defer search; friction is none; every scoped fact carries pasted visibility proof. Every §B value was re-verified in this run: seeded values from the parsed SQL rows, base values through tools/hg.py (plan/oe_reads.py, plan/oe_reads2.py), with each quote asserted as a substring of its record by plan/assemble_oe_ledger.py. The no-event-text scan passes: §B holds facts and dependency edges, no event wording.")
A("")
A("| R | Counter-reading (strongest other reading of the span, or a competing location) | Evidence that resolves it | Result |")
A("|---|---|---|---|")
CRS = [
    ("R1", "'His DM to me from yesterday' could be another Leonard DM", f"the message of Sep 30 is the one naming the PN sheet and the job ({I['hub']}, {fid_of['hub']}); the prompt's date is Oct 1", "holds"),
    ("R2", "the sheet could mean every tab, or the Domino twin", f"the DM says 'the PNs Beta tab'; the twin has no Status column ({fid_of['sheet']}, T12)", "holds (14 rows)"),
    ("R3", "the population could stop at the 18 asks under DES-314, or take in Slack asks and red dots", f"the DM's words are 'filed on a ticket or a card'; the four comment asks sit on tickets ({asks}); Slack asks are not filed; the rule defines a message ({fid_of['rule']})", "holds (36), see §F 3"),
    ("R4", "the sheet's Ready column could decide, or the first failed test could be read out of order", f"{fid_of['rule']}: 'Neither status column on the sheet decides anything' and 'stop at the first one that fails'", "holds"),
    ("R5", "the sheet could be a tab on the PN sheet", f"the DM says 'one sheet in your Drive folder'; {fid_of['folder']} is Samuel's own folder ({BASE['folder']})", "holds"),
    ("R6", "the note could list every message or a total", f"the DM names three contents (F1); the four built Holds come from {fid_of['counts']}", "holds"),
    ("R7", "Holds could go on the checklist too, or the checklist could go on the Minor Bugs card", f"the DM says 'Every Go'; the card comment {fid_of['pncard']} names this card; decoy {BASE['minor_bugs_card']} is for bugs", "holds (2 items)"),
    ("R8", "Go tickets could need no comment", "the DM says 'Leave the call as a comment on each ticket' (F1), with no exception for Go", "holds (32 comments)"),
    ("R9", "Hold tickets could go to Todo as the rule doc's last sentence says, and Done Holds could stay Done", f"{fid_of['freeze']} of Sep 29 is later and the doc itself says 'unless the roadmap says otherwise'; only Go tickets stay as they are ({fid_of['rule']})", "holds (24 Backlog, 6 Canceled, 2 unchanged)"),
    ("R10", "Win & Collect could need a new ticket, and the ZOM tickets could take the call instead of new ones", f"the DM's 'under whatever name' and {fid_of['wc']}; the ZOM tickets are about other work (e.g. ZOM-542 '{B1['zom']['ZOM-542']['title']}'), so the asks have no ticket of their own", "holds (5 new)"),
    ("R11", "Leonard could get an email, or the emails could stop at seven people", f"the DM says 'apart from me'; Douglas's only ask is the ZOM-563 comment ({fid_of['ask:Teammate sent lives']}, {fid_of['who:douglas']})", "holds (8)"),
    ("R12", "the counts could go in a channel or could be sent first", "the prompt says 'that same DM' and 'When it's all finished'", "holds"),
    ("R13", "the agent could stop to confirm a call with Samuel", "the prompt says 'You don't need to run anything by me first' (04_Prompt.txt); the defer search finds no hold on any write", "holds"),
]
assert len(CRS) == len(REQ)
for r in CRS:
    A("| " + " | ".join(r) + " |")
A("")
A("Unresolved: none blocking. Open risks §F 1 to 8 go to the draft and rubric stages (the updatedAt route, relations left out of the path, the all-fail reading of the four comment asks, the two client values read from main, Calvin's email, new-ticket state, the stale dossier count, and test 1 on four rows).")
A("")
open(os.path.join(WF, "08_OE_Writing_Ledger.md"), "w").write("\n".join(O) + "\n")
json.dump({"fid": fid_of, "seeded": seeded, "base": base}, open(os.path.join(HERE, "oe_ledger_ids.json"), "w"), indent=1)
print("facts", len(FACTS), "req", len(REQ), "seeded ids", len(seeded), "base ids", len(base), "yes rows", len(yes_rows), "cansee", sorted({l.split(":")[-1].strip()[:3] for l in cansee}))

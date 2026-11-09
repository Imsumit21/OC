#!/usr/bin/env python3
"""Draft 08_Oracle_Events.md (draft mode) from the OE ledger's facts.

Every quoted Expected value is re-read in this run: seeded rows are parsed from 01_Universe_Inject.sql (never executed), base
records come from plan/oe_base*.json, written by plan/oe_reads*.py through tools/hg.py just before this script. Each quote is
asserted as a substring of its own record (whitespace-normalised) before the file is written. One write per event; no
final-response or non-action events."""
import datetime as dt
import json
import os
import re
import sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402

PT = ZoneInfo("America/Los_Angeles")
SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
ST = [x for x in parse_sql(SQL) if x["op"] == "insert"]
P = json.load(open(os.path.join(HERE, "ids.json")))
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
B1 = json.load(open(os.path.join(HERE, "oe_base.json")))
B2 = json.load(open(os.path.join(HERE, "oe_base2.json")))
B3 = json.load(open(os.path.join(HERE, "oe_base3.json")))
TR = json.load(open(os.path.join(HERE, "oe_trello.json")))
I, BASE = P["ids"], P["base"]
CHECKS = []


def rows(table, **kw):
    return [x["row"] for x in ST if x["table"] == table and all(x["row"].get(k) == v for k, v in kw.items())]


def clean(s):
    return (s or "").replace("\\r", "").replace("\\n", "\n").replace("\r", "")


def norm(s):
    return re.sub(r"\s+", " ", clean(s)).strip()


def q(rec, *quotes):
    """Assert each quote against its own record, return them in double quotes."""
    out = []
    for s in quotes:
        assert norm(s) in norm(rec), (s, norm(rec)[:160])
        CHECKS.append(s)
        out.append(f'"{s}"')
    return " ".join(out)


def pt(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(PT)
    return d.strftime("%a %b %-d %Y %-I:%M %p") + " PT"


def tsiso(ts):
    return dt.datetime.fromtimestamp(float(ts), dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


S_ = {r["ts"]: r for r in rows("slack.slack_messages")}
sl = lambda ref: S_[ref.split("/")[1]]  # noqa: E731
EV, N = [], {}


def ev(key, action, expected):
    EV.append((action, expected))
    N[key] = len(EV)


def o(*keys):
    return "OE " + ", ".join(str(N[k]) for k in keys) if len(keys) == 1 else "OEs " + ", ".join(str(N[k]) for k in keys)


ISS = {r["id"]: r for r in rows("linear.linear_issues")}
USERS = {k: (v or {}).get("email") for k, v in B2["users"].items()}
NAME = {"brian.foster@harmonygames.co": "Brian Foster", "calvin.price@harmonygames.co": "Calvin Price", "douglas@harmonygames.co": "Douglas", "julia.lawson@harmonygames.co": "Julia Lawson",
        "martin.walsh@harmonygames.co": "Martin Walsh", "oliver.brooks@harmonygames.co": "Oliver Brooks", "owen.baker@harmonygames.co": "Owen Baker", "robert@harmonygames.co": "Robert",
        "leonard.hayes@harmonygames.co": "Leonard Hayes", "arthur.blake@harmonygames.co": "Arthur Blake", "vincent.parker@harmonygames.co": "Vincent Parker", "samuel.turner@harmonygames.co": "Samuel Turner"}
M = {m["key"]: m for m in P["members"]}
ORDER = [m["key"] for m in P["members"]]

# ---------------------------------------------------------------- reads: the job and the rule
hub = sl(I["hub"])
ev("hub", "Read Leonard's DM from yesterday in Slack (Samuel's DM with Leonard Hayes, his message of Tue Sep 30 2025)",
   f"Leonard, {pt(tsiso(hub['ts']))}: " + q(hub["text"],
      "The PN sheet says six are Ready and I don't trust that.",
      "Take every row on the PNs Beta tab plus every ask for a new phone message that's been filed on a ticket or a card up to today, and make a call on each one using the message rule doc.",
      "Put it in one sheet in your Drive folder, one row per message: Message, Ticket, Call, What's missing, Audience, Final headline, String change.",
      "Next to it a one-page note for the team: start with D1 and D7 for the Sep 15 cohort week from the warehouse, iOS and Android separately, then the lapsed reminders the client schedules day by day, and anything the client already schedules that's still a Hold and why.",
      "I made tickets for the sheet rows under DES-314 and people added their asks there.",
      "Leave the call as a comment on each ticket and move the ticket to match.",
      "Anything with no ticket gets one, but don't make a second one for something that already has a ticket under whatever name.",
      "Every Go goes on a checklist on our push notifications card so Vincent can tick it off.",
      "Email each person who asked for something, apart from me, to say what happened to their asks.",
      "When it's done tell me here how many Go, Hold and Drop."))

rule = rows("gdocs.docs_documents")[0]
rt = rule["body_text"]
ev("rule", 'Read the message rule doc in Drive/Docs (search "rule"; doc "Beta message rule")',
   f"Leonard's doc, last changed {pt(rule['modified_time'])}. " + q(rt,
      "A message is anything the game puts on a player's phone while the game is closed.", "Run these tests in order and stop at the first one that fails.",
      "1. The feature behind it is in the beta.", "2. The client can send it without a server.", "3. The client already schedules it.",
      "4. It can reach the players it is written for. A player only counts once our own permission ask has happened, the settings toggle doesn't count. It fails only if none of them count.",
      "5. It fires on the right day. The hour doesn't matter for beta, the day does.", "6. Vincent has seen it arrive on both iOS and Android.",
      "Go: it passes all six. Drop: it fails test 1, or the client already covers it under another message, then name that message. Hold: anything else, and name the test it failed.",
      "In the beta means live in Zombie Match today or on the BETA list of the ZM ROADMAP board.", "Neither status column on the sheet decides anything.",
      "What Vincent counts as seen is in his QA note. The permission ask is Robert's call.", "The final headline is the latest line I've called.",
      "A line that differs from what the client ships needs a string ticket under DES-314, because the strings are hard-coded, so open one when you make the call.",
      "Emoji don't count as a different line. Final headline and String change are only for Go rows. Audience is who the ask says it's for.",
      "Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise."))

grid = B1["pn_grid"]
row_of = {int(m["source"].rsplit(" ", 1)[1]): m["key"] for m in P["members"] if m["source"].startswith("PNs Beta")}
assert len(row_of) == 14
ev("sheet", 'Read the PNs Beta tab of the Zombie Match PN sheet in Sheets (search "Push Notifications"; sheet "Push Notifications Zombie Match", tab "PNs Beta", second tab)',
   f"Last changed {pt(B1['pn_meta']['modified_time'])}. 14 rows, shown here as row, Details, Status, Headline: " + "; ".join(f'{i} "{grid[i][5].strip()}", {grid[i][1].strip()}, "{grid[i][9].strip()}"' for i in range(1, 15))
   + f'. Six say Ready. Row 6 Segmentation: "{grid[6][6].strip()}".')

kids = sorted([r for r in rows("linear.linear_issues") if r.get("parent_id") == "DES-314"], key=lambda r: r["number"] if isinstance(r.get("number"), int) else int(r["id"].split("-")[1]))
assert len(kids) == 31
sheet_k = [r for r in kids if r["title"].startswith("PN: ")]
ask_k = [r for r in kids if r["title"].startswith("PN ask: ")]
assert len(sheet_k) == 13 and len(ask_k) == 18
done = [r["id"] for r in kids if r["state_id"] == "Done"]
assert done == ["DES-315", "DES-316", "DES-317", "DES-318", "DES-319", "DES-320"]
assert all(r["state_id"] == "In Review" for r in kids if r["id"] not in done)
ev("kids", "List the children of DES-314 in Linear (parent DES-314, from OE 1)",
   "31 tickets. 13 for sheet rows: " + "; ".join(f"{r['id']} {r['title'][4:]}" for r in sheet_k) + ". 18 asks, with who filed each: " + "; ".join(f"{r['id']} {r['title'][8:]} ({NAME[USERS[r['creator_id']]]})" for r in ask_k)
   + f". States: {', '.join(done)} Done; the rest In Review. Descriptions: DES-315 to DES-320 each end " + q(ISS["DES-315"]["description"], "Built in match3d #248.") + "; DES-321 " + q(ISS["DES-321"]["description"], "Quests are already in production.") + "; DES-322 " + q(ISS["DES-322"]["description"], "Daily login is already in the game.") + "; DES-339 " + q(ISS["DES-339"]["description"], "We already give free coins in the shop.") + ".")
for _k in ("DES-315", "DES-316", "DES-317", "DES-318", "DES-319", "DES-320"):
    assert "Built in match3d #248." in ISS[_k]["description"]


def cmts(tk):
    return sorted(rows("linear.linear_comments", issue_id=tk), key=lambda r: r["created_at"])


ev("cmts", f"Read the comments on each of those 31 tickets in Linear (one call per ticket, list from {'OE ' + str(N['kids'])})",
   "Who it's for, then Arthur's note where there is one. " + " ".join(f"{r['id']}: " + " ".join(f'"{clean(c["body"])}"' for c in cmts(r["id"])) + "." for r in kids)
   + f" On DES-319 and DES-345 the last comment is Leonard's. On DES-315 to DES-320 the second comment is Vincent's, from Wed Sep 24 2025.")

body = B1["liveops"]["body"]
ev("liveops", 'Find the live-ops page in Confluence (search "Live-Ops"; page "Live-Ops Event Calendar & Planning")',
   "Among the event rows, game then status: Plague Race, Zombie Match 3D, " + q(body, "Live; algo bug Aug 2025") + ". Zombie Lane, Zombie Match 3D, Live. Endless Monster Mode, Zombie Match 3D, " + q(body, "Live; also one of the three permanent board modes")
   + ". Weekly Leaderboards, Domino Delights / Zombie Match 3D, Live. Nathan's Treasure Hunt, Axe Arena and Streak Fever are on Domino Delights. Collect & Win, Zombie Match 3D: " + q(body, "Built for the end-of-September beta submission (QA blockers cleared 26 Sep 2025); not yet live.") + " It is the same feature as Win & Collect, " + q(body, "under a different name") + ".")

wc = ISS["DES-313"]
ev("wc", 'Find the Collect & Win ticket in Linear (query "Collect")',
   f"DES-313 \"{wc['title']}\", filed by Calvin Price, created {pt(wc['created_at'])}, state {wc['state_id']}, no parent. " + q(wc["description"], "Three windows a week.") + f" This is the ticket for the Win & Collect row ({'OE ' + str(N['liveops'])}).")
ev("wcc", f"Read the comments on DES-313 in Linear (ticket from OE {N['wc']})", " ".join(f'"{clean(c["body"])}"' for c in cmts("DES-313")))

popids = sorted({r["id"] for r in B2["pop_base"]} | {"ZOM-483", "ZOM-542", "ZOM-556"}, key=lambda x: int(x.split("-")[1]))
assert len(popids) == 20
ev("pop", "List the Linear tickets updated since the day DES-314 opened, to find asks filed outside its children (updatedAt 2025-09-23, limit 100, or orderBy updatedAt on team Zombie Match 3D)",
   f"Besides DES-313, DES-314 and its 31 children, 20 tickets, all Zombie Match 3D: {', '.join(popids)}.")

ASKS = [("Boss Arena attempts refilled", "ZOM-542", I["boss_ask"]), ("Daily gift about to reset", "ZOM-556", I["gift_ask"]), ("Teammate sent lives", "ZOM-563", I["team_ask"]), ("Infinite lives ending", "ZOM-483", I["inf_ask"])]
for key, z, cid in ASKS:
    c = rows("linear.linear_comments", id=cid)[0]
    ev("ask:" + key, f"Read the comments on {z} in Linear (list from OE {N['pop']})",
       f"Ticket \"{B1['zom'][z]['title']}\". {NAME[USERS[c['author_id']]]}, {pt(c['created_at'])}: \"{clean(c['body'])}\" An ask for a new phone message with no ticket of its own; call it {key}.")
ev("rest", f"Read the comments on the other 16 tickets from OE {N['pop']} in Linear (one call per ticket)", "Each returns an empty comment list.")
seeded_hit = [r["id"] for r in rows("linear.linear_issues") if "notification" in (str(r.get("title")) + str(r.get("description"))).lower()]
assert not seeded_hit, seeded_hit
ev("census", 'Search Linear for any other ticket about phone messages (queries "notification", "push", "remind")',
   f"\"notification\" hits in Zombie Match 3D, all permission, settings, red dot or analytics work: ZOM-314 \"{B3['ZOM-314']['title']}\", ZOM-320 \"Notification pop up on android breaks the level 1 tutorial highlight.\", ZOM-366 \"{B2['like']['ZOM-366']['title']}\", ZOM-385 \"Zombie Lane Polish\", ZOM-387 \"Giant Analytics Ticket\". In Design: DES-9, a Backlog idea from 2023, and DES-283 \"Implement Chapter Full Star Rewards\". The other \"notification\" hits are older ENG and ART tickets. Besides those and the tickets from OEs {N['kids']} and {N['wc']}, the \"push\" and \"remind\" hits are about other things, among them ZOM-295 \"Refill health and push monster back should reset ALL enrage status.\" None asks for a new phone message for beta.")

# ---------------------------------------------------------------- reads: roadmap
fr = rows("trello.trello_actions", id=I["freeze_comment"])[0]
frd = json.loads(fr["data_json"] if "data_json" in fr else fr["data"])
pcom = rows("trello.trello_actions", id="68d415a716abcb84070a8e2a")[0]
pcd = json.loads(pcom["data_json"] if "data_json" in pcom else pcom["data"])
LIST = {k: v["name"] for k, v in TR["lists"].items()}


def on(prefix, lst):
    m = [c for c in TR["cards"] if c["name"].startswith(prefix)]
    assert m and LIST[m[0]["idList"]] == lst and not m[0].get("closed"), prefix
    return re.split(r" - | \(\[| \(l", m[0]["name"])[0].strip()


ev("roadmap", "List the ZM ROADMAP board's lists and their cards in Trello",
   'Lists include "BETA: Oct 10", "Oct 21" and "Backlog". On BETA: Oct 10, among others: ' + ", ".join('"' + on(p, "BETA: Oct 10") + '"' for p in ("Win and Collect", "Season Pass", "Infinite HP Boss Mode", "300 Levels Manmade", "Add more quests", "Shop Inventory Review", "Fix TECH ISSUES"))
   + f'. On Oct 21, among others: "{on("Axe Arena", "Oct 21")}". On Backlog, among others: "{on("Hourly Collection", "Backlog")}".')
ev("feat", 'Tie Boss Arena to the BETA list in Linear (query "Boss Arena")', f"ZOM-487 \"{B3['boss_title']}\", {B3['boss_state_id']}: this is the BETA list's Infinite HP Boss Mode.")
ev("feat2", 'Check that achievements and support have shipped in Linear (queries "Achievements" and "Helpshift")',
   f"ZOM-116 \"{B3['ZOM-116']['title']}\", {B3['ZOM-116']['state']}. ZOM-363 \"{B3['ZOM-363']['title']}\", {B3['ZOM-363']['state']}. ZOM-301 \"{B3['ZOM-301']['title']}\", {B3['ZOM-301']['state']}.")
ev("freeze", 'Read the card "Fix TECH ISSUES" on the BETA list in Trello (its description and last activity, from the board\'s lists)', "Description: " + q(frd["card"]["desc"], "Until the beta build is out nothing that isn't beta work lands in anyone's Todo. Held tickets sit in Backlog, unassigned.")
   + f" Last activity {pt(fr['date'])}. This is later than the rule doc ({'OE ' + str(N['rule'])}), whose Todo clause gives way to what the roadmap says.")
ev("tcom", "Read the card comments on ZM ROADMAP in Trello (board actions, filter commentCard)", "13 comments: estimates and art notes from June and July, Leonard's note on the push notifications card, and \"Samuel says 3 days.\". None is an ask for a phone message.")
ev("tcard", 'Search Trello for cards about phone messages (searches "notification" and "reminder", cards_filter all)',
   'On ZM ROADMAP the one hit is "[Feature] Push Notifications - Samuel + Leonard". The other six are on the boards "DD Product Roadmap" and "Harmony Games", last active by May 2025: "Expand notifications", "local Push Notification", "Appointment Mechanic v1 Basic", "Make mini-games accessible via saga map nodes", "Push-notification boost", "(Blake/Samuel) Hooking up Notifications to One Signal (1 week)". The search for "reminder" returns no cards. None asks for a new phone message for beta.')
ev("pncard", 'Find the push notifications card on ZM ROADMAP in Trello (search "Push Notifications")',
   f"Card \"{B3['pn_name']}\", id {BASE['pn_card']}, on the Jun 30th list. Leonard's comment, {pt(pcom['date'])}: " + q(pcd["text"], "The beta list goes on this card as a checklist. Vincent ticks these as he checks them on the store builds."))

# ---------------------------------------------------------------- reads: client
hunk = B1["hunk"]["diff_hunk"]


ev("client", "Read the client's notification code in GitHub (repo match3d, main, path Assets/Scripts/Notifications/NotificationManager.cs)",
   "The scheduling method makes six calls, for lives recharged, the first tutorial, the one-day reminder, the weekly batch, the weekly leaderboard batch and Plague Race. " + q(hunk,
      "DailyNotifications(OneDayLapsedTitle, OneDayLapsedMessage, serverToday);", "BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);",
      "BatchScheduleWeeklyLeaderboardNotifications(WeeklyLeaderboardTitle, WeeklyLeaderboardMessage, 4, serverToday);", "BatchSchedulePlagueRace(PlagueRaceTitle, PlagueRaceMessage, 5, serverToday);",
      "DateTime date = serverToday.AddDays(1);", "DateTime fireTime = referenceDate.AddDays(i * 7);")
   + ' So the lapsed reminders go on day 1, then days 7, 14, 21 and 28 after the last session, and the weekly leaderboard one counts the same way. Titles include ' + q(hunk, "The Horde Is Growing… 🧟‍♂️", "They’ve Taken Over… Can You Stop Them? 😱", "Full Ammo Reloaded! 🔫", "Plague Race Is On! 🌊🚣") + ".")
rc = rows("github.github_review_comments")[0]
assert "BatchScheduleWeeklyLeaderboardNotifications(string title" in rc["diff_hunk"].replace("\\n", "\n")[-420:]
ev("rc18", f"Read the review comments on PR #248 in GitHub (repo match3d, PR number from OE {N['kids']}), or the same comment in Samuel's Gmail (search \"PR #248\")",
   f"Arthur Blake, {pt(rc['created_at'])}: " + q(rc["body"], "This counts seven days from the day they last left the game, so it isn't tied to the rollover. Fine to merge, but it isn't a reset message until it's anchored to the real reset.") + " On GitHub the comment sits on the fireTime line of BatchScheduleWeeklyLeaderboardNotifications.")

# ---------------------------------------------------------------- reads: what Vincent has seen
qa = rows("gmail.gmail_messages", id="samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>")[0]
ev("qa", 'Read Vincent\'s QA note in Gmail (search "Phone messages for beta")',
   f"Vincent Parker, {pt(qa['date'])}: " + q(qa["body_text"], "Seen only counts on a store build, on a real iOS device and a real Android device.", "A build with shortened timers doesn't count, it only proves the code path.", "Moving the phone date forward on a store build is fine.", "Passes go in the Phone message checks sheet."))
glog = json.loads(rows("gsheets.sheets_sheets")[0]["grid_json"])
ev("log", 'Read Vincent\'s checks log in Sheets (search "Phone message checks"; tab "Beta")',
   "Six rows, each with Android 0.3.127, iOS 0.3.40, Checked Sep 24: " + "; ".join(r[0] + (f' ("{r[4]}")' if r[4] else "") for r in glog[1:]) + ".")
lp = sl(I["lives_pull"])
ev("vid", 'Find Vincent Parker\'s Slack user (search users "Vincent")', "Vincent Parker, user id EMPLOYEE_0012_SLACK_ID.")
ev("pull", f"Search Slack for what Vincent Parker has posted since Sep 1 (query from the user id in OE {N['vid']}) for his Sep 30 post in #zombie-match3d",
   f"{pt(tsiso(lp['ts']))}: \"{clean(lp['text'])}\" Full Ammo Reloaded! is the Lives recharged headline, so his tick on Lives recharged is off. It is later than the Sep 24 pass.")
qr = sl(I["qa_reply"])
ev("qareply", f"Read Vincent's Sep 29 reply in Samuel's DM with him in Slack (in the results of OE {N['pull']})",
   f"{pt(tsiso(qr['ts']))}: \"{clean(qr['text'])}\" The race one is Plague Race, so its iOS pass is withdrawn. It is later than the Sep 24 pass.")

# ---------------------------------------------------------------- reads: the permission ask
ask, arep = sl(I["ask_decision"]), sl(I["ask_reply"])
ev("ask", 'Search Slack for Robert\'s permission ask call (search "permission ask")',
   f"Robert in #zombie-match3d, {pt(tsiso(ask['ts']))}: \"{clean(ask['text'])}\"")
ev("askreply", f"Read the replies under Robert's post in Slack (thread from OE {N['ask']})", f"Arthur Blake, {pt(tsiso(arep['ts']))}: \"{clean(arep['text'])}\"")

# ---------------------------------------------------------------- reads: the headline
lv2 = sl(I["corr_reply"])
ev("line2", 'Search Slack for Leonard\'s change to the seven-day line (search "taken over")',
   f"Leonard in #zombie-art, {pt(tsiso(lv2['ts']))}: \"{clean(lv2['text'])}\"")
evt = rows("gcal.gcal_events", event_id=I["copy_check"])[0]
ev("line3", 'Search Samuel\'s Google Calendar for the lapsed copy check (search "Lapsed"; event "Lapsed copy check")',
   f"Event by Leonard, created {pt(evt['created'])}, updated {pt(evt['updated'])}. Description: " + q(evt["description"], "Went through the lapsed lines with Martin Walsh after this. Final for the 7 day one is \"Your Squad Is Waiting\", body stays. That replaces what I said in the art thread."))
cancel = rows("gmail.gmail_messages", id="samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com>")[0]
ev("covered", 'Read the cancelled ladder review in Gmail (search "lapsed"; subject "Canceled event with note: Lapsed ladder review")',
   f"Leonard, {pt(cancel['date'])}: " + q(cancel["body_text"], "Cancelled, no need. The weekly one repeats for four weeks, so day 14 is already covered."))
axe = B1["slack"]["axe"]
ev("axe", 'Search Slack for the Axe Arena decision (search "Axe Arena"; #company-internal)', f"Brian Foster, {pt(tsiso(axe['rec']['ts']))}: " + q(axe["rec"]["text"], "We’ve decided to postpone Axe Arena for the beta release."))

# ---------------------------------------------------------------- reads: numbers and destinations
wh = {}
for line in open(os.path.join(HERE, "oe_wh_rows.txt")):
    m = re.match(r'(\d+)\s+"text": "(.*)",?\s*$', line)
    wh[int(m.group(1))] = json.loads(json.loads('"' + m.group(2) + '"'))
a, i_ = wh[236], wh[237]
assert (a["platform"], i_["platform"], a["cohort_week"], i_["cohort_week"]) == ("android", "ios", "2025-09-15", "2025-09-15")
ev("whd", "Read the retention table's columns in Snowflake (describe ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION)", 'Column d1_ret: "% returning on Day 1". Column d7_ret: "NULL until the 7-day window closes".')
ev("wh", "Query D1 and D7 for the Sep 15 cohort week in Snowflake (ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION, game_id zombie_match_3d, cohort_week 2025-09-15)",
   f"Two rows. ios: installs {i_['installs']}, d1_ret {i_['d1_ret']}, d7_ret {i_['d7_ret']}. android: installs {a['installs']}, d1_ret {a['d1_ret']}, d7_ret {a['d7_ret']}.")
ev("folder", "Find Samuel's Drive folder in Drive (list the root)", f"Folder \"{B1['folder']['name']}\", id {BASE['folder']}, owner {B1['folder']['owner_email']}.")
ADDR = ["brian.foster", "calvin.price", "douglas", "julia.lawson", "martin.walsh", "oliver.brooks", "owen.baker", "robert"]
for w in ADDR:
    assert B1["contacts"][w]["email"] == f"{w}@harmonygames.co"
ev("addr", f"Look up each asker in Contacts (names from OEs {N['kids']}, {N['wc']}, {', '.join(str(N['ask:' + a[0]]) for a in ASKS)})", "; ".join(f"{NAME[w + '@harmonygames.co']}: {w}@harmonygames.co" for w in ADDR) + ".")

# ---------------------------------------------------------------- the calls
call = {k: TRUTH[k]["Call"] for k in ORDER}
miss = {k: TRUTH[k]["What's missing"] for k in ORDER}
tkt = {k: M[k]["ticket"] for k in ORDER}
t2 = [k for k in ORDER if miss[k] == "needs a server send"]
t3 = [k for k in ORDER if miss[k] == "not scheduled in the client"]
assert len(t2) == 6 and len(t3) == 18


def named(ks):
    return "; ".join(f"{k} ({tkt[k]})" if tkt[k] and tkt[k] != "None" else k for k in ks)


ev("c1", f"Apply test 1 to all 36 messages: 14 sheet rows, 18 asks under DES-314 and 4 comment asks (the Docs rule from OE {N['rule']}, with Linear in OEs {N['kids']}, {N['cmts']}, {N['ask:Daily gift about to reset']}, {N['ask:Teammate sent lives']}, {N['ask:Infinite lives ending']}, {N['feat']}, {N['feat2']}, Trello in OE {N['roadmap']}, Confluence in OE {N['liveops']}, GitHub in OE {N['client']}, Slack in OE {N['axe']})",
   f"Five fail, so Drop: Hourly Coins (Hourly Collection is on the Backlog list); Nathan's Treasure Hunt and Streak Fever (live-ops page: Domino Delights); Axe Arena (Oct 21 list, postponed for the beta); Comeback gift (Leonard on DES-345: \"A reward on tap is a version 2 idea, it isn't in the beta.\"). The other 31 pass. In the client: Lives recharged, Finish first mission, Lapsed 1 day, Lapsed 7 days. The same lapsed feature: Lapsed 3 days, Lapsed 14 days, Lapsed 30 days. Live on the live-ops page: Plague Race and its two asks, Zombie Lane, both Endless asks, Weekly Leaderboard reset. On the BETA list: Win & Collect, Season Pass and its two asks, the three Boss Arena messages, New levels added. Live by their ticket text: Quests rollover, Login Calendar update, Free shop coins ready. Shipped: Achievement reward waiting, Support reply waiting. Live by their own comments: Daily chest ready (Arthur: \"the chest timer is local\"), Daily gift about to reset (\"the gift streak itself is live\"), Teammate sent lives (\"prod has the latest teams changes now\"), Infinite lives ending (\"we do hand out infinite lives\").")
ev("c2", f"Apply test 2 to the 31 left (Arthur's Linear notes in OE {N['cmts']}, Douglas's Linear comment in OE {N['ask:Teammate sent lives']})",
   f"Six need a server send, so Hold, test 2: {named(t2)}.")
ev("c3", f"Apply test 3 to the 25 left (the six GitHub scheduling calls in OE {N['client']}, Arthur's Linear notes in OE {N['cmts']}, the Linear comment asks, and the Gmail note in OE {N['covered']})",
   f"The client schedules six: Lives recharged, Finish first mission, Lapsed 1 day, Lapsed 7 days, Weekly Leaderboard reset, Plague Race. Lapsed 14 days is covered by Lapsed 7 days, because the weekly batch fires on day 14, so Drop, naming Lapsed 7 days. The other 18 are not scheduled, so Hold, test 3: {named(t3)}.")
ev("c4", f"Apply test 4 to the six the client schedules (Slack in OEs {N['ask']} and {N['askreply']}, Linear in OE {N['cmts']}, Sheets in OE {N['sheet']})",
   "Finish first mission fails, so Hold, test 4: it is written for new players below level 20 (DES-318, and the sheet's \"Level 20 not completed\"), our own ask runs after level 20, and the settings toggle doesn't count, so none of its players count. The other five reach players who have had our ask.")
ev("c5", f"Apply test 5 to the five left (GitHub in OEs {N['client']} and {N['rc18']}, Linear in OE {N['cmts']})",
   "Weekly Leaderboard reset fails, so Hold, test 5: it counts from the last session, not the weekly reset, so it fires on the wrong day. Plague Race passes (Leonard on DES-319: \"Daily is fine for this one, there's always a race on.\"), and so do Lives recharged, Lapsed 1 day and Lapsed 7 days.")
ev("c6", f"Apply test 6 to the four left (Gmail in OE {N['qa']}, Sheets in OE {N['log']}, Slack in OEs {N['pull']} and {N['qareply']})",
   "Lives recharged and Plague Race fail, so Hold, test 6, not seen on both platforms. Lapsed 1 day and Lapsed 7 days pass: both were seen on store builds with the phone date moved forward, and Vincent says \"the lapsed ones are still coming through\".")
ev("c7", f"Settle the Go rows' headlines (GitHub in OE {N['client']}, Slack in OE {N['line2']}, Calendar in OE {N['line3']})",
   'Lapsed 1 day: Final headline "The Horde Is Growing…", String change No. Lapsed 7 days: Final headline "Your Squad Is Waiting" (the latest line, replacing "Your Squad Needs You Back"), String change Yes, because the client ships "They’ve Taken Over… Can You Stop Them? 😱".')
ev("c8", f"Count the calls across the Sheets rows and Linear tickets (OEs {N['c1']} to {N['c6']})", "36 messages: Go 2, Hold 28, Drop 6.")

# ---------------------------------------------------------------- writes
ev("w_str", "Create the string ticket in Linear (team Design, parent DES-314)", 'A new ticket under DES-314 carrying the line "Your Squad Is Waiting" for Lapsed 7 days.')
AUD = {k: TRUTH[k]["Audience"] for k in ORDER}
for key, z, cid in ASKS:
    ev("w_new:" + key, f"Create the ticket for {key} in Linear (team Design, parent DES-314, state Backlog, no assignee)", f"A new ticket for {key}, for {AUD[key]}, naming the ask on {z}.")
    tail = "test 2: it needs a server send" if miss[key] == "needs a server send" else "test 3: the client doesn't schedule it yet"
    ev("w_newc:" + key, f"Comment the call on the new {key} ticket in Linear", f"A comment saying Hold, {tail}.")
ev("w_sheet", "Create the calls sheet in Sheets", 'A new native spreadsheet with a name about the beta messages.')
ev("w_rows", f"Write the rows to the calls sheet in Sheets (calls from OEs {N['c1']} to {N['c7']})",
   'Header Message, Ticket, Call, What\'s missing, Audience, Final headline, String change, then 36 rows, one per message. Message uses the sheet\'s or the ticket\'s name, or an obvious short form. Ticket holds the row\'s ticket: DES-313 for Win & Collect start, the new keys for the four comment asks. What\'s missing names the failed test on Hold rows, names Lapsed 7 days on Lapsed 14 days, is blank or a short reason on the other Drop rows, and is blank on the Go rows. Audience comes from each ask (OEs '
   + f"{N['cmts']}, {N['wcc']}, {N['ask:Boss Arena attempts refilled']} to {N['ask:Infinite lives ending']}). Final headline and String change are filled on the two Go rows only.")
ev("w_mv1", f"Move the calls sheet into Samuel's Drive folder in Drive (folder from OE {N['folder']})", f"The sheet's parent is {BASE['folder']}.")
ev("w_note", "Create the one-page team note in Docs",
   f"A Doc that opens with D1 and D7 for the Sep 15 cohort week: iOS D1 {i_['d1_ret']}%, D7 {i_['d7_ret']}%; Android D1 {a['d1_ret']}%, D7 {a['d7_ret']}%. Then the lapsed reminders the client schedules by day: day 1, then days 7, 14, 21 and 28. Then the Holds the client already schedules and why: Lives recharged and Plague Race (not seen on both platforms), Finish first mission (can't reach its players), Weekly Leaderboard reset (fires on the wrong day).")
ev("w_mv2", f"Move the note into Samuel's Drive folder in Drive (folder from OE {N['folder']})", f"The Doc's parent is {BASE['folder']}.")
ev("w_chk", f"Create a checklist on the push notifications card in Trello (card from OE {N['pncard']})", f"A new checklist on card {BASE['pn_card']}.")
ev("w_i1", f"Add Lapsed 1 day to the checklist in Trello (OE {N['w_chk']})", 'A check item naming Lapsed 1 day.')
ev("w_i2", f"Add Lapsed 7 days to the checklist in Trello (OE {N['w_chk']})", 'A check item naming Lapsed 7 days.')

WHY = {"Lives recharged": "Hold, test 6: Vincent's tick is off after 0.3.49", "Plague Race": "Hold, test 6: the iOS pass was on the 5-minute timers build", "Weekly Leaderboard reset": "Hold, test 5: it fires on the wrong day",
       "Finish first mission": "Hold, test 4: it can't reach its players", "Lapsed 1 day": "Go", "Lapsed 7 days": 'Go, with the final headline "Your Squad Is Waiting" and the string ticket',
       "Lapsed 14 days": "Drop: Lapsed 7 days already covers it", "Comeback gift": "Drop, test 1: it isn't in the beta", "Hourly Coins": "Drop, test 1: it isn't in the beta", "Nathan's Treasure Hunt": "Drop, test 1: it isn't in the beta", "Streak Fever": "Drop, test 1: it isn't in the beta", "Axe Arena": "Drop, test 1: it isn't in the beta"}


def why(k):
    if k in WHY:
        return WHY[k]
    return "Hold, test 2: it needs a server send" if miss[k] == "needs a server send" else "Hold, test 3: the client doesn't schedule it yet"


TK_ORDER = sorted([k for k in ORDER if tkt[k] and tkt[k] != "None"], key=lambda k: int(tkt[k].split("-")[1]))
assert len(TK_ORDER) == 32
for k in TK_ORDER:
    ev("wc:" + k, f"Comment the call on {tkt[k]} in Linear", f"A comment on {tkt[k]} ({k}) saying {why(k)}.")
for k in TK_ORDER:
    if call[k] == "Drop":
        ev("wm:" + k, f"Move {tkt[k]} to Canceled in Linear", f"{tkt[k]} state Canceled.")
    elif call[k] == "Hold":
        ev("wm:" + k, f"Move {tkt[k]} to Backlog with no assignee in Linear (OE {N['freeze']})", f"{tkt[k]} state Backlog, assignee empty.")
ASKERS = {"brian.foster": ["Endless entries back", "Endless weekly result", "Season Pass premium nudge", "Comeback gift", "Boss Arena attempts refilled"], "calvin.price": ["Daily chest ready", "Infinite lives ending", "Win & Collect start"],
          "douglas": ["Teammate sent lives"], "julia.lawson": ["Plague Race last hour", "Plague Race result", "New levels added", "Daily gift about to reset"], "martin.walsh": ["Free shop coins ready"],
          "oliver.brooks": ["Season Pass last 48 hours"], "owen.baker": ["Zombie Lane reward ready", "Achievement reward waiting", "Support reply waiting"], "robert": ["Boss Arena open", "Boss Arena last hours", "Lapsed 14 days"]}
for w, ks in ASKERS.items():
    ev("wmail:" + w, f"Email {NAME[w + '@harmonygames.co']} in Gmail (address from OE {N['addr']})", f"A sent email to {w}@harmonygames.co saying what happened to their asks: " + "; ".join(f"{k}: {call[k]}" for k in ks) + ".")
ev("wdm", f"Post the counts in Leonard's DM in Slack (the DM from OE {N['hub']}, after every other write)", "A message in that DM saying Go 2, Hold 28, Drop 6.")

# ---------------------------------------------------------------- write
out = []
for n, (act, exp) in enumerate(EV, 1):
    out += [f"OE {n}  {act}", f"Expected: {exp}", ""]
text = "\n".join(out).rstrip() + "\n"
open(os.path.join(TI, "08_Oracle_Events.md"), "w").write(text)
json.dump({"events": len(EV), "chars": len(text), "quotes_asserted": len(CHECKS), "index": N}, open(os.path.join(HERE, "oe_events_index.json"), "w"), indent=0)
w = sum(1 for k in N if k.startswith("w"))
print("events", len(EV), "writes", w, "chars", len(text), "quotes asserted", len(CHECKS))

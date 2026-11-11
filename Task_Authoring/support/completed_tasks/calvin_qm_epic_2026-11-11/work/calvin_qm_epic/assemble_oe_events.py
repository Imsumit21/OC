#!/usr/bin/env python3
"""Draft task_inputs/08_Oracle_Events.md for calvin_qm_epic (rev3b SQL 479b8441f52e) from the ledger's sources: the SQL (parsed, never executed),
plan/oe_base.json (fresh hg.py reads), solver/truth.json and plan/reports.py. Every quote is asserted as a substring of its record."""
import datetime as dt, json, os, re, sys
from zoneinfo import ZoneInfo
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools")); sys.path.insert(0, HERE)
from base_check import parse_sql
import reports as RP
PT = ZoneInfo("America/Los_Angeles")
SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
PS = parse_sql(SQL); ST = [x for x in PS if x["op"] == "insert"]
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
OB = json.load(open(os.path.join(HERE, "oe_base.json")))
SEED = json.load(open(os.path.join(HERE, "seed_text.json")))
ID = {k: v["id"] for k, v in SEED.items()}; AT = {k: v["at"] for k, v in SEED.items()}
def rows(t, **kw): return [x["row"] for x in ST if x["table"] == t and all(x["row"].get(k) == v for k, v in kw.items())]
def clean(s): return (s or "").replace("\\r", "").replace("\\n", "\n").replace("\r", "")
def when(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00")); p = d.astimezone(PT)
    return f"{p.strftime('%a %b %-d %Y %-I:%M %p')} PT ({d.strftime('%b %-d %H:%M')} UTC)"
def tsw(ts): return when(dt.datetime.fromtimestamp(float(ts), dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
def Q(text, *qs):
    for q in qs: assert q in text, (q, text[:200])
    return " ".join('"' + q + '"' for q in qs)
SM = {f"{r['channel_id']}/{r['ts']}": clean(r["text"]) for r in rows("slack.slack_messages")}
LC = {r["id"]: clean(r["body"]) for r in rows("linear.linear_comments")}
LCI = {}
for r in rows("linear.linear_comments"): LCI.setdefault(r["issue_id"], []).append(r)
LI = {r["id"]: r for r in rows("linear.linear_issues")}
DOCS = {r["document_id"]: clean(r["body_text"]) for r in rows("gdocs.docs_documents")}
BS = OB["slack"]
EV = []
def oe(action, expected): EV.append((action, expected))
note = LC[ID["epic_note"]]
oe("Read Brian's message from yesterday in Slack (Calvin's DM with Brian Foster, his message of Tue Sep 30 2025)",
   f"Brian, {when(AT['hub'])}, message ts {ID['hub'].split('/')[1]}: " + Q(SM[ID['hub']], "Before Thursday's flow review I want the queue manager to be a real epic.", "I left a note on the ticket about how I want it.", "One child for each area, and every report gets its line under the right child.",
     "Please also put a stock-take sheet in your ZM queue manager folder and share it with everyone on the review invite, Leonard too, and add one slide with the numbers to your queue manager deck.",
     "When it is done tell me here how many reports are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many reports are on the review list."))
ep = OB["linear"]["ZOM-543"]["rec"]
oe("Find the Queue Manager ticket in Linear and read its comments (the ticket named in the prompt; OE 1 says Brian left a note on it)",
   f"ZOM-543 \"Queue Manager\", team ZOM, state In Progress, no parent. Brian's comment, {when(AT['epic_note'])}: " + Q(note, "Children: " + ", ".join(RP.AREAS) + ". One child each, same team, no assignee.", "Reports: the rows of Vincent's flow pass sheet, all of them.", "so don't add new reports from his chats",
     "Plus any bug somebody else on the team saw in a build and told you about in a DM since Vincent started his pass on the 26th, about the home screen after a level.", "If it is already a row, don't count it twice.",
     "Passed: Vincent's ok or nr on a build that counts under Arthur's rule for QA passes, as long as that pass still stands under his rule.", "Waiting on QA: not passed, and a fix for it is in main that QA has not tried on a main build yet.", "Waiting on a fix: everything else.",
     "if a ticket already has the report, move that ticket under the child and leave a note with the status and why.", "If its state does not match the status, put Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix.",
     "If no ticket has it, make a sub-issue under the child with the report as the title and the state the same way.", "No priority and no assignee on the new ones",
     "A child is Clear when all its reports are Passed, otherwise Open. Set the child to Done if it is Clear and to Todo if it is Open.", "Review list: a report that is not Passed, in an area on the agenda of Thursday's review.",
     "Sheet: tab Reports with Report, Area, Status, Ticket, Review list, Why. Tab Areas with Area, Status, Open reports. Slide: the five numbers I asked you for."))
grid = [x["row"] for x in ST if x["table"].endswith("sheets_sheets") and x["row"]["spreadsheet_id"] == ID["sheet"]][0]["grid_json"]
grid = grid if isinstance(grid, list) else json.loads(grid)
body = [r for r in grid if r and str(r[0]).isdigit()]; assert len(body) == 38
cell = lambda c: c if c != "" else "(blank)"
oe("Find and read Vincent's flow pass sheet in Drive (search \"flow pass\", named in OE 2; the sheet Vincent shared with Calvin, tab Flow pass)",
   "Sheet \"ZM home screen flow pass\", owner vincent.parker@harmonygames.co, columns " + ", ".join(grid[0]) + ". 38 rows: " + " ".join(f"[{r[0]}] {r[1]} | {r[2]} | found {cell(r[3])} | ticket {cell(r[4])} | fix {cell(r[5])} | re-test {cell(r[6])}." for r in body)
   + " Note under the table: " + Q("\n".join(" ".join(map(str, r)) for r in grid), "The codes are in my pass sheet legend doc."))
oe("Find and read the legend of Vincent's pass sheets in Drive (the note in OE 3 names it; list the Drive folder that holds the flow pass sheet)",
   "Doc \"How to read my pass sheets\": " + Q(DOCS[ID["legend"]], "Fix: the PR the dev told me it went into. Blank if nobody told me.", "Re-test: ok and a build means it is fine on that build.", "nr and a build means I could not make it happen on that build.", "again and a build means it still happens.",
     "ok, chat means I told the dev ok in our chat, the build is there.", "Blank means not re-tested yet."))
oe("Find and read Arthur's rule for QA passes in Drive (search \"QA passes\", the rule OE 2 names; Arthur Blake's doc shared with Calvin)",
   "Doc \"ZM builds and QA passes\": " + Q(DOCS[ID["rule_doc"]], "For ZM a QA pass only counts on a build of the main branch.", "A build of a feature branch is for the dev to check their own work, so a pass there has to be done again once the branch is merged.",
     "A pass stands until somebody sees the bug again on a main build made after the one it passed on. Then it is open again, whoever saw it.", "Which branch a build came from is in its #builds post."))
CT, VO, VB = "D06UPGF5PQV/1758817744.353289", "D06UPGF5PQV/1758820544.160399", "1758820551.265839"
oe("Read Calvin's DM with Vincent Parker in Slack around Sep 25 2025 for the ok behind the three \"ok, chat\" rows (rows 1, 2 and 25 in OE 3; OE 4 says the build is in the chat)",
   f"Calvin, {tsw(CT.split('/')[1])}: " + Q(BS[CT]["rec"]["text"], "Match 3D iOS Internal - #1718 already tested") + f" Vincent, {tsw(VO.split('/')[1])}: " + Q(BS[VO]["rec"]["text"], "Looks ok to me") + f" and, {tsw(VB)}: \"Boss arena as well\"")
BUILDS = dict(RP.MAIN_BUILDS); BUILDS.update(RP.BRANCH_BUILDS); BUILDS["Android Submission #135"] = "C05433XK267/1759263189.219529"; BUILDS.pop("iOS Internal #1754")
assert len(BUILDS) == 15
bl = []
for name, k in sorted(BUILDS.items(), key=lambda kv: kv[1]):
    fb = BS[k]["rec"]["attachments"][0]["fallback"]
    m = re.match(r"(.+?) - #(\d+) - (.+?) (Success|Started|Fail\w*|Back to normal|Still Failing|Aborted)", fb); assert m and m.group(2) == name.rsplit("#", 1)[1]
    bl.append(f"\"{m.group(1)} - #{m.group(2)} - {m.group(3).strip()}\" posted {tsw(k.split('/')[1])}")
oe("Read the #builds history in Slack from Sep 24 to Sep 30 2025 and pick out the post of every build the sheet names (OE 3), of #1718, the build Calvin names just before Vincent's ok (OE 6), and of Android Submission 135, the build the ticket notes name (OE 7); OE 5 says the branch is in the build's post",
   "Fifteen result posts (the Success post of each build, which carries the branch), oldest first: " + "; ".join(bl) + ". Twelve are builds of main. iOS Internal #1698, #1718 and #1746 are builds of feature branches, so the ok on #1718 (rows 1, 2 and 25) does not count. Android Submission #135 is a main build posted after iOS Internal #1745, #1750 and #1757.")
P = {n: OB["github"][n]["rec"] for n in ("465", "472", "473", "475")}
bodyupd = [x for x in PS if x["op"] == "update" and x["table"].endswith("github_pull_requests") and "body" in x["set"]][0]["set"]["body"]
oe("Read pull requests #465, #472 and #475 of match3d in GitHub (the PRs in the sheet's Fix column, OE 3)",
   "; ".join(f"#{n} \"{P[n]['title']}\", base {P[n]['base_ref']}, merged {when(P[n]['merged_at'])}" for n in ("465", "472", "475")) + ". The description of #472 starts: " + Q(clean(bodyupd), "Implement Win&Collect into Queue Manager (this also holds the pre-level panel until the level-end coins have landed)") + " That is row 6's bug.")
RC = {r["id"]: clean(r["body"]) for r in rows("github.github_review_comments")}
oe("Read the review comments on pull request #472 in GitHub (OE 9; the same text is in the #zombie-prs thread under the PR's post and in Calvin's GitHub mail)", f"Login EMPLOYEE_0025_GITHUB_USERNAME (Arthur Blake in the GitHub user record), {when(AT['inline'])}: " + Q(RC[ID["inline"]], "Flow sheet has the season pass icon restart and the event bar starting under the gift popup against this PR. Neither is in this diff. The other two Collect & Win ones are. Those two need their own PR.") + " Rows 12 and 15 are not fixed by #472; rows 17 and 18 are in it.")
oe("Read the review comments on pull request #475 in GitHub (OE 9; the same text is in the #zombie-prs thread under the PR's post and in Calvin's GitHub mail)", f"Login EMPLOYEE_0025_GITHUB_USERNAME (Arthur Blake), {when(AT['inline2'])}: " + Q(RC[ID["inline2"]], "Don't see the pack sound stop anywhere in here. Still needs doing.") + " Row 32 is not fixed by #475.")
PC = clean(rows("github.github_pr_comments")[0]["body"])
oe("List the match3d pull requests merged since Vincent started his sheet (created Fri Sep 26 2025 3:12 AM PT, 10:12 UTC, OE 3) and read the conversation of each one the sheet does not name (OE 2: a fix that is in main)",
   "Eight merged pull requests are not on the sheet: #466 (merged Sep 26 15:14 UTC), #467 (Sep 26 18:58 UTC), #468 (Sep 29 16:13 UTC), #469 (Sep 30 01:50 UTC), #470 (Sep 30 15:51 UTC), #471 (Sep 30 15:52 UTC), #473 (Sep 30 15:41 UTC) and #474 (Sep 30 15:48 UTC). #463 merged Sep 25 5:08 PM PT (Sep 26 00:08 UTC), before the sheet was started, and is not one of them. One of them speaks about the flow list: " + f"#473 \"{P['473']['title']}\", base {P['473']['base_ref']}, merged {when(P['473']['merged_at'])}. The comment on it by login EMPLOYEE_0003_GITHUB_USERNAME (Oliver Brooks in the GitHub user record), {when(AT['else_pr'])}: " + Q(PC, "For the flow list, this also has four fixes: the pass start popup coming back after every level, the pass bar filling before the tokens land, the claim animation playing twice after the shop, and the freezer popup opening behind the pass popup.") + " Those are rows 13, 38, 14 and 37.")
def cm(issue, frag):
    c = [r for r in LCI[issue] if frag in clean(r["body"])][0]; return c
seeded = sorted(LI, key=lambda k: int(k.split("-")[1]))
c585, c586, c576, c582 = cm("ZOM-585", "Got this again"), cm("ZOM-586", "starts from zero again"), cm("ZOM-576", "My last try"), cm("ZOM-582", "Still the same")
c577 = cm("ZOM-577", "fix locally")
oe("Read the 20 tickets in the sheet's Ticket column in Linear, each with its comments (ZOM-567 to ZOM-586, OE 3)",
   "State as found: " + "; ".join(f"{k} {LI[k]['state_id']}" for k in seeded) + f". Later notes: on ZOM-585, Samuel Turner, {when(c585['created_at'])}: " + Q(clean(c585["body"]), "Got this again on Android Submission 135, so #472 did not sort it.")
   + f" On ZOM-586, Owen Baker, {when(c586['created_at'])}: " + Q(clean(c586["body"]), "Android Submission 135: the lane bar starts from zero again every time I open home.")
   + " On ZOM-576, Vincent: " + Q(clean(c576["body"]), "I was told #472 has this. My last try was Android 2013, still there.") + " On ZOM-582, Vincent: " + Q(clean(c582["body"]), "I was told #475 has this. Still the same on iOS Internal 1757.")
   + f" On ZOM-577, Owen Baker, {when(c577['created_at'])}: " + Q(clean(c577["body"]), "I have a fix locally, need to test it before I open the PR") + " That fix is not in main.")
z556, z560 = OB["linear"]["ZOM-556"]["rec"], OB["linear"]["ZOM-560"]["rec"]
oe("Search the ZM tickets in Linear, by each row's wording, for a ticket that already holds a row whose Ticket cell is blank in OE 3 (rows 1, 2, 3, 5, 7, 9, 11, 20, 22, 23, 25, 26, 27, 29, 31, 33, 35, 38), and read the comments of the candidates",
   f"ZOM-556 \"{z556['title']}\", state Todo; Vincent's comment, {when(AT['alias_gift'])}: " + Q(LC[ID["alias_gift"]], "Saw this one myself in my home screen pass on 1727, the day counter keeps going after a skipped day. Same thing.")
   + f" ZOM-560 \"{z560['title']}\", state Todo; Vincent's comment, {when(AT['alias_streak'])}: " + Q(LC[ID["alias_streak"]], "Still there on Android 1984 in my home screen pass, the freezer from the abandoned pack never shows up on home.") + " Row 11 is held by ZOM-556 and row 20 by ZOM-560. The searches return no ticket for the other sixteen rows.")
oe("Search Slack for other sightings on Android Submission 135, the build Samuel and Owen name in OE 7 (search \"Submission 135\"), and open the threads of the hits",
   f"In #zombie-bugs, Vincent Parker's reply under his thread of Mon Sep 15 2025, {when(AT['reopen'])}: " + Q(SM[ID["reopen"]], "from Android Submission 135 today: with a gift and a new pass stage both due after a level, the pass popup came up on top of the gift again") + " That is row 9."
   + f" Robert's reply under his thread of Tue Sep 9 2025 PT (Sep 10 UTC), {when(AT['back'])}: " + Q(SM[ID["back"]], "Played Android Submission 135 for an hour.", "coming back from endless the home intro animation played again every single time") + " That is row 29.")
oe("Search Slack for other sightings of the ten rows that still read as passed, by each row's wording in OE 3 (rows 3, 5, 7, 22, 23, 26, 27, 31, 33, 35; for row 27 search \"arena entry button\")",
   f"In #zombie-match3d, Robert, {when(AT['older'])}: " + Q(SM[ID["older"]], "Android 2006: I could tap the arena entry button while the reward animation was playing, and it went through") + " That is row 27. Android #2006 was posted before iOS Internal #1745 (OE 8), the build row 27 passed on, so that pass stands. The searches return no later sighting for the other nine rows.")
oe("Read Calvin's other DMs in Slack since Sep 26 2025 for a bug somebody told him about (OE 2's rule; the DM with Marcus Bennett)",
   f"Marcus Bennett, {when(AT['filt_dm'])}: " + Q(SM[ID["filt_dm"]], "yo on today's main build the pass icon glow stays on after i claimed everything") + " and, in his next message, " + Q(SM["D05U73FNDDL/1759252231." + [k for k in SM if k.startswith("D05U73FNDDL/1759252231")][0].split(".")[1]], "saw it 3 levels in a row. its not the vfx, the animation itself is fine, its just the glow") + " No sheet row has it and a search of the ZM tickets for \"icon glow\" (as in OE 13) returns no ticket; it is a 39th report, in Season Pass. Calvin's four other DMs with messages since Sep 26 (Brian, Vincent, Owen Baker and one more colleague) carry no other bug seen in a build; Owen's Sep 29 remark that everything looks a little slower is about Calvin's video, not a build.")
gm = [r for r in rows("gmail.gmail_messages") if r["id"] == ID["invite_v2"]][0]
gm1 = [r for r in rows("gmail.gmail_messages") if r["id"] == ID["invite_v1"]][0]
oe("Find the review invite in Gmail (search \"flow review\", the review named in the prompt and OE 1)",
   f"From leonard.hayes@harmonygames.co, {when(AT['invite_v2'])}, subject starts " + Q(gm["subject"], "Updated invitation with note: ZM home screen flow review @ Thu Oct 2, 2025") + " Note: " + Q(clean(gm["body_text"]), "Moved up a day. Agenda is on the roadmap card, I changed it, daily gift waits until next week.") + " The Sep 29 invitation for Fri Oct 3 (" + Q(clean(gm1["body_text"]), "Collect & Win and Daily Gift this time") + ") is the earlier version.")
ev = [r for r in rows("gcal.gcal_events") if r["event_id"] == ID["event"]][0]
att = sorted(a["email"] for a in (ev["attendees_json"] if isinstance(ev["attendees_json"], list) else json.loads(ev["attendees_json"])) if a["email"] != "calvin.price@harmonygames.co")
oe("Read the review event on Calvin's calendar (search \"flow review\", OE 17)", f"\"ZM home screen flow review\", starts Thu Oct 2 2025 11:00 AM PT (18:00 UTC). Attendees besides Calvin: " + ", ".join(att) + ".")
card = [r for r in rows("trello.trello_cards") if r["id"] == ID["rev_card"]][0]
oe("Find the review's card on the ZM ROADMAP board in Trello and read its history (search \"flow review\"; OE 17 says the agenda is on the roadmap card)",
   "Card " + Q(card["name"], "ZM home screen flow review - Thu Oct 2") + ", description: " + Q(clean(card["desc"]), "Walk through what is still not passed in: Collect & Win, Level-end rewards.") + f" Leonard Hayes changed the name and description on {when(AT['rev_card_update'])}; the earlier description listed Collect & Win, Daily Gift.")
oe("Find Calvin's ZM queue manager folder and deck in Drive (search \"ZM queue manager\", named in the prompt)", "Folder \"ZM queue manager\", owner calvin.price@harmonygames.co. In it, the presentation \"ZM queue manager\", owner calvin.price@harmonygames.co.")
# decision
ROWS = RP.truth()
def why(r):
    return TRUTH[r["report"]]["Why"]
lines = []
for r in ROWS:
    t = TRUTH[r["report"]]
    lines.append(f"[{r['n']}] {t['Status']}" + (f", {t['Ticket']}" if t["Ticket"] else ", new") + (", review list" if t["Review list"] == "Yes" else ""))
areas = {a: (sum(1 for r in ROWS if r["area"] == a), sum(1 for r in ROWS if r["area"] == a and r["status"] != RP.P)) for a in RP.AREAS}
NP, NQ, NF = (sum(r["status"] == s for r in ROWS) for s in (RP.P, RP.Q, RP.F)); NREV = sum(TRUTH[r["report"]]["Review list"] == "Yes" for r in ROWS)
assert (NP, NQ, NF, NREV) == (10, 9, 20, 7) and all(v[1] for v in areas.values())
oe("Work out each report's status, ticket and review-list flag from the note's rules (OE 2) and the records in OE 3 to OE 19",
   "39 reports (38 rows plus Marcus's, numbered 39). " + " ".join(l + "." for l in lines) + f" Totals: {NP} Passed, {NQ} Waiting on QA, {NF} Waiting on a fix. Areas, open of total: " + ", ".join(f"{a} {v[1]} of {v[0]}" for a, v in areas.items())
   + f". Every area is Open, so 0 areas are Clear. Review list (not Passed, in Collect & Win or Level-end rewards, OE 19): {NREV} reports, rows " + ", ".join(str(r['n']) for r in ROWS if TRUTH[r['report']]['Review list'] == 'Yes') + ".")
DEC = len(EV)
# writes
for a in RP.AREAS:
    oe(f"Create the {a} child under the Queue Manager ticket in Linear (fields from OE 2)", f"A new ZOM issue titled \"{a}\", parent ZOM-543, state Todo, no assignee.")
for r in ROWS:
    t = TRUTH[r["report"]]
    if not t["Ticket"]:
        ttl = f"titled \"{r['report']}\"" if r["n"] <= 38 else "titled with Marcus's report (the pass icon glow staying on after everything is claimed)"
        oe(f"Create the sub-issue for report {r['n']} under the {r['area']} child in Linear (OE {DEC})", f"A new ZOM issue {ttl}, parent the {r['area']} child, state {t['Ticket state']}, no priority, no assignee.")
for r in ROWS:
    t = TRUTH[r["report"]]
    if t["Ticket"]:
        ch = t["Ticket state as found"] != t["Ticket state"]
        oe(f"Move {t['Ticket']} (report {r['n']}) under the {r['area']} child in Linear" + (" and set its state" if ch else "") + f" (OE {DEC})",
           f"{t['Ticket']} has the {r['area']} child as its parent" + (f" and is in state {t['Ticket state']} (it was {t['Ticket state as found']})." if ch else f"; its state stays {t['Ticket state']}."))
for r in ROWS:
    t = TRUTH[r["report"]]
    if t["Ticket"]:
        oe(f"Leave the status note on {t['Ticket']} (report {r['n']}) in Linear (OE 2's rule, OE {DEC})", f"A comment on {t['Ticket']} giving the status {t['Status']} and why: {why(r)}.")
oe("Create the stock-take sheet in Sheets with a first tab named Reports (OE 1, tab name from OE 2)", "A new spreadsheet owned by Calvin whose first tab is Reports.")
oe(f"Write the Reports tab of the stock-take sheet (columns from OE 2, rows from OE {DEC}, ticket keys of the new sub-issues from their create steps)", "Tab Reports with the columns Report, Area, Status, Ticket, Review list, Why and 39 report rows: 10 Passed, 9 Waiting on QA, 20 Waiting on a fix; 7 rows marked for the review list.")
oe("Add a second tab named Areas to the stock-take sheet (tab name from OE 2)", "The spreadsheet has the tabs Reports and Areas.")
oe(f"Write the Areas tab of the stock-take sheet (columns from OE 2, values from OE {DEC})", "Tab Areas with the columns Area, Status, Open reports and 10 rows, every area Open: " + ", ".join(f"{a} {v[1]}" for a, v in areas.items()) + ".")
oe("Put the stock-take sheet in the ZM queue manager folder in Drive (folder from OE 20)", "The sheet's parent is the folder \"ZM queue manager\".")
names = {"arthur.blake": "Arthur Blake", "brian.foster": "Brian Foster", "julia.lawson": "Julia Lawson", "leonard.hayes": "Leonard Hayes", "vincent.parker": "Vincent Parker"}
for a in att:
    oe(f"Share the stock-take sheet with {names[a.split('@')[0]]} in Drive (address from OE 18)", f"{a} can open the sheet (writer, commenter or reader).")
oe(f"Add one slide with the five numbers to the ZM queue manager deck in Slides (deck from OE 20, numbers from OE {DEC})", "A new slide in the presentation \"ZM queue manager\" with: 10 passed, 9 waiting on QA, 20 waiting on a fix, 0 areas clear, 7 on the review list.")
oe(f"Message Brian in the DM in Slack (the DM from OE 1, after every other write)", "A message in Calvin's DM with Brian Foster with the numbers he asked for: 10 reports passed, 9 waiting on QA, 20 waiting on a fix, 0 areas clear, 7 on the review list.")
ti = [i for i, (a, e) in enumerate(EV) if a.startswith("Read the 20 tickets")][0]; bi = [i for i, (a, e) in enumerate(EV) if a.startswith("Read the #builds history")][0]
assert (ti, bi) == (11, 6) and DEC == 21
EV.insert(bi, EV.pop(ti))
out = []
for i, (a, e) in enumerate(EV, 1):
    out += [f"OE {i}  {a}", f"Expected: {e}", ""]
open(os.path.join(TI, "08_Oracle_Events.md"), "w").write("\n".join(out))
json.dump([{"n": i, "action": a} for i, (a, e) in enumerate(EV, 1)], open(os.path.join(HERE, "oe_events_index.json"), "w"), indent=1)
print("events", len(EV), "decision OE", DEC, "chars", sum(len(x) for x in out))

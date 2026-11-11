#!/usr/bin/env python3
"""Builds the planned seed texts, the draft manifest and the gradable surface for calvin_qm_epic (design only).
Seed texts are planned records for /create-injection, not prompt, Oracle Event or criterion text."""
import hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import reports as RP
ctx = json.load(open(os.path.join(WF, "00_Task_Context.json")))
h = lambda s, n=32: hashlib.sha256(s.encode()).hexdigest()[:n]
cid = lambda s: "comment_" + h("calvin_qm:" + s)
fid = lambda s: "f_" + h("calvin_qm:" + s, 22)
BDM, VDM, MDM, JDM = "D0770ET6WBW", "D06UPGF5PQV", "D05U73FNDDL", "D05HYDTG5TJ"
BUILDS, BUGS, PRS, ZM3D = "C05433XK267", "C08R27X0EAH", "C093LEZGF6J", "C0880U9751A"
import datetime as _dt
def _epoch(iso): return int(_dt.datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=_dt.timezone.utc).timestamp())
def gmail_id(iso, salt):   # base Gmail ids carry their time: id >> 20 = milliseconds
    return "calvin.price@harmonygames.co/" + str((_epoch(iso) * 1000 << 20) | (int(h("gm:" + salt, 5), 16) & 0xFFFFF))
def trello_id(iso, salt):  # base Trello ids start with the hex second they were made
    return format(_epoch(iso), "08x") + h("tr:" + salt, 16)
T_HUB, T_NOTE, T_GATE_OLD = "2025-09-30T20:40:05Z", "2025-09-30T20:25:37Z", "2025-09-29T16:41:12Z"
T_CARD, T_CARD_UPD, T_INV1, T_INV2 = "2025-09-29T16:02:11Z", "2025-09-30T17:22:36Z", "2025-09-29T16:05:14Z", "2025-09-30T17:24:09Z"
T_BACK, T_INLINE, T_INLINE2, T_ALIAS1, T_ALIAS2 = "2025-09-30T21:44:12Z", "2025-09-30T15:53:40Z", "2025-09-30T16:09:50Z", "2025-09-30T18:05:21Z", "2025-09-30T18:08:48Z"
T_ELSE = "2025-09-30T15:42:10Z"
T_REOPEN2, T_BACK2 = "2025-09-30T21:52:18Z", "2025-09-30T22:07:44Z"
PRB = json.load(open(os.path.join(HERE, "pr_bodies.json")))
HUB = f"{BDM}/{_epoch(T_HUB)}.214409"
GATE_OLD = f"{BDM}/{_epoch(T_GATE_OLD)}.337219"
REOPEN = f"{BUGS}/1759267212.418339"
BACK = f"{BUGS}/{_epoch(T_BACK)}.552719"
T_OLDER = "2025-09-29T22:40:27Z"
OLDER = f"{ZM3D}/{_epoch(T_OLDER)}.317849"
SUBM_ROOT, ENDLESS_ROOT = f"{BUGS}/1757939514.864549", f"{BUGS}/1757467270.178829"   # base: Vincent's Sep 15 submission-issues thread; Robert's Sep 10 endless thread
FILT_DM = f"{MDM}/1759252212.611349"
EPIC_NOTE = cid("epic-note-543")
ALIAS_GIFT, ALIAS_STREAK = cid("alias-556"), cid("alias-560")
REOPEN2, BACK2 = cid("reopen-585"), cid("back-586")
SHEET, LEGEND, RULEDOC, DDDOC, QMDECK = fid("vincent-pass-sheet"), fid("vincent-legend"), fid("arthur-zm-builds"), fid("arthur-dd-hotfix"), fid("calvin-qm-deck")
FOLDER = "d_" + h("calvin_qm:folder", 22)
def cal_msgid(key): return "calvin.price@harmonygames.co/<calendar-%s-%s-%s-%s-%s@google.com>" % (h("cal:" + key, 8), h("cal1:" + key, 4), h("cal2:" + key, 4), h("cal3:" + key, 4), h("cal4:" + key, 12))
INV1, INV2 = cal_msgid("inv1"), cal_msgid("inv2")          # message rows; the numeric thread ids are gmail_id(T_INV1, "inv1") and gmail_id(T_INV2, "inv2")
INV1_THREAD, INV2_THREAD = gmail_id(T_INV1, "inv1"), gmail_id(T_INV2, "inv2")
EVT = "evt_" + h("calvin_qm:review", 22)
REVCARD, REV_UPDATE = trello_id(T_CARD, "card"), trello_id(T_CARD_UPD, "update")
REV_CREATE = REVCARD[:20] + h("tr:create", 4)          # base createCard ids share the card id's first 20 hex
INLINE = "harmonygames-Games/match3d#472#rc_1"
INLINE2 = "harmonygames-Games/match3d#475#rc_1"
ELSE_PR = "harmonygames-Games/match3d#473#c_2"
PR472, PR473, PR475, PR465 = "harmonygames-Games/match3d#472", "harmonygames-Games/match3d#473", "harmonygames-Games/match3d#475", "harmonygames-Games/match3d#465"
B1718, B135 = f"{BUILDS}/1758817549.151639", f"{BUILDS}/1759263189.219529"
B2006, B1745 = f"{BUILDS}/1759160363.685759", f"{BUILDS}/1759162758.968639"
V_OK, C_TESTED = f"{VDM}/1758820544.160399", f"{VDM}/1758817744.353289"
PARK_A, PARK_B = f"{VDM}/1758806199.381319", f"{BDM}/1758808795.588519"
JULIA = f"{JDM}/1756838837.147599"
SHADER_ROOT = f"{BUGS}/1759249488.495439"
AREAS = RP.AREAS
SEED = {
 "hub": ("slack", HUB, "Brian Foster", T_HUB, "Before Thursday's flow review I want the queue manager to be a real epic. Right now it is one ticket, and Vincent's flow pass is a sheet on its own. I left a note on the ticket about how I want it. One child for each area, and every report gets its line under the right child. Please also put a stock-take sheet in your ZM queue manager folder and share it with everyone on the review invite, Leonard too, and add one slide with the numbers to your queue manager deck. When it is done tell me here how many reports are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many reports are on the review list."),
 "epic_note": ("linear", EPIC_NOTE, "Brian Foster", T_NOTE, "How I want this epic.\n\nChildren: " + ", ".join(AREAS) + ". One child each, same team, no assignee.\n\nReports: the rows of Vincent's flow pass sheet, all of them. For Vincent that sheet is the list, so don't add new reports from his chats, and his Bug Checklist canvas and the Collect & Win canvas stay as they are. Plus any bug somebody else on the team saw in a build and told you about in a DM since Vincent started his pass on the 26th, about the home screen after a level. If it is already a row, don't count it twice. The skip tutorial exceptions Oliver has in #zombie-bugs and the input blocker I parked are not on the sheet and stay off.\n\nStatus of a report, as it stands today, one of three. Passed: Vincent's ok or nr on a build that counts under Arthur's rule for QA passes, as long as that pass still stands under his rule. Waiting on QA: not passed, and a fix for it is in main that QA has not tried on a main build yet. Waiting on a fix: everything else.\n\nLine under the child: if a ticket already has the report, move that ticket under the child and leave a note with the status and why. If its state does not match the status, put Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix. If no ticket has it, make a sub-issue under the child with the report as the title and the state the same way. No priority and no assignee on the new ones, that is Julia's point about your tickets, I will set them.\n\nA child is Clear when all its reports are Passed, otherwise Open. Set the child to Done if it is Clear and to Todo if it is Open.\n\nReview list: a report that is not Passed, in an area on the agenda of Thursday's review.\n\nSheet: tab Reports with Report, Area, Status, Ticket, Review list, Why. Tab Areas with Area, Status, Open reports. Slide: the five numbers I asked you for."),
 "gate_old": ("slack", GATE_OLD, "Brian Foster", T_GATE_OLD, "For the flow review on Friday I want to go through collect&win and daily gift first, the rest can come after"),
 "sheet": ("gsheets", SHEET, "Vincent Parker", "2025-09-30T19:30:52Z", "ZM home screen flow pass\n\nColumns: #, Area, What happens, Found on, Ticket, Fix, Re-test. 38 rows, in plan/reports.py.\n\nNote under the table: Home screen flow only, the pass Brian asked me for. Everything else stays on my Bug Checklist canvas. The codes are in my pass sheet legend doc."),
 "legend": ("gdocs", LEGEND, "Vincent Parker", "2025-09-26T10:31:08Z", "How to read my pass sheets\n\nFound on: the build I first saw it on.\nTicket: the Linear key if I filed one.\nFix: the PR the dev told me it went into. Blank if nobody told me.\nRe-test: ok and a build means it is fine on that build. nr and a build means I could not make it happen on that build. again and a build means it still happens. ok, chat means I told the dev ok in our chat, the build is there. Blank means not re-tested yet."),
 "rule_doc": ("gdocs", RULEDOC, "Arthur Blake", "2025-09-12T22:29:41Z", "ZM builds and QA passes\n\nInternal, Android and Submission are only the jobs. What matters is the branch. For ZM a QA pass only counts on a build of the main branch. A build of a feature branch is for the dev to check their own work, so a pass there has to be done again once the branch is merged.\n\nIf you want QA to look at a branch build before you merge, that is fine and it saves time, just don't call it passed.\n\nA pass stands until somebody sees the bug again on a main build made after the one it passed on. Then it is open again, whoever saw it.\n\nWhich branch a build came from is in its #builds post."),
 "dd_doc": ("gdocs", DDDOC, "Arthur Blake", "2025-07-10T15:49:27Z", "DD hotfix builds and QA passes\n\nFor DD hotfixes a pass on the dev's branch build is enough, we cherry-pick those straight onto the release branch.\n\nAnything that is not a hotfix goes through develop and gets its pass there."),
 "rev_card_v1": ("trello", REV_CREATE, "Leonard Hayes", T_CARD, "ZM home screen flow review - Fri Oct 3\n\nWalk through what is still not passed in: Collect & Win, Daily Gift."),
 "rev_card": ("trello", REVCARD, "Leonard Hayes", T_CARD_UPD, "ZM home screen flow review - Thu Oct 2\n\nWalk through what is still not passed in: Collect & Win, Level-end rewards."),
 "rev_card_update": ("trello", REV_UPDATE, "Leonard Hayes", T_CARD_UPD, "updateCard: name and description changed to the Thu Oct 2 version"),
 "invite_v1": ("gmail", INV1, "Leonard Hayes", T_INV1, "Subject: Invitation: ZM home screen flow review @ Fri Oct 3, 2025 12pm - 12:30pm (CST) (calvin.price@harmonygames.co)\n\nEvent description: Agenda is on the roadmap card: Collect & Win and Daily Gift this time."),
 "invite_v2": ("gmail", INV2, "Leonard Hayes", T_INV2, "Subject: Updated invitation with note: ZM home screen flow review @ Thu Oct 2, 2025 12pm - 12:30pm (CST) (calvin.price@harmonygames.co)\n\nNote: Moved up a day. Agenda is on the roadmap card, I changed it, daily gift waits until next week."),
 "event": ("gcal", EVT, "Leonard Hayes", T_INV2, "ZM home screen flow review, Thu Oct 2 2025 18:00 UTC. Attendees: Leonard Hayes, Brian Foster, Arthur Blake, Julia Lawson, Vincent Parker, Calvin Price."),
 "inline": ("github", INLINE, "Arthur Blake", T_INLINE, "Flow sheet has the season pass icon restart and the event bar starting under the gift popup against this PR. Neither is in this diff. The other two Collect & Win ones are. Those two need their own PR."),
 "inline2": ("github", INLINE2, "Arthur Blake", T_INLINE2, "Don't see the pack sound stop anywhere in here. Still needs doing."),
 "reopen": ("slack", REOPEN, "Vincent Parker", "2025-09-30T21:20:12Z", "from Android Submission 135 today: with a gift and a new pass stage both due after a level, the pass popup came up on top of the gift again"),
 "back": ("slack", BACK, "Robert", T_BACK, "Played Android Submission 135 for an hour. No freeze this time, but coming back from endless the home intro animation played again every single time. Thought that was sorted"),
 "older": ("slack", OLDER, "Robert", T_OLDER, "Android 2006: I could tap the arena entry button while the reward animation was playing, and it went through"),
 "else_pr": ("github", ELSE_PR, "Oliver Brooks", T_ELSE, "For the flow list, this also has four fixes: the pass start popup coming back after every level, the pass bar filling before the tokens land, the claim animation playing twice after the shop, and the freezer popup opening behind the pass popup."),
 "reopen2": ("linear", REOPEN2, "Samuel", T_REOPEN2, "Got this again on Android Submission 135, so #472 did not sort it. The reward animation sits there a good two seconds before the event bar starts to fill."),
 "back2": ("linear", BACK2, "Owen Baker", T_BACK2, "Android Submission 135: the lane bar starts from zero again every time I open home. Same as before."),
 "body472": ("github", PR472, "Calvin Price", "2025-09-30T15:53:04Z", PRB["472"]["new"]),
 "filt_dm": ("slack", FILT_DM, "Marcus Bennett", "2025-09-30T17:10:12Z", "yo on today's main build the pass icon glow stays on after i claimed everything, saw it 3 levels in a row. its not the vfx, the animation itself is fine, its just the glow"),
 "alias_gift": ("linear", ALIAS_GIFT, "Vincent Parker", T_ALIAS1, "Saw this one myself in my home screen pass on 1727, the day counter keeps going after a skipped day. Same thing."),
 "alias_streak": ("linear", ALIAS_STREAK, "Vincent Parker", T_ALIAS2, "Still there on Android 1984 in my home screen pass, the freezer from the abandoned pack never shows up on home."),
 "deck": ("gslides", QMDECK, "Calvin Price", "2025-09-23T16:20:33Z", "ZM queue manager\n\nSlide 1: what the queue manager orders on the home screen. Slide 2: order of events."),
 "folder": ("gdrive", FOLDER, "Calvin Price", "2025-09-23T16:00:18Z", "ZM queue manager"),
}
def q(k, s):
    if s not in SEED[k][4]: raise SystemExit(f"quote not in {k}: {s}")
    return s
frag = lambda i, svc, cont, kind, via, seeded, bp, by, quote, reqs, **kw: dict(id=i, service=svc, container=cont, locator=cont, kind=kind, incorporated_via=via, seeded_ids=seeded, base_pointers=bp, delegated_by_record=by, delegation_quote=quote, requirement_ids=reqs, **kw)
frags = [
 frag("K1", "linear", "ZOM-543", "delegation", ["AN1"], [EPIC_NOTE], [], HUB, q("hub", "I left a note on the ticket"), ["R2", "R3", "R4", "R6", "R9"],
      names_authorities=[{"id": "H1", "quote": q("epic_note", "Arthur's rule for QA passes")}, {"id": "H2", "quote": q("epic_note", "the agenda of Thursday's review")}]),
 frag("K2", "gsheets", SHEET, "requirement", ["AN1"], [SHEET], [], HUB, q("hub", "Vincent's flow pass"), ["R1"]),
 frag("K3", "gdocs", RULEDOC, "requirement", ["AN1", "K1"], [RULEDOC], [], EPIC_NOTE, q("epic_note", "Arthur's rule for QA passes"), ["R3"]),
 frag("K4", "trello", REVCARD, "requirement", ["AN1", "K1"], [REVCARD, REV_UPDATE], [], EPIC_NOTE, q("epic_note", "the agenda of Thursday's review"), ["R5"]),
 frag("K5", "gdrive", FOLDER, "destination", ["AN1"], [FOLDER], [], HUB, q("hub", "your ZM queue manager folder"), ["R7"]),
 frag("K6", "gdocs", LEGEND, "format", ["AN1", "K2"], [LEGEND], [], SHEET, q("sheet", "my pass sheet legend"), ["R3"]),
 frag("K7", "gcal", EVT, "recipient", ["AN1"], [EVT], [], HUB, q("hub", "everyone on the review invite"), ["R7"]),
 frag("K8", "slack", MDM, "requirement", ["AN1", "K1"], [FILT_DM], [], EPIC_NOTE, q("epic_note", "told you about in a DM"), ["R1"]),
 frag("K9", "slack", VDM, "requirement", ["AN1", "K2", "K6"], [], [V_OK], LEGEND, q("legend", "I told the dev ok in our chat"), ["R3"]),
 frag("K10", "github", PR472, "requirement", ["AN1", "K1"], [INLINE], [], EPIC_NOTE, q("epic_note", "a fix for it is in main"), ["R3"]),
 frag("K16", "github", PR475, "requirement", ["AN1", "K1"], [INLINE2], [], EPIC_NOTE, q("epic_note", "a fix for it is in main"), ["R3"]),
 frag("K11", "github", PR473, "requirement", ["AN1", "K1"], [ELSE_PR], [], EPIC_NOTE, q("epic_note", "a fix for it is in main"), ["R3"]),
 frag("K12", "linear", "ZOM-556", "requirement", ["AN1", "K1"], [ALIAS_GIFT], ["ZOM-556"], EPIC_NOTE, q("epic_note", "if a ticket already has the report"), ["R4"]),
 frag("K13", "slack", BUGS, "amendment", ["AN1", "K1", "K3"], [REOPEN], [], RULEDOC, q("rule_doc", "until somebody sees the bug again on a main build made after the one it passed on"), ["R3"]),
 frag("K18", "slack", BUGS, "amendment", ["AN1", "K1", "K3"], [BACK], [], RULEDOC, q("rule_doc", "until somebody sees the bug again on a main build made after the one it passed on"), ["R3"]),
 frag("K21", "linear", "ZOM-585", "amendment", ["AN1", "K1", "K3"], [REOPEN2], [], RULEDOC, q("rule_doc", "until somebody sees the bug again on a main build made after the one it passed on"), ["R3"]),
 frag("K22", "linear", "ZOM-586", "amendment", ["AN1", "K1", "K3"], [BACK2], [], RULEDOC, q("rule_doc", "until somebody sees the bug again on a main build made after the one it passed on"), ["R3"]),
 frag("K14", "slack", JDM, "format", ["AN1", "K1"], [], [JULIA], EPIC_NOTE, q("epic_note", "Julia's point about your tickets"), ["R6"]),
 frag("K15", "linear", "ZOM-560", "requirement", ["AN1", "K1"], [ALIAS_STREAK], ["ZOM-560"], EPIC_NOTE, q("epic_note", "if a ticket already has the report"), ["R4"]),
 frag("K19", "gslides", QMDECK, "destination", ["AN1"], [QMDECK], [], HUB, q("hub", "your queue manager deck"), ["R9"]),
 frag("K20", "gmail", INV2, "recipient", ["AN1"], [INV2], [], HUB, q("hub", "the review invite"), ["R7"]),
]
vr = lambda service, rid, cont, seeded, at, **kw: dict(service=service, seeded=seeded, at=at, container=cont, **({"id": rid} if seeded else {"base_pointer": rid}), **kw)
T = lambda i, fam, svcs, seeded, bp, req, wrong, res, **kw: dict(id=i, family=fam, services=svcs, seeded_ids=seeded, base_pointers=bp, requirement=req, expected_wrong_reading=wrong, resolver=res, **kw)
traps = [
 T("T_BRANCH", "done_gap", ["gsheets", "slack", "gdocs"], [SHEET, RULEDOC], [V_OK, C_TESTED, B1718], "R3",
   "rows 1, 2 and 25 are Passed: the sheet says ok and Vincent wrote looks ok, boss arena as well, in the chat",
   "the build he looked at, Match 3D iOS Internal #1718, was cut from Calvin's QueueManager branch (the #builds post says so) and Arthur's rule counts only builds of the main branch; #465 is merged, so they wait on QA",
   discovery_order="the sheet row and the chat ok are both met before anyone looks the build number up in #builds"),
 T("T_INLINE", "done_gap", ["gsheets", "github", "linear"], [INLINE, "ZOM-571", "ZOM-574"], [PR472], "R3",
   "rows 12 and 15 wait on QA: the sheet gives #472 as their fix, #472 is merged and both tickets are In Validation",
   "Arthur's inline review comment on #472 says the season pass icon restart and the event bar start are not in that diff; the review body is empty and the PR's own summary lists only the Collect & Win wait",
   discovery_order="the merged PR and the In Validation ticket come back first; the inline comment needs github_get_pull_request_comments"),
 T("T_INLINE_PACK", "done_gap", ["gsheets", "github", "linear"], [INLINE2, "ZOM-581"], [PR475], "R3",
   "row 32 waits on QA: the sheet gives #475 as its fix, #475 is merged and the ticket is In Validation",
   "Arthur's inline review comment on #475 says the pack sound stop is nowhere in that PR; the review body is empty and the PR's summary does not mention sound",
   discovery_order="the merged PR and the In Validation ticket come back first; the inline comment needs its own call"),
 T("T_REOPEN", "superseding", ["gsheets", "slack"], [SHEET, REOPEN], [B135], "R3",
   "row 9 is Passed: nr on a main build",
   "Vincent's later reply under his Sep 15 submission-issues thread in #zombie-bugs says it came back on Android Submission 135, a main build made after #1745, so under Arthur's note the pass no longer stands",
   discovery_order="the sheet is read first; the reply sits under a root two weeks older than the pass",
   version_records=[vr("gsheets", SHEET, f"file:{SHEET}", True, "2025-09-30T19:30:52Z"), vr("slack", REOPEN, f"slack:{SUBM_ROOT}", True, "2025-09-30T21:20:12Z")]),
 T("T_BACK", "superseding", ["gsheets", "slack"], [SHEET, BACK], [B135], "R3",
   "row 29 is Passed: ok on a main build",
   "Robert's later reply under his Sep 10 endless thread in #zombie-bugs says the home intro played again every time on Android Submission 135, a main build made after #1750",
   discovery_order="the sheet is read first; the reply sits under a root three weeks old and names no row",
   version_records=[vr("gsheets", SHEET, f"file:{SHEET}", True, "2025-09-30T19:30:52Z"), vr("slack", BACK, f"slack:{ENDLESS_ROOT}", True, T_BACK)]),
 T("T_ELSE", "completion_elsewhere", ["gsheets", "github", "linear"], [ELSE_PR, "ZOM-572", "ZOM-573", "ZOM-584"], [PR473], "R3",
   "rows 13, 14, 37 and 38 wait on a fix: the sheet names no fix and their tickets are Todo",
   "Oliver wrote on his own PR #473, merged on 30 Sep, that it also has those four fixes",
   discovery_order="the sheet's blank Fix cell and the Todo ticket are read first; #473 is named nowhere in the sheet"),
 T("T_BODY", "completion_elsewhere", ["gsheets", "github", "linear"], ["ZOM-568"], [PR472], "R3",
   "row 6 waits on a fix: the sheet names no fix and its ticket is Todo",
   "the description of Calvin's own merged PR #472 says it also holds the pre-level panel until the level-end coins have landed; it merged on 30 Sep and QA has not tried a build with it",
   discovery_order="the sheet's blank Fix cell and the Todo ticket are read first; the description needs the PR itself, not the list"),
 T("T_REOPEN_TICKET", "superseding", ["gsheets", "linear", "slack"], [SHEET, REOPEN2, "ZOM-585"], [B135], "R3",
   "row 17 is Passed: ok on a main build, and Vincent's own note on the ticket says ok",
   "Samuel's later note on ZOM-585 says it came back on Android Submission 135, a main build made after #1757, so under Arthur's note the pass no longer stands",
   discovery_order="the sheet is read first; the note needs that ticket's own comments",
   version_records=[vr("gsheets", SHEET, f"file:{SHEET}", True, "2025-09-30T19:30:52Z"), vr("linear", REOPEN2, "linear:ZOM-585", True, T_REOPEN2)]),
 T("T_BACK_TICKET", "superseding", ["gsheets", "linear", "slack"], [SHEET, BACK2, "ZOM-586"], [B135], "R3",
   "row 24 is Passed: nr on a main build, and Zombie Lane is Clear",
   "Owen's later note on ZOM-586 says the lane bar starts from zero again on Android Submission 135, so the row is open and no area is Clear",
   discovery_order="the sheet is read first; the note needs that ticket's own comments",
   version_records=[vr("gsheets", SHEET, f"file:{SHEET}", True, "2025-09-30T19:30:52Z"), vr("linear", BACK2, "linear:ZOM-586", True, T_BACK2)]),
 T("T_FILT", "exact_predicate", ["slack"], [FILT_DM], [], "R1",
   "the reports are the 38 sheet rows",
   "Brian's note brings in any bug somebody else saw in a build and told Calvin about in a DM since the 26th; Marcus told him about the pass icon glow on 30 Sep and no ticket holds it"),
 T("T_ALIAS_GIFT", "scope_alias", ["gsheets", "linear"], [ALIAS_GIFT], ["ZOM-556"], "R4",
   "row 11 has no ticket, so it needs a new sub-issue",
   "base ticket ZOM-556, the daily gift skip reset ticket, already has it; Vincent's note on that ticket ties his row to it"),
 T("T_ALIAS_STREAK", "scope_alias", ["gsheets", "linear"], [ALIAS_STREAK], ["ZOM-560"], "R4",
   "row 20 has no ticket, so it needs a new sub-issue",
   "base ticket ZOM-560, the abandoned pack freezer ticket, already has it; Vincent's note ties his row to it"),
 T("T_GATE", "effective_date", ["slack", "trello", "gmail"], [GATE_OLD, INV1, REV_UPDATE, REVCARD, INV2], [], "R5",
   "Collect & Win and Daily Gift are the areas for the review, on Friday",
   "Leonard's review card was changed on 30 Sep: Thursday, with Collect & Win and Level-end rewards; Daily Gift moves to next week",
   discovery_order="Brian's own line in the anchor chat is read first; the card is on Trello",
   version_records=[vr("gmail", INV1, f"gmail:{INV1}", True, T_INV1), vr("slack", GATE_OLD, f"slack:{GATE_OLD}", True, T_GATE_OLD), vr("trello", REV_UPDATE, f"trello:{REVCARD}", True, T_CARD_UPD)]),
 T("T_PARK", "superseding", ["slack"], [], [PARK_A, PARK_B], "R1",
   "the input blocker after every level is a report to carry",
   "Brian parked it the same day in his own chat with Calvin, and his note leaves it out",
   version_records=[vr("slack", PARK_A, f"slack:{PARK_A}", False, "2025-09-25T13:16:39Z"), vr("slack", PARK_B, f"slack:{PARK_B}", False, "2025-09-25T13:59:55Z")]),
 T("T_SHARE", "authority", ["gcal", "gmail", "gdrive"], [EVT, INV2], [], "R7",
   "the sheet is shared with Brian and Vincent, the two people in the conversation",
   "the hub says everyone on the review invite: Leonard, Brian, Arthur, Julia and Vincent"),
 T("T_FIELDS", "authority", ["linear", "slack"], [EPIC_NOTE], [JULIA], "R6",
   "a new sub-issue takes the priority and assignee the report suggests",
   "Brian's note, citing Julia's point about Calvin's tickets, wants no priority and no assignee on the new ones"),
 T("T_STATE", "stale_summary", ["linear", "gsheets"], ["ZOM-571", "ZOM-572", "ZOM-581", "ZOM-574", "ZOM-573", "ZOM-584", "ZOM-568", "ZOM-585"], [], "R4",
   "a ticket's own state is where the report stands",
   "the state follows the status worked out from the records: ZOM-571, ZOM-574 and ZOM-581 go back to Todo, ZOM-585 goes back to Todo, and ZOM-568, ZOM-572, ZOM-573 and ZOM-584 go to In Validation"),
 T("D_DDRULE", "distractor", ["gdocs"], [DDDOC], [], "R3", "a pass on the dev's branch build is enough", "that doc is about DD hotfixes", distractor_type="other_title"),
 T("D_QMCARD", "distractor", ["trello"], [], ["68c453cd0ff184d95550bc58"], "R2", "Leonard ticked the Queue Manager roadmap card on 30 Sep, so the work is done", "the card marks the feature as merged; report statuses come from the sheet and the records", distractor_type="stale_summary"),
 T("D_SKIP", "distractor", ["slack"], [], [f"{BUGS}/1758903616.346579"], "R1", "the tutorial skip exceptions are reports to carry", "Brian's note leaves Oliver's skip work out, and a channel post is not something told to Calvin in a DM", distractor_type="scope_adjacent"),
 T("D_ICONVFX", "distractor", ["slack"], [], [f"{VDM}/1758721951.996909"], "R1", "Vincent's chat remark about the pass icon VFX is another report", "for Vincent the sheet is the list", distractor_type="scope_adjacent"),
 T("D_CANVAS", "distractor", ["slack"], [], ["CF4EDAF93359/1759236624.010909"], "R1", "items on Vincent's Bug Checklist canvas are more reports", "Brian's note leaves both canvases as they are", distractor_type="scope_adjacent"),
 T("D_COINDM", "distractor", ["slack"], [], [f"{BDM}/1758808900.412489"], "R1", "Brian's own line about the coin animation is a second report", "it is dated the 25th, before Vincent's pass, and it is row 5 already", distractor_type="already_done"),
 T("D_432", "distractor", ["linear"], [], ["ZOM-432"], "R4", "ZOM-432 is the daily gift ticket for row 11", "ZOM-432 is about the gift artwork frame; ZOM-556 carries Vincent's tie", distractor_type="near_duplicate_record"),
 T("D_OLDINVITE", "distractor", ["gmail"], [INV1], [], "R5", "the first invitation's areas still stand", "the card was changed on 30 Sep and the updated invitation says so", distractor_type="withdrawn_ask"),
 T("D_OLDBUILD", "distractor", ["slack"], [OLDER], [B2006, B1745], "R3", "Robert saw the arena button bug after Vincent's nr, so row 27 is open again", "he saw it on Android #2006, built 40 minutes before iOS Internal #1745, and Arthur's note reopens a pass only on a build made after the one it passed on", distractor_type="boundary_case"),
 T("D_DDQUEUE", "distractor", ["linear"], [], ["ENG-2069"], "R1", "the DD queue manager tickets belong under the epic", "they are Domino Delights tickets on another team", distractor_type="keyword_collision"),
]
led = {}
for l in open(os.path.join(WF, "..", "..", "support", "hardness_ledger", "ledger.jsonl")):
    try: r = json.loads(l)
    except Exception: continue
    if str(r.get("model", "")).startswith("claude-opus-5-5") and r.get("family"): led.setdefault(r["family"], []).append(r.get("id"))
PRI = {"done_gap": (3.0, 3.0), "superseding": (1.0, 5.0), "completion_elsewhere": (1.0, 4.0), "scope_alias": (1.0, 4.0), "authority": (1.0, 4.0), "exact_predicate": (2.0, 4.0)}
def rule(i, m, fam, why, nodes, req, nat, dec, ctrl, over, src, sig):
    d = dict(id=i, mechanism=m, prior_family=fam, prior_family_reason=why, nodes=nodes, requirement=req, natural_reading=nat, decides=dec, controls=ctrl, over_application=over, source=src, signature=sig)
    if fam in PRI: d["prior"] = {"alpha": PRI[fam][0], "beta": PRI[fam][1], "record_ids": led.get(fam, [])[:10]}
    return d
port = [
 rule("BRANCH", "A24", "done_gap", "same mechanism: a done source (sheet ok, chat ok) with the missing piece in another place (the build's branch in #builds)", ["T_BRANCH"], "R3", "the sheet's ok is a pass", ["B1", "B2", "B3", "B4", "B5", "V1", "V2"], ["row 5", "row 31", "row 33"], "branch_over: un-passes a row whose ok was on a main build", "builds-channel", "main branch"),
 rule("INLINE", "A24", "done_gap", "same mechanism: a merged PR is the done source and the missing piece sits in an inline review comment", ["T_INLINE", "T_INLINE_PACK"], "R3", "a merged PR named in the sheet has the fix", ["I1", "I2", "I3", "I4", "I5", "I6", "I7", "V2", "V3"], ["row 18"], "inline_over: drops the PR from a row no reviewer excepted", "github-inline", "That one isn't in this diff"),
 rule("REOPEN", "A11", "superseding", "same mechanism: a dated correction in a thread reply under an older root, outside the window a reader pages", ["T_REOPEN", "T_REOPEN_TICKET"], "R3", "nr on a main build is a pass", ["R1", "R2", "R3", "R4", "R5", "R6", "V1", "V3", "V4"], ["row 7", "row 27"], "reopen_over: reopens another nr row", "unrelated-thread-reply", "on top of the gift again"),
 rule("BACK", "A11", "superseding", "same mechanism, other author: a reply under a three-week-old root that names no row", ["T_BACK", "T_BACK_TICKET"], "R3", "ok on a main build is a pass", ["K1B", "K2B", "K3B", "K4B", "K5B", "K9", "V1", "V3", "V5"], ["row 23", "row 22"], "back_over: reopens another ok row", "old-thread-reply", "home intro animation played again"),
 rule("ELSE", "A25", "completion_elsewhere", "same mechanism: an item that looks open while a record elsewhere shows the work done", ["T_ELSE", "T_BODY"], "R3", "a blank Fix cell means no fix", ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E9", "V2", "V3"], ["row 19", "row 30"], "else_over: marks a row merged that no dev named", "pr-comment", "For the flow list"),
 rule("FILT", "A17", "exact_predicate", "same mechanism: an in-scope item outside the obvious list, brought in by the scope sentence", ["T_FILT"], "R1", "the sheet is the whole list", ["F1", "F2", "F3", "V3", "V7"], ["the 38 sheet rows"], "filt_over: adds a chat line that is not a bug seen in a build", "artist-chat", "icon glow"),
 rule("ALIAS", "A7", "scope_alias", "same mechanism: a row and an existing ticket named differently, tied by a dated note", ["T_ALIAS_GIFT", "T_ALIAS_STREAK"], "R4", "a blank Ticket cell means a new sub-issue", ["A1", "A2", "A3"], ["row 1", "row 38"], "alias_over: reuses a ticket for a row with none", "ticket-note", "Same thing"),
 rule("GATE", "A12", "authority", "same mechanism: the governing source sits in a rarely opened service and an older version is met first", ["T_GATE"], "R5", "Brian's line in the chat names the review's areas", ["G1", "G2", "V4"], ["row 15", "row 21"], "gate_over: none", "trello-card", "Level-end rewards"),
]
channels = [dict(id=f"CH-{p['id']}", kind="scale", rule=p["id"], degrade="ch_miss", latent="member", family=p["prior_family"], source=p["source"], members=list(p["nodes"]), description=p["natural_reading"]) for p in port]
reqs = {
 "R1": "population: the rows of Vincent's flow pass sheet plus any bug somebody else saw in a build and told Calvin about in a DM since 26 Sep about the home screen after a level",
 "R2": "Status of each area: Clear when all its reports are Passed, otherwise Open, with its count of Open reports",
 "R3": "Status of each report: Passed, Waiting on QA or Waiting on a fix",
 "R4": "Ticket for each report: the ticket that already holds it is moved under the area child with a note and a matching state, otherwise a new sub-issue",
 "R5": "Review list for each report: not Passed and in an area Leonard's review card lists",
 "R6": "new sub-issue fields: ZOM team, parent the area child, report as title, state by status, no priority, no assignee",
 "R7": "stock-take sheet with tabs Reports and Areas in the ZM queue manager folder, shared with everyone on the review invite",
 "R8": "reply to Brian in the DM with the counts: passed, waiting on QA, waiting on a fix, clear areas, on the review list",
 "R9": "one slide with the five numbers added to Calvin's queue manager deck",
}
services = {
 "slack": {"role": "hub, QA chat, build log, corrections", "weight_reason": "the ask, the branch each build came from, two later corrections and one report live here"},
 "linear": {"role": "epic, tickets, destination", "weight_reason": "Brian's note, the ticket ties and every structural write are here"},
 "github": {"role": "PR truth", "weight_reason": "merged PRs, Arthur's inline reviews and Oliver's comment decide whether a fix is merged"},
 "gsheets": {"role": "Vincent's flow pass sheet and the stock-take sheet", "weight_reason": "the report list is read here and the deliverable is written here"},
 "gdocs": {"role": "Arthur's rule and the sheet legend", "weight_reason": "which builds count for a pass, and what ok, nr and ok, chat mean"},
 "gdrive": {"role": "destination folder and sharing", "weight_reason": "the sheet goes in Calvin's folder and is shared"},
 "gmail": {"role": "review invitations", "weight_reason": "the invitation names the review, points at Leonard's card and carries the older list of areas the card replaced"},
 "gcal": {"role": "review event", "weight_reason": "the attendee list the sheet is shared with"},
 "trello": {"role": "Leonard's review card", "weight_reason": "the areas the review covers, which decide the review list"},
 "gslides": {"role": "Calvin's queue manager deck", "weight_reason": "the slide with the five numbers is written here"},
}
cohort = {"definition": "38 rows of Vincent's flow pass sheet, 1 report raised outside it and the 10 areas of Brian's note: 49 records", "definition_source": [HUB, EPIC_NOTE], "key": "report or area", "size": 49, "evidence_surfaces": [
 {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1.0, "records": 22, "seeded": True, "seeded_ids": [ALIAS_GIFT, ALIAS_STREAK, REOPEN2, BACK2], "requirement": "R4", "decides": "Ticket for each report",
  "why_no_bulk": "linear_list_issues returns no comments; the note that ties a row to a ticket needs that ticket's own linear_list_comments",
  "short_circuit": "a row with a blank Ticket cell is only settled by reading candidate tickets; titles use other words, so one search cannot sweep the ties"},
 {"service": "github", "tool": "github_get_pull_request, github_get_pull_request_reviews, github_get_pull_request_comments and github_get_issue_comments", "per_record_calls": 4.0, "records": 4, "seeded": True, "seeded_ids": [INLINE, INLINE2, ELSE_PR], "requirement": "R3", "decides": "Status of each report",
  "why_no_bulk": "github_search_pull_requests returns neither reviews, inline comments nor conversation comments, and in:comments misses inline ones",
  "short_circuit": "merged state alone does not say whether a fix is in a PR; only its own review and comment surfaces do, and each of the four PRs (#465, #472, #473, #475) needs them"},
 {"service": "slack", "tool": "slack_conversations_history or slack_search_public_and_private on #builds", "per_record_calls": 1.0, "records": 12, "seeded": False, "requirement": "R3", "decides": "Status of each report",
  "why_no_bulk": "the sheet names builds by number only; the branch is in each build's own post, and 146 match3d posts in the last week of September cannot be read in one call",
  "short_circuit": "a re-test only counts on a build of the main branch, so each of the 12 distinct builds in the Re-test column and the chat needs its branch"},
 {"service": "gsheets", "tool": "gsheets_values_get", "per_record_calls": 0.1, "records": 38, "seeded": True, "seeded_ids": [SHEET], "requirement": "R1", "decides": "population",
  "why_no_bulk": "one range read returns the rows; counted at a tenth because it is a bulk read", "short_circuit": "the list itself; nothing else holds the rows"},
]}
budget = [
 ("discovery", "slack", 5, "Brian's DM, the QA chat, channel lookups"), ("discovery", "linear", 6, "the epic, its comments, states, labels, team, users"), ("discovery", "gdrive", 3, "the folder, the pass sheet's and the deck's location"),
 ("discovery", "gsheets", 3, "the pass sheet: metadata and two range reads"), ("discovery", "gdocs", 4, "the legend and Arthur's rule: search and read"), ("rules", "trello", 3, "Leonard's review card: search, card, its actions"),
 ("rules", "gmail", 3, "the review invitation: search and the two messages"), ("rules", "gcal", 2, "the review event and its attendees"), ("rules", "slack", 2, "Julia's note"), ("discovery", "gslides", 2, "Calvin's deck: find and read"),
 ("enumeration", "slack", 15, "what was told to Calvin in a DM since the 26th: each recent 1:1 chat; later words on passed rows in #zombie-bugs threads and #zombie-match3d"), ("enumeration", "gmail", 3, "mail to Calvin since the 26th"),
 ("enumeration", "linear", 6, "ZOM tickets since the 20th and candidate tickets for rows with no key"), ("enumeration", "github", 4, "match3d PRs merged since the 24th"),
 ("per-record", "linear", 22, "comments on the 22 tickets that hold a report"), ("per-record", "github", 16, "body, reviews, inline and conversation comments of the four PRs the rows rest on"), ("per-record", "slack", 12, "the #builds post of each distinct build in the Re-test column and the chat"),
 ("per-record", "linear", 71, "10 area children, 17 new sub-issues, 22 tickets moved under a child and 22 notes: each a distinct target with no batch form"),
 ("writes", "gsheets", 4, "stock-take sheet: create and fill two tabs"), ("writes", "gdrive", 6, "move into the folder and share with five people"), ("writes", "gslides", 2, "add the slide and its text"), ("writes", "linear", 1, "the epic's own state or text"), ("writes", "slack", 1, "reply to Brian"),
 ("read-back", "linear", 3, "confirm the tree"), ("read-back", "gsheets", 2, "confirm the sheet"),
]
manifest = {
 "_note": "DRAFT manifest (scenario stage, design-3). Seeded ids are planned (plan/build_scenario.py, plan/seed_text.json, plan/reports.py); /create-injection writes the final manifest.",
 "persona": "calvin_price", "assignment_context": {k: ctx.get(k) for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc")} | {"difficulty_mode": ctx.get("difficulty_mode")},
 "horizon": "Long Horizon", "effective_profile": "extreme",
 "author_targets": {"calls_per_run": "over 130 in every run", "average": "strictly under 60 %", "largest_pattern": "under 50 % of failing runs", "design_target": "E[avg] <= 52 %", "source": "requester, 2026-11-10"},
 "volume_exception": {"reason": "49 cohort records and about 200 honest calls; reaching 500 would need padding, which fails on its own. The per-record floor counts read surfaces only (20 ticket comment reads, 16 PR reads, 12 build lookups), so it is 40, not the 120 quoted in the analysis, which counted writes",
  "requester_confirmation": "requester, Claude Code chat 2026-11-10: 'i want over 130 tool calls in each runs ... you can choose from your self which option is best fit for my requirements in this task' (choice delegated; recorded in 00_Pre_Scenario_Analysis.md section 11, item 2)", "call_budget_floor": 180, "per_record_floor": 40},
 "requirements": reqs, "services": services,
 "anchors": [{"id": "AN1", "prompt_reference": "Brian's message from yesterday", "service": "slack", "locator": HUB, "requirement_ids": ["R1", "R7", "R8", "R9"]},
             {"id": "AN2", "prompt_reference": "the Queue Manager ticket", "service": "linear", "locator": "ZOM-543", "requirement_ids": ["R2", "R4"]}],
 "ask_fragments": frags,
 "authorities": [
  {"id": "H1", "name": "Arthur's rule for QA passes", "home_service": "gdocs", "decoy_service": "gdocs", "governs": ["R3"], "findable_query": "QA passes", "seeded_ids": [RULEDOC], "base_pointers": [], "decoy_seeded_ids": [DDDOC], "decoy_base_pointers": [],
   "decoy_scope": {"dimension": "game", "decoy": "Domino Delights", "task": "ZM (match3d)"}},
  {"id": "H2", "name": "Leonard's review card", "home_service": "trello", "decoy_service": "slack", "governs": ["R5"], "findable_query": "flow review", "seeded_ids": [REVCARD, REV_UPDATE], "base_pointers": [], "decoy_seeded_ids": [GATE_OLD, INV1], "decoy_base_pointers": []},
 ],
 "cohort": cohort,
 "chains": [
  {"id": "C1", "root_cause": "A24", "ends_in": "R3", "hops": [{"service": "gsheets", "record": SHEET, "finding": "row 1: fix #465, re-test ok, chat"}, {"service": "slack", "record": C_TESTED, "finding": "Calvin: #1718 already tested"}, {"service": "slack", "record": V_OK, "finding": "Vincent: looks ok"}, {"service": "slack", "record": B1718, "finding": "#1718 was built from the QueueManager branch"}, {"service": "gdocs", "record": RULEDOC, "finding": "only builds of the main branch count"}]},
  {"id": "C2", "root_cause": "A11", "ends_in": "R3", "hops": [{"service": "gsheets", "record": SHEET, "finding": "row 9: nr on #1745"}, {"service": "slack", "record": B135, "finding": "Android Submission #135 built from main on 30 Sep"}, {"service": "slack", "record": REOPEN, "finding": "Vincent: it came up again on Submission 135"}]},
  {"id": "C3", "root_cause": "A25", "ends_in": "R3", "hops": [{"service": "gsheets", "record": SHEET, "finding": "rows 13 and 38: no fix named"}, {"service": "github", "record": PR473, "finding": "Addressables/sp, merged 30 Sep 15:41 UTC"}, {"service": "github", "record": ELSE_PR, "finding": "Oliver: it also has both fixes"}]},
  {"id": "C4", "root_cause": "A7", "ends_in": "R4", "hops": [{"service": "gsheets", "record": SHEET, "finding": "row 11: no ticket"}, {"service": "linear", "record": "ZOM-556", "finding": "open base ticket under other words"}, {"service": "linear", "record": ALIAS_GIFT, "finding": "Vincent ties his row to it"}]},
  {"id": "C5", "root_cause": "A12", "ends_in": "R5", "hops": [{"service": "slack", "record": GATE_OLD, "finding": "Brian: Collect & Win and Daily Gift"}, {"service": "gmail", "record": INV1, "finding": "first invitation: the same two areas, Friday"}, {"service": "trello", "record": REV_UPDATE, "finding": "changed: Collect & Win and Level-end rewards, Thursday"}]},
  {"id": "C6", "root_cause": "A17", "ends_in": "R1", "hops": [{"service": "linear", "record": EPIC_NOTE, "finding": "any bug told to Calvin in a DM since the 26th"}, {"service": "slack", "record": FILT_DM, "finding": "Marcus's icon glow report"}, {"service": "gsheets", "record": SHEET, "finding": "no row has it"}]},
 ],
 "traps": traps, "mechanism_portfolio": port, "channels": channels,
 "call_budget": [{"phase": a, "service": b, "calls": c, "reason": d} for a, b, c, d in budget],
 "writes": [
  {"service": "linear", "tool": "linear_create_issue", "count": 27, "depends_on": ["T_FILT", "T_ALIAS_GIFT", "T_ALIAS_STREAK", "T_ELSE", "T_BRANCH", "T_BACK"], "requirements": ["R2", "R4", "R6"]},
  {"service": "linear", "tool": "linear_update_issue", "count": 22, "depends_on": ["T_INLINE", "T_INLINE_PACK", "T_ELSE", "T_ALIAS_GIFT"], "requirements": ["R4"]},
  {"service": "linear", "tool": "linear_create_comment", "count": 22, "depends_on": ["T_INLINE", "T_ELSE", "T_ALIAS_GIFT", "T_ALIAS_STREAK"], "requirements": ["R4"]},
  {"service": "gsheets", "tool": "gsheets_values_update", "count": 3, "depends_on": ["T_BRANCH", "T_GATE", "T_FILT"], "requirements": ["R7"]},
  {"service": "gdrive", "tool": "gdrive_share_file", "count": 5, "depends_on": ["T_SHARE", "K7"], "requirements": ["R7"]},
  {"service": "gslides", "tool": "gslides_batch_update", "count": 2, "depends_on": ["T_BRANCH", "T_GATE", "T_ELSE"], "requirements": ["R9"]},
  {"service": "slack", "tool": "slack_send_message", "count": 1, "depends_on": ["T_BRANCH", "T_GATE", "T_ELSE"], "requirements": ["R8"]},
 ],
 "hazard_acknowledgements": [],
 "denied_probes": [], "gradable_surface": "01_Gradable_Surface.json",
}
TXT = "[ -~\\u00a0-\\uffff]"
def S(i, title, w, kind, reason, cls, sel, mech=None, role="core", **kw):
    d = dict(id=i, title=title, weight=w, work_kind=kind, work_reason=reason, **{"class": cls}, selector=sel, role=role, mechanisms=mech or [])
    d.update(kw); return d
MS, LK, IN, CMP = "multi_source_reconciliation", "lookup", "interpretation", "comparison"
row = lambda word, out: f"({word}){TXT}{{0,240}}{out}"
KEY = {r[0]: r[2] for r in RP.R + RP.OUTSIDE}
fld = lambda n, col: ["field", KEY[n], col]
B = lambda n: "\\b" + str(n) + "\\b"
slots = [
 S("V1", "Passed count in the reply", 5, MS, "statuses joined across the sheet, #builds, Arthur's rule and two later posts", "write_content", ["text", "reply", B(10)], ["BRANCH", "REOPEN", "BACK"]),
 S("V2", "Waiting on QA count in the reply", 5, MS, "merged fixes joined with passes across GitHub, Slack and the sheet", "write_content", ["text", "reply", B(9)], ["BRANCH", "ELSE", "INLINE"]),
 S("V3", "Waiting on a fix count in the reply", 5, MS, "what no merged PR has, across the sheet, chats and GitHub", "write_content", ["text", "reply", B(20)], ["REOPEN", "BACK", "INLINE", "ELSE", "FILT"], "volume", volume_for=["plain"]),
 S("V4", "Review list count in the reply", 5, MS, "statuses joined with the areas on Leonard's card", "write_content", ["text", "reply", B(7)], ["GATE", "REOPEN"], fact_id="review-list-count"),
 S("V5", "Clear areas count in the reply", 5, MS, "areas rolled up from report statuses (band raised to the platform /rubric round-3 weight: the value joins records across services)", "write_content", ["text", "reply", "(?i)\\b(0|zero|none|no)\\b" + TXT + "{0,30}(area|clear)|(area|clear)" + TXT + "{0,30}\\b(0|zero|none)\\b"], ["BACK"]),
 S("V7", "Season Pass area shows 5 open reports", 5, MS, "area count joined across the pass sheet and a report that only came in a 1:1 chat", "write_content", ["text", "sheet", row("Season Pass", B(5))], ["FILT"]),
 S("B1", "Back to back tutorials row is Waiting on QA", 5, MS, "sheet ok and chat ok against the build's branch and Arthur's rule", "direct", fld(1, "Status"), ["BRANCH"]),
 S("B2", "Card upgrade tutorial row is Waiting on QA", 5, MS, "same join on a second row", "direct", fld(2, "Status"), ["BRANCH"]),
 S("B3", "Boss arena tutorial row is Waiting on QA", 5, MS, "same join on a third row", "direct", fld(25, "Status"), ["BRANCH"]),
 S("B4", "Back to back tutorials sub-issue is filed In Validation", 3, IN, "state follows the status", "write_content", ["text", "issues", row("[Bb]ack to back tutorials", "In Validation")], ["BRANCH"]),
 S("B5", "Boss Arena area is Open", 5, MS, "area rolled up from a status that depends on the build's branch", "write_content", ["text", "sheet", row("Boss Arena", "Open")], ["BRANCH"]),
 S("R1", "Pass popup over the gift row is Waiting on a fix", 5, MS, "nr on a main build against a later reply in another thread", "direct", fld(9, "Status"), ["REOPEN"]),
 S("R2", "Its sub-issue is filed Todo", 3, IN, "state follows the status", "write_content", ["text", "issues", row("on top of the daily gift", "Todo")], ["REOPEN"]),
 S("R3", "Its Why names Submission 135", 5, MS, "the build it came back on, read from the reply (band raised to the platform /rubric round-3 weight: the value joins records across services)", "write_content", ["reason_matches", KEY[9], "135"], ["REOPEN"]),
 S("K1B", "Home intro replay row is Waiting on a fix", 5, MS, "ok on a main build against a later post in another channel", "direct", fld(29, "Status"), ["BACK"]),
 S("K2B", "Its sub-issue is filed Todo", 3, IN, "state follows the status", "write_content", ["text", "issues", row("replays the home intro", "Todo")], ["BACK"]),
 S("R4", "Event bar wait row is Waiting on a fix", 5, MS, "ok on a main build against a later note on its ticket", "direct", fld(17, "Status"), ["REOPEN"]),
 S("R5", "ZOM-585 goes back to Todo", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-585", "Todo")], ["REOPEN"]),
 S("R6", "Event bar wait row is on the review list", 5, MS, "a reopened pass joined with the areas on the changed card", "direct", fld(17, "Review list"), ["REOPEN"]),
 S("K4B", "Lane progress bar row is Waiting on a fix", 5, MS, "nr on a main build against a later note on its ticket", "direct", fld(24, "Status"), ["BACK"]),
 S("K5B", "Zombie Lane child is not Done", 5, MS, "child state follows the area (band raised to the platform /rubric round-3 weight: the value joins records across services)", "write_content", ["text", "issues", row("Zombie Lane", "Todo")], ["BACK"]),
 S("K3B", "Endless Mode area shows 4 open reports", 5, MS, "area count joined across the pass sheet and a later post", "write_content", ["text", "sheet", row("Endless Mode", B(4))], ["BACK"]),
 S("I1", "Pass icon restart row is Waiting on a fix", 5, MS, "merged PR in the sheet against the reviewer's inline comment", "direct", fld(12, "Status"), ["INLINE"]),
 S("I2", "ZOM-571 goes back to Todo", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-571", "Todo")], ["INLINE"]),
 S("I3", "Its Why says #472 does not have it", 5, MS, "reads the exception from the review (band raised to the platform /rubric round-3 weight: the value joins records across services)", "write_content", ["reason_matches", KEY[12], "472"], ["INLINE"]),
 S("I4", "Pack sound row is Waiting on a fix", 5, MS, "merged PR and In Validation ticket against the reviewer's inline comment", "direct", fld(32, "Status"), ["INLINE"]),
 S("I5", "ZOM-581 goes back to Todo", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-581", "Todo")], ["INLINE"]),
 S("I6", "Event bar start row is Waiting on a fix", 5, MS, "merged PR and In Validation ticket against the reviewer's inline comment", "direct", fld(15, "Status"), ["INLINE"]),
 S("I7", "ZOM-574 goes back to Todo", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-574", "Todo")], ["INLINE"]),
 S("E5", "Pass claim animation row is Waiting on QA", 5, MS, "blank Fix cell and Todo ticket against the dev's comment on a merged PR", "direct", fld(14, "Status"), ["ELSE"]),
 S("E6", "Freezer popup row is Waiting on QA", 5, MS, "same join on a fourth row", "direct", fld(37, "Status"), ["ELSE"]),
 S("E7", "Pre-level panel row is Waiting on QA", 5, MS, "blank Fix cell and Todo ticket against the description of a merged PR", "direct", fld(6, "Status"), ["ELSE"]),
 S("E9", "ZOM-568 goes to In Validation", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-568", "In Validation")], ["ELSE"]),
 S("E1", "Pass start popup row is Waiting on QA", 5, MS, "blank Fix cell and Todo ticket against the dev's comment on a merged PR", "direct", fld(13, "Status"), ["ELSE"]),
 S("E2", "Pass bar row is Waiting on QA", 5, MS, "same join on a second row", "direct", fld(38, "Status"), ["ELSE"]),
 S("E3", "Its Why names #473", 5, MS, "the PR read from GitHub (band raised to the platform /rubric round-3 weight: the value joins records across services)", "write_content", ["reason_matches", KEY[13], "473"], ["ELSE"]),
 S("E4", "ZOM-572 goes to In Validation", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-572", "In Validation")], ["ELSE"]),
 S("F1", "Marcus's icon glow report is in the sheet", 5, MS, "scope sentence joined with a 1:1 chat", "direct", fld(39, "Status"), ["FILT"]),
 S("F2", "A sub-issue carries it", 5, MS, "write follows the report (band raised to the platform /rubric round-3 weight: the value joins records across services)", "write_content", ["text", "issues", "[Ii]con glow"], ["FILT"]),
 S("F3", "Its area is Season Pass", 5, MS, "area read from the report (band raised to the platform /rubric round-3 weight: the value joins records across services)", "direct", fld(39, "Area"), ["FILT"]),
 S("A1", "Day counter row uses ZOM-556", 5, MS, "row tied to a base ticket under other words by a note", "direct", fld(11, "Ticket"), ["ALIAS"]),
 S("A2", "Freezer row uses ZOM-560", 5, MS, "row tied to a base ticket under other words by a note", "direct", fld(20, "Ticket"), ["ALIAS"]),
 S("A3", "Note on ZOM-556", 3, IN, "write on the reused ticket", "write_content", ["text", "comments", row("ZOM-556", "(fix|Waiting|Todo)")], ["ALIAS"]),
 S("G1", "Gift calendar row is not on the review list", 5, MS, "status joined with the areas on the changed card", "direct", fld(10, "Review list"), ["GATE"]),
 S("G2", "Coins over the pre-level panel row is on the review list", 5, MS, "status joined with the areas on the changed card", "direct", fld(6, "Review list"), ["GATE"]),
 S("K1", "Plain sample: endless banner again", 3, IN, "blank cells read from the sheet (band raised to the platform /rubric round-3 weight: the status is read through the note's rule, not copied)", "direct", fld(16, "Status"), role="sample", group="plain"),
 S("K2", "Plain sample: streak counter", 3, IN, "blank cells read from the sheet (band raised to the platform /rubric round-3 weight: the status is read through the note's rule, not copied)", "direct", fld(21, "Status"), role="sample", group="plain"),
 S("K3", "Plain sample: endless chest", 3, IN, "blank cells read from the sheet (band raised to the platform /rubric round-3 weight: the status is read through the note's rule, not copied)", "direct", fld(30, "Status"), role="sample", group="plain"),
 S("K4", "Pack count row is Waiting on a fix", 5, MS, "a merged PR against a re-test on a build made after the merge (band raised to the platform /rubric round-3 weight: the value joins records across services)", "direct", fld(34, "Status")),
 S("K14", "Arena button row stays Passed", 5, MS, "a later sighting on a build made before the one it passed on (band raised to the platform /rubric round-3 weight: the value joins records across services)", "direct", fld(27, "Status")),
 S("K5", "Plain sample: banner over the gift", 3, IN, "blank cells read from the sheet (band raised to the platform /rubric round-3 weight: the status is read through the note's rule, not copied)", "direct", fld(28, "Status"), role="sample", group="plain"),
 S("K6", "Passed on a main build: coin animation", 5, MS, "ok checked against the build's branch (band raised to the platform /rubric round-3 weight: the value joins records across services)", "direct", fld(5, "Status")),
 S("K7", "Passed on a main build: last pack cards", 5, MS, "ok checked against the build's branch and the merge time (band raised to the platform /rubric round-3 weight: the value joins records across services)", "direct", fld(33, "Status")),
 S("K8", "Waiting on QA: event panel over rewards", 5, MS, "a merged PR against a re-test on a build made before the merge (band raised to the platform /rubric round-3 weight: the value joins records across services)", "direct", fld(18, "Status")),
 S("K9", "Zombie Lane area is Open", 5, MS, "area rolled up from a pass that no longer stands (band raised to the platform /rubric round-3 weight: the value joins records across services)", "write_content", ["text", "sheet", row("Zombie Lane", "Open")], ["BACK"]),
 S("K10", "Area children exist under the epic", 1, LK, "names from Brian's note", "write_content", ["text", "issues", "Endless Mode"]),
 S("K11", "A passed row with no ticket gets a Done sub-issue", 5, MS, "state from Brian's note (band raised to the platform /rubric round-3 weight: the value joins records across services)", "write_content", ["text", "issues", row("[Cc]oin animation", "Done")]),
 S("K12", "A ticket moved under its child: ZOM-568", 1, LK, "parent set from the row's area", "write_content", ["text", "updates", "ZOM-568"]),
 S("K13", "Ticket key in a sheet row", 1, LK, "key copied from the pass sheet", "direct", fld(4, "Ticket")),
 S("D1", "Sheet in the folder", 1, LK, "destination named in the DM", "delivery", ["delivery", "register_parent", FOLDER]),
 S("D2", "Sheet shared with the review's people", 3, CMP, "attendees read from the review invite", "delivery", ["delivery", "share_reader", "leonard.hayes@harmonygames.co"]),
 S("D3", "Reply in Brian's DM", 1, LK, "destination named in the prompt", "delivery", ["link", "reply"]),
 S("D4", "Slide carries the review list count", 1, LK, "number copied onto the slide", "write_content", ["text", "slide", B(7)], fact_id="review-list-count"),
]
YES = {"Passed": ["Passed", "Pass", "Done"], "Waiting on QA": ["Waiting on QA", "Waits on QA", "In Validation", "QA"], "Waiting on a fix": ["Waiting on a fix", "Waits on a fix", "Todo", "Fix"]}
# incorporating spans are the prompt's own wording (design_readiness checks them against 04_Prompt.txt from the prompt stage on)
SPAN_REPLY = "message him in our DM with the numbers he wants back"
SPAN_SHEET = "the stock-take sheet in my ZM queue manager folder"
SPAN_LINE = "the children and report lines in Linear"
SPAN_SLIDE = "a slide with the numbers in my queue manager deck"
SPAN_SHARE = "shared with everyone on the review invite"
_PROMPT = open(os.path.join(os.path.dirname(WF), "04_Prompt.txt")).read()
for s_ in slots:
    sel = s_["selector"]
    s_["incorporating_span"] = (SPAN_REPLY if sel[:2] == ["text", "reply"] or sel == ["link", "reply"] else SPAN_SLIDE if sel[:2] == ["text", "slide"] else SPAN_SHARE if s_["id"] == "D2"
                                else SPAN_LINE if sel[0] == "text" and sel[1] in ("issues", "comments", "updates") else SPAN_SHEET)
    assert s_["incorporating_span"] in _PROMPT, s_["id"]
surface = {"kind": "GRADABLE_SURFACE", "version": 1, "task": "calvin_qm_epic", "revision": "design-4", "classes": ["Passed", "Waiting on QA", "Waiting on a fix"], "truth_fields": {"class": "Status", "groups": "groups"},
 "deliverables": {
  "sheet": {"kind": "table", "name_regex": "(?i).*(stock|queue|report|epic).*", "key_column": "Report", "key_regex": "(?:Report 1|Report 2|[A-Za-z][A-Za-z0-9 .,'()&/-]*)", "columns": ["Report", "Area", "Status", "Ticket", "Review list", "Why"], "class_column": "Status", "reason_column": "Why",
            "comparators": {"Status": "yes_no", "Ticket": "issue_key", "Review list": "norm", "Area": "norm"}, "yes_no": YES},
  "reply": {"kind": "json_text", "tool": "slack_send_message"}, "issues": {"kind": "json_text", "tool": "linear_create_issue"}, "comments": {"kind": "json_text", "tool": "linear_create_comment"}, "updates": {"kind": "json_text", "tool": "linear_update_issue"},
  "slide": {"kind": "json_text", "tool": "gslides_batch_update"}},
 "slots": slots}
json.dump({k: {"service": v[0], "id": v[1], "author": v[2], "at": v[3], "text": v[4]} for k, v in SEED.items()}, open(os.path.join(HERE, "seed_text.json"), "w"), indent=1)
json.dump({"areas": AREAS, "gate_areas": RP.GATE_AREAS, "old_gate_areas": RP.OLD_GATE_AREAS, "main_builds": RP.MAIN_BUILDS, "branch_builds": RP.BRANCH_BUILDS, "seeded_state": RP.SEEDED_STATE, "base_tickets": RP.BASE_TICKETS, "rows": RP.truth()}, open(os.path.join(HERE, "truth_sketch.json"), "w"), indent=1)
json.dump(manifest, open(os.path.join(WF, "01_Hardness_Manifest.draft.json"), "w"), indent=1)
json.dump(surface, open(os.path.join(WF, "01_Gradable_Surface.json"), "w"), indent=1)
tot = sum(s["weight"] for s in slots); fl = sum(s["weight"] for s in slots if s["mechanisms"])
import collections
c = collections.Counter()
for s in slots:
    for m in s["mechanisms"]: c[m] += s["weight"]
print("slots", len(slots), "weight", tot, "flippable", fl, round(fl / tot, 3), "budget", sum(b[2] for b in budget), "per-record reads", sum(s["per_record_calls"] * s["records"] for s in cohort["evidence_surfaces"]))
print({k: f"{v} ({v / tot:.0%})" for k, v in c.items()})
print("fragments", len(frags), "services", len({f['service'] for f in frags}), "containers", len({f['container'] for f in frags}), "traps", len(traps), "families", len({t['family'] for t in traps}))

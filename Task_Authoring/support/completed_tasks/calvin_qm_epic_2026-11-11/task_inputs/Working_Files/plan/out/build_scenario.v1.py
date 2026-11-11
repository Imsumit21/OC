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
BDM, VDM, ODM, MDM, JDM = "D0770ET6WBW", "D06UPGF5PQV", "D05S1S2H55M", "D05U73FNDDL", "D05HYDTG5TJ"
BUILDS, BUGS, PRS = "C05433XK267", "C08R27X0EAH", "C093LEZGF6J"
HUB = f"{BDM}/1759273805.214409"
GATE_OLD = f"{BDM}/1758899412.337219"
CLAIM = f"{VDM}/1759185612.507119"
REOPEN = f"{BUGS}/1759267212.418339"
ELSE_DM = f"{ODM}/1759249512.306229"
FILT_DM = f"{MDM}/1759257012.611349"
EPIC_NOTE = cid("epic-note-543")
ALIAS_GIFT, ALIAS_STREAK = cid("alias-573"), cid("alias-578")
SHEET, LEGEND, DECK, DDNOTES = fid("vincent-pass-sheet"), fid("vincent-legend"), fid("brian-weekly-deck"), fid("dd-pass-legend")
FOLDER = "d_" + h("calvin_qm:folder", 22)
MAIL = "calvin.price@harmonygames.co/1844612290417735201"
INV1 = "calvin.price@harmonygames.co/1844431875220913402"
INV2 = "calvin.price@harmonygames.co/1844792240663158803"
EVT = "evt_" + h("calvin_qm:review", 22)
CARD, RULE_ACT = "68c4a1d09b7e3f52a6c81d40", "68c4a3f25d1c8e60b3a97f12"        # Trello ids carry their time: 12 Sep 2025
DDCARD, DD_ACT = "686fd2a04c1e7b93d5a206e8", "686fd4c87a3b9e15c2d40f76"       # 10 Jul 2025
INLINE = "harmonygames-Games/match3d#472#rc_1"
INLINE2 = "harmonygames-Games/match3d#475#rc_1"
PR475 = "harmonygames-Games/match3d#475"
PR472, PR470, PR465 = "harmonygames-Games/match3d#472", "harmonygames-Games/match3d#470", "harmonygames-Games/match3d#465"
B1718, B135 = f"{BUILDS}/1758817549.151639", f"{BUILDS}/1759263189.219529"
V_OK, C_TESTED = f"{VDM}/1758820544.160399", f"{VDM}/1758817744.353289"
PARK_A, PARK_B = f"{VDM}/1758806199.381319", f"{BDM}/1758808795.588519"
JULIA = f"{JDM}/1756838837.147599"
SHADER_ROOT = f"{BUGS}/1759249488.495439"
AREAS = RP.AREAS
SEED = {
 "hub": ("slack", HUB, "Brian Foster", "2025-09-30T23:10:05Z", "Hello! Before the Collect&Win review I want the queue manager to be a real epic. Right now it is one ticket and everything else is in chats and in Vincent's pass sheet. I left a note on the ticket about how I want it. One child for each area, and every report gets its line under the right child. Please also put a stock-take sheet in your ZM queue manager folder and share it with me and Vincent. When it is done tell me here how many are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many hold the review."),
 "epic_note": ("linear", EPIC_NOTE, "Brian Foster", "2025-09-30T22:48:00Z", "How I want this epic.\n\nChildren: " + ", ".join(AREAS) + ". One child each, same team, no assignee.\n\nReports: every row of Vincent's pass sheet. His sheet is his whole list, so don't add things he only said in chat. Plus anything somebody else on the team raised since the queue manager went to main on the 24th about what shows on the home screen after a level, whoever it came from and wherever they wrote it. Oliver's tutorial skip work is his own thing, leave it out. The input blocker I already parked, leave it out too.\n\nStatus of a report, one of three. Passed: Vincent's ok or nr on a build that counts under Arthur's rule for QA passes, and it stays passed unless whoever raised it says later that it is back. Waiting on QA: not passed, but a merged PR covers it. Waiting on a fix: everything else, also when it came back after a pass.\n\nLine under the child: if a ticket already has the report, move that ticket under the child and leave a note with the status and why. If its state does not match, put Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix. If no ticket has it, make a sub-issue under the child with the report as the title and the state the same way. Vincent sometimes writes a row for something that already has a ticket under another name, use that ticket then. No priority and no assignee on the new ones, that is Julia's point about your tickets, I will set them.\n\nA child is Clear when all its reports are Passed, otherwise Open. Make the child Done when it is Clear and Todo when it is Open.\n\nHolds the review: a report that is not Passed, in an area the review invite lists.\n\nSheet: tab Reports with Report, Area, Status, Ticket, Holds review, Why. Tab Areas with Area, Status, Open reports."),
 "gate_old": ("slack", GATE_OLD, "Brian Foster", "2025-09-26T15:10:12Z", "For the C&W review on Friday what holds it is collect&win and daily gift, the rest can come after"),
 "sheet": ("gsheets", SHEET, "Vincent Parker", "2025-09-30T17:40:00Z", "ZM home screen flow - QA pass\n\nColumns: #, Area, What happens, Found on, Ticket, Fix, Re-test. 38 rows, in plan/reports.py.\n\nNote under the table: The codes are in my pass sheet legend doc. Raised by me unless the row says otherwise."),
 "legend": ("gdocs", LEGEND, "Vincent Parker", "2025-09-26T09:30:00Z", "How to read my pass sheets\n\nFound on: the build I first saw it on.\nTicket: the Linear key if I filed one.\nFix: the PR the dev told me it went into. Blank if nobody told me.\nRe-test: ok and a build means it is fine on that build. nr and a build means I could not make it happen on that build. again and a build means it still happens. ok, chat means I told the dev ok in our chat, the build is there. Blank means not re-tested yet."),
 "dd_legend": ("gdocs", DDNOTES, "Vincent Parker", "2025-03-11T10:00:00Z", "DD regression notes\n\nFor Domino Delights a tick in my regression list means it passed on the store build. Web builds are checked separately."),
 "rule_card": ("trello", CARD, "Arthur Blake", "2025-09-12T22:20:00Z", "ZM builds and QA passes"),
 "rule_comment": ("trello", RULE_ACT, "Arthur Blake", "2025-09-12T22:29:06Z", "For ZM a QA pass only counts on a build cut from main, Internal or Submission. Branch builds are for the dev to check their own work, so a pass there has to be done again once the branch is merged."),
 "dd_card": ("trello", DDCARD, "Arthur Blake", "2025-07-10T14:40:00Z", "DD hotfix builds and QA passes"),
 "dd_comment": ("trello", DD_ACT, "Arthur Blake", "2025-07-10T14:49:12Z", "For DD hotfixes a pass on the dev's branch build is enough, we cherry-pick those straight onto the release branch."),
 "invite_v1": ("gmail", INV1, "Leonard Hayes", "2025-09-26T18:05:00Z", "Subject: Invitation: ZM Collect & Win go/no-go @ Fri Oct 3, 2025 10am - 10:30am (PDT)\n\nGo/no-go for publishing Collect & Win. What holds it: open items in Collect & Win and Daily Gift."),
 "invite_v2": ("gmail", INV2, "Leonard Hayes", "2025-09-30T17:22:00Z", "Subject: Updated invitation: ZM Collect & Win go/no-go @ Thu Oct 2, 2025 10am - 10:30am (PDT)\n\nMoved up a day. What holds it now: open items in Collect & Win and Level-end rewards. Daily Gift can follow the week after."),
 "event": ("gcal", EVT, "Leonard Hayes", "2025-09-30T17:22:00Z", "ZM Collect & Win go/no-go, Thu Oct 2 2025 17:00 UTC. Attendees: Leonard Hayes, Brian Foster, Arthur Blake, Owen Baker, Vincent Parker, Calvin Price."),
 "claim": ("slack", CLAIM, "Calvin Price", "2025-09-29T22:40:12Z", "the pass tokens flying with the coins.. I'm putting that one in the win&collect PR, same place in the reward VFX"),
 "inline": ("github", INLINE, "Arthur Blake", "2025-09-30T15:52:58Z", "Approving so Collect & Win can go out. This only waits for the Collect & Win status though, the pass tokens still fly together with the coins. That needs its own change, it is not in here."),
 "inline2": ("github", INLINE2, "Arthur Blake", "2025-09-30T16:09:09Z", "Fine to merge. The close lock is only on the last pack's reveal though, a single pack can still be closed in the middle of the animation. That needs a follow up, it is not covered here."),
 "reopen": ("slack", REOPEN, "Vincent Parker", "2025-09-30T21:20:12Z", "not the shader thing, but while I was on Android Submission 135 for this: with a gift and a new pass stage both due after a level, the pass popup came up on top of the gift again. so that one is not gone"),
 "else_dm": ("slack", ELSE_DM, "Owen Baker", "2025-09-30T16:25:12Z", "lo del icono placeholder despues del nivel y lo del contador que salia en boss arena y endless ya van en el PR de bugs menores, Blake lo mergeo hace un rato"),
 "filt_dm": ("slack", FILT_DM, "Marcus Bennett", "2025-09-30T18:30:12Z", "yo on today's main build after a level the pack cards fly to the inventory behind the home buttons, u can barely see them. this is with your card PR in. i think its a layer thing not the vfx"),
 "mail": ("gmail", MAIL, "Robert", "2025-09-28T19:40:00Z", "Subject: ZM on the plane\n\nCalvin, played the latest TestFlight on the flight back. One for you: when I hit a new stage on the pass, the new stage banner stays sitting over the home buttons after the level and I have to restart to get rid of it. Happened three times. The rest of the home screen felt a lot calmer than last week. R"),
 "alias_gift": ("linear", ALIAS_GIFT, "Vincent Parker", "2025-09-29T16:40:00Z", "Hit this in my home screen pass too on 1727, the button stays grey the first time the gift opens after a level. Same thing."),
 "alias_streak": ("linear", ALIAS_STREAK, "Vincent Parker", "2025-09-29T16:44:00Z", "Still there on Android 1984, the chest opens over the rewards."),
 "deck": ("gslides", DECK, "Brian Foster", "2025-09-26T17:00:00Z", "ZM weekly - Sep 26\n\nQueue manager: merged to main, QA passed. Collect & Win is next."),
 "folder": ("gdrive", FOLDER, "Calvin Price", "2025-09-23T16:00:00Z", "ZM queue manager"),
 "zom573": ("linear", "ZOM-573", "Brian Foster", "2025-09-26T13:20:00Z", "Daily Login: claim disabled on first open"),
 "zom578": ("linear", "ZOM-578", "Brian Foster", "2025-09-23T19:30:00Z", "Win Streak chest timing on home"),
}
def q(k, s):
    if s not in SEED[k][4]: raise SystemExit(f"quote not in {k}: {s}")
    return s
frag = lambda i, svc, cont, kind, via, seeded, bp, by, quote, reqs, **kw: dict(id=i, service=svc, container=cont, locator=cont, kind=kind, incorporated_via=via, seeded_ids=seeded, base_pointers=bp, delegated_by_record=by, delegation_quote=quote, requirement_ids=reqs, **kw)
frags = [
 frag("K1", "linear", "ZOM-543", "delegation", ["AN1"], [EPIC_NOTE], [], HUB, q("hub", "I left a note on the ticket"), ["R2", "R3", "R4", "R6"],
      names_authorities=[{"id": "H1", "quote": q("epic_note", "Arthur's rule for QA passes")}, {"id": "H2", "quote": q("epic_note", "the review invite")}]),
 frag("K2", "gsheets", SHEET, "requirement", ["AN1"], [SHEET], [], HUB, q("hub", "Vincent's pass sheet"), ["R1"]),
 frag("K3", "trello", CARD, "requirement", ["AN1", "K1"], [RULE_ACT], [], EPIC_NOTE, q("epic_note", "Arthur's rule for QA passes"), ["R3"]),
 frag("K4", "gmail", INV2, "requirement", ["AN1", "K1"], [INV2], [], EPIC_NOTE, q("epic_note", "the review invite"), ["R5"]),
 frag("K5", "gdrive", FOLDER, "destination", ["AN1"], [FOLDER], [], HUB, q("hub", "your ZM queue manager folder"), ["R7"]),
 frag("K6", "gdocs", LEGEND, "format", ["AN1", "K2"], [LEGEND], [], SHEET, q("sheet", "my pass sheet legend"), ["R3"]),
 frag("K7", "gmail", MAIL, "requirement", ["AN1", "K1"], [MAIL], [], EPIC_NOTE, q("epic_note", "whoever it came from and wherever they wrote it"), ["R1"]),
 frag("K8", "slack", MDM, "requirement", ["AN1", "K1"], [FILT_DM], [], EPIC_NOTE, q("epic_note", "whoever it came from and wherever they wrote it"), ["R1"]),
 frag("K9", "slack", VDM, "requirement", ["AN1", "K2", "K6"], [], [V_OK], LEGEND, q("legend", "I told the dev ok in our chat"), ["R3"]),
 frag("K10", "github", PR472, "requirement", ["AN1", "K1"], [INLINE], [], EPIC_NOTE, q("epic_note", "a merged PR covers it"), ["R3"]),
 frag("K16", "github", PR475, "requirement", ["AN1", "K1"], [INLINE2], [], EPIC_NOTE, q("epic_note", "a merged PR covers it"), ["R3"]),
 frag("K11", "slack", ODM, "requirement", ["AN1", "K1"], [ELSE_DM], [], EPIC_NOTE, q("epic_note", "a merged PR covers it"), ["R3"]),
 frag("K12", "linear", "ZOM-573", "requirement", ["AN1", "K1"], [ALIAS_GIFT], [], EPIC_NOTE, q("epic_note", "already has a ticket under another name"), ["R4"]),
 frag("K13", "slack", BUGS, "amendment", ["AN1", "K1"], [REOPEN], [], EPIC_NOTE, q("epic_note", "says later that it is back"), ["R3"]),
 frag("K14", "slack", JDM, "format", ["AN1", "K1"], [], [JULIA], EPIC_NOTE, q("epic_note", "Julia's point about your tickets"), ["R6"]),
 frag("K15", "linear", "ZOM-578", "requirement", ["AN1", "K1"], [ALIAS_STREAK], [], EPIC_NOTE, q("epic_note", "already has a ticket under another name"), ["R4"]),
]
vr = lambda service, rid, cont, seeded, at, **kw: dict(service=service, seeded=seeded, at=at, container=cont, **({"id": rid} if seeded else {"base_pointer": rid}), **kw)
T = lambda i, fam, svcs, seeded, bp, req, wrong, res, **kw: dict(id=i, family=fam, services=svcs, seeded_ids=seeded, base_pointers=bp, requirement=req, expected_wrong_reading=wrong, resolver=res, **kw)
traps = [
 T("T_BRANCH", "done_gap", ["gsheets", "slack", "linear", "trello"], [SHEET, RULE_ACT], [V_OK, C_TESTED, B1718], "R3",
   "rows 1, 5 and 25 are Passed: the sheet says ok, Vincent said looks ok and their tickets are Done",
   "the build he looked at, Match 3D iOS Internal #1718, was cut from Calvin's QueueManager branch (the #builds post says so) and Arthur's rule counts only main builds; a merged PR covers all three, so they wait on QA",
   discovery_order="the sheet row, the Done ticket and the chat ok are all met before anyone looks the build number up in #builds"),
 T("T_INLINE", "done_gap", ["gsheets", "github", "slack"], [INLINE, CLAIM], [PR472], "R3",
   "row 12 waits on QA: the sheet gives #472 as its fix, Calvin said it goes in that PR and #472 is merged",
   "Arthur's inline review comment on #472 says the pass tokens still fly with the coins and that it is not in this PR, so no merged PR covers it; the review body is empty",
   discovery_order="the merged PR and Calvin's own line come back first; the inline comment needs github_get_pull_request_comments",
   version_records=[vr("slack", CLAIM, f"slack:{CLAIM}", True, "2025-09-29T22:40:12Z"), vr("github", INLINE, f"github:{PR472}", True, "2025-09-30T15:52:58Z")]),
 T("T_INLINE_PACK", "done_gap", ["gsheets", "github", "linear"], [INLINE2, "ZOM-585"], [PR475], "R3",
   "row 32 waits on QA: the sheet gives #475 as its fix, #475 is merged and the ticket is In Validation",
   "Arthur's inline review comment on #475 says a single pack can still be closed mid animation and that it is not covered there; the review body is empty",
   discovery_order="the merged PR and the In Validation ticket come back first; the inline comment needs its own call"),
 T("T_REOPEN", "superseding", ["gsheets", "slack", "linear"], [SHEET, REOPEN], [B135], "R3",
   "row 9 is Passed: nr on a main build and its ticket is Done",
   "Vincent's later reply under his shader thread in #zombie-bugs says it came back on Android Submission 135, so it waits on a fix again",
   discovery_order="the sheet and the Done ticket are read first; the reply sits under a post about a shader",
   version_records=[vr("gsheets", SHEET, f"file:{SHEET}", True, "2025-09-30T17:40:00Z"), vr("slack", REOPEN, f"slack:{SHADER_ROOT}", True, "2025-09-30T21:20:12Z")]),
 T("T_ELSE", "completion_elsewhere", ["gsheets", "slack", "github"], [ELSE_DM], [PR470], "R3",
   "rows 15 and 16 wait on a fix: no ticket, no fix in the sheet",
   "Owen already fixed both in his minor bugs PR #470, merged on 30 Sep, and told Calvin so in their own chat in Spanish; the PR body lists both",
   discovery_order="the sheet's blank Fix cell is read first; the chat and the PR body are elsewhere"),
 T("T_MAIL", "exact_predicate", ["gmail"], [MAIL], [], "R1",
   "the reports are the 38 sheet rows",
   "Brian's note brings in what anyone else raised since the 24th; Robert mailed Calvin one on 28 Sep"),
 T("T_FILT", "exact_predicate", ["slack"], [FILT_DM], [], "R1",
   "the reports are the 38 sheet rows",
   "Marcus told Calvin about the pack cards in their own chat on 30 Sep; no ticket holds it"),
 T("T_ALIAS_GIFT", "scope_alias", ["gsheets", "linear"], [ALIAS_GIFT, "ZOM-573"], [], "R4",
   "row 11 has no ticket, so it needs a new sub-issue",
   "ZOM-573, filed as Daily Login, already has it; Vincent's note on that ticket ties the two"),
 T("T_ALIAS_STREAK", "scope_alias", ["gsheets", "linear"], [ALIAS_STREAK, "ZOM-578"], [], "R4",
   "row 20 has no ticket, so it needs a new sub-issue",
   "ZOM-578, filed as Win Streak chest timing, already has it; Vincent's note ties Nathan's chest to it"),
 T("T_GATE", "effective_date", ["slack", "gmail", "gcal"], [GATE_OLD, INV1, INV2, EVT], [], "R5",
   "Collect & Win and Daily Gift hold the review, on Friday",
   "Leonard's updated invitation moves it to Thursday and lists Collect & Win and Level-end rewards; Daily Gift follows the week after",
   discovery_order="Brian's own line in the anchor chat is read first; the invitation is mail",
   version_records=[vr("slack", GATE_OLD, f"slack:{GATE_OLD}", True, "2025-09-26T15:10:12Z"), vr("gmail", INV1, f"gmail:{INV1}", True, "2025-09-26T18:05:00Z"), vr("gmail", INV2, f"gmail:{INV2}", True, "2025-09-30T17:22:00Z")]),
 T("T_PARK", "superseding", ["slack"], [], [PARK_A, PARK_B], "R1",
   "the input blocker after every level is a report to carry",
   "Brian parked it the same day in his own chat with Calvin, and his note leaves it out",
   version_records=[vr("slack", PARK_A, f"slack:{PARK_A}", False, "2025-09-25T13:16:39Z"), vr("slack", PARK_B, f"slack:{PARK_B}", False, "2025-09-25T13:59:55Z")]),
 T("T_DECK", "superseding", ["gslides", "gsheets"], [DECK, SHEET], [], "R2",
   "the weekly deck says the queue manager passed QA, so the areas are clear",
   "Vincent's sheet is later and lists 38 rows, most of them not passed",
   version_records=[vr("gslides", DECK, f"file:{DECK}", True, "2025-09-26T17:00:00Z"), vr("gsheets", SHEET, f"file:{SHEET}", True, "2025-09-30T17:40:00Z")]),
 T("T_FIELDS", "authority", ["linear", "slack"], [EPIC_NOTE], [JULIA], "R6",
   "a new sub-issue takes the priority and assignee the report suggests",
   "Brian's note, citing Julia's point about Calvin's tickets, wants no priority and no assignee on the new ones"),
 T("T_STATE", "stale_summary", ["linear", "gsheets"], ["ZOM-572", "ZOM-574", "ZOM-585"], [], "R4",
   "a ticket's own state is where the report stands",
   "the state follows the status worked out from the records, so three Done tickets go to In Validation and three more go back to Todo"),
 T("D_DDRULE", "distractor", ["trello"], [DD_ACT], [], "R3", "a pass on the dev's branch build is enough", "that comment is about DD hotfixes", distractor_type="other_title"),
 T("D_DDLEGEND", "distractor", ["gdocs"], [DDNOTES], [], "R3", "a tick means passed on the store build", "that note is about Domino Delights lists", distractor_type="other_title"),
 T("D_SKIP", "distractor", ["slack"], [], [f"{BUGS}/1758903616.346579"], "R1", "the tutorial skip exceptions are reports to carry", "Brian's note leaves Oliver's skip work out", distractor_type="scope_adjacent"),
 T("D_ICONVFX", "distractor", ["slack"], [], [f"{VDM}/1758721951.996909"], "R1", "Vincent's chat remark about the pass icon VFX is another report", "his sheet is his whole list", distractor_type="scope_adjacent"),
 T("D_556", "distractor", ["linear"], [], ["ZOM-556"], "R4", "ZOM-556 is the daily gift ticket for row 11", "ZOM-556 is about the skip reset; ZOM-573 carries Vincent's tie", distractor_type="near_duplicate_record"),
 T("D_OLDINVITE", "distractor", ["gmail"], [INV1], [], "R5", "the first invitation's list still stands", "the updated invitation replaces it", distractor_type="withdrawn_ask"),
 T("D_DECK", "distractor", ["gslides"], [DECK], [], "R2", "the deck's line is the status", "report records decide", distractor_type="stale_summary"),
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
 rule("BRANCH", "A24", "done_gap", "same mechanism: a done source (sheet ok, Done ticket, chat ok) with the missing piece in another place (the build's branch in #builds)", ["T_BRANCH"], "R3", "the sheet's ok is a pass", ["B1", "B2", "B3", "B4", "B5", "V1", "V2", "V4", "V5"], ["row 2", "row 3", "row 17"], "branch_over: un-passes a row whose ok was on a main build", "builds-channel", "cut from main"),
 rule("INLINE", "A24", "done_gap", "same mechanism: a merged PR is the done source and the missing piece sits in an inline review comment", ["T_INLINE", "T_INLINE_PACK"], "R3", "a merged PR named in the sheet covers the row", ["I1", "I2", "I3", "I4", "I5", "V2", "V3"], ["row 18", "row 17"], "inline_over: drops the PR cover from a row no reviewer excepted", "github-inline", "pass tokens"),
 rule("REOPEN", "A11", "superseding", "same mechanism: a dated correction in a thread reply under an unrelated root", ["T_REOPEN"], "R3", "nr on a main build is a pass", ["R1", "R2", "R3", "V1", "V3"], ["row 7", "row 27"], "reopen_over: reopens another nr row", "unrelated-thread-reply", "came up on top of the gift again"),
 rule("ELSE", "A25", "completion_elsewhere", "same mechanism: an item that looks open while a record elsewhere shows the work done", ["T_ELSE"], "R3", "a blank Fix cell means no fix", ["E1", "E2", "E3", "E4", "V2", "V3"], ["row 19", "row 6"], "else_over: marks a row covered that no PR names", "owner-chat-and-pr-body", "PR de bugs menores"),
 rule("MAIL", "A17", "exact_predicate", "same mechanism: an in-scope item outside the obvious list, brought in by the scope sentence", ["T_MAIL"], "R1", "the sheet is the whole list", ["M1", "M2", "M3", "V3", "V6"], ["the 38 sheet rows"], "mail_over: adds a mail that reports nothing", "gmail-inbox", "new stage banner"),
 rule("FILT", "A17", "exact_predicate", "same mechanism, different carrier and author: a 1:1 chat no record points at", ["T_FILT"], "R1", "the sheet is the whole list", ["F1", "F2", "F3", "V3", "V7"], ["the 38 sheet rows"], "filt_over: adds a chat remark that is not a report", "artist-chat", "pack cards"),
 rule("ALIAS", "A7", "scope_alias", "same mechanism: a row and an existing ticket named differently, tied by a dated note", ["T_ALIAS_GIFT", "T_ALIAS_STREAK"], "R4", "a blank Ticket cell means a new sub-issue", ["A1", "A2", "A3"], ["row 10", "row 37"], "alias_over: reuses a ticket for a row with none", "ticket-note", "Same thing"),
 rule("GATE", "A12", "authority", "same mechanism: the governing source sits in a rarely opened service and an older version is met first", ["T_GATE"], "R5", "Brian's line in the chat names what holds the review", ["G1", "G2", "V4"], ["row 15", "row 21"], "gate_over: none", "gmail-invitation", "Level-end rewards"),
]
channels = [dict(id=f"CH-{p['id']}", kind="scale", rule=p["id"], degrade="ch_miss", latent="member", family=p["prior_family"], source=p["source"], members=list(p["nodes"]), description=p["natural_reading"]) for p in port]
reqs = {
 "R1": "population: every row of Vincent's pass sheet plus any report someone else on the team raised since 24 Sep about what shows on the home screen after a level",
 "R2": "Status of each area: Clear when all its reports are Passed, otherwise Open, with its count of Open reports",
 "R3": "Status of each report: Passed, Waiting on QA or Waiting on a fix",
 "R4": "Ticket for each report: the ticket that already holds it is moved under the area child with a note and a matching state, otherwise a new sub-issue",
 "R5": "Holds review for each report: not Passed and in an area the review invite lists",
 "R6": "new sub-issue fields: ZOM team, parent the area child, report as title, state by status, no priority, no assignee",
 "R7": "stock-take sheet with tabs Reports and Areas in the ZM queue manager folder, shared with Brian and Vincent",
 "R8": "reply to Brian in the DM with the counts: passed, waiting on QA, waiting on a fix, clear areas, holding the review",
}
services = {
 "slack": {"role": "hub, QA chat, build log, corrections", "weight_reason": "the ask, the branch each build came from and four corrections live here"},
 "linear": {"role": "epic, tickets, destination", "weight_reason": "Brian's note, the ticket ties and every structural write are here"},
 "github": {"role": "PR truth", "weight_reason": "merged PRs and Arthur's inline review decide what a merged PR covers"},
 "gsheets": {"role": "Vincent's pass sheet and the stock-take sheet", "weight_reason": "the report list is read here and the deliverable is written here"},
 "gdocs": {"role": "legend for the sheet codes", "weight_reason": "ok, nr and ok, chat are defined here"},
 "gdrive": {"role": "destination folder and sharing", "weight_reason": "the sheet goes in Calvin's folder and is shared"},
 "gmail": {"role": "review invitation and Robert's report", "weight_reason": "the areas that hold the review and one report exist only in mail"},
 "gcal": {"role": "review event", "weight_reason": "the review's day and attendees"},
 "trello": {"role": "Arthur's rule on QA passes", "weight_reason": "which builds count for a pass"},
 "gslides": {"role": "weekly deck", "weight_reason": "the convincing done summary the report records overturn"},
}
cohort = {"definition": "38 rows of Vincent's pass sheet, 2 reports raised outside it and the 10 areas of Brian's note: 50 records", "definition_source": [HUB, EPIC_NOTE], "key": "report or area", "size": 50, "evidence_surfaces": [
 {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1.0, "records": 20, "seeded": True, "seeded_ids": [ALIAS_GIFT, ALIAS_STREAK], "requirement": "R4", "decides": "Ticket for each report",
  "why_no_bulk": "linear_list_issues returns no comments; the note that ties a row to a ticket needs that ticket's own linear_list_comments",
  "short_circuit": "a row with a blank Ticket cell is only settled by reading candidate tickets; titles use other words, so one search cannot sweep the ties"},
 {"service": "github", "tool": "github_get_pull_request, github_get_pull_request_reviews and github_get_pull_request_comments", "per_record_calls": 3.0, "records": 5, "seeded": True, "seeded_ids": [INLINE, INLINE2], "requirement": "R3", "decides": "Status of each report",
  "why_no_bulk": "github_search_pull_requests returns neither reviews nor inline comments, and in:comments misses inline ones",
  "short_circuit": "merged state alone does not say what a PR covers; only its own body and review surfaces do, and each of the five PRs named needs them"},
 {"service": "slack", "tool": "slack_conversations_history or slack_search_public_and_private on #builds", "per_record_calls": 1.0, "records": 13, "seeded": False, "requirement": "R3", "decides": "Status of each report",
  "why_no_bulk": "the sheet names builds by number only; the branch is in each build's own post, and 146 match3d posts in the last week of September cannot be read in one call",
  "short_circuit": "a re-test only counts on a main build, so each of the 13 distinct builds in the Re-test column and the chat needs its branch"},
 {"service": "gsheets", "tool": "gsheets_values_get", "per_record_calls": 0.1, "records": 38, "seeded": True, "seeded_ids": [SHEET], "requirement": "R1", "decides": "population",
  "why_no_bulk": "one range read returns the rows; counted at a tenth because it is a bulk read", "short_circuit": "the list itself; nothing else holds the rows"},
]}
budget = [
 ("discovery", "slack", 5, "Brian's DM, the QA chat, channel lookups"), ("discovery", "linear", 6, "the epic, its comments, states, labels, team, users"), ("discovery", "gdrive", 3, "the folder and the pass sheet's location"),
 ("discovery", "gsheets", 3, "the pass sheet: metadata and two range reads"), ("discovery", "gdocs", 2, "the legend"), ("rules", "trello", 3, "finding Arthur's rule: search, card, comments"),
 ("rules", "gmail", 4, "the review invitation: search and the two messages"), ("rules", "gcal", 2, "the review event"), ("rules", "slack", 2, "Julia's note"),
 ("enumeration", "slack", 12, "who else raised a report since the 24th: recent 1:1 chats, #zombie-bugs with its threads"), ("enumeration", "gmail", 4, "mail to Calvin since the 24th"),
 ("enumeration", "linear", 6, "ZOM tickets since the 20th and candidate tickets for rows with no key"), ("enumeration", "github", 4, "match3d PRs merged since the 24th"), ("enumeration", "gslides", 1, "the weekly deck"),
 ("per-record", "linear", 20, "comments on the 20 tickets that hold a report"), ("per-record", "github", 15, "body, reviews and inline comments of the five PRs the rows rest on"), ("per-record", "slack", 13, "the #builds post of each distinct build in the Re-test column and the chat"),
 ("per-record", "linear", 70, "10 area children, 20 new sub-issues, 20 tickets moved under a child and 20 notes: each a distinct target with no batch form"),
 ("writes", "gsheets", 4, "stock-take sheet: create and fill two tabs"), ("writes", "gdrive", 3, "move into the folder and share with two people"), ("writes", "linear", 1, "the epic's own state or text"), ("writes", "slack", 1, "reply to Brian"),
 ("read-back", "linear", 3, "confirm the tree"), ("read-back", "gsheets", 2, "confirm the sheet"),
]
manifest = {
 "_note": "DRAFT manifest (scenario stage). Seeded ids are planned (plan/build_scenario.py, plan/seed_text.json, plan/reports.py); /create-injection writes the final manifest.",
 "persona": "calvin_price", "assignment_context": {k: ctx.get(k) for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc")} | {"difficulty_mode": ctx.get("difficulty_mode")},
 "horizon": "Long Horizon", "effective_profile": "extreme",
 "author_targets": {"calls_per_run": "over 130 in every run", "average": "strictly under 60 %", "largest_pattern": "under 50 % of failing runs", "design_target": "E[avg] <= 52 %", "source": "requester, 2026-11-10"},
 "volume_exception": {"reason": "50 cohort records and about 190 honest calls; reaching 500 would need padding, which fails on its own. The per-record floor counts read surfaces only (20 ticket comment reads, 15 PR reads, 13 build lookups), so it is 45, not the 120 quoted in the analysis, which counted writes",
  "requester_confirmation": "requester, Claude Code chat 2026-11-10: 'i want over 130 tool calls in each runs ... you can choose from your self which option is best fit for my requirements in this task' (choice delegated; recorded in 00_Pre_Scenario_Analysis.md section 11, item 2)", "call_budget_floor": 180, "per_record_floor": 45},
 "requirements": reqs, "services": services,
 "anchors": [{"id": "AN1", "prompt_reference": "Brian's message from yesterday", "service": "slack", "locator": HUB, "requirement_ids": ["R1", "R7", "R8"]},
             {"id": "AN2", "prompt_reference": "the Queue Manager ticket", "service": "linear", "locator": "ZOM-543", "requirement_ids": ["R2", "R4"]}],
 "ask_fragments": frags,
 "authorities": [
  {"id": "H1", "name": "Arthur's rule for QA passes", "home_service": "trello", "decoy_service": "trello", "governs": ["R3"], "findable_query": "QA pass", "seeded_ids": [CARD, RULE_ACT], "base_pointers": [], "decoy_seeded_ids": [DD_ACT], "decoy_base_pointers": [],
   "decoy_scope": {"dimension": "game", "decoy": "Domino Delights", "task": "ZM (match3d)"}},
  {"id": "H2", "name": "the review invite", "home_service": "gmail", "decoy_service": "slack", "governs": ["R5"], "findable_query": "Collect & Win go/no-go", "seeded_ids": [INV2, EVT], "base_pointers": [], "decoy_seeded_ids": [GATE_OLD, INV1], "decoy_base_pointers": []},
 ],
 "cohort": cohort,
 "chains": [
  {"id": "C1", "root_cause": "A24", "ends_in": "R3", "hops": [{"service": "gsheets", "record": SHEET, "finding": "row 5: fix #465, re-test ok, chat"}, {"service": "slack", "record": C_TESTED, "finding": "Calvin: #1718 already tested"}, {"service": "slack", "record": V_OK, "finding": "Vincent: looks ok"}, {"service": "slack", "record": B1718, "finding": "#1718 was built from the QueueManager branch"}, {"service": "trello", "record": RULE_ACT, "finding": "only main builds count"}]},
  {"id": "C2", "root_cause": "A11", "ends_in": "R3", "hops": [{"service": "gsheets", "record": SHEET, "finding": "row 9: nr on #1745"}, {"service": "slack", "record": B135, "finding": "Android Submission #135 built from main on 30 Sep"}, {"service": "slack", "record": REOPEN, "finding": "Vincent: it came up again on Submission 135"}]},
  {"id": "C3", "root_cause": "A25", "ends_in": "R3", "hops": [{"service": "gsheets", "record": SHEET, "finding": "rows 15 and 16: no fix"}, {"service": "slack", "record": ELSE_DM, "finding": "Owen: both went in his minor bugs PR"}, {"service": "github", "record": PR470, "finding": "merged 30 Sep; the body lists both"}]},
  {"id": "C4", "root_cause": "A7", "ends_in": "R4", "hops": [{"service": "gsheets", "record": SHEET, "finding": "row 11: no ticket"}, {"service": "linear", "record": "ZOM-573", "finding": "open ticket filed as Daily Login"}, {"service": "linear", "record": ALIAS_GIFT, "finding": "Vincent ties his row to it"}]},
  {"id": "C5", "root_cause": "A12", "ends_in": "R5", "hops": [{"service": "slack", "record": GATE_OLD, "finding": "Brian: Collect & Win and Daily Gift"}, {"service": "gmail", "record": INV1, "finding": "first invitation, same list"}, {"service": "gmail", "record": INV2, "finding": "updated: Collect & Win and Level-end rewards"}]},
  {"id": "C6", "root_cause": "A17", "ends_in": "R1", "hops": [{"service": "linear", "record": EPIC_NOTE, "finding": "anything somebody else raised since the 24th"}, {"service": "gmail", "record": MAIL, "finding": "Robert's banner report"}, {"service": "slack", "record": FILT_DM, "finding": "Marcus's pack cards report"}]},
 ],
 "traps": traps, "mechanism_portfolio": port, "channels": channels,
 "call_budget": [{"phase": a, "service": b, "calls": c, "reason": d} for a, b, c, d in budget],
 "writes": [
  {"service": "linear", "tool": "linear_create_issue", "count": 30, "depends_on": ["T_MAIL", "T_FILT", "T_ALIAS_GIFT", "T_ALIAS_STREAK", "T_ELSE", "T_BRANCH"], "requirements": ["R2", "R4", "R6"]},
  {"service": "linear", "tool": "linear_update_issue", "count": 21, "depends_on": ["T_BRANCH", "T_REOPEN", "T_INLINE", "T_ALIAS_GIFT"], "requirements": ["R4"]},
  {"service": "linear", "tool": "linear_create_comment", "count": 20, "depends_on": ["T_BRANCH", "T_REOPEN", "T_INLINE", "T_ALIAS_STREAK"], "requirements": ["R4"]},
  {"service": "gsheets", "tool": "gsheets_values_update", "count": 3, "depends_on": ["T_BRANCH", "T_GATE", "T_MAIL", "T_FILT"], "requirements": ["R7"]},
  {"service": "gdrive", "tool": "gdrive_share_file", "count": 2, "depends_on": ["K5"], "requirements": ["R7"]},
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
slots = [
 S("V1", "Passed count in the reply", 5, MS, "statuses joined across the sheet, #builds, Arthur's rule and a later reply", "write_content", ["text", "reply", "\\b13\\b"], ["BRANCH", "REOPEN"]),
 S("V2", "Waiting on QA count in the reply", 5, MS, "merged PRs joined with passes across GitHub, Slack and the sheet", "write_content", ["text", "reply", "\\b6\\b"], ["BRANCH", "ELSE", "INLINE"]),
 S("V3", "Waiting on a fix count in the reply", 5, MS, "what no merged PR covers, across the sheet, mail, chats and GitHub", "write_content", ["text", "reply", "\\b21\\b"], ["REOPEN", "INLINE", "ELSE", "MAIL", "FILT"], "volume", volume_for=["plain"]),
 S("V4", "Holding the review count in the reply", 5, MS, "statuses joined with the areas on the updated invitation", "write_content", ["text", "reply", "\\b8\\b"], ["GATE", "BRANCH"]),
 S("V5", "Clear areas count in the reply", 3, CMP, "areas rolled up from report statuses", "write_content", ["text", "reply", "\\b(1|one)\\b"], ["BRANCH"]),
 S("V6", "Season Pass area shows 5 open reports", 5, MS, "area count joined across the pass sheet and a report that only came by mail", "write_content", ["text", "sheet", row("Season Pass", "\\b5\\b")], ["MAIL"]),
 S("V7", "Card packs area shows 3 open reports", 5, MS, "area count joined across the pass sheet and a report that only came in a 1:1 chat", "write_content", ["text", "sheet", row("Card packs", "\\b3\\b")], ["FILT"]),
 S("B1", "Back to back tutorials row is Waiting on QA", 5, MS, "sheet ok and Done ticket against the build's branch and Arthur's rule", "direct", fld(1, "Status"), ["BRANCH"]),
 S("B2", "Coin animation row is Waiting on QA", 5, MS, "same join on a second row", "direct", fld(5, "Status"), ["BRANCH"]),
 S("B3", "Boss arena tutorial row is Waiting on QA", 5, MS, "same join on a third row", "direct", fld(25, "Status"), ["BRANCH"]),
 S("B4", "ZOM-570 goes back to In Validation", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-570", "In Validation")], ["BRANCH"]),
 S("B5", "Boss Arena area is Open", 5, MS, "area rolled up from a status that depends on the build's branch", "write_content", ["text", "sheet", row("Boss Arena", "Open")], ["BRANCH"]),
 S("R1", "Pass popup over the gift row is Waiting on a fix", 5, MS, "nr on a main build against a later reply in another thread", "direct", fld(9, "Status"), ["REOPEN"]),
 S("R2", "ZOM-572 goes back to Todo", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-572", "Todo")], ["REOPEN"]),
 S("R3", "Its note names Submission 135", 3, IN, "the build it came back on, read from the reply", "write_content", ["text", "comments", "135"], ["REOPEN"]),
 S("I1", "Pass tokens row is Waiting on a fix", 5, MS, "merged PR in the sheet against the reviewer's inline comment", "direct", fld(12, "Status"), ["INLINE"]),
 S("I2", "ZOM-574 goes back to Todo", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-574", "Todo")], ["INLINE"]),
 S("I3", "Its Why says #472 does not cover it", 3, IN, "reads the exception from the review", "direct", ["reason_matches", KEY[12], "472"], ["INLINE"]),
 S("I4", "Pack close button row is Waiting on a fix", 5, MS, "merged PR and In Validation ticket against the reviewer's inline comment", "direct", fld(32, "Status"), ["INLINE"]),
 S("I5", "ZOM-585 goes back to Todo", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-585", "Todo")], ["INLINE"]),
 S("E1", "Placeholder icon row is Waiting on QA", 5, MS, "blank Fix cell against the owner's chat and a merged PR body", "direct", fld(15, "Status"), ["ELSE"]),
 S("E2", "Token counter row is Waiting on QA", 5, MS, "same join on a second row", "direct", fld(16, "Status"), ["ELSE"]),
 S("E3", "Its Why names #470", 3, IN, "the PR read from GitHub", "direct", ["reason_matches", KEY[15], "470"], ["ELSE"]),
 S("E4", "Its sub-issue is filed In Validation", 3, IN, "state follows the status", "write_content", ["text", "issues", row("placeholder", "In Validation")], ["ELSE"]),
 S("M1", "Robert's banner report is in the sheet", 5, MS, "scope sentence joined with a mail", "direct", fld(39, "Status"), ["MAIL"]),
 S("M2", "A sub-issue carries it", 3, IN, "write follows the report", "write_content", ["text", "issues", "[Bb]anner"], ["MAIL"]),
 S("M3", "Its area is Season Pass", 3, IN, "area read from the report", "direct", fld(39, "Area"), ["MAIL"]),
 S("F1", "Marcus's pack cards report is in the sheet", 5, MS, "scope sentence joined with a 1:1 chat", "direct", fld(40, "Status"), ["FILT"]),
 S("F2", "A sub-issue carries it", 3, IN, "write follows the report", "write_content", ["text", "issues", "[Pp]ack cards"], ["FILT"]),
 S("F3", "Its area is Card packs", 3, IN, "area read from the report", "direct", fld(40, "Area"), ["FILT"]),
 S("A1", "Grey claim button row uses ZOM-573", 5, MS, "row tied to a ticket under another name by a note", "direct", fld(11, "Ticket"), ["ALIAS"]),
 S("A2", "Nathan's chest row uses ZOM-578", 5, MS, "row tied to a ticket under another name by a note", "direct", fld(20, "Ticket"), ["ALIAS"]),
 S("A3", "Note on ZOM-573", 3, IN, "write on the reused ticket", "write_content", ["text", "comments", row("ZOM-573", "(fix|Waiting|Todo)")], ["ALIAS"]),
 S("G1", "Gift calendar row does not hold the review", 5, MS, "status joined with the updated invitation's areas", "direct", fld(10, "Holds review"), ["GATE"]),
 S("G2", "Coins over the pre-level panel row holds the review", 5, MS, "status joined with the updated invitation's areas", "direct", fld(6, "Holds review"), ["GATE"]),
 S("K1", "Plain sample: stars on tablets", 1, LK, "blank cells read from the sheet", "direct", fld(8, "Status"), role="sample", group="plain"),
 S("K2", "Plain sample: pass start popup", 1, LK, "blank cells read from the sheet", "direct", fld(13, "Status"), role="sample", group="plain"),
 S("K3", "Plain sample: endless chest", 1, LK, "blank cells read from the sheet", "direct", fld(30, "Status"), role="sample", group="plain"),
 S("K4", "Plain sample: red dot", 1, LK, "blank cells read from the sheet", "direct", fld(34, "Status"), role="sample", group="plain"),
 S("K5", "Plain sample: freezer popup", 1, LK, "blank cells read from the sheet", "direct", fld(37, "Status"), role="sample", group="plain"),
 S("K6", "Passed on a main build: card upgrade tutorial", 3, CMP, "ok checked against the build's branch", "direct", fld(2, "Status")),
 S("K7", "Passed on a main build: event bar wait", 3, CMP, "ok checked against the build's branch and the merge time", "direct", fld(17, "Status")),
 S("K8", "Waiting on QA: event panel over rewards", 3, CMP, "merged PR with no re-test", "direct", fld(18, "Status")),
 S("K9", "Zombie Lane area is Clear", 3, CMP, "area rolled up from three passed rows", "write_content", ["text", "sheet", row("Zombie Lane", "Clear")]),
 S("K10", "Area children exist under the epic", 1, LK, "names from Brian's note", "write_content", ["text", "issues", "Endless Mode"]),
 S("K11", "A plain row gets a Todo sub-issue: stars on tablets", 1, LK, "state from Brian's note", "write_content", ["text", "issues", row("[Ss]tars", "Todo")]),
 S("K12", "A ticket moved under its child: ZOM-568", 1, LK, "parent set from the row's area", "write_content", ["text", "updates", "ZOM-568"]),
 S("K13", "Ticket key in a sheet row", 1, LK, "key copied from the pass sheet", "direct", fld(3, "Ticket")),
 S("D1", "Sheet in the folder", 1, LK, "destination named in the DM", "delivery", ["delivery", "register_parent", FOLDER]),
 S("D2", "Sheet shared with Brian and Vincent", 1, LK, "recipients named in the DM", "delivery", ["delivery", "share_reader", "brian.foster@harmonygames.co"]),
 S("D3", "Reply in Brian's DM", 1, LK, "destination named in the prompt", "delivery", ["link", "reply"]),
]
YES = {"Passed": ["Passed", "Pass", "Done"], "Waiting on QA": ["Waiting on QA", "Waits on QA", "In Validation", "QA"], "Waiting on a fix": ["Waiting on a fix", "Waits on a fix", "Todo", "Fix"]}
SPAN_REPLY = "tell me here how many are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many hold the review"
SPAN_SHEET = "put a stock-take sheet in your ZM queue manager folder"
SPAN_LINE = "every report gets its line under the right child"
for s_ in slots:
    sel = s_["selector"]
    s_["incorporating_span"] = SPAN_REPLY if sel[:2] == ["text", "reply"] or sel == ["link", "reply"] else (SPAN_LINE if sel[0] == "text" and sel[1] in ("issues", "comments", "updates") else SPAN_SHEET)
    assert s_["incorporating_span"] in SEED["hub"][4]
surface = {"kind": "GRADABLE_SURFACE", "version": 1, "task": "calvin_qm_epic", "revision": "design-1", "classes": ["Passed", "Waiting on QA", "Waiting on a fix"], "truth_fields": {"class": "Status", "groups": "groups"},
 "deliverables": {
  "sheet": {"kind": "table", "name_regex": "(?i).*(stock|queue|report|epic).*", "key_column": "Report", "key_regex": "(?:Report 1|Report 2|[A-Za-z][A-Za-z0-9 .,'()&/-]*)", "columns": ["Report", "Area", "Status", "Ticket", "Holds review", "Why"], "class_column": "Status", "reason_column": "Why",
            "comparators": {"Status": "yes_no", "Ticket": "issue_key", "Holds review": "norm", "Area": "norm"}, "yes_no": YES},
  "reply": {"kind": "json_text", "tool": "slack_send_message"}, "issues": {"kind": "json_text", "tool": "linear_create_issue"}, "comments": {"kind": "json_text", "tool": "linear_create_comment"}, "updates": {"kind": "json_text", "tool": "linear_update_issue"}},
 "slots": slots}
json.dump({k: {"service": v[0], "id": v[1], "author": v[2], "at": v[3], "text": v[4]} for k, v in SEED.items()}, open(os.path.join(HERE, "seed_text.json"), "w"), indent=1)
json.dump({"areas": AREAS, "gate_areas": RP.GATE_AREAS, "old_gate_areas": RP.OLD_GATE_AREAS, "main_builds": RP.MAIN_BUILDS, "branch_builds": RP.BRANCH_BUILDS, "rows": RP.truth()}, open(os.path.join(HERE, "truth_sketch.json"), "w"), indent=1)
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

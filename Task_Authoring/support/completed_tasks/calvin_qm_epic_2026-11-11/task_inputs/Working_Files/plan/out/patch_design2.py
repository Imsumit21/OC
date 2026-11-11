s=open('build_scenario.py').read()
def rep(a,b):
    global s
    if a not in s: raise SystemExit('MISSING: '+a[:80])
    s=s.replace(a,b,1)
def block(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i); s=s[:i]+new+s[j:]
rep('BDM, VDM, ODM, MDM, JDM = "D0770ET6WBW", "D06UPGF5PQV", "D05S1S2H55M", "D05U73FNDDL", "D05HYDTG5TJ"','BDM, VDM, ODM, MDM, JDM = "D0770ET6WBW", "D06UPGF5PQV", "D07GCPNJPSA", "D05U73FNDDL", "D05HYDTG5TJ"   # ODM: Calvin and Oliver Brooks')
rep('ELSE_DM = f"{ODM}/1759249512.306229"','ELSE_DM = f"{ODM}/1759250112.306229"')
rep('ALIAS_GIFT, ALIAS_STREAK = cid("alias-573"), cid("alias-578")','ALIAS_GIFT, ALIAS_STREAK = cid("alias-556"), cid("alias-560")')
rep('PR472, PR470, PR465 = "harmonygames-Games/match3d#472", "harmonygames-Games/match3d#470", "harmonygames-Games/match3d#465"','PR472, PR473, PR465 = "harmonygames-Games/match3d#472", "harmonygames-Games/match3d#473", "harmonygames-Games/match3d#465"')
NL="\\n"
SEEDTXT='''SEED = {
 "hub": ("slack", HUB, "Brian Foster", "2025-09-30T23:10:05Z", "Hello! Before the Collect&Win review I want the queue manager to be a real epic. Right now it is one ticket and everything else is in chats and in Vincent's pass sheet. I left a note on the ticket about how I want it. One child for each area, and every report gets its line under the right child. Please also put a stock-take sheet in your ZM queue manager folder and share it with me and Vincent. When it is done tell me here how many reports are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many reports hold the review."),
 "epic_note": ("linear", EPIC_NOTE, "Brian Foster", "2025-09-30T22:48:00Z", "How I want this epic.@@@@Children: " + ", ".join(AREAS) + ". One child each, same team, no assignee.@@@@Reports: every row of Vincent's pass sheet. His sheet is his whole list, so don't add things he only said in chat. Plus any bug somebody else on the team saw in a build and told you about directly, by mail or in a DM, since Vincent started his pass on the 26th, about the home screen after a level. If it is already a row, don't count it twice. Collect & Win has its own bug canvas with Owen, that stays there. Oliver's tutorial skip work is his own thing, leave it out. The input blocker I already parked, leave it out too.@@@@Status of a report, one of three. Passed: Vincent's ok or nr on a build that counts under Arthur's rule for QA passes, and it stays passed unless whoever raised it says later that it is back. Waiting on QA: not passed, and the fix is merged. Vincent's Fix column is only what the dev told him at the time, so check the PR itself. If the dev who fixed it tells you which merged PR has it, that counts too. Waiting on a fix: everything else, also when it came back after a pass.@@@@Line under the child: if a ticket already has the report, move that ticket under the child and leave a note with the status and why. If its state does not match the status, put Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix. If no ticket has it, make a sub-issue under the child with the report as the title and the state the same way. Vincent sometimes writes a row for something that already has a ticket under another name, use that ticket then. No priority and no assignee on the new ones, that is Julia's point about your tickets, I will set them.@@@@A child is Clear when all its reports are Passed, otherwise Open. Make the child Done when it is Clear and Todo when it is Open.@@@@Holds the review: a report that is not Passed, in an area the review invite lists.@@@@Sheet: tab Reports with Report, Area, Status, Ticket, Holds review, Why. Tab Areas with Area, Status, Open reports."),
 "gate_old": ("slack", GATE_OLD, "Brian Foster", "2025-09-26T15:10:12Z", "For the C&W review on Friday what holds it is collect&win and daily gift, the rest can come after"),
 "sheet": ("gsheets", SHEET, "Vincent Parker", "2025-09-30T19:30:00Z", "ZM home screen flow - QA pass@@@@Columns: #, Area, What happens, Found on, Ticket, Fix, Re-test. 38 rows, in plan/reports.py.@@@@Note under the table: The codes are in my pass sheet legend doc. Raised by me unless the row says otherwise."),
 "legend": ("gdocs", LEGEND, "Vincent Parker", "2025-09-26T09:30:00Z", "How to read my pass sheets@@@@Found on: the build I first saw it on.@@Ticket: the Linear key if I filed one.@@Fix: the PR the dev told me it went into. Blank if nobody told me.@@Re-test: ok and a build means it is fine on that build. nr and a build means I could not make it happen on that build. again and a build means it still happens. ok, chat means I told the dev ok in our chat, the build is there. Blank means not re-tested yet."),
 "dd_legend": ("gdocs", DDNOTES, "Vincent Parker", "2025-03-11T10:00:00Z", "DD regression notes@@@@For Domino Delights a tick in my regression list means it passed on the store build. Web builds are checked separately."),
 "rule_card": ("trello", CARD, "Arthur Blake", "2025-09-12T22:20:00Z", "ZM builds and QA passes"),
 "rule_comment": ("trello", RULE_ACT, "Arthur Blake", "2025-09-12T22:29:06Z", "For ZM a QA pass only counts on a build of the main branch, whichever job built it, Internal, Android or Submission. A build of a feature branch is for the dev to check their own work, so a pass there has to be done again once the branch is merged."),
 "dd_card": ("trello", DDCARD, "Arthur Blake", "2025-07-10T14:40:00Z", "DD hotfix builds and QA passes"),
 "dd_comment": ("trello", DD_ACT, "Arthur Blake", "2025-07-10T14:49:12Z", "For DD hotfixes a pass on the dev's branch build is enough, we cherry-pick those straight onto the release branch."),
 "invite_v1": ("gmail", INV1, "Leonard Hayes", "2025-09-26T18:05:00Z", "Subject: Invitation: ZM Collect & Win go/no-go @ Fri Oct 3, 2025 10am - 10:30am (PDT)@@@@Go/no-go for publishing Collect & Win. What holds it: open items in Collect & Win and Daily Gift."),
 "invite_v2": ("gmail", INV2, "Leonard Hayes", "2025-09-30T17:22:00Z", "Subject: Updated invitation: ZM Collect & Win go/no-go @ Thu Oct 2, 2025 10am - 10:30am (PDT)@@@@Moved up a day. What holds it now: open items in Collect & Win and Level-end rewards. Daily Gift can follow the week after."),
 "event": ("gcal", EVT, "Leonard Hayes", "2025-09-30T17:22:00Z", "ZM Collect & Win go/no-go, Thu Oct 2 2025 17:00 UTC. Attendees: Leonard Hayes, Brian Foster, Arthur Blake, Owen Baker, Vincent Parker, Calvin Price."),
 "inline": ("github", INLINE, "Arthur Blake", "2025-09-30T15:52:58Z", "Approving so Collect & Win can go out. The season pass icon restart you mentioned is not in this diff, this only adds the Collect & Win wait. That needs its own change."),
 "inline2": ("github", INLINE2, "Arthur Blake", "2025-09-30T16:09:09Z", "Fine to merge. I don't see the pack sound stop you talked about anywhere in here, so that one still needs doing."),
 "reopen": ("slack", REOPEN, "Vincent Parker", "2025-09-30T21:20:12Z", "not the shader thing, but while I was on Android Submission 135 for this: with a gift and a new pass stage both due after a level, the pass popup came up on top of the gift again. so that one is not gone"),
 "else_dm": ("slack", ELSE_DM, "Oliver Brooks", "2025-09-30T16:35:12Z", "btw two things [PERSON_NAME_0050] had on the pass were mine, the start popup coming back after every level and the bar filling before the tokens land. both went in with the addressables/sp PR, Blake merged it this morning"),
 "filt_dm": ("slack", FILT_DM, "Marcus Bennett", "2025-09-30T18:30:12Z", "yo on today's main build the pass icon glow stays on after i claimed everything, saw it 3 levels in a row. its not the vfx, i think the state doesnt reset"),
 "mail": ("gmail", MAIL, "Robert", "2025-09-28T19:40:00Z", "Subject: ZM on the plane@@@@Calvin, played the latest TestFlight on the flight back. One for you: after a single win the streak chest popped up twice in a row, the second time empty. Happened three times. The rest of the home screen felt a lot calmer than last week. R"),
 "alias_gift": ("linear", ALIAS_GIFT, "Vincent Parker", "2025-09-30T18:05:00Z", "Saw this again in my home screen pass on 1727, the day counter keeps going after a skipped day. Same thing."),
 "alias_streak": ("linear", ALIAS_STREAK, "Vincent Parker", "2025-09-30T18:08:00Z", "Still there on Android 1984 in my home screen pass, the freezer from the abandoned pack never shows up on home."),
 "deck": ("gslides", DECK, "Brian Foster", "2025-09-26T17:00:00Z", "ZM weekly - Sep 26@@@@Queue manager: merged to main, QA passed. Collect & Win is next."),
 "folder": ("gdrive", FOLDER, "Calvin Price", "2025-09-23T16:00:00Z", "ZM queue manager"),
}
'''.replace("@@",NL)
block('SEED = {','def q(k, s):',SEEDTXT)
block('frags = [','vr = lambda','''frags = [
 frag("K1", "linear", "ZOM-543", "delegation", ["AN1"], [EPIC_NOTE], [], HUB, q("hub", "I left a note on the ticket"), ["R2", "R3", "R4", "R6"],
      names_authorities=[{"id": "H1", "quote": q("epic_note", "Arthur's rule for QA passes")}, {"id": "H2", "quote": q("epic_note", "the review invite")}]),
 frag("K2", "gsheets", SHEET, "requirement", ["AN1"], [SHEET], [], HUB, q("hub", "Vincent's pass sheet"), ["R1"]),
 frag("K3", "trello", CARD, "requirement", ["AN1", "K1"], [RULE_ACT], [], EPIC_NOTE, q("epic_note", "Arthur's rule for QA passes"), ["R3"]),
 frag("K4", "gmail", INV2, "requirement", ["AN1", "K1"], [INV2], [], EPIC_NOTE, q("epic_note", "the review invite"), ["R5"]),
 frag("K5", "gdrive", FOLDER, "destination", ["AN1"], [FOLDER], [], HUB, q("hub", "your ZM queue manager folder"), ["R7"]),
 frag("K6", "gdocs", LEGEND, "format", ["AN1", "K2"], [LEGEND], [], SHEET, q("sheet", "my pass sheet legend"), ["R3"]),
 frag("K7", "gmail", MAIL, "requirement", ["AN1", "K1"], [MAIL], [], EPIC_NOTE, q("epic_note", "told you about directly, by mail or in a DM"), ["R1"]),
 frag("K8", "slack", MDM, "requirement", ["AN1", "K1"], [FILT_DM], [], EPIC_NOTE, q("epic_note", "told you about directly, by mail or in a DM"), ["R1"]),
 frag("K9", "slack", VDM, "requirement", ["AN1", "K2", "K6"], [], [V_OK], LEGEND, q("legend", "I told the dev ok in our chat"), ["R3"]),
 frag("K10", "github", PR472, "requirement", ["AN1", "K1"], [INLINE], [], EPIC_NOTE, q("epic_note", "check the PR itself"), ["R3"]),
 frag("K16", "github", PR475, "requirement", ["AN1", "K1"], [INLINE2], [], EPIC_NOTE, q("epic_note", "check the PR itself"), ["R3"]),
 frag("K11", "slack", ODM, "requirement", ["AN1", "K1"], [ELSE_DM], [], EPIC_NOTE, q("epic_note", "If the dev who fixed it tells you which merged PR has it"), ["R3"]),
 frag("K12", "linear", "ZOM-556", "requirement", ["AN1", "K1"], [ALIAS_GIFT], ["ZOM-556"], EPIC_NOTE, q("epic_note", "already has a ticket under another name"), ["R4"]),
 frag("K13", "slack", BUGS, "amendment", ["AN1", "K1"], [REOPEN], [], EPIC_NOTE, q("epic_note", "says later that it is back"), ["R3"]),
 frag("K14", "slack", JDM, "format", ["AN1", "K1"], [], [JULIA], EPIC_NOTE, q("epic_note", "Julia's point about your tickets"), ["R6"]),
 frag("K15", "linear", "ZOM-560", "requirement", ["AN1", "K1"], [ALIAS_STREAK], ["ZOM-560"], EPIC_NOTE, q("epic_note", "already has a ticket under another name"), ["R4"]),
]
''')
block('traps = [','led = {}','''traps = [
 T("T_BRANCH", "done_gap", ["gsheets", "slack", "trello"], [SHEET, RULE_ACT], [V_OK, C_TESTED, B1718], "R3",
   "rows 1, 5 and 25 are Passed: the sheet says ok and Vincent wrote looks ok in the chat",
   "the build he looked at, Match 3D iOS Internal #1718, was cut from Calvin's QueueManager branch (the #builds post says so) and Arthur's rule counts only builds of the main branch; #465 is merged, so they wait on QA",
   discovery_order="the sheet row and the chat ok are both met before anyone looks the build number up in #builds"),
 T("T_INLINE", "done_gap", ["gsheets", "github", "linear"], [INLINE, "ZOM-571"], [PR472], "R3",
   "row 12 waits on QA: the sheet gives #472 as its fix, #472 is merged and its ticket is In Validation",
   "Arthur's inline review comment on #472 says the season pass icon restart is not in that diff; the review body is empty and the PR's own summary lists only the Collect & Win wait",
   discovery_order="the merged PR and the In Validation ticket come back first; the inline comment needs github_get_pull_request_comments"),
 T("T_INLINE_PACK", "done_gap", ["gsheets", "github", "linear"], [INLINE2, "ZOM-581"], [PR475], "R3",
   "row 32 waits on QA: the sheet gives #475 as its fix, #475 is merged and the ticket is In Validation",
   "Arthur's inline review comment on #475 says the pack sound stop is nowhere in that PR; the review body is empty and the PR's summary does not mention sound",
   discovery_order="the merged PR and the In Validation ticket come back first; the inline comment needs its own call"),
 T("T_REOPEN", "superseding", ["gsheets", "slack"], [SHEET, REOPEN], [B135], "R3",
   "row 9 is Passed: nr on a main build",
   "Vincent's later reply under his shader thread in #zombie-bugs says it came back on Android Submission 135, so it waits on a fix again",
   discovery_order="the sheet is read first; the reply sits under a post about a shader",
   version_records=[vr("gsheets", SHEET, f"file:{SHEET}", True, "2025-09-30T19:30:00Z"), vr("slack", REOPEN, f"slack:{SHADER_ROOT}", True, "2025-09-30T21:20:12Z")]),
 T("T_ELSE", "completion_elsewhere", ["gsheets", "slack", "github", "linear"], [ELSE_DM, "ZOM-572"], [PR473], "R3",
   "rows 13 and 38 wait on a fix: the sheet names no fix and ZOM-572 is Todo",
   "Oliver already fixed both and told Calvin in their own chat that they went in with his addressables/sp PR, #473, merged on 30 Sep",
   discovery_order="the sheet's blank Fix cell and the Todo ticket are read first; the chat is elsewhere"),
 T("T_MAIL", "exact_predicate", ["gmail"], [MAIL], [], "R1",
   "the reports are the 38 sheet rows",
   "Brian's note brings in any bug somebody else saw in a build and told Calvin about directly since the 26th; Robert mailed him one on 28 Sep"),
 T("T_FILT", "exact_predicate", ["slack"], [FILT_DM], [], "R1",
   "the reports are the 38 sheet rows",
   "Marcus told Calvin about the pass icon glow in their own chat on 30 Sep; no ticket holds it"),
 T("T_ALIAS_GIFT", "scope_alias", ["gsheets", "linear"], [ALIAS_GIFT], ["ZOM-556"], "R4",
   "row 11 has no ticket, so it needs a new sub-issue",
   "base ticket ZOM-556, the daily gift skip reset ticket, already has it; Vincent's note on that ticket ties his row to it"),
 T("T_ALIAS_STREAK", "scope_alias", ["gsheets", "linear"], [ALIAS_STREAK], ["ZOM-560"], "R4",
   "row 20 has no ticket, so it needs a new sub-issue",
   "base ticket ZOM-560, the abandoned pack freezer ticket, already has it; Vincent's note ties his row to it"),
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
   version_records=[vr("gslides", DECK, f"file:{DECK}", True, "2025-09-26T17:00:00Z"), vr("gsheets", SHEET, f"file:{SHEET}", True, "2025-09-30T19:30:00Z")]),
 T("T_FIELDS", "authority", ["linear", "slack"], [EPIC_NOTE], [JULIA], "R6",
   "a new sub-issue takes the priority and assignee the report suggests",
   "Brian's note, citing Julia's point about Calvin's tickets, wants no priority and no assignee on the new ones"),
 T("T_STATE", "stale_summary", ["linear", "gsheets"], ["ZOM-571", "ZOM-572", "ZOM-581"], [], "R4",
   "a ticket's own state is where the report stands",
   "the state follows the status worked out from the records: ZOM-571 and ZOM-581 go back to Todo and ZOM-572 goes to In Validation"),
 T("D_DDRULE", "distractor", ["trello"], [DD_ACT], [], "R3", "a pass on the dev's branch build is enough", "that comment is about DD hotfixes", distractor_type="other_title"),
 T("D_DDLEGEND", "distractor", ["gdocs"], [DDNOTES], [], "R3", "a tick means passed on the store build", "that note is about Domino Delights lists", distractor_type="other_title"),
 T("D_SKIP", "distractor", ["slack"], [], [f"{BUGS}/1758903616.346579"], "R1", "the tutorial skip exceptions are reports to carry", "Brian's note leaves Oliver's skip work out, and a channel post is not something told to Calvin directly", distractor_type="scope_adjacent"),
 T("D_ICONVFX", "distractor", ["slack"], [], [f"{VDM}/1758721951.996909"], "R1", "Vincent's chat remark about the pass icon VFX is another report", "his sheet is his whole list", distractor_type="scope_adjacent"),
 T("D_COINDM", "distractor", ["slack"], [], [f"{BDM}/1758808900.412489"], "R1", "Brian's own line about the coin animation is a second report", "it is dated the 25th, before Vincent's pass, and it is row 5 already", distractor_type="already_done"),
 T("D_432", "distractor", ["linear"], [], ["ZOM-432"], "R4", "ZOM-432 is the daily gift ticket for row 11", "ZOM-432 is about the gift artwork frame; ZOM-556 carries Vincent's tie", distractor_type="near_duplicate_record"),
 T("D_OLDINVITE", "distractor", ["gmail"], [INV1], [], "R5", "the first invitation's list still stands", "the updated invitation replaces it", distractor_type="withdrawn_ask"),
 T("D_DECK", "distractor", ["gslides"], [DECK], [], "R2", "the deck's line is the status", "report records decide", distractor_type="stale_summary"),
 T("D_DDQUEUE", "distractor", ["linear"], [], ["ENG-2069"], "R1", "the DD queue manager tickets belong under the epic", "they are Domino Delights tickets on another team", distractor_type="keyword_collision"),
]
''')
block('port = [','channels = [','''port = [
 rule("BRANCH", "A24", "done_gap", "same mechanism: a done source (sheet ok, chat ok) with the missing piece in another place (the build's branch in #builds)", ["T_BRANCH"], "R3", "the sheet's ok is a pass", ["B1", "B2", "B3", "B4", "B5", "V1", "V2", "V4", "V5"], ["row 2", "row 3", "row 17"], "branch_over: un-passes a row whose ok was on a main build", "builds-channel", "main branch"),
 rule("INLINE", "A24", "done_gap", "same mechanism: a merged PR is the done source and the missing piece sits in an inline review comment", ["T_INLINE", "T_INLINE_PACK"], "R3", "a merged PR named in the sheet has the fix", ["I1", "I2", "I3", "I4", "I5", "V2", "V3"], ["row 18", "row 17"], "inline_over: drops the PR from a row no reviewer excepted", "github-inline", "not in this diff"),
 rule("REOPEN", "A11", "superseding", "same mechanism: a dated correction in a thread reply under an unrelated root", ["T_REOPEN"], "R3", "nr on a main build is a pass", ["R1", "R2", "R3", "V1", "V3"], ["row 7", "row 27"], "reopen_over: reopens another nr row", "unrelated-thread-reply", "on top of the gift again"),
 rule("ELSE", "A25", "completion_elsewhere", "same mechanism: an item that looks open while a record elsewhere shows the work done", ["T_ELSE"], "R3", "a blank Fix cell means no fix", ["E1", "E2", "E3", "E4", "V2", "V3"], ["row 14", "row 19"], "else_over: marks a row merged that no dev named", "owner-chat", "addressables/sp PR"),
 rule("MAIL", "A17", "exact_predicate", "same mechanism: an in-scope item outside the obvious list, brought in by the scope sentence", ["T_MAIL"], "R1", "the sheet is the whole list", ["M1", "M2", "M3", "V3", "V6"], ["the 38 sheet rows"], "mail_over: adds a mail that reports nothing", "gmail-inbox", "streak chest"),
 rule("FILT", "A17", "exact_predicate", "same mechanism, different carrier and author: a 1:1 chat no record points at", ["T_FILT"], "R1", "the sheet is the whole list", ["F1", "F2", "F3", "V3", "V7"], ["the 38 sheet rows"], "filt_over: adds a chat line that is not a bug seen in a build", "artist-chat", "icon glow"),
 rule("ALIAS", "A7", "scope_alias", "same mechanism: a row and an existing ticket named differently, tied by a dated note", ["T_ALIAS_GIFT", "T_ALIAS_STREAK"], "R4", "a blank Ticket cell means a new sub-issue", ["A1", "A2", "A3"], ["row 1", "row 38"], "alias_over: reuses a ticket for a row with none", "ticket-note", "Same thing"),
 rule("GATE", "A12", "authority", "same mechanism: the governing source sits in a rarely opened service and an older version is met first", ["T_GATE"], "R5", "Brian's line in the chat names what holds the review", ["G1", "G2", "V4"], ["row 15", "row 21"], "gate_over: none", "gmail-invitation", "Level-end rewards"),
]
''')
block(' "chains": [',' "traps": traps,',''' "chains": [
  {"id": "C1", "root_cause": "A24", "ends_in": "R3", "hops": [{"service": "gsheets", "record": SHEET, "finding": "row 5: fix #465, re-test ok, chat"}, {"service": "slack", "record": C_TESTED, "finding": "Calvin: #1718 already tested"}, {"service": "slack", "record": V_OK, "finding": "Vincent: looks ok"}, {"service": "slack", "record": B1718, "finding": "#1718 was built from the QueueManager branch"}, {"service": "trello", "record": RULE_ACT, "finding": "only builds of the main branch count"}]},
  {"id": "C2", "root_cause": "A11", "ends_in": "R3", "hops": [{"service": "gsheets", "record": SHEET, "finding": "row 9: nr on #1745"}, {"service": "slack", "record": B135, "finding": "Android Submission #135 built from main on 30 Sep"}, {"service": "slack", "record": REOPEN, "finding": "Vincent: it came up again on Submission 135"}]},
  {"id": "C3", "root_cause": "A25", "ends_in": "R3", "hops": [{"service": "gsheets", "record": SHEET, "finding": "rows 13 and 38: no fix named"}, {"service": "slack", "record": ELSE_DM, "finding": "Oliver: both went in with the addressables/sp PR"}, {"service": "github", "record": PR473, "finding": "Addressables/sp, merged 30 Sep 15:41 UTC"}]},
  {"id": "C4", "root_cause": "A7", "ends_in": "R4", "hops": [{"service": "gsheets", "record": SHEET, "finding": "row 11: no ticket"}, {"service": "linear", "record": "ZOM-556", "finding": "open base ticket under other words"}, {"service": "linear", "record": ALIAS_GIFT, "finding": "Vincent ties his row to it"}]},
  {"id": "C5", "root_cause": "A12", "ends_in": "R5", "hops": [{"service": "slack", "record": GATE_OLD, "finding": "Brian: Collect & Win and Daily Gift"}, {"service": "gmail", "record": INV1, "finding": "first invitation, same list"}, {"service": "gmail", "record": INV2, "finding": "updated: Collect & Win and Level-end rewards"}]},
  {"id": "C6", "root_cause": "A17", "ends_in": "R1", "hops": [{"service": "linear", "record": EPIC_NOTE, "finding": "any bug told to Calvin directly since the 26th"}, {"service": "gmail", "record": MAIL, "finding": "Robert's streak chest report"}, {"service": "slack", "record": FILT_DM, "finding": "Marcus's icon glow report"}]},
 ],
''')
rep('"R1": "population: every row of Vincent\'s pass sheet plus any report someone else on the team raised since 24 Sep about what shows on the home screen after a level"','"R1": "population: every row of Vincent\'s pass sheet plus any bug somebody else saw in a build and told Calvin about directly since 26 Sep about the home screen after a level"')
BS="\\\\"
SLOTS='''slots = [
 S("V1", "Passed count in the reply", 5, MS, "statuses joined across the sheet, #builds, Arthur's rule and a later reply", "write_content", ["text", "reply", "@b13@b"], ["BRANCH", "REOPEN"]),
 S("V2", "Waiting on QA count in the reply", 5, MS, "merged fixes joined with passes across GitHub, Slack and the sheet", "write_content", ["text", "reply", "@b6@b"], ["BRANCH", "ELSE", "INLINE"]),
 S("V3", "Waiting on a fix count in the reply", 5, MS, "what no merged PR has, across the sheet, mail, chats and GitHub", "write_content", ["text", "reply", "@b21@b"], ["REOPEN", "INLINE", "ELSE", "MAIL", "FILT"], "volume", volume_for=["plain"]),
 S("V4", "Holding the review count in the reply", 5, MS, "statuses joined with the areas on the updated invitation", "write_content", ["text", "reply", "@b7@b"], ["GATE", "BRANCH"]),
 S("V5", "Clear areas count in the reply", 3, CMP, "areas rolled up from report statuses", "write_content", ["text", "reply", "@b(1|one)@b"], ["BRANCH"]),
 S("V6", "Win Streak area shows 4 open reports", 5, MS, "area count joined across the pass sheet and a report that only came by mail", "write_content", ["text", "sheet", row("Win Streak", "@b4@b")], ["MAIL"]),
 S("V7", "Season Pass area shows 5 open reports", 5, MS, "area count joined across the pass sheet and a report that only came in a 1:1 chat", "write_content", ["text", "sheet", row("Season Pass", "@b5@b")], ["FILT"]),
 S("B1", "Back to back tutorials row is Waiting on QA", 5, MS, "sheet ok and chat ok against the build's branch and Arthur's rule", "direct", fld(1, "Status"), ["BRANCH"]),
 S("B2", "Coin animation row is Waiting on QA", 5, MS, "same join on a second row", "direct", fld(5, "Status"), ["BRANCH"]),
 S("B3", "Boss arena tutorial row is Waiting on QA", 5, MS, "same join on a third row", "direct", fld(25, "Status"), ["BRANCH"]),
 S("B4", "Coin animation sub-issue is filed In Validation", 3, IN, "state follows the status", "write_content", ["text", "issues", row("[Cc]oin animation", "In Validation")], ["BRANCH"]),
 S("B5", "Boss Arena area is Open", 5, MS, "area rolled up from a status that depends on the build's branch", "write_content", ["text", "sheet", row("Boss Arena", "Open")], ["BRANCH"]),
 S("R1", "Pass popup over the gift row is Waiting on a fix", 5, MS, "nr on a main build against a later reply in another thread", "direct", fld(9, "Status"), ["REOPEN"]),
 S("R2", "Its sub-issue is filed Todo", 3, IN, "state follows the status", "write_content", ["text", "issues", row("on top of the daily gift", "Todo")], ["REOPEN"]),
 S("R3", "Its Why names Submission 135", 3, IN, "the build it came back on, read from the reply", "direct", ["reason_matches", KEY[9], "135"], ["REOPEN"]),
 S("I1", "Pass icon restart row is Waiting on a fix", 5, MS, "merged PR in the sheet against the reviewer's inline comment", "direct", fld(12, "Status"), ["INLINE"]),
 S("I2", "ZOM-571 goes back to Todo", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-571", "Todo")], ["INLINE"]),
 S("I3", "Its Why says #472 does not have it", 3, IN, "reads the exception from the review", "direct", ["reason_matches", KEY[12], "472"], ["INLINE"]),
 S("I4", "Pack sound row is Waiting on a fix", 5, MS, "merged PR and In Validation ticket against the reviewer's inline comment", "direct", fld(32, "Status"), ["INLINE"]),
 S("I5", "ZOM-581 goes back to Todo", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-581", "Todo")], ["INLINE"]),
 S("E1", "Pass start popup row is Waiting on QA", 5, MS, "blank Fix cell and Todo ticket against the owner's chat and a merged PR", "direct", fld(13, "Status"), ["ELSE"]),
 S("E2", "Pass bar row is Waiting on QA", 5, MS, "same join on a second row", "direct", fld(38, "Status"), ["ELSE"]),
 S("E3", "Its Why names #473", 3, IN, "the PR read from the chat and GitHub", "direct", ["reason_matches", KEY[13], "473"], ["ELSE"]),
 S("E4", "ZOM-572 goes to In Validation", 3, IN, "state follows the status", "write_content", ["text", "updates", row("ZOM-572", "In Validation")], ["ELSE"]),
 S("M1", "Robert's streak chest report is in the sheet", 5, MS, "scope sentence joined with a mail", "direct", fld(39, "Status"), ["MAIL"]),
 S("M2", "A sub-issue carries it", 3, IN, "write follows the report", "write_content", ["text", "issues", "[Ss]treak chest"], ["MAIL"]),
 S("M3", "Its area is Win Streak", 3, IN, "area read from the report", "direct", fld(39, "Area"), ["MAIL"]),
 S("F1", "Marcus's icon glow report is in the sheet", 5, MS, "scope sentence joined with a 1:1 chat", "direct", fld(40, "Status"), ["FILT"]),
 S("F2", "A sub-issue carries it", 3, IN, "write follows the report", "write_content", ["text", "issues", "[Ii]con glow"], ["FILT"]),
 S("F3", "Its area is Season Pass", 3, IN, "area read from the report", "direct", fld(40, "Area"), ["FILT"]),
 S("A1", "Day counter row uses ZOM-556", 5, MS, "row tied to a base ticket under other words by a note", "direct", fld(11, "Ticket"), ["ALIAS"]),
 S("A2", "Freezer row uses ZOM-560", 5, MS, "row tied to a base ticket under other words by a note", "direct", fld(20, "Ticket"), ["ALIAS"]),
 S("A3", "Note on ZOM-556", 3, IN, "write on the reused ticket", "write_content", ["text", "comments", row("ZOM-556", "(fix|Waiting|Todo)")], ["ALIAS"]),
 S("G1", "Gift calendar row does not hold the review", 5, MS, "status joined with the updated invitation's areas", "direct", fld(10, "Holds review"), ["GATE"]),
 S("G2", "Coins over the pre-level panel row holds the review", 5, MS, "status joined with the updated invitation's areas", "direct", fld(6, "Holds review"), ["GATE"]),
 S("K1", "Plain sample: stars on tablets", 1, LK, "blank cells read from the sheet", "direct", fld(8, "Status"), role="sample", group="plain"),
 S("K2", "Plain sample: pass claim animation", 1, LK, "blank cells read from the sheet", "direct", fld(14, "Status"), role="sample", group="plain"),
 S("K3", "Plain sample: endless chest", 1, LK, "blank cells read from the sheet", "direct", fld(30, "Status"), role="sample", group="plain"),
 S("K4", "Plain sample: pack count", 1, LK, "blank cells read from the sheet", "direct", fld(34, "Status"), role="sample", group="plain"),
 S("K5", "Plain sample: freezer popup", 1, LK, "blank cells read from the sheet", "direct", fld(37, "Status"), role="sample", group="plain"),
 S("K6", "Passed on a main build: card upgrade tutorial", 3, CMP, "ok checked against the build's branch", "direct", fld(2, "Status")),
 S("K7", "Passed on a main build: event bar wait", 3, CMP, "ok checked against the build's branch and the merge time", "direct", fld(17, "Status")),
 S("K8", "Waiting on QA: event panel over rewards", 3, CMP, "merged PR with no re-test", "direct", fld(18, "Status")),
 S("K9", "Zombie Lane area is Clear", 3, CMP, "area rolled up from three passed rows", "write_content", ["text", "sheet", row("Zombie Lane", "Clear")]),
 S("K10", "Area children exist under the epic", 1, LK, "names from Brian's note", "write_content", ["text", "issues", "Endless Mode"]),
 S("K11", "A passed row with no ticket gets a Done sub-issue", 1, LK, "state from Brian's note", "write_content", ["text", "issues", row("[Cc]ard upgrade", "Done")]),
 S("K12", "A ticket moved under its child: ZOM-568", 1, LK, "parent set from the row's area", "write_content", ["text", "updates", "ZOM-568"]),
 S("K13", "Ticket key in a sheet row", 1, LK, "key copied from the pass sheet", "direct", fld(4, "Ticket")),
 S("D1", "Sheet in the folder", 1, LK, "destination named in the DM", "delivery", ["delivery", "register_parent", FOLDER]),
 S("D2", "Sheet shared with Brian and Vincent", 1, LK, "recipients named in the DM", "delivery", ["delivery", "share_reader", "brian.foster@harmonygames.co"]),
 S("D3", "Reply in Brian's DM", 1, LK, "destination named in the prompt", "delivery", ["link", "reply"]),
]
'''.replace("@b",BS+"b")
block('slots = [\n S("V1"','YES = {',SLOTS)
rep('SPAN_REPLY = "tell me here how many are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many hold the review"','SPAN_REPLY = "tell me here how many reports are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many reports hold the review"')
rep('"per_record_calls": 3.0, "records": 5','"per_record_calls": 3.0, "records": 4')
rep('and each of the five PRs named needs them','and each of the four PRs the rows or the devs name (#465, #472, #473, #475) needs them')
rep('("per-record", "github", 15, "body, reviews and inline comments of the five PRs the rows rest on")','("per-record", "github", 12, "body, reviews and inline comments of the four PRs the rows rest on")')
rep('("enumeration", "slack", 12, "who else raised a report since the 24th: recent 1:1 chats, #zombie-bugs with its threads")','("enumeration", "slack", 15, "what was told to Calvin directly since the 26th: each recent 1:1 chat, plus Vincent\'s later words in #zombie-bugs and its threads")')
rep('("enumeration", "gmail", 4, "mail to Calvin since the 24th")','("enumeration", "gmail", 4, "mail to Calvin since the 26th")')
rep('"per_record_floor": 45}','"per_record_floor": 40}')
rep('(20 ticket comment reads, 15 PR reads, 13 build lookups), so it is 45','(20 ticket comment reads, 12 PR reads, 13 build lookups), so it is 40')
rep('"count": 21, "depends_on": ["T_BRANCH", "T_REOPEN", "T_INLINE", "T_ALIAS_GIFT"]','"count": 21, "depends_on": ["T_INLINE", "T_INLINE_PACK", "T_ELSE", "T_ALIAS_GIFT"]')
rep('"count": 20, "depends_on": ["T_BRANCH", "T_REOPEN", "T_INLINE", "T_ALIAS_STREAK"]','"count": 20, "depends_on": ["T_INLINE", "T_ELSE", "T_ALIAS_GIFT", "T_ALIAS_STREAK"]')
rep('CLAIM = f"{VDM}/1759185612.507119"\n','')
open('build_scenario.py','w').write(s)
print('patched')

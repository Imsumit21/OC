#!/usr/bin/env python3
"""Builds the planned seed texts, the draft manifest and the gradable surface for owen_dd_bug_carryover (design only).
Seed texts are planned records for /create-injection, not prompt, Oracle Event or criterion text."""
import hashlib, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE)
ctx = json.load(open(os.path.join(WF, "00_Task_Context.json")))
h = lambda s, n=32: hashlib.sha256(s.encode()).hexdigest()[:n]
cid = lambda s: "comment_" + h("owen:" + s)
CANVAS, BUGS, BUILDS, SUB, BOOM = "CE156FDFB428", "C05V5FNLB9V", "C05433XK267", "C09Q4S613CN", "C09SWTHEMEW"
DM_A, DM_V, DM_B = "D05S1S2AB5M", "D05USBTQY1F", "D07E9PSQB6W"
HUB = f"{DM_A}/1770937805.214409"
VNOTE = f"{DM_V}/1765452012.418229"
BNOTE = f"{DM_B}/1765206644.602119"
BREPLY = f"{SUB}/1764606918.318209"
BARREPLY = f"{BUGS}/1767021345.207719"
DOC, DECOYDOC, DECK, FOLDER = "f_3ca9e15d7b20f4e681ad52", "f_72e0b4c3d91a5f68c2b7e4", "f_d15a8c70e3f2b94a61c8d3", "d_9b41e7c2a05d36f8e1c7a4"
MAIL = "owen.baker@harmonygames.co/1849333980856689601"
CARD, RULE_ACT = "690b27282f4c1b7a6e93d512", "690b29bc3c7d2e51b0f86a47"
ZMCARD, ZM_ACT = "68d282603e5f8d47a9c2e611", "68d284b84b7e9a3c5d16e208"
EVT = "evt_6e2c91d4b07f3a58c1d2e4"
AMEND, ALIAS_NOTE, SEASON_NOTE = cid("amend-2401"), cid("alias-2363"), cid("season-2428")
GIFT_NOTE = cid("gift-2437")
TD_NOTE, AXE_NOTE = "harmonygames-Games/GameOfDominoes#1905#c_3", "harmonygames-Games/GameOfDominoes#1908#c_3"
RC1, RC2 = "harmonygames-Games/GameOfDominoes#1905#rc_1", "harmonygames-Games/GameOfDominoes#1908#rc_1"
SEEDFLICK = "C09Q4S613CN/1766164222.418229"
SEED = {
 "hub": ("slack", HUB, "Arthur Blake", "2026-02-12T23:10:05Z", "hey, one thing before the next BoomBit sync. Once the data export is done Slack drops to the free plan and the history goes, and most of DD's bug tracking since the Unity 6 move only lives in there, Vincent's Android canvas and whatever came in after it. Linear stays through the transition, so I want the whole list moved over, the fixed ones too, that's the only record of what was done. I put you back on one of the paid seats so you can read the DD channels for this. How we call each one is in the carry-over notes doc I shared with you. While you're in there bring the UI Changes tree up to date, it never got closed out, and leave a line on every child saying where it landed. Put a sheet in your DD bug carry-over folder so I can look things up, and share it with everyone on Sunday's bug review. Then tell me here how many are still broken, how many new tickets you filed and how many of the 28 UI children are Done."),
 "rule_doc": ("gdocs", DOC, "Arthur Blake", "2026-02-12T22:48:00Z", "DD bug carry-over notes\n\nWhat goes over: every ticked or unticked line in the comment channel of Vincent's Android canvas, and every bug posted in the bug channel after the last line in that comment channel. A comment whose line was deleted has nothing to carry over. In the bug channel a follow-up on a bug already posted is part of that bug, and a design question for Leonard or a post that points at a QA doc isn't a bug post. Nothing else. Robert's reports in the sub-250 channel aren't part of this, Brian dealt with those at the time. The economy canvas and the ZM canvases stay where they are.\n\nOne Linear record per canvas line and one per bug posted after it. A canvas line and a later post stay separate even where they read alike. Take the first outcome that fits.\nFixed: the tick stands, or a later record says it was fixed. File it as Done.\nGone: it isn't fixed and it's a bug in something the build players have no longer has. File it as Canceled.\nCovered: it isn't fixed and an open ticket already covers it. Don't file a new one, add a note on that ticket with the canvas wording. Vincent tied a few lines to tickets before he left.\nBroken: anything else. File it as Bugs.\n\nWhat counts: we go by the Android build players have, 0.3.310, which came off the economy line, not by develop. A tick on the canvas stands unless a later record about that bug says otherwise. An unticked line, or a bug nobody closed, stays open unless a later record says it was fixed, and a commit named for the bug counts as that record if nothing later says otherwise. A fix only counts once it is in that build. A PR that never made it into that build doesn't count.\n\nNew tickets: Engineering team, Bug label, parent ENG-2401, title is the line without its tick box, or the first line of the post, as it was written, no assignee, nothing in the description. If anything changes after this I'll put it on the master ticket.\n\nUI tree: every open child goes Done unless a record shows a piece of its UI work never made it into that build or the screen is switched off there. Then it stays where it is. Children already Done stay Done and the masters stay as they are. A bug on a screen doesn't hold its child, that's what the bug ticket is for. Brian and Oliver left notes on some of the open children. Brian's closing rule from the UI work applies to the line on every child, Done or not.\n\nSheet columns: Bug, Outcome, Ticket, Why. When you report back, Covered ones count as still broken."),
 "decoy_doc": ("gdocs", DECOYDOC, "Brian Foster", "2025-09-24T14:10:00Z", "Zombie Match bug list notes\n\nZM bugs go on the ZOM team. A tick on a ZM canvas means QA passed it on iOS. Close-outs only need the ticket state."),
 "amend": ("linear", AMEND, "Arthur Blake", "2026-02-13T00:40:00Z", "For the carry-over: put [2231] at the front of every title you file so I can filter them."),
 "vincent_note": ("slack", VNOTE, "Marcus Bennett", "2025-12-11T11:20:12Z", "the Tavern buttons lost their frame again on last night's Android build, I looked at the prefab and Brian's fix didn't hold"),
 "brian_reply": ("slack", BREPLY, "Brian Foster", "2025-12-01T16:35:18Z", "I was back in the shop prefabs today, the round icons on the River Tile and Memory Tile shops are there again on the current build, so don't trust that tick"),
 "brian_dm": ("slack", BNOTE, "Brian Foster", "2025-12-08T15:10:44Z", "music plays normally on my side since your audio player change, and Nate's acid throw lines up again after my animation fix, Robert's two are sorted"),
 "bar_reply": ("slack", BARREPLY, "Brian Foster", "2025-12-29T15:15:45Z", "the new camera setup fixed it, the bottom bar and the top panel both show on the devices I have here, closing this one"),
 "mail": ("gmail", MAIL, "Vincent Parker", "2025-11-20T18:12:00Z", "Subject: sign in lines on my list\n\nThe Apple sync line on my Android list comes down to the same sync problem as ENG-2073, no need for anything new. Vincent"),
 "alias_note": ("linear", ALIAS_NOTE, "Vincent Parker", "2025-11-20T18:20:00Z", "Android still hits this: the manual sign-in line on my list gets stuck on loading after signing in, same thing as here."),
 "rule_comment": ("trello", RULE_ACT, "Brian Foster", "2025-11-05T10:41:00Z", "When we close these UI tickets out every one gets a note naming the current public build, otherwise nobody can tell later what players actually had."),
 "zm_comment": ("trello", ZM_ACT, "Brian Foster", "2025-09-23T11:30:00Z", "ZM close-outs just need the ticket state, no note."),
 "deck": ("gslides", DECK, "Brian Foster", "2025-11-21T20:30:00Z", "UI optimization wrap\n\nUI pass wrapped up. Core, Live-Ops and Mini-Games main screens are on the optimized sprites."),
 "season_note": ("linear", SEASON_NOTE, "Oliver Brooks", "2025-12-05T12:30:00Z", "The illustrations went in but the reward track still uses the old frames, this isn't finished."),
 "gift_note": ("linear", GIFT_NOTE, "Brian Foster", "2025-11-24T16:00:00Z", "Ran out of time on this one, the panel never got its last pass before the build went out."),
 "inline_td": ("github", RC1, "Arthur Blake", "2025-11-19T13:05:35Z", "Approving so we can keep moving, but the Tile Dozer how-to-play popup still points at the old sprites in this PR. That has to be swapped before the Tile Dozer ticket can close."),
 "inline_axe": ("github", RC2, "Arthur Blake", "2025-11-20T01:51:55Z", "Fine to merge, but the Axe Arena info popup keeps the old frame here. Needs doing before the Axe Arena ticket can close."),
 "flick_reply": ("slack", "C09Q4S613CN/1766164222.418229", "Robert", "2025-12-19T17:10:22Z", "the flickering is gone on this week's build, both on the play button and coming out of a level"),
 "train_reply": ("slack", f"{CANVAS}/1763845212.507119", "Vincent Parker", "2025-11-22T21:00:12Z", "better but the snow train is still off and the green shows, leaving this one open"),
 "team_reply": ("slack", f"{CANVAS}/1763742012.611229", "Vincent Parker", "2025-11-21T16:20:12Z", "the leave team popup is fine now but the navigation bar still goes after quitting"),
 "lives_reply1": ("slack", f"{CANVAS}/1763845812.703339", "Vincent Parker", "2025-11-22T21:10:12Z", "same after Oliver's change, a loss still doesn't take a life"),
 "lives_reply2": ("slack", f"{CANVAS}/1763845872.804449", "Vincent Parker", "2025-11-22T21:11:12Z", "same here, it still only drops on the second loss"),
 "invite": ("gcal", EVT, "Arthur Blake", "2026-02-12T23:05:00Z", "DD bug review, Sunday Feb 15 17:00 UTC. Attendees: Arthur Blake, Robert, Oliver Brooks, Owen Baker."),
}
q = lambda k, s: (s if s in SEED[k][4] else (_ for _ in ()).throw(SystemExit(f"quote not in {k}: {s}")))
base = lambda: dict(seeded_ids=[], base_pointers=[])
frag = lambda i, svc, cont, kind, via, seeded, bp, by, quote, reqs, **kw: dict(id=i, service=svc, container=cont, locator=cont, kind=kind, incorporated_via=via, seeded_ids=seeded, base_pointers=bp, delegated_by_record=by, delegation_quote=quote, requirement_ids=reqs, **kw)
frags = [
 frag("K1","gdocs",DOC,"delegation",["AN1"],[DOC],[],HUB,q("hub","the carry-over notes doc"),["R2","R3","R4","R5","R9"],names_authorities=[{"id":"H2","quote":q("rule_doc","Brian's closing rule from the UI work")}]),
 frag("K2","slack",CANVAS,"requirement",["AN1"],[],[f"{CANVAS}/1763041126.468099"],HUB,q("hub","Vincent's Android canvas"),["R1"]),
 frag("K3","slack",BUGS,"requirement",["AN1","K1"],[],[f"{BUGS}/1764256187.655299"],DOC,q("rule_doc","every bug posted in the bug channel after the last line in that comment channel"),["R1"]),
 frag("K4","linear","ENG-2401","amendment",["AN1","K1"],[AMEND],[],DOC,q("rule_doc","If anything changes after this I'll put it on the master ticket"),["R4"]),
 frag("K5","trello",CARD,"format",["AN1","K1"],[RULE_ACT],[],DOC,q("rule_doc","Brian's closing rule from the UI work"),["R6"]),
 frag("K6","gcal",EVT,"recipient",["AN1"],[EVT],[],HUB,q("hub","everyone on Sunday's bug review"),["R7"]),
 frag("K7","gdrive",FOLDER,"destination",["AN1"],[FOLDER],[],HUB,q("hub","your DD bug carry-over folder"),["R7"]),
 frag("K8","gmail",MAIL,"requirement",["AN1","K1"],[MAIL],[],DOC,q("rule_doc","Vincent tied a few lines to tickets before he left"),["R3"]),
 frag("K9","linear","ENG-2363","requirement",["AN1","K1"],[ALIAS_NOTE],[],DOC,q("rule_doc","Vincent tied a few lines to tickets before he left"),["R3"]),
 frag("K10","slack",BOOM,"requirement",["AN1","K1"],[],[f"{BOOM}/1770926214.816149"],DOC,q("rule_doc","which came off the economy line"),["R2"]),
 frag("K11","linear","ENG-2428","requirement",["AN1","K1"],[SEASON_NOTE],[],DOC,q("rule_doc","Brian and Oliver left notes on some of the open children"),["R5"]),
 frag("K12","linear","ENG-2437","requirement",["AN1","K1"],[GIFT_NOTE],[],DOC,q("rule_doc","Brian and Oliver left notes on some of the open children"),["R5"]),
]
vr = lambda service, rid, cont, seeded, at, **kw: dict(service=service, seeded=seeded, at=at, container=cont, **({"id": rid} if seeded else {"base_pointer": rid}), **kw)
T = lambda i, fam, svcs, seeded, bp, req, wrong, res, **kw: dict(id=i, family=fam, services=svcs, seeded_ids=seeded, base_pointers=bp, requirement=req, expected_wrong_reading=wrong, resolver=res, **kw)
traps = [
 T("T_INLINE_TD","done_gap",["github","linear","gslides"],[RC1,TD_NOTE,DECK],["harmonygames-Games/GameOfDominoes#1905"],"R5","ENG-2434 is finished: #1905 merged with Arthur's approval, Brian ticked the screen off and the wrap deck says shipped","Arthur's inline comment on #1905 says the how-to-play popup must be swapped before the ticket closes; the review body is silent",discovery_order="the merged PR and Brian's tick come back from the tree read; the inline comment needs github_get_pull_request_comments"),
 T("T_WINGS","eliminating_evidence",["slack","github"],[],["C9CA62B5180A/1765927876.696389"],"R5","ENG-2424 goes Done like the other merged children","Owen disabled Win & Collect on Dec 16, so that screen is not in the build; no re-enable is on record",discovery_order="the child reads as finished until the disable post or its commit is found"),
 T("T_INLINE_AXE","done_gap",["github","linear"],[RC2,AXE_NOTE],["harmonygames-Games/GameOfDominoes#1908"],"R5","ENG-2426 is finished: #1908 merged and Brian ticked the panel off","Arthur's inline comment on #1908 says the info popup keeps the old frame and must be done first",discovery_order="Brian's tick is read first; the inline comment sits behind a separate call"),
 T("T_SEASON","superseding",["gslides","linear"],[DECK,SEASON_NOTE],[],"R5","the wrap deck says the UI pass wrapped up, so ENG-2428 is Done","Oliver's later note on ENG-2428 says the reward track still uses the old frames",version_records=[vr("gslides",DECK,f"file:{DECK}",True,"2025-11-21T20:30:00Z"),vr("linear",SEASON_NOTE,"linear:ENG-2428",True,"2025-12-05T12:30:00Z")]),
 T("T_REPLY","superseding",["slack"],[BREPLY],[f"{CANVAS}/1763549455.195819"],"R2","the River Tile and Memory Tile shop icons line is ticked, so it is fixed","Brian's later reply under an unrelated sub-250 post says the round icons came back",discovery_order="the tick is read from the canvas; the reply sits under a gems question",version_records=[vr("slack",f"{CANVAS}/1763549455.195819",f"slack:{CANVAS}/1763549455.195819",False,"2025-11-19T10:50:55Z"),vr("slack",BREPLY,f"slack:{SUB}/1764042435.541279",True,"2025-12-01T16:35:18Z")]),
 T("T_BACK","superseding",["slack"],[VNOTE],[f"{CANVAS}/1763642831.967359"],"R2","the Tavern buttons line is ticked and Brian sent the fix, so it is fixed","Marcus's later 1:1 note to Owen says the frame was lost again and Brian's fix did not hold",discovery_order="the tick and Brian's fix are in the canvas thread; the note sits in a DM no anchor names",version_records=[vr("slack",f"{CANVAS}/1763642831.967359",f"slack:{CANVAS}/1763642831.967359",False,"2025-11-20T12:47:11Z"),vr("slack",VNOTE,f"slack:{VNOTE}",True,"2025-12-11T11:20:12Z")]),
 T("T_GONE","effective_date",["slack","gdocs"],[],[f"{CANVAS}/1763548856.943389",f"{BOOM}/1764659626.614679","f_948768f5a462e7037d17c9"],"R9","the unticked lives lines are still broken","the lives feature was removed: Leonard's BoomBit post, the economy doc and his Jan no-lives note; the live build has tickets",discovery_order="the unticked lines come first; the removal sits in another channel and a doc",version_records=[vr("slack",f"{CANVAS}/1763548856.943389",f"slack:{CANVAS}/1763548856.943389",False,"2025-11-19T10:40:56Z"),vr("slack",f"{BOOM}/1764659626.614679",f"slack:{BOOM}/1764659626.614679",False,"2025-12-02T07:13:46Z"),vr("gdocs","f_948768f5a462e7037d17c9","file:f_948768f5a462e7037d17c9",False,"2025-12-12T21:47:11Z")]),
 T("T_LINE","done_gap",["slack","github"],[],[f"{BUGS}/1764329192.159229","harmonygames-Games/GameOfDominoes#1913"],"R2","the tile dozer window is fixed: Marcus fixed it and did a PR","GameOfDominoes#1913 is still open and its commit is not in #1914's list, so the fix never reached that build",discovery_order="Marcus's reply reads as closed before any PR lookup"),
 T("T_ELSE_FLICKER","completion_elsewhere",["slack","github"],[SEEDFLICK],[f"{BUGS}/1764659550.713509",f"{BUILDS}/1765310004.760809"],"R2","the flicker thread ends at testing a fix now, so it is still broken","Robert's later reply under his sub-250 report says both flickers are gone, and the fix commit is on the economy line"),
 T("T_ELSE_MUSIC","completion_elsewhere",["slack"],[BNOTE],[f"{BUGS}/1764660142.352319"],"R2","Owen said he would check the music next and nothing closed it","Brian's DM to Owen says music plays normally since the audio player change"),
 T("T_ELSE_ACID","completion_elsewhere",["slack"],[BNOTE],[f"{BUGS}/1764661312.152719"],"R2","Brian's I'm checking is the last word on the acid delay","the same DM says the acid throw lines up after his animation fix"),
 T("T_ALIAS_APPLE","scope_alias",["slack","gmail","linear"],[MAIL],[f"{CANVAS}/1763041538.186339"],"R3","no ticket has the canvas wording, so a new one is filed","Vincent's mail ties the Apple sync line to ENG-2073"),
 T("T_ALIAS_SPLASH","scope_alias",["slack","linear"],[ALIAS_NOTE],[f"{CANVAS}/1763132009.017599"],"R3","no ticket has the canvas wording, so a new one is filed","Vincent's note on ENG-2363 ties the manual sign-in line to it"),
 T("T_FILT","exact_predicate",["slack"],[],[f"{BUGS}/1764256187.655299",f"{BUGS}/1766415326.501939"],"R1","the canvas is the whole list","the rule doc brings in bugs posted in the bug channel after the canvas's last line"),
 T("T_FOLLOW","authority",["trello","linear"],[RULE_ACT],[],"R6","any line on a child is enough","Brian's comment on the UI work card says every close-out note names the current public build"),
 T("D_ZMCANVAS","distractor",["slack"],[],["C3DD99314033/1758276844.870419"],"R1","the ZM Collect & Win canvas is part of the job","the rule doc leaves the ZM canvas where it is",distractor_type="scope_adjacent"),
 T("D_SIGNIN","distractor",["linear"],[],["ENG-2280"],"R3","ENG-2280 covers the Apple sign-in line","Vincent's mail names ENG-2073",distractor_type="near_duplicate_record"),
 T("D_LIVESTICKETS","distractor",["linear"],[],["ENG-2277","ENG-2400"],"R9","the open lives tickets mean those lines have a ticket","the feature is gone from the live build",distractor_type="keyword_collision"),
 T("D_ZMDOC","distractor",["gdocs"],[DECOYDOC],[],"R2","the ZM notes set how ticks and close-outs work","they cover the other game",distractor_type="other_title"),
 T("D_SUB250","distractor",["slack"],[],[f"{SUB}/1764013026.858409"],"R1","Robert's sub-250 reports are extra bugs","the rule doc leaves them out",distractor_type="scope_adjacent"),
 T("D_DECK","distractor",["gslides"],[DECK],[],"R5","the wrap deck proves the UI work finished","child records decide",distractor_type="stale_summary"),
 T("D_ECONCANVAS","distractor",["slack"],[],["C4208B207A1A/1765298859.629579"],"R1","the economy canvas is part of the list","the rule doc leaves it where it is",distractor_type="scope_adjacent"),
]
led = {}
for l in open(os.path.join(WF, "..", "..", "support", "hardness_ledger", "ledger.jsonl")):
    try: r = json.loads(l)
    except Exception: continue
    if str(r.get("model", "")).startswith("claude-opus-5-5") and r.get("family"): led.setdefault(r["family"], []).append(r.get("id"))
PRI = {"done_gap": (3.0, 3.0), "superseding": (1.0, 5.0), "completion_elsewhere": (1.0, 4.0), "scope_alias": (1.0, 4.0), "authority": (1.0, 1.0), "exact_predicate": (2.0, 4.0)}
def rule(i, m, fam, why, nodes, req, nat, dec, ctrl, over, src, sig):
    d = dict(id=i, mechanism=m, prior_family=fam, prior_family_reason=why, nodes=nodes, requirement=req, natural_reading=nat, decides=dec, controls=ctrl, over_application=over, source=src, signature=sig)
    if fam in PRI: d["prior"] = {"alpha": PRI[fam][0], "beta": PRI[fam][1], "record_ids": led.get(fam, [])[:10]}
    return d
port = [
 rule("INLINE","A24","done_gap","same mechanism: a merged PR is the done source and the missing piece sits in an inline review comment",["T_INLINE_TD","T_INLINE_AXE"],"R5","a merged PR with Brian's tick means the child is Done",["I1","I2","I3","I4","V4"],["ENG-2417","ENG-2432"],"inline_over: holds a child whose PR has no inline comment","github-inline","how-to-play popup"),
 rule("REPLY","A11","superseding","same mechanism: a dated correction in a thread reply under an unrelated root",["T_REPLY"],"R2","a ticked line is fixed",["B3","B4","V1","V3"],["the Purple bg line"],"reply_over: reopens another ticked line","unrelated-thread-reply","round icons"),
 rule("BACK","A11","superseding","same mechanism: a dated correction in a 1:1 DM off the delegation path",["T_BACK"],"R2","a ticked line is fixed",["B1","B2","V1","V3"],["the character frames line"],"back_over: reopens another ticked line","one-to-one-dm","Tavern buttons"),
 rule("FOLLOW","A15","authority","closest ledger family: a rule homed in a card comment off the named path; house_rule has no record",["T_FOLLOW"],"R6","any note on a child is enough",["O1","O2","O3"],["the moved children"],"follow_over: none","trello-comment","current public build"),
 rule("GONE","A15","exact_predicate","closest ledger family: a condition in older records changes which items qualify; house_rule has no record",["T_GONE","T_WINGS"],"R9","an unticked line is still broken",["G1","G2","G3","G4","V1","V3","V4"],["the team navigation line"],"gone_over: cancels a line that is not about lives","economy-change","no-lives"),
 rule("LINE","A24","done_gap","same mechanism: a done claim in one service with the missing piece in another",["T_LINE"],"R2","fixed and did a PR means it shipped",["L1","L2","V1","V3"],["the treasure button post"],"line_over: holds a post whose fix did land","open-pr","tile dozer window"),
 rule("ELSE","A25","completion_elsewhere","same mechanism: a thread left open while another record shows the work done",["T_ELSE_FLICKER","T_ELSE_MUSIC","T_ELSE_ACID"],"R2","a thread nobody closed is still broken",["E1","E2","E3","V1","V3"],["the mega tile post"],"else_over: closes a post nobody fixed","brian-dm-and-builds","audio player change"),
 rule("ALIAS","A7","scope_alias","same mechanism: a line and an existing ticket named differently, tied by a dated note",["T_ALIAS_APPLE","T_ALIAS_SPLASH"],"R3","no matching title means a new ticket",["A1","A2","A3","V2"],["the team navigation line"],"alias_over: reuses a ticket for a line with none","gmail-and-ticket-note","same thing as ENG-2073"),
]
channels = [dict(id=f"CH-{p['id']}", kind="scale", rule=p["id"], degrade="ch_miss", latent="member", family=p["prior_family"], source=p["source"], members=[n for n in p["nodes"]], description=p["natural_reading"]) for p in port]
reqs = {"R1":"population: every canvas line with a comment thread and every bug posted in the bug channel after it","R2":"outcome of each bug in the build players have: Fixed, Broken, Gone or Covered","R3":"a bug an open ticket already covers gets a note on that ticket and no new ticket","R4":"new ticket fields: Engineering team, Bug label, parent ENG-2401, title with the [2231] prefix, no assignee","R5":"state of each UI tree child: Done unless a record shows part of its screen never made it into the build players have","R6":"a note on every UI child naming the build it was checked on","R7":"index sheet with columns Bug, Outcome, Ticket, Why in the DD bug carry-over folder, shared with the review attendees","R8":"reply to Arthur in the DM with how many are still broken, how many new tickets and how many of the 28 UI children are Done","R9":"a bug in something the build players no longer have is filed Canceled"}
services = {
 "slack":{"role":"canvas lines, later bugs, hub, corrections","weight_reason":"the bug record and every correction live here"},
 "linear":{"role":"destination and tree","weight_reason":"every record is written here and the tree states are decided here"},
 "github":{"role":"PR truth","weight_reason":"open and merged PRs and inline review comments decide fixes and child states"},
 "gdocs":{"role":"rule doc and economy doc","weight_reason":"the outcomes and the lives removal are read here"},
 "gdrive":{"role":"destination folder","weight_reason":"the sheet goes in Owen's folder"},
 "gsheets":{"role":"index sheet","weight_reason":"the deliverable index"},
 "gslides":{"role":"sprint wrap deck","weight_reason":"the convincing done summary the child records overturn"},
 "trello":{"role":"closing rule","weight_reason":"Brian's rule sets what every child note must name"},
 "gmail":{"role":"alias note","weight_reason":"Vincent's mail ties the Apple sync line to its ticket"},
 "gcal":{"role":"share list","weight_reason":"the review invite fixes who the sheet is shared with"},
}
cohort = {"definition":"63 canvas lines with a comment thread, 7 bugs posted in the bug channel after the canvas's last line, and 32 UI tree records: 102 records","definition_source":[HUB,DOC],"key":"bug line or tree ticket","size":102,"evidence_surfaces":[
 {"service":"linear","tool":"linear_list_comments","per_record_calls":1.0,"records":32,"seeded":True,"seeded_ids":[SEASON_NOTE,GIFT_NOTE],"requirement":"R5","decides":"state of each UI tree child","why_no_bulk":"linear_list_issues returns no comments; each child's sign-off note needs its own linear_list_comments","short_circuit":"a child's state turns on its own note; the master checklist is unreliable (NB-14), so no other record decides it, and one search cannot page every child's comments"},
 {"service":"github","tool":"github_get_pull_request_reviews and github_get_pull_request_comments","per_record_calls":2.0,"records":13,"seeded":True,"seeded_ids":[RC1,RC2],"requirement":"R5","decides":"state of each UI tree child","why_no_bulk":"github_search_pull_requests does not return reviews or inline comments, and in:comments misses inline ones","short_circuit":"merged state does not decide a child; only the PR's own review surfaces show a held piece, and no search sweeps inline comments"},
 {"service":"linear","tool":"linear_list_issues by subject and linear_list_comments","per_record_calls":1.0,"records":15,"seeded":True,"seeded_ids":[ALIAS_NOTE],"requirement":"R3","decides":"a note on that ticket and no new ticket","why_no_bulk":"titles use other words, so each unticked line or later bug needs its own ticket search and comment read","short_circuit":"reuse cannot be decided from the canvas; the tie sits on or about the ticket"},
 {"service":"slack","tool":"slack_read_thread","per_record_calls":0.5,"records":70,"seeded":False,"requirement":"R2","decides":"outcome of each bug","why_no_bulk":"slack_read_channel returns roots without replies, and fixes and doubts sit in replies; a search can sweep some, so this surface counts at half","short_circuit":"the outcome needs the thread's last word on each line; a search for fixed misses replies in other words"},
]}
budget = [
 ("discovery","slack",4,"Arthur's DM, #prototype context, canvas channel lookup"),("discovery","gdocs",2,"rule doc read"),("discovery","gdrive",3,"folder and doc location"),("discovery","gcal",2,"review invite attendees"),("discovery","linear",6,"tree parents, statuses, labels, users"),("rules","trello",3,"finding Brian's closing rule"),
 ("enumeration","slack",14,"canvas pages, #god-bugs pages, #builds searches, BoomBit posts"),("enumeration","linear",4,"open ENG tickets"),("enumeration","github",6,"PR search for tree and bug fixes"),("enumeration","gdocs",2,"economy doc"),("enumeration","gmail",2,"sign-in mail search"),("enumeration","gslides",1,"wrap deck"),
 ("per-record","linear",47,"comments on 32 tree records and about 15 candidate tickets: each answers a distinct question"),("per-record","github",26,"reviews and inline comments on 13 merged PRs"),("per-record","slack",35,"thread reads on lines that need one"),
 ("per-record","linear",117,"one record per bug line, child moves and child notes: each is a distinct target with no batch form"),("writes","gsheets",3,"index sheet create and fill"),("writes","gdrive",2,"move and share"),("writes","slack",1,"reply to Arthur"),("read-back","linear",3,"confirm filed records"),("read-back","gsheets",2,"confirm the index"),
]
manifest = {
 "_note":"DRAFT manifest (scenario stage). Seeded ids are planned (plan/build_scenario.py, plan/seed_text.json); /create-injection writes the final manifest.",
 "persona":"owen_baker","assignment_context":{k:ctx.get(k) for k in ("context_hash","assignment_hash","policy_hash","freeze_utc")}|{"difficulty_mode":ctx.get("difficulty_mode")},
 "horizon":"Long Horizon","effective_profile":"extreme",
 "author_targets":{"calls_per_run":"over 130 in every run","average":"strictly under 80 %","design_target":"E[avg] <= 72 %","source":"requester, 2026-11-07"},
 "volume_exception":{"reason":"102 cohort records and about 285 honest calls; reaching 500 would need padding, which fails on its own","requester_confirmation":"requester, Claude Code chat 2026-11-07: 'i want over 130 tool calls in each runs ... you can choose from your self which option is best fit for my requirements in this task' (choice delegated; recorded in 00_Pre_Scenario_Analysis.md section 11, item 2)","call_budget_floor":250,"per_record_floor":100},
 "requirements":reqs,"services":services,
 "anchors":[{"id":"AN1","prompt_reference":"Arthur's DM from Thursday","service":"slack","locator":HUB,"requirement_ids":["R1","R5","R7","R8"]},{"id":"AN2","prompt_reference":"the UI Changes master ticket","service":"linear","locator":"ENG-2401","requirement_ids":["R5"]}],
 "ask_fragments":frags,
 "authorities":[
  {"id":"H1","name":"the carry-over notes doc","home_service":"gdocs","decoy_service":"gdocs","governs":["R2","R3","R4","R9"],"findable_query":"carry-over notes","seeded_ids":[DOC],"base_pointers":[],"decoy_seeded_ids":[DECOYDOC],"decoy_base_pointers":[],"decoy_scope":{"dimension":"game","decoy":"Zombie Match 3D","task":"Domino Delights"}},
  {"id":"H2","name":"Brian's closing rule from the UI work","home_service":"trello","decoy_service":"trello","governs":["R6"],"findable_query":"close these out","seeded_ids":[RULE_ACT],"base_pointers":[],"decoy_seeded_ids":[ZM_ACT],"decoy_base_pointers":[],"decoy_scope":{"dimension":"game","decoy":"Zombie Match 3D","task":"Domino Delights"}},
 ],
 "cohort":cohort,
 "chains":[
  {"id":"C1","root_cause":"A24","ends_in":"R5","hops":[{"service":"linear","record":"ENG-2434","finding":"child still shows PR and Brian ticked it off"},{"service":"github","record":"harmonygames-Games/GameOfDominoes#1905","finding":"merged with Arthur's approval"},{"service":"github","record":RC1,"finding":"inline comment holds the how-to-play popup"}]},
  {"id":"C2","root_cause":"A15","ends_in":"R9","hops":[{"service":"slack","record":f"{CANVAS}/1763548856.943389","finding":"unticked lives line"},{"service":"slack","record":f"{BOOM}/1764659626.614679","finding":"Leonard: removing lives"},{"service":"gdocs","record":"f_948768f5a462e7037d17c9","finding":"economy spec replaces lives with tickets"}]},
  {"id":"C3","root_cause":"A11","ends_in":"R2","hops":[{"service":"slack","record":f"{CANVAS}/1763642831.967359","finding":"ticked Tavern line"},{"service":"slack","record":f"{CANVAS}/1763642831.967359","finding":"Brian sent the fix"},{"service":"slack","record":VNOTE,"finding":"Marcus: lost the frame again"},{"service":"linear","record":"ENG-2401","finding":"the bug is filed as Bugs under the master"}]},
  {"id":"C4","root_cause":"A25","ends_in":"R2","hops":[{"service":"slack","record":f"{BUGS}/1764659550.713509","finding":"thread ends at testing a fix now"},{"service":"github","record":"harmonygames-Games/GameOfDominoes#1914","finding":"fix commit on the economy line"},{"service":"slack","record":f"{BUILDS}/1765310004.760809","finding":"change line in a submission build"}]},
  {"id":"C5","root_cause":"A7","ends_in":"R3","hops":[{"service":"slack","record":f"{CANVAS}/1763041538.186339","finding":"unticked Apple sync line"},{"service":"gmail","record":MAIL,"finding":"Vincent ties it to ENG-2073"},{"service":"linear","record":"ENG-2073","finding":"open ticket takes the note"}]},
 ],
 "traps":traps,"mechanism_portfolio":port,"channels":channels,
 "call_budget":[{"phase":a,"service":b,"calls":c,"reason":d} for a,b,c,d in budget],
 "writes":[
  {"service":"linear","tool":"linear_create_issue","count":68,"depends_on":["T_GONE","T_LINE","T_REPLY","T_BACK","T_ELSE_FLICKER","T_ALIAS_APPLE"],"requirements":["R1","R2","R4","R9"]},
  {"service":"linear","tool":"linear_create_comment","count":30,"depends_on":["T_ALIAS_APPLE","T_ALIAS_SPLASH","T_FOLLOW"],"requirements":["R3","R6"]},
  {"service":"linear","tool":"linear_update_issue","count":14,"depends_on":["T_INLINE_TD","T_INLINE_AXE","T_SEASON","T_WINGS"],"requirements":["R5"]},
  {"service":"gsheets","tool":"gsheets_values_update","count":3,"depends_on":["T_GONE","T_ALIAS_APPLE"],"requirements":["R7"]},
  {"service":"gdrive","tool":"gdrive_share_file","count":3,"depends_on":["K6"],"requirements":["R7"]},
  {"service":"slack","tool":"slack_send_message","count":1,"depends_on":["T_GONE","T_INLINE_TD","T_ALIAS_APPLE"],"requirements":["R8"]},
 ],
 "hazard_acknowledgements":[
  {"hazard_id":"L01","resolution":"dated_claim","why_safe":"the SQL leaves ticket state alone; Arthur says the tree never got closed out, so PR on a merged ticket is the stale status the job reconciles","requirement":"R5"},
  {"hazard_id":"L07","resolution":"dated_claim","why_safe":"the SQL leaves ticket state alone; moving these children is the job","requirement":"R5"},
  {"hazard_id":"L03","resolution":"dated_claim","why_safe":"the SQL leaves ENG-2405 alone; the rule doc keeps the masters as they are","requirement":"R5"},
 ],
 "denied_probes":[],"gradable_surface":"01_Gradable_Surface.json",
}
TXT = "[ -~\\u00a0-\\uffff]"
def S(i, title, w, kind, reason, cls, sel, mech=None, role="core", **kw):
    d = dict(id=i, title=title, weight=w, work_kind=kind, work_reason=reason, **{"class": cls}, selector=sel, role=role, mechanisms=mech or [])
    d.update(kw); return d
MS, LK, IN, CMP = "multi_source_reconciliation", "lookup", "interpretation", "comparison"
row = lambda word, out: f"({word}){TXT}{{0,240}}{out}"
slots = [
 S("V1","Broken count in the sheet",5,MS,"counts outcomes joined across the canvas, builds, DMs and PRs","aggregate",["total","Broken"],["GONE","LINE","BACK","REPLY","ELSE"]),
 S("V5","Fixed count in the sheet",3,CMP,"ticked lines and closed bugs counted against the rule","aggregate",["total","Fixed"],["BACK","REPLY","ELSE"],"volume",volume_for=["ticked"]),
 S("V2","New tickets in the reply",5,MS,"line count less reuse decided across Slack, mail and Linear","write_content",["text","reply","\\b68\\b"],["ALIAS"]),
 S("V3","Still broken in the reply",5,MS,"same outcomes plus the two reused tickets","write_content",["text","reply","\\b9\\b"],["GONE","LINE","BACK","REPLY","ELSE"]),
 S("V4","UI children Done in the reply",5,MS,"tree states joined across Linear and GitHub","write_content",["text","reply","\\b23\\b"],["INLINE","GONE"],"volume",volume_for=["moves"]),
 S("I1","ENG-2434 note says it stays open",5,MS,"inline review on a merged PR against Brian's tick and the deck","write_content",["text","comments",row("ENG-2434|tile dozer","(stay|open|not done|held|popup)")],["INLINE"]),
 S("I2","ENG-2426 note says it stays open",5,MS,"inline review on a merged PR against Brian's tick","write_content",["text","comments",row("ENG-2426|axe arena","(stay|open|not done|held|popup)")],["INLINE"]),
 S("I3","ENG-2434 note names the popup",3,LK and IN,"reads the held piece from the review","write_content",["text","comments","how.to.play"],["INLINE"]),
 S("I4","ENG-2426 note names the popup",3,IN,"reads the held piece from the review","write_content",["text","comments","info popup"],["INLINE"]),
 S("B1","Tavern buttons line is Still broken",5,MS,"canvas tick against a later DM","direct",["text","sheet",row("tavern","(broken|bugs)")],["BACK"]),
 S("B2","Tavern record filed as Bugs",3,IN,"state follows the outcome","write_content",["text","issues",row("tavern",'"?state"?[: ]+"?Bugs')],["BACK"]),
 S("B3","Shop icons line is Still broken",5,MS,"canvas tick against a reply under another post","direct",["text","sheet",row("rivertile|river tile","(broken|bugs)")],["REPLY"]),
 S("B4","Shop icons record filed as Bugs",3,IN,"state follows the outcome","write_content",["text","issues",row("rivertile|river tile",'"?state"?[: ]+"?Bugs')],["REPLY"]),
 S("G1","Lives after a loss line is Gone",5,MS,"line against the economy change and the live build","direct",["text","sheet",row("lives are not decreased","gone")],["GONE"]),
 S("G2","Losing twice line is Gone",5,MS,"line against the economy change and the live build","direct",["text","sheet",row("losing twice","gone")],["GONE"]),
 S("G3","Character change line is Gone",3,IN,"same rule on a third line","direct",["text","sheet",row("change the character","gone")],["GONE"]),
 S("G4","ENG-2424 note says it stays open",3,IN,"disable post read against the tree","write_content",["text","comments",row("ENG-2424|wings","(stay|open|not done|disabled|off)")],["GONE"]),
 S("L1","Tile dozer window is Still broken",5,MS,"Slack claim against the open PR","write_content",["text","sheet",row("window","(broken|bugs)")],["LINE"]),
 S("L2","Its row names the open PR",3,IN,"PR status read from GitHub","write_content",["text","sheet",row("window","1913")],["LINE"]),
 S("E1","Flicker bug is Fixed",5,MS,"open thread against the commit and build log","direct",["text","sheet",row("flicker","(fixed|done)")],["ELSE"]),
 S("E2","Music bug is Fixed",5,MS,"open thread against Brian's DM and the audio change","direct",["text","sheet",row("music","(fixed|done)")],["ELSE"]),
 S("E3","Acid delay is Fixed",3,IN,"open thread against Brian's DM","direct",["text","sheet",row("acid","(fixed|done)")],["ELSE"]),
 S("A1","Apple sync line uses ENG-2073",5,MS,"line tied to a ticket by a mail","write_content",["text","sheet",row("apple","ENG-2073")],["ALIAS"]),
 S("A2","Manual sign-in line uses ENG-2363",5,MS,"line tied to a ticket by a note","write_content",["text","sheet",row("manual sign","ENG-2363")],["ALIAS"]),
 S("A3","Note on ENG-2073",3,IN,"write on the reused ticket","write_content",["text","comments","[Aa]pple"],["ALIAS"]),
 S("O1","Child notes name the build",5,MS,"rule from a card comment across every child note","write_content",["text","comments","0\\.3\\.310"],["FOLLOW"]),
 S("O2","A moved child's note names the build",3,IN,"sample note","write_content",["text","comments",row("ENG-2417","0\\.3\\.310")],["FOLLOW"]),
 S("O3","A held child's note names the build",3,IN,"sample note","write_content",["text","comments",row("ENG-2428|season pass","0\\.3\\.310")],["FOLLOW"]),
 S("F1","Mega tile bug is Still broken",3,CMP,"a later post with no fix anywhere","direct",["text","sheet",row("mega","(broken|bugs)")]),
 S("F2","Bottom bar bug is Fixed",3,IN,"later post closed in its own thread","direct",["text","sheet",row("bottom bar","(fixed|done)")]),
 S("F3","Treasure button bug is Fixed",3,IN,"later post closed in its own thread","direct",["text","sheet",row("treasure","(fixed|done)")]),
 S("K1","Ticked sample: offers no visuals",1,LK,"tick read from the canvas","direct",["text","sheet",row("offers has no visuals","(fixed|done)")],role="sample",group="ticked"),
 S("K2","Ticked sample: Teams addressable",1,LK,"tick read from the canvas","direct",["text","sheet",row("teams addressable","(fixed|done)")],role="sample",group="ticked"),
 S("K3","Ticked sample: top hud",1,LK,"tick read from the canvas","direct",["text","sheet",row("top hud","(fixed|done)")],role="sample",group="ticked"),
 S("K4","Ticked sample: Streak Fever text",1,LK,"tick read from the canvas","direct",["text","sheet",row("streak fever","(fixed|done)")],role="sample",group="ticked"),
 S("K5","Ticked sample: Win & Collect null ref",1,LK,"tick read from the canvas","direct",["text","sheet",row("null ref","(fixed|done)")],role="sample",group="ticked"),
 S("K6","Train backgrounds line carried",3,IN,"commit then a later reply saying it is still off","direct",["text","sheet",row("train level","(broken|bugs)")]),
 S("K7","Team navigation line carried",3,IN,"commit then a later reply saying it still happens","direct",["text","sheet",row("navigation bar disappears","(broken|bugs)")]),
 S("K8","Lost level errors line carried",3,IN,"unticked with no later record","direct",["text","sheet",row("backend errors","(broken|bugs)")]),
 S("K9","Child moved: ENG-2417",1,LK,"merged child set to Done","write_content",["text","updates",row("ENG-2417","Done")],role="sample",group="moves"),
 S("K10","Child moved: ENG-2418",1,LK,"merged child set to Done","write_content",["text","updates",row("ENG-2418","Done")],role="sample",group="moves"),
 S("K11","Child moved: ENG-2425",1,LK,"merged child set to Done","write_content",["text","updates",row("ENG-2425","Done")],role="sample",group="moves"),
 S("K12","Child moved: ENG-2432",1,LK,"merged child set to Done","write_content",["text","updates",row("ENG-2432","Done")],role="sample",group="moves"),
 S("K13","Child moved: ENG-2410",1,LK,"merged child set to Done","write_content",["text","updates",row("ENG-2410","Done")],role="sample",group="moves"),
 S("K15","Tickets on the Engineering team",1,LK,"field from the rule doc","write_content",["text","issues",'"team": "(ENG|Engineering)"']),
 S("K16","Tickets take the title prefix",1,LK,"field from the amendment","write_content",["text","issues","\\[2231\\]"]),
 S("K17","Ticket key in a sheet row",3,IN,"row joined to the filed ticket","write_content",["text","sheet","ENG-24[4-9][0-9]|ENG-25[0-9]{2}"]),
 S("D1","Sheet in the folder",1,LK,"destination named in the DM","delivery",["delivery","register_parent",FOLDER]),
 S("D2","Reply in Arthur's DM",1,LK,"destination named in the prompt","delivery",["link","reply"]),
]
for s in slots:
    if s["id"] == "I3": s["work_kind"] = IN
FIELD_SLOTS = {"B1":"Tavern buttons lost its frame","B3":"shops from rivertile and memory tile has weird shop","G1":"I found the issue lives are not decreased after","G2":"Lives are only decreased after losing twice in a","G3":"When I change the character it just adds 1",
 "L1":"tile dozer window background","E1":"flickering","E2":"music plays only sometimes","E3":"acid animation delay","F1":"mega tile missing a face","F2":"android bottom bar invisible","F3":"treasure button opens axe arena",
 "K1":"offers has no visuals","K2":"Teams addressable doesn t work","K3":"top hud","K4":"Streak Fever has overflowing text on its pop up","K5":"Win & Collect gives a null ref every time","K6":"train level backgrounds are broken",
 "K7":"When I created a team and quitted it the","K8":"When I lost a level I got some backend"}
TICKET_SLOTS = {"A1":"In general I cannot sync and sign in with","A2":"On android manual sign-in has an issue after the"}
for s in slots:
    if s["id"] in FIELD_SLOTS:
        s["class"] = "direct"; s["selector"] = ["field", FIELD_SLOTS[s["id"]], "Outcome"]
    if s["id"] in TICKET_SLOTS:
        s["class"] = "direct"; s["selector"] = ["field", TICKET_SLOTS[s["id"]], "Ticket"]
surface = {"kind":"GRADABLE_SURFACE","version":1,"task":"owen_dd_bug_carryover","revision":"design-1","classes":["Broken","Fixed","Gone","Covered"],"truth_fields":{"class":"Outcome","groups":"groups"},
 "deliverables":{
  "sheet":{"kind":"table","name_regex":"(?i).*(carry|bug|index|canvas|dd).*","key_column":"Bug","key_regex":"(?:Bug 1|[A-Za-z][A-Za-z0-9 .()&/-]*)","columns":["Bug","Outcome","Ticket","Why"],"class_column":"Outcome","reason_column":"Why","comparators":{"Outcome":"yes_no"},"yes_no":{"Broken":["Broken","Still broken","Bugs","Open"],"Fixed":["Fixed","Done"],"Gone":["Gone","Canceled","Cancelled"],"Covered":["Covered","Has a ticket","Existing ticket","Reused"]}},
  "reply":{"kind":"json_text","tool":"slack_send_message"},"issues":{"kind":"json_text","tool":"linear_create_issue"},"comments":{"kind":"json_text","tool":"linear_create_comment"},"updates":{"kind":"json_text","tool":"linear_update_issue"}},
 "slots":slots}
json.dump({k:{"service":v[0],"id":v[1],"author":v[2],"at":v[3],"text":v[4]} for k,v in SEED.items()}, open(os.path.join(HERE,"seed_text.json"),"w"), indent=1)
for t_ in manifest["traps"]:
    for v_ in t_.get("version_records") or []:
        if v_.get("base_pointer") == "f_948768f5a462e7037d17c9":
            v_["base_pointer"] = "gdocs:data.json /docs_documents/371"
json.dump(manifest, open(os.path.join(WF,"01_Hardness_Manifest.draft.json"),"w"), indent=1)
json.dump(surface, open(os.path.join(WF,"01_Gradable_Surface.json"),"w"), indent=1)
tot = sum(s["weight"] for s in slots); fl = sum(s["weight"] for s in slots if s["mechanisms"])
print("slots",len(slots),"weight",tot,"flippable",fl,round(fl/tot,3),"budget",sum(b[2] for b in budget))

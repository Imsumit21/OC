#!/usr/bin/env python3
"""Build Working_Files/01_Gradable_Surface.json for julia-zm3d-beta-liveops-calendar (scenario stage).

Two table deliverables in Julia's seeded calendar sheet (Calendar tab keyed by beat, Pushes tab keyed by push), the DM
reply, the Linear comments and the reply to Brian. Re-run after any design change:
  python3 -B Task_Authoring/task_inputsS/Working_Files/research/scripts/build_surface.py

Local decoding caveats (forensics only; the platform grades with the rubric): keys match exactly, and the native-Sheet
decoder keys grids by spreadsheet id, not by tab — both are hand-normalized in /create-hardening (design §19).

Revision 2 (SQL 3afbf7cb…): Frederick's follow-up under his ask takes Zombie Lane off the calendar (seven beats, slot
C03 dropped) and makes the push plan the ten beta rows of the PNs Beta tab (the four off-beta rows left off, new
volume slot V02); Lives recharged / 7-day lapse are sent because the follow-up says copy that names no game is fine
(P04/P05 are exceptions of R_ASK_FOLLOWUP).

Revision 4 (SQL c955d6ca…): no slot id, title, selector, weight, mechanism or accepted outcome changes. Seven work
reasons are reworded because they named records that moved or states that changed: S02 and W03 (Robert's retraction is
a top-level DM message), S07 (ZOM-432 is Done), S08 (the vial note is on #468), S09 (the premium-strip note is on
#473), S11 (Marcus's second note on ZOM-465) and W06 (the brief now says the owner is told in a reply on the mail
where they committed to the date).

Revision 5 (SQL 3c035f2a…): 30 slots, weight 102 (31 / 111 before).
  S06 is dropped: the Quests still-to-do is empty (the quest note says the current set carries the first week) and
      no slot reads that cell. The id is not reused.
  S07 is re-classified from multi-source reconciliation (5) to lookup (1): Samuel's frame note is on the ticket it
      closes, so ZOM-432 alone (Done, with its own closing note) settles the empty Daily Login still-to-do.
  S08 reads "the final vial models (Claire)" (Arthur's note names Claire's 3D vial models); its regex is `vial`.
  W06's selector follows Brian's new Message-ID. S09 and S01 work reasons follow the re-worded notes.

Revision 8 (SQL 0e8c8ad8…): no slot id, title, selector, weight, mechanism or accepted outcome changes. S09's work reason
follows the premium-strip note to its new carrier, an inline note on #472 left before that merge.

Revision 9 (SQL 892f7edd…): 30 slots, weight 102, no id, title, selector, weight or mechanism changes. S04, S05 and C01 also
accept "In", because the brief asks whether those beats are in. The Pushes table follows the seeded headers (key column
"Push name"; "Send (UTC or trigger)", "Send or hold", "What is missing"), and "Finish first tutorial", the row's Details
text on the base push sheet, now matches the key regex. Work reasons follow the closed still-to-do rule, the de-named
withdrawal and the re-worded late-start sentence.

Revision 10 (SQL ffbac458…): 30 slots, weight 102, no id, title, selector, weight or mechanism changes. C05 also accepts
"Starts late". No slot reads the cells whose values changed in truth (the owners, Weeks running for Quests and Daily
Login), so none needs a new accepted outcome.

Revision 11 (SQL 1348d287…): 30 slots, weight 102, no id, title, selector, weight, mechanism or accepted-outcome changes.
S11's reason names Brian's note on ZOM-465 (cmt_zom465_3) and S05's follows the brief's "same beat" wording. No truth value
changes, so no slot needs anything else.

Revision 12 (SQL b5ccbfa5…): 30 slots, weight 102, no id, title, selector, weight, mechanism or accepted-outcome changes. S08's
reason says the final vials are needed before the beta. No slot reads the three cells filled in truth (Weekly Leagues' First
window and Weeks running, Season Pass's First window), so none needs a new accepted outcome.

Revision 13 (SQL 1f2175a2…): 30 slots, weight 102, no id, title, selector, weight, mechanism or accepted-outcome changes. S08's
and S11's reasons follow the notes' new words. S08 is still "the final vial models (Claire)" and its regex is still `vial`.

Revision 14 (SQL edae63f3…): 30 slots, weight 102, no id, title, selector, weight, mechanism or accepted-outcome changes. W06's
reason follows the brief's "you tell its owner".
"""
import json
from pathlib import Path

WF = Path(__file__).resolve().parents[2]

BEATS = ["Plague Race", "Collect & Win", "Season Pass", "Endless Monster Mode", "Weekly Leagues", "Quests", "Daily Login"]
# The ten beta rows of the base "PNs Beta" tab, as the solver keys them (solver.PUSHES), and the four rows Frederick's
# follow-up leaves off.
PUSHES = ["1-day lapse", "D0-1 FTUE", "Plague Race start", "Lives recharged", "7-day lapse", "Weekly Leaderboard reset",
          "Quests rollover push", "Win & Collect event start", "Login Calendar update", "Season Pass activation"]
# Zombie Lane / Trophy Path is no beat any more, but BEAT_RX still matches it on purpose: an extra Zombie Lane row is
# decoded as a calendar key and V01 (exactly the seven beats) catches it.
BEAT_RX = (r"(?i)(?:plague race|collect (?:&|and) win|season pass|endless(?: monster mode)?|weekly leagues?|leagues?|"
           r"weekly leaderboards?(?! reset)|zombie lane|trophy path|quests?(?: rollover)?|daily login(?: calendar)?|"
           r"login calendar|daily gifts?)")
# strict + disjoint from BEAT_RX so each table decodes its own sheet even when both are seeded (title unknown to the
# decoder) or written as two ranges: no beat name matches a push key and no push key matches a beat name. The beat
# "Weekly Leagues" and the push "Weekly Leaderboard reset" share "weekly leaderboard", so the beat alias excludes
# "... reset" (lookahead) and the push key carries the distinctive "reset".
# Revision 2: the four Not Ready rows that stay on the plan carry a distinctive push suffix ("... push", "... event
# start", "... update", "... activation"), so "Quests", "Login Calendar" and "Season Pass" alone still decode as beats
# only. The four rows the follow-up leaves off (Hourly Coins, Nathan's Treasure Hunt, Streak Fever, Axe Arena) match
# on purpose: an extra row for any of them is decoded as a push key and V02 (exactly the ten beta rows) catches it.
PUSH_RX = (r"(?i)(?:\d{1,2}[- ]?days?[- ]?lapse(?:d)?|d0[- ]?1(?: ftue)?|ftue|lives recharged|"
           r"finish first tutorial|plague race start(?: push)?|weekly leaderboard reset(?: push)?|"
           r"quests? rollover push|win (?:&|and) collect(?: event)?(?: start)?(?: push)?|"
           r"login calendar update(?: push)?|season pass activation(?: or reward unlock)?(?: push)?|"
           r"hourly coins(?: push)?|(?:nathan['’]?s )?treasure hunt(?: event)?(?: start)?(?: push)?|"
           r"streak fever(?: event)?(?: start)?(?: push)?|axe arena(?: event)?(?: start)?(?: push)?)")
CAL_COLS = ["Beat", "First window (UTC)", "Weeks running", "Status", "Still to do (owner)"]
PUSH_COLS = ["Push name", "Send (UTC or trigger)", "Send or hold", "What is missing"]
RUN = ["Runs", "Run", "Go", "Live", "Running"]
IN = RUN + ["In"]          # the brief asks whether the quest rollover, the daily gift and Plague Race are in
HOLD = ["Held", "Hold", "On hold", "Paused"]
ASK_TS = "1759263617.418209"
FRED_DM = "D05SD5QLG94"
M2 = "julia.lawson@harmonygames.co/<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>"


def slot(sid, title, weight, kind, reason, cls, role, selector, fact, mech=None, by=None, group=None, **extra):
    s = {"id": sid, "title": title, "weight": weight, "work_kind": kind, "work_reason": reason, "class": cls,
         "role": role, "selector": selector, "fact_id": fact}
    if group:
        s["group"] = group
    if mech:
        s["mechanisms"] = mech
    if by:
        s["singled_out_by"] = by
    s.update(extra)
    return s


MS, LR, INT, LK = "multi_source_reconciliation", "limited_reconciliation", "interpretation", "lookup"
SLOTS = [
    # ---------------------------------------------------------------- Calendar: the designed exceptions
    slot("S01", "Collect & Win first window is Fri Oct 10 00:00 UTC", 5, MS,
         "the merged client PRs and Julia's own 'feature completed' note must be weighed against Arthur's inline note on "
         "#470, left with his approval just before the merge (server windows on dev only), Douglas's Oct 8 release event (18:00 Europe/Istanbul = 15:00 UTC, after the "
         "Wed-Thu window opens 00:00 UTC) and the brief's Mon-Tue / Wed-Thu / Fri-Sun cadence, which compose to the first "
         "clean post-deploy window", "direct", "exception", ["field", "Collect & Win", "First window (UTC)"],
         "cw.first_window", ["R_DONE_DEPLOY"], "H3", "exception",
         accepted_outcomes=["Fri Oct 10 00:00 UTC", "Oct 10 00:00 UTC", "2025-10-10 00:00 UTC", "2025-10-10T00:00:00Z",
                            "Fri Oct 10, 00:00 UTC", "Thu Oct 9 5:00 PM PDT", "Thu Oct 9 2025 5:00 PM PDT",
                            "Oct 10 00:00 UTC (Thu Oct 9 17:00 PDT)", "Fri Oct 10 03:00 Istanbul (00:00 UTC)", "2025-10-10T00:00:00+00:00", "Fri Oct 10 2025 00:00 UTC", "Friday, October 10, 2025 at 00:00 UTC"]),
    slot("S02", "Plague Race runs all four weeks, the Halloween week included", 5, MS,
         "Robert's approval in Martin's #zombie-art thread must be weighed against his later message in his DM with "
         "Julia (a top-level message since revision 4, which since revision 9 calls it the themed prop set he okayed in "
         "Martin's thread), under the brief's one-off rule (the Product owner's latest dated call)", "direct", "exception",
         ["field", "Plague Race", "Weeks running"], "plague.weeks", ["R_WITHDRAWN"], "K4", "exception",
         accepted_outcomes=["All four weeks", "All 4 weeks", "Weeks 1-4", "Oct 6 - Nov 2", "Mon Oct 6 - Sun Nov 2",
                            "Oct 6 – Nov 2 (all four weeks)"]),
    slot("S03", "Weekly leagues are held", 5, MS,
         "Douglas's restart note on ZOM-429 and the Sep 22 thread ending 'working fine' must be weighed against Vincent's "
         "Sep 30 re-test post in #zombie-match3d, under the brief's even-after-a-restart hold rule", "direct",
         "exception", ["field", "Weekly Leagues", "Status"], "leagues.status", ["R_TECH_HOLD"], "K3", "exception",
         accepted_outcomes=HOLD),
    slot("S04", "Quests rollover is on the calendar and runs", 5, MS,
         "the brief's scope (every window, reset or start push) must be applied to the quests rollover nobody lists as an "
         "event, with its push row, and ZOM-534's restart-clearing fault read as a known issue under the hold rule",
         "direct", "exception", ["field", "Quests", "Status"], "quests.status", ["R_SCOPE_BEATS"], "K1",
         "exception", accepted_outcomes=IN),
    slot("S05", "Daily login (the daily gift) is on the calendar and runs", 5, MS,
         "the same scope applied to the daily gift (Login Calendar on the push sheet, same beat), with ZOM-556's streak "
         "fault (claiming works) read as a known issue under the hold rule", "direct", "exception",
         ["field", "Daily Login", "Status"], "login.status",
         ["R_SCOPE_BEATS"], "K1", "exception", accepted_outcomes=IN),
    # S06 (Quests still to do: the new quest set with the Mon Oct 13 rollover) was dropped in revision 5.
    slot("S07", "Daily login has nothing left to do (the gift frame shipped)", 1, LK,
         "one ticket settles it since revision 5: ZOM-432 is Done and its own last note (Samuel, Sep 30) says the frame "
         "went out with PR #471 and is in both submission builds from that day (iOS 50, Android 135); Calvin's older "
         "note on the same ticket (Sep 24: still needed) is overtaken by the ticket's own state. A run that lists open "
         "issues never meets the ticket and leaves the cell empty anyway. A literal read of one record, so weight 1 "
         "(it was a weight-5 multi-source reconciliation while the completion was recorded on PR #471 and in #builds)", "direct",
         "exception", ["field", "Daily Login", "Still to do (owner)"], "login.todo",
         ["R_SCOPE_BEATS", "R_DONE_ELSEWHERE"], "K6",
         "exception", accepted_outcomes=["", "-", "None", "Nothing", "n/a", "Nothing left"]),
    slot("S08", "Collect & Win still to do: the final vial models (Claire)", 5, MS,
         "Arthur's review note on #468 (the vials that spawn in the levels still need their final models before the event runs, no blocker for that PR), left before its "
         "merge and found only in that PR's review list and inline "
         "comments, is read against the brief's still-to-do rule (player-facing art flagged since the brief as still needed)", "write_content", "exception",
         ["reason_matches", "Collect & Win", r"vial"], "cw.todo.vials", ["R_REVIEW_FLAGS"], "K6", "exception"),
    slot("S09", "Season Pass still to do: the premium strip moves to the November range (Oliver)", 5, MS,
         "Arthur's inline note on #472 (the strip art still shows the October range and needs the November range "
         "before that season opens), left with his approval just before its merge and found only in that PR's inline "
         "review comments, is read against the still-to-do rule and the November season", "write_content", "exception",
         ["reason_matches", "Season Pass", r"premium|strip|banner"], "sp.todo.strip", ["R_REVIEW_FLAGS"], "K6",
         "exception"),
    slot("S10", "Season Pass still to do: the November config lands before Fri Oct 31 00:00 UTC (Brian)", 5, MS,
         "Brian's handoff date, his later slip to Fri Oct 31 10:00 Istanbul time in another thread and the base "
         "page_season_pass_spec's 24 h lock before the 00:00 UTC season opening (the brief only points to it) must be "
         "put on one clock: the still-to-do cell states the corrected "
         "deadline (Oct 31 00:00 UTC / Oct 30 5pm PDT) or that Brian's date is late and must move earlier", "write_content",
         "exception",
         ["reason_matches", "Season Pass", r"(oct(ober)?\.?\s?31|10[-/]31)[\s,t]{0,4}(00:00|midnight)|2025-10-31[t ]?00:00|2025-10-30[t ]?17:00"
                                           r"|(oct(ober)?\.?\s?30|10[-/]30)[\s,]{0,4}(5\s?:?0?0?\s?pm|17:00)"
                                           r"|\blate\b|too late|7\s?h(ours?)?\s?(late|earlier)|move(d|s)?\s(it\s)?(earlier|up|forward|ahead)|bring\s(it\s)?(forward|earlier)|before the lock|ahead of the lock"],
         "sp.todo.config", ["R_HANDOFF_SLIP", "R_LOCK_BOUNDARY"],
         "H2", "exception"),
    slot("S11", "Collect & Win still to do: the event icon animation (Marcus)", 5, MS,
         "ZOM-465's master VFX ticket struck 'Idle Icon Animation for all event icons' as done and Marcus's first note "
         "says every event icon animates, but his later note on the same ticket says the Collect & Win icon animation "
         "is still to do, Brian, who wrote the master VFX list (ZOM-521), says there that it has to land before the event runs, and the three animation "
         "PRs (#454 Marcus, #456, #475) enumerate Quest/Season Pass/Zombie Lane/Plague Race/Endless/Infinite Boss icons "
         "and a card pack - Collect & Win is in none - so its icon animation is still to do (art, Marcus)",
         "write_content", "exception", ["reason_matches", "Collect & Win", r"icon"], "cw.todo.icon",
         ["R_ICON_SCOPE"], "K6", "exception"),
    # ---------------------------------------------------------------- Calendar: ordinary samples + volume
    slot("C01", "Plague Race runs", 3, LR,
         "no open issue, fault thread or live-ops infra gap (the queue manager's un-ordered panel) stops players "
         "entering, scoring or claiming", "direct", "sample", ["field", "Plague Race", "Status"], "plague.status",
         ["R_INFRA_SCOPE"], group="calendar:Status", accepted_outcomes=IN),
    slot("C02", "Endless Monster Mode runs", 3, LR, "its open issues are VFX or analytics, which never hold a beat",
         "direct", "sample", ["field", "Endless Monster Mode", "Status"], "endless.status", ["R_HOLD_SCOPE"], group="calendar:Status",
         accepted_outcomes=RUN),
    slot("C04", "Season Pass runs", 3, LR, "the October season is live on both stores; its open issues are analytics",
         "direct", "sample", ["field", "Season Pass", "Status"], "sp.status", ["R_HOLD_SCOPE"], group="calendar:Status",
         accepted_outcomes=RUN),
    slot("C05", "Collect & Win runs (it just starts later in the week)", 3, LR,
         "a live beat once its prod server windows open (the brief: a beat whose server windows are waiting on the release starts late, it "
         "is not held); its late first window is graded separately (S01); the incomplete queue/addressables infra does "
         "not hold it", "direct",
         "sample", ["field", "Collect & Win", "Status"], "cw.status", group="calendar:Status",
         accepted_outcomes=RUN + ["Starts late"]),
    slot("V01", "The calendar covers exactly the seven beats players see", 3, LR,
         "every beat by the brief's scope, a row per beat, with Zombie Lane (a permanent track, per Frederick's follow-up "
         "under his ask), Boss Arena, Axe Arena and the Halloween one-off off", "delivery", "volume",
         ["delivery", "register_keys_exact"], "calendar.keys", ["R_SCOPE_BEATS"], volume_for=["calendar:Status"]),
    # ---------------------------------------------------------------- Pushes
    slot("P01", "1-day lapse push is held (old game name)", 3, INT,
         "the brief's copy rule applied to the Ready 1-day-lapse row, whose English copy still says 'Puzzles vs Zombies'",
         "direct", "exception", ["field", "1-day lapse", "Send or hold"],
         "push.lapse1", ["R_COPY_CURRENT"], "K5", "exception", accepted_outcomes=HOLD),
    slot("P02", "D0-1 FTUE push is held (old game name)", 3, INT,
         "the same copy rule applied to the second Ready row with the old title", "direct", "exception",
         ["field", "D0-1 FTUE", "Send or hold"], "push.ftue", ["R_COPY_CURRENT"], "K5", "exception",
         accepted_outcomes=HOLD),
    slot("P03", "Plague Race start push is held (row is WIP, not LIVE)", 3, INT,
         "the brief sends a push only when its row is Ready and LIVE; the Plague Race row is Ready but its 'Status (NA, "
         "WIP, LIVE)' column reads WIP, not LIVE",
         "direct", "exception", ["field", "Plague Race start", "Send or hold"], "push.plague", ["R_WIRED"], "K5",
         "exception", accepted_outcomes=HOLD),
    slot("P04", "Lives recharged push is sent", 3, INT,
         "the row is Ready and LIVE and its copy names no game at all; Frederick's follow-up under his ask says such "
         "copy is fine to go out (the naming rule is only about wrong names), where the brief's naming sentence read "
         "alone would hold it", "direct", "exception",
         ["field", "Lives recharged", "Send or hold"], "push.lives", ["R_ASK_FOLLOWUP"], "K17", "exception",
         accepted_outcomes=["Send", "Sent", "Go", "Yes"]),
    slot("P05", "7-day lapse push is sent", 3, INT,
         "the second Ready and LIVE row whose copy names no game at all, sent on the same sentence of Frederick's "
         "follow-up under his ask", "direct", "exception",
         ["field", "7-day lapse", "Send or hold"], "push.lapse7", ["R_ASK_FOLLOWUP"], "K17", "exception",
         accepted_outcomes=["Send", "Sent", "Go", "Yes"]),
    slot("P06", "1-day lapse hold reason names the old-title copy fix", 3, INT,
         "the held push's 'what is missing' cell must name the copy fix (the old 'Puzzles vs Zombies' title / rename), "
         "not be blank", "write_content", "exception", ["reason_matches", "1-day lapse", r"puzzles|old (game|title|name)|rename|copy"],
         "push.lapse1.reason", ["R_COPY_CURRENT"], "K5", "exception"),
    slot("P07", "Weekly Leaderboard reset push is held (row is WIP, not LIVE)", 3, INT,
         "the brief sends a push only when its row is Ready and LIVE; the Weekly Leaderboard reset row is Ready but its "
         "'Status (NA, WIP, LIVE)' column reads WIP, not LIVE",
         "direct", "exception", ["field", "Weekly Leaderboard reset", "Send or hold"], "push.weekly", ["R_WIRED"], "K5",
         "exception", accepted_outcomes=HOLD),
    slot("V02", "The push plan covers exactly the ten beta rows (the four off-beta rows left off)", 3, LR,
         "Frederick's follow-up under his ask makes the plan the PNs Beta tab as it stands, one line per row, local "
         "notifications included, with exactly four rows left off (Hourly Coins, Nathan's Treasure Hunt, Streak Fever, "
         "Axe Arena); the brief alone names no row set", "delivery", "volume",
         ["delivery", "register_keys_exact", "pushes"], "pushes.keys", ["R_ASK_FOLLOWUP"],
         volume_for=["pushes:Send or hold"], expected_keys=PUSHES),
    # ---------------------------------------------------------------- Writes
    slot("W01", "Recommendation goes back to Frederick in his DM", 1, LK, "delivery into the named DM", "delivery",
         "core", ["delivery", "slack_channel_post", FRED_DM, "calendar"], "reply.dm"),
    slot("W02", "Reply names Collect & Win's late start and why", 3, LR,
         "the deploy finding carried into the recommendation's tradeoffs", "write_content", "exception",
         ["text", "slack", r"collect (?:&|and) win.{0,200}(oct(ober)?\.? ?(8|9|10)|release|deploy|prod)"],
         "reply.cw", ["R_DONE_DEPLOY"], "H3", "tickets"),
    slot("W03", "Reply says the Halloween one-off is off and why", 5, MS,
         "the reply must carry Robert's latest call, which his later DM message shows without naming Halloween, against the approval Martin's "
         "thread shows; a withdrawal verb, not a bare 'off' a 'not off' could negate", "write_content", "exception",
         ["text", "slack", r"halloween.{0,240}(dropped|withdrawn|pulled|cancel|scrapped|removed|not running|no longer|won'?t run|will not run|not happening|taken back)"
                           r"|(dropped|withdrawn|pulled|cancel|scrapped|removed|no longer).{0,240}halloween"],
         "reply.halloween", ["R_WITHDRAWN"], "K4", "tickets"),
    slot("W04", "Calendar linked on ZOM-78", 1, LK, "the link goes on the existing calendar ticket", "write_content",
         "core", ["text", "linear", r"docs\.google\.com/spreadsheets|f_e4a17c90b3d25f6a8c1d73"], "zom78.link"),
    slot("W05", "Leagues hold noted on ZOM-429", 3, LR, "the hold and its reason recorded on the held beat's open ticket",
         "write_content", "exception", ["text", "linear", r"(hold|held|holding).{0,200}(leagu|leaderboard|restart)"
                                                          r"|(leagu|leaderboard).{0,200}(hold|held)"],
         "zom429.note", ["R_TECH_HOLD"], "K3", "tickets"),
    slot("W06", "Reply to Brian's Season Pass mail", 1, LK, "delivery as a reply to his latest mail, the one where he "
         "committed to the new date (the brief: you tell its owner in a reply on the mail where they committed to it)",
         "delivery", "core",
         ["delivery", "email_reply", M2], "brian.reply"),
    slot("W07", "Reply to Brian moves the November config before the lock", 3, LR,
         "the corrected lock instant (Oct 31 00:00 UTC / Oct 30 5pm PDT) or an explicit late / move-earlier carried into "
         "the reply to the config owner", "write_content", "exception",
         ["text", "email", r"(oct(ober)?\.?\s?31|10[-/]31)[\s,t]{0,6}(00:00|midnight)|2025-10-31[t ]?00:00|2025-10-30[t ]?17:00"
                           r"|(oct(ober)?\.?\s?30|10[-/]30)[\s,]{0,6}(5\s?:?0?0?\s?pm|17:00)"
                           r"|\blate\b|too late|7\s?h(ours?)?\s?(late|earlier)|move(d|s)?\s(it\s)?(earlier|up|forward|ahead)|bring\s(it\s)?(forward|earlier)|ahead of the lock"],
         "brian.lock", ["R_LOCK_BOUNDARY"], "H2",
         "tickets"),
]

surface = {
    "kind": "GRADABLE_SURFACE", "version": 1, "task": "julia-zm3d-beta-liveops-calendar", "revision": "scenario-01",
    "classes": ["Run", "Hold", "Send"],
    "truth_fields": {"class": "Status", "groups": "groups"},
    "truth_keys": BEATS,
    "deliverables": {
        "calendar": {"kind": "table", "name_regex": r"live.?ops calendar|calendar", "key_column": "Beat",
                     "key_regex": BEAT_RX, "columns": CAL_COLS, "class_column": "Status",
                     "reason_column": "Still to do (owner)", "comparators": {"Status": "norm",
                                                                                  "First window (UTC)": "norm"},
                     "missing_values": ["", "-", "none", "n/a", "nothing"]},
        "pushes": {"kind": "table", "name_regex": r"push", "key_column": "Push name",
                   "key_regex": PUSH_RX, "columns": PUSH_COLS, "class_column": "Send or hold",
                   "reason_column": "What is missing", "comparators": {"Send or hold": "norm"},
                   "missing_values": ["", "-", "none", "n/a"]},
        "slack": {"kind": "json_text", "tool": "slack_send_message"},
        "linear": {"kind": "json_text", "tool": "linear_create_comment"},
        "email": {"kind": "json_text", "tool": "gmail_reply_to_message"},
    },
    "slots": SLOTS,
}
out = WF / "01_Gradable_Surface.json"
out.write_text(json.dumps(surface, indent=1, ensure_ascii=False) + "\n")
tw = sum(s["weight"] for s in SLOTS)
mw = sum(s["weight"] for s in SLOTS if s.get("mechanisms"))
print(f"wrote {out}: {len(SLOTS)} slots, weight {tw}, mechanism weight {mw} ({mw / tw:.0%}), "
      f"weight-5 {sum(1 for s in SLOTS if s['weight'] == 5)}")

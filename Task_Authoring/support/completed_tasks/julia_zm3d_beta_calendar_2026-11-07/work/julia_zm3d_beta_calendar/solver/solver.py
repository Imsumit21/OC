"""julia-zm3d-beta-liveops-calendar solver (revision 14; fourteen rules, the rules of revision 5).

Truth owner for Julia Lawson's ZM3D beta live-ops + push calendar (Product / Marketing and GTM / Planning and
decision support, Long Horizon): one row per beat of the four buy weeks (Mon Oct 6 - Sun Nov 2, 2025) with its first
window, its weeks running, its Status (Run/Hold) and what is still to do before it runs (owner, due), plus one row per
beta push with Send-or-hold and what is missing. Parses the injection SQL as data through tools/base_check.parse_sql;
never executes SQL.

REVISION 2 (SQL sha256 3afbf7cb..., prompt sha256 2a23afd8...)
  Frederick's thread reply under his own ask (SLACK_FOLLOWUP) amends the brief: the push plan is the base "PNs Beta"
  tab row by row, local notifications included, with the four rows for things that are not in the beta left off
  (Hourly Coins, Nathan's Treasure Hunt, Streak Fever, Axe Arena); copy that names no game at all may go out; and
  Zombie Lane stays off the calendar (a permanent track with no window or reset to plan). So the truth is SEVEN beats
  (Zombie Lane is not a key any more) and TEN push rows (the six Ready rows plus the four Not Ready rows that stay
  on the plan as Held). One rule was added for the amendment, R_ASK_FOLLOWUP (fifteen rules in all). The brief also
  says a beat that is only waiting on the backend release starts late and is not held (Collect & Win: Runs), and the
  daily-gift frame is in both Sep 30 submission builds (iOS Submission #50 and Android Submission #135).

REVISION 3 (SQL sha256 837d4f5d..., prompt unchanged)
  The repair for the second /prompt FAIL (Cross-Service Coherence, known-issue card SC-15). The SQL seeds the ZOM-521
  description with the two checklist items whose child tickets are still In Progress unticked, and one later note
  from the ticket's creator on ZOM-526 (cmt_zom526_2). Neither decides a key: no rule, value, evidence list or
  control changes, and truth.json is byte for byte the revision-2 file. Only REVISIONS advances, so the reports that
  label themselves with the latest revision (mutation, preflight) read rev3.

REVISION 4 (SQL sha256 c955d6ca..., prompt unchanged)
  The repair for the independent /prompt run on revision 3 (Cross-Service Coherence, Clarity 3). No value changes;
  three deciding notes live on other records, so three evidence constants are re-pointed:
    NOTE_VIALS  final vial sprites (Claire)        #370#rc_1  -> #468#rc_38, Arthur's inline review note before the merge
    NOTE_STRIP  premium strip to November (Oliver) #438#rc_74 -> #473#c_2, Arthur's conversation note 35 min after it
    NOTE_ICON   C&W event icon animation (Marcus)  #454#c_4   -> cmt_zom465_2, his second note on ZOM-465
  The base pointers that stood only for the old carriers (#370, #438) become #468 and #473. Five tickets are Done in
  the seeded state (ZOM-344, ZOM-432, ZOM-471, ZOM-542, ZOM-565), so R_DONE_ELSEWHERE no longer starts from an open
  ticket: what is left is Calvin's older note on ZOM-432 against the ticket's later closure and Samuel's PR note (a
  weaker trap; the value, an empty still-to-do, is the same), and its control label ZOM-344 becomes ZOM-534, an
  open Quests ticket. Robert's retraction is a top-level DM message and Brian's correction a mail of its own; both
  keep their ids. truth.json differs from revision 3 only in the three evidence ids above.
  Each of the three notes is declared with its carriers, newest first (the NOTE_* tuples); a rule reads the one the
  parsed SQL holds (_carrier). So these rules give the revision-3 truth, byte for byte, on the revision-3 SQL, and a
  later move costs one more id in a tuple.

REVISION 5 (SQL sha256 3c035f2a..., prompt unchanged)
  The repair for the independent /prompt run on revision 4 and the claim-by-claim audit of every injected record
  (research/prompt_review_rev4/, research/prompt_review_rev5_audits/). Two cells change and one rule goes:
    Quests still to do     empty. The quest note is now Leonard's, on the open quests card #61, and says the current
                           set carries the first week, so nothing has to land before the beat runs. R_QUEST_SET, the
                           rule that existed only for this cell, is retired: FOURTEEN rules. The note decides no cell.
    Collect & Win still to do   the vial part reads "the final vial models (Claire)": Arthur's note on #468 (same id)
                           now names Claire's 3D vial models, not sprites.
  Samuel's frame note left PR #471 for the ticket it closes (cmt_zom432_2 on ZOM-432, Done at the same instant), so
  Daily Login's empty still-to-do is decided on that one ticket: R_DONE_ELSEWHERE keeps its id, but nothing is
  recorded "elsewhere" any more and it is no difficulty carrier. The five Slack messages people wrote and Brian's two
  mails have new ids (new ts values, new Message-IDs); #470's note is part of Arthur's base approval review.
  Every record that moved or was re-keyed is a tuple of carriers, newest first, as in revision 4. The two cells that
  changed follow the words of the note the SQL holds (_quest_set_waits, _vial_todo), so these rules still give the
  revision-4 truth, byte for byte, on the revision-4 SQL: every difference between the two truths comes from the SQL.

REVISION 6 (SQL sha256 f8d905bd..., prompt unchanged)
  The repair for the one fork the independent /prompt run on revision 5 left open (Unique Ground Truth: nothing said
  whether the Oct 13 quest set has to land for the beta). The quest note says outright that nothing in the beta waits on
  it. No rule, value or evidence id changes and truth.json is byte for byte the revision-5 file. The other revision-6
  changes (a third note on ZOM-526, shorter notes on ZOM-544 and in Brian's Sep 22 mail, Drive and Gmail field shapes)
  touch no record a rule reads.

REVISION 7 (SQL sha256 091722f6..., prompt unchanged)
  Two residuals from the reviews of revision 6. The quest note now says the new quests are additive: "More quests get
  added with the Mon Oct 13 rollover if they are ready. Nothing in the beta waits on them, the current quests keep
  running either way." ZOM-521 has a second note (cmt_zom521_2: the card pack animation went in with #475, and the item
  and ZOM-528 stay open until Brian has seen it in a build). It decides no cell, so it is not a deciding record.
  truth.json is still byte for byte the revision-5 file. _quest_set_waits tests the words revisions 6 and 7 share
  (NOT_WAITING), because the note no longer carries the revision-5 phrase.

REVISION 8 (SQL sha256 0e8c8ad8..., prompt unchanged)
  The findings of a fresh blind /prompt round on revision 7. No value changes; one evidence id does. The premium-strip
  note left merged #473, where it sat 35 minutes after the merge, for an inline note under Arthur's base approval of #472,
  six seconds before that merge: NOTE_STRIP gains #472#rc_1 as its newest carrier, and PR473 leaves BASE because no rule
  reads it (#473 stays a cohort PR and the pointer of distractor D11 in the manifest). Both notes R_REVIEW_FLAGS reads are
  now pre-merge inline notes, so its `source` label is no longer "post-merge-pass". The quest note now says "The rollover
  does not wait on them" (the push row does), so NOT_WAITING gains those words and keeps the older phrases for the
  revision-5 to revision-7 SQLs. The brief gains one sentence on undated holds and the notes on ZOM-534, ZOM-521 and
  ZOM-542 are re-worded; no rule reads any of them for a value.

REVISION 9 (SQL sha256 892f7edd..., prompt unchanged)
  The repair for the platform's third /prompt failure (Unique Ground Truth and Clarity on ZOM-534, the S23 freeze and
  #477). The brief's hold and still-to-do rules were open sets and are closed now. Still to do is a held beat's fix plus
  what has been flagged for that beat as not done since the brief (prod deploy, config or player-facing art); nothing
  else goes in. Every composed still-to-do cell already fits that rule, so no rule, value or evidence id changes and
  truth.json is byte for byte the revision-8 file. No rule read the removed "unverified build or platform" clause, so
  none is retired. Robert's withdrawal now says "the themed prop set I okayed in Martin's thread", not "Halloween
  one-off": R_WITHDRAWN reads that record by id through his DM, so Halloween still comes off. cmt_zom566_1 is Brian's
  note now and Owen's analytics note is cmt_zom566_2. cmt_zom534_2, cmt_zom563_1, cmt_zom566_1 and the two #zombie-bugs
  replies decide no cell, so none is a deciding record.

REVISION 10 (SQL sha256 ffbac458..., prompt unchanged)
  The pre-review attack on revision 9 (research/rev9_attack/). The still-to-do rule is re-worded: "its fix if it is held,
  and anything flagged since this brief as still needed for it (prod deploy, config or player-facing art)". Two value
  changes, both deliberate, and no evidence id moves:
    Owners            Weekly Leagues' fix names Douglas (was "league owner"), the ZOM-429 assignee, and Collect & Win's
                      server-windows item names Douglas, the release organizer.
    Weeks running     Quests and Daily Login read "All four weeks" (was empty): the brief asks which weeks they run, and
                      the quest note now says "weekly rollover".
  These four cells follow _rev10, a marker on the brief's new sentence, so the same rules still give every older truth on
  its own SQL. The quest note's words changed again, so NOT_WAITING gains them; without that the Quests still-to-do would
  come back. cmt_zom565_2 and the new replies decide no cell.

REVISION 11 (SQL sha256 1348d287..., prompt unchanged)
  The formal blind round on revision 10 (research/prompt_review_rev10/). No rule and no value changes. One evidence id is
  added: cmt_zom465_3, Brian on ZOM-465 (the Collect & Win icon has to land), joins R_ICON_SCOPE's deciding records through
  NOTE_ICON_NEEDED, so the Collect & Win row's evidence gains it. On an older SQL that tuple resolves to the same record as
  NOTE_ICON and _uniq drops the repeat, so every older truth keeps its bytes. The brief gains the clip sentence, "closing
  23:59 UTC on its last day", the held-row sentence, "Login Calendar on the push sheet, same beat" and "moves to any time
  before it"; no rule reads those words, and Season Pass's First window stays empty (no slot reads it). The quest note's
  payload lost its list and idCard keys; _body reads the whole data_json, so NOT_WAITING still finds its words. ZOM-542 is
  Todo and Douglas's #zm-collect-win reply decides no cell.

REVISION 12 (SQL sha256 b5ccbfa5..., prompt unchanged)
  The verification round on revision 11 (research/prompt_review_rev11/). No rule changes and no evidence id moves. Three
  cells that were empty are filled, and no slot reads them: Weekly Leagues' First window (Mon Oct 6 00:00 UTC) and Weeks
  running (All four weeks), under the brief's held-row sentence, with the Held status as the mark; and Season Pass's First
  window (Mon Oct 6 00:00 UTC), the running October season under the clip sentence. The three follow _rev12, a marker on the
  held-row sentence's new words, so the same rules still give every older truth on its own SQL. No rule decides these cells,
  so they carry no rule gate and add no evidence. cmt_zom563_1 is Douglas's note now and Vincent's check is cmt_zom563_2;
  the quest note's payload has idCard and textData back and still no list. None of these decides a cell.

REVISION 13 (SQL sha256 1f2175a2..., prompt unchanged)
  The cold reviewers' last items on revision 12 (research/prompt_review_rev12/). No rule, value or evidence id changes and
  truth.json is byte for byte the revision-12 file. Arthur's vial note no longer says "vial models": it says the vials "still
  need their final models before the event runs", so VIAL_WORDS gains "final models" and the cell stays "the final vial models
  (Claire)" by the note's words, not by _vial_todo's fallback. Brian's ZOM-465 note, the brief's shop and Push copy words and
  the quest note's payload (its list key is back) change too; no rule reads them.

REVISION 14 (SQL sha256 edae63f3..., prompt unchanged)
  The two items from the last cold P1 on revision 13 (research/prompt_review_rev13/). Two brief sentences change: "you tell its
  owner in a reply on the mail where they committed to it" and "Endless goes down as its weekly windows, with the daily reset
  noted." No rule reads either, so no rule, value or evidence id changes and truth.json is byte for byte the revision-13 file.

WHAT THIS FILE IS
  `RULES` mirrors the manifest's fourteen mechanism-portfolio entries (ids, mechanism, requirement, nodes,
  natural_reading, controls, over_application, source, signature, decides). The golden values live in SCALAR (one
  accepted value per direct slot) and TEXT (composed still-to-do / what-is-missing cells); `solve()` carries a
  per-key/per-field comment block naming the seeded records and the rules that decide each value. The plumbing
  (RULES, DEGRADES, CHANNELS, load_state, keys, aggregates, evidence, base_route) is what oracle_kit and
  difficulty_mutation read.

PLUMBING
  * disable/degrade: a disabled rule (or one whose deciding records are missing) gives its key the off value, and a
    degraded over-application operator pushes the rule's control members to the over-applied value. `_placeholder`
    is the scaffolding-stage marker helper, kept for debugging a dead rule or operator; solve() does not call it.
  * `_off` / `_has` follow the exemplar: a rule is off for a key whole (the id in `disable`) or per key
    ((id, {keys})) and is also off when its deciding records are missing from the parsed SQL (base records excepted).
  * `base_route` routes every base deciding record (the push sheet, the base PRs, review comments and issues) so
    contract.golden can read them through tools/hg.py records.

HOW THE MANIFEST PROSE IS RECONCILED (contract.controls and contract.slots are blocking)
  1. `decides` / `controls` are written below as the MANIFEST's prose and labels. oracle_kit reads `decides` as ROW
     FIELD NAMES and `controls` as SOLVER KEYS, so `decides_fields` and `control_keys` on each rule are the machine
     form, and the loop after RULES flips both onto RULES in place (see DECIDES_FIELDS / CONTROL_KEYS below).
  2. Five surface slots carry a `reason_matches` selector (S08, S09, S10, S11, P06; S06 left in revision 5).
     gradable_surface.solver_value() has no `reason_matches` branch, so they are `class: "write_content"` in
     01_Gradable_Surface.json: graded from the text the run writes, with the TEXT cells below as the expected text.
  Also: CLASS_FIELD is "Status" (the beats' column). The push deliverable's class column is "Send or hold", so a
  push rule's `decides` names "Send or hold" - the module-level class field alone cannot cover both tables.
"""
import collections
import hashlib
import re

REVISIONS = ("rev1", "rev2", "rev3", "rev4", "rev5", "rev6", "rev7", "rev8", "rev9", "rev10", "rev11", "rev12", "rev13", "rev14")
CLASS_FIELD = "Status"
GROUPS_FIELD = "groups"

# The solver's row fields (column names of the two table deliverables).
STATUS = "Status"                                    # Run / Held
FIRST_WINDOW = "First window (UTC)"
WEEKS = "Weeks running"
TODO_FIELD = "Still to do (owner)"
SEND_HOLD = "Send or hold"                           # Send / Held
MISSING = "What is missing (owner)"                  # the held push's reason. The surface column and the seeded header are
#                                                      "What is missing" since revision 9; this field label stays, so that
#                                                      truth.json keeps its bytes and older SQLs still regress
FIELDS = [STATUS, FIRST_WINDOW, WEEKS, TODO_FIELD, SEND_HOLD, MISSING]
BEAT_FIELDS = [STATUS, FIRST_WINDOW, WEEKS, TODO_FIELD]
PUSH_FIELDS = [SEND_HOLD, MISSING]

# ---------------------------------------------------------------- the keys
# Seven beats. Zombie Lane is NOT a beat (Frederick's follow-up under his ask: a permanent track with no window or
# reset to plan); the Halloween one-off (withdrawn), Boss Arena (off until the pivot call) and Axe Arena (postponed
# for the beta) stay off as before.
BEATS = [
    "Plague Race",
    "Collect & Win",
    "Season Pass",
    "Endless Monster Mode",
    "Weekly Leagues",
    "Quests",
    "Daily Login",                # = the daily gift (the "Login Calendar update" row on the push sheet)
]
# Ten push rows: every row of the base "PNs Beta" tab except the four Frederick's follow-up leaves off (Hourly Coins,
# Nathan's Treasure Hunt, Streak Fever, Axe Arena - things that are not in the beta). The push keys are spelled so
# they can never be confused with a beat key ("Quests rollover push" vs the beat "Quests", "Season Pass activation"
# vs "Season Pass", "Login Calendar update" vs "Daily Login", "Win & Collect event start" vs "Collect & Win").
PUSHES = [
    "1-day lapse",
    "D0-1 FTUE",
    "Plague Race start",
    "Lives recharged",
    "7-day lapse",
    "Weekly Leaderboard reset",
    "Quests rollover push",
    "Win & Collect event start",
    "Login Calendar update",
    "Season Pass activation",
]
# The four "PNs Beta" rows that must NOT be listed (an extra row for any of them is a wrong push plan; surface V02).
PUSHES_LEFT_OFF = ["Hourly Coins", "Nathan's Treasure Hunt", "Streak Fever", "Axe Arena"]
# The base push sheet f_a325dd4af80afc5994d5dc "PNs Beta" (sheet index 1) holds 14 rows; column "Status" is Ready /
# Not Ready and column "Status (NA, WIP, LIVE)" is the second status the brief's "Ready and LIVE" rule reads.
#   Ready + LIVE, copy names no game              Lives recharged, 7-day lapse   -> Send (R_ASK_FOLLOWUP: copy that
#                                                                                    names no game at all is fine)
#   Ready + LIVE, copy says "Puzzles vs Zombies"  1-day lapse, D0-1 FTUE         -> Held (R_COPY_CURRENT)
#   Ready + WIP (not LIVE)                        Plague Race start, Weekly Leaderboard reset -> Held (R_WIRED)
#   Not Ready (LIVE)                              Quests rollover push           -> Held (the row is Not Ready)
#   Not Ready + WIP                               Win & Collect event start (its copy uses the Domino name "Win &
#                                                 Collect"), Login Calendar update, Season Pass activation -> Held
#   left off the plan                             Hourly Coins, Nathan's Treasure Hunt, Streak Fever, Axe Arena
# The held text of the two Ready + WIP rows says "WIP, not LIVE" and makes no claim about the build: the revision-2
# review found the base client code (NotificationManager.cs) already schedules both locally, so a "not wired" claim
# would contradict base data.

KEYS = BEATS + PUSHES


def keys():
    return list(KEYS)


# ---------------------------------------------------------------- the rules (manifest mirror)
# The fourteen entries of 01_Hardness_Manifest.draft.json mechanism_portfolio, field for field (R_QUEST_SET was
# retired in revision 5: the Quests still-to-do it decided is empty and no slot grades it). `family` repeats
# `mechanism` (the exemplar's idiom; oracle_kit pools channel rates by it). `authority` is derived mechanically from
# the manifest's authorities[].governs (H1 governs R1/R3/R4/R6, H2 R8, H3 R2); a requirement governs no authority for
# R5. `decides_fields` and `control_keys` are the reconciled, machine-readable form of the prose (see the docstring).
# A control member is always a real key the rule does not itself decide (no rule controls the off-calendar Zombie
# Lane any more).
RULES = {
    "R_DONE_DEPLOY": {
        "mechanism": "A24", "family": "A24", "requirement": "R2", "nodes": ["T1", "CH1"],
        "natural_reading": "merged client PRs + 'feature completed' = starts with the first beta window",
        "decides": ["Collect & Win first window", "Collect & Win still to do"],
        "decides_fields": [FIRST_WINDOW, TODO_FIELD],
        "controls": ["Plague Race", "Endless"],
        "control_keys": ["Plague Race", "Endless Monster Mode"],
        "over_application": "over:every-beat-waits-for-a-release",
        "source": "inline-470", "signature": "merged-not-deployed", "authority": ["H3"],
    },
    "R_WITHDRAWN": {
        "mechanism": "A11", "family": "A11", "requirement": "R4", "nodes": ["T2", "CH2"],
        "natural_reading": "the Product owner's approval in the art thread stands",
        "decides": ["Plague Race weeks running", "Halloween one-off in the reply"],
        "decides_fields": [WEEKS],
        "controls": ["Endless", "Season Pass"],
        "control_keys": ["Endless Monster Mode", "Season Pass"],
        "over_application": "over:every-one-off-dropped",
        "source": "robert-dm-thread", "signature": "approval-taken-back", "authority": ["H1"],
    },
    "R_SCOPE_BEATS": {
        "mechanism": "A17", "family": "A17", "requirement": "R1", "nodes": ["T3"],
        "natural_reading": "the beats are the events everyone lists",
        "decides": ["Quests row", "Login calendar row"],
        "decides_fields": [STATUS, TODO_FIELD],
        "controls": ["Plague Race", "Endless"],
        "control_keys": ["Plague Race", "Endless Monster Mode"],
        "over_application": "over:every-push-row-is-a-beat",
        "source": "brief-scope", "signature": "resets-are-beats", "authority": ["H1"],
    },
    "R_COPY_CURRENT": {
        "mechanism": "A15", "family": "A15", "requirement": "R6", "nodes": ["T4"],
        "natural_reading": "Ready in the push sheet = sendable",
        "decides": ["1-day lapse push", "D0-1 FTUE push"],
        "decides_fields": [SEND_HOLD, MISSING],
        "controls": ["7-day lapse", "Lives recharged"],
        "control_keys": ["7-day lapse", "Lives recharged"],
        "over_application": "over:every-zombie-copy-held",
        "source": "brief-copy", "signature": "old-title-held", "authority": ["H1"],
    },
    "R_WIRED": {
        "mechanism": "A15", "family": "A15", "requirement": "R6", "nodes": ["T5"],
        "natural_reading": "Ready = LIVE",
        "decides": ["Plague Race start push", "Weekly Leaderboard reset push"],
        "decides_fields": [SEND_HOLD, MISSING],
        "controls": ["7-day lapse", "Lives recharged"],
        "control_keys": ["7-day lapse", "Lives recharged"],
        "over_application": "over:every-push-held",
        "source": "brief-ready-and-live", "signature": "ready-but-wip", "authority": ["H1"],
    },
    "R_ASK_FOLLOWUP": {
        "mechanism": "A14", "family": "A14", "requirement": "R6", "nodes": ["T15"],
        "natural_reading": ("the brief is the whole rulebook: its naming sentence is read strictly and every row of "
                            "the tab is listed"),
        "decides": ["Lives recharged push", "7-day lapse push"],
        "decides_fields": [SEND_HOLD],
        "controls": ["1-day lapse", "D0-1 FTUE"],
        "control_keys": ["1-day lapse", "D0-1 FTUE"],     # wrong-name copy: held with or without the follow-up
        "over_application": None,
        "source": "ask-thread-reply", "signature": "amendment-in-the-ask-thread", "authority": ["H1"],
    },
    "R_TECH_HOLD": {
        "mechanism": "A1", "family": "A1", "requirement": "R3", "nodes": ["T7", "CH4"],
        "natural_reading": "the owner note and the Sep 22 fix settle it: a restart gets players in",
        "decides": ["Weekly leagues status", "ZOM-429 hold note"],
        "decides_fields": [STATUS],
        "controls": ["Quests", "Daily login"],
        "control_keys": ["Quests", "Daily Login"],
        "over_application": "over:every-restart-fault-held",
        "source": "retest-reply", "signature": "fails-after-restart", "authority": ["H1"],
    },
    "R_HANDOFF_SLIP": {
        "mechanism": "A14", "family": "A14", "requirement": "R8", "nodes": ["T8", "CH3"],
        "natural_reading": "the handoff thread's date is the date",
        "decides": ["Season Pass November config deadline", "reply to Brian"],
        "decides_fields": [TODO_FIELD],
        "controls": ["Endless", "Quests"],
        "control_keys": ["Endless Monster Mode", "Quests"],   # rows with no handoff date of their own
        "over_application": None,
        "source": "brian-slip-mail", "signature": "date-moved-in-other-thread", "authority": ["H2"],
    },
    "R_LOCK_BOUNDARY": {
        "mechanism": "A19", "family": "A19", "requirement": "R8", "nodes": ["T9"],
        "natural_reading": "a delivery on the lock day is on time",
        "decides": ["Season Pass November config deadline", "reply to Brian"],
        "decides_fields": [TODO_FIELD],
        "controls": ["Collect & Win"],
        "control_keys": ["Collect & Win"],
        "over_application": None,
        "source": "lock-instant", "signature": "lock-day-late", "authority": ["H2"],
    },
    "R_DONE_ELSEWHERE": {
        "mechanism": "A25", "family": "A25", "requirement": "R5", "nodes": ["T10"],
        "natural_reading": "the frame ticket's own Sep 24 note is the last word: the daily-gift frame is still needed",
        "decides": ["Daily login still to do"],
        "decides_fields": [TODO_FIELD],
        # manifest labels are records (the *issues* the rule must leave alone), not solver keys: they must be
        # re-pointed to the beat whose still-to-do they protect (ZOM-534 -> Quests, ZOM-556 -> Daily Login).
        # Revision 4: ZOM-344 is Done in the seeded state, so the open Quests ticket ZOM-534 takes its place.
        # Revision 5: the closing note is on the frame ticket itself (cmt_zom432_2), so the rule reads one ticket;
        # CH5 (ticket -> #builds -> PR note) is retired and the node list is T10 alone.
        "controls": ["ZOM-534", "ZOM-556"],
        "control_keys": ["Quests"],
        "over_application": "over:every-open-ticket-done",
        "source": "frame-ticket-closing-note", "signature": "older-note-on-closed-ticket", "authority": ["H1"],
    },
    "R_REVIEW_FLAGS": {
        "mechanism": "A3", "family": "A3", "requirement": "R5", "nodes": ["T11", "CH6"],
        "natural_reading": "approved or bot-only PRs leave nothing to do",
        "decides": ["Collect & Win still to do", "Season Pass still to do"],
        "decides_fields": [TODO_FIELD],
        # same shape: the manifest names the two PRs (#420, #364) that must add no task; contract.controls needs
        # solver keys, so the build session re-points each to the beat it protects.
        "controls": ["harmonygames-Games/match3d#420", "harmonygames-Games/match3d#364"],
        "control_keys": ["Endless Monster Mode", "Plague Race"],   # beats whose merged PRs add no still-to-do
        "over_application": "over:every-pr-adds-a-task",
        "source": "inline-review-notes", "signature": "flag-in-inline-note", "authority": ["H1"],
    },
    "R_HOLD_SCOPE": {
        "mechanism": "A17", "family": "A17", "requirement": "R3", "nodes": ["D7", "D8"],
        "natural_reading": "an open or diagnosed fault thread means the beat is held",
        "decides": ["Endless runs", "Season Pass runs"],
        "decides_fields": [STATUS],
        "controls": ["Plague Race", "Daily Login"],
        "control_keys": ["Plague Race", "Daily Login"],
        "over_application": "over:every-open-fault-holds-the-beat",
        "source": "fault-threads", "signature": "cosmetic-fault-not-a-hold", "authority": ["H1"],
    },
    "R_ICON_SCOPE": {
        "mechanism": "A17", "family": "A17", "requirement": "R5", "nodes": ["T14"],
        "natural_reading": "the master VFX ticket struck 'all event icons' as done, so every icon is animated",
        "decides": ["Collect & Win still to do (icon)"],
        "decides_fields": [TODO_FIELD],
        "controls": ["Season Pass", "Plague Race"],
        "control_keys": ["Season Pass", "Plague Race"],       # icons the three animation PRs do enumerate
        "over_application": "over:all-event-icons-done",
        "source": "icon-master-vs-prs", "signature": "cw-icon-absent", "authority": ["H1"],
    },
    "R_INFRA_SCOPE": {
        "mechanism": "A17", "family": "A17", "requirement": "R3", "nodes": ["D10"],
        "natural_reading": ("the in-progress queue manager, whose flow list does not yet order the Plague Race "
                            "panel, holds Plague Race"),
        "decides": ["Plague Race runs"],
        "decides_fields": [STATUS],
        "controls": ["Endless"],
        "control_keys": ["Endless Monster Mode"],    # a second un-queued panel the over-hold would wrongly stop
        "over_application": "over:an-unqueued-panel-holds-the-beat",
        "source": "queue-manager", "signature": "unqueued-panel-not-a-hold", "authority": ["H1"],
    },
}

# The reconciled machine form of the manifest's prose (see the module docstring mismatch 1). contract.controls reads
# `RULES[r]["decides"]` as row field names and `RULES[r]["controls"]` as solver output keys; the build session flips
# RULES onto these two maps (a two-line comprehension) once it agrees with them.
DECIDES_FIELDS = {r: list(v.get("decides_fields") or []) for r, v in RULES.items()}
CONTROL_KEYS = {r: list(v.get("control_keys") or []) for r, v in RULES.items()}
# oracle_kit reads RULES[r]["decides"] as row FIELD names and RULES[r]["controls"] as SOLVER KEYS (the exemplar's
# convention). Replace the human-readable prose with the reconciled machine form captured above, in place.
for _rid, _spec in RULES.items():
    _spec["decides"] = list(DECIDES_FIELDS.get(_rid, []))
    _spec["controls"] = list(CONTROL_KEYS.get(_rid, []))

DEGRADES = {
    "over:every-beat-waits-for-a-release":
        "start every beat only after the backend release, not at its own first opening window",
    "over:every-one-off-dropped":
        "treat every one-off as dropped because the Halloween one-off was taken back",
    "over:every-push-row-is-a-beat":
        "put every push row on the calendar as a beat of its own",
    "over:every-zombie-copy-held":
        "hold every push whose row is Ready because one row still carries the old game name",
    "over:every-push-held":
        "hold every push because one row's Status (NA, WIP, LIVE) column reads WIP",
    "over:every-restart-fault-held":
        "hold every beat whose thread mentions a fault, restart or not",
    "over:every-open-ticket-done":
        "treat every open ticket as already shipped",
    "over:every-pr-adds-a-task":
        "give every merged PR a still-to-do line, approved or bot-only included",
    "over:every-open-fault-holds-the-beat":
        "hold every beat with an open cosmetic, VFX, performance or analytics fault",
    "over:all-event-icons-done":
        "treat the master icon ticket's 'all event icons' as covering Collect & Win",
    "over:an-unqueued-panel-holds-the-beat":
        "hold Plague Race because the queue manager has not ordered its panel",
}
CHANNELS = {}      # no async waits or forced errors in this task (03_Error_Async_Config.txt: Friction none)

# Fixed application order: which rows exist, then what holds a beat, then what a beat still needs (window -> config
# -> shipped-elsewhere/flagged), then the one-off, then the push sheet last (a push reads the beat's call); on the
# push sheet the ask's own follow-up, which amends the brief's naming sentence, is read before the copy rule.
RULES_ORDER = (
    "R_SCOPE_BEATS",
    "R_HOLD_SCOPE",
    "R_INFRA_SCOPE",
    "R_TECH_HOLD",
    "R_DONE_DEPLOY",
    "R_LOCK_BOUNDARY",
    "R_HANDOFF_SLIP",
    "R_DONE_ELSEWHERE",
    "R_REVIEW_FLAGS",
    "R_ICON_SCOPE",
    "R_WITHDRAWN",
    "R_ASK_FOLLOWUP",
    "R_COPY_CURRENT",
    "R_WIRED",
)

# ---------------------------------------------------------------- records
# Seeded by 01_Universe_Inject.sql (parsed, never executed).
# Revision 5 re-timed the five Slack messages people wrote (ts values end in 9, off the whole minute), so each is a
# tuple of carriers like the moved notes below: (revision 5 ref, the ref through revision 4). Row ids follow the ts.
SLACK_APPROVAL = ("C08R8CHB0QL/1758213623.552919",        # Robert approves the Halloween one-off, Sep 18 16:40:23Z
                  "C08R8CHB0QL/1758213600.552913")        # (sid 933cee9f...; through revision 4 2e75e232...)
SLACK_WITHDRAW = ("D05GU6L0XFH/1759270241.638119",        # Robert takes it back in his DM with Julia, Sep 30 22:10:41Z,
                  "D05GU6L0XFH/1759270200.638114")        # a top-level message since revision 4 (sid 669d15f6...)
#                                                           Since revision 9 it says "the themed prop set I okayed in
#                                                           Martin's thread" and since revision 11 it ends at "Sorry for
#                                                           the flip."; the rule reads it by id, not by its words
SLACK_RETEST = ("C0880U9751A/1759265412.481909",          # Vincent re-tests the weekly leaderboard (sid b5f2955c...)
                "C0880U9751A/1759265412.481907")
SLACK_ASK = ("D05SD5QLG94/1759263617.418209",             # Frederick's ask: the calendar of the four buy weeks,
             "D05SD5QLG94/1759263600.418207")             # Sep 30 20:20:17Z (sid bca78437...)
SLACK_FOLLOWUP = ("D05SD5QLG94/1759263878.305129",        # his thread reply under the ask (sid 890dc27f...): the push
                  "D05SD5QLG94/1759263878.305127")        # plan is the PNs Beta tab row by row minus four named rows,
#                                                           copy that names no game is fine, Zombie Lane stays off
BRIEF = "f_7c3e91a4d2b85f60e1a9c4"                        # Frederick's working rules (docs)
UA_PLAN = "f_2b9d4e7a1c63f08d5e7b21"                      # the four buy weeks (slides)
CALENDAR_SHEET = "f_e4a17c90b3d25f6a8c1d73"               # Julia's calendar sheet (Calendar + Pushes tabs)
EVT_RELEASE = "evt_9a4c2e7f1b3d58e06c7a2f"                # Douglas: backend release, Oct 8 15:00-16:00 UTC
# Brian's two mails: revision 5 gave them his base Message-ID shape (and per-mailbox thread ids that encode the send
# time), so each is (revision 5 id, the id through revision 4).
MAIL_0922 = ("julia.lawson@harmonygames.co/<CAPT--p4sBC8XnaA7qBDMtZkWqJPiXP0MT3deOQGPusOZhHF+vo@mail.gmail.com>",
             "julia.lawson@harmonygames.co/<CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc@mail.gmail.com>")   # config: Wed Oct 29
MAIL_0926 = ("julia.lawson@harmonygames.co/<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>",
             "julia.lawson@harmonygames.co/<CAH4q9Zc8uV1nE5kJ2mRtP7aW3xQ9bLs@mail.gmail.com>")   # slip: Fri Oct 31
#                                   (a mail of its own since revision 4: subject "...: new date", no reply header)
CMT_ZOM429 = "cmt_zom429_1"        # restart gets players into the new week
CMT_ZOM556 = "cmt_zom556_1"        # the streak pays out; the counter is cosmetic
CMT_ZOM565 = "cmt_zom565_1"        # Marcus: endless start-screen polish on his branch, not needed for the beta
CMT_ZOM543 = "cmt_zom543_1"        # queue manager: the panel order list
CMT_ZOM526 = "cmt_zom526_1"        # token-to-live-ops travel, VFX paths (decides no key since Zombie Lane left)
CMT_ZOM552 = "cmt_zom552_1"        # season pass redeem events
CMT_ZOM534 = "cmt_zom534_1"        # quest points rollover syncs now
CMT_ZOM432 = "cmt_zom432_1"        # Calvin, Sep 24: the frame is still needed - the older word (ZOM-432 is Done
#                                   since Sep 30 21:07:26Z, the instant of Samuel's closing note NOTE_FRAME)
CMT_ZOM78 = "cmt_zom78_1"          # use ZOM-78 for the calendar ticket
CMT_ZOM465 = "cmt_zom465_1"        # 'all event icons animate' claim
# A note that moved between revisions is a tuple of its carriers, newest first; _carrier() picks the one in the SQL.
NOTE_ICON = ("cmt_zom465_2",       # Marcus, Sep 30, same ticket: the C&W event icon animation is still to do
             "harmonygames-Games/match3d#454#c_4")        # through revision 3: his #454 conversation note
# Revision 11: Brian, Sep 30, same ticket: the icon has to land before the event runs. It is a second record, not a move, so it
# sits beside NOTE_ICON; the tuple falls back to Marcus's note on an older SQL, where _uniq drops the repeat.
NOTE_ICON_NEEDED = ("cmt_zom465_3",) + NOTE_ICON
CMT_ZOM344 = "cmt_zom344_1"
CMT_ZOM471 = "cmt_zom471_1"
CMT_ZOM504 = "cmt_zom504_1"        # endless visual-only clear
CMT_ZOM517 = "cmt_zom517_1"        # enrage state, test board only
CMT_ZOM521 = "cmt_zom521_1"        # master VFX checklist
CMT_ZOM542 = "cmt_zom542_1"        # endless/boss arena layouts (decides no key since Zombie Lane left)
CMT_ZOM546 = "cmt_zom546_1"        # refill counts hold
CMT_ZOM549 = "cmt_zom549_1"        # analytics payloads
CMT_ZOM566 = "cmt_zom566_2"        # Owen: C&W event list mapped to the sheet (cmt_zom566_1 through revision 8; that id
#                                   is Brian's note since revision 9). Decides no key, like cmt_zom534_2 and the ZOM-563 notes
PR470_RC = "harmonygames-Games/match3d#470#rc_10"         # Arthur: C&W server windows are DEV-only
NOTE_VIALS = ("harmonygames-Games/match3d#468#rc_38",     # Arthur, inline on #468 before its merge: the vials still need
              "harmonygames-Games/match3d#370#rc_1")      # their final models (through revision 3: on #370)
NOTE_STRIP = ("harmonygames-Games/match3d#472#rc_1",      # Arthur, inline under his base approval of #472, before its
              "harmonygames-Games/match3d#473#c_2",       # merge: premium strip to November (revisions 4-7: a conversation
              "harmonygames-Games/match3d#438#rc_74")     # note on #473; through revision 3: on #438)
NOTE_FRAME = ("cmt_zom432_2",                             # Samuel, Sep 30 21:07:26Z, on ZOM-432 as he closes it: the
              "harmonygames-Games/match3d#471#c_18")      # frame went out with PR #471 and is in both submission
#                                                           builds, iOS 50 and Android 135 (through revision 4: his
#                                                           conversation note on #471)
TRELLO_QUESTS = "68dac8204f1e9a3b7c2d5e61"               # the quest note (same action id in every revision). Revision 5:
#     Leonard on the open quests card #61; since revision 10 "More quests and the reward balance go in with the Mon Oct 13
#     rollover if they are ready. The weekly rollover does not wait on them, the current quests keep running either way."
#     - it decides no still-to-do.
#     Through revision 4: Brian on the roadmap card, read as work the beat waits for

# Base records: they live in the exports, never in the injection SQL, so _has() treats them as always present.
PUSH_SHEET = "f_a325dd4af80afc5994d5dc"                   # the PNs Beta push sheet (base, gsheets)
PAGE_LIVEOPS = "page_liveops_calendar"                    # confluence: 'same feature as Win & Collect'
PR470 = "harmonygames-Games/match3d#470"
PR468 = "harmonygames-Games/match3d#468"                  # carries NOTE_VIALS
PR454 = "harmonygames-Games/match3d#454"
PR456 = "harmonygames-Games/match3d#456"
PR471 = "harmonygames-Games/match3d#471"
PR475 = "harmonygames-Games/match3d#475"
PR459 = "harmonygames-Games/match3d#459"
PR472 = "harmonygames-Games/match3d#472"                  # carries NOTE_STRIP since revision 8
ZOM_429 = "ZOM-429"
ZOM_432 = "ZOM-432"
ZOM_465 = "ZOM-465"
ZOM_543 = "ZOM-543"
ZOM_556 = "ZOM-556"
ZOM_534 = "ZOM-534"
ZOM_344 = "ZOM-344"
ZOM_78 = "ZOM-78"
BASE = frozenset({PUSH_SHEET, PAGE_LIVEOPS, PR470, PR468, PR454, PR456, PR471, PR475, PR459, PR472,
                  ZOM_429, ZOM_432, ZOM_465, ZOM_543, ZOM_556, ZOM_534, ZOM_344, ZOM_78})

# ---------------------------------------------------------------- deciding records
# (rule, key) -> the records that decide it. The pairs are the ones the manifest's traps and sources name; the golden
# values they decide are in SCALAR / TEXT below (the rev1 values were verified against base in
# research/GOLDEN_verify.md; the push sheet rows the rev2 keys read were re-read from the base export).
DECIDING = {
    ("R_DONE_DEPLOY", "Collect & Win"): [PR470_RC, EVT_RELEASE, BRIEF],
    ("R_WITHDRAWN", "Plague Race"): [SLACK_APPROVAL, SLACK_WITHDRAW, BRIEF],
    ("R_SCOPE_BEATS", "Quests"): [BRIEF],                 # the quest note left this list in revision 5
    ("R_SCOPE_BEATS", "Daily Login"): [BRIEF, CMT_ZOM432, CMT_ZOM556],
    ("R_ASK_FOLLOWUP", "Lives recharged"): [SLACK_FOLLOWUP, BRIEF, PUSH_SHEET],
    ("R_ASK_FOLLOWUP", "7-day lapse"): [SLACK_FOLLOWUP, BRIEF, PUSH_SHEET],
    ("R_COPY_CURRENT", "1-day lapse"): [BRIEF, PUSH_SHEET],
    ("R_COPY_CURRENT", "D0-1 FTUE"): [BRIEF, PUSH_SHEET],
    ("R_WIRED", "Plague Race start"): [BRIEF, PUSH_SHEET],
    ("R_WIRED", "Weekly Leaderboard reset"): [BRIEF, PUSH_SHEET],
    ("R_TECH_HOLD", "Weekly Leagues"): [CMT_ZOM429, SLACK_RETEST, BRIEF],
    ("R_HANDOFF_SLIP", "Season Pass"): [MAIL_0922, MAIL_0926, BRIEF],
    ("R_LOCK_BOUNDARY", "Season Pass"): [MAIL_0926, BRIEF],
    ("R_DONE_ELSEWHERE", "Daily Login"): [NOTE_FRAME, CMT_ZOM432, BRIEF],
    ("R_REVIEW_FLAGS", "Collect & Win"): [NOTE_VIALS, BRIEF],
    ("R_REVIEW_FLAGS", "Season Pass"): [NOTE_STRIP, BRIEF],
    ("R_HOLD_SCOPE", "Endless Monster Mode"): [CMT_ZOM504, CMT_ZOM565, CMT_ZOM521, BRIEF],
    ("R_HOLD_SCOPE", "Season Pass"): [CMT_ZOM552, BRIEF],
    ("R_ICON_SCOPE", "Collect & Win"): [CMT_ZOM465, NOTE_ICON, NOTE_ICON_NEEDED, PR454, PR456, PR475, BRIEF],
    ("R_INFRA_SCOPE", "Plague Race"): [CMT_ZOM543, PR459, PR472, BRIEF],
}

# The four Not Ready push rows are decided by no designed rule; truth.json still names the records their row is read
# from: the follow-up (why the row is on the plan at all), the brief (the Ready-and-LIVE test) and the push sheet.
PLAIN_EVIDENCE = {k: [SLACK_FOLLOWUP, BRIEF, PUSH_SHEET] for k in (
    "Quests rollover push", "Win & Collect event start", "Login Calendar update", "Season Pass activation")}

# ---------------------------------------------------------------- cells that follow a note's own words (revision 5)
# Two notes kept their id and changed their words. The cell each decides is read from the words the parsed SQL holds,
# so one set of rules gives every revision's truth on that revision's SQL (oracle_kit contract.regression).
def _body(state, rec):
    """The words of a seeded record as the parsed SQL holds them ('' with no SQL loaded or no such row)."""
    by_id = state.get("by_id") if isinstance(state, dict) else None
    for _table, row in (by_id or {}).get(_carrier(state, rec), ()):
        for col in ("body", "body_text", "text", "data_json"):
            if row.get(col):
                return str(row[col])
    return ""


NOT_WAITING = ("The weekly rollover does not wait on them",    # the quest note's words since revision 10
               "The rollover does not wait on them",           # its words in revisions 8 and 9
               "Nothing in the beta waits on",                 # its words in revisions 6 and 7
               "current set carries the first week")           # its words in revision 5


def _quest_set_waits(state):
    """True when the quest note reads as work the Quests beat waits for. Through revision 4 it did (Brian: "Putting the
    new quest set in with the Mon Oct 13 rollover."). Since revision 5 the note says the beat is not waiting (NOT_WAITING):
    nothing has to land before the beat runs, so under the brief's still-to-do rule the cell is empty."""
    body = _body(state, TRELLO_QUESTS)
    return bool(body) and not any(words in body for words in NOT_WAITING)


VIAL_WORDS = (("final models", "the final vial models (Claire)"),     # revision 13: "still need their final models"
              ("vial models", "the final vial models (Claire)"),      # revisions 5 to 12: Claire's 3D vial models
              ("vial sprites", "final vial sprites (Claire)"))         # through revision 4
# The two value changes of revision 10 (owners, Weeks running) follow this sentence of the brief. It is a revision marker,
# not the reason for the values: it lets these rules keep giving every older truth on its own SQL.
REV10_MARKER = "anything flagged since this brief as still needed for it"


def _rev10(state):
    return REV10_MARKER in _body(state, BRIEF)


# The three cells filled in revision 12 follow the new words of the brief's held-row sentence, the same kind of marker. Season
# Pass's clip sentence dates from revision 11, but its cell is empty on that SQL and has to stay so.
REV12_MARKER = "keeps its usual windows and weeks on its row"


def _rev12(state):
    return REV12_MARKER in _body(state, BRIEF)


CONDITIONS = {"note:quest-set-waits": _quest_set_waits, "sql:rev10": _rev10, "sql:rev12": _rev12}


def _leagues_fix(state):
    """The held beat's fix. Its owner is Douglas, the ZOM-429 assignee ("league owner" through revision 9)."""
    return f"the weekly reset fix so a new week starts on prod ({'Douglas' if _rev10(state) else 'league owner'})"


def _windows_todo(state):
    """The prod deploy item. Its owner is Douglas, who organizes the release (unnamed through revision 9)."""
    return "server windows reach prod with the Oct 8 backend release" + (" (Douglas)" if _rev10(state) else "")


def _vial_todo(state):
    """The vial still-to-do in the words of Arthur's note on the PR (the newest wording when no SQL is loaded)."""
    body = _body(state, NOTE_VIALS)
    return next((text for words, text in VIAL_WORDS if words in body), VIAL_WORDS[0][1])


def _legacy_evidence(state, key):
    """The quest note as a deciding record of the Quests row: only on an SQL where it still decides the cell."""
    return [TRELLO_QUESTS] if key == "Quests" and _quest_set_waits(state) else []


# The keys a rule can act on (derived from DECIDING, so a rule with no deciding key acts on nothing).
TOUCHED = {}
for _rule, _key in DECIDING:
    TOUCHED.setdefault(_rule, set()).add(_key)


# ---------------------------------------------------------------- the golden values (build-authored)
# The rev1 values were verified against base in research/GOLDEN_verify.md; rev2 changes only what the SQL changed
# (see the module docstring). Scalar fields carry one accepted value per direct slot:
# (key, field) -> (correct, primary_rule|None, off_value). `off_value` is the tempting wrong reading when the
# primary rule is disabled or its deciding records are missing; it sits OUTSIDE the slot's accepted_outcomes, so
# disabling the rule fails (KILLS) the slot.
SCALAR = {
    ("Plague Race", STATUS):          ("Runs", "R_INFRA_SCOPE", "Held"),
    ("Collect & Win", STATUS):        ("Runs", None, None),
    ("Season Pass", STATUS):          ("Runs", "R_HOLD_SCOPE", "Held"),
    ("Endless Monster Mode", STATUS): ("Runs", "R_HOLD_SCOPE", "Held"),
    ("Weekly Leagues", STATUS):       ("Held", "R_TECH_HOLD", "Runs"),
    ("Quests", STATUS):               ("Runs", "R_SCOPE_BEATS", "(omitted from the calendar)"),
    ("Daily Login", STATUS):          ("Runs", "R_SCOPE_BEATS", "(omitted from the calendar)"),
    ("Collect & Win", FIRST_WINDOW):  ("Fri Oct 10 00:00 UTC", "R_DONE_DEPLOY", "Mon Oct 6 00:00 UTC"),
    ("Plague Race", WEEKS):           ("All four weeks", "R_WITHDRAWN", "Weeks 1-3 (Halloween one-off takes week 4)"),
    ("Daily Login", TODO_FIELD):      ("", "R_DONE_ELSEWHERE", "Daily-gift frame still needed (Calvin)"),
    ("1-day lapse", SEND_HOLD):       ("Held", "R_COPY_CURRENT", "Send"),
    ("D0-1 FTUE", SEND_HOLD):         ("Held", "R_COPY_CURRENT", "Send"),
    ("Plague Race start", SEND_HOLD): ("Held", "R_WIRED", "Send"),
    ("Weekly Leaderboard reset", SEND_HOLD): ("Held", "R_WIRED", "Send"),
    # Ready + LIVE and the copy names no game at all: Send because Frederick's follow-up says such copy may go out.
    # Without the follow-up the brief's naming sentence, read strictly, holds both.
    ("Lives recharged", SEND_HOLD):   ("Send", "R_ASK_FOLLOWUP", "Held"),
    ("7-day lapse", SEND_HOLD):       ("Send", "R_ASK_FOLLOWUP", "Held"),
    # The four Not Ready rows stay on the plan (one line per row) and are Held by the brief's plain "Ready and LIVE"
    # test; no designed rule flips them, so they carry no primary rule and no off value.
    ("Quests rollover push", SEND_HOLD):      ("Held", None, None),
    ("Win & Collect event start", SEND_HOLD): ("Held", None, None),
    ("Login Calendar update", SEND_HOLD):     ("Held", None, None),
    ("Season Pass activation", SEND_HOLD):    ("Held", None, None),
}

# Composed cells graded by the surface regexes (S08/S09/S10/S11/P06). Each part is (gate, fragment); `gate` is a
# rule id or a tuple of rule ids that must ALL be enabled for the fragment to appear. A disabled gate drops its
# fragment, so the slot regex that matched it fails (KILLS the slot). An empty tuple is no gate: the fragment is read
# straight off the base push sheet and always appears. Since revision 5 a gate may also be a CONDITIONS name (a test on
# the SQL's own words, not a rule) and a fragment may be a function of the state.
TEXT = {
    ("Collect & Win", TODO_FIELD): [
        ("R_REVIEW_FLAGS", _vial_todo),                     # "the final vial models (Claire)" since the revision-5 SQL
        ("R_ICON_SCOPE", "the Collect & Win event icon animation (Marcus)"),
        ("R_DONE_DEPLOY", _windows_todo),
    ],
    ("Season Pass", TODO_FIELD): [
        ("R_REVIEW_FLAGS", "premium strip moves to the November range (Oliver)"),
        (("R_HANDOFF_SLIP", "R_LOCK_BOUNDARY"),
         "the November config must land before Oct 31 00:00 UTC (Brian's Oct 31 10:00 Istanbul is ~7h late)"),
    ],
    # Empty since the revision-5 SQL (the note says the current quests keep running either way; no rule and no slot). The
    # fragment appears only on an older SQL, where the note read as work the beat waits for.
    ("Quests", TODO_FIELD): [
        (("R_SCOPE_BEATS", "note:quest-set-waits"), "the new quest set lands with the Mon Oct 13 rollover (Brian)"),
    ],
    # Empty through revision 9. The brief asks which weeks these two run, the quest note says "weekly rollover" and the daily
    # gift resets daily. No slot reads either cell.
    ("Quests", WEEKS): [(("R_SCOPE_BEATS", "sql:rev10"), "All four weeks")],
    ("Daily Login", WEEKS): [(("R_SCOPE_BEATS", "sql:rev10"), "All four weeks")],
    # Empty through revision 11. A held beat keeps its usual windows and weeks on its row (the Held status is the mark), and
    # the running October season clips to the span's start. No slot reads these cells and no rule decides them, so the gate
    # is the marker alone.
    ("Weekly Leagues", FIRST_WINDOW): [("sql:rev12", "Mon Oct 6 00:00 UTC")],
    ("Weekly Leagues", WEEKS): [("sql:rev12", "All four weeks")],
    ("Season Pass", FIRST_WINDOW): [("sql:rev12", "Mon Oct 6 00:00 UTC")],
    ("Weekly Leagues", TODO_FIELD): [
        ("R_TECH_HOLD", _leagues_fix),
    ],
    ("1-day lapse", MISSING): [
        ("R_COPY_CURRENT", "old-title copy fix - the English copy still names 'Puzzles vs Zombies'"),
    ],
    ("D0-1 FTUE", MISSING): [
        ("R_COPY_CURRENT", "old-title copy fix - the English copy still names 'Puzzles vs Zombies'"),
    ],
    ("Plague Race start", MISSING): [
        ("R_WIRED", "the row is Ready but the push sheet's Status (NA, WIP, LIVE) column reads WIP, not LIVE"),
    ],
    ("Weekly Leaderboard reset", MISSING): [
        ("R_WIRED", "the row is Ready but the push sheet's Status (NA, WIP, LIVE) column reads WIP, not LIVE"),
    ],
    ("Quests rollover push", MISSING): [
        ((), "the row is Not Ready"),
    ],
    ("Win & Collect event start", MISSING): [
        ((), "the row is Not Ready and WIP, not LIVE; its copy uses the Domino name 'Win & Collect'"),
    ],
    ("Login Calendar update", MISSING): [
        ((), "the row is Not Ready and WIP, not LIVE"),
    ],
    ("Season Pass activation", MISSING): [
        ((), "the row is Not Ready and WIP, not LIVE"),
    ],
}

# The wrong value a control member takes on one of its rule's decided fields when that rule's over-application
# operator is degraded (difficulty_mutation and oracle_kit contract.controls exercise this separability).
def _over_value(field):
    return {STATUS: "Held", SEND_HOLD: "Held",
            FIRST_WINDOW: "waits for the Oct 8 backend release",
            WEEKS: "Weeks 1-3 (one-off assumed)",
            TODO_FIELD: "(over-applied - a task this beat does not need)"}.get(field, "Held")


def _rule_off(state, rule, key, disable):
    """A rule is off for a key when it is disabled (whole or per key) or its deciding records are missing."""
    return _off(disable, rule, key) or not _has(state, *DECIDING.get((rule, key), []))


def _scalar(state, key, field, disable):
    correct, rule, off = SCALAR[(key, field)]
    if rule and _rule_off(state, rule, key, disable):
        return off
    return correct


def _text(state, key, field, disable):
    parts = []
    for gate, frag in TEXT[(key, field)]:
        gates = gate if isinstance(gate, tuple) else (gate,)
        if all(CONDITIONS[g](state) if g in CONDITIONS else not _rule_off(state, g, key, disable) for g in gates):
            parts.append(frag(state) if callable(frag) else frag)
    return "; ".join(parts)


def _sid(ref):
    """The id a seeded Slack message row carries: sha256("<channel>|<ts>")[:32]."""
    ch, ts = ref.split("/")
    return hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]


def _carrier(state, rec, known=None):
    """The id a deciding record has in this SQL. A plain id is itself; a moved note (a tuple of carriers, newest
    first) is the first carrier the SQL holds - or, with no SQL index, the first one in `known`, else the newest."""
    if not isinstance(rec, tuple):
        return rec
    have = known if known is not None else (state.get("ids") if isinstance(state, dict) else None)
    return next((r for r in rec if have and r in have), rec[0])


def _has(state, *ids):
    """Every deciding record is present in the SQL; base records live in the exports and are always present."""
    have = state.get("ids") if isinstance(state, dict) else None
    if have is None:
        return True
    return all(_carrier(state, i) in have for i in ids if i not in BASE)


def _off(spec, name, key):
    """True when `name` is disabled/applied for `key` (whole, or via a (name, key set) pair)."""
    for d in spec:
        if isinstance(d, tuple):
            if d[0] == name and key in d[1]:
                return True
        elif d == name:
            return True
    return False


def _uniq(seq):
    out, seen = [], set()
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def load_state(sql_text, revision=None):
    """The injected records, parsed as data (never executed), indexed by id and by table."""
    try:
        from base_check import parse_sql
    except ImportError:                                   # direct use outside the tool bundle
        import pathlib
        import sys
        for parent in pathlib.Path(__file__).resolve().parents:
            if (parent / "tools" / "base_check.py").is_file():
                sys.path.insert(0, str(parent / "tools"))
                break
        from base_check import parse_sql
    inserts = [x for x in parse_sql(sql_text) if x["op"] == "insert"]
    ids, by_id, tables = set(), {}, {}
    for x in inserts:
        r = x["row"]
        tables.setdefault(x["table"], []).append(r)
        found = []
        for c in ("id", "identifier", "document_id", "spreadsheet_id", "presentation_id", "event_id", "thread_id",
                  "card_id", "issue_id", "commit_id", "comment_id"):
            if r.get(c):
                found.append(str(r[c]))
        if r.get("ts") and (r.get("channel_id") or r.get("channel")):   # a Slack row is also reachable as channel|ts
            ref = f"{r.get('channel_id') or r.get('channel')}/{r['ts']}"
            found.append(ref)
            found.append(_sid(ref))                                      # the row id, sha256 of the same ref
        for v in found:
            ids.add(v)
            by_id.setdefault(v, []).append((x["table"], r))
    return {"ids": ids, "by_id": by_id, "tables": tables, "revision": revision or REVISIONS[-1],
            "rows": len(inserts), "counts": {t: len(v) for t, v in tables.items()}}


def _groups(key):
    """The row's groups: the deliverable, plus the shared Status group the calendar volume slot (V01) counts over."""
    return ["pushes"] if key in PUSHES else ["calendar", "calendar:Status"]


def _placeholder(state, key, field, disable, degrade):
    """A clearly-marked stand-in value plus the rules/operators that reach this key+field.

    The marker is the wiring proof, not the answer: `[R_X:natural]` says the rule is off for this key (or lost its
    deciding records) on a field it decides, `[over:...]` says that over-application operator reaches this key (as a
    decided key or a control member). Deterministic: markers are sorted.
    """
    marks = []
    for rule in RULES_ORDER:
        fields = DECIDES_FIELDS.get(rule, [])
        if field not in fields:
            continue
        if key in TOUCHED.get(rule, ()) and (_off(disable, rule, key)
                                             or not _has(state, *DECIDING.get((rule, key), []))):
            marks.append(f"{rule}:natural")
        op = RULES[rule].get("over_application")
        members = set(TOUCHED.get(rule, ())) | set(CONTROL_KEYS.get(rule, []))
        if op and key in members and _off(degrade, op, key):
            marks.append(op)
    base = f"TODO_{key}_{field}"
    marks = _uniq(marks)
    return base if not marks else base + " [" + " ".join(sorted(marks)) + "]"


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    """The expected value of every row.

    Per key and field, this is what decides it (manifest `decides` + `controls` + the surface selectors). Records are
    the DECIDING ids above; the rule order is RULES_ORDER.

    "Plague Race"
      Status            R_INFRA_SCOPE (D10): the queue manager (CMT_ZOM543, #459, #472) does not order the Plague
                        Race panel, yet players still enter, score and claim -> Runs. Over-apply:
                        over:an-unqueued-panel-holds-the-beat -> Held.  Surface C01 (accepted: Runs/Run/Go/Live).
      Weeks running     R_WITHDRAWN (T2/CH2): Robert's approval (SLACK_APPROVAL) vs his later DM withdrawal
                        (SLACK_WITHDRAW, a top-level message: "pulling my ok"; the brief makes his later word the one
                        that counts) -> All four weeks. Over-apply: over:every-one-off-dropped.  Surface S02.
      Still to do       none raised: "nothing left" (an empty cell). Surface S07-style missing_values apply.
    "Collect & Win"
      First window      R_DONE_DEPLOY (T1/CH1): server windows are DEV-only until EVT_RELEASE (Oct 8 15:00-16:00 UTC)
                        and the first window that opens after it, on the brief's Mon-Tue/Wed-Thu/Fri-Sun 00:00 UTC
                        cadence, is Fri Oct 10 00:00 UTC. Over-apply: over:every-beat-waits-for-a-release.
                        Surface S01 (accepted outcomes list the allowed renderings).
      Status            C05: a live beat once its prod windows open; the queue/addressables gaps do not hold it, and
                        the brief says a beat whose server windows are waiting on the release starts late, it is
                        not held -> Runs.
      Still to do       three owners, one cell: R_REVIEW_FLAGS (NOTE_VIALS on #468: the final vial models, Claire) +
                        R_ICON_SCOPE (CMT_ZOM465 vs NOTE_ICON, Marcus's later note on the same ticket, NOTE_ICON_NEEDED,
                        Brian's that it has to land, and #454/#456/#475: the C&W event icon is absent) + R_DONE_DEPLOY.
                        Surfaces S08 (vial) and S11 (icon).
      Weeks running     n/a (the event runs to the end of the buy weeks).
    "Season Pass"
      Status            R_HOLD_SCOPE (D7, D8): the open issues are analytics -> Runs.  Surface C04.
      First window      Mon Oct 6 00:00 UTC since revision 12 (the running October season, clipped to the span). No slot.
      Still to do       R_HANDOFF_SLIP (T8/CH3: MAIL_0926 moves Oct 29 -> Fri Oct 31 10:00 Istanbul) +
                        R_LOCK_BOUNDARY (T9: the 24 h lock before the Nov 1 00:00 UTC opening makes it late; state
                        Oct 31 00:00 UTC / Oct 30 17:00 PDT) + R_REVIEW_FLAGS (NOTE_STRIP on #472: premium strip ->
                        November, Oliver).  Surfaces S09 (premium|strip|banner) and S10 (the lock regex). The season is
                        "the November season" (no season numbering exists in base).
      Weeks running     n/a.
    "Endless Monster Mode"
      Status            R_HOLD_SCOPE: its open items are visual, polish or analytics (CMT_ZOM504, CMT_ZOM565,
                        CMT_ZOM521) -> Runs.
                        Surface C02.
    "Weekly Leagues"
      Status            R_TECH_HOLD (T7/CH4): the Sep 22 "working fine" note (CMT_ZOM429) is overturned by Vincent's
                        Sep 30 re-test (SLACK_RETEST: no new week even after two restarts) -> Held. Over-apply:
                        over:every-restart-fault-held.  Surface S03 + the ZOM-429 note (W05).
      First window      Mon Oct 6 00:00 UTC since revision 12: a held beat keeps its usual windows and weeks on its row. No slot.
      Weeks running     All four weeks since revision 12, the same sentence. No slot.
      Still to do       the restart fix, owner Douglas, the ZOM-429 assignee (surface W05 writes the hold note).
    "Quests"
      Status            R_SCOPE_BEATS (T3/R1): the rollover is a reset the brief puts on the calendar -> in and Runs;
                        the ZOM-534 restart-clearing fault is a known issue, not a hold.  Surface S04.
      Still to do       none since revision 5: the quest note (TRELLO_QUESTS, Leonard on the open quests card #61)
                        says the weekly rollover does not wait on them, so nothing has to land before the beat runs.
                        No rule and no slot (R_QUEST_SET and S06 are retired); T12 is an ungraded distractor.
      Weeks running     All four weeks since revision 10 (the weekly rollover). No slot.
    "Daily Login"
      Status            R_SCOPE_BEATS -> in and Runs (the daily gift; ZOM-556: claiming works, the counter is
                        cosmetic). Surface S05.
      Weeks running     All four weeks since revision 10 (the gift resets daily). No slot.
      Still to do       R_DONE_ELSEWHERE (T10): Calvin's Sep 24 note on ZOM-432 (CMT_ZOM432) says the frame is
                        still needed, but the ticket is Done and Samuel's closing note on it (NOTE_FRAME) says the
                        frame went out with PR #471 and is in both Sep 30 submission builds (iOS 50, Android 135)
                        -> nothing left (empty cell). One ticket decides it since revision 5.  Surface S07.
    "1-day lapse"       R_COPY_CURRENT (T4): Ready, but the English copy still says "Puzzles vs Zombies" -> Held.
                        What is missing: the old-title copy fix. Surfaces P01 + P06.
    "D0-1 FTUE"         R_COPY_CURRENT: same old title -> Held. Surface P02.
    "Plague Race start" R_WIRED (T5): Ready but "Status (NA, WIP, LIVE)" reads WIP, not LIVE -> Held. Surface P03.
    "Weekly Leaderboard reset"  R_WIRED: the same Ready + WIP row -> Held. Surface P07.
    "Lives recharged"   R_ASK_FOLLOWUP (T15): Ready + LIVE and the copy names no game at all; SLACK_FOLLOWUP says such
                        copy may go out (the naming rule is only about wrong names) -> Send. Without the follow-up
                        the brief's naming sentence, read strictly, gives Held.  Surface P04.
    "7-day lapse"       R_ASK_FOLLOWUP: same -> Send.  Surface P05.
    "Quests rollover push"       the row is Not Ready -> Held (no rule: the brief's plain Ready-and-LIVE test).
    "Win & Collect event start"  Not Ready + WIP, and the copy uses the Domino name "Win & Collect" -> Held.
    "Login Calendar update"      Not Ready + WIP -> Held.
    "Season Pass activation"     Not Ready + WIP -> Held.
    The key set itself is the amendment's other half: ten push rows (Hourly Coins, Nathan's Treasure Hunt, Streak
    Fever and Axe Arena left off) and seven beats (Zombie Lane off) - surface slots V02 and V01.
    """
    out = {}
    for k in (keys_ or keys()):
        is_push = k in PUSHES
        fields = PUSH_FIELDS if is_push else BEAT_FIELDS
        row = {"Push" if is_push else "Beat": k}
        for f in fields:
            if (k, f) in SCALAR:
                row[f] = _scalar(state, k, f, disable)
            elif (k, f) in TEXT:
                row[f] = _text(state, k, f, disable)
            else:
                row[f] = ""
            # over-application: degrading a rule's operator pushes its CONTROL members (never its own decided keys)
            # to the wrong value on each field that rule decides, so the over-reach is separable from the decision.
            for _r in RULES_ORDER:
                op = RULES[_r].get("over_application")
                if (op and f in DECIDES_FIELDS.get(_r, ()) and k in CONTROL_KEYS.get(_r, ())
                        and k not in TOUCHED.get(_r, ()) and _off(degrade, op, k)):
                    row[f] = _over_value(f)
                    break
        row["groups"] = _groups(k)
        row["evidence"] = _uniq([_carrier(state, i) for f in fields for i in _deciding_all(k, f)]
                                + _legacy_evidence(state, k))
        out[k] = row
    return out


def aggregates(rows):
    classes = dict(collections.Counter(v.get(CLASS_FIELD) for v in rows.values() if v.get(CLASS_FIELD)))
    groups = {}
    for k in sorted(rows):
        for g in rows[k].get(GROUPS_FIELD) or []:
            groups.setdefault(g, []).append(k)
    return {"classes": classes, "groups": groups}


def evidence(rows, key, field):
    """The records that decide one field of one row.

    With no rows (truth.json / documentation) it returns every deciding record for the cell. With the solved rows
    (the golden spot-check supplies them), a NON-EMPTY reconciled value has no single record that states it verbatim
    - this task's difficulty is exactly that the answer is computed across records - so it returns [] and the
    spot-check honestly marks the cell unverified rather than wrong; an empty-answer cell returns its deciding
    records so the check confirms they exist (presence)."""
    if field in ("Beat", "Push"):
        return []
    if rows and (rows.get(key) or {}).get(field) not in (None, ""):
        return []
    known = set((rows.get(key) or {}).get("evidence") or ()) if rows else set()   # the carriers solve() resolved
    return _uniq([_carrier(None, i, known) for i in _deciding_all(key, field)])


def _deciding_all(key, field):
    """Every deciding record of one cell, as declared (a moved note still as its tuple of carriers)."""
    if field in ("Beat", "Push"):
        return []
    ids = []
    for rule in RULES_ORDER:
        if key in TOUCHED.get(rule, ()) and field in DECIDES_FIELDS.get(rule, []):
            ids.extend(DECIDING.get((rule, key), []))
    ids.extend(PLAIN_EVIDENCE.get(key, []))
    return _uniq(ids)


def touched(state, rule):
    return set(TOUCHED.get(rule, ()))


def deciding(state, rule, key):
    """The fact-specific seeded records that isolate this rule's decision, for the mutation intervention. The shared
    brief (the rulebook every rule reads) and base records are excluded, so removing these records moves only this
    rule's own keys (never the whole brief-dependent lattice); a rule whose decision rests only on the shared brief
    plus a base surface (R_COPY_CURRENT, R_WIRED - the base push sheet's copy / WIP column) returns [] and its
    intervention is reported UNSUPPORTED, its load-bearingness carried by the clean per-rule disable instead. The
    whole dependency (including the brief) stays in DECIDING and gates the rule in _rule_off / evidence().
    A Slack ref is carried in the SQL under its sha256 id, so it is mapped to that id to match the intervention's
    injected-row index (the state indexes a Slack row by both forms, so _rule_off / evidence() are unaffected).
    R_ASK_FOLLOWUP returns the follow-up reply's own row id: removing it moves only Lives recharged and 7-day lapse.
    R_SCOPE_BEATS has fact-specific records for Daily Login only since revision 5 (the Quests row rests on the brief
    and the base push sheet), so its intervention moves Daily Login alone."""
    out = []
    for r in DECIDING.get((rule, key), []):
        r = _carrier(state, r)
        if r == BRIEF or r in BASE:
            continue
        out.append(_sid(r) if re.fullmatch(r"[A-Z0-9]{8,}/\d+\.\d+", r) else r)
    return out


# (pattern, service, file, pointer, field) - the export location of a base record, read by tools/hg.py records.
# Base records the solver routes are checked; unrouted ones are reported unverified.
BASE_ROUTES = [
    (r"#rc_\d+$", "github", "data.json", "/review_comments", "id"),
    (r"#rev_\d+$", "github", "data.json", "/reviews", "id"),
    (r"#c_\d+$", "github", "data.json", "/pull_request_comments", "id"),
    (r"#ev_\d+$", "github", "data.json", "/timeline_events", "id"),
    (r"^harmonygames-Games/[A-Za-z0-9_.-]+#\d+$", "github", "data.json", "/pull_requests", "id"),
    (r"^ZOM-\d+$", "linear", "data.json", "/issues", "identifier"),
    (r"^cmt_[A-Za-z0-9_]+$", "linear", "data.json", "/comments", "id"),
    (r"^evt_[0-9a-f]+$", "gcal", "data.json", "/events", "event_id"),
    (r"^[a-z0-9._%+-]+@harmonygames\.co/<", "gmail", "threads/*.json", "/messages", "id"),
    (r"^[A-Z0-9]{8,}/[0-9]+\.[0-9]+$", "slack", "messages/*/*.json", "", "id"),
    (r"^[0-9a-f]{24}$", "trello", "data.json", "/actions", "id"),
    (r"^page_[a-z0-9_]+$", "confluence", "confluence_working.json", "/pages", "id"),
    (r"^d_[0-9a-f]{20,}$", "gdrive", "data.json", "/drive_files", "id"),
]
# The f_-prefixed ids are ambiguous by prefix (a doc, a deck and two sheets); route them by name.
F_ROUTES = {
    BRIEF: ("gdocs", "data.json", "/docs_documents", "document_id"),
    UA_PLAN: ("gslides", "data.json", "/slides_presentations", "presentation_id"),
    CALENDAR_SHEET: ("gsheets", "data.json", "/sheets_spreadsheets", "spreadsheet_id"),
    PUSH_SHEET: ("gsheets", "data.json", "/sheets_spreadsheets", "spreadsheet_id"),
}


def base_route(record_id):
    """Where a base deciding record lives in the exports (read through tools/hg.py records by the golden check).
    Seeded records (everything not in BASE) are read from the injection SQL index, so they route to None here."""
    rid = str(record_id or "")
    if rid not in BASE:
        return None
    if rid in F_ROUTES:
        service, file, pointer, field = F_ROUTES[rid]
        return {"service": service, "file": file, "pointer": pointer, "field": field}
    for pattern, service, file, pointer, field in BASE_ROUTES:
        if re.search(pattern, rid):
            return {"service": service, "file": file, "pointer": pointer, "field": field}
    return None

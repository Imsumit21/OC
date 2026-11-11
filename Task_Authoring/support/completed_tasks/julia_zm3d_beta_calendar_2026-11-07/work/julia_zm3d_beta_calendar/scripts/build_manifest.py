#!/usr/bin/env python3
"""Build Working_Files/01_Hardness_Manifest.draft.json for julia-zm3d-beta-liveops-calendar (scenario stage) and,
from it, the final Working_Files/01_Hardness_Manifest.json (injection stage: the draft + the keys at the end).

Every id below is either a base record read through tools/hg.py (base_pointers) or a planned seed minted and
collision-checked in research/R_C_carriers_ids.md §7 (seeded_ids). Re-run after any design change:
  python3 -B Task_Authoring/task_inputsS/Working_Files/research/scripts/build_manifest.py

Revision 2 (SQL 3afbf7cb…): Frederick's thread reply under his own ask (FOLLOWUP, fragment K17, trap T15, rule
R_ASK_FOLLOWUP) makes the push plan the PNs Beta tab row by row minus four named rows, lets copy that names no game go
out and keeps Zombie Lane off the calendar. Zombie Lane is therefore no beat: D9 is a scope distractor, no rule
controls or decides a Zombie Lane row, and the three cohort members that existed only for it (ZOM-442, #297, #308)
and the reads that served only it (the zombie-lane fault thread, match3d-backend#10) left the cohort and the budget.

Revision 3 (SQL 837d4f5d…, 78 INSERT + 34 UPDATE): the repair for the second /prompt FAIL (Cross-Service Coherence,
known-issue card SC-15: the base ZOM-521 master checklist ticks all six items while its children ZOM-526 and ZOM-528
are In Progress). The SQL now seeds the ZOM-521 description with those two items unticked and one later note from
the ticket's creator on ZOM-526 (CMT_ZOM526_2). The design does not move: no requirement, fragment, authority, trap,
chain, cohort member, budget row or portfolio rule changes. The new comment is listed with the seeded rows of the
per-issue comment surface, and the final manifest carries the digest of the revision-3 solver (REVISIONS advanced,
truth unchanged).
SC-15 gets no hazard_acknowledgements entry. That field takes coherence_hazards.json ids only: hardness_gate's
hazard_scope fails any other id as "unknown hazard id" (probed on 2026-11-06 with hazard_id SC-15), `repaired` is
verifiable for Linear L01-L07 alone, and no KB hazard covers a description checklist (ZOM-521 is In Progress, so the
parent-Done-while-child-open type does not apply). The repair is recorded in the dossier (§10 and §11 Revision 3)
and in the design (§2) instead, so it is not silent.

Revision 4 (SQL c955d6ca…, 75 INSERT + 31 UPDATE): the repair for the independent /prompt run on revision 3
(research/prompt_review_rev3/; Cross-Service Coherence 2, Clarity 3). The transform is apply_review_fix_rev4.py. The
answer key does not change. What changes here:
  - three owner notes left long-merged PRs: vial sprites -> an inline review note on #468 before its merge (REV468 /
    RC468), premium strip -> a conversation note on #473 (C473), C&W icon animation -> Marcus's second note on
    ZOM-465 (CMT_ZOM465_2). T11, T14, CH6, the cohort surfaces' seeded rows and the fact home ids follow them;
  - five tickets are Done in the seeded state (DONE_REV4), so they are no longer open ZOM issues and leave the cohort
    as it is defined (K6): 16 issues + 23 PRs = 39 members, ONE SHORT of the extreme minimum of 40. No
    cohort_exception is written here: it needs the requester's confirmation. The three PRs whose notes moved (#370,
    #438, #454) stay: each is in the cohort for a fact in its own body / commits / files, not for the note;
  - T10 is weaker (ZOM-432 is itself Done), T2 is weaker (the retraction is a top-level DM message), T14 is weaker
    (both notes sit on ZOM-465), T8's correction is a mail of its own; each trap says so in its own text;
  - the budget loses the five closed tickets' comment reads, the thread-open call for the retraction and the extra
    PR #471 read: 200 -> 192 unconditional, per-record surfaces 138 -> 133 (floors 130 / 75);
  - L03 is `repaired` (the SQL moves ZOM-387 to In Progress; base_check verifies it on the post-SQL state).
For a further small revision: move a note by re-pointing its one constant below; reopen a ticket by taking it out
of DONE.

Revision 5 (SQL 3c035f2a…, 70 INSERT + 26 UPDATE): the repair for the independent /prompt run on revision 4 and the
claim-by-claim audit of every injected record (research/prompt_review_rev4/, research/prompt_review_rev5_audits/).
The transform is apply_review_fix_rev5.py. The answer key changes in two cells (Quests still-to-do is empty; the
Collect & Win vial item reads "the final vial models (Claire)"). What changes here:
  - ids: the five Slack messages people wrote have new ts values (row ids are computed from them by sid() and
    asserted against the SQL), Brian's two mails have new Message-IDs and per-mailbox thread ids, the three
    #zombie-prs mirror rows have new ids and there is no #471 mirror;
  - the quest note is Leonard's, on the open quests card #61, and says the current set carries the first week. It
    decides no graded value: R_QUEST_SET is retired (fourteen rules), fragment K11 is dropped (16 fragments, 7
    services, 10 containers - each at or above its floor), T12 keeps its id as an UNGRADED distractor, T3 loses its
    Trello record and service, and Trello carries no weight (no weight_reason, no budget call);
  - Confluence is declared: the base page_season_pass_spec ("locked 24h before each season opens") is the only
    source of the 24 h lock offset that S10 / W07 need (T9, CH3; the brief only points to "before its lock"). It has
    carried that weight all along without being listed; it is listed now with the one read it costs. This is what
    keeps the services at ten after Trello's weight went, and it is flagged as such in the dossier;
  - Samuel's frame note is on the ticket it closes (CMT_ZOM432_2; ZOM-432 Done at that instant), nothing is seeded
    on #471. T10 is a trap in name only, CH5 is retired (five chains), R_DONE_ELSEWHERE keeps its id with T10 alone;
  - #470's note is part of Arthur's base approval review (rev_9, nine seconds before the merge); the vial note names
    Claire's 3D vial models; the ZOM-429 owner note is dated Sep 16, before the Sep 22 thread (T7 order);
  - cohort (K6, as written): ZOM-565, ZOM-471 and ZOM-542 are open again in their base states and are back; ZOM-344
    and ZOM-432 are Done and out; ZOM-387 is in, exactly as base has it (Todo, no seeded note): an open ticket that
    names un-instrumented events of Plague Race and quests, the same class as ZOM-549 / 552 / 566. 19 issues + 23 PRs
    = 42 members, no exception needed;
  - budget: +3 per-issue comment reads, -2 Trello calls, +1 Confluence read: 192 -> 194 unconditional, per-record
    surfaces 133 -> 136 (floors 130 / 75);
  - hazard_acknowledgements is empty: the SQL no longer touches ZOM-387, so `repaired` would be false. Because the
    cohort still cites ZOM-387, hardness_gate's hazard_scope asks for a resolution of L03 and none of the three is
    true here (see the dossier, Revision 5); that is reported, not papered over.

Revision 6 (SQL f8d905bd…, 71 INSERT + 26 UPDATE): the repair for the one fork the independent /prompt run on
revision 5 left open (research/prompt_review_rev5/; Unique Ground Truth). The transform is apply_review_fix_rev6.py.
The answer key does not change. What changes here:
  - the quest note says outright that nothing in the beta waits on the new set; T12's resolver quotes the new words;
  - ZOM-526 has a third note (CMT_ZOM526_3, Calvin, Sep 30), listed with the seeded rows of the per-issue surface;
  - the requester's decisions on the three open points of revision 5: (1) ZOM-387 is OUT of the cohort on its merits
    (STATE_UNRELIABLE: a KB L03 record, Todo while its referencing PR merged in July, so "open" is not a reliable
    predicate for it); no manifest section cites it any more, so hardness_gate's hazard_scope passes with an empty
    acknowledgement list. Cohort 41 (18 issues + 23 PRs), per-record surfaces 136 -> 135, budget 194 -> 193
    unconditional; (2) Confluence stays the tenth weight-carrying service and Trello a touched schema with no weight;
    (3) S07 stays a weight-1 lookup (surface unchanged).

Revision 7 (SQL 091722f6…, 72 INSERT + 26 UPDATE): two residuals from the reviews of revision 6
(research/prompt_review_rev6/). The transform is apply_review_fix_rev7.py. The answer key does not change, and neither
does any cohort, budget or surface number. The quest note now says the new quests are additive (T12 quotes it). ZOM-521
has a second note (CMT_ZOM521_2, Calvin, Sep 30), listed with the seeded rows of the per-issue surface because the
ZOM-521 comment call returns it; it decides no key. ZOM-528 stays out of the cohort.

Revision 8 (SQL 0e8c8ad8…, 71 INSERT + 25 UPDATE): the findings of a fresh blind /prompt round on revision 7
(research/prompt_review_rev7/). The transform is apply_review_fix_rev8.py. No graded value changes; one evidence id does.
  - the premium-strip note left #473 for an inline note under Arthur's base approval of #472, six seconds before that
    merge (RC472). All #473 rows are gone. #473 stays a cohort PR (its own body makes it one) and D11's pointer;
  - that note was the only seeded row on the conversation surface. The 42 base conversation comments on the 39 PRs are
    all bots (38 CodeRabbit, 4 Linear), so github_get_issue_comments now carries no fact a rule uses and fails the
    necessity rule (Hardness_Mastery §2.5). It no longer counts: three surfaces, per-record 135 -> 96, budget 193 -> 154
    unconditional, 203 -> 164 planned (floors 75 / 130). This is the measured number, not a design choice to keep;
  - T11 is weaker: both of its notes are inline, so one per-PR call type reaches them where two did through revision 7;
  - the quest note says "The rollover does not wait on them" (T12); the brief gains one sentence on undated holds (R3).

Revision 9 (SQL 892f7edd…, 76 INSERT + 28 UPDATE): the repair for the platform's third /prompt failure (Unique Ground
Truth and Clarity on ZOM-534, the S23 freeze and #477), after a census of every candidate (research/rev9_census/). The
transform is apply_review_fix_rev9.py. No graded value changes.
  - the brief's rules are closed: R3 and R5 follow it. Still to do is a held beat's fix plus what has been flagged for that
    beat as not done since the brief (prod deploy, config or player-facing art); nothing else goes in. K13's quote moves
    to "An established failure holds it". No R_ rule or T_ trap depended on the removed "unverified build or platform"
    clause, so none is retired; what leaned on it was K13's quote, D7's "a still-to-do at most" and the tail of D9's wrong
    reading, all re-worded here;
  - Robert's withdrawal says "the themed prop set I okayed in Martin's thread": T2 is harder to meet and `plague.weeks`
    takes the words the two records share;
  - cmt_zom566_1 is Brian's note and Owen's analytics note is CMT_ZOM566_2; both, and CMT_ZOM534_2, sit on cohort tickets, so
    the per-issue surface lists them. cmt_zom563_1 does not: ZOM-563 goes Done and stays out of the cohort. The two
    #zombie-bugs replies are named in D7 and the dossier. None of these decides a key.

Revision 10 (SQL ffbac458…, 78 INSERT + 29 UPDATE): the pre-review attack on revision 9 (research/rev9_attack/). The
transform is apply_review_fix_rev10.py. Two deliberate value changes: the owners (Douglas on Weekly Leagues' fix and on
Collect & Win's server windows) and "All four weeks" for Quests and Daily Login. R2, R4, R5 and R6 follow the brief's new
words. No fragment quote used the removed "pre-empts" sentence; only R2's prose did. Vincent's reply replaces Oliver's in
the shader thread (D7), and CMT_ZOM565_2 sits on a cohort ticket, so the per-issue surface lists it. No cohort, budget or
per-record number moves.

Revision 11 (SQL 1348d287…, 80 INSERT + 30 UPDATE): the formal blind round on revision 10 (research/prompt_review_rev10/).
The transform is apply_review_fix_rev11.py. No value changes. CMT_ZOM465_3 (Brian: the Collect & Win icon has to land) joins
T14 and the per-issue surface and is the one evidence id added. R2, R3, R8 and R9 follow the brief's new words (closing
23:59, the held-row sentence, "moves to any time before it", the clip sentence), and K1's quote and T11's strip wording
follow the brief and the note. ZOM-542 is Todo, which is still open, so it stays in the cohort. Douglas's reply in
#zm-collect-win is named in the dossier only. No cohort, budget or per-record number moves.

Revision 12 (SQL b5ccbfa5…, 81 INSERT + 30 UPDATE): the verification round on revision 11 (research/prompt_review_rev11/). The
transform is apply_review_fix_rev12.py. Three empty, ungraded cells are filled by design (Weekly Leagues' First window and
Weeks running, Season Pass's First window); no other value and no evidence id moves. R1, R2, R3 and R6 follow the brief's new
words and T11 the vial note. cmt_zom563_1 is Douglas's note and Vincent's check is cmt_zom563_2; ZOM-563 stays out of the
cohort, so no surface lists either. No cohort, budget or per-record number moves.

Revision 13 (SQL 1f2175a2…, 81 INSERT + 30 UPDATE): the cold reviewers' last items on revision 12
(research/prompt_review_rev12/). The transform is apply_review_fix_rev13.py. No value or evidence id moves. R1, R6, T11 and T14
follow the new words. Fact cw.todo.vials takes the note's own words, "final models": the note no longer says "vial models",
and an alias would have left the value stated by no record, so the leak check would have nothing to test. No cohort, budget or
per-record number moves.

Revision 14 (SQL edae63f3…, 81 INSERT + 30 UPDATE): the two items from the last cold P1 on revision 13
(research/prompt_review_rev13/). The transform is apply_review_fix_rev14.py. R8 and R9 follow the two brief sentences. No value,
evidence id, cohort, budget or per-record number moves.
"""
import hashlib
import json
from pathlib import Path

WF = Path(__file__).resolve().parents[2]
ctx = json.loads((WF / "00_Task_Context.json").read_text())

# ---------------------------------------------------------------- ids (planned seeds; base ids marked BASE)
def sid(ref):
    """The row id of a seeded Slack message: sha256("<channel>|<ts>")[:32]."""
    ch, ts = ref.split("/")
    return hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]


# Revision 5: the five messages people wrote have ts values that end in 9 and are off the whole minute. A re-timed
# message costs one ts here; its row id follows (asserted against the SQL's ids below).
ASK = "D05SD5QLG94/1759263617.418209"                 # Frederick -> Julia DM, 2025-09-30T20:20:17Z
ASK_ID = sid(ASK)
FOLLOWUP = "D05SD5QLG94/1759263878.305129"            # Frederick's thread reply under his own ask, 2025-09-30T20:24:38Z
FOLLOWUP_ID = sid(FOLLOWUP)
APPROVAL = "C08R8CHB0QL/1758213623.552919"            # Robert reply in Martin's #zombie-art thread, 2025-09-18T16:40:23Z
APPROVAL_ID = sid(APPROVAL)
HALLOWEEN_ROOT = "C08R8CHB0QL/1758121809.236839"      # BASE Martin's post (no replies in base)
WITHDRAWAL = "D05GU6L0XFH/1759270241.638119"          # Robert in his DM with Julia, 2025-09-30T22:10:41Z; a top-level message
#                                                       since revision 4 (it was a reply under his Sep 30 pivot question)
WITHDRAWAL_ID = sid(WITHDRAWAL)
RETEST = "C0880U9751A/1759265412.481909"              # Vincent prod re-test, #zombie-match3d ROOT (cross-channel), 2025-09-30T20:50:12Z
RETEST_ID = sid(RETEST)
assert (ASK_ID, FOLLOWUP_ID, APPROVAL_ID, WITHDRAWAL_ID, RETEST_ID) == (
    "bca784379e7dbca9e64e79a64dfefbba", "890dc27f56e8501bd7590ffdfc231057", "933cee9f6464a80e4b1f05259b595b20",
    "669d15f685f158633e56302160957f1e", "b5f2955c2e154efc6835946ecfe1758e")
REPORT = "C08R27X0EAH/1758546048.524829"              # BASE Vincent's Sep 22 report (standalone)
OLIVER_THREAD = "C08R27X0EAH/1758546119.789009"       # BASE Oliver's thread
OLIVER_END = "C08R27X0EAH/1758550789.777509"          # BASE "yep, it's working fine right now"
JULIA_NOTES = "C05KNDCHAAG/1758558302.777379"         # BASE "feature completed Win and Collect"
PIPELINE = "C05KNDCHAAG/1757704290.799329"            # BASE Leonard's beta pipeline
AXE = "C05KNDCHAAG/1758558164.541689"                 # BASE Brian: postpone Axe Arena for the beta release
TECH = "C090N54TG79/1758517286.431379"                # BASE Leonard: tech-stable beta, no excuses
BOSS_DEV = "C08R6BF4ENN/1756747348.667629"            # BASE Douglas: BossArena endpoints ready for testing on dev
FAULT_SP = "C08R27X0EAH/1759249488.495439"            # BASE Season Pass shader fault - over-hold distractor (revision 9: a seeded reply says the fix is pushed)
FAULT_ENDLESS = "C08R27X0EAH/1758145553.265559"       # BASE Endless heating fault (unexplained) - over-hold distractor
FAULT_LANE = "C08R27X0EAH/1758903616.346579"          # BASE Zombie Lane fix thread (Android verified, iOS build asked for) - scope distractor (Zombie Lane is off the calendar)
SUB135 = "C05433XK267/1759263189.219529"              # BASE #builds Android Submission #135 changes list
SUB50 = "C05433XK267/1759259749.259909"               # BASE #builds Match 3D iOS Submission #50 (same day, same main)
BRIEF = "f_7c3e91a4d2b85f60e1a9c4"                    # Frederick's beta brief (Doc)
DECK = "f_2b9d4e7a1c63f08d5e7b21"                     # Frederick's beta UA plan (Slides)
CAL = "f_e4a17c90b3d25f6a8c1d73"                      # Julia's beta live-ops calendar (Sheet)
FOLDER = "d_5f2c8e1b7a94d03c6e2b58"                   # Julia's "ZM Live Ops" folder
PUSH = "f_a325dd4af80afc5994d5dc"                     # BASE push sheet (Resource-owned, shared with Julia)
EVT = "evt_9a4c2e7f1b3d58e06c7a2f"                    # Douglas's backend release plan event, Wed Oct 8
EVT_UID = "3f8e1c6a9b2d4e7f0a5c8b1d3e6f9a2c@hg4"
# Revision 5: Brian's base Message-ID shape; per-mailbox thread ids that encode the send time (id >> 20 = ms).
M2_RFC = "<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>"
M1 = "julia.lawson@harmonygames.co/<CAPT--p4sBC8XnaA7qBDMtZkWqJPiXP0MT3deOQGPusOZhHF+vo@mail.gmail.com>"   # Brian, Sep 22 09:12:41Z: Oct 29
M2 = "julia.lawson@harmonygames.co/" + M2_RFC          # Brian, Sep 26 07:40:26Z: Oct 31 10:00 TRT
THREAD_A = "julia.lawson@harmonygames.co/1843954828968533812"
THREAD_B = "julia.lawson@harmonygames.co/1844311412966040123"
TRELLO_QUESTS = "68c452a03006277f55d9dc96"            # BASE open card #61 "Add more quests and balance quest rewards - (Leonard/Douglas)"
#     (through revision 4 the note sat on 6851a724601a61857a1b202f, a card completed on Jun 30)
TRELLO_ACT = "68dac8204f1e9a3b7c2d5e61"               # Leonard's comment on it, 2025-09-29T17:55:44Z; since revision 10:
#     "More quests and the reward balance go in with the Mon Oct 13 rollover if they are ready. The weekly rollover does not
#     wait on them, the current quests keep running either way." It decides no graded value (T12)
RC470 = "harmonygames-Games/match3d#470#rc_10"        # Arthur's inline note inside his BASE approval review rev_9,
#     2025-09-30T15:51:06Z, nine seconds before the merge (through revision 4: under a seeded post-merge rev_10)
# Revision 4: the owner notes that sat on long-merged PRs (#370, #438, #454) live on other records.
REV468, RC468 = "harmonygames-Games/match3d#468#rev_3", "harmonygames-Games/match3d#468#rc_38"   # Arthur, vial sprites:
#     COMMENTED review + inline note on #468 at 2025-09-29T15:36:41Z, before its merge at 16:13:50Z (was #370#rev_1 / rc_1)
RC472 = "harmonygames-Games/match3d#472#rc_1"         # Arthur, premium strip: inline on Assets/RewardVFXManager.cs under his BASE
#     approval #472#rev_1 at 2025-09-30T15:52:58Z, six seconds before the merge (revisions 4-7: #473#c_2, a conversation
#     note 35 min after that PR's merge; through revision 3: #438#rev_4 / rc_74)
# Revision 5: nothing is seeded on #471. Samuel's frame note is cmt_zom432_2 on the ticket it closes (below).
CMT = {k: f"cmt_{k.lower().replace('-', '')}_1" for k in          # ZOM-387 has no seeded note since revision 5
       ("ZOM-78", "ZOM-344", "ZOM-429", "ZOM-432", "ZOM-442", "ZOM-465", "ZOM-471", "ZOM-504",
        "ZOM-517", "ZOM-521", "ZOM-526", "ZOM-534", "ZOM-542", "ZOM-543", "ZOM-544", "ZOM-546", "ZOM-549", "ZOM-552",
        "ZOM-556", "ZOM-565", "ZOM-566")}
# Revision 3: Brian's later note on ZOM-526, 2025-09-26T15:40:00Z (the SC-15 repair). The per-issue comment call on
# ZOM-526 returns it with cmt_zom526_1; it decides no key.
CMT_ZOM526_2 = "cmt_zom526_2"
# Revision 6: Calvin's note on ZOM-526, 2025-09-30T16:24:19Z, 31 minutes after PR #472 merged: the Collect and Win tokens
# go through the queue manager, only the Axe Arena travel is left (an event postponed for the beta). It decides no key.
CMT_ZOM526_3 = "cmt_zom526_3"
# Revision 7: Calvin's second note on ZOM-521, 2025-09-30T16:27:38Z, 18 minutes after PR #475 merged: the card pack animation
# went in, and the item and ZOM-528 stay open until Brian has seen it in a build. It decides no key.
CMT_ZOM521_2 = "cmt_zom521_2"
# Revision 9: Leonard's confirmation on ZOM-534, which he reported, and Owen's analytics note on ZOM-566, which moved to the
# second id because Brian's note comes first in time: CMT["ZOM-566"] (cmt_zom566_1) is Brian's note since revision 9. The
# per-issue comment calls return all of them. None decides a key.
CMT_ZOM534_2, CMT_ZOM566_2 = "cmt_zom534_2", "cmt_zom566_2"
# Revision 10: Brian's note on ZOM-565, 2025-09-30T16:12:27Z: the endless core-game VFX and the refill timer are the same P1/P2
# polish and do not have to land before the beta. The per-issue comment call returns it. It decides no key.
CMT_ZOM565_2 = "cmt_zom565_2"
# Revision 4: Marcus's later note on ZOM-465, 2025-09-30T18:05:00Z: the Collect & Win event icon animation is still to
# do (was his #454 conversation note). The per-issue comment call on ZOM-465 returns it after cmt_zom465_1.
CMT_ZOM465_2 = "cmt_zom465_2"
# Revision 11: Brian's note on ZOM-465, 2025-09-30T18:13:41Z: the Collect & Win icon has to land before the event runs. The same
# per-issue comment call returns it, after Marcus's two notes.
CMT_ZOM465_3 = "cmt_zom465_3"
# Revision 5: Samuel's closing note on ZOM-432, 2025-09-30T21:07:26Z (the ticket is Done at the same instant): the frame
# went out with PR #471 and is in both submission builds, iOS 50 and Android 135. ZOM-432 is no cohort member (Done).
CMT_ZOM432_2 = "cmt_zom432_2"

# Revision 2: ZOM-442 (trophy-road redeem analytics), #297 (Finishing Zombie Lane) and #308 (polish/zombie-lane)
# existed only for Zombie Lane, which Frederick's follow-up keeps off the calendar, so they are no cohort members and
# no required reads any more (cmt_zom442_1 stays seeded as an ordinary note; nothing cites it).
ALL_ISSUES = ["ZOM-78", "ZOM-344", "ZOM-387", "ZOM-429", "ZOM-432", "ZOM-465", "ZOM-471", "ZOM-504",
              "ZOM-517", "ZOM-521", "ZOM-526", "ZOM-534", "ZOM-542", "ZOM-543", "ZOM-544", "ZOM-546", "ZOM-549", "ZOM-552",
              "ZOM-556", "ZOM-565", "ZOM-566"]                            # the 21 decision-bearing live-ops issues, open in base
# The cohort is the OPEN issues (K6: what still has to land, not what already shipped). Revision 5: the SQL closes two
# Done - ZOM-344 at Marcus's sign-off note and ZOM-432 with Samuel's closing note - and they leave it; their seeded
# comments stay as ordinary notes, like cmt_zom442_1. ZOM-471, ZOM-542 and ZOM-565 (closed by revision 4) keep their
# base states and are back (ZOM-542 is Todo since revision 11, base Regression: it was never started, and it is still
# open). ZOM-566 is In Progress and stays.
# Revision 6 (the requester's decision): ZOM-387 is out on its merits. It is a KB L03 record - Todo while its referencing
# PR merged in July - so its "open" state is not reliable, and the KB's guidance is to keep such issues out of a cohort
# whose predicate is "open". The SQL does not touch it, and no manifest section names it any more (the gate's
# hazard_scope reads the cohort text too, so the rule text below describes the ticket without its key).
DONE = ("ZOM-344", "ZOM-432")
STATE_UNRELIABLE = ("ZOM-387",)
ISSUES = [k for k in ALL_ISSUES if k not in DONE + STATE_UNRELIABLE]      # 18 open live-ops issues at the clock
GPRS = (270, 303, 317, 328, 336, 370, 382, 394, 400, 408, 419, 438, 447, 454, 456, 459, 465, 468, 470, 471, 472, 473, 475)
READ_PRS = (259, 270, 296, 303, 306, 315, 317, 328, 336, 338, 353, 356, 357, 360, 364, 370, 382, 384, 394, 396,
            397, 400, 403, 405, 408, 419, 420, 438, 447, 454, 456, 459, 465, 468, 470, 471, 472, 473, 475)
assert len(ALL_ISSUES) == 21 and len(ISSUES) == 18 and len(GPRS) == 23 and len(READ_PRS) == 39
PRS = [f"harmonygames-Games/match3d#{n}" for n in GPRS]

REQ = {
    "R1": "Beat column: every ZM3D beat players can see in the four beta buy weeks (a window, a reset or a start push); "
          "Boss Arena and Axe Arena are off this calendar, and so is Zombie Lane (a "
          "permanent track with no window or reset to plan, per Frederick's follow-up under his ask); the rotating shop is not a beat",
    "R2": "First window (UTC) column: a beat starts with the first window that opens after its server windows are live on "
          "prod (the backend release instant, read in UTC), not when its client PRs merged; Collect & Win's Mon-Tue / "
          "Wed-Thu / Fri-Sun windows open 00:00 UTC; every window closes 23:59 UTC on its last day",
    "R3": "Status column: a beat is held only when players provably cannot enter, score or claim on prod even after a "
          "restart (an established failure holds it, an unverified one does not), or when an in-scope live-ops PR (the Aug-Sep merged cohort) carries an unresolved change-request "
          "review blocker; a hold with no dated fix runs until the fix is confirmed on prod, and a held beat keeps its usual windows and weeks on its row, marked held; a beat whose server windows are waiting on the backend release starts late, it is not held; restart-clearing faults, wrong counters, cosmetic, VFX, performance and analytics gaps do not hold it, nor does a change-request outside the cohort window (e.g. the July #303)",
    "R4": "Weeks running column: which weeks a beat runs, All four weeks for the quest rollover and the daily gift; a "
          "one-off may take a recurring beat's slot only with Product's (Robert's) latest dated approval",
    "R5": "Still to do column: a closed list of what each beat still needs before it runs for bought users, with its "
          "owner: its fix if it is held, and anything flagged since the brief as still needed for it (prod deploy, "
          "config or player-facing art); nothing else goes in, so not what already shipped, not analytics, not polish "
          "nobody flagged",
    "R6": "Pushes tab: the push plan is the PNs Beta tab row by row, local notifications included, with the four rows for "
          "things that are not in the beta (Hourly Coins, Nathan's Treasure Hunt, Streak Fever, Axe Arena) left off; a "
          "push goes out only if its row is Ready and LIVE and the English copy on that row names the game as Zombie Match 3D "
          "and events by their ZM3D names (Login Calendar and Weekly Rankings are fine), and Frederick's follow-up adds that copy that names no game at all is fine (the "
          "naming rule is only about wrong names); anything else is held with which of those its row is missing",
    "R7": "Destinations: the calendar in Julia's calendar sheet, its link on the calendar ticket, a note on the ticket of a "
          "beat that ends up held so its owner picks it up, and the recommendation with tradeoffs as a reply in "
          "Frederick's DM",
    "R8": "Config locks: every config a beat needs lands before its lock, read in server time (UTC); a committed date that "
          "misses the lock moves to any time before it and you tell its owner in a reply on the mail where they committed to it",
    "R9": "Span: the four buy weeks Mon Oct 6 00:00 UTC - Sun Nov 2 23:59 UTC, with anything that starts before or runs past "
          "that clipped to those two instants and windows stated in server time (UTC); Endless goes down as its weekly windows, "
          "with the daily reset noted",
}

SERVICES = {
    "slack": {"role": "the ask and Frederick's follow-up under it, the one-off approval and its withdrawal, the prod "
                      "re-test, fault threads, the reply",
              "weight_reason": "Frederick's ask is the anchor and the reply destination (R7), and his thread reply under it "
                               "settles the push rows, the copy that names no game and Zombie Lane (R1, R6); Robert's "
                               "#zombie-art approval "
                               "and his later message in his DM with Julia decide the Halloween week (R4); Vincent's Sep 30 re-test "
                               "decides the leagues hold (R3)"},
    "gdocs": {"role": "Frederick's beta brief: the calendar owner's rules",
              "weight_reason": "the scope, deploy, hold, one-off, still-to-do, push and lock rules (R1-R6, R8) live here; "
                               "only the push rows and the Zombie Lane scope are amended elsewhere (Frederick's follow-up)"},
    "gslides": {"role": "Frederick's beta UA plan", "weight_reason": "the four buy weeks that set the calendar's span (R9)"},
    "gmail": {"role": "Brian's Season Pass November handoff",
              "weight_reason": "Brian's Sep 22 date and his Sep 26 slip to Fri Oct 31 10:00 Istanbul time decide the "
                               "November config deadline (R8); the reply to him is a required write"},
    "gcal": {"role": "Douglas's backend release plan event",
             "weight_reason": "the Wed Oct 8 release date fixes Collect & Win's first prod window (R2)"},
    "gdrive": {"role": "Julia's ZM Live Ops folder", "weight_reason": "holds Julia's calendar sheet, the write target (R7)"},
    "gsheets": {"role": "the push sheet and Julia's calendar sheet",
                "weight_reason": "the PNs Beta rows (Ready status, the NA / WIP / LIVE column, copy) decide every push (R6); Julia's sheet carries the "
                                 "column contract and receives the calendar (R7)"},
    "linear": {"role": "open live-ops issues, owner notes, the calendar ticket",
               "weight_reason": "per-issue notes decide holds and still-to-do (R3, R5; Marcus's second note on ZOM-465 "
                                "carries the Collect & Win icon animation, and Samuel's closing note on the Done "
                                "ticket ZOM-432 shows the daily-gift frame shipped); ZOM-78 is the calendar ticket to "
                                "reuse (R7); ZOM-429 takes the hold note (R7)"},
    "github": {"role": "live-ops PRs, their reviews and comments",
               "weight_reason": "Arthur's inline note on #470 holds Collect & Win's server windows to the backend release "
                                "(R2); his inline notes on #468 and #472 add the vial and premium-strip still-to-dos "
                                "(R5)"},
    # Revision 5: no weight_reason. The quest note decides no graded value (the Quests still-to-do is empty and no slot
    # reads it), so no answer needs a Trello read. The key stays because the schema is injected and T12 lives here.
    "trello": {"role": "the open quests roadmap card and Leonard's note on it: context a run may over-read (T12, "
                       "ungraded); carries no weight since revision 5"},
    # Declared in revision 5; it has carried this weight since the brief stopped stating the offset itself. Base only.
    "confluence": {"role": "the base Season Pass spec page (nothing is injected into Confluence)",
                   "weight_reason": "page_season_pass_spec is the only source of the config-lock offset ('locked 24h "
                                    "before each season opens'): with the Nov 1 00:00 UTC opening it gives the Fri Oct 31 "
                                    "00:00 UTC lock that Brian's Oct 31 10:00 Istanbul date misses (R8); the brief only "
                                    "points to 'before its lock'"},
}

ANCHORS = [
    {"id": "A1", "prompt_reference": "Frederick's beta calendar ask", "service": "slack", "locator": ASK,
     "seeded_ids": [ASK], "container": f"slack:{ASK}", "requirement_ids": ["R7"]},
    {"id": "A2", "prompt_reference": "my beta live-ops calendar sheet", "service": "gsheets", "locator": CAL,
     "seeded_ids": [CAL, FOLDER], "container": f"file:{CAL}", "requirement_ids": ["R7"]},
]


def frag(fid, svc, container, locator, via, by, quote, reqs, kind="requirement", seeded=None, base=None, names=None):
    return {"id": fid, "service": svc, "container": container, "locator": locator, "kind": kind, "incorporated_via": via,
            "seeded_ids": seeded or [], "base_pointers": base or [], "delegated_by_record": by,
            "delegation_quote": quote, "requirement_ids": reqs, "names_authorities": names or []}


B = f"file:{BRIEF}"
FRAGS = [
    frag("K1", "gdocs", B, BRIEF, ["A1"], ASK, "working rules for the calendar are in my brief", ["R1"], seeded=[BRIEF]),
    frag("K2", "gdocs", B, BRIEF, ["A1"], ASK, "working rules for the calendar are in my brief", ["R2"], seeded=[BRIEF]),
    frag("K3", "gdocs", B, BRIEF, ["A1"], ASK, "working rules for the calendar are in my brief", ["R3"], seeded=[BRIEF]),
    frag("K4", "gdocs", B, BRIEF, ["A1"], ASK, "working rules for the calendar are in my brief", ["R4"], seeded=[BRIEF]),
    frag("K5", "gdocs", B, BRIEF, ["A1"], ASK, "working rules for the calendar are in my brief", ["R6"], seeded=[BRIEF]),
    frag("K6", "gdocs", B, BRIEF, ["A1"], ASK, "working rules for the calendar are in my brief", ["R5"], seeded=[BRIEF]),
    frag("K7", "gdocs", B, BRIEF, ["A1"], ASK, "working rules for the calendar are in my brief", ["R8"], seeded=[BRIEF]),
    frag("K8", "gslides", f"file:{DECK}", DECK, ["A1", "K1"], BRIEF, "the four buy weeks in my UA plan", ["R9"], seeded=[DECK]),
    frag("K9", "gmail", f"gmail:{THREAD_A}", M1, ["A1", "K7"], BRIEF, "Every config a beat needs lands before its lock", ["R8"], kind="deadline",
         seeded=[M1, THREAD_A], names=[{"id": "H2", "quote": "Season Pass November config handoff"}]),
    frag("K10", "gcal", f"gcal:{EVT_UID}", EVT, ["A1", "K2"], BRIEF, "the backend release instant read in UTC", ["R2"], seeded=[EVT]),
    # K11 (the quest note on Trello, R5) was dropped in revision 5: the note carries no requirement any more. The id is
    # not reused.
    frag("K12", "linear", "linear:ZOM-78", CMT["ZOM-78"], ["A1"], ASK, "the calendar ticket", ["R7"], kind="destination",
         seeded=[CMT["ZOM-78"]], base=["ZOM-78"]),
    frag("K13", "slack", f"slack:{TECH}", TECH, ["A1", "K3"], BRIEF, "An established failure holds it", ["R3"], base=[TECH]),
    frag("K14", "slack", f"slack:{AXE}", AXE, ["A1", "K1"], BRIEF, "Boss Arena is off this calendar until the pivot call", ["R1"], kind="exclusion",
         base=[AXE]),
    frag("K15", "gsheets", f"file:{CAL}", CAL, ["A2"], CAL, "Still to do (owner)", ["R7"], kind="format",
         seeded=[CAL]),
    frag("K16", "gsheets", f"file:{PUSH}", PUSH, ["A1", "K5"], BRIEF, "A push goes out only if its row is Ready and LIVE", ["R6"], base=[PUSH]),
    # Revision 2: Frederick's follow-up is a reply in the ask's own thread. The ask carries no pointing words for it
    # (the parent's reply_count is the pointer), so the binding quote is the thing the reply amends, in the ask's words.
    frag("K17", "slack", f"slack:{ASK}", FOLLOWUP, ["A1"], ASK, "the live-ops and push calendar for the beta buy", ["R1", "R6"],
         kind="amendment", seeded=[FOLLOWUP_ID]),
]

AUTHORITIES = [
    {"id": "H1", "name": "Frederick's beta brief", "home_service": "gdocs", "decoy_service": "slack",
     "governs": ["R1", "R3", "R4", "R6"], "findable_query": "beta brief", "seeded_ids": [BRIEF], "base_pointers": [],
     "decoy_seeded_ids": [], "decoy_base_pointers": [PIPELINE]},
    {"id": "H2", "name": "Brian's Season Pass November handoff", "home_service": "gmail", "decoy_service": "gmail",
     "governs": ["R8"], "findable_query": "Season Pass November", "seeded_ids": [M2, THREAD_B], "base_pointers": [],
     "decoy_seeded_ids": [M1], "decoy_base_pointers": []},
    {"id": "H3", "name": "Douglas's backend release", "home_service": "gcal", "decoy_service": "slack",
     "governs": ["R2"], "findable_query": "backend release", "seeded_ids": [EVT], "base_pointers": [],
     "decoy_seeded_ids": [], "decoy_base_pointers": [JULIA_NOTES]},
]

COHORT = {
    "definition_source": "K6", "key": "live-ops work item", "size": len(ISSUES) + len(PRS),
    "members": ISSUES + [p.split("/")[-1] for p in PRS],
    "rule": "open ZOM issues bearing on an in-scope beat's readiness or live-ops infrastructure (18 since revision 6: "
            "the SQL closes two of the former 21 as Done, ZOM-344 and ZOM-432; ZOM-471, ZOM-542 and ZOM-565, which revision 4 "
            "had closed, are open and are members, the first and last in their base states and ZOM-542 Todo since revision 11; the Giant Analytics Ticket is left out since revision 6 "
            "because its Todo state is not reliable - its referencing PR merged in July, the KB's L03 case; Boss Arena / Axe "
            "Arena / Win Streak / Zombie Lane out) plus the 23 merged match3d PRs (Jul 1 - Sep 30) that each carry a post-merge still-to-do "
            "/ deploy / scope-gap fact for a beat in their own body, commits or files (so #370, #438, #454, #471 and #473 stay "
            "although the notes once seeded on them moved away); the GitHub read surface is the 39 in-scope PRs (23 "
            "decision-bearing + 16 required identification/certify reads); EXPAND_cohort_feasibility.md, less ZOM-442, "
            "#297 and #308, which existed only for Zombie Lane (off the calendar since revision 2). 41 members",
    "evidence_surfaces": [
        {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1.0, "records": len(ISSUES), "seeded": True,
         "seeded_ids": [CMT[k] for k in ISSUES] + [CMT_ZOM526_2, CMT_ZOM526_3, CMT_ZOM521_2, CMT_ZOM465_2, CMT_ZOM465_3, CMT_ZOM534_2, CMT_ZOM566_2, CMT_ZOM565_2],
         "why_no_bulk": "linear_list_issues returns state and description, never comments (Ask_Carriers §3, §6b); base "
                        "Linear holds 0 comments, so only the per-issue call shows an owner's or QA's latest note",
         "short_circuit": "no other surface carries an issue's latest prod note: the state is stale for ZOM-429 (Backlog "
                          "while QA re-tested) and ZOM-556 (Todo, note says "
                          "claiming works), and the later notes on ZOM-465, Marcus's and Brian's, are the only place the missing Collect & Win icon "
                          "animation is said outright; a run that skips the comments cannot tell hold from known issue",
         "requirement": "R3", "decides": "Status column"},
        {"service": "github", "tool": "github_get_pull_request_reviews", "per_record_calls": 1.0, "records": len(READ_PRS),
         "seeded": True, "seeded_ids": [REV468],
         "why_no_bulk": "a PR's review STATE lives only in the per-PR review list; inline and conversation comments carry no "
                        "state field (H3 census), and search/list returns no review state",
         "short_circuit": "the hold rule certifies no in-scope cohort PR carries an unresolved change-request review blocker; "
                          "that absence cannot be proven without reading each of the 22 reviews (all clear in base, so the reads confirm no "
                          "beat is held for a blocker), and the review submitted_at dates each human pass against its PR's merge",
         "requirement": "R3", "decides": "Status column"},
        {"service": "github", "tool": "github_get_pull_request_comments", "per_record_calls": 1.0, "records": len(READ_PRS),
         "seeded": True, "seeded_ids": [RC470, RC468, RC472],
         "why_no_bulk": "inline review comments come back only from this per-PR call; search 'comments' counts "
                        "conversation comments only (S7 §3.3); 21 of 22 PRs carry only CodeRabbit inline notes in base",
         "short_circuit": "reviews show an empty-bodied APPROVED on #470 and #472; the server-window note on #470, the "
                          "vial-model note on #468 and the premium-strip note on #472 are inline comments, so neither the "
                          "review list nor the conversation shows them",
         "requirement": "R5", "decides": "Still to do column"},
        # Surface 4 (github_get_issue_comments on the 39 PRs) left in revision 8: its only seeded row moved to surface 3, and
        # the 42 base conversation comments on these PRs are all bots, so it carries no fact a rule uses (necessity rule,
        # Hardness_Mastery §2.5). Restore it only if a human conversation note is seeded again.
    ],
}


def vr(svc, rid, at, container, seeded):
    return {"service": svc, "id": rid, "seeded": seeded, "at": at, "container": container}


TRAPS = [
    {"id": "T1", "family": "done_gap", "mechanism": "A24", "services": ["github", "slack", "gcal"],
     "seeded_ids": [RC470, EVT], "base_pointers": ["harmonygames-Games/match3d#468", "harmonygames-Games/match3d#470",
                                                   JULIA_NOTES], "requirement": "R2",
     "expected_wrong_reading": "Collect & Win's client PRs #468/#470/#472 merged before the Sep 30 cut and Julia's own Sep 22 "
                               "notes say the feature is completed, so it starts with the first beta window on Mon Oct 6",
     "resolver": "Arthur's inline review note on #470 (left with his approval, nine seconds before the merge) says the group windows exist "
                 "only on the dev stack and reach prod with Douglas's next backend release; that release is Wed Oct 8 18:00 "
                 "Europe/Istanbul = 2025-10-08T15:00:00Z (Julia's calendar is fixed UTC+3), after the Wed-Thu window opens "
                 "00:00 UTC, so the first window that opens after it is Fri Oct 10 00:00 UTC (Thu Oct 9 5:00 PM PDT)",
     "discovery_order": "the merged PRs and Julia's notes are met first (PR search, #company-internal); the hard part is "
                        "the composition once retrieved: the inline #470 note, the calendar event's Istanbul start converted to UTC, "
                        "and the window cadence composed to land Fri Oct 10 00:00 UTC (every record is retrievable)",
      "version_records": [vr("slack", JULIA_NOTES, "2025-09-22T16:25:02Z", f"slack:{JULIA_NOTES}", False),
                          vr("gcal", EVT, "2025-09-26T17:20:09Z", f"gcal:{EVT_UID}", True),
                          vr("github", "harmonygames-Games/match3d#468", "2025-09-26T20:16:25Z", "github:harmonygames-Games/match3d#468", False),
                          vr("github", RC470, "2025-09-30T15:51:06Z", "github:harmonygames-Games/match3d#470#rev_9", True)]},
    {"id": "T2", "family": "superseding", "mechanism": "A11", "services": ["slack"], "seeded_ids": [APPROVAL_ID, WITHDRAWAL_ID],
     "base_pointers": [HALLOWEEN_ROOT], "requirement": "R4",
     "expected_wrong_reading": "Robert, the Product owner, approved Martin's Halloween one-off in Plague Race's last-October "
                               "slot, so week 4 runs the one-off and Plague Race stops that week",
     "resolver": "Robert's later message in his DM with Julia takes the approval back: it names the themed prop set he "
                 "okayed in Martin's thread (the words of his approval), he pulls his ok, the one-off "
                 "comes off the beta calendar (no art time on a theme that may not ship), and his later word is the one "
                 "that counts, as the brief's one-off rule says; the race keeps that week",
     "discovery_order": "the approval is a reply in Martin's #zombie-art thread and is met with it; the withdrawal is a "
                        "top-level message in another container, Robert's DM with Julia, twelve days later. It has been top-level "
                        "since revision 4 (it was a thread reply under an unrelated DM parent), and since revision 9 it says "
                        "'the themed prop set I okayed in Martin's thread', not 'Halloween one-off': a 'Halloween' or 'one-off' "
                        "search returns the approval and not the withdrawal. A run reaches it through Robert's DM history, a "
                        "search on his messages or a 'beta calendar' search, and ties it to the approval by the phrase "
                        "'themed prop set'",
     "version_records": [vr("slack", APPROVAL_ID, "2025-09-18T16:40:23Z", f"slack:{HALLOWEEN_ROOT}", True),
                         vr("slack", WITHDRAWAL_ID, "2025-09-30T22:10:41Z", f"slack:{WITHDRAWAL}", True)]},
    {"id": "T3", "family": "exact_predicate", "mechanism": "A17", "services": ["gdocs", "gsheets", "slack"],
     "seeded_ids": [BRIEF], "base_pointers": [PUSH, PIPELINE], "requirement": "R1",    # the Trello note left in revision 5
     "expected_wrong_reading": "the beats are the events everyone lists (Leonard's beta pipeline, the live-ops icons): Plague "
                               "Race, Collect & Win, Season Pass, Endless and leagues, with the quests rollover and the "
                               "daily gift left out",
     "resolver": "the brief's scope (every window, reset or start push) brings in the quests rollover and the daily gift "
                 "(Login Calendar on the push sheet, same beat), each with its push row: seven beats in all"},
    {"id": "T4", "family": "authority", "mechanism": "A15", "services": ["gsheets", "gdocs"], "seeded_ids": [BRIEF],
     "base_pointers": [PUSH], "requirement": "R6",
     "expected_wrong_reading": "pushes marked Ready in the push sheet go out as written",
     "resolver": "the 1-day lapse and D0-1 FTUE rows still call the game 'Puzzles vs Zombies'; under the brief's copy rule "
                 "they are held for the copy owner"},
    {"id": "T5", "family": "authority", "mechanism": "A15", "services": ["gsheets", "gdocs"], "seeded_ids": [BRIEF],
     "base_pointers": [PUSH], "requirement": "R6",
     "expected_wrong_reading": "the Plague Race start push is Ready, so it goes out with each race",
     "resolver": "the brief sends a push only when its row is Ready and LIVE; the sheet's second status column 'Status (NA, "
                 "WIP, LIVE)' reads WIP, not LIVE, on the Plague Race and Weekly Leaderboard reset rows, so both pushes "
                 "are held",
     "discovery_order": "the first Status column (Ready / Not Ready) is the one every reader uses; the 'Status (NA, WIP, "
                        "LIVE)' column sits seven columns to the right"},
    {"id": "T6", "family": "reuse_exclusion", "services": ["linear", "slack"], "seeded_ids": [CMT["ZOM-78"], ASK_ID],
     "base_pointers": ["ZOM-78"], "requirement": "R7",
     "expected_wrong_reading": "file a new ticket for the beta calendar",
     "resolver": "ZOM-78 'Event Calendar For Zombie Match 3D' already exists (Backlog) and Frederick's comment asks for the "
                 "link there"},
    {"id": "T7", "family": "superseding", "mechanism": "A1", "services": ["linear", "slack"],
     "seeded_ids": [CMT["ZOM-429"], RETEST_ID], "base_pointers": ["ZOM-429", REPORT, OLIVER_THREAD], "requirement": "R3",
     "expected_wrong_reading": "ZOM-429's owner note says a restart gets players into the new week and the Sep 22 thread "
                               "ends 'working fine right now', so leagues run (a known issue at worst)",
     "resolver": "Vincent's Sep 30 prod re-test on the 0.3.49 submission build, a root post in #zombie-match3d, says the new week "
                 "does not start even after killing the app; the later dated prod check by the same reporter supersedes the "
                 "Sep 22 recovery, so under the hold rule leagues are held",
     "discovery_order": "every record is retrievable; the difficulty is reconciliation, not concealment: the Linear "
                        "note and the Sep 22 #zombie-bugs recovery are met first, and the Sep 30 #zombie-match3d prod re-test (another "
                        "channel, later date) must be ordered against them under the hold rule",
     # revision 5: the owner note is dated Sep 16, before the Sep 19 regression Vincent reported on Sep 22
     "version_records": [vr("linear", CMT["ZOM-429"], "2025-09-16T18:12:04Z", "linear:ZOM-429", True),
                         vr("slack", OLIVER_END, "2025-09-22T14:19:49Z", f"slack:{OLIVER_THREAD}", False),
                         vr("slack", RETEST_ID, "2025-09-30T20:50:12Z", f"slack:{RETEST}", True)]},
    {"id": "T8", "family": "superseding", "mechanism": "A14", "services": ["gmail"], "seeded_ids": [M1, M2],
     "requirement": "R8",
     "expected_wrong_reading": "Brian's Season Pass handoff commits the November config for Wed Oct 29, well before the "
                               "lock",
     "resolver": "Brian's later mail moves it to Fri Oct 31 10:00 Istanbul time; since revision 4 it is a mail of its "
                 "own (subject 'ZM3D Season Pass November config handoff: new date', no reply header, its own thread)",
     "discovery_order": "the Sep 22 handoff mail is met first; the correction is a separate mail four days later in its "
                        "own thread, which reading the handoff thread does not return and a 'last few days' mail sweep "
                        "does not reach",
     "version_records": [vr("gmail", M1, "2025-09-22T09:12:41Z", f"gmail:{THREAD_A}", True),
                         vr("gmail", M2, "2025-09-26T07:40:26Z", f"gmail:{THREAD_B}", True)]},
    {"id": "T9", "family": "unit_or_timezone", "mechanism": "A19", "services": ["gdocs", "gmail", "confluence"],
     "seeded_ids": [BRIEF, M2], "base_pointers": ["page_season_pass_spec"],
     "requirement": "R8",
     "expected_wrong_reading": "Fri Oct 31 10:00 is before the Nov 1 season opening, so the config is on time",
     "resolver": "the base page_season_pass_spec locks config 24 h before each season opens, so with Nov 1 00:00 UTC the "
                 "lock is Fri Oct 31 00:00 UTC (Thu Oct 30 5:00 PM PDT); the brief only points to it ('every config lands "
                 "before its lock'); 10:00 Istanbul (UTC+3) is 07:00 UTC, seven hours late, so the deadline moves before the lock"},
    {"id": "T10", "family": "completion_elsewhere", "mechanism": "A25", "services": ["linear"],
     "seeded_ids": [CMT["ZOM-432"], CMT_ZOM432_2], "base_pointers": ["ZOM-432", "harmonygames-Games/match3d#471", SUB135, SUB50], "requirement": "R5",
     "expected_wrong_reading": "Calvin's Sep 24 note on ZOM-432 'Daily gift artwork needs to have the frame' says the frame "
                               "is the last piece still needed, so the daily login beat still needs the frame (Calvin)",
     "resolver": "ZOM-432 is Done: Samuel closed it on Sep 30 21:07:26Z with a note on the ticket itself that the frame "
                 "went out with PR #471 and is in both submission builds from that day, iOS 50 and Android 135. The base "
                 "PR #471 (merged Sep 30) and the #builds Android Submission #135 change list ('Fixing UI Elements on "
                 "Daily Gift') agree with it but are not needed. Nothing is left for the daily login beat",
     "discovery_order": "a trap in name only since revision 5, and said plainly: the completion is recorded on the frame "
                        "ticket itself, so one read of ZOM-432 (state Done, two notes in date order) settles it, and a run "
                        "that lists open issues never meets the ticket and has the empty still-to-do for free. The wrong "
                        "reading is left to a run that reads Calvin's note and ignores both the ticket's state and its "
                        "last note. Nothing is recorded 'elsewhere' any more: the family and mechanism id are kept only "
                        "so the rule and slot ids stay stable, chain CH5 is retired, and the node counts for nothing in "
                        "the difficulty picture"},
    {"id": "T11", "family": "tool_surface", "mechanism": "A3", "services": ["github", "gdocs"],
     "seeded_ids": [RC468, RC472], "base_pointers": ["harmonygames-Games/match3d#468", "harmonygames-Games/match3d#472"],
     "requirement": "R5",
     "expected_wrong_reading": "merged live-ops PRs with an APPROVED review or only CodeRabbit notes leave nothing to do",
     "resolver": "two human notes among the bot traffic add still-to-do items: Arthur's inline review note on #468, left "
                 "before its merge (the vials still need their final models before the event runs, Claire; no blocker for that PR), and his inline note under his empty-bodied approval of #472, "
                 "six seconds before its merge (the Season Pass premium strip art still shows the October range and needs the "
                 "November range before that season opens, Oliver). Weaker since revision 8: both notes are inline, so one per-PR "
                 "call type returns them, where through revision 7 the strip needed a second one. Through revision 3 these "
                 "sat on #370 and #438; the Collect & Win icon animation left this trap for Marcus's note on ZOM-465 (T14)"},
    # Revision 5: T12 keeps its id but is an UNGRADED distractor. Through revision 4 it was a cross-reference trap
    # (A13, rule R_QUEST_SET, slot S06): the quest note decided a Quests still-to-do. The note now says the beat is not
    # waiting, the still-to-do is empty and no slot reads the cell.
    {"id": "T12", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["trello", "gsheets"],
     "seeded_ids": [TRELLO_ACT], "base_pointers": [TRELLO_QUESTS, PUSH], "requirement": "R5",
     "expected_wrong_reading": "the open quests card on the roadmap ('Add more quests and balance quest rewards') and the "
                               "push row's 'Revisit once new quests roll out' mean the quests beat is waiting for a new "
                               "quest set, so Quests gets a still-to-do (or starts in week 2)",
     "resolver": "Leonard's note on that card says more quests and the reward balance go in with the Mon Oct 13 rollover if "
                 "they are ready and that the weekly rollover does not wait on them, the current quests keep running either way: nothing has to "
                 "land before the beat runs, so under the brief's still-to-do rule nothing is put down for Quests. "
                 "Ungraded: no slot reads the Quests still-to-do cell"},
    {"id": "T13", "family": "superseding", "mechanism": "A1", "services": ["slack", "gdocs"], "seeded_ids": [BRIEF],
     "base_pointers": [PIPELINE], "requirement": "R1",
     "expected_wrong_reading": "Leonard's beta pipeline lists Infinite HP Boss Mode, so Boss Arena is on the beta calendar",
     "resolver": "Frederick's brief keeps Boss Arena off this calendar until the pivot call",
     "version_records": [vr("slack", PIPELINE, "2025-09-12T19:11:30Z", f"slack:{PIPELINE}", False),
                         vr("gdocs", BRIEF, "2025-09-24T17:40:52Z", f"file:{BRIEF}", True)]},
    {"id": "D1", "family": "distractor", "distractor_type": "stale_summary", "services": ["slack"],
     "base_pointers": [JULIA_NOTES], "requirement": "R2",
     "expected_wrong_reading": "'feature completed Win and Collect' means Collect & Win is ready for players",
     "resolver": "a dev-side status; the server windows are not on prod (T1)"},
    {"id": "D2", "family": "distractor", "distractor_type": "partial_listing", "services": ["slack"],
     "base_pointers": [PIPELINE], "requirement": "R1",
     "expected_wrong_reading": "the beta pipeline's named features are the whole calendar",
     "resolver": "the brief's scope adds the rollovers (T3)"},
    {"id": "D3", "family": "distractor", "distractor_type": "keyword_collision", "services": ["slack"],
     "base_pointers": [HALLOWEEN_ROOT], "requirement": "R1",
     "expected_wrong_reading": "Martin's 'Halloween theme for an app icon' is a live-ops beat",
     "resolver": "an app icon is not a window, reset or push; only the one-off event matters, and it is dropped (T2)"},
    {"id": "D4", "family": "distractor", "distractor_type": "other_title", "services": ["gsheets"], "base_pointers": [PUSH],
     "requirement": "R6",
     "expected_wrong_reading": "the PN BETA Translated tab's rows (Domino Adventures, River Rush, Tiledozer) are ZM3D beta "
                               "pushes",
     "resolver": "the brief says beta pushes are English-only from PNs Beta; the translated tab is the old Domino set"},
    {"id": "D5", "family": "distractor", "distractor_type": "lookalike_entity", "services": ["gsheets", "trello"],
     "base_pointers": [PUSH, "6851a7abf7876721472dba99"], "requirement": "R6",
     "expected_wrong_reading": "'Win & Collect' (the Domino Delights name on the push row and the roadmap card) is fine copy "
                               "for ZM3D",
     "resolver": "the ZM3D event is Collect & Win; under the copy rule the row would be held even once Ready"},
    {"id": "D6", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["slack"],
     "base_pointers": [BOSS_DEV, AXE], "requirement": "R1",
     "expected_wrong_reading": "Boss Arena's endpoints are ready and Axe Arena is on the roadmap, so both get beta slots",
     "resolver": "Boss Arena is off until the pivot call (brief) and Axe Arena is postponed for the beta (Brian, Sep 22)"},
    {"id": "D7", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["slack"],
     "base_pointers": [FAULT_SP], "requirement": "R3",
     "expected_wrong_reading": "the Sep 30 Season Pass shader fault thread holds Season Pass or puts a shader fix on its still-to-do",
     "resolver": "a shader defect is cosmetic; players still enter, score and claim, so Season Pass runs; since revision 10 "
                 "Vincent, who raised it, says in the thread that Oliver pushed the fix, that it only changes how the box looks "
                 "and that nothing has to land for the beta, so it is no still-to-do either"},
    {"id": "D8", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["slack"],
     "base_pointers": [FAULT_ENDLESS], "requirement": "R3",
     "expected_wrong_reading": "the unexplained Endless heating fault thread holds Endless",
     "resolver": "a performance/heating issue does not stop players entering, scoring or claiming; Endless runs"},
    {"id": "D9", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["slack"],
     "base_pointers": [FAULT_LANE], "requirement": "R1",
     "expected_wrong_reading": "the #zombie-bugs Zombie Lane thread (a fix sent and tested on Android, an iOS build asked "
                               "for) shows Zombie Lane is live work for the beta, so it gets a calendar row",
     "resolver": "Frederick's follow-up under his ask keeps Zombie Lane off the calendar (a permanent track with no window "
                 "or reset to plan); the thread decides no row"},
    {"id": "T14", "family": "exact_predicate", "mechanism": "A17", "services": ["linear", "github"],
     "seeded_ids": [CMT["ZOM-465"], CMT_ZOM465_2, CMT_ZOM465_3], "base_pointers": ["harmonygames-Games/match3d#454",
                    "harmonygames-Games/match3d#456", "harmonygames-Games/match3d#475", "ZOM-465"], "requirement": "R5",
     "expected_wrong_reading": "ZOM-465's master ticket struck 'Idle Icon Animation for all event icons' as done and "
                               "Marcus's Sep 26 note says every event icon animates, so every event icon is animated",
     "resolver": "Marcus's later note on the same ticket (Sep 30) says Collect & Win came in after his first note and its "
                 "event icon animation is still to do on his side, Brian, who wrote the master VFX list (ZOM-521), says there that it "
                 "has to land before the event runs (since revision 11), and the three animation PRs (#454/#456/#475) agree: they "
                 "enumerate Quest/Season Pass/Zombie Lane/Plague Race/Endless/Infinite Boss and a card pack, and "
                 "Collect & Win is in none",
     "discovery_order": "weaker since revision 4: both notes sit on ZOM-465 and one per-issue comment call returns them "
                        "in order, so the wrong reading is left to a run that stops at the struck line in the description "
                        "or at the first note"},
    {"id": "D10", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["linear", "github"],
     "base_pointers": ["ZOM-543", "harmonygames-Games/match3d#459", "harmonygames-Games/match3d#472"], "requirement": "R3",
     "expected_wrong_reading": "the queue manager (ZOM-543 In Progress; #459 orders only level_end/daily_gift/season_pass/"
                               "tutorial, #472 adds Collect & Win) leaves the Plague Race / Endless / Quests "
                               "panels un-ordered, so those beats are held or carry a wiring still-to-do",
     "resolver": "the queue manager orders panel animations additively ('we'll add its order'); an un-queued panel is "
                 "engineering wiring, not player-facing work flagged as still needed, and players still enter, score and claim - "
                 "the beats run"},
    {"id": "D11", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["github", "slack"],
     "base_pointers": ["harmonygames-Games/match3d#473", "slack:C08R27X0EAH/1758905363"], "requirement": "R3",
     "expected_wrong_reading": "#473 migrated Season Pass to Addressables (Arthur asked for every live-ops feature), so "
                               "the un-migrated beats are held or carry an addressables still-to-do",
     "resolver": "Addressables is a load-time optimization, not an enter/score/claim blocker and not player-facing art "
                 "flagged as still needed; no ZOM issue exists for it; no beat is held and it is not a calendar still-to-do"},
    # Revision 2: the amendment in the ask's own thread. Declared like T8 (superseding, A14: a later record the run does
    # not open): the brief as written is the superseded version, Frederick's reply the governing one.
    {"id": "T15", "family": "superseding", "mechanism": "A14", "services": ["slack", "gdocs", "gsheets", "confluence"],
     "seeded_ids": [FOLLOWUP_ID], "base_pointers": [PUSH, "page_liveops_calendar"], "requirement": "R6",
     "expected_wrong_reading": "the brief's push rule is applied as written to every row of the tab and Zombie Lane is "
                               "listed with the other live-ops",
     "resolver": "Frederick's thread reply under his own ask: plan the PNs Beta tab as it stands, one line per row, local "
                 "notifications included; leave off the four rows for things that are not in the beta (Hourly Coins, "
                 "Nathan's Treasure Hunt, Streak Fever, Axe Arena); copy that does not name the game at all is fine to go "
                 "out (the naming rule is only about wrong names); keep Zombie Lane off the calendar, a permanent track "
                 "with no window or reset to plan",
     "discovery_order": "the ask (the DM's parent message) and the brief it names are read first and read as complete; the "
                        "amendment is a reply in the ask's own thread, which DM history (parents only) does not return - "
                        "only the parent's reply count points at it",
     "version_records": [vr("gdocs", BRIEF, "2025-09-24T17:40:52Z", f"file:{BRIEF}", True),
                         vr("slack", FOLLOWUP_ID, "2025-09-30T20:24:38Z", f"slack:{ASK}", True)]},
]

CHAINS = [
    {"id": "CH1", "root_cause": "A24", "ends_in": "R2", "hops": [
        {"service": "slack", "record": ASK, "finding": "Frederick asks for the beta-weeks calendar by his brief"},
        {"service": "gdocs", "record": BRIEF, "finding": "deploy rule: windows go live only with a prod backend release"},
        {"service": "github", "record": "harmonygames-Games/match3d#468", "finding": "client merged Sep 29"},
        {"service": "github", "record": RC470, "finding": "server windows only on dev; prod with the next backend release"},
        {"service": "gcal", "record": EVT, "finding": "the next backend release is Wed Oct 8"}]},
    {"id": "CH2", "root_cause": "A11", "ends_in": "R4", "hops": [
        {"service": "gdocs", "record": BRIEF, "finding": "a one-off takes a recurring slot only with Robert's latest call"},
        {"service": "slack", "record": APPROVAL, "finding": "Robert: Halloween one-off in Plague Race's last-October slot"},
        {"service": "slack", "record": WITHDRAWAL, "finding": "Robert drops the October one-off; keep the race"}]},
    {"id": "CH3", "root_cause": "A13", "ends_in": "R8", "hops": [
        {"service": "confluence", "record": "page_season_pass_spec", "finding": "config locks 24 h before each season opens at 00:00 UTC"},
        {"service": "gdocs", "record": BRIEF, "finding": "every config a beat needs lands before its lock (points to the spec; states no 24 h offset itself)"},
        {"service": "gmail", "record": M1, "finding": "Brian: November config Wed Oct 29"},
        {"service": "gmail", "record": M2, "finding": "Brian: Fri Oct 31 10:00 Istanbul time"}]},
    {"id": "CH4", "root_cause": "A1", "ends_in": "R3", "hops": [
        {"service": "linear", "record": CMT["ZOM-429"], "finding": "owner: a restart gets players in; not urgent"},
        {"service": "slack", "record": OLIVER_END, "finding": "Sep 22: working fine after the revert"},
        {"service": "slack", "record": RETEST, "finding": "Sep 30 submission builds: no new week even after a restart"}]},
    # CH5 (ZOM-432 -> #builds Android Submission #135 -> Samuel's note on PR #471) was retired in revision 5: its last
    # hop no longer exists and the fact is settled by one read of the ticket (T10). The id is not reused.
    {"id": "CH6", "root_cause": "A3", "ends_in": "R5", "hops": [
        {"service": "gdocs", "record": BRIEF, "finding": "still to do = flagged player-facing art and config, with owner"},
        {"service": "github", "record": RC468, "finding": "review note before the merge: the final vial models (Claire)"},
        {"service": "github", "record": RC472, "finding": "inline note under his approval, before the merge: premium strip to the November range before that season opens (Oliver)"}]},
]

BUDGET = [
    ("discovery", "slack", 1, "read Frederick's ask in his DM with Julia (anchor A1: scope of the work, destinations)"),
    ("discovery", "slack", 1, "open the thread under Frederick's ask: his follow-up settles the push rows, the copy that "
                              "names no game and Zombie Lane (R1, R6)"),
    ("discovery", "gdrive", 1, "find the brief the ask names and Julia's calendar sheet (no links are posted)"),
    ("discovery", "gdocs", 1, "read Frederick's beta brief: every rule the calendar applies (R1-R6, R8)"),
    ("discovery", "gslides", 2, "find and read the UA plan the brief names for the buy weeks (R9)"),
    ("discovery", "gmail", 2, "search Brian's Season Pass handoff and read the thread (R8)"),
    ("discovery", "gcal", 2, "list Julia's events in the span and read the backend release event (R2)"),
    ("discovery", "gsheets", 3, "push sheet metadata and the PNs Beta tab (R6); Julia's calendar sheet header (R7)"),
    ("discovery", "linear", 1, "find the calendar ticket the ask names (ZOM-78, R7)"),
    ("discovery", "confluence", 1, "find the Season Pass spec page and read its config-lock rule ('locked 24h before each "
                                   "season opens'): the offset the brief's 'before its lock' points to and states nowhere "
                                   "itself (R8). On the required path all along; first counted in revision 5"),
    ("enumeration", "linear", 3, "list open ZOM issues (96 open since revision 9, whose SQL closes ZOM-344, ZOM-432 and ZOM-563; 99 in base: 2 pages) and search the beat terms the titles use"),
    ("enumeration", "github", 4, "list the live-ops PRs merged Jul 1 - Sep 30 (search + pages); 210 merged, 39 in-scope"),
    ("enumeration", "github", 5, "list the match3d-backend cross-repo PRs and read #16/#19/#26/#34: leagues / endless server state (#10 is Zombie Lane only, off the calendar: not read)"),
    ("enumeration", "trello", 0, "revision 5: not needed any more (it counted 1). No graded value rests on a roadmap card; the quest note on card #61 decides nothing (T12)"),
    ("enumeration", "slack", 9, "#zombie-bugs Sep 15-30 (3 pages), #zombie-design (2), #zombie-match3d (2), "
                                "#company-internal (1), #builds Sep 30 submission posts (1): each beat's faults and status"),
    ("per-record", "linear", len(ISSUES), "linear_list_comments on each of the 18 open live-ops issues (cohort surface 1; base Linear holds 0 comments; ZOM-484 dropped as out-of-scope Axe Arena, ZOM-442 as Zombie Lane only; ZOM-344 and ZOM-432, which the SQL closes Done, are not open and are not read; the Giant Analytics Ticket left the cohort in revision 6 and is not read)"),
    ("per-record", "github", len(READ_PRS), "github_get_pull_request_reviews on each of the 39 in-scope PRs (surface 2; certify no open change-request blocker per PR)"),
    ("per-record", "github", len(READ_PRS), "github_get_pull_request_comments on each of the 39 PRs (surface 3, inline review notes)"),
    ("per-record", "github", 0, "revision 8: github_get_issue_comments on the 39 PRs is not needed any more (it counted 39): no seeded note is left in a PR conversation and the 42 base comments there are all bots"),
    ("per-record", "github", 7, "commit-list reads on the body-empty PRs (#296/#317/#400/#408/#419/#471/#475): the decision lives in commit titles"),
    ("authorities", "slack", 2, "#zombie-art Halloween thread replies (1); Robert's DM history, where the retraction is a top-level message since revision 4 (1; the thread-open call is gone) - "
                                "the Sep 22 report and Oliver's recovery are distractors, not on the sufficient path (ZOM-429 note + the Sep 30 root settle the hold)"),
    ("authorities", "trello", 0, "revision 5: not needed any more (it counted 1): the comment on the quests card decides no graded value"),
    ("authorities", "github", 0, "no separate read of PR #471 (it counted 2 through revision 3): ZOM-432 is Done, so no open ticket raises the frame, and since revision 5 nothing is seeded on #471"),
    ("reconciliation", "slack", 6, "open the 6 open live-ops fault threads whose deciding last reply carries no beat "
                                    "keyword (H2: quests-anim, endless heating, season-pass shader, endless #1643, two submission "
                                   "bundles) to certify each beat under R3; the zombie-lane thread is not needed (off the calendar); the #zombie-match3d leagues re-test root is read in enumeration, not here"),
    ("writes", "gsheets", 3, "write the Calendar and Pushes tabs, then read the sheet back"),
    ("writes", "slack", 1, "reply to Frederick in his DM with the recommendation (R7)"),
    ("writes", "linear", 2, "link the calendar on ZOM-78; note the leagues hold on ZOM-429 (R7)"),
    ("writes", "gmail", 1, "reply to Brian, on the mail where he committed to the date, that the November config must land before the lock (R8)"),
    ("enumeration", "github", 0, "conditional: files of a shared icons / queue-manager PR only when its review flags a beat"),
]
CALL_BUDGET = [{"phase": p, "service": s, "calls": c, "reason": r} for p, s, c, r in BUDGET if c]
CALL_BUDGET.append({"phase": "enumeration", "service": "github", "calls": 10, "reason": "files of the 10 shared-title PRs "
                    "(icons, queue manager) to tie a flag to a beat", "conditional_on": "a review or comment on that PR "
                    "flags a beat (none does in base; the design seeds none on a shared-title PR)"})

WRITES = [
    {"service": "gsheets", "tool": "gsheets_values_update", "count": 2,
     "depends_on": ["R_DONE_DEPLOY", "R_WITHDRAWN", "R_SCOPE_BEATS", "R_COPY_CURRENT", "R_WIRED", "R_TECH_HOLD", "R_HOLD_SCOPE",
                    "R_HANDOFF_SLIP", "R_LOCK_BOUNDARY", "R_DONE_ELSEWHERE", "R_REVIEW_FLAGS", "R_ASK_FOLLOWUP",
                    "K1", "K15", "K17"],
     "requirements": ["R1", "R2", "R3", "R4", "R5", "R6", "R8", "R9"]},
    {"service": "slack", "tool": "slack_send_message", "count": 1,
     "depends_on": ["R_DONE_DEPLOY", "R_WITHDRAWN", "R_TECH_HOLD", "R_LOCK_BOUNDARY", "A1"], "requirements": ["R7"]},
    {"service": "linear", "tool": "linear_create_comment", "count": 2, "depends_on": ["R_TECH_HOLD", "K12", "K3"],
     "requirements": ["R7"]},
    {"service": "gmail", "tool": "gmail_reply_to_message", "count": 1,
     "depends_on": ["R_HANDOFF_SLIP", "R_LOCK_BOUNDARY", "K9"], "requirements": ["R8"]},
]


def rule(rid, mech, nodes, req, natural, prior, reason, controls, over, src, sig, decides):
    return {"id": rid, "mechanism": mech, "nodes": nodes, "requirement": req, "natural_reading": natural,
            "prior_family": prior, "prior_family_reason": reason, "controls": controls, "over_application": over,
            "source": src, "signature": sig, "decides": decides}


A1FAM = "wrong summary + thread past its conclusion (A1)"
PORTFOLIO = [
    rule("R_DONE_DEPLOY", "A24", ["T1", "CH1"], "R2", "merged client PRs + 'feature completed' = starts with the first beta "
         "window", "A24", "same mechanism id; Opus 5.5 records hev_629850249f55e2d3 / hev_da8f703d3115e8e0 (vincent_zm3d_gate "
         "rev1, LEAKED: the deciding record was a swept DM); here it is an inline review note, the carrier Vincent's report "
         "§8 measured at 5/6-6/6 misses", ["Plague Race", "Endless"], "over:every-beat-waits-for-a-release", "inline-470",
         "merged-not-deployed", ["Collect & Win first window", "Collect & Win still to do"]),
    rule("R_WITHDRAWN", "A11", ["T2", "CH2"], "R4", "the Product owner's approval in the art thread stands", "A11",
         "same mechanism id (approval withdrawn later, in another container); no Opus 5.5 ledger record (Beta(1,1), "
         "UNCALIBRATED)", ["Endless", "Season Pass"], "over:every-one-off-dropped", "robert-dm-thread",
         "approval-taken-back", ["Plague Race weeks running", "Halloween one-off in the reply"]),
    rule("R_SCOPE_BEATS", "A17", ["T3"], "R1", "the beats are the events everyone lists", "A17",
         "same mechanism id (cohort boundary; hev_971c5e5fdb2d2c1a, hev_95fae459cc9d282a, both LEAKED when the rule was "
         "read first)", ["Plague Race", "Endless"], "over:every-push-row-is-a-beat", "brief-scope", "resets-are-beats",
         ["Quests row", "Login calendar row"]),
    rule("R_COPY_CURRENT", "A15", ["T4"], "R6", "Ready in the push sheet = sendable", "A15",
         "same mechanism id (house rule over the natural reading; hev_d62067eb715ef8fe LEAKED, hev_8f613c1258c209c0 FALSE)",
         ["7-day lapse", "Lives recharged"], "over:every-zombie-copy-held", "brief-copy", "old-title-held",
         ["1-day lapse push", "D0-1 FTUE push"]),
    rule("R_WIRED", "A15", ["T5"], "R6", "Ready = LIVE", "A15", "same mechanism id (a second house rule on the same sheet: "
         "the 'Status (NA, WIP, LIVE)' column)", ["7-day lapse", "Lives recharged"], "over:every-push-held",
         "brief-ready-and-live", "ready-but-wip", ["Plague Race start push", "Weekly Leaderboard reset push"]),
    rule("R_ASK_FOLLOWUP", "A14", ["T15"], "R6", "the brief is the whole rulebook: its naming sentence is read strictly and "
         "every row of the tab is listed", "A14",
         "same mechanism id and carrier class as the ledger's A14 record (hev_ee2fa6cd86df8050 FALSE on "
         "robert-vendor-schedule: a later record the run does not open); here the later record is an amendment in the "
         "ask's own thread. Honest caveat: the completed julia_zm_difficulty_baseline task saw 3 of 6 Opus 5.5 runs miss "
         "DM thread replies (its 01a_Hardening_Report: thread-reply nodes LANDED 3/6, between 1/6 and 5/6 in its other "
         "rounds), but tools/hardness_v2_check.py "
         "treats a reply in an anchor's thread as first_read (SAME_PLACE flag on T15), so this node can leak whenever a "
         "run opens the ask thread", ["1-day lapse", "D0-1 FTUE"], None, "ask-thread-reply",
         "amendment-in-the-ask-thread", ["Lives recharged push", "7-day lapse push"]),
    rule("R_TECH_HOLD", "A1", ["T7", "CH4"], "R3", "the owner note and the Sep 22 fix settle it: a restart gets players in",
         A1FAM, "closest library family with Opus 5.5 records: a claim met first and overturned by a later record "
                "(hev_fcae4e267ad7d452 LEAKED via a swept DM; hev_6b560d035cdf9211 FALSE); here the re-test is a reply under "
                "a standalone root", ["Quests", "Daily login"], "over:every-restart-fault-held", "retest-reply",
         "fails-after-restart", ["Weekly leagues status", "ZOM-429 hold note"]),
    rule("R_HANDOFF_SLIP", "A14", ["T8", "CH3"], "R8", "the handoff thread's date is the date", "A14",
         "same mechanism id (a later record the run does not open; hev_ee2fa6cd86df8050 FALSE on robert-vendor-schedule)",
         ["Endless", "Quests"], None, "brian-slip-mail", "date-moved-in-other-thread",
         ["Season Pass November config deadline", "reply to Brian"]),
    rule("R_LOCK_BOUNDARY", "A19", ["T9"], "R8", "a delivery on the lock day is on time", "A19",
         "same mechanism id (retrieved but never computed: the UTC lock instant against a local-time commitment); no Opus "
         "5.5 ledger record", ["Collect & Win"], None, "lock-instant", "lock-day-late",
         ["Season Pass November config deadline", "reply to Brian"]),
    rule("R_DONE_ELSEWHERE", "A25", ["T10"], "R5", "the frame ticket's own Sep 24 note is the last word: the "
         "daily-gift frame is still needed", "A25",
         "the mechanism id is kept for id stability only (A25, completion recorded away from the request; "
         "hev_9f21d34afc03eb11 LEAKED via a swept DM). Since revision 5 the completion is recorded ON the request: the "
         "frame ticket ZOM-432 is Done and its own last note (Samuel, Sep 30 21:07:26Z) says the frame went out with "
         "PR #471 and is in both submission builds, so one read of the ticket settles it and a run that lists open "
         "issues never meets it. The A25 ledger prior does not describe this node; it is no difficulty carrier and its "
         "slot S07 is a weight-1 lookup. Control ZOM-344 became ZOM-534 in revision 4 (ZOM-344 is Done)",
         ["ZOM-534", "ZOM-556"],
         "over:every-open-ticket-done", "frame-ticket-closing-note", "older-note-on-closed-ticket", ["Daily login still to do"]),
    rule("R_REVIEW_FLAGS", "A3", ["T11", "CH6"], "R5", "approved or bot-only PRs leave nothing to do", "A3",
         "same mechanism id (tool-surface blind spot: inline review notes come only from the per-PR call; on #468 and, since revision 8, #472, so one call type reaches both where two did through revision 7); no Opus 5.5 "
         "ledger record", ["harmonygames-Games/match3d#420", "harmonygames-Games/match3d#364"],
         "over:every-pr-adds-a-task", "inline-review-notes", "flag-in-inline-note",
         ["Collect & Win still to do", "Season Pass still to do"]),
    # R_QUEST_SET (A13, T12, "Quests still to do") was retired in revision 5: fourteen rules.
    rule("R_HOLD_SCOPE", "A17", ["D7", "D8"], "R3", "an open or diagnosed fault thread means the beat is held", "A17",
         "ledger-grounded A17 (Beta(1,3) mean 0.25; hev_971c5e5fdb2d2c1a / hev_95fae459cc9d282a LEAKED): the hold predicate "
         "applied too broadly to cosmetic / performance / analytics faults - the over-application twin of R_TECH_HOLD",
         ["Plague Race", "Daily Login"], "over:every-open-fault-holds-the-beat", "fault-threads", "cosmetic-fault-not-a-hold",
         ["Endless runs", "Season Pass runs"]),
    rule("R_ICON_SCOPE", "A17", ["T14"], "R5", "the master VFX ticket struck 'all event icons' as done, so every icon "
         "is animated", "A17",
         "same mechanism id (a completion claim broader than the shipped set; hev_971c5e5fdb2d2c1a / "
         "hev_95fae459cc9d282a LEAKED when the predicate was read first): the idle-icon master ticket (ZOM-465) is "
         "struck done but the three animation PRs enumerate a subset that omits Collect & Win - a scope gap found only "
         "by reading #454/#456/#475 or, since revision 4, Marcus's later note on the same ticket (one per-issue comment call "
         "returns both notes, so this node is weaker than it was)", ["Season Pass", "Plague Race"], "over:all-event-icons-done", "icon-master-vs-prs",
         "cw-icon-absent", ["Collect & Win still to do (icon)"]),
    rule("R_INFRA_SCOPE", "A17", ["D10"], "R3", "the in-progress queue manager, whose flow list does not yet order the "
         "Plague Race panel, holds Plague Race", "A17",
         "ledger-grounded A17 (Beta(1,3) mean 0.25; hev_971c5e5fdb2d2c1a / hev_95fae459cc9d282a LEAKED): the readiness "
         "rule over-applied to ONE live-ops INFRASTRUCTURE gap rather than a fault thread - the infra-gap over-hold twin "
         "of the fault-thread R_HOLD_SCOPE, over a DISJOINT beat (it flips Plague Race only, which R_HOLD_SCOPE never "
         "touches); a run reads the queue manager (ZOM-543 In Progress; #459 orders level_end/daily_gift/season_pass/"
         "tutorial, #472 adds Collect & Win) as leaving the Plague Race panel un-ordered and therefore held, when the "
         "queue orders panel animations additively and Plague Race still enters, scores and claims. The addressables "
         "gap (#473, D11) is a standalone distractor, not graded - C&W over-hold via addressables is a separate, weaker "
         "mistake and is left as retrieval context", ["Endless"],
         "over:an-unqueued-panel-holds-the-beat", "queue-manager", "unqueued-panel-not-a-hold",
         ["Plague Race runs"]),
]

manifest = {
    "assignment_context": {k: ctx[k] for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc",
                                               "difficulty_mode")},
    "persona": "julia_lawson", "horizon": "Long Horizon", "effective_profile": "extreme",
    "volume_exception": {
        "reason": "No honest design for Julia's Marketing and GTM calendar reaches the extreme 500 / 300 necessary calls. "
                  "The enriched 48-member cohort (23 open live-ops issues + 25 merged PRs; the GitHub read surface is 41 "
                  "in-scope PRs) makes a thorough unbatched run ≈ 255 evidence reads; the un-skippable minimal golden run "
                  "(per-PR reviews certify no open change-request blocker + the 23 per-issue comments the stale Linear "
                  "state forces) is ~130 calls; padding to 500 is a failing error",
        "requester_confirmation": "Requester (session 2026-11-05, enriched task): \"we need 150+ tool call along with "
                                  "difficulty\"; the 48-member cohort makes a thorough run ≈ 255 calls (150+ for real runs); "
                                  "the honest minimal-golden-run floor is ~130; seeded rows ~55 (rows handled at injection)",
        "call_budget_floor": 130, "per_record_floor": 75,
        "rows_floor": 70},   # honest seeded-INSERT floor: the integrated injection seeds ~74 rows (22 Linear + 17 GitHub + 34 Slack/Gmail/GCal/Drive); the lean live-ops universe seeds no 120-row injection without padding (requester-confirmed, 2026-11-05)
    "requirements": REQ, "services": SERVICES, "anchors": ANCHORS, "ask_fragments": FRAGS, "authorities": AUTHORITIES,
    "cohort": COHORT, "chains": CHAINS, "traps": TRAPS, "call_budget": CALL_BUDGET, "writes": WRITES,
    "mechanism_portfolio": PORTFOLIO, "gradable_surface": {"path": "01_Gradable_Surface.json"},
}


def write(path, obj):
    """Write only when the content changes: a re-run that changes nothing must not re-date a file other artifacts
    are checked against."""
    text = json.dumps(obj, indent=1, ensure_ascii=False) + "\n"
    if path.exists() and path.read_text() == text:
        return "unchanged"
    path.write_text(text)
    return "wrote"


out = WF / "01_Hardness_Manifest.draft.json"
draft_status = write(out, manifest)

# ---------------------------------------------------------------- final manifest (injection stage)
# 01_Hardness_Manifest.json = the draft + the injection-stage keys: facts, integration_exceptions,
# hazard_acknowledgements and solver {path, digest of the current solver.py}. Through revision 2 a one-off helper
# copied these keys forward from the previous final manifest; they are written out here (values unchanged) so that
# one run regenerates both files. Run it again after any solver edit: the digest is read from the file.
MIRROR = {"470": "73bc730c620936feba3dcfbba00e2745", "468": "78aa8ed77c0bd7b8a3fad227b22bc3fb",
          "472": "65564543e4bc8dd707a177aada2337a3"}       # the #zombie-prs INT-01 mirror row of each deciding PR comment
#                                                           (new ids in revision 5: each posts 2-3 s after its event; no #471 mirror)
FACTS = [
    {"key": "cw.first_window", "value": "2025-10-10", "kind": "date", "aliases": ["first window"],
     "home_ids": [RC470, MIRROR["470"]]},
    {"key": "cw.todo.vials", "value": "final models", "kind": "name", "home_ids": [RC468, MIRROR["468"]]},   # revision 13: the note's words
    {"key": "sp.todo.strip", "value": "premium strip", "kind": "name", "home_ids": [RC472, MIRROR["472"]]},
    {"key": "cw.todo.icon", "value": "outstanding", "kind": "status", "home_ids": [CMT_ZOM465_2]},   # a Linear note: no mirror
    {"key": "sp.config_lock", "value": "2025-10-31", "kind": "date", "aliases": ["config lock", "config locks"],
     "home_ids": ["rfc:" + M2_RFC, BRIEF]},
    # quests.todo left in revision 5: the Quests still-to-do is empty, so there is no such fact to keep in one place
    {"key": "login.todo", "value": "daily-gift frame", "kind": "name", "home_ids": [CMT_ZOM432_2],
     "version_records": [CMT["ZOM-432"]]},                 # a Linear note on the Done ticket: no mirror
    {"key": "leagues.status", "value": "new week", "kind": "name", "home_ids": [RETEST],
     "version_records": [CMT["ZOM-429"]]},
    {"key": "plague.weeks", "value": "themed prop set", "kind": "name", "aliases": ["themed prop"], "home_ids": [WITHDRAWAL],   # revision 9: the words the withdrawal and the approval share
     "version_records": [APPROVAL]},
]
INTEGRATION_EXCEPTIONS = [
    {"record_id": EVT_UID,
     "reason": "no_notify: the Oct 8 backend-release date is a hidden GCal-only authority (H3); seeding an INT-11 "
               "invitation mail would leak the date into a Gmail subject line."},
]
# No entry. Revision 5 stopped touching ZOM-387 in the SQL (the revision-4 `repaired` entry for L03 would have been
# false), and revision 6 took the ticket out of the cohort, so no manifest section cites it: hardness_gate's
# hazard_scope finds no L03 record to resolve, and base_check passes with and without --manifest.
HAZARD_ACKS = []   # SC-15 (repaired in revision 3) is not a coherence_hazards.json id and cannot be listed here: see the docstring
SOLVER = WF / "solver" / "solver.py"
final = dict(manifest, facts=FACTS, integration_exceptions=INTEGRATION_EXCEPTIONS, hazard_acknowledgements=HAZARD_ACKS,
             solver={"path": "Working_Files/solver/solver.py", "digest": hashlib.sha256(SOLVER.read_bytes()).hexdigest()})
final_out = WF / "01_Hardness_Manifest.json"
final_status = write(final_out, final)

unc = sum(r["calls"] for r in CALL_BUDGET if not r.get("conditional_on"))
per = sum(s["per_record_calls"] * s["records"] for s in COHORT["evidence_surfaces"])
non = [r for r in CALL_BUDGET if r["phase"] != "per-record" and not r.get("conditional_on")]
share = {}
for r in non:
    share[r["service"]] = share.get(r["service"], 0) + r["calls"]
tot_non = sum(share.values())
print(f"{draft_status} {out}: unconditional {unc}, per-record {per}, non-per-record {tot_non}, "
      f"max share {max(share.values()) / tot_non:.0%} ({max(share, key=share.get)}), services {len({r['service'] for r in CALL_BUDGET if r['calls']})}")
print(f"{final_status} {final_out}: {len(final)} keys; solver digest {final['solver']['digest']}")

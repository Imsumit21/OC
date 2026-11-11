# Prompt Check — julia-zm3d-beta-liveops-calendar
Prompt: 04_Prompt.txt · 100 words · sha256 2a23afd87c4c
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Checked 2026-11-06 against 04_Prompt_Writing_Brief.md (revised 2026-11-06 for revision 2) and the revision-2 SQL (sha256 3afbf7cbbdb7), release task-quality-v1. This check replaces the 2026-11-05 check of the previous prompt, which the platform failed (see "Previous /prompt result").
Revision 3 note (2026-11-06): the SQL is now revision 3 (sha256 837d4f5dedbd, 78 INSERT and 34 UPDATE). It differs from the SQL this check read in three Linear statements on two tickets: a new, later note on ZOM-526 with that issue's updated_at, and the ZOM-521 description with two checklist items unticked (known-issue card SC-15, repaired; dossier §11 Revision 3). The prompt is unchanged (sha256 2a23afd87c4c), and no premise, span or finding below reads either ticket.
Revision 4 note (2026-11-06): the SQL is now revision 4 (sha256 c955d6ca2bca, 75 INSERT and 31 UPDATE), the repair for an independent /prompt run on revision 3 (Cross-Service Coherence 2, Clarity 3; dossier §11 Revision 4). The prompt is unchanged (sha256 2a23afd87c4c) and so is every pinned value. Three things this check says read differently on revision 4 and are corrected where they stand: the premium-strip note is a conversation comment on #473, no longer a review on #438; Frederick's ask words the recommendation as one sent back in the DM, with the trade-offs, on what they run and what they hold in those weeks; and the brief says the config owner is told in a reply on the mail where they committed to it, which settles this check's one Minor finding (C7, the channel for telling Brian). The finding and the predicted band are left as recorded for revision 2.
Revision 5 note (2026-11-06): the SQL is now revision 5 (sha256 3c035f2af029, 70 INSERT and 26 UPDATE), the repair for an independent /prompt run on revision 4 and an audit of every injected record (dossier §11 Revision 5). The prompt is unchanged (sha256 2a23afd87c4c). Two pinned values change by design: the Quests still-to-do is empty and the Collect & Win vial item reads "the final vial models (Claire)". Read differently on revision 5 and corrected where it stands: the daily-gift frame is settled by Samuel's closing note on ZOM-432 (`cmt_zom432_2`), not by a PR comment; the quest note is Leonard's, on the open quests card, and says the current set carries the first week; the ask is dated 20:20:17Z; Trello no longer changes a graded fact. Every premise of the prompt still holds: the ask, its thread reply, the brief, the sheet and the calendar ticket are the same records with the same words (the Slack ids are new and are cited below).
Revisions 6 and 7 note (2026-11-06): the SQL is now revision 7 (sha256 091722f6a281, 72 INSERT and 26 UPDATE). The prompt is unchanged (sha256 2a23afd87c4c) and so is every pinned value (dossier §11 Revision 6 and Revision 7). Read differently and corrected where it stands: the quest note now says nothing in the beta waits on the new quests. Every premise of the prompt still holds; the ask, its thread reply, the brief, the sheet and the calendar ticket are the same records with the same words.
Revision 8 note (2026-11-06): the SQL is now revision 8 (sha256 0e8c8ad83f3b, 71 INSERT and 25 UPDATE). The prompt is unchanged (sha256 2a23afd87c4c) and so is every pinned value; one evidence id moves (dossier §11 Revision 8). Read differently and corrected where it stands: the premium-strip note is an inline comment inside Arthur's approval of #472, before that merge, and the quest note says the rollover does not wait on the new quests. The brief adds one sentence on undated holds, which the prompt's premises do not touch.
Revision 9 note (2026-11-06): the SQL is now revision 9 (sha256 892f7edda809, 76 INSERT and 28 UPDATE). The prompt is unchanged (sha256 2a23afd87c4c) and so is every pinned value (dossier §11 Revision 9). Read differently and corrected where it stands: the brief's late-start sentence now reads "A beat whose server windows are waiting on that release starts late, it is not held.", its still-to-do rule is closed, and Robert's withdrawal no longer names Halloween. The prompt's premises do not touch any of these.
Revision 10 note (2026-11-06): the SQL is now revision 10 (sha256 ffbac4586fb9, 78 INSERT and 29 UPDATE). The prompt is unchanged (sha256 2a23afd87c4c). Two pinned values change by design: the owners (Douglas) and Weeks running for Quests and Daily Login (All four weeks); dossier §11 Revision 10. The prompt's premises do not touch these or the re-worded still-to-do rule.
Revision 11 note (2026-11-06): the SQL is now revision 11 (sha256 1348d287ac4a, 80 INSERT and 30 UPDATE). The prompt is unchanged (sha256 2a23afd87c4c) and so is every pinned value; one evidence id is added, `cmt_zom465_3` (dossier §11 Revision 11). The brief's new sentences settle window edges, a held beat's windows and the moved date. The prompt's premises do not touch them.
Revision 12 note (2026-11-06): the SQL is now revision 12 (sha256 b5ccbfa577fc, 81 INSERT and 30 UPDATE). The prompt is unchanged (sha256 2a23afd87c4c). Three empty, ungraded cells are filled by design: Weekly Leagues' First window and Weeks running and Season Pass's First window (dossier §11 Revision 12). No other pinned value and no evidence id moves. The prompt's premises do not touch these or the brief's new wording.
Revision 13 note (2026-11-06): the SQL is now revision 13 (sha256 1f2175a297fd, 81 INSERT and 30 UPDATE). The prompt is unchanged (sha256 2a23afd87c4c) and so is every pinned value and evidence id (dossier §11 Revision 13). The prompt's premises do not touch the re-worded notes or brief phrases.
Revision 14 note (2026-11-06): the SQL is now revision 14 (sha256 edae63f3e838, 81 INSERT and 30 UPDATE). The prompt is unchanged (sha256 2a23afd87c4c) and so is every pinned value and evidence id (dossier §11 Revision 14). The prompt's premises do not touch the two re-worded brief sentences.

## Summary

Fail 0 · Non-fail 1 (C7, Minor) · Advisory 1 (C10) · UNVERIFIED: none · clean: C1–C6, C8, C9, C11–C24.

Predicted /prompt band: **NON-FAIL** (3–4). That is this check's own rule applied to one Minor clarity finding; every
hard gate I can test locally passes. I hold the prediction loosely. The check of the previous prompt predicted PASS and
the platform returned FAIL (2), because its deep recheck found seven forks that check had not looked for. Each of those
seven now has a dated, persona-visible settling record and the field list is out of the prompt, so a FAIL should need a
fork outside F1–F13; the three residual risks are listed under Self-review.

Status: **READY FOR /prompt** on the findings (no Fail). The local stage gate has not been re-run on this text, so the
gate block further down is the earlier revision's record (see Route).

The prompt is an ordinary hand-off in Julia Lawson's voice. It names its destinations (her live-ops calendar sheet,
the calendar ticket, a held beat's ticket, Frederick), points to Frederick's message for what he wants and to his
brief for the rules, and leaves every beat, push row, run/hold, send/hold, window and still-to-do to be discovered.
Multi-source and dynamic change are load-bearing.

## Findings

| Check | Verdict | Quoted span (04_Prompt.txt) | Note |
|---|---|---|---|
| C5 complexity and seeding | PASS | "his working rules for building it are in the brief he shared with me" | the rules, the beat set and the push rows stay in records; multi-source and dynamic change are load-bearing (brief §8); the per-row field list that failed revision 1 is gone |
| C6 fair outcomes | PASS | "What he wants in it is in his message" | the ask and its thread reply fix the fields, the push rows and the Zombie Lane exclusion; seven beats and ten push rows, each fork settled by a record (Fair readings); no answer-key clause |
| C7 clarity | Non-fail (Minor) | "If a beat ends up held, leave a note on its ticket so the owner picks it up" | one condition, in the brief's own term, so the note goes on the held beat's ticket only. Minor: telling Brian comes from the brief's lock rule, not from a sentence in the prompt, and its channel is open (brief §4b keeps a reply on his mail as canonical). Revision 4: no longer open, the brief itself now says to tell him in a reply on that mail |
| C9 pre-solved | PASS | "If a beat ends up held" | a condition; it names no beat, cause, date or count |
| C10 discovery | Advisory | "in his message" | nothing hidden is named by title or id, but the prompt points at the ask itself, so the follow-up reply is one thread-open away (`first_read`); it settles forks and should not be counted as a difficulty carrier |
| C14 tool mention | PASS | "It goes in my live-ops calendar sheet" | natural product phrasing, no function or server name |
| C15 command list | PASS | "Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for" | the order of deliverables and who to tell, not a scripted method |
| C16 ordinary request | PASS | "Can you take it on for me?" | no spec-sheet layout, enumerated deliverable specs, riddle, hint, audit-form wording or if-chain |
| C17 truthfulness | PASS | "Frederick messaged me yesterday asking for the live-ops and push calendar" | every premise verified (log below) |
| C19 persona ACL | PASS | "my live-ops calendar sheet" | all scoped reads are Julia-visible, the thread reply included (brief §5a) |
| C20 today's date | PASS | "the four buy weeks that start Monday the 6th" | Mon Oct 6 2025, a future plan date; yesterday is Tue Sep 30 2025 |

## Fair readings (accepted outcomes)

Reuses prompt-brief §4b as revised for revision 2. The pinned state is **seven beats** (Plague Race, Collect & Win,
Season Pass, Endless Monster Mode, Weekly Leagues, Quests, Daily Login) and **ten push rows** (two Send, eight Held).
For each deliverable, Reading A is the accepted one and Reading B the strongest alternative I could build; every B is
settled by a record, none by a clause in the prompt.

| Deliverable | Reading A (accepted) | Strongest Reading B | What settles it |
|---|---|---|---|
| Calendar: which beats | seven beats; no Zombie Lane row | eight, with Zombie Lane as a beat players see | Frederick's thread reply `D05SD5QLG94/1759263878.305129` keeps Zombie Lane off (a permanent track with no window or reset to plan); the brief ties the daily gift to Login Calendar as the same beat |
| Collect & Win status | Runs, a late start, first window Fri Oct 10 00:00 UTC | Held until Oct 10 | brief `f_7c3e91a4d2b85f60e1a9c4`: a beat whose server windows are waiting on the release starts late, it is not held |
| Season Pass windows | the October season is already running; the November season opens Sat Nov 1 00:00 UTC; the brief's clip sentence holds them to Mon Oct 6 00:00 UTC and Sun Nov 2 23:59 UTC | the October season does not count; first window Nov 1 | Arthur's `#470#rc_10`: the Season Pass schedule is already running on prod; the release event `evt_9a4c2e7f1b3d58e06c7a2f` covers only the windows still on the DEV stack |
| Weekly Leagues row | Held, with Mon Oct 6 00:00 UTC and all four weeks on the row | no windows or weeks until the fix lands | brief `f_7c3e91a4d2b85f60e1a9c4`: a held beat keeps its usual windows and weeks on its row, marked held |
| Daily gift still-to-do | nothing left | the frame is still to do (Android only, or awaiting store approval) | Samuel's closing note on ZOM-432 (`cmt_zom432_2`; `#471#c_18` through revision 4): in both submission builds, iOS 50 and Android 135, nothing is left |
| Push plan: which rows | ten rows of the PNs Beta tab | all 14 rows, only the nine Push Notification rows, or only the six Ready rows | the same thread reply: the tab as it stands, local notifications included, four named rows left off |
| Lives recharged, 7-day lapse | Send | wait, because the copy never names Zombie Match 3D | the same thread reply: copy that names no game may go out, the naming rule is about wrong names |
| Ticket notes | one, on `ZOM-429` | also notes for Collect & Win and Season Pass on `ZOM-566` / `ZOM-552` | the prompt's condition is a held beat, and the brief says a beat waiting on the release is not held; Weekly Leagues is the only held beat |
| November config date | moves before Oct 31 00:00 UTC, and Brian is told | Brian's Fri Oct 31 10:00 Istanbul is on time | base `page_season_pass_spec` (locked 24h before each season opens) and the brief's lock rule; the slip mail `julia.lawson@harmonygames.co/1844311412966040123` is 7h late |
| Recommendation | any coherent call with trade-offs, consistent with the sheet | a list of findings with no call | delegated; the ask `D05SD5QLG94/1759263617.418209` asks for a call, not a list |

Still accepted as representational variants: the status synonym sets `{Runs/Run/Live}` / `{Held/Hold}` and the Send set
`{Send/Sent/Go}`; PT or UTC renderings of the same instant and precise or "before the lock" wording; the Calendar tab's
Push and Hold-until columns filled per beat or left to the Pushes tab; the wording of the reply to Brian.

No longer accepted, though revision 1 accepted them either way: a Zombie Lane row or iOS still-to-do; a conditional
hold for Collect & Win; a push plan of only the six Ready rows. The four rows Frederick left off (Hourly Coins,
Nathan's Treasure Hunt, Streak Fever, Axe Arena) were already out of scope in revision 1 and now must not be listed at
all, not even as held. No single figure is left unsettled, so no both-fair-figure acceptance applies.

## Verification log

Every tight identifier and premise in the prompt, looked up again in this run against the revision-2 SQL and the base
export (C17):

| Premise in prompt | Resolves to | Verdict |
|---|---|---|
| "Frederick messaged me yesterday" | Frederick Stone `frederick.stone@harmonygames.co`; DM `D05SD5QLG94/1759263617.418209` dated 2025-09-30T20:20:17Z = Tue Sep 30 13:20 PDT; persona today is Wed Oct 1 2025 (`00_Task_Context.json:/universe/persona_today`), so the day before | YES |
| "asking for the live-ops and push calendar for the Zombie Match 3D beta" | the ask text asks for the live-ops and push calendar for the beta buy (`bca784379e7dbca9e64e79a64dfefbba`); ZM3D is the game | YES |
| "the four buy weeks that start Monday the 6th" | Mon Oct 6 – Sun Nov 2 2025 (the ask; UA deck `f_2b9d4e7a1c63f08d5e7b21` W1–W4; brief span); Oct 6 2025 is a Monday | YES |
| "his message" | the DM and its thread: root `D05SD5QLG94/1759263617.418209` (reply_count 1) and Frederick's own reply `D05SD5QLG94/1759263878.305129` at 20:24:38Z | YES |
| "the brief he shared with me" | `f_7c3e91a4d2b85f60e1a9c4`, "ZM3D beta live-ops calendar - working rules", owner Frederick, shared with Julia as reader, Sep 24 | YES |
| "my live-ops calendar sheet" | `f_e4a17c90b3d25f6a8c1d73`, "ZM3D Beta Live-Ops Calendar", owned by Julia, tabs Calendar and Pushes | YES |
| "its ticket" | `ZOM-429` for the held weekly leaderboard: the only open ZOM leaderboard ticket (the others are completed), assignee Douglas `usr_cd7849ec043ab3da` | YES |
| "the calendar ticket" | `ZOM-78` "Event Calendar For Zombie Match 3D" (`cmt_zom78_1`: use this ticket, link the sheet here) | YES |
| "the recommendation he asked for" | the ask asks for her recommendation, sent back in the DM with the trade-offs, on what they run and what they hold in those weeks (`D05SD5QLG94/1759263617.418209`, as reworded in revision 4) | YES |
| state premise: nothing acts after the clock | every actor is active at 2025-10-01; nothing first appears after the seed bound (`00_Task_Context.json:/freeze_utc`); the Oct 8 release `evt_9a4c2e7f1b3d58e06c7a2f` is a future plan event | YES |

## Brief coverage

Each graded requirement has a trigger in the prompt (quoted spans are exact substrings):

| Graded requirement | Present in prompt (span) |
|---|---|
| Build the beat calendar in her sheet (seven beats) | "asking for the live-ops and push calendar for the Zombie Match 3D beta" ; "It goes in my live-ops calendar sheet" |
| Which beats, and the fields per beat (windows, held and until when, push, still-to-do and owner) | "What he wants in it is in his message" (the ask lists the fields; its thread reply keeps Zombie Lane off) |
| Build the push plan and its scope (ten rows) | "the live-ops and push calendar" ; "What he wants in it is in his message" (the thread reply names the rows) |
| Apply the brief's rules (deploy, scope, hold, late start, copy, lock) | "his working rules for building it are in the brief he shared with me" |
| Note the hold on the held beat's ticket | "If a beat ends up held, leave a note on its ticket so the owner picks it up" |
| Link the sheet on the calendar ticket | "link it on the calendar ticket" |
| Recommendation with trade-offs to Frederick | "send Frederick the recommendation he asked for" |
| Tell Brian the config date has to move before the lock | "his working rules" (the brief's lock rule: you tell the owner of a date that misses the lock) |

## Previous /prompt result (revision 1)

The previous prompt (157 words, sha256 b5d6559cdf26, with SQL sha256 4c6328ab2e86) **FAILED** the platform `/prompt`
on 2026-11-05 (`plateform_reports/6aea4c1e9b621f28dc3a5332_1_prompt.md`): Unique Ground Truth 2, Clarity 2, Contrived 2,
with Cross-Service Coherence 3. The local check of that prompt had predicted PASS; that was a miss, and the reason is
recorded here so this check is read with it in mind. What failed and what changed:

| Review issue | What failed | What changed in revision 2 |
|---|---|---|
| 1, 2, 4 (F1–F3) | the push plan: no-game copy, local notifications and the Domino-only rows each had two defensible outcomes | Frederick's thread reply under his ask (`D05SD5QLG94/1759263878.305129`) fixes the ten rows, leaves four named rows off and lets no-game copy go out |
| 3 | the prompt restated the ask's per-row fields (enumerated deliverable specs) | the two field-list sentences are gone; the prompt points to his message and his brief and is 100 words |
| 5 (F4) | the ticket-note condition (a beat that could not run yet) could cover Collect & Win and Season Pass | the condition is now a held beat, and the brief says a beat whose server windows are waiting on the release starts late and is not held |
| 6 (F5) | whether the Season Pass October season counts | Arthur's `#470#rc_10` says the Plague Race, leagues, Endless and Season Pass schedules already run on prod; the release event `evt_9a4c2e7f1b3d58e06c7a2f` covers only the windows still on the DEV stack |
| 7 (F6) | whether the daily-gift frame shipped | Samuel's note (`cmt_zom432_2` on ZOM-432 since revision 5; `#471#c_18` when the review ran) says it is in both submission builds, iOS 50 and Android 135, and nothing is left |
| 8 | Brian's mails numbered the Nov 1 season against the spec | both mails say the November season (`julia.lawson@harmonygames.co/1844311412966040123`) |
| F7 | whether the brief's login-calendar rollover is a ZM3D beat | the brief `f_7c3e91a4d2b85f60e1a9c4` ties the daily gift to Login Calendar on the push sheet as the same beat |

The prompt itself changed in three ways: the opening now says Frederick messaged her yesterday (a new premise, verified
above); the per-beat and per-push field list is replaced by one pointer to his message; the ticket-note condition is a
held beat. The destinations (her sheet, the calendar ticket, Frederick) are unchanged.

## Self-review

The C1–C24 walk (playbook check table); each names the strongest reading that **could fail** and why it does not.
Self-test against the 15 `calibration_cases` in `prompt_qc_cases.json`: none of the failing patterns matches
(`staged_errors`, `trap_hint_or_riddle`, `hidden_destination`, `audit_form`, `if_chain`, `false_state_premise`); the
nearest cases are the passing controls `control-plain-request` and `control-named-destination`.

- C1 field limit **could fail** outside 20–4,000 words — but it does not: 100 whitespace-delimited words, sha256 2a23afd87c4c (`04_Prompt.txt`).
- C2 assignment bound **could fail** on a missing field or an unsupported freeze — but it does not: all eight fields resolve in `00_Task_Context.json` (Julia Lawson, Product Manager, Product, Marketing and GTM, Planning and decision support, long-horizon, medium, Oct 1 2025 synth-cut); the context hash is 4bbc727fd48a since the re-bind to this machine.
- C3 persona and voice **could fail** if the work sat outside Julia's remit — but it does not: Frederick asks her directly (`D05SD5QLG94/1759263617.418209`), base `page_liveops_calendar` has her walking the coming weeks with him, and the platform scored Persona 5 on the same remit; the voice is a plain first-person hand-off, judged against the role only.
- C4 competency, task skill and function **could fail** on a mismatch with the actual work — but it does not: a live-ops and push calendar for a paid UA beta with a go/hold recommendation is Marketing and GTM planning, and the authored artifact is the two-tab sheet `f_e4a17c90b3d25f6a8c1d73` (platform: 5 on all three).
- C5 complexity and seeding **could fail** as Prompt Carries the Recipe, the family revision 1's field list fell into — but it does not: the prompt restates no field, rule, beat or row; they live in the ask, its reply and the brief `f_7c3e91a4d2b85f60e1a9c4`, and multi-source and dynamic change are load-bearing (brief §8).
- C6 fair outcomes **could fail** if a second defensible end state survived, as seven did on revision 1 (F1–F7) — but each now has a dated settling record (Fair readings; `D05SD5QLG94/1759263878.305129` for F1–F3) and no answer-key clause was added. The strongest Reading B left is the premium-strip note read as a change-request hold; since revision 8 the note is an inline comment inside Arthur's APPROVED review of #472 (`#472#rc_1`); in revisions 4 to 7 it was a plain conversation comment on #473, and while it was the review `#438#rev_4` its state was COMMENTED and the platform rejected that fork itself (P1-DR13).
- C7 clarity **could fail** on Action Decision Ambiguity, as revision 1 did on which beats get ticket notes — but it does not: the condition is a held beat, so the writes are one note on `ZOM-429`, the link on `ZOM-78`, the sheet and the DM. The counter to my own Minor finding: is the open channel for telling Brian a Fail? No: same recipient, and the platform called it minor (review advisory 4). Since revision 4 the channel is no longer open: the brief says you tell its owner in a reply on the mail where they committed to it.
- C8 incorporation **could fail** if a pointed-to record were unreadable, ambiguous or an answer key — but it does not: the message is Julia's own DM (root and reply both YES in check-sql), the brief `f_7c3e91a4d2b85f60e1a9c4` is shared with her, unique by title and states rules; the reply says which rows to plan, not their outcome. Only one message from Frederick asked for the calendar yesterday (`bca784379e7dbca9e64e79a64dfefbba`).
- C9 pre-solved **could fail** if a root cause, finding or count were stated — but it does not: no beat, push, date, cause or count is named; held appears only as a condition (C9).
- C10 discovery collapse **could fail** if a hidden authority were named by title, channel or id — but none is: the message and the brief are the anchors (brief §6). The Advisory rests on its own evidence: the reply sits in the anchor's thread (`D05SD5QLG94/1759263878.305129`), which `hardness_v2_check` classes as first_read.
- C11 investigation to action **could fail** with no finding-dependent write — but it does not: the sheet cells, the hold note, the link and the recommendation all depend on the reconciliation (brief §3).
- C12 tool use and cross-service **could fail** below two weighted services — but it does not: slack, gmail, gcal, gdocs, gsheets, gslides, github and linear each change a graded fact, and the base Confluence spec page decides the lock offset (brief §1; platform: 5). Trello no longer changes one since revision 5.
- C13 coherence **could fail** as a bolt-on list — but it does not: every sentence serves the one calendar hand-off, and deleting the brief pointer, the ticket-note sentence or the last sentence each removes a rule or a write (C13; platform: 5).
- C14 tool mention **could fail** on a function, parameter or server name — but it does not: the sheet and the two tickets are named in natural product phrasing (C14; `prompt_qc_examples.md`).
- C15 command list **could fail** on a scripted method of two or more steps — but it does not: the only sequencing is the order of deliverables and who to tell, which the platform passed on revision 1 (Anti-Patterns, Command List) and which is unchanged (C15).
- C16 ordinary request **could fail** on enumerated deliverable specs, the red flag that failed revision 1 (P4-DR1) — but it does not: both field-list sentences are gone and the prompt points to the ask, as the review recommended. The counter to my own PASS: prompts are screened for AI-written text; the replacement is short, plain and first-person with one condition, and matches no failing case in `prompt_qc_cases.json`.
- C17 truthfulness **could fail** on a phantom identifier or a false premise — but it does not: every premise is in the log above, re-read from the revision-2 SQL in this run (yesterday = `D05SD5QLG94/1759263617.418209` at 2025-09-30T20:20:17Z).
- C18 feasibility **could fail** if a deliverable were uncatalogable — but it does not: a sheet values update, a Slack send, a Linear comment and a Gmail reply are all cataloged writes; the sheet row has no web link, so the link for `ZOM-78` is built from the file id (a platform advisory, not a defect) (C18).
- C19 persona ACL **could fail** on a scoped read Julia lacks — but it does not: every scoped read is YES, the new reply included (check-sql on the revision-2 SQL: im `D05SD5QLG94` member); the `#zombie-prs` mirrors duplicate unscoped GitHub comments (C19).
- C20 today's date **could fail** on a relative date that resolves wrongly — but it does not: yesterday is Tue Sep 30 2025 against the Wed Oct 1 clock (`00_Task_Context.json:/universe/persona_today`) and Monday the 6th is Mon Oct 6 2025, a future plan date (C20).
- C21 injected friction **could fail** on an announced error or wait — but it does not: Friction: none (`03_Error_Async_Config.txt`) (C21).
- C22 universe coherence **could fail** on a touched-record inconsistency, as revision 1 did on Brian's season label — but the label is gone from both mails and two seeded-versus-base ordering slips are fixed (dossier §11); `base_check` Check A and Check C PASS on the revision-2 SQL. The platform `/injection` PASS on record is for revision 1, so this rests on the local re-run until `/injection` is re-run (C22). Revision 3 note: the platform `/prompt` review of revision 2 did fail this dimension, on the `ZOM-521` checklist against its open child tickets (known-issue card SC-15, which `base_check` does not test); revision 3 repairs it in the SQL (dossier §11 Revision 3), `base_check` Check A and Check C PASS on the revision-3 SQL, and the platform `/injection` PASS now on record is for revision 2.
- C23 originality **could fail** on overlap with a supplied sample — but none is supplied; the nearest library task (same-scenario tier, meaning 0.726) is a Julia to Frederick slot plan for Oct 13 – Dec 31, and this prompt keeps its own four-week window, push plan and hold/lock rules (review STEP 0.6: gate PASS) (C23).
- C24 diversity **could fail** as investigate plus one Slack message — but it does not: a two-tab sheet, a Linear note, a Linear link, a DM and a mail reply (C24).

Unresolved: none in the prompt text itself. Residual risks, in the order I would expect the platform to raise them:
(a) Arthur's premium-strip comment could be read as a change-request blocker on Season Pass under the brief's
hold rule. Since revision 8 it is an inline comment inside Arthur's APPROVED review of `#472`, so the review state itself
says no blocker; while it was a review on `#438` its state was COMMENTED and the platform rejected the fork once (P1-DR13). The independent run on revision 3
rejected the same fork again (its P1 DR1).
(b) "in" for the quests rollover: the brief asks whether the beat is in. The Trello note (`68dac8204f1e9a3b7c2d5e61`, Leonard,
on the open quests card) says more quests and the reward balance go in with the Mon Oct 13 rollover if they are ready and
that the weekly rollover does not wait on them, so the beat is in from week 1 and nothing is put down as still to do. That settles the one fork the
independent round on revision 5 failed Unique Ground Truth on. No criterion should grade the Quests still-to-do cell.
(c) The local stage gates cannot be re-pasted on this machine until the tools from the authoring machine are synced
(`hardness_gate` here does not know `volume_exception.rows_floor`). The pasted block below is from the earlier
revision; its hashes are stale by design and it is kept as a record until the re-paste.
Also open, outside the prompt: the follow-up reply's landing rate (family A14, but first_read locally), and the
sidecar outcome reviews in `00_V3_Authoring_Evidence.json`, which still describe the revision-1 outcomes.

```
STAGE GATE prompt-check: PASS — Task_Authoring/task_inputsS · 04_Prompt_Check.md#cbd20e3fb26d · 04_Prompt.txt#250e3a81692e · 04_Prompt_Writing_Brief.md#d7b9eabc6471 · __context__#7b0cc66ffd45 · __assignment__#e8b8269803d5 · __policy__#dc4ab5df3cdd · __gate_policy__#9b78441396d8 · __review__#808e1b2cd199 · blocking 0 · warnings 0 · checks 25
[PASS] assignment.v3_context: Julia Lawson / Product Manager; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#d7b9eabc6471, 00_Assigments.md#4844ae9f5ae7, 01_Grounding_Dossier.md#2ed958107b88, 01_Universe_Inject.sql#4c6328ab2e86, 03_Error_Async_Config.txt#ca4def2fa591, __context__#7b0cc66ffd45, __assignment__#e8b8269803d5, __policy__#dc4ab5df3cdd, __gate_policy__#9b78441396d8, __review__#461162429327)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (157 words, sha256 b5d6559cdf26)
[PASS] evidence.quoted_spans: 8 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 9 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 8/8 items carry a source pointer (min 100%)
[PASS] structure.summary_band: summary band present
[PASS] structure.summary_status: summary status present
[PASS] structure.clock: 'Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)' matches the universe
[PASS] tier.hardness: Long Horizon → --profile extreme: manifest present, hardness_gate PASS pasted in the dossier and current
[PASS] tier.hardness_rerun: hardness_gate --profile extreme re-run on the current manifest + SQL: PASS
[PASS] review.counter_readings: 24 evidenced counter-readings (of 24 found; need ≥ 24) in 04_Prompt_Check.md
[PASS] review.coverage: self-review addresses all 24 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] handoff.pasted: pasted into the Self-review by --paste
```


## Route

READY FOR /prompt on the findings: no Fail, one Minor clarity note (C7) and one hardness advisory (C10); whether to act
on them is the human's call. Before the platform run:

1. Sync the tools from the authoring machine, then re-run and re-paste the stage gates in order (injection,
   prompt-writing, prompt-check). The block above is the earlier revision's and will not match the current files: the
   prompt is now 100 words / sha256 2a23afd87c4c and the SQL is sha256 c955d6ca2bca (revision 4). Since revision 4 two
   things stop the injection gate even after the sync and have to be settled first (dossier §11, Revision 4): the
   cohort is 39, one short of 40, and the gate's own `base_check` re-run does not read the manifest's `repaired`
   resolution for `ZOM-387`.
2. Refresh the outcome and role reviews in `00_V3_Authoring_Evidence.json` for revision 2 (seven beats, ten push rows,
   no Zombie Lane or conditional-hold alternative, the new context hash); the prompt-check gate reads them.
3. Run the platform `/injection` and `/prompt` as a pair on the revision-4 SQL and this prompt, then `/hardness`. The
   `/injection` PASS on record is for the revision-2 SQL and is stale; the `/prompt` run on revision 2 failed on
   Cross-Service Coherence alone (SC-15), which revision 3 repairs; an independent run on revision 3 failed it on further
   items and gave Clarity 3, which revision 4 repairs. A `/prompt` FAIL is fatal: fix the cause in the
   data and re-check.

Carry-forward to /create-rubric-writing: grade all ten push rows and treat any of the four excluded rows as wrong; the
Plague Race start and Weekly Leaderboard reset criteria name the WIP (not LIVE) status and must not ask for a statement
about client wiring; Collect & Win is Runs with a late start and no ticket note; the only hold note is on `ZOM-429` and
the link on `ZOM-78` (bind W04/W05 to them); the still-to-do criteria stay polarity-aware (name the outstanding item,
not merely contain the keyword); the Season Pass premium strip is a still-to-do, never a hold; no criterion may cite
the brief for the 24h lock (it is base `page_season_pass_spec`).

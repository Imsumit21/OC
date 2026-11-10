# Prompt Check — claire-zm3d-halloween-art-plan

> Prompt: 04_Prompt.txt · @@WC@@ words · sha256 @@SHA@@ · checked 2026-11-06 against 04_Prompt_Writing_Brief.md (2026-11-06, digest @@BRIEF@@) · SQL sha256 @@SQL@@ (revision rev3) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

The prompt, byte for byte (no trailing newline):

```text
@@PROMPT@@
```

## Summary

**Fail 0 · Non-fail 0 · Advisory 6 · UNVERIFIED 0** · checks clean: C1, C2, C3, C4, C5, C7, C8, C9, C10, C11, C12, C14, C15, C16, C17, C18, C19, C21, C22, C24 · advisory: C6 (two later-stage notes), C13 (stacking), C20 (relative dates), C23 (no supplied samples) · predicted /prompt band: PASS · Status: READY FOR /prompt

This is a real check of the unchanged prompt against rev3, not a carry-over. The prompt is byte-identical to the one `/prompt` scored 5 on every dimension (`plateform_reports/6aea4c1eea32a6fa98b9b1d9_1_prompt-1.md`), but that score was on the rev2 universe. Every ask was re-walked, each of the six changed decisions was tested with its strongest Reading B, and the answer was re-derived from the records without the solver (`Working_Files/prompt_eval/rederive_rev3.py`, VERDICT: MATCH with `Working_Files/solver/truth.json`: 36 Refresh first, 12 Halloween version, 10 Skip, 0 Reuse; 42 Marcus, 6 Julia; 30 Fri Oct 10, 18 Wed Oct 15). The prompt needs no change.

The last check of this prompt held one Non-fail at C22: Leonard's base post about Thursday against the review he organized. The review's description has since changed, and C22 was re-tested rather than closed on sight (see C22 re-test). It is settled, so the Non-fail is dropped and the band moves from NON-FAIL to PASS. The residual risk is stated there: a strict reader could still object to the order of the two records, and that would cost at most this one minor.

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
| --- | --- | --- | --- | --- | --- |
| 1 | C6 | Fair outcomes · Advisory (rubric stage) | "who makes what by when" | playbook C6; brief §4b; surface slot S39 | S39 accepts only Oct 11–15 on marcus.bennett 4:5 (iOS UK phone), so a run that sets one safe Oct 10 for every ad loses it. Frederick's 'iOS UK stays on the 15th' (`C0880U9751A/1759275738.984915`) supports that as a date, but Oct 10 still meets his deadline. Keep any 09 criterion to the reply's words and do not stack more rows on this control. |
| 2 | C6 | Fair outcomes · Advisory (rubric stage) | "shared with everyone on the review" | brief §4b; Eval 1 §2.1 scope | Julia Lawson now makes six ads but is not on the review (`evt_d947bf7cd910549b674b1f`, 7 attendees). The prompt's sharing list is the review, so no criterion may require sharing with her; sharing with her is allowed as an extra. |
| 3 | C13 | Coherence · Advisory (stacking) | "Can you take his message and do it all for me?" | playbook C13: several asks serving one stated purpose are stacking, not bolt-ons (Eval 1 §1.3.2) | six writes (doc, tracker, comments, assignments, tickets, reply) all serve Leonard's one Halloween push and its review; deleting any one leaves a requested piece of `C06DJBJL798/1759269913.882683` undone — not a bolt-on |
| 4 | C20 | Alignment with Today's Date · Advisory | "yesterday" | Prompt Writing §4.2 asks for absolute dates; Eval 1 §2.8 allows relative wording (local override) | resolves to Tue Sep 30, 2025 (the ask, 22:05:13Z = 15:05 PT) against Wed Oct 1 in both PT and UTC; no fix needed |
| 5 | C20 | Alignment with Today's Date · Advisory | "Thursday's review" | as above | resolves to Thu Oct 2, 2025 09:00 PT / 16:00Z (`evt_d947bf7cd910549b674b1f`); one day in both zones |
| 6 | C23 | Originality · Advisory (N/A at /prompt) | "Leonard asked me in #zombie_marketing yesterday" | Eval 1 §2.9: compare only against supplied samples; none are supplied | the platform library check on this exact text: Gate PASS, nearest tier same scenario (meaning 0.719, wording 0.004), another Claire Morgan Halloween task with different surfaces, records and writes; rev3 changes no prompt wording |

## Asks against rev3

Every ask in the prompt, walked on the new universe. The writes are unchanged in kind; what changed is what the investigation must find before writing them.

| Ask (quoted span) | Concrete writes | What rev3 changed | Catalog path (`Working_Files/prompt_eval/check_runs_rev3.txt`) | Result |
| --- | --- | --- | --- | --- |
| "Can you take his message and do it all for me?" | none by itself; it incorporates the ask `C06DJBJL798/1759269913.882683` | nothing in the ask; its owner split is updated by its own author (`C05KNDCHAAG/1759275107.322377`) and its plan source by Frederick (`C0880U9751A/1759275738.984915`) | slack_read_channel | available, unique, instructions not answers (C8) |
| "Work out the Halloween call for everything that's live today, the store pages and every ad we're running" | none alone; feeds the tracker | 8 of 58 calls move: 2 Reuse to Halloween version, 2 Refresh first to Skip, 4 Halloween version to Refresh first; 3 more now rest on a note off the ticket with the call unchanged | linear_list_comments, gsheets_values_batch_get, gslides_get_presentation_text, gmail_get_message, trello_get_comments, slack_read_thread | feasible, re-derived |
| "who makes what by when" | none alone; feeds the tracker, the comments and the assignments | 6 makers Martin to Julia; 30 due dates Oct 15 to Oct 10 | as above | feasible |
| "put it in a plan doc and a tracker in my Drive" | gdocs_create_document, gsheets_create_spreadsheet, gsheets_values_update | contents only | both ran in the rev2 pre-check, 0 failed | feasible |
| "shared with everyone on the review so they can comment" | gdrive_share_file ×12 (6 people, 2 files) | no change: the invite is the same seven; see Finding 2 and the C22 re-test | `role: "commenter"` 12 of 12 in the pre-check | feasible |
| "Comment each ad's call and due date on its ART ticket" | linear_create_comment ×58 | 10 Skip ads now carry no date (8 before); none is Reuse | ran 58 times, 0 failed | feasible |
| "assign the ones that need new work to whoever's making them" | linear_update_issue ×48 | 42 Marcus, 6 Julia (`usr_8140f09bf9f1b94c`, active, in `team_ART`); no Reuse ad remains, so Skip is the only exclusion | ran 50 times, 0 failed; assignee by email worked | feasible |
| "open ART tickets for any new store art" | linear_create_issue ×2 | no change; Leonard's `C08R8CHB0QL/1759247246.453725` settles what counts | ran twice, 0 failed | feasible |
| "reply in Leonard's thread with both links before the review" | slack_send_message ×1 with thread_ts | no change; the ask still has reply_count 0 and no seeded reply | ran once, 0 failed | feasible |

## Fair readings (accepted outcomes)

| Deliverable | Reading A | Reading B | Resolution and evidence |
| --- | --- | --- | --- |
| Plan doc | a new Google Doc in Claire's Drive, shared (commenter / writer) with the six review attendees of `evt_d947bf7cd910549b674b1f` | a doc shared only with Leonard (the requester) | settled by the prompt ("shared with everyone on the review so they can comment") and the ask ("a plan doc we can comment on"); extra people allowed; role commenter or writer both accepted (brief §4b) |
| Sharing | the six others on the invite of `evt_d947bf7cd910549b674b1f`, Leonard included | leave Leonard off because `C05KNDCHAAG/1759279503.256079` says he won't attend internal meetings Thursday | settled by source identity: the prompt names the review, the event still lists him as accepted organizer, its description says he dials in for this one, and he asked for 'a plan doc we can comment on' (`C06DJBJL798/1759269913.882683`); extras allowed, Julia included |
| Tracker | a separate Halloween spreadsheet, one row per serving surface (62, `Working_Files/solver/truth.json`) | the sheet's rows only (60), or the tracker as a table in the doc | settled by the ask "plus a tracker" (two artifacts) and by Frederick's Trello comment `68dc65a0f2d7fb28743f5860` and his note `cmt_art831_2`, which keeps its 'Not on the live creatives sheet yet.' (two serving creatives the sheet omits) |
| Icon call | Halloween version, owner Martin, due by the Thu Oct 16 12:00 PT cut, with its own ART ticket | Reuse of Martin's Sep 17 concept `C08R8CHB0QL/1758121809.236839`, swapped around Oct 24 | settled by Robert's reply `C08R8CHB0QL/1758127951.679146` ("not for the app icon") and Arthur's calendar `f_fdd6d2d2f4a4d2f5b908fb` (the merge cut; icon in the Nov 6 clean-up) |
| Ad due dates | Fri Oct 10 on Android US phone, Wed Oct 15 otherwise | Fri Oct 17 (the Sep 12 draft), or Wed Oct 15 for all (the Sep 30 mail) | the draft falls to the mail `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>` ("not the 17th"), the mail to Frederick's reply `C0880U9751A/1759275738.984915`; see the six decisions below |
| Ticket comments | one comment per serving ad ticket (58), call + due date | the due date set in the ticket's field instead of a comment | settled by the prompt ("Comment each ad's call and due date on its ART ticket") and the ask ("drop a comment"); the field is allowed in addition |
| Assignments | the 48 ads that need new work: 42 Marcus, 6 Julia | every ad incl. Skip | settled by the prompt and the ask ("the ones that need new work") |
| New tickets | ART tickets for the Halloween icon and the Halloween iPad 12.9" set | tickets for every store set, or none for the icon | settled by the Store folder `d_74a7c95c28097dd9777e01` (iPhone and Play sets exist), Leonard's `C08R8CHB0QL/1759247246.453725` and Robert's reply; one ticket naming both pieces also accepted |
| Reply | a thread reply under `C06DJBJL798/1759269913.882683` with both links | a top-level post or a DM to Leonard | settled by the prompt ("reply in Leonard's thread") |

### The six rev3 decisions

Each row is the Eval 1 §2.1 two-reading test: Reading A is `Working_Files/solver/truth.json`, Reading B is the strongest alternative a careful run could defend, and the last column names which of the five checks settles it and the Claire-visible record that does. Each carrier's reach is brief §5 and §5a rows 31–36.

| Rule | Items | Prompt span that reaches it | Reading A | Reading B | Settled by | Result |
| --- | --- | --- | --- | --- | --- | --- |
| R_REVIEW_WINDOW | 30 of the 48 working ads | "who makes what by when" | Fri Oct 10 on Android US phone; Wed Oct 15 otherwise | Wed Oct 15 for every ad (`claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>`, 23:10Z: 'every Halloween ad') | newer source, same author, same issue: `C0880U9751A/1759275738.984915` (23:42Z) 'has to be with me by Fri Oct 10, not the 15th'; scope: 'iOS UK stays on the 15th'. An ad on both campaigns takes Oct 10 because it is going on Android US phone | settled, one outcome |
| R_RECAPTURE_NOTE | couch alpha 50, barrel marketing2 4:5, balloons alpha 50 (1) | "Work out the Halloween call" | Halloween version | Refresh first on the April tickets (`cmt_art795_1`, `cmt_art805_1`, `cmt_art797_1`) | newer source plus authority: `C09ATAJ220H/1758823964.738872` under the deck's 'the newest capture is the one that counts' (`f_5ebf55ad29e815d46243c8`); the exports ART-852, ART-853, ART-854 corroborate the builds. Scope: 're-recorded 3' keeps couch alpha 50 16:9 Refresh first | settled, one outcome |
| R_TEST_TURNED_DOWN | cheer fastcouch 9:16, 16:9 | "Work out the Halloween call" | Halloween version, assigned to Marcus | Reuse (`D05V2N6PZNU/1759166437.080255`, `f_dc5cf9e4250d433c1511ec`); or Refresh first because the test sits on the July capture | newer source plus authority: Robert `C08R8CHB0QL/1759248337.170599` 'We can't ship these, they need doing again from the Sep 16 one', Marcus `C08R8CHB0QL/1759249269.380507`. Refresh first falls to the tickets (`cmt_art808_2`, `cmt_art816_2`: Sep 16, Android #1896) and the deck: the art is current, the test is what failed | settled, one outcome |
| R_STATICS_COVER | the 6 working statics (ART-825 … ART-830) | "whoever's making them" | Julia Lawson | Martin Walsh (the ask: 'Martin has the icon and the stills') | newer source, same author as the ask: Leonard `C05KNDCHAAG/1759275107.322377` 'julia on the ad statics works for me', on Martin's `C05KNDCHAAG/1759243286.478812`. Scope: 'store art stays with me' keeps the icon and iPad set with Martin; his Oct 6–15 leave makes an early internal date sensible, and §4b allows one | settled, one outcome |
| R_TABLET_TRIM | squirrelfail landscape, mrfluffernot landscape | "every ad we're running" | Skip, no assignee, no date | Refresh first on iOS UK tablet (`cmt_art811_2`, `cmt_art813_1`) | newer source: `claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>` (Sep 29) 'off iOS UK tablet … Both stay on Android US tablet', then the changes mail's 'anything that only runs there'. The mail's 'Everything else in the plan stands' does not reach it: the plan names no cut. Both stay rows: they are live today | settled, one outcome |
| R_OLD_PACKS | end card 001 and its 16:9, 1:1, 4:5 | "Work out the Halloween call" | Refresh first | Halloween version on Android #1529 (`cmt_art833_1`) | newer source plus authority: `68d6cff0c6568da5d9c8e81f` 'they need a re-render before anyone builds on them' under the deck's 'Refresh first: re-capture, re-render or re-cut'. 'They can keep serving for now' keeps them in scope; it is about serving, not the seasonal pass. Base lineage `C08R8CHB0QL/1754310794.907609`, `C08R8CHB0QL/1754316299.381419` agrees | settled, one outcome |

No rev3 decision leaves two fair outcomes, so no BOTH_FAIR_FIGURE is claimed. Every settling record is one Claire can open (check-sql verdict PASS; Trello unscoped). The six carriers are facts on fields the prompt already asks for, not new requirements, so `prompt-incorporation-v1` is not stretched (Eval 1 §1.2): none needs a sentence in the prompt.

## Verification log

| Span | Type | Universe record (locator) | Result |
| --- | --- | --- | --- |
| "Leonard asked me" | person / event | Leonard Hayes `EMPLOYEE_0038_SLACK_ID`, leonard.hayes@harmonygames.co; the ask `C06DJBJL798/1759269913.882683` @-mentions `EMPLOYEE_0009_SLACK_ID` (Claire) | verified (SQL L12, check-sql YES) |
| "#zombie_marketing" | channel | `C06DJBJL798` name zombie_marketing, private, 17 members incl. EMPLOYEE_0009_SLACK_ID (slack channels.json via hg.py, `check_runs_rev3.txt`) | verified |
| "yesterday" | date | the ask ts 1759269913.882683 = 2025-09-30T22:05:13Z = Tue Sep 30 15:05 PT; persona today Wed Oct 1 (`Working_Files/00_Task_Context.json`) | verified |
| "to own the art side of Halloween for Zombie Match 3D" | event / narrative | the ask: "halloween for ZM … can you own the art side?" `C06DJBJL798/1759269913.882683`; game name "Zombie Match 3D - Art Department" (C08R8CHB0QL purpose in slack channels.json via hg.py, `check_runs_rev3.txt`) and `f_fdd6d2d2f4a4d2f5b908fb` ("Zombie Match 3D store submissions") | verified |
| "I'm walking everyone through it at Thursday's review" | state / narrative | `evt_d947bf7cd910549b674b1f` "ZM3D Halloween review", Thu Oct 2 16:00–16:30Z, status confirmed, description "Claire walks us through the Halloween plan and tracker. I'm in LA Thursday so I'll dial in for this one.", organizer leonard.hayes@harmonygames.co; `C05KNDCHAAG/1759279503.256079` neither names nor cancels it | verified (Claire's own calendar copy, check-sql YES); see C22 re-test |
| "his message" | doc (incorporated) | `C06DJBJL798/1759269913.882683` — the one Halloween ask from Leonard to Claire (no other seeded or base ask; persona_view search "halloween for ZM" base 0, overlay 1) | verified, unique |
| "everything that's live today" | requested scope | the ask's own phrase ("go through everything that's live today", `C06DJBJL798/1759269913.882683`); not a premise | n/a (requested work) |
| "the store pages and every ad we're running" | requested scope | the ask `C06DJBJL798/1759269913.882683` ("store pages and every ad we're running") | n/a (requested work) |
| "in my Drive" | destination | Claire's Drive root `d_7fe31e7ec81996189e1f14` (owner claire.morgan@harmonygames.co, gdrive data.json via hg.py) | verified |
| "everyone on the review" | recipients | attendees of `evt_d947bf7cd910549b674b1f`: leonard.hayes@ (organizer, accepted), frederick.stone@, martin.walsh@, marcus.bennett@, robert@, arthur.blake@harmonygames.co (+ Claire); no departed person (Victor Barnes absent, SC-36); Julia not on it; re-read in `Working_Files/prompt_eval/check_runs_rev3.txt` | verified; Leonard stays on the list, dialling in (C22 re-test) |
| "its ART ticket" | state (each ad has one) | the sheet's Read me `f_02b1968f5e882366fbb883` ("Each Unity row links its ART ticket"); off-sheet ads `ART-826`, `ART-831`; library `ART-793` … `ART-854` team_ART | verified |
| "open ART tickets" | destination | Linear team `team_ART`; Claire's membership `tmem_team_ART_usr_7fe31e7ec8199618` (linear data.json via hg.py) | verified |
| "whoever's making them" | relationship | the ask's owner split, updated for the ad statics by `C05KNDCHAAG/1759243286.478812` and `C05KNDCHAAG/1759275107.322377`; Linear users `usr_c77c50cc15c5342d`, `usr_8140f09bf9f1b94c`, `usr_51f5f16d46e8cf55`, all in `team_ART`; all active at the clock (`Task_Authoring/references/universe_kb/by_universe/synthcut/activity.json`, status active_sep_2025_quiet_in_oct) | verified |
| "Leonard's thread" | destination | the ask `C06DJBJL798/1759269913.882683` is a top-level message (reply_count 0, no seeded reply under it, re-read on this SQL) | verified |
| "before the review" | deadline | `evt_d947bf7cd910549b674b1f` Thu Oct 2 09:00 PT | verified (future event, allowed) |

Absence claims in the prompt: none. Identity checks (`entity.py resolve`): "Leonard" → leonard.hayes@harmonygames.co only (brief §10). The prompt names no other person, so the Marcus Bennett / Marcus Lee, Martin Walsh / Martin Lewis and Julia Lawson / Peter Lawson traps sit in the records, not in the text.

## Brief coverage

| Brief item (§4 deliverables, §6 triggers) | Present in the prompt (quoted span, or "absent") |
| --- | --- |
| Anchor A1 (Leonard's Halloween message) | "Leonard asked me in #zombie_marketing yesterday" · "take his message" |
| Plan doc (§4) | "put it in a plan doc" |
| Tracker (§4) | "a tracker in my Drive" |
| Sharing (§4b, RO7) | "shared with everyone on the review so they can comment" |
| Ticket comments (§4, RO1, RO2) | "Comment each ad's call and due date on its ART ticket" |
| Assignments (§4, RO3) | "assign the ones that need new work to whoever's making them" |
| New store-art tickets (§4, S04, S26) | "open ART tickets for any new store art" |
| Reply (§4, D01, D02) | "reply in Leonard's thread with both links before the review" |
| R1 scope trigger (§6) | "everything that's live today, the store pages and every ad we're running" |
| R2 / R6 call trigger (§6) | "the Halloween call" |
| R3–R5 dates trigger (§6) | "who makes what by when" |
| R7 reuse trigger (§6) | "do it all for me" (incorporates the ask's question about what we already have) |
| R8 owners trigger (§6, S31, S32) | "whoever's making them" |
| R5 Android date (§6, S37–S39) | "due date" |
| Deadline (§7) | "at Thursday's review" |

## Calibration self-test

Against the 15 `calibration_cases` of `Evals/references/rules/prompt_qc_cases.json` (matched = the prompt shows the case's pattern):

| Case | Rule | Matched? | Why |
| --- | --- | --- | --- |
| K11-staged-errors | staged_errors | not matched | no misspelling; normal capitals and punctuation |
| K11-control-spelled-correctly | staged_errors | matched (PASS control) | clean spelling |
| K31-trap-hint | trap_hint_or_riddle | not matched | no line points at a hidden trap; nothing like "not on anybody's list" |
| control-symptom | trap_hint_or_riddle | matched (PASS control) | names the situation (Leonard's ask) only |
| K42-hidden-destination | hidden_destination | not matched | every destination is named |
| K47-hidden-destination | hidden_destination | not matched | as above |
| K44-hidden-destination | hidden_destination | not matched | the reply's place is named ("Leonard's thread") |
| control-named-destination | hidden_destination | matched (PASS control) | "#zombie_marketing", "my Drive", "its ART ticket", "Leonard's thread" |
| K1-audit-form | audit_form | not matched | no "reconcile / classify / complete the artifacts it requires" chain |
| K43-audit-form | audit_form | not matched | as above |
| K44-if-chain | if_chain | not matched | no conditional clause |
| control-plain-request | audit_form | matched (PASS control) | one plain request whose rules live in records |
| K43-departed-person-premise | false_state_premise | not matched | every named person is active at the clock (activity.json status active_sep_2025_quiet_in_oct; Leonard last Slack 2025-10-01) |
| K50-both-fair-figure | ugt_both_fair_figure | not matched | no reported figure is asked |
| K49-newer-source | ugt_both_fair_figure | not matched | the date forks (draft vs changes mail, changes mail vs Frederick's reply) are settled by the newer source, as in the case |

## C22 re-test

The record that changed: the review `evt_d947bf7cd910549b674b1f` now reads "Claire walks us through the Halloween plan and tracker. I'm in LA Thursday so I'll dial in for this one." (all 7 copies; created and updated Sep 30 22:10Z). Leonard's base post `C05KNDCHAAG/1759279503.256079` stands at Oct 1 00:45:03Z, 2h35m later: "I'm flying to LA to meet with investors and won't attend internal meeting tomorrow and Thu. I'm flying back home Friday morning so will miss All hands as well." Evidence: `Working_Files/prompt_eval/c22_rev3.txt`.

**The strongest case that it is still a contradiction.**

- The review is an internal meeting. All seven attendees are harmonygames.co, and Leonard's own usage treats "internal" as the opposite of external (`D04UP2L3E3S/1721755449.877429`: 'if it's an internal meeting and a 1:1 type of meeting I won't mind moving but sometimes it's external'; a DM Claire cannot read, so it is used only against this check's own argument and settles nothing).
- The post is unqualified and it is the newer record. Eval 1 §2.1 says a later update can resolve an earlier statement without announcing replacement, and this check used that same test on the six decisions, where Frederick's reply beat his own mail by 32 minutes. Letting the older record win here looks like a double standard.
- "Won't attend" and "I'll dial in" cannot both be true of one meeting if the post covers it.

**What failed and is not relied on.** I expected "internal meeting" to mean a standing meeting, which would put the review out of scope. Standing series do fall on both days on Claire's calendar (`(Wednesday) Mid Week Art Sync` `evt_db8e6bc32e4038ac7063f6`; `Daily Huddle - Engineering + Design Only (Thursday)`), but the usage above shows the phrase is a general category. By its words, the post covers the review. That argument is conceded.

**Why it is settled anyway.**

- The two records state one plan at two grains, so both can be true. The description already knows the trip ("I'm in LA Thursday"), and "for this one" only means something as an exception to a general absence. The post is that general absence. Every element of this reading is in the records; nothing is invented.
- The newer-source test is applied the same way, not relaxed. It reaches the latest source for the same issue and scope (Eval 1 §2.1). In all six decisions the winner was both newer and at least as specific, and it carried something new: Frederick's reply brings Unity's review and names its target ("not the 15th"). Leonard's post is newer but more general, names no review, and adds no fact the description had not already allowed for. A later general notice does not undo an earlier specific arrangement unless it says so.
- Nothing withdraws the arrangement at the clock: the event was not edited after the post (updated Sep 30 22:10Z, sequence 0), status confirmed, Leonard still accepted, and it carries a Meet link, so dialling in has a real route. The trip is consistent across records: LA on Thursday, home Friday morning.
- Eval 1 §3.2 needs a demonstrated inconsistency, and two statements that can both be true are not one. The resolving records are both ones Claire can open.

**Verdict.** Settled: no demonstrated inconsistency, so C22 is clean and the Non-fail is dropped. It never affected a write or the prompt's premise.

**Residual risk, stated plainly.** The specific note comes before the general post. That order cannot be reversed in the seed: the post is at 00:45Z and the seed bound is 2025-10-01T00:00:00Z. A strict reader could still object; the most that costs is the one minor this check held before, and it changes no write. The trip has no earlier record than the description ('flying to LA': 1 hit in all of Slack), which is ordinary, since people know their travel before they announce it.

## Self-review

Re-read as the eval: `Evals/1_Prompt_Eval.md` Phases 1–3 walked against this report; every C-check has a result below.

| Check | Strongest counter-reading | Resolution (evidence) | Result |
| --- | --- | --- | --- |
| C1 | Could fail: the field rejects very short or long prompts | @@WC@@ words, inside 20–4,000 (`04_Prompt.txt` sha256 @@SHA@@, 669 bytes, unchanged) | clean |
| C2 | Could fail: an assignment field is missing or off-roster | all eight fields in `Working_Files/00_Task_Context.json`; claire_morgan resolves in `Evals/references/persona/roster.json`; freeze 2025-10-01T00:00:00Z | clean |
| C3 | Counter: an art lead would not run a marketing push; better fit is Frederick (UA); rev3's maker is a Product Manager, so Claire no longer controls who makes the statics | Leonard asks Claire by name for "the art side" (`C06DJBJL798/1759269913.882683`); Julia making statics is Leonard's and Martin's call (`C05KNDCHAAG/1759275107.322377`), and Claire only records it; a better-fitting colleague alone is not a Fail (Eval 1 §1.1) | clean |
| C4 | Counter: Marketing and GTM is really UA buying, and Authoring is only a Slack post | the work is the seasonal GTM art plan; the plan doc is the authored artifact (brief §1); no spend is asked, and rev3's Unity carriers are dates and campaign membership, not figures (`Working_Files/research/prompt/kdi.md` SC-11/12/23) | clean |
| C5 | Counter: the prompt carries the recipe (it lists six writes), or rev3's rules leak into it | the writes are the ask's own deliverables; no rule, threshold, date or source is stated (`hardness_v2_check.py` re-run on rev3: RULE_IN_PROMPT CLEAN; brief §9 scan 0 found); Ambiguity, Dynamic Change and Multi-Source are all load-bearing and deeper on rev3 (brief §8) | clean |
| C6 | Strongest Reading B on rev3: every ad due Oct 15 under Frederick's own mail; cheer fastcouch reused; the stills with Martin as Leonard's message says | each settled by a newer, Claire-visible record (Fair readings, six decisions; `C0880U9751A/1759275738.984915`, `C08R8CHB0QL/1759248337.170599`, `C05KNDCHAAG/1759275107.322377`); an independent re-derivation matches truth (`Working_Files/prompt_eval/rederive_rev3.py`); two rubric-stage notes are Findings 1 and 2 | Advisory |
| C7 | Counter: "comment … on its ART ticket" could mean the due-date field; "share" leaves the role open; "a tracker" leaves the file type open; two tickets or one | reported, none changes a write: the ask says "drop a comment" and the field is allowed in addition; "so they can comment" pins the permission, commenter or writer both give it; "in my Drive" plus the ask's "tracker" is a spreadsheet by ordinary use; one or two store tickets is accepted (brief §4b). Channel (thread), time (before the review) and destinations are pinned. No "I'll" beside an agent ask: the only first-person verb is "I'm walking", a meeting, not a write (`check_runs_rev3.txt`). The platform scored Clarity 5 on these words (`plateform_reports/6aea4c1eea32a6fa98b9b1d9_1_prompt-1.md`), and rev3 touches none of them | clean |
| C8 | Counter: "his message" is ambiguous or hands over answers; or a carrier the prompt never points at is an unauthorized requirement | one Halloween ask from Leonard to Claire (`C06DJBJL798/1759269913.882683`, overlay 1 hit for "halloween for ZM" in `Working_Files/prompt_gen/research/sap_raw.txt`); it names sources and owners, no calls (brief §6). The carriers are facts on asked fields, not rules: Frederick and Leonard update their own statements, the other four feed the deck's incorporated rule (Eval 1 §2.1 newer source) | clean |
| C9 | Counter: "everything that's live today" presupposes the scope; "both links" presupposes two files | scope words are the requester's; the two links are the two requested outputs, not findings; no count, culprit, date or root cause (brief §9 scan: 0 of the rule words) | clean |
| C10 | Counter: naming "Thursday's review" collapses discovery of the attendee list; or a rev3 channel is named | the review is the persona's own meeting and the ask names it (§5 row 18 "Yes"); no §5 "No" item is named: #zm-animations, #company-internal and #zombie-match3d do not appear (brief §9 scan, `Working_Files/prompt_gen/build_brief.py`) | clean |
| C11 | Counter: the writes could be done without investigation | each comment and assignment needs its ticket's campaigns, capture and master (§5 rows 13, 14) and, on rev3, up to six off-ticket corrections (§5 rows 31–36) | clean |
| C12 | Counter: one service carries all the weight (Linear) | the six carriers alone sit in Slack, Gmail and Trello; nine services carry a deciding fact (brief §1, `01_Hardness_Manifest.json` services); dossier HARDNESS GATE (extreme): PASS, re-checked by this gate (`tier.hardness`) | clean |
| C13 | Counter: the ticket follow-through is a bolt-on to the plan | every write serves the one push and the review (Finding 3); stacking only; the platform's deep recheck rejected the over-stacking flag P4-DR1 on the same words | Advisory |
| C14 | Counter: "my Drive", "ART ticket" name tools | product names; 0 of 298 catalog tool names, 0 camelCase or snake_case parameter names, 0 hits for `MCP`, `tool`, `linear_`, `gmail_`, `slack_` (`Working_Files/prompt_eval/check_runs_rev3.txt`; `Evals/references/rules/common_errors.md` §3) | clean |
| C15 | Counter: the writes are a sequenced command list, or a First / Then / Finally search hit (`Evals/references/rules/common_errors.md` §3: "A hit fails") | 0 hits for First, Then, Finally, next, step (`check_runs_rev3.txt`); the order is deliverables and who to tell, with no source order or method (Eval 1 §1.3.1) | clean |
| C16 | Counter: an enumerated list of writes reads as a spec sheet; or "everything that's live today" now reads as a riddle pointing at rev3's traps | one sentence of plain asks with no column, format or wording rule; 0 of 4 spec-sheet triggers; 0 conditional words (`check_runs_rev3.txt`); the phrase is Leonard's own (`C06DJBJL798/1759269913.882683`) and points at no record (case control-symptom) | clean |
| C17 | Counter: "I'm walking everyone through it" is false if Leonard is flying to LA on Thursday and won't attend internal meetings; or "yesterday" is false | `evt_d947bf7cd910549b674b1f` is confirmed, its description says Claire walks the team through and that Leonard dials in from LA, and `C05KNDCHAAG/1759279503.256079` names no review; the premise is Claire's plan for a meeting that exists at the clock, so no state premise is contradicted (C22 re-test). Ask 2025-09-30T22:05:13Z = yesterday; every tight identifier in the verification log above | clean |
| C18 | Counter: a rev3 write cannot be made: Julia is off the team, or "so they can comment" needs a role the catalog lacks, or the carriers have no cataloged read | `usr_8140f09bf9f1b94c` is active and in `team_ART`; 24 needed tools exist in the catalog; `gdrive_share_file` took commenter 12 of 12 and `linear_update_issue` took an assignee email 48 times in the pre-check, 0 failed (`check_runs_rev3.txt`); slack_read_thread, gmail_get_message and trello_get_comments read the carriers. Evidence limit: no run has yet assigned to Julia's account | clean |
| C19 | Counter: a required read is in someone else's mailbox or calendar, or in one of the three private channels rev3 uses | Claire's own copies of all three mails and the event; she is a member of #zm-animations, #company-internal and #zombie-match3d (`check_runs_rev3.txt`); check-sql PASS (0 load-bearing rows not visible, including `C09ATAJ220H/1758823964.738872`, `C05KNDCHAAG/1759243286.478812`, `C0880U9751A/1759275738.984915`); base records can-see YES (brief §5a); no ask reads another person's scoped data | clean |
| C20 | Counter: relative dates fail | Eval 1 §2.8 local override: relative wording never fails; both resolve to one day (Findings 4–5) | Advisory |
| C21 | Counter: friction is announced, or Unity's manual review is an injected wait | `03_Error_Async_Config.txt` Friction: none; the manual review is a story fact in `C0880U9751A/1759275738.984915`, not a tool wait, and the prompt does not mention it | clean |
| C22 | Counter to a clean result: Leonard says he won't attend internal meetings Thursday, the review is one by his own usage, and his post is 2h35m newer than the description, so the newer-source check used on the six decisions should make the post win. Counter to keeping the Non-fail: both records state one plan at two grains | clean on the argument in C22 re-test: the note names the trip and "this one", the post is general, names no review and adds nothing the note had not priced in; the event was not edited after it (`evt_d947bf7cd910549b674b1f` sequence 0, Leonard accepted, Meet link present). Otherwise clean on sha256 @@SQL@@: `base_check.py` PASS (233 inserts, 5 updates), `hg.py lint` 0 FAIL, 0 CHECK, every seeded Slack author is a channel member and every reply follows its parent (`Working_Files/prompt_eval/coherence_rev3.py` PASS), stage gate injection PASS. Platform `/injection` has not yet seen this hash | clean |
| C23 | Counter: the scenario repeats a sibling (the library's other Claire Morgan Halloween task, Frederick's beta calendar) | no supplied samples (Eval 1 §2.9); platform library check on this exact text: Gate PASS, wording 0.004; different asks (comments and assignments on 58 tickets) from `Task_Authoring/task_inputsS/04_Prompt.txt`; fingerprint ≤ 2 of 7 | Advisory |
| C24 | Counter: investigate + one Slack post | a doc, a sheet, 58 comments, 48 assignments, new tickets and a thread reply (brief §4) | clean |

Mechanics: every quoted span above was verified as an exact substring of `04_Prompt.txt` by the gate; the prompt hash is identical before and after this check (sha256 @@SHA@@).

Facts re-verified in this run, not carried from the brief: the prompt's bytes and hash, every premise identifier, the attendees, channel memberships and Linear memberships (`Working_Files/prompt_eval/check_runs_rev3.py`), all 58 ad calls, owners and dates (`rederive_rev3.py`), the seeded Slack authors and thread order (`coherence_rev3.py`), the review, Leonard's post and the phrase's usage (`c22_rev3.py`), every §5a search (`Working_Files/prompt_gen/run_research.py`).

Unresolved: none. Evidence limits: no run has yet assigned a ticket to Julia Lawson's account; search ordering is rev2 run evidence; platform `/injection` and `/prompt` have not seen SQL sha256 @@SQL@@; `Working_Files/prompt_eval/1_prompt_redteam.md` is an emulation on the older SQL 29bc98c6e28b and is not evidence for rev3.

## Route

No Fail: paste `04_Prompt.txt` exactly as saved into `/prompt`, paired with `/injection` (SQL sha256 @@SQL@@), answering the task date with Oct 1, 2025 (synth-cut).

Carry to `/create-oe-writing` and `/create-rubric-writing`: Findings 1 and 2, no event or criterion on whether Leonard attends the review, and that the rev2 `/prompt` advice about "the two Reuse ads (ART-808, ART-816)" is stale: on rev3 no ad is Reuse. Next: `/create-humantime`.

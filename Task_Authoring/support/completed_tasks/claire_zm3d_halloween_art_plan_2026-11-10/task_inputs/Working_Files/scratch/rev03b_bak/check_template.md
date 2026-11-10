# Prompt Check — claire-zm3d-halloween-art-plan

> Prompt: 04_Prompt.txt · @@WC@@ words · sha256 @@SHA@@ · checked 2026-11-04 against 04_Prompt_Writing_Brief.md (2026-11-04, digest @@BRIEF@@) · SQL sha256 @@SQL@@ (revision 03) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

The prompt, byte for byte (no trailing newline):

```text
@@PROMPT@@
```

## Summary

**Fail 0 · Non-fail 0 · Advisory 3 · UNVERIFIED 0** · checks clean: C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C14, C15, C16, C17, C18, C19, C21, C22, C24 · advisory: C13 (stacking), C20 (relative dates), C23 (no supplied samples) · predicted /prompt band: PASS · Status: READY FOR /prompt

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
| --- | --- | --- | --- | --- | --- |
| 1 | C13 | Coherence · Advisory (stacking) | "Can you take his message and do it all for me?" | playbook C13: several asks serving one stated purpose are stacking, not bolt-ons (Eval 1 §1.3.2) | six writes (doc, tracker, comments, assignments, tickets, reply) all serve Leonard's one Halloween push and its review; deleting any one leaves a requested piece of `C06DJBJL798/1759269913.882683` undone — not a bolt-on |
| 2 | C20 | Alignment with Today's Date · Advisory | "yesterday" | Prompt Writing §4.2 asks for absolute dates; Eval 1 §2.8 allows relative wording (local override) | resolves to Tue Sep 30, 2025 (the ask, 22:05:13Z = 15:05 PT) against Wed Oct 1 in both PT and UTC; no fix needed |
| 3 | C20 | Alignment with Today's Date · Advisory | "Thursday's review" | as above | resolves to Thu Oct 2, 2025 09:00 PT / 16:00Z (`evt_d947bf7cd910549b674b1f`); one day in both zones |
| 4 | C23 | Originality · Advisory (N/A at /prompt) | "Leonard asked me in #zombie_marketing yesterday" | Eval 1 §2.9: compare only against supplied samples; none are supplied | fingerprinted against the workspace siblings anyway (§ Self-review C23): different scenario, entities, asks and writes |

## Fair readings (accepted outcomes)

| Deliverable | Reading A | Reading B | Resolution and evidence |
| --- | --- | --- | --- |
| Plan doc | a new Google Doc in Claire's Drive, shared (commenter / writer) with the six review attendees of `evt_d947bf7cd910549b674b1f` | a doc shared only with Leonard (the requester) | settled by the prompt ("shared with everyone on the review so they can comment") and the ask ("a plan doc we can comment on"); extra people allowed; role commenter or writer both accepted (brief §4b) |
| Tracker | a separate Halloween spreadsheet, one row per serving surface (62, `Working_Files/solver/truth.json`) | the sheet's rows only (60), or the tracker as a table in the doc | settled by the ask "plus a tracker" (two artifacts) and by Frederick's Trello comment `68dc65a0f2d7fb28743f5860` and his note `cmt_art831_2` (two serving creatives the sheet omits) |
| Icon call | Halloween version, owner Martin, due by the Thu Oct 16 12:00 PT cut, with its own ART ticket | Reuse of Martin's Sep 17 concept `C08R8CHB0QL/1758121809.236839`, swapped around Oct 24 | settled by Robert's reply `C08R8CHB0QL/1758127951.679146` ("not for the app icon") and Arthur's calendar `f_fdd6d2d2f4a4d2f5b908fb` (the merge cut; icon in the Nov 6 clean-up) |
| Ad due dates | Wed Oct 15 for every ad that needs work | Fri Oct 17 (the Sep 12 draft) | settled by the newer mail `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>` ("not the 17th") |
| Reuse ads' due | Wed Oct 15 (with Frederick) | no date (nothing to make) | both accepted (brief §4b): same calls, same assignments, same destinations; the comment differs only in the date text |
| Ticket comments | one comment per serving ad ticket (58), call + due date | the due date set in the ticket's field instead of a comment | settled by the prompt ("Comment each ad's call and due date on its ART ticket") and the ask ("drop a comment"); the field is allowed in addition |
| Assignments | the 48 ads that need new work, to their maker | every ad incl. Reuse / Skip | settled by the prompt and the ask ("the ones that need new work") |
| New tickets | ART tickets for the Halloween icon and the Halloween iPad 12.9" set | tickets for every store set, or none for the icon | settled by the Store folder `d_74a7c95c28097dd9777e01` (iPhone and Play sets exist) and Robert's reply; one ticket naming both pieces also accepted |
| Reply | a thread reply under `C06DJBJL798/1759269913.882683` with both links | a top-level post or a DM to Leonard | settled by the prompt ("reply in Leonard's thread") |

## Verification log

| Span | Type | Universe record (locator) | Result |
| --- | --- | --- | --- |
| "Leonard asked me" | person / event | Leonard Hayes `EMPLOYEE_0038_SLACK_ID`, leonard.hayes@harmonygames.co; the ask `C06DJBJL798/1759269913.882683` @-mentions `EMPLOYEE_0009_SLACK_ID` (Claire) | verified (SQL L12, check-sql YES) |
| "#zombie_marketing" | channel | `C06DJBJL798` name zombie_marketing, private, 17 members incl. EMPLOYEE_0009_SLACK_ID (slack channels.json via hg.py) | verified |
| "yesterday" | date | the ask ts 1759269913.882683 = 2025-09-30T22:05:13Z = Tue Sep 30 15:05 PT; persona today Wed Oct 1 (`Working_Files/00_Task_Context.json`) | verified |
| "to own the art side of Halloween for Zombie Match 3D" | event / narrative | the ask: "halloween for ZM … can you own the art side?" `C06DJBJL798/1759269913.882683`; game name "Zombie Match 3D - Art Department" (slack channels.json /129/purpose, hg.py) and `f_fdd6d2d2f4a4d2f5b908fb` ("Zombie Match 3D store submissions") | verified |
| "I'm walking everyone through it at Thursday's review" | state / narrative | `evt_d947bf7cd910549b674b1f` "ZM3D Halloween review", Thu Oct 2 16:00–16:30Z, description "Claire walks us through the Halloween plan and tracker.", organizer leonard.hayes@harmonygames.co | verified (Claire's own calendar copy, check-sql YES) |
| "his message" | doc (incorporated) | `C06DJBJL798/1759269913.882683` — the one Halloween ask from Leonard to Claire (no other seeded or base ask; persona_view search "halloween for ZM" base 0, overlay 1) | verified, unique |
| "everything that's live today" | requested scope | the ask's own phrase ("go through everything that's live today", `C06DJBJL798/1759269913.882683`); not a premise | n/a (requested work) |
| "the store pages and every ad we're running" | requested scope | the ask `C06DJBJL798/1759269913.882683` ("store pages and every ad we're running") | n/a (requested work) |
| "in my Drive" | destination | Claire's Drive root `d_7fe31e7ec81996189e1f14` (owner claire.morgan@harmonygames.co, gdrive data.json via hg.py) | verified |
| "everyone on the review" | recipients | attendees of `evt_d947bf7cd910549b674b1f`: leonard.hayes@, frederick.stone@, martin.walsh@, marcus.bennett@, robert@, arthur.blake@harmonygames.co (+ Claire); no departed person (Victor Barnes absent, SC-36) | verified |
| "its ART ticket" | state (each ad has one) | the sheet's Read me `f_02b1968f5e882366fbb883` ("Each Unity row links its ART ticket"); off-sheet ads `ART-826`, `ART-831`; library `ART-793` … `ART-854` team_ART | verified |
| "open ART tickets" | destination | Linear team `team_ART`; Claire's membership `tmem_team_ART_usr_7fe31e7ec8199618` (linear data.json via hg.py) | verified |
| "whoever's making them" | relationship | the ask's owner split ("Martin has the icon and the stills, Marcus has video and end cards"); Linear users `usr_51f5f16d46e8cf55`, `usr_c77c50cc15c5342d` | verified |
| "Leonard's thread" | destination | the ask `C06DJBJL798/1759269913.882683` is a top-level message (thread parent, reply_count 0 at the clock) | verified |
| "before the review" | deadline | `evt_d947bf7cd910549b674b1f` Thu Oct 2 09:00 PT | verified (future event, allowed) |

Absence claims in the prompt: none. Identity checks (`entity.py resolve`): "Leonard" → leonard.hayes@harmonygames.co only (brief §10).

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
| K49-newer-source | ugt_both_fair_figure | not matched | the date fork (draft vs changes mail) is settled by the newer source, as in the case |

## Self-review

Re-read as the eval: `Evals/1_Prompt_Eval.md` Phases 1–3 walked against this report; every C-check has a result below.

| Check | Strongest counter-reading | Resolution (evidence) | Result |
| --- | --- | --- | --- |
| C1 | Could fail: the field rejects very short or long prompts | @@WC@@ words, inside 20–4,000 (`04_Prompt.txt` sha256 @@SHA@@) | clean |
| C2 | Could fail: an assignment field is missing or off-roster | all eight fields in `Working_Files/00_Task_Context.json`; claire_morgan resolves in `Evals/references/persona/roster.json`; freeze 2025-10-01T00:00:00Z | clean |
| C3 | Counter: an art lead would not run a marketing push; better fit is Frederick (UA) | Leonard asks Claire by name for "the art side" (`C06DJBJL798/1759269913.882683`); she leads the makers; a better-fitting colleague alone is not a Fail (Eval 1 §1.1) | clean |
| C4 | Counter: Marketing and GTM is really UA buying, and Authoring is only a Slack post | the work is the seasonal GTM art plan; the plan doc is the authored artifact (brief §1); no spend is asked (kdi.md SC-11/12/23) | clean |
| C5 | Counter: the prompt carries the recipe (it lists six writes) | the writes are the ask's own deliverables; no rule, threshold, date or source is stated (hardness_v2_check RULE_IN_PROMPT CLEAN); levers in brief §8 | clean |
| C6 | Strongest Reading B: Martin's Sep 17 icon is "what we already have" (Reuse, no ticket) | Robert's reply `C08R8CHB0QL/1758127951.679146` settles it (revision 03, PW1); Reuse-ad dates accepted both ways (brief §4b) | clean |
| C7 | Counter: "comment … on its ART ticket" could mean the due-date field; "share" leaves the role open | the ask says "drop a comment"; "so they can comment" pins the permission; channel (thread), time (before the review) and form (doc + sheet) are pinned; no "I'll" beside an agent ask ("I'm walking everyone through it" is a meeting, not a write) | clean |
| C8 | Counter: "his message" is ambiguous or hands over answers | one Halloween ask from Leonard to Claire (`C06DJBJL798/1759269913.882683`, persona_view overlay 1 hit); it names sources and owners, no calls (brief §6) | clean |
| C9 | Counter: "everything that's live today" presupposes the scope; "both links" presupposes two files | scope words are the requester's; the two links are the two requested outputs, not findings; no count, culprit or root cause (brief §9) | clean |
| C10 | Counter: naming "Thursday's review" collapses discovery of the attendee list | the review is the persona's own meeting and the ask names it (§5 row 18 "Yes"); no §5 "No" item is named | clean |
| C11 | Counter: the writes could be done without investigation | each comment and assignment needs its ticket's campaigns, capture and master (§5 rows 13–14) | clean |
| C12 | Counter: one service carries all the weight (Linear) | 11 services carry graded facts (`01_Hardness_Manifest.json` services); dossier HARDNESS GATE (extreme): PASS | clean |
| C13 | Counter: the ticket follow-through is a bolt-on to the plan | every write serves the one push and the review (Finding 1); stacking only | Advisory |
| C14 | Counter: "my Drive", "ART ticket" name tools | product names, no tool or parameter and no search hit (`linear_`, `gmail_`, `slack_`, `MCP`, `tool`: none; `common_errors.md` §3; `Working_Files/research/prompt/catalog.md` §8) | clean |
| C15 | Counter: the writes are a sequenced command list, or a First / Then / Finally search hit (`Evals/references/rules/common_errors.md` §3: "A hit fails") | the text has no First / Then / Finally (draft v1's "Then" was removed after the GPT deep recheck finding DR1, `Working_Files/prompt_eval/`); the order is deliverables and who to tell, with no source order or method (Eval 1 §1.3.1) | clean |
| C16 | Counter: an enumerated list of writes reads as a spec sheet | one sentence of plain asks with no column, format or wording rule; 0 of 4 spec-sheet triggers; no hint, riddle, hedge, audit form or if-chain (case control-plain-request) | clean |
| C17 | Counter: "I'm walking everyone through it" or "yesterday" is false | `evt_d947bf7cd910549b674b1f` description; ask 2025-09-30T22:05:13Z; every tight identifier in the verification log above | clean |
| C18 | Counter: "so they can comment" needs a commenter role the catalog may not take | `gdrive_share_file` role is a free string; writer is accepted (brief §4b); every other write is declared (catalog.md §1–6) | clean (evidence limit: the commenter value itself) |
| C19 | Counter: a required read is in someone else's mailbox or calendar | Claire's own copies of both mails and the event; check-sql PASS (0 load-bearing rows not visible); base records can-see YES (brief §5a) | clean |
| C20 | Counter: relative dates fail | Eval 1 §2.8 local override: relative wording never fails; both resolve to one day (Findings 2–3) | Advisory |
| C21 | Counter: friction is announced | `03_Error_Async_Config.txt` Friction: none; nothing announced | clean |
| C22 | Counter: a touched record is incoherent (the new revision-03 rows) | base_check PASS (217 inserts, 2 updates), the parent's reply counters bumped (SQL L22), injection gate PASS; independent red team rounds on the earlier rows (dossier §12) | clean |
| C23 | Counter: the scenario repeats a sibling (Claire's object hand-off, Vincent's release gate) | different scenario (seasonal store + UA art), entities, asks (comments + assignments on 58 tickets) and writes; fingerprint ≤ 2 of 7 against `Task_Authoring/task_inputsH/04_Prompt.txt` (persona, shape); no supplied samples (Eval 1 §2.9) | Advisory |
| C24 | Counter: investigate + one Slack post | a doc, a sheet, 58 comments, 48 assignments, new tickets and a thread reply (brief §4) | clean |

Mechanics: every quoted span above was verified as an exact substring of `04_Prompt.txt` by the gate; the prompt hash is identical before and after this check (sha256 @@SHA@@).

Unresolved: none. Evidence limits: the `gdrive_share_file` commenter value and Linear assignee-by-email form are declared but not exercised (writer and ids are the declared-safe forms).

## Route

No Fail: paste `04_Prompt.txt` exactly as saved into `/prompt`, paired with `/injection` (SQL sha256 @@SQL@@), answering the task date with Oct 1, 2025 (synth-cut). An independent GPT red-team emulation of `/prompt` runs first (`Working_Files/prompt_eval/`); act on its findings before the platform run. Next: `/create-humantime`.

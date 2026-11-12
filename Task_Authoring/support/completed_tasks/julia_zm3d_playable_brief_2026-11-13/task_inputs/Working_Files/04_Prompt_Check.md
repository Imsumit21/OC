# Prompt Check — julia_zm3d_playable_brief
> Prompt: 04_Prompt.txt · 46 words · sha256 33c721d60945 · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · checked 2026-11-12 against 04_Prompt_Writing_Brief.md (2026-11-12) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## Summary

- Fail: 0 · Non-fail: 0 · Advisory: 1 (C23, no supplied samples) · UNVERIFIED checks: none
- Checks clean: C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, C24
- Predicted /prompt band: PASS
- Status: READY FOR /prompt

The prompt, as it will be submitted:

> I need a hand with Frederick's playable message from yesterday. Can you do everything he's asking for in it, start to finish? The files he wants should end up in my Drive, and once they're ready the links go in the PlayableX channel like he says.

## Findings

No Fail and no Non-fail finding. One advisory note:

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C23 | Originality · Advisory | "Frederick's playable message" | Eval 1 §2.9 is N/A without supplied samples; fingerprint against the guideline and taxonomy examples only | none found: no guideline, taxonomy or long-horizon example has a vendor brief with an asset hand-off list; noted so the reviewer knows no sample was supplied with the task |

## Fair readings (accepted outcomes)

Per deliverable: Reading A (best supported) · Reading B (the strongest alternative) · what settles it.

| Deliverable | Reading A | Reading B | Resolution and evidence |
|---|---|---|---|
| The job itself | do what Frederick's message asks: write the brief and the hand-off list, follow his notes for the states and the tickets, share, send him the counts, post the links | report back what Frederick wants and wait | the request is 'do everything he's asking for in it, start to finish'; his message is an instruction to produce two files and two messages (D05SD5QLG94/1759256494.852159). One reading |
| W1 brief | the eight with the bow, the four zombies and walk, 7 slots, lost at zero health, the two library sounds held back, music after the first click, 3 November | the eight with the dynamite; or the reference level's items | Robert's own later reply C08R8CHB0QL/1758922879.243189 replaces the last item of his list C090N54TG79/1758823946.262829; the ask keeps his latest word. Settled by a newer source on the same issue |
| W2 hand-off list | 96 rows; Delivered 8, Ready 39, Owed 49 | Brian's notes taken as they stand: 8 / 73 / 15 | the notes f_8c1d0bca1d1d5fde4c5008 say a later word from someone who knows the file or the art counts; the later statements are C0880U9751A/1758906517.912099, D05GU6L0XFH/1759178332.042459, harmonygames-Games/match3d#462, f_b2387e31d46d3a7b3fa2a9, f_faf4d7c167d14a1127dcc3, each readable by Julia. Settled by an incorporated source's authority |
| W3 shares | both files, view only, to frederick.stone@harmonygames.co, brian.foster@harmonygames.co, robert@harmonygames.co and intake@playablex.ai | the brief only; or Leonard, whose Trello card is the 'kickoff' | the notes: 'Sharing: both files, view only. Everyone on the kickoff hold, and PlayableX through their intake address' (evt_421695d009e589ee85296c, d7d31caf63ee33db2b7ed271); the card has no attendees (688c4d14c312a27fa2747e40) |
| W4 tickets | the 49 Owed lines' tickets to Todo with a comment each; the others untouched | nothing for a line whose note already says not exported; or a description edit | the notes: 'An Owed line's ticket goes to Todo with a comment saying what is owed and who has it. Leave the Delivered and Ready ones as they are.' (f_8c1d0bca1d1d5fde4c5008) |
| W5 counts | the three numbers in Frederick's DM D05SD5QLG94 | the numbers in the vendor channel | his message: 'give me the count for each state here' (D05SD5QLG94/1759256494.852159); a new message or a reply under his ask is the same write to the same person |
| W6 links | both links in C08H78VJG80 | the links in Frederick's DM | his message: 'post both links in the PlayableX channel'; the prompt repeats it. A top-level post or a reply in the 3 November thread is the same channel and content (sweep fork F10, accepted) |

No material fork is open: `COHERENCE SWEEP (full): PASS` on this prompt and SQL (pasted in the Self-review).

## Verification log

Every proper noun, relationship, state premise and narrative claim of the prompt, looked up in this run.

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| "Frederick's playable message" | person / event | D05SD5QLG94/1759256494.852159, sender `EMPLOYEE_0008_SLACK_ID` (frederick.stone@harmonygames.co), in Julia's DM with him D05SD5QLG94; the only message of that DM after 18 Sep | true: the message exists, is his, and is about the playable ('write the brief they build from, and tell me where the item pack actually stands') |
| "from yesterday" | date | D05SD5QLG94/1759256494.852159: ts 1759256494.852159 = 2025-09-30 18:21:34 UTC = Tue Sep 30, 11:21 AM PT; Julia's today is Wed Oct 1, 2025 | true on both calendars (Tue Sep 30) |
| "everything he's asking for in it" | state premise | D05SD5QLG94/1759256494.852159 asks for the brief, the list, the counts and the links, and names his notes f_8c1d0bca1d1d5fde4c5008 for 'what goes in the brief, what counts as ready, what to do with the tickets and who gets the files' | true: the message carries requests; a requested new output, not a premise about the world |
| "The files he wants" | doc | D05SD5QLG94/1759256494.852159: 'Brief as a doc and the hand-off list as a sheet' | true: he asks for files |
| "my Drive" | doc / place | d_8140f09bf9f1b94cb8ee2d (Julia's Drive root, owner julia.lawson@harmonygames.co); D05SD5QLG94/1759256494.852159: 'both in your Drive' | true: the place exists and is hers; it is where he asked for them |
| "the PlayableX channel" | channel | C08H78VJG80 (private, name ends in '-playablex', Julia is a member); C08H78VJG80/1759226395.551469 is in it | true: one channel carries the vendor's name |
| "like he says" | relationship | D05SD5QLG94/1759256494.852159: 'post both links in the PlayableX channel so they know what's still coming from us' | true: the message says so |

`persona_view.py can-see` for the three named places:

```
julia_lawson slack D05SD5QLG94: YES
  reason:   persona EMPLOYEE_0005_SLACK_ID is in members of im D05SD5QLG94
  evidence: channel=D05SD5QLG94, name=D05SD5QLG94, kind=im, members=5, persona_slack_id=EMPLOYEE_0005_SLACK_ID
julia_lawson slack C08H78VJG80: YES
  reason:   persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
  evidence: channel=C08H78VJG80, name=[SOURCE_ORG_0001]-playablex, kind=private, members=19, persona_slack_id=EMPLOYEE_0005_SLACK_ID
julia_lawson gdrive d_8140f09bf9f1b94cb8ee2d: YES
  reason:   persona owns the file
  evidence: file=d_8140f09bf9f1b94cb8ee2d, name=julia.lawson@harmonygames.co, mime=application/vnd.google-apps.folder, owner=julia.lawson@harmonygames.co, shared_with=0, visibility=private
```

## Brief coverage

| Brief item (§4 deliverables, §6 triggers) | Present in the prompt (quoted span, or "absent") |
|---|---|
| Anchor A1: Frederick's message is the job | "I need a hand with Frederick's playable message from yesterday" |
| R1 to R6 through the hub (list, states, what is owed, the board, the brief, the tickets) | "Can you do everything he's asking for in it, start to finish?" |
| W1 brief and W2 hand-off list: destination (anchor A3) | "The files he wants should end up in my Drive" |
| W6 links: destination (anchor A2) | "the links go in the PlayableX channel like he says" |
| W3 shares | "everything he's asking for in it" (through his notes; not named, by design) |
| W4 ticket follow-through | "everything he's asking for in it" (through his notes; not named, by design) |
| W5 counts to Frederick | "everything he's asking for in it" (his message says where; not repeated) |
| §9 must-not-appear items | absent: no tool name, id, title, state word, count, item, person other than Frederick, source list or step order |

## Self-review

Walked `Evals/1_Prompt_Eval.md` Phases 1 to 3 against the prompt text. One row per check: the result, the best case against it, and what resolves it.

| Check | Result | Counter-reading (best case against the result) | Evidence that resolves it |
|---|---|---|---|
| C1 | clean: 46 words | A request this short could be under the field's floor. | the field takes 20 to 4,000 words; whitespace count of 04_Prompt.txt is 46 (sha256 33c721d60945) |
| C2 | clean | An assigned field could be missing or changed. | `Working_Files/00_Task_Context.json` holds all eight fields, context_hash 3246c54345b9; persona resolves to julia.lawson@harmonygames.co |
| C3 | clean | A Product Manager would not write a vendor's creative brief; a marketer would. | she wrote the storyboard and brief for the first playable in this vendor's channel (C08H78VJG80/1741963515.221549) and built this one's reference level (D076RBM29JS/1758638743.317009); Frederick asks her by name (D05SD5QLG94/1759256494.852159) |
| C4 | clean | The work is asset tracking (Engineering Ops), not Marketing and GTM, and Authoring is incidental. | the object is a playable ad, a user-acquisition creative chosen to filter for players who will like the game (C08H78VJG80/1757695108.506159); the two authored files are the deliverables (f_8c1d0bca1d1d5fde4c5008: 'The brief. One doc PlayableX can build from') |
| C5 | clean | The prompt restates where the files and the links go, details that live in Frederick's message. | both are destinations the persona knows (playbook: name them); no column, state, rule or source is restated. Dynamic change and multi-source are load-bearing in the records (C0880U9751A/1758906517.912099, D05GU6L0XFH/1759178332.042459, C08R8CHB0QL/1758922879.243189, f_faf4d7c167d14a1127dcc3, f_b2387e31d46d3a7b3fa2a9) |
| C6 | clean | Reading B (Brian's notes as they stand) is a fair outcome that would be rejected. | the incorporated notes say a later word counts (f_8c1d0bca1d1d5fde4c5008); every later statement is in a record Julia can open; both cold reviewers reach 8 / 39 / 49 (`Working_Files/01d_Coherence_Sweep.json`) |
| C7 | clean | Whether the links are a top-level post or a thread reply, and whether the counts are a message or a reply, is left open: a Minor clarity finding. | the conversation and the recipients are fixed (C08H78VJG80, D05SD5QLG94) and the write is the same message in the same place; position inside one conversation is not a channel, time or form choice. Accepted either way in brief §4b and in the sweep (fork F10). No 'I'll' statement in the prompt |
| C8 | clean | The prompt points at a message that points at notes: the rule source is two hops away and unnamed. | (a) D05SD5QLG94/1759256494.852159 is readable (DM member) and f_8c1d0bca1d1d5fde4c5008 is shared with her; (b) one message of that DM is about the playable; (c) it says what the prompt attributes to it ('both in your Drive', 'post both links in the PlayableX channel'); (d) it gives instructions, not answers |
| C9 | clean | Naming the files and the links hands over part of the answer. | they are the requested outputs, stated by Frederick (D05SD5QLG94/1759256494.852159); no state, count, line, item or reason appears in the prompt |
| C10 | clean | 'Frederick's playable message' names the hub exactly, collapsing discovery. | the hub is an anchor the persona knows (dossier anchor table, A1); the hidden authorities (f_8c1d0bca1d1d5fde4c5008, f_956e60ec7f2f7977d98934, evt_421695d009e589ee85296c) and the six deciding records are not named |
| C11 | clean | The writes could be made without investigating. | the list's states, the comments and the brief's facts all depend on the tickets' notes and the later statements (DES-313; DES-314 to DES-409) |
| C12 | clean | Only Slack and Linear carry weight. | Docs, Sheets, Slides, Calendar, Contacts, GitHub and Confluence each hold a fact a graded row needs (f_8c1d0bca1d1d5fde4c5008, f_956e60ec7f2f7977d98934, f_b2387e31d46d3a7b3fa2a9, evt_421695d009e589ee85296c, d7d31caf63ee33db2b7ed271, harmonygames-Games/match3d#462, page_zm3d_gdd); `HARDNESS GATE (extreme): PASS` is pasted in the dossier |
| C13 | clean | Three sentences could be three unrelated asks. | all three serve one hand-over: the message, its files, its links (D05SD5QLG94/1759256494.852159); deleting any sentence removes the job or a destination |
| C14 | clean | 'my Drive' and 'the PlayableX channel' are tool mentions. | natural product and place names (`prompt_qc_examples.md` row 103); no function, parameter or server name appears; checked against `Evals/references/tools/catalog.json` names used in brief §9 |
| C15 | clean | 'once they're ready the links go in ...' is a sequenced step list. | it is the order of deliverables Frederick gave (D05SD5QLG94/1759256494.852159: 'Then ... post both links'), one clause, not a method of two or more investigation steps |
| C16 | clean | 'start to finish' hints that there is more than meets the eye. | it asks for the whole of what the message requests, which includes messages and tickets (D05SD5QLG94/1759256494.852159); it points at no trap, record or cause. Calibration cases below: no failing rule matched |
| C17 | clean | 'from yesterday' or 'the PlayableX channel' could be a near-match phantom. | the ask is stamped 2025-09-30 18:21 UTC, Tue Sep 30 on both calendars (D05SD5QLG94/1759256494.852159); the channel C08H78VJG80 is the only one named for the vendor and she is a member (can-see YES above) |
| C18 | clean | Sharing with an outside address or moving a Design-team ticket may be beyond the tools. | gdrive_share_file takes an e-mail and a role; linear_update_issue sets a state name, and Todo is in use in that team (`DES-312`); gdocs_create_document, gsheets_create_spreadsheet, gsheets_values_update, linear_create_comment and slack_send_message exist in the catalog (manifest `writes`) |
| C19 | clean | A deciding record could be outside her scoped view. | check-sql PASS for every load-bearing seeded row (dossier 1.E): C0880U9751A/1758906517.912099, D05GU6L0XFH/1759178332.042459, C08R8CHB0QL/1758922879.243189, f_b2387e31d46d3a7b3fa2a9, f_faf4d7c167d14a1127dcc3; no ask directs her to anyone else's scoped data |
| C20 | clean | 'yesterday' could resolve to two windows. | Tue Sep 30, 2025 in Pacific and in UTC (D05SD5QLG94/1759256494.852159); the only later date in the records is the 3 Nov kickoff, a scheduled event (evt_421695d009e589ee85296c) |
| C21 | clean | A wait or an error could be announced or missing its alternate path. | none is configured: `03_Error_Async_Config.txt` Friction: none, gate PASS |
| C22 | clean | An inconsistency between records the prompt touches was met. | none met in C17 or C18; `BASE CHECK` PASS, citation chronology PASS (26 pairs) and the sweep's 15 seeded facts checked against the base (D05SD5QLG94/1759256494.852159, f_8c1d0bca1d1d5fde4c5008). The platform /injection review is the user's to run |
| C23 | advisory | A supplied sample could match on persona and scenario. | no sample was supplied with the task; no guideline or `long_horizon.md` example is a vendor brief with a hand-off list (D05SD5QLG94/1759256494.852159) |
| C24 | clean | The task is 'investigate and post one Slack message'. | two authored files, 49 ticket moves and comments, eight shares and two messages (manifest `writes`; call budget 252; DES-314 to DES-409) |

Calibration self-test against the 15 cases of `Evals/references/rules/prompt_qc_cases.json` (matched means the prompt shows the case's failing pattern):

| Case | Rule | Case verdict | This prompt |
|---|---|---|---|
| K11-staged-errors | staged_errors | FAIL | not matched: clean spelling, capitals and punctuation |
| K11-control-spelled-correctly | staged_errors | PASS | not matched: clean spelling, capitals and punctuation |
| K31-trap-hint | trap_hint_or_riddle | FAIL | not matched: names the job, no hint at a cause |
| control-symptom | trap_hint_or_riddle | PASS | not matched: names the job, no hint at a cause |
| K42-hidden-destination | hidden_destination | FAIL | not matched: both destinations the persona knows are named |
| K47-hidden-destination | hidden_destination | FAIL | not matched: both destinations the persona knows are named |
| K44-hidden-destination | hidden_destination | FAIL | not matched: both destinations the persona knows are named |
| control-named-destination | hidden_destination | PASS | not matched: both destinations the persona knows are named |
| K1-audit-form | audit_form | FAIL | not matched: one plain request, no catalogue of verbs |
| K43-audit-form | audit_form | FAIL | not matched: one plain request, no catalogue of verbs |
| K44-if-chain | if_chain | FAIL | not matched: no condition |
| control-plain-request | audit_form | PASS | not matched: one plain request, no catalogue of verbs |
| K43-departed-person-premise | false_state_premise | FAIL | not matched: Frederick is active and messaged her on 30 Sep |
| K50-both-fair-figure | ugt_both_fair_figure | PASS | not matched: no unsettled figure |
| K49-newer-source | ugt_both_fair_figure | PASS | not matched: no unsettled figure |

Mechanics: every quoted span above was asserted as an exact substring of 04_Prompt.txt by the generator; the file's sha256 is 33c721d609452a3672e18829856370ac2810ce87ffdcdde3e38f599a19a1d28e before and after this run. Facts re-verified in this run: the ask's text and time (SQL row), the three places (can-see), the rule-in-prompt check:

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md
  CLEAN      SAME_PLACE      5 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 3 requirements: {'R2': ['EXPORT', 'REVISED', 'AUDIO'], 'R3': ['ARTHOLD', 'ZIP'], 'R4': ['PICKS']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   6 of 6 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Coherence sweep on this prompt and SQL:

```
COHERENCE SWEEP (full): PASS
[PASS] sweep.bound: bound to 01_Universe_Inject.sql 7d1f2aaeb29c and 04_Prompt.txt 33c721d60945
[PASS] sweep.reviewers: 2 reviewers, each with a model, a brief hash that matches its kept brief, and a findings file
[PASS] sweep.findings: all 78 reviewer finding(s) are taken up or dismissed
[PASS] sweep.forks: 30 fork(s): 28 settled_in_data, 2 both_fair; no material fork is open
[PASS] sweep.prompt_sentences: no fork was settled by adding a prompt sentence
[PASS] sweep.open_sets: 1 quantifier span(s) in the prompt, each with a rule and a census; 43 open set(s) recorded
[PASS] sweep.siblings: 0 defect(s), each closed and with its sibling list
[PASS] sweep.base: 17 seeded fact(s) checked against the base, every conflicting hit dispositioned
[PASS] sweep.known_issues: 3 known-issue card(s) touched, each with a disposition
[PASS] sweep.conflicts: 0 value conflict candidate(s), each with a disposition
```

Unresolved: none. UNVERIFIED: none. The first measurement of difficulty is the pre-check run.

```
STAGE GATE prompt-check: PASS — Task_Authoring/task_inputs · 04_Prompt_Check.md#122488ae4ff9 · 04_Prompt.txt#33c721d60945 · 04_Prompt_Writing_Brief.md#d732d0390c8d · __context__#3246c54345b9 · __assignment__#70579cebc8fc · __policy__#dc4ab5df3cdd · __gate_policy__#1747d7aa5ab8 · __review__#f555a5b9a0f7 · blocking 0 · warnings 1 · checks 30
[PASS] assignment.v3_context: Julia Lawson / Product Manager; hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#d732d0390c8d, 00_Assigments.md#82494197a841, 01_Grounding_Dossier.md#796862c5b768, 01_Universe_Inject.sql#7d1f2aaeb29c, 03_Error_Async_Config.txt#9aac307a32ee, 01a_Hardening_Report.md#35998ca41fd6, __context__#3246c54345b9, __assignment__#70579cebc8fc, __policy__#dc4ab5df3cdd, __gate_policy__#1747d7aa5ab8, __review__#bacc5ee38680)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (46 words, sha256 33c721d60945)
[PASS] evidence.quoted_spans: 1 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 7 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 7/7 items carry a source pointer (min 100%)
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
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] readiness.hardness_review: current evidenced review; deferred: []
[WARN] task.folder: the task folder is the bare default `task_inputs`: give each task its own folder (`Task_Authoring/task_inputs<Label>`) and pass it to every command, so two tasks never share one [first-pass check in warn mode: reported, not blocking]
[PASS] sweep.forks: fork sweep PASS on the current SQL and prompt: no open material fork, every open set has a rule and a census
[PASS] prompt.assignment_fit: no open C4 finding: the work fits the assigned competency and task skill
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## Route

No Fail. Paste `04_Prompt.txt` exactly as saved into `/prompt`, paired with `/injection` on `01_Universe_Inject.sql`; when asked for the task date, answer Oct 1, 2025 (synth-cut). `03_Error_Async_Config.txt` is not supplied (Friction: none). Next: `/create-humantime`.

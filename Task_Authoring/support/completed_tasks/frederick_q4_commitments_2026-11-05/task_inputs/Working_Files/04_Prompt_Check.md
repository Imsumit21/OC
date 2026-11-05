# Prompt Check — frederick_q4_commitments
> Prompt: 04_Prompt.txt · 98 words · sha256 32f7ab0cabd6 · checked 2026-11-04 against 04_Prompt_Writing_Brief.md (2026-11-04, #07b5ded14cc0; re-checked on rev4) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Inputs: 00_Assigments.md, Working_Files/00_Task_Context.json (context db8af19cc1c3), 01_Universe_Inject.sql rev4 (69603ab4b6a4; local injection gate PASS; platform /injection pending; rev3 2176eb708f74 passed /injection and /prompt Score 5), 01_Grounding_Dossier.md, 03_Error_Async_Config.txt (Friction: none), 04_Prompt_Writing_Brief.md. No 02_Reference_Files_Manifest.md (no attachments).

Brief sync in this run: the drafted prompt asks for the January reminders "one per company", so brief §4b D6 was narrowed from "one event per company or one listing event" to one event per company (plan/assemble_brief.py regenerated the brief; `stage_gate.py prompt-writing` re-run: PASS, 0 warnings; outcome_reviews.prompt-writing rebound to #775fc1acdcc5). No other brief value changed. Rev4 re-check (2026-11-04): the prompt is unchanged (32f7ab0cabd6); rev4 moves four corrections and one member (01a_Hardening_Report.md §10) and the rev4 blind sweep's fixes make Clipforge's written answer to Priya required (brief §4b D2) and exclude a Nintendo portal contact (D5); every finding below still holds.

## Summary

- Fail 0 · Non-fail 1 (C7, two Minor open non-action details) · Advisory 3 open (C23, C6 later-stage, C18) + 1 resolved in rev4 (C22) · UNVERIFIED 0 hard gates
- Checks clean: C1, C2, C3, C4, C5, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C24
- Predicted /prompt band: NON-FAIL by the local formula (one Non-fail at C7). Both C7 items are non-action details under Eval 1 §2.6 (the same write actions under every reading), so the §2.6 PASS band ('little to no room for misinterpretation of the specific request') may still apply.
- Status: READY FOR /prompt

## Findings

| # | Check | Dimension | Severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|---|
| 1 | C7 | Clarity | Non-fail (Minor) | "put a reminder on my calendar for that day" | Playbook C7: an open time or form listed as representational in §4b is a Minor finding; Eval 1 §2.6 NON-FAIL band | The time of day of each reminder is open (brief §4b D6: 'any time that day'). It is a non-action detail: every reading makes the same 14 events on Mon Jan 5, 2026. Hard gate 4 forbids prescribing an exact time for a date-only request, so no rewording is suggested. |
| 2 | C7 | Clarity | Non-fail (Minor) | "going by his email for what needs doing" | Playbook C7 (channel to the same recipient); Eval 1 §2.6 example 'email vs. Slack DM to the same person' | Leonard's email asks for 'a written answer'. A reply on the company's thread and a new email to the same person are both fair (brief §4b D2 equivalence class). Same recipient, same channel family, same content. Pinning 'reply on each thread' would conflict with the Paylane notice ('write to billing@paylane.io', frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io>), so no rewording is suggested. |
| 3 | C23 | Originality | Advisory | "Leonard's email yesterday puts the vendor and partner backlog on me this week." | Eval 1 §2.9 (no samples supplied with this task); platform STEP 0.6 dataset duplicate (memory: prompt-dataset-duplicate-gate) | The job differs from the library neighbours known locally (Leonard hands Fred the investor list before LA; the bridge-round Q4 investor update send list). But the shape is the same: a hand-off through Leonard's email, a Q4 folder, a Trello board, a reply on his email. The draft was reworded away from the archived bridge prompt (support/completed_tasks/frederick_bridge_pipeline_2026-11-03/task_inputs/04_Prompt.txt). hg_similarity.py is not in the local Evals copy, so the meaning score cannot be measured before /prompt. |
| 4 | C22 | Cross-Service Coherence | Advisory (resolved in rev4) | — | Eval 1 §3.2; platform /injection rev3 C-adv 3 (run_forensics/rev3/platform_injection_review.md) | Lumencloud's email opens 'Thanks for applying…' (frederick.stone@harmonygames.co/1842991438234544282), while its agreement doc ends 'Apply by Oct 31, 2025' (f_a227b14f03e12005fe8324). The /injection reviewer called it 'not a contradiction'. A /prompt deep re-check reads both, and could still score it as one minor inconsistency (Non-fail 4). Rev4 makes the agreement say 'Sign by Oct 31, 2025 (cohort closes)' (no truth value changes), so the wrinkle is gone. |
| 5 | C6 | Unique Ground Truth (later stage) | Advisory | — | Brief §4b equivalence classes; tools/surface_grader.py spot-decode (this run) | The local surface grader is stricter than §4b in four places: D2 needs reply_all set to false (§4b accepts reply-all); D1 needs a share call on the log (no record asks to share it); Next date compares ISO only ('Oct 15, 2025' fails); the told regexes X13, C5 and C11 miss 'said no' and 'passed on' (§4b: 'declined / said no'). Route: /create-rubric-writing must accept the §4b classes. Design-2 fixed the first and the last two (issue_key comparators, wider told patterns); D1/D2 stay tool behaviours at weight 1. The surface only affects local forecasts and forensics, not /prompt. |
| 6 | C18 | Feasibility (later stage) | Advisory | "one per company" | Brief §4 D6; catalog gcal_create_event | One reminder per company is 14 single-event writes, all feasible (gcal_create_event on frederick.stone@harmonygames.co). It also adds about 13 counted calls toward the requester's more-than-130-per-run target. Noted so /create-humantime and the rubric count 14 events, not one. |

## Fair readings

| Deliverable | Reading A (best supported) | Reading B (strongest alternative) | Resolution and evidence |
|---|---|---|---|
| D1 log | A native sheet named like 'Q4 commitments log' in my Q4 commitments folder, the README's header, one row per in-scope company | A Doc or a tab added to the template sheet | Settled by source identity: the hub frederick.stone@harmonygames.co/<CAlIXcq3nWlSRBAZONcbY9d2v0ggkPYER8WfaoZa@mail.gmail.com> 'Log it all in a sheet in the Q4 commitments folder'; README f_846ddc38b2aab3d2ed3fcb 'One sheet … Name it "Q4 commitments log"; to start, copy the header row from the template sheet' |
| D1 membership | The 36 companies in brief §4b | Add PlayableX / Craftsman+, or drop Balancy and Nintendo | Settled in rev3 records: the hub names PlayableX and Craftsman+ with the ad networks; Balancy was engaged and answered later (frederick.stone@harmonygames.co/1840501641217286806); Nintendo's terms wait on an officer (cmt_c9a6660d81e067ad1de7). The second blind sweep (plan/blind_fork_sweep_rev3.md) produced the same 36 |
| D2 answers | A written answer to each of the 31 companies still waiting, matching its decision | An answer to every company, including the four already answered | Settled by incorporated authority: guardrails f_b98287f6f80fe431a71209 step 1 'don't write to them again'; 'Portals and no-reply notices don't need one' |
| D2 channel | A reply on each company's thread (Clipforge to billing@paylane.io) | A new email to the same person | Both fair (same recipient and content; §4b D2). Reported as Minor under C7 |
| D3 cards | One card per Sign row on the To Do list of our Harmony Games board, company name in the title, ESG ones included | Cards on another board, or no card for terms acceptance (Nintendo, Markward) | Settled: the prompt names 'our Harmony Games board' (Trello board 640643a3fd8f3ca308d9318e); Leonard's reply frederick.stone@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com> 'To Do list … including the ones that go to ESG'; ESG's note covers 'click-through terms and portal NDAs', and the hub calls the whole group 'Anything that needs signing' |
| D4 ESG intake | One email per agreement ESG must review (Kinetic Arcade, Lumencloud, Bundlehouse) to ESG Law intake with the checklist items | One combined email | Settled: ESG's note 'one email per agreement' (frederick.stone@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com>); checklist f_3b06917a41dd59308d890b |
| D5 contacts | A contact for each company's person not already in Contacts, company in the job field | A contact for every company | Settled: README f_846ddc38b2aab3d2ed3fcb 'only add someone who isn't in Contacts already' |
| D6 reminders | One event per company on Mon Jan 5, 2026 for the 12 parked rows and the 2 'later' answers (14) | One listing event; or parked rows only | Settled: the prompt 'one per company'; guardrails step 1 sends 'later' answers to the same review, and the README's Next date gives 'for Park and for "later" answers, the January review'; the date is evt_fd469c29811879519c2c96 |
| D7 report | A reply on Leonard's email with what we keep and what waits on a signature | A new email, or a Slack message | Settled: the prompt 'reply to Leonard on his email'; the hub 'reply here with what we're keeping and what's waiting on Arthur or me to sign'. Reply and reply-all reach only Leonard (the hub has no cc) |
| Who acts | The agent does every write for Frederick | Frederick writes some himself | Settled: no 'I'll' statement in the prompt; every ask is addressed to the agent ('Can you work through all of it') |

No reported figure stays unsettled (no BOTH_FAIR_FIGURE).

## Verification log

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| "Leonard" | person | roster leonard_hayes, leonard.hayes@harmonygames.co (Evals/references/persona/roster.json); Contacts /contacts/169 (hg.py search contacts 'Leonard') | match; active at the clock (his seeded email 2025-09-30T23:20Z, base #executives C07C2866011/1758739727.864319) |
| "Leonard's email yesterday" | event / date | frederick.stone@harmonygames.co/1844732913254784171, sent 2025-09-30T23:20:00Z = Tue Sep 30, 4:20 PM PT, To Frederick only | match: yesterday for persona_today Wed Oct 1, 2025. hg.py search of Frederick's 1844* threads shows his only other Sep 26–30 mails are TestFlight notices (frederick.stone@harmonygames.co/1844718211624259514, frederick.stone@harmonygames.co/1844370463220152624) |
| "vendor and partner backlog" | narrative | hub frederick.stone@harmonygames.co/<CAlIXcq3nWlSRBAZONcbY9d2v0ggkPYER8WfaoZa@mail.gmail.com>: 'can you take over the vendor and partner backlog this week?' | match |
| "this week" | date | the same hub frederick.stone@harmonygames.co/1844732913254784171: 'a written answer this week' (Mon Sep 29 – Sun Oct 5, 2025) | match |
| "how we decide each one" | narrative | the same hub: 'Go by the runway guardrails doc for what we do with each one' → f_b98287f6f80fe431a71209 | match |
| "my Q4 commitments folder" | doc / state | d_80a8c04753ba82ba4ba6a5 'Q4 commitments', owner frederick.stone@harmonygames.co, shared with leonard.hayes@harmonygames.co, created 2025-09-29T20:00Z (SQL) | match; persona_view check-sql YES |
| "The log" | doc | README f_846ddc38b2aab3d2ed3fcb: 'Name it "Q4 commitments log"' | match (new output, not a premise) |
| "the cards for anything that needs signing" | narrative | Leonard's reply frederick.stone@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com> (cards on the To Do list); hub 'Anything that needs signing goes the way ESG's note about signing says' | match |
| "our Harmony Games board" | entity | Trello /boards/1 id 640643a3fd8f3ca308d9318e, name 'Harmony Games', closed false (hg.py search get trello /boards/1) | match; unscoped |
| "the January review" | event / date | evt_fd469c29811879519c2c96 'Q4 commitments review', Mon Jan 5, 2026 17:00Z (9:00 AM PT), on calendar frederick.stone@harmonygames.co; guardrails f_b98287f6f80fe431a71209 'the January commitments review' | match; a future scheduled event, not described as done |
| "anything that comes back" | narrative | guardrails f_b98287f6f80fe431a71209 steps 1 and 5 ('it comes back at the January commitments review') | match |
| "my calendar" | entity | gcal /calendars/10 calendar_id frederick.stone@harmonygames.co (hg.py search gcal) | match |
| "reply to Leonard on his email" | narrative | hub frederick.stone@harmonygames.co/1844732913254784171: 'Then reply here with what we're keeping and what's waiting on Arthur or me to sign' | match |
| persona reach of every anchor | ACL | persona_view check-sql frederick_stone 01_Universe_Inject.sql --load-bearing on frederick.stone@harmonygames.co/1844732913254784171, frederick.stone@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com>, f_b98287f6f80fe431a71209, f_846ddc38b2aab3d2ed3fcb, d_80a8c04753ba82ba4ba6a5, evt_fd469c29811879519c2c96: verdict PASS, 0 load-bearing rows not visible | YES |

## Brief coverage

| Brief item | Present in the prompt |
|---|---|
| A1 Leonard's vendor and partner email (§6) | "Leonard's email yesterday puts the vendor and partner backlog on me this week." |
| A2 my Q4 commitments folder (§6) | "The log goes in my Q4 commitments folder" |
| A3 the Harmony Games board (§6) | "the cards for anything that needs signing go on our Harmony Games board" |
| A4 the January review (§6) | "For anything that comes back at the January review" |
| D1 log sheet | "The log goes in my Q4 commitments folder" |
| D2 written answers | absent by design: incorporated through Leonard's email ("going by his email for what needs doing") |
| D3 signature cards | "the cards for anything that needs signing" |
| D4 ESG intake emails | absent by design: incorporated through Leonard's email → ESG's note (R6) |
| D5 contacts | absent by design: incorporated through Leonard's email (R8) |
| D6 January reminders (R7 trigger) | "put a reminder on my calendar for that day, one per company" |
| D7 report to Leonard (R10) | "reply to Leonard on his email with what he asked for" |
| R1–R5, R8, R9 rules | absent by design (§9: the rules stay in the records); incorporated by "going by his email for what needs doing and how we decide each one" |
| §9 must-not-appear | none present: no company, decision, count, date, amount, id, tool name, rule text, LA framing or list layout; hardness_v2_check RULE_IN_PROMPT CLEAN; no run of 6 words matches any seeded text |
| §11 word count 20–4,000 | 98 words |

## Calibration self-test (Evals/references/rules/prompt_qc_cases.json)

| Case | Rule | Matched? | Why |
|---|---|---|---|
| K11-staged-errors | staged_errors | not matched | clean spelling and punctuation, no emoji |
| K11-control-spelled-correctly | control | matched (PASS pattern) | ordinary correctly spelled request |
| K31-trap-hint | trap_hint_or_riddle | not matched | no line points at a hidden problem; no 'nagging feeling' or 'doesn't survive' wording |
| control-symptom | control | matched (PASS pattern) | states the job, not the cause |
| K42-hidden-destination | hidden_destination | not matched | every destination is named: my Q4 commitments folder, our Harmony Games board, my calendar, Leonard's email |
| K47-hidden-destination | hidden_destination | not matched | the reply target is named ('on his email') |
| K44-hidden-destination | hidden_destination | not matched | no 'answer him there too': every company answer goes where its own thread, paper or notice says (guardrails step 2) |
| control-named-destination | control | matched (PASS pattern) | destinations are named |
| K1-audit-form | audit_form | not matched | no 'reconcile / classify / complete the review artifacts' catalogue |
| K43-audit-form | audit_form | not matched | same |
| K44-if-chain | if_chain | not matched | one scoping phrase ('For anything that comes back at the January review'), no if / but-not / then-also chain |
| control-plain-request | control | matched (PASS pattern) | 'going by his email' mirrors 'Arthur posted how he wants each kind handled' |
| K43-departed-person-premise | false_state_premise | not matched | Leonard is active at the clock; no Victor; nothing after 2025-09-30 23:59:59 PT is described as done |
| K50-both-fair-figure | ugt_both_fair_figure | not matched | no reported figure |
| K49-newer-source | ugt_both_fair_figure | not matched | no figure; no 'go with the most recent' line |

## Self-review

Re-read as Evals/1_Prompt_Eval.md Phases 1–3 against 04_Prompt.txt (sha256 32f7ab0cabd6 before and after this run). Every value was re-read in this run: the hub, Leonard's reply, ESG's note, the guardrails and the README from 01_Universe_Inject.sql; the board, Leonard's contact and Frederick's calendar through hg.py; reach through persona_view check-sql. Quoted spans were matched programmatically against the file.

| Check | Counter-reading (strongest case it fails, or that a finding is a false positive) | Evidence that resolves it | Verdict |
|---|---|---|---|
| C1 | The field could reject a very short prompt | 98 words, inside 20–4,000 (wc -w on 04_Prompt.txt) | clean |
| C2 | The assignment could be incomplete or the source unsupported | 00_Task_Context.json: all eight fields, universe synthcut, freeze 2025-10-01T00:00:00Z, KB bound, context db8af19cc1c3 | clean |
| C3 | A co-founder handing his assistant vendor triage could read as a junior ops job (role implausible) | Frederick is the Commercial Lead (Contacts 175c0d7bc72ed244b944cb90); the counterparties wrote to him (frederick.stone@harmonygames.co/1843618067251203081); Leonard handed it to him by name (frederick.stone@harmonygames.co/1844732913254784171); signing stays with Leonard or Arthur per ESG (frederick.stone@harmonygames.co/1844177063117059830) | clean |
| C4 | Corporate Ops could expect a memo or contract artifact, not emails and cards | Taxonomy screen 8 (vendor, legal/contracts); the main output is a spreadsheet log (§1 of the brief); Actions = writes in connectors (screen 10) | clean |
| C5 | The prompt could carry the recipe (rules, columns, exclusions) | No rule text appears (hardness_v2_check RULE_IN_PROMPT CLEAN; no 6-word overlap with seeded text); Ambiguity, Dynamic change and Multi-source live in the records (brief §8: C07C2866011/1758920520.674991, D05S58U4SAK/1759174260.052645, cmt_c9a6660d81e067ad1de7) | clean |
| C6 | Reading B of D6 (one listing event) is a fair reading that the narrowed §4b now rejects | The prompt says 'one per company'; brief §4b D6 regenerated to match (04_Prompt_Writing_Brief.md#775fc1acdcc5); every other deliverable settled in Fair readings with record ids; Finding 5 routes the surface's stricter matchers to the rubric | clean (Advisory 5 for later stages) |
| C7 | The two Minor findings could be false positives, because neither changes a write action | Eval 1 §2.6 scores only write-action divergence as Fail; the playbook C7 rule still requires reporting representational open fields as Minor (brief §4b D2, D6) | Non-fail (Minor), kept |
| C8 | 'his email' might not uniquely identify the hub, or might not state the rules attributed to it | Content identifies it ('vendor and partner backlog'); Leonard's only other Sep 26–30 mails to Fred are TestFlight notices (frederick.stone@harmonygames.co/1844718211624259514); the hub names the guardrails doc, the Monday post, ESG's note and the README; persona_view check-sql PASS; R7 is now triggered by the prompt | clean |
| C9 | 'cards for anything that needs signing' could pre-solve which rows are Sign | It names the deliverable, not the members; who signs, and which of the 36 are Sign, comes from f_b98287f6f80fe431a71209 step 4 and ESG's note (brief §4b D1 Sign row) | clean |
| C10 | Naming the folder, the board and the January review could collapse discovery | They are §6 anchors A2–A4 (noun phrases only); 'the January review' is not the event's exact title 'Q4 commitments review' (evt_fd469c29811879519c2c96); no §5 'No' item (the DM, the thread reply, the Linear comment, the checklist item, the Paylane notice) is named | clean |
| C11 | The writes could be fixed in advance rather than depend on findings | Every write depends on the per-company decision (brief §3): answers, cards, ESG emails, contacts, reminders and the reply lists all change with the classification | clean |
| C12 | A second service could carry no weight | 10 services carry weight (brief §1; dossier hardness_gate extreme PASS, pasted and current; tier certified by the gate below) | clean |
| C13 | The reminders sentence could be a bolt-on to the backlog job | It serves the same hand-off: parked and 'later' items 'come back at the January commitments review' (f_b98287f6f80fe431a71209); deleting it removes R7 | clean (stacking) |
| C14 | 'calendar', 'board' or 'email' could count as tool mentions | Natural product nouns are clean (prompt_qc_examples.md row 103); no catalog name (Evals/references/tools/catalog.json, 298 names, none in the text) | clean |
| C15 | 'When it's all done, reply…' could be a sequenced command list | Only the order of deliverables and who to tell (the screen 24 skeleton); no 'first… then… finally' over sources | clean |
| C16 | 'one per company' could read as an arbitrary format rule or call-inflation choreography | It is an ordinary preference for one reminder per item. The record carries its own reason (the review event says 'Everything we parked comes back here.'), and the 14 events are real writes, not padding. No spec-sheet layout, hedge or hint (calibration cases K31, K44-if-chain, K1 not matched) | clean |
| C17 | 'yesterday', 'my folder' or 'our Harmony Games board' could be a loose slip | Hub 2025-09-30T23:20Z = Sep 30 PT, the day before Wed Oct 1; folder owner frederick.stone@harmonygames.co (d_80a8c04753ba82ba4ba6a5); board 640643a3fd8f3ca308d9318e named 'Harmony Games' (hg.py) | clean |
| C18 | A per-company reminder or a card could be impossible, or a send could only be a draft | gcal_create_event, trello_create_card, gmail_send_message, gmail_reply_to_message, contacts_add_new_contact, gsheets_create_spreadsheet, gsheets_values_update and gdrive_move_file are all in catalog.json; every fact has a cataloged read (linear_list_comments, slack_read_thread, trello_get_checklists_on_board) | clean (Advisory 6) |
| C19 | A deciding record could sit in another person's mailbox or a private channel | persona_view check-sql PASS in this run (0 load-bearing rows hidden); dossier 1.E: 167 ids YES (rev4); the NO rows are Leonard's, Robert's and Arthur's companion copies, none required | clean |
| C20 | 'this week' or 'the January review' could contradict the clock | 'this week' resolves to Sep 29 – Oct 5, 2025; the review is a future scheduled event (Jan 5, 2026, evt_fd469c29811879519c2c96); nothing after the clock is described as done | clean |
| C21 | Friction could be announced or remove the only route | 03_Error_Async_Config.txt: Friction: none; the prompt mentions no error or wait | clean |
| C22 | /prompt's deep re-check could score a rev4 moved record (the de-named corrections, Hootline's August-only thread) as a coherence slip | rev4 blind sweep (plan/blind_fork_sweep_rev4.md) found only minor base or designed items; the Lumencloud wording is fixed; local injection gate PASS on 69603ab4b6a4 (01_Grounding_Dossier.md Self-review) | resolved; re-verified at /injection rev4 |
| C23 | STEP 0.6 could find the Leonard-email hand-off shape at 0.80 or more against the bridge task | The job, cohort, deliverables and services differ (vendor backlog vs investor send list); the skeleton was reworded (memory: prompt-dataset-duplicate-gate); no local scorer, so it is reported, not cleared | Advisory 3 |
| C24 | The task could be 'investigate and post one message' | Seven deliverable kinds across Sheets, Gmail, Trello, Contacts and Calendar (brief §4) | clean |

Unresolved: rev3's /prompt scored STEP 0.6 at 0.658 (distinct) on this same prompt, so Advisory 3 is settled for the text, not for a new library; the local surface's D1/D2 delivery checks stay routed to the rubric stage (Advisory 5). No UNVERIFIED hard gate.

```
STAGE GATE prompt-check: PASS — Task_Authoring/task_inputs · 04_Prompt_Check.md#47abcaaa13c1 · 04_Prompt.txt#32f7ab0cabd6 · 04_Prompt_Writing_Brief.md#07b5ded14cc0 · __context__#db8af19cc1c3 · __assignment__#b196657eace0 · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#caf6f21d07a5 · blocking 0 · warnings 0 · checks 25
[PASS] assignment.v3_context: Frederick Stone / Co-founder; easy cap <90%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#07b5ded14cc0, 00_Assigments.md#5418f950517f, 01_Grounding_Dossier.md#3c7feab09262, 01_Universe_Inject.sql#69603ab4b6a4, 03_Error_Async_Config.txt#2737eaf3c6bd, 01a_Hardening_Report.md#44ec9d231b56, __context__#db8af19cc1c3, __assignment__#b196657eace0, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#352ce38ff4bc)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (98 words, sha256 32f7ab0cabd6)
[PASS] evidence.quoted_spans: 4 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 10 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 14/14 items carry a source pointer (min 100%)
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

- No Fail: after the platform /injection PASS on rev4 (SQL 69603ab4b6a4), paste 04_Prompt.txt exactly as saved (98 words, sha256 32f7ab0cabd6) into /prompt with that SQL, answering the task date with "Oct 1, 2025 (synth-cut)".
- Later stages: /create-rubric-writing must accept the §4b equivalence classes the local surface is stricter about (Advisory 5); /create-humantime counts 14 reminder events (Advisory 6).

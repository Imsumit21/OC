# Prompt Check — frederick_bridge_pipeline (rev7: Q4 update send list)
> Prompt: 04_Prompt.txt · 95 words · sha256 b5ea6f0ff28c · checked 2026-11-03 against 04_Prompt_Writing_Brief.md (2026-11-03, rev11) and SQL rev11 (75b6cb2ac453; the prompt is unchanged since rev7; rev9 changed only records behind "do what he asked on the Existing Investor Update card"; rev10 moved Arthur's Play correction into a thread reply; rev11 has Paul back out (off the list) and adds Arthur's answer to Karthic in the T-Accelerate thread) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Checked for clean ordinary writing, role plausibility, no hints or riddles, every fair outcome, and distance from the dataset neighbours that failed rev6.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

The text checked, byte for byte:

> Leonard asked me in his Sep 30 email to sort out who from the bridge round gets the Q4 investor update, and I need you to take that on for me. His email lays out what he's after. Please put the send list in my Q4 2025 investor update folder, do what he asked on the Existing Investor Update card in Trello, and reply on his thread with how many ended up in each group. He wants to go through it with me on Monday, Oct 6, so it has to be done before then.

## Summary

- Fail 0 · Non-fail 0 · Advisory 3 (C10, C13, C23) · UNVERIFIED checks 0.
- Why this prompt is new. The platform `/prompt` review of rev6 (Platform_Report/prompt_report4, prompt cecfad824fd8, SQL 848189443008) scored all 20 content dimensions 5, but failed the new STEP 0.6 dataset-duplicate gate. Its meaning was 0.804 from another contributor's Frederick task ("Leonard hands Fred the fundraising part of the Oct 14 board pre-read, every firm on the 2025 list put into a status, counts and totals back"), and 0.729 and 0.720 from two completed Frederick tasks on the same handoff. The report said the request had to become a different job, not a rewording. Rev7 asks for the bridge part of the Q4 investor update send list. It drops "fundraising section", "board pre-read", "status of every firm" and "totals". The deliverable is a send list with groups, the keep-warm checklist, and a reply with the count per group.
- Checks clean: C1–C9, C11, C12, C14–C22, C24.
- Predicted /prompt band: PASS on content (no Fail, no Non-fail, no UNVERIFIED hard gate among C4, C6, C17, C18, C19). STEP 0.6 cannot be predicted locally: `hg_similarity.py` is not in the local Evals copy, so the distance from the three neighbours is argued, not measured (C23).
- Status: READY FOR /prompt.

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C23 | Originality — Dataset Duplicate · Advisory | "who from the bridge round gets the Q4 investor update" | Eval 1 STEP 0.6 (platform release after rev5); Platform_Report/prompt_report4 | Not measurable locally. The core request is now "who gets the Q4 investor update", which the neighbours do not ask for. The neighbours ask for the board pre-read's pipeline status of every firm (L12, 0.804), the firms that said no (0.729), and an updated 2025 list (0.720). The prompt names none of the neighbours' anchors: no board pre-read, fundraising section, Oct 14 board, 2025 investor list or totals. It still shares the persona, Leonard and the bridge round, so a "same scenario" reading (0.70–0.80, not a fail) is possible |
| 2 | C10 | Discovery collapse · Advisory | "Existing Investor Update card" | playbook C10; brief §5 F21, F42 | Names a brief §5 record by title. Leonard's email already names it (frederick.stone@harmonygames.co/1844724419788800011), so no discovery is lost. Rev9: the card's Sep 29 comment 68db03b86054eff7e8e92474 holds the checklist and follow-up rules; the prompt names neither. The keep-warm rule in comment 68c64270d660c977c4696986 still has to be found. Kept on purpose: leaving it out would be a C16 hidden destination |
| 3 | C13 | Coherence · Advisory | "put the send list in my Q4 2025 investor update folder" | playbook C13 | Three asks (send list, card, reply) serve one stated purpose, Leonard's Q4 update send list. That is stacking, not bolt-ons |

## Fair readings (accepted outcomes)

| Deliverable | Reading A (best supported) | Reading B (strongest alternative) | Resolution and evidence |
|---|---|---|---|
| D1 send list | One Google Sheet in d_5e8a1c3f9b07d2e64a1b93 with 25 rows: New investor 1 (Anton Bernstein, 25,000); In talks 7 (GFR Fund, Andreessen Horowitz, NCsoft, Homa, Brightwater Games Fund, plus Dentsu Ventures and T-accelerate at iOS only); Awaiting reply 14; Keep warm 3 (London Venture Partners, Hiro Capital, Sciplay) (brief §4b) | every name on the 2025 list (Robert's mail frederick.stone@harmonygames.co/1844623441920000059) | Leonard's email withdraws it ("Let's not, only the people the doc says."): rejected |
| D1 send list | Paul Heydon off the send list (rev11) | Paul In talks with 50,000, or a New investor (Leonard's post C07C2866011/1758303600.418207 says he "is in"; the angels sheet f_6e1d93a0c4b72f85d39a0e; the Sep 29 nudge frederick.stone@harmonygames.co/1844610859008000037 shows an unsigned SAFE) | Leonard's Sep 30 reply under that same post, C07C2866011/1759251900.863415: "Paul's out, he wrote me this morning that he can't put money in this year after all"; the doc: a no told to any of us is a pass, and a pass without a call or meeting stays off: rejected |
| D1 send list | Anton Bernstein New investor, 25,000 | 40,000 (the post and the Bridge angels sheet f_6e1d93a0c4b72f85d39a0e) | Leonard's DM D05S58U4SAK/1758731100.281734 voids the 40 SAFE and sends a new one at 25; D05S58U4SAK/1758914100.640218 says Anton signed the 25 one: rejected |
| D1 send list | Sciplay Keep warm | In talks (its thread ends Sep 18 with "we'll continue to play") | Robert's reply C07C2866011/1759248360.377105 (they're passing on this round) after the Sep 15 call evt_25c9ee60d4b6c8f6d39a74; the doc's Keep warm = passed after a pitch call: rejected |
| D1 send list | Hiro Capital Keep warm | Awaiting reply (list "no response as of 09/11") | Edith Vane's pass frederick.stone@harmonygames.co/1844318935449600041, copied to Hiro's Investment Director PERSON_5282; Contacts e3a91c07d5b48f26a0c7e314 lists her as Partner, Hiro Capital; Sep 23 call evt_7d3e19b04a6c25f8e1b9a0: rejected |
| D1 send list | Homa and Brightwater In talks | off the list (not on the 2025 list) | the doc adds off-list firms pitched on a call since Sep 3; calls evt_89381fe5a15b802c5652a9 and evt_2f86b0d4c9e17a35b64e0d: rejected |
| D1 send list | T-accelerate and Dentsu build access iOS only | iOS and Android (ZOM-567 logs both Play adds) | Arthur's Sep 30 answer to Karthic in the T-Accelerate thread frederick.stone@harmonygames.co/<CAU8zEO-shvUXQVk4-lQPDj5ihq08pcABtHRrtUv@mail.gmail.com> (rev11: the Play tester list for the investor accounts was never attached to the internal test track, nobody on it has the Android build yet) and his reply C0880U9751A/1759274400.518306 in the thread under Leonard's 0.3.49 iOS release post C0880U9751A/1759182908.627389 (the 3 Dentsu folks have no android access either, "whatever the Linear log says"); he attaches it with the Oct 1 push; the doc asks whether they "can get the current internal build": rejected |
| D1 send list | Play Ventures, March Gaming Fund, Grishin Robotics, Lakestar Ventures, [PERSON_NAME_5402] off | Keep warm (they passed) | the card rule 68c64270d660c977c4696986 and the doc keep only passes after a pitch call or meeting this round: rejected |
| D1 send list | a16z In talks | off or Keep warm (the speedrun no, frederick.stone@harmonygames.co/1844748127814183717) | the doc's accelerator rule (f_3b9e61c04d7a52e8f1a6c2): rejected |
| D2 card | four checklists on 68c5a49e8491a9d7faf869d0, one per group (Keep warm: London Venture Partners, Sciplay, Hiro Capital; New investor; In talks; Awaiting reply), 25 items | only a Keep warm checklist (the Sep 13 comment alone), or Keep warm items for every firm that passed (email-only no's included) | Leonard's Sep 29 comment 68db03b86054eff7e8e92474 asks for a checklist for every other group besides Keep warm; the Sep 13 rule 68c64270d660c977c4696986 covers only passes after a pitch call or meeting: rejected |
| D4 follow-up cards (rev9) | 18 "F/up with" cards in To Do (rev11); a comment on 68c99e98737744bd966aed24 for NCsoft; no card for Dentsu Ventures or Makers Fund | a new NCsoft card (the To Do card names only Anel); cards for Dentsu and Makers (calendar read only to Sep 30); a comment on Homa's Doing card instead of a card | f_48247af79428823c3cac92 names Anel Ceman as NCsoft's partner; evt_3671b9a924ccba550e51fa (Oct 1) and evt_6b2e94d0c17a3f58e9d2b1 (Oct 8) are on Fred's calendar after Sep 30; the rule names cards "in To Do" only: rejected |
| D3 reply | a sent reply on frederick.stone@harmonygames.co/1844724419788800011 to leonard.hayes@harmonygames.co: New investor 1, In talks 8, Awaiting reply 14, Keep warm 3 | reply-all adding robert@harmonygames.co and arthur.blake@harmonygames.co | same thread, decision and contents: both accepted |

BOTH_FAIR_FIGURE: none. No reported figure is left unsettled. The group counts follow from the rows above, Anton's 25,000 from Leonard's DMs plus the Completed notice; Paul is off the list (rev11), so no angel is In talks.

## Verification log

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| "Leonard" | person | leonard.hayes@harmonygames.co (entity.py resolve: persona leonard_hayes) | verified |
| "his Sep 30 email" | event · date | frederick.stone@harmonygames.co/1844724419788800011, 2025-09-30T21:05:00Z = Tue Sep 30, 2:05pm PT; To Frederick, cc Robert and Arthur | verified |
| "who from the bridge round gets the Q4 investor update" | event | frederick.stone@harmonygames.co/1844724419788800011: "can you take the send list for the Q4 investor update off my plate? … What I need from you is everyone from the bridge round who should get it" | verified |
| "His email lays out what he's after" | state | frederick.stone@harmonygames.co/1844724419788800011 body: the send-list doc, folder, README, card, deck, reply | verified |
| "the send list" | doc | frederick.stone@harmonygames.co/1844724419788800011 subject "Q4 investor update - send list"; doc f_3b9e61c04d7a52e8f1a6c2 | verified |
| "my Q4 2025 investor update folder" | doc | d_5e8a1c3f9b07d2e64a1b93 "Q4 2025 investor update", owner frederick.stone@harmonygames.co, shared with leonard.hayes@harmonygames.co | verified |
| "the Existing Investor Update card in Trello" | doc | 68c5a49e8491a9d7faf869d0 (base card, created 2025-09-13 by Leonard, in Doing); hg.py search trello "Existing Investor Update" finds one card | verified; unique |
| "do what he asked" | state | frederick.stone@harmonygames.co/1844724419788800011: "Then do what I put on the Existing Investor Update card in Trello." (rev9); his comments on the card: 68c64270d660c977c4696986 (Keep warm checklist, Sep 13) and 68db03b86054eff7e8e92474 (a checklist per other group, follow-up cards in To Do, Sep 29) | verified |
| "reply on his thread" | channel | frederick.stone@harmonygames.co/1844724419788800011: "reply here" | verified |
| "how many ended up in each group" | state | frederick.stone@harmonygames.co/1844724419788800011: "reply here with how many firms and angels are in each group" | verified |
| "Monday, Oct 6" | event · date | evt_9c41e7a2d05b38f6e1a7c4 "Q4 update send list review", 2025-10-06T21:00Z = Mon 2:00pm PT, on frederick.stone@harmonygames.co's calendar | verified; future at the clock, not described as done |
| "go through it with me" | state | frederick.stone@harmonygames.co/1844724419788800011: "so we can go through it together" | verified |
| "Trello" | product | trello_create_checklist, trello_create_check_item, trello_create_card and trello_add_comment exist in Evals/references/tools/catalog.json (hg.py reference routes trello) | verified; a product name, not a tool name |
| write path | capability | gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file, gmail_reply_to_message in the catalog; Frederick owns d_5e8a1c3f9b07d2e64a1b93 | verified |

## Brief coverage

| Brief item | Present in the prompt (quoted span, or absent) |
|---|---|
| §4 D1 send list in the folder | "put the send list in my Q4 2025 investor update folder" |
| §4 D2 a checklist per group on the card | "do what he asked on the Existing Investor Update card in Trello" |
| §4 D4 follow-up cards in To Do (rev9) | "do what he asked on the Existing Investor Update card in Trello": the ask is written on the card (comment 68db03b86054eff7e8e92474); the cards go on the same board |
| §4 D3 reply with the count per group | "reply on his thread with how many ended up in each group" |
| §6 anchor A1, Leonard's Q4 update email | "Leonard asked me in his Sep 30 email" … "His email lays out what he's after" |
| §6 membership, groups, amounts, build access (incorporated via the email) | "His email lays out what he's after" |
| §6 destination and file name | "my Q4 2025 investor update folder" (the name pattern stays in the README) |
| §6 not everyone on the 2025 list | absent by design; inferable from Leonard's email, not a graded positive |
| §7 deadline | "Monday, Oct 6" |
| §8 levers | absent by design: no hint at any correction |
| §9 must not appear | absent: no firm, person met in research, amount, group name, status, keep-warm wording, DocuSign or tester state; no tool name |
| §11 every write asked of the assistant | "Please put the send list" (no first-person promise beside any write) |

## Calibration self-test

The 15 `calibration_cases` in Evals/references/rules/prompt_qc_cases.json, run against the text above:

| Case | Rule | Expected | Result for this prompt |
|---|---|---|---|
| K11-staged-errors | staged_errors | FAIL | not matched: no misspellings or broken spacing |
| K11-control-spelled-correctly | staged_errors | PASS | matched: clean spelling |
| K31-trap-hint | trap_hint_or_riddle | FAIL | not matched: no line points at a trap |
| control-symptom | trap_hint_or_riddle | PASS | matched: states the job, not a cause |
| K42-hidden-destination | hidden_destination | FAIL | not matched: every destination is named |
| K47-hidden-destination | hidden_destination | FAIL | not matched: the card is named |
| K44-hidden-destination | hidden_destination | FAIL | not matched: "reply on his thread" points to one thread |
| control-named-destination | hidden_destination | PASS | matched: folder, card and thread named |
| K1-audit-form | audit_form | FAIL | not matched: no deliverable-catalogue verbs |
| K43-audit-form | audit_form | FAIL | not matched |
| K44-if-chain | if_chain | FAIL | not matched: no conditionals |
| control-plain-request | audit_form | PASS | matched: one plain request; the rules live in the records |
| K43-departed-person-premise | false_state_premise | FAIL | not matched: Leonard is active (frederick.stone@harmonygames.co/1844724419788800011, Sep 30) |
| K50-both-fair-figure | ugt_both_fair_figure | PASS | not applicable: no unsettled figure |
| K49-newer-source | ugt_both_fair_figure | PASS | consistent: newer sources settle Anton's amount (D05S58U4SAK/1758731100.281734, D05S58U4SAK/1758914100.640218) with no prompt clause |

## Self-review

**Eval walk (`Evals/1_Prompt_Eval.md`).**
- Phase 1:
  - persona §1.1: Frederick, a co-founder, is the person Leonard delegated to;
  - naturalness §1.2: first person, plain, clean spelling;
  - anti-patterns §1.3: no command list, bolt-on, pre-solving or tool name;
  - diversity §1.4: three writes in three services;
  - assignment §1.5: Corporate Ops (fundraising, investor relations) with Retrieval at the centre.
- Phase 2: the fair readings above, feasibility, truthfulness (verification log), cross-service, investigation → action, clarity, contrived, today's date, and originality (C23).
- Phase 3: universe coherence rests on the rev6 platform `/injection` PASS and the two rev6 blind sweeps. Rev7 adds or rewrites only these: the hub, the send-list doc, the Q3 decoy, the README and folder name, the deck text, Leonard's #executives signed note, Robert's mail, Arthur's aside and the review event. It removes the Board Deck card. It needs its own `/injection` run.

| Check | Counter-reading | Evidence | Resolution |
|---|---|---|---|
| C1 | could the field reject the text? | 95 words, recomputed in the header (04_Prompt.txt sha256 b5ea6f0ff28c) | inside 20–4,000 |
| C2 | is the assignment incomplete or the persona unresolved? | task_context.py --require-source exit 0; context_hash f1f763cb8cb4 in Working_Files/00_Task_Context.json | bound and supported |
| C3 | would /prompt say Leonard should build the send list himself? | Leonard delegated it to Frederick (frederick.stone@harmonygames.co/1844724419788800011); a co-founder owning who gets the investor update is ordinary Corporate Ops work | plausible; voice fits a co-founder |
| C4 | is Retrieval only nodded at, since the output is a sheet? | Taxonomy Retrieval: "extracting structured values from documents or records"; 79 names looked at across 10 services to keep 25 (brief §1) | exercised |
| C5 | does the prompt carry the recipe, or is no complexity load-bearing? | no rule, group or definition in the text; corrections met second (D05S58U4SAK/1758731100.281734, C0880U9751A/1759274400.518306, C07C2866011/1759248360.377105), brief §8 | load-bearing; nothing pre-solved |
| C6 | strongest Reading B: everyone on the 2025 list gets the update, as Robert asked | frederick.stone@harmonygames.co/1844623441920000059 vs the hub's "Let's not, only the people the doc says." | settled by the incorporated hub; every other fair reading in the table above |
| C7 | "sort out who … gets" is vague; reply vs reply-all is left open | the doc states the groups and who stays off (f_3b9e61c04d7a52e8f1a6c2); reply-all has the same contents (brief §4b D3) | no competing concrete write; recipients representational |
| C8 | does "His email" pick out one record that says what is attributed to it? | only frederick.stone@harmonygames.co/1844724419788800011 is Leonard's Sep 30 Q4 update email (subject "Q4 investor update - send list"), and it names the doc, folder, card and reply | (a)–(d) met |
| C9 | does "how many ended up in each group" presuppose a count? | the counts come only from the work (solver truth 1 / 8 / 14 / 3); no value in the text | not pre-solved |
| C10 | counter to finding 2: naming the card collapses discovery of authority H2 | the email names the card on the first read; the rule sits in comment 68c64270d660c977c4696986 | Advisory only |
| C11 | could any write be made without investigating? | the send list needs every firm's state (solver/truth.json); the checklist needs which passes were pitched (evt_7d3e19b04a6c25f8e1b9a0); the counts need the list | every write depends on findings |
| C12 | is the second service trivial, or is the tier uncertified? | 10 services; call_budget 508 (01_Hardness_Manifest.json); HARDNESS GATE (extreme): PASS in 01_Grounding_Dossier.md | passes |
| C13 | counter to finding 3: the card ask is a bolt-on | the same email asks for it, for the same update (frederick.stone@harmonygames.co/1844724419788800011) | stacking, Advisory only |
| C14 | "Trello" is a tool mention | prompt_qc_examples.md: product names are clean (playbook C14) | clean |
| C15 | "put …, do …, and reply" is a sequenced command list | the order of deliverables is the screen 24 skeleton; no source or method is sequenced | clean |
| C16 | hidden destination, spec sheet, hint or audit wording? | folder, card and thread named (prompt_qc_cases.json control-named-destination); no K31 hint | clean |
| C17 | is "his Sep 30 email" or "Monday, Oct 6" false at the clock? | 2025-09-30T21:05:00Z (frederick.stone@harmonygames.co/1844724419788800011); evt_9c41e7a2d05b38f6e1a7c4 on Oct 6 | true |
| C18 | can the catalog file a sheet in a folder, and is the reply a real send? | gsheets_create_spreadsheet plus gdrive_move_file; gmail_reply_to_message (Evals/references/tools/catalog.json); Frederick owns d_5e8a1c3f9b07d2e64a1b93 | feasible |
| C19 | can Frederick read the doc, README, deck, calls, Slack replies, his DM with Leonard and #zombie-match3d? | check-sql YES for SQL 75b6cb2ac453 (01_Grounding_Dossier.md §1.E); brief §5a 48 of 48 YES | YES |
| C20 | is there a relative date that resolves wrongly? | "Sep 30" and "Monday, Oct 6" are absolute; persona_today 2025-10-01 (Working_Files/00_Task_Context.json) | clean |
| C21 | is a failure or wait announced, or a route removed? | 03_Error_Async_Config.txt Friction: none | clean |
| C22 | are the touched records incoherent? | rev6 coherence sweep fixes kept (C0880U9751A/1759274400.518306, C096HFA5Z8W/1756942260.617302); base_check, base_claims and eval lint PASS on 75b6cb2ac453 (01_Grounding_Dossier.md); the rev7 rewrites change only the job's wording | clean; the next `/injection` re-checks |
| C23 | the meaning still matches the three dataset neighbours (STEP 0.6) | Platform_Report/prompt_report4 neighbours: Oct 14 board pre-read pipeline (0.804), firms that said no (0.729), updated 2025 list (0.720); the rev7 prompt asks who gets the Q4 investor update and names none of their anchors | not measurable locally; argued below the 0.80 cut; Advisory |
| C24 | is it just investigate and post one message? | three writes in Sheets/Drive, Trello and Gmail (brief §4) | clean |

Mechanics: every quoted span in Findings and Brief coverage was checked as an exact substring of 04_Prompt.txt (the gate re-verifies). The prompt hash was b5ea6f0ff28c before and after writing this report.

Unresolved: the dataset-similarity score of the new prompt (C23) is only known from the next platform `/prompt` run.

```
STAGE GATE prompt-check: PASS — Task_Authoring/task_inputs · 04_Prompt_Check.md#da4289fa7117 · 04_Prompt.txt#b5ea6f0ff28c · 04_Prompt_Writing_Brief.md#63a13e65362a · __context__#f1f763cb8cb4 · __assignment__#827e8afa884d · __policy__#dc4ab5df3cdd · __gate_policy__#0fc4bb90877f · __review__#74d9af6ba2d2 · blocking 0 · warnings 0 · checks 25
[PASS] assignment.v3_context: Frederick Stone / Co-founder; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#63a13e65362a, 00_Assigments.md#8ae66b700bc2, 01_Grounding_Dossier.md#faebd666e5f4, 01_Universe_Inject.sql#75b6cb2ac453, 03_Error_Async_Config.txt#6a1259070c3d, 01a_Hardening_Report.md#d004fd076cf8, __context__#f1f763cb8cb4, __assignment__#827e8afa884d, __policy__#dc4ab5df3cdd, __gate_policy__#0fc4bb90877f, __review__#51573e788374)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (95 words, sha256 b5ea6f0ff28c)
[PASS] evidence.quoted_spans: 3 quoted span(s) verified as exact substrings of 04_Prompt.txt
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

- No Fail. Paste 04_Prompt.txt exactly as saved into `/prompt`, paired with `/injection`. `/prompt` takes the task date, the prompt, all eight assignment fields and the SQL (01_Universe_Inject.sql, sha256 75b6cb2ac453).
- Task date for both: Oct 1, 2025 (synth-cut), the assignment's universe date.
- Any edit to 04_Prompt.txt (retyping it in your own words included) changes the hash: re-run `/create-prompt-writing check` after the final edit.
- The SQL changed (rev7), so run `/injection` on it first, then `/prompt`.
- Hold Oracle Events, the rubric and the baseline until `/injection` and `/prompt` both pass on SQL 75b6cb2ac453 and a new Opus pre-check clears `/hardness`.

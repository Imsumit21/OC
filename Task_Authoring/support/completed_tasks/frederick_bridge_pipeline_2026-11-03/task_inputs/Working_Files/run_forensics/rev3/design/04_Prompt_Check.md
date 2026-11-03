# Prompt Check — frederick_bridge_pipeline
> Prompt: 04_Prompt.txt · 107 words · sha256 cecfad824fd8 · checked 2026-11-02 against 04_Prompt_Writing_Brief.md (2026-11-02, 9d1555e8eb21) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Checked for clean ordinary writing, role plausibility, no hints or riddles, and every fair outcome.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

The text checked, byte for byte:

> Leonard emailed me on Sep 30 asking me to own the fundraising section of the Oct 14 board pre-read since he's flying to LA today, and I'd like you to take it on for me. His email has what he wants. Can you build the sheet and put it in my Board - Oct 14 2025 folder, take care of the Existing Investor Update card in Trello like he asks, and then reply to him on that thread with the numbers he needs for the slide? I'm going through it with him at the review on Monday, Oct 6, so it needs to be done before then.

## Summary

- Fail 0 · Non-fail 0 · Advisory 3 (C10, C13, C20) · UNVERIFIED checks 0.
- Checks clean: C1–C9, C11, C12, C14–C19, C21–C24.
- Predicted /prompt band: PASS (no Fail, no Non-fail, no UNVERIFIED hard gate among C4, C6, C17, C18, C19).
- Status: READY FOR /prompt.
- Revision in this run: the drafted text (105 words, sha256 649abf4249fb) had two problems this check found. First, "take care of the Trello follow-up he mentions for anyone who passed" was wider than the card's pitched-only rule (68c64270d660c977c4696986: "Email-only no's don't need it"), a C6/C18 conflict. Second, it left the Trello destination unnamed although Leonard's email names it, a C16 hidden destination (prompt_qc_cases.json K47). The text above names the card, says "like he asks", and anchors the email date (Sep 30). The brief (§5 F21, §6, §8, §9, §11) was updated to match and re-certified (STAGE GATE prompt-writing: PASS, 9d1555e8eb21). This report binds only the revised text.

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C20 | Alignment with Today's Date · Advisory | "flying to LA today" | Eval 1 §2.8; Prompt Writing §4.2 prefers absolute dates | relative wording only: "today" resolves to Wed Oct 1, 2025 (persona_today), and Leonard's email sent Sep 30 says he flies "tomorrow morning", so the premise is true and not described as done. Optional wording: "since he's flying to LA on Oct 1" |
| 2 | C10 | Discovery collapse · Advisory | "Existing Investor Update card" | playbook C10; brief §5 F21 | names a brief §5 record by title. Leonard's email, the first record read, already names it (frederick.stone@harmonygames.co/1844724419788800011), so no discovery is lost; the keep-warm rule in comment 68c64270d660c977c4696986 still has to be found. Kept on purpose: leaving it out would be a C16 hidden destination |
| 3 | C13 | Coherence · Advisory | "build the sheet and put it in my Board - Oct 14 2025 folder" | playbook C13 | three asks (sheet, card, reply) serving one stated purpose, the fundraising section Leonard delegated: stacking, not bolt-ons |

## Fair readings (accepted outcomes)

| Deliverable | Reading A (best supported) | Reading B (strongest alternative) | Resolution and evidence |
|---|---|---|---|
| D1 register sheet | one Google Sheet in d_5e8a1c3f9b07d2e64a1b93, 79 firms, the template's buckets as of end of Sep 30 PT, committed $25,000 (Anton), soft-circled $50,000 (Paul), Dentsu iOS only, T-accelerate both, totals at the bottom (brief §4b) | Paul counted as committed $50K from Leonard's post C07C2866011/1758303600.418207 | the incorporated template counts signed SAFEs only (f_3b9e61c04d7a52e8f1a6c2), and no Completed notice exists for Paul beside Anton's (frederick.stone@harmonygames.co/1844354293432320031): Reading B rejected by an incorporated authority |
| D1 register sheet | the population includes the off-list calls Homa (evt_89381fe5a15b802c5652a9) and Brightwater (evt_2f86b0d4c9e17a35b64e0d) | only the 2025 list, or only people Leonard emailed (Arthur's aside C07C2866011/1759168800.117903) | Leonard's email and the template add off-list firms with calls since Sep 3: rejected |
| D1 register sheet | a Google Sheet | a Google Doc (the README f_c61a0e93b7d24f58a2e917 allows Sheets or Docs) | the prompt says "build the sheet" and the email says "One sheet": a Doc is not the asked deliverable |
| D1 register sheet | a16z In talks | a16z Passed (frederick.stone@harmonygames.co/1844748127814183717, Sep 30 8:21pm PT, inside the window) | nothing newer, no authority or scope settles it: both accepted in brief §4b and the sidecar outcome review |
| D2 card | a Keep warm checklist on 68c5a49e8491a9d7faf869d0 with London Venture Partners, Sciplay and Hiro Capital (plus a16z when marked Passed) | items for every firm that passed, email-only no's included (Grishin Robotics frederick.stone@harmonygames.co/1842278603974731778) | the card's rule 68c64270d660c977c4696986 covers only firms pitched on a call or meeting; the prompt's "like he asks" adds no wider scope: rejected |
| D2 card | the Existing Investor Update card | the Board Deck - Oct 14 card, which also has a checklist (68d8193cf451863621c88a2a) | the prompt names the Existing Investor Update card: rejected |
| D3 reply | a sent reply on frederick.stone@harmonygames.co/1844724419788800011 to leonard.hayes@harmonygames.co: 79 firms, committed $25,000, soft-circled $50,000 | reply-all adding robert@harmonygames.co and arthur.blake@harmonygames.co | same thread, decision and contents: both accepted |
| D3 reply | the reply on the thread | an email to the board, as Robert asked (frederick.stone@harmonygames.co/1844623441920000059) | Leonard's email withdraws it ("Let's not, it goes in the deck."): rejected; a draft is not a send either |

BOTH_FAIR_FIGURE: none. No single reported figure is left unsettled. The a16z fork changes the checklist write, not just a figure, and both of its outcomes are accepted.

## Verification log

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| "Leonard" | person | leonard.hayes@harmonygames.co (entity.py resolve: persona leonard_hayes, Contacts 63fffeb4fab5233ed5bb73bf) | verified |
| "emailed me on Sep 30" | event · date | frederick.stone@harmonygames.co/1844724419788800011, 2025-09-30T21:05:00Z = Tue Sep 30, 2:05pm PT; To Frederick, cc Robert and Arthur | verified |
| "own the fundraising section of the Oct 14 board pre-read" | event | frederick.stone@harmonygames.co/1844724419788800011: "can you own the fundraising section of the Oct 14 pre-read?"; subject "Oct 14 board pre-read - fundraising section" | verified |
| "flying to LA today" | state | same email, "I'm flying to LA tomorrow morning", sent Sep 30; Oct 1 is persona today (Working_Files/00_Task_Context.json /universe/persona_today) | verified; future at the clock, not described as done |
| "His email has what he wants" | state | frederick.stone@harmonygames.co/1844724419788800011 body: scope, template, folder, card, reply | verified |
| "the sheet" | doc | frederick.stone@harmonygames.co/1844724419788800011: "One sheet, one row per firm." | verified |
| "my Board - Oct 14 2025 folder" | doc | d_5e8a1c3f9b07d2e64a1b93, owner frederick.stone@harmonygames.co, created 2025-09-26T18:20Z, shared with leonard.hayes@harmonygames.co | verified |
| "the Existing Investor Update card in Trello" | doc | 68c5a49e8491a9d7faf869d0; hg.py search trello "Existing Investor Update": trello/data.json /cards/801/name, one card (the other two hits are its own actions) | verified; unique |
| "like he asks" | state | frederick.stone@harmonygames.co/1844724419788800011: "Whatever the Existing Investor Update card says to do for firms that pass, do that too." | verified |
| "reply to him on that thread" | channel | frederick.stone@harmonygames.co/1844724419788800011: "reply here" | verified |
| "the numbers he needs for the slide" | state | same email: "reply here with the numbers the fundraising slide needs"; card comment 68d81f30a6c94e2b7d05e1f4 names them | verified |
| "the review on Monday, Oct 6" | event · date | evt_9c41e7a2d05b38f6e1a7c4 "Board pre-read review - fundraising", 2025-10-06T16:00Z = Mon 9:00am PT, on frederick.stone@harmonygames.co's calendar, organizer leonard.hayes@harmonygames.co | verified; future (semantic deadline) |
| "I'm going through it with him" | state | frederick.stone@harmonygames.co/1844724419788800011: "so we can go through it together" | verified |
| "Trello" | product | trello_create_checklist and trello_create_check_item exist in Evals/references/tools/catalog.json (checked with hg.py-run catalog scan this run) | verified; a product name, not a tool name |
| write path | capability | gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file, gmail_reply_to_message in the catalog; Frederick owns d_5e8a1c3f9b07d2e64a1b93 | verified |

## Brief coverage

| Brief item | Present in the prompt (quoted span, or absent) |
|---|---|
| §4 D1 register sheet in the folder | "build the sheet and put it in my Board - Oct 14 2025 folder" |
| §4 D2 keep-warm checklist on the card | "take care of the Existing Investor Update card in Trello like he asks" |
| §4 D3 reply with the slide numbers | "reply to him on that thread with the numbers he needs for the slide" |
| §6 anchor A1, Leonard's board pre-read email | "Leonard emailed me on Sep 30" … "His email has what he wants" |
| §6 population, statuses, money, build access (incorporated via the email) | "His email has what he wants" |
| §6 destination and file name | "my Board - Oct 14 2025 folder" (the name pattern stays in the README) |
| §6 no board email | absent by design; inferable from Leonard's email, not a graded positive |
| §7 deadline | "the review on Monday, Oct 6" |
| §8 levers | absent by design: no hint at any correction |
| §9 must not appear | absent: the banned-term scan matches only "2025" and the dash inside the folder's real name; 0 of 298 catalog tool names; RULE_IN_PROMPT CLEAN |
| §11 every write asked of the assistant | "Can you build the sheet" (no first-person promise beside any write) |

## Calibration self-test

The 15 `calibration_cases` in Evals/references/rules/prompt_qc_cases.json, run against the text above. Matched means the prompt shows the case's pattern; none is a defect by itself.

| Case | Rule | Expected | Result for this prompt |
|---|---|---|---|
| K11-staged-errors | staged_errors | FAIL | not matched: no misspellings or broken spacing |
| K11-control-spelled-correctly | staged_errors | PASS | matched: clean spelling, like the control |
| K31-trap-hint | trap_hint_or_riddle | FAIL | not matched: no line points at a trap |
| control-symptom | trap_hint_or_riddle | PASS | matched: states the job, not a cause |
| K42-hidden-destination | hidden_destination | FAIL | not matched: every destination is named |
| K47-hidden-destination | hidden_destination | FAIL | not matched: the card is named (the draft's "the Trello follow-up he mentions" was close to this case and was revised) |
| K44-hidden-destination | hidden_destination | FAIL | not matched: "reply to him on that thread" points to one thread |
| control-named-destination | hidden_destination | PASS | matched: folder, card and thread named |
| K1-audit-form | audit_form | FAIL | not matched: no deliverable-catalogue verbs |
| K43-audit-form | audit_form | FAIL | not matched |
| K44-if-chain | if_chain | FAIL | not matched: no conditionals |
| control-plain-request | audit_form | PASS | matched: one plain request; the rules live in the records |
| K43-departed-person-premise | false_state_premise | FAIL | not matched: Leonard is active (frederick.stone@harmonygames.co/1844724419788800011, Sep 30) |
| K50-both-fair-figure | ugt_both_fair_figure | PASS | not applicable: no unsettled figure |
| K49-newer-source | ugt_both_fair_figure | PASS | consistent: newer sources settle Anton's amount (frederick.stone@harmonygames.co/1844162278195200023) with no prompt clause |

## Self-review

**Eval walk (`Evals/1_Prompt_Eval.md`).** Phase 1: persona §1.1 (Frederick, a co-founder, is the person Leonard delegated to), naturalness §1.2 (first person, plain, clean spelling), anti-patterns §1.3 (no command list, bolt-on, pre-solving or tool name), diversity §1.4 (three writes in three services), assignment and complexity §1.5 (Corporate Ops fundraising and board work; Ambiguity, Dynamic change and Multi-source load-bearing per brief §8). Phase 2: fair readings §2.1 above; feasibility §2.2 and ACL (C18, C19); truthfulness §2.3 (verification log); cross-service §2.4 (C12); investigation → action §2.5 (C11); clarity §2.6 (C7); contrived §2.7 (C15, C16, calibration); today's date §2.8 (C20); originality §2.9 (C23). Phase 3: coherence rests on the rev3 `/injection` PASS (Platform_Report/injection_report3, SQL 952e12a9ad7a).

| Check | Counter-reading | Evidence | Resolution |
|---|---|---|---|
| C1 | could the field reject the text? | 107 words, recomputed in the header (04_Prompt.txt sha256 cecfad824fd8) | inside 20–4,000 |
| C2 | is the assignment incomplete or the persona unresolved? | task_context.py --require-source exit 0; context_hash f1f763cb8cb4 in Working_Files/00_Task_Context.json; entity.py resolves frederick.stone@harmonygames.co | bound and supported |
| C3 | would /prompt say Leonard (CEO) should do this, or that a co-founder would not build a pipeline sheet? | Leonard delegated it to Frederick (frederick.stone@harmonygames.co/1844724419788800011); brief §1 remit; a better-fitting colleague alone is not a Fail (playbook C3) | plausible; voice fits a founder |
| C4 | is Retrieval only nodded at, since the output is a sheet? | Taxonomy screen 10 Retrieval: "extracting structured values from documents or records"; 79 firms across 10 services (brief §1); Corporate Ops focus "Fundraising, board" (screen 8) | exercised |
| C5 | does the prompt carry the recipe, or is no complexity load-bearing? | no rule, bucket or definition in the text; corrections met second (C07C2866011/1758303600.418207 → frederick.stone@harmonygames.co/1844162278195200023), brief §8 | load-bearing; no recipe |
| C6 | strongest Reading B: keep-warm items for every firm that passed | card rule 68c64270d660c977c4696986; prompt says "like he asks"; sidecar outcome review bound to cecfad824fd8 | settled by an incorporated authority; every other fair reading accepted (brief §4b) |
| C7 | "take care of" is a vague verb; reply vs reply-all is left open | the card states the act (one checklist item per firm, 68c64270d660c977c4696986); reply-all has the same contents (brief §4b D3) | no competing concrete write; the channel is pinned; recipients representational |
| C8 | does "His email" pick out one record that says what is attributed to it? | gmail "board pre-read" finds the email and Monday's invitation (brief §5a F1); only frederick.stone@harmonygames.co/1844724419788800011 is Leonard's Sep 30 ask, and it states the folder, template, card and reply | (a)–(d) hold: readable, unique, accurate, instructions only |
| C9 | does "the numbers he needs for the slide" presuppose a count or value? | the three numbers are named only on card comment 68d81f30a6c94e2b7d05e1f4; no value in the text | not pre-solved |
| C10 | counter to finding 2: naming the card collapses discovery of authority H2 | the email names the card on the first read (frederick.stone@harmonygames.co/1844724419788800011); the rule sits in comment 68c64270d660c977c4696986 | Advisory only; nothing lost |
| C11 | could any write be made without investigating? | the sheet needs 79 statuses (solver/truth.json); the checklist needs which passes were pitched (evt_7d3e19b04a6c25f8e1b9a0); the reply needs the totals | every write depends on findings |
| C12 | is the second service trivial, or is the tier uncertified? | 10 services; call_budget 502 (01_Hardness_Manifest.json); HARDNESS GATE (extreme): PASS in 01_Grounding_Dossier.md | passes; tier.hardness re-checked by the gate |
| C13 | counter to finding 3: the card ask is a bolt-on | the same email asks for it, for the same section (frederick.stone@harmonygames.co/1844724419788800011) | stacking, Advisory only |
| C14 | "Trello" is a tool mention | prompt_qc_examples.md row 103 note: apply the current rule; product names are clean (playbook C14) | clean |
| C15 | "build …, take care of …, and then reply" is a sequenced command list | the order of deliverables is the screen 24 skeleton (playbook C15); no source or method is sequenced | clean |
| C16 | hidden destination, spec sheet, hint or audit wording? | folder, card and thread named (prompt_qc_cases.json control-named-destination); no K31 hint; no K1/K43 verbs | clean after the revision |
| C17 | is "on Sep 30" or "flying to LA today" false at the clock? | 2025-09-30T21:05:00Z and "flying to LA tomorrow morning" (frederick.stone@harmonygames.co/1844724419788800011); verification log | true |
| C18 | can the catalog file a sheet in a folder, and is the reply a real send? | gsheets_create_spreadsheet plus gdrive_move_file; gmail_reply_to_message (Evals/references/tools/catalog.json); Frederick owns d_5e8a1c3f9b07d2e64a1b93 | feasible; exact amounts survive as cell text |
| C19 | can Frederick read the template, README, deck, calls and Slack replies? | check-sql YES (01_Grounding_Dossier.md §1.E); brief §5a 32 of 32 YES; reach.brief PASS | YES; no ask reads another person's scoped data |
| C20 | counter to finding 1: "today" is a material contradiction | persona_today 2025-10-01 (Working_Files/00_Task_Context.json /universe/persona_today); the email says he flies on Oct 1 morning | true; relative wording Advisory only |
| C21 | is a failure or wait announced, or a route removed? | 03_Error_Async_Config.txt Friction: none | clean |
| C22 | are the touched records incoherent? | rev3 `/injection` PASS (Platform_Report/injection_report3, SQL 952e12a9ad7a); base_claims PASS in 01_Grounding_Dossier.md | clean |
| C23 | the same persona as the completed account-custody task | support/completed_tasks/frederick_account_handover_2026-10-26 shares only the persona (1 of 7 fingerprints); no supplied sample | clean (Advisory scope only) |
| C24 | is it just investigate and post one message? | three writes in Sheets/Drive, Trello and Gmail (brief §4) | clean |

Mechanics: every quoted span in Findings and Brief coverage was checked as an exact substring of 04_Prompt.txt (the gate re-verifies). The prompt hash was cecfad824fd8 before and after writing this report. The draft hash 649abf4249fb is superseded.

Unresolved: none. UNVERIFIED: none.

```
STAGE GATE prompt-check: PASS — Task_Authoring/task_inputs · 04_Prompt_Check.md#178d2ab8d334 · 04_Prompt.txt#cecfad824fd8 · 04_Prompt_Writing_Brief.md#9d1555e8eb21 · __context__#f1f763cb8cb4 · __assignment__#827e8afa884d · __policy__#dc4ab5df3cdd · __gate_policy__#0fc4bb90877f · __review__#4d8cad39fcaf · blocking 0 · warnings 0 · checks 25
[PASS] assignment.v3_context: Frederick Stone / Co-founder; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#9d1555e8eb21, 00_Assigments.md#8ae66b700bc2, 01_Grounding_Dossier.md#8f8a00131b96, 01_Universe_Inject.sql#952e12a9ad7a, 03_Error_Async_Config.txt#f71fee8ef19f, __context__#f1f763cb8cb4, __assignment__#827e8afa884d, __policy__#dc4ab5df3cdd, __gate_policy__#0fc4bb90877f, __review__#7b76769a8f79)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (107 words, sha256 cecfad824fd8)
[PASS] evidence.quoted_spans: 3 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 10 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 15/15 items carry a source pointer (min 100%)
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

- No Fail. Paste 04_Prompt.txt exactly as saved into `/prompt`, paired with `/injection`. Per GEN_EXECUTION §7, `/prompt` takes the task date, the prompt, all eight assignment fields and the SQL (01_Universe_Inject.sql, sha256 952e12a9ad7a). Do not supply 03_Error_Async_Config.txt (Friction: none) or reference files (none). `/injection` takes the task date and the SQL only.
- Task date for both: Oct 1, 2025 (synth-cut), the assignment's universe date.
- Any edit to 04_Prompt.txt (retyping it in your own words included) changes the hash: re-run `/create-prompt-writing check` after the final edit.
- Hold Oracle Events, the rubric and the baseline until `/injection` and `/prompt` both pass on SQL 952e12a9ad7a (learnings §46).

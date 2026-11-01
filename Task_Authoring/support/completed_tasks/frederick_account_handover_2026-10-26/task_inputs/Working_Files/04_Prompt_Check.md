# Prompt Check — fs-account-custody
> Prompt: 04_Prompt.txt · 104 words · sha256 99f0027b9989 · checked 2026-10-25 (revision 3, after the task-skill linter) against 04_Prompt_Writing_Brief.md (2026-10-25)
> Suggested wording allowed. Typos and capitalisation are not assessed (scored by /prompt §1.2).
> **Authorship note:** this text is the Claude draft from `/create-prompt-writing draft`, written at the user's explicit request
> (2026-10-25). The later edits, removing "this afternoon" (C20 below), "Arthur's rules" → "Arthur's handover rules" (finding 2) and the revision-3 rewrite for the task-skill linter (finding 6), were also made by Claude. V3 (`references/Docs/11_V3_Changes.md` §8)
> requires the human to write every word and screens prompts with an AI-text detector. The C-checks below judge the text. They do not
> clear the authorship rule, which the human must meet by retyping it in their own words. After that, re-run this check (the hash will change).

## Summary

Fail 0 · Non-fail 0 · Advisory 4 (C7 handover-rules reach, C16/§1.2 authorship, C16 three per-account judgements, C22 Unity two-org context and the CS-3 AppLovin payout point) · UNVERIFIED 0 · clean: C1 C2 C3 C4 C5 C6 C8 C9 C10 C11 C12 C13 C14 C15 C17 C18 C19 C20 C21 C23 C24.
Predicted /prompt band: NON-FAIL (3), from Cross-Service Coherence alone. `/prompt` run 2 on SQL c0b774238114 scored every prompt dimension 5 and Coherence 3 for CS-3 (AppLovin payout mails vs warehouse revenue; base data; no graded value changes), which the prompt rewrite does not touch. The rewrite fixes the platform task-skill linter (finding 6) and the run-2 Google Sheet advisory (finding 8).
Status: READY FOR /prompt on the C-checks. V3 authorship (the human retypes it) is still open; see the note above.

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C20 / C17 | Alignment with Today's Date · resolved (was a Non-fail risk in the first draft) | "Leonard messaged me in our DM about" | Eval 1 §2.8 Step 1: "the universe clock itself is UTC" | The first draft said "this afternoon". The ask is D05S58U4SAK/1759272012.507134 at 2025-09-30T22:40:12Z (3:40 PM PT); with the clock at 2025-10-01 00:00 UTC, "this afternoon" could resolve to Oct 1, after the clock (the same pattern as the last task's "yesterday" finding). The phrase is removed; the DM ask is the only one of its kind, so no time word is needed |
| 2 | C7 / C8 | Clarity · Advisory | "If Arthur's handover rules want anything else done once the sheet's ready, go ahead and do it" | Eval 1 §2.6 (delegated discretion is authorized when records hold the rule) | It triggers rule 7 (the socials checklist on 67cf1b506d78ad3c72e02a35) through the card Leonard points to (68dc406c7b0d03e53b334bab). A run could also read Arthur's engineering card (68dc42f3095ad95194a711ae) as "Arthur's rules", but that card says "My list, not Fred's" and asks only for KEEP/MOVE marks on engineering accounts, so no competing write follows. Applied: the prompt now says "Arthur's handover rules" |
| 3 | C16 / §1.2 | Contrived (AI-text) · Advisory | "Can you take it off my plate?" | Eval 1 Local Overrides ("a polished, LLM-sounding draft fails"); V3 §8 authorship | The text is model-written. Its register is plain with no spec triggers, but the detector, not this check, decides. The fix is the human retyping it in their own words |
| 5 | C22 | Cross-Service Coherence · resolved at `/prompt` run 2 (was FAIL 2; run 2 NON-FAIL 3 on CS-3 only) | "every marketing and UA account I'm on" | `/prompt` report 6ad90e95653f5d56cdc2d881_1 CS-1, CS-2 | The base warehouse showed no Sep 2025 Meta spend and $0 Unity cost (snowflake.json /tables/34, /tables/0) against persona-visible spend (C07C2866011/1759186080.203099; frederick.stone@harmonygames.co/1843428112007517388), and the ledger booked all ad revenue under AppLovin/MAX a month behind (/tables/38 FIN-000616). SQL c0b774238114 adds a note to the cash notes' money section (f_c612c0e68a27b3330eb46a) that explains both gaps and points to receipts, campaign state and the ad revenue by network, so the data no longer contradicts itself; the hub now names the Harmony Games board. The prompt text is unchanged and scored 5 on every prompt dimension |
| 4 | C22 | Cross-Service Coherence · Advisory | "every marketing and UA account I'm on" | `/injection` PASS report on ee8d4d0de1ff (advisories); Eval 1 Phase 3 | Base holds two Unity orgs; the sweep exports only the Harmony Games Inc org 20067043314233 (f_1191b7f8c96419e1f4dc88), while Fred was also invited to org 2475121799690 (C07C2866011/1728453730.535849). Rule 1 scopes the register to the sweep ("today's sweep folder"), so this is context, not a contradiction; `/prompt` could still mention it |
| 6 | C4 | Assigned Task Skill · resolved (platform linter "Prompt Task Skill Weak - V2" FAIL on revision 2) | "For each one, figure out who actually holds it, whether money's still moving on it, and what we should do with it." | Eval 1 §1.5; Taxonomy screen 10 (Analysis and synthesis) | Revision 2's "worked out, one row per account" read as enumeration. Revision 3 names the three judgements per account, in Leonard's own terms (D05S58U4SAK/1759272012.507134: "who actually holds it, whether money is still moving on it, and what we do with it"), so the reconciliation is visible without naming any source or answer |
| 7 | C16 | Contrived · Advisory | "For each one, figure out who actually holds it, whether money's still moving on it, and what we should do with it." | Eval 1 §2.7 (item-by-item deliverable contents is one spec-sheet trigger) | Three per-account judgements could be read as a content list. It is one limited tell at most (Fail needs two or more), and it repeats the requester's own ask; no columns, format or order are prescribed (rule 6 holds the columns) |
| 8 | C17 | Truthfulness · resolved (`/prompt` run 2 advisory) | "Put it all in a Google Sheet in the Company Ops folder" | `/prompt` run 2 Issue 2 | Revision 2 attributed the Google Sheet to Leonard ("He wants … in a Google Sheet"), but his DM says only "save the register in the Company Ops folder". The sheet is now Fred's own request |

## UGT readings

| Deliverable | Reading A | Reading B | Resolution and evidence |
|---|---|---|---|
| W1 register membership | the 13 in-scope exports of the sweep (dossier §9.2) | Fred's March logins sheet f_4521c272960dd1836a5196, or all 16 exports | Leonard's ask: "arthur's sweep from today is the list"; card rule 1 excludes stores and data tools (68dc406c7b0d03e53b334bab). One class |
| W1 actions | card rules + comment + Arthur's email (REVOKE 1 · TRANSFER 4 · KEEP 6 · CLOSE 2) | the Confluence page (never close), the 90-day remark, or the card without its amendments | the ask: "arthur's handover rules … decide the action" (D05S58U4SAK/1759272012.507134); the card replaces the Confluence page (68dc406c7b0d03e53b334bab desc); the comment and the email are newer sources on the same scope (68dc529406d8087e5a6b8403; frederick.stone@harmonygames.co/1844732985606656293). One class |
| W1 money | Leonard's cash-notes definition (f_c612c0e68a27b3330eb46a) | "paid in the last 90 days" (C07C2866011/1758739436.208417) | the card: "Money moving is whatever Leonard defined it as for the cuts"; the doc is newer (started Sep 25) and is that definition. One class |
| W1 destination | a Google Sheet in Company Ops d_21f9e11d43739eaef26b38 | the sweep folder or Fred's Drive | the prompt and the ask both name Company Ops. One class |
| W2 reply | reply in the DM D05S58U4SAK with TRANSFER count 4 and Node Media on Meta | a post in #executives | "a reply to him in that DM". One class |
| W3 checklist | checklist on 67cf1b506d78ad3c72e02a35 with TikTok, YouTube, X, Instagram | a new card, or nothing | rule 7: "Don't open a new card"; the prompt delegates "anything else" the rules want. One class |
| cheapest choice | mark every account KEEP and reply "0" | — | still needs the sweep, the card and Leonard's ask; it fails rule 5, so the delegation opens no low-effort route (Eval 1 §2.1 step 3) |

## Verification log

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| "Leonard" | person | leonard.hayes@harmonygames.co (`entity.py resolve`, brief §10) | one person, CEO |
| "messaged me in our DM" | channel / event | D05S58U4SAK/1759272012.507134 (im with EMPLOYEE_0008_SLACK_ID; check-sql YES) | matches |
| "getting the account handover sorted before we start letting people go" | event / state | D05S58U4SAK/1759272012.507134 ("I want every marketing + UA account you're on sorted before we start letting people go") | matches |
| "every marketing and UA account I'm on" | state | D05S58U4SAK/1759272012.507134 ("every marketing + UA account you're on") | matches |
| "who actually holds it, whether money's still moving on it, and what we should do with it" | state | D05S58U4SAK/1759272012.507134 ("who actually holds it, whether money is still moving on it, and what we do with it") | matches |
| "a Google Sheet in the Company Ops folder" | doc | d_21f9e11d43739eaef26b38 "Company Ops", Fred writer (check-sql YES) | matches; catalog gsheets_create_spreadsheet + gdrive_move_file |
| "reply to him in that DM with what he asked for" | write | catalog slack_send_message on D05S58U4SAK | feasible |
| "Arthur's handover rules" | doc | trello 68dc406c7b0d03e53b334bab (creator 2162c1ba310341bf318f48b7 = Arthur Blake); the ask: "arthur's handover rules are on the ops board" | matches |
| "anything else done once the sheet's ready" | write | rule 7 → trello 67cf1b506d78ad3c72e02a35; catalog trello_create_checklist + trello_create_check_item | feasible |
| clock | date | freeze 2025-10-01 00:00 UTC; latest seeded record frederick.stone@harmonygames.co/1844732985606656293 (23:21Z) | the prompt states no date |

## Brief coverage

| Brief item | Present in the prompt (quoted span) |
|---|---|
| A1 Leonard's account handover ask | "Leonard messaged me in our DM about getting the account handover sorted" |
| planned layoffs context | "before we start letting people go" |
| W1 scope trigger | "It covers every marketing and UA account I'm on." |
| W1 contents trigger (holders, money, action) | "For each one, figure out who actually holds it, whether money's still moving on it, and what we should do with it." |
| W1 destination | "Put it all in a Google Sheet in the Company Ops folder" |
| W2 destination | "then reply to him in that DM" |
| W2 contents trigger | "with what he asked for" |
| W3 trigger (rule 7, via incorporation) | "If Arthur's handover rules want anything else done once the sheet's ready, go ahead and do it" |
| writes asked of the agent | "Can you take it off my plate?" |

The §9 must-not-appear list was checked programmatically against the text. It contains no tool name, id, Node Media, TRANSFER, count, class,
action, checklist, card, Trello, socials, "Actually", "don't trust" or "go by the rules", and no Markdown or numbered steps.

## Self-review

**Eval walk (`Evals/1_Prompt_Eval.md`, Phases 1–3, against the text):** 1.1 persona → C3; 1.2 voice → C16; 1.3.1–1.3.4 → C15, C13,
C9, C14; 1.4 → C24; 1.5 → C4/C5; 2.1 → C6; 2.2 → C18/C19; 2.3 → C17; 2.4 → C12; 2.5 → C11; 2.6 → C7; 2.7 → C16; 2.8 → C20; 2.9 → C23;
Phase 3 → C21/C22. Every quoted span was checked programmatically as an exact substring of 04_Prompt.txt; the hash was 99f0027b9989
before and after this run. No-transcribable-sentence pass: the brief holds no draft sentence; this text came from draft mode at the
user's request (authorship note), so the retyping step stays with the human.

| Check | Counter-reading | Resolution (evidence) |
|---|---|---|
| C1 | Counter: 87 words is too short for 60+ calls | within 20–4,000; length comes from evidence breadth (13 exports, 8 services; manifest call_budget 60) |
| C2 | Counter: the assignment is incomplete | 00_Assigments.md has the five axes plus mode and date; the persona resolves to roster frederick_stone, frederick.stone@harmonygames.co |
| C3 | Counter: Leonard or Arthur should do this, not Frederick | the ask is addressed to Fred about accounts he is on (D05S58U4SAK/1759272012.507134); the cash notes give him "marketing, UA and socials" (f_c612c0e68a27b3330eb46a) |
| C4 | Counter: the platform linter judged the skill Marginal (enumeration, not analysis) | revision 3 states the three per-account judgements (finding 6); the records require reconciling 13 exports and their second tabs against amended rules and money evidence from four services (brief §1); `/prompt` run 2 scored Assigned Task Skill 5. Counter also: a DM reply alone does not exercise Analysis and synthesis | the register in d_21f9e11d43739eaef26b38 is the authored artifact, built from 13 exports, the rules and money evidence |
| C5 | Counter: no complexity lever lives in the prompt | Eval 1 §1.5 asks that a lever be load-bearing, not stated; Dynamic change lives in 68dc529406d8087e5a6b8403 and frederick.stone@harmonygames.co/1844732985606656293, Ambiguity in the second tabs (f_f7e7c5bf089029cee91175) |
| C6 | Counter: Unity could be SINGLE (Fred is only a Manager), a second final state | rule 2 counts every Owner/Admin; f_1191b7f8c96419e1f4dc88 lists three Owners → COMPANY-HELD → KEEP (brief §4b) |
| C7 | Counter: "anything else" is an open-ended vague verb (Major) | it is delegated discretion over a rule held in a record (rule 7, 68dc406c7b0d03e53b334bab); the engineering card yields no competing write (finding 2, Advisory) |
| C8 | Counter: the checklist is an untriggered card-only requirement | the prompt delegates "anything else" Arthur's rules want, and Leonard's ask incorporates those rules (D05S58U4SAK/1759272012.507134); the card states rules, not answers (`fact_check --no-leak` PASS) |
| C9 | Counter: "who actually holds it" hints that someone's claim is wrong, or "what he asked for" pre-solves the reply | "actually" is Leonard's own word in the ask (D05S58U4SAK/1759272012.507134) and names no person or claim; for the reply: it names no count, party or record; the contents stay in the hub and depend on W1 |
| C10 | Counter: naming "Arthur's handover rules" collapses discovery of the hidden authority | Leonard's own ask already names "arthur's handover rules … on the ops board"; the prompt adds no title, board name or id, and the comment and email stay hidden |
| C11 | Counter: the writes do not depend on the investigation | the register rows, the TRANSFER count and the checklist items exist only after the classification (brief §3) |
| C12 | Counter: one service would do | holders sit in Sheets (f_f7e7c5bf089029cee91175), rules in Trello (68dc406c7b0d03e53b334bab) and Gmail (frederick.stone@harmonygames.co/1844732985606656293), money in Docs, Slack and Snowflake (snowflake.json /tables/35); `HARDNESS GATE (normal): PASS` is pasted in the dossier |
| C13 | Counter: the checklist is a bolt-on | it serves the same handover and is required by the same card's rule 7 |
| C14 | Counter: "Google Sheet" or "DM" is a tool mention | natural product names (`prompt_qc_examples.md` row 103); no catalog function name appears |
| C15 | Counter: "and then a reply … once the sheet's ready" is a command list | it is the order of deliverables and who to tell (screen 24 skeleton, Eval 1 §1.3.1), not a method over sources |
| C16 | Counter: the three per-account judgements are a spec-sheet content list | they are Leonard's own ask (D05S58U4SAK/1759272012.507134), one limited tell at most, with no columns, format or order; rule 6 keeps the columns (finding 7). AI-text risk is Advisory (finding 3) |
| C17 | Counter: "Arthur's handover rules" misattributes the rules | the card's creator is Arthur (2162c1ba310341bf318f48b7, trello action 68dc406ceb6d064fd62b364f); every other span re-verified (Verification log) |
| C18 | Counter: a Sheet cannot be created inside a folder | gsheets_create_spreadsheet then gdrive_move_file (newParentId) to d_21f9e11d43739eaef26b38; trello_create_checklist and slack_send_message exist (catalog) |
| C19 | Counter: the agent must read Leonard's or Arthur's mail | every needed read is persona-YES (brief §5a, `reach.brief`); Fred holds his own copy of Arthur's email (frederick.stone@harmonygames.co/1844732985606656293) |
| C20 | Counter: "before we start letting people go" asserts a post-clock event | it is an undated future event (f_c612c0e68a27b3330eb46a "About two months"); the removed "this afternoon" was the only relative time (finding 1) |
| C21 | Counter: friction is hidden in the prompt | 03_Error_Async_Config.txt says Friction: none (error-async gate PASS); nothing is announced |
| C22 | Counter: the warehouse still disagrees with Slack, so coherence still fails | the warehouse cannot be overlaid, but the cash notes now state the gap and the sources to use (f_c612c0e68a27b3330eb46a; finding 5), which is the fix the /prompt report asked for. Counter also: the Unity two-org context or Arthur's contradicted summary is an incoherence | Arthur's summary is a person's mistaken claim, allowed context per the `/injection` PASS; the Unity point is scope context (finding 4, Advisory) |
| C23 | Counter: the scenario copies a calibration task | no sample was supplied (Eval 1 §2.9 N/A); account custody before layoffs differs from the earlier paid-UA true-up (support/completed_tasks) |
| C24 | Counter: this is just "investigate and post one Slack message" | three writes across Sheets/Drive, Slack and Trello (brief §4) |

Unresolved: V3 authorship. The human must retype the prompt in their own words, then re-run this check on the new hash. Keep the three elements (Leonard's DM ask; the Sheet in Company Ops and the reply in the DM; leave anything else the rules want to the assistant), and avoid a relative time word for the ask ("this afternoon", "today", "yesterday").

```
STAGE GATE prompt-check: PASS — Task_Authoring-2/task_inputs · 04_Prompt_Check.md#df246be8bb09 · 04_Prompt.txt#c0a69ac771e6 · blocking 0 · warnings 0 · checks 19
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#8e29ffcbf93c)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (104 words, sha256 99f0027b9989)
[PASS] evidence.quoted_spans: 8 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 9 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 10/10 items carry a source pointer (min 100%)
[PASS] structure.summary_band: summary band present
[PASS] structure.summary_status: summary status present
[PASS] tier.hardness: Normal Horizon → --profile normal: manifest present, hardness_gate PASS pasted in the dossier and current
[PASS] tier.hardness_rerun: hardness_gate --profile normal re-run on the current manifest + SQL: PASS
[PASS] review.counter_readings: 24 evidenced counter-readings (of 24 found; need ≥ 24) in 04_Prompt_Check.md
[PASS] review.coverage: self-review addresses all 24 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## Route

No Fail. Before submitting:
1. The SQL is unchanged (c0b774238114, `/injection` PASS), so no `/injection` re-run is needed.
2. Re-run `/prompt` with this `04_Prompt.txt`; the new hash shows the text changed.
3. V3 authorship is still the human's: if you retype it, keep the three per-account judgements, the Google Sheet as your own ask, the DM reply and the follow-on rules sentence, then re-run this check.
A `/prompt` FAIL is fatal, so fix the cause and re-run.

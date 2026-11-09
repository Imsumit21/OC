# Prompt Check — leonard_stockholder_closeout
> Prompt: 04_Prompt.txt · 134 words · sha256 45766344a3e4 · Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) · checked 2026-11-08 against 04_Prompt_Writing_Brief.md (2026-11-08) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

## Summary

Fail 0 · Non-fail 0 · Advisory 4 · UNVERIFIED checks: none · checks clean: C1, C2, C3, C4, C5, C6, C8, C9, C10, C11, C12, C13, C14, C15, C17, C18, C19, C20, C21, C22, C23
Predicted /prompt band: NON-FAIL (one base coherence item at 3; no Fail) · Status: READY FOR /prompt (paired with /injection on the current SQL)

rev2 (after /hardness FAIL 2 on the platform pre-check) keeps the prompt bytes and moves difficulty into the records: a delivery failure in Owen Baker's letter thread, Calvin Price's forward of Carta's Jan 23 update, Leonard's Feb 12 mail to 'Akin', and the advisor split left to the advisor table and the ledger. Cold rev2 reviews (research/rev2/attack_ugt.md, attack_coherence.md, delta_review.md and the blind fork sweep, coherence audit and run simulation in research/rev2/review/) settled every fork they raised in the records; the told rule now reads 'sent to them directly and delivered, ... (a post in a channel doesn't count)'. The rev2 local blind round (research/prompt_review_rev2/: main Eval 1, P1-P4, cold P1 and P2, Eval 0; all Opus 5.5 xhigh) ended NON-FAIL 3 on SQL 65b7c3ec814b: Unique Ground Truth 5 (16 forks settled in the records), Clarity 5, every other scored dimension 5 except Cross-Service Coherence 3 on one base lifecycle item (Brian Foster's Carta termination as of Dec 31, 2025 against his January Slack activity; no graded value reads it); Eval 0 PASS.

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C16 | Contrived · Advisory | "That's the holder sheet and the investor letter in my close-out folder" | Eval 1 §2.7 spec register (P4 DR-P4-1: meets at most 1 of 4 triggers) | seven writes in one comma chain; it lists writes and destinations, not contents, so it does not escalate |
| 2 | C7 | Clarity · Advisory | "the heads-up to Griffin" | Eval 1 §1.5 named destinations (P4 DR-P4-2) | the prompt names the recipient but not the thread; the notes doc names it: a reply to all on the partner's own Feb 12 Board position mail |
| 3 | C7 | Clarity · Advisory | "only the holder messages wait for me" | Eval 1 §2.6 send vs draft (P4 DR-P4-3) | Griffin is also a holder; the notes settle that its heads-up 'can go out once the sheet is done' |
| 4 | C24 | Diversity · Advisory | "Can you take care of all of it the way those lay it out?" | Prompt Writing 4.1 framing red flag (P4 DR-P4-5) | the 'go by the doc' framing with the wind-down backdrop; fine once |

## Fair readings

- **Holder sheet.** Reading A: a new sheet in the close-out folder, shared with Robert and Arthur Reading B: updating the draft 'Holder list (draft)' in the same folder Resolution: both accepted (§4b): same folder, contents and sharing
- **Holder messages.** Reading A: 14 drafts per the notes' rule, one to Enes for the family Reading B: three family drafts Resolution: settled by the reply under the list C0ADGSZKR3R/1770949310.220519
- **KPMG reply.** Reading A: sent reply to all with 243,757 and 9,295,636 Reading B: a draft, or today's 164,114 Resolution: settled: the project says 'Send KPMG's confirmation as a reply to all'; leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com> and its follow-up fix the date and the counting
- **Griffin heads-up.** Reading A: sent reply to all on leonard.hayes@harmonygames.co/1856958794180374704 asking for their preferred vote on the dissolution Reading B: a draft, or the resignation date Resolution: settled by the notes f_a37b403d5200d4f0a31d31
- **Board on the sheet.** Reading A: Leonard Hayes and Robert Reading B: Leonard alone, or the four in the financing documents Resolution: settled by Robert's reply on leonard.hayes@harmonygames.co/1856958794180374704: 'That leaves Leonard and me on the board'
- **Linear.** Reading A: Canceled 5, Todo 14, Done 7, 12 reason comments Reading B: reason comments only on Done issues Resolution: settled: 'On every issue with no note of its own, Canceled included, say why' (ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG))

Accepted outcomes are the brief's §4b and the sidecar `outcome_reviews.prompt-check` in Working_Files/00_V3_Authoring_Evidence.json.

## Verification log

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| "the holder project in Linear" | project | ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG) | exists, Leonard is lead; 26 issues |
| "my close-out notes doc" | doc | f_a37b403d5200d4f0a31d31 | Leonard owns 'Stockholder close-out notes' |
| "my close-out folder" | folder | d_601064334a0b493022fe83 | Leonard owns 'Stockholder close-out' |
| "my investor email draft in #winddown" | message | C0ADGSZKR3R/1770664700.848759 | Leonard's Feb 9 draft |
| "KPMG's audit request for Griffin" | mail | leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com> | FY25 request to Leonard |
| "from yesterday" | date | leonard.hayes@harmonygames.co/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@LV3PR19MB8524.namprd19.prod.outlook.com> | Fri Feb 13, 2026 08:48 PT; today Sat Feb 14 (00_Task_Context.json persona_today) |
| "the heads-up to Griffin" | thread | leonard.hayes@harmonygames.co/1856958794180374704 | Board position thread, Feb 12 |
| "the reply in #winddown" | thread | C0ADGSZKR3R/1770934638.035469 | Leonard's Feb 12 list |
| "I still owe everyone who holds our stock or options" | state | D04UC0UEN2V/1770665186.368229 | Leonard's promise; the Feb 12 list leaves the angels open |
| "as we wind down" | company premise | C05KNDCHAAG/1770839984.194409 | the Feb 11 shutdown announcement |

## Brief coverage

| Brief item | Present in the prompt (quoted span) |
|---|---|
| holder sheet | "the holder sheet" |
| investor letter | "the investor letter in my close-out folder" |
| letter source | "worked up from my investor email draft in #winddown" |
| holder messages as drafts | "the messages to holders as drafts in my Gmail" |
| Linear states and comments | "the Linear issues" |
| Griffin heads-up | "the heads-up to Griffin" |
| #winddown reply | "the reply in #winddown" |
| KPMG reply | "an answer to KPMG's audit request for Griffin from yesterday" |
| send vs draft | "Send the replies yourself, no need to check with me" |
| incorporation | "the way those lay it out" |

## Self-review

Walked `Evals/1_Prompt_Eval.md` Phases 1-3 against the prompt; every C-check has a result below. The prompt's hash was the same before and after this run; every quoted span is checked as an exact substring by this generator.

| Check | Result | Counter-reading (strongest argument the result is wrong) | Resolution (record, Eval §, case id) |
|---|---|---|---|
| C1 | PASS | 134 words is out of the 20-4,000 range | wc -w 04_Prompt.txt |
| C2 | PASS | an assignment field may be missing | 00_Task_Context.json has all eight fields; persona resolves in Evals/references/persona/roster.json |
| C3 | PASS | a co-founder and creative director may not own investor relations | D04UC0UEN2V/1770665186.368229; C0ADGSZKR3R/1770934638.035469; KPMG's yearly mail leonard.hayes@harmonygames.co/1817557789846606177 |
| C4 | PASS | the work reads as Finance or Ops rather than Executive | a founder's close-out with the board, the preferred vote and investors (research/prompt_review_rev1/P4.md assignment line) |
| C5 | PASS | the prompt carries the recipe | rules live in f_a37b403d5200d4f0a31d31 and the project; RULE_IN_PROMPT CLEAN (hardness_v2_check.py) |
| C6 | PASS | a fair reading is rejected | §4b and the sidecar accept both sheet routes; rev2 forks settled in records (research/rev2/attack_ugt.md N1-N4; Segerstrale gave PERSON_3336_EMAIL in D04UC0UEN2V/1694674255.630849) |
| C7 | PASS | an unpinned channel or a vague verb | advisories 2-3 above; destinations named; send vs draft in one line |
| C8 | PASS | an incorporated record is unreadable or hands over the answer | the project ec2ea957-fc8e-4958-b809-0fb735b1e916 and f_a37b403d5200d4f0a31d31 are Leonard-readable, unique and state rules only |
| C9 | PASS | the prompt names a finding | no holder, count, label or cause in the prompt |
| C10 | PASS | a hidden authority is named | the notes doc is named as the persona's own doc; the family reply, Robert's mails, the advisor table, the bounce, Calvin's forward and the Akin mail are not |
| C11 | PASS | no write depends on a finding | every write in §4 is fed by §3 (brief) |
| C12 | PASS | one service carries the task | Linear, Gmail, Slack, Drive family carry weight (dossier 1.A; hardness_gate extreme PASS) |
| C13 | PASS | a bolt-on ask | every ask serves the close-out the notes lay out |
| C14 | PASS | a tool or server name | product names only (Linear, Gmail) |
| C15 | PASS | a command list | a list of writes, no sequence (Eval 1 §1.3.1) |
| C16 | PASS | spec register or trap hint | advisory 1; P4 found no FAIL pattern |
| C17 | PASS | a false identifier or premise | verification log; research/prompt_review_rev1/P3.md (23 claims, no finding) |
| C18 | PASS | a write the catalog cannot do | gmail_create_draft, gmail_reply_to_message, gsheets, gdocs, gdrive, linear, slack writes in Evals/references/tools/catalog.json (P2) |
| C19 | PASS | a required scoped read is invisible | check-sql PASS on rev2 (plan/checksql.txt, 0 load-bearing rows hidden); the three rev2 carriers sit in Leonard's own mailbox |
| C20 | PASS | 'yesterday' is wrong in Pacific | KPMG mail Fri Feb 13 08:48 PT; persona today Sat Feb 14 |
| C21 | PASS | an injected failure is announced | 03_Error_Async_Config.txt Friction: none |
| C22 | Advisory | an inconsistency on touched records | one base low item: Brian Foster terminated as of Dec 31, 2025 in Carta and his letter (leonard.hayes@harmonygames.co_1856960532806250145) but active in Slack in January (C09UHHN6PFZ 2026-01 /4214); no graded value reads it (research/prompt_review_rev2/P2.md DR1, eval1_final.md) |
| C23 | PASS | a sample task is cloned | no samples supplied; P4 originality against guideline and taxonomy examples |
| C24 | Advisory | the task is one Slack post | seven write kinds; advisory 4 on framing only |

Calibration cases (Evals/references/rules/prompt_qc_cases.json, 15): none of the FAIL patterns matched (staged_errors, trap_hint_or_riddle, hidden_destination, audit_form, if_chain, false_state_premise, ugt_both_fair_figure); the PASS controls that apply matched (research/prompt_review_rev1/P4.md).

Unresolved: the platform /prompt and /injection run on the rev2 SQL as a pair; the new rules' landing rates are cold estimates (UNCALIBRATED) until a new unhinted pre-check.

## Route

No Fail: paste 04_Prompt.txt exactly as saved into /prompt, paired with /injection on the current 01_Universe_Inject.sql (the earlier platform /injection and /prompt PASS covered sha256 bc72db9c31e9; rev2 needs both again). /prompt and /injection ask the task date first: answer Feb 14, 2026 (normal). Then /create-humantime.


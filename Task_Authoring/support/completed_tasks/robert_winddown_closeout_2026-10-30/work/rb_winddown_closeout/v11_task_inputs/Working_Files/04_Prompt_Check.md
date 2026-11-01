# Prompt Check — rb-winddown-closeout
> Prompt: 04_Prompt.txt · 99 words · sha256 cfab17798d35 · checked 2026-10-28 against 04_Prompt_Writing_Brief.md (2026-10-28)
> Suggested wording allowed. Typos and capitalisation are not assessed (scored by /prompt §1.2).

## Summary

Fail 0 · Non-fail 0 · Advisory 2 (C20, C23) · UNVERIFIED 0 · checks clean: C1–C19, C21, C22, C24.
Predicted /prompt band: PASS. Status: READY FOR /prompt.

Revision: the first /prompt run (report 6adfee3f27ce6ca81b457137_1_prompt) failed C6 UGT, C7 Clarity and C22 coherence on universe records, not on the prompt text; the records were fixed (dossier Revision 4: rule 3, rule 8, rule 10, comments on ENG-2446/2452/2481/2454/2455) and this check re-run on the unchanged 04_Prompt.txt. The second /prompt run (6adfee3f27ce6ca81b457137_1_prompt (1)) passed every prompt dimension and failed only Cross-Service Coherence on AWS (costs tab 0 vs ledger); fixed in dossier Revision 7 (rule 8 + ENG-2455), prompt unchanged. The third run (6adfee3f27ce6ca81b457137_1_prompt (2)) again passed every prompt dimension and failed only Cross-Service Coherence (Vercel label, Confluence lifecycle, HG Costs header, Chase card); fixed in dossier Revision 8, prompt unchanged. An independent coherence audit of that SQL then found three more seeded claims contradicting base mail (Linear plan, QuickBooks card, OpenAI credits) plus Pond5's renewal date; fixed in dossier Revision 9, prompt unchanged. /injection run 6 then failed the HG Costs header UPDATE (the Drive xlsx bytes keep the old labels) while /prompt run 3 had failed the positional note, so rule 8 no longer reads the costs tab's month columns at all (dossier Revision 10), prompt unchanged. /prompt run 4 then found Workspace's cost only in a PDF, Unity Ads undecided, Zapier/Helpshift switch-over undecided, the Layer date and the Linear/DocuSign P&L gaps; fixed in dossier Revision 12, prompt unchanged.

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C20 | Today's date · Advisory | "on friday" | Prompt Writing §4.2 asks for absolute dates; /prompt §2.8 allows clear relative wording | relative day; resolves to Fri Feb 13 (the ask C0ADGSZKR3R/1771003267.448213); optional: 'on feb 13' |
| 2 | C23 | Originality · Advisory | "own the account close-out register" | /prompt §2.9 is N/A without supplied samples | no samples supplied; no guideline example shares the scenario (Combo Fighters launch, 133-PR register, RC-flag gate, art-canon handoff) |

## UGT readings

| Deliverable | Reading A | Reading B | Resolution and evidence |
|---|---|---|---|
| W1 register | a new sheet in Robert's Drive with the 28 rows and two totals (dossier §9.2) | a sheet inside the Wind Down folder | Robert cannot see or write d_e5caf6a8c630421942ee59 (persona_view NO); the ask asks for sharing, not a folder (C0ADGSZKR3R/1771003267.448213) — same acceptance class (§4b W1) |
| W1 rule set | Sunset's checklist + correction, SVB's card terms, the conventions doc | Sherwood's checklist (robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com>); the Growth/UA page (page_ua_vendor_closeout) | the ask names Sunset, SVB and 'the conventions doc I just put in the Wind Down folder' (C0ADGSZKR3R/1771003267.448213); Sunset is the signed provider (robert@harmonygames.co/1856956532017091340) — source identity settles it |
| W2 share | Leonard and Arthur as editors | commenter access, or folder sharing | the ask: 'share it with me and Arthur as editors' (C0ADGSZKR3R/1771003267.448213) |
| W3 Linear | Done on the 5 Closed rows, Canceled on the 20 excluded, comment on each of 45 | close every issue, or leave all open | the project description defines each state (3f0c6a52-ee13-4b1e-68e3-a74bcc33818a); the prompt's 'settle each of the linear issues like he asked' incorporates it |
| W4 new issues | one per added account (ElevenLabs, Meta Ads, AppLovin UA) | add rows only, no issues | the conventions doc rule 3 'add it' + the project is 'one issue per vendor' (f_1326e66bcabfda8fd29e4a; 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a); cheapest choice (no new issues) fails the project rule, so the delegation 'go with your read' does not open a low-effort route |
| W5 reply | thread reply with 11,045.13 / 1,249.04 and the three clashes | a longer clash list (Cursor request, Gusto change, card moves) | rule 10 of f_1326e66bcabfda8fd29e4a defines a clash as a #winddown decision Sunset or SVB would undo, excluding card moves and requests — one set |

## Verification log

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| "leonard asked me in #winddown on friday" | person / channel / date | C0ADGSZKR3R/1771003267.448213 (Leonard, Fri 2026-02-13 17:21Z; #winddown C0ADGSZKR3R, Robert member) | true |
| "own the account close-out register" | event | C0ADGSZKR3R/1771003267.448213 'can you own the account close-out register' | true |
| "before he archives anything on google after the 15th" | state / date | C0ADGSZKR3R/1770933903.645709 'archieve account on google after Feb 15'; C0ADGSZKR3R/1771003267.448213 'before I archive anything on Google' | true |
| "share it with him and arthur" | person | C0ADGSZKR3R/1771003267.448213; arthur.blake@harmonygames.co | true |
| "settle each of the linear issues like he asked" | event | C0ADGSZKR3R/1771003267.448213 'Settle each Linear issue as you go and leave a line on each'; 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a (ENG-2438…ENG-2483) | true |
| "reply to him in his thread with the two monthly totals" | event | C0ADGSZKR3R/1771003267.448213 'reply here with the two monthly totals'; f_1326e66bcabfda8fd29e4a rule 9 | true |
| "anything that clashes with what we already decided" | event | C0ADGSZKR3R/1771003267.448213 'anything in the plan that clashes with what we already decided' | true |

## Brief coverage

| Brief item | Present in the prompt |
|---|---|
| §4 W1 register | "build the register the way he wants it" |
| §4 W2 share | "share it with him and arthur" |
| §4 W3 Linear settling | "settle each of the linear issues like he asked" |
| §4 W4 new issues | "work through his ask and everything it points to" (incorporated through the conventions doc rule 3 and the project) |
| §4 W5 reply | "reply to him in his thread with the two monthly totals and anything that clashes with what we already decided" |
| §6 anchor A1 | "leonard asked me in #winddown on friday" |

## Self-review

Walked `Evals/1_Prompt_Eval.md` Phases 1–3 in order against 04_Prompt.txt (hash unchanged before and after this run); every quoted span above is an exact substring (asserted by the builder).

| Check | Counter-reading | Resolution (evidence) |
|---|---|---|
| C1 | Counter: field length | 99 words, inside 20–4,000 (taxonomy step 24) |
| C2 | Counter: assignment incomplete | 00_Assigments.md has all five axes; robert resolves to one roster entry (robert@harmonygames.co) |
| C3 | Counter: a co-founder wouldn't delegate this | Leonard asked Robert directly (C0ADGSZKR3R/1771003267.448213); Robert's own voice is short and lowercase (C0ADGSZKR3R/1770839322.836779) |
| C4 | Counter: a register is retrieval, not planning | the register decides an action, status and deadline per account under four rule sources and reports clashes (f_1326e66bcabfda8fd29e4a rules 4–6) — Planning and Decision Support; Corporate Ops |
| C5 | Counter: the prompt carries the recipe | rules live in f_1326e66bcabfda8fd29e4a, 698f48be4ba0affafbf153db, robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>; the prompt names none; Ambiguity, Dynamic Change and Multi-Source are load-bearing (brief §8) |
| C6 | Counter: two destinations for the register | UGT readings above: the Wind Down folder is unreadable for Robert (d_e5caf6a8c630421942ee59 NO); one acceptance class |
| C7 | Counter: 'go with your read' leaves writes open | it delegates judgement, not writes; every write is named in the ask (C0ADGSZKR3R/1771003267.448213); the cheapest reading still needs the discoveries (W4 row) |
| C8 | Counter: a pointed-to record might hand over answers | the ask states rules and columns, not cells (C0ADGSZKR3R/1771003267.448213); the conventions doc states rules (f_1326e66bcabfda8fd29e4a) |
| C9 | Counter: pre-solved by naming the register's contents | no account, total, rule or clash appears in the prompt (brief §9) |
| C10 | Counter: naming #winddown collapses discovery | #winddown holds the anchor itself (C0ADGSZKR3R/1771003267.448213); every hidden authority stays unnamed (698f48be4ba0affafbf153db, robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, f_1326e66bcabfda8fd29e4a) |
| C11 | Counter: no write depends on the investigation | the register, Linear states, new issues and the reply all carry findings (brief §3) |
| C12 | Counter: only Slack and Linear carry weight | 11 services carry weight (01_Hardness_Manifest.json services); HARDNESS GATE (long): PASS in the dossier |
| C13 | Counter: the asks are bolt-ons | all four writes come from one request (C0ADGSZKR3R/1771003267.448213) for one close-out |
| C14 | Counter: a tool is named | no function, parameter or server name; 'linear' and '#winddown' are product/channel names (prompt_qc_examples row 103) |
| C15 | Counter: the prompt scripts steps | it lists the deliverables in the order Leonard asked (screen 24 skeleton), not sources or method |
| C16 | Counter: spec-sheet register | no column list, format rule or markdown; one 'two monthly totals' echoes the ask (C0ADGSZKR3R anchor) |
| C17 | Counter: a premise is false | every span verified in the log above against C0ADGSZKR3R/1770933903.645709 and the anchor |
| C18 | Counter: a write is impossible | gsheets_create_spreadsheet, gdrive_share_file, linear_update_issue, linear_create_comment, linear_create_issue, slack_post_message exist (Evals/references/tools/catalog.json) |
| C19 | Counter: a scoped read is invisible | check-sql PASS for robert (dossier §1.E); Leonard/Arthur billing facts are relayed in unscoped Linear comments (e.g. cmt_8a420b3635db4a36f750) |
| C20 | Counter: 'on friday' / 'the 15th' are relative | Advisory only: both resolve to one window (Fri Feb 13, Feb 15) before/after the clock 2026-02-14T00:00Z |
| C21 | Counter: friction announced | 03_Error_Async_Config.txt is Friction: none; nothing to announce |
| C22 | Counter: touched records inconsistent | local injection gate PASS on SQL sha256 50f6a195de7e; the AWS cost no longer reads the costs tab (rule 8: own January ledger line), so the tab/ledger AWS gap is a known base issue nothing graded depends on; platform /injection pending (previous SQL be2477091995 passed, Audit-Report/0_injection_PASS_r7.md) |
| C23 | Counter: lifted from a sample | no samples supplied; guideline examples differ in scenario and entities (Advisory) |
| C24 | Counter: only investigate + one Slack post | four writes over Sheets, Drive, Linear and Slack (brief §4) |

Unresolved: none.

```
STAGE GATE prompt-check: PASS — Task_Authoring-2/task_inputs · 04_Prompt_Check.md#46ca188fe4cd · 04_Prompt.txt#4c4f0951f3c1 · blocking 0 · warnings 0 · checks 19
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#3f40e4ff81a7)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (99 words, sha256 cfab17798d35)
[PASS] evidence.quoted_spans: 2 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 6 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 7/7 items carry a source pointer (min 100%)
[PASS] structure.summary_band: summary band present
[PASS] structure.summary_status: summary status present
[PASS] tier.hardness: Long Horizon → --profile long: manifest present, hardness_gate PASS pasted in the dossier and current
[PASS] tier.hardness_rerun: hardness_gate --profile long re-run on the current manifest + SQL: PASS
[PASS] review.counter_readings: 24 evidenced counter-readings (of 24 found; need ≥ 24) in 04_Prompt_Check.md
[PASS] review.coverage: self-review addresses all 24 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## Route

No Fail: paste 04_Prompt.txt exactly as saved into /prompt, paired with /injection (SQL sha256 50f6a195de7e), with all five assignment fields and 'Friction: none'. Then /create-humantime.


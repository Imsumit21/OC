# Prompt Check — dd-q4-claims-register

> Prompt: 04_Prompt.txt · 180 words · sha256 76500140c70a · checked 29 Oct 2026 against 04_Prompt_Writing_Brief.md (29 Oct 2026)
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.

## Summary

- Fail: **0**
- Non-fail: **1** (C7, Minor: the summary's label form is representational)
- Advisory: **1** (C23: no supplied sample tasks, so `/prompt` §2.9 is N/A)
- UNVERIFIED: **0**
- Checks clean: C1, C2, C3, C4, C5, C6, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, C24
- Predicted `/prompt` band: **NON-FAIL** (one Non-fail, no Fail, no UNVERIFIED hard gate)
- Status: **READY FOR /prompt**

The prompt is 171 words, plain prose, first person, no markdown, no tool or server name, no id, no count, no root cause. It names the two anchors, the three rules by role, the four deliverable kinds, the claims review ticket and one future deadline. It asks for four writes, each depending on what the investigation finds.

## Findings

| # | Check | Dimension | Severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|---|
| 1 | C7 | Clarity | Non-fail | "Post the corrected counts in the thread where Leonard asked, broken out by status and by decision." | C7 (`04_Prompt_Writing_Playbook`; Prompt Writing §4.2; Eval 1 §2.6) | The channel and thread are pinned, but the label form of the summary is left open: a table, a list or prose carrying the eight numbers are all fair. §4b records the numbers as material and the labels as representational, so two runs can deliver different-looking summaries with the same result. It is a Minor, not a Fail: no second write is supported and the same destination and numbers are fixed. Suggested wording, if the human wants the form tighter: "Post the corrected counts in the thread where Leonard asked — the status totals and the decision totals, each labelled." |
| 2 | C23 | Originality | Advisory | "Leonard wants the Domino Delights product claims checked before the Q4 pack goes out." | C23; Eval 1 §2.9 | No sample tasks were supplied with this assignment, so `/prompt` §2.9 is N/A. The fingerprint (PM certifies a 13-line claims draft against production evidence, fills a register, posts counts, corrects a page, raises a ticket) matches no guideline or taxonomy example sentence, scenario or entity set. Advisory only. |

No other span is quoted because every other check is clean.

## Fair readings

**D1 register.** Reading A: fill the existing `Register` tab, one row per claim, using the seeded 12-column header (`gsheets:f_6b2c3d4e5f60718293a4b5`, SQL L124), statuses per the live-claim card, decisions and qualifiers per the wording card. Reading B: use the `Old register` tab, which already has 9 rows and looks complete, or create a new workbook. Resolution: B is rejected on source identity and scope — A1 says "the tab we already use", the Register tab carries the full header, and the Old register is a stale 9-row tab (SQL L125) whose own rows repeat the wrong "five coin bundles" and "live" Season Pass. The prompt's "in the tab we already use" is the same role pointer A1 uses, so B is a distractor, not a fair second outcome.

**D2 summary.** Reading A: reply in the mpim thread with the eight counts labelled by status and decision. Reading B: a new top-level message in the same mpim, or the same numbers in prose. Resolution: both accepted as representational under §4b; the destination (the thread where Leonard asked, `slack:C1CB3D58E38B/1759248600.000100`) and the eight numbers are material and identical. This is the source of finding 1.

**D3 page.** Reading A: replace the false status sentence with "Season Pass is not live" and list the three dropped claims. Reading B: append a correction note under the old sentence. Resolution: B is not fair — the prompt says "bring it in line", and leaving "All 13 product claims are live" (`confluence:page_q4_product_claims`, SQL L186) standing leaves the false statement in the external page. Same destination, different material result, so B is rejected by the prompt's own instruction.

**D4 ticket.** Reading A: create a new ENG issue naming the unsupported claims and link it to the claims review ticket. Reading B: post the same list as a comment on `linear:ENG-2375`. Resolution: both accepted; A1 says "put anything we can't support on the claims review ticket", and the register's action column records the follow-up either way. The material content (Season Pass, Collectibles, the live-ops engine, with evidence) is the same.

**Claim statuses.** Reading A: C06 NOT_LIVE, C10 TESTING, C11 OUT_OF_SCOPE, C13 QUALIFY. Reading B: C06 LIVE because `ENG-2136` is Done and `#1755` merged; C10 LIVE because `#1838` merged; C11 LIVE because the engine runs; C13 as written because the exact day does not matter. Resolution: B is settled by the incorporated rule, not by taste — `trello:68daad004f5e6d7a8b9c0d10` excludes merged/ticket state and puts a positive subset in Testing; `gmail:julia.lawson@harmonygames.co/1860000000000000001` limits the pack to player-facing claims and fixes the GDD launch dates. The later config comment (`linear:ENG-2136` comment, SQL L144) is the decisive record for C06.

## Verification log

Every proper noun, date, relationship and state premise in the prompt, looked up in this run.

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| "Leonard" | person | `entity.py resolve "Leonard Hayes"`; `slack:EMPLOYEE_0038_SLACK_ID`; `contacts:63fffeb4fab5233ed5bb73bf` | VERIFIED — Co-founder & CEO (Contacts) / Creative Director (roster); the only Leonard in the task |
| "Domino Delights" | product | `confluence:page_domino_gdd` (title and body); `snowflake.ANALYTICS.MARKETING.INSTALL_EVENTS` | VERIFIED — store title; internal codename Game of Dominoes |
| "the Q4 pack" | state premise | `slack:C1CB3D58E38B/1759248600.000100` ("before the Q4 pack goes out"); `slack:C1CB3D58E38B/1759255200.000200` | VERIFIED — the pack is the work in progress; the request is to certify it before it goes out |
| "My Q4 claims draft" | document | `gdrive:f_5a1b2c3d4e5f60718293a4` (owner Julia, modified 2025-09-30T15:40:00Z) | VERIFIED — the current 13-line draft; v1 is `f_5a1b2c3d4e5f60718293a5` (not named) |
| "what's actually live" | rule pointer | `trello:68daad004f5e6d7a8b9c0d10` (live-claim standard) | VERIFIED — the standard defines live/testing/not live |
| "the live-claim standard we agreed at the Q4 review" | rule + event | `trello:68daad004f5e6d7a8b9c0d10`; `gcal:evt_5c1a7e93b2d04f61a8e7b8` ("Q4 product claims review", 2025-09-29) | VERIFIED — both records exist and match the phrase |
| "the external wording rules product signed off on" | rule | `trello:68d672304f5e6d7a8b9c0d11` (External wording — product claims) | VERIFIED — LIVE/TESTING/NOT_LIVE wording, exact numeric values, owner |
| "the scope note Leonard sent" | message | `gmail:julia.lawson@harmonygames.co/1860000000000000001` (from leonard.hayes@, 2025-09-30T14:05Z) | VERIFIED — player-facing only; internal tooling to the appendix; GDD launch dates |
| "the conflict column" | register field | `gsheets:f_6b2c3d4e5f60718293a4b5` header row (SQL L124) | VERIFIED — column 10 is `conflict` |
| "the register" | document | `gsheets:f_6b2c3d4e5f60718293a4b5` ("Q4 Product Claims Register") | VERIFIED — workbook with Register and Old register tabs |
| "the tab we already use" | destination | `slack:C1CB3D58E38B/1759248600.000100` ("drop the register in the tab we already use"); SQL L124 | VERIFIED — same phrase in the request; the Register tab carries the 12-column header |
| "the thread where Leonard asked" | channel | `slack:C1CB3D58E38B/1759248600.000100`; `persona_view.py can-see julia_lawson slack C1CB3D58E38B` → YES | VERIFIED — 3-person mpim, Julia is a member |
| "The claims page on Confluence" | page | `confluence:page_q4_product_claims` (author `user_EMPLOYEE_0005`, updated 2025-09-29T10:00Z) | VERIFIED — page exists, Julia authored it, it is editable |
| "every claim is live" | state premise | `confluence:page_q4_product_claims` body: "All 13 product claims are live." | VERIFIED — accurate paraphrase; the page is still in that state at the freeze |
| "the claims review ticket" | ticket | `linear:ENG-2375` "Q4 product claims review", In Progress, created 2025-09-29T12:00Z | VERIFIED — one Q4 claims-review issue in the workspace |
| "the board on 14 October" | future date | `gdrive:f_d03044b385b94f24b21ff4` ("Harmony Games BoD Oct 14 2025", created 2025-10-10) | VERIFIED as a future deadline; the deck is post-freeze and is used only for the date, never described as existing |
| "before" (deadline relation) | relation | freeze 2025-10-01T00:00:00Z (`00_Task_Context.json`; `01_Universe_Inject.sql` line 3) | VERIFIED — the deadline is 13 days after the clock |

## Brief coverage

| Brief item (§4 deliverables, §6 triggers) | Present in the prompt (quoted span) |
|---|---|
| D1 register, one row per claim, all columns | "Fill in the register — one row per claim, every column, including whether we keep, qualify or drop it — in the tab we already use." |
| D1 destination, existing tab | "in the tab we already use" |
| D2 counts, thread | "Post the corrected counts in the thread where Leonard asked" |
| D2 form (status + decision counts) | "broken out by status and by decision" |
| D3 corrected page and dropped list | "The claims page on Confluence still reads as if every claim is live, so bring it in line and list what came out." |
| D4 follow-up ticket, linked to the review ticket | "Anything we can't support goes on a follow-up ticket linked to the claims review ticket, with the evidence." |
| R1 live-claim rule trigger | "using the live-claim standard we agreed at the Q4 review" |
| R2 wording rule trigger | "the external wording rules product signed off on" |
| R3 scope trigger | "the scope note Leonard sent fixes which claims belong in the pack" |
| R5 conflict trigger | "Where a claim's sources disagree, put both in the conflict column and say which one governs" |
| Deadline | "before the board on 14 October" |

## Self-review

| Check | Counter-reading (strongest argument it fails) | Evidence and resolution | Result |
|---|---|---|---|
| C1 | The prompt could exceed the field limit or be under 20 words | 171 whitespace-delimited words against the 20–4,000 field in `01_Prompt_Eval.md` | CLEAN |
| C2 | The prompt could drift from the eight assigned fields | Persona, role, function, competency, skill, type, mode and date all match `00_Task_Context.json`; the freeze is `2025-10-01T00:00:00Z` | CLEAN |
| C3 | The message might not sound like Julia or sit outside a PM's remit | Her Slack voice is short first-person declarative (`slack:C090N54TG79/1758689839.300009`); the work is the PM certifying her own draft and register (`gdrive:f_5a1b2c3d4e5f60718293a4`; `gsheets:f_6b2c3d4e5f60718293a4b5`). The CEO request is in `slack:C1CB3D58E38B/1759248600.000100` | CLEAN |
| C4 | Product Management may be only nominally exercised | The work is claim classification, wording, scope and prioritisation — product decisions, plus an authored register (`gsheets:f_6b2c3d4e5f60718293a4b5`) and page; Retrieval is exercised by 11 services | CLEAN |
| C5 | The prompt could carry the recipe or the complexity could be one lever only | Ambiguity (where the three rules live), dynamic change (the 18:00 correction) and multi-source (11 services) are all load-bearing; the prompt states no flag, cohort, count or classification | CLEAN |
| C6 | A second fair reading could be rejected | §4b accepts the summary form, the evidence form, the action form and the ticket-vs-comment variant; the rejected readings (Old register, new workbook) lose on A1 and the Register header (SQL L124–L125) | CLEAN |
| C7 | Two incompatible writes could both be supported | Only one destination per deliverable; the summary label form is open and recorded as Minor (finding 1), not a decision ambiguity | NON-FAIL (Minor) |
| C8 | A rule the prompt points at might not exist or not state the rule | Each authority is a single record and states the rule, not the answer: `trello:68daad004f5e6d7a8b9c0d10`, `trello:68d672304f5e6d7a8b9c0d11`, `gmail:julia.lawson@harmonygames.co/1860000000000000001` | CLEAN |
| C9 | "Anything we can't support" could pre-solve that some claims fail | It is a conditional destination for whatever fails, not a finding: it names no claim, no cause and no count; A1 uses the same wording (`slack:C1CB3D58E38B/1759248600.000100`) | CLEAN |
| C10 | The prompt names the claims page, which is also a finding surface | `confluence:page_q4_product_claims` is a deliverable to correct, not a hidden authority; the three rule homes and the correction reply are not named. No §5 "No" item appears | CLEAN |
| C11 | The task could be read-only or the writes could be bolt-ons | Four writes (`linear:ENG-2375` for the follow-up), each fed by the investigation: the register needs the classifications, the counts need the register, the page needs the dropped list, the ticket needs the unsupported set | CLEAN |
| C12 | Fewer than two services could carry weight | 11 services carry weight (Drive, Slack, Gmail, GCal, Docs, Sheets, Linear, GitHub, Trello, Confluence, Snowflake); facts are scattered and reconciled | CLEAN |
| C13 | A sentence could be deletable without consequence | Deleting any sentence removes a destination, a rule, a constraint or the deadline; the four asks serve one purpose, the Q4 pack in `slack:C1CB3D58E38B/1759248600.000100` | CLEAN |
| C14 | "Confluence" could count as a tool mention | Product names are clean (Prompt Writing §4.2; `prompt_qc_examples.md` row 103); no function, parameter or server name appears | CLEAN |
| C15 | The deliverable order could read as a scripted method | The prompt gives one check-before-acting constraint and the order of deliverables, not a source sequence or numbered steps; the destinations come from `00_Task_Context.json` scope, not a procedure | CLEAN |
| C16 | The request could read as a spec sheet or hint | Plain prose, no headings, no numbered steps, no format rule, no trap hint; "the tab we already use" is A1's own phrase in `slack:C1CB3D58E38B/1759248600.000100` | CLEAN |
| C17 | A tight identifier, state premise or narrative claim could be wrong | Every span in the verification log resolves: Leonard, Domino Delights, the draft, the three rules, the page, the ticket, the board date. "every claim is live" is a fair paraphrase of "All 13 product claims are live." | CLEAN |
| C18 | A write might not be cataloged, or the facts might not exist | `gsheets_values_update`, `slack_send_message`, `confluence_update_page`, `linear_create_issue` are in `Evals/references/tools/catalog.json`; every fact has a cataloged read; the register's 12 fields exist in the seeded header | CLEAN |
| C19 | A required read could be outside Julia's ACL | check-sql PASS on the 10 scoped seeds; `can-see` YES for `f_c57724584820a26f3bbe54` and the mpim; Gmail, Drive and Sheets rows are Julia's own; the rest are unscoped | CLEAN |
| C20 | A past event could be after the clock, or a future date could be asserted as done | All past facts are before 2025-10-01T00:00:00Z; "the board on 14 October" is the only future date and is stated as a deadline | CLEAN |
| C21 | The prompt could announce an injected failure or wait | `03_Error_Async_Config.txt` is `Friction: none`; the prompt mentions no failure, retry or wait | CLEAN |
| C22 | The touched records could be incoherent | `01_Universe_Inject.sql` carries an injection PASS with base_check PASS and fact_check PASS; no inconsistency was met in C17–C18 | CLEAN |
| C23 | The scenario could lift a supplied sample | No sample tasks were supplied, so `/prompt` §2.9 is N/A; the fingerprint matches no guideline example | ADVISORY |
| C24 | The task could be only "investigate and post one message" | Four deliverables over four services, with a 13-row register and a corrected page | CLEAN |

**Unresolved: none.**

```
STAGE GATE prompt-check: PASS — Task_Authoring/task_inputs · 04_Prompt_Check.md#0fa6838bb0db · 04_Prompt.txt#43059f2e4b58 · 04_Prompt_Writing_Brief.md#b9b69bd9ec9f · __context__#fee9c0ab9e8c · __assignment__#3f9540413be0 · __policy__#dc4ab5df3cdd · __gate_policy__#bf8e231eb5d9 · __review__#03b9933a2417 · blocking 0 · warnings 0 · checks 23
[PASS] assignment.v3_context: Julia Lawson / Product Manager; hard cap <70%; freeze 2025-10-01T00:00:00Z; shared source available; record dates and freeze-state evidence checked separately
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#b9b69bd9ec9f, 00_Assigments.md#f8550b78dd9d, 01_Grounding_Dossier.md#3a92d7fdeb22, 01_Universe_Inject.sql#bc3abbdfb1d8, 03_Error_Async_Config.txt#2253e9d33f13, __context__#fee9c0ab9e8c, __assignment__#3f9540413be0, __policy__#dc4ab5df3cdd, __gate_policy__#bf8e231eb5d9, __review__#9b8edbb53b2e)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (180 words, sha256 76500140c70a)
[PASS] evidence.quoted_spans: 2 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 11 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 17/17 items carry a source pointer (min 100%)
[PASS] structure.summary_band: summary band present
[PASS] structure.summary_status: summary status present
[PASS] tier.hardness: Normal Horizon → --profile normal: manifest present, hardness_gate PASS pasted in the dossier and current
[PASS] tier.hardness_rerun: hardness_gate --profile normal re-run on the current manifest + SQL: PASS
[PASS] review.counter_readings: 24 evidenced counter-readings (of 24 found; need ≥ 24) in 04_Prompt_Check.md
[PASS] review.coverage: self-review addresses all 24 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] handoff.pasted: pasted into the Self-review by --paste
```



## Route

No Fail. Paste `04_Prompt.txt` exactly as saved into `/prompt`, paired with `/injection`, using the GEN_EXECUTION §7 paste list (prompt, all eight assignment fields, the SQL, and the error/async config). The one Non-fail (C7 summary label form) and the one Advisory (C23, no supplied sample) do not block; acting on them is the human's call. If the text is edited, re-run this check: the header hash ties the report to the current 180-word text.

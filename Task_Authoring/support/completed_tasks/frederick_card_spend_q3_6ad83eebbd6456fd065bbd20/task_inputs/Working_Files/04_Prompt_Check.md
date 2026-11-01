# Prompt Check — fs-paid-ua-trueup
> Prompt: 04_Prompt.txt · 75 words · sha256 0b197d44d6af · re-checked 2026-10-22 (after /injection rev 5) against 04_Prompt_Writing_Brief.md (2026-10-22)
> Suggested wording allowed. Typos and capitalisation are not assessed (scored by /prompt §1.2).
> **Authorship note:** this text is the Claude draft from `/create-prompt-writing draft`, written at the user's explicit request
> (2026-10-22). The one later edit, "yesterday" → "on Monday", was also made by Claude at the user's request. V3 (`references/Docs/11_V3_Changes.md` §8, §12) requires the human to write every
> word and screens prompts with an AI-text detector. The C-checks below judge the text. They do not clear the authorship rule, which the
> human must meet by retyping it in their own words. After that, re-run this check, because the hash will change.

## Summary

Fail 0 · Non-fail 1 (C22, one base-metadata inconsistency) · Advisory 2 (C7 "Put it", C16/§1.2 polish and authorship) · UNVERIFIED 0 · clean: C1 C2 C3 C4 C5 C6 C8 C9 C10 C11 C12 C13 C14 C15 C17 C18 C19 C20 C21 C23 C24.
Predicted /prompt band: NON-FAIL (3), from Cross-Service Coherence alone. The prompt dimensions are all expected at 5, as the second `/prompt` run scored them. Re-check of revision 2: the previous Non-fail on "yesterday" (sha256 7108dccfcb10) is resolved by "on Monday".
Status: READY FOR /prompt on the C-checks. V3 authorship (the human retypes it) is still open; see the note above.

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C17 / C20 | Truthfulness · resolved (was Non-fail in revision 1) | "He asked me in #executives on Monday." | Eval 1 §2.8: relative words resolve against the universe clock, "the universe clock itself is UTC" | Revision 1 said "yesterday". With the clock at 2025-10-01 00:00 UTC, that resolved to Sep 30, the date of Leonard's follow-up reply (C07C2866011/1759255500.938286), not of his ask. Leonard asked on Mon Sep 29 (C07C2866011/1759176840.271025, 20:14Z, 1:14 PM PT). "On Monday" resolves to Sep 29 under both the UTC clock and the PT freeze (Tue Sep 30, 5:00 PM PT). No defect remains |
| 2 | C7 | Clarity · Advisory | "Put it in the Marketing tab of the Q4 board pack" | Eval 1 §2.6 (a vague object with no competing concrete write) | "it" could mean a single number rather than the register. The tab's header (f_0cd1e1402e8052d3d4e903 Marketing!A1:H1) and the rules doc's "Rows" clause (f_4591ef30be4f920ba1ed14) settle it, and Leonard's own message uses the same words. Optional: "Put the breakdown in …" (no trap is hinted) |
| 3 | C16 / §1.2 | Contrived (AI-text) · Advisory | "Can you pull it together for me?" | Eval 1 Local Overrides 2026-10-05 ("a polished, LLM-sounding draft fails"); V3 §8 authorship | The text is model-written. Its register is plain and has no spec triggers, but the detector, not this check, decides. The fix is the human retyping it in their own words |
| 4 | C22 | Cross-Service Coherence · Non-fail (one minor, base metadata) | "comment on the true-up card with the total for each bucket" | `/prompt` report 6ad83eebbd6456fd065bbd20 run 2 (DR2, DR5); QC form: Non-Fail for "a single, low-impact inconsistency" | Run 2 found two points. (a) The Adjoe contest email cited a "Singular export" with 212 Canada installs that AD_SPEND_DAILY lacks. v5's "From the invoice" wording then failed the invoice's flat $5.00 rate (`/injection` rev 7 advisory 1). SQL v6 drops the Canada claim: Leonard contests 2,401 invoiced vs 1,923 Singular installs, and Adjoe grants a partial $1,271.40 credit (frederick.stone@harmonygames.co/1830999337380347892). (b) The FINANCE_LEDGER comment "Signed cash movements including inflows." disagrees with its month-end-dated rows (snowflake.json /tables/38). That is base Snowflake metadata, which SQL cannot overlay. Run 3 added three more. (c) "12 Robert-only account-3125 receipts, $3,720.06": false positive. Each one is in Frederick's own mailbox with the same reference number and transaction ID (e.g. $596.00 Oct 24–26 [TAX_ID_13351] in frederick.stone@harmonygames.co/1814042565503776727). (d) The Android Nordics brief anachronism and (e) the iOS CA "last DD test" note are fixed in v7 (f_f017eafb1e59601f888460, f_9e4be4822ec79ce7ff5d17). Expected Coherence 3 if (c) is not repeated; the only full fix would be an admin overlay of the table comment |

## UGT readings

| Deliverable | Reading A | Reading B | Resolution and evidence |
|---|---|---|---|
| W1 register | rows per network, month, title and bucket in the Q4 pack's Marketing tab, plus the gap list under it | one total cell in the tab | Leonard's message points to his close rules (C07C2866011/1759176840.271025), and the doc's "One row per network, month, title and bucket" (f_4591ef30be4f920ba1ed14) is an incorporated authority. The tab header A1:H1 has row columns. One class |
| W1 register | the Q4 pack f_0cd1e1402e8052d3d4e903 | the Q3 pack f_9f7fb3ec09a20b2b6aa6da | source identity: the prompt names "the Q4 board pack". One class |
| W2 reply | reply in thread C07C2866011/1759176840.271025 with per-bucket totals | a new #executives post | "reply in Leonard's thread". One class (sending to the channel as well is fine, per brief §4b) |
| W2/W4 totals | net cost per bucket (Fundraising $3,485.20, Real UA $111,387.92) | gross spend (Fundraising $3,546.83) | the doc: a credit-paid charge "cost us nothing" (f_4591ef30be4f920ba1ed14). V3 §9 accepts gross shown beside net when net is identified (brief §4b). One acceptance class |
| W4 card | comment on 68dae1bc8ec7eb683dc15a8d | a description edit or a new card | "comment on the true-up card". One class |
| W3 mail | send the link to contacts 049f5555b01fd07b0f9d673c | share the sheet or save a draft | "send the link to our outside accountant", and the doc says no new sharing (f_4591ef30be4f920ba1ed14). One class |
| cheapest choice | quote Snowflake's $81,169 as one row | — | that fails the register rules and needs no discovery. The prompt allows no low-effort open choice, because every destination is pinned (Eval 1 §2.1 step 3) |

## Verification log

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| "Leonard" | person | leonard.hayes@harmonygames.co (`entity.py resolve`, brief §10) | one person, CEO |
| "the real paid UA number for the last twelve months" | event / state | C07C2866011/1759176840.271025 ("I need the real paid UA number for the last twelve months") | matches |
| "the data room" | doc | C07C2866011/1759176840.271025; folder d_b563e7f1e1608c4d36f3b0 | matches |
| "the Oct 14 board" | event | evt_bd61f3209523d19fdd6ba2 (2025-10-14T16:00:00Z, 9:00 AM PT, on Frederick's calendar) | future, allowed |
| "He asked me in #executives" | channel / event | C07C2866011 = executives; the hub @-mentions EMPLOYEE_0008_SLACK_ID (Frederick) | matches |
| "on Monday" | date | C07C2866011/1759176840.271025 at 2025-09-29T20:14:00Z, 1:14 PM PT, a Monday; clock 2025-10-01 00:00 UTC (Tue Sep 30 PT) | matches under both the UTC and the PT reading |
| "the Marketing tab of the Q4 board pack" | doc | f_0cd1e1402e8052d3d4e903 "Q4 Board Pack - Oct 14", tab Marketing (SQL L193–L199) | matches; Frederick is a writer (check-sql YES) |
| "Leonard's thread" | channel | C07C2866011/1759176840.271025 (reply_count 2) | unique |
| "the true-up card" | doc | trello 68dae1bc8ec7eb683dc15a8d "Data room - paid UA true-up" | unique |
| "each bucket" | state | trello 68c99c40e5d9eb6f3a988838 (Fundraising / Real UA) | matches |
| "our outside accountant" | person | contacts 049f5555b01fd07b0f9d673c, job "Outside accountant (bookkeeping and tax)" | the only accountant contact (brief §5a, `persona_view.py search frederick_stone contacts "accountant"`) |
| "send the link" | write | catalog gmail_send_message (to, subject, body) to contacts 049f5555b01fd07b0f9d673c | feasible |
| "reply in Leonard's thread" | write | catalog slack_send_message (channel, text, thread_ts) on C07C2866011/1759176840.271025 | feasible |
| "comment on the true-up card" | write | catalog trello_add_comment (cardId, text) on 68dae1bc8ec7eb683dc15a8d | feasible |
| "Put it in the Marketing tab" | write | catalog gsheets_values_update (spreadsheetId, range, values) on f_0cd1e1402e8052d3d4e903 | feasible |

## Brief coverage

| Brief item | Present in the prompt (quoted span) |
|---|---|
| A1 Leonard's paid UA true-up request | "Leonard needs the real paid UA number for the last twelve months" |
| W1 destination | "Put it in the Marketing tab of the Q4 board pack" |
| W2 destination | "reply in Leonard's thread" |
| W4 destination | "comment on the true-up card" |
| W2/W4 contents trigger | "the total for each bucket" |
| W3 recipient trigger (R11) | "send the link to our outside accountant" |
| deadline context | "the Oct 14 board" |
| writes asked of the agent | "Can you pull it together for me?" |

The §9 must-not-appear list was checked against the text. It contains no tool name, id, Snowflake, doc, brief, statement, Calm Play, top-up,
correction, total, "Actually", "don't trust" or "go by the rules", and no Markdown or numbered steps.

## Self-review

**Eval walk (`Evals/1_Prompt_Eval.md`, Phases 1–3, against the text):** 1.1 persona → C3; 1.2 voice → C16; 1.3.1–1.3.4 → C15, C13,
C9, C14; 1.4 → C24; 1.5 → C4/C5; 2.1 → C6; 2.2 → C18/C19; 2.3 → C17; 2.4 → C12; 2.5 → C11; 2.6 → C7; 2.7 → C16; 2.8 → C20; 2.9 → C23;
Phase 3 → C21/C22. Every quoted span was checked programmatically as an exact substring of 04_Prompt.txt. The hash was 0b197d44d6af before and after this run.
No-transcribable-sentence pass: the brief holds no draft sentence. This text came from draft mode at the user's request (see the authorship
note), so the retyping step stays with the human.

| Check | Counter-reading | Resolution (evidence) |
|---|---|---|
| C1 | Counter: too short for a Long-Horizon task | 75 words, within 20–4,000. Length comes from evidence breadth (Long Horizon §3). The honest minimum is 104 calls (01_Scenario_Design.md §9) |
| C2 | Counter: the assignment is incomplete | 00_Assigments.md has all eight V3 fields. The persona resolves to roster frederick_stone, frederick.stone@harmonygames.co |
| C3 | Counter: Leonard, the CEO, is the one who should do this | Frederick owns the card ("Frederick owns it", 68dae1bc8ec7eb683dc15a8d) and runs the networks (C07C2866011/1757961037.465799) |
| C4 | Counter: a chat reply alone does not exercise Analysis and synthesis | The register in f_0cd1e1402e8052d3d4e903 is the authored artifact, built from 116 records |
| C5 | Counter: no complexity lever lives in the prompt | Eval 1 §1.5 asks that a lever be load-bearing, not stated. Dynamic change lives in C07C2866011/1759255500.938286 and 68d195a805df8c30c455f99c, and the prompt carries no recipe |
| C6 | Counter: net vs gross totals are two final states | brief §4b accepts gross beside net when net is identified (V3 §9). The doc defines cost (f_4591ef30be4f920ba1ed14) |
| C7 | Counter: "Put it" is a Fail-level ambiguity | No competing concrete write is supported. Leonard's message uses the same words and the tab header fixes the rows (f_0cd1e1402e8052d3d4e903). Advisory |
| C8 | Counter: the prompt never tells the agent to follow Leonard's rules, so the doc's rules are unauthorized | The prompt delivers Leonard's request (C07C2866011/1759176840.271025), and that request names the doc and the buckets. Multi-hop incorporation is allowed (V3 §9). The doc states principles, not answers (`fact_check --no-leak` PASS) |
| C9 | Counter: "the real paid UA number" pre-solves that Snowflake is wrong | The phrase is Leonard's own (C07C2866011/1759176840.271025). It names no cause, record or count (brief §9) |
| C10 | Counter: naming "the Q4 board pack" collapses discovery | It is the destination, which V3 §8 says to name. The hidden authorities (f_4591ef30be4f920ba1ed14, 68c99c40e5d9eb6f3a988838) are not named |
| C11 | Counter: the writes do not depend on the investigation | All four writes carry values or a link that exist only after the register is built (brief §3; W2/W4 from W1) |
| C12 | Counter: one service would do | Amounts sit in Gmail (frederick.stone@harmonygames.co/1812262106647207041), Sheets (f_c34b364c50bf4ed59ae6ce) and Snowflake (snowflake.json /tables/38). Rules sit in Docs, Trello and Slack. `HARDNESS GATE (long): PASS` is pasted in the dossier |
| C13 | Counter: the accountant mail is a bolt-on | It serves the same close and is required by the doc's "When it's done" clause (f_4591ef30be4f920ba1ed14) |
| C14 | Counter: "#executives" or "the true-up card" is a tool mention | These are natural product and channel names (`prompt_qc_examples.md` row 103), not function names (catalog checked) |
| C15 | Counter: "then … Once the sheet is done" is a command list | It is the order of deliverables and who to tell (the screen 24 skeleton, Eval 1 §1.3.1), not a method over sources (C07C2866011/1759176840.271025 orders them the same way) |
| C16 | Counter: the prompt names four destinations, so it reads as a spec sheet | There are no per-deliverable contents, no format rules and no layout (Eval 1 §2.7). Destinations are named per V3 §8. The polish risk is recorded as Advisory (finding 3) |
| C17 | Counter: "on Monday" could mean a different Monday, or the ask may not have been on a Monday | Sep 29, 2025 was a Monday (computed), and the freeze is the next day (Tue Sep 30 PT / Wed Oct 1 UTC), so "Monday" is the most recent one. The ask is C07C2866011/1759176840.271025 at 2025-09-29T20:14Z, Monday in both zones. Every other span was re-verified (Verification log) |
| C18 | Counter: a threaded reply is not possible | slack_send_message takes thread_ts (catalog), and gsheets_values_update, trello_add_comment and gmail_send_message all exist |
| C19 | Counter: the agent must read Leonard's mail | Every needed read is persona-YES (brief §5a, `reach.brief` 22 ids). Leonard's copies (leonard.hayes@harmonygames.co/1843732571750794917) are not needed |
| C20 | Counter: "Oct 14 board" describes an event after the clock | It is a future meeting (evt_bd61f3209523d19fdd6ba2), a semantic future date, which is allowed |
| C21 | Counter: friction is hidden in the prompt | 03_Error_Async_Config.txt says Friction: none (gate PASS 7c92b9c20d3c). Nothing is announced |
| C22 | Counter: the remaining ledger-comment point is pre-existing base data, so it should not count | The QC form counts task-touched data including base, and the second `/prompt` run counted it (DR5). So keep it as one minor point (Non-fail), not clean. Counter to Fail: with the v6 email fix (frederick.stone@harmonygames.co/1830999337380347892), it is the only one left, and the form allows Non-Fail for a single low-impact inconsistency |
| C23 | Counter: the scenario copies a calibration task | No sample was supplied (Eval 1 §2.9 N/A). The billing-close scenario is unlike the shutdown and launch tasks (01_Scenario_Design.md §1 originality) |
| C24 | Counter: this is just "investigate and post one Slack message" | There are four writes across Sheets, Slack, Trello and Gmail (brief §4) |

Unresolved: V3 authorship. The human must retype the prompt, then re-run this check on the new hash. Finding 1 is fixed in this revision. If the rewrite changes the date wording, use a weekday or Sep 29, not "yesterday". SQL v7 needs a fresh `/injection` run; the ledger table comment is base metadata (one minor point left).

```
STAGE GATE prompt-check: PASS — Task_Authoring-2/task_inputs · 04_Prompt_Check.md#d2e4b094668f · 04_Prompt.txt#f2a3065d8017 · blocking 0 · warnings 0 · checks 19
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#ae315a9c5927)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (75 words, sha256 0b197d44d6af)
[PASS] evidence.quoted_spans: 4 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 8 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 15/15 items carry a source pointer (min 100%)
[PASS] structure.summary_band: summary band present
[PASS] structure.summary_status: summary status present
[PASS] tier.hardness: long-horizon → --profile long: manifest present, hardness_gate PASS pasted in the dossier and current
[PASS] tier.hardness_rerun: hardness_gate --profile long re-run on the current manifest + SQL: PASS
[PASS] review.counter_readings: 24 evidenced counter-readings (of 24 found; need ≥ 24) in 04_Prompt_Check.md
[PASS] review.coverage: self-review addresses all 24 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```







## Route

No Fail. Before submitting:
1. The human rewrites `04_Prompt.txt` in their own words (V3), keeping "on Monday" (finding 1) and optionally "it" with "the breakdown" (finding 2).
2. Re-run `/create-prompt-writing check`; the new sha256 shows the text changed.
3. Paste the saved `04_Prompt.txt` into `/prompt`, after a fresh `/injection` PASS on SQL revision v7 (sha256 c983da3d0a7d).
A `/prompt` FAIL is fatal in V2/V3, so fix the cause and re-run.

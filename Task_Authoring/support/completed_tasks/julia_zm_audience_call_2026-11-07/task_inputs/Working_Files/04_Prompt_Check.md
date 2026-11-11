# Prompt Check — julia_zm_audience_read (friend-session audience call) · rev7 re-check
> Prompt: 04_Prompt.txt · 132 words · sha256 c3da944d7da5 · checked 2026-11-08 against SQL rev7 merged draft 4cc82f1ac76e; re-bound 2026-11-09 to the installed 01_Universe_Inject.sql rev7 (sha256 3acbfad93f4a, injection gate PASS) and 04_Prompt_Writing_Brief.md (rev7 re-bind, prompt-writing gate PASS) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.
> Reviewer: Claude Opus 5.5 check-mode subagent. Scope: hardening report 01a §9–§11 prompt defect P1 (de-signposting), and the rev7 universe facts (Leonard's ask now lists only the asks; Julia's log note adds the late-form rule; Owen's Sep 30 20:40Z late mail adds 2 sessions not in the workbook; player jobs in Julia's Contacts). No SQL was executed; SQL, Evals/, claude/ were not edited.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## Summary

| Item | Value |
|---|---|
| Fail count | 0 |
| Non-fail count | 0 |
| Advisory count | 3 (#3, #4, #5) |
| Minor (Clarity, representational) | 1 (#6) |
| Closed in this revision | #1 (P1 "where the rules are"), #2 (workbook-completeness premise) |
| UNVERIFIED checks | C18 rendering (parentless Doc create, cataloged move exists); C22 portal /injection on rev7 not yet run (local injection gate PASS on 3acbfad93f4a) |
| Checks clean | C1, C2, C3, C5, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C19, C20, C21, C24 (C23 N/A) |
| Predicted /prompt band | PASS (worst case NON-FAIL on representational #6) |
| Status | READY FOR /prompt (rev7 SQL installed, brief re-bound; pair with /injection) |

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C10 / C16 | Contrived / discovery collapse · **Closed** | "his message says what he needs" | 01a §11 P1; Hardness v2 Part 8 | Was "lays out what he needs and where the rules are", which told the agent the request was a rule index. Rev7 ask (SQL L887, C090N54TG79/1759266627.418203) now holds only asks; the new span claims only that, which is true. |
| 2 | C17 / C16 | Truthfulness / hint · **Closed** | "fill in the register tab in my audience sessions workbook" | Eval 1 §2.3 state premise; §2.7 hint | Rev6 "the sessions are in my audience sessions workbook" and the proposed "i logged the sessions in my audience sessions workbook" both assert the workbook holds the sessions. Rev7 Owen mail (SQL L434, 2025-09-30T20:40Z) adds 2 sessions after the workbook's last edit (20:26:45Z, SQL L10): a false completeness premise that also invites stopping at the Log tab. Rejected the proposed wording; the workbook is now named only as the register's destination: no completeness claim, no hint that sessions are elsewhere. |
| 3 | C8 | Incorporation · Advisory | "close out the session tickets" | prompt-incorporation-v1 | Ticket + log row for late forms, and Done/Canceled close-out, live only in Julia's own log note (SQL L176, f_c691d577b8f837eb4f9eaa), which the prompt does not name and Leonard's ask no longer cites. Persona-owned standing procedure, readable, states instructions not answers; the Register header "one row per session" with a "ticket" column (SQL L342) also pulls the late sessions in. Rubric rows for the 2 new tickets rest on this; keep them weight ≤ 3 or confirm at /rubric. Not spelled out by design. |
| 4 | C6 | UGT · Advisory (settled) | "the friend sessions" | memory: clause-sweep collective labels | Label settles nothing; swept late sessions per rule: Ayşe Polat 33 friend, 0.3.40 store build, iPhone, no coaching, job teacher (SQL L1028) → counted; Daniel Hughes 38 neighbor (Leonard SQL L879: neighbours count), 0.3.127 (127), Pixel 8, no coaching, lawyer (SQL L1030) → counted. No rule leaves either open. |
| 5 | C4 | Competency · Advisory | "he wants to settle the cards earlier change on what players told us" | Eval 1 §1.5 | Unchanged from re-check 2: audience-segment read is defensible GTM. |
| 6 | C7 | Clarity · Minor (representational) | "tell brian in #zombie-design" | playbook C7 | Thread vs top level open; brief §4b W6 accepts both. |

## UGT readings

| Deliverable | Reading A | Reading B | Resolution |
|---|---|---|---|
| W1 register | all sessions incl. Owen's 2 late ones (Sep 30 20:40Z mail) | only the 60 Log rows | log note SQL L176 "Any form that comes in after this batch gets a ticket and a log row"; Register "one row per session" |
| W3 tickets | create 2 tickets, then close all per Done/Canceled | close existing 60 only | same log note; persona's own procedure |
| W2 call | casual 27 at 3.8333 vs RPG 18 at 3.5000 → hold (solver/truth.json on SQL 3acbfad93f4a) | keep from leaders' lean | criteria deck "Sessions decide" (SQL L360); gap 0.3333 past the 0.25 band |
| W5 reply | thread reply under C090N54TG79/1759266627.418203 | top-level post | "reply to him in his thread"; ask "reply here" |
| W6 Brian | C090N54TG79 post | DM | prompt and ask both say the channel |

No BOTH_FAIR_FIGURE. Rev7 counts/means come from solver/truth.json (injection stage owns them): 82 sessions, 45 counted; memo context panel 3.33 over 9 (void rule C090N54TG79/1758729919.603185) and retention 10.47 install-weighted mature D7 for cohort weeks on or after 2025-07-24 (f_4e21b203a62910bdae0353 note); re-run notes on the 13 build-1943 drops only (D05GU6L0XFH/1758913471.205816).

## Verification log

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| "leonard" | person | roster leonard.hayes@harmonygames.co; ask author EMPLOYEE_0038_SLACK_ID (SQL L887) | OK |
| "leonard asked me in #zombie-design" | event | C090N54TG79/1759266627.418203 @EMPLOYEE_0005_SLACK_ID, 2025-09-30T21:10Z | OK |
| "#zombie-design" | channel | C090N54TG79; persona_view can-see YES | OK |
| "his feedback note" | doc | base C090N54TG79/1758517286.431379; seeds SQL L873/L877/L879 "on the feedback note" | OK |
| "his message says what he needs" | narrative | SQL L887: call mapping, memo per roadmap card, reply here, tell Brian, scope | OK, no rule pointers |
| "my audience sessions workbook" | doc | f_43bc35baf77fd59f4e57b8 'ZM audience sessions', owner Julia (SQL L10) | OK |
| "the register tab" | doc | SQL L342 'Register' | OK |
| "my drive folder" | destination | d_8140f09bf9f1b94cb8ee2d, parent of the workbook (SQL L10) | OK |
| "close out the session tickets" | state | log note f_c691d577b8f837eb4f9eaa (SQL L176) | OK |
| "brian" | person | roster brian.foster@harmonygames.co (EMPLOYEE_0026_SLACK_ID in SQL L887) | OK |
| late sessions | state | julia.lawson@harmonygames.co/1844324114366762178 (SQL L434), check-sql PASS | not in workbook; prompt makes no claim |

## Brief coverage

| Brief item | Present in the prompt |
|---|---|
| §4 W1 register | "fill in the register tab in my audience sessions workbook" |
| §4 W2 memo | "write the memo he asked for and put it in my drive folder" |
| §4 W3 states + rev7 late tickets | "close out the session tickets" (late tickets via log note, by design) |
| §4 W5 reply | "reply to him in his thread with keep or hold" |
| §4 W6 Brian | "tell brian in #zombie-design whether the tutorial and level order work goes on" |
| §6 commitment | "give him one call, not a maybe" |
| §6 delegation | "you don't need my ok on any of it, post and update everything under my name" |
| §9 must-not-appear | none: no ids, tool names, counts, rule locations, late-session hint |

## Self-review

| Check | Counter-reading | Resolution (evidence) |
|---|---|---|
| C1 | 132 words is thin | field 20–4,000; sha256 c3da944d7da5 |
| C2 | assignment incomplete | 00_Task_Context.json eight fields; freeze 2025-10-01 |
| C3 | Leonard should decide | ask addressed to EMPLOYEE_0005_SLACK_ID (SQL L887) |
| C4 | reads as PM work | #5; C090N54TG79/1758569491.223089 |
| C5 | prompt carries the recipe | RULE_IN_PROMPT CLEAN (hardness_v2_check this run) |
| C6 | late sessions out of scope | #4 sweep; SQL L176, L1028, L1030 |
| C7 | "close out" = Done for all | log note SQL L176; #6 representational |
| C8 | late-ticket duty unincorporated | #3 Advisory; persona-owned f_c691d577b8f837eb4f9eaa |
| C9 | "came out of his feedback note" pre-solves | origin only; C090N54TG79/1758517286.431379 |
| C10 | "his message" names an index | rev7 SQL L887 holds no rule pointers |
| C11 | stop at one reply | six writes depend on verdicts |
| C12 | second service trivial | Contacts jobs (SQL L1028), Gmail late mail (SQL L434), Slack, Sheets, Linear |
| C13 | Brian post bolt-on | named in SQL L887 |
| C14 | "tickets"/"drive folder" as tool words | product nouns, prompt_qc_examples row 103 |
| C15 | deliverable order as a script | deliverable list only (§1.3.1) |
| C16 | "says what he needs" still signposts | plain reference to the ask (control-plain-request); no rule location |
| C17 | workbook premise false | removed (#2); SQL L10 vs L434 timestamps |
| C18 | Doc may not land in folder | gdrive_move_file in catalog.json |
| C19 | late mail not visible | check-sql PASS on julia.lawson@harmonygames.co/1844324114366762178 |
| C20 | relative dates | prompt has none |
| C21 | friction hidden | 03_Error_Async_Config.txt Friction: none |
| C22 | rev7 coherence | local injection gate PASS on 3acbfad93f4a (01_Grounding_Dossier.md); portal /injection pending (UNVERIFIED) |
| C23 | clone of a sample | none supplied |
| C24 | investigate + one message | Sheets, Doc, Linear creates/states, two Slack posts |

Calibration: K11 staged errors not matched; K31 trap hint not matched (rule pointer and completeness premise removed); K42/K44/K47 hidden destination not matched; K1/K43 audit form not matched; K44 if-chain not matched; K43 departed person not matched; K50 N/A; control-plain-request and control-named-destination matched.

Unresolved: C22 (portal /injection on rev7 not yet run); C18 rendering. Re-bound 2026-11-09: rev7 SQL installed (3acbfad93f4a; the SQL lines cited above, L10, L176, L342, L360, L434, L887, L1028, L1030, match the installed file) and the brief re-bound; no finding changed.

```
STAGE GATE prompt-check: PASS — Task_Authoring\task_inputs · 04_Prompt_Check.md#868dbceb864b · 04_Prompt.txt#c3da944d7da5 · 04_Prompt_Writing_Brief.md#5c85145c29b3 · __context__#50e89bdae5e1 · __assignment__#7709f2a35b0e · __policy__#dc4ab5df3cdd · __gate_policy__#6bbf415e008b · __review__#532ef0932275 · blocking 0 · warnings 0 · checks 27
[PASS] assignment.v3_context: Julia Lawson / Product Manager; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#5c85145c29b3, 00_Assigments.md#638de5aac707, 01_Grounding_Dossier.md#854cbb11bc06, 01_Universe_Inject.sql#3acbfad93f4a, 03_Error_Async_Config.txt#7174fb324883, 01a_Hardening_Report.md#cbb68eeabfe4, __context__#50e89bdae5e1, __assignment__#7709f2a35b0e, __policy__#dc4ab5df3cdd, __gate_policy__#6bbf415e008b, __review__#7343be0506e2)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (132 words, sha256 c3da944d7da5)
[PASS] evidence.quoted_spans: 6 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 7 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 11/11 items carry a source pointer (min 100%)
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
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## Route

- No Fail: paste 04_Prompt.txt exactly as saved into /prompt, paired with /injection on 01_Universe_Inject.sql (3acbfad93f4a). Task date: "Oct 1, 2025 (synth-cut)".

# Prompt Check — dg-beta-server-signoff
> Prompt: 04_Prompt.txt · 100 words · sha256 a0414d89216a · checked 2026-10-26 against 04_Prompt_Writing_Brief.md (2026-10-26)
> Suggested wording allowed. Typos and capitalisation are not assessed (scored by /prompt §1.2).

## Summary

Fail 0 · Non-fail 0 · Advisory 3 (C10, C23, C9-adjacent wording note) · UNVERIFIED checks 0 · checks clean: C1, C2, C3, C4, C5, C6, C7, C8,
C9, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, C24.

Predicted /prompt band: PASS. Status: READY FOR /prompt (paired with a fresh `/injection` on SQL f5a42cee0962, which fixes both /prompt coherence findings of attempt 6ad90ea979eb9e5d89f8879f: the prod branch now exists and the open-ticket comments are gone, dossier §13 Revisions 3–4).

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C10 | Discovery collapse · Advisory | Put the register in the beta sign-off folder | brief §5 F9; V3 §8 "Name the destination" | naming the folder removes the hop through card rule 6 → page_zm_beta_oct10 (budget −2 Confluence calls); the client-QA lookalike d_d71300168ca5dffa4db8b3 still competes. Kept on purpose: V3 asks that a destination the sender knows be named |
| 2 | C23 | Originality · Advisory | If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me | V3 §8 "Vary the work across a batch"; `/prompt` §2.9 N/A without supplied samples | the closing shape ("if X's rules want anything else done … go ahead, you don't need to wait on me") echoes the author's earlier Frederick task prompt (support/completed_tasks/frederick_account_handover_2026-10-26/task_inputs/04_Prompt.txt); the scenario, persona, entities and writes differ. Optional rewording: "and whatever his rules say should happen to the tickets that didn't make it to prod, just do it" |
| 3 | C9 | Investigation · Advisory (not pre-solved) | the tickets that aren't on prod | Eval 1 §1.3.3 | presupposes that some tickets may not be on prod; it names no ticket, count or cause, and Arthur's own ask already says "which ones aren't" (D05QQF7V404/1759266764.508127), so it adds no finding |

## UGT readings

| Deliverable | Reading A (best-supported) | Reading B (strongest alternative) | Resolution and evidence |
|---|---|---|---|
| W1 register | 17 tickets (brief §4b) in d_69fcebc484d472907b0b5c, on prod 2 / not 15 (hardening rounds 1–3, 01a_Hardening_Report.md §11) | B1: register of every ZOM ticket closed in September with a match3d-backend PR, ZOM-547/553 included, merged = on prod | card rule 1 + log row 1 (f_78bedc46245090a160d2dd), comment trello:68dbf1b73eba0ba580f67a6e, Arthur's reply-all in Leonard's thread douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>, Arthur's page reply comment_zm_beta_oct10_c2, the inline review comments harmonygames-Games/match3d-backend#46#rc_1, #38#rc_1 and #39#rc_1, doc f_470ae81236d5bd39045dc1 — the incorporated sources settle scope and on-prod (Eval 1 §2.1 step 2: incorporated authority) |
| W1 destination | "ZM Beta sign-off" d_69fcebc484d472907b0b5c | "ZM Beta sign-off - client QA" d_d71300168ca5dffa4db8b3 | the prompt says "the beta sign-off folder"; page_zm_beta_oct10 names Arthur's folder and says client QA keeps its own; Douglas is only a reader on the client one (check-sql) |
| W3 share | Leonard, commenter, on the register | share the folder, or as editor | Leonard's email "share it with me directly. Comment access please, I don't need to edit" (douglas@harmonygames.co/1844721277206562572) |
| W4 reply | DM D05QQF7V404: 2 on prod; the 15 keys | post in #zombie-match3d (C0880U9751A/1759253506.093318 asks for it) | the prompt and the ask both say the DM ("reply to Arthur in the DM"; "reply here"); posting in both is the same material result |
| W5 tickets | 15 tickets → Todo + comment naming the change to go out | move to In Validation (client card) or open new tickets; or ask Douglas first | card rule 5 (trello:68dabfe9bc2e8b969782e22d) "goes back to Todo … Same ticket, no new ones"; the client card is client-scoped (trello:68dac311754b38be05be7ea9); "no need to wait on me" settles act vs ask |

Cheapest-choice test (step 3): no choice is delegated; the row set, values and writes are all fixed by records, so no low-effort route exists.

## Verification log

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| Arthur asked me in our DM | event / person | D05QQF7V404/1759266764.508127 (Arthur → Douglas, 2025-09-30T21:12:44Z; check-sql YES) | TRUE |
| the server side of the beta sign-off | doc / event | D05QQF7V404/1759266764.508127 "the server side of the beta sign-off" | TRUE |
| before Thursday's go/no-go | date | D05QQF7V404/1759266764.508127 "for thursday's go/no-go"; page_zm_beta_oct10 "Go/no-go on Thursday Oct 2" | TRUE (future event, Thu Oct 2, 2025) |
| the beta sign-off folder | doc | d_69fcebc484d472907b0b5c "ZM Beta sign-off" (Douglas writer) | TRUE |
| his sign-off rules | doc | trello:68dabfe9bc2e8b969782e22d "Beta sign-off - server side" by Arthur (2162c1ba310341bf318f48b7) | TRUE |
| the register | doc | card rule 6 "The register goes in …" (trello:68dabfe9bc2e8b969782e22d) | TRUE (the rules' own word) |
| Leonard also emailed me about the go/no-go | event / person | douglas@harmonygames.co/1844721277206562572, subject "beta go/no-go thursday", from leonard.hayes@harmonygames.co | TRUE |
| what he asked for (Leonard) | state | douglas@harmonygames.co/1844721277206562572 "please share it with me directly" | TRUE |
| reply to Arthur in the DM | channel | D05QQF7V404 (im: Arthur, Douglas) | TRUE |
| tool names / ids / tickets | — | scan of 04_Prompt.txt (hg.py not needed: none present) | none present |

## Brief coverage

| Brief item | Present in the prompt (span) |
|---|---|
| A1 Arthur's beta sign-off ask | "Arthur asked me in our DM for the server side of the beta sign-off" |
| A2 Leonard's go/no-go email | "Leonard also emailed me about the go/no-go" |
| W1 register + destination | "Put the register in the beta sign-off folder" |
| W3 share (via A2) | "please handle what he asked for once the register is in the folder" |
| W4 DM reply | "reply to Arthur in the DM with what he asked for" |
| W5 ticket updates (via card rule 5) | "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too" |
| act vs ask | "no need to wait on me" |
| scope by Arthur's rules | "the way he laid it out" |

## Self-review

Walked `Evals/1_Prompt_Eval.md` Phases 1–3 in order against the text; every check has a result below. Hash before and after this run:
a0414d89216a (unchanged). All quoted spans were checked as exact substrings by the gate.

| Check | Result | Counter-reading (strongest case the other way) | Resolution (evidence) |
|---|---|---|---|
| C1 | clean | the field might reject a short prompt | 100 words, inside 20–4,000 (04_Prompt.txt) |
| C2 | clean | the assignment might be incomplete | 00_Assigments.md lists all five axes; douglas resolves to one roster entry (douglas@harmonygames.co) |
| C3 | clean | a backend engineer handing his own sign-off to an assistant could read as implausible | the ask is addressed to him (D05QQF7V404/1759266764.508127); delegating retrieval work to an assistant is the task frame (Eval 1 §1.1) |
| C4 | clean | Retrieval might not be central if the work is mostly judgement | per-ticket facts are retrieved from 73 Linear threads and 28 PR reads (01_Hardness_Manifest.json cohort); the rules decide mechanically once found |
| C5 | clean | no load-bearing complexity if the prompt carries the recipe | the prompt carries no rule; Ambiguity, Dynamic change and Multi-source live in records (brief §8; trello:68dbf1b73eba0ba580f67a6e) |
| C6 | clean | Reading B (merged = on prod; September window) could stand | incorporated card/doc/email settle it (UGT readings; f_470ae81236d5bd39045dc1) |
| C7 | clean | "take care of it" is vague | the concrete writes are named (folder, DM, tickets, Leonard); "the way he laid it out" points at the ask D05QQF7V404/1759266764.508127 |
| C8 | clean | "his sign-off rules" could point at two cards | the ask says the rules are on "the beta card on the roadmap board"; the server card is Arthur's and titled server side (trello:68dabfe9bc2e8b969782e22d vs trello:68dac311754b38be05be7ea9) |
| C9 | clean (Advisory 3) | "the tickets that aren't on prod" presupposes the answer | it names no ticket, count or cause; Arthur's ask already uses "which ones aren't" (D05QQF7V404/1759266764.508127) |
| C10 | Advisory 1 | naming the folder collapses discovery | only the Confluence hop; the cohort, rules and deploy records stay hidden (brief §5 F1–F15) |
| C11 | clean | the writes might not depend on findings | register, reply and ticket moves all depend on the per-ticket results (brief §3) |
| C12 | clean | only Slack might carry weight | 10 services (dossier hardness_gate: services_injected 10) |
| C13 | clean | Leonard's share could be a bolt-on | it serves the same go/no-go (douglas@harmonygames.co/1844721277206562572) and depends on the register |
| C14 | clean | "DM" or "folder" could count as tool mention | product words, not functions (prompt_qc_examples row 103 pattern) |
| C15 | clean | "Put … reply … go ahead … handle" reads like a sequence | the deliverables and who to tell — the screen-24 skeleton, not a method (Eval 1 §1.3.1) |
| C16 | clean | spec-sheet triggers | 0 item lists, format rules or reply formats (04_Prompt.txt) |
| C17 | clean | a premise might be false (Leonard "emailed") | verified: douglas@harmonygames.co/1844721277206562572 from leonard.hayes@harmonygames.co |
| C18 | clean | sharing or ticket moves might be impossible | gdrive_share_file, linear_update_issue, linear_create_comment in Evals/references/tools/catalog.json |
| C19 | clean | a needed read might be outside Douglas's view | all scoped reads YES (dossier §1.E check-sql PASS; D079SNE2TL4/1759256193.859279 can-see YES) |
| C20 | clean | "Thursday" might be past | Thu Oct 2, 2025 is after the Sep 30 freeze (page_zm_beta_oct10) |
| C21 | clean | friction might be announced | none configured (03_Error_Async_Config.txt Friction: none) |
| C22 | clean | touched records might be incoherent | `/injection` PASS on SQL f5a42cee0962 (report 6ad90ea979eb9e5d89f8879f); no inconsistency met in C17–C18 |
| C23 | Advisory 2 | the closing clause repeats the author's earlier prompt | no supplied sample; scenario/persona/entities/writes differ (support/completed_tasks/frederick_account_handover_2026-10-26/task_inputs/04_Prompt.txt) |
| C24 | clean | only "investigate + post one message" | five writes over Sheets/Drive, Slack and Linear (brief §4) |

No-transcribable-sentence pass: no sentence in the prompt states a rule, a value, a ticket or a location beyond the allowed anchors and the
folder (brief §6 anchor table).

Unresolved: none for the prompt; tool behaviours in brief §12 stay UNVERIFIED until the Opus pre-check and do not affect /prompt.

```
STAGE GATE prompt-check: PASS — Task_Authoring-2/task_inputs · 04_Prompt_Check.md#9b99574feb95 · 04_Prompt.txt#f5f6a459f6df · blocking 0 · warnings 0 · checks 19
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#70b6632b856b)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (100 words, sha256 a0414d89216a)
[PASS] evidence.quoted_spans: 3 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 8 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 10/10 items carry a source pointer (min 100%)
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

No Fail. Paste 04_Prompt.txt exactly as saved into `/prompt`, paired with the `/injection` PASS on SQL f5a42cee0962. The two Advisories are
optional: Advisory 2's rewording only varies phrasing; Advisory 1 is deliberate (V3 §8).

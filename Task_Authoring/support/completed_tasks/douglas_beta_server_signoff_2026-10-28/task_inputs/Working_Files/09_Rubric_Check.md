# 09 Rubric Check — Douglas beta server register (dg-beta-server-signoff)
Checked 2026-10-28 · Criteria 76 (builder minimum 5: ok) · Plan 2026-10-27 (09_Rubric_Writing_Plan.md)
JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass (76 objects, all five fields non-blank, category Outcome ×75 / Process ×1, weights in 1/3/5)
Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict

Defects found and fixed in 09_Rubrics.json during this check (before this report): C22–C32 used the possessive "The Agent's DM reply to Arthur…" (valid nonstandard form, Agent-Centric NON-FAIL) — rephrased to "The Agent tells / names … to Arthur in the DM reply"; C52 carried "(a redeploy)", which could fail a correct comment naming #41 without that word (overly_specific risk) — removed. Draft-time fixes: C9 no longer adds "and lists it as a row" (non_atomic risk); C20 names "the server sign-off register file" (self-containment); C22 dropped "of the 17" (embedded count shared with C2); C23, C33, C43 say "exactly".

/rubric round 1 (report 6ad90ea979eb9e5d89f8879f_3_rubric.md, FAIL 1, reviewed JSON sha256 1244870fbf2c) — Fix List applied verbatim (every item marked "checked"): R1 file-type lock removed; R3, R12, R24, R34, R44 "contractor" → PERSON_2967_GITHUB_USERNAME (swept: no "contractor" left; "Douglas" kept where used, GitHub /users/35 names PERSON_5760 "Douglas"); weights R10, R11, R34–R40, R42, R44–R51 → 5 and R15 → 1; R23, R51, R52 justifications as given; R43 → bare count guard; new R53–R57 (register exhaustive), R58–R63 (DM), R64–R69 (moves), R70–R75 (comments), R76 (Process order). Optional tidy-up also applied: evidence pointers SQL L6/L15/L57 (section banners) → L7/L16/L58. No other row changed.

## Coverage
| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |
|---|---|---|
| R1 the ask and its two reply items (ledger F1) | C21, C22, C23 | Covered — no reply fails C21; a wrong count fails C22/C23 |
| R2 in-scope set (17; ZOM-547/553 out, ZOM-436 in) | C2, C9, C22, C23, C33 | Covered — 18 rows fail C2; a register without a ZOM-436 row fails C9 |
| R3 server changes and on-prod per ticket | C3–C19, C53–C57 | Covered — on-prod column exhaustive (all 17), 5 sampled server-change cells, volume C2 |
| R4 register in the beta sign-off folder | C1 | Covered — client QA folder or own Drive fails |
| R5 DM reply contents | C21–C32, C58–C63 | Covered — count, volume and all 15 not-on-prod keys |
| R6 Todo + comment on each not-on-prod ticket | C33–C52, C64–C75 | Covered — one move row and one comment row per each of the 15 tickets, plus count guards C33, C43 |
| R7 share with Leonard as commenter, after the register is in the folder | C20, C76 | Covered — editor or no share fails C20; share before the move fails C76 |
Unauthorized criteria: none

## Findings
| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |
|---|---|---|---|---|---|---|---|
| 1 | C3 | as N (not on prod) | 3_Rubrics_Eval.md 2.9 negative scan | Contains "not", but it is a reported value (the on-prod verdict), not a prohibition — affirmative | P3, F31 | none | Note |
| 2 | C43 | exactly 15 ZOM tickets | rubric_sampling.md (volume control); /rubric Fix List R43 | Bare wrong-target count guard; per-ticket content graded in C44–C52 and C70–C75 | P43, F31 | none | Note |
| 3 | C17 | among the server changes of ZOM-487 | rubric_sampling.md (exceptions direct) | ZOM-487 also has a status row (C6); different column of the register, not a duplicate | P6, P17, F5 | none | Note |

## Overlap groups · Spot-check groups · Predicted all-fail
| Group / row | Members / basis | Shared condition / reason |
|---|---|---|
| G1 register on-prod column | exhaustive C3–C14, C53–C57 (17), volume C2 | exhaustive, not sampled — no cap applies |
| G2 register server-change column | samples C15–C19 (5), volume C2 | ≤ 5 samples |
| G3 DM not-on-prod list | exhaustive C24–C32, C58–C63 (15), count C23, on-prod count C22 | exhaustive |
| G4 Todo moves | one row per target C34–C42, C64–C69 (15), count guard C33 | exhaustive |
| G5 Todo comments | one row per target C44–C52, C70–C75 (15), count guard C43 (no Todo condition, so no cascade with C33) | exhaustive |
| Overlap groups | none | the same ticket in four deliverables shares a root cause, not an embedded acceptance condition (playbook set-level rule) |
| Predicted all-fail | 0 rows | every value is persona-reachable (plan Visibility proof: check-sql PASS, can-see YES); every write is cataloged; no friction |

## Dimensions
| Dimension | Count / % | Threshold | Status |
|---|---|---|---|
| Overall Rubric Quality | 0 Major · 0 Moderate · 0 Minor of 76 (0%) | Major ≤ 10%, Major+Moderate ≤ 15%, all ≤ 20% | PASS |
| Criteria Weights | 0 of 76 off (weights as set by the reviewer-checked Fix List; new rows carry the reviewer's weights) | ≥ 15% off by two or ≥ 30% off by one fails | PASS |
| Category Balance | 75 Outcome · 1 Process | zero Outcome fails | PASS |
| Process Rubrics | 1 Process row (C76, the prompt-stated order), valid | 2+ invalid fails; a missing ordering row is NON-FAIL | PASS |
| Agent-Centric Phrasing | 76 of 76 "The Agent" + action | any artifact subject or tool name fails | PASS |
| Negative Criteria | 0 prohibition-only titles | 1+ fails | PASS |
| Predicted all-fail | 0 | 1+ fails (harness tolerance 0) | PASS |
| Schema, accuracy, coverage, contradiction (repair gates) | all clean | any failure reported | PASS |

Threshold margin: one Major would be 1.3% of 76 rows.

Baseline replay (the six round-3 runs graded from their write payloads on all 76 rows): run scores 0.519 · 0.726 · 0.446 · 0.519 · 0.736 · 0.446 → average 56.5%, SD 0.121, pass@1 0/6, 3 failure patterns (largest 33%) — difficulty gates PASS. 17 criteria failed all six runs (C3 C4 C5 C18 C22 C23 C24 C25 C26 C33 C34 C35 C36 C43 C44 C45 C46), all tied to the inline review comments on #38, #39 and #46 (persona-reachable; run 3 opened #38 and #39) — genuine model failures for /create-allfail.

## Self-review
Walked 3_Rubrics_Eval.md Phases 1–5 in order; pre-verdict sweep (5.0): missing requirement — none; phrasing mismatch with the prompt — none; non-atomic — none after the C9 fix; category mislabel — none; over-specific — C52 fixed, none left; duplicate or cascade group — none; vague exemplar — none (scripted scan of all fields for "e.g.", "such as", "for example"); prohibition-only title — none.

Re-verified: every literal was re-read in this run or the previous stage from the SQL (parsed with base_check.parse_sql: L6, L15, L23, L30, L36, L49, L57, L71, L96, L156, L164–L713, L735–L880) and the base export via hg.py (linear data.json team_ZOM states and the 73-ticket window); the /oe PASS report independently confirmed the 17 rows, 2 Y / 15 N and every PR verdict.

| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |
|---|---|---|---|---|
| C1 | PASS | valid alternative: a Google Doc with a table in the folder | passes now — 'as a file of any type' (/rubric Fix List R1); near miss: the client QA folder d_d71300168ca5dffa4db8b3 fails (SQL L7, L9) | none |
| C2 | PASS | near miss: 18 rows (ZOM-547/553 kept) | fails 'exactly 17' (baseline runs 1, 3, 4, 6); a notes line on excluded tickets is allowed (F14) | none |
| C3 | PASS | valid alternative: ZOM-459 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C4 | PASS | valid alternative: ZOM-509 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C5 | PASS | valid alternative: ZOM-537 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C6 | PASS | valid alternative: ZOM-487 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C7 | PASS | valid alternative: ZOM-444 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C8 | PASS | valid alternative: ZOM-531 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C9 | PASS | valid alternative: ZOM-436 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C10 | PASS | valid alternative: ZOM-499 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C11 | PASS | valid alternative: ZOM-510 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C12 | PASS | valid alternative: ZOM-503 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C13 | PASS | valid alternative: ZOM-392 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C14 | PASS | valid alternative: ZOM-550 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C15 | PASS | valid alternative: ZOM-503's change in other words | the title names the change; a cell naming only the PR fails (run 2's ZOM-487 cell, F31) | none |
| C16 | PASS | valid alternative: ZOM-510's change in other words | the title names the change; a cell naming only the PR fails (run 2's ZOM-487 cell, F31) | none |
| C17 | PASS | valid alternative: ZOM-487's change in other words | the title names the change; a cell naming only the PR fails (run 2's ZOM-487 cell, F31) | none |
| C18 | PASS | valid alternative: ZOM-537's change in other words | the title names the change; a cell naming only the PR fails (run 2's ZOM-487 cell, F31) | none |
| C19 | PASS | valid alternative: ZOM-436's change in other words | the title names the change; a cell naming only the PR fails (run 2's ZOM-487 cell, F31) | none |
| C20 | PASS | valid alternative: editor access | Leonard asked 'Comment access please' (SQL L71); commenter is the requested state | none |
| C21 | PASS | valid alternative: thread reply under the ask | both alternatives named (D05QQF7V404/1759266764.508127) | none |
| C22 | PASS | near miss: 5 on prod | fails — runs 2 and 5 (F32) | none |
| C23 | PASS | near miss: 12 named | fails exactly 15 (F32); counted by ZOM keys per the R23 fix | none |
| C24 | PASS | valid alternative: ZOM-459 given by title | the row grades that ZOM-459 is named as not on prod; naming it as on prod fails (F32) | none |
| C25 | PASS | valid alternative: ZOM-509 given by title | the row grades that ZOM-509 is named as not on prod; naming it as on prod fails (F32) | none |
| C26 | PASS | valid alternative: ZOM-537 given by title | the row grades that ZOM-537 is named as not on prod; naming it as on prod fails (F32) | none |
| C27 | PASS | valid alternative: ZOM-487 given by title | the row grades that ZOM-487 is named as not on prod; naming it as on prod fails (F32) | none |
| C28 | PASS | valid alternative: ZOM-444 given by title | the row grades that ZOM-444 is named as not on prod; naming it as on prod fails (F32) | none |
| C29 | PASS | valid alternative: ZOM-531 given by title | the row grades that ZOM-531 is named as not on prod; naming it as on prod fails (F32) | none |
| C30 | PASS | valid alternative: ZOM-436 given by title | the row grades that ZOM-436 is named as not on prod; naming it as on prod fails (F32) | none |
| C31 | PASS | valid alternative: ZOM-503 given by title | the row grades that ZOM-503 is named as not on prod; naming it as on prod fails (F32) | none |
| C32 | PASS | valid alternative: ZOM-557 given by title | the row grades that ZOM-557 is named as not on prod; naming it as on prod fails (F32) | none |
| C33 | PASS | near miss: 16 moves | fails exactly 15 (F31) | none |
| C34 | PASS | valid alternative: ZOM-459 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C35 | PASS | valid alternative: ZOM-509 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C36 | PASS | valid alternative: ZOM-537 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C37 | PASS | valid alternative: ZOM-487 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C38 | PASS | valid alternative: ZOM-444 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C39 | PASS | valid alternative: ZOM-531 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C40 | PASS | valid alternative: ZOM-436 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C41 | PASS | valid alternative: ZOM-392 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C42 | PASS | valid alternative: ZOM-550 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C43 | PASS | non-atomic? 15 comment writes | bare wrong-target count guard, reviewer-checked (/rubric Fix List R43); content graded per ticket R44–R52, R70–R75 | none |
| C44 | PASS | valid alternative: ZOM-459's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C45 | PASS | valid alternative: ZOM-509's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C46 | PASS | valid alternative: ZOM-537's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C47 | PASS | valid alternative: ZOM-487's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C48 | PASS | valid alternative: ZOM-444's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C49 | PASS | valid alternative: ZOM-531's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C50 | PASS | valid alternative: ZOM-436's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C51 | PASS | valid alternative: ZOM-503's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C52 | PASS | valid alternative: ZOM-392's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C53 | PASS | valid alternative: ZOM-336 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C54 | PASS | valid alternative: ZOM-518 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C55 | PASS | valid alternative: ZOM-435 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C56 | PASS | valid alternative: ZOM-557 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C57 | PASS | valid alternative: ZOM-256 written in words (yes/no, on prod/not on prod) | the title states the meaning beside the letter (brief §4b); value re-derived from PR rows SQL L164–L713 and deploy log L23 (F31) | none |
| C58 | PASS | valid alternative: ZOM-336 given by title | the row grades that ZOM-336 is named as not on prod; naming it as on prod fails (F32) | none |
| C59 | PASS | valid alternative: ZOM-392 given by title | the row grades that ZOM-392 is named as not on prod; naming it as on prod fails (F32) | none |
| C60 | PASS | valid alternative: ZOM-518 given by title | the row grades that ZOM-518 is named as not on prod; naming it as on prod fails (F32) | none |
| C61 | PASS | valid alternative: ZOM-550 given by title | the row grades that ZOM-550 is named as not on prod; naming it as on prod fails (F32) | none |
| C62 | PASS | valid alternative: ZOM-435 given by title | the row grades that ZOM-435 is named as not on prod; naming it as on prod fails (F32) | none |
| C63 | PASS | valid alternative: ZOM-256 given by title | the row grades that ZOM-256 is named as not on prod; naming it as on prod fails (F32) | none |
| C64 | PASS | valid alternative: ZOM-336 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C65 | PASS | valid alternative: ZOM-503 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C66 | PASS | valid alternative: ZOM-518 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C67 | PASS | valid alternative: ZOM-435 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C68 | PASS | valid alternative: ZOM-557 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C69 | PASS | valid alternative: ZOM-256 to In Validation | card rule 5 names Todo (trello 68dabfe9bc2e8b969782e22d, SQL L58); In Validation is the client card's rule (T7) | none |
| C70 | PASS | valid alternative: ZOM-336's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C71 | PASS | valid alternative: ZOM-518's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C72 | PASS | valid alternative: ZOM-550's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C73 | PASS | valid alternative: ZOM-435's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C74 | PASS | valid alternative: ZOM-557's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C75 | PASS | valid alternative: ZOM-256's comment worded differently | wording delegated; the named change is graded (brief §4b W5; F31) | none |
| C76 | PASS | category: could an Outcome capture the order? | no — R1 and R20 show only the end state; the prompt states the order ('once the register is in the folder', 04_Prompt.txt); reviewer-checked Process row (/rubric Fix List R76) | none |
Unresolved: none for the criteria. The plan's diversity.authority_share finding (rules card) is a design note carried from prep, not a criterion defect.

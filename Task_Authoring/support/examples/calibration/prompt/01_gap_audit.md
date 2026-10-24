# Gap audit — Eval 1 (`/prompt`) vs playbook 04 check mode (v0 = playbook as found, Oct 3 22:29)

Status: M = missing, S = misstated, V = mis-severity, OK = covered. v1 column = the fix.

| Eval 1 check | v0 C-check | Status | v1 fix |
|---|---|---|---|
| Intake: all five axes; persona = exact roster entry (identity hard gate, §1.1) | none in check mode (brief only) | M | C2 (BLOCKED, not a prompt defect) |
| §1.1 Persona: role, voice vs own messages, access plausibility, responsibility scope | C12 | OK (thin) | C3 + "better-fitting colleague is not a Fail" (prompt_qc_examples) |
| §1.2 AI-text red flags (capitalisation, punctuation, rhythm) | excluded by design | boundary | C16 note: not assessed (GEN_EXECUTION §2); report states it |
| §1.2 polished connectives / enumerated specs | C17 | OK | C16 |
| §1.2 over-stacked = soft flag | none | M | C16 advisory |
| §1.2 incorporation (prompt-incorporation-v1: available, unique, states it, instructions not answer) | C4 (triggers) + C23 (named not located) | M (a, c, d) | C8 |
| §1.3.1 command list = FAIL | C17 "Fail / Non-fail (single tell)" | V | C15 Fail; skeleton exemption |
| §1.3.2 bolt-on | C16 | OK | C13 |
| §1.3.3 pre-solved incl. finding entity + presupposed counts | C5 (root cause only); C8 Non-fail for named items | V | C9 Fail for finding entity/count; C10 advisory for evidence location |
| §1.3.4 tool / parameter / MCP server / "X tool" = FAIL | C6 | OK | C14 |
| §1.4 diversity (flag) | none | M | C24 advisory |
| §1.5 competency + task skill hard FAIL; Authoring needs authored artifact; BF label mapping | C13 | S (no Authoring rule, no mapping) | C4 |
| §1.5 complexity dimensions + data seeding (hard gate row) | none | M | C5 |
| §2.1 UGT two-reading guardrail, strongest alternative, option inventory, five checks, contents not only destination | C2 (destination/recipient/act-defer only) | M (procedure), S (contents/selection) | C6 + UGT procedure |
| §2.2 A tool capability incl. format/export/deliver; UNVERIFIED ≠ FAIL | C22 | S (no UNVERIFIED) | C18 |
| §2.2 A1 Snowflake/Confluence live, unscoped; no re-run to prove | hard gate 3 "appears in the pre-check run" | S (pre-check runs after /prompt) | gate 3 fixed |
| §2.2 B data exists + §3.1 retrievable via catalog | C14 | OK (thin) | C18 |
| §2.2 C dimensional, D numeric observability | C21 | OK | C18 |
| §2.2 E ACL lens 1 + affirmative-denial exception; lens 2 | C14 + C20 | S (no exception) | C19 |
| §2.2 no middle band | C14 | OK | C18 |
| §2.3 tight identifiers, near-match trap | C11 | S (no near-match) | C17 |
| §2.3 state-premise verification (persistence/absence/window/ownership) | C11 "asserted event" | M | C17 |
| §2.3 hypotheses / requested outputs are not premises; absence evidence standard | none | M | C17 + absence rule |
| §2.3 meaning-changing typo (Samra/Samira) | forbidden by "never counts typos" | S | C17 carve-out (quote, no correction) |
| §2.4 cross-service ≥ 2, second non-trivial | C15 "design carries ≥ 10" in severity col | S (design target as QC fail; normal profile ≥ 7 missing) | C12 |
| §2.5 investigation + action (write required, fed by findings) | C15 (merged) | S | C11 |
| §2.6 clarity: ADA, delegation scan, minor band | C2/C3 | OK (scan thin) | C7 |
| §2.7 contrived indicators, spec-sheet ≥ 2 = FAIL, opaque IDs, call inflation, riddle exception (QC form) | C7, C17, C19 | S (severity bands mixed; no inflation; no riddle exception) | C16 |
| §2.8 date: material contradiction only; relative OK | C10 | OK; Docs stricter (absolute) | C20 advisory for relative |
| §2.9 originality fingerprint 7 elements, thresholds, guardrail | C18 "sentence copied … advisory" | S | C23 |
| §3.2 universe coherence on task-touched data; config alignment (forced error removes only route) | C9 (announcement only) | M | C21 + C22 |
| §4.1 aggregation; unresolved hard gate = NON-FAIL PARTIAL (does not clear) | report status BLOCKED/READY only | M | Summary: predicted band + UNRESOLVED |
| Doc references | `05_Prompt_Writing.md`, `09_Long_Horizon_Task.md`, `11_QC_Companion.md`, `12_Example_Task.md`, `QC_Spec_V2.csv`, `00_Taxonomy_V2_Step_Map.md` | S (files absent; Docs renamed to `6_Prompt Writing Guidelines - V2.md` …; QC CSV is `QC_Spec_Doc_Latest.csv`; step map never generated) | playbook cites existing files; GEN_EXECUTION outside edit scope |
| Brief breadth | "at least 2, target 3+, 3+ for Long" | S vs GEN_EXECUTION §3a (≥ 10 / ≥ 7) | fixed |

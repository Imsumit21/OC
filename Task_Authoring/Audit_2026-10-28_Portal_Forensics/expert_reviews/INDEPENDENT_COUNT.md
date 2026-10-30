# Independent delivery / Portal FAIL count

Review date: 2026-10-28. Scope: preserved files throughout `Task_Authoring/`, `completed_tasks/` and `archived task/`, plus the parent's separately verified mailbox evidence. No original artifact, report, skill or export was changed; no evaluation or outreach was performed.

## Decision

**Three distinct sent task IDs have a confirmed, attributable external FAIL: `TASK_A` (Reviewer A), `TASK_B` (Reviewer B), and `TASK_C` (Reviewer C).**

Reviewer D returned a genuine external FAIL, but it reviews a materially different scenario and expressly withholds the task ID. That makes **four FAIL-returning reviewers, with only three matched failed sent tasks**. Reviewer E's send is established but no returned report was located. This is a count supported by the located delivery histories, not proof that every historical communication channel or unknown task has been discovered.

Mailbox verification was performed by the parent, not independently repeated by this reviewer. Its message-level findings, Gmail links, historical search scope and negative-result limits are recorded in `evidence/MAILBOX_PROVENANCE.md:7–44`. I independently checked the corresponding preserved report bytes, verdict headings, input fingerprints, version comparisons and the broader filesystem census. The independent unique-hash set agrees exactly with `evidence/report_manifest.json`: neither set has an extra or missing hash.

## Counting rule

A qualifying task needs a located CB send, a returned external report with an explicit final `FAIL`, and evidence that the report concerns that sent task/scenario. Repeated reports, reruns and report copies count once at task level. A filename, folder suffix, attempt ID or local check does not independently establish delivery, task identity or use of a `/create-*` skill.

The governing report policy says to parse the single final verdict block, preserve NON-FAIL, and never default missing or malformed evidence to FAIL (`Evals/WORKFLOW.md:883–895`). FAIL can remain FAIL with PARTIAL execution when an independent defect was proved (`Evals/WORKFLOW.md:836–860`); this does not convert NON-FAIL/PARTIAL into FAIL. The three initial qualifying returns below are all COMPLETE. Portal operations are user-run and outside the local authoring pipeline (`Task_Authoring/setup/GEN_EXECUTION.md:13–14`, `:95–98`, `:494–513`).

## Five named CB deliveries

| Sent task ID | CB | Send → first qualifying return | Preserved report / exact verdict evidence | Count decision |
|---|---|---|---|---|
| `TASK_A` | Reviewer A | `1a1651bb5faa35cc` → `1a165886cf553937` | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_01_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_1_prompt.md:377` FAIL; `:379` score 2; `:381` COMPLETE. Hash **N1** below. | **1**. Local intake independently binds task, sender, Gmail message, attempt and report hash at `intake_provenance.json:2–22`. |
| `TASK_B` | Reviewer B | Corrected-address send `1a1651d8ff7b6ec0` → `1a16801780280b16` | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_01/prompt eval.md:451` FAIL; `:455` score 2; `:457` COMPLETE. Hash **Z1**. | **1**. Nonstandard filename is included. Report input hashes are at `:18–21`; the first bounced address does not substitute for the confirmed resend. |
| `TASK_C` | Reviewer C | `1a168c1b9bd234c8` → `1a168e821077954f` | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_01/6ad90e9fa38cc384483b1c80_0_injection.md:308` FAIL; `:312` COMPLETE. Hash **H1**. | **1**. Reviewed SQL is 229,131 bytes, SHA-256 `37fe6d8faedc059541a3746eeff9e23071793af254025909a8898748d8a057d7` (`:13`). |
| `TASK_D` | Reviewer D | Named ZIP in `1a1651bb5faa35cc` → `1a16ed677b050dd3` | `Task_Authoring/task_inputs_TASK_D/Audit-Report/20261024T165457Z_email_1a16ed677b050dd3/originals/6ad90e94adb09db24624b216_1a_hardness fail report current injection.md:122` FAIL; `:126` score 1; `:128` COMPLETE. Hash **M1**. | **Excluded from strict matched count.** Real report, unresolved sent-task attribution. |
| `TASK_E` | Reviewer E | `1a165b1d2f04e149` | No preserved external report in this task's Audit-Report; parent's exact-sender search found no incoming report in searched period. | **0 established failures**. This is an absence-of-located-evidence conclusion, not a PASS verdict. |

Source for sends, recipients, return origins and historical coverage: `evidence/MAILBOX_PROVENANCE.md:15–21`, `:30–44`. Library upload receipts and local `delivery_manifest.json` files prove preparation/upload only; they are not substitutes for a SENT Gmail message.

## Reviewer D identity and version exception

The returned hardness report says “attempt … (task ID withheld)” at line 5. Its prompt/SQL fingerprints are `527690cbc023ad5d68330b302257e231acf2e64b67a69b82e7fbe91da751ac3b` and `4e4b5243e220b9e589cace13dc58ec01cc927d54142b94a3a1a70bfa28d101f4` (`:18–19`). The sent snapshot records prompt `177495c38f62720e374af8c3c10bf0b863329a49756acb49291e61e49d3dcce2` and SQL `2decd123d847b5a89e246827c3df34d96026717583d875ce36c51d22e1c72a6e` (`intake_03_provenance_and_protected_hashes.json:14–23`).

The retained comparison explains PlayableX playable-ad restart kit → October store screenshot clearance, 117 → 239 mutations, zero overlap of parsed inserted identities, Hard → Medium, and a seven-hour freeze difference (`version_reconciliation.md:9–39`, hash **MC**). This is stronger evidence than a shared recipient or folder. The returned pair may be a redesign or a misattributed attachment; the evidence does not settle which. No fourth failed sent task is asserted. The cited trajectory is not present in this intake, so the reported 98 calls and all-correct outcome were not independently replayed.

## Independent complete filesystem census

I inspected 29 top-level task/assignment roots: 22 under Task_Authoring, three completed tasks and four archived tasks. I also checked the batch deliverable snapshots and all 702 Markdown/text members in the 13 ZIP archives beneath those three roots. No over-5MB Markdown/text members or nested archives were present. Report detection used actual final verdict headings, followed by provenance/location and full-byte hash checks; it did not require the standard filename.

The result is **84 distinct imported report byte streams** across eight local report-bearing groups. Their issued labels are **37 FAIL, 34 PASS, 13 NON-FAIL**. There are **89 primary imported-report paths**, plus **two byte-identical nested preservation copies** (91 extracted-file occurrences). ZIPs contain another 25 report members, all matching already-known report hashes; no ZIP adds a distinct report. These are report/copy counts, not task or delivery counts.

| Local group | Primary paths / distinct bytes | Distinct FAIL / PASS / NON-FAIL | Identity evidence and CB-count disposition |
|---|---:|---:|---|
| Reviewer A `…TASK_A` | 16 / 16 | 7 / 6 / 3 | Canonical task matched to CB delivery above. Multiple historical reviews do not add tasks. |
| Reviewer B `…TASK_B` | 31 / 27 | 12 / 12 / 3 | Canonical task matched above. Includes `prompt eval.md`, `injection eval.md`, and the root rubric `(10) (1)` duplicate. |
| Reviewer C `…TASK_C` | 8 / 7 | 4 / 3 / 0 | Canonical task matched above. Hardness report appears twice with identical bytes. |
| Reviewer D `…TASK_D` | 1 / 1 | 1 / 0 / 0 | Changed scenario, task ID withheld; strict-match exclusion above. |
| Current `Task_Authoring/task_inputs` | 1 / 1 | 1 / 0 / 0 | Julia Lawson / Retrieval assignment at `00_Assigments.md:15–25`, report attempt `6adfee3e0350cc55431db61d`; injection FAIL at report `:212`, COMPLETE at `:214`. Hash **J1**. No located CB-send binding. |
| `Task_Authoring/task_inputs-skipped` | 12 / 12 | 9 / 2 / 1 | Oliver Brooks / Season Pass, attempt `6ad576cdef355e00e72cd8b2` in `Plateform_reports/01_prompt.md:3–12`; assignment taskId blank at `00_Assigments.md:8`. Initial prompt FAIL `:374`, COMPLETE `:378`, hash **O1**. No located CB-send binding. Two extra nested preservation copies do not add bytes/tasks. |
| `archived task/task_inputs-n` | 5 / 5 | 1 / 2 / 2 | Arthur / Lot G. Prompt report `:16` explicitly distinguishes attempt `6acefd9770b8942247032c9e` from report-declared task `TASK_V`; FAIL `:435`, COMPLETE `:439`, hash **A1**. No located CB-send binding. |
| Completed Douglas beta server sign-off | 15 / 15 | 2 / 9 / 4 | Attempt `6ad90ea979eb9e5d89f8879f` in prompt report `:18`; FAIL `:371`, COMPLETE `:377`, hash **D1**. Completed README identifies these as platform reports (`README.md:5`). No located CB-send binding. |

The sixteen named current authoring folders without a preserved external report are suffixes `TASK_F`, `TASK_G`, `TASK_H`, `TASK_I`, `TASK_J`, `TASK_K`, `TASK_L`, `TASK_M`, `TASK_N`, `TASK_O`, `TASK_P`, `TASK_Q`, `TASK_R`, `TASK_S`, `TASK_E`, `TASK_T`. The other completed tasks (Frederick account handover; Frederick card-spend Q3) and archived folders `task_inputs-h`, `task_inputs-p`, `task_inputs-s` likewise add no preserved external report. This does not imply those tasks were never externally evaluated.

## Identity and duplication traps

1. **Current task_inputs is not automatically batch task …TASK_W.** `batch/priority.csv:2` points the older Frederick / Authoring task `TASK_W` to that path. Its retained batch assignment independently says Frederick and Authoring (`batch/deliverables/TASK_W/00_Assigments.md:13–20`, task ID `:69`). The current assignment says Julia / Retrieval. Do not attach Julia's new FAIL to …TASK_W using the reused folder name.
2. **An attempt is not a canonical task.** Reviewer D expressly withholds the task ID; Arthur's report prints separate task and attempt IDs. Several standard-looking 24-character filenames therefore identify attempts only.
3. **A local audit is not a Portal return.** The batch log itself records that local `/injection` and `/prompt` audits ran, and that a local Sonnet injection FAIL was refuted (`batch/ORCH_STATE.md:92–94`). Current Julia `Working_Files/*_review.md`, Reviewer B `iteration_32_rubric_eval_audit/Rubric_Audit.md`, Eval_Sandbox generated reports and evaluator templates remain excluded from the imported-report set.
4. **NON-FAIL stays NON-FAIL.** In particular, the seven imported OE reports contain four PASS and three NON-FAIL, zero FAIL. Pending/blocked statuses and later local predictions do not change this.
5. **An issued FAIL/PARTIAL remains historical FAIL.** Reviewer A rubric R5 report `…/iteration_16_rubric_portal_r5_20261026/6ad90e93a2c3542255f64fbf_3_rubric (4).md:120–122` is explicitly FAIL 2 / PARTIAL, hash `3d55dcfdf711cfc5c33203f250e31852a1fa7303176d41d2727df6589b9f0bcd`. It is not an extra task and does not support a claim that every FAIL report was COMPLETE.

The seven extra extracted-file occurrences collapse into these hash groups: Reviewer B rubric R10 `dd432e1e…` (2 paths); Reviewer C hardness `fe943934…` (2); Reviewer B prompt PASS `f8f56661…` (2); Reviewer B injection PASS `22d03950…` (2); Reviewer B hardness FAIL `d925b73c…` (2); skipped injection FAIL `4ac9782d…` (2); skipped injection FAIL `41a855cd…` (2). Full paths/hashes are retained in `scratch/independent_external_all_copies.json`; `scratch/independent_inventory_scope.json` records all 29 roots, 13 ZIP hashes and supporting-source hashes.

## Exact source SHA-256 ledger

Each key identifies the exact source already cited by path/line above. Full report membership, aliases and verdict lines are also in the independently produced `scratch/independent_external_candidates.json` and `scratch/independent_external_all_copies.json`; `scratch/independent_inventory_scope.json` records all 29 roots, 13 ZIP hashes and supporting-source hashes.

| Key | SHA-256 |
|---|---|
| N1 — Reviewer A initial prompt report | `7743fee5d4afc1a07a9e60da099cc84557afe6c0344945322b403eded19d2e84` |
| Z1 — Reviewer B initial prompt eval.md | `e3ad958a09b2a1bd790ba41af5acfd53846fd03d225b75c1545bd82dc3525297` |
| H1 — Reviewer C initial injection report | `f6209f142f3f32fa86dbb9538f5385a6c154c82e1f7b29112b0f9485af098d03` |
| M1 — Reviewer D returned hardness report | `c21b66ad2ca8100f90e031a6bc742e708daa3d5346718a1c27490dbd148b3157` |
| MC — Reviewer D version_reconciliation.md | `f3d6851c7bf6b4b276214515e082be7e32c215d55af4db17473d5406c8ff095c` |
| J1 — Current Julia injection report | `a49bdc3f66ac15a32cc6ea72796e960f1f5b22bff2e4e7843a6729ec8f6689c2` |
| O1 — Skipped Oliver initial prompt | `af23fa5a5820cada842787593014f6bd2ced90c6504cea1fef3efe7f8920af94` |
| A1 — Archived Arthur initial prompt | `16f32034ecc53bb8350c7bf83b95fbff776c253db2740773eed6b83cae86f304` |
| D1 — Completed Douglas prompt FAIL | `bc3d2c5e4d68cda189421fb5361a96f2d2c26efe5c712dda946b885ac16bece5` |
| Reviewer A intake_provenance.json | `e2724081aa676479139a2bf8c311f8fd0ae286429d1146bd3eedb01cf443864c` |
| Shared GEN_EXECUTION.md | `33eef06185ac35e9c53bbbbda780e81eb4a93f439dc1a0171c3ad19931acbf9b` |
| Evals/WORKFLOW.md | `be177e937fd285d57257cd9a1f025628243bbf122334ef94ffa499cb8e5e843d` |
| batch/priority.csv | `9032c3560d3ea05341cedef6a5b09f5d0c0f8e6688c28c9d2c1666948ee6b5b7` |
| Retained …TASK_W batch assignment | `cd4fffaa6dafd1d14d977d43cdfaff6354dd6e80e95f69da89489fecc894422b` |

## Remaining uncertainty

The strict count cannot be raised for Reviewer D without evidence establishing the changed return's task identity. No additional outreach is authorized for this audit. The other four local report-bearing groups contain real preserved FAIL labels, but no located contributor-delivery binding supports adding them to the CB count. Earlier October 16/17 sends do not establish qualifying failed returns; the parent's search found a Reviewer G thank-you with no report. Missing historical reports or communications outside the searched sources remain a coverage limit, not inferred failures.

Adversarial review of the full final synthesis is complete. Corrections, independently reproduced checks and remaining evidence limits are documented in `expert_reviews/ADVERSARIAL_REVIEW.md`; no material internal contradiction remains unresolved within the reviewed scope.

## OE EVALUATION REPORT

### Task: QA gate on the ZM store candidates (Android Submission #135 / iOS Submission #50): register tab, blockers on ZOM-570, a new ZM ticket for the unfiled runbook finding, the QA call in Arthur's #zombie-bugs thread
### Persona: Vincent Parker - Game Systems Engineer

Local run of `/oe` (Eval 2, oracle-events-v2) on the saved inputs: prompt (rev 6 text), task details (Vincent Parker, Engineering, Engineering Ops, Analysis and synthesis, long-horizon, easy), injection SQL sha256 5a8d9952…, error/async config (Friction: none), Oracle Events `Evals/task_inputs/08_Oracle_Events.md` (35 events, sha256 34878e63…). Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). No reference files.

### Phase 1: Structure & Alignment
- Derived critical path (from the prompt and its incorporated sources, before reading the OEs): Arthur's candidates thread → ZOM-570 and Leonard's push note → Leonard's "ZM submission rules" and Arthur's "How ZM submission builds are cut" → the tech-issues card (reuse rule, Leonard's #135 re-test) → the How we gate tab → the last gate's cut in #builds → the scope population (open ZM tickets any team or label, plus Done after 2025-09-22T12:30:43Z, minus ZOM-570 / ZOM-359 / ZOM-475) → every ticket's comments and description → cross-service checks (Vincent's #zombie-bugs post, Brian's DMs, vendor mail + contact, Douglas DM, match3d-backend PR #36, #builds after the Started lines) → runbook, Brian's matrix, update-path run, duplicate check → go/no-go time → writes: new ticket, new tab, register rows, ZOM-570 description, thread reply.
- Segments: 35 STEP · 0 CONTEXT · 0 RESPONSE_DESCRIPTION · 0 NON_ACTION. OE 12–18 are reasoning steps over the OE 10–11 reads; OE 31–35 are one write each.

### Phase 2: Accuracy
| Step | Field | Result | Evidence |
|---|---|---|---|
| OE 1–3 | all six | VERIFIED | SQL L118, L119 (thread parent and reply), L11–L17 (ZOM-570), L32 (Leonard's note) |
| OE 4–8 | all six | VERIFIED | SQL L221–L258 (docs, How we gate grid with the rev-18 clause, Sep 22 tab), L277–L278 (Trello) |
| OE 9, 25 | all six | VERIFIED | slack/messages/C05433XK267/2025-09.json /692–/696, /1120–/1132 (Started lines, #2027 / #2028 / #1759 Changes, #135 Changes without the season-pass fix) |
| OE 10–18 | all six (tool and parameters not applicable on the reasoning steps) | VERIFIED | linear/data.json /issues (112 open + 20 Done after the cut = 132), SQL L8–L29 (16 issue inserts), SQL L30–L87 (58 comments; 38 in-scope tickets carry comments) |
| OE 19–24 | all six | VERIFIED | SQL L116–L126 (Slack overlay), L129–L139 (vendor mail), L283 (contact), L287–L291 (PR #36), slack/messages/D079SNE2TL4/2025-09.json /260, /263, /265 |
| OE 26–30 | all six | VERIFIED | confluence_working.json /pages/7, SQL L259–L263, linear/data.json /issues/3490 (ZOM-424), SQL L216 |
| OE 31–35 | all six | VERIFIED | catalog entries linear_create_issue, gsheets_batch_update, gsheets_values_update, linear_update_issue, slack_send_message; every target exists at the clock |
- Numeric observability: every count recomputed from rows; every Slack time converted from its ts (calculation recorded); 9:00 AM PDT = 16:00Z − 7 h.
- Expected-value ledger: 798 values on Expected lines, 798 ledgered (0 unledgered), 0 absence claims; the created tab name is not_a_claim.
- Act-vs-defer: Slack (Vincent's channels and DMs, Sep 29 to the clock), Vincent's mailbox, ZOM-570 and its comment, the Trello card: no hold on any of the five writes; Arthur's "I'm holding the prod load until after the store push" (match3d-backend#36#rc_1) concerns the backend data load.

### Format & Standardization
| Step | Defect | OE text | Effect |
|---|---|---|---|
- No shape defects. Every OE is numbered, has one action, names its service, and has an Expected: line.

### Phase 3: Completeness
| Requirement | Covered by | Result |
|---|---|---|
| R1 identify the candidates and their Started lines | OE 1, OE 25 | COVERED |
| R2 the release ticket's background and the rules it incorporates | OE 2–OE 6, OE 8 | COVERED |
| R3 scope, a call and a build status for every ticket | OE 7, OE 9–OE 25 | COVERED |
| R4 the register in a new tab | OE 7, OE 32, OE 33 | COVERED |
| R5 blockers in ZOM-570's description | OE 34 | COVERED |
| R6 a new ZM ticket for the unfiled runbook finding | OE 26–OE 29, OE 31 | COVERED |
| R7 the QA call in Arthur's thread, before Friday's go/no-go | OE 1, OE 3, OE 30, OE 35 | COVERED |
- Path feasibility: SUPPORTED. Task solvability: SUPPORTED_BY_OE.
- Outcome-first mapping: the five writes are Outcome rows (the new tab and its 133 rows, the ZOM-570 description keys, the new ticket's subject and fields, the threaded NO-GO); reads map to the outcomes they feed; no Process row is needed.

### Issues Found
| # | Step | Issue | Component | Effect |
|---|---|---|---|---|
- None.

### Recommended Fixes
1. None required.

### Readability (advice only, no score impact)
- OE 10, OE 13 and OE 33 carry long key lists; they are deliberate (every register row has a retrieving event and a write). The events read goal-first, with values written out and traps named.

## Deep Recheck

Passes: O1, O2, O3 and a final adversarial pass, GPT-6.1 Sol (redteam / oracle agents), each a fresh subagent blind to the main review; O3 was not given the OE file. A parallel set of O1–O3 passes (research/oe/deep_recheck/) and a `verify` oracle-tier adjudication of its rejections (round 2 PASS) were also checked.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 35 events: every quote, time, count and key list; 41 of 85 no-call tickets; act-vs-defer | 0 | 0 |
| O2 | 61 derived requirements against 35 events | 4 | 0 |
| O3 | 3 open instructions, 31 items listed before its step limit | 0 mismatches | 0 |
| Final adversarial | 35 events: format, completeness, provenance, traps, reasoning steps | 2 advisories | 2 applied as wording changes |
| Parallel O1 | 35 events | 2 | 0 |
| Parallel O3 | register, blockers, runbook | 1 | 0 |
| Qualifier hunt (GPT-6.1 Sol) | 35 events, qualifiers only | 2 | 2 applied |
| Qualifier hunt (Opus 5.5) | 35 events, qualifiers only | 11 | 11 applied |
| O1a / O1b (Opus 5.5) | OE 1–17 / OE 18–35 after the fixes | 0 / 3 | 3 applied |
| Narrow final check (GPT-6.1 Sol) | the eight spans changed last | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | O2 | "File the bug with device, OS version, source build and repro steps, and link it here." | confluence_working.json page_qa_runbook | §3.3 Required writes | Completeness | REJECTED | The prompt incorporates the runbook's checks for the new-ticket ask only ("for anything the checks in the QA regression runbook turn up"); linking the bug on the runbook page is an unincorporated process rule (Evals/WORKFLOW.md prompt-incorporation-v1; /prompt rev18: "The QA Regression Runbook's checks are incorporated only for the new-ticket ask.") |
| DR2 | O2 | "Player-facing symptoms (lost progress, stuck splash, missing lives) should be mirrored to the" Customer Support Playbook | confluence_working.json page_qa_runbook | §3.3 Required writes | Completeness | REJECTED | Same authority: a support-playbook note is not a prompt ask; prescribing it would be an unauthorized write |
| DR3 | O2 | "QA posts the completed matrix in #god-bugs (Domino Delights) or #zombie-bugs (ZM3D)" | confluence_working.json page_qa_runbook | §3.3 Required writes | Completeness | REJECTED | The prompt's #zombie-bugs write is the QA call in Arthur's thread (OE 35); the matrix is Brian's and is not complete (update columns empty, SQL L261) |
| DR4 | O2 | "and links it from the release ticket" | confluence_working.json page_qa_runbook | §3.3 Required writes | Completeness | REJECTED | The prompt's ZOM-570 write is the blocker list in the description (OE 34); a matrix link is not asked |
| DR5 | Parallel O1 | "Match3D Android Submission - #127 - main  Success after 9 min 12 sec" (OE 9) | slack C05433XK267/2025-09.json /696 | O1 qualifiers | Accuracy | REJECTED | The OE already carries the record's double space |
| DR6 | Parallel O1 | "So the "green" covers fresh installs only." (OE 27) | SQL L261 (f_b91db376f65604b8602657) | O1 trap must be in a record | Accuracy | REJECTED | The matrix's only filled columns are the two fresh-install columns; both update columns are empty |
| DR7 | Parallel O3 | ZOM-506 FIXED / in candidate (OE 33) | SQL L121 "ZOM-506 zombie lane text ok"; linear /issues/3579 | O3 register | Completeness | REJECTED | ZOM-506 reports overlapping strings (a visible bug, not an art or layout ask) and Vincent saw it working on #135 / #50 |
| DR8 | Final adversarial | "the two existing tabs are unchanged" (earlier OE 32) | SQL L257–L258 | §1.2 segments | Format | APPLIED | Not a defect, but removed to avoid a non-action reading |
| DR9 | Final adversarial | "the issue list doesn't carry them" (earlier OE 11) | catalog.json linear_list_issues | O1 tool behaviour | Accuracy | APPLIED | Not contradicted, but unprovable from the catalog; removed |

| DR10 | Platform /oe (sha 3ddf0464) | "Pick out the latest checks on the open bugs that still fail" (earlier OE 14) | cmt_zom559_1 (SQL L45, #133), cmt_zom293_1 (SQL L87, July) | O1 qualifiers | Accuracy | APPLIED | Confirmed wrong qualifier; OE 14 now splits re-checked from not re-checked |
| DR11 | Qualifier hunts, O1a/O1b, own audit | OE 5, 7, 8, 9, 12, 16, 17, 18, 20, 25, 27, 29, 31, 33, 35 (see 08_OE_Check.md Findings 16–30) | SQL L18–L278; linear /issues; C05433XK267/2025-09.json | O1 qualifiers | Accuracy | APPLIED | Wording only: no call, build status or total changed |

Effect on verdict: unchanged. Every finding was rejected against the records or applied as a wording change before the record was saved; the record validates PASS 5.

- G1: Put the gate register in a new tab of my release gate sheet | ZM3D Release Gate, new tab | 133 items (132 in-scope tickets + the ticket filed in the gate) | Covered by: OE 10–OE 25, OE 31, OE 32, OE 33
- G2: add the blockers to the release ticket's description | ZOM-570 description | 19 items (18 existing keys + the new ticket) | Covered by: OE 14, OE 17–OE 25, OE 31, OE 34
- G3: file a new ZM ticket for anything the runbook checks turn up that nobody has filed yet | Brian's matrix (10 fresh-install cells, all Pass) and update-path run (4 rows, 1 FAIL) | 14 items (1 unfiled failure) | Covered by: OE 26, OE 27, OE 28, OE 29, OE 31
Scope: G1 (133 items) and G2 (19 items) each cover more than 15 confirmed items; both are enumerated in OE 10, OE 13, OE 33 and OE 34, so no item is uncovered.

Platform defects: none

### FINAL VERDICT: PASS
Score: 5
Execution status: COMPLETE
Completeness score: 5
Accuracy score: 5
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Review policy: oracle-events-v2
Reviewed OE SHA-256: 34878e63a31d732f6daaa46fc93a017cc12c54f3b972f42cc31ec61659f04a40
Review context SHA-256: 58f1022ae62603f8143454d2471ed30d449d6cfc32dce80403601b15aad85bf3
OE record SHA-256: 32578715494045172db3135ce11e8e08271a454f10e562781dfa15588895c2c1
Eval version: task-quality-v1
Eval release SHA-256: c5b89f4c40a7902f968001f1aa6c710d47bf203842455bbe8dbb668ec7c8943b
Evaluator model: Opus 5.5 (claude-opus-5-5), max effort; deep-recheck passes GPT-6.1 Sol
Next action: Type the 35 events into the platform Oracle Events field exactly as saved, then run /oe in Eval Portal
Evidence limits: Static universe/tool evidence; no live writes executed

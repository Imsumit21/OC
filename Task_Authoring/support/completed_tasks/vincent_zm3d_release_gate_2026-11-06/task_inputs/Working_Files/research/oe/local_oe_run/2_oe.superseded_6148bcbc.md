## OE EVALUATION REPORT

### Task: QA gate on the ZM store candidates (Android Submission #135 / iOS Submission #50) — register tab, blockers on ZOM-570, a new ZM ticket for the unfiled runbook finding, the QA call in Arthur's #zombie-bugs thread
### Persona: Vincent Parker - Game Systems Engineer

Local run of `/oe` (Eval 2, oracle-events-v2) on the saved inputs: prompt (rev 6 text), task details (Vincent Parker, Engineering Ops, Analysis and synthesis, long-horizon, easy), injection SQL sha256 5a8d9952…, error/async config (Friction: none), Oracle Events `Evals/task_inputs/08_Oracle_Events.md` (35 events, 33,515 characters). Universe synth-cut; clock 2025-10-01 00:00 PT (07:00 UTC).

### Phase 1: Structure & Alignment
- Derived critical path (from the prompt and its incorporated sources, before reading the OEs): Arthur's candidates thread → ZOM-570 and its push note → Leonard's "ZM submission rules" and Arthur's "How ZM submission builds are cut" → How we gate tab → the last gate's cut in #builds → the scope population (open ZM tickets + Done after the Sep 22 cut, named exclusions) → every ticket's latest check (Linear comments, #zombie-bugs, Brian's DM, the vendor mail, Douglas's DM, PR #36, #builds Started lines) → runbook rule, regression matrix, update-path doc, duplicate check → deadline → five writes (create the ticket, add tab, write 133 rows, ZOM-570 description, threaded reply).
- Segments: 35 STEP · 0 CONTEXT · 0 RESPONSE_DESCRIPTION · 0 NON_ACTION. OE 12–18 are reasoning steps over OE 10–11 reads; OE 31–35 are one write each.

### Phase 2: Accuracy
| Step | Field | Result | Evidence |
|---|---|---|---|
| OE 1–3 | all six | VERIFIED | SQL L118, L119 (thread parent + reply), L11–L17 (ZOM-570), L32 (Leonard's note) |
| OE 4–8 | all six | VERIFIED | SQL L221–L258 (docs, How we gate grid incl. the rev-18 clause), L277–L278 (Trello) |
| OE 9, 25 | all six | VERIFIED | slack/messages/C05433XK267/2025-09.json /692–/696, /1120–/1132 (Started lines, #2027/#2028 Changes, #135 Changes block without the fix) |
| OE 10–18 | all six (tool/params N/A on reasoning steps) | VERIFIED | linear/data.json /issues (112 open + 20 Done after 2025-09-22T12:30:43Z = 132), SQL L8–L29 (16 inserts), SQL L30–L87 (58 comments; 38 in-scope tickets have comments) |
| OE 19–24 | all six | VERIFIED | SQL L116–L126 (Slack overlay), L129–L139 (vendor mail), L283 (contact), L287–L291 (PR #36), slack/messages/D079SNE2TL4/2025-09.json /260, /263, /265 |
| OE 26–30 | all six | VERIFIED | confluence_working.json /pages/7, SQL L259–L263, linear/data.json /issues/3490 (ZOM-424), SQL L216 |
| OE 31–35 | all six | VERIFIED | catalog entries linear_create_issue, gsheets_batch_update, gsheets_values_update, linear_update_issue, slack_send_message; targets exist at the clock |
- Numeric observability: every count recomputed from rows; every Slack time converted from its ts (calculation recorded); 9:00 AM PDT = 16:00Z − 7 h.
- Expected-value ledger: 764 values on Expected lines, 764 ledgered (0 unledgered), 0 absence claims; write-step values are not_a_claim.
- Act-vs-defer: Slack (Vincent's channels and DMs, Sep 29–Oct 1), Vincent's mailbox, ZOM-570 and its comment, the Trello card: no hold on any of the five writes; Arthur's "I'm holding the prod load until after the store push" concerns the backend data load.

### Format & Standardization
| Step | Defect | OE text | Effect |
|---|---|---|---|
- No shape defects. Every OE is numbered, has one action, names its service, and has an Expected: line.

### Phase 3: Completeness
| Requirement | Covered by | Result |
|---|---|---|
| R1 run the gate on #135 / #50 | OE 1, OE 2, OE 6, OE 9, OE 25 | COVERED |
| R2 the release ticket's background | OE 2–OE 6, OE 8 | COVERED |
| R3 register scope, calls, build statuses | OE 7, OE 9–OE 25 | COVERED |
| R4 the new tab | OE 32, OE 33 | COVERED |
| R5 blockers on ZOM-570's description | OE 34 | COVERED |
| R6 new ZM ticket for unfiled runbook findings | OE 26–OE 29, OE 31 | COVERED |
| R7 QA call in Arthur's thread | OE 1, OE 3, OE 35 | COVERED |
| R8 before Friday's go/no-go | OE 30 | COVERED |
- Path feasibility: SUPPORTED. Task solvability: SUPPORTED_BY_OE.
- Outcome-first mapping: the five writes are Outcome rows (register tab and its 133 rows, ZOM-570 description keys, the new ticket's subject and fields, the threaded NO-GO); reads map to the outcomes they feed; no Process row needed.

### Issues Found
| # | Step | Issue | Component | Effect |
|---|---|---|---|---|
- None.

### Recommended Fixes
1. None required.

### Readability (advice only, no score impact)
- OE 10 and OE 13 carry long key lists; they are deliberate (every register row has a retrieving event). The events read goal-first with values written out and traps named.

## Deep Recheck

Passes: O1, O2, O3 — each a fresh DeepSeek general subagent, blind to the main review (O3 was not given the OE file).

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 35 events | 2 | 0 |
| O2 | 35 events | 2 | 0 |
| O3 | 5 open instructions, 151 items | 1 mismatch | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | O1 | "'Match3D Android Submission - #127 - main Success after 9 min 12 sec'" (OE 9) | slack/messages/C05433XK267/2025-09.json /696 fallback "…- main  Success after 9 min 12 sec" | 2.4 | Accuracy | REJECTED | The OE text carries the record's two spaces (grep count 1); the pass dropped a space when quoting the OE |
| DR2 | O1 | "So the 'green' covers fresh installs only." (OE 27) | SQL L259–L261 matrix, modified 2025-09-30T21:05:00Z; SQL L119 reply 21:10Z | 2.4 | Accuracy | REJECTED | The matrix predates the reply and its update columns are empty strings; the statement is what the record shows |
| DR3 | O2 | "File the bug with device, OS version, source build and repro steps, and link it here." (OE 26) | confluence_working.json /pages/7 | 3.3 | Completeness | REJECTED | The prompt incorporates the runbook only as "the checks in the QA regression runbook" to decide what to file; a Confluence edit is not a prompt-assigned write. OE 31 files the bug with device, OS, source build and repro, and OE 34 lists it on the release ticket |
| DR4 | O2 | "the save came back at level 1 with 500 coins" (OE 28) | confluence_working.json /pages/7 "should be mirrored to the Customer Support Playbook" | 3.3 | Completeness | REJECTED | Same scope: the prompt's writes are the register tab, the ZOM-570 description, a new ZM ticket and the thread reply; a support-playbook note is not asked and would be an unauthorised write |
| DR5 | O3 | M108 "ZOM-506 … NO CALL / n/a" (inventory, not an OE quote) | linear/data.json /issues/3579 "Two strings are overlapping in the Zombie Lane button"; SQL L121 "ZOM-506 zombie lane text ok" | O3 | Completeness | REJECTED | The ticket says what goes wrong (overlapping text, a visual glitch the rules call a bug: "visual and sound glitches included"), it is not an ask for new art or layout, and Vincent saw it working on #135 / #50 → FIXED / in candidate as OE 19 and OE 33 have it |

Effect on verdict: unchanged.

- G1: Put the gate register in a new tab of my release gate sheet | ZM3D Release Gate, new tab | 132 items (M1–M132) + the ticket filed during the gate | Covered by: OE 10–OE 25 (derivation), OE 33 (write). Blind counts match the OEs except ZOM-506 (DR5, rejected).
- G2: add the blockers to the release ticket's description | ZOM-570 description | 18 items (M133–M150) + the new ticket | Covered by: OE 34 (all 18 keys named, plus the OE 31 key).
- G3: file a new ZM ticket … that nobody has filed yet | Linear team ZOM | 1 item (M151, iOS N-1 → iOS Submission #50 save reset) | Covered by: OE 26–OE 29, OE 31.
Scope: G1 covers 132 confirmed items; the prompt names the covering document (the release gate sheet) and the incorporated rules decide each row, so the instruction is bounded.

Platform defects: none

### FINAL VERDICT: PASS
Score: 5
Execution status: COMPLETE
Completeness score: 5
Accuracy score: 5
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Review policy: oracle-events-v2
Reviewed OE SHA-256: 6148bcbc5a4c2805a60c766007ba9074eb4fa97734f98780aec6bfab2253eb23
Review context SHA-256: 93ed3ffad9034b40fd40a221e0f4e175bb84f412ac8a5a75de0a8f3aa0179d50
OE record SHA-256: 4c248c8aae3eeaafd95a70ab9bae03cde7699e739a8212d271894a5cb96f09c5
Eval version: task-quality-v1
Eval release SHA-256: c5b89f4c40a7902f968001f1aa6c710d47bf203842455bbe8dbb668ec7c8943b
Evaluator model: Opus 5.5 (claude-opus-5-5), max effort; deep-recheck passes on DeepSeek general workers
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Next action: Review complete — type the same 35 events into the platform OE field and run the platform /oe
Evidence limits: Static universe/tool evidence; no live writes executed; local run of the Eval (the platform /oe gives the binding verdict)

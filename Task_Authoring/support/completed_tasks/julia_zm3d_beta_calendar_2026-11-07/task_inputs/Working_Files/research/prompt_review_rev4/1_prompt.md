# Local independent /prompt review — SQL revision 4 (c955d6ca…1cf2), prompt 2a23afd8…2beb

Saved by the authoring session from the reviewer's hand-back (the reviewer could not write report files). Independent Opus 5.5 reviewer, blind to authoring notes; passes P1–P4 and Eval 0 ran as separate blind agents (their files are beside this one). The store-bound helpers were not run; the UGT record is `1_prompt_checks.json`.

## PROMPT EVALUATION REPORT

### Task: Julia asks the Agent to build Frederick's ZM3D beta live-ops and push calendar for the four buy weeks, under his shared brief. The Agent also notes any held beat on its ticket, links the sheet on the calendar ticket, and sends Frederick a run/hold recommendation.
### Assigned Persona: Julia Lawson - Product Manager
### Assigned Business Function: Product
### Assigned Competency: Marketing and GTM
### Assigned Task Skill: Planning and decision support
### Assigned Horizon: long-horizon; difficulty mode medium

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Eval version task-quality-v1.

### Injection Gate
- Independent Eval 0 (`injection-static-v2`) on this hash: PASS / COMPLETE (0 lint flags; checks A, B, C pass).
- Disagreement with Eval 0: it rated ZOM-565 "Consistent" without weighing the ticket description and commits 607ccb7f / 5c00e3c330 against the injected "live now" comment.

### Scores

| Dimension | Sub-dimension | Score |
|---|---|---|
| Prompt | Unique Ground Truth | 5 |
| Prompt | Feasibility | 5 |
| Prompt | Persona ACL Reachability | 5 |
| Prompt | Explicit Tool Mention | 5 |
| Prompt | Clarity & Specificity | 5 |
| Prompt | Contrived / Unnatural | 5 |
| Prompt | Alignment with Today's Date | 5 |
| Prompt | Originality | N/A (no sample library bundled locally) |
| Prompt | Truthfulness | 5 |
| Prompt | Tool Use & Cross-service | 5 |
| Prompt | Investigation + Action | 5 |
| Prompt | Coherence (Bolt-on) | 5 |
| Prompt | Persona | 5 |
| Prompt | Business Function | 5 |
| Prompt | Assigned Competency | 5 |
| Prompt | Assigned Task Skill | 5 |
| Prompt | Complexity & Data Seeding | 5 |
| Universe | Data Exists | 5 |
| Universe | **Cross-Service Coherence** | **2** |

### Cross-Service Coherence items

| Item | §3.2 category | Weight | Evidence (both sides) |
|---|---|---|---|
| C1 ZOM-565 closure | State / Lifecycle + Cross-service Referential | Fail-level | Injected: "The endless start screen vfx is in (commit f7e971b0). Claim button glow and the new bar are both live now, can close."; Done 2025-09-29T17:10Z. Base: f7e971b0 is dated 2025-09-25T13:25:12Z, before the ticket was created (13:46:04Z); the description says the new bar was left "not active"; 607ccb7f (2025-09-26) adds the new bar; 5c00e3c330 (2025-09-29T14:33:08Z) says "it's still hidden in there for you to use"; branch `marcus.bennett/EndlessMode_Vfx` has no PR; DM D05U73FNDDL 15:53:47Z Calvin "Should I make another branch for those changes? and merge it". |
| C2 Trello comment on a completed card | State / Lifecycle | Fail-level | Injected commentCard 2025-09-29T17:55:44Z on card 6851a724601a61857a1b202f; base: dueComplete true, dateCompleted 2025-06-30T16:56:34.857Z; 0 of 45 action-completed cards have any later comment. |
| C3 `#471#c_18` | Identifier / Format | Low-impact | Base #471 has only c_1 and c_2; all 630 base PRs number comments c_1..c_n with no gaps. |
| C4 Gmail thread ids | Identifier / Format | Low-impact | Base: id >> 20 equals the first internal_date (599 of 600 sampled). Injected ids decode to 2025-09-28T01:55Z and 2025-10-02T02:24Z (after the clock) for mails dated Sep 22 and Sep 26. |

Counting rule applied: State / Lifecycle always fails; two low-impact items also fail together.

### Deep recheck (round 2)

| DR# | Pass | Topic | Status | Reason |
|---|---|---|---|---|
| DR1 | P1 | Brian's moved-earlier handoff date | CONFIRMED as authorized variation (objective boundary) | The brief's "lands before its lock" accepts Oct 29 and any instant before 2025-10-31T00:00Z. Not a fail. |
| DR2 | P2 | ZOM-565 | CONFIRMED (point 1); point 2 rejected | "live now" contradicted by description, commits and DM. The 14:34 "i wrote a comment" refers to a base comment the export omits. |
| DR3 | P2 | Trello comment on completed card | CONFIRMED, fail-level | 45 completed cards, 0 with later non-update actions. |
| A1 | P2 | Leagues hold-until | advisory | No dated fix exists; rubric must accept an open-ended hold. |
| A2 | P2 | Pushes "Send (UTC)" for trigger-based rows | advisory | Trigger rows carry no instant. |
| A3 | P2 | Douglas's Sep 30 prod update | REJECTED | It was the teams/social fix, not Collect & Win. |
| — | P3 | Truthfulness, dates | none | 10 premises confirmed. |
| — | P4 | Naturalness, tool names, destinations | none | 6 sentences clean. |

Forks, all settled: F1 handoff date (authorized boundary); F2 Endless still-to-do (ZOM-565; conflict scored as C1); F3 leagues hold-until (open-ended); F4 PR #477 (analytics, excluded); F5 reply to Brian (required by the brief); F6 CodeRabbit reviews (no hold; only CHANGES_REQUESTED is #303 in July); F7 Season Pass October window (already on prod); F8 quest set Oct 13 (not put down — brief's quest scope sentence); F9 note ticket (ZOM-429); F10 Halloween (off).

### FINAL VERDICT: FAIL

Score: 2

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5)

Next action: Fix the injection SQL (C1 ZOM-565, C2 Trello completed-card comment, C3 `#471#c_18` → `#c_3`, C4 Gmail thread ids), then rerun /injection and /prompt.

Evidence limits: store-bound helpers not run; GCal description rendering, `gmail_reply_to_message` behaviour and Linear state history are runtime-unverified; Linear base comments are not exported.

### Minimum changes the reviewer listed (all injection SQL; no prompt change)

1. ZOM-565: a comment by Marcus dated after 14:33:08Z and at or before 14:34:25Z on 2025-09-29 that says the prefab change is on his branch, the new bar is still hidden, and Calvin still has to hook it up; ticket stays Todo; it must also say whether the work has to land before the beta buy, otherwise Endless gains a still-to-do fork.
2. Trello: move the quest-set note to an open card or drop it.
3. `#471#c_18` → `#471#c_3`.
4. Gmail thread ids: id >> 20 must equal internal_date in ms (Sep 22: 1843954785976320000–1843954785977368575; Sep 26: 1844311385702400000–1844311385703448575).

Rubric notes: accept any handoff instant before 2025-10-31T00:00Z including Oct 29; accept an open-ended leagues hold; accept a trigger description for local-push send times.

All four are fixed in SQL revision 5, together with the claim-audit findings (`claims_*.md` in this folder).

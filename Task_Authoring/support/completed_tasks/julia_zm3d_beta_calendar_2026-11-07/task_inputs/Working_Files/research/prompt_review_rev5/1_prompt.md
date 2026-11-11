# Local independent /prompt review — SQL revision 5 (3c035f2a…bc6f), prompt 2a23afd8…2beb

Saved by the authoring session from the reviewer's hand-back (the reviewer could not write report files). Independent Opus 5.5 reviewer, blind to authoring notes; passes P1–P4 and Eval 0 ran as separate blind agents (their files are beside this one; the helper-rendered Unique Ground Truth section is `ugt_section.md`, the record `1_prompt_checks.json`). The store-bound helpers were not run.

## PROMPT EVALUATION REPORT

### Task: Julia Lawson builds the ZM3D beta live-ops and push calendar for Frederick's four buy weeks (Oct 6 to Nov 2), notes any held beat on its ticket, links the sheet on the calendar ticket and sends Frederick her run/hold recommendation
### Assigned Persona: Julia Lawson, Product Manager
### Assigned Business Function: Product
### Assigned Competency: Marketing and GTM
### Assigned Task Skill: Planning and decision support
### Assigned Horizon: long-horizon; difficulty mode medium

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Eval version task-quality-v1.

### Injection Gate
Independent Eval 0 (`injection-static-v2`) on this hash, nothing reused: PASS / COMPLETE, no demonstrated defects. Each of its advisories was decided under §3.2 and the STEP 0.5 rule; none changes a value, set, order, recipient or destination the answer is graded on.

### Scores

| Dimension | Score |
|---|---|
| Unique Ground Truth | 2 (FAIL) |
| Feasibility | 5 |
| Persona ACL Reachability | 5 |
| Explicit Tool Mention | 5 |
| Clarity & Specificity | 5 |
| Contrived / Unnatural | 5 |
| Alignment with Today's Date | 5 |
| Originality | N/A (no sample library bundled locally) |
| Truthfulness | 5 |
| Tool Use & Cross-service | 5 |
| Investigation + Action | 5 |
| Coherence (Bolt-on) | 5 |
| Persona | 5 |
| Business Function | 5 |
| Assigned Competency | 5 |
| Assigned Task Skill | 5 |
| Complexity & Data Seeding | 5 |
| Data Exists | 5 |
| Cross-Service Coherence | 5 |

Cross-Service Coherence: every injected record was checked against its base record and against base evidence of the same work (ticket text and state, code and git history, commits, PRs, Slack including private DMs, mail, Trello history, table conventions). No State/Lifecycle or Quantitative inconsistency; no low-impact inconsistency counted.

### Issue

| # | Issue | Severity | Dimension |
|---|---|---|---|
| 1 | The brief does not settle whether Leonard's Oct 13 quest set ("goes in with the Mon Oct 13 rollover, the current set carries the first week") is the quest beat's still-to-do | Major | Unique Ground Truth |

### Deep recheck (round 3)

| DR# | Pass | Topic | Status | Reason |
|---|---|---|---|---|
| P1-DR1 | P1 | Quest still-to-do (Trello note) | CONFIRMED | No prompt sentence or persona-visible record rules out either reading. |
| P1-DR2 | P1 | ZOM-544 sign-in as a still-to-do | REJECTED | The brief counts only what a beat needs before it runs; the beats already run without sign-in. |
| P1-DR3 | P1 | Brian's moved-earlier date | CONFIRMED as authorized boundary | Any handoff before Fri Oct 31 00:00 UTC. |
| P1-DR4 | P1 | Leaderboard "until when" | REJECTED, no Clarity change | Open-ended is the only consistent answer; rubric must not require a date. |
| P1-DR5 | P1 | Plague Race push ready | REJECTED | Brief: "Ready and LIVE". |
| P1-DR6 | P1 | Leagues vs weekly leaderboard | REJECTED | Same Monday reset under both names in Julia-visible records. |
| P2-DR1..4 | P2 | Invitation mails, informal references, hold-until, hidden polish DMs | REJECTED, not scored | Base norm or not needed by the answer. |
| — | P3 | Truthfulness, dates | none | 13 premises confirmed. |
| — | P4 | Naturalness, tool names, destinations | none | 6 sentences clean. |

Forks: F1 quest still-to-do (open); F2–F7, F9–F12 settled by quoted records; F8 handoff date is an authorized boundary.

### FINAL VERDICT: FAIL

Score: 2

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Replace the text of Trello action 68dac8204f1e9a3b7c2d5e61 so it states whether anything in the beta waits on the new quest set, then rerun /injection and /prompt on the new SQL hash.

Evidence limits: store-bound helpers not run (record validated with the same helper functions read-only); Example Task PDF not re-read; Eval 0 supplied, not run by this reviewer.

### Reviewer's notes for the next revision

- Candidate text "New quest set goes in with the Mon Oct 13 rollover if it is ready. Nothing in the beta waits on it, the current set runs the whole time either way." settles F1 (still-to-do: none).
- Residual a second strict reviewer might score: ZOM-526 / ZOM-528 still In Progress after the Collect & Win trigger and card-pack commits landed on Sep 29–30 (SC-16 pattern); ZOM-544 if a rubric grades the still-to-do set strictly; `#468 ev_6` ordering; Gmail shape gaps; "September handoff" has no record; Business Function / Competency could be read at 3 by a stricter reader.
- Rubric must accept: no hold-until date; any Brian date before Fri Oct 31 00:00 UTC; leagues and weekly leaderboard as one beat; a ZOM-78 comment or link update; a DM thread reply or new DM message.

Revision 6 applies the Trello text, a Sep 30 ZOM-526 note saying what is left after the merges (Axe Arena), the ZOM-544 trim and the "September handoff" removal.

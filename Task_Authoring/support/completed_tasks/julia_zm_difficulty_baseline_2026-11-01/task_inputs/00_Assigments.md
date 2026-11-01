# Task Assigned Inputs

Transcribe the assignment exactly as the platform shows it (screens 2–13). Do not
choose, substitute or "improve" any of it; you may not switch personas. Field names
match the batch upload template.

```
taskId:             [ ]
task_version:       [ ]
horizon:            Long Horizon       # platform "Task Type": long-horizon
business_function:  Product
evals_category:     [ ]        # not shown on the assignment — Evals/references/rules/task_categories.md: Engineering & Live-Ops · Product & Design · Growth / UA / Marketing · Founders / Exec / Strategy · Finance / Legal / HR / Ops · Analytics & Data
competency:         Engineering Ops
task_skill:         Retrieval
specializations:    [ ]        # not shown on the assignment
persona_name:       Julia Lawson
persona_role:       Product Manager
difficulty_mode:    medium
universe_date:      October 1, 2025 07:00
env_id:             hg4-with-gsuite-bundle-1174
universe_id:        hg4-2026-08-31     # or the Universe ID you continued from
```

## Persona resolution

Resolve `persona_name` + `persona_role` to exactly one entry in
`Evals/references/persona/roster.json` (17 usable personas; exact emails also in
`Task_Authoring/references/persona_roster_v2.json`) and copy it here.
Zero or several matches means the assignment is wrong — stop and fix it. Never type
an email by hand.

```
persona_key:  julia_lawson
email:        julia.lawson@harmonygames.co
department:   Product
```

`thomas` and `tim_steudler` appear on the taxonomy's 19-person list but not in the
Evals roster: `/prompt` fails its identity gate for them, and their data cannot carry a
task (Tim: no Slack, mailbox or Drive; Thomas: mail ends Apr 2025 — `references/Scenario_Atlas.md`).
Escalate an assignment that names them.

## Fixed facts

- Clock: **February 14, 2026, 00:00 UTC** (Saturday). Nothing on or after it has happened.
- Tiers: Normal 50–100 tool calls · Long-Horizon 100–500+ (Super-Long-Horizon is paused).
  The engine's extreme profile (≥ 600 designed calls) fits Long Horizon; on Normal Horizon it
  scores Borderline Horizon (non-fail, score capped at 3) — `setup/GEN_EXECUTION.md` §3a.
- Scoped reads: Gmail, Slack, Calendar, Drive, Docs, Sheets, Slides. Unscoped: GitHub,
  Linear, Trello, Contacts, Confluence, Snowflake (the last two are live but not advertised
  to the agent).
  Writes are never ACL-governed.
- Stacking a second task skill is encouraged; the assigned one must be clearly exercised.

## Author targets for this task (set by the task author, 2026-10-30)

Author's words (chat 2026-10-30): "make sure my task is a long horizon task so i want minimum 120 tool calls in each runs and also make sure i want difficulty under 75%".
These are stricter than the assigned minimums; every stage designs to them.

- **Horizon: Long Horizon** (platform "long-horizon"; tier 100–500+ calls).
- **Tool calls per baseline run: minimum 120 in every run** (a floor, not a ceiling; tier floor is 100).
  Design profile: `effective_profile: long` with
  `profile_exception: {reason: "author target minimum 120 calls per run, below the extreme ~600-call design",
  requester_confirmation: "user chat 2026-10-30: minimum 120 tool calls in each runs"}`.
  Size the necessary-call budget at ~160 unconditional (plan ~170, no service > 50%), with a
  per-record cohort that no bulk result can replace, so the leanest correct run still clears 120.
  Calibration: Robert task designed for 150+ but ran 116–143, so lean runs undershoot; keep a ~40-call margin.
  Keep the extreme breadth (≥ 10 of 13 services, ≥ 120 rows, 2–4 hidden authorities with decoys,
  ≥ 3 chains, ≥ 12 traps).
- **Average weighted pass rate: < 75%** across the six rollouts (design target ~62–65%), stricter
  than the medium-mode cap of 85%. pass@1 ≤ 3 of 6 (design ≤ 2). Per-rollout SD 0.1–0.3;
  ≥ 2 failure patterns, largest ≤ 50%.
  Lessons from completed tasks (all missed 75%: 78.3%, 80.8%, ~85%, 85.7%):
  - Opus applies every rule it reads, so rule-application traps alone do not lower the score.
  - Use 3+ independent hidden facts, each deciding 2+ rubric rows, on different rows, behind
    different reading habits (~50% find rate each), not all rewarding "deep reading".
  - Never put a hidden fact on the ask itself.
  - Project difficulty with `tools/difficulty_stats.py` against the per-write, work-weighted
    rubric /rubric will demand (hidden-fact rows weight 5), not a grouped mental rubric.
- Difficulty mode as assigned: medium (recorded; the gates above still govern).
- Human-time estimate must fit Long Horizon.

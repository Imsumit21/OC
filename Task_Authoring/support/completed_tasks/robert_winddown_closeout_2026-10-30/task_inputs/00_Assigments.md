# Task Assigned Inputs

Transcribe the assignment exactly as the platform shows it (screens 2–13). Do not
choose, substitute or "improve" any of it; you may not switch personas. Field names
match the batch upload template.

```
taskId:             [ ]        # not supplied
task_version:       [ ]        # not supplied
horizon:            Long Horizon   # platform task type: "long-horizon"
business_function:  Executive
evals_category:     Founders / Exec / Strategy   # derived from Executive + Corporate Ops; see Evals/references/rules/task_categories.md: Engineering & Live-Ops · Product & Design · Growth / UA / Marketing · Founders / Exec / Strategy · Finance / Legal / HR / Ops · Analytics & Data
competency:         Corporate Ops
task_skill:         Planning and Decision Support
specializations:    [ ]        # not supplied; e.g. art, game-design, game-engineering, business-entrepreneurship
persona_name:       Robert
persona_role:       Co-founder & Creative Director
env_id:             hg4-with-gsuite-bundle-1174
universe_id:        hg4-2026-08-31     # or the Universe ID you continued from
difficulty_mode:    easy
universe_date:      February 14, 2026 00:00
```

## Persona resolution

Resolve `persona_name` + `persona_role` to exactly one entry in
`Evals/references/persona/roster.json` (17 usable personas; exact emails also in
`Task_Authoring/references/persona_roster_v2.json`) and copy it here.
Zero or several matches means the assignment is wrong — stop and fix it. Never type
an email by hand.

```
persona_key:  robert
email:        robert@harmonygames.co
department:   Executive
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

## Assignment as supplied (verbatim)

```
Business Function: Executive
Persona: Robert — Role: Co-founder & Creative Director
Competency: Corporate Ops
Task Skill: Planning and decision support
Task Type: long-horizon
Difficulty Mode: easy
Universe Date: February 14, 2026 00:00
```

## Author targets

Set by the task author in chat on 2026-10-28: "make sure my task is a long-horizon task so i want minimum above 150 tool calls in each also i want difficulty under 80%".

- Per-run tool-call band: **more than 150 counted tool calls in every baseline run** (floor, not a ceiling). Design the necessary-call budget at ~200+ so the leanest correct run still clears 150.
- Average weighted pass rate: author target **< 80%**; the harness/Evals gate is **< 75%** (strictest governs, GEN_EXECUTION §3), so design to a ~62–65% projection.
- Profile: `effective_profile: long` with `profile_exception` quoting the author's confirmation (a ~600-call extreme design would overshoot a 150+ band by a wide margin and is not what the author asked for).
- Difficulty mode as assigned: easy (recorded; the gates above still govern).

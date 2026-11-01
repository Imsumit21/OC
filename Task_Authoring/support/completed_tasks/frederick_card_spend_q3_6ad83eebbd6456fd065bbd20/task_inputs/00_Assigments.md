# Task Assigned Inputs

Transcribe the assignment exactly as the platform shows it (screens 2–13). Do not
choose, substitute or "improve" any of it; you may not switch personas. Field names
match the batch upload template.

```
taskId:             [ ]
task_version:       [ ]
horizon:            long-horizon   # the platform's "task type" — copy verbatim; /prompt needs it
business_function:  Executive        # as assigned (e.g. Design, Engineering, Executive, Product, Sales)
evals_category:     [ ]        # Evals/references/rules/task_categories.md: Engineering & Live-Ops · Product & Design · Growth / UA / Marketing · Founders / Exec / Strategy · Finance / Legal / HR / Ops · Analytics & Data
competency:         Finance
task_skill:         Analysis and synthesis
specializations:    [ ]        # e.g. art, game-design, game-engineering, business-entrepreneurship
persona_name:       Frederick Stone
persona_role:       Co-founder
env_id:             hg4-with-gsuite-bundle-1174
universe_id:        hg4-2026-08-31     # or the Universe ID you continued from
```

## Additional assigned fields (verbatim from the platform)

```
difficulty_mode:    medium
universe_date:      October 1, 2025 07:00
```

## Persona resolution

Resolve `persona_name` + `persona_role` to exactly one entry in
`Evals/references/persona/roster.json` (17 usable personas; exact emails also in
`Task_Authoring/references/persona_roster_v2.json`) and copy it here.
Zero or several matches means the assignment is wrong — stop and fix it. Never type
an email by hand.

```
persona_key:  frederick_stone
email:        frederick.stone@harmonygames.co
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

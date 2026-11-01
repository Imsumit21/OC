# Task Assigned Inputs

Transcribe the assignment exactly as the platform shows it (screens 2–13). Do not
choose, substitute or "improve" any of it; you may not switch personas. Field names
match the batch upload template.

```
taskId:             [ ]
task_version:       [ ]
horizon:            Long Horizon     # platform "Task Type" shows: long-horizon
business_function:  Engineering      # as assigned (e.g. Design, Engineering, Executive, Product, Sales)
evals_category:     [ ]        # Evals/references/rules/task_categories.md: Engineering & Live-Ops · Product & Design · Growth / UA / Marketing · Founders / Exec / Strategy · Finance / Legal / HR / Ops · Analytics & Data
competency:         Engineering Ops
task_skill:         Retrieval
specializations:    [ ]        # e.g. art, game-design, game-engineering, business-entrepreneurship
persona_name:       Douglas
persona_role:       Software Engineer
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
persona_key:  douglas
email:        douglas@harmonygames.co
department:   Engineering
```

`thomas` and `tim_steudler` appear on the taxonomy's 19-person list but not in the
Evals roster: `/prompt` fails its identity gate for them, and their data cannot carry a
task (Tim: no Slack, mailbox or Drive; Thomas: mail ends Apr 2025 — `references/Scenario_Atlas.md`).
Escalate an assignment that names them.

## Fixed facts

- Clock (V3, assigned): **October 1, 2025, 00:00 UTC** = Tuesday, September 30, 2025, 5:00 PM Pacific.
  Nothing seeded may be dated after it; building on February 14, 2026 fails outright.
- Difficulty mode **medium**: six-rollout average must stay strictly under 85%; 5+ of 6 full passes fails.
- Tiers: Normal 50–100 tool calls · Long-Horizon 100–500+ (Super-Long-Horizon is paused).
  The engine's extreme profile (≥ 600 designed calls) fits Long Horizon; on Normal Horizon it
  scores Borderline Horizon (non-fail, score capped at 3) — `setup/GEN_EXECUTION.md` §3a.
- Scoped reads: Gmail, Slack, Calendar, Drive, Docs, Sheets, Slides. Unscoped: GitHub,
  Linear, Trello, Contacts, Confluence, Snowflake (the last two are live but not advertised
  to the agent).
  Writes are never ACL-governed.
- Stacking a second task skill is encouraged; the assigned one must be clearly exercised.

## Author targets for this task (set by the task author, 2026-10-26)

These are stricter than the assigned minimums; they are the goals every stage designs to.

- **Tool calls per baseline run: 130–150, minimum 130 in every run** (Long-Horizon tier floor is
  100). Requester-confirmed (chat 2026-10-26: "minimum 130 to 150 tool calls in each runs").
  Design profile: `effective_profile: long` with
  `profile_exception: {reason: "author target 130–150 calls per run, below the extreme ~600-call design",
  requester_confirmation: "user chat 2026-10-26: minimum 130 to 150 tool calls in each runs"}`.
  Keep the extreme breadth (≥ 10 of 13 services, ≥ 120 rows, 2–4 hidden authorities with decoys,
  ≥ 3 chains, ≥ 12 traps); size the necessary-call budget at ~140 unconditional (plan ~145,
  no service > 50%), with a per-record cohort that no bulk result can replace, so even an
  efficient run cannot finish under 130 and a thorough one stays near 150.
  Calibration from completed tasks: designed ≈ actual (account handover ~75 designed → 68–100;
  card spend ~600 → 554–573).
- **Average weighted pass rate: < 75%** across the six rollouts (design target ≤ 65%), stricter
  than the medium-mode cap of 85%. pass@1 ≤ 3 of 6 (design ≤ 2). Per-rollout SD 0.1–0.3.
  Both completed tasks missed this line (78.3% and 80.8%): the strong runs found every
  authority and passed almost everything. Design several independent hidden authorities on
  different rows so finding one does not unlock the rest, and give the Retrieval answer rows
  boundary records and supersessions that a careful run can still get wrong.
- Human-time estimate must fit Long Horizon.

# Task Assigned Inputs — V3

## Platform assignment

Paste the assignment exactly as the platform displays it, including the role,
difficulty mode and universe date. The eight assigned fields appear in seven
groups because Role is inside Persona. Do not change any assigned value. The user
only needs to supply this platform block; authoring setup resolves the inputs below.

```text
🏢 Business Function
[Business function]

🧑 Persona
[Persona name]
Role: [Assigned role]

🎯 Competency
[Competency]

🛠️ Task Skill
[Task skill]

📋 Task Type
[Task type]

🎚️ Difficulty Mode
[Difficulty mode]

📅 Universe Date
[Universe date exactly as displayed, including its time]
```

## Resolved authoring inputs

Authoring setup fills this mirror from the platform block and the selected persona
roster. Keep `persona_name`, `persona_role`, `persona_key`, `email`, `department`
and `horizon` for compatibility with existing tools. Do not ask the user to
reformat the assignment or supply a timezone. Normalize and validate it with
`python3 Task_Authoring/tools/task_context.py --task-dir Task_Authoring/task_inputs --write`.
Add `--require-source` before grounding task facts.

```text
spec_version:       V3
business_function:  [From platform]
persona_name:       [From platform]
persona_role:       [From platform]
competency:         [From platform]
task_skill:         [From platform]
task_type:          [normal | long-horizon]
horizon:            [Normal Horizon | Long Horizon]
difficulty_mode:    [easy | medium | hard]
universe_date:      [Exact platform display]
universe_date_key:  [2025-10-01 | 2026-02-14]
freeze_utc:         [V3 freeze for the assigned date]
persona_key:        [Resolved from roster]
email:              [Copied from roster]
department:         [Copied from roster]
```

Resolve the assigned name and role to one persona in
`Evals/references/persona/roster.json`; use
`Task_Authoring/references/persona_roster_v2.json` as a cross-check. Never invent an
email, substitute a persona or silently discard a conflicting role. If a persona
is absent from the selected source or roster, report the source mismatch.

Task ID, attempt ID, task version, environment ID, source snapshot ID,
specializations and evaluation category are separate operational metadata. Record
them when supplied or verified; they are not additional required assignment fields.
Do not prefill an environment or snapshot ID from the old V2 template.

## V3 authoring constraints

Use `Task_Authoring/references/Docs/11_V3_Changes.md` for V3 changes; unaffected
V2 rules still apply. This workspace-relative path remains valid when the
template is copied into `task_inputs/`.

- Freeze mapping: October 1, 2025 → `2025-10-01T00:00:00Z`; February 14, 2026 →
  `2026-02-14T00:00:00Z`. Preserve the displayed time above. This mapping comes
  from the course's assigned dates, not an inferred conversion of the display time.
- Both V3 dates use the supplied shared universe. Verify task evidence against the
  assigned freeze during scenario and injection creation. Nothing seeded may be
  dated after it; future deadlines are allowed. Later completed events cannot be
  treated as past, and earlier mutable state needs dated records/history.
- Difficulty: Easy average <90%; Medium <85%; Hard <70%. Equality fails. Use the
  assigned mode and corrected, fairly graded results; never switch modes.
- Horizon: Normal ≥50 tool calls; Long-Horizon ≥100. Use the golden run when one
  exists, otherwise the six-rollout average. Exceeding the displayed range is
  allowed. Human effort: Normal under about 8 hours; Long-Horizon about 12–24 hours.
- The existing local horizon design is retained at the user's request:
  Long-Horizon uses the extreme profile with at least 500 designed calls; Normal
  uses its existing normal profile and budget limits. Assigned difficulty mode
  still supplies its own weighted score cap.
- The pre-check and all six baseline rollouts use Opus 5.5. Five or more full-pass
  rollouts fails regardless of the average; unchanged error and failure-pattern
  checks still apply.
- The work must be plausible for the assigned role. Exercise the assigned
  competency and task skill; their alignment is distinct from role plausibility.

Eval Portal reviews and uploads are handled by the user. This file records inputs
and constraints; it does not certify dated task evidence, completed runs or reviews.

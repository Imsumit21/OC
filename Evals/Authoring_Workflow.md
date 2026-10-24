# Authoring

No stage in this package authors task artifacts. `/hint` and its `create` mode
were removed on 2026-09-26: hinting is no longer part of the contributor task
flow. `/rubric create` and prefill writers are retired.

- `/prompt`, `/oe` and `/rubric` evaluate the supplied artifact, report findings
  and suggested fixes, and stop. They never rewrite, generate or prefill the
  artifact.
- For newly developed tasks, obtain one baseline run and use `/hardness` before
  dependent stages. Prefer Opus; an existing Haiku run is accepted without
  backfill. Load only Eval 1A for Opus or Eval 1B for Haiku prediction.
- Before judging any expected deliverable, apply `WORKFLOW.md`'s **Output
  capability and failure attribution** contract. Report unsupported requirements
  as upstream blockers; never grade their absence as a model failure.
- Replacing a canonical task input needs an explicit user instruction. Preserve
  the prior version and identify affected downstream evidence using `WORKFLOW.md`.

Write every stage report through `Evals/tools/hg_write_output.py` to its fixed
`Evals/task_inputs/reports/` path.

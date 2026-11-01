# Working_Files — everything the commands generate

`task_inputs/` holds only the platform slots, in the same layout as the task template.
Every other file a `/create-*` command or `stage_gate.py` writes lands here, so the
top level always shows exactly what goes to the platform. Start a task with
`cp -R Task_Authoring/references/Tasks_Template/. Task_Authoring/task_inputs/`.
Slots are numbered in platform screen order; the full map (author, screen, command,
Evals key) is in `setup/GEN_EXECUTION.md` §5.

## Platform slots (top of `task_inputs/`)

| Slot | Filled by |
|---|---|
| `00_Assigments.md` | You — transcribe the assignment (all five fields, incl. horizon) |
| `01_Universe_Inject.sql` | `/create-injection` (after `/create-scenario`) |
| `02_Reference_Files/` | `/create-reference-files` (optional) |
| `03_Error_Async_Config.txt` | `/create-error-async` (optional) |
| `04_Prompt.txt` | **You only** — exactly as you will submit it |
| `05_Human_Time.md` | **You only** — the estimate you type on the platform (pasting is blocked) |
| `06_PreCheck_Trajectory/` | Platform — the Opus pre-check run, saved as `06_PreCheck_Trajectory/trajectory.json` |
| `07_Baseline_Trajectories/` | Platform — the baseline rollouts |
| `08_Oracle_Events.md` | **You only** |
| `09_Rubrics.json` | **You only** — export from the Rubric Criteria Builder |
| `10_Baseline_Verifier_Results.md` | Platform — paste the verifier results |
| `11_AF_Justification.md` | `/create-allfail` — the all-fail justifications for the Rate All-Fail Rubrics screen |
| `Audit-Report/` | Review reports, when the task is audited |

## Generated here (`task_inputs/Working_Files/`)

`01_Scenario_Design.md`, `01_Hardness_Manifest.draft.json`, `01_Hardness_Manifest.json`,
`01b_Redteam_Review.md` (+ `.second.md`), `01_Grounding_Dossier.md`, `01a_Hardening_Report.md`,
`02_Reference_Files_Manifest.md`, `04_Prompt_Writing_Brief.md`, `04_Prompt_Check.md`,
`05_Human_Time_Worksheet.md`, `08_OE_Writing_Ledger.md`, `08_OE_Check.md`,
`09_Rubric_Writing_Plan.md`, `09_Rubric_Check.md`, `12_difficulty_input.json`,
`12_Difficulty_Stats.txt` and `13_Release_Gate.txt`. None is scaffolded; each command
creates its own. There is no changelog slot.

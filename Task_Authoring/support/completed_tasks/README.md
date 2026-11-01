# support/completed_tasks/ — submitted HarmonyGames tasks

Each folder is a real task taken through the full pipeline and submitted. They are kept
so the next author can see what a finished slot looks like, which levers moved the
baseline average, and what the platform evaluators flagged. Read each folder's
`README.md` first: its **Lessons carried forward** section is the distilled learning.
Cross-task lessons also go into the root `learnings` file.

Do not copy a cohort, rule vocabulary, record set, prompt, Oracle Event or criterion
from here into a new task (originality, `playbooks/01_Scenario_Design.md` S1).

## Layout (same in every folder)

| Path | Contents |
|---|---|
| `README.md` | Persona, horizon, mode, universe date, final state, key answers, baseline results, lessons |
| `task_inputs/` | The slot folder as submitted: `00_Assigments.md`, `01_Universe_Inject.sql`, `02_Changelog.json`, `02_Reference_Files/`, `03_Error_Async_Config.txt`, `04_Prompt.txt`, `05_Human_Time.md`, `06_PreCheck_Trajectory/`, `07_Baseline_Trajectories/`, `08_Oracle_Events.md`, `09_Rubrics.json`, `10_Baseline_Verifier_Results.md`, `11_AF_Justification.md` (when there were all-fail rows), `Working_Files/` |
| `eval_reports/` | Platform eval reports (/injection, /prompt, /hardness, /oe, /rubric), every round kept |
| `work/` | Local builder and scoring scripts used to produce the inputs (SQL, manifest, dossier, OE, rubric generators, baseline replays) |

Scripts under `work/` may hard-code the original author's absolute paths; adjust them
before re-running. Backup copies (`*.bak*`), pickles and `*.err` probes are git-ignored.

## Tasks

| Folder | Persona · horizon · mode | Universe date | Baseline average |
|---|---|---|---|
| `frederick_card_spend_q3_6ad83eebbd6456fd065bbd20` | Frederick Stone · Long · medium | Oct 1, 2025 | 78.3% |
| `frederick_account_handover_2026-10-26` | Frederick Stone · Normal · medium | Oct 1, 2025 | 80.8% |
| `douglas_beta_server_signoff_2026-10-28` | Douglas · Long · medium | Oct 1, 2025 | 56.3% |
| `robert_winddown_closeout_2026-10-30` | Robert · Long · easy | Feb 14, 2026 | 85.7% |
| `julia_zm_difficulty_baseline_2026-11-01` | Julia Lawson · Long · medium | Oct 1, 2025 | 83.8% |

## Adding a task

Copy the submitted slot to `<persona>_<short_topic>_<YYYY-MM-DD>/task_inputs/`, put the
platform reports in `eval_reports/` and your builders in `work/`, write the `README.md`
in the same shape as the others, add a row above, then commit. `.gitignore` already
tracks `task_inputs/` here (and only here).

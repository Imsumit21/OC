# support/completed_tasks/ — HarmonyGames completed tasks

Each folder is a real task taken through the full pipeline. Most were submitted; two
are archived unfinished and are flagged as such below. They are kept so the next author
can see what a finished slot looks like, which levers moved the baseline average, and
what the platform evaluators flagged. Read each folder's `README.md` first: its
**Lessons carried forward** / **Lessons for the next author** section is the distilled
learning. Cross-task lessons also go into the root `learnings` file.

Do not copy a cohort, rule vocabulary, record set, prompt, Oracle Event or criterion
from here into a new task (originality, `playbooks/01_Scenario_Design.md` S1).

## Layout

| Path | Contents |
|---|---|
| `README.md` | Persona, horizon, mode, universe date, final state, key answers, baseline results, lessons |
| `task_inputs/` | The slot folder as submitted: `00_Assigments.md`, `01_Universe_Inject.sql`, `02_Changelog.json`, `02_Reference_Files/`, `03_Error_Async_Config.txt`, `04_Prompt.txt`, `05_Human_Time.md`, `06_PreCheck_Trajectory/`, `07_Baseline_Trajectories/`, `08_Oracle_Events.md`, `09_Rubrics.json`, `10_Baseline_Verifier_Results.md`, `11_AF_Justification.md` (when there were all-fail rows), `Working_Files/` |
| `eval_reports/` | Platform eval reports (/injection, /prompt, /hardness, /oe, /rubric), every round kept |
| `work/` | Local builder and scoring scripts used to produce the inputs (SQL, manifest, dossier, OE, rubric generators, baseline replays) |

Scripts under `work/` may hard-code the original author's absolute paths; adjust them
before re-running. Backup copies (`*.bak*`), pickles and `*.err` probes are git-ignored.

The two 2026-11-02 folders keep the slot at their own root (numbered files plus
`Working_Files/`) with the platform reviews in `plateform_report/` or
`plateform-reports/`, instead of the `task_inputs/` / `eval_reports/` / `work/` split.

## Tasks

| Folder | Persona · horizon · mode | Universe date | Baseline average |
|---|---|---|---|
| `frederick_card_spend_q3_6ad83eebbd6456fd065bbd20` | Frederick Stone · Long · medium | Oct 1, 2025 | 78.3% |
| `frederick_account_handover_2026-10-26` | Frederick Stone · Normal · medium | Oct 1, 2025 | 80.8% |
| `douglas_beta_server_signoff_2026-10-28` | Douglas · Long · medium | Oct 1, 2025 | 56.3% |
| `robert_winddown_closeout_2026-10-30` | Robert · Long · easy | Feb 14, 2026 | 85.7% |
| `julia_zm_difficulty_baseline_2026-11-01` | Julia Lawson · Long · medium | Oct 1, 2025 | 83.8% |
| `arthur_sunset_delivery_plan_2026-11-02` ⚠ | Arthur Blake · Long · hard | Feb 14, 2026 | 87.9% (missed the <70% cap) |
| `julia_dd_closeout_2026-11-02` ⚠ | Julia Lawson · Long · easy | Oct 1, 2025 | 69.7% |
| `frederick_bridge_pipeline_2026-11-03` | Frederick Stone · Long · medium | Oct 1, 2025 | 77.7% |
| `frederick_q4_commitments_2026-11-05` | Frederick Stone · Long · easy | Oct 1, 2025 | 71.0% |
| `robert_llc_takeover_2026-11-06` | Robert · Long · easy | Feb 14, 2026 | 83.6% |
| `owen_dd_bug_carryover_2026-11-09` | Owen Baker · Long · medium | Feb 14, 2026 | 84.3% |
| `samuel_zm_beta_messages_2026-11-09` ⚠ | Samuel Turner · Long · medium | Oct 1, 2025 | 70.8% (weighted local grade; six stored runs) |
| `claire_zm3d_halloween_art_plan_2026-11-10` | Claire Morgan · Long · medium (platform: easy) | Oct 1, 2025 | 64.1% |
| `julia_zm3d_beta_calendar_2026-11-07` | Julia Lawson · Long · medium | Oct 1, 2025 | none (moved before a /prompt pass) |
| `leonard_stockholder_closeout_2026-11-10` | Leonard Hayes · Long · medium | Feb 14, 2026 | 76.9% |
| `robert_seed_bets_2026-11-11` | Robert · Long · easy | Feb 14, 2026 | 85.5% |
| `calvin_qm_epic_2026-11-11` | Calvin Price · Long · hard | Oct 1, 2025 | 64.4% |
| `julia_zm_audience_call_2026-11-07` ⚠ | Julia Lawson · Long · medium (designed to the hard target) | Oct 1, 2025 | 78.2% |
| `julia_zm3d_playable_brief_2026-11-13` | Julia Lawson · Long · hard | Oct 1, 2025 | 40.5% (spread 0.095, under the 0.1 band) |

⚠ = archived unfinished: `/rubric` never passed (Arthur: FAIL 2 on the reviewed 43-row set; Julia DD close-out: FAIL 1
on one evidence line, fixed locally and never re-sent; Samuel: FAIL 1 twice on attempt `6aeed825`, the round-2 Fix List
is applied locally and was not re-reviewed; Julia audience call: FAIL 1 then FAIL 2 on the retention row only on attempt
`6aeed824`, that row rewritten and passed locally, no later portal report in the archive). The four READMEs state the
open stage and what was learned; do not read their presence here as a cleared task.

## Adding a task

Copy the submitted slot to `<persona>_<short_topic>_<YYYY-MM-DD>/task_inputs/`, put the
platform reports in `eval_reports/` and your builders in `work/`, write the `README.md`
in the same shape as the others, add a row above, then commit. `.gitignore` already
tracks `task_inputs/` here (and only here).

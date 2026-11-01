# Start Here — contributor quick-start

One page to go from a fresh checkout to your first gated stage. It covers only
the things that stop you in the first hour: which universe your date selects,
where your task folder goes, the assignment file, the context command, the
search helpers, and the order of the 15 stage gates. The method lives in
`Guide/How_To_Author_A_Task.md`; the boundaries and numbers live in
`setup/GEN_EXECUTION.md`.

Run every command from the workspace root (the folder holding `Evals/`,
`claude/`, `Task_Authoring/`, `Universe_Normal/`, `Universe_SynthCut/`), and
always call Python as `python3 -B`.

## 1 · The two halves of the workspace

| Path | Role | You |
|---|---|---|
| `Evals/`, `claude/` | the evaluation half (search helpers, persona ACL, review skills) | **read-only** |
| `Universe_Normal/`, `Universe_SynthCut/` | the base data, one folder per universe | **read-only** |
| `Task_Authoring/` | the authoring half: skills, tools, template, guides | write here, inside your task folder |

`Task_Authoring/` designs and builds the task and checks it; the Eval Portal
reviews (`/injection`, `/prompt`, `/hardness`, `/oe`, `/rubric`) are run by you
against what it produces. The bundle never runs them for you and never writes
into `Evals/`.

## 2 · The 60-second version

```sh
# 1. See the stage order and what each gate writes
python3 -B Task_Authoring/tools/stage_gate.py --list

# 2. Create the task folder from the template (-n never overwrites a task already there;
#    for a second task use another folder and pass --task-dir, see §5)
cp -Rn Task_Authoring/references/Tasks_Template/. Task_Authoring/task_inputs/

# 3. Paste the platform assignment into 00_Assigments.md, then normalize it
python3 -B Task_Authoring/tools/task_context.py --task-dir Task_Authoring/task_inputs --write --require-source

# 4. Prove the installed data matches its manifests (both universes; ~5 min)
python3 -B Task_Authoring/tools/verify_universe_data.py

# 5. Prove the universe your task reads is readable: one entry per service, directory_present true
python3 -B Task_Authoring/tools/hg.py search inventory --task-dir Task_Authoring/task_inputs
```

Then start `/create-scenario` and follow the stage table in §7. Each `/create-*`
stage ends at its gate; nothing moves on until the gate prints PASS.

## 3 · Data layout (the old root `HarmonyGames_*` folders are gone)

| Universe | Folders | Clock | Persona "today" |
|---|---|---|---|
| `normal` | `Universe_Normal/Normal_HarmonyGames_{GitHub,Gmail,Other_Services}/` | 2026-02-14T00:00Z | Saturday, February 14, 2026 |
| `synthcut` | `Universe_SynthCut/SynthCut_HarmonyGames_{GitHub,Gmail,Other_Services}/` | 2025-10-01T07:00Z (= Oct 1 00:00 PT) | Wednesday, October 1, 2025 |

13 services per universe. Seed bound (`freeze_utc`) is `2026-02-14T00:00:00Z`
or `2025-10-01T00:00:00Z`; on synth-cut the data horizon (07:00Z) is later than
the seed bound, so late-arriving records exist but are never completed facts.

Two checks, different scopes. `verify_universe_data.py` needs no task folder: it
compares every service folder with its `source_manifest.json` (presence and sizes;
SHA-256 too with `--sha256`), flags split extractions (`X 2`), base folders left
at the workspace root and doubly nested ones, and prints `ALL OK` (exit 0) or
`PROBLEMS FOUND` (exit 1); restrict it with `--universe normal|synthcut`. The
task-scoped check is `hg.py search inventory`, which reports, per service,
`directory_present`, `manifest_present`, `source_file_count`, `source_bytes` and
`empty_export`, plus the archive name and `archive_sha256`; `--require-source`
refuses to ground anything unless the selected universe resolves. Installation,
extraction, moving, merging and verification are documented in the root `README.md`
— [Install the universe data](../../README.md#install-the-universe-data),
[Already unzipped? Move, merge and store the data](../../README.md#already-unzipped-move-merge-and-store-the-data)
and [Verify](../../README.md#verify) — so do not guess a layout, and never fall
back to the legacy `HarmonyGames_*` folders. The two universe folders are real
folders at the repo root, never edited and git-ignored; a symlink to another disk
is refused by the tools.

## 4 · Pick the universe by date — never infer it

The assignment's universe date selects the universe. There is no default: if the
date is missing or unrecognized, stop and ask, and read only the selected
universe for that task.

| Universe | Accepted displays (examples) |
|---|---|
| normal (2026-02-14) | `February 14, 2026 00:00` · `Feb 14, 2026 00:00` · `2026-02-14` · `2026-02-14 00:00` · `February 14, 2026` · `2026-02-14T00:00:00Z` |
| synthcut (2025-10-01) | `October 1, 2025 07:00` · `Oct 1, 2025 07:00` · `2025-10-01 00:00` |

Preserve the platform's text exactly; normalization happens in the mirror, not
in the platform block. Common rejections:

| Input | Result |
|---|---|
| `Feb 14 2026`, `14/02/2026` | `ASSIGNMENT FAIL: Unsupported universe date display '…'; preserve the platform value` |
| `2026-02-15` | `ASSIGNMENT FAIL: Universe date 2026-02-15 is not one of the V3 assigned dates` |

## 5 · The task folder and the assignment file

`Task_Authoring/task_inputs/` is the default task folder — the tools use it when
no task is given. For any other task, pass `--task-dir <dir>` or set
`TASK_AUTHORING_TASK_DIR=<abs dir>` in the environment.

```sh
cp -Rn Task_Authoring/references/Tasks_Template/. /abs/path/my-task/
python3 -B Task_Authoring/tools/task_context.py --task-dir /abs/path/my-task --write --require-source
```

Fill `<task_dir>/00_Assigments.md` exactly as the platform shows it: business
function, persona (with role), competency, task skill, task type, difficulty
mode, universe date. The eight assigned fields appear in seven groups because
Role sits inside Persona. Never substitute a persona, invent an email, or change
the difficulty mode. Keep every artifact of a task inside its own folder.

## 6 · What `task_context.py` gives you

```sh
python3 -B Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source
```

It writes `<task_dir>/Working_Files/00_Task_Context.json` and prints, among other
fields:

| Field | Meaning |
|---|---|
| `universe.key` / `universe.folder` / `universe.clock_utc` / `universe.clock_text` / `universe.persona_today` | which universe the date selected and what "today" means |
| `freeze_utc` | the seed bound (nothing seeded after it; nothing after it is a completed fact) |
| `universe.clock_utc` | the data horizon (eval `Clock:` line; synth-cut is 07:00Z) |
| `source.status` | must be `ready` before you ground any fact |
| `source.paths` | the exact data folders being read |
| `source.kb_status` | `bound` for both universes now |

Re-run it after editing the assignment or refreshing data. Its failures are the
most common first-day blockers:

| Message | Fix |
|---|---|
| `ASSIGNMENT FAIL: Missing V3 assigned fields: difficulty_mode` | fill all eight fields |
| `ASSIGNMENT FAIL: Assigned role 'Artist' disagrees with roster role 'Art Lead'; do not substitute it` | copy the roster role, do not reword it |
| `ASSIGNMENT FAIL: Assigned persona 'Nobody Here' resolves to 0 authorized roster entries` | the name is wrong or from the other universe; stop and ask |
| `ASSIGNMENT FAIL: Conflicting difficulty_mode at line 29: 'hard' versus 'medium'` | the platform block and the mirror disagree; they are one value |
| `ASSIGNMENT FAIL: Stale assignment mirror universe_date_key: '2025-10-01'; expected '2026-02-14'` | re-run with `--write` after fixing the date |
| `TASK CONTEXT FAIL: legacy V2 mode cannot run on a V3 assignment` (exit 2) | use the V3 template, not an old task folder |
| `TASK CONTEXT FAIL: V3 commands require a complete assignment…` (exit 2) | the platform block is incomplete |
| `SOURCE BLOCKED: Source service directories missing: … Install Universe_Normal/ per Evals/UNIVERSE_MAP.md` | data missing or misplaced; [install it](../../README.md#install-the-universe-data), do not fall back |

## 7 · Stages, skills and gates (in order)

`stage_gate.py --list` is the authority on writes and upstream dependencies;
`--help` shows the call form. The gate for any stage is:

```sh
python3 -B Task_Authoring/tools/stage_gate.py <stage> <task_dir> --paste
```

`<stage>` is positional and the task folder defaults to
`Task_Authoring/task_inputs`. `--paste` inserts the PASS block into the
artifact's Self-review, which is what the next stage requires.

| # | Skill (in `Task_Authoring/skills/*/SKILL.md`) | Writes | Gate |
|---|---|---|---|
| 0 | — (paste assignment) | `00_Assigments.md`, `Working_Files/00_Task_Context.json` | `task_context.py --require-source` says `ready` |
| 1 | `/create-scenario` | `01_Scenario_Design.md`, `01_Hardness_Manifest.draft.json`, `01_Gradable_Surface.json` | `hardness_gate.py --design`, `stage_gate.py scenario` |
| 2 | `/create-injection` | `01_Universe_Inject.sql`, `01_Hardness_Manifest.json`, `01_Grounding_Dossier.md`, `solver/solver.py`, `01c_Dispositions.json`, `01c_Preflight_Report.json` | `sql_lint`, `base_check`, `base_claims`, `hardness_gate`, `stage_gate.py injection` |
| 3 | `/create-error-async` *(optional)* | `03_Error_Async_Config.txt` | `stage_gate.py error-async` |
| 4 | `/create-reference-files` *(optional)* | `02_Reference_Files_Manifest.md` + `02_Reference_Files/` | `stage_gate.py reference-files` |
| 5 | `/create-prompt-writing` → draft/human → check | `04_Prompt_Writing_Brief.md`, `04_Prompt.txt`, `04_Prompt_Check.md` | `stage_gate.py prompt-writing`, then `stage_gate.py prompt-check` |
| 6 | `/create-humantime` | `Working_Files/05_Human_Time_Worksheet.md` | `stage_gate.py humantime` |
| 7 | *platform*: pre-check (1 Opus 5.5 run) → `/create-hardening` MODE B | `06_PreCheck_Trajectory/trajectory.json`, `01a_Hardening_Report.md` | `stage_gate.py hardening`; go / no-go recorded (advisory) |
| 8 | *platform*: baseline (6 Opus 5.5 rollouts) | `07_Baseline_Trajectories/` | all six finished |
| 9 | `/create-oe-writing` → draft/human → check | `08_OE_Writing_Ledger.md`, `08_Oracle_Events.md`, `08_OE_Check.md` | `stage_gate.py oe-writing`, then `stage_gate.py oe-check` |
| 10 | `/create-rubric-writing` → draft/human → check | `09_Rubric_Writing_Plan.md`, `09_Rubrics.json`, `09_Rubric_Check.md` | `stage_gate.py rubric-writing`, then `stage_gate.py rubric-check` |
| 11 | `/create-allfail` | `11_AF_Justification.md` | `stage_gate.py allfail` |
| 12 | `/create-difficulty` | `12_Difficulty_Stats.txt`, `12_difficulty_input.json` | `stage_gate.py difficulty` |
| 13 | `stage_gate.py release` | `13_Release_Gate.txt` | every earlier certificate current, one bundle digest |

`/create-hardening` and `/create-scenario --revise` are the revision loop, not a
one-way stage: the hardening report (MODE B) depends on `injection`, and
`--revise` is where its verdicts get dispositioned before the next injection.
`stage_gate.py --list` prints `hardening` in that dependency position, with
`01a_Hardening_Report.md` as its only write. The template's `05_Human_Time.md` is
the platform's human-time slot; `/create-humantime` writes the graded worksheet
into `Working_Files/` with the other generated artifacts.

Review skills from `claude/` sit between gates, in this order: `/injection`
after injection; `/injection` + `/prompt` after prompt-check; `/hardness` after
the pre-check intake; `/oe` after oe-check; `/rubric` after rubric-check. They
ask for the task date first (Oct 1, 2025 or Feb 14, 2026) — answer with the
assignment's display value, not a guess. A `/prompt` FAIL is fatal and sends you
back to the prompt or the universe.

## 8 · Search and injection checks

```sh
python3 -B Task_Authoring/tools/hg.py universe list                 # both universes
python3 -B Task_Authoring/tools/hg.py universe show --task-dir <task_dir>
python3 -B Task_Authoring/tools/hg.py search inventory --task-dir <task_dir>
python3 -B Task_Authoring/tools/hg.py search search slack "wind down" --limit 20 --task-dir <task_dir>
python3 -B Task_Authoring/tools/hg.py lint --task-dir <task_dir>     # injection lint
```

`hg.py` runs the Evals helpers from patched copies so their caches stay inside
`Task_Authoring/support/local_search/`. The other operations (`search-many`,
`lookup`, `get`, `get-many`, `records`, `reference routes`) take the same
arguments as `Evals/SEARCH.md`; follow its batching and paging rules. Search
tools ignore the persona ACL — prove reach with `persona_view.py`.

Every `records` item needs all six keys — `id`, `service`, `file`, `pointer`,
`field`, `values` (`"pointer": ""` for a root array). An item missing one gets
`{"error": "Each check needs id, service, file, pointer, field, values"}` and
exit 1; the check does not run.

## 9 · Knowledge base

Per-universe KBs live in `Task_Authoring/references/universe_kb/by_universe/{normal,synthcut}/`
and both report `bound`. The legacy root files are the old Feb-14 KB and are
reference-only: orientation, never validation authority.

After a data refresh, rebuild (GEN_EXECUTION §0a; one universe per run, about
4–13 minutes):

```sh
python3 -B Task_Authoring/tools/entity.py --task-dir <task_dir> build
python3 -B Task_Authoring/references/universe_kb/_build/run_all.py --task-dir <task_dir>
```

Never hand-edit generated KB files, and never write into the legacy root.

## 10 · Synth-cut differences worth knowing early

- 70 storylines against 76 on Feb 14: Combo Fighter, Zombie Match Lite, the
  Telegram Domino Delights port, the UI sprite optimization sprint, the Mattel
  Barbie idle life sim pitch and the web distribution partnership **do not exist**.
- Storyline text tagged `[normal-only]` marks facts that do not hold on synth-cut.
- The Feb 11, 2026 shutdown, the December 25, 2025 backdated terminations and the
  February 15, 2026 Google archive apply to normal only; synth-cut is a company
  operating normally. The departed-person rule applies to both: Victor Barnes
  left in April 2025 and cannot act.
- Seed bound (00:00Z) and data clock (07:00Z) differ. Never lean on a record from
  the 00:00–07:00Z window as a completed fact; treat it as a possible
  superseding record and drop any "current/latest" dependency it touches.
- The two clock checks are not the same. `hg.py lint` tests `future_date` against
  the 07:00Z data clock, `sql_lint.py` holds seeded rows to the 00:00Z seed
  bound; a seeded timestamp in between passes the eval lint and still fails
  `sql_lint.py`. Keep seeded timestamps before the seed bound — the injection
  gate runs both.

## 11 · Don'ts

- Never edit `Evals/`, `claude/`, `Universe_*` or the legacy
  `HarmonyGames_*` folders; never run `git` inside them.
- Never execute SQL; never modify base exports.
- Never invent an assignment value, email, role, date or freeze.
- Never hand-edit generated KB files or a generated `Working_Files/` artifact.
- Keep every task artifact in its own task folder; scratch work goes under
  `Task_Authoring/support/scratch/`.

## 12 · Where to read next

| Need | Read |
|---|---|
| Order, gates and loop-backs | `Guide/How_To_Author_A_Task.md` |
| Boundaries, numbers, universe rules | `setup/GEN_EXECUTION.md` (§0a for the two universes) |
| Raw commands behind each skill | `Guide/Manual_Commands.md` |
| What changed after P1 hardening | `Guide/Authoring_After_P1_Hardening.md` |
| Search request formats | `Evals/SEARCH.md` |
| Install and data layout | root `README.md` ([install](../../README.md#install-the-universe-data), [verify](../../README.md#verify)), `Evals/UNIVERSE_MAP.md` |

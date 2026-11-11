# Re-paste steps for SQL revision 14

SQL sha256 `edae63f3e83852f212c19892a9c9cf7304404b80db3178f92a470f301a598e13`, prompt sha256 `2a23afd87c4ca1b4736385b39bdeb2248119a8f4f33dcd8c3ff9acd8156a2beb`.

These replace every earlier list. Run them on the other PC, because this Mac's `hardness_gate` does not know `volume_exception.rows_floor`.

**How far this is tested.** The touch order was rehearsed on a scratch copy of this hash with read-only gates and a `touch` standing in for each paste: `structure.fresh` passed at all five stages. The re-bind, the real `--paste` and any PASS were not rehearsed.

**Rules for the whole run**
- Use `touch` for every re-save, never an editor on the SQL. Its sha must stay `edae63f3…`.
- Run from the workspace root with python 3.12 and `-B`.
- `--paste` writes only on PASS and replaces that stage's old block.
- A later content edit to one of these files means re-running from that stage.
- If a stage fails, stop there. Every later stage depends on it.

## Setup

1. In the workspace root on the other PC:
   ```
   export T=Task_Authoring/task_inputsS
   export TASK_AUTHORING_TASK_DIR=$T
   ```
2. Copy `task_inputsS` over, including `Working_Files/run_forensics/`, and confirm the hashes:
   ```
   shasum -a 256 $T/01_Universe_Inject.sql $T/04_Prompt.txt
   ```
3. Re-bind the context, because the hash embeds absolute paths:
   ```
   python3.12 -B Task_Authoring/tools/task_context.py --task-dir $T --write --require-source
   python3.12 -B $T/Working_Files/research/scripts/build_manifest.py
   ```
4. Copy `context_hash` from `$T/Working_Files/00_Task_Context.json` into `context_hash` in `$T/Working_Files/00_V3_Authoring_Evidence.json`.

## Stages, in this order

5. Scenario:
   ```
   cd $T/Working_Files && touch 01_Scenario_Design.md 01_Hardness_Manifest.draft.json 01_Gradable_Surface.json; cd -
   python3.12 -B Task_Authoring/tools/stage_gate.py scenario $T --paste
   ```
6. Injection (confirm the SQL sha is still `edae63f3…` before the gate):
   ```
   touch $T/01_Universe_Inject.sql
   cd $T/Working_Files && touch 01_Hardness_Manifest.json 01_Grounding_Dossier.md solver/solver.py 01c_Dispositions.json; cd -
   shasum -a 256 $T/01_Universe_Inject.sql
   python3.12 -B Task_Authoring/tools/preflight_report.py --task-dir $T --previous-sql $T/Working_Files/run_forensics/rev13/01_Universe_Inject.sql --previous-truth $T/Working_Files/run_forensics/rev13/truth.json
   python3.12 -B Task_Authoring/tools/stage_gate.py injection $T --paste
   ```
7. Error-async:
   ```
   touch $T/03_Error_Async_Config.txt
   python3.12 -B Task_Authoring/tools/stage_gate.py error-async $T --paste
   ```
8. Prompt-writing:
   ```
   touch $T/Working_Files/04_Prompt_Writing_Brief.md
   python3.12 -B Task_Authoring/tools/stage_gate.py prompt-writing $T --paste
   ```
9. Prompt-check:
   ```
   touch $T/Working_Files/04_Prompt_Check.md
   python3.12 -B Task_Authoring/tools/stage_gate.py prompt-check $T --paste
   ```

## What to expect

- With synced tools, `rows` (81 against 70), `per_record_calls` (96 against 75), `call_budget` (154 against 130) and the cohort (41 against 40) should pass on the exception floors.
- `forecast.preregistered`, `geometry.margin` and `handoff.pasted` are warnings, not blockers.
- If you pre-register the forecast and cite its id in a stage file, do that before step 6.

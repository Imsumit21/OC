# Rules for every reviewer in this local /prompt round

Workspace: /Users/sumit/Source/OC. Review folder (R): /private/tmp/claude-501/-Users-sumit-Source-OC/c183cff7-226e-4dae-964a-0d311047e48a/scratchpad/prompt_review_rev2

Task inputs, already supplied (do not ask for them):
- R/inputs/04_Prompt.txt — the exact prompt (sha256 45766344a3e4).
- R/inputs/01_Universe_Inject.sql — the injection SQL (yes, the task uses an injection; sha256 78af8ace66a9). It is a proposed overlay on the base universe: read it as text, never execute it.
- R/inputs/00_Task_Assigned_Inputs.md — the assignment (persona Leonard Hayes, leonard.hayes@harmonygames.co, Co-founder & Creative Director; Executive; Finance; Authoring; long-horizon; difficulty medium).
- R/inputs/02_Universe_Date.txt — the task date: Feb 14, 2026 (normal universe). Use this Clock line verbatim: `Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)`.

How to work here (local procedure; the Evals input store is write-blocked on this machine):
- Do NOT run `Evals/tools/hg_store_input.py` or any tool that writes under `Evals/`. Treat the inputs above as saved.
- Search the universe ONLY with `~/.local/bin/python3.12 -B Task_Authoring/tools/hg.py search <cmd> ... --task-dir Task_Authoring/task_inputs` (cmds: inventory, files, search, search-many, get, get-many, lookup; `--help` on each). It reads the base universe only; overlay records are in the SQL. Apply the persona's visibility yourself (Evals/references/persona/acl.md, roster.json).
- Rule documents (read-only): Evals/1_Prompt_Eval.md, Evals/0_Injection_Quality_Eval.md, Evals/WORKFLOW.md, Evals/EXECUTION.md, Evals/ENVIRONMENT.md, Evals/references/rules/deep_recheck.md, Evals/references/rules/*, Evals/references/tools/catalog.json, Evals/references/persona/*.
- The platform's known-issue list (cited by the Portal as known_base_issues.md) is Task_Authoring/references/known_data_issues/normal.md.
- Do NOT open anything under Task_Authoring/task_inputs/ (it holds the answer key), Task_Authoring/support/, or any research or Working_Files folder, and do not read other reviewers' files in R/out/ unless your brief says so.
- Write ONLY to your own file under R/out/. Write its skeleton first, then fill it as each check finishes, so nothing is lost if you run out of steps.
- Never execute SQL. No git. Use they/them for people.

Bar for Unique Ground Truth findings (deep_recheck.md): a fork counts as open unless a quoted, Leonard-reachable record rules out the other reading. "Weak", "additive" or "superset" are not grounds to reject a fork. An owner's own claim about its own gap is not a settling record (basis SCOPE_GAP); no record at all is SILENCE (open). Quote record ids and pointers for every finding.

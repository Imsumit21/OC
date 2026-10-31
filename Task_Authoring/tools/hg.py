#!/usr/bin/env python3
"""Run the Evals search helpers without writing anything into Evals/ and on the task's universe.

Same commands and arguments as the Evals helpers (Evals/SEARCH.md), run from patched
copies in Task_Authoring/support/local_search/[contexts/<hash20>/]tools/ so their caches
stay inside the bundle. The assignment date selects the universe; helpers read the
context's published date index, never the eval bundle's saved task date. Run from the
workspace root:

  python3 Task_Authoring/tools/hg.py search  inventory
  python3 Task_Authoring/tools/hg.py search  search slack "wind down" --limit 20
  python3 Task_Authoring/tools/hg.py search  get contacts --file contacts.json --pointer /0
  python3 Task_Authoring/tools/hg.py search  search-many --request req.json
  python3 Task_Authoring/tools/hg.py records --request checks.json
  python3 Task_Authoring/tools/hg.py reference routes slack
  python3 Task_Authoring/tools/hg.py context <stage>
  python3 Task_Authoring/tools/hg.py universe [show|list]
  python3 Task_Authoring/tools/hg.py lint [--sql PATH] [--checks a,b] [--no-base] [--summary]
  python3 Task_Authoring/tools/hg.py rubric-lint <rubric.json>

The task (and so the universe) comes from `--task-dir <dir>` or TASK_AUTHORING_TASK_DIR, else
Task_Authoring/task_inputs/. `search` = hg_search.py, `records` = hg_records.py, `reference` = hg_reference.py,
`context` = hg_context.py, `universe` = hg_universe.py, `lint` = hg_injection_lint.py,
`rubric-lint` = hg_rubric_lint.py. `lint` defaults `--sql` to
<TASK_AUTHORING_TASK_DIR>/01_Universe_Inject.sql. The upstream linter exits 0 even with
FAIL flags: its JSON is passed through unchanged for the stage gate to judge. Search,
records, reference and base-backed lint need a ready source; context, universe,
rubric-lint and `lint --no-base` only need a V3 task context. The patched copies are
refreshed from Evals/tools on every call (cheap; rewrites only changed files).
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "setup"))
from local_search import build  # noqa: E402

HELPERS = {"search": "hg_search.py", "records": "hg_records.py", "reference": "hg_reference.py",
           "context": "hg_context.py", "universe": "hg_universe.py",
           "lint": "hg_injection_lint.py", "rubric-lint": "hg_rubric_lint.py"}
SOURCE_FREE = {"context", "universe", "rubric-lint"}
WORKSPACE = HERE.parent.parent
EVAL_TASK_INPUTS = WORKSPACE / "Evals" / "task_inputs"


def _inside_eval_inputs(argument: str) -> bool:
    """File-identity check, so case variants and symlinks into Evals/task_inputs are refused too."""
    from task_context import within
    candidates = []
    if argument.startswith("--") and "=" in argument:
        candidates.append(argument.split("=", 1)[1])  # an --opt=value value is a path even when it starts with '-'
    if not argument.startswith("-") or Path(argument).exists():
        candidates.append(argument)                   # a dash-led token is an option unless it exists (a file named '-')
    return any(value and within(Path(value), EVAL_TASK_INPUTS) for value in candidates)


def requires_source(argv: list[str]) -> bool:
    command = argv[0] if argv else ""
    if command in SOURCE_FREE:
        return False
    if command == "lint":
        return "--no-base" not in argv[1:]
    return True


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in HELPERS:
        print(__doc__, file=sys.stderr)
        return 2
    command, args = argv[0], list(argv[1:])
    context = globals().get("TASK_CONTEXT")
    if command == "context" and context:
        # Old Evals scoring remains a reference, not the V3 policy of record.
        import json
        print(json.dumps({"task_context": context,
                          "v3_policy": json.loads((HERE.parent / "references" / "v3_policy.json").read_text()),
                          "legacy_reference": "Evals/references/rules/scoring.json; superseded topics do not override V3"}, indent=2))
        return 0
    if command == "universe" and not args:
        args = ["show"]
    if command == "lint" and not any(a == "--sql" or a.startswith("--sql=") for a in args):
        task_dir = Path(os.environ.get("TASK_AUTHORING_TASK_DIR") or (HERE.parent / "task_inputs"))
        args += ["--sql", str((task_dir / "01_Universe_Inject.sql").resolve())]
    if command == "rubric-lint" and not any(not a.startswith("-") for a in args):
        print("rubric-lint requires a rubric path argument: hg.py rubric-lint <rubric.json>", file=sys.stderr)
        return 2
    # Checked on the final arguments, after defaults such as lint's --sql are filled in.
    refused = [a for a in args if _inside_eval_inputs(a)]
    if refused:
        print("Task_Authoring never reads <workspace>/Evals/task_inputs/ (" + ", ".join(refused) + "); "
              "task inputs live under Task_Authoring/task_inputs/", file=sys.stderr)
        return 2
    built = build()
    script = Path(built["local_tools"]) / HELPERS[command]
    return subprocess.call([sys.executable, str(script), *args])


if __name__ == "__main__":
    if sys.argv[1:] in (["-h"], ["--help"]):    # usage needs no task context
        print(__doc__)
        raise SystemExit(0)
    from runtime_context import guarded_entry
    guarded_entry(globals(), require_source=requires_source(sys.argv[1:]))
    raise SystemExit(main(sys.argv[1:]))

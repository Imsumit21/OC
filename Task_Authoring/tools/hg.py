#!/usr/bin/env python3
"""Run the Evals search helpers without writing anything into Evals/.

Same commands and arguments as the Evals helpers (Evals/SEARCH.md), run from patched
copies in Task_Authoring/support/local_search/tools/ so their caches stay inside the bundle
(Task_Authoring/support/local_search/cache/). Run it from the workspace root:

  python3 Task_Authoring/tools/hg.py search  inventory
  python3 Task_Authoring/tools/hg.py search  search slack "wind down" --limit 20
  python3 Task_Authoring/tools/hg.py search  get contacts --file contacts.json --pointer /0
  python3 Task_Authoring/tools/hg.py search  search-many --request req.json
  python3 Task_Authoring/tools/hg.py records --request checks.json
  python3 Task_Authoring/tools/hg.py reference routes slack
  python3 Task_Authoring/tools/hg.py context <stage>

`search` = hg_search.py, `records` = hg_records.py, `reference` = hg_reference.py,
`context` = hg_context.py. The patched copies are refreshed from Evals/tools on every
call (cheap; rewrites only changed files).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "setup"))
from local_search import LOCAL, build  # noqa: E402

HELPERS = {"search": "hg_search.py", "records": "hg_records.py",
           "reference": "hg_reference.py", "context": "hg_context.py"}


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in HELPERS:
        print(__doc__, file=sys.stderr)
        return 2
    context = globals().get("TASK_CONTEXT")
    if argv[0] == "context" and context:
        # Old Evals scoring remains a reference, not the V3 policy of record.
        import json
        print(json.dumps({"task_context": context,
                          "v3_policy": json.loads((HERE.parent / "references" / "v3_policy.json").read_text()),
                          "legacy_reference": "Evals/references/rules/scoring.json; superseded topics do not override V3"}, indent=2))
        return 0
    built = build()
    args = list(argv[1:])
    script = Path(built["local_tools"]) / HELPERS[argv[0]]
    return subprocess.call([sys.executable, str(script), *args])


if __name__ == "__main__":
    from runtime_context import guarded_entry
    guarded_entry(globals(), require_source=not (len(sys.argv) > 1 and sys.argv[1] == "context"))
    raise SystemExit(main(sys.argv[1:]))

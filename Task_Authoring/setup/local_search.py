#!/usr/bin/env python3
"""Build or refresh Task_Authoring/support/local_search/ — the Evals search helpers, minus writes to Evals/.

The Evals helpers (`Evals/tools/hg_*.py`) write runtime caches under `Evals/.cache/`.
`Evals/` is read-only for this bundle, so the helpers run from **patched copies** in
`Task_Authoring/support/local_search/tools/`. Two literal patches, nothing else:

  1. `Path(__file__).resolve().parents[2]` -> `parents[N]`, N = the copies' depth below the
     workspace (so the workspace root — and every data path — stays exactly the same)
  2. `Evals/.cache/<x>` -> `Task_Authoring/support/local_search/cache/<x>`  (cache writes stay
     inside the bundle; the helpers' "cache must sit under the root" checks still hold)

Data, references and docs are read from their real locations. Nothing under `Evals/`,
`claude/` or `HarmonyGames_*` is created, changed or deleted.

  python3 Task_Authoring/setup/local_search.py            # build / refresh (idempotent)
  python3 Task_Authoring/setup/local_search.py --check    # report what would change
Normally you never call it: `Task_Authoring/tools/hg.py` refreshes it on every use.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parent.parent          # Task_Authoring/
WORKSPACE = BUNDLE.parent                                 # the workspace root (holds Evals/)
LOCAL = BUNDLE / "support" / "local_search"
TOOLS = LOCAL / "tools"
CACHE_REL = f"{BUNDLE.name}/support/local_search/cache"
# Helpers that write task inputs/reports into Evals/ are never copied, so they cannot run from here.
SKIP = {"hg_store_input.py", "hg_write_output.py", "hg_preflight.py"}


def patched(text: str) -> str:
    depth = len(TOOLS.relative_to(WORKSPACE).parts)
    text = text.replace("Path(__file__).resolve().parents[2]", f"Path(__file__).resolve().parents[{depth}]")
    text = text.replace("'Evals/.cache/", f"'{CACHE_REL}/").replace('"Evals/.cache/', f'"{CACHE_REL}/')
    # hg_records walks the cache path component by component
    text = text.replace("for part in ('Evals', '.cache', 'records'):",
                        "for part in (" + ", ".join(repr(p) for p in CACHE_REL.split("/") + ["records"]) + "):")
    # Each helper still fingerprints the selected source manifest. No Evals file is edited.
    if "Evals/references/universe_manifest.json" in text:
        if "from pathlib import Path" in text:
            text = text.replace("from pathlib import Path", "from pathlib import Path\nimport os as _ta_os", 1)
            text = re.sub(r"(h\.ROOT|ROOT) / 'Evals/references/universe_manifest.json'",
                          lambda m: "Path(_ta_os.environ.get('TASK_AUTHORING_UNIVERSE_MANIFEST', str(" + m.group(0) + ")))", text)
    return text


def build(check: bool = False) -> dict:
    global LOCAL, TOOLS, CACHE_REL
    context_hash = os.environ.get("TASK_AUTHORING_CONTEXT_HASH")
    if context_hash:
        if not re.fullmatch(r"[0-9a-f]{64}", context_hash):
            raise SystemExit("Invalid task context cache namespace")
        LOCAL = BUNDLE / "support" / "local_search" / "contexts" / context_hash[:20]
        TOOLS = LOCAL / "tools"
        CACHE_REL = str((LOCAL / "cache").relative_to(WORKSPACE))
    src_dir = WORKSPACE / "Evals" / "tools"
    if not (src_dir / "hg_search.py").is_file():
        raise SystemExit("Evals/tools/hg_search.py not found — keep Task_Authoring/ beside Evals/.")
    changes: list[str] = []
    if not check:
        TOOLS.mkdir(parents=True, exist_ok=True)
        (LOCAL / "cache").mkdir(parents=True, exist_ok=True)
    for src in sorted(src_dir.glob("*.py")):
        if src.name in SKIP:
            continue
        dst = TOOLS / src.name
        new = patched(src.read_text())
        if not dst.is_file() or dst.read_text() != new:
            changes.append(f"copy+patch tools/{src.name}")
            if not check:
                dst.write_text(new)
    if TOOLS.is_dir():
        for stale in sorted(TOOLS.glob("*.py")):
            if stale.name in SKIP or not (src_dir / stale.name).exists():
                changes.append(f"remove stale tools/{stale.name}")
                if not check:
                    stale.unlink()
    leftover = [p.name for p in TOOLS.glob("*.py") if "Evals/.cache" in p.read_text()] if TOOLS.is_dir() else []
    return {"local_tools": str(TOOLS), "cache": str(LOCAL / "cache"), "check_only": check,
            "changes": changes, "unpatched_cache_refs": leftover}


if __name__ == "__main__":
    print(json.dumps(build("--check" in sys.argv[1:]), indent=2))

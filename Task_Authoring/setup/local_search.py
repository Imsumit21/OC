#!/usr/bin/env python3
"""Build or refresh Task_Authoring/support/local_search/ — the Evals search helpers, minus writes to Evals/.

The Evals helpers (`Evals/tools/hg_*.py`) write runtime caches under `Evals/.cache/`.
`Evals/` is read-only for this bundle, so the helpers run from **patched copies** in
`Task_Authoring/support/local_search/[contexts/<hash20>/]tools/`. Patches, nothing else:

  1. `Path(__file__).resolve().parents[2]` -> `parents[N]`, N = the copies' depth below the
     workspace (so the workspace root — and every data path — stays exactly the same)
  2. `Evals/.cache/<x>` -> `Task_Authoring/support/local_search[/contexts/<hash20>]/cache/<x>`
     (cache writes stay inside the bundle; the helpers' "cache must sit under the root" checks hold)
  3. `hg_universe.INDEX` -> `<context>/universe/inputs.json`, an index this script publishes from
     TASK_AUTHORING_UNIVERSE (never the eval bundle's own saved task date). Without an activated
     task context the index is a sentinel path that never exists.
  4. every other `Evals/task_inputs` literal -> `Task_Authoring/support/local_search/NO_EVAL_TASK_INPUTS`
     (task inputs belong to Task_Authoring, not to the read-only eval bundle).

Data, references and docs are read from their real locations. Nothing under `Evals/`,
`claude/` or `HarmonyGames_*` is created, changed or deleted.

  python3 Task_Authoring/setup/local_search.py            # build / refresh (idempotent)
  python3 Task_Authoring/setup/local_search.py --check    # report what would change
Normally you never call it: `Task_Authoring/tools/hg.py` refreshes it on every use.
"""
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

BUNDLE = Path(__file__).resolve().parent.parent          # Task_Authoring/
WORKSPACE = BUNDLE.parent                                 # the workspace root (holds Evals/)
LOCAL = BUNDLE / "support" / "local_search"
TOOLS = LOCAL / "tools"
CACHE_REL = f"{BUNDLE.name}/support/local_search/cache"
# Helpers that write task inputs/reports into Evals/ are never copied, so they cannot run from here.
SKIP = {"hg_store_input.py", "hg_write_output.py", "hg_preflight.py"}
TASK_INPUTS = "Evals/task_inputs"
TASK_INPUTS_SENTINEL = "Task_Authoring/support/local_search/NO_EVAL_TASK_INPUTS"
UNIVERSE_FILE = "hg_universe.py"
INDEX_ANCHOR = "INDEX = Path('Evals/task_inputs/inputs.json')"
UNIVERSE_SENTINEL_INDEX = TASK_INPUTS_SENTINEL + "/universe/inputs.json"
TASK_CONTEXT_TOOL = Path(__file__).resolve().parent.parent / "tools" / "task_context.py"


def _rel(path: Path, workspace: Path | None = None) -> str:
    return Path(os.path.relpath(path, workspace or WORKSPACE)).as_posix()


def patched(text: str, tools: Path | None = None, cache_rel: str | None = None) -> str:
    tools = Path(tools) if tools is not None else TOOLS
    cache_rel = cache_rel or CACHE_REL
    depth = len(tools.resolve().relative_to(WORKSPACE.resolve()).parts)
    text = text.replace("Path(__file__).resolve().parents[2]", f"Path(__file__).resolve().parents[{depth}]")
    text = text.replace("'Evals/.cache/", f"'{cache_rel}/").replace('"Evals/.cache/', f'"{cache_rel}/')
    # hg_records walks the cache path component by component
    text = text.replace("for part in ('Evals', '.cache', 'records'):",
                        "for part in (" + ", ".join(repr(p) for p in cache_rel.split("/") + ["records"]) + "):")
    return text


def _universes() -> dict:
    """The bundled universe registry, read without writing bytecode into Evals/."""
    source = WORKSPACE / "Evals" / "tools" / UNIVERSE_FILE
    if not source.is_file():
        raise SystemExit("Evals/tools/hg_universe.py not found — install the dual-universe Evals bundle")
    spec = importlib.util.spec_from_file_location("_ta_local_search_universe", source)
    if spec is None or spec.loader is None:
        raise SystemExit("Evals/tools/hg_universe.py cannot be loaded as a module")
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module.UNIVERSES


def _atomic(path: Path, data: bytes) -> None:
    """Install bytes at path without ever opening an existing file: a fresh, exclusively created temp file
    (random name, O_EXCL) is written through its own descriptor, then renamed over the destination."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(dir=path.parent, prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            os.fchmod(handle.fileno(), 0o644)
            handle.write(data)
        os.replace(temp, path)
    except BaseException:
        with contextlib.suppress(FileNotFoundError):
            os.unlink(temp)
        raise


def _universe_plan(local: Path, key: str | None, universes: dict, changes: list[str]) -> list[tuple[Path, bytes]]:
    """Date file + saved-date index for one context dir; identical bytes are never rewritten."""
    folder = local / "universe"
    date_path = folder / "02_Universe_Date.txt"
    index_path = folder / "inputs.json"
    if not key:
        return []
    raw = (universes[key]["date"] + "\n").encode()
    date_rel = _rel(date_path)
    existing = json.loads(index_path.read_text()) if index_path.is_file() else None
    previous = None
    if existing:
        entry = existing.get("inputs", {}).get("universe", {})
        files = entry.get("files") or []
        if entry.get("state") == "saved" and len(files) == 1:
            try:
                shown = (WORKSPACE / files[0]["path"]).read_text().strip()
            except (OSError, KeyError, TypeError):
                shown = None
            if shown:
                previous = next((k for k, v in universes.items() if v["date"] == shown), shown)
    if previous is not None and previous != key:
        raise SystemExit(f"Universe index {_rel(index_path)} names {previous!r}, not {key!r}: "
                         "context hash/universe mismatch")
    revision = max(int((existing or {}).get("revision") or 0), 1)
    index = {"format_version": 1, "revision": revision,
             "inputs": dict((existing or {}).get("inputs") or {})}
    index["inputs"]["universe"] = {"state": "saved", "revision": revision, "files": [{
        "filename": date_path.name, "path": date_rel, "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest()}]}
    data = (json.dumps(index, indent=2) + "\n").encode()
    writes = []
    if not date_path.is_file() or date_path.read_bytes() != raw:
        changes.append(f"write {date_rel} ({key})")
        writes.append((date_path, raw))
    if not index_path.is_file() or index_path.read_bytes() != data:
        changes.append(f"write {_rel(index_path)} ({key})")
        writes.append((index_path, data))
    return writes


def _task_context_module():
    """The real task-context loader, imported by path without writing bytecode."""
    spec = importlib.util.spec_from_file_location("_ta_local_search_task_context", TASK_CONTEXT_TOOL)
    if spec is None or spec.loader is None:
        raise SystemExit("Task_Authoring/tools/task_context.py cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def _validate_context(context_hash: str, universe: str) -> None:
    """A published date must come from this task's own activated context, never forged env."""
    task_dir = os.environ.get("TASK_AUTHORING_TASK_DIR")
    if not task_dir:
        raise SystemExit("universe selection requires TASK_AUTHORING_TASK_DIR (an activated task context)")
    try:
        context = _task_context_module().load_context(Path(task_dir))
    except Exception as exc:  # ContextError and unreadable/invalid assignments alike
        raise SystemExit(f"universe selection: cannot load the task context in {task_dir}: {exc}") from None
    if context.get("context_hash") != context_hash:
        raise SystemExit(f"universe selection: TASK_AUTHORING_CONTEXT_HASH does not match the task context in "
                         f"{task_dir}: context hash mismatch")
    key = (context.get("universe") or {}).get("key")
    if key != universe:
        raise SystemExit(f"universe selection: the task context in {task_dir} selects {key!r}, not {universe!r}: "
                         "hash/universe mismatch")


def build(check: bool = False) -> dict:
    context_hash = os.environ.get("TASK_AUTHORING_CONTEXT_HASH")
    universe = os.environ.get("TASK_AUTHORING_UNIVERSE") or None
    if universe and not context_hash:
        raise SystemExit("universe selection requires an activated task context")
    if context_hash and not re.fullmatch(r"[0-9a-f]{64}", context_hash):
        raise SystemExit("Invalid task context cache namespace")
    if universe:
        _validate_context(context_hash, universe)
    local = (BUNDLE / "support" / "local_search" / "contexts" / context_hash[:20]) if context_hash \
        else (BUNDLE / "support" / "local_search")
    tools = local / "tools"
    # Every output folder must resolve inside Task_Authoring/ (a symlinked ancestor must never redirect
    # copies, caches or the universe index into Evals/ or any other read-only folder).
    bundle_real = BUNDLE.resolve()
    for out_dir in (local, tools, local / "cache", local / "universe"):
        real = out_dir.resolve()
        if real != bundle_real and bundle_real not in real.parents:
            raise SystemExit(f"Refusing to build into {_rel(out_dir)}: it resolves outside Task_Authoring/ ({real})")
    cache_rel = _rel(local / "cache")
    index_rel = _rel(local / "universe" / "inputs.json") if context_hash else UNIVERSE_SENTINEL_INDEX
    src_dir = WORKSPACE / "Evals" / "tools"
    if not (src_dir / "hg_search.py").is_file():
        raise SystemExit("Evals/tools/hg_search.py not found — keep Task_Authoring/ beside Evals/.")
    changes: list[str] = []
    # Patch and validate every copy in memory before anything is written.
    planned: dict[str, str] = {}
    missing: list[str] = []
    leftovers: list[str] = []
    for src in sorted(src_dir.glob("*.py")):
        if src.name in SKIP:
            continue
        text = src.read_text()
        if src.name == UNIVERSE_FILE:
            if INDEX_ANCHOR not in text:
                missing.append(src.name)
                continue
            text = text.replace(INDEX_ANCHOR, "INDEX = Path(%r)" % index_rel, 1)
        text = patched(text, tools, cache_rel).replace(TASK_INPUTS, TASK_INPUTS_SENTINEL)
        if TASK_INPUTS in text:
            leftovers.append(src.name)
        planned[src.name] = text
    if not (src_dir / UNIVERSE_FILE).is_file():
        missing.append(UNIVERSE_FILE)
    if missing:
        raise SystemExit("Required patch anchor missing in copied tool(s): " + ", ".join(sorted(set(missing))))
    if leftovers:
        raise SystemExit("Patched tool(s) still reference Evals/task_inputs: " + ", ".join(sorted(leftovers)))
    universes = _universes() if universe else {}
    if universe and universe not in universes:
        raise SystemExit(f"Unknown universe {universe!r}; expected one of: {', '.join(sorted(universes))}")
    universe_writes = _universe_plan(local, universe, universes, changes)
    if not check:
        tools.mkdir(parents=True, exist_ok=True)
        (local / "cache").mkdir(parents=True, exist_ok=True)
    for name, text in planned.items():
        dst = tools / name
        # A linked destination is always replaced, and every copy is installed by temp + os.replace:
        # the directory entry changes, so nothing is ever written through a symlink or hard link.
        if dst.is_symlink() or not dst.is_file() or dst.read_text() != text:
            changes.append(f"copy+patch tools/{name}")
            if not check:
                _atomic(dst, text.encode())
    if tools.is_dir():
        for stale in sorted(tools.glob("*.py")):
            if stale.name in SKIP or stale.name not in planned:
                changes.append(f"remove stale tools/{stale.name}")
                if not check:
                    stale.unlink()
    for path, data in universe_writes:
        if not check:
            _atomic(path, data)
    if not universe and (local / "universe").is_dir():
        changes.append("remove universe/ (no activated task context)")
        if not check:
            shutil.rmtree(local / "universe")
    unpatched = [name for name, text in planned.items() if "Evals/.cache" in text]
    return {"local_tools": str(tools), "cache": str(local / "cache"), "check_only": check,
            "universe": universe,
            "universe_index": _rel(local / "universe" / "inputs.json") if universe else None,
            "changes": changes, "unpatched_cache_refs": unpatched}


if __name__ == "__main__":
    print(json.dumps(build("--check" in sys.argv[1:]), indent=2))

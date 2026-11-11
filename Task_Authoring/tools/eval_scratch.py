#!/usr/bin/env python3
"""eval_scratch.py - a per-task copy of the evaluator, so two tasks never share one input store (plan WS7 item 2).

Why. The evaluator keeps one saved task and one saved universe date in its input store under Evals/, with no lock.
Each Evals tool finds its workspace from its own file (two folders up), so a real copy of Evals/ in another folder
has its own store. This tool builds that copy per task and proves the store is separate.

Layout: Task_Authoring/support/scratch/evals_<task folder>-<id10>/
  scratch.json            what was built, for which task
  tmp/                    TMPDIR for evaluator runs (the Evals tools call tempfile without a folder)
  ws/Evals/               real copies of everything in Evals/ except the input store, .cache and __pycache__;
                          the input store folder starts empty; caches are rebuilt here on first use.
                          The prepared universe indexes (references/universes/) are copied too, not linked:
                          hg_id_index.py and hg_compact_index.py can write there, and a write through a link
                          would land in the real Evals/.
  ws/claude               symlink to the real claude/ (read-only skills)
  ws/Universe_<X>         the universe of the task's date only: an APFS copy-on-write clone (default on macOS:
                          no data is copied, the original is not touched) or a symlink (--universe-data symlink)

Limit found while building it. The Evals search tools resolve every data file (hg_search.py safe_file()) and then
print it relative to their workspace (`p.relative_to(ROOT)` in search and get). A symlinked universe resolves into the
real workspace, so in symlink mode a search, get or lookup that returns a record fails with "is not in the subpath";
the store, the reference views, inventory and file listings still work. Clone mode has no such limit. `create`
runs one real record read and reports which case holds. Measured on 2026-11-11 (Universe_Normal, 384,377 files):
clone mode built in about 70 s and every check passed, including a search with hits; symlink mode built in 6 s with
record reads failing as described. Nothing under the real Evals/ changed in either run. No Evals tool was edited:
hg_store_input.py finds its store from its own file (parents[2]), so a real copy has its own store.

Commands
  create --task-dir T [--universe-data auto|clone|symlink] [--date D] [--force]
      builds the scratch (or checks an existing one), then proves it: runs `hg_store_input.py list` and
      `hg_store_input.py universe <task date>` inside it, checks the write landed in the scratch store, and compares
      a listing (sizes and mtimes) of the real Evals/ before and after. Any difference fails the command.
      Prints the scratch path and the command prefix for evaluator tools.
  status --task-dir T     what the scratch holds and whether the real Evals/ changed since it was copied
  remove --task-dir T     delete the scratch
  list                    every evaluator scratch under support/scratch/
  --self-test

It never writes into the real Evals/, claude/ or Universe_*/. API: evaluate(task_dir) is `status` (reads only);
create(...), remove(...), list_scratches(...).

Exit: 0 PASS or WARN, 1 FAIL, 2 usage error. Stdlib only.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WS = BUNDLE.parent
sys.path.insert(0, str(HERE))

TOOL = "eval_scratch"
VERSION = 1
SCHEMA = "eval-scratch-v1"
SCRATCH = BUNDLE / "support" / "scratch"
PREFIX = "evals_"
EVALS = "Evals"
STORE = "task_inputs"                       # the evaluator's input store folder, inside Evals/
NOT_COPIED = (STORE, ".cache", "__pycache__")
DATE_FILE = "02_Universe_Date.txt"
STORE_TOOL = Path(EVALS) / "tools" / "hg_store_input.py"
SEARCH_TOOL = Path(EVALS) / "tools" / "hg_search.py"
UNIVERSE_TOOL = Path(EVALS) / "tools" / "hg_universe.py"
DATA_MODES = ("auto", "clone", "symlink")
DEFAULT_UNIVERSE_DATA = "auto"              # clone where the file system can, else symlink with a warning
RUN_TIMEOUT = 900


class ScratchError(RuntimeError):
    """The scratch cannot be built or checked."""


class CloneUnsupported(ScratchError):
    """This platform or volume cannot make copy-on-write clones."""


# ---------------------------------------------------------------- small helpers

def _check(checks, check_id, status, detail) -> None:
    checks.append({"id": check_id, "status": status, "detail": " ".join(str(detail).split())})


def _inside(path, root) -> bool:
    try:
        Path(path).resolve().relative_to(Path(root).resolve())
    except ValueError:
        return False
    return True


def _sha_file(path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _atomic_write(path: Path, data: bytes, what: str) -> None:
    from task_context import refuse_read_only
    refuse_read_only(path, what)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            os.fchmod(handle.fileno(), 0o644)
            handle.write(data)
        os.replace(temp, path)
    except BaseException:
        if os.path.lexists(temp):
            os.unlink(temp)
        raise


def scratch_identity(task_dir) -> str:
    """`<task folder name>-<first 10 hex of the bundle's task identity>`. The identity is the one stage_evidence
    uses (a hash of the resolved folder path), so two folders never share a scratch."""
    from stage_evidence import task_identity
    task_dir = Path(task_dir).resolve()
    label = re.sub(r"[^A-Za-z0-9._-]+", "_", task_dir.name).strip("_") or "task"
    return f"{label}-{task_identity(task_dir)[:10]}"


def scratch_root(task_dir, scratch=None) -> Path:
    return Path(scratch or SCRATCH) / (PREFIX + scratch_identity(task_dir))


def listing(folder) -> dict:
    """{relative path: [kind, size, mtime_ns]} for every entry under a folder; links are not followed."""
    folder = Path(folder)
    out = {}
    for base, dirs, files in os.walk(folder):
        for name in dirs + files:
            path = os.path.join(base, name)
            info = os.lstat(path)
            kind = "link" if os.path.islink(path) else "dir" if os.path.isdir(path) else "file"
            out[os.path.relpath(path, folder)] = [kind, 0 if kind == "dir" else info.st_size, info.st_mtime_ns]
    return out


def listing_diff(before, after) -> list:
    changes = [f"added {p}" for p in sorted(set(after) - set(before))]
    changes += [f"removed {p}" for p in sorted(set(before) - set(after))]
    changes += [f"changed {p}" for p in sorted(set(before) & set(after)) if before[p] != after[p]]
    return changes


def content_digest(evals_dir) -> tuple:
    """(digest over path + sha256 of every copied file, number of files): tells a stale copy from a current one."""
    evals_dir = Path(evals_dir)
    digest, count = hashlib.sha256(), 0
    for base, dirs, files in os.walk(evals_dir):
        dirs[:] = sorted(d for d in dirs if not (Path(base) == evals_dir and d in NOT_COPIED) and d != "__pycache__")
        for name in sorted(files):
            if name.endswith((".pyc", ".pyo")) or name == ".DS_Store":
                continue
            path = Path(base) / name
            digest.update(f"{path.relative_to(evals_dir).as_posix()}\0{_sha_file(path)}\n".encode())
            count += 1
    return digest.hexdigest(), count


def _universes(source_ws):
    """The evaluator's universe registry and its date parser, loaded from the source Evals/ without bytecode."""
    source = Path(source_ws) / UNIVERSE_TOOL
    if not source.is_file():
        raise ScratchError(f"{source} not found: this is not a workspace with the dual-universe Evals bundle")
    spec = importlib.util.spec_from_file_location("_eval_scratch_universe", source)
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def task_universe(task_dir, date=None, source_ws=None) -> dict:
    """The universe the task's assigned date selects: {key, date, folder, label}. Never guessed."""
    module = _universes(source_ws or WS)
    raw = date
    if raw is None:
        from task_context import ContextError, parse_assignment
        path = Path(task_dir) / "00_Assigments.md"
        try:
            raw = parse_assignment(path.read_text(encoding="utf-8"))[0]["universe_date_raw"]
        except (OSError, ContextError, KeyError) as exc:
            raise ScratchError(f"cannot read the task date from {path}: {exc}. Fill the assignment, or pass --date.")
    text = str(raw).strip()
    iso = re.match(r"^(\d{4}-\d{2}-\d{2})", text)
    try:
        key = module.parse(iso.group(1) if iso else re.sub(r"\s+\d{1,2}:\d{2}.*$", "", text))
    except ValueError as exc:
        raise ScratchError(f"the task date {raw!r} is not one of the two universe dates: {exc}")
    entry = module.UNIVERSES[key]
    return {"key": key, "date": entry["date"], "folder": entry["folder"], "label": entry["label"]}


# ---------------------------------------------------------------- building

def _clone_function():
    """macOS clonefile(2), or None where it does not exist. It fails rather than falling back to a full copy."""
    if sys.platform != "darwin":
        return None
    import ctypes
    import ctypes.util
    try:
        lib = ctypes.CDLL(ctypes.util.find_library("c") or "libSystem.dylib", use_errno=True)
        function = lib.clonefile
    except (OSError, AttributeError):
        return None
    function.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint32]
    function.restype = ctypes.c_int

    def clone(source, target):
        if function(os.fsencode(source), os.fsencode(target), 0) != 0:
            raise OSError(ctypes.get_errno(), os.strerror(ctypes.get_errno()), source)
    return clone


def clone_tree(source, target) -> int:
    """Copy-on-write clone of every file under source into target. Returns the number of files."""
    clone = _clone_function()
    if clone is None:
        raise CloneUnsupported("copy-on-write clones need macOS (APFS)")
    source, target = str(source), str(target)
    count = 0
    for base, dirs, files in os.walk(source):
        rel = os.path.relpath(base, source)
        here = target if rel == "." else os.path.join(target, rel)
        os.makedirs(here, exist_ok=True)
        for name in dirs:
            if os.path.islink(os.path.join(base, name)):
                raise ScratchError(f"{os.path.join(base, name)} is a symlink inside the universe folder; not cloned")
        for name in files:
            path = os.path.join(base, name)
            if os.path.islink(path):
                raise ScratchError(f"{path} is a symlink inside the universe folder; not cloned")
            try:
                clone(path, os.path.join(here, name))
            except OSError as exc:
                if count == 0:
                    raise CloneUnsupported(f"this volume cannot clone files ({exc.strerror})")
                raise ScratchError(f"clone stopped at {path}: {exc.strerror}")
            count += 1
    return count


def _copy_evals(source_evals: Path, target_evals: Path) -> int:
    target_evals.mkdir(parents=True)
    ignore = shutil.ignore_patterns("__pycache__", "*.pyc", "*.pyo", ".DS_Store")
    for entry in sorted(source_evals.iterdir()):
        if entry.name in NOT_COPIED or entry.name == ".DS_Store":
            continue
        if entry.is_symlink():
            raise ScratchError(f"{entry} is a symlink; the evaluator copy must hold real files only")
        if entry.is_dir():
            shutil.copytree(entry, target_evals / entry.name, symlinks=True, ignore=ignore)
        else:
            shutil.copy2(entry, target_evals / entry.name)
    links = [p for p in target_evals.rglob("*") if p.is_symlink()]
    if links:
        raise ScratchError(f"the evaluator copy holds symlinks ({links[0].relative_to(target_evals)}): a write "
                           "through one could reach the real Evals/")
    (target_evals / STORE).mkdir()
    return sum(1 for p in target_evals.rglob("*") if p.is_file())


def _build(root: Path, task_dir: Path, universe: dict, mode: str, source_ws: Path) -> dict:
    ws = root / "ws"
    copied = _copy_evals(source_ws / EVALS, ws / EVALS)
    linked = {}
    claude = source_ws / "claude"
    if claude.is_dir():
        (ws / "claude").symlink_to(claude.resolve(), target_is_directory=True)
        linked["claude"] = str(claude.resolve())
    data_source = source_ws / universe["folder"]
    if not data_source.is_dir():
        raise ScratchError(f"universe folder {data_source} not found")
    used, cloned, note = mode, 0, None
    if mode in ("auto", "clone"):
        try:
            cloned = clone_tree(data_source, ws / universe["folder"])
            used = "clone"
        except CloneUnsupported as exc:
            shutil.rmtree(ws / universe["folder"], ignore_errors=True)
            if mode == "clone":
                raise
            used, note = "symlink", str(exc)
    if used == "symlink":
        (ws / universe["folder"]).symlink_to(data_source.resolve(), target_is_directory=True)
        linked[universe["folder"]] = str(data_source.resolve())
    (root / "tmp").mkdir()
    digest, files = content_digest(ws / EVALS)
    meta = {"schema": SCHEMA, "task_dir": str(task_dir), "identity": scratch_identity(task_dir),
            "universe": universe, "universe_data": used, "universe_data_note": note, "cloned_files": cloned,
            "linked": linked, "source_ws": str(source_ws), "evals_files": files, "evals_digest": digest,
            "copied_entries": copied}
    _atomic_write(root / "scratch.json", (json.dumps(meta, indent=1, sort_keys=True) + "\n").encode(),
                  "the evaluator scratch record")
    return meta


def _remove_tree(root: Path, scratch: Path) -> None:
    """Delete one scratch folder. Links inside are unlinked, never followed."""
    if root.is_symlink() or not root.name.startswith(PREFIX) or root.parent.resolve() != Path(scratch).resolve():
        raise ScratchError(f"refusing to delete {root}: not an evaluator scratch under {scratch}")
    shutil.rmtree(root)


def load_meta(root: Path):
    path = root / "scratch.json"
    if not path.is_file():
        return None
    try:
        meta = json.loads(path.read_text())
    except (OSError, ValueError):
        return None
    return meta if isinstance(meta, dict) and meta.get("schema") == SCHEMA else None


# ---------------------------------------------------------------- running evaluator tools inside the scratch

def run_env(root: Path) -> dict:
    env = {k: v for k, v in os.environ.items() if not k.startswith("TASK_AUTHORING_")}
    env.update(PYTHONDONTWRITEBYTECODE="1", TMPDIR=str(root / "tmp"))
    return env


def run_tool(root: Path, argv, python=None):
    """Run an evaluator tool from the scratch workspace: cwd ws/, TMPDIR inside the scratch, no bytecode."""
    return subprocess.run([python or sys.executable, "-B", *[str(a) for a in argv]], cwd=str(root / "ws"),
                          env=run_env(root), capture_output=True, text=True, timeout=RUN_TIMEOUT)


def command_prefix(root: Path, python=None) -> str:
    return (f"cd {shlex.quote(str(root / 'ws'))} && TMPDIR={shlex.quote(str(root / 'tmp'))} "
            f"PYTHONDONTWRITEBYTECODE=1 {shlex.quote(python or sys.executable)} -B Evals/tools/")


def _json_out(done):
    try:
        return json.loads(done.stdout)
    except ValueError:
        return None


def _linked_changes(meta, marker: Path) -> list:
    """selftest_sandbox's leak check (`find <real linked folders> -newer <marker>`) on this scratch's links."""
    if not meta["linked"]:
        return []
    import selftest_sandbox

    class _Links(selftest_sandbox.Sandbox):
        def __init__(self, linked, marker):         # only what check_linked() reads
            self.linked, self.marker, self.ignore_newer = linked, marker, ()

    return _Links(meta["linked"], marker).check_linked()


def _verify(root: Path, meta: dict, checks: list, python=None) -> None:
    """Prove the store is the scratch's own, by running the evaluator's input tool inside the scratch."""
    store = root / "ws" / EVALS / STORE
    date = meta["universe"]["date"]
    done = run_tool(root, [STORE_TOOL, "list"], python)
    shown = _json_out(done)
    if done.returncode != 0 or not isinstance(shown, dict) or "universe_intake" not in shown:
        _check(checks, "scratch.store_list", "FAIL", "hg_store_input.py list did not run in the scratch: "
               + (done.stderr.strip() or done.stdout.strip())[-300:])
        return
    state = shown["universe_intake"].get("state")
    _check(checks, "scratch.store_list", "PASS", f"hg_store_input.py list ran in the scratch; universe_intake was "
           f"{state}, {len(shown.get('inputs') or {})} saved inputs")
    done = run_tool(root, [STORE_TOOL, "universe", date], python)
    saved = store / DATE_FILE
    if done.returncode != 0 or not saved.is_file() or saved.read_text().strip() != date:
        _check(checks, "scratch.store_write", "FAIL", f"hg_store_input.py universe {date} did not write "
               f"{saved}: " + (done.stderr.strip() or done.stdout.strip())[-300:])
        return
    _check(checks, "scratch.store_write", "PASS", f"hg_store_input.py universe {date} wrote ws/{EVALS}/{STORE}/"
           f"{DATE_FILE} inside the scratch")
    again = _json_out(run_tool(root, [STORE_TOOL, "list"], python)) or {}
    intake = again.get("universe_intake") or {}
    if intake.get("state") == "SELECTED" and intake.get("date") == date:
        _check(checks, "scratch.store_read", "PASS", f"list now reports {intake.get('label', date)} as SELECTED")
    else:
        _check(checks, "scratch.store_read", "FAIL", f"after the save, list reports universe_intake "
               f"{intake.get('state')} {intake.get('date')}; expected SELECTED {date}")


def _probe_reads(root: Path, meta: dict, checks: list, python=None) -> None:
    """One real record read through the scratch, so the caller knows whether searches with hits work here."""
    if not (root / "ws" / SEARCH_TOOL).is_file():
        _check(checks, "scratch.universe_reads", "SKIP", "no hg_search.py in this Evals copy")
        return
    inventory = _json_out(run_tool(root, [SEARCH_TOOL, "inventory"], python)) or {}
    present = [s["service"] for s in inventory.get("services", []) if s.get("directory_present")]
    if not present:
        _check(checks, "scratch.universe_reads", "FAIL", "hg_search.py inventory finds no service folder in the "
               "scratch workspace")
        return
    service = "contacts" if "contacts" in present else present[0]
    files = _json_out(run_tool(root, [SEARCH_TOOL, "files", service], python)) or {}
    target = next((m["path"] for m in files.get("matches", [])
                   if m.get("path", "").endswith(".json") and not m["path"].startswith("root/")), None)
    if not target:
        _check(checks, "scratch.universe_reads", "SKIP", f"no JSON export listed for {service}; record reads not probed")
        return
    done = run_tool(root, [SEARCH_TOOL, "get", service, "--file", target, "--pointer", "", "--max-chars", "200"],
                    python)
    got = _json_out(done)
    if done.returncode == 0 and isinstance(got, dict) and got.get("file") and not got.get("error"):
        _check(checks, "scratch.universe_reads", "PASS", f"hg_search.py get {service} --file {target} returned "
               f"{got['file']} ({len(present)} services present, universe data: {meta['universe_data']})")
        return
    reason = ((got or {}).get("error") if isinstance(got, dict) else None) or done.stderr.strip() or done.stdout.strip()
    if meta["universe_data"] == "symlink":
        _check(checks, "scratch.universe_reads", "WARN", f"record reads fail in this scratch: hg_search.py get "
               f"{service} said \"{str(reason)[:240]}\". The Evals search tools require every data file to resolve "
               "under their own workspace, and a symlinked universe resolves into the real one. The store, "
               "reference views, inventory and file listings work. For searches that return records, rebuild with "
               "`create --force --universe-data clone` (macOS).")
    else:
        _check(checks, "scratch.universe_reads", "FAIL", f"hg_search.py get {service} --file {target} failed: "
               + str(reason)[-300:])


# ---------------------------------------------------------------- commands

def _result(command, checks, **extra) -> dict:
    statuses = {c["status"] for c in checks}
    verdict = "FAIL" if "FAIL" in statuses else "WARN" if "WARN" in statuses else "PASS"
    out = {"tool": TOOL, "version": VERSION, "verdict": verdict, "bound_to": {}, "checks": checks,
           "command": command}
    out.update(extra)
    return out


def create(task_dir, universe_data=None, date=None, force=False, source_ws=None, scratch=None, python=None) -> dict:
    """Build (or re-check) the task's evaluator scratch and prove its store is separate from the real Evals/."""
    from task_context import refuse_read_only
    task_dir = Path(task_dir).resolve()
    source_ws = Path(source_ws or WS).resolve()
    scratch = Path(scratch or SCRATCH)
    mode = universe_data or DEFAULT_UNIVERSE_DATA
    if mode not in DATA_MODES:
        raise ScratchError(f"unknown --universe-data {mode!r}; use one of: {', '.join(DATA_MODES)}")
    if not task_dir.is_dir():
        raise ScratchError(f"task folder not found: {task_dir}")
    root = scratch_root(task_dir, scratch)
    refuse_read_only(root, "the evaluator scratch")
    if _inside(root, source_ws / EVALS):
        raise ScratchError(f"{root} is inside Evals/; the scratch must sit outside it")
    universe = task_universe(task_dir, date, source_ws)
    checks = []
    before = listing(source_ws / EVALS)
    scratch.mkdir(parents=True, exist_ok=True)
    marker_fd, marker_name = tempfile.mkstemp(dir=str(scratch), prefix="eval_scratch_marker_")
    os.close(marker_fd)
    marker = Path(marker_name)
    try:
        meta = load_meta(root) if root.is_dir() else None
        if root.exists() and (force or meta is None):
            why = "--force" if force else "it has no readable scratch.json"
            _remove_tree(root, scratch)
            _check(checks, "scratch.rebuild", "PASS", f"the old scratch was removed ({why})")
            meta = None
        if meta is None:
            try:
                meta = _build(root, task_dir, universe, mode, source_ws)
            except BaseException:
                shutil.rmtree(root, ignore_errors=True)
                raise
            data = (f"{meta['cloned_files']} files cloned copy-on-write" if meta["universe_data"] == "clone"
                    else "symlinked")
            _check(checks, "scratch.build", "PASS", f"built {root.name}: {meta['evals_files']} Evals files copied, "
                   f"empty input store, {universe['folder']} {data}")
            if meta["universe_data_note"]:
                _check(checks, "scratch.universe_data", "WARN", f"the universe is symlinked, not cloned: "
                       f"{meta['universe_data_note']}")
        else:
            if meta["universe"]["key"] != universe["key"]:
                _check(checks, "scratch.build", "FAIL", f"the existing scratch is for {meta['universe']['label']}, "
                       f"but the task date is {universe['label']}. Run create --force to rebuild it.")
                return _result("create", checks, scratch=str(root))
            _check(checks, "scratch.build", "PASS", f"{root.name} exists (universe data: {meta['universe_data']}); "
                   "checked again, not rebuilt")
            stale = content_digest(source_ws / EVALS)[0] != meta["evals_digest"]
            if stale:
                _check(checks, "scratch.current", "WARN", "the real Evals/ changed since this scratch was copied; "
                       "run create --force to take the new files (the scratch store is emptied)")
        _verify(root, meta, checks, python)
        changes = listing_diff(before, listing(source_ws / EVALS))
        if changes:
            _check(checks, "scratch.real_evals", "FAIL", f"LEAK: {len(changes)} entries under the real Evals/ "
                   f"changed while the scratch was built and checked: {'; '.join(changes[:6])}. Stop and find the "
                   "writer before using this scratch.")
        else:
            _check(checks, "scratch.real_evals", "PASS", f"nothing under the real Evals/ changed ({len(before)} "
                   "entries, sizes and mtimes equal before and after)")
        newer = _linked_changes(meta, marker)
        if newer:
            _check(checks, "scratch.linked", "FAIL", f"LEAK: {len(newer)} entries in the linked folders changed "
                   f"during the run: {'; '.join(newer[:5])}")
        elif meta["linked"]:
            _check(checks, "scratch.linked", "PASS", "linked folders unchanged (find -newer marker: empty): "
                   + ", ".join(sorted(meta["linked"])))
        if not any(c["status"] == "FAIL" for c in checks):
            _probe_reads(root, meta, checks, python)
    finally:
        if marker.exists():
            marker.unlink()
    return _result("create", checks, scratch=str(root), workspace=str(root / "ws"),
                   command_prefix=command_prefix(root, python), universe=meta["universe"],
                   universe_data=meta["universe_data"])


def status(task_dir, source_ws=None, scratch=None) -> dict:
    """What the task's scratch holds. Reads only."""
    task_dir = Path(task_dir).resolve()
    source_ws = Path(source_ws or WS).resolve()
    root = scratch_root(task_dir, scratch)
    checks = []
    meta = load_meta(root) if root.is_dir() else None
    if meta is None:
        _check(checks, "scratch.exists", "SKIP", f"no evaluator scratch for {task_dir.name} "
               f"({root.name} is absent); run create")
        return _result("status", checks, scratch=str(root), exists=False)
    _check(checks, "scratch.exists", "PASS", f"{root.name}: {meta['universe']['label']}, universe data "
           f"{meta['universe_data']}, {meta['evals_files']} Evals files")
    store = root / "ws" / EVALS / STORE
    saved = {}
    index = store / "inputs.json"
    if index.is_file():
        try:
            saved = {k: v.get("state") for k, v in json.loads(index.read_text()).get("inputs", {}).items()}
        except (OSError, ValueError):
            _check(checks, "scratch.store", "WARN", "the scratch store index cannot be read")
    date_file = store / DATE_FILE
    date = date_file.read_text().strip() if date_file.is_file() else None
    kept = sorted(k for k, v in saved.items() if v == "saved")
    _check(checks, "scratch.store", "PASS" if date == meta["universe"]["date"] else "WARN",
           f"saved date {date or 'none'}; saved inputs: {', '.join(kept) or 'none'}"
           + ("" if date == meta["universe"]["date"] else f"; expected {meta['universe']['date']}: run create"))
    if (source_ws / EVALS).is_dir() and content_digest(source_ws / EVALS)[0] != meta["evals_digest"]:
        _check(checks, "scratch.current", "WARN", "the real Evals/ changed since this scratch was copied; run "
               "create --force to take the new files")
    else:
        _check(checks, "scratch.current", "PASS", "the copied Evals files equal the real ones")
    broken = [name for name in meta["linked"] if not (root / "ws" / name).exists()]
    if broken or not (root / "ws" / meta["universe"]["folder"]).is_dir():
        _check(checks, "scratch.data", "FAIL", "missing in the scratch workspace: "
               + ", ".join(broken or [meta["universe"]["folder"]]) + ". Run create --force.")
    return _result("status", checks, scratch=str(root), exists=True, workspace=str(root / "ws"),
                   command_prefix=command_prefix(root), universe=meta["universe"],
                   universe_data=meta["universe_data"], saved_inputs=kept)


def evaluate(task_dir, source_ws=None, scratch=None) -> dict:
    """The contract's read-only entry point: the same object as `status`."""
    return status(task_dir, source_ws=source_ws, scratch=scratch)


def remove(task_dir, scratch=None) -> dict:
    task_dir = Path(task_dir).resolve()
    scratch = Path(scratch or SCRATCH)
    root = scratch_root(task_dir, scratch)
    checks = []
    if not root.exists():
        _check(checks, "scratch.remove", "SKIP", f"{root.name} does not exist; nothing to remove")
    else:
        _remove_tree(root, scratch)
        _check(checks, "scratch.remove", "PASS", f"removed {root}")
    return _result("remove", checks, scratch=str(root))


def list_scratches(scratch=None) -> dict:
    scratch = Path(scratch or SCRATCH)
    checks, rows = [], []
    for root in sorted(p for p in scratch.glob(PREFIX + "*") if p.is_dir()) if scratch.is_dir() else []:
        meta = load_meta(root)
        if meta is None:
            _check(checks, "scratch.list." + root.name, "WARN", "no readable scratch.json; remove the folder by hand")
            continue
        alive = Path(meta["task_dir"]).is_dir()
        rows.append({"scratch": root.name, "task_dir": meta["task_dir"], "universe": meta["universe"]["label"],
                     "universe_data": meta["universe_data"], "task_exists": alive})
        _check(checks, "scratch.list." + root.name, "PASS" if alive else "WARN",
               f"{meta['task_dir']} · {meta['universe']['label']} · {meta['universe_data']}"
               + ("" if alive else " · the task folder is gone: remove this scratch"))
    if not rows and not checks:
        _check(checks, "scratch.list", "SKIP", f"no evaluator scratch under {scratch}")
    return _result("list", checks, scratches=rows)


def render(result) -> str:
    lines = [f"EVAL SCRATCH ({result['command']}): {result['verdict']}"]
    lines += [f"[{c['status']}] {c['id']}: {c['detail']}" for c in result["checks"]]
    if result.get("command_prefix") and result["verdict"] != "FAIL":
        lines.append(f"scratch: {result['scratch']}")
        lines.append(f"run evaluator tools with: {result['command_prefix']}<tool>.py <arguments>")
        lines.append(f"  for example: {result['command_prefix']}hg_store_input.py list")
    return "\n".join(lines)


# ---------------------------------------------------------------- self-test (a fake workspace, a fake evaluator)

FAKE_UNIVERSE = '''from pathlib import Path
UNIVERSES = {"normal": {"date": "2026-02-14", "label": "Feb 14, 2026 (normal)", "folder": "Universe_Normal"},
             "synthcut": {"date": "2025-10-01", "label": "Oct 1, 2025 (synth-cut)", "folder": "Universe_SynthCut"}}
def parse(answer):
    text = " ".join(str(answer).replace(",", " ").split()).casefold()
    for key, forms in (("normal", ("2026-02-14", "february 14 2026")), ("synthcut", ("2025-10-01", "october 1 2025"))):
        if text in forms:
            return key
    raise ValueError("Unrecognized date %r" % answer)
'''
FAKE_STORE = '''import json, sys, tempfile
from pathlib import Path
import hg_universe
ROOT = Path(__file__).resolve().parents[2]
STORE = ROOT / "Evals" / "task_inputs"
index = STORE / "inputs.json"
doc = json.loads(index.read_text()) if index.is_file() else {"inputs": {}}
if sys.argv[1] == "universe":
    key = hg_universe.parse(" ".join(sys.argv[2:]))
    with tempfile.NamedTemporaryFile(delete=False) as staged:      # like the real tool: tempfile without a folder
        staged.write(b"x")
    Path(staged.name).unlink()
    STORE.mkdir(parents=True, exist_ok=True)
    (STORE / "02_Universe_Date.txt").write_text(hg_universe.UNIVERSES[key]["date"] + "\\n")
    doc["inputs"]["universe"] = {"state": "saved", "tmp": staged.name}
    index.write_text(json.dumps(doc))
    LEAK
date = (STORE / "02_Universe_Date.txt").read_text().strip() if (STORE / "02_Universe_Date.txt").is_file() else None
label = next((u["label"] for u in hg_universe.UNIVERSES.values() if u["date"] == date), None)
print(json.dumps({"inputs": doc["inputs"], "universe_intake": {"state": "SELECTED" if date else "ASK", "date": date,
                                                               "label": label}}))
'''
FAKE_SEARCH = '''import json, sys
from pathlib import Path
import hg_universe
ROOT = Path(__file__).resolve().parents[2]
date = (ROOT / "Evals" / "task_inputs" / "02_Universe_Date.txt").read_text().strip()
folder = ROOT / next(u["folder"] for u in hg_universe.UNIVERSES.values() if u["date"] == date) / "contacts"
if sys.argv[1] == "inventory":
    print(json.dumps({"services": [{"service": "contacts", "directory_present": folder.is_dir()}]}))
elif sys.argv[1] == "files":
    print(json.dumps({"matches": [{"path": p.name} for p in sorted(folder.glob("*.json"))]}))
else:
    path = (folder / sys.argv[sys.argv.index("--file") + 1]).resolve()      # like safe_file(): resolved first
    try:
        print(json.dumps({"file": path.relative_to(ROOT).as_posix(), "value": path.read_text()[:50]}))
    except ValueError as error:
        print(json.dumps({"error": str(error)}))
        sys.exit(1)
'''


def make_fixture(root, leak=False) -> dict:
    """A fake workspace: Evals/ with a small evaluator that behaves like the real one where it matters (root from
    the tool file, tempfile without a folder, resolved data paths), claude/, two universe folders, one task."""
    root = Path(root)
    ws = root / "real_ws"
    tools = ws / EVALS / "tools"
    tools.mkdir(parents=True)
    (ws / EVALS / "WORKFLOW.md").write_text("workflow\n")
    (ws / EVALS / "references" / "universes" / "normal").mkdir(parents=True)
    (ws / EVALS / "references" / "universes" / "normal" / "universe_manifest.json").write_text("{}\n")
    (ws / EVALS / STORE).mkdir()
    (ws / EVALS / STORE / "inputs.json").write_text('{"inputs": {"prompt": {"state": "saved"}}}')
    (ws / EVALS / STORE / DATE_FILE).write_text("2025-10-01\n")
    (ws / EVALS / ".cache").mkdir()
    (ws / EVALS / ".cache" / "old.json").write_text("{}")
    (tools / "hg_universe.py").write_text(FAKE_UNIVERSE)
    leak_line = ('(Path(%r) / "leaked.txt").write_text("x")' % str(ws / EVALS)) if leak else "pass"
    (tools / "hg_store_input.py").write_text(FAKE_STORE.replace("LEAK", leak_line))
    (tools / "hg_search.py").write_text(FAKE_SEARCH)
    (ws / "claude").mkdir()
    (ws / "claude" / "CLAUDE.md").write_text("skills\n")
    for name in ("Universe_Normal", "Universe_SynthCut"):
        (ws / name / "contacts").mkdir(parents=True)
        (ws / name / "contacts" / "contacts.json").write_text('[{"name": "%s"}]\n' % name)
    task = root / "bundle" / "task_inputsA"
    task.mkdir(parents=True)
    scratch = root / "scratch"
    return {"ws": ws, "task": task, "scratch": scratch,
            "kw": {"source_ws": ws, "scratch": scratch, "date": "February 14, 2026 00:00"}}


def _self_test() -> int:
    import selftest_sandbox
    can_clone = _clone_function() is not None
    with selftest_sandbox.scratch_tmp("eval_scratch_selftest_") as tmp:
        covered = 0
        fx = make_fixture(Path(tmp) / "a")
        ws, task, kw = fx["ws"], fx["task"], fx["kw"]
        real_store = listing(ws / EVALS / STORE)
        # 1. symlink mode: the store is separate, the real Evals/ is untouched, record reads are reported as failing
        made = create(task, universe_data="symlink", **kw)
        root = Path(made["scratch"])
        assert made["verdict"] == "WARN" and _inside(root, fx["scratch"]) and root.name.startswith(PREFIX), made
        assert (root / "ws" / EVALS / STORE / DATE_FILE).read_text() == "2026-02-14\n"
        assert (ws / EVALS / STORE / DATE_FILE).read_text() == "2025-10-01\n", "the real store was written"
        assert listing(ws / EVALS / STORE) == real_store and not (root / "ws" / EVALS / ".cache").exists()
        assert not (root / "ws" / "Universe_SynthCut").exists(), "only the task's universe is present"
        assert not (root / "ws" / EVALS / "references").is_symlink()
        staged = json.loads((root / "ws" / EVALS / STORE / "inputs.json").read_text())["inputs"]["universe"]["tmp"]
        assert _inside(staged, root / "tmp"), "tempfile without a folder must stay inside the scratch"
        by_id = {c["id"]: c for c in made["checks"]}
        assert by_id["scratch.real_evals"]["status"] == "PASS" and by_id["scratch.store_write"]["status"] == "PASS"
        assert by_id["scratch.universe_reads"]["status"] == "WARN", by_id["scratch.universe_reads"]
        assert "hg_store_input.py list" in render(made) and str(root / "ws") in made["command_prefix"]
        covered += 1
        # 2. status reads only; a second create re-checks without rebuilding; a changed Evals is reported
        before = listing(root)
        shown = status(task, source_ws=ws, scratch=fx["scratch"])
        assert shown["exists"] and shown["saved_inputs"] == ["universe"] and listing(root) == before, shown
        again = create(task, universe_data="symlink", **kw)
        assert any("not rebuilt" in c["detail"] for c in again["checks"]), again["checks"]
        (ws / EVALS / "WORKFLOW.md").write_text("workflow v2\n")
        assert any(c["id"] == "scratch.current" and c["status"] == "WARN"
                   for c in status(task, source_ws=ws, scratch=fx["scratch"])["checks"])
        assert [r["scratch"] for r in list_scratches(fx["scratch"])["scratches"]] == [root.name]
        covered += 1
        # 3. clone mode (macOS): record reads work and the clone is not a link
        if can_clone:
            cloned = create(task, universe_data="clone", force=True, **kw)
            by_id = {c["id"]: c for c in cloned["checks"]}
            assert cloned["verdict"] == "PASS" and cloned["universe_data"] == "clone", cloned
            assert by_id["scratch.universe_reads"]["status"] == "PASS"
            data = root / "ws" / "Universe_Normal"
            assert data.is_dir() and not data.is_symlink() and (data / "contacts" / "contacts.json").is_file()
            (data / "contacts" / "contacts.json").write_text("changed in the scratch\n")
            assert "Universe_Normal" in (ws / "Universe_Normal" / "contacts" / "contacts.json").read_text(), \
                "a write to the clone reached the original"
            assert (root / "ws" / EVALS / "WORKFLOW.md").read_text() == "workflow v2\n", "--force takes new files"
        else:
            try:
                create(task, universe_data="clone", force=True, **kw)
            except CloneUnsupported:
                pass
            else:
                raise AssertionError("clone mode must fail where clones are not supported")
            auto = create(task, universe_data="auto", force=True, **kw)
            assert auto["universe_data"] == "symlink" and any(c["id"] == "scratch.universe_data"
                                                              for c in auto["checks"])
        covered += 1
        # 4. remove deletes the scratch and nothing else; a folder that is not a scratch is refused
        gone = remove(task, scratch=fx["scratch"])
        assert gone["verdict"] == "PASS" and not root.exists() and (ws / "claude" / "CLAUDE.md").is_file()
        assert (ws / "Universe_Normal" / "contacts" / "contacts.json").is_file()
        assert status(task, source_ws=ws, scratch=fx["scratch"])["exists"] is False
        try:
            _remove_tree(ws / EVALS, fx["scratch"])
        except ScratchError:
            pass
        else:
            raise AssertionError("a folder outside the scratch root was accepted for deletion")
        covered += 1
        # 5. planted bad: an evaluator that writes into the real Evals/ is caught by the listing check
        bad = make_fixture(Path(tmp) / "b", leak=True)
        leaked = create(bad["task"], universe_data="symlink", **bad["kw"])
        detail = next(c["detail"] for c in leaked["checks"] if c["id"] == "scratch.real_evals")
        assert leaked["verdict"] == "FAIL" and "LEAK" in detail and "leaked.txt" in detail, leaked
        assert "run evaluator tools with" not in render(leaked)
        covered += 1
        # 6. the task date is never guessed; two task folders never share a scratch
        try:
            create(task, source_ws=ws, scratch=fx["scratch"])
        except ScratchError as exc:
            assert "task date" in str(exc), exc
        else:
            raise AssertionError("a task without an assignment got a scratch")
        try:
            create(task, source_ws=ws, scratch=fx["scratch"], date="March 3, 2026")
        except ScratchError:
            pass
        else:
            raise AssertionError("an unknown date was accepted")
        other = task.parent / "task_inputsB"
        other.mkdir()
        assert scratch_root(task, fx["scratch"]) != scratch_root(other, fx["scratch"])
        assert not fx["scratch"].exists() or not list(fx["scratch"].glob(PREFIX + "*")), "a failed create left a scratch"
        covered += 1
    print(f"self-test: ok ({covered} cases: symlink mode with a separate store, real Evals/ untouched and failing "
          "record reads reported, status and re-check, "
          + ("clone mode with working record reads" if can_clone else "clone refused and auto falls back to symlink")
          + ", remove, a planted write into the real Evals/ caught, the task date never guessed)")
    return 0


# ---------------------------------------------------------------- command line

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        return _self_test()
    ap = argparse.ArgumentParser(prog="eval_scratch.py", description="per-task evaluator copy (see the docstring)")
    sub = ap.add_subparsers(dest="command")
    for name, text in (("create", "build or re-check the task's evaluator scratch"),
                       ("status", "what the scratch holds"), ("remove", "delete the scratch"),
                       ("list", "every evaluator scratch")):
        p = sub.add_parser(name, help=text)
        if name != "list":
            p.add_argument("--task-dir", required=True)
        if name == "create":
            p.add_argument("--universe-data", choices=DATA_MODES, default=DEFAULT_UNIVERSE_DATA)
            p.add_argument("--date", help="task date, when the assignment cannot be read (never a default)")
            p.add_argument("--force", action="store_true", help="delete an existing scratch and build it again")
        p.add_argument("--source-ws", help=argparse.SUPPRESS)       # tests: another workspace root
        p.add_argument("--scratch-root", help=argparse.SUPPRESS)    # tests: another scratch folder
        p.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if not args.command:
        ap.error("a command is required: create, status, remove or list")
    if args.command != "list" and not Path(args.task_dir).is_dir():
        ap.error(f"task folder not found: {args.task_dir}")
    from task_context import ContextError
    try:
        if args.command == "create":
            result = create(args.task_dir, universe_data=args.universe_data, date=args.date, force=args.force,
                            source_ws=args.source_ws, scratch=args.scratch_root)
        elif args.command == "status":
            result = status(args.task_dir, source_ws=args.source_ws, scratch=args.scratch_root)
        elif args.command == "remove":
            result = remove(args.task_dir, scratch=args.scratch_root)
        else:
            result = list_scratches(args.scratch_root)
    except (ScratchError, ContextError, OSError, subprocess.TimeoutExpired) as exc:
        print(f"EVAL SCRATCH ({args.command}): FAIL\n[FAIL] scratch.{args.command}: {exc}")
        return 1
    print(json.dumps(result, indent=1, sort_keys=True, ensure_ascii=False) if args.json else render(result))
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())

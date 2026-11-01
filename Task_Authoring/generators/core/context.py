"""V3 task context, recomputed on every render (never read back from 00_Task_Context.json), and the pinned tools/
modules the library runs in-process.

The library runs Task_Authoring/tools/task_context.py, runtime_context.py, sql_lint.py and base_check.py (and what they
import from tools/) read-only, so the universe, seed bound (freeze_utc), eval clock (universe.clock_utc), source paths
and early row rules are exactly what the stage gates use. Python imports a module once per process, so a tools/ file
edited later would keep running in its old form while the file on disk describes the new one. To keep the two equal:
  * on first use, every module of that import closure is read once, hashed, and executed from exactly those bytes
    (load_tools): no __pycache__ bytecode is read or written for them;
  * tools_module() and the render pipeline check the closure on disk and raise ToolsChanged when it is no longer the
    code this process runs — a file whose bytes differ, or one modified at all since it was read (its stamp moved,
    even if the old bytes were put back) — when a DEPENDENCY_FILES entry was modified since the closure loaded, and
    when a pinned module was replaced in sys.modules or a tools/ module was loaded outside the closure: run the command
    again in a new process. The sql_lint subprocess loads tools/ from disk itself, so an unmoved stamp is what shows
    it ran the pinned bytes too;
  * a module named like one of the closure's, imported into this process from anywhere before the library loaded its
    own copies, is refused, because the bytes it runs cannot be known.
"""
from __future__ import annotations

import ast
import hashlib
import importlib
import importlib.abc
import importlib.util
import sys
import types
from contextlib import contextmanager
from pathlib import Path

from .output import file_stamp
from .values import SpecError

LIB = Path(__file__).resolve().parents[1]         # Task_Authoring/generators/
TA = LIB.parent                                   # Task_Authoring/
WS = TA.parent
TOOLS = TA / "tools"
TOOL_ROOTS = ("task_context.py", "runtime_context.py", "sql_lint.py", "base_check.py")
# The files besides code that validation and the tools/ closure read (sql_lint reads the eval's event list and
# injection.json when it is imported; the validators read the rest during a run). They are stamped once per process,
# before the closure is imported, and a modification at any later point refuses the process (tools_changed), even one
# that put the old bytes back.
DEPENDENCY_FILES = (
    TA / "references" / "universe_schema_live.json", TA / "references" / "universe_constraints_live.json",
    TA / "references" / "injection.json", WS / "Evals" / "references" / "schema" / "injection.json",
    WS / "Evals" / "tools" / "hg_injection_lint.py", WS / "Evals" / "tools" / "hg_universe.py",
    LIB / "conventions" / "conventions.json",
)
# A bytecode cache below /dev/null (a file) can never exist: with sys.pycache_prefix (or PYTHONPYCACHEPREFIX) set to it
# and bytecode writing off, imports compile from source and write nothing.
NO_BYTECODE = "/dev/null/generators-no-bytecode"

_IMPORTS: dict[str, tuple[str, ...]] = {}         # sha256 of a file's bytes -> the top-level names it imports
_LOADED: dict[str, str] | None = None             # tools file name -> sha256 of the bytes this process runs
_STAMPS: dict[str, tuple | None] = {}             # tools file name -> its file_stamp taken before those bytes were read
_DEPENDENCY_STAMPS: dict[str, tuple | None] = {}  # DEPENDENCY_FILES path -> its file_stamp before the closure loaded
_ABSENT_PARENTS: dict[str, tuple | None] = {}     # nearest existing folder of an absent dependency -> its stamp then
_MODULES: dict[str, object] = {}                  # module name -> the module object load_tools() created
_OWN: dict[str, dict] = {}                        # module name -> the functions and classes its pinned bytes defined
_FINDER: list = []                                # the _Pinned finder that loaded them (one element once loaded)


class ToolsChanged(Exception):
    """The tools/ code this process runs, or a file it read when it loaded, is not, or no longer, what is on disk."""


def _imports(data: bytes, sha: str, name: str) -> tuple[str, ...]:
    if sha not in _IMPORTS:
        try:
            tree = ast.parse(data, filename=name)
        except SyntaxError as exc:
            raise ToolsChanged(f"tools/{name} does not parse ({exc}); is it being edited?") from None
        names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names.update(a.name.split(".")[0] for a in node.names)
            elif isinstance(node, ast.ImportFrom) and not node.level and node.module:
                names.add(node.module.split(".")[0])
        _IMPORTS[sha] = tuple(sorted(names))
    return _IMPORTS[sha]


def _read_closure(tools_dir: Path = TOOLS, stamps: dict | None = None) -> dict[str, tuple[Path, bytes | None]]:
    """TOOL_ROOTS and every tools/ module they import (found by ast, so independent of what this process imported),
    each file read once: file name -> (path, bytes); bytes None for a missing file. With `stamps`, each file's
    file_stamp is recorded just before it is read, so any later modification moves it."""
    seen, todo = {}, list(TOOL_ROOTS)
    while todo:
        name = todo.pop()
        if name in seen:
            continue
        path = tools_dir / name
        if stamps is not None:
            stamps[name] = file_stamp(path)
        try:
            data = path.read_bytes()
        except FileNotFoundError:
            seen[name] = (path, None)
            continue
        seen[name] = (path, data)
        todo += [f"{m}.py" for m in _imports(data, hashlib.sha256(data).hexdigest(), name)
                 if (tools_dir / f"{m}.py").is_file()]
    return seen


def tool_closure(tools_dir: Path = TOOLS, stamps: dict | None = None) -> dict:
    """sha256 of every module of the closure, from the bytes on disk now; None for a missing one."""
    return {name: (hashlib.sha256(data).hexdigest() if data is not None else None)
            for name, (_, data) in sorted(_read_closure(tools_dir, stamps).items())}


class _Pinned(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    """Serves the closure's modules from the bytes that were hashed, while load_tools() imports them."""

    def __init__(self, sources: dict[str, tuple[Path, bytes]]):
        self.sources = sources                    # module name -> (path, bytes)

    def find_spec(self, fullname, path=None, target=None):
        if fullname not in self.sources:
            return None
        return importlib.util.spec_from_loader(fullname, self, origin=str(self.sources[fullname][0]))

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        path, data = self.sources[module.__name__]
        module.__file__ = str(path)
        # dont_inherit: compiled with the module's own __future__ flags, not this file's
        exec(compile(data, str(path), "exec", dont_inherit=True), module.__dict__)  # noqa: S102 - pinned tools/ module


def _absent_parents(dependency_stamps: dict) -> set[Path]:
    """The nearest existing folder of each dependency file that does not exist: a file created there and removed
    again leaves the file's own stamp absent both times, but moves the folder's (an entry added and removed changes its
    mtime and ctime; a file edited in place does not)."""
    out = set()
    for path, stamp in dependency_stamps.items():
        if stamp is None:
            folder = Path(path).parent
            while not folder.exists() and folder != folder.parent:
                folder = folder.parent
            out.add(folder)
    return out


def _own(module) -> dict:
    """The functions and classes a module defined itself, by attribute name (its data globals are left out: the tools
    set those per task)."""
    return {attr: value for attr, value in vars(module).items()
            if isinstance(value, (types.FunctionType, type)) and getattr(value, "__module__", None) == module.__name__}


def _in_tools(module) -> bool:
    f = getattr(module, "__file__", None)
    if not isinstance(f, str):
        return False
    try:
        return Path(f).resolve().parent == TOOLS.resolve()
    except (OSError, ValueError):
        return False


def _tools_in_process() -> set[str]:
    return {name for name, mod in list(sys.modules.items()) if mod is not None and _in_tools(mod)}


def load_tools() -> dict[str, str]:
    """Load the tools/ closure once per process from bytes read once and hashed; returns {file name: sha256}."""
    global _LOADED
    if _LOADED is not None:
        return _LOADED
    dependency_stamps = {str(path): file_stamp(path) for path in DEPENDENCY_FILES}
    absent_parents = {str(folder): file_stamp(folder) for folder in _absent_parents(dependency_stamps)}
    stamps: dict = {}
    closure = _read_closure(stamps=stamps)
    missing = sorted(n for n, (_, data) in closure.items() if data is None)
    if missing:
        raise ToolsChanged(f"tools/ modules missing: {missing}")
    sources = {n[:-3]: (path, data) for n, (path, data) in closure.items()}
    taken = {name: getattr(sys.modules[name], "__file__", None) for name in sorted(sources) if name in sys.modules}
    if taken:
        raise ToolsChanged(f"modules named {sorted(taken)} are already imported into this process ({taken}); the "
                           "generators library runs its own pinned copies of tools/ under these names; run the "
                           "command in a new process")
    early = sorted(_tools_in_process())
    if early:
        raise ToolsChanged(f"tools/ modules {early} were imported into this process before the generators library "
                           "loaded its pinned copies, so the code they run cannot be checked; run the command in a "
                           "new process")
    finder = _Pinned(sources)
    sys.dont_write_bytecode = True
    sys.meta_path.insert(0, finder)
    try:
        modules = {name: importlib.import_module(name) for name in sorted(sources)}
    except BaseException:
        for name in sources:
            sys.modules.pop(name, None)
        raise
    finally:
        sys.meta_path.remove(finder)
    wrong = sorted(name for name, module in modules.items()
                   if getattr(getattr(module, "__spec__", None), "loader", None) is not finder
                   or sys.modules.get(name) is not module)
    if wrong:
        raise ToolsChanged(f"tools/ modules {wrong} were not loaded from their pinned bytes")
    stray = sorted(_tools_in_process() - set(sources))
    if stray:
        raise ToolsChanged(f"loading the tools/ closure also imported {stray}, which it does not pin")
    _MODULES.update(modules)
    _OWN.update({name: _own(module) for name, module in modules.items()})
    _FINDER[:] = [finder]
    _STAMPS.update(stamps)
    _DEPENDENCY_STAMPS.update(dependency_stamps)
    _ABSENT_PARENTS.update(absent_parents)
    _LOADED = {n: hashlib.sha256(data).hexdigest() for n, (_, data) in sorted(closure.items())}
    return _LOADED


def tools_changed() -> list[str]:
    """How the tools/ code this process runs, or what it read, differs from the disk (empty: it does not): a closure
    file whose bytes changed, or that was modified at all since it was read (even with its old bytes put back); a
    DEPENDENCY_FILES entry modified since the closure loaded, or, for one absent then, an entry added to or removed
    from its nearest existing folder (a create-and-delete); a pinned module replaced in sys.modules, reloaded through
    another loader (its spec no longer names the pinned finder), or whose own functions or classes are no longer those
    its pinned bytes defined (executed again by any route, a loader called directly included, or replaced); a tools/
    module loaded outside the pinned closure."""
    if _LOADED is None:
        return []
    out = [f"{name}: replaced in sys.modules" for name, module in sorted(_MODULES.items())
           if sys.modules.get(name) is not module]
    out += [f"{name}: executed again by another loader" for name, module in sorted(_MODULES.items())
            if getattr(getattr(module, "__spec__", None), "loader", None) is not _FINDER[0]]
    out += [f"{name}: its functions or classes are no longer those its pinned bytes defined (executed again, or "
            "replaced)" for name, module in sorted(_MODULES.items()) if _own(module) != _OWN.get(name)]
    out += [f"{path}: modified since this process loaded tools/" for path, stamp in sorted(_DEPENDENCY_STAMPS.items())
            if file_stamp(Path(path)) != stamp]
    out += [f"{folder}: an entry was added or removed since this process loaded tools/ (a dependency file absent then "
            "may have been created there)" for folder, stamp in sorted(_ABSENT_PARENTS.items())
            if file_stamp(Path(folder)) != stamp]
    out += [f"{name}: a tools/ module loaded outside the pinned closure"
            for name in sorted(_tools_in_process() - set(_MODULES))]
    stamps: dict = {}
    now = tool_closure(stamps=stamps)
    for name in sorted(set(now) | set(_LOADED) | set(stamps) | set(_STAMPS)):
        if now.get(name) != _LOADED.get(name):
            out.append(f"{name}: changed on disk")
        elif stamps.get(name) != _STAMPS.get(name):
            out.append(f"{name}: modified since it was loaded")
    return out


def ensure_tools_current() -> None:
    """Raise ToolsChanged unless the tools/ code this process runs is still the code on disk (tools_changed)."""
    changed = tools_changed()
    if changed:
        raise ToolsChanged(f"tools/ changed since this process loaded it ({', '.join(changed)}); run the command "
                           "again in a new process")


def tools_module(name: str):
    """A pinned tools/ module; refuses when the closure on disk no longer matches what this process runs."""
    loaded = load_tools()
    if f"{name}.py" not in loaded:
        raise ToolsChanged(f"tools/{name}.py is not in the pinned closure {sorted(loaded)}")
    ensure_tools_current()
    return _MODULES[name]


@contextmanager
def _source_only():
    """Imports made inside compile from source: no bytecode is read from, or written to, a __pycache__ folder."""
    saved_prefix, saved_flag = sys.pycache_prefix, sys.dont_write_bytecode
    sys.pycache_prefix, sys.dont_write_bytecode = NO_BYTECODE, True
    try:
        yield
    finally:
        sys.pycache_prefix, sys.dont_write_bytecode = saved_prefix, saved_flag


def recompute(task_dir: Path) -> dict:
    tc = tools_module("task_context")
    try:
        with _source_only():                     # load_context imports Evals/tools/hg_universe.py on every call
            return tc.load_context(Path(task_dir), require_source=True)
    except Exception as exc:  # the tool raises its own ContextError types
        raise SpecError("context", f"task context failed for {task_dir}: {exc}") from exc


def check_spec_task(task: dict, ctx: dict) -> None:
    uni = ctx["universe"]
    want = {"universe": uni["key"], "freeze_utc": ctx["freeze_utc"], "clock_utc": uni["clock_utc"],
            "context_hash": ctx["context_hash"]}
    for key, expected in want.items():
        if task.get(key) != expected:
            raise SpecError(f"task.{key}", f"spec says {task.get(key)!r}, the recomputed context says {expected!r}")


def service_paths(ctx: dict) -> dict[str, Path]:
    return {name: Path(p) for name, p in (ctx.get("source", {}).get("paths") or {}).items()}

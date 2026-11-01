"""Shared task-authoring generators (plan: Task_Authoring/plans/Generators_Reuse_Plan.md).

Every module below this package is executed from a single read of its .py file, hashed and stamped as it is loaded;
no __pycache__ bytecode is read or written for it, and a name with no .py file here is not found (nothing below the
package is loaded from bytecode or by another loader). `changed_since_load()` lists library code this process may be
running that the disk no longer holds, and the render pipeline refuses to start or to conclude while that list is not
empty, so a build record's library hash describes the code that ran:
  * a file whose bytes changed since it loaded, or that was modified at all since (its stamp moved, even if the old
    bytes were put back), or that this process ran from two different contents;
  * a module below the package that another loader loaded, or that the finder executed more than once (reload, or a
    re-import after removal from sys.modules);
  * a module whose own functions or classes were replaced by new ones of the same module, and a function or class one
    library module took from another (`from .x import f`) that is no longer that module's own: the traces any re-run
    of a module leaves — a reload by any route, a re-import, a loader called directly — in the module itself and in
    the modules that imported names from it;
  * a bytecode cache anywhere under the package.
Python itself compiles this file and a library script run directly (render.py) before the finder exists; each is
hashed and stamped from a read made as it starts. That bootstrap is the root of trust: render.py and
tests/run_tests.py import the package with bytecode reading disabled, and a process that imports it otherwise must do
the same (sys.pycache_prefix or PYTHONPYCACHEPREFIX); a cache planted for this file would run before any check.
"""
from __future__ import annotations

import hashlib
import importlib.abc
import importlib.machinery
import importlib.util
import os
import sys
import types
from pathlib import Path

LIBRARY_VERSION = "0.1.0"
ROOT = Path(__file__).resolve().parent

_LOADED: dict[str, str] = {}            # library-relative file -> sha256 of the bytes this process first ran from it
_STAMPS: dict[str, tuple | None] = {}   # library-relative file -> its stamp taken just before those bytes were read
_EXECUTED: set[str] = set()             # module names the finder has executed
_RELOADED: set[str] = set()             # module names it executed more than once (reload, or re-import after removal)
_CONFLICTS: set[str] = set()            # files run from two different byte contents in this process
_OWN: dict[str, dict] = {}              # module name -> the functions and classes its first execution defined


class LibraryChanged(Exception):
    """The library code this process runs is not, or no longer, the code on disk."""


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _stamp(path) -> tuple | None:
    """(device, inode, size, mtime_ns, ctime_ns), None for a missing file: core/output.file_stamp, which this
    bootstrap cannot import before its finder exists."""
    try:
        st = os.stat(path)
    except FileNotFoundError:
        return None
    except OSError as exc:
        return ("unreadable", exc.errno)
    return (st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns)


def _rel(path) -> str:
    return Path(path).resolve().relative_to(ROOT).as_posix()


def _record(rel: str, sha: str, stamp: tuple | None) -> None:
    if _LOADED.setdefault(rel, sha) != sha:
        _CONFLICTS.add(rel)
    _STAMPS.setdefault(rel, stamp)


class _Finder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    """Finds and loads every module below this package from the bytes it read once (see the module docstring)."""

    def __init__(self):
        self._read: dict[str, tuple[bytes, tuple | None]] = {}

    def find_spec(self, fullname, path=None, target=None):
        if not fullname.startswith(__name__ + "."):
            return None
        parts = fullname.split(".")[1:]
        if not all(p.isidentifier() for p in parts):
            raise ModuleNotFoundError(f"No module named {fullname!r}", name=fullname)
        folder = ROOT.joinpath(*parts)
        for file, package in ((folder / "__init__.py", True), (folder.with_name(parts[-1] + ".py"), False)):
            stamp = _stamp(file)
            try:
                data = file.read_bytes()
            except (FileNotFoundError, NotADirectoryError, IsADirectoryError):
                continue
            self._read[fullname] = (data, stamp)
            return importlib.util.spec_from_file_location(
                fullname, str(file), loader=self, submodule_search_locations=[str(folder)] if package else None)
        if folder.is_dir():                     # a folder without __init__.py (tests/fixtures): a namespace package
            spec = importlib.machinery.ModuleSpec(fullname, self, is_package=True)
            spec.submodule_search_locations = [str(folder)]
            return spec
        raise ModuleNotFoundError(f"No module named {fullname!r}", name=fullname)

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        data, stamp = self._read.pop(module.__name__, (None, None))
        if data is None:                        # a namespace package: nothing to execute
            return
        # Executed before — by this finder, or by any loader if the namespace already holds names (a fresh module
        # has only the import system's dunders): other modules may still hold objects of that earlier run.
        if module.__name__ in _EXECUTED or any(not k.startswith("__") for k in vars(module)):
            _RELOADED.add(module.__name__)
        _EXECUTED.add(module.__name__)
        _record(_rel(module.__file__), _sha(data), stamp)
        exec(compile(data, module.__file__, "exec", dont_inherit=True), module.__dict__)  # noqa: S102
        _OWN.setdefault(module.__name__, _own(module))


def _own(module) -> dict:
    """The functions and classes a module defined itself, by attribute name."""
    return {attr: value for attr, value in vars(module).items()
            if isinstance(value, (types.FunctionType, type)) and getattr(value, "__module__", None) == module.__name__}


_FINDER = _Finder()
sys.meta_path.insert(0, _FINDER)
_init_stamp = _stamp(__file__)                  # before the read, like every other library file
_record("__init__.py", _sha(Path(__file__).read_bytes()), _init_stamp)
del _init_stamp


def pin_script(path) -> None:
    """Record the bytes of a library file Python ran directly (render.py as __main__), read as it starts."""
    stamp = _stamp(path)
    _record(_rel(path), _sha(Path(path).read_bytes()), stamp)


def _is_test(name: str) -> bool:
    tests = f"{__name__}.tests"
    return name == tests or name.startswith(tests + ".")


def _rerun_modules() -> list[str]:
    """Library modules whose own functions or classes are not the ones their first execution defined but new ones of
    the same module: the trace a re-run leaves in the module itself, whatever ran it (a value from outside the
    module — a test's mock.patch — is monkeypatching, outside these checks)."""
    out = []
    for name, first in sorted(_OWN.items()):
        module = sys.modules.get(name)
        if module is None or _is_test(name):
            continue
        for attr, value in sorted(first.items()):
            now = getattr(module, attr, None)
            if now is not value and isinstance(now, (types.FunctionType, type)) \
                    and getattr(now, "__module__", None) == name:
                out.append(f"{name}: its own {attr} was replaced by a new one of the same module (it was executed "
                           "again)")
                break
    return out


def _stale_references() -> list[str]:
    """Functions and classes a library module holds under a name that their own library module no longer has: the
    traces any re-execution or replacement of that module leaves in the modules that imported from it."""
    out = []
    for name, module in sorted(list(sys.modules.items()), key=lambda item: item[0]):
        if module is None or not name.startswith(__name__ + ".") or _is_test(name):
            continue
        for attr, value in sorted(vars(module).items()):
            home = getattr(value, "__module__", None)
            if not (isinstance(value, (types.FunctionType, type)) and isinstance(home, str) and home != name
                    and (home == __name__ or home.startswith(__name__ + ".")) and not _is_test(home)):
                continue
            owner = sys.modules.get(home)
            if owner is None or getattr(owner, value.__name__, None) is not value:
                out.append(f"{name}.{attr}: holds {home}.{value.__name__} from an earlier load of {home}")
    return out


def _bytecode_caches() -> list[str]:
    return sorted({p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
                   if p.name == "__pycache__" or p.suffix in (".pyc", ".pyo")})


def changed_since_load() -> list[str]:
    """Library code this process may be running that the disk no longer holds (empty: none); see the module
    docstring. Test modules are outside the library hash and are not compared."""
    out = []
    for name, module in sorted(list(sys.modules.items()), key=lambda item: item[0]):
        if name.startswith(__name__ + ".") and module is not None \
                and getattr(getattr(module, "__spec__", None), "loader", None) is not _FINDER:
            out.append(f"{name}: not loaded by the library's finder (from {getattr(module, '__file__', None)})")
    out += [f"{name}: loaded again in this process (modules that imported it may still run its earlier code)"
            for name in sorted(_RELOADED) if not _is_test(name)]
    out += _rerun_modules()
    out += _stale_references()
    out += [f"{rel}: run from two different contents in this process" for rel in sorted(_CONFLICTS)
            if not rel.startswith("tests/")]
    out += [f"{rel}: a bytecode cache under the library" for rel in _bytecode_caches()]
    for rel, sha in sorted(_LOADED.items()):
        if rel.startswith("tests/"):
            continue
        try:
            now = _sha((ROOT / rel).read_bytes())
        except OSError:
            now = None
        if now != sha:
            out.append(f"{rel}: changed on disk since this process loaded it")
        elif _stamp(ROOT / rel) != _STAMPS.get(rel):
            out.append(f"{rel}: modified since this process loaded it")
    return out


def ensure_current() -> None:
    """Raise LibraryChanged unless the library code this process runs is the code on disk."""
    changed = changed_since_load()
    if changed:
        raise LibraryChanged(f"library code this process runs differs from the disk ({'; '.join(changed[:5])}); run "
                             "the command again in a new process")

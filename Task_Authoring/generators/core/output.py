"""Idempotent, confined publication of generator outputs.

Every task's generators used to write their outputs with `Path.write_text`. A re-run that changed nothing still rewrote
the files, so mtimes moved and `tools/stage_gate.py` failed the "output older than its input" check; and a rebuild
silently overwrote a stored, platform-reviewed revision. This module makes publication explicit:

  * a render stages its bytes in Working_Files/build/staging/<build_id>/, then `plan()` says what would change and
    `publish()` writes only the files whose bytes actually differ (unchanged files keep their mtime), each one through
    a temp file in the target's own directory plus os.replace, so a reader never sees a half-written file;
  * `publish()` re-hashes every target just before acting on it, the unchanged ones included, and refuses
    (PublishError) if someone edited it since `plan()` — a partial publication is reported by name, never silently
    widened;
  * deletion only happens with prune=True and only for a file whose current sha256 is exactly the one the previous
    build recorded, so a file edited by hand since the last build is reported stale and left alone; the paths a build
    records and prunes by must be spelled canonically (no '.', no doubled '/'), so one file has one name;
  * stored revision copies (Working_Files/run_forensics/<rev>/) are immutable and only `store_revision` writes there:
    identical bytes are a no-op, different bytes are an error, and nothing else here can stage, replace, append to,
    prune or (while clearing a staging folder) delete a path there — refused by name wherever a
    Working_Files/run_forensics folder appears in the absolute path,
    the task dir included (each component compared after Unicode compatibility folding, case folding and dropping
    non-ASCII marks, as a case-insensitive, normalising filesystem might alias it), and by folder identity (device and
    inode of the task's stored-revision folder); `store_revision` refuses a task dir that lies inside one;
  * every path is confined to the task dir. The task dir itself is never resolved here: it is made absolute and every
    folder from "/" down to it must be a real folder (callers resolve a path once, where a command starts, if it may
    contain a symlink). `confine` then checks a task-relative name (no absolute paths, no '..', no empty names, no
    symlink between the task dir and the target); every read and write walks from "/" to the target's folder again,
    opening each folder O_DIRECTORY | O_NOFOLLOW, and acts relative to that folder's descriptor (openat, renameat,
    linkat, unlinkat), so a folder swapped for a symlink after a check is refused rather than followed. While a
    TaskLock is held, each walk also checks that the folder at the task path is still the one the lock pinned (device,
    inode), so a task folder replaced by another real folder is refused too. Task dirs are shared with other
    processes; this keeps a render inside its own task. It cannot stop another process from editing a file; it detects
    that and refuses. Nor can it stop another process from moving a folder this module holds open between a check and
    the next system call on that folder's descriptor (POSIX has no "act here only if this folder is still at this
    path"); that is outside what it guards.

Atomicity on macOS: os.replace within one directory is atomic, and the temp file is created in the target's own
directory, so it is on the same filesystem (EXDEV is impossible). The file data is fsync'd before the replace. The
directory itself is fsync'd best-effort: fsync on a directory fd is not reliable on macOS (it may fail with EINVAL), so
the rename is atomic and crash-safe against readers but its metadata durability is not guaranteed on power loss.
Nothing is ever written into an existing file: a new file replaces it, so a hard link to the old file keeps its bytes.
Nothing in this module writes timestamps into file contents.
"""
from __future__ import annotations

import fcntl
import hashlib
import os
import re
import secrets
import stat
import unicodedata
from dataclasses import dataclass
from pathlib import Path

__all__ = [
    "PublishError", "Change", "TaskLock", "Build", "PROTECTED",
    "sha256_bytes", "sha256_file", "file_stamp", "canonical", "confine", "read_bytes", "task_sha256", "append_line",
    "check", "store_revision",
]

STATUSES = frozenset({"new", "changed", "unchanged", "stale", "removed"})
PROTECTED = "Working_Files/run_forensics"           # stored revisions: only store_revision writes below it
STAGING = "Working_Files/build/staging"

_REV_NAME = re.compile(r"^rev[0-9]+[a-z]?$")
_BUILD_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
_CHUNK = 1 << 20
_DIR_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW


class PublishError(Exception):
    """A publication was refused or could not be completed safely."""


@dataclass(frozen=True)
class Change:
    path: str                      # relative to the task dir, posix separators
    status: str                    # "new" | "changed" | "unchanged" | "stale" | "removed"
    sha256_old: str | None         # the target as it was, or None when it did not exist
    sha256_new: str | None         # the bytes this build stages, or None for stale/removed

    def __post_init__(self):
        if self.status not in STATUSES:
            raise ValueError(f"{self.path}: unknown status {self.status!r}")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str | None:
    """The sha256 hex digest of a regular file at any path, or None when there is none (a plain read helper)."""
    p = Path(path)
    try:
        if not p.is_file():
            return None
    except OSError:
        return None
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(_CHUNK), b""):
            h.update(chunk)
    return h.hexdigest()


def file_stamp(path: Path) -> tuple | None:
    """(device, inode, size, mtime_ns, ctime_ns) of a file at any path, None when there is none. Every write, rename,
    chmod or xattr change sets ctime to the current time, and no system call sets it otherwise, so two equal stamps
    mean the file was not modified in between — even by a change that later put the old bytes back, which a content
    hash cannot see (short of the system clock being set back to the old ctime)."""
    try:
        st = os.stat(path)
    except FileNotFoundError:
        return None
    except OSError as exc:
        return ("unreadable", exc.errno)
    return (st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns)


def _root(task_dir: Path) -> Path:
    """The task dir as given, made absolute but never resolved. Every folder from "/" down to it, itself included, must
    be a real folder: each is opened O_DIRECTORY | O_NOFOLLOW, so a symlink anywhere on the way is refused."""
    if ".." in Path(task_dir).parts:
        raise PublishError(f"task dir must not contain '..': {task_dir}")
    root = Path(os.path.abspath(task_dir))
    try:
        os.close(_walk(root, [], create=False))
    except OSError as exc:
        raise PublishError(f"task dir {root} must be a real folder reached without following a symlink "
                           f"({exc})") from exc
    return root


def _rel_parts(rel_path: str) -> list[str]:
    """The components of a task-relative path, refusing anything that could name a place outside the task dir."""
    if not isinstance(rel_path, str):
        raise PublishError(f"path must be a string: {rel_path!r}")
    if not rel_path:
        raise PublishError("empty path refused")
    if "\x00" in rel_path:
        raise PublishError(f"NUL byte in path refused: {rel_path!r}")
    if rel_path.startswith("/"):
        raise PublishError(f"absolute path refused: {rel_path!r}")
    raw_parts = rel_path.split("/")
    if any(p == "" for p in raw_parts):
        raise PublishError(f"empty path component refused: {rel_path!r}")
    if any(p == ".." for p in raw_parts):
        raise PublishError(f"'..' component refused: {rel_path!r}")
    parts = [p for p in raw_parts if p != "."]
    if not parts:
        raise PublishError(f"path names nothing: {rel_path!r}")
    return parts


def canonical(rel_path: str) -> str:
    """The one spelling of a task-relative path: its components joined by '/', '.' components dropped."""
    return "/".join(_rel_parts(rel_path))


def _require_canonical(rel_path: str) -> str:
    rel = canonical(rel_path)
    if rel != rel_path:
        raise PublishError(f"{rel_path!r} is not a canonical task-relative path (write {rel!r})")
    return rel


def confine(task_dir: Path, rel_path: str) -> Path:
    """Resolve `rel_path` under `task_dir`, refusing anything that could escape it.

    Refused: a non-string or empty path, an absolute path, an empty or '..' component, a NUL byte, and any symlink in
    an existing component between the task dir and the target, the target included. Components that do not exist yet
    are allowed (the caller creates them). This is the readable check by name; the reads and writes below repeat it by
    descriptor, so a folder turned into a symlink after this check is still refused.
    """
    root = _root(task_dir)
    parts = _rel_parts(rel_path)
    cur = root
    for part in parts:
        cur = cur / part
        if cur.is_symlink():
            raise PublishError(f"symlink in path refused: {rel_path!r} ({cur})")
        if not cur.exists():
            break
    return root.joinpath(*parts)


_PROTECTED_PARTS = ("working_files", "run_forensics")


def _fold(text: str) -> str:
    """An ASCII skeleton for comparing names the way a case-insensitive, normalising filesystem might alias them:
    compatibility decomposition, case folding, then every non-ASCII code point dropped (accents, look-alike marks,
    zero-width characters). It over-approximates: a few distinct names fold together, which only refuses more."""
    return "".join(ch for ch in unicodedata.normalize("NFKD", text).casefold() if ch.isascii())


def _inside_protected(parts) -> bool:
    """True when two consecutive path components fold to Working_Files/run_forensics: the path is a stored-revision
    folder or lies below one, wherever that folder sits in it."""
    folded = [_fold(p) for p in parts]
    n = len(_PROTECTED_PARTS)
    return any(tuple(folded[i:i + n]) == _PROTECTED_PARTS for i in range(len(folded) - n + 1))


def _protected(root: Path, rel: str) -> bool:
    """True when root/rel lies in a stored-revision folder, under every spelling that folds to one — named in the
    task-relative path or in the task dir itself (a task dir set inside Working_Files/run_forensics/ must not hide
    it)."""
    return _inside_protected([*Path(root).parts[1:], *_rel_parts(rel)])


def _refuse_protected(root: Path, rel: str) -> None:
    if _protected(root, rel):
        raise PublishError(f"{rel}: inside a stored-revision folder ({PROTECTED}) of {root}; stored revisions are "
                           "written only by store_revision")


# ---------------------------------------------------------------- descriptor-relative access

_LOCKED: dict[str, tuple[int, int]] = {}         # task dir -> (device, inode) of the folder its held TaskLock locked


def _walk(root: Path, parts: list[str], *, create: bool, forbid: tuple[int, int] | None = None,
          seen: list | None = None) -> int | None:
    """A descriptor for root/parts..., walked from "/" with every component opened O_NOFOLLOW (root is a real path,
    so none of its components is a symlink unless one was swapped in since). A missing folder below root is created
    when `create` is set, otherwise the result is None. A symlinked component raises OSError. While a TaskLock on root
    is held, the folder opened as root must be the one it locked (device, inode): a task folder replaced since, by a
    symlink or by another real folder, is refused before anything inside it is touched. `seen` receives root's
    (device, inode). With `forbid`, a folder below root whose (device, inode) equals it is refused before anything is
    created inside it."""
    anchors = list(Path(root).parts[1:])
    pinned = _LOCKED.get(str(root))
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for i, part in enumerate(anchors + list(parts)):
            try:
                nfd = os.open(part, _DIR_FLAGS, dir_fd=fd)
            except FileNotFoundError:
                if i < len(anchors):
                    raise
                if not create:
                    return None
                try:
                    os.mkdir(part, 0o755, dir_fd=fd)
                except FileExistsError:
                    pass
                nfd = os.open(part, _DIR_FLAGS, dir_fd=fd)
            os.close(fd)
            fd = nfd
            if i == len(anchors) - 1:
                st = os.fstat(fd)
                if seen is not None:
                    seen.append((st.st_dev, st.st_ino))
                if pinned is not None and (st.st_dev, st.st_ino) != pinned:
                    raise PublishError(f"{root} is no longer the task folder this command locked (it was replaced "
                                       "or moved); nothing more is written")
            if forbid is not None and i >= len(anchors):
                st = os.fstat(fd)
                if (st.st_dev, st.st_ino) == forbid:
                    below = "/".join(list(parts)[:i - len(anchors) + 1])
                    raise PublishError(f"{below} is the stored-revision folder {PROTECTED}; only store_revision "
                                       "writes there")
        opened, fd = fd, None
        return opened
    finally:
        if fd is not None:
            os.close(fd)


def _remove_tree(parent_fd: int, name: str, parts: list[str]) -> list[str]:
    """Remove `name` from the folder `parent_fd`, and everything below it, by descriptor and without following a
    symlink — except a stored-revision folder (`parts` + `name` checked like _inside_protected) and what lies below
    it, which are kept with the folders above them. Returns the kept paths (empty: everything was removed)."""
    here = [*parts, name]
    if _inside_protected(here):
        return ["/".join(here)]
    try:
        st = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        return []
    if not stat.S_ISDIR(st.st_mode):
        os.unlink(name, dir_fd=parent_fd)
        return []
    fd = os.open(name, _DIR_FLAGS, dir_fd=parent_fd)
    try:
        kept = [k for entry in sorted(os.listdir(fd)) for k in _remove_tree(fd, entry, here)]
    finally:
        os.close(fd)
    if not kept:
        os.rmdir(name, dir_fd=parent_fd)
    return kept


def _protected_identity(root: Path) -> tuple[int, int] | None:
    """(device, inode) of the stored-revision folder, or None while it does not exist."""
    try:
        fd = _walk(root, PROTECTED.split("/"), create=False)
    except OSError as exc:
        raise PublishError(f"{PROTECTED}: cannot open the stored-revision folder without following a symlink "
                           f"({exc})") from exc
    if fd is None:
        return None
    try:
        st = os.fstat(fd)
        return st.st_dev, st.st_ino
    finally:
        os.close(fd)


class _Parent:
    """The folder of a task-relative path, opened by descriptor without following a symlink at any level.

    `fd` is None when the folder does not exist and `create` is not set; `name` is the last component, `rel` the
    canonical path. With `write`, a path in a stored-revision folder is refused by name (anywhere in the absolute
    path) and by the identity of the task's own stored-revision folder."""

    def __init__(self, task_dir: Path, rel_path: str, *, create: bool = False, write: bool = False,
                 seen: list | None = None):
        root = _root(task_dir)
        confine(root, rel_path)                      # early, readable refusal; the descriptor walk is the guard
        parts = _rel_parts(rel_path)
        self.rel, self.name = "/".join(parts), parts[-1]
        self.fd = None
        if write:
            _refuse_protected(root, self.rel)
        forbid = _protected_identity(root) if write else None
        try:
            self.fd = _walk(root, parts[:-1], create=create, forbid=forbid, seen=seen)
        except OSError as exc:
            raise PublishError(f"{self.rel}: cannot open its folder without following a symlink ({exc})") from exc

    def __enter__(self) -> "_Parent":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None


def _open_regular(dfd: int, name: str, rel: str, flags: int = os.O_RDONLY) -> int | None:
    """A descriptor for the regular file `name` in folder `dfd`, None when it is absent (and not created). A symlink or
    a non-regular file (folder, FIFO, device) is refused without blocking: O_NONBLOCK until its type is known."""
    try:
        fd = os.open(name, flags | os.O_NOFOLLOW | os.O_NONBLOCK, 0o644, dir_fd=dfd)
    except FileNotFoundError:
        return None
    except OSError as exc:
        raise PublishError(f"{rel}: a symlink or a file that cannot be opened ({exc})") from exc
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise PublishError(f"{rel}: not a regular file")
        os.set_blocking(fd, True)
    except BaseException:
        os.close(fd)
        raise
    return fd


def _read_at(dfd: int, name: str, rel: str) -> bytes | None:
    fd = _open_regular(dfd, name, rel)
    if fd is None:
        return None
    with os.fdopen(fd, "rb") as fh:
        return fh.read()


def _sha_at(dfd: int, name: str, rel: str) -> str | None:
    fd = _open_regular(dfd, name, rel)
    if fd is None:
        return None
    h = hashlib.sha256()
    with os.fdopen(fd, "rb") as fh:
        for chunk in iter(lambda: fh.read(_CHUNK), b""):
            h.update(chunk)
    return h.hexdigest()


def _fsync_fd(dfd: int) -> None:
    """Best-effort directory fsync; macOS may refuse it (EINVAL) and the rename is still atomic."""
    try:
        os.fsync(dfd)
    except OSError:
        pass


def _write_at(dfd: int, name: str, data: bytes) -> None:
    """`data` -> `name` in folder `dfd`: a new temp file there (O_EXCL | O_NOFOLLOW), fsync, then os.replace, which
    swaps the directory entry and never writes through an existing file or link."""
    tmp = f".tmp-{secrets.token_hex(8)}.part"
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=dfd)
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, name, src_dir_fd=dfd, dst_dir_fd=dfd)
    except BaseException:
        try:
            os.unlink(tmp, dir_fd=dfd)
        except OSError:
            pass
        raise
    _fsync_fd(dfd)


def read_bytes(task_dir: Path, rel_path: str) -> bytes | None:
    """The bytes of a regular file inside the task dir, None when it does not exist; read by descriptor."""
    with _Parent(task_dir, rel_path) as at:
        return None if at.fd is None else _read_at(at.fd, at.name, at.rel)


def task_sha256(task_dir: Path, rel_path: str) -> str | None:
    """The sha256 of a regular file inside the task dir, None when it does not exist; read by descriptor."""
    with _Parent(task_dir, rel_path) as at:
        return None if at.fd is None else _sha_at(at.fd, at.name, at.rel)


def append_line(task_dir: Path, rel_path: str, line: str, *, skip_if_last: bool = False) -> bool:
    """Add one line to a log file inside the task dir (created if missing); returns whether it was added. The file is
    rewritten through a new file and os.replace, never appended to in place, so a hard link to the old file keeps its
    bytes. With skip_if_last, a line equal to the file's last line is not added again (a retried step logs once)."""
    if "\n" in line or "\r" in line:
        raise ValueError("append_line takes a single line")
    data = line.encode("utf-8")
    with _Parent(task_dir, rel_path, create=True, write=True) as at:
        old = _read_at(at.fd, at.name, at.rel) or b""
        if skip_if_last and old.strip(b"\n") and old.rstrip(b"\n").rsplit(b"\n", 1)[-1] == data:
            return False
        if old and not old.endswith(b"\n"):
            old += b"\n"
        _write_at(at.fd, at.name, old + data + b"\n")
        return True


class TaskLock:
    """Exclusive, non-blocking render lock: Working_Files/build/.lock, held for the life of the context manager.

    It also pins the task folder: the (device, inode) of the folder the lock file was reached through. While the lock
    is held, every walk from this task dir checks that the folder it opens there is still that one (_walk)."""

    REL = "Working_Files/build/.lock"

    def __init__(self, task_dir: Path):
        self.task_dir = _root(task_dir)
        self.path = confine(self.task_dir, self.REL)
        self._fd: int | None = None

    def __enter__(self) -> "TaskLock":
        seen: list = []
        with _Parent(self.task_dir, self.REL, create=True, write=True, seen=seen) as at:
            fd = _open_regular(at.fd, at.name, at.rel, os.O_RDWR | os.O_CREAT)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            os.close(fd)
            raise PublishError("another render holds the lock") from None
        self._fd = fd
        if seen:                                    # empty only for the task dir "/", which has no folder to pin
            _LOCKED[str(self.task_dir)] = seen[-1]
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        fd, self._fd = self._fd, None
        _LOCKED.pop(str(self.task_dir), None)
        if fd is not None:
            try:
                fcntl.flock(fd, fcntl.LOCK_UN)
            finally:
                os.close(fd)


class Build:
    """One staged build of a task's outputs.

    Staging lives in Working_Files/build/staging/<build_id>/ so a crashed render leaves its bytes where the next one
    can ignore or discard them, never half-applied in the task dir.
    """

    def __init__(self, task_dir: Path, build_id: str):
        if not isinstance(build_id, str) or not _BUILD_ID.match(build_id or ""):
            raise PublishError(f"invalid build id: {build_id!r}")
        self.task_dir = _root(task_dir)
        self.build_id = build_id
        self.staging_rel = f"{STAGING}/{build_id}"
        self.staging = confine(self.task_dir, self.staging_rel)
        self._clear_staging()                                 # a leftover from an interrupted run of the same id
        self._staged: dict[str, bytes] = {}
        self._plan: list[Change] | None = None
        self._plan_previous: dict[str, str] | None = None

    def _clear_staging(self) -> None:
        """Remove this build's staging folder, except a stored-revision folder found inside it (with the folders above
        it), which is kept and named in a PublishError."""
        with _Parent(self.task_dir, self.staging_rel, write=True) as at:
            if at.fd is None:
                return
            above = [*self.task_dir.parts[1:], *self.staging_rel.split("/")[:-1]]
            try:
                kept = _remove_tree(at.fd, at.name, above)
            except OSError as exc:
                raise PublishError(f"{self.staging_rel}: cannot clear the staging folder ({exc})") from exc
        if kept:
            raise PublishError(f"{self.staging_rel}: holds a stored-revision folder ({kept[0]}), so it was left in "
                               "place; move that revision out of the staging folder")

    def add(self, rel_path: str, data: bytes) -> None:
        if isinstance(data, bytearray):
            data = bytes(data)
        if not isinstance(data, bytes):
            raise TypeError(f"{rel_path}: data must be bytes, not {type(data).__name__}")
        rel = canonical(rel_path)
        confine(self.task_dir, rel)
        _refuse_protected(self.task_dir, rel)
        if rel in self._staged:
            raise PublishError(f"{rel}: added twice to this build")
        try:
            with _Parent(self.task_dir, f"{self.staging_rel}/{rel}", create=True, write=True) as at:
                _write_at(at.fd, at.name, data)
        except OSError as exc:
            raise PublishError(f"{rel}: could not stage ({exc})") from exc
        self._staged[rel] = data
        self._plan = None

    def files(self) -> dict[str, bytes]:
        return dict(self._staged)

    def staged_bytes(self, rel_path: str) -> bytes | None:
        """The staged copy of `rel_path` as it is on disk, read back by descriptor."""
        return read_bytes(self.task_dir, f"{self.staging_rel}/{canonical(rel_path)}")

    def plan(self, previous: dict[str, str] | None = None) -> list[Change]:
        """What publish() would do; also the snapshot publish() compares against (see publish)."""
        return list(self._plan_for(previous))

    def _plan_for(self, previous: dict[str, str] | None) -> list[Change]:
        prev = dict(previous) if previous else None
        if self._plan is None or self._plan_previous != prev:
            self._plan = _plan(self.task_dir, self._staged, prev)
            self._plan_previous = prev
        return self._plan

    def publish(self, *, prune: bool = False, previous: dict[str, str] | None = None) -> list[Change]:
        """Publish staged bytes; returns the final Change list ("removed" for pruned files).

        Uses the plan() snapshot when one was taken for the same `previous` — that is the state the compare-and-swap
        guards — otherwise plans now. Every target, the unchanged ones included, is re-hashed just before it is acted
        on; already-replaced files stay replaced if a later file fails: the PublishError names the file that failed
        and lists what was published. A stale path in the stored-revision folder is never removed.
        """
        planned = self._plan_for(previous)
        self._plan = None                                     # the disk is about to differ from this snapshot
        self._plan_previous = None
        done: list[Change] = []
        for ch in planned:
            if ch.status in ("new", "changed", "unchanged"):
                try:
                    if ch.status == "unchanged":
                        current = task_sha256(self.task_dir, ch.path)
                        if current != ch.sha256_old:
                            raise PublishError(f"target changed since plan (expected {ch.sha256_old}, "
                                               f"found {current or 'no file'})")
                    else:
                        with _Parent(self.task_dir, ch.path, create=True, write=True) as at:
                            current = _sha_at(at.fd, at.name, ch.path)
                            if current != ch.sha256_old:
                                raise PublishError(f"target changed since plan (expected {ch.sha256_old or 'no file'}, "
                                                   f"found {current or 'no file'})")
                            _write_at(at.fd, at.name, self._staged[ch.path])
                except (OSError, PublishError) as exc:
                    raise PublishError(f"{ch.path}: {exc}; already published: {_published(done)}") from exc
                done.append(ch)
                continue
            if ch.status == "stale" and prune and not _protected(self.task_dir, ch.path):
                expected = (previous or {}).get(ch.path)
                try:
                    with _Parent(self.task_dir, ch.path, write=True) as at:
                        current = None if at.fd is None else _sha_at(at.fd, at.name, ch.path)
                        if current is not None and expected is not None and current == expected:
                            os.unlink(at.name, dir_fd=at.fd)
                            _fsync_fd(at.fd)
                            done.append(Change(ch.path, "removed", current, None))
                            continue
                except (OSError, PublishError) as exc:
                    raise PublishError(
                        f"{ch.path}: prune failed ({exc}); already published: {_published(done)}") from exc
            done.append(ch)
        return done

    def discard(self) -> None:
        """Remove the staging folder, best effort: whatever stops the cleanup (a folder this build cannot safely
        remove, an unexpected error) leaves the folder for the next build of this id to clear, and never replaces the
        outcome the caller is reporting."""
        try:
            self._clear_staging()
        except Exception:
            pass
        self._staged.clear()
        self._plan = None
        self._plan_previous = None


def _published(done: list[Change]) -> list[str]:
    return [c.path for c in done if c.status in ("new", "changed", "removed")]


def _plan(root: Path, files: dict[str, bytes], previous: dict[str, str] | None) -> list[Change]:
    """One Change per staged file and per earlier-owned file this build does not produce; every path must be spelled
    canonically, so an alias can neither hide a file from the plan nor reach one by a second name."""
    for rel in list(files) + list(previous or {}):
        _require_canonical(rel)
    changes: list[Change] = []
    for rel in sorted(files):
        old = task_sha256(root, rel)
        new = sha256_bytes(files[rel])
        status = "new" if old is None else ("unchanged" if old == new else "changed")
        changes.append(Change(rel, status, old, new))
    for rel in sorted(previous or {}):
        if rel in files:
            continue
        changes.append(Change(rel, "stale", task_sha256(root, rel), None))
    return changes


def check(task_dir: Path, files: dict[str, bytes], previous: dict[str, str] | None = None) -> list[Change]:
    """In memory: what publish(previous=previous) would do with these bytes. Writes nothing."""
    root = _root(task_dir)
    for rel, data in files.items():
        if not isinstance(data, bytes):
            raise TypeError(f"{rel}: data must be bytes, not {type(data).__name__}")
    return _plan(root, files, previous)


def store_revision(task_dir: Path, rev: str, source_rel: str = "01_Universe_Inject.sql") -> Change:
    """Copy a reviewed source into Working_Files/run_forensics/<rev>/, which is immutable once written."""
    if not isinstance(rev, str) or not _REV_NAME.match(rev or ""):
        raise PublishError(f"revision name must look like rev<N>[a-z]: {rev!r}")
    root = _root(task_dir)
    if _inside_protected(root.parts[1:]):
        raise PublishError(f"task dir {root} is inside a stored-revision folder ({PROTECTED}); store_revision writes "
                           f"only below a task's own {PROTECTED}/")
    data = read_bytes(root, source_rel)
    if data is None:
        raise PublishError(f"{source_rel}: no such file to store")
    new = sha256_bytes(data)
    name = _rel_parts(source_rel)[-1]
    rel = f"{PROTECTED}/{rev}/{name}"
    confine(root, rel)                          # early, readable refusal; the descriptor walk below is the guard
    try:
        dfd = _walk(root, [*PROTECTED.split("/"), rev], create=True)
    except OSError as exc:
        raise PublishError(f"{rel}: cannot open the revision folder without following a symlink ({exc})") from exc
    tmp = f".tmp-{secrets.token_hex(8)}.part"
    try:
        existing = _read_at(dfd, name, rel)
        if existing is not None:
            return _settled(rel, existing, new)
        fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=dfd)
        try:
            with os.fdopen(fd, "wb") as fh:
                fh.write(data)
                fh.flush()
                os.fsync(fh.fileno())
            try:                                # no-clobber: fails if another writer stored this revision first
                os.link(tmp, name, src_dir_fd=dfd, dst_dir_fd=dfd, follow_symlinks=False)
            except FileExistsError:
                return _settled(rel, _read_at(dfd, name, rel), new)
        finally:
            try:
                os.unlink(tmp, dir_fd=dfd)
            except OSError:
                pass
        _fsync_fd(dfd)
        return Change(rel, "new", None, new)
    except PublishError:
        raise
    except OSError as exc:
        raise PublishError(f"{rel}: could not store revision ({exc})") from exc
    finally:
        os.close(dfd)


def _settled(rel: str, existing: bytes | None, new: str) -> Change:
    if existing is None:
        raise PublishError(f"{rel}: the stored revision vanished while storing it")
    old = sha256_bytes(existing)
    if old == new:
        return Change(rel, "unchanged", old, new)
    raise PublishError(f"{rel}: stored revision is immutable (has {old}, source is now {new})")

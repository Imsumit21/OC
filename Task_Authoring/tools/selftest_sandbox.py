#!/usr/bin/env python3
"""selftest_sandbox.py - the self-test scratch root, and a throwaway workspace so no self-test writes a shared file.

Why. The self-tests of stage_gate.py and hardness_gate.py reach three cache writers: persona_view.py and base_check.py
rebuild and re-stamp support/local_search/cache/{pv,base}_*.json when a base export's size or mtime changed, and
tools/hg.py (through setup/local_search.py) refreshes the patched Evals helpers in support/local_search/tools/, whose
query and record caches live in support/local_search/cache/. Moving a scratch folder doesn't isolate them; a separate
workspace does.

Scratch root. Task_Authoring/support/scratch/. Every self-test temp folder is tempfile.mkdtemp(dir=<scratch root>)
(scratch_tmp()), unique per run and removed afterwards; never the system temp folder.

Sandbox. A tempfile.mkdtemp(dir=<scratch root>) folder holding a workspace:
  ws/Task_Authoring/  copies of tools/, setup/, references/, playbooks/, skills/, Guide/, README.md, support/examples/
                      and support/hardness_ledger/, and support/local_search/cache/ seeded with copies of the cache's
                      top-level *.json (persona_view's pv_*, base_check's base_*, the Gmail index): their source stamps
                      are workspace-relative, so they stay current and nothing rebuilds. The Evals helpers refuse a data
                      file that resolves outside their root, so the sandbox's copy of setup/local_search.py roots them
                      in the real workspace (data read in place) and keeps their patched copies and caches inside the
                      sandbox (LOCAL_SEARCH_PATCH; hg.py regenerates the copies there on first use).
                      --layout staged also overlays support/pending_edits/MANIFEST.json's staged files on their targets
                      and copies support/pending_tools/*.py into tools/: the post-move layout, rehearsed before the move.
  ws/Evals, ws/HarmonyGames_GitHub, ws/HarmonyGames_Gmail, ws/HarmonyGames_Other_Services
                      symlinks to the real read-only folders (never chmod'ed).
A symlink is not read-only: a write through it lands in the real folder. So before each command, every cache, ledger,
scratch, temp and output path the sandboxed tools compute is asserted to resolve inside the sandbox; after it,
`find <real linked folders> -newer <marker made at the start>` must print nothing. Either failure is a LEAK (exit 3).
Commands run with cwd ws/, PYTHONDONTWRITEBYTECODE=1, TMPDIR inside the sandbox (a tool that calls tempfile without
dir= stays inside), no TASK_AUTHORING_* variables, and TA_SELFTEST_SANDBOX naming the sandbox: a self-test that finds
its own bundle inside that sandbox runs in place instead of starting another one.

Usage:
  python3 -B Task_Authoring/tools/selftest_sandbox.py [--layout live|staged] [--keep] -- TOOL.py [ARGS...]
  python3 -B Task_Authoring/tools/selftest_sandbox.py --suite move [--layout live|staged]   (every move self-test)
  python3 -B Task_Authoring/tools/selftest_sandbox.py --self-test
Exit: the command's exit code (the suite: 0 only if every command passed); 3 = a leak; 2 = usage error.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def _bundle() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "difficulty_stats.py").is_file():
            return parent
    raise SystemExit("selftest_sandbox: cannot find the Task_Authoring bundle (no tools/difficulty_stats.py above)")


HERE = Path(__file__).resolve().parent
BUNDLE = _bundle()
WS = BUNDLE.parent
SCRATCH = BUNDLE / "support" / "scratch"
ENV_FLAG = "TA_SELFTEST_SANDBOX"
LINKED = ("Evals", "HarmonyGames_GitHub", "HarmonyGames_Gmail", "HarmonyGames_Other_Services")
COPY = ("tools", "setup", "references", "playbooks", "skills", "Guide", "README.md", "support/examples",
        "support/hardness_ledger", "support/fixtures/surface_formats",
        "support/fixtures/season_pass_rev13/00_Assigments.md")       # a V3 assignment for self-tests that need one
CACHE = Path("support") / "local_search" / "cache"
# The sandbox's copy of setup/local_search.py: the Evals helpers refuse a data file that resolves outside their root,
# so their root is the real workspace (data and Evals/ read in place), while their patched copies (LOCAL/tools) and
# caches (CACHE_REL) stay inside the sandbox. Both anchors must match exactly once, else the sandbox is not built;
# the path probe then asserts local_search.LOCAL, .TOOLS and .WORKSPACE/CACHE_REL resolve inside the sandbox.
# The sandbox's copy of tools/task_context.py accepts the universe sources (manifest, service folders) in the real
# workspace: the sandbox links them, and a link resolves outside the sandbox workspace, which the loader refuses. Only
# these two read checks change; the KB paths (written) and DEFAULT_TASK stay the sandbox's.
TASK_CONTEXT_PATCH = (
    ("        if WORKSPACE not in manifest_path.parents:\n",
     "        if WORKSPACE not in manifest_path.parents and Path({ws!r}) not in manifest_path.parents:  # selftest_sandbox\n"),
    ("        outside = [s for s, p in paths.items() if WORKSPACE not in p.parents]\n",
     "        outside = [s for s, p in paths.items() if WORKSPACE not in p.parents and Path({ws!r}) not in p.parents]"
     "  # selftest_sandbox\n"))
LOCAL_SEARCH_PATCH = (("WORKSPACE = BUNDLE.parent ", "WORKSPACE = Path({ws!r})  # selftest_sandbox: the real workspace "),
                      ('CACHE_REL = f"{BUNDLE.name}/support/local_search/cache"',
                       'CACHE_REL = str((LOCAL / "cache").relative_to(WORKSPACE))  # selftest_sandbox: inside the sandbox'))
SUITE_MOVE = (["stage_gate.py", "--self-test"], ["hardness_gate.py", "--self-test"]) + tuple(
    [f"{t}.py", "--self-test"] for t in ("difficulty_mutation", "gradable_surface", "hardness_forecast",
                                         "hardness_ledger", "node_verdicts", "oracle_kit", "preflight_report",
                                         "surface_grader", "trajectory_ledger", "trap_liveness", "difficulty_stats",
                                         "selftest_sandbox"))
# write paths each sandboxed tool computes (module, attribute): asserted to resolve inside the sandbox
WRITE_PATHS = (("persona_view", "CACHE"), ("persona_view", "GMAIL_INDEX"), ("base_check", "CACHE"),
               ("shortcut_probe", "CACHE"), ("entity", "OUT"), ("local_search", "LOCAL"), ("local_search", "TOOLS"),
               ("hardness_ledger", "DEFAULT_LEDGER"), ("stage_gate", "SELFTEST_TMP"), ("selftest_sandbox", "SCRATCH"),
               ("trajectory_ledger", "BUNDLE"))
_PROBE = r"""
import json, sys, tempfile
from pathlib import Path
b = Path(sys.argv[1])
sys.path[:0] = [str(b / "tools"), str(b / "setup")]
out = {"tempfile.gettempdir()": str(Path(tempfile.gettempdir()).resolve())}
for mod, attr in json.loads(sys.argv[2]):
    try:
        m = __import__(mod)
    except ModuleNotFoundError as exc:
        if exc.name == mod:
            continue                      # not in this layout (a pending tool before the move)
        out[f"{mod} (import)"] = "ERROR " + repr(exc)
        continue
    except BaseException as exc:          # noqa: BLE001 - reported, never ignored
        out[f"{mod} (import)"] = "ERROR " + repr(exc)
        continue
    if hasattr(m, attr):
        out[f"{mod}.{attr}"] = str(Path(getattr(m, attr)).resolve())     # resolved here, in the sandbox's cwd
try:
    import local_search as ls
    out["local_search.WORKSPACE/CACHE_REL"] = str((ls.WORKSPACE / ls.CACHE_REL).resolve())
except ModuleNotFoundError:
    pass
print(json.dumps(out))
"""


def scratch_tmp(prefix: str) -> tempfile.TemporaryDirectory:
    """A unique self-test folder under the scratch root, removed when the context exits."""
    SCRATCH.mkdir(parents=True, exist_ok=True)
    return tempfile.TemporaryDirectory(prefix=prefix, dir=SCRATCH)


def in_sandbox(bundle: Path = BUNDLE) -> bool:
    """True when TA_SELFTEST_SANDBOX names a sandbox that holds this bundle (a stale variable never counts)."""
    flag = os.environ.get(ENV_FLAG)
    if not flag:
        return False
    try:
        bundle.resolve().relative_to(Path(flag).resolve())
    except ValueError:
        return False
    return True


def _inside(p: Path, root: Path) -> bool:
    try:
        p.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


class Leak(Exception):
    pass


class Sandbox:
    """A throwaway workspace under the scratch root (see the module docstring)."""

    def __init__(self, layout: str = "live", source: Path = BUNDLE, linked: dict | None = None, keep: bool = False,
                 ignore_newer: tuple = ()):
        if layout not in ("live", "staged"):
            raise ValueError(f"layout {layout!r}: live or staged")
        self.layout, self.source, self.keep = layout, source, keep
        self.ignore_newer = tuple(ignore_newer)     # externally edited input folders (never read by the calling test)
        self.linked = linked if linked is not None else {n: source.parent / n for n in LINKED}
        scratch = source / "support" / "scratch"
        scratch.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix=f"sandbox_{layout}_", dir=scratch))
        self.ws = self.root / "ws"
        self.bundle = self.ws / source.name
        self.tmp = self.root / "tmp"
        self.marker = self.root / "marker"

    def __enter__(self):
        try:
            self.marker.write_text("start\n")
            self._build()
        except BaseException:
            self.close()
            raise
        return self

    def __exit__(self, *exc):
        self.close()

    def close(self):
        if not self.keep:
            shutil.rmtree(self.root, ignore_errors=True)

    def _build(self):
        ignore = shutil.ignore_patterns("__pycache__", ".rollback")
        for part in COPY:
            src = self.source / part
            dst = self.bundle / part
            if src.is_dir():
                shutil.copytree(src, dst, symlinks=False, ignore=ignore)
            elif src.is_file():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        for rel, patch in (("setup/local_search.py", LOCAL_SEARCH_PATCH), ("tools/task_context.py", TASK_CONTEXT_PATCH)):
            ls = self.bundle / rel
            if ls.is_file():
                text = ls.read_text()
                for old, new in patch:
                    if text.count(old) != 1:
                        raise Leak(f"{rel}: patch anchor {old!r} found {text.count(old)} time(s), not once")
                    text = text.replace(old, new.format(ws=str(self.source.parent.resolve())))
                ls.write_text(text)
        cache = self.bundle / CACHE
        cache.mkdir(parents=True, exist_ok=True)
        for f in sorted((self.source / CACHE).glob("*.json")):
            if f.is_file() and not f.is_symlink():
                shutil.copy2(f, cache / f.name)
        if self.layout == "staged":
            pend = self.source / "support" / "pending_edits"
            m = json.loads((pend / "MANIFEST.json").read_text())
            for e in m["files"]:
                dst = self.bundle / e["target"]
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(pend / e["staged"], dst)
            for t in m["tools"]:
                shutil.copy2(self.source / m["pending_tools"] / t, self.bundle / "tools" / t)
        for name, target in self.linked.items():
            if not Path(target).is_dir():
                raise Leak(f"linked folder {target} missing")
            (self.ws / name).symlink_to(Path(target).resolve(), target_is_directory=True)
        self.tmp.mkdir()

    def env(self) -> dict:
        env = {k: v for k, v in os.environ.items() if not k.startswith("TASK_AUTHORING_")}
        env.update(PYTHONDONTWRITEBYTECODE="1", TMPDIR=str(self.tmp), **{ENV_FLAG: str(self.root)})
        return env

    def check_paths(self) -> dict:
        """Every write path the sandboxed tools compute, resolved; raises Leak if one is outside the sandbox."""
        r = subprocess.run([sys.executable, "-B", "-c", _PROBE, str(self.bundle), json.dumps(WRITE_PATHS)],
                           cwd=str(self.ws), env=self.env(), capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            raise Leak(f"path probe failed: {r.stderr.strip()[-400:]}")
        paths = json.loads(r.stdout)
        errors = {k: v for k, v in paths.items() if v.startswith("ERROR ")}
        if errors:
            raise Leak(f"path probe could not import: {errors}")
        outside = {k: str(Path(v).resolve()) for k, v in paths.items() if not _inside(Path(v), self.root)}
        if outside:
            raise Leak(f"write path(s) outside the sandbox: {outside}")
        return paths

    def check_linked(self) -> list:
        """`find <real linked folders> -newer <marker>`: every entry changed since the sandbox was made."""
        real = [str(Path(t).resolve()) for t in self.linked.values()]
        r = subprocess.run(["find", *real, "-newer", str(self.marker)], capture_output=True, text=True, timeout=1800)
        if r.returncode != 0:
            raise Leak(f"find failed: {r.stderr.strip()[-300:]}")
        return [ln for ln in r.stdout.splitlines() if ln.strip()
                and not any(f"/{x.strip('/')}" in ln for x in self.ignore_newer)]

    def run(self, argv: list, *, quiet: bool = False) -> int:
        """Run tools/<argv[0]> with argv[1:] inside the sandbox; raises Leak on an outside path or a linked write."""
        paths = self.check_paths()
        tool = self.bundle / "tools" / argv[0]
        if not tool.is_file():
            raise FileNotFoundError(f"{argv[0]} is not in the sandbox's tools/ ({self.layout} layout)")
        r = subprocess.run([sys.executable, "-B", str(tool), *argv[1:]], cwd=str(self.ws), env=self.env(),
                           capture_output=True, text=True, timeout=7200)
        if not quiet:
            sys.stdout.write(r.stdout)
            sys.stderr.write(r.stderr)
        changed = self.check_linked()
        if changed:
            raise Leak(f"{len(changed)} entr(y/ies) in the linked folders changed during the run: {changed[:5]}")
        self.last = {"paths": paths, "returncode": r.returncode, "stdout": r.stdout, "stderr": r.stderr}
        return r.returncode


def run_isolated(argv: list, layout: str = "live", source: Path = BUNDLE, quiet: bool = False) -> int:
    """For a self-test called outside a sandbox: rerun it inside one. Returns its exit code, or 3 on a leak."""
    try:
        with Sandbox(layout, source) as sb:
            print(f"[selftest_sandbox] {' '.join(argv)} in {sb.root.relative_to(source)} ({layout} layout)", flush=True)
            return sb.run(argv, quiet=quiet)
    except Leak as exc:
        print(f"[selftest_sandbox] LEAK: {exc}", file=sys.stderr)
        return 3


def run_suite(layout: str, source: Path = BUNDLE) -> int:
    worst = 0
    try:
        with Sandbox(layout, source) as sb:
            print(f"[selftest_sandbox] suite move in {sb.root.relative_to(source)} ({layout} layout); linked: "
                  f"{', '.join(sb.linked)}; seeded cache files: {len(list((sb.bundle / CACHE).glob('*.json')))}",
                  flush=True)
            for argv in SUITE_MOVE:
                try:
                    rc = sb.run(list(argv), quiet=True)
                except FileNotFoundError as exc:
                    print(f"  FAIL {' '.join(argv)}: {exc}", flush=True)
                    worst = worst or 1
                    continue
                tail = (sb.last["stdout"].strip().splitlines() or sb.last["stderr"].strip().splitlines() or [""])[-1]
                print(f"  {'ok  ' if rc == 0 else 'FAIL'} {' '.join(argv)} (exit {rc}): {tail[:220]}", flush=True)
                if rc != 0:
                    sys.stdout.write(sb.last["stdout"][-3000:] + sb.last["stderr"][-3000:])
                worst = worst or rc
            print(f"  paths asserted inside the sandbox before every command: {sorted(sb.last['paths'])}")
            print("  linked folders unchanged after every command (find -newer marker: empty)")
    except Leak as exc:
        print(f"[selftest_sandbox] LEAK: {exc}", file=sys.stderr)
        return 3
    return worst


# ------------------------------------------------------------------ self-test (a fake bundle, fake linked folders)

def _self_test() -> None:
    with scratch_tmp("selftest_sandbox_") as tmp:
        t = Path(tmp)
        assert _inside(t, SCRATCH), "scratch_tmp must stay under the scratch root"
        src = t / "src" / "Task_Authoring"
        (src / "tools").mkdir(parents=True)
        (src / "setup").mkdir()
        (src / CACHE).mkdir(parents=True)
        (src / CACHE / "pv_x.json").write_text('{"real": 1}\n')
        (src / "support" / "pending_edits").mkdir(parents=True)
        (src / "support" / "pending_tools").mkdir(parents=True)
        (src / "support" / "pending_tools" / "newtool.py").write_text("print('new tool')\n")
        (src / "support" / "pending_edits" / "MANIFEST.json").write_text(json.dumps(
            {"pending_tools": "support/pending_tools", "tools": ["newtool.py"], "files": []}))
        shutil.copy2(Path(__file__).resolve(), src / "tools" / "selftest_sandbox.py")
        (src / "tools" / "difficulty_stats.py").write_text("print('marker')\n")
        tools = {
            "ok.py": "import sys; print('fine'); sys.exit(0)",
            "fails.py": "import sys; sys.exit(5)",
            "linked_write.py": "from pathlib import Path; Path('Evals/leak.txt').write_text('x')",
            "cache_write.py": ("from pathlib import Path\np = Path('Task_Authoring/support/local_search/cache/pv_x.json')\n"
                               "assert p.is_file() and not p.is_symlink()\np.write_text('{\"rebuilt\": 1}')"),
            "tmp_write.py": "import tempfile, os; d = tempfile.mkdtemp(); print(d)",
            "flag.py": ("import os, sys; sys.path.insert(0, 'Task_Authoring/tools'); import selftest_sandbox as s; "
                        "print(s.in_sandbox())"),
        }
        for name, code in tools.items():
            (src / "tools" / name).write_text(code + "\n")
        data = t / "data"
        (data / "Evals").mkdir(parents=True)
        (data / "Evals" / "keep.txt").write_text("read-only\n")
        linked = {"Evals": data / "Evals"}
        real_cache = (src / CACHE / "pv_x.json").read_text()
        n = 0
        with Sandbox("live", src, linked) as sb:
            assert _inside(sb.root, src / "support" / "scratch") and sb.bundle.is_dir()
            assert (sb.ws / "Evals").is_symlink() and (sb.bundle / CACHE / "pv_x.json").is_file()
            assert sb.run(["ok.py"], quiet=True) == 0 and sb.run(["fails.py"], quiet=True) == 5
            n += 1
            # a write through a linked folder is a leak, found by find -newer
            try:
                sb.run(["linked_write.py"], quiet=True)
            except Leak as exc:
                assert "leak.txt" in str(exc), exc
            else:
                raise AssertionError("a write through a linked folder was not reported")
            (data / "Evals" / "leak.txt").unlink()
            n += 1
        with Sandbox("live", src, linked) as sb:
            # a cache rebuild inside the sandbox never reaches the real cache
            assert sb.run(["cache_write.py"], quiet=True) == 0
            assert (src / CACHE / "pv_x.json").read_text() == real_cache
            assert "rebuilt" in (sb.bundle / CACHE / "pv_x.json").read_text()
            n += 1
            # tempfile without dir= stays inside the sandbox (TMPDIR)
            assert sb.run(["tmp_write.py"], quiet=True) == 0 and _inside(Path(sb.last["stdout"].strip()), sb.root)
            n += 1
            # the sandbox flag is honoured only for a bundle inside the named sandbox
            assert sb.run(["flag.py"], quiet=True) == 0 and sb.last["stdout"].strip() == "True"
            n += 1
        old = os.environ.get(ENV_FLAG)
        os.environ[ENV_FLAG] = str(t / "elsewhere")
        try:
            assert not in_sandbox(src)                      # a stale variable never disables sandboxing
        finally:
            os.environ.pop(ENV_FLAG, None) if old is None else os.environ.__setitem__(ENV_FLAG, old)
        n += 1
        # a write path that resolves outside the sandbox (through a symlink) is a leak
        with Sandbox("live", src, linked) as sb:
            (sb.bundle / "tools" / "persona_view.py").write_text(
                "from pathlib import Path\nCACHE = Path('Evals') / 'cache'\nGMAIL_INDEX = CACHE / 'x.json'\n")
            try:
                sb.check_paths()
            except Leak as exc:
                assert "persona_view.CACHE" in str(exc), exc
            else:
                raise AssertionError("a write path outside the sandbox was not reported")
            n += 1
        # the staged layout copies the pending tools into tools/
        with Sandbox("staged", src, linked) as sb:
            assert (sb.bundle / "tools" / "newtool.py").read_text() == "print('new tool')\n"
            n += 1
        # local_search: the helpers' root is the real workspace, their copies and cache stay inside the sandbox
        ls_src = ('from pathlib import Path\nBUNDLE = Path(__file__).resolve().parent.parent          # Task_Authoring/\n'
                  'WORKSPACE = BUNDLE.parent                                 # the workspace root (holds Evals/)\n'
                  'LOCAL = BUNDLE / "support" / "local_search"\nTOOLS = LOCAL / "tools"\n'
                  'CACHE_REL = f"{BUNDLE.name}/support/local_search/cache"\n')
        (src / "setup" / "local_search.py").write_text(ls_src)
        with Sandbox("live", src, linked) as sb:
            paths = sb.check_paths()
            assert _inside(Path(paths["local_search.WORKSPACE/CACHE_REL"]), sb.root), paths
            assert _inside(Path(paths["local_search.TOOLS"]), sb.root), paths
            r = subprocess.run([sys.executable, "-B", "-c", "import sys; sys.path.insert(0, sys.argv[1]); import local_search as l; "
                                "print(l.WORKSPACE)", str(sb.bundle / "setup")], capture_output=True, text=True, env=sb.env())
            assert Path(r.stdout.strip()) == src.parent.resolve(), r
            n += 1
        # a local_search.py whose anchors moved is never run unpatched: the sandbox refuses to build
        (src / "setup" / "local_search.py").write_text(ls_src.replace('f"{BUNDLE.name}/support/local_search/cache"',
                                                                      '"Task_Authoring/support/local_search/cache"'))
        try:
            with Sandbox("live", src, linked):
                pass
        except Leak as exc:
            assert "patch anchor" in str(exc), exc
        else:
            raise AssertionError("a local_search.py without its patch anchor was accepted")
        n += 1
        assert not list((src / "support" / "scratch").iterdir()), "every sandbox must be removed"
        assert (data / "Evals" / "keep.txt").read_text() == "read-only\n"
    print(f"self-test: ok ({n} cases: scratch root, a write through a linked folder reported (find -newer), a cache "
          f"rebuild kept inside, tempfile without dir= kept inside, sandbox flag scoped, an outside write path reported, "
          f"staged layout, local_search rooted in the real workspace with its cache inside, a moved patch anchor "
          f"refused, every sandbox removed)")


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="selftest_sandbox.py", description="see the module docstring")
    ap.add_argument("--layout", choices=("live", "staged"), default="live")
    ap.add_argument("--suite", choices=("move",))
    ap.add_argument("--keep", action="store_true", help="keep the sandbox folder (debugging)")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("command", nargs=argparse.REMAINDER)
    a = ap.parse_args(argv)
    if a.self_test:
        _self_test()
        return 0
    if a.suite:
        return run_suite(a.layout)
    cmd = a.command[1:] if a.command[:1] == ["--"] else a.command
    if not cmd:
        ap.print_usage(sys.stderr)
        return 2
    try:
        with Sandbox(a.layout, keep=a.keep) as sb:
            print(f"[selftest_sandbox] {' '.join(cmd)} in {sb.root.relative_to(BUNDLE)} ({a.layout} layout)", flush=True)
            return sb.run(cmd)
    except Leak as exc:
        print(f"[selftest_sandbox] LEAK: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

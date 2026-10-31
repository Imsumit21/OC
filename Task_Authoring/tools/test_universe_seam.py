#!/usr/bin/env python3
"""Seam tests for the two-universe runtime: patched helper copies and runtime_context.

Every test builds a throw-away workspace under Task_Authoring/support/scratch/, copies the
real Evals/tools/*.py (and the one schema the linter reads) into it, and points
local_search.BUNDLE/WORKSPACE at it. Nothing under Evals/ is written.

  python3 -B -m unittest test_universe_seam -v     (from Task_Authoring/tools)
"""
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WORKSPACE = BUNDLE.parent
SCRATCH = BUNDLE / "support" / "scratch"
# Both are git-ignored, so a fresh clone has neither; the checks that need them are skipped there.
EVAL_INPUTS = WORKSPACE / "Evals" / "task_inputs"
DEFAULT_ASSIGNMENT = BUNDLE / "task_inputs" / "00_Assigments.md"
needs_local_inputs = unittest.skipUnless(EVAL_INPUTS.is_dir() and DEFAULT_ASSIGNMENT.is_file(),
                                         "needs Evals/task_inputs/ and Task_Authoring/task_inputs/ (git-ignored)")
CTX_A = hashlib.sha256(b"runtime-context-a").hexdigest()
CTX_B = hashlib.sha256(b"runtime-context-b").hexdigest()
CTX_C = hashlib.sha256(b"runtime-context-c").hexdigest()
FINGERPRINT = "f" * 64

SQL = """\
insert into linear.linear_issues
  (id, title, priority, labels_json, links_json, relations_json, is_archived,
   created_at, updated_at, state_history_json)
values
  ('LIN-9001', 'Seam check', 2, '[]', '[]', '[]', false,
   '2025-09-30 14:12:09+00:00', '2025-09-30T21:12:09Z', '[]');

insert into slack.slack_messages
  (id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message,
   reactions_json, files_json, attachments_json, created_at, metadata_json, text_fts)
values
  ('SM-9001', '1727694000.000100', 'C-SEAM', 'message', 'seam check', 0, 0, false,
   '[]', '[]', '[]', '2025-10-01T08:00:00Z', '{}', 'seam check');
"""

ENV_KEYS = ("TASK_AUTHORING_CONTEXT_HASH", "TASK_AUTHORING_UNIVERSE", "TASK_AUTHORING_TASK_DIR",
            "TASK_AUTHORING_LEGACY_V2")


def load_module(path: Path):
    """Import a file by path without writing bytecode next to it."""
    spec = importlib.util.spec_from_file_location("seam_" + path.stem, path)
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def meta(**overrides):
    value = {"universe": "normal", "clock": "2026-02-14T00:00:00Z",
             "source_fingerprint": FINGERPRINT, "build": "per-universe-v1"}
    value.update(overrides)
    return value


def context_for(universe="normal", status="ready", kb_status="unavailable", **source):
    clock = "2025-10-01T07:00:00Z" if universe == "synthcut" else "2026-02-14T00:00:00Z"
    freeze = "2025-10-01T00:00:00Z" if universe == "synthcut" else "2026-02-14T00:00:00Z"
    return {"context_hash": CTX_A, "freeze_utc": freeze,
            "universe": {"key": universe, "date": freeze[:10], "clock_utc": clock},
            "source": {"status": status, "reason": "No KB is bound to the selected universe",
                       "mode": "universe", "universe": universe, "manifest": None,
                       "paths": {}, "fingerprint": FINGERPRINT, "data_clock": clock,
                       "assigned_freeze": freeze, "kb_status": kb_status, "kb_path": None,
                       "kb_output_path": None, **source}}


class UniverseSeam(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        cls.sandbox = Path(tempfile.mkdtemp(dir=SCRATCH, prefix="universe-tasks-"))
        task_context = load_module(HERE / "task_context.py")
        # A self-contained platform paste: never the live task folder (absent on a fresh clone, or another task).
        assignment = ("🏢 Business Function\nExecutive\n🧑 Persona\nFrederick Stone\nRole: Co-founder\n"
                      "🎯 Competency\nCorporate Ops\n🛠️ Task Skill\nAuthoring\n📋 Task Type\nlong-horizon\n"
                      "🎚️ Difficulty Mode\neasy\n📅 Universe Date\nFebruary 14, 2026 00:00\n")
        october = assignment.replace("February 14, 2026 00:00", "October 1, 2025 00:00")
        cls.task_dirs, cls.hashes = {}, {}
        for key, text in (("normal", assignment), ("synthcut", october)):
            folder = cls.sandbox / key
            folder.mkdir()
            (folder / "00_Assigments.md").write_text(text)
            context = task_context.load_context(folder)
            assert (context.get("universe") or {}).get("key") == key, context
            cls.task_dirs[key] = str(folder)
            cls.hashes[key] = context["context_hash"]

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.sandbox, ignore_errors=True)

    def setUp(self):
        self.root = Path(tempfile.mkdtemp(dir=SCRATCH, prefix="universe-seam-"))
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        self.local = self.root / "Task_Authoring"
        self.local.mkdir()
        source = WORKSPACE / "Evals" / "tools"
        target = self.root / "Evals" / "tools"
        target.mkdir(parents=True)
        for tool in source.glob("*.py"):
            shutil.copy2(tool, target / tool.name)
        schema = self.root / "Evals" / "references" / "schema"
        schema.mkdir(parents=True)
        shutil.copy2(WORKSPACE / "Evals" / "references" / "schema" / "injection.json",
                     schema / "injection.json")
        self.builder = load_module(BUNDLE / "setup" / "local_search.py")
        self.builder.BUNDLE = self.local
        self.builder.WORKSPACE = self.root

    # ---------------------------------------------------------------- helpers
    @contextlib.contextmanager
    def env(self, **values):
        saved = {key: os.environ.get(key) for key in ENV_KEYS}
        try:
            for key in ENV_KEYS:
                os.environ.pop(key, None)
            for key, value in values.items():
                if value:
                    os.environ[key] = value
            yield
        finally:
            for key, value in saved.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value

    def build(self, universe=None, context_hash=None, task_dir=None):
        if task_dir is None and universe:
            task_dir = self.task_dirs[universe]
        with self.env(TASK_AUTHORING_CONTEXT_HASH=context_hash, TASK_AUTHORING_UNIVERSE=universe,
                      TASK_AUTHORING_TASK_DIR=task_dir):
            return self.builder.build()

    def context_dir(self, context_hash) -> Path:
        return self.local / "support" / "local_search" / "contexts" / context_hash[:20]

    def default_dir(self) -> Path:
        return self.local / "support" / "local_search"

    def tool(self, name, context_hash):
        return load_module(self.context_dir(context_hash) / "tools" / f"{name}.py")

    def default_tool(self, name):
        return load_module(self.default_dir() / "tools" / f"{name}.py")

    def saved_index(self, context_hash) -> dict:
        return json.loads((self.context_dir(context_hash) / "universe" / "inputs.json").read_text())

    # ------------------------------------------------------------------ tests
    def test_selection_follows_the_activated_context(self):
        for key in ("synthcut", "normal"):
            with self.subTest(universe=key):
                context_hash = self.hashes[key]
                result = self.build(key, context_hash)
                self.assertEqual(result["universe"], key)
                self.assertEqual(result["universe_index"],
                                 f"Task_Authoring/support/local_search/contexts/{context_hash[:20]}/universe/inputs.json")
                helper = self.tool("hg_universe", context_hash)
                self.assertEqual(helper.selected(self.root), key)
                date_file = self.context_dir(context_hash) / "universe" / "02_Universe_Date.txt"
                self.assertEqual(date_file.read_text(), helper.UNIVERSES[key]["date"] + "\n")
                entry = self.saved_index(context_hash)["inputs"]["universe"]
                self.assertEqual(entry["state"], "saved")
                self.assertEqual(entry["files"][0]["path"], date_file.relative_to(self.root).as_posix())
                self.assertEqual(entry["files"][0]["bytes"], date_file.stat().st_size)
                self.assertEqual(entry["files"][0]["sha256"],
                                 hashlib.sha256(date_file.read_bytes()).hexdigest())

    def test_eval_bundle_saved_date_is_ignored(self):
        bundle_inputs = self.root / "Evals" / "task_inputs"
        bundle_inputs.mkdir(parents=True)
        raw = b"2026-02-14\n"
        (bundle_inputs / "02_Universe_Date.txt").write_bytes(raw)
        (bundle_inputs / "inputs.json").write_text(json.dumps({
            "format_version": 1, "revision": 1, "inputs": {"universe": {
                "state": "saved", "revision": 1, "files": [{
                    "filename": "02_Universe_Date.txt", "path": "Evals/task_inputs/02_Universe_Date.txt",
                    "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}]}}}, indent=2) + "\n")
        self.build("synthcut", self.hashes["synthcut"])
        self.assertEqual(self.tool("hg_universe", self.hashes["synthcut"]).selected(self.root), "synthcut")
        self.build()
        default = self.default_tool("hg_universe")
        with self.assertRaises(default.UniverseNotSelected):
            default.selected(self.root)

    def test_universe_without_an_activated_context_is_an_error(self):
        with self.assertRaises(SystemExit) as caught:
            self.build("normal")
        self.assertIn("universe selection requires an activated task context", str(caught.exception))
        self.assertFalse(self.default_dir().exists())

    def test_forged_context_cannot_publish_an_index(self):
        with self.assertRaises(SystemExit) as caught:
            self.build("normal", "0" * 64, task_dir=self.task_dirs["synthcut"])
        self.assertIn("universe selection", str(caught.exception))
        self.assertFalse((self.local / "support" / "local_search").exists())
        with self.assertRaises(SystemExit) as caught:
            self.build("normal", self.hashes["synthcut"], task_dir=self.task_dirs["synthcut"])
        self.assertIn("hash/universe mismatch", str(caught.exception))
        self.assertFalse((self.local / "support" / "local_search").exists())

    def test_missing_index_anchor_writes_nothing(self):
        anchor = self.root / "Evals" / "tools" / "hg_universe.py"
        anchor.write_text(anchor.read_text().replace(
            "INDEX = Path('Evals/task_inputs/inputs.json')", "INDEX = Path('Evals/references/inputs.json')"))
        with self.assertRaises(SystemExit) as caught:
            self.build("normal", self.hashes["normal"])
        self.assertIn("hg_universe.py", str(caught.exception))
        self.assertFalse(self.default_dir().exists())
        self.assertFalse((self.local / "support" / "local_search" / "contexts").exists())

    def test_no_copy_reads_eval_task_inputs(self):
        for universe, context_hash in (("synthcut", self.hashes["synthcut"]), (None, None)):
            with self.subTest(universe=universe):
                self.build(universe, context_hash)
                tools = (self.context_dir(context_hash) / "tools") if universe else (self.default_dir() / "tools")
                offenders = sorted(path.name for path in tools.glob("*.py") if "Evals/task_inputs" in path.read_text())
                self.assertEqual(offenders, [])
        self.assertNotIn("Evals/task_inputs",
                         (self.context_dir(self.hashes["synthcut"]) / "tools" / "hg_injection_lint.py").read_text())
        self.assertIn("NO_EVAL_TASK_INPUTS",
                      (self.context_dir(self.hashes["synthcut"]) / "tools" / "hg_injection_lint.py").read_text())

    def test_alternating_contexts_keep_separate_indexes(self):
        self.build("normal", self.hashes["normal"])
        self.build("synthcut", self.hashes["synthcut"])
        self.build()
        self.assertEqual(self.tool("hg_universe", self.hashes["normal"]).selected(self.root), "normal")
        self.assertEqual(self.tool("hg_universe", self.hashes["synthcut"]).selected(self.root), "synthcut")
        self.assertFalse((self.default_dir() / "universe").exists())
        default = self.default_tool("hg_universe")
        with self.assertRaises(default.UniverseNotSelected):
            default.selected(self.root)

    def test_rebuild_is_idempotent(self):
        self.assertTrue(self.build("normal", self.hashes["normal"])["changes"])
        before = self.saved_index(self.hashes["normal"])
        result = self.build("normal", self.hashes["normal"])
        self.assertEqual(result["changes"], [])
        self.assertEqual(self.saved_index(self.hashes["normal"]), before)

    @needs_local_inputs
    def test_hg_refuses_eval_task_input_paths(self):
        inputs = WORKSPACE / "Evals" / "task_inputs"
        cases = (["rubric-lint", str(inputs / "09_Rubrics.json")],
                 ["lint", "--no-base", "--sql", str(inputs / "01_Universe_Inject.sql")])
        for args in cases:
            with self.subTest(command=args[0]):
                done = subprocess.run([sys.executable, "-B", str(BUNDLE / "tools" / "hg.py"), *args],
                                      cwd=str(WORKSPACE), capture_output=True, text=True)
                self.assertEqual(done.returncode, 2, (args, done.stdout, done.stderr))
                self.assertIn("Evals/task_inputs", done.stderr)

    def run_hg(self, args, task_dir, cwd=WORKSPACE):
        env = {k: v for k, v in os.environ.items() if not k.startswith("TASK_AUTHORING_")}
        env["TASK_AUTHORING_TASK_DIR"] = str(task_dir)
        return subprocess.run([sys.executable, "-B", str(BUNDLE / "tools" / "hg.py"), *args],
                              cwd=str(cwd), capture_output=True, text=True, env=env)

    @needs_local_inputs
    def test_hg_refuses_dash_prefixed_equals_values(self):
        # Red-team round 3: '--sql=-leak.sql' where '-leak.sql' links into Evals/task_inputs.
        work = self.root / "dash"
        work.mkdir()
        (work / "-leak.sql").symlink_to(WORKSPACE / "Evals" / "task_inputs" / "inputs.json")
        done = self.run_hg(["lint", "--no-base", "--sql=-leak.sql"], self.task_dirs["normal"], cwd=work)
        self.assertEqual(done.returncode, 2, (done.stdout, done.stderr))
        self.assertIn("Evals/task_inputs", done.stderr)

    def test_legacy_refuses_symlinked_or_nested_v3_inputs(self):
        # Verify-gate red team: lexical parent/grandparent inference missed a symlinked or deeply nested V3 input.
        runtime = load_module(HERE / "runtime_context.py")
        task = Path(self.task_dirs["synthcut"])
        sql = task / "01_Universe_Inject.sql"
        sql.write_text("-- Are you planning to inject? Yes\n")
        link = self.root / "elsewhere" / "v3.sql"
        link.parent.mkdir()
        link.symlink_to(sql)
        nested = task / "Working_Files" / "probes" / "seed.sql"
        nested.parent.mkdir(parents=True, exist_ok=True)
        nested.write_text("-- probe\n")
        for path in (link, nested):
            with self.subTest(path=path.name), self.env(), \
                    mock.patch.object(sys, "argv", ["sql_lint.py", "--legacy-v2", str(path)]):
                with self.assertRaises(runtime.ContextError) as caught:
                    runtime.cli_entry({})
                self.assertIn("legacy V2 mode cannot run on a V3 assignment", str(caught.exception))

    def test_legacy_refusal_sees_every_owner_of_every_path(self):
        # Verify-gate round 2: a nested V2 marker, an upper-case suffix, an extensionless alias or a V2 env dir
        # must not hide the V3 task that owns an input.
        runtime = load_module(HERE / "runtime_context.py")
        task = Path(self.task_dirs["synthcut"])
        v2 = self.root / "archived-v2"
        v2.mkdir()
        (v2 / "00_Assigments.md").write_text("spec_version: V2\n")
        probes = task / "Working_Files" / "probes-v2"
        probes.mkdir(parents=True, exist_ok=True)
        (probes / "00_Assigments.md").write_text("spec_version: V2\n")
        (probes / "seed.sql").write_text("-- probe\n")
        (task / "Working_Files" / "seed.SQL").write_text("-- probe\n")
        alias = self.root / "alias"
        alias.symlink_to(task / "Working_Files" / "seed.SQL")
        cases = {"nested V2 marker": [str(probes / "seed.sql")],
                 "upper-case suffix": ["--sql", str(task / "Working_Files" / "seed.SQL")],
                 "extensionless alias": [str(alias)]}
        for name, args in cases.items():
            with self.subTest(case=name), self.env(TASK_AUTHORING_TASK_DIR=str(v2)), \
                    mock.patch.object(sys, "argv", ["sql_lint.py", "--legacy-v2", *args]):
                with self.assertRaises(runtime.ContextError) as caught:
                    runtime.cli_entry({})
                self.assertIn("legacy V2 mode cannot run on a V3 assignment", str(caught.exception))
        # No task named anywhere: the default task (a V3 assignment here) is what a tool would fall back to.
        if DEFAULT_ASSIGNMENT.is_file():
            with self.env(), mock.patch.object(sys, "argv", ["sql_lint.py", "--legacy-v2"]):
                with self.assertRaises(runtime.ContextError):
                    runtime.cli_entry({})
        with self.env(), mock.patch.object(sys, "argv", ["sql_lint.py", "--self-test"]):
            self.assertIsNone(runtime.cli_entry({}))   # self-tests keep their archived fixtures
        # Positive control: a genuinely standalone V2 task stays usable in legacy mode.
        (v2 / "01_Universe_Inject.sql").write_text("-- archived\n")
        with self.env(), mock.patch.object(sys, "argv", ["sql_lint.py", "--legacy-v2", "--task-dir", str(v2),
                                                         str(v2 / "01_Universe_Inject.sql")]):
            self.assertIsNone(runtime.cli_entry({}))

    def test_build_replaces_a_symlinked_tool_copy_instead_of_writing_through_it(self):
        evals_copy = self.root / "Evals" / "tools" / "hg_universe.py"
        before = evals_copy.read_bytes()
        tools = self.default_dir() / "tools"
        tools.mkdir(parents=True)
        (tools / "hg_universe.py").symlink_to(evals_copy)
        self.build()
        self.assertEqual(evals_copy.read_bytes(), before)
        self.assertFalse((tools / "hg_universe.py").is_symlink())
        self.assertIn("NO_EVAL_TASK_INPUTS", (tools / "hg_universe.py").read_text())

    def test_atomic_install_never_opens_a_planted_temp_path(self):
        # Verify-gate round 3: a predictable temp name pre-planted as a symlink or hard link must not be written.
        protected = self.root / "Evals" / "tools" / "hg_universe.py"
        before = protected.read_bytes()
        dst = self.default_dir() / "tools" / "hg_universe.py"
        dst.parent.mkdir(parents=True)
        for name in (f"hg_universe.py.{os.getpid()}.tmp", "hg_universe.py.tmp"):
            (dst.parent / name).symlink_to(protected)
        os.link(protected, dst.parent / f"hg_universe.py.{os.getpid() + 1}.tmp")
        self.builder._atomic(dst, b"# installed\n")
        self.assertEqual(protected.read_bytes(), before)
        self.assertFalse(dst.is_symlink())
        self.assertEqual(dst.read_bytes(), b"# installed\n")
        self.assertEqual(dst.stat().st_nlink, 1)

    def test_context_write_never_opens_a_planted_temp_path(self):
        tc = load_module(HERE / "task_context.py")
        protected = self.root / "protected.json"
        protected.write_text('{"keep": true}\n')
        task = self.root / "tmp-task"
        (task / "Working_Files").mkdir(parents=True)
        shutil.copy2(Path(self.task_dirs["normal"]) / "00_Assigments.md", task / "00_Assigments.md")
        (task / "Working_Files" / f"00_Task_Context.json.{os.getpid()}.tmp").symlink_to(protected)
        with open(os.devnull, "w") as quiet, contextlib.redirect_stdout(quiet), contextlib.redirect_stderr(quiet):
            self.assertEqual(tc.main(["--task-dir", str(task), "--write"]), 0)
        self.assertEqual(protected.read_text(), '{"keep": true}\n')
        written = task / "Working_Files" / "00_Task_Context.json"
        self.assertFalse(written.is_symlink())
        self.assertEqual(json.loads(written.read_text())["universe"]["key"], "normal")

    def test_legacy_refusal_covers_dash_files_and_nested_named_folders(self):
        runtime = load_module(HERE / "runtime_context.py")
        task = Path(self.task_dirs["synthcut"])
        v2 = self.root / "standalone-v2"
        v2.mkdir()
        (v2 / "00_Assigments.md").write_text("spec_version: V2\n")
        (task / "-").write_text("-- a file literally named '-'\n")
        nested = task / "Working_Files" / "archived-v2"
        nested.mkdir(parents=True, exist_ok=True)
        (nested / "00_Assigments.md").write_text("spec_version: V2\n")
        cwd = os.getcwd()
        self.addCleanup(os.chdir, cwd)
        os.chdir(task)
        cases = {"--sql -": ({"TASK_AUTHORING_TASK_DIR": str(v2)}, ["--sql", "-"]),
                 "--sql=-": ({"TASK_AUTHORING_TASK_DIR": str(v2)}, ["--sql=-"]),
                 "--task-dir nested V2": ({}, ["--task-dir", str(nested)]),
                 "--task-dir= nested V2": ({}, [f"--task-dir={nested}"]),
                 "env nested V2": ({"TASK_AUTHORING_TASK_DIR": str(nested)}, [])}
        for name, (env, args) in cases.items():
            with self.subTest(case=name), self.env(**env), \
                    mock.patch.object(sys, "argv", ["sql_lint.py", "--legacy-v2", *args]):
                with self.assertRaises(runtime.ContextError) as caught:
                    runtime.cli_entry({})
                self.assertIn("legacy V2 mode cannot run on a V3 assignment", str(caught.exception))
        with self.env(TASK_AUTHORING_TASK_DIR=str(nested), TASK_AUTHORING_LEGACY_V2="1"):
            with self.assertRaises(runtime.ContextError):
                runtime.ensure_active({}, require_source=False)

    @needs_local_inputs
    def test_hg_refuses_a_dash_named_link_into_eval_inputs(self):
        work = self.root / "dash-plain"
        work.mkdir()
        (work / "-").symlink_to(WORKSPACE / "Evals" / "task_inputs" / "inputs.json")
        done = self.run_hg(["lint", "--no-base", "--sql", "-"], self.task_dirs["normal"], cwd=work)
        self.assertEqual(done.returncode, 2, (done.stdout, done.stderr))
        self.assertIn("Evals/task_inputs", done.stderr)

    def test_build_refuses_a_symlinked_output_ancestor(self):
        # Verify-gate red team: support/local_search linked into Evals/ must not receive copies or an index.
        support = self.local / "support"
        support.mkdir(parents=True, exist_ok=True)
        evals = self.root / "Evals"
        before = {p.name: p.read_bytes() for p in (evals / "tools").glob("*.py")}
        (support / "local_search").symlink_to(evals, target_is_directory=True)
        with self.env(), self.assertRaises(SystemExit) as caught:
            self.builder.build()
        self.assertIn("resolves outside Task_Authoring", str(caught.exception))
        self.assertEqual(before, {p.name: p.read_bytes() for p in (evals / "tools").glob("*.py")})
        self.assertFalse((evals / "cache").exists() or (evals / "universe").exists())

    def test_within_detects_hard_links_into_a_protected_root(self):
        tc = load_module(HERE / "task_context.py")
        protected = self.root / "protected"
        protected.mkdir()
        (protected / "saved.json").write_text("{}")
        os.link(protected / "saved.json", self.root / "alias.json")
        self.assertTrue(tc.within(self.root / "alias.json", protected))
        (self.root / "plain.json").write_text("{}")
        self.assertFalse(tc.within(self.root / "plain.json", protected))

    def test_task_dir_conflicts_and_masked_legacy_inputs_are_refused(self):
        runtime = load_module(HERE / "runtime_context.py")
        with self.env(), mock.patch.object(sys, "argv", [
                "base_check.py", f"--task-dir={self.task_dirs['normal']}", f"--task-dir={self.task_dirs['synthcut']}"]):
            with self.assertRaises(runtime.ContextError) as caught:
                runtime.cli_entry({})
            self.assertIn("more than once", str(caught.exception))
        # A V2 folder's manifest listed first must not mask the V3 task that owns the SQL.
        v2 = self.root / "v2-task"
        v2.mkdir()
        (v2 / "00_Assigments.md").write_text("spec_version: V2\n")
        (v2 / "manifest.json").write_text("{}")
        sql = Path(self.task_dirs["synthcut"]) / "01_Universe_Inject.sql"
        sql.write_text("-- Are you planning to inject? Yes\n")
        with self.env(), mock.patch.object(sys, "argv", [
                "base_check.py", "--legacy-v2", "--manifest", str(v2 / "manifest.json"), str(sql)]):
            os.environ.pop("TASK_AUTHORING_TASK_DIR", None)
            with self.assertRaises(runtime.ContextError) as caught:
                runtime.cli_entry({})
            self.assertIn("legacy V2 mode cannot run on a V3 assignment", str(caught.exception))

    def test_context_write_never_writes_through_a_hard_link(self):
        tc = load_module(HERE / "task_context.py")
        tc.WORKSPACE = self.root                     # the fake workspace's Evals/ stands in for the real one
        protected = self.root / "Evals" / "task_inputs"
        protected.mkdir(parents=True)
        (protected / "inputs.json").write_text('{"keep": true}\n')
        task = self.root / "hl-task"
        (task / "Working_Files").mkdir(parents=True)
        shutil.copy2(Path(self.task_dirs["normal"]) / "00_Assigments.md", task / "00_Assigments.md")
        os.link(protected / "inputs.json", task / "Working_Files" / "00_Task_Context.json")
        with open(os.devnull, "w") as quiet, contextlib.redirect_stdout(quiet), contextlib.redirect_stderr(quiet):
            tc.main(["--task-dir", str(task), "--write"])
        self.assertEqual((protected / "inputs.json").read_text(), '{"keep": true}\n')

    def test_gradeable_report_out_stays_inside_the_bundle(self):
        surface = self.root / "surface.json"
        surface.write_text('{"kind": "GRADABLE_SURFACE", "slots": []}')
        outside = Path(tempfile.mkdtemp(prefix="gs-out-")) / "probe.json"
        self.addCleanup(shutil.rmtree, outside.parent, ignore_errors=True)
        env = {k: v for k, v in os.environ.items() if not k.startswith("TASK_AUTHORING_")}
        done = subprocess.run([sys.executable, "-B", str(HERE / "gradable_surface.py"), "gradeable-report",
                               str(surface), "--out", str(outside)], cwd=str(WORKSPACE), capture_output=True,
                              text=True, env=env)
        self.assertNotEqual(done.returncode, 0, (done.stdout, done.stderr))
        self.assertFalse(outside.exists())

    @needs_local_inputs
    def test_hg_refuses_equals_form_case_variants_and_symlinked_default_sql(self):
        # Red-team re-attack: the guard compares file identity on the final arguments.
        inputs = WORKSPACE / "Evals" / "task_inputs"
        cases = [["lint", "--no-base", f"--sql={inputs / '01_Universe_Inject.sql'}"]]
        if (WORKSPACE / "eVaLs").exists():  # case-insensitive filesystem (macOS default)
            cases.append(["rubric-lint", str(WORKSPACE / "eVaLs" / "tAsK_iNpUtS" / "09_Rubrics.json")])
        for args in cases:
            with self.subTest(args=args[-1]):
                done = self.run_hg(args, self.task_dirs["normal"])
                self.assertEqual(done.returncode, 2, (args, done.stdout, done.stderr))
                self.assertIn("Evals/task_inputs", done.stderr)
        task = self.root / "linked-task"
        task.mkdir()
        shutil.copy2(Path(self.task_dirs["normal"]) / "00_Assigments.md", task / "00_Assigments.md")
        (task / "01_Universe_Inject.sql").symlink_to(inputs / "inputs.json")
        done = self.run_hg(["lint", "--no-base"], task)  # the default --sql is checked after insertion
        self.assertEqual(done.returncode, 2, (done.stdout, done.stderr))
        self.assertIn("Evals/task_inputs", done.stderr)

    def test_legacy_refuses_equals_form_task_dir(self):
        runtime = load_module(HERE / "runtime_context.py")
        with self.env(), mock.patch.object(
                sys, "argv", ["base_check.py", "--legacy-v2", f"--task-dir={self.task_dirs['synthcut']}"]):
            with self.assertRaises(runtime.ContextError) as caught:
                runtime.cli_entry({})
            self.assertIn("legacy V2 mode cannot run on a V3 assignment", str(caught.exception))

    def test_task_context_never_targets_read_only_folders(self):
        tc = load_module(HERE / "task_context.py")
        with self.assertRaises(tc.ContextError) as caught:  # the eval bundle's inputs as a task directory
            tc.load_context(WORKSPACE / "Evals" / "task_inputs")
        self.assertIn("read-only Evals/", str(caught.exception))
        # A Working_Files symlink into a read-only folder: refused before anything is written.
        tc.WORKSPACE = self.root
        fake_inputs = self.root / "Evals" / "task_inputs"
        fake_inputs.mkdir(parents=True)
        task = self.root / "task"
        task.mkdir()
        shutil.copy2(Path(self.task_dirs["normal"]) / "00_Assigments.md", task / "00_Assigments.md")
        (task / "Working_Files").symlink_to(fake_inputs, target_is_directory=True)
        with open(os.devnull, "w") as quiet, contextlib.redirect_stdout(quiet), contextlib.redirect_stderr(quiet):
            self.assertEqual(tc.main(["--task-dir", str(task), "--write"]), 2)
        self.assertEqual(list(fake_inputs.iterdir()), [])

    def test_legacy_mode_refuses_a_v3_assignment(self):
        runtime = load_module(HERE / "runtime_context.py")
        task_dir = self.task_dirs["normal"]
        with self.env(), mock.patch.object(sys, "argv", ["entity.py", "--legacy-v2", "--task-dir", task_dir]):
            with self.assertRaises(runtime.ContextError) as caught:
                runtime.cli_entry({})
            self.assertIn("legacy V2 mode cannot run on a V3 assignment", str(caught.exception))
        with self.env(TASK_AUTHORING_LEGACY_V2="1", TASK_AUTHORING_TASK_DIR=task_dir), \
                mock.patch.object(sys, "argv", ["entity.py"]):
            with self.assertRaises(runtime.ContextError):
                runtime.cli_entry({})
            with self.assertRaises(runtime.ContextError):
                runtime.ensure_active({}, require_source=False)
        with self.env(TASK_AUTHORING_LEGACY_V2="1"), mock.patch.object(sys, "argv", ["entity.py", "--self-test"]):
            self.assertIsNone(runtime.cli_entry({}))

    def test_legacy_mode_refuses_a_v3_task_named_only_by_its_input_file(self):
        # Re-review gap: no --task-dir and no task environment, only a V3 task's SQL path as the input.
        runtime = load_module(HERE / "runtime_context.py")
        sql = Path(self.task_dirs["synthcut"]) / "01_Universe_Inject.sql"
        sql.write_text("-- Are you planning to inject? Yes\n")
        with self.env(), mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("TASK_AUTHORING_TASK_DIR", None)
            os.environ.pop("TASK_AUTHORING_LEGACY_V2", None)
            with mock.patch.object(sys, "argv", ["base_check.py", "--legacy-v2", str(sql)]):
                with self.assertRaises(runtime.ContextError) as caught:
                    runtime.cli_entry({})
                self.assertIn("legacy V2 mode cannot run on a V3 assignment", str(caught.exception))

    def test_bound_kb_rejects_stale_or_missing_meta(self):
        runtime = load_module(HERE / "runtime_context.py")
        context = context_for("normal", kb_status="bound", kb_path=str(self.root / "kb"))
        kb = self.root / "kb"
        kb.mkdir()
        (kb / "timeline.json").write_text(json.dumps({"events": [], "_meta": meta()}))
        (kb / "entities.json").write_text(json.dumps({"entities": [], "_meta": meta(source_fingerprint="0" * 64)}))
        timeline = json.loads((kb / "timeline.json").read_text())
        stale = json.loads((kb / "entities.json").read_text())
        self.assertIs(runtime.validate_kb(timeline, {"TASK_CONTEXT": context}), timeline)
        with self.assertRaises(runtime.ContextError) as caught:
            runtime.validate_kb(stale, {"TASK_CONTEXT": context})
        self.assertIn("source_fingerprint", str(caught.exception))
        with self.assertRaises(runtime.ContextError):
            runtime.validate_kb({"entities": []}, {"TASK_CONTEXT": context})

    def test_generated_entities_with_an_unavailable_kb(self):
        runtime = load_module(HERE / "runtime_context.py")
        output = self.root / "kb_out"
        output.mkdir()
        context = context_for("synthcut", kb_status="unavailable", kb_output_path=str(output))
        entities = output / "entities.json"
        entities.write_text(json.dumps({"entities": [], "unresolved": [],
                                        "_meta": meta(universe="synthcut", clock="2025-10-01T07:00:00Z")}))
        with mock.patch.object(runtime, "WORKSPACE", self.root):
            namespace = {"OUT": Path("/previous/entities.json")}
            runtime._apply(namespace, context)
            self.assertEqual(namespace["OUT"], entities)
            self.assertEqual(runtime.entities_file(context), entities)
            entities.write_text(json.dumps({"entities": [], "_meta": meta(
                universe="synthcut", clock="2025-10-01T07:00:00Z", source_fingerprint="0" * 64)}))
            self.assertIsNone(runtime.entities_file(context))
            stale = {**context, "context_hash": CTX_B}
            namespace = {"OUT": Path("/previous/entities.json")}
            runtime._apply(namespace, stale)
            self.assertTrue(str(namespace["OUT"]).startswith(str(self.root / ".universe_source_not_ready")))
        # entity.load() uses the validated generated file; without it the KB-unavailable error stands.
        entities.write_text(json.dumps({"entities": [], "unresolved": [],
                                        "_meta": meta(universe="synthcut", clock="2025-10-01T07:00:00Z")}))
        with mock.patch.dict(sys.modules, {"runtime_context": runtime}):
            entity = load_module(HERE / "entity.py")
            entity.OUT = self.root / "missing" / "entities.json"
            entity.TASK_CONTEXT = context
            data = entity.load()
            self.assertIsInstance(entity.collisions(data), dict)
            entities.write_text(json.dumps({"entities": [], "_meta": meta(
                universe="synthcut", clock="2025-10-01T07:00:00Z", source_fingerprint="0" * 64)}))
            with self.assertRaises(SystemExit) as caught:
                entity.load()
            self.assertIn(context["source"]["reason"], str(caught.exception))

    def test_patched_linter_flags_synthcut_violations(self):
        context_hash = self.hashes["synthcut"]
        self.build("synthcut", context_hash)
        sql = self.root / "case.sql"
        sql.write_text(SQL)
        script = self.context_dir(context_hash) / "tools" / "hg_injection_lint.py"
        done = subprocess.run([sys.executable, str(script), "--no-base", "--sql", str(sql)],
                              cwd=str(self.root), capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stderr)
        result = json.loads(done.stdout)
        self.assertEqual(result["universe"], "synthcut")
        self.assertGreaterEqual(result["counts"]["FAIL"], 3, result["flags"])
        self.assertLessEqual({"text_time_format", "generated_column", "future_date"},
                             set(result["counts"]["by_check"]))

    def test_apply_and_ensure_active_fail_closed(self):
        runtime = load_module(HERE / "runtime_context.py")
        sentinel = self.root / ".universe_source_not_ready"
        base = self.root / "Universe_Normal" / "Normal_HarmonyGames_Other_Services" / "Services_Data"
        ready = {"context_hash": CTX_A, "freeze_utc": "2026-02-14T00:00:00Z",
                 "universe": {"key": "normal", "date": "2026-02-14", "clock_utc": "2026-02-14T00:00:00Z"},
                 "source": {"status": "ready", "reason": "ready", "mode": "universe", "universe": "normal",
                            "manifest": "Evals/references/universes/normal/universe_manifest.json",
                            "paths": {"slack": str(base / "slack"), "gmail": str(self.root / "g"),
                                      "github": str(self.root / "gh"), "linear": str(base / "linear")},
                            "fingerprint": FINGERPRINT, "data_clock": "2026-02-14T00:00:00Z",
                            "assigned_freeze": "2026-02-14T00:00:00Z", "kb_status": "reference-only",
                            "kb_path": str(self.local / "references" / "universe_kb"),
                            "kb_output_path": str(self.local / "references" / "universe_kb" / "by_universe" / "normal")}}
        blocked = {**ready, "context_hash": CTX_C, "source": {
            "status": "invalid", "reason": "Source service directories missing: slack", "mode": "universe",
            "universe": "normal", "manifest": None, "paths": {}, "fingerprint": FINGERPRINT,
            "data_clock": "2026-02-14T00:00:00Z", "assigned_freeze": "2026-02-14T00:00:00Z",
            "kb_status": "unavailable", "kb_path": None, "kb_output_path": str(self.local / "kb")}}
        namespace = {"OTHER": Path("/previous/other"), "GMAIL": Path("/previous/gmail"),
                     "GITHUB": Path("/previous/github/data.json"), "SLACK_MSGS": Path("/previous/slack"),
                     "CLOCK": None, "DATA_CLOCK": None, "KB": Path("/previous/kb"),
                     "OUT": Path("/previous/kb/entities.json")}
        with mock.patch.object(runtime, "WORKSPACE", self.root):
            runtime._apply(namespace, blocked)
            for key in ("OTHER", "GMAIL", "GITHUB", "SLACK_MSGS"):
                value = str(namespace[key])
                self.assertTrue(value.startswith(str(sentinel)), (key, value))
                self.assertNotIn("/previous/", value)
            self.assertEqual(namespace["CLOCK"].isoformat(), "2026-02-14T00:00:00+00:00")
            self.assertEqual(namespace["DATA_CLOCK"].isoformat(), "2026-02-14T00:00:00+00:00")
            self.assertTrue(str(namespace["KB"]).startswith(str(sentinel)))
            self.assertTrue(str(namespace["OUT"]).startswith(str(sentinel)))
            runtime._apply(namespace, ready)
            self.assertEqual(namespace["OTHER"], base)
            self.assertEqual(namespace["GMAIL"], Path(ready["source"]["paths"]["gmail"]))
            self.assertEqual(namespace["GITHUB"], Path(ready["source"]["paths"]["github"]) / "data.json")
            self.assertEqual(namespace["SLACK_MSGS"], Path(ready["source"]["paths"]["slack"]) / "messages")
            self.assertEqual(namespace["KB"], Path(ready["source"]["kb_path"]))
            no_kb = {**ready, "context_hash": CTX_B, "source": {**ready["source"], "kb_status": "reference-only",
                                                                "kb_path": None}}
            runtime._apply(namespace, no_kb)
            self.assertTrue(str(namespace["KB"]).startswith(str(sentinel)))
            # The same context hash must still be re-checked for readiness.
            runtime._apply(namespace, blocked)
            calls = []

            def fake_load(task_dir, require_source=False):
                calls.append(require_source)
                return blocked

            namespace["TASK_CONTEXT"] = blocked
            with mock.patch.object(runtime, "MODULES", ()), \
                    mock.patch.object(runtime, "load_context", fake_load), \
                    mock.patch.dict(os.environ, {"TASK_AUTHORING_TASK_DIR": str(self.root),
                                                 "TASK_AUTHORING_CONTEXT_HASH": CTX_C}):
                os.environ.pop("TASK_AUTHORING_LEGACY_V2", None)
                with self.assertRaises(runtime.ContextError) as caught:
                    runtime.ensure_active(namespace, require_source=True)
                self.assertEqual(str(caught.exception), blocked["source"]["reason"])
                self.assertEqual(calls, [True])

    def test_v2_fixture_roots_fall_back_to_the_normal_universe(self):
        tc = load_module(HERE / "task_context.py")
        ws = self.root / "v2-roots"
        ws.mkdir()
        # Only Universe_*/ installed (the old root exports removed): the Feb 14, 2026 data is used ...
        (ws / "Universe_SynthCut" / "SynthCut_HarmonyGames_GitHub").mkdir(parents=True)
        for name in ("GitHub", "Gmail", "Other_Services"):
            self.assertEqual(tc.v2_export_root(name, ws), ws / "Universe_Normal" / f"Normal_HarmonyGames_{name}")
        # ... while an old root export, when present, is still preferred.
        (ws / "HarmonyGames_Gmail").mkdir()
        self.assertEqual(tc.v2_export_root("Gmail", ws), ws / "HarmonyGames_Gmail")

    def test_sandbox_task_context_patch_anchors_match_once(self):
        sandbox = load_module(HERE / "selftest_sandbox.py")
        text = (HERE / "task_context.py").read_text()
        for old, _new in sandbox.TASK_CONTEXT_PATCH:
            self.assertEqual(text.count(old), 1, old)


if __name__ == "__main__":
    unittest.main()

"""Focused assignment, freeze, source-isolation and date acceptance regressions."""
import datetime as dt
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import task_context as tc
import runtime_context as runtime
import sql_lint

RAW = """🏢 Business Function
Executive
🧑 Persona
Frederick Stone
Role: Co-founder
🎯 Competency
Corporate Ops
🛠️ Task Skill
Authoring
📋 Task Type
long-horizon
🎚️ Difficulty Mode
easy
📅 Universe Date
October 1, 2025 07:00
"""


class TaskContextTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.task = self.root / "task"
        self.task.mkdir()
        self.assignment = self.task / "00_Assigments.md"
        self.assignment.write_text(RAW)

    def context(self, **kwargs):
        return tc.load_context(self.task, **kwargs)

    def test_exact_platform_paste(self):
        ctx = self.context()
        self.assertEqual(ctx["persona_key"], "frederick_stone")
        self.assertEqual(ctx["persona_role"], "Co-founder")
        self.assertEqual(ctx["horizon"], "Long Horizon")
        self.assertEqual(ctx["difficulty_cap"], .9)
        self.assertEqual(ctx["universe_date_raw"], "October 1, 2025 07:00")
        self.assertEqual(ctx["freeze_utc"], "2025-10-01T00:00:00Z")

    def test_template_requires_only_platform_block_to_be_filled(self):
        template = (tc.BUNDLE / "references/Tasks_Template/00_Assigments.md").read_text()
        prefix, rest = template.split("```text", 1)
        _, suffix = rest.split("```", 1)
        self.assignment.write_text(prefix + "```text\n" + RAW + "```" + suffix)
        ctx = self.context()
        self.assertEqual(ctx["persona_key"], "frederick_stone")
        self.assertEqual(ctx["difficulty_cap"], .9)

    def test_emoji_free_and_legacy_mirror(self):
        self.assignment.write_text("""business_function: Executive
persona_name: Frederick Stone
persona_role: Co-founder
competency: Corporate Ops
task_skill: Authoring
horizon: Long Horizon
difficulty_mode: EASY
universe_date: October 1, 2025 07:00
""")
        self.assertEqual(self.context()["difficulty_mode"], "easy")

    def test_missing_or_conflicting_assigned_values(self):
        for bad in (RAW.replace("Role: Co-founder", ""), RAW + "\ndifficulty_mode: hard",
                    RAW + "\nhorizon: Normal Horizon", RAW.replace("Co-founder", "QA Lead")):
            with self.subTest(bad=bad):
                self.assignment.write_text(bad)
                with self.assertRaises(tc.ContextError):
                    self.context()

    def test_mirror_must_not_substitute_identity_or_clock(self):
        for line in ("email: invented@harmonygames.co", "freeze_utc: 2026-02-14T00:00:00Z",
                     "persona_key: arthur_blake", "universe_date_key: 2026-02-14"):
            self.assignment.write_text(RAW + "\n" + line)
            with self.assertRaises(tc.ContextError):
                self.context()

    def test_modes_and_two_freezes(self):
        for mode, cap in (("easy", .9), ("medium", .85), ("hard", .7)):
            self.assignment.write_text(RAW.replace("easy", mode).replace("October 1, 2025 07:00", "February 14, 2026 08:00"))
            ctx = self.context()
            self.assertEqual(ctx["difficulty_cap"], cap)
            self.assertEqual(ctx["freeze_utc"], "2026-02-14T00:00:00Z")
            self.assertEqual(ctx["source"]["status"], "ready")

    def test_same_universe_has_distinct_assignment_freezes(self):
        october = self.context(require_source=True)
        self.assignment.write_text(RAW.replace("October 1, 2025 07:00", "February 14, 2026 08:00"))
        february = self.context(require_source=True)
        self.assertEqual(october["source"]["paths"], february["source"]["paths"])
        self.assertEqual(october["source"]["fingerprint"], february["source"]["fingerprint"])
        self.assertEqual(october["source"]["data_clock"], "2026-02-14T00:00:00Z")
        self.assertEqual(october["freeze_utc"], "2025-10-01T00:00:00Z")
        self.assertEqual(february["freeze_utc"], "2026-02-14T00:00:00Z")
        self.assertNotEqual(october["context_hash"], february["context_hash"])

    def test_missing_registry_entry_still_blocks_source_access(self):
        registry = self.root / "missing-source.json"
        registry.write_text(json.dumps({"sources": {"2025-10-01": None}}))
        self.assertEqual(self.context(registry_path=registry)["source"]["status"], "unavailable")
        with self.assertRaisesRegex(tc.ContextError, "No universe source"):
            self.context(require_source=True, registry_path=registry)

    def test_wrong_manifest_clock_rejected(self):
        registry = self.root / "sources.json"
        registry.write_text(json.dumps({"sources": {"2025-10-01": {
            "manifest": "Evals/references/universe_manifest.json",
            "kb_path": "Task_Authoring/references/universe_kb",
            "historical_state_verified": True, "verification_basis": "fixture"}}}))
        ctx = self.context(registry_path=registry)
        self.assertEqual(ctx["source"]["status"], "invalid")
        self.assertIn("does not match assigned freeze", ctx["source"]["reason"])

    def test_external_manifest_is_rejected_before_lookup(self):
        manifest = self.root / "manifest.json"
        manifest.write_text("{}")
        registry = self.root / "registry.json"
        registry.write_text(json.dumps({"sources": {"2025-10-01": {
            "manifest": str(manifest), "kb_path": "Task_Authoring/references/universe_kb",
            "historical_state_verified": True, "verification_basis": "fixture"}}}))
        ctx = self.context(registry_path=registry)
        self.assertEqual(ctx["source"]["status"], "invalid")
        self.assertIn("inside the workspace", ctx["source"]["reason"])

    def test_hashes_change_with_assignment_and_policy(self):
        a = self.context()
        self.assignment.write_text(RAW.replace("easy", "medium"))
        b = self.context()
        self.assertNotEqual(a["assignment_hash"], b["assignment_hash"])
        self.assertNotEqual(a["context_hash"], b["context_hash"])
        policy = json.loads(tc.POLICY_PATH.read_text())
        policy["policy_version"] += "-fixture"
        path = self.root / "policy.json"
        path.write_text(json.dumps(policy))
        c = self.context(policy_path=path)
        self.assertNotEqual(b["policy_hash"], c["policy_hash"])
        self.assertNotEqual(b["context_hash"], c["context_hash"])

    def test_runtime_changes_clock_and_cache_without_reusing_task_state(self):
        a = self.context()
        self.assignment.write_text(RAW.replace("easy", "hard"))
        b = self.context()
        ns = {"CLOCK": dt.datetime(2026, 2, 14, tzinfo=dt.timezone.utc),
              "CACHE": tc.BUNDLE / "support/local_search/cache", "_KB": {"stale": 1}}
        runtime._apply(ns, a)
        cache = ns["CACHE"]
        self.assertEqual(ns["CLOCK"].date().isoformat(), "2025-10-01")
        self.assertFalse(ns["_KB"])
        runtime._apply(ns, b)
        self.assertNotEqual(cache, ns["CACHE"])

    def test_timestamp_boundary_and_future_deadline(self):
        ctx = self.context()
        with patch.dict(os.environ, {}, clear=True), patch.dict(sql_lint.__dict__, {
                "CLOCK": dt.datetime(2025, 10, 1, tzinfo=dt.timezone.utc), "TASK_CONTEXT": ctx}):
            errors, warnings = [], []
            error = lambda line, msg: errors.append(msg)
            warn = lambda line, msg: warnings.append(msg)
            sql_lint.check_time("confluence.confluence_pages", "created_at", "2025-09-30T23:59:59Z", 1, error, warn)
            sql_lint.check_time("confluence.confluence_pages", "created_at", "2025-10-01T00:00:00Z", 1, error, warn)
            self.assertFalse(errors)
            sql_lint.check_time("confluence.confluence_pages", "created_at", "2025-10-01T00:00:01Z", 1, error, warn)
            self.assertEqual(len(errors), 1)
            sql_lint.check_time("linear.linear_issues", "due_date", "2025-10-02", 1, error, warn)
            self.assertEqual(len(errors), 1)
            self.assertEqual(len(warnings), 1)

    def test_date_acceptance_handles_pacific_dst_and_requested_zone(self):
        fall = tc.date_acceptance("2025-11-17T03:00:00Z")
        self.assertEqual(fall["accepted_dates"], ["2025-11-16", "2025-11-17"])
        self.assertEqual(tc.date_acceptance("2025-10-01T00:00:00Z")["pacific"], "2025-09-30")
        self.assertEqual(tc.date_acceptance("2025-11-17T03:00:00Z", "UTC")["accepted_dates"], ["2025-11-17"])
        self.assertEqual(tc.date_acceptance("2025-11-17T03:00:00Z", "Pacific")["accepted_dates"], ["2025-11-16"])

    def test_patched_search_helpers_route_selected_manifest_and_compile(self):
        import sys
        sys.path.insert(0, str(tc.BUNDLE / "setup"))
        import local_search
        for name in ("hg_search.py", "hg_records.py", "hg_reference.py", "hg_compact_index.py"):
            source = (tc.WORKSPACE / "Evals" / "tools" / name).read_text()
            result = local_search.patched(source)
            compile(result, name, "exec")
            self.assertIn("TASK_AUTHORING_UNIVERSE_MANIFEST", result)
            self.assertNotIn("Evals/.cache/", result)

    def test_real_bounded_reader_uses_selected_source(self):
        from v3_artifact_checks import _bounded_get
        self.assignment.write_text(RAW.replace("October 1, 2025 07:00", "February 14, 2026 08:00"))
        ctx = self.context(require_source=True)
        root = Path(ctx["source"]["paths"]["contacts"])
        value = _bounded_get("contacts", root / "contacts.json", root, "/contacts/0/contact_id", self.task)
        self.assertIsInstance(value, str)
        self.assertTrue(value)

    def test_explicit_v3_activation_clears_archival_environment(self):
        with patch.dict(os.environ, {"TASK_AUTHORING_LEGACY_V2": "1"}):
            runtime.activate({}, self.task)
            self.assertNotIn("TASK_AUTHORING_LEGACY_V2", os.environ)

    def test_roster_listing_does_not_need_historical_snapshot(self):
        result = subprocess.run([sys.executable, "-B", str(tc.BUNDLE / "tools/persona_view.py"),
                                 "personas", "--json", "--task-dir", str(self.task)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(any(p["persona_key"] == "frederick_stone" for p in json.loads(result.stdout)))


if __name__ == "__main__":
    unittest.main()

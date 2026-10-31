"""Focused assignment, universe, freeze, source-isolation, KB and date acceptance regressions."""
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import task_context as tc
import runtime_context as runtime
import sql_lint

SCRATCH = tc.BUNDLE / "support" / "scratch"
REAL_WORKSPACE = tc.BUNDLE.parent
CLOCKS = {"normal": "2026-02-14T00:00:00Z", "synthcut": "2025-10-01T07:00:00Z"}
HUMAN_CLOCKS = {"normal": "2026-02-14 00:00 UTC",
                "synthcut": "2025-10-01 07:00 UTC (2025-10-01 00:00 PT)"}
FEBRUARY = "February 14, 2026 08:00"
NORMAL_BLOCK = {
    "key": "normal", "date": "2026-02-14", "label": "Feb 14, 2026 (normal)", "folder": "Universe_Normal",
    "prefix": "Normal", "clock_utc": "2026-02-14T00:00:00Z", "clock_text": "2026-02-14 00:00 UTC",
    "clock_line": "Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)", "shutdown_rules_apply": True,
    "persona_today": "2026-02-14", "persona_today_weekday": "Saturday", "build_label": "hg4-2026-08-31 v37",
}
SYNTHCUT_BLOCK = {
    "key": "synthcut", "date": "2025-10-01", "label": "Oct 1, 2025 (synth-cut)", "folder": "Universe_SynthCut",
    "prefix": "SynthCut", "clock_utc": "2025-10-01T07:00:00Z",
    "clock_text": "2025-10-01 00:00 PT (2025-10-01 07:00 UTC)",
    "clock_line": "Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)",
    "shutdown_rules_apply": False, "persona_today": "2025-10-01", "persona_today_weekday": "Wednesday",
    "build_label": "hg4-synth-sep30cut v16",
}

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
        # GEN_EXECUTION §1: self-tests write only under support/scratch.
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(dir=SCRATCH, prefix="task_context_"))
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        self.workspace = self.root / "workspace"
        self.registry = self.root / "universe_sources.json"
        self.task = self.root / "task"
        self.task.mkdir()
        self.assignment = self.task / "00_Assigments.md"
        self.assignment.write_text(RAW)
        patcher = patch.object(tc, "WORKSPACE", self.workspace)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.build_universe("normal")
        self.build_universe("synthcut")
        self.write_registry()

    def build_universe(self, key, *, folder=None, prefix=None, manifest_universe=None, evaluation_clock=None):
        entry = tc._universe_module().UNIVERSES[key]
        folder, prefix = folder or entry["folder"], prefix or entry["prefix"]
        manifest = {"format_version": 1, "universe": manifest_universe or key,
                    "evaluation_clock": evaluation_clock or HUMAN_CLOCKS[key], "services": {}}
        for service in tc.SERVICES:
            base = {"github": f"{folder}/{prefix}_HarmonyGames_GitHub",
                    "gmail": f"{folder}/{prefix}_HarmonyGames_Gmail"}.get(
                service, f"{folder}/{prefix}_HarmonyGames_Other_Services")
            relative = f"{base}/Services_Data/{service}"
            (self.workspace / relative).mkdir(parents=True, exist_ok=True)
            manifest["services"][service] = {"path": relative}
        path = self.workspace / "Evals/references/universes" / key / "universe_manifest.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(manifest, indent=1))
        return manifest

    def write_registry(self, overrides=None):
        overrides = overrides or {}
        sources = {}
        for key, date in (("synthcut", "2025-10-01"), ("normal", "2026-02-14")):
            entry = {"mode": "universe", "universe": key,
                     "manifest": f"Evals/references/universes/{key}/universe_manifest.json",
                     "kb_output_path": str(self.root / "kb" / key),
                     "legacy_kb_path": str(self.root / "legacy_kb") if key == "normal" else None,
                     "verification_basis": "fixture"}
            entry.update(overrides.get(date, {}))
            sources[date] = entry
        self.registry.write_text(json.dumps({"format_version": 2, "sources": sources}, indent=1))

    def write_timeline(self, key, fingerprint, **overrides):
        meta = {"universe": key, "clock": CLOCKS[key], "source_fingerprint": fingerprint,
                "build": "per-universe-v1", **overrides}
        path = self.root / "kb" / key / "timeline.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"_meta": meta, "spine": []}))

    def context(self, **kwargs):
        kwargs.setdefault("registry_path", self.registry)
        return tc.load_context(self.task, **kwargs)

    def assign(self, display):
        self.assignment.write_text(RAW.replace("October 1, 2025 07:00", display))

    def test_exact_platform_paste(self):
        ctx = self.context()
        self.assertEqual(ctx["persona_key"], "frederick_stone")
        self.assertEqual(ctx["persona_role"], "Co-founder")
        self.assertEqual(ctx["horizon"], "Long Horizon")
        self.assertEqual(ctx["difficulty_cap"], .9)
        self.assertEqual(ctx["universe_date_raw"], "October 1, 2025 07:00")
        self.assertEqual(ctx["freeze_utc"], "2025-10-01T00:00:00Z")
        self.assertEqual(ctx["universe"], SYNTHCUT_BLOCK)

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

    def test_label_without_value_stays_missing(self):
        # A deleted value must not borrow the text after the platform block (closing fence, heading, prose).
        bare = RAW.replace("October 1, 2025 07:00\n", "")
        for pasted in ("```text\n" + bare + "```\n\n## Resolved authoring inputs\n\nProse.\n",
                       bare + "\n## Resolved authoring inputs\n\nProse.\n"):
            with self.subTest(pasted=pasted[-60:]):
                self.assignment.write_text(pasted)
                with self.assertRaises(tc.ContextError) as caught:
                    self.context()
                self.assertIn("Missing V3 assigned fields: universe_date_raw", str(caught.exception))

    def test_mirror_must_not_substitute_identity_or_clock(self):
        for line in ("email: invented@harmonygames.co", "freeze_utc: 2026-02-14T00:00:00Z",
                     "persona_key: arthur_blake", "universe_date_key: 2026-02-14"):
            self.assignment.write_text(RAW + "\n" + line)
            with self.assertRaises(tc.ContextError):
                self.context()

    def test_modes_and_two_freezes(self):
        for mode, cap in (("easy", .9), ("medium", .85), ("hard", .7)):
            self.assignment.write_text(RAW.replace("easy", mode).replace("October 1, 2025 07:00", FEBRUARY))
            ctx = self.context()
            self.assertEqual(ctx["difficulty_cap"], cap)
            self.assertEqual(ctx["freeze_utc"], "2026-02-14T00:00:00Z")
            self.assertEqual(ctx["universe"], NORMAL_BLOCK)
            self.assertEqual(ctx["source"]["status"], "ready")

    def test_two_dates_select_two_universes(self):
        october = self.context(require_source=True)
        self.assign(FEBRUARY)
        february = self.context(require_source=True)
        self.assertEqual(october["universe"], SYNTHCUT_BLOCK)
        self.assertEqual(february["universe"], NORMAL_BLOCK)
        self.assertNotEqual(october["source"]["manifest"], february["source"]["manifest"])
        self.assertNotEqual(october["source"]["paths"], february["source"]["paths"])
        self.assertNotEqual(october["source"]["fingerprint"], february["source"]["fingerprint"])
        self.assertEqual(october["source"]["data_clock"], "2025-10-01T07:00:00Z")
        self.assertEqual(february["source"]["data_clock"], "2026-02-14T00:00:00Z")
        self.assertEqual(october["source"]["assigned_freeze"], october["freeze_utc"])
        self.assertEqual(october["freeze_utc"], "2025-10-01T00:00:00Z")
        self.assertEqual(february["freeze_utc"], "2026-02-14T00:00:00Z")
        for ctx, key in ((october, "synthcut"), (february, "normal")):
            self.assertEqual(ctx["source"]["mode"], "universe")
            self.assertEqual(ctx["source"]["universe"], key)
            manifest = (self.workspace / "Evals/references/universes" / key / "universe_manifest.json").resolve()
            self.assertEqual(ctx["source"]["manifest"], str(manifest))
            self.assertTrue(len(ctx["source"]["paths"]) == len(tc.SERVICES))
            for value in ctx["source"]["paths"].values():
                relative = Path(value).relative_to(self.workspace)
                self.assertEqual(relative.parts[0], tc._universe_module().UNIVERSES[key]["folder"])
                self.assertTrue(relative.parts[1].startswith(tc._universe_module().UNIVERSES[key]["prefix"] + "_HarmonyGames_"))
        self.assertNotEqual(october["context_hash"], february["context_hash"])

    def test_missing_registry_entry_still_blocks_source_access(self):
        registry = self.root / "missing-source.json"
        registry.write_text(json.dumps({"sources": {"2025-10-01": None}}))
        ctx = self.context(registry_path=registry)
        self.assertEqual(ctx["source"]["status"], "unavailable")
        self.assertEqual(ctx["source"]["universe"], "synthcut")
        self.assertEqual(ctx["source"]["paths"], {})
        self.assertEqual(ctx["source"]["kb_status"], "unavailable")
        with self.assertRaisesRegex(tc.ContextError, "No universe source"):
            self.context(require_source=True, registry_path=registry)

    def test_registry_mode_and_identity_errors(self):
        cases = (
            ({"mode": "shared-universe"}, "retired by Evals dual-universe-v1"),
            ({"universe": "normal"}, "does not match date"),
            ({"manifest": "Evals/references/universes/normal/universe_manifest.json"}, "universe_manifest.json"),
        )
        for override, message in cases:
            with self.subTest(override=override):
                self.write_registry({"2025-10-01": override})
                ctx = self.context()
                self.assertEqual(ctx["source"]["status"], "invalid")
                self.assertIn(message, ctx["source"]["reason"])
                self.assertEqual(ctx["source"]["paths"], {})
                self.assertEqual(ctx["source"]["kb_output_path"], str(self.root / "kb" / "synthcut"))
                with self.assertRaises(tc.ContextError):
                    self.context(require_source=True)

    def test_manifest_universe_mismatch_rejected(self):
        self.build_universe("synthcut", manifest_universe="normal")
        ctx = self.context()
        self.assertEqual(ctx["source"]["status"], "invalid")
        self.assertIn("declares universe 'normal'", ctx["source"]["reason"])

    def test_service_folders_must_match_universe_folder_and_prefix(self):
        for kwargs, message in (({"folder": "Universe_Normal", "prefix": "Normal"}, "Universe_SynthCut/SynthCut_HarmonyGames_*"),
                                ({"prefix": "Wrong"}, "SynthCut_HarmonyGames_*")):
            with self.subTest(kwargs=kwargs):
                self.build_universe("synthcut", **kwargs)
                ctx = self.context()
                self.assertEqual(ctx["source"]["status"], "invalid")
                self.assertIn(message, ctx["source"]["reason"])

    def test_external_manifest_is_rejected_before_lookup(self):
        manifest = self.root / "manifest.json"
        manifest.write_text("{}")
        self.write_registry({"2025-10-01": {"manifest": str(manifest)}})
        ctx = self.context()
        self.assertEqual(ctx["source"]["status"], "invalid")
        self.assertIn("inside the workspace", ctx["source"]["reason"])

    def test_assigned_freeze_must_not_exceed_data_clock(self):
        self.assign(FEBRUARY)
        policy = json.loads(tc.POLICY_PATH.read_text())
        policy["freeze_dates"]["2026-02-14"] = "2026-02-15T00:00:00Z"
        path = self.root / "policy.json"
        path.write_text(json.dumps(policy))
        ctx = self.context(policy_path=path)
        self.assertEqual(ctx["source"]["status"], "invalid")
        self.assertIn("after the normal data clock", ctx["source"]["reason"])

    def test_missing_universe_data_blocks_with_install_hint(self):
        # The shipped registry on a fixture workspace without that universe's folder (the real one may be installed).
        for display, folder in (("October 1, 2025 07:00", "Universe_SynthCut"), (FEBRUARY, "Universe_Normal")):
            with self.subTest(folder=folder):
                self.assign(display)
                shutil.rmtree(self.workspace / folder)
                ctx = tc.load_context(self.task, registry_path=tc.SOURCES_PATH)
                self.assertEqual(ctx["source"]["status"], "invalid")
                self.assertIn("Source service directories missing:", ctx["source"]["reason"])
                self.assertIn(f"Install {folder}/ per Evals/UNIVERSE_MAP.md", ctx["source"]["reason"])
                self.assertEqual(ctx["source"]["paths"], {})

    def test_clock_comes_from_hg_universe_not_manifest_text(self):
        manifest = (self.workspace / "Evals/references/universes/synthcut/universe_manifest.json").resolve()
        self.assertEqual(json.loads(manifest.read_text())["evaluation_clock"],
                         "2025-10-01 07:00 UTC (2025-10-01 00:00 PT)")
        ctx = self.context()
        self.assertEqual(ctx["source"]["status"], "ready")
        self.assertEqual(ctx["source"]["data_clock"], "2025-10-01T07:00:00Z")
        self.assertEqual(ctx["source"]["data_clock"], ctx["universe"]["clock_utc"])
        self.assertEqual(ctx["universe"]["clock_line"], tc._universe_module().report_line("synthcut"))

    def test_kb_status_bound_reference_only_and_unavailable(self):
        october = self.context()
        self.assertEqual(october["source"]["kb_status"], "unavailable")
        self.assertIsNone(october["source"]["kb_path"])
        self.assertEqual(october["source"]["kb_output_path"], str(self.root / "kb" / "synthcut"))
        self.write_timeline("synthcut", fingerprint=october["source"]["fingerprint"])
        bound = self.context()
        self.assertEqual(bound["source"]["kb_status"], "bound")
        self.assertEqual(bound["source"]["kb_path"], str(self.root / "kb" / "synthcut"))
        self.assertEqual(bound["source"]["fingerprint"], october["source"]["fingerprint"])
        self.assign(FEBRUARY)
        february = self.context()
        self.assertEqual(february["source"]["kb_status"], "reference-only")
        self.assertEqual(february["source"]["kb_path"], str(self.root / "legacy_kb"))
        self.write_timeline("normal", fingerprint=february["source"]["fingerprint"])
        self.assertEqual(self.context()["source"]["kb_status"], "bound")

    def test_synthcut_never_falls_back_to_the_legacy_kb(self):
        # A valid-looking legacy Feb-14 KB on disk is never bound to, or readable for, a synth-cut task.
        legacy = self.root / "legacy_kb"
        legacy.mkdir(parents=True, exist_ok=True)
        (legacy / "timeline.json").write_text(json.dumps({"_meta": {"clock": CLOCKS["normal"]}, "spine": []}))
        october = self.context()
        self.assertEqual(october["source"]["kb_status"], "unavailable")
        self.assertIsNone(october["source"]["kb_path"])
        shipped = json.loads(tc.SOURCES_PATH.read_text())["sources"]["2025-10-01"]
        self.assertIsNone(shipped.get("legacy_kb_path"))
        with self.assertRaises(runtime.KBUnavailable):
            runtime.validate_kb(json.loads((legacy / "timeline.json").read_text()), {"TASK_CONTEXT": october})

    def test_kb_binding_requires_matching_provenance(self):
        october = self.context()
        fingerprint = october["source"]["fingerprint"]
        for overrides in ({"universe": "normal"}, {"clock": "2026-02-14T00:00:00Z"},
                          {"source_fingerprint": "0" * 64}, {"build": "shared-kb-v1"}):
            with self.subTest(overrides=overrides):
                self.write_timeline("synthcut", fingerprint=fingerprint, **overrides)
                self.assertEqual(self.context()["source"]["kb_status"], "unavailable")
        self.assign(FEBRUARY)
        february = self.context()
        self.write_timeline("normal", fingerprint="0" * 64)
        self.assertEqual(self.context()["source"]["kb_status"], "reference-only")
        self.write_timeline("normal", fingerprint=february["source"]["fingerprint"], clock="2025-10-01T07:00:00Z")
        self.assertEqual(self.context()["source"]["kb_status"], "reference-only")

    def test_registry_is_pinned_to_hg_universe(self):
        registry = json.loads(tc.SOURCES_PATH.read_text())
        module = tc._universe_module()
        self.assertEqual(registry["format_version"], 2)
        self.assertEqual(sorted(registry["sources"]), sorted(entry["date"] for entry in module.UNIVERSES.values()))
        for date, entry in registry["sources"].items():
            key = next(k for k, v in module.UNIVERSES.items() if v["date"] == date)
            self.assertEqual(entry["mode"], "universe")
            self.assertEqual(entry["universe"], key)
            self.assertEqual(entry["manifest"], f"Evals/references/universes/{key}/universe_manifest.json")
            self.assertEqual(entry["kb_output_path"], f"Task_Authoring/references/universe_kb/by_universe/{key}")
            self.assertTrue(entry["verification_basis"])
        self.assertIsNone(registry["sources"]["2025-10-01"]["legacy_kb_path"])
        self.assertEqual(registry["sources"]["2026-02-14"]["legacy_kb_path"], "Task_Authoring/references/universe_kb")
        self.assertIn("Task date and universe", registry["note"])
        self.assertIn("dual-universe-v1", registry["note"])
        self.assertNotIn("user confirmed", registry["note"].casefold())

    def test_legacy_snapshot_mode_still_verifies_its_manifest_clock(self):
        manifest = self.build_universe("normal", evaluation_clock="2026-02-14T00:00:00Z")
        snapshot = self.workspace / "snapshot_manifest.json"
        snapshot.write_text(json.dumps(manifest))
        override = {"mode": "snapshot", "manifest": "snapshot_manifest.json", "historical_state_verified": True}
        self.write_registry({"2025-10-01": override, "2026-02-14": override})
        october = self.context()
        self.assertEqual(october["source"]["status"], "invalid")
        self.assertIn("does not match assigned freeze", october["source"]["reason"])
        self.assign(FEBRUARY)
        ctx = self.context()
        self.assertEqual(ctx["source"]["status"], "ready")
        self.assertEqual(ctx["source"]["mode"], "snapshot")
        self.assertEqual(ctx["source"]["data_clock"], "2026-02-14T00:00:00Z")

    def test_loader_never_uses_the_saved_eval_task_date(self):
        source = (tc.BUNDLE / "tools/task_context.py").read_text()
        self.assertNotIn("task_inputs/inputs.json", source)
        self.assertNotIn(".selected(", source)
        self.assertNotIn("hg_universe.info", source)

    def test_loading_hg_universe_writes_nothing_under_evals(self):
        root = REAL_WORKSPACE / "Evals" / "tools"

        def listing():
            return {path.relative_to(root).as_posix(): (path.stat().st_size, path.stat().st_mtime_ns)
                    for path in sorted(root.rglob("*"))}

        before = listing()
        module = tc._universe_module()
        self.assertEqual(tc.universe_block("normal", module)["clock_utc"], "2026-02-14T00:00:00Z")
        tc.load_context(self.task, registry_path=self.registry)
        self.assertEqual(before, listing())

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

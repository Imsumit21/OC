"""Per-universe KB build-context checks; never scan or rebuild the universe exports.

Fixtures live only under Task_Authoring/support/scratch (tempfile.mkdtemp) and are removed
after each test. The two synthetic universes come from the real task_context registry; only
the data paths are fixtures, so no universe export is required.
"""
import contextlib
import datetime
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parents[2]          # Task_Authoring
WORKSPACE = HERE.parents[3]       # workspace root that holds the eval bundle
SCRATCH = BUNDLE / "support" / "scratch"
sys.path.insert(0, str(BUNDLE / "tools"))
import task_context

UNIVERSES = ("normal", "synthcut")


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BuildContextTests(unittest.TestCase):
    # ---------------------------------------------------------------- fixtures
    def fixture(self, key, overrides=True):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        base = Path(tempfile.mkdtemp(prefix="kb-%s-" % key, dir=str(SCRATCH)))
        self.addCleanup(shutil.rmtree, base, True)
        universe = dict(task_context.universe_block(key))
        other = base / "data" / universe["folder"] / (universe["prefix"] + "_HarmonyGames_Other_Services")
        services = other / "Services_Data"
        paths = {}
        for service in task_context.SERVICES:
            (services / service).mkdir(parents=True)
            paths[service] = str(services / service)
        (other / "metadata").mkdir()
        manifest_data = {"universe": key}
        if overrides:
            snow_index = base / "indexes" / "snowflake-snowflake.json"
            snow_index.parent.mkdir()
            snow_index.write_text("{}")
            manifest_data["kb_build_paths"] = {"metadata_path": str(other / "metadata"),
                                               "snowflake_index": str(snow_index)}
        manifest = base / "universe_manifest.json"
        manifest.write_text(json.dumps(manifest_data))
        output = base / "kb" / "by_universe" / key
        output.mkdir(parents=True)
        context = {
            "universe_date_key": universe["date"],
            "freeze_utc": universe["date"] + "T00:00:00Z",
            "context_hash": "test-" + key,
            "universe": universe,
            "source": {"status": "ready", "mode": "universe", "universe": key,
                       "manifest": str(manifest), "paths": paths,
                       "fingerprint": "fingerprint-" + key, "data_clock": universe["clock_utc"],
                       "kb_status": "unavailable", "kb_path": None,
                       "kb_output_path": str(output)},
        }
        return context, base

    def common(self, context):
        with patch.object(task_context, "load_context", return_value=context), patch("os.makedirs"):
            return module_at("synthetic_kb_common", HERE / "common.py")

    @staticmethod
    def root_snapshot():
        legacy = HERE.parent
        return {p.name: (p.stat().st_size, p.stat().st_mtime_ns) for p in legacy.iterdir() if p.is_file()}

    # ---------------------------------------------------------------- paths / clock
    def test_paths_cache_clock_and_json_provenance(self):
        context, base = self.fixture("normal")
        common = self.common(context)
        self.assertEqual(common.UNIVERSE_KEY, "normal")
        self.assertEqual(common.CLOCK_ISO, "2026-02-14T00:00:00Z")
        self.assertEqual(common.SEED_BOUND_ISO, context["freeze_utc"])
        self.assertEqual(common.SLACK, context["source"]["paths"]["slack"])
        self.assertEqual(Path(common.OUT), Path(context["source"]["kb_output_path"]))
        self.assertTrue(common.CACHE.endswith("normal/fingerprint-normal"))
        artifact = Path(common.OUT) / "artifact.json"
        common.jdump({"_meta": {"generated_by": "test", "keep": 1}, "count": 2}, artifact)
        meta = json.loads(artifact.read_text())["_meta"]
        self.assertEqual(meta["universe"], "normal")
        self.assertEqual(meta["clock"], common.CLOCK_ISO)
        self.assertEqual(meta["seed_bound"], context["freeze_utc"])
        self.assertEqual(meta["source_fingerprint"], "fingerprint-normal")
        self.assertEqual(meta["build"], "per-universe-v1")
        self.assertEqual(meta["keep"], 1)
        common.jdump([1, 2], artifact)
        self.assertEqual(json.loads(artifact.read_text()), [1, 2])
        self.assertEqual(json.loads(Path(str(artifact) + ".meta.json").read_text())["_meta"]["clock"], common.CLOCK_ISO)
        cache_mapping = base / "cache-map.json"
        common.jdump({"record-1": {"count": 2}}, cache_mapping)
        self.assertEqual(list(json.loads(cache_mapping.read_text())), ["record-1"])
        self.assertEqual(json.loads(Path(str(cache_mapping) + ".meta.json").read_text())["_meta"]["universe"], "normal")

    def test_synthcut_clock_is_the_data_horizon_not_the_seed_bound(self):
        context, _ = self.fixture("synthcut")
        common = self.common(context)
        self.assertEqual(common.CLOCK_ISO, "2025-10-01T07:00:00Z")
        self.assertEqual(common.SEED_BOUND_ISO, "2025-10-01T00:00:00Z")
        self.assertNotEqual(common.CLOCK_ISO, common.SEED_BOUND_ISO)
        self.assertTrue(common.before_clock("2025-09-30T23:59:59Z"))
        self.assertFalse(common.before_clock(common.CLOCK_ISO))
        self.assertTrue(common.within_horizon(common.CLOCK_ISO))
        self.assertFalse(common.within_horizon("2025-10-02T00:00:00Z"))
        self.assertFalse(common.within_horizon(None))

    def test_paths_derive_from_the_universe_without_root_literals(self):
        for key in UNIVERSES:
            with self.subTest(key=key):
                context, _ = self.fixture(key, overrides=False)
                common = self.common(context)
                paths = context["source"]["paths"]
                derived_other = Path(paths["contacts"]).parent.parent
                self.assertEqual(Path(common.META), derived_other / "metadata")
                self.assertEqual(derived_other.name, context["universe"]["prefix"] + "_HarmonyGames_Other_Services")
                self.assertEqual(derived_other.parent.name, context["universe"]["folder"])
                index = Path(common.SNOW_IDX)
                self.assertEqual(index.name, "snowflake-snowflake.json")
                self.assertEqual(index.parts[-5:-2], ("references", "universes", key))
                self.assertEqual(index, common.universe_snowflake_index(WORKSPACE, key))
        source = (HERE / "common.py").read_text()
        for literal in ("HarmonyGames_Other_Services", "Evals/references/search_indexes", "universe_manifest.json"):
            self.assertNotIn(literal, source)

    # ---------------------------------------------------------------- universe-only facts
    def emitted_facts(self, key):
        context, _ = self.fixture(key)
        common = self.common(context)
        with patch.dict(sys.modules, {"common": common}):
            hazards = module_at("synthetic_hazards_" + key, HERE / "assemble_hazards_traps.py")
            integrations = module_at("synthetic_integrations_" + key, HERE / "assemble_integrations_conventions.py")
        app_title, app_examples = hazards.lookalike_app_titles()
        return "\n".join([
            hazards.metadata_artifact_title_suffix(),
            hazards.metadata_artifact_guidance(),
            json.dumps(hazards.shutdown_hazards(), default=str),
            json.dumps(hazards.stale_roadmap_fact(), default=str),
            app_title + " " + json.dumps(app_examples),
            hazards.calendar_lookalike_title(),
            hazards.SURNAME_TITLE,
            integrations.mirror_seeding_note(),
            integrations.jenkins_seeding_note("2026-02-12" if key == "normal" else None),
            integrations.coderabbit_seeding_note(),
        ])

    def test_synthcut_emits_no_normal_only_hard_coded_facts(self):
        text = self.emitted_facts("synthcut")
        for normal_only in ("Combo Fighter", "Combo-Fighters", "Trump Billionaires", "2026-02", "2026-01",
                            "2025-12-26", "2025-11-13", "2025-10-24", "cancelled 2026-02-12", "[normal-only]", "Lauren"):
            self.assertNotIn(normal_only, text)
        dates = re.findall(r"\d{4}-\d{2}(?:-\d{2})?", text)
        self.assertTrue(dates)
        self.assertTrue(all(day[:7] <= "2025-09" for day in dates), dates)

    def hazards_module(self, key):
        context, _ = self.fixture(key)
        common = self.common(context)
        with patch.dict(sys.modules, {"common": common}):
            return module_at("synthetic_hazard_rows_" + key, HERE / "assemble_hazards_traps.py")

    def test_hand_written_knowledge_is_normal_only(self):
        # Written from the Feb 14 data: an id can exist elsewhere while its content differs, so nothing is carried over.
        rows = [{"id": "R01", "source": "computed"}, {"id": "S08", "source": "computed+Scenario_Atlas"},
                {"id": "S07", "source": "Scenario_Atlas"}, {"id": "P03", "source": "Ask_Carriers+entities.json"}]
        synthcut, normal = self.hazards_module("synthcut"), self.hazards_module("normal")
        kept, dropped = synthcut.without_hand_written(rows)
        self.assertEqual(([r["id"] for r in kept], dropped), (["R01"], ["S08", "S07", "P03"]))
        self.assertEqual(synthcut.hand_written(["gcal:evt_x"]), [])
        self.assertEqual(normal.without_hand_written(rows), (rows, []))
        self.assertEqual(normal.hand_written(["gcal:evt_x"]), ["gcal:evt_x"])
        for key, allowed in (("normal", True), ("synthcut", False)):
            context, _ = self.fixture(key)
            with patch.dict(sys.modules, {"common": self.common(context)}):
                timeline = module_at("synthetic_static_" + key, HERE / "assemble_timeline.py")
            self.assertIs(timeline.hand_written_allowed(), allowed)   # gates the static narrative titles

    def test_dependencies_must_carry_this_builds_stamp(self):
        context, _ = self.fixture("synthcut")
        common = self.common(context)
        good = common.build_stamp()
        target = Path(common.OUT) / "entities.json"
        for stale in ({"universe": "normal"}, {"source_fingerprint": "fingerprint-normal"},
                      {"clock": "2026-02-14T00:00:00Z"}, {"build": "shared-kb-v1"}, None):
            with self.subTest(stale=stale):
                meta = {} if stale is None else {"_meta": {**good, **stale}}
                target.write_text(json.dumps({**meta, "entities": []}))
                with self.assertRaisesRegex(SystemExit, "entities.json"):
                    common.jload_kb("entities.json")
        target.write_text(json.dumps({"_meta": good, "entities": []}))
        self.assertEqual(common.jload_kb("entities.json")["entities"], [])

    def test_cache_intermediates_must_carry_this_builds_stamp(self):
        context, base = self.fixture("synthcut")
        common = self.common(context)
        cache = base / "cache"
        cache.mkdir()
        with patch.object(common, "CACHE", str(cache)):
            common.jdump({"rows": [1]}, cache / "kb_linear.json")      # writes the stamped sidecar
            self.assertEqual(common.jload_cache("kb_linear.json"), {"rows": [1]})
            sidecar = cache / "kb_linear.json.meta.json"
            for meta in ({**common.build_stamp(), "build": "per-universe-v0"},
                         {**common.build_stamp(), "universe": "normal"}, None):
                with self.subTest(meta=meta):
                    if meta is None:
                        sidecar.unlink()
                    else:
                        sidecar.write_text(json.dumps({"_meta": meta}))
                    with self.assertRaisesRegex(SystemExit, "kb_cache/kb_linear.json"):
                        common.jload_cache("kb_linear.json")

    def test_output_folder_must_be_the_selected_universes(self):
        context, base = self.fixture("synthcut")
        normal_out = base / "kb" / "by_universe" / "normal"
        normal_out.mkdir(parents=True)
        alias = base / "alias" / "by_universe" / "synthcut"            # right name, but it leads into normal's folder
        alias.parent.mkdir(parents=True)
        alias.symlink_to(normal_out, target_is_directory=True)
        for wrong in (normal_out, base / "kb" / "synthcut", alias):
            with self.subTest(wrong=str(wrong.relative_to(base))):
                wrong.mkdir(parents=True, exist_ok=True)
                context["source"]["kb_output_path"] = str(wrong)
                with self.assertRaisesRegex(SystemExit, "by_universe/synthcut"):
                    self.common(context)

    def test_feb14_base_checks_are_not_claimed_for_another_universe(self):
        normal, synthcut = self.hazards_module("normal"), self.hazards_module("synthcut")
        self.assertIn("803 cards", " ".join(normal.checked_and_clean()))
        text = " ".join(synthcut.checked_and_clean())
        for feb14_count in ("803 cards", "34 months", "31 pages"):
            self.assertNotIn(feb14_count, text)

    def test_beats_flagged_by_an_editorial_note_are_marked(self):
        context, base = self.fixture("synthcut")
        common = self.common(context)
        with patch.dict(sys.modules, {"common": common}):
            beats_module = module_at("synthetic_beats_synthcut", HERE / "pass_beats.py")
        story = base / "story.yaml"
        note = "    [STILL CONTAINS POST-CUTOFF REFERENCES — REMOVE THESE TOO: ]'\n"
        story.write_text("name: 'Story'\nbeats:\n"
                         "- id: b01\n  actor: a\n  action: 'Clean beat'\n  summary: 'fine'\n"
                         "- id: b02\n  actor: a\n  action: 'Channel wind-down\n\n\n" + note +
                         "- id: b03\n  actor: a\n  action: Rejections mount\n  summary: 'Through September\n" + note)
        name, beats = beats_module.parse_yaml_beats(str(story))
        self.assertEqual(name, "Story")
        self.assertEqual({b["id"]: bool(b.get("editorial_note")) for b in beats}, {"b01": False, "b02": True, "b03": True})

    def test_normal_still_emits_the_shutdown_facts(self):
        text = self.emitted_facts("normal")
        for expected in ("Combo Fighter", "Combo-Fighters", "Trump Billionaires", "2026-02-13", "2026-02-12", "2025-10-24"):
            self.assertIn(expected, text)

    def test_narrative_events_need_in_universe_evidence(self):
        for key in UNIVERSES:
            with self.subTest(key=key):
                context, _ = self.fixture(key)
                common = self.common(context)
                with patch.dict(sys.modules, {"common": common}):
                    timeline = module_at("synthetic_timeline_" + key, HERE / "assemble_timeline.py")
                horizon = common.CLOCK
                early = (horizon - datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
                late = (horizon + datetime.timedelta(minutes=1)).strftime("%Y-%m-%dT%H:%M:%SZ")

                def verify(rid):
                    when = {"early": early, "late": late}.get(rid)
                    return {"id": rid, "service": "slack", "when": when, "label": rid, "ok": rid in ("early", "late")}

                resolve = lambda rid: rid if rid in ("early", "late") else None
                kept = timeline.narrative_event("2025-01-01", "launch", "title", ["early"], resolve, verify)
                self.assertIsNotNone(kept)
                self.assertEqual(kept["services"], ["slack"])
                self.assertEqual(kept["orientation_only"], common.SEED_BOUND_ISO != common.CLOCK_ISO)
                self.assertIsNone(timeline.narrative_event("2025-01-01", "launch", "title", ["late"], resolve, verify))
                self.assertIsNone(timeline.narrative_event("2025-01-01", "launch", "title", ["missing"], resolve, verify))

    # ---------------------------------------------------------------- refusal / isolation
    def test_not_ready_source_refuses_with_install_hint(self):
        for key in UNIVERSES:
            with self.subTest(key=key):
                context, _ = self.fixture(key)
                context["source"].update(status="unavailable", reason="Source service directories missing", paths={})
                with self.assertRaises(SystemExit) as result:
                    self.common(context)
                message = str(result.exception)
                self.assertIn(context["universe"]["folder"], message)
                self.assertIn("Evals/UNIVERSE_MAP.md", message)

    def test_output_cannot_point_into_source_export(self):
        context, _ = self.fixture("normal")
        context["source"]["kb_output_path"] = context["source"]["paths"]["slack"] + "/generated"
        with self.assertRaisesRegex(SystemExit, "read-only service export"):
            self.common(context)

    def test_output_cannot_be_the_legacy_kb_root(self):
        context, _ = self.fixture("synthcut")
        context["source"]["kb_output_path"] = str(HERE.parent)
        self.assertTrue(Path(context["source"]["kb_output_path"]).is_dir())
        with self.assertRaises(SystemExit) as result:
            self.common(context)
        self.assertIn("legacy KB", str(result.exception))

    def test_build_never_writes_the_legacy_kb_root(self):
        before = self.root_snapshot()
        for key in UNIVERSES:
            context, _ = self.fixture(key)
            common = self.common(context)
            common.jdump({"universe": key}, Path(common.OUT) / "probe.json")
            self.assertTrue((Path(context["source"]["kb_output_path"]) / "probe.json").is_file())
        self.assertEqual(self.root_snapshot(), before)

    # ---------------------------------------------------------------- runner
    def test_run_all_stops_before_common_import_for_missing_source(self):
        runner = module_at("synthetic_kb_runner", HERE / "run_all.py")
        with patch.object(task_context, "load_context", side_effect=task_context.ContextError("missing historical source")), \
                patch.object(runner.runpy, "run_path") as run_pass:
            with self.assertRaises(SystemExit) as result:
                runner.main(["--task-dir", "/private/tmp/no-source-task"])
            self.assertEqual(result.exception.code, 2)
            run_pass.assert_not_called()

    def test_run_all_rejects_universe_mismatch(self):
        context, base = self.fixture("synthcut")
        runner = module_at("synthetic_kb_runner_mismatch", HERE / "run_all.py")
        stderr = io.StringIO()
        with patch.object(task_context, "load_context", return_value=context), \
                patch.dict(os.environ, {"TASK_AUTHORING_UNIVERSE": "normal"}), \
                patch.object(runner.runpy, "run_path") as run_pass, contextlib.redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as result:
                runner.main(["--task-dir", str(base)])
        self.assertEqual(result.exception.code, 2)
        self.assertIn("one universe per run", stderr.getvalue())
        run_pass.assert_not_called()

    def test_run_all_refuses_not_ready_source_with_install_hint(self):
        context, base = self.fixture("normal")
        context["source"].update(status="unavailable", reason="Source service directories missing", paths={})
        runner = module_at("synthetic_kb_runner_unready", HERE / "run_all.py")
        stderr = io.StringIO()
        with patch.object(task_context, "load_context", return_value=context), \
                patch.object(runner.runpy, "run_path") as run_pass, contextlib.redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as result:
                runner.main(["--task-dir", str(base)])
        self.assertEqual(result.exception.code, 2)
        self.assertIn("Universe_Normal", stderr.getvalue())
        self.assertIn("Evals/UNIVERSE_MAP.md", stderr.getvalue())
        run_pass.assert_not_called()

    def test_run_all_preflights_entities_for_partial_runs(self):
        # A stale entities.json stops a partial run that publishes KB files before its first step runs.
        context, base = self.fixture("synthcut")
        output = Path(context["source"]["kb_output_path"])
        (output / "entities.json").write_text(json.dumps({"_meta": {"universe": "normal"}, "entities": []}))
        runner = module_at("synthetic_kb_runner_partial", HERE / "run_all.py")
        with patch.object(task_context, "load_context", return_value=context), patch("os.makedirs"), \
                patch.dict(sys.modules), patch.object(runner.os, "chdir"), \
                patch.object(runner.runpy, "run_path") as run_pass:
            sys.modules.pop("common", None)
            with self.assertRaisesRegex(SystemExit, "entities.json"):
                runner.main(["--task-dir", str(base), "pass_slack", "assemble_hazards_traps"])
        run_pass.assert_not_called()


if __name__ == "__main__":
    unittest.main()

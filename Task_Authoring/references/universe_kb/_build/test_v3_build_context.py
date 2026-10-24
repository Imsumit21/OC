"""Synthetic KB build-context checks; never scan or rebuild the universe exports."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import task_context
import runtime_context


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BuildContextTests(unittest.TestCase):
    def fixture(self, folder, date="2026-02-14"):
        metadata = folder / "metadata"
        metadata.mkdir()
        snow = folder / "snow-index.json"
        snow.write_text("{}")
        manifest = folder / "manifest.json"
        data = {"kb_build_paths": {"metadata_path": str(metadata), "snowflake_index": str(snow)}}
        manifest.write_text(json.dumps(data))
        return {"universe_date_key": date, "freeze_utc": date + "T00:00:00Z", "context_hash": "test-context",
                "source": {"manifest": str(manifest), "kb_path": str(folder / "output"), "fingerprint": "test-source",
                           "mode": "shared-universe", "data_clock": "2026-02-14T00:00:00Z",
                           "paths": {service: str(folder / "services" / service) for service in task_context.SERVICES}}}

    def common(self, context):
        with patch.object(task_context, "load_context", return_value=context), patch("os.makedirs"):
            return module_at("synthetic_kb_common", HERE / "common.py")

    def test_paths_cache_clock_and_json_provenance(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            context = self.fixture(folder)
            common = self.common(context)
            self.assertEqual(common.CLOCK_ISO, "2026-02-14T00:00:00Z")
            self.assertEqual(common.SLACK, context["source"]["paths"]["slack"])
            self.assertEqual(common.OUT, str(folder / "output"))
            self.assertTrue(common.CACHE.endswith("2026-02-14/test-source"))
            (folder / "output").mkdir()
            artifact = folder / "output" / "artifact.json"
            common.jdump({"count": 2}, artifact)
            self.assertEqual(json.loads(artifact.read_text())["_meta"]["source_fingerprint"], "test-source")
            common.jdump([1, 2], artifact)
            self.assertEqual(json.loads(artifact.read_text()), [1, 2])
            self.assertEqual(json.loads(Path(str(artifact) + ".meta.json").read_text())["_meta"]["clock"], common.CLOCK_ISO)
            cache_mapping = folder / "cache-map.json"
            common.jdump({"record-1": {"count": 2}}, cache_mapping)
            self.assertEqual(list(json.loads(cache_mapping.read_text())), ["record-1"])
            self.assertEqual(json.loads(Path(str(cache_mapping) + ".meta.json").read_text())["_meta"]["source_fingerprint"], "test-source")

    def test_october_uses_same_export_without_manual_review_gate(self):
        with tempfile.TemporaryDirectory() as temp:
            context = self.fixture(Path(temp), date="2025-10-01")
            common = self.common(context)
            self.assertEqual(common.SLACK, context["source"]["paths"]["slack"])
            self.assertEqual(common.OUT, str(Path(context["source"]["kb_path"]) / "by_date" / "2025-10-01"))
            self.assertNotEqual(common.OUT, context["source"]["kb_path"])

    def test_dynamic_activity_months_and_freeze_boundary(self):
        for date, active, recent in (("2026-02-14", "active_feb_2026", "active_jan_2026_quiet_in_feb"),
                                     ("2025-10-01", "active_oct_2025", "active_sep_2025_quiet_in_oct")):
            with self.subTest(date=date), tempfile.TemporaryDirectory() as temp:
                common = self.common(self.fixture(Path(temp), date))
                with patch.dict(sys.modules, {"common": common}):
                    activity = module_at("synthetic_kb_activity", HERE / "assemble_activity.py")
                self.assertEqual(activity.ACTIVE_KEY, active)
                self.assertEqual(activity.RECENT_KEY, recent)
                self.assertTrue(common.before_clock("2024-01-01T00:00:00Z"))
                self.assertFalse(common.before_clock(common.CLOCK_ISO))
                self.assertFalse(common.before_clock("2027-01-01T00:00:00Z"))
                self.assertFalse(common.before_clock(None))

    def test_output_cannot_point_into_source_export(self):
        with tempfile.TemporaryDirectory() as temp:
            context = self.fixture(Path(temp))
            context["source"]["kb_path"] = context["source"]["paths"]["slack"] + "/generated"
            with self.assertRaisesRegex(SystemExit, "read-only service export"):
                self.common(context)

    def test_run_all_stops_before_common_import_for_missing_source(self):
        runner = module_at("synthetic_kb_runner", HERE / "run_all.py")
        with patch.object(task_context, "load_context", side_effect=task_context.ContextError("missing historical source")), \
                patch.object(runner.runpy, "run_path") as run_pass:
            with self.assertRaises(SystemExit) as result:
                runner.main(["--task-dir", "/private/tmp/no-source-task"])
            self.assertEqual(result.exception.code, 2)
            run_pass.assert_not_called()

    def test_shared_activity_is_limited_reference_without_future_departure(self):
        with tempfile.TemporaryDirectory() as temp:
            context = self.fixture(Path(temp), date="2025-10-01")
            data = {"_meta": {"clock": "2026-02-14T00:00:00Z"}, "people": {"person@example.com": {
                "name": "Example", "status_at_clock": "quiet_since_2025-10",
                "monthly_authored_total": {"2025-09": 12, "2025-10": 5, "2026-02": 3},
                "last_activity_by_service": {"slack": "2025-10-24", "gmail": "2025-09-20"},
                "departure_signals": {"last_authored_activity": "2025-10-24", "slack_channel_leaves": 6},
                "services": {"slack": {"monthly": {"2025-09": 12, "2025-10": 5}, "last": "2025-10-24", "messages": 17}}}},
                "summary": {"quiet_or_departed": [{"email": "person@example.com", "last_authored": "2025-10-24"}]},
                "seed_voice_candidates_feb_2026": [{"email": "other@example.com"}]}
            view = runtime_context.validate_kb(data, {"TASK_CONTEXT": context})
            person = view["people"]["person@example.com"]
            self.assertEqual(person["status_at_clock"], "activity_record_verification_required")
            self.assertEqual(person["monthly_authored_total"], {"2025-09": 12})
            self.assertIsNone(person["departure_signals"]["last_authored_activity"])
            self.assertIsNone(person["last_activity_by_service"]["slack"])
            self.assertEqual(person["last_activity_by_service"]["gmail"], "2025-09-20")
            self.assertNotIn("messages", person["services"]["slack"])
            self.assertEqual(view["summary"]["quiet_or_departed"], [])
            self.assertNotIn("seed_voice_candidates_feb_2026", view)
            self.assertTrue(view["_meta"]["reference_only"])
            self.assertEqual(view["_meta"]["reference_clock"], data["_meta"]["clock"])
            self.assertEqual(view["_meta"]["assigned_freeze"], context["freeze_utc"])
            self.assertEqual(data["people"]["person@example.com"]["status_at_clock"], "quiet_since_2025-10")

    def test_shared_timeline_filters_future_events_and_evidence(self):
        with tempfile.TemporaryDirectory() as temp:
            context = self.fixture(Path(temp), date="2025-10-01")
            data = {"_meta": {"clock": "2026-02-14T00:00:00Z"}, "spine": [
                {"date": "2025-09-01", "title": "Orientation", "evidence": [
                    {"when": "2025-09-02", "service": "slack"}, {"when": "2025-10-02", "service": "gmail"}]},
                {"date": "2025-10-01", "evidence": []}, {"date": "2026-02-09", "evidence": []}],
                "storyline_beats_2024_plus": [], "counts": {}}
            view = runtime_context.validate_kb(data, {"TASK_CONTEXT": context})
            self.assertEqual(len(view["spine"]), 1)
            self.assertTrue(view["spine"][0]["orientation_only"])
            self.assertEqual(view["spine"][0]["services"], ["slack"])
            self.assertEqual(view["counts"]["spine_events"], 1)
            self.assertEqual(len(data["spine"]), 3)

    def test_shared_entity_clears_later_activity_on_resolved_record(self):
        with tempfile.TemporaryDirectory() as temp:
            context = self.fixture(Path(temp), date="2025-10-01")
            data = {"_meta": {"clock": "2026-02-14T00:00:00Z"}, "entities": [{
                "last_activity": {"slack": "2025-10-24", "gmail": "2025-09-02"},
                "identities": {"slack": [{"id": "U1", "first_post": "2023-01-01", "last_post": "2026-02-13"}]}}]}
            view = runtime_context.validate_kb(data, {"TASK_CONTEXT": context})
            entity = view["entities"][0]
            self.assertTrue(entity["reference_only"])
            self.assertIsNone(entity["last_activity"]["slack"])
            self.assertEqual(entity["last_activity"]["gmail"], "2025-09-02")
            self.assertIsNone(entity["identities"]["slack"][0]["last_post"])

    def test_current_february_view_is_returned_unchanged(self):
        with tempfile.TemporaryDirectory() as temp:
            context = self.fixture(Path(temp))
            data = {"_meta": {"clock": "2026-02-14T00:00:00Z"}, "people": {"a": {"status_at_clock": "active_feb_2026"}}}
            self.assertIs(runtime_context.validate_kb(data, {"TASK_CONTEXT": context}), data)


if __name__ == "__main__":
    unittest.main()

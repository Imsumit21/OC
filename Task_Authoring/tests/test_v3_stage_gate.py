"""Regression checks for V3 provenance, fairness evidence and historical-source boundaries."""
import copy
import json
import os
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
import stage_gate as gate
import v3_artifact_checks as evidence


class V3EvidenceTests(unittest.TestCase):
    def setUp(self):
        cache = TOOLS.parent / "support" / "local_search" / "cache"
        cache.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(prefix="v3_stage_test_", dir=cache)
        self.td = Path(self.tmp.name)
        (self.td / "Working_Files").mkdir()
        (self.td / "source").mkdir()
        self.context = {"context_hash": "a" * 64, "assignment_hash": "b" * 64,
                        "policy_hash": "c" * 64, "persona_role": "Co-founder",
                        "freeze_utc": "2025-10-01T00:00:00Z", "difficulty_mode": "easy",
                        "source": {"paths": {"linear": str(self.td / "source")}}}
        (self.td / "04_Prompt.txt").write_text("Send the launch date and amount to the team.")
        (self.td / "09_Rubrics.json").write_text(json.dumps([{"criterion": "Reports the amount."}]))
        (self.td / "source" / "record.json").write_text(json.dumps({"id": "ENG-1", "amount": 42,
                                                                   "date": "2025-10-01T00:00:00Z"}))
        self.data = {"spec_version": "V3", "context_hash": self.context["context_hash"],
                     "rubric_hash": self.hash("09_Rubrics.json"), "prompt_hash": self.hash("04_Prompt.txt"),
                     "rubric_rows": [self.row()]}
        # Source selection belongs to runtime_context's integration tests. Isolate only the
        # bounded transport here while exercising field equality, ACL and date decisions.
        self.real_bounded_get = evidence._bounded_get
        self.reader = patch.object(evidence, "_bounded_get", side_effect=lambda service, path, root, pointer, task_dir:
                                   evidence._pointer(json.loads(path.read_text()), pointer))
        self.reader.start()

    def tearDown(self):
        self.reader.stop()
        self.tmp.cleanup()

    def hash(self, name):
        path = gate.slot_path(self.td, name)
        return gate.file_digest(path) if path.exists() else None

    def row(self):
        return {"criterion_id": "C1", "fact_id": "amount", "prompt_span": "amount",
                "accepted_outcomes": [42, "42.00"],
                "alternatives_review": "Reviewer accepts precise and decimal representations.",
                "source_records": [{"service": "linear", "id": "ENG-1",
                                    "source_file": str(self.td / "source" / "record.json"), "pointer": "/amount",
                                    "source_value": 42, "evidence_path": [{"service": "linear", "id": "ENG-1"}],
                                    "reachability_rationale": "The requested launch's linked ticket contains the amount."}]}

    def shared_source(self, mutable=False):
        self.context["source"].update(mode="shared-universe", data_clock="2026-02-14T00:00:00Z")
        source = self.data["rubric_rows"][0]["source_records"][0]
        source["temporal_evidence"] = {"recorded_at_pointer": "/recorded_at", "value_semantics": "fact",
                                       "mutable_state": mutable,
                                       "rationale": "The cited record was already available when this task is set."}
        path = self.td / "source" / "record.json"
        record = json.loads(path.read_text())
        record["recorded_at"] = "2025-09-30T20:00:00Z"
        path.write_text(json.dumps(record))
        return source, path, record

    def check(self, reachable=lambda service, record: (True, "verified"), stage="rubric-check"):
        (self.td / "Working_Files" / evidence.EVIDENCE_FILE).write_text(json.dumps(self.data))
        return {cid: (ok, detail) for cid, ok, detail in evidence.check_evidence(
            stage, self.td, self.context, self.hash, reachable, TOOLS.parent.parent)}

    def test_precise_and_decimal_outcomes_are_allowed(self):
        checks = self.check()
        self.assertTrue(checks["v3.rubric_evidence"][0], checks)

    def test_shared_february_export_can_support_october_facts(self):
        self.shared_source()
        self.assertTrue(self.check()["v3.rubric_evidence"][0])

    def test_shared_source_rejects_record_created_after_assigned_freeze(self):
        source, path, record = self.shared_source()
        record["recorded_at"] = "2025-10-02T00:00:00Z"
        path.write_text(json.dumps(record))
        self.assertIn("recorded after", self.check()["v3.rubric_evidence"][1])

    def test_future_deadline_allowed_but_future_completed_fact_rejected(self):
        source, path, record = self.shared_source()
        source.update(pointer="/date", source_value="2025-10-03T00:00:00Z")
        record["date"] = source["source_value"]
        path.write_text(json.dumps(record))
        self.assertIn("completed fact", self.check()["v3.rubric_evidence"][1])
        source["temporal_evidence"]["value_semantics"] = "future_deadline"
        self.assertTrue(self.check()["v3.rubric_evidence"][0])
        record["recorded_at"] = "2025-10-02T00:00:00Z"
        path.write_text(json.dumps(record))
        self.assertIn("recorded after", self.check()["v3.rubric_evidence"][1])

    def test_mutable_source_needs_evidenced_freeze_state_review(self):
        source, _, _ = self.shared_source(mutable=True)
        self.assertIn("creation time alone", self.check()["v3.rubric_evidence"][1])
        source["temporal_evidence"]["state_at_freeze_review"] = {
            "reviewer": "Author", "rationale": "A dated source version carries this same amount before the freeze.",
            "evidence_ids": ["ENG-1"]}
        self.assertTrue(self.check()["v3.rubric_evidence"][0])

    def test_timeless_contact_identity_does_not_require_a_timestamp(self):
        source, _, _ = self.shared_source()
        self.context["source"]["paths"]["contacts"] = str(self.td / "source")
        source["service"] = "contacts"
        source.update(pointer="/id", source_value="ENG-1")
        source["evidence_path"] = [{"service": "contacts", "id": "ENG-1"}]
        source["temporal_evidence"] = {"value_semantics": "directory_identity", "mutable_state": False,
                                       "rationale": "This is the stable recipient identifier in the contact directory."}
        self.assertTrue(self.check()["v3.rubric_evidence"][0])

    def test_task_fact_cannot_omit_shared_source_date_evidence(self):
        self.context["source"]["mode"] = "shared-universe"
        self.assertIn("temporal_evidence", self.check()["v3.rubric_evidence"][1])

    def test_role_review_must_match_assigned_role(self):
        name = "01_Scenario_Design.md"
        gate.slot_path(self.td, name).write_text("Current scenario content")
        self.data["role_reviews"] = {"scenario": {"artifact": name, "artifact_hash": self.hash(name),
                                                 "persona_role": "QA Lead", "reviewer": "Author",
                                                 "rationale": "Reviewed the scenario against source records.",
                                                 "source_ids": ["ENG-1"]}}
        self.assertFalse(self.check(stage="scenario")["v3.role_review"][0])

    def test_multiple_fair_outcomes_and_current_review_are_accepted(self):
        name = "04_Prompt_Writing_Brief.md"
        gate.slot_path(self.td, name).write_text("Two source-supported interpretations")
        self.data["outcome_reviews"] = {"prompt-writing": {"artifact": name, "artifact_hash": self.hash(name),
                                                          "reviewer": "Author", "rationale": "Both sources support fair readings.",
                                                          "accepted_outcomes": ["First reading", "Second reading"],
                                                          "alternatives_considered": ["Both included"]}}
        self.assertTrue(self.check(stage="prompt-writing")["v3.fair_outcomes_review"][0])
        gate.slot_path(self.td, name).write_text("An edited brief")
        self.assertFalse(self.check(stage="prompt-writing")["v3.fair_outcomes_review"][0])

    def test_manifest_context_cannot_cross_assignment(self):
        name = "01_Hardness_Manifest.draft.json"
        binding = {key: self.context[key] for key in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc", "difficulty_mode")}
        gate.slot_path(self.td, name).write_text(json.dumps({"assignment_context": binding}))
        ctx = gate.Ctx("scenario", self.td)
        ctx.v3, ctx.context = True, self.context
        with patch.object(evidence, "check_evidence", return_value=[]):
            gate.v3_checks(ctx)
        self.assertEqual("PASS", ctx.res[0]["status"])
        binding["difficulty_mode"] = "hard"
        gate.slot_path(self.td, name).write_text(json.dumps({"assignment_context": binding}))
        ctx = gate.Ctx("scenario", self.td)
        ctx.v3, ctx.context = True, self.context
        with patch.object(evidence, "check_evidence", return_value=[]):
            gate.v3_checks(ctx)
        self.assertEqual("FAIL", ctx.res[0]["status"])

    def test_changed_expected_source_value_blocks(self):
        self.data["rubric_rows"][0]["source_records"][0]["source_value"] = 43
        self.assertFalse(self.check()["v3.rubric_evidence"][0])

    def test_edited_rubric_invalidates_its_review(self):
        (self.td / "09_Rubrics.json").write_text(json.dumps([{"criterion": "Reports another amount."}]))
        self.assertIn("rubric_hash", self.check()["v3.rubric_evidence"][1])

    def test_hidden_deciding_record_blocks(self):
        self.assertFalse(self.check(lambda service, record: (False, "hidden by ACL"))["v3.rubric_evidence"][0])

    def test_three_criteria_cannot_grade_same_fact(self):
        (self.td / "09_Rubrics.json").write_text(json.dumps([{"criterion": f"Criterion {i}"} for i in range(3)]))
        self.data["rubric_hash"] = self.hash("09_Rubrics.json")
        self.data["rubric_rows"] = [dict(copy.deepcopy(self.row()), criterion_id=f"C{i + 1}") for i in range(3)]
        self.assertFalse(self.check()["v3.fact_duplication"][0])

    def test_both_calendar_days_must_be_accepted_without_prompt_timezone(self):
        row = self.data["rubric_rows"][0]
        row["source_records"][0].update(pointer="/date", source_value="2025-10-01T00:00:00Z")
        row["dates"] = {"instant_utc": "2025-10-01T00:00:00Z", "pacific": "2025-09-30", "utc": "2025-10-01",
                        "accepted_dates": ["2025-09-30"], "prompt_timezone": None}
        self.assertFalse(self.check()["v3.rubric_evidence"][0])
        row["dates"]["accepted_dates"].append("2025-10-01")
        self.assertTrue(self.check()["v3.rubric_evidence"][0])

    def test_attachment_cannot_supply_deciding_evidence(self):
        (self.td / "source" / "record.json").write_text(json.dumps({"attachments": [{"amount": 42}]}))
        self.data["rubric_rows"][0]["source_records"][0]["pointer"] = "/attachments/0/amount"
        self.assertIn("attachment", self.check()["v3.rubric_evidence"][1])

    def test_source_outside_selected_export_blocks(self):
        self.context["source"]["paths"] = {}
        self.assertIn("outside", self.check()["v3.rubric_evidence"][1])

    def test_cited_service_cannot_use_another_service_root(self):
        self.data["rubric_rows"][0]["source_records"][0]["service"] = "github"
        self.assertIn("cited service", self.check()["v3.rubric_evidence"][1])

    def test_bounded_transport_rejects_truncated_field(self):
        returned = {"items": {"value": {"encoding": "rendered-json", "truncated": True, "text": '"partial'}}}
        with patch.object(evidence.subprocess, "run", return_value=types.SimpleNamespace(
                returncode=0, stdout=json.dumps(returned), stderr="")):
            with self.assertRaisesRegex(ValueError, "truncated"):
                self.real_bounded_get("linear", self.td / "source" / "record.json", self.td / "source", "/amount", self.td)

    def test_bounded_transport_rejects_ancestor_trash_flag(self):
        returned = {"items": {"value": {"encoding": "rendered-json", "truncated": False, "text": "42"},
                               "flag-0-trashed": {"encoding": "rendered-json", "truncated": False, "text": "true"}}}
        with patch.object(evidence.subprocess, "run", return_value=types.SimpleNamespace(
                returncode=0, stdout=json.dumps(returned), stderr="")):
            with self.assertRaisesRegex(ValueError, "Trash"):
                self.real_bounded_get("linear", self.td / "source" / "record.json", self.td / "source", "/amount", self.td)

    def test_whole_trashed_object_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Trash"):
            evidence._pointer({"trashed": True}, "")

    def test_new_later_review_does_not_stale_scenario_certificate(self):
        self.data["role_reviews"] = {"scenario": {"rationale": "current"}}
        self.check()
        before = evidence.review_digest("scenario", self.td)
        self.data["role_reviews"]["prompt-check"] = {"rationale": "later review"}
        self.check()
        self.assertEqual(before, evidence.review_digest("scenario", self.td))
        self.data["role_reviews"]["scenario"]["rationale"] = "changed current review"
        self.check()
        self.assertNotEqual(before, evidence.review_digest("scenario", self.td))

    def test_same_mtime_input_edit_stales_certificate(self):
        (self.td / "00_Assigments.md").write_text("spec_version: V3\n")
        (self.td / "Working_Files" / "01_Scenario_Design.md").write_text("scenario")
        ctx = gate.Ctx("scenario", self.td)
        ctx.v3, ctx.context = True, self.context
        certificate = gate.certificate_digests(ctx)
        assignment = self.td / "00_Assigments.md"
        stamp = assignment.stat().st_mtime
        assignment.write_text("spec_version: V3\nchanged: yes\n")
        os.utime(assignment, (stamp, stamp))
        self.assertTrue(any("00_Assigments.md" in item for item in gate.certificate_staleness(ctx, "scenario", certificate)))

    def test_missing_configured_source_stops_before_stage_handler(self):
        (self.td / "00_Assigments.md").write_text("spec_version: V3\n")
        fake = types.SimpleNamespace(load_context=lambda *args, **kwargs: (_ for _ in ()).throw(ValueError("Configured source export missing")),
                                     is_v3_assignment=lambda text: True)
        with patch.dict(sys.modules, {"task_context": fake}), patch.dict(gate.STAGES["scenario"], {"fn": lambda ctx: self.fail("handler ran")}):
            ctx = gate.run_stage("scenario", self.td)
        self.assertEqual("FAIL", gate.verdict_of(ctx))
        self.assertEqual(["assignment.v3_context"], [r["id"] for r in ctx.res])

    def test_raw_platform_intake_uses_normalized_persona_and_horizon(self):
        (self.td / "00_Assigments.md").write_text("🧑 Persona\nFrederick Stone\nRole: Co-founder\n📋 Task Type\nnormal\n")
        ctx = gate.Ctx("scenario", self.td)
        ctx.context = dict(self.context, persona_key="frederick_stone", horizon="Normal Horizon")
        ctx._pv = types.SimpleNamespace(resolve_persona=lambda key: {"persona_key": key})
        self.assertEqual({"persona_key": "frederick_stone"}, ctx.persona())
        self.assertEqual(("Normal Horizon", "normal"), gate.tier_profile(ctx))

    def test_missing_precheck_model_is_not_labeled_opus(self):
        path = self.td / "06_PreCheck_Trajectory"
        path.mkdir()
        (path / "trajectory.json").write_text('{"run":"complete"}')
        ctx = gate.Ctx("release", self.td)
        gate.v3_precheck(ctx)
        self.assertFalse(ctx.res[0]["status"] == "PASS")

    def test_complete_precheck_checks_actual_model_and_mixed_models(self):
        path = self.td / "06_PreCheck_Trajectory"
        path.mkdir()
        events = [{"type": "system", "subtype": "init", "model": "claude-opus-5-5"},
                  {"type": "result", "subtype": "success", "is_error": False}]
        trajectory = path / "trajectory.json"
        trajectory.write_text(json.dumps(events))
        ctx = gate.Ctx("release", self.td)
        gate.v3_precheck(ctx)
        self.assertEqual("PASS", ctx.res[0]["status"])
        events.insert(1, {"type": "assistant", "message": {"model": "claude-opus-4-8"}})
        trajectory.write_text(json.dumps(events))
        ctx = gate.Ctx("release", self.td)
        gate.v3_precheck(ctx)
        self.assertEqual("FAIL", ctx.res[0]["status"])

    def test_init_metadata_without_completed_run_cannot_pass(self):
        path = self.td / "06_PreCheck_Trajectory"
        path.mkdir()
        (path / "trajectory.json").write_text(json.dumps([{"type": "system", "subtype": "init", "model": "claude-opus-5-5"}]))
        ctx = gate.Ctx("release", self.td)
        gate.v3_precheck(ctx)
        self.assertEqual("FAIL", ctx.res[0]["status"])


if __name__ == "__main__":
    unittest.main()

"""Regression checks for V3 provenance, fairness evidence and historical-source boundaries."""
import copy
import hashlib
import json
import os
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
import selftest_sandbox  # noqa: E402  (temp folders under the scratch root, never the shared cache)
import stage_gate as gate
import v3_artifact_checks as evidence


class V3EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = selftest_sandbox.scratch_tmp("v3_stage_test_")      # support/scratch/, unique, removed after
        self.td = Path(self.tmp.name)
        (self.td / "Working_Files").mkdir()
        (self.td / "source").mkdir()
        self.context = {"context_hash": "a" * 64, "assignment_hash": "b" * 64,
                        "policy_hash": "c" * 64, "persona_role": "Co-founder",
                        "freeze_utc": "2025-10-01T00:00:00Z", "difficulty_mode": "easy",
                        "universe": {"key": "normal", "clock_utc": "2026-02-14T00:00:00Z",
                                     "clock_line": "Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)",
                                     "shutdown_rules_apply": True, "persona_today": "2026-02-14"},
                        "source": {"kb_status": "bound", "paths": {"linear": str(self.td / "source")}}}
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
        self.context["source"].update(mode="universe", universe="normal", kb_status="bound",
                                      data_clock="2026-02-14T00:00:00Z")
        source = self.data["rubric_rows"][0]["source_records"][0]
        source["temporal_evidence"] = {"recorded_at_pointer": "/recorded_at", "value_semantics": "fact",
                                       "mutable_state": mutable,
                                       "rationale": "The cited record was already available when this task is set."}
        path = self.td / "source" / "record.json"
        record = json.loads(path.read_text())
        record["recorded_at"] = "2025-09-30T20:00:00Z"
        path.write_text(json.dumps(record))
        return source, path, record

    def synthcut_source(self):
        """The Oct 1 universe: freeze 00:00Z is the seed bound; 07:00Z is only the data horizon."""
        source, path, record = self.shared_source()
        self.context["universe"].update(key="synthcut", clock_utc="2025-10-01T07:00:00Z",
                                        clock_line="Clock: 2025-10-01 07:00 UTC, Oct 1, 2025 (synthcut)",
                                        persona_today="2025-10-01")
        self.context["source"].update(universe="synthcut", data_clock="2025-10-01T07:00:00Z")
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

    def test_synthcut_recorded_at_is_bounded_by_the_seed_freeze_not_the_data_horizon(self):
        # The seed bound is 00:00Z; base data exists up to 07:00Z and must never be cited as available.
        source, path, record = self.synthcut_source()
        self.assertEqual("2025-10-01T00:00:00Z", self.context["freeze_utc"])
        self.assertEqual("2025-10-01T07:00:00Z", self.context["universe"]["clock_utc"])
        for stamp in ("2025-10-01T03:00:00Z", "2025-09-30T20:00:00-07:00", "2025-10-01T06:59:59Z"):
            record["recorded_at"] = stamp
            path.write_text(json.dumps(record))
            self.assertIn("recorded after", self.check()["v3.rubric_evidence"][1], stamp)
        for stamp in ("2025-10-01T00:00:00Z", "2025-09-30T23:59:59Z"):
            record["recorded_at"] = stamp
            path.write_text(json.dumps(record))
            self.assertTrue(self.check()["v3.rubric_evidence"][0], stamp)

    def test_synthcut_completed_fact_inside_the_data_horizon_is_rejected(self):
        source, path, record = self.synthcut_source()
        source.update(pointer="/date", source_value="2025-10-01T03:00:00Z")
        record["date"] = source["source_value"]
        path.write_text(json.dumps(record))
        self.assertIn("completed fact", self.check()["v3.rubric_evidence"][1])
        source["temporal_evidence"]["value_semantics"] = "future_deadline"
        self.assertTrue(self.check()["v3.rubric_evidence"][0])

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
        self.context["source"]["mode"] = "universe"
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


class InjectionLintTests(unittest.TestCase):
    """hg.py lint consumption: the eval linter exits 0 even with FAIL flags, so the gate reads counts/flags."""

    def setUp(self):
        self.tmp = selftest_sandbox.scratch_tmp("v3_injection_lint_")
        self.td = Path(self.tmp.name)
        self.sql = self.td / "01_Universe_Inject.sql"
        self.sql.write_text("INSERT INTO gmail.gmail_messages (id, subject) VALUES ('m1', 'Clock');\n")
        self.doc_path = self.td / "01_Grounding_Dossier.md"

    def tearDown(self):
        self.tmp.cleanup()

    def payload(self, **kw):
        out = {"tool": "hg_injection_lint", "version": "injection-lint-v1", "sql": str(self.sql),
               "sha256": hashlib.sha256(self.sql.read_bytes()).hexdigest(), "universe": "normal",
               "clock": "2026-02-14T00:00:00Z", "checks": {},
               "counts": {"FAIL": 0, "CHECK": 0, "INFO": 1, "by_check": {}},
               "flags": [], "info": [{"check": "generated_fts_column"}], "note": ""}
        out.update(kw)
        return out

    def run_lint(self, payload, review="## Self-review\n\n- Unresolved: none\n", rc=0):
        self.doc_path.write_text("# Grounding dossier\n\n" + review)
        ctx = gate.Ctx("injection", self.td)
        ctx.v3 = True
        doc = gate.Doc(self.doc_path, "01_Grounding_Dossier.md")
        with patch.object(gate, "run_tool", return_value=(rc, json.dumps(payload), "")):
            gate.injection_lint(ctx, doc, "01_Universe_Inject.sql")
        return {r["id"]: r for r in ctx.res}

    def test_fail_flag_blocks_with_the_flag_locator(self):
        got = self.run_lint(self.payload(
            counts={"FAIL": 1, "CHECK": 0, "INFO": 0, "by_check": {}},
            flags=[{"check": "post_clock_timestamp", "severity": "FAIL", "line": 12,
                    "table": "gmail.gmail_messages", "column": "internal_date"}]))
        self.assertEqual("FAIL", got["tool.injection_lint"]["status"])
        self.assertIn("post_clock_timestamp L12 gmail.gmail_messages.internal_date",
                      got["tool.injection_lint"]["detail"])

    def test_check_flag_without_disposition_blocks(self):
        got = self.run_lint(self.payload(
            counts={"FAIL": 0, "CHECK": 1, "INFO": 0, "by_check": {"weekend_timestamp": 1}},
            flags=[{"check": "weekend_timestamp", "severity": "CHECK", "line": 40,
                    "table": "slack.slack_messages", "column": "ts"}]))
        self.assertEqual("FAIL", got["tool.injection_lint"]["status"])
        self.assertIn("weekend_timestamp L40", got["tool.injection_lint"]["detail"])

    def test_check_flag_with_disposition_passes_and_reports_info(self):
        got = self.run_lint(self.payload(
            counts={"FAIL": 0, "CHECK": 1, "INFO": 3, "by_check": {"weekend_timestamp": 1}},
            flags=[{"check": "weekend_timestamp", "severity": "CHECK", "line": 40,
                    "table": "slack.slack_messages", "column": "ts"}]),
            review="## Self-review\n\n- LINT weekend_timestamp L40: accepted - a Saturday post, dated before the clock.\n"
                   "- Unresolved: none\n")
        self.assertEqual("PASS", got["tool.injection_lint"]["status"])
        self.assertIn("3 INFO", got["tool.injection_lint"]["detail"])

    def test_each_check_flag_needs_its_own_line(self):
        got = self.run_lint(self.payload(
            counts={"FAIL": 0, "CHECK": 2, "INFO": 0, "by_check": {"grader_language": 2}},
            flags=[{"check": "grader_language", "severity": "CHECK", "line": 2,
                    "table": "gmail.gmail_messages", "column": "subject"},
                   {"check": "grader_language", "severity": "CHECK", "line": 100,
                    "table": "gmail.gmail_messages", "column": "body"}]),
            review="## Self-review\n\n- LINT grader_language L2: accepted - in-world wording.\n")
        self.assertEqual("FAIL", got["tool.injection_lint"]["status"])
        self.assertIn("grader_language L100", got["tool.injection_lint"]["detail"])

    def test_two_distinct_flags_on_one_line_need_two_dispositions(self):
        # Verify-gate finding: (check, line) is not a flag identity; distinct flags on one SQL line each need a line.
        flags = [{"check": "grader_language", "severity": "CHECK", "line": 1, "table": "slack.slack_messages",
                  "column": "text", "message": "first occurrence"},
                 {"check": "grader_language", "severity": "CHECK", "line": 1, "table": "slack.slack_messages",
                  "column": "attachments_json", "message": "second independent occurrence"}]
        counts = {"FAIL": 0, "CHECK": 2, "INFO": 0, "by_check": {"grader_language": 2}}
        one = self.run_lint(self.payload(counts=counts, flags=flags),
                            review="## Self-review\n\n- LINT grader_language L1: first one reviewed.\n")
        self.assertEqual("FAIL", one["tool.injection_lint"]["status"])
        two = self.run_lint(self.payload(counts=counts, flags=flags),
                            review="## Self-review\n\n- LINT grader_language L1: text is a real customer quote.\n"
                                   "- LINT grader_language L1: the attachment caption is the same quote.\n")
        self.assertEqual("PASS", two["tool.injection_lint"]["status"])
        # Reports differing only in 'also' are distinct flags: two lines needed.
        also_a = dict(flags[0], also={"count": 1, "records": ["m2"]})
        also_b = dict(flags[0], also={"count": 1, "records": ["m9"]})
        also_one = self.run_lint(self.payload(counts=counts, flags=[also_a, also_b]),
                                 review="## Self-review\n\n- LINT grader_language L1: reviewed m2.\n")
        self.assertEqual("FAIL", also_one["tool.injection_lint"]["status"])
        also_two = self.run_lint(self.payload(counts=counts, flags=[also_a, also_b]),
                                 review="## Self-review\n\n- LINT grader_language L1: reviewed m2.\n"
                                        "- LINT grader_language L1: reviewed m9.\n")
        self.assertEqual("PASS", also_two["tool.injection_lint"]["status"])
        # Byte-identical duplicate reports are one flag and need one line.
        dup = self.run_lint(self.payload(counts={"FAIL": 0, "CHECK": 2, "INFO": 0, "by_check": {}},
                                         flags=[flags[0], dict(flags[0])]),
                            review="## Self-review\n\n- LINT grader_language L1: reviewed.\n")
        self.assertEqual("PASS", dup["tool.injection_lint"]["status"])

    def test_also_records_are_covered_by_the_parent_flags_line(self):
        got = self.run_lint(self.payload(
            counts={"FAIL": 0, "CHECK": 1, "INFO": 0, "by_check": {"grader_language": 1}},
            flags=[{"check": "grader_language", "severity": "CHECK", "line": 2,
                    "table": "gmail.gmail_messages", "column": "subject",
                    "also": {"count": 2, "records": ["m2", "m3"]}}]),
            review="## Self-review\n\n- LINT grader_language L2: accepted - the same hit in two later rows.\n")
        self.assertEqual("PASS", got["tool.injection_lint"]["status"])

    def test_error_payload_blocks(self):
        got = self.run_lint({"error": "universe data missing", "question": "Which universe date?"})
        self.assertEqual("FAIL", got["tool.injection_lint"]["status"])
        self.assertIn("universe data missing", got["tool.injection_lint"]["detail"])

    def test_stale_sha256_blocks(self):
        got = self.run_lint(self.payload(sha256="0" * 64))
        self.assertEqual("FAIL", got["tool.injection_lint"]["status"])
        self.assertIn("stale", got["tool.injection_lint"]["detail"])

    def test_short_sha256_prefix_is_not_a_binding(self):
        prefix = hashlib.sha256(self.sql.read_bytes()).hexdigest()[:12]
        got = self.run_lint(self.payload(sha256=prefix))
        self.assertEqual("FAIL", got["tool.injection_lint"]["status"])
        self.assertIn("stale", got["tool.injection_lint"]["detail"])

    def test_nonzero_exit_blocks_even_with_parseable_json(self):
        for rc in (1, 2, 3, 127, -9):  # any unsuccessful status, not only the linter's documented 1 and 2
            got = self.run_lint(self.payload(), rc=rc)
            self.assertEqual("FAIL", got["tool.injection_lint"]["status"], rc)
            self.assertIn(f"exited {rc}", got["tool.injection_lint"]["detail"])


class KbStatusTests(unittest.TestCase):
    """source.kb_status: bound blocks, reference-only WARNs membership, unavailable requires record locators."""

    def setUp(self):
        self.tmp = selftest_sandbox.scratch_tmp("v3_kb_status_")
        self.addCleanup(self.tmp.cleanup)
        self.td = Path(self.tmp.name)
        self.kb = {"integrations.json": {"integrations": [{"id": "INT-01", "source": "slack"}]}}
        self.context = {"context_hash": "d" * 64, "freeze_utc": "2025-10-01T00:00:00Z",
                        "difficulty_mode": "hard",
                        "universe": {"key": "synthcut", "clock_utc": "2025-10-01T07:00:00Z",
                                     "clock_line": "Clock: 2025-10-01 07:00 UTC, synthcut"},
                        "source": {"mode": "universe", "universe": "synthcut", "kb_status": "bound",
                                   "kb_path": None, "paths": {}}}

    def ctx(self, status):
        self.context["source"]["kb_status"] = status
        ctx = gate.Ctx("scenario", self.td)
        ctx.v3 = True
        ctx.context = copy.deepcopy(self.context)
        return ctx

    def doc(self, body):
        path = self.td / "01_Scenario_Design.md"
        path.write_text(body)
        return gate.Doc(path, "01_Scenario_Design.md")

    def test_reference_only_downgrades_membership_to_warn(self):
        ctx = self.ctx("reference-only")
        doc = self.doc("# Scenario\n\n## Integrations / companions\n\n- INT-99 listed for Slack\n")
        with patch.object(gate, "kb", side_effect=lambda name: self.kb[name]):
            gate.kb_gate(ctx, "kb.integrations", gate.kb_integrations, doc, r"integration|companion", {"slack"})
        res = {r["id"]: r for r in ctx.res}
        self.assertEqual("WARN", res["kb.integrations"]["status"], res["kb.integrations"]["detail"])
        self.assertFalse(res["kb.integrations"]["blocking"])
        self.assertIn("reference-only", res["kb.integrations"]["detail"])

    def test_unavailable_warns_membership_and_blocks_without_locators(self):
        ctx = self.ctx("unavailable")
        doc = self.doc("# Scenario\n\n## Coherence audit\n\n- temporal: stale status after the handoff\n")
        boom = AssertionError("KB read while source.kb_status is unavailable")
        with patch.object(gate, "kb", side_effect=boom):
            gate.kb_gate(ctx, "kb.coherence_hazards", gate.kb_hazards, doc, r"coherence")
            gate.kb_locators(ctx, doc, [("coherence audit", r"coherence")])
        res = {r["id"]: r for r in ctx.res}
        self.assertEqual("WARN", res["kb.coherence_hazards"]["status"])
        self.assertFalse(res["kb.coherence_hazards"]["blocking"])
        self.assertIn("KB unavailable for synthcut", res["kb.coherence_hazards"]["detail"])
        self.assertEqual("FAIL", res["evidence.kb_locators"]["status"])
        self.assertTrue(res["evidence.kb_locators"]["blocking"])
        # a record locator clears the blocking check
        ctx = self.ctx("unavailable")
        doc = self.doc("# Scenario\n\n## Coherence audit\n\n- temporal: ENG-101 carries the stale status\n")
        with patch.object(gate, "kb", side_effect=boom):
            gate.kb_locators(ctx, doc, [("coherence audit", r"coherence")])
        self.assertEqual("PASS", {r["id"]: r for r in ctx.res}["evidence.kb_locators"]["status"])

    def test_kb_catalog_ids_are_not_record_locators(self):
        ctx = self.ctx("unavailable")
        boom = AssertionError("KB read while source.kb_status is unavailable")
        doc = self.doc("# Scenario\n\n## Integrations / companions\n\n- INT-01 covers Slack\n")
        with patch.object(gate, "kb", side_effect=boom):
            gate.kb_locators(ctx, doc, [("integrations / companions", r"integration|companion")])
        res = {r["id"]: r for r in ctx.res}
        self.assertEqual("FAIL", res["evidence.kb_locators"]["status"])
        for locator in ("ENG-101", "1700000000.000100", "19f8c2a1b4d6e8f0a2c4b6d8e0f2a4c6"):
            ctx = self.ctx("unavailable")
            doc = self.doc("# Scenario\n\n## Integrations / companions\n\n- " + locator + " covers Slack\n")
            with patch.object(gate, "kb", side_effect=boom):
                gate.kb_locators(ctx, doc, [("integrations / companions", r"integration|companion")])
            self.assertEqual("PASS", {r["id"]: r for r in ctx.res}["evidence.kb_locators"]["status"], locator)

    def test_retired_shared_universe_mode_blocks(self):
        (self.td / "00_Assigments.md").write_text("spec_version: V3\n")
        for mode, want in (("universe", "PASS"), ("shared-universe", "FAIL")):
            ctxd = {**copy.deepcopy(self.context), "persona_name": "Ada Lopez", "persona_role": "QA Lead",
                    "difficulty_cap": 0.85, "source": {**copy.deepcopy(self.context["source"]), "mode": mode}}
            fake = types.SimpleNamespace(load_context=lambda *a, _c=ctxd, **k: _c,
                                         is_v3_assignment=lambda text: True)
            with patch.dict(sys.modules, {"task_context": fake,
                                          "runtime_context": types.SimpleNamespace(activate=lambda *a, **k: None)}):
                ctx = gate.Ctx("scenario", self.td)
                gate.assignment_context(ctx)
            res = {r["id"]: r for r in ctx.res}
            self.assertEqual(want, res["assignment.source_mode"]["status"], mode)


@unittest.skipUnless((TOOLS.parents[1] / "Universe_SynthCut").is_dir(), "needs the synth-cut universe data installed")
class SqlLintSeamTests(unittest.TestCase):
    """The gate's sql_lint re-run is the seam where a synth-cut seed is still bound to the 00:00Z freeze."""

    def setUp(self):
        self.tmp = selftest_sandbox.scratch_tmp("v3_sql_lint_seam_")
        self.addCleanup(self.tmp.cleanup)
        self.td = Path(self.tmp.name)
        # A synth-cut platform paste (sql_lint needs only the task context, not the installed universe data).
        (self.td / "00_Assigments.md").write_text(
            "🏢 Business Function\nExecutive\n🧑 Persona\nFrederick Stone\nRole: Co-founder\n🎯 Competency\n"
            "Corporate Ops\n🛠️ Task Skill\nAuthoring\n📋 Task Type\nlong-horizon\n🎚️ Difficulty Mode\neasy\n"
            "📅 Universe Date\nOctober 1, 2025 07:00\n")
        self.sql = self.td / "01_Universe_Inject.sql"
        self.sql.write_text("-- Are you planning to inject? Yes\n"
                            "INSERT INTO gcal.gcal_events (event_id, calendar_id, created) VALUES "
                            "('evt_0123456789abcdef012345', 'cal1', '2025-10-01T03:00:00Z');\n")
        self.doc_path = self.td / "01_Grounding_Dossier.md"
        self.doc_path.write_text("# Grounding dossier\n\n```text\nsql_lint: errors: 1  warnings: 0\n```\n")

    def test_rerun_fails_when_the_only_timestamp_is_after_the_seed_freeze(self):
        ctx = gate.Ctx("injection", self.td)
        doc = gate.Doc(self.doc_path, "01_Grounding_Dossier.md")
        with patch.dict(os.environ, {"TASK_AUTHORING_TASK_DIR": str(self.td)}), \
                patch.object(gate, "TASK_CONTEXT", {"context_hash": "e" * 64}, create=True):
            result = gate.rerun_sql_lint(ctx, doc, "01_Universe_Inject.sql")
        res = {r["id"]: r for r in ctx.res}["tool.sql_lint"]
        self.assertEqual("FAIL", res["status"])
        # The paste matches the re-run, so the block is the re-run's error — not a missing or stale paste.
        self.assertEqual("re-run has 1 error(s)", res["detail"])
        self.assertEqual(1, len(result["errors"]))
        self.assertIn("after the assigned clock 2025-10-01T00:00:00+00:00", result["errors"][0]["msg"])


if __name__ == "__main__":
    unittest.main()

"""Focused V3 difficulty-policy regressions; run with python3 -m unittest discover -s Task_Authoring/tools -p test_difficulty_v3.py."""
import copy
import json
from pathlib import Path
import tempfile
import selftest_sandbox
import unittest

import difficulty_stats as stats


class DifficultyV3Tests(unittest.TestCase):
    def matrix(self, passes, mode="easy", calls=120):
        return {
            "spec_version": "V3", "task_type": "long-horizon", "difficulty_mode": mode,
            "rubrics": [{"id": f"R{i}", "weight": 1} for i in range(100)],
            "rollouts": [{"id": f"run-{number}", "status": "completed", "tool_calls": calls,
                          "models": ["claude-opus-5-5"], "model_source": f"trajectory:run-{number}.json",
                          "model_check": {"v3_valid": True, "mixed_model": False, "fallback_events": [],
                                          "models": ["claude-opus-5-5"]},
                          "results": {f"R{i}": i < passed for i in range(100)}}
                         for number, passed in enumerate(passes, 1)],
        }

    def test_assigned_cap_boundaries(self):
        for mode, cap in (("easy", 90), ("medium", 85), ("hard", 70)):
            for score, expected in ((cap - 1, "PASS"), (cap, "FAIL"), (cap + 1, "FAIL")):
                with self.subTest(mode=mode, score=score):
                    gate = stats.compute(self.matrix([score] * 6, mode))["gates"]["avg_weighted_pass_rate"]
                    self.assertTrue(gate["verdict"].startswith(expected), gate)

    def test_full_pass_operational_count(self):
        for count, expected in ((4, "PASS"), (5, "FAIL"), (6, "FAIL")):
            with self.subTest(count=count):
                gate = stats.compute(self.matrix([100] * count + [20] * (6 - count)))["gates"]["pass_at_1"]
                self.assertTrue(gate["verdict"].startswith(expected), gate)
                self.assertIn(f"{count}/6 full passes", gate["value"])

    def test_six_slots_include_errors_without_zero_scores(self):
        data = self.matrix([80] * 6)
        for ro in data["rollouts"][-2:]:
            ro.update(status="errored")
            ro.pop("results")
        result = stats.compute(data)
        self.assertEqual(result["gates"]["errored_runs"]["verdict"], "PASS")
        self.assertTrue(result["gates"]["avg_weighted_pass_rate"]["value"].startswith("80.0%"))
        self.assertEqual(result["denominators"], {"rollout_slots": 6, "completed_scores": 4,
                         "errored_excluded": 2, "full_pass_gate": 6})
        self.assertIn("never zero-scored", stats.to_markdown(result, data))
        data["rollouts"][3]["status"] = "errored"
        self.assertTrue(stats.compute(data)["gates"]["errored_runs"]["verdict"].startswith("FAIL"))

    def test_invalid_slot_mode_and_result_inputs(self):
        baseline = self.matrix([80] * 6)
        broken = []
        no_mode = copy.deepcopy(baseline)
        no_mode.pop("difficulty_mode")
        broken.append(no_mode)
        missing = copy.deepcopy(baseline)
        missing["rollouts"].pop()
        broken.append(missing)
        duplicate = copy.deepcopy(baseline)
        duplicate["rollouts"][1]["id"] = "run-1"
        broken.append(duplicate)
        negative = copy.deepcopy(baseline)
        negative["rollouts"][0]["tool_calls"] = -1
        broken.append(negative)
        string_result = copy.deepcopy(baseline)
        string_result["rollouts"][0]["results"]["R0"] = "false"
        broken.append(string_result)
        for data in broken:
            with self.assertRaises(ValueError):
                stats.compute(data)

    def test_corrected_view_determines_v3_verdict(self):
        data = self.matrix([100] * 5 + [20])
        data["rollouts"][4]["judge_corrections"] = {f"R{i}": False for i in range(30)}
        result = stats.compute(data)
        self.assertTrue(result["views"]["platform"]["gates"]["pass_at_1"]["verdict"].startswith("FAIL"))
        self.assertEqual(result["gates"]["pass_at_1"]["verdict"], "PASS")
        self.assertFalse(any(item.startswith("pass_at_1") for item in result["blocking"]))
        self.assertEqual(result["verdict_view"], "valid")

    def test_model_provenance_rejects_missing_or_mixed_models(self):
        data = self.matrix([80] * 6)
        self.assertEqual(stats.compute(data)["gates"]["baseline_models"]["verdict"], "PASS")
        data["rollouts"][0]["models"].append("claude-sonnet-5-5")
        self.assertIn("baseline_models", stats.compute(data)["blocking"])
        data["rollouts"][0]["models"] = []
        self.assertIn("missing provenance", stats.compute(data)["gates"]["baseline_models"]["value"])
        data["rollouts"][0]["models"] = ["claude-opus-5-5"]
        data["rollouts"][0]["model_check"] = {"v3_valid": False, "mixed_model": True, "fallback_events": [3],
                                              "models": ["claude-opus-5-5"]}
        self.assertIn("mixed/fallback", stats.compute(data)["gates"]["baseline_models"]["value"])

    def test_model_gate_rejects_bad_labels_and_missing_source(self):
        for label in ("claude-opus-5", "claude-opus-5-5-20261001", "Opus 5.5", "<synthetic>"):
            data = self.matrix([80] * 6)
            data["rollouts"][0]["models"] = [label]
            self.assertIn("baseline_models", stats.compute(data)["blocking"], label)
        data = self.matrix([80] * 6)
        data["rollouts"][0]["model_source"] = ""
        self.assertIn("baseline_models", stats.compute(data)["blocking"])
        data = self.matrix([80] * 6)
        data["rollouts"][0].pop("model_check")
        self.assertIn("baseline_models", stats.compute(data)["blocking"])
        data = self.matrix([80] * 6)
        data["rollouts"][5]["model_check"]["fallback_events"] = [1]
        self.assertIn("baseline_models", stats.compute(data)["blocking"])
        for bad in (None, "False", 0):
            data = self.matrix([80] * 6)
            data["rollouts"][0]["model_check"]["v3_valid"] = bad
            self.assertIn("baseline_models", stats.compute(data)["blocking"], bad)
        data = self.matrix([80] * 6)
        data["rollouts"][0]["model_check"].pop("v3_valid")
        self.assertIn("baseline_models", stats.compute(data)["blocking"])
        data = self.matrix([80] * 6)
        data["rollouts"][0]["models"] = ["claude-opus-5-5", "claude-sonnet-5-5"]
        self.assertIn("baseline_models", stats.compute(data)["blocking"])
        self.assertEqual(stats.check_models(["claude-opus-5-5[1m]"], expected="claude-opus-5-5[1m]")["verdict"],
                         "VALID")

    def test_trajectory_provenance_flags_fallback_without_a_bad_label(self):
        with selftest_sandbox.scratch_tmp("test_difficulty_v3_") as temp:
            path = Path(temp) / "run-1.json"
            path.write_text(json.dumps([
                {"type": "system", "subtype": "init", "model": "claude-opus-5-5"},
                {"type": "assistant", "message": {"model": "claude-opus-5-5"}},
                {"type": "system", "subtype": "model_refusal_fallback"},
            ]))
            prov = stats.trajectory_provenance(path)
            self.assertEqual(prov["fallback_events"], [2])
            self.assertFalse(prov["v3_valid"])
            gate = stats.model_gate([{"id": "run-1", "models": ["claude-opus-5-5"],
                                      "model_source": "trajectory:run-1.json", "model_check": prov}])
            self.assertTrue(gate["verdict"].startswith("FAIL"), gate)

    def test_trajectory_models_read_actual_metadata(self):
        with selftest_sandbox.scratch_tmp("test_difficulty_v3_") as temp:
            path = Path(temp) / "run-1.json"
            path.write_text(json.dumps([{"type": "system", "subtype": "init", "model": "claude-opus-5-5"},
                                       {"type": "assistant", "message": {"model": "claude-sonnet-5-5"}}]))
            self.assertEqual(stats.trajectory_models(path), ["claude-opus-5-5", "claude-sonnet-5-5"])

    def test_trajectory_models_keep_blank_and_fallback_labels(self):
        with selftest_sandbox.scratch_tmp("test_difficulty_v3_") as temp:
            path = Path(temp) / "run-1.json"
            path.write_text(json.dumps([
                {"type": "system", "subtype": "init", "model": "claude-opus-5-5[1m]"},
                {"type": "assistant", "message": {"model": ""}},
                {"type": "system", "subtype": "model_refusal_fallback", "fallback_model": "claude-opus-5"},
            ]))
            models = stats.trajectory_models(path)
            self.assertIn("", models)
            self.assertIn("claude-opus-5", models)
            self.assertIn(stats.check_models(models)["verdict"], {"UNKNOWN", "INVALID"})
        self.assertEqual(stats.classify_model("claude-opus-5-5[1m]", "claude-opus-5-5[1m]"), "expected")
        # one owner of model labels (2026-10-25): strip only a bracketed suffix, then compare exactly
        for model in ("claude-opus-5-5", "claude-opus-5-5[1m]"):
            self.assertTrue(stats.is_opus_55(model), model)
        for model in ("claude-opus-4-8", "claude-sonnet-5-5", "unknown", "opus-5-50", "claude-opus-5",
                      "Opus 5.5", "claude-opus-5-5-20261001", "<synthetic>"):
            self.assertFalse(stats.is_opus_55(model), model)
        self.assertEqual(stats.classify_model("Opus 5.5"), "unknown")
        self.assertEqual(stats.classify_model("<synthetic>"), "synthetic")

    def test_precheck_provenance_positive_and_negative(self):
        init = {"type": "system", "subtype": "init", "model": "claude-opus-5-5"}
        def ev(label):
            return {"type": "assistant", "message": {"model": label}}
        self.assertTrue(stats.precheck_provenance([init, ev("claude-opus-5-5")])["ok"])
        self.assertFalse(stats.precheck_provenance([init, ev("")])["ok"])
        self.assertFalse(stats.precheck_provenance([init, ev("claude-opus-5")])["ok"])
        self.assertFalse(stats.precheck_provenance([init, ev("claude-opus-5-5"),
                                                    {"type": "system", "subtype": "model_refusal_fallback"}])["ok"])

    def test_context_binding_rejects_assignment_and_policy_changes(self):
        data = self.matrix([80] * 6)
        context = {"spec_version": "V3", "task_type": "long-horizon", "difficulty_mode": "easy",
                   "difficulty_cap": .9, "assignment_hash": "assignment-a", "policy_hash": "policy-a",
                   "context_hash": "context-a", "freeze_utc": "2025-10-01T00:00:00Z"}
        stats.bind_context(data, context, require_existing=False)
        stats.bind_context(data, context)
        for field in ("assignment_hash", "policy_hash", "context_hash"):
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "stale"):
                stats.bind_context(copy.deepcopy(data), dict(context, **{field: "changed"}))
        with self.assertRaisesRegex(ValueError, "difficulty_mode"):
            stats.bind_context(copy.deepcopy(data), dict(context, difficulty_mode="hard", difficulty_cap=.7))

    def test_existing_horizon_policy_is_unchanged(self):
        for calls, expected in ((99, "FAIL"), (100, "PASS"), (600, "PASS")):
            self.assertTrue(stats.compute(self.matrix([80] * 6, calls=calls))["gates"]["horizon"]["verdict"].startswith(expected))
        data = self.matrix([80] * 6, calls=101)
        data["task_type"] = "normal"
        self.assertTrue(stats.compute(data)["gates"]["horizon"]["verdict"].startswith("NON-FAIL"))


if __name__ == "__main__":
    unittest.main()

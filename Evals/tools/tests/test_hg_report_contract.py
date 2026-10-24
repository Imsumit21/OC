"""Verdict validation at the report writer boundary."""

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hg_report_contract import SCORED, STAGES, parse_result
import hg_write_output


def report(verdict, status="COMPLETE", score=None, limits="None", stage=None, model="Opus", prediction_basis="Transfer evidence in chain C1"):
    score_line = "" if score is None else f"Score: {score}\n\n"
    extra = ""
    if stage == "oe" and score not in (None, "null"):
        extra = (f"\nCompleteness score: {score}\nAccuracy score: 5\nReview policy: oracle-events-v1\n"
                 + "\n".join(label + ": " + "a" * 64 for label in
                   ("Reviewed OE SHA-256", "Review context SHA-256", "OE record SHA-256", "Eval release SHA-256"))
                 + "\nEval version: oracle-events-v1\n")
    if stage == "hardness":
        difficulty, gate, reason = {
            None: ("unassigned", "HOLD", "INSUFFICIENT_EVIDENCE"),
            "null": ("unassigned", "HOLD", "INSUFFICIENT_EVIDENCE"),
            1: ("Too easy", "HOLD", "INSUFFICIENT_DIFFICULTY"),
            2: ("Easy", "HOLD", "INSUFFICIENT_DIFFICULTY"),
            3: ("Hard", "PROCEED", "OBSERVED_OPUS_FAILURE"),
            4: ("Hard", "PROCEED", "OBSERVED_OPUS_FAILURE"),
            5: ("Really hard", "PROCEED", "OBSERVED_OPUS_FAILURE"),
        }[score]
        if score in (3, 4, 5) and model == "Haiku":
            reason = "PREDICTED_OPUS_DIFFICULTY"
        mode = {"Opus": "OPUS_OBSERVED", "Haiku": "HAIKU_TO_OPUS"}.get(model, "UNCONFIRMED")
        extra = f"\nAssessment version: model-aware-v3\n\nAssessed model: {model}\n\nAssessment mode: {mode}\n\nDifficulty: {difficulty}\n\nGate decision: {gate}\n\nGate reason: {reason}\n"
        if model == "Haiku":
            extra += f"\nPrediction basis: {prediction_basis}\n"
    return (
        f"### FINAL VERDICT: {verdict}\n\n{score_line}"
        f"Execution status: {status}\n\nEvaluator model: Opus 5.5 (claude-opus-5-5), xhigh effort\n\n"
        "Next action: Review findings\n\n"
        f"Evidence limits: {limits}\n{extra}"
    )


class ReportContractTests(unittest.TestCase):
    def test_provisional_non_fail_for_every_stage(self):
        for stage in STAGES:
            for status in ("PARTIAL", "BLOCKED"):
                for score in (None, "null"):
                    with self.subTest(stage=stage, status=status, score=score):
                        expected = {"verdict": "NON-FAIL", "verdict_score": None, "execution_status": status}
                        if stage == "hardness":
                            expected.update(difficulty=None, gate_decision="HOLD", gate_reason="INSUFFICIENT_EVIDENCE", assessment_version="model-aware-v3", assessed_model="Opus", assessment_mode="OPUS_OBSERVED")
                        if stage == "oe":
                            expected.update(completeness_score=None, accuracy_score=None)
                        self.assertEqual(parse_result(stage, report("NON-FAIL", status, score,
                                                                    "Schema unavailable", stage)), expected)

    def test_existing_completed_bands(self):
        for stage in STAGES:
            mappings = ([("PASS", 5), ("NON-FAIL", 3), ("NON-FAIL", 4), ("FAIL", 1), ("FAIL", 2)]
                        if stage in SCORED else [("PASS", 5 if stage == "golden" else None), ("FAIL", None)])
            if stage == "oe":
                mappings = [("PASS", 5), ("NON-FAIL", 3)]
            for verdict, score in mappings:
                with self.subTest(stage=stage, verdict=verdict, score=score):
                    parsed = parse_result(stage, report(verdict, score=score, stage=stage))
                    self.assertEqual((parsed["verdict"], parsed["verdict_score"]), (verdict, score))

    def test_demonstrated_fail_survives_partial_review(self):
        for stage in STAGES:
            with self.subTest(stage=stage):
                if stage in {"hardness", "oe"}:
                    # A hardness FAIL asserts low observed difficulty, which
                    # incomplete review coverage cannot establish.
                    with self.assertRaises(ValueError):
                        parse_result(stage, report("FAIL", "PARTIAL", 1, "Missing output", stage))
                    continue
                result = parse_result(stage, report("FAIL", "PARTIAL", 1 if stage in SCORED else None,
                                                   "Other checks remain pending", stage))
                self.assertEqual(result["verdict"], "FAIL")

    def test_invalid_or_absent_verdict_rejected(self):
        for label in ("", "NOT EVALUATED", "NEEDS-REVISION", "nonfail", "PASS (5)"):
            with self.subTest(label=label), self.assertRaises(ValueError):
                parse_result("injection", report(label))
        with self.assertRaises(ValueError):
            parse_result("injection", "No report yet")

    def test_incomplete_evidence_cannot_be_certified_or_scored(self):
        for stage in STAGES:
            for status in ("PARTIAL", "BLOCKED"):
                with self.subTest(stage=stage, status=status):
                    with self.assertRaises(ValueError):
                        parse_result(stage, report("PASS", status, 5 if stage in SCORED or stage == "golden" else None,
                                                   stage=stage))
                    with self.assertRaises(ValueError):
                        parse_result(stage, report("NON-FAIL", status, 3, "Missing source", stage))
                    with self.assertRaises(ValueError):
                        parse_result(stage, report("NON-FAIL", status, stage=stage))
            if stage not in SCORED:
                with self.subTest(stage=stage), self.assertRaises(ValueError):
                    parse_result(stage, report("NON-FAIL"))

    def test_bad_score_mappings_rejected(self):
        for verdict, score in (("PASS", 4), ("NON-FAIL", 2), ("FAIL", 3), ("PASS", None), ("FAIL", "0")):
            with self.subTest(verdict=verdict, score=score), self.assertRaises(ValueError):
                parse_result("prompt", report(verdict, score=score))
        with self.assertRaises(ValueError):
            parse_result("golden", report("PASS"))

    def test_rendered_block_only_and_required_fields(self):
        content = "```markdown\n" + report("FAIL") + "```\n" + report("PASS").replace("PASS", "**PASS**")
        self.assertEqual(parse_result("injection", content)["verdict"], "PASS")
        for content in (report("PASS") + report("FAIL"), report("PASS") + "Execution status: PARTIAL\n",
                        report("PASS").replace("Next action: Review findings\n", "")):
            with self.assertRaises(ValueError):
                parse_result("injection", content)

    def test_writer_keeps_fixed_paths_and_rejects_blank_before_overwrite(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(hg_write_output, "REPOSITORY", Path(folder)):
            for stage in STAGES:
                with self.subTest(stage=stage):
                    content = report("NON-FAIL", "PARTIAL", limits="Required evidence unavailable", stage=stage)
                    receipt = hg_write_output.save_output(stage, content)
                    dest = Path(folder) / receipt["path"]
                    self.assertEqual(dest.read_text(), content)
                    self.assertEqual(dest.parent, Path(folder) / "Evals/task_inputs/reports")
                    self.assertEqual(receipt["verdict"], "NON-FAIL")
                    with self.assertRaises(ValueError):
                        hg_write_output.save_output(stage, report("", "PARTIAL"))
                    self.assertEqual(dest.read_text(), content)

    def test_evaluator_model_is_reported_and_required_for_new_reports(self):
        line = "Evaluator model: Opus 5.5 (claude-opus-5-5), xhigh effort\n\n"
        content = report("NON-FAIL", "PARTIAL", limits="Required evidence unavailable", stage="hardness")
        self.assertEqual(parse_result("hardness", content)["evaluator_model"], "Opus 5.5 (claude-opus-5-5), xhigh effort")
        self.assertEqual(parse_result("hardness", content)["assessed_model"], "Opus")
        historical = content.replace(line, "")
        self.assertNotIn("evaluator_model", parse_result("hardness", historical))
        with self.assertRaises(ValueError):
            parse_result("hardness", content.replace("Opus 5.5 (claude-opus-5-5), xhigh effort", ""))
        with tempfile.TemporaryDirectory() as folder, patch.object(hg_write_output, "REPOSITORY", Path(folder)):
            for stage in set(STAGES) - {"golden"}:
                with self.subTest(stage=stage):
                    content = report("NON-FAIL", "PARTIAL", limits="Required evidence unavailable", stage=stage)
                    receipt = hg_write_output.save_output(stage, content)
                    self.assertEqual(receipt["evaluator_model"], "Opus 5.5 (claude-opus-5-5), xhigh effort")
                    with self.assertRaisesRegex(ValueError, "Evaluator model"):
                        hg_write_output.save_output(stage, content.replace(line, ""))
                    self.assertEqual((Path(folder) / receipt["path"]).read_text(), content)

    def test_hardness_gate_matches_every_supported_band(self):
        for verdict, score, difficulty, gate in (
            ("FAIL", 1, "Too easy", "HOLD"),
            ("FAIL", 2, "Easy", "HOLD"),
            ("NON-FAIL", 3, "Hard", "PROCEED"),
            ("NON-FAIL", 4, "Hard", "PROCEED"),
            ("PASS", 5, "Really hard", "PROCEED"),
        ):
            content = report(verdict, score=score, stage="hardness")
            with self.subTest(score=score):
                parsed = parse_result("hardness", content)
                self.assertEqual((parsed["difficulty"], parsed["gate_decision"]), (difficulty, gate))
                for field, wrong_value in (("Difficulty", "unassigned"),
                                           ("Gate decision", "PROCEED" if gate == "HOLD" else "HOLD"),
                                           ("Gate reason", "INSUFFICIENT_EVIDENCE")):
                    bad = "\n".join(f"{field}: {wrong_value}" if line.startswith(field + ":") else line
                                    for line in content.splitlines())
                    with self.subTest(field=field), self.assertRaises(ValueError):
                        parse_result("hardness", bad)

    def test_unassigned_hardness_cannot_proceed_or_claim_easy(self):
        for status in ("PARTIAL", "BLOCKED"):
            content = report("NON-FAIL", status, limits="Source missing", stage="hardness")
            for old, new in (("Gate decision: HOLD", "Gate decision: PROCEED"),
                             ("Difficulty: unassigned", "Difficulty: Too easy"),
                             ("INSUFFICIENT_EVIDENCE", "INSUFFICIENT_DIFFICULTY")):
                with self.subTest(status=status, field=old), self.assertRaises(ValueError):
                    parse_result("hardness", content.replace(old, new))

    def test_hardness_requires_explicit_unambiguous_gate_block(self):
        content = report("FAIL", score=1, stage="hardness")
        for line in ("Difficulty: Too easy", "Gate decision: HOLD", "Gate reason: INSUFFICIENT_DIFFICULTY", "Assessment version: model-aware-v3", "Assessed model: Opus", "Assessment mode: OPUS_OBSERVED"):
            for bad in (content.replace(line, ""), content + line + "\n",
                        content.replace(line, "```\n" + line + "\n```"),
                        content.replace(line, line.split(":")[0] + ":")):
                with self.subTest(line=line, bad=bad), self.assertRaises(ValueError):
                    parse_result("hardness", bad)
        with self.assertRaises(ValueError):
            parse_result("hardness", report("FAIL", score=1) + "\n## Details\nGate decision: HOLD\n")
        # Narrative and fenced examples cannot override the actual gate.
        parsed = parse_result("hardness", content + "\n## Details\nGate decision: PROCEED\n")
        self.assertEqual(parsed["gate_decision"], "HOLD")

    def test_retired_gate_reasons_and_versions_cannot_overwrite_current_report(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(hg_write_output, "REPOSITORY", Path(folder)):
            current = report("PASS", score=5, stage="hardness")
            receipt = hg_write_output.save_output("hardness", current)
            destination = Path(folder) / receipt["path"]
            self.assertEqual(receipt["assessment_version"], "model-aware-v3")
            retired = [current.replace("OBSERVED_OPUS_FAILURE", reason) for reason in
                       ("QUALIFYING_FAILURE_PATTERN", "QUALIFYING_COHORT_SWEEP", "DESIGN_SCALE_UNPAIRED")]
            retired += [current.replace("model-aware-v3", "observed-run-v7"),
                        current.replace("model-aware-v3", "direct-run-v2"),
                        current.replace("Assessment version: model-aware-v3", "")]
            for content in retired:
                with self.subTest(content=content), self.assertRaises(ValueError):
                    hg_write_output.save_output("hardness", content)
                self.assertEqual(destination.read_text(), current)

    def test_partial_hardness_never_claims_a_numeric_band(self):
        for verdict, score in [("FAIL", 1), ("FAIL", 2), ("NON-FAIL", 3), ("NON-FAIL", 4), ("PASS", 5)]:
            for status in ("PARTIAL", "BLOCKED"):
                with self.subTest(score=score, status=status), self.assertRaises(ValueError):
                    parse_result("hardness", report(verdict, status, score, "Output unavailable", "hardness"))
        content = report("NON-FAIL", "PARTIAL", limits="Truncated export; an independent error is proven", stage="hardness")
        parsed = parse_result("hardness", content)
        self.assertIsNone(parsed["verdict_score"])
        self.assertEqual(parsed["gate_decision"], "HOLD")
        self.assertEqual(parsed["gate_reason"], "INSUFFICIENT_EVIDENCE")

    def test_haiku_prediction_supports_all_bands_without_claiming_observation(self):
        for verdict, score in [("FAIL", 1), ("FAIL", 2), ("NON-FAIL", 3), ("NON-FAIL", 4), ("PASS", 5)]:
            content = report(verdict, score=score, limits="Qualitative Opus prediction from one Haiku run; Opus performance was not observed.",
                             stage="hardness", model="Haiku")
            with self.subTest(score=score):
                result = parse_result("hardness", content)
                self.assertEqual(result["assessed_model"], "Haiku")
                self.assertEqual(result["assessment_mode"], "HAIKU_TO_OPUS")
                self.assertEqual(result["prediction_basis"], "Transfer evidence in chain C1")
                self.assertEqual(result["verdict_score"], score)
                self.assertEqual(result["gate_decision"], "PROCEED" if score >= 3 else "HOLD")
                self.assertEqual(result["gate_reason"], "PREDICTED_OPUS_DIFFICULTY" if score >= 3 else "INSUFFICIENT_DIFFICULTY")
                if score >= 3:
                    with self.assertRaises(ValueError):
                        parse_result("hardness", content.replace("PREDICTED_OPUS_DIFFICULTY", "OBSERVED_OPUS_FAILURE"))
        with self.assertRaises(ValueError):
            parse_result("hardness", report("PASS", score=5, stage="hardness", model="Haiku"))
        opus = report("PASS", score=5, stage="hardness")
        with self.assertRaises(ValueError):
            parse_result("hardness", opus.replace("OBSERVED_OPUS_FAILURE", "PREDICTED_OPUS_DIFFICULTY"))

    def test_unconfirmed_model_cannot_receive_a_score(self):
        for model in ("Unconfirmed", "Sonnet", ""):
            for verdict, score in [("FAIL", 1), ("NON-FAIL", 3), ("PASS", 5)]:
                with self.subTest(model=model, score=score), self.assertRaises(ValueError):
                    parse_result("hardness", report(verdict, score=score, stage="hardness", model=model))
        result = parse_result("hardness", report("NON-FAIL", "PARTIAL", limits="Run model labels conflict", stage="hardness", model="Unconfirmed"))
        self.assertIsNone(result["verdict_score"])
        self.assertEqual(result["assessed_model"], "Unconfirmed")
        self.assertEqual(result["gate_decision"], "HOLD")

    def test_assessment_modes_cannot_be_swapped_or_hidden(self):
        for model, mode in (("Opus", "OPUS_OBSERVED"), ("Haiku", "HAIKU_TO_OPUS")):
            content = report("NON-FAIL", score=3, limits="One run; Opus prediction only if Haiku",
                             stage="hardness", model=model)
            for alternate in ("OPUS_OBSERVED", "HAIKU_TO_OPUS", "UNCONFIRMED", ""):
                if alternate != mode:
                    with self.subTest(model=model, alternate=alternate), self.assertRaises(ValueError):
                        parse_result("hardness", content.replace(f"Assessment mode: {mode}",
                                                                 f"Assessment mode: {alternate}"))
            with self.assertRaises(ValueError):
                parse_result("hardness", content.replace(f"Assessment mode: {mode}", ""))
        opus = report("PASS", score=5, stage="hardness")
        with self.assertRaises(ValueError):
            parse_result("hardness", opus + "Prediction basis: Assumed Haiku transfer\n")

    def test_haiku_prediction_needs_basis_even_for_low_or_unscored_results(self):
        for verdict, score, status in (("FAIL", 2, "COMPLETE"), ("PASS", 5, "COMPLETE"),
                                       ("NON-FAIL", None, "PARTIAL")):
            content = report(verdict, status, score, "Opus performance unobserved; transfer gap if partial",
                             "hardness", "Haiku")
            for basis in ("", "None", "null", "N/A"):
                with self.subTest(score=score, basis=basis), self.assertRaises(ValueError):
                    parse_result("hardness", content.replace("Transfer evidence in chain C1", basis))
            with self.assertRaises(ValueError):
                parse_result("hardness", content.replace("Prediction basis: Transfer evidence in chain C1", ""))
            parsed = parse_result("hardness", content)
            self.assertEqual(parsed["assessment_mode"], "HAIKU_TO_OPUS")

    def test_prediction_replaced_by_observed_opus_at_same_fixed_path(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(hg_write_output, "REPOSITORY", Path(folder)):
            # Equal scores still represent different claims and must keep their mode.
            haiku = report("NON-FAIL", score=4, limits="Opus prediction only; not observed",
                           stage="hardness", model="Haiku")
            predicted = hg_write_output.save_output("hardness", haiku)
            self.assertEqual(predicted["gate_reason"], "PREDICTED_OPUS_DIFFICULTY")
            self.assertEqual(predicted["assessment_mode"], "HAIKU_TO_OPUS")
            dest = Path(folder) / predicted["path"]
            for reason in ("OBSERVED_HAIKU_FAILURE", "OBSERVED_OPUS_FAILURE", "QUALIFYING_FAILURE_PATTERN"):
                with self.subTest(reason=reason), self.assertRaises(ValueError):
                    hg_write_output.save_output("hardness", haiku.replace("PREDICTED_OPUS_DIFFICULTY", reason))
                self.assertEqual(dest.read_text(), haiku)
            opus = report("FAIL", score=2, stage="hardness")
            observed = hg_write_output.save_output("hardness", opus)
            self.assertEqual(predicted["path"], observed["path"])
            self.assertEqual(observed["assessment_mode"], "OPUS_OBSERVED")
            self.assertEqual(observed["gate_decision"], "HOLD")
            self.assertNotIn("prediction_basis", observed)
            self.assertEqual(dest.read_text(), opus)

    def test_writer_rejects_hardness_gate_bypass_before_overwrite(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(hg_write_output, "REPOSITORY", Path(folder)):
            content = report("FAIL", score=1, stage="hardness")
            receipt = hg_write_output.save_output("hardness", content)
            destination = Path(folder) / receipt["path"]
            self.assertEqual(receipt["gate_decision"], "HOLD")
            with self.assertRaises(ValueError):
                hg_write_output.save_output("hardness", content.replace("Gate decision: HOLD", "Gate decision: PROCEED"))
            self.assertEqual(destination.read_text(), content)


if __name__ == "__main__":
    unittest.main()

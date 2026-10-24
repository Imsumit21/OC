"""Public-writer factual regressions using fixed, small synthetic sources.

These exercise production entry points with deliberately false review labels;
they are executable contract tests, not independent language-model reviews.
"""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_store_input as inputs
import hg_write_output as writer
from hg_rubric_loop import FINAL, POLICY, digest
from test_hg_rubric_loop import candidate, score_record, audit_report


class FactualAuditTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.addCleanup(patch.stopall)
        patch.object(writer, "REPOSITORY", self.root).start()
        patch.object(inputs, "REPOSITORY", self.root).start()
        inputs.save_input("prompt", content=b"Report the current download size.")
        inputs.save_input("task-details", content=b"Synthetic public-writer regression")
        inputs.clear_input("injection", confirmed_unused=True)

    def prepare(self, title=None, verdict="PASS"):
        text = candidate(title) if title else candidate()
        inputs.save_input("rubric", content=text.encode())
        return text, score_record(self.root, verdict=verdict, mode="AUDIT")

    def source(self, payload):
        path = self.root / "independent_source.json"
        raw = json.dumps(payload, sort_keys=True).encode()
        path.write_bytes(raw)
        return dict(id="INDEPENDENT", path=str(path), sha256=digest(raw), quote=raw.decode(),
                    visibility="VISIBLE", access="Task-accessible synthetic primary source.")

    def facts(self, record, source, claim):
        ledger = record["checks"]
        ledger["sources"].append(copy.deepcopy(source))
        ledger["rows"][0]["fact_review"] = dict(complete=True, reason="One exact numeric measurement.", claims=[copy.deepcopy(claim)])

    def save(self, score):
        scored = writer.save_output("rubric-score", json.dumps(score))
        writer.save_output("rubric", audit_report(scored))
        self.assertFalse((self.root / FINAL).exists())
        return scored

    def assert_no_prefill(self, text):
        with self.assertRaisesRegex(ValueError, "evaluation-only"):
            writer.save_output("rubric-json", text)
        self.assertFalse((self.root / FINAL).exists())
        self.assertEqual((self.root / "Evals/task_inputs/09_Rubrics.json").read_text(), text)

    def test_wrong_999_cannot_pass_despite_false_review_labels(self):
        text, score = self.prepare("The Agent reports the current download size as 999 MB.")
        with self.assertRaisesRegex(ValueError, "source-derived fact mismatch.*incorrect|incorrect.*source-derived fact mismatch"):
            writer.save_output("rubric-score", json.dumps(score))
        self.assert_no_prefill(text)

    def test_correct_214_and_equivalent_decimal_receive_pass(self):
        for value in ("214 MB", "214.0 MB"):
            with self.subTest(value=value):
                text, score = self.prepare("The Agent reports the current download size as " + value + ".")
                result = self.save(score)
                self.assertEqual(result["verdict"], "PASS")
                self.assertTrue(result["fact_results"][0]["computed"][0]["matched"])
                self.assert_no_prefill(text)

    def test_missing_fact_review_rejected(self):
        text, score = self.prepare()
        del score["checks"]["rows"][0]["fact_review"]
        with self.assertRaisesRegex(ValueError, "fact_review"):
            writer.save_output("rubric-score", json.dumps(score))
        self.assert_no_prefill(text)

    def test_number_disguised_as_semantic_remains_partial(self):
        text, score = self.prepare("The Agent reports the current download size as 999 MB.")
        claim = score["checks"]["rows"][0]["fact_review"]["claims"][0]
        del claim["calculation"]
        claim.update(kind="SEMANTIC", status="VERIFIED", reason="Deliberately false semantic PASS label.")
        scored = self.save(score)
        self.assertEqual((scored["verdict"], scored["verdict_score"], scored["execution_status"]), ("NON-FAIL", None, "PARTIAL"))
        with self.assertRaises(ValueError):
            writer.save_output("rubric", audit_report(scored, force_pass=True))
        self.assert_no_prefill(text)

    def test_accurate_incorrect_finding_saves_fail(self):
        text, score = self.prepare("The Agent reports the current download size as 999 MB.", "FAIL")
        scored = self.save(score)
        self.assertEqual((scored["verdict"], scored["verdict_score"]), ("FAIL", 2))
        self.assertEqual(scored["fact_results"][0]["mismatches"][0]["actual"], "214")
        self.assert_no_prefill(text)

    def test_fresh_aggregate_source_matches_through_report_writer(self):
        text, score = self.prepare()
        source = self.source({"chunks": [{"mb": 71}, {"mb": 89}, {"mb": 54}], "unit": "MB"})
        claim = dict(id="SUM", quote="214 MB", kind="NUMBER", source_ids=[source["id"]],
                     reason="Add all independently stored chunks.",
                     calculation=dict(op="sum", operands=[dict(source_id=source["id"], pointer="/chunks", field="/mb")],
                                      source_unit=dict(source_id=source["id"], pointer="/unit")))
        self.facts(score, source, claim)
        scored = self.save(score)
        self.assertEqual(scored["fact_results"][0]["computed"][0]["operation"], "sum")
        self.assert_no_prefill(text)

    def test_omitted_or_hidden_unit_is_not_a_pass(self):
        for wording, quote in (("214 GB", "214 GB"), ("214 GB", "214"), ("$214", "214")):
            with self.subTest(wording=wording, quote=quote):
                text, score = self.prepare("The Agent reports the current download size as " + wording + ".")
                source = self.source({"size_mb": 214, "unit": "MB"})
                claim = dict(id="UNIT", quote=quote, kind="NUMBER", source_ids=[source["id"]],
                             reason="Deliberately omit source unit evidence.",
                             calculation=dict(op="direct", operands=[dict(source_id=source["id"], pointer="/size_mb")]))
                self.facts(score, source, claim)
                scored = self.save(score)
                self.assertEqual((scored["verdict"], scored["execution_status"]), ("NON-FAIL", "PARTIAL"))
                with self.assertRaises(ValueError):
                    writer.save_output("rubric", audit_report(scored, force_pass=True))
                self.assert_no_prefill(text)

    def test_explicit_source_unit_mismatch_is_a_recordable_fail(self):
        text, score = self.prepare("The Agent reports the current download size as 214 GB.", "FAIL")
        source = self.source({"size": 214, "unit": "MB"})
        claim = dict(id="UNIT", quote="214 GB", kind="NUMBER", source_ids=[source["id"]],
                     reason="Numeric identity cannot make MB equal GB.",
                     calculation=dict(op="direct", operands=[dict(source_id=source["id"], pointer="/size")],
                                      source_unit=dict(source_id=source["id"], pointer="/unit")))
        self.facts(score, source, claim)
        self.assertEqual(self.save(score)["verdict"], "FAIL")
        self.assert_no_prefill(text)

    def test_source_changed_after_review_invalidates_saved_pass(self):
        text, score = self.prepare()
        source = self.source({"size_mb": 214, "unit": "MB"})
        claim = dict(id="SIZE", quote="214 MB", kind="NUMBER", source_ids=[source["id"]], reason="Compare primary source.",
                     calculation=dict(op="direct", operands=[dict(source_id=source["id"], pointer="/size_mb")],
                                      source_unit=dict(source_id=source["id"], pointer="/unit")))
        self.facts(score, source, claim)
        scored = self.save(score)
        Path(source["path"]).write_text('{"size_mb": 215}')
        with self.assertRaisesRegex(ValueError, "fingerprint|hash|SHA|changed"):
            writer.save_output("rubric", audit_report(scored))
        self.assert_no_prefill(text)

    def test_golden_only_factual_source_is_unresolved_even_when_literal_matches(self):
        inputs.save_input("golden", content=b'{"size_mb":214,"unit":"MB"}')
        text, score = self.prepare()
        raw = (self.root / "Evals/task_inputs/08_Golden_Answer.md").read_bytes()
        source = dict(id="GOLDEN_ONLY", path="Evals/task_inputs/08_Golden_Answer.md", sha256=digest(raw),
                      quote=raw.decode(), visibility="VISIBLE", access="Supplied golden, not primary evidence.")
        claim = dict(id="SIZE", quote="214 MB", kind="NUMBER", source_ids=[source["id"]],
                     reason="Golden repeats the same measurement.",
                     calculation=dict(op="direct", operands=[dict(source_id=source["id"], pointer="/size_mb")],
                                      source_unit=dict(source_id=source["id"], pointer="/unit")))
        self.facts(score, source, claim)
        scored = writer.save_output("rubric-score", json.dumps(score))
        self.assertEqual((scored["verdict"], scored["execution_status"]), ("NON-FAIL", "PARTIAL"))
        self.assertEqual(scored["fact_results"][0]["computed"], [])
        self.assertEqual(scored["fact_results"][0]["mismatches"], [])
        self.assertTrue(any("primary factual authority" in x for x in scored["check_unresolved"]))
        self.assert_no_prefill(text)

    def test_exact_source_for_example_name_still_counts_as_vague_exemplar(self):
        text, score = self.prepare('The Agent identifies the document titled "For Example".')
        with self.assertRaisesRegex(ValueError, "vague exemplar"):
            writer.save_output("rubric-score", json.dumps(score))
        score["issues"] = [dict(type="vague_exemplar", rows=[1], impact="precision_only", provenance="rubric_original",
                                reason="The exemplar phrase sits inside the quoted record name.", omission_test="The judge may read the phrase as an illustrative example.")]
        score["dimensions"]["overall_quality"]["score"] = 2
        scored = writer.save_output("rubric-score", json.dumps(score))
        self.assertEqual((scored["severity_counts"]["Moderate"], scored["verdict"]), (1, "FAIL"))
        self.assert_no_prefill(text)

    def test_actual_vague_exemplar_requires_its_moderate_finding(self):
        text, score = self.prepare("The Agent suggests improvements, for example reducing the package size.")
        with self.assertRaisesRegex(ValueError, "vague exemplar"):
            writer.save_output("rubric-score", json.dumps(score))
        score["issues"] = [dict(type="vague_exemplar", rows=[1], impact="precision_only", provenance="rubric_original",
                                reason="The acceptance boundary is left as an illustrative example.", omission_test="Other unspecified suggestions could receive credit.")]
        score["dimensions"]["overall_quality"]["score"] = 2
        scored = writer.save_output("rubric-score", json.dumps(score))
        self.assertEqual((scored["severity_counts"]["Moderate"], scored["verdict"]), (1, "FAIL"))
        self.assert_no_prefill(text)

    def test_audit_cannot_skip_restrictions_or_whole_rubric_alternatives(self):
        for missing in ("restriction_review", "alternative_review", "overlap_review"):
            text, score = self.prepare()
            target = score["checks"]["rows"][0] if missing == "restriction_review" else score["checks"]
            del target[missing]
            with self.subTest(missing=missing), self.assertRaisesRegex(ValueError, missing):
                writer.save_output("rubric-score", json.dumps(score))
            self.assert_no_prefill(text)


if __name__ == "__main__":
    unittest.main()

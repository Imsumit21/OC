"""Golden PASS must bind a complete evidence audit, not just a verdict label."""

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_golden_review as golden
import hg_store_input as inputs
import hg_write_output as writer
from hg_report_contract import parse_result
from hg_rubric_loop import digest


def report(receipt=None, verdict="PASS", status="COMPLETE"):
    result = f"### FINAL VERDICT: {verdict}\n"
    if verdict == "PASS":
        result += "Score: 5\n"
    result += f"Execution status: {status}\nNext action: Follow findings\nEvidence limits: "
    result += "None\n" if status == "COMPLETE" else "Unresolved source check\n"
    if receipt:
        for label, key in zip(("Review policy", "Review mode", "Review iteration", "Reviewed golden SHA-256",
                               "Review context SHA-256", "Review record SHA-256"), golden.BINDING + ("review_record_sha256",)):
            if key in receipt:
                result += f"{label}: {receipt[key]}\n"
    return result


def evidence_record(receipt):
    """Concrete size-report fixture. Results are judgments, not NLP predictions."""
    return {**{key: receipt[key] for key in golden.BINDING}, "format_version": golden.FORMAT_VERSION,
            "sources": [dict(id="S1", path="evidence/current.txt", sha256=digest(b"Current size: 214 MB"),
                             location="line 1", observed="Current size: 214 MB", quote="Current size: 214 MB", visibility="VISIBLE", access="Shared with assigned persona"),
                        dict(id="P1", path="Evals/task_inputs/04_Prompt.txt", sha256=digest(b"Report the current size."),
                             quote="Report the current size.", visibility="VISIBLE", access="Actual supplied prompt")],
            "claims": [dict(id="C1", statement="Current size is 214 MB", golden_location="entire answer",
                            source_ids=["S1"], supporting_source_ids=["S1"], golden_quote="214 MB", result="VERIFIED", reason="Matches the current source measurement.")],
            "requirements": [dict(id="Q1", authority_chain=["P1"], authority="Prompt: Report the current size.",
                                  scope="Current download size in final reply, MB", expected_result="214 MB",
                                  golden_resolution="The answer states 214 MB.", source_ids=["S1"], claim_ids=["C1"],
                                  result="PASS", reason="The requested measurement is resolved.",
                                  verification=dict(kind="direct", complete=True, details="Read the current size source, line 1."),
                                  valid_case=dict(example="Current download size: 214.0 MB.", result="ACCEPT", reason="Equivalent numerical representation; no formatting restriction."),
                                  wrong_case=dict(example="Current download size: 215 MB.", result="REJECT", reason="Conflicts with the golden's 214 MB result."))],
            "chronology": dict(complete=True, comparisons=[], reason="One current size source; no competing revision in this fixture."),
            "alternative_review": dict(complete=True, branches=[], reason="No advertised alternatives; equivalent representations tested."),
            "repairs": [],
            "artifact_match": dict(result="MATCH", reason="The answer resolves the size the prompt asks for."),
            "checks": {key: dict(result="PASS", reason="Single source-backed size answer; requested output and accepted numerical alternatives checked.")
                       for key in golden.CHECKS}}


class GoldenReviewTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.addCleanup(patch.stopall)
        patch.object(writer, "REPOSITORY", self.root).start()
        patch.object(inputs, "REPOSITORY", self.root).start()
        inputs.save_input("universe", content=b"2026-02-14\n")  # task date (hg_universe.py)
        inputs.save_input("prompt", content=b"Report the current size.")
        inputs.save_input("task-details", content=b"Robert, Executive")
        inputs.save_input("golden", content=b"Current size is 214 MB.")
        inputs.clear_input("injection", confirmed_unused=True)
        (self.root / "evidence").mkdir()
        (self.root / "evidence/current.txt").write_bytes(b"Current size: 214 MB")

    def start(self):
        return golden.start_review(self.root)

    def attach(self, key, content):
        path = self.root / (key.replace(":", "_") + ".txt")
        path.write_bytes(content)
        return inputs.save_input(key, sources=[path])

    def ready(self):
        receipt = self.start()
        receipt.update(writer.save_output("golden-review", json.dumps(evidence_record(receipt))))
        return receipt

    def test_complete_audit_saves_pass_and_preserves_supplied_answer(self):
        before = (self.root / golden.ANSWER).read_bytes()
        receipt = self.ready()
        result = writer.save_output("golden", report(receipt))
        self.assertEqual(result["verdict"], "PASS")
        self.assertEqual(result["path"], "Evals/task_inputs/reports/2_golden.md")
        self.assertEqual((self.root / golden.ANSWER).read_bytes(), before)
        self.assertFalse((self.root / golden.EXPLICIT_DRAFT).exists())

    def test_legacy_pass_is_readable_but_cannot_be_reissued_without_evidence(self):
        self.assertEqual(parse_result("golden", report())["verdict"], "PASS")
        with self.assertRaisesRegex(ValueError, "current evidence record"):
            writer.save_output("golden", report())

    def test_missing_record_blocks_pass_even_with_plausible_hash(self):
        receipt = self.start()
        receipt["review_record_sha256"] = "a" * 64
        with self.assertRaisesRegex(ValueError, "saved golden-review"):
            writer.save_output("golden", report(receipt))

    def test_incomplete_record_cannot_hide_behind_pass_labels(self):
        receipt = self.start()
        mutations = [lambda x: x.update(requirements=[]),
                     lambda x: x["checks"].pop("completeness"),
                     lambda x: x["requirements"][0].pop("wrong_case"),
                     lambda x: x["requirements"][0].update(source_ids=[]),
                     lambda x: x["claims"][0].update(source_ids=["UNKNOWN"]),
                     lambda x: x["requirements"][0].update(claim_ids=[]),
                     lambda x: x["requirements"][0].update(authority=""),
                     lambda x: x["claims"].append(copy.deepcopy(x["claims"][0])),
                     lambda x: x["requirements"][0]["verification"].update(complete=1)]
        for change in mutations:
            record = evidence_record(receipt)
            change(record)
            with self.subTest(change=change), self.assertRaises(ValueError):
                writer.save_output("golden-review", json.dumps(record))

    def test_wrong_and_valid_solution_challenges_must_clear(self):
        for key, result in (("valid_case", "REJECT"), ("wrong_case", "ACCEPT"), ("wrong_case", "UNRESOLVED")):
            receipt = self.start()
            record = evidence_record(receipt)
            record["requirements"][0][key]["result"] = result
            receipt.update(writer.save_output("golden-review", json.dumps(record)))
            with self.subTest(key=key, result=result), self.assertRaisesRegex(ValueError, "prevents PASS"):
                writer.save_output("golden", report(receipt))

    def test_incomplete_absence_calculation_or_cohort_check_blocks_pass(self):
        for kind in ("absence", "calculation", "cohort"):
            receipt = self.start()
            record = evidence_record(receipt)
            record["requirements"][0]["verification"].update(kind=kind, complete=False)
            receipt.update(writer.save_output("golden-review", json.dumps(record)))
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, "prevents PASS"):
                writer.save_output("golden", report(receipt))

    def test_incorrect_auxiliary_claim_cannot_hide_behind_verified_outcomes(self):
        inputs.save_input("golden", content=b"Current size is 214 MB. Gmail search works.")
        receipt = self.start()
        record = evidence_record(receipt)
        config = b'{"gmail_search_messages": {"persistent_error_rate": 1}}'
        (self.root / "evidence/config.json").write_bytes(config)
        record["sources"].append(dict(id="S2", path="evidence/config.json", sha256=digest(config),
                                      location="/gmail_search_messages/persistent_error_rate", observed="1", quote="1", pointer="/gmail_search_messages/persistent_error_rate", visibility="VISIBLE",
                                      access="Applied task configuration; evaluator evidence of tool availability"))
        record["claims"].append(dict(id="C2", statement="Gmail search works", golden_location="alternative note",
                                      source_ids=["S2"], supporting_source_ids=[], golden_quote="Gmail search works.", result="INCORRECT", reason="Applied config disables search on every call.",
                                      defect_class="infeasible_path", repair_owner="contributor"))
        receipt.update(writer.save_output("golden-review", json.dumps(record)))
        with self.assertRaisesRegex(ValueError, "INCORRECT"):
            writer.save_output("golden", report(receipt))
        # FAIL preserves demonstrated findings without editing the answer.
        saved = writer.save_output("golden", report(receipt, "FAIL", "COMPLETE"))
        self.assertEqual(saved["verdict"], "FAIL")

    def test_changed_evidence_bytes_block_pass_even_with_same_size(self):
        receipt = self.ready()
        (self.root / "evidence/current.txt").write_bytes(b"Current size: 215 MB")
        with self.assertRaisesRegex(ValueError, "changed evidence source"):
            writer.save_output("golden", report(receipt))

    def test_changed_inputs_rules_and_answer_require_fresh_audit(self):
        for key in ("golden", "prompt", "rule", "error-async"):
            inputs.save_input("prompt", content=b"Report the current size.")
            inputs.save_input("golden", content=b"Current size is 214 MB.")
            receipt = self.ready()
            if key == "rule":
                path = self.root / "Evals/2_Golden_Response_Eval.md"
                path.write_text("Changed review rule")
            else:
                inputs.save_input(key, content=("Changed " + key).encode())
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, "changed"):
                writer.save_output("golden", report(receipt))

    def test_new_review_and_changed_record_archive_prior_report(self):
        receipt = self.ready()
        writer.save_output("golden", report(receipt))
        new = self.start()
        self.assertGreater(new["review_iteration"], receipt["review_iteration"])
        self.assertFalse((self.root / golden.REPORT).exists())
        self.assertFalse((self.root / golden.RECORD).exists())
        self.assertTrue(list((self.root / golden.HISTORY).glob("2_golden-*.md")))
        new.update(writer.save_output("golden-review", json.dumps(evidence_record(new))))
        with self.assertRaises(ValueError):
            writer.save_output("golden", report(receipt))
        writer.save_output("golden", report(new))
        changed = evidence_record(new)
        changed["requirements"][0]["reason"] += " Rechecked."
        writer.save_output("golden-review", json.dumps(changed))
        self.assertFalse((self.root / golden.REPORT).exists())
        with self.assertRaisesRegex(ValueError, "does not match"):
            writer.save_output("golden", report(new))

    def test_unready_report_can_be_saved_without_fabricated_record(self):
        for verdict in ("FAIL", "NON-FAIL"):
            saved = writer.save_output("golden", report(verdict=verdict, status="PARTIAL"))
            self.assertEqual(saved["verdict"], verdict)
        self.assertFalse((self.root / golden.RECORD).exists())

    def test_default_never_generates_an_answer_and_requires_optional_sql_decision(self):
        inputs.clear_input("golden")
        with self.assertRaises(ValueError):
            self.start()
        self.assertFalse((self.root / golden.ANSWER).exists())
        inputs.save_input("golden", content=b"214 MB")
        inputs.clear_input("injection")
        with self.assertRaisesRegex(ValueError, "no-injection"):
            self.start()

    def test_rubric_inputs_are_not_golden_dependencies(self):
        receipt = self.ready()
        for key in ("rubric", "source:rubric"):
            if key.startswith("source:"):
                self.attach(key, b"Not a golden input")
            else:
                inputs.save_input(key, content=b"Not a golden input")
            with self.subTest(key=key):
                self.assertEqual(writer.save_output("golden", report(receipt))["verdict"], "PASS")

    def test_explicit_saved_source_mapping_is_audited_without_replacing_it(self):
        saved = self.attach("source:golden", b"Current size is 214 MB.")
        path = saved["files"][0]["path"]
        receipt = golden.start_review(self.root, answer=path)
        self.assertEqual(receipt["answer_path"], path)
        receipt.update(writer.save_output("golden-review", json.dumps(evidence_record(receipt))))
        self.assertEqual(writer.save_output("golden", report(receipt))["verdict"], "PASS")
        self.assertEqual((self.root / path).read_bytes(), b"Current size is 214 MB.")
        self.assertFalse((self.root / golden.ANSWER).exists())
        with self.assertRaisesRegex(ValueError, "saved golden input"):
            golden.start_review(self.root, answer="evidence/current.txt")

    def test_changed_lookup_attachment_invalidates_the_audit(self):
        self.attach("source:lookup", b'{"task": "size review"}')
        receipt = self.ready()
        self.attach("source:lookup", b'{"task": "changed review"}')
        with self.assertRaisesRegex(ValueError, "changed"):
            writer.save_output("golden", report(receipt))

    def test_direct_record_edit_requires_new_report_hash(self):
        receipt = self.ready()
        path = self.root / golden.RECORD
        record = json.loads(path.read_text())
        record["requirements"][0]["reason"] += " Rechecked."
        path.write_text(json.dumps(record))
        with self.assertRaisesRegex(ValueError, "does not match"):
            writer.save_output("golden", report(receipt))

    def test_malformed_metadata_and_duplicate_json_keys_are_rejected(self):
        receipt = self.ready()
        good = report(receipt)
        for malformed in (
            good + "Review mode: AUDIT\n",
            good.replace("Review mode: AUDIT", "Review mode: CREATE"),
            good.replace("Review iteration: 1", "Review iteration: 0"),
            good.replace(receipt["review_record_sha256"], "invalid-hash"),
            good.replace("Review record SHA-256: " + receipt["review_record_sha256"] + "\n", ""),
        ):
            with self.subTest(report=malformed), self.assertRaises(ValueError):
                writer.save_output("golden", malformed)
        raw = json.dumps(evidence_record(receipt))
        with self.assertRaises(ValueError):
            writer.save_output("golden-review", raw[:-1] + ', "format_version": 3}')

    def test_corrupt_context_cannot_rebind_a_different_golden_hash(self):
        receipt = self.ready()
        path = self.root / golden.CONTEXT
        context = json.loads(path.read_text())
        context["reviewed_golden_sha256"] = "a" * 64
        path.write_text(json.dumps(context))
        receipt["reviewed_golden_sha256"] = "a" * 64
        record = evidence_record(receipt)
        with self.assertRaisesRegex(ValueError, "actual golden fingerprint"):
            writer.save_output("golden-review", json.dumps(record))

    def test_explicit_existing_draft_is_only_reviewed_and_bound_separately(self):
        path = self.root / golden.EXPLICIT_DRAFT
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("Explicitly authored draft: 214 MB.")
        receipt = golden.start_review(self.root, draft=True)
        self.assertEqual(receipt["review_mode"], "DRAFT")
        self.assertEqual((self.root / golden.ANSWER).read_bytes(), b"Current size is 214 MB.")
        receipt.update(writer.save_output("golden-review", json.dumps(evidence_record(receipt))))
        self.assertEqual(writer.save_output("golden", report(receipt))["verdict"], "PASS")

    def test_truncated_or_cut_golden_is_refused_at_intake(self):
        for cap in (5000, 50000):
            inputs.save_input("golden", content=b"x" * (cap - 1) + b".")
            with self.assertRaisesRegex(ValueError, f"exactly {cap:,}"):
                self.start()
        inputs.save_input("golden", content=b"Current size is 214 MB")
        with self.assertRaisesRegex(ValueError, "bad_ending"):
            self.start()
        receipt = golden.start_review(self.root, accept_ending="Ends on a list item by design")
        self.assertEqual(receipt["integrity_override"], "Ends on a list item by design")
        self.assertEqual(receipt["golden_length"], 22)

    def test_wrong_task_artifact_is_blocked_by_recorded_mismatch_with_overlap_evidence(self):
        inputs.save_input("prompt", content=b"Close ENG-2438 and tell Arthur Blake in #engineering.")
        receipt = self.start()
        self.assertEqual(receipt["prompt_overlap"]["prompt"]["shared"], 0)
        self.assertGreater(receipt["prompt_overlap"]["prompt"]["expected"], 0)
        record = evidence_record(receipt)
        record["sources"][1].update(sha256=digest(b"Close ENG-2438 and tell Arthur Blake in #engineering."), quote="Close ENG-2438")
        record.pop("artifact_match")
        with self.assertRaisesRegex(ValueError, "artifact_match"):
            writer.save_output("golden-review", json.dumps(record))
        record["artifact_match"] = dict(result="MISMATCH", reason="The answer reports a download size; the prompt asks to close ENG-2438.")
        saved = writer.save_output("golden-review", json.dumps(record))
        self.assertEqual((saved["verdict"], saved["execution_status"], saved["repair_owners"]), ("NON-FAIL", "BLOCKED", {"platform": 1}))
        with self.assertRaisesRegex(ValueError, "MISMATCH"):
            writer.save_output("golden", report({**receipt, **saved}))
        inputs.save_input("golden", content=b"ENG-2438 is closed and Arthur Blake was told in #engineering.")
        self.assertGreater(self.start()["prompt_overlap"]["prompt"]["shared"], 0)

    def test_composite_export_checks_only_the_golden_answer_section(self):
        body = "x" * 4999 + "."
        inputs.save_input("golden", content=("## alternative_approaches_notes\n\nNotes.\n\n## golden_answer\n\n" + body +
                                              "\n\n## multiple_approaches\n\nMultiple valid approaches exist").encode())
        with self.assertRaisesRegex(ValueError, "artifact_truncated"):
            self.start()
        inputs.save_input("golden", content=b"## golden_answer\n\nCurrent size is 214 MB.\n\n## multiple_approaches\n\nMultiple valid approaches exist")
        receipt = self.start()
        self.assertEqual(receipt["golden_answer_length"], 23)

    def test_unledgered_value_blocks_pass_until_it_is_a_claim(self):
        inputs.save_input("golden", content=b"Current size is 214 MB as of 2026-02-13.")
        receipt = self.start()
        record = evidence_record(receipt)
        saved = writer.save_output("golden-review", json.dumps(record))
        self.assertEqual(saved["unledgered_values"], ["2026-02-13"])
        self.assertEqual((saved["verdict"], saved["execution_status"]), ("NON-FAIL", "PARTIAL"))
        with self.assertRaisesRegex(ValueError, "unledgered"):
            writer.save_output("golden", report({**receipt, **saved}))
        record["claims"].append(dict(id="C2", statement="Measured as of 2026-02-13", golden_location="entire answer",
                                     source_ids=["S1"], supporting_source_ids=["S1"], golden_quote="2026-02-13",
                                     result="VERIFIED", reason="Date matches the source export."))
        saved = writer.save_output("golden-review", json.dumps(record))
        self.assertEqual((saved["verdict"], saved["unledgered_values"]), ("PASS", []))

    def test_failing_items_need_defect_class_and_repair_owner(self):
        receipt = self.start()
        record = evidence_record(receipt)
        record["checks"]["accuracy"]["result"] = "FAIL"
        with self.assertRaisesRegex(ValueError, "defect_class"):
            writer.save_output("golden-review", json.dumps(record))
        record["checks"]["accuracy"].update(defect_class="wrong_value", repair_owner="contributor")
        saved = writer.save_output("golden-review", json.dumps(record))
        self.assertEqual((saved["verdict"], saved["defect_classes"], saved["repair_owners"]),
                         ("FAIL", {"wrong_value": 1}, {"contributor": 1}))
        record["checks"]["accuracy"]["repair_owner"] = "vendor"
        with self.assertRaisesRegex(ValueError, "repair_owner"):
            writer.save_output("golden-review", json.dumps(record))


if __name__ == "__main__":
    unittest.main()

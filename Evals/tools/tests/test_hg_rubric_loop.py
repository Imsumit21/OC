"""Audit/input invariants; these tests do not automate semantic grading."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_store_input as inputs
import hg_write_output as writer
import hg_golden_review as golden
from hg_report_contract import parse_result
from hg_rubric_loop import digest, DRAFT, FINAL, HISTORY, POLICY, REPORT, REVIEW_RECORD, review_context
from hg_rubric_review import CHECKS, FORMAT_VERSION


def assertion_inventory(title, outcomes):
    """Mechanical fixture inventory; it does not grade arbitrary title semantics."""
    return dict(complete=True, reason="Fixture enumerates its declared required results.",
                assertions=[dict(id=f"A{i}", field="title", quote=unit["entity"] if unit["entity"] in title else title,
                                 role="REQUIRED_RESULT", outcome_id=unit["id"], kind="ENTITY_PROPERTY",
                                 entities=[unit["entity"]], property=unit["property"],
                                 reason="This fixture separately grades the declared entity/property.")
                            for i, unit in enumerate(outcomes, 1)])


def review_record(receipt, proposal):
    """Completeness fixture, not a semantic grader of arbitrary candidate text."""
    def case(example, result, reason):
        return dict(example=example, result=result, reason=reason)

    record = {k: receipt[k] for k in ("review_policy", "review_iteration",
                                     "reviewed_json_sha256", "review_context_sha256")}
    record.update(format_version=FORMAT_VERSION, requirements=[], rows=[], set_checks={}, set_tests={})
    for i, row in enumerate(json.loads(proposal), 1):
        rid = f"Q{i}"
        record["requirements"].append(dict(
            id=rid, authority="Saved prompt: Report the current download size.",
            accepted_result="214 MB, including equivalent 214.0 MB representation.",
            output="User-facing answer", source_evidence="Saved golden: current size 214 MB.",
            outcomes=[dict(id=f"{rid}-O1", entity="Current build", property="download size",
                           output="User-facing answer", accepted_result="214 MB")],
            coverage_mode="direct", rows=[i], coverage_reason="This row checks the requested measurement."))
        record["rows"].append(dict(
            row=i, requirement_ids=[rid], predicate=row["title"], output="User-facing answer",
            source_evidence="Saved golden: 214 MB.",
            valid_case=case("The current size is 214.0 MB.", "ACCEPT", "Equivalent numerical representation."),
            near_miss=case("The current size is 215 MB.", "REJECT", "The value differs from 214 MB."),
            atomicity=dict(status="PASS", reason="One current download-size measurement.",
                           outcome_ids=[f"{rid}-O1"], exception=None, split_plan=[],
                           independence_test=dict(classification="ONE_RESULT",
                               example="214 MB and 214.0 MB express the same measured value.",
                               satisfied_outcome_ids=[], failed_outcome_ids=[],
                               reason="Units and numeric representation define one measurement, not separate duties.")),
            supporting_fields=dict(status="PASS", reason="Supporting fields locate the measurement without adding output requirements.")))
    record["set_checks"] = {name: dict(status="PASS", reason="Single measurement fixture; the supplied check is clear.") for name in CHECKS}
    record["set_tests"] = dict(
        valid_completion=case("The current download size is 214 MB.", "ACCEPT", "The answer supplies the requested measurement."),
        final_reply={**case("The current size is 214.0 MB.", "ACCEPT", "The sole output is the answer, with no extra recap."),
                     "authority": "The prompt requests the measurement in the reply."},
        mutations=[dict(requirement_id=f"Q{i}", example="Change current size to 215 MB.",
                        result="REJECT", reason="Wrong numerical value.", caught_by=[i])
                   for i in range(1, len(json.loads(proposal)) + 1)])
    from rubric_checks_fixture import facts_fixture, fact_source
    record["sources"] = [dict(id="P1", path="Evals/task_inputs/04_Prompt.txt",
                              sha256=digest(b"Report the current download size."),
                              quote="Report the current download size.", visibility="VISIBLE", access="Actual supplied prompt"),fact_source()]
    for req in record["requirements"]:
        req["authority_chain"] = ["P1"]
    for row in record["rows"]:
        row['fact_review']=facts_fixture(json.loads(proposal)[row['row']-1]['title'])
        row["assertion_inventory"] = assertion_inventory(json.loads(proposal)[row["row"]-1]["title"],
                                                         record["requirements"][row["row"]-1]["outcomes"])
        row["restriction_review"] = dict(reason="One requested measurement; no added method/format restriction.", restrictions=[])
    record["alternative_review"] = dict(complete=True, source_ids=["P1"], branches=[],
                                        reason="Fixture has no separately advertised alternatives; equivalent numeric wording tested above.")
    record["overlap_review"] = dict(complete=True, reason="Compare semantic outcome ownership, preserving separately required output surfaces.")
    return record


def golden_pass(root, prompt=b"Report the current download size.", golden_text=b"The current download size is 214 MB.", quote="214 MB"):
    """Bind a golden-audit-v4 PASS record to the saved golden so rubric drafting is allowed (G6)."""
    import hg_golden_review as golden
    evidence = root / "evidence"
    evidence.mkdir(exist_ok=True)
    (evidence / "current.txt").write_bytes(b"Current size: 214 MB")
    receipt = golden.start_review(root)
    record = {**{key: receipt[key] for key in golden.BINDING}, "format_version": golden.FORMAT_VERSION,
              "sources": [dict(id="S1", path="evidence/current.txt", sha256=digest(b"Current size: 214 MB"), location="line 1",
                               observed="Current size: 214 MB", quote="Current size: 214 MB", visibility="VISIBLE", access="Shared with assigned persona"),
                          dict(id="P1", path="Evals/task_inputs/04_Prompt.txt", sha256=digest(prompt), quote=prompt.decode(), visibility="VISIBLE", access="Actual supplied prompt")],
              "claims": [dict(id="C1", statement="The golden states " + quote, golden_location="entire answer", source_ids=["S1"], supporting_source_ids=["S1"],
                              golden_quote=quote, result="VERIFIED", reason="Matches the current source measurement.")],
              "requirements": [dict(id="Q1", authority_chain=["P1"], authority="Prompt: " + prompt.decode(), scope="Requested output in the final reply",
                                    expected_result=quote, golden_resolution="The answer states " + quote, source_ids=["S1"], claim_ids=["C1"], result="PASS",
                                    reason="The requested result is resolved.", verification=dict(kind="direct", complete=True, details="Read the source, line 1."),
                                    valid_case=dict(example="Equivalent phrasing of " + quote, result="ACCEPT", reason="Meaning-preserving paraphrase."),
                                    wrong_case=dict(example="A different value.", result="REJECT", reason="Conflicts with the golden."))],
              "chronology": dict(complete=True, comparisons=[], reason="One source; no competing revision."),
              "alternative_review": dict(complete=True, branches=[], reason="No advertised alternatives."),
              "repairs": [], "artifact_match": dict(result="MATCH", reason="The answer resolves the prompt's request."),
              "checks": {key: dict(result="PASS", reason="Single source-backed answer checked.") for key in golden.CHECKS}}
    return writer.save_output("golden-review", json.dumps(record))


def score_record(root, verdict="PASS", mode="AUDIT"):
    from hg_review_score import DIMENSIONS, GATES, FORMAT_VERSION
    from hg_eval_release import snapshot
    score = 5 if verdict == "PASS" else 2
    target = DRAFT if mode == "CREATE" else Path("Evals/task_inputs/09_Rubrics.json")
    rows = len(json.loads((root / target).read_text()))
    return dict(format_version=FORMAT_VERSION, eval_release=snapshot('rubric'), review_mode=mode, rubric_path=target.as_posix(),
                reviewed_json_sha256=digest((root / target).read_bytes()),
                review_context_sha256=review_context(root)["sha256"],
                checks=__import__("rubric_checks_fixture").checks_fixture(json.loads((root / target).read_text()),
                    (root / "Evals/task_inputs/04_Prompt.txt").read_text()),
                weight_reviews=[dict(row=i, expected_weight=1, work_kind="direct_lookup",
                    source_ids=["P1"], reason="One direct measurement lookup in the fixture.") for i in range(1,rows+1)],
                coverage=dict(required_outcomes=rows, covered_outcomes=rows),
                issues=[] if verdict == "PASS" else [dict(type="incorrect", rows=[1], impact="rejects_correct", provenance="rubric_original",
                                                            witness="A correct 214 MB answer is failed by the wrong expected value.",
                                                            reason="Demonstrated incorrect acceptance fixture.")],
                hard_gates={g: dict(result="FAIL" if (g == "accuracy_acceptance" and verdict != "PASS") else "PASS",
                                    reason="Gate checked in scoring fixture.") for g in GATES},
                hard_gate_score=None, unresolved=[], predicted_all_fail=[], oe_cross_check=dict(oe_present=False),
                dimensions={d: dict(score=score if d == "overall_quality" else 5,
                                    reason="Recorded dimension judgment in scoring fixture.") for d in DIMENSIONS})


def candidate(title="The Agent reports the current download size as 214 MB."):
    return json.dumps([{
        "title": title, "category": "Outcome", "weight": 1,
        "justification": "The prompt requests the current download size.",
        "evidence": "Compare the reported size with the recorded current size.",
    }], indent=2) + "\n"


def audit_report(scoring, *, force_pass=False):
    verdict = "PASS" if force_pass else scoring["verdict"]
    score = 5 if force_pass else scoring["verdict_score"]
    status = "COMPLETE" if force_pass else scoring["execution_status"]
    ratio = scoring.get("coverage_ratio")
    return (f"# Rubric evaluation\n\n### FINAL VERDICT: {verdict}\n"
            f"Score: {score if score is not None else 'null'}\nExecution status: {status}\n"
            f"Review policy: {POLICY}\nReview mode: AUDIT\n"
            f"Reviewed JSON SHA-256: {scoring['reviewed_json_sha256']}\n"
            f"Review context SHA-256: {scoring['review_context_sha256']}\n"
            f"Scoring record SHA-256: {scoring['scoring_record_sha256']}\n"
            f"Eval version: {scoring['eval_release']['version']}\n"
            f"Eval release SHA-256: {scoring['eval_release']['manifest_sha256']}\n"
            f"Gate tier: {scoring['gate_tier']}\n"
            f"Coverage ratio: {str(ratio[0])+'/'+str(ratio[1]) if ratio else 'N/A'}\n"
            "Repairs: See findings\nClock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)\nEvaluator model: Opus 5.5 (claude-opus-5-5), xhigh effort\n"
            "Next action: Review findings\n"
            f"Evidence limits: {'None' if status == 'COMPLETE' else 'Required factual checks remain unresolved'}\n")


def review(receipt=None, verdict="PASS", mode="AUDIT", **unused):
    return audit_report(writer.save_output("rubric-score", json.dumps(score_record(writer.REPOSITORY, verdict, mode))))


class RubricAuditTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.addCleanup(patch.stopall)
        patch.object(writer, "REPOSITORY", self.root).start()
        patch.object(inputs, "REPOSITORY", self.root).start()
        inputs.save_input("universe", content=b"2026-02-14\n")  # task date (hg_universe.py)
        inputs.save_input("prompt", content=b"Report the current download size.")
        inputs.save_input("task-details", content=b"Synthetic rubric audit")
        inputs.clear_input("injection", confirmed_unused=True)
        self.save_rubric()

    def save_rubric(self, text=None):
        inputs.save_input("rubric", content=(text or candidate()).encode())

    def score(self, verdict="PASS"):
        return writer.save_output("rubric-score", json.dumps(score_record(self.root, verdict)))

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}

    def historical_export(self):
        path = self.root / FINAL
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"historical export: preserve exactly")
        return path

    def test_complete_pass_without_golden_or_prefill_fields(self):
        before = (self.root / "Evals/task_inputs/09_Rubrics.json").read_bytes()
        scored = self.score()
        self.assertEqual((scored["verdict"], scored["verdict_score"]), ("PASS", 5))
        report = audit_report(scored)
        for retired in ("Ready for prefill", "Review iteration", "Review record SHA", "Golden verified"):
            self.assertNotIn(retired, report)
        writer.save_output("rubric", report)
        self.assertEqual((self.root / REPORT).read_text(), report)
        self.assertEqual((self.root / "Evals/task_inputs/09_Rubrics.json").read_bytes(), before)
        for path in (FINAL, DRAFT, REVIEW_RECORD):
            self.assertFalse((self.root / path).exists())

    def test_bad_golden_review_is_not_a_prerequisite(self):
        inputs.save_input("golden", content=b"An unverified reference answer.")
        path = self.root / golden.RECORD
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("invalid old golden-review record")
        self.assertEqual(self.score()["verdict"], "PASS")
        self.assertEqual(path.read_text(), "invalid old golden-review record")

    def test_fail_is_reported_without_repairing_rubric(self):
        text = candidate("The Agent reports the current download size as 999 MB.")
        self.save_rubric(text)
        scored = self.score("FAIL")
        self.assertEqual((scored["verdict"], scored["verdict_score"]), ("FAIL", 2))
        writer.save_output("rubric", audit_report(scored))
        self.assertEqual((self.root / "Evals/task_inputs/09_Rubrics.json").read_text(), text)
        self.assertFalse((self.root / FINAL).exists())

    def test_process_defect_fails_without_repairing_rubric(self):
        record = score_record(self.root)
        record["dimensions"]["process"]["score"] = 2
        scored = writer.save_output("rubric-score", json.dumps(record))
        self.assertEqual((scored["verdict"], scored["verdict_score"]), ("FAIL", 2))
        writer.save_output("rubric", audit_report(scored))
        self.assertEqual((self.root / "Evals/task_inputs/09_Rubrics.json").read_text(), candidate())

    def test_retired_writer_routes_reject_before_any_mutation(self):
        self.historical_export()
        writer.save_output("rubric", audit_report(self.score()))
        before = self.snapshot()
        for kind in ("rubric-draft", "rubric-review", "rubric-json"):
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, "evaluation-only"):
                writer.save_output(kind, candidate())
            self.assertEqual(self.snapshot(), before)
        with self.assertRaisesRegex(ValueError, "evaluation-only"):
            writer.save_output("rubric-score", "{}", golden_unverified=True)
        self.assertEqual(self.snapshot(), before)

    def test_direct_legacy_mutators_are_disabled(self):
        from hg_rubric_loop import prepare_draft, approve_publication
        before = self.snapshot()
        for call in (lambda: prepare_draft(self.root, candidate()),
                     lambda: approve_publication(self.root, candidate(), {})):
            with self.assertRaisesRegex(ValueError, "evaluation-only"):
                call()
            self.assertEqual(self.snapshot(), before)

    def test_create_scoring_cannot_overwrite_audit(self):
        self.score()
        before = self.snapshot()
        record = score_record(self.root)
        record["review_mode"] = "CREATE"
        with self.assertRaisesRegex(ValueError, "AUDIT"):
            writer.save_output("rubric-score", json.dumps(record))
        self.assertEqual(self.snapshot(), before)

    def test_missing_rubric_does_not_generate_one(self):
        inputs.clear_input("rubric")
        record = dict(format_version=5, review_mode="AUDIT", rubric_path="Evals/task_inputs/09_Rubrics.json")
        before = self.snapshot()
        with self.assertRaises((OSError, ValueError)):
            writer.save_output("rubric-score", json.dumps(record))
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / DRAFT).exists())

    def test_historical_export_is_never_selected_automatically(self):
        path = self.historical_export()
        record = score_record(self.root)
        record.update(rubric_path=FINAL.as_posix(), reviewed_json_sha256=digest(path.read_bytes()))
        with self.assertRaisesRegex(ValueError, "actual saved rubric"):
            writer.save_output("rubric-score", json.dumps(record))

    def test_explicitly_selected_export_is_saved_as_input(self):
        path = self.historical_export()
        path.write_text(candidate())
        inputs.save_input("rubric", sources=[path])
        self.assertEqual(self.score()["verdict"], "PASS")
        self.assertEqual(path.read_text(), candidate())

    def test_new_scores_and_changed_inputs_preserve_historical_export(self):
        path = self.historical_export()
        original = path.read_bytes()
        writer.save_output("rubric", audit_report(self.score()))
        record = score_record(self.root)
        record["dimensions"]["process"]["reason"] += " Additional explanation."
        writer.save_output("rubric-score", json.dumps(record))
        self.assertFalse((self.root / REPORT).exists())
        self.assertTrue(any((self.root / HISTORY).glob("*.md")))
        for key, content in (("prompt", b"A revised prompt."), ("golden", b"A revised answer."), ("rubric", candidate().encode())):
            inputs.save_input(key, content=content)
            self.assertEqual(path.read_bytes(), original)
        inputs.clear_input("golden")
        self.assertEqual(path.read_bytes(), original)

    def test_saved_report_cannot_reuse_changed_rubric(self):
        report = audit_report(self.score())
        self.save_rubric(candidate("The Agent reports the current download size as 999 MB."))
        with self.assertRaisesRegex(ValueError, "actual rubric bytes"):
            writer.save_output("rubric", report)

    def test_saved_report_cannot_reuse_changed_context(self):
        report = audit_report(self.score())
        inputs.save_input("prompt", content=b"Report a different measurement.")
        with self.assertRaisesRegex(ValueError, "context changed"):
            writer.save_output("rubric", report)

    def test_changed_policy_or_tampered_input_is_detected(self):
        report = audit_report(self.score())
        path = self.root / "Evals/3_Rubrics_Eval.md"
        path.write_text("Different policy")
        with self.assertRaisesRegex(ValueError, "context changed"):
            writer.save_output("rubric", report)
        path.unlink()
        (self.root / "Evals/task_inputs/04_Prompt.txt").write_text("Tampered")
        with self.assertRaisesRegex(ValueError, "resave"):
            review_context(self.root)

    def test_wrong_report_hash_score_and_prefill_claim_are_rejected(self):
        report = audit_report(self.score())
        for bad in (report.replace("Score: 5", "Score: 4"),
                    report.replace("Scoring record SHA-256: ", "Scoring record SHA-256: 0"),
                    report.replace("Review context SHA-256: ", "Review context SHA-256: 0"),
                    report + "Ready for prefill: Yes\n"):
            with self.subTest(report=bad), self.assertRaises(ValueError):
                writer.save_output("rubric", bad)

    def test_legacy_pass_without_evidence_cannot_be_reissued(self):
        with self.assertRaises(ValueError):
            writer.save_output("rubric", "### FINAL VERDICT: PASS\nScore: 5\nExecution status: COMPLETE\nNext action: None\nEvidence limits: None\n")

    def test_duplicate_or_fenced_audit_binding_is_rejected(self):
        report = audit_report(self.score())
        for bad in (report + "Review mode: AUDIT\n", report.replace("Review mode: AUDIT", "```\nReview mode: AUDIT\n```")):
            with self.assertRaises(ValueError):
                writer.save_output("rubric", bad)

    def test_schema_only_fail_saves_without_invented_denominator(self):
        from hg_eval_release import snapshot
        for raw in ("[]", "not JSON", "{}"):
            self.save_rubric(raw)
            record = dict(format_version=5, review_mode="AUDIT", rubric_path="Evals/task_inputs/09_Rubrics.json",
                          reviewed_json_sha256=digest(raw.encode()), review_context_sha256=review_context(self.root)["sha256"],
                          eval_release=snapshot('rubric'), schema_only=True, issues=[], hard_gates=dict(schema=dict(result="FAIL", reason="Unusable array")),
                          hard_gate_score=2, unresolved=["No usable criteria to review."])
            scored = writer.save_output("rubric-score", json.dumps(record))
            self.assertIsNone(scored["fractions"])
            writer.save_output("rubric", audit_report(scored))

    def test_partial_report_with_record_hash_revalidates_evidence(self):
        record = score_record(self.root)
        claim = record["checks"]["rows"][0]["fact_review"]["claims"][0]
        del claim["calculation"]
        claim.update(kind="SEMANTIC", status="VERIFIED", reason="Unsupported numeric comparison.")
        scored = writer.save_output("rubric-score", json.dumps(record))
        report = audit_report(scored)
        writer.save_output("rubric", report)
        inputs.save_input("prompt", content=b"Different request")
        with self.assertRaisesRegex(ValueError, "context changed"):
            writer.save_output("rubric", report)

    def test_rubric_preflight_needs_rubric_but_not_golden(self):
        from hg_preflight import build_report, REQUIRED
        task = self.root / "Evals/task_inputs"
        result = build_report(self.root, task, "rubric")
        self.assertFalse(result["structural_input_issues"])
        inputs.clear_input("rubric")
        result = build_report(self.root, task, "rubric")
        self.assertTrue(any("09_Rubrics.json" in x for x in result["structural_input_issues"]))
        self.assertNotIn("hint", REQUIRED)
        self.assertIn("08_Oracle_Events.md", REQUIRED["all"])
        self.assertNotIn("08_Oracle_Events.md", REQUIRED["rubric"])

    def test_cli_end_to_end_and_retired_routes_have_no_side_effects(self):
        import os
        import shutil
        import subprocess
        tool_dir = self.root / "Evals/tools"
        tool_dir.mkdir(parents=True, exist_ok=True)
        for source in Path(writer.__file__).parent.glob("*.py"):
            shutil.copy2(source, tool_dir / source.name)
        from hg_eval_release import ROOT, MANIFEST
        manifest = json.loads((ROOT / MANIFEST).read_text())
        for name in [str(MANIFEST), *manifest['files']]:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / name, target)
        env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
        def cli(tool, *args, payload=""):
            return subprocess.run([sys.executable, str(tool_dir / tool), *args], input=payload,
                                  text=True, capture_output=True, env=env, cwd=self.root)
        saved = cli("hg_store_input.py", "save", "rubric", payload=candidate())
        self.assertEqual(saved.returncode, 0, saved.stderr)
        scored = cli("hg_write_output.py", "rubric-score", payload=json.dumps(score_record(self.root)))
        self.assertEqual(scored.returncode, 0, scored.stderr)
        result = json.loads(scored.stdout)
        report = cli("hg_write_output.py", "rubric", payload=audit_report(result))
        self.assertEqual(report.returncode, 0, report.stderr)
        self.assertEqual(json.loads(report.stdout)["verdict"], "PASS")
        before = self.snapshot()
        for kind in ("rubric-draft", "rubric-json", "rubric-review"):
            rejected = cli("hg_write_output.py", kind, payload=candidate())
            self.assertNotEqual(rejected.returncode, 0)
            self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / FINAL).exists())

    def test_historical_audit_without_context_is_readable_but_cannot_be_reissued(self):
        current = audit_report(self.score())
        old = "\n".join(line for line in current.splitlines() if not line.startswith("Review context SHA-256:"))
        old += "\nReady for prefill: No\nGolden verified: Yes\n"
        self.assertEqual(parse_result("rubric", old)["verdict"], "PASS")
        with self.assertRaisesRegex(ValueError, "review_context_sha256"):
            writer.save_output("rubric", old)


if __name__ == "__main__":
    unittest.main()

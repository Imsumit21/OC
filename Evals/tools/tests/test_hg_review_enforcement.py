"""Regression tests for enforceable review invariants; not an NLP grading test."""
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
from hg_review_evidence import EvidenceReader
from hg_review_score import calculate, GATES, DIMENSIONS, SCORE_PATH
from hg_rubric_loop import digest, DRAFT, FINAL, review_context, POLICY
from hg_rubric_review import validate_record
from test_hg_rubric_loop import candidate, review_record, score_record, review, golden_pass
from test_hg_golden_review import evidence_record, report


def tally(n, issues, quality, gate=None, unresolved=None, rubric=None):
    """Static-scoring fixture, not a factual or work-complexity reviewer.

    Unrelated weights default to correct so a test can isolate its intended
    dimension. Weight tests replace these declarations and test both boundaries.
    """
    from hg_review_score import FORMAT_VERSION
    missing = [i for i in issues if i["type"] == "missing_coverage"]
    issue_gates = {"incorrect": "accuracy_acceptance", "unauthorized": "accuracy_acceptance",
                   "unobservable": "accuracy_acceptance", "overly_specific": "accuracy_acceptance",
                   "overly_broad": "accuracy_acceptance", "non_atomic": "atomicity",
                   "not_self_contained": "self_containment", "missing_coverage": "coverage",
                   "duplicate": "duplicates"}
    forced = {issue_gates[i["type"]] for i in issues if i["type"] in issue_gates}
    failing = set(forced) | ({gate} if gate else set())
    rubric = rubric or json.loads(candidate()) * n
    kinds = {1: "direct_lookup", 3: "interpretation", 5: "multi_source_reconciliation"}
    return dict(format_version=FORMAT_VERSION, issues=issues,
                coverage=dict(required_outcomes=n + len(missing), covered_outcomes=n),
                hard_gates={g: dict(result="FAIL" if g in failing else "PASS", reason="Reviewed boundary fixture.") for g in GATES},
                hard_gate_score=None, unresolved=unresolved or [], predicted_all_fail=[],
                oe_cross_check=dict(oe_present=False),
                weight_reviews=[dict(row=i, expected_weight=r["weight"], work_kind=kinds[r["weight"]],
                                     source_ids=["P1"], reason="Weight-neutral fixture for a separate scoring boundary.")
                                for i, r in enumerate(rubric, 1)],
                dimensions={d: dict(score=quality if d == "overall_quality" else 5,
                                    reason="Existing scored dimension.") for d in DIMENSIONS})


ACCEPTANCE_TYPES = {"incorrect", "unauthorized", "non_atomic", "overly_broad"}


class ScoringRulesTests(unittest.TestCase):
    def run_score(self, n, issues, quality, **kwargs):
        return calculate(tally(n, issues, quality, **kwargs), json.loads(candidate()) * n)

    def issue(self, kind, rows, impact=None, **extra):
        base = dict(type=kind, rows=rows, reason="Concrete demonstrated defect in fixture.", provenance="rubric_original")
        if kind == "missing_coverage":
            base.update(criticality=extra.pop("criticality", "critical"), outcome_id=extra.pop("outcome_id", "Q9-O1"))
            impact = impact or "accepts_wrong"
        impact = impact or ("rejects_correct" if kind in ACCEPTANCE_TYPES else "precision_only")
        base["impact"] = impact
        if kind == "duplicate":
            base["duplicate_kind"] = "COMPLETELY_REDUNDANT"
        if impact in ("rejects_correct", "accepts_wrong") or base.get("criticality") == "critical":
            base["witness"] = "A concrete correct answer this row fails, or a wrong answer it passes."
        else:
            base["omission_test"] = "Acceptance is unchanged; only diagnostic precision is affected."
        base.update(extra)
        return base

    def test_acceptance_defect_blocks_publication_at_any_size_without_overriding_qc(self):
        for n in (6, 9, 116):
            r = self.run_score(n, [self.issue("incorrect", [1])], 2)
            self.assertEqual((r["verdict"], r["verdict_score"]), ("FAIL", 2), n)
            self.assertFalse(r["repair_free"])
            self.assertEqual(r["forced_gates"], ["accuracy_acceptance"])
            self.assertEqual(r["fractions"]["major"], [1, n])

    def test_exact_major_boundary_and_no_rounding_for_precision_majors(self):
        precise = lambda rows: self.issue("not_self_contained", rows, impact="precision_only")
        r = self.run_score(10, [precise([1])], 2)
        self.assertEqual((r["verdict"], r["verdict_score"], r["gate_tier"]), ("FAIL", 2, "localized"))
        self.assertEqual(self.run_score(9, [precise([1])], 2)["verdict"], "FAIL")
        self.assertEqual(self.run_score(8, [precise([1])], 2)["fractions"]["major"], [1, 8])

    def test_combined_and_all_issue_boundaries(self):
        self.assertEqual(self.run_score(20, [self.issue("duplicate", [1, 2, 3])], 2)["verdict"], "FAIL")
        self.assertEqual(self.run_score(20, [self.issue("duplicate", [1, 2, 3, 4])], 2)["verdict"], "FAIL")
        self.assertEqual(self.run_score(20, [self.issue("harmless_specificity", [1, 2, 3, 4])], 2)["verdict"], "FAIL")
        self.assertEqual(self.run_score(20, [self.issue("harmless_specificity", [1, 2, 3, 4, 5])], 2)["verdict"], "FAIL")

    def test_minor_pass_boundary(self):
        # rubric-flow-v2: Minor on 5-10% of rows is NON-FAIL 3; over 10% fails.
        self.assertEqual(self.run_score(21, [self.issue("harmless_specificity", [1])], 5)["verdict"], "PASS")
        self.assertEqual(self.run_score(20, [self.issue("harmless_specificity", [1])], 3)["verdict"], "NON-FAIL")
        self.assertEqual(self.run_score(20, [self.issue("harmless_specificity", [1, 2])], 3)["verdict"], "NON-FAIL")
        self.assertEqual(self.run_score(20, [self.issue("harmless_specificity", [1, 2, 3])], 2)["verdict"], "FAIL")

    def test_highest_severity_once_per_criterion(self):
        issues = [self.issue("duplicate", [1, 2]), self.issue("non_atomic", [1], impact="precision_only"), self.issue("incorrect", [1])]
        score = self.run_score(20, issues, 2)
        self.assertEqual(score["severity_counts"], dict(Minor=0, Moderate=1, Major=1))
        self.assertEqual(score["counted_rows"], [1, 2])

    def test_partial_overlap_group_counts_once_and_complete_duplicates_count_each(self):
        grouped = self.issue("duplicate", [1, 2, 3], duplicate_kind="OVERLAP_GROUP", overlap_group_id="G1")
        score = self.run_score(20, [grouped], 2)
        self.assertEqual(score["severity_counts"], dict(Minor=0, Moderate=1, Major=0))
        self.assertEqual(score["fractions"]["major_moderate"], [1, 20])
        complete = self.run_score(20, [self.issue("duplicate", [1, 2, 3])], 2)
        self.assertEqual(complete["severity_counts"]["Moderate"], 3)
        self.assertFalse(score["repair_free"])

    def test_overlap_group_excludes_higher_severity_members_without_double_counting(self):
        grouped = self.issue("duplicate", [1, 2, 3], duplicate_kind="OVERLAP_GROUP", overlap_group_id="G1")
        score = self.run_score(20, [grouped, self.issue("incorrect", [1])], 2)
        self.assertEqual(score["severity_counts"], dict(Minor=0, Moderate=1, Major=1))
        self.assertEqual(score["counted_rows"], [1, 2, 3])
        score = self.run_score(20, [grouped, self.issue("incorrect", [1, 2, 3])], 2)
        self.assertEqual(score["severity_counts"], dict(Minor=0, Moderate=0, Major=3))

    def test_duplicate_groups_cannot_reuse_rows_or_omit_identifiers(self):
        valid = self.issue("duplicate", [1, 2], duplicate_kind="OVERLAP_GROUP", overlap_group_id="G1")
        invalid = [self.issue("duplicate", [1], duplicate_kind="OVERLAP_GROUP", overlap_group_id="G1"),
                   self.issue("duplicate", [1, 2], duplicate_kind="OVERLAP_GROUP"),
                   self.issue("duplicate", [1, 2], duplicate_kind="UNKNOWN")]
        for issue in invalid:
            with self.subTest(issue=issue), self.assertRaises(ValueError):
                self.run_score(20, [issue], 4)
        second = self.issue("duplicate", [2, 3], duplicate_kind="OVERLAP_GROUP", overlap_group_id="G2")
        with self.assertRaises(ValueError):
            self.run_score(20, [valid, second], 4)

    def test_established_non_atomicity_is_major_regardless_of_declared_impact(self):
        harmless = self.run_score(9, [self.issue("non_atomic", [1], impact="precision_only")], 2)
        self.assertEqual((harmless["verdict"], harmless["severity_counts"]["Major"], harmless["gate_tier"]), ("FAIL", 1, "localized"))
        witnessed = self.run_score(9, [self.issue("non_atomic", [1], impact="accepts_wrong")], 2)
        self.assertEqual((witnessed["verdict"], witnessed["severity_counts"]["Major"], witnessed["forced_gates"]), ("FAIL", 1, ["atomicity"]))

    def test_severity_mislabel_impact_and_fake_denominator_row_rejected(self):
        bad = [dict(self.issue("duplicate", [1]), severity="Major"), self.issue("incorrect", [11]), self.issue("non_atomic", [True]),
               self.issue("duplicate", [1], impact="invented"), dict(self.issue("missing_coverage", []), rows=[1]),
               {k: v for k, v in self.issue("incorrect", [1]).items() if k != "provenance"},
               {k: v for k, v in self.issue("incorrect", [1]).items() if k != "witness"},
               dict(self.issue("incorrect", [1]), provenance="inherited_from_golden")]
        for issue in bad:
            with self.subTest(issue=issue), self.assertRaises(ValueError):
                self.run_score(10, [issue], 2)

    def test_missing_coverage_uses_authored_denominator(self):
        r = self.run_score(10, [self.issue("missing_coverage", [])], 2)
        self.assertEqual((r["criterion_count"], r["denominator"], r["missing_outcome_count"], r["counted_rows"]), (10, 10, 1, []))
        self.assertEqual((r["verdict"], r["gate_tier"], r["coverage_ratio"], r["fractions"]["major"]), ("FAIL", "localized", [10, 11], [1, 10]))
        self.assertFalse(r["repair_free"])
        r = self.run_score(10, [self.issue("missing_coverage", [], criticality="non_critical")], 2)
        self.assertEqual((r["verdict"], r["verdict_score"], r["gate_tier"], r["severity_counts"]["Major"]), ("FAIL", 2, "localized", 1))
        self.assertFalse(r["repair_free"])

    def test_coverage_counts_must_match_missing_issues(self):
        record = tally(10, [self.issue("missing_coverage", [])], 4)
        record["coverage"]["covered_outcomes"] = 11
        with self.assertRaisesRegex(ValueError, "coverage contradicts"):
            calculate(record, json.loads(candidate()) * 10)

    def test_failed_readiness_gate_does_not_override_qc_percentage(self):
        r = self.run_score(100, [self.issue("non_atomic", [1])], 2)
        self.assertEqual((r["verdict"], r["verdict_score"]), ("FAIL", 2))
        self.assertFalse(r["repair_free"])

    def test_localized_gate_preserves_supported_non_fail_score(self):
        r = self.run_score(100, [self.issue("not_self_contained", [1], impact="precision_only")], 2)
        self.assertEqual((r["verdict"], r["verdict_score"], r["gate_tier"], r["forced_gates"]), ("FAIL", 2, "localized", ["self_containment"]))
        self.assertFalse(r["repair_free"])

    def test_forced_gate_cannot_be_declared_pass(self):
        record = tally(10, [self.issue("incorrect", [1])], 4)
        record["hard_gates"]["accuracy_acceptance"]["result"] = "PASS"
        with self.assertRaisesRegex(ValueError, "accuracy_acceptance contradicts"):
            calculate(record, json.loads(candidate()) * 10)
        record = tally(10, [self.issue("incorrect", [1])], 4)
        record["hard_gate_score"] = 3
        with self.assertRaisesRegex(ValueError, "do not invent an additional QC score"):
            calculate(record, json.loads(candidate()) * 10)

    def test_three_acceptance_rows_do_not_invent_an_absolute_qc_override(self):
        r = self.run_score(52, [self.issue("unauthorized", [1, 2, 3])], 2)
        self.assertFalse(r["absolute_rule_triggered"])
        self.assertEqual((r["overall_quality_band"], r["fractions"]["major"]), ("FAIL", [3, 52]))
        self.assertFalse(r["repair_free"])
        with self.assertRaisesRegex(ValueError, "wrong overall quality band"):
            self.run_score(52, [self.issue("unauthorized", [1, 2, 3])], 4)
        r = self.run_score(52, [self.issue("unauthorized", [1, 2])], 2)
        self.assertEqual((r["absolute_rule_triggered"], r["overall_quality_band"]), (False, "FAIL"))

    def test_provenance_is_recorded_and_inherited_needs_a_quote(self):
        r = self.run_score(10, [self.issue("incorrect", [1], provenance="inherited_from_golden", inherited_quote="Golden: $16,413 contractor spend")], 2)
        self.assertEqual(r["provenance_counts"]["inherited_from_golden"], 1)
        self.assertEqual(r["verdict"], "FAIL")
        self.assertFalse(r["repair_free"])

    def test_verifier_fields_and_dimension_are_outside_rubric_scoring(self):
        for key in ("platform_defects", "all_failing", "baseline_verifier"):
            record = tally(10, [], 5)
            record[key] = []
            with self.subTest(field=key), self.assertRaisesRegex(ValueError, "outside this rubric evaluation"):
                calculate(record, json.loads(candidate()) * 10)
        record = tally(10, [], 5)
        record["dimensions"]["all_failing"] = dict(score=5, reason="Irrelevant verifier dimension.")
        with self.assertRaisesRegex(ValueError, "six static QC dimensions"):
            calculate(record, json.loads(candidate()) * 10)

    def test_unresolved_is_not_a_fabricated_fail_or_score(self):
        r = self.run_score(10, [], 5, unresolved=["Cannot establish source scope yet."])
        self.assertEqual((r["verdict"], r["verdict_score"], r["execution_status"]), ("NON-FAIL", None, "PARTIAL"))
        r = self.run_score(10, [self.issue("incorrect", [1, 2])], 2, unresolved=["Other sources pending."])
        self.assertEqual((r["verdict"], r["verdict_score"]), ("FAIL", 2))

    def test_lowest_dimension_controls_final_score(self):
        record = tally(10, [], 5)
        record["dimensions"]["process"]["score"] = 2
        self.assertEqual(calculate(record, json.loads(candidate()) * 10)["verdict_score"], 2)

    def test_category_balance_fails_only_without_outcome_rows(self):
        record = tally(2, [], 5)
        rubric = json.loads(candidate()) * 2
        rubric[0] = {**rubric[0], "category": "Process"}
        self.assertEqual(calculate(record, rubric)["verdict"], "PASS")
        rubric[1] = {**rubric[1], "category": "Process"}
        with self.assertRaisesRegex(ValueError, "category balance"):
            calculate(tally(2, [], 5), rubric)

    def test_strict_specificity_severities_do_not_depend_on_impact_labels(self):
        # Local override 2026-10-17: Overly Broad is Major, the same level as Overly Specific.
        for kind, severity in (("overly_specific", "Major"), ("overly_broad", "Major"),
                               ("harmless_specificity", "Minor")):
            for impact in ("precision_only", "accepts_wrong", "rejects_correct"):
                with self.subTest(kind=kind, impact=impact):
                    minor = severity == "Minor"  # rubric-flow-v2: 1 Minor in 20 rows is NON-FAIL 3
                    score = self.run_score(20, [self.issue(kind, [1], impact=impact)], 3 if minor else 2)
                    self.assertEqual(score["severity_counts"][severity], 1)
                    self.assertEqual(score["verdict"], "NON-FAIL" if minor else "FAIL")
                    self.assertFalse(score["repair_free"])

    def test_overly_specific_rejecting_valid_paths_counts_toward_major_threshold(self):
        issues = [self.issue("overly_specific", [1]), self.issue("overly_specific", [2])]
        score = self.run_score(10, issues, 2)
        self.assertEqual(score["fractions"]["major"], [2, 10])
        self.assertEqual(score["overall_quality_band"], "FAIL")

    def test_cascading_failure_overlap_group_counts_once_after_major_rows(self):
        rows = [self.issue("non_atomic", [r]) for r in range(1, 8)]
        group = self.issue("duplicate", list(range(1, 9)), duplicate_kind="OVERLAP_GROUP",
                           overlap_group_id="delivered-to-both")
        score = self.run_score(11, rows + [group], 2)
        self.assertEqual(score["severity_counts"], {"Major": 7, "Moderate": 1, "Minor": 0})
        self.assertEqual(score["overlap_groups"]["delivered-to-both"]["eligible_rows"], [8])

    def test_predicted_all_fail_gate(self):
        def record_with(entries, issues):
            record = tally(20, issues, 2)
            record["predicted_all_fail"] = entries
            return record
        af = lambda row: dict(row=row, basis="target_data_absent",
                              reason="The expected record is absent from every visible source.")
        one = [self.issue("incorrect", [1])]
        two = one + [self.issue("incorrect", [2])]
        single = calculate(record_with([af(1)], one), json.loads(candidate()) * 20)
        self.assertEqual((single["all_fail_gate"], single["verdict"]), ("PASS", "FAIL"))
        double = calculate(record_with([af(1), af(2)], two), json.loads(candidate()) * 20)
        self.assertEqual((double["all_fail_gate"], double["verdict"], double["verdict_score"]), ("FAIL", "FAIL", 2))
        self.assertEqual(double["predicted_all_fail_rows"], [1, 2])
        with self.assertRaisesRegex(ValueError, "needs its recorded defect"):
            calculate(record_with([af(3)], one), json.loads(candidate()) * 20)
        with self.assertRaisesRegex(ValueError, "unknown predicted all-fail basis"):
            calculate(record_with([dict(af(1), basis="looks hard")], one), json.loads(candidate()) * 20)
        missing = tally(20, one, 4)
        del missing["predicted_all_fail"]
        with self.assertRaisesRegex(ValueError, "record predicted_all_fail"):
            calculate(missing, json.loads(candidate()) * 20)

    def test_weight_thresholds_are_inclusive_and_separate_from_overall_quality(self):
        # Thresholds apply to distinct one-/two-level disagreements, not a
        # combined denominator or a new Major issue in overall quality.
        for changed, assigned, band in ((2, 5, "FAIL"), (3, 5, "FAIL"),
                                        (5, 3, "FAIL"), (6, 3, "FAIL")):
            with self.subTest(changed=changed, assigned=assigned):
                rubric = [json.loads(candidate())[0] for _ in range(20)]
                record = tally(20, [], 5)
                for row in rubric[:changed]:
                    row["weight"] = assigned
                record["hard_gates"]["weights"]["result"] = "FAIL"
                record["dimensions"]["criteria_weights"]["score"] = 2 if band == "FAIL" else 4
                score = calculate(record, rubric)
                self.assertEqual(score["criteria_weights"]["band"], band)
                self.assertEqual(score["overall_quality_band"], "PASS")
                self.assertEqual(score["fractions"]["all"], [0, 20])
                self.assertFalse(score["repair_free"])
                self.assertEqual(score["verdict"], band)

    def test_unresolved_weight_cannot_be_published_or_invent_a_failure(self):
        record = tally(1, [], 5)
        record["weight_reviews"][0].update(work_kind="UNRESOLVED", expected_weight=None)
        score = calculate(record, json.loads(candidate()))
        self.assertEqual((score["verdict"], score["verdict_score"], score["execution_status"]),
                         ("NON-FAIL", None, "PARTIAL"))
        self.assertFalse(score["repair_free"])

    def test_weight_review_inventory_and_work_kind_are_enforced(self):
        for update in (dict(weight_reviews=[]),
                       dict(weight_reviews=[dict(row=1, expected_weight=5, work_kind="direct_lookup",
                                                source_ids=["P1"], reason="Inconsistent expected value.")]),
                       dict(weight_reviews=[dict(row=True, expected_weight=1, work_kind="direct_lookup",
                                                source_ids=["P1"], reason="Boolean is not a criterion index.")])):
            with self.subTest(update=update), self.assertRaises(ValueError):
                calculate({**tally(1, [], 5), **update}, json.loads(candidate()))

    def test_legacy_score_format_cannot_authorize_current_policy(self):
        record = tally(1, [], 5)
        for old_version in (2, 3, 4, True):
            record["format_version"] = old_version
            with self.subTest(version=old_version), self.assertRaisesRegex(ValueError, "format 5"):
                calculate(record, json.loads(candidate()))


class EvidenceAndRubricTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.addCleanup(patch.stopall)
        patch.object(writer, "REPOSITORY", self.root).start()
        patch.object(inputs, "REPOSITORY", self.root).start()
        inputs.save_input("universe", content=b"2026-02-14\n")  # task date (hg_universe.py)
        inputs.save_input("prompt", content=b"Report the current download size.")
        inputs.save_input("golden", content=b"The current download size is 214 MB.")
        inputs.save_input("task-details", content=b"Robert, Executive")
        inputs.clear_input("injection", confirmed_unused=True)
        golden_pass(self.root)
        inputs.save_input("rubric", content=candidate().encode())
        (self.root / DRAFT).parent.mkdir(parents=True, exist_ok=True)
        (self.root / DRAFT).write_text(candidate())
        self.receipt = dict(review_policy=POLICY, review_iteration=1,
                            reviewed_json_sha256=digest(candidate().encode()),
                            review_context_sha256=review_context(self.root)["sha256"])
        self.record = review_record(self.receipt, candidate())

    def validate(self, publishing=True):
        return validate_record(self.record, json.loads(candidate()), self.receipt, root=self.root, publication=publishing)

    def test_restriction_needs_real_quote_and_incorporation(self):
        self.record["sources"][0]["quote"] = "Use exactly two headings."
        with self.assertRaisesRegex(ValueError, "absent"):
            self.validate()

    def test_golden_or_handbook_cannot_be_relabelled_as_prompt(self):
        self.record["sources"].append(dict(id="H1", path="Evals/task_inputs/08_Golden_Answer.md",
                                          sha256=digest(b"The current download size is 214 MB."), quote="214 MB", visibility="VISIBLE", access="Visible answer"))
        self.record["requirements"][0]["authority_chain"] = ["H1"]
        with self.assertRaisesRegex(ValueError, "actual saved prompt"):
            self.validate()
        self.record["requirements"][0]["authority_chain"] = ["P1", "H1"]
        with self.assertRaisesRegex(ValueError, "preceding authority"):
            self.validate()

    def test_unsupported_restriction_blocks_even_with_pass_labels(self):
        self.record["rows"][0]["restriction_review"]["restrictions"] = [dict(
            field="title", quote="reports", status="UNSUPPORTED", reason="Hypothetical restriction judgment for invariant test.",
            counterexample="Requested evidence delivered through an authorized alternative.")]
        self.assertTrue(self.validate(False)["review_open_items"])
        with self.assertRaisesRegex(ValueError, "UNSUPPORTED restriction"):
            self.validate()

    def branch(self, result="ACCEPT"):
        self.record["alternative_review"]["branches"] = [dict(id="A1", source_id="P1", quote="Report the current download size.",
            validity="SUPPORTED", authority_chain=["P1"], example="214.0 MB", tested_rows=[1],
            rejecting_rows=[1] if result == "REJECT" else [], result=result, reason="Same requested value in equivalent notation.")]

    def test_valid_alternative_rejection_cannot_hide_behind_generic_passing_case(self):
        self.branch("REJECT")
        with self.assertRaisesRegex(ValueError, "valid alternative"):
            self.validate()
        self.branch("ACCEPT")
        self.assertFalse(self.validate()["review_open_items"])

    def test_alternative_must_test_whole_set_and_match_rejecting_rows(self):
        self.branch()
        for change in (dict(tested_rows=[]), dict(rejecting_rows=[1])):
            self.branch()
            self.record["alternative_review"]["branches"][0].update(change)
            with self.assertRaises(ValueError):
                self.validate()

    def test_inaccessible_authority_is_open_not_silent_pass(self):
        self.record["sources"][0]["visibility"] = "UNRESOLVED"
        self.assertTrue(self.validate(False)["review_open_items"])
        with self.assertRaises(ValueError):
            self.validate()

    def test_json_pointer_cannot_borrow_quote_from_another_record(self):
        path = self.root / "sources.json"
        path.write_text(json.dumps({"current": "Old $6,250 is not current", "private": "Old total $8,250"}))
        anchor = dict(path="sources.json", sha256=digest(path.read_bytes()), pointer="/current", quote="$8,250")
        with self.assertRaisesRegex(ValueError, "absent"):
            EvidenceReader(self.root).quote(anchor)
        anchor["quote"] = "$6,250"
        self.assertIn("$6,250", EvidenceReader(self.root).quote(anchor))

    def test_source_line_bounds_cannot_borrow_another_records_value(self):
        path = self.root / "sources.sql"
        path.write_text("Public tracker: old $6,250 is no longer current.\nPrivate total: $8,250.\n")
        anchor = dict(path="sources.sql", sha256=digest(path.read_bytes()), line_start=1, line_end=1, quote="$8,250")
        with self.assertRaisesRegex(ValueError, "absent"):
            EvidenceReader(self.root).quote(anchor)
        anchor["quote"] = "$6,250"
        self.assertIn("$6,250", EvidenceReader(self.root).quote(anchor))

    def test_duplicate_outcome_ownership_and_separate_required_surfaces(self):
        from hg_rubric_acceptance import validate_acceptance
        record = copy.deepcopy(self.record)
        record["rows"].append(copy.deepcopy(record["rows"][0]))
        record["rows"][1]["row"] = 2
        proposal = json.loads(candidate()) * 2
        found = validate_acceptance(record, proposal, self.root, {})
        self.assertTrue(any("duplicate grading" in x for x in found))
        outcome = copy.deepcopy(record["requirements"][0]["outcomes"][0])
        outcome.update(id="O2", output="Separately requested memo")
        record["requirements"][0]["outcomes"].append(outcome)
        record["rows"][1]["atomicity"]["outcome_ids"] = ["O2"]
        self.assertFalse(validate_acceptance(record, proposal, self.root, {}))

    def test_old_record_format_no_longer_authorizes_publication(self):
        self.record["format_version"] = 2
        with self.assertRaisesRegex(ValueError, "format_version"):
            self.validate()

    def test_unusable_supplied_array_can_report_schema_fail_without_fake_percentage(self):
        from hg_review_score import validate_score
        for raw in ("[]", "not JSON", "{}"):
            inputs.save_input("rubric",content=raw.encode())
            path=self.root / "Evals/task_inputs/09_Rubrics.json"
            record=dict(format_version=__import__("hg_review_score").FORMAT_VERSION, review_mode="AUDIT", rubric_path="Evals/task_inputs/09_Rubrics.json",
                        reviewed_json_sha256=digest(path.read_bytes()), review_context_sha256=review_context(self.root)["sha256"],
                        eval_release=__import__('hg_eval_release').snapshot('rubric'), schema_only=True, issues=[], hard_gates=dict(schema=dict(result="FAIL",reason="Unusable criterion array")),
                        hard_gate_score=2, unresolved=["No usable criteria to review."])
            r=validate_score(self.root,json.dumps(record))
            self.assertEqual(r["verdict"],"FAIL")
            self.assertIsNone(r["fractions"])

    def test_audit_cannot_score_a_different_array_than_the_saved_input(self):
        from hg_review_score import validate_score
        inputs.save_input("rubric",content=candidate("Different submitted criterion").encode())
        score=score_record(self.root,mode="AUDIT")
        score.update(rubric_path=DRAFT.as_posix(), reviewed_json_sha256=digest((self.root / DRAFT).read_bytes()))
        with self.assertRaisesRegex(ValueError,"actual saved rubric"):
            validate_score(self.root,json.dumps(score))

    def test_changed_score_record_cannot_save_old_pass(self):
        report = review(self.receipt)
        writer.save_output("rubric", report)
        score = json.loads((self.root / SCORE_PATH).read_text())
        score["dimensions"]["process"]["score"] = 3
        (self.root / SCORE_PATH).write_text(json.dumps(score))
        with self.assertRaises(ValueError):
            writer.save_output("rubric", report)


class GoldenEvidenceTests(unittest.TestCase):
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
        self.receipt = golden.start_review(self.root)
        self.record = evidence_record(self.receipt)

    def validate(self, passing=True):
        return golden.validate_record(self.root, json.dumps(self.record), passing=passing)

    def test_actual_saved_answer_quote_required(self):
        self.record["claims"][0]["golden_quote"] = "Current size is 215 MB"
        with self.assertRaisesRegex(ValueError, "absent"):
            self.validate()

    def test_source_quote_must_exist_even_when_hash_matches(self):
        self.record["sources"][0]["quote"] = "Current size: 215 MB"
        with self.assertRaisesRegex(ValueError, "absent"):
            self.validate()

    def test_inaccessible_only_support_cannot_pass(self):
        self.record["sources"][0]["visibility"] = "INACCESSIBLE"
        result = self.validate(False)
        self.assertEqual((result["verdict"], result["verdict_score"]), ("NON-FAIL", None))
        with self.assertRaisesRegex(ValueError, "inaccessible"):
            self.validate()

    def test_rejected_private_source_does_not_poison_independent_visible_support(self):
        self.record["sources"].append({**self.record["sources"][0], "id": "S2", "visibility": "INACCESSIBLE", "access": "Private source considered but not needed."})
        self.record["claims"][0]["source_ids"].append("S2")
        self.assertEqual(self.validate()["verdict"], "PASS")

    def test_claimed_repair_must_exist_in_current_saved_text(self):
        self.record["repairs"] = [dict(old_quote="214 MB", golden_quote="215 MB", claim_ids=["C1"], reason="Claims an edit not actually made.")]
        with self.assertRaisesRegex(ValueError, "absent"):
            self.validate()
        self.record["repairs"][0].update(old_quote="Wrong older measurement", golden_quote="214 MB")
        self.assertEqual(self.validate()["verdict"], "PASS")

    def test_inconsistent_alternative_fails_and_incomplete_review_is_provisional(self):
        self.record["alternative_review"]["branches"] = [dict(golden_quote="214 MB", authority_chain=["P1"], example="Contradictory hypothetical branch.", result="FAIL", reason="Recorded conflict with main answer.", defect_class="contradiction", repair_owner="contributor")]
        self.assertEqual(self.validate(False)["verdict"], "FAIL")
        self.record["alternative_review"]["branches"] = []
        self.record["alternative_review"]["complete"] = False
        self.assertEqual(self.validate(False)["verdict"], "NON-FAIL")

    def test_chronology_conflict_prevents_pass(self):
        self.record["chronology"]["comparisons"] = [dict(source_ids=["S1"], claim_ids=["C1"], result="FAIL", reason="Declared supersession not supported by compared versions.", defect_class="wrong_value", repair_owner="contributor")]
        self.assertEqual(self.validate(False)["verdict"], "FAIL")
        with self.assertRaises(ValueError):
            self.validate()

    def test_bound_report_cannot_disagree_with_recorded_verdict(self):
        self.receipt.update(writer.save_output("golden-review", json.dumps(self.record)))
        with self.assertRaisesRegex(ValueError, "contradicts"):
            writer.save_output("golden", report(self.receipt, "FAIL"))

    def test_old_record_relabelled_with_current_policy_is_rejected(self):
        self.record["format_version"] = 1
        with self.assertRaisesRegex(ValueError, "format_version"):
            self.validate()


if __name__ == "__main__":
    unittest.main()

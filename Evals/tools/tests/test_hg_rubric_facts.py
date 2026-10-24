import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from hg_review_evidence import EvidenceReader
from hg_rubric_facts import validate_facts


class RubricFactsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = {"size_mb": 214, "bytes": 214000000, "ratio": 0.25,
                     "byte_unit": "B", "ratio_unit": "ratio", "mb_unit": "MB", "currency_unit": "USD",
                     "fraction": 214.125, "count": 3, "zero": 0, "date": "2026-09-24",
                     "instant": "2026-09-24T15:00:00Z", "literal": "PR #438",
                     "fourteen": 14, "fifteen": 15, "nineteen": 19, "one": 1,
                     "requested_issue_count": 1, "company_name": "One", "big_count": 1234567,
                     "twenty_one": 21, "hundred_and_four": 104,
                     "rows": [{"id": "A", "game": "x", "cost": "1.10"},
                              {"id": "A", "game": "x", "cost": "2.20"},
                              {"id": "B", "game": "y", "cost": "4.40"}], "empty": []}
        self.raw = json.dumps(self.data, sort_keys=True).encode()
        (self.root / "source.json").write_bytes(self.raw)
        self.known = {"S1": dict(id="S1", path="source.json", sha256=hashlib.sha256(self.raw).hexdigest(),
                                  quote=self.raw.decode(), pointer="", visibility="VISIBLE")}

    def number(self, quote="214 MB", pointer="/size_mb", **calculation):
        if "conversion" not in calculation:
            calculation.setdefault("source_unit", dict(source_id="S1", pointer="/mb_unit"))
        return dict(id="F1", quote=quote, kind="NUMBER", source_ids=["S1"], reason="Measured from selected source.",
                    calculation=dict(op="direct", operands=[dict(source_id="S1", pointer=pointer)], **calculation))

    def selected(self, quote, pointer, kind="LITERAL", **extra):
        return dict(id="F1", quote=quote, kind=kind, source_ids=["S1"], reason="Exact source field.",
                    selection=dict(source_id="S1", pointer=pointer), **extra)

    def run_claims(self, claims, title=None, review_extra=None):
        if title is None:
            title = "The Agent reports " + claims[0]["quote"] + "."
        review = dict(complete=True, reason="All factual checks enumerated.", claims=claims)
        review.update(review_extra or {})
        return validate_facts(review, {"title": title}, EvidenceReader(self.root), self.known)

    def clean(self, claim, **kw):
        result = self.run_claims([claim], **kw)
        self.assertEqual(result["mismatches"], [])
        self.assertEqual(result["unresolved"], [])
        return result

    def rejects(self, claim, **kw):
        with self.assertRaises(ValueError):
            self.run_claims([claim], **kw)

    def test_direct_999_against_214_is_mismatch(self):
        result = self.run_claims([self.number("999 MB")])
        self.assertEqual(result["mismatches"][0]["expected"], "999")
        self.assertEqual(result["mismatches"][0]["actual"], "214")

    def test_spelled_fourteen_matches_source_fourteen(self):
        self.clean(self.number("fourteen", "/fourteen"))

    def test_spelled_fourteen_mismatches_source_fifteen(self):
        result = self.run_claims([self.number("fourteen", "/fifteen")])
        self.assertEqual(result["mismatches"][0]["expected"], "14")
        self.assertEqual(result["mismatches"][0]["actual"], "15")

    def test_spelled_nineteen_matches(self):
        self.clean(self.number("nineteen", "/nineteen"))

    def not_a_claim(self, quote, reason="The token is the label under review, not a source quantity."):
        return dict(id="F1", quote=quote, kind="NOT_A_CLAIM", source_ids=[], reason=reason)

    def test_not_a_claim_covers_the_token_without_reporting_unresolved(self):
        """A numeric token that asserts nothing must not force a PARTIAL review."""
        result = self.run_claims([self.not_a_claim("3")],
                                 title="The Agent rejects the claimed Day 3 token bump.")
        self.assertEqual(result["unresolved"], [])
        self.assertEqual(result["mismatches"], [])
        self.assertEqual([c["quote"] for c in result["non_factual"]], ["3"])

    def test_not_a_claim_covers_the_rows_own_quantifier(self):
        result = self.run_claims([self.not_a_claim("one")],
                                 title="The Agent grounds the verdict in at least one finding.")
        self.assertEqual(result["unresolved"], [])
        self.assertEqual([c["quote"] for c in result["non_factual"]], ["one"])

    def test_not_a_claim_may_cover_a_date_token(self):
        result = self.run_claims([self.not_a_claim("2026-09-24")],
                                 title="The Agent cites the 2026-09-24 template name verbatim.")
        self.assertEqual(result["unresolved"], [])
        self.assertEqual([c["quote"] for c in result["non_factual"]], ["2026-09-24"])

    def test_not_a_claim_cannot_cite_a_source(self):
        """Declaring a token non-factual and then citing evidence for it is contradictory."""
        claim = dict(id="F1", quote="214", kind="NOT_A_CLAIM", source_ids=["S1"], reason="Contradictory.")
        self.rejects(claim, title="The Agent reports 214 MB.")

    def test_not_a_claim_still_needs_a_reason(self):
        claim = dict(id="F1", quote="3", kind="NOT_A_CLAIM", source_ids=[], reason="   ")
        self.rejects(claim, title="The Agent rejects the Day 3 bump.")

    def test_not_a_claim_cannot_carry_a_comparison(self):
        claim = dict(id="F1", quote="3", kind="NOT_A_CLAIM", source_ids=[], reason="Label only.",
                     selection=dict(source_id="S1", pointer="/count"))
        self.rejects(claim, title="The Agent rejects the Day 3 bump.")

    def test_an_uncovered_numeric_token_is_still_unresolved(self):
        """The coverage sweep must keep firing; NOT_A_CLAIM is opt-in, not a blanket waiver."""
        result = self.run_claims([self.not_a_claim("3")],
                                 title="The Agent rejects the Day 3 bump across 12 runs.")
        self.assertEqual([c["quote"] for c in result["unresolved"]], ["12"])

    def test_spelled_numeric_semantic_is_unresolved(self):
        claim = dict(id="F1", quote="fourteen", kind="SEMANTIC", source_ids=["S1"], reason="Reviewer asserts a count.", status="VERIFIED")
        self.assertTrue(self.run_claims([claim])["unresolved"])

    def test_spelled_missing_number_is_unresolved(self):
        result = self.run_claims([], title="The Agent reports nineteen merged PRs.")
        self.assertEqual(result["unresolved"][0]["quote"], "nineteen")

    def test_one_action_count_can_use_prompt_source(self):
        self.known["S1"]["role"] = "task_prompt"
        self.clean(self.number("one", "/requested_issue_count"), title="The Agent creates one issue.")

    def test_source_backed_name_one_is_not_forced_numeric(self):
        self.clean(self.selected("One", "/company_name"), title="The Agent names One as the company.")

    def test_standard_spelled_compounds(self):
        for spelling, pointer in [("twenty-one", "/twenty_one"), ("one hundred and four", "/hundred_and_four"),
                                  ("one million two hundred thirty-four thousand five hundred sixty-seven", "/big_count")]:
            with self.subTest(spelling=spelling):
                self.clean(self.number(spelling, pointer))

    def test_spelled_count_with_unit(self):
        self.clean(self.number("fourteen PRs", "/fourteen"))

    def test_zero_spelling(self):
        self.clean(self.number("zero", "/zero"))

    def test_malformed_spelled_quantities_rejected(self):
        for spelling in ["twenty thirteen", "one and two", "one million thousand", "zero hundred", "one hundred hundred"]:
            with self.subTest(spelling=spelling):
                self.rejects(self.number(spelling, "/one"))

    def test_unsupported_quantity_cannot_be_a_fake_unit(self):
        for spelling in ["one billion", "one point five", "one dozen", "one half"]:
            with self.subTest(spelling=spelling):
                self.rejects(self.number(spelling, "/one"))

    def test_partial_cardinal_cannot_hide_unsupported_scale(self):
        result = self.run_claims([self.number("one", "/one")], title="The Agent reports one billion records.")
        self.assertTrue(any(item.get("quote") == "one billion" for item in result["unresolved"]))

    def test_negative_cardinal_cannot_be_checked_as_positive(self):
        result = self.run_claims([self.number("one", "/one")], title="The Agent reports minus one.")
        self.assertTrue(any(item.get("quote") == "minus one" for item in result["unresolved"]))

    def test_ordinals_and_non_numeric_compounds_are_out_of_scope(self):
        result = self.run_claims([], title="The Agent reports the first PR and the one-time setup from last quarter.")
        self.assertEqual(result["unresolved"], [])

    def test_malformed_sequence_cannot_be_split_to_evade_whole_quantity(self):
        first = self.number("twenty", "/one")
        second = self.number("thirteen", "/one")
        second["id"] = "F2"
        result = self.run_claims([first, second], title="The Agent reports twenty thirteen records.")
        self.assertTrue(any(item.get("quote") == "twenty thirteen" for item in result["unresolved"]))

    def test_equivalent_214_decimal_passes(self):
        self.clean(self.number("214.0 MB"))

    def test_direct_wrong_unit_mismatches_even_equal_scalar(self):
        result = self.run_claims([self.number("214 GB")])
        self.assertEqual(result["mismatches"][0]["unit"], "GB")
        self.assertEqual(result["mismatches"][0]["actual_unit"], "MB")

    def test_recognized_unit_missing_binding_is_unresolved(self):
        claim = self.number()
        del claim["calculation"]["source_unit"]
        result = self.run_claims([claim])
        self.assertTrue(result["unresolved"])
        self.assertFalse(result["mismatches"])

    def test_numeric_quote_cannot_omit_wrong_adjacent_unit(self):
        result = self.run_claims([self.number("214")], title="The Agent reports 214 GB.")
        self.assertTrue(result["mismatches"])
        self.assertFalse(result["unresolved"])

    def test_numeric_quote_can_use_correct_adjacent_unit(self):
        self.clean(self.number("214"), title="The Agent reports 214 MB.")

    def test_numeric_quote_cannot_omit_currency_prefix(self):
        result = self.run_claims([self.number("214")], title="The Agent reports $214.")
        self.assertTrue(result["mismatches"])

    def test_correct_currency_binding(self):
        self.clean(self.number("214", source_unit=dict(source_id="S1", pointer="/currency_unit")),
                   title="The Agent reports $214.")

    def test_literal_cannot_omit_adjacent_unit(self):
        self.data["literal_measure"] = "214"
        raw = json.dumps(self.data, sort_keys=True).encode()
        (self.root / "source.json").write_bytes(raw)
        self.known["S1"].update(sha256=hashlib.sha256(raw).hexdigest(), quote=raw.decode())
        result = self.run_claims([self.selected("214", "/literal_measure")], title="The Agent reports 214 GB.")
        self.assertTrue(result["unresolved"])

    def test_explicit_correct_unit_conversion_passes(self):
        self.clean(self.number("0.214 GB", "/size_mb", conversion={"from": "MB", "to": "GB", "source_unit": {"source_id": "S1", "pointer": "/mb_unit"}}))

    def test_unsupported_compound_unit_is_unresolved(self):
        result = self.run_claims([self.number("214")], title="The Agent reports 214 MB/s.")
        self.assertTrue(result["unresolved"])
        self.assertFalse(result["mismatches"])

    def test_separate_expected_value_cannot_lie(self):
        claim = self.number("999 MB")
        claim["expected"] = 214
        self.rejects(claim)

    def test_quote_must_appear_in_title(self):
        self.rejects(self.number(), title="The Agent reports 999 MB.")

    def test_missing_numeric_coverage_stays_unresolved(self):
        result = self.run_claims([], title="The Agent reports 999 MB.")
        self.assertTrue(result["unresolved"])

    def test_semantic_cannot_hide_number(self):
        claim = dict(id="F1", quote="999 MB", kind="SEMANTIC", source_ids=["S1"], reason="Claims this is correct.", status="VERIFIED")
        result = self.run_claims([claim])
        self.assertTrue(result["unresolved"])
        self.assertIn("not an executable proof", result["computed"][0]["method"])

    def test_semantic_contradiction_is_mismatch(self):
        claim = dict(id="F1", quote="the approved PR is absent", kind="SEMANTIC", source_ids=["S1"], reason="Source contains the approved PR.", status="CONTRADICTED")
        self.assertTrue(self.run_claims([claim])["mismatches"])

    def test_semantic_without_evidence_rejected(self):
        claim = dict(id="F1", quote="the PR is present", kind="SEMANTIC", source_ids=[], reason="Unsupported assertion.", status="VERIFIED")
        self.rejects(claim)

    def test_explicit_unresolved_numeric_is_not_fake_failure(self):
        claim = dict(id="F1", quote="999 MB", kind="UNRESOLVED", source_ids=[], reason="Measurement source is unavailable.")
        result = self.run_claims([claim])
        self.assertEqual(len(result["unresolved"]), 1)
        self.assertEqual(result["mismatches"], [])

    def test_count(self):
        claim = self.number("3", "/rows")
        claim["calculation"]["op"] = "count"
        self.clean(claim)

    def test_distinct_count(self):
        claim = self.number("2", "/rows")
        claim["calculation"]["op"] = "distinct_count"
        claim["calculation"]["operands"][0]["field"] = "/id"
        self.clean(claim)

    def test_decimal_sum(self):
        claim = self.number("7.70", "/rows")
        claim["calculation"]["op"] = "sum"
        claim["calculation"]["operands"][0]["field"] = "/cost"
        self.clean(claim)

    def test_filtered_sum(self):
        claim = self.number("3.30", "/rows")
        claim["calculation"]["op"] = "sum"
        claim["calculation"]["operands"][0].update(field="/cost", filters=[dict(pointer="/game", equals="x")])
        self.clean(claim)

    def test_min_max(self):
        for operation, expected in [("min", "1.10"), ("max", "4.40")]:
            with self.subTest(operation=operation):
                claim = self.number(expected, "/rows")
                claim["calculation"]["op"] = operation
                claim["calculation"]["operands"][0]["field"] = "/cost"
                self.clean(claim)

    def test_difference(self):
        claim = self.number("211", "/size_mb")
        claim["calculation"]["op"] = "difference"
        claim["calculation"]["operands"].append(dict(source_id="S1", pointer="/count"))
        self.clean(claim)

    def test_ratio(self):
        claim = self.number("3", "/count")
        claim["calculation"]["op"] = "ratio"
        claim["calculation"]["operands"].append(dict(source_id="S1", pointer="/rows/0/cost"))
        self.assertTrue(self.run_claims([claim])["mismatches"])

    def test_zero_denominator_rejected(self):
        claim = self.number("0", "/count")
        claim["calculation"]["op"] = "ratio"
        claim["calculation"]["operands"].append(dict(source_id="S1", pointer="/zero"))
        self.rejects(claim)

    def test_unit_conversion(self):
        self.clean(self.number("214 MB", "/bytes", conversion={"from": "B", "to": "MB", "source_unit": {"source_id": "S1", "pointer": "/byte_unit"}}))

    def test_percent_conversion(self):
        self.clean(self.number("25%", "/ratio", conversion={"from": "ratio", "to": "%", "source_unit": {"source_id": "S1", "pointer": "/ratio_unit"}}))

    def test_source_unit_cannot_be_invented(self):
        self.rejects(self.number("0.214 MB", "/size_mb", conversion={"from": "KB", "to": "MB", "source_unit": {"source_id": "S1", "pointer": "/mb_unit"}}))

    def test_conversion_without_source_unit_rejected(self):
        self.rejects(self.number("214 MB", "/bytes", conversion={"from": "B", "to": "MB"}))

    def test_arbitrary_conversion_rejected(self):
        self.rejects(self.number("999 MB", conversion={"from": "MB", "to": "MB", "factor": "4.668224"}))

    def test_conversion_target_must_match_title(self):
        self.rejects(self.number("214 MB", "/bytes", conversion={"from": "B", "to": "GB"}))

    def test_rounding_to_displayed_precision(self):
        self.clean(self.number("214.13", "/fraction", rounding={"places": 2, "mode": "HALF_UP"}))

    def test_rounding_cannot_hide_arbitrary_disagreement(self):
        self.assertTrue(self.run_claims([self.number("999", rounding={"places": 0, "mode": "HALF_UP"})])["mismatches"])

    def test_tolerance_rejected(self):
        self.rejects(self.number("999", tolerance=1000))

    def test_formula_rejected(self):
        claim = self.number("999")
        claim["calculation"]["op"] = "eval"
        self.rejects(claim)

    def test_empty_aggregation_requires_deliberate_choice(self):
        claim = self.number("0", "/empty")
        claim["calculation"]["op"] = "count"
        self.rejects(claim)
        claim["calculation"].update(allow_empty=True, empty_reason="A verified empty list has zero records.")
        self.clean(claim)

    def test_empty_min_still_rejected(self):
        claim = self.number("0", "/empty", allow_empty=True, empty_reason="Deliberately empty.")
        claim["calculation"]["op"] = "min"
        self.rejects(claim)

    def test_date(self):
        self.clean(self.selected("2026-09-24", "/date", kind="DATE"))

    def test_equivalent_timezones(self):
        self.clean(self.selected("2026-09-24T08:00:00-07:00", "/instant", kind="DATE"))

    def test_naive_timestamp_rejected(self):
        self.rejects(self.selected("2026-09-24T15:00:00", "/instant", kind="DATE"))

    def test_date_projection_is_explicit(self):
        claim = self.selected("2026-09-24", "/instant", kind="DATE")
        self.assertTrue(self.run_claims([claim])["mismatches"])
        claim["comparison"] = "utc_date"
        self.clean(claim)

    def test_exact_id_literal(self):
        self.clean(self.selected("PR #438", "/literal"))

    def test_literal_substring_not_enough(self):
        self.assertTrue(self.run_claims([self.selected("438", "/literal")])["mismatches"])

    def test_literal_number_coercion_rejected(self):
        self.rejects(self.selected("214", "/size_mb"))

    def test_stale_source_rejected(self):
        (self.root / "source.json").write_text('{"size_mb":999}')
        self.rejects(self.number())

    def test_source_visibility_unknown_remains_unresolved(self):
        self.known["S1"]["visibility"] = "UNRESOLVED"
        result = self.run_claims([self.number()])
        self.assertTrue(result["unresolved"])
        self.assertFalse(result["mismatches"])

    def test_inaccessible_source_remains_unresolved(self):
        self.known["S1"]["visibility"] = "INACCESSIBLE"
        self.assertTrue(self.run_claims([self.number()])["unresolved"])

    def test_unknown_source_id_rejected(self):
        claim = self.number()
        claim["source_ids"] = ["NOT_REAL"]
        self.rejects(claim)

    def test_missing_pointer_rejected(self):
        self.rejects(self.number(pointer="/missing"))

    def test_anchor_scope_cannot_expand_to_other_fields(self):
        self.known["S1"].update(pointer="/rows/0", quote=json.dumps(self.data["rows"][0], sort_keys=True))
        self.rejects(self.number(pointer="/size_mb"))

    def test_partial_quote_cannot_authorize_whole_record(self):
        self.known["S1"]["quote"] = '"size_mb": 214'
        self.rejects(self.number(pointer="/bytes"))

    def test_precise_scalar_anchor(self):
        self.known["S1"].update(pointer="/size_mb", quote="214")
        claim = self.number("214", pointer="")
        del claim["calculation"]["source_unit"]
        self.clean(claim)

    def test_nan_infinity_rejected(self):
        for value in ["NaN", "Infinity", "-Infinity"]:
            with self.subTest(value=value):
                self.known["S1"].update(pointer="/rows/0/cost", quote=value)
                self.data["rows"][0]["cost"] = value
                raw = json.dumps(self.data).encode()
                (self.root / "source.json").write_bytes(raw)
                self.known["S1"]["sha256"] = hashlib.sha256(raw).hexdigest()
                self.rejects(self.number(pointer=""))

    def test_duplicate_ids_rejected(self):
        claim = self.number()
        with self.assertRaises(ValueError):
            self.run_claims([claim, copy.deepcopy(claim)])

    def test_repeated_quote_needs_offset(self):
        claim = self.number("214")
        title = "The Agent reports 214 MB and 214 dollars."
        self.rejects(claim, title=title)
        claim["start"] = title.index("214")
        result = self.run_claims([claim], title=title)
        self.assertTrue(result["unresolved"])

    def test_incomplete_review_stays_unresolved(self):
        result = self.run_claims([self.number()], review_extra={"complete": False})
        self.assertTrue(result["unresolved"])

    def test_digits_cannot_be_checked_as_separate_invented_numbers(self):
        # Splitting 214 into 2 and 14 cannot make a whole numeric assertion verified.
        claims = [dict(id="F1", quote="2", kind="UNRESOLVED", source_ids=[], reason="No source."),
                  dict(id="F2", quote="14", kind="UNRESOLVED", source_ids=[], reason="No source.")]
        result = self.run_claims(claims, title="The Agent reports 214 MB.")
        self.assertTrue(any(item.get("quote") == "214" and item["claim_id"] is None for item in result["unresolved"]))

    def test_date_components_cannot_substitute_for_source_date(self):
        claims = [dict(id="F1", quote="2026", kind="UNRESOLVED", source_ids=[], reason="No source."),
                  dict(id="F2", quote="09", kind="UNRESOLVED", source_ids=[], reason="No source."),
                  dict(id="F3", quote="24", kind="UNRESOLVED", source_ids=[], reason="No source.")]
        result = self.run_claims(claims, title="The Agent reports 2026-09-24.")
        self.assertTrue(any(item.get("quote") == "2026-09-24" and item["claim_id"] is None for item in result["unresolved"]))

    def test_malformed_nested_values_are_value_errors(self):
        for section, key, bad in [("calculation", "op", []), ("calculation", "operands", {}),
                                   (None, "kind", []), (None, "source_ids", [None])]:
            claim = self.number()
            target = claim[section] if section else claim
            target[key] = bad
            with self.subTest(section=section, key=key):
                self.rejects(claim)
        semantic = dict(id="F1", quote="the measurement", kind="SEMANTIC", source_ids=["S1"], reason="Source record.", status=[])
        self.rejects(semantic)
        self.rejects(self.selected("2026-09-24", "/date", kind="DATE", comparison=[]))

    def test_malformed_objects_are_value_errors(self):
        for malformed in [None, [], {"complete": True}, {"complete": 1, "reason": "x", "claims": []}]:
            with self.subTest(value=malformed), self.assertRaises(ValueError):
                validate_facts(malformed, {"title": "The Agent reports."}, EvidenceReader(self.root), self.known)


if __name__ == "__main__":
    unittest.main()

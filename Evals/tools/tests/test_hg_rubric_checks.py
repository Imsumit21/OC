"""Historical false-pass regressions and valid controls; not a model benchmark."""
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
from hg_review_score import calculate, validate_score
from hg_rubric_checks import title_facts, validate_checks
from hg_rubric_loop import digest, review_context, FINAL
from rubric_checks_fixture import checks_fixture, facts_fixture, idle_case
from test_hg_review_enforcement import tally
from test_hg_rubric_loop import candidate, score_record

HISTORICAL = json.loads((Path(__file__).parent / "fixtures/rubric_396e.json").read_text())
C18 = HISTORICAL["rubric"][17]["title"]


def PHRASING(row):
    return dict(type="non_agent_centric", rows=[row], impact="precision_only", provenance="rubric_original",
                reason="The title's subject is an artifact, not The Agent.",
                omission_test="Acceptance is unchanged; only the required Agent phrasing is missing.")


class RubricChecksTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.addCleanup(patch.stopall)
        patch.object(writer, "REPOSITORY", self.root).start()
        patch.object(inputs, "REPOSITORY", self.root).start()
        inputs.save_input("universe", content=b"2026-02-14\n")  # task date (hg_universe.py)
        self.prompt = "Report the current download size."
        inputs.save_input("prompt", content=self.prompt.encode())
        self.rubric = json.loads(candidate())
        self.checks = checks_fixture(self.rubric)

    def check(self, issues=None):
        return validate_checks(self.checks, self.rubric, issues or [], root=self.root,
                               context=review_context(self.root)["manifest"])

    def title(self, text):
        self.rubric[0]["title"] = text
        self.checks = checks_fixture(self.rubric, self.prompt)

    def missing(self):
        req = self.checks["requirements"][0]
        req["coverage"] = "MENTION_ONLY"
        req["omission_test"].update(result="ACCEPT", caught_by=[], example="Mention exposure without any commercial substance.")
        return dict(type="missing_coverage", rows=[], outcome_id=req["id"], criticality="critical",
                    impact="accepts_wrong", witness=req["omission_test"]["example"],
                    reason="Explicit substantive deliverable is ungraded.", provenance="rubric_original")

    def bundled_plan(self):
        self.prompt = HISTORICAL["prompt"]
        inputs.save_input("prompt", content=self.prompt.encode())
        self.title(C18.replace("The write-up explicitly addresses", "The Agent explicitly addresses"))
        base = self.checks["requirements"][0]
        reqs, assertions = [], []
        for i, name in enumerate(("beats", "channels", "positioning", "exposure"), 1):
            req = copy.deepcopy(base)
            req.update(id=f"O{i}", entity="Zombie Match 3D", property=name,
                       accepted_result="Substantive, source-supported " + name, reason="Explicit plan dimension.")
            reqs.append(req)
            assertion = copy.deepcopy(self.checks["rows"][0]["assertion_inventory"]["assertions"][0])
            assertion.update(id=f"A{i}", quote=name, outcome_id=f"O{i}", entities=["Zombie Match 3D"], property=name)
            assertions.append(assertion)
        self.checks["requirements"] = reqs
        self.checks["instruction_reviews"][0]["clauses"][0]["outcome_ids"] = [r["id"] for r in reqs]
        row = self.checks["rows"][0]
        row["assertion_inventory"]["assertions"] = assertions
        row["atomicity"].update(outcome_ids=[r["id"] for r in reqs])
        row["atomicity"]["independence_test"].update(classification="INDEPENDENT_RESULTS",
            example="Accurate beats, channels and positioning, with exposure entirely omitted.",
            satisfied_outcome_ids=["O1", "O2", "O3"], failed_outcome_ids=["O4"],
            reason="The plan dimensions can be satisfied independently.")
        return dict(type="non_atomic", rows=[1], impact="accepts_wrong", provenance="rubric_original",
                    witness="A plan names all four dimensions but supplies no exposure analysis; the presence-only interpretation accepts it.",
                    reason="Four independently graded plan dimensions share one result.")

    def test_actual_18_row_false_agent_score_is_rejected(self):
        rubric = HISTORICAL["rubric"]
        self.assertEqual(len(rubric), 18)
        record = tally(18, [PHRASING(18)], 2, rubric=rubric)
        record["dimensions"]["agent_centric"]["score"] = 4
        with self.assertRaisesRegex(ValueError, "non-Agent subject requires FAIL"):
            calculate(record, rubric)
        record["dimensions"]["agent_centric"]["score"] = 2
        result = calculate(record, rubric)
        self.assertEqual(result["verdict"], "FAIL")
        self.assertIn(18, result["repairs"])
        self.assertEqual(result["severity_counts"]["Major"], 1)

    def test_non_agent_row_is_a_major_tally_issue_that_cannot_be_omitted(self):
        rubric = HISTORICAL["rubric"]
        record = tally(18, [], 5, rubric=rubric)
        record["dimensions"]["agent_centric"]["score"] = 2
        with self.assertRaisesRegex(ValueError, "needs a non_agent_centric issue on rows 18"):
            calculate(record, rubric)
        record = tally(18, [PHRASING(18), dict(PHRASING(1), type="incorrect", impact="rejects_correct",
                                               witness="A correct answer this row fails.")], 5, rubric=rubric)
        record["dimensions"]["agent_centric"]["score"] = 2
        record["hard_gates"]["accuracy_acceptance"]["result"] = "FAIL"
        record["dimensions"]["overall_quality"]["score"] = 2
        self.assertEqual(calculate(record, rubric)["overall_quality_band"], "FAIL")

    def test_obvious_artifact_subjects_cannot_be_relabelled_agent(self):
        for text in (C18, "The reply states 214 MB.", "The final report contains 214 MB.", "The new issue identifies 214 MB."):
            with self.subTest(title=text):
                self.title(text)
                self.checks["rows"][0]["wording"]["subject"] = "AGENT_ACTION"
                with self.assertRaisesRegex(ValueError, "subject contradicts"):
                    self.check()

    def test_agent_possessive_and_bare_action_are_non_fail_not_artifact_fail(self):
        for title in ("The Agent's reply states 214 MB.", "The Agent’s report states 214 MB.", "Reports 214 MB."):
            self.title(title)
            checked = self.check()
            score = tally(1, [], 5)
            score["dimensions"]["agent_centric"]["score"] = 2
            self.assertEqual(calculate(score, self.rubric, checked)["verdict"], "FAIL")
            self.assertEqual(checked["wording_fail_rows"], [])

    def test_exact_catalog_tool_name_fails_but_service_name_does_not(self):
        p = self.root / "Evals/references/tools/catalog.json"
        p.parent.mkdir(parents=True)
        p.write_text('[{"name":"gmail_send_email"}]')
        self.title("The Agent uses gmail_send_email to report 214 MB.")
        checked = self.check()
        self.assertEqual(checked["wording_fail_rows"], [1])
        with self.assertRaisesRegex(ValueError, "non-Agent subject requires FAIL"):
            calculate(tally(1, [], 5), self.rubric, checked)
        self.title("The Agent reports 214 MB in Gmail.")
        self.assertEqual(self.check()["wording_fail_rows"], [])

    def test_independent_c18_components_cannot_clear_without_an_issue(self):
        self.bundled_plan()
        with self.assertRaisesRegex(ValueError, "record the demonstrated non_atomic"):
            self.check()

    def test_independent_c18_issue_cannot_keep_atomicity_gate_pass(self):
        issue = self.bundled_plan()
        checked = self.check([issue])
        record = tally(1, [issue], 2)
        record["coverage"] = dict(required_outcomes=4, covered_outcomes=4)
        record["hard_gates"]["atomicity"]["result"] = "PASS"
        with self.assertRaisesRegex(ValueError, "atomicity contradicts"):
            calculate(record, self.rubric, checked)

    def test_one_result_label_cannot_erase_a_partial_success_witness(self):
        self.bundled_plan()
        self.checks["rows"][0]["atomicity"]["independence_test"]["classification"] = "ONE_RESULT"
        with self.assertRaisesRegex(ValueError, "non_atomic"):
            self.check()

    def test_precision_only_bundle_needs_independent_catching_controls(self):
        issue = self.bundled_plan()
        issue.update(impact="precision_only", omission_test="Claim that other rows catch every component.")
        with self.assertRaisesRegex(ValueError, "set-wide catching controls"):
            self.check([issue])

    def test_redundant_non_atomic_bundle_keeps_major_severity_and_blocks_publication(self):
        issue = self.bundled_plan()
        issue.update(impact="precision_only", omission_test="Each component is graded by a separate existing row.")
        bundle = self.checks["rows"][0]
        bundle["precision_controls"] = []
        for i, req in enumerate(self.checks["requirements"], 2):
            title = "The Agent reports the correct " + req["property"] + " for Zombie Match 3D."
            self.rubric.append(json.loads(candidate(title))[0])
            req["rows"].append(i)
            row = copy.deepcopy(bundle)
            row.update(row=i, title=title, fact_review=facts_fixture(title), do_nothing_case=idle_case(title))
            row["atomicity"]["outcome_ids"] = [req["id"]]
            row["atomicity"]["independence_test"].update(classification="ONE_RESULT", satisfied_outcome_ids=[], failed_outcome_ids=[])
            row["assertion_inventory"]["assertions"] = [copy.deepcopy(bundle["assertion_inventory"]["assertions"][i-2])]
            self.checks["rows"].append(row)
            bundle["precision_controls"].append(dict(assertion_id=f"A{i-1}", row=i, quote=title,
                reason="This existing criterion rejects a wrong or omitted component."))
        checked = self.check([issue])
        record = tally(5, [issue], 2)
        record["coverage"] = dict(required_outcomes=4, covered_outcomes=4)
        scored = calculate(record, self.rubric, checked)
        self.assertEqual(scored["severity_counts"]["Major"], 1)
        self.assertEqual(scored["verdict"], "FAIL")
        self.assertFalse(scored["repair_free"])

    def test_valid_separate_plan_dimensions_clear(self):
        self.bundled_plan()
        template = copy.deepcopy(self.checks["rows"][0])
        self.rubric, self.checks["rows"] = [], []
        for i, req in enumerate(self.checks["requirements"], 1):
            title = "The Agent reports source-supported " + req["property"] + " for Zombie Match 3D."
            self.rubric.append(json.loads(candidate(title))[0])
            row = copy.deepcopy(template)
            row.update(row=i, title=title, fact_review=facts_fixture(title), do_nothing_case=idle_case(title))
            req["rows"] = [i]
            for name in ("omission_test", "wrong_result_test"):
                req[name]["caught_by"] = [dict(row=i, quote=title)]
            row["atomicity"]["outcome_ids"] = [req["id"]]
            row["atomicity"]["independence_test"].update(classification="ONE_RESULT", satisfied_outcome_ids=[], failed_outcome_ids=[])
            assertion = row["assertion_inventory"]["assertions"][i-1]
            row["assertion_inventory"]["assertions"] = [assertion]
            self.checks["rows"].append(row)
        self.assertEqual(self.check()["unresolved"], [])
        self.assertEqual(calculate(tally(4, [], 5), self.rubric, self.check())["verdict"], "PASS")

    def test_exposure_omission_cannot_claim_full_coverage(self):
        issue = self.missing()
        self.checks["requirements"][0]["coverage"] = "SUBSTANTIVE"
        with self.assertRaisesRegex(ValueError, "missing substantive coverage"):
            self.check([issue])

    def test_exposure_omission_cannot_be_suppressed_or_demoted_to_depth(self):
        issue = self.missing()
        with self.assertRaisesRegex(ValueError, "exactly match"):
            self.check()
        self.checks["requirements"][0]["criticality"] = "non_critical"
        issue["criticality"] = "non_critical"
        with self.assertRaisesRegex(ValueError, "depth weakness"):
            self.check([issue])

    def test_missing_outcome_uses_authored_denominator_once(self):
        issue = self.missing()
        checked = self.check([issue])
        score = tally(1, [issue], 2)
        score["coverage"] = dict(required_outcomes=1, covered_outcomes=0)
        result = calculate(score, self.rubric, checked)
        self.assertEqual((result["denominator"], result["fractions"]["major"], result["verdict"]), (1, [1, 1], "FAIL"))
        with self.assertRaisesRegex(ValueError, "duplicate missing outcome"):
            calculate(tally(1, [issue, issue], 2), self.rubric)

    def test_prompt_clause_cannot_be_silently_dropped(self):
        self.bundled_plan()
        clause = self.checks["instruction_reviews"][0]["clauses"][0]
        clause["end"] -= 20
        clause["quote"] = clause["quote"][:-20]
        with self.assertRaisesRegex(ValueError, "omitted prompt text"):
            self.check()

    def test_unrequested_golden_metrics_do_not_become_outcomes(self):
        (self.root / "extra_golden_facts.txt").write_text("3993 installs; $10 revenue; zero IAP; no Season Pass sales.")
        result = self.check()
        self.assertEqual((result["required_outcomes"], result["covered_outcomes"]), (1, 1))
        self.assertEqual(calculate(tally(1, [], 5), self.rubric, result)["verdict"], "PASS")

    def test_descriptive_negation_is_affirmative(self):
        self.title("The Agent reports that PR #438 had no human-submitted review.")
        self.checks["rows"][0]["negative"]["classification"] = "DESCRIPTIVE_NEGATION"
        self.assertEqual(self.check()["negative_fail_rows"], [])

    def test_prohibition_fails_even_with_explicit_prompt_prohibition(self):
        self.title("The Agent does not email partners.")
        row = self.checks["rows"][0]
        with self.assertRaisesRegex(ValueError, "negative graded action"):
            self.check()
        row["negative"].update(classification="PROHIBITION", explicit_prompt_prohibition=False)
        result = self.check()
        with self.assertRaisesRegex(ValueError, "prohibition-only acceptance requires Negative FAIL"):
            calculate(tally(1, [], 5), self.rubric, result)
        self.prompt = "Do not email partners."
        inputs.save_input("prompt", content=self.prompt.encode())
        self.title("The Agent does not email partners.")
        self.checks["rows"][0]["negative"].update(classification="PROHIBITION", explicit_prompt_prohibition=True,
                                               authority_chain=["P1"], quote=self.prompt)
        self.assertEqual(self.check()["negative_fail_rows"], [1])

    def test_additional_negative_openings_are_prohibitions(self):
        for title in ("The Agent makes no changes to ENG-123.", "The Agent doesn't email partners.",
                      "The Agent declines to close ENG-123."):
            with self.subTest(title=title):
                self.assertTrue(title_facts(title)["negative_action"])
        self.assertFalse(title_facts("The Agent reports that PR #438 had no human-submitted review.")["negative_action"])
        self.assertFalse(title_facts("The Agent leaves ENG-123 open.")["negative_action"])

    def test_title_and_supporting_field_conflict_needs_recorded_issue(self):
        self.checks["rows"][0]["supporting_fields"].update(status="ISSUE", witness="Title requires 214; evidence prescribes 221.")
        with self.assertRaisesRegex(ValueError, "conflict must be recorded"):
            self.check()

    def test_wrong_row_or_justification_cannot_supply_the_catching_predicate(self):
        self.checks["requirements"][0]["omission_test"]["caught_by"][0]["quote"] = self.rubric[0]["justification"]
        with self.assertRaisesRegex(ValueError, "exact title"):
            self.check()

    def test_missing_checks_block_audit_score(self):
        inputs.save_input("rubric", content=json.dumps(self.rubric).encode())
        record = score_record(self.root, mode="AUDIT")
        del record["checks"]
        with self.assertRaisesRegex(ValueError, "checks must be an object"):
            writer.save_output("rubric-score", json.dumps(record))
        self.assertFalse((self.root / FINAL).exists())

    def test_saved_audit_rejects_lying_dimension_but_accepts_accurate_fail(self):
        self.title(C18)
        inputs.save_input("rubric", content=json.dumps(self.rubric).encode())
        record = score_record(self.root, mode="AUDIT")
        with self.assertRaisesRegex(ValueError, "non-Agent subject requires FAIL"):
            writer.save_output("rubric-score", json.dumps(record))
        record["dimensions"]["agent_centric"]["score"] = 2
        with self.assertRaisesRegex(ValueError, "needs a non_agent_centric issue"):
            writer.save_output("rubric-score", json.dumps(record))
        record["issues"].append(PHRASING(1))
        record["dimensions"]["overall_quality"]["score"] = 2
        self.assertEqual(writer.save_output("rubric-score", json.dumps(record))["verdict"], "FAIL")

    def test_unknown_coverage_is_partial_not_fabricated_failure(self):
        req = self.checks["requirements"][0]
        req.update(coverage="UNRESOLVED")
        req["omission_test"].update(result="UNRESOLVED", caught_by=[])
        inputs.save_input("rubric", content=json.dumps(self.rubric).encode())
        record = score_record(self.root, mode="AUDIT")
        record.update(checks=self.checks, coverage=dict(required_outcomes=1, covered_outcomes=0, unresolved_outcomes=1))
        result = validate_score(self.root, json.dumps(record))
        self.assertEqual((result["execution_status"], result["verdict"], result["verdict_score"]), ("PARTIAL", "NON-FAIL", None))

    def test_inaccessible_instruction_does_not_create_a_missing_outcome_fail(self):
        self.checks["sources"][0]["visibility"] = "UNRESOLVED"
        req = self.checks["requirements"][0]
        req["coverage"] = "UNRESOLVED"
        req["omission_test"].update(result="ACCEPT", caught_by=[])
        result = self.check()
        self.assertEqual(result["covered_outcomes"], 0)
        self.assertTrue(result["unresolved"])

    def test_old_score_format_cannot_authorize_a_new_audit(self):
        inputs.save_input("rubric", content=json.dumps(self.rubric).encode())
        record = score_record(self.root, mode="AUDIT")
        record["format_version"] = 2
        with self.assertRaisesRegex(ValueError, "format_version"):
            writer.save_output("rubric-score", json.dumps(record))

    def test_changed_check_title_cannot_follow_an_old_score(self):
        inputs.save_input("rubric", content=json.dumps(self.rubric).encode())
        record = score_record(self.root, mode="AUDIT")
        record["checks"]["rows"][0]["title"] = "The Agent reports 221 MB."
        with self.assertRaisesRegex(ValueError, "title differs"):
            writer.save_output("rubric-score", json.dumps(record))

    def test_unknown_actor_cannot_be_certified_without_agent_text(self):
        self.title("A beautifully formatted executive briefing contains 214 MB.")
        self.checks["rows"][0]["wording"]["subject"] = "AGENT_ACTION"
        with self.assertRaisesRegex(ValueError, "actor quote"):
            self.check()

    def test_coherent_pr_identity_and_date_remain_valid(self):
        self.prompt = "Report the first merged PR and its merge date."
        inputs.save_input("prompt", content=self.prompt.encode())
        self.title("The Agent reports PR #10 and merge date 2026-02-10.")
        source = dict(number=10, merged_at="2026-02-10")
        raw = json.dumps([source]).encode()
        (self.root / "pr.json").write_bytes(raw)
        self.checks["sources"].append(dict(id="S1", path="pr.json", sha256=digest(raw), pointer="/0",
            quote="2026-02-10", visibility="VISIBLE", access="Shared repository record", reachability="PROMPT_LINKED"))
        row = self.checks["rows"][0]
        row["atomicity"]["exception"] = dict(kind="coherent_record", record_kind="pull_request", source_id="S1",
            entity="repo#10", fields=["number", "merged_at"], reason="Attributes of one verified selected record.")
        row["assertion_inventory"]["assertions"] = [dict(id=f"A{i}", field="title", quote=quote,
            role="REQUIRED_RESULT", outcome_id="Q1-O1", kind="ENTITY_PROPERTY", entities=["repo#10"],
            property=prop, source_id="S1", reason="One PR record attribute.")
            for i, prop, quote in ((1, "number", "PR #10"), (2, "merged_at", "2026-02-10"))]
        self.assertEqual(self.check()["unresolved"], [])


if __name__ == "__main__":
    unittest.main()

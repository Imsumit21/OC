"""Atomicity record invariants. These tests do not judge natural-language truth."""

import copy
import json
from pathlib import Path
import sys
import unittest
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hg_rubric_review import validate_record
from hg_rubric_loop import POLICY, digest
from test_hg_rubric_loop import candidate, review_record, assertion_inventory


class AtomicityRecordTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        prompt = self.root / "Evals/task_inputs/04_Prompt.txt"
        prompt.parent.mkdir(parents=True)
        prompt.write_text("Report the current download size.")
        self.receipt = dict(review_policy=POLICY, review_iteration=1,
                            reviewed_json_sha256="a" * 64, review_context_sha256="b" * 64)
        self.proposal = json.loads(candidate())
        self.record = review_record(self.receipt, candidate())

    def validate(self, publication=True):
        return validate_record(self.record, self.proposal, self.receipt, publication=publication, root=self.root)

    def ticket_facts(self, title, outcomes):
        return dict(complete=True,reason='Fixed synthetic ticket identities for atomicity controls.',claims=[
            dict(id='ID'+str(i),quote=o['entity'],kind='LITERAL',source_ids=['TICKETS'],
                reason='The ticket identity is in the fixed cohort.',
                selection=dict(source_id='TICKETS',pointer='/'+str(i)))
            for i,o in enumerate(outcomes) if o['entity'] in title])

    def bundle(self, count=2, same_status=False):
        outcomes = [dict(id=f"O{i}", entity=f"ENG-{2410+i}", property="reported status",
                         output="#engineering summary", accepted_result="Done" if same_status or i % 2 == 0 else "In Progress")
                    for i in range(count)]
        self.record["requirements"][0]["outcomes"] = outcomes
        self.proposal[0]["title"] = "The Agent reports " + ", ".join(
            x["entity"] + " " + x["accepted_result"] for x in outcomes) + "."
        self.record["rows"][0]["predicate"] = self.proposal[0]["title"]
        ids = [x["id"] for x in outcomes]
        self.record["rows"][0]["atomicity"].update(
            outcome_ids=ids, split_plan=[[oid] for oid in ids],
            independence_test=dict(classification="INDEPENDENT_RESULTS",
                example="The first ticket has its correct status; every other ticket has the opposite status.",
                satisfied_outcome_ids=ids[:1], failed_outcome_ids=ids[1:],
                reason="Every ticket's independently required status can be correct or wrong separately."))
        self.record["rows"][0]["assertion_inventory"] = assertion_inventory(self.proposal[0]["title"], outcomes)
        raw=json.dumps([o['entity'] for o in outcomes]).encode()
        (self.root/'tickets.json').write_bytes(raw)
        self.record['sources']=[s for s in self.record['sources'] if s['id']!='TICKETS']+[
            dict(id='TICKETS',path='tickets.json',sha256=digest(raw),quote=raw.decode(),
                visibility='VISIBLE',access='Fixed synthetic cohort.')]
        self.record['rows'][0]['fact_review']=self.ticket_facts(self.proposal[0]['title'],outcomes)
        return self.record["rows"][0]["atomicity"]

    def test_single_measurement_remains_publishable(self):
        self.assertEqual(self.validate()["review_outcomes"], 1)

    def test_32_ticket_partition_and_same_status_bundles_are_blocked(self):
        for same_status in (True, False):
            self.bundle(32, same_status)
            saved = self.validate(publication=False)
            self.assertEqual(saved["review_outcomes"], 32)
            with self.subTest(same_status=same_status), self.assertRaisesRegex(ValueError, "need splitting"):
                self.validate()

    def test_pass_labels_and_exception_cannot_override_independence(self):
        atomicity = self.bundle()
        atomicity["exception"] = dict(kind="identity_only_set", reason="Claims this is one partition.")
        with self.assertRaisesRegex(ValueError, "need splitting"):
            self.validate()

    def test_multiple_declared_outcomes_cannot_be_labelled_one_result(self):
        atomicity = self.bundle()
        atomicity["independence_test"]["classification"] = "ONE_RESULT"
        atomicity["split_plan"] = []
        with self.assertRaisesRegex(ValueError, "multiple declared outcomes"):
            self.validate()

    def test_unresolved_independence_blocks_publication(self):
        self.record["rows"][0]["atomicity"]["independence_test"]["classification"] = "UNRESOLVED"
        self.assertTrue(self.validate(False)["review_open_items"])
        with self.assertRaisesRegex(ValueError, "unresolved independence"):
            self.validate()

    def test_generic_pass_reason_is_no_longer_enough(self):
        self.record["rows"][0]["atomicity"] = dict(status="PASS", reason="One classification.")
        with self.assertRaises(ValueError):
            self.validate()

    def test_missing_inventory_or_evidence_is_rejected(self):
        original = copy.deepcopy(self.record)
        for field in ("outcome_ids", "independence_test", "exception", "split_plan"):
            self.record = copy.deepcopy(original)
            del self.record["rows"][0]["atomicity"][field]
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.validate()
        self.record = copy.deepcopy(original)
        del self.record["requirements"][0]["outcomes"]
        with self.assertRaises(ValueError):
            self.validate()

    def test_invented_exception_is_rejected(self):
        for kind in ("same_status", "one_partition", "same_source", "same_write"):
            self.record["rows"][0]["atomicity"]["exception"] = dict(kind=kind, reason="Same source.")
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, "unknown atomic exception"):
                self.validate()

    def test_unknown_duplicate_and_cross_requirement_outcomes_are_rejected(self):
        original = copy.deepcopy(self.record)
        for ids in (["UNKNOWN"], [True], ["Q1-O1", "Q1-O1"]):
            self.record = copy.deepcopy(original)
            self.record["rows"][0]["atomicity"]["outcome_ids"] = ids
            with self.subTest(ids=ids), self.assertRaises(ValueError):
                self.validate()
        self.record = copy.deepcopy(original)
        self.record["requirements"][0]["outcomes"] *= 2
        with self.assertRaisesRegex(ValueError, "duplicate outcome"):
            self.validate()

    def test_uncovered_outcome_cannot_disappear(self):
        self.record["requirements"][0]["outcomes"].append(dict(
            id="Q1-O2", entity="Other build", property="download size", output="Reply", accepted_result="99 MB"))
        with self.assertRaisesRegex(ValueError, "every declared outcome"):
            self.validate()

    def test_witness_must_cover_distinct_pass_and_fail_outcomes(self):
        for passed, failed in [([], ["O0", "O1"]), (["O0"], []),
                              (["O0"], ["O0"]), (["O0"], ["UNKNOWN"])]:
            atomicity = self.bundle()
            atomicity["independence_test"].update(satisfied_outcome_ids=passed, failed_outcome_ids=failed)
            with self.subTest(passed=passed, failed=failed), self.assertRaises(ValueError):
                self.validate(False)

    def test_split_plan_cannot_rebundle_or_omit_independent_outcomes(self):
        for plan in ([], [["O0", "O1"]], [["O0"]], [["O0"], ["O0"]]):
            atomicity = self.bundle()
            atomicity["split_plan"] = plan
            with self.subTest(plan=plan), self.assertRaisesRegex(ValueError, "split_plan"):
                self.validate(False)

    def test_legitimate_single_result_exceptions_remain_available(self):
        cases = [
            ("identity_only_set", "declared identifiers", "exact membership", "alpha and beta"),
            ("aggregate_invariant", "register", "total row count", "32"),
            ("destination_identity", "requested reply", "destination", "channel C1, thread T1"),
            ("atomic_cell", "requested coordinate", "location", "51N, 0W"),
        ]
        for kind, entity, prop, result in cases:
            unit = self.record["requirements"][0]["outcomes"][0]
            unit.update(entity=entity, property=prop, accepted_result=result)
            self.record["rows"][0]["atomicity"]["exception"] = dict(
                kind=kind, reason="The stated request asks for this single set, invariant or identity.")
            with self.subTest(kind=kind):
                self.assertFalse(self.validate()["review_open_items"])

    def test_large_audit_exception_requires_actual_sampling_links(self):
        self.record["rows"][0]["atomicity"]["exception"] = dict(
            kind="large_audit", reason="One reconciliation control in a qualified audit.")
        with self.assertRaisesRegex(ValueError, "mapped sampled"):
            self.validate()
        req = self.record["requirements"][0]
        req["coverage_mode"] = "sampled"
        req["sampling"] = dict(eligibility="Qualifying repetitive audit fixture.", controls=[1],
                               spot_checks=[1], limitations="Unsampled cell swaps are not guaranteed detected.")
        self.assertFalse(self.validate()["review_open_items"])

    def test_revised_individual_status_rows_can_publish(self):
        self.bundle()
        row = self.record["rows"][0]
        self.record["rows"] = [copy.deepcopy(row), copy.deepcopy(row)]
        self.proposal = [copy.deepcopy(self.proposal[0]), copy.deepcopy(self.proposal[0])]
        self.record["requirements"][0]["rows"] = [1, 2]
        for i, item in enumerate(self.record["rows"]):
            item["row"] = i + 1
            item["atomicity"].update(outcome_ids=[f"O{i}"], split_plan=[], exception=None)
            item["atomicity"]["independence_test"].update(
                classification="ONE_RESULT", example=f"Only ticket {i}'s status is graded here.",
                satisfied_outcome_ids=[], failed_outcome_ids=[], reason="One ticket's reported status.")
            self.proposal[i]["title"] = f"The Agent reports ENG-{2410+i} as " + ("Done." if i == 0 else "In Progress.")
            item["predicate"] = self.proposal[i]["title"]
            unit = self.record["requirements"][0]["outcomes"][i]
            item["assertion_inventory"] = assertion_inventory(self.proposal[i]["title"], [unit])
            item['fact_review']=self.ticket_facts(self.proposal[i]['title'],self.record['requirements'][0]['outcomes'])
        self.assertFalse(self.validate()["review_open_items"])


if __name__ == "__main__":
    unittest.main()

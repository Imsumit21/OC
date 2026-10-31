"""2026-10-17 rubric-eval fixes, calibrated on real rows from the Kelvin 50 and the …eccb QC fail.

Mechanical checks only: the do-nothing and valid-answer tests, count formats, LITERAL keys,
PT-or-UTC days, reachable evidence, anonymized tokens, Overly Broad severity and the OE
cross-check. Row text is copied verbatim from the submitted rubrics (task IDs in comments).
"""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_store_input as inputs
import hg_write_output as writer
from hg_review_evidence import EvidenceReader
from hg_review_score import calculate, check_oe_binding
from hg_rubric_checks import title_facts, validate_checks
from hg_rubric_fact_binding import checked_facts
from hg_rubric_facts import validate_facts
from hg_rubric_lint import lint
from hg_rubric_loop import INPUT_KEYS, review_context
from rubric_checks_fixture import checks_fixture, idle_case
from test_hg_review_enforcement import tally

# Task 6ac674e16329279865bbeccb (Robert close-out pay; QC Criteria Framing fail, 2026-10-17).
ECCB_PROMPT = ("Robert handed the close-out pay over to me, it's his message in winddown after the sign-off call. "
               "can you take the whole thing off my plate? work out what everyone is actually owed for their "
               "close-out hours and then do what he asked with it, the sheet, letting each person know their "
               "number, getting the list to arthur and closing out the payout ticket.")
C26 = ("The Agent leaves Arthur's Close-out chores spreadsheet (f_c81eed8850e8cd4fd16799) as found, with its one "
       "Chores tab of 210 chore rows under Ticket, Chore and Owner")
C52 = "The Agent leaves every payee's own hours and amount off ENG-2558 (Pay out logged close-out hours)"
C47 = ("The Agent records the close-out total of $1,570.00 on ENG-2558 (Pay out logged close-out hours), "
       "in a comment or in the ticket's description")
C32 = ("The Agent keeps the pay figures in its close-out pay email to oliver.brooks@harmonygames.co to Oliver "
       "Brooks's own, leaving every other payee's hours and amount out of it")
# Task 6abc8c9f7032c280016df2ec (#16), submitted R2 and the prompt's only length instruction.
R2_16 = ("The Agent keeps its reply to Leonard short: besides lines that give labelled spend or install figures, "
         "it has at most five other lines, and every line is one sentence or less.")
RUN1_16 = ("Short synthetic reply modelled on run 1: ten short lines giving the Adjoe, AppLovin and Unity spend and "
           "installs for Domino and Zombie, April to August 2025 (all 32 figures), then a closing source note of "
           "three sentences saying the numbers come from the warehouse, not the recap.")
# Task 6aa8272b1b7a2df0fc0fea90 (#7), criterion-10.
QUEST_7 = ("The Agent reports that the event the specification calls `quest_completion` ships under the same "
           "name, `quest_completion`.")
# Task 6aa8272b1b7a2df0fc0fea7a (#40): Arthur's 'Total download size is 276mb' (ts 1763341093.990849).
INSTANT_40 = "2025-11-17T00:58:13Z"
# Task 6aa8272b1b7a2df0fc0fea69 (#5), criterion-19; the 20 Oct roster shows the masked name.
HOMA_5 = "The Agent's write-up records HOMA as Closed - passed."
# Task 6abc06a64719e24dcc073712 (#4), row 52; the deciding notice sits in Gmail Trash.
TRASH_4 = ("The Agent sets a due date of 2026-02-26 on Linear issue ENG-2443, the Engineering issue for the "
           "Domino Delights crashes.")
# Task 6aad7d1ec6922756b9ad3954 (#45): OE 13-14 vs criterion-18.
OE_45 = ("OE 13  Get the destination folder ID. Read the Drive metadata of the amendment from OE 3, or of another "
         "Wind Down file shared with Leonard (\"Termination Notices.docx\", \"Task List.xlsx\").\n"
         "        Expected: the parent folder is \"Wind Down\", d_e5caf6a8c630421942ee59.\n"
         "OE 14  Create the settlement workbook in that folder. Use Google Drive to create a Google Sheets file "
         "with parentId d_e5caf6a8c630421942ee59 (or create the spreadsheet in Google Sheets and move it into "
         "d_e5caf6a8c630421942ee59).\n"
         "        Expected: a new spreadsheet ID and link, with the Wind Down folder as its parent.\n"
         "OE 21  Reply to Leonard with the settlement offers.\n")
ROW_45 = ("The Agent tells Leonard that it could not save the settlement sheet in the Wind Down folder because his "
          "account does not have access to the folder.")
# Task 6ac674e16329279865bbecca (#13): OE 21's model reply vs R85.
OE_13 = ("OE 21  Reply-all on Leonard's \"Sunset - engineering side\" thread in Gmail so Leonard and Robert see where "
         "each register item lands.\n      Expected: the reply goes to Leonard with Robert addressed and covers each "
         "item. CF dev and staging: close by 2026-02-17, owner Arthur. CF prod and all AWS accounts: close after the "
         "2026-03-09 teardown review, owner Arthur. AWS cost: $1,485 a month.\n")
R85_13 = ("The Agent states in the reply on Leonard's 'Sunset - engineering side' thread that the Domino Delights "
          "dev account can be shut down now or by 2026-02-17.")


def row(title, weight=1):
    return dict(title=title, category="Outcome", weight=weight,
                justification="Copied from the submitted rubric.", evidence="See ENG-2558 (SQL L825).")


def issue(kind, rows, impact="rejects_correct"):
    return dict(type=kind, rows=rows, impact=impact, provenance="rubric_original",
                reason="Demonstrated in the calibration case.", witness="A prompt-allowed answer this row fails.")


class Workspace(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.addCleanup(patch.stopall)
        patch.object(inputs, "REPOSITORY", self.root).start()
        inputs.save_input("universe", content=b"2026-02-14\n")  # task date (hg_universe.py)
        patch.object(writer, "REPOSITORY", self.root).start()

    def use(self, titles, prompt="Report the current download size."):
        self.prompt = prompt
        inputs.save_input("prompt", content=prompt.encode())
        self.rubric = [row(t) for t in titles]
        self.checks = checks_fixture(self.rubric, prompt)

    def check(self, issues=()):
        return validate_checks(self.checks, self.rubric, list(issues), root=self.root,
                               context=review_context(self.root)["manifest"])

    def source(self, sid, payload, reachability="PROMPT_LINKED"):
        raw = json.dumps(payload).encode()
        (self.root / (sid + ".json")).write_bytes(raw)
        anchor = dict(id=sid, path=sid + ".json", sha256=hashlib.sha256(raw).hexdigest(), quote=raw.decode(),
                      visibility="VISIBLE", access="Persona-visible synthetic copy of the task record.",
                      reachability=reachability)
        self.checks["sources"].append(anchor)
        return anchor


class DoNothingTests(Workspace):
    """Card h: rows an Agent passes by doing nothing fail Negative Criteria however they are worded."""

    def setUp(self):
        super().setUp()
        self.use([C26, C52, C47, C32], ECCB_PROMPT)

    def test_lint_flags_disguised_negatives_only(self):
        hits = {(h["row"], h["check"]) for h in lint(self.rubric)}
        self.assertIn((1, "disguised_negative"), hits)
        self.assertIn((2, "disguised_negative"), hits)
        self.assertNotIn((3, "disguised_negative"), hits)
        self.assertNotIn((4, "disguised_negative"), hits)
        self.assertTrue(title_facts("The Agent leaves ENG-123 open.")["disguised_negative"])
        self.assertTrue(title_facts("The Agent keeps the totals off the ticket.")["disguised_negative"])
        self.assertFalse(title_facts("The Agent leaves ENG-123 open.")["negative_action"])

    def test_c26_and_c52_fail_negative_criteria_c47_and_c32_pass(self):
        for number in (1, 2):
            self.assertEqual(self.checks["rows"][number-1]["do_nothing_case"]["result"], "ACCEPT")
        with self.assertRaisesRegex(ValueError, "negative in disguise"):
            self.check()
        for number in (1, 2):
            self.checks["rows"][number-1]["negative"]["classification"] = "PROHIBITION"
        self.checks["rows"][2]["do_nothing_case"] = dict(
            result="REJECT", quote="records the close-out total of $1,570.00 on ENG-2558",
            reason="An idle Agent never writes the total on the ticket.")
        self.checks["rows"][3]["do_nothing_case"] = dict(
            result="REJECT", quote="in its close-out pay email to oliver.brooks@harmonygames.co",
            reason="The row is a condition on the pay email the Agent must send; with no email it fails.")
        result = self.check()
        self.assertEqual(result["negative_fail_rows"], [1, 2])
        with self.assertRaisesRegex(ValueError, "prohibition-only acceptance requires Negative FAIL"):
            calculate(tally(4, [], 5, rubric=self.rubric), self.rubric, result)
        record = tally(4, [], 5, rubric=self.rubric)
        record["dimensions"]["negative"]["score"] = 2
        self.assertEqual(calculate(record, self.rubric, result)["verdict"], "FAIL")

    def test_preserved_state_cannot_be_quoted_as_the_required_write(self):
        self.checks["rows"][0]["do_nothing_case"] = dict(
            result="REJECT", quote="leaves Arthur's Close-out chores spreadsheet (f_c81eed8850e8cd4fd16799) as found",
            reason="Claims the preserved state is a write.")
        with self.assertRaisesRegex(ValueError, "do_nothing_case.quote"):
            self.check()
        self.checks["rows"][0]["do_nothing_case"]["quote"] = "a phrase that is not in the title"
        with self.assertRaisesRegex(ValueError, "do_nothing_case.quote"):
            self.check()

    def test_do_nothing_case_is_required(self):
        for number in (1, 2):
            self.checks["rows"][number-1]["negative"]["classification"] = "PROHIBITION"
        del self.checks["rows"][2]["do_nothing_case"]
        with self.assertRaisesRegex(ValueError, "do_nothing_case"):
            self.check()


class ValidCaseTests(Workspace):
    """Point 2: each row accepts a prompt-allowed answer; a rejection forces overly_specific."""

    def setUp(self):
        super().setUp()
        self.use([R2_16], "can you get me what we actually spent on paid ua ... and reply to him in the thread "
                          "with them. keep it short")

    def test_r2_rejects_run_one_and_is_flagged_overly_specific(self):
        self.checks["rows"][0]["valid_case"] = dict(
            example=RUN1_16, result="REJECT",
            reason="The prompt says only 'keep it short'; the 3-sentence source note breaks R2's one-sentence rule.")
        with self.assertRaisesRegex(ValueError, "valid_case is rejected"):
            self.check()
        found = issue("overly_specific", [1])
        checked = self.check([found])
        scored = calculate(tally(1, [found], 2, rubric=self.rubric), self.rubric, checked)
        self.assertEqual((scored["severity_counts"]["Major"], scored["verdict"]), (1, "FAIL"))

    def test_count_phrases_are_flagged_for_a_second_look(self):
        hits = [h["text"] for h in lint(self.rubric) if h["check"] == "format_lock"]
        self.assertIn("at most five", hits)
        self.assertTrue(any("line" in h for h in hits))
        self.assertEqual(title_facts("The Agent keeps its reply to Leonard brief.")["format_lock"], [])
        self.assertEqual(title_facts("The Agent fills the line tab with 167 line rows.")["format_lock"], [])
        self.assertEqual(title_facts("Agent posts one sentence per line.")["format_lock"], ["one sentence", "per line"])

    def test_valid_case_is_required_and_unresolved_stays_partial(self):
        self.checks["rows"][0]["valid_case"]["result"] = "UNRESOLVED"
        self.assertIn("R1: unresolved valid_case", self.check()["unresolved"])
        del self.checks["rows"][0]["valid_case"]
        with self.assertRaisesRegex(ValueError, "valid_case"):
            self.check()

    def test_concise_final_reply_rejection_needs_the_rows_issue(self):
        self.checks["final_reply_test"].update(result="REJECT", rejecting_rows=[1],
                                               example="The figures in the thread and a one-line source note.")
        with self.assertRaisesRegex(ValueError, "concise final reply is rejected"):
            self.check()
        self.check([issue("overly_specific", [1])])
        self.checks["final_reply_test"]["rejecting_rows"] = []
        with self.assertRaisesRegex(ValueError, "contradicts rejecting_rows"):
            self.check()


class LiteralKeyTests(Workspace):
    """Point 3 / #7: ID-shaped keys bind as LITERAL, like numbers bind as NUMBER."""

    def setUp(self):
        super().setUp()
        self.anchor = None
        raw = json.dumps(dict(event="quest_completed", roster="[PERSON_NAME_0854]")).encode()
        (self.root / "events.json").write_bytes(raw)
        self.anchor = dict(id="E", path="events.json", sha256=hashlib.sha256(raw).hexdigest(), quote=raw.decode(),
                           visibility="VISIBLE", access="Shared repository record.")
        self.known = {"E": self.anchor}

    def facts(self, title, claims, **options):
        return validate_facts(dict(complete=True, reason="Listed claims.", claims=claims), dict(title=title),
                              EvidenceReader(self.root), self.known, **options)

    def literal(self, quote, pointer, start):
        return dict(id="L" + str(start), quote=quote, start=start, kind="LITERAL", source_ids=["E"],
                    reason="Exact event key from the shipped code.", selection=dict(source_id="E", pointer=pointer))

    def test_quest_completion_is_a_mismatch_with_quest_completed(self):
        claims = [self.literal("quest_completion", "/event", QUEST_7.index("quest_completion")),
                  self.literal("quest_completion", "/event", QUEST_7.rindex("quest_completion"))]
        result = self.facts(QUEST_7, claims, literal_tokens=True)
        self.assertEqual([m["actual"] for m in result["mismatches"]], ["quest_completed", "quest_completed"])
        self.assertEqual(result["unresolved"], [])

    def test_semantic_label_cannot_bind_an_event_key(self):
        claim = dict(id="S", quote="quest_completion", start=QUEST_7.index("quest_completion"), kind="SEMANTIC",
                     status="VERIFIED", source_ids=["E"], reason="Reviewer judgment only.")
        result = self.facts(QUEST_7, [claim], literal_tokens=True)
        self.assertEqual(len(result["unresolved"]), 2)
        self.assertIn("LITERAL", result["unresolved"][0]["reason"])
        # Other stages (prompt premises) keep the previous coverage rule.
        self.assertEqual(self.facts(QUEST_7, [claim])["unresolved"], [])
        review = dict(complete=True, reason="Listed claims.", claims=[claim])
        self.assertEqual(checked_facts(review, dict(title=QUEST_7), EvidenceReader(self.root), self.known,
                                       self.root, {})["unresolved"], [])

    def test_homa_against_the_masked_roster_name_is_an_anonymized_mismatch(self):
        claim = self.literal("HOMA", "/roster", HOMA_5.index("HOMA"))
        result = self.facts(HOMA_5, [claim], literal_tokens=True)
        self.assertEqual(result["mismatches"][0]["anonymized_token"], "[PERSON_NAME_0854]")
        title = "The Agent's write-up records [PERSON_NAME_0854] as Closed - passed."
        self.assertTrue(self.facts(title, [], literal_tokens=True)["unresolved"])
        token = self.literal("[PERSON_NAME_0854]", "/roster", title.index("["))
        result = self.facts(title, [token], literal_tokens=True)
        self.assertEqual((result["mismatches"], result["unresolved"]), ([], []))

    def test_lint_flags_anonymized_tokens_and_evidence_without_a_record(self):
        rubric = [dict(row(HOMA_5), evidence="Read the write-up body and confirm an entry naming HOMA."),
                  dict(row(HOMA_5), evidence="The 20 Oct roster lists [PERSON_NAME_0854] as Scheduled.")]
        hits = {(h["row"], h["check"]) for h in lint(rubric)}
        self.assertIn((1, "evidence_no_record"), hits)
        self.assertIn((2, "anon_token"), hits)
        self.assertNotIn((2, "evidence_no_record"), hits)


class AnonymizedRowTests(Workspace):
    def test_row_rejecting_the_token_needs_overly_specific(self):
        self.use([HOMA_5], "Everyone on the target list I posted in executives on 20 October.")
        self.source("ROSTER", dict(slot6="[PERSON_NAME_0854]"))
        self.checks["rows"][0]["fact_review"] = dict(complete=True, reason="Name bound.", claims=[dict(
            id="H", quote="HOMA", kind="LITERAL", source_ids=["ROSTER"], reason="The roster's sixth Scheduled name.",
            selection=dict(source_id="ROSTER", pointer="/slot6"))])
        with self.assertRaisesRegex(ValueError, "anonymized source token"):
            self.check()
        self.check([issue("overly_specific", [1])])


class PacificDateTests(Workspace):
    """Card e / #40: a calendar day matches the UTC day or the America/Los_Angeles day."""

    def date_claim(self, title, quote, comparison="pt_or_utc_date"):
        return dict(id="D" + quote[-8:-6], quote=quote, start=title.index(quote), kind="DATE", source_ids=["TS"],
                    reason="Day of Arthur's post.", comparison=comparison,
                    selection=dict(source_id="TS", pointer="/created"))

    def run_title(self, title, quotes, comparison="pt_or_utc_date", issues=()):
        self.use([title], "what's the last measured download size versus that cap")
        self.source("TS", dict(created=INSTANT_40))
        claims = [self.date_claim(title, q, comparison) for q in quotes]
        claims.append(dict(id="SIZE", quote="276 MB", kind="NOT_A_CLAIM", source_ids=[],
                           reason="Size checked by a separate fixture."))
        self.checks["rows"][0]["fact_review"] = dict(complete=True, reason="Date bound.", claims=claims)
        return self.check(issues)

    def test_nov_16_matches_under_pt_or_utc_date_but_not_utc_date(self):
        title = "The Agent reports 276 MB on November 16, 2025 as the last measured total download size."
        known = {"TS": None}
        self.use([title])
        anchor = self.source("TS", dict(created=INSTANT_40))
        known["TS"] = anchor
        claim = self.date_claim(title, "November 16, 2025")
        size = dict(id="SIZE", quote="276 MB", kind="NOT_A_CLAIM", source_ids=[], reason="Not under test.")
        result = validate_facts(dict(complete=True, reason="r", claims=[claim, size]), dict(title=title),
                                EvidenceReader(self.root), known)
        computed = result["computed"][0]
        self.assertEqual((computed["matched"], computed["pt_day"], computed["utc_day"], computed["split_day"]),
                         (True, "2025-11-16", "2025-11-17", True))
        self.assertEqual(result["mismatches"], [])
        claim["comparison"] = "utc_date"
        self.assertTrue(validate_facts(dict(complete=True, reason="r", claims=[claim, size]), dict(title=title),
                                       EvidenceReader(self.root), known)["mismatches"])

    def test_a_row_accepting_only_nov_17_is_flagged_overly_specific(self):
        title = "The Agent reports 276 MB on November 17, 2025 as the last measured total download size."
        with self.assertRaisesRegex(ValueError, "only one of the PT and UTC calendar days"):
            self.run_title(title, ["November 17, 2025"])
        self.run_title(title, ["November 17, 2025"], issues=[issue("overly_specific", [1])])

    def test_the_same_rule_applies_to_a_pt_only_row(self):
        title = "The Agent reports 276 MB on November 16, 2025 as the last measured total download size."
        with self.assertRaisesRegex(ValueError, "only one of the PT and UTC calendar days"):
            self.run_title(title, ["November 16, 2025"])

    def test_a_row_accepting_both_days_is_clean(self):
        title = ("The Agent reports 276 MB on November 16, 2025 (PT) or November 17, 2025 (UTC) as the last "
                 "measured total download size.")
        self.assertEqual(self.run_title(title, ["November 16, 2025", "November 17, 2025"])["fact_results"][0]
                         ["mismatches"], [])

    def test_a_same_day_instant_needs_no_second_day(self):
        title = "The Agent reports 276 MB on November 12, 2025 as the last measured total download size."
        self.use([title])
        self.source("TS", dict(created="2025-11-12T18:00:00Z"))
        self.checks["rows"][0]["fact_review"] = dict(complete=True, reason="Date bound.", claims=[
            self.date_claim(title, "November 12, 2025"),
            dict(id="SIZE", quote="276 MB", kind="NOT_A_CLAIM", source_ids=[], reason="Not under test.")])
        self.check()


class ReachabilityTests(Workspace):
    """#4: the deciding record cannot sit only in Trash, only in an attachment or where nothing points."""

    def setUp(self):
        super().setUp()
        self.use([TRASH_4], "get it into linear for engineering due whenever googles latest domino notice says")

    def bind(self, reachability):
        self.source("NOTICE", dict(labelIds=["TRASH", "CATEGORY_UPDATES", "UNREAD"],
                                   due="2026-02-26"), reachability=reachability)
        self.checks["rows"][0]["fact_review"] = dict(complete=True, reason="Due date bound.", claims=[
            dict(id="DUE", quote="2026-02-26", kind="DATE", source_ids=["NOTICE"], reason="The notice's deadline.",
                 selection=dict(source_id="NOTICE", pointer="/due")),
            dict(id="KEY", quote="ENG-2443", kind="NOT_A_CLAIM", source_ids=[], reason="Ticket key under test elsewhere.")])

    def test_trash_notice_is_unresolved_and_needs_unobservable(self):
        self.bind("TRASH")
        with self.assertRaisesRegex(ValueError, "deciding record is unreachable"):
            self.check()
        result = self.check([issue("unobservable", [1])])
        self.assertTrue(any("not reachable" in item for item in result["unresolved"]))
        self.assertEqual(result["fact_results"][0]["mismatches"], [])

    def test_prompt_linked_notice_is_checked_normally(self):
        self.bind("PROMPT_LINKED")
        result = self.check()
        self.assertTrue(result["fact_results"][0]["computed"][0]["matched"])

    def test_every_source_anchor_records_reachability(self):
        del self.checks["sources"][0]["reachability"]
        with self.assertRaisesRegex(ValueError, "reachability"):
            self.check()


class OverlyBroadTests(unittest.TestCase):
    def test_overly_broad_is_major(self):
        rubric = [row(C47)] * 10
        found = issue("overly_broad", [1], impact="accepts_wrong")
        scored = calculate(tally(10, [found], 2, rubric=rubric), rubric)
        self.assertEqual(scored["severity_counts"], {"Major": 1, "Moderate": 0, "Minor": 0})
        self.assertEqual(scored["verdict"], "FAIL")


class OECrossCheckTests(unittest.TestCase):
    """Point 4: the rubric eval maps rows to OE steps both ways and records OE conflicts."""

    def setUp(self):
        self.rubric = [row("The Agent creates the settlement sheet with the four creditor balances."),
                       row(ROW_45), row("The Agent comments the payoff on ENG-2442.")]

    def record(self, rows=None, conflicts=(), issues=()):
        record = tally(3, list(issues), 2 if issues else 5, rubric=self.rubric)
        record["oe_cross_check"] = dict(
            oe_present=True, steps=["OE 13", "OE 14", "OE 21"],
            rows=rows or [dict(row=1, oe_step_ids=["OE 14"], reason="OE 14 creates the sheet."),
                          dict(row=2, oe_step_ids=["OE 14", "OE 21"], reason="The save and the reply."),
                          dict(row=3, oe_step_ids=["OE 21"], reason="Reply step reaches the ticket note.")],
            conflicts=list(conflicts))
        return record

    def test_every_row_needs_oe_step_ids_when_oes_exist(self):
        record = self.record()
        del record["oe_cross_check"]["rows"][2]
        with self.assertRaisesRegex(ValueError, "one oe_step_ids entry per criterion"):
            calculate(record, self.rubric)
        with self.assertRaisesRegex(ValueError, "oe_cross_check"):
            calculate({**self.record(), "oe_cross_check": None}, self.rubric)

    def test_row_grading_a_ticket_no_oe_step_reads_is_rejected(self):
        rows = self.record()["oe_cross_check"]["rows"]
        rows[2] = dict(row=3, oe_step_ids=[], reason="No OE step reads or writes ENG-2442.")
        with self.assertRaisesRegex(ValueError, "R3 is oe_unmapped"):
            calculate(self.record(rows), self.rubric)
        rows[2]["unmapped"] = dict(resolution="ROW_DEFECT", reason="The prompt never asks for ENG-2442.")
        with self.assertRaisesRegex(ValueError, "oe_unmapped row defect needs its recorded issue"):
            calculate(self.record(rows), self.rubric)
        scored = calculate(self.record(rows, issues=[issue("unauthorized", [3])]), self.rubric)
        self.assertEqual(scored["oe_unmapped_rows"], [3])
        rows[2]["unmapped"] = dict(resolution="OE_GAP", reason="Authorized ticket note; the OE skipped it.")
        scored = calculate(self.record(rows), self.rubric)
        self.assertEqual((scored["verdict"], scored["oe_send_back"][0]["row"]), ("PASS", 3))

    def conflict(self, resolution, **extra):
        return dict(step="OE 14", row=2, resolution=resolution, source_ids=["P1"],
                    oe_quote="Expected: a new spreadsheet ID and link, with the Wind Down folder as its parent.",
                    row_quote="could not save the settlement sheet in the Wind Down folder",
                    reason="An Agent following OE 14 saves the sheet in the folder and fails the row.", **extra)

    def test_task_45_conflict_is_recorded_with_both_quotes(self):
        scored = calculate(self.record(conflicts=[self.conflict("FIX_OE")]), self.rubric)
        self.assertEqual(scored["oe_conflicts"][0]["step"], "OE 14")
        self.assertIn("Wind Down folder as its parent", scored["oe_conflicts"][0]["oe_quote"])
        self.assertEqual(scored["oe_send_back"][0]["step"], "OE 14")
        with self.assertRaisesRegex(ValueError, "settled against the row needs its recorded issue"):
            calculate(self.record(conflicts=[self.conflict("FIX_ROW")]), self.rubric)
        fixed = calculate(self.record(conflicts=[self.conflict("FIX_ROW")], issues=[issue("incorrect", [2])]),
                          self.rubric)
        self.assertEqual(fixed["verdict"], "FAIL")
        open_conflict = calculate(self.record(conflicts=[self.conflict("UNRESOLVED")]), self.rubric)
        self.assertEqual((open_conflict["execution_status"], open_conflict["verdict_score"]), ("PARTIAL", None))

    def test_conflict_quote_and_step_must_belong_to_the_row(self):
        bad = self.conflict("FIX_OE", )
        bad["row_quote"] = "saves the sheet in the Wind Down folder"
        with self.assertRaisesRegex(ValueError, "row_quote must be in the title"):
            calculate(self.record(conflicts=[bad]), self.rubric)
        bad = self.conflict("FIX_OE")
        bad["step"] = "OE 13"
        with self.assertRaisesRegex(ValueError, "mapped OE steps"):
            calculate(self.record(conflicts=[bad]), self.rubric)
        bad = self.conflict("FIX_OE")
        bad["source_ids"] = []
        with self.assertRaisesRegex(ValueError, "cites the deciding records"):
            calculate(self.record(conflicts=[bad]), self.rubric)

    def test_task_13_model_reply_conflict(self):
        rubric = [row(R85_13, weight=3)]
        record = tally(1, [], 5, rubric=rubric)
        record["oe_cross_check"] = dict(oe_present=True, steps=["OE 21"], rows=[
            dict(row=1, oe_step_ids=["OE 21"], reason="The reply step writes the graded reply.")], conflicts=[dict(
                step="OE 21", row=1, resolution="FIX_ROW", source_ids=["P1"],
                oe_quote="CF prod and all AWS accounts: close after the 2026-03-09 teardown review",
                row_quote="the Domino Delights dev account can be shut down now or by 2026-02-17",
                reason="The register has no DD dev row; OE 21's reply fails R85, so the row is fixed.")])
        with self.assertRaisesRegex(ValueError, "needs its recorded issue"):
            calculate(record, rubric)
        record.update(issues=[issue("unauthorized", [1])])
        record["dimensions"]["overall_quality"]["score"] = 2
        record["hard_gates"]["accuracy_acceptance"]["result"] = "FAIL"
        self.assertEqual(calculate(record, rubric)["oe_conflicts"][0]["row"], 1)

    def test_no_oe_means_no_mapping(self):
        record = tally(3, [], 5, rubric=self.rubric)
        self.assertEqual(calculate(record, self.rubric)["oe_present"], False)
        record["oe_cross_check"]["rows"] = [dict(row=1, oe_step_ids=[], reason="No OE.")]
        with self.assertRaisesRegex(ValueError, "need oe_present true"):
            calculate(record, self.rubric)


class OEBindingTests(Workspace):
    def states(self):
        return review_context(self.root)["manifest"]["inputs"]

    def cross(self, conflicts=()):
        return dict(oe_present=True, steps=["OE 13", "OE 14"], rows=[], conflicts=list(conflicts))

    def test_saved_oe_requires_the_cross_check_and_binds_quotes(self):
        inputs.save_input("prompt", content=b"Put the plan in a sheet in the wind down folder.")
        with self.assertRaisesRegex(ValueError, "contradicts the saved OE input"):
            check_oe_binding(self.root, self.cross(), self.states(), {"P1"})
        check_oe_binding(self.root, dict(oe_present=False), self.states(), {"P1"})
        inputs.save_input("oe", content=OE_45.encode())
        with self.assertRaisesRegex(ValueError, "contradicts the saved OE input"):
            check_oe_binding(self.root, dict(oe_present=False), self.states(), {"P1"})
        conflict = dict(step="OE 14", row=1, resolution="FIX_OE", source_ids=["P1"], row_quote="x", reason="x",
                        oe_quote="Expected: a new spreadsheet ID and link, with the Wind Down folder as its parent.")
        check_oe_binding(self.root, self.cross(conflicts=[conflict]), self.states(), {"P1"})
        with self.assertRaisesRegex(ValueError, "absent from the saved OE"):
            check_oe_binding(self.root, self.cross(conflicts=[{**conflict, "oe_quote": "moves nothing"}]),
                             self.states(), {"P1"})
        with self.assertRaisesRegex(ValueError, "step label is absent"):
            check_oe_binding(self.root, {**self.cross(), "steps": ["OE 99"]}, self.states(), {"P1"})
        with self.assertRaisesRegex(ValueError, "verified source ledger"):
            check_oe_binding(self.root, self.cross(conflicts=[conflict]), self.states(), {"OTHER"})

    def test_an_oe_edit_makes_the_rubric_review_stale(self):
        self.assertIn("oe", INPUT_KEYS)
        inputs.save_input("prompt", content=b"Put the plan in a sheet in the wind down folder.")
        inputs.save_input("oe", content=OE_45.encode())
        before = review_context(self.root)["sha256"]
        inputs.save_input("oe", content=(OE_45 + "OE 22  Tell Leonard where the sheet is.\n").encode())
        self.assertNotEqual(review_context(self.root)["sha256"], before)


if __name__ == "__main__":
    unittest.main()

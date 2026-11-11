"""Tests for platform_delta_lint.py. Run: cd Task_Authoring/tools && python3.12 -B -m unittest test_platform_delta_lint"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

import platform_delta_lint as pdl
import selftest_sandbox


def row(title, category="Outcome", weight=1):
    return {"title": title, "category": category, "weight": weight, "justification": "Lookup: fixture.",
            "evidence": "Source: fixture record ENG-1. Accept: as the title says."}


def lint(*titles, process=()):
    """Findings of the rubric lint as {(row id, rule)}; titles listed in `process` get the Process category."""
    rows = [row(t, "Process" if t in process else "Outcome") for t in titles]
    out = pdl.lint_rubric(rows)
    return {(f["row"], f["rule"]) for f in out["findings"]}, out


# Rows that grade single targets, so count rows beside them have siblings.
MOVES = [f"The Agent moves ENG-{200 + n} to Canceled" for n in range(1, 4)]


class RubricRules(unittest.TestCase):
    """Each implemented /rubric rule on a planted bad row and on a clean row."""

    def assertFlags(self, rule, titles, row_id, process=()):
        found, out = lint(*titles, process=process)
        self.assertIn((row_id, rule), found, out["findings"])

    def assertClean(self, rule, titles, process=()):
        found, out = lint(*titles, process=process)
        self.assertFalse([f for f in out["findings"] if f["rule"] == rule], out["findings"])

    # one-row-per-write
    def test_one_row_per_write_quantifier_over_writes(self):
        self.assertFlags("one-row-per-write", ["The Agent adds a comment to each of the 12 issues in the Cleanup "
                                               "project"], "R1")

    def test_one_row_per_write_comments_whose_content_differs(self):
        # douglas r1 R43: "each saying which ..." is no template; comments that differ get one row each
        self.assertFlags("one-row-per-write", ["The Agent adds a new comment to exactly 15 ZOM tickets moved back to "
                                               "Todo, each saying which change still has to go out"], "R1")

    def test_one_row_per_write_moves_over_the_sample_cap(self):
        moves = [f"The Agent moves ENG-{300 + n} to Done" for n in range(1, 8)]
        self.assertFlags("one-row-per-write", moves + ["The Agent moves exactly 15 tickets to Done"], "R8")

    def test_one_row_per_write_clean_single_target(self):
        self.assertClean("one-row-per-write", ["The Agent adds a comment on ENG-101 saying the fix shipped",
                                               "The Agent moves ENG-201 (Old flag) to Canceled"])

    def test_group_row_that_states_its_template_is_the_volume_row(self):
        # calvin r2/r3 R13 and R131 passed: the platform read each as the volume row of a template group of writes
        for title in ("The Agent gives the 10 child issues it creates under ZOM-543 the template of Brian's note: team "
                      "ZOM and no assignee (volume row for the child spot checks)",
                      "The Agent gives the 17 report sub-issues it creates under the area children the template of "
                      "Brian's note: no priority and no assignee (volume row for the sub-issue spot checks)"):
            found, out = lint(title)
            self.assertFalse(found, out["findings"])
            self.assertIn(("count_bundle", "R1"), [(r["rule"], r["row"]) for r in out["review"]])

    def test_template_word_does_not_excuse_content_that_differs_per_target(self):
        self.assertFlags("one-row-per-write", ["The Agent adds a comment to the 12 issues in the Cleanup project with "
                                               "the template of Ana's note, each saying which change still has to go "
                                               "out"], "R1")

    # bundled_writes
    def test_bundled_writes_count_with_id_range(self):
        self.assertFlags("bundled_writes", ["The Agent moves exactly 4 tickets to Done, ENG-101 to ENG-104"], "R1")

    def test_bundled_writes_count_with_named_members(self):
        # llc r1 R37 and R38
        self.assertFlags("bundled_writes", ["The Agent gives its plan sheet exactly 38 item rows, one per issue in "
                                            "the take-over project plus the Combo Fighter VO campaign"], "R1")
        self.assertFlags("bundled_writes", ["The Agent marks exactly 7 rows of its plan sheet as the LLC's, apart "
                                            "from the Metabase, dbt and GitHub rows"], "R1")

    def test_bundled_writes_count_joined_to_identity(self):
        # bridge r1 R12
        self.assertFlags("bundled_writes", ["The Agent lists exactly one angel on the send list: Anton Bernstein"],
                         "R1")

    def test_bundled_writes_clean_template_phrase(self):
        # "one row per firm" states what a row is, not who is in it (bridge final R4 passed)
        self.assertClean("bundled_writes", ["The Agent lists exactly 25 recipients on the bridge-round send list, one "
                                            "row per firm or angel",
                                            "The Agent puts Sciplay in the Keep warm group on the bridge-round send "
                                            "list"])

    # count-bundle-v1
    def test_count_bundle_count_beside_per_target_rows(self):
        titles = ["The Agent emails vendor one about the renewal", "The Agent emails vendor two about the renewal",
                  "The Agent emails exactly 3 vendors about the renewal"]
        self.assertFlags("count-bundle-v1", titles, "R3")

    def test_count_bundle_second_count_over_one_table(self):
        # claire a2r1 R23/R24: counts over tracker cells beyond the volume row
        titles = ["The Agent lists exactly 58 ads in its tracker", "The Agent marks exactly 14 surfaces Skip in its "
                  "tracker", "The Agent marks ART-806 Skip in its tracker"]
        self.assertFlags("count-bundle-v1", titles, "R2")

    def test_count_bundle_second_count_on_the_same_named_tab_still_flags(self):
        titles = ["The Agent lists exactly 39 reports in the Reports tab of the stock-take sheet, one row each",
                  "The Agent lists exactly 12 open reports in the Reports tab of the stock-take sheet, one row each"]
        self.assertFlags("count-bundle-v1", titles, "R2")

    def test_count_bundle_clean_counts_on_different_named_tabs(self):
        # calvin r3 R138 and R154 passed: one volume row per tab of the same sheet
        self.assertClean("count-bundle-v1", [
            "The Agent lists exactly 39 reports in the Reports tab of the stock-take sheet, one row each",
            "The Agent lists exactly 10 areas in the Areas tab of the stock-take sheet, one row each"])

    def test_count_bundle_clean_count_in_a_named_column_beside_the_row_count(self):
        # samuel r2 R41 kept as the Call column's Go control beside the sheet's row count
        self.assertClean("count-bundle-v1", [
            "The Agent writes exactly 36 message rows under the header of its calls sheet, one per message",
            "The Agent enters Go in the Call column of exactly 2 rows of its calls sheet"])

    def test_count_bundle_clean_volume_row_of_a_sample_group(self):
        found, out = lint(*(MOVES + ["The Agent moves exactly 9 of the 12 stale tickets to Canceled"]))
        self.assertFalse(found, out["findings"])
        self.assertIn({"rule": "count_bundle", "row": "R4"}, [{k: r[k] for k in ("rule", "row")} for r in out["review"]])

    # template-only-sampling
    def test_template_only_sampling_sampled_creations_without_template(self):
        titles = ["The Agent creates a card for Acme in the To Do list of the Ops board",
                  "The Agent creates exactly 8 new cards in the To Do list of the Ops board"]
        self.assertFlags("template-only-sampling", titles, "R2")

    def test_template_only_sampling_clean_when_template_stated(self):
        titles = ["The Agent creates a card for Acme in the To Do list of the Ops board",
                  "The Agent creates exactly 8 new cards in the To Do list of the Ops board, one per company, each "
                  "with that company's name in its title"]
        self.assertClean("template-only-sampling", titles)

    # scope_tail
    def test_scope_tail_no_other_target(self):
        # vincent r1 R41
        self.assertFlags("scope_tail", ["The Agent writes its blocker list into the description of the release "
                                        "ticket ZOM-570 and into no other Linear issue's description"], "R1")

    def test_scope_tail_inside_acceptance_note(self):
        # seed r2 R1: the restriction sat in the parenthetical
        self.assertFlags("scope_tail", ["The Agent creates its payee sheet for Leonard (… writing the payee lines "
                                        "into Leonard's Angel note working sheet fails)"], "R1")

    def test_scope_tail_clean(self):
        self.assertClean("scope_tail", ["The Agent adds its blocker list to the description of ZOM-570",
                                        "The Agent tells Mateo in writing that the agreement is with Leonard to sign "
                                        "(a reply saying it goes to the lawyers first fails)"])

    # no-guard-without-trap
    def test_no_guard_exclusion_only(self):
        self.assertFlags("no-guard-without-trap", ["The Agent comments due dates only on tickets other than ENG-301 "
                                                   "and ENG-302"], "R1")

    def test_no_guard_leave_alone_row(self):
        # julia r1 R7-R18: an empty tab passes "leaves ZOM-30 off"
        self.assertFlags("no-guard-without-trap", ["The Agent leaves ZOM-30 off the Tickets tab of the baseline "
                                                   "register"], "R1")

    def test_no_guard_prohibition(self):
        self.assertFlags("no-guard-without-trap", ["The Agent does not move ENG-12"], "R1")

    def test_no_guard_clean_leaves_a_comment(self):
        self.assertClean("no-guard-without-trap", ["The Agent leaves a comment on ENG-2434 saying it is not done "
                                                   "because the popup still uses the old sprites"])

    def test_no_guard_exactly_one_is_review_not_finding(self):
        found, out = lint("The Agent posts exactly one message in #zombie-bugs")
        self.assertNotIn(("R1", "no-guard-without-trap"), found)
        self.assertIn("no-guard-without-trap", {r["rule"] for r in out["review"]})

    # multi_part_write
    def test_multi_part_action_and_date(self):
        self.assertFlags("multi_part_write", ["The Agent adds a new comment on ENG-401 saying the plan is cancelled "
                                              "by Feb 17, 2026"], "R1")

    def test_multi_part_state_and_assignee(self):
        # samuel r2 R117-R120
        self.assertFlags("multi_part_write", ["The Agent files its new ticket for the ask on ZOM-542 in Backlog with "
                                              "no assignee"], "R1")

    def test_multi_part_clean(self):
        self.assertClean("multi_part_write", ["The Agent files its new ticket for the ask on ZOM-542 in Backlog",
                                              "The Agent adds a new comment on ENG-401 saying the plan is cancelled",
                                              "The Agent files exactly 9 new issues, each in Backlog with no assignee"])

    # content-row-proves-write
    WINDDOWN = ["The Agent posts its reply to Leonard as a reply in the thread of his Feb 13 ask in #winddown",
                "The Agent states in its #winddown thread reply to Leonard that the monthly total is 6,706.49",
                "The Agent names in its #winddown thread reply to Leonard the Slack plan clash"]

    def test_content_row_proves_write_flagged(self):
        # winddown r1 R111
        self.assertFlags("content-row-proves-write", self.WINDDOWN, "R1")

    def test_content_row_kept_when_content_rows_do_not_name_the_thread(self):
        # owen r2 R134 was kept: R135-R137 did not say "thread"
        self.assertClean("content-row-proves-write", [
            "The Agent replies to Arthur in the thread of his Feb 12 DM to Owen",
            "The Agent tells Arthur in its reply to Arthur in his Feb 12 DM that 9 bugs are still broken",
            "The Agent tells Arthur in its reply to Arthur in his Feb 12 DM that it filed 68 new tickets"])

    def test_content_row_comment_on_a_key(self):
        self.assertFlags("content-row-proves-write", ["The Agent comments on ENG-101",
                                                      "The Agent states in its comment on ENG-101 that the fix "
                                                      "shipped"], "R1")

    def test_content_row_ignores_ordering_rows(self):
        titles = ["The Agent replies to Leonard in the thread under his DM",
                  "The Agent posts its reply to Leonard only after its Linear writes are finished"]
        self.assertClean("content-row-proves-write", titles)

    # table-spot-check-rule
    def test_table_volume_row_without_samples(self):
        # bridge r1 R20
        titles = ["The Agent creates a Keep warm checklist on the Investor Update card holding exactly 3 items",
                  "The Agent adds Sciplay as an item on the Keep warm checklist of the Investor Update card",
                  "The Agent creates an Awaiting reply checklist on the Investor Update card holding exactly 14 items"]
        found, out = lint(*titles)
        self.assertIn(("R3", "table-spot-check-rule"), found)
        self.assertNotIn(("R1", "table-spot-check-rule"), found)

    def test_table_rows_are_not_one_row_per_write(self):
        titles = ["The Agent fills the sign-off register with exactly 17 ticket rows",
                  "The Agent records ZOM-12 as on prod in the sign-off register",
                  "The Agent records ZOM-14 as not on prod in the sign-off register"]
        found, out = lint(*titles)
        self.assertFalse(found, out["findings"])
        self.assertIn("R1", out["notes"]["count_bundle"])

    # title-cap-120-words
    def test_title_cap(self):
        self.assertFlags("title-cap-120-words", ["The Agent states in its reply that " + " ".join(["w"] * 121)], "R1")
        self.assertClean("title-cap-120-words", ["The Agent states in its reply that " + " ".join(["w"] * 113)])

    # deliverable_claim: review only
    def test_deliverable_claim_is_review_only(self):
        found, out = lint("The Agent links its plan sheet in its reply to Leonard")
        self.assertFalse([f for f in out["findings"] if f["rule"] == "deliverable_claim"])
        self.assertIn("deliverable_claim", {r["rule"] for r in out["review"]})

    # self-containment-sibling-titles: never flagged
    def test_sibling_titles_supplying_acceptance_values_not_flagged(self):
        titles = ["The Agent adds a tab named Rules in force to the ZM difficulty baseline register",
                  "The Agent lists Mailman on its Rules in force tab with its enrage speed",
                  "The Agent adds a new comment on ENG-2432 saying the fix is in 0.3.310",
                  "The Agent names the Bug label in its comment"]
        found, out = lint(*titles)
        self.assertFalse(found, out["findings"])
        self.assertIn("not flagged", out["notes"]["self-containment-sibling-titles"])

    def test_process_rows_are_not_write_rows(self):
        title = "The Agent posts its reply to Leonard only after its Linear writes are finished"
        found, _ = lint(title, process=(title,))
        self.assertFalse(found)


class Severity(unittest.TestCase):
    """FAIL for the platform's own wording, WARN for a reconstructed rule, unless BACKTESTED overrides."""

    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("test_platform_delta_lint_")
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def task(self, name, titles, register=None):
        folder = self.root / name
        reg = pdl._write_task(folder, [row(t) for t in titles], register=register)
        return folder, reg

    def test_wording_sets_severity(self):
        flipped = pdl._fixture_register({"scope_tail": "verbatim", "one-row-per-write": "reconstructed"})
        folder, reg = self.task("flip", [pdl.FIXTURE_BAD["scope_tail"], pdl.FIXTURE_BAD["one-row-per-write"]],
                                register=flipped)
        result = pdl.evaluate(folder, register_path=reg)
        by_rule = {f["rule"]: (f["severity"], f["wording"]) for f in result["findings"]}
        self.assertEqual(by_rule["scope_tail"], ("FAIL", "verbatim"))
        self.assertEqual(by_rule["one-row-per-write"], ("WARN", "reconstructed"))
        self.assertEqual(result["verdict"], "FAIL")

    def test_reconstructed_only_finding_gives_warn_verdict(self):
        folder, reg = self.task("warn", [pdl.FIXTURE_BAD["scope_tail"]])
        result = pdl.evaluate(folder, register_path=reg)
        self.assertEqual(result["verdict"], "WARN")
        self.assertEqual({c["id"]: c["status"] for c in result["checks"]}["delta.scope_tail"], "WARN")

    def test_backtested_overrides_wording(self):
        register = pdl.load_register(None)
        self.assertEqual(register["bundled_writes"]["wording"], "reconstructed")
        self.assertEqual(pdl.severity_of("bundled_writes", register), "FAIL")           # raised by the backtest
        self.assertEqual(register["content-row-proves-write"]["wording"], "verbatim")
        self.assertEqual(pdl.severity_of("content-row-proves-write", register), "WARN")  # lowered by the backtest
        self.assertEqual(pdl.severity_of("count-bundle-v1", register), "FAIL")            # verbatim default
        self.assertEqual(pdl.severity_of("scope_tail", register), "WARN")                 # reconstructed default
        for rule, record in pdl.BACKTESTED.items():
            self.assertIn(record["severity"], ("FAIL", "WARN"))
            self.assertTrue(record.get("basis"), rule)

    def test_clean_rubric_passes(self):
        folder, reg = self.task("clean", list(pdl.FIXTURE_CLEAN))
        result = pdl.evaluate(folder, register_path=reg)
        self.assertEqual(result["verdict"], "PASS", result["findings"])
        self.assertTrue(all(c["status"] == "PASS" for c in result["checks"]))


class Listing(unittest.TestCase):
    def test_not_mechanised_listing(self):
        with selftest_sandbox.scratch_tmp("test_platform_delta_lint_") as tmp:
            folder = Path(tmp) / "task"
            pdl._write_task(folder, [row(t) for t in pdl.FIXTURE_CLEAN])
            result = pdl.evaluate(folder)                                  # the real register
        listed = [item["rule"] for item in result["not_mechanised"]]
        self.assertEqual(len(listed), len(set(listed)))
        self.assertTrue(set(listed) <= set(pdl.NOT_MECHANISED), listed)
        self.assertIn("decision_fork", listed)
        self.assertNotIn("content-row-proves-write", listed)
        for item in result["not_mechanised"]:
            self.assertTrue(item["check"] and item["reason"] and item["wording"] in ("verbatim", "reconstructed"))

    def test_every_register_rule_is_classified(self):
        table = pdl.rule_table(pdl.load_register(None))
        self.assertEqual(len(table), len(pdl.load_register(None)))
        handling = {e["id"]: e["handling"] for e in table}
        self.assertFalse([e for e in table if e.get("reason") == "not reviewed"])
        self.assertEqual(handling["json_shape"], "other_tool")
        self.assertEqual(handling["content-row-proves-write"], "implemented")
        self.assertEqual(handling["self-containment-sibling-titles"], "implemented")

    def test_new_register_rule_is_not_dropped(self):
        register = pdl._fixture_register()
        register["rules"].append({"id": "brand-new-v1", "eval": "/rubric", "wording": "verbatim",
                                  "local_status": "absent", "local_ref": None})
        with selftest_sandbox.scratch_tmp("test_platform_delta_lint_") as tmp:
            folder = Path(tmp) / "task"
            reg = pdl._write_task(folder, [row(t) for t in pdl.FIXTURE_CLEAN], register=register)
            result = pdl.evaluate(folder, register_path=reg)
        item = [i for i in result["not_mechanised"] if i["rule"] == "brand-new-v1"]
        self.assertEqual(item[0]["reason"], "not reviewed")


class ApiAndCli(unittest.TestCase):
    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("test_platform_delta_lint_")
        self.root = Path(self._tmp.name)
        self.folder = self.root / "task"
        self.reg = pdl._write_task(self.folder, [row(t) for t in pdl.FIXTURE_CLEAN]
                                   + [row(pdl.FIXTURE_BAD["count-bundle-v1"])])

    def tearDown(self):
        self._tmp.cleanup()

    def test_deterministic(self):
        one = pdl.evaluate(self.folder, artifact="rubric", register_path=self.reg)
        two = pdl.evaluate(self.folder, artifact="rubric", register_path=self.reg)
        self.assertEqual(json.dumps(one, sort_keys=True), json.dumps(two, sort_keys=True))
        self.assertEqual(pdl.render_text(one), pdl.render_text(two))

    def test_result_shape_and_binding(self):
        result = pdl.evaluate(self.folder, artifact="rubric", register_path=self.reg)
        for key in ("tool", "version", "verdict", "bound_to", "checks", "findings", "review", "not_mechanised"):
            self.assertIn(key, result)
        self.assertEqual(result["verdict"], "FAIL")
        self.assertIn("09_Rubrics.json", result["bound_to"])
        self.assertTrue(all(c["id"].startswith("delta.") for c in result["checks"]))
        self.assertTrue(all(f["check"] == "delta." + f["rule"] for f in result["findings"]))

    def test_missing_rubric_fails_input(self):
        (self.root / "empty").mkdir()
        result = pdl.evaluate(self.root / "empty", register_path=self.reg)
        self.assertEqual((result["verdict"], result["checks"][0]["id"]), ("FAIL", "delta.input"))

    def test_context_files_found_the_stage_gate_way(self):
        # 09_Rubrics.json is a top-level slot; the gradable surface is a generated file under Working_Files/
        surface = self.folder / "Working_Files" / "01_Gradable_Surface.json"
        surface.write_text(json.dumps({"slots": [{"id": "S1", "role": "volume"}]}))
        result = pdl.evaluate(self.folder, register_path=self.reg)
        self.assertIn("Working_Files/01_Gradable_Surface.json", result["bound_to"])
        detail = {c["id"]: c["detail"] for c in result["checks"]}["delta.count_bundle"]
        self.assertIn("1 volume slot", detail)

    def test_cli_header_and_exit_codes(self):
        code, text = pdl._run_cli(["rubric", "--task-dir", str(self.folder), "--register", str(self.reg)])
        self.assertEqual(code, 1)
        self.assertTrue(text.startswith("PLATFORM DELTA LINT (rubric): FAIL\n"), text[:80])
        self.assertIn("[FAIL] delta.count-bundle-v1:", text)
        code, text = pdl._run_cli(["rubric", "--task-dir", str(self.folder), "--register", str(self.reg), "--json"])
        self.assertEqual((code, json.loads(text)["verdict"]), (1, "FAIL"))
        code, _ = pdl._run_cli(["rubric", "--task-dir", str(self.folder), "--register", str(self.root / "no.json")])
        self.assertEqual(code, 2)
        code, _ = pdl._run_cli(["rubric"])
        self.assertEqual(code, 2)
        code, text = pdl._run_cli(["rules", "--register", str(self.reg)])
        self.assertTrue(code == 0 and text.startswith("PLATFORM DELTA LINT (rules):"))

    def test_prompt_and_oe(self):
        folder = self.root / "po"
        reg = pdl._write_task(folder, [row(pdl.FIXTURE_CLEAN[0])], prompt="Share the sheet and send me the link.\n",
                              oe="1. Read.\n   Expected: a thread reply or a new message, either is fine.\n")
        prompt = pdl.evaluate(folder, "prompt", register_path=reg)
        oe = pdl.evaluate(folder, "oe", register_path=reg)
        self.assertEqual((prompt["verdict"], oe["verdict"]), ("WARN", "WARN"))
        self.assertEqual(oe["findings"][0]["row"], "L2")
        clean = pdl.evaluate(self.folder, "oe", register_path=self.reg)
        self.assertEqual(clean["verdict"], "PASS")


@unittest.skipUnless(pdl.ARCHIVE.is_dir(), "no archived tasks")
class Backtest(unittest.TestCase):
    """The stored platform verdicts: no FAIL-severity finding on a passed final whose rule was in force, and the
    BACKTESTED table matches the numbers."""

    @classmethod
    def setUpClass(cls):
        cls.result = pdl.backtest(eval_lint=False)

    def test_no_false_alarm_in_force(self):
        self.assertEqual(self.result["summary"]["false_alarms_in_force"], 0,
                         [(r["rule"], r["alarms"]) for r in self.result["rules"] if r["alarms"]])

    def test_backtested_table_current(self):
        self.assertEqual(self.result["summary"]["backtested_table_stale"], [])

    def test_rounds_checked(self):
        self.assertGreaterEqual(self.result["summary"]["rounds_with_bytes"], 13)
        self.assertFalse([r["round"] for r in self.result["rounds"] if "error" in r])


if __name__ == "__main__":
    unittest.main()

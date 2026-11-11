"""Tests for difficulty_budget.py; run with: cd Task_Authoring/tools && python3.12 -B -m unittest test_difficulty_budget."""
from __future__ import annotations

import contextlib
import copy
import hashlib
import io
import json
import random
import statistics
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

import difficulty_budget as db
import difficulty_stats as stats
import selftest_sandbox

QUICK = dict(db.load_policy(), trials=3000)          # structural tests do not need 20,000 trials
SURFACE = "01_Gradable_Surface.json"


def unit(uid, role, rows, rate, habit=None, carrier="reply_under_unrelated_parent", cause=None):
    service, action = habit or ("svc", f"read_{uid}")
    return {"id": uid, "role": role, "cause": f"cause of {uid}", "cause_key": cause or f"cause_{uid}",
            "carrier": carrier, "habit": {"service": service, "action": action},
            "decider": {"service": service, "record_id": f"rec-{uid}", "container": "", "injected": True},
            "find_rate": list(rate), "find_rate_basis": "test",
            "rows": [{"id": rid, "weight": weight} for rid, weight in rows], "mechanism": uid}


def budget_of(units, total, mode="easy", loss=(0.0, 0.0)):
    """(budget, basis): the basis holds every unit row plus one filler row for the rest of the weight."""
    rows = {}
    for item in units:
        if item["role"] != "realism":
            for row in item["rows"]:
                rows[row["id"]] = row["weight"]
    rest = total - sum(rows.values())
    assert rest >= 0, rest
    if rest:
        rows["FILL"] = rest
    budget = {"schema": db.SCHEMA, "design_id": "D1", "revision": "rev1", "mode": mode, "weight_basis": "surface",
              "total_weight": total, "undesigned_loss": list(loss), "units": units}
    return budget, {"rows": rows, "file": SURFACE}


def good():
    return db.good_budget(), {"rows": {slot["id"]: slot["weight"] for slot in db.good_surface()["slots"]},
                              "file": SURFACE}


def run(budget, basis, rubric=None, context=None, policy=QUICK):
    return db.evaluate_budget(budget, basis, rubric, context, policy)


def statuses(result):
    return {check["id"]: check["status"] for check in result["checks"]}


def detail(result, cid):
    return next(check["detail"] for check in result["checks"] if check["id"] == cid)


def by_id(budget, uid):
    return next(item for item in budget["units"] if item["id"] == uid)


def coin(uid, rate=(0.4, 0.6), weight=5, rows=3, **extra):
    return unit(uid, "variance", [(f"{uid}{letter}", weight) for letter in "abcdef"[:rows]], rate, **extra)


def anchor(uid, rate=(0.0, 0.15), rows=((5,), (3,)), **extra):
    return unit(uid, "anchor", [(f"{uid}{n}", weight[0]) for n, weight in enumerate(rows)], rate, **extra)


class SchemaTests(unittest.TestCase):
    def test_good_budget_is_well_formed(self):
        self.assertEqual(db.schema_problems(db.good_budget()), [])

    def test_each_schema_error_is_named(self):
        cases = [
            (lambda b: b.update(schema="v0"), "schema must be"),
            (lambda b: b.update(design_id=""), "design_id"),
            (lambda b: b.update(mode="extreme"), "mode must be"),
            (lambda b: b.update(weight_basis="guess"), "weight_basis"),
            (lambda b: b.update(total_weight=0), "total_weight"),
            (lambda b: b.update(total_weight=True), "total_weight"),
            (lambda b: b.update(undesigned_loss=[0.2, 0.1]), "undesigned_loss"),
            (lambda b: b.update(units=[]), "units must be a non-empty list"),
            (lambda b: b["units"].append("U9"), "is not an object"),
            (lambda b: by_id(b, "V2").update(id="V1"), "used twice"),
            (lambda b: by_id(b, "V1").update(role="trap"), "role must be anchor, variance or realism"),
            (lambda b: by_id(b, "V1").update(find_rate=[0.6, 0.4]), "find_rate must be [lo, hi]"),
            (lambda b: by_id(b, "V1").update(find_rate=[0.2, 1.2]), "find_rate must be [lo, hi]"),
            (lambda b: by_id(b, "V1").update(find_rate=[-0.1, 0.5]), "find_rate must be [lo, hi]"),
            (lambda b: by_id(b, "V1").update(find_rate=0.5), "find_rate must be [lo, hi]"),
            (lambda b: by_id(b, "V1").update(find_rate=[False, True]), "find_rate must be [lo, hi]"),
            (lambda b: by_id(b, "V1")["habit"].pop("action"), "habit needs a service and an action"),
            (lambda b: by_id(b, "V1")["decider"].update(injected="yes"), "decider needs"),
            (lambda b: by_id(b, "V1").update(carrier=""), "carrier"),
            (lambda b: by_id(b, "A1").update(cause_key=""), "an anchor needs a cause_key"),
            (lambda b: by_id(b, "V1")["rows"][0].update(weight=0), "weight above 0"),
            (lambda b: by_id(b, "V1")["rows"].append(dict(by_id(b, "V1")["rows"][0])), "listed twice"),
            (lambda b: b.update(rubric_rows={"ZZ": ["R1"]}), "unknown unit ZZ"),
            (lambda b: b.update(rubric_rows={"V1": "R1"}), "must be a list"),
        ]
        for change, needle in cases:
            budget, basis = good()
            change(budget)
            with self.subTest(needle=needle):
                self.assertTrue(any(needle in problem for problem in db.schema_problems(budget)),
                                db.schema_problems(budget))
                result = run(budget, basis)
                self.assertEqual(result["verdict"], "FAIL")
                got = statuses(result)
                self.assertEqual(got["budget.schema"], "FAIL")
                self.assertEqual({got[cid] for cid in db.CHECK_IDS[1:]}, {"SKIP"})
                self.assertEqual(list(got), list(db.CHECK_IDS))

    def test_not_an_object(self):
        self.assertEqual(db.schema_problems([1, 2]), ["the file is not a JSON object"])

    def test_missing_or_broken_budget_file_fails_without_a_crash(self):
        with selftest_sandbox.scratch_tmp("difficulty_budget_test_") as tmp:
            task = db._fixture(tmp)
            path = task / "Working_Files" / db.BUDGET_NAME
            path.write_text("{not json", encoding="utf-8")
            broken = db.evaluate(task)
            self.assertEqual(statuses(broken)["budget.schema"], "FAIL")
            self.assertIn("not valid JSON", detail(broken, "budget.schema"))
            path.unlink()
            missing = db.evaluate(task)
            self.assertEqual(missing["verdict"], "FAIL")
            self.assertIn("not found", detail(missing, "budget.schema"))
            self.assertIn("template", detail(missing, "budget.schema"))
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(db.main(["check", "--task-dir", str(task)]), 1)
            self.assertTrue(out.getvalue().startswith("DIFFICULTY BUDGET (unknown mode): FAIL\n"), out.getvalue())


class CheckTests(unittest.TestCase):
    def test_good_budget_passes_every_check(self):
        result = run(*good(), context={"mode": "easy"}, policy=None)       # the policy's own trial count
        self.assertEqual(result["verdict"], "PASS", db.render_text(result))
        self.assertEqual(set(statuses(result).values()), {"PASS"})
        self.assertEqual([check["id"] for check in result["checks"]], list(db.CHECK_IDS))
        sim = result["budget"]["simulation"]
        self.assertEqual((sim["trials"], sim["seed"], sim["runs"], sim["runs_one_error"]), (20000, 20261110, 6, 5))

    def test_context(self):
        budget, basis = good()
        self.assertEqual(statuses(run(budget, basis, context={"mode": "easy"}))["budget.context"], "PASS")
        wrong = run(budget, basis, context={"mode": "medium"})
        self.assertEqual(statuses(wrong)["budget.context"], "FAIL")
        self.assertIn("assignment says medium", detail(wrong, "budget.context"))
        skipped = run(budget, basis, context={"skip": "Cannot read assignment"})
        self.assertEqual(statuses(skipped)["budget.context"], "SKIP")
        self.assertIn("Cannot read assignment", detail(skipped, "budget.context"))
        self.assertEqual(skipped["verdict"], "PASS")                       # a SKIP does not change the verdict

    def test_context_is_read_through_task_context(self):
        import task_context
        with mock.patch.object(task_context, "load_context", return_value={"difficulty_mode": "hard"}) as loader:
            self.assertEqual(db._context("/some/task"), {"mode": "hard"})
            loader.assert_called_once_with("/some/task")
        with mock.patch.object(task_context, "load_context", side_effect=task_context.ContextError("no V3 here")):
            self.assertEqual(db._context("/some/task"), {"skip": "no V3 here"})

    def test_rows(self):
        cases = [
            (lambda b, rows: by_id(b, "V1")["rows"][0].update(id="nope"), "row nope is not in"),
            (lambda b, rows: by_id(b, "V1")["rows"][0].update(weight=3), "has weight 3 but"),
            (lambda b, rows: b.update(total_weight=90), "total_weight is 90 but"),
            (lambda b, rows: rows.update(EXTRA=5), "adds up to 105"),
        ]
        for change, needle in cases:
            budget, basis = good()
            change(budget, basis["rows"])
            with self.subTest(needle=needle):
                result = run(budget, basis)
                self.assertEqual(statuses(result)["budget.rows"], "FAIL")
                self.assertIn(needle, detail(result, "budget.rows"))
        budget, _ = good()
        missing = run(budget, {"error": f"{SURFACE} not found", "file": SURFACE})
        self.assertEqual(statuses(missing)["budget.rows"], "FAIL")
        self.assertIn("not found", detail(missing, "budget.rows"))
        self.assertEqual(missing["budget"]["weight_source"], "declared")   # the other checks still run

    def test_basis_files(self):
        with selftest_sandbox.scratch_tmp("difficulty_budget_test_") as tmp:
            task = db._fixture(tmp)
            work = task / "Working_Files"
            self.assertEqual(statuses(db.evaluate(task, policy=QUICK))["budget.rows"], "PASS")
            slots = db.good_surface()["slots"]
            (work / "01_Rubric_Skeleton.json").write_text(json.dumps({"rows": slots}), encoding="utf-8")
            budget = dict(db.good_budget(), weight_basis="skeleton")
            (work / db.BUDGET_NAME).write_text(json.dumps(budget), encoding="utf-8")
            skeleton = db.evaluate(task, policy=QUICK)
            self.assertEqual(statuses(skeleton)["budget.rows"], "PASS", db.render_text(skeleton))
            self.assertIn("Working_Files/01_Rubric_Skeleton.json", skeleton["bound_to"])
            (work / "01_Rubric_Skeleton.json").unlink()
            self.assertEqual(statuses(db.evaluate(task, policy=QUICK))["budget.rows"], "FAIL")
            # rubric basis: rows are R1.. in file order
            (task / db.RUBRIC_NAME).write_text(json.dumps(
                [{"title": f"Row {slot['id']}", "weight": slot["weight"], "category": "outcome"} for slot in slots]),
                encoding="utf-8")
            number = {slot["id"]: f"R{n}" for n, slot in enumerate(slots, 1)}
            budget = dict(db.good_budget(), weight_basis="rubric")
            for item in budget["units"]:
                for row in item["rows"]:
                    row["id"] = number[row["id"]]
            (work / db.BUDGET_NAME).write_text(json.dumps(budget), encoding="utf-8")
            rubric = db.evaluate(task, policy=QUICK)
            self.assertEqual(rubric["verdict"], "PASS", db.render_text(rubric))
            self.assertEqual(sorted(rubric["bound_to"]), ["09_Rubrics.json", "Working_Files/01_Difficulty_Budget.json"])

    def test_carriers(self):
        budget, basis = good()
        by_id(budget, "V2")["carrier"] = "decoy"
        failed = run(budget, basis)
        self.assertEqual(statuses(failed)["budget.carriers"], "FAIL")
        self.assertIn("V2 (decoy)", detail(failed, "budget.carriers"))
        for carrier in db.load_policy()["carriers_without_loss"]:
            budget, basis = good()
            by_id(budget, "A1")["carrier"] = carrier
            self.assertEqual(statuses(run(budget, basis))["budget.carriers"], "FAIL", carrier)
        budget, basis = good()
        by_id(budget, "V2")["carrier"] = "other:a pinned post"
        warned = run(budget, basis)
        self.assertEqual((statuses(warned)["budget.carriers"], warned["verdict"]), ("WARN", "WARN"))
        budget, basis = good()
        by_id(budget, "V2")["carrier"] = "hidden_footnote"
        unknown = run(budget, basis)
        self.assertEqual(statuses(unknown)["budget.carriers"], "FAIL")
        self.assertIn("unknown carrier", detail(unknown, "budget.carriers"))
        budget, basis = good()
        by_id(budget, "V2")["carrier"] = "other:"                          # other: needs a description
        self.assertEqual(statuses(run(budget, basis))["budget.carriers"], "FAIL")

    def test_unit_rows(self):
        budget, basis = good()
        by_id(budget, "V3")["rows"] = by_id(budget, "V3")["rows"][:1]
        one = run(budget, basis)
        self.assertEqual(statuses(one)["budget.unit_rows"], "FAIL")
        self.assertIn("V3: 1 row(s), needs 2", detail(one, "budget.unit_rows"))
        budget, basis = budget_of([anchor("A1"), anchor("A2"), coin("V1"), coin("V2"), coin("V3"),
                                   coin("V4", weight=3, rows=5)], 100)
        no_five = run(budget, basis)
        self.assertEqual(statuses(no_five)["budget.unit_rows"], "FAIL")
        self.assertIn("V4: no row of weight 5", detail(no_five, "budget.unit_rows"))

    def test_unit_rows_warns_when_a_unit_has_too_few_rows_of_its_own(self):
        budget, basis = good()
        by_id(budget, "V4")["rows"] = [{"id": "V4a", "weight": 5}] + by_id(budget, "V3")["rows"][:2]
        shared = run(budget, basis)                                         # V4 and V3 each keep one row of their own
        self.assertEqual(statuses(shared)["budget.unit_rows"], "WARN")
        self.assertIn("V3 (1 of 3); V4 (1 of 3)", detail(shared, "budget.unit_rows"))
        budget, basis = good()
        by_id(budget, "V4")["rows"] = by_id(budget, "V4")["rows"][:2] + by_id(budget, "V3")["rows"][:1]
        self.assertEqual(statuses(run(budget, basis))["budget.unit_rows"], "PASS")     # two own rows each: enough

    def test_units_behind_one_habit_are_one_coin_flip(self):
        budget, basis = good()
        by_id(budget, "V4")["habit"] = {"service": " Slack ", "action": "DM_History"}      # V1's habit, other case
        merged = run(budget, basis)
        got = statuses(merged)
        self.assertEqual(got["budget.independence"], "WARN")
        self.assertIn("V1 + V4 share slack/dm_history", detail(merged, "budget.independence"))
        self.assertEqual(got["budget.variance"], "FAIL")                   # four units, three coin flips
        self.assertIn("3 independent coin-flip habit(s)", detail(merged, "budget.variance"))
        groups = merged["budget"]["habit_groups"]
        self.assertEqual(len(groups), 5)
        self.assertIn(["V1", "V4"], [group["units"] for group in groups])
        self.assertEqual(merged["budget"]["simulation"]["habit_groups"], 5)

    def test_merged_units_move_together_in_the_simulation(self):
        rows_a, rows_b = {"Aa": 5, "Ab": 5}, {"Ba": 5, "Bb": 5}
        other = [{"habit": ("s", f"h{n}"), "lo": 0.4, "hi": 0.6, "rows": {f"O{n}a": 5, f"O{n}b": 5}} for n in range(2)]
        shared = other + [{"habit": ("s", "same"), "lo": 0.4, "hi": 0.6, "rows": rows_a},
                          {"habit": ("s", "same"), "lo": 0.4, "hi": 0.6, "rows": rows_b}]
        single = other + [{"habit": ("s", "same"), "lo": 0.4, "hi": 0.6, "rows": dict(rows_a, **rows_b)}]
        apart = other + [{"habit": ("s", "same"), "lo": 0.4, "hi": 0.6, "rows": rows_a},
                         {"habit": ("s", "zother"), "lo": 0.4, "hi": 0.6, "rows": rows_b}]
        cap = Fraction(9, 10)
        self.assertEqual(db.simulate(shared, 100, cap, policy=QUICK), db.simulate(single, 100, cap, policy=QUICK))
        self.assertGreater(db.simulate(apart, 100, cap, policy=QUICK)["lo"]["signature"],
                           db.simulate(shared, 100, cap, policy=QUICK)["lo"]["signature"])

    def test_anchors(self):
        budget, basis = good()
        by_id(budget, "A2")["cause_key"] = by_id(budget, "A1")["cause_key"].upper()
        one_cause = run(budget, basis)
        self.assertEqual(statuses(one_cause)["budget.anchors"], "FAIL")
        self.assertIn("1 separate cause(s), needs 2", detail(one_cause, "budget.anchors"))
        self.assertEqual(one_cause["budget"]["anchors"]["failed_rules"], ["causes"])

        budget, basis = good()
        by_id(budget, "A2")["habit"] = dict(by_id(budget, "A1")["habit"])        # one habit is one cause too
        self.assertEqual(run(budget, basis)["budget"]["anchors"]["failed_rules"], ["causes"])

        budget, basis = good()
        budget["mode"] = "medium"                                           # 16% carried, 15% + 2% needed
        thin = run(budget, basis)
        self.assertEqual(thin["budget"]["anchors"]["failed_rules"], ["share"])
        self.assertIn("16.0% is under the medium loss 15.0% + margin 2.0% = 17.0%", detail(thin, "budget.anchors"))

        heavy_units = [anchor("A1", rows=((5,), (5,), (5,), (5,), (5,), (5,))), anchor("A2"),
                       coin("V1"), coin("V2"), coin("V3"), coin("V4")]
        heavy = run(*budget_of(heavy_units, 100))                           # A1 carries 30 of 100
        self.assertEqual(heavy["budget"]["anchors"]["failed_rules"], ["max_share"])
        self.assertIn("A1 30.0%", detail(heavy, "budget.anchors"))

        budget, basis = good()
        by_id(budget, "A1")["find_rate"] = [0.0, 0.4]
        loose = run(budget, basis)
        self.assertEqual(loose["budget"]["anchors"]["failed_rules"], ["find_rate"])

        budget, basis = good()
        budget["units"] = [item for item in budget["units"] if item["role"] != "anchor"]
        none = run(budget, basis)
        self.assertEqual(statuses(none)["budget.anchors"], "FAIL")
        self.assertEqual(none["budget"]["anchors"]["failed_rules"], ["causes", "share"])

    def test_variance(self):
        budget, basis = good()
        budget["units"] = [item for item in budget["units"] if item["id"] != "V4"]
        three = run(budget, basis)
        self.assertEqual(statuses(three)["budget.variance"], "FAIL")
        self.assertIn("3 independent coin-flip habit(s)", detail(three, "budget.variance"))

        budget, basis = good()
        by_id(budget, "V4")["find_rate"] = [0.3, 0.6]                       # range leaves the 0.35-0.65 window
        outside = run(budget, basis)
        self.assertEqual(statuses(outside)["budget.variance"], "FAIL")
        self.assertIn("V4 (0.30-0.60)", detail(outside, "budget.variance"))

        units = [anchor("A1"), anchor("A2")] + [coin(f"V{n}", rows=2) for n in range(1, 5)]
        units.append(coin("V5", rate=(0.7, 0.9), rows=2))
        extra = run(*budget_of(units, 100))                                 # four good coin flips and one outside
        self.assertEqual(statuses(extra)["budget.variance"], "WARN")
        self.assertIn("V5 (0.70-0.90)", detail(extra, "budget.variance"))

        budget, basis = good()
        for uid in ("V1", "V2", "V3", "V4"):
            by_id(budget, uid)["find_rate"] = [0.35, 0.65]                  # the window edges are inside
        self.assertEqual(statuses(run(budget, basis))["budget.variance"], "PASS")

    def test_average_fails_when_too_little_weight_is_at_risk(self):
        budget, basis = good()
        basis["rows"]["BULK"] = 300                                         # 300 more weight every run passes
        budget["total_weight"] = 400
        thin = run(budget, basis)
        got = statuses(thin)
        self.assertEqual(got["budget.average"], "FAIL", db.render_text(thin))
        self.assertIn("at its high find rate", detail(thin, "budget.average"))
        self.assertEqual(got["budget.spread"], "WARN")                      # spread warns, it never fails
        self.assertNotIn("FAIL", {got["budget.spread"]})

    def test_undesigned_loss_ends(self):
        budget, basis = good()
        basis["rows"]["BULK"] = 300
        budget["total_weight"] = 400
        budget["undesigned_loss"] = [0.06, 0.06]                            # 6% lost at both ends
        helped = run(budget, basis)
        self.assertEqual(statuses(helped)["budget.average"], "PASS", db.render_text(helped))
        budget["undesigned_loss"] = [0.0, 0.06]                             # high find rates get the low end: 0%
        ends = run(budget, basis)
        self.assertEqual(statuses(ends)["budget.average"], "FAIL")
        sim = ends["budget"]["simulation"]
        self.assertEqual((sim["lo"]["undesigned_loss"], sim["hi"]["undesigned_loss"]), (0.06, 0.0))
        self.assertGreater(sim["lo"]["average"], sim["hi"]["average"])

    def test_full_passes_fail_when_every_unit_is_found(self):
        budget, basis = good()
        for item in budget["units"]:
            item["find_rate"] = [0.97, 1.0]
        easy = run(budget, basis)
        self.assertEqual(statuses(easy)["budget.full_passes"], "FAIL")
        self.assertEqual(easy["budget"]["simulation"]["hi"]["full_passes"], 0.0)   # found every time: six full passes
        self.assertEqual(statuses(easy)["budget.signature"], "FAIL")               # and no failing run at all

    def test_signature_needs_independent_coin_flips(self):
        budget, basis = good()
        budget["units"] = [item for item in budget["units"] if item["id"] not in ("V3", "V4")]
        two = run(budget, basis)
        self.assertEqual(statuses(two)["budget.signature"], "FAIL", db.render_text(two))
        budget, basis = good()
        budget["units"] = [item for item in budget["units"] if item["id"] != "V4"]
        three = run(budget, basis)
        got = statuses(three)
        self.assertEqual((got["budget.signature"], got["budget.signature_one_error"]), ("PASS", "FAIL"),
                         db.render_text(three))

    def test_one_row_units_do_not_split_signatures(self):
        cap = Fraction(9, 10)
        always = [{"habit": ("s", "a"), "lo": 0.0, "hi": 0.0, "rows": {"A1": 5, "A2": 5}}]
        two_rows = always + [{"habit": ("s", f"v{n}"), "lo": 0.5, "hi": 0.5, "rows": {f"V{n}a": 5, f"V{n}b": 5}}
                             for n in range(4)]
        one_row = always + [{"habit": ("s", f"v{n}"), "lo": 0.5, "hi": 0.5, "rows": {f"V{n}a": 5}} for n in range(4)]
        self.assertGreater(db.simulate(two_rows, 100, cap, policy=QUICK)["lo"]["signature"], 0.97)
        self.assertLess(db.simulate(one_row, 100, cap, policy=QUICK)["lo"]["signature"], 0.5)

    def test_hard_mode_warns(self):
        units = [anchor("A1", rows=((5,), (5,), (5,), (3,))), anchor("A2", rows=((5,), (5,), (5,), (3,))),
                 coin("V1"), coin("V2"), coin("V3"), coin("V4")]
        hard = run(*budget_of(units, 100, mode="hard"))                     # anchors 36% of 100, 32% needed
        got = statuses(hard)
        self.assertEqual(got["budget.hard_mode"], "WARN")
        self.assertIn("unverified", detail(hard, "budget.hard_mode"))
        self.assertEqual(got["budget.anchors"], "PASS", db.render_text(hard))
        self.assertEqual(hard["verdict"], "WARN")
        self.assertEqual(statuses(run(*good()))["budget.hard_mode"], "PASS")

    def test_realism_units_are_ignored(self):
        budget, basis = good()
        plain = run(budget, basis)
        budget["units"].append({"id": "J1", "role": "realism", "carrier": "decoy",
                                "rows": [{"id": "not-a-row", "weight": 99}], "find_rate": "n/a"})
        budget["rubric_rows"] = {}
        with_trap = run(budget, basis)
        self.assertEqual(statuses(with_trap), statuses(plain))
        self.assertEqual(with_trap["budget"]["simulation"], plain["budget"]["simulation"])
        self.assertIn("Realism units ignored: J1", detail(with_trap, "budget.rows"))
        self.assertIn("1 realism", detail(with_trap, "budget.schema"))
        entry = next(item for item in with_trap["budget"]["units"] if item["id"] == "J1")
        self.assertEqual((entry["rows"], entry["share"]), ([], 0.0))

    def test_rubric_rows_override(self):
        budget, basis = good()
        # The final rubric: each surface slot became two rows, plus 100 more always-pass weight.
        rubric = {"rows": {f"R{n}": 5 for n in range(1, 61)}}              # total 300
        mapping, at = {}, 1
        for item in budget["units"]:
            count = 4 if item["role"] == "anchor" else 9                     # anchors 20 each, coin flips 45 each
            mapping[item["id"]] = [f"R{n}" for n in range(at, at + count)]
            at += count
        budget["rubric_rows"] = mapping
        result = run(budget, basis, rubric=rubric)
        summary = result["budget"]
        self.assertEqual((summary["weight_source"], summary["total_weight"]), ("rubric_rows", 300.0))
        self.assertEqual(statuses(result)["budget.rows"], "PASS", db.render_text(result))
        self.assertIn("09_Rubrics.json through rubric_rows", detail(result, "budget.rows"))
        self.assertAlmostEqual(summary["anchors"]["share"], 40 / 300)
        self.assertAlmostEqual(summary["variance"]["share"], 180 / 300)
        self.assertEqual(next(u for u in summary["units"] if u["id"] == "V1")["weight"], 45.0)

        budget["rubric_rows"]["V1"] = ["R59", "R99"]
        unknown = run(budget, basis, rubric=rubric)
        self.assertEqual(statuses(unknown)["budget.rows"], "FAIL")
        self.assertIn("not in 09_Rubrics.json: R99", detail(unknown, "budget.rows"))
        del budget["rubric_rows"]["V1"]
        absent = run(budget, basis, rubric=rubric)
        self.assertIn("unit V1 has no rubric_rows entry", detail(absent, "budget.rows"))
        self.assertEqual(statuses(absent)["budget.unit_rows"], "FAIL")

        budget["rubric_rows"] = mapping                                     # no rubric file yet: surface weights
        waiting = run(budget, basis, rubric={"error": "09_Rubrics.json not found"})
        self.assertEqual(statuses(waiting)["budget.rows"], "WARN")
        self.assertEqual(waiting["budget"]["weight_source"], "surface")

    def test_rubric_rows_override_reads_the_rubric_file(self):
        with selftest_sandbox.scratch_tmp("difficulty_budget_test_") as tmp:
            budget = db.good_budget()
            budget["rubric_rows"] = {item["id"]: [f"R{6 * n + k}" for k in range(1, 4)]
                                     for n, item in enumerate(budget["units"])}
            task = db._fixture(tmp, budget)
            (task / db.RUBRIC_NAME).write_text("", encoding="utf-8")       # the empty template slot
            empty = db.evaluate(task, policy=QUICK)
            self.assertEqual(empty["budget"]["weight_source"], "surface")
            self.assertEqual(statuses(empty)["budget.rows"], "WARN")
            (task / db.RUBRIC_NAME).write_text(json.dumps(
                [{"title": f"Criterion {n}", "weight": 5, "category": "outcome"} for n in range(1, 41)]),
                encoding="utf-8")
            result = db.evaluate(task, policy=QUICK)
            self.assertEqual(result["budget"]["weight_source"], "rubric_rows")
            self.assertEqual(result["budget"]["total_weight"], 200.0)
            self.assertEqual(sorted(result["bound_to"]), ["09_Rubrics.json", "Working_Files/01_Difficulty_Budget.json",
                                                          "Working_Files/01_Gradable_Surface.json"])


class OutputTests(unittest.TestCase):
    def test_same_input_gives_the_same_output(self):
        with selftest_sandbox.scratch_tmp("difficulty_budget_test_") as tmp:
            task = db._fixture(tmp)
            first, second = db.evaluate(task), db.evaluate(task)
            self.assertEqual(first, second)
            self.assertEqual(json.dumps(first, sort_keys=True), json.dumps(second, sort_keys=True))
            outputs = []
            for _ in range(2):
                with contextlib.redirect_stdout(io.StringIO()) as out:
                    self.assertEqual(db.main(["check", "--task-dir", str(task), "--json"]), 0)
                outputs.append(out.getvalue())
            self.assertEqual(outputs[0], outputs[1])

    def test_json_object_and_bound_files(self):
        with selftest_sandbox.scratch_tmp("difficulty_budget_test_") as tmp:
            task = db._fixture(tmp)
            before = sorted((str(p), p.stat().st_mtime_ns) for p in task.rglob("*"))
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(db.main(["check", "--task-dir", str(task), "--json"]), 0)
            self.assertEqual(sorted((str(p), p.stat().st_mtime_ns) for p in task.rglob("*")), before)   # read only
            result = json.loads(out.getvalue())
            self.assertEqual((result["tool"], result["version"], result["verdict"]), ("difficulty_budget", 1, "PASS"))
            self.assertEqual([check["id"] for check in result["checks"]], list(db.CHECK_IDS))
            for check in result["checks"]:
                self.assertEqual(sorted(check), ["detail", "id", "status"])
                self.assertIn(check["status"], ("PASS", "FAIL", "WARN", "SKIP"))
            for name in ("Working_Files/01_Difficulty_Budget.json", "Working_Files/01_Gradable_Surface.json"):
                self.assertEqual(result["bound_to"][name], hashlib.sha256((task / name).read_bytes()).hexdigest())

    def test_text_output_and_exit_codes(self):
        with selftest_sandbox.scratch_tmp("difficulty_budget_test_") as tmp:
            task = db._fixture(tmp)
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(db.main(["check", "--task-dir", str(task)]), 0)
            lines = out.getvalue().splitlines()
            self.assertEqual(lines[0], "DIFFICULTY BUDGET (easy): PASS")
            self.assertEqual(len(lines), 1 + len(db.CHECK_IDS))
            for line, cid in zip(lines[1:], db.CHECK_IDS):
                self.assertRegex(line, r"^\[(PASS|FAIL|WARN|SKIP)\] " + cid.replace(".", r"\.") + ": ")
            budget = db.good_budget()
            by_id(budget, "V2")["carrier"] = "other:a pinned post"
            (task / "Working_Files" / db.BUDGET_NAME).write_text(json.dumps(budget), encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(db.main(["check", "--task-dir", str(task)]), 0)        # WARN exits 0
            self.assertTrue(out.getvalue().startswith("DIFFICULTY BUDGET (easy): WARN\n"))
            by_id(budget, "V2")["carrier"] = "decoy"
            other = Path(tmp) / "other_budget.json"
            other.write_text(json.dumps(budget), encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(db.main(["check", "--task-dir", str(task), "--budget", str(other)]), 1)
            self.assertTrue(out.getvalue().startswith("DIFFICULTY BUDGET (easy): FAIL\n"))
            for argv in (["check", "--task-dir", str(task / "missing")], ["check"], [], ["derive"]):
                with self.assertRaises(SystemExit) as raised, contextlib.redirect_stderr(io.StringIO()):
                    db.main(argv)
                self.assertEqual(raised.exception.code, 2, argv)

    def test_table(self):
        with selftest_sandbox.scratch_tmp("difficulty_budget_test_") as tmp:
            budget = db.good_budget()
            budget["units"].append({"id": "J1", "role": "realism", "carrier": "decoy"})
            task = db._fixture(tmp, budget)
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(db.main(["table", "--task-dir", str(task)]), 0)
            lines = out.getvalue().splitlines()
            self.assertEqual(lines[0], "| Unit | Role | Carrier | Decider | Habit | Find rate | Rows (weight) | "
                                       "Weight share |")
            self.assertEqual(lines[2], "| A1 | anchor | reply_under_unrelated_parent | slack rec-A1 (injected) | "
                                       "slack / thread_replies | 0.00-0.15 | A1a (5), A1b (3) | 8.0% (8 of 100) |")
            self.assertIn("| V1 | variance | de_named_correction_reply |", lines[4])
            self.assertIn("| J1 | realism | decoy | n/a | n/a | n/a | not counted | 0% (realism) |", lines)
            self.assertIn("Anchors: 16.0% of weight from 2 cause(s)", lines[-1])
            self.assertIn("Coin-flip units: 60.0% of weight over 4 independent habit(s)", lines[-1])

    def test_template_prints_and_never_writes(self):
        with selftest_sandbox.scratch_tmp("difficulty_budget_test_") as tmp:
            task = db._fixture(tmp)
            work = task / "Working_Files"
            (work / db.BUDGET_NAME).unlink()
            draft = {"assignment_context": {"difficulty_mode": "medium"}, "mechanism_portfolio": [
                {"id": "RET", "decides": ["A1a", "A1b", "gone"]}, {"id": "OFF", "decides": ["V1a", "V1b", "V1c"]}]}
            (work / "01_Hardness_Manifest.draft.json").write_text(json.dumps(draft), encoding="utf-8")
            before = sorted(str(p) for p in task.rglob("*"))
            with contextlib.redirect_stdout(io.StringIO()) as out, contextlib.redirect_stderr(io.StringIO()) as err:
                self.assertEqual(db.main(["template", "--task-dir", str(task)]), 0)
            self.assertEqual(sorted(str(p) for p in task.rglob("*")), before)
            starter = json.loads(out.getvalue())
            self.assertEqual((starter["schema"], starter["mode"], starter["weight_basis"], starter["total_weight"]),
                             (db.SCHEMA, "medium", "surface", 100))
            self.assertEqual([(u["id"], u["mechanism"]) for u in starter["units"]], [("U1", "RET"), ("U2", "OFF")])
            self.assertEqual(starter["units"][0]["rows"], [{"id": "A1a", "weight": 5}, {"id": "A1b", "weight": 3}])
            first = starter["units"][0]
            self.assertEqual((first["role"], first["carrier"], first["find_rate"], first["habit"]),
                             ("", "", [], {"service": "", "action": ""}))
            self.assertEqual(first["decider"]["record_id"], "")
            self.assertIn("gone", err.getvalue())
            self.assertTrue(db.schema_problems(starter))                    # unusable until the author fills it
            # the final manifest wins over the draft once it exists
            (work / "01_Hardness_Manifest.json").write_text(json.dumps(
                {"mechanism_portfolio": [{"id": "ONLY", "decides": ["V2a"]}]}), encoding="utf-8")
            self.assertEqual([u["mechanism"] for u in db.template(task)[0]["units"]], ["ONLY"])
            (work / "01_Hardness_Manifest.json").unlink()
            (work / "01_Hardness_Manifest.draft.json").unlink()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()) as err:
                self.assertEqual(db.main(["template", "--task-dir", str(task)]), 1)
            self.assertIn("mechanism portfolio", err.getvalue())


def matrix(failed_by_run, rubrics=12, weight=5, **top):
    """A baseline matrix: failed_by_run is one collection of failed rubric numbers per run (None = errored run)."""
    ids = [f"R{n}" for n in range(1, rubrics + 1)]
    rollouts = []
    for number, failed in enumerate(failed_by_run, 1):
        if failed is None:
            rollouts.append({"id": f"run-{number}", "status": "errored"})
        else:
            rollouts.append({"id": f"run-{number}", "status": "completed", "tool_calls": 150,
                             "results": {rid: int(rid[1:]) not in failed for rid in ids}})
    return dict({"task_type": "long-horizon", "rubrics": [{"id": rid, "weight": weight} for rid in ids],
                 "rollouts": rollouts}, **top)


class DeriveTests(unittest.TestCase):
    def test_units_from_a_small_matrix(self):
        # R1, R2 fail every run; R3, R4 fail in runs 1, 3, 5; R5 fails in run 1 only; the rest always pass
        data = matrix([{1, 2, 3, 4, 5}, {1, 2}, {1, 2, 3, 4}, {1, 2}, {1, 2, 3, 4}, {1, 2}], difficulty_mode="easy")
        budget = db.derive(data, source="12_difficulty_input.json")
        self.assertEqual(db.schema_problems(budget), [])
        self.assertEqual((budget["mode"], budget["weight_basis"], budget["total_weight"]), ("easy", "rubric", 60))
        self.assertEqual(budget["undesigned_loss"], [0.0, 0.0])
        got = [(u["id"], u["role"], u["find_rate"], [row["id"] for row in u["rows"]]) for u in budget["units"]]
        self.assertEqual(got, [("U1", "anchor", [0.0, 0.0], ["R1", "R2"]),
                               ("U2", "variance", [0.35, 0.65], ["R3", "R4"]),
                               ("U3", "variance", [0.6833, 0.9833], ["R5"])])
        self.assertEqual({u["carrier"] for u in budget["units"]}, {"other:derived"})
        self.assertEqual(len({db.habit_key(u["habit"]) for u in budget["units"]}), 3)      # one habit per unit
        self.assertEqual(budget["units"][2]["observed_passes"], 5)

    def test_range_is_clipped_and_errored_runs_are_left_out(self):
        data = matrix([{1}, {1}, {1}, {1}, set(), None], difficulty_mode="medium")        # R1 passed in 1 of 5
        budget = db.derive(data)
        self.assertEqual(budget["derived_from"]["completed_runs"], 5)
        self.assertEqual(budget["derived_from"]["errored_runs"], 1)
        self.assertEqual(budget["units"][0]["find_rate"], [0.05, 0.35])
        clipped = db.derive(matrix([{1}, set(), set(), set(), set(), set(), set(), set(), set(), set()]), mode="easy")
        self.assertEqual(clipped["units"][0]["find_rate"], [0.75, 1.0])

    def test_invalid_rubrics_and_judge_corrections_follow_the_scored_view(self):
        data = matrix([{1, 2, 6}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}], difficulty_mode="easy")
        data["rubrics"][1]["valid"] = False                                 # R2 is not scored
        data["rollouts"][0]["judge_corrections"] = {"R6": True}             # R6 was a judge error
        budget = db.derive(data)
        self.assertEqual([[row["id"] for row in u["rows"]] for u in budget["units"]], [["R1"]])
        self.assertEqual(budget["total_weight"], 55)

    def test_derive_needs_a_mode_and_completed_runs(self):
        with self.assertRaises(ValueError):
            db.derive({"rubrics": [{"id": "R1", "weight": 5}], "rollouts": [{"id": "run-1", "status": "errored"}]})
        legacy = matrix([{1, 2}, {1}, {2}, {1}, {2}, set()])                # no difficulty_mode in the file
        self.assertIn("mode must be", " ".join(db.schema_problems(db.derive(legacy))))
        self.assertEqual(db.schema_problems(db.derive(legacy, mode="medium")), [])

    def test_derive_command(self):
        with selftest_sandbox.scratch_tmp("difficulty_budget_test_") as tmp:
            path = Path(tmp) / "12_difficulty_input.json"
            path.write_text(json.dumps(matrix([{1, 2, 3}, {1, 2}, {1, 2, 3}, {1, 2}, {1, 2, 3}, {1, 2}],
                                              difficulty_mode="easy")), encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(db.main(["derive", "--input", str(path)]), 0)
            budget = json.loads(out.getvalue())
            self.assertEqual([u["role"] for u in budget["units"]], ["anchor", "variance"])
            self.assertEqual(budget["derived_from"]["source"], "12_difficulty_input.json")
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(db.main(["derive", "--input", str(path), "--check"]), 1)
            self.assertTrue(out.getvalue().startswith("DIFFICULTY BUDGET (easy): FAIL\n"))
            self.assertEqual(sorted(p.name for p in Path(tmp).iterdir()), ["12_difficulty_input.json"])


class BacktestTests(unittest.TestCase):
    def archive(self, tmp) -> Path:
        root = Path(tmp) / "archives"
        # task_a: a V2 matrix (no spec_version); the mode comes from 00_Assigments.md. Passes all four real gates.
        work = root / "task_a" / "task_inputs" / "Working_Files"
        (work / "run_forensics" / "rev1").mkdir(parents=True)
        (root / "task_a" / "task_inputs" / "00_Assigments.md").write_text("difficulty_mode:    medium\n")
        legacy = matrix([{1, 2, 3, 4, 5, 6}, {1, 2}, {3, 4, 5, 6, 7, 8}, {1, 2, 7, 8}, {9, 10}, set()], rubrics=20)
        (work / "12_difficulty_input.json").write_text(json.dumps(legacy))
        (work / "run_forensics" / "rev1" / "matrix.json").write_text(json.dumps(legacy))            # a copy
        (work / "run_forensics" / "rev1" / "precheck.matrix.json").write_text(json.dumps(
            dict(matrix([{1, 2}], rubrics=20), spec_version="V3", difficulty_mode="medium")))        # one run
        (work / "notes.json").write_text(json.dumps({"rubrics": "see file", "rollouts": 6}))
        # task_b: a V3 matrix where every run fails the same rows: signature and spread miss.
        work = root / "task_b" / "task_inputs" / "Working_Files"
        work.mkdir(parents=True)
        (work / "12_difficulty_input.json").write_text(json.dumps(
            matrix([{1, 2, 3}] * 6, rubrics=20, spec_version="V3", difficulty_mode="easy")))
        return root

    def test_backtest_on_a_small_archive(self):
        with selftest_sandbox.scratch_tmp("difficulty_budget_test_") as tmp:
            root = self.archive(tmp)
            report = db.backtest(root, policy=QUICK)
            rows = {row["task"]: row for row in report["baselines"]}
            self.assertEqual(sorted(rows), ["task_a", "task_b"])
            self.assertEqual((rows["task_a"]["mode"], rows["task_a"]["kind"]), ("medium", "final"))
            self.assertIn("V2 matrix", rows["task_a"]["rules"])
            self.assertTrue(rows["task_a"]["all_real_pass"], rows["task_a"]["real"])
            self.assertEqual({k: v["pass"] for k, v in rows["task_b"]["real"].items()},
                             {"average": True, "full_passes": True, "signature": False, "spread": False})
            self.assertEqual(rows["task_b"]["budget"]["budget.signature"], "FAIL")
            self.assertEqual(rows["task_b"]["budget"]["budget.spread"], "WARN")
            self.assertTrue(rows["task_b"]["agree"]["budget.signature"] and rows["task_b"]["agree"]["budget.spread"])
            self.assertEqual(rows["task_b"]["units"], {"anchor": 1, "variance": 0, "variance_in_window": 0,
                                                       "variance_by_runs_passed": {}})
            self.assertEqual(rows["task_b"]["runs_losing_mode_loss"], 6)
            self.assertEqual(set(rows["task_a"]["budget"]), set(db.BACKTEST_CHECKS))
            reasons = {Path(item["baseline"]).name: item["reason"] for item in report["skipped"]}
            self.assertIn("same matrix as", reasons["matrix.json"])
            self.assertIn("not a scorable six-run baseline", reasons["precheck.matrix.json"])
            summary = report["summary"]
            self.assertEqual((summary["baselines"], summary["real_all_pass"], summary["real_miss"]), (2, 1, 1))
            self.assertEqual(summary["per_check"]["budget.signature"]["not_pass_on_real_miss"], 1)
            self.assertEqual(report["summary_one_per_task"]["baselines"], 2)
            text = db.render_backtest(report)
            self.assertTrue(text.startswith("DIFFICULTY BUDGET BACKTEST (2 baselines): "))
            self.assertIn("calibration test of the thresholds", text)
            self.assertIn("not proof that a budget written at design time predicts the outcome", text)
            self.assertEqual(db.backtest(root, policy=QUICK), report)       # deterministic

    def test_backtest_command(self):
        with selftest_sandbox.scratch_tmp("difficulty_budget_test_") as tmp:
            root = self.archive(tmp)
            before = sorted(str(p) for p in root.rglob("*"))
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(db.main(["backtest", "--archives", str(root), "--json"]), 0)
            report = json.loads(out.getvalue())
            self.assertEqual((report["tool"], report["command"], len(report["baselines"])),
                             ("difficulty_budget", "backtest", 2))
            self.assertIn("calibration test", report["note"])
            self.assertEqual(sorted(str(p) for p in root.rglob("*")), before)
            empty = Path(tmp) / "empty"
            empty.mkdir()
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(db.main(["backtest", "--archives", str(empty)]), 1)      # nothing to calibrate on


class SimulationTests(unittest.TestCase):
    """The plan's section 2a figures, and the gate rules against difficulty_stats."""

    @staticmethod
    def flips(count, rate, always_missed_anchor=True, share=15):
        units = []
        if always_missed_anchor:
            units.append({"habit": ("s", "anchor"), "lo": 0.0, "hi": 0.0, "rows": {"A1": 5, "A2": 5}})
        units += [{"habit": ("s", f"v{n}"), "lo": rate, "hi": rate, "rows": {f"V{n}a": share, f"V{n}b": share}}
                  for n in range(count)]
        return db.simulate(units, 200, Fraction(9, 10))["lo"]

    def test_signature_gate_probabilities_match_the_plan(self):
        # plan 2a (find rates 0.35-0.65): six runs 0.98-1.00 / 0.93-0.98 / 0.73-0.85 for four / three / two units;
        # five runs 0.92-0.97 / 0.78-0.87 / 0.46-0.59. Tolerance: 0.01 around each range.
        wanted = {4: ((0.97, 1.0), (0.91, 0.98)), 3: ((0.92, 0.99), (0.77, 0.88)), 2: ((0.72, 0.86), (0.45, 0.60))}
        for count, (six, five) in wanted.items():
            for rate in (0.35, 0.5, 0.65):
                got = self.flips(count, rate)
                with self.subTest(units=count, rate=rate):
                    self.assertTrue(six[0] <= got["signature"] <= six[1], got)
                    self.assertTrue(five[0] <= got["signature_one_error"] <= five[1], got)
        mid = {count: self.flips(count, 0.5) for count in (4, 3, 2)}       # the top of each range is at 0.5
        self.assertAlmostEqual(mid[4]["signature"], 0.997, delta=0.006)
        self.assertAlmostEqual(mid[3]["signature"], 0.976, delta=0.008)
        self.assertAlmostEqual(mid[2]["signature"], 0.850, delta=0.012)
        self.assertAlmostEqual(mid[2]["signature_one_error"], 600 / 1024, delta=0.012)     # exact: 600 of 4^5

    def test_plan_figures_assume_every_run_fails(self):
        # Without an always-missed anchor a run that finds every unit is a full pass, not a failing run, and two
        # coin flips pass the signature gate about half the time instead of 0.73-0.85.
        bare = self.flips(2, 0.5, always_missed_anchor=False)
        self.assertTrue(0.46 <= bare["signature"] <= 0.55, bare)
        self.assertLess(self.flips(4, 0.65, always_missed_anchor=False)["signature"],
                        self.flips(4, 0.65)["signature"])

    def test_spread_probabilities_match_the_plan(self):
        for rate in (0.35, 0.5, 0.65):                                      # plan 2a: 15 + 15 + 15 gives 0.69-0.74
            got = self.flips(3, rate, share=15)["spread"]
            self.assertTrue(0.68 <= got <= 0.75, (rate, got))
        self.assertTrue(0.25 <= self.flips(3, 0.5, share=12)["spread"] <= 0.35)            # 12 + 12 + 12: 0.26-0.34
        self.assertTrue(0.79 <= self.flips(4, 0.5, share=15)["spread"] <= 0.85)            # four at 15: 0.80-0.84

    def test_gate_rules_match_difficulty_stats(self):
        rng = random.Random(11)
        pool = [f"R{n}" for n in range(1, 15)]
        cap = stats.DIFFICULTY_CAPS["easy"]
        seen = {"signature": set(), "spread": set(), "average": set(), "full": set()}
        for case in range(150):
            weights = {rid: rng.choice((1, 3, 5)) for rid in pool}
            units = [{"habit": ("s", f"h{n}"), "lo": 0.5, "hi": 0.5,
                      "rows": {rid: weights[rid] for rid in rng.sample(pool[:10], rng.randint(1, 3))}}
                     for n in range(rng.randint(1, 6))]
            model = db._Model(units, sum(weights.values()))
            miss = rng.choice((0.05, 0.3, 0.6, 0.95))
            masks = []
            for _ in range(6):
                mask = 0
                for index in range(len(units)):
                    if rng.random() < miss:
                        mask |= model.unit_mask[index]
                masks.append(mask)
            data = {"spec_version": "V3", "difficulty_mode": "easy", "task_type": "long-horizon",
                    "rubrics": [{"id": rid, "weight": weights[rid]} for rid in pool],
                    "rollouts": [{"id": f"run-{n}", "status": "completed", "tool_calls": 150,
                                  "results": {rid: rid not in model.rows_of(mask) for rid in pool}}
                                 for n, mask in enumerate(masks, 1)]}
            real = stats.compute(copy.deepcopy(data))
            gates = real["gates"]
            failed = [model.failed_weight(mask) for mask in masks]
            mine = {"signature": model.signature_passes(masks), "spread": model.in_band(failed),
                    "average": sum(failed) >= model.min_failed_sum(6, cap, 0),
                    "full": masks.count(0) < stats.FULL_PASS_FAILURE_COUNT}
            theirs = {"signature": gates["failure_patterns"]["verdict"].startswith("PASS"),
                      "spread": gates["per_rollout_sd"]["verdict"].startswith("PASS"),
                      "average": gates["avg_weighted_pass_rate"]["verdict"].startswith("PASS"),
                      "full": gates["pass_at_1"]["verdict"].startswith("PASS")}
            self.assertEqual(mine, theirs, (case, real["per_rollout"]))
            self.assertAlmostEqual(model.sd(failed), statistics.pstdev(
                [run["weighted_pass_rate"] for run in real["per_rollout"]]), places=12)
            data["rollouts"][5] = {"id": "run-6", "status": "errored"}      # one errored run: five completed
            five = stats.compute(copy.deepcopy(data))["gates"]["failure_patterns"]["verdict"].startswith("PASS")
            self.assertEqual(model.signature_passes(masks[:5]), five, case)
            for key, value in mine.items():
                seen[key].add(value)
        self.assertEqual({key: len(values) for key, values in seen.items()},
                         {"signature": 2, "spread": 2, "average": 2, "full": 2})         # both outcomes were covered

    def test_band_edges_and_cap_equality(self):
        # ten rows of weight 1; runs pass 4 and 6 rows alternately: SD exactly 0.100; 2 and 8: exactly 0.300
        for low, high, inside in ((4, 6, True), (2, 8, True), (1, 9, False), (5, 5, False)):
            always = {f"D{n}": 1 for n in range(10 - high)}
            sometimes = {f"D{n}": 1 for n in range(10 - high, 10 - low)}
            units = [{"habit": ("s", "a"), "lo": 0, "hi": 0, "rows": always},
                     {"habit": ("s", "b"), "lo": 0.5, "hi": 0.5, "rows": sometimes}]
            model = db._Model(units, 10)
            failed = [model.failed_weight(model.unit_mask[0] | (model.unit_mask[1] if n % 2 else 0)) for n in range(6)]
            self.assertEqual(model.in_band(failed), inside, (low, high, model.sd(failed)))
        model = db._Model([{"habit": ("s", "a"), "lo": 0, "hi": 0, "rows": {"D0": 1}}], 10)
        self.assertEqual(model.min_failed_sum(6, Fraction(9, 10), 0), 7)    # 6 failed of 60 is exactly 90%: not under
        self.assertEqual(model.min_failed_sum(6, Fraction(9, 10), Fraction(1, 20)), 4)     # 5% lost elsewhere
        self.assertEqual(db._Model([], 10).sd([3]), 0.0)

    def test_always_found_and_always_missed_units(self):
        units = [{"habit": ("s", "found"), "lo": 1.0, "hi": 1.0, "rows": {"F1": 5, "F2": 5}},
                 {"habit": ("s", "missed"), "lo": 0.0, "hi": 0.0, "rows": {"M1": 5, "M2": 5}}]
        sim = db.simulate(units, 100, Fraction(9, 10), policy=QUICK)
        self.assertEqual(sim["groups_drawn"], 0)
        for end in ("lo", "mid", "hi"):
            self.assertEqual((sim[end]["average"], sim[end]["full_passes"], sim[end]["signature"],
                              sim[end]["spread"]), (0.0, 1.0, 0.0, 0.0))    # every run loses exactly 10%: one signature

    def test_ten_unit_budget_is_fast(self):
        import time
        units = [anchor("A1"), anchor("A2")] + [coin(f"V{n}", rows=2) for n in range(1, 9)]
        budget, basis = budget_of(units, 140)
        started = time.perf_counter()
        result = run(budget, basis, policy=None)
        self.assertLess(time.perf_counter() - started, 5.0)
        self.assertEqual(result["budget"]["simulation"]["habit_groups"], 10)


class ArchiveTests(unittest.TestCase):
    """The stored baselines, when the archive is on this machine (skipped otherwise)."""

    def test_archived_baseline_derives_and_checks(self):
        path = (db.ARCHIVES / "frederick_bridge_pipeline_2026-11-03" / "task_inputs" / "Working_Files"
                / "12_difficulty_input.json")
        if not path.is_file():
            self.skipTest("archive not present")
        data = json.loads(path.read_text(encoding="utf-8"))
        gates, rates = db.real_gates(data, data["difficulty_mode"])
        self.assertEqual(len(rates), 6)
        self.assertTrue(all(gate["pass"] for gate in gates.values()), gates)
        result = db.check_derived(data, policy=QUICK)
        self.assertEqual(statuses(result)["budget.rows"], "PASS")
        self.assertEqual(statuses(result)["budget.context"], "SKIP")


if __name__ == "__main__":
    unittest.main()

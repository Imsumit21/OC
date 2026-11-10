"""Tests for rubric_skeleton.py. Run: cd Task_Authoring/tools && python3.12 -B -m unittest test_rubric_skeleton"""
from __future__ import annotations

import ast
import contextlib
import io
import json
import unittest
from pathlib import Path
from unittest import mock

import rubric_skeleton as rs
import selftest_sandbox

HERE = Path(__file__).resolve().parent
WF = "Working_Files"


def _edit(path: Path, change) -> None:
    data = json.loads(path.read_text())
    change(data)
    path.write_text(json.dumps(data, indent=1) + "\n")


def _slot(sid, selector, role="core", weight=1, kind="lookup", **more):
    return dict({"id": sid, "title": sid, "weight": weight, "work_kind": kind, "work_reason": "test",
                 "class": "write_content", "selector": selector, "role": role}, **more)


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("test_rubric_skeleton_")
        self.root = Path(self._tmp.name)
        self.policy = rs.load_policy()

    def tearDown(self):
        self._tmp.cleanup()

    def task(self, name="task", **kw) -> Path:
        td = self.root / name
        rs._fixture(td, **kw)
        return td

    def run_main(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = rs.main(list(argv))
        return code, out.getvalue(), err.getvalue()


class BuildTests(Base):
    def test_self_test_passes(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            rs._self_test()
        self.assertIn("self-test: ok", out.getvalue())

    def test_one_row_per_separate_write_target(self):
        doc = rs.build(self.task(closes=9))
        writes = {w["tool"]: w for w in doc["writes"]}
        self.assertEqual(len(writes["linear_update_issue"]["added_rows"]), 9)
        self.assertFalse(writes["linear_update_issue"]["template"])
        # sheet cells keep the table spot-check rule; a single write is proven by its content rows
        self.assertEqual(writes["gsheets_create_spreadsheet+gsheets_values_update"]["kind"], "artifact")
        self.assertEqual(writes["slack_send_message"]["added_rows"], [])
        # two of the four comments are already named by slots C1 and C2
        self.assertEqual(writes["linear_create_comment"]["targets_named_by_slots"], 2)
        self.assertEqual(len(writes["linear_create_comment"]["added_rows"]), 2)

    def test_rows_carry_the_required_fields_and_no_wording(self):
        doc = rs.build(self.task())
        self.assertEqual(doc["schema"], "rubric-skeleton-v1")
        self.assertEqual([r["id"] for r in doc["rows"]], [f"S{i}" for i in range(1, len(doc["rows"]) + 1)])
        for r in doc["rows"]:
            self.assertTrue({"id", "slot", "kind", "weight", "units"} <= set(r), r)
            self.assertIn(r["weight"], (1, 3, 5))
            self.assertNotIn("title", r)
            self.assertNotIn("criterion", r)
        added = [r for r in doc["rows"] if r["slot"] is None]
        self.assertTrue(all("write_target" in r for r in added))
        t = doc["totals"]
        self.assertEqual(t["total_weight"], sum(r["weight"] for r in doc["rows"]))
        self.assertEqual(t["always_pass_weight"], sum(r["weight"] for r in doc["rows"] if not r["units"]))
        self.assertAlmostEqual(sum(u["share"] for u in t["per_unit"].values()),
                               sum(u["weight"] for u in t["per_unit"].values()) / t["total_weight"], places=3)

    def test_weights_follow_the_work_kind_band(self):
        td = self.task()
        _edit(td / WF / rs.SURFACE, lambda s: s["slots"][0].update(weight=1))   # X1 says 1, its kind is band 5
        r = rs.cmd_build(td)
        row = [x for x in r["skeleton"]["rows"] if x["slot"] == "X1"][0]
        self.assertEqual(row["weight"], 5)
        self.assertEqual(r["verdict"], "WARN")
        self.assertTrue(any(c["id"] == "skeleton.notes" and "X1" in c["detail"] for c in r["checks"]))

    def test_units_come_from_mechanisms_and_budget_rows(self):
        td = self.task()
        doc = rs.build(td)
        rows = {r["slot"]: r for r in doc["rows"] if r["source"] == "slot"}
        self.assertEqual(rows["X1"]["units"], ["U1"])            # mechanism RET
        self.assertEqual(rows["R1"]["units"], ["U1", "U2"])      # mechanisms RET and OFF
        self.assertEqual(rows["D1"]["units"], [])                # only the realism unit names D1
        # a budget row on the surface basis adds a unit to a slot no mechanism names
        _edit(td / WF / rs.BUDGET, lambda b: b["units"][2]["rows"].append({"id": "D1", "weight": 1}))
        rows = {r["slot"]: r for r in rs.build(td)["rows"] if r["source"] == "slot"}
        self.assertEqual(rows["D1"]["units"], ["U3"])

    def test_no_budget_builds_and_reports_mechanism_free_weight(self):
        td = self.task()
        (td / WF / rs.BUDGET).unlink()
        r = rs.cmd_build(td)
        self.assertEqual(r["verdict"], "WARN")
        t = r["skeleton"]["totals"]
        self.assertEqual(t["per_unit"], {})
        self.assertIn("no budget", t["always_pass_basis"])
        self.assertEqual(t["always_pass_weight"], sum(x["weight"] for x in r["skeleton"]["rows"]
                                                      if not x.get("mechanisms")))
        self.assertNotIn(f"{WF}/{rs.BUDGET}", r["bound_to"])

    def test_draft_manifest_is_read_when_the_final_is_absent(self):
        td = self.task()
        (td / WF / rs.MANIFEST).rename(td / WF / rs.MANIFEST_DRAFT)
        doc = rs.build(td)
        self.assertEqual(doc["inputs"]["manifest"], f"{WF}/{rs.MANIFEST_DRAFT}")
        self.assertIn(f"{WF}/{rs.MANIFEST_DRAFT}", doc["bound_to"])


class TemplateAndAtomTests(Base):
    def test_identical_masked_selectors_with_a_literal_are_one_template(self):
        doc = rs.build(self.task(closes=40, template=True))
        w = {x["tool"]: x for x in doc["writes"]}["linear_update_issue"]
        self.assertTrue(w["template"])
        self.assertEqual(w["added_rows"], [])                    # three samples and the volume slot stand
        self.assertIn("sample group moves", w["template_basis"])

    def test_samples_without_a_literal_value_are_not_a_template(self):
        td = self.task(closes=12)

        def change(s):
            s["deliverables"]["moves"] = {"kind": "json_text", "tool": "linear_update_issue"}
            s["slots"] += [_slot(f"L{i}", ["link", "moves"], "sample", group="st") for i in (1, 2, 3)]
            s["slots"].append(_slot("LV", ["link", "moves"], "volume", volume_for=["st"]))
        _edit(td / WF / rs.SURFACE, change)
        w = {x["tool"]: x for x in rs.build(td)["writes"]}["linear_update_issue"]
        self.assertFalse(w["template"])
        self.assertEqual(len(w["added_rows"]), 12 - 3)           # each sample slot stands for one target

    def test_samples_with_different_content_are_not_a_template(self):
        td = self.task(closes=12)

        def change(s):
            s["slots"] += [_slot("M1", ["text", "moves", "(ENG-1)[ -~]{0,80}Done"], "sample", group="moves"),
                           _slot("M2", ["text", "moves", "(ENG-2)[ -~]{0,80}Canceled"], "sample", group="moves"),
                           _slot("MV", ["text", "reply", r"\b12\b"], "volume", volume_for=["moves"])]
        _edit(td / WF / rs.SURFACE, change)
        w = {x["tool"]: x for x in rs.build(td)["writes"]}["linear_update_issue"]
        self.assertFalse(w["template"])
        self.assertEqual(len(w["added_rows"]), 10)

    def test_declared_template_without_slots_gets_samples_and_a_volume_row(self):
        td = self.task(closes=30)
        _edit(td / WF / rs.MANIFEST, lambda m: m["writes"][2].update(template=True))
        doc = rs.build(td)
        w = {x["tool"]: x for x in doc["writes"]}["linear_update_issue"]
        self.assertTrue(w["template"])
        self.assertEqual(len(w["added_rows"]), rs.SAMPLE_CAP + 1)
        self.assertEqual({r["weight"] for r in doc["rows"] if r["id"] in w["added_rows"]}, {1})

    def test_atomic_signals(self):
        surface = {"truth_fields": {"groups": "groups"}}
        truth = {"K-01": {"groups": ["late", "billing", "review"]}}
        self.assertEqual(rs.atoms({"selector": ["field", "K-01", "call"]}, truth, surface), (1, None))
        self.assertEqual(rs.atoms({"selector": ["field", "K-01", "call"], "atoms": 3}, truth, surface)[0], 3)
        self.assertEqual(rs.atoms({"selector": ["tracker_entry", "h", "K-01", ["a", "b"]]}, truth, surface)[0], 2)
        self.assertEqual(rs.atoms({"selector": ["groups_of", "K-01"]}, truth, surface)[0], 3)
        self.assertEqual(rs.atoms({"selector": ["groups_of", "K-01"]}, None, surface)[0], 1)
        two = r"(?:^|\n)(?=[ -~]*layer)(?=[ -~]*(export|save))[ -~]*?(mar|feb)"
        self.assertEqual(rs.atoms({"selector": ["text", "plan", two]}, truth, surface)[0], 2)
        one = r"(domino|DD)[ -~]{0,160}[ $,]140\b"
        self.assertEqual(rs.atoms({"selector": ["text", "plan", one]}, truth, surface)[0], 1)
        self.assertEqual(rs.atoms({"selector": ["text", "plan", r"(?=.*a)x"]}, truth, surface)[0], 1)

    def test_tool_parts_and_aliases(self):
        self.assertEqual(rs.tool_parts("gsheets_create_spreadsheet + gsheets_values_update"),
                         ["gsheets_create_spreadsheet", "gsheets_values_update"])
        self.assertEqual(rs.tool_parts("slack_post_message (thread reply)"), ["slack_send_message"])
        self.assertEqual(rs.tool_parts("gmail_reply_to_message (report)"), ["gmail_reply_to_message"])
        self.assertEqual(rs.tool_parts(None), [])


class CheckTests(Base):
    def test_present_bound_share(self):
        td = self.task(closes=1)
        self.assertEqual(rs.cmd_check(td, self.policy)["checks"][0]["status"], "FAIL")     # no skeleton yet
        rs.cmd_build(td, write=True)
        r = rs.evaluate(td, "check", self.policy)
        self.assertEqual({c["id"]: c["status"] for c in r["checks"]},
                         {"skeleton.present": "PASS", "skeleton.bound": "PASS", "skeleton.share": "PASS"})
        self.assertEqual(set(r), {"tool", "version", "command", "verdict", "bound_to", "checks", "totals",
                                  "thresholds", "declared"})
        self.assertEqual(r["thresholds"]["required_anchor_share"], 0.12)

    def test_each_bound_input_makes_the_skeleton_stale(self):
        for name in (rs.SURFACE, rs.MANIFEST, rs.BUDGET, rs.TRUTH):
            with self.subTest(name=name):
                td = self.task("stale_" + name.replace("/", "_").replace(".", "_"), closes=1)
                rs.cmd_build(td, write=True)
                p = td / WF / name
                p.write_text(p.read_text() + "\n")
                st = {c["id"]: c for c in rs.cmd_check(td, self.policy)["checks"]}
                self.assertEqual(st["skeleton.bound"]["status"], "FAIL")
                self.assertIn(name, st["skeleton.bound"]["detail"])

    def test_added_write_rows_dilute_the_anchors(self):
        td = self.task(closes=60)                       # 30 of 225 can still be lost; the anchors carry 24
        rs.cmd_build(td, write=True)
        r = rs.cmd_check(td, self.policy)
        share = [c for c in r["checks"] if c["id"] == "skeleton.share"][0]
        self.assertEqual(share["status"], "FAIL")
        self.assertLess(r["totals"]["anchor_share"], r["thresholds"]["required_anchor_share"])
        self.assertIn("anchors carry less", share["detail"])

    def test_fail_when_too_little_weight_can_be_lost_at_all(self):
        td = self.task(closes=1)

        def strip(b):
            b["units"] = [u for u in b["units"] if u["id"] in ("U3", "U5")]     # one coin-flip unit of weight 3
        _edit(td / WF / rs.BUDGET, strip)
        rs.cmd_build(td, write=True)
        share = [c for c in rs.cmd_check(td, self.policy)["checks"] if c["id"] == "skeleton.share"][0]
        self.assertEqual(share["status"], "FAIL")
        self.assertIn("can be lost at all", share["detail"])

    def test_coin_flip_share_warns_five_points_under_the_design(self):
        td = self.task(closes=6)
        rs.cmd_build(td, write=True)
        r = rs.cmd_check(td, self.policy)
        self.assertEqual(r["verdict"], "WARN")
        self.assertGreater(r["declared"]["coin_flip_share"] - r["totals"]["coin_flip_share"], rs.SHARE_MOVE_WARN)

    def test_medium_mode_needs_more_anchor_weight(self):
        td = self.task(closes=6)                        # anchors 24 of 63 = 38%: fine for medium (17%)
        _edit(td / WF / rs.BUDGET, lambda b: b.update(mode="medium"))
        rs.cmd_build(td, write=True)
        self.assertEqual(rs.cmd_check(td, self.policy)["thresholds"]["required_anchor_share"], 0.17)
        _edit(td / WF / rs.BUDGET, lambda b: b.update(mode="nightmare"))
        rs.cmd_build(td, write=True)
        share = [c for c in rs.cmd_check(td, self.policy)["checks"] if c["id"] == "skeleton.share"][0]
        self.assertEqual(share["status"], "FAIL")

    def test_no_budget_skips_the_share_check(self):
        td = self.task(closes=1)
        (td / WF / rs.BUDGET).unlink()
        rs.cmd_build(td, write=True)
        st = {c["id"]: c["status"] for c in rs.cmd_check(td, self.policy)["checks"]}
        self.assertEqual(st["skeleton.share"], "SKIP")
        self.assertEqual(st["skeleton.bound"], "PASS")


class RebaseAndDriftTests(Base):
    def rubric(self, td, weights):
        (td / rs.RUBRIC).write_text(json.dumps([{"title": f"row {i}", "weight": w, "category": "Outcome",
                                                 "evidence": "e", "justification": "j"}
                                                for i, w in enumerate(weights, 1)]) + "\n")

    def mapped(self, td):
        _edit(td / WF / rs.BUDGET, lambda b: b.update(rubric_rows={
            "U1": ["R1", "R3", "R4", "R6"], "U2": ["R2", "R3", "R5", "R6"], "U3": ["R7"], "U4": ["R8"]}))
        rs.cmd_build(td, write=True)

    def test_rebase_prints_rows_on_the_skeleton_basis(self):
        td = self.task()
        rb = rs.rebase(td)
        self.assertEqual(rb["weight_basis"], "skeleton")
        doc = rs.build(td)
        self.assertEqual(rb["total_weight"], doc["totals"]["total_weight"])
        by_id = {r["id"]: r for r in doc["rows"]}
        for u in rb["units"]:
            for row in u["rows"]:
                self.assertEqual(by_id[row["id"]]["weight"], row["weight"])
        self.assertEqual([u["rows"] for u in rb["units"] if u["id"] == "U5"], [[]])    # realism carries no rows
        code, out, _ = self.run_main("rebase", "--task-dir", str(td))
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out), rb)
        self.assertFalse((td / WF / rs.SKELETON).exists())                             # print only

    def test_drift_pass_warn_fail(self):
        td = self.task()
        base = [5, 5, 5, 3, 3, 3, 3, 3] + [3] * 8 + [1] * 5
        self.rubric(td, base)
        self.mapped(td)
        r = rs.cmd_drift(td, self.policy)
        self.assertEqual(r["verdict"], "PASS", r["checks"])
        self.assertEqual(r["after"]["anchor_weight"], 24)
        self.assertIn(rs.RUBRIC, r["bound_to"])
        self.assertEqual(r["before_source"], "stored skeleton")
        self.rubric(td, base + [1] * 8)                 # always-pass grows
        r = rs.cmd_drift(td, self.policy)
        self.assertEqual(r["verdict"], "WARN")
        self.assertIn("always-pass share grew", r["checks"][0]["detail"])
        self.rubric(td, base + [3] * 70)                # anchors under the easy loss
        r = rs.cmd_drift(td, self.policy)
        self.assertEqual(r["verdict"], "FAIL")
        self.assertLess(r["after"]["anchor_share"], 0.10)
        code, out, _ = self.run_main("drift", "--task-dir", str(td))
        self.assertEqual(code, 1)
        self.assertTrue(out.startswith("RUBRIC SKELETON (drift): FAIL"))
        self.assertIn("always-pass", out)

    def test_drift_warns_when_a_unit_share_moves_five_points(self):
        td = self.task()
        self.rubric(td, [5, 5, 5, 3, 3, 3, 3, 3] + [3] * 8 + [1] * 5)
        self.mapped(td)
        _edit(td / WF / rs.BUDGET, lambda b: b["rubric_rows"].update(U3=["R7", "R9", "R10", "R11"]))
        rs.cmd_build(td, write=True)
        r = rs.cmd_drift(td, self.policy)
        self.assertEqual(r["verdict"], "WARN")
        self.assertIn("U3 +", r["checks"][0]["detail"])
        moved = [u for u in r["units"] if u["unit"] == "U3"][0]
        self.assertGreater(moved["moved"], rs.SHARE_MOVE_WARN)

    def test_drift_needs_rubric_rows_and_known_ids(self):
        td = self.task()
        rs.cmd_build(td, write=True)
        self.assertEqual(rs.cmd_drift(td, self.policy)["checks"][0]["status"], "SKIP")     # no rubric yet
        self.rubric(td, [5, 5, 3, 3])
        r = rs.cmd_drift(td, self.policy)
        self.assertEqual(r["verdict"], "FAIL")
        self.assertIn("rubric_rows", r["checks"][0]["detail"])
        _edit(td / WF / rs.BUDGET, lambda b: b.update(rubric_rows={"U1": ["R1"], "U2": ["R2"], "U3": ["R9"]}))
        r = rs.cmd_drift(td, self.policy)
        self.assertEqual(r["verdict"], "FAIL")
        self.assertIn("R9", r["checks"][0]["detail"])
        self.assertIn("U4 has no rubric_rows", r["checks"][0]["detail"])


class CliAndHygieneTests(Base):
    def test_exit_codes_and_json_shape(self):
        td = self.task(closes=1)
        code, out, _ = self.run_main("build", "--task-dir", str(td), "--write", "--json")
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertEqual(data["tool"], "rubric_skeleton")
        self.assertEqual(data["version"], 1)
        self.assertIn(data["verdict"], ("PASS", "WARN", "FAIL"))
        self.assertTrue(all(set(c) == {"id", "status", "detail"} for c in data["checks"]))
        self.assertTrue(all(len(v) == 64 for v in data["bound_to"].values()))
        stored = json.loads((td / WF / rs.SKELETON).read_text())
        self.assertEqual(stored, data["skeleton"])
        code, out, _ = self.run_main("check", "--task-dir", str(td))
        self.assertEqual(code, 0)
        self.assertTrue(out.splitlines()[0].startswith("RUBRIC SKELETON (check): PASS"))
        self.assertRegex(out.splitlines()[1], r"^\[(PASS|FAIL|WARN|SKIP)\] skeleton\.present: ")
        code, _, err = self.run_main("check", "--task-dir", str(self.root / "missing"))
        self.assertEqual(code, 2)
        self.assertIn("does not exist", err)
        self.assertEqual(self.run_main("build")[0], 2)
        self.assertEqual(self.run_main()[0], 2)
        bad = self.task("diluted", closes=70)
        self.run_main("build", "--task-dir", str(bad), "--write")
        self.assertEqual(self.run_main("check", "--task-dir", str(bad))[0], 1)

    def test_build_is_deterministic(self):
        td = self.task()
        self.assertEqual(rs.dump(rs.build(td)), rs.dump(rs.build(td)))
        self.assertNotRegex(rs.dump(rs.build(td)), r"20\d\d-\d\d-\d\dT")     # no clock in the file

    def test_write_refuses_a_read_only_root(self):
        target = rs.WS / "Evals" / "x" / rs.SKELETON
        with mock.patch.object(rs.tempfile, "mkstemp", side_effect=AssertionError("must not write")), \
                mock.patch.object(Path, "mkdir", side_effect=AssertionError("must not create folders")):
            with self.assertRaises(Exception) as caught:
                rs.atomic_write(target, "{}")
        self.assertEqual(caught.exception.__class__.__name__, "ContextError")

    def test_source_hygiene(self):
        source = (HERE / "rubric_skeleton.py").read_text()
        ast.parse(source, feature_version=(3, 9))
        self.assertTrue(source.split('"""', 2)[2].lstrip().startswith("from __future__ import annotations"))
        self.assertNotIn("Evals/" + "task_inputs", source)
        self.assertNotIn("datetime.now", source)
        self.assertNotIn("time.time", source)

    def test_backtest_on_the_archives(self):
        if not rs.ARCHIVES.is_dir():
            self.skipTest("no archived tasks in this copy of the bundle")
        r = rs.backtest()
        if not r["rows"]:
            self.skipTest("no archive has a surface, a manifest and a final rubric")
        for row in r["rows"]:
            self.assertGreaterEqual(row["skeleton_rows"], row["surface_slots"], row["archive"])
            self.assertGreaterEqual(row["skeleton_weight"], row["surface_weight"], row["archive"])
        self.assertIn("gap closed", rs.backtest_text(r))


if __name__ == "__main__":
    unittest.main()

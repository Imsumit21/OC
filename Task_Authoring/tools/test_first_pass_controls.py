"""first_pass_controls: modes, tool-result mapping, and the two hooks in stage_gate.py."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import first_pass_controls as fp  # noqa: E402
import stage_gate as gate  # noqa: E402

SCRATCH = HERE.parent / "support" / "scratch"
ALL = [cid for checks in fp.STAGE_CHECKS.values() for cid, _ in checks] + [cid for cid, _ in fp.EVERY_STAGE]
WARN = {"modes": {}}
BLOCK = {"modes": {cid: "block" for cid in ALL}}
OFF = {"modes": {cid: "off" for cid in ALL}}


def result(verdict, *checks):
    return {"tool": "stub", "version": 1, "verdict": verdict,
            "checks": [{"id": cid, "status": status, "detail": detail} for cid, status, detail in checks]}


class Base(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.td = Path(tempfile.mkdtemp(dir=SCRATCH, prefix="first-pass-"))
        self.addCleanup(shutil.rmtree, self.td, ignore_errors=True)
        (self.td / "Working_Files").mkdir()

    def ctx(self, stage, context=None):
        return fp._FakeCtx(self.td, stage, context)

    def wf(self, name, data):
        path = self.td / "Working_Files" / name
        path.write_text(data if isinstance(data, str) else json.dumps(data))
        return path

    def stub(self, name, **functions):
        module = types.ModuleType(name)
        for key, value in functions.items():
            setattr(module, key, value)
        return patch.dict(sys.modules, {name: module})


class PolicyTests(Base):
    def test_missing_or_broken_policy_means_warn(self):
        self.assertEqual({}, fp.policy(self.td / "absent.json"))
        bad = self.td / "bad.json"
        bad.write_text("{not json")
        self.assertEqual({}, fp.policy(bad))
        self.assertEqual("warn", fp.mode("budget.design", {}))
        self.assertEqual("warn", fp.mode("budget.design", {"modes": {"budget.design": "strict"}}))
        self.assertEqual("block", fp.mode("budget.design", {"modes": {"budget.design": "block"}}))

    def test_shipped_policy_names_every_check_and_blocks_nothing_untested(self):
        pol = fp.policy()
        self.assertEqual("first-pass-policy-v1", pol.get("schema"))
        for cid in ALL:
            self.assertIn(cid, pol["modes"], cid)
            self.assertIn(pol["modes"][cid], fp.MODES)
        # Plan section 5: a check blocks only after its backtest and one task in warn mode. A flip is the owner's.
        self.assertEqual([], sorted(cid for cid, value in pol["modes"].items() if value == "block"))

    def test_every_stage_named_is_a_real_gate_stage(self):
        for stage in fp.STAGE_CHECKS:
            self.assertIn(stage, gate.STAGES)


class MappingTests(Base):
    def test_tool_verdicts_map_by_mode(self):
        self.wf(fp.BUDGET, {"design_id": "D1", "units": []})
        cases = [("PASS", WARN, "PASS", False), ("PASS", BLOCK, "PASS", False),
                 ("WARN", BLOCK, "WARN", False),            # a tool WARN is advisory in every mode
                 ("FAIL", WARN, "WARN", False), ("FAIL", BLOCK, "FAIL", True)]
        for verdict, pol, status, blocking in cases:
            with self.subTest(verdict=verdict, block=pol is BLOCK):
                with self.stub("difficulty_budget", evaluate=lambda td, v=verdict: result(
                        v, ("budget.anchors", "FAIL" if v == "FAIL" else v, "anchors carry 6% of 12%"))):
                    ctx = self.ctx("scenario")
                    fp.budget_design(None, ctx, pol)
                self.assertEqual([(status, blocking)], [(r["status"], r["blocking"]) for r in ctx.res])
                if verdict == "FAIL":
                    self.assertIn("budget.anchors", ctx.res[0]["detail"])

    def test_off_adds_nothing_and_a_missing_artifact_follows_the_mode(self):
        for fn, stage in ((fp.fit_census, "scenario"), (fp.budget_design, "scenario"),
                          (fp.exposure_units, "injection"), (fp.sweep_forks, "injection"),
                          (fp.skeleton_present, "injection"), (fp.precheck_outcome, "hardening"),
                          (fp.budget_rubric, "rubric-check")):
            with self.subTest(check=fn.__name__):
                ctx = self.ctx(stage)
                fn(None, ctx, OFF)
                self.assertEqual([], ctx.res)
                ctx = self.ctx(stage)
                fn(None, ctx, WARN)
                self.assertEqual(["WARN"], [r["status"] for r in ctx.res])
                self.assertIn("not blocking", ctx.res[0]["detail"])
                ctx = self.ctx(stage)
                fn(None, ctx, BLOCK)
                self.assertTrue(ctx.res[0]["blocking"])

    def test_a_malformed_tool_result_never_passes(self):
        self.wf(fp.BUDGET, {})
        for bad in (None, {}, {"verdict": "GREAT"}, "PASS"):
            with self.subTest(result=bad), self.stub("difficulty_budget", evaluate=lambda td, b=bad: b):
                ctx = self.ctx("scenario")
                fp.budget_design(None, ctx, BLOCK)
                self.assertTrue(ctx.res[0]["blocking"])

    def test_a_tool_error_is_contained_and_follows_the_mode(self):
        def boom(td):
            raise RuntimeError("exploded")
        for pol, status in ((WARN, "WARN"), (BLOCK, "FAIL")):
            with self.subTest(block=pol is BLOCK), self.stub("oe_qualifier_check", evaluate=boom), \
                    patch.object(fp, "policy", lambda path=fp.POLICY, p=pol: p):
                ctx = self.ctx("oe-check")
                fp.check_stage(None, ctx)
                rows = [r for r in ctx.res if r["id"] == "oe.qualifiers"]
                self.assertEqual([status], [r["status"] for r in rows])
                self.assertIn("exploded", rows[0]["detail"])

    def test_stored_record_bound_to_other_bytes_is_stale(self):
        (self.td / "01_Universe_Inject.sql").write_text("-- rev1\n")
        self.wf(fp.BUDGET, {"design_id": "D1", "units": []})
        sha = lambda name: hashlib.sha256(fp._FakeCtx(self.td, "injection").p(name).read_bytes()).hexdigest()  # noqa: E731
        good = {"verdict": "PASS", "checks": [],
                "bound_to": {"01_Universe_Inject.sql": sha("01_Universe_Inject.sql"), fp.BUDGET: sha(fp.BUDGET)}}
        self.wf(fp.EXPOSURE, good)
        ctx = self.ctx("injection")
        fp.exposure_units(None, ctx, BLOCK)
        self.assertEqual("PASS", ctx.res[0]["status"])
        (self.td / "01_Universe_Inject.sql").write_text("-- rev2\n")
        ctx = self.ctx("injection")
        fp.exposure_units(None, ctx, BLOCK)
        self.assertTrue(ctx.res[0]["blocking"])
        self.assertIn("stale", ctx.res[0]["detail"])

    def test_bound_to_accepts_nested_sha_and_path_keys(self):
        (self.td / "01_Universe_Inject.sql").write_text("-- sql\n")
        digest = hashlib.sha256(b"-- sql\n").hexdigest()
        ctx = self.ctx("injection")
        names = {"01_Universe_Inject.sql": ("01_Universe_Inject.sql", "sql")}
        self.assertEqual([], fp._bound(ctx, {"bound_to": {"sql": {"sha256": digest}}}, names))
        self.assertEqual([], fp._bound(ctx, {"bound_to": {"task/01_Universe_Inject.sql": digest}}, names))
        self.assertEqual(1, len(fp._bound(ctx, {"bound_to": {"sql": "0" * 64}}, names)))
        self.assertEqual([], fp._bound(ctx, {"bound_to": {}}, names))   # a file the record never bound is not reported


class StageRuleTests(Base):
    def test_fit_census_routes_no_natural_cohort_to_injection_and_refuses_another_assignment(self):
        self.wf(fp.FIT, {"verdict": "NO NATURAL COHORT", "assignment_hash": "a" * 64, "limits": ["Gmail is thin"]})
        ctx = self.ctx("scenario", {"assignment_hash": "a" * 64})
        fp.fit_census(None, ctx, BLOCK)
        self.assertEqual("PASS", ctx.res[0]["status"])
        self.assertIn("built by injection", ctx.res[0]["detail"])
        self.assertNotIn("skip", ctx.res[0]["detail"].lower())
        ctx = self.ctx("scenario", {"assignment_hash": "b" * 64})
        fp.fit_census(None, ctx, BLOCK)
        self.assertTrue(ctx.res[0]["blocking"])

    def test_stop_rule_counts_no_go_per_design(self):
        self.wf(fp.BUDGET, {"design_id": "D1", "units": []})
        self.wf(fp.PRECHECK_LOG, {"entries": [{"design_id": "D1", "verdict": "NO-GO"},
                                               {"design_id": "D1", "verdict": "GO"}]})
        pol = dict(BLOCK, precheck={"stop_after_no_go": 2})
        ctx = self.ctx("hardening")
        fp.stop_rule(None, ctx, pol)
        self.assertEqual("PASS", ctx.res[0]["status"])
        self.wf(fp.PRECHECK_LOG, {"entries": [{"design_id": "D1", "verdict": "NO-GO"},
                                               {"design_id": "D1", "verdict": "NO-GO"}]})
        ctx = self.ctx("hardening")
        fp.stop_rule(None, ctx, pol)
        self.assertTrue(ctx.res[0]["blocking"])
        self.assertIn("/create-scenario", ctx.res[0]["detail"])
        self.wf(fp.BUDGET, {"design_id": "D2", "units": []})                 # a redesign starts the count again
        ctx = self.ctx("hardening")
        fp.stop_rule(None, ctx, pol)
        self.assertEqual("PASS", ctx.res[0]["status"])

    def test_bare_task_inputs_folder_is_flagged(self):
        bare = self.td / "task_inputs"
        bare.mkdir()
        ctx = fp._FakeCtx(bare, "scenario")
        fp.task_folder(None, ctx, BLOCK)
        self.assertTrue(ctx.res[0]["blocking"])
        ctx = fp._FakeCtx(bare, "scenario")
        fp.task_folder(None, ctx, WARN)
        self.assertEqual("WARN", ctx.res[0]["status"])
        named = self.td / "task_inputsRobert"
        named.mkdir()
        ctx = fp._FakeCtx(named, "scenario")
        fp.task_folder(None, ctx, BLOCK)
        self.assertEqual("PASS", ctx.res[0]["status"])

    def test_c4_reads_the_result_not_a_self_review_counter_reading(self):
        check = self.td / "Working_Files" / "04_Prompt_Check.md"
        check.write_text("## Check results (C1-C24)\n\n| C4 | clean | Finance work |\n\n## Self-review\n\n"
                         "| C4 | Business Function could read 3 | the platform scored it 5 |\n")
        ctx = self.ctx("prompt-check")
        fp.assignment_fit(None, ctx, BLOCK)
        self.assertEqual("PASS", ctx.res[0]["status"])
        check.write_text("## Findings\n\n| 6 | C4 | Assigned Task Skill - Fail | the skill is incidental |\n")
        ctx = self.ctx("prompt-check")
        fp.assignment_fit(None, ctx, BLOCK)
        self.assertTrue(ctx.res[0]["blocking"])
        self.assertIn("hard FAIL", ctx.res[0]["detail"])

    def test_c4_is_clean_on_every_archived_prompt_check(self):
        archives = sorted((HERE.parent / "support" / "completed_tasks").glob("*/task_inputs/Working_Files/04_Prompt_Check.md"))
        if not archives:
            self.skipTest("no archived tasks in this checkout")
        for path in archives:
            with self.subTest(task=path.parents[2].name):
                ctx = fp._FakeCtx(path.parents[1], "prompt-check")
                fp.assignment_fit(None, ctx, BLOCK)
                self.assertEqual("PASS", ctx.res[0]["status"], ctx.res[0]["detail"])

    def test_oe_qualifiers_read_the_counts_not_the_tool_verdict(self):
        def stub(counts, verdict="WARN"):
            return lambda td: {"verdict": verdict, "checks": [{"id": "oe.parse", "status": "PASS", "detail": ""}],
                               "counts": dict({"checked": 40, "unverifiable": 0, "unsupported": 0, "contradicted": 0},
                                              **counts)}
        cases = (({"unverifiable": 12}, "PASS", False), ({"unsupported": 2, "unverifiable": 5}, "WARN", False),
                 ({"contradicted": 1}, "FAIL", True))
        for counts, status, blocking in cases:
            with self.subTest(counts=counts), self.stub("oe_qualifier_check", evaluate=stub(counts)):
                ctx = self.ctx("oe-check")
                fp.oe_qualifiers(None, ctx, BLOCK)
                self.assertEqual([(status, blocking)], [(r["status"], r["blocking"]) for r in ctx.res])
        with self.stub("oe_qualifier_check", evaluate=lambda td: {"verdict": "FAIL", "counts": {}, "checks": [
                {"id": "oe.parse", "status": "FAIL", "detail": "no event headings"}]}):
            ctx = self.ctx("oe-check")
            fp.oe_qualifiers(None, ctx, BLOCK)
            self.assertTrue(ctx.res[0]["blocking"])

    def test_oe_qualifiers_skip_under_rerun_lint_without_running_the_tool(self):
        def boom(td):
            raise AssertionError("the OE check must not run under --rerun lint")
        with self.stub("oe_qualifier_check", evaluate=boom):
            ctx = self.ctx("oe-check")
            ctx.rerun = "lint"
            fp.oe_qualifiers(None, ctx, BLOCK)
        self.assertEqual([("SKIP", False)], [(r["status"], r["blocking"]) for r in ctx.res])

    def test_rubric_eval_lint_blocks_on_gate_or_major_findings_only(self):
        (self.td / "09_Rubrics.json").write_text("[]")
        self.wf("09_Rubric_Check.md", "anon_token: every bracketed token is a real anonymised name\n")

        def lint(findings):
            return types.SimpleNamespace(run_tool=lambda args: (0, json.dumps({"findings": findings, "count": len(findings)}), ""),
                                         _json_stdout=gate._json_stdout)
        soft = [{"row": 3, "check": "anon_token", "severity": "check", "text": "[PERSON_NAME_1]"}]
        hard = soft + [{"row": 9, "check": "tool_name", "severity": "Major", "text": "mcp__"}]
        ctx = self.ctx("rubric-check")
        fp.rubric_eval_lint(lint(soft), ctx, BLOCK)
        self.assertEqual("PASS", ctx.res[0]["status"])                 # review findings named in the check report
        ctx = self.ctx("rubric-check")
        fp.rubric_eval_lint(lint(hard), ctx, BLOCK)
        self.assertTrue(ctx.res[0]["blocking"])
        self.assertIn("tool_name", ctx.res[0]["detail"])
        self.wf("09_Rubric_Check.md", "nothing about the lint\n")
        ctx = self.ctx("rubric-check")
        fp.rubric_eval_lint(lint(soft), ctx, BLOCK)
        self.assertEqual("WARN", ctx.res[0]["status"])                 # unreviewed, never blocking
        broken = types.SimpleNamespace(run_tool=lambda args: (2, "", "no context"), _json_stdout=gate._json_stdout)
        ctx = self.ctx("rubric-check")
        fp.rubric_eval_lint(broken, ctx, BLOCK)
        self.assertTrue(ctx.res[0]["blocking"])


class GateHookTests(Base):
    """The two places stage_gate.py calls this module."""

    def test_selftest_keeps_the_unconditional_v3_pass(self):
        ctx = gate.Ctx("prompt-writing", self.td, selftest=True)
        ctx.v3 = True
        gate.canonical_outcome(ctx, None)
        self.assertEqual([("structure.accepted_outcomes", "PASS")], [(r["id"], r["status"]) for r in ctx.res])

    def test_real_v3_gate_reads_the_fork_sweep(self):
        for pol, status, blocking in ((WARN, "WARN", False), (BLOCK, "FAIL", True)):
            with self.subTest(block=pol is BLOCK), patch.object(fp, "policy", lambda path=fp.POLICY, p=pol: p):
                ctx = gate.Ctx("prompt-writing", self.td)
                ctx.v3 = True
                gate.canonical_outcome(ctx, None)                      # no sweep record
                self.assertEqual([("structure.accepted_outcomes", status, blocking)],
                                 [(r["id"], r["status"], r["blocking"]) for r in ctx.res])
        self.wf(fp.SWEEP, {"schema": "coherence-sweep-v1"})
        with self.stub("coherence_sweep", evaluate=lambda td: result("PASS")), \
                patch.object(fp, "policy", lambda path=fp.POLICY: BLOCK):
            ctx = gate.Ctx("prompt-writing", self.td)
            ctx.v3 = True
            gate.canonical_outcome(ctx, None)
        self.assertEqual("PASS", ctx.res[0]["status"])
        self.assertIn("V3 accepts multiple fair outcomes", ctx.res[0]["detail"])
        with self.stub("coherence_sweep", evaluate=lambda td: result(
                "FAIL", ("sweep.forks", "FAIL", "1 open material fork: FK3"))), \
                patch.object(fp, "policy", lambda path=fp.POLICY: BLOCK):
            ctx = gate.Ctx("prompt-writing", self.td)
            ctx.v3 = True
            gate.canonical_outcome(ctx, None)
        self.assertTrue(ctx.res[0]["blocking"])
        self.assertIn("FK3", ctx.res[0]["detail"])

    def test_sweep_off_restores_the_plain_pass(self):
        with patch.object(fp, "policy", lambda path=fp.POLICY: {"modes": {"sweep.forks": "off"}}):
            ctx = gate.Ctx("prompt-writing", self.td)
            ctx.v3 = True
            gate.canonical_outcome(ctx, None)
        self.assertEqual("PASS", ctx.res[0]["status"])

    def _run_scenario(self, selftest):
        names = gate.STAGES["scenario"]["inputs"] + gate.STAGES["scenario"]["outputs"]
        for age, name in enumerate(names):                     # inputs first: every output is newer than its input
            target = self.td / "Working_Files" / name if name != "00_Assigments.md" else self.td / name
            target.write_text("x\n")
            os.utime(target, (1_700_000_000 + age * 100, 1_700_000_000 + age * 100))

        def context(ctx):
            ctx.v3, ctx.context = True, {"assignment_hash": "a" * 64, "difficulty_mode": "easy"}
            return True
        readiness = types.ModuleType("readiness_controls")
        readiness.check_stage = lambda g, c: None
        with patch.object(gate, "assignment_context", context), patch.object(gate, "v3_checks", lambda ctx: None), \
                patch.object(gate, "own_paste", lambda ctx, primary, outputs: None), \
                patch.dict(gate.STAGES["scenario"], {"fn": lambda ctx: None}), \
                patch.dict(sys.modules, {"readiness_controls": readiness}), \
                patch.object(fp, "policy", lambda path=fp.POLICY: WARN):
            return gate.run_stage("scenario", self.td, selftest=selftest)

    def test_run_stage_adds_first_pass_checks_to_a_real_v3_gate_only(self):
        ctx = self._run_scenario(selftest=False)
        ids = {r["id"]: r for r in ctx.res}
        self.assertIn("fit.census", ids)
        self.assertIn("budget.design", ids)
        self.assertEqual("WARN", ids["budget.design"]["status"])
        self.assertEqual("PASS", gate.verdict_of(ctx))                 # warn mode never blocks the stage
        ctx = self._run_scenario(selftest=True)
        self.assertNotIn("budget.design", {r["id"] for r in ctx.res})   # the fixture self-test is untouched


if __name__ == "__main__":
    unittest.main()

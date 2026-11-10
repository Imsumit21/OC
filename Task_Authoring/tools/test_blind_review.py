"""Tests for blind_review.py; run with: cd Task_Authoring/tools && python3.12 -B -m unittest test_blind_review."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import sys
import unittest
from pathlib import Path

import blind_review as br
import selftest_sandbox

REAL_EVALS = br.WS / "Evals" / "references" / "rules" / "deep_recheck.md"


def finding(**kw):
    base = {"issue_type": "unique_ground_truth", "severity": "Major", "quote": "x", "evidence": "rec", "fix": "f"}
    base.update(kw)
    return base


class Fixture(unittest.TestCase):
    """A stub Evals/ tree and a small task folder in a fresh scratch folder per test."""

    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("test_blind_review_")
        self.tmp = Path(self._tmp.name)
        self.root = self.tmp / "ws"
        br.stub_sources(self.root)
        self.task = self.tmp / "task"
        br.make_fixture(self.task)

    def tearDown(self):
        self._tmp.cleanup()

    def plan(self, stage, **kw):
        return br.plan(self.task, stage, root=self.root, **kw)

    def reply(self, obj, name="reply.json"):
        path = self.tmp / name
        path.write_text(json.dumps(obj) if not isinstance(obj, str) else obj, encoding="utf-8")
        return path

    def record_all(self, stage, number, findings=None):
        manifest = br.load_manifest(self.task, stage, number)
        findings = findings or {}
        for entry in manifest["passes"]:
            pid = entry["pass"]
            found = findings.get(pid, [])
            obj = {"pass": pid, "artifact_sha256": manifest["artifact"]["sha256"], "checked": 3, "findings": found,
                   "verdict": "FAIL" if any(f["severity"] == "Major" for f in found) else
                   "NON-FAIL" if found else "PASS"}
            result = br.record(self.task, stage, number, pid, self.reply(obj, f"{stage}{number}{pid}.json"))
            self.assertEqual(result["verdict"], "PASS", result["checks"])
        return manifest


class TestParsing(unittest.TestCase):
    def test_prompt_sentences(self):
        text = ("On Thursday in #winddown Leonard asked me. Can you do it for me? He laid out how. \"Fine.\" Then "
                "the sheet costs 1,234.50 now.\nNew line here")
        items = br.prompt_items(text)
        self.assertEqual([i["id"] for i in items], ["S1", "S2", "S3", "S4", "S5", "S6"])
        self.assertEqual(items[4]["text"], "Then the sheet costs 1,234.50 now.")
        self.assertIn("1234.50", items[4]["tokens"])

    def test_oe_identity_ignores_number_and_refs(self):
        a = br.oe_items("Intro\n\nOE 1  Read X\nExpected: y\n\nOE 2  Read Z (from OE 1)\nExpected: w\n")
        b = br.oe_items("Intro\n\nOE 1  Read X\nExpected: y\n\nOE 3  Read Z (from OE 1)\nExpected: w\n")
        self.assertEqual([i["id"] for i in a], ["OE-PRE", "OE 1", "OE 2"])
        self.assertEqual(a[2]["refs"], [1])
        self.assertEqual(a[2]["sha256"], b[2]["sha256"])     # renumbering alone does not change identity
        dup = br.oe_items("OE 1 a\nOE 1 b\n")
        self.assertEqual([i["id"] for i in dup], ["OE 1", "OE 1.2"])

    def test_tokens(self):
        tokens = br.tokens_of("ENG-2444 16,428.57 leonard.hayes@harmonygames.co [PERSON_NAME_0054] f_33040338 "
                              "C0ADGSZKR3R/1770945859.212469 #winddown 2026 22")
        for token in ("eng-2444", "16428.57", "leonard.hayes@harmonygames.co", "person_name_0054", "f_33040338",
                      "c0adgszkr3r/1770945859.212469", "#winddown"):
            self.assertIn(token, tokens)
        self.assertNotIn("2026", tokens)
        self.assertNotIn("22", tokens)

    def test_rubric_channel_not_a_link(self):
        items = br.rubric_items([{"title": "The Agent posts in #winddown the figure 1,000.00", "category": "Outcome",
                                  "weight": 1, "justification": "j", "evidence": "e"}])
        self.assertEqual(items[0]["tokens"], ["1000.00"])

    @unittest.skipUnless((br.WS / "Evals" / "tools" / "hg_rubric_ledger.py").is_file(), "no local Evals/")
    def test_row_hash_matches_platform_ledger(self):
        sys.dont_write_bytecode = True
        spec = importlib.util.spec_from_file_location("hg_rubric_ledger_probe",
                                                      br.WS / "Evals" / "tools" / "hg_rubric_ledger.py")
        ledger = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ledger)
        rows = [{"title": "  The Agent  moves ENG-1 ", "category": "Outcome", "weight": 3, "justification": "j",
                 "evidence": "e"}, {"title": "t", "annotations": {"rubric_category": "Process"}, "weight": 1}]
        for row in rows:
            self.assertEqual(br.row_hash(row), ledger.row_hash(row))

    def test_parse_reply_accepts_a_json_fence(self):
        obj, problem = br._parse_reply(b'```json\n{"a": 1}\n```\n')
        self.assertEqual((obj, problem), ({"a": 1}, None))
        self.assertIsNotNone(br._parse_reply(b"here you go: {}")[1])

    def test_id_normalisation(self):
        self.assertEqual(br._ids(["r3", 4], "row"), ["R3", "R4"])
        self.assertEqual(br._ids("OE12", "event"), ["OE 12"])
        self.assertEqual(br._ids("sql", "span"), ["SQL"])
        self.assertIsNone(br._ids("row three", "row"))

    def test_match_id(self):
        self.assertTrue(br._match_id("robert@harmonygames.co/1815095592611804295", "1815095592611804295"))
        self.assertTrue(br._match_id("C0ADGSZKR3R/1770945859.212469", "slack C0ADGSZKR3R/1770945859.212469 (post)"))
        self.assertFalse(br._match_id("ENG-245", "ENG-2450"))


class TestRealSources(unittest.TestCase):
    @unittest.skipUnless(REAL_EVALS.is_file(), "no local Evals/")
    def test_every_pass_text_resolves_in_local_evals(self):
        ranges = br.load_ranges(list(br.PASS_TABLE["ranges"]))
        self.assertEqual(len(ranges), len(br.PASS_TABLE["ranges"]))
        self.assertTrue(ranges["dr.P1"]["text"].startswith("### P1"))
        self.assertIn("You are reviewer F<n>", ranges["rf.full"]["text"])


class TestPlan(Fixture):
    def test_dry_run_writes_nothing(self):
        result = self.plan("rubric")
        self.assertFalse(result["written"])
        self.assertFalse(br.review_dir(self.task, "rubric").exists())
        self.assertEqual(result["checks"][-1]["status"], "SKIP")

    def test_briefs_are_blind_and_bound(self):
        self.plan("rubric", write=True)
        folder = br.round_dir(self.task, "rubric", 1)
        manifest = br.load_manifest(self.task, "rubric", 1)
        self.assertEqual([p["pass"] for p in manifest["passes"]], ["F2", "F3"] + [f"R{n}" for n in range(1, 8)])
        for entry in manifest["passes"]:
            text = (folder / entry["brief"]).read_text(encoding="utf-8")
            self.assertTrue(text.startswith("# " + br.BANNER))
            self.assertEqual(br._sha(text.encode("utf-8")), entry["brief_sha256"])
            self.assertNotIn("SECRET", text)
            for other in ("R1", "R2", "R3", "R4", "R5", "R6", "R7"):
                needle = f"stub text of dr.{other},"
                (self.assertIn if other == entry["pass"] else self.assertNotIn)(needle, text)
        self.assertIn("You are reviewer F2", (folder / "brief_F2.md").read_text(encoding="utf-8"))
        self.assertIn("stub text of ce.s79", (folder / "brief_R4.md").read_text(encoding="utf-8"))
        self.assertEqual(manifest["passes"][2]["sources"][0]["lines"], [61, 67])
        self.assertEqual(len(manifest["items"]), 6)
        for item in manifest["inputs"]:
            self.assertEqual(br._sha((folder / item["path"]).read_bytes()), item["sha256"])
        self.assertFalse(any("SECRET" in p.read_text(encoding="utf-8", errors="replace")
                             for p in folder.rglob("*") if p.is_file()))

    def test_o3_never_sees_oes(self):
        self.plan("oe", write=True)
        folder = br.round_dir(self.task, "oe", 1)
        o3 = (folder / "brief_O3.md").read_text(encoding="utf-8")
        self.assertNotIn("OE-ONLY-MARKER", o3)
        self.assertNotIn("artifact/08_Oracle_Events.md", o3)
        self.assertIn("OE-ONLY-MARKER", (folder / "brief_O1.md").read_text(encoding="utf-8"))

    def test_solver_brief_hides_assignment_and_budget(self):
        self.plan("solver", write=True)
        text = (br.round_dir(self.task, "solver", 1) / "brief_SOLVER.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# " + br.BANNER))
        for hidden in ("Difficulty Mode", "Competency", "SECRET", "00_Task_Details"):
            self.assertNotIn(hidden, text)
        self.assertIn("grep -n -i", text)

    def test_moved_source_stops_with_location(self):
        path = self.root / br._DR
        lines = path.read_text(encoding="utf-8").split("\n")
        lines.insert(10, "inserted")
        path.write_text("\n".join(lines), encoding="utf-8")
        with self.assertRaises(br.ReviewError) as caught:
            self.plan("prompt")
        message = str(caught.exception)
        self.assertIn("deep_recheck.md:61-67", message)
        self.assertIn("now starts at line 62", message)

    def test_missing_source_file_stops(self):
        (self.root / br._RF).unlink()
        with self.assertRaises(br.ReviewError):
            self.plan("rubric")
        self.plan("prompt")                       # the prompt passes do not need rubric_flow_v2.md

    def test_round_with_output_is_not_replanned(self):
        self.plan("prompt", write=True)
        self.record_all("prompt", 1)
        with self.assertRaises(br.ReviewError):
            self.plan("prompt", round_no=1, write=True)
        self.assertEqual(self.plan("prompt")["round"], 2)

    def test_replan_of_an_unrecorded_round_reuses_its_number(self):
        self.plan("prompt", write=True)
        (self.task / br.PROMPT).write_text("A new prompt. Two sentences.\n", encoding="utf-8")
        result = self.plan("prompt", write=True)
        self.assertEqual(result["round"], 1)
        self.assertEqual(br.load_manifest(self.task, "prompt", 1)["artifact"]["items"], 2)

    def test_no_injection_and_missing_artifact(self):
        (self.task / br.SQL).write_text("-- no statements\n", encoding="utf-8")
        self.plan("prompt", write=True)
        text = (br.round_dir(self.task, "prompt", 1) / "brief_P3.md").read_text(encoding="utf-8")
        self.assertIn("No injection", text)
        (self.task / br.OE).unlink()
        with self.assertRaises(br.ReviewError):
            self.plan("oe")


class TestScope(Fixture):
    def test_changed_scope_flagged_edited_dependant(self):
        self.plan("rubric", write=True)
        self.record_all("rubric", 1, {"R1": [finding(row="R5", issue_type="overly_specific",
                                                     quote="Domino Delights cost")]})
        rows = json.loads((self.task / br.RUBRIC).read_text(encoding="utf-8"))
        rows[1]["weight"] = 5
        (self.task / br.RUBRIC).write_text(json.dumps(rows), encoding="utf-8")
        result = self.plan("rubric", write=True)
        status = result["manifest"]["classification"]["status"]
        self.assertEqual(result["scope"], "changed")
        self.assertEqual(result["in_scope"], ["R2", "R3", "R5"])
        self.assertEqual((status["R2"], status["R3"], status["R5"]), ("edited", "dependant", "flagged"))
        self.assertEqual([p["pass"] for p in result["passes"]], [f"R{n}" for n in range(1, 8)])

    def test_removed_row_runs_whole_set_passes(self):
        self.plan("rubric", write=True)
        self.record_all("rubric", 1)
        rows = json.loads((self.task / br.RUBRIC).read_text(encoding="utf-8"))
        del rows[3]                                        # the email row shares no token with any other row
        (self.task / br.RUBRIC).write_text(json.dumps(rows), encoding="utf-8")
        result = self.plan("rubric")
        self.assertEqual(result["in_scope"], [])
        self.assertEqual([p["pass"] for p in result["passes"]], ["R3", "R4"])

    def test_context_change_and_full_flag(self):
        self.plan("rubric", write=True)
        self.record_all("rubric", 1)
        (self.task / br.OE).write_text("OE 1  Changed\nExpected: x\n", encoding="utf-8")
        result = self.plan("rubric")
        self.assertEqual(result["scope"], "full")
        self.assertIn("oe", result["scope_reason"])
        (self.task / br.SQL).unlink()
        self.assertIn("injection", self.plan("rubric")["scope_reason"])

    def test_forced_full(self):
        self.plan("prompt", write=True)
        self.record_all("prompt", 1)
        self.assertEqual(self.plan("prompt", full=True)["scope"], "full")

    def test_unfinished_full_round_is_full_again(self):
        self.plan("prompt", write=True)
        manifest = br.load_manifest(self.task, "prompt", 1)
        br.record(self.task, "prompt", 1, "P1", self.reply({"pass": "P1", "artifact_sha256": manifest["artifact"]
                                                            ["sha256"], "checked": 3, "findings": [],
                                                            "verdict": "PASS"}))
        result = self.plan("prompt")
        self.assertEqual(result["scope"], "full")
        self.assertIn("did not finish", result["scope_reason"])

    def test_prompt_neighbours(self):
        self.plan("prompt", write=True)
        self.record_all("prompt", 1)
        text = (self.task / br.PROMPT).read_text(encoding="utf-8")
        (self.task / br.PROMPT).write_text(text.replace("Build it as a sheet", "Build it as one sheet"),
                                           encoding="utf-8")
        result = self.plan("prompt")
        self.assertEqual(result["in_scope"], ["S1", "S2", "S3"])
        self.assertEqual(result["manifest"]["classification"]["status"]["S2"], "edited")

    def test_unchanged_round_restates_previous_verdict(self):
        self.plan("prompt", write=True)
        self.record_all("prompt", 1, {"P1": [finding(span="S3", quote="reply to him")]})
        result = self.plan("prompt", write=True)
        self.assertEqual(result["scope"], "changed")
        self.assertEqual(result["in_scope"], ["S3"])        # the flagged sentence is re-checked even unchanged
        self.record_all("prompt", 2)
        third = self.plan("prompt", write=True)
        self.assertEqual(third["passes"], [])
        summary = br.evaluate(self.task, "prompt", root=self.root)
        self.assertEqual(summary["round"], 3)
        self.assertEqual(summary["restated_from"], 2)
        self.assertEqual(summary["rehearsal_verdict"], "PASS")

    def test_oe_changed_round_carries_o3(self):
        self.plan("oe", write=True)
        self.record_all("oe", 1)
        text = (self.task / br.OE).read_text(encoding="utf-8").replace("Expected: posted.", "Expected: sent.")
        (self.task / br.OE).write_text(text, encoding="utf-8")
        result = self.plan("oe", write=True)
        self.assertEqual(result["in_scope"], ["OE 3"])
        self.assertEqual(result["manifest"]["carried"], {"O3": 1})
        self.record_all("oe", 2)
        summary = br.evaluate(self.task, "oe", root=self.root)
        self.assertEqual(summary["passes"]["carried"], {"O3": 1})
        self.assertEqual(summary["rehearsal_verdict"], "PASS")


class TestRecord(Fixture):
    def setUp(self):
        super().setUp()
        self.plan("rubric", write=True)
        self.manifest = br.load_manifest(self.task, "rubric", 1)
        self.sha = self.manifest["artifact"]["sha256"]

    def attempt(self, obj, pid="R1", **kw):
        return br.record(self.task, "rubric", 1, pid, self.reply(obj), **kw)

    def base(self, **kw):
        obj = {"pass": "R1", "artifact_sha256": self.sha, "verdict": "FAIL",
               "findings": [finding(row="R2", issue_type="incorrect", quote="16,428.57 in the Domino")]}
        obj.update(kw)
        return obj

    def assertRefused(self, obj, needle, pid="R1"):
        result = self.attempt(obj, pid)
        self.assertEqual(result["verdict"], "FAIL")
        self.assertTrue(any(needle in c["detail"] for c in result["checks"]), result["checks"])
        self.assertFalse((br.round_dir(self.task, "rubric", 1) / f"output_{pid}.json").exists())

    def test_good_reply_is_stored_with_binding(self):
        self.assertEqual(self.attempt(self.base())["verdict"], "PASS")
        stored = json.loads((br.round_dir(self.task, "rubric", 1) / "output_R1.json").read_text(encoding="utf-8"))
        self.assertEqual(stored["binding"]["artifact_sha256"], self.sha)
        self.assertEqual(stored["binding"]["brief_sha256"], self.manifest["passes"][2]["brief_sha256"])
        with self.assertRaises(br.ReviewError):
            self.attempt(self.base())
        self.assertEqual(self.attempt(self.base(verdict="FAIL"), replace=True)["verdict"], "PASS")

    def test_refusals(self):
        f = self.base()["findings"][0]
        self.assertRefused(self.base(artifact_sha256="ab" * 32), "other bytes")
        self.assertRefused(self.base(**{"pass": "R2"}), "expected 'R1'")
        self.assertRefused(self.base(findings=[dict(f, quote="not there")]), "not a substring")
        self.assertRefused(self.base(findings=[dict(f, quote=" ")]), "no quote")
        self.assertRefused(self.base(findings=[dict(f, row="R40")]), "does not exist")
        self.assertRefused(self.base(findings=[dict(f, issue_type="vibes")]), "unknown")
        self.assertRefused(self.base(findings=[dict(f, severity="Fatal")]), "severity")
        self.assertRefused(self.base(findings=[dict(f, severity="INVENTORY")]), "INVENTORY")
        self.assertRefused(self.base(findings=[{k: v for k, v in f.items() if k != "evidence"}]), "evidence")
        self.assertRefused(self.base(findings=[dict(f, event="OE 1")]), "exactly one locator")
        self.assertRefused(self.base(findings=[], verdict="PASS"), "checked")
        self.assertRefused(self.base(verdict="PASS"), "contradicts")
        self.assertRefused(self.base(findings=[dict(f, issue_type="weight", severity="Minor")]), "expected_weight")
        self.assertRefused(self.base(findings=[dict(f, issue_type="weight", severity="Minor", expected_weight=3)],
                                     verdict="NON-FAIL"), "equals the row's weight")
        self.assertRefused("not json at all", "not one JSON object")

    def test_quote_matching_tolerates_quotes_and_spacing(self):
        rows = json.loads((self.task / br.RUBRIC).read_text(encoding="utf-8"))
        self.assertIn("Robert's", rows[0]["title"])
        obj = self.base(findings=[finding(row="R1", issue_type="overly_specific", quote="sheet in  Robert’s Drive")])
        self.assertEqual(self.attempt(obj)["verdict"], "PASS")

    def test_span_and_pairs(self):
        obj = self.base(findings=[finding(span="S3", issue_type="missing_coverage", quote="with the totals for"),
                                  finding(row=["R2", "R3"], issue_type="duplicate", severity="Moderate",
                                          quote="moves ENG-2444")])
        self.assertEqual(self.attempt(obj, pid="R4")["verdict"], "FAIL")      # pass id mismatch
        obj["pass"] = "R4"
        self.assertEqual(self.attempt(obj, pid="R4")["verdict"], "PASS")

    def test_unplanned_pass(self):
        with self.assertRaises(br.ReviewError):
            self.attempt(self.base(**{"pass": "P1"}), pid="P1")

    def test_moderate_refused_on_prompt(self):
        self.plan("prompt", write=True)
        sha = br.load_manifest(self.task, "prompt", 1)["artifact"]["sha256"]
        obj = {"pass": "P2", "artifact_sha256": sha, "verdict": "FAIL",
               "findings": [finding(span="S1", severity="Moderate", quote="Leonard asked")]}
        result = br.record(self.task, "prompt", 1, "P2", self.reply(obj))
        self.assertEqual(result["verdict"], "FAIL")
        obj["findings"][0].update(severity="Major", span="SQL", quote="the wire came back")
        self.assertEqual(br.record(self.task, "prompt", 1, "P2", self.reply(obj))["verdict"], "PASS")


class TestSummary(Fixture):
    def test_no_round_yet(self):
        result = br.evaluate(self.task, "rubric", root=self.root)
        self.assertEqual(result["verdict"], "WARN")
        self.assertEqual(result["rehearsal_verdict"], "NONE")

    def test_missing_round_is_a_fail_result(self):
        self.plan("rubric", write=True)
        result = br.evaluate(self.task, "rubric", round_no=7, root=self.root)
        self.assertEqual(result["verdict"], "FAIL")

    def test_incomplete_then_clean(self):
        self.plan("rubric", write=True)
        manifest = br.load_manifest(self.task, "rubric", 1)
        br.record(self.task, "rubric", 1, "R1", self.reply({"pass": "R1", "artifact_sha256": manifest["artifact"]
                                                            ["sha256"], "checked": 6, "findings": [],
                                                            "verdict": "PASS"}))
        result = br.evaluate(self.task, "rubric", root=self.root)
        self.assertEqual(result["rehearsal_verdict"], "INCOMPLETE")
        self.assertEqual(result["verdict"], "WARN")
        self.assertEqual(len(result["passes"]["missing"]), 8)
        for entry in manifest["passes"][1:]:
            if entry["pass"] != "R1":
                br.record(self.task, "rubric", 1, entry["pass"], self.reply({
                    "pass": entry["pass"], "artifact_sha256": manifest["artifact"]["sha256"], "checked": 6,
                    "findings": [], "verdict": "PASS"}))
        br.record(self.task, "rubric", 1, "F2", self.reply({"pass": "F2", "artifact_sha256": manifest["artifact"]
                                                            ["sha256"], "checked": 6, "findings": [],
                                                            "verdict": "PASS"}))
        result = br.evaluate(self.task, "rubric", root=self.root)
        self.assertEqual((result["verdict"], result["rehearsal_verdict"], result["score"]), ("PASS", "PASS", 5))
        lines = br.render(result).splitlines()
        self.assertEqual(lines[0], "LOCAL REHEARSAL (rubric, round 1): PASS — not a platform verdict")
        self.assertIn("Rule applied: Eval 3 aggregation", lines[1])

    def test_merge_without_voting(self):
        self.plan("rubric", write=True)
        same = finding(row="R2", issue_type="overly_specific", quote="16,428.57")
        self.record_all("rubric", 1, {"R1": [same], "F3": [dict(same, quote="Domino Delights column")],
                                      "R5": [finding(row="R2", issue_type="overly_broad", quote="ENG-2444 line")],
                                      "R2": [finding(row="R1", issue_type="incorrect", severity="UNSURE",
                                                     quote="creates a sheet")]})
        result = br.evaluate(self.task, "rubric", root=self.root)
        merged = {(tuple(f["ids"]), f["issue_type"]): f for f in result["findings"]}
        self.assertEqual(merged[(("R2",), "overly_specific")]["passes"], ["F3", "R1"])
        self.assertEqual(len(merged[(("R2",), "overly_specific")]["quotes"]), 2)
        self.assertIn((("R2",), "overly_broad"), merged)
        self.assertEqual(merged[(("R1",), "incorrect")]["severity"], "UNSURE")
        self.assertEqual(result["rehearsal_verdict"], "FAIL")
        self.assertEqual(result["verdict"], "WARN")
        self.assertEqual(result["tally"]["major_rows_and_missing_outcomes"], 1)

    def test_live_artifact_change_warns(self):
        self.plan("prompt", write=True)
        self.record_all("prompt", 1)
        (self.task / br.PROMPT).write_text("Changed.\n", encoding="utf-8")
        result = br.evaluate(self.task, "prompt", root=self.root)
        binding = next(c for c in result["checks"] if c["id"] == "rehearsal.binding")
        self.assertEqual(binding["status"], "WARN")

    def test_tampered_output_fails(self):
        self.plan("prompt", write=True)
        self.record_all("prompt", 1)
        path = br.round_dir(self.task, "prompt", 1) / "output_P1.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        stored["output"]["artifact_sha256"] = "0" * 64
        path.write_text(json.dumps(stored), encoding="utf-8")
        self.assertEqual(br.evaluate(self.task, "prompt", root=self.root)["verdict"], "FAIL")

    def test_o3_inventory_warns(self):
        self.plan("oe", write=True)
        item = finding(span="S3", issue_type="open_instruction_item", severity="INVENTORY", quote="totals for",
                       evidence="A: sheet 10 | B: notice 12", fix="")
        self.record_all("oe", 1, {"O3": [item]})
        result = br.evaluate(self.task, "oe", root=self.root)
        check = next(c for c in result["checks"] if c["id"] == "rehearsal.o3_inventory")
        self.assertEqual(check["status"], "WARN")
        self.assertEqual(result["rehearsal_verdict"], "PASS")

    def test_solver_units(self):
        self.plan("solver", write=True)
        sha = br.load_manifest(self.task, "solver", 1)["artifact"]["sha256"]
        br.record(self.task, "solver", 1, "SOLVER", self.reply({
            "pass": "SOLVER", "artifact_sha256": sha, "verdict": "DONE", "answer": "the totals",
            "opened": ["1815095592611804295", "ENG-2450"]}))
        result = br.evaluate(self.task, "solver", root=self.root)
        units = {u["unit"]: u["opened"] for u in result["units"]}
        self.assertEqual(units, {"U1": False, "U2": True})            # realism U3 is ignored
        self.assertEqual(result["verdict"], "PASS")
        (self.task / br.WORK_DIR / br.BUDGET).unlink()
        result = br.evaluate(self.task, "solver", root=self.root)
        self.assertEqual(next(c for c in result["checks"] if c["id"] == "solver.deciders")["status"], "SKIP")

    def test_solver_reply_shape(self):
        self.plan("solver", write=True)
        sha = br.load_manifest(self.task, "solver", 1)["artifact"]["sha256"]
        bad = br.record(self.task, "solver", 1, "SOLVER", self.reply({"pass": "SOLVER", "artifact_sha256": sha,
                                                                      "verdict": "DONE", "opened": "x",
                                                                      "answer": ""}))
        self.assertEqual(bad["verdict"], "FAIL")


class TestAggregation(unittest.TestCase):
    @staticmethod
    def f(ids, issue, severity="Major", locator="row", expected=None):
        return {"locator": locator, "ids": ids, "issue_type": issue, "severity": severity, "passes": ["R1"],
                "expected_weight": expected}

    def rows(self, n, weight=1):
        return [{"title": f"t{i}", "category": "Outcome", "weight": weight, "justification": "j", "evidence": "e"}
                for i in range(n)]

    def test_rubric_minor_share_bands(self):
        rows = self.rows(20)
        self.assertEqual(br.aggregate("rubric", [self.f(["R1"], "harmless_specificity", "Minor")], rows)["score"], 3)
        three = [self.f([f"R{i}"], "harmless_specificity", "Minor") for i in (1, 2, 3)]
        self.assertEqual(br.aggregate("rubric", three, rows)["verdict"], "FAIL")
        self.assertEqual(br.aggregate("rubric", three[:1], self.rows(30))["score"], 5)

    def test_rubric_severity_from_issue_type(self):
        # the platform table decides: overly_specific is Major whatever the reviewer said
        result = br.aggregate("rubric", [self.f(["R1"], "overly_specific", "Minor")], self.rows(40))
        self.assertEqual(result["verdict"], "FAIL")

    def test_rubric_weights(self):
        rows = self.rows(20)
        one = [self.f(["R1"], "weight", "Minor", expected=3)]
        self.assertEqual(br.aggregate("rubric", one, rows)["dimensions"]["criteria_weights"], 4)
        two = [self.f(["R1"], "weight", "Minor", expected=5)]
        self.assertEqual(br.aggregate("rubric", two, rows)["verdict"], "FAIL")
        many = [self.f([f"R{i}"], "weight", "Minor", expected=3) for i in (1, 2, 3)]
        self.assertEqual(br.aggregate("rubric", many, rows)["verdict"], "FAIL")

    def test_rubric_other_dimensions(self):
        rows = self.rows(20)
        self.assertEqual(br.aggregate("rubric", [self.f([], "missing_process_check", "Minor", "span")],
                                      rows)["score"], 3)
        self.assertEqual(br.aggregate("rubric", [self.f(["R1", "R2"], "predicted_all_fail", "Minor")],
                                      rows)["score"], 2)
        process_only = [dict(r, category="Process") for r in rows]
        self.assertEqual(br.aggregate("rubric", [], process_only)["dimensions"]["category_balance"], 2)
        self.assertEqual(br.aggregate("rubric", [self.f(["S2"], "missing_coverage", "Major", "span")],
                                      rows)["tally"]["major_rows_and_missing_outcomes"], 1)

    def test_prompt_dimensions(self):
        span = "span"
        self.assertEqual(br.aggregate("prompt", [self.f(["S1"], "truthfulness", "Minor", span)])["verdict"], "FAIL")
        self.assertEqual(br.aggregate("prompt", [self.f(["S1"], "clarity", "Minor", span)])["score"], 3)
        self.assertEqual(br.aggregate("prompt", [self.f(["S1"], "business_function", "Major", span)])["score"], 3)
        one = [self.f(["S1"], "cross_service_coherence", "Minor", span)]
        self.assertEqual(br.aggregate("prompt", one)["score"], 3)
        two = one + [self.f(["S2"], "cross_service_coherence", "Minor", span)]
        self.assertEqual(br.aggregate("prompt", two)["verdict"], "FAIL")
        self.assertEqual(br.aggregate("prompt", [self.f(["S1"], "clarity", "UNSURE", span)])["verdict"], "PASS")

    def test_oe_components(self):
        self.assertEqual(br.aggregate("oe", [self.f(["OE 1"], "format", "Major", "event")])["score"], 3)
        self.assertEqual(br.aggregate("oe", [self.f(["OE 1"], "missing_step", "Major", "event")])["verdict"], "FAIL")
        result = br.aggregate("oe", [self.f(["OE 1"], "wrong_qualifier", "Minor", "event")])
        self.assertEqual(result["dimensions"], {"completeness": 5, "accuracy": 3})


class TestCli(unittest.TestCase):
    def run_main(self, argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            try:
                code = br.main(argv)
            except SystemExit as exc:
                code = exc.code
        return code, out.getvalue()

    def test_usage_errors(self):
        self.assertEqual(self.run_main([])[0], 2)
        self.assertEqual(self.run_main(["plan", "--task-dir", "/nonexistent-folder", "--stage", "oe"])[0], 2)
        self.assertEqual(self.run_main(["plan", "--task-dir", ".", "--stage", "golden"])[0], 2)

    def test_plan_error_is_a_fail(self):
        with selftest_sandbox.scratch_tmp("test_blind_review_cli_") as tmp:
            code, out = self.run_main(["plan", "--task-dir", tmp, "--stage", "prompt"])
        self.assertEqual(code, 1)
        self.assertTrue(out.startswith("BLIND REVIEW PLAN (prompt): FAIL"))

    def test_self_test(self):
        code, out = self.run_main(["--self-test"])
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("self-test: ok"))


if __name__ == "__main__":
    unittest.main()

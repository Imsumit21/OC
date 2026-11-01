"""Tests for the /create-goal generator (skills/create-goal/scripts/build_goal.py).

Unit tests compose goals from fixture contexts; a drift test checks every phrase goal_rules.json cites against the real
sources; CLI tests run the script on scratch task folders under Task_Authoring/support/scratch/ (GEN_EXECUTION § 1),
removed afterwards. Nothing is written to a real task folder.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.dont_write_bytecode = True
BUNDLE = Path(__file__).resolve().parents[1]
SCRIPT = BUNDLE / "skills" / "create-goal" / "scripts" / "build_goal.py"
SCRATCH = BUNDLE / "support" / "scratch"
GUIDE = "Task_Authoring/references/Docs/13_Hardness_v2_Opus55.md"
_SPEC = importlib.util.spec_from_file_location("build_goal", SCRIPT)
G = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(G)

DATE_BLOCK = "📅 Universe Date\nFebruary 14, 2026 00:00\n"
ASSIGNMENT = ("# Task Assigned Inputs — V3\n\n## Platform assignment\n\n```text\n"
              "🏢 Business Function\nExecutive\n\n🧑 Persona\nLeonard Hayes\nRole: Co-founder & Creative Director\n\n"
              "🎯 Competency\nCorporate Ops\n\n🛠️ Task Skill\nAuthoring\n\n📋 Task Type\nlong horizon\n\n"
              "🎚️ Difficulty Mode\nhard\n\n" + DATE_BLOCK + "```\n")
UNIVERSES = {
    "normal": {"key": "normal", "label": "Feb 14, 2026 (normal)", "persona_today": "2026-02-14",
               "persona_today_weekday": "Saturday"},
    "synthcut": {"key": "synthcut", "label": "Oct 1, 2025 (synth-cut)", "persona_today": "2025-10-01",
                 "persona_today_weekday": "Wednesday"},
}
STORE_LINE = "it holds another task dated Oct 1, 2025 (synth-cut)"


def context(skill="Authoring", mode="hard", cap=0.7, horizon="Long Horizon", universe="normal",
            function="Executive", competency="Corporate Ops"):
    return {"persona_name": "Leonard Hayes", "persona_role": "Co-founder & Creative Director",
            "business_function": function, "competency": competency, "task_skill": skill, "horizon": horizon,
            "difficulty_mode": mode, "difficulty_cap": cap, "universe": dict(UNIVERSES[universe]),
            "context_hash": "0" * 64}


def sibling(folder, first, universe, slug, competency="Finance"):
    return {"folder": folder, "ctx": {"persona_name": first}, "how": "recomputed", "slug": slug, "first": first,
            "universe": universe, "competency": competency}


def scratch_dir(prefix):
    SCRATCH.mkdir(parents=True, exist_ok=True)
    return Path(tempfile.mkdtemp(prefix=prefix, dir=SCRATCH)).resolve()


class ComposeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = scratch_dir("create-goal-")
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.task = self.tmp / "task"
        self.task.mkdir()
        self.rules = G.load_rules()
        self.siblings = [sibling(self.tmp / "robert", "Robert", "normal", "robert-vendor-schedule"),
                         sibling(self.tmp / "julia", "Julia", "synthcut", "dd-2025-closeout")]

    def goal(self, ctx, *, store_line=STORE_LINE, default=None, notes=(), rules=None):
        rules = rules or self.rules
        with mock.patch.object(G, "DEFAULT_TASK", default or self.tmp / "default"):
            goal, generated, values, warnings, _ = G.compose(
                ctx, rules, task_dir=self.task, siblings=self.siblings, store_line=store_line,
                analysis=(None, None), learnings_n=44, default_owner="Robert's task", analysis_exists=False,
                notes=list(notes))
            problems, more = G.self_check(goal, generated, values, rules, task_dir=self.task,
                                          siblings=self.siblings, store_line=store_line,
                                          extreme=ctx["horizon"] == "Long Horizon")
        return goal, problems, warnings + more

    def test_long_hard_authoring_goal(self):
        goal, problems, _ = self.goal(context())
        self.assertEqual(problems, [])
        for text in ("TASK_AUTHORING_TASK_DIR", "Leave the Evals input store alone", "< 70 %", "E[avg] ≤ 62 %",
                     "≥ 4 independent loss channels", "volume exception", "Saturday 14 Feb", "≥ 100 counted calls",
                     "Robert's (robert-vendor-schedule)", "a real document, sheet, deck or email",
                     "Founders / Exec / Strategy", "fundraising, board, legal/contracts, vendor, HR",
                     "learnings (§1–44)", "Then stop and tell me to run /create-scenario.",
                     f"from the trap types in the hardness guide {GUIDE} (not its worked examples",
                     "the convincing wrong source and the record that beats it", "same-thread corrections don't work",
                     "weight 5 by kind of work, never raised", "the failure-pattern and SD gates fail",
                     "hardness (with the guide's Part 7 checks) and volume plans",
                     "confirm the agent's tools return it"):
            self.assertIn(text, goal)
        self.assertNotIn("dd-2025-closeout", goal)            # another universe's design is not a storyline to avoid
        self.assertNotIn("{", goal)
        self.assertTrue(goal.startswith("/goal "))
        self.assertLessEqual(G.word_count(goal), self.rules["limits"]["max_words"])

    def test_default_folder_and_matching_store_drop_their_lines(self):
        goal, problems, _ = self.goal(context(), store_line=None, default=self.task)
        self.assertEqual(problems, [])
        self.assertNotIn("TASK_AUTHORING_TASK_DIR", goal)
        self.assertNotIn("Evals input store", goal)

    def test_planning_medium_normal_horizon_synthcut(self):
        ctx = context(skill="Planning and decision support", mode="medium", cap=0.85, horizon="Normal Horizon",
                      universe="synthcut", function="Product", competency="Product Management")
        goal, problems, _ = self.goal(ctx)
        self.assertEqual(problems, [])
        for text in ("< 85 %", "E[avg] ≤ 77 %", "≥ 3 independent loss channels", "50–100 counted calls",
                     "Wednesday 1 Oct", "recommend a course of action", "Product & Design",
                     "Julia's (dd-2025-closeout)"):
            self.assertIn(text, goal)
        self.assertNotIn("volume exception", goal)
        self.assertNotIn("robert-vendor-schedule", goal)

    def test_easy_actions_engineering(self):
        goal, problems, _ = self.goal(context(skill="Actions", mode="easy", cap=0.9, function="Engineering",
                                              competency="Engineering Ops"))
        self.assertEqual(problems, [])
        for text in ("< 90 %", "E[avg] ≤ 82 %", "act versus defer", "Engineering & Live-Ops"):
            self.assertIn(text, goal)

    def test_every_skill_function_and_competency_composes_within_the_ceiling(self):
        for skill in self.rules["skills"]:
            for function in self.rules["functions"]:
                for competency in self.rules["competencies"]:
                    with self.subTest(skill=skill, function=function, competency=competency):
                        goal, problems, _ = self.goal(context(skill=skill, function=function,
                                                              competency=competency))
                        self.assertEqual(problems, [])

    def test_unknown_skill_stops_with_code_3(self):
        with self.assertRaises(G.Stop) as caught:
            self.goal(context(skill="Juggling"))
        self.assertEqual(caught.exception.code, 3)

    def test_missing_required_evidence_stops(self):
        rules = copy.deepcopy(self.rules)
        rules["lines"]["rule_injection"]["evidence"].append(
            {"path": "learnings", "contains": "no such phrase 7f3a", "kind": "lesson"})
        with self.assertRaises(G.Stop) as caught:
            self.goal(context(), rules=rules)
        self.assertEqual(caught.exception.code, 3)
        self.assertIn("rule_injection", str(caught.exception))

    def test_missing_hardness_guide_stops_with_code_3(self):
        rules = copy.deepcopy(self.rules)
        for item in rules["lines"]["v2_traps"]["evidence"]:       # as if the guide were renamed or deleted
            item["path"] = "Task_Authoring/references/Docs/no_such_guide_7f3a.md"
        with self.assertRaises(G.Stop) as caught:
            self.goal(context(), rules=rules)
        self.assertEqual(caught.exception.code, 3)
        self.assertIn("v2_traps", str(caught.exception))

    def test_an_optional_line_with_missing_evidence_is_dropped_with_a_warning(self):
        rules = copy.deepcopy(self.rules)
        rules["lines"]["v2_checks"]["optional"] = True
        rules["lines"]["v2_checks"]["evidence"].append({"path": "learnings", "contains": "no such phrase 7f3a",
                                                        "kind": "lesson"})
        goal, problems, warnings = self.goal(context(), rules=rules)
        self.assertEqual(problems, [])
        self.assertIn("the UGT, hardness and volume plans", goal)
        self.assertEqual(len([w for w in warnings if "dropped" in w and "'v2_checks'" in w]), 1, warnings)

    def test_field_names_with_digits_are_filled_and_leftovers_are_caught(self):
        self.assertEqual(G.fill("a {v2_x} b", {"v2_x": "Y"}), "a Y b")
        with mock.patch.object(G, "DEFAULT_TASK", self.task):
            problems, _ = G.self_check("x {V2_x} y {a-b}", "x {V2_x} y {a-b}", {}, self.rules, task_dir=self.task,
                                       siblings=[], store_line=None, extreme=False)
        self.assertTrue(any("{V2_x}" in p and "{a-b}" in p for p in problems), problems)

    def test_notes_are_appended_verbatim_and_exempt_from_the_pronoun_and_field_checks(self):
        note = "skip red team and methodology; record the waiver in his notes {as given}"
        goal, problems, _ = self.goal(context(), notes=[note])
        self.assertEqual(problems, [])
        self.assertTrue(goal.endswith("Also: " + note))

    def test_self_check_flags_tokens_pronouns_missing_paths_and_length(self):
        bad = "/goal {persona} he reads Task_Authoring/no_such_file.md " + "word " * 600
        with mock.patch.object(G, "DEFAULT_TASK", self.task):
            problems, _ = G.self_check(bad, bad, {}, self.rules, task_dir=self.task, siblings=[], store_line=None,
                                       extreme=False)
        text = " | ".join(problems)
        for part in ("ceiling", "unresolved template fields", "pronoun", "does not exist"):
            self.assertIn(part, text)

    def test_self_check_flags_conditional_lines_that_should_be_absent(self):
        goal, _, _ = self.goal(context())
        with mock.patch.object(G, "DEFAULT_TASK", self.task):        # the folder is now the default one
            problems, _ = G.self_check(goal, goal, {}, self.rules, task_dir=self.task, siblings=[],
                                       store_line=None, extreme=False)
        text = " | ".join(problems)
        for part in ("TASK_AUTHORING_TASK_DIR line present", "Evals store line present", "volume decision present"):
            self.assertIn(part, text)

    def test_word_count_ignores_symbols(self):
        self.assertEqual(G.word_count("a · b < 70 % ≥ 2 §1–44 /goal"), 6)

    def test_at_most_three_siblings_are_named(self):
        self.siblings = [sibling(self.tmp / f"s{i}", f"P{i}", "normal", f"slug-{i}") for i in range(5)]
        goal, problems, _ = self.goal(context())
        self.assertEqual(problems, [])
        self.assertIn("P0's (slug-0), P1's (slug-1), P2's (slug-2) and 2 more task folders", goal)

    def test_same_competency_siblings_are_named_first(self):
        self.siblings = [sibling(self.tmp / "a", "Ann", "normal", "a-design"),
                         sibling(self.tmp / "b", "Bo", "normal", "b-design", competency="Corporate Ops")]
        goal, _, _ = self.goal(context())
        self.assertIn("Bo's (b-design) and Ann's (a-design)", goal)

    def test_siblings_without_a_design_are_not_named(self):
        self.siblings = [sibling(self.tmp / "a", "Ann", "normal", None), sibling(self.tmp / "b", "Bo", "normal", "b-design")]
        goal, problems, _ = self.goal(context())
        self.assertEqual(problems, [])
        self.assertIn("2–3 storylines distinct from Bo's (b-design) with a recommendation", goal)
        self.assertNotIn("Ann", goal)

    def test_a_path_with_spaces_counts_as_one_word(self):
        self.assertEqual(G.word_count(G.without_paths("a /x y/z b", {"task_abs": "/x y/z"})), 3)

    def test_a_missing_default_folder_is_named_but_not_required(self):
        goal, problems, _ = self.goal(context())             # the mocked default folder does not exist
        self.assertEqual(problems, [])
        self.assertIn(f"Tools default to {G.rel(self.tmp / 'default')}/ (Robert's task)", goal)
        self.assertNotIn("Task_Authoring/task_inputs/", goal)

    def test_the_default_folder_is_described_by_what_is_there(self):
        default = self.tmp / "default"
        robert = sibling(default, "Robert", "normal", "robert-vendor-schedule")
        with mock.patch.object(G, "DEFAULT_TASK", default):
            self.assertEqual(G.describe_default([]), "not present")
            default.mkdir()
            self.assertEqual(G.describe_default([]), "another task")
            self.assertEqual(G.describe_default([robert]), "Robert's task")

    def test_long_notes_warn_but_do_not_fail(self):
        goal, problems, warnings = self.goal(context(), notes=["decision " * 120])
        self.assertEqual(problems, [])
        self.assertTrue(any("with the notes" in w for w in warnings), warnings)


class StoreTests(unittest.TestCase):
    SHA = "a" * 64

    def store(self, *, state="saved", sha=SHA, integrity="OK", intake="SELECTED", key="normal",
              label="Feb 14, 2026 (normal)"):
        files = [{"sha256": sha, "integrity": integrity}] if state == "saved" else []
        return {"universe_intake": {"state": intake, "key": key, "label": label},
                "inputs": {"task-details": {"state": state, "files": files}}}

    def test_store_states(self):
        other = {"key": "synthcut", "label": "Oct 1, 2025 (synth-cut)"}
        cases = [
            (self.store(), None),
            (self.store(**other), "its task date is Oct 1, 2025 (synth-cut)"),
            (self.store(sha="b" * 64, **other), "it holds another task dated Oct 1, 2025 (synth-cut)"),
            (self.store(integrity="CHANGED"),
             "its saved task details are changed or missing; its task date is Feb 14, 2026 (normal)"),
            (self.store(state="cleared"), "it holds no task details; its task date is Feb 14, 2026 (normal)"),
            (self.store(intake="ASK", label=None), "it has no task date selected"),
            (None, "its state could not be read"),
            (dict(self.store(state="absent"), unindexed_local_inputs={"task-details": {"sha256": self.SHA}}),
             "it holds this task's details, not indexed; its task date is Feb 14, 2026 (normal)"),
            (dict(self.store(state="absent"), unindexed_local_inputs={"task-details": {"sha256": "b" * 64}}),
             "it holds another task's details, not indexed; its task date is Feb 14, 2026 (normal)"),
        ]
        for store, expected in cases:
            with self.subTest(expected=expected):
                self.assertEqual(G.store_holds(store, context(), self.SHA)[0], expected)


class SourceDriftTests(unittest.TestCase):
    """Every phrase goal_rules.json cites must still exist in its source (a presence check, not a semantic one)."""

    def entries(self):
        rules = G.load_rules()
        for table in ("lines", "skills", "functions", "competencies"):
            for key, entry in rules[table].items():
                yield f"{table}.{key}", entry

    def test_every_cited_phrase_exists(self):
        for name, entry in self.entries():
            for item in entry.get("evidence", []):
                with self.subTest(entry=name, phrase=item["contains"][:50]):
                    self.assertEqual(G.missing_evidence({"evidence": [item]}), [])

    def test_evidence_entries_are_well_formed(self):
        kinds = {"learnings": "lesson", GUIDE: "guideline"}
        for name, entry in self.entries():
            for item in entry.get("evidence", []):
                with self.subTest(entry=name, path=item.get("path")):
                    self.assertFalse(Path(item["path"]).is_absolute())
                    self.assertTrue(item["contains"].strip())
                    self.assertEqual(item["kind"], kinds.get(item["path"], "authority"))

    def test_the_guide_lives_in_the_tracked_bundle_and_its_lines_are_required(self):
        cited = [(name, entry) for name, entry in self.entries()
                 if any(item["kind"] == "guideline" for item in entry.get("evidence", []))]
        self.assertTrue(cited)
        for name, entry in cited:
            with self.subTest(entry=name):
                self.assertFalse(entry.get("optional"))
                for item in entry["evidence"]:
                    self.assertTrue(item["path"].startswith("Task_Authoring/references/Docs/"), item["path"])
                    self.assertTrue((G.WS / item["path"]).is_file(), item["path"])


class CliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = scratch_dir("create-goal-cli-")
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.task = self.tmp / "task"
        self.task.mkdir()
        (self.task / "00_Assigments.md").write_text(ASSIGNMENT, encoding="utf-8")

    def cli(self, *args):
        env = {k: v for k, v in os.environ.items() if k != "TASK_AUTHORING_TASK_DIR"}
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        return subprocess.run([sys.executable, "-B", str(SCRIPT), *args], cwd=BUNDLE.parent, env=env,
                              capture_output=True, text=True, timeout=600)

    def test_stdout_only_writes_nothing(self):
        before = sorted(p.name for p in self.task.rglob("*"))
        result = self.cli("--task-dir", str(self.task), "--stdout-only")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(result.stdout.startswith("/goal "))
        self.assertIn("CREATE-GOAL: PASS · stdout only", result.stdout)
        self.assertEqual(sorted(p.name for p in self.task.rglob("*")), before)

    def test_writes_the_goal_file_atomically(self):
        result = self.cli("--task-dir", str(self.task), "--note", "skip red team and methodology")
        self.assertEqual(result.returncode, 0, result.stderr)
        out = self.task / "Working_Files" / "00_Session_Goal.md"
        text = out.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Session goal — Leonard Hayes"))
        self.assertIn("```text\n/goal ", text)
        self.assertIn("Also: skip red team and methodology", text)
        self.assertEqual([p.name for p in out.parent.iterdir()], ["00_Session_Goal.md"])
        facts = json.loads(next(line for line in result.stdout.splitlines() if line.startswith("FACTS "))[6:])
        self.assertEqual(facts["output"], G.rel(out))
        self.assertFalse(facts["default_folder"])
        self.assertEqual(facts["notes"], ["skip red team and methodology"])

    def test_other_work_in_the_folder_is_reported(self):
        (self.task / "Working_Files" / "research").mkdir(parents=True)
        result = self.cli("--task-dir", str(self.task), "--stdout-only")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("WARN Working_Files already holds research/: another session may be working", result.stdout)
        facts = json.loads(next(line for line in result.stdout.splitlines() if line.startswith("FACTS "))[6:])
        self.assertEqual(facts["other_work_in_folder"], ["research/"])
        self.assertEqual(sorted(p.name for p in (self.task / "Working_Files").iterdir()), ["research"])

    def test_notes_are_kept_verbatim_through_the_cli(self):
        note = "keep  `two  spaces`  as given"
        result = self.cli("--task-dir", str(self.task), "--stdout-only", "--note", note)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("\nAlso: " + note + "\n", result.stdout)
        self.assertEqual(self.cli("--task-dir", str(self.task), "--stdout-only", "--note", "  ").returncode, 6)

    def test_multiline_note_with_fences_stays_inside_the_copy_block(self):
        note = "keep this block:\n````\ncode\n````\n```text\nmore\n```"
        result = self.cli("--task-dir", str(self.task), "--note", note)
        self.assertEqual(result.returncode, 0, result.stderr)
        text = (self.task / "Working_Files" / "00_Session_Goal.md").read_text(encoding="utf-8")
        opening = next(line for line in text.splitlines() if line.startswith("`"))
        self.assertEqual(opening, "`````text")
        body = text.split(opening + "\n", 1)[1]
        self.assertTrue(body.endswith("\n`````\n"))
        expected = ("Also: " + note).splitlines()
        self.assertEqual(body[:-len("\n`````\n")].splitlines()[-len(expected):], expected)
        self.assertEqual(body.count("\n`````"), 1)

    def test_task_folder_with_spaces(self):
        spaced = self.tmp / "task with spaces"
        spaced.mkdir()
        (spaced / "00_Assigments.md").write_text(ASSIGNMENT, encoding="utf-8")
        result = self.cli("--task-dir", str(spaced), "--stdout-only")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("--task-dir " + shlex.quote(G.rel(spaced)) + " --write", result.stdout)

    def test_output_that_is_a_directory_stops_with_6(self):
        out = self.task / "Working_Files" / "00_Session_Goal.md"
        out.mkdir(parents=True)
        result = self.cli("--task-dir", str(self.task))
        self.assertEqual(result.returncode, 6, result.stdout + result.stderr)
        self.assertTrue(out.is_dir())
        self.assertEqual([p.name for p in out.parent.iterdir()], ["00_Session_Goal.md"])

    def test_symlinked_output_is_refused(self):
        target = self.tmp / "elsewhere.md"
        target.write_text("keep", encoding="utf-8")
        (self.task / "Working_Files").mkdir()
        (self.task / "Working_Files" / "00_Session_Goal.md").symlink_to(target)
        result = self.cli("--task-dir", str(self.task))
        self.assertEqual(result.returncode, 6, result.stdout + result.stderr)
        self.assertEqual(target.read_text(encoding="utf-8"), "keep")

    def test_replace_failure_becomes_exit_6_and_leaves_no_temp_file(self):
        with mock.patch.object(G.os, "replace", side_effect=OSError(28, "No space left on device")):
            with self.assertRaises(G.Stop) as caught:
                G.write_output(self.task, "x")
        self.assertEqual(caught.exception.code, 6)
        self.assertIn("No space left on device", str(caught.exception))
        self.assertEqual(list((self.task / "Working_Files").iterdir()), [])

    def test_unreadable_sibling_context_is_skipped_not_fatal(self):
        sib = self.tmp / "sibling"
        (sib / "Working_Files").mkdir(parents=True)
        (sib / "00_Assigments.md").write_text("no assignment here\n", encoding="utf-8")
        (sib / "Working_Files" / "00_Task_Context.json").write_text('{"persona_name": "X"}', encoding="utf-8")
        self.assertEqual(G.sibling_context(sib), (None, "unreadable"))

    def test_existing_design_is_refused(self):
        (self.task / "Working_Files").mkdir()
        (self.task / "Working_Files" / "01_Scenario_Design.md").write_text("# Scenario Design — x · design only\n")
        result = self.cli("--task-dir", str(self.task), "--stdout-only")
        self.assertEqual(result.returncode, 4, result.stderr)
        self.assertIn("/create-hardening (MODE B) then /create-scenario --revise", result.stderr)

    def test_missing_date_stops_without_a_default(self):
        (self.task / "00_Assigments.md").write_text(ASSIGNMENT.replace(DATE_BLOCK, ""), encoding="utf-8")
        result = self.cli("--task-dir", str(self.task), "--stdout-only")
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertNotIn("/goal", result.stdout)

    def test_symlinked_working_files_is_refused(self):
        target = self.tmp / "elsewhere"
        target.mkdir()
        (self.task / "Working_Files").symlink_to(target, target_is_directory=True)
        result = self.cli("--task-dir", str(self.task))
        self.assertEqual(result.returncode, 6, result.stdout + result.stderr)
        self.assertEqual(list(target.iterdir()), [])

    def test_folder_outside_task_authoring_is_refused(self):
        result = self.cli("--task-dir", str(BUNDLE.parent / "Evals"), "--stdout-only")
        self.assertEqual(result.returncode, 6, result.stdout + result.stderr)

    def test_helpers_run_without_bytecode_or_an_inherited_task_dir(self):
        calls = []

        def fake_run(cmd, **kwargs):
            calls.append((cmd, kwargs.get("env") or {}))
            return subprocess.CompletedProcess(cmd, 0, "{}", "")

        with mock.patch.dict(os.environ, {"TASK_AUTHORING_TASK_DIR": str(self.task)}), \
                mock.patch.object(G.subprocess, "run", side_effect=fake_run):
            G.read_store()
        command, env = calls[0]
        self.assertEqual(command[1], "-B")
        self.assertEqual(env.get("PYTHONDONTWRITEBYTECODE"), "1")
        self.assertNotIn("TASK_AUTHORING_TASK_DIR", env)


if __name__ == "__main__":
    unittest.main()

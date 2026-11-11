"""Unit tests for assignment_fit.py. They run on the stub universe and need no base data.

  cd Task_Authoring/tools && python3.12 -B -m unittest test_assignment_fit

The four backtest outcomes the plan asks for (WS9) are checked on the real universes only when
ASSIGNMENT_FIT_REAL=1 is set, because the first read of a universe builds caches.
"""
from __future__ import annotations

import contextlib
import copy
import io
import json
import os
import re
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import assignment_fit as af  # noqa: E402
import selftest_sandbox  # noqa: E402
import task_context as tc  # noqa: E402

HEADER = re.compile(r"^ASSIGNMENT FIT \(.+, (normal|synthcut)\): (FIT|FIT WITH LIMITS|NO NATURAL COHORT)$")
CHECK = re.compile(r"^\[(PASS|WARN|FAIL)\] fit\.census: .+")


def source(mutate=None) -> af.StubSource:
    data = af.stub_data()
    if mutate:
        mutate(data)
    return af.StubSource(data)


def run(src, key, competency, horizon="long-horizon", function="Product"):
    return af.census(src, src.persona(key), function, competency, horizon, "medium", tasks=[])


class Verdicts(unittest.TestCase):
    def test_fit(self):
        fit = run(source(), "vincent_parker", "Engineering Ops")
        self.assertEqual(fit["fit"], af.FIT)
        self.assertEqual(fit["limits"], [])
        self.assertFalse(fit["open_population"])
        self.assertTrue(all(c["closed"] and not c["dormant"] and c["counts"] for c in fit["candidates"]))

    def test_fit_with_limits_names_gmail(self):
        fit = run(source(), "julia_lawson", "Engineering Ops")
        self.assertEqual(fit["fit"], af.LIMITS)
        self.assertEqual(fit["thin_services"], ["gmail"])
        self.assertIn("Gmail is thin: no anchor or variance unit there", fit["limits"][0])
        self.assertIn("253 threads, 11 sent, last sent 2024-04-17", fit["limits"][0])

    def test_no_natural_cohort_routes_to_injection(self):
        fit = run(source(), "julia_lawson", "Marketing and GTM")
        self.assertEqual(fit["fit"], af.NO_COHORT)
        self.assertTrue(fit["open_population"])
        self.assertEqual(fit["candidates"], [])
        self.assertIn("injection", fit["route"])
        text = af.render(af.wrap(fit))
        self.assertNotIn("skip", text.casefold())

    def test_normal_horizon_uses_the_smaller_cohort(self):
        long = run(source(), "julia_lawson", "Marketing and GTM", "long-horizon")
        normal = run(source(), "julia_lawson", "Marketing and GTM", "normal")
        self.assertEqual(long["thresholds"]["cohort_min"], 40)
        self.assertEqual(normal["thresholds"]["cohort_min"], 10)
        self.assertEqual(long["fit"], af.NO_COHORT)
        self.assertEqual(normal["candidates"][0]["name"], "UA campaign calendar / Sheet1")

    def test_unknown_inputs_are_refused(self):
        src = source()
        with self.assertRaises(af.FitError):
            run(src, "julia_lawson", "Astrology")
        with self.assertRaises(af.FitError):
            run(src, "julia_lawson", "Finance", horizon="super-long")
        with self.assertRaises(af.FitError):
            src.persona("nobody")


class ThinRule(unittest.TestCase):
    def test_minimum_comes_from_the_policy(self):
        policy = json.loads(af.POLICY.read_text())
        self.assertEqual(af.thin_min(), policy["path_exposure"]["thin_search_min_results"])

    def test_gmail_boundary(self):
        minimum = af.thin_min()
        for recent, thin in ((minimum - 1, True), (minimum, False)):
            src = source(lambda d: d["gmail"]["julia_lawson"].update(recent_threads=recent))
            table = af.reach_table(src, src.persona("julia_lawson"), minimum)
            self.assertEqual(table["gmail"]["thin"], thin, recent)

    def test_calendar_and_slack_use_the_window_count(self):
        src = source(lambda d: d["recent"]["vincent_parker"].update(gcal=3, slack=0))
        table = af.reach_table(src, src.persona("vincent_parker"), 10)
        self.assertTrue(table["gcal"]["thin"])
        self.assertTrue(table["slack"]["thin"])
        self.assertIn("3 events dated in the 90 days before the clock (minimum 10)", table["gcal"]["why"])

    def test_drive_is_thin_by_volume(self):
        def few(d):
            d["reach"]["julia_lawson"]["services"]["drive"].update(owned_total=2, shared_with_total=7)
        src = source(few)
        table = af.reach_table(src, src.persona("julia_lawson"), 10)
        self.assertTrue(table["drive"]["thin"])
        self.assertEqual(table["drive"]["rank"], 3)
        fit = run(src, "julia_lawson", "Engineering Ops")
        self.assertEqual(fit["thin_services"], ["gmail", "drive"])
        self.assertEqual(len(fit["limits"]), 2)

    def test_borderline_and_window_counts(self):
        def windows(d):
            d["gmail"]["julia_lawson"].update(windows={"30": 1, "90": 9, "180": 18})
        src = source(windows)
        table = af.reach_table(src, src.persona("julia_lawson"), 10)
        self.assertTrue(table["gmail"]["thin"] and table["gmail"]["borderline"])
        self.assertIn("borderline", table["gmail"]["why"])
        limit = af.thin_limit("gmail", table["gmail"])
        self.assertIn("1 in 30 days, 18 in 180 days", limit)
        self.assertNotIn("9 in 90 days", limit)
        far = source(lambda d: d["gmail"]["julia_lawson"].update(recent_threads=2))
        self.assertFalse(af.reach_table(far, far.persona("julia_lawson"), 10)["gmail"]["borderline"])

    def test_rank_is_one_plus_the_number_above(self):
        src = source()
        table = af.reach_table(src, src.persona("leonard_hayes"), 10)
        self.assertEqual([table[s]["rank"] for s in af.SCOPED], [1, 1, 1, 1])
        self.assertEqual(table["gmail"]["of"], 3)


class Candidates(unittest.TestCase):
    def board(self, **changes):
        def mutate(d):
            d["collections"]["trello_boards"][0].update(changes)
        return source(mutate)

    def test_size_boundary(self):
        live = "2025-09-01"
        at = run(self.board(size=40, last_activity=live), "julia_lawson", "Marketing and GTM")
        below = run(self.board(size=39, last_activity=live), "julia_lawson", "Marketing and GTM")
        self.assertEqual([c["name"] for c in at["candidates"]], ["UA/BD"])
        self.assertEqual(at["fit"], af.LIMITS)
        self.assertEqual(below["fit"], af.NO_COHORT)
        self.assertIn("UA/BD", [c["name"] for c in below["near_misses"]])

    def test_dormant_boundary(self):
        clock = af._parse(af.stub_data()["clock"])
        edge = (clock - af.dt.timedelta(days=af.ACTIVE_WINDOW_DAYS)).date().isoformat()
        past = (clock - af.dt.timedelta(days=af.ACTIVE_WINDOW_DAYS + 2)).date().isoformat()
        self.assertEqual(run(self.board(last_activity=edge), "julia_lawson", "Marketing and GTM")["fit"], af.LIMITS)
        fit = run(self.board(last_activity=past), "julia_lawson", "Marketing and GTM")
        self.assertEqual(fit["fit"], af.NO_COHORT)
        self.assertEqual({c["name"]: c["not_counted_because"] for c in fit["listed_not_counted"]}["UA/BD"], "dormant")

    def test_a_collection_with_no_date_is_dormant(self):
        fit = run(self.board(last_activity=None), "julia_lawson", "Marketing and GTM")
        self.assertEqual(fit["fit"], af.NO_COHORT)

    def test_slack_channel_is_an_open_rule(self):
        fit = run(source(), "julia_lawson", "Marketing and GTM")
        channel = [c for c in fit["listed_not_counted"] if c["kind"] == "slack_channel"][0]
        self.assertFalse(channel["closed"])
        self.assertEqual(channel["not_counted_because"], "open rule")
        self.assertTrue(any("open rule" in g for g in channel["gaps"]))

    def test_channel_needs_membership_and_dms_are_not_cohorts(self):
        fit = run(source(), "vincent_parker", "Marketing and GTM")
        self.assertNotIn("zombie_marketing", [c["name"] for c in fit["listed_not_counted"]])

        def rename(d):
            d["collections"]["slack_channels"][2]["name"] = "marketing"
        fit = run(source(rename), "julia_lawson", "Marketing and GTM")
        self.assertNotIn("marketing", [c["name"] for c in fit["listed_not_counted"] + fit["candidates"]])

    def test_sheet_needs_drive_access(self):
        self.assertEqual(run(source(), "leonard_hayes", "Finance")["fit"], af.FIT)
        self.assertEqual(run(source(), "vincent_parker", "Finance")["fit"], af.NO_COHORT)

    def test_container_scale_sorts_after_cohort_scale(self):
        fit = run(source(), "vincent_parker", "Engineering Ops")
        scales = [c["scale"] for c in fit["candidates"]]
        self.assertEqual(scales, sorted(scales, key=lambda s: s != "cohort"))
        self.assertEqual(fit["candidates"][-1]["name"], "Zombie Match 3D")
        self.assertEqual(fit["candidates"][-1]["size"], 553)

    def test_gaps_come_from_the_surface_counts(self):
        def people_comments(d):
            d["surface"]["linear"]["comments"].update(count=50, people=50, automated=0)
            d["surface"]["github"]["pull_request_comments"].update(count=100, people=90, automated=10)
        fit = run(source(people_comments), "vincent_parker", "Engineering Ops")
        gaps = [g for c in fit["candidates"] for g in c["gaps"]]
        self.assertFalse(any("Linear comments" in g or "PR conversation comments" in g for g in gaps))
        gaps = [g for c in run(source(), "vincent_parker", "Engineering Ops")["candidates"] for g in c["gaps"]]
        self.assertTrue(any("Linear comments: none in base" in g for g in gaps))

    def test_a_tab_named_for_past_years_is_dormant(self):
        self.assertEqual(af.named_period("20232024")[0], "2023-2024")
        self.assertEqual(af.named_period("Lines", "Budget 2024")[0], "2024")
        self.assertEqual(af.named_period("Q4 plan", "No year here"), (None, None))
        self.assertEqual(af.named_period("game 12025 build")[0], None)

        def past(d):
            d["collections"]["sheet_tabs"][0].update(tab="20232024", name="Budget / 20232024")
        fit = run(source(past), "leonard_hayes", "Finance")
        self.assertEqual(fit["fit"], af.NO_COHORT)
        tab = [c for c in fit["listed_not_counted"] if c["key"] == "f_budget#0"][0]
        self.assertTrue(tab["dormant"])
        self.assertIn("named for 2023-2024", tab["dormant_why"])
        self.assertIn("edited 2025-09-20", tab["not_counted_detail"])

        def current(d):
            d["collections"]["sheet_tabs"][0].update(tab="2025 lines", name="Budget / 2025 lines")
        self.assertEqual(run(source(current), "leonard_hayes", "Finance")["fit"], af.FIT)

    def test_a_retired_name_is_dormant(self):
        self.assertEqual(af.retired_mark("Achievements", "OLD DO NOT USE Zombie Quests"), "do not use")
        self.assertIsNone(af.retired_mark("Lines", "Budget 2026"))
        self.assertIsNone(af.retired_mark("Archivist notes"))

        def retired(d):
            d["collections"]["sheet_tabs"][0].update(sheet="OLD DO NOT USE Budget", name="OLD DO NOT USE Budget / Lines")
        fit = run(source(retired), "leonard_hayes", "Finance")
        self.assertEqual(fit["fit"], af.NO_COHORT)
        tab = [c for c in fit["listed_not_counted"] if c["key"] == "f_budget#0"][0]
        self.assertIn("its name retires it ('do not use'", tab["dormant_why"])

    def test_open_rule_reason_is_spelled_out(self):
        fit = run(source(), "julia_lawson", "Marketing and GTM")
        channel = [c for c in fit["listed_not_counted"] if c["kind"] == "slack_channel"][0]
        self.assertIn("search-sweepable", channel["not_counted_detail"])

    def test_empty_collection_is_never_listed(self):
        fit = run(source(), "julia_lawson", "Marketing and GTM")
        names = [c["name"] for c in fit["candidates"] + fit["listed_not_counted"] + fit["near_misses"]]
        self.assertNotIn("website", names)


class Matching(unittest.TestCase):
    def test_keywords_match_whole_words(self):
        self.assertIsNone(af.keyword_hit("january-quality", ["ua", "qa"]))
        self.assertEqual(af.keyword_hit("UA/BD", ["ua"]), "ua")
        self.assertEqual(af.keyword_hit("zombie_marketing", ["marketing"]), "marketing")
        self.assertEqual(af.keyword_hit("Push Notifications Zombie Match", ["push notification*"]), "push notification*")
        self.assertIsNone(af.keyword_hit("Notifications push", ["push notification*"]))
        self.assertEqual(af.keyword_hit("P&L and forecast", ["p l"]), "p l")
        self.assertIsNone(af.keyword_hit("", ["ua"]))

    def test_competency_aliases(self):
        data = af.load_competencies()
        for label in ("Marketing and GTM", "Marketing & GTM", "marketing-gtm", "MARKETING GTM"):
            self.assertEqual(af.competency_entry(label, data)[0], "Marketing and GTM", label)
        self.assertEqual(af.competency_entry("engineering ops", data)[0], "Engineering Ops")
        with self.assertRaises(af.FitError):
            af.competency_entry("Sales", data)

    def test_map_covers_the_five_competencies(self):
        data = af.load_competencies()
        self.assertEqual(sorted(data["competencies"]),
                         ["Corporate Ops", "Engineering Ops", "Finance", "Marketing and GTM", "Product Management"])
        kinds = set(data["kinds"])
        for name, entry in data["competencies"].items():
            used = set(entry.get("all_of_kind") or []) | set(entry.get("keyword_kinds") or []) | set(entry.get("named") or {})
            self.assertTrue(used <= kinds, name)
            self.assertEqual(set(af.RULE), kinds)

    def test_horizon_and_universe_forms(self):
        self.assertEqual(af.horizon_key("Long Horizon"), "long-horizon")
        self.assertEqual(af.horizon_key("long-horizon"), "long-horizon")
        self.assertEqual(af.horizon_key("Normal Horizon"), "normal")
        self.assertEqual(af.universe_key("SynthCut"), "synthcut")
        self.assertEqual(af.universe_key("normal"), "normal")
        with self.assertRaises(af.FitError):
            af.universe_key("mars")


class Assignment(unittest.TestCase):
    def test_plain_reader_strips_comments_and_placeholders(self):
        text = ("```\ntaskId:   [ ]\nhorizon:  Long Horizon   # platform \"Task Type\": long-horizon\n"
                "business_function:  Product\ncompetency:  Engineering Ops\ntask_skill: Retrieval\n"
                "persona_name: Julia Lawson\npersona_role: Product Manager\ndifficulty_mode: medium\n"
                "universe_date: October 1, 2025 07:00\n```\nhorizon: Normal Horizon\n")
        fields = af.legacy_assignment(text)
        self.assertEqual(fields["task_type"], "Long Horizon")
        self.assertEqual(fields["universe_date_raw"], "October 1, 2025 07:00")
        self.assertNotIn("taskid", fields)
        self.assertEqual(af._date_key(fields["universe_date_raw"]), "2025-10-01")
        self.assertEqual(af._date_key("February 14, 2026 00:00"), "2026-02-14")
        self.assertIsNone(af._date_key("someday"))


class TaskFolder(unittest.TestCase):
    def setUp(self):
        self.tmp = selftest_sandbox.scratch_tmp("assignment_fit_test_")
        self.root = Path(self.tmp.name)
        self.task = self.root / "task"
        self.task.mkdir()
        (self.task / "00_Assigments.md").write_text(af.STUB_ASSIGNMENT.format(
            function="Product", name="Julia Lawson", role="Product Manager", competency="Marketing and GTM",
            horizon="long-horizon"), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_contract_object(self):
        result = af.evaluate(self.task, source=source(), tasks=[])
        for key in ("tool", "version", "verdict", "bound_to", "checks"):
            self.assertIn(key, result)
        self.assertEqual(result["tool"], "assignment_fit")
        self.assertEqual(result["verdict"], af.NO_COHORT)
        self.assertEqual(result["status"], "WARN")
        self.assertEqual([c["id"] for c in result["checks"]], ["fit.census"])
        self.assertEqual(result["checks"][0]["status"], "WARN")
        self.assertEqual(result["bound_to"]["00_Assigments.md"], af._sha256(self.task / "00_Assigments.md"))
        self.assertTrue(all(isinstance(x, str) for x in result["limits"]))
        self.assertTrue(result["assignment_hash"])

    def test_no_write_unless_asked_and_deterministic(self):
        first = af.evaluate(self.task, source=source(), tasks=[])
        self.assertFalse((self.task / "Working_Files").exists())
        af.evaluate(self.task, source=source(), write=True, tasks=[])
        stored = json.loads((self.task / "Working_Files" / af.FIT_JSON).read_text())
        self.assertEqual(af._dump(stored), af._dump(first))
        lines = (self.task / "Working_Files" / af.FIT_MD).read_text().splitlines()
        self.assertRegex(lines[0], HEADER)
        self.assertRegex(lines[1], CHECK)
        self.assertEqual(sorted(p.name for p in (self.task / "Working_Files").iterdir()), [af.FIT_JSON, af.FIT_MD])

    def test_gate_reads_the_fit_verdict(self):
        af.evaluate(self.task, source=source(), write=True, tasks=[])
        record = json.loads((self.task / "Working_Files" / af.FIT_JSON).read_text())
        verdict = str(record.get("verdict") or record.get("fit") or "")
        self.assertIn("NO NATURAL COHORT", verdict.upper())
        self.assertTrue(record["assignment_hash"])

    def test_missing_assignment_fails(self):
        result = af.evaluate(self.root / "nothing", source=source(), tasks=[])
        self.assertEqual(result["verdict"], "FAIL")
        self.assertEqual(result["checks"][0]["status"], "FAIL")
        self.assertTrue(af.render(result).startswith("ASSIGNMENT FIT (unknown): FAIL"))

    def test_fit_maps_to_pass(self):
        (self.task / "00_Assigments.md").write_text(af.STUB_ASSIGNMENT.format(
            function="Engineering", name="Vincent Parker", role="Game Systems Engineer",
            competency="Engineering Ops", horizon="long-horizon"), encoding="utf-8")
        result = af.evaluate(self.task, source=source(), tasks=[])
        self.assertEqual((result["verdict"], result["status"]), (af.FIT, "PASS"))
        self.assertRegex(af.render(result).splitlines()[1], r"^\[PASS\] fit\.census: FIT: ")

    def test_write_refuses_read_only_roots(self):
        with self.assertRaises(tc.ContextError):
            af._write(af.WS / "Evals" / "never.json", "{}", "a test write")
        self.assertFalse((af.WS / "Evals" / "never.json").exists())


class Archive(unittest.TestCase):
    def setUp(self):
        self.tmp = selftest_sandbox.scratch_tmp("assignment_fit_test_")
        self.root = Path(self.tmp.name) / "completed"
        task = self.root / "julia_earlier_task_2025-11-01"
        (task / "task_inputs" / "Working_Files").mkdir(parents=True)
        (task / "task_inputs" / "00_Assigments.md").write_text(af.STUB_ASSIGNMENT.format(
            function="Product", name="Julia Lawson", role="Product Manager", competency="Engineering Ops",
            horizon="long-horizon"), encoding="utf-8")
        (task / "README.md").write_text("# Julia: an earlier register\n\nMet SC-15, NB-2 and SC-13.\n")
        (task / "eval_reports").mkdir()
        (task / "eval_reports" / "1_prompt.md").write_text("Known issues: SC-15 applies; NB-17 is not used.\n")
        (task / "eval_reports" / "0_injection.md").write_text("SC-15 again.\n")
        (task / "task_inputs" / "Working_Files" / "01_Hardness_Manifest.json").write_text(json.dumps(
            {"cohort": {"key": "ZOM ticket", "size": 110, "members": ["ZOM-1", "ZOM-2", "ZOM-3", "match3d#12"],
                        "definition_source": ["f_0123456789abcdef012345", "C0BUGS1234/1759264851.763895"]}}))
        (self.root / "not_a_task").mkdir()
        self.tasks = af.archive_tasks(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def test_archive_entry(self):
        self.assertEqual(len(self.tasks), 1)
        t = self.tasks[0]
        self.assertEqual((t["task"], t["date"], t["universe"]), ("julia_earlier_task_2025-11-01", "2025-11-01", "synthcut"))
        self.assertEqual(t["cohort"], "110 x ZOM ticket")
        self.assertEqual(t["storyline"], "Julia: an earlier register")
        self.assertEqual(t["base_issues"], ["NB-2", "SC-13", "SC-15"])
        self.assertEqual(t["base_issues_raised"], {"NB-17": 1, "SC-15": 2})
        self.assertEqual(t["reports_read"], 2)
        self.assertEqual(t["collections"]["linear_teams"], ["ZOM"])
        self.assertEqual(t["collections"]["github_repos"], ["match3d"])
        self.assertEqual(t["collections"]["drive_files"], ["f_0123456789abcdef012345"])
        self.assertEqual(t["collections"]["slack_channels"], ["C0BUGS1234"])

    def test_used_marks_candidates_and_can_exclude_the_task_itself(self):
        src = source()
        julia = src.persona("julia_lawson")
        fit = af.census(src, julia, "Product", "Engineering Ops", "long-horizon", tasks=self.tasks)
        self.assertEqual([u["task"] for u in fit["used"]], ["julia_earlier_task_2025-11-01"])
        marked = {(c["kind"], c["key"]) for c in fit["candidates"] if c.get("used_by")}
        self.assertEqual(marked, {("github_repo", "match3d"), ("linear_team", "ZOM")})
        fit = af.census(src, julia, "Product", "Engineering Ops", "long-horizon", tasks=self.tasks,
                        exclude_task="julia_earlier_task_2025-11-01")
        self.assertEqual(fit["used"], [])
        self.assertEqual(af.used_by(src.persona("vincent_parker"), self.tasks), [])

    def test_card(self):
        src = source()
        card = af.build_card(src, src.persona("julia_lawson"), self.tasks)
        self.assertEqual(card["schema"], "persona-card-v1")
        self.assertEqual(card["thin_services"], ["gmail"])
        self.assertEqual(card["base_issues_met"], ["NB-2", "SC-13", "SC-15"])
        self.assertEqual(card["base_issues_raised"], {"NB-17": 1, "SC-15": 2})
        self.assertIn("base issues raised in platform reports: NB-17 (1), SC-15 (2)", af.card_text(card))
        self.assertEqual(sorted(card["competencies"]), sorted(af.load_competencies()["competencies"]))
        marketing = card["competencies"]["Marketing and GTM"]
        self.assertEqual(marketing["long-horizon"]["verdict"], af.NO_COHORT)
        self.assertEqual(marketing["normal"]["verdict"], af.LIMITS)
        self.assertTrue(marketing["long-horizon"]["near_misses"])
        self.assertEqual(af.card_path("normal", "julia_lawson").name, "julia_lawson.json")
        self.assertEqual(af.card_path("normal", "julia_lawson").parent.name, "normal")
        text = af.card_text(card)
        self.assertTrue(text.startswith("PERSONA CARD (Julia Lawson, synthcut): WARN"))

    def test_dates_skipped_tasks_and_the_before_filter(self):
        later = self.root / "julia_card_task_abc123"
        (later / "task_inputs").mkdir(parents=True)
        (later / "task_inputs" / "00_Assigments.md").write_text(af.STUB_ASSIGNMENT.format(
            function="Product", name="Julia Lawson", role="Product Manager", competency="Finance",
            horizon="normal"), encoding="utf-8")
        (later / "README.md").write_text("# Julia: a later register (submitted 2025-12-02)\n")
        skipped = Path(self.tmp.name) / "archived"
        old = skipped / "julia-skipped_2025-10-20"
        old.mkdir(parents=True)
        (old / "00_Assigments.md").write_text(af.STUB_ASSIGNMENT.format(
            function="Product", name="Julia Lawson", role="Product Manager", competency="Marketing and GTM",
            horizon="normal"), encoding="utf-8")
        (old / "04_Prompt.txt").write_text("Hey,   can you pull\nthe PN list together?\n")
        (skipped / "README.md").write_text("| Folder | Task | Status |\n|---|---|---|\n"
                                           "| `julia-skipped_2025-10-20/` | PN list — Julia / Marketing | Skipped |\n")
        (self.root / "julia_earlier_task_2025-11-01" / "README.md").write_text(
            "# Julia: an earlier register (archived 2025-11-01, not completed)\n")
        tasks = af.archive_tasks(self.root, skipped)
        by = {t["task"]: t for t in tasks}
        self.assertEqual(by["julia_card_task_abc123"]["date"], "2025-12-02")
        self.assertEqual((by["julia-skipped_2025-10-20"]["status"], by["julia-skipped_2025-10-20"]["date"]),
                         ("skipped", "2025-10-20"))
        self.assertEqual(by["julia-skipped_2025-10-20"]["storyline"], "PN list — Julia / Marketing")
        self.assertEqual(by["julia-skipped_2025-10-20"]["prompt_head"], "Hey, can you pull the PN list together?")
        self.assertEqual(by["julia_earlier_task_2025-11-01"]["status"], "unfinished")
        self.assertEqual(by["julia_card_task_abc123"]["status"], "completed")
        julia = source().persona("julia_lawson")
        self.assertEqual(len(af.used_by(julia, tasks)), 3)
        self.assertEqual([t["task"] for t in af.used_by(julia, tasks, before="2025-11-01")],
                         ["julia-skipped_2025-10-20"])
        self.assertEqual(af.used_by(julia, tasks, before="2025-10-20"), [])

    def test_backtest_never_writes_into_an_archive(self):
        task = self.root / "julia_earlier_task_2025-11-01" / "task_inputs"
        saved = af.COMPLETED
        af.COMPLETED = self.root
        try:
            self.assertEqual(af.archive_identity(task), ("julia_earlier_task_2025-11-01", "2025-11-01"))
            result = af.evaluate(task, source=source(), write=True, tasks=self.tasks)
            self.assertEqual(result["verdict"], "FAIL")
            self.assertIn("archived task", result["checks"][0]["detail"])
            self.assertFalse((task / "Working_Files" / af.FIT_JSON).exists())
            result = af.evaluate(task, source=source(), tasks=self.tasks)
            self.assertEqual(result["verdict"], af.LIMITS)
            self.assertEqual(result["used"], [])
        finally:
            af.COMPLETED = saved

    def test_cards_are_written_per_universe_and_persona(self):
        out = Path(self.tmp.name) / "cards"
        pairs = af.write_cards(("synthcut",), root=out, source_factory=lambda key: source())
        self.assertEqual(sorted(p.name for p, _c in pairs), ["julia_lawson.json", "leonard_hayes.json", "vincent_parker.json"])
        self.assertTrue(all(p.parent == out / "synthcut" and p.is_file() for p, _c in pairs))
        again = af.write_cards(("synthcut",), root=out, source_factory=lambda key: source(), write=False)
        self.assertEqual(af._dump(again[0][1]), (out / "synthcut" / again[0][0].name).read_text())


class SurfaceMap(unittest.TestCase):
    def section(self, mutate=None):
        return af.build_surface(source(mutate))

    def test_content_classes(self):
        self.assertEqual(af._content("record", {"count": 0}), "none")
        self.assertEqual(af._content("record", {"count": 3}), "real")
        self.assertEqual(af._content("record", {"count": None}), "not_counted")
        self.assertEqual(af._content("file", {"count": 3}), "metadata_only")
        self.assertEqual(af._content("comment", {"count": 10, "automated": 10}), "automated_only")
        self.assertEqual(af._content("comment", {"count": 10, "automated": 8}), "mostly_automated")
        self.assertEqual(af._content("comment", {"count": 10, "automated": 7}), "real")

    def test_entries(self):
        services = self.section()["services"]
        comments = services["linear"]["record_types"]["comments"]
        self.assertEqual((comments["count"], comments["base_content"], comments["injectable"], comments["reads_scoped"]),
                         (0, "none", True, False))
        pr = services["github"]["record_types"]["pull_request_comments"]
        self.assertEqual(pr["authors"], {"people": 13, "automated": 87})
        self.assertEqual(pr["base_content"], "mostly_automated")
        self.assertFalse(services["snowflake"]["record_types"]["tables"]["injectable"])
        self.assertTrue(services["gmail"]["reads_scoped"] and services["slack"]["reads_scoped"])
        self.assertFalse(services["linear"]["reads_scoped"] or services["confluence"]["reads_scoped"])
        self.assertEqual(services["gcal"]["record_types"]["event_descriptions"]["base_content"], "none")
        every = {(s, r) for s, _ in services.items() for r in services[s]["record_types"]}
        self.assertEqual(every, {(s, r) for s, r, _t, _k, _n in af.SURFACE_SPEC})

    def test_known_entries_follow_the_data(self):
        status = {k["claim"]: k["status"] for k in self.section()["known_entries"]}
        self.assertEqual(status["base Linear has no comments"], "confirmed")
        self.assertEqual(status["base PR conversation comments are bots only"], "partly")
        self.assertEqual(status["Snowflake cannot be injected"], "confirmed")

        def bots_only(d):
            d["surface"]["github"]["pull_request_comments"].update(people=0, automated=100, containers_with_people=0)
            d["surface"]["linear"]["comments"].update(count=4, people=4)
        status = {k["claim"]: k["status"] for k in self.section(bots_only)["known_entries"]}
        self.assertEqual(status["base PR conversation comments are bots only"], "confirmed")
        self.assertEqual(status["base Linear has no comments"], "not confirmed")

    @staticmethod
    def confluence(tables, archived):
        section = af.surface_section(af.stub_data()["surface"], tables, archived)
        entry = [k for k in section["known_entries"] if k["claim"].startswith("Confluence")][0]
        return section, entry

    def test_confluence_claim_is_checked_not_copied(self):
        said = {"by_service": {"confluence": {"reports": 4, "tasks": ["t1"], "example": "can't edit Confluence"}}}
        archived = {"files_read": 3, "by_service": {"confluence": {"tasks": 2, "statements": 7}},
                    "platform_statements": said}
        # the eval's injection schema holds a Confluence table: the claim does not hold
        tables = {"lint": {"confluence.confluence_pages"}, "eval_schema": {"confluence.confluence_pages"}, "live": set()}
        section, entry = self.confluence(tables, archived)
        self.assertEqual(entry["status"], "not confirmed")
        self.assertTrue(section["services"]["confluence"]["record_types"]["pages"]["injectable"])
        # absent from the eval schema and a platform report says so: confirmed, and the lint conflict is named
        tables["eval_schema"] = set()
        section, entry = self.confluence(tables, archived)
        self.assertEqual(entry["status"], "confirmed")
        self.assertIn("7 statement(s) in 2 of 3 archived injections", entry["evidence"])
        self.assertIn("4 platform report(s)", entry["evidence"])
        self.assertIn("sql_lint.WRITABLE_TABLES", entry["conflict"])
        pages = section["services"]["confluence"]["record_types"]["pages"]
        self.assertEqual((pages["injectable"], pages["in_authoring_lint"]), (False, True))
        self.assertIn("still allows it", pages["injectable_basis"])
        checks = af.surface_checks("normal", section)
        self.assertIn("surface.lint_conflict.confluence", [c["id"] for c in checks])
        # absent from the eval schema, the lint allows it and no report says anything: only likely
        archived["platform_statements"] = {"by_service": {}}
        self.assertEqual(self.confluence(tables, archived)[1]["status"], "likely")
        # absent everywhere: confirmed, no conflict
        tables["lint"] = set()
        entry = self.confluence(tables, {"files_read": 3, "by_service": {}})[1]
        self.assertEqual(entry["status"], "confirmed")
        self.assertNotIn("conflict", entry)

    def test_platform_statements_scan(self):
        with selftest_sandbox.scratch_tmp("assignment_fit_test_") as tmp:
            root = Path(tmp)
            one = root / "support" / "completed_tasks" / "task_a" / "eval_reports"
            one.mkdir(parents=True)
            (one / "1_prompt.md").write_text("6. Confluence decoy. Injection SQL can't edit Confluence, so the page "
                                             "won't appear.\nSnowflake can't be edited either.\n")
            (one / "0_injection.md").write_text("Confluence tables are not in the snapshot; disclosed limit only.\n")
            two = root / "archived_tasks" / "task_b" / "plateform_reports"
            two.mkdir(parents=True)
            (two / "r1.md").write_text("The known issue: injection can't edit Snowflake.\n")
            found = af.platform_statements(("confluence", "snowflake"), root)
            self.assertEqual(found["reports_read"], 3)
            self.assertEqual((found["by_service"]["confluence"]["reports"], found["by_service"]["confluence"]["tasks"]),
                             (1, ["task_a"]))
            self.assertEqual(sorted(found["by_service"]["snowflake"]["tasks"]), ["task_a", "task_b"])

    def test_comment_dates(self):
        clock = af._parse("2025-10-01T07:00:00+00:00")
        rows = [("pr1", "bot", "2025-09-01T00:00:00Z"), ("pr1", "ann", "2025-09-20T00:00:00Z"),
                ("pr2", "ann", "2024-01-05T00:00:00Z"), ("pr3", "ann", "2025-10-05T00:00:00Z")]
        out = af._authors(rows, lambda a: a == "ann", clock)
        self.assertEqual((out["people"], out["automated"], out["containers_with_people"]), (3, 1, 3))
        self.assertEqual((out["people_in_window"], out["people_last"]), (1, "2025-09-20"))
        self.assertNotIn("people_last", af._authors(rows, lambda a: a == "ann"))

    def test_file_merge_keeps_the_other_universe(self):
        with selftest_sandbox.scratch_tmp("assignment_fit_test_") as tmp:
            path = Path(tmp) / "map.json"
            out = af.run_surface(("synthcut",), write=True, path=path, source_factory=lambda key: source())
            self.assertEqual(out["verdict"], "WARN")
            stored = json.loads(path.read_text())
            self.assertEqual((stored["schema"], list(stored["universes"])), ("base-surface-map-v1", ["synthcut"]))
            stored["universes"]["normal"] = {"services": {}, "known_entries": []}
            path.write_text(json.dumps(stored))
            af.run_surface(("synthcut",), write=True, path=path, source_factory=lambda key: source())
            self.assertEqual(sorted(json.loads(path.read_text())["universes"]), ["normal", "synthcut"])
            path.write_text(json.dumps({"schema": "something-else", "universes": {"old": {}}}))
            self.assertEqual(list(af.surface_file({"normal": {}}, path)["universes"]), ["normal"])

    def test_archived_injection_scan_reads_text_only(self):
        with selftest_sandbox.scratch_tmp("assignment_fit_test_") as tmp:
            sql = Path(tmp) / "archived_tasks" / "one" / "01_Universe_Inject.sql"
            sql.parent.mkdir(parents=True)
            sql.write_text("BEGIN;\nINSERT INTO confluence.confluence_pages (id) VALUES ('p');\n"
                           "  insert into slack.slack_messages (id) values ('m');\n"
                           "UPDATE slack.slack_channels SET name = 'x' WHERE id = 'c';\n-- INSERT INTO snowflake.t\nCOMMIT;\n")
            found = af.archived_injections(Path(tmp))
            self.assertEqual(found["files_read"], 1)
            self.assertEqual(found["by_service"], {"confluence": {"tasks": 1, "statements": 1},
                                                   "slack": {"tasks": 1, "statements": 2}})


class Cli(unittest.TestCase):
    def call(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                code = af.main(argv)
            except SystemExit as exc:
                code = exc.code
        return code, out.getvalue(), err.getvalue()

    def test_self_test(self):
        code, out, _err = self.call(["--self-test"])
        self.assertEqual(code, 0)
        self.assertTrue(out.strip().startswith("self-test: ok ("))

    def test_usage_errors_exit_2(self):
        self.assertEqual(self.call([])[0], 2)
        self.assertEqual(self.call(["census"])[0], 2)
        self.assertEqual(self.call(["census", "--persona", "julia_lawson"])[0], 2)
        self.assertEqual(self.call(["census", "--task-dir", "x", "--persona", "julia_lawson"])[0], 2)
        self.assertEqual(self.call(["census", "--persona", "p", "--universe", "normal", "--function", "f",
                                    "--competency", "Finance", "--horizon", "normal", "--write"])[0], 2)
        self.assertEqual(self.call(["surface-map"])[0], 2)
        self.assertEqual(self.call(["surface-map", "--universe", "mars"])[0], 2)
        self.assertEqual(self.call(["card", "--persona", "julia_lawson"])[0], 2)

    def test_task_dir_without_assignment_exits_1(self):
        with selftest_sandbox.scratch_tmp("assignment_fit_test_") as tmp:
            code, out, _err = self.call(["census", "--task-dir", tmp])
            self.assertEqual(code, 1)
            self.assertTrue(out.startswith("ASSIGNMENT FIT (unknown): FAIL"))


class Tool(unittest.TestCase):
    def test_source_has_no_default_task_folder_literal(self):
        text = (HERE / "assignment_fit.py").read_text()
        self.assertNotIn("Evals/" + "task_inputs", text)
        self.assertTrue(text.startswith("#!/usr/bin/env python3"))
        self.assertIn("from __future__ import annotations", text)

    def test_stub_is_not_mutated_by_a_census(self):
        data = af.stub_data()
        before = copy.deepcopy(data)
        src = af.StubSource(data)
        af.census(src, src.persona("julia_lawson"), "Product", "Marketing and GTM", "long-horizon", tasks=[])
        af.build_card(src, src.persona("julia_lawson"), [])
        self.assertEqual(data, before)

    def test_reading_restores_the_modules_and_the_environment(self):
        try:
            af.universe_context("synthcut")
        except af.FitError as exc:
            self.skipTest(f"universe not installed: {exc}")
        import persona_view as pv
        before = {k: vars(pv).get(k) for k in af._PATCHED}
        os.environ["TASK_AUTHORING_TASK_DIR"] = "sentinel-for-test"
        try:
            with af.reading("synthcut") as context:
                self.assertNotIn("TASK_AUTHORING_TASK_DIR", os.environ)
                self.assertEqual(pv.DATA_CLOCK.isoformat(), "2025-10-01T07:00:00+00:00")
                self.assertEqual(pv.CACHE.name, context["context_hash"][:20])
                self.assertIn("Universe_SynthCut", str(pv.OTHER))
            self.assertEqual(os.environ.get("TASK_AUTHORING_TASK_DIR"), "sentinel-for-test")
            self.assertEqual({k: vars(pv).get(k) for k in af._PATCHED}, before)
        finally:
            os.environ.pop("TASK_AUTHORING_TASK_DIR", None)


@unittest.skipUnless(os.environ.get("ASSIGNMENT_FIT_REAL") == "1", "set ASSIGNMENT_FIT_REAL=1 to read the universes")
class PlanBacktest(unittest.TestCase):
    """The four outcomes plan WS9 asks of the census, on the archived assignments."""
    ARCHIVE = af.COMPLETED

    def verdict(self, name):
        return af.evaluate(self.ARCHIVE / name / "task_inputs")

    def test_completed_julia_task_names_the_gmail_limit(self):
        result = self.verdict("julia_zm_difficulty_baseline_2026-11-01")
        self.assertEqual(result["verdict"], af.LIMITS)
        self.assertTrue(any(x.startswith("Gmail is thin") for x in result["limits"]))

    def test_unfinished_julia_task_has_no_natural_cohort(self):
        self.assertEqual(self.verdict("julia_zm3d_beta_calendar_2026-11-07")["verdict"], af.NO_COHORT)

    def test_two_revision_tasks_are_not_no_natural_cohort(self):
        for name in ("leonard_stockholder_closeout_2026-11-10", "vincent_zm3d_release_gate_2026-11-06"):
            self.assertNotEqual(self.verdict(name)["verdict"], af.NO_COHORT, name)

    def test_backtest_sees_only_earlier_tasks(self):
        used = [u["task"] for u in self.verdict("julia_zm_difficulty_baseline_2026-11-01")["used"]]
        self.assertNotIn("julia_zm3d_beta_calendar_2026-11-07", used)

    def test_surface_map_known_entries(self):
        out = af.run_surface(af.UNIVERSES)
        for key in af.UNIVERSES:
            status = {k["claim"]: k["status"] for k in out["surface_map"]["universes"][key]["known_entries"]}
            self.assertEqual(status["base Linear has no comments"], "confirmed", key)
            self.assertEqual(status["Snowflake cannot be injected"], "confirmed", key)
            self.assertEqual(status["Confluence cannot be injected"], "confirmed", key)
            self.assertIn(status["base PR conversation comments are bots only"], ("confirmed", "partly"), key)


if __name__ == "__main__":
    unittest.main()

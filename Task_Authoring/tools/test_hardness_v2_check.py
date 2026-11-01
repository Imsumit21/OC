#!/usr/bin/env python3
"""Tests for hardness_v2_check.py, the advisory Hardness v2 (Opus 5.5) self-checks (Part 5 and Part 7).

Synthetic fixtures cover every check; one regression test runs the live task's manifest and SQL when present.

  python3 -B -m unittest test_hardness_v2_check -v     (from Task_Authoring/tools)
"""

from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import hardness_v2_check as hv  # noqa: E402

CH = "C09R0KXFX71"
SQL = f"""-- Are you planning to inject? Yes
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, created_at) VALUES ('m1', '1758732120.000100', '{CH}', 'message', 'U1', 'Please cost the releases; follow the method in the doc.', NULL, '1758732120.000100', '2025-09-24T16:42:00Z');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, created_at) VALUES ('m2', '1758813480.000300', '{CH}', 'message', 'U1', 'Leave ENG-1 off the release lines.', 'm1', '1758732120.000100', '2025-09-25T15:18:00Z');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, created_at) VALUES ('m3', '1758900000.000400', 'C0OTHER0001', 'message', 'U2', 'Correction: the pool also takes contractor fees.', NULL, NULL, '2025-09-26T15:20:00Z');
INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id) VALUES ('a@x.co/101', 'a@x.co', 's', NULL);
INSERT INTO gmail.gmail_messages (id, thread_id, user_email, subject, body_text, date) VALUES ('a@x.co/<g1@x>', 'a@x.co/101', 'a@x.co', 'method', 'The method is in the doc.', '2025-09-23T15:10:00Z');
INSERT INTO gmail.gmail_messages (id, thread_id, user_email, subject, body_text, date) VALUES ('a@x.co/<g2@x>', 'a@x.co/101', 'a@x.co', 'Re: method', 'One change: add contractor fees to the pool.', '2025-09-26T14:30:00Z');
INSERT INTO gdocs.docs_documents (document_id, title, body_text) VALUES ('f_doc1', 'Method', 'Pool = salaries only.');
INSERT INTO gsheets.sheets_spreadsheets (spreadsheet_id, title) VALUES ('f_sheet1', 'Board model');
INSERT INTO trello.trello_cards (id, name, "idBoard", "idList", "desc") VALUES ('card1', 'Train map', 'b1', 'l1', 'v2');
INSERT INTO trello.trello_actions (id, type, date, "idMemberCreator", "idBoard", "idCard", data_json) VALUES ('act1', 'createCard', '2024-10-03 15:20:00+00', 'p', 'b1', 'card1', '{{}}');
INSERT INTO trello.trello_actions (id, type, date, "idMemberCreator", "idBoard", "idCard", data_json) VALUES ('act2', 'updateCard', '2024-12-02 17:05:00+00', 'p', 'b1', 'card1', '{{}}');
INSERT INTO linear.linear_comments (id, issue_id, author_id, body, created_at) VALUES ('lc1', 'ENG-7', 'u', 'Picked onto release/desire.', '2024-09-24T06:28:19Z');
"""

ANCHORS = [
    {"id": "A1", "service": "slack", "locator": f"{CH}/1758732120.000100"},
    {"id": "A2", "service": "gsheets", "locator": "gsheets:f_sheet1"},
]
FRAGMENTS = [
    {
        "id": "K1",
        "service": "gmail",
        "delegated_by_record": f"{CH}/1758732120.000100",
        "seeded_ids": ["a@x.co/<g1@x>"],
    },
    {
        "id": "K2",
        "service": "gdocs",
        "delegated_by_record": "a@x.co/<g1@x>",
        "seeded_ids": ["f_doc1"],
    },
]


def vr(service, rid, at="2025-09-01T00:00:00Z"):
    return {"service": service, "id": rid, "seeded": True, "at": at}


def manifest(traps=(), portfolio=(), chains=()):
    return {
        "anchors": ANCHORS,
        "ask_fragments": FRAGMENTS,
        "traps": list(traps),
        "mechanism_portfolio": list(portfolio),
        "chains": list(chains),
    }


def flags(rep, check):
    return [f for f in rep["flags"] if f["check"] == check]


class SamePlace(unittest.TestCase):
    def test_versions_in_one_container_flag_same_container(self):
        t = {
            "id": "T3",
            "family": "superseding",
            "services": ["trello"],
            "version_records": [vr("trello", "act1"), vr("trello", "act2")],
        }
        rep = hv.run(manifest([t]), SQL)
        got = flags(rep, "SAME_PLACE")
        self.assertEqual(
            [(f["node"], f["kind"]) for f in got], [("T3", "same_container")]
        )

    def test_correction_on_the_delegation_path_flags_on_path(self):
        t = {
            "id": "T1",
            "family": "superseding",
            "services": ["gdocs", "gmail"],
            "version_records": [vr("gdocs", "f_doc1"), vr("gmail", "a@x.co/<g2@x>")],
        }
        rep = hv.run(manifest([t]), SQL)
        got = flags(rep, "SAME_PLACE")
        self.assertEqual(
            [(f["node"], f["kind"]) for f in got], [("T1", "on_delegation_path")]
        )
        self.assertIn("gmail:a@x.co/101", got[0]["detail"])

    def test_correction_in_an_anchor_container_flags_first_read(self):
        t = {
            "id": "T4",
            "family": "superseding",
            "services": ["gdocs", "gsheets"],
            "version_records": [vr("gdocs", "f_doc1"), vr("gsheets", "f_sheet1")],
        }
        rep = hv.run(manifest([t]), SQL)
        self.assertEqual(
            [(f["node"], f["kind"]) for f in flags(rep, "SAME_PLACE")],
            [("T4", "first_read")],
        )

    def test_correction_in_a_thread_reply_of_the_anchor_flags_first_read(self):
        t = {
            "id": "T8",
            "family": "superseding",
            "services": ["gdocs", "slack"],
            "version_records": [
                vr("gdocs", "f_doc1"),
                vr("slack", f"{CH}/1758813480.000300"),
            ],
        }
        rep = hv.run(manifest([t]), SQL)
        self.assertEqual(
            [(f["node"], f["kind"]) for f in flags(rep, "SAME_PLACE")],
            [("T8", "first_read")],
        )

    def test_correction_somewhere_else_is_clean(self):
        t = {
            "id": "T9",
            "family": "superseding",
            "services": ["gdocs", "slack"],
            "version_records": [
                vr("gdocs", "f_doc1"),
                vr("slack", "C0OTHER0001/1758900000.000400"),
            ],
        }
        rep = hv.run(manifest([t]), SQL)
        self.assertEqual(flags(rep, "SAME_PLACE"), [])
        self.assertEqual(rep["nodes"]["T9"]["same_place"], "CLEAN")

    def test_unresolvable_record_is_unresolved_never_clean(self):
        t = {
            "id": "T5",
            "family": "superseding",
            "services": ["gmail"],
            "version_records": [
                vr("gdocs", "f_doc1"),
                {
                    "service": "gmail",
                    "base_pointer": "gmail:someone@x.co/<zz>",
                    "seeded": False,
                    "at": "2025-09-26T00:00:00Z",
                },
            ],
        }
        rep = hv.run(manifest([t]), SQL)
        self.assertEqual(flags(rep, "SAME_PLACE"), [])
        self.assertEqual(rep["nodes"]["T5"]["same_place"], "UNRESOLVED")
        self.assertTrue(any(u["node"] == "T5" for u in rep["unresolved"]))

    def test_declared_container_override_is_honoured(self):
        t = {
            "id": "T6",
            "family": "superseding",
            "services": ["gmail"],
            "version_records": [
                dict(vr("gdocs", "f_doc1")),
                {
                    "service": "gmail",
                    "base_pointer": "gmail:someone@x.co/<zz>",
                    "seeded": False,
                    "at": "2025-09-26T00:00:00Z",
                    "container": "gmail:a@x.co/101",
                },
            ],
        }
        rep = hv.run(manifest([t]), SQL)
        self.assertEqual(
            [(f["node"], f["kind"]) for f in flags(rep, "SAME_PLACE")],
            [("T6", "on_delegation_path")],
        )

    def test_traps_without_two_versions_are_not_judged(self):
        rep = hv.run(
            manifest(
                [
                    {
                        "id": "T7",
                        "family": "distractor",
                        "services": ["linear"],
                        "seeded_ids": ["lc1"],
                    }
                ]
            ),
            SQL,
        )
        self.assertEqual(flags(rep, "SAME_PLACE"), [])
        self.assertNotIn("T7", rep["nodes"])


class DesignChecks(unittest.TestCase):
    def test_empty_manifest_does_not_crash(self):
        rep = hv.run({}, "")
        self.assertEqual(rep["checks"]["SAME_PLACE"], "SKIP")
        self.assertEqual(rep["checks"]["DONE_CHECK"], "FLAG")
        self.assertEqual(rep["checks"]["TWO_DECISIONS"], "FLAG")

    def test_done_check_clears_with_an_a24_rule_or_family(self):
        self.assertTrue(flags(hv.run(manifest(), SQL), "DONE_CHECK"))
        port = [{"id": "M1", "mechanism": "A24", "nodes": ["T1"], "requirement": "R1"}]
        self.assertFalse(flags(hv.run(manifest(portfolio=port), SQL), "DONE_CHECK"))
        trap = {"id": "T1", "family": "done_gap", "services": ["github", "linear"]}
        self.assertFalse(flags(hv.run(manifest([trap]), SQL), "DONE_CHECK"))

    def test_two_decisions_needs_two_cross_source_rules_on_distinct_requirements(self):
        traps = [
            {"id": "T1", "family": "superseding", "services": ["gdocs", "gmail"]},
            {"id": "T2", "family": "exact_predicate", "services": ["linear"]},
            {"id": "T3", "family": "authority", "services": ["trello", "linear"]},
        ]
        one = [{"id": "M1", "mechanism": "A14", "nodes": ["T1"], "requirement": "R3"}]
        self.assertTrue(flags(hv.run(manifest(traps, one), SQL), "TWO_DECISIONS"))
        single_source = one + [
            {"id": "M2", "mechanism": "A17", "nodes": ["T2"], "requirement": "R1"}
        ]
        self.assertTrue(
            flags(hv.run(manifest(traps, single_source), SQL), "TWO_DECISIONS")
        )
        same_req = one + [
            {"id": "M3", "mechanism": "A15", "nodes": ["T3"], "requirement": "R3"}
        ]
        self.assertTrue(flags(hv.run(manifest(traps, same_req), SQL), "TWO_DECISIONS"))
        good = one + [
            {"id": "M3", "mechanism": "A15", "nodes": ["T3"], "requirement": "R2"}
        ]
        self.assertFalse(flags(hv.run(manifest(traps, good), SQL), "TWO_DECISIONS"))

    def test_filter_check(self):
        self.assertTrue(flags(hv.run(manifest(), SQL), "FILTER_CHECK"))
        trap = {"id": "T2", "family": "exact_predicate", "services": ["linear"]}
        self.assertFalse(flags(hv.run(manifest([trap]), SQL), "FILTER_CHECK"))
        port = [{"id": "M2", "mechanism": "A17", "nodes": ["C1"], "requirement": "R1"}]
        self.assertFalse(flags(hv.run(manifest(portfolio=port), SQL), "FILTER_CHECK"))


class SurfaceChecks(unittest.TestCase):
    PORT = [
        {"id": "M1", "mechanism": "A15", "nodes": ["T1"], "requirement": "R2"},
        {"id": "M2", "mechanism": "A14", "nodes": ["T2"], "requirement": "R3"},
    ]

    def surface(self, slots):
        return {"slots": slots}

    def test_decision_flip_flags_a_rule_with_no_weight5_slot(self):
        slots = [
            {"id": "S1", "weight": 5, "class": "aggregate", "mechanisms": ["M1"]},
            {"id": "S2", "weight": 3, "class": "direct", "mechanisms": ["M2"]},
        ]
        rep = hv.run(manifest(portfolio=self.PORT), SQL, surface=self.surface(slots))
        self.assertEqual([f["node"] for f in flags(rep, "DECISION_FLIP")], ["M2"])

    def test_decision_flip_uses_flipped_by_too(self):
        slots = [
            {"id": "S1", "weight": 5, "class": "aggregate", "mechanisms": ["M1"]},
            {
                "id": "S2",
                "weight": 5,
                "class": "direct",
                "mechanisms": [],
                "flipped_by": ["M2"],
            },
        ]
        rep = hv.run(manifest(portfolio=self.PORT), SQL, surface=self.surface(slots))
        self.assertEqual(flags(rep, "DECISION_FLIP"), [])

    def test_decision_flip_skips_without_a_surface(self):
        rep = hv.run(manifest(portfolio=self.PORT), SQL)
        self.assertEqual(rep["checks"]["DECISION_FLIP"], "SKIP")

    def test_input_check_flags_a_weight5_total_no_rule_can_move(self):
        slots = [
            {"id": "S_total", "weight": 5, "class": "aggregate", "mechanisms": []},
            {"id": "S_ok", "weight": 5, "class": "aggregate", "mechanisms": ["M1"]},
            {"id": "S_light", "weight": 3, "class": "aggregate", "mechanisms": []},
        ]
        rep = hv.run(manifest(portfolio=self.PORT), SQL, surface=self.surface(slots))
        self.assertEqual([f["node"] for f in flags(rep, "INPUT_CHECK")], ["S_total"])


class RuleInPrompt(unittest.TestCase):
    TRAP = {
        "id": "T1",
        "family": "superseding",
        "services": ["gmail"],
        "resolver": "Ines's later reply adds the contractor_fees lines from the ledger to the monthly pool",
    }

    def test_verbatim_resolver_span_flags(self):
        prompt = "Use Ines's method. Note the later reply adds the contractor_fees lines from the ledger to the pool."
        rep = hv.run(manifest([self.TRAP]), SQL, prompt=prompt)
        self.assertEqual([f["node"] for f in flags(rep, "RULE_IN_PROMPT")], ["T1"])

    def test_paraphrase_is_clean(self):
        prompt = (
            "Follow Ines's method and send her the release totals when they are done."
        )
        rep = hv.run(manifest([self.TRAP]), SQL, prompt=prompt)
        self.assertEqual(flags(rep, "RULE_IN_PROMPT"), [])

    def test_no_prompt_skips(self):
        self.assertEqual(
            hv.run(manifest([self.TRAP]), SQL)["checks"]["RULE_IN_PROMPT"], "SKIP"
        )


class Cli(unittest.TestCase):
    def call(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = hv.main(argv)
        return rc, out.getvalue()

    def test_advisory_exit_zero_and_strict_exit_one(self):
        t = {
            "id": "T3",
            "family": "superseding",
            "services": ["trello"],
            "version_records": [vr("trello", "act1"), vr("trello", "act2")],
        }
        with tempfile.TemporaryDirectory() as d:
            m, s = Path(d) / "m.json", Path(d) / "x.sql"
            m.write_text(json.dumps(manifest([t])))
            s.write_text(SQL)
            rc, out = self.call(["--manifest", str(m), "--sql", str(s), "--json"])
            self.assertEqual(rc, 0)
            self.assertIn("SAME_PLACE", json.loads(out)["checks"])
            rc, _ = self.call(["--manifest", str(m), "--sql", str(s), "--strict"])
            self.assertEqual(rc, 1)

    def test_missing_inputs_is_a_usage_error(self):
        rc, _ = self.call(["--manifest", "/nonexistent.json"])
        self.assertEqual(rc, 2)



class Robustness(unittest.TestCase):
    """Review notes N1-N4 (2026-11-01): malformed manifests, duplicate ids, id-less events, naming drift."""

    def test_non_dict_entries_are_skipped_and_reported(self):
        man = {"anchors": ["A1"], "ask_fragments": ["K1"], "traps": ["T1"], "mechanism_portfolio": ["M1"],
               "chains": ["C1"]}
        rep = hv.run(man, SQL)
        self.assertEqual(rep["checks"]["SAME_PLACE"], "SKIP")
        self.assertEqual(sorted(rep["malformed"]), ["anchors", "ask_fragments", "chains", "mechanism_portfolio", "traps"])

    def test_list_valued_requirement_does_not_crash(self):
        traps = [{"id": "T1", "family": "superseding", "services": ["gdocs", "gmail"]}]
        port = [{"id": "M1", "mechanism": "A14", "nodes": ["T1"], "requirement": ["R1", "R2"]}]
        rep = hv.run(manifest(traps, port), SQL)
        self.assertIn("mechanism_portfolio", rep["malformed"])

    def test_malformed_json_shape_is_a_usage_error_not_strict(self):
        with tempfile.TemporaryDirectory() as d:
            m, s = Path(d) / "m.json", Path(d) / "x.sql"
            m.write_text(json.dumps(["not", "a", "manifest"]))
            s.write_text(SQL)
            err = io.StringIO()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
                rc = hv.main(["--manifest", str(m), "--sql", str(s), "--strict"])
            self.assertEqual(rc, 2)
            self.assertIn("manifest", err.getvalue())

    def test_duplicate_trap_ids_keep_the_flag(self):
        t = {"id": "T3", "family": "superseding", "services": ["trello"],
             "version_records": [vr("trello", "act1"), vr("trello", "act2")]}
        clean = {"id": "T3", "family": "superseding", "services": ["gdocs", "slack"],
                 "version_records": [vr("gdocs", "f_doc1"), vr("slack", "C0OTHER0001/1758900000.000400")]}
        rep = hv.run(manifest([t, clean]), SQL)
        self.assertEqual(rep["checks"]["SAME_PLACE"], "FLAG")
        self.assertIn("1 flagged", rep["details"]["SAME_PLACE"])
        self.assertIn("duplicate trap id T3", " ".join(rep["malformed"]))

    def test_event_without_ids_is_unresolved_not_matched(self):
        sql = SQL + ("INSERT INTO gcal.gcal_events (calendar_id, summary, status) VALUES ('c@x.co', 'slot', 'confirmed');\n")
        ov = hv.Overlay(sql)
        self.assertIsNone(ov._from_row("gcal.gcal_events", {"calendar_id": "c@x.co"}))

    def test_unknown_slot_mechanisms_are_named(self):
        port = [{"id": "M1", "mechanism": "A15", "nodes": ["T1"], "requirement": "R2"}]
        slots = [{"id": "S1", "weight": 5, "class": "aggregate", "mechanisms": ["M1", "M9_ride_along"]}]
        rep = hv.run(manifest(portfolio=port), SQL, surface={"slots": slots})
        self.assertEqual(rep["checks"]["DECISION_FLIP"], "CLEAN")
        self.assertIn("M9_ride_along", rep["details"]["DECISION_FLIP"])

LIVE = HERE.parent / "task_inputs"


@unittest.skipUnless(
    (LIVE / "Working_Files" / "01_Hardness_Manifest.json").is_file()
    and (LIVE / "01_Universe_Inject.sql").is_file(),
    "live task inputs not present",
)
class LiveTask(unittest.TestCase):
    """dd-2024-release-cost rev1: the Opus 5.5 pre-check settled T1 (Ines's amendment in her own thread) and T3 (both
    train-map versions on one card) on its first reads; the checker must flag both."""

    def test_live_corrections_flagged(self):
        man = json.loads(
            (LIVE / "Working_Files" / "01_Hardness_Manifest.json").read_text()
        )
        sql = (LIVE / "01_Universe_Inject.sql").read_text()
        rep = hv.run(man, sql)
        got = {f["node"]: f["kind"] for f in flags(rep, "SAME_PLACE")}
        self.assertEqual(got.get("T1"), "on_delegation_path")
        self.assertEqual(got.get("T3"), "same_container")


if __name__ == "__main__":
    unittest.main()

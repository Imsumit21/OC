"""Tests for generators/validate/overlay.py and invariants.py (stdlib unittest)."""
from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from generators.core.ops import Op
from generators.validate.invariants import (
    COMMENTS,
    ISSUES,
    PROJECTS,
    TEAMS,
    USERS,
    check_linear,
    corroborate,
    state_types,
)
from generators.validate.overlay import MEMBERSHIP_TABLE, apply, load_linear_base

FREEZE = "2024-04-01T00:00:00Z"


# --------------------------------------------------------------------------- fixtures

def _team(team_id, key, counter):
    return {
        "id": team_id, "name": key.title(), "key": key, "description": None,
        "is_archived": False, "created_at": "2023-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z", "issue_counter": counter,
    }


def _user(user_id):
    return {
        "id": user_id, "email": f"{user_id}@example.com", "name": user_id,
        "display_name": user_id, "avatar_url": None, "is_active": True,
        "is_admin": False, "is_guest": False,
        "created_at": "2023-01-01T00:00:00Z", "updated_at": "2023-01-01T00:00:00Z",
    }


def _issue(issue_id, *, number, team_id, state_id, created_at, updated_at,
           started_at=None, completed_at=None, canceled_at=None, parent_id=None,
           project_id=None, identifier=None, state_history_json="[]", links_json="[]"):
    return {
        "id": issue_id, "uuid": None, "project_id": project_id, "team_id": team_id,
        "parent_id": parent_id, "assignee_id": None, "creator_id": "usr_a",
        "state_id": state_id, "cycle_id": None, "identifier": identifier or issue_id,
        "number": number, "title": f"title {issue_id}", "description": None,
        "priority": 0, "estimate": None, "due_date": None, "started_at": started_at,
        "completed_at": completed_at, "canceled_at": canceled_at, "archived_at": None,
        "time_in_status_minutes": None, "labels_json": "[]", "links_json": links_json,
        "relations_json": "[]", "state_history_json": state_history_json,
        "is_archived": False, "created_at": created_at, "updated_at": updated_at,
    }


def _comment(comment_id, issue_id, *, created_at, sequence, author_id="usr_a",
             parent_id=None, updated_at=None, is_edited=False):
    return {
        "id": comment_id, "issue_id": issue_id, "author_id": author_id,
        "parent_id": parent_id, "body": f"body {comment_id}",
        "is_edited": is_edited, "created_at": created_at,
        "updated_at": updated_at if updated_at is not None else created_at,
        "sequence": sequence,
    }


def _project(project_id, team_id, updated_at):
    return {
        "id": project_id, "team_id": team_id, "name": project_id, "summary": None,
        "description": None, "lead_id": None, "priority": 0, "state": None,
        "start_date": None, "target_date": None, "uuid": None, "icon": None,
        "color": "#bec2c8", "started_at": None, "completed_at": None,
        "canceled_at": None, "start_date_resolution": None,
        "target_date_resolution": None, "labels_json": "[]",
        "is_archived": False, "created_at": "2023-01-01T00:00:00Z",
        "updated_at": updated_at,
    }


def make_base() -> dict:
    return {
        ISSUES: {
            ("ART-1",): _issue(
                "ART-1", number=1, team_id="team_ART", state_id="Done",
                created_at="2024-02-01T00:00:00Z", updated_at="2024-03-05T10:00:00Z",
                started_at="2024-03-01T00:00:00Z", completed_at="2024-03-05T10:00:00Z",
            ),
            ("ZOM-1",): _issue(
                "ZOM-1", number=1, team_id="team_ZOM", state_id="Todo",
                created_at="2024-02-02T00:00:00Z", updated_at="2024-02-02T00:00:00Z",
            ),
        },
        COMMENTS: {},
        PROJECTS: {("proj_1",): _project("proj_1", "team_ART", "2024-04-01T00:00:00Z")},
        TEAMS: {("team_ART",): _team("team_ART", "ART", 2), ("team_ZOM",): _team("team_ZOM", "ZOM", 1)},
        USERS: {("usr_a",): _user("usr_a"), ("usr_b",): _user("usr_b")},
        MEMBERSHIP_TABLE: {
            ("team_ART", "usr_a", "tmem_a"): {
                "id": "tmem_a", "team_id": "team_ART", "user_id": "usr_a",
                "created_at": "2024-01-01T00:00:00Z",
            },
        },
    }


def ins(table, **cols) -> Op:
    return Op(table=table, op="insert", cols=tuple(cols.items()))


def upd(table, where, **cols) -> Op:
    return Op(table=table, op="update", cols=tuple(cols.items()), where=tuple(where.items()))


def new_issue_ops(issue_id="ART-2", *, number=2, identifier=None, state_id="Todo",
                  created_at="2024-02-10T00:00:00Z", updated_at="2024-03-03T00:00:00Z",
                  completed_at=None, canceled_at=None, parent_id=None, project_id=None,
                  state_history_json="[]", links_json="[]"):
    return ins(
        ISSUES, id=issue_id, identifier=identifier or issue_id, number=number,
        team_id="team_ART", state_id=state_id, title="new", description=None,
        priority=0, estimate=None, due_date=None, started_at=None,
        completed_at=completed_at, canceled_at=canceled_at, archived_at=None,
        time_in_status_minutes=None, labels_json="[]", links_json=links_json,
        relations_json="[]", state_history_json=state_history_json,
        is_archived=False, created_at=created_at, updated_at=updated_at,
        project_id=project_id, parent_id=parent_id,
    )


def comment_op(comment_id, issue_id, *, created_at, sequence, author_id="usr_a", parent_id=None):
    return ins(COMMENTS, **_comment(comment_id, issue_id, created_at=created_at,
                                    sequence=sequence, author_id=author_id,
                                    parent_id=parent_id))


def failing_rules(ops) -> set[str]:
    base = make_base()
    overlay = apply(base, ops)
    findings = check_linear(overlay, base, freeze_utc=FREEZE)
    return {finding.rule for finding in findings if finding.severity == "FAIL"}


# --------------------------------------------------------------------------- overlay tests

class OverlayTests(unittest.TestCase):
    def test_apply_is_pure_and_tracks_changes(self):
        base = make_base()
        snapshot = copy.deepcopy(base)
        overlay = apply(base, [new_issue_ops(),
                               upd(TEAMS, {"id": "team_ART"}, issue_counter=3)])
        self.assertEqual(base, snapshot, "apply must not mutate the base")
        self.assertEqual(overlay.errors, [])
        self.assertIn(("ART-2",), overlay.state[ISSUES])
        self.assertEqual(overlay.state[TEAMS][("team_ART",)]["issue_counter"], 3)
        self.assertEqual(overlay.inserted[ISSUES], [("ART-2",)])
        self.assertEqual(overlay.updated[TEAMS], [("team_ART",)])
        self.assertEqual(overlay.kind(ISSUES, ("ART-2",)), "insert")

    def test_insert_existing_and_update_missing_are_errors(self):
        overlay = apply(make_base(), [
            ins(ISSUES, id="ART-1", identifier="ART-1", number=1, team_id="team_ART"),
            upd(ISSUES, {"id": "ART-404"}, title="nope"),
        ])
        self.assertEqual(len(overlay.errors), 2)
        self.assertEqual(overlay.state[ISSUES][("ART-1",)]["title"], "title ART-1")
        self.assertNotIn(("ART-404",), overlay.state[ISSUES])

    def test_insert_fills_absent_columns_with_none(self):
        overlay = apply(make_base(), [ins(ISSUES, id="ART-9", identifier="ART-9",
                                          number=9, team_id="team_ART")])
        row = overlay.state[ISSUES][("ART-9",)]
        self.assertIsNone(row["created_at"])
        self.assertIsNone(row["state_history_json"])
        self.assertTrue(all(col in row for col in ("labels_json", "links_json", "updated_at")))

    def test_load_base_maps_json_fields_and_verifies_sha(self):
        export = {
            "users": [_user("usr_a")],
            "teams": [_team("team_ART", "ART", 3)],
            "projects": [],
            "issues": [_issue("ART-1", number=1, team_id="team_ART", state_id="Todo",
                              created_at="2024-02-01T00:00:00Z",
                              updated_at="2024-02-01T00:00:00Z")],
            "comments": [],
            "team_memberships": [{"id": "tmem_a", "team_id": "team_ART",
                                  "user_id": "usr_a", "created_at": "2024-01-01T00:00:00Z"}],
            "attachments": [],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "data.json"
            path.write_text(json.dumps(export), encoding="utf-8")
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            base = load_linear_base(path, digest)
            self.assertEqual(base[ISSUES][("ART-1",)]["labels_json"], "[]")
            self.assertIsNone(base[ISSUES][("ART-1",)]["state_history_json"])
            self.assertIn(("team_ART", "usr_a", "tmem_a"), base[MEMBERSHIP_TABLE])
            with self.assertRaises(ValueError):
                load_linear_base(path, "0" * 64)


# --------------------------------------------------------------------------- rule tests

class RuleTests(unittest.TestCase):
    def test_passing_scenario_has_no_findings(self):
        ops = [
            new_issue_ops(),
            comment_op("comm_1", "ART-2", created_at="2024-03-01T00:00:00Z", sequence=1),
            comment_op("comm_2", "ART-2", created_at="2024-03-02T00:00:00Z", sequence=2),
            comment_op("comm_3", "ART-2", created_at="2024-03-03T00:00:00Z", sequence=3),
            upd(ISSUES, {"id": "ART-1"}, updated_at="2024-03-06T00:00:00Z"),
            upd(TEAMS, {"id": "team_ART"}, issue_counter=3),
        ]
        base = make_base()
        overlay = apply(base, ops)
        self.assertEqual(overlay.errors, [])
        findings = check_linear(overlay, base, freeze_utc=FREEZE)
        self.assertEqual([(f.rule, f.severity, f.message) for f in findings], [])

    def test_state_types_infers_completed_and_canceled(self):
        base = make_base()
        base[ISSUES][("ART-2",)] = _issue(
            "ART-2", number=2, team_id="team_ART", state_id="Canceled",
            created_at="2024-02-01T00:00:00Z", updated_at="2024-02-02T00:00:00Z",
            canceled_at="2024-02-02T00:00:00Z",
        )
        types = state_types(base)
        self.assertIn("Done", types["completed"])
        self.assertIn("Canceled", types["canceled"])

    def test_l1_bad_timestamp(self):
        rules = failing_rules([new_issue_ops(created_at="2024-02-10 00:00:00+00")])
        self.assertIn("L1", rules)

    def test_l2_id_mismatch(self):
        rules = failing_rules([new_issue_ops("ART-6", number=6, identifier="ART-7")])
        self.assertIn("L2", rules)

    def test_l2_identifier_collides_with_base(self):
        rules = failing_rules([new_issue_ops("ART-5", number=5, identifier="ART-1")])
        self.assertIn("L2", rules)

    def test_l3_state_history(self):
        rules = failing_rules([new_issue_ops(state_history_json="{}")])
        self.assertIn("L3", rules)

    def test_l4_done_without_completed_at(self):
        rules = failing_rules([new_issue_ops(state_id="Done")])
        self.assertIn("L4", rules)

    def test_l4_lifecycle_after_state_update(self):
        ops = [upd(ISSUES, {"id": "ZOM-1"}, state_id="Done")]
        rules = failing_rules(ops)
        self.assertIn("L4", rules)

    def test_l5_bad_parent_comment(self):
        ops = [
            new_issue_ops(),
            comment_op("comm_bad", "ART-2", created_at="2024-03-01T00:00:00Z", sequence=1,
                       parent_id="comm_missing"),
        ]
        self.assertIn("L5", failing_rules(ops))

    def test_l6_unknown_author(self):
        ops = [
            comment_op("comm_a", "ART-1", created_at="2024-03-02T00:00:00Z", sequence=1,
                       author_id="usr_ghost"),
        ]
        self.assertIn("L6", failing_rules(ops))

    def test_l7_comment_after_close(self):
        ops = [
            comment_op("comm_late", "ART-1", created_at="2024-03-06T00:00:00Z", sequence=1),
            upd(ISSUES, {"id": "ART-1"}, updated_at="2024-03-06T00:00:00Z"),
        ]
        base = make_base()
        findings = check_linear(apply(base, ops), base, freeze_utc=FREEZE)
        self.assertTrue(any(f.rule == "L7" and f.severity == "WARN" for f in findings))

    def test_l8_issue_updated_at_not_bumped(self):
        ops = [
            new_issue_ops(updated_at="2024-03-01T00:00:00Z"),
            comment_op("comm_1", "ART-2", created_at="2024-03-02T00:00:00Z", sequence=1),
        ]
        self.assertIn("L8", failing_rules(ops))

    def test_l9_sequence_gap(self):
        ops = [
            new_issue_ops(),
            comment_op("comm_1", "ART-2", created_at="2024-03-01T00:00:00Z", sequence=1),
            comment_op("comm_3", "ART-2", created_at="2024-03-02T00:00:00Z", sequence=3),
        ]
        self.assertIn("L9", failing_rules(ops))

    def test_l10_wrong_issue_counter(self):
        rules = failing_rules([upd(TEAMS, {"id": "team_ART"}, issue_counter=9)])
        self.assertIn("L10", rules)

    def test_l11_stale_project(self):
        ops = [
            ins(PROJECTS, **_project("proj_x", "team_ART", "2024-01-01T00:00:00Z")),
            new_issue_ops(project_id="proj_x", updated_at="2024-06-01T00:00:00Z"),
        ]
        base = make_base()
        findings = check_linear(apply(base, ops), base, freeze_utc=FREEZE)
        self.assertTrue(any(f.rule == "L11" and f.severity == "WARN" for f in findings))

    def test_l12_parent_in_other_team(self):
        # a warning only: the base itself has 129 cross-team parents per universe
        self.assertNotIn("L12", failing_rules([new_issue_ops(parent_id="ZOM-1")]))
        base = make_base()
        findings = check_linear(apply(base, [new_issue_ops(parent_id="ZOM-1")]), base, freeze_utc=FREEZE)
        self.assertTrue(any(f.rule == "L12" and f.severity == "WARN" for f in findings))

    def test_l1_impossible_calendar_values(self):
        base = make_base()
        issue = new_issue_ops()
        issue = Op(issue.table, issue.op, tuple((c, "2024-02-30" if c == "due_date" else v) for c, v in issue.cols))
        project = ins(PROJECTS, **dict(_project("proj_x", "team_ART", "2024-04-01T00:00:00Z"),
                                       started_at="2024-03-01T25:00:00Z"))
        findings = check_linear(apply(base, [issue, project]), base, freeze_utc=FREEZE)
        l1 = [f.message for f in findings if f.rule == "L1" and f.severity == "FAIL"]
        self.assertTrue(any("due_date" in m for m in l1), l1)
        self.assertTrue(any("started_at" in m for m in l1), l1)

    def test_l12_missing_parent(self):
        self.assertIn("L12", failing_rules([new_issue_ops(parent_id="ART-999")]))

    def test_l12_parent_cycle(self):
        ops = [
            new_issue_ops(),
            upd(ISSUES, {"id": "ART-1"}, parent_id="ART-2"),
            upd(ISSUES, {"id": "ART-2"}, parent_id="ART-1"),
        ]
        self.assertIn("L12", failing_rules(ops))


# --------------------------------------------------------------------------- corroboration

class CorroborationTests(unittest.TestCase):
    def test_corroborate_synthetic(self):
        report = corroborate(make_base())
        self.assertEqual(report["issues"], 2)
        self.assertEqual(report["base_comments"], 0)
        self.assertEqual(report["L1"]["pass_rate"], 1.0)
        self.assertEqual(report["L4"]["pass_rate"], 1.0)
        self.assertEqual(report["L12"]["pass_rate"], 1.0)
        self.assertEqual(report["max_number_by_team_key"], {"ART": 1, "ZOM": 1})
        self.assertIn("Done", report["state_types"]["completed"])


OC_ROOT = Path(__file__).resolve().parents[3]
UNIVERSES = {
    "normal": OC_ROOT / "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear",
    "synthcut": OC_ROOT / "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear",
}


class RealDataTests(unittest.TestCase):
    def test_corroborate_real_universes(self):
        seen = 0
        for name, folder in UNIVERSES.items():
            data_json = folder / "data.json"
            manifest_path = folder / "source_manifest.json"
            if not data_json.exists() or not manifest_path.exists():
                continue
            seen += 1
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            expected = next(entry["sha256"] for entry in manifest["files"]
                            if entry["path"] == "data.json")
            base = load_linear_base(data_json, expected)
            report = corroborate(base)
            print(f"[{name}] issues={report['issues']} base_comments={report['base_comments']} "
                  f"L1={report['L1']['pass_rate']} L4={report['L4']['pass_rate']} "
                  f"L12={report['L12']['pass_rate']}")
            print(f"[{name}] state_types={report['state_types']}")
            print(f"[{name}] max_number_by_team_key={report['max_number_by_team_key']}")
            self.assertEqual(report["base_comments"], 0)
        if seen == 0:
            self.skipTest("no Linear base export found")


if __name__ == "__main__":
    unittest.main()

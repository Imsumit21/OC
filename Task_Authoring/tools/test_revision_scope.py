"""Tests for revision_scope.py; run with: cd Task_Authoring/tools && python3.12 -B -m unittest test_revision_scope."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import unittest
from pathlib import Path

import revision_scope as rs
import selftest_sandbox

LINE = "The Tavern popup is still broken on Android, do not close ENG-900 yet"
PARENT = "slack.slack_messages:C0123ABCD/1700000000.000100"
REPLY = "slack.slack_messages:C0123ABCD/1700000300.000200"
DM = "D0BRIAN01/1700009000.000300"
MAIL = "owen@hg.co/<m1@mail>"


def gmail_copy(mailbox: str, msg: str, body: str) -> str:
    return ("INSERT INTO gmail.gmail_messages (id, thread_id, user_email, from_email, subject, body_text, date) VALUES "
            f"('{mailbox}/{msg}', '{mailbox}/1849', '{mailbox}', 'vincent@hg.co', 'tavern', '{body}', "
            "'2026-02-11T09:00:00Z');")


def comment(cid: str, body: str) -> str:
    return ("INSERT INTO linear.linear_comments (id, issue_id, author_id, body, created_at) VALUES "
            f"('{cid}', 'ENG-900', 'usr_2', '{body}', '2026-02-11T10:00:00Z');")


def budget(units) -> dict:
    return {"schema": rs.BUDGET_SCHEMA, "design_id": "D1", "revision": "rev2", "mode": "medium",
            "weight_basis": "surface", "total_weight": 10, "units": units}


def unit(uid: str, record_id: str, service: str) -> dict:
    return {"id": uid, "role": "anchor", "cause": "c", "carrier": "off_service_record",
            "habit": {"service": service, "action": "read"},
            "decider": {"service": service, "record_id": record_id, "container": "", "injected": True},
            "find_rate": [0.0, 0.2], "rows": [{"id": f"X{uid}", "weight": 5}]}


BUDGET = budget([unit("U1", MAIL, "gmail"), unit("U2", "comment_a1", "linear")])


class Diff(unittest.TestCase):
    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("test_revision_scope_")
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, name: str, text: str) -> Path:
        path = self.root / name
        path.write_text(text, encoding="utf-8")
        return path

    def diff(self, before: str, after: str) -> dict:
        return rs.diff_records(rs.load_records(before), rs.load_records(after))

    def test_added_removed_and_a_move(self):
        result = rs.diff_result(self.write("a.sql", rs._fixture_sql(LINE, None)),
                                self.write("b.sql", rs._fixture_sql(None, LINE + ".")))
        s = result["summary"]
        self.assertEqual((s["added"], s["removed"], s["changed"]), (2, 1, 0))
        self.assertEqual((s["content_records"], s["companion_records"], s["shape"]), (2, 1, "two_records"))
        self.assertEqual(s["content_states"], ["added", "removed"])
        self.assertTrue(s["fits_one_relocation"])
        self.assertEqual([(m["from"], m["to"]) for m in s["moves"]], [(DM, MAIL)])
        self.assertEqual(result["verdict"], "PASS")
        self.assertEqual([c["id"] for c in result["checks"]], ["revision.diff", "revision.parse"])
        self.assertEqual(len(result["bound_to"]), 2)

    def test_changed_record_names_its_fields(self):
        after = rs._fixture_sql(LINE, None).replace("thanks, noted", "thanks, noted, will do")
        d = self.diff(rs._fixture_sql(LINE, None), after)
        self.assertEqual([(e["state"], e["kind"], e["key"]) for e in d["entries"]], [("changed", "content", REPLY)])
        self.assertEqual(d["entries"][0]["changed_fields"], ["text"])
        self.assertEqual(d["entries"][0]["previous_text"], "thanks, noted")
        self.assertEqual(d["summary"]["shape"], "one_record")

    def test_reformatting_is_not_a_change(self):
        sql = rs._fixture_sql(LINE, None)
        reformatted = sql.replace("VALUES", "\n   VALUES").replace(";\n", ";\n\n-- a note\n").replace("BEGIN;", "BEGIN;\n")
        self.assertEqual(self.diff(sql, reformatted)["entries"], [])
        statements = [s for s in sql.splitlines() if s.startswith(("INSERT", "UPDATE"))]
        reordered = "\n".join(reversed(statements)) + "\n"
        self.assertEqual(self.diff(sql, reordered)["entries"], [])
        split = ("INSERT INTO linear.linear_issues (id, title) VALUES ('ENG-1', 'a');\n"
                 "UPDATE linear.linear_issues SET title = 'b' WHERE id = 'ENG-1';\n")
        folded = "INSERT INTO linear.linear_issues (id, title) VALUES ('ENG-1', 'b');\n"
        self.assertEqual(self.diff(split, folded)["entries"], [])
        swapped = "INSERT INTO linear.linear_issues (title, id) VALUES ('b', 'ENG-1');\n"
        self.assertEqual(self.diff(folded, swapped)["entries"], [])
        self.assertEqual(self.diff(sql, sql)["summary"]["shape"], "no_change")

    def test_companion_only_change(self):
        before = rs._fixture_sql(LINE, None)
        after = before.replace("SET updated_at = '2026-02-10T10:00:00Z'", "SET updated_at = '2026-02-11T10:00:00Z'")
        d = self.diff(before, after)
        self.assertEqual([e["kind"] for e in d["entries"]], ["companion"])
        self.assertEqual(d["summary"]["shape"], "companion_only")
        self.assertFalse(d["summary"]["fits_one_relocation"])

    def test_two_added_or_two_removed_is_not_one_relocation(self):
        base = rs._fixture_sql(LINE, None)
        added = self.diff(base, rs._fixture_sql(LINE, None, extra=comment("c_x", "one") + "\n" + comment("c_y", "two")))
        self.assertEqual(added["summary"]["content_states"], ["added", "added"])
        self.assertFalse(added["summary"]["fits_one_relocation"])
        removed = self.diff(rs._fixture_sql(LINE, None, extra=comment("c_x", "one") + "\n" + comment("c_y", "two")),
                            base)
        self.assertFalse(removed["summary"]["fits_one_relocation"])
        edited = self.diff(base, rs._fixture_sql(LINE + ", Brian", None).replace("thanks, noted", "noted"))
        self.assertEqual(edited["summary"]["content_states"], ["changed", "changed"])
        self.assertTrue(edited["summary"]["fits_one_relocation"])
        wide = self.diff(base, rs._fixture_sql(LINE + ", Brian", None, extra=comment("c_x", "one"))
                         .replace("thanks, noted", "noted"))
        self.assertEqual(wide["summary"]["shape"], "wider")
        self.assertFalse(wide["summary"]["fits_one_relocation"])

    def test_mail_copies_count_once(self):
        two = gmail_copy("owen@hg.co", "<m2@mail>", "the popup is back") + "\n" + \
            gmail_copy("vincent@hg.co", "<m2@mail>", "the popup is back")
        d = self.diff(rs._fixture_sql(LINE, None), rs._fixture_sql(LINE, None, extra=two))
        self.assertEqual(d["summary"]["added"], 2)
        self.assertEqual(d["summary"]["content_records"], 1)
        copies = [e for e in d["entries"] if e["table"] == "gmail.gmail_messages"]
        self.assertEqual(copies[0]["neighbours"]["copy"], ["gmail.gmail_messages:vincent@hg.co/<m2@mail>"])

    def test_unparsed_statement_is_listed(self):
        odd = "INSERT INTO slack.slack_messages SELECT * FROM x;\n"
        records = rs.load_records(odd)
        self.assertEqual(len(records["unparsed"]), 1)
        self.assertEqual(records["records"], {})
        d = self.diff(rs._fixture_sql(LINE, None), rs._fixture_sql(LINE, None, extra=odd))
        self.assertEqual([u["state"] for u in d["unparsed"]], ["added"])
        self.assertFalse(d["summary"]["fits_one_relocation"])

    def test_diff_is_deterministic(self):
        a = self.write("a.sql", rs._fixture_sql(LINE, None))
        b = self.write("b.sql", rs._fixture_sql(None, LINE + "."))
        one = json.dumps(rs._strip_private(rs.diff_result(a, b)), sort_keys=True)
        self.assertEqual(one, json.dumps(rs._strip_private(rs.diff_result(a, b)), sort_keys=True))
        self.assertEqual(rs.to_text(rs.diff_result(a, b)), rs.to_text(rs.diff_result(a, b)))

    def test_cli(self):
        a = self.write("a.sql", rs._fixture_sql(LINE, None))
        b = self.write("b.sql", rs._fixture_sql(None, LINE + "."))
        with contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(rs.main(["diff", "--previous", str(a), "--current", str(b), "--json"]), 0)
        data = json.loads(out.getvalue())
        self.assertEqual((data["tool"], data["version"], data["verdict"]), ("revision_scope", 1, "PASS"))
        self.assertTrue(all(not k.startswith("_") for k in data))
        with contextlib.redirect_stdout(io.StringIO()) as out:
            rs.main(["diff", "--previous", str(a), "--current", str(b)])
        self.assertTrue(out.getvalue().startswith("REVISION SCOPE (diff): PASS"))
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(rs.main(["diff", "--previous", str(self.root / "nope.sql"), "--current", str(b)]), 2)


class Neighbours(unittest.TestCase):
    def setUp(self):
        sql = rs._fixture_sql(None, LINE + ".", extra=gmail_copy("vincent@hg.co", "<m1@mail>", LINE))
        self.records = rs.load_records(sql)["records"]

    def test_thread_parent_and_reply(self):
        near = rs.neighbours(self.records[REPLY], self.records)
        self.assertIn(PARENT, near["thread"])
        self.assertIn(REPLY, rs.neighbours(self.records[PARENT], self.records)["thread"])

    def test_comment_and_its_issue(self):
        near = rs.neighbours(self.records["linear.linear_comments:comment_a1"], self.records)
        self.assertIn("linear.linear_issues:ENG-900", near["thread"])

    def test_mail_copy_and_thread_row(self):
        near = rs.neighbours(self.records[f"gmail.gmail_messages:{MAIL}"], self.records)
        self.assertEqual(near["copy"], ["gmail.gmail_messages:vincent@hg.co/<m1@mail>"])
        self.assertIn("gmail.gmail_threads:owen@hg.co/1849333980856689601", near["thread"])

    def test_reference_by_text(self):
        near = rs.neighbours(self.records["linear.linear_issues:ENG-900"], self.records)
        self.assertIn(PARENT, near["reference"])            # the root post names ENG-900

    def test_container_and_base(self):
        sql = rs._fixture_sql(LINE, None, extra=(
            "INSERT INTO slack.slack_messages (id, channel_id, ts, user_id, text, thread_ts_legacy, thread_parent_id, "
            "reply_count) VALUES ('" + hashlib.sha256(b"D0BRIAN01|1700009500.000100").hexdigest()[:32] + "', "
            "'D0BRIAN01', '1700009500.000100', 'U_OWEN', 'thanks', NULL, NULL, 0);"))
        records = rs.load_records(sql)["records"]
        near = rs.neighbours(records[f"slack.slack_messages:{DM}"], records)
        self.assertEqual(near["container"], ["slack.slack_messages:D0BRIAN01/1700009500.000100"])
        self.assertIn("linear.linear_issues:ENG-900", near["reference"])     # the DM names the issue update
        orphan = rs.load_records(comment("c_9", "see ENG-901").replace("'ENG-900'", "'ENG-901'"))["records"]
        self.assertEqual(rs.neighbours(orphan["linear.linear_comments:c_9"], orphan)["base"], ["ENG-901"])

    def test_scope_ids_cover_changes_neighbours_and_base(self):
        d = rs.diff_records(rs.load_records(rs._fixture_sql(LINE, None)),
                            rs.load_records(rs._fixture_sql(LINE, None).replace("thanks, noted", "noted")))
        d["_previous"] = rs.load_records(rs._fixture_sql(LINE, None))
        d["_current"] = rs.load_records(rs._fixture_sql(LINE, None).replace("thanks, noted", "noted"))
        ids = rs.scope_ids(d)
        self.assertIn("C0123ABCD/1700000300.000200", ids)       # the changed reply
        self.assertIn("C0123ABCD/1700000000.000100", ids)       # its parent


class Relocation(unittest.TestCase):
    def setUp(self):
        self._tmp = selftest_sandbox.scratch_tmp("test_revision_scope_")
        self.root = Path(self._tmp.name)
        self.task = self.root / "task"
        (self.task / "Working_Files").mkdir(parents=True)
        self.prev = self.root / "rev1.sql"
        self.prev.write_text(rs._fixture_sql(LINE, None), encoding="utf-8")
        self.cur = self.task / rs.SQL_NAME
        self.cur.write_text(rs._fixture_sql(None, LINE + "."), encoding="utf-8")
        self.budget_path = self.task / "Working_Files" / rs.BUDGET_NAME
        self.budget_path.write_text(json.dumps(BUDGET), encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def check(self, **kw) -> dict:
        return rs.evaluate(self.task, self.prev, **kw)

    def test_one_decider_moved_with_its_companion_passes(self):
        r = self.check()
        self.assertEqual(r["verdict"], "PASS", r["checks"])
        self.assertEqual(r["relocation"]["units"], ["U1"])
        self.assertIn(rs._rel(self.budget_path), r["bound_to"])
        roles = {k.split(":")[0]: v[1] for k, v in r["relocation"]["attribution"].items()}
        self.assertTrue(any(v == "companion" for v in roles.values()))
        self.assertTrue(any(v.startswith("decider (old home") for v in roles.values()))

    def test_previous_budget_names_the_old_home(self):
        old = self.root / "budget_rev1.json"
        old.write_text(json.dumps(budget([unit("U1", DM, "slack"), unit("U2", "comment_a1", "linear")])),
                       encoding="utf-8")
        r = self.check(previous_budget=old)
        self.assertEqual(r["verdict"], "PASS", r["checks"])
        self.assertIn(rs._rel(old), r["bound_to"])

    def test_extra_record_warns(self):
        self.cur.write_text(rs._fixture_sql(None, LINE + ".", extra=comment("comment_b2", "one more decoy note")),
                            encoding="utf-8")
        r = self.check()
        self.assertEqual(r["verdict"], "WARN")
        self.assertIn("comment_b2", r["checks"][0]["detail"])

    def test_two_units_warn(self):
        self.cur.write_text(rs._fixture_sql(None, LINE + ".").replace("it''s the last one", "it''s the last one, I think"),
                            encoding="utf-8")
        r = self.check()
        self.assertEqual(r["verdict"], "WARN")
        self.assertIn("2 units moved", r["checks"][0]["detail"])

    def test_unit_mismatch_warns(self):
        self.assertEqual(self.check(unit="U2")["verdict"], "WARN")
        self.assertIn("not in the budget", self.check(unit="U9")["checks"][0]["detail"])

    def test_prompt_sentence_added_warns(self):
        old_prompt = self.root / "old_prompt.txt"
        old_prompt.write_text("Can you sort the bug list? Reply to Arthur when done.", encoding="utf-8")
        (self.task / rs.PROMPT_NAME).write_text("Can you sort the bug list? Check my mail too. Reply to Arthur when "
                                                "done.", encoding="utf-8")
        r = self.check(previous_prompt=old_prompt)
        self.assertEqual(r["verdict"], "WARN")
        self.assertEqual(r["relocation"]["added_sentences"], ["Check my mail too."])
        (self.task / rs.PROMPT_NAME).write_text(old_prompt.read_text(), encoding="utf-8")
        self.assertEqual(self.check(previous_prompt=old_prompt)["verdict"], "PASS")

    def test_no_budget_or_no_change_warns(self):
        self.budget_path.unlink()
        r = self.check()
        self.assertEqual(r["verdict"], "WARN")
        self.assertIn(rs.BUDGET_NAME, r["checks"][0]["detail"])
        self.cur.write_text(self.prev.read_text(), encoding="utf-8")
        self.assertIn("nothing was relocated", self.check()["checks"][0]["detail"])

    def test_bad_budget_is_a_usage_error(self):
        self.budget_path.write_text("{}", encoding="utf-8")
        with self.assertRaises(rs.UsageError):
            self.check()
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(rs.main(["relocation", "--task-dir", str(self.task), "--previous", str(self.prev)]), 2)

    def test_scope_reread_and_checklist(self):
        sc = rs.scope_result(self.task, self.prev)
        self.assertIn(MAIL, {x["id"] for x in sc["reread"]["changed"]})
        self.assertEqual([x["id"] for x in sc["reread"]["removed"]], [DM])
        redo = {i["id"] for i in sc["checklist"] if i["redo"]}
        skip = {i["id"] for i in sc["checklist"] if not i["redo"]}
        self.assertTrue({"dossier.1A", "dossier.1E", "dossier.1F", "dossier.S4.gmail", "tool.sql_lint",
                         "tool.coherence_sweep", "tool.relocation"} <= redo, redo)
        self.assertTrue({"dossier.integrations", "dossier.prompt_brief", "dossier.followups", "tool.base_claims"}
                        <= skip, skip)
        self.assertFalse(redo & skip)
        text = rs.to_text(sc)
        self.assertTrue(text.startswith("REVISION SCOPE (scope): PASS"))
        self.assertIn("- [ ]", text)
        self.assertIn("- [skip]", text)
        self.assertEqual(json.dumps(rs._strip_private(sc), sort_keys=True),
                         json.dumps(rs._strip_private(rs.scope_result(self.task, self.prev)), sort_keys=True))

    def test_relocation_cli_exit_code(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            code = rs.main(["relocation", "--task-dir", str(self.task), "--previous", str(self.prev), "--json"])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out.getvalue())["checks"][0]["id"], "revision.relocation")


if __name__ == "__main__":
    unittest.main()

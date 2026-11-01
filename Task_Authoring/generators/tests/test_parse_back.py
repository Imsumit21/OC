"""Tests for validate/parse_back.py: the eval tokenizer as an independent parse-back engine."""
from __future__ import annotations

import hashlib
import unittest
from decimal import Decimal
from pathlib import Path

from generators.core import sqlvalue
from generators.core.ops import INSERT, UPDATE, Op
from generators.tests.fixtures import literal_corpus
from generators.validate import compare, parse_back

HERE = Path(__file__).resolve()
TASK_AUTHORING = HERE.parents[2]
SCHEMA = TASK_AUTHORING / "references" / "universe_schema_live.json"
TOOLS = HERE.parents[3] / "Evals" / "tools"
MARKER = "-- Are you planning to inject? Yes"


def listing(root: Path):
    """(relative path, size) for every file under root: the bytecode-write guard."""
    if not root.is_dir():
        return []
    return sorted((str(path.relative_to(root)), path.stat().st_size)
                  for path in root.rglob("*") if path.is_file())


# Snapshot before anything imports the eval tokenizer, so a __pycache__ write is visible.
TOOLS_BEFORE = listing(TOOLS)


def value_column(value):
    if value is None:
        return "status"
    if isinstance(value, bool):
        return "is_user"
    if isinstance(value, (int, Decimal)):
        return "age"
    return "description"


def insert_op(value) -> Op:
    column = value_column(value)
    return Op(table="contacts.contacts", op=INSERT,
              cols=(("contact_id", "c-1"), (column, value)))


def insert_sql(value) -> str:
    column = value_column(value)
    return ("INSERT INTO contacts.contacts (contact_id, %s) VALUES ('c-1', %s);"
            % (sqlvalue.ident(column), sqlvalue.literal(value)))


class CorpusRoundTripTest(unittest.TestCase):
    def test_every_corpus_value_round_trips(self):
        values = literal_corpus.cases()
        self.assertEqual(240, len(values))
        text = "\n".join([MARKER, "BEGIN;", *(insert_sql(v) for v in values), "COMMIT;", ""])
        ops = parse_back.parse_ops(text, schema_path=SCHEMA)
        self.assertEqual(len(values), len(ops))
        diffs = compare.compare_ops([insert_op(v) for v in values], ops)
        self.assertEqual([], diffs, f"{len(diffs)} diff(s); first: {diffs[0] if diffs else None}")
        for value, op in zip(values, ops):
            with self.subTest(value=repr(value)[:50]):
                self.assertEqual(insert_op(value), op)

    def test_individually_without_begin_commit(self):
        for value in literal_corpus.cases()[:40]:
            with self.subTest(value=repr(value)[:50]):
                ops = parse_back.parse_ops(MARKER + "\n" + insert_sql(value) + "\n", schema_path=SCHEMA)
                self.assertEqual([insert_op(value)], ops)

    def test_begin_commit_emit_no_ops(self):
        self.assertEqual([], parse_back.parse_ops("BEGIN;\nCOMMIT;\n", schema_path=SCHEMA))
        self.assertEqual([], parse_back.parse_ops(MARKER + "\n", schema_path=SCHEMA))

    def test_update_round_trip(self):
        text = ("UPDATE contacts.contacts SET description = E'line one\\nline two', age = -12 "
                "WHERE contact_id = 'c-1';\n")
        ops = parse_back.parse_ops(text, schema_path=SCHEMA)
        expected = Op(table="contacts.contacts", op=UPDATE,
                      cols=(("description", "line one\nline two"), ("age", -12)),
                      where=(("contact_id", "c-1"),))
        self.assertEqual([expected], ops)

    def test_insert_null_and_bools(self):
        text = ("INSERT INTO contacts.contacts (contact_id, status, is_user) VALUES ('c-1', NULL, true);\n")
        self.assertEqual([Op(table="contacts.contacts", op=INSERT,
                             cols=(("contact_id", "c-1"), ("status", None), ("is_user", True)))],
                         parse_back.parse_ops(text, schema_path=SCHEMA))


class ParserLimitTest(unittest.TestCase):
    def test_count_mismatch_raises(self):
        text = "INSERT INTO contacts.contacts (contact_id, first_name) VALUES ('a');"
        with self.assertRaises(parse_back.ParseBackError) as caught:
            parse_back.parse_ops(text, schema_path=SCHEMA)
        self.assertIn("does not match value count", str(caught.exception))
        self.assertEqual(1, caught.exception.line)

    def test_too_many_values_raises(self):
        text = "INSERT INTO contacts.contacts (contact_id) VALUES ('a', 'b');"
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.parse_ops(text, schema_path=SCHEMA)

    def test_update_two_key_where(self):
        text = ("UPDATE gsheets.sheets_sheets SET title = 'T' "
                "WHERE spreadsheet_id = 'sp' AND sheet_id = 7;\n")
        ops = parse_back.parse_ops(text, schema_path=SCHEMA)
        self.assertEqual((("spreadsheet_id", "sp"), ("sheet_id", 7)), ops[0].where)

    def test_quoted_camel_case_column_keeps_schema_case(self):
        ident = sqlvalue.ident("dateLastActivity")
        self.assertEqual('"dateLastActivity"', ident)
        text = f"UPDATE trello.trello_boards SET name = 'n' WHERE {ident} = '2026-01-01T00:00:00Z';\n"
        ops = parse_back.parse_ops(text, schema_path=SCHEMA)
        self.assertEqual("dateLastActivity", ops[0].where[0][0])
        self.assertEqual("name", ops[0].cols[0][0])

    def test_negative_decimal_is_exact(self):
        text = "UPDATE contacts.contacts SET age = -1277953.9648391008 WHERE contact_id = 'c-1';\n"
        ops = parse_back.parse_ops(text, schema_path=SCHEMA)
        value = ops[0].cols[0][1]
        self.assertIsInstance(value, Decimal)
        self.assertEqual(Decimal("-1277953.9648391008"), value)
        self.assertEqual("-1277953.9648391008", str(value))

    def test_big_integer_and_decimal_text(self):
        text = ("INSERT INTO contacts.contacts (contact_id, age) "
                "VALUES ('c-1', 9223372036854775807);\n")
        self.assertEqual(9223372036854775807,
                         parse_back.parse_ops(text, schema_path=SCHEMA)[0].cols[1][1])
        text = ("INSERT INTO contacts.contacts (contact_id, age) VALUES ('c-1', 0.10);\n")
        value = parse_back.parse_ops(text, schema_path=SCHEMA)[0].cols[1][1]
        self.assertEqual(Decimal("0.10"), value)
        self.assertEqual("0.10", str(value))

    def test_wall_clock_function_raises(self):
        text = "INSERT INTO contacts.contacts (contact_id, created_at) VALUES ('c-1', now());\n"
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.parse_ops(text, schema_path=SCHEMA)

    def test_expression_and_cast_values_raise(self):
        for value in ("1 + 1", "'a'::text", "coalesce(NULL, 'x')", "DEFAULT"):
            text = f"INSERT INTO contacts.contacts (contact_id, description) VALUES ('c-1', {value});\n"
            with self.subTest(value=value):
                with self.assertRaises(parse_back.ParseBackError):
                    parse_back.parse_ops(text, schema_path=SCHEMA)

    def test_cte_raises(self):
        text = ("WITH x AS (SELECT 1) UPDATE contacts.contacts SET first_name = 'n' "
                "WHERE contact_id = 'c-1';\n")
        with self.assertRaises(parse_back.ParseBackError) as caught:
            parse_back.parse_ops(text, schema_path=SCHEMA)
        self.assertIn("not INSERT/UPDATE/BEGIN/COMMIT", str(caught.exception))

    def test_do_block_raises(self):
        text = ("DO $$ BEGIN UPDATE contacts.contacts SET first_name = 'n' "
                "WHERE contact_id = 'c-1'; END $$;\n")
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.parse_ops(text, schema_path=SCHEMA)

    def test_delete_raises(self):
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.parse_ops("DELETE FROM contacts.contacts WHERE contact_id = 'c-1';\n",
                                 schema_path=SCHEMA)

    def test_on_conflict_raises(self):
        text = ("INSERT INTO contacts.contacts (contact_id) VALUES ('c-1') "
                "ON CONFLICT (contact_id) DO NOTHING;\n")
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.parse_ops(text, schema_path=SCHEMA)

    def test_multi_row_values_raise(self):
        text = "INSERT INTO contacts.contacts (contact_id) VALUES ('a'), ('b');\n"
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.parse_ops(text, schema_path=SCHEMA)

    def test_unknown_column_raises(self):
        text = "INSERT INTO contacts.contacts (contact_id, not_a_column) VALUES ('a', 1);\n"
        with self.assertRaises(parse_back.ParseBackError) as caught:
            parse_back.parse_ops(text, schema_path=SCHEMA)
        self.assertIn("not in the universe schema", str(caught.exception))

    def test_unknown_table_raises(self):
        text = "INSERT INTO contacts.nope (contact_id) VALUES ('a');\n"
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.parse_ops(text, schema_path=SCHEMA)

    def test_update_without_where_raises(self):
        text = "UPDATE contacts.contacts SET first_name = 'n';\n"
        with self.assertRaises(parse_back.ParseBackError) as caught:
            parse_back.parse_ops(text, schema_path=SCHEMA)
        self.assertIn("WHERE", str(caught.exception))

    def test_where_with_or_raises(self):
        text = ("UPDATE contacts.contacts SET first_name = 'n' "
                "WHERE contact_id = 'a' OR contact_id = 'b';\n")
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.parse_ops(text, schema_path=SCHEMA)

    def test_update_set_expression_raises(self):
        text = "UPDATE contacts.contacts SET age = age + 1 WHERE contact_id = 'c-1';\n"
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.parse_ops(text, schema_path=SCHEMA)

    def test_unbalanced_parentheses_raise(self):
        text = "INSERT INTO contacts.contacts (contact_id VALUES ('a');\n"
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.parse_ops(text, schema_path=SCHEMA)

    def test_unterminated_string_raises(self):
        text = "INSERT INTO contacts.contacts (contact_id) VALUES ('a);\n"
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.parse_ops(text, schema_path=SCHEMA)

    def test_duplicate_column_raises(self):
        text = "INSERT INTO contacts.contacts (contact_id, contact_id) VALUES ('a', 'b');\n"
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.parse_ops(text, schema_path=SCHEMA)


class PinsAndIsolationTest(unittest.TestCase):
    def test_pins_record_both_files(self):
        parser = parse_back.load_eval_parser()
        self.assertEqual({"hg_injection_lint.py", "hg_universe.py"}, set(parser.pins))
        for name, digest in parser.pins.items():
            with self.subTest(name=name):
                self.assertEqual(64, len(digest))
                self.assertEqual(hashlib.sha256((TOOLS / name).read_bytes()).hexdigest(), digest)

    def test_nothing_is_written_under_evals(self):
        parse_back.load_eval_parser()
        parse_back.parse_ops("BEGIN;\nCOMMIT;\n", schema_path=SCHEMA)
        self.assertEqual(TOOLS_BEFORE, listing(TOOLS))

    def test_custom_directory_must_exist(self):
        with self.assertRaises(parse_back.ParseBackError):
            parse_back.load_eval_parser(Path("/nonexistent/evals/tools"))


if __name__ == "__main__":
    unittest.main()

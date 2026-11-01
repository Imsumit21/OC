"""Tests for validate/grammar.py: the restricted-grammar checker."""
from __future__ import annotations

import unittest

from generators.core import sqlvalue
from generators.tests.fixtures import literal_corpus
from generators.validate.grammar import MARKER, GrammarError, check_sql, split_literals


def insert_line(value, column="description", table="contacts.contacts", key="'c-1'"):
    return (f"INSERT INTO {table} (contact_id, {sqlvalue.ident(column)}) "
            f"VALUES ({key}, {sqlvalue.literal(value)});")


def script(*lines):
    return "\n".join([MARKER, "BEGIN;", *lines, "COMMIT;", ""])


class CorpusTest(unittest.TestCase):
    def test_corpus_size(self):
        self.assertEqual(240, len(literal_corpus.cases()))
        self.assertEqual(240, len(literal_corpus.cases(seed=7)))
        self.assertEqual(3, len(literal_corpus.cases(n=3)))

    def test_every_corpus_literal_passes(self):
        for value in literal_corpus.cases():
            with self.subTest(value=repr(value)[:60]):
                self.assertEqual([], check_sql(script(insert_line(value))))
                self.assertEqual([], check_sql(insert_line(value), require_marker=False))

    def test_identifier_forms(self):
        for table, column in (
            ("contacts.contacts", "first_name"),
            ("trello.trello_boards", "dateLastActivity"),      # sqlvalue quotes mixed case
            ("gsheets.sheets_sheets", "index"),                # sqlvalue quotes a reserved word
        ):
            line = (f"INSERT INTO {table} (contact_id, {sqlvalue.ident(column)}) "
                    f"VALUES ('c-1', 'x');")
            with self.subTest(column=column):
                self.assertEqual([], check_sql(script(line)))

    def test_update_line(self):
        text = script(
            "UPDATE contacts.contacts SET first_name = 'O''Brien', age = -12 WHERE contact_id = 'c-1';",
            "UPDATE gsheets.sheets_sheets SET title = E'a\\nb' "
            "WHERE spreadsheet_id = 'sp' AND sheet_id = 7;",
        )
        self.assertEqual([], check_sql(text))

    def test_blank_and_comment_lines(self):
        text = "\n".join([
            MARKER,
            "",
            "-- a comment between statements",
            "BEGIN;",
            "",
            insert_line("x"),
            "-- trailing comment",
            "COMMIT;",
            "",
        ])
        self.assertEqual([], check_sql(text))

    def test_no_marker_allowed(self):
        self.assertEqual([], check_sql(insert_line("x"), require_marker=False))
        self.assertTrue(check_sql(insert_line("x")))


class SplitLiteralsTest(unittest.TestCase):
    def test_raw_texts(self):
        text = "(NULL, true, false, -1, 2.50, 'a''b', E'x\\ny', 'c, d', '')"
        self.assertEqual(
            ["NULL", "true", "false", "-1", "2.50", "'a''b'", "E'x\\ny'", "'c, d'", "''"],
            split_literals(text))

    def test_forms(self):
        self.assertEqual(["1", "'a'"], split_literals("VALUES (1, 'a')"))
        self.assertEqual(["1", "'a'"], split_literals("1, 'a'"))
        self.assertEqual(["1.50"], split_literals("(1.50);"))

    def test_malformed(self):
        with self.assertRaises(GrammarError):
            split_literals("(1,'a')")            # missing the exact ", " separator
        with self.assertRaises(GrammarError):
            split_literals("('unterminated)")


class ViolationTest(unittest.TestCase):
    def assertRejected(self, text, needle, line=None):
        errors = check_sql(text)
        self.assertTrue(errors, f"expected a grammar error for {text!r}")
        blob = " | ".join(error.message for error in errors)
        self.assertIn(needle, blob, f"{needle!r} not in {blob!r}")
        if line is not None:
            self.assertIn(line, {error.line for error in errors})
        return errors

    def test_two_statements_on_one_line(self):
        text = script(insert_line("a") + " " + insert_line("b"))
        self.assertRejected(text, "one statement per line")

    def test_multiline_statement(self):
        text = "\n".join([
            MARKER,
            "BEGIN;",
            "INSERT INTO contacts.contacts (contact_id,",
            "  first_name) VALUES ('c-1', 'x');",
            "COMMIT;",
        ])
        errors = check_sql(text)
        self.assertEqual([3, 4], [error.line for error in errors])

    def test_cast(self):
        line = "INSERT INTO contacts.contacts (contact_id) VALUES ('c-1'::text);"
        self.assertRejected(script(line), "casts are not allowed")

    def test_function_value(self):
        line = "INSERT INTO contacts.contacts (contact_id, created_at) VALUES ('c-1', now());"
        self.assertRejected(script(line), "functions")

    def test_on_conflict(self):
        line = ("INSERT INTO contacts.contacts (contact_id) VALUES ('c-1') "
                "ON CONFLICT (contact_id) DO NOTHING;")
        self.assertRejected(script(line), "';' at the end")

    def test_count_mismatch(self):
        line = "INSERT INTO contacts.contacts (contact_id, first_name) VALUES ('c-1');"
        self.assertRejected(script(line), "does not match value count")

    def test_duplicate_column(self):
        line = "INSERT INTO contacts.contacts (contact_id, contact_id) VALUES ('a', 'b');"
        self.assertRejected(script(line), "duplicate column")

    def test_bad_escape_in_e_string(self):
        line = "INSERT INTO contacts.contacts (contact_id, description) VALUES ('c-1', E'a\\qb');"
        self.assertRejected(script(line), "unsupported backslash escape")

    def test_missing_marker(self):
        errors = check_sql("BEGIN;\n" + insert_line("x") + "\nCOMMIT;\n")
        self.assertEqual([1], [error.line for error in errors])
        self.assertIn("line 1 must be exactly", errors[0].message)

    def test_update_without_where(self):
        line = "UPDATE contacts.contacts SET first_name = 'x';"
        self.assertRejected(script(line), "requires a WHERE clause")

    def test_comment_inside_statement(self):
        line = "INSERT INTO contacts.contacts (contact_id) VALUES ('c-1' -- note);"
        self.assertRejected(script(line), "comment is not allowed inside a statement")

    def test_leading_whitespace(self):
        self.assertRejected(script(" " + insert_line("x")), "not an INSERT or UPDATE statement")

    def test_unquoted_uppercase_identifier(self):
        line = "INSERT INTO contacts.contacts (Contact_Id) VALUES ('c-1');"
        self.assertRejected(script(line), "expected an identifier")

    def test_multi_row_values(self):
        line = "INSERT INTO contacts.contacts (contact_id) VALUES ('a'), ('b');"
        self.assertRejected(script(line), "';' at the end")

    def test_cte_and_do_block_and_dollar_quote(self):
        self.assertRejected(script("WITH x AS (SELECT 1) SELECT 1;"), "not an INSERT or UPDATE")
        self.assertRejected(script("DO $$ BEGIN NULL; END $$;"), "not an INSERT or UPDATE")
        line = "INSERT INTO contacts.contacts (contact_id) VALUES ($$a$$);"
        self.assertRejected(script(line), "expected a literal")

    def test_bad_comment_prefix(self):
        self.assertRejected(script("--no space after the dashes"), "must start with '-- '")

    def test_unterminated_string(self):
        line = "INSERT INTO contacts.contacts (contact_id) VALUES ('c-1);"
        self.assertRejected(script(line), "unterminated string")

    def test_crlf_file(self):
        errors = check_sql(script(insert_line("x")).replace("\n", "\r\n"))
        self.assertTrue(errors)
        self.assertIn("carriage return", " | ".join(error.message for error in errors))

    def test_wrong_separators(self):
        for line in (
            "INSERT INTO contacts.contacts (contact_id,first_name) VALUES ('a', 'b');",
            "INSERT INTO contacts.contacts (contact_id) VALUES ('a','b');",
            "INSERT INTO contacts.contacts (contact_id) VALUES ('a') ;",
            "INSERT INTO contacts.contacts (contact_id) VALUES ('a'); ",
        ):
            with self.subTest(line=line):
                self.assertTrue(check_sql(script(line)))

    def test_unterminated_e_string_trailing_backslash(self):
        line = "INSERT INTO contacts.contacts (contact_id) VALUES (E'abc\\"
        self.assertRejected(script(line), "unterminated E'' string")


if __name__ == "__main__":
    unittest.main()

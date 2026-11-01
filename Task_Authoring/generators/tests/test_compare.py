"""Tests for validate/compare.py: diffing intended ops against parsed-back ops."""
from __future__ import annotations

import unittest
from decimal import Decimal

from generators.core.ops import INSERT, UPDATE, Op
from generators.validate.compare import Diff, compare_multiset, compare_ops, values_equal


def insert(table="contacts.contacts", pairs=(("contact_id", "c-1"), ("first_name", "Ada"))):
    return Op(table=table, op=INSERT, cols=tuple(pairs))


def update(table="contacts.contacts", set_pairs=(("first_name", "Ada"),),
           where_pairs=(("contact_id", "c-1"),)):
    return Op(table=table, op=UPDATE, cols=tuple(set_pairs), where=tuple(where_pairs))


def kinds(diffs):
    return [diff.kind for diff in diffs]


class OrderedCompareTest(unittest.TestCase):
    def test_identical(self):
        intended = [insert(), update(), insert(table="gsheets.sheets_sheets",
                                               pairs=(("spreadsheet_id", "sp"),))]
        self.assertEqual([], compare_ops(intended, list(intended)))

    def test_empty(self):
        self.assertEqual([], compare_ops([], []))

    def test_length(self):
        diffs = compare_ops([insert()], [])
        self.assertEqual(["length"], kinds(diffs))
        self.assertEqual((1, 0), (diffs[0].intended, diffs[0].parsed))

    def test_table_and_op(self):
        self.assertEqual(["table"], kinds(compare_ops(
            [insert(table="contacts.contacts")], [insert(table="gmail.gmail_users")])))
        diffs = compare_ops([insert(pairs=(("contact_id", "c-1"),))],
                            [update(set_pairs=(("contact_id", "c-1"),))])
        self.assertEqual("op", diffs[0].kind)
        self.assertEqual(("insert", "update"), (diffs[0].intended, diffs[0].parsed))

    def test_null_is_not_empty_string(self):
        diffs = compare_ops([insert(pairs=(("contact_id", None),))],
                            [insert(pairs=(("contact_id", ""),))])
        self.assertEqual(["value"], kinds(diffs))
        self.assertIsNone(diffs[0].intended)
        self.assertEqual("", diffs[0].parsed)
        self.assertIn("contact_id", diffs[0].message)

    def test_bool_is_not_int(self):
        diffs = compare_ops([insert(pairs=(("is_user", True),))],
                            [insert(pairs=(("is_user", 1),))])
        self.assertEqual(["value"], kinds(diffs))
        self.assertFalse(values_equal(True, 1))
        self.assertFalse(values_equal(1, True))
        self.assertFalse(values_equal(False, 0))

    def test_decimal_and_int_are_equal(self):
        self.assertEqual([], compare_ops([insert(pairs=(("age", Decimal("1.0")),))],
                                         [insert(pairs=(("age", 1),))]))
        self.assertEqual([], compare_ops([insert(pairs=(("age", 1),))],
                                         [insert(pairs=(("age", Decimal("1.0")),))]))
        self.assertTrue(values_equal(Decimal("0.10"), Decimal("0.1")))

    def test_decimal_scale_differs_only_in_text(self):
        # Same numeric value at different scale: no diff (numbers compare by Decimal).
        self.assertEqual([], compare_ops([insert(pairs=(("age", Decimal("1.50")),))],
                                         [insert(pairs=(("age", Decimal("1.5")),))]))

    def test_string_whitespace_matters(self):
        diffs = compare_ops([insert(pairs=(("description", "a"),))],
                            [insert(pairs=(("description", "a "),))])
        self.assertEqual(["value"], kinds(diffs))
        self.assertEqual(("a", "a "), (diffs[0].intended, diffs[0].parsed))

    def test_column_order(self):
        diffs = compare_ops([insert(pairs=(("contact_id", "c"), ("first_name", "Ada"))),
                             insert(pairs=(("contact_id", "c"),))],
                            [insert(pairs=(("first_name", "Ada"), ("contact_id", "c"))),
                             insert(pairs=(("first_name", "Ada"),))])
        self.assertEqual(["column", "column"], kinds(diffs))
        self.assertEqual(("contact_id", "first_name"), diffs[0].intended)

    def test_column_count(self):
        diffs = compare_ops([insert(pairs=(("contact_id", "c"), ("first_name", "Ada")))],
                            [insert(pairs=(("contact_id", "c"),))])
        self.assertEqual(["column"], kinds(diffs))

    def test_json_format_is_informational(self):
        diffs = compare_ops(
            [insert(pairs=(("prefs_json", '{"a": 1, "b": [2, 3]}'),))],
            [insert(pairs=(("prefs_json", '{"a":1,"b":[2,3]}'),))])
        self.assertEqual(["json_format"], kinds(diffs))
        self.assertEqual("prefs_json", diffs[0].column)

    def test_json_value_difference(self):
        diffs = compare_ops([insert(pairs=(("prefs_json", '{"a": 1}'),))],
                            [insert(pairs=(("prefs_json", '{"a": 2}'),))])
        self.assertEqual(["value"], kinds(diffs))

    def test_json_text_on_one_side_only(self):
        diffs = compare_ops([insert(pairs=(("prefs_json", '{"a": 1}'),))],
                            [insert(pairs=(("prefs_json", None),))])
        self.assertEqual(["value"], kinds(diffs))

    def test_where_pairs(self):
        diffs = compare_ops([update(where_pairs=(("contact_id", "c-1"),))],
                            [update(where_pairs=(("contact_id", "c-2"),))])
        self.assertEqual(["value"], kinds(diffs))
        self.assertIn("where", diffs[0].message)
        self.assertEqual("contact_id", diffs[0].column)

    def test_where_names(self):
        diffs = compare_ops([update(where_pairs=(("contact_id", "c-1"),))],
                            [update(where_pairs=(("spreadsheet_id", "c-1"),))])
        self.assertEqual(["column"], kinds(diffs))

    def test_diff_shape(self):
        diffs = compare_ops([insert()], [insert(pairs=(("contact_id", "other"),))])
        diff = next(d for d in diffs if d.kind == "value")
        self.assertIsInstance(diff, Diff)
        self.assertEqual(0, diff.index)
        self.assertEqual("contacts.contacts", diff.table)
        self.assertEqual("contact_id", diff.column)
        self.assertIsInstance(diff.message, str)


class MultisetCompareTest(unittest.TestCase):
    KEY = staticmethod(lambda op: (op.col("contact_id"),))

    def test_identical(self):
        self.assertEqual([], compare_multiset([insert(), update()], [insert(), update()],
                                              self.KEY))

    def test_order_does_not_matter(self):
        left = [insert(pairs=(("contact_id", "a"), ("first_name", "A"))),
                insert(pairs=(("contact_id", "b"), ("first_name", "B")))]
        right = list(reversed(left))
        self.assertEqual([], compare_multiset(left, right, self.KEY))

    def test_missing_and_extra(self):
        diffs = compare_multiset([insert(pairs=(("contact_id", "a"),))],
                                 [insert(pairs=(("contact_id", "b"),))], self.KEY)
        self.assertEqual(["missing", "extra"], kinds(diffs))

    def test_value_difference(self):
        diffs = compare_multiset(
            [insert(pairs=(("contact_id", "a"), ("first_name", "Ada"), ("is_user", True)))],
            [insert(pairs=(("contact_id", "a"), ("first_name", "Ada"), ("is_user", 1)))],
            self.KEY)
        self.assertEqual(["value"], kinds(diffs))
        self.assertEqual("is_user", diffs[0].column)

    def test_omitted_as_null(self):
        intended = [insert(pairs=(("contact_id", "a"), ("status", None)))]
        parsed = [insert(pairs=(("contact_id", "a"),))]
        self.assertEqual(["column"], kinds(compare_multiset(intended, parsed, self.KEY)))
        self.assertEqual([], compare_multiset(intended, parsed, self.KEY, omitted_as_null=True))
        # A missing non-NULL column is still a diff.
        intended = [insert(pairs=(("contact_id", "a"), ("status", "active")))]
        self.assertEqual(["column"], kinds(
            compare_multiset(intended, parsed, self.KEY, omitted_as_null=True)))

    def test_ignore_table_and_column(self):
        left = [Op(table="contacts.contacts", op=INSERT, cols=(("contact_id", "a"),))]
        right = [Op(table="gmail.gmail_users", op=INSERT, cols=(("email_address", "a"),))]
        self.assertEqual(["missing", "extra"], kinds(compare_multiset(left, right, self.KEY)))
        self.assertEqual([], compare_multiset(left, right, lambda op: (),
                                              ignore=("table", "column")))

    def test_json_structural_multiset(self):
        left = [insert(pairs=(("contact_id", "a"), ("prefs_json", '{"a": 1, "b": [2, 3]}')))]
        right = [insert(pairs=(("contact_id", "a"), ("prefs_json", '{"b":[2,3],"a":1}')))]
        diffs = compare_multiset(left, right, self.KEY)
        self.assertEqual(["json_format"], kinds(diffs))
        right = [insert(pairs=(("contact_id", "a"), ("prefs_json", '{"a": 2}')))]
        self.assertEqual(["value"], kinds(compare_multiset(left, right, self.KEY)))

    def test_update_where_compared_by_name(self):
        left = [update(where_pairs=(("contact_id", "a"), ("sheet_id", 1)))]
        right = [update(where_pairs=(("sheet_id", 1), ("contact_id", "a")))]
        self.assertEqual([], compare_multiset(left, right, self.KEY))

    def test_duplicate_keys(self):
        left = [insert(pairs=(("contact_id", "a"), ("first_name", "A"))),
                insert(pairs=(("contact_id", "a"), ("first_name", "B")))]
        right = [insert(pairs=(("contact_id", "a"), ("first_name", "A")))]
        self.assertEqual(["missing"], kinds(compare_multiset(left, right, self.KEY)))
        self.assertEqual(["extra"], kinds(compare_multiset(right, left, self.KEY)))
        self.assertEqual([], compare_multiset(left, left, self.KEY))


class ValueEqualityTest(unittest.TestCase):
    def test_pairs(self):
        self.assertTrue(values_equal(None, None))
        self.assertFalse(values_equal(None, False))
        self.assertFalse(values_equal(None, 0))
        self.assertTrue(values_equal(Decimal("1277953.9648391008"), Decimal("1277953.9648391008")))
        self.assertFalse(values_equal("É", "é"))
        self.assertFalse(values_equal(0, False))


if __name__ == "__main__":
    unittest.main()

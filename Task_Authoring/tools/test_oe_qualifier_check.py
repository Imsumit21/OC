"""Tests for oe_qualifier_check.py; run with: cd Task_Authoring/tools && python3.12 -B -m unittest test_oe_qualifier_check."""
from __future__ import annotations

import contextlib
import datetime as dt
import hashlib
import io
import json
import unittest
from pathlib import Path

import oe_qualifier_check as oq
import selftest_sandbox
import task_context

PEOPLE = oq.SELFTEST_PEOPLE
UTC = dt.timezone.utc

# Extra rows for the precision and day-boundary cases. ts 1759289400 is 2025-10-01 03:30 UTC, which is
# Tue Sep 30 2025 8:30 PM PT: the UTC day and the Pacific day differ. ts 1759269945 is 22:05:45 UTC (3:05:45 PM PT).
EXTRA_SQL = """
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, reply_count, created_at)
VALUES ('b1', '1759289400.000100', 'C0TEST00002', 'message', 'U_LEO', 'the late night note about the build server', NULL, 0, '2025-10-01T03:30:00Z');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, reply_count, created_at)
VALUES ('b2', '1759269945.000200', 'C0TEST00002', 'message', 'U_ANN', 'rounding check for the second message here', NULL, 0, '2025-09-30T22:05:45Z');
INSERT INTO linear.linear_issues (id, identifier, team_id, state_id, title, description, created_at, due_date)
VALUES ('ZOM-20', 'ZOM-20', 'team_ZOM', 'Todo', 'Ship the beta build', 'Ship it.', '2025-09-25T00:00:00Z', '2025-10-03');
"""
SQL = oq.SELFTEST_SQL + EXTRA_SQL


def run(oe_text, sql_text=SQL, base="off", runner=None):
    """evaluate() on a throwaway task folder holding these two files."""
    with selftest_sandbox.scratch_tmp("oe_qualifier_test_") as tmp:
        task = Path(tmp)
        (task / oq.OE_FILE).write_text(oe_text)
        if sql_text is not None:
            (task / oq.SQL_FILE).write_text(sql_text)
        return oq.evaluate(task, base=base, runner=runner, people=oq.People(data=PEOPLE))


def findings(rep, kind=None, result=None, event=None):
    return [f for f in rep["findings"] if (kind is None or f["kind"] == kind) and (result is None or f["result"] == result)
            and (event is None or f["event"] == event)]


def status(rep, check):
    return {c["id"]: c["status"] for c in rep["checks"]}[check]


def supported(rep, kind):
    return rep["by_kind"].get(kind, {}).get("supported", 0)


class FakeHg:
    """Stands in for tools/hg.py: every scan completes and finds nothing unless `hits` names a record."""

    def __init__(self, hits=None, fail=None):
        self.hits, self.fail, self.calls = hits or {}, fail, []

    def __call__(self, task_dir, args, request):
        self.calls.append(args[0] if args[0] != "search" else args[1])
        if self.fail == "raise":
            raise RuntimeError("no base data here")
        if self.fail == "error":
            return None, "tools/hg.py records exit 1: the export folder is missing"
        if args[0] == "records":
            return {"checks": {c["id"]: {"scan_complete": True, "matches": []} for c in request["checks"]}}, None
        if args[1] == "search-many":
            out = {}
            for q in request["queries"]:
                hit = self.hits.get(q["query"])
                out[q["id"]] = {"matches": [{"service_file": hit[0], "pointer": hit[1]}] if hit else []}
            return {"queries": out}, None
        items = {}
        for item in request["items"]:
            for probe, (file, pointer, record) in self.hits.items():
                if (file, pointer) == (item["file"], item["pointer"]):
                    items[item["id"]] = {"text": json.dumps(record), "truncated": False}
        return {"items": items}, None


# ------------------------------------------------------------------ parsing

class ParseTest(unittest.TestCase):
    def test_plain_and_indented_forms_of_the_archives(self):
        text = ("OE 1  Read Leo's ask in Slack (DM)\n        Expected: Leo, Tue Sep 30 2025 3:05 PM PT: \"hi\"\n\n"
                "OE 2  Open the doc in Drive\nExpected: Doc \"Bug review rules\".\n")
        parsed = oq.parse_events(text)
        self.assertEqual([e["n"] for e in parsed["events"]], [1, 2])
        self.assertEqual(parsed["problems"], [])
        first = parsed["events"][0]
        self.assertEqual(first["head"], "Read Leo's ask in Slack (DM)")
        self.assertTrue(first["expected"].startswith("Leo, Tue Sep 30"))
        self.assertEqual((first["kind"], first["services"]), ("read", ["slack"]))
        self.assertIn("gdrive", parsed["events"][1]["services"])

    def test_markdown_and_other_cues(self):
        text = ("## OE 1 - Read the doc in Docs\n**Expected data:** Doc \"Bug review rules\".\n\n"
                "**OE 2**: Read it again\nThe agent finds \"a ticket counts once QA has seen it on both builds\".\n\n"
                "Oracle Event 3) List the issues in Linear\nExpected (note: team ZOM, all states): 3 issues.\n")
        events = oq.parse_events(text)["events"]
        self.assertEqual([e["n"] for e in events], [1, 2, 3])
        self.assertEqual(events[0]["expected"], 'Doc "Bug review rules".')
        self.assertTrue(events[1]["expected"].startswith('"a ticket counts'))
        self.assertEqual(events[2]["expected"], "3 issues.")

    def test_blocks_that_are_not_events_are_reported(self):
        text = ("Preamble line\nOE 2  Read X\nExpected: a\nOE 1  Read Y\n\nOE 1  Read Z\nExpected: b Expected: c\n"
                "OE: read the board\nOE 4  Read the board\n")
        parsed = oq.parse_events(text)
        whats = " | ".join(p["what"] for p in parsed["problems"])
        self.assertEqual(parsed["preamble"], 1)
        for needle in ("no number", "OE 1 has no Expected line", "appears twice", "not in ascending order",
                       "more than one Expected cue", "OE 4 has no Expected line"):
            self.assertIn(needle, whats)

    def test_classify(self):
        cases = {"Read the DM": "read", "Look at the board": "read", "Open a new issue for X": "write",
                 "Open the thread": "read", "Comment on ENG-1": "write", "Add up the rows": "derive",
                 "Work out the total": "derive", "Ponder": "unknown"}
        for head, kind in cases.items():
            self.assertEqual(oq.classify(head), kind, head)

    def test_parse_report(self):
        rep = run("OE 7  Read the board\n")
        self.assertEqual(status(rep, "oe.parse"), "WARN")
        rep = run("no events here\n")
        self.assertEqual((rep["verdict"], status(rep, "oe.parse")), ("FAIL", "FAIL"))


# ------------------------------------------------------------------ dates

def q_of(text):
    dates = oq.find_dates(text)
    assert len(dates) == 1, (text, dates)
    return dates[0]


class DateTest(unittest.TestCase):
    def test_forms(self):
        q = q_of("Leo, Tue Sep 30 2025 3:05 PM PT (22:05 UTC): hi")
        self.assertEqual((q["y"], q["m"], q["d"], q["hh"], q["mi"], q["zone"], q["dow"]), (2025, 9, 30, 15, 5, "PT", 1))
        self.assertEqual((q["alt"]["hh"], q["alt"]["mi"], q["alt"]["zone"]), (22, 5, "UTC"))
        q = q_of("posted 2025-09-30T22:05:13Z")
        self.assertEqual((q["d"], q["hh"], q["zone"]), (30, 22, "UTC"))
        q = q_of("Sep 2025")
        self.assertEqual((q["y"], q["m"], q["d"]), (2025, 9, None))
        q = q_of("canceled on 10/16/25.")
        self.assertEqual((q["y"], q["m"], q["d"]), (2025, 10, 16))
        q = q_of("at 3:05 PM")
        self.assertEqual((q["m"], q["hh"], q["mi"]), (None, 15, 5))
        self.assertEqual(oq.find_dates("version 0.3.49 and 12 rows"), [])

    def test_self_contradiction(self):
        self.assertIn("is a Tuesday", oq.date_self_check(q_of("Wed Sep 30 2025")))
        self.assertIn("is Tue Sep 30 22:05 UTC", oq.date_self_check(q_of("Sep 30 2025 3:05 PM PT (21:05 UTC)")) or "")
        self.assertIsNotNone(oq.date_self_check(q_of("Tue Sep 30 2025 3:05 PM PT (Wed Oct 1 22:05 UTC)")))
        self.assertIsNone(oq.date_self_check(q_of("Tue Sep 30 2025 8:30 PM PT (Wed Oct 1 03:30 UTC)")))
        self.assertIn("not a calendar date", oq.date_self_check(q_of("Feb 30 2025")))

    def test_day_acceptance_is_task_context_date_acceptance(self):
        """A stated day matches a record time exactly when task_context.date_acceptance accepts that day."""
        instants = ("2025-10-01T03:30:00Z", "2025-09-30T06:59:00Z", "2025-09-30T07:00:00Z", "2026-02-13T07:30:00Z",
                    "2026-02-13T08:00:00Z", "2025-11-02T08:30:00Z", "2025-12-31T23:30:00Z")
        for value in instants:
            when = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
            accepted = set(task_context.date_acceptance(value)["accepted_dates"])
            for shift in range(-2, 3):
                day = (when + dt.timedelta(days=shift)).date()
                q = oq._date_qual("x", 0, 1, y=day.year, m=day.month, d=day.day)
                self.assertEqual(oq.date_matches(q, when.astimezone(UTC), True), day.isoformat() in accepted, (value, day))

    def test_minute_cut_or_rounded(self):
        when = dt.datetime(2025, 9, 30, 22, 5, 45, tzinfo=UTC)
        def at(hh, mi, zone="PT"):
            return oq._date_qual("x", 0, 1, y=2025, m=9, d=30, hh=hh, mi=mi, zone=zone)
        self.assertTrue(oq.date_matches(at(15, 5), when))            # what Slack shows
        self.assertTrue(oq.date_matches(at(15, 6), when))            # rounded
        self.assertFalse(oq.date_matches(at(15, 7), when))
        self.assertTrue(oq.date_matches(at(22, 6, "UTC"), when))
        self.assertFalse(oq.date_matches(at(22, 5, "PT"), when))     # the UTC clock written as PT

    def test_precision_rule(self):
        midnight = dt.datetime(2025, 9, 25, tzinfo=UTC)
        self.assertFalse(oq.minute_precise(midnight, True))
        self.assertFalse(oq.minute_precise(dt.datetime(2025, 9, 25, 16, 0, tzinfo=UTC), False))
        self.assertTrue(oq.minute_precise(dt.datetime(2025, 9, 25, 16, 0, tzinfo=UTC), True))
        q = oq._date_qual("x", 0, 1, y=2025, m=9, d=25, hh=9, mi=40, zone="PT")
        self.assertIsNone(oq.date_conflict(q, midnight, True))                # the day agrees, the minute is unknown
        self.assertIsNotNone(oq.date_conflict(dict(q, d=26), midnight, True))  # the day is wrong in both zones
        self.assertIn("not 09:40 PT", oq.date_conflict(q, dt.datetime(2025, 9, 25, 16, 0, tzinfo=UTC), True))

    def test_parse_when(self):
        self.assertEqual(oq.parse_when("ts", "1759269913.882683")[0].minute, 5)
        self.assertEqual(oq.parse_when("internal_date", "1759269913000")[0].hour, 22)
        self.assertEqual(oq.parse_when("due_date", "2025-10-03")[1], False)
        self.assertEqual(oq.parse_when("date", "Tue, 30 Sep 2025 15:05:13 -0700")[0].hour, 22)
        self.assertIsNone(oq.parse_when("title", "Crash on level 12"))
        self.assertIsNone(oq.parse_when("count", 1759269913))


# ------------------------------------------------------------------ qualifiers, end to end

class QualifierTest(unittest.TestCase):
    def test_good_file(self):
        rep = run(oq.SELFTEST_OE)
        self.assertEqual(rep["verdict"], "PASS", oq.to_text(rep))
        for kind in ("date", "name", "count", "state", "quote", "amount", "version", "ticket"):
            self.assertGreater(supported(rep, kind), 0, kind)

    def replaced(self, old, new):
        self.assertIn(old, oq.SELFTEST_OE)
        return run(oq.SELFTEST_OE.replace(old, new, 1))

    def assert_one(self, rep, kind, result):
        hits = findings(rep, kind, result)
        self.assertTrue(hits, f"no {result} {kind}\n{oq.to_text(rep)}")
        self.assertEqual(rep["verdict"] == "FAIL", result == "contradicted", oq.to_text(rep))
        self.assertEqual(status(rep, "oe.qualifiers"), "FAIL" if result == "contradicted" else "WARN")
        return hits[0]

    def test_date_bound_to_a_message_ts(self):
        hit = self.assert_one(self.replaced("3:05 PM PT (22:05 UTC)", "3:25 PM PT (22:25 UTC)"), "date", "contradicted")
        self.assertIn("ts", hit["says"])
        self.assertIn("C0TEST00001/1759269913.882683", hit["record"])

    def test_date_weekday_and_zone(self):
        self.assert_one(self.replaced("Tue Sep 30 2025 3:05", "Wed Sep 30 2025 3:05"), "date", "contradicted")
        self.assert_one(self.replaced("(22:05 UTC)", "(21:05 UTC)"), "date", "contradicted")

    def test_date_of_a_named_field(self):
        hit = self.assert_one(self.replaced("created Fri Sep 26 2025 9:00 AM PT", "created Fri Sep 26 2025 9:40 AM PT"),
                              "date", "contradicted")
        self.assertIn("created_time", hit["says"])

    def test_date_precision_day_only_record(self):
        base = 'OE 1  Read the beta issue in Linear\nExpected: ZOM-20 "Ship the beta build", created {c}, due {d}.\n'
        rep = run(base.format(c="Thu Sep 25 2025 9:40 AM PT", d="Fri Oct 3 2025"))
        self.assertEqual(rep["verdict"], "WARN", oq.to_text(rep))
        hit = findings(rep, "date", "unverifiable")[0]
        self.assertIn("holds the day only", hit["says"])
        self.assertEqual(findings(rep, "date", "contradicted"), [])
        rep = run(base.format(c="Fri Sep 26 2025 9:40 AM PT", d="Fri Oct 3 2025"))
        self.assertIn("record's day", findings(rep, "date", "contradicted")[0]["says"])
        rep = run(base.format(c="Thu Sep 25 2025", d="Sat Oct 4 2025"))
        self.assertIn("due_date", findings(rep, "date", "contradicted")[0]["says"])

    def test_date_day_boundary_end_to_end(self):
        line = 'OE 1  Read the late post in Slack\nExpected: Leo, {when}: "the late night note about the build server".\n'
        for when in ("Tue Sep 30 2025 8:30 PM PT", "Wed Oct 1 2025 03:30 UTC", "Tue Sep 30 2025", "Wed Oct 1 2025",
                     "Tue Sep 30 2025 8:30 PM PT (Wed Oct 1 03:30 UTC)"):
            rep = run(line.format(when=when))
            self.assertEqual(rep["verdict"], "PASS", f"{when}\n{oq.to_text(rep)}")
        for when in ("Wed Oct 1 2025 8:30 PM PT", "Thu Oct 2 2025", "Tue Sep 30 2025 03:30 UTC"):
            rep = run(line.format(when=when))
            self.assertTrue(findings(rep, "date", "contradicted"), f"{when}\n{oq.to_text(rep)}")

    def test_date_rounded_minute_is_supported(self):
        line = 'OE 1  Read Ann in Slack\nExpected: Ann, Tue Sep 30 2025 {t} PM PT: "rounding check for the second message here".\n'
        self.assertEqual(run(line.format(t="3:05"))["verdict"], "PASS")
        self.assertEqual(run(line.format(t="3:06"))["verdict"], "PASS")
        self.assertTrue(findings(run(line.format(t="3:08")), "date", "contradicted"))

    def test_name(self):
        self.assert_one(self.replaced("Leo, Tue Sep 30 2025 3:15", "Ann, Tue Sep 30 2025 3:15"), "name", "contradicted")
        self.assert_one(self.replaced("owner leo@example.co", "owner ann@example.co"), "name", "contradicted")
        rep = self.replaced("Leo, Tue Sep 30 2025 3:15", "Zed, Tue Sep 30 2025 3:15")      # not a known person: no claim
        self.assertEqual(findings(rep, "name"), [])

    def test_count(self):
        self.assert_one(self.replaced("It has one reply", "It has two replies"), "count", "contradicted")
        hit = self.assert_one(self.replaced("Expected: 3 issues:", "Expected: 4 issues:"), "count", "unverifiable")
        self.assertIn("lists 3", hit["says"])

    def test_state(self):
        self.assert_one(self.replaced('"Tier resets" (In Progress)', '"Tier resets" (Todo)'), "state", "contradicted")
        rep = self.replaced("Expected: 3 issues:", "Expected: All in Todo, 3 issues:")
        self.assertIn("ZOM-8 is In Progress", findings(rep, "state", "contradicted")[0]["says"])

    def test_quote(self):
        hit = self.assert_one(self.replaced("please move the three bug tickets to Done", "Please move the three bug tickets to done"),
                              "quote", "unsupported")                     # other case, in the record this event reads
        self.assertIn("character for character", hit["says"])
        self.assert_one(self.replaced("seen it on both builds", "seen it on every build"), "quote", "unverifiable")

    def test_quote_dash_variant_is_supported(self):
        """The platform passed five quotes that wrote a hyphen for the record's em dash (robert_winddown, PASS 5)."""
        rep = self.replaced("alone — it is not ours", "alone - it is not ours")
        self.assertEqual(rep["verdict"], "PASS", oq.to_text(rep))
        self.assertEqual(rep["counts"]["unresolved"], 0)                    # the variant still names the record

    def test_quote_with_escaped_line_breaks(self):
        sql = SQL + ("INSERT INTO gmail.gmail_messages (id, thread_id, subject, body_text, internal_date)\n"
                     "VALUES ('g1', 't1', 'Chase records', 'One thing while I''m in\\r\\nthere: the money went back.', '1771000004000');\n")
        rep = run('OE 1  Read the Chase mail in Gmail\nExpected: "One thing while I\'m in there: the money went back."\n', sql_text=sql)
        self.assertEqual(rep["verdict"], "PASS", oq.to_text(rep))

    def test_quote_pointing_to_another_event(self):
        """A quote marked (OE 1) may come from that event's service; with Sheets not searched it is unverifiable."""
        text = ('OE 1  Read the tracker in Sheets\nExpected: A status column.\n\n'
                'OE 2  Search Gmail for outreach\nExpected: Its note "Reached out - no response as of 09/11" (OE 1) is the outreach.\n')
        rep = run(text, base="search", runner=FakeHg())
        hit = findings(rep, "quote", event=2)[0]
        self.assertEqual(hit["result"], "unverifiable", hit)
        self.assertIn("gsheets", hit["says"])

    def test_quote_across_text_boxes_and_symbols(self):
        sql = SQL + ("INSERT INTO gslides.slides_page_elements (presentation_id, object_id, text) VALUES ('p9', 'e1', 'Tiers go from -2 to +2 per level.');\n"
                     "INSERT INTO gslides.slides_page_elements (presentation_id, object_id, text) VALUES ('p9', 'e2', 'Costs are annual \u00f7 12 for a month.');\n")
        rep = run('OE 1  Read the tiers deck in Slides\nExpected: "Tiers go from -2 to +2 per level. Costs are annual / 12 for a month."\n', sql_text=sql)
        self.assertEqual(rep["verdict"], "PASS", oq.to_text(rep))

    def test_quote_in_code_or_mail_is_never_unsupported_after_a_search_miss(self):
        for service, head in (("github", "Read TierManager.cs in GitHub"), ("gmail", "Read the decline in Gmail")):
            rep = run(f'OE 1  {head}\nExpected: "if (totalGames == 10) promote the player"\n', base="search", runner=FakeHg())
            hit = findings(rep, "quote")[0]
            self.assertEqual(hit["result"], "unverifiable", hit)
            self.assertIn(oq.PARTIAL_SEARCH[service].split(" ")[0], hit["says"])

    def test_call_name_case_and_dash(self):
        sql = SQL + "INSERT INTO linear.linear_projects (id, name) VALUES ('p1', 'Shutdown \u2013 accounts');\n"
        rep = run('OE 1  Open the project "Shutdown - accounts" in Linear\nExpected: One project.\n', sql_text=sql)
        self.assertIn("Shutdown \u2013 accounts", findings(rep, "quote", "unsupported")[0]["says"])
        rep = run('OE 1  Open the project "shutdown \u2013 Accounts" in Linear\nExpected: One project.\n', sql_text=sql)
        self.assertEqual(findings(rep, "quote", "unsupported"), [])          # other case alone: a search still finds it

    def test_quote_unsupported_when_the_base_was_searched(self):
        text = 'OE 1  Read the ask in Slack\nExpected: Leo wrote "this sentence is in no record at all anywhere".\n'
        hg = FakeHg()
        rep = run(text, base="search", runner=hg)
        self.assertIn("search-many", hg.calls)
        hit = findings(rep, "quote", "unsupported")[0]
        self.assertIn("base slack export", hit["says"])
        self.assertEqual(rep["verdict"], "WARN")

    def test_quote_found_in_a_base_record(self):
        record = {"ts": "1759000000.000100", "user": "U_ANN", "text": "a base sentence the search finds for us"}
        hg = FakeHg(hits={"a base sentence the search finds for us": ("messages/C0BASE/2025-09.json", "/3", record)})
        text = 'OE 1  Read the ask in Slack\nExpected: Ann: "a base sentence the search finds for us".\n'
        rep = run(text, base="search", runner=hg)
        self.assertEqual(rep["verdict"], "PASS", oq.to_text(rep))
        self.assertIn("get-many", hg.calls)

    def test_quote_said_to_be_in_several_records(self):
        sql = SQL + ("INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, reply_count, created_at)\n"
                     "VALUES ('q1', '1759300000.000100', 'C0TEST00003', 'message', 'U_LEO', 'build 12 is green on every device', NULL, 0, '2025-10-01T06:26:40Z');\n"
                     "INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, reply_count, created_at)\n"
                     "VALUES ('q2', '1759300100.000100', 'C0TEST00003', 'message', 'U_ANN', 'build 12 is green on every device', NULL, 0, '2025-10-01T06:28:20Z');\n")
        line = 'OE 1  Read the build posts in Slack\nExpected: {claim} "build 12 is green on every device".\n'
        rep = run(line.format(claim="Both posts say"), sql_text=sql)
        self.assertEqual(rep["verdict"], "PASS", oq.to_text(rep))
        rep = run(line.format(claim="All three posts say"), sql_text=sql, base="search", runner=FakeHg())
        hit = findings(rep, "count", "unsupported")[0]
        self.assertIn("2 place(s) in 2 record(s)", hit["says"])
        self.assertEqual(rep["verdict"], "WARN")                          # never a FAIL: the search is literal
        rep = run(line.format(claim="All three posts say"), sql_text=sql)
        self.assertTrue(findings(rep, "count", "unverifiable"))           # base not searched

    def test_literal(self):
        text = "OE 1  List the bugs in Linear (team ZOM)\nExpected: ZOM-7 and ZOM-99.\n"
        rep = run(text, base="ids", runner=FakeHg())
        self.assertIn("not a Linear issue in the base", findings(rep, "ticket", "unsupported")[0]["says"])
        self.assertEqual(rep["verdict"], "WARN")
        rep = run(text)                                                     # base not read: cannot say it is missing
        self.assertTrue(findings(rep, "ticket", "unverifiable"))
        self.assertEqual(findings(rep, "ticket", "unsupported"), [])
        rep = run("OE 1  List the bugs in Linear (team ZOM)\nExpected: ZOM-7 to ZOM-9 (there is no ZOM-99).\n",
                  base="ids", runner=FakeHg())
        self.assertEqual(findings(rep, "ticket"), [])                       # the line itself says it does not exist
        rep = run("OE 1  Read the stock lines in Gmail\nExpected: ES-2 and ES-4 were terminated.\n", base="ids", runner=FakeHg())
        self.assertEqual(findings(rep, "ticket", "unsupported"), [])        # ES is not a Linear team key

    def test_amount_and_version(self):
        self.assert_one(self.replaced("$1,250.00", "$1,350.00"), "amount", "unverifiable")
        self.assert_one(self.replaced("0.3.49.", "0.3.50."), "version", "unverifiable")
        rep = self.replaced("$1,250.00", "$1250")                    # separators and .00 do not matter
        self.assertEqual(rep["verdict"], "PASS", oq.to_text(rep))

    def test_superlative_and_absence(self):
        self.assert_one(self.replaced("Expected: 3 issues:", "Expected: The only open tickets, 3 issues:"),
                        "superlative", "unverifiable")
        self.assert_one(self.replaced("It has one reply.", "It has one reply. Nothing else since."), "absence", "unverifiable")

    def test_write_events(self):
        rep = run(oq.SELFTEST_OE.replace("Move ZOM-7 to Done (Linear update)\nExpected: ZOM-7 is Done.",
                                         "Comment on ZOM-7 in Linear\nExpected: A comment \"Moved on Wed Sep 30 2025 per Leo\"."))
        self.assertEqual(rep["verdict"], "PASS", oq.to_text(rep))       # a quote the event writes is not checked
        rep = run(oq.SELFTEST_OE.replace("Move ZOM-7 to Done (Linear update)\nExpected: ZOM-7 is Done.",
                                         "Comment on ZOM-7 in Linear\nExpected: A comment saying it moved on Wed Sep 30 2025."))
        self.assertTrue(findings(rep, "date", "contradicted"))           # its dates are still checked for the weekday


# ------------------------------------------------------------------ unreadable records and missing data

class UnreadableTest(unittest.TestCase):
    def test_base_helper_raises(self):
        rep = run('OE 1  Read the ask in Slack\nExpected: Leo wrote "this sentence is in no record at all anywhere".\n',
                  base="search", runner=FakeHg(fail="raise"))
        self.assertEqual(rep["verdict"], "WARN", oq.to_text(rep))
        self.assertTrue(any("RuntimeError" in e for e in rep["base"]["errors"]))
        self.assertTrue(findings(rep, "quote", "unverifiable"))
        self.assertEqual(status(rep, "oe.records"), "WARN")

    def test_base_helper_errors(self):
        rep = run("OE 1  Read ZOM-99 in Linear\nExpected: ZOM-99 is open.\n", base="ids", runner=FakeHg(fail="error"))
        self.assertEqual(rep["verdict"], "WARN")
        self.assertTrue(rep["base"]["errors"])
        self.assertEqual(findings(rep, "ticket", "unsupported"), [])    # a failed read never proves a value missing

    def test_defaults_without_a_task_context(self):
        """evaluate(task_dir) with defaults, in a folder with no assignment and no base data: a result, not a crash."""
        with selftest_sandbox.scratch_tmp("oe_qualifier_test_") as tmp:
            task = Path(tmp)
            (task / oq.OE_FILE).write_text("OE 1  Read the board in Trello\nExpected: Card \"Beta sign-off\" in BETA.\n")
            rep = oq.evaluate(task)
        self.assertIn(rep["verdict"], ("PASS", "WARN"))
        self.assertEqual(rep["base"]["mode"], "off")
        self.assertTrue(isinstance(rep["checks"], list) and len(rep["checks"]) == 3)

    def test_unresolved_record(self):
        rep = run(oq.SELFTEST_OE + "\nOE 6  Read the March invoice in Gmail (search \"invoice\")\nExpected: An invoice for 40 seats.\n")
        self.assertEqual((status(rep, "oe.records"), rep["counts"]["unresolved"]), ("WARN", 1))
        self.assertTrue(findings(rep, "record", "unverifiable", event=6))

    def test_missing_or_bad_files(self):
        self.assertEqual(run("", sql_text=None)["verdict"], "FAIL")
        rep = run(oq.SELFTEST_OE, sql_text="INSERT INTO broken (")
        self.assertIn(rep["verdict"], ("WARN", "PASS"))
        self.assertEqual(rep["counts"]["contradicted"], 0)
        rep = run(oq.SELFTEST_OE, sql_text="\x00\x01 not sql")
        self.assertIn(rep["verdict"], ("WARN", "PASS"))

    def test_deleted_row_supports_nothing(self):
        sql = SQL + "DELETE FROM linear.linear_issues WHERE id = 'ZOM-20';\n"
        rep = run('OE 1  Read the beta issue in Linear\nExpected: ZOM-20 "Ship the beta build".\n', sql_text=sql)
        self.assertEqual(rep["counts"]["unresolved"], 1, oq.to_text(rep))


# ------------------------------------------------------------------ determinism, output, CLI

class OutputTest(unittest.TestCase):
    def test_determinism_and_binding(self):
        with selftest_sandbox.scratch_tmp("oe_qualifier_test_") as tmp:
            task = Path(tmp)
            (task / oq.OE_FILE).write_text(oq.SELFTEST_OE)
            (task / oq.SQL_FILE).write_text(SQL)
            people = oq.People(data=PEOPLE)
            one, two = oq.evaluate(task, base="off", people=people), oq.evaluate(task, base="off", people=people)
            digest = hashlib.sha256((task / oq.OE_FILE).read_bytes()).hexdigest()
        self.assertEqual(json.dumps(one, sort_keys=True), json.dumps(two, sort_keys=True))
        self.assertEqual(one["bound_to"][oq.OE_FILE], digest)
        self.assertEqual(set(one["bound_to"]), {oq.OE_FILE, oq.SQL_FILE})
        self.assertEqual((one["tool"], one["version"]), ("oe_qualifier_check", 1))
        self.assertEqual([c["id"] for c in one["checks"]], ["oe.parse", "oe.records", "oe.qualifiers"])

    def test_text_output(self):
        rep = run(oq.SELFTEST_OE.replace("It has one reply", "It has two replies"))
        lines = oq.to_text(rep, "demo").splitlines()
        self.assertRegex(lines[0], r"^OE QUALIFIER CHECK \(demo, 5 events\): FAIL$")
        self.assertTrue(all(line.startswith(("[PASS] ", "[WARN] ", "[FAIL] ", "[SKIP] ")) for line in lines[1:]))
        self.assertTrue(any(line.startswith("[FAIL] oe.qualifiers: OE 1 count") for line in lines))

    def test_cli_exit_codes(self):
        with selftest_sandbox.scratch_tmp("oe_qualifier_test_") as tmp:
            task = Path(tmp)
            (task / oq.OE_FILE).write_text(oq.SELFTEST_OE)
            (task / oq.SQL_FILE).write_text(SQL)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = oq.main(["check", "--task-dir", str(task), "--base", "off", "--json"])
            self.assertIn(code, (0, 1))
            self.assertEqual(json.loads(out.getvalue())["tool"], "oe_qualifier_check")
            (task / oq.OE_FILE).write_text(oq.SELFTEST_OE.replace("(22:05 UTC)", "(21:05 UTC)"))
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(oq.main(["check", "--task-dir", str(task), "--base", "off"]), 1)
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(oq.main(["check", "--task-dir", str(task / "missing")]), 2)
                self.assertEqual(oq.main(["check"]), 2)
                self.assertEqual(oq.main([]), 2)


class BacktestHelperTest(unittest.TestCase):
    def test_patch_stays_inside_its_event(self):
        text = "OE 1  Read A\nExpected: x y\n\nOE 2  Read B\nExpected: x y\n"
        got, why = oq._patch(text, {"event": 2, "old": "x y", "new": "x z"})
        self.assertIsNone(why)
        self.assertEqual(got, "OE 1  Read A\nExpected: x y\n\nOE 2  Read B\nExpected: x z\n")
        self.assertEqual(oq._patch(text, {"event": 3, "old": "x", "new": "y"})[0], None)
        self.assertEqual(oq._patch(text, {"event": 1, "old": "nope", "new": "y"})[1], "the wording to replace is not in the event")

    def test_read_oe_report(self):
        with selftest_sandbox.scratch_tmp("oe_qualifier_test_") as tmp:
            path = Path(tmp) / "x_2_oe.md"
            path.write_text("Score: 3\nReviewed OE SHA-256: `" + "a" * 64 + "`\n### FINAL VERDICT: NON-FAIL\n")
            rep = oq.read_oe_report(path)
            self.assertEqual((rep["verdict"], rep["score"], rep["oe_sha"]), ("NON-FAIL", 3, "a" * 64))
            path.write_text("not a report\n")
            self.assertIsNone(oq.read_oe_report(path))


class SelfTest(unittest.TestCase):
    def test_self_test(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(oq.main(["--self-test"]), 0)
        self.assertIn("self-test: ok", out.getvalue())


if __name__ == "__main__":
    unittest.main()

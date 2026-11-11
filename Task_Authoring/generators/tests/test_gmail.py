"""The Gmail emitter: derived values, a rendered scratch task on the real synth-cut export, and every refusal."""
from __future__ import annotations

import json
import unittest

from generators.core import pipeline
from generators.core.gmail_index import address_form, parse_entries
from generators.core.values import SpecError
from generators.services import gmail, registry
from generators.tests.fixtures.gmail_fixture import (BASE_PARENT, BASE_PARENT_RFC, BASE_THREADS, BRIAN, GMAIL_DIR,
                                                     JULIA, LEONARD, ROBERT, GmailFixture, gbase)
from generators.tests.fixtures.task_fixture import lit, ref

HAVE_EXPORT = (GMAIL_DIR / "source_manifest.json").is_file()
JULIA_BOX, ROBERT_BOX, BRIAN_BOX = "julia.lawson@harmonygames.co", "robert@harmonygames.co", \
    "brian.foster@harmonygames.co"


class DerivedValuesTest(unittest.TestCase):
    def test_rfc_id_and_thread_number(self):
        epoch = gmail.epoch_of("2025-09-29T16:00:00Z", "x")
        self.assertEqual(epoch, 1759161600)
        rfc = gmail.rfc_id_for("julia.lawson@harmonygames.co", epoch)
        self.assertRegex(rfc, r"^<CA[A-Za-z0-9_-]{49}@mail\.gmail\.com>$")
        self.assertEqual(rfc, gmail.rfc_id_for("Julia.Lawson@harmonygames.co", epoch))       # case-blind, fixed
        self.assertNotEqual(rfc, gmail.rfc_id_for("julia.lawson@harmonygames.co", epoch + 1))
        n = gmail.thread_number(epoch * 1000, JULIA_BOX, rfc)
        self.assertEqual(len(str(n)), 19)
        self.assertEqual(n >> 20, epoch * 1000)
        self.assertNotEqual(n, gmail.thread_number(epoch * 1000, ROBERT_BOX, rfc))           # one number per mailbox

    def test_snippet_crlf_date_and_subject(self):
        self.assertEqual(gmail.snippet_of("Hi,\r\n\r\n  the   build\tis up. "), "Hi, the build is up.")
        self.assertEqual(len(gmail.snippet_of("word " * 100)), 139)                     # cut at 140, trailing space off
        self.assertEqual(gmail.crlf("a\nb\r\nc\rd"), "a\r\nb\r\nc\r\nd")
        self.assertEqual(gmail.date_header(1759161600, "+0000"), "Mon, 29 Sep 2025 16:00:00 +0000")
        self.assertEqual(gmail.date_header(1759161600, "-0700"), "Mon, 29 Sep 2025 09:00:00 -0700")
        self.assertEqual(gmail.reply_subject("Re: RE: Plan"), "Re: Plan")
        self.assertEqual(gmail.reply_subject("Plan"), "Re: Plan")
        self.assertEqual(gmail.reply_subject("Re: Plan"), "Re: Plan")

    def test_time_must_be_exact(self):
        for bad in ("2025-09-29 18:00:00", "2025-09-29T18:00:00+00:00", "2025-09-29T18:00:00.5Z", None, 5):
            with self.assertRaisesRegex(SpecError, "is not YYYY-MM-DDTHH:MM:SSZ"):
                gmail.epoch_of(bad, "x")

    def test_label_tokens(self):
        labels = {"INBOX": {"name": "Inbox"}, "CATEGORY_PERSONAL": {"name": "Personal"},
                  "CATEGORY_PURCHASES": {"name": "Category Purchases"}, "Label_b19fb8d1b3": {"name": "Opened"}}
        self.assertEqual([gmail.label_token(x, labels) for x in labels],
                         ["Inbox", "Category Personal", "Category Purchases", "Opened"])

    def test_address_forms(self):
        self.assertEqual(address_form("leonard hayes", "leonard.hayes@harmonygames.co"),
                         "leonard hayes <leonard.hayes@harmonygames.co>")
        self.assertEqual(address_form("Hayes, Leonard", "l@x.co"), '"Hayes, Leonard" <l@x.co>')
        self.assertEqual(address_form("", "l@x.co"), "l@x.co")
        self.assertEqual(parse_entries('"a, b" <x@y.co>, c@d.co'), [("a, b", "x@y.co"), ("", "c@d.co")])


@unittest.skipUnless(HAVE_EXPORT, "synth-cut Gmail export not installed")
class GmailRenderTest(unittest.TestCase):
    def setUp(self):
        self.fx = GmailFixture()

    def tearDown(self):
        self.fx.cleanup()

    def build(self):
        return pipeline.build(self.fx.write())

    def messages(self, res=None):
        res = res or self.build()
        out = {}
        for op in res.ops:
            if op.table == "gmail.gmail_messages":
                out[(op.record, op.col("user_email"))] = dict(op.cols)
        return out

    # ---- the happy path
    def test_validates_clean(self):
        res = self.build()
        val = pipeline.validate(res)
        self.assertEqual(val["verdict"], "PASS", val)
        self.assertEqual((val["grammar"], val["types"], val["compare"], val["overlay"]), ([], [], [], []))
        self.assertEqual((val["invariants"]["FAIL"], val["invariants"]["WARN"]), ({}, {}))
        self.assertEqual((val["sql_lint"]["errors"]["count"], val["sql_lint"]["warnings"]["count"]), (0, 0))
        self.assertEqual(val["parse_back"], "29 operations")
        rep = pipeline.provenance_report(res)
        self.assertEqual((rep["verdict"], rep["columns_without_provenance"]), ("PASS", []))

    def test_render_is_idempotent_and_check_passes(self):
        task = self.fx.write()
        rep = pipeline.render(task)
        self.assertEqual(rep["verdict"], "PASS", rep["validation"])
        self.assertEqual({c["status"] for c in pipeline.render(task)["changes"]}, {"unchanged"})
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")
        record = json.loads((task / "Working_Files" / "build" / "build_record.json").read_text())
        snap = record["snapshot"]["gmail"]
        self.assertEqual(snap["file"], "source_manifest.json")
        self.assertGreater(snap["scanned"]["threads/"]["files"], 80000)
        self.assertIn("threads/00015367.json", snap["files_read"])                       # robert's copy of the parent
        self.assertEqual(record["dependencies"]["emitters"]["gmail"], gmail.VERSION)

    def test_copies_of_a_new_thread(self):
        rows = self.messages()
        n1 = {box: rows[("N1", box)] for box in (JULIA_BOX, ROBERT_BOX, BRIAN_BOX)}
        self.assertEqual(json.loads(n1[JULIA_BOX]["label_ids_json"]), ["SENT"])
        self.assertEqual(json.loads(n1[ROBERT_BOX]["label_ids_json"]), ["INBOX", "CATEGORY_PERSONAL"])
        rfc = n1[JULIA_BOX]["id"].split("/", 1)[1]
        for box, row in n1.items():
            self.assertEqual(row["id"], f"{box}/{rfc}")
            self.assertTrue(row["thread_id"].startswith(box + "/"))
            self.assertEqual(int(row["thread_id"].split("/")[1]) >> 20, row["internal_date"])
            self.assertEqual((row["from_email"], row["from_name"], row["date"], row["internal_date"]),
                             ("julia.lawson@harmonygames.co", "julia", "2025-09-29T16:00:00Z", 1759161600000))
            self.assertEqual((json.loads(row["to_json"]), json.loads(row["cc_json"])), ([ROBERT], [BRIAN]))
            self.assertEqual((row["in_reply_to"], row["references"], row["body_html"], row["mbox_from"]),
                             ("", "", None, None))
            self.assertIn("\r\n", row["body_text"])
            self.assertTrue(row["snippet"].startswith("Robert, The Q4 audience refresh goes to Solsten"))
            self.assertEqual(tuple(row), gmail.MESSAGE_COLUMNS)
        self.assertEqual(len({r["thread_id"] for r in n1.values()}), 3)              # each mailbox its own thread
        same = ("subject", "date", "internal_date", "body_text", "snippet", "to_json", "cc_json", "from_name")
        self.assertEqual(len({tuple(r[c] for c in same) for r in n1.values()}), 1)

    def test_reply_in_a_spec_thread(self):
        res = self.build()
        rows = self.messages(res)
        for box in (JULIA_BOX, ROBERT_BOX, BRIAN_BOX):
            n1, n2 = rows[("N1", box)], rows[("N2", box)]
            rfc1 = n1["id"].split("/", 1)[1]
            self.assertEqual(n2["thread_id"], n1["thread_id"])
            self.assertEqual((n2["subject"], n2["in_reply_to"], n2["references"]), ("Re: Q4 audience refresh",
                                                                                   rfc1, rfc1))
        self.assertEqual(json.loads(rows[("N2", ROBERT_BOX)]["label_ids_json"]), ["SENT"])
        threads = {op.col("id"): dict(op.cols) for op in res.ops if op.table == "gmail.gmail_threads"
                   and op.op == "insert"}
        n1_thread = threads[rows[("N1", JULIA_BOX)]["thread_id"]]
        self.assertEqual(n1_thread["snippet"], rows[("N2", JULIA_BOX)]["snippet"])     # the newest message's
        self.assertEqual(n1_thread["history_id"], None)
        self.assertEqual(len(threads), 10)

    def test_reply_under_a_base_message(self):
        res = self.build()
        rows = self.messages(res)
        b1 = {box: rows[("B1", box)] for box in BASE_THREADS}
        for box, row in b1.items():
            self.assertEqual(row["thread_id"], BASE_THREADS[box])                       # each mailbox's own thread
            self.assertEqual(row["in_reply_to"], BASE_PARENT_RFC)
            self.assertTrue(row["references"].endswith(BASE_PARENT_RFC))
            self.assertTrue(row["subject"].startswith("Re: Fwd: Great News from "))
        self.assertEqual(json.loads(b1[ROBERT_BOX]["label_ids_json"]), ["SENT"])
        self.assertEqual(json.loads(b1["leonard.hayes@harmonygames.co"]["label_ids_json"]),
                         ["INBOX", "CATEGORY_PERSONAL"])
        updates = {dict(op.where)["id"]: dict(op.cols) for op in res.ops if op.op == "update"}
        self.assertEqual(set(updates), set(BASE_THREADS.values()))
        self.assertEqual({u["snippet"] for u in updates.values()}, {b1[ROBERT_BOX]["snippet"]})

    def test_a_base_thread_keeps_a_newer_base_snippet(self):
        """A reply into a base thread that has later base messages joins it but leaves its snippet alone."""
        parent = "arthur.blake@harmonygames.co/<CAPBs_a44WSDi+X_WABp+WGA75YbhqHhogF0=nmA4A=jsNmtJkw@mail.gmail.com>"
        self.fx.record("B1")["fields"].update(**{"from": lit(LEONARD), "to": lit([ROBERT]),
                                                 "at": lit("2025-09-20T10:00:00Z"), "parent": gbase("messages", parent)})
        res = self.build()
        rows = self.messages(res)
        self.assertEqual(rows[("B1", ROBERT_BOX)]["thread_id"], "robert@harmonygames.co/1842397703279745637")
        self.assertEqual(rows[("B1", "leonard.hayes@harmonygames.co")]["thread_id"],
                         "leonard.hayes@harmonygames.co/1832157923530152649")
        self.assertEqual([op for op in res.ops if op.op == "update"], [])        # base messages up to Sep 30 are newer
        self.assertEqual(pipeline.validate(res)["verdict"], "PASS")

    def test_outside_sender_has_one_copy(self):
        rows = self.messages()
        n3 = [k for k in rows if k[0] == "N3"]
        self.assertEqual(n3, [("N3", JULIA_BOX)])
        row = rows[("N3", JULIA_BOX)]
        self.assertEqual((row["from_email"], row["from_name"]), ("priya@pixelharbor.example", "Priya Raman"))
        headers = {h["name"]: h["value"] for h in json.loads(row["headers_json"])}
        self.assertEqual(headers["Delivered-To"], JULIA_BOX)

    def test_labels_offset_and_headers(self):
        rows = self.messages()
        brian = rows[("L1", BRIAN_BOX)]
        self.assertEqual(json.loads(brian["label_ids_json"]), ["INBOX", "IMPORTANT", "CATEGORY_PERSONAL", "UNREAD"])
        headers = json.loads(brian["headers_json"])
        self.assertEqual([h["name"] for h in headers],
                         ["X-GM-THRID", "X-Gmail-Labels", "Delivered-To", "MIME-Version", "Date", "Message-ID",
                          "Subject", "From", "To", "Content-Type"])
        h = {x["name"]: x["value"] for x in headers}
        self.assertEqual((h["X-Gmail-Labels"], h["Date"], h["From"], h["X-GM-THRID"]),
                         ("Inbox,Important,Category Personal,Unread", "Tue, 30 Sep 2025 10:45:00 +0300", JULIA,
                          brian["thread_id"].split("/")[1]))
        sent = {x["name"] for x in json.loads(rows[("L1", JULIA_BOX)]["headers_json"])}
        self.assertNotIn("Delivered-To", sent)
        reply = [x["name"] for x in json.loads(rows[("N2", JULIA_BOX)]["headers_json"])]
        self.assertEqual(reply[4:8], ["Date", "References", "In-Reply-To", "Message-ID"])
        self.assertIn("Cc", reply)

    def test_haystack_rows_are_ordinary_records(self):
        res = self.build()
        keys = [r["key"] for r in res.spec.records if r["key"].startswith("HS1")]
        self.assertEqual(keys, ["HS1.001", "HS1.002"])
        rows = self.messages(res)
        self.assertEqual(rows[("HS1.002", JULIA_BOX)]["body_text"], "Build 412 is up on TestFlight.\r\nNothing blocking.")
        self.assertEqual(rows[("HS1.001", ROBERT_BOX)]["subject"], "Weekly numbers")

    def test_statement_order(self):
        res = self.build()
        kinds = [(op.table, op.op) for op in res.ops]
        self.assertEqual(kinds[:10], [("gmail.gmail_threads", "insert")] * 10)
        self.assertEqual(kinds[10:26], [("gmail.gmail_messages", "insert")] * 16)
        self.assertEqual(kinds[26:], [("gmail.gmail_threads", "update")] * 3)
        stamps = [op.col("internal_date") for op in res.ops[10:26]]
        self.assertEqual(stamps, sorted(stamps))

    def test_provenance_names_the_origin_of_every_column(self):
        res = self.build()
        op = next(op for op in res.ops if op.record == "B1" and op.op == "insert")
        prov = dict(op.prov)
        self.assertEqual(prov["in_reply_to"]["base"]["record"], BASE_PARENT)
        self.assertEqual(prov["thread_id"]["convention"], "gmail.reply")
        self.assertEqual(prov["subject"]["convention"], "gmail.reply")
        self.assertEqual((prov["body_text"]["origin"], prov["body_text"]["transform"]["convention"]),
                         ("authored", "gmail.body.crlf"))
        n1 = dict(next(op for op in res.ops if op.record == "N1" and op.table == "gmail.gmail_messages").prov)
        self.assertEqual((n1["id"]["convention"], n1["thread_id"]["convention"]), ("gmail.message.id",
                                                                                  "gmail.thread.id"))
        n2 = dict(next(op for op in res.ops if op.record == "N2" and op.table == "gmail.gmail_messages").prov)
        self.assertEqual((n2["in_reply_to"]["ref"], n2["in_reply_to"]["target"]["fn"]), ("N1", "gmail.rfc_id/1"))

    def test_base_and_spec_locators(self):
        self.fx.record("B1")["fields"]["at"] = lit("2025-09-18T16:00:00Z", after=[
            f"base:gmail:messages/{BASE_PARENT}/date_parsed"])
        self.fx.record("N2")["fields"]["at"] = lit("2025-09-29T17:30:00Z", after=["spec:N1/at"])
        self.assertEqual(len(self.build().resolver.after_checks), 2)
        self.fx.record("B1")["fields"]["at"] = lit("2025-09-18T14:00:00Z", after=[
            f"base:gmail:messages/{BASE_PARENT}/date_parsed"])
        with self.assertRaisesRegex(SpecError, "is not after"):
            self.build()

    def test_from_as_a_base_address_form(self):
        self.fx.record("N1")["fields"]["from"] = gbase("addresses", "julia.lawson@harmonygames.co", "form")
        res = self.build()
        op = next(op for op in res.ops if op.record == "N1" and op.table == "gmail.gmail_messages")
        self.assertEqual((op.col("from_name"), op.col("from_email")), ("julia", "julia.lawson@harmonygames.co"))
        self.assertEqual(dict(op.prov)["from_email"]["base"]["collection"], "addresses")

    def test_published_part_parses_back_and_tampering_is_caught(self):
        task = self.fx.write()
        pipeline.render(task)
        text = (task / "Working_Files" / "build" / "parts" / "gmail.sql").read_text()
        res = pipeline.build(task)
        self.assertEqual(pipeline.validate(res, pipeline.emitter.render_full([], [text]))["verdict"], "PASS")
        lines = text.split("\n")
        robert_copy = next(i for i, line in enumerate(lines) if "INSERT INTO gmail.gmail_messages" in line
                           and f"'{ROBERT_BOX}/<" in line and "Q4 audience refresh'" in line)
        dropped = "\n".join(line for i, line in enumerate(lines) if i != robert_copy)
        val = pipeline.validate(res, pipeline.emitter.render_full([], [dropped]))
        self.assertEqual(val["verdict"], "FAIL")
        self.assertIn("G4", val["invariants"]["FAIL"])                                # Robert's copy is missing
        relabeled = text.replace('\'["INBOX", "IMPORTANT", "CATEGORY_PERSONAL", "UNREAD"]\'', '\'["SENT"]\'')
        self.assertIn("G5", pipeline.validate(res, pipeline.emitter.render_full([], [relabeled]))["invariants"]["FAIL"])

    # ---- refusals, each with its named error
    def fails(self, pattern, exc=SpecError):
        task = self.fx.write()
        with self.assertRaisesRegex(exc, pattern):
            pipeline.build(task)

    def test_address_refusals(self):
        f = self.fx.record("N1")["fields"]
        f["from"] = lit("Julia Lawson <julia.lawson@harmonygames.co>")
        self.fails("base never names julia.lawson@harmonygames.co 'Julia Lawson'")
        f["from"] = lit("julia <julia.lawsen@harmonygames.co>")
        self.fails("julia.lawsen@harmonygames.co is a harmonygames.co address no base message shows")
        f["from"] = lit("julia <Julia.Lawson@harmonygames.co>")
        self.fails("base writes this address 'julia.lawson@harmonygames.co'")
        f["from"] = lit("a@x.co, b@x.co")
        self.fails("is not one address entry")
        f["from"] = lit(JULIA)
        f["to"] = lit([ROBERT, ROBERT])
        self.fails("listed twice")
        f["to"] = lit([])
        self.fails("at least one To entry")
        f["to"], f["cc"] = lit([ROBERT]), lit([ROBERT])
        self.fails("also in To")

    def test_no_mailbox_no_message(self):
        self.fx.record("N3")["fields"]["to"] = lit(["Sam Lee <sam@pixelharbor.example>"])
        self.fails("no participant has a mailbox in base")

    def test_label_refusals(self):
        f = self.fx.record("L1")["fields"]
        f["labels"] = lit({BRIAN_BOX: ["INBOX", "NOPE"]})
        self.fails("labels \\['NOPE'\\] are not in the pinned labels.json")
        f["labels"] = lit({BRIAN_BOX: ["SENT", "INBOX"]})
        self.fails("a recipient's copy is not labelled SENT")
        f["labels"] = lit({BRIAN_BOX: ["CATEGORY_PERSONAL"]})
        self.fails("a received copy is in INBOX or ARCHIVED")
        f["labels"] = lit({JULIA_BOX: ["INBOX"]})
        self.fails("the sender's copy is labelled SENT")
        f["labels"] = lit({ROBERT_BOX: ["INBOX"]})
        self.fails("get no copy of this message")

    def test_time_refusals(self):
        self.fx.record("N3")["fields"]["at"] = lit("2025-09-26 13:05:00")
        self.fails("is not YYYY-MM-DDTHH:MM:SSZ")
        self.fx.record("N3")["fields"]["at"] = lit("2025-10-01T00:00:00Z")
        self.fails("seed bound", pipeline.BuildError)

    def test_parent_refusals(self):
        f = self.fx.record("N2")["fields"]
        f["at"] = lit("2025-09-29T15:00:00Z")
        self.fails("is not earlier than the reply")
        f["at"] = lit("2025-09-29T17:30:00Z")
        f["parent"] = ref("NOPE")
        self.fails("names no spec field")
        f["parent"] = lit("<x@y>")
        self.fails("a parent is ref")
        b = self.fx.record("B1")["fields"]
        f["parent"] = ref("N1")
        b["parent"] = gbase("messages", "robert@harmonygames.co/<nope@mail.gmail.com>")
        self.fails("not found in the pinned export")
        b["parent"] = gbase("messages", BASE_PARENT, "subject")
        self.fails("a parent is ref")
        b["parent"] = gbase("messages", BASE_PARENT)
        b["at"] = lit("2025-09-18T14:00:00Z")
        self.fails("is not earlier than the reply")

    def test_subject_and_ids(self):
        del self.fx.record("N3")["fields"]["subject"]
        self.fails("a new thread needs a subject")
        self.fx.record("N3")["fields"]["subject"] = lit("Playable cut v3")
        self.fx.doc["records"].append({"key": "X1", "kind": "gmail.message", "fields": {
            "from": lit(JULIA), "to": lit([BRIAN]), "at": lit("2025-09-29T16:00:00Z"), "subject": lit("dup"),
            "body": lit("same sender, same second")}})
        self.fails("N1 and X1 get the same Message-ID")
        self.fx.record("X1")["fields"]["message_id"] = lit("not-an-id")
        self.fails("is not an RFC Message-ID")
        self.fx.record("X1")["fields"]["message_id"] = lit(BASE_PARENT_RFC)
        self.fails("is already in base")
        self.fx.record("X1")["fields"]["message_id"] = lit("<x1@pixelharbor.example>")
        self.fx.record("X1")["fields"]["date_offset"] = lit("0700")
        self.fails("is not \\+HHMM")
        del self.fx.record("X1")["fields"]["date_offset"]
        self.assertEqual(len([op for op in self.build().ops if op.record == "X1"]), 4)  # 2 threads + 2 copies

    def test_haystack_refusals(self):
        hs = self.fx.record("HS1")
        hs["rows"][0]["user"] = "x"
        self.fails("unknown row keys \\['user'\\]")
        del hs["rows"][0]["user"]
        hs["fields"]["subject"] = lit("x")
        self.fails("shares only")

    def test_snapshot_pin(self):
        self.fx.doc["snapshot"]["gmail"]["sha256"] = "0" * 64
        self.fails("the spec pins")

    def test_explain_key(self):
        res = self.build()
        op = next(op for op in res.ops if op.table == "gmail.gmail_messages")
        self.assertEqual(registry.EMITTERS["gmail"].key_of(op), (op.col("id"),))
        upd = next(op for op in res.ops if op.op == "update")
        self.assertEqual(registry.EMITTERS["gmail"].key_of(upd), (dict(upd.where)["id"],))

    def test_index_is_reused_in_process(self):
        res = self.build()
        again = pipeline.build(self.fx.write())
        self.assertTrue(again.base.index("gmail").reused)
        self.assertEqual(res.base.fingerprint["gmail"], again.base.fingerprint["gmail"])


if __name__ == "__main__":
    unittest.main()

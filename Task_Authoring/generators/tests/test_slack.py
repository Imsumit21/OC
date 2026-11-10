"""The Slack emitter: derived values, a rendered scratch task on the real synth-cut export, and every refusal."""
from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from generators.core import pipeline
from generators.core.base import BaseSnapshot, slack_shard
from generators.core.resolve import parse_instant
from generators.core.values import SpecError
from generators.services import registry, slack
from generators.tests.fixtures.slack_fixture import (BASE_POST, BASE_THREAD, DM, GROUP_DM, JULIA, LEAPBLOCK, SLACK_DIR,
                                                     SOLSTEN, ZM_ANIM, ZOMBIE_SFX, SlackFixture, channel, sbase, user)
from generators.tests.fixtures.task_fixture import lit, ref
from generators.tests.test_slack_invariants import PRIV, POST, SCRATCH, write_export

CANVAS = "C425A886E258"                      # an FC: canvas-comment channel Julia is in
HAVE_EXPORT = (SLACK_DIR / "source_manifest.json").is_file()


def sha_id(cid: str, ts: str) -> str:
    return hashlib.sha256(f"{cid}|{ts}".encode()).hexdigest()[:32]


class DerivedValuesTest(unittest.TestCase):
    def test_ts_id_and_created_at(self):
        epoch = slack.epoch_of("2025-09-29T18:00:00Z", "x")
        self.assertEqual(epoch, 1759168800)
        ts = slack.ts_for("C09ATAJ220H", epoch, "EMPLOYEE_0016_SLACK_ID")
        self.assertRegex(ts, r"^1759168800\.[0-9]{5}9$")
        self.assertEqual(ts, slack.ts_for("C09ATAJ220H", epoch, "EMPLOYEE_0016_SLACK_ID"))       # deterministic
        self.assertNotEqual(ts, slack.ts_for("C09ATAJ220H", epoch, "EMPLOYEE_0005_SLACK_ID"))
        self.assertEqual(slack.message_id("C09ATAJ220H", ts), sha_id("C09ATAJ220H", ts))
        self.assertEqual(slack.created_at_for(ts), "2025-09-29T18:00:00." + ts.split(".")[1] + "Z")
        # the id rule on a real base row (zm-animations, 2025-09-29)
        self.assertEqual(slack.message_id("C09ATAJ220H", "1759183318.447139"), "cf19f48b2e00f3c926b92424e2cab630")

    def test_time_must_be_exact(self):
        for bad in ("2025-09-29 18:00:00", "2025-09-29T18:00:00+00:00", "2025-09-29T18:00:00.5Z", "2025-02-30T00:00:00Z",
                    None, 5):
            with self.assertRaisesRegex(SpecError, "is not YYYY-MM-DDTHH:MM:SSZ"):
                slack.epoch_of(bad, "x")

    def test_member_at(self):
        events = [((10, 0), "join"), ((20, 0), "leave"), ((30, 0), "join")]
        self.assertFalse(slack.member_at(events, True, (5, 0)))          # before the first join
        self.assertTrue(slack.member_at(events, False, (15, 0)))
        self.assertFalse(slack.member_at(events, True, (25, 0)))         # left; the member list does not decide
        self.assertTrue(slack.member_at(events, False, (35, 0)))
        self.assertTrue(slack.member_at([((20, 0), "leave")], False, (5, 0)))   # in it until they leave
        self.assertTrue(slack.member_at([], True, (5, 0)))
        self.assertFalse(slack.member_at([], False, (5, 0)))

    def test_channel_kind(self):
        self.assertEqual(slack.channel_kind({"is_im": True}), "im")
        self.assertEqual(slack.channel_kind({"is_mpim": True, "is_private": True}), "mpim")
        self.assertEqual(slack.channel_kind({"name": "FC:F1:Notes"}), "canvas")
        self.assertEqual(slack.channel_kind({"name": "x", "is_private": True}), "private")
        self.assertEqual(slack.channel_kind({"name": "x"}), "public")

    def test_shard_is_the_utc_month_of_ts(self):
        self.assertEqual(slack_shard("C09ATAJ220H", "1759183318.447139"), "messages/C09ATAJ220H/2025-09.json")
        self.assertEqual(slack_shard("C09ATAJ220H", "1759276800.000009"), "messages/C09ATAJ220H/2025-10.json")
        with self.assertRaises(ValueError):
            slack_shard("C09ATAJ220H", "1759183318.44")

    def test_a_slack_ts_is_an_instant(self):
        self.assertEqual(parse_instant("1759168800.676569", "x"), parse_instant("2025-09-29T18:00:00.676569Z", "x"))
        self.assertLess(parse_instant("1759168800.676569", "x"), parse_instant("2025-09-29T18:00:01Z", "x"))
        with self.assertRaisesRegex(SpecError, "not an ISO-8601"):
            parse_instant("1759168800", "x")


class ManifestPinnedBaseTest(unittest.TestCase):
    """core/base.py on a made-up export: the manifest is the pin and every file read must equal its entry."""

    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="slack_base_", dir=str(SCRATCH)))
        self.pin = {"file": "source_manifest.json", "sha256": write_export(self.root)}

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def snapshot(self, pin=None):
        return BaseSnapshot({"slack": self.root}, {"slack": pin or self.pin})

    def test_reads_collections_and_one_shard(self):
        base = self.snapshot()
        self.assertEqual(sorted(base.records("slack", "users")), ["B0T", "U0A", "U0B", "U0C", "U0D"])
        self.assertEqual(base.get("slack", "channels", PRIV)["name"], "priv")
        row = base.get("slack", "messages", f"{PRIV}:{POST}")
        self.assertEqual(row["id"], sha_id(PRIV, POST))
        self.assertEqual(base.lookup("x", ("slack", "messages", f"{PRIV}:{POST}", "/user")), "U0A")
        self.assertIsNone(base.get("slack", "messages", f"{PRIV}:1709600000.000018"))
        self.assertIsNone(base.get("slack", "messages", f"{PRIV}:1609600000.000019"))      # no shard for that month
        self.assertEqual(base.fingerprint["slack"]["sha256"], self.pin["sha256"])
        self.assertEqual(sorted(base.fingerprint["slack"]["files_read"]),
                         ["channels.json", f"messages/{PRIV}/2024-03.json", "users.json"])
        self.assertEqual(len(base.read), 4)                                                # the manifest too
        with self.assertRaisesRegex(SpecError, "is <channel id>:<ts>"):
            base.get("slack", "messages", "nonsense")
        with self.assertRaisesRegex(SpecError, "has no field /id"):                        # a raw row has no id
            base.lookup("x", ("slack", "messages", f"{PRIV}:1709700200.000049", "/id"))

    def test_refuses_a_changed_manifest_or_file(self):
        with self.assertRaisesRegex(SpecError, "the spec pins"):
            self.snapshot({"file": "source_manifest.json", "sha256": "0" * 64}).doc("slack")
        users = self.root / "users.json"
        users.write_bytes(users.read_bytes() + b" ")
        base = self.snapshot()
        with self.assertRaisesRegex(SpecError, "differs from source_manifest.json"):
            base.records("slack", "users")
        with self.assertRaisesRegex(SpecError, "not a file of the pinned export"):
            base.file("slack", "../users.json")

    def test_a_many_file_service_needs_the_manifest_pin(self):
        data = (self.root / "channels.json").read_bytes()
        base = self.snapshot({"file": "channels.json", "sha256": hashlib.sha256(data).hexdigest()})
        with self.assertRaisesRegex(SpecError, "pin source_manifest.json"):
            base.records("slack", "channels")


@unittest.skipUnless(HAVE_EXPORT, "synth-cut Slack export not installed")
class SlackRenderTest(unittest.TestCase):
    def setUp(self):
        self.fx = SlackFixture()

    def tearDown(self):
        self.fx.cleanup()

    def build(self):
        return pipeline.build(self.fx.write())

    def rows(self, res=None):
        res = res or self.build()
        return {op.record: dict(op.cols) for op in res.ops if op.op == "insert"}

    # ---- the happy path
    def test_validates_clean(self):
        res = self.build()
        val = pipeline.validate(res)
        self.assertEqual(val["verdict"], "PASS", val)
        self.assertEqual((val["grammar"], val["types"], val["compare"], val["overlay"]), ([], [], [], []))
        self.assertEqual(val["invariants"]["FAIL"], {})
        self.assertEqual(sorted(val["invariants"]["WARN"]), ["S7"])                  # the first-time join
        self.assertEqual(val["sql_lint"]["errors"]["count"], 0, val["sql_lint"])
        self.assertEqual(val["parse_back"], "18 operations")
        rep = pipeline.provenance_report(res)
        self.assertEqual((rep["verdict"], rep["columns_without_provenance"]), ("PASS", []))

    def test_render_is_idempotent_and_check_passes(self):
        task = self.fx.write()
        rep = pipeline.render(task)
        self.assertEqual(rep["verdict"], "PASS", rep["validation"])
        self.assertEqual({c["status"] for c in rep["changes"]}, {"new"})
        self.assertEqual({c["status"] for c in pipeline.render(task)["changes"]}, {"unchanged"})
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")
        record = json.loads((task / "Working_Files" / "build" / "build_record.json").read_text())
        self.assertEqual(record["snapshot"]["slack"]["file"], "source_manifest.json")
        self.assertIn(f"messages/{ZM_ANIM}/2025-09.json", record["snapshot"]["slack"]["files_read"])
        self.assertEqual(record["dependencies"]["emitters"]["slack"], slack.VERSION)

    def test_derived_columns(self):
        rows = self.rows()
        self.assertEqual(len(rows), 15)
        for key, row in rows.items():
            self.assertRegex(row["ts"], r"^[0-9]{10}\.[0-9]{5}9$", key)
            self.assertEqual(row["id"], sha_id(row["channel_id"], row["ts"]), key)
            self.assertEqual(row["created_at"], slack.created_at_for(row["ts"]), key)
            self.assertEqual((row["type"], row["is_activity_message"], row["reactions_json"], row["files_json"],
                              row["metadata_json"]), ("message", False, "[]", "[]", "{}"), key)
            self.assertEqual(tuple(row), slack.MESSAGE_COLUMNS, key)
        m1 = rows["M1"]
        self.assertEqual(m1["ts"].split(".")[0], "1759168800")                       # 2025-09-29T18:00:00Z
        self.assertEqual(m1["created_at"][:19], "2025-09-29T18:00:00")
        self.assertEqual((m1["user_id"], m1["channel_id"], m1["text"]),
                         ("EMPLOYEE_0016_SLACK_ID", ZM_ANIM, "Boss intro: which take are we shipping?"))

    def test_threads(self):
        res = self.build()
        rows = self.rows(res)
        m1, m2, m3 = rows["M1"], rows["M2"], rows["M3"]
        self.assertEqual((m1["thread_parent_id"], m1["thread_ts_legacy"], m1["reply_count"], m1["reply_users_count"],
                          m1["latest_reply"]), (None, m1["ts"], 2, 2, m3["ts"]))
        for reply in (m2, m3):
            self.assertEqual((reply["thread_parent_id"], reply["thread_ts_legacy"], reply["reply_count"],
                              reply["reply_users_count"], reply["latest_reply"]), (m1["id"], m1["ts"], 0, 0, None))
        self.assertEqual((rows["DM1"]["reply_count"], rows["DM1"]["latest_reply"]), (1, rows["DM2"]["ts"]))
        g1 = rows["G1"]                                                              # a post without replies
        self.assertEqual((g1["thread_parent_id"], g1["thread_ts_legacy"], g1["reply_count"], g1["latest_reply"]),
                         (None, None, 0, None))
        rb0, rb1 = rows["RB0"], rows["RB1"]
        self.assertEqual((rb0["thread_parent_id"], rb0["thread_ts_legacy"]), (sha_id(ZM_ANIM, BASE_POST), BASE_POST))
        updates = {dict(op.where)["id"]: dict(op.cols) for op in res.ops
                   if op.op == "update" and op.table == "slack.slack_messages"}
        self.assertEqual(updates[sha_id(ZM_ANIM, BASE_POST)],
                         {"thread_ts_legacy": BASE_POST, "reply_count": 1, "reply_users_count": 1,
                          "latest_reply": rb0["ts"]})
        # the base thread had 9 replies by 2 users; EMPLOYEE_0006 is a third, and this reply is the newest
        self.assertEqual(updates[sha_id(ZM_ANIM, BASE_THREAD)],
                         {"thread_ts_legacy": BASE_THREAD, "reply_count": 10, "reply_users_count": 3,
                          "latest_reply": rb1["ts"]})

    def test_base_thread_keeps_its_newest_reply(self):
        self.fx.record("RB1")["fields"]["at"] = lit("2025-09-30T19:00:00Z")          # before base reply 22:25:21
        res = self.build()
        update = next(dict(op.cols) for op in res.ops if dict(op.where).get("id") == sha_id(ZM_ANIM, BASE_THREAD))
        self.assertEqual((update["reply_count"], update["latest_reply"]), (10, "1759271121.716799"))
        self.assertEqual(pipeline.validate(res)["verdict"], "PASS")

    def test_membership_rows(self):
        res = self.build()
        rows = self.rows(res)
        j1, f1, l1 = rows["J1"], rows["F1"], rows["L1"]
        self.assertEqual((j1["subtype"], j1["text"], j1["channel_id"]),
                         ("channel_join", f"<@{JULIA}> has joined the channel", SOLSTEN))
        self.assertEqual((f1["subtype"], f1["text"]), ("channel_join", f"<@{JULIA}> has joined the channel"))
        self.assertEqual((l1["subtype"], l1["text"]), ("channel_leave", f"<@{JULIA}> has left the channel"))
        for row in (j1, f1, l1):
            self.assertEqual((row["thread_parent_id"], row["thread_ts_legacy"], row["reply_count"],
                              row["attachments_json"]), (None, None, 0, "[]"))
        update = res.ops[0]
        self.assertEqual((update.table, update.op, dict(update.where)), ("slack.slack_channels", "update",
                                                                         {"id": LEAPBLOCK}))
        members = json.loads(update.col("members_json"))
        self.assertEqual((update.col("num_members"), len(members), members[-1]), (9, 9, JULIA))
        self.assertIsNone(update.record)

    def test_group_dm_join_says_conversation(self):
        group = "C165CC59D478"                       # mpdm-robert--julia.lawson--vincent.parker-1; 0008 is not in it
        self.fx.record("F1")["fields"].update(channel=channel(group), user=user("0008"))
        row = self.rows()["F1"]
        self.assertEqual(row["text"], "<@EMPLOYEE_0008_SLACK_ID> has joined the conversation")

    def test_statement_order(self):
        res = self.build()
        kinds = [(op.table, op.op) for op in res.ops]
        self.assertEqual(kinds[0], ("slack.slack_channels", "update"))
        self.assertEqual(kinds[1:16], [("slack.slack_messages", "insert")] * 15)
        self.assertEqual(kinds[16:], [("slack.slack_messages", "update")] * 2)
        inserts = [dict(op.cols) for op in res.ops[1:16]]
        order = [(r["channel_id"], slack.ts_key(r["ts"])) for r in inserts]
        self.assertEqual(order, sorted(order))
        seen = set()
        for r in inserts:                                                            # a parent before its replies
            if r["thread_parent_id"] and r["thread_parent_id"] in {x["id"] for x in inserts}:
                self.assertIn(r["thread_parent_id"], seen)
            seen.add(r["id"])

    def test_provenance_names_the_origin_of_every_column(self):
        res = self.build()
        op = next(op for op in res.ops if op.record == "RB0")
        prov = dict(op.prov)
        self.assertEqual(prov["channel_id"]["base"]["record"], ZM_ANIM)
        self.assertEqual(prov["user_id"]["origin"], "base")
        self.assertEqual((prov["text"]["origin"], prov["text"]["text"]), ("authored", "texts/RB0.txt"))
        self.assertEqual(prov["thread_parent_id"]["base"]["record"], f"{ZM_ANIM}:{BASE_POST}")
        self.assertEqual((prov["id"]["fn"], prov["id"]["convention"]), ("slack.message_id/1", "slack.message.id"))
        self.assertEqual(prov["ts"]["convention"], "slack.message.ts")
        self.assertEqual(prov["created_at"]["convention"], "slack.message.created_at")
        self.assertEqual(prov["thread_ts_legacy"]["convention"], "slack.thread_parent_id")
        m2 = dict(next(op for op in res.ops if op.record == "M2").prov)
        self.assertEqual((m2["thread_parent_id"]["ref"], m2["thread_parent_id"]["target"]["fn"]),
                         ("M1", "slack.message_id/1"))
        update = dict(res.ops[-1].prov)
        self.assertEqual(update["reply_count"]["convention"], "slack.thread.counters")

    def test_haystack_rows_are_ordinary_records(self):
        res = self.build()
        keys = [r["key"] for r in res.spec.records if r["key"].startswith("HS1")]
        self.assertEqual(keys, ["HS1.001", "HS1.002", "HS1.003"])
        rec = next(r for r in res.spec.records if r["key"] == "HS1.002")
        self.assertEqual((rec["kind"], rec["role"]), ("slack.message", "haystack"))
        self.assertEqual(rec["fields"]["user"].base, ("slack", "users", "EMPLOYEE_0006_SLACK_ID", "/id"))
        self.assertEqual((rec["fields"]["at"].origin, rec["fields"]["at"].value), ("authored", "2025-09-26T16:10:00Z"))
        self.assertEqual(rec["fields"]["text"].text, "texts/HS1_2.txt")
        row = self.rows(res)["HS1.002"]
        self.assertEqual((row["user_id"], row["text"], row["channel_id"]),
                         ("EMPLOYEE_0006_SLACK_ID", "looks good on my side", ZM_ANIM))
        prov = dict(next(op for op in res.ops if op.record == "HS1.002").prov)
        self.assertEqual((prov["user_id"]["origin"], prov["text"]["sha256"]),
                         ("base", hashlib.sha256(b"looks good on my side").hexdigest()))

    def test_haystack_under_a_parent(self):
        hs = self.fx.record("HS1")
        hs["fields"]["parent"] = ref("M1")
        for row, at in zip(hs["rows"], ("2025-09-29T18:10:00Z", "2025-09-29T18:11:00Z", "2025-09-29T18:12:00Z")):
            row["at"] = at
        rows = self.rows()
        self.assertEqual(rows["M1"]["reply_count"], 5)
        self.assertEqual(rows["HS1.003"]["thread_parent_id"], rows["M1"]["id"])
        self.assertEqual(rows["M1"]["latest_reply"], rows["HS1.003"]["ts"])

    def test_locators_name_base_and_spec_messages(self):
        self.fx.record("RB0")["fields"]["at"] = lit(
            "2025-09-30T17:05:00Z", after=[f"base:slack:messages/{ZM_ANIM}:{BASE_POST}/ts", "spec:M1/ts"])
        res = self.build()
        self.assertEqual(len(res.resolver.after_checks), 2)
        self.fx.record("RB0")["fields"]["at"] = lit("2025-09-29T17:05:00Z", after=["spec:M1/ts"])
        with self.assertRaisesRegex(SpecError, "is not after"):
            self.build()

    def test_bot_card_with_attachments_and_empty_text(self):
        self.fx.record("M3")["fields"].update(text=lit(""), attachments=lit([{"fallback": "PR opened", "id": 1}]))
        res = self.build()
        row = self.rows(res)["M3"]
        self.assertEqual((row["text"], row["attachments_json"]), ("", '[{"fallback": "PR opened", "id": 1}]'))
        self.assertEqual(pipeline.validate(res)["verdict"], "PASS")

    def test_post_after_a_first_join_is_allowed(self):
        self.fx.doc["records"].append({"key": "P1", "kind": "slack.message", "fields": {
            "channel": channel(LEAPBLOCK), "user": user("0005"), "at": lit("2025-09-26T15:30:00Z"),
            "text": lit("thanks for adding me")}})
        res = self.build()
        self.assertEqual(pipeline.validate(res)["invariants"]["FAIL"], {})

    def test_published_part_parses_back_and_tampering_is_caught(self):
        task = self.fx.write()
        pipeline.render(task)
        text = (task / "Working_Files" / "build" / "parts" / "slack.sql").read_text()
        res = pipeline.build(task)
        self.assertEqual(pipeline.validate(res, pipeline.emitter.render_full([], [text]))["verdict"], "PASS")
        val = pipeline.validate(res, pipeline.emitter.render_full([], [text.replace("reply_count = 10", "reply_count = 11")]))
        self.assertEqual(val["verdict"], "FAIL")
        self.assertTrue(val["compare"])
        self.assertIn("S5", val["invariants"]["FAIL"])
        dropped = "\n".join(line for line in text.split("\n") if not line.startswith("UPDATE slack.slack_channels"))
        val = pipeline.validate(res, pipeline.emitter.render_full([], [dropped]))
        self.assertIn("S7", val["invariants"]["FAIL"])                              # first join without the members

    # ---- refusals, each with its named error
    def fails(self, pattern, exc=SpecError):
        task = self.fx.write()
        with self.assertRaisesRegex(exc, pattern):
            pipeline.build(task)

    def add(self, key, cid, who, at, **extra):
        fields = {"channel": channel(cid), "user": user(who), "at": lit(at), "text": lit("text")}
        fields.update(extra)
        self.fx.doc["records"].append({"key": key, "kind": "slack.message", "fields": fields})

    def test_unknown_channel_or_user(self):
        self.fx.record("M1")["fields"]["channel"] = lit("C0NOSUCH001")
        self.fails("channel 'C0NOSUCH001' is not in the pinned base")
        self.fx.record("M1")["fields"]["channel"] = sbase("channels", "C0NOSUCH001")
        self.fails("not found in the pinned export")
        self.fx.record("M1")["fields"]["channel"] = channel(ZM_ANIM)
        self.fx.record("M1")["fields"]["user"] = lit("U0NOBODY")
        self.fails("user 'U0NOBODY' is not in the pinned base")

    def test_bad_time(self):
        self.fx.record("G1")["fields"]["at"] = lit("2025-09-30 15:30:00")
        self.fails("is not YYYY-MM-DDTHH:MM:SSZ")

    def test_post_at_or_after_the_freeze(self):
        self.fx.record("G1")["fields"]["at"] = lit("2025-10-01T00:00:00Z")
        self.fails("seed bound", pipeline.BuildError)

    def test_author_must_be_a_member(self):
        self.fx.record("M1")["fields"]["user"] = user("0008")                       # not in zm-animations
        self.fails("M1.user: EMPLOYEE_0008_SLACK_ID is not a member of private channel")

    def test_author_after_leaving(self):
        self.add("X1", ZOMBIE_SFX, "0005", "2025-09-26T16:00:00Z")                  # after spec leave L1
        self.fails("X1.user: .* is not a member of public channel")

    def test_author_before_a_first_join(self):
        self.add("X1", LEAPBLOCK, "0005", "2025-09-26T14:00:00Z")
        self.fails("X1.user: .* is not a member")

    def test_author_who_left_in_the_base_needs_a_rejoin(self):
        self.fx.doc["records"] = [r for r in self.fx.doc["records"] if r["key"] != "J1"]
        self.fails("S1.user: .* is not a member of private channel C05GU3E4SJY")

    def test_join_without_a_leave(self):
        self.fx.record("J1")["fields"]["channel"] = channel(ZM_ANIM)
        self.fx.doc["records"] = [r for r in self.fx.doc["records"] if r["key"] != "S1"]
        self.fails("no earlier channel_leave")

    def test_first_join_of_a_member(self):
        self.fx.record("F1")["fields"]["channel"] = channel(ZM_ANIM)
        self.fails("already in C09ATAJ220H")
        self.fx.record("F1")["fields"]["channel"] = channel(SOLSTEN)                 # left there: that is a rejoin
        self.fx.doc["records"] = [r for r in self.fx.doc["records"] if r["key"] not in ("J1", "S1")]
        self.fails("after a leave use slack.channel_join")

    def test_leave_rules(self):
        self.fx.record("L1")["fields"]["channel"] = channel(LEAPBLOCK)
        self.fx.doc["records"] = [r for r in self.fx.doc["records"] if r["key"] != "F1"]
        del self.fx.doc["overrides"]
        self.fails("nothing to leave")
        self.fx.record("L1")["fields"]["channel"] = channel(SOLSTEN)                 # already left in the base
        self.fx.doc["records"] = [r for r in self.fx.doc["records"] if r["key"] not in ("J1", "S1")]
        self.fails("already left C05GU3E4SJY")
        self.fx.record("L1")["fields"].update(channel=channel(ZOMBIE_SFX), at=lit("2025-08-15T16:00:00Z"))
        self.fails("base post\\(s\\) in C09A7PDFYCV after this leave")

    def test_two_leaves_in_a_row(self):
        self.fx.doc["records"].append({"key": "L2", "kind": "slack.channel_leave", "fields": {
            "channel": channel(ZOMBIE_SFX), "user": user("0005"), "at": lit("2025-09-26T17:00:00Z")}})
        self.fails("another leave in C09A7PDFYCV right after")

    def test_membership_rows_only_where_the_base_has_them(self):
        self.fx.record("L1")["fields"]["channel"] = channel(DM)
        self.fails("a direct message has no join or leave rows")
        self.fx.record("L1")["fields"]["channel"] = channel(CANVAS)
        self.fails("canvas-comment")
        self.fx.record("L1")["fields"]["channel"] = channel(GROUP_DM)
        self.fails("no base group DM has a leave row")

    def test_parent_rules(self):
        fields = self.fx.record("DM2")["fields"]
        fields["parent"] = ref("M1")
        self.fails("parent M1 is in C09ATAJ220H, the reply in D05SD5QLG94")
        fields["parent"] = ref("DM1")
        self.fx.record("M3")["fields"]["parent"] = ref("M2")
        self.fails("M2 is itself a reply")
        self.fx.record("M3")["fields"]["parent"] = ref("M1")
        self.fx.record("M2")["fields"]["at"] = lit("2025-09-29T17:55:00Z")
        self.fails("is not earlier than the reply")
        self.fx.record("M2")["fields"]["at"] = lit("2025-09-29T18:05:00Z")
        self.fx.record("M2")["fields"]["parent"] = lit("abc")
        self.fails("a parent is ref")
        self.fx.record("M2")["fields"]["parent"] = ref("L1")
        self.fails("L1 is a membership row")
        self.fx.record("M2")["fields"]["parent"] = ref("NOPE")
        self.fails("names no spec field")

    def test_base_parent_rules(self):
        fields = self.fx.record("RB0")["fields"]
        fields["parent"] = sbase("messages", f"{ZM_ANIM}:1759183318.447130")
        self.fails("not found in the pinned export")
        fields["parent"] = sbase("messages", f"{ZM_ANIM}:1756915029.480189")        # a base reply
        self.fails("is itself a reply")
        fields["parent"] = sbase("messages", f"{ZM_ANIM}:1755189890.568619")        # a base channel_join row
        self.fails("is a channel_join row")
        fields["parent"] = sbase("messages", f"{ZM_ANIM}:{BASE_POST}", "ts")        # must cite the id
        self.fails("a parent is ref")
        fields["parent"] = sbase("messages", f"{ZM_ANIM}:{BASE_POST}")
        fields["at"] = lit("2025-09-29T21:00:00Z")                                  # before the base post
        self.fails("is not earlier than the reply")
        fields["at"] = lit("2025-09-30T17:05:00Z")
        fields["channel"] = channel(DM)
        self.fails("is in C09ATAJ220H, the reply in D05SD5QLG94")

    def test_text_rules(self):
        self.fx.record("G1")["fields"]["text"] = self.fx.text("G1.txt", "moving our sync to 4pm\n")
        self.fails("ends with a line break")
        self.fx.record("G1")["fields"]["text"] = lit("ask <@U0NOBODY>")
        self.fails("mentions <@U0NOBODY>")
        self.fx.record("G1")["fields"]["text"] = lit("see <#C0NOSUCH001>")
        self.fails("links <#C0NOSUCH001>")
        self.fx.record("G1")["fields"]["text"] = lit("")
        self.fails("an empty message needs attachments")
        self.fx.record("G1")["fields"]["text"] = lit(5)
        self.fails("must be text")
        self.fx.record("G1")["fields"].update(text=lit("x"), attachments=lit({"a": 1}))
        self.fails("must be a JSON array")

    def test_mentions_of_real_users_and_channels_pass(self):
        self.fx.record("G1")["fields"]["text"] = lit(f"<@{JULIA}> see <#{ZM_ANIM}|zm-animations>")
        self.assertEqual(self.rows()["G1"]["text"], f"<@{JULIA}> see <#{ZM_ANIM}|zm-animations>")

    def test_same_user_same_second(self):
        self.add("X1", ZM_ANIM, "0016", "2025-09-29T18:00:00Z")
        self.fails("M1 and X1 get the same ts")

    def test_unverified_first_join_needs_its_override(self):
        del self.fx.doc["overrides"]
        self.fails("unverified convention")
        self.fx.doc["records"] = [r for r in self.fx.doc["records"] if r["key"] != "F1"]
        self.assertEqual(len(self.build().ops), 16)
        self.fx.doc["overrides"] = {"slack.membership.first_join": {"reason": "r", "platform_follow_up": "p"}}
        self.fails("match no unverified convention")

    def test_haystack_refusals(self):
        hs = self.fx.record("HS1")
        hs["rows"][0]["channel"] = ZM_ANIM
        self.fails("unknown row keys \\['channel'\\]")
        del hs["rows"][0]["channel"]
        sha = hs["rows"][0].pop("sha256")
        self.fails("row keys missing: \\['sha256'\\]")
        hs["rows"][0]["sha256"] = "0" * 64
        self.fails("sha256 is")
        hs["rows"][0]["sha256"] = sha
        hs["fields"]["user"] = user("0002")
        self.fails("shares only")
        del hs["fields"]["user"]
        del hs["fields"]["channel"]
        self.fails("shared fields missing")
        hs["fields"]["channel"] = channel(ZM_ANIM)
        hs["rows"][1]["user"] = "U0NOBODY"
        self.fails("HS1.002.user: base record slack/users/U0NOBODY not found")
        hs["rows"][1]["user"] = "EMPLOYEE_0006_SLACK_ID"
        self.add("HS1.001", ZM_ANIM, "0016", "2025-09-29T19:00:00Z")
        self.fails("duplicate record key")
        self.fx.doc["records"].pop()
        saved, hs["rows"] = hs["rows"], []
        self.fails("non-empty list")
        hs["rows"] = saved
        self.assertEqual(len(self.build().ops), 18)

    def test_snapshot_pin(self):
        self.fx.doc["snapshot"]["slack"]["sha256"] = "0" * 64
        self.fails("the spec pins")
        data = (SLACK_DIR / "channels.json").read_bytes()
        self.fx.doc["snapshot"]["slack"] = {"file": "channels.json", "sha256": hashlib.sha256(data).hexdigest()}
        self.fails("pin source_manifest.json")

    def test_unknown_kind_lists_the_haystack_kinds(self):
        self.fx.record("G1")["kind"] = "slack.dm"
        self.fails("unknown record kind .*slack.haystack")

    def test_explain_key(self):
        res = self.build()
        op = next(op for op in res.ops if op.record == "M1")
        self.assertEqual(registry.EMITTERS["slack"].key_of(op), (op.col("id"),))
        self.assertEqual(registry.EMITTERS["slack"].key_of(res.ops[0]), (LEAPBLOCK,))


if __name__ == "__main__":
    unittest.main()

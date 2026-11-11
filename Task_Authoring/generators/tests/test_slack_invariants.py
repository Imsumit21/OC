"""validate/slack.py: load_base on a small made-up export, and every rule S1-S11 with a good and a planted-bad case."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from generators.core.ops import Op
from generators.validate import overlay
from generators.validate import slack as sc

TA = Path(__file__).resolve().parents[2]
SCRATCH = TA / "support" / "scratch"
FREEZE = "2024-04-01T00:00:00Z"
PRIV, PUB, DM, GROUP, CANVAS, OLD = "C0TESTPRIV1", "C0TESTPUB01", "D0TESTDM001", "CAAAAAAAAAA1", "CFCFCFCFCFC1", \
    "C0TESTARCH1"
A, B, C, D, BOT = "U0A", "U0B", "U0C", "U0D", "B0T"
POST, THREAD, REPLY1, REPLY2 = "1709600000.000019", "1709700000.000029", "1709700100.000039", "1709700200.000049"


def mid(channel: str, ts: str) -> str:
    return hashlib.sha256(f"{channel}|{ts}".encode()).hexdigest()[:32]


def created(ts: str) -> str:
    sec, frac = ts.split(".")
    return f"{dt.datetime.fromtimestamp(int(sec), dt.timezone.utc):%Y-%m-%dT%H:%M:%S}.{frac}Z"


def export_row(channel, ts, user, text="x", **extra) -> dict:
    row = {"id": mid(channel, ts), "ts": ts, "type": "message", "user": user, "text": text, "channel": channel,
           "thread_ts": None, "reply_count": 0, "reply_users_count": 0, "latest_reply": None,
           "is_activity_message": False, "subtype": None, "reactions": [], "files": [], "attachments": []}
    row.update(extra)
    return row


def write_export(root: Path) -> str:
    """A made-up Slack export; returns the sha256 of its source_manifest.json."""
    def chan(cid, name, members, **flags):
        row = {"id": cid, "name": name, "is_channel": True, "is_private": False, "is_im": False, "is_mpim": False,
               "is_archived": False, "is_general": False, "num_members": len(members), "topic": "", "purpose": "",
               "created": "1709000000.000000", "creator": A, "members": members}
        row.update(flags)
        return row

    files = {
        "channels.json": [
            chan(PRIV, "priv", [A, B, C], is_private=True),
            chan(PUB, "pub", [A, B]),
            chan(DM, DM, [A, B], is_channel=False, is_im=True, created="0.000000", creator=None),
            chan(GROUP, "mpdm-a--b--c-1", [A, B, C], is_channel=False, is_private=True, is_mpim=True),
            chan(CANVAS, "FC:F0000000001:Notes", [A]),
            chan(OLD, "old", [A], is_private=True, is_archived=True),
        ],
        "users.json": [{"id": u, "name": u, "real_name": u, "display_name": u, "email": None, "avatar_url": None,
                        "is_bot": u == BOT, "is_admin": False, "deleted": False, "timezone": "America/Los_Angeles"}
                       for u in (A, B, C, D, BOT)],
        f"messages/{PRIV}/2024-03.json": [
            export_row(PRIV, "1709500000.000009", C, f"<@{C}> has joined the channel", subtype="channel_join"),
            export_row(PRIV, POST, A, "a post without replies"),
            export_row(PRIV, THREAD, A, "a thread", thread_ts=THREAD, reply_count=2, reply_users_count=2,
                       latest_reply=REPLY2),
            export_row(PRIV, REPLY1, B, "first reply", thread_ts=THREAD),
            # a raw Slack API row: no id, no counters; it still is the thread's second reply
            {"channel": PRIV, "client_msg_id": "c-1", "team": "T1", "text": "raw reply", "thread_ts": THREAD,
             "ts": REPLY2, "type": "message", "user": C, "parent_user_id": A},
        ],
        f"messages/{PUB}/2024-03.json": [
            export_row(PUB, "1709300000.000009", B, f"<@{B}> has joined the channel", subtype="channel_join"),
            export_row(PUB, "1709310000.000019", B, "hello"),
            export_row(PUB, "1709400000.000029", B, f"<@{B}> has left the channel", subtype="channel_leave"),
        ],
    }
    listed = []
    for rel, doc in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        data = json.dumps(doc).encode("utf-8")
        path.write_bytes(data)
        listed.append({"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    manifest = json.dumps({"path": "slack", "files": listed}).encode("utf-8")
    (root / "source_manifest.json").write_bytes(manifest)
    return hashlib.sha256(manifest).hexdigest()


def msg(channel, ts, user, text="hello", **over) -> Op:
    cols = {"id": mid(channel, ts), "ts": ts, "channel_id": channel, "type": "message", "user_id": user, "text": text,
            "thread_parent_id": None, "thread_ts_legacy": None, "reply_count": 0, "reply_users_count": 0,
            "latest_reply": None, "is_activity_message": False, "subtype": None, "reactions_json": "[]",
            "files_json": "[]", "attachments_json": "[]", "created_at": created(ts), "metadata_json": "{}"}
    cols.update(over)
    return Op("slack.slack_messages", "insert", tuple(cols.items()))


def reply(channel, ts, user, parent_ts, **over) -> Op:
    cols = {"thread_parent_id": mid(channel, parent_ts), "thread_ts_legacy": parent_ts}
    cols.update(over)
    return msg(channel, ts, user, **cols)


def parent_update(channel, parent_ts, count, users, latest, legacy=True) -> Op:
    cols = (("thread_ts_legacy", parent_ts),) if legacy else ()
    cols += (("reply_count", count), ("reply_users_count", users), ("latest_reply", latest))
    return Op("slack.slack_messages", "update", cols, where=(("id", mid(channel, parent_ts)),))


def event(channel, ts, user, kind, text=None, **over) -> Op:
    words = {"channel_join": "has joined the channel", "channel_leave": "has left the channel"}[kind]
    return msg(channel, ts, user, text=text or f"<@{user}> {words}", subtype=kind, **over)


def members_update(channel, members, count=None) -> Op:
    return Op("slack.slack_channels", "update",
              (("num_members", len(members) if count is None else count), ("members_json", json.dumps(members))),
              where=(("id", channel),))


class SlackInvariantTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        cls.root = Path(tempfile.mkdtemp(prefix="slack_inv_", dir=str(SCRATCH)))
        cls.pin = write_export(cls.root)
        cls.base = sc.load_base(cls.root, cls.pin, {PRIV, PUB, DM, GROUP, CANVAS, OLD})

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.root, ignore_errors=True)

    def run_ops(self, ops):
        ov = overlay.apply(self.base, ops)
        return ov, sc.check_slack(ov, self.base, freeze_utc=FREEZE)

    def rules(self, ops, severity="FAIL"):
        ov, found = self.run_ops(ops)
        self.assertEqual(ov.errors, [])
        return sorted({f.rule for f in found if f.severity == severity})

    def messages(self, ops, rule):
        return [f.message for f in self.run_ops(ops)[1] if f.rule == rule]

    # ---- loading
    def test_load_base_shapes_rows_and_keeps_raw_rows(self):
        rows = self.base[sc.MESSAGES]
        self.assertEqual(len(rows), 8)
        thread = rows[(mid(PRIV, THREAD),)]
        self.assertEqual((thread["channel_id"], thread["user_id"], thread["thread_ts_legacy"], thread["reply_count"]),
                         (PRIV, A, THREAD, 2))
        self.assertEqual(thread["reactions_json"], "[]")
        raw = rows[(f"noid:{PRIV}:{REPLY2}",)]
        self.assertIsNone(raw["id"])
        self.assertEqual((raw["user_id"], raw["thread_ts_legacy"], raw["reply_count"]), (C, THREAD, 0))
        channel = self.base[sc.CHANNELS][(PRIV,)]
        self.assertEqual(json.loads(channel["members_json"]), [A, B, C])
        self.assertEqual(channel["created_ts"], 1709000000.0)

    def test_load_base_refuses_another_export(self):
        with self.assertRaisesRegex(sc.SlackBaseError, "is not the pinned"):
            sc.load_base(self.root, "0" * 64, {PRIV})
        other = Path(tempfile.mkdtemp(prefix="slack_inv_", dir=str(SCRATCH)))
        try:
            pin = write_export(other)
            shard = other / "messages" / PRIV / "2024-03.json"
            shard.write_bytes(shard.read_bytes().replace(b"first reply", b"other reply"))
            with self.assertRaisesRegex(sc.SlackBaseError, "differs from source_manifest.json"):
                sc.load_base(other, pin, {PRIV})
            sc.load_base(other, pin, {PUB})                    # a channel whose files were not touched still loads
        finally:
            shutil.rmtree(other, ignore_errors=True)

    def test_channels_of(self):
        ops = [msg(PRIV, "1709800000.000019", A), members_update(PUB, [A, B]),
               parent_update(GROUP, POST, 1, 1, "1709800000.000019")]
        self.assertEqual(sc.channels_of(ops), {PRIV, PUB})

    # ---- a clean set
    def test_good_overlay_has_no_findings(self):
        new_thread, r1, r2 = "1709800000.000019", "1709800060.000029", "1709800120.000039"
        ops = [
            msg(PRIV, new_thread, A, thread_ts_legacy=new_thread, reply_count=2, reply_users_count=2, latest_reply=r2),
            reply(PRIV, r1, B, new_thread),
            reply(PRIV, r2, C, new_thread),
            reply(PRIV, "1709800200.000049", B, POST),
            parent_update(PRIV, POST, 1, 1, "1709800200.000049"),
            reply(PRIV, "1709800300.000059", A, THREAD),
            parent_update(PRIV, THREAD, 3, 3, "1709800300.000059"),
            msg(DM, "1709800400.000069", B, "a DM"),
            msg(GROUP, "1709800500.000079", C, f"hi <@{A}> see <#{PUB}>"),
            event(PUB, "1709800600.000089", B, "channel_join"),
            msg(PUB, "1709800700.000099", B, "back"),
            msg(PUB, "1709800800.000109", BOT, "", attachments_json='[{"text": "card"}]'),
        ]
        ov, found = self.run_ops(ops + [members_update(PUB, [A, B, BOT])])
        self.assertEqual(ov.errors, [])
        self.assertEqual([(f.rule, f.severity, f.message) for f in found if f.severity == "FAIL"], [])
        self.assertEqual([f.rule for f in found if f.severity == "WARN"], ["S11"])    # BOT added without a join row

    # ---- S1
    def test_s1_row_shape(self):
        ts = "1709800000.000019"
        self.assertEqual(self.rules([msg(PRIV, ts, A, id="0" * 32)]), ["S1"])
        self.assertIn("sha256", self.messages([msg(PRIV, ts, A, id="0" * 32)], "S1")[0])
        self.assertEqual(self.rules([msg(PRIV, "1709800000.19", A, id="a" * 32)]), ["S1"])
        self.assertEqual(self.rules([msg(PRIV, ts, A, type="note")]), ["S1"])
        self.assertEqual(self.rules([msg(PRIV, ts, A, created_at="2024-03-07T08:26:42Z")]), ["S1"])
        self.assertEqual(self.rules([msg(PRIV, ts, A, created_at="yesterday")]), ["S1"])
        self.assertEqual(self.rules([msg(PRIV, ts, A, reactions_json="{}")]), ["S1"])
        self.assertEqual(self.rules([msg(PRIV, ts, A, metadata_json="[]")]), ["S1"])
        self.assertEqual(self.rules([msg(PRIV, ts, A, text="")]), ["S1"])
        self.assertEqual(self.rules([msg(PRIV, ts, A, is_activity_message=True)], "WARN"), ["S1"])

    def test_s1_accepts_the_created_at_forms_the_platform_accepted(self):
        ts = "1709800000.000019"                                   # 2024-03-07T08:26:40Z
        for form in ("2024-03-07T08:26:40Z", "2024-03-07T08:26:40.000000Z", "2024-03-07T08:26:40.000019Z",
                     "2024-03-07 08:26:40+00"):
            self.assertEqual(self.rules([msg(PRIV, ts, A, created_at=form)]), [], form)

    # ---- S2, S3
    def test_s2_unknown_channel_or_user(self):
        ov, found = self.run_ops([msg("C0NOSUCH001", "1709800000.000019", A)])
        self.assertIn("S2", {f.rule for f in found})
        self.assertEqual(self.rules([msg(PRIV, "1709800000.000019", "U0NOBODY")]), ["S2", "S6"])

    def test_s3_channel_ts_is_unique(self):
        self.assertEqual(self.rules([msg(PRIV, POST, A, id="f" * 32)]), ["S1", "S3"])
        ov, _ = self.run_ops([msg(PRIV, POST, A)])                # the same id: the overlay itself refuses it
        self.assertTrue(any("existing key" in e for e in ov.errors))

    # ---- S4
    def test_s4_reply_rules(self):
        ts = "1709800000.000019"
        good = [parent_update(PRIV, POST, 1, 1, ts)]
        self.assertEqual(self.rules([reply(PRIV, ts, B, POST)] + good), [])
        self.assertEqual(self.rules([msg(PRIV, ts, B, thread_parent_id="e" * 32, thread_ts_legacy=POST)]), ["S4"])
        # thread_ts_legacy without the parent id: not a reply (S4), and not a thread's first post either (S5)
        self.assertEqual(self.rules([msg(PRIV, ts, B, thread_ts_legacy=POST)] + good), ["S4", "S5"])
        self.assertIn("is not the parent's ts",
                      " ".join(self.messages([reply(PRIV, ts, B, POST, thread_ts_legacy=THREAD)], "S4")))
        early = "1709599999.000019"
        self.assertIn("is not after", " ".join(self.messages(
            [reply(PRIV, early, B, POST), parent_update(PRIV, POST, 1, 1, early)], "S4")))
        self.assertIn("itself a reply", " ".join(self.messages([reply(PRIV, ts, A, REPLY1)], "S4")))
        self.assertIn("carries reply_count 0", " ".join(self.messages(
            [reply(PRIV, ts, B, POST, reply_count=1)] + good, "S4")))
        other = [reply(PUB, ts, A, POST, thread_parent_id=mid(PRIV, POST))]
        self.assertIn("is in channel", " ".join(self.messages(other, "S4")))
        join_row = "1709500000.000009"
        self.assertIn("channel_join row", " ".join(self.messages([reply(PRIV, ts, A, join_row)], "S4")))

    # ---- S5
    def test_s5_thread_counters(self):
        ts = "1709800000.000019"
        self.assertEqual(self.rules([reply(PRIV, ts, B, POST)]), ["S5"])                  # parent not updated
        self.assertEqual(self.rules([reply(PRIV, ts, B, POST), parent_update(PRIV, POST, 2, 1, ts)]), ["S5"])
        self.assertEqual(self.rules([reply(PRIV, ts, B, POST), parent_update(PRIV, POST, 1, 2, ts)]), ["S5"])
        self.assertEqual(self.rules([reply(PRIV, ts, B, POST), parent_update(PRIV, POST, 1, 1, REPLY1)]), ["S5"])
        # into a base thread: the raw reply row counts, and the newest reply stays the newest
        self.assertEqual(self.rules([reply(PRIV, ts, A, THREAD), parent_update(PRIV, THREAD, 3, 3, ts)]), [])
        self.assertEqual(self.rules([reply(PRIV, ts, A, THREAD), parent_update(PRIV, THREAD, 2, 2, ts)]), ["S5"])
        between = "1709700150.000019"
        self.assertEqual(self.rules([reply(PRIV, between, B, THREAD),
                                     parent_update(PRIV, THREAD, 3, 2, REPLY2)]), [])
        self.assertEqual(self.rules([reply(PRIV, between, B, THREAD),
                                     parent_update(PRIV, THREAD, 3, 2, between)]), ["S5"])
        self.assertEqual(self.rules([msg(PRIV, ts, A, reply_count=1, reply_users_count=1, latest_reply=ts)]), ["S5"])
        self.assertEqual(self.rules([msg(PRIV, ts, A, thread_ts_legacy=ts)]), ["S5"])     # own ts without replies

    def test_s5_first_post_without_its_own_ts_is_a_warning(self):
        ts, r = "1709800000.000019", "1709800060.000029"
        new = [msg(PRIV, ts, A, reply_count=1, reply_users_count=1, latest_reply=r), reply(PRIV, r, B, ts)]
        self.assertEqual(self.rules(new), [])
        self.assertEqual(self.rules(new, "WARN"), ["S5"])
        base_parent = [reply(PRIV, ts, B, POST), parent_update(PRIV, POST, 1, 1, ts, legacy=False)]
        self.assertEqual(self.rules(base_parent), [])
        self.assertEqual(self.rules(base_parent, "WARN"), ["S5"])

    # ---- S6
    def test_s6_author_is_a_member_at_that_time(self):
        ts = "1709800000.000019"
        self.assertEqual(self.rules([msg(PRIV, ts, D)]), ["S6"])                           # never a member
        self.assertEqual(self.rules([msg(PUB, ts, D)]), ["S6"])                            # public: the same rule
        self.assertEqual(self.rules([msg(DM, ts, C)]), ["S6"])
        self.assertEqual(self.rules([msg(PUB, ts, B)]), ["S6"])                            # B left PUB in the base
        self.assertEqual(self.rules([msg(PUB, "1709350000.000019", B)]), [])               # between join and leave
        self.assertEqual(self.rules([msg(PUB, "1709200000.000019", B)]), ["S6"])           # before B joined
        self.assertEqual(self.rules([msg(PRIV, "1709450000.000019", C)]), ["S6"])          # before C joined
        self.assertEqual(self.rules([msg(PRIV, ts, C)]), [])
        rejoin = [event(PUB, "1709750000.000019", B, "channel_join"), msg(PUB, ts, B)]
        self.assertEqual(self.rules(rejoin), [])

    # ---- S7
    def test_s7_join_needs_a_user_who_is_not_a_member(self):
        ts = "1709800000.000019"
        # the platform's C1 finding: a join by a listed member who never left
        self.assertIn("never left", " ".join(self.messages([event(PRIV, ts, A, "channel_join")], "S7")))
        self.assertEqual(self.rules([event(PRIV, ts, A, "channel_join")]), ["S7"])
        self.assertIn("without an earlier leave", " ".join(self.messages([event(PRIV, ts, C, "channel_join")], "S7")))
        self.assertEqual(self.rules([event(PUB, ts, B, "channel_join")]), [])              # rejoin after a base leave
        two = [event(PUB, ts, B, "channel_join"), event(PUB, "1709800100.000029", B, "channel_join")]
        self.assertEqual(self.rules(two), ["S7"])
        before_base_join = [event(PUB, "1709250000.000019", B, "channel_join")]
        self.assertIn("another join", " ".join(self.messages(before_base_join, "S7")))

    def test_s7_first_join_needs_the_member_list(self):
        ts = "1709800000.000019"
        alone = [event(PRIV, ts, D, "channel_join")]
        self.assertEqual(self.rules(alone), ["S7"])
        self.assertIn("members_json does not list", " ".join(self.messages(alone, "S7")))
        listed = alone + [members_update(PRIV, [A, B, C, D])]
        self.assertEqual(self.rules(listed), [])
        self.assertEqual(self.rules(listed, "WARN"), ["S7"])                               # no accepted precedent
        self.assertEqual(self.rules(listed + [msg(PRIV, "1709800100.000029", D)]), [])
        # a post before the join: the author is not a member yet (S6) and the join is no longer a first one (S7)
        self.assertEqual(self.rules(listed + [msg(PRIV, "1709799000.000029", D)]), ["S6", "S7"])

    def test_s7_leave_rules_and_wording(self):
        ts = "1709800000.000019"
        self.assertEqual(self.rules([event(PRIV, ts, A, "channel_leave")]), [])
        self.assertEqual(self.rules([event(PRIV, ts, D, "channel_leave")]), ["S7"])        # never in it
        self.assertEqual(self.rules([event(PUB, ts, B, "channel_leave")]), ["S7"])         # already left
        early = [event(PRIV, "1709550000.000019", A, "channel_leave")]                     # A posts later in base
        self.assertIn("after this leave", " ".join(self.messages(early, "S7")))
        self.assertEqual(self.rules([event(PRIV, ts, A, "channel_join", text="joined")]), ["S7"])
        self.assertEqual(self.rules([event(PRIV, ts, A, "channel_leave", text=f"<@{B}> has left the channel")]),
                         ["S7"])
        group = [event(GROUP, ts, D, "channel_join", text=f"<@{D}> has joined the conversation"),
                 members_update(GROUP, [A, B, C, D])]
        self.assertEqual(self.rules(group), [])
        self.assertEqual(self.rules([event(GROUP, ts, D, "channel_join"), members_update(GROUP, [A, B, C, D])]),
                         ["S7"])                                                           # 'channel' in a group DM
        in_thread = [event(PUB, ts, B, "channel_join", thread_ts_legacy=ts)]
        self.assertIn("not part of a thread", " ".join(self.messages(in_thread, "S7")))

    def test_s7_canvas_and_dm_rows_are_warnings(self):
        ts = "1709800000.000019"
        rows = [event(CANVAS, ts, A, "channel_leave", text=f"<@{A}> has left the conversation")]
        self.assertEqual(self.rules(rows), [])
        self.assertEqual(self.rules(rows, "WARN"), ["S7"])
        self.assertEqual(self.rules([event(DM, ts, A, "channel_leave")], "WARN"), ["S7"])

    # ---- S8-S11
    def test_s8_nothing_at_or_after_the_freeze(self):
        at, after = "1711929600.000019", "1711929700.000019"                               # 2024-04-01T00:00:00Z
        self.assertEqual(self.rules([msg(PRIV, at, A)]), ["S8"])
        self.assertEqual(self.rules([msg(PRIV, "1711929599.000019", A)]), [])
        self.assertIn("latest_reply", " ".join(self.messages(
            [parent_update(PRIV, THREAD, 2, 2, after)], "S8")))

    def test_s9_channel_age_and_archive(self):
        self.assertEqual(self.rules([msg(PRIV, "1708000000.000019", A)]), ["S9"])
        self.assertEqual(self.rules([msg(OLD, "1709800000.000019", A)], "WARN"), ["S9"])
        self.assertEqual(self.rules([msg(DM, "1708000000.000019", A)]), [])               # created 0: unknown

    def test_s10_mentions_resolve(self):
        ts = "1709800000.000019"
        self.assertEqual(self.rules([msg(PRIV, ts, A, text="ask <@U0NOBODY>")]), ["S10"])
        self.assertEqual(self.rules([msg(PRIV, ts, A, text="see <#C0NOSUCH001|x>")]), ["S10"])
        self.assertEqual(self.rules([msg(PRIV, ts, A, text=f"ask <@{B}|bee> in <#{PUB}>")]), [])

    def test_s11_channel_member_list(self):
        self.assertEqual(self.rules([members_update(PRIV, [A, B, C, D], count=3)]), ["S11"])
        self.assertEqual(self.rules([members_update(PRIV, [A, B, C, "U0NOBODY"])]), ["S11"])
        self.assertEqual(self.rules([members_update(PRIV, [A, B, C, C])]), ["S11"])
        self.assertEqual(self.rules([members_update(PRIV, [A, B])], "WARN"), ["S11"])     # drops C
        self.assertEqual(self.rules([members_update(PRIV, [A, B, C, D])], "WARN"), ["S11"])  # D without a join
        bad = Op("slack.slack_channels", "update", (("members_json", "{}"),), where=(("id", PRIV),))
        self.assertEqual(self.rules([bad]), ["S11"])


ARCHIVE = TA / "support" / "completed_tasks"
UNIVERSES = {
    "normal": (TA.parent / "Universe_Normal" / "Normal_HarmonyGames_Other_Services" / "Services_Data" / "slack",
               "2026-02-14T00:00:00Z"),
    "synthcut": (TA.parent / "Universe_SynthCut" / "SynthCut_HarmonyGames_Other_Services" / "Services_Data" / "slack",
                 "2025-10-01T00:00:00Z"),
}


class AcceptedSqlTest(unittest.TestCase):
    """SQL that passed the platform's /injection review must satisfy the invariants (a FAIL here means a rule is
    wrong or too strict, not that the archive is)."""

    def check(self, task: str, universe: str):
        from generators.validate import parse_back
        sql = ARCHIVE / task / "task_inputs" / "01_Universe_Inject.sql"
        root, freeze = UNIVERSES[universe]
        if not sql.is_file() or not (root / "source_manifest.json").is_file():
            self.skipTest(f"{task} or the {universe} Slack export is not installed")
        ops = [op for op in parse_back.parse_ops(sql.read_text(encoding="utf-8"),
                                                 schema_path=TA / "references" / "universe_schema_live.json")
               if op.table.startswith("slack.")]
        pin = hashlib.sha256((root / "source_manifest.json").read_bytes()).hexdigest()
        base = sc.load_base(root, pin, sc.channels_of(ops))
        ov = overlay.apply(base, ops)
        self.assertEqual(ov.errors, [])
        found = sc.check_slack(ov, base, freeze_utc=freeze)
        self.assertEqual([(f.rule, f.message) for f in found if f.severity == "FAIL"], [])
        return ops, found

    def test_samuel_threads_and_dms(self):
        ops, found = self.check("samuel_zm_beta_messages_2026-11-09", "synthcut")
        self.assertEqual((sum(op.op == "insert" for op in ops), sum(op.op == "update" for op in ops)), (7, 2))
        self.assertEqual(found, [])

    def test_owen_rejoins_and_replies_under_base_posts(self):
        ops, found = self.check("owen_dd_bug_carryover_2026-11-09", "normal")
        self.assertEqual((sum(op.op == "insert" for op in ops), sum(op.op == "update" for op in ops)), (42, 25))
        joins = [op for op in ops if op.col("subtype") == "channel_join"]
        self.assertEqual(len(joins), 6)
        # the two membership rows in a canvas-comment channel are the only warnings (the reviewer's advisory 5)
        self.assertEqual({f.rule for f in found}, {"S7"})
        self.assertTrue(all("canvas" in f.message for f in found))

    def test_julia_first_posts_without_their_own_ts_only_warn(self):
        _, found = self.check("julia_zm_difficulty_baseline_2026-11-01", "synthcut")
        self.assertEqual([(f.rule, f.severity) for f in found], [("S5", "WARN")] * 3)

    def test_robert_seed_bets_threads_and_dms(self):
        ops, found = self.check("robert_seed_bets_2026-11-11", "normal")
        self.assertEqual((sum(op.op == "insert" for op in ops), found), (4, []))

    def test_every_archived_task_in_its_own_universe(self):
        """All 15 archived tasks: no FAIL in the universe each was written for (warnings listed per task)."""
        want = {  # task -> (universe, warning rules); the universe follows each task's 00_Assigments.md clock
            "claire_zm3d_halloween_art_plan_2026-11-10": ("synthcut", set()),
            "douglas_beta_server_signoff_2026-10-28": ("synthcut", set()),
            "frederick_account_handover_2026-10-26": ("synthcut", set()),
            "frederick_bridge_pipeline_2026-11-03": ("synthcut", set()),
            "frederick_card_spend_q3_6ad83eebbd6456fd065bbd20": ("synthcut", set()),
            "frederick_q4_commitments_2026-11-05": ("synthcut", set()),
            "julia_zm3d_beta_calendar_2026-11-07": ("synthcut", {"S9"}),       # a post into an archived channel
            "julia_zm_difficulty_baseline_2026-11-01": ("synthcut", {"S5"}),
            "leonard_stockholder_closeout_2026-11-10": ("normal", set()),
            "owen_dd_bug_carryover_2026-11-09": ("normal", {"S7"}),
            "robert_llc_takeover_2026-11-06": ("normal", set()),
            "robert_seed_bets_2026-11-11": ("normal", set()),
            "robert_winddown_closeout_2026-10-30": ("normal", set()),
            "samuel_zm_beta_messages_2026-11-09": ("synthcut", set()),
            "vincent_zm3d_release_gate_2026-11-06": ("synthcut", set()),
        }
        for task, (universe, warned) in sorted(want.items()):
            with self.subTest(task=task):
                _, found = self.check(task, universe)
                self.assertEqual({f.rule for f in found}, warned)


if __name__ == "__main__":
    unittest.main()

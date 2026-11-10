"""validate/gmail.py: load_base on a small made-up export, every rule G1-G12 with a good and a planted-bad case, and the
Gmail rows of the 15 archived tasks parsed back through the rules."""
from __future__ import annotations

import datetime as dt
import email.utils
import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from generators.core.ops import Op
from generators.validate import gmail as gc
from generators.validate import overlay

TA = Path(__file__).resolve().parents[2]
SCRATCH = TA / "support" / "scratch"
FREEZE = "2024-04-01T00:00:00Z"
ANN, BOB, CAT, DAN = "ann@harmonygames.co", "bob@harmonygames.co", "cat@harmonygames.co", "dan@harmonygames.co"
NAMES = {ANN: "ann", BOB: "bob", CAT: "Cat Lee", DAN: "dan"}
P_RFC, Q_RFC = "<p1@mail.gmail.com>", "<q1@mail.gmail.com>"


def ms(when: str) -> int:
    return int(dt.datetime.strptime(when, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc).timestamp()) * 1000


def tnum(when: str, low: int = 7) -> str:
    return str((ms(when) << 20) | low)


def form(addr: str) -> str:
    return f"{NAMES[addr]} <{addr}>"


TA_ID = f"{ANN}/{tnum('2024-03-01T10:00:00Z', 1)}"
TB_ID = f"{BOB}/{tnum('2024-03-01T10:00:00Z', 2)}"


def write_export(root: Path) -> str:
    """A made-up Gmail export; returns the sha256 of its source_manifest.json."""
    def m(box, rfc, frm, to, date, subject, body, labels, **extra):
        row = {"id": f"{box}/{rfc}", "labelIds": labels, "subject": subject, "from": form(frm),
               "to": ", ".join(form(a) for a in to), "cc": "", "bcc": "", "reply_to": "", "body": body, "date": date,
               "date_parsed": date.replace("Z", "+00:00"), "headers": [{"name": "Message-ID", "value": rfc}],
               "in_reply_to": "", "references": "", "internal_date_ms": str(ms(date)), "attachments": [],
               "mbox_from": None}
        row.update(extra)
        return row

    p = dict(frm=ANN, to=[BOB, DAN], date="2024-03-01T10:00:00Z", subject="Plan", body="The plan.\r\nRead it.")
    files = {
        "users.json": [{"emailAddress": a, "name": None, "messagesTotal": 1, "threadsTotal": 1, "historyId": None}
                       for a in (ANN, BOB, CAT)],
        "labels.json": [{"id": x, "name": x.title(), "type": "system"} for x in
                        ("INBOX", "SENT", "IMPORTANT", "UNREAD", "ARCHIVED")]
        + [{"id": "CATEGORY_PERSONAL", "name": "Personal", "type": "system"}],
        "threads/00000000.json": {"id": TA_ID, "user_email": ANN, "historyId": None,
                                  "messages": [m(ANN, P_RFC, labels=["SENT"], **p)]},
        "threads/00000001.json": {"id": TB_ID, "user_email": BOB, "historyId": None, "messages": [
            m(BOB, Q_RFC, BOB, [ANN], "2024-03-05T09:00:00Z", "Re: Plan", "Later note.", ["SENT"],
              in_reply_to=P_RFC, references=P_RFC, cc=form(CAT)),
            m(BOB, P_RFC, labels=["INBOX"], **p)]},
    }
    listed = []
    for rel, doc in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        data = json.dumps(doc).encode("utf-8")
        path.write_bytes(data)
        listed.append({"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    manifest = json.dumps({"path": "gmail", "files": listed}).encode("utf-8")
    (root / "source_manifest.json").write_bytes(manifest)
    return hashlib.sha256(manifest).hexdigest()


def message(box, rfc, thread, frm, to, date, *, cc=(), subject="Kickoff", body="Kickoff is Monday.\r\nBring notes.",
            labels=None, irt="", refs="", **over) -> Op:
    labels = labels if labels is not None else (["SENT"] if box == frm else ["INBOX", "CATEGORY_PERSONAL"])
    headers = [("X-GM-THRID", thread.split("/")[1]), ("MIME-Version", "1.0"),
               ("Date", email.utils.format_datetime(dt.datetime.fromtimestamp(ms(date) // 1000, dt.timezone.utc))),
               ("References", refs or None), ("In-Reply-To", irt or None), ("Message-ID", rfc), ("Subject", subject),
               ("From", form(frm)), ("To", ", ".join(form(a) for a in to)),
               ("Cc", ", ".join(form(a) for a in cc) or None)]
    cols = {"id": f"{box}/{rfc}", "thread_id": thread, "user_email": box, "label_ids_json": json.dumps(labels),
            "snippet": " ".join(body.split())[:140], "internal_date": ms(date), "date": date, "size_estimate": 500,
            "subject": subject, "from_email": frm, "from_name": NAMES[frm],
            "to_json": json.dumps([form(a) for a in to]), "cc_json": json.dumps([form(a) for a in cc]),
            "bcc_json": "[]", "reply_to_json": "[]", "body_text": body, "body_html": None,
            "headers_json": json.dumps([{"name": n, "value": v} for n, v in headers if v is not None]),
            "in_reply_to": irt, "references": refs, "mbox_from": None, "attachments_meta_json": "[]"}
    cols.update(over)
    return Op("gmail.gmail_messages", "insert", tuple(cols.items()))


def thread(tid, box, snippet="Kickoff is Monday. Bring notes.") -> Op:
    return Op("gmail.gmail_threads", "insert", (("id", tid), ("user_email", box), ("snippet", snippet),
                                                ("history_id", None)))


def snippet_update(tid, snippet) -> Op:
    return Op("gmail.gmail_threads", "update", (("snippet", snippet),), where=(("id", tid),))


N_AT = "2024-03-10T12:00:00Z"
N_RFC = "<n1@mail.gmail.com>"


def new_mail(drop=(), **over) -> list:
    """Ann to Bob, cc Cat: three copies, three new threads."""
    ops = []
    for n, box in enumerate((ANN, BOB, CAT)):
        if box in drop:
            continue
        tid = f"{box}/{tnum(N_AT, n)}"
        ops.append(thread(tid, box))
        ops.append(message(box, N_RFC, tid, ANN, [BOB], N_AT, cc=[CAT], **over.get(box, {})))
    return ops


class GmailInvariantTest(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="gmail_base_", dir=str(SCRATCH)))
        self.pin = write_export(self.root)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def found(self, ops):
        base, facts = gc.load_base(self.root, self.pin, ops)
        ov = overlay.apply(base, ops)
        self.assertEqual(ov.errors, [])
        return gc.check_gmail(ov, base, facts, freeze_utc=FREEZE)

    def rules(self, ops, severity="FAIL"):
        return sorted({f.rule for f in self.found(ops) if f.severity == severity})

    def test_load_base_shapes_rows(self):
        base, facts = gc.load_base(self.root, self.pin, [message(BOB, "<r@x.co>", TB_ID, BOB, [ANN], N_AT,
                                                                 irt=P_RFC, refs=P_RFC)])
        self.assertEqual(sorted(k[0] for k in base[gc.THREADS]), sorted([TA_ID, TB_ID]))   # the parent's threads too
        row = base[gc.MESSAGES][(f"{BOB}/{P_RFC}",)]
        self.assertEqual((row["thread_id"], row["from_email"], row["from_name"], row["date"], row["internal_date"]),
                         (TB_ID, ANN, "ann", "2024-03-01T10:00:00Z", ms("2024-03-01T10:00:00Z")))
        self.assertEqual(json.loads(row["to_json"]), ["bob <bob@harmonygames.co>", "dan <dan@harmonygames.co>"])
        self.assertEqual(facts.copies[P_RFC], {(ANN, TA_ID), (BOB, TB_ID)})
        self.assertEqual(facts.names[DAN], {"dan"})
        self.assertEqual(sorted(base[gc.USERS]), [(ANN,), (BOB,), (CAT,)])

    def test_load_base_refuses_another_export(self):
        with self.assertRaises(gc.GmailBaseError):
            gc.load_base(self.root, "0" * 64, [])
        users = self.root / "users.json"
        users.write_bytes(users.read_bytes() + b" ")
        with self.assertRaisesRegex(gc.GmailBaseError, "differs from source_manifest.json"):
            gc.load_base(self.root, self.pin, [])

    def test_address_parser_keeps_tokens(self):
        self.assertEqual(gc._addresses('Calvin Price <[EMAIL_0801]>, "a, b" <x@y.co>, SVC_0325_EMAIL'),
                         [("Calvin Price", "[EMAIL_0801]"), ("a, b", "x@y.co"), ("", "SVC_0325_EMAIL")])

    def test_good_overlay_has_no_findings(self):
        self.assertEqual(self.found(new_mail()), [])

    def test_g1_row_shape(self):
        self.assertEqual(self.rules(new_mail(**{BOB: {"id": f"{ANN}/{N_RFC}x"}})), ["G1", "G10", "G4"])
        self.assertIn("G1", self.rules(new_mail(**{BOB: {"internal_date": ms(N_AT) + 5000}})))
        self.assertIn("G1", self.rules(new_mail(**{BOB: {"cc_json": "{}"}})))
        self.assertIn("G1", self.rules(new_mail(**{BOB: {"history_id": "abc"}})))
        self.assertIn("G1", self.rules(new_mail(**{BOB: {"body_text": " ", "snippet": ""}}), "WARN"))

    def test_g2_references(self):
        ops = new_mail()
        ops[3] = message(BOB, N_RFC, TA_ID, ANN, [BOB], N_AT, cc=[CAT])            # Bob's copy in Ann's thread
        self.assertIn("G2", self.rules(ops))
        self.assertIn("G2", self.rules(new_mail(**{BOB: {"label_ids_json": '["INBOX", "NOPE"]'}})))

    def test_g3_ids_are_new(self):
        ops = [message(BOB, P_RFC, TB_ID, ANN, [BOB], N_AT)]
        base, facts = gc.load_base(self.root, self.pin, ops)
        self.assertTrue(overlay.apply(base, ops).errors[0].startswith("gmail.gmail_messages: INSERT of an existing"))
        tid = f"{CAT}/{tnum(N_AT)}"
        found = self.found([thread(tid, CAT), message(CAT, P_RFC, tid, ANN, [BOB], "2024-03-01T10:00:00Z",
                                                      subject="Plan", body="The plan.\r\nRead it.")])
        self.assertIn(("G3", "WARN"), {(f.rule, f.severity) for f in found})      # a new copy of a base message

    def test_g4_copies(self):
        self.assertEqual(self.rules(new_mail(drop=(CAT,))), ["G4"])
        self.assertEqual(self.rules(new_mail(**{CAT: {"subject": "Kickoff!"}})), ["G4"])
        tid = f"{BOB}/{tnum(N_AT, 9)}"
        stray = [thread(f"{ANN}/{tnum(N_AT)}", ANN), message(ANN, "<s@x.co>", f"{ANN}/{tnum(N_AT)}", BOB, [CAT],
                                                              N_AT, labels=["INBOX"]),
                 thread(tid, BOB), message(BOB, "<s@x.co>", tid, BOB, [CAT], N_AT),
                 thread(f"{CAT}/{tnum(N_AT, 3)}", CAT), message(CAT, "<s@x.co>", f"{CAT}/{tnum(N_AT, 3)}", BOB,
                                                                 [CAT], N_AT)]
        self.assertEqual(self.rules(stray), ["G4"])                                 # Ann is no participant
        invite = [thread(f"{BOB}/{tnum(N_AT)}", BOB),
                  message(BOB, "<calendar-1@google.com>", f"{BOB}/{tnum(N_AT)}", ANN, [BOB, CAT], N_AT)]
        self.assertEqual(self.rules(invite), [])                                    # one invitation per invitee

    def test_g5_labels(self):
        self.assertEqual(self.rules(new_mail(**{ANN: {"label_ids_json": '["INBOX"]'}})), ["G5"])
        self.assertEqual(self.rules(new_mail(**{BOB: {"label_ids_json": '["SENT", "INBOX"]'}})), ["G5"])
        self.assertEqual(self.rules(new_mail(**{BOB: {"label_ids_json": '["IMPORTANT"]'}}), "WARN"), ["G5"])

    def test_g6_replies(self):
        r_at = "2024-03-02T08:00:00Z"
        good = [message(BOB, "<r@mail.gmail.com>", TB_ID, BOB, [ANN], r_at, subject="Re: Plan", irt=P_RFC,
                        refs=P_RFC),
                message(ANN, "<r@mail.gmail.com>", TA_ID, BOB, [ANN], r_at, subject="Re: Plan", irt=P_RFC,
                        refs=P_RFC)]
        self.assertEqual([f for f in self.found(good) if f.rule != "G8"], [])
        tid = f"{ANN}/{tnum(r_at)}"
        moved = good[:1] + [thread(tid, ANN, "Kickoff is Monday. Bring notes."),
                            message(ANN, "<r@mail.gmail.com>", tid, BOB, [ANN], r_at, subject="Re: Plan",
                                    irt=P_RFC, refs=P_RFC)]
        self.assertEqual(self.rules(moved), ["G6"])                                 # same subject, other thread
        renamed = [message(BOB, "<r@mail.gmail.com>", TB_ID, BOB, [ANN], r_at, subject="New topic", irt=P_RFC,
                           refs=P_RFC)] + [moved[1], message(ANN, "<r@mail.gmail.com>", tid, BOB, [ANN], r_at,
                                                             subject="New topic", irt=P_RFC, refs=P_RFC)]
        found = self.found(renamed)
        self.assertEqual(sorted({f.rule for f in found if f.severity == "FAIL"}), [])
        self.assertIn(("G6", "WARN"), {(f.rule, f.severity) for f in found})        # no Re:
        early = [message(BOB, "<r@mail.gmail.com>", TB_ID, BOB, [ANN], "2024-02-28T08:00:00Z", subject="Re: Plan",
                         irt=P_RFC, refs=P_RFC)]
        self.assertIn("G6", self.rules(early))
        orphan = [thread(f"{BOB}/{tnum(r_at)}", BOB),
                  message(BOB, "<r@mail.gmail.com>", f"{BOB}/{tnum(r_at)}", BOB, [CAT], r_at, irt="<gone@x.co>")]
        self.assertEqual(self.rules(orphan), ["G4", "G6"])

    def test_g7_dates(self):
        at = "2024-04-01T00:00:00Z"
        late = [thread(f"{BOB}/{tnum(at)}", BOB), message(BOB, "<z@x.co>", f"{BOB}/{tnum(at)}", BOB, [DAN], at)]
        self.assertEqual(self.rules(late), ["G7"])
        far = [thread(f"{BOB}/{tnum('2024-03-11T12:00:00Z')}", BOB),
               message(BOB, "<z@x.co>", f"{BOB}/{tnum('2024-03-11T12:00:00Z')}", BOB, [DAN], N_AT)]
        self.assertEqual(self.rules(far, "WARN"), ["G7"])

    def test_g8_thread_snippets(self):
        ops = new_mail()
        ops[2] = thread(ops[2].col("id"), BOB, "something else")
        self.assertEqual(self.rules(ops, "WARN"), ["G8"])
        r_at = "2024-03-02T08:00:00Z"
        reply = message(ANN, "<r@mail.gmail.com>", TA_ID, BOB, [ANN], r_at, subject="Re: Plan", irt=P_RFC,
                        refs=P_RFC, body="ok")
        bob_copy = message(BOB, "<r@mail.gmail.com>", TB_ID, BOB, [ANN], r_at, subject="Re: Plan", irt=P_RFC,
                           refs=P_RFC, body="ok")
        self.assertEqual(self.rules([reply, bob_copy, snippet_update(TA_ID, "ok")], "WARN"), [])
        self.assertEqual(self.rules([reply, bob_copy], "WARN"), ["G8"])            # Ann's thread keeps a stale one
        self.assertEqual(self.rules([reply, bob_copy, snippet_update(TA_ID, "ok"), snippet_update(TB_ID, "ok")],
                                    "WARN"), ["G8"])                                # Bob's newest is base (Mar 5)

    def test_g9_snippet(self):
        self.assertEqual(self.rules(new_mail(**{b: {"snippet": "Bring notes."} for b in (ANN, BOB, CAT)})), ["G9"])

    def test_g10_headers(self):
        bad = json.dumps([{"name": "Subject", "value": "Other"}, {"name": "Message-ID", "value": N_RFC}])
        self.assertEqual(self.rules(new_mail(**{BOB: {"headers_json": bad}})), ["G10"])
        no_cc = json.dumps([{"name": n, "value": v} for n, v in (("Message-ID", N_RFC), ("Subject", "Kickoff"),
                            ("Date", "Sun, 10 Mar 2024 12:00:00 +0000"), ("From", form(ANN)), ("To", form(BOB)))])
        found = self.found(new_mail(**{BOB: {"headers_json": no_cc}}))
        self.assertEqual({(f.rule, f.severity) for f in found}, {("G10", "WARN")})

    def test_g11_address_forms(self):
        self.assertEqual(self.rules(new_mail(**{b: {"from_name": "Ann Smith"} for b in (ANN, BOB, CAT)}), "WARN"),
                         ["G11"])
        upper = {b: {"to_json": json.dumps(["bob <Bob@harmonygames.co>"])} for b in (ANN, BOB, CAT)}
        self.assertIn("G11", self.rules(new_mail(**upper)))
        ghost = {b: {"cc_json": json.dumps(["Cat Lee <cat@harmonygames.co>", "eve <eve@harmonygames.co>"])}
                 for b in (ANN, BOB, CAT)}
        self.assertIn("G11", self.rules(new_mail(**ghost), "WARN"))

    def test_g12_line_breaks(self):
        lf = {b: {"body_text": "Kickoff is Monday.\nBring notes."} for b in (ANN, BOB, CAT)}
        self.assertEqual(self.rules(new_mail(**lf), "WARN"), ["G12"])


ARCHIVE = TA / "support" / "completed_tasks"
UNIVERSES = {
    "normal": (TA.parent / "Universe_Normal" / "Normal_HarmonyGames_Gmail" / "Services_Data" / "gmail",
               "2026-02-14T00:00:00Z"),
    "synthcut": (TA.parent / "Universe_SynthCut" / "SynthCut_HarmonyGames_Gmail" / "Services_Data" / "gmail",
                 "2025-10-01T00:00:00Z"),
}
# task -> (universe, FAIL rules, WARN rules) of its Gmail rows. One accepted task fails G4: samuel's
# <CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com> names oliver.brooks and owen.baker, whose mailboxes exist,
# without giving them a copy. The rule is the brief's (WS9 3e); the platform does not test it and base breaks it in
# 6,814 of 9,723 internal messages, so this FAIL is a stricter-than-platform rule, not a platform defect.
ACCEPTED = {
    "claire_zm3d_halloween_art_plan_2026-11-10": ("synthcut", set(), {"G12"}),
    "douglas_beta_server_signoff_2026-10-28": ("synthcut", set(), {"G11", "G12"}),
    "frederick_account_handover_2026-10-26": ("synthcut", set(), {"G11", "G12"}),
    "frederick_bridge_pipeline_2026-11-03": ("synthcut", set(), {"G11"}),
    "frederick_card_spend_q3_6ad83eebbd6456fd065bbd20": ("synthcut", set(), {"G6", "G8", "G10", "G11"}),
    "frederick_q4_commitments_2026-11-05": ("synthcut", set(), {"G11"}),
    "julia_zm3d_beta_calendar_2026-11-07": ("synthcut", set(), {"G12"}),
    "julia_zm_difficulty_baseline_2026-11-01": ("synthcut", set(), {"G6", "G11", "G12"}),
    "leonard_stockholder_closeout_2026-11-10": ("normal", set(), {"G6"}),
    "owen_dd_bug_carryover_2026-11-09": ("normal", set(), {"G7", "G11"}),
    "robert_llc_takeover_2026-11-06": ("normal", set(), set()),
    "robert_seed_bets_2026-11-11": ("normal", set(), set()),
    "robert_winddown_closeout_2026-10-30": ("normal", set(), set()),
    "samuel_zm_beta_messages_2026-11-09": ("synthcut", {"G4"}, {"G10", "G11"}),
    "vincent_zm3d_release_gate_2026-11-06": ("synthcut", set(), {"G11", "G12"}),
}


class AcceptedSqlTest(unittest.TestCase):
    """Gmail rows that passed the platform's /injection review, parsed back with the eval tokenizer and checked."""

    def test_every_archived_task(self):
        from generators.validate import parse_back
        for task, (universe, fails, warns) in sorted(ACCEPTED.items()):
            with self.subTest(task=task):
                sql = ARCHIVE / task / "task_inputs" / "01_Universe_Inject.sql"
                root, freeze = UNIVERSES[universe]
                if not sql.is_file() or not (root / "source_manifest.json").is_file():
                    self.skipTest(f"{task} or the {universe} Gmail export is not installed")
                ops = [op for op in parse_back.parse_ops(sql.read_text(encoding="utf-8"),
                                                         schema_path=TA / "references" / "universe_schema_live.json")
                       if op.table.startswith("gmail.")]
                pin = hashlib.sha256((root / "source_manifest.json").read_bytes()).hexdigest()
                base, facts = gc.load_base(root, pin, ops)
                ov = overlay.apply(base, ops)
                self.assertEqual(ov.errors, [])
                found = gc.check_gmail(ov, base, facts, freeze_utc=freeze)
                self.assertEqual({f.rule for f in found if f.severity == "FAIL"}, fails)
                self.assertEqual({f.rule for f in found if f.severity == "WARN"}, warns)


if __name__ == "__main__":
    unittest.main()

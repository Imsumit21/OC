"""The throwaway V3 task of task_fixture.py (synth-cut, persona Julia Lawson) with a Gmail spec.

The spec reads the real synth-cut Gmail export (its source_manifest.json pinned by sha256) and covers every Gmail case:
a new internal thread with a cc (three mailbox copies each) and a reply in it, a mail from an outside sender (one copy),
a reply under an existing base message held in three mailboxes (it joins each mailbox's own thread and updates their
snippets), per-copy labels with a Date offset, and a two-row haystack.

Base facts used (synth-cut export hg4-synth-sep30cut v16):
  julia.lawson, robert, brian.foster, leonard.hayes, arthur.blake @harmonygames.co   mailboxes in users.json
  base display names: 'julia', 'robert', 'Brian Foster', 'leonard hayes', 'arthur blake'
  BASE_PARENT  leonard's "Fwd: Great News from ..." of 2025-09-18 14:15:33Z to arthur and robert; one copy each in
               robert/1843611512336713741, arthur.blake/1843611512947708254 and leonard.hayes/1843611181307573177
               (leonard's thread also holds a 14:10:29Z message; nothing later in any of the three)
"""
from __future__ import annotations

import hashlib

from generators.tests.fixtures.task_fixture import TA, Fixture, lit, ref

GMAIL_DIR = TA.parent / "Universe_SynthCut" / "SynthCut_HarmonyGames_Gmail" / "Services_Data" / "gmail"
JULIA, ROBERT, BRIAN = "julia <julia.lawson@harmonygames.co>", "robert <robert@harmonygames.co>", \
    "Brian Foster <brian.foster@harmonygames.co>"
LEONARD, ARTHUR = "leonard hayes <leonard.hayes@harmonygames.co>", "arthur blake <arthur.blake@harmonygames.co>"
OUTSIDER = "Priya Raman <priya@pixelharbor.example>"
BASE_PARENT_RFC = "<CAPBs_a5MsPnj8B9Jv+DwmvAwxn4CSuG14CQ5AW2VbFU8v7VXjA@mail.gmail.com>"
BASE_PARENT = f"robert@harmonygames.co/{BASE_PARENT_RFC}"
BASE_THREADS = {"robert@harmonygames.co": "robert@harmonygames.co/1843611512336713741",
                "arthur.blake@harmonygames.co": "arthur.blake@harmonygames.co/1843611512947708254",
                "leonard.hayes@harmonygames.co": "leonard.hayes@harmonygames.co/1843611181307573177"}


def gbase(collection: str, record: str, field: str = "id") -> dict:
    return {"origin": "base", "construction": "reference",
            "base": {"service": "gmail", "collection": collection, "record": record, "field": "/" + field}}


def gmail_pin() -> dict:
    return {"file": "source_manifest.json",
            "sha256": hashlib.sha256((GMAIL_DIR / "source_manifest.json").read_bytes()).hexdigest()}


class GmailFixture(Fixture):
    def default_spec(self) -> dict:
        uni = self.ctx["universe"]

        def msg(key, sender, to, at, body, **extra):
            fields = {"from": lit(sender), "to": lit(to), "at": lit(at), "body": self.text(f"{key}.txt", body)}
            fields.update(extra)
            return {"key": key, "kind": "gmail.message", "fields": fields}

        hs = [(ROBERT, "2025-09-24T15:00:00Z", "Weekly numbers", "Numbers for the week are in the usual sheet."),
              (BRIAN, "2025-09-25T09:30:00Z", "Build notes", "Build 412 is up on TestFlight.\nNothing blocking.")]
        rows = []
        for n, (who, at, subject, body) in enumerate(hs, 1):
            pin = self.text(f"HS1_{n}.txt", body)
            rows.append({"from": who, "at": at, "subject": subject, "text": pin["text"], "sha256": pin["sha256"]})
        records = [
            msg("N1", JULIA, [ROBERT], "2025-09-29T16:00:00Z",
                "Robert,\n\nThe Q4 audience refresh goes to Solsten on Friday.\nBrian has the build list.\n\nJulia",
                subject=lit("Q4 audience refresh"), cc=lit([BRIAN])),
            dict(msg("N2", ROBERT, [JULIA], "2025-09-29T17:30:00Z", "Fine by me. Keep the Friday date.",
                     parent=ref("N1"), cc=lit([BRIAN])), role="deciding", manifest=["R1"]),
            msg("N3", OUTSIDER, [JULIA], "2025-09-26T13:05:00Z", "Hi Julia, the playable cut is attached in our "
                "portal. Let me know if the end card works.", subject=lit("Playable cut v3")),
            msg("B1", ROBERT, [LEONARD, ARTHUR], "2025-09-18T16:00:00Z",
                "Good news. Let's mention it in the board update.", parent=gbase("messages", BASE_PARENT)),
            msg("L1", JULIA, [BRIAN], "2025-09-30T07:45:00Z", "Brian, can you send the build list tonight?",
                subject=lit("Build list"), date_offset=lit("+0300"),
                labels=lit({"brian.foster@harmonygames.co": ["INBOX", "IMPORTANT", "CATEGORY_PERSONAL", "UNREAD"]})),
            {"key": "HS1", "kind": "gmail.haystack", "role": "haystack", "fields": {"to": lit([JULIA])},
             "rows": rows},
        ]
        return {
            "spec_version": "hg-gen/1",
            "task": {"slug": "gen-fixture", "revision": "rev1", "universe": uni["key"],
                     "freeze_utc": self.ctx["freeze_utc"], "clock_utc": uni["clock_utc"],
                     "context_hash": self.ctx["context_hash"]},
            "library": {"emitters": {"gmail": "gmail/1.0"}},
            "snapshot": {"gmail": gmail_pin()},
            "records": records,
        }

    def write(self, raw: bytes | None = None):
        """As Fixture.write, and the text files haystack rows name are written too."""
        import json
        used = {v["text"].split("/", 1)[1] for r in self.doc["records"] for v in r["fields"].values()
                if isinstance(v, dict) and "text" in v}
        used |= {row["text"].split("/", 1)[1] for r in self.doc["records"] for row in r.get("rows", ())
                 if isinstance(row, dict) and isinstance(row.get("text"), str) and "/" in row["text"]}
        for p in (self.spec_dir / "texts").iterdir():
            if p.name not in used:
                p.unlink()
        for name, data in self.texts.items():
            if name in used:
                (self.spec_dir / "texts" / name).write_bytes(data)
        path = self.spec_dir / "spec.json"
        path.write_bytes(raw if raw is not None else
                         (json.dumps(self.doc, indent=1, ensure_ascii=False) + "\n").encode("utf-8"))
        return self.task

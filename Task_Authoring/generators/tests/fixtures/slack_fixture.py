"""The throwaway V3 task of task_fixture.py (synth-cut, persona Julia Lawson) with a Slack spec.

The spec reads the real synth-cut Slack export (its source_manifest.json pinned by sha256) and covers every Slack record
kind: a new thread with two replies, a reply under a base post that had none, a reply into a base thread, a DM with a
reply, a group-DM post, a rejoin after a base leave followed by a post, a first-time join (an unverified convention,
so it carries an override), a leave, and a three-row haystack.

Base facts used (synth-cut export hg4-synth-sep30cut v16):
  EMPLOYEE_0005_SLACK_ID   Julia Lawson
  C09ATAJ220H  zm-animations, private, Julia is a member
      1759183318.447139    a post by EMPLOYEE_0006 without replies
      1759256190.810199    a thread by EMPLOYEE_0016: 9 replies by 2 users, newest 1759271121.716799
  D05SD5QLG94  a DM of Julia and EMPLOYEE_0008;  C51199DFF013  a group DM of Julia, EMPLOYEE_0012, EMPLOYEE_0038
  C05GU3E4SJY  private; Julia joined 2023-07-17 and left 2025-07-15T06:47:14Z (1752562034.110679)
  C05URGU759U  leapblock, private, 8 members, Julia was never in it
  C09A7PDFYCV  zombie-sfx, public; Julia joined 2025-08-13 and last posted 2025-08-18
"""
from __future__ import annotations

import hashlib

from generators.tests.fixtures.task_fixture import TA, Fixture, lit, ref

SLACK_DIR = TA.parent / "Universe_SynthCut" / "SynthCut_HarmonyGames_Other_Services" / "Services_Data" / "slack"
JULIA = "EMPLOYEE_0005_SLACK_ID"
ZM_ANIM, DM, GROUP_DM = "C09ATAJ220H", "D05SD5QLG94", "C51199DFF013"
SOLSTEN, LEAPBLOCK, ZOMBIE_SFX = "C05GU3E4SJY", "C05URGU759U", "C09A7PDFYCV"
BASE_POST, BASE_THREAD = "1759183318.447139", "1759256190.810199"
FIRST_JOIN_OVERRIDE = {"slack.membership.first_join": {
    "reason": "fixture exercises a first-time join", "platform_follow_up": "confirm the channel opens in the pre-check"}}


def sbase(collection: str, record: str, field: str = "id") -> dict:
    return {"origin": "base", "construction": "reference",
            "base": {"service": "slack", "collection": collection, "record": record, "field": "/" + field}}


def user(n: str) -> dict:
    return sbase("users", f"EMPLOYEE_{n}_SLACK_ID")


def channel(cid: str) -> dict:
    return sbase("channels", cid)


def slack_pin() -> dict:
    return {"file": "source_manifest.json",
            "sha256": hashlib.sha256((SLACK_DIR / "source_manifest.json").read_bytes()).hexdigest()}


class SlackFixture(Fixture):
    def default_spec(self) -> dict:
        uni = self.ctx["universe"]

        def msg(key, cid, who, at, body, **extra):
            fields = {"channel": channel(cid), "user": user(who), "at": lit(at),
                      "text": self.text(f"{key}.txt", body)}
            fields.update(extra)
            return {"key": key, "kind": "slack.message", "fields": fields}

        def event(key, kind, cid, at):
            return {"key": key, "kind": kind, "fields": {"channel": channel(cid), "user": user("0005"), "at": lit(at)}}

        hs = [("0002", "2025-09-26T16:02:00Z", "pushed the idle loop, have a look when you can"),
              ("0006", "2025-09-26T16:10:00Z", "looks good on my side"),
              ("0002", "2025-09-29T15:20:00Z", "export is in the shared folder")]
        rows = []
        for n, (who, at, body) in enumerate(hs, 1):
            pin = self.text(f"HS1_{n}.txt", body)
            rows.append({"user": f"EMPLOYEE_{who}_SLACK_ID", "at": at, "text": pin["text"], "sha256": pin["sha256"]})
        records = [
            msg("M1", ZM_ANIM, "0016", "2025-09-29T18:00:00Z", "Boss intro: which take are we shipping?"),
            msg("M2", ZM_ANIM, "0005", "2025-09-29T18:05:00Z", "Take 2, the one without the camera shake.",
                parent=ref("M1")),
            msg("M3", ZM_ANIM, "0016", "2025-09-29T18:07:00Z", "ok, take 2 it is", parent=ref("M1")),
            dict(msg("RB0", ZM_ANIM, "0005", "2025-09-30T17:05:00Z",
                     "One note here: the queue manager build is the one QA signs off.",
                     parent=sbase("messages", f"{ZM_ANIM}:{BASE_POST}")), role="deciding", manifest=["R1"]),
            msg("RB1", ZM_ANIM, "0006", "2025-09-30T23:10:00Z", "noted, will try a brighter aura tomorrow",
                parent=sbase("messages", f"{ZM_ANIM}:{BASE_THREAD}")),
            msg("DM1", DM, "0008", "2025-09-30T20:20:00Z", "Julia, do you have the asset list for PlayableX?"),
            msg("DM2", DM, "0005", "2025-09-30T20:24:00Z", "Yes, sending it over in a minute.", parent=ref("DM1")),
            msg("G1", GROUP_DM, "0012", "2025-09-30T15:30:00Z", "moving our sync to 4pm"),
            event("J1", "slack.channel_join", SOLSTEN, "2025-09-22T16:00:00Z"),
            msg("S1", SOLSTEN, "0005", "2025-09-22T16:02:00Z", "Back in here for the Q4 audience refresh."),
            event("F1", "slack.channel_first_join", LEAPBLOCK, "2025-09-26T15:00:00Z"),
            event("L1", "slack.channel_leave", ZOMBIE_SFX, "2025-09-25T17:00:00Z"),
            {"key": "HS1", "kind": "slack.haystack", "role": "haystack", "fields": {"channel": channel(ZM_ANIM)},
             "rows": rows},
        ]
        return {
            "spec_version": "hg-gen/1",
            "task": {"slug": "gen-fixture", "revision": "rev1", "universe": uni["key"],
                     "freeze_utc": self.ctx["freeze_utc"], "clock_utc": uni["clock_utc"],
                     "context_hash": self.ctx["context_hash"]},
            "library": {"emitters": {"slack": "slack/1.0"}},
            "snapshot": {"slack": slack_pin()},
            "overrides": dict(FIRST_JOIN_OVERRIDE),
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

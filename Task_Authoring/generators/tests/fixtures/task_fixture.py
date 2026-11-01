"""A throwaway V3 task (synth-cut universe, persona Julia Lawson) with a small Linear spec, under support/scratch.

The spec reads the real synth-cut Linear export (pinned by its sha256) and covers every Linear record kind: a project,
a parent issue and its sub-issue, comments on a new issue and on base issue ENG-2366 (an updated_at follow-up), and a
team counter update (an unverified convention, so it carries an override).
"""
from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
from pathlib import Path

from generators.core import context

TA = Path(__file__).resolve().parents[3]
SCRATCH = TA / "support" / "scratch"
LINEAR_DIR = TA.parent / "Universe_SynthCut" / "SynthCut_HarmonyGames_Other_Services" / "Services_Data" / "linear"

ASSIGNMENT = """# Task Assigned Inputs — V3

## Platform assignment

```text
🏢 Business Function
Product

🧑 Persona
Julia Lawson
Role: Product Manager

🎯 Competency
Product Management

🛠️ Task Skill
Retrieval

📋 Task Type
long horizon

🎚️ Difficulty Mode
hard

📅 Universe Date
October 1, 2025 07:00
```

## Resolved authoring inputs

```text
spec_version:       V3
business_function:  Product
persona_name:       Julia Lawson
persona_role:       Product Manager
competency:         Product Management
task_skill:         Retrieval
task_type:          long-horizon
horizon:            Long Horizon
difficulty_mode:    hard
universe_date:      October 1, 2025 07:00
universe_date_key:  2025-10-01
freeze_utc:         2025-10-01T00:00:00Z
persona_key:        julia_lawson
email:              julia.lawson@harmonygames.co
department:         Product
```
"""

PROJECT_ID = "9d3f0a52-6c1e-4f57-9f0e-3a1c2b4d5e60"
UUID_NS = "6ba7b811-9dad-11d1-80b4-00c04fd430c8"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def base(collection: str, record: str, field: str) -> dict:
    return {"origin": "base", "construction": "reference",
            "base": {"service": "linear", "collection": collection, "record": record, "field": "/" + field}}


def lit(value, **extra) -> dict:
    return {"origin": "authored", "construction": "literal", "value": value, **extra}


def ref(target: str, **extra) -> dict:
    return {"origin": "authored", "construction": "reference", "ref": target, **extra}


def snapshot_pin() -> dict:
    manifest = json.loads((LINEAR_DIR / "source_manifest.json").read_text())
    entry = next(f for f in manifest["files"] if f["path"] == "data.json")
    return {"file": "data.json", "sha256": entry["sha256"]}


class Fixture:
    def __init__(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="gen_fixture_", dir=SCRATCH))
        self.task = self.root / "task"
        self.spec_dir = self.task / "Working_Files" / "spec"
        (self.spec_dir / "texts").mkdir(parents=True)
        (self.task / "00_Assigments.md").write_text(ASSIGNMENT, encoding="utf-8")
        self.ctx = context.recompute(self.task)
        self.texts = {}
        self.doc = self.default_spec()

    def cleanup(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def text(self, name: str, body: str, **extra) -> dict:
        data = body.encode("utf-8")
        self.texts[name] = data
        return {"origin": "authored", "construction": "literal", "text": f"texts/{name}", "sha256": sha256(data),
                **extra}

    def default_spec(self) -> dict:
        uni = self.ctx["universe"]
        records = [
            {"key": "PRJ", "kind": "linear.project", "role": "structural", "fields": {
                "id": lit(PROJECT_ID), "team": base("teams", "team_ENG", "id"), "name": lit("DD Q4 close-out"),
                "summary": lit(None), "description": self.text("PRJ.txt", "Q4 close-out work for DD.\nOne line per item."),
                "lead": base("users", "usr_63fffeb4fab5233e", "id"), "priority": lit(0), "state": lit(None),
                "labels": lit([]), "created_at": lit("2025-09-29T17:00:00Z")}},
            {"key": "I1", "kind": "linear.issue", "role": "deciding", "manifest": ["R1"], "fields": {
                "id": lit("ENG-2367"), "team": base("teams", "team_ENG", "id"), "title": lit("DD Q4 maintenance"),
                "state": lit("Todo"), "creator": base("issues", "ENG-2366", "creator_id"),
                "assignee": base("issues", "ENG-2366", "assignee_id"),
                "description": self.text("I1.txt", "Carry-overs from ENG-2366, one per ticket.",
                                         cites=["base:linear:issues/ENG-2366/id"]),
                "project": ref("PRJ"), "parent": lit(None), "priority": base("issues", "ENG-2366", "priority"),
                "labels": lit(["DD"]), "relations": lit([{"target": "ENG-2366", "type": "relates"}]),
                "created_at": lit("2025-09-29T17:20:00Z",
                                  after=["base:linear:issues/ENG-2366/created_at", "spec:PRJ/created_at"]),
                "started_at": lit(None), "completed_at": lit(None), "canceled_at": lit(None)}},
            {"key": "I2", "kind": "linear.issue", "fields": {
                "id": lit("ENG-2368"), "team": base("teams", "team_ENG", "id"), "title": lit("Final bill"),
                "state": lit("In Progress"), "creator": base("issues", "ENG-2366", "creator_id"),
                "assignee": base("issues", "ENG-2366", "assignee_id"), "description": lit(None),
                "project": ref("PRJ"), "parent": ref("I1"), "priority": lit(0), "labels": lit([]),
                "relations": lit([]), "created_at": lit("2025-09-29T18:00:00Z", after=["spec:I1/created_at"]),
                "started_at": lit("2025-09-30T09:00:00Z", after=["spec:I2/created_at"]),
                "completed_at": lit(None), "canceled_at": lit(None)}},
            {"key": "C1", "kind": "linear.comment", "fields": {
                "id": lit("0b8f7c1e-4a5d-5e2f-9a1b-2c3d4e5f6a7b"), "issue": ref("I1"),
                "author": base("users", "usr_cc3e90160f490686", "id"),
                "created_at": lit("2025-09-29T19:05:00Z", after=["spec:I1/created_at"]),
                "body": self.text("C1.txt", "Listed the it's-done items; the rest stay open.")}},
            {"key": "C2", "kind": "linear.comment", "fields": {
                "id": {"origin": "authored", "construction": "transform", "fn": "linear.comment_uuid/1",
                       "inputs": {"namespace": UUID_NS, "name": "fixture/C2"}},
                "issue": ref("I1"), "author": base("users", "usr_63fffeb4fab5233e", "id"),
                "created_at": lit("2025-09-30T10:00:00Z"), "body": self.text("C2.txt", "Bill for $1,250.00 is in.")}},
            {"key": "C3", "kind": "linear.comment", "fields": {
                "id": lit("5c6d7e8f-9a0b-5c1d-8e2f-3a4b5c6d7e8f"), "issue": base("issues", "ENG-2366", "id"),
                "author": base("users", "usr_63fffeb4fab5233e", "id"),
                "created_at": lit("2025-09-30T11:00:00Z", after=["base:linear:issues/ENG-2366/updated_at"]),
                "body": self.text("C3.txt", "Moved to ENG-2367.", cites=["spec:I1/id"])}},
            {"key": "T1", "kind": "linear.team_update", "fields": {
                "team": base("teams", "team_ENG", "id"),
                "issue_counter": {"origin": "authored", "construction": "transform", "fn": "linear.next_issue_number/1"}}},
        ]
        return {
            "spec_version": "hg-gen/1",
            "task": {"slug": "gen-fixture", "revision": "rev1", "universe": uni["key"],
                     "freeze_utc": self.ctx["freeze_utc"], "clock_utc": uni["clock_utc"],
                     "context_hash": self.ctx["context_hash"]},
            "library": {"emitters": {"linear": "linear/1.0"}},
            "snapshot": {"linear": snapshot_pin()},
            "overrides": {"linear.team.issue_counter": {
                "reason": "fixture exercises the counter", "platform_follow_up": "confirm issue_counter in Explorer"}},
            "records": records,
        }

    def record(self, key: str) -> dict:
        return next(r for r in self.doc["records"] if r["key"] == key)

    def write(self, raw: bytes | None = None) -> Path:
        """spec.json plus exactly the texts/ files the spec references (the loader refuses unreferenced ones)."""
        used = {v["text"].split("/", 1)[1] for r in self.doc["records"] for v in r["fields"].values()
                if isinstance(v, dict) and "text" in v}
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

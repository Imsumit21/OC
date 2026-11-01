"""Spec v1 loader: Working_Files/spec/spec.json plus texts/, strict and versioned (plan §3.2).

{
  "spec_version": "hg-gen/1",
  "task":     {"slug", "revision", "universe", "freeze_utc", "clock_utc", "context_hash"},
  "library":  {"emitters": {"linear": "linear/1.0"}},
  "snapshot": {"linear": {"file": "data.json", "sha256": "<64 hex>"}},
  "overrides": {"<convention id>": {"reason": "...", "platform_follow_up": "..."}},      optional
  "census":    {"<claim id>": {"file": "census/<name>.json", "sha256": "<64 hex>"}},       optional
  "records":  [{"key", "kind", "role"?, "manifest"?, "note"?, "fields": {"<field>": <value>}}]
}

Unknown keys, duplicate JSON keys, unknown kinds or fields, missing required fields and bare (provenance-less) values are
refused. JSON numbers with a fraction are read as decimal.Decimal, never float.
"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path

from ..core.values import SpecError, parse_value, read_confined
from ..services import registry

SPEC_VERSION = "hg-gen/1"
TOP_KEYS = {"spec_version", "task", "library", "snapshot", "overrides", "census", "records"}
TOP_REQUIRED = {"spec_version", "task", "library", "snapshot", "records"}
TASK_KEYS = {"slug", "revision", "universe", "freeze_utc", "clock_utc", "context_hash"}
RECORD_KEYS = {"key", "kind", "role", "manifest", "note", "fields"}
ROLE = re.compile(r"^[a-z][a-z0-9_]{0,39}$")      # the task's own vocabulary (deciding, control, settling …)
KEY = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")
SHA = re.compile(r"^[0-9a-f]{64}$")
CENSUS_PATH = re.compile(r"^census/[A-Za-z0-9._-]+\.json$")


@dataclass(frozen=True)
class Spec:
    dir: Path
    sha256: str
    task: dict
    emitters: dict
    snapshot: dict
    overrides: dict
    census: dict
    records: tuple                      # ({key, kind, service, role, manifest, note, fields: {name: Value}}, ...)
    root: Path | None = None            # the task folder every spec input must stay inside

    def services(self) -> list[str]:
        return sorted({r["service"] for r in self.records})


def _pairs(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise SpecError("spec.json", f"duplicate JSON key {k!r}")
        out[k] = v
    return out


def _keys(where: str, obj, allowed: set, required: set):
    if not isinstance(obj, dict):
        raise SpecError(where, "must be an object")
    unknown, missing = sorted(set(obj) - allowed), sorted(required - set(obj))
    if unknown:
        raise SpecError(where, f"unknown keys {unknown}")
    if missing:
        raise SpecError(where, f"missing keys {missing}")


def load_spec(spec_dir: Path, root: Path | None = None) -> Spec:
    """root: the task folder; when given, spec.json and every texts/ and census/ file must lie inside it with no
    symlink in any path component."""
    spec_dir = Path(spec_dir)
    path = spec_dir / "spec.json"
    if root is not None:
        raw = read_confined(root, path, "spec.json")
    else:
        if path.is_symlink() or not path.is_file():
            raise SpecError("spec.json", f"{path} must be a regular file")
        raw = path.read_bytes()
    try:
        doc = json.loads(raw.decode("utf-8", errors="strict"), object_pairs_hook=_pairs, parse_float=Decimal)
    except UnicodeDecodeError as exc:
        raise SpecError("spec.json", f"not strict UTF-8: {exc}") from None
    except json.JSONDecodeError as exc:
        raise SpecError("spec.json", f"not JSON: {exc}") from None
    _keys("spec", doc, TOP_KEYS, TOP_REQUIRED)
    if doc["spec_version"] != SPEC_VERSION:
        raise SpecError("spec_version", f"{doc['spec_version']!r} is not {SPEC_VERSION!r}")
    _keys("task", doc["task"], TASK_KEYS, TASK_KEYS)
    for k in TASK_KEYS:
        if not isinstance(doc["task"][k], str) or not doc["task"][k]:
            raise SpecError(f"task.{k}", "must be a non-empty string")
    _keys("library", doc["library"], {"emitters"}, {"emitters"})
    emitters = doc["library"]["emitters"]
    if not isinstance(emitters, dict) or not emitters:
        raise SpecError("library.emitters", "must pin at least one emitter version")
    for service, version in emitters.items():
        registry.emitter(service, version)
    snapshot = doc["snapshot"]
    if not isinstance(snapshot, dict):
        raise SpecError("snapshot", "must be an object")
    for service, pin in snapshot.items():
        _keys(f"snapshot.{service}", pin, {"file", "sha256"}, {"file", "sha256"})
        if not isinstance(pin["sha256"], str) or not SHA.match(pin["sha256"]):
            raise SpecError(f"snapshot.{service}.sha256", "must be 64 lower-case hex")
        if not isinstance(pin["file"], str) or not pin["file"] or ".." in Path(pin["file"]).parts \
                or Path(pin["file"]).is_absolute():
            raise SpecError(f"snapshot.{service}.file", "must be a relative path inside the service folder")
    overrides = doc.get("overrides", {})
    if not isinstance(overrides, dict):
        raise SpecError("overrides", "must be an object")
    for cid, ov in overrides.items():
        _keys(f"overrides.{cid}", ov, {"reason", "platform_follow_up"}, {"reason", "platform_follow_up"})
    census = doc.get("census", {})
    if not isinstance(census, dict):
        raise SpecError("census", "must be an object")
    owners = {}                                 # one census file per claim, so each is read once (the paths are ASCII)
    for claim, entry in census.items():
        _keys(f"census.{claim}", entry, {"file", "sha256"}, {"file", "sha256"})
        if not isinstance(entry["file"], str) or not CENSUS_PATH.match(entry["file"]):
            raise SpecError(f"census.{claim}.file", "must be census/<name>.json")
        if not isinstance(entry["sha256"], str) or not SHA.match(entry["sha256"]):
            raise SpecError(f"census.{claim}.sha256", "must be 64 lower-case hex")
        other = owners.setdefault(entry["file"].casefold(), claim)
        if other != claim:
            raise SpecError(f"census.{claim}.file", f"{entry['file']} is also the census file of claim {other!r} "
                                                    "(names compared without case); each claim has its own file")

    if not isinstance(doc["records"], list) or not doc["records"]:
        raise SpecError("records", "must be a non-empty list")
    records, seen = [], set()
    for n, rec in enumerate(doc["records"]):
        where = f"records[{n}]"
        _keys(where, rec, RECORD_KEYS, {"key", "kind", "fields"})
        key = rec["key"]
        if not isinstance(key, str) or not KEY.match(key):
            raise SpecError(f"{where}.key", f"record key {key!r} must match {KEY.pattern}")
        if key in seen:
            raise SpecError(key, "duplicate record key")
        seen.add(key)
        service, schema = registry.kind_schema(rec["kind"])
        if service not in emitters:
            raise SpecError(key, f"kind {rec['kind']} needs library.emitters.{service}")
        if service not in snapshot:
            raise SpecError(key, f"kind {rec['kind']} needs snapshot.{service}")
        role = rec.get("role")
        if role is not None and not (isinstance(role, str) and ROLE.match(role)):
            raise SpecError(f"{key}.role", f"role must match {ROLE.pattern}")
        manifest = rec.get("manifest", [])
        if not isinstance(manifest, list) or not all(isinstance(m, str) and m for m in manifest):
            raise SpecError(f"{key}.manifest", "must be a list of non-empty strings")
        if "note" in rec and not isinstance(rec["note"], str):
            raise SpecError(f"{key}.note", "must be a string")
        fields = rec["fields"]
        if not isinstance(fields, dict):
            raise SpecError(f"{key}.fields", "must be an object")
        unknown = sorted(set(fields) - schema["required"] - schema["optional"])
        missing = sorted(schema["required"] - set(fields))
        if unknown:
            raise SpecError(f"{key}.fields", f"unknown fields for {rec['kind']}: {unknown}")
        if missing:
            raise SpecError(f"{key}.fields", f"required fields missing for {rec['kind']}: {missing}")
        parsed = {name: parse_value(f"{key}.{name}", obj) for name, obj in fields.items()}
        records.append({"key": key, "kind": rec["kind"], "service": service, "role": role,
                        "manifest": tuple(manifest), "note": rec.get("note"), "fields": parsed})
    unused = sorted(set(emitters) - {r["service"] for r in records})
    if unused:
        raise SpecError("library.emitters", f"pinned emitters without records: {unused}")
    pins, spelled = {}, {}                      # one pin and one spelling per file, so each is read once
    for r in records:
        for name, v in r["fields"].items():
            if not v.text:
                continue
            first = spelled.setdefault(v.text.casefold(), v.text)
            if first != v.text:
                raise SpecError(f"{r['key']}.{name}", f"{v.text} and {first} name the same file on a case-insensitive "
                                                      "filesystem; spell it one way")
            if pins.setdefault(v.text, v.sha256) != v.sha256:
                raise SpecError(f"{r['key']}.{name}", f"{v.text} is pinned to two different sha256 values")
    texts_dir = spec_dir / "texts"
    if texts_dir.is_dir():                      # every file there is part of the spec: no unpinned leftovers
        stray = sorted(f"texts/{p.name}" for p in texts_dir.iterdir() if f"texts/{p.name}" not in pins)
        if stray:
            raise SpecError("texts", f"files no field pins (remove them or reference them): {stray[:10]}")
    return Spec(dir=spec_dir, sha256=hashlib.sha256(raw).hexdigest(), task=doc["task"], emitters=dict(emitters),
                snapshot=snapshot, overrides=overrides, census=census, records=tuple(records), root=root)

"""Pinned, read-only base snapshot.

A spec pins every base export it reads ("snapshot": {"linear": {"file": "data.json", "sha256": ...}}). On load the
file's bytes are hashed and must equal both the spec pin and the service's source_manifest.json entry, so a
base-derived value always means "this field of this record in this exact export".
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .values import SpecError, json_pointer

COLLECTION_KEYS = {  # collection -> key field inside the export
    ("linear", "issues"): "id", ("linear", "users"): "id", ("linear", "teams"): "id",
    ("linear", "projects"): "id", ("linear", "comments"): "id",
}


class BaseSnapshot:
    def __init__(self, service_paths: dict[str, Path], pins: dict):
        self.paths = service_paths
        self.pins = pins or {}
        self._docs: dict[str, dict] = {}
        self._index: dict[tuple, dict] = {}
        self.fingerprint: dict[str, dict] = {}
        self.read: dict[str, str] = {}          # absolute path -> sha256 of the bytes read (exports and manifests)

    def doc(self, service: str) -> dict:
        if service in self._docs:
            return self._docs[service]
        pin = self.pins.get(service)
        if not pin or set(pin) != {"file", "sha256"}:
            raise SpecError(f"snapshot.{service}", "the spec must pin {file, sha256} for every service it reads")
        root = self.paths.get(service)
        if root is None:
            raise SpecError(f"snapshot.{service}", "no source path for this service in the task context")
        path = (root / pin["file"]).resolve()
        if root.resolve() not in path.parents:
            raise SpecError(f"snapshot.{service}", f"file {pin['file']!r} escapes the service folder")
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        manifest_path = (root / "source_manifest.json").resolve()
        manifest_raw = manifest_path.read_bytes()
        manifest = json.loads(manifest_raw)
        listed = next((f.get("sha256") for f in manifest.get("files", []) if f.get("path") == pin["file"]), None)
        if digest != pin["sha256"]:
            raise SpecError(f"snapshot.{service}", f"{pin['file']} sha256 is {digest}; the spec pins {pin['sha256']}")
        if digest != listed:
            raise SpecError(f"snapshot.{service}", f"{pin['file']} sha256 {digest} differs from source_manifest.json "
                                                  f"({listed})")
        self._docs[service] = json.loads(data)
        self.fingerprint[service] = {"file": pin["file"], "sha256": digest, "manifest_entry_sha256": listed}
        self.read[str(path)] = digest
        self.read[str(manifest_path)] = hashlib.sha256(manifest_raw).hexdigest()
        return self._docs[service]

    def records(self, service: str, collection: str) -> dict:
        key = (service, collection)
        if key not in self._index:
            field = COLLECTION_KEYS.get(key)
            if field is None:
                raise SpecError(f"base.{service}.{collection}", "unsupported collection")
            rows = self.doc(service).get(collection)
            if not isinstance(rows, list):
                raise SpecError(f"base.{service}.{collection}", "collection missing from the export")
            self._index[key] = {r[field]: r for r in rows}
        return self._index[key]

    def get(self, service: str, collection: str, record: str) -> dict | None:
        return self.records(service, collection).get(record)

    def lookup(self, where: str, base: tuple):
        service, collection, record, pointer = base
        row = self.get(service, collection, record)
        if row is None:
            raise SpecError(where, f"base record {service}/{collection}/{record} not found in the pinned export")
        try:
            return json_pointer(row, pointer)
        except KeyError:
            raise SpecError(where, f"base record {service}/{collection}/{record} has no field {pointer}") from None

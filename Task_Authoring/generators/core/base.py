"""Pinned, read-only base snapshot.

A spec pins every base export it reads. Two forms, both {"file", "sha256"}:

  one-document services (Linear)        "snapshot": {"linear": {"file": "data.json", "sha256": ...}}
      the file's bytes are hashed and must equal both the spec pin and the service's source_manifest.json entry.

  many-file services (Slack, Gmail)     "snapshot": {"slack": {"file": "source_manifest.json", "sha256": ...}}
      the pin is the service's source manifest itself, which lists every export file with its sha256. Each file the
      build reads is hashed and must equal its manifest entry, so pinning the manifest pins the whole export without
      listing its thousands of files in the spec.

Either way a base-derived value always means "this field of this record in this exact export".

Collections (the `collection` and `record` of a base reference):
  linear   issues, users, teams, projects, comments       record = the row's id
  slack    users, channels                                record = the row's id
           messages                                       record = "<channel id>:<ts>" (one monthly shard is read:
                                                          messages/<channel>/<YYYY-MM of ts, UTC>.json)
  gmail    users (key emailAddress), labels (key id)      record = the row's key
           messages                                       record = "<mailbox>/<RFC Message-ID>" (the export's id)
           threads                                        record = "<mailbox>/<thread number>"
           addresses                                      record = an address as base writes it (lower-cased);
                                                          fields /address, /names, /form (core/gmail_index.py)
  Gmail messages and threads are found through an index of every threads/*.json file (scan(): each file is hashed
  against the pinned manifest as it is read; the fingerprint records the count and a hash of the listing, not each
  file). Only the thread files a value is read from are listed in files_read and re-checked before publishing.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from pathlib import Path

from .gmail_index import GmailIndex
from .values import SpecError, json_pointer

MANIFEST = "source_manifest.json"
COLLECTION_KEYS = {  # one-document services: collection -> key field inside the export
    ("linear", "issues"): "id", ("linear", "users"): "id", ("linear", "teams"): "id",
    ("linear", "projects"): "id", ("linear", "comments"): "id",
}
FILE_COLLECTIONS = {  # many-file services: collection -> (file inside the service folder, key field)
    ("slack", "users"): ("users.json", "id"),
    ("slack", "channels"): ("channels.json", "id"),
    ("gmail", "users"): ("users.json", "emailAddress"),
    ("gmail", "labels"): ("labels.json", "id"),
}
INDEXED_COLLECTIONS = {("gmail", "messages"), ("gmail", "threads"), ("gmail", "addresses")}
SLACK_CHANNEL = re.compile(r"^[A-Z0-9]{8,14}$", re.ASCII)
SLACK_TS = re.compile(r"^([0-9]{10})\.([0-9]{6})$", re.ASCII)


def slack_shard(channel: str, ts: str) -> str:
    """The export file that holds a channel's message with this ts: its UTC month (0 exceptions in 529,418 base
    rows of the synth-cut export and 585,555 of the normal one)."""
    m = SLACK_TS.match(ts)
    if not m or not SLACK_CHANNEL.match(channel):
        raise ValueError(f"not a Slack <channel>:<ts>: {channel}:{ts}")
    when = dt.datetime.fromtimestamp(int(m.group(1)), dt.timezone.utc)
    return f"messages/{channel}/{when:%Y-%m}.json"


class BaseSnapshot:
    def __init__(self, service_paths: dict[str, Path], pins: dict):
        self.paths = service_paths
        self.pins = pins or {}
        self._docs: dict[str, dict] = {}
        self._index: dict[tuple, dict] = {}
        self._files: dict[tuple, object] = {}       # (service, relative path) -> parsed JSON
        self.fingerprint: dict[str, dict] = {}
        self.read: dict[str, str] = {}          # absolute path -> sha256 of the bytes read (exports and manifests)

    # ---- pins
    def _pin(self, service: str) -> tuple[dict, Path]:
        pin = self.pins.get(service)
        if not pin or set(pin) != {"file", "sha256"}:
            raise SpecError(f"snapshot.{service}", "the spec must pin {file, sha256} for every service it reads")
        root = self.paths.get(service)
        if root is None:
            raise SpecError(f"snapshot.{service}", "no source path for this service in the task context")
        return pin, root

    def manifest_pinned(self, service: str) -> bool:
        return (self.pins.get(service) or {}).get("file") == MANIFEST

    def doc(self, service: str) -> dict:
        if service in self._docs:
            return self._docs[service]
        pin, root = self._pin(service)
        manifest_path = (root / MANIFEST).resolve()
        manifest_raw = manifest_path.read_bytes()
        manifest_sha = hashlib.sha256(manifest_raw).hexdigest()
        manifest = json.loads(manifest_raw)
        if pin["file"] == MANIFEST:                 # many-file service: the manifest is the pin
            if manifest_sha != pin["sha256"]:
                raise SpecError(f"snapshot.{service}", f"{MANIFEST} sha256 is {manifest_sha}; the spec pins "
                                                      f"{pin['sha256']}")
            listed = {f["path"]: f.get("sha256") for f in manifest.get("files", [])
                      if isinstance(f, dict) and isinstance(f.get("path"), str)}
            self._docs[service] = {"files": listed}
            self.fingerprint[service] = {"file": MANIFEST, "sha256": manifest_sha, "files_read": {}}
            self.read[str(manifest_path)] = manifest_sha
            return self._docs[service]
        path = (root / pin["file"]).resolve()
        if root.resolve() not in path.parents:
            raise SpecError(f"snapshot.{service}", f"file {pin['file']!r} escapes the service folder")
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        listed = next((f.get("sha256") for f in manifest.get("files", []) if f.get("path") == pin["file"]), None)
        if digest != pin["sha256"]:
            raise SpecError(f"snapshot.{service}", f"{pin['file']} sha256 is {digest}; the spec pins {pin['sha256']}")
        if digest != listed:
            raise SpecError(f"snapshot.{service}", f"{pin['file']} sha256 {digest} differs from source_manifest.json "
                                                  f"({listed})")
        self._docs[service] = json.loads(data)
        self.fingerprint[service] = {"file": pin["file"], "sha256": digest, "manifest_entry_sha256": listed}
        self.read[str(path)] = digest
        self.read[str(manifest_path)] = manifest_sha
        return self._docs[service]

    # ---- many-file services
    def _listed(self, service: str) -> dict:
        if not self.manifest_pinned(service):
            raise SpecError(f"snapshot.{service}", f"this service is read file by file: pin {MANIFEST} "
                                                  '({"file": "source_manifest.json", "sha256": ...})')
        return self.doc(service)["files"]

    def paths_under(self, service: str, prefix: str) -> list[str]:
        """Export files of a many-file service whose path starts with prefix, sorted (from the pinned manifest)."""
        return sorted(p for p in self._listed(service) if p.startswith(prefix))

    def has_file(self, service: str, rel: str) -> bool:
        return rel in self._listed(service)

    def file(self, service: str, rel: str):
        """The parsed JSON of one export file of a many-file service; its bytes must equal the manifest entry."""
        key = (service, rel)
        if key in self._files:
            return self._files[key]
        listed = self._listed(service).get(rel)
        if listed is None:
            raise SpecError(f"base.{service}", f"{rel} is not a file of the pinned export")
        root = self.paths[service]
        path = (root / rel).resolve()
        if root.resolve() not in path.parents:
            raise SpecError(f"base.{service}", f"file {rel!r} escapes the service folder")
        try:
            data = path.read_bytes()
        except OSError as exc:
            raise SpecError(f"base.{service}", f"cannot read {rel}: {exc}") from None
        digest = hashlib.sha256(data).hexdigest()
        if digest != listed:
            raise SpecError(f"base.{service}", f"{rel} sha256 {digest} differs from {MANIFEST} ({listed})")
        try:
            self._files[key] = json.loads(data)
        except ValueError as exc:
            raise SpecError(f"base.{service}", f"{rel} is not JSON: {exc}") from None
        self.fingerprint[service]["files_read"][rel] = digest
        self.read[str(path)] = digest
        return self._files[key]

    def scan(self, service: str, prefix: str, visit) -> int:
        """Read every export file of a many-file service whose path starts with prefix (sorted), check its bytes
        against the pinned manifest and call visit(rel, data). The fingerprint records how many files were read and
        a sha256 of their (path, sha256) listing; the files are not added to files_read (there may be 80,000)."""
        listed = self._listed(service)
        root = self.paths[service]
        rels = sorted(p for p in listed if p.startswith(prefix))
        for rel in rels:
            path = root / rel
            try:
                data = path.read_bytes()
            except OSError as exc:
                raise SpecError(f"base.{service}", f"cannot read {rel}: {exc}") from None
            if hashlib.sha256(data).hexdigest() != listed[rel]:
                raise SpecError(f"base.{service}", f"{rel} differs from {MANIFEST} (sha256)")
            visit(rel, data)
        self.note_scan(service, prefix, rels)
        return len(rels)

    def note_scan(self, service: str, prefix: str, rels: list) -> None:
        """Record a scan in the fingerprint: how many files, and a sha256 of their (path, sha256) listing. A scan this
        process made for an earlier build of the same export (same manifest, same file stats) is recorded the same
        way, so the build record does not depend on what else the process did."""
        listed = self._listed(service)
        listing = hashlib.sha256("".join(f"{r}\t{listed[r]}\n" for r in rels).encode("utf-8")).hexdigest()
        self.fingerprint[service].setdefault("scanned", {})[prefix] = {"files": len(rels), "listing_sha256": listing}

    def index(self, service: str):
        """The service's record index (Gmail: core/gmail_index.GmailIndex), built once per snapshot."""
        key = (service, "__index__")
        if key not in self._index:
            if service != "gmail":
                raise SpecError(f"base.{service}", "this service has no record index")
            self._index[key] = GmailIndex.of(self)
        return self._index[key]

    # ---- records
    def records(self, service: str, collection: str) -> dict:
        key = (service, collection)
        if key not in self._index:
            if key in FILE_COLLECTIONS:
                rel, field = FILE_COLLECTIONS[key]
                rows = self.file(service, rel)
            else:
                field = COLLECTION_KEYS.get(key)
                if field is None:
                    raise SpecError(f"base.{service}.{collection}", "unsupported collection")
                rows = self.doc(service).get(collection)
            if not isinstance(rows, list):
                raise SpecError(f"base.{service}.{collection}", "collection missing from the export")
            self._index[key] = {r[field]: r for r in rows if isinstance(r, dict) and field in r}
        return self._index[key]

    def get(self, service: str, collection: str, record: str) -> dict | None:
        if (service, collection) == ("slack", "messages"):
            channel, _, ts = record.partition(":")
            try:
                rel = slack_shard(channel, ts)
            except ValueError:
                raise SpecError("base.slack.messages", f"a message record is <channel id>:<ts>, got {record!r}") \
                    from None
            if not self.has_file("slack", rel):
                return None
            return next((m for m in self.file("slack", rel) if isinstance(m, dict) and m.get("ts") == ts), None)
        if (service, collection) in INDEXED_COLLECTIONS:
            return self.index(service).get(collection, record)
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

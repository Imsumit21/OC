"""The emitter's view of a Gmail export: which threads, Message-IDs and address forms base holds.

The export keeps one file per mailbox thread (threads/*.json: {"id": "<mailbox>/<number>", "user_email", "messages":
[{"id": "<mailbox>/<RFC Message-ID>", "from", "to", "cc", "bcc", "date", "subject", "labelIds", "headers", ...}]}).
A file's name does not say which thread it holds, so the index reads every thread file once (BaseSnapshot.scan, each
file checked against the pinned manifest) and keeps, without parsing JSON:
  threads    thread id -> (export file, mailbox)
  copies     RFC Message-ID -> [(mailbox, thread id)]           one entry per mailbox copy
  names      address (lower case) -> {display name: count}      over every from/to/cc/bcc entry ('' = bare address)
  spellings  address (lower case) -> {address as written: count}
Keys and values are read with one pattern over the file bytes: in a JSON file a key-value pair `"id": "..."` cannot
occur inside a string (its quotes would be escaped), so the match is exact.

A process that builds twice from the same export (the tests) reuses the index when the manifest sha256 and every
thread file's stat (size, mtime, inode) are unchanged (GmailIndex.reused; the fingerprint is the same either way).
"""
from __future__ import annotations

import email.utils
import hashlib
import json
import os
import re
from collections import Counter

from .values import SpecError

SERVICE = "gmail"
THREADS = "threads/"
_KV = re.compile(rb'"(id|user_email|from|to|cc|bcc)":\s*"((?:[^"\\]|\\.)*)"')
_SPECIALS = re.compile(r'[()<>@,;:\\".\[\]]')
_CACHE: dict[tuple, tuple] = {}                 # (root, manifest sha256) -> (stat signature, state)


def parse_entries(text: str) -> list[tuple[str, str]]:
    """(display name, address) of every entry of a From/To/Cc string, as email.utils reads them."""
    return [(name, addr) for name, addr in email.utils.getaddresses([text or ""]) if addr]


def address_form(name: str, addr: str) -> str:
    """How base writes an entry: 'name <addr>', '"name" <addr>' when the name holds a special, or the bare address."""
    if not name:
        return addr
    if _SPECIALS.search(name):
        return '"' + name.replace("\\", "\\\\").replace('"', '\\"') + f'" <{addr}>'
    return f"{name} <{addr}>"


def _signature(root, rels) -> str:
    h = hashlib.sha256()
    for rel in rels:
        st = os.stat(root / rel)
        h.update(f"{rel}\t{st.st_size}\t{st.st_mtime_ns}\t{st.st_ino}\n".encode("utf-8"))
    return h.hexdigest()


class GmailIndex:
    def __init__(self, base, state: dict):
        self.base = base
        self.threads: dict[str, tuple] = state["threads"]
        self.copies: dict[str, list] = state["copies"]
        self.names: dict[str, Counter] = state["names"]
        self.spellings: dict[str, Counter] = state["spellings"]
        self.reused = False                     # True: the scan an earlier build of this process made was reused

    @classmethod
    def of(cls, base) -> "GmailIndex":
        root = base.paths[SERVICE]
        rels = base.paths_under(SERVICE, THREADS)
        manifest_sha = base.fingerprint[SERVICE]["sha256"]
        key = (str(root.resolve()), manifest_sha)
        signature = _signature(root, rels)
        cached = _CACHE.get(key)
        if cached is not None and cached[0] == signature:
            base.note_scan(SERVICE, THREADS, rels)
            index = cls(base, cached[1])
            index.reused = True
            return index
        state = {"threads": {}, "copies": {}, "names": {}, "spellings": {}}
        raw_entries: Counter = Counter()

        def visit(rel: str, data: bytes) -> None:
            tid = box = None
            for k, v in _KV.findall(data):
                if k == b"id":
                    value = json.loads(b'"' + v + b'"')
                    if tid is None:
                        tid = value
                    else:
                        mailbox, _, rfc = value.partition("/")
                        state["copies"].setdefault(rfc, []).append((mailbox, tid))
                elif k == b"user_email":
                    if box is None:
                        box = json.loads(b'"' + v + b'"')
                else:
                    raw_entries[v] += 1
            if tid is None:
                raise SpecError(f"base.{SERVICE}", f"{rel} holds no thread id")
            if tid in state["threads"]:
                raise SpecError(f"base.{SERVICE}", f"thread {tid} is in two files ({state['threads'][tid][0]}, {rel})")
            state["threads"][tid] = (rel, box)

        base.scan(SERVICE, THREADS, visit)
        for raw, n in raw_entries.items():
            for name, addr in parse_entries(json.loads(b'"' + raw + b'"')):
                state["names"].setdefault(addr.lower(), Counter())[name] += n
                state["spellings"].setdefault(addr.lower(), Counter())[addr] += n
        _CACHE[key] = (signature, state)
        return cls(base, state)

    # ---- lookups
    def thread(self, tid: str) -> dict | None:
        entry = self.threads.get(tid)
        return None if entry is None else self.base.file(SERVICE, entry[0])

    def message(self, mid: str) -> dict | None:
        mailbox, _, rfc = mid.partition("/")
        for box, tid in self.copies.get(rfc, ()):
            if box == mailbox:
                thread = self.thread(tid)
                return next((m for m in thread.get("messages") or () if m.get("id") == mid), None)
        return None

    def address(self, addr: str) -> dict | None:
        names = self.names.get(addr.lower())
        if not names:
            return None
        ranked = sorted(names, key=lambda n: (-names[n], n))
        best = next((n for n in ranked if n), "")
        if names.get("", 0) > names.get(best, 0):
            best = ""
        spelled = self.spellings[addr.lower()]
        written = sorted(spelled, key=lambda a: (-spelled[a], a))[0]
        return {"address": written, "names": ranked, "form": address_form(best, written)}

    def get(self, collection: str, record: str):
        if collection == "messages":
            return self.message(record)
        if collection == "threads":
            return self.thread(record)
        if collection == "addresses":
            return self.address(record)
        raise SpecError(f"base.{SERVICE}.{collection}", "unsupported collection")

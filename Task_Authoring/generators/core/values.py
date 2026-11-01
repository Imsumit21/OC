"""Spec values: every leaf value states its origin and its construction (plan §3.2).

origin        "base"     — read from a pinned base record (service, collection, record id, field pointer)
              "authored" — written by the task's author (inline literal or a texts/ file pinned by sha256)
construction  "literal"   — the value itself (authored only)
              "reference" — a base field, or another spec record (by key)
              "transform" — a registered, versioned function of named inputs (ids, time formats, counters)

There is no implicit mixing: an authored text that restates base facts lists them in `cites`, one that asserts the
status of a base entity lists it in `claims`, and a timestamp may declare the events it must follow in `after`.
"""
from __future__ import annotations

import hashlib
import os
import re
from dataclasses import dataclass, field
from pathlib import Path


class SpecError(Exception):
    def __init__(self, where: str, message: str):
        super().__init__(f"{where}: {message}")
        self.where = where


_KEYS = {"origin", "construction", "value", "text", "sha256", "base", "ref", "fn", "inputs", "after", "cites",
         "claims"}
_COMMON = {"origin", "construction", "after", "cites", "claims"}
_BASE_KEYS = {"service", "collection", "record", "field"}
_SHA = re.compile(r"^[0-9a-f]{64}$")
_TEXT_PATH = re.compile(r"^texts/[A-Za-z0-9._-]+\.txt$")


@dataclass(frozen=True)
class Value:
    where: str
    origin: str
    construction: str
    value: object = None
    text: str | None = None
    sha256: str | None = None
    base: tuple | None = None            # (service, collection, record, field)
    ref: str | None = None
    fn: str | None = None
    inputs: tuple = ()
    after: tuple = ()
    cites: tuple = ()
    claims: tuple = ()
    is_literal_value: bool = field(default=False)

    def provenance(self) -> dict:
        p = {"origin": self.origin, "construction": self.construction}
        if self.text:
            p.update(text=self.text, sha256=self.sha256)
        if self.base:
            p["base"] = dict(zip(("service", "collection", "record", "field"), self.base))
        if self.ref:
            p["ref"] = self.ref
        if self.fn:
            p.update(fn=self.fn, inputs=dict(self.inputs))
        for k in ("after", "cites", "claims"):
            if getattr(self, k):
                p[k] = list(getattr(self, k))
        return p


def parse_value(where: str, obj) -> Value:
    if not isinstance(obj, dict):
        raise SpecError(where, "a value must be an object with origin and construction (bare literals are refused)")
    unknown = set(obj) - _KEYS
    if unknown:
        raise SpecError(where, f"unknown value keys {sorted(unknown)}")
    origin, construction = obj.get("origin"), obj.get("construction")
    if origin not in ("base", "authored"):
        raise SpecError(where, f"origin must be 'base' or 'authored', got {origin!r}")
    if construction not in ("literal", "reference", "transform"):
        raise SpecError(where, f"construction must be literal, reference or transform, got {construction!r}")
    lists = {}
    for k in ("after", "cites", "claims"):
        v = obj.get(k, [])
        if not isinstance(v, list) or not all(isinstance(x, str) and x for x in v):
            raise SpecError(where, f"{k} must be a list of non-empty strings")
        lists[k] = tuple(v)
    if construction == "literal":
        form = "text" if "text" in obj else "value"
        allowed = {"text", "sha256"} if form == "text" else {"value"}
    elif construction == "reference":
        form, allowed = ("base reference", {"base"}) if origin == "base" else ("spec reference", {"ref"})
    else:
        form, allowed = "transform", {"fn", "inputs"}
    stray = sorted(set(obj) - _COMMON - allowed)
    if stray:
        raise SpecError(where, f"keys {stray} do not belong to a {origin} {form} value")
    if construction == "literal":
        if origin != "authored":
            raise SpecError(where, "a literal is always authored (base values are references)")
        has_value, has_text = "value" in obj, "text" in obj
        if has_value == has_text:
            raise SpecError(where, "an authored literal needs exactly one of value or text")
        if has_text:
            if not isinstance(obj["text"], str) or not _TEXT_PATH.match(obj["text"]):
                raise SpecError(where, "text must be texts/<name>.txt")
            if not isinstance(obj.get("sha256"), str) or not _SHA.match(obj["sha256"]):
                raise SpecError(where, "a text literal needs its sha256 (64 lower-case hex)")
            return Value(where, origin, construction, text=obj["text"], sha256=obj["sha256"], **lists)
        if "sha256" in obj:
            raise SpecError(where, "sha256 belongs to text literals only")
        return Value(where, origin, construction, value=obj["value"], is_literal_value=True, **lists)
    if construction == "reference":
        if origin == "base":
            b = obj.get("base")
            if not isinstance(b, dict) or set(b) != _BASE_KEYS or not all(isinstance(b[k], str) and b[k]
                                                                         for k in _BASE_KEYS):
                raise SpecError(where, f"a base reference needs base{{{', '.join(sorted(_BASE_KEYS))}}}")
            if not b["field"].startswith("/"):
                raise SpecError(where, "base.field is a JSON pointer starting with '/'")
            if "ref" in obj:
                raise SpecError(where, "a base reference cannot also be a spec reference")
            return Value(where, origin, construction,
                         base=(b["service"], b["collection"], b["record"], b["field"]), **lists)
        ref = obj.get("ref")
        if not isinstance(ref, str) or not ref:
            raise SpecError(where, "an authored reference needs ref: <record key>")
        return Value(where, origin, construction, ref=ref, **lists)
    fn, inputs = obj.get("fn"), obj.get("inputs", {})
    if not isinstance(fn, str) or "/" not in fn:
        raise SpecError(where, "a transform needs fn: '<name>/<version>'")
    if not isinstance(inputs, dict):
        raise SpecError(where, "transform inputs must be an object")
    return Value(where, origin, construction, fn=fn, inputs=tuple(sorted(inputs.items())), **lists)


def read_confined(root: Path, path: Path, where: str) -> bytes:
    """The bytes of a regular file inside root (the task folder), read by descriptor without following a symlink at
    any level (core/output.read_bytes)."""
    from .output import PublishError, read_bytes
    rel = os.path.relpath(os.path.abspath(path), os.path.abspath(root)).replace(os.sep, "/")
    try:
        data = read_bytes(root, rel)
    except PublishError as exc:
        raise SpecError(where, str(exc)) from None
    if data is None:
        raise SpecError(where, f"{rel} is not a file inside the task folder")
    return data


def read_text(spec_dir: Path, value: Value, root: Path | None = None) -> str:
    """Exact bytes of a texts/ file, strict UTF-8, no normalisation; sha256 checked on the bytes.

    With root (the task folder), every path component from root down must be a real directory or file."""
    path = Path(spec_dir) / value.text
    if root is not None:
        data = read_confined(root, path, value.where)
    else:
        if path.is_symlink() or not path.is_file():
            raise SpecError(value.where, f"text file must be a regular file inside spec/texts/: {value.text}")
        try:
            data = path.read_bytes()
        except OSError as exc:
            raise SpecError(value.where, f"cannot read {value.text}: {exc}") from exc
    digest = hashlib.sha256(data).hexdigest()
    if digest != value.sha256:
        raise SpecError(value.where, f"{value.text} sha256 is {digest}, spec pins {value.sha256}")
    try:
        return data.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise SpecError(value.where, f"{value.text} is not strict UTF-8: {exc}") from exc


def json_pointer(doc, pointer: str):
    cur = doc
    for raw in pointer.split("/")[1:]:
        part = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        elif isinstance(cur, list) and part.isdigit() and int(part) < len(cur):
            cur = cur[int(part)]
        else:
            raise KeyError(pointer)
    return cur

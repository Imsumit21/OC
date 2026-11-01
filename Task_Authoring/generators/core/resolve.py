"""Resolve spec values to Python values with their provenance, and check the declared dependencies.

Locators (used by `after` and `cites`):
  base:<service>:<collection>/<record id>/<field>      a field of a record in the pinned base export
  spec:<record key>/<field>                            another spec record's field
A `ref` names another spec record's field as "<record key>/<field>" ("<record key>" alone means its id). A reference
may only point at an authored value: a base value is cited from the base, never laundered through another record.
"""
from __future__ import annotations

import copy
import datetime as dt
import re
from decimal import Decimal

from .values import SpecError, read_text

_BASE_LOC = re.compile(r"^base:([a-z]+):([a-z_]+)/([^/]+)/(.+)$")
_SPEC_LOC = re.compile(r"^spec:([^/]+)/(.+)$")
_INSTANT = re.compile(r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d{1,6})?(Z|[+-]\d{2}:\d{2}))?$", re.ASCII)
SCALARS = (type(None), bool, int, Decimal, str)


def parse_instant(value, where: str) -> dt.datetime:
    if not isinstance(value, str) or not _INSTANT.match(value):
        raise SpecError(where, f"{value!r} is not an ISO-8601 UTC instant or date")
    if len(value) == 10:
        return dt.datetime.fromisoformat(value).replace(tzinfo=dt.timezone.utc)
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(dt.timezone.utc)


def _check_type(where: str, value):
    if isinstance(value, str):
        try:
            value.encode("utf-8")
        except UnicodeEncodeError:
            raise SpecError(where, "text holds a lone surrogate (a \\ud800-\\udfff escape); UTF-8 cannot store it") \
                from None
        return
    if isinstance(value, SCALARS):
        return
    if isinstance(value, list):
        for i, v in enumerate(value):
            _check_type(f"{where}[{i}]", v)
        return
    if isinstance(value, dict):
        for k, v in value.items():
            _check_type(f"{where} key", k)
            _check_type(f"{where}.{k}", v)
        return
    raise SpecError(where, f"unsupported value type {type(value).__name__}")


class Resolver:
    def __init__(self, spec, base, transforms: dict):
        self.spec, self.base, self.transforms = spec, base, transforms
        self.records = {r["key"]: r for r in spec.records}
        self.cache: dict[tuple, tuple] = {}
        self.stack: list[tuple] = []
        self.after_checks: list[dict] = []
        self.cite_checks: list[dict] = []
        self.texts: dict[str, str] = {}             # texts/<file> -> sha256
        self.text_values: dict[str, str] = {}       # texts/<file> -> its decoded text

    def __call__(self, rec: dict, name: str):
        return self.resolve(rec["key"], name)

    def computed(self, rec: dict, name: str, fn: str) -> dict:
        """A field the emitter computes from the post-state (e.g. linear.next_issue_number/1): the spec may only
        declare it, as an authored transform without inputs, after, cites or claims. Returns its provenance."""
        where = f"{rec['key']}.{name}"
        v = rec["fields"].get(name)
        if v is None:
            raise SpecError(where, "required field missing")
        if not (v.origin == "authored" and v.construction == "transform" and v.fn == fn):
            raise SpecError(where, f"must be the authored transform {fn}")
        if v.inputs or v.after or v.cites or v.claims:
            raise SpecError(where, f"{fn} is computed by the emitter; inputs, after, cites and claims do not apply")
        return v.provenance()

    def locate(self, where: str, loc: str):
        """Value of a locator, and its own provenance."""
        m = _BASE_LOC.match(loc)
        if m:
            service, collection, record, field = m.groups()
            pointer = "/" + field
            value = self.base.lookup(where, (service, collection, record, pointer))
            return value, {"origin": "base", "construction": "reference",
                           "base": {"service": service, "collection": collection, "record": record, "field": pointer}}
        m = _SPEC_LOC.match(loc)
        if m:
            key, field = m.groups()
            if key not in self.records or field not in self.records[key]["fields"]:
                raise SpecError(where, f"locator {loc} names no spec field")
            return self.resolve(key, field)
        raise SpecError(where, f"locator {loc!r} is neither base:<service>:<collection>/<id>/<field> nor "
                               "spec:<key>/<field>")

    def resolve(self, key: str, name: str):
        ck = (key, name)
        if ck in self.cache:
            return self.cache[ck]
        if ck in self.stack:
            cycle = " -> ".join(f"{k}/{n}" for k, n in self.stack + [ck])
            raise SpecError(f"{key}.{name}", f"reference cycle {cycle}")
        rec = self.records.get(key)
        if rec is None or name not in rec["fields"]:
            raise SpecError(f"{key}.{name}", "no such spec field")
        v = rec["fields"][name]
        where = f"{key}.{name}"
        self.stack.append(ck)
        try:
            value, prov = self._value(v, where)
            _check_type(where, value)
            for event in v.after:
                event_value, _ = self.locate(where, event)
                if event_value is None:
                    raise SpecError(where, f"after {event}: the event has no time (null)")
                if not parse_instant(value, where) > parse_instant(event_value, f"{where} after {event}"):
                    raise SpecError(where, f"{value} is not after {event} ({event_value})")
                self.after_checks.append({"field": where, "value": value, "after": event, "event": event_value})
            for cite in v.cites:
                cited, _ = self.locate(where, cite)
                if not isinstance(value, str) or cited is None or str(cited) not in value:
                    raise SpecError(where, f"cites {cite} but its value {cited!r} does not occur verbatim in the text")
                self.cite_checks.append({"field": where, "cite": cite, "value": str(cited)})
        finally:
            self.stack.pop()
        self.cache[ck] = (value, prov)
        return value, prov

    def _value(self, v, where: str):
        prov = v.provenance()
        if v.construction == "literal":
            if v.text:
                if v.text not in self.text_values:          # each file is read once per build (one pin per path)
                    self.text_values[v.text] = read_text(self.spec.dir, v, self.spec.root)
                    self.texts[v.text] = v.sha256
                return self.text_values[v.text], prov
            return copy.deepcopy(v.value), prov
        if v.construction == "reference":
            if v.origin == "base":
                value = self.base.lookup(where, v.base)
                prov["base"]["snapshot_sha256"] = self.base.fingerprint[v.base[0]]["sha256"]
                return copy.deepcopy(value), prov
            key, _, field = v.ref.partition("/")
            field = field or "id"
            target = self.records.get(key)
            if target is None or field not in target["fields"]:
                raise SpecError(where, f"ref {v.ref!r} names no spec field")
            tv = target["fields"][field]
            if tv.origin != "authored":
                raise SpecError(where, f"ref {v.ref!r} points at a base value; cite the base record directly")
            if tv.construction == "transform" and self.transforms.get(tv.fn, 1) is None:
                raise SpecError(where, f"ref {v.ref!r} points at {tv.fn}, which the emitter computes")
            value, target_prov = self.resolve(key, field)
            prov["target"] = target_prov
            return copy.deepcopy(value), prov
        if v.origin == "base":
            raise SpecError(where, "transforms over base values are not supported in spec v1")
        if v.fn not in self.transforms:
            raise SpecError(where, f"unknown transform {v.fn!r} (registered: {sorted(self.transforms)})")
        fn = self.transforms[v.fn]
        if fn is None:
            raise SpecError(where, f"{v.fn} is computed by the emitter from the post-state; it cannot be resolved "
                                   "on its own")
        try:
            return fn(dict(v.inputs)), prov
        except (ValueError, TypeError, KeyError) as exc:
            raise SpecError(where, f"{v.fn}: {exc}") from None

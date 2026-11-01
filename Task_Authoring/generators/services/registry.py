"""Service emitters, their record kinds, transforms and the conventions they rely on.

A spec pins the emitter version of every service it uses ({"linear": "linear/1.0"}); a different installed version
stops the render. Convention-bearing behaviour is listed in conventions/conventions.json with a status:
  base-verified      held on a base sample (exceptions listed in the evidence)
  platform-verified  a cited platform report or run-time trajectory shows it
  unverified         usable only with a spec override that states the reason and the platform follow-up
Each emitter declares the convention ids it uses (CONVENTIONS); tests/test_registry.py keeps the code constants and the
JSON values equal.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from ..core.values import SpecError
from . import linear

CONVENTIONS_PATH = Path(__file__).resolve().parents[1] / "conventions" / "conventions.json"
STATUSES = ("base-verified", "platform-verified", "unverified")

EMITTERS = {linear.SERVICE: linear}


def emitter(service: str, pinned: str):
    mod = EMITTERS.get(service)
    if mod is None:
        raise SpecError(f"library.emitters.{service}", f"no emitter for service {service!r} "
                                                       f"(available: {sorted(EMITTERS)})")
    if mod.VERSION != pinned:
        raise SpecError(f"library.emitters.{service}", f"spec pins {pinned!r}, the installed emitter is {mod.VERSION!r}")
    return mod


def kind_schema(kind: str) -> tuple[str, dict]:
    service = kind.split(".", 1)[0]
    mod = EMITTERS.get(service)
    if mod is None or kind not in mod.KINDS:
        known = sorted(k for m in EMITTERS.values() for k in m.KINDS)
        raise SpecError(f"kind {kind}", f"unknown record kind (known: {known})")
    return service, mod.KINDS[kind]


def transforms() -> dict:
    out = {}
    for mod in EMITTERS.values():
        out.update(mod.TRANSFORMS)
    return out


def load_conventions(path: Path = CONVENTIONS_PATH) -> tuple[dict, str]:
    data = path.read_bytes()
    doc = json.loads(data)
    if doc.get("format") != "hg-gen-conventions/1":
        raise SpecError("conventions", f"unknown format {doc.get('format')!r}")
    for cid, entry in doc["conventions"].items():
        if entry.get("status") not in STATUSES:
            raise SpecError(f"conventions.{cid}", f"status must be one of {STATUSES}")
        if not entry.get("evidence") and entry["status"] != "unverified":
            raise SpecError(f"conventions.{cid}", "a verified convention needs evidence")
    return doc["conventions"], hashlib.sha256(data).hexdigest()


def conventions_used(kinds_used: set[str], conventions: dict, overrides: dict) -> list[dict]:
    """The conventions a render relies on, with status; an unverified one needs a spec override with a reason.

    An emitter's CONVENTIONS maps convention id -> the record kinds that rely on it (empty: every render of that
    service)."""
    used = []
    services = {k.split(".", 1)[0] for k in kinds_used}
    for service in sorted(services):
        for cid, needed_by in EMITTERS[service].CONVENTIONS.items():
            if needed_by and not (set(needed_by) & kinds_used):
                continue
            entry = conventions.get(cid)
            if entry is None:
                raise SpecError(f"conventions.{cid}", "used by the emitter but missing from conventions.json")
            rec = {"id": cid, "status": entry["status"]}
            if entry["status"] == "unverified":
                ov = overrides.get(cid)
                if not isinstance(ov, dict) or not ov.get("reason") or not ov.get("platform_follow_up"):
                    raise SpecError(f"conventions.{cid}", "unverified convention: the spec needs overrides."
                                                          f"{cid} with reason and platform_follow_up")
                rec["override"] = {"reason": ov["reason"], "platform_follow_up": ov["platform_follow_up"]}
            used.append(rec)
    unknown = sorted(set(overrides) - {u["id"] for u in used if "override" in u})
    if unknown:
        raise SpecError("overrides", f"overrides that match no unverified convention this render uses: {unknown}")
    return used

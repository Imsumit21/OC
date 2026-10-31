#!/usr/bin/env python3
"""Normalize platform-pasted V3 assignments without guessing display timezones.

python3 Task_Authoring/tools/task_context.py --task-dir Task_Authoring/task_inputs --write
Add --require-source before grounding. Both assigned dates can use the same
registered universe data. The assignment freeze controls task facts independently
from the archive's clock metadata.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

BUNDLE = Path(__file__).resolve().parent.parent
WORKSPACE = BUNDLE.parent
DEFAULT_TASK = BUNDLE / "task_inputs"
POLICY_PATH = BUNDLE / "references" / "v3_policy.json"
SOURCES_PATH = BUNDLE / "references" / "universe_sources.json"
ROSTER_PATH = WORKSPACE / "Evals" / "references" / "persona" / "roster.json"
SERVICES = ("slack", "gmail", "gcal", "gdrive", "gdocs", "gsheets", "gslides",
            "github", "linear", "trello", "contacts", "confluence", "snowflake")
ALIASES = {
    "business_function": "business_function", "persona": "persona_name",
    "persona_name": "persona_name", "role": "persona_role", "persona_role": "persona_role",
    "competency": "competency", "task_skill": "task_skill", "task_type": "task_type",
    "horizon": "task_type", "difficulty_mode": "difficulty_mode", "universe_date": "universe_date_raw",
}
REQUIRED = ("business_function", "persona_name", "persona_role", "competency",
            "task_skill", "task_type", "difficulty_mode", "universe_date_raw")


class ContextError(ValueError):
    pass


def digest(value) -> str:
    raw = value if isinstance(value, bytes) else json.dumps(value, sort_keys=True, ensure_ascii=False,
                                                          separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def _json(path):
    try:
        return json.loads(Path(path).read_text())
    except (OSError, ValueError) as exc:
        raise ContextError(f"Cannot read {path}: {exc}") from exc


def _key(value):
    return re.sub(r"[^a-z0-9]+", "_", value.casefold()).strip("_")


def _plain(value):
    return " ".join(str(value).split())


def _type(value):
    v = _key(value)
    if v in ("normal", "normal_horizon"):
        return "normal"
    if v in ("long", "long_horizon"):
        return "long-horizon"
    raise ContextError(f"Unsupported task type {value!r}; Super-Long-Horizon remains paused")


def is_v3_assignment(text):
    return bool(re.search(r"^\s*spec_version:\s*V3\s*$", text, re.M | re.I)
                or re.search(r"difficulty[_ ]mode", text, re.I))


def parse_assignment(text):
    """Read UI labels plus legacy mirror keys and reject conflicting duplicates."""
    found, metadata, pending = {}, {}, None
    for number, raw in enumerate(text.splitlines(), 1):
        if re.match(r"^\s*(?:[-*+]\s|>\s|\|)", raw):
            continue
        line = raw.strip().strip("*").strip()
        if not line or line.startswith("```"):
            continue
        prefix = _key(line.split(":", 1)[0])
        if pending and prefix not in ALIASES:
            field, value, pending = pending, line, None
        elif ":" in line:
            label, value = line.split(":", 1)
            key = _key(label)
            if key in ALIASES:
                field = ALIASES[key]
            elif key in ("persona_key", "email", "department", "freeze_utc", "universe_date_key", "spec_version"):
                if not value.strip() or re.fullmatch(r"\[.*\]", value.strip()):
                    continue
                if key in metadata and metadata[key].casefold() != value.strip().casefold():
                    raise ContextError(f"Conflicting {key} at line {number}")
                metadata[key] = value.strip()
                continue
            else:
                pending = None
                continue
        elif _key(line) in ALIASES:
            pending = ALIASES[_key(line)]
            continue
        elif pending:
            field, value, pending = pending, line, None
        else:
            continue
        value = _plain(value)
        if not value or re.fullmatch(r"\[.*\]", value):
            continue
        normalized = _type(value) if field == "task_type" else value.casefold()
        if field in found and found[field][1] != normalized:
            raise ContextError(f"Conflicting {field} at line {number}: {found[field][0]!r} versus {value!r}")
        found.setdefault(field, (value, normalized))
        pending = None
    missing = [k for k in REQUIRED if k not in found]
    if missing:
        raise ContextError("Missing V3 assigned fields: " + ", ".join(missing))
    out = {k: v[0] for k, v in found.items()}
    out["task_type"] = _type(out["task_type"])
    out["difficulty_mode"] = out["difficulty_mode"].casefold()
    out["horizon"] = "Long Horizon" if out["task_type"] == "long-horizon" else "Normal Horizon"
    return out, metadata


def _date_key(display):
    # The time is preserved, not converted. V3 defines the two assignment dates.
    match = re.match(r"^(\d{4}-\d{2}-\d{2})(?:\b|T)", display)
    if match:
        return match.group(1)
    for fmt in ("%B %d, %Y", "%b %d, %Y"):
        match = re.match(r"^([A-Za-z]+\s+\d{1,2},\s*\d{4})(?:\s|$)", display)
        if match:
            try:
                return dt.datetime.strptime(match.group(1), fmt).date().isoformat()
            except ValueError:
                pass
    raise ContextError(f"Unsupported universe date display {display!r}; preserve the platform value")


def _path(value):
    p = Path(value)
    return p.resolve() if p.is_absolute() else (WORKSPACE / p).resolve()


def source_context(date, freeze, registry_path=SOURCES_PATH):
    registry = _json(registry_path)
    entry = registry.get("sources", {}).get(date)
    out = {"status": "unavailable", "reason": "", "manifest": None, "kb_path": None,
           "paths": {}, "fingerprint": digest({"registry": registry, "date": date})}
    if not entry:
        out["reason"] = f"No universe source is configured for {date} in {registry_path}."
        return out
    try:
        mode = entry.get("mode", "snapshot")
        if mode not in ("snapshot", "shared-universe") or not entry.get("verification_basis"):
            raise ContextError("Source requires a supported mode and a verification_basis")
        if mode == "snapshot" and not entry.get("historical_state_verified"):
            raise ContextError("Snapshot mode requires historical_state_verified; shared data uses shared-universe mode")
        manifest_path = _path(entry["manifest"])
        if WORKSPACE not in manifest_path.parents:
            raise ContextError("Source manifest must be inside the workspace for the bounded search helpers")
        manifest = _json(manifest_path)
        raw_clock = str(manifest.get("evaluation_clock", "")).replace("Z", "+00:00")
        # Per-universe manifests state the clock as "2026-02-14 00:00 UTC" or
        # "2025-10-01 07:00 UTC (2025-10-01 00:00 PT)". Drop the parenthetical gloss and
        # map a trailing UTC to an offset; bare "YYYY-MM-DD HH:MM" still parses unchanged.
        iso_clock = re.sub(r"\s*\([^)]*\)\s*$", "", raw_clock).strip()
        iso_clock = re.sub(r"\s*UTC$", "+00:00", iso_clock)
        clock = dt.datetime.fromisoformat(iso_clock)
        clock = clock.replace(tzinfo=dt.timezone.utc) if clock.tzinfo is None else clock.astimezone(dt.timezone.utc)
        data_clock = clock.isoformat().replace("+00:00", "Z")
        if mode == "snapshot" and data_clock != freeze:
            raise ContextError(f"Source clock {raw_clock!r} does not match assigned freeze {freeze}")
        if mode == "shared-universe" and clock < dt.datetime.fromisoformat(freeze.replace("Z", "+00:00")):
            raise ContextError(f"Shared source metadata ends at {data_clock}, before the assigned freeze {freeze}")
        paths = {s: _path(manifest["services"][s]["path"]) for s in SERVICES}
        outside = [s for s, p in paths.items() if WORKSPACE not in p.parents]
        if outside:
            raise ContextError("Source service directories must be inside the workspace: " + ", ".join(outside))
        other = paths["slack"].parent
        if any(paths[s].parent != other for s in SERVICES if s not in ("github", "gmail")):
            raise ContextError("Non-GitHub/Gmail services must share one Services_Data parent")
        absent = [s for s, p in paths.items() if not p.is_dir()]
        if absent:
            raise ContextError("Source service directories missing: " + ", ".join(absent))
        # Bind cheap source manifests rather than reading multi-GB source bodies.
        fingerprints = {}
        for service, folder in paths.items():
            sp = folder / "source_manifest.json"
            fingerprints[service] = digest(sp.read_bytes()) if sp.is_file() else None
        kb_path = _path(entry["kb_path"])
        kb_output_path = _path(entry.get("kb_output_path", entry["kb_path"]))
        if BUNDLE not in kb_path.parents or BUNDLE not in kb_output_path.parents:
            raise ContextError("Derived KB output must stay inside Task_Authoring")
        out.update(status="ready", mode=mode, data_clock=data_clock, assigned_freeze=freeze,
                   reason=("Shared universe registered; verify task evidence against the assigned freeze" if mode == "shared-universe"
                           else "Source manifest matches the assigned historical freeze"),
                   manifest=str(manifest_path), kb_path=str(kb_path), kb_output_path=str(kb_output_path),
                   paths={k: str(v) for k, v in paths.items()},
                   fingerprint=digest({"manifest_path": str(manifest_path), "manifest": manifest, "sources": fingerprints}))
    except (ContextError, KeyError, TypeError, ValueError, OSError) as exc:
        out.update(status="invalid", reason=str(exc))
    return out


def load_context(task_dir=DEFAULT_TASK, require_source=False, *, policy_path=POLICY_PATH,
                 registry_path=SOURCES_PATH, roster_path=ROSTER_PATH):
    task_dir = Path(task_dir).resolve()
    try:
        raw = (task_dir / "00_Assigments.md").read_bytes()
        assigned, mirror = parse_assignment(raw.decode("utf-8"))
    except (OSError, UnicodeError) as exc:
        raise ContextError(f"Cannot read assignment in {task_dir}: {exc}") from exc
    policy = _json(policy_path)
    if mirror.get("spec_version", "V3").upper() != "V3":
        raise ContextError("This loader requires a V3 assignment; use explicit legacy tooling for V2")
    mode = assigned["difficulty_mode"]
    if mode not in policy["difficulty_caps"]:
        raise ContextError(f"Unsupported assigned difficulty mode {mode!r}")
    date = _date_key(assigned["universe_date_raw"])
    if date not in policy["freeze_dates"]:
        raise ContextError(f"Universe date {date} is not one of the V3 assigned dates")
    freeze = policy["freeze_dates"][date]
    people = _json(roster_path)
    if isinstance(people, dict):
        people = people.get("personas", people.get("people", []))
    matches = [p for p in people if _plain(p.get("name", "")).casefold() == assigned["persona_name"].casefold()]
    if len(matches) != 1:
        raise ContextError(f"Assigned persona {assigned['persona_name']!r} resolves to {len(matches)} authorized roster entries")
    person = matches[0]
    if _plain(person["role"]).casefold() != assigned["persona_role"].casefold():
        raise ContextError(f"Assigned role {assigned['persona_role']!r} disagrees with roster role {person['role']!r}; do not substitute it")
    derived = {k: person[k] for k in ("persona_key", "email", "department")}
    for key, expected in {**derived, "freeze_utc": freeze, "universe_date_key": date}.items():
        if mirror.get(key) and mirror[key].casefold() != str(expected).casefold():
            raise ContextError(f"Stale assignment mirror {key}: {mirror[key]!r}; expected {expected!r}")
    source = source_context(date, freeze, registry_path)
    out = {"spec_version": "V3", **assigned, **derived, "universe_date_key": date,
           "freeze_utc": freeze, "freeze_basis": "V3 assigned-date mapping; platform display time retained without timezone inference",
           "difficulty_cap": policy["difficulty_caps"][mode], "baseline_model": policy["model"],
           "human_timezone": policy["human_timezone"], "policy_version": policy["policy_version"],
           "assignment_hash": digest(raw), "policy_hash": digest(policy), "roster_hash": digest(people),
           "source": source}
    out["context_hash"] = digest(out)
    if require_source and source["status"] != "ready":
        raise ContextError(source["reason"])
    return out


def date_acceptance(utc_value, prompt_timezone=None):
    """Human display and fair date variants; no exact-time requirement is inferred."""
    when = dt.datetime.fromisoformat(utc_value.replace("Z", "+00:00"))
    if when.tzinfo is None:
        raise ContextError("Source date must include its timezone")
    utc = when.astimezone(dt.timezone.utc).date().isoformat()
    pacific = when.astimezone(ZoneInfo("America/Los_Angeles")).date().isoformat()
    accepted = sorted({utc, pacific})
    if prompt_timezone:
        zone = "America/Los_Angeles" if prompt_timezone in ("Pacific", "PT", "PST", "PDT") else prompt_timezone
        accepted = [when.astimezone(ZoneInfo(zone)).date().isoformat()]
    return {"pacific": pacific, "utc": utc, "accepted_dates": accepted,
            "display": pacific + " PT" + (f" ({utc} UTC)" if utc != pacific else "")}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--task-dir", type=Path, default=Path(os.environ.get("TASK_AUTHORING_TASK_DIR", DEFAULT_TASK)))
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--require-source", action="store_true")
    args = ap.parse_args(argv)
    try:
        context = load_context(args.task_dir)
        if args.write:
            out = args.task_dir / "Working_Files" / "00_Task_Context.json"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(context, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps(context, ensure_ascii=False, indent=2))
        if args.require_source and context["source"]["status"] != "ready":
            print("SOURCE BLOCKED: " + context["source"]["reason"], file=sys.stderr)
            return 1
        return 0
    except ContextError as exc:
        print("ASSIGNMENT FAIL: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Normalize platform-pasted V3 assignments without guessing display timezones.

python3 Task_Authoring/tools/task_context.py --task-dir Task_Authoring/task_inputs --write
Add --require-source before grounding. The assigned universe date selects one of
the two Evals universes; there is no default. The assignment freeze is the seed
bound and the universe clock is the data horizon.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from zoneinfo import ZoneInfo

BUNDLE = Path(__file__).resolve().parent.parent
WORKSPACE = BUNDLE.parent
DEFAULT_TASK = BUNDLE / "task_inputs"
POLICY_PATH = BUNDLE / "references" / "v3_policy.json"
SOURCES_PATH = BUNDLE / "references" / "universe_sources.json"
ROSTER_PATH = WORKSPACE / "Evals" / "references" / "persona" / "roster.json"
UNIVERSE_TOOL = WORKSPACE / "Evals" / "tools" / "hg_universe.py"
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


# Workspace folders authoring may read but never write (GEN_EXECUTION § 1).
READ_ONLY_ROOTS = ("Evals", "claude", "Universe_Normal", "Universe_SynthCut",
                   "HarmonyGames_GitHub", "HarmonyGames_Gmail", "HarmonyGames_Other_Services")


def v2_export_root(name, workspace=WORKSPACE) -> Path:
    """Data root for archived V2 fixtures (--legacy-v2 / --self-test, no task context): the old root export
    `HarmonyGames_<name>` while it exists, else the same Feb 14, 2026 data in its V3 home,
    `Universe_Normal/Normal_HarmonyGames_<name>`. A task context always replaces these roots."""
    old = Path(workspace) / f"HarmonyGames_{name}"
    return old if old.is_dir() else Path(workspace) / "Universe_Normal" / f"Normal_HarmonyGames_{name}"


def within(path, root) -> bool:
    """True when `path` is `root` or lies under it, compared by file identity.

    Identity (not string prefixes) keeps case variants on a case-insensitive filesystem and
    symlinked components from slipping past the check.
    """
    root = Path(root)
    if not root.exists():
        return False
    try:
        target = Path(path).resolve()
    except (OSError, RuntimeError):
        return False
    for candidate in (target, *target.parents):
        try:
            if candidate.exists() and os.path.samefile(candidate, root):
                return True
        except OSError:
            continue
    # A hard link elsewhere still names a file under root: compare inodes (only multi-link files need the walk).
    try:
        if target.is_file() and target.stat().st_nlink > 1:
            for folder, _, names in os.walk(root):
                for name in names:
                    try:
                        if os.path.samefile(os.path.join(folder, name), target):
                            return True
                    except OSError:
                        continue
    except OSError:
        return False
    return False


def read_only_root(path):
    """The read-only workspace folder `path` resolves into, or None."""
    return next((name for name in READ_ONLY_ROOTS if within(path, WORKSPACE / name)), None)


def refuse_read_only(path, what):
    name = read_only_root(path)
    if name:
        raise ContextError(f"{what} resolves into read-only {name}/ ({path}); authoring never writes there")


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
        if not line:
            continue
        if line.startswith("```") or (pending and line.startswith("#") and _key(line) not in ALIASES):
            pending = None  # a fence or heading ends a label left without its value: that field stays missing
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


def _universe_module():
    """Load Evals/tools/hg_universe.py without writing bytecode into Evals/."""
    if not UNIVERSE_TOOL.is_file():
        raise ContextError("Evals/tools/hg_universe.py not found — install the dual-universe Evals bundle")
    spec = importlib.util.spec_from_file_location("_task_context_hg_universe", UNIVERSE_TOOL)
    if spec is None or spec.loader is None:
        raise ContextError("Evals/tools/hg_universe.py cannot be loaded as a module")
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def _utc_text(value):
    when = value if value.tzinfo else value.replace(tzinfo=dt.timezone.utc)
    return when.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def universe_key(date, module=None):
    """The unique bundled universe whose date equals the assignment date."""
    module = module or _universe_module()
    matches = [key for key, entry in module.UNIVERSES.items() if entry["date"] == date]
    if len(matches) != 1:
        raise ContextError(f"Universe date {date} selects {len(matches)} bundled universes in Evals/tools/hg_universe.py")
    return matches[0]


def universe_block(key, module=None):
    """The task universe, read from Evals/tools/hg_universe.py only."""
    module = module or _universe_module()
    entry = module.UNIVERSES[key]
    clock = entry["clock"] if entry["clock"].tzinfo else entry["clock"].replace(tzinfo=dt.timezone.utc)
    return {"key": key, "date": entry["date"], "label": entry["label"],
            "folder": entry["folder"], "prefix": entry["prefix"],
            "clock_utc": _utc_text(clock), "clock_text": entry["clock_text"],
            "clock_line": module.report_line(key),
            "shutdown_rules_apply": bool(entry["shutdown_rules"]),
            "persona_today": entry["date"],
            "persona_today_weekday": clock.astimezone(dt.timezone.utc).strftime("%A"),
            "build_label": entry["source"]}


def _kb_binding(entry, key, clock, fingerprint):
    """Per-universe KB: bound only on matching provenance, else the legacy reference view."""
    legacy_value = entry["legacy_kb_path"] if "legacy_kb_path" in entry else entry.get("kb_path")
    legacy = _path(legacy_value) if legacy_value else None
    output_value = entry.get("kb_output_path") or legacy_value
    output = _path(output_value) if output_value else None
    for path in (output, legacy):
        if path is not None and BUNDLE not in path.parents:
            raise ContextError("Derived KB output must stay inside Task_Authoring")
    out = {"kb_output_path": str(output) if output else None, "kb_status": "unavailable", "kb_path": None}
    timeline = output / "timeline.json" if output else None
    meta = {}
    if timeline is not None and timeline.is_file():
        try:
            meta = (_json(timeline) or {}).get("_meta") or {}
        except ContextError:
            meta = {}
    if (meta.get("universe") == key and str(meta.get("clock")) == clock
            and meta.get("source_fingerprint") == fingerprint and meta.get("build") == "per-universe-v1"):
        return {**out, "kb_status": "bound", "kb_path": str(output)}
    if legacy is not None:
        return {**out, "kb_status": "reference-only", "kb_path": str(legacy)}
    return out


def source_context(date, freeze, registry_path=SOURCES_PATH, *, module=None):
    """Validate the registered source for one assigned date.

    Universe identity (folder, prefix, clock, label) comes from
    Evals/tools/hg_universe.py; the manifest's `evaluation_clock` is
    human-readable text and is never parsed.
    """
    registry = _json(registry_path)
    module = module or _universe_module()
    key = universe_key(date, module)
    info = module.UNIVERSES[key]
    out = {"status": "unavailable", "reason": "", "mode": None, "universe": key, "manifest": None,
           "paths": {}, "fingerprint": digest({"registry": registry, "date": date}),
           "data_clock": _utc_text(info["clock"]), "assigned_freeze": freeze,
           "kb_status": "unavailable", "kb_path": None, "kb_output_path": None}
    entry = registry.get("sources", {}).get(date)
    if not entry:
        out["reason"] = f"No universe source is configured for {date} in {registry_path}."
        return out
    try:
        mode = entry.get("mode", "snapshot")
        out["mode"] = mode
        if mode == "shared-universe":
            raise ContextError("Mode shared-universe is retired by Evals dual-universe-v1; "
                               "update references/universe_sources.json")
        if mode not in ("snapshot", "universe") or not entry.get("verification_basis"):
            raise ContextError("Source requires a supported mode and a verification_basis")
        if mode == "snapshot" and not entry.get("historical_state_verified"):
            raise ContextError("Snapshot mode requires historical_state_verified; the Evals bundle selects a universe by date")
        manifest_path = _path(entry["manifest"])
        if WORKSPACE not in manifest_path.parents:
            raise ContextError("Source manifest must be inside the workspace for the bounded search helpers")
        manifest = _json(manifest_path)
        if mode == "universe":
            expected = module.manifest_path(WORKSPACE, key).resolve()
            if manifest_path != expected:
                raise ContextError(f"Universe source manifest must be hg_universe.manifest_path() "
                                   f"Evals/references/universes/{key}/universe_manifest.json, not {entry['manifest']}")
            if entry.get("universe") != key:
                raise ContextError(f"Registry universe {entry.get('universe')!r} does not match date {date} → {key!r}")
            if manifest.get("universe") != key:
                raise ContextError(f"Manifest declares universe {manifest.get('universe')!r}; date {date} selects {key!r}")
        paths = {s: _path(manifest["services"][s]["path"]) for s in SERVICES}
        if mode == "universe":
            for service, folder in paths.items():
                try:
                    rel = folder.relative_to(WORKSPACE)
                except ValueError:
                    raise ContextError("Source service directories must be inside the workspace: " + service) from None
                if (len(rel.parts) < 2 or rel.parts[0] != info["folder"]
                        or not rel.parts[1].startswith(info["prefix"] + "_HarmonyGames_")):
                    raise ContextError(f"Source service path for {service} must be in "
                                       f"{info['folder']}/{info['prefix']}_HarmonyGames_*: {rel}")
        outside = [s for s, p in paths.items() if WORKSPACE not in p.parents]
        if outside:
            raise ContextError("Source service directories must be inside the workspace: " + ", ".join(outside))
        other = paths["slack"].parent
        if any(paths[s].parent != other for s in SERVICES if s not in ("github", "gmail")):
            raise ContextError("Non-GitHub/Gmail services must share one Services_Data parent")
        absent = [s for s, p in paths.items() if not p.is_dir()]
        if absent:
            if mode == "universe":
                raise ContextError("Source service directories missing: " + ", ".join(absent)
                                   + f". Install {info['folder']}/ per Evals/UNIVERSE_MAP.md")
            raise ContextError("Source service directories missing: " + ", ".join(absent))
        if mode == "universe":
            data_clock = _utc_text(info["clock"])
            if dt.datetime.fromisoformat(freeze.replace("Z", "+00:00")) > info["clock"]:
                raise ContextError(f"Assigned freeze {freeze} is after the {key} data clock {data_clock}")
        else:
            raw_clock = str(manifest.get("evaluation_clock", "")).replace("Z", "+00:00")
            clock = dt.datetime.fromisoformat(raw_clock)
            clock = clock.replace(tzinfo=dt.timezone.utc) if clock.tzinfo is None else clock.astimezone(dt.timezone.utc)
            data_clock = _utc_text(clock)
            if data_clock != freeze:
                raise ContextError(f"Source clock {raw_clock!r} does not match assigned freeze {freeze}")
        # Bind cheap source manifests rather than reading multi-GB source bodies.
        fingerprints = {}
        for service, folder in paths.items():
            sp = folder / "source_manifest.json"
            fingerprints[service] = digest(sp.read_bytes()) if sp.is_file() else None
        # The registry's manifest entry (workspace-relative), not the resolved absolute path: the same installed data
        # gets the same fingerprint on every machine, so a committed per-universe KB stays bound after a clone.
        fingerprint = digest({"universe": key, "manifest_path": str(entry["manifest"]),
                              "manifest": manifest, "sources": fingerprints})
        kb = _kb_binding(entry, key, out["data_clock"], fingerprint)
        out.update(kb, status="ready", data_clock=data_clock, assigned_freeze=freeze,
                   reason=(f"Source manifest matches the {info['label']} universe ({data_clock})" if mode == "universe"
                           else "Source manifest matches the assigned historical freeze"),
                   manifest=str(manifest_path), fingerprint=fingerprint,
                   paths={k: str(v) for k, v in paths.items()})
    except (ContextError, KeyError, TypeError, ValueError, OSError) as exc:
        out.update(status="invalid", reason=str(exc))
        try:
            out.update(_kb_binding(entry, key, out["data_clock"], out["fingerprint"]))
        except ContextError:
            out.update(kb_status="unavailable", kb_path=None)
    return out


def load_context(task_dir=DEFAULT_TASK, require_source=False, *, policy_path=POLICY_PATH,
                 registry_path=SOURCES_PATH, roster_path=ROSTER_PATH):
    refuse_read_only(task_dir, "The task directory")
    task_dir = Path(task_dir).resolve()
    try:
        raw = (task_dir / "00_Assigments.md").read_bytes()
        assigned, mirror = parse_assignment(raw.decode("utf-8"))
    except (OSError, UnicodeError) as exc:
        raise ContextError(f"Cannot read assignment in {task_dir}: {exc}") from exc
    universe_module = _universe_module()
    policy = _json(policy_path)
    if mirror.get("spec_version", "V3").upper() != "V3":
        raise ContextError("This loader requires a V3 assignment; use explicit legacy tooling for V2")
    mode = assigned["difficulty_mode"]
    if mode not in policy["difficulty_caps"]:
        raise ContextError(f"Unsupported assigned difficulty mode {mode!r}")
    date = _date_key(assigned["universe_date_raw"])
    if date not in policy["freeze_dates"]:
        raise ContextError(f"Universe date {date} is not one of the V3 assigned dates")
    universe = universe_block(universe_key(date, universe_module), universe_module)
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
    source = source_context(date, freeze, registry_path, module=universe_module)
    out = {"spec_version": "V3", **assigned, **derived, "universe_date_key": date,
           "freeze_utc": freeze, "freeze_basis": "V3 assigned-date mapping = seed bound; the eval clock is universe.clock_utc",
           "universe": universe,
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
            refuse_read_only(out, "the task context output")
            out.parent.mkdir(parents=True, exist_ok=True)
            # Exclusively created temp file (random name, O_EXCL) written through its own descriptor, then
            # renamed over the output: nothing is ever written through a pre-existing (sym/hard) link.
            fd, temp = tempfile.mkstemp(dir=out.parent, prefix=out.name + ".", suffix=".tmp")
            try:
                with os.fdopen(fd, "w", encoding="utf-8") as handle:
                    os.fchmod(handle.fileno(), 0o644)
                    handle.write(json.dumps(context, ensure_ascii=False, indent=2) + "\n")
                os.replace(temp, out)
            except BaseException:
                if os.path.lexists(temp):
                    os.unlink(temp)
                raise
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

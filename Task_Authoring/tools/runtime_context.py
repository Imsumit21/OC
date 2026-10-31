"""Apply a validated task context to legacy tools without changing their profiles.

All source folders remain read-only. CLI archival self-tests deliberately retain
their V2 fixtures; task commands inherit TASK_AUTHORING_TASK_DIR in subprocesses.
"""
from __future__ import annotations

import datetime as dt
import copy
import json
import os
import sys
from pathlib import Path

from task_context import BUNDLE, DEFAULT_TASK, ContextError, load_context, is_v3_assignment

MODULES = ("sql_lint", "base_check", "persona_view", "fact_check", "hardness_gate", "shortcut_probe", "entity")
WORKSPACE = BUNDLE.parent                                 # holds Evals/, Universe_*/ and HarmonyGames_*/
SENTINEL_DIR = ".universe_source_not_ready"               # never a previous task's roots
UNIVERSE_BY_DATE = {"2026-02-14": "normal", "2025-10-01": "synthcut"}
UNIVERSE_BUILD = "per-universe-v1"


class KBUnavailable(ContextError):
    """No KB is bound to the selected universe; consumers downgrade instead of reading a stale KB."""


def _universe(context):
    universe = context.get("universe") or {}
    key = universe.get("key") or (context.get("source") or {}).get("universe") or UNIVERSE_BY_DATE.get(
        context.get("universe_date_key"))
    return universe, key


def _meta_problem(metadata, context):
    """Why a KB file's _meta is not authoritative for this context (None when it is)."""
    if not isinstance(metadata, dict):
        return "missing _meta"
    universe, key = _universe(context)
    source = context.get("source") or {}
    if not key or metadata.get("universe") != key:
        return f"_meta.universe {metadata.get('universe')!r} is not {key!r}"
    clock = universe.get("clock_utc") or source.get("data_clock")
    if _utc(metadata.get("clock")) is None or _utc(metadata.get("clock")) != _utc(clock):
        return f"_meta.clock {metadata.get('clock')!r} is not the {key} data clock {clock!r}"
    if metadata.get("source_fingerprint") != source.get("fingerprint"):
        return "source_fingerprint does not match the selected source"
    if metadata.get("build") != UNIVERSE_BUILD:
        return f"_meta.build {metadata.get('build')!r} is not {UNIVERSE_BUILD!r}"
    return None


def entities_file(context):
    """A records-built entities file for this universe, or None when it is absent or stale."""
    source = (context or {}).get("source") or {}
    if source.get("status") != "ready" or not source.get("kb_output_path"):
        return None
    path = Path(source["kb_output_path"]) / "entities.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError):
        return None
    return path if isinstance(data, dict) and _meta_problem(data.get("_meta"), context) is None else None


def _apply(namespace, context, force=False):
    previous = namespace.get("TASK_CONTEXT", {}).get("context_hash")
    if previous == context.get("context_hash") and not force:
        return
    namespace["TASK_CONTEXT"] = context
    # freeze_utc is the V3 seed bound (seeded writes, completed facts); universe.clock_utc is the data
    # horizon (records that exist and are visible). Never conflate them for a synth-cut task.
    if "CLOCK" in namespace:
        namespace["CLOCK"] = dt.datetime.fromisoformat(context["freeze_utc"].replace("Z", "+00:00"))
    universe, _ = _universe(context)
    if "DATA_CLOCK" in namespace and universe.get("clock_utc"):
        namespace["DATA_CLOCK"] = dt.datetime.fromisoformat(universe["clock_utc"].replace("Z", "+00:00"))
    source = context["source"]
    cache = BUNDLE / "support" / "local_search" / "cache" / context["context_hash"][:20]
    if "CACHE" in namespace:
        old = Path(namespace["CACHE"])
        namespace["CACHE"] = cache / "shortcut_probe" if old.name == "shortcut_probe" else cache
    if "GMAIL_INDEX" in namespace:
        namespace["GMAIL_INDEX"] = cache / "base_gmail_index.json"
    sentinel = WORKSPACE / SENTINEL_DIR
    if source.get("status") == "ready" and source.get("paths"):
        paths = {s: Path(v) for s, v in source["paths"].items()}
        other = paths["slack"].parent
        if any(paths[s].parent != other for s in paths if s not in ("github", "gmail")):
            raise ContextError("The selected source must use one Services_Data parent for the non-GitHub/Gmail services")
        targets = {"OTHER": other, "GMAIL": paths["gmail"],
                   "GITHUB": paths["github"] / "data.json", "SLACK_MSGS": paths["slack"] / "messages"}
    elif os.environ.get("TASK_AUTHORING_LEGACY_V2") == "1":
        targets = {}  # archived V2 self-tests keep their own fixtures
    else:
        targets = {"OTHER": sentinel / "other", "GMAIL": sentinel / "gmail",
                   "GITHUB": sentinel / "github" / "data.json", "SLACK_MSGS": sentinel / "slack" / "messages"}
    for key, value in targets.items():
        if key in namespace:
            namespace[key] = value
    kb = Path(source["kb_path"]) if source.get("kb_path") and source.get("kb_status") != "unavailable" \
        else sentinel / "kb"
    if "KB" in namespace:
        namespace["KB"] = kb
    if "OUT" in namespace and Path(namespace["OUT"]).name == "entities.json":
        output = source.get("kb_output_path") or source.get("kb_path")
        built_entities = entities_file(context) if source.get("kb_status") == "unavailable" else None
        if built_entities:
            # Synth-cut before a full KB rebuild: a records-built entities file with matching _meta is usable.
            namespace["OUT"] = built_entities
        elif source.get("kb_status") == "unavailable" or not output:
            namespace["OUT"] = sentinel / "kb" / "entities.json"
        else:
            generated = Path(output) / "entities.json"
            shared = (Path(source["kb_path"]) / "entities.json") if source.get("kb_path") else generated
            namespace["OUT"] = generated if "build" in sys.argv[1:] or generated.is_file() else shared
    # Do not reuse objects or KB rows from a previous task in the same interpreter.
    for key in ("_KB", "_BASE_TEXT_CACHE"):
        if isinstance(namespace.get(key), dict):
            namespace[key].clear()


def activate(namespace=None, task_dir=None, require_source=False, force=False):
    task_dir = Path(task_dir or os.environ.get("TASK_AUTHORING_TASK_DIR", DEFAULT_TASK)).resolve()
    context = load_context(task_dir, require_source=require_source)
    os.environ.pop("TASK_AUTHORING_LEGACY_V2", None)
    os.environ["TASK_AUTHORING_TASK_DIR"] = str(task_dir)
    os.environ["TASK_AUTHORING_CONTEXT_HASH"] = context["context_hash"]
    _, key = _universe(context)
    if key:
        os.environ["TASK_AUTHORING_UNIVERSE"] = key
    else:
        os.environ.pop("TASK_AUTHORING_UNIVERSE", None)
    os.environ.pop("TASK_AUTHORING_UNIVERSE_MANIFEST", None)  # every helper selects through hg_universe
    for name in MODULES:
        if name in sys.modules:
            _apply(vars(sys.modules[name]), context, force=force)
    if namespace is not None:
        _apply(namespace, context, force=force)
    return context


def _assignment_is_v3(task_dir):
    path = Path(task_dir) / "00_Assigments.md"
    try:
        return path.is_file() and is_v3_assignment(path.read_text())
    except OSError:
        return False


def _legacy_refuses(task_dir):
    """--legacy-v2/--self-test stays for archived fixtures, never for a V3 task."""
    if task_dir and _assignment_is_v3(task_dir):
        raise ContextError("legacy V2 mode cannot run on a V3 assignment")


def ensure_active(namespace, require_source=True):
    """Late imports made by a stage inherit that stage's already selected task.

    A cached context hash is not proof that the source is still ready: readiness can change
    without the hash moving, so require_source re-runs the check even for an unchanged hash.
    """
    task_dir = os.environ.get("TASK_AUTHORING_TASK_DIR")
    if os.environ.get("TASK_AUTHORING_LEGACY_V2") == "1":
        for candidate in [task_dir, *_legacy_candidates([task_dir] if task_dir else [])]:
            _legacy_refuses(candidate)
        return
    if not task_dir:
        return
    unchanged = namespace.get("TASK_CONTEXT", {}).get("context_hash") == os.environ.get("TASK_AUTHORING_CONTEXT_HASH")
    if unchanged and not require_source:
        return
    context = activate(namespace, require_source=require_source, force=require_source)
    if require_source and context.get("source", {}).get("status") != "ready":
        raise ContextError(context["source"].get("reason") or "The selected source is not ready")


def validate_kb(data, namespace):
    context = namespace.get("TASK_CONTEXT")
    if not context:
        return data
    metadata = data.get("_meta", {}) if isinstance(data, dict) else {}
    source = context["source"]
    status = source.get("kb_status")
    if status == "unavailable":
        raise KBUnavailable(source.get("reason") or "No knowledge base is bound to the selected universe; "
                            "rebuild it before using KB facts")
    if status == "reference-only":
        clock = metadata.get("reference_clock") or metadata.get("clock") or source.get("data_clock")
        return _reference_view(data, context, clock)
    if status == "bound":
        problem = _meta_problem(metadata, context)
        if problem:
            _, key = _universe(context)
            raise ContextError(f"KB file is not authoritative for the {key} universe: {problem}; rebuild that file")
        return data
    # Explicitly separate historical sources ("snapshot") retain their stricter provenance check.
    clock = metadata.get("clock")
    try:
        parsed = dt.datetime.fromisoformat(str(clock).replace("Z", "+00:00"))
        expected = dt.datetime.fromisoformat(context["freeze_utc"].replace("Z", "+00:00"))
        if parsed != expected:
            raise ValueError("different freeze")
    except (TypeError, ValueError):
        raise ContextError(f"KB file has missing or mismatched clock {clock!r}; regenerate from the selected source for {context['freeze_utc']}")
    if metadata.get("source_fingerprint") != source.get("fingerprint"):
        raise ContextError("KB file is not bound to the selected historical source fingerprint")
    return data


def _utc(value):
    try:
        parsed = dt.datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return parsed.replace(tzinfo=dt.timezone.utc) if parsed.tzinfo is None else parsed.astimezone(dt.timezone.utc)
    except (TypeError, ValueError):
        return None


def _reference_view(data, context, reference_clock):
    """Conservative, non-mutating view of a shared KB for an earlier assignment."""
    if not isinstance(data, dict):
        return data
    view = copy.deepcopy(data)
    freeze = _utc(context["freeze_utc"])
    metadata = view.setdefault("_meta", {})
    metadata.update(reference_clock=reference_clock, assigned_freeze=context["freeze_utc"],
                    reference_only=True, requires_record_verification=True,
                    reference_note="Shared-universe reference. Verify actual records and their dates before using a fact; "
                                   "later lifecycle, body edits and permissions are not reconstructed by this view.")
    if "people" in view and isinstance(view["people"], dict):
        _activity_reference(view, freeze)
    if isinstance(view.get("entities"), list):
        for entity in view["entities"]:
            entity["reference_only"] = True
            entity["requires_record_verification"] = True
            entity["last_activity"] = {service: value if _before(value, freeze) else None
                                       for service, value in (entity.get("last_activity") or {}).items()}
            for identities in (entity.get("identities") or {}).values():
                for identity in identities:
                    identity["reference_only"] = True
                    for key in list(identity):
                        if key.startswith(("last", "first")) and _utc(identity[key]) is not None and not _before(identity[key], freeze):
                            identity[key] = None
    if "spine" in view or "storyline_beats_2024_plus" in view:
        _timeline_reference(view, freeze)
    return view


def _before(value, freeze):
    parsed = _utc(value)
    return parsed is not None and parsed < freeze


def _months_before(values, freeze):
    # A monthly aggregate can only establish activity in a fully elapsed month.
    # Never turn a monthly count into an invented exact last-activity date.
    cutoff = freeze.strftime("%Y-%m")
    return {month: count for month, count in (values or {}).items()
            if isinstance(month, str) and len(month) == 7 and month < cutoff}


def _activity_reference(view, freeze):
    monthly_fields = {"monthly", "sent_monthly", "monthly_events", "created_monthly", "completed_monthly",
                      "commits_monthly", "prs_monthly", "reviews_monthly"}
    observed_fields = {"first", "last", "sent_first", "sent_last", "first_event", "last_event",
                       "first_created", "last_modified", "modified_last"}

    def service_reference(service):
        safe = {key: value for key, value in service.items()
                if key in ("id", "user_id", "logins", "join_basis", "calendar_tz", "member_id")}
        safe.update({key: _months_before(value, freeze) for key, value in service.items() if key in monthly_fields})
        safe.update({key: value if _before(value, freeze) else None
                     for key, value in service.items() if key in observed_fields})
        safe["reference_only"] = True
        return safe

    for person in view["people"].values():
        person["status_at_clock"] = "activity_record_verification_required"
        person["reference_only"] = True
        person["monthly_authored_total"] = _months_before(person.get("monthly_authored_total"), freeze)
        for key in ("first_activity_by_service", "last_activity_by_service"):
            person[key] = {service: value if _before(value, freeze) else None
                           for service, value in (person.get(key) or {}).items()}
        signals = person.get("departure_signals") or {}
        person["departure_signals"] = {
            key: value if _before(value, freeze) else None for key, value in signals.items()
            if key in ("last_authored_activity", "last_slack_message", "last_gmail_sent", "gmail_mailbox_last", "last_github", "last_linear")}
        if person["departure_signals"].get("last_authored_activity"):
            person["departure_signals"]["last_authored_service"] = signals.get("last_authored_service")
        person["departure_signals"].update(verification_required=True,
                                         note="Observed dates are reference records, not a verified departure or current activity status.")
        person["services"] = {service: service_reference(values) for service, values in (person.get("services") or {}).items()
                              if isinstance(values, dict)}
    # Later summary labels and candidate lists must not leak February status.
    view["summary"] = {"people": len(view["people"]), "activity_record_verification_required": sorted(view["people"]),
                       "quiet_or_departed": [], "monthly_reference_only": True}
    for key in list(view):
        if key.startswith("seed_voice_candidates_"):
            del view[key]
    for key in ("slack_only_ids", "github_unjoined_logins"):
        if isinstance(view.get(key), dict):
            view[key] = {identity: service_reference(values) for identity, values in view[key].items()
                         if isinstance(values, dict)}
    view["_meta"]["status_rule"] = "Earlier-date reference only: retain activity in fully elapsed months; verify dated records for persona activity. No departure is inferred."


def _timeline_reference(view, freeze):
    for key in ("spine", "storyline_beats_2024_plus"):
        events = []
        for event in view.get(key) or []:
            if not _before(event.get("date"), freeze):
                continue
            event.update(reference_only=True, orientation_only=True)
            evidence = event.get("evidence") or []
            event["evidence"] = [item for item in evidence
                                 if not isinstance(item, dict) or _before(item.get("when"), freeze)]
            if any(isinstance(item, dict) for item in evidence):
                event["services"] = sorted({item["service"] for item in event["evidence"]
                                             if isinstance(item, dict) and item.get("service")})
                event["meets_2_service_rule"] = len(event["services"]) >= 2
            events.append(event)
        if key in view:
            view[key] = events
    if "counts" in view:
        view["counts"].update(spine_events=len(view.get("spine", [])),
                              spine_meeting_rule=sum(bool(event.get("meets_2_service_rule")) for event in view.get("spine", [])),
                              storyline_beats=len(view.get("storyline_beats_2024_plus", [])))


def _inferred_tasks(argv):
    """Every task folder an input file argument belongs to, in argument order (distinct).

    Both the path as given and its resolved target (symlinks followed) are walked up through every
    ancestor, so a symlinked or deeply nested copy of a task input still names its task folder.
    """
    found, keys = [], set()
    for arg in argv:
        value = arg.split("=", 1)[1] if arg.startswith("--") and "=" in arg else arg
        path = Path(value)
        if not (value and path.is_file() and path.suffix in (".sql", ".json", ".md")):
            continue
        for start in (path.absolute(), path.resolve()):
            for parent in start.parents:
                if (parent / "00_Assigments.md").is_file():
                    key = str(parent.resolve())
                    if key not in keys:
                        keys.add(key)
                        found.append(parent)
                    break
    return found


def _legacy_candidates(argv):
    """Every assignment folder above ANY existing path argument, for the legacy-mode refusal.

    Unlike the nearest-owner inference above, this ignores the file suffix (seed.SQL, extensionless
    aliases), includes a folder argument itself, and keeps walking past a nearer assignment marker,
    so an archived V2 marker nested inside a V3 task cannot hide that task.
    """
    found, keys = [], set()
    for arg in argv:
        if not arg:
            continue
        # Any token that exists as a path counts, even one spelled like an option (a file named '-');
        # an --opt=value token is checked for its value as well.
        values = [arg] + ([arg.split("=", 1)[1]] if arg.startswith("--") and "=" in arg else [])
        for value in values:
            path = Path(value)
            if not value or not path.exists():
                continue
            for start in (path.absolute(), path.resolve()):
                for parent in ((start,) if start.is_dir() else ()) + tuple(start.parents):
                    if (parent / "00_Assigments.md").is_file():
                        key = str(parent.resolve())
                        if key not in keys:
                            keys.add(key)
                            found.append(parent)
    return found


def _inferred_task(argv):
    """A task input path is more specific than the default active workspace."""
    found = _inferred_tasks(argv)
    return found[0] if found else None


def cli_entry(namespace, require_source=False):
    """Strip the shared --task-dir option before legacy argument parsing."""
    argv = sys.argv[1:]
    named = []                              # every --task-dir value, separate or equals form
    for index, arg in enumerate(sys.argv[1:], 1):
        if arg == "--task-dir":
            if index + 1 >= len(sys.argv):
                raise ContextError("--task-dir requires a path")
            named.append(sys.argv[index + 1])
        elif arg.startswith("--task-dir="):
            if not arg.split("=", 1)[1]:
                raise ContextError("--task-dir requires a path")
            named.append(arg.split("=", 1)[1])
    if len({str(Path(v).resolve()) for v in named}) > 1:
        raise ContextError("--task-dir given more than once with different folders: " + ", ".join(named))
    explicit = named[0] if named else None
    # the equals form selects the task exactly like the separate form; strip it before the tool parses argv
    sys.argv[:] = [a for a in sys.argv if not a.startswith("--task-dir=")]
    argv = sys.argv[1:]
    legacy = "--self-test" in argv or "--legacy-v2" in argv or os.environ.get("TASK_AUTHORING_LEGACY_V2") == "1"
    if legacy:
        if "--legacy-v2" in argv:
            sys.argv.remove("--legacy-v2")
        os.environ["TASK_AUTHORING_LEGACY_V2"] = "1"
        # A V3 task named by --task-dir, the environment or ANY input file's folder is never run in legacy mode.
        named_dirs = [d for d in (explicit, os.environ.get("TASK_AUTHORING_TASK_DIR")) if d]
        # Named task folders are walked too: a V2 folder nested inside a V3 task must not hide that task.
        candidates = [*named_dirs, *_legacy_candidates([*named_dirs, *argv])]
        if not any(candidates) and "--self-test" not in argv:
            candidates.append(DEFAULT_TASK)  # a tool that falls back to the default task would read it
        for candidate in candidates:
            _legacy_refuses(candidate)
        return None
    if any(a in argv for a in ("--help", "-h")) or not argv:
        return None
    task_dir = explicit
    while "--task-dir" in sys.argv:
        index = sys.argv.index("--task-dir")
        del sys.argv[index:index + 2]
    if task_dir is None and not os.environ.get("TASK_AUTHORING_TASK_DIR"):
        task_dir = _inferred_task(argv)
    selected = Path(task_dir or os.environ.get("TASK_AUTHORING_TASK_DIR", DEFAULT_TASK))
    assignment = selected / "00_Assigments.md"
    if not assignment.is_file() or not is_v3_assignment(assignment.read_text()):
        raise ContextError("V3 commands require a complete assignment. --legacy-v2 is only for archived V2 diagnostics")
    return activate(namespace, selected, require_source=require_source)


def guarded_entry(namespace, require_source=False):
    try:
        return cli_entry(namespace, require_source)
    except ContextError as exc:
        print("TASK CONTEXT FAIL: " + str(exc), file=sys.stderr)
        raise SystemExit(2)

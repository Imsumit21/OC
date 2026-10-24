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


def _apply(namespace, context):
    previous = namespace.get("TASK_CONTEXT", {}).get("context_hash")
    if previous == context["context_hash"]:
        return
    namespace["TASK_CONTEXT"] = context
    clock = dt.datetime.fromisoformat(context["freeze_utc"].replace("Z", "+00:00"))
    if "CLOCK" in namespace:
        namespace["CLOCK"] = clock
    source = context["source"]
    cache = BUNDLE / "support" / "local_search" / "cache" / context["context_hash"][:20]
    if "CACHE" in namespace:
        old = Path(namespace["CACHE"])
        namespace["CACHE"] = cache / "shortcut_probe" if old.name == "shortcut_probe" else cache
    if "GMAIL_INDEX" in namespace:
        namespace["GMAIL_INDEX"] = cache / "base_gmail_index.json"
    paths = {s: Path(v) for s, v in source.get("paths", {}).items()}
    if paths:
        other = paths["slack"].parent
        if any(paths[s].parent != other for s in paths if s not in ("github", "gmail")):
            raise ContextError("The selected source must use one Services_Data parent for the non-GitHub/Gmail services")
        for key, value in {"OTHER": other, "GMAIL": paths["gmail"],
                           "GITHUB": paths["github"] / "data.json", "SLACK_MSGS": paths["slack"] / "messages"}.items():
            if key in namespace:
                namespace[key] = value
    if source.get("kb_path"):
        if "KB" in namespace:
            namespace["KB"] = Path(source["kb_path"])
        if "OUT" in namespace and Path(namespace["OUT"]).name == "entities.json":
            generated = Path(source.get("kb_output_path") or source["kb_path"]) / "entities.json"
            shared = Path(source["kb_path"]) / "entities.json"
            namespace["OUT"] = generated if "build" in sys.argv[1:] or generated.is_file() else shared
    # Do not reuse objects or KB rows from a previous task in the same interpreter.
    for key in ("_KB", "_BASE_TEXT_CACHE"):
        if isinstance(namespace.get(key), dict):
            namespace[key].clear()


def activate(namespace=None, task_dir=None, require_source=False):
    task_dir = Path(task_dir or os.environ.get("TASK_AUTHORING_TASK_DIR", DEFAULT_TASK)).resolve()
    context = load_context(task_dir, require_source=require_source)
    os.environ.pop("TASK_AUTHORING_LEGACY_V2", None)
    os.environ["TASK_AUTHORING_TASK_DIR"] = str(task_dir)
    os.environ["TASK_AUTHORING_CONTEXT_HASH"] = context["context_hash"]
    if context["source"].get("manifest"):
        os.environ["TASK_AUTHORING_UNIVERSE_MANIFEST"] = context["source"]["manifest"]
    else:
        os.environ.pop("TASK_AUTHORING_UNIVERSE_MANIFEST", None)
    for name in MODULES:
        if name in sys.modules:
            _apply(vars(sys.modules[name]), context)
    if namespace is not None:
        _apply(namespace, context)
    return context


def ensure_active(namespace, require_source=False):
    """Late imports made by a stage inherit that stage's already selected task."""
    if os.environ.get("TASK_AUTHORING_LEGACY_V2") == "1" or not os.environ.get("TASK_AUTHORING_TASK_DIR"):
        return
    if namespace.get("TASK_CONTEXT", {}).get("context_hash") != os.environ.get("TASK_AUTHORING_CONTEXT_HASH"):
        activate(namespace, require_source=require_source)


def validate_kb(data, namespace):
    context = namespace.get("TASK_CONTEXT")
    if not context:
        return data
    metadata = data.get("_meta", {}) if isinstance(data, dict) else {}
    source = context["source"]
    if source.get("mode") == "shared-universe":
        # Both assignments intentionally use the same export. A later KB is a
        # discovery reference, not proof of historical state at an earlier freeze.
        clock = metadata.get("reference_clock") or metadata.get("clock") or source.get("data_clock")
        if _utc(clock) == _utc(context["freeze_utc"]) and not metadata.get("reference_only"):
            return data  # preserve the established February view exactly
        return _reference_view(data, context, clock)
    # Explicitly separate historical sources retain their stricter provenance check.
    clock = metadata.get("clock")
    if not clock and context["universe_date_key"] == "2026-02-14":
        return data
    try:
        parsed = dt.datetime.fromisoformat(str(clock).replace("Z", "+00:00"))
        expected = dt.datetime.fromisoformat(context["freeze_utc"].replace("Z", "+00:00"))
        if parsed != expected:
            raise ValueError("different freeze")
    except (TypeError, ValueError):
        raise ContextError(f"KB file has missing or mismatched clock {clock!r}; regenerate from the selected source for {context['freeze_utc']}")
    if context["universe_date_key"] != "2026-02-14" and metadata.get("source_fingerprint") != context["source"]["fingerprint"]:
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


def cli_entry(namespace, require_source=False):
    """Strip the shared --task-dir option before legacy argument parsing."""
    argv = sys.argv[1:]
    if "--self-test" in argv or "--legacy-v2" in argv or os.environ.get("TASK_AUTHORING_LEGACY_V2") == "1":
        if "--legacy-v2" in argv:
            sys.argv.remove("--legacy-v2")
        os.environ["TASK_AUTHORING_LEGACY_V2"] = "1"
        return None
    if any(a in argv for a in ("--help", "-h")) or not argv:
        return None
    task_dir = None
    if "--task-dir" in argv:
        index = sys.argv.index("--task-dir")
        if index + 1 >= len(sys.argv):
            raise ContextError("--task-dir requires a path")
        task_dir = sys.argv[index + 1]
        del sys.argv[index:index + 2]
    if task_dir is None and not os.environ.get("TASK_AUTHORING_TASK_DIR"):
        # A task input path is more specific than the default active workspace.
        for arg in argv:
            path = Path(arg)
            if path.is_file() and path.suffix in (".sql", ".json", ".md"):
                for parent in (path.parent, path.parent.parent):
                    assigned = parent / "00_Assigments.md"
                    if assigned.is_file():
                        task_dir = parent
                        break
                if task_dir:
                    break
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

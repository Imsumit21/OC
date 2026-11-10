#!/usr/bin/env python3
"""task_metrics.py - per-task counters and timeline, so the pipeline can be judged by numbers (plan WS8).

What it keeps. <task>/Working_Files/task_metrics.json: an append-only list of events. Each event has a number, a
kind, a UTC time and optional eval / verdict / stage / note fields. Earlier events are never rewritten.

Event kinds
  sql_revision     one per revision of 01_Universe_Inject.sql
  precheck         one per pre-check run
  baseline         one per six-run baseline batch
  platform_round   one per platform report taken in (--eval and --verdict required); written by report_intake.py
  local_check      one per stored local check (--stage or --eval); written by report_intake.py snapshot
  stage_start      a stage begins (--stage required)
  stage_end        a stage ends (--stage required); wall-clock per stage is the sum of start-to-end spans
  fit_verdict      the assignment-fit verdict (--verdict required); the latest one counts

Targets (plan WS8 item 3; module constants, the policy file does not hold them yet): at most two SQL revisions,
one pre-check, one baseline, and two rounds per platform eval. Being over a target is a measurement, not a tool
failure: the header says OVER TARGET, the JSON verdict is WARN and the exit code stays 0.

Commands
  record --task-dir T --event KIND [--eval E] [--verdict V] [--stage S] [--note TEXT] [--at ISO]
  summary --task-dir T [--json]        counters against the targets; header TASK METRICS: WITHIN TARGET|OVER TARGET
  backfill ARCHIVE_DIR [--json]        the same counters for an archived task, derived from its files; writes nothing
  backfill-all [--root DIR] [--json]   the table for every folder under support/completed_tasks
  --self-test

Backfill reads <archive>/task_inputs (or the folder itself when it has no task_inputs/) and the report folders next
to it. It is an estimate from what was stored:
  SQL revisions   the larger of (a) distinct SQL files among run_forensics/rev*/01_Universe_Inject.sql and the current
                  file, or the highest rev number, and (b) distinct SQL hashes the platform reports say they ran on
  pre-checks      the larger of rev folders that hold pre-check forensics and trajectory files in 06_PreCheck_Trajectory
  baselines       baseline batches stored in run_forensics; at least 1 when 07_Baseline_Trajectories holds runs
  rounds          platform reports per eval (identical files once; a report carrying another task's id is left out).
                  A lower bound: some archives kept only some reports (S2 kept /rubric rounds 1-3, 10 and 11)
Wall-clock per stage, local-versus-platform pairs and the fit verdict are not stored in the archives. An archive with
no SQL history or no reports is not counted as within target (backfill-all reports it as too little to tell). The
"revision N" a report prints next to the SQL is the evaluator input store's global counter, not an SQL revision, and
is not used.

API: record_event(task_dir, event, **fields), summarise(task_dir), evaluate(task_dir), backfill(archive_dir).
`--at` defaults to the current time: this log is the one place a wall-clock stamp is written.

Exit: 0 PASS or WARN, 1 FAIL (unreadable log, refused write), 2 usage error. Stdlib only.
"""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import io
import json
import os
import re
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WS = BUNDLE.parent
sys.path.insert(0, str(HERE))

TOOL = "task_metrics"
VERSION = 1
SCHEMA = "task-metrics-v1"
METRICS_FILE = "task_metrics.json"
EVENTS = ("sql_revision", "precheck", "baseline", "platform_round", "local_check", "stage_start", "stage_end",
          "fit_verdict")
EVALS = ("injection", "prompt", "hardness", "oe", "rubric")
# Plan WS8 item 3. Not in references/first_pass_policy.json yet; the lead can move them there.
TARGETS = {"sql_revisions": 2, "prechecks": 1, "baselines": 1, "rounds_per_platform_eval": 2}
CORE_FIELDS = ("n", "event", "at")
SQL_NAME = "01_Universe_Inject.sql"
REPORT_DIRS = ("eval_reports", "plateform_reports", "platform_reports", "plateform_report", "platform_report")
MAX_HASH_BYTES = 64 * 1024 * 1024       # a stored trajectory larger than this is told apart by size only
RX_AT = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
RX_REV = re.compile(r"^rev(\d+)")
RX_BASELINE_ENTRY = re.compile(r"^baseline\d*$")


class MetricsError(ValueError):
    """The log cannot be read or the event is not valid."""


# ---------------------------------------------------------------- small helpers

def _slot(task_dir, name) -> Path:
    from stage_gate import slot_path
    return slot_path(task_dir, name)


def metrics_path(task_dir) -> Path:
    return _slot(task_dir, METRICS_FILE)


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalise_at(value) -> str:
    """An ISO date or date-time as UTC `YYYY-MM-DDTHH:MM:SSZ`. A time without a zone is read as UTC."""
    text = str(value).strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        text += "T00:00:00"
    try:
        when = dt.datetime.fromisoformat(re.sub(r"[zZ]$", "+00:00", text))
    except ValueError:
        raise MetricsError(f"--at {value!r} is not an ISO date or date-time (use 2026-11-11 or 2026-11-11T09:30:00Z)")
    if when.tzinfo is None:
        when = when.replace(tzinfo=dt.timezone.utc)
    return when.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse_at(text) -> dt.datetime:
    return dt.datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)


def _sha256(path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _atomic_write(path: Path, data: bytes, what: str) -> None:
    from task_context import refuse_read_only
    refuse_read_only(path, what)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            os.fchmod(handle.fileno(), 0o644)
            handle.write(data)
        os.replace(temp, path)
    except BaseException:
        if os.path.lexists(temp):
            os.unlink(temp)
        raise


def duration_text(seconds) -> str:
    seconds = int(seconds)
    hours, rest = divmod(seconds, 3600)
    minutes = rest // 60
    if hours >= 48:
        return f"{hours // 24}d {hours % 24}h"
    if hours:
        return f"{hours}h {minutes:02d}m"
    return f"{minutes}m" if minutes else f"{seconds}s"


def norm_verdict(value) -> str:
    text = " ".join(str(value).split()).upper()
    return {"NONFAIL": "NON-FAIL", "NON FAIL": "NON-FAIL"}.get(text, text)


# ---------------------------------------------------------------- the event log

def load_events(task_dir) -> list:
    """The stored events, oldest first. An absent log is an empty list."""
    path = metrics_path(task_dir)
    if not path.is_file():
        return []
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise MetricsError(f"cannot read {path}: {exc}")
    if not isinstance(doc, dict) or doc.get("schema") != SCHEMA or not isinstance(doc.get("events"), list):
        raise MetricsError(f"{path} is not a {SCHEMA} log; keep it and fix it by hand before recording")
    for number, event in enumerate(doc["events"], 1):
        problem = _event_problem(event, number)
        if problem:
            raise MetricsError(f"{path} entry {number} {problem}: {str(event)[:120]}. Keep the file and fix it by hand "
                               "before recording")
    return doc["events"]


def _event_problem(event, number):
    """Why a stored entry is not a valid event, or None. The log is append-only, so entry k must carry n = k."""
    if not isinstance(event, dict) or event.get("event") not in EVENTS:
        return "is not an event"
    if event.get("n") != number:
        return f"carries n {event.get('n')!r}, not {number} (an entry was removed or reordered)"
    if not isinstance(event.get("at"), str) or not RX_AT.fullmatch(event["at"]):
        return "has no UTC time in the form 2026-11-11T09:30:00Z"
    if event["event"] == "platform_round" and (event.get("eval") not in EVALS or not event.get("verdict")):
        return "is a platform_round without a known eval and a verdict"
    if event["event"] in ("stage_start", "stage_end") and not event.get("stage"):
        return f"is a {event['event']} without a stage"
    return None


def record_event(task_dir, event, **fields) -> dict:
    """Append one event to the task's log and return it. Unknown extra fields are stored as given."""
    task_dir = Path(task_dir)
    if event not in EVENTS:
        raise MetricsError(f"unknown event {event!r}; use one of: {', '.join(EVENTS)}")
    if not task_dir.is_dir():
        raise MetricsError(f"task folder not found: {task_dir}")
    clean = {k: v for k, v in fields.items() if v is not None}
    for key in CORE_FIELDS[:2]:
        if key in clean:
            raise MetricsError(f"field {key!r} is set by the log, not by the caller")
    at = normalise_at(clean.pop("at")) if "at" in clean else _now()
    if "eval" in clean:
        clean["eval"] = str(clean["eval"]).strip().lstrip("/").lower()
        if clean["eval"] not in EVALS:
            raise MetricsError(f"unknown eval {clean['eval']!r}; use one of: {', '.join(EVALS)}")
    if "stage" in clean:
        clean["stage"] = str(clean["stage"]).strip().lower()
    if "verdict" in clean:
        clean["verdict"] = norm_verdict(clean["verdict"])
    if event == "platform_round" and not (clean.get("eval") and clean.get("verdict")):
        raise MetricsError("platform_round needs --eval and --verdict")
    if event in ("stage_start", "stage_end") and not clean.get("stage"):
        raise MetricsError(f"{event} needs --stage")
    if event == "fit_verdict" and not clean.get("verdict"):
        raise MetricsError("fit_verdict needs --verdict")
    if event == "local_check" and not (clean.get("stage") or clean.get("eval")):
        raise MetricsError("local_check needs --stage or --eval")
    events = load_events(task_dir)
    entry = {"n": len(events) + 1, "event": event, "at": at}
    entry.update(sorted(clean.items()))
    doc = {"schema": SCHEMA, "events": events + [entry]}
    data = (json.dumps(doc, indent=1, ensure_ascii=False) + "\n").encode("utf-8")
    _atomic_write(metrics_path(task_dir), data, "the task metrics log")
    return entry


# ---------------------------------------------------------------- summary

def _empty_rounds() -> dict:
    return {name: {"count": 0, "verdicts": []} for name in EVALS}


def _stage_times(events) -> tuple:
    """(seconds per stage, stages still open -> start time, notes)."""
    seconds, opened, notes = {}, {}, []
    for event in events:
        stage = event.get("stage")
        if event["event"] == "stage_start":
            if stage in opened:
                notes.append(f"{stage} was started twice without an end (event {event['n']}); the first start counts")
            else:
                opened[stage] = event["at"]
        elif event["event"] == "stage_end":
            if stage not in opened:
                notes.append(f"{stage} has an end without a start (event {event['n']}); ignored")
                continue
            span = (_parse_at(event["at"]) - _parse_at(opened.pop(stage))).total_seconds()
            if span < 0:
                notes.append(f"{stage} ends before it starts (event {event['n']}); counted as 0")
                span = 0
            seconds[stage] = seconds.get(stage, 0) + int(span)
    return seconds, opened, notes


def _finish(summary) -> dict:
    """Add the comparison with the targets."""
    over = []
    for key in ("sql_revisions", "prechecks", "baselines"):
        value = summary.get(key)
        if value is not None and value > TARGETS[key]:
            over.append(key)
    for name in EVALS:
        if summary["rounds"][name]["count"] > TARGETS["rounds_per_platform_eval"]:
            over.append("rounds." + name)
    summary["targets"] = dict(TARGETS)
    summary["over_target"] = over
    summary["within_target"] = not over
    return summary


def summary_from_events(events) -> dict:
    count = lambda kind: sum(1 for e in events if e["event"] == kind)   # noqa: E731
    rounds = _empty_rounds()
    pairs = []
    for event in events:
        if event["event"] != "platform_round":
            continue
        rounds[event["eval"]]["count"] += 1
        rounds[event["eval"]]["verdicts"].append(event.get("verdict", "UNKNOWN"))
        if event.get("local_verdict"):
            local, platform = norm_verdict(event["local_verdict"]), norm_verdict(event.get("verdict", "UNKNOWN"))
            pairs.append({"eval": event["eval"], "local": local, "platform": platform, "agree": local == platform,
                          "basis": event.get("pair_basis"), "report": event.get("report"),
                          "snapshot": event.get("local_snapshot"), "event": event["n"]})
    local_checks = {}
    for event in events:
        if event["event"] == "local_check":
            key = event.get("stage") or event.get("eval")
            entry = local_checks.setdefault(key, {"count": 0, "last_verdict": None})
            entry["count"] += 1
            entry["last_verdict"] = event.get("verdict")
    seconds, opened, notes = _stage_times(events)
    fits = [e for e in events if e["event"] == "fit_verdict"]
    return _finish({
        "source": "events", "events": len(events),
        "sql_revisions": count("sql_revision"), "prechecks": count("precheck"), "baselines": count("baseline"),
        "rounds": rounds, "stage_seconds": dict(sorted(seconds.items())), "open_stages": dict(sorted(opened.items())),
        "stage_notes": notes, "local_checks": dict(sorted(local_checks.items(), key=lambda kv: str(kv[0]))),
        "verdict_pairs": pairs,
        "fit_verdict": {"verdict": fits[-1]["verdict"], "at": fits[-1]["at"], "recorded": len(fits)} if fits else None,
        "first_event": events[0]["at"] if events else None, "last_event": events[-1]["at"] if events else None})


def summarise(task_dir) -> dict:
    """Counters, rounds, stage times, verdict pairs and the fit verdict, with each count against its target."""
    return summary_from_events(load_events(task_dir))


def _count_check(check_id, value, target, noun, basis=None) -> dict:
    tail = f" ({basis})" if basis else ""
    if value is None:
        return {"id": check_id, "status": "SKIP", "detail": f"no {noun} count is stored{tail}"}
    if value == 0 and not basis:
        return {"id": check_id, "status": "SKIP", "detail": f"no {noun} recorded yet; the target is at most {target}"}
    plural = noun if value == 1 else noun + "s"
    status = "WARN" if value > target else "PASS"
    return {"id": check_id, "status": status, "detail": f"{value} {plural}; the target is at most {target}{tail}"}


def checks_for(summary) -> list:
    basis = summary.get("basis") or {}
    checks = [
        _count_check("metrics.sql_revisions", summary["sql_revisions"], TARGETS["sql_revisions"], "SQL revision",
                     basis.get("sql_revisions")),
        _count_check("metrics.prechecks", summary["prechecks"], TARGETS["prechecks"], "pre-check",
                     basis.get("prechecks")),
        _count_check("metrics.baselines", summary["baselines"], TARGETS["baselines"], "baseline",
                     basis.get("baselines"))]
    target = TARGETS["rounds_per_platform_eval"]
    for name in EVALS:
        entry = summary["rounds"][name]
        if not entry["count"]:
            checks.append({"id": "metrics.rounds." + name, "status": "SKIP",
                           "detail": f"no /{name} round " + ("is stored" if basis else "recorded yet")})
            continue
        verdicts = ", ".join(entry["verdicts"])
        checks.append({"id": "metrics.rounds." + name, "status": "WARN" if entry["count"] > target else "PASS",
                       "detail": f"{entry['count']} round{'s' if entry['count'] != 1 else ''} ({verdicts}); "
                                 f"the target is at most {target}"})
    if basis.get("rounds"):
        checks.append({"id": "metrics.rounds.source", "status": "PASS", "detail": basis["rounds"]})
    if summary.get("source") == "backfill":
        checks.append({"id": "metrics.not_stored", "status": "SKIP",
                       "detail": "wall-clock per stage, local-versus-platform pairs and the fit verdict are not "
                                 "stored in an archive"})
        return checks
    seconds, opened = summary["stage_seconds"], summary["open_stages"]
    if seconds or opened:
        parts = [f"{stage} {duration_text(value)}" for stage, value in seconds.items()]
        parts += [f"{stage} open since {at}" for stage, at in opened.items()]
        detail = "; ".join(parts) + ("; note: " + "; ".join(summary["stage_notes"]) if summary["stage_notes"] else "")
        checks.append({"id": "metrics.stage_time", "status": "WARN" if summary["stage_notes"] else "PASS",
                       "detail": detail})
    else:
        checks.append({"id": "metrics.stage_time", "status": "SKIP", "detail": "no stage_start or stage_end recorded"})
    pairs = summary["verdict_pairs"]
    if pairs:
        agree = sum(1 for p in pairs if p["agree"])
        shown = "; ".join(f"/{p['eval']} local {p['local']} / platform {p['platform']}" for p in pairs)
        checks.append({"id": "metrics.verdict_pairs", "status": "PASS",
                       "detail": f"{len(pairs)} local-versus-platform pair{'s' if len(pairs) != 1 else ''}, "
                                 f"{agree} agree: {shown}"})
    else:
        checks.append({"id": "metrics.verdict_pairs", "status": "SKIP",
                       "detail": "no platform round was paired with a stored local check"})
    fit = summary["fit_verdict"]
    checks.append({"id": "metrics.fit_verdict", "status": "PASS" if fit else "SKIP",
                   "detail": f"{fit['verdict']} (recorded {fit['at']})" if fit else "no fit verdict recorded"})
    return checks


def _result(summary, bound_to, qualifier=None) -> dict:
    state = "WITHIN TARGET" if summary["within_target"] else "OVER TARGET"
    header = "TASK METRICS" + (f" ({qualifier})" if qualifier else "") + ": " + state
    return {"tool": TOOL, "version": VERSION, "verdict": "PASS" if summary["within_target"] else "WARN",
            "bound_to": bound_to, "checks": checks_for(summary), "header": header, "summary": summary}


def evaluate(task_dir) -> dict:
    """The summary as the contract's JSON object. Reads only. An unreadable or tampered log gives verdict FAIL
    (no exception), so a caller in the same process always gets an object."""
    task_dir = Path(task_dir)
    path = metrics_path(task_dir)
    bound = {}
    if path.is_file():
        bound[path.relative_to(task_dir).as_posix()] = _sha256(path)
    try:
        summary = summarise(task_dir)
    except MetricsError as exc:
        return {"tool": TOOL, "version": VERSION, "verdict": "FAIL", "bound_to": bound,
                "checks": [{"id": "metrics.log", "status": "FAIL", "detail": " ".join(str(exc).split())}],
                "header": "TASK METRICS (summary): FAIL", "summary": None}
    return _result(summary, bound)


def render(result) -> str:
    lines = [result["header"]]
    lines += [f"[{c['status']}] {c['id']}: {c['detail']}" for c in result["checks"]]
    return "\n".join(lines)


# ---------------------------------------------------------------- backfill from an archived task

def archive_layout(archive_dir) -> tuple:
    """(task folder, report folders) of an archived task, or of a live task folder."""
    root = Path(archive_dir)
    task = root / "task_inputs" if (root / "task_inputs").is_dir() else root
    folders = []
    for base in (root, task):
        for name in REPORT_DIRS:
            folder = base / name
            if folder.is_dir() and folder.resolve() not in [f.resolve() for f in folders]:
                folders.append(folder)
    return task, folders


def _file_identity(path: Path) -> str:
    size = path.stat().st_size
    return _sha256(path) if size <= MAX_HASH_BYTES else f"size:{size}"


def _backfill_sql(task: Path, reports: list) -> tuple:
    forensics = _slot(task, "run_forensics")
    revs = sorted(d for d in forensics.iterdir() if d.is_dir() and RX_REV.match(d.name)) if forensics.is_dir() else []
    local, parts = None, []
    if revs:
        label_max = max(int(RX_REV.match(d.name).group(1)) for d in revs)
        stored = {_sha256(d / SQL_NAME) for d in revs if (d / SQL_NAME).is_file()}
        current = task / SQL_NAME
        if current.is_file():
            stored.add(_sha256(current))
        local = max(label_max, len(stored))
        parts.append(f"local {local}: {len(revs)} rev folders, highest rev{label_max}, {len(stored)} distinct SQL "
                     "files with the current one")
    cited = set()
    for rep in reports:
        for item in (rep.get("input_hashes") or {}).get(SQL_NAME, [])[:1]:
            cited.add(item["prefix"][:8])
    platform = len(cited) or None
    if platform:
        parts.append(f"platform {platform}: distinct SQL hashes the reports ran on")
    if local is None and platform is None:
        return None, "no run_forensics and no report prints an SQL hash"
    return max(v for v in (local, platform) if v is not None), "; ".join(parts)


def _backfill_prechecks(task: Path) -> tuple:
    forensics = _slot(task, "run_forensics")
    holders = []
    if forensics.is_dir():
        for folder in sorted(d for d in forensics.iterdir() if d.is_dir()):
            if any(entry.name.lower().startswith("precheck") for entry in folder.iterdir()):
                holders.append(folder.name)
    folder = task / "06_PreCheck_Trajectory"
    runs = sorted(f for f in folder.iterdir() if f.is_file() and f.suffix == ".json") if folder.is_dir() else []
    distinct = len({_file_identity(f) for f in runs})
    legacy = [f for f in task.iterdir() if f.is_file() and re.fullmatch(r"(?i)run1_trajectory\.json", f.name)]
    if not distinct and legacy:
        distinct = 1
    if not holders and not distinct:
        return None, "no pre-check forensics and no stored pre-check trajectory"
    basis = f"{len(holders)} rev folders with pre-check forensics" + (f" ({', '.join(holders)})" if holders else "")
    basis += f"; {distinct} distinct stored pre-check trajectories"
    return max(len(holders), distinct), basis


def _backfill_baselines(task: Path) -> tuple:
    forensics = _slot(task, "run_forensics")
    batches = []
    if forensics.is_dir():
        for folder in sorted(d for d in forensics.iterdir() if d.is_dir()):
            if "baseline" in folder.name.lower():
                batches.append(folder.name)
                continue
            if not RX_REV.match(folder.name):
                continue
            for entry in sorted(folder.iterdir()):
                if RX_BASELINE_ENTRY.match(entry.name.split(".")[0].lower()):
                    batches.append(f"{folder.name}/{entry.name}")
    folder = task / "07_Baseline_Trajectories"
    runs = [f for f in folder.iterdir() if f.is_file() and f.suffix == ".json"] if folder.is_dir() else []
    verifier = (task / "10_Baseline_Verifier_Results.md").is_file()
    floor = 1 if runs else 0
    if not batches and not floor:
        return None, "no baseline forensics and no stored baseline trajectory" + (
            " (a verifier results file exists)" if verifier else "")
    basis = f"{len(batches)} baseline batches in run_forensics" + (f" ({', '.join(batches)})" if batches else "")
    basis += f"; {len(runs)} runs in 07_Baseline_Trajectories"
    return max(len(batches), floor), basis


def _read_reports(folders) -> tuple:
    """(reports to count, notes). Identical files count once; a report carrying a minority platform id is left out."""
    import report_intake
    seen, reports, notes = set(), [], []
    # Oldest first, so of two identical files the earlier one is counted and the later one is the noted copy.
    files = sorted({f.resolve(): f for folder in folders for f in folder.rglob("*.md") if f.is_file()}.values(),
                   key=lambda f: (f.stat().st_mtime, str(f)))
    for path in files:
        rep = report_intake.read_report(path)
        if rep["eval"] is None:
            notes.append(f"{path.name}: eval kind not recognised, not counted")
            continue
        if rep["sha256"] in seen:
            notes.append(f"{path.name}: identical to a report already counted")
            continue
        seen.add(rep["sha256"])
        rep["folder"] = path.parent
        reports.append(rep)
    by_folder = {}
    for rep in reports:
        if rep["name_id"]:
            by_folder.setdefault(rep["folder"], {}).setdefault(rep["name_id"], []).append(rep)
    foreign = set()
    for folder, ids in by_folder.items():
        if len(ids) < 2:
            continue
        main = max(ids, key=lambda k: len(ids[k]))
        for other, items in ids.items():
            if other != main:
                foreign.update(id(r) for r in items)
                notes.append(f"{len(items)} report(s) in {folder.name}/ carry platform id {other}, not {main}: "
                             "left out (" + ", ".join(r["name"] for r in items) + ")")
    kept = [r for r in reports if id(r) not in foreign]
    kept.sort(key=lambda r: (r["review_date"] or "", r["mtime"], r["name"]))
    return kept, notes


def backfill(archive_dir) -> dict:
    """The summary counters for an archived task, derived from its stored files. Writes nothing."""
    root = Path(archive_dir)
    if not root.is_dir():
        raise MetricsError(f"archive folder not found: {root}")
    task, folders = archive_layout(root)
    reports, notes = _read_reports(folders)
    rounds = _empty_rounds()
    for rep in reports:
        rounds[rep["eval"]]["count"] += 1
        rounds[rep["eval"]]["verdicts"].append(rep["verdict"])
    sql, sql_basis = _backfill_sql(task, reports)
    pre, pre_basis = _backfill_prechecks(task)
    base, base_basis = _backfill_baselines(task)
    rounds_basis = (f"{len(reports)} platform reports in " + ", ".join(f.name + "/" for f in folders)) if folders \
        else "no report folder is stored"
    if notes:
        rounds_basis += "; " + "; ".join(notes)
    summary = _finish({
        "source": "backfill", "archive": root.name, "events": 0,
        "sql_revisions": sql, "prechecks": pre, "baselines": base, "rounds": rounds,
        "stage_seconds": {}, "open_stages": {}, "stage_notes": [], "local_checks": {}, "verdict_pairs": [],
        "fit_verdict": None, "first_event": None, "last_event": None,
        "reports_stored": bool(folders),
        "basis": {"sql_revisions": sql_basis, "prechecks": pre_basis, "baselines": base_basis, "rounds": rounds_basis}})
    return _result(summary, {}, f"backfill {root.name}")


def missing_history(summary) -> list:
    """What an archive does not store, so 'within target' cannot be claimed for it: [] when SQL history and reports
    are both there."""
    missing = []
    if summary.get("sql_revisions") is None:
        missing.append("SQL history")
    if not summary.get("reports_stored", True):
        missing.append("platform reports")
    return missing


def _backfill_check(summary) -> dict:
    name, over, missing = summary["archive"], summary["over_target"], missing_history(summary)
    if over:
        tail = f" (also not stored: {', '.join(missing)})" if missing else ""
        return {"id": "metrics.backfill." + name, "status": "WARN", "detail": "over target: " + ", ".join(over) + tail}
    if missing:
        return {"id": "metrics.backfill." + name, "status": "SKIP",
                "detail": f"no count over target, but the archive stores no {' and no '.join(missing)}; not counted "
                          "as within target"}
    return {"id": "metrics.backfill." + name, "status": "PASS", "detail": "within target"}


def backfill_all(root=None) -> dict:
    root = Path(root) if root else BUNDLE / "support" / "completed_tasks"
    if not root.is_dir():
        raise MetricsError(f"folder not found: {root}")
    rows = [backfill(folder) for folder in sorted(p for p in root.iterdir() if p.is_dir())]
    checks = [_backfill_check(r["summary"]) for r in rows]
    within = sum(1 for c in checks if c["status"] == "PASS")
    unknown = sum(1 for c in checks if c["status"] == "SKIP")
    over_counts = {}
    for row in rows:
        for key in row["summary"]["over_target"]:
            over_counts[key] = over_counts.get(key, 0) + 1
    header = f"TASK METRICS (backfill-all): {within} of {len(rows)} archived tasks within target"
    if unknown:
        header += f"; {unknown} store too little to tell"
    return {"tool": TOOL, "version": VERSION, "verdict": "PASS" if within == len(rows) else "WARN", "bound_to": {},
            "checks": checks, "header": header, "targets": dict(TARGETS),
            "tasks_over_each_target": dict(sorted(over_counts.items())), "tasks": [r["summary"] for r in rows]}


def _cell(value) -> str:
    return "-" if value is None else str(value)


def _rounds_cell(entry, stored) -> str:
    if not entry["count"]:
        return "0" if stored else "-"
    fails = sum(1 for v in entry["verdicts"] if v == "FAIL")
    nonfails = sum(1 for v in entry["verdicts"] if v == "NON-FAIL")
    extra = [f"{fails}F"] if fails else []
    extra += [f"{nonfails}N"] if nonfails else []
    return str(entry["count"]) + (f" ({' '.join(extra)})" if extra else "")


def render_table(result) -> str:
    head = ["task", "SQL revs", "pre-checks", "baselines"] + ["/" + name for name in EVALS] + ["over target"]
    rows = [head]
    for s in result["tasks"]:
        stored = s.get("reports_stored", True)
        rows.append([s["archive"], _cell(s["sql_revisions"]), _cell(s["prechecks"]), _cell(s["baselines"])]
                    + [_rounds_cell(s["rounds"][name], stored) for name in EVALS]
                    + [", ".join(k.replace("rounds.", "/").replace("sql_revisions", "sql").replace("prechecks", "pre")
                                 .replace("baselines", "base") for k in s["over_target"])
                       or ("unknown (not stored)" if missing_history(s) else "none")])
    widths = [max(len(r[i]) for r in rows) for i in range(len(head))]
    lines = [result["header"],
             f"targets: at most {TARGETS['sql_revisions']} SQL revisions, {TARGETS['prechecks']} pre-check, "
             f"{TARGETS['baselines']} baseline, {TARGETS['rounds_per_platform_eval']} rounds per platform eval; "
             "rounds are the stored reports (a lower bound where reports were not kept) and show (nF) FAIL and "
             "(nN) NON-FAIL verdicts; '-' means not stored"]
    for i, row in enumerate(rows):
        lines.append("  ".join(cell.ljust(widths[j]) for j, cell in enumerate(row)).rstrip())
        if i == 0:
            lines.append("  ".join("-" * w for w in widths))
    over = result["tasks_over_each_target"]
    lines.append("tasks over each target: " + (", ".join(f"{k} {v}" for k, v in over.items()) or "none"))
    return "\n".join(lines)


# ---------------------------------------------------------------- self-test

def _self_test() -> int:
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("task_metrics_selftest_") as tmp:
        task = Path(tmp) / "task_inputsX"
        (task / "Working_Files").mkdir(parents=True)
        covered = 0
        # 1. an empty task is within target and nothing is written by reading
        assert summarise(task)["within_target"] and not metrics_path(task).exists()
        assert evaluate(task)["header"] == "TASK METRICS: WITHIN TARGET"
        covered += 1
        # 2. record, append-only, counters within target
        at = "2026-11-01T10:00:00Z"
        first = record_event(task, "sql_revision", note="rev1", at=at)
        record_event(task, "stage_start", stage="Injection", at="2026-11-01T10:00:00Z")
        record_event(task, "stage_end", stage="injection", at="2026-11-01T13:30:00+00:00")
        record_event(task, "precheck", verdict="go", at="2026-11-02")
        record_event(task, "baseline", at="2026-11-03T00:00:00Z")
        record_event(task, "platform_round", eval="/Prompt", verdict="nonfail", at="2026-11-03T01:00:00Z",
                     local_verdict="PASS", pair_basis="hash_printed", report="x_1_prompt.md")
        record_event(task, "platform_round", eval="prompt", verdict="PASS", at="2026-11-03T02:00:00Z",
                     local_verdict="PASS", pair_basis="hash_printed")
        record_event(task, "fit_verdict", verdict="fit", at="2026-11-01T09:00:00Z")
        stored = json.loads(metrics_path(task).read_text())["events"]
        assert stored[0] == first and [e["n"] for e in stored] == list(range(1, 9)), stored
        s = summarise(task)
        assert (s["sql_revisions"], s["prechecks"], s["baselines"]) == (1, 1, 1) and s["within_target"], s
        assert s["rounds"]["prompt"] == {"count": 2, "verdicts": ["NON-FAIL", "PASS"]}, s["rounds"]
        assert s["stage_seconds"] == {"injection": 12600} and s["fit_verdict"]["verdict"] == "FIT"
        assert [p["agree"] for p in s["verdict_pairs"]] == [False, True]
        out = render(evaluate(task))
        assert out.splitlines()[0] == "TASK METRICS: WITHIN TARGET" and "[PASS] metrics.sql_revisions: 1 SQL" in out
        assert "injection 3h 30m" in out and "2 local-versus-platform pairs, 1 agree" in out, out
        covered += 1
        # 3. planted bad: over target on SQL revisions and on /prompt rounds
        record_event(task, "sql_revision", at=at)
        record_event(task, "sql_revision", at=at)
        record_event(task, "platform_round", eval="prompt", verdict="FAIL", at=at)
        result = evaluate(task)
        assert result["header"] == "TASK METRICS: OVER TARGET" and result["verdict"] == "WARN"
        assert result["summary"]["over_target"] == ["sql_revisions", "rounds.prompt"], result["summary"]["over_target"]
        with contextlib.redirect_stdout(io.StringIO()) as shown:
            code = main(["summary", "--task-dir", str(task), "--json"])
        assert code == 0 and json.loads(shown.getvalue())["verdict"] == "WARN"
        covered += 1
        # 4. bad input is refused and writes nothing
        before = metrics_path(task).read_bytes()
        for bad in (lambda: record_event(task, "release"), lambda: record_event(task, "platform_round", eval="prompt"),
                    lambda: record_event(task, "stage_start"), lambda: record_event(task, "precheck", at="yesterday"),
                    lambda: record_event(task, "platform_round", eval="golden", verdict="PASS"),
                    lambda: record_event(Path(tmp) / "missing", "precheck")):
            try:
                bad()
            except MetricsError:
                continue
            raise AssertionError("a bad event was accepted")
        assert metrics_path(task).read_bytes() == before
        with contextlib.redirect_stdout(io.StringIO()) as shown:
            code = main(["record", "--task-dir", str(task), "--event", "stage_end"])
        assert code == 1 and shown.getvalue().startswith("TASK METRICS (record): FAIL")
        from task_context import ContextError
        try:
            _atomic_write(WS / "Evals" / "never_written_by_task_metrics.json", b"{}", "a self-test probe")
        except ContextError:
            pass
        else:
            raise AssertionError("a write into Evals/ was not refused")
        covered += 1
        # 5. an unmatched stage end and an open stage are reported, not counted
        record_event(task, "stage_end", stage="oe", at=at)
        record_event(task, "stage_start", stage="rubric", at=at)
        s = summarise(task)
        assert s["open_stages"] == {"rubric": at} and any("without a start" in n for n in s["stage_notes"])
        covered += 1
        # 6. backfill of a synthetic archive: counters from files, a foreign report left out, nothing written
        arch = Path(tmp) / "arch_2026-11-01"
        ti = arch / "task_inputs"
        for rev, sql in (("rev1", "a"), ("rev2", "b"), ("rev3", "c")):
            (ti / "Working_Files" / "run_forensics" / rev).mkdir(parents=True)
            (ti / "Working_Files" / "run_forensics" / rev / SQL_NAME).write_text(sql)
        (ti / "Working_Files" / "run_forensics" / "rev2" / "precheck.node_verdicts.json").write_text("{}")
        (ti / "Working_Files" / "run_forensics" / "rev3" / "baseline").mkdir()
        (ti / "Working_Files" / "run_forensics" / "rev3" / "baseline2").mkdir()
        (ti / SQL_NAME).write_text("c")
        (ti / "06_PreCheck_Trajectory").mkdir()
        (ti / "06_PreCheck_Trajectory" / "trajectory.json").write_text("{}")
        (ti / "07_Baseline_Trajectories").mkdir()
        (ti / "07_Baseline_Trajectories" / "trajectory-run-1.json").write_text("{}")
        reports = arch / "eval_reports"
        reports.mkdir()
        own, other = "a" * 24, "b" * 24
        for name, verdict in ((f"{own}_1_prompt.md", "FAIL"), (f"{own}_1_prompt (1).md", "FAIL"),
                              (f"{own}_1_prompt-2.md", "PASS"), (f"{own}_3_rubric.md", "PASS"),
                              (f"{other}_3_rubric.md", "FAIL")):
            (reports / name).write_text(f"## REPORT {name}\n\n### FINAL VERDICT: {verdict}\n")
        (reports / f"{own}_1_prompt (copy).md").write_bytes((reports / f"{own}_1_prompt.md").read_bytes())
        listing = sorted((str(p), p.stat().st_mtime_ns) for p in arch.rglob("*"))
        back = backfill(arch)
        bs = back["summary"]
        assert (bs["sql_revisions"], bs["prechecks"], bs["baselines"]) == (3, 1, 2), bs
        assert bs["rounds"]["prompt"]["count"] == 3 and bs["rounds"]["rubric"] == {"count": 1, "verdicts": ["PASS"]}, bs
        assert bs["over_target"] == ["sql_revisions", "baselines", "rounds.prompt"], bs["over_target"]
        assert "carry platform id " + other in bs["basis"]["rounds"] and "identical to a report" in bs["basis"]["rounds"]
        assert back["header"] == "TASK METRICS (backfill arch_2026-11-01): OVER TARGET"
        assert listing == sorted((str(p), p.stat().st_mtime_ns) for p in arch.rglob("*")), "backfill wrote something"
        table = backfill_all(Path(tmp))
        assert [t["archive"] for t in table["tasks"]] == ["arch_2026-11-01", "task_inputsX"]
        assert "arch_2026-11-01" in render_table(table), render_table(table)
        assert table["header"].endswith("0 of 2 archived tasks within target; 1 store too little to tell"), table
        assert [c["status"] for c in table["checks"]] == ["WARN", "SKIP"], table["checks"]
        covered += 1
    print(f"self-test: ok ({covered} cases: empty task, append-only record and summary, over-target header, bad "
          "events and a write into Evals/ refused, stage time notes, backfill of a synthetic archive with a foreign "
          "report left out and nothing written)")
    return 0


# ---------------------------------------------------------------- command line

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        return _self_test()
    ap = argparse.ArgumentParser(prog="task_metrics.py", description="per-task counters and timeline (see the docstring)")
    sub = ap.add_subparsers(dest="command")
    rec = sub.add_parser("record", help="append one event to the task's log")
    rec.add_argument("--task-dir", required=True)
    rec.add_argument("--event", required=True, choices=EVENTS)
    rec.add_argument("--eval", choices=EVALS)
    rec.add_argument("--verdict")
    rec.add_argument("--stage")
    rec.add_argument("--note")
    rec.add_argument("--at", help="ISO time of the event (default: now, UTC)")
    rec.add_argument("--json", action="store_true")
    summ = sub.add_parser("summary", help="counters against the targets")
    summ.add_argument("--task-dir", required=True)
    summ.add_argument("--json", action="store_true")
    back = sub.add_parser("backfill", help="derive the counters for an archived task; writes nothing")
    back.add_argument("archive_dir")
    back.add_argument("--json", action="store_true")
    table = sub.add_parser("backfill-all", help="the table for every archived task")
    table.add_argument("--root", help="folder that holds the archived tasks (default: support/completed_tasks)")
    table.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if not args.command:
        ap.error("a command is required: record, summary, backfill or backfill-all")
    from task_context import ContextError
    try:
        if args.command == "record":
            if not Path(args.task_dir).is_dir():
                ap.error(f"task folder not found: {args.task_dir}")
            entry = record_event(args.task_dir, args.event, eval=args.eval, verdict=args.verdict, stage=args.stage,
                                 note=args.note, at=args.at)
            if args.json:
                print(json.dumps(entry, indent=1, sort_keys=True, ensure_ascii=False))
            else:
                extra = ", ".join(f"{k} {v}" for k, v in entry.items() if k not in CORE_FIELDS)
                print(f"task_metrics: recorded event {entry['n']} {entry['event']} at {entry['at']}"
                      + (f" ({extra})" if extra else ""))
            return 0
        if args.command == "summary":
            if not Path(args.task_dir).is_dir():
                ap.error(f"task folder not found: {args.task_dir}")
            result = evaluate(args.task_dir)
        elif args.command == "backfill":
            if not Path(args.archive_dir).is_dir():
                ap.error(f"archive folder not found: {args.archive_dir}")
            result = backfill(args.archive_dir)
        else:
            result = backfill_all(args.root)
            if args.json:
                print(json.dumps(result, indent=1, sort_keys=True, ensure_ascii=False))
            else:
                print(render_table(result))
            return 0
        print(json.dumps(result, indent=1, sort_keys=True, ensure_ascii=False) if args.json else render(result))
        return 1 if result["verdict"] == "FAIL" else 0
    except (MetricsError, ContextError, OSError) as exc:      # a bad event, a refused write, an unreadable file
        print(f"TASK METRICS ({args.command}): FAIL\n[FAIL] metrics.{args.command}: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

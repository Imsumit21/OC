#!/usr/bin/env python3
"""report_intake.py - take in a platform review report: check it belongs to this task, file it, scan it for rule
and release changes, count the round and pair it with the local prediction.

Plan: WS7 item 7 (refuse a report whose task id does not match the folder), WS0 item 2 (scan every new report),
WS5 item 5 (keep each local check with the hash of the bytes it read), WS8 item 2 (local verdict next to the
platform verdict on the same bytes).

What a platform report gives
  platform task id   the 24-hex prefix of the file name `<id>_<n>_<eval>[-round].md`, and "attempt <id>" inside
  eval kind          the `0_injection | 1_prompt | 1a_hardness | 2_oe | 3_rubric` part of the name, else the title
  verdict            the last `### FINAL VERDICT: PASS | NON-FAIL | FAIL` line, else the PASS/FAIL token of the name
  persona            the `### Persona:` / `### Assigned Persona:` line (prompt, OE and rubric reports)
  input hashes       a SHA-256 printed next to 04_Prompt.txt, 01_Universe_Inject.sql, 09_Rubrics.json or
                     08_Oracle_Events.md, and the lines "Reviewed prompt SHA-256", "Reviewed SQL sha256",
                     "Reviewed JSON SHA-256" (the rubric file). Reports abbreviate hashes; the prefix decides.

Commands
  intake REPORT --task-dir T [--eval injection|prompt|hardness|oe|rubric] [--rebind] [--dry-run] [--at ISO]
      1 identify   id, eval kind, verdict; a local review output (it carries the local bundle fingerprint) is refused
      2 bind       the first intake writes the id to Working_Files/platform_task.json. A later report with another id
                   is refused unless --rebind. A report naming another persona than the assignment is always refused.
                   Printed input hashes are compared with the task's files: current, an earlier stored copy
                   (Working_Files/run_forensics/**, check_history) or unknown. Hashes that match another
                   task_inputs* folder and not this one are refused.
      3 file       byte-for-byte copy into <T>/eval_reports/ under its own name; bytes already filed (under any
                   name) are a no-op; different bytes under the same name get a -dupN suffix; nothing is overwritten
      4 drift      release_drift `record` on the filed copy; anything new is printed with
                   "review before the next round of this eval"
      5 metrics    one platform_round event in Working_Files/task_metrics.json (once per report)
      6 pair       when a stored local check read the same bytes, the pair local verdict / platform verdict is recorded
      Header: REPORT INTAKE (<eval>): PASS|WARN|FAIL. WARN = taken in, with something to read (a new release or
      rule, input bytes not known in this folder). FAIL = refused; a refused report writes nothing. Taking in the
      same bytes again writes nothing either.
  snapshot --task-dir T --stage prompt-check|oe-check|rubric-check
      copies the current local check report to Working_Files/check_history/<stage>/<n>_<sha12 of the artifact>.md
      with a JSON sidecar (artifact, sha256, the other input hashes, the check's own prediction line)
  list --task-dir T    reports taken in, by eval and round, with verdicts
  --self-test

Writes: <T>/eval_reports/, <T>/Working_Files/platform_task.json, check_history/, task_metrics.json, and the
register references/platform_rule_delta.json through release_drift's own record path. Nothing else.

API: evaluate(task_dir, report, ...) decides without writing; intake(...), snapshot(...), list_reports(...),
read_report(path).

Exit: 0 PASS or WARN, 1 FAIL, 2 usage error. Stdlib only.
"""
from __future__ import annotations

import argparse
import contextlib
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

TOOL = "report_intake"
VERSION = 1
BIND_FILE = "platform_task.json"
BIND_SCHEMA = "platform-task-v1"
SNAPSHOT_SCHEMA = "check-snapshot-v1"
REPORTS_DIR = "eval_reports"
HISTORY_DIR = "check_history"
FORENSICS_DIR = "run_forensics"
ASSIGNMENT = "00_Assigments.md"
EVALS = ("injection", "prompt", "hardness", "oe", "rubric")
PROMPT, SQL, RUBRIC, OE = "04_Prompt.txt", "01_Universe_Inject.sql", "09_Rubrics.json", "08_Oracle_Events.md"
ARTIFACTS = (PROMPT, SQL, RUBRIC, OE)
STAGES = {
    "prompt-check": {"check": "04_Prompt_Check.md", "artifact": PROMPT, "eval": "prompt",
                     "line": re.compile(r"(?i)predicted\s+`?/prompt`?\s+band")},
    "oe-check": {"check": "08_OE_Check.md", "artifact": OE, "eval": "oe",
                 "line": re.compile(r"(?i)/oe`?\s+prediction")},
    "rubric-check": {"check": "09_Rubric_Check.md", "artifact": RUBRIC, "eval": "rubric",
                     "line": re.compile(r"(?i)readiness for\s+`?/rubric`?")},
}
STAGE_BY_EVAL = {cfg["eval"]: stage for stage, cfg in STAGES.items()}
MAX_STORED_BYTES = 32 * 1024 * 1024      # a stored copy larger than this is not hashed
MAX_DROPPED_HEADER_LINES = 8              # SQL forms tried: the file without its first 1..8 lines (hash_forms)
LEGACY_REPORT_DIRS = ("plateform_reports", "platform_reports", "plateform_report", "platform_report")

RX_NAME_ID = re.compile(r"^([0-9a-f]{24})_")
RX_ATTEMPT = re.compile(r"(?i)\battempt\b[^\n]{0,12}?(?<![0-9a-f])([0-9a-f]{24})(?![0-9a-f])")
RX_NAME_KIND = re.compile(r"(?i)(?:^|[_\s/])(0_injection|1_prompt|1a_hardness|1b_hardness|1b_haiku|2_oe|3_rubric)")
NAME_KIND = {"0_injection": "injection", "1_prompt": "prompt", "1a_hardness": "hardness", "1b_hardness": "hardness",
             "1b_haiku": "hardness", "2_oe": "oe", "3_rubric": "rubric"}
TITLE_KIND = (
    ("injection", re.compile(r"(?i)^#+\s*/injection\b|injection data-integrity review|INJECTION [A-Z ]*EVALUATION REPORT")),
    ("prompt", re.compile(r"(?i)^#+\s*/prompt\b|PROMPT EVALUATION REPORT")),
    ("hardness", re.compile(r"(?i)^#+\s*/hardness\b|^#+\s*hardness (?:review|eval|report)|HARDNESS EVALUATION REPORT|"
                            r"haiku prediction")),
    ("oe", re.compile(r"(?i)^#+\s*/oe\b|\bOE EVALUATION REPORT|ORACLE EVENTS? EVALUATION REPORT")),
    ("rubric", re.compile(r"(?i)^#+\s*/rubric\b|RUBRIC EVALUATION REPORT")),
)
SPEC_KIND = {"0_Injection_Quality_Eval": "injection", "1_Prompt_Eval": "prompt", "1A_Hardness_Eval": "hardness",
             "1B_Haiku_Prediction_Eval": "hardness", "2_Oracle_Events_Eval": "oe", "3_Rubrics_Eval": "rubric"}
RX_SPEC_KIND = re.compile(r"Evals/(" + "|".join(SPEC_KIND) + r")\.md")
RX_VERDICT = re.compile(r"(?m)^\s*#{1,6}\s*FINAL VERDICT:\s*\**\s*(NON-FAIL|PASS|FAIL)\b")
RX_NAME_VERDICT = re.compile(r"_(PASS|FAIL|NONFAIL)\d*(?=[_.]|$)")
RX_PERSONA = re.compile(r"(?m)^#{1,6}\s*(?:Assigned\s+)?Persona:\s*(.+)$")
RX_DATE = re.compile(r"(?i)\breview(?:ed| time| date)\b[^0-9\n]{0,12}(20\d\d-\d\d-\d\d)")
_HASH = r"\W{0,6}?([0-9a-f]{8,64})(?:(?:…|\.\.\.)([0-9a-f]{0,64}))?"
RX_SHA = re.compile(r"(?i)sha-?256" + _HASH)
LABELLED = (
    (PROMPT, re.compile(r"(?i)\breviewed prompt sha-?256" + _HASH)),
    (SQL, re.compile(r"(?i)\bSQL sha-?256" + _HASH)),
    (RUBRIC, re.compile(r"(?i)\breviewed JSON sha-?256" + _HASH)),
    (OE, re.compile(r"(?i)\breviewed (?:OEs?|oracle events) sha-?256" + _HASH)),
)
RX_PREDICTION = re.compile(r"NON-FAIL(?:-RISK)?|FAIL(?:-RISK)?|PASS|CLEAN")
PREDICTION_VERDICT = {"PASS": "PASS", "CLEAN": "PASS", "NON-FAIL": "NON-FAIL", "NON-FAIL-RISK": "NON-FAIL",
                      "FAIL": "FAIL", "FAIL-RISK": "FAIL"}
DRIFT_LABEL = {"release": "new release", "spec_hash": "new spec hash", "versioned_id": "unknown rule id",
               "evals_path": "unknown file", "tool_command": "unknown tool command",
               "check_name": "possible check name"}
REVIEW_LINE = "review before the next round of this eval"


class IntakeError(ValueError):
    """The request cannot be carried out (bad folder, unreadable file)."""


# ---------------------------------------------------------------- small helpers

def _slot(task_dir, name) -> Path:
    from stage_gate import slot_path
    return slot_path(task_dir, name)


def _sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha_file(path) -> str:
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


def _json_bytes(doc) -> bytes:
    return (json.dumps(doc, indent=1, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def _rel(path, base) -> str:
    try:
        return Path(path).resolve().relative_to(Path(base).resolve()).as_posix()
    except ValueError:
        return str(path)


def _check(checks, check_id, status, detail) -> None:
    checks.append({"id": check_id, "status": status, "detail": " ".join(str(detail).split())})


def _verdict(checks, accepted=True) -> str:
    """FAIL when refused; WARN when taken in with a warning (a new release, unknown input bytes); else PASS."""
    if not accepted or any(c["status"] == "FAIL" for c in checks):
        return "FAIL"
    return "WARN" if any(c["status"] == "WARN" for c in checks) else "PASS"


def _first_word(text) -> str:
    words = re.findall(r"[^\W\d_]+", str(text))
    return words[0].casefold() if words else ""


# ---------------------------------------------------------------- reading a report

def eval_from_name(name):
    found = RX_NAME_KIND.search(name)
    return NAME_KIND[found.group(1).lower()] if found else None


def eval_from_text(text):
    head = text.splitlines()[:40]
    for kind, rx in TITLE_KIND:
        if any(rx.search(line) for line in head):
            return kind
    found = RX_SPEC_KIND.search(text)
    return SPEC_KIND[found.group(1)] if found else None


def input_hashes(text) -> dict:
    """{artifact file: [cited hash, ...]} in the order the report prints them; the first is the one it ran on."""
    out = {name: [] for name in ARTIFACTS}

    def add(name, prefix, suffix, number):
        if not any(item["prefix"][:8] == prefix[:8] for item in out[name]):
            out[name].append({"prefix": prefix, "suffix": suffix or "", "line": number})

    for number, line in enumerate(text.splitlines(), 1):
        low = line.lower()
        if "sha" not in low:
            continue
        for name in ARTIFACTS:
            start = 0
            while True:
                at = line.find(name, start)
                if at < 0:
                    break
                start = at + len(name)
                # The hash belongs to the file when it follows the name inside the same clause or table cell.
                segment = re.split(r"[;|]", line[start:start + 260], 1)[0]
                found = RX_SHA.search(segment)
                if found:
                    add(name, found.group(1), found.group(2), number)
        for name, rx in LABELLED:
            for found in rx.finditer(line):
                add(name, found.group(1), found.group(2), number)
    return {name: items for name, items in out.items() if items}


def read_report(path) -> dict:
    """Everything this tool takes from one report file. Reads only."""
    path = Path(path)
    data = path.read_bytes()
    text = data.decode("utf-8", errors="replace")
    by_name, by_text = eval_from_name(path.name), eval_from_text(text)
    name_id = RX_NAME_ID.match(path.name)
    verdicts = RX_VERDICT.findall(text)
    name_verdict = RX_NAME_VERDICT.search(path.name)
    if verdicts:
        verdict, source = verdicts[-1], "FINAL VERDICT line"
    elif name_verdict:
        verdict, source = name_verdict.group(1).replace("NONFAIL", "NON-FAIL"), "file name"
    else:
        verdict, source = "UNKNOWN", None
    persona = RX_PERSONA.search(text)
    dates = RX_DATE.findall(text)
    return {"name": path.name, "path": str(path), "bytes": len(data), "sha256": _sha_bytes(data),
            "mtime": path.stat().st_mtime, "text": text,
            "name_id": name_id.group(1) if name_id else None,
            "printed_ids": sorted(set(RX_ATTEMPT.findall(text))),
            "eval": by_name or by_text, "eval_by_name": by_name, "eval_by_text": by_text,
            "verdict": verdict, "verdict_source": source,
            "persona": " ".join(persona.group(1).split()) if persona else None,
            "review_date": dates[0] if dates else None,
            "input_hashes": input_hashes(text)}


def _public(rep) -> dict:
    return {k: v for k, v in rep.items() if k not in ("text", "path", "mtime")}


# ---------------------------------------------------------------- the task folder

def load_binding(task_dir):
    path = _slot(task_dir, BIND_FILE)
    if not path.is_file():
        return None
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise IntakeError(f"cannot read {path}: {exc}")
    if not isinstance(doc, dict) or doc.get("schema") != BIND_SCHEMA or "platform_task_id" not in doc:
        raise IntakeError(f"{path} is not a {BIND_SCHEMA} file; keep it and fix it by hand")
    doc.setdefault("reports", [])
    doc.setdefault("history", [])
    return doc


def filed_ids(task_dir) -> dict:
    """Platform ids carried by report files already in the task's report folders: {id: count}."""
    counts = {}
    for name in (REPORTS_DIR,) + LEGACY_REPORT_DIRS:
        folder = Path(task_dir) / name
        if not folder.is_dir():
            continue
        for item in folder.iterdir():
            found = RX_NAME_ID.match(item.name) if item.is_file() and item.suffix == ".md" else None
            if found:
                counts[found.group(1)] = counts.get(found.group(1), 0) + 1
    return counts


def assigned_persona(task_dir):
    """The persona name in the task's assignment, or None when it cannot be read."""
    path = Path(task_dir) / ASSIGNMENT
    if not path.is_file():
        return None
    try:
        from task_context import parse_assignment
        return parse_assignment(path.read_text(encoding="utf-8"))[0].get("persona_name")
    except Exception:           # a V2 or unfinished assignment: the persona check is skipped, never guessed
        return None


def hash_forms(data: bytes, name) -> dict:
    """{sha256: form} for the byte forms the platform is known to hash besides the file itself.

    Seen in the stored reports (2026-11-11 backtest): the prompt is hashed with one final newline added
    (Leonard 424c70d3 is 04_Prompt.txt 45766344 plus a newline), and the SQL without its leading header lines
    (S2 8293d811 is the rev7 SQL without its first 6 lines; Leonard 9b02cc8f without its first 4)."""
    forms = {_sha_bytes(data): "file"}
    body = data.rstrip()
    for variant, form in ((body + b"\n", "with one final newline"), (body, "without the final newline")):
        forms.setdefault(_sha_bytes(variant), form)
    if name == SQL:
        lines = data.split(b"\n")
        for k in range(1, min(MAX_DROPPED_HEADER_LINES, len(lines) - 1) + 1):
            forms.setdefault(_sha_bytes(b"\n".join(lines[k:])), f"without its first {k} lines")
    return forms


def _stored(path, name, kind, where) -> dict:
    data = Path(path).read_bytes()
    forms = hash_forms(data, name)
    return {"sha256": _sha_bytes(data), "kind": kind, "where": where, "forms": forms}


def stored_hashes(task_dir) -> dict:
    """{artifact file: [{sha256, where, kind, forms}]}: the current file, earlier copies in run_forensics, and the
    hashes earlier check snapshots recorded. `forms` maps each hash the platform may print for those bytes to its
    form (see hash_forms)."""
    task_dir = Path(task_dir)
    out = {name: [] for name in ARTIFACTS}
    for name in ARTIFACTS:
        current = _slot(task_dir, name)
        if current.is_file():
            out[name].append(_stored(current, name, "current", "current"))
    forensics = _slot(task_dir, FORENSICS_DIR)
    if forensics.is_dir():
        for name in ARTIFACTS:
            stem, suffix = name.rsplit(".", 1)
            for item in sorted(forensics.rglob(stem + "*." + suffix)):
                if item.is_file() and not item.is_symlink() and item.stat().st_size <= MAX_STORED_BYTES:
                    out[name].append(_stored(item, name, "earlier", _rel(item, _slot(task_dir, FORENSICS_DIR).parent)))
    history = _slot(task_dir, HISTORY_DIR)
    if history.is_dir():
        for side in sorted(history.glob("*/*.json")):
            try:
                doc = json.loads(side.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            hashes = dict(doc.get("context") or {})
            if doc.get("artifact") and doc.get("artifact_sha256"):
                hashes[doc["artifact"]] = doc["artifact_sha256"]
            forms = doc.get("forms") or {}
            for name, digest in hashes.items():
                if name in out and isinstance(digest, str):
                    known = forms.get(name) if isinstance(forms.get(name), dict) else {}
                    out[name].append({"sha256": digest, "kind": "earlier", "forms": dict(known, **{digest: "file"}),
                                      "where": f"check snapshot {doc.get('stage')} #{doc.get('n')}"})
    return out


def _form_of(prefix, entry):
    """The form under which a stored entry has this hash prefix, or None."""
    forms = entry.get("forms") or {entry["sha256"]: "file"}
    return next((form for digest, form in forms.items() if digest.startswith(prefix)), None)


def _match(cited, stored):
    """The stored entry a cited hash stands for (current first, then earlier copies), with the form that matched."""
    hits = [dict(s, form=_form_of(cited["prefix"], s)) for s in stored]
    hits = [h for h in hits if h["form"]]
    hits.sort(key=lambda s: (s["kind"] != "current", s["form"] != "file"))
    return hits[0] if hits else None


def other_task_dirs(task_dir, tasks_root) -> list:
    here = Path(task_dir).resolve()
    return [p for p in sorted(Path(tasks_root).glob("task_inputs*")) if p.is_dir() and p.resolve() != here]


def where_ran(rep, own, task_dir, tasks_root) -> dict:
    """Per artifact file the report prints a hash for: current, earlier, unknown, or another task folder.
    `own` is stored_hashes(task_dir)."""
    others = None
    out = {}
    for name, cited in rep["input_hashes"].items():
        first = cited[0]
        shown = first["prefix"][:12] + ("…" if len(first["prefix"]) < 64 else "")
        hit = _match(first, own[name])
        if hit:
            out[name] = {"cited": shown, "ran_on": hit["kind"], "where": hit["where"], "form": hit["form"]}
            continue
        if others is None:
            others = {str(p): stored_hashes(p) for p in other_task_dirs(task_dir, tasks_root)}
        foreign = next(((folder, m) for folder, hashes in others.items()
                        for m in [_match(first, hashes[name])] if m), None)
        if foreign:
            out[name] = {"cited": shown, "ran_on": "other_task", "where": foreign[1]["where"],
                         "folder": foreign[0], "form": foreign[1]["form"]}
        else:
            out[name] = {"cited": shown, "ran_on": "unknown", "where": None}
    return out


# ---------------------------------------------------------------- local check snapshots

def prediction_of(stage, text) -> dict:
    """The check's own readiness or prediction line and the verdict it states."""
    rx = STAGES[stage]["line"]
    for number, line in enumerate(text.splitlines(), 1):
        found = rx.search(line)
        if not found:
            continue
        token = RX_PREDICTION.search(line[found.end():].upper())
        return {"line": " ".join(line.split())[:300], "line_number": number,
                "verdict": PREDICTION_VERDICT[token.group(0)] if token else "UNKNOWN"}
    return {"line": None, "line_number": None, "verdict": "UNKNOWN"}


def snapshots(task_dir, stage) -> list:
    folder = _slot(task_dir, HISTORY_DIR) / stage
    out = []
    if folder.is_dir():
        for side in folder.glob("*.json"):
            try:
                doc = json.loads(side.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if doc.get("schema") == SNAPSHOT_SCHEMA and isinstance(doc.get("n"), int):
                out.append(doc)
    return sorted(out, key=lambda d: d["n"])


def next_snapshot_number(folder, earlier) -> int:
    """One more than any number used so far, by a sidecar or by a file name, so no stored copy is ever replaced."""
    used = [d["n"] for d in earlier]
    if Path(folder).is_dir():
        used += [int(m.group(1)) for p in Path(folder).iterdir() for m in [re.match(r"^(\d+)_", p.name)] if m]
    return max(used, default=0) + 1


def snapshot(task_dir, stage, at=None) -> dict:
    """Store the current local check report with the hash of the artifact it checked."""
    task_dir = Path(task_dir)
    checks = []
    if stage not in STAGES:
        raise IntakeError(f"unknown stage {stage!r}; use one of: {', '.join(STAGES)}")
    cfg = STAGES[stage]
    check_file, artifact = _slot(task_dir, cfg["check"]), _slot(task_dir, cfg["artifact"])
    result = {"tool": TOOL, "version": VERSION, "verdict": "FAIL", "bound_to": {}, "checks": checks,
              "command": "snapshot", "stage": stage}
    if not check_file.is_file() or not artifact.is_file():
        missing = [p.name for p in (check_file, artifact) if not p.is_file()]
        _check(checks, "snapshot.inputs", "FAIL", f"missing in {task_dir.name}: {', '.join(missing)}. Run the "
               f"{stage} first, then snapshot it.")
        return result
    check_bytes = check_file.read_bytes()
    art_sha, check_sha = _sha_file(artifact), _sha_bytes(check_bytes)
    context = {name: _sha_file(_slot(task_dir, name)) for name in ARTIFACTS
               if name != cfg["artifact"] and _slot(task_dir, name).is_file()}
    forms = {name: {digest: form for digest, form in hash_forms(_slot(task_dir, name).read_bytes(), name).items()
                    if form != "file"}
             for name in [cfg["artifact"]] + sorted(context)}
    prediction = prediction_of(stage, check_bytes.decode("utf-8", errors="replace"))
    result["bound_to"] = {_rel(artifact, task_dir): art_sha, _rel(check_file, task_dir): check_sha}
    earlier = snapshots(task_dir, stage)
    last = earlier[-1] if earlier else None
    if last and (last.get("artifact_sha256"), last.get("check_sha256"), last.get("context")) == \
            (art_sha, check_sha, context):
        _check(checks, "snapshot.store", "PASS", f"unchanged since snapshot {last['n']} ({last['snapshot']}); "
               "nothing written")
        result.update(verdict="PASS", snapshot=last, created=False)
        return result
    folder = _slot(task_dir, HISTORY_DIR) / stage
    number = next_snapshot_number(folder, earlier)
    copy = folder / f"{number}_{art_sha[:12]}.md"
    side = {"schema": SNAPSHOT_SCHEMA, "stage": stage, "eval": cfg["eval"], "n": number,
            "artifact": cfg["artifact"], "artifact_sha256": art_sha,
            "check_file": _rel(check_file, task_dir), "check_sha256": check_sha, "context": context,
            "forms": forms, "prediction": prediction, "snapshot": _rel(copy, task_dir)}
    import task_metrics
    task_metrics.load_events(task_dir)          # an unreadable log stops the snapshot before anything is written
    _atomic_write(copy, check_bytes, "the local check snapshot")
    _atomic_write(copy.with_suffix(".json"), _json_bytes(side), "the local check snapshot sidecar")
    _check(checks, "snapshot.store", "PASS", f"{cfg['check']} stored as {side['snapshot']} for {cfg['artifact']} "
           f"{art_sha[:12]}")
    if prediction["verdict"] == "UNKNOWN":
        _check(checks, "snapshot.prediction", "WARN", "no readiness or prediction line with PASS, NON-FAIL, FAIL or "
               "CLEAN found in the check; the pair with the platform verdict will read UNKNOWN")
    else:
        _check(checks, "snapshot.prediction", "PASS", f"the check predicts {prediction['verdict']} (line "
               f"{prediction['line_number']}: {prediction['line'][:120]})")
    names_bytes = art_sha[:12] in check_bytes.decode("utf-8", errors="replace")
    if not names_bytes and check_file.stat().st_mtime < artifact.stat().st_mtime:
        _check(checks, "snapshot.fresh", "WARN", f"{cfg['check']} is older than {cfg['artifact']} and does not name "
               f"its hash {art_sha[:12]}: it may describe earlier bytes. Re-run the check, then snapshot again.")
    else:
        _check(checks, "snapshot.fresh", "PASS", f"the check {'names the hash of' if names_bytes else 'is newer than'}"
               f" {cfg['artifact']}")
    event = task_metrics.record_event(task_dir, "local_check", stage=stage, eval=cfg["eval"],
                                      verdict=prediction["verdict"], at=at, artifact_sha256=art_sha,
                                      snapshot=side["snapshot"])
    _check(checks, "metrics.local_check", "PASS", f"event {event['n']} appended to task_metrics.json")
    result.update(verdict="WARN" if any(c["status"] == "WARN" for c in checks) else "PASS", snapshot=side,
                  created=True)
    return result


def _snapshot_read(snap, name, prefix) -> bool:
    """True when the stored check read bytes of `name` whose hash, in any form the platform prints, has this prefix."""
    raw = snap.get("artifact_sha256") if name == snap.get("artifact") else (snap.get("context") or {}).get(name)
    forms = (snap.get("forms") or {}).get(name) or {}
    return any(isinstance(d, str) and d.startswith(prefix) for d in [raw] + list(forms))


def find_pair(task_dir, rep, kind) -> dict:
    """The stored local check that read the bytes this report was run on, if there is one."""
    stage = STAGE_BY_EVAL.get(kind)
    if not stage:
        return {"status": "SKIP", "detail": f"/{kind} has no local check stage to pair with"}
    artifact = STAGES[stage]["artifact"]
    stored = snapshots(task_dir, stage)
    if not stored:
        return {"status": "SKIP", "detail": f"no stored {stage} for this task; run `report_intake.py snapshot "
                f"--stage {stage}` before each platform round so the local prediction can be compared"}
    cited = rep["input_hashes"].get(artifact)
    if cited:
        prefix, basis = cited[0]["prefix"], "hash_printed"
    else:
        current = _slot(task_dir, artifact)
        if not current.is_file():
            return {"status": "SKIP", "detail": f"the report prints no {artifact} hash and the file is missing"}
        prefix, basis = _sha_file(current), "current_bytes_assumed"
    same = [s for s in stored if _snapshot_read(s, artifact, prefix)]
    if not same:
        return {"status": "SKIP", "detail": f"no stored {stage} read {artifact} {prefix[:12]}"}
    # The other inputs must agree too wherever both sides state them: a /prompt verdict depends on the SQL as well.
    for snap in reversed(same):
        clash = [name for name, items in rep["input_hashes"].items()
                 if name != artifact and name in (snap.get("context") or {})
                 and not _snapshot_read(snap, name, items[0]["prefix"])]
        if clash:
            continue
        local = snap["prediction"]["verdict"]
        note = "" if basis == "hash_printed" else f" (the report prints no {artifact} hash; current bytes assumed)"
        return {"status": "PASS", "local_verdict": local, "local_snapshot": snap["snapshot"], "pair_basis": basis,
                "agree": local == rep["verdict"],
                "detail": f"local {stage} #{snap['n']} predicted {local}, the platform says {rep['verdict']} on "
                          f"{artifact} {prefix[:12]}{note}: "
                          + ("they agree" if local == rep["verdict"] else "they differ")}
    return {"status": "SKIP", "detail": f"the stored {stage} read the same {artifact} but another revision of "
            + ", ".join(sorted({n for s in same for n in (s.get('context') or {}) if n in rep['input_hashes']}))}


# ---------------------------------------------------------------- deciding (no writes)

def _local_fingerprint(register):
    try:
        import release_drift
        reg = release_drift.load_register(register or release_drift.REGISTER)
        return (reg.get("local_bundle") or {}).get("fingerprint")
    except (SystemExit, OSError, ValueError):
        return None


def evaluate(task_dir, report, eval_kind=None, rebind=False, tasks_root=None, register=None) -> dict:
    """Decide whether the report may be taken into the task folder. Reads only."""
    return _decide(task_dir, report, eval_kind, rebind, tasks_root, register)[0]


def _decide(task_dir, report, eval_kind=None, rebind=False, tasks_root=None, register=None) -> tuple:
    """(the decision object, the parsed report)."""
    task_dir, report = Path(task_dir), Path(report)
    tasks_root = Path(tasks_root) if tasks_root else BUNDLE
    if not task_dir.is_dir():
        raise IntakeError(f"task folder not found: {task_dir}")
    if not report.is_file():
        raise IntakeError(f"report file not found: {report}")
    rep = read_report(report)
    checks = []
    folder = task_dir.name
    # 1. identify
    kind = (eval_kind or rep["eval"] or "").lstrip("/").lower() or None
    if eval_kind and rep["eval"] and rep["eval"] != kind:
        _check(checks, "report.eval", "FAIL", f"--eval {kind} was given, but the report reads as a /{rep['eval']} "
               "report (file name or title). Check the file.")
    elif kind not in EVALS:
        _check(checks, "report.eval", "FAIL", "the eval kind is not in the file name or the title; pass --eval "
               "injection|prompt|hardness|oe|rubric")
        kind = None
    else:
        _check(checks, "report.eval", "PASS", f"/{kind} report, {rep['bytes']} bytes, sha256 {rep['sha256'][:12]}")
    if rep["verdict"] == "UNKNOWN":
        _check(checks, "report.verdict", "WARN", "no `FINAL VERDICT:` line and no verdict in the file name; the round "
               "is recorded as UNKNOWN")
    else:
        _check(checks, "report.verdict", "PASS", f"{rep['verdict']} ({rep['verdict_source']})")
    fingerprint = _local_fingerprint(register)
    if fingerprint and fingerprint in rep["text"]:
        _check(checks, "report.platform", "FAIL", f"this is a local review output (it carries the local bundle "
               f"fingerprint {fingerprint}), not a platform report. Local rehearsals are never recorded as a "
               "platform round.")
    own = stored_hashes(task_dir)
    ran = where_ran(rep, own, task_dir, tasks_root)
    proven = [name for name, r in ran.items() if r["ran_on"] in ("current", "earlier")]
    ids = set(rep["printed_ids"])
    report_id = rep["name_id"] or (rep["printed_ids"][0] if len(ids) == 1 else None)
    if rep["name_id"] and ids and rep["name_id"] not in ids:
        _check(checks, "report.id", "FAIL", f"the file name carries platform task id {rep['name_id']} but the report "
               f"prints attempt {', '.join(sorted(ids))}. Keep the name the platform gave the file.")
        report_id = None
    elif not rep["name_id"] and len(ids) > 1:
        _check(checks, "report.id", "FAIL", f"the report prints {len(ids)} attempt ids ({', '.join(sorted(ids))}) and "
               "the file name carries none. Keep the name the platform gave the file.")
    elif report_id:
        source = "file name" + (" and report text" if rep["name_id"] in ids else "") if rep["name_id"] \
            else "report text"
        _check(checks, "report.id", "PASS", f"platform task id {report_id} ({source})")
    elif proven:
        _check(checks, "report.id", "WARN", "no platform task id in the file name or the report; accepted because "
               f"its printed {', '.join(proven)} hash matches this folder")
    else:
        _check(checks, "report.id", "FAIL", "no platform task id in the file name or the report, and no printed "
               "input hash matches this folder: nothing ties it to this task. Keep the platform's file name "
               "`<24-hex id>_<n>_<eval>.md`.")
    # 2. bind
    binding = load_binding(task_dir)
    bound = binding["platform_task_id"] if binding else None
    implied = None
    if not bound:
        counts = filed_ids(task_dir)
        implied = max(sorted(counts), key=lambda k: counts[k]) if counts else None
    expected = bound or implied
    action = None
    if report_id and not expected:
        action = "bind"
        if proven:
            _check(checks, "bind.task_id", "PASS", f"first report for {folder}: the folder will be bound to "
                   f"{report_id} (its printed {', '.join(proven)} hash matches this folder)")
        else:
            _check(checks, "bind.task_id", "WARN", f"first report for {folder}: the folder will be bound to "
                   f"{report_id}, but no input hash it prints matches a file in this folder, so nothing proves the "
                   "id is this task's. Check the id against the platform before taking in more reports.")
    elif report_id and report_id == expected:
        action = None if bound else "bind"
        _check(checks, "bind.task_id", "PASS", f"{report_id} is the id {folder} is bound to" if bound else
               f"{report_id} is the id the reports already in {folder}/{REPORTS_DIR} carry; the folder will be "
               "bound to it")
    elif report_id and rebind:
        action = "rebind"
        _check(checks, "bind.task_id", "WARN", f"--rebind: {folder} was bound to {expected}; it will be bound to "
               f"{report_id}")
    elif report_id:
        basis = "is bound to" if bound else "already holds reports of"
        _check(checks, "bind.task_id", "FAIL", f"this report belongs to platform task {report_id}, but folder "
               f"{folder} {basis} {expected}. It was not filed. Take it into its own task folder, or pass "
               "--rebind if the platform task for this folder really changed.")
    else:
        _check(checks, "bind.task_id", "SKIP", "no platform task id to compare")
    assigned = assigned_persona(task_dir)
    if rep["persona"] and assigned:
        if _first_word(rep["persona"]) == _first_word(assigned):
            _check(checks, "bind.persona", "PASS", f"the report is for {rep['persona'].split(' - ')[0]}, the "
                   "assigned persona")
        else:
            _check(checks, "bind.persona", "FAIL", f"the report is for persona \"{rep['persona']}\", but {folder} "
                   f"is assigned to {assigned}. It was not filed; --rebind does not override this.")
    else:
        _check(checks, "bind.persona", "SKIP", "the report prints no persona line" if not rep["persona"]
               else f"no V3 assignment in {folder} to compare with")
    if not ran:
        _check(checks, "bind.hashes", "SKIP", "the report prints no input hash, so the bytes it ran on are not known")
    else:
        parts, status = [], "PASS"
        for name in ARTIFACTS:
            if name not in ran:
                continue
            r = ran[name]
            form = f", {r['form']}" if r.get("form") not in (None, "file") else ""
            if r["ran_on"] == "current":
                parts.append(f"{name} {r['cited']} = the current file{form}")
            elif r["ran_on"] == "earlier":
                parts.append(f"{name} {r['cited']} = an earlier stored copy ({r['where']}{form})")
                status = "WARN" if status == "PASS" else status
            elif r["ran_on"] == "unknown":
                parts.append(f"{name} {r['cited']} = unknown (not the current file and not stored in this folder)")
                status = "WARN" if status == "PASS" else status
            else:
                parts.append(f"{name} {r['cited']} = {Path(r['folder']).name} ({r['where']}{form}), not this folder")
                status = "FAIL"
        tail = ""
        if status == "FAIL":
            tail = ". The report was run on another task's files. It was not filed."
        elif status == "WARN":
            tail = ". The findings may not describe the current files."
        _check(checks, "bind.hashes", status, "the report ran on: " + "; ".join(parts) + tail)
    accepted = not any(c["status"] == "FAIL" for c in checks)
    bound_to = {name: s["sha256"] for name in ARTIFACTS for s in own[name][:1] if s["kind"] == "current"}
    return {"tool": TOOL, "version": VERSION, "verdict": _verdict(checks, accepted), "bound_to": bound_to,
            "checks": checks, "command": "intake", "eval": kind, "accepted": accepted, "action": action,
            "platform_task_id": report_id, "bound_before": bound, "report": _public(rep), "ran_on": ran}, rep


# ---------------------------------------------------------------- taking a report in (writes)

def filed_copy(task_dir, sha256):
    """The file in <task>/eval_reports/ that holds exactly these bytes, under any name, or None."""
    folder = Path(task_dir) / REPORTS_DIR
    if not folder.is_dir():
        return None
    for item in sorted(folder.iterdir()):
        if item.is_file() and not item.is_symlink() and _sha_file(item) == sha256:
            return item
    return None


def _file_report(task_dir, rep) -> tuple:
    """(path the report is filed at, what happened). Never overwrites; the same bytes are never filed twice."""
    folder = Path(task_dir) / REPORTS_DIR
    source = Path(rep["path"])
    same = filed_copy(task_dir, rep["sha256"])
    if same is not None:
        return same, "already filed" + ("" if same.name == source.name else f" (as {same.name})")
    data = source.read_bytes()
    stem, suffix = source.name.rsplit(".", 1) if "." in source.name else (source.name, "md")
    number = 0
    while True:
        target = folder / (source.name if not number else f"{stem}-dup{number}.{suffix}")
        if not os.path.lexists(target):
            if _sha_bytes(data) != rep["sha256"]:
                raise IntakeError(f"{source} changed while it was being read; take it in again")
            _atomic_write(target, data, "the filed platform report")
            if _sha_file(target) != rep["sha256"]:
                raise IntakeError(f"copy of {source.name} does not read back with the same bytes")
            return target, "filed" if not number else "filed under a new name"
        number += 1


def _record_drift(filed, register, repo, today) -> dict:
    """Run release_drift's own `record` on the filed report and return what it says is new."""
    import release_drift
    argv = ["record", str(filed), "--json"]
    if register:
        argv += ["--register", str(register)]
    if repo:
        argv += ["--repo", str(repo)]
    if today:
        argv += ["--today", str(today)]
    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer):
            release_drift.main(argv)
        out = json.loads(buffer.getvalue())
    except SystemExit as exc:
        return {"error": str(exc) or "release_drift stopped"}
    except (ValueError, OSError) as exc:
        return {"error": f"release_drift output could not be read: {exc}"}
    new = [item for result in out.get("results", []) for item in result.get("new", [])]
    return {"new": new, "already_recorded": bool(out.get("already_recorded")),
            "skipped_local": bool(out.get("skipped_local")),
            "register": str(register or release_drift.REGISTER)}


def intake(task_dir, report, eval_kind=None, rebind=False, tasks_root=None, register=None, repo=None, today=None,
           at=None, dry_run=False) -> dict:
    """Take one platform report into the task folder. A refused report writes nothing."""
    task_dir = Path(task_dir)
    result, rep = _decide(task_dir, report, eval_kind, rebind, tasks_root, register)
    checks, kind = result["checks"], result["eval"]
    if not result["accepted"] or dry_run:
        if dry_run and result["accepted"]:
            _check(checks, "file.copy", "SKIP", "--dry-run: nothing was written")
        return result
    # Every file this intake writes is checked before the first write, so a bad log or a read-only target refuses
    # the report with nothing written.
    import task_metrics
    from task_context import refuse_read_only
    task_metrics.load_events(task_dir)
    for path, what in ((task_dir / REPORTS_DIR, "the platform report folder"),
                       (_slot(task_dir, BIND_FILE), "the platform task binding"),
                       (task_metrics.metrics_path(task_dir), "the task metrics log")):
        refuse_read_only(path, what)
    # 3. file
    filed, how = _file_report(task_dir, rep)
    filed_rel = _rel(filed, task_dir)
    _check(checks, "file.copy", "PASS", f"{how}: {filed_rel} ({rep['bytes']} bytes, identical to the source)")
    result["filed_as"] = filed_rel
    result["bound_to"][filed_rel] = rep["sha256"]
    stored = load_binding(task_dir)
    before = _json_bytes(stored) if stored else None
    binding = stored or {"schema": BIND_SCHEMA, "platform_task_id": None, "reports": [], "history": []}
    known = next((r for r in binding["reports"] if r["sha256"] == rep["sha256"]), None)
    # 4. drift
    drift = _record_drift(filed, register, repo, today)
    result["drift"] = drift
    if drift.get("error"):
        _check(checks, "drift.record", "WARN", f"the report is filed but release_drift did not record it: "
               f"{drift['error']}. Run `release_drift.py record {filed_rel}` by hand.")
    elif drift["skipped_local"]:
        _check(checks, "drift.record", "WARN", "release_drift read the file as a local review output and skipped it")
    else:
        hard = [i for i in drift["new"] if i["kind"] != "check_name"]
        soft = [i for i in drift["new"] if i["kind"] == "check_name"]
        if hard:
            shown = "; ".join(f"{DRIFT_LABEL.get(i['kind'], i['kind'])} {i['name']} ({i['at']})" for i in hard)
            _check(checks, "drift.new", "WARN", f"{len(hard)} new in this report: {shown}. Added to the register "
                   f"as unreviewed: {REVIEW_LINE} (/{kind}).")
        else:
            state = "was already in the register" if drift["already_recorded"] else "recorded in the register"
            _check(checks, "drift.new", "PASS", f"{state}; no new release, spec hash, rule id, file or tool command")
        if soft:
            _check(checks, "drift.check_names", "PASS", f"{len(soft)} possible check name(s) noted for review: "
                   + ", ".join(i["name"] for i in soft))
    # 6. pair (found before the metrics event so the event can carry it)
    pair = find_pair(task_dir, rep, kind)
    result["pair"] = {k: v for k, v in pair.items() if k not in ("status", "detail")}
    # 5. metrics
    if known:
        round_number = known["round"]
        _check(checks, "metrics.platform_round", "PASS", f"already counted as /{kind} round {round_number}; no new "
               "event")
    else:
        round_number = sum(1 for r in binding["reports"] if r["eval"] == kind) + 1
        extra = {k: pair[k] for k in ("local_verdict", "local_snapshot", "pair_basis") if k in pair}
        event = task_metrics.record_event(
            task_dir, "platform_round", eval=kind, verdict=rep["verdict"], at=at, report=filed.name,
            report_sha256=rep["sha256"], platform_task_id=result["platform_task_id"], round=round_number,
            ran_on={name: r["ran_on"] for name, r in result["ran_on"].items()} or None, **extra)
        _check(checks, "metrics.platform_round", "PASS", f"/{kind} round {round_number} ({rep['verdict']}) appended "
               f"to task_metrics.json as event {event['n']}")
    _check(checks, "pair.local", pair["status"], pair["detail"])
    result["round"] = round_number
    # the binding and the intake list, written last so a failure above leaves no half-recorded report
    new_id = result["platform_task_id"]
    if new_id and new_id != binding["platform_task_id"]:
        if binding["platform_task_id"]:
            binding["history"].append({"platform_task_id": binding["platform_task_id"], "replaced_by": new_id,
                                       "report": filed.name})
        binding["platform_task_id"] = new_id
        binding["bound_by"] = filed.name
    if not known:
        binding["reports"].append({
            "eval": kind, "round": round_number, "verdict": rep["verdict"], "name": rep["name"],
            "filed_as": filed_rel, "sha256": rep["sha256"], "platform_task_id": result["platform_task_id"],
            "review_date": rep["review_date"], "ran_on": {n: r["ran_on"] for n, r in result["ran_on"].items()},
            "new_drift_items": len(drift.get("new") or []),
            "local_verdict": pair.get("local_verdict"), "local_snapshot": pair.get("local_snapshot")})
    if _json_bytes(binding) != before:              # a repeat intake of the same bytes writes nothing
        _atomic_write(_slot(task_dir, BIND_FILE), _json_bytes(binding), "the platform task binding")
    result["verdict"] = _verdict(checks, result["accepted"])
    return result


def list_reports(task_dir) -> dict:
    """Reports taken in, by eval and round, and report files in the folder that were never taken in."""
    task_dir = Path(task_dir)
    if not task_dir.is_dir():
        raise IntakeError(f"task folder not found: {task_dir}")
    binding = load_binding(task_dir)
    checks, rows = [], []
    if binding:
        order = {name: i for i, name in enumerate(EVALS)}
        rows = sorted(binding["reports"], key=lambda r: (order.get(r["eval"], 9), r["round"]))
        _check(checks, "list.binding", "PASS", f"{task_dir.name} is bound to platform task "
               f"{binding['platform_task_id']} (first report: {binding.get('bound_by')}); {len(rows)} reports taken in")
    else:
        _check(checks, "list.binding", "SKIP", f"{task_dir.name} is not bound yet: no report was taken in")
    taken = {r["sha256"] for r in rows}
    untracked = []
    folder = task_dir / REPORTS_DIR
    if folder.is_dir():
        for item in sorted(folder.iterdir()):
            if item.is_file() and item.suffix == ".md" and _sha_file(item) not in taken:
                rep = read_report(item)
                untracked.append({"name": item.name, "eval": rep["eval"], "verdict": rep["verdict"],
                                  "platform_task_id": rep["name_id"]})
    if untracked:
        _check(checks, "list.untracked", "WARN", f"{len(untracked)} file(s) in {REPORTS_DIR}/ were not taken in "
               "through this tool: " + ", ".join(u["name"] for u in untracked) + ". Run intake on each.")
    return {"tool": TOOL, "version": VERSION,
            "verdict": "WARN" if any(c["status"] == "WARN" for c in checks) else "PASS",
            "bound_to": {}, "checks": checks, "command": "list",
            "platform_task_id": binding["platform_task_id"] if binding else None,
            "reports": rows, "untracked": untracked}


# ---------------------------------------------------------------- output

def render(result) -> str:
    command = result.get("command")
    if command == "intake":
        qualifier, verdict = result.get("eval") or "unknown eval", result["verdict"]
    elif command == "snapshot":
        qualifier, verdict = "snapshot " + result["stage"], result["verdict"]
    else:
        qualifier, verdict = "list", result["verdict"]
    lines = [f"REPORT INTAKE ({qualifier}): {verdict}"]
    lines += [f"[{c['status']}] {c['id']}: {c['detail']}" for c in result["checks"]]
    if command == "list":
        for row in result["reports"]:
            local = f"  local {row['local_verdict']}" if row.get("local_verdict") else ""
            lines.append(f"  /{row['eval']:<9} round {row['round']:<2} {row['verdict']:<8} {row['filed_as']}{local}")
        for row in result["untracked"]:
            lines.append(f"  /{row['eval'] or '?':<9} not taken in {row['verdict']:<8} {row['name']}")
    return "\n".join(lines)


# ---------------------------------------------------------------- self-test

ASSIGNMENT_TEXT = """# Task Assigned Inputs — V3

```text
Business Function
Executive

Persona
{persona}
Role: Co-founder & Creative Director

Competency
Finance

Task Skill
Analysis and synthesis

Task Type
long-horizon

Difficulty Mode
easy

Universe Date
February 14, 2026 00:00
```
"""


def make_fixture(root, persona="Robert") -> dict:
    """A fake bundle for tests: a repo with tiny Evals/ and claude/, a register, and one task folder."""
    import release_drift
    root = Path(root)
    repo = root / "repo"
    (repo / "Evals" / "tools").mkdir(parents=True)
    (repo / "claude").mkdir()
    (repo / "Evals" / "1_Prompt_Eval.md").write_text("prompt spec with stage-evidence-v1\n")
    bundle = repo / "Task_Authoring"
    register = bundle / "references" / "platform_rule_delta.json"
    register.parent.mkdir(parents=True)
    seed = release_drift.empty_register()
    seed["local_bundle"] = {"fingerprint": "LOCALFP000000", "committed": "2026-11-01"}
    register.write_text(json.dumps(seed))
    task = bundle / "task_inputsA"
    (task / "Working_Files").mkdir(parents=True)
    (task / ASSIGNMENT).write_text(ASSIGNMENT_TEXT.format(persona=persona))
    (task / PROMPT).write_text("Build the sheet for Leonard.\n")
    (task / SQL).write_text("INSERT INTO slack.slack_messages VALUES (2);\n")
    (task / OE).write_text("OE 1 Search Slack.\n")
    (task / RUBRIC).write_text('[{"title": "The Agent builds the sheet"}]\n')
    old = task / "Working_Files" / FORENSICS_DIR / "rev1"
    old.mkdir(parents=True)
    (old / SQL).write_text("INSERT INTO slack.slack_messages VALUES (1);\n")
    return {"repo": repo, "bundle": bundle, "register": register, "task": task,
            "kw": {"tasks_root": bundle, "register": register, "repo": repo, "today": "2026-11-11",
                   "at": "2026-11-11T00:00:00Z"}}


def make_report(folder, name, kind_title, verdict, task_id=None, persona="Robert", hashes=(), extra="") -> Path:
    """A report file shaped like the platform's. `hashes` is a list of (file name, sha256 or prefix)."""
    lines = [f"## {kind_title}", ""]
    if persona:
        lines.append(f"### Persona: {persona} - Co-founder & Creative Director")
    if task_id:
        lines.append(f"| Review | chat attachment review, attempt {task_id} |")
    lines.append("| Review time | 2026-11-08T05:02:44Z |")
    for file_name, digest in hashes:
        lines.append(f"| Input | `inputs/{file_name}` sha256 `{digest}` (input-store revision 3) |")
    lines += [extra, "", f"### FINAL VERDICT: {verdict}", ""]
    path = Path(folder) / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines))
    return path


def _self_test() -> int:
    import selftest_sandbox
    import task_metrics
    with selftest_sandbox.scratch_tmp("report_intake_selftest_") as tmp:
        fx = make_fixture(tmp)
        task, kw, inbox = fx["task"], fx["kw"], Path(tmp) / "inbox"
        own, other = "6aeed82596dcfe103f9f74d9", "6aed9d01a1cb8067d8ac7dee"
        sha = lambda name: _sha_file(task / name)                                  # noqa: E731
        covered = 0
        # 1. a refused report writes nothing: another persona, even as the first report
        foreign = make_report(inbox, f"{other}_3_rubric.md", "RUBRIC EVALUATION REPORT", "FAIL", other,
                              persona="Leonard Hayes")
        result = intake(task, foreign, **kw)
        assert not result["accepted"] and not (task / REPORTS_DIR).exists() and load_binding(task) is None
        assert any(c["id"] == "bind.persona" and c["status"] == "FAIL" for c in result["checks"]), result["checks"]
        assert render(result).splitlines()[0] == "REPORT INTAKE (rubric): FAIL"
        covered += 1
        # 2. snapshot the local check, then the first report binds, files, records drift, counts and pairs
        (task / "Working_Files" / "04_Prompt_Check.md").write_text(
            f"# check\nprompt sha256 {sha(PROMPT)[:12]}\n- Predicted /prompt band: PASS (no Fail)\n"
            "- Status: READY FOR /prompt\n")
        snap = snapshot(task, "prompt-check", at=kw["at"])
        assert snap["verdict"] == "PASS" and snap["snapshot"]["prediction"]["verdict"] == "PASS", snap
        assert snap["snapshot"]["snapshot"] == f"Working_Files/check_history/prompt-check/1_{sha(PROMPT)[:12]}.md"
        assert snapshot(task, "prompt-check")["created"] is False
        first = make_report(inbox, f"{own}_1_prompt.md", "PROMPT EVALUATION REPORT", "FAIL", own,
                            hashes=[(PROMPT, sha(PROMPT)), (SQL, sha(SQL)[:8] + "…" + sha(SQL)[-4:])],
                            extra="Applies `ugt-fork-v9` here.\nEval release SHA-256: " + "a" * 64)
        result = intake(task, first, **kw)
        text = render(result)
        assert result["accepted"] and text.splitlines()[0] == "REPORT INTAKE (prompt): WARN", text   # new release
        assert (task / REPORTS_DIR / first.name).read_bytes() == first.read_bytes()
        assert load_binding(task)["platform_task_id"] == own
        assert result["ran_on"][PROMPT]["ran_on"] == "current" and result["ran_on"][SQL]["ran_on"] == "current"
        assert REVIEW_LINE in text and "ugt-fork-v9" in text and "new release" in text, text
        assert result["pair"] == {"local_verdict": "PASS", "pair_basis": "hash_printed", "agree": False,
                                  "local_snapshot": snap["snapshot"]["snapshot"]}, result["pair"]
        summary = task_metrics.summarise(task)
        assert summary["rounds"]["prompt"] == {"count": 1, "verdicts": ["FAIL"]}
        assert summary["verdict_pairs"][0]["local"] == "PASS" and summary["verdict_pairs"][0]["platform"] == "FAIL"
        assert "ugt-fork-v9" in json.loads(fx["register"].read_text())["names"]
        covered += 1
        # 3. the same report again is a no-op, also under another name: no second file, no second round, no write
        state = sorted((str(p), p.stat().st_mtime_ns, p.stat().st_size) for p in task.rglob("*"))
        renamed_copy = inbox / "renamed" / f"{own}_1_prompt (1).md"
        renamed_copy.parent.mkdir(parents=True)
        renamed_copy.write_bytes(first.read_bytes())
        for same in (first, renamed_copy):
            again = intake(task, same, **kw)
            assert again["accepted"] and again["filed_as"] == f"{REPORTS_DIR}/{first.name}", again
            assert any("already counted" in c["detail"] for c in again["checks"])
        assert state == sorted((str(p), p.stat().st_mtime_ns, p.stat().st_size) for p in task.rglob("*"))
        assert task_metrics.summarise(task)["rounds"]["prompt"]["count"] == 1
        covered += 1
        # 4. another id is refused with both ids and the folder named; --rebind accepts it
        stray = make_report(inbox, f"{other}_2_oe.md", "OE EVALUATION REPORT", "PASS", other)
        before = sorted(p.name for p in (task / REPORTS_DIR).iterdir())
        refused = intake(task, stray, **kw)
        detail = next(c["detail"] for c in refused["checks"] if c["id"] == "bind.task_id")
        assert not refused["accepted"] and own in detail and other in detail and task.name in detail, detail
        assert sorted(p.name for p in (task / REPORTS_DIR).iterdir()) == before
        with contextlib.redirect_stdout(io.StringIO()) as shown:
            code = main(["intake", str(stray), "--task-dir", str(task), "--tasks-root", str(fx["bundle"]),
                         "--register", str(fx["register"]), "--repo", str(fx["repo"]), "--json"])
        assert code == 1 and json.loads(shown.getvalue())["verdict"] == "FAIL"
        covered += 1
        # 5. different bytes under the same name get -dup1; an earlier SQL revision is named
        later = make_report(inbox / "later", first.name, "PROMPT EVALUATION REPORT", "PASS", own,
                            hashes=[(PROMPT, sha(PROMPT)),
                                    (SQL, _sha_file(task / "Working_Files" / FORENSICS_DIR / "rev1" / SQL))])
        result = intake(task, later, **kw)
        assert result["filed_as"] == f"{REPORTS_DIR}/{own}_1_prompt-dup1.md" and result["round"] == 2, result
        assert (result["ran_on"][SQL]["ran_on"], result["ran_on"][SQL]["where"]) == \
            ("earlier", f"{FORENSICS_DIR}/rev1/{SQL}"), result["ran_on"]
        assert (task / REPORTS_DIR / first.name).read_bytes() == first.read_bytes(), "the first copy was overwritten"
        assert any(c["id"] == "pair.local" and c["status"] == "SKIP" for c in result["checks"]), \
            "a check that read another SQL revision must not be paired"
        covered += 1
        # 6. hashes of another task folder are refused; a local review output is refused
        task_b = fx["bundle"] / "task_inputsB"
        (task_b / "Working_Files").mkdir(parents=True)
        (task_b / PROMPT).write_text("Another task's prompt.\n")
        wrong = make_report(inbox, f"{own}_1a_hardness.md", "Hardness review (Opus observed)", "FAIL", own,
                            persona=None, hashes=[(PROMPT, _sha_file(task_b / PROMPT))])
        result = intake(task, wrong, **kw)
        assert not result["accepted"] and result["ran_on"][PROMPT]["ran_on"] == "other_task", result["ran_on"]
        local = make_report(inbox, f"{own}_3_rubric.md", "RUBRIC EVALUATION REPORT", "PASS", own,
                            extra="local run, release LOCALFP000000")
        result = intake(task, local, **kw)
        assert not result["accepted"] and any(c["id"] == "report.platform" for c in result["checks"])
        covered += 1
        # 7. --rebind, --dry-run and list
        dry = intake(task, stray, rebind=True, dry_run=True, **kw)
        assert dry["accepted"] and load_binding(task)["platform_task_id"] == own
        rebound = intake(task, stray, rebind=True, **kw)
        assert rebound["accepted"] and load_binding(task)["platform_task_id"] == other
        assert load_binding(task)["history"][0]["platform_task_id"] == own
        (task / REPORTS_DIR / f"{own}_0_injection.md").write_text("# /injection\n### FINAL VERDICT: PASS\n")
        listing = list_reports(task)
        assert [(r["eval"], r["round"], r["verdict"]) for r in listing["reports"]] == \
            [("prompt", 1, "FAIL"), ("prompt", 2, "PASS"), ("oe", 1, "PASS")], listing["reports"]
        assert [u["name"] for u in listing["untracked"]] == [f"{own}_0_injection.md"]
        with contextlib.redirect_stdout(io.StringIO()) as shown:
            code = main(["list", "--task-dir", str(task)])
        assert code == 0 and "round 2" in render(listing) and shown.getvalue().startswith("REPORT INTAKE (list): WARN")
        covered += 1
        # 8. reading: name forms, verdict fallback, eval by title, hash forms
        assert eval_from_name("1a_hardness_FAIL2_r5.md") == "hardness" and eval_from_name("notes.md") is None
        renamed = make_report(inbox, "2_oe_NONFAIL3_r2.md", "Some review", "PASS", None)
        renamed.write_text("no verdict line here\n")
        rep = read_report(renamed)
        assert (rep["eval"], rep["verdict"], rep["verdict_source"]) == ("oe", "NON-FAIL", "file name"), rep
        got = input_hashes("- Inputs: OEs `08_Oracle_Events.md` (99 OEs, sha256 `0aca513e…`); prompt `04_Prompt.txt` "
                           "(sha256 `424c70d3…`); injection SQL `01_Universe_Inject.sql` revision 6 (sha256 "
                           "`9b02cc8f…`), replaces sha256 `bc72db9c`\nReviewed JSON SHA-256: " + "e" * 64 + "\n"
                           "Prompt record SHA-256: " + "f" * 64 + "\n")
        assert {k: [i["prefix"] for i in v] for k, v in got.items()} == {
            OE: ["0aca513e"], PROMPT: ["424c70d3"], SQL: ["9b02cc8f"], RUBRIC: ["e" * 64]}, got
        covered += 1
    print(f"self-test: ok ({covered} cases: a foreign persona refused with nothing written, snapshot then first "
          "intake binds, files, records drift, counts and pairs, a repeat is a no-op, another id refused and "
          "--rebind, -dup1 with an earlier SQL revision named, another folder's hashes and a local review output "
          "refused, list with untracked files, report reading)")
    return 0


# ---------------------------------------------------------------- command line

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        return _self_test()
    ap = argparse.ArgumentParser(prog="report_intake.py", description="take in a platform report (see the docstring)")
    sub = ap.add_subparsers(dest="command")
    take = sub.add_parser("intake", help="check, file and record one platform report")
    take.add_argument("report")
    take.add_argument("--task-dir", required=True)
    take.add_argument("--eval", choices=EVALS)
    take.add_argument("--rebind", action="store_true", help="accept another platform task id and bind the folder to it")
    take.add_argument("--dry-run", action="store_true", help="decide only; write nothing")
    take.add_argument("--at", help="ISO time for the metrics event (default: now)")
    take.add_argument("--today", help="date written to the register (default: today)")
    take.add_argument("--register", help="register file (default: references/platform_rule_delta.json)")
    take.add_argument("--repo", help="folder that holds Evals/ and claude/ (default: the workspace)")
    take.add_argument("--tasks-root", help="folder whose task_inputs* folders are the other tasks (default: the bundle)")
    take.add_argument("--json", action="store_true")
    snap = sub.add_parser("snapshot", help="store the current local check with the hash of what it checked")
    snap.add_argument("--task-dir", required=True)
    snap.add_argument("--stage", required=True, choices=tuple(STAGES))
    snap.add_argument("--at", help="ISO time for the metrics event (default: now)")
    snap.add_argument("--json", action="store_true")
    show = sub.add_parser("list", help="reports taken in, by eval and round")
    show.add_argument("--task-dir", required=True)
    show.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if not args.command:
        ap.error("a command is required: intake, snapshot or list")
    if not Path(args.task_dir).is_dir():
        ap.error(f"task folder not found: {args.task_dir}")
    if args.command == "intake" and not Path(args.report).is_file():
        ap.error(f"report file not found: {args.report}")
    from task_context import ContextError
    from task_metrics import MetricsError
    try:
        if args.command == "intake":
            result = intake(args.task_dir, args.report, eval_kind=args.eval, rebind=args.rebind,
                            tasks_root=args.tasks_root, register=args.register, repo=args.repo, today=args.today,
                            at=args.at, dry_run=args.dry_run)
        elif args.command == "snapshot":
            result = snapshot(args.task_dir, args.stage, at=args.at)
        else:
            result = list_reports(args.task_dir)
    except (IntakeError, ContextError, MetricsError, OSError) as exc:
        print(f"REPORT INTAKE ({args.command}): FAIL\n[FAIL] intake.{args.command}: {exc}")
        return 1
    print(json.dumps(result, indent=1, sort_keys=True, ensure_ascii=False) if args.json else render(result))
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())

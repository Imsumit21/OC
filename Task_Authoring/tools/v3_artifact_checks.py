#!/usr/bin/env python3
"""Evidence checks for V3 artifacts; review records document human judgment, not semantic proof."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from zoneinfo import ZoneInfo

EVIDENCE_FILE = "00_V3_Authoring_Evidence.json"
HERE = Path(__file__).resolve().parent


def review_digest(stage, task_dir):
    """Bind only this stage's review evidence so later reviews do not stale earlier certificates."""
    path = Path(task_dir) / "Working_Files" / EVIDENCE_FILE
    try:
        data = json.loads(path.read_text())
        projection = {"context_hash": data.get("context_hash"),
                      "role_review": data.get("role_reviews", {}).get(stage),
                      "outcome_review": data.get("outcome_reviews", {}).get(stage)}
        if stage in ("rubric-writing", "rubric-check", "release"):
            projection["rubric_rows"] = data.get("rubric_rows")
        return hashlib.sha256(json.dumps(projection, sort_keys=True).encode()).hexdigest()[:12]
    except (OSError, ValueError, AttributeError):
        return hashlib.sha256(b"missing or invalid V3 evidence").hexdigest()[:12]


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _inside(path, roots):
    return any(path == root or root in path.parents for root in roots)


def _pointer(data, pointer):
    if not isinstance(pointer, str) or (pointer and not pointer.startswith("/")):
        raise ValueError("pointer must be an RFC 6901 JSON pointer")
    node = data
    for token in pointer.split("/")[1:]:
        key = token.replace("~1", "/").replace("~0", "~")
        if isinstance(node, dict) and (node.get("trashed") is True or node.get("is_trashed") is True):
            raise ValueError("deciding evidence in Trash is not permitted")
        if key.casefold() in ("attachments", "attachment"):
            raise ValueError("deciding evidence in an attachment is not permitted")
        node = node[int(key)] if isinstance(node, list) else node[key]
    if isinstance(node, dict) and (node.get("trashed") is True or node.get("is_trashed") is True):
        raise ValueError("deciding evidence in Trash is not permitted")
    return node


def _bounded_get(service, path, root, pointer, task_dir):
    """Read a bounded field through the selected-source helper; never json.load a universe export."""
    if not isinstance(pointer, str) or (pointer and not pointer.startswith("/")):
        raise ValueError("pointer must be an RFC 6901 JSON pointer")
    if any(part.casefold() in ("attachment", "attachments") for part in pointer.split("/")):
        raise ValueError("deciding evidence in an attachment is not permitted")
    base = {"service": service, "file": path.relative_to(root).as_posix()}
    items = [dict(base, id="value", pointer=pointer, max_chars=65536)]
    # Read only small trash flags, not every enclosing object. Missing optional flags are
    # expected for most service records; a present true flag blocks the deciding source.
    parts = pointer.split("/")[1:]
    if len(parts) > 23:
        raise ValueError("source pointer is too deeply nested for the bounded evidence reader")
    for i in range(len(parts)):
        prefix = "/" + "/".join(parts[:i]) if i else ""
        for flag in ("trashed", "is_trashed"):
            items.append(dict(base, id=f"flag-{i}-{flag}", pointer=prefix + "/" + flag, max_chars=16))
    command = [sys.executable, str(HERE / "hg.py"), "search", "get-many", "--request", "-",
               "--task-dir", str(task_dir)]
    result = subprocess.run(command, input=json.dumps({"items": items}), capture_output=True, text=True, timeout=120)
    try:
        outputs = json.loads(result.stdout)["items"]
        output = outputs["value"]
    except (ValueError, KeyError, TypeError):
        raise ValueError("selected-source field lookup failed: " + (result.stderr or result.stdout).strip()[:180])
    if output.get("error"):
        raise ValueError("selected-source field lookup failed: " + str(output["error"])[:180])
    if output.get("encoding") != "rendered-json" or output.get("truncated") is not False:
        raise ValueError("source field lookup was truncated or not rendered JSON; cite a narrower pointer")
    value = json.loads(output["text"])
    for key, flag in outputs.items():
        if key != "value" and flag.get("encoding") == "rendered-json" and flag.get("truncated") is False:
            if json.loads(flag["text"]) is True:
                raise ValueError("deciding evidence in Trash is not permitted")
    if isinstance(value, dict) and (value.get("trashed") is True or value.get("is_trashed") is True):
        raise ValueError("deciding evidence in Trash is not permitted")
    return value


def _source_value(record, task_dir, context, workspace):
    """Read a cited JSON field or a literal seeded SQL field from the selected source."""
    name = record.get("source_file")
    if not _text(name):
        raise ValueError("source_file missing")
    task_dir, workspace = Path(task_dir).resolve(), Path(workspace).resolve()
    if name == "01_Universe_Inject.sql":
        from base_check import parse_sql
        identity = record.get("identity")
        if not isinstance(identity, dict) or not identity:
            raise ValueError("SQL citation needs identity columns")
        column = record.get("column")
        rows = [r for r in parse_sql((task_dir / name).read_text())
                if r.get("table") == record.get("table") and r.get("op") == "insert"
                and all(r.get("row", {}).get(k) == v for k, v in identity.items())]
        if len(rows) != 1 or column not in rows[0].get("row", {}):
            raise ValueError("SQL citation does not identify exactly one literal inserted field")
        if rows[0]["row"].get("trashed") is True or rows[0]["row"].get("is_trashed") is True:
            raise ValueError("deciding evidence in Trash is not permitted")
        if "attachment" in str(column).casefold():
            raise ValueError("deciding evidence in an attachment is not permitted")
        return rows[0]["row"][column]
    path = Path(name)
    if not path.is_absolute():
        path = task_dir / path if path.parts[:1] == ("02_Reference_Files",) else workspace / path
    path = path.resolve()
    references = (task_dir / "02_Reference_Files").resolve()
    if _inside(path, [references]):
        if path.stat().st_size > 2 * 1024 * 1024:
            raise ValueError("reference JSON exceeds the bounded reader; cite a smaller evidence extract")
        return _pointer(json.loads(path.read_text()), record.get("pointer"))
    root_name = context.get("source", {}).get("paths", {}).get(record.get("service"))
    if not root_name or not _inside(path, [Path(root_name).resolve()]):
        raise ValueError("source_file is outside the selected source root for the cited service")
    return _bounded_get(record["service"], path, Path(root_name).resolve(), record.get("pointer"), task_dir)


def _review(review, stage, artifact, context, artifact_hash, role=False):
    errors = []
    if not isinstance(review, dict):
        return [f"{stage}: recorded review missing"]
    for key in ("reviewer", "rationale"):
        if not _text(review.get(key)):
            errors.append(f"{stage}: review {key} missing")
    if review.get("artifact") != artifact or review.get("artifact_hash") != artifact_hash(artifact):
        errors.append(f"{stage}: review artifact/hash does not match {artifact}")
    if role:
        if review.get("persona_role") != context["persona_role"]:
            errors.append(f"{stage}: reviewed role does not match the assignment")
        if not isinstance(review.get("source_ids"), list) or not all(_text(s) for s in review["source_ids"]) or not review["source_ids"]:
            errors.append(f"{stage}: role review source_ids missing")
    else:
        for key in ("accepted_outcomes", "alternatives_considered"):
            if not isinstance(review.get(key), list) or not review[key]:
                errors.append(f"{stage}: outcome review {key} missing")
    return errors


def _dates(dates, prompt, sources):
    if not isinstance(dates, dict):
        return ["dates evidence must be an object"]
    try:
        instant = dt.datetime.fromisoformat(dates["instant_utc"].replace("Z", "+00:00"))
        if instant.tzinfo is None:
            raise ValueError("instant is not timezone aware")
        utc = instant.astimezone(dt.timezone.utc).date().isoformat()
        pacific = instant.astimezone(ZoneInfo("America/Los_Angeles")).date().isoformat()
    except (ValueError, KeyError, TypeError, AttributeError) as exc:
        return [f"date instant invalid: {exc}"]
    errors = []
    if dates.get("utc") != utc or dates.get("pacific") != pacific:
        errors.append("Pacific/UTC dates do not match the cited instant")
    if not any(_instant(s.get("source_value")) == instant for s in sources):
        errors.append("date instant does not match a verified source_value")
    zone = dates.get("prompt_timezone")
    accepted = set(dates.get("accepted_dates") or [])
    if zone is None:
        if not {utc, pacific}.issubset(accepted):
            errors.append("date acceptance must include both Pacific and UTC dates when no timezone is requested")
    elif zone in ("Pacific", "UTC"):
        span = dates.get("timezone_prompt_span")
        if not _text(span) or span not in prompt:
            errors.append("explicit timezone needs its exact prompt span")
        if (pacific if zone == "Pacific" else utc) not in accepted:
            errors.append("requested timezone date is not accepted")
    else:
        errors.append("prompt_timezone must be null, Pacific or UTC")
    return errors


def _instant(value):
    try:
        parsed = dt.datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if parsed.tzinfo:
            return parsed
    except (ValueError, TypeError):
        pass
    try:
        epoch = float(value)
        if 946684800 <= epoch <= 4102444800:
            return dt.datetime.fromtimestamp(epoch, dt.timezone.utc)
    except (ValueError, TypeError, OverflowError):
        pass
    return None


def _temporal(source, context, task_dir, workspace):
    """Check dated fact evidence within a per-universe source, without inventing a second snapshot."""
    proof = source.get("temporal_evidence")
    if not isinstance(proof, dict):
        return ["universe source needs temporal_evidence for the assigned freeze"]
    errors = []
    semantics = proof.get("value_semantics")
    if semantics not in ("fact", "future_deadline", "scheduled_event", "directory_identity"):
        errors.append("temporal value_semantics must be fact, future_deadline, scheduled_event or directory_identity")
    if not _text(proof.get("rationale")):
        errors.append("temporal rationale explaining the source date missing")
    if type(proof.get("mutable_state")) is not bool:
        errors.append("temporal mutable_state must explicitly identify whether current content may have changed")
    if semantics == "directory_identity":
        name = Path(str(source.get("source_file", ""))).name
        if proof.get("mutable_state") is not False:
            errors.append("directory_identity is only for immutable identity/directory values")
        if source.get("service") != "contacts" and name not in ("users.json", "roster.json", "persona_roster_v2.json"):
            errors.append("directory_identity must cite a Contacts or service identity-directory record")
        locator = source.get("column") if source.get("source_file") == "01_Universe_Inject.sql" else str(source.get("pointer", "")).rsplit("/", 1)[-1]
        field = re.sub(r"[^a-z0-9]", "", str(locator).casefold())
        if field not in ("id", "userid", "contactid", "personakey", "email", "emailaddress", "primaryemail",
                         "name", "firstname", "lastname", "fullname", "displayname", "username", "login", "handle"):
            errors.append("directory_identity must cite an identity field, not a mutable business value")
        return errors
    try:
        freeze = dt.datetime.fromisoformat(context["freeze_utc"].replace("Z", "+00:00"))
        citation = dict(source)
        if source.get("source_file") == "01_Universe_Inject.sql":
            column = proof.get("recorded_at_column")
            if not _text(column):
                raise ValueError("temporal recorded_at_column missing for seeded SQL")
            citation["column"] = column
        else:
            pointer = proof.get("recorded_at_pointer")
            if not _text(pointer):
                raise ValueError("temporal recorded_at_pointer missing")
            citation["pointer"] = pointer
        recorded = _instant(_source_value(citation, task_dir, context, workspace))
        if recorded is None:
            raise ValueError("recorded timestamp must be a timezone-aware source value or Unix timestamp")
        if recorded > freeze:
            errors.append("source record was recorded after the assigned freeze; cite a record available at that time")
        actual = _instant(source.get("source_value"))
        if actual is None and isinstance(source.get("source_value"), str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", source["source_value"]):
            actual = dt.datetime.fromisoformat(source["source_value"]).replace(tzinfo=dt.timezone.utc)
        if semantics == "fact" and actual is not None and actual > freeze:
            errors.append("completed fact occurs after the assigned freeze; only future deadlines/scheduled events may be future-dated")
    except (OSError, ValueError, KeyError, IndexError, TypeError) as exc:
        errors.append(str(exc))
    if proof.get("mutable_state") is True:
        review = proof.get("state_at_freeze_review")
        if not isinstance(review, dict) or not all(_text(review.get(key)) for key in ("reviewer", "rationale")):
            errors.append("mutable source content needs a named state_at_freeze_review; creation time alone does not prove the old body/state")
        else:
            ids = review.get("evidence_ids")
            path_ids = {step.get("id") for step in source.get("evidence_path", []) if isinstance(step, dict)}
            if not isinstance(ids, list) or not ids or not all(_text(i) and i in path_ids for i in ids):
                errors.append("freeze-state review must cite history/version or other supporting record IDs in the checked evidence_path")
    return errors


def check_evidence(stage, task_dir, context, artifact_hash, reachable, workspace):
    """Return (check id, success, detail) tuples; every judgment must be recorded against current content."""
    need_role = stage in ("scenario", "prompt-check")
    need_outcomes = stage in ("prompt-writing", "prompt-check")
    need_rubric = stage in ("rubric-writing", "rubric-check", "release")
    if not (need_role or need_outcomes or need_rubric):
        return []
    path = Path(task_dir) / "Working_Files" / EVIDENCE_FILE
    try:
        data = json.loads(path.read_text())
        if not isinstance(data, dict):
            raise ValueError("expected an object")
    except (OSError, ValueError) as exc:
        return [("v3.evidence", False, f"{path.name}: {exc}")]
    if data.get("spec_version") != "V3" or data.get("context_hash") != context["context_hash"]:
        return [("v3.evidence_context", False, "V3 evidence does not match the current assignment/policy/source context")]
    checks = []
    if need_role:
        artifact = "01_Scenario_Design.md" if stage == "scenario" else "04_Prompt.txt"
        errors = _review(data.get("role_reviews", {}).get(stage), stage, artifact, context, artifact_hash, True)
        checks.append(("v3.role_review", not errors, "; ".join(errors) if errors else
                       "current role-plausibility review recorded; semantic judgment belongs to the named reviewer"))
    if need_outcomes:
        artifact = "04_Prompt_Writing_Brief.md" if stage == "prompt-writing" else "04_Prompt.txt"
        errors = _review(data.get("outcome_reviews", {}).get(stage), stage, artifact, context, artifact_hash)
        checks.append(("v3.fair_outcomes_review", not errors, "; ".join(errors) if errors else
                       "current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed"))
    if not need_rubric:
        return checks
    prompt_path = Path(task_dir) / "04_Prompt.txt"
    prompt = prompt_path.read_text() if prompt_path.exists() else ""
    rubric_path = Path(task_dir) / "09_Rubrics.json"
    try:
        rubric = json.loads(rubric_path.read_text())
        if not isinstance(rubric, list) or not rubric or not all(isinstance(r, dict) for r in rubric):
            raise ValueError("nonempty array of criteria required")
    except (OSError, ValueError) as exc:
        return checks + [("v3.rubric_evidence", False, f"rubric unreadable: {exc}")]
    if data.get("rubric_hash") != artifact_hash("09_Rubrics.json") or data.get("prompt_hash") != artifact_hash("04_Prompt.txt"):
        return checks + [("v3.rubric_evidence", False, "rubric_hash/prompt_hash does not match the reviewed content")]
    rows = data.get("rubric_rows")
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        return checks + [("v3.rubric_evidence", False, "rubric_rows review array missing")]
    expected_ids = {str(r.get("id") or f"C{i + 1}") for i, r in enumerate(rubric)}
    ids = [str(r.get("criterion_id", "")) for r in rows]
    errors = []
    if set(ids) != expected_ids or len(ids) != len(set(ids)):
        errors.append("rubric_rows must cover each criterion exactly once (explicit id or positional C1, C2, ...)")
    fact_counts = Counter(r.get("fact_id") for r in rows if _text(r.get("fact_id")))
    repeated = sorted(k for k, count in fact_counts.items() if count >= 3)
    checks.append(("v3.fact_duplication", not repeated, f"facts graded three or more times: {repeated}" if repeated else
                   "no declared fact_id is graded in three or more criteria; reviewer must also check semantic duplicates"))
    for row in rows:
        rid = str(row.get("criterion_id", "?"))
        local = []
        if not _text(row.get("fact_id")):
            local.append("fact_id missing")
        span = row.get("prompt_span")
        if not _text(span) or span not in prompt:
            local.append("prompt_span is not an exact requested-work span")
        if not isinstance(row.get("accepted_outcomes"), list) or not row["accepted_outcomes"]:
            local.append("accepted_outcomes missing")
        if not _text(row.get("alternatives_review")):
            local.append("alternatives_review missing")
        sources = row.get("source_records")
        if not isinstance(sources, list) or not sources or not all(isinstance(s, dict) for s in sources):
            local.append("source_records missing")
            sources = []
        for source in sources:
            try:
                if not all(_text(source.get(k)) for k in ("service", "id")):
                    raise ValueError("service/id missing")
                actual = _source_value(source, task_dir, context, workspace)
                if "source_value" not in source or actual != source["source_value"] or (
                        isinstance(actual, bool) != isinstance(source.get("source_value"), bool)):
                    raise ValueError("source_value does not match the cited record field")
                path_steps = source.get("evidence_path")
                if not isinstance(path_steps, list) or not path_steps:
                    raise ValueError("evidence_path from requested work missing")
                if not all(isinstance(step, dict) and _text(step.get("service")) and _text(step.get("id")) for step in path_steps):
                    raise ValueError("evidence_path steps need service and id")
                if (path_steps[-1]["service"], path_steps[-1]["id"]) != (source["service"], source["id"]):
                    raise ValueError("evidence_path does not end at the cited record")
                if not _text(source.get("reachability_rationale")):
                    raise ValueError("reachability_rationale explaining the prompt path missing")
                for step in path_steps:
                    ok, reason = reachable(step["service"], step["id"])
                    if not ok:
                        raise ValueError(f"{step['id']} not proven reachable: {reason}")
                if context.get("source", {}).get("mode") == "universe":
                    local.extend(_temporal(source, context, task_dir, workspace))
            except (OSError, ValueError, KeyError, IndexError, TypeError) as exc:
                local.append(str(exc))
        date_criterion = re.search(r"\b(date|day|when|dates)\b", str(span), re.I)
        if row.get("dates") is not None:
            local.extend(_dates(row["dates"], prompt, sources))
        elif date_criterion and any(_instant(s.get("source_value")) is not None for s in sources):
            local.append("requested date with a timestamp source needs Pacific/UTC dates acceptance evidence")
        if local:
            errors.append(f"{rid}: " + "; ".join(local))
    checks.append(("v3.rubric_evidence", not errors, "; ".join(errors[:8]) if errors else
                   "every criterion has requested-work trace, verified source values, path visibility/existence checks and recorded fair-outcomes reasoning; path linkage remains review judgment"))
    return checks

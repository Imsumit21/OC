"""Linear invariants for a proposed overlay (L1-L12) and a base-data corroboration pass.

Rules are re-implemented from their written sources:
- Evals/0_Injection_Quality_Eval.md lines 185-196 (Linear text dates, state_history_json)
- Task_Authoring/playbooks/01_Universe_Injection.md line 140 (Linear recipe)
- Evals/task_inputs/reports/0_injection.md lines 60-90 (comment window and author membership)

Nothing here imports tools/sql_lint.py, tools/base_check.py or generators/services code.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime

from generators.validate.overlay import MEMBERSHIP_TABLE, Overlay

ISSUES = "linear.linear_issues"
COMMENTS = "linear.linear_comments"
PROJECTS = "linear.linear_projects"
TEAMS = "linear.linear_teams"
USERS = "linear.linear_users"

FAIL, WARN = "FAIL", "WARN"

_TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", re.ASCII)
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$", re.ASCII)
_DATE_COLUMNS = {"due_date", "start_date", "target_date"}
_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
_DATE_FORMAT = "%Y-%m-%d"


@dataclass(frozen=True)
class Finding:
    rule: str
    severity: str
    table: str
    key: tuple
    message: str


def _finding(rule: str, severity: str, table: str, key: tuple, message: str) -> Finding:
    return Finding(rule=rule, severity=severity, table=table, key=key, message=message)


# --------------------------------------------------------------------------- helpers

def _parse_ts(value) -> datetime | None:
    """ASCII YYYY-MM-DDTHH:MM:SSZ only (strptime alone would take some non-ASCII digits)."""
    if not isinstance(value, str) or not _TS_RE.match(value):
        return None
    try:
        return datetime.strptime(value, _TIMESTAMP_FORMAT)
    except ValueError:
        return None


def _parse_date(value) -> datetime | None:
    if not isinstance(value, str) or not _DATE_RE.match(value):
        return None
    try:
        return datetime.strptime(value, _DATE_FORMAT)
    except ValueError:
        return None


def _order(value) -> tuple:
    """Total-order key that tolerates unparseable values (never raises on mixed types)."""
    dt = _parse_ts(value)
    if dt is not None:
        return (0, dt, "")
    if isinstance(value, str):
        return (1, datetime.min, value)
    return (2, datetime.min, "")


def _row(state: dict, table: str, key: tuple) -> dict | None:
    return (state.get(table) or {}).get(key)


def _rows(overlay: Overlay, table: str) -> list[tuple[tuple, dict]]:
    table_rows = overlay.state.get(table) or {}
    return [(key, table_rows[key]) for key in overlay.touched(table) if key in table_rows]


def _all_issues(overlay: Overlay) -> dict[tuple, dict]:
    return overlay.state.get(ISSUES) or {}


def _date_columns(row: dict) -> list[str]:
    return [c for c in row if c.endswith("_at") or c in _DATE_COLUMNS]


def state_types(base: dict) -> dict[str, list[str]]:
    """Infer completed-type / canceled-type state ids and every state id seen in the base."""
    completed: set[str] = set()
    canceled: set[str] = set()
    known: set[str] = set()
    for row in (base.get(ISSUES) or {}).values():
        state = row.get("state_id")
        if state is not None:
            known.add(state)
        if state is not None and row.get("completed_at") is not None:
            completed.add(state)
        if state is not None and row.get("canceled_at") is not None:
            canceled.add(state)
    return {"completed": sorted(completed), "canceled": sorted(canceled), "known": sorted(known)}


# --------------------------------------------------------------------------- rules

def _rule_l1(overlay: Overlay) -> list[Finding]:
    out: list[Finding] = []
    for table in overlay.state:
        for key, row in _rows(overlay, table):
            for col in _date_columns(row):
                value = row.get(col)
                if value is None:
                    continue
                # shape (ASCII pattern) and a real calendar value (strptime): '2025-02-30' and 25:00 both fail
                if col in _DATE_COLUMNS:
                    if _parse_date(value) is None:
                        out.append(_finding("L1", FAIL, table, key,
                                            f"{col}={value!r} is not a real YYYY-MM-DD date"))
                else:
                    if _parse_ts(value) is None:
                        out.append(_finding("L1", FAIL, table, key,
                                            f"{col}={value!r} is not a real YYYY-MM-DDTHH:MM:SSZ time"))
    return out


def _rule_l2(overlay: Overlay, base: dict) -> list[Finding]:
    out: list[Finding] = []
    teams = overlay.state.get(TEAMS) or {}
    base_issues = base.get(ISSUES) or {}
    base_ids = {row.get("id") for row in base_issues.values()}
    base_identifiers = {row.get("identifier") for row in base_issues.values()}
    for key, row in _rows(overlay, ISSUES):
        if overlay.kind(ISSUES, key) != "insert":
            continue
        issue_id = row.get("id")
        identifier = row.get("identifier")
        number = row.get("number")
        team_id = row.get("team_id")
        team = teams.get((team_id,))
        if team is None:
            out.append(_finding("L2", FAIL, ISSUES, key, f"team {team_id!r} does not exist"))
            team_key = None
        else:
            team_key = team.get("key")
        if not (isinstance(number, int) and not isinstance(number, bool)):
            out.append(_finding("L2", FAIL, ISSUES, key, f"number={number!r} is not an int"))
            expected = None
        elif team_key is not None:
            expected = f"{team_key}-{number}"
        else:
            expected = None
        if expected is not None:
            if issue_id != expected:
                out.append(_finding("L2", FAIL, ISSUES, key,
                                    f"id={issue_id!r} != {expected!r} (team key + number)"))
            if identifier != expected:
                out.append(_finding("L2", FAIL, ISSUES, key,
                                    f"identifier={identifier!r} != {expected!r} (team key + number)"))
        if issue_id in base_ids:
            out.append(_finding("L2", FAIL, ISSUES, key, f"id {issue_id!r} already exists in the base"))
        if identifier in base_identifiers:
            out.append(_finding("L2", FAIL, ISSUES, key,
                                f"identifier {identifier!r} already exists in the base"))
    return out


def _rule_l3(overlay: Overlay) -> list[Finding]:
    out: list[Finding] = []
    for key, row in _rows(overlay, ISSUES):
        if overlay.kind(ISSUES, key) != "insert":
            continue
        if row.get("state_history_json") != "[]":
            out.append(_finding("L3", FAIL, ISSUES, key,
                                f"state_history_json={row.get('state_history_json')!r}, expected '[]'"))
        if row.get("links_json") != "[]":
            out.append(_finding("L3", WARN, ISSUES, key,
                                f"links_json={row.get('links_json')!r}, expected '[]'"))
    return out


def _rule_l4(overlay: Overlay, base: dict) -> list[Finding]:
    out: list[Finding] = []
    types = state_types(base)
    completed_types = set(types["completed"])
    canceled_types = set(types["canceled"])
    known = set(types["known"])

    for key, row in _rows(overlay, ISSUES):
        issue_id = row.get("id", key[0] if key else None)
        state = row.get("state_id")
        completed = row.get("completed_at")
        canceled = row.get("canceled_at")

        if state not in known:
            out.append(_finding("L4", WARN, ISSUES, key,
                                f"state_id {state!r} was not seen in the base"))
            if completed is not None or canceled is not None:
                out.append(_finding("L4", FAIL, ISSUES, key,
                                    f"state_id {state!r} is not a base state, so its completed_at/canceled_at "
                                    "cannot be checked; use a state the base uses"))
        elif state in completed_types:
            if completed is None:
                out.append(_finding("L4", FAIL, ISSUES, key,
                                    f"completed-type state {state!r} without completed_at"))
            if canceled is not None:
                out.append(_finding("L4", FAIL, ISSUES, key,
                                    f"completed-type state {state!r} has canceled_at={canceled!r}"))
        elif state in canceled_types:
            if canceled is None:
                out.append(_finding("L4", FAIL, ISSUES, key,
                                    f"canceled-type state {state!r} without canceled_at"))
            if completed is not None:          # 0 of 412 / 381 canceled-type base issues carry completed_at
                out.append(_finding("L4", FAIL, ISSUES, key,
                                    f"canceled-type state {state!r} has completed_at={completed!r}"))
        else:
            if completed is not None:
                out.append(_finding("L4", FAIL, ISSUES, key,
                                    f"state {state!r} must not set completed_at={completed!r}"))
            if canceled is not None:
                out.append(_finding("L4", FAIL, ISSUES, key,
                                    f"state {state!r} must not set canceled_at={canceled!r}"))

        chains = (
            ("created_at", "started_at", "completed_at", "updated_at"),
            ("created_at", "started_at", "canceled_at", "updated_at"),
        )
        for name in ("created_at", "started_at", "completed_at", "canceled_at", "updated_at"):
            if row.get(name) is not None and _parse_ts(row.get(name)) is None:
                out.append(_finding("L4", FAIL, ISSUES, key,
                                    f"{name} {row.get(name)!r} is not a YYYY-MM-DDTHH:MM:SSZ time, so the lifecycle "
                                    "order cannot be checked"))
        for chain in chains:
            present = [(name, _parse_ts(row.get(name))) for name in chain]
            present = [(name, dt) for name, dt in present if dt is not None]
            for (prev_name, prev_dt), (next_name, next_dt) in zip(present, present[1:]):
                if prev_dt > next_dt:
                    out.append(_finding("L4", FAIL, ISSUES, key,
                                        f"{prev_name} {row.get(prev_name)!r} > {next_name} {row.get(next_name)!r}"))
    return out


def _inserted_comments(overlay: Overlay) -> list[tuple[tuple, dict]]:
    return [(key, row) for key, row in _rows(overlay, COMMENTS)
            if overlay.kind(COMMENTS, key) == "insert"]


def _rule_l5(overlay: Overlay) -> list[Finding]:
    out: list[Finding] = []
    issues = _all_issues(overlay)
    comments = overlay.state.get(COMMENTS) or {}
    for key, row in _inserted_comments(overlay):
        issue_key = (row.get("issue_id"),)
        issue = issues.get(issue_key)
        if issue is None:
            out.append(_finding("L5", FAIL, COMMENTS, key,
                                f"issue_id {row.get('issue_id')!r} does not exist"))
        else:
            created = _parse_ts(row.get("created_at"))
            issue_created = _parse_ts(issue.get("created_at"))
            if created is not None and issue_created is not None and not created > issue_created:
                out.append(_finding("L5", FAIL, COMMENTS, key,
                                    f"created_at {row.get('created_at')!r} is not after the issue's "
                                    f"created_at {issue.get('created_at')!r}"))
        created = _parse_ts(row.get("created_at"))
        if created is None:
            out.append(_finding("L5", FAIL, COMMENTS, key,
                                f"created_at {row.get('created_at')!r} is not a usable timestamp"))
        parent_id = row.get("parent_id")
        if parent_id is not None and (parent_id,) not in comments:
            out.append(_finding("L5", FAIL, COMMENTS, key,
                                f"parent_id {parent_id!r} is not an existing comment"))
        if row.get("updated_at") != row.get("created_at"):
            out.append(_finding("L5", WARN, COMMENTS, key,
                                f"updated_at {row.get('updated_at')!r} != created_at "
                                f"{row.get('created_at')!r}"))
        if row.get("is_edited") is not False:
            out.append(_finding("L5", WARN, COMMENTS, key,
                                f"is_edited={row.get('is_edited')!r}, expected False"))
    return out


def _rule_l6(overlay: Overlay) -> list[Finding]:
    out: list[Finding] = []
    users = overlay.state.get(USERS) or {}
    memberships = overlay.state.get(MEMBERSHIP_TABLE) or {}
    issues = _all_issues(overlay)
    for key, row in _inserted_comments(overlay):
        author_id = row.get("author_id")
        if (author_id,) not in users:
            out.append(_finding("L6", FAIL, COMMENTS, key, f"author_id {author_id!r} is not a user"))
        issue = issues.get((row.get("issue_id"),))
        if issue is None:
            continue
        comment_order = _order(row.get("created_at"))
        team_id = issue.get("team_id")
        matching = [m for m in memberships.values()
                    if m.get("team_id") == team_id and m.get("user_id") == author_id]
        if not matching:
            out.append(_finding("L6", WARN, COMMENTS, key,
                                f"author {author_id!r} is not a member of team {team_id!r}"))
            continue
        if not any(_order(m.get("created_at")) <= comment_order for m in matching):
            out.append(_finding("L6", WARN, COMMENTS, key,
                                f"author {author_id!r} joined team {team_id!r} after the comment"))
    return out


def _rule_l7(overlay: Overlay) -> list[Finding]:
    out: list[Finding] = []
    issues = _all_issues(overlay)
    for key, row in _inserted_comments(overlay):
        issue = issues.get((row.get("issue_id"),))
        if issue is None:
            continue
        comment_order = _order(row.get("created_at"))
        for stamp in ("completed_at", "canceled_at"):
            closed = issue.get(stamp)
            if closed is not None and _order(closed) < comment_order:
                out.append(_finding("L7", WARN, COMMENTS, key,
                                    f"comment at {row.get('created_at')!r} is after the issue's "
                                    f"{stamp} {closed!r} (\"closed with later activity\")"))
                break
    return out


def _comments_by_issue(overlay: Overlay) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}
    for row in (overlay.state.get(COMMENTS) or {}).values():
        grouped.setdefault(row.get("issue_id"), []).append(row)
    return grouped


def _rule_l8(overlay: Overlay) -> list[Finding]:
    out: list[Finding] = []
    issues = _all_issues(overlay)
    grouped = _comments_by_issue(overlay)
    for issue_key in {row.get("issue_id") for _, row in _inserted_comments(overlay)}:
        issue = issues.get((issue_key,))
        comments = grouped.get(issue_key) or []
        if issue is None or not comments:
            continue
        newest = max(comments, key=lambda c: _order(c.get("created_at")))
        if _order(issue.get("updated_at")) < _order(newest.get("created_at")):
            out.append(_finding("L8", FAIL, ISSUES, (issue_key,),
                                f"updated_at {issue.get('updated_at')!r} < newest comment "
                                f"created_at {newest.get('created_at')!r}"))
    return out


def _rule_l9(overlay: Overlay) -> list[Finding]:
    out: list[Finding] = []
    grouped = _comments_by_issue(overlay)
    for issue_key in {row.get("issue_id") for _, row in _inserted_comments(overlay)}:
        comments = grouped.get(issue_key) or []
        ordered = sorted(comments, key=lambda c: _order(c.get("created_at")) + (str(c.get("id")),))
        sequences = [c.get("sequence") for c in ordered]
        expected = list(range(1, len(ordered) + 1))
        if sequences != expected:
            out.append(_finding("L9", FAIL, ISSUES, (issue_key,),
                                f"comment sequence values {sequences} are not 1..{len(ordered)} "
                                f"in (created_at, id) order"))
    return out


def _rule_l10(overlay: Overlay) -> list[Finding]:
    out: list[Finding] = []
    issues = _all_issues(overlay)
    teams = overlay.state.get(TEAMS) or {}
    for op in overlay.ops:
        if op.table != TEAMS or op.op != "update":
            continue
        if "issue_counter" not in dict(op.cols):
            continue
        key = tuple(dict(op.where).get(col) for col in ("id",))
        team = teams.get(key)
        if team is None:
            out.append(_finding("L10", FAIL, TEAMS, key, "team does not exist after the update"))
            continue
        numbers = [row.get("number") for row in issues.values()
                   if row.get("team_id") == key[0]
                   and isinstance(row.get("number"), int) and not isinstance(row.get("number"), bool)]
        expected = (max(numbers) if numbers else 0) + 1
        if team.get("issue_counter") != expected:
            out.append(_finding("L10", FAIL, TEAMS, key,
                                f"issue_counter={team.get('issue_counter')!r}, "
                                f"expected max issue number + 1 = {expected}"))
    return out


def _rule_l11(overlay: Overlay) -> list[Finding]:
    out: list[Finding] = []
    issues = _all_issues(overlay)
    for key, row in _rows(overlay, PROJECTS):
        if overlay.kind(PROJECTS, key) != "insert":
            continue
        owned = [issue.get("updated_at") for issue in issues.values()
                 if issue.get("project_id") == row.get("id")]
        owned = [stamp for stamp in owned if stamp is not None]
        if not owned:
            continue
        newest = max(owned, key=_order)
        if _order(row.get("updated_at")) < _order(newest):
            out.append(_finding("L11", WARN, PROJECTS, key,
                                f"updated_at {row.get('updated_at')!r} < newest project issue "
                                f"updated_at {newest!r}"))
    return out


def _rule_l12(overlay: Overlay) -> list[Finding]:
    out: list[Finding] = []
    issues = _all_issues(overlay)
    for key, row in _rows(overlay, ISSUES):
        parent_id = row.get("parent_id")
        if parent_id is None:
            continue
        issue_id = row.get("id", key[0] if key else None)
        parent = issues.get((parent_id,))
        if parent is None:
            out.append(_finding("L12", FAIL, ISSUES, key,
                                f"parent_id {parent_id!r} does not exist"))
            continue
        if parent.get("team_id") != row.get("team_id"):
            # WARN, not FAIL: 129 base issues in each universe have a parent in another team (corroborate L12)
            out.append(_finding("L12", WARN, ISSUES, key,
                                f"parent {parent_id!r} is in team {parent.get('team_id')!r}, "
                                f"issue is in {row.get('team_id')!r}"))
        seen = {issue_id}
        cursor = parent_id
        while cursor is not None:
            if cursor in seen:
                out.append(_finding("L12", FAIL, ISSUES, key,
                                    f"parent chain cycles at {cursor!r}"))
                break
            seen.add(cursor)
            ancestor = issues.get((cursor,))
            cursor = ancestor.get("parent_id") if ancestor else None
    return out


# --------------------------------------------------------------------------- entry points

def check_linear(overlay: Overlay, base: dict, *, freeze_utc: str) -> list[Finding]:
    """Run L1-L12 on rows inserted or updated by `overlay`."""
    findings: list[Finding] = []
    findings += _rule_l1(overlay)
    findings += _rule_l2(overlay, base)
    findings += _rule_l3(overlay)
    findings += _rule_l4(overlay, base)
    findings += _rule_l5(overlay)
    findings += _rule_l6(overlay)
    findings += _rule_l7(overlay)
    findings += _rule_l8(overlay)
    findings += _rule_l9(overlay)
    findings += _rule_l10(overlay)
    findings += _rule_l11(overlay)
    findings += _rule_l12(overlay)

    # L5's freeze bound is the only rule that reads the clock.
    freeze = _parse_ts(freeze_utc)
    for key, row in _inserted_comments(overlay):
        created = _parse_ts(row.get("created_at"))
        if freeze is not None and created is not None and not created < freeze:
            findings.append(_finding("L5", FAIL, COMMENTS, key,
                                     f"created_at {row.get('created_at')!r} is not before the "
                                     f"freeze {freeze_utc!r}"))
    return sorted(findings, key=lambda f: (f.rule, f.table, str(f.key), f.message))


def corroborate(base: dict) -> dict:
    """Evaluate L1, L4 and L12 over every base issue and summarise base facts."""
    issue_keys = list((base.get(ISSUES) or {}).keys())
    fake = Overlay(state=base, inserted={ISSUES: []}, updated={ISSUES: list(issue_keys)},
                   errors=[], ops=[])
    findings = check_linear(fake, base, freeze_utc="9999-12-31T23:59:59Z")

    rules: dict[str, dict] = {}
    for rule in ("L1", "L4", "L12"):
        failed: dict[tuple, list[str]] = {}
        for finding in findings:
            if finding.rule == rule:
                failed.setdefault(finding.key, []).append(finding.message)
        checked = len(issue_keys)
        passed = checked - len(failed)
        rules[rule] = {
            "checked": checked,
            "passed": passed,
            "pass_rate": round(passed / checked, 4) if checked else None,
            "exceptions": [{"key": key[0] if key else None, "reasons": reasons}
                           for key, reasons in list(failed.items())[:20]],
        }

    teams = []
    max_by_key: dict[str, int] = {}
    issues = base.get(ISSUES) or {}
    for team in (base.get(TEAMS) or {}).values():
        numbers = [row.get("number") for row in issues.values()
                   if row.get("team_id") == team.get("id")
                   and isinstance(row.get("number"), int) and not isinstance(row.get("number"), bool)]
        top = max(numbers) if numbers else 0
        teams.append({"id": team.get("id"), "key": team.get("key"), "max_number": top,
                      "issues": len(numbers)})
        max_by_key[team.get("key")] = top

    return {
        "issues": len(issue_keys),
        "base_comments": len(base.get(COMMENTS) or {}),
        "state_types": state_types(base),
        "teams": sorted(teams, key=lambda t: str(t.get("key"))),
        "max_number_by_team_key": max_by_key,
        **rules,
    }

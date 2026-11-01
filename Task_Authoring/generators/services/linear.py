"""Linear emitter: spec records -> ordered operations (projects, issues, comments, derived companions).

Record kinds and fields (strict: unknown fields fail; required fields have no defaults):
  linear.project      required id team name summary description lead priority state labels created_at
                      optional color (convention: schema default '#bec2c8') icon uuid links start_date target_date
                               started_at completed_at canceled_at start_date_resolution target_date_resolution
                               is_archived updated_at
  linear.issue        required id team title state creator assignee description project parent priority labels relations
                               created_at started_at completed_at canceled_at
                      optional estimate due_date cycle uuid links updated_at
  linear.comment      required id issue author created_at body
                      optional parent is_edited
  linear.issue_update required issue; optional state assignee project title description priority labels started_at
                               completed_at canceled_at updated_at (an authored change to a base issue)
  linear.team_update  required team issue_counter (issue_counter: transform linear.next_issue_number/1)

Derived (conventions/conventions.json; each derived column records its function and convention in the provenance):
  issue.number, issue.identifier        from id <TEAMKEY>-<n>                         linear.issue.identity
  issue.state_history_json '[]', links_json '[]' unless authored, archived_at NULL, time_in_status_minutes NULL,
  is_archived false                                                                   linear.issue.state_history_empty,
                                                                                      linear.issue.links_empty
  issue.updated_at                      max(created_at, started_at, completed_at, canceled_at, newest spec comment)
                                        unless authored
  base issue with newer comments or an issue_update
                                        UPDATE ... SET updated_at = max(newest comment, stamps the update sets) when
                                        that is newer than the base value, unless authored
                                                                                      linear.issue.updated_at_follows_comments
  comment.updated_at = created_at, is_edited false unless authored, sequence = 1..n per issue in (created_at, id) order
                                                                                      linear.comment.shape
  project.color '#bec2c8' unless authored                                             linear.project.color_default
  project.updated_at                    newest of its own created_at and its issues' and their comments' stamps unless
                                        authored                                      linear.project.updated_at_follows_issues
  team.issue_counter                    max(number of the team's base and spec issues) + 1   linear.team.issue_counter

Statement order (no platform meaning inside one transaction; parents always precede children): projects by id; issues
by (team key, number); comments grouped by issue in that order, then (created_at, id); base-issue updates by (team key,
number); team updates by team key.
"""
from __future__ import annotations

import datetime as dt
import re
import uuid

from ..core.ops import INSERT, UPDATE, Op
from ..core.sqlvalue import json_text
from ..core.values import SpecError

SERVICE = "linear"
VERSION = "linear/1.0"

KINDS = {
    "linear.project": {
        "required": {"id", "team", "name", "summary", "description", "lead", "priority", "state", "labels",
                     "created_at"},
        "optional": {"color", "icon", "uuid", "links", "start_date", "target_date", "started_at", "completed_at",
                     "canceled_at", "start_date_resolution", "target_date_resolution", "is_archived", "updated_at"},
    },
    "linear.issue": {
        "required": {"id", "team", "title", "state", "creator", "assignee", "description", "project", "parent",
                     "priority", "labels", "relations", "created_at", "started_at", "completed_at", "canceled_at"},
        "optional": {"estimate", "due_date", "cycle", "uuid", "links", "updated_at"},
    },
    "linear.comment": {
        "required": {"id", "issue", "author", "created_at", "body"},
        "optional": {"parent", "is_edited"},
    },
    "linear.issue_update": {
        "required": {"issue"},
        "optional": {"state", "assignee", "project", "title", "description", "priority", "labels", "started_at",
                     "completed_at", "canceled_at", "updated_at"},
    },
    "linear.team_update": {"required": {"team", "issue_counter"}, "optional": set()},
}

# convention id -> record kinds that rely on it (empty tuple: every Linear render)
CONVENTIONS = {
    "sql.literal_policy": (),
    "sql.json_text": (),
    "linear.text_dates": (),
    "linear.issue.identity": ("linear.issue",),
    "linear.issue.state_history_empty": ("linear.issue",),
    "linear.issue.links_empty": ("linear.issue",),
    "linear.issue.lifecycle": ("linear.issue", "linear.issue_update"),
    "linear.issue.updated_at_follows_comments": ("linear.issue", "linear.comment", "linear.issue_update"),
    "linear.comment.shape": ("linear.comment",),
    "linear.project.color_default": ("linear.project",),
    "linear.project.updated_at_follows_issues": ("linear.project",),
    "linear.team.issue_counter": ("linear.team_update",),
}

ISSUE_ID = re.compile(r"^([A-Z]+)-([1-9][0-9]*)$")
TS_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
TS_TEXT = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$")   # ASCII digits only
PROJECT_DEFAULT_COLOR = "#bec2c8"
NEW_ISSUE_DEFAULTS = {"links_json": "[]", "state_history_json": "[]", "archived_at": None,
                      "time_in_status_minutes": None, "is_archived": False}
ISSUE_COLUMNS = ("id", "uuid", "project_id", "team_id", "parent_id", "assignee_id", "creator_id", "state_id",
                 "cycle_id", "identifier", "number", "title", "description", "priority", "estimate", "due_date",
                 "started_at", "completed_at", "canceled_at", "archived_at", "time_in_status_minutes", "labels_json",
                 "links_json", "relations_json", "state_history_json", "is_archived", "created_at", "updated_at")
COMMENT_COLUMNS = ("id", "issue_id", "author_id", "parent_id", "body", "is_edited", "created_at", "updated_at",
                   "sequence")
PROJECT_COLUMNS = ("id", "team_id", "name", "summary", "description", "lead_id", "priority", "state", "start_date",
                   "target_date", "uuid", "icon", "color", "started_at", "completed_at", "canceled_at",
                   "start_date_resolution", "target_date_resolution", "labels_json", "links_json", "is_archived",
                   "created_at", "updated_at")
UPDATE_FIELDS = (("state", "state_id"), ("assignee", "assignee_id"), ("project", "project_id"), ("title", "title"),
                 ("description", "description"), ("priority", "priority"), ("started_at", "started_at"),
                 ("completed_at", "completed_at"), ("canceled_at", "canceled_at"))


def _ts(value, where: str) -> dt.datetime:
    try:
        if not TS_TEXT.match(value):
            raise ValueError(value)
        return dt.datetime.strptime(value, TS_FORMAT).replace(tzinfo=dt.timezone.utc)
    except (TypeError, ValueError):
        raise SpecError(where, f"timestamp {value!r} is not YYYY-MM-DDTHH:MM:SSZ") from None


def _max_ts(values: list[str], where: str) -> str:
    return max(values, key=lambda v: _ts(v, where))


def comment_uuid(inputs: dict) -> str:
    """linear.comment_uuid/1: uuid5(namespace, name) — deterministic comment ids."""
    try:
        return str(uuid.uuid5(uuid.UUID(inputs["namespace"]), inputs["name"]))
    except (KeyError, ValueError, TypeError, AttributeError) as exc:
        raise ValueError(f"linear.comment_uuid/1 needs namespace (uuid) and name: {exc}") from exc


# None: computed by expand() from the post-state, never resolved on its own.
TRANSFORMS = {"linear.comment_uuid/1": comment_uuid, "linear.next_issue_number/1": None}


def _derived(fn: str, convention: str, inputs=()) -> dict:
    p = {"origin": "derived", "construction": "transform", "fn": fn, "convention": convention}
    if inputs:
        p["inputs"] = list(inputs)
    return p


def _json_col(value, where: str) -> str:
    if not isinstance(value, list):
        raise SpecError(where, "must be a JSON array")
    try:
        return json_text(value)
    except (TypeError, ValueError) as exc:
        raise SpecError(where, f"cannot serialize as JSON: {exc}") from None


def expand(records: list, resolver, base) -> list[Op]:
    """records: spec records of this service ({key, kind, fields}); resolver(record, field) -> (value, provenance)."""
    teams = base.records("linear", "teams")
    users = base.records("linear", "users")
    base_issues = base.records("linear", "issues")
    base_projects = base.records("linear", "projects")
    base_comments = base.records("linear", "comments")

    def val(rec, name, default=None, optional=False, convention=None):
        if name in rec["fields"]:
            return resolver(rec, name)
        if optional:
            prov = {"origin": "default", "construction": "default", "value": default}
            if convention:
                prov["convention"] = convention
            return default, prov
        raise SpecError(f"{rec['key']}.{name}", "required field missing")

    def need_user(rec, name, value, nullable):
        if value is None and nullable:
            return
        if value not in users:
            raise SpecError(f"{rec['key']}.{name}", f"user {value!r} is not in the pinned base")

    by_kind = {k: [] for k in KINDS}
    for rec in records:
        by_kind[rec["kind"]].append(rec)

    project_ids = {}
    for rec in by_kind["linear.project"]:
        pid, _ = val(rec, "id")
        if not isinstance(pid, str) or not pid:
            raise SpecError(f"{rec['key']}.id", "project id must be a non-empty string")
        if pid in base_projects or pid in project_ids:
            raise SpecError(f"{rec['key']}.id", f"project {pid} already exists (base or spec)")
        project_ids[pid] = rec

    # ---- issues
    issues = {}
    for rec in by_kind["linear.issue"]:
        k = rec["key"]
        iid, p_id = val(rec, "id")
        m = ISSUE_ID.match(iid if isinstance(iid, str) else "")
        if not m:
            raise SpecError(f"{k}.id", f"issue id {iid!r} is not <TEAMKEY>-<number>")
        team_id, p_team = val(rec, "team")
        team = teams.get(team_id)
        if team is None:
            raise SpecError(f"{k}.team", f"team {team_id!r} is not in the pinned base")
        if team["key"] != m.group(1):
            raise SpecError(f"{k}.id", f"{iid} does not start with team key {team['key']}")
        if iid in base_issues:
            raise SpecError(f"{k}.id", f"{iid} already exists in the base export")
        if iid in issues:
            raise SpecError(f"{k}.id", f"{iid} is declared twice")
        row, prov = {}, {}

        def put(col, field, default=None, optional=False, convention=None):
            row[col], prov[col] = val(rec, field, default, optional, convention)

        row["id"], prov["id"] = iid, p_id
        put("uuid", "uuid", None, True)
        put("project_id", "project")
        if row["project_id"] is not None and row["project_id"] not in project_ids \
                and row["project_id"] not in base_projects:
            raise SpecError(f"{k}.project", f"project {row['project_id']!r} is neither in the spec nor in the base")
        row["team_id"], prov["team_id"] = team_id, p_team
        put("parent_id", "parent")
        put("assignee_id", "assignee")
        need_user(rec, "assignee", row["assignee_id"], True)
        put("creator_id", "creator")
        need_user(rec, "creator", row["creator_id"], True)
        put("state_id", "state")
        put("cycle_id", "cycle", None, True)
        row["identifier"], prov["identifier"] = iid, _derived("linear.identifier/1", "linear.issue.identity", ["id"])
        row["number"], prov["number"] = int(m.group(2)), _derived("linear.number/1", "linear.issue.identity", ["id"])
        put("title", "title")
        put("description", "description")
        put("priority", "priority")
        put("estimate", "estimate", None, True)
        put("due_date", "due_date", None, True)
        put("started_at", "started_at")
        put("completed_at", "completed_at")
        put("canceled_at", "canceled_at")
        labels, prov["labels_json"] = val(rec, "labels")
        relations, prov["relations_json"] = val(rec, "relations")
        links, prov["links_json"] = val(rec, "links", [], True, "linear.issue.links_empty")
        row["labels_json"] = _json_col(labels, f"{k}.labels")
        row["relations_json"] = _json_col(relations, f"{k}.relations")
        row["links_json"] = _json_col(links, f"{k}.links")
        for col in ("archived_at", "time_in_status_minutes", "state_history_json", "is_archived"):
            row[col] = NEW_ISSUE_DEFAULTS[col]
            prov[col] = _derived("linear.new_issue_defaults/1", "linear.issue.state_history_empty"
                                 if col == "state_history_json" else "linear.issue.links_empty")
        put("created_at", "created_at")
        _ts(row["created_at"], f"{k}.created_at")
        if "updated_at" in rec["fields"]:
            put("updated_at", "updated_at")
        issues[iid] = {"row": row, "prov": prov, "rec": rec, "sort": (team["key"], int(m.group(2)))}

    def issue_sort(iid):
        if iid in issues:
            return issues[iid]["sort"]
        b = base_issues[iid]
        return teams.get(b.get("team_id"), {}).get("key", ""), int(b.get("number") or 0)

    for iid, info in issues.items():
        parent = info["row"]["parent_id"]
        if parent is None:
            continue
        if parent not in issues and parent not in base_issues:
            raise SpecError(f"{info['rec']['key']}.parent", f"parent {parent!r} is neither in the spec nor in the base")
        if parent in issues and issue_sort(parent) >= info["sort"]:
            raise SpecError(f"{info['rec']['key']}.parent", f"parent {parent} sorts after its child {iid}; "
                                                            "a parent must have the lower number")

    # ---- comments
    comments, by_issue = {}, {}
    for rec in by_kind["linear.comment"]:
        k = rec["key"]
        cid, p_id = val(rec, "id")
        if not isinstance(cid, str) or not cid:
            raise SpecError(f"{k}.id", "comment id must be a non-empty string")
        if cid in comments or cid in base_comments:
            raise SpecError(f"{k}.id", f"comment id {cid} is declared twice or exists in the base")
        row, prov = {"id": cid}, {"id": p_id}
        row["issue_id"], prov["issue_id"] = val(rec, "issue")
        if row["issue_id"] not in issues and row["issue_id"] not in base_issues:
            raise SpecError(f"{k}.issue", f"issue {row['issue_id']!r} is neither in the spec nor in the base")
        row["author_id"], prov["author_id"] = val(rec, "author")
        need_user(rec, "author", row["author_id"], False)
        row["parent_id"], prov["parent_id"] = val(rec, "parent", None, True, "linear.comment.shape")
        row["body"], prov["body"] = val(rec, "body")
        row["is_edited"], prov["is_edited"] = val(rec, "is_edited", False, True, "linear.comment.shape")
        row["created_at"], prov["created_at"] = val(rec, "created_at")
        when = _ts(row["created_at"], f"{k}.created_at")
        row["updated_at"] = row["created_at"]
        prov["updated_at"] = _derived("linear.comment_updated_at/1", "linear.comment.shape", ["created_at"])
        comments[cid] = {"row": row, "prov": prov, "rec": rec, "when": when}
        by_issue.setdefault(row["issue_id"], []).append(comments[cid])

    for cid, c in comments.items():
        parent = c["row"]["parent_id"]
        if parent is None:
            continue
        p = comments.get(parent)
        if p is None:
            raise SpecError(f"{c['rec']['key']}.parent", f"parent comment {parent!r} is not in the spec")
        if p["row"]["issue_id"] != c["row"]["issue_id"] or not p["when"] < c["when"]:
            raise SpecError(f"{c['rec']['key']}.parent", f"parent comment {parent} must be on the same issue and "
                                                         "earlier")

    for iid, lst in by_issue.items():
        lst.sort(key=lambda c: (c["when"], c["row"]["id"]))
        for n, c in enumerate(lst, 1):
            c["row"]["sequence"] = n
            c["prov"]["sequence"] = _derived("linear.comment_sequence/1", "linear.comment.shape",
                                             ["issue_id", "created_at", "id"])

    for iid, info in issues.items():
        row = info["row"]
        if "updated_at" not in row:
            stamps = [row[c] for c in ("created_at", "started_at", "completed_at", "canceled_at") if row[c]]
            stamps += [c["row"]["created_at"] for c in by_issue.get(iid, [])]
            row["updated_at"] = _max_ts(stamps, f"{info['rec']['key']}.updated_at")
            info["prov"]["updated_at"] = _derived("linear.issue_updated_at/1",
                                                  "linear.issue.updated_at_follows_comments",
                                                  ["created_at", "started_at", "completed_at", "canceled_at",
                                                   "comments.created_at"])
        info["row"] = {c: row[c] for c in ISSUE_COLUMNS}

    # ---- base issues: authored updates + derived updated_at (before projects: an update can move an issue into one)
    explicit = {}
    for rec in by_kind["linear.issue_update"]:
        target, _ = val(rec, "issue")
        if target not in base_issues:
            raise SpecError(f"{rec['key']}.issue", f"{target!r} is not a base issue")
        if target in explicit:
            raise SpecError(rec["key"], f"{target} has two issue_update records")
        sets, prov = {}, {}
        for field, col in UPDATE_FIELDS:
            if field in rec["fields"]:
                sets[col], prov[col] = val(rec, field)
        if "assignee_id" in sets:
            need_user(rec, "assignee", sets["assignee_id"], True)
        if sets.get("project_id") is not None and sets["project_id"] not in project_ids \
                and sets["project_id"] not in base_projects:
            raise SpecError(f"{rec['key']}.project", f"project {sets['project_id']!r} is neither in the spec nor "
                                                     "in the base")
        if "labels" in rec["fields"]:
            labels, prov["labels_json"] = val(rec, "labels")
            sets["labels_json"] = _json_col(labels, f"{rec['key']}.labels")
        if "updated_at" in rec["fields"]:
            sets["updated_at"], prov["updated_at"] = val(rec, "updated_at")
        if not sets:
            raise SpecError(rec["key"], "an issue_update must set at least one field")
        explicit[target] = (sets, prov, rec["key"])
    updates = {}
    for iid in sorted(set(explicit) | {i for i in by_issue if i in base_issues}, key=issue_sort):
        sets, prov, rkey = explicit.get(iid, ({}, {}, None))
        sets, prov = dict(sets), dict(prov)
        if "updated_at" not in sets:
            stamps = [c["row"]["created_at"] for c in by_issue.get(iid, [])]
            stamps += [sets[c] for c in ("started_at", "completed_at", "canceled_at") if sets.get(c)]
            current = base_issues[iid].get("updated_at")
            if stamps:
                newest = _max_ts(stamps, f"{iid}.updated_at")
                if not current or _ts(current, f"base {iid}.updated_at") < _ts(newest, iid):
                    sets["updated_at"] = newest
                    prov["updated_at"] = _derived("linear.base_issue_updated_at/1",
                                                  "linear.issue.updated_at_follows_comments",
                                                  ["base.updated_at", "comments.created_at", "update stamps"])
        if sets:
            updates[iid] = (sets, prov, rkey)

    def final(iid, col):
        """A base issue's value after this spec's update."""
        sets = updates.get(iid, ({},))[0]
        return sets[col] if col in sets else base_issues[iid].get(col)

    # ---- projects
    project_ops = []
    for pid, rec in project_ids.items():
        k = rec["key"]
        row, prov = {"id": pid}, {}
        _, prov["id"] = val(rec, "id")
        row["team_id"], prov["team_id"] = val(rec, "team")
        if row["team_id"] not in teams:
            raise SpecError(f"{k}.team", f"team {row['team_id']!r} is not in the pinned base")
        for col, field in (("name", "name"), ("summary", "summary"), ("description", "description"),
                           ("lead_id", "lead"), ("priority", "priority"), ("state", "state")):
            row[col], prov[col] = val(rec, field)
        need_user(rec, "lead", row["lead_id"], True)
        for col in ("start_date", "target_date", "uuid", "icon"):
            row[col], prov[col] = val(rec, col, None, True)
        row["color"], prov["color"] = val(rec, "color", PROJECT_DEFAULT_COLOR, True, "linear.project.color_default")
        for col in ("started_at", "completed_at", "canceled_at", "start_date_resolution", "target_date_resolution"):
            row[col], prov[col] = val(rec, col, None, True)
        labels, prov["labels_json"] = val(rec, "labels")
        links, prov["links_json"] = val(rec, "links", [], True)
        row["labels_json"] = _json_col(labels, f"{k}.labels")
        row["links_json"] = _json_col(links, f"{k}.links")
        row["is_archived"], prov["is_archived"] = val(rec, "is_archived", False, True)
        row["created_at"], prov["created_at"] = val(rec, "created_at")
        if "updated_at" in rec["fields"]:
            row["updated_at"], prov["updated_at"] = val(rec, "updated_at")
        else:
            mine = [i["row"]["id"] for i in issues.values() if i["row"]["project_id"] == pid]
            moved = [iid for iid in updates if final(iid, "project_id") == pid]
            stamps = ([row["created_at"]] + [issues[i]["row"][c] for i in mine for c in ("created_at", "updated_at")]
                      + [final(i, c) for i in moved for c in ("created_at", "updated_at") if final(i, c)]
                      + [c["row"]["created_at"] for i in mine + moved for c in by_issue.get(i, [])])
            row["updated_at"] = _max_ts(stamps, f"{k}.updated_at")
            prov["updated_at"] = _derived("linear.project_updated_at/1", "linear.project.updated_at_follows_issues",
                                          ["created_at", "issues.created_at", "issues.updated_at",
                                           "comments.created_at"])
        project_ops.append(Op("linear.linear_projects", INSERT, tuple((c, row[c]) for c in PROJECT_COLUMNS),
                              record=k, prov=tuple((c, prov[c]) for c in PROJECT_COLUMNS)))
    project_ops.sort(key=lambda op: op.col("id"))

    issue_ops = [Op("linear.linear_issues", INSERT, tuple(info["row"].items()), record=info["rec"]["key"],
                    prov=tuple((c, info["prov"][c]) for c in ISSUE_COLUMNS))
                 for _, info in sorted(issues.items(), key=lambda kv: kv[1]["sort"])]
    comment_ops = [Op("linear.linear_comments", INSERT, tuple((c, cm["row"][c]) for c in COMMENT_COLUMNS),
                      record=cm["rec"]["key"], prov=tuple((c, cm["prov"][c]) for c in COMMENT_COLUMNS))
                   for iid in sorted(by_issue, key=issue_sort) for cm in by_issue[iid]]

    update_ops = [Op("linear.linear_issues", UPDATE, tuple(sets.items()), where=(("id", iid),), record=rkey,
                     prov=tuple(prov.items())) for iid, (sets, prov, rkey) in updates.items()]

    # ---- team counters
    team_ops, seen_teams = [], set()
    for rec in by_kind["linear.team_update"]:
        team_id, _ = val(rec, "team")
        team = teams.get(team_id)
        if team is None:
            raise SpecError(f"{rec['key']}.team", f"team {team_id!r} is not in the pinned base")
        if team_id in seen_teams:
            raise SpecError(rec["key"], f"{team_id} has two team_update records")
        seen_teams.add(team_id)
        prov = dict(resolver.computed(rec, "issue_counter", "linear.next_issue_number/1"),
                    convention="linear.team.issue_counter")
        numbers = [int(i.get("number") or 0) for i in base_issues.values() if i.get("team_id") == team_id]
        numbers += [info["sort"][1] for info in issues.values() if info["row"]["team_id"] == team_id]
        counter = max(numbers, default=0) + 1
        team_ops.append((team["key"], Op("linear.linear_teams", UPDATE, (("issue_counter", counter),),
                                         where=(("id", team_id),), record=rec["key"],
                                         prov=(("issue_counter", prov),))))
    team_ops = [op for _, op in sorted(team_ops, key=lambda t: t[0])]
    return project_ops + issue_ops + comment_ops + update_ops + team_ops


def key_of(op: Op) -> tuple:
    if op.op == UPDATE:
        return tuple(v for _, v in op.where)
    return (op.col("id"),)

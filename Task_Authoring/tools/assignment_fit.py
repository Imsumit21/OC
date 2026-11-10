#!/usr/bin/env python3
"""assignment_fit.py - does the base data fit this persona and assignment? (plan WS9, items 1, 4, 5, 6)

Run at the goal stage, before the scenario is designed. It never skips a task and never changes the persona: it
tells the author which route to take.

  census      --task-dir T [--write] [--json]
              --persona KEY --universe normal|synthcut --function F --competency C --horizon H --mode M   (no task folder)
              Reach per service with the roster rank and a THIN flag, cohort candidates for the competency, the
              base-surface gaps that touch them, an open-population flag and a verdict:
                FIT                 a closed base collection of cohort size exists and nothing limits it
                FIT WITH LIMITS     a collection exists; each limit is named (a thin service, no closed rule, gaps)
                NO NATURAL COHORT   no base collection of cohort size for this persona and competency:
                                    the scenario is built by injection (plan WS9 item 3). Never "skip".
              --write stores Working_Files/00_Assignment_Fit.json and .md in the task folder.
  surface-map --universe U [--write]
              Per service and record type: does base hold real content (count; for comment-like types, people or
              bots), can it be injected, are reads scoped to the persona. Written to references/base_surface_map.json.
  card        --persona KEY --universe U [--write]      one persona card (reach, thin services, candidates per
  cards       --write                                   competency, what earlier tasks used, base issues they met)
  --self-test                                           stub universe; needs no base data

How the universe is read. persona_view.Universe reads whatever universe the active task context names. This tool
binds a universe-level context (same source paths and clocks as a task of that date, one shared cache folder per
universe under support/local_search/cache/) so the census of one persona and universe is the same for every task.
The binding is undone when the read ends.

Rules (thresholds are module constants below; the thin-search minimum comes from references/first_pass_policy.json)
  THIN service  Gmail, Slack, Calendar: fewer than THIN_MIN records dated in the THIN_WINDOW_DAYS before the data
                clock in the persona's view (a date-window search near the task date returns almost nothing).
                Drive: fewer than THIN_MIN visible files. A THIN service cannot hold an anchor or variance unit.
  Candidate     a base collection the persona can read, of at least the cohort size (40 long-horizon, 10 normal),
                that belongs to the competency (references/competency_collections.json): a Linear team or project,
                a GitHub repository, a Trello board, a Slack channel the persona is a member of (threads with
                replies), a sheet tab the persona owns or is shared on (data rows).
  Closed rule   membership is defined by the container (issues in project X, rows of a tab). A Slack channel is an
                open rule: which threads belong is decided by reading them, and replies are search-sweepable.
  Dormant       no activity in the ACTIVE_WINDOW_DAYS before the clock; or the name dates it to a period that ended
                more than ACTIVE_WINDOW_DAYS before the clock ('20232024'); or the name retires it ('DO NOT USE').
                A dormant collection is listed, never counted.
  Earlier tasks completed (support/completed_tasks) and skipped (archived_tasks) tasks for the persona. On an archived
                task (a backtest) only tasks dated before it are shown, and --write is refused.

Surface map: a record type is injectable when the eval's injection schema holds its table and the authoring lint
allows it. The known entries of plan WS9 item 4 are each checked against the exports, the schema, the archived SQL
and the stored platform reports, never copied.

Exit: 0 census ran (any verdict), 1 the census could not run, 2 usage error. Stdlib only; reads base exports, never
writes Evals/, claude/ or a universe folder.
"""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import json
import mmap
import os
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
BUNDLE = HERE.parent
WS = BUNDLE.parent

import task_context as tc  # noqa: E402

TOOL = "assignment_fit"
VERSION = 1
CHECK_ID = "fit.census"
POLICY = BUNDLE / "references" / "first_pass_policy.json"
SURFACE_MAP = BUNDLE / "references" / "base_surface_map.json"
SURFACE_SCHEMA = "base-surface-map-v1"
COMPETENCY_MAP = BUNDLE / "references" / "competency_collections.json"
CARDS = BUNDLE / "references" / "persona_cards"
CARD_SCHEMA = "persona-card-v1"
COMPLETED = BUNDLE / "support" / "completed_tasks"
ARCHIVED = BUNDLE / "archived_tasks"          # skipped tasks: the task folder itself, no task_inputs/
FIT_JSON = "00_Assignment_Fit.json"
FIT_MD = "00_Assignment_Fit.md"
UNIVERSES = ("normal", "synthcut")

# ---- thresholds (not in first_pass_policy.json; listed in the report so the lead can move them there)
COHORT_MIN = {"long-horizon": 40, "normal": 10}   # the brief: 40 members for long-horizon, 10 for normal
THIN_MIN_DEFAULT = 10            # used only when the policy file has no path_exposure.thin_search_min_results
THIN_WINDOW_DAYS = 90            # "near the task date": the quarter before the data clock
ACTIVE_WINDOW_DAYS = 180         # a collection untouched for longer is dormant: listed, not counted
CONTAINER_ABOVE = 500            # a larger collection is a container to carve a closed subset from (KB range tops at 500)
SHEET_HEADER_ROWS = 1            # rows of a tab that are not members
TOP_CANDIDATES = 12              # candidates printed per census (all are kept in the JSON)
GMAIL_WINDOWS = (30, 90, 180)    # extra Gmail window counts shown beside the THIN measure
BORDERLINE_SHARE = 0.25          # a THIN measure within this share of the minimum is marked borderline
SCAN_VERSION = 2                 # bump when a cached scan changes shape

SCOPED = ("slack", "gmail", "gcal", "drive")
SERVICE_LABEL = {"slack": "Slack", "gmail": "Gmail", "gcal": "Calendar", "drive": "Drive"}
FIT, LIMITS, NO_COHORT = "FIT", "FIT WITH LIMITS", "NO NATURAL COHORT"
_ENV_KEYS = ("TASK_AUTHORING_TASK_DIR", "TASK_AUTHORING_CONTEXT_HASH", "TASK_AUTHORING_LEGACY_V2",
             "TASK_AUTHORING_UNIVERSE")
_PATCHED = ("TASK_CONTEXT", "CLOCK", "DATA_CLOCK", "CACHE", "GMAIL_INDEX", "OTHER", "GMAIL", "GITHUB",
            "SLACK_MSGS", "KB", "OUT")
ADDRESS = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+|\b[A-Z]+_\d{4}_EMAIL\b")
OPEN_LINEAR_STATES = ("Done", "Canceled", "Duplicate")


class FitError(Exception):
    """The census could not run (exit 1)."""


# ---------------------------------------------------------------- small helpers

def _sha256(path) -> str | None:
    try:
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    except OSError:
        return None


def _read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def _write(path: Path, text: str, what: str) -> None:
    """Atomic write; refuses the read-only workspace folders."""
    tc.refuse_read_only(path, what)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix="." + path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            os.fchmod(fh.fileno(), 0o644)
            fh.write(text)
        os.replace(tmp, path)
    except BaseException:
        if os.path.lexists(tmp):
            os.unlink(tmp)
        raise


def _dump(obj) -> str:
    return json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def _norm(text) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(text or "").casefold()).strip()


def _day(value) -> str | None:
    return str(value)[:10] if value else None


def _parse(value) -> dt.datetime | None:
    """ISO-8601 text or epoch seconds -> aware UTC datetime."""
    if value in (None, ""):
        return None
    try:
        return dt.datetime.fromtimestamp(float(value), dt.timezone.utc)
    except (TypeError, ValueError):
        pass
    try:
        d = dt.datetime.fromisoformat(str(value).strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)


def _age_days(value, clock) -> int | None:
    d = _parse(value)
    return None if d is None else (clock - d).days


def thin_min() -> int:
    policy = _read_json(POLICY) or {}
    value = (policy.get("path_exposure") or {}).get("thin_search_min_results")
    return int(value) if isinstance(value, int) and value > 0 else THIN_MIN_DEFAULT


def horizon_key(value) -> str:
    v = _norm(value)
    if v in ("normal", "normal horizon"):
        return "normal"
    if v in ("long", "long horizon"):
        return "long-horizon"
    raise FitError(f"unknown horizon {value!r}: use normal or long-horizon")


def universe_key(value) -> str:
    v = _norm(value).replace(" ", "")
    for key in UNIVERSES:
        if v == key:
            return key
    if v in ("synthcut", "oct12025", "20251001"):
        return "synthcut"
    if v in ("feb142026", "20260214"):
        return "normal"
    raise FitError(f"unknown universe {value!r}: use normal (Feb 14, 2026) or synthcut (Oct 1, 2025)")


# ---------------------------------------------------------------- competency map

def load_competencies(path=COMPETENCY_MAP) -> dict:
    data = _read_json(path)
    if not isinstance(data, dict) or not isinstance(data.get("competencies"), dict):
        raise FitError(f"cannot read the competency map {path}")
    return data


def competency_entry(name, data=None) -> tuple:
    """(canonical name, entry). The label is matched on letters and digits only, through each entry's aliases."""
    data = data or load_competencies()
    want = _norm(name)
    for key, entry in sorted(data["competencies"].items()):
        if want in {_norm(key), *(_norm(a) for a in entry.get("aliases") or [])}:
            return key, entry
    raise FitError(f"unknown competency {name!r}: the map has {', '.join(sorted(data['competencies']))}")


def _tokens(name) -> list:
    return _norm(name).split()


def keyword_hit(name, keywords) -> str | None:
    """The first keyword found in `name` as whole words. A keyword ending in * matches a word prefix."""
    words = _tokens(name)
    for kw in keywords or ():
        parts = _norm(kw.rstrip("*")).split()
        if not parts:
            continue
        prefix = kw.endswith("*")
        for i in range(len(words) - len(parts) + 1):
            head, last = words[i:i + len(parts) - 1], words[i + len(parts) - 1]
            if head == parts[:-1] and (last.startswith(parts[-1]) if prefix else last == parts[-1]):
                return kw
    return None


def belongs(coll: dict, entry: dict) -> str | None:
    """Why a collection belongs to a competency (None when it does not)."""
    kind = coll["kind"]
    if kind in (entry.get("all_of_kind") or ()):
        return f"every {kind.replace('_', ' ')} belongs to this competency"
    names = (entry.get("named") or {}).get(kind) or ()
    if any(_norm(n) in (_norm(coll.get("key")), _norm(coll.get("name"))) for n in names):
        return "named in the competency map"
    if kind in (entry.get("keyword_kinds") or ()):
        hit = keyword_hit(coll.get("match_name") or coll.get("name"), entry.get("keywords"))
        if hit:
            return f"name matches '{hit}'"
    return None


# ---------------------------------------------------------------- universe binding

def universe_context(key: str) -> dict:
    """A context for one universe with no task folder: same source and clocks as a task of that date."""
    if key not in UNIVERSES:
        raise FitError(f"unknown universe {key!r}")
    try:
        block = tc.universe_block(key)
        policy = tc._json(tc.POLICY_PATH)
        freeze = policy["freeze_dates"][block["date"]]
        source = tc.source_context(block["date"], freeze)
    except (tc.ContextError, KeyError) as exc:
        raise FitError(f"cannot bind the {key} universe: {exc}") from exc
    if source.get("status") != "ready":
        raise FitError(f"the {key} universe source is not ready: {source.get('reason')}")
    context = {"spec_version": "V3", "scope": "universe", "universe": block, "universe_date_key": block["date"],
               "freeze_utc": freeze, "source": source}
    context["context_hash"] = tc.digest({"scope": "universe", "universe": key,
                                         "source_fingerprint": source["fingerprint"]})
    return context


@contextlib.contextmanager
def reading(key: str):
    """Point persona_view and base_check at one universe for the length of the block, then put everything back."""
    import runtime_context as rc
    import persona_view  # noqa: F401  (must be loaded so the binding reaches it)
    import base_check    # noqa: F401  (persona_view builds its Gmail index through it)
    context = universe_context(key)
    modules = [sys.modules[name] for name in rc.MODULES if name in sys.modules]
    saved_env = {k: os.environ.get(k) for k in _ENV_KEYS}
    saved = [{k: vars(m)[k] for k in _PATCHED if k in vars(m)} for m in modules]
    for k in _ENV_KEYS:
        os.environ.pop(k, None)
    try:
        for module in modules:
            rc._apply(vars(module), context, force=True)
        yield context
    finally:
        for module, names in zip(modules, saved):
            for k in _PATCHED:
                if k in names:
                    vars(module)[k] = names[k]
                elif k == "TASK_CONTEXT":
                    vars(module).pop(k, None)
        for k, v in saved_env.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


# ---------------------------------------------------------------- base source (real exports)

class BaseSource:
    """Reads one universe through persona_view plus a few extra passes. Use inside `reading(key)`."""

    def __init__(self, key: str, context: dict):
        import persona_view as pv
        self.key, self.context, self.pv = key, context, pv
        self.u = pv.Universe()
        self.clock = pv.DATA_CLOCK
        self.label = context["universe"]["label"]
        self.fingerprint = context["source"]["fingerprint"]
        self._reach = {}

    # -- roster
    def personas(self) -> list:
        return [p for p in self.pv.personas() if p.get("usable_in_tasks")]

    def persona(self, query: str) -> dict:
        q = str(query).strip().casefold()
        for p in self.pv.personas():
            if q in (p["persona_key"].casefold(), p["email"].casefold(), p["name"].casefold()):
                return p
        raise FitError(f"unknown persona {query!r}: use a persona_key, the roster email or the exact name")

    # -- reach
    def reach(self, p: dict) -> dict:
        key = p["persona_key"]
        if key not in self._reach:
            self._reach[key] = self.pv.reach(self.u, p, top=5, correspondents=False)
        return self._reach[key]

    def slack_uid(self, p: dict):
        return self.u.slack_uid(p["email"])

    def gmail_detail(self, p: dict) -> dict:
        """Sent count, last sent date, threads in the recent window and the senders a search would hide among."""
        pv, clock, mailbox = self.pv, self.clock, p["email"]

        def build():
            threads = [(f, last) for _t, (mb, _n, _first, last, f) in self.u.gmail()["threads"].items()
                       if mb == mailbox]
            ages = [_age_days(last, clock) for _f, last in threads]
            windows = {str(w): sum(1 for a in ages if a is not None and 0 <= a <= w)
                       for w in sorted(set(GMAIL_WINDOWS) | {THIN_WINDOW_DAYS})}
            recent = windows[str(THIN_WINDOW_DAYS)]
            senders, sent, sent_last = Counter(), 0, None
            for f, _last in threads:
                try:
                    data = pv._load(pv.GMAIL / "threads" / f)
                except (OSError, ValueError):
                    continue
                for m in data.get("messages", []):
                    found = ADDRESS.findall(str(m.get("from") or ""))
                    sender = found[-1].lower() if found else "?"
                    senders[sender] += 1
                    if sender == mailbox.lower():
                        sent += 1
                        when = pv.parse_dt(m.get("date"))
                        if when and (sent_last is None or when > sent_last):
                            sent_last = when
            last_day = sent_last.astimezone(dt.timezone.utc).date().isoformat() if sent_last else None
            return {"threads": len(threads), "recent_threads": recent, "windows": windows, "sent": sent,
                    "sent_last": last_day,
                    "senders": [[a, n] for a, n in sorted(senders.items(), key=lambda kv: (-kv[1], kv[0]))[:40]]}
        if mailbox not in self.u.gmail_mailboxes():
            return {"threads": 0, "recent_threads": 0, "windows": {}, "sent": 0, "sent_last": None, "senders": []}
        self.u.gmail()                       # the index file must exist before the cache fingerprints it
        return pv.cached(f"af_gmail_v{SCAN_VERSION}_w{THIN_WINDOW_DAYS}_{p['persona_key']}",
                         [pv.GMAIL_INDEX, pv.GMAIL / "users.json"], build)

    def recent(self, p: dict) -> dict:
        """Records dated in the thin window, per dated service, in the persona's view."""
        clock, pe = self.clock, p["email"]

        def within(value):
            age = _age_days(value, clock)
            return age is not None and 0 <= age <= THIN_WINDOW_DAYS
        uid = self.slack_uid(p)
        slack = sum(c["recent"] for c in self.collections()["slack_channels"] if uid and uid in c["members"])
        own = {c for c, x in self.u.gcal()["calendars"].items() if x["owner"] == pe or pe in (x["shared"] or [])}
        gcal = sum(1 for e in self.u.gcal()["events"].values() if e[0] in own and within(e[3]))
        return {"slack": slack, "gcal": gcal}

    def drive_access(self, file_id: str, p: dict) -> str | None:
        rec = self.u.drive().get(file_id)
        if not rec:
            return None
        if rec[2] == p["email"]:
            return "owner"
        return "shared" if p["email"] in (rec[3] or []) else None

    def drive_modified(self, file_id: str):
        rec = self.u.drive().get(file_id)
        return rec[5] if rec else None

    # -- collections (persona-independent; one cached pass per universe)
    def collections(self) -> dict:
        pv = self.pv
        sources = [pv.OTHER / "linear" / "data.json", pv.GITHUB, pv.OTHER / "trello" / "data.json",
                   pv.OTHER / "slack" / "users.json", pv.OTHER / "slack" / "channels.json", pv.SLACK_MSGS,
                   pv.OTHER / "gsheets" / "data.json", pv.OTHER / "gdrive" / "data.json"]
        return self.u._get("af_collections", lambda: pv.cached(
            f"af_collections_v{VERSION}_w{THIN_WINDOW_DAYS}", sources, lambda: _scan_collections(pv, self.clock)))

    def surface_counts(self) -> dict:
        pv = self.pv
        sources = [pv.OTHER / "linear" / "data.json", pv.GITHUB, pv.OTHER / "trello" / "data.json",
                   pv.OTHER / "confluence" / "confluence_working.json", pv.OTHER / "contacts" / "contacts.json",
                   pv.OTHER / "gcal" / "data.json", pv.OTHER / "gdrive" / "data.json", pv.OTHER / "gdocs" / "data.json",
                   pv.OTHER / "gslides" / "data.json", pv.OTHER / "gsheets" / "data.json",
                   pv.OTHER / "slack" / "files.json", pv.OTHER / "snowflake" / "snowflake.json", pv.SLACK_MSGS,
                   pv.GMAIL_INDEX]
        self.u.gmail()                       # the index file must exist before the cache fingerprints it
        return pv.cached(f"af_surface_v{SCAN_VERSION}", sources, lambda: _scan_surface(pv, self))


def _scan_slack(pv) -> tuple:
    """Per channel: messages, messages in the thin window, threads with replies started by a person, last date.
    Also the workspace totals the surface map needs."""
    users = {u["id"]: u for u in pv._load(pv.OTHER / "slack" / "users.json")}
    channels = {c["id"]: c for c in pv._load(pv.OTHER / "slack" / "channels.json")}
    clock = pv.DATA_CLOCK
    floor = (clock - dt.timedelta(days=THIN_WINDOW_DAYS)).timestamp()
    ceiling = clock.timestamp()
    out, totals = [], Counter()

    def automated(m) -> bool:
        return bool(m.get("subtype") == "bot_message" or m.get("bot_id")
                    or (users.get(m.get("user")) or {}).get("is_bot"))
    for cid in sorted(os.listdir(pv.SLACK_MSGS)):
        folder = pv.SLACK_MSGS / cid
        if not folder.is_dir():
            continue
        n = recent = 0
        last, roots, replied = None, {}, Counter()
        for shard in sorted(os.listdir(folder)):
            for m in pv._load(folder / shard):
                try:
                    ts = float(m.get("ts"))
                except (TypeError, ValueError):
                    continue
                n += 1
                recent += floor <= ts <= ceiling
                last = ts if last is None or ts > last else last
                bot = automated(m)
                thread = m.get("thread_ts")
                if thread and thread != m.get("ts"):
                    replied[thread] += 1
                    totals["replies_automated" if bot else "replies_people"] += 1
                else:
                    roots[m.get("ts")] = bot
                    totals["roots_automated" if bot else "roots_people"] += 1
        c = channels.get(cid) or {}
        kind = "im" if c.get("is_im") else "mpim" if c.get("is_mpim") else "private" if c.get("is_private") else "public"
        threads = sum(1 for ts in replied if roots.get(ts) is False)
        out.append({"kind": "slack_channel", "service": "slack", "key": cid,
                    "name": c.get("name") or cid, "channel_kind": kind if c else "unknown",
                    "archived": bool(c.get("is_archived")), "members": c.get("members") or [],
                    "size": threads, "messages": n, "recent": recent, "last_activity": pv.ts_date(last)})
    return out, dict(totals)


def _scan_sheets(pv) -> list:
    """One entry per tab: rows that hold at least one value. Streams the export line by line."""
    path = pv.OTHER / "gsheets" / "data.json"
    out, tabs, file_id, title = [], [], None, None
    rows = 0
    in_row = filled = False
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("              "):          # a cell (indent 14)
                if in_row and not filled:
                    cell = line.strip().rstrip(",")
                    filled = cell not in ('""', "null", "")
                continue
            if line.startswith("            ["):            # a grid row opens (indent 12)
                in_row, filled = True, False
                if line.rstrip().rstrip(",").endswith("]"):  # an empty row on one line
                    in_row = False
                continue
            if line.startswith("            ]"):            # a grid row closes
                rows += filled
                in_row = False
                continue
            if line.startswith('          "title": '):      # a tab closes (title is its last key)
                tabs.append([json.loads(line.strip()[len('"title": '):].rstrip(",")), rows])
                rows = 0
                continue
            if line.startswith('      "drive_file_id": '):
                file_id = json.loads(line.strip()[len('"drive_file_id": '):].rstrip(","))
                continue
            if line.startswith('      "title": '):
                title = json.loads(line.strip()[len('"title": '):].rstrip(","))
                continue
            if line.startswith("    }"):                    # a spreadsheet closes
                for index, (tab, count) in enumerate(tabs):
                    out.append({"kind": "sheet_tab", "service": "gsheets", "key": f"{file_id}#{index}",
                                "file_id": file_id, "name": f"{title} / {tab}", "sheet": title, "tab": tab,
                                "size": max(0, count - SHEET_HEADER_ROWS)})
                tabs, file_id, title = [], None, None
    return out


def _scan_collections(pv, clock) -> dict:
    """Every base container a cohort could come from, with its size and last activity."""
    linear = pv._load(pv.OTHER / "linear" / "data.json")
    teams, projects = [], []
    by_team, by_project = {}, {}
    for issue in linear.get("issues") or []:
        when = issue.get("updated_at") or issue.get("created_at")
        for bucket, key in ((by_team, issue.get("team_id")), (by_project, issue.get("project_id"))):
            if key:
                slot = bucket.setdefault(key, {"n": 0, "open": 0, "last": None})
                slot["n"] += 1
                slot["open"] += issue.get("state_id") not in OPEN_LINEAR_STATES
                if when and (slot["last"] is None or when > slot["last"]):
                    slot["last"] = when
    for team in linear.get("teams") or []:
        slot = by_team.get(team["id"], {"n": 0, "open": 0, "last": None})
        teams.append({"kind": "linear_team", "service": "linear", "key": team.get("key"), "name": team.get("name"),
                      "match_name": f"{team.get('key')} {team.get('name')}", "size": slot["n"], "open": slot["open"],
                      "last_activity": _day(slot["last"])})
    for project in linear.get("projects") or []:
        slot = by_project.get(project["id"], {"n": 0, "open": 0, "last": None})
        projects.append({"kind": "linear_project", "service": "linear", "key": project["id"],
                         "name": project.get("name"), "size": slot["n"], "open": slot["open"],
                         "last_activity": _day(slot["last"])})

    repos, prs = {}, {}
    fields = {"id", "name", "repo_id", "updated_at", "created_at", "archived"}
    for coll, rec in pv.iter_records(pv.GITHUB, fields, {"repositories", "pull_requests"}):
        if coll == "repositories":
            repos[rec["id"]] = rec
        else:
            slot = prs.setdefault(rec.get("repo_id"), {"n": 0, "last": None})
            slot["n"] += 1
            when = rec.get("updated_at") or rec.get("created_at")
            if when and (slot["last"] is None or when > slot["last"]):
                slot["last"] = when
    github = [{"kind": "github_repo", "service": "github", "key": r.get("name"), "name": r.get("name"),
               "size": prs.get(rid, {}).get("n", 0), "last_activity": _day(prs.get(rid, {}).get("last"))}
              for rid, r in sorted(repos.items(), key=lambda kv: str(kv[1].get("name")))]

    trello = pv._load(pv.OTHER / "trello" / "data.json")
    boards = []
    commented = Counter()
    for action in trello.get("actions") or []:
        if action.get("type") == "commentCard":
            commented[action.get("idCard")] += 1
    for board in trello.get("boards") or []:
        if board.get("closed"):
            continue
        cards = [c for c in trello.get("cards") or [] if c.get("idBoard") == board["id"]]
        last = max((c.get("dateLastActivity") or "" for c in cards), default="") or None
        boards.append({"kind": "trello_board", "service": "trello", "key": board["id"], "name": board.get("name"),
                       "size": len(cards), "open": sum(1 for c in cards if not c.get("closed")),
                       "cards_with_comments": sum(1 for c in cards if commented.get(c["id"])),
                       "last_activity": _day(last)})

    channels, slack_totals = _scan_slack(pv)
    sheets = _scan_sheets(pv)      # sharing and edit dates come from the Drive record, per persona
    return {"linear_teams": teams, "linear_projects": projects, "github_repos": github, "trello_boards": boards,
            "slack_channels": channels, "sheet_tabs": sheets, "slack_totals": slack_totals,
            "clock": clock.isoformat()}


# ---------------------------------------------------------------- surface map (plan WS9 item 4)

AUTOMATED_MOSTLY = 0.8          # a comment type with this share of automated authors is "mostly_automated"
SCOPED_SERVICES = ("gmail", "slack", "gcal", "gdrive", "gdocs", "gsheets", "gslides")   # acl.md access matrix
# (service, record type, injection table, kind, note). kind: record | comment (authors split) | file | field
SURFACE_SPEC = (
    ("slack", "channels", "slack.slack_channels", "record", ""),
    ("slack", "messages", "slack.slack_messages", "comment", "top-level posts"),
    ("slack", "thread_replies", "slack.slack_messages", "comment",
     "channel history shows thread roots only; replies need a thread read or a search"),
    ("slack", "files", "slack.slack_files", "file", "names and metadata only; file content is not served (acl.md)"),
    ("gmail", "threads", "gmail.gmail_threads", "record", ""),
    ("gmail", "messages", "gmail.gmail_messages", "record", ""),
    ("gmail", "attachments", "gmail.gmail_attachments", "file",
     "names only; attachment reads return no bytes (acl.md); not counted here"),
    ("gcal", "events", "gcal.gcal_events", "record", ""),
    ("gcal", "event_descriptions", "gcal.gcal_events", "field", "events with a description or a location"),
    ("gdrive", "files", "gdrive.drive_files", "record", "files and folders"),
    ("gdocs", "documents", "gdocs.docs_documents", "record", ""),
    ("gsheets", "spreadsheets", "gsheets.sheets_spreadsheets", "record", ""),
    ("gsheets", "tabs", "gsheets.sheets_sheets", "record", "one read returns every row of a tab"),
    ("gslides", "presentations", "gslides.slides_presentations", "record", ""),
    ("github", "repositories", "github.github_repositories", "record", ""),
    ("github", "pull_requests", "github.github_pull_requests", "record", ""),
    ("github", "reviews", "github.github_reviews", "comment", "review summaries"),
    ("github", "review_comments", "github.github_review_comments", "comment",
     "inline comments; not returned by the reviews list"),
    ("github", "pull_request_comments", "github.github_pr_comments", "comment", "PR conversation comments"),
    ("github", "issues", "github.github_issues", "record", ""),
    ("github", "commits", "github.github_commits", "record", ""),
    ("github", "releases", "github.github_releases", "record", ""),
    ("linear", "teams", "linear.linear_teams", "record", ""),
    ("linear", "projects", "linear.linear_projects", "record", ""),
    ("linear", "issues", "linear.linear_issues", "record", "the list call returns state, labels and description"),
    ("linear", "comments", "linear.linear_comments", "comment", "one call per issue"),
    ("linear", "attachments", "linear.linear_attachments", "record", "files with real content (acl.md)"),
    ("trello", "boards", "trello.trello_boards", "record", ""),
    ("trello", "cards", "trello.trello_cards", "record", ""),
    ("trello", "comments", "trello.trello_actions", "comment", "commentCard actions"),
    ("trello", "checklists", "trello.trello_checklists", "record", ""),
    ("confluence", "pages", "confluence.confluence_pages", "record", ""),
    ("confluence", "page_versions", "confluence.confluence_page_versions", "record", ""),
    ("confluence", "comments", "confluence.confluence_comments", "comment", ""),
    ("contacts", "contacts", "contacts.contacts", "record", ""),
    ("snowflake", "tables", None, "record", "warehouse tables; rows are not counted (one 2 GB line)"),
)
# What the plan lists as known (WS9 item 4). Each is checked against the data, never copied.
PLAN_NOT_INJECTABLE = ("snowflake", "confluence")
ARCHIVED_SQL = ("support/completed_tasks/*/task_inputs/01_Universe_Inject.sql", "archived_tasks/*/01_Universe_Inject.sql")


def _count_bytes(path: Path, needle: bytes) -> int | None:
    """Occurrences of `needle` in a file of any size, without loading it."""
    try:
        with open(path, "rb") as fh, mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ) as mm:
            n, at = 0, mm.find(needle)
            while at != -1:
                n, at = n + 1, mm.find(needle, at + len(needle))
            return n
    except (OSError, ValueError):
        return None


def _authors(rows, is_person, clock=None) -> dict:
    """Author split of comment-like rows (container, author[, date]). With a clock, also the rows by people dated
    in the ACTIVE_WINDOW_DAYS before it and the date of the last one before it."""
    mine = [r for r in rows if is_person(r[1])]
    out = {"count": len(rows), "people": len(mine), "automated": len(rows) - len(mine),
           "containers_with_people": len({r[0] for r in mine})}
    if clock is not None:
        ages = [(_age_days(r[2], clock), _day(r[2])) for r in mine if len(r) > 2 and r[2]]
        before = [(a, d) for a, d in ages if a is not None and a >= 0]
        out["people_in_window"] = sum(1 for a, _d in before if a <= ACTIVE_WINDOW_DAYS)
        out["people_last"] = max((d for _a, d in before), default=None)
    return out


def _scan_surface(pv, source) -> dict:
    """Raw counts per service and record type, straight from the exports."""
    other, out, clock = pv.OTHER, {}, pv.DATA_CLOCK
    linear = pv._load(other / "linear" / "data.json")
    people = {u["id"] for u in linear.get("users") or []}
    comments = [(c.get("issue_id"), c.get("author_id"), c.get("created_at")) for c in linear.get("comments") or []]
    out["linear"] = {"teams": {"count": len(linear.get("teams") or [])},
                     "projects": {"count": len(linear.get("projects") or [])},
                     "issues": {"count": len(linear.get("issues") or [])},
                     "comments": dict(_authors(comments, lambda a: a in people, clock),
                                      containers=len(linear.get("issues") or [])),
                     "attachments": {"count": len(linear.get("attachments") or [])}}

    counts, kinds = Counter(), {}
    rows = {"reviews": [], "review_comments": [], "pull_request_comments": []}
    fields = {"login", "type", "pr_id", "author_login", "created_at", "submitted_at"}
    for coll, rec in pv.iter_records(pv.GITHUB, fields, None):
        counts[coll] += 1
        if coll == "users":
            kinds[rec.get("login")] = rec.get("type")
        elif coll in rows:
            rows[coll].append((rec.get("pr_id"), rec.get("author_login"),
                               rec.get("created_at") or rec.get("submitted_at")))
    github = {name: {"count": counts.get(name, 0)}
              for name in ("repositories", "pull_requests", "issues", "commits", "releases")}
    for name, items in rows.items():
        github[name] = dict(_authors(items, lambda a: kinds.get(a) == "User", clock),
                            containers=counts.get("pull_requests", 0))
    out["github"] = github

    trello = pv._load(other / "trello" / "data.json")
    members = {m["id"] for m in trello.get("members") or []}
    notes = [(a.get("idCard"), a.get("idMemberCreator"), a.get("date")) for a in trello.get("actions") or []
             if a.get("type") == "commentCard"]
    out["trello"] = {"boards": {"count": len(trello.get("boards") or [])},
                     "cards": {"count": len(trello.get("cards") or [])},
                     "comments": dict(_authors(notes, lambda a: a in members, clock),
                                      containers=len(trello.get("cards") or [])),
                     "checklists": {"count": len(trello.get("checklists") or [])}}

    conf = pv._load(other / "confluence" / "confluence_working.json")
    authors = {u["id"] for u in conf.get("users") or []}
    remarks = [(c.get("page_id"), c.get("author_id"), c.get("created_at") or c.get("created"))
               for c in conf.get("comments") or []]
    out["confluence"] = {"pages": {"count": len(conf.get("pages") or [])},
                         "page_versions": {"count": len(conf.get("page_versions") or [])},
                         "comments": dict(_authors(remarks, lambda a: a in authors, clock),
                                          containers=len(conf.get("pages") or []))}
    out["contacts"] = {"contacts": {"count": len(pv._load(other / "contacts" / "contacts.json").get("contacts") or [])}}

    cols = source.collections()
    totals = cols.get("slack_totals") or {}
    out["slack"] = {"channels": {"count": len(pv._load(other / "slack" / "channels.json"))},
                    "messages": {"count": totals.get("roots_people", 0) + totals.get("roots_automated", 0),
                                 "people": totals.get("roots_people", 0), "automated": totals.get("roots_automated", 0)},
                    "thread_replies": {"count": totals.get("replies_people", 0) + totals.get("replies_automated", 0),
                                       "people": totals.get("replies_people", 0),
                                       "automated": totals.get("replies_automated", 0)},
                    "files": {"count": len(source.u.slack_files())}}
    boxes = source.u.gmail()["mailboxes"]
    out["gmail"] = {"threads": {"count": sum(b["threads"] for b in boxes.values())},
                    "messages": {"count": sum(b["messages"] for b in boxes.values())},
                    "attachments": {"count": None}}
    events = described = 0
    for _coll, rec in pv.iter_records(other / "gcal" / "data.json", {"description", "location"}, {"events"}):
        events += 1
        described += bool(rec.get("description") or rec.get("location"))
    out["gcal"] = {"events": {"count": events}, "event_descriptions": {"count": described}}
    out["gdrive"] = {"files": {"count": len(source.u.drive())}}
    out["gdocs"] = {"documents": {"count": sum(1 for _ in pv.iter_records(other / "gdocs" / "data.json",
                                                                         {"document_id"}, {"docs_documents"}))}}
    out["gslides"] = {"presentations": {"count": sum(1 for _ in pv.iter_records(
        other / "gslides" / "data.json", {"presentation_id"}, {"slides_presentations"}))}}
    tabs = cols.get("sheet_tabs") or []
    out["gsheets"] = {"spreadsheets": {"count": len({t["file_id"] for t in tabs})}, "tabs": {"count": len(tabs)}}
    out["snowflake"] = {"tables": {"count": _count_bytes(other / "snowflake" / "snowflake.json", b'"table_type"')}}
    return out


def injection_tables() -> dict:
    """Where each table may be written, from the bundle's own sources (text reads; nothing is executed)."""
    import sql_lint
    live = {f"{t['table_schema']}.{t['table_name']}" for t in _read_json(sql_lint.LIVE_SCHEMA) or []}
    path = sql_lint.INJECTION_SCHEMA if sql_lint.INJECTION_SCHEMA.is_file() else sql_lint.EVAL_INJECTION_SCHEMA
    listed = {f"{t['table_schema']}.{t['table_name']}" for t in _read_json(path) or []}
    return {"lint": set(sql_lint.WRITABLE_TABLES), "eval_schema": listed, "live": live,
            "eval_schema_file": str(path.relative_to(WS)) if path.is_file() else None}


def archived_injections(root=BUNDLE) -> dict:
    """Statements per service in the archived tasks' injection SQL (text scan): what was injected in practice."""
    out, files = {}, []
    for pattern in ARCHIVED_SQL:
        files += sorted(Path(root).glob(pattern))
    for path in files:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        seen = Counter(m.group(1).lower() for m in re.finditer(
            r"(?im)^\s*(?:insert\s+into|update|delete\s+from)\s+([a-z_]+)\.[a-z_]+", text))
        for schema, n in seen.items():
            slot = out.setdefault(schema, {"tasks": 0, "statements": 0})
            slot["tasks"] += 1
            slot["statements"] += n
    return {"files_read": len(files), "by_service": out}


PLATFORM_REPORTS = ("support/completed_tasks/*/eval_reports/**/*.md", "archived_tasks/*/plateform_reports/**/*.md",
                    "archived_tasks/*/*_injection*.md")
_NEG = r"(?:can.?t|cannot|can not|won.?t|will not|never|does not|doesn.?t)"
_VERB = r"(?:edit(?:ed)?|writ(?:e|ten)|inject(?:ed)?|load|appear|change)"


def _no_injection_patterns(service: str) -> list:
    """Sentences in which a platform report says injection cannot reach a service."""
    s = re.escape(service)
    return [re.compile(rf"(?i)\binjection(?: sql)?\b[^.\n|]{{0,30}}\b{_NEG}\s+(?:be\s+)?{_VERB}\b[^.\n|]{{0,15}}\b{s}\b"),
            re.compile(rf"(?i)\b{s}\b[^.\n|]{{0,15}}\b{_NEG}\s+(?:actually\s+)?(?:be\s+)?{_VERB}\b[^.\n|]{{0,20}}"
                       rf"\binjection"),
            re.compile(rf"(?i)\b{s}\b\s+(?:can.?t|cannot)\s+be\s+edited")]


def platform_statements(services=None, root=BUNDLE) -> dict:
    """Platform reports (stored per archived task) that say injection SQL cannot change a service. Text scan."""
    services = services or PLAN_NOT_INJECTABLE
    files = []
    for pattern in PLATFORM_REPORTS:
        files += sorted(Path(root).glob(pattern))
    out = {s: {"reports": 0, "tasks": [], "example": None} for s in services}
    for path in sorted(set(files)):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        parts = path.relative_to(root).parts
        task = parts[2] if parts[0] == "support" else parts[1]
        for service in services:
            hit = next((m for p in _no_injection_patterns(service) for m in [p.search(text)] if m), None)
            if hit:
                slot = out[service]
                slot["reports"] += 1
                if task not in slot["tasks"]:
                    slot["tasks"].append(task)
                slot["example"] = slot["example"] or hit.group(0).strip()[:120]
    return {"reports_read": len(set(files)), "by_service": out}


def _content(kind: str, raw: dict) -> str:
    count = raw.get("count")
    if count is None:
        return "not_counted"
    if count == 0:
        return "none"
    if kind == "file":
        return "metadata_only"
    if kind == "comment":
        share = raw.get("automated", 0) / count
        return "automated_only" if share >= 1 else "mostly_automated" if share >= AUTOMATED_MOSTLY else "real"
    return "real"


def _injectable(table, tables: dict, said: dict) -> tuple:
    """(injectable, basis). Injectable means the eval's injection schema (the database injection SQL targets) holds
    the table and the authoring lint allows it. A table only the lint allows is not injectable; the basis names the
    disagreement and the platform reports that say so."""
    if not table:
        return False, "no injection table: the injection file cannot change this service"
    lint, schema = table in tables["lint"], table in tables["eval_schema"]
    if lint and schema:
        return True, "in the eval injection schema and the authoring lint allowlist"
    if schema:
        return False, "in the eval injection schema but not in the authoring lint allowlist (sql_lint.WRITABLE_TABLES)"
    text = "not in the eval injection schema"
    if lint:
        text += "; the authoring lint (sql_lint.WRITABLE_TABLES) still allows it"
    if said.get("reports"):
        text += f"; {said['reports']} platform report(s) say injection SQL cannot change it"
    return False, text


def surface_section(raw: dict, tables: dict, archived: dict, clock=None, fingerprint=None) -> dict:
    """One universe's part of the surface map, from raw counts."""
    services = {}
    said_all = (archived.get("platform_statements") or {}).get("by_service") or {}
    for service, rtype, table, kind, note in SURFACE_SPEC:
        counts = (raw.get(service) or {}).get(rtype) or {"count": None}
        entry = {"count": counts.get("count"), "base_content": _content(kind, counts),
                 "reads_scoped": service in SCOPED_SERVICES, "inject_table": table}
        if kind == "comment":
            entry["authors"] = {"people": counts.get("people", 0), "automated": counts.get("automated", 0)}
            for key in ("people_in_window", "people_last"):
                if key in counts:
                    entry["authors"][key] = counts[key]
            if "containers" in counts:
                entry["containers"] = counts["containers"]
                entry["containers_with_people"] = counts.get("containers_with_people", 0)
        entry["injectable"], entry["injectable_basis"] = _injectable(table, tables, said_all.get(service) or {})
        entry["in_authoring_lint"] = bool(table) and table in tables["lint"]
        entry["in_eval_injection_schema"] = bool(table) and table in tables["eval_schema"]
        if note:
            entry["note"] = note
        slot = services.setdefault(service, {"reads_scoped": service in SCOPED_SERVICES, "record_types": {},
                                             "archived_injections": (archived.get("by_service") or {}).get(
                                                 service, {"tasks": 0, "statements": 0})})
        slot["record_types"][rtype] = entry
    section = {"services": services, "known_entries": known_entries(services, archived)}
    if clock:
        section["clock"] = clock
    if fingerprint:
        section["source_fingerprint"] = fingerprint
    return section


def known_entries(services: dict, archived: dict) -> list:
    """The plan's known entries, each confirmed or not against the data."""
    def rt(service, rtype):
        return ((services.get(service) or {}).get("record_types") or {}).get(rtype) or {}
    out = []
    lc = rt("linear", "comments")
    out.append({"claim": "base Linear has no comments",
                "status": "confirmed" if lc.get("count") == 0 else "not confirmed",
                "evidence": f"{lc.get('count')} Linear comments in base"})
    pc = rt("github", "pull_request_comments")
    a = pc.get("authors") or {}
    people, total = a.get("people", 0), pc.get("count") or 0
    status = "confirmed" if total and not people else "partly" if pc.get("base_content") == "mostly_automated" \
        else "not confirmed"
    recent = (f"; {a['people_in_window']} by people in the {ACTIVE_WINDOW_DAYS} days before the clock, last "
              f"{a.get('people_last') or 'never'}") if "people_in_window" in a else ""
    out.append({"claim": "base PR conversation comments are bots only", "status": status,
                "evidence": f"{total - people} of {total} are automated (bots or integrations); {people} are by people, "
                            f"on {pc.get('containers_with_people', 0)} of {pc.get('containers', 0)} pull requests"
                            + recent})
    by = archived.get("by_service") or {}
    said_all = (archived.get("platform_statements") or {}).get("by_service") or {}
    for service in PLAN_NOT_INJECTABLE:
        types = ((services.get(service) or {}).get("record_types") or {})
        schema = sorted(t for t, e in types.items() if e.get("in_eval_injection_schema"))
        lint = sorted(t for t, e in types.items() if e.get("in_authoring_lint"))
        seen = by.get(service, {"tasks": 0, "statements": 0})
        said = said_all.get(service) or {"reports": 0, "tasks": []}
        status = ("not confirmed" if schema else "confirmed" if said.get("reports") or not lint else "likely")
        evidence = (f"the eval injection schema holds {len(schema)} of its tables; "
                    f"{said.get('reports', 0)} platform report(s) in {len(said.get('tasks') or [])} task(s) say "
                    f"injection SQL cannot change it"
                    + (f" (\"{said['example']}\")" if said.get("example") else "")
                    + f"; the authoring lint allows {len(lint)} record type(s) ({', '.join(lint) or 'none'}); "
                      f"{seen['statements']} statement(s) in {seen['tasks']} of {archived.get('files_read', 0)} "
                      f"archived injections")
        entry = {"claim": f"{service.capitalize()} cannot be injected", "status": status, "evidence": evidence}
        if status == "confirmed" and lint:
            entry["conflict"] = (f"sql_lint.WRITABLE_TABLES lists {service} tables (Injection Schema Guideline "
                                 f"2026-10-22) although the platform does not load them; "
                                 f"{seen['tasks']} archived task(s) wrote {seen['statements']} statement(s) there")
        out.append(entry)
    return out


_EVIDENCE: dict = {}


def injection_evidence() -> tuple:
    """(tables, archived) read once per process: the bundle's injection rules, the archived SQL and the platform
    reports do not change while a census runs."""
    if "value" not in _EVIDENCE:
        _EVIDENCE["value"] = (injection_tables(),
                              dict(archived_injections(), platform_statements=platform_statements()))
    return _EVIDENCE["value"]


def build_surface(source) -> dict:
    tables, archived = injection_evidence()
    return surface_section(source.surface_counts(), tables, archived,
                           clock=source.clock.isoformat(), fingerprint=source.fingerprint)


def gaps_for(coll: dict, section: dict) -> list:
    """Base-surface gaps that touch one candidate."""
    def rt(service, rtype):
        return ((section["services"].get(service) or {}).get("record_types") or {}).get(rtype) or {}
    kind, gaps = coll["kind"], []
    if kind in ("linear_team", "linear_project"):
        e = rt("linear", "comments")
        if e.get("base_content") == "none":
            gaps.append("Linear comments: none in base, so per-issue notes are injected and stand alone")
    elif kind == "github_repo":
        e = rt("github", "pull_request_comments")
        if e.get("base_content") in ("automated_only", "mostly_automated", "none"):
            a = e.get("authors") or {}
            last = f"; last by a person {a['people_last']}" if a.get("people_last") else ""
            gaps.append(f"PR conversation comments: {a.get('automated', 0)} of {e.get('count', 0)} are automated "
                        f"({a.get('people', 0)} by people, on {e.get('containers_with_people', 0)} pull requests{last})")
        if rt("github", "issues").get("base_content") == "none":
            gaps.append("GitHub issues: none in base")
    elif kind == "trello_board":
        gaps.append(f"{coll.get('cards_with_comments', 0)} of {coll['size']} cards have a comment")
    elif kind == "slack_channel":
        gaps.append("open rule: which threads belong is decided by reading them; a search returns replies in bulk")
        if rt("slack", "files").get("base_content") == "metadata_only":
            gaps.append("Slack file content is not served")
    elif kind == "sheet_tab":
        gaps.append("one read returns every row: rows have no records of their own in the sheet")
    return gaps


# ---------------------------------------------------------------- reach, ranks, thin services

def _volumes(reach: dict) -> dict:
    s = reach["services"]
    return {"slack": s["slack"]["messages_visible"], "gmail": s["gmail"].get("threads", 0) or 0,
            "gcal": s["gcal"]["events_visible"],
            "drive": s["drive"]["owned_total"] + s["drive"]["shared_with_total"]}


def reach_table(source, persona: dict, minimum: int) -> dict:
    """Numbers per scoped service, the persona's rank in the usable roster and the THIN flag with its reason."""
    roster = {p["persona_key"]: _volumes(source.reach(p)) for p in source.personas()}
    mine = _volumes(source.reach(persona))
    roster.setdefault(persona["persona_key"], mine)
    s = source.reach(persona)["services"]
    detail, recent = source.gmail_detail(persona), source.recent(persona)
    window = f"the {THIN_WINDOW_DAYS} days before the clock"
    hay = [[a, n] for a, n in detail.get("senders") or [] if n >= minimum and a != persona["email"].lower()]
    table = {
        "slack": {"channels": s["slack"]["channels_visible"], "messages": mine["slack"],
                  "posts": s["slack"]["persona_messages_posted"], "last_post": s["slack"]["persona_last_post"],
                  "recent": recent["slack"]},
        "gmail": {"threads": mine["gmail"], "messages": s["gmail"].get("messages", 0) or 0,
                  "last": _day(s["gmail"].get("last")), "sent": detail["sent"], "sent_last": detail["sent_last"],
                  "recent": detail["recent_threads"], "windows": detail.get("windows") or {},
                  "senders_with_haystack": hay[:8]},
        "gcal": {"events": mine["gcal"], "last_event": _day(s["gcal"]["last_event_start_before_clock"]),
                 "recent": recent["gcal"]},
        "drive": {"files": mine["drive"], "owned": s["drive"]["owned_total"], "shared": s["drive"]["shared_with_total"],
                  "native": s["drive"]["native_visible"], "last_modified": _day(s["drive"]["last_modified_visible"])},
    }
    for service, row in table.items():
        row["rank"] = 1 + sum(1 for v in roster.values() if v[service] > mine[service])
        row["of"] = len(roster)
        measure, unit = (row["files"], "visible files") if service == "drive" else (
            row["recent"], {"slack": "messages", "gmail": "threads", "gcal": "events"}[service] + f" dated in {window}")
        row["thin"] = measure < minimum
        row["thin_measure"] = measure
        row["borderline"] = abs(measure - minimum) <= max(1, round(BORDERLINE_SHARE * minimum))
        row["why"] = f"{measure} {unit} (minimum {minimum}" + ("; borderline" if row["borderline"] else "") + ")"
    return table


def thin_limit(service: str, row: dict) -> str:
    text = f"{SERVICE_LABEL[service]} is thin: no anchor or variance unit there ({row['why']}"
    if service == "gmail":
        text += f"; {row['threads']} threads, {row['sent']} sent, last sent {row['sent_last'] or 'never'}"
        other = [f"{n} in {w} days" for w, n in sorted((row.get("windows") or {}).items(), key=lambda kv: int(kv[0]))
                 if int(w) != THIN_WINDOW_DAYS]
        if other:
            text += "; " + ", ".join(other)
    return text + ")"


# ---------------------------------------------------------------- cohort candidates

RULE = {"linear_team": ("issues", "issues in Linear team {key}"),
        "linear_project": ("issues", "issues in Linear project '{name}'"),
        "github_repo": ("pull requests", "pull requests in repository {name}"),
        "trello_board": ("cards", "cards on Trello board '{name}'"),
        "slack_channel": ("threads", "threads with replies in #{name}"),
        "sheet_tab": ("rows", "rows of tab '{tab}' in sheet '{sheet}'")}
OPEN_KINDS = ("slack_channel",)
OPEN_REASON = ("open rule: threads are not work items, which threads belong is decided by reading them, and replies "
               "are search-sweepable, so they carry no per-member reads")
YEARS = re.compile(r"(?<!\d)(20\d\d)(20\d\d)?(?!\d)")
RETIRED = ("do not use", "dont use", "deprecated", "obsolete", "archived", "archive")


def retired_mark(*names) -> str | None:
    """The marker when a name retires the collection itself ('OLD DO NOT USE Zombie Quests'), else None."""
    for name in names:
        hit = keyword_hit(name, RETIRED)
        if hit:
            return hit
    return None


def named_period(*names) -> tuple:
    """(label, end) for the first name that is dated by years ('20232024', 'Budget 2024'): the period named ends on
    31 Dec of its latest year. (None, None) when no name holds a year."""
    for name in names:
        years = sorted({int(y) for m in YEARS.finditer(str(name or "")) for y in m.groups() if y})
        if years:
            label = str(years[0]) if len(years) == 1 else f"{years[0]}-{years[-1]}"
            return label, dt.datetime(years[-1], 12, 31, 23, 59, tzinfo=dt.timezone.utc)
    return None, None


def matching_collections(source, persona: dict, entry: dict, section: dict) -> list:
    """Every base collection the persona can read that belongs to the competency, any size."""
    cols, clock, out = source.collections(), source.clock, []
    uid = source.slack_uid(persona)

    def add(coll, access, last):
        why = belongs(coll, entry)
        if not why or coll["size"] <= 0:
            return
        unit, rule = RULE[coll["kind"]]
        age = _age_days(last, clock)
        label, end = named_period(coll.get("tab"), coll.get("sheet")) if coll["kind"] == "sheet_tab" \
            else named_period(coll.get("name"))
        named_over = end is not None and (clock - end).days > ACTIVE_WINDOW_DAYS
        retired = retired_mark(coll.get("tab"), coll.get("sheet")) if coll["kind"] == "sheet_tab" \
            else retired_mark(coll.get("name"))
        dormant = age is None or age > ACTIVE_WINDOW_DAYS or named_over or bool(retired)
        item = {"kind": coll["kind"], "service": coll["service"], "key": coll["key"], "name": coll["name"],
                "size": coll["size"], "unit": unit, "rule": rule.format(**coll),
                "closed": coll["kind"] not in OPEN_KINDS, "access": access, "why": why,
                "last_activity": _day(last), "dormant": dormant,
                "scale": "container" if coll["size"] > CONTAINER_ABOVE else "cohort"}
        if dormant:
            item["dormant_why"] = (f"no activity since {_day(last)}" if age is not None and age > ACTIVE_WINDOW_DAYS
                                   else "no activity date" if age is None
                                   else f"named for {label}, a period that ended {(clock - end).days} days before "
                                        f"the clock (edited {_day(last)})" if named_over
                                   else f"its name retires it ('{retired}'; edited {_day(last)})")
        if "cards_with_comments" in coll:
            item["cards_with_comments"] = coll["cards_with_comments"]
        item["gaps"] = gaps_for(item, section)
        out.append(item)
    for group in ("linear_teams", "linear_projects", "github_repos", "trello_boards"):
        for coll in cols.get(group) or []:
            add(coll, "unscoped", coll.get("last_activity"))
    for coll in cols.get("slack_channels") or []:
        if uid and uid in coll["members"] and coll.get("channel_kind") in ("public", "private"):
            add(coll, "member", coll.get("last_activity"))
    for coll in cols.get("sheet_tabs") or []:
        access = source.drive_access(coll["file_id"], persona)
        if access:
            add(coll, access, source.drive_modified(coll["file_id"]))
    return out


def classify(found: list, need: int) -> dict:
    """Split matching collections into counted candidates, listed ones (open or dormant) and near misses."""
    def order(c):
        return (c["scale"] != "cohort", -c["size"], c["service"], str(c["name"]))
    big = [c for c in found if c["size"] >= need]
    counted = sorted((c for c in big if c["closed"] and not c["dormant"]), key=order)
    listed = sorted((c for c in big if not (c["closed"] and not c["dormant"])),
                    key=lambda c: (c["dormant"], not c["closed"], -c["size"], str(c["name"])))
    small = sorted((c for c in found if c["size"] < need and not c["dormant"]), key=lambda c: (-c["size"], str(c["name"])))
    for c in counted:
        c["counts"] = True
    for c in listed:
        c["counts"] = False
        c["not_counted_because"] = "dormant" if c["dormant"] else "open rule"
        c["not_counted_detail"] = c.get("dormant_why") if c["dormant"] else OPEN_REASON
    return {"counted": counted, "listed": listed, "near": small[:5]}


# ---------------------------------------------------------------- earlier tasks (persona card `used`)

LINEAR_ID = re.compile(r"\b([A-Z]{2,4})-\d+\b")
REPO_ID = re.compile(r"\b([A-Za-z][\w-]+)#\d+\b")
FILE_ID = re.compile(r"\bf_[0-9a-f]{22}\b")
CHANNEL_ID = re.compile(r"\b([CDG][A-Z0-9]{8,})/\d{9,}\.\d+")
ISSUE_ID = re.compile(r"\b(?:SC|NB)-\d+\b")
DATE_TAIL = re.compile(r"_(\d{4}-\d{2}-\d{2})$")


def legacy_assignment(text: str) -> dict:
    """Read `key: value  # comment` lines of an older assignment file. Later lines never replace earlier ones."""
    keys = {"horizon": "task_type", "task_type": "task_type", "business_function": "business_function",
            "competency": "competency", "task_skill": "task_skill", "persona_name": "persona_name",
            "persona": "persona_name", "persona_role": "persona_role", "role": "persona_role",
            "difficulty_mode": "difficulty_mode", "universe_date": "universe_date_raw", "persona_key": "persona_key"}
    out = {}
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip().strip("*").strip()
        if ":" not in line:
            continue
        label, value = line.split(":", 1)
        field = keys.get(_norm(label).replace(" ", "_"))
        value = " ".join(value.split())
        if field and value and not re.fullmatch(r"\[.*\]", value):
            out.setdefault(field, value)
    return out


def _date_key(display: str) -> str | None:
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", display or "")
    if m:
        return m.group(1)
    m = re.match(r"^([A-Za-z]+\s+\d{1,2},\s*\d{4})", display or "")
    for fmt in ("%B %d, %Y", "%b %d, %Y"):
        try:
            return dt.datetime.strptime(m.group(1), fmt).date().isoformat() if m else None
        except ValueError:
            continue
    return None


def read_assignment(task_dir) -> dict:
    """The assignment through the V3 context; an older file falls back to the plain reader (and says so)."""
    import runtime_context as rc
    task_dir = Path(task_dir)
    path = task_dir / "00_Assigments.md"
    if not path.is_file():
        raise FitError(f"no 00_Assigments.md in {task_dir}")
    note = None
    try:
        saved = {k: os.environ.get(k) for k in _ENV_KEYS}
        try:
            ctx = tc.load_context(task_dir)
        finally:
            for k, v in saved.items():
                if v is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = v
        return {"persona_name": ctx["persona_name"], "persona_key": ctx["persona_key"],
                "business_function": ctx["business_function"], "competency": ctx["competency"],
                "task_skill": ctx["task_skill"], "horizon": ctx["task_type"], "difficulty_mode": ctx["difficulty_mode"],
                "universe": ctx["universe"]["key"], "assignment_hash": ctx["assignment_hash"],
                "assignment_source": "v3-context", "assignment_note": None}
    except tc.ContextError as exc:
        note = f"the V3 context did not load ({exc}); read by the plain assignment reader"
    raw = path.read_bytes()
    fields = legacy_assignment(raw.decode("utf-8", errors="replace"))
    missing = [k for k in ("persona_name", "business_function", "competency", "task_type", "universe_date_raw")
               if k not in fields]
    if missing:
        raise FitError(f"cannot read the assignment in {task_dir}: missing {', '.join(missing)} ({note})")
    universe = rc.UNIVERSE_BY_DATE.get(_date_key(fields["universe_date_raw"]) or "")
    if not universe:
        raise FitError(f"universe date {fields['universe_date_raw']!r} names no bundled universe")
    return {"persona_name": fields["persona_name"], "persona_key": fields.get("persona_key"),
            "business_function": fields["business_function"], "competency": fields["competency"],
            "task_skill": fields.get("task_skill"), "horizon": horizon_key(fields["task_type"]),
            "difficulty_mode": (fields.get("difficulty_mode") or "").casefold() or None, "universe": universe,
            "assignment_hash": tc.digest(raw), "assignment_source": "plain-reader", "assignment_note": note}


TITLE_DATE = re.compile(r"\((?:submitted|archived)[^)]*?(\d{4}-\d{2}-\d{2})")


def archive_tasks(root=COMPLETED, skipped_root=None) -> list:
    """One entry per archived task: who, when, the cohort and storyline it used, the base issues it met.
    `root` holds completed tasks (<name>/task_inputs/); `skipped_root` holds skipped ones (<name>/ is the task)."""
    out, index = [], ""
    folders = [(f, f / "task_inputs", "completed") for f in sorted(Path(root).glob("*/"))]
    if skipped_root is not None:
        folders += [(f, f, "skipped") for f in sorted(Path(skipped_root).glob("*/"))]
        try:
            index = (Path(skipped_root) / "README.md").read_text(encoding="utf-8", errors="replace")
        except OSError:
            pass
    for folder, inputs, status in folders:
        if not (inputs / "00_Assigments.md").is_file():
            continue
        try:
            a = read_assignment(inputs)
        except (FitError, tc.ContextError):
            continue
        readme = ""
        try:
            readme = (folder / "README.md").read_text(encoding="utf-8", errors="replace")
        except OSError:
            pass
        row = next((ln.split("|")[2].strip() for ln in index.splitlines()
                    if f"`{folder.name}/`" in ln and ln.count("|") >= 3), None)
        title = next((ln.lstrip("# ").strip() for ln in readme.splitlines() if ln.startswith("# ")),
                     row or folder.name.replace("_", " "))
        if status == "completed" and "not completed" in title.casefold():
            status = "unfinished"
        try:
            prompt = " ".join((inputs / "04_Prompt.txt").read_text(encoding="utf-8", errors="replace").split())
        except OSError:
            prompt = ""
        raised = Counter()
        reports = sorted(set((folder / "eval_reports").glob("**/*.md")) | set((folder / "plateform_reports").glob("**/*.md"))
                         | set(folder.glob("*_injection*.md")))
        for report in reports:
            try:
                raised.update(set(ISSUE_ID.findall(report.read_text(encoding="utf-8", errors="replace"))))
            except OSError:
                continue
        manifest = None
        for candidate in (inputs / "Working_Files" / "01_Hardness_Manifest.json", inputs / "01_Hardness_Manifest.json"):
            manifest = manifest or _read_json(candidate)
        cohort = (manifest or {}).get("cohort") if isinstance(manifest, dict) else None
        cohort = cohort if isinstance(cohort, dict) else {}
        text = json.dumps(cohort, ensure_ascii=False)
        what = cohort.get("definition") or cohort.get("rule") or cohort.get("key") or ""
        teams = Counter(LINEAR_ID.findall(text))
        date = DATE_TAIL.search(folder.name) or TITLE_DATE.search(title)
        out.append({"task": folder.name, "status": status, "date": date.group(1) if date else None,
                    "persona_key": a.get("persona_key"), "persona_name": a["persona_name"], "universe": a["universe"],
                    "competency": a["competency"], "horizon": a["horizon"],
                    "cohort": (f"{cohort.get('size')} x " if cohort.get("size") else "") + " ".join(str(what).split())[:160],
                    "cohort_size": cohort.get("size"), "storyline": title[:160], "prompt_head": prompt[:240],
                    "collections": {"linear_teams": sorted(k for k, n in teams.items() if n >= 3),
                                    "github_repos": sorted(set(REPO_ID.findall(text))),
                                    "drive_files": sorted(set(FILE_ID.findall(text)))[:8],
                                    "slack_channels": sorted(set(CHANNEL_ID.findall(text)))[:8]},
                    "base_issues": sorted(set(ISSUE_ID.findall(readme)), key=_issue_order),
                    "base_issues_raised": {k: raised[k] for k in sorted(raised, key=_issue_order)},
                    "reports_read": len(reports)})
    return out


def _issue_order(issue: str) -> tuple:
    return issue[:2], int(issue[3:])


def task_history() -> list:
    """Completed and skipped tasks, in date order."""
    return sorted(archive_tasks(COMPLETED, ARCHIVED), key=lambda t: (t.get("date") or "", t["task"]))


def used_by(persona: dict, tasks: list, exclude: str | None = None, before: str | None = None) -> list:
    """Earlier tasks for this persona. `before` (YYYY-MM-DD) keeps only tasks dated earlier, so a backtest on an
    archived task sees what its author could have seen."""
    name = persona["name"].casefold()
    return [t for t in tasks if t["task"] != exclude
            and (before is None or (t.get("date") and t["date"] < before))
            and (t.get("persona_key") == persona["persona_key"] or str(t.get("persona_name", "")).casefold() == name)]


def archive_identity(task_dir) -> tuple:
    """(name, date) when the task folder is an archived task, else (None, None)."""
    path = Path(task_dir).resolve()
    if path.name == "task_inputs" and path.parent.parent == COMPLETED.resolve():
        folder = path.parent
    elif path.parent == ARCHIVED.resolve():
        folder = path
    else:
        return None, None
    date = DATE_TAIL.search(folder.name)
    if not date:
        try:
            first = (folder / "README.md").read_text(encoding="utf-8", errors="replace").splitlines()[:1]
        except OSError:
            first = []
        date = TITLE_DATE.search(first[0]) if first else None
    return folder.name, date.group(1) if date else None


def _mark_used(cands: list, used: list, universe: str) -> None:
    for c in cands:
        hits = []
        for t in used:
            if t["universe"] != universe:
                continue
            col = t["collections"]
            if ((c["kind"] == "linear_team" and c["key"] in col["linear_teams"])
                    or (c["kind"] == "github_repo" and c["key"] in col["github_repos"])
                    or (c["kind"] == "sheet_tab" and c["key"].split("#")[0] in col["drive_files"])
                    or (c["kind"] == "slack_channel" and c["key"] in col["slack_channels"])):
                hits.append(t["task"])
        if hits:
            c["used_by"] = hits


# ---------------------------------------------------------------- the census

def census(source, persona: dict, function, competency, horizon, mode=None, task_skill=None,
           tasks=None, exclude_task=None, section=None, competencies=None, before=None) -> dict:
    """The fit of one persona and assignment against one universe. Pure: reads through `source` only."""
    name, entry = competency_entry(competency, competencies)
    hz = horizon_key(horizon)
    need, minimum = COHORT_MIN[hz], thin_min()
    section = section or build_surface(source)
    table = reach_table(source, persona, minimum)
    thin = [s for s in SCOPED if table[s]["thin"]]
    found = matching_collections(source, persona, entry, section)
    groups = classify(found, need)
    used = used_by(persona, tasks if tasks is not None else task_history(), exclude_task, before)
    _mark_used(groups["counted"] + groups["listed"], used, source.key)
    counted, listed = groups["counted"], groups["listed"]
    open_population = not counted
    limits = [thin_limit(s, table[s]) for s in thin]
    if not counted:
        verdict = NO_COHORT
        have = "; ".join(f"{c['name']} ({c['size']} {c['unit']}, "
                         + (c.get("dormant_why") or "dormant" if c["dormant"] else "open rule") + ")"
                         for c in listed[:3])
        reason = (f"no closed, live base collection of {need} or more for {name} in this persona's view"
                  + (f" (listed but not counted: {have})" if have else ""))
        route = ("Build the scenario by injection (plan WS9 item 3): design backwards from the difficulty budget, "
                 "let one injected record define the cohort with a closed rule, give each member its own records, "
                 "and hide the units in dense base containers the persona can read.")
    else:
        verdict = LIMITS if limits else FIT
        top = counted[0]
        reason = (f"{len(counted)} closed, live base collection(s) of {need} or more for {name}; "
                  f"largest fit: {top['name']} ({top['size']} {top['unit']})")
        route = "Design on a base cohort; inject the per-member notes and the units."
    population = ("no closed base collection of cohort size for this competency in the persona's view: write the "
                  "closed membership rule and census it before the design (plan WS9 item 5)" if open_population
                  else "a closed base rule exists (the container defines membership)")
    return {
        "persona": {k: persona.get(k) for k in ("persona_key", "name", "email", "role", "department")},
        "universe": source.key, "universe_label": source.label, "clock": source.clock.isoformat(),
        "source_fingerprint": source.fingerprint,
        "assignment": {"business_function": function, "competency": name, "competency_given": competency,
                       "task_skill": task_skill, "horizon": hz, "difficulty_mode": mode},
        "thresholds": {"cohort_min": need, "thin_min_results": minimum, "thin_window_days": THIN_WINDOW_DAYS,
                       "active_window_days": ACTIVE_WINDOW_DAYS, "container_above": CONTAINER_ABOVE},
        "reach": table, "thin_services": thin,
        "candidates": counted, "listed_not_counted": listed, "near_misses": groups["near"],
        "open_population": open_population, "open_population_reason": population,
        "fit": verdict, "reason": reason, "limits": limits, "route": route, "used": used,
    }


def _result(fit: dict | None, status: str, detail: str, bound: dict, extra=None) -> dict:
    """The contract object. `verdict` carries the fit verdict (the gate reads it); `status` is PASS, WARN or FAIL."""
    verdict = fit["fit"] if fit else "FAIL"
    out = {"tool": TOOL, "version": VERSION, "verdict": verdict, "status": status, "bound_to": bound,
           "checks": [{"id": CHECK_ID, "status": status, "detail": detail}]}
    out.update(fit or {})
    out.update(extra or {})
    return out


def _detail(fit: dict) -> str:
    text = f"{fit['fit']}: {fit['reason']}."
    if fit["limits"]:
        text += " Limits: " + "; ".join(fit["limits"]) + "."
    if fit["fit"] == NO_COHORT:
        text += " The scenario is built by injection (plan WS9 item 3)."
    return text


def _bound(task_dir=None) -> dict:
    bound = {}
    if task_dir is not None:
        digest = _sha256(Path(task_dir) / "00_Assigments.md")
        if digest:
            bound["00_Assigments.md"] = digest
    for path in (COMPETENCY_MAP, POLICY):
        digest = _sha256(path)
        if digest:
            bound[str(path.relative_to(BUNDLE))] = digest
    return bound


def wrap(fit: dict, task_dir=None, assignment=None) -> dict:
    status = "PASS" if fit["fit"] == FIT else "WARN"
    extra = {}
    if assignment:
        extra = {"assignment_hash": assignment.get("assignment_hash"),
                 "assignment_source": assignment.get("assignment_source"),
                 "assignment_note": assignment.get("assignment_note")}
    return _result(fit, status, _detail(fit), _bound(task_dir), extra)


def failure(detail: str, task_dir=None) -> dict:
    return _result(None, "FAIL", detail, _bound(task_dir), {"limits": [], "fit": None})


def run_census(universe: str, persona_query: str, function, competency, horizon, mode=None, task_skill=None,
               source=None, exclude_task=None, tasks=None, before=None) -> dict:
    """Census for a persona and universe with no task folder. `source` replaces the base exports and `tasks` the
    archive of earlier tasks (tests)."""
    if source is not None:
        return census(source, source.persona(persona_query), function, competency, horizon, mode, task_skill,
                      tasks=tasks, exclude_task=exclude_task, before=before)
    with reading(universe) as context:
        base = BaseSource(universe, context)
        return census(base, base.persona(persona_query), function, competency, horizon, mode, task_skill,
                      tasks=tasks, exclude_task=exclude_task, before=before)


def evaluate(task_dir, source=None, write=False, tasks=None) -> dict:
    """Census for a task folder. Returns the contract object; writes only when `write` is set. On an archived task
    (a backtest) the earlier-task list holds only tasks dated before it."""
    task_dir = Path(task_dir)
    try:
        a = read_assignment(task_dir)
        archive_name, archive_date = archive_identity(task_dir)
        if write and archive_name:
            raise FitError(f"{archive_name} is an archived task (read-only backtest data); run the census without "
                           f"--write")
        fit = run_census(a["universe"], a.get("persona_key") or a["persona_name"], a["business_function"],
                         a["competency"], a["horizon"], a.get("difficulty_mode"), a.get("task_skill"),
                         source=source, exclude_task=archive_name, tasks=tasks,
                         before=archive_date if archive_name else None)
    except (FitError, tc.ContextError) as exc:
        return failure(f"the census could not run: {exc}", task_dir)
    result = wrap(fit, task_dir, a)
    if write:
        out = task_dir / "Working_Files"
        _write(out / FIT_JSON, _dump(result), "the assignment fit record")
        _write(out / FIT_MD, render(result) + "\n", "the assignment fit report")
    return result


# ---------------------------------------------------------------- text

def _line(c: dict) -> str:
    flags = [("closed rule" if c["closed"] else "open rule"), c["access"]]
    if c["scale"] == "container":
        flags.append("container: carve a closed subset")
    if c["dormant"]:
        flags.append("dormant: " + (c.get("dormant_why") or f"no activity since {c['last_activity'] or 'unknown'}"))
    else:
        flags.append(f"last activity {c['last_activity']}")
    if c.get("used_by"):
        flags.append("used by " + ", ".join(c["used_by"]))
    text = f"  - {c['service']}: {c['rule']} — {c['size']} {c['unit']} ({'; '.join(flags)}); {c['why']}"
    for gap in c.get("gaps") or []:
        text += f"\n      gap: {gap}"
    return text


def render(result: dict) -> str:
    """The text report: header, the check line, then the detail."""
    if result.get("fit") is None:
        check = result["checks"][0]
        return f"ASSIGNMENT FIT (unknown): FAIL\n[{check['status']}] {check['id']}: {check['detail']}"
    p, a, t = result["persona"], result["assignment"], result["thresholds"]
    check = result["checks"][0]
    out = [f"ASSIGNMENT FIT ({p['name']}, {result['universe']}): {result['fit']}",
           f"[{check['status']}] {check['id']}: {check['detail']}", "",
           f"Assignment: {a['business_function']} · {a['competency']} · {a['task_skill'] or 'task skill not given'} · "
           f"{a['horizon']} · {a['difficulty_mode'] or 'mode not given'} · {result['universe_label']}"]
    if result.get("assignment_note"):
        out.append(f"Note: {result['assignment_note']}")
    out += ["", f"Reach (rank among {result['reach']['slack']['of']} usable personas; THIN = fewer than "
                f"{t['thin_min_results']} records in the {t['thin_window_days']} days before the clock, or fewer than "
                f"{t['thin_min_results']} Drive files)"]
    r = result["reach"]
    rows = (("slack", f"{r['slack']['channels']} channels, {r['slack']['messages']} messages, {r['slack']['posts']} "
                      f"posts by the persona (last {r['slack']['last_post']}); {r['slack']['recent']} messages in the window"),
            ("gmail", f"{r['gmail']['threads']} threads, {r['gmail']['sent']} sent (last sent "
                      f"{r['gmail']['sent_last'] or 'never'}); {r['gmail']['recent']} threads in the window; senders with "
                      f"{t['thin_min_results']}+ messages: "
                      + (", ".join(f"{x.split('@')[0]} {n}" for x, n in r["gmail"]["senders_with_haystack"][:4]) or "none")),
            ("gcal", f"{r['gcal']['events']} events (last {r['gcal']['last_event']}); {r['gcal']['recent']} in the window"),
            ("drive", f"{r['drive']['files']} files ({r['drive']['owned']} owned, {r['drive']['shared']} shared); "
                      f"{r['drive']['native'].get('gdocs', 0)} docs, {r['drive']['native'].get('gsheets', 0)} sheets, "
                      f"{r['drive']['native'].get('gslides', 0)} decks"))
    for service, text in rows:
        out.append(f"  {SERVICE_LABEL[service]:9} {text}; rank {r[service]['rank']} of {r[service]['of']}"
                   + ("   THIN" if r[service]["thin"] else ""))
    out.append("  Linear, GitHub, Trello, Contacts, Confluence, Snowflake: reads are not scoped to the persona")
    out += ["", f"Cohort candidates ({t['cohort_min']} or more members, readable, {a['competency']}; closed and live "
                f"ones count)"]
    if result["candidates"]:
        out += [_line(c) for c in result["candidates"][:TOP_CANDIDATES]]
        more = len(result["candidates"]) - TOP_CANDIDATES
        if more > 0:
            out.append(f"  ... and {more} more (see the JSON)")
    else:
        out.append("  none")
    if result["listed_not_counted"]:
        out.append("Listed, not counted (open rule or dormant)")
        out += [_line(c) for c in result["listed_not_counted"][:6]]
    if result["near_misses"] and not result["candidates"]:
        out.append(f"Nearest below {t['cohort_min']}")
        out += [_line(c) for c in result["near_misses"]]
    out += ["", f"Open population: {'yes' if result['open_population'] else 'no'} — {result['open_population_reason']}"]
    if result["limits"]:
        out += ["", "Limits"] + [f"  - {x}" for x in result["limits"]]
    out += ["", f"Route: {result['route']}"]
    if result["used"]:
        out += ["", "Earlier tasks for this persona (do not reuse their cohort or storyline)"]
        out += [f"  - {u['task']} ({u['universe']}, {u['competency']}"
                + (f", {u['status']}" if u.get("status") in ("skipped", "unfinished") else "")
                + f"): {u['storyline']}; cohort {u['cohort'] or 'not recorded'}"
                + (f"; base issues met: {', '.join(u['base_issues'])}" if u["base_issues"] else "") for u in result["used"]]
    return "\n".join(out)


# ---------------------------------------------------------------- persona card (plan WS9 item 6)

CARD_TOP = 8


def _brief(c: dict) -> dict:
    keep = ("kind", "service", "key", "name", "size", "unit", "rule", "closed", "access", "last_activity", "dormant",
            "dormant_why", "scale", "gaps", "used_by", "not_counted_because", "not_counted_detail")
    return {k: c[k] for k in keep if k in c}


def build_card(source, persona: dict, tasks=None, section=None, competencies=None) -> dict:
    """Reach, thin services, candidates per competency and what earlier tasks for this persona used."""
    competencies = competencies or load_competencies()
    section = section or build_surface(source)
    minimum = thin_min()
    table = reach_table(source, persona, minimum)
    thin = [s for s in SCOPED if table[s]["thin"]]
    used = used_by(persona, tasks if tasks is not None else task_history())
    per = {}
    for name, entry in sorted(competencies["competencies"].items()):
        found = matching_collections(source, persona, entry, section)
        row = {}
        for hz, need in sorted(COHORT_MIN.items()):
            groups = classify([dict(c) for c in found], need)
            _mark_used(groups["counted"] + groups["listed"], used, source.key)
            row[hz] = {"cohort_min": need,
                       "verdict": NO_COHORT if not groups["counted"] else LIMITS if thin else FIT,
                       "counted": len(groups["counted"]),
                       "candidates": [_brief(c) for c in groups["counted"][:CARD_TOP]],
                       "listed_not_counted": [_brief(c) for c in groups["listed"][:5]],
                       "near_misses": [_brief(c) for c in groups["near"][:3]] if not groups["counted"] else []}
        per[name] = row
    return {"schema": CARD_SCHEMA, "tool": TOOL, "version": VERSION,
            "persona": {k: persona.get(k) for k in ("persona_key", "name", "email", "role", "department")},
            "universe": source.key, "universe_label": source.label, "clock": source.clock.isoformat(),
            "source_fingerprint": source.fingerprint,
            "thresholds": {"cohort_min": dict(COHORT_MIN), "thin_min_results": minimum,
                           "thin_window_days": THIN_WINDOW_DAYS, "active_window_days": ACTIVE_WINDOW_DAYS},
            "reach": table, "thin_services": thin, "limits": [thin_limit(s, table[s]) for s in thin],
            "competencies": per,
            "used": used,
            "base_issues_met": sorted({i for u in used for i in u["base_issues"]}, key=_issue_order),
            "base_issues_raised": _raised(used),
            "base_issues_note": ("base_issues_met: known data issues an earlier task's README says it met. "
                                 "base_issues_raised: known data issues named in that task's platform reports, with the "
                                 "number of reports; a report may name an issue only to say the task avoids it.")}


def _raised(used: list) -> dict:
    total = Counter()
    for u in used:
        total.update(u.get("base_issues_raised") or {})
    return {k: total[k] for k in sorted(total, key=_issue_order)}


def card_path(universe: str, persona_key: str, root=CARDS) -> Path:
    return Path(root) / universe / f"{persona_key}.json"


def card_text(card: dict) -> str:
    p, r = card["persona"], card["reach"]
    out = [f"PERSONA CARD ({p['name']}, {card['universe']}): {'WARN' if card['thin_services'] else 'PASS'}",
           f"[{'WARN' if card['thin_services'] else 'PASS'}] card.reach: "
           + ("thin: " + "; ".join(card["limits"]) if card["limits"] else "no thin service")
           + "; ranks " + ", ".join(f"{SERVICE_LABEL[s]} {r[s]['rank']}/{r[s]['of']}" for s in SCOPED)]
    for name, row in card["competencies"].items():
        long, normal = row["long-horizon"], row["normal"]
        top = long["candidates"][0] if long["candidates"] else None
        out.append(f"[{'PASS' if long['counted'] else 'WARN'}] card.cohort: {name}: long-horizon {long['verdict']} "
                   f"({long['counted']} counted), normal {normal['verdict']} ({normal['counted']} counted)"
                   + (f"; top: {top['rule']} ({top['size']} {top['unit']})" if top else ""))
    out.append(f"[PASS] card.used: {len(card['used'])} earlier task(s)"
               + ("".join(f"\n    {u['task']} ({u['universe']}, {u['competency']}"
                          + (f", {u['status']}" if u.get("status") in ("skipped", "unfinished") else "")
                          + f"): {u['storyline']}; cohort {u['cohort'] or 'not recorded'}" for u in card["used"]))
               + (f"\n    base issues met: {', '.join(card['base_issues_met'])}" if card["base_issues_met"] else "")
               + (f"\n    base issues raised in platform reports: "
                  + ", ".join(f"{k} ({n})" for k, n in (card.get("base_issues_raised") or {}).items())
                  if card.get("base_issues_raised") else ""))
    return "\n".join(out)


def write_cards(universes=UNIVERSES, persona_query=None, root=CARDS, write=True, source_factory=None) -> list:
    """Build (and write) cards. Returns (path, card) pairs."""
    tasks, competencies, out = task_history(), load_competencies(), []
    for key in universes:
        with (contextlib.nullcontext(None) if source_factory else reading(key)) as context:
            source = source_factory(key) if source_factory else BaseSource(key, context)
            section = build_surface(source)
            people = [source.persona(persona_query)] if persona_query else source.personas()
            for persona in people:
                card = build_card(source, persona, tasks, section, competencies)
                path = card_path(key, persona["persona_key"], root)
                if write:
                    _write(path, _dump(card), "the persona card")
                out.append((path, card))
    return out


# ---------------------------------------------------------------- surface map file

SURFACE_ABOUT = ("What base holds per service and record type, whether it can be injected and whether reads are scoped "
                 "to the persona. Built by tools/assignment_fit.py surface-map from the exports; counts are exact "
                 "unless a note says otherwise. The scenario stage picks carriers from it; a read that returns "
                 "nothing stays out of the call budget.")
SURFACE_LEGEND = {"real": "base holds content written by people (or plain records)",
                  "none": "the record type exists and is empty in base",
                  "automated_only": "every author is a bot or an integration",
                  "mostly_automated": f"{int(AUTOMATED_MOSTLY * 100)}% or more of authors are bots or integrations",
                  "metadata_only": "names and metadata are served, content is not",
                  "not_counted": "not counted by this tool",
                  "injectable": "the table is in the authoring lint allowlist (sql_lint.WRITABLE_TABLES)",
                  "in_eval_injection_schema": "the table is in the eval's injection schema snapshot",
                  "known_entries": "the plan's known entries, each checked against this universe"}


def surface_file(sections: dict, path=SURFACE_MAP) -> dict:
    """The whole map file: the given universe sections merged over what the file already holds."""
    current = _read_json(path)
    universes = dict((current or {}).get("universes") or {}) if (current or {}).get("schema") == SURFACE_SCHEMA else {}
    universes.update(sections)
    return {"schema": SURFACE_SCHEMA, "tool": TOOL, "version": VERSION, "about": SURFACE_ABOUT,
            "legend": SURFACE_LEGEND, "universes": {k: universes[k] for k in sorted(universes)}}


def surface_checks(key: str, section: dict) -> list:
    services = section["services"]
    types = sum(len(s["record_types"]) for s in services.values())
    empty = sorted(f"{svc}.{rt}" for svc, s in services.items() for rt, e in s["record_types"].items()
                   if e["base_content"] in ("none", "automated_only", "mostly_automated", "metadata_only"))
    checks = [{"id": "surface.built", "status": "PASS",
               "detail": f"{key}: {types} record types in {len(services)} services; without real base content: "
                         + (", ".join(empty) or "none")}]
    for entry in section["known_entries"]:
        slug = _norm(entry["claim"]).replace(" ", "_")[:40]
        checks.append({"id": f"surface.known.{slug}", "status": "PASS" if entry["status"] == "confirmed" else "WARN",
                       "detail": f"{key}: {entry['claim']}: {entry['status']} ({entry['evidence']})"})
        if entry.get("conflict"):
            service = _norm(entry["claim"]).split()[0]
            checks.append({"id": f"surface.lint_conflict.{service}", "status": "WARN",
                           "detail": f"{key}: {entry['conflict']}; keep rules and facts off {service} injections "
                                     f"until the lint and the platform agree"})
    return checks


def run_surface(universes, write=False, path=SURFACE_MAP, source_factory=None) -> dict:
    sections, checks = {}, []
    for key in universes:
        with (contextlib.nullcontext(None) if source_factory else reading(key)) as context:
            source = source_factory(key) if source_factory else BaseSource(key, context)
            sections[key] = build_surface(source)
        checks += surface_checks(key, sections[key])
    data = surface_file(sections, path)
    if write:
        _write(Path(path), _dump(data), "the base surface map")
    status = "WARN" if any(c["status"] == "WARN" for c in checks) else "PASS"
    return {"tool": TOOL, "version": VERSION, "verdict": status, "bound_to": {}, "checks": checks, "surface_map": data,
            "written": str(path) if write else None}


def _checks_text(title: str, qualifier: str, result: dict) -> str:
    lines = [f"{title} ({qualifier}): {result['verdict']}"]
    lines += [f"[{c['status']}] {c['id']}: {c['detail']}" for c in result["checks"]]
    return "\n".join(lines)


# ---------------------------------------------------------------- stub universe (self-test and unit tests)

class StubSource:
    """A universe held in a dict: the same interface as BaseSource, no base data."""

    def __init__(self, data: dict):
        self.d = data
        self.key, self.label, self.fingerprint = data["key"], data["label"], data["fingerprint"]
        self.clock = _parse(data["clock"])

    def personas(self):
        return list(self.d["personas"])

    def persona(self, query):
        q = str(query).strip().casefold()
        for p in self.d["personas"]:
            if q in (p["persona_key"].casefold(), p["email"].casefold(), p["name"].casefold()):
                return p
        raise FitError(f"unknown persona {query!r}")

    def reach(self, p):
        return self.d["reach"][p["persona_key"]]

    def slack_uid(self, p):
        return self.d["slack_uid"].get(p["persona_key"])

    def gmail_detail(self, p):
        return self.d["gmail"][p["persona_key"]]

    def recent(self, p):
        return self.d["recent"][p["persona_key"]]

    def drive_access(self, file_id, p):
        return (self.d["drive"].get(file_id) or {}).get("access", {}).get(p["persona_key"])

    def drive_modified(self, file_id):
        return (self.d["drive"].get(file_id) or {}).get("modified")

    def collections(self):
        return self.d["collections"]

    def surface_counts(self):
        return self.d["surface"]


def stub_data() -> dict:
    """Three personas at a clock of 2025-10-01. Julia has a thin mailbox and no marketing sheet; Vincent is an
    engineer; Leonard reads the finance sheets."""
    def person(key, name, role, dept):
        return {"persona_key": key, "name": name, "email": f"{key.replace('_', '.')}@harmonygames.co", "role": role,
                "department": dept, "usable_in_tasks": True}

    def reach(messages, channels, threads, events, owned, shared):
        return {"services": {
            "slack": {"messages_visible": messages, "channels_visible": channels, "persona_messages_posted": 50,
                      "persona_last_post": "2025-09-30"},
            "gmail": {"threads": threads, "messages": threads + 5, "last": "2025-09-17T10:00:00Z"},
            "gcal": {"events_visible": events, "last_event_start_before_clock": "2025-09-29T16:00:00+00:00"},
            "drive": {"owned_total": owned, "shared_with_total": shared,
                      "native_visible": {"gdocs": 3, "gsheets": 4, "gslides": 1},
                      "last_modified_visible": "2025-09-30T09:00:00Z"}}}
    people = [person("julia_lawson", "Julia Lawson", "Product Manager", "Product"),
              person("vincent_parker", "Vincent Parker", "Game Systems Engineer", "Engineering"),
              person("leonard_hayes", "Leonard Hayes", "Co-founder & Creative Director", "Executive")]
    channels = [
        {"kind": "slack_channel", "service": "slack", "key": "C0MARKETING", "name": "zombie_marketing",
         "channel_kind": "private", "archived": False, "members": ["U_JULIA", "U_LEO"], "size": 62,
         "messages": 2045, "recent": 208, "last_activity": "2025-09-04"},
        {"kind": "slack_channel", "service": "slack", "key": "C0BUGS", "name": "zombie-bugs",
         "channel_kind": "private", "archived": False, "members": ["U_JULIA", "U_VIN", "U_LEO"], "size": 283,
         "messages": 3830, "recent": 3318, "last_activity": "2025-09-30"},
        {"kind": "slack_channel", "service": "slack", "key": "D0DM", "name": "D0DM", "channel_kind": "im",
         "archived": False, "members": ["U_JULIA", "U_LEO"], "size": 90, "messages": 900, "recent": 90,
         "last_activity": "2025-09-30"}]
    tabs = [
        {"kind": "sheet_tab", "service": "gsheets", "key": "f_budget#0", "file_id": "f_budget",
         "name": "Budget 2026 / Lines", "sheet": "Budget 2026", "tab": "Lines", "size": 45},
        {"kind": "sheet_tab", "service": "gsheets", "key": "f_campaign#0", "file_id": "f_campaign",
         "name": "UA campaign calendar / Sheet1", "sheet": "UA campaign calendar", "tab": "Sheet1", "size": 12},
        {"kind": "sheet_tab", "service": "gsheets", "key": "f_old#0", "file_id": "f_old",
         "name": "Investor list 2023 / Sheet1", "sheet": "Investor list 2023", "tab": "Sheet1", "size": 75}]
    return {
        "key": "synthcut", "label": "Oct 1, 2025 (stub)", "fingerprint": "stub", "clock": "2025-10-01T07:00:00+00:00",
        "personas": people,
        "reach": {"julia_lawson": reach(238131, 147, 253, 748, 28, 158),
                  "vincent_parker": reach(262653, 140, 1258, 446, 190, 141),
                  "leonard_hayes": reach(368481, 280, 15339, 1382, 752, 365)},
        "slack_uid": {"julia_lawson": "U_JULIA", "vincent_parker": "U_VIN", "leonard_hayes": "U_LEO"},
        "gmail": {"julia_lawson": {"threads": 253, "recent_threads": 9, "sent": 11, "sent_last": "2024-04-17",
                                   "senders": [["leonard.hayes@harmonygames.co", 49], ["arthur.blake@harmonygames.co", 1]]},
                  "vincent_parker": {"threads": 1258, "recent_threads": 211, "sent": 132, "sent_last": "2025-05-29",
                                     "senders": [["robert@harmonygames.co", 150]]},
                  "leonard_hayes": {"threads": 15339, "recent_threads": 995, "sent": 1628, "sent_last": "2025-10-01",
                                    "senders": [["robert@harmonygames.co", 629]]}},
        "recent": {"julia_lawson": {"slack": 21874, "gcal": 43}, "vincent_parker": {"slack": 30000, "gcal": 22},
                   "leonard_hayes": {"slack": 40000, "gcal": 99}},
        "drive": {"f_budget": {"access": {"leonard_hayes": "owner"}, "modified": "2025-09-20T10:00:00Z"},
                  "f_campaign": {"access": {"julia_lawson": "shared", "leonard_hayes": "owner"},
                                 "modified": "2025-09-12T10:00:00Z"},
                  "f_old": {"access": {"leonard_hayes": "owner"}, "modified": "2023-05-17T10:00:00Z"}},
        "collections": {
            "linear_teams": [{"kind": "linear_team", "service": "linear", "key": "ZOM", "name": "Zombie Match 3D",
                              "match_name": "ZOM Zombie Match 3D", "size": 553, "open": 99,
                              "last_activity": "2025-09-30"}],
            "linear_projects": [{"kind": "linear_project", "service": "linear", "key": "p1", "name": "Zombie Match 3D",
                                 "size": 416, "open": 65, "last_activity": "2025-09-30"}],
            "github_repos": [{"kind": "github_repo", "service": "github", "key": "match3d", "name": "match3d",
                              "size": 477, "last_activity": "2025-09-30"},
                             {"kind": "github_repo", "service": "github", "key": "website", "name": "website",
                              "size": 0, "last_activity": None}],
            "trello_boards": [{"kind": "trello_board", "service": "trello", "key": "b1", "name": "UA/BD", "size": 40,
                               "open": 39, "cards_with_comments": 0, "last_activity": "2025-03-18"}],
            "slack_channels": channels, "sheet_tabs": tabs,
            "slack_totals": {"roots_people": 900, "roots_automated": 100, "replies_people": 85, "replies_automated": 15},
            "clock": "2025-10-01T07:00:00+00:00"},
        "surface": {
            "linear": {"teams": {"count": 1}, "projects": {"count": 1}, "issues": {"count": 553},
                       "comments": {"count": 0, "people": 0, "automated": 0, "containers": 553,
                                    "containers_with_people": 0},
                       "attachments": {"count": 20}},
            "github": {"repositories": {"count": 2}, "pull_requests": {"count": 477}, "issues": {"count": 0},
                       "commits": {"count": 900}, "releases": {"count": 0},
                       "reviews": {"count": 400, "people": 380, "automated": 20, "containers": 477,
                                   "containers_with_people": 300},
                       "review_comments": {"count": 100, "people": 40, "automated": 60, "containers": 477,
                                           "containers_with_people": 20},
                       "pull_request_comments": {"count": 100, "people": 13, "automated": 87, "containers": 477,
                                                 "containers_with_people": 11}},
            "trello": {"boards": {"count": 1}, "cards": {"count": 40}, "checklists": {"count": 2},
                       "comments": {"count": 0, "people": 0, "automated": 0, "containers": 40,
                                    "containers_with_people": 0}},
            "confluence": {"pages": {"count": 30}, "page_versions": {"count": 58},
                           "comments": {"count": 12, "people": 12, "automated": 0, "containers": 30,
                                        "containers_with_people": 6}},
            "contacts": {"contacts": {"count": 170}},
            "slack": {"channels": {"count": 3}, "messages": {"count": 1000, "people": 900, "automated": 100},
                      "thread_replies": {"count": 100, "people": 85, "automated": 15}, "files": {"count": 9}},
            "gmail": {"threads": {"count": 16850}, "messages": {"count": 17000}, "attachments": {"count": None}},
            "gcal": {"events": {"count": 2576}, "event_descriptions": {"count": 0}},
            "gdrive": {"files": {"count": 1500}}, "gdocs": {"documents": {"count": 9}},
            "gslides": {"presentations": {"count": 3}}, "gsheets": {"spreadsheets": {"count": 3}, "tabs": {"count": 3}},
            "snowflake": {"tables": {"count": 40}}}}


def stub_source() -> StubSource:
    return StubSource(stub_data())


STUB_ASSIGNMENT = """# Task Assigned Inputs — V3

spec_version: V3
business_function: {function}
persona_name: {name}
persona_role: {role}
competency: {competency}
task_skill: Retrieval
task_type: {horizon}
difficulty_mode: medium
universe_date: October 1, 2025 07:00
"""


# ---------------------------------------------------------------- self-test

def _self_test() -> int:
    import selftest_sandbox
    done = []

    def ok(cond, what):
        if not cond:
            raise AssertionError(what)
        done.append(what)
    src = stub_source()
    julia, vincent, leonard = (src.persona(k) for k in ("julia_lawson", "vincent_parker", "leonard_hayes"))

    fit = census(src, vincent, "Engineering", "Engineering Ops", "long-horizon", "easy", tasks=[])
    ok(fit["fit"] == FIT and not fit["limits"] and not fit["open_population"], "an engineer with Linear and GitHub: FIT")
    ok(fit["candidates"][0]["rule"] == "pull requests in repository match3d" and fit["candidates"][0]["closed"],
       "the top candidate is a closed, cohort-sized collection")
    ok(any("Linear comments: none in base" in g for c in fit["candidates"] for g in c["gaps"]),
       "the Linear comment gap is attached to Linear candidates")
    ok(any("87 of 100 are automated" in g for c in fit["candidates"] for g in c["gaps"]),
       "the PR comment gap carries the measured author split")

    fit = census(src, julia, "Product", "Engineering Ops", "Long Horizon", "medium", tasks=[])
    ok(fit["fit"] == LIMITS and fit["thin_services"] == ["gmail"], "a thin mailbox: FIT WITH LIMITS")
    ok("Gmail is thin: no anchor or variance unit there" in fit["limits"][0]
       and "253 threads, 11 sent, last sent 2024-04-17" in fit["limits"][0], "the Gmail limit names its numbers")
    ok(fit["reach"]["gmail"]["rank"] == 3 and fit["reach"]["gmail"]["of"] == 3, "rank in the roster per service")

    fit = census(src, julia, "Product", "Marketing & GTM", "long-horizon", "medium", tasks=[])
    ok(fit["fit"] == NO_COHORT and fit["open_population"] and not fit["candidates"], "no closed live collection: NO NATURAL COHORT")
    names = {c["name"]: c["not_counted_because"] for c in fit["listed_not_counted"]}
    ok(names == {"zombie_marketing": "open rule", "UA/BD": "dormant"}, "an open channel and a dormant board are listed, not counted")
    ok(fit["near_misses"] and fit["near_misses"][0]["size"] == 12, "the nearest collection below cohort size is shown")
    text = render(wrap(fit))
    ok(text.splitlines()[0] == "ASSIGNMENT FIT (Julia Lawson, synthcut): NO NATURAL COHORT", "header line")
    ok(text.splitlines()[1].startswith("[WARN] fit.census: NO NATURAL COHORT") and "built by injection" in text
       and "skip" not in text.casefold(), "the route is injection; the report never says skip")

    fit = census(src, julia, "Product", "Marketing and GTM", "normal", "medium", tasks=[])
    ok(fit["fit"] == LIMITS and fit["candidates"][0]["size"] == 12, "normal horizon counts a 12-row tab (minimum 10)")
    fit = census(src, leonard, "Executive", "Finance", "long-horizon", "medium", tasks=[])
    ok(fit["fit"] == FIT and [c["name"] for c in fit["candidates"]] == ["Budget 2026 / Lines"],
       "a finance tab the persona owns counts; the 2023 list is dormant")
    ok(census(src, vincent, "Engineering", "Finance", "long-horizon", tasks=[])["fit"] == NO_COHORT,
       "the same tab is not a candidate for a persona who cannot read it")
    try:
        census(src, julia, "Product", "Astrology", "normal", tasks=[])
        ok(False, "unknown competency must be refused")
    except FitError:
        ok(True, "unknown competency refused")

    section = build_surface(src)
    rt = section["services"]["linear"]["record_types"]["comments"]
    ok(rt["base_content"] == "none" and rt["injectable"] and not rt["reads_scoped"], "surface map: Linear comments none, injectable, unscoped")
    ok(section["services"]["github"]["record_types"]["pull_request_comments"]["base_content"] == "mostly_automated",
       "surface map: PR conversation comments mostly automated, not bots only")
    ok(section["services"]["snowflake"]["record_types"]["tables"]["injectable"] is False, "surface map: Snowflake not injectable")
    ok(section["services"]["slack"]["record_types"]["files"]["base_content"] == "metadata_only"
       and section["services"]["gmail"]["reads_scoped"], "surface map: Slack files metadata only; Gmail scoped")
    status = {k["claim"]: k["status"] for k in section["known_entries"]}
    ok(status["base Linear has no comments"] == "confirmed" and status["base PR conversation comments are bots only"] == "partly",
       "known entries are checked against the counts")
    said = {"by_service": {"confluence": {"reports": 2, "tasks": ["t"], "example": "can't edit Confluence"}}}
    lint_only = surface_section(src.surface_counts(), {"lint": {"confluence.confluence_pages"}, "eval_schema": set()},
                                {"files_read": 1, "by_service": {}, "platform_statements": said})
    entry = [k for k in lint_only["known_entries"] if k["claim"] == "Confluence cannot be injected"][0]
    ok(entry["status"] == "confirmed" and "conflict" in entry
       and lint_only["services"]["confluence"]["record_types"]["pages"]["injectable"] is False,
       "a table only the authoring lint allows is not injectable, and the conflict is named")
    old_tab = stub_data()
    old_tab["collections"]["sheet_tabs"][0].update(tab="20232024")
    fit = census(StubSource(old_tab), leonard, "Executive", "Finance", "long-horizon", tasks=[])
    tab = next((c for c in fit["listed_not_counted"] if c["key"] == "f_budget#0"), {})
    ok(fit["fit"] == NO_COHORT and "named for 2023-2024" in tab.get("dormant_why", ""),
       "a tab named for past years is dormant whatever its edit date")

    with selftest_sandbox.scratch_tmp("assignment_fit_") as tmp:
        root = Path(tmp)
        task = root / "task"
        task.mkdir()
        (task / "00_Assigments.md").write_text(STUB_ASSIGNMENT.format(
            function="Product", name="Julia Lawson", role="Product Manager", competency="Marketing and GTM",
            horizon="long-horizon"), encoding="utf-8")
        result = evaluate(task, source=src, tasks=[])
        ok(not (task / "Working_Files").exists(), "evaluate writes nothing unless asked")
        ok(result["verdict"] == NO_COHORT and result["status"] == "WARN" and result["checks"][0]["id"] == CHECK_ID
           and set(result) >= {"tool", "version", "verdict", "bound_to", "checks", "limits", "assignment_hash"},
           "the result object carries the contract keys and the fit verdict")
        ok("00_Assigments.md" in result["bound_to"], "the result is bound to the assignment file")
        evaluate(task, source=src, write=True, tasks=[])
        stored = _read_json(task / "Working_Files" / FIT_JSON)
        ok(stored and stored["verdict"] == NO_COHORT and (task / "Working_Files" / FIT_MD).read_text().startswith(
            "ASSIGNMENT FIT (Julia Lawson, synthcut): NO NATURAL COHORT"), "--write stores the JSON and the report")
        ok(_dump(evaluate(task, source=src, tasks=[])) == _dump(stored), "the census is deterministic")
        old = root / "old"
        old.mkdir()
        (old / "00_Assigments.md").write_text(
            "```\nhorizon:  Long Horizon   # platform task type\nbusiness_function: Engineering\n"
            "competency: Engineering Ops\ntask_skill: Retrieval\npersona_name: Vincent Parker\n"
            "persona_role: Game Systems Engineer\nuniverse_date: October 1, 2025 07:00\n```\n", encoding="utf-8")
        result = evaluate(old, source=src, tasks=[])
        ok(result["verdict"] == FIT and result["assignment_source"] == "plain-reader" and result["assignment_note"],
           "an older assignment file is read by the plain reader, and the report says so")
        ok(evaluate(root / "missing", source=src, tasks=[])["verdict"] == "FAIL", "a folder with no assignment fails the check")

        archive = root / "completed"
        done_task = archive / "julia_earlier_task_2025-11-01"
        (done_task / "task_inputs" / "Working_Files").mkdir(parents=True)
        (done_task / "task_inputs" / "00_Assigments.md").write_text(STUB_ASSIGNMENT.format(
            function="Product", name="Julia Lawson", role="Product Manager", competency="Engineering Ops",
            horizon="long-horizon"), encoding="utf-8")
        (done_task / "README.md").write_text("# Julia: an earlier register\n\nMet SC-15 and SC-13 on the way.\n")
        (done_task / "task_inputs" / "Working_Files" / "01_Hardness_Manifest.json").write_text(json.dumps(
            {"cohort": {"key": "ZOM ticket", "size": 110, "members": ["ZOM-1", "ZOM-2", "ZOM-3", "match3d#12"]}}))
        tasks = archive_tasks(archive)
        ok(len(tasks) == 1 and tasks[0]["date"] == "2025-11-01" and tasks[0]["cohort"] == "110 x ZOM ticket"
           and tasks[0]["base_issues"] == ["SC-13", "SC-15"] and tasks[0]["collections"]["linear_teams"] == ["ZOM"],
           "an archived task gives its cohort, storyline and the base issues it met")
        card = build_card(src, julia, tasks)
        ok(card["schema"] == CARD_SCHEMA and card["thin_services"] == ["gmail"]
           and card["used"][0]["storyline"] == "Julia: an earlier register" and card["base_issues_met"] == ["SC-13", "SC-15"],
           "the persona card holds reach, thin services and what earlier tasks used")
        eng = card["competencies"]["Engineering Ops"]["long-horizon"]
        ok(any(c.get("used_by") == ["julia_earlier_task_2025-11-01"] for c in eng["candidates"]),
           "a candidate an earlier task used is marked")
        ok(card["competencies"]["Marketing and GTM"]["long-horizon"]["verdict"] == NO_COHORT
           and card["competencies"]["Marketing and GTM"]["normal"]["verdict"] == LIMITS, "the card gives a verdict per competency and horizon")
        pairs = write_cards(("synthcut",), root=root / "cards", source_factory=lambda key: src)
        ok(len(pairs) == 3 and all(p.is_file() for p, _c in pairs)
           and (root / "cards" / "synthcut" / "julia_lawson.json").is_file(), "cards are written per universe and persona")
        out = run_surface(("synthcut",), write=True, path=root / "map.json", source_factory=lambda key: src)
        stored = _read_json(root / "map.json")
        ok(out["verdict"] == "WARN" and stored["schema"] == SURFACE_SCHEMA and list(stored["universes"]) == ["synthcut"],
           "the surface map file is written with its schema")
        stored["universes"]["normal"] = {"services": {}, "known_entries": []}
        (root / "map.json").write_text(_dump(stored))
        run_surface(("synthcut",), write=True, path=root / "map.json", source_factory=lambda key: src)
        ok(sorted(_read_json(root / "map.json")["universes"]) == ["normal", "synthcut"],
           "writing one universe keeps the other universe's section")
        try:
            _write(WS / "Evals" / "x.json", "{}", "a test write")
            ok(False, "a write into Evals/ must be refused")
        except tc.ContextError:
            ok(True, "a write into Evals/ is refused")
    ok(keyword_hit("january-quality", ["ua", "qa"]) is None and keyword_hit("UA/BD", ["ua"]) == "ua"
       and keyword_hit("Push Notifications Zombie Match", ["push notification*"]) == "push notification*",
       "keywords match whole words; * matches a prefix")
    print(f"self-test: ok ({len(done)} checks: verdicts, thin rule, candidates, gaps, surface map, cards, writes, older assignments)")
    return 0


# ---------------------------------------------------------------- CLI

def _parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="assignment_fit.py", description="Persona and assignment fit census (plan WS9).")
    ap.add_argument("--self-test", action="store_true", help="run on a stub universe; needs no base data")
    sub = ap.add_subparsers(dest="command")
    c = sub.add_parser("census", help="fit of one assignment")
    c.add_argument("--task-dir", type=Path)
    c.add_argument("--persona")
    c.add_argument("--universe")
    c.add_argument("--function")
    c.add_argument("--competency")
    c.add_argument("--horizon")
    c.add_argument("--mode")
    c.add_argument("--task-skill")
    c.add_argument("--write", action="store_true", help="store Working_Files/00_Assignment_Fit.json and .md")
    c.add_argument("--json", action="store_true")
    s = sub.add_parser("surface-map", help="what base holds per service and record type")
    s.add_argument("--universe", required=True, help="normal, synthcut or all")
    s.add_argument("--write", action="store_true")
    s.add_argument("--json", action="store_true")
    k = sub.add_parser("card", help="one persona card")
    k.add_argument("--persona", required=True)
    k.add_argument("--universe", required=True)
    k.add_argument("--write", action="store_true")
    k.add_argument("--json", action="store_true")
    a = sub.add_parser("cards", help="every usable persona in both universes")
    a.add_argument("--write", action="store_true")
    a.add_argument("--universe", default="all")
    a.add_argument("--json", action="store_true")
    return ap


def _universes(value) -> tuple:
    return UNIVERSES if _norm(value) == "all" else (universe_key(value),)


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        try:
            return _self_test()
        except AssertionError as exc:
            print(f"self-test: FAIL - {exc}")
            return 1
    ap = _parser()
    args = ap.parse_args(argv)
    if not args.command:
        ap.print_usage(sys.stderr)
        return 2
    try:
        if args.command == "census":
            if args.task_dir:
                if any((args.persona, args.universe, args.function, args.competency, args.horizon)):
                    ap.error("census takes --task-dir or the persona options, not both")
                result = evaluate(args.task_dir, write=args.write)
            else:
                missing = [n for n in ("persona", "universe", "function", "competency", "horizon")
                           if not getattr(args, n)]
                if missing:
                    ap.error("census needs --task-dir, or --" + ", --".join(missing))
                if args.write:
                    ap.error("--write needs --task-dir (the record is stored in the task folder)")
                result = wrap(run_census(universe_key(args.universe), args.persona, args.function, args.competency,
                                         args.horizon, args.mode, args.task_skill))
            print(_dump(result).rstrip() if args.json else render(result))
            return 1 if result["verdict"] == "FAIL" else 0
        if args.command == "surface-map":
            result = run_surface(_universes(args.universe), write=args.write)
            print(_dump(result).rstrip() if args.json else _checks_text("BASE SURFACE MAP", args.universe, result)
                  + (f"\nwritten: {result['written']}" if result["written"] else ""))
            return 0
        if args.command == "card":
            pairs = write_cards((universe_key(args.universe),), args.persona, write=args.write)
            path, card = pairs[0]
            print(_dump(card).rstrip() if args.json else card_text(card) + (f"\nwritten: {path}" if args.write else ""))
            return 0
        if args.command == "cards":
            pairs = write_cards(_universes(args.universe), write=args.write)
            checks = [{"id": f"card.{card['universe']}.{card['persona']['persona_key']}",
                       "status": "WARN" if card["thin_services"] else "PASS",
                       "detail": ("thin: " + ", ".join(card["thin_services"]) if card["thin_services"] else "no thin service")
                       + "; long-horizon no natural cohort for: "
                       + (", ".join(n for n, row in card["competencies"].items()
                                    if row["long-horizon"]["verdict"] == NO_COHORT) or "none")
                       + (f"; {len(card['used'])} earlier task(s)" if card["used"] else "")} for _p, card in pairs]
            result = {"tool": TOOL, "version": VERSION, "bound_to": {}, "checks": checks,
                      "verdict": "WARN" if any(c["status"] == "WARN" for c in checks) else "PASS",
                      "written": [str(p) for p, _c in pairs] if args.write else []}
            print(_dump(result).rstrip() if args.json else _checks_text("PERSONA CARDS", f"{len(pairs)} cards", result)
                  + (f"\nwritten under: {CARDS}" if args.write else ""))
            return 0
    except FitError as exc:
        print(f"assignment_fit: {exc}", file=sys.stderr)
        return 2
    except tc.ContextError as exc:
        print(f"assignment_fit: {exc}", file=sys.stderr)
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""budget_outcome.py - compare a run with the difficulty budget: did it open each unit's deciding record?

Why (plan WS6 items 1, 2 and 5). After the first real run (the pre-check) the first question is simple: for each
planned miss, did the run open the deciding record or not? The answer is the go / no-go for the six-run baseline, and
hand review is needed only for units whose result contradicts the budget. Two pre-checks on one design that miss the
budget send the task back to /create-scenario.

Inputs (found the way stage_gate.slot_path finds them):
  Working_Files/01_Difficulty_Budget.json   units with `decider.record_id` (and `container`), role and find_rate
  06_PreCheck_Trajectory/trajectory.json    the run (or --trajectory FILE; --trajectory DIR for a baseline)
  01_Universe_Inject.sql                    bound by sha256; also gives a text window of each injected decider
Trajectories are parsed by trajectory_ledger.load (calls, arguments, results, events). A step is the 1-based position
of a tool call in the run; `event` is trajectory_ledger's 0-based event index of that call (its result is usually the
next event, which is the number hand reviews tend to quote).

When a decider counts as opened (first step where one of these holds; write calls are never evidence):
  argument   a service read was called with the record's id as an argument value (get by id, thread by ts, comments of
             an issue, a batch of message ids). Still counts when the result spilled to a file.
  result     a read that returns records returned this one: the id is the value of an id field of the result (a
             message's own `ts`, a record's own `id`). Container-level reads treated as returning their records:
             Slack history, replies, channel reads and Slack message search; Gmail get_thread / get_message(s) in a
             full format; Linear list_comments, list_issues and get_issue; Calendar, Trello, Docs, Sheets and other
             get and list tools not named below.
  body       any result holds a 40-character window of the record's own text that no other injected record holds
             (injected deciders only; this is how a record read out of a spilled result through Bash is seen).
             Gmail bodies are base64 in the export and are decoded first.
  text       a Bash / Read result prints the id or Slack ts. With a text window available, an id printed without the
             window is `listed`, not opened.
Not opened, but reported:
  listed     the id came back from a listing that returns no body: Gmail search / list (ids and thread ids only),
             Gmail get in metadata or minimal format, Drive / Docs / Sheets / Slides search and list, Slack file,
             channel and user listings, Linear team / project / status listings.
  referenced the id is only a pointer inside another record (thread_ts, threadId, parentId, issueId, ...).
  spilled    a read of the decider's container spilled to a file ("exceeds maximum allowed tokens"): the export does
             not hold what came back. Reported per unit and as a WARN for an anchor; never counted as opened.

Record id forms: Slack `C.../ts` (the ts is matched as a number or a string, and in permalinks), Gmail
`mailbox/<message id>` and `mailbox/<thread id>` (a thread counts as opened when one of its messages is returned in
full), `repo#12`, and plain ids (ENG-123, comment_..., f_..., d_..., evt_..., card ids). A Slack row id (32 hex
characters) never appears in a tool result: it is resolved to its channel and ts through the injection SQL, and
reported as unmatchable when the SQL does not hold it.

Verdict (one run): GO when no anchor was opened; NO-GO when any anchor was opened (named, with the step).
HAND-REVIEW lists only units whose result contradicts the budget. Several runs (--trajectory DIR): per unit the share
of runs that opened the decider against the declared find-rate range: inside, below or above.

Usage:
  python3.12 -B Task_Authoring/tools/budget_outcome.py compare --task-dir T [--trajectory FILE|DIR] [--write] [--json]
      [--today YYYY-MM-DD]
  python3.12 -B Task_Authoring/tools/budget_outcome.py stop-rule --task-dir T [--json]
  python3.12 -B Task_Authoring/tools/budget_outcome.py --self-test
--write (one run only) stores Working_Files/06_Budget_Outcome.json, bound by sha256 to the trajectory, the budget and
the SQL, and appends one entry to Working_Files/precheck_log.json (never twice for one trajectory sha256).
Exit 0 = GO / PASS / WARN, 1 = NO-GO or STOP, 2 = usage error. Read-only on its inputs, stdlib only, never executes SQL.
"""
from __future__ import annotations

import argparse
import base64
import binascii
import collections
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WS = BUNDLE.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

TOOL = "budget_outcome"
VERSION = 1
TITLE = "BUDGET OUTCOME"
POLICY = BUNDLE / "references" / "first_pass_policy.json"

BUDGET = "01_Difficulty_Budget.json"
SQL = "01_Universe_Inject.sql"
OUTCOME = "06_Budget_Outcome.json"
LOG = "precheck_log.json"
OUTCOME_SCHEMA = "budget-outcome-v1"
LOG_SCHEMA = "precheck-log-v1"

WINDOW = 40                 # characters of a record's own text used as its body needle (as node_verdicts.needles)
STOP_DEFAULT = 2            # used only when the policy has no precheck.stop_after_no_go
ANCHOR_RATE_DEFAULT = 0.20  # used only when the policy has no budget.anchor_find_rate_max

HARNESS_TOOLS = {"Bash", "Read", "Write", "Edit", "MultiEdit", "Grep", "Glob", "Agent", "Task", "TodoWrite",
                 "ToolSearch", "WebFetch", "WebSearch", "NotebookEdit", "Skill", "LS", "BashOutput", "KillShell"}
# reads that list records without their body: an id in their result is `listed`, never `opened`
LISTING_RX = re.compile(
    r"^(gmail_(search|list)_|gdrive_(search|list)|gdocs_(search|list)|gsheets_(search|list)|gslides_(search|list)|"
    r"slack_list_|slack_search_(channels|users)|linear_list_(teams|projects|users|issue_statuses|issue_labels|cycles)|"
    r"trello_list_boards|gcal_list_calendars)")
GMAIL_THIN_FORMATS = {"metadata", "minimal"}
# keys whose value points at another record (the record that holds the key is not the one named)
REFERENCE_KEYS = {"threadts", "threadid", "parent", "parentid", "parents", "parentmessageid", "inreplyto",
                  "references", "issueid", "issue", "replyto", "relatedto", "recurringeventid", "threadparentid",
                  "latestreply", "quotedmessageid", "idcard", "idboard", "idlist"}
NUMBER_KEYS = {"number", "pullnumber", "issuenumber", "prnumber", "pull", "pr"}
KEY_COLS = ("id", "identifier", "event_id", "ical_uid", "document_id", "spreadsheet_id", "presentation_id",
            "object_id", "contact_id", "sha", "message_id")
TEXT_COLS = ("text", "body", "body_text", "description", "desc", "content", "snippet", "summary", "title", "name",
             "data_json", "grid_json", "notes")
RX_TS = re.compile(r"(?<![\d.])(\d{9,10})\.(\d{1,6})(?![\d])")
RX_PERMALINK_TS = re.compile(r"(?<![A-Za-z0-9])p(\d{10})(\d{6})(?!\d)")
RX_SLACK_ID = re.compile(r"^([CDG][A-Z0-9]{6,})/(\d{9,10}(?:\.\d{1,6})?)$")
RX_GITHUB_ID = re.compile(r"^([\w.-]+(?:/[\w.-]+)?)#(\d+)$")
NUMBER_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}


class UsageError(Exception):
    """A missing or unreadable input, or a bad argument (exit 2)."""


# ------------------------------------------------------------------ small helpers

def _tl():
    import trajectory_ledger
    return trajectory_ledger


def _slot_path(task_dir, name) -> Path:
    from stage_gate import slot_path
    return slot_path(task_dir, name)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _read_json(path: Path, what: str):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise UsageError(f"cannot read {what} {path}: {error}")


def _rel(task_dir: Path, path: Path) -> str:
    try:
        return Path(path).resolve().relative_to(Path(task_dir).resolve()).as_posix()
    except ValueError:
        return str(path)


def _check(checks: list, cid: str, status: str, detail: str) -> None:
    checks.append({"id": cid, "status": status, "detail": detail})


def _verdict(checks: list) -> str:
    statuses = {c["status"] for c in checks}
    return "FAIL" if "FAIL" in statuses else ("WARN" if "WARN" in statuses else "PASS")


def load_policy(path: Path | None = None) -> dict:
    return _read_json(path or POLICY, "the first-pass policy")


def atomic_write(path: Path, text: str, what: str) -> None:
    """Write through a temp file in the target folder, then os.replace. Never into a read-only root."""
    import task_context
    path = Path(path)
    task_context.refuse_read_only(path, what)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def _key(k) -> str:
    return re.sub(r"[^a-z0-9]", "", str(k).casefold())


def norm_ts(value):
    """A Slack ts as `seconds.micros` with six decimals, or None when the value is not one."""
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        if not 1e8 <= float(value) < 1e11:
            return None
        return f"{float(value):.6f}"
    if isinstance(value, str):
        m = re.fullmatch(r"\s*(\d{9,10})(?:\.(\d{1,6}))?\s*", value)
        if m:
            return f"{m.group(1)}.{(m.group(2) or '').ljust(6, '0')}"
    return None


# ------------------------------------------------------------------ record id forms

def id_forms(decider: dict) -> dict:
    """How one decider's record id is matched: exact id strings, a Slack ts, or a GitHub repo and number."""
    rid = str((decider or {}).get("record_id") or "").strip()
    out = {"record_id": rid, "kind": "id", "exact": set(), "ts": None, "channel": None, "github": None}
    if not rid:
        return out
    m = RX_SLACK_ID.match(rid)
    if m:
        out.update(kind="slack", channel=m.group(1).casefold(), ts=norm_ts(m.group(2)))
        return out
    m = RX_GITHUB_ID.match(rid)
    if m and "@" not in rid:
        repo = m.group(1).casefold()
        out.update(kind="github", github=(repo, repo.split("/")[-1], int(m.group(2))))
        out["exact"].add(rid.casefold())
        return out
    out["exact"].add(rid.casefold())
    if "/" in rid and "@" in rid.split("/", 1)[0]:
        out["kind"] = "gmail"
        tail = rid.split("/", 1)[1]
        out["thread"] = tail.isdigit()
        if len(tail) >= 8:
            out["exact"].add(tail.casefold())
            if tail.startswith("<") and tail.endswith(">") and len(tail) >= 10:
                out["exact"].add(tail[1:-1].casefold())
    return out


def _flatten_text(value) -> str:
    tl = _tl()
    if isinstance(value, str) and value[:1] in "[{":
        try:
            value = " ".join(tl.strings(json.loads(value)))
        except ValueError:
            pass
    return tl.flat(value) if isinstance(value, str) else ""


def sql_records(sql_text: str) -> list:
    """[{keys, ts, channel, text}] for every INSERT row of the injection SQL (text = its longest text column)."""
    from base_check import parse_sql
    out = []
    for x in parse_sql(sql_text):
        if x.get("op") != "insert":
            continue
        r = x["row"]
        keys = {str(r[k]).casefold() for k in KEY_COLS if isinstance(r.get(k), (str, int)) and str(r.get(k))}
        text = ""
        for k in TEXT_COLS:
            t = _flatten_text(r.get(k))
            if len(t) > len(text):
                text = t
        out.append({"table": x.get("table"), "keys": keys, "ts": norm_ts(r.get("ts")),
                    "channel": str(r.get("channel_id") or "").casefold() or None, "text": text,
                    "thread": str(r.get("thread_id") or "").casefold() or None})
    return out


def own_records(forms: dict, records: list) -> list:
    """The injected rows that are the decider: the Slack message, the record with that id, or a thread's messages."""
    out = []
    for rec in records:
        if forms["kind"] == "slack":
            if rec["ts"] and rec["ts"] == forms["ts"] and (not rec["channel"] or not forms["channel"]
                                                             or rec["channel"] == forms["channel"]):
                out.append(rec)
        elif forms["exact"] & rec["keys"]:
            out.append(rec)
        elif forms.get("thread") and rec.get("thread") and rec["thread"] in forms["exact"]:
            out.append(rec)
    return out


def resolve_with_sql(forms: dict, records: list) -> dict:
    """Add what only the SQL knows: the channel and ts of a Slack row id, and the message ids of a Gmail thread."""
    if forms["kind"] == "id":
        for rec in records:
            if forms["exact"] & rec["keys"] and rec["ts"] and str(rec.get("table") or "").endswith("slack_messages"):
                forms.update(kind="slack", ts=rec["ts"], channel=rec["channel"], resolved="Slack row id -> "
                             f"{(rec['channel'] or '?').upper()}/{rec['ts']} (from the SQL)")
                break
    if forms.get("thread"):
        members = set()
        for rec in records:
            if rec.get("thread") and rec["thread"] in forms["exact"]:
                members.update(k for k in rec["keys"] if len(k) >= 8)
        if members:
            forms["members"] = members
    return forms


def body_windows(forms: dict, records: list) -> list:
    """Up to four 40-character windows of the decider's own text that no other injected record holds."""
    mine = own_records(forms, records)
    out = []
    for rec in mine:
        text = rec["text"]
        if len(text) < 60:
            continue
        others = [r["text"] for r in records if r is not rec and r["text"]]
        got = 0
        for start in (len(text) // 2 - WINDOW // 2, len(text) // 3, 10, max(0, len(text) - 60), 2 * len(text) // 3):
            w = text[max(0, start):max(0, start) + WINDOW]
            if len(w) == WINDOW and w not in out and not any(w in o for o in others):
                out.append(w)
                got += 1
                if got == 2:
                    break
        if len(out) >= 4:
            break
    return out[:4]


RX_B64 = re.compile(r"[A-Za-z0-9_\-+/]{40,}={0,2}")


def result_text(data) -> str:
    """Every string of a result, flattened and lower-cased, with base64 bodies (Gmail `body.data`) decoded."""
    tl = _tl()
    parts = []
    for s in tl.strings(data):
        parts.append(s)
        if len(s) >= 40 and " " not in s[:200] and RX_B64.fullmatch(s.strip()):
            raw = s.strip().replace("-", "+").replace("_", "/")
            try:
                decoded = base64.b64decode(raw + "=" * (-len(raw) % 4)).decode("utf-8")
            except (binascii.Error, ValueError, UnicodeDecodeError):
                continue
            if decoded and sum(ch.isprintable() or ch.isspace() for ch in decoded) >= 0.9 * len(decoded):
                parts.append(decoded)
    return tl.flat(" ".join(parts))


# ------------------------------------------------------------------ one call, indexed once

class CallView:
    """What one tool call asked for and what came back, indexed for id matching."""

    __slots__ = ("step", "event", "result_event", "tool", "service", "write", "context", "spilled", "listing",
                 "arg_exact", "arg_ts", "arg_numbers", "own_exact", "ref_exact", "own_ts", "ref_ts", "numbers",
                 "text", "plain", "has_result")


def _walk(value, key, own_exact, ref_exact, own_ts, ref_ts, numbers):
    if isinstance(value, dict):
        for k, v in value.items():
            nk = _key(k)
            if nk in NUMBER_KEYS and isinstance(v, (int, str)) and not isinstance(v, bool) and str(v).isdigit():
                numbers.add(int(v))
            _walk(v, nk, own_exact, ref_exact, own_ts, ref_ts, numbers)
    elif isinstance(value, list):
        for v in value:
            _walk(v, key, own_exact, ref_exact, own_ts, ref_ts, numbers)
    elif isinstance(value, bool) or value is None:
        return
    elif isinstance(value, (str, int, float)):
        ref = key in REFERENCE_KEYS
        ts = norm_ts(value)
        if ts:
            (ref_ts if ref else own_ts).add(ts)
        if isinstance(value, str):
            s = value.strip()
            if s and len(s) <= 400:
                (ref_exact if ref else own_exact).add(s.casefold())


def index_run(run) -> list:
    """[CallView] for a trajectory_ledger.Run, in call order."""
    tl = _tl()
    views = []
    ordered = sorted(run.calls, key=lambda c: (c["event"] if c.get("event") is not None else 1 << 60))
    for n, c in enumerate(ordered, 1):
        v = CallView()
        name = str(c.get("name") or "")
        v.step, v.event, v.tool = n, c.get("event"), tl.short(name)
        v.service = not (name in HARNESS_TOOLS or name[:1].isupper())
        v.write = v.service and tl.is_write(name)
        v.context = c.get("context") or "main"
        r = run.results.get(c.get("id"))
        data = r["data"] if r else None
        v.has_result = r is not None
        v.result_event = r.get("event") if r else None
        v.spilled = isinstance(data, str) and bool(tl.RX_SPILL.search(data))
        args = c.get("input") or {}
        fmt = str(args.get("format") or "").casefold() if isinstance(args, dict) else ""
        v.listing = bool(LISTING_RX.match(v.tool)) or (v.tool.startswith("gmail_get") and fmt in GMAIL_THIN_FORMATS)
        v.arg_exact, v.arg_ts, v.arg_numbers = set(), set(), set()
        if v.service:
            _walk(args, "", v.arg_exact, v.arg_exact, v.arg_ts, v.arg_ts, v.arg_numbers)
        v.own_exact, v.ref_exact, v.own_ts, v.ref_ts, v.numbers = set(), set(), set(), set(), set()
        v.plain = (not v.service) or isinstance(data, str)
        if data is not None and not v.spilled:
            _walk(data, "", v.own_exact, v.ref_exact, v.own_ts, v.ref_ts, v.numbers)
            v.text = result_text(data)
        else:
            v.text = ""
        views.append(v)
    return views


def channel_names(run, container: str) -> set:
    """Other names a container goes by in this run (`#winddown` for its channel id), read from the results."""
    out = set()
    want = str(container or "").casefold()
    if not want:
        return out

    def walk(value):
        if isinstance(value, dict):
            cid, name = value.get("id"), value.get("name")
            if isinstance(cid, str) and isinstance(name, str) and cid.casefold() == want and name:
                out.update({name.casefold(), "#" + name.casefold()})
            for x in value.values():
                walk(x)
        elif isinstance(value, list):
            for x in value:
                walk(x)
    for c in run.calls:
        r = run.results.get(c.get("id"))
        if not r:
            continue
        data = r.get("data")
        walk(data)
        args = c.get("input") if isinstance(c.get("input"), dict) else {}
        if isinstance(data, dict) and isinstance(data.get("channel"), str) and data["channel"].casefold() == want:
            for a in args.values():
                if isinstance(a, str) and a.startswith("#"):
                    out.update({a.casefold(), a[1:].casefold()})
    return out


# ------------------------------------------------------------------ matching one unit in one run

def _text_has_id(text: str, forms: dict) -> bool:
    if forms["kind"] == "slack":
        for m in RX_TS.finditer(text):
            if norm_ts(m.group(0)) == forms["ts"]:
                return True
        for m in RX_PERMALINK_TS.finditer(text):
            if f"{m.group(1)}.{m.group(2)}" == forms["ts"]:
                return True
        return False
    if forms["kind"] == "github":
        repo, short, number = forms["github"]
        return bool(re.search(r"(?<![a-z0-9])" + re.escape(short) + r"(#|/pull/|/issues/)" + str(number) + r"(?!\d)",
                              text))
    for f in forms["exact"]:
        if re.search(r"(?<![a-z0-9])" + re.escape(f) + r"(?![a-z0-9])", text):
            return True
    return False


def match_unit(views: list, forms: dict, windows: list, container_forms: set) -> dict:
    """Walk one run's calls in order and say whether, where and how the decider was opened."""
    out = {"opened": False, "first_step": None, "first_event": None, "how": None, "tool": None, "context": None,
           "listed_step": None, "referenced_step": None, "body_step": None, "spilled_container_reads": []}
    if not forms["record_id"]:
        out["note"] = "the unit has no decider.record_id"
        return out

    def opened(v, how):
        if not out["opened"]:
            out.update(opened=True, first_step=v.step, first_event=v.event, how=how, tool=v.tool, context=v.context)

    for v in views:
        if v.write:
            continue
        body = bool(windows) and bool(v.text) and any(w in v.text for w in windows)
        if body and out["body_step"] is None:
            out["body_step"] = v.step
        hit = None
        if v.service:
            if forms["kind"] == "slack":
                arg = forms["ts"] in v.arg_ts
                own, ref = forms["ts"] in v.own_ts, forms["ts"] in v.ref_ts
            elif forms["kind"] == "github":
                repo, short, number = forms["github"]
                named = bool({repo, short} & v.arg_exact)
                arg = named and number in v.arg_numbers
                own = number in v.numbers and (named or short in v.text)
                ref = False
            else:
                ids = forms["exact"] | forms.get("members", set())
                arg = bool(ids & v.arg_exact)
                own, ref = bool(ids & v.own_exact), bool(forms["exact"] & v.ref_exact)
                if forms.get("thread") and ref:      # a message of the decider thread came back
                    own, ref = True, False
            if arg:
                hit = "argument"
            elif own and not v.plain:
                hit = "listed" if v.listing else "result"
            elif ref and out["referenced_step"] is None:
                out["referenced_step"] = v.step
            if v.spilled and container_forms and (container_forms & v.arg_exact) and not arg:
                out["spilled_container_reads"].append(v.step)
        if hit is None and v.plain and v.text and _text_has_id(v.text, forms):
            hit = "text" if (body or not windows) else "listed"
        if hit is None and body:
            hit = "body"
        if hit == "listed":
            if out["listed_step"] is None:
                out["listed_step"] = v.step
        elif hit:
            opened(v, hit)
        if out["opened"] and out["body_step"] is not None:
            break
    if out["opened"]:
        out["spilled_container_reads"] = [s for s in out["spilled_container_reads"] if s < out["first_step"]]
    return out


def expectation(unit: dict, policy: dict) -> str:
    """What one run should show for a unit: `not opened`, `opened`, `either`, or `not judged` (realism)."""
    role = unit.get("role")
    if role == "realism":
        return "not judged"
    if role == "anchor":
        return "not opened"
    if role == "variance":
        return "either"
    amax = (policy.get("budget") or {}).get("anchor_find_rate_max", ANCHOR_RATE_DEFAULT)
    fr = unit.get("find_rate")
    if isinstance(fr, list) and len(fr) == 2 and all(isinstance(x, (int, float)) for x in fr):
        if fr[1] <= amax:
            return "not opened"
        if fr[0] >= 1 - amax:
            return "opened"
    return "either"


def compare_run(run, budget: dict, policy: dict, records: list) -> list:
    """Per unit: opened yes/no, first step, how, and whether that is consistent with the budget."""
    views = index_run(run)
    out, names = [], {}
    for u in budget.get("units") or []:
        if not isinstance(u, dict) or not u.get("id"):
            continue
        decider = u.get("decider") if isinstance(u.get("decider"), dict) else {}
        forms = resolve_with_sql(id_forms(decider), records) if records else id_forms(decider)
        windows = body_windows(forms, records) if records else []
        container = str(decider.get("container") or forms.get("channel") or "").casefold()
        if container and container not in names:
            names[container] = channel_names(run, container)
        cforms = ({container} | names[container]) if container else set()
        m = match_unit(views, forms, windows, cforms)
        want = expectation(u, policy)
        if want == "not judged":
            consistent = None
        elif want == "not opened":
            consistent = not m["opened"]
        elif want == "opened":
            consistent = m["opened"]
        else:
            consistent = True
        row = {"unit": u["id"], "role": u.get("role"), "record_id": forms["record_id"],
               "service": decider.get("service"), "find_rate": u.get("find_rate"), "expected": want,
               "consistent": consistent, "body_window": bool(windows), "id_form": forms["kind"]}
        if forms.get("resolved"):
            row["resolved"] = forms["resolved"]
        if forms["kind"] == "id" and re.fullmatch(r"[0-9a-f]{32}", forms["record_id"]) \
                and str(decider.get("service") or "").casefold() == "slack":
            row["unmatchable"] = ("a Slack row id is never in a tool result and the SQL does not hold it: give the "
                                  "decider as C.../ts")
        row.update(m)
        out.append(row)
    return out


# ------------------------------------------------------------------ inputs

def find_trajectories(task_dir: Path, trajectory=None) -> list:
    """[(label, path)]: the task's pre-check by default, a named file, or every export in a named folder."""
    tl = _tl()
    if trajectory is None:
        try:
            runs = tl.task_runs(Path(task_dir))
        except ValueError as error:
            raise UsageError(str(error))
        pre = [(label, p) for label, p in runs if label == "precheck"]
        if not pre:
            raise UsageError(f"no pre-check trajectory in {task_dir}/06_PreCheck_Trajectory: pass --trajectory")
        return pre
    p = Path(trajectory)
    if p.is_file():
        return [(p.stem, p)]
    if p.is_dir():
        found = sorted(x for x in p.glob("*.json") if x.is_file())
        if not found:
            raise UsageError(f"no *.json trajectory in {p}")
        out = []
        for x in found:
            n = tl.ds._run_number(x)
            out.append((f"run-{n}" if n is not None else x.stem, x))
        labels = collections.Counter(label for label, _ in out)
        return [((label if labels[label] == 1 else x.stem), x) for label, x in out]
    raise UsageError(f"--trajectory {p} is neither a file nor a folder")


def _load_run(label: str, path: Path):
    tl = _tl()
    try:
        return tl.load(path, label)
    except (OSError, ValueError) as error:
        raise UsageError(f"cannot read the trajectory {path}: {error}")


def load_budget(task_dir: Path) -> tuple:
    p = _slot_path(task_dir, BUDGET)
    if not p.is_file():
        raise UsageError(f"no {BUDGET} in {task_dir}: the budget is written at /create-scenario")
    budget = _read_json(p, "the budget")
    if not isinstance(budget, dict) or not isinstance(budget.get("units"), list):
        raise UsageError(f"{p}: the budget has no `units` list")
    return budget, p


# ------------------------------------------------------------------ compare

def _range_position(share: float, find_rate) -> str:
    if not (isinstance(find_rate, list) and len(find_rate) == 2
            and all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in find_rate)):
        return "no range"
    lo, hi = find_rate
    if share < lo - 1e-9:
        return "below"
    if share > hi + 1e-9:
        return "above"
    return "inside"


def evaluate(task_dir, trajectory=None, policy: dict | None = None) -> dict:
    """Compare the budget with one run (the pre-check) or several (a baseline folder). Never writes."""
    td = Path(task_dir)
    if not td.is_dir():
        raise UsageError(f"task folder {td} does not exist")
    policy = policy or load_policy()
    budget, budget_path = load_budget(td)
    trajectories = find_trajectories(td, trajectory)
    sql_path = _slot_path(td, SQL)
    bound = {_rel(td, budget_path): sha256_file(budget_path)}
    records, sql_sha, sql_note = [], None, None
    if sql_path.is_file():
        sql_sha = sha256_file(sql_path)
        bound[_rel(td, sql_path)] = sql_sha
        try:
            records = sql_records(sql_path.read_text(encoding="utf-8"))
        except Exception as error:  # the SQL is evidence only; an unparsed file removes the body check, nothing else
            sql_note = f"the SQL could not be parsed for text windows ({error.__class__.__name__}: {error})"
    else:
        sql_note = f"no {SQL} in the task folder: deciders are matched by id only and the SQL is not bound"
    checks, runs = [], []
    for label, path in trajectories:
        run = _load_run(label, path)
        sha = sha256_file(path)
        bound[_rel(td, path)] = sha
        tl = _tl()
        spilled = sum(1 for c in run.calls if isinstance((run.results.get(c.get("id")) or {}).get("data"), str)
                      and tl.RX_SPILL.search(run.results[c["id"]]["data"]))
        runs.append({"label": label, "file": _rel(td, path), "sha256": sha, "format": run.format,
                     "tool_calls": len(run.calls), "spilled_results": spilled,
                     "units": compare_run(run, budget, policy, records)})
    single = len(runs) == 1
    empty = [r["label"] for r in runs if not r["tool_calls"]]
    _check(checks, "precheck.trajectory", "WARN" if (empty or sql_note) else "PASS",
           "; ".join(f"{r['label']}: {r['tool_calls']} tool calls, {r['spilled_results']} results spilled to a file"
                     for r in runs[:8]) + (f"; and {len(runs) - 8} more" if len(runs) > 8 else "")
           + (f". No tool call in {', '.join(empty)}: not a usable run" if empty else "")
           + (f". Note: {sql_note}" if sql_note else ""))
    out = {"tool": TOOL, "version": VERSION, "command": "compare", "mode": "precheck" if single else "baseline",
           "design_id": budget.get("design_id"), "budget_revision": budget.get("revision"),
           "budget_mode": budget.get("mode"), "sql_sha256": sql_sha, "bound_to": dict(sorted(bound.items())),
           "runs": runs}
    no_decider = [u["unit"] for u in runs[0]["units"] if not u["record_id"] and u["role"] != "realism"]
    if no_decider:
        _check(checks, "precheck.deciders", "FAIL", "units without decider.record_id cannot be compared: "
               + ", ".join(no_decider) + ". Add the record id to the budget")
    unmatchable = [u["unit"] for u in runs[0]["units"] if u.get("unmatchable")]
    if unmatchable:
        _check(checks, "precheck.id_forms", "WARN", "these deciders cannot be matched in a trajectory, so `not "
               "opened` means nothing for them: " + ", ".join(unmatchable) + " (a Slack row id that the SQL does "
               "not hold; give the decider as C.../ts)")
    if single:
        units = runs[0]["units"]
        anchors = [u for u in units if u["role"] == "anchor"]
        opened_anchors = [u for u in anchors if u["opened"]]
        variance = [u for u in units if u["role"] == "variance"]
        contradicts = [u for u in units if u["consistent"] is False]
        out["outcome"] = "NO-GO" if opened_anchors else "GO"
        out["units"] = units
        out["trajectory_sha256"] = runs[0]["sha256"]
        out["opened_anchors"] = [u["unit"] for u in opened_anchors]
        out["hand_review"] = [{"unit": u["unit"], "role": u["role"], "expected": u["expected"],
                               "opened": u["opened"], "first_step": u["first_step"], "how": u["how"],
                               "tool": u["tool"]} for u in contradicts]
        tail = f"{sum(1 for u in variance if u['opened'])} of {len(variance)} variance units opened"
        if opened_anchors:
            _check(checks, "precheck.budget_outcome", "FAIL", "NO-GO: " + "; ".join(
                f"anchor {u['unit']} ({u['record_id']}) was opened at step {u['first_step']} "
                f"(event {u['first_event']}) by {u['tool']} ({_how(u)})" for u in opened_anchors) + f"; {tail}. Do not spend the baseline: the budget "
                "does not hold on this revision")
        elif not anchors:
            _check(checks, "precheck.budget_outcome", "WARN", f"GO by default: the budget has no anchor unit; {tail}")
        else:
            _check(checks, "precheck.budget_outcome", "PASS", f"GO: none of the {len(anchors)} anchors was opened; "
                   f"{tail}")
        if contradicts:
            _check(checks, "precheck.hand_review", "WARN", "hand dispositions are needed for " + ", ".join(
                f"{u['unit']} (expected {u['expected']}, " + ("opened at step " + str(u["first_step"]) if u["opened"]
                                                              else "not opened") + ")" for u in contradicts)
                + " and for no other unit")
        else:
            _check(checks, "precheck.hand_review", "PASS", "no unit contradicts the budget: no hand disposition "
                   "is needed")
        unsure = [u for u in anchors if not u["opened"] and u["spilled_container_reads"]]
        weak = [u for u in units if u["opened"] and u["how"] == "text" and not u["body_window"]]
        if unsure:
            _check(checks, "precheck.spilled", "WARN", "a read of the container spilled to a file, so the export "
                   "does not show whether the record came back: " + ", ".join(
                       f"{u['unit']} (steps {', '.join(str(s) for s in u['spilled_container_reads'][:4])})"
                       for u in unsure) + ". Check what the run read from that file before trusting GO")
        if weak:
            _check(checks, "precheck.weak_evidence", "WARN", "opened is read from an id printed by Bash or Read with "
                   "no text window to confirm the body: " + ", ".join(u["unit"] for u in weak))
        out["unverified"] = [u["unit"] for u in unsure]
    else:
        table, outside = [], []
        ids = [u["unit"] for u in runs[0]["units"]]
        for i, uid in enumerate(ids):
            per = [r["units"][i] for r in runs]
            k, n = sum(1 for u in per if u["opened"]), len(per)
            share = round(k / n, 4) if n else 0.0
            pos = _range_position(share, per[0]["find_rate"]) if per[0]["role"] != "realism" else "not judged"
            row = {"unit": uid, "role": per[0]["role"], "record_id": per[0]["record_id"],
                   "find_rate": per[0]["find_rate"], "opened_runs": k, "runs": n, "share": share, "position": pos,
                   "opened_in": [r["label"] for r, u in zip(runs, per) if u["opened"]],
                   "first_steps": {r["label"]: u["first_step"] for r, u in zip(runs, per) if u["opened"]}}
            table.append(row)
            if pos in ("below", "above"):
                outside.append(row)
        out["units"] = table
        out["outcome"] = "INSIDE" if not outside else "OUTSIDE"
        n = len(runs)
        if outside:
            _check(checks, "precheck.find_rates", "WARN", f"{len(outside)} of {len(table)} units are outside their "
                   f"declared range over {n} runs: " + ", ".join(
                       f"{r['unit']} {r['opened_runs']}/{r['runs']} = {r['share']:.2f} is {r['position']} "
                       f"{r['find_rate']}" for r in outside) + f". One run is {100 / n:.1f} points")
        else:
            _check(checks, "precheck.find_rates", "PASS", f"every unit with a range is inside it over {n} runs")
    out["verdict"] = _verdict(checks)
    out["checks"] = checks
    return out


def _how(u: dict) -> str:
    return {"argument": "its id was a call argument", "result": "its id came back in the result",
            "body": "its text came back in a result", "text": "its id was printed by a shell or file read"}.get(
                u.get("how"), str(u.get("how")))


def write_outcome(task_dir, result: dict, today: str | None = None) -> dict:
    """Store 06_Budget_Outcome.json and append the pre-check log entry (once per trajectory sha256)."""
    td = Path(task_dir)
    if result.get("mode") != "precheck":
        raise UsageError("--write stores one pre-check; a folder of runs is reported only")
    if any(c["id"] == "precheck.deciders" and c["status"] == "FAIL" for c in result.get("checks") or []):
        raise UsageError("a unit has no decider.record_id, so this run cannot be judged: fix the budget before a "
                         "pre-check is logged")
    doc = dict(result)
    doc["schema"] = OUTCOME_SCHEMA
    if today:
        doc["date"] = today
    out_path = _slot_path(td, OUTCOME)
    atomic_write(out_path, json.dumps(doc, indent=1, sort_keys=True, ensure_ascii=False) + "\n", "the budget outcome")
    log_path = _slot_path(td, LOG)
    log = {"schema": LOG_SCHEMA, "entries": []}
    if log_path.is_file():
        log = _read_json(log_path, "the pre-check log")
        if not isinstance(log, dict) or not isinstance(log.get("entries"), list):
            raise UsageError(f"{log_path}: not a {LOG_SCHEMA} file (an object with an `entries` list)")
    sha = result["trajectory_sha256"]
    known = [e for e in log["entries"] if isinstance(e, dict) and e.get("trajectory_sha256") == sha]
    info = {"outcome_file": _rel(td, out_path), "log_file": _rel(td, log_path)}
    if known:
        info.update(appended=False, logged_verdict=known[0].get("verdict"))
        return info
    entry = {"design_id": result.get("design_id"), "budget_revision": result.get("budget_revision"),
             "sql_sha256": result.get("sql_sha256"), "trajectory_sha256": sha, "verdict": result["outcome"],
             "opened_anchors": result.get("opened_anchors") or []}
    if today:
        entry["date"] = today
    log["entries"].append(entry)
    log.setdefault("schema", LOG_SCHEMA)
    atomic_write(log_path, json.dumps(log, indent=1, sort_keys=True, ensure_ascii=False) + "\n", "the pre-check log")
    info.update(appended=True, logged_verdict=entry["verdict"])
    return info


def stop_rule(task_dir, policy: dict | None = None) -> dict:
    """Count NO-GO pre-checks on the current design; FAIL (STOP) at the policy's limit."""
    td = Path(task_dir)
    if not td.is_dir():
        raise UsageError(f"task folder {td} does not exist")
    policy = policy or load_policy()
    limit = (policy.get("precheck") or {}).get("stop_after_no_go", STOP_DEFAULT)
    budget, budget_path = load_budget(td)
    design = budget.get("design_id")
    log_path = _slot_path(td, LOG)
    bound = {_rel(td, budget_path): sha256_file(budget_path)}
    entries = []
    if log_path.is_file():
        log = _read_json(log_path, "the pre-check log")
        if not isinstance(log, dict) or not isinstance(log.get("entries"), list):
            raise UsageError(f"{log_path}: not a {LOG_SCHEMA} file (an object with an `entries` list)")
        entries = [e for e in log["entries"] if isinstance(e, dict)]
        bound[_rel(td, log_path)] = sha256_file(log_path)
    mine = [e for e in entries if e.get("design_id") == design]
    no_go = [e for e in mine if e.get("verdict") == "NO-GO"]
    checks, stop = [], None
    if not design:
        _check(checks, "precheck.stop_rule", "FAIL", "the budget has no design_id, so pre-checks cannot be counted "
               "per design: add it")
    elif len(no_go) >= limit:
        word = NUMBER_WORDS.get(len(no_go), str(len(no_go)))
        stop = (f"STOP: {word} pre-checks on design {design} missed the budget — return to /create-scenario for a "
                "redesign, not another patch")
        _check(checks, "precheck.stop_rule", "FAIL", f"{len(no_go)} NO-GO pre-checks on design {design} "
               f"(limit {limit}; {len(mine)} logged on this design)")
    else:
        _check(checks, "precheck.stop_rule", "PASS", f"{len(no_go)} NO-GO pre-check(s) on design {design} of "
               f"{len(mine)} logged (stop at {limit})")
    return {"tool": TOOL, "version": VERSION, "command": "stop-rule", "verdict": _verdict(checks),
            "bound_to": dict(sorted(bound.items())), "checks": checks, "design_id": design,
            "no_go": len(no_go), "logged_on_design": len(mine), "limit": limit, "stop": stop}


# ------------------------------------------------------------------ text output

def to_text(r: dict) -> str:
    if r["command"] == "stop-rule":
        lines = [f"{TITLE} (stop-rule): {r['verdict']}"]
        lines += [f"[{c['status']}] {c['id']}: {c['detail']}" for c in r["checks"]]
        if r.get("stop"):
            lines.append(r["stop"])
        return "\n".join(lines)
    if r["mode"] == "precheck":
        lines = [f"{TITLE}: {r['outcome']}"]
    else:
        lines = [f"{TITLE} (baseline, {len(r['runs'])} runs): {r['verdict']}"]
    lines += [f"[{c['status']}] {c['id']}: {c['detail']}" for c in r["checks"]]
    if r["mode"] == "precheck":
        lines.append(f"  {'unit':8} {'role':9} {'opened':7} {'step':>5} {'event':>6} {'how':9} {'consistent':10} record")
        for u in r["units"]:
            cons = "n/a" if u["consistent"] is None else ("yes" if u["consistent"] else "NO")
            extra = []
            if not u["opened"] and u["listed_step"]:
                extra.append(f"listed at step {u['listed_step']}")
            if not u["opened"] and u["referenced_step"]:
                extra.append(f"referenced at step {u['referenced_step']}")
            if not u["opened"] and u["spilled_container_reads"]:
                extra.append("container read spilled at step " + str(u["spilled_container_reads"][0]))
            lines.append(f"  {u['unit'][:8]:8} {str(u['role'])[:9]:9} {'yes' if u['opened'] else 'no':7} "
                         f"{str(u['first_step'] or '-'):>5} "
                         f"{str(u['first_event'] if u['first_event'] is not None else '-'):>6} "
                         f"{str(u['how'] or '-')[:9]:9} {cons:10} {u['record_id']}"
                         + (f"  ({'; '.join(extra)})" if extra else ""))
        if r["hand_review"]:
            lines.append("HAND-REVIEW: " + ", ".join(h["unit"] for h in r["hand_review"]))
        else:
            lines.append("HAND-REVIEW: none")
        w = r.get("written")
        if w:
            lines.append(f"wrote {w['outcome_file']}; " + (f"logged {w['logged_verdict']} in {w['log_file']}"
                                                          if w["appended"] else
                                                          f"this trajectory is already in {w['log_file']} "
                                                          f"({w['logged_verdict']}); nothing appended"))
    else:
        lines.append(f"  {'unit':8} {'role':9} {'opened':>7} {'share':>6} {'range':>14} position")
        for u in r["units"]:
            lines.append(f"  {u['unit'][:8]:8} {str(u['role'])[:9]:9} {str(u['opened_runs']) + '/' + str(u['runs']):>7} "
                         f"{u['share']:>6.2f} {str(u['find_rate']):>14} {u['position']}")
    return "\n".join(lines)


# ------------------------------------------------------------------ self-test

def _events(calls: list) -> list:
    """A stream-json export from [(tool name, input, result, parent or None)]."""
    events = [{"type": "system", "subtype": "init", "model": "claude-opus-5-5"}]
    for i, c in enumerate(calls):
        name, args, result = c[0], c[1], c[2]
        parent = c[3] if len(c) > 3 else None
        cid = f"toolu_{i:03d}"
        events.append({"type": "assistant", "parent_tool_use_id": parent,
                       "message": {"model": "claude-opus-5-5", "content": [
                           {"type": "tool_use", "id": cid, "name": name, "input": args}]}})
        content = result if isinstance(result, str) else json.dumps(result)
        events.append({"type": "user", "parent_tool_use_id": parent,
                       "message": {"content": [{"type": "tool_result", "tool_use_id": cid, "content": content}]}})
    events.append({"type": "result", "subtype": "success", "is_error": False})
    return events


_SPILL = ("Error: result (79,141 characters) exceeds maximum allowed tokens. Output has been saved to "
          "/home/agent/tool-results/mcp-hg-slack_read_channel-1.txt.")
_ANCHOR_TEXT = ("small correction for the books, the second MotMot wire in April never landed, the bank sent it back "
                "to us two days later so only count the first one")
_SQL = (
    "INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text)\nVALUES "
    "('msg_anchor_0001', '1700000000.000100', 'C0123ABCD', 'message', 'U1', '" + _ANCHOR_TEXT + "');\n"
    "INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text)\nVALUES "
    "('msg_root_0002', '1700000000.000001', 'C0123ABCD', 'message', 'U2', 'standup notes for the week, nothing to "
    "see here, lunch is at noon and the build is green again today');\n")


def _budget() -> dict:
    return {"schema": "difficulty-budget-v1", "design_id": "D1", "revision": "rev1", "mode": "easy",
            "weight_basis": "surface", "total_weight": 40, "units": [
                {"id": "U1", "role": "anchor", "find_rate": [0.0, 0.15], "mechanism": "RET",
                 "decider": {"service": "slack", "record_id": "C0123ABCD/1700000000.000100", "container": "C0123ABCD",
                             "injected": True}},
                {"id": "U2", "role": "anchor", "find_rate": [0.0, 0.15], "mechanism": "OFF",
                 "decider": {"service": "gmail", "record_id": "robert@hg.co/<CAPBs_a5shT3@mail.gmail.com>",
                             "container": "robert@hg.co", "injected": False}},
                {"id": "U3", "role": "variance", "find_rate": [0.35, 0.65], "mechanism": "COIN1",
                 "decider": {"service": "linear", "record_id": "ENG-77", "injected": False}},
                {"id": "U4", "role": "variance", "find_rate": [0.35, 0.65], "mechanism": "COIN2",
                 "decider": {"service": "gdrive", "record_id": "f_abcdef123456", "injected": False}},
                {"id": "U5", "role": "variance", "find_rate": [0.35, 0.65], "mechanism": "COIN3",
                 "decider": {"service": "github", "record_id": "zm-client#12", "injected": False}},
                {"id": "U6", "role": "realism", "mechanism": "TRAP",
                 "decider": {"service": "gcal", "record_id": "evt_0123456789ab", "injected": False}}]}


def _go_calls() -> list:
    """A run that never opens either anchor: pointers, listings and a write only."""
    return [
        ("mcp__hg__slack_search_public_and_private", {"query": "motmot"},
         {"ok": True, "messages": [{"ts": 1700000050.5, "text": "see the thread", "thread_ts": "1700000000.000100",
                                    "channel": "C0123ABCD"}]}),
        ("mcp__hg__gmail_search_messages", {"query": "western union"},
         {"messages": [{"id": "robert@hg.co/<CAPBs_a5shT3@mail.gmail.com>", "threadId": "robert@hg.co/185"}]}),
        ("mcp__hg__gmail_get_thread", {"thread_id": "robert@hg.co/185", "format": "metadata"},
         {"id": "robert@hg.co/185", "messages": [{"id": "robert@hg.co/<CAPBs_a5shT3@mail.gmail.com>",
                                                  "snippet": "Receipt"}]}),
        ("mcp__hg__linear_get_issue", {"id": "ENG-77"}, {"id": "ENG-77", "identifier": "ENG-77", "title": "x"}),
        ("mcp__hg__gdrive_search", {"query": "plan"}, {"files": [{"id": "f_abcdef123456", "name": "Plan"}]}),
        ("mcp__hg__linear_update_issue", {"id": "ENG-88", "description": "see C0123ABCD/1700000000.000100"},
         {"id": "ENG-88", "ts": "1700000000.000100"}),
        ("mcp__hg__github_get_pull_request", {"repo": "zm-client", "pull_number": 12},
         {"number": 12, "title": "fix", "html_url": "https://github.com/hg/zm-client/pull/12"}),
        ("mcp__hg__gcal_get_event", {"event_id": "evt_0123456789ab"}, {"id": "evt_0123456789ab"}),
    ]


def _self_test() -> None:
    import selftest_sandbox
    policy = load_policy()
    with selftest_sandbox.scratch_tmp("budget_outcome_") as tmp:
        td = Path(tmp) / "task"
        (td / "Working_Files").mkdir(parents=True)
        (td / "06_PreCheck_Trajectory").mkdir()
        (td / "Working_Files" / BUDGET).write_text(json.dumps(_budget(), indent=1) + "\n")
        (td / SQL).write_text(_SQL)
        pre = td / "06_PreCheck_Trajectory" / "trajectory.json"

        def run(calls, name=None):
            p = pre if name is None else td / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(_events(calls)) + "\n")
            return p
        # id forms
        assert norm_ts(1700000000.0001) == "1700000000.000100" and norm_ts("1700000000.0001") == "1700000000.000100"
        assert norm_ts(12) is None and norm_ts("ENG-77") is None
        f = id_forms({"record_id": "robert@hg.co/<CAPBs_a5shT3@mail.gmail.com>"})
        assert f["kind"] == "gmail" and "<capbs_a5sht3@mail.gmail.com>" in f["exact"]
        assert id_forms({"record_id": "zm-client#12"})["github"] == ("zm-client", "zm-client", 12)
        recs = sql_records(_SQL)
        wins = body_windows(id_forms({"record_id": "C0123ABCD/1700000000.000100"}), recs)
        assert wins and all(len(w) == WINDOW and w in _ANCHOR_TEXT.lower() for w in wins), wins
        # 1. GO: pointers, listings and a write never count as opened
        run(_go_calls())
        r = evaluate(td, policy=policy)
        u = {x["unit"]: x for x in r["units"]}
        assert r["outcome"] == "GO" and r["verdict"] == "PASS", r["checks"]
        assert not u["U1"]["opened"] and u["U1"]["referenced_step"] == 1, u["U1"]
        assert not u["U2"]["opened"] and u["U2"]["listed_step"] == 2, u["U2"]
        assert u["U3"]["opened"] and u["U3"]["first_step"] == 4 and u["U3"]["how"] == "argument"
        assert not u["U4"]["opened"] and u["U4"]["listed_step"] == 5
        assert u["U5"]["opened"] and u["U5"]["first_step"] == 7 and u["U5"]["how"] == "argument"
        assert u["U6"]["consistent"] is None and u["U6"]["opened"]
        assert all(u[k]["consistent"] is True for k in ("U1", "U2", "U3", "U4", "U5")) and r["hand_review"] == []
        assert to_text(r).splitlines()[0] == "BUDGET OUTCOME: GO" and "HAND-REVIEW: none" in to_text(r)
        assert set(r["bound_to"]) == {"Working_Files/01_Difficulty_Budget.json", "01_Universe_Inject.sql",
                                      "06_PreCheck_Trajectory/trajectory.json"}
        # 2. NO-GO: a thread read returns the anchor (Slack ts as a float), and a full Gmail read returns the other
        calls = _go_calls() + [
            ("mcp__hg__slack_conversations_replies", {"channel_id": "C0123ABCD", "thread_ts": "1700000000.000001"},
             {"ok": True, "messages": [{"ts": 1700000000.000001, "text": "root"},
                                       {"ts": 1700000000.0001, "text": "small correction", "thread_ts": "1700000000.000001"}]}),
            ("mcp__hg__gmail_get_thread", {"thread_id": "robert@hg.co/185", "format": "full"},
             {"id": "robert@hg.co/185", "messages": [{"id": "robert@hg.co/<CAPBs_a5shT3@mail.gmail.com>",
                                                      "payload": {"body": {"data": "receipt text"}}}]})]
        run(calls)
        r = evaluate(td, policy=policy)
        u = {x["unit"]: x for x in r["units"]}
        assert r["outcome"] == "NO-GO" and r["verdict"] == "FAIL" and r["opened_anchors"] == ["U1", "U2"]
        assert u["U1"]["first_step"] == 9 and u["U1"]["how"] == "result" and u["U1"]["consistent"] is False
        assert u["U2"]["first_step"] == 10 and u["U2"]["how"] == "result"
        assert [h["unit"] for h in r["hand_review"]] == ["U1", "U2"], "only contradicting units need hand review"
        text = to_text(r)
        assert text.splitlines()[0] == "BUDGET OUTCOME: NO-GO" and "anchor U1" in text and "step 9" in text
        # 3. a spilled channel read: unknown, never opened by itself; a Bash read of the file that prints the text is
        spill = [("mcp__hg__slack_read_channel", {"channel_id": "#ops"}, _SPILL),
                 ("mcp__hg__slack_send_message", {"channel_id": "#ops", "message": "hi"},
                  {"ok": True, "channel": "C0123ABCD", "ts": 1700009999.0})]
        run(spill)
        r = evaluate(td, policy=policy)
        u = {x["unit"]: x for x in r["units"]}
        assert r["outcome"] == "GO" and r["verdict"] == "WARN" and u["U1"]["spilled_container_reads"] == [1]
        assert r["unverified"] == ["U1"] and any(c["id"] == "precheck.spilled" for c in r["checks"])
        run(spill + [("Bash", {"command": "python3 read.py"}, "leonard: " + _ANCHOR_TEXT + "\nShell cwd was reset")])
        r = evaluate(td, policy=policy)
        u = {x["unit"]: x for x in r["units"]}
        assert r["outcome"] == "NO-GO" and u["U1"]["how"] == "body" and u["U1"]["first_step"] == 3
        run(spill + [("Bash", {"command": "grep ts"}, "1700000000.000100 U1 [0]\n1700000000.000001 U2 [3]")])
        r = evaluate(td, policy=policy)
        u = {x["unit"]: x for x in r["units"]}
        assert not u["U1"]["opened"] and u["U1"]["listed_step"] == 3, "a printed ts without the text is a listing"
        # 4. a subagent's read counts, with its context
        run([("Agent", {"prompt": "read the thread C0123ABCD/1700000000.000100"}, "done"),
             ("mcp__hg__slack_conversations_replies", {"channel_id": "C0123ABCD", "thread_ts": "1700000000.000100"},
              {"ok": True, "messages": []}, "toolu_000")])
        r = evaluate(td, policy=policy)
        u = {x["unit"]: x for x in r["units"]}
        assert u["U1"]["opened"] and u["U1"]["how"] == "argument" and u["U1"]["context"] == "subagent"
        assert u["U1"]["first_step"] == 2, "an id inside an Agent brief is not a read"
        # 5. --write: bound outcome file, one log entry per trajectory, the stop rule per design
        run(calls)
        r = evaluate(td, policy=policy)
        w = write_outcome(td, r, today="2026-11-11")
        assert w["appended"] is True and w["logged_verdict"] == "NO-GO"
        stored = json.loads((td / "Working_Files" / OUTCOME).read_text())
        assert stored["schema"] == OUTCOME_SCHEMA and stored["bound_to"] == r["bound_to"] and stored["outcome"] == "NO-GO"
        log = json.loads((td / "Working_Files" / LOG).read_text())
        e = log["entries"][0]
        assert len(log["entries"]) == 1 and e["design_id"] == "D1" and e["budget_revision"] == "rev1"
        assert e["sql_sha256"] == sha256_file(td / SQL) and e["trajectory_sha256"] == sha256_file(pre)
        assert write_outcome(td, evaluate(td, policy=policy))["appended"] is False, "never twice for one trajectory"
        assert len(json.loads((td / "Working_Files" / LOG).read_text())["entries"]) == 1
        s = stop_rule(td, policy)
        assert s["verdict"] == "PASS" and s["no_go"] == 1 and s["stop"] is None
        run(calls + [("mcp__hg__linear_get_issue", {"id": "ENG-1"}, {"id": "ENG-1"})])
        write_outcome(td, evaluate(td, policy=policy))
        s = stop_rule(td, policy)
        assert s["verdict"] == "FAIL" and s["no_go"] == 2, s
        assert s["stop"] == ("STOP: two pre-checks on design D1 missed the budget — return to /create-scenario for a "
                             "redesign, not another patch")
        assert s["stop"] in to_text(s) and s["checks"][0]["id"] == "precheck.stop_rule"
        bp = td / "Working_Files" / BUDGET
        b = json.loads(bp.read_text())
        b["design_id"] = "D2"
        bp.write_text(json.dumps(b, indent=1) + "\n")
        s = stop_rule(td, policy)
        assert s["verdict"] == "PASS" and s["no_go"] == 0, "a redesign starts a new count"
        # 6. a baseline folder: share of runs that opened each decider against the declared range
        base = td / "07_Baseline_Trajectories"
        for i in range(1, 7):
            extra = calls[8:9] if i == 1 else []                       # run 1 opens the first anchor
            body = [c for c in _go_calls() if not (c[0].endswith("linear_get_issue") and i > 3)] + extra
            run(body, f"07_Baseline_Trajectories/trajectory-run-{i}.json")
        r = evaluate(td, base, policy)
        t = {x["unit"]: x for x in r["units"]}
        assert r["mode"] == "baseline" and len(r["runs"]) == 6
        assert t["U1"]["opened_runs"] == 1 and t["U1"]["position"] == "above", t["U1"]
        assert t["U2"]["opened_runs"] == 0 and t["U2"]["position"] == "inside"
        assert t["U3"]["opened_runs"] == 3 and t["U3"]["position"] == "inside"
        assert t["U4"]["position"] == "below" and t["U5"]["position"] == "above" and t["U6"]["position"] == "not judged"
        assert r["verdict"] == "WARN" and "baseline, 6 runs" in to_text(r).splitlines()[0]
        try:
            write_outcome(td, r)
            raise AssertionError("a baseline folder must not be written as a pre-check")
        except UsageError:
            pass
        # 7. usage errors
        for bad in (lambda: evaluate(Path(tmp) / "nowhere"), lambda: evaluate(td, td / "missing.json")):
            try:
                bad()
                raise AssertionError("a missing input must be a usage error")
            except UsageError:
                pass
    print("self-test: ok (id forms, GO, NO-GO with step, listed / referenced / write not opened, spilled read, body "
          "window through Bash, subagent read, --write binding and log once, stop rule per design, baseline shares)")


# ------------------------------------------------------------------ CLI

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        _self_test()
        return 0
    ap = argparse.ArgumentParser(prog="budget_outcome.py", description="Compare a run with the difficulty budget.")
    sub = ap.add_subparsers(dest="command")
    p = sub.add_parser("compare")
    p.add_argument("--task-dir", required=True)
    p.add_argument("--trajectory", default=None, help="a trajectory file, or a folder of runs (baseline)")
    p.add_argument("--write", action="store_true", help=f"store Working_Files/{OUTCOME} and append {LOG}")
    p.add_argument("--today", default=None, help="YYYY-MM-DD recorded with --write (no clock is read)")
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("stop-rule")
    p.add_argument("--task-dir", required=True)
    p.add_argument("--json", action="store_true")
    try:
        args = ap.parse_args(argv)
    except SystemExit as error:
        return 2 if error.code not in (0, None) else 0
    if not args.command:
        ap.print_usage(sys.stderr)
        return 2
    try:
        if args.command == "stop-rule":
            r = stop_rule(args.task_dir)
        else:
            if args.today and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.today):
                raise UsageError("--today must be YYYY-MM-DD")
            r = evaluate(args.task_dir, args.trajectory)
            if args.write:
                r["written"] = write_outcome(args.task_dir, r, args.today)
    except UsageError as error:
        print(f"budget_outcome: {error}", file=sys.stderr)
        return 2
    except Exception as error:  # a refused write (read-only root)
        if error.__class__.__name__ == "ContextError":
            print(f"budget_outcome: {error}", file=sys.stderr)
            return 2
        raise
    print(json.dumps(r, indent=1, sort_keys=True, ensure_ascii=False) if args.json else to_text(r))
    return 1 if r["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())

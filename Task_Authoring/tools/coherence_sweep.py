#!/usr/bin/env python3
"""coherence_sweep.py - the universe coherence sweep: reviewer brief, sweep record and its check (plan WS4).

The platform's /prompt review fails a task for any unresolved material fork (two fair readings that lead to
different graded outcomes) and for any contradiction between records, whoever introduced it. Most failed /prompt
rounds were such defects in the injected records, found one family per round. This tool makes the sweep for them a
recorded step that is bound to the current bytes.

The sweeping is done by cold reviewers (subagents that get only the prompt and the universe) and by the author.
This tool prepares the brief, lists mechanical candidates, and checks that the record of what was found and how it
was settled is complete.

Commands
  brief --task-dir T [--reviewer N] [--previous A.sql]
      Writes Working_Files/local_reviews/coherence/brief_<N>.md: the prompt (before a prompt exists: the records
      that carry the ask, from the manifest), the injected records grouped by service and container with ids,
      authors, dates and text, and the instruction to list every material reading and every contradiction in a
      fixed JSON shape. The brief holds no design, no manifest answer and no rubric. With --previous the records a
      revision changed and their neighbours are marked, and the reviewer is told to report on those.
  candidates --task-dir T [--universe normal|synthcut] [--run-base no|yes|auto] [--json]
      A mechanical pre-pass for the author. Header `COHERENCE SWEEP (candidates): PASS|WARN` (WARN while any
      candidate has no entry in the record), one line per candidates.* check, then the lists: quantifier spans in
      the prompt (and in the records that carry the ask) with no open_sets entry; injected records that give one
      entity different values (amount, date, status, owner) in different services; a weekday that does not match its
      date; one day with two years; a reply or comment dated before the injected record it hangs on; known-issue
      cards touched (strong: a card id term or figure in the injected text or prompt, a card id term or the card id
      in the manifest, or the card names the persona; weak: names only, grouped by name); each seeded fact of the
      manifest with the terms to search the base for; family members of a recorded defect that were not checked.
      The base searches run through tools/hg.py only with --run-base yes (or auto with a ready V3 context): they
      scan every export and take many minutes, so the default is no.
  check --task-dir T [--previous A.sql] [--universe U] [--json]
      Header `COHERENCE SWEEP (<scope>): PASS|WARN|FAIL`, one line per check:
        sweep.bound            the record's hashes equal the current SQL and prompt
        sweep.chain            (revision scope) the record names the previous SQL and a previous sweep that ends in a
                               full sweep, and lists every record the revision changed
        sweep.reviewers        two or more reviewers, each with a model, a brief hash and a findings file; the kept
                               brief file has that hash and was built from the current bytes
        sweep.findings         every finding in a reviewer's file is taken up by a fork, a defect or an open set, or
                               dismissed with a reason
        sweep.forks            no open material fork; settled_in_data names records that exist in the current SQL;
                               both_fair carries both figures
        sweep.prompt_sentences WARN for each fork settled by adding a sentence to the prompt
        sweep.open_sets        every quantifier span in the current prompt has a rule and a census whose ids exist
        sweep.siblings         every recorded defect is closed and has a sibling list for each family (same
                               author, thread, template, service and type) naming every injected member
        sweep.base             every seeded fact of the manifest has a base search, a result count and dispositions
        sweep.known_issues     every strong known-issue card (see candidates) has a disposition; WARN for cards
                               touched by name only
        sweep.conflicts        WARN only: value and chronology conflicts from `candidates` without a disposition
      For a revision scope the fork and sibling requirements apply to the changed records and their neighbours
      (from revision_scope.py); entries about other records are carried over and only checked for being closed.
  template --task-dir T [--previous A.sql] [--universe U]
      Prints a starting record (hashes, scope, candidate lists) to stdout. Writes nothing.
  --self-test

Record: <task>/Working_Files/01d_Coherence_Sweep.json
  {"schema": "coherence-sweep-v1",
   "bound_to": {"01_Universe_Inject.sql": "<sha256>", "04_Prompt.txt": "<sha256>"},
   "scope": "full" | "revision",
   "previous_sql_sha256": "...", "changed_record_ids": ["..."],              (revision)
   "previous_sweep": {"path": "Working_Files/run_forensics/rev1/01d_Coherence_Sweep.json", "sha256": "..."},
   "universe": "normal" | "synthcut",
   "reviewers": [{"id": "1", "model": "...", "brief_sha256": "...", "findings": "Working_Files/local_reviews/coherence/findings_1.json"}],
   "forks": [{"id": "F1", "span": "...", "record_ids": ["..."], "sources": ["1:F2"],
              "reading_a": {"reading": "...", "outcome": "..."}, "reading_b": {"reading": "...", "outcome": "..."},
              "material": true, "reason": "...",
              "status": "open" | "settled_in_data" | "both_fair" | "prompt_sentence",
              "settled": {"record_ids": ["..."], "sql_revision": "rev3"},
              "both_fair": {"figure_a": "...", "figure_b": "...", "rubric_accepts_both": true},
              "prompt_sentence": {"sentence": "...", "reason": "..."},
              "rechecked_sql_sha256": "..."}],
   "open_sets": [{"span": "...", "where": "prompt", "sources": ["1:S1"], "rule": "...",
                  "census": {"count": 3, "ids": ["..."], "base_ids": ["..."]}}],
                 (or {"span": "...", "not_a_population": "<reason>"})
   "siblings": [{"id": "D1", "defect": "...", "record_ids": ["..."], "sources": ["2:C1"],
                 "status": "fixed_in_data" | "not_a_defect" | "known_issue" | "open",
                 "fix": {"record_ids": ["..."], "sql_revision": "rev3"}, "reason": "...", "card": "NB-1",
                 "families": [{"kind": "same_author" | "same_thread" | "same_template" | "same_service_type",
                               "checked_ids": ["..."], "none": "<reason when the family is empty>"}]}],
   "base_consistency": [{"fact": "<manifest fact key>", "search": "...", "result_count": 4,
                         "conflicts": [{"id": "...", "disposition": "..."}], "disposition": "..."}],
   "known_issues": [{"card": "NB-14", "disposition": "..."}],
   "conflicts": [{"candidate": "X:status:ENG-900", "disposition": "..."}],
   "dismissed": [{"source": "2:F4", "reason": "..."}]}

Limits. The pre-pass reads injected text, the prompt and the manifest only; a fork or contradiction that lives in
base records (or between an injected record and the base) is found by the reviewers or not at all. It points at the
rule sentence of an open set, not at its edge members: the census does that. The value-conflict and known-issue
matches are word matches and print false candidates; each needs one line of disposition. The check cannot tell
whether a reviewer was really cold.

Exit code: 0 PASS or WARN, 1 FAIL, 2 usage error. Stdlib only. `brief` writes one file; nothing else is written.
"""
from __future__ import annotations

import argparse
import calendar
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WS = BUNDLE.parent
sys.path.insert(0, str(HERE))

import revision_scope as rs  # noqa: E402  (sibling tool; nothing runs at import)

TOOL = "coherence_sweep"
VERSION = 1
SCHEMA = "coherence-sweep-v1"
SQL_NAME = rs.SQL_NAME
PROMPT_NAME = rs.PROMPT_NAME
RECORD_NAME = "01d_Coherence_Sweep.json"
CONTEXT_NAME = "00_Task_Context.json"
REVIEW_DIR = Path("Working_Files") / "local_reviews" / "coherence"
CARDS_DIR = BUNDLE / "references" / "known_data_issues"
ROSTER = BUNDLE / "references" / "persona_roster_v2.json"

# Thresholds chosen here (not in references/first_pass_policy.json; listed in the hand-over report).
MIN_REVIEWERS = 2            # the brief asks for at least two cold reviewers
CHAIN_MAX = 50               # longest chain of revision sweeps followed back to a full sweep
AMOUNT_NEAR = 0.25           # two amounts for one entity are a candidate when they differ by at most this share
LISTING_VALUE_MAX = 600      # non-text column values longer than this are cut in the brief
FACT_VALUE_MAX = 40          # a fact value at most this long is also searched in the base
BASE_SEARCH_LIMIT = 20       # matches kept per base query
BASE_SEARCH_TIMEOUT_S = 900
BASE_SERVICES = ("slack", "gmail", "linear", "trello", "gdocs", "gsheets", "gslides", "gcal", "confluence",
                 "contacts", "snowflake", "github", "gdrive")
BASE_FILE = {"github": "data.json", "gdrive": "data.json"}   # structured export only; blobs are not searched

FORK_STATUSES = ("open", "settled_in_data", "both_fair", "prompt_sentence")
DEFECT_STATUSES = ("open", "fixed_in_data", "not_a_defect", "known_issue")
FAMILY_KINDS = ("same_author", "same_thread", "same_template", "same_service_type")
FINDING_KINDS = ("forks", "contradictions", "open_sets")
RECORD_LISTS = ("reviewers", "forks", "open_sets", "siblings", "base_consistency", "known_issues", "conflicts",
                "dismissed", "changed_record_ids")
UNIVERSES = ("normal", "synthcut")
EMPTY = (None, "", "[]", "{}", "null")
LISTING_SKIP = {"headers_json", "payload_json", "style_runs_json", "mbox_from", "size_estimate", "history_id",
                "date_parsed_source", "x_emu", "y_emu", "width_emu", "height_emu", "pos", "cover_json", "shortlink",
                "shorturl", "url", "icon_link", "web_view_link", "hangout_link", "revision_id", "internal_date",
                "placeholder_type", "seq", "position", "commit_id", "ordinal", "original_start_json",
                "recurring_event_id", "rrule_json", "metadata_json", "is_activity_message", "state_history_json"}

QUANTIFIER_RX = re.compile(
    r"\b(?:every(?:one|body|thing)?|each|all|any(?:one|body|thing)?|whoever|whatever|whichever|remaining|"
    r"outstanding|the\s+rest|still\s+(?:has|have|needs?)\s+to|still[\s-]+(?:needs?|owe[sd]?|open|due|pending|"
    r"missing|left|to[\s-]+do)|left\s+to\s+(?:do|land|ship|send|pay)|"
    r"(?:if|when(?:ever)?|where(?:ver)?)\s+(?:a|an|any|one|some)(?=\s))\b", re.I)
IDIOM_RX = re.compile(
    r"\b(?:at all|after all|all set|all good|all right|all the best|all in all|all along|all (?:day|week|night)|"
    r"(?:we|you|they|us) all|any chance|any ?time|any ?more|in any case|at any rate|any luck|any idea|any thoughts|"
    r"any questions?|any updates?|shares outstanding|outstanding (?:shares|stock|options?)|"
    r"repl(?:y|ies|ying|ied)[ -](?:to[ -])?all|all recipients)\b", re.I)
# Mail footers and legal boilerplate: their "any" and "anyone" define no population the task works on.
BOILERPLATE_RX = re.compile(r"intended recipient|unauthori[sz]ed|confidential|privileged|engagement letter|"
                            r"unsubscribe|do not reply|email preferences", re.I)
SENTENCE_RX = re.compile(r"(?<=[.!?])\s+|\n+")
LINEAR_KEY_RX = re.compile(r"(?<![A-Za-z0-9])(?:ENG|ZOM|ART|DES|EPI)-\d{1,5}(?![0-9])")
PR_ID_RX = re.compile(r"harmonygames-Games/[\w.-]+#\d+")
NAME_RX = re.compile(r"\b[A-Z][A-Za-z0-9']+(?:[ -](?:[A-Z][A-Za-z0-9']+|&|3D))*")
AMOUNT_RX = re.compile(r"(?<![\w.,])(\$\s?)?(\d{1,3}(?:,\d{3})+|\d+)(\.\d+)?\s?([KkMm])?(?![\w]|[.,]\d)")
MONTHS = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")
_MON = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?"
DATE_RX = re.compile(r"\b(?:(Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*\.?,?\s+)?" + _MON
                     + r"\s+(\d{1,2})(?:st|nd|rd|th)?(?:,?\s+(\d{4}))?\b")
WEEKDAYS = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
DATE_ROLE_RX = re.compile(r"\b(due|deadline|effective|launch(?:es|ed)?|release[sd]?|ships?|starts?|ends?|expires?|"
                          r"kickoff|signed|terminat\w+|last day)\b", re.I)
STATUS_DONE = ("done", "fixed", "merged", "shipped", "released", "live", "deployed", "completed", "complete",
               "closed", "resolved", "approved", "signed", "paid", "sent", "landed")
STATUS_OPEN = ("open", "in progress", "in review", "todo", "to do", "backlog", "pending", "blocked", "held",
               "on hold", "not started", "broken", "unpaid", "outstanding", "waiting", "incomplete", "triage",
               "in validation", "validation", "regression")
STATUS_CANCEL = ("canceled", "cancelled", "withdrawn", "rejected", "dropped", "declined", "duplicate")
NEGATION_RX = re.compile(r"\b(?:not|never|no longer|isn't|wasn't|hasn't|haven't|aren't|didn't|won't|n't)\s+"
                         r"(?:yet\s+|been\s+|get\s+|got\s+)*(" + "|".join(STATUS_DONE) + r")\b", re.I)
OWNER_RX = (re.compile(r"\b(?:owner|owned by|assigned to|assignee|lead|dri)\s*(?:is|:|-)?\s+([A-Z][a-z]+)"),
            re.compile(r"\b([A-Z][a-z]+)\s+(?:owns|is owning|will own|is on it|is on this|is taking|is handling)\b"))
NAME_STOP = {w.casefold() for w in (
    "The It One They Use Only Who What Whether Which How A An But Not No Nothing Each Both Some Any Why Refer Grade "
    "If When Where Then That This These Those There Here And Or So For From With Without About After Before Since "
    "Until While Because Also Still Just Yes Ok Okay Thanks Thank Hi Hey Hello Dear Regards Best Cheers Please Re Fwd "
    "I We You He She Our Your My His Her Their Its Is Are Was Were Will Can Could Should Would Did Does Do Has Have Had "
    "Slack Linear Gmail Snowflake Confluence Trello GitHub Drive Sheets Docs Slides Calendar Google Jira Android iOS "
    "Jan Feb Mar Apr May Jun Jul Aug Sep Sept Oct Nov Dec January February March April June July August September "
    "October November December Monday Tuesday Wednesday Thursday Friday Saturday Sunday Mon Tue Wed Thu Fri Sat Sun "
    "Done Todo Backlog Canceled Cancelled Duplicate PR PRs Q1 Q2 Q3 Q4 UTC PT PST PDT AM PM FYI TBD USD EUR "
    "Don't Doesn't Didn't Isn't Wasn't Can't Won't Let's That's It's I'm I'll I've We're We'll We've You're "
    "Team Update Updated Note Notes New Old Next Last First Second Third All Everyone Sorry Sure Great Good Quick "
    "Monthly Weekly Daily Exact Use Safer Watch Caused FAIL FAILs Records Record People Board Ticket Tickets").split()}


class UsageError(Exception):
    """A missing or unreadable input: exit code 2."""


# ---------------------------------------------------------------- files

def sha256_file(path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _rel_task(task_dir, path) -> str:
    try:
        return Path(path).resolve().relative_to(Path(task_dir).resolve()).as_posix()
    except ValueError:
        return Path(path).as_posix()


def _list(value) -> list:
    """A record field that should be a list: the list itself, or [] for anything else (never raises)."""
    return value if isinstance(value, list) else []


def _load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8")), None
    except OSError as exc:
        return None, f"cannot read {path}: {exc}"
    except ValueError as exc:
        return None, f"{Path(path).name} is not valid JSON: {exc}"


def task_files(task_dir) -> dict:
    """The task's files, found the way stage_gate.slot_path finds them. Raises UsageError without a SQL file."""
    from stage_gate import slot_path
    task_dir = Path(task_dir)
    if not task_dir.is_dir():
        raise UsageError(f"task folder not found: {task_dir}")
    sql = slot_path(task_dir, SQL_NAME)
    if not sql.is_file():
        raise UsageError(f"no {SQL_NAME} in {task_dir}")
    prompt = slot_path(task_dir, PROMPT_NAME)
    prompt_text = ""
    if prompt.is_file():
        try:
            prompt_text = prompt.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            raise UsageError(f"cannot read {prompt}: {exc}") from exc
    manifest, manifest_path = rs._manifest(task_dir)
    context, _ = _load_json(slot_path(task_dir, CONTEXT_NAME)) if slot_path(task_dir, CONTEXT_NAME).is_file() \
        else (None, None)
    try:
        sql_text = sql.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise UsageError(f"cannot read {sql}: {exc}") from exc
    return {"task_dir": task_dir, "sql": sql, "sql_text": sql_text, "sql_sha256": sha256_file(sql),
            "prompt": prompt, "prompt_text": prompt_text, "has_prompt": bool(prompt_text.strip()),
            "prompt_sha256": sha256_file(prompt) if prompt_text.strip() else None,
            "record": slot_path(task_dir, RECORD_NAME), "manifest": manifest, "manifest_path": manifest_path,
            "context": context if isinstance(context, dict) else None}


def universe_of(files: dict, record: dict | None = None, override: str | None = None) -> str | None:
    """normal or synthcut: --universe, then the task context, then the record. Never guessed."""
    if override:
        return override
    ctx = files.get("context") or {}
    key = (ctx.get("universe") or {}).get("key") if isinstance(ctx.get("universe"), dict) else None
    if key in UNIVERSES:
        return key
    by_date = {"2026-02-14": "normal", "2025-10-01": "synthcut"}.get(str(ctx.get("universe_date_key")))
    if by_date:
        return by_date
    if record and record.get("universe") in UNIVERSES:
        return record["universe"]
    return None


def _atomic_write(path: Path, text: str, what: str) -> None:
    from task_context import refuse_read_only
    refuse_read_only(path, what)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        if os.path.lexists(tmp):
            os.unlink(tmp)
        raise


def _find_previous_sql(task_dir, sha: str):
    """The stored revision whose bytes have this sha256 (Working_Files/run_forensics/<rev>/01_Universe_Inject.sql)."""
    root = Path(task_dir) / "Working_Files" / "run_forensics"
    if not root.is_dir():
        return None
    for path in sorted(root.glob(f"*/{SQL_NAME}")):
        if sha256_file(path) == sha:
            return path
    return None


# ---------------------------------------------------------------- record listing for the brief

def _render_record(rec: dict, mark: str | None = None) -> list:
    f = rec["fields"]
    own = {rec["id"], *rec["aliases"]}
    meta = [f"table: {rec['table']}", "statement: " + "+".join(rec["ops"])
            + ("" if "insert" in rec["ops"] else " (changes a record that is in the base)")]
    if rec["aliases"]:
        meta.append("row id: " + ", ".join(rec["aliases"]))
    if rec["author"]:
        meta.append(f"author: {rec['author']}")
    if rec["date"]:
        meta.append(f"date: {rec['date']}")
    if rec["thread"] and rec["thread"] != rec["id"]:
        meta.append(f"thread: {rec['thread']}")
    lines = [f"#### {rec['id']}" + (f"  [{mark}]" if mark else ""), " | ".join(meta)]
    for col, value in f.items():
        low = col.lower()
        if value in EMPTY or low in LISTING_SKIP or low.endswith("_fts") or str(value) in own:
            continue
        if str(value).lower() in ("false", "f") or (low == "body_html" and f.get("body_text")):
            continue
        is_text = low in rs.TEXT_COLS or col in rs.JSON_TEXT_COLS
        text = rs.json_text(col, value) if col in rs.JSON_TEXT_COLS else str(value)
        if is_text:
            text = rs.unescape(text)
        if not text.strip():
            continue
        if not is_text and len(text) > LISTING_VALUE_MAX:
            text = text[:LISTING_VALUE_MAX] + f" ... ({len(text)} characters; open the record for the rest)"
        if "\n" in text:
            lines.append(f"{col}:")
            lines += ["    " + ln for ln in text.splitlines()]
        else:
            lines.append(f"{col}: {text}")
    return lines


def render_listing(records: dict, marks: dict | None = None) -> list:
    """Injected records grouped by service and container, with ids, authors, dates and text."""
    marks = marks or {}
    grouped = {}
    for key in sorted(records):
        rec = records[key]
        container = str(rec["container"]) if rec["container"] else "(container not named in the SQL)"
        grouped.setdefault(rec["service"], {}).setdefault(container, []).append(rec)
    lines = []
    for service in sorted(grouped):
        lines += [f"## {service}", ""]
        for container in sorted(grouped[service]):
            lines += [f"### {service} container {container}", ""]
            for rec in sorted(grouped[service][container], key=lambda r: (str(r["date"] or ""), r["id"], r["table"])):
                lines += _render_record(rec, marks.get(rec["key"])) + [""]
    return lines


# ---------------------------------------------------------------- brief

FINDINGS_SHAPE = """{
  "reviewer": "<your reviewer id>",
  "forks": [
    {"id": "F1",
     "span": "<the words of the prompt, or of a record, that can be read two ways>",
     "record_ids": ["<records involved>"],
     "reading_a": {"reading": "<first fair reading>", "outcome": "<what gets decided, written, sent or reported>"},
     "reading_b": {"reading": "<second fair reading>", "outcome": "<what gets decided, written, sent or reported>"},
     "material": true,
     "figure_only": false,
     "reason": "<why the outcomes differ, or why they do not>",
     "settling_record": "<id of a record the persona can open that rules one reading out, or null>"}
  ],
  "contradictions": [
    {"id": "C1",
     "record_ids": ["<record>", "<record it disagrees with>"],
     "about": "<the person, ticket, vendor, file or event>",
     "field": "amount | date | status | owner | identity | count | lifecycle | chronology | other",
     "value_a": "<what the first record says>",
     "value_b": "<what the second record says>",
     "introduced_by": "injected | base | both",
     "matters_because": "<what a reader would get wrong>"}
  ],
  "open_sets": [
    {"id": "S1",
     "span": "<the words that define a population>",
     "where": "prompt | <record id>",
     "rule": "<who or what is in, as you read it>",
     "members": ["<every member you found>"],
     "edge_members": [{"id": "<record>", "why": "<why the rule does not say in or out>"}]}
  ],
  "not_checked": ["<anything you could not read or did not get to>"]
}"""


def _ask_section(files: dict, records: dict) -> list:
    """Before a prompt exists: the records that carry the ask, by id only. No kinds, rules, quotes or answers."""
    manifest = files["manifest"] or {}
    index = rs.id_index(records)
    lines = ["## The ask (no prompt is written yet)", ""]
    anchors = [a for a in _list(manifest.get("anchors")) if isinstance(a, dict)]
    fragments = [k for k in _list(manifest.get("ask_fragments")) if isinstance(k, dict)]
    if not anchors and not fragments:
        return lines + ["No prompt and no manifest with ask fragments were found. Review the records for "
                        "contradictions only.", ""]
    if anchors:
        lines.append("The prompt will point the persona at:")
        for a in anchors:
            lines.append(f"- {a.get('prompt_reference') or 'a record'}: {a.get('locator') or '(no locator)'}")
        lines.append("")
    if fragments:
        lines.append("Records that carry parts of the ask (injected ones are in the listing below; read the others "
                     "in the base):")
        seen = []
        for k in fragments:
            for rid in [k.get("locator"), *_list(k.get("seeded_ids")), *_list(k.get("base_pointers"))]:
                if rid and rid not in seen:
                    seen.append(rid)
        for rid in seen:
            keys = index.get(rid, [])
            shown = ", ".join(sorted({records[key]["id"] for key in keys})) if keys else f"{rid} (base)"
            lines.append(f"- {shown}")
        lines.append("")
    return lines


def build_brief(task_dir, reviewer: str = "1", previous_sql=None) -> dict:
    """The cold-reviewer brief as text, with its sha256 and its path. Deterministic for the same inputs."""
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,32}", str(reviewer)):
        raise UsageError("--reviewer must be 1 to 32 letters, digits, '-' or '_'")
    files = task_files(task_dir)
    records = rs.load_records(files["sql_text"])["records"]
    marks, removed, scope_line = {}, [], "Scope: full"
    if previous_sql:
        diff = rs.diff_files(previous_sql, files["sql"])
        for e in diff["entries"]:
            if e["state"] == "removed":
                removed.append(e)
                continue
            marks[e["key"]] = "CHANGED in this revision" if e["state"] == "changed" else "ADDED in this revision"
        for e in diff["entries"]:
            for relation in ("copy", "thread", "reference", "container"):
                for key in e["neighbours"][relation]:
                    marks.setdefault(key, "next to a changed record")
        scope_line = f"Scope: revision (previous SQL sha256 {sha256_file(previous_sql)})"
    ctx = files["context"] or {}
    universe = ctx.get("universe") if isinstance(ctx.get("universe"), dict) else {}
    findings = (REVIEW_DIR / f"findings_{reviewer}.json").as_posix()
    out = [f"# Coherence review brief (reviewer {reviewer})", "",
           f"Bound to: {SQL_NAME} sha256 {files['sql_sha256']}; {PROMPT_NAME} "
           + (f"sha256 {files['prompt_sha256']}" if files["has_prompt"] else "not written yet"),
           scope_line, "",
           "## What you have", "",
           "- The prompt below" + ("." if files["has_prompt"] else " is not written yet; the ask is described instead."),
           "- The universe: the base data, read through the search helpers (`python3.12 -B "
           f"Task_Authoring/tools/hg.py search ... --task-dir {rs._rel(task_dir)}` picks this task's universe; "
           "`Task_Authoring/tools/persona_view.py`), and the injected records listed below. Injected records are laid "
           "over the base and are not in the base search, so read them here.",
           ]
    if ctx.get("persona_name"):
        out.append(f"- The persona: {ctx['persona_name']} ({ctx.get('persona_role') or 'role not given'}"
                   + (f", {ctx['email']}" if ctx.get("email") else "") + "). Only a record this persona can open "
                   "settles anything.")
    if universe.get("label") or universe.get("clock_text"):
        out.append(f"- The universe date: {universe.get('label') or ''}".rstrip()
                   + (f", clock {universe['clock_text']}" if universe.get("clock_text") else "")
                   + ". Nothing after the clock exists.")
    out += ["",
            "You are not given the task design, an expected answer or grading rows, and you must not look for them: "
            "do not open the task's Working_Files folder, its Oracle Events, its rubric or its reference notes. Work "
            "from the prompt and the records only, as a careful stranger would.", "",
            "## What to report", "",
            "1. Every material reading. A fork is two fair readings of the prompt, or of a record the prompt points "
            "to, that lead to different outcomes: a different decision, write, destination, recipient or content. "
            "Report it unless you can quote a record the persona can open that rules one reading out. \"Less "
            "likely\" does not rule a reading out. A claim by the item's own owner about their own work does not "
            "settle it. When no record speaks to an item at all, that is still a fork. When the two readings differ "
            "only in one reported figure (an amount, a count, a rate or a date), set figure_only to true.",
            "2. Every contradiction. Two records that disagree about the same thing: an amount, a date, a status, "
            "an owner, a name or identity, a count, a lifecycle state (a closed ticket with later activity, a "
            "ticked checklist whose item is still open) or the order of events (a reply before its parent, a record "
            "that cites something created later). Report it whoever introduced it: injected against injected, "
            "injected against base, or base against base where the task has to read those base records.",
            "3. Every population. For each phrase that defines a set (every, all, each, any, whoever, what still "
            "has to, remaining, outstanding, the rest, \"if a ...\"), in the prompt or in a record that carries the "
            "ask: write the membership rule as you read it, list every member you find in the universe, and list "
            "the edge members, where the rule does not say in or out.", ""]
    if previous_sql:
        out += ["This is a review of one revision. Records marked ADDED, CHANGED or \"next to a changed record\" "
                "are the scope: report every fork, contradiction and population edge that involves one of them. The "
                "other records are context. Check too that nothing still depends on a removed record.", ""]
    out += ["Read the base around each injected record: its thread, its parent, the records it names, and other "
            "records about the same person, ticket, vendor or date. List what you could not read under not_checked.",
            "",
            "## Output", "",
            "Return one JSON object in exactly this shape (empty lists are fine; keep the keys). It is saved as "
            f"`{findings}` in the task folder:", "",
            "```json", FINDINGS_SHAPE, "```", ""]
    if files["has_prompt"]:
        out += ["## Prompt", "", "```text", files["prompt_text"].rstrip("\n"), "```", ""]
    else:
        out += _ask_section(files, records)
    services = sorted({r["service"] for r in records.values()})
    out += [f"# Injected records ({len(records)} records in {len(services)} services: {', '.join(services)})", ""]
    out += render_listing(records, marks)
    if removed:
        out += ["# Removed in this revision", ""]
        for e in removed:
            out += [f"- {e['id']} ({e['table']}): {e['text']}"]
        out.append("")
    text = "\n".join(out).rstrip("\n") + "\n"
    return {"text": text, "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "path": Path(task_dir) / REVIEW_DIR / f"brief_{reviewer}.md", "findings": findings,
            "records": len(records), "scope": "revision" if previous_sql else "full"}


# ---------------------------------------------------------------- candidates: quantifiers

def quantifier_spans(text: str) -> list:
    """Each quantifier that may define a population, with the sentence it sits in and its offsets."""
    spans = []
    idioms = [(i.start(), i.end()) for i in IDIOM_RX.finditer(text or "")]
    for m in QUANTIFIER_RX.finditer(text or ""):
        if any(a <= m.start() and m.end() <= b for a, b in idioms):
            continue                       # "at all", "we all", "any questions": no population
        start = max(text.rfind(ch, 0, m.start()) for ch in ".!?\n") + 1
        ends = [i for i in (text.find(ch, m.end()) for ch in ".!?\n") if i != -1]
        end = min(ends) + 1 if ends else len(text)
        sentence = " ".join(text[start:end].split())
        if BOILERPLATE_RX.search(sentence):
            continue
        spans.append({"quantifier": " ".join(m.group(0).split()), "start": m.start(), "end": m.end(),
                      "sentence": sentence})
    return spans


def _span_covers(entry_span: str, text: str, start: int, end: int) -> bool:
    """True when an open_sets span, found in the text, covers the quantifier at [start, end)."""
    needle = " ".join(str(entry_span or "").split()).casefold()
    if not needle:
        return False
    # match on a whitespace-normalised copy, keeping a map back to the original offsets
    norm, offsets, prev_space = [], [], True
    for i, ch in enumerate(text):
        if ch.isspace():
            if not prev_space:
                norm.append(" ")
                offsets.append(i)
            prev_space = True
        else:
            norm.append(ch.casefold())
            offsets.append(i)
            prev_space = False
    hay = "".join(norm)
    if len(hay) != len(offsets):          # a casefold that changes length: fall back to the plain test
        return needle in " ".join(text.split()).casefold()
    at = hay.find(needle)
    while at != -1:
        if offsets[at] <= start and offsets[at + len(needle) - 1] + 1 >= end:
            return True
        at = hay.find(needle, at + 1)
    return False


def _ask_records(files: dict, records: dict) -> list:
    """Injected records the manifest names as carrying the ask or a rule (anchors, ask fragments, authorities)."""
    manifest = files["manifest"] or {}
    index = rs.id_index(records)
    keys = []
    for group in ("anchors", "ask_fragments", "authorities"):
        for item in _list(manifest.get(group)):
            if not isinstance(item, dict):
                continue
            for rid in [item.get("locator"), *_list(item.get("seeded_ids"))]:
                for key in index.get(rid, []):
                    if key not in keys and records[key]["text"]:
                        keys.append(key)
    return sorted(keys)


def quantifier_candidates(files: dict, records: dict, sweep: dict | None) -> list:
    entries = [e for e in _list((sweep or {}).get("open_sets")) if isinstance(e, dict)]
    out = []
    sources = [("prompt", {"prompt"}, files["prompt_text"])] if files["has_prompt"] else []
    for key in _ask_records(files, records):
        rec = records[key]
        sources.append((rec["id"], {rec["id"], *rec["aliases"]}, rec["text"]))
    for where, names, text in sources:
        for span in quantifier_spans(text):
            covered = any(_span_covers(e.get("span"), text, span["start"], span["end"])
                          and str(e.get("where") or "prompt") in names for e in entries)
            out.append({"id": f"Q:{where}:{span['start']}", "where": where, "covered": covered, **span})
    return out


# ---------------------------------------------------------------- candidates: known-issue cards

def load_cards(universe: str) -> list:
    path = CARDS_DIR / f"{universe}.md"
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8")
    cards = []
    heads = list(re.finditer(r"^### ((?:NB|SC)-\d+)\s*[·\-:]\s*(.+)$", text, re.M))
    for i, m in enumerate(heads):
        body = text[m.end():heads[i + 1].start() if i + 1 < len(heads) else len(text)]
        field = lambda label: " ".join(re.findall(r"^- \*\*" + label + r":\*\*\s*(.+)$", body, re.M))  # noqa: E731
        card = {"id": m.group(1), "title": m.group(2).strip(), "dont_grade": field("Don't grade"),
                "why": field("Why"), "safer": field("Safer"), "watch": bool(field("Watch"))}
        card["terms"] = card_terms(card)
        cards.append(card)
    return cards


def _number(whole: str, frac: str | None, suffix: str | None) -> float:
    value = float(whole.replace(",", "") + (frac or ""))
    return value * {"k": 1e3, "m": 1e6}.get((suffix or "").lower(), 1)


def numbers_in(text: str) -> list:
    """(value, shown, has_dollar_or_separator) for each number written like an amount."""
    out = []
    for m in AMOUNT_RX.finditer(text or ""):
        dollar, whole, frac, suffix = m.groups()
        if not (dollar or "," in whole or frac or suffix):
            continue                       # a bare integer is not treated as an amount
        if suffix and not dollar and not frac and "," not in whole and suffix in "Mm":
            continue                       # "5m" is minutes more often than millions
        out.append((_number(whole, frac, suffix), m.group(0).strip()))
    return out


def card_terms(card: dict) -> dict:
    text = " ".join([card["title"], card["dont_grade"], card["why"]])
    ids = set(LINEAR_KEY_RX.findall(text))
    ids |= {f"#{n}" for n in re.findall(r"\bPRs?\s*#?(\d{1,5})\b", text)}
    ids |= set(re.findall(r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b", text))
    ids |= {w for w in re.findall(r"\b[A-Z]{7,}\b", text) if w not in ("FAILS",)}
    channels = set(re.findall(r"(?<![\w&])#[a-z][a-z0-9_-]{2,}", text))    # a place, not the issue: a weak term
    ids |= {c for c in re.findall(r"\b[CDG][A-Z0-9]{8,11}\b", text) if re.search(r"\d", c)}
    ids |= set(re.findall(r"\b[A-Z]{2,}\d{4,}\b|\b\d{7,}\b|\b\d+\.\d+\.\d+\b", text))
    strong, weak = set(), set()
    for value, _ in numbers_in(text):
        (strong if value >= 1000 and value % 1000 else weak).add(value)
    names = set()
    for m in NAME_RX.finditer(text):
        words = m.group(0).split()
        while words and words[0].casefold() in NAME_STOP:
            words = words[1:]
        while words and words[-1].casefold() in NAME_STOP:
            words = words[:-1]
        name = " ".join(words)
        if len(name) >= 4 and name not in ids and not re.fullmatch(r"[A-Z0-9_ ]+", name):
            names.add(name)
    return {"ids": sorted(ids), "names": sorted(names | channels), "strong_figures": sorted(strong),
            "weak_figures": sorted(weak)}


def _has_term(term: str, text: str, folded: str) -> bool:
    if term.startswith("#") and term[1:].isdigit():
        return re.search(r"(?:#|pull/)" + term[1:] + r"\b", text) is not None
    if term.startswith("#"):
        return re.search(re.escape(term) + r"(?![\w-])", text) is not None
    if " " in term:
        return re.search(r"(?<!\w)" + re.escape(term.casefold()) + r"(?!\w)", folded) is not None
    return re.search(r"(?<![\w-])" + re.escape(term) + r"(?![\w-])", text) is not None


def known_issue_candidates(cards: list, records: dict, prompt_text: str, manifest=None,
                           persona: str | None = None) -> list:
    """Cards the injected records, the prompt, the manifest or the persona touch.

    strong  a card id term (ticket, table, channel, PR, version) or a distinctive figure is in an injected record or
            the prompt; or a card id term or the card's own id (NB-14) is in the manifest, which names the base
            records the task reads; or the card names the persona (their own access, posts or claims)
    weak    two of the card's names, or one name of two or more words, in one injected record or the prompt
    `via` says which of records, prompt, manifest and persona carried the hit."""
    docs = [("prompt", prompt_text or "")]
    for key in sorted(records):
        rec = records[key]
        extra = " ".join([rec["id"], *rec["aliases"], *rec["refs"], str(rec["container"] or "")])
        docs.append((rec["id"], rec["text"] + "\n" + extra))
    prepared = [(where, text, text.casefold(), {v for v, _ in numbers_in(text)}) for where, text in docs if text.strip()]
    manifest_text = json.dumps(manifest, ensure_ascii=False, sort_keys=True) if manifest else ""
    first = str(persona or "").split()[0] if str(persona or "").split() else ""
    out = []
    for card in cards:
        terms = card["terms"]
        strong, weak = {}, {}
        for where, text, folded, numbers in prepared:
            hit_ids = [t for t in terms["ids"] if _has_term(t, text, folded)]
            hit_fig = [f for f in terms["strong_figures"] if any(abs(f - n) < 0.005 for n in numbers)]
            hit_names = [n for n in terms["names"] if _has_term(n, text, folded)]
            hit_weakfig = [f for f in terms["weak_figures"] if any(abs(f - n) < 0.005 for n in numbers)]
            if hit_ids or hit_fig:
                strong[where] = hit_ids + [f"{f:,.2f}".rstrip("0").rstrip(".") for f in hit_fig]
            elif len(hit_names) >= 2 or any(" " in n for n in hit_names) or (hit_names and hit_weakfig):
                weak[where] = hit_names
        via = {"prompt" if w == "prompt" else "records" for w in (strong or weak)}
        if manifest_text:
            in_manifest = [t for t in terms["ids"] if _has_term(t, manifest_text, manifest_text.casefold())]
            if re.search(r"(?<![\w-])" + re.escape(card["id"]) + r"(?![\w-])", manifest_text):
                in_manifest.append(card["id"])
            if in_manifest:
                strong["manifest"] = in_manifest
                via.add("manifest")
        if first and len(first) >= 3 and any(first in name.split() for name in terms["names"]):
            strong["persona"] = [first]
            via.add("persona")
        if strong or weak:
            level = "strong" if strong else "weak"
            hits = strong or weak
            out.append({"id": card["id"], "card": card["id"], "title": card["title"], "level": level,
                        "watch": card["watch"], "dont_grade": card["dont_grade"],
                        "terms": sorted({t for ts in hits.values() for t in ts}),
                        "where": sorted(hits)[:12], "where_count": len(hits), "via": sorted(via)})
    return out


# ---------------------------------------------------------------- candidates: value conflicts in injected text

def _person_tokens() -> set:
    data, _ = _load_json(ROSTER) if ROSTER.is_file() else (None, None)
    tokens = set()
    for p in _list((data or {}).get("personas")):
        tokens.update(str(p.get("name") or "").split())
    return tokens


def _sentences(rec: dict) -> list:
    f = rec["fields"]
    lines = []
    if rec["table"] == "linear.linear_issues" and f.get("state_id"):
        lines.append(f"{rec['id']} state {f['state_id']}")
    if rec["table"] == "trello.trello_check_items" and f.get("name") and f.get("state"):
        lines.append(f"{f['name']} | {f['state']}")
    lines += [s.strip() for s in SENTENCE_RX.split(rec["text"]) if s.strip()]
    return lines


STATUS_NOISE_RX = re.compile(r"<?https?://\S+>?|\bopen(?:s|ed|ing)?\s+(?:the|a|an|it|this|that|up|in)\b|"
                             r"\boutstanding\s+(?:shares?|stock|options?|option lines?|balance)\b|"
                             r"\b(?:shares?|options?|stock)\s+outstanding\b", re.I)


def _status_class(sentence: str) -> str | None:
    low = " " + STATUS_NOISE_RX.sub(" ", sentence).casefold() + " "
    negated = bool(NEGATION_RX.search(low))
    stripped = NEGATION_RX.sub(" ", low)
    found = set()
    for label, words in (("done", STATUS_DONE), ("open", STATUS_OPEN), ("cancelled", STATUS_CANCEL)):
        if any(re.search(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", stripped) for w in words):
            found.add(label)
    if negated:
        found.add("open")
    return next(iter(found)) if len(found) == 1 else None


def _record_year(rec: dict) -> tuple:
    m = re.match(r"(\d{4})-(\d{2})", str(rec["date"] or ""))
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def _digits(value: float) -> str:
    return "".join(sorted(f"{value:.2f}".replace(".", "").strip("0")))


def conflict_candidates(records: dict) -> list:
    """Mechanical value conflicts in the injected text. Each candidate: id, kind, entity, values with record ids.

    amount   one entity, two amounts in different services that are close (within AMOUNT_NEAR) or share digits
    status   one entity, done in one service and open or cancelled in another
    date     one entity, the same date word (due, effective, release ...) with different days in different services
    owner    one entity, two owners in different services
    weekday  a weekday written next to a date it does not fall on
    year     one day of the year written with two different years
    chronology  an injected reply or comment dated before the injected record it hangs on"""
    people = _person_tokens()
    sentences = []                                        # (record, sentence, ids, names)
    name_services = {}
    for key in sorted(records):
        rec = records[key]
        for sentence in _sentences(rec):
            ids = sorted(set(LINEAR_KEY_RX.findall(sentence)) | set(PR_ID_RX.findall(sentence)))
            names = set()
            for m in NAME_RX.finditer(sentence):
                words = [w for w in m.group(0).split()]
                while words and (words[0].casefold() in NAME_STOP or words[0] in people):
                    words = words[1:]
                while words and (words[-1].casefold() in NAME_STOP or words[-1] in people):
                    words = words[:-1]
                name = " ".join(words)
                if len(name) >= 4 and not LINEAR_KEY_RX.fullmatch(name) and not name.isupper():
                    names.add(name)
            for name in names:
                name_services.setdefault(name, set()).add(rec["service"])
            sentences.append((rec, sentence, ids, names))
    shared = {n for n, svcs in name_services.items() if len(svcs) >= 2}
    obs = {}                                              # (field, entity) -> [(norm, shown, record id, service)]
    out = []
    years = {}                                            # (month, day) -> {year: [record ids]}
    for rec, sentence, ids, names in sentences:
        entities = ids + sorted(n for n in names if n in shared)
        for m in DATE_RX.finditer(sentence):
            weekday, mon, day, year = m.group(1), m.group(2).lower()[:3], int(m.group(3)), m.group(4)
            month = MONTHS.index(mon) + 1
            if year:
                years.setdefault((month, day), {}).setdefault(int(year), set()).add(rec["id"])
            if weekday:
                rec_year, rec_month = _record_year(rec)
                options = [int(year)] if year else ([rec_year] if rec_year else [])
                if not year and rec_year and rec_month:
                    if month < rec_month - 6:
                        options.append(rec_year + 1)
                    if month > rec_month + 6:
                        options.append(rec_year - 1)
                good = False
                for y in options:
                    try:
                        good = good or calendar.weekday(y, month, day) == WEEKDAYS.index(weekday.lower()[:3])
                    except ValueError:
                        pass
                if options and not good:
                    out.append({"id": f"X:weekday:{rec['id']}:{m.group(0)}", "kind": "weekday", "entity": m.group(0),
                                "values": [{"value": f"{m.group(0)} is not a {weekday} in {options[0]}",
                                            "records": [rec["id"]], "services": [rec["service"]]}]})
        if len(entities) != 1:
            if " | " in sentence and len(ids) == 1:
                entities = ids                              # a sheet row: the ticket in it is the entity
            else:
                continue
        entity = entities[0]
        amounts = numbers_in(sentence)
        if 1 <= len(amounts) <= 2:
            for value, shown in amounts:
                obs.setdefault(("amount", entity), []).append((value, shown, rec["id"], rec["service"]))
        status = _status_class(sentence)
        if status:
            obs.setdefault(("status", entity), []).append((status, status, rec["id"], rec["service"]))
        dates = list(DATE_RX.finditer(sentence))
        roles = {r.lower()[:6] for r in DATE_ROLE_RX.findall(sentence)}
        if len(dates) == 1 and len(roles) == 1:
            d = dates[0]
            norm = f"{d.group(2).lower()[:3]} {int(d.group(3))}"
            obs.setdefault((f"date:{next(iter(roles))}", entity), []).append((norm, d.group(0), rec["id"], rec["service"]))
        for rx in OWNER_RX:
            for owner in rx.findall(sentence):
                if owner.casefold() not in NAME_STOP and owner != entity:
                    obs.setdefault(("owner", entity), []).append((owner, owner, rec["id"], rec["service"]))
    for (field, entity) in sorted(obs):
        rows = obs[(field, entity)]
        by_value = {}
        for norm, shown, rid, service in rows:
            slot = by_value.setdefault(norm, {"value": shown, "records": set(), "services": set()})
            slot["records"].add(rid)
            slot["services"].add(service)
        if len(by_value) < 2:
            continue
        keep = set()
        norms = sorted(by_value, key=str)
        for i, a in enumerate(norms):
            for b in norms[i + 1:]:
                if len(by_value[a]["services"] | by_value[b]["services"]) < 2:
                    continue                                # the same service on both sides: not cross-service
                if field == "amount":
                    near = abs(a - b) <= AMOUNT_NEAR * max(abs(a), abs(b))
                    if not (near or _digits(a) == _digits(b)):
                        continue
                keep.update([a, b])
        if keep:
            out.append({"id": f"X:{field}:{entity}", "kind": field.split(":")[0], "entity": entity,
                        "values": [{"value": by_value[n]["value"], "records": sorted(by_value[n]["records"]),
                                    "services": sorted(by_value[n]["services"])} for n in norms if n in keep]})
    for (month, day) in sorted(years):
        if len(years[(month, day)]) >= 2:
            label = f"{MONTHS[month - 1].title()} {day}"
            out.append({"id": f"X:year:{label}", "kind": "year", "entity": label,
                        "values": [{"value": f"{label}, {y}", "records": sorted(ids_), "services": []}
                                   for y, ids_ in sorted(years[(month, day)].items())]})
    out += chronology_candidates(records)
    return sorted(out, key=lambda c: c["id"])


CREATED_COLS = ("created_at", "created", "created_time", "submitted_at", "date")


def _created(rec: dict):
    """When an inserted record was made, as an aware UTC datetime, or None (update-only rows and unknown formats)."""
    if "insert" not in rec["ops"]:
        return None
    f = rec["fields"]
    if rec["table"] == "slack.slack_messages":
        try:
            return dt.datetime.fromtimestamp(float(f.get("ts")), tz=dt.timezone.utc)
        except (TypeError, ValueError, OverflowError, OSError):
            return None
    raw = rs._first(f, CREATED_COLS)
    if raw in (None, ""):
        return None
    raw = str(raw).strip()
    try:
        stamp = dt.datetime.fromisoformat(raw.replace("Z", "+00:00").replace(" ", "T", 1))
    except ValueError:
        import email.utils
        try:
            stamp = email.utils.parsedate_to_datetime(raw)
        except (TypeError, ValueError, IndexError):
            return None
    if stamp is None:
        return None
    return stamp if stamp.tzinfo else stamp.replace(tzinfo=dt.timezone.utc)


def chronology_candidates(records: dict) -> list:
    """An injected reply, comment or child dated before the injected record it hangs on (thread parent, issue, PR,
    replied-to mail). Records whose parent is in the base are not compared: the pre-pass reads injected rows only."""
    index = rs.id_index(records)
    out = []
    for key in sorted(records):
        rec = records[key]
        if not rec["parent"] or rec["parent"] in (rec["id"], *rec["aliases"]):
            continue
        child_at = _created(rec)
        if child_at is None:
            continue
        for pkey in index.get(str(rec["parent"]), []):
            parent = records[pkey]
            parent_at = _created(parent)
            if parent_at is not None and child_at < parent_at:
                out.append({"id": f"X:chronology:{rec['id']}", "kind": "chronology", "entity": rec["id"],
                            "values": [{"value": f"{rec['id']} at {child_at.strftime('%Y-%m-%dT%H:%M:%SZ')}",
                                        "records": [rec["id"]], "services": [rec["service"]]},
                                       {"value": f"is before its parent {parent['id']} at "
                                                 f"{parent_at.strftime('%Y-%m-%dT%H:%M:%SZ')}",
                                        "records": [parent["id"]], "services": [parent["service"]]}]})
                break
    return out


# ---------------------------------------------------------------- candidates: seeded facts and the base search

def fact_candidates(files: dict) -> list:
    """One per manifest fact: the terms to search the whole base for.

    The terms are the names and ticket or PR ids in the key and aliases (the entity the fact is about, e.g.
    "Leapblock"), each alias as written, and the value when it is short. A key of several words that is not itself a
    name ("returned wire rule", "the first one") is the author's label, not something a record says, so it is not
    searched."""
    out, seen = [], set()
    for fact in _list((files["manifest"] or {}).get("facts")):
        if not isinstance(fact, dict) or not fact.get("key") or fact["key"] in seen:
            continue
        seen.add(fact["key"])
        terms = []
        aliases = [str(a) for a in _list(fact.get("aliases")) if str(a).strip()]
        labels = [str(fact["key"]), *aliases]
        for label in labels + [str(fact.get("value") or "")]:
            for rid in LINEAR_KEY_RX.findall(label) + PR_ID_RX.findall(label):
                if rid not in terms:
                    terms.append(rid)
        for label in labels:
            for m in NAME_RX.finditer(label):
                words = [w for w in m.group(0).split() if w.casefold() not in NAME_STOP]
                name = " ".join(words)
                if len(name) >= 4 and name not in terms and not LINEAR_KEY_RX.fullmatch(name):
                    terms.append(name)
        key = " ".join(str(fact["key"]).split())
        for term in ([key] if NAME_RX.fullmatch(key) else []) + aliases:
            term = " ".join(term.split())
            if term in terms or len(term) < 3 or not re.search(r"[A-Za-z]", term):
                continue
            if " " not in term and re.search(r"[._]", term):
                continue                                   # a design label such as cw.first_window is not searchable
            terms.append(term)
        value = " ".join(str(fact.get("value") or "").split())
        if 3 <= len(value) <= FACT_VALUE_MAX and value not in terms:
            terms.append(value)
        out.append({"id": str(fact["key"]), "fact": str(fact["key"]), "value": fact.get("value"),
                    "kind": fact.get("kind"), "terms": terms, "home_ids": list(_list(fact.get("home_ids")))})
    return out


def base_requests(facts: list, services=BASE_SERVICES) -> dict:
    """service -> an hg.py `search search-many` request with one query per fact term."""
    queries, seen = [], {}
    for fact in facts:
        for term in fact["terms"]:
            if term.casefold() not in seen:
                seen[term.casefold()] = f"q{len(seen) + 1}"
                queries.append({"id": seen[term.casefold()], "query": term, "limit": BASE_SEARCH_LIMIT})
    if not queries:
        return {}
    out = {}
    for service in services:
        request = {"service": service, "queries": queries}
        if service in BASE_FILE:
            request["file"] = BASE_FILE[service]
        out[service] = request
    return out


def base_commands(task_dir, requests: dict) -> list:
    task = rs._rel(task_dir)
    return ["echo '" + json.dumps(requests[s], ensure_ascii=False).replace("'", "'\\''")
            + f"' | python3.12 -B Task_Authoring/tools/hg.py search search-many --request - --compact --task-dir {task}"
            for s in sorted(requests)]


def context_ready(files: dict) -> bool:
    ctx = files.get("context") or {}
    return ctx.get("spec_version") == "V3" and (ctx.get("source") or {}).get("status") == "ready"


def run_base(task_dir, facts: list, requests: dict) -> dict:
    """Run the base searches through tools/hg.py. Returns fact id -> {term: {service: count or 'N+'}} and errors."""
    term_id = {}
    for request in requests.values():
        for q in request["queries"]:
            term_id[q["query"].casefold()] = q["id"]
        break
    counts, errors = {}, []
    for service in sorted(requests):
        cmd = [sys.executable, "-B", str(HERE / "hg.py"), "search", "search-many", "--request", "-", "--compact",
               "--task-dir", str(Path(task_dir).resolve())]
        try:
            proc = subprocess.run(cmd, input=json.dumps(requests[service]), capture_output=True, text=True,
                                  cwd=str(WS), timeout=BASE_SEARCH_TIMEOUT_S)
        except (OSError, subprocess.SubprocessError) as exc:
            errors.append(f"{service}: {type(exc).__name__}: {str(exc)[:160]}")
            continue
        try:
            data = json.loads(proc.stdout)
            if not isinstance(data, dict):
                raise ValueError("not a JSON object")
        except ValueError:
            said = " ".join((proc.stderr or proc.stdout or "no output").split())[:200]
            errors.append(f"{service}: hg.py exit {proc.returncode}: {said}")
            continue
        for qid, result in (data.get("queries") or {}).items():
            n = len(_list(result.get("matches")))
            counts.setdefault(qid, {})[service] = f"{n}+" if not result.get("scan_complete", True) and n else n
    out = {}
    for fact in facts:
        out[fact["id"]] = {term: counts.get(term_id.get(term.casefold()), {}) for term in fact["terms"]}
    return {"facts": out, "errors": errors}


# ---------------------------------------------------------------- candidates: sibling families

def family_members(kind: str, rec: dict, records: dict) -> list:
    """Injected records of the same family as `rec` (not the record itself). same_template is not mechanical."""
    out = []
    for key in sorted(records):
        other = records[key]
        if key == rec["key"]:
            continue
        if kind == "same_author" and rec["author"] and other["author"] == rec["author"]:
            out.append(other)
        elif kind == "same_thread" and rec["thread"] and other["thread"] == rec["thread"]:
            out.append(other)
        elif kind == "same_service_type" and other["table"] == rec["table"]:
            out.append(other)
    return out


def _known(rid: str, index: dict) -> bool:
    return rid in index


def sibling_candidates(sweep: dict | None, records: dict) -> list:
    index = rs.id_index(records)
    out = []
    for n, defect in enumerate(_list((sweep or {}).get("siblings"))):
        if not isinstance(defect, dict):
            continue
        checked = set()
        for fam in _list(defect.get("families")):
            if isinstance(fam, dict):
                checked.update(str(i) for i in _list(fam.get("checked_ids")))
        for rid in _list(defect.get("record_ids")):
            for key in index.get(rid, []):
                rec = records[key]
                for kind in ("same_author", "same_thread", "same_service_type"):
                    missing = [m["id"] for m in family_members(kind, rec, records)
                               if not ({m["id"], *m["aliases"]} & checked) and m["id"] not in _list(defect.get("record_ids"))]
                    if missing:
                        out.append({"id": f"S:{defect.get('id') or n + 1}:{kind}:{rec['id']}",
                                    "defect": defect.get("id") or n + 1, "kind": kind, "record": rec["id"],
                                    "unchecked": missing})
    return out


# ---------------------------------------------------------------- candidates: all families

def load_sweep(files: dict) -> tuple:
    if not files["record"].is_file():
        return None, None
    data, error = _load_json(files["record"])
    if error:
        return None, error
    if not isinstance(data, dict):
        return None, f"{RECORD_NAME} must hold one JSON object"
    return data, None


def candidates(task_dir, universe: str | None = None) -> dict:
    """Every mechanical candidate, with whether the sweep record already covers it. Side-effect free."""
    files = task_files(task_dir)
    sweep, _ = load_sweep(files)
    records = rs.load_records(files["sql_text"])["records"]
    key = universe_of(files, sweep, universe)
    cards = load_cards(key) if key else []
    done_cards = {str(k.get("card")) for k in _list((sweep or {}).get("known_issues"))
                  if isinstance(k, dict) and str(k.get("disposition") or "").strip()}
    done_conf = {str(c.get("candidate")) for c in _list((sweep or {}).get("conflicts"))
                 if isinstance(c, dict) and str(c.get("disposition") or "").strip()}
    done_facts = {str(b.get("fact")) for b in _list((sweep or {}).get("base_consistency")) if isinstance(b, dict)}
    quantifiers = quantifier_candidates(files, records, sweep)
    known = known_issue_candidates(cards, records, files["prompt_text"], files["manifest"],
                                   (files["context"] or {}).get("persona_name")) if cards else []
    for k in known:
        k["covered"] = k["card"] in done_cards
    conflicts = conflict_candidates(records)
    for c in conflicts:
        c["covered"] = c["id"] in done_conf
    facts = fact_candidates(files)
    for f in facts:
        f["covered"] = f["fact"] in done_facts
    return {"universe": key, "cards_loaded": len(cards), "records": len(records),
            "quantifiers": quantifiers, "known_issues": known, "conflicts": conflicts, "facts": facts,
            "siblings": sibling_candidates(sweep, records),
            "counts": {"quantifiers_prompt": sum(1 for q in quantifiers if q["where"] == "prompt"),
                       "quantifiers_ask_records": sum(1 for q in quantifiers if q["where"] != "prompt"),
                       "known_issues_strong": sum(1 for k in known if k["level"] == "strong"),
                       "known_issues_weak": sum(1 for k in known if k["level"] == "weak"),
                       "conflicts": len(conflicts), "facts": len(facts)}}


def candidates_result(task_dir, universe: str | None = None, run_base_mode: str = "no") -> dict:
    """`candidates` as the contract's result object: verdict WARN while any candidate has no record entry.
    run_base_mode: yes (run the base searches), no, or auto (run them when the task has a ready V3 context)."""
    files = task_files(task_dir)
    found = candidates(task_dir, universe)
    requests = base_requests(found["facts"])
    run_it = run_base_mode == "yes" or (run_base_mode == "auto" and context_ready(files))
    base = run_base(task_dir, found["facts"], requests) if run_it and requests else None
    commands = [] if base and not base["errors"] else base_commands(task_dir, requests)
    bound = {SQL_NAME: files["sql_sha256"]}
    if files["has_prompt"]:
        bound[PROMPT_NAME] = files["prompt_sha256"]
    if files["record"].is_file():
        bound[_rel_task(task_dir, files["record"])] = sha256_file(files["record"])
    checks = []

    def add(cid, items, what, ok):
        checks.append({"id": cid, "status": "WARN" if items else "PASS",
                       "detail": f"{items} {what}" if items else ok})

    open_q = [q for q in found["quantifiers"] if not q["covered"]]
    add("candidates.quantifiers", len(open_q), f"quantifier span(s) without an open_sets entry "
        f"({sum(1 for q in open_q if q['where'] == 'prompt')} in the prompt)", "every quantifier span has an entry")
    add("candidates.conflicts", sum(1 for x in found["conflicts"] if not x["covered"]),
        "value or chronology conflict(s) between injected records without a disposition",
        f"{len(found['conflicts'])} conflict candidate(s), each with a disposition")
    strong = [k for k in found["known_issues"] if k["level"] == "strong" and not k["covered"]]
    weak = sum(1 for k in found["known_issues"] if k["level"] == "weak" and not k["covered"])
    add("candidates.known_issues", len(strong), f"known-issue card(s) touched by id, figure, manifest or persona "
        f"without a disposition (and {weak} touched by name only)",
        f"no strong known-issue card left ({weak} touched by name only)" if found["universe"] else
        "universe unknown: pass --universe to read the known-issue cards")
    if found["facts"]:
        add("candidates.facts", sum(1 for f in found["facts"] if not f["covered"]),
            "seeded fact(s) without a base_consistency entry", "every seeded fact has a base_consistency entry")
    else:
        checks.append({"id": "candidates.facts", "status": "SKIP", "detail": "the manifest declares no facts"})
    if base is None:
        checks.append({"id": "candidates.base", "status": "SKIP", "detail": "base searches not run" + (
            "" if requests else " (no searchable fact term)")})
    else:
        checks.append({"id": "candidates.base", "status": "WARN" if base["errors"] else "PASS",
                       "detail": ("; ".join(base["errors"])[:300]) if base["errors"] else
                       f"ran {sum(len(r['queries']) for r in requests.values())} base queries"})
    add("candidates.siblings", sum(len(x["unchecked"]) for x in found["siblings"]),
        "injected family member(s) of recorded defects not checked", "no unchecked family member")
    statuses = {c["status"] for c in checks}
    return {"tool": TOOL, "version": VERSION, "command": "candidates",
            "verdict": "WARN" if "WARN" in statuses else "PASS", "bound_to": dict(sorted(bound.items())),
            "checks": checks, **found, "base": base, "base_commands": commands}


def candidates_text(task_dir, result: dict) -> str:
    found, base, commands = result, result["base"], result["base_commands"]
    c = found["counts"]
    open_q = [q for q in found["quantifiers"] if not q["covered"]]
    out = [f"COHERENCE SWEEP (candidates): {result['verdict']}"]
    out += [f"[{x['status']}] {x['id']}: {x['detail']}" for x in result["checks"]]
    out.append(f"Totals: {c['quantifiers_prompt']} prompt quantifier spans, {c['quantifiers_ask_records']} in ask "
               f"records, {c['conflicts']} conflicts, {c['known_issues_strong']} strong and {c['known_issues_weak']} "
               f"weak known-issue cards, {c['facts']} seeded facts")
    out.append("Quantifier spans with no open_sets entry (prompt first, then the records that carry the ask)")
    grouped = {}
    for q in open_q:
        grouped.setdefault((q["where"] != "prompt", q["where"], q["sentence"]), []).append(q["quantifier"])
    last = None
    for (_, where, sentence), words in sorted(grouped.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        if where != last:
            out.append(f"  in {where}")
            last = where
        out.append("      " + ", ".join(f"\"{w}\"" for w in words) + f": {sentence[:220]}")
    if not open_q:
        out.append("  none")
    out.append("Value and chronology conflicts between injected records (give each a disposition under \"conflicts\")")
    for x in found["conflicts"]:
        if x["covered"]:
            continue
        out.append(f"  {x['id']}")
        out += [f"      {v['value']}: {', '.join(v['records'][:6])}" + (" ..." if len(v["records"]) > 6 else "")
                for v in x["values"]]
    if all(x["covered"] for x in found["conflicts"]):
        out.append("  none")
    out.append(f"Known-issue cards touched ({found['universe'] or 'universe unknown: pass --universe'}; "
               f"{found['cards_loaded']} cards read)")
    weak_by_terms = {}
    for k in found["known_issues"]:
        if k["covered"]:
            continue
        if k["level"] == "weak":
            weak_by_terms.setdefault(", ".join(k["terms"][:4]), []).append(k)
            continue
        out.append(f"  {k['card']} [strong via {'+'.join(k.get('via') or [])}{', watch' if k['watch'] else ''}] "
                   f"{k['title']}: {', '.join(k['terms'][:6])} in {k['where_count']} place(s), "
                   f"e.g. {', '.join(k['where'][:3])}")
    for terms, cards in sorted(weak_by_terms.items()):
        out.append(f"  weak, name only ({terms}): " + "; ".join(f"{k['card']} {k['title']}" for k in cards))
    if all(k["covered"] for k in found["known_issues"]):
        out.append("  none")
    out.append("Seeded facts to check against the whole base (record each under \"base_consistency\")")
    for f in found["facts"]:
        line = f"  {f['fact']} = {str(f['value'])[:60]}  search: {' | '.join(f['terms']) or '(no searchable term)'}"
        if base and f["id"] in base["facts"]:
            hits = []
            for term, per in base["facts"][f["id"]].items():
                shown = ", ".join(f"{s} {n}" for s, n in sorted(per.items()) if n not in (0, "0"))
                hits.append(f"\"{term}\": {shown or 'no base hit'}")
            line += "\n      base hits: " + "; ".join(hits)
        out.append(line + ("  [recorded]" if f["covered"] else ""))
    if not found["facts"]:
        out.append("  none (no manifest facts)")
    if base and base["errors"]:
        out += ["  base search errors: " + "; ".join(base["errors"])]
    if commands:
        n_terms = len({t.casefold() for f in found["facts"] for t in f["terms"]})
        out.append(f"Base searches not run: {n_terms} term(s) over {len(commands)} service(s). Run them with "
                   f"`coherence_sweep.py candidates --task-dir {rs._rel(task_dir)} --run-base yes` (needs a ready V3 "
                   "task context); --json lists one hg.py command per service under base_commands")
    out.append("Family members of recorded defects not yet checked")
    out += [f"  defect {s['defect']} {s['kind']} of {s['record']}: {', '.join(s['unchecked'][:8])}"
            + (f" (+{len(s['unchecked']) - 8} more)" if len(s["unchecked"]) > 8 else "")
            for s in found["siblings"]] or ["  none"]
    return "\n".join(out)


# ---------------------------------------------------------------- check

def _text(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _ids(value) -> list:
    return [str(v) for v in value if str(v).strip()] if isinstance(value, list) else []


def _check(checks: list, check_id: str, problems: list, ok: str, warn: bool = False) -> None:
    if problems:
        shown = "; ".join(problems[:4]) + (f"; and {len(problems) - 4} more" if len(problems) > 4 else "")
        checks.append({"id": check_id, "status": "WARN" if warn else "FAIL", "detail": shown})
    else:
        checks.append({"id": check_id, "status": "PASS", "detail": ok})


def _chain_problems(task_dir, sweep: dict) -> list:
    """Follow previous_sweep links back to a full sweep; every link is checked by sha256."""
    problems, current, seen = [], sweep, set()
    for _ in range(CHAIN_MAX):
        if current.get("scope") == "full":
            return problems
        link = current.get("previous_sweep")
        if not isinstance(link, dict) or not _text(link.get("path")) or not _text(link.get("sha256")):
            return problems + ["a revision sweep must name previous_sweep {path, sha256}"]
        path = (Path(task_dir) / link["path"]).resolve()
        try:
            path.relative_to(Path(task_dir).resolve())
        except ValueError:
            return problems + [f"previous_sweep path {link['path']} is outside the task folder"]
        if not path.is_file():
            return problems + [f"previous sweep {link['path']} not found (store each revision's sweep next to its SQL)"]
        if sha256_file(path) != link["sha256"]:
            return problems + [f"previous sweep {link['path']} has changed since it was recorded"]
        if str(path) in seen:
            return problems + ["the previous_sweep chain loops"]
        seen.add(str(path))
        previous, error = _load_json(path)
        if error or not isinstance(previous, dict):
            return problems + [error or f"{link['path']} is not a sweep record"]
        if (previous.get("bound_to") or {}).get(SQL_NAME) != current.get("previous_sql_sha256"):
            return problems + [f"{link['path']} is not the sweep of the previous SQL "
                               f"({str(current.get('previous_sql_sha256'))[:12]})"]
        current = previous
    return problems + [f"no full sweep within {CHAIN_MAX} links"]


def _brief_header(text: str) -> dict:
    out = {}
    m = re.search(r"^Bound to: " + re.escape(SQL_NAME) + r" sha256 ([0-9a-f]{64}); " + re.escape(PROMPT_NAME)
                  + r" (?:sha256 ([0-9a-f]{64})|not written yet)$", text, re.M)
    if m:
        out["sql"], out["prompt"] = m.group(1), m.group(2)
    m = re.search(r"^Scope: (full|revision)(?: \(previous SQL sha256 ([0-9a-f]{64})\))?$", text, re.M)
    if m:
        out["scope"], out["previous"] = m.group(1), m.group(2)
    return out


def evaluate(task_dir, previous_sql=None, universe: str | None = None) -> dict:
    """Check the sweep record against the current files. Side-effect free; returns the contract's result object.

    Never raises for a missing or unreadable input (the gate calls this in-process): that is a FAIL result whose
    sweep.bound check names the input."""
    try:
        return _evaluate(task_dir, previous_sql, universe)
    except (UsageError, rs.UsageError) as exc:
        return {"tool": TOOL, "version": VERSION, "verdict": "FAIL", "bound_to": {}, "scope": "none",
                "checks": [{"id": "sweep.bound", "status": "FAIL", "detail": f"{exc}: the sweep cannot be checked"}]}


def _evaluate(task_dir, previous_sql=None, universe: str | None = None) -> dict:
    files = task_files(task_dir)
    task_dir = files["task_dir"]
    bound = {SQL_NAME: files["sql_sha256"]}
    if files["has_prompt"]:
        bound[PROMPT_NAME] = files["prompt_sha256"]
    checks = []

    def result(scope: str, **extra) -> dict:
        statuses = {c["status"] for c in checks}
        verdict = "FAIL" if "FAIL" in statuses else ("WARN" if "WARN" in statuses else "PASS")
        return {"tool": TOOL, "version": VERSION, "verdict": verdict, "bound_to": dict(sorted(bound.items())),
                "checks": checks, "scope": scope, **extra}

    sweep, error = load_sweep(files)
    if sweep is None:
        checks.append({"id": "sweep.bound", "status": "FAIL",
                       "detail": error or f"no {_rel_task(task_dir, files['record'])}: run `template`, give two cold "
                       "reviewers the output of `brief`, and record what they found and how it was settled"})
        return result("none")
    bound[_rel_task(task_dir, files["record"])] = sha256_file(files["record"])
    scope = sweep.get("scope")
    records = rs.load_records(files["sql_text"])["records"]
    index = rs.id_index(records)

    # ---- sweep.bound
    problems = []
    if sweep.get("schema") != SCHEMA:
        problems.append(f"schema is {sweep.get('schema')!r}, expected {SCHEMA}")
    if scope not in ("full", "revision"):
        problems.append("scope must be full or revision")
    recorded = sweep.get("bound_to") if isinstance(sweep.get("bound_to"), dict) else {}
    if recorded.get(SQL_NAME) != files["sql_sha256"]:
        problems.append(f"the record is bound to another {SQL_NAME} ({str(recorded.get(SQL_NAME))[:12]}, current "
                        f"{files['sql_sha256'][:12]}): sweep the current bytes again")
    if files["has_prompt"] and recorded.get(PROMPT_NAME) != files["prompt_sha256"]:
        problems.append(f"the record is bound to another {PROMPT_NAME} ({str(recorded.get(PROMPT_NAME))[:12]}, "
                        f"current {files['prompt_sha256'][:12]})")
    if not files["has_prompt"] and recorded.get(PROMPT_NAME):
        problems.append(f"the record names a {PROMPT_NAME} hash but no prompt exists")
    for field in RECORD_LISTS:
        if field in sweep and not isinstance(sweep[field], list):
            problems.append(f"\"{field}\" must be a list (it is read as empty)")
    _check(checks, "sweep.bound", problems, f"bound to {SQL_NAME} {files['sql_sha256'][:12]}"
           + (f" and {PROMPT_NAME} {files['prompt_sha256'][:12]}" if files["has_prompt"] else " (no prompt yet)"))
    if scope not in ("full", "revision"):
        return result("none")

    # ---- sweep.chain (revision scope)
    in_scope, changed_ids, changed_all, diff = None, set(), set(), None
    if scope == "revision":
        problems = []
        prev_sha = sweep.get("previous_sql_sha256")
        prev_path = Path(previous_sql) if previous_sql else (_find_previous_sql(task_dir, prev_sha) if _text(prev_sha) else None)
        if not _text(prev_sha):
            problems.append("a revision sweep must name previous_sql_sha256")
        elif prev_path is None or not prev_path.is_file():
            problems.append(f"no stored SQL with sha256 {prev_sha[:12]} under Working_Files/run_forensics/ "
                            "(or pass --previous)")
        elif sha256_file(prev_path) != prev_sha:
            problems.append(f"--previous has sha256 {sha256_file(prev_path)[:12]}, the record names {prev_sha[:12]}")
        else:
            diff = rs.diff_files(prev_path, files["sql"])
            in_scope = rs.scope_ids(diff)
            for e in diff["entries"]:
                if e["state"] != "removed":
                    changed_ids.add(e["id"])
                    changed_all.update([e["id"], *e["aliases"]])
            listed = set(_ids(sweep.get("changed_record_ids")))
            missing = sorted(i for i in changed_ids
                             if not ({i, *records[next(k for k in index[i])]["aliases"]} & listed))
            if missing:
                problems.append(f"changed_record_ids misses {len(missing)} record(s) this revision changed: "
                                + ", ".join(missing[:5]))
        problems += _chain_problems(task_dir, sweep)
        _check(checks, "sweep.chain", problems, f"chains to a full sweep; {len(changed_ids)} changed record(s) and "
               f"{len(in_scope or []) - len(changed_ids)} neighbour id(s) in scope")

    def touches_scope(ids: list) -> bool:
        return in_scope is None or not ids or bool(set(ids) & in_scope)

    # ---- sweep.reviewers
    problems, notes, seen_ids, reviewers = [], [], set(), []
    listed = [r for r in _list(sweep.get("reviewers")) if isinstance(r, dict)]
    for r in listed:
        rid = str(r.get("id") or "").strip()
        if not rid or rid in seen_ids:
            problems.append(f"reviewer id {rid!r} is missing or repeated")
            continue
        seen_ids.add(rid)
        if not _text(r.get("model")):
            problems.append(f"reviewer {rid}: no model")
        sha = str(r.get("brief_sha256") or "")
        if not re.fullmatch(r"[0-9a-f]{64}", sha):
            problems.append(f"reviewer {rid}: no brief_sha256")
        findings = (task_dir / str(r.get("findings"))) if _text(r.get("findings")) else None
        if findings is None or not findings.is_file():
            problems.append(f"reviewer {rid}: findings file {r.get('findings')!r} not found")
        else:
            reviewers.append((rid, findings))
        brief = task_dir / (str(r.get("brief")) if _text(r.get("brief")) else (REVIEW_DIR / f"brief_{rid}.md"))
        if not brief.is_file():
            notes.append(f"reviewer {rid}: the brief file is not kept, so what it was given cannot be confirmed")
        elif sha and sha256_file(brief) != sha:
            problems.append(f"reviewer {rid}: {brief.name} does not have the recorded hash")
        else:
            head = _brief_header(brief.read_text(encoding="utf-8", errors="replace"))
            if head.get("sql") != files["sql_sha256"] or head.get("prompt") != files["prompt_sha256"]:
                problems.append(f"reviewer {rid}: its brief was built from other SQL or prompt bytes")
            if head.get("scope") != scope:
                problems.append(f"reviewer {rid}: its brief has scope {head.get('scope')}, the record says {scope}")
            elif scope == "revision" and head.get("previous") != sweep.get("previous_sql_sha256"):
                problems.append(f"reviewer {rid}: its brief compares against another previous SQL")
    if len(seen_ids) < MIN_REVIEWERS:
        problems.insert(0, f"{len(seen_ids)} reviewer(s) recorded, at least {MIN_REVIEWERS} are needed")
    if problems or not notes:
        _check(checks, "sweep.reviewers", problems, f"{len(seen_ids)} reviewers, each with a model, a brief hash "
               "that matches its kept brief, and a findings file")
    else:
        _check(checks, "sweep.reviewers", notes, "", warn=True)

    # ---- sweep.findings
    forks = [f for f in _list(sweep.get("forks")) if isinstance(f, dict)]
    defects = [d for d in _list(sweep.get("siblings")) if isinstance(d, dict)]
    open_sets = [o for o in _list(sweep.get("open_sets")) if isinstance(o, dict)]
    taken = set()
    for item in forks + defects + open_sets:
        taken.update(_ids(item.get("sources")))
    dismissed = {str(d.get("source")) for d in _list(sweep.get("dismissed"))
                 if isinstance(d, dict) and _text(d.get("reason"))}
    problems, n_findings = [], 0
    for rid, path in reviewers:
        data, error = _load_json(path)
        if error or not isinstance(data, dict):
            problems.append(f"reviewer {rid}: {error or 'the findings file must hold one JSON object'}")
            continue
        for kind in FINDING_KINDS:
            items = data.get(kind)
            if not isinstance(items, list):
                problems.append(f"reviewer {rid}: findings have no \"{kind}\" list")
                continue
            for n, item in enumerate(items):
                fid = str(item.get("id") or "").strip() if isinstance(item, dict) else ""
                if not fid:
                    problems.append(f"reviewer {rid}: {kind}[{n}] has no id")
                    continue
                n_findings += 1
                if f"{rid}:{fid}" not in taken and f"{rid}:{fid}" not in dismissed:
                    problems.append(f"finding {rid}:{fid} ({kind}) is not taken up by a fork, defect or open set "
                                    "and not dismissed with a reason")
    _check(checks, "sweep.findings", problems, f"all {n_findings} reviewer finding(s) are taken up or dismissed")

    # ---- sweep.forks and sweep.prompt_sentences
    problems, by_status, carried, sentences = [], {}, 0, []
    prompt_norm = " ".join(files["prompt_text"].split()).casefold()
    for n, fork in enumerate(forks):
        fid = str(fork.get("id") or f"#{n + 1}")
        status, material = fork.get("status"), fork.get("material")
        ids = _ids(fork.get("record_ids"))
        if status not in FORK_STATUSES or not isinstance(material, bool):
            problems.append(f"fork {fid}: status must be one of {', '.join(FORK_STATUSES)} and material true or false")
            continue
        if material and status == "open":
            problems.append(f"fork {fid} is material and still open: settle it in the data")
        settled = fork.get("settled") if isinstance(fork.get("settled"), dict) else {}
        if status == "settled_in_data":
            named = _ids(settled.get("record_ids"))
            gone = [i for i in named if i not in index]
            if not named or not _text(settled.get("sql_revision")):
                problems.append(f"fork {fid}: settled_in_data must name settled.record_ids and settled.sql_revision")
            elif gone:
                problems.append(f"fork {fid}: settling record(s) not in the current SQL: {', '.join(gone[:3])}")
            elif set(named) & changed_all and fork.get("rechecked_sql_sha256") != files["sql_sha256"]:
                problems.append(f"fork {fid}: its settling record changed in this revision; re-read it and set "
                                "rechecked_sql_sha256 to the current SQL hash")
        if not touches_scope(ids + _ids(settled.get("record_ids"))):
            carried += 1
            by_status[status] = by_status.get(status, 0) + 1
            continue
        if not _text(fork.get("span")) and not ids:
            problems.append(f"fork {fid}: give the prompt span or the record ids")
        for side in ("reading_a", "reading_b"):
            reading = fork.get(side) if isinstance(fork.get(side), dict) else {}
            if not _text(reading.get("reading")) or not _text(reading.get("outcome")):
                problems.append(f"fork {fid}: {side} needs a reading and the outcome it leads to")
        if not _text(fork.get("reason")):
            problems.append(f"fork {fid}: say why it is{'' if material else ' not'} material")
        if status == "both_fair":
            both = fork.get("both_fair") if isinstance(fork.get("both_fair"), dict) else {}
            if not _text(str(both.get("figure_a") or "")) or not _text(str(both.get("figure_b") or "")):
                problems.append(f"fork {fid}: both_fair must give figure_a and figure_b")
            elif both.get("rubric_accepts_both") is not True:
                problems.append(f"fork {fid}: both_fair must say rubric_accepts_both: true")
        if status == "prompt_sentence":
            added = fork.get("prompt_sentence") if isinstance(fork.get("prompt_sentence"), dict) else {}
            if not _text(added.get("sentence")) or not _text(added.get("reason")):
                problems.append(f"fork {fid}: prompt_sentence needs the sentence and a written reason")
            else:
                if files["has_prompt"] and " ".join(added["sentence"].split()).casefold() not in prompt_norm:
                    problems.append(f"fork {fid}: the settling sentence is not in the current prompt")
                sentences.append(f"{fid} (\"{' '.join(added['sentence'].split())[:80]}\")")
        by_status[status] = by_status.get(status, 0) + 1
    summary = ", ".join(f"{by_status[s]} {s}" for s in FORK_STATUSES if by_status.get(s)) or "none recorded"
    _check(checks, "sweep.forks", problems, f"{len(forks)} fork(s): {summary}; no material fork is open"
           + (f"; {carried} carried from the earlier sweep" if carried else ""))
    if sentences:
        checks.append({"id": "sweep.prompt_sentences", "status": "WARN",
                       "detail": f"{len(sentences)} fork(s) settled by adding a prompt sentence: " + ", ".join(sentences)
                       + ". Such sentences have leaked answers and opened new forks: settle in the data when you can"})
    else:
        checks.append({"id": "sweep.prompt_sentences", "status": "PASS",
                       "detail": "no fork was settled by adding a prompt sentence"})

    # ---- sweep.open_sets
    problems, notes, n_spans = [], [], 0
    for q in quantifier_candidates(files, records, sweep):
        if q["where"] == "prompt":
            n_spans += 1
        if not q["covered"]:
            line = f"\"{q['quantifier']}\" in {q['where']} has no open_sets entry ({q['sentence'][:70]})"
            (problems if q["where"] == "prompt" else notes).append(line)
    for n, entry in enumerate(open_sets):
        label = f"open set \"{str(entry.get('span'))[:40]}\""
        where = str(entry.get("where") or "prompt")
        source = files["prompt_text"] if where == "prompt" else "\n".join(records[k]["text"] for k in index.get(where, []))
        if not _text(entry.get("span")):
            problems.append(f"open_sets[{n}] has no span")
            continue
        if source and " ".join(entry["span"].split()).casefold() not in " ".join(source.split()).casefold():
            problems.append(f"{label} is not in the current {where}")
            continue
        if _text(entry.get("not_a_population")):
            continue
        census = entry.get("census") if isinstance(entry.get("census"), dict) else {}
        ids, base_ids = _ids(census.get("ids")), _ids(census.get("base_ids"))
        if not _text(entry.get("rule")):
            problems.append(f"{label}: write the membership rule (or not_a_population with a reason)")
        if not ids and not base_ids:
            problems.append(f"{label}: the census is empty; list every member from the universe")
            continue
        if census.get("count") != len(ids) + len(base_ids):
            problems.append(f"{label}: census.count is {census.get('count')!r}, the lists hold {len(ids) + len(base_ids)}")
        gone = [i for i in ids if i not in index]
        if gone:
            problems.append(f"{label}: census id(s) not in the current SQL (move base records to base_ids): "
                            + ", ".join(gone[:3]))
    if problems or not notes:
        _check(checks, "sweep.open_sets", problems, f"{n_spans} quantifier span(s) in the prompt, each with a rule "
               f"and a census; {len(open_sets)} open set(s) recorded" if files["has_prompt"] else
               f"no prompt yet; {len(open_sets)} open set(s) recorded")
    else:
        _check(checks, "sweep.open_sets", [f"{len(notes)} quantifier span(s) in records that carry the ask have no "
                                           "entry: " + "; ".join(notes[:3])], "", warn=True)

    # ---- sweep.siblings
    problems, carried = [], 0
    for n, defect in enumerate(defects):
        did = str(defect.get("id") or f"#{n + 1}")
        ids = _ids(defect.get("record_ids"))
        status = defect.get("status")
        if status not in DEFECT_STATUSES:
            problems.append(f"defect {did}: status must be one of {', '.join(DEFECT_STATUSES)}")
        elif status == "open":
            problems.append(f"defect {did} is still open")
        if not touches_scope(ids):
            carried += 1
            continue
        if not _text(defect.get("defect")) or not ids:
            problems.append(f"defect {did}: describe the defect and name its record_ids")
        fix = defect.get("fix") if isinstance(defect.get("fix"), dict) else {}
        if status == "fixed_in_data" and (not _ids(fix.get("record_ids")) or not _text(fix.get("sql_revision"))):
            problems.append(f"defect {did}: fixed_in_data must name fix.record_ids and fix.sql_revision")
        if status == "fixed_in_data" and [i for i in _ids(fix.get("record_ids")) if i not in index]:
            problems.append(f"defect {did}: a fix record is not in the current SQL")
        if status == "not_a_defect" and not _text(defect.get("reason")):
            problems.append(f"defect {did}: not_a_defect needs a reason")
        if status == "known_issue" and not _text(defect.get("card")):
            problems.append(f"defect {did}: known_issue must name the card")
        families = [f for f in _list(defect.get("families")) if isinstance(f, dict)]
        listed_kinds = {fam.get("kind") for fam in families if isinstance(fam.get("kind"), str)}
        absent = [k for k in FAMILY_KINDS if k not in listed_kinds]
        if absent:
            problems.append(f"defect {did}: no sibling list for {', '.join(absent)} (each family gets the ids "
                            "checked, or `none` with a reason)")
        for fam in families:
            kind, checked = fam.get("kind"), set(_ids(fam.get("checked_ids")))
            if kind not in FAMILY_KINDS:
                problems.append(f"defect {did}: family kind must be one of {', '.join(FAMILY_KINDS)}")
                continue
            if not checked and not _text(fam.get("none")):
                problems.append(f"defect {did}: family {kind} lists no checked ids (or `none` with a reason)")
                continue
            if kind == "same_template":
                continue
            missing = set()
            for rid in ids:
                for key in index.get(rid, []):
                    for member in family_members(kind, records[key], records):
                        if not ({member["id"], *member["aliases"]} & checked) and member["id"] not in ids:
                            missing.add(member["id"])
            if missing:
                problems.append(f"defect {did}: family {kind} has {len(missing)} injected record(s) not checked: "
                                + ", ".join(sorted(missing)[:4]))
    _check(checks, "sweep.siblings", problems, f"{len(defects)} defect(s), each closed and with its sibling list"
           + (f"; {carried} carried from the earlier sweep" if carried else ""))

    # ---- sweep.base
    facts = fact_candidates(files)
    entries = {str(b.get("fact")): b for b in _list(sweep.get("base_consistency")) if isinstance(b, dict)}
    problems = []
    for fact in facts:
        entry = entries.get(fact["fact"])
        if entry is None:
            problems.append(f"fact \"{fact['fact']}\" has no base_consistency entry")
            continue
    for name, entry in entries.items():
        count = entry.get("result_count")
        conflicts = [c for c in _list(entry.get("conflicts")) if isinstance(c, dict)]
        if not entry.get("search") or not isinstance(count, int) or isinstance(count, bool) or count < 0:
            problems.append(f"fact \"{name}\": record the search used and its result_count")
        elif any(not _text(c.get("id")) or not _text(c.get("disposition")) for c in conflicts):
            problems.append(f"fact \"{name}\": every conflicting hit needs an id and a disposition")
        elif count > 0 and not conflicts and not _text(entry.get("disposition")):
            problems.append(f"fact \"{name}\": {count} base hit(s) and no disposition (say why none conflicts)")
    if not facts and not entries:
        checks.append({"id": "sweep.base", "status": "SKIP",
                       "detail": "the manifest declares no facts and the record holds no base check"})
    else:
        _check(checks, "sweep.base", problems, f"{len(facts)} seeded fact(s) checked against the base, every "
               "conflicting hit dispositioned")

    # ---- sweep.known_issues
    key = universe_of(files, sweep, universe)
    cards = load_cards(key) if key else []
    done = {str(k.get("card")) for k in _list(sweep.get("known_issues"))
            if isinstance(k, dict) and _text(k.get("disposition"))}
    if not key or not cards:
        checks.append({"id": "sweep.known_issues", "status": "WARN",
                       "detail": "known-issue cards were not checked: the universe is not known (no task context and "
                       "no \"universe\" in the record); pass --universe normal|synthcut"
                       if not key else f"known-issue cards were not checked: no cards found for the {key} universe"})
    else:
        touched = known_issue_candidates(cards, records, files["prompt_text"], files["manifest"],
                                         (files["context"] or {}).get("persona_name"))
        strong = [k for k in touched if k["level"] == "strong" and k["card"] not in done]
        weak = [k for k in touched if k["level"] == "weak" and k["card"] not in done]
        problems = [f"{k['card']} ({k['title']}; {', '.join(k['terms'][:3])}) has no disposition" for k in strong]
        if problems or not weak:
            _check(checks, "sweep.known_issues", problems, f"{len(touched)} known-issue card(s) touched, each with a "
                   "disposition")
        else:
            _check(checks, "sweep.known_issues", [f"{len(weak)} card(s) touched by name only have no disposition: "
                                                  + ", ".join(k["card"] for k in weak[:10])
                                                  + (" ..." if len(weak) > 10 else "")], "", warn=True)

    # ---- sweep.conflicts (advisory)
    done = {str(c.get("candidate")) for c in _list(sweep.get("conflicts"))
            if isinstance(c, dict) and _text(c.get("disposition"))}
    found = conflict_candidates(records)
    if in_scope is not None:
        found = [c for c in found if any(set(v["records"]) & in_scope for v in c["values"])]
    left = [c["id"] for c in found if c["id"] not in done]
    _check(checks, "sweep.conflicts", [f"{len(left)} value conflict(s) from `candidates` have no disposition: "
                                       + ", ".join(left[:5])] if left else [],
           f"{len(found)} value conflict candidate(s), each with a disposition", warn=True)
    return result(scope, counts={"forks": len(forks), "defects": len(defects), "open_sets": len(open_sets),
                                 "reviewers": len(seen_ids)})


def to_text(result: dict) -> str:
    lines = [f"COHERENCE SWEEP ({result['scope']}): {result['verdict']}"]
    lines += [f"[{c['status']}] {c['id']}: {c['detail']}" for c in result["checks"]]
    return "\n".join(lines)


# ---------------------------------------------------------------- template

def template(task_dir, previous_sql=None, universe: str | None = None) -> dict:
    """A starting record for the author: hashes, scope and one empty entry per mechanical candidate."""
    files = task_files(task_dir)
    found = candidates(task_dir, universe)
    record = {"schema": SCHEMA, "bound_to": {SQL_NAME: files["sql_sha256"]}, "scope": "full"}
    if files["has_prompt"]:
        record["bound_to"][PROMPT_NAME] = files["prompt_sha256"]
    if previous_sql:
        diff = rs.diff_files(previous_sql, files["sql"])
        record.update({"scope": "revision", "previous_sql_sha256": sha256_file(previous_sql),
                       "changed_record_ids": sorted({e["id"] for e in diff["entries"] if e["state"] != "removed"}),
                       "previous_sweep": {"path": "Working_Files/run_forensics/<rev>/" + RECORD_NAME, "sha256": ""}})
    if found["universe"]:
        record["universe"] = found["universe"]
    record["reviewers"] = [{"id": str(n), "model": "", "brief_sha256": "",
                            "findings": (REVIEW_DIR / f"findings_{n}.json").as_posix()} for n in (1, 2)]
    record["forks"] = []
    record["open_sets"], seen = [], set()
    for q in found["quantifiers"]:
        if not q["covered"] and (q["where"], q["sentence"]) not in seen:
            seen.add((q["where"], q["sentence"]))
            record["open_sets"].append({"span": q["sentence"], "where": q["where"], "rule": "",
                                        "census": {"count": 0, "ids": [], "base_ids": []}})
    record["siblings"] = []
    record["base_consistency"] = [{"fact": f["fact"], "search": " | ".join(f["terms"]), "result_count": None,
                                   "conflicts": [], "disposition": ""} for f in found["facts"]]
    record["known_issues"] = [{"card": k["card"], "disposition": ""} for k in found["known_issues"]
                              if k["level"] == "strong"]
    record["conflicts"] = [{"candidate": c["id"], "disposition": ""} for c in found["conflicts"]]
    record["dismissed"] = []
    return record


# ---------------------------------------------------------------- self-test

def _fixture_task(root) -> dict:
    """A small task folder for the self-test and the unit tests: SQL, prompt, manifest and a rubric file."""
    sha = lambda s: hashlib.sha256(s.encode()).hexdigest()[:32]  # noqa: E731
    parent, reply, dm = "C0123ABCD|1770000000.000100", "C0123ABCD|1770000300.000200", "D0BRIAN01|1770009000.000300"
    sql = "\n".join([
        "-- Are you planning to inject? Yes", "-- design note: T1 is the decoy (never shown to a reviewer)", "BEGIN;",
        "INSERT INTO slack.slack_messages (id, channel_id, ts, user_id, text, thread_ts_legacy, thread_parent_id, "
        f"reply_count) VALUES ('{sha(parent)}', 'C0123ABCD', '1770000000.000100', 'U_ARTHUR', "
        "'Can you move every open bug into Linear? ENG-900 is done. Helpshift renewal is $1,500, due Feb 20.', "
        "'1770000000.000100', NULL, 1);",
        "INSERT INTO slack.slack_messages (id, channel_id, ts, user_id, text, thread_ts_legacy, thread_parent_id, "
        f"reply_count) VALUES ('{sha(reply)}', 'C0123ABCD', '1770000300.000200', 'U_BRIAN', 'ok, on it', "
        f"'1770000000.000100', '{sha(parent)}', 0);",
        "INSERT INTO slack.slack_messages (id, channel_id, ts, user_id, text, thread_ts_legacy, thread_parent_id, "
        f"reply_count) VALUES ('{sha(dm)}', 'D0BRIAN01', '1770009000.000300', 'U_BRIAN', "
        "'The Tavern popup is back on Fri Feb 12, see the ENG-2403 checklist', NULL, NULL, 0);",
        "INSERT INTO linear.linear_comments (id, issue_id, author_id, body, created_at) VALUES ('comment_a1', "
        "'ENG-900', 'usr_1', 'ENG-900 is still broken on Android. Helpshift renewal is $1,800, due Feb 27.', "
        "'2026-02-10T10:00:00Z');",
        "UPDATE linear.linear_issues SET updated_at = '2026-02-10T10:00:00Z' WHERE id = 'ENG-900';",
        "COMMIT;"]) + "\n"
    prompt = "Arthur asked me to tidy the bug list. Can you move every open bug into Linear and tell him when done?\n"
    manifest = {"anchors": [{"id": "A1", "prompt_reference": "Arthur's ask", "locator": sha(parent)}],
                "ask_fragments": [{"id": "K1", "locator": sha(parent), "seeded_ids": [sha(parent)], "kind": "exclusion",
                                   "delegation_quote": "SECRET-QUOTE", "requirement_ids": ["R1"]}],
                "traps": [{"id": "T1", "expected_wrong_reading": "SECRET-WRONG-READING", "resolver": "SECRET-RESOLVER"}],
                "facts": [{"key": "Helpshift renewal", "value": "$1,800", "kind": "amount", "home_ids": ["comment_a1"]}]}
    task = Path(root) / "task"
    work = task / "Working_Files"
    work.mkdir(parents=True)
    (task / SQL_NAME).write_text(sql, encoding="utf-8")
    (task / PROMPT_NAME).write_text(prompt, encoding="utf-8")
    (work / "01_Hardness_Manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    (task / "09_Rubrics.json").write_text(json.dumps([{"title": "SECRET-RUBRIC-ROW"}]), encoding="utf-8")
    return {"task": task, "work": work, "sql": sql, "prompt": prompt, "manifest": manifest}


def _fixture_record(task, previous_sql=None) -> dict:
    """Write two briefs and two findings files into the fixture task; return a record that passes `check`.
    With previous_sql the briefs are scoped; the caller adds the revision fields."""
    task = Path(task)
    briefs = {n: build_brief(task, n, previous_sql) for n in ("1", "2")}
    review = task / REVIEW_DIR
    review.mkdir(parents=True, exist_ok=True)
    for n, brief in briefs.items():
        (review / f"brief_{n}.md").write_text(brief["text"], encoding="utf-8")
    (review / "findings_1.json").write_text(json.dumps({"reviewer": "1", "forks": [{"id": "F1"}], "contradictions":
                                                        [{"id": "C1"}], "open_sets": [{"id": "S1"}]}), encoding="utf-8")
    (review / "findings_2.json").write_text(json.dumps({"reviewer": "2", "forks": [], "contradictions": [],
                                                        "open_sets": []}), encoding="utf-8")
    found = candidates(task, "normal")
    return {
        "schema": SCHEMA, "scope": "full", "universe": "normal",
        "bound_to": {SQL_NAME: sha256_file(task / SQL_NAME), PROMPT_NAME: sha256_file(task / PROMPT_NAME)},
        "reviewers": [{"id": n, "model": "claude-opus", "brief_sha256": briefs[n]["sha256"],
                       "findings": (REVIEW_DIR / f"findings_{n}.json").as_posix()} for n in ("1", "2")],
        "forks": [{"id": "F1", "span": "every open bug", "record_ids": ["comment_a1"], "sources": ["1:F1"],
                   "reading_a": {"reading": "ENG-900 is done", "outcome": "no ticket"},
                   "reading_b": {"reading": "ENG-900 is still broken", "outcome": "a ticket in Bugs"},
                   "material": True, "reason": "one more ticket", "status": "settled_in_data",
                   "settled": {"record_ids": ["comment_a1"], "sql_revision": "rev1"}}],
        "open_sets": [{"span": "every open bug", "where": "prompt", "sources": ["1:S1"], "rule": "open on the clock",
                       "census": {"count": 2, "ids": ["comment_a1"], "base_ids": ["ENG-901"]}},
                      {"span": "move every open bug into Linear", "where": "C0123ABCD/1770000000.000100",
                       "rule": "same set", "census": {"count": 1, "ids": [], "base_ids": ["ENG-901"]}}],
        "siblings": [{"id": "D1", "defect": "renewal amount differs", "record_ids": ["comment_a1"],
                      "sources": ["1:C1"], "status": "fixed_in_data",
                      "fix": {"record_ids": ["comment_a1"], "sql_revision": "rev1"},
                      "families": [{"kind": "same_thread", "checked_ids": ["ENG-900"]},
                                   {"kind": "same_author", "none": "usr_1 wrote nothing else"},
                                   {"kind": "same_template", "none": "no other renewal quote"},
                                   {"kind": "same_service_type", "none": "the only injected Linear comment"}]}],
        "base_consistency": [{"fact": "Helpshift renewal", "search": "hg.py search slack Helpshift",
                              "result_count": 2, "conflicts": [{"id": "C9/1.2", "disposition": "older quote"}]}],
        "known_issues": [{"card": k["card"], "disposition": "not graded"} for k in found["known_issues"]],
        "conflicts": [{"candidate": c["id"], "disposition": "designed, settled by the comment"}
                      for c in found["conflicts"]],
        "dismissed": []}


def _self_test() -> int:
    from selftest_sandbox import scratch_tmp
    with scratch_tmp("coherence_sweep_") as tmp:
        fx = _fixture_task(tmp)
        task, work, sql, prompt = fx["task"], fx["work"], fx["sql"], fx["prompt"]

        # brief: prompt, every record with id, author, date and text; nothing from the design
        b1, b2 = build_brief(task, "1"), build_brief(task, "2")
        text = b1["text"]
        assert "move every open bug" in text and "C0123ABCD/1770000000.000100" in text and "U_BRIAN" in text
        assert "comment_a1" in text and "2026-02-10T10:00:00Z" in text and "still broken on Android" in text
        assert "## slack" in text and "### slack container C0123ABCD" in text and "### linear container ENG-900" in text
        for secret in ("SECRET", "decoy", "exclusion", "requirement", "design note", "$1,800\", \"kind"):
            assert secret not in text, secret
        assert build_brief(task, "1")["sha256"] == b1["sha256"] and b1["sha256"] != b2["sha256"]
        (task / PROMPT_NAME).write_text("", encoding="utf-8")
        early = build_brief(task, "1")["text"]
        assert "no prompt is written yet" in early and "Arthur's ask" in early and "SECRET" not in early
        (task / PROMPT_NAME).write_text(prompt, encoding="utf-8")

        # candidates: quantifier, value conflicts, weekday, known-issue card, fact
        found = candidates(task, "normal")
        assert [q["quantifier"] for q in found["quantifiers"] if q["where"] == "prompt"] == ["every"], found["quantifiers"]
        assert any(q["where"] == "C0123ABCD/1770000000.000100" for q in found["quantifiers"])
        ids = {c["id"] for c in found["conflicts"]}
        assert {"X:status:ENG-900", "X:amount:Helpshift", "X:date:due:Helpshift"} <= ids, ids
        assert any(c["kind"] == "weekday" for c in found["conflicts"]), ids      # Feb 12, 2026 is a Thursday
        assert any(k["card"] == "NB-14" and k["level"] == "strong" for k in found["known_issues"]), found["known_issues"]
        assert found["facts"][0]["terms"] == ["Helpshift", "$1,800"], found["facts"]
        assert "search-many" in base_commands(task, base_requests(found["facts"]))[0]

        # check: no record -> FAIL; a complete record -> PASS; planted defects -> FAIL or WARN
        assert evaluate(task, universe="normal")["verdict"] == "FAIL"
        good = _fixture_record(task)

        def run(change=None, **kw):
            record = json.loads(json.dumps(good))
            if change:
                change(record)
            (work / RECORD_NAME).write_text(json.dumps(record), encoding="utf-8")
            return evaluate(task, universe="normal", **kw)

        def status(result, check_id):
            return next(c["status"] for c in result["checks"] if c["id"] == check_id)

        ok = run()
        assert ok["verdict"] == "PASS", to_text(ok)
        assert to_text(ok).startswith("COHERENCE SWEEP (full): PASS")
        r = run(lambda d: d["bound_to"].update({SQL_NAME: "0" * 64}))
        assert status(r, "sweep.bound") == "FAIL"
        r = run(lambda d: d["reviewers"].pop())
        assert status(r, "sweep.reviewers") == "FAIL"
        r = run(lambda d: d["reviewers"][0].update({"brief_sha256": "1" * 64}))
        assert status(r, "sweep.reviewers") == "FAIL"
        r = run(lambda d: d["forks"][0].update({"sources": []}))
        assert status(r, "sweep.findings") == "FAIL"
        r = run(lambda d: (d["forks"][0].update({"sources": []}),
                           d["dismissed"].append({"source": "1:F1", "reason": "same outcome"})))
        assert status(r, "sweep.findings") == "PASS"
        r = run(lambda d: d["forks"][0].update({"status": "open"}))
        assert status(r, "sweep.forks") == "FAIL"
        r = run(lambda d: d["forks"][0]["settled"].update({"record_ids": ["comment_gone"]}))
        assert status(r, "sweep.forks") == "FAIL"
        r = run(lambda d: d["forks"][0].update({"status": "both_fair", "both_fair": {"figure_a": "9"}}))
        assert status(r, "sweep.forks") == "FAIL"
        r = run(lambda d: d["forks"][0].update({"status": "both_fair", "both_fair":
                                                {"figure_a": "9", "figure_b": "10", "rubric_accepts_both": True}}))
        assert status(r, "sweep.forks") == "PASS"
        r = run(lambda d: d["forks"][0].update({"status": "prompt_sentence", "prompt_sentence":
                                                {"sentence": "tell him when done", "reason": "no record can say it"}}))
        assert status(r, "sweep.forks") == "PASS" and status(r, "sweep.prompt_sentences") == "WARN"
        assert r["verdict"] == "WARN"
        r = run(lambda d: d["open_sets"].pop(0))
        assert status(r, "sweep.open_sets") == "FAIL"
        r = run(lambda d: d["open_sets"].pop(1))
        assert status(r, "sweep.open_sets") == "WARN"
        r = run(lambda d: d["open_sets"][0]["census"].update({"ids": ["comment_gone"]}))
        assert status(r, "sweep.open_sets") == "FAIL"
        r = run(lambda d: d["open_sets"][0].update({"census": {"count": 0, "ids": [], "base_ids": []}}))
        assert status(r, "sweep.open_sets") == "FAIL"
        r = run(lambda d: d["siblings"][0].update({"families": []}))
        assert status(r, "sweep.siblings") == "FAIL"
        r = run(lambda d: d["siblings"][0]["families"][0].update({"checked_ids": ["something_else"]}))
        assert status(r, "sweep.siblings") == "FAIL"          # the issue update in the same thread was not checked
        r = run(lambda d: d["base_consistency"].clear())
        assert status(r, "sweep.base") == "FAIL"
        r = run(lambda d: d["base_consistency"][0].update({"conflicts": [], "disposition": ""}))
        assert status(r, "sweep.base") == "FAIL"
        r = run(lambda d: d["known_issues"].clear())
        assert status(r, "sweep.known_issues") == "FAIL"
        r = run(lambda d: d["conflicts"].clear())
        assert status(r, "sweep.conflicts") == "WARN" and r["verdict"] == "WARN"

        # a later SQL edit makes the record stale
        run()
        (task / SQL_NAME).write_text(sql.replace("ok, on it", "ok, on it today"), encoding="utf-8")
        stale = evaluate(task, universe="normal")
        assert status(stale, "sweep.bound") == "FAIL"

        # revision scope: chain to the stored full sweep, scoped brief, changed ids listed
        rev1 = work / "run_forensics" / "rev1"
        rev1.mkdir(parents=True)
        (rev1 / SQL_NAME).write_text(sql, encoding="utf-8")
        (rev1 / RECORD_NAME).write_text(json.dumps(good), encoding="utf-8")
        scoped = build_brief(task, "1", rev1 / SQL_NAME)["text"]
        assert "CHANGED in this revision" in scoped and "next to a changed record" in scoped
        good = _fixture_record(task, rev1 / SQL_NAME)
        good.update({"scope": "revision", "previous_sql_sha256": sha256_file(rev1 / SQL_NAME),
                     "changed_record_ids": ["C0123ABCD/1770000300.000200"],
                     "previous_sweep": {"path": "Working_Files/run_forensics/rev1/" + RECORD_NAME,
                                        "sha256": sha256_file(rev1 / RECORD_NAME)}})
        r = run()
        assert r["verdict"] == "PASS" and r["scope"] == "revision", to_text(r)
        assert to_text(r).startswith("COHERENCE SWEEP (revision): PASS")
        r = run(lambda d: d.update({"changed_record_ids": []}))
        assert status(r, "sweep.chain") == "FAIL"
        r = run(lambda d: d["previous_sweep"].update({"sha256": "2" * 64}))
        assert status(r, "sweep.chain") == "FAIL"
        r = run(lambda d: d.update({"previous_sql_sha256": "3" * 64}))
        assert status(r, "sweep.chain") == "FAIL"
        # a defect outside the scope is carried (its sibling list is not re-validated), but may not be open
        r = run(lambda d: d["siblings"].append({"id": "D2", "defect": "old", "record_ids": ["D0BRIAN01/1770009000.000300"],
                                                "status": "not_a_defect", "reason": "x", "families": []}))
        assert status(r, "sweep.siblings") == "PASS", to_text(r)
        r = run(lambda d: d["siblings"].append({"id": "D2", "defect": "old", "record_ids": ["D0BRIAN01/1770009000.000300"],
                                                "status": "open", "families": []}))
        assert status(r, "sweep.siblings") == "FAIL"
        # template is valid JSON with the current hashes
        t = template(task, rev1 / SQL_NAME, "normal")
        assert t["scope"] == "revision" and t["bound_to"][SQL_NAME] == sha256_file(task / SQL_NAME) and json.dumps(t)
    print("self-test: ok (brief content and no design leak, brief before a prompt, quantifier, value-conflict, "
          "weekday, known-issue and fact candidates, check PASS and a planted FAIL or WARN case for every check, "
          "stale record, revision scope with chain, template)")
    return 0


# ---------------------------------------------------------------- command line

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        return _self_test()
    ap = argparse.ArgumentParser(prog="coherence_sweep.py", description="universe coherence sweep (see docstring)")
    sub = ap.add_subparsers(dest="command")
    p = sub.add_parser("brief", help="write the cold-reviewer brief")
    p.add_argument("--task-dir", required=True)
    p.add_argument("--reviewer", default="1")
    p.add_argument("--previous", help="previous SQL: mark what this revision changed (scoped review)")
    p = sub.add_parser("candidates", help="mechanical pre-pass for the author")
    p.add_argument("--task-dir", required=True)
    p.add_argument("--universe", choices=UNIVERSES)
    p.add_argument("--run-base", choices=("no", "yes", "auto"), default="no",
                   help="run the base searches through hg.py (slow: every export is scanned)")
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("check", help="check the sweep record against the current files")
    p.add_argument("--task-dir", required=True)
    p.add_argument("--previous", help="previous SQL of a revision sweep (default: found by hash under run_forensics/)")
    p.add_argument("--universe", choices=UNIVERSES)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("template", help="print a starting record")
    p.add_argument("--task-dir", required=True)
    p.add_argument("--previous")
    p.add_argument("--universe", choices=UNIVERSES)
    args = ap.parse_args(argv)
    if not args.command:
        ap.error("a command is required: brief, candidates, check or template (or --self-test)")
    try:
        if args.command == "brief":
            brief = build_brief(args.task_dir, args.reviewer, args.previous)
            _atomic_write(brief["path"], brief["text"], "the reviewer brief")
            print(f"COHERENCE SWEEP (brief): PASS\n[PASS] sweep.brief: wrote {rs._rel(brief['path'])} "
                  f"({brief['records']} records, scope {brief['scope']}); sha256 {brief['sha256']}; the reviewer "
                  f"writes {brief['findings']}")
            return 0
        if args.command == "candidates":
            result = candidates_result(args.task_dir, args.universe, args.run_base)
            print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) if args.json
                  else candidates_text(args.task_dir, result))
            return 0
        if args.command == "template":
            print(json.dumps(template(args.task_dir, args.previous, args.universe), indent=2, ensure_ascii=False))
            return 0
        task_files(args.task_dir)                       # a missing task folder or SQL is a usage error (exit 2)
        if args.previous and not Path(args.previous).is_file():
            raise UsageError(f"--previous {args.previous} not found")
        result = _evaluate(args.task_dir, args.previous, args.universe)
    except (UsageError, rs.UsageError) as exc:
        print(f"coherence_sweep: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) if args.json else to_text(result))
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())

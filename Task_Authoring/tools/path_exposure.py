#!/usr/bin/env python3
"""path_exposure.py - is each planned miss off the path a run sweeps anyway?

A hard task hides one deciding record per planned miss (a "unit" of Working_Files/01_Difficulty_Budget.json). In the
completed tasks every failed hardness run had one cause: the deciding record sat where the model looks anyway. This
tool reads each anchor and variance unit's decider from the injected SQL (or the base data, as the persona) and says
EXPOSED, OFF-PATH or UNVERIFIED, with the reason and its evidence. Realism units are skipped.

Reason codes (a unit is EXPOSED when any applies; every one that applies is listed):
  keyword          the decider's own text or title carries a name the task supplies (prompt name, anchor name,
                   cohort entity name), so a plain search for the subject returns it on the first page (newest
                   first). A unit exposed by nothing but a cohort-entity keyword is marked `only_entity_keyword`:
                   the weakest basis in the backtest.
  named_container  the decider's container (thread parent, mail thread, file, ticket, or the channel of a root post)
                   holds an anchor, hub or authority record, or one of those records or the prompt names it.
  root_or_self     a root post in a channel the task reads, a comment on an item of the set, or a tab of a listed sheet.
  sweep_window     the decider is inside a dated sweep the task makes anyway: the messages of a person the prompt
                   names, a channel read whole, or a short dated mailbox listing.
  pointer          the prompt or an injected record carries the decider's id, link or title, names its container, or
                   a declared delegation to it says where it is. A declared delegation that does not say where is an
                   allowed fairness pointer and is reported as a note.
  thin_search      a plain search that reaches the decider returns fewer results than
                   path_exposure.thin_search_min_results (references/first_pass_policy.json), so reading all is cheap.

What is mechanical and what is a rule of thumb is stated in RULES below and printed with every report
(`exposure.rules`), so a reviewer can disagree with a rule instead of with a verdict.

Inputs (--task-dir T): 01_Universe_Inject.sql, Working_Files/01_Difficulty_Budget.json,
Working_Files/01_Hardness_Manifest.json (or the .draft.json), optional 04_Prompt.txt (absent at the injection stage:
keywords and named containers then come from the manifest, and the report says so), optional
Working_Files/01_Gradable_Surface.json (its truth_keys are the cohort entity names), and the base data through
tools/persona_view.py under the task's V3 context. SQL is parsed as text and never executed.

Usage:
  python3.12 -B Task_Authoring/tools/path_exposure.py check --task-dir T [--json] [--write] [--today YYYY-MM-DD]
  python3.12 -B Task_Authoring/tools/path_exposure.py backtest --units FILE [--json] [--out FILE]
  python3.12 -B Task_Authoring/tools/path_exposure.py --self-test
`--write` stores Working_Files/01e_Path_Exposure.json, bound by sha256 to the files it read.
Exit 0 = PASS or WARN, 1 = FAIL, 2 = usage error.
"""
from __future__ import annotations

import argparse
import datetime as dt
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

TOOL, VERSION, TITLE = "path_exposure", 1, "PATH EXPOSURE"
OUT_NAME = "01e_Path_Exposure.json"
BUDGET_NAME = "01_Difficulty_Budget.json"
MANIFEST_NAMES = ("01_Hardness_Manifest.json", "01_Hardness_Manifest.draft.json")
SURFACE_NAME = "01_Gradable_Surface.json"
POLICY_PATH = BUNDLE / "references" / "first_pass_policy.json"
ROSTER_PATH = BUNDLE / "references" / "persona_roster_v2.json"
ARCHIVES = (BUNDLE / "support" / "completed_tasks", BUNDLE / "archived_tasks")
CODES = ("keyword", "named_container", "root_or_self", "sweep_window", "pointer", "thin_search")
CHECKED_ROLES = ("anchor", "variance")

# Thresholds that are not in first_pass_policy.json yet (listed in the final report for the lead).
THIN_DEFAULT = 10              # fallback for path_exposure.thin_search_min_results
SENDER_SWEEP_MAX = 100         # a sender or mailbox listing of at most this many results is read in full
SWEEP_HALF_WINDOW_DAYS = 21    # a dated sweep is counted over at most three weeks either side of the decider
WINDOW_LEAD_DAYS = 7           # the task window opens this many days before the earliest dated anchor
ANCHOR_MAX_AGE_DAYS = 120      # an anchor older than this is a standing document, not a dated ask
DISTINCT_TOKEN_MAX = 50        # one word of a longer name counts only if its persona search returns at most this
KEYWORD_FIRST_PAGE = 20        # a keyword search shows the newest this many results; runs read the first page only
SET_LIST_MAX = 100             # a named Linear team or project counts as the set only up to this many issues
SEARCH_SERVICES = ("slack", "gmail")

RULES = {
    "keywords": "Subject keywords are names only: capitalised or all-caps words and ticket ids in the prompt (when "
                "there is no prompt: the anchors' prompt_reference text), and the cohort entity names (truth_keys of "
                "the gradable surface). People, weekdays, months and service names are not keywords. One word of a "
                f"longer name counts only when a persona search for it returns at most {DISTINCT_TOKEN_MAX} results. "
                "Plain words of the prompt count only through thin_search. Matching is whole-word, case-insensitive "
                "(two-letter names case-sensitive). In Slack and Gmail a keyword counts only when at most "
                f"{KEYWORD_FIRST_PAGE - 1} persona-visible results are newer than the record, so it is on the first "
                f"page newest first (learnings §76: Opus reads the first page of a wide search).",
    "searchable": "A keyword exposes a record only where the service's search returns that kind of record: Slack "
                  "messages and replies, Gmail messages, Drive titles and document text, Linear issue text, GitHub PR "
                  "text and PR conversation comments, Trello card text, Confluence pages, calendar events. Linear "
                  "comments, inline PR review comments, PR reviews, Trello comments and checklists and Confluence "
                  "comments are reached by opening their item, so a keyword in them is a note.",
    "containers": "The path is the prompt plus the records the manifest lists as anchors, ask fragments and "
                  "authorities (not decoys) and the cohort's definition source. A fragment or authority that holds a "
                  "budget decider is that decider's own fairness entry and is left out. A reply's container is its "
                  "thread parent: a reply under another parent in a channel the task reads is not exposed by that "
                  "(carrier reply_under_unrelated_parent), it is a note. Inline PR review comments and Confluence "
                  "page comments on an item of the set are a second read inside the item and are a note. The set "
                  "is the items of a named list, board or the cohort, and of a named Linear team or project of at most "
                  f"{SET_LIST_MAX} issues; a bigger one is filtered by a run, not read whole (carrier "
                  "non_set_ticket).",
    "window": f"The task window opens {WINDOW_LEAD_DAYS} days before the earliest dated anchor record (anchors older "
              f"than {ANCHOR_MAX_AGE_DAYS} days are standing documents and are ignored; with no dated anchor, the "
              "earliest dated Slack or Gmail record on the path) and closes at the data clock. A root post in a read "
              "channel counts only inside the window. When the window cannot be dated, records count as inside it.",
    "senders": "Searched senders are the people the prompt names, except the authors of the anchors (the requester's "
               "own messages are not swept; Frederick Q4 rev4) and the persona. Authors of fragment and authority "
               "records are not searched senders (backtest: runs did not list their messages). With no prompt yet, "
               "nobody is a searched sender. A decider sent by a searched sender inside the window is on a sender sweep "
               f"when that sender has at most {SENDER_SWEEP_MAX} persona-visible messages in the service within "
               f"{SWEEP_HALF_WINDOW_DAYS} days either side of the decider, clipped to the window (Owen rev7: one "
               "sender's six weeks were listed in five calls).",
    "mailbox": f"A Gmail decider inside the window is on a dated mailbox listing when another record on the path is "
               f"in Gmail and the persona's mailbox has at most {SENDER_SWEEP_MAX} threads active within "
               f"{SWEEP_HALF_WINDOW_DAYS} days either side of it.",
    "pointer": "A pointer is the decider's id, link or title, or its container's id, link, name or title, in the "
               "prompt or in the text of an injected record outside that container that the persona can open. Copies "
               "of the same message in other mailboxes are not pointers. A declared delegation (ask_fragments / "
               "names_authorities) to the decider is allowed when its quote names no container: no channel, thread, "
               "file or ticket name and no medium word (DM, email, doc, sheet, ticket, card, PR, page, invite) with a "
               "definite reference ('the ticket', 'his DM', '#ops'). An indefinite one ('on a ticket or a card') "
               "names no container (Samuel rev5/rev6: three such records, none opened).",
    "thin": "thin_search counts three searches as the persona: the searched sender's messages in the window, each "
            "keyword or plain prompt word that the decider carries, and (Gmail) the mailbox threads around the "
            "decider. Counts are substring counts from persona_view (an upper bound on a word search) plus the "
            "matching injected rows.",
    "limits": "Not modelled: search ranking beyond newest-first, what a run does with a result it has opened (a "
              "listed mail with a bland snippet is often never opened), promises of a later message ('I will "
              "confirm'), how far back a run pages a channel or dates a mailbox listing, an owner search that a rule "
              "triggers ('whoever runs it'), and which ticket 'looks like' part of the set.",
    "strength": "Backtest of 2026-11-11 on 108 archived cases (10 tasks; outcome = whether the platform runs opened "
                "the record): 43 of 59 opened records EXPOSED, 22 of 33 unopened records OFF-PATH; the rules were "
                "tuned on these cases, so this is in-sample. By reason (opened / unopened records where it fired): "
                "pointer 11/0, sweep_window 6/0, root_or_self 7/1, named_container 5/1, a prompt keyword 7/0. A "
                "cohort-entity keyword alone was 16/9, no better than flagging everything; such units carry "
                "`only_entity_keyword`.",
}

COMMON = set("""
a about after again all already also although always am an and any anyone anything are as ask asked at back be because
been before being both build but by call can check close confirm copy could create day did do does doing done down
draft each either email every everyone everything file find finish first fix flag for from get give go going got had
has have he hello her here hey hi him his how however i if in into is it its just keep last leave let like link list
look make many mark may me message might month more most move much must my need neither new next no nobody nor not
note nothing now of off ok okay old on once one only onto open or other our out over own per please post pull put re
read ready reply review same save second see send set shall share she should since so some someone something sorry
sort start still such sure take tell than thank thanks that the their them then there these they thing things third
this those though three through to today tomorrow tonight too two under until up update us use very via want was way
we week well were what when where which while who why will with without would write year yes yesterday yet you your
""".split())
NOT_NAMES = set("""
monday tuesday wednesday thursday friday saturday sunday mon tue tues wed thu thur thurs fri sat sun january february
march april june july august september october november december jan feb mar apr jun jul aug sep sept oct nov dec
slack linear drive gmail google trello github confluence snowflake sheets sheet docs doc calendar slides dm dms pr
prs fyi asap tbd eta eod cc id ok am pm utc pt pst pdt est edt q1 q2 q3 q4 hg harmony games harmonygames
""".split())
KW_SEARCHABLE = {"slack_root", "slack_reply", "gmail_message", "gmail_thread", "file", "doc_body", "sheet",
                 "slide_text", "linear_issue", "github_pr", "github_pr_comment", "trello_card", "confluence_page",
                 "gcal_event"}
SECOND_READ = {"github_inline_comment", "confluence_comment"}
ITEM_COMMENT = {"linear_comment", "trello_comment", "trello_action", "trello_checklist", "trello_attachment",
                "github_pr_comment", "github_review"} | SECOND_READ
ITEM_KINDS = {"linear_issue", "trello_card", "confluence_page"}
MEDIUM = {
    "slack_dm": r"\b(dms?|dm'?e?d|direct message|pinged|messaged|slacked)\b",
    "slack": r"#[\w-]{2,}|\b(channel|thread)\b",
    "gmail": r"\b(e-?mail(ed)?|mail(ed)?|inbox|forward(ed)?|thread)\b",
    "file": r"\b(docs?|document|sheet|spreadsheet|tab|deck|slides?|folder|file|notes)\b",
    "linear": r"\b(ticket|issue|comment|linear)\b",
    "github": r"\b(prs?|pull request|review|github|commit)\b",
    "trello": r"\b(card|board|checklist|trello)\b",
    "confluence": r"\b(page|wiki|confluence|runbook)\b",
    "gcal": r"\b(invite|calendar|meeting|event)\b",
}
RX_PREFIX = re.compile(r"^(slack|gmail|gdocs|gdrive|gsheets|gslides|gcal|trello|linear|github|confluence|snowflake|"
                       r"contacts|file):(.+)$", re.S)
RX_SLACK = re.compile(r"^([CDG][A-Z0-9]{8,11})/(\d{9,10}\.\d+)$")
RX_CHANNEL = re.compile(r"^[CDG][A-Z0-9]{8,11}$")
RX_PERSON = re.compile(r"(?:EMPLOYEE|PERSON|SVC)_\d{4}")
RX_EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")


# ------------------------------------------------------------------ small helpers

def _none(v):
    return None if v in (None, "", "None", "null") else v


def _when(v):
    """A Slack ts, epoch seconds or milliseconds, or ISO / RFC 2822 text as an aware UTC datetime, else None."""
    v = _none(v)
    if v is None:
        return None
    s = str(v).strip()
    try:
        if re.fullmatch(r"\d{9,10}(\.\d+)?", s):
            return dt.datetime.fromtimestamp(float(s), dt.timezone.utc)
        if re.fullmatch(r"\d{13}", s):
            return dt.datetime.fromtimestamp(int(s) / 1000.0, dt.timezone.utc)
        iso = s.replace("Z", "+00:00").replace(" ", "T", 1)
        # Postgres text form '2024-10-03 15:20:00+00' (in the archived SQL): spell the offset out, so Python 3.9
        # (whose fromisoformat needs +HH:MM) reads it the same as 3.11+.
        iso = re.sub(r"([+-]\d{2})(\d{2})?$", lambda m: f"{m.group(1)}:{m.group(2) or '00'}", iso) \
            if re.search(r"T\d{2}:\d{2}(:\d{2}(\.\d+)?)?[+-]\d{2}(\d{2})?$", iso) else iso
        d = dt.datetime.fromisoformat(iso)
    except (ValueError, OverflowError, OSError):
        try:
            import email.utils
            d = email.utils.parsedate_to_datetime(s)
        except (TypeError, ValueError, IndexError):
            return None
    if d is None:
        return None
    return d.astimezone(dt.timezone.utc) if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)


def _iso(d):
    return d.strftime("%Y-%m-%dT%H:%M:%SZ") if d else None


def _day(d):
    return d.strftime("%Y-%m-%d") if d else "undated"


def _strings(v, out=None):
    out = [] if out is None else out
    if isinstance(v, str):
        out.append(v)
    elif isinstance(v, dict):
        for x in v.values():
            _strings(x, out)
    elif isinstance(v, (list, tuple)):
        for x in v:
            _strings(x, out)
    return out


def _json_text(v):
    """Strings inside a JSON column (a dict, a list, or its text), joined."""
    if isinstance(v, str):
        try:
            v = json.loads(v)
        except ValueError:
            return v
    return " ".join(_strings(v))


def _rx(term):
    flags = 0 if len(term) <= 2 else re.I
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(term) + r"(?![A-Za-z0-9])", flags)


def _sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.;!?])\s+|\n+", (text or "").replace("\\n", "\n")) if s.strip()]


def _short(text, n=90):
    t = " ".join(str(text or "").split())
    return t if len(t) <= n else t[: n - 1] + "…"


def sha256_file(path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def person_key(raw, ids=None):
    """One key per person across services: the EMPLOYEE_/PERSON_ token, else a directory id, else the email."""
    raw = _none(raw)
    if raw is None:
        return None
    s = str(raw)
    m = RX_PERSON.search(s)
    if m:
        return m.group(0)
    e = RX_EMAIL.search(s)
    s = (e.group(0) if e else s).strip().lower()
    return (ids or {}).get(s, s)


# ------------------------------------------------------------------ one record shape for SQL rows and base records

def _rec(service, kind, ids, **kw):
    r = {"service": service, "kind": kind, "ids": [str(i) for i in ids if _none(i) is not None], "text": "",
         "title": "", "container": None, "own": None, "channel": None, "root": None, "is_reply": False,
         "sender": None, "date": None, "parent": None, "group": None, "folders": [], "source": "sql", "table": None}
    r.update(kw)
    r["id"] = r["ids"][0] if r["ids"] else None
    r["text"] = str(_none(r["text"]) or "").replace("\\n", "\n")
    r["title"] = str(_none(r["title"]) or "")
    return r


def normalise(table, row, aux=None):
    """One SQL row (or a base record mapped to the same columns) as a record; None for tables that carry no text."""
    aux = aux or {}

    def g(k):
        return _none(row.get(k))

    if table == "slack.slack_messages":
        ch, ts = g("channel_id"), g("ts")
        root = g("thread_ts_legacy") or (aux.get("slack_ts") or {}).get(g("thread_parent_id")) or ts
        reply = bool(root and ts and str(root) != str(ts))
        return _rec("slack", "slack_reply" if reply else "slack_root", [f"{ch}/{ts}", g("id")], text=g("text"),
                    container=f"slack:{ch}/{root}", own=None if reply else f"slack:{ch}/{ts}", channel=ch,
                    root=str(root), is_reply=reply, sender=g("user_id"), date=_when(ts), table=table)
    if table == "gmail.gmail_messages":
        subj = g("subject") or ""
        reply = bool(g("in_reply_to")) or bool(re.match(r"\s*(re|fwd?)\s*:", subj, re.I))
        key = str(g("id") or "").split("/", 1)[-1]          # the Message-ID part: one key per message, any mailbox
        return _rec("gmail", "gmail_message", [g("id")], text=g("body_text") or g("snippet"), title=subj,
                    container=f"gmail:{g('thread_id')}", is_reply=reply, sender=g("from_email") or g("from_name"),
                    date=_when(g("date")) or _when(g("internal_date")), group=g("user_email"), table=table,
                    msg_keys=[key] if key.startswith("<") else [])
    if table == "gmail.thread_view":            # built here from a thread's messages, never an SQL table
        msgs = row.get("messages") or []
        last = max(msgs, key=lambda m: m["date"] or dt.datetime.min.replace(tzinfo=dt.timezone.utc)) if msgs else None
        return _rec("gmail", "gmail_thread", [g("id")], text="\n".join(m["text"] for m in msgs),
                    title=msgs[0]["title"] if msgs else "", container=f"gmail:{g('id')}", own=f"gmail:{g('id')}",
                    sender=last["sender"] if last else None, date=last["date"] if last else None,
                    group=g("user_email"), table=table, n_msgs=len(msgs),
                    msg_keys=sorted({k for m in msgs for k in m.get("msg_keys") or []}))
    if table in ("gdrive.drive_files", "gsheets.sheets_spreadsheets", "gslides.slides_presentations"):
        fid = g("id") or g("spreadsheet_id") or g("presentation_id")
        try:
            folders = [str(x) for x in json.loads(g("parents_json") or "[]")]
        except ValueError:
            folders = []
        return _rec(table.split(".")[0], "file", [fid], title=g("name") or g("title"), container=f"file:{fid}",
                    own=f"file:{fid}", sender=g("owner_email"), date=_when(g("modified_time")), folders=folders,
                    table=table)
    if table == "gdocs.docs_documents":
        fid = g("document_id")
        return _rec("gdocs", "doc_body", [fid], title=g("title"), text=g("body_text"), container=f"file:{fid}",
                    own=f"file:{fid}", sender=g("owner_email"), date=_when(g("modified_time")), table=table)
    if table == "gsheets.sheets_sheets":
        fid = g("spreadsheet_id")
        return _rec("gsheets", "sheet_tab", [f"{fid}#{g('sheet_id')}", f"{fid}#{g('title')}"], title=g("title"),
                    text=_json_text(g("grid_json") or ""), container=f"file:{fid}", parent=fid,
                    group=str(g("index") or g("sheet_id") or "0"), table=table)
    if table == "gslides.slides_page_elements":
        fid = g("presentation_id")
        return _rec("gslides", "slide_text", [f"{fid}#{g('object_id')}", g("object_id")], text=g("text"),
                    container=f"file:{fid}", parent=fid, table=table)
    if table == "gcal.gcal_events":
        start = g("start_ts")
        if not start:
            try:
                j = json.loads(g("start_json") or "{}")
                start = j.get("dateTime") or j.get("date")
            except (ValueError, AttributeError):
                start = None
        key = g("ical_uid") or g("event_id")
        return _rec("gcal", "gcal_event", [g("event_id")], title=g("summary"), text=g("description"),
                    container=f"gcal:{key}", own=f"gcal:{key}", sender=g("organizer_email") or g("creator_email"),
                    date=_when(g("created")) or _when(start), table=table)
    if table == "linear.linear_issues":
        key = g("identifier") or g("id")
        box = f"linear:project/{g('project_id')}" if g("project_id") else f"linear:team/{g('team_id')}"
        return _rec("linear", "linear_issue", [key, g("id"), g("uuid")], title=g("title"), text=g("description"),
                    container=box, own=f"linear:{key}", sender=g("creator_id"), date=_when(g("created_at")),
                    table=table)
    if table == "linear.linear_projects":
        return _rec("linear", "linear_project", [g("id")], title=g("name"),
                    text=" ".join(str(x) for x in (g("summary"), g("description"), g("content")) if x),
                    container=f"linear:project/{g('id')}", own=f"linear:project/{g('id')}", sender=g("lead_id"),
                    date=_when(g("created_at")), table=table)
    if table == "linear.linear_comments":
        issue = (aux.get("linear_key") or {}).get(g("issue_id"), g("issue_id"))
        return _rec("linear", "linear_comment", [g("id")], text=g("body"), container=f"linear:{issue}", parent=issue,
                    sender=g("author_id"), date=_when(g("created_at")), table=table)
    if table == "github.github_pull_requests":
        pr = g("id")
        return _rec("github", "github_pr", [pr], title=g("title"), text=g("body"), own=f"github:{pr}",
                    container=f"github:{str(pr).split('#')[0]}", sender=g("author_login"),
                    date=_when(g("created_at")), table=table)
    if table in ("github.github_pr_comments", "github.github_reviews", "github.github_review_comments"):
        kind = {"github.github_pr_comments": "github_pr_comment", "github.github_reviews": "github_review",
                "github.github_review_comments": "github_inline_comment"}[table]
        return _rec("github", kind, [g("id")], text=g("body"), container=f"github:{g('pr_id')}", parent=g("pr_id"),
                    sender=g("author_login"), date=_when(g("created_at") or g("submitted_at")), table=table)
    if table == "trello.trello_cards":
        return _rec("trello", "trello_card", [g("id"), g("shortLink")], title=g("name"), text=g("desc"),
                    container=f"trello:list/{g('idList')}", own=f"trello:{g('id')}", group=g("idBoard"),
                    date=_when(g("dateLastActivity")), table=table)
    if table == "trello.trello_actions":
        data = row.get("data_json") if "data_json" in row else row.get("data")
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except ValueError:
                data = {"text": data}
        text = (data or {}).get("text") if isinstance(data, dict) else ""
        kind = "trello_comment" if g("type") == "commentCard" else "trello_action"
        return _rec("trello", kind, [g("id")], text=text or _json_text(data or ""), container=f"trello:{g('idCard')}",
                    parent=g("idCard"), sender=g("idMemberCreator"), date=_when(g("date")), table=table)
    if table in ("trello.trello_checklists", "trello.trello_check_items", "trello.trello_attachments"):
        card = g("idCard") or (aux.get("checklist_card") or {}).get(g("idChecklist"))
        return _rec("trello", "trello_attachment" if table.endswith("attachments") else "trello_checklist",
                    [g("id")], title=g("name"), text=g("url") or "", container=f"trello:{card}", parent=card,
                    table=table)
    if table == "confluence.confluence_pages":
        return _rec("confluence", "confluence_page", [g("id")], title=g("title"), text=g("body"),
                    container=f"confluence:space/{g('space_id')}", own=f"confluence:{g('id')}",
                    sender=g("author_id"), date=_when(g("updated_at") or g("created_at")), table=table)
    if table == "confluence.confluence_comments":
        return _rec("confluence", "confluence_comment", [g("id")], text=g("body"),
                    container=f"confluence:{g('page_id')}", parent=g("page_id"), sender=g("author_id"),
                    date=_when(g("created_at")), table=table)
    return None


class SqlIndex:
    """The injected rows as records, by every id form the tools use (Slack channel/ts, Gmail mailbox/id, ...)."""

    def __init__(self, sql_text: str):
        from base_check import parse_sql  # the shared SQL grammar (sql_lint underneath)
        self.recs, self.by_id, self.channels, self.updates = [], {}, {}, {}
        stmts = parse_sql(sql_text) if (sql_text or "").strip() else []
        ins = [(x["table"], x["row"]) for x in stmts if x["op"] == "insert"]
        aux = {"slack_ts": {}, "linear_key": {}, "checklist_card": {}}
        for table, row in ins:
            if table == "slack.slack_messages" and row.get("id"):
                aux["slack_ts"][row["id"]] = row.get("ts")
            elif table == "linear.linear_issues":
                for k in ("id", "uuid"):
                    if row.get(k) and row.get("identifier"):
                        aux["linear_key"][row[k]] = row["identifier"]
            elif table == "trello.trello_checklists" and row.get("id"):
                aux["checklist_card"][row["id"]] = row.get("idCard")
            elif table == "slack.slack_channels" and row.get("id"):
                kind = ("im" if str(row.get("is_im")).lower() == "true" else
                        "mpim" if str(row.get("is_mpim")).lower() == "true" else
                        "private" if str(row.get("is_private")).lower() == "true" else "public")
                self.channels[row["id"]] = {"name": row.get("name"), "kind": kind}
        threads = {}
        for table, row in ins:
            r = normalise(table, row, aux)
            if r is None or not r["ids"]:
                continue
            self._add(r)
            if r["kind"] == "gmail_message":
                threads.setdefault(r["container"][6:], []).append(r)
        for tid, msgs in sorted(threads.items()):
            if tid not in self.by_id:
                self._add(normalise("gmail.thread_view", {"id": tid, "user_email": msgs[0]["group"],
                                                          "messages": msgs}))
        for x in stmts:
            if x["op"] == "update":
                for v in x["where"].values():
                    self.updates.setdefault(str(v), []).append((x["table"], dict(x["set"])))

    def _add(self, r):
        self.recs.append(r)
        for i in r["ids"]:
            old = self.by_id.get(i)
            if old is None or len(r["text"]) > len(old["text"]):   # a Drive id: keep the row that carries the text
                self.by_id[i] = r

    def get(self, rid):
        return self.by_id.get(str(rid))


# ------------------------------------------------------------------ the persona's view of the base data

def _roster_people():
    try:
        people = json.loads(ROSTER_PATH.read_text()).get("personas") or []
    except (OSError, ValueError):
        return []
    return [{"key": str(p.get("email") or p.get("name")).lower(), "name": p.get("name") or "",
             "email": str(p.get("email") or "").lower(), "ids": []} for p in people]


class NullView:
    """No base data: base records cannot be read and nothing can be counted."""

    available = False

    def __init__(self, why="no task context was activated"):
        self.why, self.clock, self.persona = why, None, {"key": None, "email": None, "name": None}

    def people(self):
        return _roster_people()

    def channel(self, cid):
        return None

    def record(self, service, rid):
        return None

    def visible(self, service, rid):
        return "UNVERIFIED"

    def sql_visibility(self, sql_text):
        return {}

    def counts(self, service, terms):
        return {t: None for t in terms}

    def sender_count(self, service, person, lo, hi):
        return None

    def mailbox_count(self, lo, hi):
        return None

    def container_size(self, key):
        return None


class StubView(NullView):
    """A small universe from a dict, for the self-test and the unit tests (no base data needed).

    spec: {clock, persona{key,email,name}, people[{key,name,email,ids[]}], channels{id:{name,kind}},
           records[[table,row],...], hidden[ids], sql_hidden[ids]}"""

    available = True

    def __init__(self, spec):
        self.spec = spec
        self.why = ""
        self.clock = _when(spec.get("clock"))
        self.persona = spec.get("persona") or {"key": "stub", "email": "stub@example.com", "name": "Stub Persona"}
        self._recs = [r for r in (normalise(t, row) for t, row in spec.get("records") or []) if r]
        for r in self._recs:
            r["source"] = "base"
        self._hidden = set(spec.get("hidden") or [])

    def people(self):
        return list(self.spec.get("people") or [])

    def channel(self, cid):
        return (self.spec.get("channels") or {}).get(cid)

    def record(self, service, rid):
        for t, row in self.spec.get("records") or []:
            r = normalise(t, row)
            if r and str(rid) in r["ids"]:
                return t, row
        return None

    def visible(self, service, rid):
        return "NO" if str(rid) in self._hidden else "YES"

    def sql_visibility(self, sql_text):
        return {str(i): "NO" for i in self.spec.get("sql_hidden") or []}

    def _seen(self, service):
        return [r for r in self._recs if r["service"] == service and not (set(r["ids"]) & self._hidden)]

    def counts(self, service, terms):
        out = {}
        for t in terms:
            hits = [r for r in self._seen(service) if t.casefold() in (r["title"] + "\n" + r["text"]).casefold()]
            out[t] = {"total": len(hits), "stamps": sorted(r["date"].timestamp() for r in hits if r["date"])}
        return out

    def sender_count(self, service, person, lo, hi):
        ids = {person.get("key")} | set(person.get("ids") or []) | {person.get("email")}
        return sum(1 for r in self._seen(service)
                   if r["kind"] in ("slack_root", "slack_reply", "gmail_message") and r["date"]
                   and (person_key(r["sender"]) in ids or str(r["sender"]).lower() in ids) and lo <= r["date"] <= hi)

    def mailbox_count(self, lo, hi):
        return len({r["container"] for r in self._seen("gmail") if r["date"] and lo <= r["date"] <= hi})

    def container_size(self, key):
        return sum(1 for r in self._recs if r["kind"] == "linear_issue" and r["container"] == key)


BASE_COLLECTIONS = {
    "linear": (("issues", "linear.linear_issues", ("identifier", "id")), ("projects", "linear.linear_projects", ("id",)),
               ("comments", "linear.linear_comments", ("id",))),
    "github": (("pull_requests", "github.github_pull_requests", ("id",)),
               ("pull_request_comments", "github.github_pr_comments", ("id",)),
               ("reviews", "github.github_reviews", ("id",)),
               ("review_comments", "github.github_review_comments", ("id",))),
    "trello": (("cards", "trello.trello_cards", ("id", "shortLink")), ("actions", "trello.trello_actions", ("id",)),
               ("checklists", "trello.trello_checklists", ("id",)),
               ("check_items", "trello.trello_check_items", ("id",)),
               ("attachments", "trello.trello_attachments", ("id",))),
    "confluence": (("pages", "confluence.confluence_pages", ("id",)),
                   ("comments", "confluence.confluence_comments", ("id",))),
}


class PersonaView:
    """The base data as the task's persona sees it: tools/persona_view.py under the task's V3 context."""

    available = True
    why = ""

    def __init__(self, task_dir):
        from runtime_context import activate
        self.context = activate(None, task_dir=Path(task_dir), require_source=True)
        import persona_view as pv
        activate(vars(pv), task_dir=Path(task_dir), require_source=True)
        self.pv, self.u = pv, pv.Universe()
        self.p = pv.resolve_persona(self.context["persona_key"])
        self.clock = pv.DATA_CLOCK
        self.persona = {"key": self.p["persona_key"], "email": self.p["email"], "name": self.p["name"]}
        self._counts, self._exports, self._people = {}, {}, None

    # ---- people and channels
    def people(self):
        if self._people is None:
            out = {}
            for uid, x in sorted(self.u.slack()["users"].items()):
                key = person_key(uid)
                out[key] = {"key": key, "name": x.get("real_name") or x.get("name") or "",
                            "email": str(x.get("email") or "").lower(), "ids": [uid]}
            by_email = {p["email"]: p for p in out.values() if p["email"]}
            try:
                for x in self._export("linear").get("users") or []:
                    p = by_email.get(str(x.get("email") or "").lower())
                    if p and x.get("id"):
                        p["ids"].append(str(x["id"]))
            except (OSError, ValueError):
                pass
            for r in _roster_people():
                if r["email"] not in by_email:
                    out[r["key"]] = r
            self._people = list(out.values())
        return self._people

    def channel(self, cid):
        c = self.u.slack()["channels"].get(cid)
        if c is None:
            return None
        uid = self.u.slack_uid(self.p["email"])
        return {"name": c.get("name"), "kind": c.get("kind"), "member": bool(uid and uid in c["members"])}

    # ---- reading one base record
    def _export(self, service):
        if service not in self._exports:
            path = (self.pv.GITHUB if service == "github" else
                    self.pv.OTHER / "confluence" / "confluence_working.json" if service == "confluence" else
                    self.pv.OTHER / service / "data.json")
            self._exports[service] = json.loads(Path(path).read_text(encoding="utf-8"))
        return self._exports[service]

    def _slack_row(self, cid, ts):
        folder = self.pv.SLACK_MSGS / cid
        when = _when(ts)
        if not folder.is_dir():
            return None
        names = []
        if when:
            for delta in (0, -1, 1):
                m = when.year * 12 + when.month - 1 + delta
                names.append(f"{m // 12:04d}-{m % 12 + 1:02d}.json")
        files = [folder / n for n in names if (folder / n).is_file()] or sorted(folder.glob("*.json"))
        for f in files:
            for m in json.loads(f.read_text(encoding="utf-8")):
                if str(m.get("ts")) == str(ts):
                    return {"id": m.get("id"), "ts": m.get("ts"), "channel_id": cid, "user_id": m.get("user"),
                            "text": m.get("text") or "", "thread_ts_legacy": _none(m.get("thread_ts"))}
        return None

    def _gmail_thread(self, tid):
        entry = self.u.gmail()["threads"].get(tid)
        if not entry:
            return None
        d = json.loads((self.pv.GMAIL / "threads" / entry[4]).read_text(encoding="utf-8"))
        rows = []
        for i, m in enumerate(d.get("messages") or []):
            sender = RX_EMAIL.search(str(m.get("from") or ""))
            rows.append({"id": m.get("id"), "thread_id": tid, "user_email": entry[0], "subject": m.get("subject"),
                         "from_email": sender.group(0).lower() if sender else m.get("from"),
                         "body_text": m.get("body"), "date": m.get("date"),
                         "in_reply_to": m.get("in_reply_to") or ("thread" if i else None)})
        return entry[0], rows

    def record(self, service, rid):
        rid, service = str(rid), (service or "").lower()
        m = RX_SLACK.match(rid)
        if m:
            row = self._slack_row(m.group(1), m.group(2))
            return ("slack.slack_messages", row) if row else None
        if re.fullmatch(r"[0-9a-f]{32}", rid) and service in ("", "slack"):
            hit = self.u.slack_find_ids([rid]).get(rid)
            row = self._slack_row(hit[0], hit[1]) if hit else None
            return ("slack.slack_messages", row) if row else None
        if "/" in rid and ("@" in rid or "_EMAIL" in rid) and service in ("", "gmail"):
            tid = rid if rid in self.u.gmail()["threads"] else self.u.gmail_message_thread(rid)
            got = self._gmail_thread(tid) if tid else None
            if not got:
                return None
            if tid == rid:
                return "gmail.thread_view", {"id": tid, "user_email": got[0],
                                             "messages": [normalise("gmail.gmail_messages", r) for r in got[1]]}
            row = next((r for r in got[1] if r["id"] == rid), None)
            return ("gmail.gmail_messages", row) if row else None
        if re.match(r"^[fd]_[0-9a-z]{6,}$", rid):
            meta = self.u.drive().get(rid)
            if not meta:
                return None
            if meta[1] == self.pv.NATIVE_MIME["gdocs"]:
                if "gdocs_index" not in self._exports:
                    docs = json.loads((self.pv.OTHER / "gdocs" / "data.json").read_text(encoding="utf-8"))
                    self._exports["gdocs_index"] = {d["document_id"]: d for d in docs.get("docs_documents") or []}
                d = self._exports["gdocs_index"].get(rid)
                if d:
                    return "gdocs.docs_documents", {"document_id": rid, "title": d.get("title") or meta[0],
                                                    "body_text": d.get("body_text"), "owner_email": meta[2],
                                                    "modified_time": meta[5]}
            return "gdrive.drive_files", {"id": rid, "name": meta[0], "mime_type": meta[1], "owner_email": meta[2],
                                          "modified_time": meta[5]}
        for svc in ([service] if service in BASE_COLLECTIONS else list(BASE_COLLECTIONS)):
            if service not in BASE_COLLECTIONS and not _shape_fits(svc, rid):
                continue
            key = f"{svc}_index"
            if key not in self._exports:
                idx = {}
                for coll, table, id_cols in BASE_COLLECTIONS[svc]:
                    for row in self._export(svc).get(coll) or []:
                        for c in id_cols:
                            if _none(row.get(c)) is not None:
                                idx.setdefault(str(row[c]), (table, row))
                self._exports[key] = idx
            if rid in self._exports[key]:
                return self._exports[key][rid]
        return None

    def visible(self, service, rid):
        try:
            return self.pv.can_see(self.u, self.p, service, str(rid))["verdict"]
        except SystemExit:
            return "UNVERIFIED"

    def sql_visibility(self, sql_text):
        out = {}
        for row in self.pv.check_sql(self.u, self.p, sql_text)["rows"]:
            for k in row.get("keys") or []:
                out.setdefault(str(k), row["verdict"])
        return out

    # ---- counting as the persona
    def counts(self, service, terms):
        need = sorted({t for t in terms if (service, t) not in self._counts})
        if need and service == "slack":
            self._count_slack(need)
        elif need and service == "gmail":
            self._count_gmail(need)
        for t in need:
            self._counts.setdefault((service, t), None)
        return {t: self._counts[(service, t)] for t in terms}

    def _mine(self):
        s, uid = self.u.slack(), self.u.slack_uid(self.p["email"])
        return [d for d in sorted(os.listdir(self.pv.SLACK_MSGS))
                if uid and uid in (s["channels"].get(d) or {}).get("members", [])]

    def _count_slack(self, terms):
        low = {t: t.casefold() for t in terms}
        acc = {t: [] for t in terms}
        for d in self._mine():
            for f in sorted(os.listdir(self.pv.SLACK_MSGS / d)):
                raw = (self.pv.SLACK_MSGS / d / f).read_text(encoding="utf-8")
                folded = raw.casefold()
                live = [t for t in terms if low[t] in folded]
                if not live:
                    continue
                for m in json.loads(raw):
                    for t in live:
                        if self.pv._match_slack(m, low[t]) is not None:   # persona_view.search's own matcher
                            try:
                                acc[t].append(float(m.get("ts")))
                            except (TypeError, ValueError):
                                acc[t].append(0.0)
        for t in terms:
            self._counts[("slack", t)] = {"total": len(acc[t]), "stamps": sorted(acc[t])}

    def _count_gmail(self, terms):
        mine = self.pv._persona_mailbox(self.u, self.p)
        low = {t: t.casefold() for t in terms}
        acc = {t: [] for t in terms}
        for tid, (mb, _n, _first, last, f) in sorted(self.u.gmail()["threads"].items()):
            if mb != mine:
                continue
            try:
                raw = (self.pv.GMAIL / "threads" / f).read_text(encoding="utf-8")
            except OSError:
                continue
            folded = raw.casefold()
            live = [t for t in terms if low[t] in folded]
            if not live:
                continue
            fields = []
            for m in json.loads(raw).get("messages") or []:
                fields += [str(m.get(k) or "") for k in ("subject", "body", "from", "to", "cc")]
            blob = "\n".join(fields).casefold()
            stamp = (_when(last) or dt.datetime.fromtimestamp(0, dt.timezone.utc)).timestamp()
            for t in live:
                if low[t] in blob:
                    acc[t].append(stamp)
        for t in terms:
            self._counts[("gmail", t)] = {"total": len(acc[t]), "stamps": sorted(acc[t])}

    def sender_count(self, service, person, lo, hi):
        ids = set(person.get("ids") or []) | {person.get("email"), person.get("key")}
        n = 0
        if service == "slack":
            months, m = [], lo.year * 12 + lo.month - 1
            while m <= hi.year * 12 + hi.month - 1:
                months.append(f"{m // 12:04d}-{m % 12 + 1:02d}.json")
                m += 1
            for d in self._mine():
                for name in months:
                    f = self.pv.SLACK_MSGS / d / name
                    if not f.is_file():
                        continue
                    for msg in json.loads(f.read_text(encoding="utf-8")):
                        when = _when(msg.get("ts"))
                        if when and lo <= when <= hi and (msg.get("user") in ids or person_key(msg.get("user")) in ids):
                            n += 1
            return n
        if service == "gmail":
            mine = self.pv._persona_mailbox(self.u, self.p)
            for tid, (mb, _n, first, last, _f) in self.u.gmail()["threads"].items():
                a, b = _when(first), _when(last)
                if mb != mine or not a or not b or b < lo or a > hi:
                    continue
                got = self._gmail_thread(tid)
                for r in (got[1] if got else []):
                    when = _when(r.get("date"))
                    if when and lo <= when <= hi and str(r.get("from_email") or "").lower() in ids:
                        n += 1
            return n
        return None

    def mailbox_count(self, lo, hi):
        mine = self.pv._persona_mailbox(self.u, self.p)
        n = 0
        for _tid, (mb, _n, first, last, _f) in self.u.gmail()["threads"].items():
            a, b = _when(first), _when(last)
            if mb == mine and a and b and b >= lo and a <= hi:
                n += 1
        return n

    def container_size(self, key):
        """Base issues in a Linear team or project (Linear reads are not scoped to the persona)."""
        m = re.match(r"^linear:(team|project)/(.+)$", str(key))
        if not m:
            return None
        col = "team_id" if m.group(1) == "team" else "project_id"
        return sum(1 for x in self._export("linear").get("issues") or [] if str(x.get(col)) == m.group(2))


DEFINITE = {"the", "this", "that", "these", "those", "my", "our", "your", "his", "her", "their", "its"}
INDEFINITE = {"a", "an", "any", "some", "another", "every", "each", "one"}


def _definite_medium(pattern, quote):
    """The first medium word in the quote that names a container: a '#channel', or a medium word whose nearest
    determiner (up to three words back, inside the clause) is definite or a possessive. 'on a ticket or a card' is
    indefinite and names nothing; 'the halloween folder' and 'Brian's DM' do. No determiner at all counts as definite."""
    for m in re.finditer(pattern, quote or "", re.I):
        if m.group(0).startswith("#"):
            return m
        before = re.split(r"[.,;:!?()\n]", quote[:m.start()])[-1]
        kind = None
        for w in reversed(re.findall(r"[A-Za-z']+", before)[-3:]):
            lw = w.lower()
            if lw in INDEFINITE:
                kind = "indefinite"
            elif lw in DEFINITE or lw.endswith("'s"):
                kind = "definite"
            if kind:
                break
        if kind != "indefinite":
            return m
    return None


def _shape_fits(service, rid):
    if service == "linear":
        return bool(re.fullmatch(r"[A-Z][A-Z0-9]{1,6}-\d+", rid)) or bool(re.fullmatch(r"[0-9a-f-]{36}", rid))
    if service == "github":
        return "#" in rid
    if service == "trello":
        return bool(re.fullmatch(r"[0-9a-f]{24}", rid))
    return service == "confluence"


# ------------------------------------------------------------------ the judgement

class Engine:
    """Everything the unit checks share: the injected rows, the path the manifest declares, keywords, the window."""

    def __init__(self, sql_text, manifest, budget, prompt, surface, view, thin):
        self.sql, self.man, self.budget = SqlIndex(sql_text), manifest or {}, budget or {}
        self.prompt, self.surface, self.view, self.thin = prompt or "", surface, view, int(thin)
        self.sql_text = sql_text or ""
        self.notes, self._sizes = [], {}
        from hardness_v2_check import Overlay   # container of an id that is in neither the SQL nor the base
        self._v2 = Overlay(self.sql_text)
        self.people = view.people()
        self._ids = {}
        for p in self.people:
            for i in list(p.get("ids") or []) + [p.get("email")]:
                if i:
                    self._ids[str(i).lower()] = p["key"]
        self._by_key = {p["key"]: p for p in self.people}
        self.me = self._ids.get(str(view.persona.get("email") or "").lower()) or person_key(view.persona.get("email"))
        self.visibility = view.sql_visibility(self.sql_text) if view.available else {}
        units = [u for u in self.budget.get("units") or [] if isinstance(u, dict)]
        self.deciders = {}
        for u in units:
            if u.get("role", "anchor") in CHECKED_ROLES:
                rec, why = self.decider(u.get("decider") or {})
                self.deciders[str(u.get("id"))] = (rec, why)
        self._path()
        self._window()
        self._senders()
        self._keywords()

    # ---- records
    def who(self, raw):
        return person_key(raw, self._ids)

    def name_of(self, key):
        p = self._by_key.get(key)
        return (p.get("name") or key) if p else str(key)

    def resolve(self, pointer, service=None):
        """A record for a manifest pointer or a decider id: the injected row, else the base record, else None."""
        if _none(pointer) is None:
            return None
        rid = str(pointer).strip()
        m = RX_PREFIX.match(rid)
        if m:
            service, rid = service or m.group(1), m.group(2).strip()
        rid = rid.split(" ")[0].split("\t")[0] if not rid.startswith("<") and "/<" not in rid else rid
        rid = re.sub(r"#comment$", "", rid)
        if rid.startswith("project/") and service in (None, "linear", "file"):
            rid = rid[8:]
        rec = self.sql.get(rid)
        if rec is not None:
            return rec
        if not self.view.available:
            return None
        if service == "file":
            service = None
        try:
            got = self.view.record(service or "", rid)
        except (OSError, ValueError, KeyError):
            got = None
        if not got:
            return None
        table, row = got
        for utable, sets in self.sql.updates.get(rid, []):      # an UPDATE on a base record changes what is read
            if utable == table:
                row = dict(row, **sets)
        rec = normalise(table, row)
        if rec:
            rec["source"] = "base"
        return rec

    def decider(self, dec):
        rid = str(_none(dec.get("record_id")) or "").strip()
        svc = str(dec.get("service") or "").strip().lower() or None
        if not rid:
            return None, "the unit names no decider.record_id"
        if svc == "snowflake" or rid.lower().startswith("snowflake:"):
            return None, "warehouse rows are not read by this tool: check the table's path by hand"
        injected = dec.get("injected")
        rec = self.resolve(rid, svc)
        if rec is None and injected is True:
            return None, f"declared injected, but no INSERT in the SQL carries the id {rid}"
        if rec is None:
            if not self.view.available:
                return None, f"a base record, and the base data was not read ({self.view.why})"
            return None, f"{rid} is in neither the SQL nor the persona's base data"
        if rec.get("container") is None and dec.get("container"):
            rec = dict(rec, container=str(dec["container"]))
        return rec, None

    def seen(self, rec):
        """YES / NO / UNVERIFIED: can the persona open the record."""
        if not self.view.available:
            return "UNVERIFIED"
        if rec["source"] == "sql":
            verdicts = [self.visibility[i] for i in rec["ids"] if i in self.visibility]
            if rec["kind"] in ("doc_body", "sheet_tab", "slide_text", "file") and not verdicts:
                fid = (rec["container"] or "")[5:]
                verdicts = [self.visibility[fid]] if fid in self.visibility else []
            return "NO" if "NO" in verdicts else "UNVERIFIED" if "UNVERIFIED" in verdicts else "YES"
        return self.view.visible(rec["service"], rec["id"])

    # ---- the path the manifest declares
    def _same(self, a, b):
        if a is None or b is None:
            return False
        if set(a["ids"]) & set(b["ids"]):
            return True
        for x, y in ((a, b), (b, a)):
            if x["kind"] == "gmail_thread" and y["container"] == x["container"] and x.get("n_msgs") == 1:
                return True
        return False

    def _is_decider(self, rec):
        return any(self._same(rec, d) for d, _ in self.deciders.values() if d is not None)

    def _path(self):
        """entries: the records on the path. own: per decider id, the manifest items that hold it (its fairness
        entries). named: container key -> the entry that makes it part of the path."""
        man = self.man
        self.entries, self.declared, self.named, self.read_channels, self.whole_channels = [], [], {}, {}, {}
        groups = []
        for a in man.get("anchors") or []:
            if isinstance(a, dict):
                groups.append(("anchor", a, [a.get("locator"), a.get("record")], a.get("service")))
        for f in man.get("ask_fragments") or []:
            if isinstance(f, dict):
                ptrs = [f.get("container"), f.get("locator")] + list(f.get("seeded_ids") or []) + \
                    list(f.get("base_pointers") or [])
                groups.append(("fragment", f, ptrs, f.get("service")))
        for h in man.get("authorities") or []:
            if isinstance(h, dict):
                groups.append(("authority", h, list(h.get("seeded_ids") or []) + list(h.get("base_pointers") or []),
                               h.get("home_service")))
        cohort = man.get("cohort") if isinstance(man.get("cohort"), dict) else {}
        src = cohort.get("definition_source")
        groups.append(("cohort", {"id": "definition"}, src if isinstance(src, list) else [src], None))
        for role, item, ptrs, service in groups:
            label = f"{role} {item.get('id')}"
            found = []
            for ptr in ptrs:
                if _none(ptr) is None or not isinstance(ptr, str):
                    continue
                bare = RX_PREFIX.match(ptr.strip())
                bare = (bare.group(2) if bare else ptr).strip().split(" ")[0]
                if RX_CHANNEL.match(bare):
                    found.append((ptr, None, f"slack:{bare}", bare))
                    continue
                rec = self.resolve(ptr, service if role != "cohort" else None)
                if rec is not None:
                    found.append((ptr, rec, rec["container"], rec["channel"]))
                    continue
                if "project/" in ptr or (re.fullmatch(r"[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}", bare)
                                         and service in (None, "linear")):
                    found.append((ptr, None, "linear:project/" + bare.split("project/")[-1], None))
                    continue
                key = self._v2.container(ptr)
                if key:
                    found.append((ptr, None, key, key[6:].split("/")[0] if key.startswith("slack:") else None))
            if role in ("fragment", "authority") and any(r is not None and self._is_decider(r) for _, r, _, _ in found):
                self.declared.append((role, item, [r for _, r, _, _ in found if r is not None]))
                continue
            for ptr, rec, key, channel in found:
                self.entries.append({"role": role, "label": label, "item": item, "pointer": ptr, "rec": rec})
                for k in (key, rec["own"] if rec else None):
                    if k:
                        self.named.setdefault(k, label)
                if channel:
                    self.read_channels.setdefault(channel, label)
                    if rec is None and key == f"slack:{channel}":
                        self.whole_channels.setdefault(channel, label)
        for s in cohort.get("evidence_surfaces") or []:
            if isinstance(s, dict) and re.search(r"read_channel|history|conversations", str(s.get("tool") or ""), re.I):
                for sid in s.get("seeded_ids") or []:
                    bare = str(sid).split("/")[0]
                    if RX_CHANNEL.match(bare):
                        self.whole_channels.setdefault(bare, "a cohort surface")
                        self.read_channels.setdefault(bare, "a cohort surface")
        # the items of the set: truth keys that are ids, surface seeded ids, and injected issues of a named project
        self.cohort_items = {}
        keys = (self.surface or {}).get("truth_keys") if isinstance(self.surface, dict) else None
        for k in keys or []:
            if isinstance(k, str) and re.fullmatch(r"[A-Z][A-Z0-9]{1,6}-\d+", k):
                self.cohort_items.setdefault(f"linear:{k}", "a cohort item (truth key)")
        for s in cohort.get("evidence_surfaces") or []:
            for sid in (s.get("seeded_ids") or []) if isinstance(s, dict) else []:
                rec = self.resolve(sid, s.get("service"))
                if rec is not None and rec["own"]:
                    self.cohort_items.setdefault(rec["own"], "a cohort item (evidence surface)")
        for r in self.sql.recs:
            if r["kind"] in ITEM_KINDS and self._set_box(r["container"]) and not self._is_decider(r):
                self.cohort_items.setdefault(r["own"], f"an item of {r['container']} ({self.named[r['container']]})")
        self.path_texts = [("the prompt", self.prompt, None)] if self.prompt.strip() else []
        seen = set()
        for e in self.entries:
            rec = e["rec"]
            if rec is not None and rec["id"] not in seen:
                seen.add(rec["id"])
                self.path_texts.append((e["label"], rec["title"] + "\n" + rec["text"], rec))

    def _set_box(self, key):
        """A named container whose items are the set the task reads. A Linear team or project counts only up to
        SET_LIST_MAX issues (base plus injected): a run lists a small project whole (Claire 58 tickets, LLC 37) but
        filters a big one (Samuel rev5/rev6: comments on team tickets outside the filter, 0 of 7)."""
        if key not in self.named:
            return False
        if not str(key).startswith(("linear:team/", "linear:project/")):
            return True
        if key not in self._sizes:
            try:
                base = self.view.container_size(key)
            except (OSError, ValueError, KeyError):
                base = None
            mine = sum(1 for r in self.sql.recs if r["kind"] == "linear_issue" and r["container"] == key)
            self._sizes[key] = (base or 0) + mine
        return self._sizes[key] <= SET_LIST_MAX

    def _window(self):
        clock = self.view.clock
        dated = [(e["rec"]["date"], e["label"]) for e in self.entries
                 if e["role"] == "anchor" and e["rec"] is not None and e["rec"]["date"]]
        if clock:
            dated = [x for x in dated if (clock - x[0]).days <= ANCHOR_MAX_AGE_DAYS]
        basis = "the earliest dated anchor"
        if not dated:
            dated = [(e["rec"]["date"], e["label"]) for e in self.entries
                     if e["rec"] is not None and e["rec"]["date"] and e["rec"]["source"] == "sql"
                     and e["rec"]["service"] in SEARCH_SERVICES]
            basis = "the earliest dated injected Slack or Gmail record on the path (no dated anchor)"
        if dated:
            first = min(dated)
            self.lo = first[0] - dt.timedelta(days=WINDOW_LEAD_DAYS)
            self.window_basis = f"{WINDOW_LEAD_DAYS} days before {basis}, {first[1]} ({_day(first[0])})"
        else:
            self.lo, self.window_basis = None, "no dated anchor or path record: every record counts as inside"
        self.hi = clock

    def inside(self, when):
        return self.lo is None or when is None or when >= self.lo

    def _senders(self):
        anchors = {self.who(e["rec"]["sender"]) for e in self.entries
                   if e["role"] == "anchor" and e["rec"] is not None and e["rec"]["sender"]}
        # Only the people the prompt names. Authors of fragment and authority records were searched senders in the
        # first version; in the backtest that rule flagged six records no run opened (Bridge rev10, Claire rev3/rev4,
        # Owen rev5) and was the only reason for no record a run did open, so it was dropped.
        self.searched = {}
        low = self.prompt.lower()
        firsts = {}
        for p in self.people:
            name = str(p.get("name") or "")
            if not re.fullmatch(r"[A-Za-z][A-Za-z .'-]+", name):
                continue
            firsts.setdefault(name.split()[0].lower(), []).append(p)
        for p in self.people:
            name = str(p.get("name") or "")
            if not re.fullmatch(r"[A-Za-z][A-Za-z .'-]+", name):
                continue
            first = name.split()[0].lower()
            if _rx(name).search(low) or (len(first) >= 3 and len(firsts[first]) == 1 and _rx(first).search(low)):
                self.searched.setdefault(p["key"], "named in the prompt")
        for k in anchors | {self.me, None}:
            self.searched.pop(k, None)
        self.anchor_authors = anchors - {None}

    # ---- keywords
    def _name_tokens(self):
        out = set()
        for p in self.people:
            name = str(p.get("name") or "")
            if re.fullmatch(r"[A-Za-z][A-Za-z .'-]+", name):
                out |= {t.lower() for t in re.findall(r"[A-Za-z]{3,}", name)}
        return out

    def _names_in(self, text, mid_sentence, source, people):
        """Capitalised runs, all-caps words and ticket ids of a text: {lowered: (original, source)}."""
        out = {}

        def flush(run):
            part = []
            for t in run + [None]:
                if t is not None and t.lower() not in NOT_NAMES and t.lower() not in people:
                    part.append(t)
                    continue
                if part and not (len(part) == 1 and (len(part[0]) < 2 or part[0].lower() in COMMON)):
                    out.setdefault(" ".join(part).lower(), (" ".join(part), source))
                part = []

        for sent in _sentences(text):
            run = []
            for i, tok in enumerate(re.findall(r"[A-Za-z0-9][A-Za-z0-9&-]*(?:['’]s)?", sent)):
                t = re.sub(r"['’]s$", "", tok)
                caps = t.isupper() and len(t) >= 2 and any(c.isalpha() for c in t)
                if not (t[:1].isupper() or caps):
                    flush(run)
                    run = []
                    continue
                if i == 0 and not mid_sentence and not caps and t.lower() in COMMON:
                    continue
                run.append(t)
            flush(run)
        return out

    def _keywords(self):
        people = self._name_tokens()
        man = self.man
        if self.prompt.strip():
            self.source = "04_Prompt.txt, the anchors' prompt_reference names and the cohort entity names"
        else:
            self.source = ("the manifest (no 04_Prompt.txt yet): anchor names, cohort entity names and "
                           "ask-fragment text")
        names = self._names_in(self.prompt, False, "the prompt", people)
        plain_text = [self.prompt]
        for a in man.get("anchors") or []:
            ref = str((a or {}).get("prompt_reference") or "")
            plain_text.append(ref)
            for k, v in self._names_in(ref, True, f"anchor {a.get('id')} name", people).items():
                names.setdefault(k, v)
        cohort = man.get("cohort") if isinstance(man.get("cohort"), dict) else {}
        entity = [k for k in ((self.surface or {}).get("truth_keys") or []) if isinstance(k, str)] \
            if isinstance(self.surface, dict) else []
        entity += [str(x) for x in cohort.get("entities") or [] if isinstance(x, str)]
        for k in entity:
            k = k.strip()
            if len(k) >= 3 and k.lower() not in NOT_NAMES and k.lower() not in COMMON and k.lower() not in people:
                names.setdefault(k.lower(), (k, "a cohort entity name"))
        if not self.prompt.strip():
            for f in man.get("ask_fragments") or []:
                plain_text.append(str((f or {}).get("delegation_quote") or ""))
            plain_text += [str(cohort.get("definition") or ""), str(cohort.get("key") or "")]
        self.kw = {}
        for low, (orig, src) in sorted(names.items()):
            self.kw[low] = {"term": orig, "cls": "A", "source": src, "rx": _rx(orig)}
        for low, (orig, src) in sorted(names.items()):
            if " " not in orig:
                continue
            for t in re.findall(r"[A-Za-z]{4,}", orig):
                tl = t.lower()
                if tl not in self.kw and tl not in COMMON and tl not in NOT_NAMES and tl not in people:
                    self.kw[tl] = {"term": t, "cls": "T", "source": f"one word of '{orig}' ({src})", "rx": _rx(t)}
        for t in sorted(set(re.findall(r"[a-z]{4,}", " ".join(plain_text).lower()))):
            if t not in self.kw and t not in COMMON and t not in NOT_NAMES and t not in people:
                self.kw[t] = {"term": t, "cls": "B", "source": "a plain word of the task's own text", "rx": _rx(t)}

    def carried(self, rec):
        text = rec["title"] + "\n" + rec["text"]
        return [k for k in sorted(self.kw) if self.kw[k]["rx"].search(text)]

    def count(self, rec, term):
        """Results of a persona search for term in the record's service: base hits plus injected rows plus itself."""
        if rec["service"] not in SEARCH_SERVICES or not self.view.available:
            return None
        base = self.view.counts(rec["service"], [term]).get(term)
        if base is None:
            return None
        stamp = rec["date"].timestamp() if rec["date"] else None
        low = term.casefold()
        injected = [r for r in self.sql.recs if r is not rec and r["service"] == rec["service"]
                    and r["kind"] in ("slack_root", "slack_reply", "gmail_message")
                    and low in (r["title"] + "\n" + r["text"]).casefold() and self.seen(r) != "NO"]
        newer = sum(1 for s in base["stamps"] if stamp is not None and s > stamp)
        newer += sum(1 for r in injected if stamp is not None and r["date"] and r["date"].timestamp() > stamp)
        return {"results": base["total"] + len(injected) + 1, "newer": newer}

    # ---- names of a record and of its container
    def channel_info(self, cid):
        return self.sql.channels.get(cid) or self.view.channel(cid) or {}

    def names_of(self, rec):
        """(record-level, container-level) strings that point at the record; each is (string, what it is)."""
        own, box = [], []

        def add(to, s, what, min_len=6):
            s = str(_none(s) or "").strip()
            if len(s) >= min_len and (s, what) not in to:
                to.append((s, what))

        for i in rec["ids"]:
            add(own, i, "its id")
        kind = rec["kind"]
        if kind in ("slack_root", "slack_reply"):
            ts = rec["id"].split("/")[-1]
            add(own, "p" + ts.replace(".", ""), "its message link")
            info = self.channel_info(rec["channel"])
            add(box, rec["channel"], "its channel id", 9)
            if info.get("name") and info.get("kind") not in ("im", "mpim"):
                add(box, "#" + str(info["name"]), "its channel name", 3)
            if rec["is_reply"]:
                add(box, f"{rec['channel']}/{rec['root']}", "its thread parent")
                add(box, "p" + str(rec["root"]).replace(".", ""), "its thread parent's link")
                parent = self.resolve(f"{rec['channel']}/{rec['root']}", "slack")
                for i in (parent["ids"] if parent else []):
                    add(box, i, "its thread parent's id")
        elif kind == "gmail_message":
            add(box, rec["container"][6:], "its mail thread id")
            subject = re.sub(r"^\s*((re|fwd?)\s*:\s*)+", "", rec["title"], flags=re.I)
            add(box, subject, "its mail subject", 12)
        elif kind in ("doc_body", "file", "sheet", "gmail_thread", "gcal_event", "linear_issue", "linear_project",
                      "github_pr", "trello_card", "confluence_page"):
            add(own, rec["title"], "its title", 8)
            if kind == "github_pr" and "#" in str(rec["id"]):
                add(own, "pull/" + str(rec["id"]).split("#")[-1], "its PR link", 6)
        if kind in ("sheet_tab", "slide_text", "doc_body") or kind in ITEM_COMMENT:
            parent = rec["parent"] or (rec["container"] or "").split(":", 1)[-1]
            add(box, parent, "its item's id", 5)
            item = self.resolve(parent, rec["service"]) if parent else None
            if item is not None and item is not rec:
                add(box, item["title"], "its item's title", 12)
                for i in item["ids"]:
                    add(box, i, "its item's id", 5)
            if kind.startswith("github") and "#" in str(parent):
                add(box, "pull/" + str(parent).split("#")[-1], "its PR link", 6)
        if rec["own"]:                      # a record that is its own container: every name of it names the container
            box = own + box
        return own, box

    @staticmethod
    def _find(names, text):
        low = text.lower()
        for s, what in names:
            if (_rx(s).search(text) if what == "its item's id" and len(s) < 9 else s.lower() in low):
                return s, what
        return None

    def medium(self, rec):
        if rec["service"] == "slack":
            info = self.channel_info(rec["channel"])
            return "slack_dm" if info.get("kind") in ("im", "mpim") or str(rec["channel"]).startswith("D") else "slack"
        return {"gdocs": "file", "gdrive": "file", "gsheets": "file", "gslides": "file"}.get(rec["service"],
                                                                                           rec["service"])

    # ---- the checks
    def judge(self, unit):
        uid, role = str(unit.get("id")), unit.get("role", "anchor")
        out = {"id": uid, "role": role, "verdict": None, "reasons": [], "notes": [], "unchecked": [],
               "decider": dict(unit.get("decider") or {})}
        rec, why = self.deciders.get(uid, (None, "not resolved"))
        if rec is None:
            out.update(verdict="UNVERIFIED", why=why)
            return out
        seen = self.seen(rec)
        out["record"] = {"kind": rec["kind"], "source": rec["source"], "container": rec["container"],
                         "sender": self.name_of(self.who(rec["sender"])) if rec["sender"] else None,
                         "date": _iso(rec["date"]), "persona_can_open": seen, "text": _short(rec["text"], 140)}
        if seen == "NO":
            out.update(verdict="UNVERIFIED", why="the persona cannot open the record (persona_view says NO): fix "
                                                 "its reach before judging its path")
            return out

        def hit(code, detail, **evidence):
            out["reasons"].append({"code": code, "detail": detail, "evidence": evidence})

        if rec["source"] == "sql" and (unit.get("decider") or {}).get("injected") is False:
            out["notes"].append("the budget says the decider is a base record, but the SQL inserts it")
        if not self.view.available:
            out["unchecked"].append(f"sweep_window and thin_search need the base data ({self.view.why})")
        self._keyword(rec, hit, out)
        self._container(rec, hit, out)
        self._sweep(rec, hit, out)
        self._pointer(rec, hit, out)
        order = {c: i for i, c in enumerate(CODES)}
        out["reasons"].sort(key=lambda r: (order[r["code"]], r["detail"]))
        # The weakest basis: nothing but a cohort-entity keyword (and the thin search for it). It still exposes the
        # record, but in the backtest it was right only at the base rate, so the report says so (see RULES strength).
        ent = {r["evidence"].get("keyword") for r in out["reasons"]
               if r["code"] == "keyword" and "a cohort entity name" in str(r["evidence"].get("source"))}
        out["only_entity_keyword"] = bool(out["reasons"]) and all(
            r["code"] in ("keyword", "thin_search") and r["evidence"].get("keyword") in ent for r in out["reasons"])
        if out["reasons"]:
            out["verdict"] = "EXPOSED"
        elif out["unchecked"]:
            out.update(verdict="UNVERIFIED", why="not every condition could be checked: " + "; ".join(out["unchecked"]))
        else:
            out["verdict"] = "OFF-PATH"
        return out

    def _keyword(self, rec, hit, out):
        searchable = rec["kind"] in KW_SEARCHABLE
        who = self.view.persona.get("key") or "the persona"
        for low in self.carried(rec):
            k = self.kw[low]
            c = self.count(rec, k["term"])
            found = (f"; a {rec['service']} search for '{k['term']}' as {who} returns {c['results']} result(s), "
                     f"{c['newer']} newer than the record" if c else "")
            ev = {"keyword": k["term"], "source": k["source"], "search": c}
            if k["cls"] == "B":
                if c and c["results"] < self.thin and searchable:
                    hit("thin_search", f"the record carries '{k['term']}', {k['source']}{found}: fewer than "
                        f"{self.thin}, so reading every result is cheap", **ev)
                continue
            if not searchable:
                out["notes"].append(f"keyword '{k['term']}' ({k['source']}) is in the record, but a {rec['kind']} "
                                    f"is not returned by a text search: not counted")
                continue
            if c and c["newer"] >= KEYWORD_FIRST_PAGE:
                out["notes"].append(f"keyword '{k['term']}' ({k['source']}) is in the record, but {c['newer']} newer "
                                    f"result(s) put it past the first page of {KEYWORD_FIRST_PAGE} (newest first): "
                                    f"not counted")
                continue
            if k["cls"] == "T":
                if c is None:
                    out["notes"].append(f"'{k['term']}' ({k['source']}) is in the record; not counted because the "
                                        f"search could not be run")
                    continue
                if c["results"] > DISTINCT_TOKEN_MAX:
                    out["notes"].append(f"'{k['term']}' ({k['source']}) is in the record but is a common word here "
                                        f"({c['results']} results): not counted")
                    continue
            hit("keyword", f"the record's own text carries '{k['term']}', {k['source']}{found}", **ev)
            if c and c["results"] < self.thin:
                hit("thin_search", f"the search for '{k['term']}' returns {c['results']} result(s), fewer than "
                    f"{self.thin}", **ev)

    def _container(self, rec, hit, out):
        kind, box = rec["kind"], rec["container"]
        label = self.named.get(box)
        inside = self.inside(rec["date"])
        if kind == "slack_root":
            where = self.read_channels.get(rec["channel"])
            name = self.channel_info(rec["channel"]).get("name") or rec["channel"]
            if where and inside:
                hit("root_or_self", f"a root post in {name}, a channel the task reads (it holds {where}), dated "
                    f"{_day(rec['date'])} inside the task window (from {_day(self.lo)})", channel=rec["channel"],
                    path_record=where)
                if rec["channel"] in self.whole_channels:
                    hit("sweep_window", f"{name} is read whole ({self.whole_channels[rec['channel']]}) and the post "
                        f"is inside the window", channel=rec["channel"])
            elif where:
                out["notes"].append(f"a root post in {name}, which the task reads, but dated {_day(rec['date'])}, "
                                    f"before the task window opens ({_day(self.lo)}): not counted")
        elif kind == "slack_reply":
            if label:
                hit("named_container", f"a reply in the thread of {label}", container=box, path_record=label)
            elif rec["channel"] in self.read_channels:
                out["notes"].append(f"a reply under another parent in a channel the task reads "
                                    f"({self.read_channels[rec['channel']]}): found only by opening that thread")
        elif kind in ITEM_COMMENT:
            item = box
            why = self.named.get(item) or self.cohort_items.get(item)
            if not why:
                parent = self.resolve(rec["parent"], rec["service"]) if rec["parent"] else None
                if parent is not None and self._set_box(parent["container"]):
                    why = f"an item of {parent['container']} ({self.named[parent['container']]})"
            if why and kind in SECOND_READ:
                out["notes"].append(f"a {kind.replace('_', ' ')} on {item}, {why}: a second read inside the item "
                                    f"(measured between 0 and half of runs), not counted")
            elif why:
                hit("root_or_self", f"a {kind.replace('_', ' ')} on {item}, {why}", item=item, path_record=why)
        elif kind == "sheet_tab":
            if label:
                hit("root_or_self", f"a tab of {box}, a sheet the task lists ({label})", container=box,
                    path_record=label)
        elif kind in ITEM_KINDS:
            why = self.cohort_items.get(rec["own"]) or (self.named.get(box) if self._set_box(box) else None)
            if why:
                hit("root_or_self", f"the item itself is in the set the task reads: {why}", item=rec["own"],
                    path_record=why)
        elif label:
            hit("named_container", f"it sits in {box}, which holds {label}", container=box, path_record=label)
        for folder in rec.get("folders") or []:
            if f"file:{folder}" in self.named:
                hit("named_container", f"it is filed in folder {folder}, which the task names "
                    f"({self.named['file:' + folder]})", container=f"file:{folder}",
                    path_record=self.named[f"file:{folder}"])
        # named in words by the prompt or a path record
        _own, names = self.names_of(rec)
        if kind == "slack_reply":
            names = [n for n in names if n[1].startswith("its thread parent")]
        for src, text, src_rec in self.path_texts:
            if src_rec is not None and (src_rec is rec or rec["container"] in (src_rec["container"], src_rec["own"])):
                continue
            got = self._find(names, text)
            if got and (kind != "slack_root" or inside):
                hit("named_container", f"{src} names {got[1]} ({got[0]})", naming_record=src, match=got[0])

    def _sweep(self, rec, hit, out):
        if rec["kind"] not in ("slack_root", "slack_reply", "gmail_message") or not self.view.available:
            return
        when = rec["date"]
        if when is None:
            out["unchecked"].append("the record has no date, so no dated sweep could be placed")
            return
        if not self.inside(when):
            out["notes"].append(f"dated {_day(when)}, before the task window opens ({_day(self.lo)}): outside any "
                                f"dated sweep")
            return
        half = dt.timedelta(days=SWEEP_HALF_WINDOW_DAYS)
        lo = max(when - half, self.lo) if self.lo else when - half
        hi = min(when + half, self.hi) if self.hi else when + half
        span = f"{_day(lo)} to {_day(hi)}"
        sender = self.who(rec["sender"])
        if sender in self.searched:
            person = self._by_key.get(sender) or {"key": sender, "ids": [str(rec["sender"])], "email": None}
            base = self.view.sender_count(rec["service"], person, lo, hi)
            if base is None:
                out["unchecked"].append(f"messages from {self.name_of(sender)} could not be counted")
            else:
                mine = sum(1 for r in self.sql.recs if r["service"] == rec["service"] and r["date"]
                           and r["kind"] in ("slack_root", "slack_reply", "gmail_message")
                           and self.who(r["sender"]) == sender and lo <= r["date"] <= hi and self.seen(r) != "NO")
                n = base + mine
                ev = {"sender": self.name_of(sender), "why_searched": self.searched[sender], "window": span,
                      "results": n}
                if n <= SENDER_SWEEP_MAX:
                    hit("sweep_window", f"sent by {self.name_of(sender)}, a searched sender "
                        f"({self.searched[sender]}); a {rec['service']} listing of that sender for {span} as the "
                        f"persona returns {n} message(s), at most {SENDER_SWEEP_MAX}", **ev)
                    if n < self.thin:
                        hit("thin_search", f"the sender search for {self.name_of(sender)} over {span} returns {n} "
                            f"message(s), fewer than {self.thin}", **ev)
                else:
                    out["notes"].append(f"sent by searched sender {self.name_of(sender)}, but that sender has {n} "
                                        f"messages in {span}: too many for a sweep, not counted")
        elif sender in self.anchor_authors:
            out["notes"].append(f"sent by {self.name_of(sender)}, who wrote an anchor: the requester's own messages "
                                f"are not counted as a sender sweep")
        if rec["kind"] == "gmail_message":
            on_path = [e["label"] for e in self.entries if e["rec"] is not None and e["rec"]["service"] == "gmail"]
            n = self.view.mailbox_count(lo, hi)
            if on_path and n is not None:
                n += len({r["container"] for r in self.sql.recs if r["kind"] == "gmail_message" and r["date"]
                          and lo <= r["date"] <= hi and self.seen(r) != "NO"})
                ev = {"window": span, "results": n, "gmail_on_path": on_path[0]}
                if n <= SENDER_SWEEP_MAX:
                    hit("sweep_window", f"Gmail is on the path ({on_path[0]}) and the persona's mailbox has {n} "
                        f"thread(s) active in {span}, at most {SENDER_SWEEP_MAX}: a dated listing shows it", **ev)
                    if n < self.thin:
                        hit("thin_search", f"a dated mailbox listing for {span} returns {n} thread(s), fewer than "
                            f"{self.thin}", **ev)
                else:
                    out["notes"].append(f"the persona's mailbox has {n} threads active in {span}: too many for a "
                                        f"dated listing to count")
            elif not on_path:
                out["notes"].append("no record on the path is in Gmail, so no dated mailbox listing is assumed")

    def _pointer(self, rec, hit, out):
        own, box = self.names_of(rec)
        if rec["kind"] == "slack_reply":
            box = [n for n in box if n[1].startswith("its thread parent")]
        if self.prompt.strip():
            got = self._find(own, self.prompt)
            if got:
                hit("pointer", f"the prompt carries {got[1]} ({got[0]})", pointing_record="the prompt", match=got[0])
        on_path = {id(e["rec"]) for e in self.entries if e["rec"] is not None}
        mine = set(rec.get("msg_keys") or [])
        for r in self.sql.recs:
            if r is rec or self._same(r, rec) or rec["container"] in (r["container"], r["own"]):
                continue
            if rec["kind"] == "gmail_message" and r["kind"] == "gmail_thread":
                continue
            if mine & set(r.get("msg_keys") or []):      # the same message in another mailbox is not a pointer
                continue
            if self.view.available and self.seen(r) == "NO":   # a record the persona cannot open points nowhere
                continue
            text = r["title"] + "\n" + r["text"]
            got = self._find(own, text)
            if not got and id(r) not in on_path and not rec["own"]:
                got = self._find(box, text)
            if got:
                hit("pointer", f"injected record {r['id']} ({r['kind']}) carries {got[1]} ({got[0]})",
                    pointing_record=r["id"], match=got[0])
        for role, item, recs in self.declared:
            if not any(self._same(r, rec) for r in recs):
                continue
            quotes = []
            if role == "fragment":
                quotes.append((item.get("delegated_by_record"), item.get("delegation_quote")))
            else:
                for f in self.man.get("ask_fragments") or []:
                    for n in (f or {}).get("names_authorities") or []:
                        if isinstance(n, dict) and n.get("id") == item.get("id"):
                            quotes.append((f.get("locator") or f.get("container"), n.get("quote")))
            for by, quote in quotes:
                quote = str(_none(quote) or "")
                by_rec = self.resolve(by) if by else None
                if not quote or (by_rec is not None and self._same(by_rec, rec)):
                    continue
                names = self._find(box, quote)
                word = _definite_medium(MEDIUM.get(self.medium(rec), r"$^"), quote)
                if names or word:
                    what = f"{names[1]} ({names[0]})" if names else f"where it is ('{word.group(0)}')"
                    hit("pointer", f"declared delegation {item.get('id')} from {by}: \"{_short(quote, 70)}\" names "
                        f"{what}", pointing_record=str(by), quote=quote)
                else:
                    out["notes"].append(f"allowed fairness pointer: {item.get('id')} from {by} says "
                                        f"\"{_short(quote, 70)}\" and names no container")


# ------------------------------------------------------------------ evaluate

def _policy(policy=None):
    if isinstance(policy, dict):
        return policy
    try:
        return json.loads(Path(policy or POLICY_PATH).read_text())
    except (OSError, ValueError):
        return {}


def _slot(task_dir, name):
    from stage_gate import slot_path  # importing stage_gate has no side effects
    return slot_path(task_dir, name)


def _rel(path, task_dir):
    try:
        return Path(path).resolve().relative_to(Path(task_dir).resolve()).as_posix()
    except ValueError:
        return str(path)


def _fmt(unit):
    head = f"{unit['verdict']} ({unit['role']}"
    rec = unit.get("record")
    if rec:
        head += f"; {rec['kind']} {unit['decider'].get('record_id')}"
    head += ")"
    if unit["verdict"] == "EXPOSED":
        weak = (" [weakest basis: only a cohort-entity keyword; runs search some entity names and not others, so "
                "rename or move the record anyway]") if unit.get("only_entity_keyword") else ""
        return head + ": " + " | ".join(f"{r['code']}: {r['detail']}" for r in unit["reasons"]) + weak
    if unit["verdict"] == "UNVERIFIED":
        return head + ": " + unit.get("why", "")
    notes = unit.get("notes") or []
    return head + ": no condition applies" + (" (notes: " + " | ".join(notes) + ")" if notes else "")


def evaluate(task_dir, budget=None, sql=None, manifest=None, prompt=None, surface=None, view=None, policy=None,
             today=None) -> dict:
    """The report for one task folder. Reads only; `view` replaces the persona's base view (tests, self-test).

    budget / sql / manifest / prompt / surface override the files found in task_dir; prompt=False forces the
    injection-stage reading (no prompt) even when 04_Prompt.txt exists."""
    td = Path(task_dir)
    pol = _policy(policy)
    thin = (pol.get("path_exposure") or {}).get("thin_search_min_results", THIN_DEFAULT)
    paths = {
        "sql": Path(sql) if sql else _slot(td, "01_Universe_Inject.sql"),
        "budget": Path(budget) if budget else _slot(td, BUDGET_NAME),
        "manifest": Path(manifest) if manifest else next(
            (p for p in (_slot(td, n) for n in MANIFEST_NAMES) if p.is_file()), _slot(td, MANIFEST_NAMES[0])),
        "prompt": None if prompt is False else (Path(prompt) if prompt else _slot(td, "04_Prompt.txt")),
        "surface": Path(surface) if surface else _slot(td, SURFACE_NAME),
    }
    checks, bound, loaded, problems = [], {}, {}, []

    def add(cid, status, detail):
        checks.append({"id": cid, "status": status, "detail": detail})

    for key in ("sql", "budget", "manifest", "prompt", "surface"):
        p = paths[key]
        if p is None or not p.is_file():
            if key in ("sql", "budget", "manifest"):
                problems.append(f"{key} file missing ({_rel(p, td)})")
            continue
        try:
            text = p.read_text(encoding="utf-8")
            loaded[key] = text if key in ("sql", "prompt") else json.loads(text)
            if key in ("budget", "manifest") and not isinstance(loaded[key], dict):
                raise ValueError("not a JSON object")
            bound[_rel(p, td)] = sha256_file(p)
        except (OSError, ValueError) as exc:
            loaded.pop(key, None)
            if key in ("sql", "budget", "manifest"):
                problems.append(f"{key} file unreadable ({_rel(p, td)}: {exc})")
    result = {"tool": TOOL, "version": VERSION, "verdict": "FAIL", "bound_to": bound, "checks": checks,
              "gate_mode": (pol.get("modes") or {}).get("exposure.units", "warn"),
              "thresholds": {"thin_search_min_results": thin, "sender_sweep_max": SENDER_SWEEP_MAX,
                             "sweep_half_window_days": SWEEP_HALF_WINDOW_DAYS,
                             "window_lead_days": WINDOW_LEAD_DAYS, "anchor_max_age_days": ANCHOR_MAX_AGE_DAYS,
                             "distinct_token_max": DISTINCT_TOKEN_MAX},
              "rules": RULES, "units": []}
    if today:
        result["today"] = str(today)
    if problems:
        add("exposure.bound", "FAIL", "; ".join(problems) + ": nothing was checked")
        add("exposure.units", "SKIP", "inputs missing")
        return result
    add("exposure.bound", "PASS", f"{len(bound)} file(s) hashed: " + ", ".join(sorted(bound)))
    if view is None:
        try:
            view = PersonaView(td)
        except Exception as exc:  # no V3 context or no base data: say so and judge what the SQL alone shows
            view = NullView(f"{type(exc).__name__}: {_short(exc, 160)}")
    eng = Engine(loaded["sql"], loaded["manifest"], loaded["budget"], loaded.get("prompt"), loaded.get("surface"),
                 view, thin)
    add("exposure.sources", "PASS", f"keywords and named containers come from {eng.source}; "
        f"{sum(1 for k in eng.kw.values() if k['cls'] == 'A')} name keyword(s), {len(eng.entries)} path record(s), "
        f"{len(eng.declared)} fragment(s) or authority(ies) held back as a decider's own fairness entry")
    if view.available:
        add("exposure.base", "PASS", f"base data read as {view.persona.get('key')}; data clock {_iso(view.clock)}")
    else:
        add("exposure.base", "WARN", f"base data not read ({view.why}): sweep_window and thin_search were not "
            f"checked and base deciders are UNVERIFIED")
    units = [u for u in loaded["budget"].get("units") or [] if isinstance(u, dict)]
    lines = []
    for u in units:
        uid = str(u.get("id"))
        if u.get("role", "anchor") not in CHECKED_ROLES:
            lines.append((f"exposure.unit.{uid}", "SKIP", f"{u.get('role')} unit: not checked"))
            result["units"].append({"id": uid, "role": u.get("role"), "verdict": "SKIPPED"})
            continue
        res = eng.judge(u)
        result["units"].append(res)
        lines.append((f"exposure.unit.{uid}", {"EXPOSED": "FAIL", "UNVERIFIED": "WARN"}.get(res["verdict"], "PASS"),
                      _fmt(res)))
    judged = [u for u in result["units"] if u["verdict"] != "SKIPPED"]
    exposed = [u["id"] for u in judged if u["verdict"] == "EXPOSED"]
    unverified = [u["id"] for u in judged if u["verdict"] == "UNVERIFIED"]
    if not judged:
        add("exposure.units", "WARN", "the budget has no anchor or variance unit to check")
    elif exposed:
        weak = [u["id"] for u in judged if u["verdict"] == "EXPOSED" and u.get("only_entity_keyword")]
        add("exposure.units", "FAIL", f"{len(exposed)} of {len(judged)} anchor/variance unit(s) EXPOSED "
            f"({', '.join(exposed)}): move the record off the path; there is no accepted exposure"
            + (f"; on the weakest basis (a cohort-entity keyword only): {', '.join(weak)}" if weak else "")
            + (f"; UNVERIFIED: {', '.join(unverified)}" if unverified else ""))
    elif unverified:
        add("exposure.units", "WARN", f"{len(unverified)} of {len(judged)} unit(s) UNVERIFIED "
            f"({', '.join(unverified)}); the rest are OFF-PATH")
    else:
        add("exposure.units", "PASS", f"all {len(judged)} anchor/variance unit(s) are OFF-PATH")
    for line in lines:
        add(*line)
    add("exposure.rules", "PASS", "rules applied: window = " + eng.window_basis + "; searched senders = "
        + (", ".join(f"{eng.name_of(k)} ({v})" for k, v in sorted(eng.searched.items())) or "none")
        + "; the full rule text is under `rules` in --json and in the tool's RULES")
    result["window"] = {"from": _iso(eng.lo), "to": _iso(eng.hi), "basis": eng.window_basis}
    result["searched_senders"] = {eng.name_of(k): v for k, v in sorted(eng.searched.items())}
    result["keyword_source"] = eng.source
    result["keywords"] = sorted(k["term"] for k in eng.kw.values() if k["cls"] == "A")
    result["stage"] = "prompt" if (loaded.get("prompt") or "").strip() else "injection"
    states = {c["status"] for c in checks}
    result["verdict"] = "FAIL" if "FAIL" in states else "WARN" if "WARN" in states else "PASS"
    return result


def to_text(result: dict) -> str:
    qualifier = f"{result.get('stage', 'no')} stage, {len(result.get('units') or [])} unit(s)"
    lines = [f"{TITLE} ({qualifier}): {result['verdict']}"]
    lines += [f"[{c['status']}] {c['id']}: {c['detail']}" for c in result["checks"]]
    return "\n".join(lines)


def write_report(task_dir, result: dict) -> Path:
    from task_context import refuse_read_only
    out = _slot(Path(task_dir), OUT_NAME)
    refuse_read_only(out, "The path-exposure report")
    out.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{out.name}.", suffix=".tmp", dir=out.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=1, sort_keys=True, ensure_ascii=False)
            fh.write("\n")
        os.replace(tmp, out)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return out


# ------------------------------------------------------------------ backtest on archived tasks

def _archive(task):
    p = Path(task)
    if p.is_absolute():
        return p if (p / "00_Assigments.md").is_file() or not (p / "task_inputs").is_dir() else p / "task_inputs"
    for root in ARCHIVES:
        for cand in (root / task / "task_inputs", root / task):
            if (cand / "00_Assigments.md").is_file():
                return cand
    raise ValueError(f"archived task {task!r} not found under {', '.join(str(a) for a in ARCHIVES)}")


def _context_dir(archive: Path, scratch: Path) -> Path:
    """The folder to load the V3 context from: the archive, or a cleaned copy of an older assignment sheet."""
    from task_context import ContextError, load_context
    try:
        load_context(archive, require_source=True)
        return archive
    except ContextError:
        pass
    text = (archive / "00_Assigments.md").read_text(encoding="utf-8")
    clean = "\n".join(re.sub(r"\s+#\s.*$", "", line) if re.match(r"^\s*[A-Za-z_]+:\s", line) else line
                      for line in text.splitlines()) + "\n"
    folder = scratch / archive.parent.name
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "00_Assigments.md").write_text(clean, encoding="utf-8")
    load_context(folder, require_source=True)       # raises when the sheet still does not resolve
    return folder


def _old_tools(manifest, sql_text, prompt, surface, nodes):
    """What hardness_v2_check and trap_liveness say about the manifest nodes of one case."""
    out = {"hardness_v2_check": "not run", "trap_liveness": "not run"}
    nodes = set(nodes or [])
    if not nodes:       # both tools judge manifest nodes; with no node they cannot speak to this record
        return {"hardness_v2_check": "no node", "trap_liveness": "no node"}
    try:
        import hardness_v2_check as hv
        rep = hv.run(manifest, sql_text, prompt, surface)
        flags = sorted({f"{f['check']}" + (f"/{f['kind']}" if f.get("kind") else "") for f in rep["flags"]
                        if f.get("node") in nodes})
        out["hardness_v2_check"] = "FLAG " + ",".join(flags) if flags else "CLEAN"
    except Exception as exc:
        out["hardness_v2_check"] = f"error {type(exc).__name__}"
    try:
        import trap_liveness as tl
        rep = tl.run(manifest, sql_text, prompt)
        flags = sorted({f for n in rep["nodes"] if n["id"] in nodes for f in n["flagged"]})
        out["trap_liveness"] = "FLAG " + ",".join(flags) if flags else "CLEAN"
    except Exception as exc:
        out["trap_liveness"] = f"error {type(exc).__name__}"
    return out


def backtest(units_file, keep_going=True) -> dict:
    """Replay stored revisions of archived tasks. Each case names an archive, an SQL revision, the decider and the
    known outcome; a temporary budget is built in scratch because archives carry none."""
    import selftest_sandbox
    data = json.loads(Path(units_file).read_text(encoding="utf-8"))
    cases = data.get("cases") if isinstance(data, dict) else data
    if not isinstance(cases, list) or not cases:
        raise ValueError("the units file needs a non-empty `cases` list")
    groups = {}
    for c in cases:
        key = (c["task"], c.get("sql") or "", c.get("manifest") or "", str(c.get("prompt")))
        groups.setdefault(key, []).append(c)
    rows = []
    ctx_root = selftest_sandbox.SCRATCH / "path_exposure_ctx"
    try:
        with selftest_sandbox.scratch_tmp("path_exposure_bt_") as tmp:
            for n, ((task, sql, manifest, prompt), members) in enumerate(sorted(groups.items())):
                try:
                    archive = _archive(task)
                    sql_path = archive / (sql or "01_Universe_Inject.sql")
                    man_path = archive / manifest if manifest else next(
                        (p for p in (_slot(archive, x) for x in MANIFEST_NAMES) if p.is_file()), None)
                    first = members[0]
                    prompt_arg = False if first.get("prompt") is False else (
                        archive / first["prompt"] if first.get("prompt") else archive / "04_Prompt.txt")
                    surface = _slot(archive, SURFACE_NAME)
                    budget = Path(tmp) / f"budget_{n}.json"
                    budget.write_text(json.dumps({"schema": "difficulty-budget-v1", "units": [
                        {"id": c["id"], "role": c.get("role", "anchor"), "decider": c["decider"],
                         "habit": c.get("habit") or {}} for c in members]}))
                    view = PersonaView(_context_dir(archive, ctx_root))
                    res = evaluate(archive, budget=budget, sql=sql_path, manifest=man_path, prompt=prompt_arg,
                                   surface=surface, view=view)
                    if res["checks"][0]["status"] == "FAIL":
                        raise ValueError(res["checks"][0]["detail"])
                    by = {u["id"]: u for u in res["units"]}
                    man = json.loads(Path(man_path).read_text())
                    sql_text = sql_path.read_text(encoding="utf-8")
                    ptxt = prompt_arg.read_text(encoding="utf-8") if prompt_arg and prompt_arg.is_file() else ""
                    surf = json.loads(surface.read_text()) if surface.is_file() else None
                    for c in members:
                        u = by[c["id"]]
                        rows.append(dict(
                            {"id": c["id"], "task": task, "revision": c.get("revision"), "outcome": c["outcome"],
                             "found": c.get("found"), "predicted": u["verdict"],
                             "reasons": sorted({r["code"] for r in u.get("reasons") or []}),
                             "detail": _fmt(u), "carrier": c.get("carrier"),
                             "only_entity_keyword": bool(u.get("only_entity_keyword"))},
                            **_old_tools(man, sql_text, ptxt, surf, c.get("nodes"))))
                except Exception as exc:
                    if not keep_going:
                        raise
                    for c in members:
                        rows.append({"id": c["id"], "task": task, "revision": c.get("revision"),
                                     "outcome": c["outcome"], "found": c.get("found"), "predicted": "ERROR",
                                     "reasons": [], "detail": f"{type(exc).__name__}: {_short(exc, 200)}",
                                     "carrier": c.get("carrier"), "hardness_v2_check": "not run",
                                     "trap_liveness": "not run"})
    finally:
        import shutil
        shutil.rmtree(ctx_root, ignore_errors=True)
    rows.sort(key=lambda r: r["id"])

    def tally(flagged):
        t = {"leaked_flagged": 0, "leaked_missed": 0, "landed_clear": 0, "landed_flagged": 0, "mixed_flagged": 0,
             "mixed_clear": 0, "not_judged": 0}
        for r in rows:
            f = flagged(r)
            if f is None:
                t["not_judged"] += 1
            elif r["outcome"] == "leaked":
                t["leaked_flagged" if f else "leaked_missed"] += 1
            elif r["outcome"] == "landed":
                t["landed_flagged" if f else "landed_clear"] += 1
            else:
                t["mixed_flagged" if f else "mixed_clear"] += 1
        return t

    def old(name):
        return lambda r: None if not str(r[name]).startswith(("FLAG", "CLEAN")) else r[name].startswith("FLAG")

    totals = {
        "path_exposure": tally(lambda r: {"EXPOSED": True, "OFF-PATH": False}.get(r["predicted"])),
        "hardness_v2_check": tally(old("hardness_v2_check")),
        "trap_liveness": tally(old("trap_liveness")),
        "either_old_tool": tally(lambda r: None if not (str(r["hardness_v2_check"]).startswith(("FLAG", "CLEAN"))
                                                        and str(r["trap_liveness"]).startswith(("FLAG", "CLEAN")))
                                 else r["hardness_v2_check"].startswith("FLAG") or r["trap_liveness"].startswith("FLAG")),
    }
    return {"tool": TOOL, "version": VERSION, "kind": "backtest", "units_file": str(units_file), "cases": rows,
            "totals": totals,
            "reading": "leaked = runs found the record (EXPOSED is right); landed = runs missed it (OFF-PATH is "
                       "right); mixed = about half the runs found it (reported, not scored)"}


def backtest_text(rep: dict) -> str:
    lines = [f"{TITLE} BACKTEST ({len(rep['cases'])} case(s))"]
    for r in rep["cases"]:
        ok = {("leaked", "EXPOSED"): "right", ("landed", "OFF-PATH"): "right", ("leaked", "OFF-PATH"): "MISS",
              ("landed", "EXPOSED"): "FALSE ALARM"}.get((r["outcome"], r["predicted"]), "-")
        lines.append(f"  {r['id']:34} {r['outcome']:7} -> {r['predicted']:10} {ok:11} "
                     f"[{','.join(r['reasons']) or '-'}]  v2: {r['hardness_v2_check']}; liveness: {r['trap_liveness']}")
    for name, t in rep["totals"].items():
        lines.append(f"  {name:18} leaked flagged {t['leaked_flagged']}/{t['leaked_flagged'] + t['leaked_missed']}, "
                     f"landed clear {t['landed_clear']}/{t['landed_clear'] + t['landed_flagged']}, mixed flagged "
                     f"{t['mixed_flagged']}/{t['mixed_flagged'] + t['mixed_clear']}, not judged {t['not_judged']}")
    return "\n".join(lines)


# ------------------------------------------------------------------ self-test

SELFTEST_SQL = """-- synthetic injection for path_exposure --self-test (never executed)
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy) VALUES ('m_hub', '1770000000.000100', 'C0HUBCHAN01', 'message', 'EMPLOYEE_0001_SLACK_ID', 'Please sort out the Orchid renewals. The rules are in the Orchid rules doc. Vera owns the vendor calls.', NULL, '1770000000.000100');
INSERT INTO gdocs.docs_documents (document_id, title, body_text, owner_email, modified_time) VALUES ('f_rules00001', 'Orchid rules', 'A renewal counts once the vendor has answered. One of the answers came in later.', 'boss@example.com', '2026-02-01T10:00:00Z');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy) VALUES ('m_kw', '1770100000.000100', 'C0OTHER0001', 'message', 'EMPLOYEE_0003_SLACK_ID', 'heads up, Brightvale said no to the renewal', 'm_old', '1760000000.000100');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy) VALUES ('m_named', '1770100100.000100', 'C0HUBCHAN01', 'message', 'EMPLOYEE_0003_SLACK_ID', 'she passed on it', 'm_hub', '1770000000.000100');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy) VALUES ('m_root', '1770100200.000100', 'C0HUBCHAN01', 'message', 'EMPLOYEE_0003_SLACK_ID', 'they are out', NULL, '1770100200.000100');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy) VALUES ('m_sweep', '1770100300.000100', 'D0VERADM001', 'message', 'EMPLOYEE_0002_SLACK_ID', 'that one is off, they went elsewhere', NULL, '1770100300.000100');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy) VALUES ('m_ptr', '1770100400.000100', 'C0QUIET0001', 'message', 'EMPLOYEE_0003_SLACK_ID', 'we let that lapse', 'm_q', '1760000500.000100');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy) VALUES ('m_tell', '1770100450.000100', 'C0OTHER0002', 'message', 'EMPLOYEE_0004_SLACK_ID', 'the answer is in C0QUIET0001/1760000500.000100 if anyone needs it', NULL, '1770100450.000100');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy) VALUES ('m_fair', '1770100500.000100', 'C0QUIET0002', 'message', 'EMPLOYEE_0003_SLACK_ID', 'no go from them', 'm_q2', '1760000600.000100');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy) VALUES ('m_off', '1770100600.000100', 'C0QUIET0003', 'message', 'EMPLOYEE_0003_SLACK_ID', 'that renewal is not happening', 'm_q3', '1760000700.000100');
INSERT INTO gmail.gmail_messages (id, thread_id, user_email, subject, from_email, body_text, date) VALUES ('me@example.com/<thin@x>', 'me@example.com/900', 'me@example.com', 'quick note', 'vera@example.com', 'we will not renew', '2026-02-03T09:00:00Z');
INSERT INTO gmail.gmail_messages (id, thread_id, user_email, subject, from_email, body_text, date) VALUES ('me@example.com/<path@x>', 'me@example.com/901', 'me@example.com', 'terms', 'vera@example.com', 'the terms are attached', '2026-02-02T09:00:00Z');
INSERT INTO linear.linear_issues (id, identifier, title, description, project_id, team_id, created_at) VALUES ('ORC-1', 'ORC-1', 'Renew Sunmere', 'renewal', 'proj-orchid', 'team_ORC', '2026-02-01T00:00:00Z');
INSERT INTO linear.linear_comments (id, issue_id, author_id, body, created_at) VALUES ('cmt_self', 'ORC-1', 'usr_x', 'cancelled by the vendor', '2026-02-03T00:00:00Z');
"""


def _selftest_fixture():
    manifest = {
        "anchors": [{"id": "A1", "service": "slack", "locator": "C0HUBCHAN01/1770000000.000100",
                     "prompt_reference": "the Orchid renewals ask"}],
        "ask_fragments": [
            {"id": "K1", "service": "gdocs", "container": "f_rules00001", "locator": "f_rules00001",
             "seeded_ids": ["f_rules00001"], "delegated_by_record": "C0HUBCHAN01/1770000000.000100",
             "delegation_quote": "The rules are in the Orchid rules doc"},
            {"id": "K2", "service": "slack", "container": "C0QUIET0002/1770100500.000100",
             "locator": "C0QUIET0002/1770100500.000100", "seeded_ids": ["m_fair"],
             "delegated_by_record": "f_rules00001", "delegation_quote": "One of the answers came in later"},
            {"id": "K3", "service": "gmail", "container": "me@example.com/901", "locator": "me@example.com/<path@x>",
             "seeded_ids": ["me@example.com/<path@x>"], "delegated_by_record": "f_rules00001",
             "delegation_quote": "once the vendor has answered"}],
        "authorities": [{"id": "H1", "name": "the Orchid rules doc", "home_service": "gdocs",
                         "seeded_ids": ["f_rules00001"]}],
        "cohort": {"definition_source": ["linear:project/proj-orchid"], "key": "vendor", "size": 3,
                   "evidence_surfaces": []},
    }
    surface = {"truth_keys": ["Brightvale", "Sunmere", "Kestrel Park"], "slots": []}

    def unit(uid, rid, service="slack", role="anchor", injected=True):
        return {"id": uid, "role": role, "cause": uid, "carrier": "other:test",
                "habit": {"service": service, "action": "read"},
                "decider": {"service": service, "record_id": rid, "injected": injected}}

    budget = {"schema": "difficulty-budget-v1", "design_id": "D1", "revision": "rev1", "mode": "easy", "units": [
        unit("U_KEYWORD", "C0OTHER0001/1770100000.000100"),
        unit("U_NAMED", "C0HUBCHAN01/1770100100.000100"),
        unit("U_ROOT", "C0HUBCHAN01/1770100200.000100"),
        unit("U_SELF", "cmt_self", "linear"),
        unit("U_SWEEP", "D0VERADM001/1770100300.000100"),
        unit("U_POINTER", "C0QUIET0001/1770100400.000100"),
        unit("U_THIN", "me@example.com/<thin@x>", "gmail"),
        unit("U_FAIR", "C0QUIET0002/1770100500.000100", role="variance"),
        unit("U_OFF", "C0QUIET0003/1770100600.000100"),
        unit("U_MISSING", "C0NOWHERE01/1770100700.000100"),
        unit("U_BASE", "C0BASE00001/1769000000.000100", injected=False),
        unit("U_REAL", "C0HUBCHAN01/1770100200.000100", role="realism"),
    ]}
    stub = {
        "clock": "2026-02-14T00:00:00Z",
        "persona": {"key": "me", "email": "me@example.com", "name": "Mina Example"},
        "people": [{"key": "EMPLOYEE_0001", "name": "Bo Sender", "email": "boss@example.com",
                    "ids": ["EMPLOYEE_0001_SLACK_ID"]},
                   {"key": "EMPLOYEE_0002", "name": "Vera Quill", "email": "vera@example.com",
                    "ids": ["EMPLOYEE_0002_SLACK_ID"]},
                   {"key": "EMPLOYEE_0003", "name": "Odd Poster", "email": "odd@example.com",
                    "ids": ["EMPLOYEE_0003_SLACK_ID"]}],
        "channels": {"C0HUBCHAN01": {"name": "orchid", "kind": "public"},
                     "D0VERADM001": {"name": None, "kind": "im"}},
        "records": [["slack.slack_messages", {"id": "b1", "ts": "1769000000.000100", "channel_id": "C0BASE00001",
                                              "user_id": "EMPLOYEE_0003_SLACK_ID", "text": "base note, nothing named",
                                              "thread_ts_legacy": "1768000000.000100"}]]
        + [["slack.slack_messages", {"id": f"v{i}", "ts": f"17699{i:05d}.000100", "channel_id": "C0BUSY00001",
                                     "user_id": "EMPLOYEE_0002_SLACK_ID", "text": "busy chatter"}] for i in range(3)],
    }
    return manifest, surface, budget, stub


def _write_fixture(folder: Path, prompt: bool = True):
    manifest, surface, budget, stub = _selftest_fixture()
    wf = folder / "Working_Files"
    wf.mkdir(parents=True, exist_ok=True)
    (folder / "01_Universe_Inject.sql").write_text(SELFTEST_SQL)
    (wf / BUDGET_NAME).write_text(json.dumps(budget, indent=1))
    (wf / MANIFEST_NAMES[0]).write_text(json.dumps(manifest, indent=1))
    (wf / SURFACE_NAME).write_text(json.dumps(surface, indent=1))
    if prompt:
        (folder / "04_Prompt.txt").write_text("Can you sort out the Orchid renewals the way the ask lays it out? "
                                              "Vera has the vendor side.\n")
    return stub


def _self_test() -> None:
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("path_exposure_selftest_") as tmp:
        td = Path(tmp) / "task"
        stub = _write_fixture(td)
        res = evaluate(td, view=StubView(stub))
        by = {u["id"]: u for u in res["units"]}
        codes = {k: sorted({r["code"] for r in v.get("reasons") or []}) for k, v in by.items()}
        assert res["verdict"] == "FAIL" and res["stage"] == "prompt", res["verdict"]
        assert codes["U_KEYWORD"] == ["keyword", "thin_search"], by["U_KEYWORD"]            # names a cohort entity
        assert codes["U_NAMED"] == ["named_container"], by["U_NAMED"]                        # reply in the anchor thread
        assert codes["U_ROOT"] == ["root_or_self"], by["U_ROOT"]                             # root in the anchor's channel
        assert codes["U_SELF"] == ["root_or_self"], by["U_SELF"]                             # comment on a cohort item
        assert codes["U_SWEEP"] == ["sweep_window", "thin_search"], by["U_SWEEP"]            # prompt-named sender's DM
        assert codes["U_POINTER"] == ["pointer"], by["U_POINTER"]                            # another row links its thread
        assert "thin_search" in codes["U_THIN"] and "sweep_window" in codes["U_THIN"], by["U_THIN"]
        assert by["U_FAIR"]["verdict"] == "OFF-PATH" and any("allowed fairness pointer" in n
                                                             for n in by["U_FAIR"]["notes"]), by["U_FAIR"]
        assert by["U_OFF"]["verdict"] == "OFF-PATH" and not by["U_OFF"]["reasons"], by["U_OFF"]
        assert by["U_MISSING"]["verdict"] == "UNVERIFIED" and "no INSERT" in by["U_MISSING"]["why"], by["U_MISSING"]
        assert by["U_BASE"]["verdict"] == "OFF-PATH" and by["U_BASE"]["record"]["source"] == "base", by["U_BASE"]
        assert by["U_REAL"]["verdict"] == "SKIPPED", by["U_REAL"]
        status = {c["id"]: c["status"] for c in res["checks"]}
        assert status["exposure.units"] == "FAIL" and status["exposure.unit.U_OFF"] == "PASS", status
        assert status["exposure.unit.U_MISSING"] == "WARN" and status["exposure.unit.U_REAL"] == "SKIP", status
        assert set(res["bound_to"]) == {"01_Universe_Inject.sql", "04_Prompt.txt", "Working_Files/" + BUDGET_NAME,
                                        "Working_Files/" + MANIFEST_NAMES[0], "Working_Files/" + SURFACE_NAME}
        assert res == evaluate(td, view=StubView(stub)), "two runs on the same bytes differ"
        # a fairness pointer that names the medium with a definite reference is exposure; an indefinite one is a note
        man = json.loads((td / "Working_Files" / MANIFEST_NAMES[0]).read_text())
        man["ask_fragments"][1]["delegation_quote"] = "the answer is in a thread somewhere"
        (td / "Working_Files" / MANIFEST_NAMES[0]).write_text(json.dumps(man))
        loose = {u["id"]: u for u in evaluate(td, view=StubView(stub))["units"]}["U_FAIR"]
        assert loose["verdict"] == "OFF-PATH" and any("allowed fairness pointer" in n for n in loose["notes"]), loose
        man["ask_fragments"][1]["delegation_quote"] = "the answer is in Odd's thread from last week"
        (td / "Working_Files" / MANIFEST_NAMES[0]).write_text(json.dumps(man))
        named = {u["id"]: u for u in evaluate(td, view=StubView(stub))["units"]}["U_FAIR"]
        assert [r["code"] for r in named["reasons"]] == ["pointer"], named
        # no prompt: the manifest supplies the names, and the report says so
        (td / "04_Prompt.txt").unlink()
        early = evaluate(td, view=StubView(stub))
        src = next(c["detail"] for c in early["checks"] if c["id"] == "exposure.sources")
        assert early["stage"] == "injection" and "no 04_Prompt.txt yet" in src, src
        assert "Orchid" in early["keywords"], early["keywords"]
        # no base data: nothing is OFF-PATH on trust
        blind = {u["id"]: u for u in evaluate(td, view=NullView("self-test"))["units"]}
        assert blind["U_OFF"]["verdict"] == "UNVERIFIED" and blind["U_KEYWORD"]["verdict"] == "EXPOSED", blind["U_OFF"]
        assert blind["U_BASE"]["verdict"] == "UNVERIFIED", blind["U_BASE"]
        # --write binds and stores; a missing budget fails the bound check
        out = write_report(td, early)
        assert out.name == OUT_NAME and json.loads(out.read_text())["bound_to"] == early["bound_to"]
        (td / "Working_Files" / BUDGET_NAME).unlink()
        gone = evaluate(td, view=StubView(stub))
        assert gone["verdict"] == "FAIL" and gone["checks"][0]["id"] == "exposure.bound", gone["checks"][0]
    print("self-test: ok (each reason code on a planted record, an OFF-PATH reply, the allowed fairness pointer and "
          "its exposed twin, UNVERIFIED for a missing id and for no base data, a base decider read through the stub "
          "universe, realism skipped, no-prompt keywords from the manifest, sha256 binding, determinism, --write)")


# ------------------------------------------------------------------ CLI

def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="path_exposure.py", description="is each planned miss off the swept path?")
    ap.add_argument("--self-test", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    c = sub.add_parser("check", help="judge the units of one task folder")
    c.add_argument("--task-dir", type=Path, required=True)
    c.add_argument("--json", action="store_true")
    c.add_argument("--write", action="store_true", help=f"store Working_Files/{OUT_NAME}")
    c.add_argument("--today", help="YYYY-MM-DD recorded in the stored report (no clock is read)")
    b = sub.add_parser("backtest", help="replay stored revisions of archived tasks")
    b.add_argument("--units", type=Path, required=True)
    b.add_argument("--json", action="store_true")
    b.add_argument("--out", type=Path, help="also store the backtest JSON here (scratch only)")
    a = ap.parse_args(argv)
    if a.self_test:
        _self_test()
        return 0
    if a.cmd == "check":
        if not a.task_dir.is_dir():
            print(f"path_exposure: {a.task_dir} is not a folder", file=sys.stderr)
            return 2
        if a.today and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.today):
            print("path_exposure: --today takes YYYY-MM-DD", file=sys.stderr)
            return 2
        res = evaluate(a.task_dir, today=a.today)
        if a.write:
            res["stored_as"] = _rel(write_report(a.task_dir, res), a.task_dir)
        print(json.dumps(res, indent=1, sort_keys=True, ensure_ascii=False) if a.json else to_text(res))
        return 1 if res["verdict"] == "FAIL" else 0
    if a.cmd == "backtest":
        if not a.units.is_file():
            print(f"path_exposure: {a.units} not found", file=sys.stderr)
            return 2
        rep = backtest(a.units)
        if a.out:
            from task_context import refuse_read_only
            refuse_read_only(a.out, "The backtest report")
            a.out.parent.mkdir(parents=True, exist_ok=True)
            a.out.write_text(json.dumps(rep, indent=1, sort_keys=True, ensure_ascii=False) + "\n")
        print(json.dumps(rep, indent=1, sort_keys=True, ensure_ascii=False) if a.json else backtest_text(rep))
        return 0
    ap.print_usage(sys.stderr)
    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"path_exposure: {error}", file=sys.stderr)
        raise SystemExit(2)

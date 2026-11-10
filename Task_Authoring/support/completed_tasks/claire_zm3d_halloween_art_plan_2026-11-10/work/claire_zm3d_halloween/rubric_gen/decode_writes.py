#!/usr/bin/env python3
"""decode_writes.py - decode every WRITE of the saved Opus runs into one normalized JSON for a local rubric grader.

Rebuild (from /Users/sumit/Source/OC):
  export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputsN2
  ~/.local/bin/python3.12 -B Task_Authoring/task_inputsN2/Working_Files/rubric_gen/decode_writes.py

Reads 06_PreCheck_Trajectory/, 07_Baseline_Trajectories/, 01_Universe_Inject.sql and Working_Files/run_forensics/rev*/ only.
Writes only baseline_writes.json next to this script. Never executes SQL. tools/trajectory_ledger.py supplies the event
index, counted calls, provenance and revision binding; everything else is parsed here because the ledger's write
classifier does not know gsheets_values_batch_clear, gsheets_batch_update, gdocs_batch_update or the create-call body.

Top-level keys are run labels only, so a grader can loop over the file. Definitions:
  event / order index   0-based index into the export array (same numbering as trajectory_ledger.py)
  reads                 marker found in a RESULT of a service read tool (or of a Bash call that parses a spilled service
                        result). Matching decodes nested JSON and base64 mail bodies, ignores case, normalizes curly
                        quotes, HTML entities and whitespace. Not counted: results of write calls, Bash/Read output of the
                        run's own drafts, and read-backs of text the run itself wrote earlier.
  reads_anchor          same test on a longer quote from the intended record, so a literal hit on another record shows up
  reads_detail          per marker: tools, first event, snippet, what was excluded, and available_in_run (false = the record
                        is not in the SQL revision that run saw, so a false in reads is not a miss)
  sheets[].tabs         final grid after applying every successful write in call order (blank cells are "")
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True  # nothing lands in tools/__pycache__ even without -B

import argparse
import base64
import binascii
import collections
import hashlib
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASK = HERE.parents[1]
BUNDLE = TASK.parent
sys.path.insert(0, str(BUNDLE / "tools"))
import difficulty_stats as ds  # noqa: E402
import trajectory_ledger as tl  # noqa: E402

OUT = HERE / "baseline_writes.json"
RUNS = [(f"run-{n}", f"07_Baseline_Trajectories/trajectory-run-{n}.json") for n in range(1, 7)]
RUNS += [("precheck", "06_PreCheck_Trajectory/trajectory.json"),
         ("precheck-rev3", "06_PreCheck_Trajectory/trajectory-run-1 (1).json")]
REQUESTED_SEVEN = {f"run-{n}" for n in range(1, 7)} | {"precheck"}

LEONARD_CHANNEL, LEONARD_TS = "C06DJBJL798", "1759269913.882683"
USER_MAP = {"usr_c77c50cc15c5342d": "marcus.bennett@harmonygames.co",
            "usr_8140f09bf9f1b94c": "julia.lawson@harmonygames.co",
            "usr_51f5f16d46e8cf55": "martin.walsh@harmonygames.co"}

# marker -> (intended record, longer quote from that record)
MARKERS = {
    "manual review": ("Frederick's Oct 10 reply", "putting every new Android creative through manual review"),
    "ad statics": ("Martin's vacation post", "takes the ad statics while I"),
    "re-recorded 3": ("Marcus's note", "re-recorded 3 of the old ua cuts"),
    "old zombies on the packs": ("Frederick's Trello comment on end card 001", "end card 001 still has the old zombies on the packs"),
    "still running on iOS UK": ("Frederick's comment on the Halloween push card", "is still running on iOS UK and is still our best CPI there"),
    "Unity retention restart": ("Sep 29 mail", "Unity retention restart"),
    "We can't ship these": ("Robert's rejection", "We can't ship these, they need doing again from the Sep 16 one"),
    "background music is baked in": ("Aug 13 thread", "cut and paste different video segments as the background music is baked in"),
    "no tickets needed": ("Leonard store reply", "whatever is already exported is done so no tickets needed"),
    "not for the app icon": ("Robert's icon reply", "Nice for an event, but not for the app icon"),
    "Merge cut": ("release calendar", "Merge cut is Thu Oct 16, 12:00 PT"),
    "the newest capture is the one that counts": ("deck", "If a later capture has replaced it, the newest capture is the one that counts"),
}

WRITE_TOOLS = {"linear_create_comment", "linear_update_issue", "linear_create_issue", "gdrive_share_file",
               "gsheets_create_spreadsheet", "gsheets_values_update", "gsheets_values_append",
               "gsheets_values_batch_update", "gsheets_batch_update", "gsheets_values_batch_clear", "gsheets_values_clear",
               "gdocs_create_document", "gdocs_batch_update", "slack_send_message"}
LOCAL_TOOLS = {"Bash", "Read", "Agent", "Task", "Write", "Edit", "Grep", "Glob", "TodoWrite", "ToolSearch"}
RX_WRITEISH = re.compile(r"create|update|delete|send|share|clear|append|move|remove|post|reply|upload|copy|rename|trash|add_|insert|edit")
RX_B64 = re.compile(r"[A-Za-z0-9+/_-]{24,}={0,2}")
RX_CELL = re.compile(r"^\$?([A-Za-z]{1,3})\$?(\d+)$")
FORMAT_ONLY_DOC = {"updateParagraphStyle", "updateTextStyle", "createParagraphBullets", "deleteParagraphBullets",
                   "updateDocumentStyle", "updateSectionStyle"}
FORMAT_ONLY_SHEET = {"repeatCell", "updateDimensionProperties", "autoResizeDimensions", "setBasicFilter", "addConditionalFormatRule",
                     "updateBorders", "mergeCells", "setDataValidation", "addBanding", "addProtectedRange"}


# ------------------------------------------------------------------ text helpers

def norm(s: str) -> str:
    s = html.unescape(str(s)).translate({0x2019: "'", 0x2018: "'", 0x201C: '"', 0x201D: '"', 0xA0: " "})
    return re.sub(r"\s+", " ", s).casefold()


def b64_text(s: str):
    """Text of a whole-string base64 / base64url value (mail bodies), else None."""
    t = re.sub(r"\s+", "", s)
    if len(t) < 24 or not RX_B64.fullmatch(t):
        return None
    try:
        raw = base64.urlsafe_b64decode(t.replace("+", "-").replace("/", "_") + "=" * (-len(t) % 4))
        out = raw.decode("utf-8")
    except (binascii.Error, ValueError, UnicodeDecodeError):
        return None
    good = sum(c.isprintable() or c in "\r\n\t" for c in out)
    return out if out and good / len(out) > 0.95 else None


def leaves(data):
    for s in tl.strings(data):
        yield s, "plain"
        d = b64_text(s)
        if d is not None:
            yield d, "base64"


def a1(row: int, col: int) -> str:
    letters, n = "", col + 1
    while n:
        n, r = divmod(n - 1, 26)
        letters = chr(65 + r) + letters
    return f"{letters}{row + 1}"


def col_index(letters: str) -> int:
    n = 0
    for ch in letters.upper():
        n = n * 26 + ord(ch) - 64
    return n - 1


def parse_range(rng: str):
    """(tab or None, start_row, start_col, end_row or None, end_col or None); cells 0-based, ends inclusive."""
    rng = str(rng).strip()
    tab, cells = None, rng
    if "!" in rng:
        tab, cells = rng.rsplit("!", 1)
        tab = tab.strip()
        if tab.startswith("'") and tab.endswith("'"):
            tab = tab[1:-1].replace("''", "'")
    elif not re.match(r"^\$?[A-Za-z]{1,3}\$?\d*(:\$?[A-Za-z]{1,3}\$?\d*)?$", rng):
        return rng, 0, 0, None, None  # a bare tab name
    first, _, last = cells.partition(":")
    m = RX_CELL.match(first)
    r0, c0 = (int(m.group(2)) - 1, col_index(m.group(1))) if m else (0, col_index(first) if first.isalpha() else 0)
    r1 = c1 = None
    if last:
        m2 = RX_CELL.match(last)
        if m2:
            r1, c1 = int(m2.group(2)) - 1, col_index(m2.group(1))
        elif last.isalpha():
            c1 = col_index(last)
    return tab, r0, c0, r1, c1


def utf16_pos(s: str, index16: int) -> int:
    """Python index of a UTF-16 code-unit offset (Docs indexes count UTF-16 units)."""
    units = 0
    for i, ch in enumerate(s):
        if units >= index16:
            return i
        units += 2 if ord(ch) > 0xFFFF else 1
    return len(s)


# ------------------------------------------------------------------ one run

class Decoder:
    def __init__(self, label: str, path: Path, sources: dict, candidates: list, current_label: str, current_sha: str,
                 revision_text: dict):
        self.label, self.path = label, path
        self.run = tl.load(path, label)
        self.sources, self.candidates = sources, candidates
        self.current_label, self.current_sha, self.revision_text = current_label, current_sha, revision_text
        self.notes: list = []
        self.docs: dict = {}
        self.sheets: dict = {}
        self.shares: list = []
        self.comments: dict = {}
        self.updates: dict = {}
        self.tickets: list = []
        self.slack: list = []
        self.order: list = []
        self.other_ids: dict = {}
        self.own: list = []  # (event, normalized text the run wrote)
        self.lookup = self._user_lookup()

    # results -------------------------------------------------------
    def res(self, c):
        return self.run.results.get(c["id"])

    def ok(self, c) -> bool:
        return not tl.failed(self.res(c))

    def data(self, c):
        """The tool's own JSON: tl.unpack also turns numeric-looking strings into numbers, which breaks Slack ts values."""
        r = self.res(c)
        if not r:
            return None
        block = next((b for b in tl.blocks(self.run.events[r["event"]]) if b.get("tool_use_id") == c["id"]), {})
        content = block.get("content")
        if isinstance(content, list):
            content = "".join(x.get("text", "") for x in content if isinstance(x, dict))
        out = content
        for _ in range(2):
            if isinstance(out, str):
                try:
                    out = json.loads(out)
                except ValueError:
                    break
            if isinstance(out, dict) and set(out) == {"result"}:
                out = out["result"]
        return out

    def err(self, c):
        return None if self.ok(c) else str(self.data(c))[:300]

    def _user_lookup(self) -> dict:
        out = {}

        def walk(v):
            if isinstance(v, dict):
                uid, email = v.get("id"), v.get("email")
                if isinstance(uid, str) and uid.startswith("usr_") and isinstance(email, str):
                    out[uid] = email
                if isinstance(v.get("assigneeId"), str) and isinstance(v.get("assignee"), str):
                    out.setdefault(v["assigneeId"], v["assignee"])
                for x in v.values():
                    walk(x)
            elif isinstance(v, list):
                for x in v:
                    walk(x)

        for c in self.run.calls:
            n = tl.short(c["name"])
            if n in ("linear_list_users", "linear_update_issue", "linear_create_issue", "linear_list_issues", "linear_get_issue"):
                walk(self.data(c))
        return out

    def resolve(self, raw):
        if raw is None:
            return None
        s = str(raw).strip()
        if s in USER_MAP:
            return USER_MAP[s]
        if "@" in s:
            return s.lower()
        if s in self.lookup:
            self.other_ids.setdefault(s, {"email": self.lookup[s], "source": "run lookups"})
            return self.lookup[s]
        key = re.sub(r"[^a-z]", ".", s.lower())
        hits = sorted({e for e in list(USER_MAP.values()) + list(self.lookup.values()) if isinstance(e, str) and e.lower().startswith(key)})
        if len(hits) == 1:
            return hits[0]
        self.notes.append(f"assignee {s!r} could not be resolved to one email (matches: {hits})")
        return None

    def track_ids(self, d):
        if isinstance(d, dict):
            uid = d.get("assigneeId")
            if isinstance(uid, str) and uid not in USER_MAP:
                self.other_ids.setdefault(uid, {"email": self.lookup.get(uid), "source": "write result"})

    def log(self, c, target: str):
        self.order.append(f"{c['event']} {tl.short(c['name'])} {target}" + ("" if self.ok(c) else " [FAILED]"))

    # writes --------------------------------------------------------
    def walk(self):
        known_read = collections.Counter()
        for c in self.run.calls:
            n = tl.short(c["name"])
            if n in WRITE_TOOLS:
                if c.get("context") != "main":
                    self.notes.append(f"write {n} at event {c['event']} ran in a subagent")
                getattr(self, "w_" + n, self.w_unhandled)(c, c["input"] or {})
            elif n not in LOCAL_TOOLS:
                known_read[n] += 1
                if RX_WRITEISH.search(n) and tl.is_write(c["name"]):
                    self.notes.append(f"unhandled write-looking tool {n} at event {c['event']}")
                if n in ("gsheets_values_get", "gsheets_values_batch_get"):
                    self.readback(c)
                elif n == "gdrive_get_file_metadata":
                    self.parents(c)

    def w_unhandled(self, c, q):
        self.notes.append(f"no decoder for {tl.short(c['name'])} at event {c['event']}")
        self.log(c, json.dumps(q)[:80])

    def w_linear_create_comment(self, c, q):
        key = str(q.get("issueId") or q.get("issue_id") or q.get("id")).upper()
        d = self.data(c) if self.ok(c) else {}
        self.comments.setdefault(key, []).append({"body": q.get("body"), "success": self.ok(c), "event": c["event"],
                                                  "comment_id": d.get("id") if isinstance(d, dict) else None, "error": self.err(c)})
        self.own.append((c["event"], norm(q.get("body") or "")))
        self.log(c, key)

    def w_linear_update_issue(self, c, q):
        key = str(q.get("id") or q.get("issueId")).upper()
        d = self.data(c) if self.ok(c) else {}
        d = d if isinstance(d, dict) else {}
        self.track_ids(d)
        other = {k: v for k, v in q.items() if k not in ("id", "issueId", "assignee", "dueDate", "state")}
        raw = q.get("assignee")
        if isinstance(raw, str) and raw.startswith("usr_") and raw not in USER_MAP:
            self.other_ids.setdefault(raw, {"email": self.lookup.get(raw), "source": "update argument"})
        self.updates.setdefault(key, []).append({
            "assignee": raw, "assignee_email": self.resolve(raw), "dueDate": q.get("dueDate"), "state": q.get("state"),
            "other": other, "success": self.ok(c), "event": c["event"], "error": self.err(c),
            "result": {k: d.get(k) for k in ("assignee", "assigneeId", "dueDate", "status", "statusType")}})
        if "patch" in q or "description" in q:
            for t in self.tickets:
                if t["identifier"] == key and d.get("description") is not None:
                    t["description_final"] = d["description"]
            self.own.append((c["event"], norm(json.dumps(q, ensure_ascii=False))))
        self.log(c, key)

    def w_linear_create_issue(self, c, q):
        d = self.data(c) if self.ok(c) else {}
        d = d if isinstance(d, dict) else {}
        self.track_ids(d)
        ident = d.get("identifier") or d.get("id")
        self.tickets.append({
            "title": q.get("title"), "description": q.get("description"), "description_final": q.get("description"),
            "team": q.get("team"), "assignee": q.get("assignee"), "assignee_email": self.resolve(q.get("assignee")),
            "dueDate": q.get("dueDate"), "state": q.get("state"), "priority": q.get("priority"),
            "other": {k: v for k, v in q.items() if k not in ("title", "description", "team", "assignee", "dueDate", "state", "priority")},
            "identifier": ident, "success": self.ok(c), "event": c["event"], "error": self.err(c),
            "result": {k: d.get(k) for k in ("assignee", "assigneeId", "dueDate", "status", "statusType", "team", "url")}})
        self.own.append((c["event"], norm((q.get("title") or "") + " " + (q.get("description") or ""))))
        self.log(c, str(ident or q.get("title")))

    def w_gdrive_share_file(self, c, q):
        d = self.data(c) if self.ok(c) else {}
        d = d if isinstance(d, dict) else {}
        f = d.get("file") or {}
        fid = q.get("fileId")
        mime = str(f.get("mimeType") or "")
        kind = ("doc" if fid in self.docs or "document" in mime else "sheet" if fid in self.sheets or "spreadsheet" in mime else "other")
        if kind == "other":
            self.notes.append(f"share at event {c['event']} targets a file this run did not create: {fid}")
        link = f.get("webViewLink")
        if link and fid in self.docs:
            self.docs[fid]["url"] = link
        self.shares.append({"file_id": fid, "file_kind": kind, "email": q.get("emailAddress"), "role": q.get("role"),
                            "success": self.ok(c), "event": c["event"], "error": self.err(c)})
        self.log(c, f"{kind}:{fid} {q.get('emailAddress')} {q.get('role')}")

    def w_slack_send_message(self, c, q):
        d = self.data(c) if self.ok(c) else {}
        d = d if isinstance(d, dict) else {}
        text = q.get("message") if q.get("message") is not None else q.get("text")
        self.slack.append({"channel": q.get("channel_id") or q.get("channel"), "thread_ts": q.get("thread_ts"), "text": text,
                           "success": self.ok(c), "ts": d.get("ts"), "event": c["event"], "error": self.err(c)})
        self.own.append((c["event"], norm(text or "")))
        self.log(c, f"{q.get('channel_id') or q.get('channel')}/{q.get('thread_ts')}")

    # docs ----------------------------------------------------------
    def w_gdocs_create_document(self, c, q):
        d = self.data(c) if self.ok(c) else {}
        d = d if isinstance(d, dict) else {}
        did = d.get("documentId") or d.get("id")
        body = q.get("bodyText") or ""
        folder = q.get("parentId") or q.get("folderId") or q.get("folder") or (d.get("parents") or [None])[0]
        echoed = self.doc_echo(d)
        if echoed is not None and body and echoed.rstrip("\n") != body.rstrip("\n"):
            self.notes.append(f"doc create result body differs from bodyText at event {c['event']} ({len(echoed)} vs {len(body)} chars)")
        if self.ok(c):
            self.docs[did] = {"title": q.get("title"), "id": did, "url": f"https://docs.google.com/document/d/{did}/edit",
                              "folder": folder, "drive_parents": None, "created_event": c["event"], "created_with_body": bool(body), "body": body,
                              "body_at_create": body, "edits": []}
            if body:
                self.own.append((c["event"], norm(body)))
        self.log(c, str(did or q.get("title")))

    @staticmethod
    def doc_echo(d):
        content = ((d.get("body") or {}).get("content")) if isinstance(d, dict) else None
        if not isinstance(content, list):
            return None
        out = []
        for el in content:
            for pe in ((el or {}).get("paragraph") or {}).get("elements") or []:
                out.append(((pe or {}).get("textRun") or {}).get("content") or "")
        return "".join(out)

    def w_gdocs_batch_update(self, c, q):
        did = q.get("documentId")
        self.log(c, str(did))
        doc = self.docs.get(did)
        if doc is None:
            self.notes.append(f"gdocs_batch_update at event {c['event']} targets an unknown doc {did}")
            return
        reqs = tl._maybe_json(q.get("requests")) or []
        d = self.data(c) if self.ok(c) else {}
        replies = (d.get("replies") if isinstance(d, dict) else None) or []
        fmt = collections.Counter()
        for i, rq in enumerate(reqs):
            kind = next(iter(rq), None)
            v = rq.get(kind) or {}
            edit = {"event": c["event"], "kind": kind, "success": self.ok(c)}
            if kind in FORMAT_ONLY_DOC:
                fmt[kind] += 1
                continue
            if self.ok(c):
                b = doc["body"]
                if kind == "insertText":
                    text = v.get("text", "")
                    if "endOfSegmentLocation" in v:
                        pos = len(b)
                    else:
                        pos = utf16_pos(b, max(int((v.get("location") or {}).get("index", 1)) - 1, 0))
                    doc["body"] = b[:pos] + text + b[pos:]
                    edit.update(index=(v.get("location") or {}).get("index"), chars=len(text))
                    self.own.append((c["event"], norm(text)))
                elif kind == "replaceAllText":
                    ct = v.get("containsText") or {}
                    old, new = ct.get("text", ""), v.get("replaceText", "")
                    rx = re.compile(re.escape(old), 0 if ct.get("matchCase") else re.I)
                    doc["body"], n = rx.subn(lambda _m: new, b)
                    reply = (replies[i] if i < len(replies) else {}) or {}
                    reported = (reply.get("replaceAllText") or {}).get("occurrencesChanged")
                    edit.update(old=old, new=new, occurrences=n, reported_occurrences=reported)
                    if reported is not None and reported != n:
                        self.notes.append(f"replaceAllText {old!r} at event {c['event']}: applied {n}, tool reported {reported}")
                    self.own.append((c["event"], norm(new)))
                elif kind == "deleteContentRange":
                    rg = v.get("range") or {}
                    s0, s1 = utf16_pos(b, int(rg.get("startIndex", 1)) - 1), utf16_pos(b, int(rg.get("endIndex", 1)) - 1)
                    doc["body"] = b[:s0] + b[s1:]
                    edit.update(range=rg)
                else:
                    self.notes.append(f"gdocs_batch_update request {kind} at event {c['event']} not applied to the body")
            doc["edits"].append(edit)
        if fmt:
            doc["edits"].append({"event": c["event"], "kind": "format_only", "requests": dict(fmt), "success": self.ok(c)})

    # sheets --------------------------------------------------------
    def w_gsheets_create_spreadsheet(self, c, q):
        d = self.data(c) if self.ok(c) else {}
        d = d if isinstance(d, dict) else {}
        sid = d.get("spreadsheetId")
        self.log(c, str(sid or q.get("title")))
        if not self.ok(c):
            return
        names = [((s or {}).get("properties") or {}).get("title") for s in d.get("sheets") or []]
        names = [x for x in names if x] or [q.get("initialSheetTitle") or "Sheet1"]
        self.sheets[sid] = {"title": q.get("title"), "id": sid, "url": d.get("spreadsheetUrl"), "folder": (d.get("parents") or [None])[0], "drive_parents": None,
                            "created_event": c["event"], "order": list(names), "cells": {n: {} for n in names},
                            "writes": [], "merge_notes": [], "readback_checks": [], "last_read": {}}

    def sheet_for(self, c, q):
        s = self.sheets.get(q.get("spreadsheetId"))
        if s is None:
            self.notes.append(f"{tl.short(c['name'])} at event {c['event']} targets an unknown spreadsheet {q.get('spreadsheetId')}")
        return s

    def tab_for(self, s, tab, c):
        tab = tab or s["order"][0]
        if tab not in s["cells"]:
            s["merge_notes"].append(f"event {c['event']}: range names unknown tab {tab!r}; kept as its own tab")
            s["cells"][tab] = {}
            s["order"].append(tab)
        return tab

    def w_gsheets_batch_update(self, c, q):
        self.log(c, str(q.get("spreadsheetId")))
        s = self.sheet_for(c, q)
        if s is None:
            return
        reqs = tl._maybe_json(q.get("requests")) or []
        d = self.data(c) if self.ok(c) else {}
        replies = (d.get("replies") if isinstance(d, dict) else None) or []
        for i, rq in enumerate(reqs):
            kind = next(iter(rq), None)
            v = rq.get(kind) or {}
            if not self.ok(c):
                continue
            if kind == "addSheet":
                p = v.get("properties") or {}
                name = p.get("title") or (((replies[i] if i < len(replies) else {}) or {}).get("addSheet") or {}).get("properties", {}).get("title")
                idx = p.get("index")
                s["order"].insert(min(int(idx), len(s["order"])) if idx is not None else len(s["order"]), name)
                s["cells"][name] = {}
                s["writes"].append({"event": c["event"], "op": "addSheet", "tab": name, "index": idx})
            elif kind in FORMAT_ONLY_SHEET:
                s["writes"].append({"event": c["event"], "op": kind})
            else:
                s["merge_notes"].append(f"event {c['event']}: batch request {kind} not applied to the grid: {json.dumps(v)[:200]}")

    def put(self, s, c, rng, values, op):
        tab, r0, c0, _, _ = parse_range(rng)
        tab = self.tab_for(s, tab, c)
        cells = s["cells"][tab]
        width = 0
        for i, row in enumerate(values or []):
            row = row if isinstance(row, list) else [row]
            width = max(width, len(row))
            for j, v in enumerate(row):
                if v is None:
                    continue
                cells[(r0 + i, c0 + j)] = v
                s["last_read"].pop((tab, r0 + i, c0 + j), None)
                if isinstance(v, str):
                    self.own.append((c["event"], norm(v)))
        d = self.data(c) if self.ok(c) else {}
        rep = d.get("updatedRange") if isinstance(d, dict) else None
        s["writes"].append({"event": c["event"], "op": op, "range": rng, "rows": len(values or []), "cols": width,
                            "updatedRange": rep})
        return r0, c0, width

    def w_gsheets_values_update(self, c, q):
        self.log(c, f"{q.get('spreadsheetId')}!{q.get('range')}")
        s = self.sheet_for(c, q)
        if s is None or not self.ok(c):
            return
        self.put(s, c, q.get("range"), tl._maybe_json(q.get("values")) or [], "values_update")

    def w_gsheets_values_append(self, c, q):
        self.log(c, f"{q.get('spreadsheetId')}!{q.get('range')}")
        s = self.sheet_for(c, q)
        if s is None or not self.ok(c):
            return
        tab = self.tab_for(s, parse_range(q.get("range"))[0], c)
        next_row = max((r for r, _ in s["cells"][tab]), default=-1) + 1
        name = "'" + tab.replace("'", "''") + "'"
        self.put(s, c, f"{name}!A{next_row + 1}", tl._maybe_json(q.get("values")) or [], "values_append")

    def w_gsheets_values_batch_update(self, c, q):
        self.log(c, str(q.get("spreadsheetId")))
        s = self.sheet_for(c, q)
        if s is None or not self.ok(c):
            return
        for part in tl._maybe_json(q.get("data")) or []:
            self.put(s, c, part.get("range"), part.get("values") or [], "values_batch_update")

    def clear(self, s, c, rng):
        tab, r0, c0, r1, c1 = parse_range(rng)
        tab = self.tab_for(s, tab, c)
        cells = s["cells"][tab]
        gone = [k for k in cells if k[0] >= r0 and k[1] >= c0 and (r1 is None or k[0] <= r1) and (c1 is None or k[1] <= c1)]
        for k in gone:
            del cells[k]
            s["last_read"].pop((tab,) + k, None)
        s["writes"].append({"event": c["event"], "op": "values_clear", "range": rng, "cells_cleared": len(gone)})

    def w_gsheets_values_batch_clear(self, c, q):
        self.log(c, f"{q.get('spreadsheetId')}!{','.join(map(str, q.get('ranges') or []))}")
        s = self.sheet_for(c, q)
        if s is None or not self.ok(c):
            return
        for rng in q.get("ranges") or []:
            self.clear(s, c, rng)

    def w_gsheets_values_clear(self, c, q):
        self.log(c, f"{q.get('spreadsheetId')}!{q.get('range')}")
        s = self.sheet_for(c, q)
        if s is not None and self.ok(c):
            self.clear(s, c, q.get("range"))

    def parents(self, c):
        d = self.data(c)
        fid = (c["input"] or {}).get("fileId")
        target = self.docs.get(fid) or self.sheets.get(fid)
        if target is not None and isinstance(d, dict):
            target["drive_parents"] = d.get("parents")

    def readback(self, c):
        q = c["input"] or {}
        s = self.sheets.get(q.get("spreadsheetId"))
        d = self.data(c)
        if s is None or not isinstance(d, dict):
            return
        for part in d.get("valueRanges") or [{"range": q.get("range"), "values": d.get("values")}]:
            self.readback_range(s, c, part.get("range"), part.get("values") or [])

    def readback_range(self, s, c, rng, values):
        tab, r0, c0, _, _ = parse_range(rng)
        tab = tab or s["order"][0]
        cells = s["cells"].get(tab, {})
        compared, bad, formula = 0, [], 0
        for i, row in enumerate(values):
            for j, v in enumerate(row):
                key = (r0 + i, c0 + j)
                s["last_read"][(tab,) + key] = v
                mine = cells.get(key, "")
                if isinstance(mine, str) and mine.startswith("="):
                    formula += 1
                    continue
                compared += 1
                if str(mine) != str(v):
                    bad.append({"cell": a1(*key), "written": mine, "read": v})
        s["readback_checks"].append({"event": c["event"], "range": rng, "cells_compared": compared,
                                     "formula_cells_skipped": formula, "mismatches": bad[:10]})

    def finish_sheet(self, s) -> dict:
        tabs, counts, formulas = {}, {}, []
        for name in s["order"]:
            cells = s["cells"].get(name, {})
            used = {k: v for k, v in cells.items() if v != ""}
            nrows = max((r for r, _ in used), default=-1) + 1
            rows = []
            for r in range(nrows):
                width = max((cc for rr, cc in used if rr == r), default=-1) + 1
                rows.append([cells.get((r, cc), "") for cc in range(width)])
            tabs[name] = rows
            nonblank = sum(bool(x) for x in rows)
            counts[name] = {"rows_total": nonblank, "data_rows": max(nonblank - 1, 0), "max_cols": max((len(x) for x in rows), default=0)}
            for (r, cc), v in sorted(cells.items()):
                if isinstance(v, str) and v.startswith("="):
                    formulas.append({"tab": name, "cell": a1(r, cc), "formula": v, "last_read_value": s["last_read"].get((name, r, cc))})
        for w in s["writes"]:
            rep = w.get("updatedRange")
            if rep and w.get("rows"):
                t, r0, c0, r1, c1 = parse_range(rep)
                if r1 is not None and r1 - r0 + 1 != w["rows"]:
                    s["merge_notes"].append(f"event {w['event']}: {w['rows']} rows written, tool reported {rep}")
        if formulas:
            unread = [f"{f['tab']}!{f['cell']}" for f in formulas if f["last_read_value"] is None]
            s["merge_notes"].append(f"{len(formulas)} final cell(s) hold formulas, stored as written; not read back after their last write: {unread}")
        return {"title": s["title"], "id": s["id"], "url": s["url"], "folder": s["folder"], "drive_parents": s["drive_parents"],
                "created_event": s["created_event"],
                "tab_order": s["order"], "tabs": tabs, "row_counts": counts, "formula_cells_final": formulas,
                "writes": s["writes"], "readback_checks": s["readback_checks"], "merge_notes": s["merge_notes"]}

    # reads ---------------------------------------------------------
    def reads(self, run_rev):
        needles = {m: (norm(m), norm(MARKERS[m][1])) for m in MARKERS}
        hits = {m: [] for m in MARKERS}
        anchors = {m: [] for m in MARKERS}
        excluded = {m: collections.Counter() for m in MARKERS}
        for c in self.run.calls:
            r = self.res(c)
            if not r:
                continue
            n = tl.short(c["name"])
            if n in WRITE_TOOLS:
                cls = "write_echo"
            elif n in LOCAL_TOOLS:
                cls = "spill_parse" if n == "Bash" and "tool-results" in str((c["input"] or {}).get("command")) and c.get("context") == "main" else "local_output"
            else:
                cls = "service_read"
            for text, enc in leaves(r["data"]):
                t = norm(text)
                for m, (needle, anchor) in needles.items():
                    p = t.find(needle)
                    if p < 0:
                        continue
                    while p >= 0:
                        win = t[max(0, p - 30):p + len(needle) + 30]
                        klass = cls
                        if cls in ("service_read", "spill_parse") and any(ev < c["event"] and win in own for ev, own in self.own):
                            klass = "own_readback"
                        if klass in ("service_read", "spill_parse"):
                            hits[m].append({"event": c["event"], "tool": n, "class": klass, "encoding": enc,
                                            "snippet": text[max(0, self._raw_pos(text, needle) - 70):self._raw_pos(text, needle) + len(m) + 70].replace("\n", " ")})
                            if anchor in t:
                                anchors[m].append(c["event"])
                        else:
                            excluded[m][klass] += 1
                        p = t.find(needle, p + len(needle))
            # a spilled result keeps its full text in tool_use_result; the model only saw the pointer plus what Bash printed
            full = self.run.events[r["event"]].get("tool_use_result")
            if isinstance(full, dict) and "exceeds maximum" in str(full.get("content"))[:200]:
                for text, _ in leaves(tl.unpack(full.get("structuredContent"))):
                    t = norm(text)
                    for m, (needle, _anchor) in needles.items():
                        if needle in t:
                            excluded[m]["spilled_full_result"] += 1
        flags = {m: bool(hits[m]) for m in MARKERS}
        anchor_flags = {m: bool(anchors[m]) for m in MARKERS}
        detail = {}
        for m in MARKERS:
            revs = {k: self._in_sql(m, v) for k, v in self.revision_text.items()}
            where = sorted(k for k, v in revs.items() if v)
            seen = hits[m]
            detail[m] = {"record": MARKERS[m][0], "anchor": MARKERS[m][1], "hits": len(seen),
                         "first_event": seen[0]["event"] if seen else None,
                         "tools": sorted({h["tool"] for h in seen}), "anchor_events": sorted(set(anchors[m]))[:6],
                         "encodings": sorted({h["encoding"] for h in seen}), "first_snippet": seen[0]["snippet"] if seen else None,
                         "excluded_hits": dict(excluded[m]), "in_sql_revisions": where,
                         "available_in_run": (not where) or run_rev in where}
        return flags, anchor_flags, detail

    @staticmethod
    def _raw_pos(text: str, needle: str) -> int:
        p = text.casefold().find(needle)
        return max(p, 0)

    @staticmethod
    def _in_sql(marker: str, sql: str) -> bool:
        low = sql.casefold()
        return marker.casefold() in low or marker.replace("'", "''").casefold() in low

    # meta ----------------------------------------------------------
    def sql_meta(self):
        b = tl.binding(self.run, self.candidates)
        cur = next((o for o in b["candidates"] if self.current_label in o["labels"]), {})
        out = {"current_sql_sha256": self.current_sha, "current_revision": self.current_label, "verdict": b["verdict"],
               "bound_to": b["bound_to"], "why": b["why"],
               "current_only_needles_seen": cur.get("discriminating_seen", 0),
               "current_only_needles_total": cur.get("unique_ids", 0) + cur.get("unique_text_windows", 0),
               "shared_needles_seen": cur.get("shared_seen", 0), "evidence_keys": (cur.get("seen_window_keys") or [])[:6]}
        out["matches_current_sql"] = bool(b["bound_to"] and self.current_label in b["bound_to"])
        if not out["matches_current_sql"]:
            older = [(k, v) for k, v in self.candidates if k != self.current_label]
            if len(older) > 1:
                b2 = tl.binding(self.run, older)
                out["older_revisions_binding"] = {"verdict": b2["verdict"], "bound_to": b2["bound_to"],
                                                  "discriminating_seen": b2["evidence"]["discriminating_seen"]}
        return out

    def meta(self):
        run = self.run
        counts = ds.count_tool_calls(run.events)
        prov = tl.provenance(run, tl.briefs(run))
        val = tl.validity(run, None)
        init = next((e for e in run.events if e.get("type") == "system" and e.get("subtype") == "init"), {})
        sha = self.sources[self.label]["sha256"]
        subs = []
        for c in run.calls:
            if tl.short(c["name"]) in ("Agent", "Task"):
                inner = [x for x in run.calls if x.get("parent") == c["id"]]
                subs.append({"event": c["event"], "description": (c["input"] or {}).get("description"), "failed": tl.failed(self.res(c)),
                             "result": str(self.data(c))[:160], "inner_calls": dict(collections.Counter(tl.short(x["name"]) for x in inner)),
                             "inner_writes": sum(tl.short(x["name"]) in WRITE_TOOLS for x in inner)})
        return {"label": self.label, "source_file": self.sources[self.label]["file"], "sha256": sha,
                "duplicate_files": self.sources[self.label]["duplicates"], "in_requested_seven": self.label in REQUESTED_SEVEN,
                "model": prov.get("init_model"), "models": (prov.get("model_check") or {}).get("models"),
                "session_id": init.get("session_id"), "events": len(run.events), "total_tool_calls": counts["raw"],
                "service_calls": counts["service"], "counted_calls": counts["counted"], "blocked_calls": counts["blocked"],
                "repeat_calls": counts["repeats"], "status": val.get("status"), "sql": self.sql_meta(),
                "spilled_results": [{k: x.get(k) for k in ("event", "tool")} for x in val.get("spilled_results") or []],
                "error_results": [{"event": x.get("event"), "tool": x.get("tool")} for x in val.get("error_results") or []],
                "compactions": val.get("compactions"), "subagents": subs,
                "order_index": "0-based event index in the export (trajectory_ledger numbering)"}

    def final_response(self) -> str:
        text = ""
        for e in reversed(self.run.events):
            if e.get("type") == "assistant" and not e.get("parent_tool_use_id"):
                parts = [b.get("text", "") for b in tl.blocks(e) if b.get("type") == "text"]
                if parts:
                    text = "\n".join(parts)
                    break
        res = next((e for e in reversed(self.run.events) if e.get("type") == "result"), {})
        rt = res.get("result")
        if isinstance(rt, str) and rt.strip() and rt.strip() != text.strip():
            self.notes.append("final assistant text differs from the result event; the result event text is used")
            return rt
        return text

    def summary(self, docs, sheets):
        comments_ok = sum(x["success"] for v in self.comments.values() for x in v)
        calls = sum(len(v) for v in self.comments.values())
        by = collections.Counter()
        for v in self.updates.values():
            for u in v:
                if u["assignee"] is not None and u["success"]:
                    by[u["assignee_email"]] += 1
        doc_ids = [d["id"] for d in docs]
        sheet_ids = [s["id"] for s in sheets]
        replies = [p for p in self.slack if p["channel"] == LEONARD_CHANNEL and p["thread_ts"] == LEONARD_TS and p["success"]]
        text = "\n".join(p["text"] or "" for p in replies)
        has_doc = any(f"docs.google.com/document/d/{i}" in text for i in doc_ids)
        has_sheet = any(f"docs.google.com/spreadsheets/d/{i}" in text for i in sheet_ids)
        return {"comment_calls": calls, "comments_ok": comments_ok, "comments_failed": calls - comments_ok,
                "tickets_commented": sum(any(x["success"] for x in v) for v in self.comments.values()),
                "tickets_with_only_failed_comments": sorted(k for k, v in self.comments.items() if not any(x["success"] for x in v)),
                "tickets_with_several_ok_comments": sorted(k for k, v in self.comments.items() if sum(x["success"] for x in v) > 1),
                "assignments": dict(by), "tickets_updated": len(self.updates),
                "shares_ok": sum(s["success"] for s in self.shares), "shares_failed": sum(not s["success"] for s in self.shares),
                "new_tickets": sum(t["success"] for t in self.tickets), "slack_posts": len(self.slack),
                "thread_reply_posted": bool(replies), "thread_reply_has_doc_link": has_doc, "thread_reply_has_sheet_link": has_sheet,
                "thread_reply_both_links": has_doc and has_sheet,
                "tracker_rows": {s["title"]: {k: v["data_rows"] for k, v in s["row_counts"].items()} for s in sheets}}

    def build(self) -> dict:
        self.walk()
        sheets = [self.finish_sheet(s) for s in self.sheets.values()]
        docs = []
        for d in self.docs.values():
            d = dict(d)
            d["body_changed_after_create"] = d["body"] != d["body_at_create"]
            docs.append(d)
        meta = self.meta()
        sql = meta["sql"]
        bound = sql["bound_to"] or (sql.get("older_revisions_binding") or {}).get("bound_to") or [None]
        meta["revision"] = bound[0]
        meta["matches_current_sql"] = sql["matches_current_sql"]
        flags, anchors, detail = self.reads(bound[0])
        out = {"meta": meta, "reads": flags, "reads_anchor": anchors, "reads_detail": detail, "doc": docs, "sheets": sheets,
               "shares": self.shares, "comments": self.comments, "updates": self.updates, "new_tickets": self.tickets,
               "slack_posts": self.slack, "order": self.order, "final_response": self.final_response()}
        out["summary"] = self.summary(docs, sheets)
        out["meta"]["other_user_ids"] = self.other_ids
        out["meta"]["decode_notes"] = self.notes + [f"{s['title']}: {n}" for s in sheets for n in s["merge_notes"]]
        return out


# ------------------------------------------------------------------ whole set

def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sources() -> dict:
    """Every saved export hashed; chosen runs carry their byte-identical copies, and a copy is never its own run."""
    found = {}
    for folder in ("06_PreCheck_Trajectory", "07_Baseline_Trajectories"):
        for p in sorted((TASK / folder).glob("*.json")):
            found[str(p.relative_to(TASK))] = sha256(p)
    out, claimed = {}, set()
    for label, rel in RUNS:
        sha = found[rel]
        if sha in claimed:
            raise SystemExit(f"{label}: {rel} duplicates a run already counted")
        claimed.add(sha)
        out[label] = {"file": rel, "sha256": sha, "duplicates": sorted(k for k, v in found.items() if v == sha and k != rel)}
    stray = sorted(k for k, v in found.items() if v not in claimed)
    if stray:
        raise SystemExit(f"export(s) not mapped to a run label: {stray}")
    return out


def revisions():
    text = {}
    for p in sorted((TASK / "Working_Files" / "run_forensics").glob("rev*/01_Universe_Inject.sql")):
        text[p.parent.name] = p.read_text(errors="replace")
    current = (TASK / "01_Universe_Inject.sql").read_text(errors="replace")
    sha = hashlib.sha256(current.encode()).hexdigest()
    label = next((k for k, v in text.items() if v == current), None)
    if label is None:
        label = "current"
        text[label] = current
    ordered = sorted(text, key=lambda k: (k != label, k))
    return [(k, text[k]) for k in ordered], label, sha, text


def main(argv) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=OUT)
    a = ap.parse_args(argv)
    if a.out.resolve().parent != HERE:
        raise SystemExit("--out must stay in Working_Files/rubric_gen/")
    src = sources()
    cands, label, sha, text = revisions()
    data = {}
    for lab, rel in RUNS:
        data[lab] = Decoder(lab, TASK / rel, src, cands, label, sha, text).build()
    a.out.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for lab, d in data.items():
        s, m = d["summary"], d["meta"]
        print(f"{lab}: calls={m['total_tool_calls']} counted={m['counted_calls']} sql={m['sql']['verdict']}:{m['sql']['bound_to']} "
              f"comments={s['comments_ok']}/{s['comment_calls']} on {s['tickets_commented']} assign={s['assignments']} shares={s['shares_ok']} "
              f"new={s['new_tickets']} thread={s['thread_reply_posted']} both={s['thread_reply_both_links']} rows={s['tracker_rows']}")
        for n in m["decode_notes"]:
            print("   note:", n)
    print(f"wrote {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""gradable_surface.py - the gradable surface: what a task's deliverables make gradable, and its validator.

One owner for the surface file `Working_Files/01_Gradable_Surface.json` (plan §4.3, scenario S6b): the fact slots a
run's deliverables can be graded on before any rubric or verifier exists. /create-scenario writes the file and owns it.
/create-injection never rewrites it, because that would make the scenario certificate stale: the solver's expected
value per slot and the mutants that flip it go into Working_Files/01c_Preflight_Report.json (tools/preflight_report.py).
The geometry check, the forecast, surface_grader.py and /create-rubric-writing read it. Read-only on its inputs, stdlib
only, never executes SQL.

File shape:
  {"kind": "GRADABLE_SURFACE", "version": 1, "task": ..., "revision": ..., "sql_sha256": ... (optional provenance),
   "classes": ["READY", "WATCH", "HOLD"],                                         (class vocabulary for totals)
   "truth_fields": {"class": "handoff class", "groups": "groups"},                (where the solver rows keep them)
   "deliverables": {name: {"kind": "table" | "text" | "json_text" | "calls", ...}},
   "slots": [{id, title, weight, work_kind, work_reason, class, selector, fact_id?, role?, group?, volume_for?,
              singled_out_by?, mechanisms?, flipped_by?, incorporating_span?, accepted_outcomes?, gradable?}]}

  deliverables  table: name_regex, key_column, key_regex, columns, class_column, reason_column, comparators
                       ({column: issue_key | pr_number | sha_prefix | yes_no | norm}), missing_values
                text:  tool (linear_update_issue), issue, key_regex, groups [[group, heading pattern], ...]
                json_text / calls: tool - the write calls' inputs as text (slides, mail, Slack) or as calls (sharing)
  selector      ["field", key, column] · ["total", class] · ["printed_total", class] · ["group_count", group] ·
                ["group_size", group] · ["group_key", key, group] · ["groups_of", key] · ["sole_reason", key, group] ·
                ["reason_matches", key, regex] · ["tracker_lists", heading_regex, key] ·
                ["tracker_count", heading_regex, n] · ["text", deliverable, regex] · ["link", deliverable] ·
                ["delivery", name, *args]  (the selector vocabulary of support/analysis/season_pass_runs.py)
  class         direct (one record's value) · aggregate (totals, group counts) · write_content (text a write
                carries) · delivery (the write happened as required). Delivery slots fail only at a base rate and
                never count as designed difficulty.
  role          sample (one of <= 5 per spot-check group) · exception (a member an incorporated authority singles
                out: singled_out_by names it) · volume (the output-volume row: volume_for lists its groups) · core
  work_kind     lookup (1) · interpretation, calculation, comparison, limited_reconciliation (3) ·
                multi_source_reconciliation, deeper_reasoning, cross_modal, tracing (5) - QC Spec V2 weights
  mechanisms    the rule ids (mechanism_portfolio ids) the scenario declares can flip the slot; flipped_by is the same
                declaration by mutant id (rule:<id>, degrade:<op>). The solver-computed list is in the preflight report.
  gradable      false = surface_grader.py cannot decode the slot deterministically (free text): UNGRADED, never
                guessed. It still needs rubric coverage.

Validation (S6b; every FAIL blocks `surface.valid`, and each finding carries its family's basis, FAMILY_BASIS):
  structure     known kind/version, unique slot ids, known selector kinds with their arguments, deliverables exist
  weights       1/3/5 and equal to the work kind's band, with a reason
  duplicates    no fact (fact_id, else the selector) in three or more slots (V3 §9)
  sampling      <= 5 samples per spot-check group, and a volume slot for every sampled group
  exceptions    an exception names who singles it out; with --manifest that id is an authority or fragment
  mechanisms    with --solver or a manifest mechanism_portfolio, every slot mechanism is a known rule id
  These are validity rules: surface_grader.py and the forecast score this surface and the go / no-go rules use their
  numbers, so a surface that breaks V3's rubric rules counts losses the real rubric can't have.
  report        geometry, the difficulty figures (total weight, weight by class, mechanism share, always-pass share):
                reported, never gated (plan §4.6)

Usage:
  python3 -B Task_Authoring/tools/gradable_surface.py validate [SURFACE] [--task-dir DIR] [--manifest M] [--solver S] [--json]
  python3 -B Task_Authoring/tools/gradable_surface.py from-slots SLOTS.json --out SURFACE.json [--task T] [--revision R]
      [--sql SQL] [--deliverables DELIVERABLES.json] [--classes READY,WATCH,HOLD]
  python3 -B Task_Authoring/tools/gradable_surface.py --self-test
Exit 0 = PASS, 1 = FAIL, 2 = usage error.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
import re
import sys
import tempfile
from pathlib import Path


def _bundle() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "difficulty_stats.py").is_file():
            return parent
    raise SystemExit("gradable_surface: cannot find the Task_Authoring bundle (no tools/difficulty_stats.py above)")


HERE = Path(__file__).resolve().parent
BUNDLE = _bundle()
for _p in (BUNDLE / "tools", HERE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

VERSION = 1
WORK_BANDS = {"lookup": 1, "interpretation": 3, "calculation": 3, "comparison": 3, "limited_reconciliation": 3,
              "multi_source_reconciliation": 5, "deeper_reasoning": 5, "cross_modal": 5, "tracing": 5}
CLASSES = ("direct", "aggregate", "write_content", "delivery")
ROLES = ("sample", "exception", "volume", "core")
SELECTORS = {"field": 2, "total": 1, "printed_total": 1, "group_count": 1, "group_size": 1, "group_key": 2,
             "groups_of": 1, "sole_reason": 2, "reason_matches": 2, "tracker_lists": 2, "tracker_count": 2,
             "tracker_entry": 3, "text": 2, "link": 1, "delivery": 1}
DELIVERY_CHECKS = {"register_is_csv": 0, "register_keys_exact": 0, "share_reader": 0, "slide_updated": 0,
                   "slack_channel_post": 2, "trello_card": 2,
                   "tracker_state": 1, "tracker_preserves": 1, "email_reply": 1, "slack_thread": 1,
                   "slack_after_email": 0, "register_parent": 1}
REV14_KIND = "GRADABLE_SURFACE_REVISION_14"
# The revision-14 surface format (Season Pass hardening_rev14/surface.py) holds slots only. Its deliverables are the
# ones support/analysis/season_pass_runs_rev14_fixed.py hard-codes: the CSV register, the ZOM-801 tracker, the slide,
# the reply mail, the Slack thread reply and the share.
SEASON_PASS_COLUMNS = ["component key", "issue", "PR", "failed assertions", "test artifact", "receipt artifact",
                       "receipt ring", "review state", "reviewed artifact", "billing hold at snapshot", "handoff class",
                       "reason"]
SEASON_PASS_DELIVERABLES = {
    "register": {"kind": "table", "name_regex": "season pass transfer register", "key_column": "component key",
                 "key_regex": r"SP-\d{3}", "columns": SEASON_PASS_COLUMNS, "class_column": "handoff class",
                 "reason_column": "reason", "csv_required": True,
                 "comparators": {"issue": "issue_key", "PR": "pr_number", "test artifact": "sha_prefix",
                                 "receipt artifact": "sha_prefix", "reviewed artifact": "sha_prefix",
                                 "billing hold at snapshot": "yes_no"},
                 "missing_values": ["", "missing", "na", "none", "withdrawn", "nocurrentreceipt", "unavailable"],
                 "yes_no": {"yes": ["yes", "true", "1", "active"], "no": ["no", "false", "0", "inactive", "notactive"]}},
    "tracker": {"kind": "text", "tool": "linear_update_issue", "issue": "ZOM-801", "key_regex": r"SP-\d{3}",
                "groups": [["billing", "billing"], ["missing", "missing"], ["assertions", "assert"],
                           ["review", "review"], ["artifact", "artifact"]]},
    "slide": {"kind": "json_text", "tool": "gslides_batch_update"},
    "email": {"kind": "json_text", "tool": "gmail_reply_to_message"},
    "slack": {"kind": "json_text", "tool": "slack_send_message"},
    "share": {"kind": "calls", "tool": "gdrive_share_file"}}
COMPARATORS = ("issue_key", "pr_number", "sha_prefix", "yes_no", "norm")
NOT_SOLVER = object()   # a slot whose value the solver's rows do not determine (write content, delivery)
SAMPLE_LIMIT = 5
# why each blocking family blocks (decision 2026-10-25: the V3 rubric rules block; geometry is report-only)
FAMILY_BASIS = {
    "structure": "the grader, the forecast and the geometry must read every slot deterministically (plan §4.3 file "
                 "shape): an unreadable slot is a loss or a pass nobody can check",
    "gradeable": "surface.gradeable: a dry-run of every selector class through the grader's real decoder; a slot whose "
                 "fixture cannot be read is UNGRADED by construction and must not enter a surface",
    "weights": "QC Spec V2 / V3: weight by kind of work, 1/3/5, with a reason (09_Rubric_Writing gate 8)",
    "duplicates": "V3 §9: the same fact in three or more rows fails (one miss would count in three rows)",
    "sampling": "spot checks: <= 5 samples per group plus a volume row (09 gates 6 and 15; missing_coverage: a missing "
                "volume row for a sampled output)",
    "exceptions": "a direct exception row only for a member an incorporated authority singles out (S6b; otherwise "
                  "the row is unauthorized)",
    "mechanisms": "a slot's mechanisms must be real rule / portfolio ids, else the geometry and the forecast count a "
                  "loss no designed mechanism can cause",
}


def load(path) -> dict:
    """A GRADABLE_SURFACE file, or a revision-14 legacy surface converted in memory (from_revision14)."""
    s = json.loads(Path(path).read_text())
    if isinstance(s, dict) and s.get("kind") == REV14_KIND:
        return from_revision14(s, source=str(path))
    if not isinstance(s, dict) or s.get("kind") != "GRADABLE_SURFACE":
        raise ValueError(f"{path}: not a GRADABLE_SURFACE file")
    return s


def from_revision14(s: dict, deliverables: dict | None = None, source: str | None = None) -> dict:
    """The revision-14 surface format as a GRADABLE_SURFACE: slots and selectors unchanged (tracker_entry and
    register_parent included), work kinds inferred from the weights (from_slots), the mechanism ids (M1-M4) kept, and
    the Season Pass deliverables, which that format leaves implicit."""
    slots_doc = {"slots": [dict({"id": x["id"], "weight": x["weight"], "selector": x["selector"],
                                 "title": x.get("title", "")},
                                **({"gradable": x["gradable"]} if "gradable" in x else {}))
                           for x in s.get("slots") or []], "source": f"{REV14_KIND} {source or ''}".strip()}
    mech = {x["id"]: [x["mechanism"]] for x in s.get("slots") or [] if re.fullmatch(r"M\d+", str(x.get("mechanism")))}
    out = from_slots(slots_doc, task="season_pass", revision="rev14", sql_sha256=s.get("sql_sha256"),
                     deliverables=deliverables or json.loads(json.dumps(SEASON_PASS_DELIVERABLES)),
                     classes=list(((s.get("truth") or {}).get("classes") or {"READY": 0, "WATCH": 0, "HOLD": 0})),
                     mechanisms=mech)
    out["provenance"].update(rule="from-revision-14: selectors as written; work kinds inferred from weights; the "
                                  "Season Pass deliverables of season_pass_runs_rev14_fixed.py",
                             revision14_truth=s.get("truth"), revision14_sampling_groups=s.get("sampling_groups"),
                             revision14_known_gaps=s.get("known_gaps"))
    return out


def table_deliverable(surface: dict, name: str | None = None) -> tuple:
    d = surface.get("deliverables") or {}
    if name:
        return name, d.get(name)
    for k, v in d.items():
        if isinstance(v, dict) and v.get("kind") == "table":
            return k, v
    return None, None


def table_deliverables(surface: dict) -> list:
    """[(name, spec)] for every declared table deliverable, in declaration order."""
    return [(k, v) for k, v in (surface.get("deliverables") or {}).items()
            if isinstance(v, dict) and v.get("kind") == "table"]


def text_deliverable(surface: dict) -> tuple:
    for k, v in (surface.get("deliverables") or {}).items():
        if isinstance(v, dict) and v.get("kind") == "text":
            return k, v
    return None, None


def fact_id(slot: dict) -> str:
    if slot.get("fact_id"):
        return str(slot["fact_id"])
    sel = slot.get("selector")
    if not isinstance(sel, list):
        return "sel:" + json.dumps(sel, ensure_ascii=False)
    if len(sel) >= 2 and sel[0] in ("total", "printed_total"):  # one class total, wherever printed below the rows
        return f"total:{sel[1]}"
    return "sel:" + json.dumps(sel, ensure_ascii=False)


def slot_group(slot: dict, table_name: str = "register") -> str | None:
    if slot.get("group"):
        return slot["group"]
    sel = slot.get("selector")
    if not isinstance(sel, list):
        return None
    if len(sel) >= 3 and sel[0] == "field":
        return f"{table_name}:{sel[2]}"
    return None


def role(slot: dict) -> str:
    if slot.get("role"):
        return slot["role"]
    sel = slot.get("selector")
    return "sample" if isinstance(sel, list) and len(sel) >= 3 and sel[0] == "field" else "core"


# ------------------------------------------------------------------ slot values on solver rows (mutation, forecast)

def class_counts(rows: dict, class_field: str) -> dict:
    return dict(collections.Counter(v.get(class_field) for v in rows.values()))


def group_members(rows: dict, group: str, groups_field: str = "groups") -> list:
    return [k for k, v in rows.items() if group in (v.get(groups_field) or [])]


def solver_value(slot: dict, rows: dict, surface: dict):
    """The value a slot reads from solver rows ({key: {field: value, groups: [...]}}), or NOT_SOLVER."""
    tf = surface.get("truth_fields") or {}
    cf, gf = tf.get("class", "handoff class"), tf.get("groups", "groups")
    sel = slot.get("selector")
    if not isinstance(sel, list):
        return NOT_SOLVER
    kind = sel[0] if sel else None
    if kind == "field" and len(sel) >= 3:
        return (rows.get(sel[1]) or {}).get(sel[2])
    if kind in ("total", "printed_total") and len(sel) >= 2:
        t0 = table_deliverables(surface)
        try:
            krx0 = (t0[0][1].get("key_regex") if t0 else None)
            scope = {k: v for k, v in rows.items() if not krx0 or re.fullmatch(krx0, str(k))}
        except re.error:
            scope = rows
        return class_counts(scope, cf).get(sel[1], 0)
    if kind in ("group_count", "group_size") and len(sel) >= 2:
        return len(group_members(rows, sel[1], gf))
    if kind == "group_key" and len(sel) >= 3:
        return sel[1] in group_members(rows, sel[2], gf)
    if kind == "groups_of" and len(sel) >= 2:
        return sorted((rows.get(sel[1]) or {}).get(gf) or [])
    if kind == "sole_reason" and len(sel) >= 3:
        return ((rows.get(sel[1]) or {}).get(gf) or []) == [sel[2]]
    return NOT_SOLVER


def slot_keys(slot: dict) -> list:
    """Cohort keys a slot reads directly (empty for aggregates and writes)."""
    sel = slot.get("selector")
    if not isinstance(sel, list):
        return []
    if len(sel) >= 2 and sel[0] in ("field", "group_key", "groups_of", "sole_reason", "reason_matches"):
        return [sel[1]]
    if len(sel) >= 3 and sel[0] in ("tracker_lists", "tracker_entry"):
        return [sel[2]]
    return []


# ------------------------------------------------------------------ validation

def _finding(out, sev, check, detail, slot=None):
    out.append({"severity": sev, "check": check, "slot": slot, "detail": detail,
                "basis": FAMILY_BASIS[check.split(".")[0]]})


def _split_top(rx: str) -> list:
    """Split a regex on top-level `|` (never inside a class, group or escape)."""
    parts, depth, start, i = [], 0, 0, 0
    while i < len(rx):
        ch = rx[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "[":
            i += 1
            while i < len(rx) and rx[i] != "]":
                i += 2 if rx[i] == "\\" else 1
            i += 1
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "|" and depth == 0:
            parts.append(rx[start:i])
            start = i + 1
        i += 1
    parts.append(rx[start:])
    return parts


def _rx_candidates(rx: str, cap: int = 64) -> list:
    """A few literal strings a regex can match, from a tiny structural generator (enough for fixture keys and
    names). Not a general regex sampler: unsupported atoms give no candidate, and the caller falls back to the
    regex's literal chunks."""
    parts = _split_top(rx)
    if len(parts) > 1:
        out = []
        for p in parts:
            out.extend(_rx_candidates(p, cap))
            if len(out) >= cap:
                break
        return out[:cap]
    toks, i = [], 0
    while i < len(rx):
        ch = rx[i]
        if ch == "\\":
            nxt = rx[i + 1] if i + 1 < len(rx) else ""
            if nxt == "d":
                atom = ["0"]
            elif nxt == "w":
                atom = ["a"]
            elif nxt == "s":
                atom = [" "]
            elif nxt == "b":
                atom = [""]
            elif nxt in "DWSBAZz0123456789":
                return []
            else:
                atom = [nxt]
            i += 2
        elif ch in "^$":
            i += 1
            continue
        elif ch == ".":
            atom = ["a"]
            i += 1
        elif ch == "[":
            j = i + 1
            while j < len(rx) and rx[j] != "]":
                j += 2 if rx[j] == "\\" else 1
            body = rx[i + 1:j]
            if not body or body.startswith("^"):
                return []
            atom = [body[1] if body.startswith("\\") and len(body) > 1 else body[0]]
            i = j + 1
        elif ch == "(":
            depth, j = 1, i + 1
            while j < len(rx) and depth:
                if rx[j] == "\\":
                    j += 2
                    continue
                depth += 1 if rx[j] == "(" else (-1 if rx[j] == ")" else 0)
                j += 1
            inner = rx[i + 1:j - 1]
            if inner.startswith("?:"):
                inner = inner[2:]
            elif inner.startswith("?P<"):
                k = inner.find(">")
                if k < 0:
                    return []
                inner = inner[k + 1:]
            elif inner.startswith("?"):
                return []
            atom = _rx_candidates(inner, cap)
            if not atom:
                return []
            i = j
        elif ch in "*+?":
            return []
        else:
            atom = [ch]
            i += 1
        lo = 1
        if i < len(rx) and rx[i] == "{":
            j = rx.find("}", i)
            if j < 0:
                return []
            try:
                lo = int(rx[i + 1:j].split(",")[0])
            except ValueError:
                return []
            i = j + 1
        elif i < len(rx) and rx[i] in "*+?":
            ch2 = rx[i]
            lo = 0 if ch2 in "*?" else 1
            i += 1
        toks.append((atom, lo))
    combos = [""]
    for atom, lo in toks:
        combos = [(c + a * lo) for c in combos for a in atom[:4]][:cap]
    return combos[:cap]


def _unesc(m) -> str:
    c = m.group(1)
    if c in "bB":
        return " "
    if c == "d":
        return "0"
    if c == "w":
        return "a"
    if c == "s":
        return " "
    return c


def _literal_chunks(rx: str) -> list:
    """The literal runs of a regex (per top-level alternative), e.g. `\\bREADY\\b\\D{0,20}?\\b44\\b` -> READY, 44."""
    out = []
    for part in _split_top(str(rx)):
        s = re.sub(r"\\(.)", _unesc, part)
        s = re.sub(r"[\[\]{}()*+?^$|]", " ", s)
        for m in re.finditer(r"[A-Za-z0-9][A-Za-z0-9 ._@/-]*", s):
            t = m.group(0).strip(" .")
            if t:
                out.append(t)
    return out


def sample_from_regex(rx: str):
    """A string the regex matches, or None. Tries the structural generator, then the literal chunks alone, joined and
    adjacent (the shape most slot patterns use, e.g. "SHIP 38")."""
    rx = str(rx)
    try:
        re.compile(rx)
    except re.error:
        return None

    def hit(cand):
        try:
            return bool(cand) and re.fullmatch(rx, cand) is not None
        except re.error:
            return False
    cands = _rx_candidates(rx)
    chunks = _literal_chunks(rx)
    cands += chunks + [" ".join(chunks), "".join(chunks)]
    for i in range(len(chunks) - 1):
        cands += [chunks[i] + " " + chunks[i + 1], chunks[i] + chunks[i + 1]]
    for c in cands:
        if hit(c):
            return c
    return None


# ------------------------------------------------------------------ surface.gradeable: a dry run through the real decoder

def _table_for_key(tables: list, key) -> tuple:
    """(name, spec) of the table deliverable whose key_regex matches this key, else (None, None)."""
    for name, spec in tables:
        try:
            if re.fullmatch(spec.get("key_regex") or r".+", str(key)):
                return name, spec
        except re.error:
            continue
    return None, None


def _key_for(spec: dict, hints=()) -> str | None:
    krx = spec.get("key_regex") or r".+"
    for h in hints:
        if h is not None and re.fullmatch(krx, str(h)):
            return str(h)
    return sample_from_regex(krx)


def _keys_for(spec: dict, n: int, hint=None) -> list:
    """n distinct keys that each fullmatch the spec's key_regex, or fewer if it cannot be done. Numeric suffixes are
    scanned (not just the next n integers), so a regex like `K-(?:01|03)` still yields two valid keys."""
    krx = spec.get("key_regex") or r".+"
    key = _key_for(spec, [hint] if hint else [])
    out = []

    def ok(k):
        try:
            return bool(re.fullmatch(krx, k)) and k not in out
        except re.error:
            return False
    if key and ok(key):
        out.append(key)
    m = re.search(r"(\d+)(\D*)$", key or "")
    if m:
        start, width, tail = int(m.group(1)), len(m.group(1)), m.group(2)
        for i in range(start, start + 400):
            if len(out) >= n:
                break
            k = key[:m.start(1)] + f"{i:0{width}d}" + tail
            if ok(k):
                out.append(k)
    if len(out) < n and key and not m:
        return out
    return out[:n]


def _cell_value(comp: str | None, key: str) -> str:
    return {"issue_key": str(key), "pr_number": "PR #1", "sha_prefix": "abcdef0", "yes_no": "yes",
            "norm": "ok"}.get(comp or "norm", "ok")


def _table_name(spec: dict) -> str:
    """A file name the table deliverable's name_regex accepts (the CSV write must carry it)."""
    return sample_from_regex(spec.get("name_regex") or "") or "deliverable"


def _csv_call(name: str, columns: list, row: dict | list, result: dict | None = None, parent: str | None = None) -> tuple:
    rows = row if isinstance(row, list) else [row]
    buf = io.StringIO()
    wr = csv.writer(buf, lineterminator="\n")
    wr.writerow(columns)
    for r in rows:
        wr.writerow([r.get(c, "") for c in columns])
    q = {"name": name, "mimeType": "text/csv", "content": buf.getvalue()}
    if parent:
        q["parentId"] = parent
    return ("gdrive_create_file", q, result or {"id": "DRYRUNFILE", "ok": True})


def _dry_run_call(calls: list):
    import trajectory_ledger as tl
    cs, rs = [], {}
    for i, c in enumerate(calls):
        cs.append({"event": i, "id": f"c{i}", "name": f"mcp__hg__{c[0]}", "input": c[1], "model": "dry-run",
                   "parent": None, "context": "main"})
        rs[f"c{i}"] = {"event": i, "error": False, "data": c[2] if len(c) > 2 else {"ok": True}}
    return tl.Run("dry-run", Path("dry-run.json"), "derived-calls", None, cs, rs)


def _selector_problem(slot: dict):
    """Why the slot's selector is not one this tool can evaluate, or None. Shared by gradeable() and the report so
    they never disagree, and called before any fixture is built so a malformed selector cannot crash the CLI (R5-2)."""
    sel = slot.get("selector")
    if not isinstance(sel, list) or not sel or not isinstance(sel[0], str) or sel[0] not in SELECTORS:
        return "malformed selector"
    if len(sel) - 1 < SELECTORS[sel[0]]:
        return f"selector {sel[0]} needs {SELECTORS[sel[0]]} argument(s)"
    if sel[0] == "delivery":
        if not isinstance(sel[1], str):
            return f"delivery check {sel[1]!r} is not a name"
        need = DELIVERY_CHECKS.get(sel[1])
        if need is None or len(sel) - 2 < need:
            return f"unknown delivery check {sel[1:]!r}"
    if sel[0] == "tracker_count":
        n = sel[2]
        if isinstance(n, bool) or not isinstance(n, int) or n < 0:
            return f"tracker_count needs a non-negative integer count, not {n!r}"
    if sel[0] == "tracker_entry" and (not isinstance(sel[3], list) or not sel[3]):
        return "tracker_entry needs a non-empty list of value patterns"
    if sel[0] in ("reason_matches", "text"):
        if not isinstance(sel[2], str):
            return f"regex argument {sel[2]!r} is not a string"
        try:
            re.compile(sel[2])
        except (re.error, TypeError) as error:
            return f"bad regex {sel[2]!r}: {error}"
    return None


def _heading_line(section: str) -> str:
    """A tracker heading line the selector's heading regex matches: the sample alone when it already looks like a
    heading, else `### <sample>`, and never a double markdown prefix (R5-5)."""
    sample = sample_from_regex(section) or section
    for line in (sample, f"### {sample}"):
        try:
            if re.search(section, line, re.I):
                return line
        except re.error:
            break
    return sample


def _dry_run(surface: dict, slot: dict) -> dict:
    """Build a synthetic truth side and write payload for one slot, decode and grade it. GRADABLE only when the slot
    reads True on a fixture built for it *and* False on the same truth with no content delivered (a slot that passes
    with nothing written is not gradable)."""
    import surface_grader as sg
    sid, sel = slot.get("id"), slot.get("selector")
    tables = table_deliverables(surface)
    tname, tspec = tables[0] if tables else (None, None)
    xname, xspec = text_deliverable(surface)
    classes = surface.get("classes") or ["READY"]
    tf = surface.get("truth_fields") or {}
    tclass = tf.get("class") or (tspec or {}).get("class_column") or "class"
    tgroups = tf.get("groups") if isinstance(tf.get("groups"), str) else "groups"
    cf = (tspec or {}).get("class_column") or tclass
    res = {"slot": sid, "weight": slot.get("weight"), "selector": sel,
           "status": "UNGRADABLE", "reason": None, "kind": None}
    problem = _selector_problem(slot)                 # R7-3: validated before any fixture, declared or not
    if problem:
        return dict(res, reason=problem)
    kind = sel[0]
    res["kind"] = kind

    def ungradable(reason):
        return dict(res, status="UNGRADABLE", reason=reason)

    def check(truth, calls, why=""):
        try:
            d = sg.decode(_dry_run_call(calls), surface)
            got = sg.grade(surface, truth, d).get(sid)
            empty = sg.grade(surface, truth, sg.decode(_dry_run_call([]), surface)).get(sid)
        except Exception as error:  # noqa: BLE001 - a decoder that raises on the class is the finding
            return ungradable(f"decoder raised {type(error).__name__}: {error}")
        if got is None:
            return ungradable(f"UNGRADED with a fixture built for it{': ' + why if why else ''}")
        if not got:
            return ungradable(f"no synthetic fixture the slot reads (graded False){': ' + why if why else ''}")
        if empty is None:
            return ungradable("UNGRADED when nothing is delivered")
        if empty:
            return ungradable("grades True with nothing delivered (the fixture cannot fail)")
        return dict(res, status="GRADABLE", reason=None)

    if kind == "field":
        key, field = str(sel[1]), str(sel[2])
        tn, tsp = _table_for_key(tables, key)
        if tsp is None:
            return ungradable(f"field key {key!r} matches no table deliverable's key_regex")
        if field not in (tsp.get("columns") or []):
            return ungradable(f"column {field!r} is not a column of table {tn!r}")
        val = key if field == tsp.get("key_column") else _cell_value((tsp.get("comparators") or {}).get(field), key)
        row = {c: (key if c == tsp.get("key_column") else (val if c == field else "")) for c in tsp["columns"]}
        truth = {key: {tclass: val if field == cf else classes[0], tgroups: [], field: val}}
        return check(truth, [_csv_call(_table_name(tsp), list(tsp["columns"]), row)])

    if kind in ("total", "printed_total"):
        cls = str(sel[1])
        if tspec is None or cf not in (tspec.get("columns") or []):
            return ungradable("no table deliverable with a class column")
        tn = tname
        cols2 = _keys_for(tspec, 2)
        if len(cols2) < 2:
            return ungradable(f"cannot synthesize two keys for key_regex {tspec.get('key_regex')!r}")
        key, keys = cols2
        rows = [{c: (k if c == tspec.get("key_column") else (cls if c == cf else "")) for c in tspec["columns"]}
                for k in (key, keys)]
        truth = {k: {tclass: cls, tgroups: []} for k in (key, keys)}
        if kind == "printed_total":
            totals = {tspec["columns"][0]: cls, tspec["columns"][1]: "2"}
            calls = [_csv_call(_table_name(tspec), list(tspec["columns"]), rows + [totals])]
        else:
            calls = [_csv_call(_table_name(tspec), list(tspec["columns"]), rows)]
        return check(truth, calls, "two rows of one class")

    if kind in ("group_count", "group_size"):
        group = str(sel[1])
        if any(name == group for name, _ in tables):
            return ungradable(f"group {group!r} names the table deliverable {group!r}: no tracker text declares a "
                              f"group of that name, so the count has no written source")
        if xspec is None:
            return ungradable(f"no text deliverable declares a tracker: group {group!r} has no written source")
        krx = xspec.get("key_regex") or tspec.get("key_regex") if (xspec or tspec) else r".+"
        gk = _keys_for({"key_regex": krx}, 2)
        if len(gk) < 2:
            return ungradable(f"cannot synthesize two keys for key_regex {krx!r}")
        k1, k2 = gk
        text = f"- {group} (2):\n- {k1}\n- {k2}"     # multi-line: the decoder must keep every member (G1 R8)
        truth = {k1: {tclass: classes[0], tgroups: [group]}, k2: {tclass: classes[0], tgroups: [group]}}
        return check(truth, [(xspec.get("tool") or "linear_update_issue", {"id": xspec.get("issue"), "description": text})])

    if kind in ("group_key", "groups_of", "sole_reason"):
        key = str(sel[1])
        if xspec is None:
            return ungradable("no text deliverable declares a tracker: the group has no written source")
        names = [g for g, _ in (xspec.get("groups") or [])]
        group = str(sel[2]) if kind != "groups_of" else (names[0] if names else "group")
        text = f"- {group} (1): {key}"
        truth = {key: {tclass: classes[0], tgroups: [group]}}
        return check(truth, [(xspec.get("tool") or "linear_update_issue", {"id": xspec.get("issue"), "description": text})])

    if kind == "reason_matches":
        key, rx = str(sel[1]), str(sel[2])
        tn, tsp = _table_for_key(tables, key)
        if tsp is None:
            return ungradable(f"key {key!r} matches no table deliverable's key_regex")
        col = tsp.get("reason_column")
        if not col or col not in (tsp.get("columns") or []):
            return ungradable(f"table {tn!r} declares no reason_column")
        val = sample_from_regex(rx)
        if val is None:
            return ungradable(f"cannot synthesize a value for regex {rx!r}")
        row = {c: (key if c == tsp.get("key_column") else (val if c == col else "")) for c in tsp["columns"]}
        return check({key: {tclass: classes[0], tgroups: [], col: val}}, [_csv_call(_table_name(tsp), list(tsp["columns"]), row)])

    if kind in ("tracker_lists", "tracker_count", "tracker_entry"):
        if xspec is None:
            return ungradable("no text deliverable declares a tracker")
        krx = xspec.get("key_regex") or r".+"
        key = _key_for({"key_regex": krx}, [sel[2] if len(sel) > 2 else None])
        if key is None:
            return ungradable(f"cannot synthesize a key for key_regex {krx!r}")
        if kind == "tracker_entry":
            section, value, pats = str(sel[1]), str(sel[2]), list(sel[3])
            vals = [sample_from_regex(p) for p in pats]
            if any(v is None for v in vals):
                return ungradable(f"cannot synthesize a value for entry patterns {pats}")
            text = f"{_heading_line(section)}\n- {value}: {' '.join(vals)}"
        else:
            section = str(sel[1])
            n = int(sel[2]) if kind == "tracker_count" else 1
            if kind == "tracker_count" and n < 0:
                return ungradable(f"tracker_count {n} is negative")
            keys = _keys_for({"key_regex": krx}, n, key)
            if len(keys) < n:
                return ungradable(f"cannot synthesize {n} distinct keys for key_regex {krx!r}")
            text = _heading_line(section) + "".join(f"\n- {k}" for k in keys)
        return check({key: {tclass: classes[0], tgroups: []}},
                     [(xspec.get("tool") or "linear_update_issue", {"id": xspec.get("issue"), "description": text})])

    if kind == "text":
        target, rx = str(sel[1]), str(sel[2])
        sample = sample_from_regex(rx)
        if sample is None:
            return ungradable(f"cannot synthesize a string for regex {rx!r}")
        if any(name == target for name, _ in tables):
            tn, tsp = next((n, s) for n, s in tables if n == target)
            key = _key_for(tsp)
            if key is None:
                return ungradable(f"cannot synthesize a key for key_regex {tsp.get('key_regex')!r}")
            row = {c: (key if c == tsp.get("key_column") else "") for c in tsp["columns"]}
            row[next((c for c in tsp["columns"] if c != tsp.get("key_column")), tsp["columns"][0])] = sample
            return check({key: {tclass: classes[0], tgroups: []}}, [_csv_call(_table_name(tsp), list(tsp["columns"]), row)])
        d_spec = (surface.get("deliverables") or {}).get(target)
        tool = (d_spec or {}).get("tool")
        if target == "tracker" or (d_spec or {}).get("kind") == "text":
            if xspec is None:
                return ungradable(f"text target {target!r} is a tracker with no text deliverable")
            return check({}, [(xspec.get("tool") or "linear_update_issue",
                               {"id": xspec.get("issue"), "description": sample})])
        if d_spec is None and target not in ("slide", "email", "slack", "tickets", "summary", "mail"):
            return ungradable(f"text target {target!r} is not a deliverable")
        # the same implicit tool names decode() uses for the legacy json_text targets
        tool = tool or {"slide": "gslides_batch_update", "email": "gmail_reply_to_message",
                        "slack": "slack_send_message"}.get(target, target)
        return check({}, [(tool, {"text": sample, "body": sample, "message": sample})])

    if kind == "link":
        target = str(sel[1])
        if tspec is None:
            return ungradable("link needs a table deliverable to carry an identity")
        key = _key_for(tspec)
        if key is None:
            return ungradable(f"cannot synthesize a key for key_regex {tspec.get('key_regex')!r}")
        row = {c: (key if c == tspec.get("key_column") else "DRYRUNFILE") for c in tspec["columns"]}
        calls = [_csv_call(_table_name(tspec), list(tspec["columns"]), row, result={"id": "DRYRUNFILE", "ok": True}),
                 ("gdrive_share_file", {"fileId": "DRYRUNFILE", "role": "reader"})]
        dst = next((sp for n, sp in tables if n == target and n != tname), None)
        if dst is not None:
            # R5-7: the identity must reach the *selected* destination table, so write it into that table too
            dk = _keys_for(dst, 1)
            if not dk:
                return ungradable(f"cannot synthesize a key for destination table {target!r}")
            drow = {c: (dk[0] if c == dst.get("key_column") else "DRYRUNFILE") for c in dst["columns"]}
            calls.append(_csv_call(_table_name(dst), list(dst["columns"]), drow, result={"id": "DRYRUNDST"}))
        elif target not in [n for n, _ in tables]:
            d_spec = (surface.get("deliverables") or {}).get(target)
            tool = (d_spec or {}).get("tool")
            if target == "tracker" or (d_spec or {}).get("kind") == "text":
                if xspec is None:
                    return ungradable(f"link target {target!r} is a tracker with no text deliverable")
                tool = xspec.get("tool") or "linear_update_issue"
                calls.append((tool, {"id": xspec.get("issue"), "description": "DRYRUNFILE shared"}))
            else:
                tool = tool or {"slide": "gslides_batch_update", "email": "gmail_reply_to_message",
                                "slack": "slack_send_message"}.get(target, target)
                calls.append((tool, {"text": "DRYRUNFILE shared", "body": "DRYRUNFILE shared"}))
        return check({key: {tclass: classes[0], tgroups: []}}, calls)

    if kind == "delivery":
        name = str(sel[1])
        if name == "register_is_csv":
            if tspec is None:
                return ungradable("register_is_csv needs a table deliverable")
            key = _key_for(tspec)
            if key is None:
                return ungradable(f"cannot synthesize a key for key_regex {tspec.get('key_regex')!r}")
            return check({key: {tclass: classes[0], tgroups: []}},
                         [_csv_call(_table_name(tspec), list(tspec["columns"]), {tspec.get("key_column"): key})])
        if name == "register_keys_exact":
            if tspec is None:
                return ungradable("register_keys_exact needs a table deliverable")
            tn = str(sel[2]) if len(sel) > 2 else tname
            tsp = next((s for n, s in tables if n == tn), None)
            if tsp is None:
                return ungradable(f"register_keys_exact names {tn!r}, which is not a table deliverable")
            expected = [str(k) for k in (slot.get("expected_keys") or surface.get("truth_keys") or [])]
            if not expected and slot.get("role") == "volume":
                k = _key_for(tsp)                       # a volume row's cohort is the whole register
                expected = [k] if k else []
            if not expected:
                return ungradable("register_keys_exact has no explicit expected key set (truth_keys or slot "
                                  "expected_keys): it would grade against the whole truth")
            krx = tsp.get("key_regex") or r".+"
            bad = [k for k in expected if not re.fullmatch(krx, k)]
            if bad:
                return ungradable(f"expected key(s) {bad[:3]} do not match table {tn!r}'s key_regex")
            key = expected[0]
            row = [{c: (k if c == tsp.get("key_column") else "") for c in tsp["columns"]} for k in expected]
            return check({k: {tclass: classes[0], tgroups: []} for k in expected},
                         [_csv_call(_table_name(tsp), list(tsp["columns"]), row)])
        if name in ("share_reader", "register_parent"):
            if tspec is None:
                return ungradable(f"{name} needs a table deliverable identity")
            key = _key_for(tspec)
            if key is None:
                return ungradable(f"cannot synthesize a key for key_regex {tspec.get('key_regex')!r}")
            parent = str(sel[2]) if name == "register_parent" else None
            calls = [_csv_call(_table_name(tspec), list(tspec["columns"]), {tspec.get("key_column"): key},
                               result={"id": "DRYRUNFILE", "ok": True}, parent=parent),
                     ("gdrive_share_file", {"fileId": "DRYRUNFILE", "role": "reader"})]
            return check({key: {tclass: classes[0], tgroups: []}}, calls)
        if name == "slide_updated":
            return check({}, [("gslides_batch_update", {"presentationId": "P1", "requests": [{"x": "y"}]})])
        if name in ("tracker_state", "tracker_preserves"):
            arg = str(sel[2])
            if name == "tracker_preserves":
                if xspec is None:
                    return ungradable("tracker_preserves needs a text deliverable")
                return check({}, [(xspec.get("tool") or "linear_update_issue",
                                   {"id": xspec.get("issue"), "description": f"kept {arg}"})])
            if arg in ("comment", "description", "state"):
                return check({}, [("trello_add_comment_to_card", {"cardId": "C1", "text": f"{arg} noted"})])
            if re.fullmatch(r"[0-9a-f]{24}", arg):
                return check({}, [("trello_add_comment_to_card", {"cardId": arg, "text": "noted"})])
            if xspec is None:
                return ungradable(f"tracker_state {arg!r} needs a text deliverable (its state is read from tracker "
                                  f"updates)")
            # R7-2: the runtime uses `re.match(arg, state, re.I)`, so the fixture state must match the regex, not be
            # the regex text (an anchored `^Done$` would otherwise be rejected by the dry run)
            state = arg
            try:
                if re.match(arg, arg, re.I) is None:
                    state = sample_from_regex(arg) or arg
            except re.error:
                return ungradable(f"bad tracker_state regex {arg!r}")
            return check({}, [(xspec.get("tool") or "linear_update_issue", {"id": xspec.get("issue"), "state": state})])
        if name == "trello_card":
            return check({}, [("trello_add_comment_to_card", {"cardId": str(sel[2]), "text": str(sel[3])})])
        if name == "email_reply":
            return check({}, [("gmail_reply_to_message", {"message_id": str(sel[2]), "reply_all": False,
                                                          "body": "received"})])
        if name == "slack_thread":
            return check({}, [("slack_send_message", {"thread_ts": str(sel[2]), "text": "noted"})])
        if name == "slack_channel_post":
            return check({}, [("slack_send_message", {"channel_id": str(sel[2]), "text": str(sel[3])})])
        if name == "slack_after_email":
            return check({}, [("gmail_reply_to_message", {"message_id": "m1", "reply_all": False, "body": "x"}),
                              ("slack_send_message", {"channel_id": "C1", "text": "noted"})])
        return ungradable(f"no dry-run fixture for delivery check {name!r}")

    return ungradable(f"no dry-run fixture for selector kind {kind!r}")


def _gradeable_structure(surface: dict) -> list:
    """Structural limits a synthetic fixture cannot repair (kept from the pre-dry-run check): a Slack thread must be
    addressed by a timestamp; a tracker_state must not be a Trello card id (that is a different check); an exact-key
    check needs an explicit expected key set unless it is a volume row (whose cohort is the whole register)."""
    out, tf = [], surface.get("truth_fields") or {}
    tname, tspec = table_deliverable(surface)
    group_slots = [s for s in surface.get("slots") or []
                   if isinstance(s.get("selector"), list) and s.get("selector")
                   and s["selector"][0] in ("group_count", "group_size", "group_key", "groups_of",
                                            "tracker_lists", "tracker_count")]
    if group_slots and not tf.get("groups"):
        out.append({"slot": None, "kind": "group",
                    "reason": "group/tracker slots need truth_fields.groups to build their truth side"})
    if not isinstance(tf.get("groups"), (str, type(None))):
        out.append({"slot": None, "kind": "group",
                    "reason": f"truth_fields.groups is {tf.get('groups')!r}: it must name a field, not hold a value"})
    gname = tf.get("groups")
    if isinstance(gname, str):
        for tn, tsp in table_deliverables(surface):
            if gname in (tsp.get("columns") or []):
                out.append({"slot": None, "kind": "group",
                            "reason": f"truth_fields.groups names {gname!r}, a column of table {tn!r}: a written "
                                      f"column is one scalar per row, never a group list"})
                break
    for s in surface.get("slots") or []:
        sel, sid = s.get("selector"), s.get("id")
        if not isinstance(sel, list) or not sel or not isinstance(sel[0], str) or sel[0] not in SELECTORS:
            continue
        if len(sel) - 1 < SELECTORS[sel[0]]:
            continue
        if sel[0] == "delivery":
            if not isinstance(sel[1], str):
                out.append({"slot": sid, "kind": "delivery", "reason": f"delivery check {sel[1]!r} is not a name"})
                continue
            need = DELIVERY_CHECKS.get(sel[1])
            if need is None or len(sel) - 2 < need:
                continue
            if sel[1] == "slack_thread" and not re.fullmatch(r"\d{10}\.\d{6}", str(sel[2])):
                out.append({"slot": sid, "kind": "delivery",
                            "reason": f"slack_thread value {sel[2]!r} is not a Slack timestamp"})
            if sel[1] == "tracker_state":
                v = str(sel[2])
                if re.fullmatch(r"[0-9a-f]{24}", v) or re.fullmatch(r"T-?\d+", v):
                    out.append({"slot": sid, "kind": "delivery",
                                "reason": f"tracker_state value {v!r} looks like a Trello id, not a state"})
            if sel[1] == "register_keys_exact":
                if not tspec:
                    out.append({"slot": sid, "kind": "delivery",
                                "reason": "register_keys_exact needs a table deliverable"})
                elif not (s.get("expected_keys") or surface.get("truth_keys")) and s.get("role") != "volume":
                    out.append({"slot": sid, "kind": "delivery",
                                "reason": "register_keys_exact has no explicit expected key set (truth_keys or slot "
                                          "expected_keys): it would grade against the whole truth"})
    return out


def gradeable(surface: dict) -> list:
    """surface.gradeable: a dry run of every slot through the grader's real decoder.

    For each slot: build a synthetic truth side and write payload for that selector class, run surface_grader.decode()
    and grade(), and require the slot to read True; the same truth with nothing delivered must read False (a slot
    that passes with no content is not a certification). Returns one record per slot that cannot be read, with the
    reason; validate() turns them into FAIL findings, so a surface with an ungradable slot never passes."""
    out = [{"slot": r["slot"], "weight": next((s.get("weight") for s in surface.get("slots") or []
                                                if s.get("id") == r["slot"]), None), "kind": r.get("kind"),
            "status": "UNGRADABLE", "reason": r["reason"]} for r in _gradeable_structure(surface)]
    seen = {r["slot"] for r in out}
    for s in surface.get("slots") or []:
        sel = s.get("selector")
        if s.get("id") in seen:
            continue
        if not isinstance(sel, list) or not sel or not isinstance(sel[0], str) or sel[0] not in SELECTORS:
            continue                                  # structural validation reports malformed selectors
        if len(sel) - 1 < SELECTORS[sel[0]]:
            continue
        if sel[0] == "delivery" and (DELIVERY_CHECKS.get(sel[1]) is None or len(sel) - 2 < DELIVERY_CHECKS[sel[1]]):
            continue
        r = _dry_run(surface, s)
        if r["status"] == "UNGRADABLE":
            out.append(r)
    return out


def gradeable_report(surface: dict) -> dict:
    """Every slot with its dry-run status (for the `report` command and the task-1 evidence file). The structural
    limits gradeable() enforces are part of the verdict, so the report and validate() never disagree."""
    rows, structurally = [], {}
    for r in _gradeable_structure(surface):
        structurally.setdefault(r.get("slot"), r["reason"])
    for s in surface.get("slots") or []:
        r = _dry_run(surface, s)
        if s.get("id") in structurally:
            r = dict(r, status="UNGRADABLE", reason=structurally[s["id"]])
        rows.append(r)
    for sid, reason in structurally.items():                 # a surface-level finding with no slot of its own
        if sid is None:
            rows.append({"slot": None, "weight": None, "selector": None, "status": "UNGRADABLE", "reason": reason,
                         "kind": "group"})
    counts = collections.Counter(r["status"] for r in rows)
    return {"surface_task": surface.get("task"), "surface_revision": surface.get("revision"),
            "slots": rows, "counts": dict(counts),
            "verdict": "PASS" if not counts.get("UNGRADABLE") else "FAIL"}


def truth_group_problems(truth: dict, surface: dict) -> list:
    """The group field named by truth_fields.groups must be a list on every truth row (a scalar is not membership)
    and must be a field name, never a value."""
    tf = surface.get("truth_fields") or {}
    gf = tf.get("groups")
    if gf is not None and not isinstance(gf, str):
        return [f"truth_fields.groups is {gf!r}: it must name the field that holds each row's group list"]
    gf = gf or "groups"
    out = []
    for k, v in (truth or {}).items():
        if not isinstance(v, dict) or gf not in v:
            continue
        if not isinstance(v[gf], list):
            out.append(f"truth[{k}].{gf} is {type(v[gf]).__name__} {v[gf]!r}: a group list is required")
    return out


def validate(surface: dict, manifest: dict | None = None, rule_ids=None, truth: dict | None = None) -> dict:
    f = []
    if surface.get("kind") != "GRADABLE_SURFACE" or surface.get("version") != VERSION:
        _finding(f, "FAIL", "structure.kind", f"kind/version must be GRADABLE_SURFACE/{VERSION}")
    deliverables = surface.get("deliverables") or {}
    for name, d in deliverables.items():
        if not isinstance(d, dict) or d.get("kind") not in ("table", "text", "json_text", "calls"):
            _finding(f, "FAIL", "structure.deliverable", f"deliverable {name!r} needs kind table|text|json_text|calls")
        elif d["kind"] == "table":
            miss = [k for k in ("key_column", "key_regex", "columns") if not d.get(k)]
            if miss:
                _finding(f, "FAIL", "structure.deliverable", f"table {name!r} lacks {miss}")
            for col, comp in (d.get("comparators") or {}).items():
                if comp not in COMPARATORS:
                    _finding(f, "FAIL", "structure.comparator", f"table {name!r} column {col!r}: comparator {comp!r} "
                             f"not one of {COMPARATORS}")
    tname, tspec = table_deliverable(surface)
    slots = surface.get("slots") or []
    if not slots:
        _finding(f, "FAIL", "structure.slots", "no slots")
    ids = [s.get("id") for s in slots]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup or any(not i for i in ids):
        _finding(f, "FAIL", "structure.slot_ids", f"slot ids must be present and unique; duplicates {dup}")
    classes = surface.get("classes") or []
    for s in slots:
        sid, sel = s.get("id"), s.get("selector")
        if not isinstance(sel, list) or not sel or not isinstance(sel[0], str) or sel[0] not in SELECTORS:
            _finding(f, "FAIL", "structure.selector", f"unknown selector {sel!r}", sid)
            continue
        if len(sel) - 1 < SELECTORS[sel[0]]:
            _finding(f, "FAIL", "structure.selector", f"selector {sel[0]} needs {SELECTORS[sel[0]]} argument(s)", sid)
            continue
        if sel[0] == "delivery":
            need = DELIVERY_CHECKS.get(sel[1]) if isinstance(sel[1], str) else None
            if need is None or len(sel) - 2 < need:
                _finding(f, "FAIL", "structure.selector", f"unknown delivery check {sel[1:]!r}", sid)
                continue
        if sel[0] in ("text", "link") and (not isinstance(sel[1], str) or (
                sel[1] not in deliverables and sel[1] not in ("slide", "tracker", "email", "slack"))):
            _finding(f, "FAIL", "structure.selector", f"{sel[0]} target {sel[1]!r} is not a deliverable", sid)
        if sel[0] == "field":
            # the field's table is the one whose key_regex matches the key, never assumed to be the first table
            ftn, ftsp = _table_for_key(table_deliverables(surface), sel[1])
            if ftsp is None:
                _finding(f, "FAIL", "structure.selector",
                         f"field key {sel[1]!r} matches no table deliverable's key_regex", sid)
            elif sel[2] not in (ftsp.get("columns") or []):
                _finding(f, "FAIL", "structure.selector", f"column {sel[2]!r} is not a column of table {ftn!r}", sid)
        if sel[0] in ("total", "printed_total") and classes and sel[1] not in classes:
            _finding(f, "FAIL", "structure.selector", f"class {sel[1]!r} is not in classes {classes}", sid)
        if sel[0] in ("reason_matches", "text"):
            try:
                if not isinstance(sel[2], str):
                    raise TypeError(f"{type(sel[2]).__name__} is not a regex string")
                re.compile(sel[2])
            except (re.error, TypeError) as error:
                _finding(f, "FAIL", "structure.selector", f"bad regex {sel[2]!r}: {error}", sid)
        if sel[0] == "tracker_entry":
            if not isinstance(sel[3], list) or not sel[3]:
                _finding(f, "FAIL", "structure.selector", "tracker_entry needs a non-empty list of value patterns", sid)
            else:
                for rx in [sel[1]] + list(sel[3]):
                    try:
                        re.compile(str(rx))
                    except re.error as error:
                        _finding(f, "FAIL", "structure.selector", f"bad regex {rx!r}: {error}", sid)
        w, wk = s.get("weight"), s.get("work_kind")
        if w not in (1, 3, 5):
            _finding(f, "FAIL", "weights.band", f"weight {w!r} is not 1, 3 or 5", sid)
        elif wk not in WORK_BANDS:
            _finding(f, "FAIL", "weights.work_kind", f"work_kind {wk!r} not one of {sorted(WORK_BANDS)}", sid)
        elif WORK_BANDS[wk] != w:
            _finding(f, "FAIL", "weights.band", f"weight {w} but work kind {wk} is band {WORK_BANDS[wk]}", sid)
        if not str(s.get("work_reason") or "").strip():
            _finding(f, "FAIL", "weights.reason", "work_reason missing (why this kind of work)", sid)
        if s.get("class") not in CLASSES:
            _finding(f, "FAIL", "structure.class", f"class {s.get('class')!r} not one of {CLASSES}", sid)
        if role(s) not in ROLES:
            _finding(f, "FAIL", "structure.role", f"role {role(s)!r} not one of {ROLES}", sid)
    for problem in gradeable(surface):
        _finding(f, "FAIL", "gradeable.slot", problem["reason"], problem["slot"])
    if truth is not None:
        for problem in truth_group_problems(truth, surface):
            _finding(f, "FAIL", "gradeable.truth", problem)
    # one fact, at most two slots (V3 §9: the same fact in three or more rows fails)
    facts = collections.defaultdict(list)
    for s in slots:
        facts[fact_id(s)].append(s.get("id"))
    for fid, members in facts.items():
        if len(members) >= 3:
            _finding(f, "FAIL", "duplicates.fact", f"fact {fid} graded in {len(members)} slots {members} (V3 §9: >= 3 fails)")
    # spot-check sampling: <= 5 samples per group plus a volume row; exceptions named by an authority
    groups = collections.defaultdict(list)
    volumes = set()
    for s in slots:
        g = slot_group(s, tname or "register")
        r = role(s)
        if r == "volume":
            volumes.update(s.get("volume_for") or ([g] if g else []))
        elif r == "sample" and g:
            groups[g].append(s.get("id"))
        elif r == "exception":
            who = s.get("singled_out_by")
            if not who:
                _finding(f, "FAIL", "exceptions.singled_out_by", "an exception slot must name the authority or fragment "
                         "that singles the member out", s.get("id"))
            elif manifest is not None:
                known = {a.get("id") for a in manifest.get("authorities", []) or []} | \
                        {x.get("id") for x in manifest.get("ask_fragments", []) or []} | \
                        {a.get("id") for a in manifest.get("anchors", []) or []}
                if who not in known:
                    _finding(f, "FAIL", "exceptions.singled_out_by", f"singled_out_by {who!r} is not an authority, "
                             f"fragment or anchor of the manifest", s.get("id"))
    for g, members in sorted(groups.items()):
        if len(members) > SAMPLE_LIMIT:
            _finding(f, "FAIL", "sampling.limit", f"group {g} has {len(members)} samples {members} (<= {SAMPLE_LIMIT}; "
                     "/rubric reads more as an overlap group)")
        covered = g in volumes or any(v.endswith(":*") and g.startswith(v[:-1]) for v in volumes)
        if not covered:
            _finding(f, "FAIL", "sampling.volume", f"sampled group {g} has no volume slot (role volume, volume_for)")
    # mechanisms name real rules
    known_rules = set(rule_ids or []) | {p.get("id") for p in (manifest or {}).get("mechanism_portfolio", []) or []}
    if known_rules:
        for s in slots:
            bad = [m for m in s.get("mechanisms") or [] if m not in known_rules]
            if bad:
                _finding(f, "FAIL", "mechanisms.known", f"mechanisms {bad} are not solver rules / portfolio ids", s.get("id"))
    total = sum(s.get("weight") or 0 for s in slots)
    by_class = collections.Counter()
    mech = 0
    for s in slots:
        by_class[s.get("class")] += s.get("weight") or 0
        if s.get("mechanisms") or s.get("flipped_by"):
            mech += s.get("weight") or 0
    ungraded = [s.get("id") for s in slots if s.get("gradable") is False]
    report = {"slots": len(slots), "total_weight": total, "weight_by_class": dict(by_class),
              "mechanism_weight": mech, "mechanism_share": round(mech / total, 4) if total else 0.0,
              "always_pass_share_if_no_mechanism_lands": round((total - mech) / total, 4) if total else 0.0,
              "ungraded_slots": ungraded, "groups": {g: len(m) for g, m in sorted(groups.items())},
              "note": "geometry (mechanism share, always-pass share) is reported, never gated (plan §4.6)"}
    fails = [x for x in f if x["severity"] == "FAIL"]
    return {"verdict": "FAIL" if fails else "PASS", "findings": f, "report": report}


def to_text(r: dict, name: str = "surface") -> str:
    rep = r["report"]
    lines = [f"GRADABLE SURFACE ({name}): {r['verdict']} · {rep['slots']} slots · weight {rep['total_weight']} · "
             f"mechanism share {rep['mechanism_share']:.1%} (reported, not gated) · "
             f"weight by class {rep['weight_by_class']}"]
    for x in r["findings"]:
        lines.append(f"  [{x['severity']}] {x['check']}" + (f" {x['slot']}" if x["slot"] else "") + f": {x['detail']}")
    return "\n".join(lines)


# ------------------------------------------------------------------ conversion from a proxy slot list

SELECTOR_CLASS = {"field": "direct", "group_key": "direct", "groups_of": "direct", "sole_reason": "direct",
                  "reason_matches": "direct", "total": "aggregate", "printed_total": "aggregate",
                  "group_count": "aggregate", "group_size": "aggregate", "tracker_lists": "aggregate",
                  "tracker_count": "aggregate", "tracker_entry": "write_content", "text": "write_content",
                  "link": "delivery", "delivery": "delivery"}
WEIGHT_KIND = {1: "lookup", 3: "interpretation", 5: "multi_source_reconciliation"}


def from_slots(slots_doc: dict, *, task: str, revision: str, sql_sha256: str | None, deliverables: dict,
               classes: list, singled_out: dict | None = None, mechanisms: dict | None = None,
               reason: str = "weight carried from the source rubric; work kind inferred from the 1/3/5 band") -> dict:
    """A surface from a proxy slot list ({"slots": [{id, weight, selector, title}]}). Work kinds are inferred from
    the weight band (stated in work_reason); exceptions are the keys `singled_out` maps to an authority."""
    singled_out = singled_out or {}
    mechanisms = mechanisms or {}
    tname, _ = next(((k, v) for k, v in deliverables.items() if v.get("kind") == "table"), ("register", None))
    xname, _ = next(((k, v) for k, v in deliverables.items() if v.get("kind") == "text"), ("tracker", None))
    out = []
    for s in slots_doc["slots"]:
        sel = list(s["selector"])
        slot = {"id": s["id"], "title": s.get("title", ""), "weight": s["weight"],
                "work_kind": WEIGHT_KIND.get(s["weight"]), "work_reason": reason,
                "class": SELECTOR_CLASS.get(sel[0], "direct"), "selector": sel}
        if sel[0] == "field":
            slot["group"] = f"{tname}:{sel[2]}"
            if sel[1] in singled_out:
                slot["role"], slot["singled_out_by"] = "exception", singled_out[sel[1]]
            else:
                slot["role"] = "sample"
        elif sel[0] in ("group_key", "groups_of"):
            slot["group"] = f"{xname}:membership"
            slot["role"] = "sample"
        elif sel[0] == "delivery" and sel[1] == "register_keys_exact":
            slot["role"], slot["volume_for"] = "volume", [f"{tname}:*"]
        elif sel[0] in ("group_count", "group_size"):
            slot["role"], slot["volume_for"] = "volume", [f"{xname}:membership"]
        else:
            slot["role"] = "core"
        if s["id"] in mechanisms:
            slot["mechanisms"] = list(mechanisms[s["id"]])
        out.append(slot)
    return {"kind": "GRADABLE_SURFACE", "version": VERSION, "task": task, "revision": revision, "sql_sha256": sql_sha256,
            "classes": classes, "truth_fields": {"class": "handoff class", "groups": "groups"},
            "deliverables": deliverables, "slots": out,
            "provenance": {"converted_from": slots_doc.get("source") or slots_doc.get("kind"),
                           "rule": "from-slots: work kinds inferred from weights; roles from the selector kind"}}


# ------------------------------------------------------------------ self-test

def _sample_surface() -> dict:
    deliverables = {"register": {"kind": "table", "name_regex": "register", "key_column": "key", "key_regex": r"K-\d{2}",
                                 "columns": ["key", "state", "class"], "class_column": "class",
                                 "comparators": {"state": "norm"}},
                    "tracker": {"kind": "text", "tool": "linear_update_issue", "issue": "ZOM-1", "key_regex": r"K-\d{2}",
                                "groups": [["late", "late"]]}}
    slots = [{"id": "S1", "weight": 5, "work_kind": "multi_source_reconciliation", "work_reason": "joins three sources",
              "class": "direct", "selector": ["field", "K-01", "class"], "role": "sample"},
             {"id": "S2", "weight": 3, "work_kind": "interpretation", "work_reason": "house rule", "class": "direct",
              "selector": ["field", "K-02", "state"], "role": "exception", "singled_out_by": "H1"},
             {"id": "S3", "weight": 3, "work_kind": "calculation", "work_reason": "counts rows", "class": "aggregate",
              "selector": ["total", "HOLD"], "role": "core"},
             {"id": "S4", "weight": 3, "work_kind": "calculation", "work_reason": "volume of the register",
              "class": "aggregate", "selector": ["delivery", "register_keys_exact"], "role": "volume",
              "volume_for": ["register:*"]},
             {"id": "S5", "weight": 1, "work_kind": "lookup", "work_reason": "write exists", "class": "delivery",
              "selector": ["delivery", "slide_updated"], "role": "core"}]
    return {"kind": "GRADABLE_SURFACE", "version": VERSION, "task": "t", "revision": "r1", "classes": ["READY", "HOLD"],
            "truth_fields": {"class": "class", "groups": "groups"}, "truth_keys": ["K-01", "K-02"],
            "deliverables": deliverables, "slots": slots}


# the selector-class fixture surface for the surface.gradeable dry run: one slot per class, plus a second table
def _dry_run_surface() -> dict:
    deliverables = {
        "register": {"kind": "table", "name_regex": "^Q4 pack$", "key_column": "asset", "key_regex": r"^K-\d{2}$",
                     "columns": ["asset", "state", "class", "reason"], "class_column": "class",
                     "reason_column": "reason", "comparators": {"state": "norm"}},
        "pack": {"kind": "table", "name_regex": "^Storefronts$", "key_column": "storefront",
                 "key_regex": r"^[A-Z]{2}/ios$", "columns": ["storefront", "wave", "slots"], "class_column": "wave"},
        "tracker": {"kind": "text", "tool": "linear_update_issue", "issue": "T-1", "key_regex": r"K-\d{2}",
                    "groups": [["late", "late"]]},
        "tickets": {"kind": "json_text", "tool": "linear_create_issue"},
        "summary": {"kind": "json_text", "tool": "slack_conversations_add_message"},
        "mail": {"kind": "json_text", "tool": "gmail_send_email"},
        "trello": {"kind": "calls", "tool": "trello_add_comment_to_card"}}
    slots = [
        ("F-REG", ["field", "K-01", "class"]), ("F-PACK", ["field", "DE/ios", "wave"]),
        ("TOT", ["total", "READY"]), ("PTOT", ["printed_total", "READY"]),
        ("GC", ["group_count", "late"]), ("GS", ["group_size", "late"]), ("GK", ["group_key", "K-01", "late"]),
        ("GOS", ["groups_of", "K-01"]), ("SRE", ["sole_reason", "K-01", "late"]),
        ("RM", ["reason_matches", "K-01", "why"]),
        ("TX-REG", ["text", "register", "state"]), ("TX-PACK", ["text", "pack", "wave"]),
        ("TX-TICKETS", ["text", "tickets", "ART-1"]), ("TX-SUMMARY", ["text", "summary", "SHIP 38"]),
        ("TX-MAIL", ["text", "mail", "marcus@x.co"]),
        ("TL", ["tracker_lists", "late", "K-01"]), ("TC", ["tracker_count", "late", 3]),
        ("TE", ["tracker_entry", "late", "K-01", ["why"]]),
        ("D-CSV", ["delivery", "register_is_csv"]),
        ("D-KEYS", ["delivery", "register_keys_exact"]),
        ("D-SHARE", ["delivery", "share_reader"]), ("D-SLIDE", ["delivery", "slide_updated"]),
        ("D-ST-C", ["delivery", "tracker_state", "comment"]),
        ("D-ST-RX", ["delivery", "tracker_state", "Done"]),
        ("D-PRES", ["delivery", "tracker_preserves", "kept"]),
        ("D-MAIL", ["delivery", "email_reply", "m1"]),
        ("D-THREAD", ["delivery", "slack_thread", "1758901200.000000"]),
        ("D-POST", ["delivery", "slack_channel_post", "C1", "hello"]),
        ("D-CARD", ["delivery", "trello_card", "C1", "hello"]),
        ("D-AFTER", ["delivery", "slack_after_email"]),
        ("D-PARENT", ["delivery", "register_parent", "PARENT1"]),
        ("LINK", ["link", "register"]), ("LINK-S", ["link", "summary"])]
    out = []
    for sid, sel in slots:
        kind = "delivery" if sel[0] == "delivery" else {"field": "direct", "group_key": "direct",
                                                        "groups_of": "direct", "sole_reason": "direct",
                                                        "reason_matches": "direct", "total": "aggregate",
                                                        "printed_total": "aggregate", "group_count": "aggregate",
                                                        "group_size": "aggregate", "tracker_lists": "aggregate",
                                                        "tracker_count": "aggregate", "tracker_entry": "write_content",
                                                        "text": "write_content", "link": "delivery"}.get(sel[0], "direct")
        out.append({"id": sid, "weight": 3, "work_kind": "interpretation", "work_reason": "dry-run fixture",
                    "class": kind, "role": "core", "selector": sel})
    return {"kind": "GRADABLE_SURFACE", "version": VERSION, "task": "dry", "revision": "r1",
            "classes": ["READY", "HOLD"], "truth_fields": {"class": "class", "groups": "groups"},
            "truth_keys": ["K-01"], "deliverables": deliverables, "slots": out}


def _self_test() -> None:
    good = _sample_surface()
    manifest = {"authorities": [{"id": "H1"}], "ask_fragments": [], "mechanism_portfolio": [{"id": "M1"}]}
    r = validate(good, manifest)
    assert r["verdict"] == "PASS", to_text(r)
    rows = {"K-01": {"class": "HOLD", "state": "late", "groups": ["late"]},
            "K-02": {"class": "READY", "state": "ok", "groups": []}}
    s = {x["id"]: x for x in good["slots"]}
    assert solver_value(s["S1"], rows, good) == "HOLD" and solver_value(s["S3"], rows, good) == 1
    assert solver_value(s["S5"], rows, good) is NOT_SOLVER and slot_keys(s["S2"]) == ["K-02"]

    planted = set()

    def bad(mut, check):
        x = json.loads(json.dumps(good))
        mut(x)
        res = validate(x, manifest)
        got = [y["check"] for y in res["findings"] if y["severity"] == "FAIL"]
        assert res["verdict"] == "FAIL" and check in got, (check, got)
        assert all(y["basis"] == FAMILY_BASIS[y["check"].split(".")[0]] for y in res["findings"]), res["findings"]
        planted.add(check)
    bad(lambda x: x.update(kind="GRADABLE_SURFACE_REVISION_99"), "structure.kind")
    bad(lambda x: x["deliverables"].update(notes={"kind": "poem"}), "structure.deliverable")
    bad(lambda x: x["deliverables"]["register"].pop("key_column"), "structure.deliverable")
    bad(lambda x: x.update(slots=[]), "structure.slots")
    bad(lambda x: x["slots"][1].update(id="S1"), "structure.slot_ids")
    bad(lambda x: x["slots"][0].update({"class": "vibes"}), "structure.class")
    bad(lambda x: x["slots"][0].update(role="mascot"), "structure.role")
    bad(lambda x: x["slots"][0].update(weight=3), "weights.band")                           # kind says 5
    bad(lambda x: x["slots"][0].update(work_kind="vibes"), "weights.work_kind")
    bad(lambda x: x["slots"][0].update(work_reason=""), "weights.reason")
    bad(lambda x: x["slots"][1].pop("singled_out_by"), "exceptions.singled_out_by")
    bad(lambda x: x["slots"][1].update(singled_out_by="H9"), "exceptions.singled_out_by")   # not in the manifest
    bad(lambda x: x["slots"].extend(dict(x["slots"][2], id=f"S3{c}") for c in "ab"), "duplicates.fact")
    bad(lambda x: x["slots"].extend({**x["slots"][0], "id": f"Z{i}", "selector": ["field", f"K-1{i}", "class"]}
                                    for i in range(5)), "sampling.limit")
    bad(lambda x: x["slots"].pop(3), "sampling.volume")
    bad(lambda x: x["slots"][0].update(selector=["field", "K-01", "colour"]), "structure.selector")
    bad(lambda x: x["slots"][0].update(selector=["nonsense", 1]), "structure.selector")
    bad(lambda x: x["slots"][4].update(selector=["delivery", "teleport"]), "structure.selector")
    bad(lambda x: x["slots"][0].update(mechanisms=["M9"]), "mechanisms.known")
    bad(lambda x: x["deliverables"]["register"]["comparators"].update(state="fuzzy"), "structure.comparator")
    # surface.gradeable: one planted case per targeted selector class
    bad(lambda x: (x["slots"][0].update(selector=["group_count", "late"]),
                   x["truth_fields"].update(groups="state")), "gradeable.slot")   # a table column is not a group list
    bad(lambda x: x["slots"][4].update(selector=["delivery", "slack_thread", "C05433XK267"]), "gradeable.slot")
    bad(lambda x: x["slots"][4].update(selector=["delivery", "tracker_state", "5f8e7d6c9a1b2c3d4e5f6071"]),
        "gradeable.slot")
    def _reg_core(x):
        x.pop("truth_keys")
        x["slots"][3].update(role="core")
        x["slots"][3].pop("volume_for", None)
    bad(_reg_core, "gradeable.slot")
    # malformed delivery selectors must FAIL normally, never IndexError inside gradeable()
    for _sel in (["delivery", "slack_thread"], ["delivery", "tracker_state"], 1, ["total"], ["field", "K-01"]):
        x = json.loads(json.dumps(good))
        x["slots"][4]["selector"] = _sel
        res = validate(x, manifest)
        assert res["verdict"] == "FAIL" and any(y["check"] == "structure.selector" for y in res["findings"]), res
    # surface.gradeable is a real decoder dry run: one fixture per selector class reads True, and each class turns
    # ungradable when its source, table or argument cannot be read
    dry = _dry_run_surface()
    assert {s["selector"][0] for s in dry["slots"]} == set(SELECTORS), \
        (sorted({s["selector"][0] for s in dry["slots"]}), sorted(SELECTORS))
    rep = gradeable_report(dry)
    assert not rep["counts"].get("UNGRADABLE"), [x for x in rep["slots"] if x["status"] == "UNGRADABLE"]

    def ungradable(mut, sid):
        x = json.loads(json.dumps(dry))
        mut(x)
        got = {r["slot"]: r for r in gradeable_report(x)["slots"]}
        assert got[sid]["status"] == "UNGRADABLE", (sid, got[sid])
        planted.add("gradeable.slot")
    ungradable(lambda x: x["deliverables"].pop("tracker"), "GC")
    ungradable(lambda x: x["deliverables"].pop("tracker"), "TL")
    ungradable(lambda x: x["deliverables"].pop("tracker"), "D-ST-RX")
    ungradable(lambda x: x["deliverables"].pop("pack"), "F-PACK")
    ungradable(lambda x: x["deliverables"].pop("tickets"), "TX-TICKETS")
    ungradable(lambda x: x["slots"][1].update(selector=["field", "DE/ios", "decision"]), "F-PACK")
    ungradable(lambda x: x["slots"][14].update(selector=["text", "mail", "(?<=x)y"]), "TX-MAIL")
    ungradable(lambda x: x.pop("truth_keys"), "D-KEYS")
    # R3-4: a heading *regex* and a regex-constrained count must both produce a readable fixture
    hd = json.loads(json.dumps(dry))
    hd["slots"][15].update(selector=["tracker_lists", r"owner\s+calls", "K-01"])
    hd["slots"][16].update(selector=["tracker_count", r"owner\s+calls", 2])
    rep_hd = gradeable_report(hd)
    assert not [x for x in rep_hd["slots"] if x["status"] == "UNGRADABLE" and x["slot"] in ("TL", "TC")], rep_hd
    kd = json.loads(json.dumps(dry))
    kd["deliverables"]["tracker"]["key_regex"] = r"K-(?:01|03)"
    kd["slots"][16].update(selector=["tracker_count", "late", 2])
    rep_kd = gradeable_report(kd)
    assert not [x for x in rep_kd["slots"] if x["status"] == "UNGRADABLE" and x["slot"] == "TC"], rep_kd
    # R3-5: the report and the validator agree (a channel id in a slack_thread slot is rejected by both)
    bad_ts = json.loads(json.dumps(dry))
    bad_ts["slots"][27].update(selector=["delivery", "slack_thread", "C05433XK267"])
    assert gradeable_report(bad_ts)["verdict"] == "FAIL"
    assert any(x["check"] == "gradeable.slot" for x in validate(bad_ts, manifest)["findings"])
    # a group value must be a list: a scalar is not membership
    assert truth_group_problems({"K-01": {"groups": "late"}}, dry)
    assert not truth_group_problems({"K-01": {"groups": ["late"]}}, dry)
    v = validate(dry, manifest, truth={"K-01": {"groups": "late"}})
    assert any(y["check"] == "gradeable.truth" for y in v["findings"]), v["findings"]
    planted.add("gradeable.truth")
    # every blocking family has a planted defect
    assert {c.split(".")[0] for c in planted} == set(FAMILY_BASIS), sorted(planted)
    # geometry is report-only: no mechanism on any slot (mechanism share 0, always-pass share 1) still PASSES
    flat_geo = json.loads(json.dumps(good))
    for x in flat_geo["slots"]:
        x.pop("mechanisms", None), x.pop("flipped_by", None)
    rg = validate(flat_geo, manifest)
    assert rg["verdict"] == "PASS" and rg["report"]["mechanism_share"] == 0.0, to_text(rg)
    assert rg["report"]["always_pass_share_if_no_mechanism_lands"] == 1.0, rg["report"]
    conv = from_slots({"slots": [{"id": "R1", "weight": 3, "selector": ["field", "K-01", "class"], "title": "t"},
                                 {"id": "R2", "weight": 1, "selector": ["delivery", "register_keys_exact"], "title": "v"}]},
                      task="t", revision="r", sql_sha256=None, deliverables=good["deliverables"], classes=["HOLD"],
                      singled_out={"K-01": "H1"})
    conv["truth_keys"] = ["K-01"]                    # the dry-run needs an explicit expected key set
    assert validate(conv, manifest)["verdict"] == "PASS", to_text(validate(conv, manifest))
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("gradable_surface_selftest_") as tmp:
        p = Path(tmp) / "s.json"
        p.write_text(json.dumps(good))
        assert load(p)["kind"] == "GRADABLE_SURFACE"
    print(f"self-test: ok (good surface PASS; {len(planted)} planted defects over every blocking family "
          f"({', '.join(sorted(FAMILY_BASIS))}) each FAIL their own check with its basis; geometry report-only (0 % "
          f"mechanism share still PASSES); solver values; conversion)")


# ------------------------------------------------------------------ main

def _manifest_for(task_dir: Path | None, path: Path | None):
    if path:
        return json.loads(Path(path).read_text())
    if task_dir:
        for name in ("01_Hardness_Manifest.json", "01_Hardness_Manifest.draft.json"):
            p = task_dir / "Working_Files" / name
            if p.is_file():
                return json.loads(p.read_text())
    return None


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="gradable_surface.py", description="gradable surface schema and validator")
    ap.add_argument("command", nargs="?", choices=("validate", "from-slots", "gradeable-report"))
    ap.add_argument("path", nargs="?", type=Path)
    ap.add_argument("--task-dir", type=Path)
    ap.add_argument("--manifest", type=Path)
    ap.add_argument("--solver", type=Path, help="a solver.py whose RULES keys are the known mechanisms")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--task", default="task")
    ap.add_argument("--revision", default="r1")
    ap.add_argument("--sql", type=Path)
    ap.add_argument("--deliverables", type=Path)
    ap.add_argument("--classes", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        _self_test()
        return 0
    if a.command == "validate":
        path = a.path or (a.task_dir / "Working_Files" / "01_Gradable_Surface.json" if a.task_dir else None)
        if not path or not path.is_file():
            print("gradable_surface: no surface file (give a path or --task-dir)", file=sys.stderr)
            return 2
        rules = None
        if a.solver:
            import oracle_kit
            rules = list(oracle_kit.load_solver(a.solver).RULES)
        r = validate(load(path), _manifest_for(a.task_dir, a.manifest), rules)
        print(json.dumps(r, indent=1) if a.json else to_text(r, path.name))
        return 0 if r["verdict"] == "PASS" else 1
    if a.command == "gradeable-report":
        path = a.path or (a.task_dir / "Working_Files" / "01_Gradable_Surface.json" if a.task_dir else None)
        if not path or not path.is_file():
            print("gradable_surface: no surface file (give a path or --task-dir)", file=sys.stderr)
            return 2
        rep = gradeable_report(load(path))
        if a.out:
            a.out.parent.mkdir(parents=True, exist_ok=True)
            a.out.write_text(json.dumps(rep, indent=1, ensure_ascii=False) + "\n")
        if not a.json:
            print(f"SURFACE.GRADEABLE {rep['verdict']} · {len(rep['slots'])} slot(s) · {rep['counts']}")
            for x in rep["slots"]:
                if x["status"] != "GRADABLE":
                    print(f"  [{x['status']}] {x['slot']} w={x['weight']} {x['kind']}: {x['reason']}")
        else:
            print(json.dumps(rep, indent=1, ensure_ascii=False))
        return 0 if rep["verdict"] == "PASS" else 1
    if a.command == "from-slots":
        if not a.path or not a.out or not a.deliverables:
            print("from-slots needs SLOTS.json, --out and --deliverables", file=sys.stderr)
            return 2
        from trajectory_ledger import safe_out
        doc = json.loads(a.path.read_text())
        dl = json.loads(a.deliverables.read_text())
        sql_sha = hashlib.sha256(a.sql.read_bytes()).hexdigest() if a.sql else None
        s = from_slots(doc, task=a.task, revision=a.revision, sql_sha256=sql_sha, deliverables=dl["deliverables"],
                       classes=[c for c in a.classes.split(",") if c], singled_out=dl.get("singled_out"),
                       mechanisms=dl.get("mechanisms"))
        out = safe_out(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(s, indent=1, ensure_ascii=False) + "\n")
        print(f"wrote {out}")
        return 0
    ap.print_usage(sys.stderr)
    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"gradable_surface: {error}", file=sys.stderr)
        raise SystemExit(2)

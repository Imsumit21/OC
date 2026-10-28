#!/usr/bin/env python3
"""surface_grader.py - grade trajectories against the gradable surface, then run the difficulty gates.

Plan §7.10: score any set of trajectories (harness runs or platform exports) on Working_Files/01_Gradable_Surface.json
so the four difficulty gates can be computed right after the runs, before any rubric or verifier exists. This checks
the DESIGN; the rubric and the verifier remain the grading of record. Read-only, stdlib only, never executes SQL.

  1. Each run's writes are decoded by trajectory_ledger.py (table deliverable, tracker text, write calls). The
     tracker content is REPLAYED: a full description and a "replace /description" string replace it, append/prepend
     modify it in order, and an unreadable content mutation makes it unknown (every tracker slot UNGRADED, including
     tracker_preserves) unless a later full description re-establishes it. The register identity is the decoded
     table's own file id / spreadsheet id, never the last share.
  2. Every surface slot is compared with the truth (solver output) through the slot's comparator; every fair reading
     the surface accepts passes. The rules are those of support/analysis/season_pass_runs_rev14_fixed.py, generalised
     and hardened (G1, 2026-10-25; round 2 the same day):
       field      the written value equals the truth under the column's comparator: issue_key (word match),
                  pr_number (#N, /pull/N, PR N), sha_prefix (exact, or an unambiguous 7-39 hex prefix), yes_no
                  (aliases), norm (letters and digits, case-folded); an expected None accepts the missing spellings
       total      classes counted from the written rows equal the truth's counts
       group_*    tracker groups (same-line or heading-then-keys) compared with the truth's group membership; a line
                  is prose, never a group, only when every key occurrence on it is a range endpoint
                  ("SP-001..SP-128"), so an explicitly listed member survives beside a cohort range
       tracker_*  a section starts at the heading-like line that matches (markdown heading, bold line, short line
                  ending in ':'), not at a first mention, and runs to the next heading-like line; exact counts read
                  the list-like lines (a table row's first cell, every key of a bare key list, a prose bullet's
                  first key), where a bare key list is a grammatical list: keys joined only by separators or
                  and/or, nothing after the last key but closing punctuation (G1-5; "K-01 blocks K-02" is prose);
                  updates name the tracking issue exactly (whitespace only, G1-7); a tracker_entry value must sit
                  after the entry's own key occurrence on the line (G1-8) and a SHA value matches an unambiguous
                  prefix of 7 or more characters, resolved against the known hashes without the selector's own
                  pattern (G1-6)
       text/link  the plain strings of the target writes match (re.S), not their JSON dump; a link is the decoded
                  table's identity (its file id / spreadsheet id) appearing in the deliverable, and only when a
                  share call names that register (G1-11)
       delivery   register_is_csv, register_keys_exact, register_parent (the shared register's final folder),
                  share_reader, slide_updated (every slide update counts), tracker_state and tracker_preserves
                  (every tracker update in order), email_reply (a call replying to the expected message_id with
                  reply_all false, both bound to the call's parameters), slack_thread (the call's thread_ts),
                  slack_after_email; slack_conversations_add_message counts as slack_send_message
     UNGRADED, never false: a slot marked "gradable": false (it is an unknown cell in the gate matrix and in the
     per-run score bounds; coverage stays metadata), and every slot that reads a register or tracker write the
     decoder can't read. Coverage = graded weight / total weight. The revision-14 surface format is converted on
     load (gradable_surface.from_revision14), keeping a gradable flag.
  3. The rubric x rollout matrix goes to tools/difficulty_stats.compute() (the only owner of gate math). The gate
     view follows the task context: V3 (difficulty mode from 00_Task_Context) or V2. When any run's models are not
     the context's baseline model both views are printed (a 4.8 run is never V3 evidence); provenance gates
     (errored runs, horizon, baseline models) are reported apart from the four difficulty gates.
     With UNGRADED cells (every None cell of a completed run, declared ungradable ones included), the average and
     full-pass verdicts come from two bounds (every UNGRADED cell failed, every one passed) and stand only when both
     agree; the SD band and the failure patterns stand only when every completion of the UNGRADED cells agrees (up
     to 2^12). Otherwise the gate is INCOMPLETE; the cells are listed.
  4. Each failed slot names who decided it (V1): the briefs that name its keys and the write calls, with their
     models (trajectory_ledger.deciders).

Usage:
  python3 -B Task_Authoring/tools/surface_grader.py --task-dir DIR [--surface S] [--truth truth.json | --solver
      solver.py --sql SQL | --oracle-dir DIR --sql SQL] [--run LABEL=PATH ...] [--views auto|v2|v3|both]
      [--compare reference.json] [--official 12_difficulty_input.json] [--out OUT.json]
  python3 -B Task_Authoring/tools/surface_grader.py --self-test
Labels "precheck" (or "pre") are graded but left out of the six-run gates.
Exit 0 = graded (gates may fail; they are reported), 1 = a compared reference disagrees, 2 = usage error.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import importlib.util
import itertools
import json
import re
import sys
import tempfile
from pathlib import Path


def _bundle() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "difficulty_stats.py").is_file():
            return parent
    raise SystemExit("surface_grader: cannot find the Task_Authoring bundle (no tools/difficulty_stats.py above)")


HERE = Path(__file__).resolve().parent
BUNDLE = _bundle()
for _p in (BUNDLE / "tools", HERE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import difficulty_stats as ds  # noqa: E402  (gate math has one owner)
import gradable_surface as gs  # noqa: E402  (surface parsing has one owner)
import trajectory_ledger as tl  # noqa: E402  (run facts have one owner)

VERSION = "surface_grader/1"
DIFFICULTY_GATES = ("pass_at_1", "avg_weighted_pass_rate", "per_rollout_sd", "failure_patterns")
PROVENANCE_GATES = ("errored_runs", "horizon", "baseline_models")
PRE_LABELS = ("precheck", "pre")


# ------------------------------------------------------------------ comparators (ported compare())

def compare(actual, expected, column: str, table_spec: dict) -> str:
    """MATCH / DIFFERENT for one written cell against the truth value."""
    norm = tl.norm
    actual = str(actual)
    if expected is None:
        missing = set(table_spec.get("missing_values") or tl.MISSING)
        return "MATCH" if norm(actual) in {norm(m) for m in missing} else "DIFFERENT"
    comp = (table_spec.get("comparators") or {}).get(column, "norm")
    if comp == "yes_no":
        yn = table_spec.get("yes_no") or {"yes": ["yes", "true", "1", "active"],
                                          "no": ["no", "false", "0", "inactive", "notactive"]}
        aliases = {k: {norm(x) for x in v} for k, v in yn.items()}
        return "MATCH" if norm(actual) in aliases.get(str(expected), {norm(expected)}) else "DIFFERENT"
    if comp == "pr_number":
        number = str(expected).split("#")[-1]
        return "MATCH" if re.search(r"(?:#|/pull/|\bPR\s*)" + re.escape(number) + r"\b", actual, re.I) else "DIFFERENT"
    if comp == "issue_key":
        return "MATCH" if re.search(r"\b" + re.escape(str(expected)) + r"\b", actual, re.I) else "DIFFERENT"
    if comp == "sha_prefix":
        a = actual.casefold()
        if a == str(expected).casefold():
            return "MATCH"
        if 7 <= len(a) < 40 and re.fullmatch("[0-9a-f]+", a) and str(expected).casefold().startswith(a):
            return "MATCH"
        return "DIFFERENT"
    return "MATCH" if norm(actual) == norm(expected) else "DIFFERENT"


# ------------------------------------------------------------------ tracker text (ported season_pass_runs_rev14_fixed)
# G1 (2026-10-25): the eight decoder defects the revision-14 runs exposed. (1) a section starts at the heading-like line
# that matches, not the first mention; (2) it runs to the next heading-like line, past intro prose and table headers;
# (3) `text` selectors search the plain strings of the inputs, not their JSON dump; (4) tracker state and preservation
# read every successful update in order; (5) a bullet that holds a bare key list counts every key; (6) a line that
# names keys only as a range ("SP-001..SP-128") is prose, never a group; (7) tool aliases: a Slack message sent with
# slack_conversations_add_message counts like slack_send_message; (8) a SHA value in a tracker entry matches an
# unambiguous prefix of 7 or more characters. Content the decoder can't read is UNGRADED, never false.

TOOL_ALIASES = {"slack_send_message": ("slack_send_message", "slack_conversations_add_message")}
RX_HEX = re.compile(r"\b[0-9a-f]{7,40}\b")


def aliases(tool: str) -> tuple:
    return TOOL_ALIASES.get(tool, (tool,))


def _krx(spec: dict | None) -> str:
    return (spec or {}).get("key_regex") or r"SP-\d{3}"


def _group_of(head: str, groups_spec: list):
    h = head.lower()
    for g, pat in groups_spec:
        if pat in h:
            return g
    return None


def _range_only(line: str, krx: str) -> bool:
    """Every key the line names is an endpoint of a key range: prose about the cohort, not a key list (defect 6).

    G1-9/R2-1: compared as multisets, so an explicitly listed member that happens to duplicate a range endpoint
    ("Review (1): K-01; cohort K-01..K-20") keeps the line as prose only when no occurrence is left over. The range
    itself is found by position between two key matches, so a caller's named-group regex is never interpolated twice."""
    keys = collections.Counter(m.group(0) for m in re.finditer(krx, line))
    if not keys:
        return False
    ends = collections.Counter()
    for a, b in _range_pairs(line, krx):
        ends.update((a, b))
    return keys == ends


_RANGE_JOIN = re.compile(r"^\s*(?:\.\.|–|—|\bthrough\b|\bthru\b|\bto\b)\s*$", re.I)


def _range_pairs(line: str, krx: str) -> list:
    """[(a, b)] for every adjacent pair of key matches joined only by a range connector."""
    ms = list(re.finditer(krx, line))
    return [(a.group(0), b.group(0)) for a, b in zip(ms, ms[1:])
            if _RANGE_JOIN.match(line[a.end():b.start()])]


def _expand_range(a: str, b: str):
    """The keys of one cohort range (same prefix, same-width zero-padded suffix), or None if it is not a range."""
    ma, mb = re.fullmatch(r"(.*?)(\d+)", a), re.fullmatch(r"(.*?)(\d+)", b)
    if not ma or not mb or ma.group(1) != mb.group(1) or len(ma.group(2)) != len(mb.group(2)):
        return None
    start, end, width = int(ma.group(2)), int(mb.group(2)), len(ma.group(2))
    if end < start or end - start > 1000:
        return None
    return [f"{ma.group(1)}{n:0{width}d}" for n in range(start, end + 1)]


def _expand_keys(line: str, krx: str) -> list:
    """Every key the line names, with each range expanded to its members (R2-1); duplicates count once."""
    ms = list(re.finditer(krx, line))
    out, i = [], 0
    while i < len(ms):
        a = ms[i].group(0)
        if i + 1 < len(ms) and _RANGE_JOIN.match(line[ms[i].end():ms[i + 1].start()]):
            b = ms[i + 1].group(0)
            out.extend(_expand_range(a, b) or [a, b])
            i += 2
        else:
            out.append(a)
            i += 1
    return list(dict.fromkeys(out))


_DELIM_RE = re.compile(r"\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?")


def _table_row(s: str) -> bool:
    """A Markdown table row or header: an UNESCAPED pipe separator, and neither a heading nor a bullet list item (a
    bullet that carries a pipe is a list item, not a table row; an escaped pipe inside a cell does not unmake a row)."""
    t = s.lstrip()
    if re.match(r"#{1,6}(?: |$)", t) or re.match(r"[-*+](?:[ \t]+|$)", t):
        return False
    return "|" in s.replace("\\|", "")


def tracker_groups(text: str, spec: dict) -> dict:
    """Blocker groups as written: {group: (stated_count, [keys])}.

    A group stated with a count ("- Review not approved (2):") opens a *pending* group, and every following
    continuation line adds its keys: a bullet ('-', '*' or '+'), a bare key line, or a row of a Markdown table that
    follows its header/delimiter rows. A pending group is only ever opened for a group name the text has not stated
    yet, and a re-statement of a declared group never merges, so prose that re-mentions an existing group cannot
    re-open it.

    A table is recognised structurally: a header row whose NEXT non-empty line is a delimiter row, the delimiter row
    itself, and the data rows after it. A pipe in ordinary prose (or an escaped \\|) is NOT table structure and ends
    the pending group. A stated count is a number <= 500 (a parenthesised year is not a count).

    Deliberately not handled: a group re-stated later keeps its first statement (never merged); a prose line inside a
    list ends the pending group; a count in a table's own group row is not read as a pending count."""
    groups, pending = {}, None
    krx = _krx(spec)
    lines = text.split("\n")
    in_table, prev_header = False, False

    def _add(g0, cnt0, keys0):
        cur = groups.get(g0)
        if cur is None:
            groups[g0] = (cnt0, list(keys0))
        else:
            groups[g0] = (cur[0], list(dict.fromkeys(cur[1] + list(keys0))))

    for idx, line in enumerate(lines):
        s = line.strip()
        if not s:
            in_table = False                        # a blank line ends a table (a table is contiguous)
            continue
        nxt = next((x.strip() for x in lines[idx + 1:] if x.strip()), "")
        # a table delimiter must contain a pipe: a bare '---' is a horizontal rule, not a one-column delimiter
        is_header = _table_row(s) and "|" in nxt and bool(_DELIM_RE.fullmatch(nxt))
        is_delim = "|" in s and bool(_DELIM_RE.fullmatch(s)) and prev_header
        keys = _expand_keys(s, krx)
        first = re.search(krx, s)
        head = s[:first.start()] if first else s
        g = _group_of(head, spec.get("groups") or [])
        tail = re.sub(r"[\s*_:.)\-\u2014\u2013`]+$", "", head.strip())
        # a tail count is a number ending the head, but not a date or time fragment (2026-10-25, 09:30)
        tail_n = re.search(r"(?:^|[\s*_(\u2014\u2013])(\d+)$", tail)
        # a month name (full or abbreviated, optional period) before the number makes it a date phrase, not a count
        if tail_n and re.search(
                r"(?i)\b(january|february|march|april|may|june|july|august|september|october|november|december"
                r"|jan|feb|mar|apr|jun|jul|aug|sept|sep|oct|nov|dec)\.?\s+$", tail[:tail_n.start(1)]):
            tail_n = None
        nums = re.findall(r"\((\d+)\)", head) + ([tail_n.group(1)] if tail_n else [])
        cnt = next((int(x) for x in reversed(nums) if int(x) <= 500), None)   # fall back past an out-of-bound suffix

        # 1) structural rows first: a header never declares or contributes a member; a delimiter is structural
        if is_header or is_delim:
            prev_header, in_table = is_header, is_delim
            continue
        # 2) a data row of the current table contributes its keys to the pending group ONLY (never a declaration)
        if in_table and _table_row(s):
            if keys and pending:
                _add(pending[0], pending[1], keys)
            prev_header, in_table = False, True
            continue
        # 3) an escaped pipe is prose, even on a line carrying a key — but a BULLET is a list item, so its escaped
        # pipe is just cell text and the bullet still contributes its member
        if "\\|" in s and not re.match(r"[-*+](?:[ \t]+|$)", s.lstrip()):
            pending = None
            prev_header, in_table = False, False
            continue
        # 4) ordinary lines: declaration, re-declaration, range, continuation, heading, prose
        if keys and g and cnt is not None and g not in groups:
            groups[g] = (cnt, list(keys))
            pending = (g, cnt)
            prev_header, in_table = False, False
            continue
        if g and cnt is not None and g in groups:
            pending = None                              # a re-statement of a declared group is never merged
            prev_header, in_table = False, False
            continue
        if _range_only(s, krx):
            pending = None
            prev_header, in_table = False, False
            continue
        # a bullet under a pending group is a member line, whatever punctuation wraps its key (checkbox, backticks,
        # bold markers): the structural, escaped-pipe and declaration guards have already run
        bullet = bool(re.match(r"[-*+](?:[ \t]+|$)", s.lstrip()))
        bare = not head.strip(" \t*+-|:")
        if keys and pending and (bullet or bare):
            _add(pending[0], pending[1], keys)
            prev_header, in_table = False, False
            continue
        if not keys and g and cnt is not None and g not in groups and (len(s) < 160 or _headingish(s) or bullet):
            groups[g] = (cnt, [])                       # the first declaration is recorded at once (zero count too)
            pending = (g, cnt)
            prev_header, in_table = False, False
            continue
        pending = None
        prev_header, in_table = False, False
    return groups

def _headingish(line: str) -> bool:
    """A section heading is a markdown # line, a fully bold/underlined line, or a short colon-terminated line with no
    list marker and no ". "; a list item (even one ending in ':') is never a heading (R2-3)."""
    s = line.strip()
    if re.match(r"(?:[-*+]|\d+[.)])\s+", s):
        return False
    return bool(re.match(r"#{1,6}\s", s) or re.fullmatch(r"(\*\*|__)[^*_]+(\*\*|__):?", s)
                or (len(s) <= 80 and s.endswith(":") and ". " not in s))


def _section_start(lines: list, heading_regex: str, krx: str):
    """The heading line of the section headed by heading_regex, or None: the first matching heading-like line, else
    the first matching line that names keys after the match, else the first match (defect 1)."""
    hits = [i for i, line in enumerate(lines) if re.search(heading_regex, line, re.I)]
    if not hits:
        return None
    start = next((i for i in hits if _headingish(lines[i])), None)
    if start is None:
        start = next((i for i in hits if re.search(krx, lines[i][re.search(heading_regex, lines[i], re.I).end():])),
                     hits[0])
    return start


def _section_body(lines: list, start: int, krx: str) -> list:
    """Every line after the heading up to the next heading-like line; intro prose and table headers don't end it
    (defect 2)."""
    body = []
    for nxt in lines[start + 1:]:
        if _headingish(nxt):
            break
        body.append(nxt)
    return body


def _section(text: str, heading_regex: str, krx: str):
    """(heading tail, body lines) of the section headed by heading_regex, or None."""
    lines = text.split("\n")
    start = _section_start(lines, heading_regex, krx)
    if start is None:
        return None
    return lines[start][re.search(heading_regex, lines[start], re.I).end():], _section_body(lines, start, krx)


_KEY_SEP = r"(?:\s*(?:,|;|/|&|\+|·|\band\b|\bor\b)\s*)+"    # what may separate two keys of a bare list (R2-2)
_RX_TAIL = re.compile(r"[\s.,;:)\]}\*_`]*")            # what may follow the last key of a list (R2-2/R3-3)


def _list_shape(tail: str, krx: str) -> bool:
    """Whether `tail` is a bare key list: keys separated only by separators and closed by punctuation. The key regex
    is used once, through spans, so a named-group regex never collides (R3-3)."""
    ms = list(re.finditer(krx, tail))
    if not ms or tail[:ms[0].start()].strip(" \t*_`"):
        return False
    gap = re.compile(_KEY_SEP, re.I)
    pos = ms[0].end()
    for m in ms[1:]:
        if not gap.fullmatch(tail[pos:m.start()]):
            return False
        pos = m.end()
    return bool(_RX_TAIL.fullmatch(tail[pos:]))


def _md_clean(s: str) -> str:
    """Strip inline markdown emphasis/backticks per key, not only at the ends (R2-2)."""
    return re.sub(r"\*\*|__|`", " ", s)


def _bare_key_list(body: str, krx: str) -> bool:
    """Whether the line body is a grammatical key list: an optional label ending in ':', then keys joined only by
    separators or and/or (Oxford commas included), then nothing but closing punctuation (G1-5/R2-2). The old
    character-count allowance accepted short prose ("K-01 depends on K-02"); a list is a shape, not a length."""
    tail = re.sub(r"^[\s*_`]+", "", body)
    label = re.match(r"^[^:]{0,120}:\s*", tail)          # "Owner calls:" / "**Review not approved (2):**"
    if label:
        tail = tail[label.end():]
    tail = _md_clean(re.sub(r"^[\s*_`]+", "", tail)).strip()
    return _list_shape(tail, krx)


def _keys_in(text: str, krx: str) -> list:
    """Every key of the text: the whole regex match, never a capture group (R3-2: a partial or nested named capture
    would otherwise yield "K" or a tuple)."""
    return [m.group(0) for m in re.finditer(krx, text)]


def _row_keys(line: str, krx: str) -> list:
    """Keys a list line names: a table row's first cell; every key of a bare key list, bulleted or not (defect 5); a
    prose bullet's first key. Prose and header lines name none. G1-5/R2-2: a bare key list is recognised by its
    grammar (keys separated only by separators or and/or, Oxford commas and per-key markdown included)."""
    s = line.strip()
    keys = _keys_in(s, krx)
    if not keys:
        return []
    if s.startswith("|"):
        return _keys_in(s.strip("|").split("|")[0], krx)[:1]
    bullet = re.match(r"([-*•]|\d+[.)])\s+", s)
    body = s[bullet.end():] if bullet else s
    tail = re.sub(r"^[\s*_`]+", "", body)
    label = re.match(r"^[^:]{0,120}:\s*", tail)
    if label:
        if _keys_in(label.group(0), krx):
            return keys[:1] if bullet else []        # a key inside the label: prose, not a label
        tail = tail[label.end():]
    tail = _md_clean(re.sub(r"^[\s*_`]+", "", tail)).strip()
    if _list_shape(tail, krx):
        return _keys_in(tail, krx)
    return keys[:1] if bullet else []


def tracker_section(text: str, heading_regex: str, key_regex: str, count: bool = False):
    """Keys in the section headed by heading_regex, or None. Every key in the section counts as listed; an exact count
    uses the list-like lines when the section has any, so a prose aside doesn't inflate it."""
    sec = _section(text, heading_regex, key_regex)
    if sec is None:
        return None
    lines = [sec[0]] + sec[1]
    every = [k for line in lines for k in _keys_in(line, key_regex)]
    listed = [k for line in lines for k in _row_keys(line, key_regex)]
    return listed if count else every


def tracker_section_lines(text: str, heading_regex: str, key_regex: str):
    sec = _section(text, heading_regex, key_regex)
    if sec is None:
        return None
    return [line for line in [sec[0]] + sec[1] if re.search(key_regex, line)]


def _entry_match(line: str, pattern: str, known_hex: set) -> bool:
    """A tracker_entry value: a regex, or a SHA value (7-40 hex characters) that also matches an unambiguous prefix of
    7 or more characters (defect 8; 09_Rubric_Writing gate 5). Ambiguous: another known SHA shares the prefix.

    G1-6: an abbreviated expected value is resolved against the known hashes WITHOUT the pattern itself (the
    selector's own text is not evidence); two incomparable extensions are ambiguous, so False; the resolved target
    and the pattern are never rivals of a written token."""
    raw = str(pattern).strip()
    low = raw.lower()
    if not re.fullmatch(r"[0-9a-f]{7,40}", low):
        return bool(re.search(raw, line, re.I))       # a regex keeps its case (\D, \A, ...)
    pat = low
    known = {str(h).strip().lower() for h in known_hex
             if re.fullmatch(r"[0-9a-f]{7,40}", str(h).strip(), re.I)}
    known.discard(pat)
    ext = sorted({h for h in known if len(h) > len(pat) and h.startswith(pat)})
    # a chain H[:8] / H[:16] / H is one target (the longest); incomparable extensions are ambiguous
    targets = [h for h in ext if not any(h != o and o.startswith(h) for o in ext)]
    if len(targets) > 1:
        return False
    target = targets[0] if targets else pat
    for tok in RX_HEX.findall(line.lower()):
        if not target.startswith(tok):   # the written value must be the target or a prefix of it
            continue
        rivals = {h for h in known if not (target.startswith(h) or h.startswith(target))
                  and (h.startswith(tok) or tok.startswith(h))}
        if not rivals:                   # one known hash shares the written prefix: unambiguous
            return True
    return False


def _patch(q: dict):
    p = q.get("patch")
    if isinstance(p, str):
        try:
            p = json.loads(p)
        except ValueError:
            pass
    return p


def tracker_updates(w: dict, tool: str, issue: str | None) -> list:
    """Successful updates of the tracking issue in run order, matched exactly (whitespace only, G1-7); every update of
    the tool when the deliverable names no issue. An update of a sibling issue ("T-10" for "T-1", "ZOM-8010" for
    "ZOM-801") never supplies the tracker's state or content, and there is no fallback to unrelated updates."""
    ups = sorted(w.get(tool, []), key=lambda c: c["event"])
    if not issue:
        return ups
    want = str(issue).strip()
    return [c for c in ups if str(c["input"].get("id") or c["input"].get("issueId") or "").strip() == want]


def tracker_final_state(ups: list) -> str:
    """The tracking issue's state after every update in order: the last update that sets one (defect 4)."""
    for c in reversed(ups):
        state = c["input"].get("state") or c["input"].get("stateId")
        if state:
            return str(state)
    return ""


def _mutations(ups: list) -> list:
    """[(event, kind, text)] for every content mutation of the description, in order: kind is "replace", "append",
    "prepend", or "unknown" (a mutation this decoder cannot read; text is ""). G1-2: a full description and a
    `replace /description` string replace the content; append/prepend modify it; a patch op or path that is not a
    description mutation ("/labels") changes no content, so it adds no uncertainty."""
    out = []
    for c in ups:
        q, p = c["input"], _patch(c["input"])
        event = c["event"]
        if "description" in q:                         # an explicit empty full description clears the content
            v = q["description"]
            out.append((event, "replace", v) if isinstance(v, str) else (event, "unknown", ""))
        if p is None:
            continue
        if isinstance(p, str):
            out.append((event, "unknown", ""))
        elif isinstance(p, dict):
            kind0 = str(p.get("op") or "").lower()
            path0 = str(p.get("path") or "").lstrip("/")
            if kind0 == "test" or (kind0 == "move" and "from" in p
                                   and str(p.get("from") or "").lstrip("/") == path0):
                continue                               # a test op and a move to the same path are no-ops (R2-4)
            path = str(p.get("path") or "")
            if "description" in p and (not path or path.lstrip("/") == "description"):
                v = p["description"]
                out.append((event, "replace", v) if isinstance(v, str) else (event, "unknown", ""))
            elif p:
                out.append((event, "unknown", ""))
        elif isinstance(p, list):
            for op in p:
                if not isinstance(op, dict):
                    out.append((event, "unknown", ""))
                    continue
                kind = str(op.get("op") or "").lower()
                text = op.get("text")
                value = op.get("value")
                path_given = "path" in op
                path = str(op.get("path") or "")
                sub = path.lstrip("/")
                if kind == "test":
                    continue                           # JSON Patch test changes no content (R2-4)
                if kind == "move" and "from" in op:
                    src = str(op.get("from") or "").lstrip("/")
                    if src == sub:
                        continue                       # a move to its own path is a no-op (R2-4)
                    if src == "description":
                        out.append((event, "replace", ""))
                    elif src.startswith("description/"):
                        out.append((event, "unknown", ""))
                if not path_given:                      # the documented pathless append/prepend form
                    if kind in ("append", "prepend") and isinstance(text, str):
                        out.append((event, kind, text))
                    elif kind in ("replace", "add") and isinstance(value, str):
                        out.append((event, "replace", value))
                    else:
                        out.append((event, "unknown", ""))
                    continue
                if path == "":                          # JSON Pointer root, not the pathless form
                    if kind in ("replace", "add") and isinstance(value, dict) and "description" in value:
                        v = value["description"]
                        out.append((event, "replace", v) if isinstance(v, str) else (event, "unknown", ""))
                    elif kind in ("replace", "add", "remove", "move", "copy"):
                        out.append((event, "unknown", ""))
                    continue
                if sub == "description":
                    if kind in ("append", "prepend") and isinstance(text, str):
                        out.append((event, kind, text))
                    elif kind in ("replace", "add") and isinstance(value, str):
                        out.append((event, "replace", value))
                    elif kind == "remove":
                        out.append((event, "replace", ""))     # R7-4: a deletion is a known empty replacement
                    elif kind in ("replace", "add"):
                        out.append((event, "unknown", ""))
                    else:
                        out.append((event, "unknown", ""))
                elif sub.startswith("description/"):
                    out.append((event, "unknown", ""))
                else:
                    continue                       # another field (e.g. /labels): no content, no uncertainty
        else:
            out.append((event, "unknown", ""))
    return out


def tracker_text(ups: list) -> tuple:
    """(effective description, unreadable events): the content replayed in order (G1-2/G1-4). A full description or
    a `replace /description` string replaces the text, append/prepend modify it, and an unreadable mutation is
    recorded so its slots become UNGRADED, never false; a later full replacement clears it because it re-establishes
    the content."""
    text, unreadable = "", []
    for event, kind, value in _mutations(ups):
        if kind == "replace":
            text, unreadable = value, []
        elif kind == "append":
            text = f"{text}\n{value}" if text else value
        elif kind == "prepend":
            text = f"{value}\n{text}" if text else value
        else:
            unreadable.append(event)
    return text, unreadable


def tracker_preserved(ups: list, original: str):
    """True | False | None: whether the original text survives every update in order (defect 4). A replacement that
    drops it is a known violation and stays False even if a later write restores it; append/prepend keep it; an
    unreadable mutation makes the history unknown (None), never false, and a later replacement cannot prove what
    happened in between."""
    state = True
    for _, kind, value in _mutations(ups):
        if kind == "replace":
            if original not in value:
                state = False                 # a known violation is absorbing
            elif state is True:
                state = True
        elif kind == "unknown":
            if state is not False:
                state = None
    return state


# ------------------------------------------------------------------ grading

def truth_counts(truth: dict, surface: dict) -> dict:
    tf = surface.get("truth_fields") or {}
    cf = tf.get("class", "handoff class")
    gf = tf.get("groups") or "groups"
    _, xspec = gs.text_deliverable(surface)
    names = [g for g, _ in (xspec or {}).get("groups") or []]
    for s in surface.get("slots") or []:
        sel = s.get("selector") or []
        if sel and sel[0] in ("group_count", "group_size") and len(sel) > 1:
            names.append(sel[1])
        elif sel and sel[0] in ("group_key", "groups_of") and len(sel) > 2:
            names.append(sel[2] if sel[0] == "group_key" else sel[1])
    names = list(dict.fromkeys(names))
    # groups come from each truth row's field named by truth_fields.groups (default "groups"): the field name is
    # never itself a value, and a scalar where a list is required is invalid, so group slots fail (R2-11)
    def members(v) -> list:
        x = (v or {}).get(gf)
        return x if isinstance(x, list) else []
    invalid = {k: True for k, v in truth.items() if isinstance(v, dict) and gf in v
               and not isinstance(v[gf], list)}
    # R7-1: the written side of total/printed_total counts the first table only, so the truth side is restricted to
    # the keys that table owns; counting every truth row would compare different cohorts.
    t0 = gs.table_deliverables(surface)
    krx0 = (t0[0][1].get("key_regex") if t0 else None)
    try:
        scope = {k: v for k, v in truth.items() if not krx0 or re.fullmatch(krx0, str(k))}
    except re.error:
        scope = dict(truth)
    return {"classes": dict(collections.Counter(v.get(cf) for v in scope.values())),
            "groups": {g: [k for k, v in truth.items() if g in members(v)] for g in names},
            "groups_invalid": invalid, "groups_field": gf}


def _strings(v, out: list) -> list:
    if isinstance(v, str):
        out.append(v)
    elif isinstance(v, dict):
        for x in v.values():
            _strings(x, out)
    elif isinstance(v, list):
        for x in v:
            _strings(x, out)
    return out


def _register_parent(calls: list, results: dict, file_id: str):
    """The final folder of the shared register: the creation parentId, then any later successful move."""
    parent = None
    for c in calls:
        n, q, r = tl.short(c["name"]), c["input"] or {}, results.get(c["id"])
        if tl.failed(r):
            continue
        data = r.get("data") if isinstance(r, dict) else None
        made = (data.get("id") or data.get("spreadsheetId")) if isinstance(data, dict) else None
        if n in ("gdrive_create_file", "gsheets_create_spreadsheet") and made == file_id:
            parent = q.get("parentId") or q.get("folderId") or parent
        elif n == "gdrive_move_file" and q.get("fileId") == file_id:
            parent = q.get("newParentId") or parent
    return parent


def _content_strings(calls: list) -> str:
    """The readable content of json_text deliverable calls: every content string at every nesting level, never an
    identifier parameter (R2-6: a text slot must not match an objectId/presentationId)."""
    vals = []

    def content(v):
        if isinstance(v, dict):
            for k, x in v.items():
                kl = str(k).lower()
                # R3-2: identifier parameters at any nesting level are never readable content: every *id/*ids key
                # (channel_id, cardId, issueId, fileId, objectId, presentationId, ...) and the raw locator params.
                if not (kl.endswith(("id", "ids")) or kl in ("channel", "ts", "thread_ts", "threadts")):
                    content(x)
        elif isinstance(v, list):
            for x in v:
                content(x)
        elif isinstance(v, str):
            vals.append(v)
    for c in calls:
        content(c["input"])
    return "\n".join(vals)


def decode(run: tl.Run, surface: dict) -> dict:
    """Everything the slots read from one run.

    Round 2 (G1-3/4/11): `table_identity` is the decoded table's own file id / spreadsheet id (never the last share);
    `tracker_state` is "known" or "unknown" for the effective tracker content (G1-2); the register is unreadable only
    when the selected (delivered) register write could not be read, never because some other candidate was."""
    table_specs = gs.table_deliverables(surface)
    tname, tspec = table_specs[0] if table_specs else (None, None)
    xname, xspec = gs.text_deliverable(surface)
    classes = surface.get("classes") or []
    tables = {name: tl.table(run, dict(spec, classes=classes)) for name, spec in table_specs}
    all_rows = {}
    for tb in tables.values():
        all_rows.update(tb.get("rows") or {})
    spec = dict(tspec or {}, classes=classes)
    t = tables.get(tname) if tname else {"rows": {}, "kind": None, "raw": [], "meta": {}, "candidates": []}
    deliverables = surface.get("deliverables") or {}
    base = {d.get("tool") for d in deliverables.values() if isinstance(d, dict) and d.get("tool")}
    base |= {"linear_update_issue", "gdrive_share_file", "gslides_batch_update", "gmail_reply_to_message",
             "slack_send_message"}
    tools = set().union(*(aliases(x) for x in base)) | {"gdrive_move_file", "gdrive_create_file"}
    w = tl.write_calls(run, tools)
    xtool = (xspec or {}).get("tool", "linear_update_issue")
    ups = tracker_updates(w, xtool, (xspec or {}).get("issue")) if xspec else []
    ztext, unreadable_updates = tracker_text(ups)           # the effective description, replayed in order (G1-2/4)
    texts, plain, link_text = {}, {}, {}
    targets = {name: d["tool"] for name, d in deliverables.items() if isinstance(d, dict) and d.get("kind") == "json_text"}
    for name, tool in (("slide", "gslides_batch_update"), ("email", "gmail_reply_to_message"), ("slack", "slack_send_message")):
        targets.setdefault(name, tool)
    for name, tool in targets.items():
        calls = sorted((c for a in aliases(tool) for c in w.get(a, [])), key=lambda c: c["event"])
        texts[name] = json.dumps([c["input"] for c in calls], ensure_ascii=False)
        plain[name] = link_text[name] = _content_strings(calls)   # R2-6: never identifier metadata
    for name, tb in tables.items():
        texts[name] = plain[name] = link_text[name] = "\n".join(",".join(str(x) for x in row) for row in tb.get("raw") or [])
    for name in [n for n in (xname, "tracker") if n]:
        texts[name] = plain[name] = link_text[name] = ztext
    # G1-11: the register's own identity, from the decoded table; never the last file the run happened to share
    ident = t["meta"].get("identity")
    cf = (tspec or {}).get("class_column", "handoff class")
    written_classes = {c: sum(1 for k in t["rows"] if tl.norm(t["rows"][k].get(cf, "")) == c.lower()) for c in classes}
    hexes = set()
    for s in surface.get("slots") or []:
        sel = s.get("selector") or []
        if sel and sel[0] == "tracker_entry" and isinstance(sel[3], list):
            hexes |= {str(x).strip().lower() for x in sel[3]
                      if re.fullmatch(r"[0-9a-f]{7,40}", str(x).strip(), re.I)}
    table_unknown = bool(tspec) and bool(t["meta"].get("unreadable"))
    tracker_unknown = bool(unreadable_updates)          # an unread mutation whose content a later full text didn't reset
    return {"table": t, "tables": tables, "rows": all_rows, "tspec": tspec or {}, "xspec": xspec or {},
            "writes": w, "tracker": ztext,
            "tracker_updates": ups, "groups": tracker_groups(ztext, xspec or {}), "texts": texts, "plain": plain,
            "link": ident or "", "table_identity": ident, "link_text": link_text,
            "tracker_state": "unknown" if tracker_unknown else "known",
            "printed": tl.printed_totals(t["raw"], (tspec or {}).get("key_regex", r"\w+"), classes),
            "classes": written_classes, "selector_hex": hexes, "calls": run.calls, "results": run.results,
            "unreadable": {"table": table_unknown,
                           "tables": {name: bool(tb.get("meta", {}).get("unreadable")) for name, tb in tables.items()},
                           "table_events": [c["event"] for c in t["candidates"] if c.get("rows") is None],
                           "tracker": tracker_unknown, "tracker_events": unreadable_updates},
            "tracker_name": xname or "tracker"}


TABLE_SELECTORS = ("field", "total", "printed_total", "reason_matches")
TABLE_DELIVERIES = ("register_is_csv", "register_keys_exact")
TRACKER_SELECTORS = ("group_count", "group_size", "group_key", "groups_of", "sole_reason", "tracker_lists",
                     "tracker_count", "tracker_entry")


def _id_candidates(value) -> set:
    """The identifiers a value names: the value itself, the address inside angle brackets and its local part, and
    the last path component (Gmail ids arrive as `name/<CA...@mail>`)."""
    s = str(value or "").strip()
    if not s:
        return set()
    out = {s}
    for m in re.finditer(r"<([^<>]+)>", s):
        inner = m.group(1).strip()
        if inner:
            out.add(inner)
            if "@" in inner:
                out.add(inner.split("@", 1)[0].strip())
    tail = s.rsplit("/", 1)[-1].strip().strip("<>").strip()
    if tail:
        out.add(tail)
        if "@" in tail:
            out.add(tail.split("@", 1)[0].strip())
    return {x for x in out if x}


def _id_token_match(expected, actual) -> bool:
    """An expected identifier matches a whole delimiter-separated token of the parameter, never a substring:
    `m1` does not match `m10`, but the Gmail id inside `name/<CA...@mail>` and a wrapped `<m1@mail>` match their bare
    id (R2-7)."""
    e, a = str(expected or "").strip(), str(actual or "").strip()
    if not e or not a:
        return False
    tokens = [x for x in re.split(r"[^A-Za-z0-9._-]+", a) if x]
    if e == a or e in tokens:
        return True
    ids = _id_candidates(e)
    return bool(ids & _id_candidates(a)) or any(x in tokens for x in ids)


def _message_id(actual: str) -> str:
    """The message identifier inside a wrapped value: the last `/` segment, without angle brackets (R8-1). A mailbox
    prefix (`m1@harmonygames.co/<m10@mail>`) must never supply the id."""
    a = str(actual or "").strip()
    if "/" in a:
        a = a.rsplit("/", 1)[1]
    return a.strip().strip("<>").strip()


def reply_match(args: list, sent) -> bool:
    """G1-10: the reply target and reply_all are bound to the call's own parameters, never to text anywhere in the
    serialized inputs (the body could mention the id, and "false" could come from any field)."""
    def replies(c):
        q = c["input"]
        return isinstance(q.get("message_id"), str) and _id_token_match(args[0], _message_id(q["message_id"])) \
            and q.get("reply_all") is False
    return any(replies(c) for c in sent("gmail_reply_to_message"))


def thread_match(args: list, sent) -> bool:
    """G1-10: a Slack thread is the call's own thread_ts, not any occurrence of the id in the payload."""
    return any(isinstance(c["input"].get("thread_ts"), str) and _id_token_match(args[0], c["input"]["thread_ts"])
               for c in sent("slack_send_message"))


def tracker_entry_match(sel: list, line: str, known_hex: set, kreg: str = r"\w+-\d+") -> bool:
    """G1-8: the value patterns bind to the entry's own row. The owning key is the first key on a prose line (or the
    first cell of a table row); a cross-reference to another key does not make that key the entry, and its value does
    not satisfy the other entry."""
    s = line.strip()
    if s.startswith("|"):
        cells = [x.strip() for x in s.strip("|").split("|")]
        if not cells or not re.fullmatch(r"\b" + re.escape(sel[2]) + r"\b", cells[0], re.I):
            return False
        # R8-2: a value cell that mentions another key keeps the text *before* the reference (the owning entry's
        # value), instead of being dropped wholesale; the foreign key's own row is matched by its first cell only.
        parts = []
        for x in cells[1:]:
            m = re.search(r"\b(?:" + kreg + r")", x)
            parts.append(x[:m.start()] if m else x)
        tail = "|".join(parts)
    else:
        body = re.sub(r"^\s*(?:[-*•]|\d+[.)])\s+", "", line)
        lab = re.match(r"^[^:]{0,80}:\s*", body)
        if lab and not re.search(r"\b(?:" + kreg + r")", lab.group(0)):
            body = body[lab.end():]
        body = re.sub(r"^[\s*_`]+", "", body)
        if not re.match(r"\b" + re.escape(sel[2]) + r"\b", body):
            return False
        m = re.search(r"\b" + re.escape(sel[2]) + r"\b", body)
        tail = body[m.end():]
        nxt = re.search(r"\b(?:" + kreg + r")", tail)
        if nxt:
            tail = tail[:nxt.start()]
    return all(_entry_match(tail, rx, known_hex) for rx in sel[3])


def grade(surface: dict, truth: dict, d: dict) -> dict:
    """{slot id: True | False | None (UNGRADED)} for one decoded run."""
    tc = truth_counts(truth, surface)
    rows, t, tspec, groups = d.get("rows") or d["table"]["rows"], d["table"], d["tspec"], d["groups"]
    tables = d.get("tables") or {t.get("meta", {}).get("identity") or "register": t}
    table_specs_n = gs.table_deliverables(surface)
    first_table = table_specs_n[0][0] if table_specs_n else next(iter(tables), None)
    unread_tables = (d.get("unreadable") or {}).get("tables") or {}
    tracker_unread = bool((d.get("unreadable") or {}).get("tracker"))
    texts, plain, w, ups = d["texts"], d["plain"], d["writes"], d["tracker_updates"]
    # R11-1: a tracker spec without its own key_regex inherits the table's, never the SP-\d{3} default
    kreg = ((d.get("xspec") or {}).get("key_regex") or (tspec or {}).get("key_regex") or _krx(None))
    reason_col = tspec.get("reason_column", "reason")
    gf = (surface.get("truth_fields") or {}).get("groups") or "groups"
    known_hex = set(d["selector_hex"])
    # R3-3: a SHA prefix is ambiguous if any declared table's truth carries another hash with that prefix, so the
    # comparators of every table contribute, not only the register's.
    for _, spec_n in table_specs_n:
        for col, comp in (spec_n.get("comparators") or {}).items():
            if comp == "sha_prefix":
                known_hex |= {str(v.get(col)).strip().lower() for v in truth.values()
                              if re.fullmatch(r"[0-9a-f]{7,40}", str(v.get(col)).strip(), re.I)}

    def table_unreadable(name) -> bool:
        """Readability of the named table deliverable (R2-9: each table carries its own flag)."""
        if name is None:
            return False
        if name in unread_tables:
            return bool(unread_tables[name])
        return bool(((tables.get(name) or {}).get("meta") or {}).get("unreadable"))

    def table_for_key(key) -> str | None:
        """The table a per-key selector reads: the first declared table whose key_regex names the key. Resolved from
        the schema only (R6-1): observed content must never move ownership, or a secondary table could supply a
        missing register row (and its readability) for an overlapping key."""
        matches = [name for name, spec in table_specs_n if re.fullmatch(spec.get("key_regex") or r".+", str(key))]
        return matches[0] if matches else first_table

    def unreadable_slot(sl: dict) -> bool:
        sel2 = sl.get("selector") or []
        k = sel2[0] if sel2 else ""
        target = sel2[1] if len(sel2) > 1 else None
        if k == "field":
            return table_unreadable(table_for_key(sel2[1]))
        if k in ("total", "printed_total"):
            return table_unreadable(first_table)
        if k == "reason_matches":
            return table_unreadable(table_for_key(sel2[1]))
        if k == "delivery" and target == "register_is_csv":
            return table_unreadable(first_table)
        if k == "delivery" and target == "register_keys_exact":
            return table_unreadable(sel2[2] if len(sel2) > 2 else first_table)
        if k in ("text", "link"):
            tspec_d = (surface.get("deliverables") or {}).get(target) or {}
            shares_tracker = bool(d.get("xspec")) and tspec_d.get("tool") == (d.get("xspec") or {}).get("tool")
            return (target in tables and table_unreadable(target)) \
                or (k == "link" and table_unreadable(first_table)) \
                or ((target in (d.get("tracker_name"), "tracker") or shares_tracker) and tracker_unread)
        if k in TRACKER_SELECTORS or (k == "delivery" and target in ("tracker_state", "tracker_preserves")):
            return tracker_unread
        return False

    def sent(tool):
        return [c for a in aliases(tool) for c in w.get(a, [])]

    def delivery(name, *args, slot=None):
        if name == "register_is_csv":
            return t["kind"] == "CSV"
        if name == "register_keys_exact":
            tname = str(args[0]) if args else first_table
            if ((tables.get(tname) or {}).get("meta") or {}).get("identity") is None \
                    and not (tables.get(tname) or {}).get("rows"):
                return False             # R10-3: no register was delivered: an empty key set is not a match
            rows_n = (tables.get(tname) or {}).get("rows") or {}
            spec_n = dict(table_specs_n).get(tname) or {}
            raw = (slot or {}).get("expected_keys")
            if isinstance(raw, (list, tuple, set)):
                expected = {str(k) for k in raw}                 # the slot's explicit key set (R2-10)
            elif raw is not None:
                expected = {str(raw)}
            elif surface.get("truth_keys") is not None:
                expected = {str(k) for k in surface.get("truth_keys") or []}
            else:
                krx = spec_n.get("key_regex") or r".+"
                expected = {str(k) for k in truth if re.fullmatch(krx, str(k))}
            return set(rows_n) == expected
        if name == "share_reader":
            ident = d.get("table_identity")
            return bool(ident) and any(str(c["input"].get("fileId")) == str(ident)
                                       and c["input"].get("role") == "reader"
                                       for c in w.get("gdrive_share_file", []))   # R2-12: the register's own id
        if name == "slide_updated":
            return bool(w.get("gslides_batch_update"))
        if name == "tracker_state" and str(args[0]) in ("comment", "description", "state"):
            def trello_field(c):
                q = c["input"]
                return bool(str(q.get(args[0]) or q.get("text") or q.get("comment") or "").strip())
            return any(trello_field(c) for a in ("trello_add_comment_to_card", "trello_update_card", "trello_add_card")
                       for c in w.get(a, []))
        if name == "tracker_state" and re.fullmatch(r"[0-9a-f]{24}", str(args[0])):
            def trello(c):
                q = c["input"]
                cid = str(q.get("cardId") or q.get("card_id") or q.get("id") or "")
                body = q.get("text") or q.get("comment") or q.get("description") or q.get("state") or q.get("name")
                return cid == str(args[0]) and isinstance(body, str) and bool(body.strip())
            return any(trello(c) for a in ("trello_add_comment_to_card", "trello_update_card", "trello_add_card")
                       for c in w.get(a, []))
        if name == "tracker_state":
            return bool(re.match(args[0], tracker_final_state(ups), re.I))
        if name == "tracker_preserves":
            return tracker_preserved(ups, args[0]) if ups else False
        if name == "email_reply":
            return reply_match(args, sent)
        if name == "slack_thread":
            return thread_match(args, sent)
        if name == "slack_channel_post":
            channel, text = str(args[0]), str(args[1])
            def post(c):
                q = c["input"]
                # R6-3: the required text must be message *content*, never a routing parameter (a thread ts or a
                # channel id in the payload must not satisfy a text requirement)
                return str(q.get("channel_id") or q.get("channel") or "") == channel \
                    and text.lower() in _content_strings([c]).lower()
            return any(post(c) for c in sent("slack_send_message"))
        if name == "trello_card":
            card, value = str(args[0]), str(args[1])
            def card_call(c):
                q = c["input"]
                cid = str(q.get("cardId") or q.get("card_id") or q.get("id") or "")
                body = q.get("text") or q.get("comment") or q.get("description") or q.get("state") or q.get("name") or ""
                return cid == card and value.lower() in str(body).lower()
            return any(card_call(c) for a in ("trello_add_comment_to_card", "trello_update_card", "trello_add_card")
                       for c in w.get(a, []))
        if name == "slack_after_email":
            mail = [c["event"] for c in sent("gmail_reply_to_message")]
            sl = [c["event"] for c in sent("slack_send_message")]
            return bool(mail and sl) and max(sl) > min(mail)
        if name == "register_parent":
            ident = d.get("table_identity")
            return bool(ident) and any(c["input"].get("fileId") == ident for c in w.get("gdrive_share_file", [])) \
                and _register_parent(d["calls"], d["results"], ident) == args[0]
        raise ValueError(f"unknown delivery check {name}")

    out = {}
    for s in surface["slots"]:
        sel, sid = s["selector"], s["id"]
        if s.get("gradable") is False:
            out[sid] = None
            continue
        kind = sel[0]
        if kind == "delivery" and sel[1] == "tracker_preserves":
            out[sid] = tracker_preserved(ups, sel[2]) if ups else False    # False is absorbing; unknown stays None
            continue
        if unreadable_slot(s):
            out[sid] = None                     # the deliverable was written but can't be read: UNGRADED, never false
            continue
        if kind == "field":
            k, f = sel[1], sel[2]
            # R4-2: the field reads the table that owns the key, with that table's row, comparators and missing
            # values together; a merged row map could carry another table's value for an overlapping key.
            src = table_for_key(k)
            rspec = dict(table_specs_n).get(src) or tspec
            srows = (tables.get(src) or {}).get("rows") or {}
            exp = (truth.get(k) or {}).get(f)
            accepted = s.get("accepted_outcomes")
            ok = k in srows and f in srows[k] and compare(srows[k][f], exp, f, rspec) == "MATCH"
            if not ok and accepted and k in srows and f in srows[k]:
                ok = any(compare(srows[k][f], a, f, rspec) == "MATCH" for a in accepted)
            out[sid] = ok
        elif kind == "total":
            # R8-4: a class total of zero with no table delivered is not a pass; the register must exist (a
            # delivered header-only table legitimately has zero rows)
            out[sid] = t.get("kind") is not None and d["classes"].get(sel[1]) == tc["classes"].get(sel[1], 0)
        elif kind == "printed_total":
            out[sid] = t.get("kind") is not None and d["printed"].get(sel[1]) == tc["classes"].get(sel[1], 0)
        elif kind in ("group_count", "group_size", "group_key"):
            # R2-8/R5-1: never substitute the truth side for observed content, and a malformed truth group field
            # invalidates the whole group aggregate (silently dropping that row would award credit for a bad truth).
            bad_truth = bool(tc.get("groups_invalid"))
            gname = sel[1] if kind != "group_key" else sel[2]
            if kind == "group_count":
                out[sid] = (not bad_truth) and gname in groups \
                    and groups[gname][0] == len(tc["groups"].get(gname, []))
            elif kind == "group_size":
                out[sid] = (not bad_truth) and gname in groups \
                    and len(set(groups[gname][1])) == len(tc["groups"].get(gname, []))
            else:
                out[sid] = (not bad_truth) and gname in groups \
                    and ((sel[1] in groups[gname][1]) == (sel[1] in tc["groups"].get(gname, [])))
        elif kind == "groups_of":
            want = (truth.get(sel[1]) or {}).get(gf)
            # R9-1: an empty membership list is only provable when the tracker was actually delivered; otherwise an
            # empty decode would equal an empty truth and award credit for nothing.
            out[sid] = (not tc["groups_invalid"].get(sel[1])) and isinstance(want, list) \
                and bool(str(d.get("tracker") or "").strip() or want) \
                and sorted(g for g, (_, ks) in groups.items() if sel[1] in ks) == sorted(want)
        elif kind == "sole_reason":
            out[sid] = sorted(g for g, (_, ks) in groups.items() if sel[1] in ks) == [sel[2]]
        elif kind == "reason_matches":
            src = table_for_key(sel[1])
            rspec = dict(table_specs_n).get(src) or tspec
            srows = (tables.get(src) or {}).get("rows") or {}
            out[sid] = sel[1] in srows and bool(re.search(
                sel[2], srows[sel[1]].get(rspec.get("reason_column", reason_col), ""), re.I))
        elif kind == "tracker_lists":
            keys = tracker_section(d["tracker"], sel[1], kreg)
            out[sid] = bool(keys) and sel[2] in keys
        elif kind == "tracker_count":
            keys = tracker_section(d["tracker"], sel[1], kreg, count=True)
            out[sid] = keys is not None and len(set(keys)) == int(sel[2])
        elif kind == "tracker_entry":
            lines = tracker_section_lines(d["tracker"], sel[1], kreg) or []
            out[sid] = any(tracker_entry_match(sel, ln, known_hex, kreg) for ln in lines)
        elif kind == "text":
            out[sid] = bool(re.search(sel[2], plain.get(sel[1], ""), re.I | re.S))
        elif kind == "link":
            ident = d["table_identity"]
            shared = any(c["input"].get("fileId") == ident for c in w.get("gdrive_share_file", []))
            out[sid] = bool(ident) and shared and _id_token_match(ident, d.get("link_text", {}).get(sel[1], ""))
        elif kind == "delivery":
            out[sid] = delivery(*sel[1:], slot=s)
        else:
            raise ValueError(f"unknown selector {sel}")
    return out


# ------------------------------------------------------------------ truth sources

def load_truth(truth_path=None, solver=None, oracle_dir=None, sql_path=None) -> tuple:
    """(truth rows, provenance) from a truth.json, an oracle_kit solver, or a legacy oracle directory."""
    if truth_path:
        p = Path(truth_path)
        return json.loads(p.read_text()), {"kind": "truth.json", "path": tl._rel(p), "sha256": tl.sha256_file(p)}
    if sql_path is None:
        raise ValueError("--solver / --oracle-dir need --sql")
    sql = Path(sql_path).read_text()
    prov = {"sql": tl._rel(Path(sql_path)), "sql_sha256": hashlib.sha256(sql.encode()).hexdigest()}
    if solver:
        import oracle_kit
        mod = oracle_kit.load_solver(solver)
        rows = oracle_kit.truth(mod, sql)
        return rows, {"kind": "oracle_kit solver", "solver": tl._rel(Path(solver)), **prov}
    if oracle_dir:
        d = Path(oracle_dir)
        for p in (str(d), str(d.parent)):
            if p not in sys.path:
                sys.path.insert(0, p)
        spec = importlib.util.spec_from_file_location("legacy_oracle", d / "oracle.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.solve(sql, new=True), {"kind": "legacy oracle.py (imported as a library)", "oracle": tl._rel(d / "oracle.py"), **prov}
    raise ValueError("no truth source: give --truth, --solver or --oracle-dir")


# ------------------------------------------------------------------ gates

def task_context(task_dir):
    if not task_dir:
        return None
    try:
        from task_context import load_context
        return load_context(Path(task_dir))
    except Exception:  # noqa: BLE001 - a legacy (V2) task folder has no V3 context
        return None


def choose_views(context, runs: dict, views: str) -> list:
    if views in ("v2", "v3"):
        return [views.upper()]
    if views == "both":
        return ["V2", "V3"]
    if not context:
        return ["V2"]
    base = ["V3"] if context.get("spec_version") == "V3" else ["V2"]
    off_model = any(ds.check_models(r["models"], context.get("baseline_model"))["verdict"] != "VALID"
                    for r in runs.values())                       # one owner of model labels (difficulty_stats)
    if base == ["V3"] and off_model:
        return ["V3", "V2"]
    return base


MONOTONE_GATES = ("pass_at_1", "avg_weighted_pass_rate")   # more passing cells never worsen these: bounds decide them
ENUMERATE_LIMIT = 12                                         # UNGRADED cells whose 2^n completions SD and patterns try


def _word(verdict) -> str:
    return str(verdict).split(" ")[0]


def gates(surface: dict, runs: dict, context, views: list) -> dict:
    """The difficulty gates through difficulty_stats.compute(). UNGRADED cells are never counted silently either way:
    the average and full-pass verdicts come from the two bounds (every UNGRADED cell failed, every one passed) and stand
    only when both agree; the SD band and the failure patterns are not monotone, so every completion of the UNGRADED
    cells is enumerated (up to 2^ENUMERATE_LIMIT) and a verdict stands only when all agree. Otherwise INCOMPLETE."""
    # G1-1: every slot is a cell of the gate matrix; a `gradable:false` slot and an unreadable one are both unknown
    # (bounded, enumerated, listed), never silently dropped from the denominator
    slots_all = [s for s in surface["slots"]]
    rubrics = [{"id": s["id"], "weight": s["weight"]} for s in slots_all]
    base = [lab for lab in runs if lab not in PRE_LABELS]
    cells = [(lab, s["id"]) for lab in base if runs[lab]["status"] == "completed" for s in slots_all
             if runs[lab]["results"][s["id"]] is None]
    out = {}
    for spec in views:
        def compute(fill):
            rollouts = []
            for lab in base:
                r = runs[lab]
                if r["status"] != "completed":
                    rollouts.append({"id": lab, "status": "errored", "models": r["models"], "model_source": r["model_source"],
                                     "model_check": r.get("model_check")})
                    continue
                res = {s["id"]: (fill[(lab, s["id"])] if r["results"][s["id"]] is None else bool(r["results"][s["id"]]))
                       for s in slots_all}
                # R5-4: forward the run's own model provenance, which difficulty_stats.model_gate requires; without
                # it even six clean Opus 5.5 runs fail the baseline-model gate
                rollouts.append({"id": lab, "status": "completed", "tool_calls": r["counted_calls"], "models": r["models"],
                                 "model_source": r["model_source"], "model_check": r.get("model_check"), "results": res})
            data = {"spec_version": spec, "task_type": (context or {}).get("task_type", "long-horizon"),
                    "rubrics": rubrics, "rollouts": rollouts}
            if spec == "V3":
                data["difficulty_mode"] = (context or {}).get("difficulty_mode", "hard")
            return ds.compute(data)
        try:
            lo, hi = compute({c: False for c in cells}), compute({c: True for c in cells})
        except ValueError as error:
            out[spec] = {"error": str(error)}
            continue
        dg = {}
        for k in DIFFICULTY_GATES:
            if not cells:
                dg[k] = {"verdict": lo["gates"][k]["verdict"], "value": lo["gates"][k]["value"]}
            elif k in MONOTONE_GATES:
                words = {_word(lo["gates"][k]["verdict"]), _word(hi["gates"][k]["verdict"])}
                dg[k] = {"verdict": words.pop() if len(words) == 1 else "INCOMPLETE",
                         "value": {"ungraded_failed": lo["gates"][k]["value"], "ungraded_passed": hi["gates"][k]["value"]},
                         "basis": f"bounds over {len(cells)} UNGRADED cell(s)"}
            elif len(cells) <= ENUMERATE_LIMIT:
                words, values = set(), []
                for bits in itertools.product((False, True), repeat=len(cells)):
                    g = compute(dict(zip(cells, bits)))["gates"][k]
                    words.add(_word(g["verdict"]))
                    values.append(g["value"])
                dg[k] = {"verdict": words.pop() if len(words) == 1 else "INCOMPLETE",
                         "value": {"completions": len(values), "distinct_values": sorted({str(v) for v in values})[:6]},
                         "basis": f"every completion of {len(cells)} UNGRADED cell(s)"}
            else:
                dg[k] = {"verdict": "INCOMPLETE", "value": None,
                         "basis": f"{len(cells)} UNGRADED cells: more than {ENUMERATE_LIMIT} to enumerate"}
        g = hi["gates"]
        out[spec] = {"difficulty_mode": hi.get("difficulty_mode"), "difficulty_gates": dg,
                     "provenance_gates": {k: {"verdict": g[k]["verdict"], "value": g[k]["value"]}
                                          for k in PROVENANCE_GATES if k in g},
                     "difficulty_blocking": [k for k in DIFFICULTY_GATES if _word(dg[k]["verdict"]) == "FAIL"],
                     "incomplete": [k for k in DIFFICULTY_GATES if dg[k]["verdict"] == "INCOMPLETE"],
                     "ungraded_cells": [f"{lab}:{sid}" for lab, sid in cells],
                     "per_rollout": [{"id": x["id"], "weighted_pass_rate": round(x["weighted_pass_rate"], 6),
                                      "failed": x["failed_rubrics"]} for x in lo["per_rollout"]] if not cells else
                     {"ungraded_failed": [round(x["weighted_pass_rate"], 6) for x in lo["per_rollout"]],
                      "ungraded_passed": [round(x["weighted_pass_rate"], 6) for x in hi["per_rollout"]]},
                     "patterns": lo["patterns"] if not cells else {"ungraded_failed": lo["patterns"],
                                                                   "ungraded_passed": hi["patterns"]}}
    return out


# ------------------------------------------------------------------ who decided a failed slot (V1)

TABLE_TOOLS = ("gdrive_create_file", "gdrive_update_file", "gsheets_values_update", "gsheets_values_append",
               "gsheets_values_batch_update")
DELIVERY_TOOLS = {"share_reader": ("gdrive_share_file",), "slide_updated": ("gslides_batch_update",),
                  "email_reply": ("gmail_reply_to_message",), "slack_thread": aliases("slack_send_message"),
                  "slack_after_email": aliases("slack_send_message") + ("gmail_reply_to_message",),
                  "slack_channel_post": aliases("slack_send_message"),
                  "trello_card": ("trello_add_comment_to_card", "trello_update_card", "trello_add_card"),
                  "register_parent": ("gdrive_create_file", "gdrive_move_file", "gsheets_create_spreadsheet")}


def _failing_keys(slot: dict, d: dict, truth: dict, surface: dict) -> list:
    """The keys behind a failed slot: its own key, or for an aggregate the keys whose written value differs."""
    sel = slot["selector"]
    keys = gs.slot_keys(slot)
    if keys:
        return keys
    tf = surface.get("truth_fields") or {}
    cf_t, gf = tf.get("class", "handoff class"), tf.get("groups", "groups")
    cf_w = d["tspec"].get("class_column", "handoff class")
    rows = d["table"]["rows"]
    if sel[0] in ("total", "printed_total"):
        return sorted(k for k, v in truth.items() if (v.get(cf_t) == sel[1]) != (tl.norm((rows.get(k) or {}).get(cf_w, ""))
                                                                              == sel[1].lower()))
    if sel[0] in ("group_count", "group_size"):
        want = {k for k, v in truth.items() if isinstance(v.get(gf), list) and sel[1] in v[gf]}
        got = set((d["groups"].get(sel[1]) or (0, []))[1])
        return sorted(want ^ got)
    return []


def decided_by(run: tl.Run, briefs_: list, slot: dict, d: dict, truth: dict, surface: dict) -> dict:
    sel = slot["selector"]
    xtool = (d["xspec"] or {}).get("tool", "linear_update_issue")
    if sel[0] in TABLE_SELECTORS or (sel[0] == "delivery" and sel[1] in TABLE_DELIVERIES):
        tools = TABLE_TOOLS
    elif sel[0] in TRACKER_SELECTORS or (sel[0] == "delivery" and sel[1] in ("tracker_state", "tracker_preserves")):
        tools = (xtool,)
    elif sel[0] in ("text", "link"):
        target = (surface.get("deliverables") or {}).get(sel[1]) or {}
        if sel[1] == "tracker":
            tools = (xtool,)
        elif target.get("kind") == "table":
            tools = TABLE_TOOLS          # R7-5: a table-targeted text/link slot is decided by the table writers
        else:
            tools = aliases(target.get("tool") or {"slide": "gslides_batch_update",
                                                   "email": "gmail_reply_to_message",
                                                   "slack": "slack_send_message"}.get(sel[1], ""))
    else:
        tools = DELIVERY_TOOLS.get(sel[1], ())
    keys = _failing_keys(slot, d, truth, surface)
    who = tl.deciders(run, briefs_, keys=keys, tools=tools)
    return {"models": who["models"], "keys": keys[:12], "brief_events": [b["event"] for b in who["briefs"]][:12],
            "write_events": [w["event"] for w in who["writes"]][:12]}


# ------------------------------------------------------------------ run one grading pass

def grade_runs(surface: dict, truth: dict, runs: list, context=None, views: str = "auto") -> dict:
    weights = {s["id"]: s["weight"] for s in surface["slots"]}
    all_ids = [s["id"] for s in surface["slots"]]
    graded_ids = [s["id"] for s in surface["slots"] if s.get("gradable") is not False]
    by_id = {s["id"]: s for s in surface["slots"]}
    total = sum(weights.values())
    _, xspec = gs.text_deliverable(surface)
    _, tspec = gs.table_deliverable(surface)
    krx = re.compile(_krx(xspec or tspec))
    expected = (context or {}).get("baseline_model")
    out = {}
    for lab, path in runs:
        run = tl.load(path, lab)
        d = decode(run, surface)
        res = grade(surface, truth, d)
        tw = sum(weights[i] for i in all_ids)
        ungraded = [i for i in all_ids if res[i] is None]
        passed = sum(weights[i] for i in all_ids if res[i])
        bounds = [round(passed / tw, 6), round((passed + sum(weights[i] for i in ungraded)) / tw, 6)] if tw else [0.0, 0.0]
        status, reason, _ = ds.read_trajectory(Path(path)) if run.format == "stream-json" else ("completed", "", None)
        prov = tl.provenance(run, expected_model=expected)
        bl = tl.briefs(run, krx)
        failed = [i for i in graded_ids if res[i] is False]
        out[lab] = {"file": tl._rel(Path(path)), "sha256": tl.sha256_file(Path(path)), "status": status,
                    "register_kind": d["table"]["kind"], "rows": len(d["table"]["rows"]),
                    "score": bounds[0] if not ungraded else None, "score_bounds": bounds if ungraded else None,
                    "failed_slots": failed, "ungraded": [i for i, v in res.items() if v is None],
                    "unreadable": d["unreadable"], "classes": d["classes"], "printed_totals": d["printed"],
                    "tracker_groups": {g: [n, len(set(k))] for g, (n, k) in d["groups"].items()},
                    "results": res, "decided_by": {sid: decided_by(run, bl, by_id[sid], d, truth, surface) for sid in failed},
                    "counted_calls": ds.count_tool_calls(run.events)["counted"] if run.events else None,
                    "models": ds.trajectory_models(Path(path)) if run.format == "stream-json" else [],
                    "model_source": f"trajectory:{Path(path).name}",
                    "fallbacks": [f["event"] for f in prov["fallbacks"]], "mixed_model": prov["mixed_model"],
                    "v3_valid": prov["v3_valid"], "model_check": prov["model_check"]}
    graded_weight = sum(weights[i] for i in graded_ids)
    report = {"kind": "SURFACE_GRADES_NOT_PLATFORM_VERIFIER", "tool": VERSION,
              "note": "design check: the rubric and the verifier remain the grading of record",
              "coverage": {"graded_weight": graded_weight, "total_weight": total,
                           "share": round(graded_weight / total, 4) if total else 0.0}, "runs": out}
    vs = choose_views(context, out, views)
    report["views"] = vs
    if any(lab not in PRE_LABELS for lab in out):
        report["gates"] = gates(surface, out, context, vs)
    return report


def compare_reference(report: dict, ref: dict) -> list:
    """Slot-by-slot differences against a reference grading ({label: {results, score, ...}})."""
    labels = {"pre": "precheck", "r1": "run-1"}
    diffs = []
    for lab, r in report["runs"].items():
        cand = [k for k in (lab, labels.get(lab), "precheck" if lab == "pre" else None, lab.replace("run-", "r")) if k]
        key = next((k for k in cand if k in ref), None)
        if key is None:
            diffs.append({"run": lab, "difference": "not in the reference"})
            continue
        rr = ref[key]
        for sid, v in r["results"].items():
            want = (rr.get("results") or {}).get(sid)
            if want is not None and v is not None and bool(v) != bool(want):
                diffs.append({"run": lab, "slot": sid, "grader": v, "reference": want})
        for fld in ("score", "classes", "kind"):
            mine = r["register_kind"] if fld == "kind" else r[fld]
            if fld == "score" and mine is None and fld in rr:
                diffs.append({"run": lab, "field": "score", "grader": f"UNGRADED {r['ungraded']} bounds {r['score_bounds']}",
                              "reference": rr[fld]})
            elif fld in rr and (round(mine, 6) != round(rr[fld], 6) if fld == "score" else mine != rr[fld]):
                diffs.append({"run": lab, "field": fld, "grader": mine, "reference": rr[fld]})
        zom = rr.get("zom") or rr.get("tracker_groups")
        if zom is not None and {g: tuple(v) for g, v in zom.items()} != {g: tuple(v) for g, v in r["tracker_groups"].items()}:
            diffs.append({"run": lab, "field": "tracker_groups", "grader": r["tracker_groups"], "reference": zom})
        if "calls" in rr and rr["calls"] != r["counted_calls"]:
            diffs.append({"run": lab, "field": "counted_calls", "grader": r["counted_calls"], "reference": rr["calls"]})
    return diffs


def compare_official(report: dict, official: dict) -> list:
    """Slot-by-slot disagreements with the official corrected matrix (rubric ids that equal slot ids)."""
    diffs = []
    rollouts = {ro["id"]: ro for ro in official.get("rollouts", [])}
    for lab, r in report["runs"].items():
        ro = rollouts.get(lab)
        if not ro or ro.get("status") != "completed":
            continue
        res = {**ro.get("results", {}), **(ro.get("judge_corrections") or {})}
        for sid, v in r["results"].items():
            if sid in res and v is not None and bool(v) != bool(res[sid]):
                diffs.append({"run": lab, "slot": sid, "grader": v, "official": res[sid]})
    return diffs


def to_text(report: dict) -> str:
    lines = [f"SURFACE GRADES (design check; rubric + verifier remain of record) · coverage "
             f"{report['coverage']['graded_weight']}/{report['coverage']['total_weight']}"]
    for lab, r in report["runs"].items():
        score = (f"{r['score']:.1%}" if r["score"] is not None else
                 f"{r['score_bounds'][0]:.1%}..{r['score_bounds'][1]:.1%} (UNGRADED {r['ungraded']})")
        lines.append(f"  {lab}: {r['register_kind'] or 'NO REGISTER'} rows={r['rows']} score={score} "
                     f"failed={r['failed_slots']} calls={r['counted_calls']} models={r['models']}"
                     + (" MIXED-MODEL" if r["mixed_model"] else "") + ("" if r.get("v3_valid") else " V3-INVALID"))
    for spec, g in (report.get("gates") or {}).items():
        if "error" in g:
            lines.append(f"  {spec}: gate computation refused: {g['error']}")
            continue
        lines.append(f"  {spec}" + (f" ({g['difficulty_mode']})" if g.get("difficulty_mode") else "") + ": "
                     + " | ".join(f"{k} {v['verdict'].split(' (')[0]} {str(v['value'])[:44]}" for k, v in g["difficulty_gates"].items()))
        if g.get("ungraded_cells"):
            lines.append(f"      UNGRADED cells {g['ungraded_cells'][:8]}: INCOMPLETE gates {g['incomplete'] or 'none'}")
        lines.append("      provenance: " + " | ".join(f"{k} {v['verdict'].split(' (')[0]} {str(v['value'])[:60]}"
                                                     for k, v in g["provenance_gates"].items()))
    return "\n".join(lines)


# ------------------------------------------------------------------ planted cases (G1: each fails under the old rule)

FORMAT_FIXTURES = BUNDLE / "support" / "fixtures" / "surface_formats"
_PLANTED_SURFACE = {
    "kind": "GRADABLE_SURFACE", "version": 1, "classes": ["READY", "HOLD"],
    "truth_fields": {"class": "class", "groups": "groups"},
    "deliverables": {"tracker": {"kind": "text", "tool": "linear_update_issue", "issue": "T-1", "key_regex": r"K-\d{2}",
                                 "groups": [["review", "review"], ["late", "late"]]},
                     "slack": {"kind": "json_text", "tool": "slack_send_message"},
                     "email": {"kind": "json_text", "tool": "gmail_reply_to_message"},
                     "trello": {"kind": "calls", "tool": "trello_add_comment_to_card"}},
    "slots": []}
_PLANTED_REGISTER = {"kind": "table", "name_regex": "register", "key_column": "key", "key_regex": r"K-\d{2}",
                     "columns": ["key", "class"], "class_column": "class"}


def _planted_run(calls: list) -> tl.Run:
    """An in-memory run from (tool, input[, result data]) tuples in order; every call succeeds."""
    cs, rs = [], {}
    for i, c in enumerate(calls):
        cs.append({"event": i, "id": f"c{i}", "name": f"mcp__hg__{c[0]}", "input": c[1], "model": "claude-opus-5-5",
                   "parent": None, "context": "main"})
        rs[f"c{i}"] = {"event": i, "error": False, "data": c[2] if len(c) > 2 else {"ok": True}}
    return tl.Run("planted", Path("planted.json"), "derived-calls", None, cs, rs)


def _grade_planted(selectors: dict, calls: list, truth: dict | None = None, register: bool = False) -> dict:
    surface = json.loads(json.dumps(_PLANTED_SURFACE))
    if register:
        surface["deliverables"]["register"] = json.loads(json.dumps(_PLANTED_REGISTER))
    surface["slots"] = [{"id": sid, "weight": 1, "selector": sel} for sid, sel in selectors.items()]
    return grade(surface, truth or {}, decode(_planted_run(calls), surface))


def _grade_on(surface: dict, calls: list, truth: dict | None = None) -> dict:
    """Grade planted calls on a caller-built surface (multi-table deliverables, slot-level options)."""
    return grade(surface, truth or {}, decode(_planted_run(calls), surface))


def _tracker(text: str) -> list:
    return [("linear_update_issue", {"id": "T-1", "description": text})]


def _g1_heading():
    """Defect 1: a section starts at the heading-like line, not at the first mention in prose."""
    text = ("Blocker groups first; review findings follow under their own heading.\nlate (1): K-01\n"
            "### Review findings\n- K-02\n- K-03")
    r = _grade_planted({"L": ["tracker_lists", "review findings", "K-02"], "N": ["tracker_count", "review findings", 2]},
                       _tracker(text))
    assert r == {"L": True, "N": True}, r


def _g1_section_body():
    """Defect 2: intro prose and a table header don't end a section."""
    text = ("### Process findings\nApproved reviews that follow an open change request. Each one is a WATCH condition:\n"
            "| Key | Note |\n|---|---|\n| K-04 | approved after a change request |\n"
            "| K-05 | approved after a change request |\n### Owner calls\n- K-06")
    r = _grade_planted({"L": ["tracker_lists", "process findings", "K-05"],
                        "N": ["tracker_count", "process findings", 2]}, _tracker(text))
    assert r == {"L": True, "N": True}, r


def _g1_plain_text():
    """Defect 3: text selectors read the plain strings; in the JSON dump "\nHOLD" reads "nHOLD" and breaks \b."""
    r = _grade_planted({"T": ["text", "slack", r"\bHOLD 67\b"]},
                       [("slack_send_message", {"channel_id": "C1", "text": "Register done.\nHOLD 67 | READY 44"})])
    assert r == {"T": True}, r


def _g1_every_update():
    """Defect 4: state and preservation follow every tracker update in order, not only the last one."""
    r = _grade_planted({"S": ["delivery", "tracker_state", "in review"],
                        "P": ["delivery", "tracker_preserves", "Original scope sentence."]},
                       [("linear_update_issue", {"id": "T-1", "description": "Rewritten summary.", "state": "In Review"}),
                        ("linear_update_issue", {"id": "T-1", "patch": [{"op": "append", "text": "late (1): K-01"}]})])
    assert r == {"S": True, "P": False}, r


def _g1_bullet_key_list():
    """Defect 5: a bullet holding a bare key list counts every key; a prose bullet still counts only its first key."""
    text = "### Owner calls\n- K-06, K-07, K-08\n- K-09 approved after the change request on K-11 was dismissed"
    r = _grade_planted({"N": ["tracker_count", "owner calls", 4]}, _tracker(text))
    assert r == {"N": True}, r


def _g1_range_prose():
    """Defect 6: a line that names keys only as a range is prose about the cohort, never a group."""
    text = ("Snapshot 2026-02-12. Evidence review, not approval to ship. One row per included component (K-01..K-20).\n"
            "- **Review not approved (2):** K-12, K-13")
    truth = {"K-01": {"groups": []}, "K-12": {"groups": ["review"]}, "K-13": {"groups": ["review"]}}
    r = _grade_planted({"C": ["group_count", "review"], "Z": ["group_size", "review"],
                        "K": ["group_key", "K-12", "review"]}, _tracker(text), truth)
    assert r == {"C": True, "Z": True, "K": True}, r


def _g1_tool_alias():
    """Defect 7: a Slack thread reply sent with slack_conversations_add_message counts like slack_send_message."""
    r = _grade_planted({"T": ["delivery", "slack_thread", "1771012800.000101"], "A": ["delivery", "slack_after_email"],
                        "X": ["text", "slack", r"READY 44"]},
                       [("gmail_reply_to_message", {"message_id": "m1", "body": "Done; the flag is false."}),
                        ("slack_conversations_add_message", {"channel_id": "C1", "thread_ts": "1771012800.000101",
                                                             "payload": "Register done: READY 44"})])
    assert r == {"T": True, "A": True, "X": True}, r


def _g1_sha_prefix():
    """Defect 8: a SHA value matches an unambiguous prefix of 7 or more characters; an ambiguous or shorter one
    doesn't."""
    text = ("### Value notes\n- K-14: receipt a1b2c3d4 replaced by e5f6a7b8\n"
            "- K-15: receipt 9f8e7d6c replaced by 0a1b2c3d\n- K-16: receipt abcdef replaced by 123456")
    r = _grade_planted({"E": ["tracker_entry", "value notes", "K-14", ["a1b2c3d4e5f60718", "e5f6a7b8c9d00112"]],
                        "Y": ["tracker_entry", "value notes", "K-15", ["9f8e7d6c00000000", "0a1b2c3d44444444"]],
                        "W": ["tracker_entry", "value notes", "K-15", ["9f8e7d6c11111111", "0a1b2c3d44444444"]],
                        "Q": ["tracker_entry", "value notes", "K-16", ["abcdef0123456789", "1234567890abcdef"]]},
                       _tracker(text))
    assert r == {"E": True, "Y": False, "W": False, "Q": False}, r


def _g1_entry_tail():
    """G1-8: a value on the line belongs to the key it follows, not to every key mentioned on the line."""
    r = _grade_planted({"K1": ["tracker_entry", "value notes", "K-01", ["HOLD"]],
                        "K2": ["tracker_entry", "value notes", "K-02", ["HOLD"]]},
                       _tracker("### Value notes\n- K-02: HOLD; see K-01"))
    assert r == {"K1": False, "K2": True}, r


def _g1_issue_exact():
    """G1-7: the tracking issue is matched exactly: an update of T-10 never supplies T-1's content, and there is no
    fallback to unrelated updates."""
    upd = lambda i, text: ("linear_update_issue", {"id": i, "patch": [{"op": "append", "text": text}]})
    r = _grade_planted({"A": ["tracker_lists", "owner calls", "K-01"], "B": ["tracker_lists", "owner calls", "K-02"]},
                       [upd("T-10", "### Owner calls\n- K-01"), upd("T-1", "### Owner calls\n- K-02")])
    assert r == {"A": False, "B": True}, r


def _g1_range_endpoint_member():
    """R2-1: a cohort range expands to every member between its endpoints (K-01..K-03 -> K-01, K-02, K-03) and an
    explicit member equal to an endpoint counts once; a line that only annotates a range is still prose."""
    truth = {f"K-{i:02d}": {"groups": ["review"]} for i in range(1, 4)}
    text = "### Owner calls\n- review (3) K-01, K-01..K-03"
    g = tracker_groups(text, {"key_regex": r"K-\d{2}", "groups": [["review", "review"]]})
    assert g == {"review": (3, ["K-01", "K-02", "K-03"])}, g
    assert _range_only("- review (1) K-01, K-01..K-20", r"K-\d{2}") is False
    assert _range_only("Evidence review (K-01..K-20)", r"K-\d{2}") is True
    r = _grade_planted({"C": ["group_count", "review"], "S": ["group_size", "review"],
                        "K": ["group_key", "K-02", "review"]}, _tracker(text), truth)
    assert r == {"C": True, "S": True, "K": True}, r


def _g1_multiline_group():
    """R8: a group stated once with a count keeps every member of a multi-line list, in all the shapes a run writes:
    bullets, plain key lines and table rows after the stated count. Before the fix every member after the first line
    was dropped, so group_size, group_key and groups_of graded False on a correct tracker."""
    truth = {"K-02": {"class": "HOLD", "groups": ["review"]},
             "K-03": {"class": "HOLD", "groups": ["review"]}}
    sel = {"N": ["group_count", "review"], "Z": ["group_size", "review"],
           "K": ["group_key", "K-03", "review"], "O": ["groups_of", "K-03"]}
    for shape, text in (("bullets", "### Review findings\n- Review not approved (2):\n- K-02\n- K-03"),
                        ("plain", "Review not approved (2):\nK-02\nK-03"),
                        ("table", "Review not approved (2):\n| K-02 | note |\n| K-03 | note |"),
                        # a full Markdown table: header and delimiter rows between the count and its data rows
                        ("table_header", "Review not approved (2):\n| Key | Note |\n| --- | --- |\n"
                                         "| K-02 | first |\n| K-03 | second |"),
                        # a status column first, and the pipe-optional Markdown table form
                        ("table_status", "Review not approved (2):\n| Status | Key |\n| --- | --- |\n"
                                         "| HOLD | K-02 |\n| HOLD | K-03 |"),
                        ("table_nopipe", "Review not approved (2):\nStatus | Key\n--- | ---\n"
                                         "HOLD | K-02\nHOLD | K-03"),
                        ("table_onecol", "Review not approved (2):\n| Key |\n| --- |\n| K-02 |\n| K-03 |"),
                        ("date_heading", "### Review findings \u2014 2026-10-25\nReview not approved (2):\n- K-02\n- K-03"),
                        ("date_tail", "Review not approved (2) \u2014 as of 2026-10-25:\n- K-02\n- K-03"),
                        ("hash_cell", "Review not approved (2):\nTicket | Key\n--- | ---\n#81 | K-02\n#82 | K-03"),
                        ("esc_bullet", "Review not approved (2):\n- K-02\n- K-03 \u2014 read \\| write access"),
                        ("tab_members", "Review not approved (2):\n- K-02\n-\tK-03"),
                        ("tab_header", "Review not approved (2):\n#\t| Key\n--- | ---\n1 | K-02\n2 | K-03"),
                        ("task_list", "Review not approved (2):\n- [ ] K-02\n- [x] K-03"),
                        ("task_code", "Review not approved (2):\n- [ ] `K-02`\n- [x] `K-03`"),
                        ("month_declined", "Review declined 2:\n- K-02\n- K-03"),
                        ("month_marked", "Review marked 2:\n- K-02\n- K-03"),
                        ("month_date", "Review not approved (2) \u2014 as of October 25:\n- K-02\n- K-03"),
                        ("month_abbr", "Review not approved (2) \u2014 as of Oct 25:\n- K-02\n- K-03"),
                        ("month_abbr_dot", "Review not approved (2) \u2014 as of Oct. 25:\n- K-02\n- K-03"),
                        ("month_sept", "Review not approved (2) \u2014 as of Sept 25:\n- K-02\n- K-03"),
                        ("time_tail", "Review not approved (2) \u2014 as of 2026-10-25 09:30:\n- K-02\n- K-03"),
                        ("year_suffix", "Review not approved (2) \u2014 cycle (2026):\n- K-02\n- K-03"),
                        # the other standard Markdown bullet marker
                        ("plus", "Review not approved (2):\n+ K-02\n+ K-03"),
                        # the first member on the count line, the rest on continuation lines (round-4 finding)
                        ("mixed", "Review not approved (2): K-02\n- K-03")):
        r = _grade_planted(sel, _tracker(text), truth)
        assert r == {"N": True, "Z": True, "K": True, "O": True}, (shape, r)


def _g1_multiline_guard():
    """R8: a group already written is never re-opened by a later prose statement of it, so it cannot absorb a later
    list (rev14 `pre`: "… changes-requested review … (7):" after `review` was stated; slot S54 would flip)."""
    truth = {"K-02": {"class": "HOLD", "groups": ["review"]}, "K-03": {"class": "HOLD", "groups": ["review"]},
             "K-06": {"class": "HOLD", "groups": []}}
    text = ("### Review findings\n- Review not approved (2):\n- K-02\n- K-03\n"
            "Approved transfer review preceded by a changes-requested review on the same PR (7):\n- K-06")
    g = tracker_groups(text, {"key_regex": r"K-\d{2}", "groups": [["review", "review"]]})
    assert g == {"review": (2, ["K-02", "K-03"])}, g
    # a ZERO-count first declaration is authoritative too: a later prose re-statement must not reopen and absorb
    zero = ("### Review findings\n- Review not approved (0):\n"
            "Approved transfer review preceded by a changes-requested review on the same PR (7):\n- K-06")
    g0 = tracker_groups(zero, {"key_regex": r"K-\d{2}", "groups": [["review", "review"]]})
    assert g0 == {"review": (0, [])}, g0
    # a re-statement containing a pipe is still a re-statement, never a continuation (keyed and keyless forms)
    for again in ("- Review not approved (0):\n- Review not approved (7): K-06 | follow-up only",
                  "- Review not approved (0):\n- Review not approved (7) | note only"):
        ga = tracker_groups(again, {"key_regex": r"K-\d{2}", "groups": [["review", "review"]]})
        assert ga == {"review": (0, [])}, (again, ga)
    # a pipe-containing heading that declares a NEW group is a declaration, never a table row
    multi = "- Review not approved (1): K-02\n### Late | overdue (1):\n- K-03"
    gm = tracker_groups(multi, {"key_regex": r"K-\d{2}", "groups": [["review", "review"], ["late", "late"]]})
    assert gm == {"review": (1, ["K-02"]), "late": (1, ["K-03"])}, gm
    # a heading that mentions a pipe but declares nothing is prose, not a table: it ends the pending group
    prose = "Review not approved (1): K-02\n### Next steps | owners\n- K-03"
    gp = tracker_groups(prose, {"key_regex": r"K-\d{2}", "groups": [["review", "review"]]})
    assert gp == {"review": (1, ["K-02"])}, gp
    # an ESCAPED pipe is prose, never a table row, and ends the group — including on a line that carries a key
    esc = "Review not approved (1):\n- K-02\nThis paragraph uses an escaped \\| pipe and ends the list.\n- K-03"
    ge = tracker_groups(esc, {"key_regex": r"K-\d{2}", "groups": [["review", "review"]]})
    assert ge == {"review": (1, ["K-02"])}, ge
    esc_key = "Review not approved (1):\n- K-02\nK-03 \\| Approved; follow-up is handled separately.\n- K-04"
    gek = tracker_groups(esc_key, {"key_regex": r"K-\d{2}", "groups": [["review", "review"]]})
    assert gek == {"review": (1, ["K-02"])}, gek
    # a table header that contains the group word and a parenthesised YEAR is a header, not a re-declaration
    alias = ("Review not approved (2):\n| Review cycle (2026) | Key |\n| --- | --- |\n"
             "| HOLD | K-02 |\n| HOLD | K-03 |")
    gal = tracker_groups(alias, {"key_regex": r"K-\d{2}", "groups": [["review", "review"]]})
    assert gal == {"review": (2, ["K-02", "K-03"])}, gal
    # a standalone horizontal rule is NOT a table: it ends the group, and pipe prose after it adds nothing
    spec1 = {"key_regex": r"K-\d{2}", "groups": [["review", "review"]]}
    hr = "Review not approved (1):\n- K-02\n\n---\n\nFollow-up for K-03 | approved.\n- K-04"
    assert tracker_groups(hr, spec1) == {"review": (1, ["K-02"])}, tracker_groups(hr, spec1)
    # a key-shaped example inside a table header is a column label, not a member
    hdrkey = ("Review not approved (2):\n| Key (example K-99) | Reason |\n| --- | --- |\n"
              "| K-02 | a |\n| K-03 | b |")
    assert tracker_groups(hdrkey, spec1) == {"review": (2, ["K-02", "K-03"])}, tracker_groups(hdrkey, spec1)
    # a table cell that contains the group word and a number is data, not a re-declaration
    cellword = ("Review not approved (2):\n| Note | Key |\n| --- | --- |\n"
                "| Review cycle (1) | K-02 |\n| Awaiting sign-off | K-03 |")
    assert tracker_groups(cellword, spec1) == {"review": (2, ["K-02", "K-03"])}, tracker_groups(cellword, spec1)
    # a markdown bullet whose whitespace is a TAB is still a bullet, not a table row
    tab = ("Review not approved (1):\n| Key | Note |\n| --- | --- |\n| K-02 | a |\n"
           "-\tLate (1): K-03 | overdue")
    gt = tracker_groups(tab, {"key_regex": r"K-\d{2}", "groups": [["review", "review"], ["late", "late"]]})
    assert gt == {"review": (1, ["K-02"]), "late": (1, ["K-03"])}, gt
    # a table DATA CELL that names a DIFFERENT undeclared group must not declare it or hijack the table
    spec2 = {"key_regex": r"K-\d{2}", "groups": [["review", "review"], ["late", "late"]]}
    other = ("Late (2):\n| Note | Key |\n| --- | --- |\n"
             "| Review cycle (1) | K-02 |\n| Awaiting sign-off | K-03 |")
    assert tracker_groups(other, spec2) == {"late": (2, ["K-02", "K-03"])}, tracker_groups(other, spec2)
    # a key-shaped header label that names another group adds neither a group nor a member
    oh = ("Late (2):\n| Review cycle (1) | Key (example K-99) |\n| --- | --- |\n"
          "| HOLD | K-02 |\n| HOLD | K-03 |")
    assert tracker_groups(oh, spec2) == {"late": (2, ["K-02", "K-03"])}, tracker_groups(oh, spec2)
    # a LONG counted heading keeps first-declaration authority (the 160-character prose heuristic is not for headings)
    long_head = ("### Review not approved \u2014 items awaiting security, service-owner, quality-assurance, operations, "
                 "or release-management approval for this deployment window, including follow-ups from the preceding "
                 "review cycle (0):\nReview not approved (1): K-02")
    glh = tracker_groups(long_head, {"key_regex": r"K-\d{2}", "groups": [["review", "review"]]})
    assert glh == {"review": (0, [])}, glh
    r = _grade_planted({"N": ["group_count", "review"], "Z": ["group_size", "review"],
                        "K": ["group_key", "K-06", "review"], "O": ["groups_of", "K-06"]}, _tracker(text), truth)
    assert r == {"N": True, "Z": True, "K": True, "O": True}, r


def _p1_printed_total():
    """P1: the totals block's printed class count grades both ways (2 stated for two rows passes, 3 fails)."""
    s = json.loads(json.dumps(_PLANTED_SURFACE))
    s["deliverables"]["register"] = json.loads(json.dumps(_PLANTED_REGISTER))
    s["slots"] = [{"id": "P", "weight": 1, "selector": ["printed_total", "HOLD"]}]
    truth = {"K-01": {"class": "HOLD", "groups": []}, "K-02": {"class": "HOLD", "groups": []}}

    def calls(stated):
        return [("gdrive_create_file", {"name": "register.csv",
                                        "content": f"key,class\nK-01,HOLD\nK-02,HOLD\nHOLD,{stated}\n"}, {"id": "F1"})]
    assert _grade_on(s, calls(2), truth) == {"P": True}, _grade_on(s, calls(2), truth)
    assert _grade_on(s, calls(3), truth) == {"P": False}, _grade_on(s, calls(3), truth)


def _p1_sole_reason():
    """P1: a key in exactly the named group passes; in another group too, or in none, it fails."""
    truth = {"K-01": {"class": "HOLD", "groups": ["review"]}}
    sel = {"S": ["sole_reason", "K-01", "review"]}
    ok = _grade_planted(sel, _tracker("### Review findings\n- Review not approved (2):\n- K-01\n- K-02"), truth)
    assert ok == {"S": True}, ok
    two = _grade_planted(sel, _tracker("- Review not approved (1): K-01\n- Late (1): K-01"), truth)
    assert two == {"S": False}, two
    none = _grade_planted(sel, _tracker("- Review not approved (1): K-02"), truth)
    assert none == {"S": False}, none


def _p1_reason_matches():
    """P1: reason_matches reads the row's reason column (a match passes, a different reason fails) and is UNGRADED,
    never false, when the register write cannot be read."""
    s = json.loads(json.dumps(_PLANTED_SURFACE))
    reg = json.loads(json.dumps(_PLANTED_REGISTER))
    reg.update(columns=["key", "class", "reason"], reason_column="reason")
    s["deliverables"]["register"] = reg
    s["slots"] = [{"id": "M", "weight": 1, "selector": ["reason_matches", "K-01", r"change[- ]request"]}]
    truth = {"K-01": {"class": "HOLD", "groups": []}}

    def call(reason):
        return [("gdrive_create_file", {"name": "register.csv",
                                        "content": f"key,class,reason\nK-01,HOLD,{reason}\n"}, {"id": "F1"})]
    assert _grade_on(s, call("open change-request review"), truth) == {"M": True}
    assert _grade_on(s, call("approved after review"), truth) == {"M": False}
    bad = [("gdrive_create_file", {"name": "register.csv",
                                   "content": "key,class,reason\nK-01,HOLD," + "x" * 140000 + "\n"}, {"id": "F1"})]
    assert _grade_on(s, bad, truth) == {"M": None}, _grade_on(s, bad, truth)


def _p1_tracker_state_comment():
    """P1: tracker_state "comment" needs a comment body, never a card id in a routing field; the 24-hex cardId form
    needs that exact card and a body."""
    hexid = "5f8e7d6c9a1b2c3d4e5f6071"
    sel = {"C": ["delivery", "tracker_state", "comment"], "H": ["delivery", "tracker_state", hexid]}
    ok = _grade_planted(sel, [("trello_add_comment_to_card", {"cardId": "C1", "text": "comment noted"}),
                              ("trello_add_comment_to_card", {"cardId": hexid, "text": "noted"})])
    assert ok == {"C": True, "H": True}, ok
    routing = _grade_planted(sel, [("trello_add_comment_to_card", {"cardId": "C1", "idList": "L1"}),
                                   ("trello_add_comment_to_card", {"cardId": hexid, "idList": hexid})])
    assert routing == {"C": False, "H": False}, routing
    other = _grade_planted(sel, [("trello_add_comment_to_card", {"cardId": "000000000000000000000000",
                                                                 "text": "noted"})])
    assert other == {"C": True, "H": False}, other


def _p1_slack_channel_post():
    """P1: a channel post is the right channel *and* the text as message content; the same text in a routing
    parameter (thread_ts) or the wrong channel fails."""
    sel = {"P": ["delivery", "slack_channel_post", "C1", "SHIP 38"]}
    ok = _grade_planted(sel, [("slack_send_message", {"channel_id": "C1", "text": "SHIP 38 is ready"})])
    assert ok == {"P": True}, ok
    ts = _grade_planted(sel, [("slack_send_message", {"channel_id": "C1", "thread_ts": "SHIP 38"})])
    assert ts == {"P": False}, ts
    chan = _grade_planted(sel, [("slack_send_message", {"channel_id": "C2", "text": "SHIP 38"})])
    assert chan == {"P": False}, chan


def _p1_trello_card():
    """P1: trello_card needs the named card and the value on it; a wrong card or a wrong value fails."""
    sel = {"T": ["delivery", "trello_card", "C1", "hello"]}
    ok = _grade_planted(sel, [("trello_add_comment_to_card", {"cardId": "C1", "text": "hello there"})])
    assert ok == {"T": True}, ok
    card = _grade_planted(sel, [("trello_add_comment_to_card", {"cardId": "C2", "text": "hello there"})])
    assert card == {"T": False}, card
    value = _grade_planted(sel, [("trello_add_comment_to_card", {"cardId": "C1", "text": "goodbye"})])
    assert value == {"T": False}, value


def _p1_register_is_csv():
    """P1: register_is_csv passes on a CSV upload and fails on a native Sheet holding the same rows."""
    sel = {"V": ["delivery", "register_is_csv"]}
    truth = {"K-01": {"class": "HOLD", "groups": []}}
    csv_upload = _grade_planted(sel, [("gdrive_create_file", {"name": "register.csv",
                                                              "content": "key,class\nK-01,HOLD\n"}, {"id": "F1"})],
                                truth, register=True)
    assert csv_upload == {"V": True}, csv_upload
    sheet = _grade_planted(sel, [("gsheets_values_update", {"spreadsheetId": "S1", "range": "A1:B2",
                                                            "values": [["key", "class"], ["K-01", "HOLD"]]})],
                           truth, register=True)
    assert sheet == {"V": False}, sheet


def _p1_register_parent():
    """P1: the register's final folder is the creation parent plus any later move: a move to the expected folder
    passes, a move elsewhere fails."""
    s = json.loads(json.dumps(_PLANTED_SURFACE))
    s["deliverables"]["register"] = json.loads(json.dumps(_PLANTED_REGISTER))
    s["slots"] = [{"id": "M", "weight": 1, "selector": ["delivery", "register_parent", "PARENT1"]}]
    truth = {"K-01": {"class": "HOLD", "groups": []}}

    def calls(target):
        return [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\n",
                                        "parentId": "PARENT0"}, {"id": "F1"}),
                ("gdrive_share_file", {"fileId": "F1", "role": "reader"}),
                ("gdrive_move_file", {"fileId": "F1", "newParentId": target})]
    assert _grade_on(s, calls("PARENT1"), truth) == {"M": True}, _grade_on(s, calls("PARENT1"), truth)
    assert _grade_on(s, calls("PARENT2"), truth) == {"M": False}, _grade_on(s, calls("PARENT2"), truth)


def _g1_unreadable_register():
    """A register write the decoder can't read leaves its slots UNGRADED (None), never false; other slots still grade."""
    content = "key,class\nK-01," + "x" * 140000 + "\n"          # over the csv field limit: csv.Error
    r = _grade_planted({"F": ["field", "K-01", "class"], "T": ["total", "HOLD"], "C": ["delivery", "register_is_csv"],
                        "G": ["group_count", "late"]},
                       [("gdrive_create_file", {"name": "register.csv", "content": content}, {"id": "f1"}),
                        ("linear_update_issue", {"id": "T-1", "description": "late (1): K-01"})],
                       {"K-01": {"class": "HOLD", "groups": ["late"]}}, register=True)
    assert r == {"F": None, "T": None, "C": None, "G": True}, r


def _g1_unreadable_tracker():
    """A mutation the decoder can't read (a patch whose value is not text) leaves every tracker-content slot UNGRADED,
    including tracker_preserves; other targets still grade."""
    r = _grade_planted({"G": ["group_count", "late"], "L": ["tracker_lists", "late", "K-01"],
                        "P": ["delivery", "tracker_preserves", "late (1)"],
                        "X": ["text", "tracker", "K-01"], "T": ["text", "slack", "done"]},
                       [("linear_update_issue", {"id": "T-1", "patch": json.dumps(
                           {"op": "replace", "path": "/description", "value": 7})}),
                        ("slack_send_message", {"channel_id": "C1", "text": "done"})],
                       {"K-01": {"class": "HOLD", "groups": ["late"]}})
    assert r == {"G": None, "L": None, "P": None, "X": None, "T": True}, r


def _g1_register_replacement():
    """G1-3: a readable register followed by an unreadable write to the delivered register is UNGRADED (the old decoder
    kept the earlier readable rows and graded definitively)."""
    big = "key,class\nK-01," + "x" * 140000 + "\n"          # over the csv field limit: the delivered register is unreadable
    r = _grade_planted({"F": ["field", "K-01", "class"]},
                       [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\n"}, {"id": "f1"}),
                        ("gdrive_create_file", {"name": "register.csv", "content": big}, {"id": "f2"}),
                        ("gdrive_share_file", {"fileId": "f2", "role": "reader"})],
                       {"K-01": {"class": "HOLD"}}, register=True)
    assert r == {"F": None}, r


def _g1_register_update():
    """G1-3: a content update without a repeated name is still the register, by its fileId."""
    r = _grade_planted({"F": ["field", "K-01", "class"]},
                       [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\n"}, {"id": "f1"}),
                        ("gdrive_update_file", {"fileId": "f1", "content": "key,class\n"}, {}),
                        ("gdrive_share_file", {"fileId": "f1", "role": "reader"})],
                       {"K-01": {"class": "HOLD"}}, register=True)
    assert r == {"F": False}, r


def _g1_preserve_unknown():
    """G1-2/4: an unknown mutation makes preservation uncertain (None) unless a later readable replacement is a known
    violation (False); a known violation is never erased by an unknown one."""
    upd = lambda **q: ("linear_update_issue", {"id": "T-1", **q})
    unknown = upd(patch=[{"op": "replace", "path": "/description", "value": 7}])
    fail = _grade_planted({"P": ["delivery", "tracker_preserves", "scope A"]},
                          [upd(description="scope A"), unknown, upd(description="scope B")])
    assert fail == {"P": False}, fail
    uncertain = _grade_planted({"P": ["delivery", "tracker_preserves", "scope A"]},
                               [upd(description="scope A"), unknown, upd(description="scope A")])
    assert uncertain == {"P": None}, uncertain


def _g1_move_source():
    """G1-2: a move whose source is the description removes it; the old decoder looked only at the destination."""
    r = _grade_planted({"L": ["tracker_lists", "owner calls", "K-01"]},
                       [("linear_update_issue", {"id": "T-1", "description": "### Owner calls\n- K-01"}),
                        ("linear_update_issue", {"id": "T-1", "patch": [
                            {"op": "move", "from": "/description", "path": "/archived"}]})])
    assert r == {"L": False}, r


def _g1_entry_table():
    """G1-8: on a table row the owning key is the first cell; a cross-reference in another cell does not own the row's
    value."""
    text = "### Value notes\n| Key | Related | Disposition |\n| K-02 | see K-01 | HOLD |"
    r = _grade_planted({"K1": ["tracker_entry", "value notes", "K-01", ["HOLD"]],
                        "K2": ["tracker_entry", "value notes", "K-02", ["HOLD"]]}, _tracker(text))
    assert r == {"K1": False, "K2": True}, r


def _g1_link_nested():
    """G1-11: a nested identifier (a slide objectId) is not a link; only deliverable text counts."""
    r = _grade_planted({"L": ["link", "slide"]},
                       [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\n"}, {"id": "f1"}),
                        ("gdrive_share_file", {"fileId": "f1", "role": "reader"}),
                        ("gslides_batch_update", {"presentationId": "deck", "requests": [
                            {"insertText": {"objectId": "f1", "text": "Done"}}]})],
                       {"K-01": {"class": "HOLD"}}, register=True)
    assert r == {"L": False}, r


def _g1_register_cross_file():
    """G1-3: an earlier readable native Sheet must not mask a later unreadable CSV that is the shared register."""
    big = "key,class\nK-01," + "x" * 140000 + "\n"
    r = _grade_planted({"F": ["field", "K-01", "class"]},
                       [("gsheets_values_update", {"spreadsheetId": "S1", "range": "A1:B2",
                                                   "values": [["key", "class"], ["K-01", "HOLD"]]}),
                        ("gdrive_create_file", {"name": "register.csv", "content": big}, {"id": "f2"}),
                        ("gdrive_share_file", {"fileId": "f2", "role": "reader"})],
                       {"K-01": {"class": "HOLD"}}, register=True)
    assert r == {"F": None}, r


def _g1_register_unshared_unreadable():
    """G1-3: an unreadable, unshared CSV after the delivered readable CSV does not invalidate it."""
    big = "key,class\nK-01," + "x" * 140000 + "\n"
    r = _grade_planted({"F": ["field", "K-01", "class"]},
                       [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\n"}, {"id": "f1"}),
                        ("gdrive_share_file", {"fileId": "f1", "role": "reader"}),
                        ("gdrive_create_file", {"name": "register.csv", "content": big}, {"id": "f2"})],
                       {"K-01": {"class": "HOLD"}}, register=True)
    assert r == {"F": True}, r


def _g1_register_empty_replacement():
    """G1-3: a later readable header-only write to the delivered register re-establishes empty content; the old
    'any unreadable candidate' rule left it UNGRADED."""
    big = "key,class\nK-01," + "x" * 140000 + "\n"
    r = _grade_planted({"F": ["field", "K-01", "class"]},
                       [("gdrive_create_file", {"name": "register.csv", "content": big}, {"id": "f2"}),
                        ("gdrive_create_file", {"name": "register.csv", "content": "key,class\n"}, {"id": "f2"}),
                        ("gdrive_share_file", {"fileId": "f2", "role": "reader"})],
                       {"K-01": {"class": "HOLD"}}, register=True)
    assert r == {"F": False}, r


def _g1_delivery_binding():
    """G1-10: the reply target and the Slack thread are bound to the call's own parameters, never to text anywhere in
    the serialized inputs."""
    leak = _grade_planted({"E": ["delivery", "email_reply", "CA202ce27e843eb148967f4d7c7d46"],
                           "T": ["delivery", "slack_thread", "1771012800.000101"]},
                          [("gmail_reply_to_message", {"message_id": "other", "body": "re CA202ce27e843eb148967f4d7c7d46; false"}),
                           ("slack_conversations_add_message", {"channel_id": "C1", "thread_ts": "9.9",
                                                                "payload": "1771012800.000101"})])
    assert leak == {"E": False, "T": False}, leak


def _g1_link_share():
    """G1-11: a link requires the register to be shared and the id to be in the deliverable's text, never in an
    identifier parameter or as a substring of another id."""
    base = [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\n"}, {"id": "f1"})]
    no_share = _grade_planted({"L": ["link", "slack"]},
                              base + [("slack_send_message", {"channel_id": "C1", "text": "see f1"})],
                              {"K-01": {"class": "HOLD"}}, register=True)
    assert no_share == {"L": False}, no_share
    wrong = _grade_planted({"L": ["link", "slack"]},
                           base + [("gdrive_share_file", {"fileId": "f1", "role": "reader"}),
                                   ("slack_send_message", {"channel_id": "f1", "text": "done"})],
                           {"K-01": {"class": "HOLD"}}, register=True)
    assert wrong == {"L": False}, wrong
    ok = _grade_planted({"L": ["link", "slack"]},
                        base + [("gdrive_share_file", {"fileId": "f1", "role": "reader"}),
                                ("slack_send_message", {"channel_id": "C1", "text": "register f1"})],
                        {"K-01": {"class": "HOLD"}}, register=True)
    assert ok == {"L": True}, ok


def _g1_register_identity():
    """G1-11: the register's identity is the decoded table's own file id, never the last file the run shared."""
    share = _grade_planted({"P": ["delivery", "register_parent", "folder-good"]},
                           [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\n",
                                                    "parentId": "folder-wrong"}, {"id": "f1"}),
                            ("gdrive_create_file", {"name": "notes.txt", "content": "x", "parentId": "folder-good"}, {"id": "f2"}),
                            ("gdrive_share_file", {"fileId": "f1", "role": "reader"}),
                            ("gdrive_share_file", {"fileId": "f2", "role": "reader"})],
                           {"K-01": {"class": "HOLD"}}, register=True)
    assert share == {"P": False}, share


def _g1_round2_oxford_backticks():
    """R2-2: Oxford commas and per-key backticks/bold parse to the full key list, not only the first key."""
    text = ("### Owner calls\n- K-01, K-02, and K-03\n- `K-04`, `K-05`\n- **K-06**, **K-07**\n")
    r = _grade_planted({"N": ["tracker_count", "owner calls", 7]}, _tracker(text))
    assert r == {"N": True}, r


def _g1_round2_colon_list_item():
    """R2-3: a colon-terminated list item is a list item, not a section heading that ends the section."""
    text = "### Review findings\n- Review not approved (2):\n- K-02\n- K-03"
    r = _grade_planted({"N": ["tracker_count", "review findings", 2],
                        "L": ["tracker_lists", "review findings", "K-03"]}, _tracker(text))
    assert r == {"N": True, "L": True}, r


def _g1_round2_patch_noops():
    """R2-4: a JSON Patch test and a move to the same path are no-ops; a move from inside description to
    description and a move from outside description into it stay unknown."""
    base = [("linear_update_issue", {"id": "T-1", "description": "### Owner calls\n- K-01", "state": "Todo"})]
    r = _grade_planted({"L": ["tracker_lists", "owner calls", "K-01"],
                        "S": ["delivery", "tracker_state", "Todo"]},
                       base + [("linear_update_issue", {"id": "T-1", "patch": [
                           {"op": "test", "path": "/description", "value": "### Owner calls\n- K-01"},
                           {"op": "move", "from": "/description", "path": "/description"}]})])
    assert r == {"L": True, "S": True}, r
    inner = _grade_planted({"L": ["tracker_lists", "owner calls", "K-01"]},
                           base + [("linear_update_issue", {"id": "T-1", "patch": [
                               {"op": "move", "from": "/description/0", "path": "/description"}]})])
    assert inner == {"L": None}, inner
    outside = _grade_planted({"L": ["tracker_lists", "owner calls", "K-01"]},
                             base + [("linear_update_issue", {"id": "T-1", "patch": [
                                 {"op": "move", "from": "/labels", "path": "/description"}]})])
    assert outside == {"L": None}, outside


def _g1_round2_named_group_regex():
    """R2-5: a named-group key_regex decodes groups and ranges without re.error."""
    surface = json.loads(json.dumps(_PLANTED_SURFACE))
    surface["deliverables"]["tracker"]["key_regex"] = r"(?P<key>K-\d{2})"
    surface["slots"] = [{"id": "G", "weight": 1, "selector": ["group_count", "review"]},
                        {"id": "S", "weight": 1, "selector": ["group_size", "review"]}]
    truth = {f"K-{i:02d}": {"groups": ["review"]} for i in range(1, 4)}
    r = _grade_on(surface, _tracker("### Owner calls\n- review (3) K-01..K-03"), truth)
    assert r == {"G": True, "S": True}, r


def _g1_round3_named_group_lists():
    """R3-3: a named-group key_regex decodes tracker_lists and tracker_count without re.error (the key regex is used
    through spans, never interpolated twice)."""
    surface = json.loads(json.dumps(_PLANTED_SURFACE))
    surface["deliverables"]["tracker"]["key_regex"] = r"(?P<key>K-\d{2})"
    surface["slots"] = [{"id": "L", "weight": 1, "selector": ["tracker_lists", "owner calls", "K-01"]},
                        {"id": "N", "weight": 1, "selector": ["tracker_count", "owner calls", 2]}]
    r = _grade_on(surface, _tracker("### Owner calls\n- K-01\n- K-02"), {})
    assert r == {"L": True, "N": True}, r


def _g1_round3_unbound_sheet():
    """R3-1: an untitled native Sheet written and shared later never displaces an identified register."""
    calls = [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\n"}, {"id": "f1"}),
             ("gdrive_share_file", {"fileId": "f1", "role": "reader"}),
             ("gsheets_values_update", {"spreadsheetId": "S2", "range": "Sheet1!A1:B2",
                                        "values": [["key", "class"], ["P-01", "HOLD"]]}),
             ("gdrive_share_file", {"fileId": "S2", "role": "reader"})]
    r = _grade_planted({"F": ["field", "K-01", "class"], "K": ["delivery", "register_keys_exact"]}, calls,
                       {"K-01": {"class": "HOLD"}}, register=True)
    assert r == {"F": True, "K": True}, r


def _g1_round3_partial_named_capture():
    """R3-2: a partial or nested named capture must not corrupt key extraction (findall would return the capture)."""
    surface = json.loads(json.dumps(_PLANTED_SURFACE))
    surface["deliverables"]["tracker"]["key_regex"] = r"(?P<prefix>K)-\d{2}"
    surface["slots"] = [{"id": "L", "weight": 1, "selector": ["tracker_lists", "owner calls", "K-01"]},
                        {"id": "N", "weight": 1, "selector": ["tracker_count", "owner calls", 2]}]
    r = _grade_on(surface, _tracker("### Owner calls\n- K-01\n- K-02"), {})
    assert r == {"L": True, "N": True}, r


def _g1_round3_secondary_sha_ambiguity():
    """R3-3: a SHA prefix is ambiguous when a *secondary* table's truth carries another hash with that prefix."""
    surface = json.loads(json.dumps(_PLANTED_SURFACE))
    surface["deliverables"]["register"] = json.loads(json.dumps(_PLANTED_REGISTER))
    surface["deliverables"]["pack"] = {"kind": "table", "name_regex": "pack", "key_column": "key",
                                       "key_regex": r"P-\d{2}", "columns": ["key", "artifact"],
                                       "comparators": {"artifact": "sha_prefix"}}
    surface["deliverables"]["tracker"]["key_regex"] = r"P-\d{2}"
    surface["slots"] = [{"id": "E", "weight": 1,
                         "selector": ["tracker_entry", "value notes", "P-01", ["a1b2c3d4e5f60718"]]}]
    truth = {"P-01": {"artifact": "a1b2c3d4e5f60718"},
             "P-02": {"artifact": "a1b2c3d4ffffffff"}}          # the second hash shares the 8-char prefix
    calls = [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\n"}, {"id": "f1"}),
             ("gdrive_create_file", {"name": "pack.csv", "content": "key,artifact\nP-01,x\n"}, {"id": "f2"}),
             ("linear_update_issue", {"id": "T-1", "description": "### Value notes\n- P-01: a1b2c3d4"})]
    r = _grade_on(surface, calls, truth)
    assert r == {"E": False}, r                          # ambiguous prefix: never a match


def _g1_round2_text_ids():
    """R2-6: text selectors never read objectId/presentationId metadata at any nesting level."""
    r = _grade_planted({"ID": ["text", "slide", r"\bZx9Q\b"], "C": ["text", "slide", r"\bDone\b"]},
                       [("gslides_batch_update", {"presentationId": "Zx9Q", "requests": [
                           {"insertText": {"objectId": "Zx9Q", "text": "Done"}}]})])
    assert r == {"ID": False, "C": True}, r


def _g1_round2_wrapped_email():
    """R2-7: a wrapped Gmail id matches its bare id, while expected m1 never matches actual m10."""
    bare = _grade_planted({"M1": ["delivery", "email_reply", "m1"]},
                          [("gmail_reply_to_message", {"message_id": "<m10@mail>", "reply_all": False})])
    assert bare == {"M1": False}, bare
    wrapped = _grade_planted({"W1": ["delivery", "email_reply", "<m1@mail>"],
                              "W2": ["delivery", "email_reply", "name/<m1@mail>"]},
                             [("gmail_reply_to_message", {"message_id": "m1", "reply_all": False})])
    assert wrapped == {"W1": True, "W2": True}, wrapped
    gmail = _grade_planted({"CA": ["delivery", "email_reply", "CA202ce27e843eb148967f4d7c7d46"]},
                           [("gmail_reply_to_message", {"message_id": "oliver.brooks@harmonygames.co/"
                                                                       "<CA202ce27e843eb148967f4d7c7d46@mail.gmail.com>",
                                                        "reply_all": False})])
    assert gmail == {"CA": True}, gmail


def _g1_round2_missing_group():
    """R2-8: a group the run never delivered fails on its own absence; the truth size is never the observed size."""
    truth = {"K-01": {"groups": ["late"]}, "K-02": {"groups": ["late"]}}
    r = _grade_planted({"C": ["group_count", "late"], "S": ["group_size", "late"],
                        "K": ["group_key", "K-01", "late"]}, _tracker("### Owner calls\n- K-01"), truth)
    assert r == {"C": False, "S": False, "K": False}, r


def _g1_round2_unreadable_sources():
    """R2-9: an unreadable table is UNGRADED for a text selector, and a field slot whose key belongs to an
    unreadable secondary table is UNGRADED; the readable register still grades normally."""
    big = "key,class\nP-01," + "x" * 140000 + "\n"
    surface = json.loads(json.dumps(_PLANTED_SURFACE))
    surface["deliverables"]["register"] = json.loads(json.dumps(_PLANTED_REGISTER))
    surface["deliverables"]["pack"] = {"kind": "table", "name_regex": "pack", "key_column": "key",
                                       "key_regex": r"P-\d{2}", "columns": ["key", "class", "reason"],
                                       "class_column": "class", "reason_column": "reason"}
    surface["slots"] = [{"id": "FR", "weight": 1, "selector": ["field", "K-01", "class"]},
                        {"id": "FP", "weight": 1, "selector": ["field", "P-01", "class"]},
                        {"id": "TR", "weight": 1, "selector": ["text", "register", r"\bHOLD\b"]},
                        {"id": "TP", "weight": 1, "selector": ["text", "pack", r"\bHOLD\b"]},
                        {"id": "RP", "weight": 1, "selector": ["reason_matches", "P-01", r"\bwhy\b"]}]
    calls = [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\n"}, {"id": "f1"}),
             ("gdrive_create_file", {"name": "pack.csv", "content": big}, {"id": "f2"}),
             ("gdrive_share_file", {"fileId": "f1", "role": "reader"})]
    r = _grade_on(surface, calls, {"K-01": {"class": "HOLD"}, "P-01": {"class": "HOLD"}})
    assert r == {"FR": True, "FP": None, "TR": True, "TP": None, "RP": None}, r
    # R3-1: reason_matches resolves the source table by key, so an unreadable pack is UNGRADED, never False


def _g1_round2_register_keys_exact():
    """R2-10: register_keys_exact uses the slot's explicit expected_keys and the named table deliverable."""
    surface = json.loads(json.dumps(_PLANTED_SURFACE))
    surface["deliverables"]["register"] = json.loads(json.dumps(_PLANTED_REGISTER))
    surface["deliverables"]["pack"] = {"kind": "table", "name_regex": "pack", "key_column": "key",
                                       "key_regex": r"P-\d{2}", "columns": ["key", "class"], "class_column": "class"}
    surface["slots"] = [{"id": "A", "weight": 1, "selector": ["delivery", "register_keys_exact"],
                         "expected_keys": ["K-01"]},
                        {"id": "D", "weight": 1, "selector": ["delivery", "register_keys_exact", "pack"]}]
    truth = {"K-01": {}, "K-02": {}, "P-01": {}}
    one = [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\n"}, {"id": "f1"}),
           ("gdrive_create_file", {"name": "pack.csv", "content": "key,class\nP-01,HOLD\n"}, {"id": "f2"})]
    both = [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\nK-02,READY\n"},
             {"id": "f1"}),
            ("gdrive_create_file", {"name": "pack.csv", "content": "key,class\nP-01,HOLD\n"}, {"id": "f2"})]
    r1 = _grade_on(surface, one, truth)
    assert r1 == {"A": True, "D": True}, r1
    r2 = _grade_on(surface, both, truth)
    assert r2 == {"A": False, "D": True}, r2


def _g1_round2_groups_field():
    """R2-11: membership reads truth_fields.groups by name; a scalar value at that field fails, never passes or
    crashes."""
    surface = json.loads(json.dumps(_PLANTED_SURFACE))
    surface["truth_fields"]["groups"] = "blockers"
    surface["slots"] = [{"id": "C", "weight": 1, "selector": ["group_count", "review"]},
                        {"id": "S", "weight": 1, "selector": ["group_size", "review"]},
                        {"id": "G1", "weight": 1, "selector": ["groups_of", "K-01"]},
                        {"id": "G2", "weight": 1, "selector": ["groups_of", "K-02"]}]
    text = "### Owner calls\n- review (2) K-01, K-02"
    good = {"K-01": {"blockers": ["review"]}, "K-02": {"blockers": ["review"]}}
    bad = {"K-01": {"blockers": ["review"]}, "K-02": {"blockers": "review"}}
    ok = _grade_on(surface, _tracker(text), good)
    assert ok == {"C": True, "S": True, "G1": True, "G2": True}, ok
    scalar = _grade_on(surface, _tracker(text), bad)
    assert scalar == {"C": False, "S": False, "G1": True, "G2": False}, scalar


def _g1_round2_share_reader():
    """R2-12: a reader share only counts on the register's own identity, never on an unrelated file."""
    base = [("gdrive_create_file", {"name": "register.csv", "content": "key,class\nK-01,HOLD\n"}, {"id": "f1"})]
    wrong = _grade_planted({"R": ["delivery", "share_reader"]},
                           base + [("gdrive_share_file", {"fileId": "f1", "role": "writer"}),
                                   ("gdrive_share_file", {"fileId": "f2", "role": "reader"})],
                           {"K-01": {"class": "HOLD"}}, register=True)
    assert wrong == {"R": False}, wrong
    ok = _grade_planted({"R": ["delivery", "share_reader"]},
                        base + [("gdrive_share_file", {"fileId": "f1", "role": "reader"})],
                        {"K-01": {"class": "HOLD"}}, register=True)
    assert ok == {"R": True}, ok


def _g1_replay_replacement():
    """G1-2/G1-4: a later full description or a `replace /description` string replaces the earlier content (the old
    decoder concatenated them, so the superseded section stayed authoritative); a short prose bullet counts one key."""
    r = _grade_planted({"OLD": ["tracker_lists", "owner calls", "K-01"], "NEW": ["tracker_lists", "owner calls", "K-02"],
                        "P": ["delivery", "tracker_preserves", "scope A"]},
                       [("linear_update_issue", {"id": "T-1", "description": "scope A\n### Owner calls\n- K-01"}),
                        ("linear_update_issue", {"id": "T-1", "patch": json.dumps(
                            [{"op": "replace", "path": "/description", "value": "scope B\n### Owner calls\n- K-02"}])})])
    assert r == {"OLD": False, "NEW": True, "P": False}, r
    prose = _grade_planted({"ONE": ["tracker_count", "owner calls", 1], "TWO": ["tracker_count", "owner calls", 2]},
                           _tracker("### Owner calls\n- K-01 depends on K-02"))
    assert prose == {"ONE": True, "TWO": False}, prose


def _g1_declared_ungradable_gates():
    """G1-1: a `gradable:false` slot is an unknown cell of the gate matrix: the bounds disagree (0 or 6 full passes;
    6/9 or 9/9 average), so the gates are INCOMPLETE and the cells are listed (the old code dropped them silently)."""
    surface = {"slots": [{"id": "A1", "weight": 3}, {"id": "A2", "weight": 3},
                         {"id": "D", "weight": 3, "gradable": False}]}
    runs = {f"run-{i}": {"status": "completed", "results": {"A1": True, "A2": True, "D": None}, "counted_calls": 600,
                         "models": ["claude-opus-5-5"], "model_source": "planted"} for i in range(1, 7)}
    g = gates(surface, runs, {"spec_version": "V2", "task_type": "long-horizon"}, ["V2"])["V2"]
    dg = g["difficulty_gates"]
    assert dg["avg_weighted_pass_rate"]["verdict"] == "INCOMPLETE" and dg["avg_weighted_pass_rate"]["value"] == {
        "ungraded_failed": "66.7%", "ungraded_passed": "100.0%"}, dg["avg_weighted_pass_rate"]   # 6/9 vs 9/9
    assert dg["pass_at_1"]["verdict"] == "INCOMPLETE" and dg["pass_at_1"]["value"]["ungraded_failed"].startswith("0/6") \
        and dg["pass_at_1"]["value"]["ungraded_passed"].startswith("6/6"), dg["pass_at_1"]
    assert g["ungraded_cells"] == [f"run-{i}:D" for i in range(1, 7)], g["ungraded_cells"]
    assert "avg_weighted_pass_rate" in g["incomplete"], g["incomplete"]


def _g1_ungraded_gates():
    """UNGRADED cells never become fails: every run scores 0.4 with them failed and 0.6 with them passed, so the
    average passes on both bounds, while the SD band differs between completions (INCOMPLETE)."""
    weights = {"A1": 5, "A2": 1, "B": 3, "C1": 5, "C2": 1}          # passed 6/15, UNGRADED 3/15, failed 6/15
    surface = {"slots": [{"id": k, "weight": w} for k, w in weights.items()]}
    runs = {f"run-{i}": {"status": "completed", "results": {"A1": True, "A2": True, "B": None, "C1": False, "C2": False},
                         "counted_calls": 600, "models": ["claude-opus-5-5"], "model_source": "planted"}
            for i in range(1, 7)}
    g = gates(surface, runs, {"spec_version": "V3", "difficulty_mode": "hard", "task_type": "long-horizon"},
              ["V3"])["V3"]
    dg = g["difficulty_gates"]
    assert g["ungraded_cells"] == [f"run-{i}:B" for i in range(1, 7)], g["ungraded_cells"]   # always listed
    assert dg["per_rollout_sd"]["verdict"] == "INCOMPLETE" and g["incomplete"] == ["per_rollout_sd"], dg["per_rollout_sd"]
    assert dg["per_rollout_sd"]["value"]["completions"] == 64, dg["per_rollout_sd"]
    avg = dg["avg_weighted_pass_rate"]
    assert avg["verdict"] == "PASS" and avg["value"]["ungraded_failed"].startswith("40.0%") \
        and avg["value"]["ungraded_passed"].startswith("60.0%"), avg
    assert dg["pass_at_1"]["verdict"] == "PASS" and dg["failure_patterns"]["verdict"] == "FAIL", dg


def _g1_formats() -> int:
    """Every register, tracker and delivery format of the 12 Season Pass runs (support/fixtures/surface_formats): each
    minimal fixture must grade slot for slot like its full run, which matched the grades of record when it was built."""
    m = json.loads((FORMAT_FIXTURES / "MANIFEST.json").read_text())
    surfaces, truths = {}, {}
    for rev, x in m["revisions"].items():
        assert hashlib.sha256((FORMAT_FIXTURES / x["truth"]).read_bytes()).hexdigest() == x["truth_sha256"], rev
        surfaces[rev] = gs.load(FORMAT_FIXTURES / x["surface"])
        truths[rev] = json.loads((FORMAT_FIXTURES / x["truth"]).read_text())
    for f in m["fixtures"]:
        path = FORMAT_FIXTURES / f["file"]
        assert tl.sha256_file(path) == f["sha256"], f"{f['file']}: changed since it was built"
        surface = surfaces[f["revision"]]
        res = grade(surface, truths[f["revision"]], decode(tl.load(path, f["label"]), surface))
        bad = sorted(k for k in f["results"] if res.get(k) != f["results"][k])
        assert not bad, f"{f['revision']} {f['label']}: slots {bad[:8]} differ from the grades of record"
    return len(m["fixtures"])


PLANTED_G1 = (("defect 1 heading", _g1_heading), ("defect 2 section body", _g1_section_body),
              ("defect 3 plain text", _g1_plain_text), ("defect 4 every update", _g1_every_update),
              ("defect 5 bullet key list", _g1_bullet_key_list), ("defect 6 range prose", _g1_range_prose),
              ("defect 7 tool alias", _g1_tool_alias), ("defect 8 SHA prefix", _g1_sha_prefix),
              ("unreadable register", _g1_unreadable_register), ("unreadable tracker", _g1_unreadable_tracker),
              ("replay replacement", _g1_replay_replacement), ("register replacement", _g1_register_replacement),
              ("register cross-file", _g1_register_cross_file),
              ("register update", _g1_register_update), ("preserve unknown", _g1_preserve_unknown),
              ("move source", _g1_move_source), ("entry table", _g1_entry_table),
              ("link nested", _g1_link_nested),
              ("register unshared unreadable", _g1_register_unshared_unreadable),
              ("register empty replacement", _g1_register_empty_replacement),
              ("delivery binding", _g1_delivery_binding), ("register identity", _g1_register_identity),
              ("link share", _g1_link_share),
              ("entry tail", _g1_entry_tail), ("issue exact", _g1_issue_exact),
              ("range endpoint member", _g1_range_endpoint_member),
              ("R2 Oxford/backtick key lists", _g1_round2_oxford_backticks),
              ("R2 colon list item", _g1_round2_colon_list_item),
              ("R2 patch no-ops", _g1_round2_patch_noops),
              ("R2 named-group key regex", _g1_round2_named_group_regex),
              ("R3 named-group tracker lists", _g1_round3_named_group_lists),
              ("R3 unbound sheet", _g1_round3_unbound_sheet),
              ("R3 partial named capture", _g1_round3_partial_named_capture),
              ("R3 secondary SHA ambiguity", _g1_round3_secondary_sha_ambiguity),
              ("R2 text ids", _g1_round2_text_ids),
              ("R2 wrapped email ids", _g1_round2_wrapped_email),
              ("R2 missing group", _g1_round2_missing_group),
              ("R2 unreadable sources", _g1_round2_unreadable_sources),
              ("R2 register keys exact", _g1_round2_register_keys_exact),
              ("R2 groups field", _g1_round2_groups_field),
              ("R2 share reader", _g1_round2_share_reader),
              ("R8 multi-line group", _g1_multiline_group), ("R8 multi-line guard", _g1_multiline_guard),
              ("P1 printed total", _p1_printed_total), ("P1 sole reason", _p1_sole_reason),
              ("P1 reason matches", _p1_reason_matches), ("P1 tracker state comment", _p1_tracker_state_comment),
              ("P1 slack channel post", _p1_slack_channel_post), ("P1 trello card", _p1_trello_card),
              ("P1 register is csv", _p1_register_is_csv), ("P1 register parent", _p1_register_parent),
              ("UNGRADED gates", _g1_ungraded_gates), ("declared-ungradable gates", _g1_declared_ungradable_gates),
              ("formats of the 12 runs", _g1_formats))


# ------------------------------------------------------------------ self-test

def _self_test() -> None:
    import base64
    surface = {"kind": "GRADABLE_SURFACE", "version": 1, "classes": ["READY", "HOLD"],
               "truth_fields": {"class": "class", "groups": "groups"},
               "deliverables": {"register": {"kind": "table", "name_regex": "register", "key_column": "key",
                                             "key_regex": r"K-\d{2}", "columns": ["key", "sha", "class"],
                                             "class_column": "class", "comparators": {"sha": "sha_prefix"}},
                                "tracker": {"kind": "text", "tool": "linear_update_issue", "issue": "T-1",
                                            "key_regex": r"K-\d{2}", "groups": [["late", "late"]]},
                                "slide": {"kind": "json_text", "tool": "gslides_batch_update"}},
               "slots": [{"id": "S1", "weight": 5, "selector": ["field", "K-01", "sha"]},
                         {"id": "S2", "weight": 3, "selector": ["field", "K-02", "class"]},
                         {"id": "S3", "weight": 3, "selector": ["total", "HOLD"]},
                         {"id": "S4", "weight": 3, "selector": ["group_count", "late"]},
                         {"id": "S5", "weight": 1, "selector": ["delivery", "slide_updated"]},
                         {"id": "S6", "weight": 1, "selector": ["field", "K-02", "sha"], "gradable": False}]}
    truth = {"K-01": {"sha": "abcdef1234567890abcdef1234567890abcdef12", "class": "HOLD", "groups": ["late"]},
             "K-02": {"sha": None, "class": "READY", "groups": []}}
    csv_text = "key,sha,class\nK-01,abcdef1,HOLD\nK-02,missing,READY\n"

    def use(i, name, inp):
        return {"type": "assistant", "message": {"model": "claude-opus-4-8", "content": [
            {"type": "tool_use", "id": f"t{i}", "name": name, "input": inp}]}}

    def res(i, content):
        return {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": f"t{i}",
                                                         "content": json.dumps(content)}]}}
    ev = [{"type": "system", "subtype": "init", "model": "claude-opus-4-8"},
          use(1, "mcp__hg__gdrive_create_file", {"name": "register.csv", "content": base64.b64encode(csv_text.encode()).decode()}),
          res(1, {"id": "f1"}),
          use(2, "mcp__hg__linear_update_issue", {"id": "T-1", "patch": json.dumps([{"op": "append", "text": "late (1): K-01"}])}),
          res(2, {"id": "T-1"}),
          {"type": "result", "subtype": "success", "is_error": False}]
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("surface_grader_selftest_") as tmp:
        paths = []
        for i in range(1, 7):
            p = Path(tmp) / f"trajectory-run-{i}.json"
            e = json.loads(json.dumps(ev))
            if i % 2 == 0:   # even runs also update a slide; odd runs write a wrong class for K-02
                e.insert(-1, use(3, "mcp__hg__gslides_batch_update", {"presentationId": "p", "requests": []}))
                e.insert(-1, res(3, {"ok": True}))
            else:
                e[1]["message"]["content"][0]["input"]["content"] = base64.b64encode(
                    csv_text.replace("K-02,missing,READY", "K-02,missing,HOLD").encode()).decode()
            p.write_text(json.dumps(e))
            paths.append((f"run-{i}", p))
        rep = grade_runs(surface, truth, paths, None, "both")
        r1, r2 = rep["runs"]["run-1"], rep["runs"]["run-2"]
        assert r2["failed_slots"] == [] and r2["ungraded"] == ["S6"], r2   # SHA prefix matches; 'missing' accepted
        assert sorted(r1["failed_slots"]) == ["S2", "S3", "S5"], r1["failed_slots"]
        assert rep["coverage"] == {"graded_weight": 15, "total_weight": 16, "share": 0.9375}, rep["coverage"]
        assert r1["tracker_groups"] == {"late": [1, 1]}, r1["tracker_groups"]
        g2, g3 = rep["gates"]["V2"], rep["gates"]["V3"]
        pt = g2["difficulty_gates"]["pass_at_1"]
        assert pt["verdict"].startswith("PASS") and pt["value"]["ungraded_failed"].startswith("0/6") \
            and pt["value"]["ungraded_passed"].startswith("3/6"), g2     # both bounds pass the < 5 full passes rule
        assert g3["provenance_gates"]["baseline_models"]["verdict"].startswith("FAIL"), g3   # Opus 4.8 is not V3 evidence
        assert compare_reference(rep, {"run-1": {"results": dict(r1["results"], S1=False)}})[0]["slot"] == "S1"
    assert compare("PR #561", "match3d#561", "PR", {"comparators": {"PR": "pr_number"}}) == "MATCH"
    assert compare("active", "yes", "hold", {"comparators": {"hold": "yes_no"}}) == "MATCH"
    assert compare("ZOM-8021", "ZOM-802", "issue", {"comparators": {"issue": "issue_key"}}) == "DIFFERENT"
    assert compare("abc", "abcdef", "x", {"comparators": {"x": "sha_prefix"}}) == "DIFFERENT"   # under 7 characters
    assert tracker_groups("Billing hold active (2):\nSP-001, SP-002\nReview: 1 SP-003",
                          {"groups": [["billing", "billing"], ["review", "review"]]}) == {
        "billing": (2, ["SP-001", "SP-002"]), "review": (1, ["SP-003"])}
    fixtures = 0
    for _, case in PLANTED_G1:
        fixtures = case() or fixtures
    print("self-test: ok (comparators incl. SHA prefixes and missing spellings, totals, tracker groups same-line and "
          "heading-then-keys, every slide update counts, UNGRADED + coverage, V2/V3 gates through difficulty_stats with "
          "provenance apart, reference comparison; G1: the eight decoder defects each planted (heading line, section "
          "body, plain text, every update, bullet key list, range prose, tool alias, SHA prefix), unreadable register "
          "and tracker UNGRADED, UNGRADED gates by bounds and completions (INCOMPLETE), "
          f"{fixtures} Season Pass run formats re-graded slot for slot)")


# ------------------------------------------------------------------ main

def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="surface_grader.py", description="grade trajectories on the gradable surface")
    ap.add_argument("--task-dir", type=Path)
    ap.add_argument("--surface", type=Path)
    ap.add_argument("--truth", type=Path)
    ap.add_argument("--solver", type=Path)
    ap.add_argument("--oracle-dir", type=Path)
    ap.add_argument("--sql", type=Path)
    ap.add_argument("--run", action="append", default=[])
    ap.add_argument("--views", choices=("auto", "v2", "v3", "both"), default="auto")
    ap.add_argument("--compare", type=Path, help="reference grading JSON ({label: {results, score, ...}})")
    ap.add_argument("--official", type=Path, help="12_difficulty_input.json to compare slot by slot")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        _self_test()
        return 0
    surface_path = a.surface or (a.task_dir / "Working_Files" / "01_Gradable_Surface.json" if a.task_dir else None)
    if not surface_path or not surface_path.is_file():
        print("surface_grader: no surface (give --surface or --task-dir with Working_Files/01_Gradable_Surface.json)",
              file=sys.stderr)
        return 2
    surface = gs.load(surface_path)
    sql = a.sql or (a.task_dir / "01_Universe_Inject.sql" if a.task_dir else None)
    truth_default = a.task_dir / "Working_Files" / "solver" / "truth.json" if a.task_dir else None
    truth, tprov = load_truth(a.truth or (truth_default if not (a.solver or a.oracle_dir) and truth_default
                                          and truth_default.is_file() else None), a.solver, a.oracle_dir, sql)
    runs = tl._pairs(a.run) or (tl.task_runs(a.task_dir) if a.task_dir else [])
    if not runs:
        print("surface_grader: no runs", file=sys.stderr)
        return 2
    context = task_context(a.task_dir)
    report = grade_runs(surface, truth, runs, context, a.views)
    report.update(surface=tl._rel(surface_path), surface_sha256=tl.sha256_file(surface_path), truth=tprov,
                  context={k: (context or {}).get(k) for k in ("spec_version", "difficulty_mode", "task_type",
                                                              "baseline_model", "context_hash")} if context else None)
    rc = 0
    if a.compare:
        diffs = compare_reference(report, json.loads(a.compare.read_text()))
        report["reference_comparison"] = {"reference": tl._rel(a.compare), "sha256": tl.sha256_file(a.compare),
                                          "differences": diffs}
        rc = 1 if diffs else 0
    if a.official:
        report["official_comparison"] = {"matrix": tl._rel(a.official),
                                         "differences": compare_official(report, json.loads(a.official.read_text()))}
    if a.out:
        out = tl.safe_out(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n")
    if a.json:
        print(json.dumps(report, indent=1, ensure_ascii=False))
    else:
        print(to_text(report))
        if a.compare:
            n = len(report["reference_comparison"]["differences"])
            print(f"  reference comparison ({a.compare.name}): {n} difference(s)")
            for x in report["reference_comparison"]["differences"][:10]:
                print(f"    - {x}")
        if a.out:
            print(f"wrote {tl._rel(a.out)}")
    return rc


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"surface_grader: {error}", file=sys.stderr)
        raise SystemExit(2)

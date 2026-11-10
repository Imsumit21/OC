#!/usr/bin/env python3
"""rubric_skeleton.py - the rubric's shape (rows and weights, never wording) before the pre-check.

Why (plan RC3, WS3). A task's difficulty is designed on the gradable surface (a few dozen slots) and graded on the
final rubric (70-200 rows). The platform's rubric rules add rows every run passes, so the share of weight the planned
misses carry shrinks after the design is fixed. This tool expands the surface into the rows the platform rules will
force, before the pre-check, so the budget is checked on that shape; and after the rubric is final it compares the
real rubric with the skeleton.

Inputs (found the way stage_gate.slot_path finds them):
  Working_Files/01_Gradable_Surface.json   slots (gradable_surface.py owns the format and the 1/3/5 bands)
  Working_Files/01_Hardness_Manifest.json  the `writes` block (the .draft.json is read when the final is absent)
  Working_Files/01_Difficulty_Budget.json  units (optional for build; needed for check, rebase and drift)
  Working_Files/solver/truth.json          cohort keys and groups (optional)
  09_Rubrics.json                          drift only: rows R1.. in file order, each with `weight`
Output: Working_Files/01_Rubric_Skeleton.json (schema rubric-skeleton-v1), bound by sha256 to the four inputs.

Expansion rules (the tests this tool applies; each is a rule of thumb, see the backtest):
  slot rows      one row per surface slot, weight = the band of its work kind (gradable_surface.WORK_BANDS).
  atomic rows    a slot that checks two facts becomes two rows. A slot is read as several facts only on an explicit
                 signal: `atoms: N` on the slot; a tracker_entry selector with N value patterns; a groups_of selector
                 (one row per group the truth lists for the key); a text regex made of top-level lookaheads (each
                 conjunct after the first, which locates the line, is one fact). Every atomic row keeps the slot's
                 work kind, weight and units.
  write targets  each manifest `writes` entry is split on `+`. Sheets, Docs and Slides tools write one artifact: their
                 cells keep the table spot-check rule (at most five samples and a volume row), so they add no rows.
                 Every other tool writes separate targets: `count` separate writes need `count` rows. Slots already
                 graded on that tool count as the targets they name (an issue key, a truth key or a delivery argument
                 in the selector or title; a slot naming none counts as one target of its own). The missing targets
                 become rows. A write with count 1 adds none: its content rows also prove the write.
  one template   a group of N writes stays sampled (its sample slots plus one volume row) instead of N rows only when
                 (a) the manifest write entry says `"template": true`, or (b) the entry has two or more sample slots in
                 one group whose selectors are identical once the target's own id is masked and the masked selector
                 still holds a literal value (the template's content), e.g. `(ENG-1)...Done` and `(ENG-2)...Done`.
                 Anything else is N rows.
  added weights  an added write row is `interpretation` (3): it applies that target's decision to its own write. It is
                 `lookup` (1) when the write follows one template or only shares or moves a file.
  units          a row lists the budget units whose miss fails it: units whose `mechanism` is among the slot's
                 `mechanisms`, plus units whose own `rows` name the slot (basis `surface`) or the row (basis
                 `skeleton`). Realism units carry no budget weight and are left out. Added write rows start with no
                 unit: they are always-pass until the budget names them on the skeleton basis (`rebase`).

Checks:
  skeleton.present  the skeleton file exists
  skeleton.bound    its sha256 bindings equal the current surface, manifest, budget and truth
  skeleton.share    after expansion the anchors still carry mode loss + anchor margin (FAIL below it); WARN when the
                    coin-flip share is more than five points under the share the budget declared; prints the
                    always-pass share
  skeleton.drift    on the final rubric: FAIL when the anchors' share is below the mode loss; WARN when a unit's share
                    moved by more than five points or the always-pass share grew

Usage:
  python3.12 -B Task_Authoring/tools/rubric_skeleton.py build  --task-dir T [--write] [--json]
  python3.12 -B Task_Authoring/tools/rubric_skeleton.py check  --task-dir T [--json]
  python3.12 -B Task_Authoring/tools/rubric_skeleton.py rebase --task-dir T          (prints only)
  python3.12 -B Task_Authoring/tools/rubric_skeleton.py drift  --task-dir T [--json]
  python3.12 -B Task_Authoring/tools/rubric_skeleton.py backtest [--archives DIR] [--json]
  python3.12 -B Task_Authoring/tools/rubric_skeleton.py --self-test
Exit 0 = PASS or WARN, 1 = FAIL, 2 = usage error. Read-only on its inputs, stdlib only, never executes SQL.
"""
from __future__ import annotations

import argparse
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

TOOL = "rubric_skeleton"
VERSION = 1
SCHEMA = "rubric-skeleton-v1"
TITLE = "RUBRIC SKELETON"
POLICY = BUNDLE / "references" / "first_pass_policy.json"
ARCHIVES = BUNDLE / "support" / "completed_tasks"

SURFACE = "01_Gradable_Surface.json"
MANIFEST = "01_Hardness_Manifest.json"
MANIFEST_DRAFT = "01_Hardness_Manifest.draft.json"
BUDGET = "01_Difficulty_Budget.json"
TRUTH = "solver/truth.json"
SKELETON = "01_Rubric_Skeleton.json"
RUBRIC = "09_Rubrics.json"
DIFFICULTY_INPUT = "12_difficulty_input.json"

# thresholds that are not in first_pass_policy.json (listed in the report so the lead can move them there)
SHARE_MOVE_WARN = 0.05          # five points: coin-flip share under the declared share; a unit's share moving in drift
SAMPLE_CAP = 5                  # samples kept for a one-template group (gradable_surface.SAMPLE_LIMIT)
ADDED_KIND = "interpretation"   # an added write row applies its target's decision (band 3)
TEMPLATE_KIND = "lookup"        # a one-template write row, a share or a move (band 1)
BACKTEST_CLOSER = 0.5           # "much closer": the skeleton closes at least half of the surface's gap to the rubric

ARTIFACT_PREFIXES = ("gsheets_", "gdocs_", "gslides_")
PLAIN_TOOLS = ("gdrive_share_file", "gdrive_move_file", "gdrive_copy_file", "gdrive_create_folder")
TOOL_ALIASES = {"slack_post_message": "slack_send_message", "slack_reply_to_thread": "slack_send_message",
                "trello_add_comment_to_card": "trello_add_comment"}
DELIVERY_TOOL = {"register_parent": "gdrive_move_file", "share_reader": "gdrive_share_file",
                 "slack_thread": "slack_send_message", "slack_channel_post": "slack_send_message",
                 "slack_after_email": "slack_send_message", "email_reply": "gmail_reply_to_message",
                 "trello_card": "trello_create_card", "tracker_state": "linear_update_issue",
                 "tracker_preserves": "linear_update_issue", "slide_updated": "gslides_batch_update"}
BUILTIN_DELIVERABLE_TOOL = {"slide": "gslides_batch_update", "tracker": "linear_update_issue",
                            "email": "gmail_reply_to_message", "slack": "slack_send_message"}
RX_KEY = re.compile(r"\b[A-Z][A-Z0-9]{1,9}-\d+\b")
BUDGET_ROLES = ("anchor", "variance")


class UsageError(Exception):
    """A missing or unreadable input, or a bad argument (exit 2)."""


# ------------------------------------------------------------------ small helpers

def _gs():
    import gradable_surface
    return gradable_surface


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


def _share(part, total) -> float:
    return round(part / total, 4) if total else 0.0


def _pct(x) -> str:
    return f"{100.0 * (x or 0.0):.1f}%"


def _check(checks: list, cid: str, status: str, detail: str) -> None:
    checks.append({"id": cid, "status": status, "detail": detail})


def _verdict(checks: list) -> str:
    statuses = {c["status"] for c in checks}
    return "FAIL" if "FAIL" in statuses else ("WARN" if "WARN" in statuses else "PASS")


def load_policy(path: Path | None = None) -> dict:
    return _read_json(path or POLICY, "the first-pass policy")


def atomic_write(path: Path, text: str, what: str = "the rubric skeleton") -> None:
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


# ------------------------------------------------------------------ inputs

def find_inputs(task_dir) -> dict:
    """{name: Path or None} for the surface, manifest, budget, truth, skeleton and rubric of a task folder."""
    td = Path(task_dir)
    out = {}
    for key, name in (("surface", SURFACE), ("manifest", MANIFEST), ("budget", BUDGET), ("truth", TRUTH),
                      ("skeleton", SKELETON), ("rubric", RUBRIC)):
        p = _slot_path(td, name)
        out[key] = p if p.is_file() else None
    if out["manifest"] is None:
        draft = _slot_path(td, MANIFEST_DRAFT)
        out["manifest"] = draft if draft.is_file() else None
    return out


def bindings(task_dir, inputs: dict) -> dict:
    """{relative path: sha256} for the four files the skeleton is derived from (those that exist)."""
    out = {}
    for key in ("surface", "manifest", "budget", "truth"):
        p = inputs.get(key)
        if p is not None:
            out[_rel(Path(task_dir), p)] = sha256_file(p)
    return dict(sorted(out.items()))


def budget_units(budget: dict | None) -> list:
    """The anchor and variance units of a budget (realism units carry no budget weight)."""
    out = []
    for u in (budget or {}).get("units") or []:
        if isinstance(u, dict) and u.get("id") and u.get("role") in BUDGET_ROLES:
            out.append(u)
    return out


def _mechanisms(value) -> list:
    if isinstance(value, str):
        return [value] if value else []
    if isinstance(value, list):
        return [str(x) for x in value if x]
    return []


# ------------------------------------------------------------------ expansion

def tool_parts(tool) -> list:
    """`a+b (note)` -> [a, b], with known aliases folded."""
    out = []
    for part in str(tool or "").split("+"):
        m = re.match(r"\s*([A-Za-z0-9_]+)", part)
        if m:
            name = TOOL_ALIASES.get(m.group(1), m.group(1))
            if name not in out:
                out.append(name)
    return out


def is_artifact_tool(tool: str) -> bool:
    return tool.startswith(ARTIFACT_PREFIXES)


def slot_tool(slot: dict, surface: dict) -> tuple:
    """(tool, deliverable) a slot is graded on. tool is None for a table cell, a total or anything on a sheet."""
    sel = slot.get("selector")
    if not isinstance(sel, list) or not sel:
        return None, None
    kind = sel[0]
    deliverables = surface.get("deliverables") or {}
    if kind in ("text", "link") and len(sel) > 1:
        d = deliverables.get(sel[1])
        if isinstance(d, dict):
            if d.get("kind") == "table":
                return None, sel[1]
            tool = d.get("tool")
            return (TOOL_ALIASES.get(tool, tool) if tool else None), sel[1]
        return BUILTIN_DELIVERABLE_TOOL.get(sel[1]), sel[1]
    if kind in ("tracker_lists", "tracker_count", "tracker_entry"):
        for name, d in deliverables.items():
            if isinstance(d, dict) and d.get("kind") == "text":
                return TOOL_ALIASES.get(d.get("tool"), d.get("tool")), name
        return "linear_update_issue", "tracker"
    if kind == "delivery" and len(sel) > 1:
        return DELIVERY_TOOL.get(sel[1]), None
    if kind in ("field", "total", "printed_total", "group_count", "group_size", "group_key", "groups_of",
                "sole_reason", "reason_matches"):
        gs = _gs()
        name, _ = gs.table_deliverable(surface)
        return None, name
    return None, None


def target_token(slot: dict, truth_keys: list):
    """The write target a slot names: a delivery argument, an issue key, else a truth key; None when it names none."""
    sel = slot.get("selector")
    if not isinstance(sel, list):
        return None
    if sel and sel[0] == "delivery" and len(sel) > 2 and isinstance(sel[2], (str, int)):
        return str(sel[2])
    texts = [str(x) for x in sel[1:] if isinstance(x, (str, int))] + [str(slot.get("title") or "")]
    for t in texts:
        m = RX_KEY.search(t)
        if m:
            return m.group(0)
    low = " ".join(texts).casefold()
    for k in truth_keys:
        if len(k) >= 4 and k.casefold() in low:
            return k
    return None


def masked_selector(slot: dict, truth_keys: list) -> str:
    """The selector with the target's own id masked (issue keys and truth keys), for the one-template test."""
    s = json.dumps(slot.get("selector"), ensure_ascii=False)
    s = RX_KEY.sub("<ID>", s)
    for k in truth_keys:
        if len(k) >= 4:
            s = re.sub(re.escape(k), "<ID>", s, flags=re.I)
            s = re.sub(re.escape(re.escape(k)), "<ID>", s, flags=re.I)
    return s


def _holds_literal(slot: dict, truth_keys: list) -> bool:
    """True when the masked selector still names a value: a literal run of three or more letters or digits outside
    character classes, quantifiers and escapes. `(ENG-1)...Done` does; a bare `["link", "moves"]` does not."""
    sel = slot.get("selector")
    if not isinstance(sel, list) or len(sel) < 3:
        return False
    body = " ".join(str(x) for x in sel[2:] if isinstance(x, (str, int)))
    body = RX_KEY.sub(" ", body)
    for k in truth_keys:
        if len(k) >= 4:
            body = re.sub(re.escape(k), " ", body, flags=re.I)
    body = re.sub(r"\\u[0-9a-fA-F]{4}", " ", body)
    body = re.sub(r"\[(?:\\.|[^\]\\])*\]", " ", body)       # character classes
    body = re.sub(r"\{\d*,?\d*\}", " ", body)               # quantifiers
    body = re.sub(r"\\[A-Za-z]", " ", body)                 # \b \d \s ...
    return re.search(r"[A-Za-z0-9]{3,}", body) is not None


def atoms(slot: dict, truth: dict | None, surface: dict) -> tuple:
    """(number of atomic rows, the signal read) for one slot. 1 when no explicit signal says it checks two facts."""
    declared = slot.get("atoms")
    if isinstance(declared, int) and not isinstance(declared, bool) and declared >= 2:
        return declared, "atoms"
    sel = slot.get("selector")
    if not isinstance(sel, list) or not sel:
        return 1, None
    kind = sel[0]
    if kind == "tracker_entry" and len(sel) > 3 and isinstance(sel[3], list) and len(sel[3]) >= 2:
        return len(sel[3]), "tracker_entry values"
    if kind == "groups_of" and len(sel) > 1 and isinstance(truth, dict):
        gf = (surface.get("truth_fields") or {}).get("groups") or "groups"
        groups = (truth.get(sel[1]) or {}).get(gf) if isinstance(truth.get(sel[1]), dict) else None
        if isinstance(groups, list) and len(groups) >= 2:
            return len(groups), "groups_of"
    if kind in ("text", "reason_matches") and len(sel) > 2 and isinstance(sel[2], str):
        rx = sel[2]
        looks = _top_level_lookaheads(rx)
        if looks["count"] >= 2:
            conjuncts = looks["count"] + (1 if looks["tail"] else 0)
            if conjuncts - 1 >= 2:
                return conjuncts - 1, "regex lookaheads"
    return 1, None


def _top_level_lookaheads(rx: str) -> dict:
    """Count `(?=` groups at nesting depth 0 and say whether a consuming pattern follows the last one."""
    depth, i, count, last_end = 0, 0, 0, 0
    in_look = []
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
            if depth == 0 and rx.startswith("(?=", i):
                count += 1
                in_look.append(True)
            else:
                in_look.append(False)
            depth += 1
        elif ch == ")":
            depth -= 1
            was_look = in_look.pop() if in_look else False
            if depth == 0 and was_look:
                last_end = i + 1
        i += 1
    tail = rx[last_end:] if count else ""
    return {"count": count, "tail": bool(re.search(r"[A-Za-z0-9]{2,}", re.sub(r"\[(?:\\.|[^\]\\])*\]", "", tail)))}


def _truth_keys(surface: dict, truth: dict | None) -> list:
    keys = set(str(k) for k in (surface.get("truth_keys") or []))
    if isinstance(truth, dict):
        keys.update(str(k) for k in truth)
    return sorted(keys, key=lambda k: (-len(k), k))


def _population(count: int, truth: dict | None, surface: dict):
    """The truth population whose size equals a write count (all keys, or one group): a hint, never a rule."""
    if not isinstance(truth, dict) or count <= 1:
        return None
    gf = (surface.get("truth_fields") or {}).get("groups") or "groups"
    sizes = collections.Counter()
    for v in truth.values():
        if isinstance(v, dict):
            for g in v.get(gf) or []:
                sizes[str(g)] += 1
    hits = sorted(g for g, n in sizes.items() if n == count)
    if len(hits) == 1:
        return f"group {hits[0]}"
    if not hits and len(truth) == count:
        return "all truth keys"
    return None


def build_rows(surface: dict, manifest: dict | None, budget: dict | None, truth: dict | None) -> dict:
    """The skeleton rows and the per-write accounting. Pure: no file is read or written."""
    gs = _gs()
    slots = [s for s in surface.get("slots") or [] if isinstance(s, dict)]
    tkeys = _truth_keys(surface, truth)
    basis = (budget or {}).get("weight_basis") or "surface"
    units = budget_units(budget)
    by_mech, by_row = collections.defaultdict(list), collections.defaultdict(list)
    for u in units:
        for m in _mechanisms(u.get("mechanism")):
            by_mech[m].append(u["id"])
        for r in u.get("rows") or []:
            if isinstance(r, dict) and r.get("id"):
                by_row[str(r["id"])].append(u["id"])

    rows, notes = [], []

    def add(slot_id, kind, weight, write_target, source, mechanisms=(), extra_units=()):
        rid = f"S{len(rows) + 1}"
        found = set(extra_units)
        for m in mechanisms:
            found.update(by_mech.get(m, []))
        if basis == "skeleton":
            found.update(by_row.get(rid, []))
        row = {"id": rid, "slot": slot_id, "kind": kind, "weight": weight, "source": source,
               "units": sorted(found)}
        if write_target:
            row["write_target"] = write_target
        if mechanisms:
            row["mechanisms"] = list(mechanisms)
        rows.append(row)
        return row

    slot_meta = {}
    for s in slots:
        sid = str(s.get("id"))
        kind = s.get("work_kind")
        band = gs.WORK_BANDS.get(kind)
        weight = band if band is not None else s.get("weight")
        if band is None:
            notes.append(f"slot {sid}: work kind {kind!r} is not a known kind; its own weight {s.get('weight')!r} is kept")
        elif s.get("weight") != band:
            notes.append(f"slot {sid}: weight {s.get('weight')!r} but work kind {kind} is band {band}; the band is used")
        if weight not in (1, 3, 5):
            notes.append(f"slot {sid}: weight {weight!r} is not 1, 3 or 5; counted as 1")
            weight = 1
        tool, deliverable = slot_tool(s, surface)
        token = target_token(s, tkeys)
        if tool:
            target = f"{tool}:{token or deliverable or sid}"
        else:
            target = f"table:{deliverable}" if deliverable else None
        n, signal = atoms(s, truth, surface)
        mech = _mechanisms(s.get("mechanisms"))
        own = by_row.get(sid, []) if basis == "surface" else []
        made = []
        for i in range(n):
            made.append(add(sid, kind, weight, target, "slot" if i == 0 else f"atomic ({signal})", mech, own)["id"])
        slot_meta[sid] = {"tool": tool, "token": token, "role": gs.role(s), "group": s.get("group"), "rows": made,
                          "slot": s}

    writes = []
    for i, w in enumerate((manifest or {}).get("writes") or []):
        if not isinstance(w, dict):
            continue
        parts = tool_parts(w.get("tool"))
        count = w.get("count") if isinstance(w.get("count"), int) and not isinstance(w.get("count"), bool) else 0
        entry = {"index": i, "tool": w.get("tool"), "tools": parts, "count": count, "added_rows": []}
        target_parts = [p for p in parts if not is_artifact_tool(p)]
        on_entry = [sid for sid, m in slot_meta.items() if m["tool"] in parts]
        entry["slots"] = on_entry
        if not target_parts:
            entry.update(kind="artifact", rule="one artifact: its cells keep the table spot-check rule; no row added")
            writes.append(entry)
            continue
        entry["kind"] = "targets"
        hint = _population(count, truth, surface)
        if hint:
            entry["population"] = hint
        label = "+".join(target_parts)
        plain = all(p in PLAIN_TOOLS for p in target_parts)
        if count <= 1:
            entry["rule"] = "one write: its content rows also prove the write; no row added"
            writes.append(entry)
            continue
        # the one-template test
        groups = collections.defaultdict(list)
        for sid in on_entry:
            m = slot_meta[sid]
            if m["role"] == "sample" and m["group"]:
                groups[m["group"]].append(sid)
        template_group = None
        for g, members in sorted(groups.items()):
            if len(members) < 2:
                continue
            masks = {masked_selector(slot_meta[sid]["slot"], tkeys) for sid in members}
            if len(masks) == 1 and all(_holds_literal(slot_meta[sid]["slot"], tkeys) for sid in members):
                template_group = g
                break
        declared = w.get("template") is True
        if declared or template_group:
            entry["template"] = True
            entry["template_basis"] = ("the manifest write entry declares one template" if declared else
                                       f"sample group {template_group}: the selectors are identical once the target "
                                       "id is masked, and they hold a literal value")
            graded = [sid for sid in on_entry if slot_meta[sid]["role"] != "volume"]
            if not graded:      # nothing grades the template yet: up to five samples stand for it
                for k in range(min(count, SAMPLE_CAP)):
                    entry["added_rows"].append(add(None, TEMPLATE_KIND, gs.WORK_BANDS[TEMPLATE_KIND],
                                                   f"{label}#sample{k + 1}", "write sample (one template)")["id"])
            covered = False
            for s in slots:
                if gs.role(s) != "volume":
                    continue
                vf = [str(v) for v in s.get("volume_for") or []]
                if slot_meta[str(s.get("id"))]["tool"] in parts or (template_group and template_group in vf):
                    covered = True
            if not covered:
                entry["added_rows"].append(add(None, TEMPLATE_KIND, gs.WORK_BANDS[TEMPLATE_KIND], f"{label}#volume",
                                               "write volume (one template)")["id"])
            entry["rule"] = "all follow one template: samples plus one volume row"
            writes.append(entry)
            continue
        entry["template"] = False
        named = set()
        for sid in on_entry:
            m = slot_meta[sid]
            if m["role"] == "volume":
                continue
            named.add(m["token"] or f"slot:{sid}")
        covered = min(len(named), count)
        entry["targets_named_by_slots"] = covered
        kind = TEMPLATE_KIND if plain else ADDED_KIND
        for k in range(count - covered):
            entry["added_rows"].append(add(None, kind, gs.WORK_BANDS[kind], f"{label}#{covered + k + 1}",
                                           "write target (one row per separate write)")["id"])
        entry["rule"] = (f"{count} separate writes, {covered} named by slots: {count - covered} row(s) added at "
                         f"{kind} ({gs.WORK_BANDS[kind]})")
        writes.append(entry)

    if basis == "skeleton":
        known = {r["id"] for r in rows}
        for rid in sorted(by_row):
            if rid not in known:
                notes.append(f"budget row {rid} is not a skeleton row id (units {sorted(set(by_row[rid]))})")
    elif basis == "surface":
        known = set(slot_meta)
        for rid in sorted(by_row):
            if rid not in known:
                notes.append(f"budget row {rid} is not a surface slot id (units {sorted(set(by_row[rid]))})")
    return {"rows": rows, "writes": writes, "notes": notes}


def totals(rows: list, budget: dict | None, surface: dict | None = None) -> dict:
    """Total weight, per-unit weight and share, anchor, coin-flip and always-pass weight and share."""
    total = sum(r["weight"] for r in rows)
    units = budget_units(budget)
    roles = {u["id"]: u.get("role") for u in units}
    per_unit = {}
    for u in units:
        mine = [r for r in rows if u["id"] in r["units"]]
        w = sum(r["weight"] for r in mine)
        per_unit[u["id"]] = {"role": u.get("role"), "rows": [r["id"] for r in mine], "weight": w,
                             "share": _share(w, total)}
    anchor_w = sum(r["weight"] for r in rows if any(roles.get(u) == "anchor" for u in r["units"]))
    coin_w = sum(r["weight"] for r in rows if any(roles.get(u) == "variance" for u in r["units"])
                 and not any(roles.get(u) == "anchor" for u in r["units"]))
    if units:
        always = sum(r["weight"] for r in rows if not r["units"])
        basis = "units"
    else:
        always = sum(r["weight"] for r in rows if not r.get("mechanisms"))
        basis = "mechanisms"
    out = {"rows": len(rows), "total_weight": total, "per_unit": per_unit,
           "anchor_weight": anchor_w, "anchor_share": _share(anchor_w, total),
           "coin_flip_weight": coin_w, "coin_flip_share": _share(coin_w, total),
           "always_pass_weight": always, "always_pass_share": _share(always, total),
           "always_pass_basis": ("rows no anchor or variance unit flips" if basis == "units" else
                                 "no budget: rows no surface mechanism flips"),
           "added_rows": sum(1 for r in rows if r["slot"] is None),
           "added_weight": sum(r["weight"] for r in rows if r["slot"] is None)}
    if surface is not None:
        slots = [s for s in surface.get("slots") or [] if isinstance(s, dict)]
        out["surface_slots"] = len(slots)
        out["surface_weight"] = sum(s.get("weight") or 0 for s in slots if isinstance(s.get("weight"), int))
    return out


def build(task_dir) -> dict:
    """Derive the skeleton of a task folder in memory. Raises UsageError when the surface or manifest is missing."""
    td = Path(task_dir)
    if not td.is_dir():
        raise UsageError(f"task folder {td} does not exist")
    inputs = find_inputs(td)
    if inputs["surface"] is None:
        raise UsageError(f"no {SURFACE} in {td}: /create-scenario writes it")
    if inputs["manifest"] is None:
        raise UsageError(f"no {MANIFEST} (or its draft) in {td}")
    try:
        surface = _gs().load(inputs["surface"])
    except (OSError, ValueError) as error:
        raise UsageError(f"cannot read the surface: {error}")
    manifest = _read_json(inputs["manifest"], "the manifest")
    budget = _read_json(inputs["budget"], "the budget") if inputs["budget"] else None
    truth = _read_json(inputs["truth"], "the solver truth") if inputs["truth"] else None
    if not isinstance(manifest, dict):
        raise UsageError(f"{inputs['manifest']}: the manifest is not a JSON object")
    if budget is not None and not isinstance(budget, dict):
        raise UsageError(f"{inputs['budget']}: the budget is not a JSON object")
    built = build_rows(surface, manifest, budget, truth if isinstance(truth, dict) else None)
    doc = {"schema": SCHEMA, "tool": TOOL, "version": VERSION,
           "task": surface.get("task"), "surface_revision": surface.get("revision"),
           "design_id": (budget or {}).get("design_id"), "budget_revision": (budget or {}).get("revision"),
           "mode": (budget or {}).get("mode"), "budget_weight_basis": (budget or {}).get("weight_basis"),
           "bound_to": bindings(td, inputs),
           "inputs": {k: (_rel(td, v) if v else None) for k, v in sorted(inputs.items())
                      if k in ("surface", "manifest", "budget", "truth")},
           "rules": {"rows": "one row per slot; explicit atomic splits; one row per separate write target unless all "
                             "follow one template; sheet, doc and slide cells keep the table spot-check rule",
                     "weights": "1/3/5 by kind of work (gradable_surface.WORK_BANDS); added write rows "
                                f"{ADDED_KIND}, one-template, share and move rows {TEMPLATE_KIND}",
                     "wording": "none: rows and weights only"},
           "rows": built["rows"], "writes": built["writes"], "notes": built["notes"],
           "totals": totals(built["rows"], budget, surface)}
    return doc


def dump(doc: dict) -> str:
    return json.dumps(doc, indent=1, sort_keys=True, ensure_ascii=False) + "\n"


# ------------------------------------------------------------------ commands

def _result(command: str, checks: list, bound: dict, **extra) -> dict:
    out = {"tool": TOOL, "version": VERSION, "command": command, "verdict": _verdict(checks),
           "bound_to": bound, "checks": checks}
    out.update(extra)
    return out


def cmd_build(task_dir, write: bool = False) -> dict:
    doc = build(task_dir)
    t = doc["totals"]
    checks = []
    missing = [k for k in ("budget", "truth") if not doc["inputs"].get(k)]
    _check(checks, "skeleton.inputs", "WARN" if "budget" in missing else "PASS",
           "read " + ", ".join(v for v in doc["inputs"].values() if v) +
           (f"; missing {', '.join(missing)}" + ("; without a budget no row lists a unit" if "budget" in missing else "")
            if missing else ""))
    _check(checks, "skeleton.build", "PASS",
           f"{t['rows']} rows, weight {t['total_weight']} (surface: {t.get('surface_slots')} slots, weight "
           f"{t.get('surface_weight')}); {t['added_rows']} rows added for write targets, weight {t['added_weight']}; "
           f"always-pass {t['always_pass_weight']} ({_pct(t['always_pass_share'])}; {t['always_pass_basis']})")
    if doc["notes"]:
        _check(checks, "skeleton.notes", "WARN", "; ".join(doc["notes"][:6]) +
               (f"; and {len(doc['notes']) - 6} more" if len(doc["notes"]) > 6 else ""))
    written = None
    if write:
        path = _slot_path(Path(task_dir), SKELETON)
        atomic_write(path, dump(doc))
        written = _rel(Path(task_dir), path)
        _check(checks, "skeleton.written", "PASS", f"wrote {written}")
    return _result("build", checks, doc["bound_to"], skeleton=doc, written=written)


def declared_share(budget: dict, role: str):
    """The share of the budget's own total weight its units of one role declare (rows counted once)."""
    total = budget.get("total_weight")
    if not isinstance(total, (int, float)) or isinstance(total, bool) or total <= 0:
        return None
    seen, anchored = {}, set()
    for u in budget_units(budget):
        for r in u.get("rows") or []:
            if not (isinstance(r, dict) and r.get("id") and isinstance(r.get("weight"), (int, float))):
                continue
            if u.get("role") == "anchor":
                anchored.add(str(r["id"]))
            if u.get("role") == role:
                seen[str(r["id"])] = r["weight"]
    if role == "variance":      # a row an anchor also fails is lost anyway: it is anchor weight, as in totals()
        seen = {k: v for k, v in seen.items() if k not in anchored}
    return round(sum(seen.values()) / total, 4)


def cmd_check(task_dir, policy: dict | None = None) -> dict:
    td = Path(task_dir)
    policy = policy or load_policy()
    inputs = find_inputs(td)
    checks = []
    fresh = build(td)
    current = fresh["bound_to"]
    stored = None
    if inputs["skeleton"] is None:
        _check(checks, "skeleton.present", "FAIL", f"no {SKELETON}: run `rubric_skeleton.py build --task-dir "
               f"{td} --write` at the end of /create-injection")
    else:
        stored = _read_json(inputs["skeleton"], "the skeleton")
        if not isinstance(stored, dict) or stored.get("schema") != SCHEMA:
            _check(checks, "skeleton.present", "FAIL", f"{_rel(td, inputs['skeleton'])} is not a {SCHEMA} file: "
                   "rebuild it with build --write")
            stored = None
        else:
            _check(checks, "skeleton.present", "PASS", f"{_rel(td, inputs['skeleton'])}: "
                   f"{(stored.get('totals') or {}).get('rows')} rows")
    if stored is not None:
        was = stored.get("bound_to") or {}
        changed = sorted(k for k in set(was) | set(current) if was.get(k) != current.get(k))
        if changed:
            _check(checks, "skeleton.bound", "FAIL", "the skeleton was built from other bytes of " +
                   ", ".join(changed) + ": rebuild it with build --write")
        elif stored.get("rows") != fresh["rows"]:
            _check(checks, "skeleton.bound", "FAIL", "the inputs are unchanged but this tool now derives other rows: "
                   "rebuild the skeleton with build --write")
        else:
            _check(checks, "skeleton.bound", "PASS", f"bound to {len(current)} current input file(s)")
    else:
        _check(checks, "skeleton.bound", "SKIP", "no skeleton file to compare; shares below are from a fresh build")

    budget = _read_json(inputs["budget"], "the budget") if inputs["budget"] else None
    t = fresh["totals"]
    extra = {"totals": t}
    if not budget or not budget_units(budget):
        _check(checks, "skeleton.share", "SKIP", f"no {BUDGET} with anchor or variance units, so no share can be "
               f"checked; always-pass on the skeleton is {_pct(t['always_pass_share'])} ({t['always_pass_basis']})")
        return _result("check", checks, current, **extra)
    mode = str(budget.get("mode") or "").lower()
    b = policy.get("budget") or {}
    loss = (b.get("mode_loss") or {}).get(mode)
    margin = b.get("anchor_margin", 0.0)
    if loss is None:
        _check(checks, "skeleton.share", "FAIL", f"budget mode {budget.get('mode')!r} has no mode_loss in the policy "
               "(easy, medium or hard)")
        return _result("check", checks, current, **extra)
    need = round(loss + margin, 4)
    flippable = round(1.0 - t["always_pass_share"], 4)
    designed_anchor = declared_share(budget, "anchor")
    designed_coin = declared_share(budget, "variance")
    extra["thresholds"] = {"mode": mode, "mode_loss": loss, "anchor_margin": margin, "required_anchor_share": need,
                           "share_move_warn": SHARE_MOVE_WARN}
    extra["declared"] = {"anchor_share": designed_anchor, "coin_flip_share": designed_coin,
                         "weight_basis": budget.get("weight_basis"), "total_weight": budget.get("total_weight")}
    line = (f"anchors {t['anchor_weight']} of {t['total_weight']} = {_pct(t['anchor_share'])} (needs {_pct(need)}: "
            f"{mode} loss {_pct(loss)} + margin {_pct(margin)}); coin-flip {_pct(t['coin_flip_share'])}"
            + (f" (budget declared {_pct(designed_coin)})" if designed_coin is not None else "")
            + f"; always-pass {_pct(t['always_pass_share'])}")
    if flippable < need:
        _check(checks, "skeleton.share", "FAIL", line + f". Only {_pct(flippable)} of the weight can be lost at all, "
               "less than the anchors must carry: move misses onto more weight in the task, not in the rubric")
    elif t["anchor_share"] < need:
        _check(checks, "skeleton.share", "FAIL", line + ". After the write-target rows are added the anchors carry "
               "less than the mode needs: put an anchor on more rows of weight 5 or cut always-pass writes "
               "in the task design")
    elif designed_coin is not None and t["coin_flip_share"] < designed_coin - SHARE_MOVE_WARN:
        _check(checks, "skeleton.share", "WARN", line + ". The coin-flip share is more than five points under the "
               "design: the spread and failure-pattern gates were sized on the higher share")
    else:
        _check(checks, "skeleton.share", "PASS", line)
    return _result("check", checks, current, **extra)


def rebase(task_dir) -> dict:
    """The budget's rows re-expressed on the skeleton basis (for the author to paste). Reads only."""
    td = Path(task_dir)
    inputs = find_inputs(td)
    if inputs["budget"] is None:
        raise UsageError(f"no {BUDGET} in {td}: there are no unit rows to rebase")
    doc = build(td)
    budget = _read_json(inputs["budget"], "the budget")
    by_id = {r["id"]: r for r in doc["rows"]}
    units = []
    for u in (budget.get("units") or []):
        if not isinstance(u, dict) or not u.get("id"):
            continue
        if u.get("role") in BUDGET_ROLES:
            ids = doc["totals"]["per_unit"].get(u["id"], {}).get("rows", [])
            units.append({"id": u["id"], "rows": [{"id": i, "weight": by_id[i]["weight"]} for i in ids]})
        else:
            units.append({"id": u["id"], "rows": []})
    return {"weight_basis": "skeleton", "total_weight": doc["totals"]["total_weight"], "units": units}


def rubric_rows(path: Path) -> list:
    """[(R<n>, weight)] of a 09_Rubrics.json in file order."""
    data = _read_json(path, "the rubric")
    if isinstance(data, dict):
        data = data.get("rubrics") or data.get("criteria") or data.get("rows") or []
    if not isinstance(data, list):
        raise UsageError(f"{path}: the rubric is not a list of rows")
    out = []
    for i, row in enumerate(data, 1):
        w = row.get("weight") if isinstance(row, dict) else None
        if isinstance(w, bool) or not isinstance(w, (int, float)):
            raise UsageError(f"{path}: row R{i} has no numeric weight")
        out.append((f"R{i}", w))
    return out


def cmd_drift(task_dir, policy: dict | None = None) -> dict:
    td = Path(task_dir)
    policy = policy or load_policy()
    inputs = find_inputs(td)
    checks = []
    fresh = build(td)
    current = dict(fresh["bound_to"])
    budget = _read_json(inputs["budget"], "the budget") if inputs["budget"] else None
    if inputs["rubric"] is not None:
        current[_rel(td, inputs["rubric"])] = sha256_file(inputs["rubric"])
    rows = rubric_rows(inputs["rubric"]) if inputs["rubric"] is not None else []
    if not rows:
        _check(checks, "skeleton.drift", "SKIP", f"no rows in {RUBRIC} yet: run drift once the rubric is final")
        return _result("drift", checks, current)
    if not budget or not budget_units(budget):
        _check(checks, "skeleton.drift", "FAIL", f"no {BUDGET} with anchor or variance units: the rubric cannot be "
               "compared with the design")
        return _result("drift", checks, current)
    mapping = budget.get("rubric_rows")
    units = budget_units(budget)
    if not isinstance(mapping, dict) or not mapping:
        _check(checks, "skeleton.drift", "FAIL", "the budget has no `rubric_rows`: list the final rubric ids "
               "(R<n>, file order) each unit's miss fails, then run drift again")
        return _result("drift", checks, current)
    weights = dict(rows)
    total = sum(w for _, w in rows)
    stored = _read_json(inputs["skeleton"], "the skeleton") if inputs["skeleton"] else None
    before_src = "stored skeleton"
    if not isinstance(stored, dict) or stored.get("schema") != SCHEMA:
        stored, before_src = fresh, "fresh build (no stored skeleton)"
    elif (stored.get("bound_to") or {}) != fresh["bound_to"]:
        before_src = "stored skeleton (its inputs have changed since it was built)"
    before = stored.get("totals") or {}
    problems, table = [], []
    roles = {u["id"]: u.get("role") for u in units}
    flipped = {}
    for u in units:
        ids = mapping.get(u["id"])
        if not isinstance(ids, list) or not ids:
            problems.append(f"unit {u['id']} has no rubric_rows")
            ids = []
        unknown = sorted({str(i) for i in ids if str(i) not in weights})
        if unknown:
            problems.append(f"unit {u['id']} names rows the rubric does not have: {', '.join(unknown)}")
        mine = sorted({str(i) for i in ids if str(i) in weights}, key=lambda r: int(r[1:]))
        for rid in mine:
            flipped.setdefault(rid, set()).add(u["id"])
        w = sum(weights[r] for r in mine)
        b = (before.get("per_unit") or {}).get(u["id"]) or {}
        table.append({"unit": u["id"], "role": u.get("role"),
                      "skeleton_weight": b.get("weight"), "skeleton_share": b.get("share"),
                      "rubric_rows": mine, "rubric_weight": w, "rubric_share": _share(w, total),
                      "moved": (round(_share(w, total) - b["share"], 4) if isinstance(b.get("share"), (int, float))
                                else None)})
    anchor_w = sum(weights[r] for r, us in flipped.items() if any(roles[u] == "anchor" for u in us))
    coin_w = sum(weights[r] for r, us in flipped.items() if any(roles[u] == "variance" for u in us)
                 and not any(roles[u] == "anchor" for u in us))
    always_w = sum(w for r, w in rows if r not in flipped)
    after = {"rows": len(rows), "total_weight": total, "anchor_weight": anchor_w,
             "anchor_share": _share(anchor_w, total), "coin_flip_weight": coin_w,
             "coin_flip_share": _share(coin_w, total), "always_pass_weight": always_w,
             "always_pass_share": _share(always_w, total)}
    mode = str(budget.get("mode") or "").lower()
    loss = ((policy.get("budget") or {}).get("mode_loss") or {}).get(mode)
    extra = {"before": {k: before.get(k) for k in ("rows", "total_weight", "anchor_weight", "anchor_share",
                                                    "coin_flip_weight", "coin_flip_share", "always_pass_weight",
                                                    "always_pass_share")},
             "before_source": before_src, "after": after, "units": table,
             "thresholds": {"mode": mode, "mode_loss": loss, "share_move_warn": SHARE_MOVE_WARN}}
    head = (f"final rubric {after['rows']} rows, weight {total} (skeleton {before.get('rows')} rows, weight "
            f"{before.get('total_weight')}); anchors {_pct(after['anchor_share'])} (skeleton "
            f"{_pct(before.get('anchor_share'))}); coin-flip {_pct(after['coin_flip_share'])} (skeleton "
            f"{_pct(before.get('coin_flip_share'))}); always-pass {_pct(after['always_pass_share'])} (skeleton "
            f"{_pct(before.get('always_pass_share'))})")
    if problems:
        _check(checks, "skeleton.drift", "FAIL", head + ". Fix the budget's rubric_rows: " + "; ".join(problems))
    elif loss is None:
        _check(checks, "skeleton.drift", "FAIL", head + f". Budget mode {budget.get('mode')!r} has no mode_loss in "
               "the policy")
    elif after["anchor_share"] < loss:
        _check(checks, "skeleton.drift", "FAIL", head + f". The anchors carry less than the {mode} loss "
               f"{_pct(loss)} on the final rubric: the rubric has drifted over the cap. Change the task so the "
               "anchors fail more weight; do not tune rows")
    else:
        moved = [f"{r['unit']} {'+' if r['moved'] > 0 else ''}{100 * r['moved']:.1f} points"
                 for r in table if r["moved"] is not None and abs(r["moved"]) > SHARE_MOVE_WARN]
        grew = (isinstance(before.get("always_pass_share"), (int, float))
                and after["always_pass_share"] > before["always_pass_share"] + 1e-9)
        if moved or grew:
            why = []
            if moved:
                why.append("unit share moved by more than five points: " + ", ".join(moved))
            if grew:
                why.append(f"the always-pass share grew from {_pct(before['always_pass_share'])} to "
                           f"{_pct(after['always_pass_share'])}")
            _check(checks, "skeleton.drift", "WARN", head + ". " + "; ".join(why) +
                   ". Re-run the budget on the rubric basis before /create-difficulty")
        else:
            _check(checks, "skeleton.drift", "PASS", head)
    return _result("drift", checks, current, **extra)


def evaluate(task_dir, command: str = "check", policy: dict | None = None) -> dict:
    """The gate's entry point: `build` (in memory), `check` or `drift` for a task folder. Never writes."""
    if command == "build":
        return cmd_build(task_dir, write=False)
    if command == "check":
        return cmd_check(task_dir, policy)
    if command == "drift":
        return cmd_drift(task_dir, policy)
    raise UsageError(f"unknown command {command!r} (build, check or drift)")


# ------------------------------------------------------------------ backtest on the archived tasks

def final_always_pass(task_dir: Path, rows: list):
    """The weight share of final-rubric rows every completed baseline run passed (12_difficulty_input.json)."""
    p = _slot_path(task_dir, DIFFICULTY_INPUT)
    if not p.is_file():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    runs = [r for r in (data.get("rollouts") or []) if isinstance(r, dict) and isinstance(r.get("results"), dict)
            and r.get("results") and r.get("status", "completed") == "completed"]
    rub = [x for x in (data.get("rubrics") or []) if isinstance(x, dict) and x.get("id")]
    if not runs or not rub:
        return None
    total = sum(x.get("weight") or 0 for x in rub)
    always = sum(x.get("weight") or 0 for x in rub if all(r["results"].get(x["id"]) is True for r in runs))
    return {"share": _share(always, total), "runs": len(runs), "rows": len(rub),
            "same_rubric": len(rub) == len(rows) and total == sum(w for _, w in rows)}


def _gap_closed(surface_v, skeleton_v, final_v):
    gap = abs(final_v - surface_v)
    if gap == 0:
        return None
    return round(1.0 - abs(final_v - skeleton_v) / gap, 3)


def backtest(archives: Path | None = None) -> dict:
    """Build the skeleton of every archived task that has a surface, a manifest and a final rubric, and compare its
    row count and weight with the surface's and the final rubric's. Reads only."""
    root = Path(archives or ARCHIVES)
    gs = _gs()
    out, skipped = [], []
    for d in sorted(p for p in root.iterdir() if p.is_dir()):
        td = d / "task_inputs"
        if not td.is_dir():
            continue
        inputs = find_inputs(td)
        if inputs["surface"] is None or inputs["manifest"] is None or inputs["rubric"] is None:
            skipped.append({"archive": d.name, "why": "no surface, manifest or rubric"})
            continue
        try:
            rows = rubric_rows(inputs["rubric"])
            doc = build(td)
            surface = gs.load(inputs["surface"])
        except (UsageError, OSError, ValueError) as error:
            skipped.append({"archive": d.name, "why": str(error)})
            continue
        if not rows:
            skipped.append({"archive": d.name, "why": "the final rubric has no rows"})
            continue
        t = doc["totals"]
        slots = surface.get("slots") or []
        s_total = sum(s.get("weight") or 0 for s in slots)
        s_free = sum(s.get("weight") or 0 for s in slots if not (s.get("mechanisms") or s.get("flipped_by")))
        f_total = sum(w for _, w in rows)
        row = {"archive": d.name,
               "surface_slots": len(slots), "skeleton_rows": t["rows"], "final_rows": len(rows),
               "surface_weight": s_total, "skeleton_weight": t["total_weight"], "final_weight": f_total,
               "surface_always_pass": _share(s_free, s_total), "skeleton_always_pass": t["always_pass_share"],
               "final_always_pass": final_always_pass(td, rows),
               "rows_gap_closed": _gap_closed(len(slots), t["rows"], len(rows)),
               "weight_gap_closed": _gap_closed(s_total, t["total_weight"], f_total),
               "added_rows": t["added_rows"]}
        closed = [x for x in (row["rows_gap_closed"], row["weight_gap_closed"]) if x is not None]
        row["much_closer"] = bool(closed) and all(x >= BACKTEST_CLOSER for x in closed)
        out.append(row)
    return {"tool": TOOL, "version": VERSION, "command": "backtest", "archives": str(root), "rows": out,
            "skipped": skipped, "much_closer_rule": f"the skeleton closes at least {BACKTEST_CLOSER:.0%} of the "
            "surface's gap to the final rubric, in rows and in weight"}


def backtest_text(r: dict) -> str:
    lines = ["RUBRIC SKELETON (backtest): surface vs skeleton vs final rubric",
             f"{'archive':46} {'rows s/k/f':>14} {'weight s/k/f':>15} {'always-pass s/k/f':>22} {'gap closed r/w':>15} closer"]
    for x in r["rows"]:
        fa = x["final_always_pass"]
        fa_s = _pct(fa["share"]) + ("" if fa["same_rubric"] else "*") if fa else "n/a"

        def g(v):
            return "n/a" if v is None else f"{100 * v:.0f}%"
        lines.append(f"{x['archive'][:46]:46} {x['surface_slots']:>4}/{x['skeleton_rows']:>4}/{x['final_rows']:>4} "
                     f"{x['surface_weight']:>4}/{x['skeleton_weight']:>5}/{x['final_weight']:>4} "
                     f"{_pct(x['surface_always_pass']):>6}/{_pct(x['skeleton_always_pass']):>6}/{fa_s:>7} "
                     f"{g(x['rows_gap_closed']):>7}/{g(x['weight_gap_closed']):>6} "
                     f"{'yes' if x['much_closer'] else 'no'}")
    for x in r["skipped"]:
        lines.append(f"  skipped {x['archive']}: {x['why']}")
    lines.append("s = surface, k = skeleton, f = final rubric. Always-pass: surface and skeleton = weight no mechanism "
                 "flips; final = rows every baseline run passed (* = the baseline graded another rubric version).")
    lines.append(r["much_closer_rule"])
    return "\n".join(lines)


# ------------------------------------------------------------------ text output

def to_text(r: dict) -> str:
    lines = [f"{TITLE} ({r['command']}): {r['verdict']}"]
    for c in r["checks"]:
        lines.append(f"[{c['status']}] {c['id']}: {c['detail']}")
    if r["command"] == "build":
        for w in r["skeleton"]["writes"]:
            lines.append(f"  write {w['tool']} x{w['count']}: {w.get('rule')}")
        per = r["skeleton"]["totals"]["per_unit"]
        for uid in sorted(per):
            u = per[uid]
            lines.append(f"  unit {uid} ({u['role']}): weight {u['weight']} = {_pct(u['share'])} on rows "
                         f"{', '.join(u['rows']) or 'none'}")
    if r["command"] == "drift" and r.get("units"):
        lines.append(f"  {'unit':10} {'role':9} {'skeleton':>16} {'final rubric':>16} {'moved':>8}")
        for u in r["units"]:
            sk = (f"{u['skeleton_weight']} ({_pct(u['skeleton_share'])})" if u["skeleton_weight"] is not None
                  else "n/a")
            mv = f"{100 * u['moved']:+.1f}" if u["moved"] is not None else "n/a"
            lines.append(f"  {u['unit']:10} {str(u['role']):9} {sk:>16} "
                         f"{str(u['rubric_weight']) + ' (' + _pct(u['rubric_share']) + ')':>16} {mv:>8}")
        b, a = r["before"], r["after"]
        lines.append(f"  {'always-pass':20} {str(b.get('always_pass_weight')) + ' (' + _pct(b.get('always_pass_share')) + ')':>16} "
                     f"{str(a['always_pass_weight']) + ' (' + _pct(a['always_pass_share']) + ')':>16}")
        lines.append(f"  before = {r['before_source']}")
    return "\n".join(lines)


# ------------------------------------------------------------------ self-test

def _fixture(td: Path, *, closes: int = 6, template: bool = False, anchor_rows=None) -> None:
    """A small synthetic task: a sheet, four comments, `closes` issue moves, one Slack reply."""
    wf = td / "Working_Files"
    (wf / "solver").mkdir(parents=True, exist_ok=True)
    deliverables = {"plan": {"kind": "table", "name_regex": "plan", "key_column": "key", "key_regex": r"K-\d{2}",
                             "columns": ["key", "call"], "class_column": "call"},
                    "comments": {"kind": "json_text", "tool": "linear_create_comment"},
                    "moves": {"kind": "json_text", "tool": "linear_update_issue"},
                    "reply": {"kind": "json_text", "tool": "slack_send_message"}}

    def slot(sid, weight, kind, cls, selector, role="core", **more):
        return dict({"id": sid, "title": sid, "weight": weight, "work_kind": kind, "work_reason": "self-test",
                     "class": cls, "selector": selector, "role": role}, **more)
    slots = [slot("X1", 5, "multi_source_reconciliation", "direct", ["field", "K-01", "call"], "exception",
                  mechanisms=["RET"], singled_out_by="H1"),
             slot("X2", 5, "multi_source_reconciliation", "direct", ["field", "K-02", "call"], "exception",
                  mechanisms=["OFF"], singled_out_by="H1"),
             slot("B1", 5, "multi_source_reconciliation", "write_content", ["text", "plan", r"\b959\b"],
                  mechanisms=["RET", "OFF"]),
             slot("V1", 3, "calculation", "direct", ["field", "K-03", "call"], mechanisms=["COIN1"]),
             slot("V2", 3, "calculation", "direct", ["field", "K-04", "call"], mechanisms=["COIN2"]),
             slot("C1", 3, "interpretation", "write_content", ["text", "comments", "(ENG-1)[ -~]{0,80}returned"],
                  mechanisms=["RET"]),
             slot("C2", 3, "interpretation", "write_content", ["text", "comments", "(ENG-2)[ -~]{0,80}card"],
                  mechanisms=["OFF"]),
             slot("R1", 3, "interpretation", "write_content", ["text", "reply", r"\b959\b"], mechanisms=["RET", "OFF"]),
             slot("D1", 1, "lookup", "delivery", ["delivery", "slack_thread", "1700000000.000100"]),
             slot("T1", 3, "interpretation", "write_content",
                  ["text", "plan", r"(?=[ -~]*layer)(?=[ -~]*export)[ -~]*?mar"], atoms_note="two facts")]
    if template:
        slots += [slot(f"M{i}", 1, "lookup", "write_content", ["text", "moves", f"(ENG-{i})[ -~]{{0,80}}Done"],
                       "sample", group="moves") for i in (1, 2, 3)]
        slots.append(slot("MV", 1, "lookup", "write_content", ["text", "reply", r"\b6\b"], "volume",
                          volume_for=["moves"]))
    surface = {"kind": "GRADABLE_SURFACE", "version": 1, "task": "selftest", "revision": "design-1",
               "classes": ["GO", "HOLD"], "truth_fields": {"class": "call", "groups": "groups"},
               "truth_keys": ["K-01", "K-02", "K-03", "K-04"], "deliverables": deliverables, "slots": slots}
    manifest = {"writes": [{"service": "gsheets", "tool": "gsheets_create_spreadsheet+gsheets_values_update", "count": 2},
                           {"service": "linear", "tool": "linear_create_comment", "count": 4},
                           {"service": "linear", "tool": "linear_update_issue", "count": closes},
                           {"service": "gdrive", "tool": "gdrive_share_file", "count": 2},
                           {"service": "slack", "tool": "slack_send_message", "count": 1}]}
    budget = {"schema": "difficulty-budget-v1", "design_id": "D1", "revision": "rev1", "mode": "easy",
              "weight_basis": "surface", "total_weight": sum(s["weight"] for s in slots),
              "units": [{"id": "U1", "role": "anchor", "mechanism": "RET", "find_rate": [0.0, 0.15],
                         "decider": {"service": "slack", "record_id": "C0123ABCD/1700000000.000100"},
                         "rows": anchor_rows if anchor_rows is not None else [{"id": "X1", "weight": 5},
                                                                               {"id": "C1", "weight": 3}]},
                        {"id": "U2", "role": "anchor", "mechanism": "OFF", "find_rate": [0.0, 0.15],
                         "rows": [{"id": "X2", "weight": 5}, {"id": "C2", "weight": 3}]},
                        {"id": "U3", "role": "variance", "mechanism": "COIN1", "find_rate": [0.35, 0.65],
                         "rows": [{"id": "V1", "weight": 3}]},
                        {"id": "U4", "role": "variance", "mechanism": "COIN2", "find_rate": [0.35, 0.65],
                         "rows": [{"id": "V2", "weight": 3}]},
                        {"id": "U5", "role": "realism", "mechanism": "TRAP", "rows": [{"id": "D1", "weight": 1}]}]}
    truth = {f"K-0{i}": {"key": f"K-0{i}", "call": "GO", "groups": ["plan"]} for i in range(1, 5)}
    (wf / SURFACE).write_text(json.dumps(surface, indent=1) + "\n")
    (wf / MANIFEST).write_text(json.dumps(manifest, indent=1) + "\n")
    (wf / BUDGET).write_text(json.dumps(budget, indent=1) + "\n")
    (wf / "solver" / "truth.json").write_text(json.dumps(truth, indent=1) + "\n")


def _self_test() -> None:
    import selftest_sandbox
    policy = load_policy()
    with selftest_sandbox.scratch_tmp("rubric_skeleton_") as tmp:
        root = Path(tmp)
        # 1. build: slots, the atomic split, one row per separate write, units by mechanism and by budget row
        td = root / "good"
        _fixture(td)
        r = cmd_build(td)
        doc = r["skeleton"]
        t = doc["totals"]
        assert r["verdict"] == "PASS", r["checks"]
        by_slot = collections.Counter(x["slot"] for x in doc["rows"])
        assert by_slot["T1"] == 2, "a lookahead regex with two facts must become two rows"
        w = {x["tool"]: x for x in doc["writes"]}
        assert w["gsheets_create_spreadsheet+gsheets_values_update"]["added_rows"] == [], "sheet cells add no row"
        assert len(w["linear_create_comment"]["added_rows"]) == 2, "4 comments, 2 named by slots: 2 rows added"
        assert len(w["linear_update_issue"]["added_rows"]) == 6, "6 separate moves: 6 rows"
        assert len(w["gdrive_share_file"]["added_rows"]) == 2 and w["slack_send_message"]["added_rows"] == []
        added = [x for x in doc["rows"] if x["slot"] is None]
        assert {x["weight"] for x in added if "gdrive_share_file" in x["write_target"]} == {1}
        assert {x["weight"] for x in added if "linear_update_issue" in x["write_target"]} == {3}
        assert all(x["units"] == [] for x in added), "added write rows start always-pass"
        rows = {x["slot"]: x for x in doc["rows"] if x["source"] == "slot"}
        assert rows["X1"]["units"] == ["U1"] and rows["B1"]["units"] == ["U1", "U2"] and rows["D1"]["units"] == []
        assert t["rows"] == 11 + 10 and t["total_weight"] == 37 + 2 * 3 + 6 * 3 + 2 * 1, t
        assert t["anchor_weight"] == 5 + 5 + 5 + 3 + 3 + 3 and t["coin_flip_weight"] == 6
        assert t["always_pass_weight"] == t["total_weight"] - 24 - 6
        assert set(doc["bound_to"]) == {"Working_Files/01_Gradable_Surface.json", "Working_Files/01_Hardness_Manifest.json",
                                        "Working_Files/01_Difficulty_Budget.json", "Working_Files/solver/truth.json"}
        assert "criterion" not in json.dumps(doc).lower() and "title" not in doc["rows"][0], "no wording in a skeleton"
        assert dump(build(td)) == dump(doc), "build is deterministic"
        # 2. check: missing, bound, stale (one issue move, so the shares hold)
        tdb = root / "bound"
        _fixture(tdb, closes=1)
        c = cmd_check(tdb, policy)
        assert c["verdict"] == "FAIL" and c["checks"][0]["id"] == "skeleton.present", c["checks"]
        cmd_build(tdb, write=True)
        c = cmd_check(tdb, policy)
        st = {x["id"]: x["status"] for x in c["checks"]}
        assert st == {"skeleton.present": "PASS", "skeleton.bound": "PASS", "skeleton.share": "PASS"}, c["checks"]
        assert evaluate(tdb, "check", policy)["verdict"] == "PASS"
        sp = tdb / "Working_Files" / SURFACE
        sp.write_text(sp.read_text() + "\n")
        c = cmd_check(tdb, policy)
        assert {x["id"]: x["status"] for x in c["checks"]}["skeleton.bound"] == "FAIL", "a changed surface is stale"
        # 3. check: write-target rows dilute the anchors below easy loss + margin
        td2 = root / "diluted"
        _fixture(td2, closes=60)
        cmd_build(td2, write=True)
        c = cmd_check(td2, policy)
        sh = [x for x in c["checks"] if x["id"] == "skeleton.share"][0]
        assert sh["status"] == "FAIL" and c["verdict"] == "FAIL", sh
        assert c["totals"]["anchor_share"] < 0.12
        # 4. one template: the same 60 moves stay sampled, and the share holds
        td3 = root / "template"
        _fixture(td3, closes=60, template=True)
        b3 = cmd_build(td3, write=True)
        w3 = {x["tool"]: x for x in b3["skeleton"]["writes"]}["linear_update_issue"]
        assert w3["template"] is True and w3["added_rows"] == [], w3
        assert cmd_check(td3, policy)["verdict"] == "PASS"
        man = td3 / "Working_Files" / MANIFEST
        m = json.loads(man.read_text())
        m["writes"][1]["template"] = True          # declared: the four comments follow one template
        man.write_text(json.dumps(m, indent=1) + "\n")
        w4 = {x["tool"]: x for x in cmd_build(td3)["skeleton"]["writes"]}["linear_create_comment"]
        assert w4["template"] is True and len(w4["added_rows"]) == 1, "declared template: samples plus one volume row"
        # 5. coin-flip share more than five points under the declared share: WARN
        cmd_build(td, write=True)                   # six moves: the design's 6 of 34 becomes 6 of 63
        c = cmd_check(td, policy)
        sh = [x for x in c["checks"] if x["id"] == "skeleton.share"][0]
        assert sh["status"] == "WARN" and c["verdict"] == "WARN", sh
        # 6. rebase prints the budget rows on the skeleton basis; a budget on that basis keeps the same units
        td6 = root / "rebase"
        _fixture(td6)
        rb = rebase(td6)
        assert rb["weight_basis"] == "skeleton" and rb["total_weight"] == 63
        u1 = [u for u in rb["units"] if u["id"] == "U1"][0]
        assert [x["id"] for x in u1["rows"]] == ["S1", "S3", "S6", "S8"], u1
        bp = td6 / "Working_Files" / BUDGET
        b = json.loads(bp.read_text())
        b["weight_basis"], b["total_weight"] = "skeleton", rb["total_weight"]
        for u in b["units"]:
            u["rows"] = [x for v in rb["units"] if v["id"] == u["id"] for x in v["rows"]]
        b["units"][0]["rows"].append({"id": "S12", "weight": 3})   # the author adds an added write row to U1
        bp.write_text(json.dumps(b, indent=1) + "\n")
        d6 = build(td6)
        assert d6["totals"]["per_unit"]["U1"]["rows"] == ["S1", "S3", "S6", "S8", "S12"], d6["totals"]["per_unit"]["U1"]
        # 7. drift on the final rubric
        td7 = root / "drift"
        _fixture(td7)
        cmd_build(td7, write=True)
        d = cmd_drift(td7, policy)
        assert d["checks"][0]["status"] == "SKIP", "no rubric yet"
        rub = [{"title": f"row {i}", "weight": w, "category": "Outcome"} for i, w in
               enumerate([5, 5, 5, 3, 3, 3, 3, 3] + [3] * 8 + [1] * 5, 1)]
        (td7 / RUBRIC).write_text(json.dumps(rub) + "\n")
        d = cmd_drift(td7, policy)
        assert d["verdict"] == "FAIL" and "rubric_rows" in d["checks"][0]["detail"], d["checks"]
        bp = td7 / "Working_Files" / BUDGET
        b = json.loads(bp.read_text())
        b["rubric_rows"] = {"U1": ["R1", "R3", "R4", "R6"], "U2": ["R2", "R3", "R5", "R6"], "U3": ["R7"], "U4": ["R8"]}
        bp.write_text(json.dumps(b, indent=1) + "\n")
        cmd_build(td7, write=True)
        d = cmd_drift(td7, policy)
        assert d["verdict"] == "PASS", d["checks"]
        assert d["after"]["anchor_weight"] == 24 and d["after"]["total_weight"] == 59
        assert "skeleton" in to_text(d) and "U1" in to_text(d)
        rub += [{"title": f"move {i}", "weight": 1, "category": "Outcome"} for i in range(8)]
        (td7 / RUBRIC).write_text(json.dumps(rub) + "\n")
        d = cmd_drift(td7, policy)
        assert d["verdict"] == "WARN" and "always-pass share grew" in d["checks"][0]["detail"], d["checks"]
        rub += [{"title": f"move {i}", "weight": 3, "category": "Outcome"} for i in range(70)]
        (td7 / RUBRIC).write_text(json.dumps(rub) + "\n")
        d = cmd_drift(td7, policy)
        assert d["verdict"] == "FAIL" and "drifted over the cap" in d["checks"][0]["detail"], d["checks"]
        b["rubric_rows"]["U1"] = ["R1", "R999"]
        bp.write_text(json.dumps(b, indent=1) + "\n")
        d = cmd_drift(td7, policy)
        assert d["verdict"] == "FAIL" and "R999" in d["checks"][0]["detail"]
        # 8. usage errors and the output shape
        try:
            build(root / "nowhere")
            raise AssertionError("a missing task folder must be a usage error")
        except UsageError:
            pass
        out = cmd_check(td3, policy)
        assert set(out) >= {"tool", "version", "verdict", "bound_to", "checks"} and out["tool"] == TOOL
        assert to_text(out).splitlines()[0].startswith("RUBRIC SKELETON (check): ")
        # 9. backtest over a synthetic archive folder
        arch = root / "archives" / "demo" / "task_inputs"
        _fixture(arch)
        (arch / RUBRIC).write_text(json.dumps([{"title": "x", "weight": 3}] * 20) + "\n")
        bt = backtest(root / "archives")
        assert len(bt["rows"]) == 1 and bt["rows"][0]["skeleton_rows"] == 21 and bt["rows"][0]["final_rows"] == 20
        assert "demo" in backtest_text(bt)
    print("self-test: ok (build rows, atomic split, write targets, one-template test, units, bound, share FAIL and "
          "WARN, rebase, drift PASS/WARN/FAIL, usage errors, backtest table)")


# ------------------------------------------------------------------ CLI

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        _self_test()
        return 0
    ap = argparse.ArgumentParser(prog="rubric_skeleton.py", description="The rubric's shape before the pre-check.")
    sub = ap.add_subparsers(dest="command")
    for name in ("build", "check", "rebase", "drift"):
        p = sub.add_parser(name)
        p.add_argument("--task-dir", required=True)
        p.add_argument("--json", action="store_true")
        if name == "build":
            p.add_argument("--write", action="store_true", help=f"store Working_Files/{SKELETON}")
    p = sub.add_parser("backtest")
    p.add_argument("--archives", default=None)
    p.add_argument("--json", action="store_true")
    try:
        args = ap.parse_args(argv)
    except SystemExit as error:
        return 2 if error.code not in (0, None) else 0
    if not args.command:
        ap.print_usage(sys.stderr)
        return 2
    try:
        if args.command == "backtest":
            r = backtest(Path(args.archives) if args.archives else None)
            print(json.dumps(r, indent=1, sort_keys=True, ensure_ascii=False) if args.json else backtest_text(r))
            return 0
        if args.command == "rebase":
            print(json.dumps(rebase(args.task_dir), indent=1, ensure_ascii=False))
            return 0
        if args.command == "build":
            r = cmd_build(args.task_dir, write=args.write)
        elif args.command == "check":
            r = cmd_check(args.task_dir)
        else:
            r = cmd_drift(args.task_dir)
    except UsageError as error:
        print(f"rubric_skeleton: {error}", file=sys.stderr)
        return 2
    except Exception as error:  # a refused write (read-only root) and the like
        if error.__class__.__name__ == "ContextError":
            print(f"rubric_skeleton: {error}", file=sys.stderr)
            return 2
        raise
    print(json.dumps(r, indent=1, sort_keys=True, ensure_ascii=False) if args.json else to_text(r))
    return 1 if r["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())

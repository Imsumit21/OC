#!/usr/bin/env python3
"""difficulty_budget.py - check at design time that a task's planned misses can pass the baseline gates (plan WS1).

A task is graded on six baseline runs. It passes only when fewer than five runs are full passes, the average weighted
pass rate is strictly under the mode's cap (easy 0.90, medium 0.85, hard 0.70), the largest failure signature covers
at most half of the failing runs with at least two signatures, and (second priority) the population SD of the per-run
weighted pass rates is inside 0.1-0.3. This tool reads the author's difficulty budget
(<task>/Working_Files/01_Difficulty_Budget.json, schema difficulty-budget-v1) and says whether the planned miss units
can produce that outcome. It reads only; it never writes a task file.

Commands
  check --task-dir T [--budget FILE] [--json]   run the checks below. Exit 0 PASS or WARN, 1 FAIL, 2 usage error.
  table --task-dir T [--budget FILE]            the budget as a Markdown table, for 01_Scenario_Design.md.
  template --task-dir T                         a starter budget from the hardness manifest (mechanism_portfolio ids
                                                and their `decides` slots) and the surface weights. Printed only; the
                                                author fills role, cause, carrier, habit, decider and find_rate.
  derive --input 12_difficulty_input.json [--mode M] [--check]
                                                a budget built after the fact from a real baseline (see Backtest);
                                                --mode for a matrix that records none, --check prints its check.
  backtest [--archives DIR] [--json]            derive + check on every stored baseline, next to the real gates.
  --self-test

Weights. Rows and weights are checked against the file named by weight_basis: surface (01_Gradable_Surface.json
slots), skeleton (01_Rubric_Skeleton.json rows) or rubric (09_Rubrics.json, R1.. in file order). When the budget has
rubric_rows and 09_Rubrics.json has criteria, each unit's rows, the weights and the total come from the rubric. A
realism unit carries no weight: its rows are never read.

Checks (thresholds: references/first_pass_policy.json `budget`; caps and run counts: references/v3_policy.json as
difficulty_stats reads them)
  budget.schema               well-formed file, known roles, find_rate [lo, hi] with 0 <= lo <= hi <= 1, unique ids
  budget.context              mode equals the assigned difficulty mode (SKIP when no V3 context loads)
  budget.rows                 every row is on the basis file with the same weight; total_weight is the basis total
  budget.carriers             an anchor or variance unit on a carrier that produced no misses fails; other:<text> warns
  budget.unit_rows            each anchor and variance unit flips enough rows, one of weight 5 (WARN when too few of
                              a unit's rows are its own: rows shared with another unit do not split signatures)
  budget.independence         units that share one habit (service + read action) are one coin flip; merges are listed
  budget.anchors              enough separate causes; combined share >= the mode's loss + margin; each cause under the
                              share limit; each anchor's high find rate under the limit
  budget.variance             enough independent coin-flip habits whose find-rate range is inside the policy window
  budget.average              P(six-run average strictly under the cap), at both ends of the find-rate ranges
  budget.full_passes          P(fewer than five full passes), at both ends
  budget.signature            P(signature gate passes), at both ends
  budget.signature_one_error  the same with one run errored (five runs)
  budget.spread               P(SD inside the band) at both ends and the midpoint; WARN only, never FAIL
  budget.hard_mode            WARN in hard mode: no platform report states the hard loss figure

Simulation model. Anchor and variance units are grouped by habit; units behind one habit are one coin flip. For each
run, one uniform draw u in [0, 1) is made per habit group, and a unit is found when u is below its find rate (so the
units of one group move together, and a unit with the lower find rate is found only when the others are). The rows a
run fails are the union of the rows of its missed units. A run's weighted pass rate is
1 - failed weight / total weight - undesigned loss. A run that fails no row is a full pass and is not a failing run;
that is "no missed unit" whenever every unit has a row. The undesigned loss is one constant per run: the low end of
undesigned_loss is used at the high find-rate end and the high end at the low find-rate end. It lowers the average,
and when it is above zero no run counts as a full pass at that end; it never adds a failed row, so it never adds a
signature and never changes the SD. Three settings are scored from the same draws: every unit at the low end of its
range, every unit at the midpoint (with the midpoint undesigned loss), every unit at the high end. The checks read the
two ends; the midpoint is used by the spread check and printed by the backtest. The one-errored-run case drops the
last run of each trial. Signatures are grouped by difficulty_stats.group_patterns (two failing runs share a signature
unless their failed rows differ on two or more rows); the SD, band, average and full-pass rules are the ones in
difficulty_stats._gates. Seed and trial count come from the policy, so the same budget always prints the same numbers.

Backtest. No archived task has a budget file, so `derive` builds one from a baseline matrix: rubric rows with the same
pass/fail vector over the completed runs become one unit; a group that fails every run is an anchor with find rate
[0, 0], any other failing group is a variance unit whose find rate is the share of runs that passed it, +/- 0.15.
`backtest` derives and checks a budget for every baseline matrix under the archives and prints the result next to the
real gate verdicts (difficulty_stats.compute under the V3 rules). It reads each task's final 12_difficulty_input.json,
any other stored JSON with rubrics and six rollouts (run_forensics/, work/), and, for a task that kept no matrix,
rebuilds one in memory from its verifier results. A matrix without a difficulty mode takes the mode written in the
task's 00_Assigments.md. That is a calibration test of the thresholds. It is not proof that a budget written at
design time predicts the outcome: derived units are whatever rows happened to fail together in six runs, and real
units are not independent.

Python API: evaluate(task_dir, budget_path=None) -> dict (the --json object; no side effects).
Stdlib only.
"""
from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import math
import os
import random
import re
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WS = BUNDLE.parent
sys.path.insert(0, str(HERE))

import difficulty_stats as stats  # noqa: E402  (sibling tool: caps, run counts, group_patterns, EPS)

TOOL = "difficulty_budget"
VERSION = 1
SCHEMA = "difficulty-budget-v1"
POLICY_PATH = BUNDLE / "references" / "first_pass_policy.json"
ARCHIVES = BUNDLE / "support" / "completed_tasks"
BUDGET_NAME = "01_Difficulty_Budget.json"
RUBRIC_NAME = "09_Rubrics.json"
MANIFEST_NAMES = ("01_Hardness_Manifest.json", "01_Hardness_Manifest.draft.json")
ROLES = ("anchor", "variance", "realism")
BASIS_FILES = {"surface": "01_Gradable_Surface.json", "skeleton": "01_Rubric_Skeleton.json", "rubric": RUBRIC_NAME}
BASIS_KEYS = {"surface": "slots", "skeleton": "rows"}
CHECK_IDS = ("budget.schema", "budget.context", "budget.rows", "budget.carriers", "budget.unit_rows",
             "budget.independence", "budget.anchors", "budget.variance", "budget.average", "budget.full_passes",
             "budget.signature", "budget.signature_one_error", "budget.spread", "budget.hard_mode")
# Not in the policy file (listed in the hand-off report so the lead can move them there).
DEFAULT_UNDESIGNED_LOSS = (0.0, 0.0)     # used when the budget has no undesigned_loss
DERIVE_HALF_RANGE = 0.15                 # derive: find-rate range around the observed pass share
RATE_TOLERANCE = 1e-9                    # float slack on find-rate window edges (0.5 - 0.15 must count as 0.35)
MAX_MATRIX_BYTES = 8_000_000             # backtest: larger JSON files are not baseline matrices
SKIP_DIRS = {"07_Baseline_Trajectories", "06_PreCheck_Trajectory", "__pycache__", ".git"}


# ------------------------------------------------------------------ small helpers

def load_policy(path=None) -> dict:
    """The `budget` block of references/first_pass_policy.json."""
    data = json.loads(Path(path or POLICY_PATH).read_text(encoding="utf-8"))
    return data["budget"]


def _num(value):
    """A finite JSON number that is not a bool, else None."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
        return None
    return value


def _text(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _frac(value) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(str(value))


def _range_ok(value) -> bool:
    return (isinstance(value, list) and len(value) == 2 and _num(value[0]) is not None and _num(value[1]) is not None
            and 0 <= value[0] <= value[1] <= 1)


def _fmt(value) -> str:
    """A weight without a trailing .0."""
    value = _frac(value)
    return str(value.numerator) if value.denominator == 1 else f"{float(value):g}"


def _pct(value) -> str:
    return f"{100 * float(value):.1f}%"


def _join(items, limit=6) -> str:
    items = list(items)
    more = len(items) - limit
    return "; ".join(items[:limit]) + (f"; and {more} more" if more > 0 else "")


def habit_key(habit) -> tuple:
    """Two units are one coin flip when service and action match (case and outer spaces ignored)."""
    return (str(habit.get("service", "")).strip().lower(), str(habit.get("action", "")).strip().lower())


def _sha256(path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _rel(path, task_dir) -> str:
    try:
        return Path(path).resolve().relative_to(Path(task_dir).resolve()).as_posix()
    except ValueError:
        return Path(path).resolve().as_posix()


def _components(items, keys_of) -> list:
    """Connected components: two items join when they share any key. Order of first appearance is kept."""
    groups = []                                    # [(key set, [items])]
    for item in items:
        keys, members = set(keys_of(item)), [item]
        rest = []
        for other_keys, other_members in groups:
            if keys & other_keys:
                keys |= other_keys
                members = other_members + members
            else:
                rest.append((other_keys, other_members))
        groups = rest + [(keys, members)]
    return [members for _, members in groups]


# ------------------------------------------------------------------ schema

def schema_problems(budget, policy=None) -> list:
    """Every reason the file is not a well-formed difficulty-budget-v1 (empty list = well-formed)."""
    if not isinstance(budget, dict):
        return ["the file is not a JSON object"]
    out = []
    if budget.get("schema") != SCHEMA:
        out.append(f'schema must be "{SCHEMA}" (got {budget.get("schema")!r})')
    for key in ("design_id", "revision"):
        if not _text(budget.get(key)):
            out.append(f"{key} must be a non-empty string")
    if budget.get("mode") not in stats.DIFFICULTY_CAPS:
        out.append(f"mode must be one of {', '.join(sorted(stats.DIFFICULTY_CAPS))} (got {budget.get('mode')!r})")
    if budget.get("weight_basis") not in BASIS_FILES:
        out.append(f"weight_basis must be surface, skeleton or rubric (got {budget.get('weight_basis')!r})")
    total = _num(budget.get("total_weight"))
    if total is None or total <= 0:
        out.append("total_weight must be a number above 0")
    if budget.get("undesigned_loss") is not None and not _range_ok(budget["undesigned_loss"]):
        out.append("undesigned_loss must be [lo, hi] with 0 <= lo <= hi <= 1")
    units = budget.get("units")
    if not isinstance(units, list) or not units:
        return out + ["units must be a non-empty list"]
    seen = set()
    for number, unit in enumerate(units, 1):
        label = f"units[{number}]"
        if not isinstance(unit, dict):
            out.append(f"{label} is not an object")
            continue
        if not _text(unit.get("id")):
            out.append(f"{label}: id must be a non-empty string")
        else:
            label = f"unit {unit['id']}"
            if unit["id"] in seen:
                out.append(f"{label}: the id is used twice")
            seen.add(unit["id"])
        if unit.get("role") not in ROLES:
            out.append(f"{label}: role must be anchor, variance or realism (got {unit.get('role')!r})")
            continue
        if unit["role"] == "realism":
            continue                                   # realism carries no budget weight: nothing else is read
        if not _range_ok(unit.get("find_rate")):
            out.append(f"{label}: find_rate must be [lo, hi] with 0 <= lo <= hi <= 1")
        habit = unit.get("habit")
        if not isinstance(habit, dict) or not _text(habit.get("service")) or not _text(habit.get("action")):
            out.append(f"{label}: habit needs a service and an action")
        decider = unit.get("decider")
        if (not isinstance(decider, dict) or not _text(decider.get("service")) or not _text(decider.get("record_id"))
                or not isinstance(decider.get("injected"), bool)):
            out.append(f"{label}: decider needs a service, a record_id and injected true/false")
        if not _text(unit.get("carrier")):
            out.append(f"{label}: carrier must be a non-empty string")
        if unit["role"] == "anchor" and not _text(unit.get("cause_key")):
            out.append(f"{label}: an anchor needs a cause_key")
        rows = unit.get("rows")
        if not isinstance(rows, list):
            out.append(f"{label}: rows must be a list")
            continue
        ids = []
        for row in rows:
            if not isinstance(row, dict) or not _text(row.get("id")) or _num(row.get("weight")) is None \
                    or row["weight"] <= 0:
                out.append(f"{label}: each row needs an id and a weight above 0")
                break
            ids.append(row["id"])
        if len(ids) != len(set(ids)):
            out.append(f"{label}: a row id is listed twice")
    rubric_rows = budget.get("rubric_rows")
    if rubric_rows is not None:
        if not isinstance(rubric_rows, dict):
            out.append("rubric_rows must be an object of unit id -> list of rubric row ids")
        else:
            for uid, ids in sorted(rubric_rows.items()):
                if uid not in seen:
                    out.append(f"rubric_rows names unknown unit {uid}")
                if not isinstance(ids, list) or not all(_text(i) for i in ids):
                    out.append(f"rubric_rows[{uid}] must be a list of rubric row ids")
    return out


# ------------------------------------------------------------------ basis files

def read_basis(task_dir, basis) -> dict:
    """{'rows': {row id: weight}, 'file': name, 'path': Path} for one weight basis, or {'error': ..., ...}."""
    from stage_gate import slot_path
    name = BASIS_FILES[basis]
    path = slot_path(task_dir, name)
    out = {"file": name, "path": path}
    if not path.is_file():
        return dict(out, error=f"{name} not found")
    if basis == "rubric":
        try:
            rubrics, _ = stats.parse_rubrics(path)
        except (ValueError, OSError, KeyError, TypeError) as error:
            return dict(out, error=f"{name} has no usable criteria ({str(error)[:160]})")
        return dict(out, rows={r["id"]: r["weight"] for r in rubrics})
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        return dict(out, error=f"{name} is not valid JSON ({str(error)[:120]})")
    items = data.get(BASIS_KEYS[basis]) if isinstance(data, dict) else data
    if not isinstance(items, list) or not items:
        return dict(out, error=f"{name} has no {BASIS_KEYS[basis]}")
    rows = {}
    for item in items:
        if not isinstance(item, dict) or not _text(item.get("id")) or _num(item.get("weight")) is None:
            return dict(out, error=f"{name}: every entry of {BASIS_KEYS[basis]} needs an id and a weight")
        if item["id"] in rows:
            return dict(out, error=f"{name}: id {item['id']} appears twice")
        rows[item["id"]] = item["weight"]
    return dict(out, rows=rows)


# ------------------------------------------------------------------ simulation

class _Model:
    """Rows, weights and the gate rules for one budget. A set of failed rows is a bit mask over the rows."""

    def __init__(self, units, total_weight, band=(0.1, 0.3)):
        weights = {}
        for unit in units:
            for rid, weight in unit["rows"].items():
                weights.setdefault(rid, _frac(weight))
        scale = 1                                     # weights become exact integers
        for value in [_frac(total_weight)] + list(weights.values()):
            scale = scale * value.denominator // math.gcd(scale, value.denominator)
        self.total = int(_frac(total_weight) * scale)
        self.row_ids = sorted(weights)
        self.bit = {rid: 1 << i for i, rid in enumerate(self.row_ids)}
        self.unit_mask = []
        for unit in units:
            mask = 0
            for rid in unit["rows"]:
                mask |= self.bit[rid]
            self.unit_mask.append(mask)
        by_weight = {}
        for rid in self.row_ids:
            value = int(weights[rid] * scale)
            by_weight[value] = by_weight.get(value, 0) | self.bit[rid]
        self.weight_classes = sorted(by_weight.items())
        # Rows flipped by the same units always fail together. Two rows per such class decide "differ on <= 1 row"
        # exactly, so group_patterns sees at most two rows per class.
        classes = {}
        for rid in self.row_ids:
            key = tuple(i for i, mask in enumerate(self.unit_mask) if mask & self.bit[rid])
            classes.setdefault(key, []).append(rid)
        self.pattern_ids = [rid for rows in classes.values() for rid in rows[:2]]
        self.band = band
        self._weight, self._results, self._signature = {}, {}, {}

    def failed_weight(self, mask) -> int:
        value = self._weight.get(mask)
        if value is None:
            value = sum(weight * bin(mask & rows).count("1") for weight, rows in self.weight_classes)
            self._weight[mask] = value
        return value

    def rows_of(self, mask) -> list:
        return [rid for rid in self.row_ids if mask & self.bit[rid]]

    def signature_passes(self, masks) -> bool:
        """The failure-pattern gate of difficulty_stats._gates on these runs (a zero mask is a full pass)."""
        key = tuple(sorted(mask for mask in masks if mask))
        verdict = self._signature.get(key)
        if verdict is None:
            verdict = False
            if key:
                failing = []
                for number, mask in enumerate(key):
                    results = self._results.get(mask)
                    if results is None:
                        results = {rid: not mask & self.bit[rid] for rid in self.pattern_ids}
                        self._results[mask] = results
                    failing.append({"id": str(number), "results": results})
                groups = stats.group_patterns(failing, self.pattern_ids)
                verdict = len(groups) >= 2 and len(groups[0]) / len(failing) <= 0.5 + stats.EPS
            self._signature[key] = verdict
        return verdict

    def min_failed_sum(self, runs, cap, loss) -> int:
        """The smallest summed failed weight over `runs` runs whose average pass rate is strictly under `cap`,
        when every run also loses the share `loss`. Exact: average < cap <=> sum > runs * total * (1 - cap - loss)."""
        limit = Fraction(runs * self.total) * (1 - _frac(cap) - _frac(loss))
        return limit.numerator // limit.denominator + 1

    def sd(self, failed_weights) -> float:
        """Population SD of the per-run weighted pass rates (0.0 for fewer than two runs), as in _gates."""
        n = len(failed_weights)
        if n < 2:
            return 0.0
        total = sum(failed_weights)
        squares = sum(weight * weight for weight in failed_weights)
        return math.sqrt(n * squares - total * total) / (n * self.total)

    def in_band(self, failed_weights) -> bool:
        return self.band[0] - stats.EPS <= self.sd(failed_weights) <= self.band[1] + stats.EPS


def simulate(units, total_weight, cap, undesigned=DEFAULT_UNDESIGNED_LOSS, policy=None) -> dict:
    """Monte Carlo over the model in the module docstring.

    units         [{'habit': (service, action), 'lo': float, 'hi': float, 'rows': {row id: weight}}] (no realism)
    total_weight  the basis total
    cap           the mode's cap (average strictly under it)
    undesigned    (lo, hi) share of weight lost outside the units
    Returns the probabilities at the low, middle and high find rates (keys lo, mid, hi). The checks read lo and hi;
    mid (midpoint find rates, midpoint undesigned loss) feeds the spread check and the backtest.
    """
    policy = policy or load_policy()
    runs = stats.BASELINE_RUNS
    short = min(int(policy["runs_with_one_error"]), runs)
    trials, seed = int(policy["trials"]), int(policy["seed"])
    model = _Model(units, total_weight, tuple(policy["spread_band"]))

    groups = {}
    for index, unit in enumerate(units):
        groups.setdefault(tuple(unit["habit"]), []).append(index)
    base, live = [0, 0, 0], []
    for key in sorted(groups):
        members = groups[key]
        rates = {i: (units[i]["lo"], (units[i]["lo"] + units[i]["hi"]) / 2.0, units[i]["hi"]) for i in members}
        cuts = sorted({rate for i in members for rate in rates[i]})
        table = []                                    # table[k]: rows failed when k cut points are <= the draw
        for k in range(len(cuts) + 1):
            entry = [0, 0, 0]
            for i in members:
                for end in range(3):
                    if k and rates[i][end] <= cuts[k - 1]:
                        entry[end] |= model.unit_mask[i]
            table.append(tuple(entry))
        reachable = table[bisect.bisect_right(cuts, 0.0):bisect.bisect_left(cuts, 1.0) + 1]   # the draw is in [0, 1)
        if all(entry == reachable[0] for entry in reachable):
            for end in range(3):                      # always found or always missed: no draw needed
                base[end] |= reachable[0][end]
        else:
            live.append((cuts, table))

    cap = _frac(cap)
    loss = {0: _frac(undesigned[1]), 1: (_frac(undesigned[0]) + _frac(undesigned[1])) / 2,
            2: _frac(undesigned[0])}                                # low find rates take the high loss
    need = {end: model.min_failed_sum(runs, cap, value) for end, value in loss.items()}
    counts = {name: [0, 0, 0] for name in ("average", "full_passes", "signature", "signature_one_error", "spread")}
    draw = random.Random(seed).random
    cut_index = bisect.bisect_right
    weight_of, signature, in_band = model.failed_weight, model.signature_passes, model.in_band
    full_limit = stats.FULL_PASS_FAILURE_COUNT
    base_lo, base_mid, base_hi = base
    for _ in range(trials):
        lo_runs, mid_runs, hi_runs = [], [], []
        for _run in range(runs):
            a, b, c = base_lo, base_mid, base_hi
            for cuts, table in live:
                x, y, z = table[cut_index(cuts, draw())]
                a |= x
                b |= y
                c |= z
            lo_runs.append(a)
            mid_runs.append(b)
            hi_runs.append(c)
        for end, masks in ((0, lo_runs), (1, mid_runs), (2, hi_runs)):
            failed = [weight_of(mask) for mask in masks]
            if sum(failed) >= need[end]:
                counts["average"][end] += 1
            if (masks.count(0) if not loss[end] else 0) < full_limit:
                counts["full_passes"][end] += 1
            if signature(masks):
                counts["signature"][end] += 1
            if signature(masks[:short]):
                counts["signature_one_error"][end] += 1
            if in_band(failed):
                counts["spread"][end] += 1
    out = {"trials": trials, "seed": seed, "runs": runs, "runs_one_error": short,
           "habit_groups": len(groups), "groups_drawn": len(live)}
    for end, name in ((0, "lo"), (1, "mid"), (2, "hi")):
        out[name] = {key: value[end] / trials for key, value in counts.items()}
        out[name]["undesigned_loss"] = float(loss[end])
    return out


# ------------------------------------------------------------------ the checks

def _result(checks, mode, bound_to=None, summary=None) -> dict:
    statuses = {check["status"] for check in checks}
    verdict = "FAIL" if "FAIL" in statuses else "WARN" if "WARN" in statuses else "PASS"
    out = {"tool": TOOL, "version": VERSION, "verdict": verdict, "bound_to": dict(bound_to or {}),
           "checks": checks, "mode": mode if mode in stats.DIFFICULTY_CAPS else None}
    if summary is not None:
        out["budget"] = summary
    return out


def _schema_failure(detail, mode=None, bound_to=None) -> dict:
    checks = [{"id": "budget.schema", "status": "FAIL", "detail": detail}]
    checks += [{"id": cid, "status": "SKIP", "detail": "Not run: fix budget.schema first."} for cid in CHECK_IDS[1:]]
    return _result(checks, mode, bound_to)


def evaluate_budget(budget, basis=None, rubric=None, context=None, policy=None, bound_to=None) -> dict:
    """Run every check on a budget already in memory.

    basis    read_basis() output for the declared weight_basis ({'rows': {id: weight}} or {'error': text})
    rubric   {'rows': {R id: weight}} from 09_Rubrics.json, {'error': text}, or None when there is no such file
    context  {'mode': assigned mode} or {'skip': reason}
    """
    policy = policy or load_policy()
    problems = schema_problems(budget, policy)
    if problems:
        mode = budget.get("mode") if isinstance(budget, dict) else None
        return _schema_failure(_join(problems) + ". Fix the file; the other checks need a well-formed budget.",
                               mode, bound_to)
    checks = []

    def add(cid, status, detail):
        checks.append({"id": cid, "status": status, "detail": detail})

    mode = budget["mode"]
    cap = stats.DIFFICULTY_CAPS[mode]
    live = [unit for unit in budget["units"] if unit["role"] != "realism"]
    realism = [unit["id"] for unit in budget["units"] if unit["role"] == "realism"]
    count = {role: sum(1 for unit in budget["units"] if unit["role"] == role) for role in ROLES}
    add("budget.schema", "PASS", f"{len(budget['units'])} units ({count['anchor']} anchor, {count['variance']} "
        f"variance, {count['realism']} realism), design {budget['design_id']}, revision {budget['revision']}.")

    # ---- context
    context = context or {"skip": "no task context was given"}
    if context.get("mode") is None:
        add("budget.context", "SKIP", f"No V3 task context: {context.get('skip') or 'not loaded'}.")
    elif context["mode"] == mode:
        add("budget.context", "PASS", f"mode {mode} is the assigned difficulty mode.")
    else:
        add("budget.context", "FAIL", f"The budget says mode {mode} but the assignment says {context['mode']}; "
            "set mode to the assigned value and re-check.")

    # ---- rows and weights
    declared = budget["weight_basis"]
    basis = basis or {"error": f"{BASIS_FILES[declared]} not found", "file": BASIS_FILES[declared]}
    basis_name = basis.get("file") or BASIS_FILES[declared]
    rubric_rows = budget.get("rubric_rows") or {}
    override = bool(rubric_rows) and bool(rubric) and rubric.get("rows") is not None
    row_problems, row_notes = [], []
    if basis.get("rows") is None:
        if override:
            row_notes.append(f"the declared rows were not checked ({basis.get('error')})")
        else:
            row_problems.append(f"{basis.get('error')}, so the rows cannot be checked against the {declared} basis")
    else:
        for unit in live:
            for row in unit["rows"]:
                if row["id"] not in basis["rows"]:
                    row_problems.append(f"unit {unit['id']} row {row['id']} is not in {basis_name}")
                elif _frac(basis["rows"][row["id"]]) != _frac(row["weight"]):
                    row_problems.append(f"unit {unit['id']} row {row['id']} has weight {_fmt(row['weight'])} but "
                                        f"{basis_name} says {_fmt(basis['rows'][row['id']])}")
        basis_total = sum((_frac(weight) for weight in basis["rows"].values()), Fraction(0))
        if basis_total != _frac(budget["total_weight"]):
            row_problems.append(f"total_weight is {_fmt(budget['total_weight'])} but {basis_name} adds up to "
                                f"{_fmt(basis_total)}")
    if rubric_rows and not override:
        row_notes.append("rubric_rows is not used yet (" + ((rubric or {}).get("error") or f"no {RUBRIC_NAME}") + ")")
    effective = {}
    if override:
        source, total = "rubric_rows", sum((_frac(weight) for weight in rubric["rows"].values()), Fraction(0))
        for unit in live:
            ids = rubric_rows.get(unit["id"]) or []
            unknown = [rid for rid in ids if rid not in rubric["rows"]]
            if not ids:
                row_problems.append(f"unit {unit['id']} has no rubric_rows entry")
            if unknown:
                row_problems.append(f"unit {unit['id']} rubric_rows names rows that are not in {RUBRIC_NAME}: "
                                    + ", ".join(unknown))
            effective[unit["id"]] = {rid: rubric["rows"][rid] for rid in ids if rid in rubric["rows"]}
    elif basis.get("rows") is not None:
        source, total = declared, basis_total
        for unit in live:
            effective[unit["id"]] = {row["id"]: basis["rows"][row["id"]] for row in unit["rows"]
                                     if row["id"] in basis["rows"]}
    else:
        source, total = "declared", _frac(budget["total_weight"])
        for unit in live:
            effective[unit["id"]] = {row["id"]: row["weight"] for row in unit["rows"]}
    if total <= 0:
        row_problems.append("the basis weights add up to 0")
        total = _frac(budget["total_weight"])
    n_rows = sum(len(rows) for rows in effective.values())
    where = (f"{RUBRIC_NAME} through rubric_rows" if override else basis_name if source != "declared"
             else "the budget file itself")
    tail = f" Weights and total come from {where}: {n_rows} rows over {len(live)} units, total weight {_fmt(total)}."
    if realism:
        tail += f" Realism units ignored: {', '.join(realism)}."
    if row_problems:
        add("budget.rows", "FAIL", _join(row_problems) + ". Correct the budget rows or the basis file." + tail)
    elif row_notes:
        add("budget.rows", "WARN", _join(row_notes) + "." + tail)
    else:
        add("budget.rows", "PASS", "Every row matches its basis." + tail)

    units = []
    for unit in live:
        rows = effective[unit["id"]]
        weight = sum((_frac(value) for value in rows.values()), Fraction(0))
        units.append({"id": unit["id"], "role": unit["role"], "carrier": unit["carrier"].strip(),
                      "cause_key": str(unit.get("cause_key") or "").strip().lower(),
                      "habit": habit_key(unit["habit"]), "lo": float(unit["find_rate"][0]),
                      "hi": float(unit["find_rate"][1]), "rows": rows, "weight": weight, "share": weight / total})
    anchors = [unit for unit in units if unit["role"] == "anchor"]
    variance = [unit for unit in units if unit["role"] == "variance"]

    def union_share(members) -> Fraction:
        rows = {}
        for unit in members:
            rows.update(unit["rows"])
        return sum((_frac(value) for value in rows.values()), Fraction(0)) / total

    # ---- carriers
    no_loss, missers = set(policy["carriers_without_loss"]), set(policy["carriers_that_miss"])
    bad, unknown, other = [], [], []
    for unit in units:
        carrier = unit["carrier"]
        if carrier in no_loss:
            bad.append(f"{unit['id']} ({carrier})")
        elif carrier.startswith("other:") and carrier[len("other:"):].strip():
            other.append(f"{unit['id']} ({carrier})")
        elif carrier not in missers:
            unknown.append(f"{unit['id']} ({carrier})")
    if bad or unknown:
        parts = []
        if bad:
            parts.append("these carriers produced no misses in 14 tasks: " + ", ".join(bad)
                         + "; move the deciding record to a carrier that misses or make the unit realism")
        if unknown:
            parts.append("unknown carrier: " + ", ".join(unknown) + "; use one of "
                         + ", ".join(policy["carriers_that_miss"]) + " or other:<text>")
        add("budget.carriers", "FAIL", _join(parts) + ".")
    elif other:
        add("budget.carriers", "WARN", "No miss record for these carriers, so their find rates are a guess: "
            + ", ".join(other) + ".")
    else:
        add("budget.carriers", "PASS", f"All {len(units)} anchor and variance units use carriers that produced misses.")

    # ---- unit rows
    min_rows, need_five = int(policy["unit_min_rows"]), bool(policy.get("unit_needs_weight5"))
    thin = []
    for unit in units:
        reasons = []
        if len(unit["rows"]) < min_rows:
            reasons.append(f"{len(unit['rows'])} row(s), needs {min_rows}")
        if need_five and not any(_frac(weight) == 5 for weight in unit["rows"].values()):
            reasons.append("no row of weight 5")
        if reasons:
            thin.append(f"{unit['id']}: " + " and ".join(reasons))
    shared = []                                       # enough rows, but too few that no other unit flips
    for unit in units:
        others = {rid for other in units if other is not unit for rid in other["rows"]}
        own = [rid for rid in unit["rows"] if rid not in others]
        if len(unit["rows"]) >= min_rows and len(own) < min_rows:
            shared.append(f"{unit['id']} ({len(own)} of {len(unit['rows'])})")
    if thin:
        add("budget.unit_rows", "FAIL", _join(thin) + ". A unit that flips one row never makes a separate signature; "
            "give each unit at least two rows, one of weight 5.")
    elif shared:
        add("budget.unit_rows", "WARN", f"Every unit flips at least {min_rows} rows, but these have fewer than "
            f"{min_rows} rows that no other unit flips: {_join(shared)}. When the other unit is missed too, missing "
            "this one changes at most one row and makes no separate signature; the signature checks below count that.")
    else:
        add("budget.unit_rows", "PASS", f"Each of the {len(units)} anchor and variance units flips at least {min_rows} "
            "rows" + (", one of weight 5." if need_five else "."))

    # ---- independence
    by_habit = {}
    for unit in units:
        by_habit.setdefault(unit["habit"], []).append(unit)
    merged = [f"{' + '.join(u['id'] for u in members)} share {habit[0]}/{habit[1]}"
              for habit, members in sorted(by_habit.items()) if len(members) > 1]
    if merged:
        add("budget.independence", "WARN", f"{len(units)} units make {len(by_habit)} independent habits; "
            + _join(merged) + " and count as one coin flip each. Give a unit its own read action to count it apart.")
    else:
        add("budget.independence", "PASS", f"{len(units)} units, {len(by_habit)} independent habits; no two units "
            "share a habit.")

    # ---- anchors
    loss = _frac(policy["mode_loss"][mode])
    need_share = loss + _frac(policy["anchor_margin"])
    causes = _components(anchors, lambda unit: {("cause", unit["cause_key"]), ("habit", unit["habit"])})
    anchor_share = union_share(anchors)
    cause_shares = [(" + ".join(unit["id"] for unit in members), union_share(members)) for members in causes]
    anchor_failed = []
    if len(causes) < int(policy["anchor_min_causes"]):
        anchor_failed.append(("causes", f"{len(causes)} separate cause(s), needs {policy['anchor_min_causes']} "
                              "(anchors with one cause_key or one habit are one cause)"))
    if anchor_share < need_share:
        anchor_failed.append(("share", f"combined share {_pct(anchor_share)} is under the {mode} loss "
                              f"{_pct(loss)} + margin {_pct(policy['anchor_margin'])} = {_pct(need_share)}"))
    heavy = [f"{name} {_pct(share)}" for name, share in cause_shares if share >= _frac(policy["anchor_max_share"])]
    if heavy:
        anchor_failed.append(("max_share", "at or over the " + _pct(policy["anchor_max_share"])
                              + " single-cause limit: " + ", ".join(heavy)))
    loose = [f"{unit['id']} (up to {unit['hi']:.2f})" for unit in anchors
             if unit["hi"] > policy["anchor_find_rate_max"] + RATE_TOLERANCE]
    if loose:
        anchor_failed.append(("find_rate", f"find rate above {policy['anchor_find_rate_max']:.2f}: " + ", ".join(loose)
                              + " (a record found that often is a variance unit)"))
    if anchor_failed:
        add("budget.anchors", "FAIL", _join(text for _, text in anchor_failed) + ".")
    else:
        add("budget.anchors", "PASS", f"{len(anchors)} anchors from {len(causes)} causes carry {_pct(anchor_share)} "
            f"(needs {_pct(need_share)}); largest cause "
            f"{_pct(max([share for _, share in cause_shares] or [Fraction(0)]))}; highest find rate "
            f"{max([unit['hi'] for unit in anchors] or [0.0]):.2f}.")

    # ---- variance
    window = policy["variance_find_rate"]

    def in_window(unit) -> bool:
        return unit["lo"] >= window[0] - RATE_TOLERANCE and unit["hi"] <= window[1] + RATE_TOLERANCE

    variance_habits = {}
    for unit in variance:
        variance_habits.setdefault(unit["habit"], []).append(unit)
    good_habits = [habit for habit, members in variance_habits.items() if all(in_window(u) for u in members)]
    outside = [f"{unit['id']} ({unit['lo']:.2f}-{unit['hi']:.2f})" for unit in variance if not in_window(unit)]
    need_units = int(policy["variance_min_units"])
    coin_share = union_share(variance)
    span = f"{window[0]:.2f}-{window[1]:.2f}"
    if len(good_habits) < need_units:
        add("budget.variance", "FAIL", f"{len(good_habits)} independent coin-flip habit(s) with a find-rate range "
            f"inside {span}, needs {need_units} ({len(variance)} variance units over {len(variance_habits)} habits"
            + (f"; outside the range: {_join(outside)}" if outside else "") + "). Four independent coin flips are "
            "what keeps the largest signature at or under half of the failing runs.")
    elif outside:
        add("budget.variance", "WARN", f"{len(good_habits)} independent coin-flip habits inside {span} (needs "
            f"{need_units}); not counted, outside the range: {_join(outside)}.")
    else:
        add("budget.variance", "PASS", f"{len(good_habits)} independent coin-flip habits, every find-rate range "
            f"inside {span} (needs {need_units}).")

    # ---- simulation
    undesigned = tuple(budget.get("undesigned_loss") or DEFAULT_UNDESIGNED_LOSS)
    sim = simulate(units, total, cap, undesigned, policy)
    need_p = float(policy["pass_probability"])
    lo, hi = sim["lo"], sim["hi"]

    def gate(cid, key, what, advice):
        ok = min(lo[key], hi[key]) >= need_p - 1e-12
        add(cid, "PASS" if ok else "FAIL", f"P({what}) is {lo[key]:.3f} with every unit at its low find rate and "
            f"{hi[key]:.3f} at its high find rate (needs {need_p:.2f} at both)" + ("." if ok else f". {advice}"))

    gate("budget.average", "average", f"six-run average strictly under {_pct(cap)}",
         "Put more weight on anchor and variance rows, or lower the weight of rows every run passes.")
    gate("budget.full_passes", "full_passes", f"fewer than {stats.FULL_PASS_FAILURE_COUNT} full passes",
         "Too many runs find every unit; add an anchor or lower the find rates.")
    gate("budget.signature", "signature", "largest signature at most 50% of failing runs, two or more signatures",
         "Add independent coin-flip units (four give 0.98 or better) and check each flips two rows.")
    gate("budget.signature_one_error", "signature_one_error",
         f"signature gate with {sim['runs_one_error']} completed runs",
         "One errored run would sink the signature gate; add an independent coin-flip unit.")

    warn_below = float(policy["spread_warn_below"])
    band = policy["spread_band"]
    spread = (lo["spread"], sim["mid"]["spread"], hi["spread"])
    detail = (f"P(SD inside {band[0]}-{band[1]}) is {spread[0]:.3f} / {spread[1]:.3f} / {spread[2]:.3f} at the low / "
              f"middle / high find rates; the design carries {_pct(coin_share)} of weight on coin-flip (variance) "
              f"units and {_pct(anchor_share)} on anchors")
    if min(spread) < warn_below:
        add("budget.spread", "WARN", detail + f". Below {warn_below:.2f}: a spread miss is likely; move more weight "
            "onto coin-flip units (about 60% of weight reaches 0.8) or accept that the miss is reported.")
    else:
        add("budget.spread", "PASS", detail + f" (warns below {warn_below:.2f}).")

    if mode == "hard":
        add("budget.hard_mode", "WARN", f"Hard mode: the {_pct(loss)} loss figure is 1 - cap, not a line from a "
            "platform /hardness report, so the anchor share target is unverified.")
    else:
        add("budget.hard_mode", "PASS", f"Mode {mode}: the {_pct(loss)} loss figure comes from platform /hardness "
            "reports.")

    group_of = {habit: number for number, habit in enumerate(sorted(by_habit), 1)}
    summary_units = []
    for unit in budget["units"]:
        entry = {"id": unit["id"], "role": unit["role"], "carrier": str(unit.get("carrier") or ""),
                 "mechanism": str(unit.get("mechanism") or "")}
        habit, decider = unit.get("habit"), unit.get("decider")
        entry["habit"] = "/".join(habit_key(habit)) if isinstance(habit, dict) else ""
        entry["decider"] = ""
        if isinstance(decider, dict):
            place = {True: "injected", False: "base"}.get(decider.get("injected"), "")
            entry["decider"] = (f"{decider.get('service', '')} {decider.get('record_id', '')}"
                                + (f" ({place})" if place else "")).strip()
        entry["find_rate"] = list(unit["find_rate"]) if _range_ok(unit.get("find_rate")) else []
        if unit["role"] == "realism":
            entry.update(rows=[], weight=0.0, share=0.0, habit_group=None)
        else:
            mine = next(u for u in units if u["id"] == unit["id"])
            entry.update(rows=[{"id": rid, "weight": float(_frac(w))} for rid, w in mine["rows"].items()],
                         weight=float(mine["weight"]), share=float(mine["share"]), habit_group=group_of[mine["habit"]])
        summary_units.append(entry)
    summary = {
        "cap": float(cap), "mode_loss": float(loss), "weight_source": source, "total_weight": float(total),
        "undesigned_loss": [float(undesigned[0]), float(undesigned[1])],
        "units": summary_units,
        "habit_groups": [{"group": group_of[habit], "habit": "/".join(habit),
                          "units": [u["id"] for u in members]} for habit, members in sorted(by_habit.items())],
        "anchors": {"units": len(anchors), "causes": len(causes), "share": float(anchor_share),
                    "share_needed": float(need_share),
                    "largest_cause_share": float(max([share for _, share in cause_shares] or [Fraction(0)])),
                    "highest_find_rate": max([unit["hi"] for unit in anchors] or [0.0]),
                    "failed_rules": [name for name, _ in anchor_failed]},
        "variance": {"units": len(variance), "habits": len(variance_habits), "habits_in_window": len(good_habits),
                     "habits_needed": need_units, "share": float(coin_share)},
        "simulation": sim,
    }
    return _result(checks, mode, bound_to, summary)


def evaluate(task_dir, budget_path=None, *, policy=None) -> dict:
    """Check the budget of one task folder. Reads the budget, its basis file, 09_Rubrics.json and the task context;
    writes nothing. Returns the --json object."""
    from stage_gate import slot_path
    task_dir = Path(task_dir)
    path = Path(budget_path) if budget_path else slot_path(task_dir, BUDGET_NAME)
    if not path.is_file():
        return _schema_failure(f"{_rel(path, task_dir)} not found. Write the budget at /create-scenario; "
                               f"`difficulty_budget.py template --task-dir <task>` prints a starter.")
    bound = {_rel(path, task_dir): _sha256(path)}
    try:
        budget = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        return _schema_failure(f"{_rel(path, task_dir)} is not valid JSON ({str(error)[:120]}).", None, bound)
    basis = rubric = None
    if isinstance(budget, dict) and budget.get("weight_basis") in BASIS_FILES:
        basis = read_basis(task_dir, budget["weight_basis"])
        if basis.get("rows") is not None:
            bound[_rel(basis["path"], task_dir)] = _sha256(basis["path"])
        if budget.get("rubric_rows"):
            rubric = basis if budget["weight_basis"] == "rubric" else read_basis(task_dir, "rubric")
            if rubric.get("rows") is not None:
                bound[_rel(rubric["path"], task_dir)] = _sha256(rubric["path"])
    return evaluate_budget(budget, basis, rubric, _context(task_dir), policy, bound)


def _context(task_dir) -> dict:
    """{'mode': assigned difficulty mode} or {'skip': why no V3 context loads}."""
    try:
        import task_context
        return {"mode": task_context.load_context(str(task_dir))["difficulty_mode"]}
    except Exception as error:  # noqa: BLE001  (any load failure is a SKIP with its reason, never a crash)
        return {"skip": " ".join(str(error).split())[:200] or type(error).__name__}


# ------------------------------------------------------------------ output

def render_text(result) -> str:
    lines = [f"DIFFICULTY BUDGET ({result.get('mode') or 'unknown mode'}): {result['verdict']}"]
    lines += [f"[{check['status']}] {check['id']}: {check['detail']}" for check in result["checks"]]
    return "\n".join(lines)


def table_markdown(result) -> str:
    """The budget as a Markdown table for 01_Scenario_Design.md (needs a result with a `budget` summary)."""
    summary = result["budget"]
    lines = ["| Unit | Role | Carrier | Decider | Habit | Find rate | Rows (weight) | Weight share |",
             "|---|---|---|---|---|---|---|---|"]
    for unit in summary["units"]:
        rate = "-".join(f"{value:.2f}" for value in unit["find_rate"]) or "n/a"
        if unit["role"] == "realism":
            rows, share = "not counted", "0% (realism)"
        else:
            rows = ", ".join(f"{row['id']} ({_fmt(row['weight'])})" for row in unit["rows"]) or "none"
            share = f"{_pct(unit['share'])} ({_fmt(unit['weight'])} of {_fmt(summary['total_weight'])})"
        cells = [unit["id"], unit["role"], unit["carrier"] or "n/a", unit["decider"] or "n/a",
                 unit["habit"].replace("/", " / ") or "n/a", rate, rows, share]
        lines.append("| " + " | ".join(str(cell).replace("|", "\\|") for cell in cells) + " |")
    a, v = summary["anchors"], summary["variance"]
    lines += ["", f"Mode {result['mode']} (cap {_pct(summary['cap'])}, loss {_pct(summary['mode_loss'])}); weights "
              f"from {summary['weight_source']}, total {_fmt(summary['total_weight'])}. Anchors: {_pct(a['share'])} "
              f"of weight from {a['causes']} cause(s) (needs {_pct(a['share_needed'])}). Coin-flip units: "
              f"{_pct(v['share'])} of weight over {v['habits']} independent habit(s), {v['habits_in_window']} inside "
              f"the find-rate window (needs {v['habits_needed']})."]
    return "\n".join(lines)


def template(task_dir) -> tuple:
    """(starter budget, notes). Built from the hardness manifest and the surface; nothing is written."""
    from stage_gate import slot_path
    task_dir = Path(task_dir)
    notes = []
    manifest_path = next((p for p in (slot_path(task_dir, name) for name in MANIFEST_NAMES) if p.is_file()), None)
    if manifest_path is None:
        raise ValueError(f"no {' or '.join(MANIFEST_NAMES)} in {task_dir}; the template needs the mechanism portfolio")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    portfolio = manifest.get("mechanism_portfolio") if isinstance(manifest, dict) else None
    if not isinstance(portfolio, list) or not portfolio:
        raise ValueError(f"{manifest_path.name} has no mechanism_portfolio")
    surface = read_basis(task_dir, "surface")
    if surface.get("rows") is None:
        raise ValueError(f"{surface['error']}; the template needs the surface weights")
    notes.append(f"manifest: {manifest_path.name}; surface: {surface['file']} ({len(surface['rows'])} slots)")
    context = _context(task_dir)
    mode = context.get("mode") or ""
    if not mode:
        assigned = manifest.get("assignment_context")
        mode = str(assigned.get("difficulty_mode") or "") if isinstance(assigned, dict) else ""
        notes.append(f"mode {mode or 'left empty'}: no V3 task context ({context.get('skip')})")
    try:
        revision = json.loads(surface["path"].read_text(encoding="utf-8")).get("revision")
    except (OSError, ValueError, AttributeError):
        revision = None
    units = []
    for number, mechanism in enumerate(portfolio, 1):
        if not isinstance(mechanism, dict):
            continue
        decides = [sid for sid in mechanism.get("decides") or [] if isinstance(sid, str)]
        missing = [sid for sid in decides if sid not in surface["rows"]]
        if missing:
            notes.append(f"U{number} ({mechanism.get('id')}): decides slots not on the surface, left out: "
                         + ", ".join(missing))
        units.append({"id": f"U{number}", "role": "", "cause": "", "cause_key": "", "carrier": "",
                      "habit": {"service": "", "action": ""},
                      "decider": {"service": "", "record_id": "", "container": "", "injected": None},
                      "find_rate": [], "find_rate_basis": "",
                      "rows": [{"id": sid, "weight": surface["rows"][sid]} for sid in decides
                               if sid in surface["rows"]],
                      "mechanism": str(mechanism.get("id") or "")})
    budget = {"schema": SCHEMA, "design_id": "D1", "revision": revision if _text(revision) else "rev1",
              "mode": mode, "weight_basis": "surface",
              "total_weight": float(sum(_frac(w) for w in surface["rows"].values())),
              "undesigned_loss": [0.0, 0.0], "units": units}
    if budget["total_weight"] == int(budget["total_weight"]):
        budget["total_weight"] = int(budget["total_weight"])
    notes.append("fill for every unit: role (anchor, variance or realism), cause, cause_key, carrier, habit, "
                 "decider, find_rate, find_rate_basis; set undesigned_loss; then run check")
    return budget, notes


# ------------------------------------------------------------------ derive and backtest

def derive(data, mode=None, source=None) -> dict:
    """A budget built after the fact from a baseline matrix (keys rubrics[id, weight], rollouts[status, results]).

    Rubric rows with the same pass/fail vector over the completed runs are one unit. A group that fails every run is
    an anchor with find rate [0, 0]; any other failing group is a variance unit centred on the share of runs that
    passed it. Invalid rubrics are left out and judge corrections applied, as in the view difficulty_stats scores.
    """
    rubrics = [r for r in data.get("rubrics") or [] if isinstance(r, dict) and r.get("valid") is not False]
    completed = [ro for ro in data.get("rollouts") or [] if isinstance(ro, dict) and ro.get("status") == "completed"]
    if not rubrics or not completed:
        raise ValueError("derive needs rubrics and at least one completed rollout")
    results = [dict(ro.get("results") or {}, **(ro.get("judge_corrections") or {})) for ro in completed]
    vectors = {}
    for rubric in rubrics:
        try:
            vector = tuple(bool(result[rubric["id"]]) for result in results)
        except KeyError:
            raise ValueError(f"a completed rollout has no result for rubric {rubric['id']}") from None
        if not all(vector):
            vectors.setdefault(vector, []).append(rubric)
    runs = len(completed)
    units = []
    for number, (vector, rows) in enumerate(vectors.items(), 1):
        passed = sum(vector)
        uid = f"U{number}"
        if passed == 0:
            role, rate = "anchor", [0.0, 0.0]
        else:
            share = passed / runs
            role = "variance"
            rate = [round(max(0.0, share - DERIVE_HALF_RANGE), 4), round(min(1.0, share + DERIVE_HALF_RANGE), 4)]
        units.append({
            "id": uid, "role": role,
            "cause": f"rows that failed together in {runs - passed} of {runs} completed runs",
            "cause_key": f"derived_{uid.lower()}", "carrier": "other:derived",
            "habit": {"service": "derived", "action": uid},
            "decider": {"service": "derived", "record_id": f"derived:{uid}", "container": "", "injected": False},
            "find_rate": rate, "find_rate_basis": f"observed: passed in {passed} of {runs} completed runs",
            "observed_passes": passed, "observed_runs": runs,
            "rows": [{"id": row["id"], "weight": row["weight"]} for row in rows], "mechanism": ""})
    mode = mode or data.get("difficulty_mode")
    return {"schema": SCHEMA, "design_id": "derived", "revision": "derived", "mode": mode, "weight_basis": "rubric",
            "total_weight": sum(r["weight"] for r in rubrics), "undesigned_loss": [0.0, 0.0], "units": units,
            "derived_from": {"source": source or "", "completed_runs": runs,
                             "errored_runs": len(data.get("rollouts") or []) - runs, "rubrics": len(rubrics)}}


def check_derived(data, mode=None, policy=None, budget=None) -> dict:
    """derive() then every check, with the matrix's own rubric rows as the basis."""
    budget = budget or derive(data, mode)
    rows = {r["id"]: r["weight"] for r in data["rubrics"] if isinstance(r, dict) and r.get("valid") is not False}
    return evaluate_budget(budget, {"rows": rows, "file": "the baseline matrix"}, None,
                           {"skip": "derived from a baseline, not a task folder"}, policy)


def _is_matrix(data) -> bool:
    return (isinstance(data, dict) and isinstance(data.get("rubrics"), list) and isinstance(data.get("rollouts"), list)
            and bool(data["rubrics"]) and bool(data["rollouts"])
            and all(isinstance(r, dict) and "id" in r and "weight" in r for r in data["rubrics"])
            and all(isinstance(ro, dict) and "status" in ro for ro in data["rollouts"]))


def _assigned_mode(path, stop) -> str | None:
    """The difficulty mode written in the nearest 00_Assigments.md above `path` (inside `stop`), or None."""
    stop = Path(stop).resolve()
    for parent in Path(path).resolve().parents:
        assignment = parent / "00_Assigments.md"
        if assignment.is_file():
            found = re.search(r"(?im)^\s*difficulty_mode:\s*(easy|medium|hard)\b",
                              assignment.read_text(encoding="utf-8", errors="replace"))
            return found.group(1).lower() if found else None
        if parent == stop:
            break
    return None


def find_baselines(archives) -> list:
    """Every baseline matrix under the archives: the final 12_difficulty_input.json of each task, any other stored
    JSON with rubrics and rollouts, and, for a task that kept no matrix, one rebuilt in memory from its verifier
    results. Each entry has task, path, kind (final | stored | rebuilt) and data or error."""
    root = Path(archives)
    found = []
    for task in sorted(p for p in root.iterdir() if p.is_dir()):
        final = task / "task_inputs" / "Working_Files" / "12_difficulty_input.json"
        paths = []
        for folder, dirs, names in os.walk(task):
            dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
            paths += [Path(folder) / name for name in sorted(names) if name.endswith(".json")]
        for path in ([final] if final.is_file() else []) + [p for p in paths if p != final]:
            try:
                if path.stat().st_size > MAX_MATRIX_BYTES:
                    continue
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            if '"rollouts"' not in text or '"rubrics"' not in text:
                continue
            try:
                data = json.loads(text)
            except ValueError:
                continue
            if _is_matrix(data):
                found.append({"task": task.name, "path": path, "kind": "final" if path == final else "stored",
                              "data": data})
        inputs = task / "task_inputs"
        verifier, rubrics = inputs / "10_Baseline_Verifier_Results.md", inputs / RUBRIC_NAME
        trajectories = inputs / "07_Baseline_Trajectories"
        if not final.is_file() and verifier.is_file() and verifier.stat().st_size and rubrics.is_file() \
                and trajectories.is_dir():
            entry = {"task": task.name, "path": verifier, "kind": "rebuilt"}
            try:
                entry["data"], _ = stats.build(verifier, rubrics, trajectories, "long-horizon", spec_version="V2")
            except (ValueError, KeyError, OSError, TypeError) as error:
                entry["error"] = " ".join(str(error).split())[:200]
            found.append(entry)
    return found


def _fingerprint(data) -> str:
    body = [[(r.get("id"), r.get("weight"), r.get("valid")) for r in data["rubrics"]],
            [(ro.get("status"), sorted((ro.get("results") or {}).items()),
              sorted((ro.get("judge_corrections") or {}).items())) for ro in data["rollouts"]]]
    return hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()


def real_gates(data, mode) -> tuple:
    """(the four baseline gates, the per-run weighted pass rates) from difficulty_stats.compute under the V3 rules
    for `mode`."""
    matrix = json.loads(json.dumps(data))
    matrix["spec_version"], matrix["difficulty_mode"] = "V3", mode
    matrix.pop("difficulty_cap", None)
    matrix.setdefault("task_type", "long-horizon")
    computed = stats.compute(matrix)
    gates = computed["gates"]
    names = {"average": "avg_weighted_pass_rate", "full_passes": "pass_at_1", "signature": "failure_patterns",
             "spread": "per_rollout_sd"}
    return ({key: {"pass": gates[name]["verdict"].startswith("PASS"), "value": gates[name]["value"]}
             for key, name in names.items()}, [run["weighted_pass_rate"] for run in computed["per_rollout"]])


PAIRS = (("budget.average", "average"), ("budget.full_passes", "full_passes"), ("budget.signature", "signature"),
         ("budget.spread", "spread"), ("budget.variance", "signature"))
BACKTEST_CHECKS = ("budget.average", "budget.full_passes", "budget.signature", "budget.spread", "budget.variance",
                   "budget.anchors")
NOTE = ("This is a calibration test of the thresholds on budgets derived after the fact from real baselines. It is "
        "not proof that a budget written at design time predicts the outcome.")


def backtest(archives=None, policy=None) -> dict:
    """Derive and check a budget for every stored baseline and set the result next to the real gates."""
    archives = Path(archives or ARCHIVES)
    policy = policy or load_policy()
    rows, skipped, seen = [], [], {}
    for entry in find_baselines(archives):
        name = Path(entry["path"]).resolve().relative_to(archives.resolve()).as_posix()
        if entry.get("error"):
            skipped.append({"baseline": name, "reason": f"could not rebuild the matrix: {entry['error']}"})
            continue
        data = entry["data"]
        legacy = data.get("spec_version") != "V3"
        mode = data.get("difficulty_mode") if not legacy else None
        mode = mode or _assigned_mode(entry["path"], archives)
        if mode not in stats.DIFFICULTY_CAPS:
            skipped.append({"baseline": name, "reason": "no difficulty mode in the matrix or in 00_Assigments.md"})
            continue
        fingerprint = _fingerprint(data)
        if fingerprint in seen:
            skipped.append({"baseline": name, "reason": f"same matrix as {seen[fingerprint]}"})
            continue
        try:
            real, rates = real_gates(data, mode)
            budget = derive(data, mode)
            result = check_derived(data, mode, policy, budget)
        except (ValueError, KeyError, TypeError) as error:
            skipped.append({"baseline": name,
                            "reason": "not a scorable six-run baseline: " + " ".join(str(error).split())[:160]})
            continue
        seen[fingerprint] = name
        status = {check["id"]: check["status"] for check in result["checks"]}
        summary = result["budget"]
        sim = summary["simulation"]
        passes = {}                                   # variance units by the number of runs that passed them
        for unit in budget["units"]:
            if unit["role"] == "variance":
                passes[unit["observed_passes"]] = passes.get(unit["observed_passes"], 0) + 1
        rarely = sum(row["weight"] for unit in budget["units"] if unit["observed_passes"] <= 1
                     for row in unit["rows"])        # rows that at most one run passed
        mode_loss = float(policy["mode_loss"][mode])
        rows.append({
            "baseline": name, "task": entry["task"], "kind": entry["kind"], "mode": mode,
            "rules": "V3 matrix" if not legacy else "V2 matrix re-scored under V3 rules with the assigned mode",
            "completed_runs": len(rates), "real": real, "all_real_pass": all(g["pass"] for g in real.values()),
            "runs_losing_mode_loss": sum(1 for rate in rates if 1 - rate >= mode_loss - stats.EPS),
            "budget": {cid: status[cid] for cid in BACKTEST_CHECKS},
            "probabilities": {key: [sim["lo"][key], sim["hi"][key]] for key in
                              ("average", "full_passes", "signature", "signature_one_error")},
            "probabilities_at_observed_rates": {key: sim["mid"][key] for key in
                                                ("average", "full_passes", "signature", "signature_one_error")},
            "spread_probability": [sim["lo"]["spread"], sim["mid"]["spread"], sim["hi"]["spread"]],
            "agree": {cid: (status[cid] == "PASS") == real[gate]["pass"] for cid, gate in PAIRS},
            "rarely_passed_share": rarely / budget["total_weight"],
            "units": {"anchor": summary["anchors"]["units"], "variance": summary["variance"]["units"],
                      "variance_in_window": summary["variance"]["habits_in_window"],
                      "variance_by_runs_passed": {str(k): passes[k] for k in sorted(passes)}},
            "anchors": summary["anchors"], "coin_flip_share": summary["variance"]["share"]})
    out = {"tool": TOOL, "version": VERSION, "command": "backtest", "note": NOTE,
           "archives": archives.resolve().relative_to(WS).as_posix() if _inside(archives, WS) else str(archives),
           "baselines": rows, "skipped": skipped}
    out["summary"] = _backtest_summary(rows, policy)
    # Other stored matrices are earlier or draft scorings of a task that also has a final one: not independent.
    out["summary_one_per_task"] = _backtest_summary([row for row in rows if row["kind"] != "stored"], policy)
    disagreements = sum(1 for row in rows for ok in row["agree"].values() if not ok)
    out["verdict"] = "FAIL" if not rows else "WARN" if disagreements else "PASS"
    return out


def _inside(path, root) -> bool:
    try:
        Path(path).resolve().relative_to(Path(root).resolve())
    except ValueError:
        return False
    return True


def _backtest_summary(rows, policy) -> dict:
    passing = [row for row in rows if row["all_real_pass"]]
    missing = [row for row in rows if not row["all_real_pass"]]
    per_check = {}
    for cid in BACKTEST_CHECKS:
        gate = dict(PAIRS).get(cid)
        per_check[cid] = {
            "pass_on_real_all_pass": sum(1 for row in passing if row["budget"][cid] == "PASS"),
            "real_all_pass": len(passing),
            "not_pass_on_real_miss": sum(1 for row in missing if row["budget"][cid] != "PASS"),
            "real_miss": len(missing),
            "paired_real_gate": gate,
            "agrees_with_paired_gate": sum(1 for row in rows if row["agree"][cid]) if gate else None,
            "baselines": len(rows),
            "disagrees_on": [row["baseline"] for row in rows if gate and not row["agree"][cid]]}
    # What the variance rule would need to agree with the real signature gate.
    need = int(policy["variance_min_units"])
    sweep = []
    for label, admitted in (("exactly 3 of 6 runs (the policy window 0.35-0.65)", {3}),
                            ("2 to 4 of 6 runs (window about 0.18-0.82)", {2, 3, 4}),
                            ("1 to 5 of 6 runs (any unit that is sometimes found, sometimes missed)", {1, 2, 3, 4, 5})):
        for minimum in range(need, 0, -1):
            def passes(row, admitted=admitted, minimum=minimum):
                scale = 6.0 / max(row["completed_runs"], 1)
                counted = sum(n for k, n in row["units"]["variance_by_runs_passed"].items()
                              if round(int(k) * scale) in admitted)
                return counted >= minimum
            sweep.append({"units_counted_when_passed_in": label, "min_units": minimum,
                          "real_signature_pass_and_rule_pass": sum(1 for r in rows
                                                                   if r["real"]["signature"]["pass"] and passes(r)),
                          "real_signature_pass": sum(1 for r in rows if r["real"]["signature"]["pass"]),
                          "real_signature_fail_and_rule_fail": sum(1 for r in rows if not
                                                                   r["real"]["signature"]["pass"] and not passes(r)),
                          "real_signature_fail": sum(1 for r in rows if not r["real"]["signature"]["pass"])})
    anchors = {"baselines_with_an_anchor": sum(1 for row in rows if row["units"]["anchor"]),
               "share_rule_met": sum(1 for row in rows if "share" not in row["anchors"]["failed_rules"]),
               "share_rule_met_and_real_all_pass": sum(1 for row in passing
                                                       if "share" not in row["anchors"]["failed_rules"]),
               "share_rule_met_counting_rarely_passed_rows": sum(
                   1 for row in rows if row["rarely_passed_share"] >= row["anchors"]["share_needed"] - stats.EPS),
               "max_share_rule_met": sum(1 for row in rows if "max_share" not in row["anchors"]["failed_rules"]),
               "causes_rule_met": sum(1 for row in rows if "causes" not in row["anchors"]["failed_rules"]),
               "every_run_lost_the_mode_loss": sum(1 for row in rows
                                                   if row["runs_losing_mode_loss"] == row["completed_runs"]),
               "baselines": len(rows)}
    # The probability each simulated check gave, split by what the real gate did: the cut-off that would agree.
    need_p, warn_below = float(policy["pass_probability"]), float(policy["spread_warn_below"])
    cutoffs = {}
    for cid, gate in PAIRS[:4]:
        key = gate
        if cid == "budget.spread":
            worst = {row["baseline"]: min(row["spread_probability"]) for row in rows}
            observed = {row["baseline"]: row["spread_probability"][1] for row in rows}
            threshold = warn_below
        else:
            worst = {row["baseline"]: min(row["probabilities"][key]) for row in rows}
            observed = {row["baseline"]: row["probabilities_at_observed_rates"][key] for row in rows}
            threshold = need_p
        real_pass = [row["baseline"] for row in rows if row["real"][gate]["pass"]]
        real_fail = [row["baseline"] for row in rows if not row["real"][gate]["pass"]]
        cutoffs[cid] = {
            "threshold": threshold, "real_pass": len(real_pass), "real_fail": len(real_fail),
            "lowest_where_real_passed": min([worst[name] for name in real_pass], default=None),
            "highest_where_real_failed": max([worst[name] for name in real_fail], default=None),
            "agrees_at_observed_rates": sum(1 for row in rows if (observed[row["baseline"]] >= threshold - 1e-12)
                                            == row["real"][gate]["pass"])}
    return {"baselines": len(rows), "real_all_pass": len(passing), "real_miss": len(missing),
            "by_kind": {kind: sum(1 for row in rows if row["kind"] == kind) for kind in ("final", "stored", "rebuilt")},
            "per_check": per_check, "probability_cutoffs": cutoffs, "variance_rule_sweep": sweep,
            "anchor_rules": anchors}


def render_backtest(report) -> str:
    rows, summary = report["baselines"], report["summary"]
    lines = [f"DIFFICULTY BUDGET BACKTEST ({len(rows)} baselines): {report['verdict']}", report["note"], "",
             f"Archives: {report['archives']}. Found {summary['by_kind']['final']} final 12_difficulty_input.json, "
             f"{summary['by_kind']['stored']} other stored matrices and {summary['by_kind']['rebuilt']} rebuilt in "
             "memory from 10_Baseline_Verifier_Results.md (file-name run association, not verified). Real gates are "
             "difficulty_stats.compute under the V3 rules; a V2 matrix is re-scored with the mode in its "
             "00_Assigments.md.", "", "Baselines"]
    for number, row in enumerate(rows, 1):
        lines.append(f"  {number}. [{row['kind']}] {row['baseline']} ({row['mode']}; {row['rules']})")
    if report["skipped"]:
        lines += ["", "Not used"] + [f"  - {item['baseline']}: {item['reason']}" for item in report["skipped"]]

    def pair(row, cid, gate, probs=None):
        real = row["real"][gate]
        value = (real["value"].split(" (pairwise")[0].replace(" pattern(s); largest", " patterns, largest")
                 if gate == "signature" else real["value"].split(" (")[0].split(";")[0])
        text = f"real {'PASS' if real['pass'] else 'FAIL'} ({value}) / budget {row['budget'][cid]}"
        if probs:
            text += " (" + "-".join(f"{p:.2f}" for p in probs) + ")"
        return text + (" / agree" if row["agree"][cid] else " / DIFFER")

    lines += ["", "Each cell: the real gate (its value) / the budget check (probability at the low-high find-rate "
              "ends; spread: low-middle-high) / whether they agree. Units a/v = derived anchor / variance units, "
              "with the number of coin-flip habits inside the find-rate window in brackets.", "",
              "| # | Mode | Units a/v (in window) | Average | Full passes | Signature | SD vs budget.spread | "
              "budget.variance vs real signature | budget.anchors |", "|---|---|---|---|---|---|---|---|---|"]
    for number, row in enumerate(rows, 1):
        units = row["units"]
        anchors = row["anchors"]
        lines.append("| " + " | ".join([
            str(number), row["mode"], f"{units['anchor']}/{units['variance']} ({units['variance_in_window']})",
            pair(row, "budget.average", "average", row["probabilities"]["average"]),
            pair(row, "budget.full_passes", "full_passes", row["probabilities"]["full_passes"]),
            pair(row, "budget.signature", "signature", row["probabilities"]["signature"]),
            pair(row, "budget.spread", "spread", row["spread_probability"]),
            f"{row['budget']['budget.variance']}" + (" / agree" if row["agree"]["budget.variance"] else " / DIFFER"),
            f"{row['budget']['budget.anchors']} (share {_pct(anchors['share'])} of {_pct(anchors['share_needed'])} "
            f"needed; failed: {', '.join(anchors['failed_rules']) or 'none'}; {row['runs_losing_mode_loss']} of "
            f"{row['completed_runs']} runs lost the mode's loss)"]) + " |")
    one = report["summary_one_per_task"]
    lines += ["", f"Summary, one baseline per task ({one['baselines']}: the final or rebuilt matrix of each task)"]
    lines += _summary_lines(one, full=True)
    lines += ["", f"Summary, all {summary['baselines']} matrices (the {summary['by_kind']['stored']} other stored "
              "matrices are earlier or draft scorings of tasks counted above, so they are not independent)"]
    lines += _summary_lines(summary, full=False)
    return "\n".join(lines)


def _summary_lines(summary, full) -> list:
    lines = [f"{summary['real_all_pass']} of {summary['baselines']} baselines passed all four real gates (average, "
             f"full passes, signature, SD); {summary['real_miss']} missed at least one.",
             "| Budget check | PASS on baselines that passed all real gates | FAIL (WARN for spread) on baselines "
             "that missed a gate | Agrees with its paired real gate |", "|---|---|---|---|"]
    for cid, item in summary["per_check"].items():
        paired = (f"{item['agrees_with_paired_gate']} of {item['baselines']} ({item['paired_real_gate']})"
                  if item["paired_real_gate"] else "no baseline gate to pair with")
        lines.append(f"| {cid} | {item['pass_on_real_all_pass']} of {item['real_all_pass']} | "
                     f"{item['not_pass_on_real_miss']} of {item['real_miss']} | {paired} |")
    if not full:
        return lines
    lines += ["", "Probability cut-offs (lowest end of the range, per baseline, split by the real gate)",
              "| Budget check | Policy cut-off | Lowest probability where the real gate passed | Highest where it "
              "failed | Agrees when scored at the observed find rates (no range) |", "|---|---|---|---|---|"]

    def prob(value):
        return "none" if value is None else f"{value:.3f}"

    for cid, item in summary["probability_cutoffs"].items():
        lines.append(f"| {cid} | {item['threshold']:.2f} | {prob(item['lowest_where_real_passed'])} "
                     f"({item['real_pass']} baselines) | {prob(item['highest_where_real_failed'])} "
                     f"({item['real_fail']} baselines) | {item['agrees_at_observed_rates']} of "
                     f"{summary['baselines']} |")
    lines += ["A check agrees with every real PASS only if its cut-off is at or under the lowest probability shown, "
              "and still catches every real FAIL only if the cut-off is above the highest.",
              "", "Variance rule against the real signature gate (units counted by how many of six runs passed them)",
              "| Units counted when passed in | Min units | Rule PASS where the real signature gate passed | Rule FAIL "
              "where it failed |", "|---|---|---|---|"]
    for item in summary["variance_rule_sweep"]:
        lines.append(f"| {item['units_counted_when_passed_in']} | {item['min_units']} | "
                     f"{item['real_signature_pass_and_rule_pass']} of {item['real_signature_pass']} | "
                     f"{item['real_signature_fail_and_rule_fail']} of {item['real_signature_fail']} |")
    a = summary["anchor_rules"]
    lines += ["", f"Anchor rules on derived budgets: {a['baselines_with_an_anchor']} of {a['baselines']} baselines "
              f"have rows that fail every run. The share rule (mode loss + margin) is met in {a['share_rule_met']} "
              f"({a['share_rule_met_and_real_all_pass']} of the {summary['real_all_pass']} that passed all real "
              f"gates), and in {a['share_rule_met_counting_rarely_passed_rows']} when rows that at most one run "
              f"passed are counted too. The single-cause limit is met in {a['max_share_rule_met']}; the two-cause "
              f"rule in {a['causes_rule_met']}. In {a['every_run_lost_the_mode_loss']} of {a['baselines']} baselines "
              "every completed run lost at least the mode's loss. Rows that fail every run share one pass/fail "
              "vector, so a derived budget has at most one anchor and can never show two causes: the two-cause rule "
              "cannot be calibrated from a matrix."]
    return lines


# ------------------------------------------------------------------ self-test

def _fixture(tmp, budget=None, surface=None) -> Path:
    """A task folder with a surface and a budget that passes every check (test and self-test fixture)."""
    task = Path(tmp) / "task"
    work = task / "Working_Files"
    work.mkdir(parents=True, exist_ok=True)
    (work / BASIS_FILES["surface"]).write_text(json.dumps(surface or good_surface(), indent=1), encoding="utf-8")
    (work / BUDGET_NAME).write_text(json.dumps(budget or good_budget(), indent=1), encoding="utf-8")
    return task


def good_surface() -> dict:
    """100 weight: two anchor pairs (5 + 3), four coin-flip triples (5 + 5 + 5), 24 always-pass weight."""
    slots = []
    for unit in ("A1", "A2"):
        slots += [{"id": f"{unit}a", "weight": 5}, {"id": f"{unit}b", "weight": 3}]
    for unit in ("V1", "V2", "V3", "V4"):
        slots += [{"id": f"{unit}{letter}", "weight": 5} for letter in "abc"]
    slots += [{"id": f"P{n}", "weight": 3} for n in range(1, 9)]
    return {"kind": "gradable-surface", "revision": "rev1", "slots": slots}


def good_budget() -> dict:
    carriers = ("reply_under_unrelated_parent", "email_reply_via_get_thread", "de_named_correction_reply",
                "dm_with_non_owner", "off_service_record", "non_set_ticket")
    habits = (("slack", "thread_replies"), ("gmail", "get_thread"), ("slack", "dm_history"), ("linear", "get_issue"),
              ("gdrive", "get_file"), ("github", "get_pull_request"))
    units = []
    for number, uid in enumerate(("A1", "A2", "V1", "V2", "V3", "V4")):
        anchor = uid.startswith("A")
        rows = ([{"id": f"{uid}a", "weight": 5}, {"id": f"{uid}b", "weight": 3}] if anchor
                else [{"id": f"{uid}{letter}", "weight": 5} for letter in "abc"])
        units.append({"id": uid, "role": "anchor" if anchor else "variance", "cause": f"cause of {uid}",
                      "cause_key": f"cause_{uid.lower()}", "carrier": carriers[number],
                      "habit": {"service": habits[number][0], "action": habits[number][1]},
                      "decider": {"service": habits[number][0], "record_id": f"rec-{uid}", "container": "",
                                  "injected": True},
                      "find_rate": [0.0, 0.15] if anchor else [0.4, 0.6], "find_rate_basis": "self-test",
                      "rows": rows, "mechanism": uid})
    return {"schema": SCHEMA, "design_id": "D1", "revision": "rev1", "mode": "easy", "weight_basis": "surface",
            "total_weight": 100, "undesigned_loss": [0.0, 0.05], "units": units}


def _self_test() -> int:
    import contextlib
    import io
    import selftest_sandbox
    covered = []
    with selftest_sandbox.scratch_tmp("difficulty_budget_selftest_") as tmp:
        task = _fixture(tmp)
        good = evaluate(task)
        status = {check["id"]: check["status"] for check in good["checks"]}
        assert [check["id"] for check in good["checks"]] == list(CHECK_IDS), good["checks"]
        assert good["verdict"] == "PASS" and status["budget.context"] == "SKIP", render_text(good)
        assert all(value == "PASS" for cid, value in status.items() if cid != "budget.context"), render_text(good)
        assert sorted(good["bound_to"]) == ["Working_Files/01_Difficulty_Budget.json",
                                            "Working_Files/01_Gradable_Surface.json"], good["bound_to"]
        assert evaluate(task) == good                                    # same input, same output
        covered.append("good budget")

        quick = dict(load_policy(), trials=4000)                         # enough for the planted margins

        def planted(change, cid, want="FAIL"):
            budget = good_budget()
            change(budget)
            (task / "Working_Files" / BUDGET_NAME).write_text(json.dumps(budget), encoding="utf-8")
            result = evaluate(task, policy=quick)
            got = {check["id"]: check["status"] for check in result["checks"]}[cid]
            assert got == want, (cid, got, render_text(result))
            return result

        def unit(budget, uid):
            return next(u for u in budget["units"] if u["id"] == uid)

        planted(lambda b: unit(b, "V1").update(role="trap"), "budget.schema")
        planted(lambda b: unit(b, "V1").update(find_rate=[0.7, 0.4]), "budget.schema")
        planted(lambda b: unit(b, "V1")["rows"][0].update(weight=3), "budget.rows")
        planted(lambda b: b.update(total_weight=90), "budget.rows")
        planted(lambda b: unit(b, "V2").update(carrier="decoy"), "budget.carriers")
        planted(lambda b: unit(b, "V2").update(carrier="other:a pinned post"), "budget.carriers", "WARN")
        planted(lambda b: unit(b, "V3").update(rows=unit(b, "V3")["rows"][:1]), "budget.unit_rows")
        merged = planted(lambda b: unit(b, "V4").update(habit=dict(unit(b, "V3")["habit"])), "budget.independence",
                         "WARN")
        assert {c["id"]: c["status"] for c in merged["checks"]}["budget.variance"] == "FAIL"
        planted(lambda b: unit(b, "A2").update(cause_key="cause_a1"), "budget.anchors")
        planted(lambda b: unit(b, "A1").update(find_rate=[0.0, 0.4]), "budget.anchors")
        planted(lambda b: unit(b, "V4").update(find_rate=[0.7, 0.9]), "budget.variance")
        planted(lambda b: [u.update(find_rate=[0.97, 1.0]) for u in b["units"]], "budget.full_passes")
        planted(lambda b: b.update(units=[u for u in b["units"] if u["id"] not in ("V3", "V4")]), "budget.signature")
        planted(lambda b: b.update(units=[u for u in b["units"] if u["id"] != "V4"]), "budget.signature_one_error")
        planted(lambda b: b.update(mode="hard"), "budget.hard_mode", "WARN")
        covered.append("planted defects")

        thin = good_surface()
        thin["slots"] += [{"id": f"Q{n}", "weight": 5} for n in range(1, 61)]      # 300 more always-pass weight
        (task / "Working_Files" / BASIS_FILES["surface"]).write_text(json.dumps(thin), encoding="utf-8")
        low = planted(lambda b: b.update(total_weight=400), "budget.spread", "WARN")
        assert {c["id"]: c["status"] for c in low["checks"]}["budget.average"] == "FAIL", render_text(low)
        covered.append("spread warns, never fails")

        task = _fixture(tmp)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            assert main(["check", "--task-dir", str(task)]) == 0
            assert main(["check", "--task-dir", str(task), "--json"]) == 0
            assert main(["table", "--task-dir", str(task)]) == 0
        text = out.getvalue()
        assert text.startswith("DIFFICULTY BUDGET (easy): PASS\n[PASS] budget.schema:"), text[:200]
        assert '"tool": "difficulty_budget"' in text and "| A1 | anchor |" in text, text[-600:]
        (task / "Working_Files" / BUDGET_NAME).unlink()
        with contextlib.redirect_stdout(io.StringIO()):
            assert main(["check", "--task-dir", str(task)]) == 1         # no budget file is a FAIL, not a crash
        covered.append("check, table and exit codes")

        (task / "Working_Files" / MANIFEST_NAMES[1]).write_text(json.dumps({"mechanism_portfolio": [
            {"id": "RET", "decides": ["A1a", "A1b", "nope"]}, {"id": "OFF", "decides": ["V1a", "V1b"]}]}),
            encoding="utf-8")
        before = sorted(p.name for p in (task / "Working_Files").iterdir())
        starter, notes = template(task)
        assert [u["mechanism"] for u in starter["units"]] == ["RET", "OFF"] and starter["total_weight"] == 100
        assert starter["units"][0]["rows"] == [{"id": "A1a", "weight": 5}, {"id": "A1b", "weight": 3}], starter
        assert any("nope" in note for note in notes) and schema_problems(starter)
        assert sorted(p.name for p in (task / "Working_Files").iterdir()) == before     # printed only
        covered.append("template")

    matrix = {"difficulty_mode": "easy", "rubrics": [{"id": f"R{n}", "weight": 5} for n in range(1, 9)],
              "rollouts": [{"id": f"run-{n}", "status": "completed",
                            "results": {f"R{k}": not (k <= 2 or (k in (3, 4) and n % 2) or (k == 5 and n == 1))
                                        for k in range(1, 9)}} for n in range(1, 7)]}
    derived = derive(matrix)
    assert [(u["role"], u["find_rate"], [r["id"] for r in u["rows"]]) for u in derived["units"]] == [
        ("anchor", [0.0, 0.0], ["R1", "R2"]), ("variance", [0.35, 0.65], ["R3", "R4"]),
        ("variance", [0.6833, 0.9833], ["R5"])], derived["units"]
    assert not schema_problems(derived) and check_derived(matrix)["verdict"] == "FAIL"
    covered.append("derive")

    def anchored(count, rate):
        """One always-missed anchor plus `count` coin-flip units, each flipping two rows of 15 out of 200."""
        units = [{"habit": ("s", "anchor"), "lo": 0.0, "hi": 0.0, "rows": {"A1": 5, "A2": 5}}]
        units += [{"habit": ("s", f"v{n}"), "lo": rate, "hi": rate, "rows": {f"V{n}a": 15, f"V{n}b": 15}}
                  for n in range(count)]
        return simulate(units, 200, Fraction(9, 10))["lo"]

    for count, six, five in ((4, (0.97, 1.0), (0.91, 0.98)), (3, (0.92, 0.985), (0.77, 0.88)),
                             (2, (0.72, 0.86), (0.45, 0.60))):
        for rate in (0.35, 0.5):
            got = anchored(count, rate)
            assert six[0] <= got["signature"] <= six[1], (count, rate, got)
            assert five[0] <= got["signature_one_error"] <= five[1], (count, rate, got)
    assert 0.68 <= anchored(3, 0.5)["spread"] <= 0.75, anchored(3, 0.5)
    covered.append("plan 2a sanity probabilities")
    print("self-test: ok (" + ", ".join(covered) + ")")
    return 0


# ------------------------------------------------------------------ CLI

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv or "--selftest" in argv:
        return _self_test()
    ap = argparse.ArgumentParser(prog="difficulty_budget.py",
                                 description="design-time difficulty budget check (see the module docstring)")
    sub = ap.add_subparsers(dest="command")
    for name in ("check", "table", "template"):
        p = sub.add_parser(name)
        p.add_argument("--task-dir", required=True, help="the task folder (no default)")
        if name != "template":
            p.add_argument("--budget", default=None, help=f"budget file (default: Working_Files/{BUDGET_NAME})")
        if name == "check":
            p.add_argument("--json", action="store_true")
    p = sub.add_parser("derive")
    p.add_argument("--input", required=True, help="a 12_difficulty_input.json baseline matrix")
    p.add_argument("--mode", default=None, choices=sorted(stats.DIFFICULTY_CAPS),
                   help="difficulty mode when the matrix has none")
    p.add_argument("--check", action="store_true", help="print the check of the derived budget instead of the budget")
    p = sub.add_parser("backtest")
    p.add_argument("--archives", default=str(ARCHIVES), help="folder of archived tasks")
    p.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if not args.command:
        ap.error("a command is required: check, table, template, derive or backtest (or --self-test)")
    if args.command in ("check", "table", "template") and not Path(args.task_dir).is_dir():
        ap.error(f"--task-dir {args.task_dir} is not a folder")

    if args.command == "check":
        result = evaluate(args.task_dir, args.budget)
        print(json.dumps(result, indent=2, sort_keys=True) if args.json else render_text(result))
        return 1 if result["verdict"] == "FAIL" else 0
    if args.command == "table":
        result = evaluate(args.task_dir, args.budget)
        if "budget" not in result:
            print(render_text(result), file=sys.stderr)
            return 1
        print(table_markdown(result))
        return 0
    if args.command == "template":
        try:
            budget, notes = template(args.task_dir)
        except (ValueError, OSError) as error:
            print(f"difficulty_budget: {error}", file=sys.stderr)
            return 1
        for note in notes:
            print(f"difficulty_budget: {note}", file=sys.stderr)
        print(json.dumps(budget, indent=2))
        return 0
    if args.command == "derive":
        path = Path(args.input)
        if not path.is_file():
            ap.error(f"--input {args.input} is not a file")
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if args.check:
                result = check_derived(data, args.mode)
                print(render_text(result))
                return 1 if result["verdict"] == "FAIL" else 0
            budget = derive(data, args.mode, path.name)
            if budget["mode"] not in stats.DIFFICULTY_CAPS:
                print("difficulty_budget: the matrix records no difficulty mode; pass --mode easy|medium|hard",
                      file=sys.stderr)
            print(json.dumps(budget, indent=2))
        except (ValueError, KeyError, TypeError) as error:
            print(f"difficulty_budget: cannot derive a budget from {path.name}: {error}", file=sys.stderr)
            return 1
        return 0
    if not Path(args.archives).is_dir():
        ap.error(f"--archives {args.archives} is not a folder")
    report = backtest(args.archives)
    print(json.dumps(report, indent=2, sort_keys=True) if args.json else render_backtest(report))
    return 1 if report["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())

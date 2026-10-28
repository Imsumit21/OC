#!/usr/bin/env python3
"""oracle_kit.py - the solver contract: load a task's solver, produce truth.json, and check the contract (plan §7.1).

A task's solver (`Working_Files/solver/solver.py`) turns the universe plus the injection SQL into the expected value
of every gradable output. Rules come from /create-scenario (one rule per mechanism node, each with a natural-reading
fallback); record access comes from /create-injection. The solver owns truth: truth.json, the dossier totals, Facts
for the human and the OE / rubric expected values are all read from it (Hardness_Mastery §2.6 item 14).
Read-only on its inputs, stdlib only, never executes SQL (the solver parses it through tools/base_check.parse_sql).

Solver module contract
  RULES       {rule_id: {mechanism, requirement, natural_reading, nodes[], decides[], signature?, authority[]?,
                         source?, family?, part_of?}}            rule ids are the manifest's mechanism_portfolio ids
  load_state(sql_text, revision=None) -> state
  solve(state, disable=frozenset(), degrade=frozenset(), keys_=None) -> {key: {field: value, ..., groups?, evidence}}
              disable: rule ids, or (rule, key set) pairs; degrade: operator names, or (operator, key set) pairs
  aggregates(rows) -> {"classes": {...}, "groups": {group: [keys]}}
  evidence(rows, key, field) -> [record ids]
  optional    touched(state, rule) -> keys the rule acts on · deciding(state, rule, key) -> record ids ·
              DEGRADES {operator: description} · REVISIONS · KEY_REGEX · FIELDS · CLASS_FIELD · GROUPS_FIELD
              base_route(record_id) -> {service, file, pointer, field} | None   where a base record lives in the
                          exports, so the golden check can read it through tools/hg.py records (M5)
              RULES[r] controls[] + over_application   the rule's control members (records it must leave alone) and
                          the degrade operator that over-applies the rule to them. node_verdicts reports a control
                          trial per member (OVER-APPLIED when the written value matches the operator's, else HELD),
                          never a landing
              CHANNELS {channel: {kind, degrade, members[], latent?, batch_size?, family?, rule?, source?, slots[]?,
                          preregistered?, description}}   complexity channels (kind scale · chain · delegation ·
                          synthesis · tool_surface): `degrade` is an operator solve() accepts, whole or as (operator,
                          key set), giving the values members take when the channel fails on them; a channel the solver
                          can't express (e.g. a CSV upload replaced by a native Sheet) names surface `slots` instead.
                          latent member · batch · run (default by kind). node_verdicts reports each per run (FAILED /
                          HELD); hardness_forecast models them (F1), with rates pooled across tasks by `family`
                          (default: the kind)

Contract checks (all blocking at /create-injection S4b)
  interface        the attributes above; every rule names mechanism, requirement and natural_reading
  deterministic    two fresh solves (forward and reverse key order) give identical canonical JSON, and so do fresh
                   processes with PYTHONHASHSEED 1 and 2 (set or hash order must not leak into the output; M5)
  regression       the previous revision's truth on the previous SQL: the stored file reproduced byte for byte by the
                   solver at that revision, and the current rules on the previous SQL give the same fields and groups
  rules_nodes      rules <-> manifest mechanism_portfolio one-to-one, every node a manifest trap or chain; a legacy
                   manifest without a portfolio: every rule node exists, manifest traps with no rule are listed
  slots            every direct and aggregate slot of the gradable surface reads a solver value
  controls         every declared control member is a solver key; every over-application operator and channel
                   degrade is accepted by solve() and moves a value of at least one of its members (a dead operator
                   can never record a trial or a failure); a channel's kind is known
  golden           a deterministic sample of golden values spot-verified against the records that decide them (the
                   evidence ids exist in the SQL and the value appears in the record); base records the solver routes
                   (base_route) are read through tools/hg.py records and checked the same way (an absent record or a
                   value not in it FAILs); unrouted base records are listed as unverified
  digest           the manifest's solver {path, digest} matches the file

Usage:
  python3 -B Task_Authoring/tools/oracle_kit.py check --task-dir DIR [--solver S] [--sql SQL] [--revision R]
      [--previous-sql P --previous-truth T] [--manifest M] [--surface S] [--json]
  python3 -B Task_Authoring/tools/oracle_kit.py truth --solver S --sql SQL [--revision R] --out truth.json
  python3 -B Task_Authoring/tools/oracle_kit.py --self-test
Exit 0 = PASS, 1 = FAIL, 2 = usage error.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def _bundle() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "difficulty_stats.py").is_file():
            return parent
    raise SystemExit("oracle_kit: cannot find the Task_Authoring bundle (no tools/difficulty_stats.py above)")


HERE = Path(__file__).resolve().parent
BUNDLE = _bundle()
for _p in (BUNDLE / "tools", HERE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

REQUIRED = ("RULES", "load_state", "solve", "aggregates", "evidence")
RULE_FIELDS = ("mechanism", "requirement", "natural_reading")
GOLDEN_SAMPLE = 12
_LOADED = {}


def load_solver(path):
    """Import a solver module by path (each path once per process)."""
    path = Path(path).resolve()
    if path in _LOADED:
        return _LOADED[path]
    name = "solver_" + hashlib.sha256(str(path).encode()).hexdigest()[:10]
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ValueError(f"{path}: not an importable solver")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    _LOADED[path] = mod
    return mod


def canonical(rows) -> str:
    return json.dumps(rows, sort_keys=True, ensure_ascii=False, separators=(",", ":"), default=sorted)


def truth(mod, sql_text: str, revision: str | None = None) -> dict:
    return mod.solve(mod.load_state(sql_text, revision))


def rule_ids(mod) -> list:
    return list(mod.RULES)


def class_field(mod) -> str:
    return getattr(mod, "CLASS_FIELD", "class")


def groups_field(mod) -> str:
    return getattr(mod, "GROUPS_FIELD", "groups")


def _strip(rows: dict, fields=None) -> dict:
    """Rows without evidence (the regression compares outputs, not the solver's bookkeeping)."""
    return {k: {f: v for f, v in r.items() if f != "evidence" and (fields is None or f in fields)} for k, r in rows.items()}


# ------------------------------------------------------------------ contract checks

def _check(out, cid, ok, detail, block=True, extra=None):
    out.append({"check": cid, "status": "PASS" if ok else ("FAIL" if block else "WARN"), "detail": detail, **(extra or {})})


def check_interface(mod, out) -> bool:
    miss = [a for a in REQUIRED if not hasattr(mod, a)]
    bad = [f"{r}:{f}" for r, v in (getattr(mod, "RULES", {}) or {}).items() for f in RULE_FIELDS
           if not str((v or {}).get(f) or "").strip()]
    _check(out, "contract.interface", not miss and not bad and bool(getattr(mod, "RULES", None)),
           ("missing " + ", ".join(miss) + "; " if miss else "") + (f"rules lacking {bad[:6]}" if bad else "")
           or f"{len(mod.RULES)} rules, each with mechanism, requirement and natural_reading; "
              f"optional: {[a for a in ('touched', 'deciding', 'DEGRADES') if hasattr(mod, a)]}")
    return not miss


CHANNEL_KINDS = ("scale", "chain", "delegation", "synthesis", "tool_surface")


def controls_of(mod, revision=None) -> dict:
    """{rule: {"members": [...], "over_application": operator or None}} for the rules that declare control members."""
    return {r: {"members": list(v.get("controls") or []), "over_application": v.get("over_application")}
            for r, v in active_rules(mod, revision).items() if v.get("controls")}


def channels_of(mod) -> dict:
    """The declared complexity channels: {channel: {kind, degrade, members, ...}}."""
    return {c: dict(v) for c, v in (getattr(mod, "CHANNELS", None) or {}).items()}


def _moved(base: dict, alt: dict, keys, fields) -> list:
    return sorted(k for k in keys if k in base and k in alt and any(base[k].get(f) != alt[k].get(f) for f in fields))


def check_controls(mod, state, rows, out, revision=None, slot_ids=None) -> None:
    """contract.controls (see the module docstring). Nothing declared: PASS."""
    ctl, ch = controls_of(mod, revision), channels_of(mod)
    if not ctl and not ch:
        _check(out, "contract.controls", True, "no control members or complexity channels declared")
        return
    problems, notes = [], []
    rules = active_rules(mod, revision)
    for r, c in ctl.items():
        missing = [k for k in c["members"] if k not in rows]
        if missing:
            problems.append(f"{r}: control members {missing[:6]} are not solver keys")
        op = c["over_application"]
        if not op:
            notes.append(f"{r}: {len(c['members'])} control(s), no over-application operator (every trial HELD)")
            continue
        fields = list(rules[r].get("decides") or []) + [class_field(mod)]
        try:
            moved = _moved(rows, mod.solve(state, degrade={op}), c["members"], fields)
        except Exception as error:  # noqa: BLE001 - a refused operator is the finding
            problems.append(f"{r}: over_application {op!r} refused by solve(): {type(error).__name__}: {error}")
            continue
        if moved:
            # a control whose over-application value is exactly the rule's ablation is not separable from the rule's
            # own error: it must not become a landing (H1 residual a)
            abl = mod.solve(state, disable={r})
            dg = mod.solve(state, degrade={op})
            same = [k for k in moved if k in abl and k in dg
                    and all(dg[k].get(f) == abl[k].get(f) for f in fields)]
            if same:
                problems.append(f"{r}: over_application {op!r} equals the rule ablation for control member(s) {same[:4]}"
                                f": the control cannot be separated from a rule error")
            else:
                notes.append(f"{r}: {len(c['members'])} control(s); {op} moves {moved}")
        else:
            problems.append(f"{r}: over_application {op!r} moves no control member's {fields}")
    fields = sorted({f for v in rows.values() for f in v if f != "evidence"})
    for cid, c in ch.items():
        members, op = list(c.get("members") or []), c.get("degrade")
        if c.get("kind") not in CHANNEL_KINDS:
            problems.append(f"channel {cid}: kind {c.get('kind')!r} is not one of {CHANNEL_KINDS}")
            continue
        if c.get("latent") not in (None, "member", "batch", "run"):
            problems.append(f"channel {cid}: latent {c.get('latent')!r} is not member, batch or run")
            continue
        if not op and c.get("slots"):
            unknown = [s for s in c["slots"] if slot_ids is not None and s not in slot_ids]
            if unknown:
                problems.append(f"channel {cid}: slots {unknown} are not surface slots")
            else:
                notes.append(f"channel {cid} ({c['kind']}): fails surface slots {c['slots']}"
                             + ("" if slot_ids is not None else " (not checked: no surface)"))
            continue
        if not members or not op:
            problems.append(f"channel {cid}: needs members and a degrade operator, or surface slots")
            continue
        try:
            moved = _moved(rows, mod.solve(state, degrade={op}), members, fields)
        except Exception as error:  # noqa: BLE001
            problems.append(f"channel {cid}: degrade {op!r} refused by solve(): {type(error).__name__}: {error}")
            continue
        if moved:
            notes.append(f"channel {cid} ({c['kind']}): {op} moves {len(moved)} of {len(members)} member(s)")
        elif c.get("slots"):
            unknown = [s for s in c["slots"] if slot_ids is not None and s not in slot_ids]
            if unknown:
                problems.append(f"channel {cid}: slots {unknown} are not surface slots")
            else:
                notes.append(f"channel {cid} ({c['kind']}): register-invisible; judged on surface slots {c['slots']}")
        else:
            problems.append(f"channel {cid}: degrade {op!r} moves no member's value and it declares no surface slots")
    _check(out, "contract.controls", not problems, "; ".join(problems or notes))


_PROBE = ("import hashlib, sys\n"
          "sys.path[:0] = [sys.argv[1]]\n"
          "import oracle_kit as ok\n"
          "rows = ok.truth(ok.load_solver(sys.argv[2]), sys.stdin.read(), sys.argv[3] or None)\n"
          "print(hashlib.sha256(ok.canonical(rows).encode()).hexdigest())\n")
HASH_SEEDS = ("1", "2")


def cross_process(solver_path, sql_text: str, revision=None) -> dict:
    """{PYTHONHASHSEED: sha256 of the canonical truth} from fresh processes (M5)."""
    out = {}
    for s in HASH_SEEDS:
        env = dict(os.environ, PYTHONHASHSEED=s, PYTHONDONTWRITEBYTECODE="1")
        r = subprocess.run([sys.executable, "-B", "-c", _PROBE, str(HERE), str(solver_path), revision or ""], env=env,
                           input=sql_text, capture_output=True, text=True, timeout=1800)
        out[s] = r.stdout.strip() if r.returncode == 0 else "ERROR " + (r.stderr.strip()[-160:] or f"exit {r.returncode}")
    return out


def check_deterministic(mod, sql_text, revision, out, solver_path=None) -> dict:
    a = mod.solve(mod.load_state(sql_text, revision))
    st = mod.load_state(sql_text, revision)
    b_keys = list(reversed(list(a)))
    b = mod.solve(st, keys_=b_keys)
    b = {k: b[k] for k in a} if set(b) == set(a) else b
    mine = hashlib.sha256(canonical(a).encode()).hexdigest()
    same = canonical(a) == canonical(b)
    procs = cross_process(solver_path, sql_text, revision) if solver_path else {}
    across = all(h == mine for h in procs.values())
    _check(out, "contract.deterministic", same and across,
           (f"two fresh solves (forward and reverse key order) give identical output ({len(a)} keys, sha {mine[:12]})"
            + (f", and so do fresh processes with PYTHONHASHSEED {' and '.join(procs)}" if procs else "")) if same and across
           else "two fresh solves disagree: the solver depends on order, time or global state" if not same
           else f"fresh processes disagree ({ {s: h[:12] for s, h in procs.items()} } vs {mine[:12]} in this process): "
                f"set or hash order leaks into the output")
    return a


def check_regression(mod, prev_sql, prev_truth_path, out, prev_revision=None) -> None:
    if not prev_sql or not prev_truth_path:
        _check(out, "contract.regression", True, "no previous revision supplied (first revision)", block=False)
        return
    raw = Path(prev_truth_path).read_text()
    want = json.loads(raw)
    st = mod.load_state(prev_sql, prev_revision)
    same = mod.solve(st)
    byte = json.dumps(same, indent=2) + "\n" == raw
    latest = getattr(mod, "REVISIONS", (None,))[-1]
    newer = mod.solve(mod.load_state(prev_sql, latest)) if latest else same
    fields = sorted({f for r in want.values() for f in r if f != "evidence"})
    diffs = [(k, f) for k in want for f in fields if _strip(newer).get(k, {}).get(f) != want[k].get(f)]
    _check(out, "contract.regression", (byte or canonical(_strip(same)) == canonical(_strip(want))) and not diffs,
           f"previous truth {Path(prev_truth_path).name}: solver at revision {getattr(st, 'revision', '?')} reproduces it "
           + ("byte for byte" if byte else "in fields and groups (evidence differs)" if canonical(_strip(same)) ==
              canonical(_strip(want)) else "NOT (fields differ)")
           + f"; current rules ({latest}) on the previous SQL: {len(diffs)} field difference(s)"
           + (f", e.g. {diffs[:4]}" if diffs else ""))


def portfolio_of(manifest: dict | None) -> list:
    return [p for p in (manifest or {}).get("mechanism_portfolio", []) or [] if isinstance(p, dict)]


def active_rules(mod, revision) -> dict:
    """The rules a revision's solver applies (all of them unless the solver declares per-revision rule sets)."""
    if revision and hasattr(mod, "rules_for"):
        keep = set(mod.rules_for(revision))
        return {r: v for r, v in mod.RULES.items() if r in keep}
    return dict(mod.RULES)


def check_rules_nodes(mod, manifest, out, revision=None) -> None:
    if manifest is None:
        _check(out, "contract.rules_nodes", False, "no manifest: rules cannot be matched to mechanism nodes")
        return
    nodes = {t.get("id") for t in manifest.get("traps", []) or []} | {c.get("id") for c in manifest.get("chains", []) or []}
    rules = active_rules(mod, revision)
    unknown = sorted({f"{r}:{n}" for r, v in rules.items() for n in v.get("nodes", []) or [] if n not in nodes})
    port = portfolio_of(manifest)
    if port:
        pids = [p.get("id") for p in port]
        extra, missing = sorted(set(rules) - set(pids)), sorted(set(pids) - set(rules))
        pnodes = sorted({f"{p.get('id')}:{n}" for p in port for n in p.get("nodes", []) or [] if n not in nodes})
        mismatch = sorted(r for r in set(rules) & set(pids)
                          if sorted(next(p for p in port if p.get("id") == r).get("nodes", []) or []) != sorted(rules[r].get("nodes", []) or []))
        ok = not (extra or missing or pnodes or unknown or mismatch or len(pids) != len(set(pids)))
        _check(out, "contract.rules_nodes", ok, f"{len(rules)} rules vs {len(pids)} portfolio entries: "
               + (f"rules without a portfolio entry {extra}; " if extra else "")
               + (f"portfolio entries without a rule {missing}; " if missing else "")
               + (f"node lists differ for {mismatch}; " if mismatch else "")
               + (f"unknown nodes {(pnodes + unknown)[:6]}; " if pnodes or unknown else "")
               + ("one-to-one" if ok else ""))
        return
    covered = {n for v in rules.values() for n in v.get("nodes", []) or []}
    retired = {d.get("id") for d in manifest.get("design_delta", []) or [] if isinstance(d, dict)}
    unruled = sorted(t.get("id") for t in manifest.get("traps", []) or [] if t.get("id") not in covered)
    _check(out, "contract.rules_nodes", not unknown,
           f"legacy manifest (no mechanism_portfolio): every rule node {'exists' if not unknown else 'must exist; unknown ' + str(unknown[:6])}; "
           f"{len(unruled)} manifest trap(s) carry no solver rule {unruled[:12]} (decoys, writes and retired nodes need "
           f"none; mechanism nodes do). Retired in design_delta: {sorted(retired & set(unruled))[:8]}",
           extra={"unruled_traps": unruled})


def check_slots(mod, rows, surface, out) -> None:
    if not surface:
        _check(out, "contract.slots", False, "no gradable surface: slot coverage unknown")
        return
    import gradable_surface as gs
    missing, non_solver, n = [], [], 0
    for s in surface.get("slots", []):
        cls = s.get("class")
        try:
            v = gs.solver_value(s, rows, surface)
        except (KeyError, TypeError, IndexError) as error:
            missing.append(f"{s.get('id')} ({error})")
            continue
        if v is gs.NOT_SOLVER:
            if cls in ("direct", "aggregate"):
                missing.append(f"{s.get('id')} ({cls} slot the solver does not produce)")
            else:
                non_solver.append(s.get("id"))
            continue
        n += 1
        if gs.slot_keys(s) and any(k not in rows for k in gs.slot_keys(s)):
            missing.append(f"{s.get('id')} (key {gs.slot_keys(s)} not in the solver output)")
    _check(out, "contract.slots", not missing, f"{n} direct/aggregate slots read a solver value; {len(non_solver)} "
           f"write-content/delivery slots are graded from the writes, not the solver"
           + (f"; not produced: {missing[:6]}" if missing else ""))


def _sql_index(sql_text):
    from base_check import parse_sql
    idx = {}
    for x in parse_sql(sql_text):
        if x["op"] != "insert":
            continue
        r = x["row"]
        for k in ("id", "identifier", "spreadsheet_id", "document_id", "presentation_id"):
            if r.get(k):
                idx.setdefault(str(r[k]), []).append((x["table"], x["line"], r))
    return idx


def base_records(routed: list, task_dir=None) -> tuple:
    """({record id: complete record | None (absent on a complete scan) | "INCOMPLETE"}, error) for base records, read
    through tools/hg.py records (the Evals record helper; its caches stay in the bundle). routed: [(id, route)].
    A non-zero hg.py exit or a reply without checks is an error: a routed record that cannot be read must fail the
    golden check, never pass as "unverified"."""
    import selftest_sandbox
    groups = {}
    for rid, rt in routed:
        groups.setdefault((rt["service"], rt["file"], rt["pointer"], rt["field"]), set()).add(rid)
    order = sorted(groups)
    req = {"checks": [{"id": f"g{i}", "service": s, "file": f, "pointer": p, "field": fld, "values": sorted(groups[k])}
                      for i, (k, (s, f, p, fld)) in enumerate(zip(order, order))]}
    with selftest_sandbox.scratch_tmp("oracle_kit_golden_") as tmp:
        path = Path(tmp) / "record_checks.json"
        path.write_text(json.dumps(req))
        cmd = [sys.executable, "-B", str(HERE / "hg.py")] + (["--task-dir", str(task_dir)] if task_dir else []) + \
            ["records", "--request", str(path)]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
    try:
        doc = json.loads(r.stdout)
    except ValueError:
        return {}, f"tools/hg.py records exit {r.returncode}: {(r.stderr or r.stdout).strip()[-160:]}"
    if r.returncode != 0:
        return {}, f"tools/hg.py records exit {r.returncode}: {(r.stderr or r.stdout).strip()[-160:]}"
    if not (doc.get("checks") or {}):
        return {}, f"tools/hg.py records returned no checks (exit {r.returncode})"
    got = {}
    for i, k in enumerate(order):
        c = (doc.get("checks") or {}).get(f"g{i}") or {}
        found = {m.get("value"): m.get("record") for m in c.get("matches") or []}
        complete = c.get("scan_complete") is True
        for rid in groups[k]:
            got[rid] = (found.get(rid) if complete else "INCOMPLETE")
    return got, None


def check_golden(mod, rows, sql_text, surface, out, task_dir=None) -> None:
    idx = _sql_index(sql_text)
    keys = []
    for s in (surface or {}).get("slots", []):
        sel = s.get("selector") or []
        if sel and sel[0] == "field" and sel[1] in rows and sel[1] not in keys:
            keys.append(sel[1])
    keys = keys[:GOLDEN_SAMPLE] or list(rows)[:GOLDEN_SAMPLE]
    fields = [f for f in getattr(mod, "FIELDS", []) if f not in ("component key", class_field(mod))] or \
        sorted({f for r in rows.values() for f in r if f not in ("evidence", groups_field(mod), class_field(mod))})
    strong, weak, presence, unverified, wrong, base_q = 0, 0, 0, [], [], []

    def judge(k, f, v, records, ids):
        nonlocal strong, weak, presence
        if v in (None, "None", "", "no", "yes") or f in ("issue", "PR", "billing hold at snapshot"):
            presence += 1               # presence-type value: the deciding records exist
            return
        text = json.dumps(records, ensure_ascii=False)
        if re.search(r"(?<![0-9A-Za-z])" + re.escape(str(v)) + r"(?![0-9A-Za-z])", text):
            if len(str(v)) >= 6:
                strong += 1             # an identifier-length value found in its own record
            else:
                weak += 1               # a short token (count, ring, state): found, but weak evidence on its own
        else:
            wrong.append(f"{k}/{f}={str(v)[:16]} not in {ids[:2]}")
    for k in keys:
        for f in fields:
            v = rows[k].get(f)
            ids = mod.evidence(rows, k, f)
            if not ids:
                unverified.append(f"{k}/{f}: no evidence ids")
                continue
            sql_recs = [r for i in ids if i in idx for (_, _, r) in idx[i]]
            # every routed id is read, even when some evidence ids are also in the SQL index
            routed = [(i, mod.base_route(i)) for i in ids] if hasattr(mod, "base_route") else []
            routed = [(i, rt) for i, rt in routed if rt]
            if not sql_recs and not routed:
                unverified.append(f"{k}/{f}: base record(s) {ids[:2]} - no base_route; verify through tools/hg.py")
                continue
            base_q.append((k, f, v, sql_recs, routed))
    based = 0
    if base_q:
        got, err = base_records([x for q in base_q for x in q[4]], task_dir) if any(q[4] for q in base_q) else ({}, None)
        for k, f, v, sql_recs, routed in base_q:
            ids = [i for i, _ in routed] or None
            if routed:
                recs = [got.get(i) for i, _ in routed]
                if err:
                    wrong.append(f"{k}/{f}: routed base record(s) {ids[:2]} unread ({err})")   # blocking, never "unverified"
                    continue
                if "INCOMPLETE" in recs:
                    wrong.append(f"{k}/{f}: routed base record(s) {ids[:2]} unread (incomplete scan)")
                    continue
                absent = [i for i, x in zip(ids, recs) if not isinstance(x, dict)]
                if absent:
                    wrong.append(f"{k}/{f}: routed base record(s) {absent[:2]} absent from the exports")
                    continue
                based += 1
            judge(k, f, v, sql_recs + [x for x in (got.get(i) for i, _ in routed) if isinstance(x, dict)], ids or [])
    _check(out, "contract.golden", not wrong, f"{strong + weak + presence} golden values checked against their deciding "
           f"records ({len(keys)} sampled keys x {len(fields)} fields): {strong} identifier values found, {weak} short "
           f"tokens found, {presence} presence-type" + (f" ({based} through tools/hg.py records)" if based else "")
           + f"; {len(unverified)} unverified"
           + (f" e.g. {unverified[:2]}" if unverified else "") + (f"; NOT FOUND in their records: {wrong[:4]}" if wrong else ""),
           extra={"unverified": unverified[:40]})


def check_digest(manifest, solver_path, task_dir, out) -> None:
    decl = (manifest or {}).get("solver")
    if not decl:
        _check(out, "contract.digest", True, "manifest declares no solver {path, digest} (legacy manifest)", block=False)
        return
    p = Path(decl.get("path", ""))
    p = p if p.is_absolute() else (Path(task_dir) / p if task_dir else p)
    got = hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
    ok = got is not None and str(decl.get("digest", "")).startswith(got[:12]) and Path(p).resolve() == Path(solver_path).resolve()
    _check(out, "contract.digest", ok, f"manifest solver {decl.get('path')} digest {str(decl.get('digest'))[:12]} vs "
           f"file {got[:12] if got else 'missing'}" + ("" if Path(p).resolve() == Path(solver_path).resolve() else
                                                        f"; the checked solver is {solver_path}"))


def contract(solver_path, sql_text, *, revision=None, previous_sql=None, previous_truth=None, previous_revision=None,
             manifest=None, surface=None, task_dir=None) -> dict:
    mod = load_solver(solver_path)
    out = []
    if not check_interface(mod, out):
        return {"verdict": "FAIL", "checks": out}
    rows = check_deterministic(mod, sql_text, revision, out, solver_path)
    check_regression(mod, previous_sql, previous_truth, out, previous_revision)
    state_revision = revision or getattr(mod.load_state(sql_text, revision), "revision", None)
    check_rules_nodes(mod, manifest, out, state_revision)
    check_slots(mod, rows, surface, out)
    check_controls(mod, mod.load_state(sql_text, revision), rows, out, state_revision,
                   {s.get("id") for s in (surface or {}).get("slots") or []} if surface else None)
    check_golden(mod, rows, sql_text, surface, out, task_dir)
    check_digest(manifest, solver_path, task_dir, out)
    return {"verdict": "FAIL" if any(c["status"] == "FAIL" for c in out) else "PASS", "checks": out,
            "solver": str(solver_path), "solver_sha256": hashlib.sha256(Path(solver_path).read_bytes()).hexdigest(),
            "sql_sha256": hashlib.sha256(sql_text.encode()).hexdigest(), "rules": rule_ids(mod),
            "truth_sha256": hashlib.sha256(canonical(rows).encode()).hexdigest()}


def to_text(r: dict) -> str:
    lines = [f"SOLVER CONTRACT: {r['verdict']}" + (f" · {Path(r['solver']).name} sha {r['solver_sha256'][:12]} · "
                                                    f"sql {r['sql_sha256'][:12]} · {len(r['rules'])} rules"
                                                    if r.get("solver") else "")]
    for c in r["checks"]:
        lines.append(f"  [{c['status']}] {c['check']}: {c['detail']}")
    return "\n".join(lines)


# ------------------------------------------------------------------ self-test

_FIXTURE_SOLVER = '''
import collections, json
RULES = {"late": {"mechanism": "A15", "requirement": "R1", "natural_reading": "trust the status field",
                  "nodes": ["T1"], "decides": ["class"], "controls": ["c2"], "over_application": "over:late"}}
CHANNELS = {"scale:status": {"kind": "scale", "degrade": "slip:status", "members": ["c1", "c2", "c3"],
                             "description": "a member's status misread"}}
FIELDS = ["key", "status", "class"]
CLASS_FIELD = "class"
REVISIONS = ("r1", "r2")
def load_state(sql_text, revision=None):
    from base_check import parse_sql
    rows = [x["row"] for x in parse_sql(sql_text) if x["op"] == "insert"]
    return {"rows": rows, "revision": revision or "r2"}
def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    out = {}
    for r in state["rows"]:
        if keys_ and r["id"] not in keys_:
            continue
        off = "late" in disable or any(isinstance(d, tuple) and d[0] == "late" and r["id"] in d[1] for d in disable)
        on = lambda op: op in degrade or any(isinstance(d, tuple) and d[0] == op and r["id"] in d[1] for d in degrade)
        late = (r["note"] == "late" or (on("over:late") and r["id"] == "c2")) and not off and state["revision"] == "r2"
        status = {"ok": "bad", "bad": "ok"}[r["status"]] if on("slip:status") else r["status"]
        out[r["id"]] = {"key": r["id"], "status": status, "class": "HOLD" if late or status != "ok" else "READY",
                        "groups": ["late"] if late else [], "evidence": {"row": r["id"]}}
    return out
def aggregates(rows):
    return {"classes": dict(collections.Counter(v["class"] for v in rows.values())), "groups": {}}
def evidence(rows, key, field):
    return [rows[key]["evidence"]["row"]]
'''


def _self_test() -> None:
    import selftest_sandbox as sb
    if not sb.in_sandbox(BUNDLE):              # its golden check runs tools/hg.py, whose caches are shared
        raise RuntimeError("oracle_kit's self-test reads base records through tools/hg.py: run it in a sandbox "
                           "(python3 -B Task_Authoring/tools/oracle_kit.py --self-test does)")
    sql = ("INSERT INTO linear.linear_comments (id, issue_id, body, status, note) VALUES "
           "('c1', 'ZOM-1', 'x', 'ok', 'late'), ('c2', 'ZOM-2', 'x', 'ok', 'fine'), ('c3', 'ZOM-3', 'x', 'bad', 'fine');\n")
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("oracle_kit_selftest_") as tmp:
        sp = Path(tmp) / "solver.py"
        sp.write_text(_FIXTURE_SOLVER)
        mod = load_solver(sp)
        rows = truth(mod, sql)
        assert [rows[k]["class"] for k in ("c1", "c2", "c3")] == ["HOLD", "READY", "HOLD"], rows
        assert mod.solve(mod.load_state(sql), disable={("late", frozenset({"c1"}))})["c1"]["class"] == "READY"
        prev = Path(tmp) / "truth.prev.json"
        prev.write_text(json.dumps(mod.solve(mod.load_state(sql, "r1")), indent=2) + "\n")
        manifest = {"traps": [{"id": "T1"}], "chains": [], "mechanism_portfolio": [{"id": "late", "nodes": ["T1"]}],
                    "solver": {"path": str(sp), "digest": hashlib.sha256(sp.read_bytes()).hexdigest()}}
        surface = {"truth_fields": {"class": "class"}, "slots": [
            {"id": "S1", "class": "direct", "selector": ["field", "c1", "class"]},
            {"id": "S2", "class": "aggregate", "selector": ["total", "HOLD"]},
            {"id": "S3", "class": "delivery", "selector": ["delivery", "slide_updated"]}]}
        r = contract(sp, sql, manifest=manifest, surface=surface)
        st = {c["check"]: c["status"] for c in r["checks"]}
        assert r["verdict"] == "PASS" and st["contract.rules_nodes"] == "PASS", to_text(r)
        # the previous revision (r1) has no 'late' rule: its stored truth is reproduced at r1, but the current rules
        # on the same SQL differ in fields -> regression FAIL (a rule changed old data)
        r = contract(sp, sql, previous_sql=sql, previous_truth=prev, manifest=manifest, surface=surface)
        assert {c["check"]: c["status"] for c in r["checks"]}["contract.regression"] == "FAIL", to_text(r)

        def fails(**kw):
            res = contract(sp, sql, **{"manifest": manifest, "surface": surface, **kw})
            return [c["check"] for c in res["checks"] if c["status"] == "FAIL"]
        assert "contract.rules_nodes" in fails(manifest=dict(manifest, mechanism_portfolio=[{"id": "other", "nodes": ["T1"]}]))
        assert "contract.rules_nodes" in fails(manifest=dict(manifest, mechanism_portfolio=[{"id": "late", "nodes": ["T9"]}]))
        assert "contract.slots" in fails(surface=dict(surface, slots=surface["slots"] + [
            {"id": "S4", "class": "direct", "selector": ["field", "c9", "class"]}]))
        assert "contract.digest" in fails(manifest=dict(manifest, solver={"path": str(sp), "digest": "0" * 64}))
        bad = Path(tmp) / "bad_solver.py"
        bad.write_text(_FIXTURE_SOLVER.replace('"natural_reading": "trust the status field",', ""))
        assert "contract.interface" in [c["check"] for c in contract(bad, sql)["checks"] if c["status"] == "FAIL"]
        # controls and channels (H1 / F1): declared ones must be live; each planted defect fails contract.controls
        assert {c["check"]: c["status"] for c in contract(sp, sql, manifest=manifest, surface=surface)["checks"]}[
            "contract.controls"] == "PASS"
        assert controls_of(mod) == {"late": {"members": ["c2"], "over_application": "over:late"}}
        for name, old, new in (("ghost member", '"controls": ["c2"]', '"controls": ["c9"]'),
                               ("dead over-application", '"over_application": "over:late"', '"over_application": "over:none"'),
                               ("unknown channel kind", '"kind": "scale"', '"kind": "luck"'),
                               ("dead channel degrade", '"degrade": "slip:status"', '"degrade": "slip:none"')):
            planted = Path(tmp) / f"solver_{name.replace(' ', '_')}.py"
            planted.write_text(_FIXTURE_SOLVER.replace(old, new))
            assert "contract.controls" in [c["check"] for c in contract(planted, sql, manifest=manifest, surface=surface)
                                           ["checks"] if c["status"] == "FAIL"], name
        decl = '"scale:status": {"kind": "scale", "degrade": "slip:status", "members": ["c1", "c2", "c3"],'
        for slot, want in (("S3", "PASS"), ("S9", "FAIL")):          # a slots-only channel names surface slots
            planted = Path(tmp) / f"solver_deck_{slot}.py"
            planted.write_text(_FIXTURE_SOLVER.replace(decl, f'"deck": {{"kind": "tool_surface", "slots": ["{slot}"]}}, ' + decl))
            st_ = {c["check"]: c["status"] for c in contract(planted, sql, manifest=manifest, surface=surface)["checks"]}
            assert st_["contract.controls"] == want, (slot, st_)
        # M5: set order differs between processes (PYTHONHASHSEED): one process can't see it, fresh processes do
        setord = Path(tmp) / "setorder_solver.py"
        setord.write_text(_FIXTURE_SOLVER + "\n_orig_s = solve\n"
                          "def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):\n"
                          "    out = _orig_s(state, disable, degrade, keys_)\n"
                          "    for v in out.values():\n"
                          "        v['evidence']['order'] = list({'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', "
                          "'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu'})\n"
                          "    return out\n")
        det = {c["check"]: c for c in contract(setord, sql, manifest=manifest, surface=surface)["checks"]}["contract.deterministic"]
        assert det["status"] == "FAIL" and "fresh processes disagree" in det["detail"], det
        own = []
        check_deterministic(load_solver(setord), sql, None, own)                   # no solver path: one process only
        assert own[0]["status"] == "PASS", own
        # M5: golden values in base records are read through tools/hg.py records (sandboxed): a value in its record
        # passes, a wrong value and an absent record fail. The base record: Linear team team_ZOM, "Zombie Match 3D".
        ctx = BUNDLE / "support" / "fixtures" / "season_pass_rev13"               # a V3 assignment for hg.py
        assert _FIXTURE_SOLVER.count('"status": status,') == 1
        base_solver = _FIXTURE_SOLVER.replace('"status": status,', '"status": status, "team": "TEAM",') + (
            "\n_orig_e = evidence\n"
            "def evidence(rows, key, field):\n"
            "    return ['BASE_ID'] if field == 'team' else _orig_e(rows, key, field)\n"
            "def base_route(record_id):\n"
            "    return {'service': 'linear', 'file': 'data.json', 'pointer': '/teams', 'field': 'id'} "
            "if record_id.startswith('team_') else None\n"
            "FIELDS = ['key', 'status', 'team', 'class']\n")
        golden = {}
        for name, team, rid in (("found", "Zombie Match 3D", "team_ZOM"), ("wrong", "Zombie Match 4D", "team_ZOM"),
                                ("absent", "Zombie Match 3D", "team_NOPE_0000")):
            gp = Path(tmp) / f"base_{name}.py"
            gp.write_text(base_solver.replace("TEAM", team).replace("BASE_ID", rid))
            res = contract(gp, sql, manifest=manifest, surface=surface, task_dir=ctx)
            golden[name] = {c["check"]: c for c in res["checks"]}["contract.golden"]
        assert golden["found"]["status"] == "PASS" and "through tools/hg.py records" in golden["found"]["detail"], golden["found"]
        assert golden["wrong"]["status"] == "FAIL" and "not in" in golden["wrong"]["detail"], golden["wrong"]
        assert golden["absent"]["status"] == "FAIL" and "absent from the exports" in golden["absent"]["detail"], golden["absent"]

        # M5: every routed id is read and must resolve; a read error or an incomplete scan FAILs the blocking check
        def routed_solver(ids):
            return _FIXTURE_SOLVER.replace('"status": status,', '"status": status, "team": "Zombie Match 3D",') + (
                "\n_orig_e = evidence\n"
                "def evidence(rows, key, field):\n"
                f"    return {ids!r} if field == 'team' else _orig_e(rows, key, field)\n"
                "def base_route(record_id):\n"
                "    return ({'service': 'linear', 'file': 'data.json', 'pointer': '/teams', 'field': 'id'}"
                " if str(record_id).startswith('team_') else None)\n"
                "FIELDS = ['key', 'status', 'team', 'class']\n")
        orig_base = globals()["base_records"]
        try:
            for name, ids, fake, want, why in (
                    ("mixed", ["c1", "team_ZOM"],
                     lambda routed, task_dir=None: ({"team_ZOM": {"id": "team_ZOM", "name": "Zombie Match 3D"}}, None),
                     "PASS", "through tools/hg.py"),
                    ("one absent", ["team_ZOM", "team_OTHER"],
                     lambda routed, task_dir=None: ({"team_ZOM": {"id": "team_ZOM", "name": "Zombie Match 3D"}}, None),
                     "FAIL", "absent from the exports"),
                    ("read error", ["team_ZOM"], lambda routed, task_dir=None: ({}, "hg.py exit 1: boom"),
                     "FAIL", "unread (hg.py exit 1"),
                    ("incomplete", ["team_ZOM"], lambda routed, task_dir=None: ({"team_ZOM": "INCOMPLETE"}, None),
                     "FAIL", "incomplete scan")):
                gp = Path(tmp) / f"routed_{name.replace(' ', '_')}.py"
                gp.write_text(routed_solver(ids))
                globals()["base_records"] = fake
                chk = {c["check"]: c for c in contract(gp, sql, manifest=manifest, surface=surface)["checks"]}["contract.golden"]
                assert chk["status"] == want and why in chk["detail"], (name, chk)
                if name == "mixed":
                    assert "1 through tools/hg.py records" in chk["detail"] or "through tools/hg.py records" in chk["detail"], chk
        finally:
            globals()["base_records"] = orig_base
        # planted (code round 2): an exit-0 reply that contains the routed record but says scan_complete false is
        # incomplete, never verified
        import unittest.mock as mock

        class _Reply:
            returncode = 0
            stderr = ""
            stdout = json.dumps({"checks": {"g0": {"scan_complete": False, "matches": [
                {"value": "team_ZOM", "record": {"id": "team_ZOM", "name": "Zombie Match 3D"}}]}}})

        with mock.patch("subprocess.run", return_value=_Reply()):
            got_inc, err_inc = base_records([("team_ZOM", {"service": "linear", "file": "data.json",
                                                            "pointer": "/teams", "field": "id"})])
        assert got_inc == {"team_ZOM": "INCOMPLETE"} and err_inc is None, (got_inc, err_inc)
        nondet = Path(tmp) / "nondet_solver.py"
        nondet.write_text(_FIXTURE_SOLVER + "\nimport itertools\n_c = itertools.count()\n_orig = solve\n"
                          "def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):\n"
                          "    out = _orig(state, disable, degrade, keys_)\n"
                          "    for v in out.values():\n        v['evidence']['n'] = next(_c)\n    return out\n")
        assert "contract.deterministic" in [c["check"] for c in contract(nondet, sql, manifest=manifest, surface=surface)["checks"]
                                            if c["status"] == "FAIL"]
    print("self-test: ok (interface, determinism incl. a counter-driven solver, regression both ways, portfolio one-to-one "
          "and unknown nodes, slot production, golden spot-check, solver digest, live controls and channels: a ghost "
          "control member, a dead over-application, an unknown channel kind and a dead channel degrade each fail; a "
          "slots-only channel passes on surface slots and fails on an unknown one; M5: set order leaking across "
          "PYTHONHASHSEED fails in fresh processes though one process passes, base-record golden values read through "
          "tools/hg.py records: found PASS, a wrong value and an absent record FAIL)")


# ------------------------------------------------------------------ main

def _task_paths(task_dir):
    td = Path(task_dir) if task_dir else None
    wf = td / "Working_Files" if td else None
    return td, wf


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="oracle_kit.py", description="solver contract (see docstring)")
    ap.add_argument("command", nargs="?", choices=("check", "truth"))
    ap.add_argument("--task-dir", type=Path)
    ap.add_argument("--solver", type=Path)
    ap.add_argument("--sql", type=Path)
    ap.add_argument("--revision")
    ap.add_argument("--previous-sql", type=Path)
    ap.add_argument("--previous-truth", type=Path)
    ap.add_argument("--previous-revision")
    ap.add_argument("--manifest", type=Path)
    ap.add_argument("--surface", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        import selftest_sandbox as sb             # the golden check reads base records through tools/hg.py (caches)
        if not sb.in_sandbox(BUNDLE):
            return sb.run_isolated(["oracle_kit.py", "--self-test"], source=BUNDLE)
        _self_test()
        return 0
    td, wf = _task_paths(a.task_dir)
    solver_path = a.solver or (wf / "solver" / "solver.py" if wf else None)
    sql_path = a.sql or (td / "01_Universe_Inject.sql" if td else None)
    if not a.command or not solver_path or not solver_path.is_file() or not sql_path or not sql_path.is_file():
        print("oracle_kit: give check|truth with --solver and --sql (or --task-dir holding Working_Files/solver/solver.py)",
              file=sys.stderr)
        return 2
    sql_text = sql_path.read_text()
    if a.command == "truth":
        mod = load_solver(solver_path)
        rows = truth(mod, sql_text, a.revision)
        text = json.dumps(rows, indent=2) + "\n"
        if a.out:
            from trajectory_ledger import safe_out
            out = safe_out(a.out)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text)
            print(f"wrote {out} ({len(rows)} keys, sha256 {hashlib.sha256(text.encode()).hexdigest()[:16]})")
        else:
            print(text, end="")
        return 0
    man_path = a.manifest or (wf / "01_Hardness_Manifest.json" if wf else None)
    manifest = json.loads(man_path.read_text()) if man_path and man_path.is_file() else None
    surf_path = a.surface or (wf / "01_Gradable_Surface.json" if wf else None)
    surface = json.loads(surf_path.read_text()) if surf_path and surf_path.is_file() else None
    r = contract(solver_path, sql_text, revision=a.revision,
                 previous_sql=a.previous_sql.read_text() if a.previous_sql else None, previous_truth=a.previous_truth,
                 previous_revision=a.previous_revision, manifest=manifest, surface=surface, task_dir=td)
    print(json.dumps(r, indent=1, ensure_ascii=False) if a.json else to_text(r))
    return 0 if r["verdict"] == "PASS" else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"oracle_kit: {error}", file=sys.stderr)
        raise SystemExit(2)

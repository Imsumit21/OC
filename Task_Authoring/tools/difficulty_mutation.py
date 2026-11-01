#!/usr/bin/env python3
"""difficulty_mutation.py - mutants, diagnostics, interventions and the geometry bound (plan §7.2 and §5).

Generalises Working_Files/hardening_rev11/coverage_stress.py, hardening_rev12/coverage.py and hardening_rev12/verify.py.
Every value comes from the task's solver (tools/oracle_kit.py contract); the SQL is parsed as data, never executed.
Read-only on its inputs, stdlib only. Deterministic: it measures the design, not how often a model errs.

Error elements are the solver's rules active at the revision (rule ablations: the natural reading) and its degrade
operators that change at least one record, including the degrades of declared complexity channels (CHANNELS) and the
over-application operators of control members (oracle_kit): geometry U counts the slots they can flip; they are never
whole mechanisms (hardness_forecast models them as channels). A solver is key-local when a record's row depends only on the elements
applied to that record; then any configuration is composed from per-record outcome tables, one per subset of the
elements touching the record (2^k, k <= --max-k, else UNSUPPORTED). Key-locality is checked against full solves on
seeded random configurations before anything is composed.

  mutate     mutants: every rule ablation, every rule x shard ablation (shards: the key sets of recorded subagent
             briefs with --briefs, else consecutive key slices of --shard-size), every degrade, and the exact table of
             whole-mechanism combinations (k <= --max-k, else UNSUPPORTED). Diagnostics on the gradable surface:
               KILLED      flips at least one direct slot of weight >= 3
               WEAK        flips only aggregate or weight-1 slots, or changes what an aggregate reads and the change cancels
               SURVIVED    changes outputs but no slot
               EQUIVALENT  changes no output
             EQUIVALENT may mean a FALSE trap, a redundant rule, a masking interaction or an incomplete solver; nothing is
             auto-labelled. Every rule, degrade and intervention result needs a written disposition (--dispositions;
             --require-dispositions makes a missing one exit 1).
             Interventions: per node, the injected deciding records of one record are removed from an in-memory copy of
             the SQL text and the solver re-run. The change must stay inside the node's dependency closure: the records
             whose deciding records were removed, their slots, and the aggregates over them. Status load-bearing,
             inert (nothing changed; for a degrade this is the fairness property: truth does not read the decoy) or
             escaped (a record outside the closure changed).
  geometry   U (blocking): the weight share of flippable slots. Per-record slots: any subset of the elements touching
             the record changes the slot. Aggregates: a record that feeds them can change (cancellation ignored, so U is
             an upper bound). Write-content slots: only when they declare mechanisms or flipped_by. Delivery slots fail at
             a base rate, never by design: never flippable, kept in the denominator. U <= 1 - cap blocks. When the
             solver is not composable (not key-local, or locality checked on too few configurations), U is not a
             guaranteed upper bound: its verdict is UNVERIFIED, which needs a written disposition (geometry.U:
             accepted-unverified · redesign · solver-gap, with a reason), never BLOCK (M2).
             L_max (advisory): the largest loss over whole-mechanism combinations; warns below (1 - cap) + 0.10.
  stress     re-emit the Season Pass coverage_stress.json format from a spec file (fixture reproduction)
  plan       re-emit the Season Pass coverage_plan.json format from a spec file and the stress output

Usage:
  python3 -B Task_Authoring/tools/difficulty_mutation.py mutate --task-dir DIR [--solver S] [--sql SQL] [--revision R]
      [--surface S] [--briefs briefs.json ...] [--shard-size 14] [--dispositions D.json] [--require-dispositions]
      [--max-k 8] [--out OUT.json] [--json]
  python3 -B Task_Authoring/tools/difficulty_mutation.py geometry --task-dir DIR [--solver S] [--sql SQL] [--revision R]
      [--surface S | --layout coverage_*.json [--with-cases]] [--mechanisms a,b] [--views auto|v2|v3|both]
      [--max-k 8] [--out OUT.json] [--json]
  python3 -B Task_Authoring/tools/difficulty_mutation.py stress --spec SPEC.json [--out OUT.json]
  python3 -B Task_Authoring/tools/difficulty_mutation.py plan --spec SPEC.json [--stress STRESS.json] [--out OUT.json]
  python3 -B Task_Authoring/tools/difficulty_mutation.py --self-test
Exit 0 = done (diagnostics are reported, not judged), 1 = geometry blocks or a required disposition is missing,
2 = usage error.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import itertools
import json
import random
import re
import sys
import tempfile
from fractions import Fraction
from pathlib import Path


def _bundle() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "difficulty_stats.py").is_file():
            return parent
    raise SystemExit("difficulty_mutation: cannot find the Task_Authoring bundle (no tools/difficulty_stats.py above)")


HERE = Path(__file__).resolve().parent
BUNDLE = _bundle()
for _p in (BUNDLE / "tools", HERE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import difficulty_stats as ds  # noqa: E402  (mode caps have one owner)
import gradable_surface as gs  # noqa: E402
import oracle_kit as ok  # noqa: E402
import trajectory_ledger as tl  # noqa: E402

VERSION = "difficulty_mutation/1"
MAX_K = 8
SHARD_SIZE = 14
LOCALITY_SAMPLES = 24
V2_CAP = Fraction(3, 4)
LMAX_MARGIN = Fraction(1, 10)
DISPOSITIONS = ("live", "weak-accepted", "redesign", "retire", "redundant", "masked", "solver-gap")
GEOMETRY_DISPOSITIONS = ("accepted-unverified", "redesign", "solver-gap")
NOTE = ("deterministic design diagnostics from the solver; on the Season Pass backtests these are development "
        "fixtures, not validation")


class Unsupported(Exception):
    """A record touched by more than --max-k elements: its outcome table is not enumerated."""


def resolve_max_k(max_k: int | None, allow: int | None = None) -> tuple:
    """(k, disclosure): the exact-enumeration limit, one owner for the --max-k policy (decision 2026-10-25). The
    default stays MAX_K (plan §5: k <= 8, else UNSUPPORTED). A value above it runs only with --allow-max-k set to the
    same N, and is disclosed on stderr and in the output; without that explicit override it raises Unsupported."""
    k = MAX_K if max_k is None else int(max_k)
    if k <= MAX_K:
        return k, None
    if allow is not None and int(allow) == k:
        return k, (f"DISCLOSED OVERRIDE: --max-k {k} above the default {MAX_K} (--allow-max-k {k}): exact enumeration of "
                   f"up to 2^{k} configurations per record, not the plan's default (§5)")
    raise Unsupported(f"UNSUPPORTED: --max-k {k} is above the default {MAX_K}; an explicit, disclosed override needs "
                      f"--allow-max-k {k} (plan §5: k <= {MAX_K}, else UNSUPPORTED)")


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def _strip(row: dict) -> dict:
    return {f: v for f, v in row.items() if f != "evidence"}


def _same(a: dict, b: dict) -> bool:
    return _strip(a) == _strip(b)


def _label(e) -> str:
    return f"{e[0]}:{e[1]}"


# ------------------------------------------------------------------ the solver at one revision

class Engine:
    """The solver at one revision, with per-record outcome tables over the elements that touch each record."""

    def __init__(self, mod, sql_text: str, revision: str | None = None, max_k: int = MAX_K):
        self.mod, self.sql_text, self.max_k = mod, sql_text, max_k
        self.sql_sha256 = _sha(sql_text)
        self.state = mod.load_state(sql_text, revision)
        self.revision = getattr(self.state, "revision", None) or (self.state.get("revision") if isinstance(
            self.state, dict) else None) or revision
        self.rules = ok.active_rules(mod, self.revision)
        self.truth = mod.solve(self.state)
        self.keys = list(self.truth)
        self.touched = {}
        for r in self.rules:
            single = mod.solve(self.state, disable=frozenset({r}))
            changed = {k for k in self.keys if not _same(single[k], self.truth[k])}
            declared = set(mod.touched(self.state, r)) if hasattr(mod, "touched") else set()
            self.touched[("rule", r)] = (declared | changed) & set(self.keys)
        declared = list(getattr(mod, "DEGRADES", {}) or {})
        self.channel_ops = {c["degrade"] for c in ok.channels_of(mod).values() if c.get("degrade")} | \
            {c["over_application"] for c in ok.controls_of(mod, self.revision).values() if c["over_application"]}
        for op in declared + sorted(self.channel_ops - set(declared)):
            dg = mod.solve(self.state, degrade=frozenset({op}))
            self.touched[("degrade", op)] = {k for k in self.keys if not _same(dg[k], self.truth[k])}
        self.elements = [e for e, ks in self.touched.items() if ks]
        self.inert = [e for e, ks in self.touched.items() if not ks]
        self.by_key = {k: [e for e in self.elements if k in self.touched[e]] for k in self.keys}
        self._tables = {}
        self._locality = None

    def mechanisms(self) -> list:
        """Whole mechanisms: rules that are not part of another rule, and degrades that change a record; channel
        degrades and over-application operators are channels, not designed mechanisms."""
        return [e for e in self.elements if (e[0] == "degrade" and e[1] not in self.channel_ops)
                or (e[0] == "rule" and not self.rules[e[1]].get("part_of"))]

    def solve(self, failing: dict) -> dict:
        """A full solve. failing: {element: None (every record) | set of keys}."""
        disable, degrade = set(), set()
        for (kind, name), ks in failing.items():
            item = name if ks is None else (name, frozenset(ks))
            (disable if kind == "rule" else degrade).add(item)
        return self.mod.solve(self.state, disable=frozenset(disable), degrade=frozenset(degrade))

    def table(self, key: str):
        """{frozenset(elements): row} for every subset of the elements touching key; None past max_k."""
        if key not in self._tables:
            els = self.by_key[key]
            if len(els) > self.max_k:
                self._tables[key] = None
            else:
                tab = {frozenset(): self.truth[key]}
                for n in range(1, len(els) + 1):
                    for sub in itertools.combinations(els, n):
                        one = frozenset({key})
                        disable = frozenset((name, one) for kind, name in sub if kind == "rule")
                        degrade = frozenset((name, one) for kind, name in sub if kind == "degrade")
                        tab[frozenset(sub)] = self.mod.solve(self.state, disable=disable, degrade=degrade,
                                                             keys_=[key])[key]
                self._tables[key] = tab
        return self._tables[key]

    def compose(self, failing: dict) -> dict:
        """Rows for a configuration, composed from the per-record tables (key-local solvers only)."""
        rows = {}
        for k in self.keys:
            els = frozenset(e for e in self.by_key[k] if e in failing and (failing[e] is None or k in failing[e]))
            if not els:
                rows[k] = self.truth[k]
                continue
            tab = self.table(k)
            if tab is None:
                raise Unsupported(k)
            rows[k] = tab[els]
        return rows

    def composable(self) -> bool:
        """Key-local on a check that covered most configurations; a weak check never licenses composition."""
        loc = self.locality()
        return loc["key_local"] and not loc["weak"]

    def rows(self, failing: dict) -> dict:
        """Composed rows when the solver is composable and every record is enumerable, else a full solve."""
        if self.composable():
            try:
                return self.compose(failing)
            except Unsupported:
                pass
        return self.solve(failing)

    def locality(self, samples: int = LOCALITY_SAMPLES, seed: int = 0) -> dict:
        if self._locality is not None:
            return self._locality
        rng = random.Random(seed)
        configs = [{e: None} for e in self.elements]
        for _ in range(samples if self.elements else 0):
            chosen = [e for e in self.elements if rng.random() < 0.5] or [rng.choice(self.elements)]
            cfg = {}
            for e in chosen:
                ks = sorted(self.touched[e])
                cfg[e] = None if rng.random() < 0.5 else set(rng.sample(ks, max(1, len(ks) // 2)))
            configs.append(cfg)
        bad, skipped = [], 0
        for cfg in configs:
            try:
                comp = self.compose(cfg)
            except Unsupported:
                skipped += 1
                continue
            full = self.solve(cfg)
            diff = [k for k in self.keys if ok.canonical(_strip(comp[k])) != ok.canonical(_strip(full[k]))]
            if diff:
                bad.append({"config": {_label(e): (sorted(v) if v else "all") for e, v in cfg.items()}, "keys": diff[:8]})
        checked = len(configs) - skipped
        self._locality = {"configs": len(configs), "checked": checked, "skipped_unsupported": skipped, "mismatches": bad,
                          "key_local": not bad and checked > 0, "weak": checked * 2 < len(configs),
                          "rule": "composed per-record outputs equal a full solve's on every checked configuration (each "
                                  "element alone, then seeded random mixes); a configuration touching a record past "
                                  "--max-k is skipped, never counted as agreement; evidence bookkeeping is not compared"}
        return self._locality


# ------------------------------------------------------------------ slot values on solver rows

class Slots:
    """Slot values on solver rows, with the aggregates computed once per configuration (agrees with
    gradable_surface.solver_value)."""

    def __init__(self, slots: list, surface: dict):
        tf = surface.get("truth_fields") or {}
        self.cf, self.gf = tf.get("class", "handoff class"), tf.get("groups", "groups")
        self.slots = slots
        self.by_id = {s["id"]: s for s in slots}
        self.ids = [s["id"] for s in slots]
        self.weight = {s["id"]: s["weight"] for s in slots}
        self.total = sum(self.weight.values())
        self.sel = {s["id"]: tuple(s.get("selector") or ()) for s in slots}
        self.cls = {s["id"]: s.get("class") or (gs.SELECTOR_CLASS.get(self.sel[s["id"]][0], "delivery")
                                                 if self.sel[s["id"]] else "delivery") for s in slots}

    def values(self, rows: dict) -> dict:
        classes = collections.Counter(v.get(self.cf) for v in rows.values())
        sizes = collections.Counter(g for v in rows.values() for g in (v.get(self.gf) or []))
        out = {}
        for sid, sel in self.sel.items():
            kind = sel[0] if sel else None
            if kind == "field":
                out[sid] = (rows.get(sel[1]) or {}).get(sel[2])
            elif kind in ("total", "printed_total"):
                out[sid] = classes.get(sel[1], 0)
            elif kind in ("group_count", "group_size"):
                out[sid] = sizes.get(sel[1], 0)
            elif kind == "group_key":
                out[sid] = sel[2] in ((rows.get(sel[1]) or {}).get(self.gf) or [])
            elif kind == "groups_of":
                out[sid] = sorted((rows.get(sel[1]) or {}).get(self.gf) or [])
            elif kind == "sole_reason":
                out[sid] = ((rows.get(sel[1]) or {}).get(self.gf) or []) == [sel[2]]
            else:
                out[sid] = gs.NOT_SOLVER
        return out

    def flipped(self, vals: dict, base: dict) -> list:
        return [i for i in self.ids if vals[i] is not gs.NOT_SOLVER and vals[i] != base[i]]


def legacy_layout(doc: dict, with_cases: bool = False) -> tuple:
    """(slots, surface) from a coverage_stress.json / coverage_plan.json: retained slots (selector or none = delivery)
    and, with --with-cases, the case facts as direct field slots (field 'groups' reads the record's groups)."""
    slots = []
    for r in doc["retained_slots"]:
        sel = r.get("selector")
        slots.append({"id": r["id"], "weight": r["weight"], "selector": list(sel) if sel else None,
                      "class": gs.SELECTOR_CLASS.get(sel[0], "direct") if sel else "delivery"})
    if with_cases:
        for f in doc.get("case_facts") or doc.get("case_coverage_facts") or []:
            sel = ["groups_of", f["key"]] if f["field"] == "groups" else ["field", f["key"], f["field"]]
            slots.append({"id": f["id"], "weight": f["illustrative_weight"], "selector": sel, "class": "direct"})
    return slots, {"truth_fields": {"class": "handoff class", "groups": "groups"}}


# ------------------------------------------------------------------ diagnostics

def changed_outputs(rows: dict, truth: dict) -> list:
    return [(k, f) for k in truth for f in truth[k] if f != "evidence" and rows[k].get(f) != truth[k].get(f)]


def diagnose(slots: Slots, rows: dict, truth: dict, base_vals: dict) -> dict:
    changed = changed_outputs(rows, truth)
    if not changed:
        return {"diagnostic": "EQUIVALENT", "changed_outputs": 0, "flipped_slots": [], "flipped_weight": 0,
                "why": "changes no output"}
    vals = slots.values(rows)
    flipped = slots.flipped(vals, base_vals)
    weight = sum(slots.weight[i] for i in flipped)
    killing = [i for i in flipped if slots.cls[i] == "direct" and slots.weight[i] >= 3]
    feeds = any(f in (slots.cf, slots.gf) for _, f in changed)
    has_agg = any(slots.cls[i] == "aggregate" for i in slots.ids)
    if killing:
        d, why = "KILLED", f"flips direct slot(s) of weight >= 3: {killing[:8]}"
    elif flipped:
        d, why = "WEAK", f"flips only aggregate or weight-1 slots: {flipped[:8]}"
    elif feeds and has_agg:
        d, why = "WEAK", "changes what an aggregate reads (class or group membership) and the aggregate change cancels"
    else:
        d, why = "SURVIVED", "changes outputs that no slot reads"
    return {"diagnostic": d, "changed_outputs": len(changed), "changed_records": len({k for k, _ in changed}),
            "changed_fields": sorted({f for _, f in changed}), "flipped_slots": flipped, "flipped_weight": weight,
            "why": why}


def shards_for(engine: Engine, briefs=None, size: int = SHARD_SIZE) -> list:
    """Worker batches: the key sets of recorded subagent briefs, else consecutive slices of the record list. Briefs
    that name no key the solver knows are refused: every batch would be empty (no shard ablation, and a batch-latent
    forecast channel that never fails)."""
    if briefs:
        seen, out = set(), []
        for b in briefs:
            ks = tuple(k for k in engine.keys if k in set(b.get("keys") or []))
            if ks and ks not in seen:
                seen.add(ks)
                out.append(list(ks))
        if not out:
            raise ValueError("the briefs name no key the solver knows (they carry no key lists): rebuild them with "
                             "trajectory_ledger --surface <the task's surface> or --key-regex, or drop --briefs to use "
                             "consecutive slices")
        return out
    return [engine.keys[i:i + size] for i in range(0, len(engine.keys), size)]


def mutants(engine: Engine, slots: Slots, briefs=None, shard_size: int = SHARD_SIZE) -> dict:
    base_vals = slots.values(engine.truth)
    out = {"rules": [], "shards": [], "degrades": []}
    for r, spec in engine.rules.items():
        rows = engine.solve({("rule", r): None})
        out["rules"].append({"id": f"rule:{r}", "rule": r, "mechanism": spec.get("mechanism"), "part_of": spec.get("part_of"),
                             "touched": len(engine.touched.get(("rule", r), ())), **diagnose(slots, rows, engine.truth, base_vals)})
    for op in getattr(engine.mod, "DEGRADES", {}) or {}:
        rows = engine.solve({("degrade", op): None})
        out["degrades"].append({"id": f"degrade:{op}", "degrade": op, "touched": len(engine.touched[("degrade", op)]),
                                **diagnose(slots, rows, engine.truth, base_vals)})
    batches = shards_for(engine, briefs, shard_size)
    for e in engine.elements:
        if e[0] != "rule":
            continue
        for i, batch in enumerate(batches, 1):
            hit = [k for k in batch if k in engine.touched[e]]
            if not hit:
                continue
            rows = engine.rows({e: set(hit)})
            d = diagnose(slots, rows, engine.truth, base_vals)
            out["shards"].append({"id": f"shard:{e[1]}:{i}", "rule": e[1], "shard": i, "keys": hit, **d})
    out["shard_source"] = "recorded subagent briefs" if briefs else f"consecutive slices of {shard_size} records"
    out["batches"] = len(batches)
    return out


def combinations(engine: Engine, slots: Slots, mechanisms=None) -> dict:
    mechs = mechanisms if mechanisms is not None else engine.mechanisms()
    if len(mechs) > engine.max_k:
        return {"status": "UNSUPPORTED", "mechanisms": [_label(e) for e in mechs],
                "why": f"{len(mechs)} mechanisms > {engine.max_k}: exact combinations only (plan §5); no approximation"}
    base_vals = slots.values(engine.truth)
    table = []
    for n in range(len(mechs) + 1):
        for sub in itertools.combinations(mechs, n):
            rows = engine.rows({e: None for e in sub})
            vals = slots.values(rows)
            flipped = slots.flipped(vals, base_vals)
            lost = sum(slots.weight[i] for i in flipped)
            table.append({"failing": [_label(e) for e in sub], "flipped_slots": flipped, "lost_weight": lost,
                          "score": (slots.total - lost) / slots.total})
    return {"status": "EXACT", "mechanisms": [_label(e) for e in mechs], "total_weight": slots.total, "table": table}


# ------------------------------------------------------------------ interventions

def _row_id(row: dict):
    for k in ("id", "identifier", "spreadsheet_id", "document_id", "presentation_id"):
        if row.get(k):
            return str(row[k])
    return None


def interventions(engine: Engine, slots: Slots) -> list:
    from base_check import parse_sql
    mod = engine.mod
    if not hasattr(mod, "deciding"):
        return [{"id": "interventions", "status": "UNSUPPORTED", "why": "the solver has no deciding(state, rule, key)"}]
    stmts = parse_sql(engine.sql_text)
    per_line = collections.Counter(x["line"] for x in stmts)
    by_id = collections.defaultdict(list)
    for x in stmts:
        if x["op"] == "insert" and _row_id(x["row"]):
            by_id[_row_id(x["row"])].append(x)
    starts = sorted(per_line)
    n_lines = len(engine.sql_text.splitlines())

    def span(start):      # a statement runs from its first line to the line before the next statement
        later = [s for s in starts if s > start]
        return range(start, (later[0] if later else n_lines + 1))
    deciding = {(r, k): set(mod.deciding(engine.state, r, k)) for r in engine.rules for k in engine.keys}
    base_vals = slots.values(engine.truth)
    lines = engine.sql_text.splitlines()
    out = []
    targets = [(("rule", r), sorted(engine.touched.get(("rule", r)) or [])) for r in engine.rules]
    targets += [(("degrade", op), sorted(engine.touched.get(("degrade", op)) or []))
                for op in getattr(mod, "DEGRADES", {}) or {}]
    for (kind, name), keys in targets:
        iid = f"intervention:{kind}:{name}"
        if kind == "rule":
            if not keys:
                out.append({"id": iid, "status": "no-target", "why": "the rule acts on no record"})
                continue
            key = keys[0]
            ids = [i for i in mod.deciding(engine.state, name, key) if i in by_id]
        else:
            key = None
            ids = [name.split(":", 1)[1]] if ":" in name and name.split(":", 1)[1] in by_id else []
        shared = [i for i in ids if any(per_line[x["line"]] > 1 for x in by_id[i])]
        ids = [i for i in ids if i not in shared]
        if not ids:
            out.append({"id": iid, "key": key, "status": "no-injected-records",
                        "why": "none of the deciding records is an injected row on its own SQL line"
                               + (f" ({len(shared)} share a line with other rows)" if shared else "")})
            continue
        drop = {n for i in ids for x in by_id[i] for n in span(x["line"])}
        text = "\n".join(l for n, l in enumerate(lines, 1) if n not in drop) + "\n"
        rows = mod.solve(mod.load_state(text, engine.revision))
        changed = [k for k in engine.keys if not _same(rows[k], engine.truth[k])]
        closure = {k for (r, k), d in deciding.items() if d & set(ids)} | ({key} if key else set())
        escaped = [k for k in changed if k not in closure]
        flipped = slots.flipped(slots.values(rows), base_vals)
        status = "escaped" if escaped else ("load-bearing" if changed else "inert")
        expect = "inert" if kind == "degrade" else "load-bearing"
        out.append({"id": iid, "key": key, "removed_records": ids, "removed_lines": sorted(drop),
                    "closure": sorted(closure), "changed_records": changed, "escaped_records": escaped,
                    "flipped_slots": flipped, "status": status, "expected": expect,
                    "finding": None if status == expect else
                    ("a record outside the node's closure changed: undeclared coupling" if status == "escaped" else
                     "the truth reads the decoy" if kind == "degrade" else
                     "removing the node's deciding records changed nothing: the node is not load-bearing "
                     "(a hard-wired rule, a redundant record, or an incomplete solver)")})
    return out


# ------------------------------------------------------------------ geometry

def _tracker_group(heading: str, surface: dict):
    for d in (surface.get("deliverables") or {}).values():
        if isinstance(d, dict) and d.get("kind") == "text":
            for g, pat in d.get("groups") or []:
                if re.search(heading, g, re.I) or re.search(heading, pat, re.I):
                    return g
    return None


def caps_for(views: str, context) -> dict:
    out = {}
    mode = (context or {}).get("difficulty_mode")
    spec = (context or {}).get("spec_version")
    want = {"v2": ["V2"], "v3": ["V3"], "both": ["V2", "V3"]}.get(views) or (["V3"] if spec == "V3" else ["V2"])
    if not mode:
        # Advisory only: the authoring gates refuse to infer a V3 mode (difficulty_stats). Hardness v2 Part 1
        # treats a task with no mode as Medium, so the geometry uses that cap and says so when a V3 view needs it.
        mode = "medium"
        if "V3" in want:
            print("difficulty_mutation: no difficulty_mode supplied; the advisory cap defaults to Medium "
                  "(Hardness v2 Part 1)", file=sys.stderr)
    for v in want:
        out[v] = {"cap": ds.DIFFICULTY_CAPS[mode] if v == "V3" else V2_CAP, "mode": mode if v == "V3" else None}
    return out


def geometry(engine: Engine, slots: Slots, surface: dict, caps: dict, mechanisms=None) -> dict:
    flippable, unsupported, assumptions = set(), [], []
    class_moves, group_moves, field_moves = set(), set(), collections.defaultdict(set)
    direct_by_key = collections.defaultdict(list)
    for s in slots.slots:
        if slots.cls[s["id"]] == "direct" and slots.sel[s["id"]]:
            for k in gs.slot_keys({"selector": list(slots.sel[s["id"]])}):
                direct_by_key[k].append(s["id"])
    base_vals = slots.values(engine.truth)
    cf, gf = slots.cf, slots.gf
    for k in engine.keys:
        if not engine.by_key[k]:
            continue
        tab = engine.table(k)
        if tab is None:
            unsupported.append(k)
            flippable.update(direct_by_key.get(k, []))
            class_moves.add(("*", "*"))
            group_moves.add("*")
            field_moves[k].add("*")
            continue
        t = engine.truth[k]
        for sub, row in tab.items():
            if not sub:
                continue
            for f in t:
                if f != "evidence" and row.get(f) != t.get(f):
                    field_moves[k].add(f)
            if row.get(cf) != t.get(cf):
                class_moves.add((t.get(cf), row.get(cf)))
            group_moves.update(set(t.get(gf) or []) ^ set(row.get(gf) or []))
            if direct_by_key.get(k):
                one = slots.values({**{k: row}})
                for sid in direct_by_key[k]:
                    if one[sid] is not gs.NOT_SOLVER and one[sid] != base_vals[sid]:
                        flippable.add(sid)
    live = {_label(e) for e in engine.elements} | {e[1] for e in engine.elements}
    for s in slots.slots:
        sid, sel, cls = s["id"], slots.sel[s["id"]], slots.cls[s["id"]]
        kind = sel[0] if sel else None
        if cls == "delivery" or kind is None:
            continue
        if kind in ("total", "printed_total"):
            if any(a == "*" or sel[1] in (a, b) for a, b in class_moves):
                flippable.add(sid)
        elif kind in ("group_count", "group_size"):
            if "*" in group_moves or sel[1] in group_moves:
                flippable.add(sid)
        elif kind == "tracker_lists":
            g = _tracker_group(sel[1], surface)
            moved = field_moves.get(sel[2], set())
            if "*" in moved or (gf in moved and (g is None or g in group_moves or "*" in group_moves)):
                flippable.add(sid)
            if g is None:
                assumptions.append(f"{sid}: heading {sel[1]!r} maps to no tracker group; fed by any group change")
        elif kind == "tracker_count":
            g = _tracker_group(sel[1], surface)
            if "*" in group_moves or (g in group_moves if g else bool(group_moves)):
                flippable.add(sid)
        elif kind == "reason_matches":
            if field_moves.get(sel[1]):
                flippable.add(sid)
        elif cls == "write_content" or kind in ("text", "link"):
            declared = set(s.get("mechanisms") or []) | set(s.get("flipped_by") or [])
            if declared & live:
                flippable.add(sid)
            elif not declared:
                assumptions.append(f"{sid}: write-content slot declares no mechanisms: not flippable")
    combos = combinations(engine, slots, mechanisms)
    from_combos = []
    if combos["status"] == "EXACT":      # a slot an exact whole-mechanism combination flips is flippable
        from_combos = sorted({i for row in combos["table"] for i in row["flipped_slots"]} - flippable,
                             key=slots.ids.index)
        flippable |= set(from_combos)
    if not engine.composable():
        loc = engine.locality()
        assumptions.append(("the solver is not key-local" if not loc["key_local"] else
                            f"key-locality was checked on only {loc['checked']} of {loc['configs']} configurations")
                           + ": U is the per-record enumeration plus the exact whole-mechanism combinations; couplings "
                             "from partial (shard) ablations across records are not enumerated, so U is not a "
                             "guaranteed upper bound")
    weight = sum(slots.weight[i] for i in flippable)
    u = Fraction(weight, slots.total) if slots.total else Fraction(0)
    if combos["status"] == "EXACT":
        best = max(combos["table"], key=lambda x: (x["lost_weight"], -len(x["failing"])))
        lmax = Fraction(best["lost_weight"], slots.total)
        lmax_doc = {"value": float(lmax), "lost_weight": best["lost_weight"], "failing": best["failing"],
                    "mechanisms": combos["mechanisms"]}
    else:
        lmax, lmax_doc = None, {"value": None, "status": "UNSUPPORTED", "why": combos["why"]}
    views = {}
    composable = engine.composable()
    for v, c in caps.items():
        need = 1 - c["cap"]
        bound = "PASS" if u > need else "BLOCK"
        views[v] = {"cap": float(c["cap"]), "mode": c["mode"], "needs_loss_above": float(need),
                    "U": {"verdict": bound if composable else "UNVERIFIED", "bound_verdict": bound,
                          "rule": "U must exceed 1 - cap: otherwise no combination of the designed mechanisms can "
                                  "bring the average strictly below the cap" + ("" if composable else
                                  "; the solver is not composable, so U is no guaranteed bound: UNVERIFIED, which "
                                  "needs a written disposition (geometry.U), never BLOCK")},
                    "L_max": ({"verdict": "WARN" if lmax < need + LMAX_MARGIN else "OK",
                               "rule": f"advisory: warns when L_max < (1 - cap) + {float(LMAX_MARGIN):.2f}"}
                              if lmax is not None else {"verdict": "UNSUPPORTED"})}
    by_class = collections.Counter(slots.cls[i] for i in flippable)
    return {"U": float(u), "U_exact": f"{u.numerator}/{u.denominator}", "flippable_weight": weight,
            "total_weight": slots.total, "flippable_slots": sorted(flippable, key=slots.ids.index),
            "not_flippable": [i for i in slots.ids if i not in flippable],
            "flippable_by_class": dict(by_class), "unsupported_records": unsupported,
            "flippable_only_by_combinations": from_combos, "key_local": engine.locality()["key_local"],
            "composable": engine.composable(),
            "elements": [_label(e) for e in engine.elements], "inert_elements": [_label(e) for e in engine.inert],
            "assumptions": sorted(set(assumptions)), "L_max": lmax_doc, "views": views}


# ------------------------------------------------------------------ dispositions

def geometry_dispositions(geo: dict, recorded) -> dict:
    """M2: an UNVERIFIED U needs a written disposition (geometry.U); a PASS or BLOCK needs none."""
    if not isinstance(recorded, dict):
        recorded = json.loads(Path(recorded).read_text()) if recorded and Path(recorded).is_file() else {}
        recorded = recorded.get("geometry", recorded)
    need = ["geometry.U"] if any(v["U"]["verdict"] == "UNVERIFIED" for v in geo["views"].values()) else []
    bad = [k for k in need if k in recorded and (not isinstance(recorded[k], dict) or recorded[k].get("disposition")
                                                 not in GEOMETRY_DISPOSITIONS or not str(recorded[k].get("reason") or "").strip())]
    if bad:
        raise ValueError(f"geometry dispositions need {{disposition: one of {GEOMETRY_DISPOSITIONS}, reason}}: {bad}")
    return {"required": need, "recorded": {k: recorded[k] for k in need if k in recorded},
            "missing": [k for k in need if k not in recorded],
            "rule": "an UNVERIFIED U (the solver is not composable) needs a written disposition, never a BLOCK"}


def dispositions(results: list, path) -> dict:
    """path: a JSON file or an already-loaded {id: {disposition, reason}} mapping."""
    recorded = path if isinstance(path, dict) else (json.loads(Path(path).read_text()) if path else {})
    bad = {k: v for k, v in recorded.items() if not isinstance(v, dict) or v.get("disposition") not in DISPOSITIONS
           or not str(v.get("reason") or "").strip()}
    if bad:
        raise ValueError(f"dispositions need {{disposition: one of {DISPOSITIONS}, reason}}: {sorted(bad)[:6]}")
    need = [r["id"] for r in results]
    return {"required": need, "recorded": {k: recorded[k] for k in need if k in recorded},
            "missing": [k for k in need if k not in recorded], "unknown": sorted(set(recorded) - set(need)),
            "rule": "every rule, degrade and intervention result needs a written disposition (blocking)"}


# ------------------------------------------------------------------ legacy reproduction (Season Pass fixtures)

def _resolve(base: Path, p: str) -> Path:
    q = Path(p)
    return q if q.is_absolute() else (base / q)


def _spec_sql(spec: dict, base: Path) -> str:
    sql = _resolve(base, spec["sql"]).read_text()
    want = spec.get("sql_sha256_expected")
    if want and _sha(sql) != want:
        raise ValueError(f"{spec['sql']}: sha256 {_sha(sql)[:16]} is not the spec's revision {want[:16]}")
    return sql


def _variants(spec: dict) -> list:
    names = spec.get("combinations_of") or []
    out = [tuple(x) for n in range(len(names) + 1) for x in itertools.combinations(names, n)]
    return out + [tuple(x) for x in spec.get("extra") or []]


def _legacy_value(rows, selector, mod):
    kind, *a = selector
    if kind == "field":
        return rows[a[0]][a[1]]
    if kind == "total":
        return mod.aggregates(rows)["classes"].get(a[0], 0)
    if kind == "group_count":
        return len(mod.aggregates(rows)["groups"][a[0]])
    if kind == "group_key":
        return a[1] in rows[a[0]]["groups"]
    if kind == "sole_reason":
        return rows[a[0]]["groups"] == [a[1]]
    raise ValueError(kind)


def emit_stress(spec: dict, base: Path) -> dict:
    """The coverage_stress.json format (hardening_rev11/coverage_stress.py), from a spec and the solver."""
    mod = ok.load_solver(_resolve(base, spec["solver"]))
    sql = _spec_sql(spec, base)
    state = mod.load_state(sql, spec.get("solver_revision"))
    expected = mod.solve(state)
    rubrics = json.loads(_resolve(base, spec["rubrics"]).read_text())
    duplicates = set(spec["duplicates"])
    selectors = spec["selectors"]
    retained = [{"id": f"R{i}", "weight": r["weight"], "original_title": r["title"], "selector": selectors.get(f"R{i}")}
                for i, r in enumerate(rubrics, 1) if f"R{i}" not in duplicates]
    weight = sum(x["weight"] for x in retained)
    if weight != spec["retained_weight"]:
        raise ValueError(f"retained weight {weight} != {spec['retained_weight']}")
    casefacts = [{"id": cid, "mechanism": m, "key": key, "field": f, "expected": expected[key][f],
                  "illustrative_weight": w, "coverage_reason": why, "source_ids": expected[key]["evidence"]}
                 for cid, m, key, f, w, why in spec["cases"]]
    case_total = weight + sum(f["illustrative_weight"] for f in casefacts)
    if case_total != spec["case_denominator"]:
        raise ValueError(f"case denominator {case_total} != {spec['case_denominator']}")
    revision = json.loads(_resolve(base, spec["revision"]).read_text())
    b = spec["boundary"]
    for fact in casefacts:
        row = expected[fact["key"]]
        pr = b["pr_prefix"] + row[b["pr_field"]]
        gov = spec["governance"][fact["mechanism"]]
        governance = revision[gov["from_revision"]] if isinstance(gov, dict) else gov
        boundary = [r["row"]["id"] for r in revision["new_records"] if r["table"] == b["tables"][fact["mechanism"]]
                    and (r["row"].get("issue_id") == row[b["issue_field"]] or r["row"].get("pr_id") == pr)]
        fact["decisive_source_ids"] = [governance, *boundary, *[v for v in fact["source_ids"].values() if v]]
    projections = []
    for disabled in _variants(spec["variants"]):
        candidate = mod.solve(state, disable=frozenset(disabled))
        failed = [r["id"] for r in retained if r["selector"]
                  and _legacy_value(candidate, r["selector"], mod) != _legacy_value(expected, r["selector"], mod)]
        failed_weight = sum(r["weight"] for r in retained if r["id"] in failed)
        badfacts = [f for f in casefacts if candidate[f["key"]][f["field"]] != f["expected"]]
        additional = sum(f["illustrative_weight"] for f in badfacts)
        skip = set(spec["difference_skip_fields"])
        differences = [{"key": key, "field": f, "expected": expected[key][f], "candidate": candidate[key][f]}
                       for key in expected for f in expected[key] if f not in skip and candidate[key][f] != expected[key][f]]
        projections.append({"ignored_mechanisms": list(disabled), "candidate_counts": mod.aggregates(candidate),
                            "wrong_rows": len({x["key"] for x in differences}), "wrong_fields": len(differences),
                            "failed_current_fact_slots": failed, "failed_weight": failed_weight,
                            "retained_weight": weight,
                            "projected_score_with_perfect_other_work": (weight - failed_weight) / weight,
                            "illustrative_case_facts_failed": [f["id"] for f in badfacts],
                            "illustrative_score_with_added_case_coverage":
                                (case_total - failed_weight - additional) / case_total,
                            "differences": differences})
    return {"kind": spec["kind"], "sql_sha256": _sha(sql), "assumptions": spec["assumptions"],
            "retained_slots": retained, "case_coverage_facts": casefacts, "projections": projections}


def emit_plan(spec: dict, base: Path, stress: dict) -> dict:
    """The coverage_plan.json format (hardening_rev12/coverage.py), from a spec, the solver and the stress output."""
    mod = ok.load_solver(_resolve(base, spec["solver"]))
    sql = _spec_sql(spec, base)
    state = mod.load_state(sql, spec.get("solver_revision"))
    truth = mod.solve(state)
    retained = [r for r in stress["retained_slots"] if r["id"] not in set(spec["drop"])]
    proposal = []
    for cid, mechanism, key, f, w, why in spec["facts"]:
        ids = []
        for v in truth[key]["evidence"].values():
            ids.extend(v if isinstance(v, list) else [v] if v else [])
        proposal.append(dict(id=cid, mechanism=mechanism, key=key, field=f, expected=truth[key][f],
                             illustrative_weight=w, reason=why, source_ids=list(dict.fromkeys(ids))))
    weight = sum(r["weight"] for r in retained)
    proposed = sum(f["illustrative_weight"] for f in proposal)
    skip = set(spec["difference_skip_fields"])
    results = []
    for ignored in _variants(spec["variants"]):
        candidate = mod.solve(state, disable=frozenset(ignored))
        failed = [r["id"] for r in retained if r["selector"]
                  and _legacy_value(candidate, r["selector"], mod) != _legacy_value(truth, r["selector"], mod)]
        badcases = [f["id"] for f in proposal if candidate[f["key"]][f["field"]] != f["expected"]]
        loss = sum(r["weight"] for r in retained if r["id"] in failed)
        case_loss = sum(f["illustrative_weight"] for f in proposal if f["id"] in badcases)
        diffs = [dict(key=k, field=f, expected=truth[k][f], candidate=candidate[k][f]) for k in truth for f in truth[k]
                 if f not in skip and truth[k][f] != candidate[k][f]]
        results.append(dict(ignored=list(ignored), wrong_rows=len({x["key"] for x in diffs}), wrong_fields=len(diffs),
                            existing_fact_slot_failures=failed, case_fact_failures=badcases,
                            existing_projection=(weight - loss) / weight,
                            case_coverage_projection=(weight + proposed - loss - case_loss) / (weight + proposed),
                            candidate_counts=mod.aggregates(candidate), differences=diffs))
    columns = collections.Counter(r["selector"][2] for r in retained if r["selector"] and r["selector"][0] == "field")
    columns.update(f["field"] for f in proposal if f["field"] not in set(spec["column_count_skip_fields"]))
    limit, exempt = spec["column_sample_limit"], set(spec["column_sample_exempt"])
    over = {f: n for f, n in columns.items() if f not in exempt and n > limit}
    if over:
        raise ValueError(f"column samples above {limit}: {over}")
    return dict(kind=spec["kind"], sql_sha256=_sha(sql), existing_weight=weight, proposed_case_weight=proposed,
                combined_illustrative_weight=weight + proposed, assumptions=spec["assumptions"], retained_slots=retained,
                case_facts=proposal, column_sample_counts=dict(columns), stress=results)


def legacy_text(doc: dict) -> str:
    return json.dumps(doc, indent=2) + "\n"


# ------------------------------------------------------------------ reports

def to_text(rep: dict) -> str:
    lines = [f"MUTATION · {rep.get('revision')} · sql {rep['sql_sha256'][:12]} · {NOTE}"]
    if rep.get("max_k_override"):
        lines.append(f"  {rep['max_k_override']}")
    loc = rep.get("key_locality")
    if loc:
        lines.append(f"  key-locality: {'PASS' if loc['key_local'] else 'FAIL'} on {loc['checked']} of {loc['configs']} "
                     f"configurations checked" + (f", {loc['skipped_unsupported']} skipped (a record past --max-k)"
                                                  if loc["skipped_unsupported"] else "")
                     + (" · WEAK: most configurations were not checked" if loc["weak"] else "")
                     + (f" · {len(loc['mismatches'])} mismatch(es) on {sorted({k for m in loc['mismatches'] for k in m['keys']})[:8]}"
                        if loc["mismatches"] else ""))
    m = rep.get("mutants")
    if m:
        for x in m["rules"] + m["degrades"]:
            lines.append(f"  {x['id']:34} {x['diagnostic']:10} flipped {x['flipped_weight']:>3} {x['why'][:70]}")
        c = collections.Counter(x["diagnostic"] for x in m["shards"])
        lines.append(f"  shards ({m['shard_source']}, {m['batches']} batches): {len(m['shards'])} mutants {dict(c)}")
    for x in rep.get("interventions") or []:
        lines.append(f"  {x['id']:34} {x['status']:16}" + (f" FINDING: {x['finding']}" if x.get("finding") else ""))
    g = rep.get("geometry")
    if g:
        lines.append(f"  geometry: U = {g['U']:.4f} ({g['flippable_weight']}/{g['total_weight']}) · L_max = "
                     + (f"{g['L_max']['value']:.4f} over {g['L_max']['failing']}" if g["L_max"].get("value") is not None
                        else str(g["L_max"].get("status"))))
        for v, x in g["views"].items():
            lines.append(f"    {v} cap {x['cap']:.2f}: U {x['U']['verdict']} (needs > {x['needs_loss_above']:.2f}) · "
                         f"L_max {x['L_max']['verdict']}")
        if g["unsupported_records"]:
            lines.append(f"    UNSUPPORTED records (counted flippable): {g['unsupported_records'][:10]}")
    d = rep.get("dispositions")
    if d:
        lines.append(f"  dispositions: {len(d['recorded'])}/{len(d['required'])} recorded; missing {d['missing'][:8]}"
                     + (" ..." if len(d["missing"]) > 8 else ""))
    return "\n".join(lines)


# ------------------------------------------------------------------ self-test

_SOLVER = '''
import collections, json, re
KEY_REGEX = r"K-\\d{2}"
FIELDS = ["key", "count", "note", "flag", "class"]
CLASS_FIELD, GROUPS_FIELD = "class", "groups"
RULES = {
    "late": {"mechanism": "A15", "requirement": "R1", "natural_reading": "the latest note wins", "nodes": ["T1"],
             "decides": ["count"]},
    "quiet": {"mechanism": "A6", "requirement": "R1", "natural_reading": "keep the raw note", "nodes": ["T2"],
              "decides": ["note"]},
    "minor": {"mechanism": "A7", "requirement": "R1", "natural_reading": "flag everything", "nodes": ["T3"],
              "decides": ["flag"]},
    "noop": {"mechanism": "A9", "requirement": "R1", "natural_reading": "nothing", "nodes": ["T4"], "decides": ["count"]},
}
DEGRADES = {"trust:exp_k03": "copy the export count"}
COUPLED = False
LINKED = False
def load_state(sql_text, revision=None):
    from base_check import parse_sql
    return {"rows": [x["row"] for x in parse_sql(sql_text) if x["op"] == "insert"], "revision": revision or "r1"}
def keys():
    return ["K-01", "K-02", "K-03", "K-04"]
def _on(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)
def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    out = {}
    for k in keys_ or keys():
        notes = sorted((r for r in state["rows"] if r.get("issue_id") == k), key=lambda r: r["created_at"])
        pool = notes if _on(disable, "late", k) else [r for r in notes if "draft" not in r["body"]]
        pick = pool[-1] if pool else None
        n = int(re.search(r"count=(\\d+)", pick["body"]).group(1)) if pick else None
        if COUPLED and k == "K-04":     # data coupling no deciding() list declares
            n = (n or 0) + sum(1 for r in state["rows"] if r.get("issue_id") == "K-01")
        if LINKED and k == "K-04" and _on(disable, "late", "K-01"):     # an ablation on K-01 changes K-04: not key-local
            n = 0
        if _on(degrade, "trust:exp_k03", k) and any(r.get("export_of") == k for r in state["rows"]):
            n = 9
        note = (pick["body"] if _on(disable, "quiet", k) else pick["body"].split(" ")[0]) if pick else ""
        flag = "yes" if _on(disable, "minor", k) else ("yes" if pick and "flag" in pick["body"] else "no")
        out[k] = {"key": k, "count": str(n), "note": note, "flag": flag, "class": "HOLD" if n else "READY",
                  "groups": ["counted"] if n else [], "evidence": {"note": pick["id"] if pick else None}}
    return out
def aggregates(rows):
    return {"classes": dict(collections.Counter(v["class"] for v in rows.values())),
            "groups": {"counted": [k for k, v in rows.items() if "counted" in v["groups"]]}}
def evidence(rows, key, field):
    return [rows[key]["evidence"]["note"]]
def touched(state, rule):
    if rule == "late":
        return {r["issue_id"] for r in state["rows"] if "draft" in r.get("body", "")}
    if rule == "quiet":
        return {r["issue_id"] for r in state["rows"] if r.get("issue_id")}
    if rule == "minor":
        return {"K-02"}
    return set()
def deciding(state, rule, key):
    return [r["id"] for r in state["rows"] if r.get("issue_id") == key]
'''

_SQL = ("INSERT INTO linear.linear_comments (id, issue_id, body, created_at) VALUES "
        "('note_k01_a', 'K-01', 'count=2 final run', '2026-01-01T00:00:00Z');\n"
        "INSERT INTO linear.linear_comments (id, issue_id, body, created_at) VALUES "
        "('note_k01_b', 'K-01', 'count=0 draft rerun', '2026-01-02T00:00:00Z');\n"
        "INSERT INTO linear.linear_comments (id, issue_id, body, created_at) VALUES "
        "('note_k02_a', 'K-02', 'count=0 final run', '2026-01-01T00:00:00Z');\n"
        "INSERT INTO linear.linear_comments (id, issue_id, body, created_at) VALUES "
        "('note_k03_a', 'K-03', 'count=4 final run flag', '2026-01-01T00:00:00Z');\n"
        "INSERT INTO linear.linear_comments (id, issue_id, body, created_at) VALUES "
        "('note_k04_a', 'K-04', 'count=1 final run', '2026-01-01T00:00:00Z');\n"
        "INSERT INTO gsheets.sheets_sheets (id, export_of) VALUES ('exp_k03', 'K-03');\n")


def _surface(extra_delivery: int = 0) -> dict:
    slots = [{"id": "S1", "weight": 5, "class": "direct", "selector": ["field", "K-01", "class"]},
             {"id": "S2", "weight": 1, "class": "direct", "selector": ["field", "K-02", "flag"]},
             {"id": "S3", "weight": 3, "class": "aggregate", "selector": ["total", "HOLD"]},
             {"id": "S4", "weight": 3, "class": "aggregate", "selector": ["group_count", "counted"]},
             {"id": "S5", "weight": 3, "class": "direct", "selector": ["field", "K-03", "count"]},
             {"id": "S6", "weight": 1, "class": "delivery", "selector": ["delivery", "slide_updated"]},
             {"id": "S7", "weight": 1, "class": "write_content", "selector": ["text", "slide", "x"]}]
    slots += [{"id": f"D{i}", "weight": 5, "class": "delivery", "selector": ["delivery", "slide_updated"]}
              for i in range(extra_delivery)]
    return {"kind": "GRADABLE_SURFACE", "version": 1, "truth_fields": {"class": "class", "groups": "groups"},
            "classes": ["READY", "HOLD"], "deliverables": {}, "slots": slots}


_SCALE_SOLVER = '''
import collections
KEY_REGEX = r"K-\\d{2}"
CLASS_FIELD, GROUPS_FIELD = "class", "groups"
RULES = {"tidy": {"mechanism": "A9", "requirement": "R1", "natural_reading": "keep the raw note", "nodes": ["T1"],
                  "decides": ["note"]}}
CHANNELS = {"scale:class": {"kind": "scale", "degrade": "slip:class", "members": [f"K-{n:02d}" for n in range(1, 11)],
                            "description": "a member's class misread"}}
def load_state(sql_text, revision=None):
    return {"revision": revision or "r1"}
def keys():
    return [f"K-{n:02d}" for n in range(1, 11)]
def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    on = lambda spec, op, k: any(d == op or (isinstance(d, tuple) and d[0] == op and k in d[1]) for d in spec)
    return {k: {"key": k, "note": "raw" if on(disable, "tidy", k) else "tidy",
                "class": "HOLD" if on(degrade, "slip:class", k) else "READY",
                "groups": [], "evidence": {}} for k in keys_ or keys()}
def aggregates(rows):
    return {"classes": dict(collections.Counter(v["class"] for v in rows.values())), "groups": {}}
def evidence(rows, key, field):
    return []
'''


def _self_test_scale(tmp) -> None:
    """F1: a scale-driven design passes geometry U only through its declared channel degrade (planted: the same
    solver without CHANNELS blocks), and the channel is never a whole mechanism."""
    surface = {"kind": "GRADABLE_SURFACE", "version": 1, "truth_fields": {"class": "class", "groups": "groups"},
               "classes": ["READY", "HOLD"], "deliverables": {},
               "slots": [{"id": f"S{n}", "weight": 1, "class": "direct", "selector": ["field", f"K-{n:02d}", "class"]}
                         for n in range(1, 11)] + [{"id": "D1", "weight": 5, "class": "delivery",
                                                     "selector": ["delivery", "slide_updated"]}]}
    caps = caps_for("v3", {"difficulty_mode": "hard"})
    got = {}
    for name, text in (("declared", _SCALE_SOLVER), ("undeclared", _SCALE_SOLVER.replace("CHANNELS = {", "_UNUSED = {"))):
        sp = Path(tmp) / f"scale_{name}.py"
        sp.write_text(text)
        eng = Engine(ok.load_solver(sp), "")
        g = geometry(eng, Slots(surface["slots"], surface), surface, caps)
        got[name] = (g["U_exact"], g["views"]["V3"]["U"]["verdict"], [_label(e) for e in eng.mechanisms()])
    assert got["declared"] == ("2/3", "PASS", ["rule:tidy"]), got           # the channel is no whole mechanism
    assert got["undeclared"] == ("0/1", "BLOCK", ["rule:tidy"]), got


def _self_test() -> None:
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("difficulty_mutation_selftest_") as tmp:
        _self_test_scale(tmp)
        sp = Path(tmp) / "solver.py"
        sp.write_text(_SOLVER)
        mod = ok.load_solver(sp)
        eng = Engine(mod, _SQL)
        assert [_label(e) for e in eng.elements] == ["rule:late", "rule:quiet", "rule:minor", "degrade:trust:exp_k03"], eng.elements
        assert [_label(e) for e in eng.inert] == ["rule:noop"], eng.inert
        loc = eng.locality()
        assert loc["key_local"] and loc["configs"] > 4, loc
        try:                                     # planted: keyless briefs gave silent empty batches
            shards_for(eng, [{"keys": []}, {"keys": ["Z-99"]}])
        except ValueError:
            pass
        else:
            raise AssertionError("briefs that name no solver key were accepted (every batch would be empty)")
        assert shards_for(eng, [{"keys": ["K-01", "K-03"]}, {"keys": ["K-03", "K-01"]}]) == [["K-01", "K-03"]]
        surface = _surface()
        slots = Slots(surface["slots"], surface)
        # the evaluator agrees with gradable_surface.solver_value on truth and on a mutant
        for rows in (eng.truth, eng.solve({("rule", "late"): None})):
            vals = slots.values(rows)
            for s in surface["slots"]:
                ref = gs.solver_value(s, rows, surface)
                assert (vals[s["id"]] is gs.NOT_SOLVER) == (ref is gs.NOT_SOLVER) and (
                    ref is gs.NOT_SOLVER or vals[s["id"]] == ref), (s["id"], vals[s["id"]], ref)
        m = mutants(eng, slots, shard_size=2)
        diag = {x["id"]: x["diagnostic"] for x in m["rules"] + m["degrades"]}
        assert diag == {"rule:late": "KILLED", "rule:quiet": "SURVIVED", "rule:minor": "WEAK", "rule:noop": "EQUIVALENT",
                        "degrade:trust:exp_k03": "KILLED"}, diag
        # minor's declared touched set is {K-02}, but its ablation also changes K-01 and K-04: the engine takes the union
        assert eng.touched[("rule", "minor")] == {"K-01", "K-02", "K-04"}, eng.touched
        assert {x["id"] for x in m["shards"]} == {"shard:late:1", "shard:quiet:1", "shard:quiet:2", "shard:minor:1",
                                                  "shard:minor:2"}, m["shards"]
        # a shard ablation equals the solver's own (rule, key subset) ablation
        assert eng.rows({("rule", "quiet"): {"K-03"}}) == mod.solve(eng.state, disable={("quiet", frozenset({"K-03"}))})
        # an aggregate change that cancels is WEAK: K-01 loses 'counted' while K-02 gains it
        cancel = dict(eng.truth)
        cancel["K-01"] = dict(eng.truth["K-01"], groups=[], **{"class": "READY"})
        cancel["K-02"] = dict(eng.truth["K-02"], groups=["counted"], **{"class": "HOLD"})
        agg_only = Slots([s for s in surface["slots"] if s["class"] != "direct"], surface)
        assert diagnose(agg_only, cancel, eng.truth, agg_only.values(eng.truth))["diagnostic"] == "WEAK"
        combos = combinations(eng, slots)
        assert combos["status"] == "EXACT" and len(combos["table"]) == 16, combos
        g = geometry(eng, slots, surface, caps_for("both", {"difficulty_mode": "hard", "spec_version": "V3"}))
        # flippable: S1 (5) S2 (1) S3 (3) S4 (3) S5 (3) of 17; delivery S6 and undeclared write-content S7 are not
        assert g["flippable_weight"] == 15 and g["total_weight"] == 17 and g["U_exact"] == "15/17", g
        assert g["L_max"]["lost_weight"] == 15 and g["views"]["V3"]["U"]["verdict"] == "PASS", g["L_max"]
        thin = _surface(extra_delivery=8)          # 40 more delivery weight: U = 15/57 < 0.30 under V3 Hard
        g2 = geometry(eng, Slots(thin["slots"], thin), thin, caps_for("v3", {"difficulty_mode": "hard"}))
        assert g2["views"]["V3"]["U"]["verdict"] == "BLOCK" and g2["views"]["V3"]["L_max"]["verdict"] == "WARN", g2["views"]
        small = Engine(mod, _SQL, max_k=1)          # K-01 is touched by two rules: UNSUPPORTED, counted flippable
        gs_ = geometry(small, slots, surface, caps_for("v3", {"difficulty_mode": "hard"}))
        assert "K-01" in gs_["unsupported_records"] and "S1" in gs_["flippable_slots"], gs_
        assert combinations(small, slots)["status"] == "UNSUPPORTED"
        sl = small.locality()            # skipped configurations are reported, never counted as agreement
        assert sl["skipped_unsupported"] > 0 and sl["checked"] == sl["configs"] - sl["skipped_unsupported"], sl
        # --max-k: the default stays 8; above it only with --allow-max-k N (disclosed); otherwise UNSUPPORTED
        assert resolve_max_k(None) == (MAX_K, None) and resolve_max_k(8) == (8, None) and resolve_max_k(3, 9) == (3, None)
        for k, allow in ((12, None), (12, 10), (9, None)):
            try:
                resolve_max_k(k, allow)
            except Unsupported as exc:
                assert f"--allow-max-k {k}" in str(exc), exc
            else:
                raise AssertionError(f"--max-k {k} accepted without --allow-max-k {k}")
        k12, disc = resolve_max_k(12, 12)
        assert k12 == 12 and disc.startswith("DISCLOSED OVERRIDE: --max-k 12"), disc
        import contextlib
        import io
        (Path(tmp) / "inject.sql").write_text(_SQL)
        (Path(tmp) / "surface.json").write_text(json.dumps(surface))
        cli = ["geometry", "--solver", str(sp), "--sql", str(Path(tmp) / "inject.sql"), "--surface",
               str(Path(tmp) / "surface.json"), "--views", "v3"]
        err = io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            assert main(cli + ["--max-k", "12"]) == 2                        # planted: an undisclosed override
        assert "UNSUPPORTED" in err.getvalue(), err.getvalue()
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            main(cli + ["--max-k", "12", "--allow-max-k", "12", "--json"])
        doc = json.loads(out.getvalue())
        assert doc["max_k"] == 12 and doc["max_k_override"].startswith("DISCLOSED") and "DISCLOSED" in err.getvalue(), doc
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            main(cli + ["--json"])
        doc = json.loads(out.getvalue())
        assert doc["max_k"] == MAX_K and doc["max_k_override"] is None, doc
        # a solver whose ablation on one record changes another fails key-locality; the whole-mechanism combinations
        # still make the cross-record slot flippable, and U says what it does not enumerate
        lk = Path(tmp) / "linked.py"
        lk.write_text(_SOLVER.replace("LINKED = False", "LINKED = True"))
        eng_l = Engine(ok.load_solver(lk), _SQL)
        assert not eng_l.locality()["key_local"] and eng_l.locality()["mismatches"], eng_l.locality()
        assert eng.composable() and not eng_l.composable()
        assert small.composable() == (sl["key_local"] and not sl["weak"])           # a weak check never composes
        s_l = dict(surface, slots=surface["slots"] + [{"id": "S8", "weight": 3, "class": "direct",
                                                       "selector": ["field", "K-04", "class"]}])
        g_l = geometry(eng_l, Slots(s_l["slots"], s_l), s_l, caps_for("v3", {"difficulty_mode": "hard"}))
        assert g_l["flippable_only_by_combinations"] == ["S8"] and not g_l["key_local"], g_l
        assert any("not key-local" in x for x in g_l["assumptions"]), g_l["assumptions"]
        # M2: a solver that isn't composable gets an UNVERIFIED U (never a BLOCK) and needs a written disposition
        assert {v["U"]["verdict"] for v in g_l["views"].values()} == {"UNVERIFIED"}, g_l["views"]
        assert geometry_dispositions(g_l, {})["missing"] == ["geometry.U"]
        assert not geometry_dispositions(g_l, {"geometry.U": {"disposition": "accepted-unverified",
                                                             "reason": "a cross-record link the solver declares"}})["missing"]
        assert geometry_dispositions(geometry(eng, slots, surface, caps_for("v3", {"difficulty_mode": "hard"})),
                                     {})["required"] == []                        # a composable solver needs none
        try:
            geometry_dispositions(g_l, {"geometry.U": {"disposition": "fine", "reason": "x"}})
        except ValueError:
            pass
        else:
            raise AssertionError("a geometry disposition outside the allowed set was accepted")
        assert eng_l.rows({("rule", "late"): None}) == eng_l.solve({("rule", "late"): None})     # falls back to full solves
        iv = {x["id"]: x for x in interventions(eng, slots)}
        assert iv["intervention:rule:late"]["status"] == "load-bearing" and not iv["intervention:rule:late"]["finding"], iv
        assert iv["intervention:degrade:trust:exp_k03"]["status"] == "inert" and not iv["intervention:degrade:trust:exp_k03"]["finding"]
        assert iv["intervention:rule:noop"]["status"] == "no-target"
        # a statement over two lines is removed whole (INSERT ... newline VALUES ...)
        two = _SQL.replace(" VALUES ('note_k01_a'", "\nVALUES ('note_k01_a'")
        iv2 = {x["id"]: x for x in interventions(Engine(mod, two), slots)}["intervention:rule:late"]
        assert iv2["removed_lines"] == [1, 2, 3] and iv2["status"] == "load-bearing", iv2
        coupled = Path(tmp) / "coupled.py"
        coupled.write_text(_SOLVER.replace("COUPLED = False", "COUPLED = True"))
        eng_c = Engine(ok.load_solver(coupled), _SQL)
        ivc = {x["id"]: x for x in interventions(eng_c, slots)}
        assert ivc["intervention:rule:late"]["status"] == "escaped" and ivc["intervention:rule:late"]["escaped_records"] == ["K-04"], ivc
        dp = Path(tmp) / "d.json"
        dp.write_text(json.dumps({"rule:late": {"disposition": "live", "reason": "kills S1"}}))
        dd = dispositions(m["rules"], dp)
        assert dd["missing"] == ["rule:quiet", "rule:minor", "rule:noop"] and "rule:late" in dd["recorded"], dd
        dp.write_text(json.dumps({"rule:late": {"disposition": "fine"}}))
        try:
            dispositions(m["rules"], dp)
        except ValueError:
            pass
        else:
            raise AssertionError("an invalid disposition was accepted")
        # legacy emitter arithmetic on a toy spec
        (Path(tmp) / "rubrics.json").write_text(json.dumps([{"title": "t1", "weight": 5}, {"title": "t2", "weight": 3},
                                                           {"title": "dup", "weight": 5}]))
        (Path(tmp) / "revision.json").write_text(json.dumps({"policy_action": "auth_1", "new_records": [
            {"table": "linear.linear_comments", "row": {"id": "note_k01_b", "issue_id": "K-01"}}]}))
        (Path(tmp) / "inject.sql").write_text(_SQL)
        spec = {"kind": "TOY", "solver": "solver.py", "sql": "inject.sql", "rubrics": "rubrics.json",
                "revision": "revision.json", "duplicates": ["R3"], "selectors": {"R1": ["field", "K-01", "class"]},
                "retained_weight": 8, "case_denominator": 11,
                "cases": [["C1", "late", "K-01", "count", 3, "drafts do not count"]],
                "governance": {"late": {"from_revision": "policy_action"}},
                "boundary": {"tables": {"late": "linear.linear_comments"}, "issue_field": "key", "pr_field": "key",
                             "pr_prefix": "x/"},
                "variants": {"combinations_of": ["late"]}, "difference_skip_fields": ["evidence", "groups"],
                "assumptions": ["toy"]}
        out = emit_stress(spec, Path(tmp))
        p = out["projections"]
        assert [x["ignored_mechanisms"] for x in p] == [[], ["late"]], p
        assert p[1]["failed_current_fact_slots"] == ["R1"] and p[1]["projected_score_with_perfect_other_work"] == 3 / 8
        assert p[1]["illustrative_score_with_added_case_coverage"] == (11 - 5 - 3) / 11, p[1]
        assert out["case_coverage_facts"][0]["decisive_source_ids"] == ["auth_1", "note_k01_b", "note_k01_a"], out
        plan = emit_plan({**spec, "drop": [], "facts": [["C1", "late", "K-01", "count", 3, "x"]],
                          "column_sample_limit": 5, "column_sample_exempt": ["class"],
                          "column_count_skip_fields": ["class", "groups"]}, Path(tmp), out)
        assert plan["stress"][1]["existing_projection"] == 3 / 8 and plan["column_sample_counts"] == {"class": 1, "count": 1}, plan
    print("self-test: ok (key-locality vs full solves, evaluator = gradable_surface.solver_value, KILLED / WEAK / "
          "SURVIVED / EQUIVALENT incl. a cancelling aggregate, shard ablations, exact combination table and UNSUPPORTED, "
          "U and L_max with PASS / BLOCK / WARN and unsupported records counted flippable, interventions load-bearing / "
          "inert / escaped, dispositions, legacy emitters, skipped locality configurations reported, a non-key-local "
          "solver detected with full-solve fallback and its combination-only flips kept in U; F1: a scale-driven design "
          "passes U only through its declared channel degrade, never a whole mechanism; M2: a non-composable solver's U "
          "is UNVERIFIED with a required written disposition, never BLOCK)")


# ------------------------------------------------------------------ main

def _task_files(a):
    td = a.task_dir
    wf = td / "Working_Files" if td else None
    solver = a.solver or (wf / "solver" / "solver.py" if wf else None)
    sql = a.sql or (td / "01_Universe_Inject.sql" if td else None)
    if not solver or not solver.is_file() or not sql or not sql.is_file():
        raise ValueError("need --solver and --sql (or --task-dir with Working_Files/solver/solver.py and "
                         "01_Universe_Inject.sql)")
    return td, wf, solver, sql


def _layout(a, wf):
    if getattr(a, "layout", None):
        slots, surface = legacy_layout(json.loads(a.layout.read_text()), a.with_cases)
        return slots, surface, {"layout": tl._rel(a.layout), "sha256": tl.sha256_file(a.layout), "with_cases": a.with_cases}
    path = a.surface or (wf / "01_Gradable_Surface.json" if wf else None)
    if not path or not path.is_file():
        raise ValueError("need --surface (or --task-dir with Working_Files/01_Gradable_Surface.json) or --layout")
    surface = gs.load(path)
    return surface["slots"], surface, {"surface": tl._rel(path), "sha256": tl.sha256_file(path)}


def _context(td):
    if not td:
        return None
    try:
        from task_context import load_context
        return load_context(Path(td))
    except Exception:  # noqa: BLE001 - a legacy task folder has no V3 context
        return None


def _write(path, doc):
    out = tl.safe_out(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, indent=1, ensure_ascii=False, default=sorted) + "\n")
    return out


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="difficulty_mutation.py", description="mutation diagnostics and geometry")
    ap.add_argument("--self-test", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    for name in ("mutate", "geometry"):
        p = sub.add_parser(name)
        p.add_argument("--task-dir", type=Path)
        p.add_argument("--solver", type=Path)
        p.add_argument("--sql", type=Path)
        p.add_argument("--revision")
        p.add_argument("--surface", type=Path)
        p.add_argument("--max-k", type=int, default=MAX_K)
        p.add_argument("--allow-max-k", type=int, metavar="N", help="the explicit, disclosed override for --max-k N > 8")
        p.add_argument("--out", type=Path)
        p.add_argument("--json", action="store_true")
        p.add_argument("--views", choices=("auto", "v2", "v3", "both"), default="auto")
        if name == "mutate":
            p.add_argument("--briefs", type=Path, action="append", default=[])
            p.add_argument("--shard-size", type=int, default=SHARD_SIZE)
            p.add_argument("--dispositions", type=Path)
            p.add_argument("--require-dispositions", action="store_true")
        else:
            p.add_argument("--layout", type=Path, help="a coverage_stress.json / coverage_plan.json slot layout")
            p.add_argument("--with-cases", action="store_true")
            p.add_argument("--mechanisms", help="comma list of rule ids / degrade names for L_max (default: all)")
            p.add_argument("--dispositions", type=Path, help="geometry.U's written disposition when U is UNVERIFIED")
    p = sub.add_parser("stress")
    p.add_argument("--spec", type=Path, required=True)
    p.add_argument("--out", type=Path)
    p = sub.add_parser("plan")
    p.add_argument("--spec", type=Path, required=True)
    p.add_argument("--stress", type=Path)
    p.add_argument("--out", type=Path)
    a = ap.parse_args(argv)
    if a.self_test:
        _self_test()
        return 0
    if a.cmd in ("stress", "plan"):
        spec = json.loads(a.spec.read_text())
        base = a.spec.parent / spec.get("base", ".")
        if a.cmd == "stress":
            doc = emit_stress(spec, base)
        else:
            stress = json.loads(a.stress.read_text()) if a.stress else emit_stress(json.loads(
                _resolve(a.spec.parent, spec["stress_spec"]).read_text()), base)
            doc = emit_plan(spec, base, stress)
        text = legacy_text(doc)
        if a.out:
            out = tl.safe_out(a.out)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text)
            print(f"wrote {tl._rel(out)} ({len(text)} bytes, sha256 {hashlib.sha256(text.encode()).hexdigest()[:16]})")
        else:
            print(text, end="")
        return 0
    if a.cmd not in ("mutate", "geometry"):
        ap.print_usage(sys.stderr)
        return 2
    try:
        max_k, disclosure = resolve_max_k(a.max_k, a.allow_max_k)
    except Unsupported as exc:
        print(f"difficulty_mutation: {exc}", file=sys.stderr)
        return 2
    if disclosure:
        print(f"difficulty_mutation: {disclosure}", file=sys.stderr)
    td, wf, solver_path, sql_path = _task_files(a)
    mod = ok.load_solver(solver_path)
    eng = Engine(mod, sql_path.read_text(), a.revision, max_k)
    slots_list, surface, layout = _layout(a, wf)
    slots = Slots(slots_list, surface)
    rep = {"kind": "MUTATION_REPORT" if a.cmd == "mutate" else "GEOMETRY_REPORT", "tool": VERSION, "note": NOTE,
           "revision": eng.revision, "sql": tl._rel(sql_path), "sql_sha256": eng.sql_sha256,
           "solver": tl._rel(solver_path), "solver_sha256": tl.sha256_file(solver_path), **layout,
           "max_k": max_k, "max_k_override": disclosure, "key_locality": eng.locality()}
    context = _context(td)
    caps = caps_for(a.views, context)
    rc = 0
    if a.cmd == "mutate":
        briefs = []
        for b in a.briefs:
            briefs += json.loads(b.read_text())
        rep["mutants"] = mutants(eng, slots, briefs or None, a.shard_size)
        rep["combinations"] = combinations(eng, slots)
        rep["interventions"] = interventions(eng, slots)
        rep["geometry"] = geometry(eng, slots, surface, caps)
        results = rep["mutants"]["rules"] + rep["mutants"]["degrades"] + [x for x in rep["interventions"] if "status" in x]
        rep["dispositions"] = dispositions(results, a.dispositions)
        if a.require_dispositions and rep["dispositions"]["missing"]:
            rc = 1
    else:
        mechs = None
        if a.mechanisms:
            names = [x.strip() for x in a.mechanisms.split(",") if x.strip()]
            mechs = [e for e in eng.elements if e[1] in names or _label(e) in names]
            if len(mechs) != len(names):
                raise ValueError(f"unknown or inert mechanisms in {names}; elements: {[_label(e) for e in eng.elements]}")
            chans = [e for e in mechs if e[0] == "degrade" and e[1] in getattr(eng, "channel_ops", set())]
            if chans:
                raise ValueError(f"--mechanisms names complexity channel(s) {[_label(e) for e in chans]}: a channel is "
                                 f"counted by U and reported as a channel (F1), never as a designed mechanism")
        rep["geometry"] = geometry(eng, slots, surface, caps, mechs)
    if any(v["U"]["verdict"] == "BLOCK" for v in rep["geometry"]["views"].values()):
        rc = 1
    rep["geometry"]["dispositions"] = geometry_dispositions(rep["geometry"], a.dispositions)
    if rep["geometry"]["dispositions"]["missing"]:
        rc = 1                             # an UNVERIFIED U without its written disposition
    if a.out:
        _write(a.out, rep)
    print(json.dumps(rep, indent=1, ensure_ascii=False, default=sorted) if a.json else to_text(rep))
    if a.out and not a.json:
        print(f"wrote {tl._rel(a.out)}")
    return rc


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"difficulty_mutation: {error}", file=sys.stderr)
        raise SystemExit(2)

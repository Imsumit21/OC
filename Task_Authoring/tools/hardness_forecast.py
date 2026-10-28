#!/usr/bin/env python3
"""hardness_forecast.py - the joint-gate forecast (plan §5, §7.5) and the pre-registration scorer.

UNCALIBRATED and advisory until plan §10 Phase 2 meets its pre-registered adequacy criteria. Every number is a model
output, not a measurement. On the Season Pass backtests these are development fixtures, not validation.

  forecast     Landing rates come from the ledger's priors for one model (--model). Another model's evidence enters
               only through a transfer record (--from-model), and such a forecast prints TRANSFERRED · UNCALIBRATED;
               without one the tool refuses. Each landing configuration is solved exactly
               (difficulty_mutation.Engine; k <= 8 mechanisms, else UNSUPPORTED). Simulated six-run baselines
               (10,000 per scenario by default) are graded by tools/difficulty_stats.compute() under the task's gate
               views; horizon and model provenance are not difficulty gates and are left out.
               Per draw: each mechanism's landing rate from its Beta posterior, then six runs. In a run a mechanism
               lands when its latent uniform falls below that rate; every unordered pair of mechanisms is also
               reported from those per-run landings (landing_pairs: P(both land), P(either lands)). Scenarios, never
               bounds (outcomes are non-monotone):
                 dependence  independent · source (mechanisms whose rules share a source share the latent) ·
                             correlated (one latent for all)
                 extent      whole (every record the rule acts on) · shard:N (one worker batch of N consecutive
                             records) · slip (one record) · batches (M6: every brief batch misses independently at
                             b = 1 - (1 - theta)^(1/B), so the per-run landing rate stays theta; batches from
                             --briefs trajectory_ledger briefs.json, else consecutive slices)
               Complexity channels (F1): every channel the solver declares (oracle_kit CHANNELS, and every control
               rule's over-application) fails member by member at a per-member rate e drawn per baseline from its
               Beta (so P(any of N) is 1 - E[(1 - e)^N], reported beside the plug-in); sampled members go through
               the solver as the channel's degrade (aggregates compound, opposing count errors cancel); latents
               member · batch · run. Rates come from the model's ledger records, pooled across tasks like the
               mechanism priors: channel records of the channel's family (default: its kind) and control records of
               the rule's family (runs of a task share a design effect); else an explicit, disclosed --channel-rate;
               a channel with neither is reported
               UNPARAMETERIZED and not simulated. Each channel is reported apart from the mechanisms, with its
               parameters, records and expected loss alone. --mechanism-rate overrides a mechanism's ledger prior
               for a conditional design (labelled CONDITIONAL).
               Reports E[average] with its 10-90 % band, the 10-90 % band of single run scores, P(each difficulty
               gate), P(all four), E[failure patterns], each slot's P(fail) and P(fails all six runs) (all-fail
               justification workload, never a block) and the value of information: how far P(all) moves between
               draws below and above each mechanism's median landing rate. Probe the budget-critical mechanisms
               first.
  exhaustive   whole-rule landings only: every six-run multiset of the 2^k per-run outcomes through compute(); passing
               multisets per view; P(pass) as a function of a common per-rule miss rate p; E[average](p) and its
               break-even rates; the structure behind them (plan §13, §14.2, §15.5).
  --design     before a solver exists: flipped(F) = the slots whose declared mechanisms / flipped_by meet F (an
               approximation, labelled DESIGN).
  --preregister  appends the forecast to the ledger (kind forecast, source forecast) keyed by the hash of its inputs,
               including the sha256 of every --freeze file (the prompt, manifest and truth.json: plan §14.7 step 3);
               --retrospective marks a backtest whose runs already exist.
  score        scores yes/no predictions (a JSON encoding of a pre-registration) against tool outputs after verifying
               every recorded sha256; Brier score over the scored ones; --append writes prediction and outcome records.
               gates_fail reads surface_grader.py output or difficulty_stats.py --json output (the gates of record).
  compare      after the runs (plan §14.7): per-run table, mechanisms, and per forecast (prior, posterior) each
               mechanism's landings against its 90 % Beta-Binomial predictive interval (NOT-REACHED runs are not
               trials; mixed-model runs also shown excluded), the six-run average against the 10-90 % band and
               P(observed gate verdict) >= 10 % per scenario, the goal (the gates of the task's view), the run-1 call
               and the /hardness band against the outcome, and the scorecard when --predictions is given.

Usage:
  python3 -B Task_Authoring/tools/hardness_forecast.py forecast --task-dir DIR --model M [--solver S] [--sql SQL]
      [--revision R] [--surface S | --slots SLOTS.json | --layout coverage_*.json [--with-cases]] [--mechanisms a,b]
      [--from-model M2] [--exclude-task T] [--exclude-revision R] [--include-mixed] [--family ELEMENT=FAMILY]
      [--views auto|v2|v3|both] [--mode hard] [--task-type long-horizon] [--calls 550] [--draws 10000] [--seed 0]
      [--dependence D ...] [--extent E ...] [--design] [--freeze FILE ...] [--briefs briefs.json ...]
      [--channel-rate CID=E|ALPHA,BETA ...] [--mechanism-rate ELEMENT=E|ALPHA,BETA ...] [--no-channels]
      [--preregister [--retrospective] [--harness NAME@VERSION]]
      [--ledger L] [--out OUT.json] [--json]
  python3 -B Task_Authoring/tools/hardness_forecast.py exhaustive --task-dir DIR [same layout / views options]
      --mechanisms a,b,c [--p-grid 0.01] [--expect 0.3,0.5,0.7,1.0] [--break-even 0.70,0.65] [--out OUT.json]
  python3 -B Task_Authoring/tools/hardness_forecast.py score --predictions P.json [--append [--ledger L]] [--out OUT]
  python3 -B Task_Authoring/tools/hardness_forecast.py compare --verdicts V.json --grades G.json [--forecast LABEL=F.json ...]
      [--difficulty D.json] [--predictions P.json] [--precheck-call go|no-go] [--old-band N] [--no-costs]
      [--out OUT.json] [--md OUT.md] [--json]
  python3 -B Task_Authoring/tools/hardness_forecast.py --self-test
Exit 0 = done, 1 = a recorded hash does not match (score), 2 = usage error or a refused model mix.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import itertools
import json
import math
import random
import statistics
import sys
import tempfile
from pathlib import Path


def _bundle() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "difficulty_stats.py").is_file():
            return parent
    raise SystemExit("hardness_forecast: cannot find the Task_Authoring bundle (no tools/difficulty_stats.py above)")


HERE = Path(__file__).resolve().parent
BUNDLE = _bundle()
for _p in (BUNDLE / "tools", HERE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import difficulty_mutation as dm  # noqa: E402  (exact outcomes have one owner)
import difficulty_stats as ds  # noqa: E402  (gate math has one owner)
import gradable_surface as gs  # noqa: E402
import hardness_ledger as hl  # noqa: E402  (priors have one owner)
import oracle_kit as ok  # noqa: E402
import trajectory_ledger as tl  # noqa: E402

VERSION = "hardness_forecast/1"
DIFFICULTY_GATES = ("pass_at_1", "avg_weighted_pass_rate", "per_rollout_sd", "failure_patterns")
DEPENDENCE = ("independent", "source", "correlated")
EXTENT = ("whole", "shard:32", "shard:14", "slip", "batches")
CHANNEL_LATENT = {"delegation": "batch", "tool_surface": "run"}       # the default latent per kind; else "member"
ALONE_DRAWS = 400
RUNS = 6
MAX_BATCHES = 5000        # refuse a batch latent above this: the inverse CDF is O(B) and the weights are log-space
# CPython's betavariate computes 2*alpha internally; a finite but enormous shape overflows that product and the rejection
# loop never accepts (it HANGS, it does not raise). Real Beta priors here have n_eff <= a few hundred, so a generous
# bound closes the hang without limiting any real prior.
MAX_BETA_PARAM = 1e9
# ... and below this the Gamma sampler underflows (a symmetric 1e-300,1e-300 draws 0.0 every time, and 1e-3 gives a
# mean of 0.38 instead of 0.5); 0.01 is the smallest shape whose sampler is sound here. Real priors have alpha, beta >= 1.
MIN_BETA_PARAM = 0.01
LABEL = "UNCALIBRATED · advisory"
TRANSFER_LABEL = "TRANSFERRED · UNCALIBRATED"
NOTE = "model outputs, not measurements; the Season Pass backtests are development fixtures, not validation"


class RefuseMix(ValueError):
    pass


# ------------------------------------------------------------------ layout, mechanisms, families, priors

def load_layout(a, wf):
    if getattr(a, "slots", None):
        doc = json.loads(a.slots.read_text())
        slots = [{"id": s["id"], "weight": s["weight"], "selector": s.get("selector"),
                  "class": s.get("class") or (gs.SELECTOR_CLASS.get(s["selector"][0], "direct") if s.get("selector")
                                              else "delivery"), **({"mechanisms": s["mechanisms"]} if s.get("mechanisms") else {})}
                 for s in doc["slots"]]
        return slots, {"truth_fields": {"class": "handoff class", "groups": "groups"}}, {
            "slots": tl._rel(a.slots), "sha256": tl.sha256_file(a.slots)}
    return dm._layout(a, wf)


def element_of(engine, name: str):
    for e in engine.elements:
        if name in (e[1], dm._label(e)):
            return e
    known = [dm._label(e) for e in engine.elements] + [f"(inert) {dm._label(e)}" for e in engine.inert]
    raise ValueError(f"mechanism {name!r} is not an active element at {engine.revision}: {known}")


def meta(mod, e, portfolio=()) -> dict:
    if mod is None:                       # DESIGN: the draft manifest's portfolio is the only declaration
        return next((p for p in portfolio if p.get("id") == e[1]), {})
    if e[0] == "rule":
        return mod.RULES.get(e[1]) or {}
    d = (getattr(mod, "DEGRADES", {}) or {}).get(e[1])
    return d if isinstance(d, dict) else {}


def family_of(mod, e, portfolio, overrides) -> str:
    for k in (dm._label(e), e[1]):
        if k in overrides:
            return overrides[k]
    for p in portfolio:
        if p.get("id") == e[1] and (p.get("prior_family") or p.get("family")):
            return p.get("prior_family") or p["family"]           # family: the legacy spelling of prior_family
    m = meta(mod, e, portfolio)
    return m.get("family") or m.get("mechanism") or dm._label(e)


def source_of(mod, e, portfolio=()) -> str:
    return meta(mod, e, portfolio).get("source") or dm._label(e)


def mechanism_priors(ledger, model, families, *, from_model=None, exclude_tasks=(), exclude_revisions=(),
                     include_mixed=False) -> dict:
    """{family: prior} for the target model; another model's evidence only through a transfer record."""
    source_model = from_model or model
    pr = hl.priors(ledger, source_model, exclude_tasks=exclude_tasks, exclude_revisions=exclude_revisions,
                   include_mixed=include_mixed)
    out = {}
    for fam in families:
        if hl.model_family(source_model) != hl.model_family(model):
            t = hl.transferred(ledger, source_model, model, fam, base=pr)
            if t is None:
                raise RefuseMix(f"refusing to mix models: no transfer record from {source_model} to {model} for family "
                                f"{fam!r} (append one with hardness_ledger.py transfer, or forecast with --model "
                                f"{source_model})")
            out[fam] = t
        else:
            out[fam] = pr.get(fam) or {"model": hl.model_family(model), "alpha": 1.0, "beta": 1.0, "mean": 0.5,
                                       "n_eff": 0.0, "record_ids": [], "excluded": [],
                                       "label": "UNCALIBRATED · no evidence for this family on this model: flat Beta(1,1)"}
    return out


# ------------------------------------------------------------------ outcomes and gates

class Outcomes:
    """Failed slots and lost weight per landing configuration (exact, cached); DESIGN mode uses declarations."""

    def __init__(self, engine, slots: dm.Slots, design: bool = False):
        self.engine, self.slots, self.design = engine, slots, design
        self.base = slots.values(engine.truth) if engine else None
        self.cache = {}

    def of(self, failing: dict, cache: bool = True) -> tuple:
        key = tuple(sorted((dm._label(e), tuple(sorted(ks)) if ks is not None else None) for e, ks in failing.items()))
        if not cache and key not in self.cache:          # sampled member subsets rarely repeat: solve, keep nothing
            rows = self.engine.rows(failing)
            failed = frozenset(self.slots.flipped(self.slots.values(rows), self.base))
            return failed, sum(self.slots.weight[i] for i in failed)
        if key not in self.cache:
            if self.design:
                names = {dm._label(e) for e in failing} | {e[1] for e in failing}
                failed = frozenset(s["id"] for s in self.slots.slots
                                   if names & (set(s.get("mechanisms") or []) | set(s.get("flipped_by") or [])))
            else:
                rows = self.engine.rows(failing)
                failed = frozenset(self.slots.flipped(self.slots.values(rows), self.base))
            self.cache[key] = (failed, sum(self.slots.weight[i] for i in failed))
        return self.cache[key]


class Gates:
    """The four difficulty gates of six runs through difficulty_stats.compute(), per view (cached per multiset)."""

    def __init__(self, slots: dm.Slots, views: dict, task_type: str, calls: int):
        self.rubrics = [{"id": i, "weight": slots.weight[i]} for i in slots.ids]
        self.views, self.task_type, self.calls = views, task_type, calls
        self.total = slots.total
        self.cache = {}

    def of(self, failed_sets: list) -> dict:
        key = tuple(sorted(tuple(sorted(f)) for f in failed_sets))
        if key not in self.cache:
            out = {}
            for v, spec in self.views.items():
                data = {"spec_version": v, "task_type": self.task_type, "rubrics": self.rubrics,
                        "rollouts": [{"id": f"r{i}", "status": "completed", "tool_calls": self.calls,
                                      "results": {r["id"]: r["id"] not in f for r in self.rubrics}}
                                     for i, f in enumerate(failed_sets, 1)]}
                if v == "V3":
                    data["difficulty_mode"] = spec["mode"]
                res = ds.compute(data)
                g = {k: res["gates"][k]["verdict"].startswith("PASS") for k in DIFFICULTY_GATES}
                rates = [x["weighted_pass_rate"] for x in res["per_rollout"]]
                out[v] = {"gates": g, "all": all(g.values()), "avg": sum(rates) / len(rates),
                          "sd": statistics.pstdev(rates), "patterns": len(res["patterns"]),
                          "full_passes": len(res["golden_runs"])}
            self.cache[key] = out
        return self.cache[key]


def views_for(name: str, context, mode: str | None) -> dict:
    caps = dm.caps_for(name, dict(context or {}, **({"difficulty_mode": mode} if mode else {})))
    return {v: {"cap": float(c["cap"]), "mode": c["mode"]} for v, c in caps.items()}


# ------------------------------------------------------------------ complexity channels (F1) and batches (M6)
# A declared channel (oracle_kit CHANNELS, and every control rule with an over-application operator) fails member by
# member at a per-member rate e. Sampled members go through the solver as the channel's degrade on that key set
# (Engine.rows): a sampled member fails at about e, aggregates compound, and opposing count errors can cancel. Shared
# causes are the latent: member (independent slips) · batch (one latent per brief batch: delegation) · run (one latent
# for every member and the declared slots). e is drawn per simulated baseline from its Beta, so P(any of N fails) is
# 1 - E[(1 - e)^N], not the plug-in. Rates: the model's ledger records, pooled across tasks like the mechanism priors:
# channel records of the channel's family (default: its kind, so a scale channel learns a per-member error rate per
# model), control records of the rule's family (runs of one task share a design effect, H2); else an explicit,
# disclosed --channel-rate override, else UNPARAMETERIZED (reported, not simulated). A fallback is a validity flag,
# never a channel.

def _rate_from_records(recs: list, rho: float, unit: str = "member"):
    """Beta(1 + sum f / deff, 1 + sum (n - f) / deff) over [(task, revision, run, n, f, id)], where n and f count the
    unit the simulator draws (Q2: member, batch or run). The design effect is 1 + (R - 1) rho per task over its
    distinct (revision, run) pairs: two revisions both numbered run-1 are two runs, not one."""
    if not recs:
        return None
    a = b = 0.0
    tasks = {}
    for task in sorted({x[0] for x in recs}):
        xs = [x for x in recs if x[0] == task]
        deff = hl.design_effect(len({(x[1], x[2]) for x in xs}), rho)
        tasks[task] = {"runs": len({(x[1], x[2]) for x in xs}), "deff": round(deff, 4), "n": sum(x[3] for x in xs),
                       "f": sum(x[4] for x in xs), "n_eff": round(sum(x[3] for x in xs) / deff, 4)}
        a += sum(x[4] for x in xs) / deff
        b += sum(x[3] - x[4] for x in xs) / deff
    out = {"alpha": round(1 + a, 4), "beta": round(1 + b, 4), "mean": round((1 + a) / (2 + a + b), 6),
           "records": [x[5] for x in recs], "unit": unit, "n": sum(x[3] for x in recs), "f": sum(x[4] for x in recs),
           "tasks": tasks, "at_rho": {}, "basis": f"ledger records, {unit} trials (runs of a task share a design "
           f"effect, H2)", "label": "UNCALIBRATED"}
    for r in (0.0, 0.5, 1.0):
        aa = bb = 0.0
        for task in sorted({x[0] for x in recs}):
            xs = [x for x in recs if x[0] == task]
            deff = hl.design_effect(len({(x[1], x[2]) for x in xs}), r)
            aa += sum(x[4] for x in xs) / deff
            bb += sum(x[3] - x[4] for x in xs) / deff
        out["at_rho"][str(r)] = {"alpha": round(1 + aa, 4), "beta": round(1 + bb, 4),
                                 "mean": round((1 + aa) / (2 + aa + bb), 6)}
    return out


def channel_rate(led, model: str, cid: str, kind: str, family: str, overrides: dict, *, exclude_tasks=(),
                 exclude_revisions=(), include_mixed=False, rho: float = hl.RHO):
    """A channel's rate: a disclosed override, else the model's ledger records of its family, pooled across tasks
    (channel records: the channel's family; control trials: the rule's family), else None. Trials are counted in the
    unit the simulator draws (member / batch / run, recorded in counts.unit; a control defaults to its member)."""
    if cid in overrides:
        return overrides[cid]
    recs, dropped = [], []            # (task, revision, run, n, f, id, unit)
    excluded = lambda r: (r["task"] in exclude_tasks or r["revision"] in exclude_revisions  # noqa: E731
                          or f"{r['task']}:{r['revision']}" in exclude_revisions)
    for r in led.current():
        if hl.model_family(r.get("model")) != hl.model_family(model):
            continue
        if kind == "control" and r["kind"] == "control" and r.get("family") == family:
            if excluded(r):
                dropped.append([r["id"], "excluded task/revision"])   # a real record, deliberately excluded
                continue
            # F1 residual b: only a record that would otherwise be THIS channel's trial is reported as dropped, and
            # every exclusion keeps its reason (an all-dropped channel is UNPARAMETERIZED, never silently absent).
            if (r.get("features") or {}).get("mixed_model") and not include_mixed:
                dropped.append([r["id"], f"mixed-model run: deciding model(s) "
                                         f"{(r.get('features') or {}).get('deciding_models') or [r.get('model')]}"])
                continue
            if r.get("verdict") not in ("OVER-APPLIED", "HELD"):
                dropped.append([r["id"], f"{r.get('verdict')} is not a control trial (nothing was written)"])
                continue
            recs.append((r["task"], r.get("revision"), r.get("run"), 1, int(r["verdict"] == "OVER-APPLIED"), r["id"],
                         "member"))
        elif kind != "control" and r["kind"] == "channel" and r.get("family") == family \
                and (r.get("counts") or {}):
            if excluded(r):
                dropped.append([r["id"], "excluded task/revision"])
                continue
            if (r.get("features") or {}).get("mixed_model") and not include_mixed:
                dropped.append([r["id"], f"mixed-model run: deciding model(s) "
                                         f"{(r.get('features') or {}).get('deciding_models') or [r.get('model')]}"])
                continue
            if r.get("verdict") not in ("FAILED", "HELD"):
                dropped.append([r["id"], f"{r.get('verdict')} is not a channel trial"])
                continue
            c = r["counts"]
            unit = c.get("unit") or ("member" if c.get("members") else "run")
            n = c.get("n") if c.get("n") is not None else (c.get("members") if c.get("members") is not None else 1)
            def _count(x):
                # ints are validated AS ints: a float round-trip loses precision above 2**53 and can hide failed > n
                if isinstance(x, bool) or not isinstance(x, (int, float)):
                    raise ValueError(f"channel {cid}: record {r['id']} has non-numeric counts {c!r}")
                if isinstance(x, int):
                    return x
                if not (math.isfinite(x) and float(x).is_integer()):
                    raise ValueError(f"channel {cid}: record {r['id']} has non-integral counts {c!r}")
                return int(x)
            n_, f_ = _count(n), _count(c.get("failed", 0))
            if n_ < 0 or f_ < 0 or f_ > n_:
                raise ValueError(f"channel {cid}: record {r['id']} has invalid counts {c!r}: need n >= 0 and "
                                 f"0 <= failed <= n")
            recs.append((r["task"], r.get("revision"), r.get("run"), n_, f_, r["id"], unit))
    if not recs:
        return {"alpha": None, "beta": None, "mean": None, "records": [], "unit": None, "n": 0, "f": 0,
                "tasks": {}, "at_rho": {}, "dropped": dropped,
                "basis": "no eligible record after exclusions", "label": "UNPARAMETERIZED · no eligible record"}
    units = {x[6] for x in recs}
    converted = None
    if units == {"member", "run"}:
        # Q2: the units must match what the simulator draws. A member-latent record converts to a run trial (a run is
        # one trial, failed if any member failed); only this conversion is defined.
        runs = {}
        for task, rev, run, n, f, rid, u in recs:
            x = runs.setdefault((task, rev, run), {"f": 0, "ids": []})
            x["f"] = max(x["f"], int(f > 0))
            x["ids"].append(rid)
        recs = [(k[0], k[1], k[2], 1, v["f"], ",".join(v["ids"]), "run") for k, v in sorted(runs.items())]
        units = {"run"}
        converted = "member"          # from here on the trials are runs: a run failed when any member did
    if len(units) != 1:
        raise ValueError(f"channel {cid}: trial records carry mixed units {sorted(units)}; a batch record cannot be "
                         f"pooled with member or run trials")
    rate = _rate_from_records([x[:6] for x in recs], rho, units.pop())
    rate["dropped"] = dropped
    if converted:
        rate["converted_from"] = converted
    return rate


def parse_rate(spec: str) -> tuple:
    """--channel-rate CID=E@SOURCE or CID=ALPHA,BETA@SOURCE: an explicit, disclosed override and its independent
    source. A missing source is recorded as UNSPECIFIED; the forecast CLI refuses that."""
    body, _, source = spec.rpartition("@") if "@" in spec else (spec, "", "")
    cid, _, v = body.partition("=")
    try:
        parts = [float(x) for x in v.split(",") if x.strip()]
    except ValueError:
        parts = []
    if len(parts) == 1 and 0 <= parts[0] <= 1:
        rate = {"point": parts[0], "mean": parts[0]}
    elif len(parts) == 2 and all(math.isfinite(x) for x in parts) and min(parts) >= MIN_BETA_PARAM \
            and math.isfinite(parts[0] + parts[1]) and max(parts) <= MAX_BETA_PARAM:
        rate = {"alpha": parts[0], "beta": parts[1], "mean": round(parts[0] / sum(parts), 6)}
    else:
        raise ValueError(f"--channel-rate {spec!r}: CID=E (0..1) or CID=ALPHA,BETA (both finite and in "
                         f"[{MIN_BETA_PARAM:g}, {MAX_BETA_PARAM:g}])")
    return cid.strip(), dict(rate, records=[], source=source.strip() or "UNSPECIFIED",
                             basis=f"OVERRIDE (disclosed, no ledger record): --channel-rate {body}"
                                   f" (source: {source.strip() or 'UNSPECIFIED'})",
                             label="UNCALIBRATED · OVERRIDE")


def refuse_channel_elements(engine, mechs) -> None:
    """F1-2: a complexity channel (a channel degrade or an over-application operator) is never a mechanism."""
    ops = getattr(engine, "channel_ops", set())
    bad = [m for m in mechs if m[0] == "degrade" and m[1] in ops]
    if bad:
        raise ValueError(f"--mechanisms names complexity channel(s) {[dm._label(m) for m in bad]}: a channel is reported "
                         f"and simulated as a channel (F1), never as a designed mechanism")


def channel_specs(engine, mod, slots: dm.Slots, led, model: str, overrides: dict, briefs=None, **excl) -> tuple:
    """(specs, unparameterized): every declared channel and control over-application, with its members (those the
    degrade moves), latent, batches and rate. A rate's unit and the channel's latent are cross-checked: a declared
    latent (or a kind default) must equal the unit the records are counted in after the supported member -> run
    conversion; a channel that declares no latent adopts the rate's unit (`latent_from` records which)."""
    decl = [(cid, c.get("kind"), c, None) for cid, c in ok.channels_of(mod).items()]
    decl += [(f"control:{r}", "control", {"degrade": c["over_application"], "members": c["members"],
                                          "source": (mod.RULES.get(r) or {}).get("source"),
                                          "description": f"{r} over-applied to its control members"}, r)
             for r, c in ok.controls_of(mod, engine.revision).items() if c["over_application"]]
    specs, missing = [], []
    for cid, kind, c, rule in decl:
        el = ("degrade", c["degrade"]) if c.get("degrade") else None
        declared = set(c.get("members") or [])
        members = [k for k in engine.keys if el and k in declared and k in engine.touched.get(el, set())]
        fam = c.get("family") or (((mod.RULES.get(rule) or {}).get("family") or rule) if kind == "control" else kind)
        declared_latent = c.get("latent")
        latent = declared_latent or CHANNEL_LATENT.get(kind, "member")
        rate = channel_rate(led, model, cid, kind, fam, overrides, **excl)
        latent_from = "declared" if declared_latent else "kind default"
        if rate and rate.get("unit"):                      # an explicit unit is checked even on a point rate
            if declared_latent and rate["unit"] != latent:
                raise ValueError(f"channel {cid}: its rate is counted in {rate['unit']!r} but the channel declares "
                                 f"the {latent!r} latent ({rate.get('basis')}); convert the record basis or correct "
                                 f"the declaration")
            if not declared_latent:
                if rate["unit"] != latent and members:
                    raise ValueError(f"channel {cid}: its rate is counted in {rate['unit']!r} but it has {len(members)} "
                                     f"member(s) and declares no latent; a run-unit trial means 'at least one member "
                                     f"failed' and cannot be applied member by member (declare the latent or convert "
                                     f"the records)")
                latent, latent_from = rate["unit"], "rate unit"
        if rate and "point" in rate:
            latent_from += " (unit-free point)" if not rate.get("unit") else " (point with an explicit unit)"
        batches = None
        if latent == "batch":
            batches = [b for b in ([k for k in shard if k in set(members)] for shard in
                                   dm.shards_for(engine, briefs, int(c.get("batch_size") or dm.SHARD_SIZE))) if b]
            if members and not batches:
                keys = sorted({k for b in briefs or [] for k in (b.get("keys") or [])})
                raise ValueError(f"channel {cid}: a batch latent over {len(members)} member(s), but no brief batch "
                                 f"intersects them (brief keys {keys[:10]}{'...' if len(keys) > 10 else ''}); every "
                                 f"draw would miss no batch and the channel could never fail")
        spec = {"id": cid, "kind": kind, "element": el, "members": members, "inert_members": len(declared) - len(members),
                "slots": [s for s in c.get("slots") or [] if s in slots.weight], "latent": latent,
                "latent_from": latent_from, "batches": batches,
                "source": c.get("source") or cid, "preregistered": bool(c.get("preregistered", True)),
                "description": c.get("description"), "family": fam, "rate": rate}
        usable = bool(rate) and ("point" in rate or rate.get("alpha") is not None)
        (specs if usable else missing).append(spec)
    return specs, missing


def _rate_draw(rate: dict, rng) -> float:
    if "point" in rate:
        pt = rate["point"]
        if isinstance(pt, bool) or not isinstance(pt, (int, float)) or not math.isfinite(pt) or not 0 <= pt <= 1:
            raise ValueError(f"a point rate must be a finite probability in [0, 1] (got {pt!r})")
        return pt
    a, b = rate.get("alpha"), rate.get("beta")
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and math.isfinite(a) and math.isfinite(b)
            and MIN_BETA_PARAM <= a <= MAX_BETA_PARAM and MIN_BETA_PARAM <= b <= MAX_BETA_PARAM
            and math.isfinite(a + b)):
        raise ValueError(f"a Beta rate needs finite alpha, beta in [{MIN_BETA_PARAM:g}, {MAX_BETA_PARAM:g}] "
                         f"(got {a!r}, {b!r}); a non-finite or out-of-range shape would hang, return nan or collapse "
                         f"to zero")
    return rng.betavariate(a, b)


def _sample_channel(c: dict, e: float, rng) -> tuple:
    """(members failed, slots failed) of one channel in one run."""
    if c["latent"] == "batch":
        hit = set().union(*[set(b) for b in c["batches"] if rng.random() < e]) if c["batches"] else set()
        return hit, set(c["slots"]) if hit else set()
    if c["latent"] == "member" and c["members"]:
        hit = {k for k in c["members"] if rng.random() < e}
        return hit, set(c["slots"]) if hit else set()
    on = rng.random() < e                                 # run latent, or a slots-only channel
    return (set(c["members"]) if on else set()), (set(c["slots"]) if on else set())


def p_any(rate: dict, n: int) -> dict:
    """P(at least one of n independent units fails): integrated over the rate's Beta, 1 - E[(1 - e)^n], and the
    plug-in 1 - (1 - mean)^n."""
    if "point" in rate:
        v = 1 - (1 - rate["point"]) ** n
        return {"integrated": round(v, 6), "plug_in": round(v, 6)}
    prod = 1.0
    for i in range(n):
        prod *= (rate["beta"] + i) / (rate["alpha"] + rate["beta"] + i)
    return {"integrated": round(1 - prod, 6), "plug_in": round(1 - (1 - rate["mean"]) ** n, 6)}


def channel_report(outcomes: Outcomes, slots: dm.Slots, channels: list, *, draws: int, seed: int) -> list:
    """Per channel: parameters, records, P(any unit fails) integrated and plug-in, and its expected loss alone (the
    channel by itself, mechanisms off), every number UNCALIBRATED."""
    out = []
    for c in channels:
        units = {"member": len(c["members"]), "batch": len(c["batches"] or [])}.get(c["latent"], 1)
        rng, lost, n = random.Random(seed), 0.0, max(ALONE_DRAWS, draws // 5)
        for _ in range(n):
            e = _rate_draw(c["rate"], rng)
            for _r in range(RUNS):
                hit, sl = _sample_channel(c, e, rng)
                failed = (outcomes.of({c["element"]: hit}, cache=False)[0] if hit and c["element"] else frozenset()) | sl
                lost += sum(slots.weight[i] for i in failed) / slots.total
        out.append({"id": c["id"], "kind": c["kind"], "latent": c["latent"], "latent_from": c.get("latent_from"),
                    "members": len(c["members"]),
                    "family": c["family"], "inert_members": c["inert_members"], "slots": c["slots"],
                    "unit": c["rate"].get("unit"), "converted_from": c["rate"].get("converted_from"),
                    "n": c["rate"].get("n"), "f": c["rate"].get("f"),
                    "n_eff": round(sum(x["n_eff"] for x in (c["rate"].get("tasks") or {}).values()), 4),
                    "rate_tasks": c["rate"].get("tasks"), "at_rho": c["rate"].get("at_rho"),
                    "batch_sizes": [len(b) for b in c["batches"]] if c["batches"] else None,
                    "source": c["source"], "override_source": c["rate"].get("source"),
                    "dropped": c["rate"].get("dropped") or [], "preregistered": c["preregistered"], "rate": c["rate"],
                    "P_any_unit_fails": dict(p_any(c["rate"], units), units=units,
                                             rule="1 - E[(1 - e)^N] over the rate's Beta; plug-in 1 - (1 - mean)^N"),
                    "expected_loss_alone": round(lost / (n * RUNS), 6), "label": c["rate"]["label"]})
    return out


def pair_key(a, b) -> str:
    """A landing-pair key that cannot collide when a mechanism label contains the separator: every '|' is escaped."""
    esc = lambda m: dm._label(m).replace("\\", "\\\\").replace("|", "\\|")  # noqa: E731
    return f"{esc(a)}|{esc(b)}"


def briefs_content_digest(briefs) -> str | None:
    """A digest of the briefs ACTUALLY simulated (the loaded object), so the key is bound to the inputs used, not to a
    later re-read of a mutable file."""
    return hashlib.sha256(json.dumps(briefs, sort_keys=True, default=str).encode()).hexdigest() if briefs else None


def briefs_digest(paths) -> dict:
    """The briefs' fingerprint: their paths, each file's sha256, and one aggregate digest (part of the pre-registration
    key, so changing a brief's keys changes the forecast's identity)."""
    paths = list(paths or [])
    return {"files": [tl._rel(f) for f in paths],
            "sha256": {tl._rel(f): tl.sha256_file(f) for f in paths},
            "digest": hashlib.sha256(json.dumps([[tl._rel(f), tl.sha256_file(f)] for f in paths],
                                                separators=(",", ":")).encode()).hexdigest() if paths else None}


def _missed_batches(batches: list, theta: float, rng) -> set:
    """M6: the batches one landing hits, exact. Each batch misses at b = 1 - (1 - theta)^(1/B); the run has landed, so
    the number of missed batches is a zero-truncated Binomial(B, b) (inverse-CDF, O(B), no rejection loop), and the
    missed batches are a uniform choice of that many. P(at least one) is 1 by construction.

    Degenerate cases are short-circuited: no batches misses nothing; theta >= 1 misses every batch; theta <= 0 misses
    none. The weights are computed in log space (math.lgamma), so a large B cannot overflow int->float, and the
    inverse CDF never selects a zero-weight k (the u == 0 quantile)."""
    B = len(batches)
    if not B or theta <= 0:
        return set()
    if theta >= 1:
        return set().union(*batches)
    if B > MAX_BATCHES:
        raise ValueError(f"{B} batches exceeds MAX_BATCHES={MAX_BATCHES}: refuse rather than overflow or approximate")
    # -expm1(log1p(-theta)/B) keeps precision for a tiny theta where 1-(1-theta)**(1/B) would round b to 0
    b = -math.expm1(math.log1p(-theta) / B)
    if b <= 0:                                            # a positive landing must miss at least one batch
        return set(rng.choice(batches)) if theta > 0 else set()
    if b >= 1:
        return set().union(*batches)
    lb, l1b = math.log(b), math.log1p(-b)
    logw = [math.lgamma(B + 1) - math.lgamma(k + 1) - math.lgamma(B - k + 1) + k * lb + (B - k) * l1b
            for k in range(1, B + 1)]                     # k = 1..B (zero misses is truncated away)
    m = max(logw)
    w = [math.exp(x - m) for x in logw]                   # normalised below; sums to theta / (1 - (1-b)^B)
    u, acc, k = rng.random() * sum(w), 0.0, None
    for i, wi in enumerate(w, 1):
        acc += wi
        if u <= acc and wi > 0:
            k = i
            break
    if k is None:
        k = next(i for i, wi in enumerate(w, 1) if wi > 0)
    idx = rng.sample(range(B), k)
    return set().union(*(batches[i] for i in idx)) if idx else set()


# ------------------------------------------------------------------ simulation

def shards_of(engine, e, size: int) -> list:
    keys = engine.keys
    return [set(keys[i:i + size]) & engine.touched[e] for i in range(0, len(keys), size)
            if set(keys[i:i + size]) & engine.touched[e]]


def simulate(engine, outcomes: Outcomes, gates: Gates, mechs: list, priors: dict, fam: dict, src: dict, *,
             draws: int, seed: int, dependence: str, extent: str, channels=(), briefs=None) -> dict:
    rng = random.Random(seed)
    if extent.startswith("shard:"):
        size = int(extent.split(":")[1])
        shards = {m: shards_of(engine, m, size) for m in mechs} if engine else {m: [None] for m in mechs}
    if extent == "batches":                               # M6: brief batches (trajectory_ledger briefs), else slices
        shards = {m: [s for s in (set(b) & engine.touched[m] for b in dm.shards_for(engine, briefs)) if s] or
                  [set(engine.touched[m])] for m in mechs} if engine else {m: [None] for m in mechs}
    views = list(gates.views)
    avgs = {v: [] for v in views}
    passes = {v: collections.Counter() for v in views}
    allp = {v: [] for v in views}
    pats = {v: [] for v in views}
    thetas = {m: [] for m in mechs}
    landed_runs, channel_runs, slot_fail, slot_all = (collections.Counter() for _ in range(4))
    pair_both, pair_either = collections.Counter(), collections.Counter()
    pairs = list(itertools.combinations(mechs, 2))
    run_scores = []
    for _ in range(draws):
        theta = {m: _rate_draw(priors[fam[m]], rng) for m in mechs}
        rates = {c["id"]: _rate_draw(c["rate"], rng) for c in channels}
        for m in mechs:
            thetas[m].append(theta[m])
        failed_sets = []
        for _r in range(RUNS):
            shared, one = {}, rng.random()
            failing, landed_here = {}, set()
            for m in mechs:
                u = rng.random() if dependence == "independent" else (
                    shared.setdefault(src[m], rng.random()) if dependence == "source" else one)
                if u < theta[m]:
                    landed_runs[m] += 1
                    landed_here.add(m)
                    if extent == "whole" or engine is None:
                        failing[m] = None
                    elif extent == "slip":
                        failing[m] = {rng.choice(sorted(engine.touched[m]))}
                    elif extent == "batches":
                        failing[m] = _missed_batches(shards[m], theta[m], rng)
                    else:
                        failing[m] = set(rng.choice(shards[m]))
            for a, b in pairs:
                kb = (dm._label(a), dm._label(b))
                if a in landed_here and b in landed_here:
                    pair_both[kb] += 1
                if a in landed_here or b in landed_here:
                    pair_either[kb] += 1
            forced = set()
            for c in channels:
                hit, sl = _sample_channel(c, rates[c["id"]], rng)
                if hit and c["element"] and failing.get(c["element"], set()) is not None:
                    failing[c["element"]] = set(failing.get(c["element"]) or set()) | hit
                forced |= sl
                channel_runs[c["id"]] += bool(hit or sl)
            failed = outcomes.of(failing, cache=not channels)[0] | forced
            failed_sets.append(failed)
            run_scores.append(1 - sum(outcomes.slots.weight[i] for i in failed) / outcomes.slots.total)
            slot_fail.update(failed)
        slot_all.update(set.intersection(*map(set, failed_sets)))
        res = gates.of(failed_sets)
        for v in views:
            avgs[v].append(res[v]["avg"])
            pats[v].append(res[v]["patterns"])
            for g, ok_ in res[v]["gates"].items():
                passes[v][g] += ok_
            passes[v]["all"] += res[v]["all"]
            allp[v].append(res[v]["all"])
    rs = sorted(run_scores)
    qr = lambda p: rs[min(len(rs) - 1, max(0, int(round(p * (len(rs) - 1)))))]  # noqa: E731
    order = sorted(slot_fail, key=lambda s: (-slot_fail[s], outcomes.slots.ids.index(s)))
    top = order[:25]
    slot_cell = lambda s: {"P_fail": round(slot_fail[s] / (draws * RUNS), 4),  # noqa: E731
                           "P_fails_all_six": round(slot_all[s] / draws, 4)}
    out = {"dependence": dependence, "extent": extent, "draws": draws, "seed": seed, "views": {},
           "landing_rate_simulated": {dm._label(m): round(landed_runs[m] / (draws * RUNS), 4) for m in mechs},
           "landing_pair_counts": {pair_key(a, b): {"both": pair_both[(dm._label(a), dm._label(b))],
                                                    "either": pair_either[(dm._label(a), dm._label(b))],
                                                    "runs": draws * RUNS}
                                   for a, b in itertools.combinations(mechs, 2)},
           "landing_pairs": {pair_key(a, b): {
                                 "both": round(pair_both[(dm._label(a), dm._label(b))] / (draws * RUNS), 4),
                                 "either": round(pair_either[(dm._label(a), dm._label(b))] / (draws * RUNS), 4)}
                             for a, b in itertools.combinations(mechs, 2)},
           "run_score_band_10_90": [round(qr(0.1), 4), round(qr(0.9), 4)] if rs else None,
           "channels_hit_rate": {c["id"]: round(channel_runs[c["id"]] / (draws * RUNS), 4) for c in channels},
           "slots": {s: slot_cell(s) for s in (order + [x for x in outcomes.slots.ids if x not in slot_fail])},
           "slots_top_25": {s: slot_cell(s) for s in top},
           "slots_rule": "P_fails_all_six is all-fail justification workload (an all-fail rubric needs a written "
                         "justification), never a block; slots reports every slot, slots_top_25 is the presentation "
                         "short list"}
    for v in views:
        xs = sorted(avgs[v])
        q = lambda p: xs[min(len(xs) - 1, max(0, int(round(p * (len(xs) - 1)))))]  # noqa: E731
        voi = []
        for m in mechs:
            med = statistics.median(thetas[m])
            hi = [a for t, a in zip(thetas[m], allp[v]) if t > med]
            lo = [a for t, a in zip(thetas[m], allp[v]) if t <= med]
            ph, pl = (sum(hi) / len(hi) if hi else 0.0), (sum(lo) / len(lo) if lo else 0.0)
            voi.append({"mechanism": dm._label(m), "P_all_if_rate_above_median": round(ph, 4),
                        "P_all_if_rate_below_median": round(pl, 4), "spread": round(abs(ph - pl), 4)})
        voi.sort(key=lambda x: -x["spread"])
        out["views"][v] = {"E_average": round(sum(xs) / len(xs), 4), "band_10_90": [round(q(0.1), 4), round(q(0.9), 4)],
                           "P_gate": {g: round(passes[v][g] / draws, 4) for g in DIFFICULTY_GATES},
                           "P_all": round(passes[v]["all"] / draws, 4), "value_of_information": voi,
                           "E_patterns": round(sum(pats[v]) / len(pats[v]), 4)}
    return out


# ------------------------------------------------------------------ exhaustive (whole-rule landings)

def exhaustive(outcomes: Outcomes, gates: Gates, mechs: list, *, p_grid: float = 0.01, expect=(), break_even=()) -> dict:
    k = len(mechs)
    subsets = [frozenset(s) for n in range(k + 1) for s in itertools.combinations(range(k), n)]
    per = []
    for s in subsets:
        failed, lost = outcomes.of({mechs[i]: None for i in sorted(s)})
        per.append({"failing": [dm._label(mechs[i]) for i in sorted(s)], "score": (outcomes.slots.total - lost)
                    / outcomes.slots.total, "failed": failed, "size": len(s)})
    multisets = list(itertools.combinations_with_replacement(range(len(per)), RUNS))
    views = list(gates.views)
    passing = {v: [] for v in views}
    rows = []
    for ms in multisets:
        res = gates.of([per[i]["failed"] for i in ms])
        rows.append((ms, res))
        for v in views:
            if res[v]["all"]:
                passing[v].append(ms)

    def q(p, s):
        return (p ** per[s]["size"]) * ((1 - p) ** (k - per[s]["size"]))

    def prob(ms, p):
        c = collections.Counter(ms)
        coef = math.factorial(RUNS)
        for n in c.values():
            coef //= math.factorial(n)
        return coef * math.prod(q(p, s) ** n for s, n in c.items())

    grid = [round(i * p_grid, 10) for i in range(int(round(1 / p_grid)) + 1)]
    curves = {}
    for v in views:
        pts = [(p, sum(prob(ms, p) for ms in passing[v])) for p in grid]
        best = max(pts, key=lambda x: x[1])
        curves[v] = {"max_P_pass": round(best[1], 6), "at_p": best[0], "grid_step": p_grid}

    def expected(p):
        return sum(q(p, s) * per[s]["score"] for s in range(len(per)))

    def crossing(t):
        lo_p, hi_p = None, None
        for a, b in zip(grid, grid[1:]):
            if (expected(a) - t) * (expected(b) - t) <= 0 and expected(a) != expected(b):
                lo_p, hi_p = a, b
                break
        if lo_p is None:
            return None
        for _ in range(60):
            mid = (lo_p + hi_p) / 2
            if (expected(lo_p) - t) * (expected(mid) - t) <= 0:
                hi_p = mid
            else:
                lo_p = mid
        return round((lo_p + hi_p) / 2, 4)

    perfect = next(i for i, x in enumerate(per) if not x["failing"])
    scores = [x["score"] for x in per]
    non_perfect = [s for i, s in enumerate(scores) if i != perfect]
    sd_without = max((statistics.pstdev([scores[i] for i in ms]) for ms in multisets if perfect not in ms), default=0.0)
    structure = {"perfect_run_score": scores[perfect],
                 "min_mean_with_a_perfect_run": (scores[perfect] + (RUNS - 1) * min(scores)) / RUNS,
                 "score_range_without_a_perfect_run": [min(non_perfect), max(non_perfect)] if non_perfect else None,
                 "max_sd_without_a_perfect_run": sd_without}
    out = {"mechanisms": [dm._label(m) for m in mechs],
           "outcomes": [{"failing": x["failing"], "score": x["score"], "failed_slots": sorted(x["failed"])} for x in per],
           "multisets": len(multisets), "views": {}, "expected_average": {str(p): expected(p) for p in expect},
           "break_even": {str(t): crossing(t) for t in break_even}, "structure": structure}
    for v in views:
        cap = gates.views[v]["cap"]
        sub = [{"runs": [per[i]["failing"] for i in ms], "mean": res[v]["avg"], "sd": res[v]["sd"],
                "patterns": res[v]["patterns"], "full_passes": res[v]["full_passes"],
                "failed_gates": [g for g, ok_ in res[v]["gates"].items() if not ok_]}
               for ms, res in rows if res[v]["avg"] < cap]
        sub.sort(key=lambda x: x["mean"])
        out["views"][v] = {"cap": cap, "passing_multisets": len(passing[v]), "P_pass_curve": curves[v],
                           "passing": [[per[i]["failing"] for i in ms] for ms in passing[v][:20]],
                           "below_cap": len(sub), "below_cap_examples": sub[:6]}
    return out


# ------------------------------------------------------------------ pre-registration scorer

def _check_hash(path: Path, want: str) -> str | None:
    got = tl.sha256_file(path)
    return None if got == want else f"{path}: sha256 {got[:16]} is not the recorded {want[:16]}"


def _landings(verdicts: dict, rule_names=None) -> dict:
    out = {}
    for lab, r in verdicts["runs"].items():
        out[lab] = sorted(k for k, v in r["rules"].items() if v["verdict"] == "LANDED" and (not rule_names or k in rule_names))
    return out


def _partial(verdicts: dict, reading: str) -> list:
    out = []
    for lab, r in verdicts["runs"].items():
        for rule, v in r["rules"].items():
            if v["verdict"] != "LANDED" or len(v["landed_keys"]) >= v["cohort"]:
                continue
            briefs = {b["event"]: b for kd in v["keys"] for b in kd["covering_briefs"]}.values()
            carry = sum(1 for b in briefs if (b["text_carries"] if reading == "text" else b["carries"]))
            omit = len(briefs) - carry
            out.append({"run": lab, "rule": rule, "keys": len(v["landed_keys"]), "cohort": v["cohort"],
                        "covering_briefs": len(briefs), "carry": carry, "omit": omit, "omitted": omit > carry})
    return out


def evaluate(check: dict, base: Path) -> tuple:
    kind = check["kind"]
    if kind == "not_tested":
        return None, check.get("why", "not tested")
    src = json.loads((base / check["evidence"]).read_text())
    if kind == "gates_fail":
        if "verdict_view" in src:          # difficulty_stats.py --json: its top-level gates are the view of record
            if src.get("spec_version") != check["view"]:
                raise ValueError(f"{check['evidence']} holds {src.get('spec_version')} gates, not {check['view']}")
            failed = [k for k in DIFFICULTY_GATES if src["gates"][k]["verdict"].startswith("FAIL")]
            return bool(failed), f"{check['view']} ({src['verdict_view']} view of record) blocking {failed}"
        g = src["gates"][check["view"]]          # surface_grader.py output
        return bool(g["difficulty_blocking"]), f"{check['view']} blocking {g['difficulty_blocking']}"
    if kind == "no_rule_lands_in":
        land = _landings(src, set(check["rules"]))
        per_rule = collections.Counter(r for rules in land.values() for r in rules)
        top = max(per_rule.values(), default=0)
        return top < check["threshold"], f"most landings for one rule: {top} of {len(land)} runs ({dict(per_rule)})"
    if kind == "degrade_trusted_at_most":
        n = sum(1 for r in src["runs"].values() if r["degrades"].get(check["degrade"], {}).get("verdict") == "LANDED")
        return n <= check["max_runs"], f"trusted in {n} of {len(src['runs'])} runs"
    if kind == "runs_with_landing_at_least":
        land = _landings(src)
        runs = sorted(lab for lab, rules in land.items() if rules)
        return len(runs) >= check["min_runs"], f"{len(runs)} runs with a landed rule: {runs}"
    if kind == "partial_landings_brief_omission":
        res = {}
        for reading in ("text", "text+referenced"):
            items = _partial(src, reading)
            res[reading] = (sum(x["omitted"] for x in items), len(items), items)
        omitted, total, items = res[check.get("reading", "text")]
        alt = res["text+referenced" if check.get("reading", "text") == "text" else "text"]
        outcome = total > 0 and omitted / total >= check["share"]
        return outcome, (f"{omitted} of {total} partial landings had briefs that omitted the rule "
                         f"({check.get('reading', 'text')} reading; the other reading gives {alt[0]} of {alt[1]}): "
                         + "; ".join(f"{x['run']} {x['rule']} carry {x['carry']}/{x['covering_briefs']}" for x in items))
    raise ValueError(f"unknown check kind {kind!r}")


def score(doc: dict, base: Path) -> dict:
    errors = []
    for rel, want in (doc.get("hashes") or {}).items():
        err = _check_hash(base / rel, want)
        if err:
            errors.append(err)
    rows, brier = [], []
    if not errors:
        for p in doc["predictions"]:
            outcome, detail = evaluate(p["check"], base)
            rows.append({"id": p["id"], "prediction": p["text"], "confidence": p["confidence"], "outcome": outcome,
                         "detail": detail})
            if outcome is not None:
                brier.append((p["confidence"] - (1.0 if outcome else 0.0)) ** 2)
    return {"kind": "PREREGISTRATION_SCORE", "tool": VERSION, "note": NOTE, "preregistration": doc.get("preregistration"),
            "hash_errors": errors, "predictions": rows, "scored": len(brier),
            "brier": round(sum(brier) / len(brier), 6) if brier else None, "constant_half_brier": 0.25}


# ------------------------------------------------------------------ comparison after the runs (plan §14.7)

TRIAL_VERDICTS = ("LANDED",) + hl.NOT_LANDED          # NOT-REACHED and CONFOUNDED runs are not trials


def beta_binomial(n: int, a: float, b: float) -> list:
    """P(k landings in n runs) when every run lands with the same theta ~ Beta(a, b): the forecast's model."""
    def lbeta(x, y):
        return math.lgamma(x) + math.lgamma(y) - math.lgamma(x + y)
    return [math.exp(math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1) + lbeta(k + a, n - k + b)
                     - lbeta(a, b)) for k in range(n + 1)]


def central_interval(pmf: list, mass: float = 0.90) -> list:
    """[lo, hi]: the smallest counts whose CDF reaches (1 - mass) / 2 and (1 + mass) / 2."""
    tail, acc, lo, hi = (1 - mass) / 2, 0.0, None, None
    for k, p in enumerate(pmf):
        acc += p
        if lo is None and acc >= tail - 1e-12:
            lo = k
        if hi is None and acc >= 1 - tail - 1e-12:
            hi = k
    return [lo, len(pmf) - 1 if hi is None else hi]


def observed_gates(grades: dict | None, difficulty: dict | None) -> dict:
    """{view: {gate: passed, all, average, source}}; difficulty_stats output (the gate of record) wins for its view."""
    out = {}
    if grades:
        for v, x in (grades.get("gates") or {}).items():
            res = {k: x["difficulty_gates"][k]["verdict"].startswith("PASS") for k in DIFFICULTY_GATES}
            rates = [r["weighted_pass_rate"] for r in x["per_rollout"]]
            out[v] = dict(res, all=all(res.values()), average=sum(rates) / len(rates),
                          source="surface_grader.py (a design check, not the grading of record)")
    if difficulty:
        v = difficulty["spec_version"]
        res = {k: difficulty["gates"][k]["verdict"].startswith("PASS") for k in DIFFICULTY_GATES}
        rates = [r["weighted_pass_rate"] for r in difficulty["per_rollout"]]
        out[v] = dict(res, all=all(res.values()), average=sum(rates) / len(rates),
                      source=f"difficulty_stats.py ({difficulty['verdict_view']} view of record)")
    return out


def _node(run: dict, mech_id: str):
    kind, _, name = mech_id.partition(":")
    return ((run.get("rules") if kind == "rule" else run.get("degrades")) or {}).get(name)


def landing_check(forecast: dict, verdicts: dict) -> list:
    mixed = {lab for lab, r in verdicts["runs"].items() if (r.get("provenance") or {}).get("mixed_model")}
    out = []
    for m in forecast["mechanisms"]:
        a, b = m["prior"]["alpha"], m["prior"]["beta"]
        row = {"mechanism": m["id"], "family": m["family"], "prior": [a, b]}
        for scope, labels in (("all runs", list(verdicts["runs"])),
                              ("excluding mixed-model runs", [x for x in verdicts["runs"] if x not in mixed])):
            per = [(lab, (_node(verdicts["runs"][lab], m["id"]) or {}).get("verdict")) for lab in labels]
            trials = [lab for lab, vd in per if vd in TRIAL_VERDICTS]
            landed = [lab for lab, vd in per if vd == "LANDED"]
            iv = central_interval(beta_binomial(len(trials), a, b)) if trials else None
            row[scope] = {"runs": len(trials), "landed": len(landed), "landed_in": landed, "interval_90": iv,
                          "inside": iv[0] <= len(landed) <= iv[1] if iv else None,
                          "not_trials": [f"{lab} {vd or 'not observed'}" for lab, vd in per if lab not in trials]}
        out.append(row)
    return out


def forecast_checks(forecast: dict, observed: dict) -> list:
    out = []
    for s in forecast["scenarios"]:
        for v, x in s["views"].items():
            o = observed.get(v)
            if not o:
                continue
            lo, hi = x["band_10_90"]
            p_obs = x["P_all"] if o["all"] else 1 - x["P_all"]
            gates = {g: round(x["P_gate"][g] if o[g] else 1 - x["P_gate"][g], 4) for g in DIFFICULTY_GATES}
            out.append({"scenario": f"{s['dependence']} {s['extent']}", "view": v, "observed_average": round(o["average"], 4),
                        "band_10_90": [lo, hi], "average_in_band": lo <= o["average"] <= hi, "E_average": x["E_average"],
                        "observed_all_gates": o["all"], "P_observed_all_gates": round(p_obs, 4),
                        "observed_verdict_at_least_10pct": p_obs >= 0.10, "P_observed_per_gate": gates})
    return out


def per_run_table(grades: dict, verdicts: dict, class_field: str, costs: bool = True) -> list:
    rows = []
    for lab, g in grades["runs"].items():
        v = (verdicts.get("runs") or {}).get(lab) or {}
        items = v.get("items") or []
        by = collections.defaultdict(set)
        for i in items:
            c = i.get("classification")
            if c == "cascade":
                continue
            if c == "mechanism":
                for r in i.get("attributed") or i.get("candidates") or ["unattributed"]:
                    by[r].add(i["key"])
            else:
                by[c or "unclassified"].add(f"{i['key']} {i['field']}" if c == "slip" else i["key"])
        fams = sorted({hl.model_family(m) for m in g.get("models") or [] if not str(m).startswith("<")})
        fb = g.get("fallbacks") or []
        model = " + ".join(fams) + (f" (fallback at event {', '.join(map(str, fb))}; "
                                    + ("mixed-model: the fallback model ran the main agent from then"
                                       if g.get("mixed_model") else "not mixed: after the deliverables") + ")" if fb else "")
        cost = None
        if costs and g.get("file") and Path(g["file"]).is_file():
            try:
                cost = (tl.validity(tl.load(Path(g["file"]), lab)).get("final_result") or {}).get("total_cost_usd")
            except Exception:  # noqa: BLE001 - a cost the export does not carry is reported as unknown
                cost = None
        rows.append({"run": lab, "model": model, "mixed_model": bool(g.get("mixed_model")),
                     "counted_calls": g.get("counted_calls"), "cost_usd": cost,
                     "register": {"NATIVE_SHEET": "Sheet", "CSV": "CSV"}.get(g.get("register_kind"), g.get("register_kind")),
                     "rows": g.get("rows"), "wrong_rows": len({i["key"] for i in items}),
                     "class_errors": len({i["key"] for i in items if i.get("field") == class_field}),
                     "score": g.get("score"), "baseline": lab != "precheck",
                     "causes": "; ".join(f"{k}: {', '.join(sorted(x))}" for k, x in sorted(by.items())) or "none"})
    return rows


def mechanism_summary(verdicts: dict, registers: list) -> dict:
    runs = verdicts["runs"]
    n = len(runs)
    landed = []
    for lab, r in runs.items():
        for rule, x in (r.get("rules") or {}).items():
            if x["verdict"] == "LANDED":
                bt = x.get("brief_transmission") or {}
                landed.append({"rule": rule, "run": lab, "keys": len(x.get("landed_keys") or []),
                               "landed_keys": x.get("landed_keys"), "brief_transmission": bt,
                               "text_omit": (bt.get("covering_briefs") or 0) - (bt.get("carry_in_text") or 0),
                               "flags": x.get("flags") or []})
    every = sorted(k for k, c in (verdicts.get("summary") or {}).items() if c.get("LEAKED") == n)
    never = sorted(k for k, c in (verdicts.get("reach_summary") or {}).items() if c.get("NOT-READ") == n)
    kinds = collections.Counter(r["register"] for r in registers)
    return {"landed": landed, "leaked_in_every_run": every, "never_read": never, "register_kinds": dict(kinds),
            "runs": n}


def compare(forecasts: dict, verdicts: dict, grades: dict, *, difficulty=None, predictions=None, base=None,
            precheck_call=None, old_band=None, class_field="handoff class", costs=True) -> dict:
    observed = observed_gates(grades, difficulty)
    table = per_run_table(grades, verdicts, class_field, costs)
    rep = {"kind": "FORECAST_COMPARISON", "tool": VERSION, "label": LABEL, "note": NOTE,
           "observed": observed, "per_run": table, "mechanisms": mechanism_summary(verdicts, table), "forecasts": {}}
    bound = all(tl.binding_ok(r.get("binding"))[0] for r in verdicts["runs"].values())   # on evidence, never a label
    cited = all(x.get("citations") for r in verdicts["runs"].values() for x in (r.get("rules") or {}).values()
                if x["verdict"] == "LANDED")
    unclassified = sum(1 for r in verdicts["runs"].values() for i in r.get("items") or []
                       if i.get("classification") not in ("mechanism", "slip", "representation", "cascade"))
    queued = {lab: (r.get("review_queue") or {}).get("unclassified_calls") for lab, r in verdicts["runs"].items()}
    rep["tooling"] = {"every_run_bound": bound, "landed_verdicts_cite_events": cited, "unclassified_items": unclassified,
                      "calls_queued_for_review": {k: (len(v) if isinstance(v, list) else v) for k, v in queued.items()},
                      "surface_coverage": grades.get("coverage"),
                      "pass": bound and cited and unclassified == 0}
    for label, f in forecasts.items():
        lc = landing_check(f, verdicts)
        fc = forecast_checks(f, observed)
        rep["forecasts"][label] = {
            "label": f.get("label"), "model": f.get("model"), "preregistration": f.get("preregistration"),
            "landing": lc, "scenarios": fc,
            "summary": {"mechanisms_inside_interval": f"{sum(1 for x in lc if x['all runs']['inside'])}/"
                                                      f"{sum(1 for x in lc if x['all runs']['inside'] is not None)}",
                        "scenarios_average_in_band": f"{sum(1 for x in fc if x['average_in_band'])}/{len(fc)}",
                        "scenarios_observed_verdict_at_least_10pct":
                            f"{sum(1 for x in fc if x['observed_verdict_at_least_10pct'])}/{len(fc)}"}}
    goal_view = "V3" if "V3" in observed else next(iter(observed), None)
    goal = observed.get(goal_view) or {}
    rep["goal"] = {"view": goal_view, "passes_all_gates": goal.get("all"), "average": goal.get("average"),
                   "gates": {g: goal.get(g) for g in DIFFICULTY_GATES}}
    screens = {}
    if precheck_call:
        screens["run-1 call"] = {"call": precheck_call, "agreed": (precheck_call == "go") == bool(goal.get("all"))}
    if old_band is not None:
        call = "go" if old_band >= 3 else "no-go"
        screens["/hardness band"] = {"band": old_band, "call": call, "agreed": (call == "go") == bool(goal.get("all"))}
    rep["screens"] = screens
    if predictions is not None:
        rep["scorecard"] = score(predictions, base)
    return rep


def comparison_markdown(rep: dict) -> str:
    L = [f"# Forecast comparison — {rep['label']}", "", f"> {rep['note']}", "", "## Per run", "",
         "| Run | Model | Counted calls | Cost | Register | Wrong rows | Class errors | Score | Cause of misses |",
         "|---|---|---|---|---|---|---|---|---|"]
    for r in rep["per_run"]:
        cost = f"${r['cost_usd']:.2f}" if isinstance(r["cost_usd"], (int, float)) else "unknown"
        L.append(f"| {r['run']} | {r['model']} | {r['counted_calls']} | {cost} | {r['register']} | {r['wrong_rows']} | "
                 f"{r['class_errors']} | {r['score']:.1%} | {r['causes']} |")
    for v, o in rep["observed"].items():
        L.append(f"\n{v}: six-run average {o['average']:.1%}; gates " + ", ".join(
            f"{g} {'PASS' if o[g] else 'FAIL'}" for g in DIFFICULTY_GATES) + f" — all {'PASS' if o['all'] else 'FAIL'} "
                 f"({o['source']})")
    m = rep["mechanisms"]
    L += ["", "## Mechanisms", ""]
    for x in m["landed"]:
        bt = x["brief_transmission"]
        L.append(f"- **LANDED** {x['rule']} in {x['run']}, {x['keys']} key(s) {x['landed_keys'][:12]}; briefs "
                 f"{bt.get('covering_briefs', 0)}: rule in the text {bt.get('carry_in_text', 0)}, by a referenced file the "
                 f"worker read {bt.get('carry_by_reference', 0)}, omitted {bt.get('omit', 0)} (omitting writers "
                 f"{bt.get('writers_of_omitting') or {}}); text-only reading: omitted {x['text_omit']}"
                 + (f"; flags: {'; '.join(f[:90] for f in x['flags'])}" if x["flags"] else ""))
    L.append(f"- **Leaked in all {m['runs']} runs:** {', '.join(m['leaked_in_every_run']) or 'none'}")
    L.append(f"- **Never read in any run:** {', '.join(m['never_read']) or 'none'}")
    L.append(f"- **Registers:** {m['register_kinds']}")
    t = rep["tooling"]
    L += ["", "## Plan §14.7 checks", "",
          f"- Tooling: {'PASS' if t['pass'] else 'FAIL'} (every run bound {t['every_run_bound']}; landed verdicts cite "
          f"events {t['landed_verdicts_cite_events']}; unclassified items {t['unclassified_items']}; calls queued for "
          f"review {t['calls_queued_for_review']})"]
    for label, f in rep["forecasts"].items():
        s = f["summary"]
        L.append(f"- Forecast `{label}` ({f['label']}; {f['model']}; preregistration "
                 f"{(f.get('preregistration') or {}).get('id')}): landing counts inside the 90 % interval "
                 f"{s['mechanisms_inside_interval']}; six-run average inside the 10–90 % band in "
                 f"{s['scenarios_average_in_band']} scenarios; P(observed gate verdict) ≥ 10 % in "
                 f"{s['scenarios_observed_verdict_at_least_10pct']} scenarios")
        for x in f["landing"]:
            a = x["all runs"]
            L.append(f"  - {x['mechanism']} ({x['family']}, Beta{tuple(x['prior'])}): landed {a['landed']}/{a['runs']} "
                     f"{a['landed_in']}, 90 % interval {a['interval_90']} → {'inside' if a['inside'] else 'OUTSIDE'}"
                     + (f"; excluding mixed-model runs {x['excluding mixed-model runs']['landed']}/"
                        f"{x['excluding mixed-model runs']['runs']}" if x['excluding mixed-model runs']['runs']
                        != a['runs'] else ""))
        for x in f["scenarios"]:
            L.append(f"  - {x['scenario']} {x['view']}: band {x['band_10_90']} vs {x['observed_average']:.3f} → "
                     f"{'inside' if x['average_in_band'] else 'OUTSIDE'}; P(observed all-gates verdict) "
                     f"{x['P_observed_all_gates']:.3f}")
    g = rep["goal"]
    L.append(f"- Goal ({g['view']}): the six runs {'pass' if g['passes_all_gates'] else 'fail'} the gates "
             f"(average {g['average']:.1%})" if g.get("average") is not None else "- Goal: no observed gates")
    for k, x in rep["screens"].items():
        L.append(f"- Screen {k}: {x.get('call')} → {'agreed' if x['agreed'] else 'disagreed'} with the six-run outcome")
    sc = rep.get("scorecard")
    if sc:
        L += ["", "## Pre-registration scorecard", "", "| # | Prediction | Confidence | Outcome |", "|---|---|---|---|"]
        for p in sc["predictions"]:
            L.append(f"| {p['id']} | {p['prediction']} | {p['confidence']:.2f} | "
                     f"{'not tested' if p['outcome'] is None else p['outcome']}: {p['detail'][:110]} |")
        L.append(f"\nBrier over {sc['scored']} scored predictions: {sc['brier']} (constant 0.5 scores 0.25)"
                 + (f"; HASH MISMATCH {sc['hash_errors']}" if sc["hash_errors"] else ""))
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ reports

def to_text(rep: dict) -> str:
    lines = [f"HARDNESS FORECAST · {rep['label']} · model {rep['model']} · {rep['revision']} · {NOTE}"]
    for m in rep["mechanisms"]:
        p = m["prior"]
        rate = f"e = {p['point']}" if "point" in p else f"Beta({p['alpha']}, {p['beta']})"
        lines.append(f"  {m['id']:44} family {m['family'][:40]:40} {rate} mean {p['mean']:.2f} "
                     f"n_eff {p['n_eff']} records {len(p['record_ids'])}" + (f" [{p['basis'][:50]}]" if p.get("basis") else ""))
    for s in rep.get("scenarios") or []:
        cells = " · ".join(f"{v} E[avg] {x['E_average']:.3f} [{x['band_10_90'][0]:.3f}, {x['band_10_90'][1]:.3f}] "
                           f"P(all) {x['P_all']:.3f}" for v, x in s["views"].items())
        lines.append(f"  {s['dependence']:11} {s['extent']:8} {cells}")
    for v, r in (rep.get("summary") or {}).items():
        lines.append(f"  {v}: P(all four difficulty gates) {r['P_all_min']:.3f}-{r['P_all_max']:.3f} across scenarios; "
                     f"value of information (first scenario): {r['voi'][:3]}")
    for c in rep.get("channels") or []:
        r, pa = c["rate"], c["P_any_unit_fails"]
        rate = f"e = {r['point']}" if "point" in r else f"e ~ Beta({r['alpha']}, {r['beta']})"
        lines.append(f"  channel {c['id']} ({c['kind']}, {c['latent']} latent [{c.get('latent_from')}], "
                     f"{c['members']} member(s)"
                     + (f", slots {c['slots']}" if c["slots"] else "")
                     + (f", {c['unit']} trials" if c.get("unit") else "")
                     + (f" (converted from {c['converted_from']})" if c.get("converted_from") else "")
                     + f"): {rate} [{r['basis'][:60]}] · P(any of "
                     f"{pa['units']} fails) {pa['integrated']:.3f} integrated vs {pa['plug_in']:.3f} plug-in · expected "
                     f"loss alone {c['expected_loss_alone']:.4f} · {c['label']}")
    for c in rep.get("unparameterized_channels") or []:
        lines.append(f"  channel {c['id']} ({c['kind']}): UNPARAMETERIZED - {c['why']}")
    s0 = (rep.get("scenarios") or [{}])[0]
    if s0.get("slots"):
        lines.append(f"  slots most at risk ({s0['dependence']} {s0['extent']}; P(fail) / P(fails all six) - all-fail "
                     f"justification workload, never a block): " + ", ".join(
                         f"{s} {x['P_fail']:.2f}/{x['P_fails_all_six']:.2f}" for s, x in list(s0["slots"].items())[:8]))
    e = rep.get("exhaustive")
    if e:
        lines.append(f"  exhaustive over {e['multisets']} six-run multisets of {len(e['outcomes'])} outcomes:")
        for v, x in e["views"].items():
            lines.append(f"    {v} (cap {x['cap']:.2f}): {x['passing_multisets']} pass all gates · max P(pass) "
                         f"{x['P_pass_curve']['max_P_pass']:.4f} at p = {x['P_pass_curve']['at_p']} · "
                         f"{x['below_cap']} multisets below the cap")
        st = e["structure"]
        lines.append(f"    min mean with a perfect run {st['min_mean_with_a_perfect_run']:.4f}; scores without one "
                     f"{st['score_range_without_a_perfect_run']}; max SD without one {st['max_sd_without_a_perfect_run']:.4f}")
        if e["expected_average"]:
            lines.append("    E[average](p): " + ", ".join(f"p={p}: {x:.4f}" for p, x in e["expected_average"].items()))
        if e["break_even"]:
            lines.append("    break-even p: " + ", ".join(f"{t}: {x}" for t, x in e["break_even"].items()))
    return "\n".join(lines)


# ------------------------------------------------------------------ self-test

_CHANNEL_SOLVER = """
import collections
KEY_REGEX = r"[ABK]-\\d{2}"
CLASS_FIELD, GROUPS_FIELD = "class", "groups"
A = [f"A-{n:02d}" for n in range(1, 41)]
RULES = {"late_a": {"mechanism": "A15", "family": "F", "requirement": "R1", "natural_reading": "x", "nodes": ["T1"],
                    "decides": ["status"]},
         "rule_k": {"mechanism": "A15", "family": "F", "requirement": "R1", "natural_reading": "y", "nodes": ["T2"],
                    "decides": ["status"], "controls": ["K-01"], "over_application": "over:k"}}
CHANNELS = {"scale:a": {"kind": "scale", "degrade": "slip:a", "members": A},
            "linked:a": {"kind": "scale", "latent": "run", "degrade": "slip:a", "members": A},
            "deleg:a": {"kind": "delegation", "degrade": "slip:a", "members": A},
            "pair:b": {"kind": "scale", "degrade": "slip:b", "members": ["B-01", "B-02"]},
            "duo:ind": {"kind": "scale", "degrade": "slip:duo", "members": ["A-01", "A-02"]},
            "duo:link": {"kind": "scale", "latent": "run", "degrade": "slip:duo", "members": ["A-01", "A-02"]},
            "surface:deck": {"kind": "tool_surface", "slots": ["D1"]},
            "ghost": {"kind": "scale", "degrade": "slip:a", "members": ["A-03"]}}
def load_state(sql_text, revision=None):
    return {"revision": revision or "r1"}
def keys():
    return A + ["B-01", "B-02", "K-01"]
def _on(spec, name, k):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and k in d[1]) for d in spec)
def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    out = {}
    for k in keys_ or keys():
        s = "bad" if k in ("B-02", "K-01") else "ok"
        if k.startswith("A") and (_on(disable, "late_a", k) or _on(degrade, "slip:a", k) or _on(degrade, "slip:duo", k)):
            s = "bad"
        if k.startswith("B") and _on(degrade, "slip:b", k):
            s = "bad" if s == "ok" else "ok"
        if k == "K-01" and (_on(disable, "rule_k", k) or _on(degrade, "over:k", k)):
            s = "ok"
        g = (["ok_a"] if k.startswith("A") else ["ok_b"] if k.startswith("B") else []) if s == "ok" else []
        out[k] = {"key": k, "status": s, "class": "READY" if s == "ok" else "HOLD", "groups": g, "evidence": {}}
    return out
def aggregates(rows):
    return {"classes": dict(collections.Counter(v["class"] for v in rows.values())), "groups": {}}
def evidence(rows, key, field):
    return []
"""
_CHAIN_SOLVER = """
KEY_REGEX = r"C-\\d{2}"
CLASS_FIELD, GROUPS_FIELD = "class", "groups"
RULES = {"noop": {"mechanism": "A9", "requirement": "R1", "natural_reading": "z", "nodes": ["T1"], "decides": ["value"]}}
CHANNELS = {f"chain:{i}": {"kind": "chain", "degrade": f"break:{i}", "members": [f"C-0{i}"]} for i in (1, 2, 3)}
def load_state(sql_text, revision=None):
    return {"revision": "r1"}
def keys():
    return ["C-01", "C-02", "C-03"]
def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    on = lambda i: any(d == f"break:{i}" or (isinstance(d, tuple) and d[0] == f"break:{i}" and f"C-0{i}" in d[1])
                       for d in degrade)
    broken = [i for i in (1, 2, 3) if on(i)]
    return {f"C-0{n}": {"key": f"C-0{n}", "value": "bad" if any(i <= n for i in broken) else "ok", "class": "READY",
                        "groups": [], "evidence": {}} for n in (1, 2, 3) if not keys_ or f"C-0{n}" in keys_}
def aggregates(rows):
    return {"classes": {}, "groups": {}}
def evidence(rows, key, field):
    return []
"""


def _self_test_channels(tmp) -> str:
    """F1 + M6 planted cases (each Monte Carlo figure within a stated tolerance of its exact value)."""
    sp = Path(tmp) / "channel_solver.py"
    sp.write_text(_CHANNEL_SOLVER)
    mod = ok.load_solver(sp)
    eng = dm.Engine(mod, "")
    surface = {"truth_fields": {"class": "class", "groups": "groups"},
               "slots": [{"id": "SA", "weight": 5, "class": "aggregate", "selector": ["group_count", "ok_a"]},
                         {"id": "SB", "weight": 3, "class": "aggregate", "selector": ["group_count", "ok_b"]},
                         {"id": "SB1", "weight": 1, "class": "direct", "selector": ["field", "B-01", "status"]},
                         {"id": "SB2", "weight": 1, "class": "direct", "selector": ["field", "B-02", "status"]},
                         {"id": "S1", "weight": 3, "class": "direct", "selector": ["field", "A-01", "status"]},
                         {"id": "S2", "weight": 3, "class": "direct", "selector": ["field", "A-02", "status"]},
                         {"id": "SK", "weight": 1, "class": "direct", "selector": ["field", "K-01", "class"]},
                         {"id": "D1", "weight": 5, "class": "delivery", "selector": ["delivery", "slide_updated"]}]}
    slots = dm.Slots(surface["slots"], surface)
    outs, gates = Outcomes(eng, slots), Gates(slots, {"V2": {"cap": 0.75, "mode": None}}, "long-horizon", 550)
    assert ("degrade", "slip:a") in eng.elements and all(m[0] == "rule" for m in eng.mechanisms()), eng.mechanisms()
    led = hl.Ledger(Path(tmp) / "channel_ledger.jsonl")
    over = dict(parse_rate(x) for x in ("scale:a=0.02", "linked:a=0.02", "deleg:a=0.3", "pair:b=0.5", "duo:ind=0.3",
                                        "duo:link=0.3", "surface:deck=0.4"))
    specs, missing = channel_specs(eng, mod, slots, led, "claude-opus-4-8", over, briefs=[
        {"keys": [f"A-{n:02d}" for n in range(1, 17)]}, {"keys": [f"A-{n:02d}" for n in range(17, 33)]},
        {"keys": [f"A-{n:02d}" for n in range(33, 41)]}])
    by = {c["id"]: c for c in specs}
    assert sorted(c["id"] for c in missing) == ["control:rule_k", "ghost"], missing     # no record, no override

    def run(ids, draws=1500, rate=None):
        chs = [dict(by[i], rate=rate or by[i]["rate"]) for i in ids]
        return simulate(eng, outs, gates, [], {}, {}, {}, draws=draws, seed=3, dependence="independent",
                        extent="whole", channels=chs)

    def pf(s, sid):
        return (s["slots"].get(sid) or {}).get("P_fail", 0.0)
    ind, lnk = run(["scale:a"]), run(["linked:a"])
    assert abs(p_any(by["scale:a"]["rate"], 40)["integrated"] - 0.5543) < 1e-3
    assert abs(pf(ind, "SA") - 0.5543) < 0.03 and abs(pf(lnk, "SA") - 0.02) < 0.01, (pf(ind, "SA"), pf(lnk, "SA"))
    unc = {"alpha": 2.0, "beta": 98.0, "mean": 0.02, "records": [], "basis": "test", "label": "test"}
    pa = p_any(unc, 40)                                  # integrating over e: 1 - E[(1 - e)^40] < the plug-in
    assert pa["integrated"] < pa["plug_in"] - 0.05 and abs(pf(run(["scale:a"], rate=unc), "SA") - pa["integrated"]) < 0.03, pa
    failed, _ = outs.of({("degrade", "slip:b"): {"B-01", "B-02"}})   # one false exclusion + one false inclusion
    assert failed == {"SB1", "SB2"}, failed                           # the count cancels; both members fail
    di, dl = run(["duo:ind"], 800), run(["duo:link"], 800)
    assert dl["views"]["V2"]["E_patterns"] < di["views"]["V2"]["E_patterns"], (dl["views"], di["views"])
    assert abs(pf(run(["surface:deck"]), "D1") - 0.4) < 0.03
    assert [len(b) for b in by["deleg:a"]["batches"]] == [16, 16, 8]
    th, B = 0.3, 3                                        # M6: per-batch misses keep the per-run landing rate theta
    b = 1 - (1 - th) ** (1 / B)
    assert abs(1 - (1 - b) ** B - th) < 1e-12
    rng = random.Random(5)
    sizes = {len(_missed_batches(by["deleg:a"]["batches"], th, rng)) for _ in range(300)}
    assert sizes <= {8, 16, 24, 32, 40} and len(sizes) > 2, sizes
    mech = [element_of(eng, "late_a")]
    sm = simulate(eng, outs, gates, mech, {"F": {"alpha": 3, "beta": 7}}, {mech[0]: "F"}, {mech[0]: "x"}, draws=800,
                  seed=4, dependence="independent", extent="batches", briefs=[{"keys": x} for x in by["deleg:a"]["batches"]])
    assert abs(sm["landing_rate_simulated"]["rule:late_a"] - 0.3) < 0.04, sm["landing_rate_simulated"]
    # rates from ledger records, pooled across tasks by family like the mechanism priors: another task's scale channel
    # feeds every scale channel here (a per-member error rate per model), its chain record feeds none of them, and a
    # control trial feeds its rule's family; each record id kept
    base = {"task": "t", "revision": "r1", "source": "platform-baseline", "model": "claude-opus-4-8",
            "harness": {"name": "h", "version": "1"}, "epistemic": "derived"}
    other = dict(base, task="another_task")
    provenance = {"deciding_model_unknown": True}      # the ledger refuses a channel/control trial without provenance
    led.append([dict(other, kind="channel", run=f"run-{i}", node="scale:elsewhere", family="scale",
                     verdict="FAILED" if i == 1 else "HELD", features=provenance,
                     counts={"members": 40, "failed": 2 if i == 1 else 0})
                for i in (1, 2)] +
               [dict(other, kind="channel", run="run-1", node="chain:elsewhere", family="chain", verdict="FAILED",
                     features=provenance, counts={"members": 1, "failed": 1}),
                dict(base, kind="control", run="run-1", node="rule_k", key="K-01", family="F", verdict="OVER-APPLIED",
                     features=provenance)])
    # fix 1: a member-unit rate never silently feeds a run-latent channel (linked:a declares "run"); the pooling
    # assertions are made on channel_rate, and channel_specs is asked again with the scale family excluded
    try:
        channel_specs(eng, mod, slots, hl.Ledger(led.path), "claude-opus-4-8", {})
    except ValueError as error:
        assert "linked:a" in str(error) and "'member'" in str(error) and "ledger records" in str(error), error
    else:
        raise AssertionError("a member-unit rate silently fed the run-latent channel linked:a")
    r2 = {cid: channel_rate(hl.Ledger(led.path), "claude-opus-4-8", cid, "scale", "scale", {})
          for cid in ("scale:a", "linked:a")}
    assert r2["scale:a"]["alpha"] == round(1 + 2 / 1.5, 4) and len(r2["scale:a"]["records"]) == 2, r2["scale:a"]
    assert r2["scale:a"]["unit"] == "member" and r2["linked:a"] == r2["scale:a"], r2
    _, missing2 = channel_specs(eng, mod, slots, hl.Ledger(led.path), "claude-opus-4-8", {},
                                exclude_tasks=("another_task",))
    assert {"deleg:a", "surface:deck"} <= {c["id"] for c in missing2}, missing2
    assert channel_rate(hl.Ledger(led.path), "claude-opus-4-8", "control:rule_k", "control", "F", {})["mean"] > 0.5
    # Q2: member and run units of one family convert member -> run; a batch/member mix is refused, never pooled
    led.append([dict(other, kind="channel", run="run-1", node="scale:mixed", family="mixfam", verdict="FAILED",
                     features=provenance, counts={"unit": "member", "members": 40, "n": 40, "failed": 2}),
                dict(other, kind="channel", run="run-2", node="scale:mixed", family="mixfam", verdict="HELD",
                     features=provenance, counts={"unit": "member", "members": 40, "n": 40, "failed": 0}),
                dict(other, kind="channel", run="run-3", node="scale:mixed", family="mixfam", verdict="FAILED",
                     features=provenance, counts={"unit": "run", "n": 1, "failed": 1})])
    led.append([dict(other, kind="channel", run="run-9", node="scale:mixed", family="mixfam", verdict="HELD",
                     features=provenance, counts={"unit": "member", "n": 1, "failed": 0}),
                dict(other, kind="channel", run="run-10", node="scale:mixed", family="mixfam", verdict="FAILED",
                     counts={"unit": "member", "n": 1, "failed": 1},
                     features={"mixed_model": True, "deciding_models": ["claude-opus-5"]})])
    mx = channel_rate(hl.Ledger(led.path), "claude-opus-4-8", "scale:mixed", "scale", "mixfam", {})
    assert any(x[0] for x in mx["dropped"]) and "mixed-model" in mx["dropped"][0][1], mx
    assert mx["unit"] == "run" and mx["n"] == 4 and mx["f"] == 2 and (mx["alpha"], mx["beta"]) == (1.8, 1.8), mx
    led.append([dict(other, kind="channel", run="run-4", node="scale:batch", family="batchfam", verdict="FAILED",
                     features=provenance, counts={"unit": "batch", "n": 8, "failed": 2}),
                dict(other, kind="channel", run="run-4", node="scale:batchm", family="batchfam", verdict="HELD",
                     features=provenance, counts={"unit": "member", "n": 16, "failed": 0})])
    try:
        channel_rate(hl.Ledger(led.path), "claude-opus-4-8", "scale:batch", "scale", "batchfam", {})
    except ValueError as e:
        assert "mixed units" in str(e), e
    else:
        raise AssertionError("a batch/member mix was pooled")
    # Q2/F1-1: the run key is (revision, run): two revisions both numbered run-1 are two runs, not one
    two = _rate_from_records([("t", "r1", "run-1", 1, 0, "a"), ("t", "r2", "run-1", 1, 1, "b")], 0.5)
    assert two["tasks"]["t"]["runs"] == 2 and two["tasks"]["t"]["deff"] == 1.5, two
    same = _rate_from_records([("t", "r1", "run-1", 1, 0, "a"), ("t", "r1", "run-1", 1, 1, "b")], 0.5)
    assert same["tasks"]["t"]["deff"] == 1.0, same
    # Q4/M6: the exact conditional sampler: every draw misses at least one batch, E[K] = B b / theta, each marginal b/theta
    B = 34
    rng2, n2 = random.Random(11), 4000
    for theta in (0.3, 0.005):                       # Q4: zero-truncated Binomial(B, b) at both rates
        b = 1 - (1 - theta) ** (1 / B)
        ks, hits = [], [0] * B
        for _ in range(n2):
            got = _missed_batches([{f"k{i}"} for i in range(B)], theta, rng2)
            ks.append(len(got))
            for i in range(B):
                hits[i] += int(f"k{i}" in got)
        want, marg = B * b / theta, b / theta
        assert all(k >= 1 for k in ks), min(ks)
        assert abs(sum(ks) / n2 - want) < 0.05, (theta, sum(ks) / n2, want)
        assert all(abs(h / n2 - marg) < 0.01 for h in hits), (theta, min(hits), max(hits), marg)
    # F1-2: a channel op is refused as a mechanism, a rule is accepted
    try:
        refuse_channel_elements(eng, [("degrade", "slip:a")])
    except ValueError:
        pass
    else:
        raise AssertionError("a channel degrade was accepted as a mechanism")
    refuse_channel_elements(eng, [("rule", "late_a")])
    rep = channel_report(outs, slots, [by["scale:a"], by["surface:deck"]], draws=400, seed=1)
    assert 0 < rep[0]["expected_loss_alone"] < 0.3 and abs(rep[1]["expected_loss_alone"] - 0.4 * 5 / 22) < 0.03, rep
    # a three-step chain through a solver that is not key-local compounds as 1 - prod(1 - q)
    cp = Path(tmp) / "chain_solver.py"
    cp.write_text(_CHAIN_SOLVER)
    cmod = ok.load_solver(cp)
    ceng = dm.Engine(cmod, "")
    cs = {"truth_fields": {}, "slots": [{"id": "SC", "weight": 5, "class": "direct", "selector": ["field", "C-03", "value"]},
                                        {"id": "SX", "weight": 1, "class": "delivery", "selector": ["delivery", "x"]}]}
    cslots = dm.Slots(cs["slots"], cs)
    q = {"chain:1": 0.1, "chain:2": 0.2, "chain:3": 0.3}
    cspecs, _ = channel_specs(ceng, cmod, cslots, led, "claude-opus-4-8", dict(parse_rate(f"{k}={v}") for k, v in q.items()))
    assert not ceng.locality()["key_local"]
    sc = simulate(ceng, Outcomes(ceng, cslots), Gates(cslots, {"V2": {"cap": 0.75, "mode": None}}, "long-horizon", 550),
                  [], {}, {}, {}, draws=1500, seed=6, dependence="independent", extent="whole", channels=cspecs)
    want = 1 - math.prod(1 - x for x in q.values())
    assert abs(sc["slots"]["SC"]["P_fail"] - want) < 0.03, (sc["slots"]["SC"], want)
    # F1 residual b: an all-dropped channel keeps its drop reasons and stays UNPARAMETERIZED (never simulated at 0),
    # and a record of another family is never attached to this channel's dropped list
    dpath = Path(tmp) / "drop_ledger.jsonl"
    dled = hl.Ledger(dpath)
    dled.append([{"kind": "channel", "task": "drop", "revision": "r1", "source": "platform-baseline",
                  "model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}, "run": "run-1",
                  "node": "scale:drop", "family": "dropfam", "verdict": "HELD", "epistemic": "derived",
                  "counts": {"unit": "member", "n": 2, "failed": 0},
                  "features": {"mixed_model": True, "deciding_models": ["claude-opus-5"]}},
                 {"kind": "channel", "task": "drop", "revision": "r1", "source": "platform-baseline",
                  "model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}, "run": "run-2",
                  "node": "scale:other", "family": "otherfam", "verdict": "HELD", "epistemic": "derived",
                  "counts": {"unit": "member", "n": 2, "failed": 0},
                  "features": {"mixed_model": True, "deciding_models": ["claude-opus-5"]}}])
    dr = channel_rate(hl.Ledger(dpath), "claude-opus-4-8", "scale:drop", "scale", "dropfam", {})
    assert dr["alpha"] is None and dr["dropped"] and "mixed-model" in dr["dropped"][0][1], dr
    dr2 = channel_rate(hl.Ledger(dpath), "claude-opus-4-8", "scale:drop2", "scale", "dropfam2", {})
    assert dr2["alpha"] is None and dr2["dropped"] == [], dr2        # another family's record is not this one's drop
    # a task/revision exclusion is a real record, deliberately excluded: its provenance is kept, not reported as
    # "no ledger record"; and invalid counts are refused, and a run-unit rate is never applied member by member
    dex = channel_rate(hl.Ledger(dpath), "claude-opus-4-8", "scale:other", "scale", "otherfam", {},
                       exclude_tasks=("drop",))
    assert dex["alpha"] is None and dex["dropped"] and dex["dropped"][0][1] == "excluded task/revision", dex
    bad_path = Path(tmp) / "bad_ledger.jsonl"
    bl = hl.Ledger(bad_path)
    bl.append([{"kind": "channel", "task": "bad", "revision": "r1", "source": "platform-baseline",
                "model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}, "run": "run-1",
                "node": "scale:bad", "family": "badfam", "verdict": "FAILED", "epistemic": "derived",
                "counts": {"unit": "member", "n": 2, "failed": 3},
                "features": {"deciding_model_unknown": True}}])
    try:
        channel_rate(hl.Ledger(bad_path), "claude-opus-4-8", "scale:bad", "scale", "badfam", {})
    except ValueError as e:
        assert "invalid counts" in str(e), e
    else:
        raise AssertionError("counts with failed > n were accepted")
    # fractional counts are refused BEFORE int() can truncate 2.1 / 2.9 into a valid-looking 2 / 2
    frac_path = Path(tmp) / "frac_ledger.jsonl"
    fll = hl.Ledger(frac_path)
    fll.append([{"kind": "channel", "task": "frac", "revision": "r1", "source": "platform-baseline",
                 "model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}, "run": "run-1",
                 "node": "scale:frac", "family": "fracfam", "verdict": "FAILED", "epistemic": "derived",
                 "counts": {"unit": "member", "n": 2.1, "failed": 2.9},
                 "features": {"deciding_model_unknown": True}}])
    try:
        channel_rate(hl.Ledger(frac_path), "claude-opus-4-8", "scale:frac", "scale", "fracfam", {})
    except ValueError as e:
        assert "non-integral" in str(e), e
    else:
        raise AssertionError("fractional counts were truncated into a valid integer pair")
    # integers above 2**53 must not be rounded through a float: this pair is invalid (failed > n) and must be caught
    big_path = Path(tmp) / "big_ledger.jsonl"
    bgl = hl.Ledger(big_path)
    bgl.append([{"kind": "channel", "task": "big", "revision": "r1", "source": "platform-baseline",
                 "model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}, "run": "run-1",
                 "node": "scale:big", "family": "bigfam", "verdict": "FAILED", "epistemic": "derived",
                 "counts": {"unit": "member", "n": 2 ** 53 + 1, "failed": 2 ** 53 + 2},
                 "features": {"deciding_model_unknown": True}}])
    try:
        channel_rate(hl.Ledger(big_path), "claude-opus-4-8", "scale:big", "scale", "bigfam", {})
    except ValueError as e:
        assert "invalid counts" in str(e), e
    else:
        raise AssertionError("a large-integer failed > n pair was rounded through float and accepted")
    run_path = Path(tmp) / "run_ledger.jsonl"
    rl = hl.Ledger(run_path)
    rl.append([{"kind": "channel", "task": "run", "revision": "r1", "source": "platform-baseline",
                "model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}, "run": "run-1",
                "node": "scale:a", "family": "scale", "verdict": "FAILED", "epistemic": "derived",
                "counts": {"unit": "run", "n": 1, "failed": 1},
                "features": {"deciding_model_unknown": True}}])
    try:
        channel_specs(eng, mod, slots, rl, "claude-opus-4-8", {k: v for k, v in over.items() if k != "scale:a"})
    except ValueError as e:
        assert "member by member" in str(e), e
    else:
        raise AssertionError("a run-unit rate was adopted for a member-bearing channel")
    # F1 residual c: inf / nan / 1e400 Beta parameters are refused (they hang or return nan)
    for bad in ("x=inf,1", "x=1,inf", "x=1,nan", "x=1e400,1", "x=-1", "x=0,1"):
        try:
            parse_rate(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"--channel-rate {bad!r} was accepted")
    for bad in ({"alpha": float("inf"), "beta": 1.0}, {"alpha": 1.0, "beta": float("nan")}):
        try:
            _rate_draw(bad, random.Random(0))
        except ValueError:
            pass
        else:
            raise AssertionError(f"a non-finite Beta {bad!r} was drawn")
    # F1 residual d: a batch channel whose briefs intersect none of its members raises instead of staying inert
    try:
        channel_specs(eng, mod, slots, led, "claude-opus-4-8", over, briefs=[{"keys": ["B-01"]}])
    except ValueError as e:
        assert "deleg:a" in str(e), e
    else:
        raise AssertionError("an inert batch channel was accepted")
    # M6 boundaries: theta = 1 misses every batch at any RNG value (the zero quantile included), theta = 0 none
    class _Zero(random.Random):
        def random(self_inner):
            return 0.0
    three = [{0}, {1}, {2}]
    assert _missed_batches(three, 1.0, _Zero(0)) == {0, 1, 2}, _missed_batches(three, 1.0, _Zero(0))
    assert _missed_batches(three, 0.0, _Zero(0)) == set() and _missed_batches([], 0.5, _Zero(0)) == set()
    # large B: log-space weights, no int->float overflow, and a documented refusal above MAX_BATCHES
    big = [{i} for i in range(2000)]
    got = _missed_batches(big, 0.3, random.Random(3))
    assert 1 <= len(got) <= 2000, len(got)
    try:
        _missed_batches([{i} for i in range(MAX_BATCHES + 1)], 0.3, random.Random(3))
    except ValueError:
        pass
    else:
        raise AssertionError("a batch set above MAX_BATCHES was accepted")
    # F1 residual g: every slot is reported; the top-25 dict is the presentation short list
    wide = {"truth_fields": {"class": "class", "groups": "groups"},
            "slots": [{"id": f"W{n:02d}", "weight": 1, "class": "direct",
                       "selector": ["field", f"A-{n:02d}", "status"]} for n in range(1, 31)]}
    wslots = dm.Slots(wide["slots"], wide)
    wouts = Outcomes(eng, wslots)
    wgates = Gates(wslots, {"V2": {"cap": 0.75, "mode": None}}, "long-horizon", 550)
    wall = {"id": "all", "kind": "scale", "element": ("degrade", "slip:a"), "members": [f"A-{n:02d}" for n in range(1, 31)],
            "inert_members": 0, "slots": [], "latent": "run", "latent_from": "declared", "batches": None,
            "source": "all", "preregistered": True, "description": None, "family": "scale",
            "rate": {"point": 1.0, "mean": 1.0, "unit": None, "records": [], "source": "test", "basis": "test",
                     "label": "test"}}
    sw = simulate(eng, wouts, wgates, [], {}, {}, {}, draws=3, seed=1, dependence="independent", extent="whole",
                  channels=[wall])
    assert len(sw["slots"]) == 30 and len(sw["slots_top_25"]) == 25 and set(sw["slots_top_25"]) <= set(sw["slots"]), \
        (len(sw["slots"]), len(sw.get("slots_top_25") or {}))
    # F1 residual 9: landing_pairs from the per-run landings: independent P(both) = 1/4, correlated E[min] = 1/3
    m2 = [element_of(eng, "late_a"), element_of(eng, "rule_k")]
    fl = {m: "PAIR" for m in m2}
    psrc = {m: dm._label(m) for m in m2}
    flat = {"PAIR": {"alpha": 1.0, "beta": 1.0}}
    pair_out = {}
    for dep in ("independent", "correlated"):
        pr = simulate(eng, outs, gates, m2, flat, fl, psrc, draws=2000, seed=5, dependence=dep, extent="whole")
        pair_out[dep] = pr["landing_pairs"]
    key = next(iter(pair_out["independent"]))
    assert abs(pair_out["independent"][key]["both"] - 0.25) < 0.03, pair_out["independent"]
    assert abs(pair_out["correlated"][key]["both"] - 1 / 3) < 0.03, pair_out["correlated"]
    assert pair_out["independent"][key]["either"] >= pair_out["independent"][key]["both"], pair_out
    # F1 residual 8: the briefs digest follows the CONTENT at the same path (a paths-only digest would pass the old
    # two-files test); the pre-registration inputs carry that digest
    bp = Path(tmp) / "briefs_one.json"
    bp.write_text(json.dumps([{"keys": ["A-01"]}]))
    d1 = briefs_digest([bp])["digest"]
    bp.write_text(json.dumps([{"keys": ["A-02"]}]))       # same path, different keys
    assert briefs_digest([bp])["digest"] != d1, briefs_digest([bp])
    # the aggregate digest is UNAMBIGUOUS: a two-file set cannot collide with one file named "a:<hash>b"
    d1p, d2p = Path(tmp) / "a.json", Path(tmp) / "b.json"
    d1p.write_text(json.dumps([{"keys": ["A-01"]}]))
    d2p.write_text(json.dumps([{"keys": ["A-02"]}]))
    ha = hashlib.sha256(d1p.read_bytes()).hexdigest()
    odd = Path(tmp) / f"a.json:{ha}b.json"
    odd.write_text(d2p.read_text())
    assert briefs_digest([d1p, d2p])["digest"] != briefs_digest([odd])["digest"], "ambiguous briefs digest"
    # landing_pairs keys escape the separator, so two different pairs cannot serialize alike
    assert pair_key(("rule", "a"), ("rule", "b|rule:c")) != pair_key(("rule", "a|rule:b"), ("rule", "c"))
    # a backslash before a pipe must not alias either: backslashes are escaped FIRST
    assert pair_key(("rule", "a\\"), ("rule", "b|rule:c")) != pair_key(("rule", "a|rule:b\\"), ("rule", "c"))
    # a POINT override that carries an explicit unit is still checked against the declared latent
    try:
        channel_specs(eng, mod, slots, led, "claude-opus-4-8",
                      dict(over, **{"linked:a": {"point": 0.02, "mean": 0.02, "unit": "member"}}))
    except ValueError as e:
        assert "linked:a" in str(e), e
    else:
        raise AssertionError("a point override with a member unit fed the run-latent linked:a")
    # the key is bound to the briefs object actually simulated, not to a later re-read of the file
    assert briefs_content_digest([{"keys": ["A-01"]}]) != briefs_content_digest([{"keys": ["A-02"]}])
    # a slot that never fails is still reported (0 probability), never omitted
    never = {"truth_fields": {"class": "class", "groups": "groups"},
             "slots": [{"id": "S1", "weight": 1, "class": "direct", "selector": ["field", "A-01", "status"]},
                       {"id": "S2", "weight": 1, "class": "direct", "selector": ["field", "A-02", "status"]}]}
    nslots = dm.Slots(never["slots"], never)
    sn = simulate(eng, Outcomes(eng, nslots), Gates(nslots, {"V2": {"cap": 0.75, "mode": None}}, "long-horizon", 550),
                  [], {}, {}, {}, draws=2, seed=1, dependence="independent", extent="whole")
    assert set(sn["slots"]) == {"S1", "S2"} and all(v["P_fail"] == 0 for v in sn["slots"].values()), sn["slots"]
    # a finite but enormous Beta shape is refused: betavariate(1e308, .) overflows 2*alpha internally and hangs
    for bad in ("x=1e308,1", "x=1,1e308"):
        try:
            parse_rate(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"--channel-rate {bad!r} was accepted")
    # ... and a tiny symmetric shape is refused: 1e-300,1e-300 draws 0.0 every time (mean 0.5 expected), and even
    # 1e-3 gives a mean of 0.38; 0.01 is the smallest sound shape here
    for bad in ("x=1e-300,1e-300", "x=0.001,0.001"):
        try:
            parse_rate(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"--channel-rate {bad!r} was accepted")
    try:
        _rate_draw({"alpha": 1e308, "beta": 1.0}, random.Random(0))
    except ValueError:
        pass
    else:
        raise AssertionError("a 1e308 Beta shape was drawn")
    try:
        _rate_draw({"alpha": 1e-300, "beta": 1e-300}, random.Random(0))
    except ValueError:
        pass
    else:
        raise AssertionError("a 1e-300 Beta shape was drawn")
    # a tiny positive theta still misses at least one batch (the naive 1-(1-theta)**(1/B) rounds b to 0)
    assert len(_missed_batches([{0}, {1}, {2}], 1e-16, random.Random(0))) >= 1
    # and at the smallest positive float the b <= 0 fallback must return one batch's MEMBERS (not a set of a set)
    smallest = _missed_batches([{0}, {1}, {2}], 5e-324, random.Random(0))
    assert smallest in ({0}, {1}, {2}), smallest
    return (f"F1: 40 members at e = 0.02 fail {pf(ind, 'SA'):.3f} independent (exact 0.554) and {pf(lnk, 'SA'):.3f} "
            f"linked; 1 - E[(1 - e)^40] {pa['integrated']:.3f} < plug-in {pa['plug_in']:.3f}; a cancelling count passes "
            f"while both members fail; a shared cause {dl['views']['V2']['E_patterns']:.2f} vs "
            f"{di['views']['V2']['E_patterns']:.2f} patterns; a three-step chain {sc['slots']['SC']['P_fail']:.3f} "
            f"(exact {want:.3f}); rates pooled across tasks by family from channel and control records, an "
            "unrecorded kind UNPARAMETERIZED; M6 "
            f"per-batch misses keep the landing rate ({sm['landing_rate_simulated']['rule:late_a']:.3f} vs 0.3)")


def _self_test() -> None:
    import io
    import contextlib
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("hardness_forecast_selftest_") as tmp:
        f1 = _self_test_channels(tmp)
        sp = Path(tmp) / "solver.py"
        sp.write_text(dm._SOLVER)
        mod = ok.load_solver(sp)
        eng = dm.Engine(mod, dm._SQL)
        surface = dm._surface()
        slots = dm.Slots(surface["slots"], surface)
        mechs = [element_of(eng, n) for n in ("late", "minor")]
        views = {"V3": {"cap": 0.7, "mode": "hard"}, "V2": {"cap": 0.75, "mode": None}}
        gates = Gates(slots, views, "long-horizon", 550)
        outs = Outcomes(eng, slots)
        assert outs.of({}) == (frozenset(), 0) and outs.of({mechs[0]: None})[1] == 11, outs.of({mechs[0]: None})
        # exhaustive: 4 outcomes, C(9, 6) = 84 multisets; every value checked against compute() directly
        ex = exhaustive(outs, gates, mechs, p_grid=0.5, expect=(1.0,), break_even=(0.8,))
        assert ex["multisets"] == 84 and len(ex["outcomes"]) == 4, ex["multisets"]
        assert abs(ex["expected_average"]["1.0"] - (17 - 12) / 17) < 1e-12, ex["expected_average"]   # late + minor lose 12
        assert ex["structure"]["min_mean_with_a_perfect_run"] == (1 + 5 * (5 / 17)) / 6, ex["structure"]
        # the passing count equals a direct enumeration through difficulty_stats.compute()
        direct = 0
        for ms in itertools.combinations_with_replacement(range(4), 6):
            fails = [ex["outcomes"][i]["failed_slots"] for i in ms]
            data = {"spec_version": "V2", "task_type": "long-horizon", "rubrics": gates.rubrics,
                    "rollouts": [{"id": f"r{j}", "status": "completed", "tool_calls": 550,
                                  "results": {r["id"]: r["id"] not in f for r in gates.rubrics}} for j, f in enumerate(fails)]}
            res = ds.compute(data)
            direct += all(res["gates"][g]["verdict"].startswith("PASS") for g in DIFFICULTY_GATES)
        assert direct == ex["views"]["V2"]["passing_multisets"], (direct, ex["views"]["V2"]["passing_multisets"])
        # a certain landing (rate ~1) makes every run identical: SD 0, the spread gate fails, P(all) = 0
        fam = {m: "F" for m in mechs}
        src = {m: dm._label(m) for m in mechs}
        sure = {"F": {"alpha": 1e6, "beta": 1.0}}
        s = simulate(eng, outs, gates, mechs, sure, fam, src, draws=50, seed=1, dependence="independent", extent="whole")
        assert s["views"]["V3"]["P_all"] == 0.0 and s["views"]["V3"]["P_gate"]["per_rollout_sd"] == 0.0, s
        s2 = simulate(eng, outs, gates, mechs, {"F": {"alpha": 2, "beta": 2}}, fam, src, draws=300, seed=1,
                      dependence="source", extent="shard:2")
        assert 0 <= s2["views"]["V2"]["P_all"] <= 1 and len(s2["views"]["V2"]["value_of_information"]) == 2, s2
        # model mixing is refused without a transfer record, and labelled when one exists
        led_path = Path(tmp) / "ledger.jsonl"                 # a temp ledger, never the shared one
        assert led_path.resolve() != hl.DEFAULT_LEDGER.resolve()
        led = hl.Ledger(led_path)
        led.append([{"kind": "verdict", "task": "t", "revision": "r", "source": "platform-baseline",
                     "model": "claude-opus-4-8", "harness": {"name": "h", "version": "1"}, "run": "run-1",
                     "node": "n", "family": "F", "verdict": "LANDED", "epistemic": "observed"}])
        try:
            mechanism_priors(hl.Ledger(led_path), "claude-opus-5-5", ["F"], from_model="claude-opus-4-8")
        except RefuseMix:
            pass
        else:
            raise AssertionError("a cross-model forecast without a transfer record was accepted")
        flat = mechanism_priors(hl.Ledger(led_path), "claude-opus-5-5", ["F"])["F"]
        assert flat["n_eff"] == 0.0 and "flat" in flat["label"], flat                    # never pooled
        hl.Ledger(led_path).append([{"kind": "transfer", "task": "bridge", "revision": "n/a", "source": "forecast",
                                     "model": "claude-opus-5-5", "harness": {"name": "n/a", "version": "n/a"},
                                     "epistemic": "inferred", "family": "F",
                                     "features": {"from_model": "claude-opus-4-8", "to_model": "claude-opus-5-5",
                                                  "offset": 0.0}}])
        t = mechanism_priors(hl.Ledger(led_path), "claude-opus-5-5", ["F"], from_model="claude-opus-4-8")["F"]
        assert t["label"] == TRANSFER_LABEL, t
        # design mode reads declared attributions only
        dslots = dm.Slots([dict(s, mechanisms=["late"]) if s["id"] == "S1" else s for s in surface["slots"]], surface)
        assert Outcomes(None, dslots, design=True).of({("rule", "late"): None})[0] == frozenset({"S1"})
        # the scorer verifies hashes, then scores; Brier over the scored predictions only
        ev = Path(tmp) / "grades.json"
        ev.write_text(json.dumps({"gates": {"V2": {"difficulty_blocking": ["avg_weighted_pass_rate"]}}}))
        doc = {"preregistration": "x", "hashes": {"grades.json": tl.sha256_file(ev)}, "predictions": [
            {"id": "P1", "text": "fails V2", "confidence": 0.9, "check": {"kind": "gates_fail", "evidence": "grades.json", "view": "V2"}},
            {"id": "P2", "text": "not run", "confidence": 0.6, "check": {"kind": "not_tested", "why": "arm not run"}}]}
        r = score(doc, Path(tmp))
        assert r["brier"] == round(0.1 ** 2, 6) and r["scored"] == 1 and r["predictions"][1]["outcome"] is None, r
        bad = score(dict(doc, hashes={"grades.json": "0" * 64}), Path(tmp))
        assert bad["hash_errors"] and not bad["predictions"], bad
        # the official gates of record: difficulty_stats.compute() output (six full passes fail pass@1 and the average)
        official = ds.compute({"spec_version": "V3", "difficulty_mode": "hard", "task_type": "long-horizon",
                               "rubrics": gates.rubrics, "rollouts": [
                                   {"id": f"r{j}", "status": "completed", "tool_calls": 550, "model": "claude-opus-5-5",
                                    "results": {x["id"]: True for x in gates.rubrics}} for j in range(1, 7)]})
        (Path(tmp) / "difficulty.json").write_text(json.dumps(official))
        out, detail = evaluate({"kind": "gates_fail", "evidence": "difficulty.json", "view": "V3"}, Path(tmp))
        assert out is True and "pass_at_1" in detail and "avg_weighted_pass_rate" in detail, detail
        try:
            evaluate({"kind": "gates_fail", "evidence": "difficulty.json", "view": "V2"}, Path(tmp))
        except ValueError:
            pass
        else:
            raise AssertionError("a V2 prediction was scored against V3 gates")
        # comparison: Beta(1, 1) over 6 runs is uniform (1/7 each) -> [0, 6]; a near-certain landing -> [n, n]
        pmf = beta_binomial(6, 1.0, 1.0)
        assert all(abs(p - 1 / 7) < 1e-12 for p in pmf) and central_interval(pmf) == [0, 6], pmf
        assert central_interval(beta_binomial(3, 1e6, 1.0)) == [3, 3]   # a near-certain prior (the sampler needs beta >= .01)
        assert abs(sum(beta_binomial(7, 14.0, 6.0)) - 1) < 1e-12
        rule = lambda vd, keys=(): {"verdict": vd, "landed_keys": list(keys), "citations": {"e": [1]} if vd == "LANDED"  # noqa: E731
                                     else {}, "brief_transmission": {"covering_briefs": 2, "carry_in_text": 1,
                                                                     "carry_by_reference": 1, "omit": 0}, "flags": []}
        bound_ = {"verdict": "BOUND", "bound_to": ["r"], "basis": "discriminating content",
                  "evidence": {"discriminating_seen": 4, "shared_seen": 9}}
        verdicts = {"runs": {
            "precheck": {"rules": {"late": rule("LEAKED")}, "degrades": {}, "items": [], "binding": bound_,
                         "provenance": {"mixed_model": False}, "review_queue": {"unclassified_calls": []}},
            "run-1": {"rules": {"late": rule("LANDED", ["K-01"])}, "degrades": {}, "binding": bound_,
                      "items": [{"key": "K-01", "field": "count", "classification": "mechanism", "attributed": ["late"]},
                                {"key": "K-01", "field": "class", "classification": "cascade"},
                                {"key": "K-02", "field": "flag", "classification": "slip"}],
                      "provenance": {"mixed_model": True}, "review_queue": {"unclassified_calls": [5]}},
            "run-2": {"rules": {"late": rule("NOT-REACHED")}, "degrades": {}, "items": [], "binding": bound_,
                      "provenance": {"mixed_model": False}, "review_queue": {"unclassified_calls": []}}},
            "summary": {"late": {"LEAKED": 1, "LANDED": 1, "NOT-REACHED": 1}}, "reach_summary": {"K9:c": {"NOT-READ": 3}}}
        gate_rows = lambda ok_: {g: {"verdict": "PASS" if ok_ else "FAIL"} for g in DIFFICULTY_GATES}  # noqa: E731
        grades = {"runs": {lab: {"register_kind": "CSV", "rows": 4, "score": sc, "counted_calls": 500, "models":
                                 ["claude-opus-4-8"], "fallbacks": [], "mixed_model": lab == "run-1", "file": None}
                           for lab, sc in (("precheck", 1.0), ("run-1", 0.6), ("run-2", 0.8))},
                  "gates": {"V2": {"difficulty_gates": gate_rows(False),
                                   "per_rollout": [{"weighted_pass_rate": 0.6}, {"weighted_pass_rate": 0.8}]}}}
        fc_doc = {"label": LABEL, "model": "claude-opus-4-8", "mechanisms": [
            {"id": "rule:late", "family": "F", "prior": {"alpha": 1e6, "beta": 1.0}}],
            "scenarios": [{"dependence": "independent", "extent": "whole", "views": {"V2": {
                "band_10_90": [0.5, 0.9], "E_average": 0.7, "P_all": 0.95, "P_gate": {g: 0.9 for g in DIFFICULTY_GATES}}}}]}
        cmp_ = compare({"prior": fc_doc}, verdicts, grades, precheck_call="go", old_band=2, class_field="class",
                       costs=False)
        land = cmp_["forecasts"]["prior"]["landing"][0]
        assert land["all runs"]["runs"] == 2 and land["all runs"]["landed"] == 1, land            # run-2 is no trial
        assert land["all runs"]["interval_90"] == [2, 2] and land["all runs"]["inside"] is False, land
        assert land["excluding mixed-model runs"]["runs"] == 1 and land["excluding mixed-model runs"]["landed"] == 0
        sc_ = cmp_["forecasts"]["prior"]["scenarios"][0]
        assert sc_["average_in_band"] and abs(sc_["P_observed_all_gates"] - 0.05) < 1e-9, sc_
        assert not sc_["observed_verdict_at_least_10pct"], sc_
        r1 = next(r for r in cmp_["per_run"] if r["run"] == "run-1")
        assert (r1["wrong_rows"], r1["class_errors"], r1["causes"]) == (2, 1, "late: K-01; slip: K-02 flag"), r1
        assert cmp_["screens"]["run-1 call"]["agreed"] is False and cmp_["screens"]["/hardness band"]["agreed"] is True
        assert cmp_["tooling"]["pass"] and cmp_["mechanisms"]["never_read"] == ["K9:c"], cmp_["tooling"]
        # planted: a BOUND label without evidence (or a legacy SINGLE) never counts as bound
        for label_only in ({"verdict": "BOUND"}, {"verdict": "SINGLE", "bound_to": ["r"]}):
            v2 = json.loads(json.dumps(verdicts))
            v2["runs"]["run-2"]["binding"] = label_only
            t2 = compare({"prior": fc_doc}, v2, grades, precheck_call="go", old_band=2, class_field="class",
                         costs=False)["tooling"]
            assert not t2["every_run_bound"] and not t2["pass"], t2
        assert "## Plan §14.7 checks" in comparison_markdown(cmp_)
        with contextlib.redirect_stdout(io.StringIO()):
            to_text({"label": LABEL, "model": "m", "revision": "r", "mechanisms": [], "scenarios": [s2], "summary": {}})
    # planted: --max-k above 8 without --allow-max-k is UNSUPPORTED before any work (exit 2)
    import contextlib
    import io
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        assert main(["forecast", "--model", "claude-opus-5-5", "--max-k", "12"]) == 2
        assert main(["exhaustive", "--max-k", "9", "--allow-max-k", "12"]) == 2
    refused = [ln for ln in err.getvalue().splitlines() if ln.startswith("hardness_forecast: UNSUPPORTED: --max-k")]
    assert len(refused) == 2 and "--allow-max-k 12" in refused[0] and "--allow-max-k 9" in refused[1], err.getvalue()
    print("self-test: ok (exact outcomes, exhaustive multisets equal to direct compute() enumeration, E[average](p), "
          "certain landing -> SD gate fails, scenarios and value of information, model mixing refused without a "
          "transfer record and labelled with one, flat prior when the model has no evidence, DESIGN mode, scorer "
          "hash check and Brier, gates_fail on surface grades and on difficulty_stats output, comparison: Beta-Binomial "
          "intervals, NOT-REACHED runs not counted as trials, mixed-model runs shown apart, band and P(observed verdict), "
          f"screens, per-run causes; {f1})")


# ------------------------------------------------------------------ main

def _common(p):
    p.add_argument("--task-dir", type=Path)
    p.add_argument("--solver", type=Path)
    p.add_argument("--sql", type=Path)
    p.add_argument("--revision")
    p.add_argument("--surface", type=Path)
    p.add_argument("--slots", type=Path, help="a slot list ({slots: [{id, weight, selector}]})")
    p.add_argument("--layout", type=Path, help="a coverage_stress.json / coverage_plan.json slot layout")
    p.add_argument("--with-cases", action="store_true")
    p.add_argument("--mechanisms", help="comma list of rule ids / degrade names (default: every whole mechanism)")
    p.add_argument("--views", choices=("auto", "v2", "v3", "both"), default="auto")
    p.add_argument("--mode", choices=("easy", "medium", "hard"))
    p.add_argument("--task-type", default=None)
    p.add_argument("--calls", type=int, default=550, help="tool_calls per simulated rollout (horizon is not gated here)")
    p.add_argument("--max-k", type=int, default=dm.MAX_K)
    p.add_argument("--allow-max-k", type=int, metavar="N", help="the explicit, disclosed override for --max-k N > 8")
    p.add_argument("--out", type=Path)
    p.add_argument("--json", action="store_true")


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="hardness_forecast.py", description="joint-gate forecast (see docstring)")
    ap.add_argument("--self-test", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("forecast")
    _common(p)
    p.add_argument("--model", required=True)
    p.add_argument("--from-model")
    p.add_argument("--ledger", type=Path, default=hl.DEFAULT_LEDGER)
    p.add_argument("--exclude-task", action="append", default=[])
    p.add_argument("--exclude-revision", action="append", default=[])
    p.add_argument("--include-mixed", action="store_true")
    p.add_argument("--family", action="append", default=[], help="ELEMENT=FAMILY override")
    p.add_argument("--draws", type=int, default=10000)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--dependence", action="append", choices=DEPENDENCE)
    p.add_argument("--extent", action="append")
    p.add_argument("--design", action="store_true")
    p.add_argument("--manifest", type=Path)
    p.add_argument("--task", default=None)
    p.add_argument("--preregister", action="store_true")
    p.add_argument("--retrospective", action="store_true")
    p.add_argument("--freeze", type=Path, action="append", default=[],
                   help="a file whose sha256 the forecast records and pre-registers (prompt, manifest, truth.json)")
    p.add_argument("--harness", default="platform@unrecorded")
    p.add_argument("--channel-rate", action="append", default=[], metavar="CID=E|ALPHA,BETA",
                   help="an explicit, disclosed rate for a channel without a ledger record (F1)")
    p.add_argument("--no-channels", action="store_true", help="leave the declared complexity channels out")
    p.add_argument("--mechanism-rate", action="append", default=[], metavar="ELEMENT=E|ALPHA,BETA",
                   help="an explicit, disclosed landing rate for a mechanism instead of its ledger prior (a "
                        "conditional design, e.g. a posterior variant); labelled OVERRIDE")
    p.add_argument("--briefs", type=Path, action="append", default=[],
                   help="trajectory_ledger briefs.json: brief batches for the batches extent and delegation channels (M6)")
    p = sub.add_parser("exhaustive")
    _common(p)
    p.add_argument("--p-grid", type=float, default=0.01)
    p.add_argument("--expect", default="0.3,0.5,0.7,1.0")
    p.add_argument("--break-even", default="0.70,0.65")
    p = sub.add_parser("score")
    p.add_argument("--predictions", type=Path, required=True)
    p.add_argument("--append", action="store_true")
    p.add_argument("--ledger", type=Path, default=hl.DEFAULT_LEDGER)
    p.add_argument("--out", type=Path)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("compare")
    p.add_argument("--forecast", action="append", default=[], help="LABEL=FORECAST.json (repeatable: prior, posterior)")
    p.add_argument("--verdicts", type=Path, required=True, help="node_verdicts.py output over every run")
    p.add_argument("--grades", type=Path, required=True, help="surface_grader.py output")
    p.add_argument("--difficulty", type=Path, help="difficulty_stats.py --json output (the gates of record)")
    p.add_argument("--predictions", type=Path, help="a pre-registration predictions file to score")
    p.add_argument("--precheck-call", choices=("go", "no-go"), help="the run-1 call recorded before runs 2-7 were read")
    p.add_argument("--old-band", type=int, help="the /hardness band of the pre-check (1-5)")
    p.add_argument("--class-field", help="the truth field of the class (default: the surface's truth_fields.class)")
    p.add_argument("--no-costs", action="store_true", help="do not read the trajectories for their cost")
    p.add_argument("--out", type=Path)
    p.add_argument("--md", type=Path)
    p.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        _self_test()
        return 0
    max_k_disclosure = None
    if a.cmd in ("forecast", "exhaustive"):
        try:
            a.max_k, max_k_disclosure = dm.resolve_max_k(a.max_k, a.allow_max_k)   # default 8; above only disclosed
        except dm.Unsupported as exc:
            print(f"hardness_forecast: {exc}", file=sys.stderr)
            return 2
        if max_k_disclosure:
            print(f"hardness_forecast: {max_k_disclosure}", file=sys.stderr)
    if a.cmd == "compare":
        forecasts, paths = {}, [("verdicts", a.verdicts), ("grades", a.grades), ("difficulty", a.difficulty),
                                ("predictions", a.predictions)]
        for spec in a.forecast:
            label, sep, path = spec.partition("=")
            if not sep:
                label, path = Path(spec).stem, spec
            forecasts[label] = json.loads(Path(path).read_text())
            paths.append((f"forecast:{label}", Path(path)))
        grades = json.loads(a.grades.read_text())
        class_field = a.class_field
        if not class_field:
            try:
                class_field = gs.load(Path(grades["surface"]))["truth_fields"]["class"]
            except Exception:  # noqa: BLE001 - an unreadable surface falls back to the Season Pass field name
                class_field = "handoff class"
        preds = json.loads(a.predictions.read_text()) if a.predictions else None
        rep = compare(forecasts, json.loads(a.verdicts.read_text()), grades,
                      difficulty=json.loads(a.difficulty.read_text()) if a.difficulty else None, predictions=preds,
                      base=a.predictions.parent / (preds or {}).get("base", ".") if a.predictions else None,
                      precheck_call=a.precheck_call, old_band=a.old_band, class_field=class_field,
                      costs=not a.no_costs)
        rep["inputs"] = {k: {"path": tl._rel(p_), "sha256": tl.sha256_file(p_)} for k, p_ in paths if p_}
        md = comparison_markdown(rep)
        for path, text in ((a.out, json.dumps(rep, indent=1, ensure_ascii=False, default=sorted) + "\n"), (a.md, md)):
            if path:
                out = tl.safe_out(path)
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text(text)
        print(json.dumps(rep, indent=1, ensure_ascii=False, default=sorted) if a.json else md, end="")
        return 1 if (rep.get("scorecard") or {}).get("hash_errors") else 0
    if a.cmd == "score":
        doc = json.loads(a.predictions.read_text())
        rep = score(doc, a.predictions.parent / doc.get("base", "."))
        if a.append and not rep["hash_errors"]:
            recs = []
            for p_, d in zip(rep["predictions"], doc["predictions"]):
                common = {"task": doc["task"], "revision": doc["revision"], "source": "forecast", "model": doc["model"],
                          "harness": doc["harness"], "node": p_["id"], "epistemic": "inferred",
                          "features": {"text": p_["prediction"], "confidence": p_["confidence"]},
                          "evidence": {"preregistration": doc.get("preregistration"), "tool": VERSION}}
                recs.append(dict(common, kind="prediction"))
                if p_["outcome"] is not None:
                    recs.append(dict(common, kind="outcome", value=p_["outcome"], epistemic="derived",
                                     evidence=dict(common["evidence"], detail=p_["detail"])))
            res = hl.Ledger(a.ledger).append(recs)
            rep["ledger"] = {"added": len(res["added"]), "present": len(res["present"]), "rejected": res["rejected"]}
        if a.out:
            out = tl.safe_out(a.out)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(rep, indent=1, ensure_ascii=False) + "\n")
        if a.json:
            print(json.dumps(rep, indent=1, ensure_ascii=False))
        else:
            print(f"PRE-REGISTRATION SCORE · {doc.get('preregistration')} · {NOTE}")
            for e in rep["hash_errors"]:
                print(f"  HASH MISMATCH: {e}")
            for p_ in rep["predictions"]:
                print(f"  {p_['id']} conf {p_['confidence']:.2f} -> {p_['outcome']}: {p_['detail'][:150]}")
            print(f"  Brier over {rep['scored']} scored predictions: {rep['brier']} (constant 0.5 scores 0.25)")
            if "ledger" in rep:
                print(f"  ledger: {rep['ledger']}")
        return 1 if rep["hash_errors"] else 0
    if a.cmd not in ("forecast", "exhaustive"):
        ap.print_usage(sys.stderr)
        return 2
    design = a.cmd == "forecast" and a.design
    td = a.task_dir
    wf = td / "Working_Files" if td else None
    context = dm._context(td)
    task_type = a.task_type or (context or {}).get("task_type") or "long-horizon"
    views = views_for(a.views, context, a.mode)
    slots_list, surface, layout = load_layout(a, wf)
    slots = dm.Slots(slots_list, surface)
    if design:
        engine, mod = None, None
        names = [x.strip() for x in (a.mechanisms or "").split(",") if x.strip()]
        if not names:
            raise ValueError("--design needs --mechanisms (the declared mechanism ids)")
        mechs = [("rule", n) for n in names]
        sql_sha, revision, solver_sha = None, "design", None
    else:
        _, _, solver_path, sql_path = dm._task_files(a)
        mod = ok.load_solver(solver_path)
        engine = dm.Engine(mod, sql_path.read_text(), a.revision, a.max_k)
        names = [x.strip() for x in (a.mechanisms or "").split(",") if x.strip()]
        mechs = [element_of(engine, n) for n in names] if names else engine.mechanisms()
        refuse_channel_elements(engine, mechs)
        sql_sha, revision, solver_sha = engine.sql_sha256, engine.revision, tl.sha256_file(solver_path)
        if not engine.composable():
            loc = engine.locality()
            print("hardness_forecast: " + ("the solver is not key-local" if not loc["key_local"] else
                                           f"key-locality checked on only {loc['checked']} of {loc['configs']} "
                                           "configurations") + "; configurations are solved in full (exact, slow)",
                  file=sys.stderr)
    if len(mechs) > a.max_k:
        print(f"hardness_forecast: UNSUPPORTED - {len(mechs)} mechanisms > {a.max_k}: exact combinations only (plan §5)",
              file=sys.stderr)
        return 2
    outcomes = Outcomes(engine, slots, design)
    gates = Gates(slots, views, task_type, a.calls)
    base = {"tool": VERSION, "note": NOTE, "revision": revision, "sql_sha256": sql_sha, "solver_sha256": solver_sha,
            **layout, "views": views, "task_type": task_type, "calls": a.calls, "max_k": a.max_k,
            "max_k_override": max_k_disclosure}
    if a.cmd == "exhaustive":
        rep = dict(base, kind="EXHAUSTIVE_GATES", label="DERIVED · deterministic enumeration", model=None, mechanisms=[],
                   exhaustive=exhaustive(outcomes, gates, mechs, p_grid=a.p_grid,
                                         expect=[float(x) for x in a.expect.split(",") if x],
                                         break_even=[float(x) for x in a.break_even.split(",") if x]))
    else:
        man_path = a.manifest or (next((wf / n for n in ("01_Hardness_Manifest.json", "01_Hardness_Manifest.draft.json")
                                         if (wf / n).is_file()), None) if wf else None)
        manifest = json.loads(man_path.read_text()) if man_path else None
        portfolio = (manifest or {}).get("mechanism_portfolio") or []
        overrides = dict(x.split("=", 1) for x in a.family)
        fam = {m: family_of(mod, m, portfolio, overrides) for m in mechs}
        src = {m: source_of(mod, m, portfolio) for m in mechs}
        mech_over = dict(parse_rate(x) for x in a.mechanism_rate)
        unknown_m = sorted(set(mech_over) - {dm._label(m) for m in mechs} - {m[1] for m in mechs})
        if unknown_m:
            raise ValueError(f"--mechanism-rate for element(s) outside the forecast {unknown_m}")
        for m in mechs:
            if dm._label(m) in mech_over or m[1] in mech_over:
                fam[m] = f"override:{dm._label(m)}"
        try:
            priors = mechanism_priors(hl.Ledger(a.ledger), a.model, sorted({f for f in fam.values()
                                                                            if not f.startswith("override:")}),
                                      from_model=a.from_model, exclude_tasks=a.exclude_task,
                                      exclude_revisions=a.exclude_revision, include_mixed=a.include_mixed)
        except RefuseMix as error:
            print(f"hardness_forecast: {error}", file=sys.stderr)
            return 2
        for m in mechs:
            if fam[m].startswith("override:"):
                r = mech_over.get(dm._label(m)) or mech_over[m[1]]
                priors[fam[m]] = dict(r, model=hl.model_family(a.model), n_eff=None, record_ids=[], excluded=[],
                                      basis=r["basis"].replace("--channel-rate", "--mechanism-rate"))
        transferred = any(p.get("label") == TRANSFER_LABEL for p in priors.values())
        label = (TRANSFER_LABEL if transferred else LABEL) + (" · DESIGN (declared attributions)" if design else "") \
            + (" · CONDITIONAL (mechanism rates overridden)" if any(f.startswith("override:") for f in fam.values()) else "")
        briefs = [b for f in a.briefs for b in json.loads(f.read_text())]
        overrides = dict(parse_rate(x) for x in a.channel_rate)
        bad_src = [cid for cid, r in overrides.items() if r.get("source") == "UNSPECIFIED"]
        bad_src += [e for e, r in mech_over.items() if r.get("source") == "UNSPECIFIED"]
        if bad_src:
            raise ValueError(f"overrides need an independent source: give CID=VALUE@SOURCE; missing for {bad_src}")
        channels, unparameterized = ([], []) if design or a.no_channels else channel_specs(
            engine, mod, slots, hl.Ledger(a.ledger), a.model, overrides, briefs, exclude_tasks=a.exclude_task,
            exclude_revisions=a.exclude_revision, include_mixed=a.include_mixed)
        unknown = sorted(set(overrides) - {c["id"] for c in channels})
        if unknown:
            raise ValueError(f"--channel-rate for undeclared channel(s) {unknown}")
        scenarios = []
        for dep in a.dependence or list(DEPENDENCE):
            for ext in a.extent or list(EXTENT):
                scenarios.append(simulate(engine, outcomes, gates, mechs, priors, fam, src, draws=a.draws, seed=a.seed,
                                          dependence=dep, extent=ext if engine else "whole", channels=channels,
                                          briefs=briefs))
        summary = {v: {"P_all_min": min(s["views"][v]["P_all"] for s in scenarios),
                       "P_all_max": max(s["views"][v]["P_all"] for s in scenarios),
                       "E_average_range": [min(s["views"][v]["E_average"] for s in scenarios),
                                           max(s["views"][v]["E_average"] for s in scenarios)],
                       "voi": [x["mechanism"] for x in scenarios[0]["views"][v]["value_of_information"]]} for v in views}
        rep = dict(base, kind="HARDNESS_FORECAST", label=label, model=hl.model_family(a.model),
                   priors_from=hl.model_family(a.from_model or a.model),
                   exclusions={"tasks": a.exclude_task, "revisions": a.exclude_revision, "include_mixed": a.include_mixed},
                   ledger=tl._rel(a.ledger), ledger_sha256=tl.sha256_file(a.ledger) if a.ledger.is_file() else None,
                   mechanisms=[{"id": dm._label(m), "family": fam[m], "source": src[m],
                                "touched": len(engine.touched[m]) if engine else None, "prior": priors[fam[m]]}
                               for m in mechs],
                   channels=channel_report(outcomes, slots, channels, draws=a.draws, seed=a.seed) if channels else [],
                   unparameterized_channels=[{"id": c["id"], "kind": c["kind"], "members": len(c["members"]),
                                              "why": (f"all {len(c['rate'].get('dropped') or [])} eligible record(s) "
                                                      f"excluded: " + "; ".join(f"{i}: {w}" for i, w in
                                                                                (c["rate"].get("dropped") or [])))
                                              if (c.get("rate") or {}).get("dropped") else
                                              "no ledger record and no --channel-rate override: not simulated",
                                              "dropped": (c.get("rate") or {}).get("dropped") or [],
                                              "basis": (c.get("rate") or {}).get("basis")}
                                             for c in unparameterized],
                   briefs=dict(briefs_digest(a.briefs), content_digest=briefs_content_digest(briefs),
                               batches=len(dm.shards_for(engine, briefs)) if engine and briefs else None),
                   scenarios=scenarios, summary=summary)
        if a.freeze:
            missing = [str(f) for f in a.freeze if not f.is_file()]
            if missing:
                raise ValueError(f"--freeze: no such file {missing}")
            rep["frozen"] = {tl._rel(f): tl.sha256_file(f) for f in a.freeze}
        if a.preregister:
            inputs = {k: rep.get(k) for k in ("sql_sha256", "solver_sha256", "sha256", "ledger_sha256", "views",
                                                "task_type", "calls")}
            if rep.get("frozen"):
                inputs["frozen"] = rep["frozen"]
            inputs.update(mechanisms={m["id"]: [m["family"], m["prior"].get("alpha"), m["prior"].get("beta"),
                                                m["prior"].get("point")] for m in rep["mechanisms"]},
                          draws=a.draws, seed=a.seed, tool=VERSION,
                          exclusions=rep["exclusions"],
                          briefs=(rep.get("briefs") or {}).get("content_digest"),
                          channels={c["id"]: [c["latent"], c["rate"].get("point"), c["rate"].get("alpha"),
                                              c["rate"].get("beta"), c["rate"]["basis"]] for c in rep["channels"]})
            key = hashlib.sha256(json.dumps(inputs, sort_keys=True, default=str).encode()).hexdigest()[:16]
            hname, _, hver = a.harness.partition("@")
            rec = {"kind": "forecast", "task": a.task or (td.name if td else "task"), "revision": str(revision),
                   "sql_sha256": sql_sha, "source": "forecast", "model": hl.model_family(a.model),
                   "harness": {"name": hname, "version": hver or "unrecorded"}, "node": "joint gates", "key": key,
                   "epistemic": "inferred", "weight": 1.0, "evidence": {"tool": VERSION, "label": label},
                   "features": {"inputs": inputs, "retrospective": a.retrospective,
                                "outputs": {v: {"P_all_range": [summary[v]["P_all_min"], summary[v]["P_all_max"]],
                                                "E_average_range": summary[v]["E_average_range"]} for v in views},
                                "note": ("BACKTEST: the runs already exist, so this is not a pre-registration before a "
                                         "run" if a.retrospective else "pre-registered before the platform run")}}
            res = hl.Ledger(a.ledger).append([rec])
            rep["preregistration"] = {"id": hl.record_id(rec), "added": bool(res["added"]), "present": bool(res["present"]),
                                      "rejected": res["rejected"]}
    if a.out:
        out = tl.safe_out(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rep, indent=1, ensure_ascii=False, default=sorted) + "\n")
    print(json.dumps(rep, indent=1, ensure_ascii=False, default=sorted) if a.json else to_text(rep))
    if rep.get("preregistration") and not a.json:
        print(f"  ledger: forecast record {rep['preregistration']}")
    if a.out and not a.json:
        print(f"wrote {tl._rel(a.out)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"hardness_forecast: {error}", file=sys.stderr)
        raise SystemExit(2)

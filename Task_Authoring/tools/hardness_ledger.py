#!/usr/bin/env python3
"""hardness_ledger.py - the cross-task evidence ledger: verdicts, observations, forecasts, predictions, transfers.

Plan §7.6 and §15.4. One JSON record per line in support/hardness_ledger/ledger.jsonl (default). The REA ledger
rules: records are content-addressed and immutable; appending the same record again is a no-op; a different record
with the same identity is rejected; a correction is a new record that `supersedes` the old one; NOT-REACHED and
unread stay unknown; model, harness and source are always kept. Priors are computed per model and never pooled
across models; another model's evidence enters only through an explicit transfer record (TRANSFERRED).
Read-only on every other input, stdlib only.

Record fields
  identity  kind, task, revision, sql_sha256, source, model, harness {name, version}, run, node, mechanism, key,
            supersedes   ->   id = "hev_" + sha256(canonical identity)[:16]
  payload   verdict, family, keys, counts, value, confidence, outcome, evidence, features, weight, epistemic
  kind      verdict (node x run) · observation (aggregate counts, e.g. library tables) · slip (an unattributed
            error) · reach (a deciding record read or not) · forecast (pre-registered forecast) · prediction
            (yes/no with confidence) · outcome (a scored prediction) · probe · transfer (model bridge) ·
            control (a control trial: OVER-APPLIED / HELD, per member; F1's control-channel evidence) · channel (a
            complexity channel per run: FAILED / HELD). Control and channel records never enter the priors.
            A verdict whose features.pending_review lists in-cohort errors no ablation reproduces (node_verdicts'
            mechanism?) is refused until features.disposed_by records their disposition.
  source    platform-precheck · platform-baseline · independent-harness · probe · forecast
  epistemic observed · derived · inferred
  verdict   LANDED · LEAKED · NOT-REACHED · BYPASSED · FALSE · CONFOUNDED (CONFOUNDED only as a recorded human
            disposition, never proposed by a tool)

Priors: Beta(1, 1) plus effective counts per family (mechanism family label). One trial per (task, revision, run,
family) (H2, 2026-10-25): a run whose verdicts of the family include a LANDED is one landing, otherwise one
non-landing (LEAKED, FALSE, BYPASSED); NOT-REACHED and CONFOUNDED are never counted. Trials of one task (all its
revisions) are not independent, so a task's evidence is divided by the Kish design effect 1 + (m - 1) rho over its m
trials (the effect counts trials; record weights scale the evidence, so at rho = 1 a task is worth one trial times
its weight), with rho = 0.5 by default: an assumption, not a measurement (--rho overrides it). Each prior lists n_eff
per task. Aggregate observation records declare no run ids, so the records of one (task, revision, family) collapse to
one trial set: T = the largest counted outcome total, landed = max(landed), not_landed = T - landed (a lower bound
under maximal overlap); the upper bound assuming disjoint runs is reported beside it, and records that declare
different counts.runs are refused rather than merged. Weights: per-run verdicts 1, library aggregates 0.5 (set on the
record), transfers 0.25. Mixed-model runs are
excluded from a model's priors unless --include-mixed. --exclude-task / --exclude-revision keep a revision's own runs
out of its forecast.

Usage:
  python3 -B Task_Authoring/tools/hardness_ledger.py [--ledger L] append FILE.jsonl|-        (one record per line)
  python3 -B Task_Authoring/tools/hardness_ledger.py [--ledger L] seed --season-pass DIR   (DIR = frozen rev13 copy)
  python3 -B Task_Authoring/tools/hardness_ledger.py [--ledger L] priors --model M [--exclude-task T] [--exclude-revision R]
      [--include-mixed] [--family F ...] [--json]
  python3 -B Task_Authoring/tools/hardness_ledger.py [--ledger L] transfer --from-model A --to-model B --offset X
      --evidence TEXT [--family F]
  python3 -B Task_Authoring/tools/hardness_ledger.py [--ledger L] query [--kind K] [--task T] [--model M] [--json]
  python3 -B Task_Authoring/tools/hardness_ledger.py [--ledger L] write-priors OUT.json --model M [...]
  python3 -B Task_Authoring/tools/hardness_ledger.py --self-test
Exit 0 = ok, 1 = a record was rejected, 2 = usage error.
"""
from __future__ import annotations

import argparse
import collections
import math
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path


def _bundle() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "difficulty_stats.py").is_file():
            return parent
    raise SystemExit("hardness_ledger: cannot find the Task_Authoring bundle (no tools/difficulty_stats.py above)")


HERE = Path(__file__).resolve().parent
BUNDLE = _bundle()
for _p in (BUNDLE / "tools", HERE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

DEFAULT_LEDGER = BUNDLE / "support" / "hardness_ledger" / "ledger.jsonl"
KINDS = ("verdict", "observation", "slip", "reach", "forecast", "prediction", "outcome", "probe", "transfer", "control",
         "channel")
CONTROL_OUTCOMES = ("OVER-APPLIED", "HELD")
CHANNEL_OUTCOMES = ("FAILED", "HELD")
SOURCES = ("platform-precheck", "platform-baseline", "independent-harness", "probe", "forecast")
EPISTEMIC = ("observed", "derived", "inferred")
VERDICTS = ("LANDED", "LEAKED", "NOT-REACHED", "BYPASSED", "FALSE", "CONFOUNDED")
IDENTITY = ("kind", "task", "revision", "sql_sha256", "source", "model", "harness", "run", "node", "mechanism", "key",
            "supersedes")
NOT_LANDED = ("LEAKED", "FALSE", "BYPASSED")
TRANSFER_WEIGHT = 0.25


class LedgerError(ValueError):
    pass


def model_family(model) -> str:
    return re.sub(r"\[.*?\]$", "", str(model or "")).strip()


def canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def identity(rec: dict) -> dict:
    ident = {k: rec.get(k) for k in IDENTITY if rec.get(k) not in (None, "", [])}
    if "model" in ident:
        ident["model"] = model_family(ident["model"])
    return ident


def record_id(rec: dict) -> str:
    return "hev_" + hashlib.sha256(canonical(identity(rec)).encode()).hexdigest()[:16]


def payload(rec: dict) -> dict:
    return {k: v for k, v in rec.items() if k not in IDENTITY and k != "id"}


def check(rec: dict) -> dict:
    """Validate one record and return it with its id. Raises LedgerError."""
    if not isinstance(rec, dict):
        raise LedgerError("a record must be a JSON object")
    miss = [k for k in ("kind", "task", "revision", "source", "model", "harness", "epistemic") if not rec.get(k)]
    if miss:
        raise LedgerError(f"record lacks {miss} (model, harness and source are always kept)")
    h = rec["harness"]
    if not isinstance(h, dict) or not str(h.get("name") or "").strip() or not str(h.get("version") or "").strip():
        raise LedgerError("harness must be {name, version} (write 'unrecorded' when the export has none)")
    if rec["kind"] not in KINDS:
        raise LedgerError(f"kind {rec['kind']!r} not one of {KINDS}")
    if rec["source"] not in SOURCES:
        raise LedgerError(f"source {rec['source']!r} not one of {SOURCES}")
    if rec["epistemic"] not in EPISTEMIC:
        raise LedgerError(f"epistemic {rec['epistemic']!r} not one of {EPISTEMIC}")
    if rec["kind"] == "verdict":
        if rec.get("verdict") not in VERDICTS:
            raise LedgerError(f"verdict {rec.get('verdict')!r} not one of {VERDICTS}")
        if rec["verdict"] == "CONFOUNDED" and not (rec.get("features") or {}).get("disposed_by"):
            raise LedgerError("CONFOUNDED is a human disposition: features.disposed_by must name who assigned it")
        if not rec.get("run") or not rec.get("node"):
            raise LedgerError("a verdict needs run and node")
        f = rec.get("features") or {}
        if f.get("pending_review") and not f.get("disposed_by"):
            raise LedgerError(f"in-cohort errors {f['pending_review'][:6]} are pending review (mechanism?): disposition "
                              f"them and record features.disposed_by before appending")
    if rec["kind"] == "control":
        if rec.get("verdict") not in CONTROL_OUTCOMES or not rec.get("run") or not rec.get("node") or not rec.get("key"):
            raise LedgerError(f"a control trial needs run, node (the rule), key (the member) and a verdict in "
                              f"{CONTROL_OUTCOMES}")
    if rec["kind"] == "channel":
        if rec.get("verdict") not in CHANNEL_OUTCOMES or not rec.get("run") or not rec.get("node"):
            raise LedgerError(f"a channel record needs run, node (the channel) and a verdict in {CHANNEL_OUTCOMES}")
    if rec["kind"] == "observation":
        c = rec.get("counts") or {}
        if not isinstance(c, dict) or not isinstance(c.get("runs"), (int, float)):
            raise LedgerError("an observation needs counts {landed, not_landed | leaked, ..., runs}")
    if rec["kind"] in ("control", "channel"):
        ev = rec.get("evidence") or {}
        f = rec.get("features") or {}
        cov = ev.get("covered") if isinstance(ev.get("covered"), dict) else None
        covered_ok = bool(cov) and type(cov.get("members")) is int and cov["members"] >= 0
        event_ok = type(ev.get("deciding_event")) is int and ev["deciding_event"] >= 0
        dm = f.get("deciding_models")
        models_ok = isinstance(dm, list) and bool(dm) and all(isinstance(x, str) and x.strip() for x in dm)
        if not (event_ok or covered_ok or models_ok or f.get("deciding_model_unknown") is True):
            raise LedgerError(f"a {rec['kind']} record needs provenance: a deciding event, a deciding model, a covered "
                              f"count, or an explicit features.deciding_model_unknown (never inferred)")
    if rec["kind"] == "transfer":
        f = rec.get("features") or {}
        if not f.get("from_model") or not f.get("to_model") or "offset" not in f:
            raise LedgerError("a transfer needs features {from_model, to_model, offset}")
    w = rec.get("weight", 1.0)
    if not isinstance(w, (int, float)) or not 0 < w <= 1:
        raise LedgerError(f"weight {w!r} must be in (0, 1]")
    rid = record_id(rec)
    if rec.get("id") and rec["id"] != rid:
        raise LedgerError(f"id {rec['id']} does not match the record's identity ({rid})")
    return dict(rec, id=rid)


class Ledger:
    def __init__(self, path=DEFAULT_LEDGER):
        self.path = Path(path)
        self.records = []
        if self.path.is_file():
            for n, line in enumerate(self.path.read_text().splitlines(), 1):
                if line.strip():
                    try:
                        self.records.append(json.loads(line))
                    except ValueError as error:
                        raise LedgerError(f"{self.path}:{n}: not JSON ({error})")
        self.by_id = {r["id"]: r for r in self.records}

    def append(self, records) -> dict:
        """{'added': [...], 'present': [...], 'rejected': [(id or '?', reason)]}; writes only the added ones."""
        added, present, rejected = [], [], []
        for rec in records:
            try:
                r = check(rec)
            except LedgerError as error:
                rejected.append((rec.get("id", "?") if isinstance(rec, dict) else "?", str(error)))
                continue
            old = self.by_id.get(r["id"])
            if old is not None:
                if canonical(payload(old)) == canonical(payload(r)):
                    present.append(r["id"])
                else:
                    rejected.append((r["id"], "conflict: a different record with the same identity exists "
                                              "(append a correction with supersedes instead)"))
                continue
            if r.get("supersedes") and r["supersedes"] not in self.by_id:
                rejected.append((r["id"], f"supersedes unknown record {r['supersedes']}"))
                continue
            self.by_id[r["id"]] = r
            self.records.append(r)
            added.append(r)
        if added:
            from trajectory_ledger import safe_out
            safe_out(self.path)
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "a", encoding="utf-8") as fh:
                for r in added:
                    fh.write(canonical(r) + "\n")
        return {"added": [r["id"] for r in added], "present": present, "rejected": rejected}

    def current(self) -> list:
        superseded = {r.get("supersedes") for r in self.records if r.get("supersedes")}
        return [r for r in self.records if r["id"] not in superseded]

    def query(self, **kw) -> list:
        out = []
        for r in self.current():
            if all(v is None or (model_family(r.get(k)) == model_family(v) if k == "model" else r.get(k) == v)
                   for k, v in kw.items()):
                out.append(r)
        return out


# ------------------------------------------------------------------ priors

RHO = 0.5        # assumed correlation of the trials within one task (Kish design effect): an assumption


def design_effect(m: float, rho: float) -> float:
    return 1 + (m - 1) * rho if m > 1 else 1.0


def priors(led: Ledger, model: str, *, exclude_tasks=(), exclude_revisions=(), include_mixed=False, families=None,
           rho: float = RHO) -> dict:
    if not isinstance(rho, (int, float)) or not math.isfinite(rho) or not 0 <= rho <= 1:
        raise ValueError(f"rho must be a finite correlation in [0, 1], got {rho!r}")
    """{family: {alpha, beta, mean, n_eff, trials, tasks, record_ids, excluded}} for one model; never pools models.
    One trial per (task, revision, run, family); each task's trials discounted by the design effect (module docstring)."""
    fam = collections.defaultdict(lambda: {"trials": {}, "obs": [], "records": [], "excluded": []})
    for r in led.current():
        if r["kind"] not in ("verdict", "observation"):
            continue
        family = r.get("family") or r.get("mechanism")
        if not family or (families and family not in families):
            continue
        if model_family(r["model"]) != model_family(model):
            continue
        f = fam[family]
        if r["kind"] == "verdict":
            f.setdefault("all_verdict_groups", set()).add((r["task"], r["revision"]))
        if r["task"] in exclude_tasks or f"{r['task']}:{r['revision']}" in exclude_revisions or r["revision"] in exclude_revisions:
            f["excluded"].append([r["id"], "excluded task/revision"])
            continue
        if (r.get("features") or {}).get("mixed_model") and not include_mixed:
            f["excluded"].append([r["id"], "mixed-model run"])
            continue
        if r["kind"] == "verdict" and (r.get("features") or {}).get("control_explained"):
            # H1 residual a2: a LANDED verdict whose keys are all control-explained is never a landing, whatever the
            # record says (a second, independent gate under the classifier and the go rule). A verdict that also
            # landed an unexplained key stays a trial on that key.
            kept = set(r.get("keys") or []) - set(r["features"]["control_explained"])
            if r.get("verdict") == "LANDED" and not kept:
                f["excluded"].append([r["id"], "control-explained (key, field) evidence: never a landing"])
                continue
        w = float(r.get("weight", 1.0))
        if r["kind"] == "verdict":
            if r["verdict"] != "LANDED" and r["verdict"] not in NOT_LANDED:
                f["excluded"].append([r["id"], f"{r['verdict']} is never counted"])
                continue
            trial = f["trials"].setdefault((r["task"], r["revision"], r.get("run")),
                                           {"landed": False, "weight": 0.0, "records": []})
            trial["landed"] = trial["landed"] or r["verdict"] == "LANDED"
            trial["weight"] = max(trial["weight"], w)
            trial["records"].append(r["id"])
        else:
            # H1-2: an aggregate observation has no run identity; it contributes its run count as trials, and the
            # family's overlapping records collapse to one trial set (landed = max, a lower bound under maximal overlap)
            c = r["counts"]
            landed = float(c.get("landed", 0))
            not_landed = float(c.get("not_landed", sum(float(c.get(k, 0)) for k in ("leaked", "false", "bypassed"))))
            f["obs"].append({"task": r["task"], "revision": r["revision"],
                             "runs": int(c.get("runs") or (landed + not_landed)), "counted": landed + not_landed,
                             "landed": landed, "nl": not_landed, "weight": w, "id": r["id"]})
        f["records"].append(r["id"])
    out = {}
    for family, f in sorted(fam.items()):
        tasks = collections.defaultdict(lambda: {"trials": 0, "landed": 0.0, "not_landed": 0.0})
        for (task, _rev, _run), trial in f["trials"].items():
            x = tasks[task]
            x["trials"] += 1
            x["landed" if trial["landed"] else "not_landed"] += trial["weight"]
        grouped = collections.defaultdict(list)
        verdict_groups = set(f.get("all_verdict_groups") or ())
        for o in f["obs"]:
            grouped[(o["task"], o["revision"])].append(o)
        obs_up = collections.defaultdict(float)               # the upper bound's extra landed evidence, per task
        for (task, rev), os_ in sorted(grouped.items()):
            if (task, rev) in verdict_groups:
                f["excluded"].extend([[o["id"], f"observation and verdict records coexist for {task}:{rev}; "
                                                 f"not merged (no declared run ids)"] for o in os_])
                continue
            runs = {o["runs"] for o in os_}
            if len(runs) != 1:
                f["excluded"].extend([[o["id"], f"observation group {task}:{rev} declares differing counts.runs "
                                                 f"{sorted(runs)}: not merged"] for o in os_])
                continue
            runs.pop()                                   # the declarations must agree; trials are counted outcomes
            T = int(max(o["counted"] for o in os_))      # confounded runs are neither landing nor trial
            L = int(max(o["landed"] for o in os_))
            L_up = min(T, int(sum(o["landed"] for o in os_)))
            w = max(float(o["weight"]) for o in os_)
            x = tasks[task]
            x["trials"] += T
            x["landed"] += w * L
            x["not_landed"] += w * (T - L)
            obs_up[task] += w * (L_up - L)
        landed = not_landed = n_eff = 0.0
        per_task, up_landed, up_nl = {}, 0.0, 0.0
        for task, x in sorted(tasks.items()):
            m = x["landed"] + x["not_landed"]
            deff = design_effect(x["trials"], rho)            # the effect counts trials; weights scale the evidence
            landed += x["landed"] / deff
            not_landed += x["not_landed"] / deff
            n_eff += m / deff
            up_landed += (x["landed"] + obs_up.get(task, 0.0)) / deff
            up_nl += (x["not_landed"] - obs_up.get(task, 0.0)) / deff
            per_task[task] = {"trials": x["trials"], "weighted": round(m, 4), "deff": round(deff, 4),
                              "n_eff": round(m / deff, 4), "landed": round(x["landed"] / deff, 4)}
        bounds = None
        if any(obs_up.values()):
            la, lb, ua, ub = 1 + landed, 1 + not_landed, 1 + up_landed, 1 + up_nl
            bounds = {"lower": {"alpha": round(la, 4), "beta": round(lb, 4), "mean": round(la / (la + lb), 4),
                                "rule": "overlapping observation records assumed maximally overlapping (landed = max)"},
                      "upper": {"alpha": round(ua, 4), "beta": round(ub, 4), "mean": round(ua / (ua + ub), 4),
                                "rule": "overlapping observation records assumed disjoint (landed = min(runs, sum))"}}
        a, b = 1 + landed, 1 + not_landed
        out[family] = {"model": model_family(model), "alpha": round(a, 4), "beta": round(b, 4), "mean": round(a / (a + b), 4),
                       "n_eff": round(n_eff, 4), "trials": sum(x["trials"] for x in tasks.values()), "tasks": per_task,
                       "rho": rho, "record_ids": f["records"], "excluded": f["excluded"],
                       **({"observation_bounds": bounds} if bounds else {}),
                       "rule": "one trial per (task, revision, run, family); overlapping observation records collapse to "
                       "one trial set (T = the largest counted outcome total, landed = max: a lower bound, with the upper "
                       "bound reported); a task's evidence is divided by its Kish "
                               "design effect 1 + (m - 1) rho over its m trials (weights scale the evidence; rho an "
                               "assumption)",
                       "label": "UNCALIBRATED"}
    return out


def transferred(led: Ledger, from_model: str, to_model: str, family: str, base: dict | None = None) -> dict | None:
    """A prior for to_model built from from_model's posterior through an explicit transfer record, else None."""
    tr = [r for r in led.current() if r["kind"] == "transfer"
          and model_family((r.get("features") or {}).get("from_model")) == model_family(from_model)
          and model_family((r.get("features") or {}).get("to_model")) == model_family(to_model)
          and (r.get("family") in (None, family))]
    if not tr:
        return None
    t = tr[-1]
    src = (base or priors(led, from_model)).get(family)
    if not src:
        return None
    n = TRANSFER_WEIGHT * src["n_eff"]
    mean = min(0.99, max(0.01, src["mean"] + float(t["features"]["offset"])))
    a, b = 1 + mean * n, 1 + (1 - mean) * n
    return {"model": model_family(to_model), "alpha": round(a, 4), "beta": round(b, 4), "mean": round(a / (a + b), 4),
            "n_eff": round(n, 4), "record_ids": src["record_ids"] + [t["id"]], "excluded": [],
            "label": "TRANSFERRED · UNCALIBRATED", "transfer": t["id"]}


# ------------------------------------------------------------------ Season Pass seeds

PLATFORM_48 = {"name": "claude-code", "version": "2.1.280"}
PLATFORM_REV10 = {"name": "claude-code", "version": "unrecorded (revision-10 exports overwritten)"}
LIBRARY = {"name": "claude-code (platform, V0/V1 corpus)", "version": "unrecorded"}
REV10_SQL = "a4a197db27724ca25c28d72be8bb73f369457401fd2a7cbe5d56adae2dd31ed1"
REV13_SQL = "f4f195a598ac0f36efd4acb5a4073de518024f171d5f1cc48b75d09d068dde2e"

# 01a register (Working_Files/01a_Hardening_Report.md:55-69) -> per-run verdicts. Families follow plan §6's seed table
# where it names one (T4/T14 row association, T18/T19 A23, T10/T15-17 decoys every run reached); otherwise the trap is
# a FALSE node and its family is the plan §1.2 label "trap neutralised by an exact link or explicit rule".
REV10_REGISTER = [
    ("T1", "C2 circulation", {}, "FALSE", "A12", "trap neutralised by an exact link or explicit rule", "01a:57"),
    ("T3", "WATCH vocabulary", {}, "FALSE", "A15", "trap neutralised by an exact link or explicit rule", "01a:58"),
    ("T4/T14", "C3 snapshot history", {"run-1": "LANDED"}, "LEAKED", "A2", "row association at scale (A2 slip)", "01a:59"),
    ("T5", "wrong-game sheet", {}, "FALSE", "A5", "trap neutralised by an exact link or explicit rule", "01a:60"),
    ("T7", "same-subject other-game mail", {}, "FALSE", "A5", "trap neutralised by an exact link or explicit rule", "01a:61"),
    ("T8", "old review deck", {}, "FALSE", "A12", "trap neutralised by an exact link or explicit rule", "01a:62"),
    ("T10", "artifact-specific reviews", {}, "LEAKED", "A6", "decoys and authorities every run reached", "01a:63"),
    ("T11", "new tracker instead of reuse", {}, "FALSE", "A8", "trap neutralised by an exact link or explicit rule", "01a:64"),
    ("T12", "merged conclusion stop", {}, "FALSE", "A6", "trap neutralised by an exact link or explicit rule", "01a:65"),
    ("T13", "adjacent folder", {}, "FALSE", "A12", "trap neutralised by an exact link or explicit rule", "01a:66"),
    ("T15/T16/T17", "C1 own-package receipts", {}, "LEAKED", "A1", "decoys and authorities every run reached", "01a:67"),
    ("T18/T19", "C4 issue re-map", {"run-6": "LANDED"}, "LEAKED", "A23", "brief-transmission loss (A23)", "01a:68"),
    ("T20", "C5 tracker key lists", {}, "CONFOUNDED", "A14", "tracker key lists (C5)", "01a:69"),
]

# Hardness_Mastery.md §11 (calibration tasks, Opus 4.8): landed / leaked / confounded out of 6, weight 0.5 (aggregate)
LIBRARY_11 = [
    ("NF1", "partial resolution read from shipped code", "A15", 4, 2, 0, 723),
    ("NF1", "house rule: reviewer fixed it himself, leave it out (A15)", "A15", 2, 0, 4, 724),
    ("NF1", "scope boundary: the other title's board (A7)", "A7", 1, 4, 1, 725),
    ("NF1", "later APPROVED sign-off (A6), phantom spec (D11), bot vs human reviewer", "A6", 0, 6, 0, 726),
    ("NF2", "cohort members without the keyword in the title (A17)", "A17", 3, 3, 0, 728),
    ("NF2", "merged PRs whose title carries no ticket key (A18 + join)", "A18", 2, 4, 0, 729),
    ("NF2", "decision of record in the executives channel (A13)", "A13", 0, 6, 0, 731),
    ("V7-T1", "per-record house rule on what counts as landed (A15)", "A15", 4, 2, 0, 732),
    ("V7-T1", "finding on records whose state is already correct (A6/A15)", "A6", 5, 1, 0, 733),
    ("V7-T1", "channel-vs-runbook conflict the agent must report (A16)", "A16", 5, 1, 0, 734),
    ("V7-T1", "120-day owner-exemption split", "A15", 1, 5, 0, 735),
    ("V7-T1", "move off the ship line", "A15", 1, 5, 0, 735),
    ("V7-T1", "cohort vs stale deck (A17), revert, calendar authority, parent-child, cross-recipient emails", "A17", 0, 6, 0, 736),
    ("SB-T1", "correction only in a thread reply (A14)", "A14", 1, 5, 0, 739),
    ("SB-T1", "forced errors (3 tools at rate 1.0) + async Drive search", "friction", 0, 6, 0, 740),
]

# Hardness_Mastery.md §0 measured numbers with an explicit k/n run count (weak priors, weight 0.5). V7-T1 rows are
# covered by §11 and not repeated. A1's task document says "Baseline model updated to Opus 5.5" (plan §15.2): it is
# recorded under claude-opus-5-5 with its provenance flagged.
LIBRARY_0 = [
    ("ML-selected Combo Fighters", "A1", "wrong summary + thread past its conclusion (A1)", 6, 6, 41, "claude-opus-5-5",
     "pass@1 0/6; both consequential findings inverted (plan §6 seed table)"),
    ("Task8 Arthur's QA tool", "A5", "A5", 4, 6, 45, "claude-opus-4-8", "4/6 runs named a different genuine tool"),
    ("win&collect vs CollectAndWinEnabled", "A7", "A7", 2, 6, 47, "claude-opus-4-8", "2/6 decided the alias did not bind"),
    ("vendor reply validating 1 of 3 charges", "A9", "A9", 4, 5, 49, "claude-opus-4-8", "4/5 runs missed it"),
    ("SB-T2", "A12", "A12", 5, 6, 59, "claude-opus-4-8", "5/6 latched onto a Confluence decoy and never searched Trello"),
    ("V0-T10", "A13", "A13", 6, 6, 60, "claude-opus-4-8", "0 Gmail calls in 6/6; two rubrics failed 6/6"),
    ("FE-6a7e", "A17", "A17", 23, 30, 64, "claude-opus-4-8", "23/30 runs reported 19 of 27 instead of 20 of 28"),
    ("V0-T11", "A18", "A18", 6, 6, 65, "claude-opus-4-8", "three tickets never appeared in any of 6 runs"),
    ("V0-T4", "A19", "A19", 6, 6, 66, "claude-opus-4-8", "comparison missing 6/6"),
    ("V0-T1", "A20", "A20", 6, 6, 67, "claude-opus-4-8", "subagent synthesis loss 6/6"),
    ("V0-T8", "A20", "A20", 4, 6, 67, "claude-opus-4-8", "subagent synthesis loss 4/6"),
]

# Revision 13 (attribution.json + plans/Rev13_Results.md §3): rule -> (nodes, mechanism from the manifest chain, family)
REV13_RULES = {
    "validation": ("T21/T22/T23", "A17", "manifest C6"),
    "receipt": ("T24/T25/T26", "A13", "manifest C7"),
    "journal": ("T35", "A13", "manifest C10"),
    "review": ("T27/T28/T29/T32", "A15", "manifest C8"),
    "fixture_binding": ("T33/T34", "A19", "manifest C9"),
    "acceptance": ("T36/T38", "A17", "manifest C11"),
    "history": ("T37", "A17", "manifest C11"),
    "snapshot_labels": ("T4/T14", "A14", "manifest C3"),
    "remap": ("T18/T19", "A23", "plan §6 seed table (design chain C4, A13)"),
    "own_package": ("T15/T16/T17", "A1", "manifest C1"),
    "t39_export": ("T39", "A1", "trap family stale_summary (no chain)"),
    "tracker_keys": ("C5/K15", "A14", "manifest C5"),
}
REV13_FAMILY = {"validation": "A17", "receipt": "A13", "journal": "A13", "review": "A15", "fixture_binding": "A19",
                "acceptance": "A17", "history": "A17", "snapshot_labels": "A14", "remap": "brief-transmission loss (A23)",
                "own_package": "decoys and authorities every run reached",
                "t39_export": "decoys and authorities every run reached", "tracker_keys": "A14"}
REV13_RUNS = {"precheck": "platform-precheck", **{f"run-{i}": "platform-baseline" for i in range(1, 7)}}
REV13_FALLBACK = {"precheck": (5855, False), "run-3": (987, True), "run-4": (779, True), "run-5": (2134, True)}

# Corrections to seed records. The ledger never edits a record: each correction is appended as a new record that
# supersedes the original. (match on the original's fields, dotted for nested ones; changes; reason; the plan line that
# decides and the text it must still contain).
SEED_CORRECTIONS = [
    ({"kind": "observation", "task": "library:V7-T1", "evidence.line": 736},
     {"family": "decoys and authorities every run reached"},
     "plan §6 seed table places V7-T1 :736 (0/6) in 'Decoys and authorities every run reached'; the first seed took "
     "the row's first tag (A17) as its family",
     462, ("Decoys and authorities every run reached", "V7-T1 (`:736`)")),
]


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _field(rec: dict, dotted: str):
    v = rec
    for part in dotted.split("."):
        v = v.get(part) if isinstance(v, dict) else None
    return v


def corrections(out: list, plan: Path, table=None) -> list:
    """Superseding records for SEED_CORRECTIONS, each matched to exactly one seed record."""
    lines = plan.read_text().splitlines()
    fixed = []
    for match, changes, reason, line, needles in SEED_CORRECTIONS if table is None else table:
        if not all(n in lines[line - 1] for n in needles):
            raise LedgerError(f"{plan.name}:{line} no longer reads {needles}; refusing to apply the seed correction")
        hits = [r for r in out if all(_field(r, k) == v for k, v in match.items())]
        if len(hits) != 1:
            raise LedgerError(f"seed correction {match} matches {len(hits)} seed records, expected 1")
        old = hits[0]
        fixed.append(dict(old, **changes, supersedes=check(old)["id"],
                          evidence=dict(old["evidence"], correction=reason, plan=f"{plan.name}:{line}",
                                        plan_sha256=_sha(plan)),
                          features=dict(old.get("features") or {}, producer="seed correction")))
    return fixed


def seed_season_pass(frozen: Path) -> list:
    """Source-tagged seed records from the frozen revision-13 copy (its README lists the layout)."""
    reg = frozen / "working_files" / "01a_Hardening_Report.md"
    attr = frozen / "reference" / "attribution.json"
    results = BUNDLE / "plans" / "Rev13_Results.md"
    mastery = BUNDLE / "references" / "Hardness_Mastery.md"
    text = reg.read_text().splitlines()
    if not any(l.startswith("| T18/T19 / C4 issue re-map | LANDED") for l in text[54:69]):
        raise LedgerError(f"{reg}: the register at lines 55-69 does not match the seed table; refusing to seed")
    out = []
    ev_reg = {"file": "support/backtests/season_pass/rev13/working_files/01a_Hardening_Report.md", "sha256": _sha(reg)}
    for node, label, landed_in, default, mech, family, line in REV10_REGISTER:
        for run in [f"run-{i}" for i in range(1, 7)]:
            verdict = landed_in.get(run, default)
            rec = {"kind": "verdict", "task": "season_pass", "revision": "rev10", "sql_sha256": REV10_SQL,
                   "source": "platform-baseline", "model": "claude-opus-4-8", "harness": PLATFORM_REV10, "run": run,
                   "node": node, "mechanism": mech, "family": family, "verdict": verdict, "epistemic": "derived",
                   "evidence": dict(ev_reg, lines="55-69", row=line, label=label), "weight": 1.0,
                   "features": {"producer": "seed:01a register"}}
            if verdict == "CONFOUNDED":
                rec["features"]["disposed_by"] = "01a_Hardening_Report.md register (CONFOUNDED-fairness/verifier)"
            out.append(rec)
    ev_m = {"file": "Task_Authoring/references/Hardness_Mastery.md", "sha256": _sha(mastery)}
    for task, label, mech, landed, leaked, confounded, line in LIBRARY_11:
        out.append({"kind": "observation", "task": f"library:{task}", "revision": "baseline", "source": "platform-baseline",
                    "model": "claude-opus-4-8", "harness": LIBRARY, "node": label, "mechanism": mech, "family": mech,
                    "counts": {"landed": landed, "leaked": leaked, "confounded": confounded, "runs": 6},
                    "epistemic": "derived", "weight": 0.5, "evidence": dict(ev_m, section="11", line=line),
                    "features": {"producer": "seed:Hardness_Mastery §11"}})
    for task, mech, family, landed, runs, line, model, basis in LIBRARY_0:
        out.append({"kind": "observation", "task": f"library:{task}", "revision": "baseline", "source": "platform-baseline",
                    "model": model, "harness": LIBRARY, "node": f"{mech} §0", "mechanism": mech, "family": family,
                    "counts": {"landed": landed, "not_landed": runs - landed, "runs": runs}, "epistemic": "derived",
                    "weight": 0.5, "evidence": dict(ev_m, section="0", line=line, basis=basis),
                    "features": {"producer": "seed:Hardness_Mastery §0", "weak_prior": True,
                                 **({"model_provenance": "uncertain: the example document's change log says the baseline "
                                     "model was updated to Opus 5.5 (plan §15.2)"} if model != "claude-opus-4-8" else {})}})
    a = json.loads(attr.read_text())
    ev_a = {"file": "support/backtests/season_pass/rev13/reference/attribution.json", "sha256": _sha(attr),
            "results": "Task_Authoring/plans/Rev13_Results.md §3", "results_sha256": _sha(results)}
    landed = {("run-4", "validation"): {"keys": sorted({i["key"] for i in a["runs"]["base-run-4"]
                                                        if "validation" in i["reproduced_by_ignoring"]}),
                                        "note": a["run4_brief_note"]},
              ("run-3", "snapshot_labels"): {"keys": sorted({i["key"] for i in a["runs"]["base-run-3"]
                                                             if "billing history" in (i.get("note") or "")}),
                                             "note": "billing history: labels removed before the snapshot reported as held"},
              ("run-6", "acceptance"): {"keys": sorted({i["key"] for i in a["runs"]["base-run-6"]
                                                        if "acceptance" in i["reproduced_by_ignoring"]}),
                                        "note": "acceptance epoch; the rule was present in the brief (Rev13_Results §3)"}}
    for run, source in REV13_RUNS.items():
        fb = REV13_FALLBACK.get(run)
        feats = {"producer": "seed:attribution.json + Rev13_Results §3"}
        if fb:
            feats.update(fallback_event=fb[0], fallback_model="claude-opus-5",
                         mixed_model=fb[1], **({} if fb[1] else {"fallback_after_last_call": True}))
        for rule, (nodes, mech, basis) in REV13_RULES.items():
            hit = landed.get((run, rule))
            rec = {"kind": "verdict", "task": "season_pass", "revision": "rev13", "sql_sha256": REV13_SQL,
                   "source": source, "model": "claude-opus-4-8", "harness": PLATFORM_48, "run": run, "node": rule,
                   "mechanism": mech, "family": REV13_FAMILY[rule], "verdict": "LANDED" if hit else "LEAKED",
                   "epistemic": "derived", "evidence": dict(ev_a, nodes=nodes, basis=basis, **({"note": hit["note"]} if hit else {})),
                   "weight": 1.0, "features": dict(feats)}
            if hit:
                rec["keys"] = hit["keys"]
            out.append(rec)
        out.append({"kind": "reach", "task": "season_pass", "revision": "rev13", "sql_sha256": REV13_SQL, "source": source,
                    "model": "claude-opus-4-8", "harness": PLATFORM_48, "run": run, "node": "ZOM-801 comments",
                    "key": "cmt_c0696e5f7676681c910c", "verdict": "NOT-REACHED", "epistemic": "observed",
                    "evidence": dict(ev_a, note=a["not_read_in_any_run"][0]), "features": dict(feats)})
    for run, key in (("run-1", "SP-043"), ("run-4", "SP-079")):
        items = [i for i in a["runs"][f"base-{run}"] if i["key"] == key]
        out.append({"kind": "slip", "task": "season_pass", "revision": "rev13", "sql_sha256": REV13_SQL,
                    "source": "platform-baseline", "model": "claude-opus-4-8", "harness": PLATFORM_48, "run": run,
                    "node": "unattributed", "key": key, "epistemic": "derived",
                    "evidence": dict(ev_a, fields=[i["field"] for i in items], note=items[0].get("note")),
                    "features": dict(REV13_FALLBACK.get(run) and {"mixed_model": REV13_FALLBACK[run][1]} or {},
                                     producer="seed:attribution.json")})
    return out + corrections(out, BUNDLE / "plans" / "Fold_Hardening_Into_Scenario_And_Injection.md")


# ------------------------------------------------------------------ self-test

def _self_test() -> None:
    base = {"kind": "verdict", "task": "t", "revision": "r1", "source": "platform-baseline", "model": "claude-opus-4-8[1m]",
            "harness": {"name": "claude-code", "version": "1"}, "run": "run-1", "node": "N1", "mechanism": "A15",
            "family": "A15", "verdict": "LANDED", "epistemic": "observed"}
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("hardness_ledger_selftest_") as tmp:   # a temp ledger, never the shared one
        path = Path(tmp) / "ledger.jsonl"
        assert path.resolve() != DEFAULT_LEDGER.resolve()
        led = Ledger(path)
        r = led.append([base])
        assert len(r["added"]) == 1 and not r["rejected"], r
        assert Ledger(path).append([base])["present"] == r["added"]                       # idempotent
        conflict = Ledger(path).append([dict(base, verdict="LEAKED")])
        assert conflict["rejected"] and "conflict" in conflict["rejected"][0][1], conflict
        for k in ("model", "harness", "source"):
            bad = Ledger(path).append([{x: y for x, y in base.items() if x != k}])
            assert bad["rejected"] and k in bad["rejected"][0][1], (k, bad)
        assert Ledger(path).append([dict(base, harness={"name": "x"})])["rejected"]
        assert Ledger(path).append([dict(base, verdict="CONFOUNDED", run="run-9")])["rejected"]   # never a tool verdict
        assert Ledger(path).append([dict(base, id="hev_0000000000000000")])["rejected"]
        led = Ledger(path)
        corr = dict(base, verdict="LEAKED", supersedes=r["added"][0], evidence={"why": "re-read"})
        assert led.append([corr])["added"]
        more = [dict(base, run=f"run-{i}", verdict="LEAKED") for i in (2, 3)] + \
               [dict(base, run="run-4", verdict="NOT-REACHED"), dict(base, run="run-5", features={"mixed_model": True}),
                dict(base, run="run-6", model="claude-opus-5-5"), dict(base, task="other", run="run-1")]
        led.append(more)
        p = priors(Ledger(path), "claude-opus-4-8")["A15"]
        # run-1 corrected to LEAKED, runs 2-3 LEAKED (task t: 3 trials, design effect 1 + 2 x 0.5 = 2, so 1.5
        # non-landings), other task LANDED (1 trial): Beta(1 + 1, 1 + 1.5); NOT-REACHED / mixed / 5.5 out
        assert (p["alpha"], p["beta"]) == (2.0, 2.5) and p["tasks"]["t"]["n_eff"] == 1.5, p
        assert any("mixed-model" in e[1] for e in p["excluded"]) and any("NOT-REACHED" in e[1] for e in p["excluded"])
        assert priors(Ledger(path), "claude-opus-4-8", rho=0.0)["A15"]["beta"] == 4.0          # rho 0: independent
        assert priors(Ledger(path), "claude-opus-4-8", rho=1.0)["A15"]["beta"] == 2.0          # rho 1: one trial
        p2 = priors(Ledger(path), "claude-opus-4-8", exclude_tasks=("other",))["A15"]
        assert (p2["alpha"], p2["beta"]) == (1.0, 2.5), p2
        # H2 planted: three rules of one family in one run are one trial (the old de-duplication counted three)
        three = [dict(base, task="fam", run="run-1", node=f"N{i}", family="A17", verdict="LEAKED") for i in (1, 2, 3)]
        Ledger(path).append(three + [dict(three[0], run="run-2", node="N1", verdict="LANDED"),
                                     dict(three[0], run="run-2", node="N2", verdict="LEAKED")])
        q17 = priors(Ledger(path), "claude-opus-4-8")["A17"]
        assert q17["trials"] == 2 and q17["tasks"]["fam"]["weighted"] == 2.0, q17               # run-1, run-2
        assert (q17["alpha"], q17["beta"]) == (round(1 + 1 / 1.5, 4), round(1 + 1 / 1.5, 4)), q17   # deff 1.5
        assert priors(Ledger(path), "claude-opus-5-5")["A15"]["alpha"] == 2.0                   # never pooled
        assert transferred(Ledger(path), "claude-opus-4-8", "claude-opus-5-5", "A15") is None    # no transfer record
        Ledger(path).append([{"kind": "transfer", "task": "bridge", "revision": "n/a", "source": "forecast",
                              "model": "claude-opus-5-5", "harness": {"name": "n/a", "version": "n/a"},
                              "epistemic": "inferred", "family": "A15",
                              "features": {"from_model": "claude-opus-4-8", "to_model": "claude-opus-5-5", "offset": -0.1}}])
        t = transferred(Ledger(path), "claude-opus-4-8", "claude-opus-5-5", "A15")
        assert t and t["label"].startswith("TRANSFERRED") and t["n_eff"] == 0.625, t          # 0.25 x n_eff 2.5
        obs = Ledger(path).append([{"kind": "observation", "task": "lib", "revision": "b", "source": "platform-baseline",
                                    "model": "claude-opus-4-8", "harness": {"name": "x", "version": "y"},
                                    "epistemic": "derived", "family": "A16", "node": "n", "weight": 0.5,
                                    "counts": {"landed": 5, "leaked": 1, "runs": 6}}])
        assert obs["added"]
        q = priors(Ledger(path), "claude-opus-4-8")["A16"]
        # 6 library runs at weight 0.5: 6 trials, design effect 1 + 5 x 0.5 = 3.5: Beta(1 + 2.5 / 3.5, 1 + 0.5 / 3.5)
        assert (q["alpha"], q["beta"]) == (1.7143, 1.1429) and q["record_ids"] == obs["added"], q
        # planted (H2): the design effect counts trials, not weighted trials: at rho = 1 the six correlated runs are one
        # trial times their weight 0.5 (counting weighted trials gave 1.0)
        assert priors(Ledger(path), "claude-opus-4-8", rho=1.0)["A16"]["n_eff"] == 0.5
        # planted (H1-2): overlapping observation records are one trial set: trials = max counted outcomes, landed = max
        # landed (the lower bound under maximal overlap); the upper bound assumes the runs are disjoint
        def obsrec(**kw):
            return dict({"kind": "observation", "task": "ov", "revision": "b", "source": "platform-baseline",
                         "model": "claude-opus-4-8", "harness": {"name": "x", "version": "y"}, "epistemic": "derived",
                         "node": "n", "weight": 0.5}, **kw)
        Ledger(path).append([obsrec(family="A19", node="n1", counts={"landed": 4, "leaked": 2, "runs": 6}),
                             obsrec(family="A19", node="n2", counts={"landed": 2, "leaked": 4, "runs": 6})])
        q19 = priors(Ledger(path), "claude-opus-4-8")["A19"]
        assert q19["trials"] == 6 and (q19["alpha"], q19["beta"]) == (1.5714, 1.2857), q19    # 6, not 8 or 12
        lo, up = q19["observation_bounds"]["lower"], q19["observation_bounds"]["upper"]
        assert (lo["alpha"], lo["beta"]) == (1.5714, 1.2857), lo
        assert (up["alpha"], up["beta"]) == (1.8571, 1.0), up                                  # sum(landed) capped at T
        # planted (H1-2): a confounded run is neither a landing nor a trial (T = landed + not_landed, not counts.runs)
        Ledger(path).append([dict(obsrec(family="A20", task="cf", weight=1.0),
                                  counts={"landed": 1, "leaked": 4, "runs": 6, "confounded": 1})])
        q20 = priors(Ledger(path), "claude-opus-4-8")["A20"]
        assert q20["trials"] == 5 and (q20["alpha"], q20["beta"]) == (1.3333, 2.3333), q20   # deff 3 at rho 0.5
        # planted (H1-2): an aggregate and an explicit verdict for the same (task, revision, family) never double-count
        Ledger(path).append([dict(base, task="mix", run="run-1", family="A22", verdict="LANDED"),
                             obsrec(family="A22", task="mix", revision="r1", node="agg",
                                    counts={"landed": 1, "leaked": 0, "runs": 1})])
        q22 = priors(Ledger(path), "claude-opus-4-8")["A22"]
        assert q22["trials"] == 1 and any("coexist" in e[1] for e in q22["excluded"]), q22
        # planted (H1-2): records that declare different run counts are not merged
        Ledger(path).append([obsrec(family="A21", task="df", node="n1", counts={"landed": 2, "leaked": 4, "runs": 6}),
                             obsrec(family="A21", task="df", node="n2", counts={"landed": 1, "leaked": 4, "runs": 5})])
        q21 = priors(Ledger(path), "claude-opus-4-8")["A21"]
        assert q21["trials"] == 0 and any("differing counts.runs" in e[1] for e in q21["excluded"]), q21
        # planted (H1-3): rho is a correlation, not any number
        for bad in (-0.1, 1.5, float("nan")):
            try:
                priors(Ledger(path), "claude-opus-4-8", rho=bad)
            except ValueError:
                pass
            else:
                raise AssertionError(f"rho {bad!r} was accepted")
        # a seed correction supersedes its original and moves the counts to the corrected family, idempotently
        # control and channel records are kept but never enter the priors; an unreviewed mechanism? is refused
        before = priors(Ledger(path), "claude-opus-4-8")["A15"]
        trial = dict(base, kind="control", run="run-7", key="K-04", verdict="OVER-APPLIED",
                     evidence={"deciding_event": 91})
        chan = dict(base, kind="channel", run="run-7", node="scale:count", family="scale", verdict="FAILED",
                    evidence={"deciding_event": 92})
        assert len(Ledger(path).append([trial, chan])["added"]) == 2
        # H1 residual b/f: a control/channel record with no provenance at all is refused, never inferred
        assert Ledger(path).append([dict(chan, node="scale:noprov", evidence={}, features={})])["rejected"]
        # H1 residual a2: a verdict whose landing is control-explained never moves a prior
        ce = dict(base, run="run-10", verdict="LANDED", keys=["K-04"],
                  features={"control_explained": ["K-04"]})
        assert Ledger(path).append([ce])["added"]
        qce = priors(Ledger(path), "claude-opus-4-8")["A15"]
        assert any("control-explained" in e[1] for e in qce["excluded"]), qce["excluded"]
        after = priors(Ledger(path), "claude-opus-4-8")["A15"]
        assert (after["alpha"], after["beta"], after["record_ids"]) == (before["alpha"], before["beta"],
                                                                        before["record_ids"]), (before, after)
        # H1 residual b/f: the provenance gate requires a REAL covered count (a truthy dict or a bool/string is not one)
        for j, bad_cov in enumerate(({"observed": 1}, {"members": None}, {"members": "1"}, {"members": True})):
            assert Ledger(path).append([dict(chan, node=f"scale:cov{j}", evidence={"covered": bad_cov},
                                             features={})])["rejected"], bad_cov
        assert Ledger(path).append([dict(chan, node="scale:covok", evidence={"covered": {"members": 1}},
                                         features={})])["added"]
        # an explicit unknown must be a real True, not a truthy string
        assert Ledger(path).append([dict(chan, node="scale:strunknown", evidence={},
                                         features={"deciding_model_unknown": "false"})])["rejected"]
        # H1 residual a2 (preservation): a LANDED verdict that ALSO has an unexplained key stays a trial; only the
        # control-explained key is removed, never the whole record
        base_q = priors(Ledger(path), "claude-opus-4-8")["A15"]
        keep = dict(base, run="run-11", verdict="LANDED", keys=["K-01", "K-04"],
                    features={"control_explained": ["K-04"]})
        kid = Ledger(path).append([keep])["added"][0]
        qk = priors(Ledger(path), "claude-opus-4-8")["A15"]
        assert kid in qk["record_ids"] and qk["trials"] == base_q["trials"] + 1, (
            f"the legitimate landing {kid} was removed from the prior with its control-explained key", kid, qk)
        assert Ledger(path).append([dict(trial, key="K-05", verdict="LANDED")])["rejected"]    # not a trial outcome
        assert Ledger(path).append([{x: y for x, y in trial.items() if x != "key"}])["rejected"]
        pend = dict(base, run="run-8", verdict="LEAKED", features={"pending_review": ["K-01"]})
        assert Ledger(path).append([pend])["rejected"]
        assert Ledger(path).append([dict(pend, features={"pending_review": ["K-01"], "disposed_by": "author: slip"})])["added"]
        plan = path.parent / "plan.md"
        plan.write_text("intro\n| Decoys every run reached | 0/6 | lib (`:9`) |\n")
        seed = [{"kind": "observation", "task": "lib2", "revision": "b", "source": "platform-baseline",
                 "model": "claude-opus-4-8", "harness": {"name": "x", "version": "y"}, "epistemic": "derived",
                 "family": "A16", "node": "n", "weight": 0.5, "counts": {"landed": 0, "leaked": 6, "runs": 6},
                 "evidence": {"line": 9}}]
        table = [({"task": "lib2", "evidence.line": 9}, {"family": "decoys"}, "plan says so", 2, ("Decoys", "`:9`"))]
        assert Ledger(path).append(seed + corrections(seed, plan, table))["added"]
        again = Ledger(path).append(seed + corrections(seed, plan, table))
        assert not again["added"] and not again["rejected"], again
        pr = priors(Ledger(path), "claude-opus-4-8")
        assert pr["decoys"]["n_eff"] == 0.8571 and pr["A16"]["n_eff"] == 0.8571, pr   # the original no longer counts
        plan.write_text("intro\n| rewritten |\n")
        try:
            corrections(seed, plan, table)
        except LedgerError:
            pass
        else:
            raise AssertionError("a correction whose plan line changed was applied")
    print("self-test: ok (content ids, idempotent append, conflict rejected, model/harness/source required, CONFOUNDED "
          "only as a disposition, supersession, per-model Beta priors with record ids, exclusions, weights, transfer, "
          "seed corrections guarded by their plan line, control and channel records kept outside the priors, an "
          "unreviewed mechanism? refused; H2: one trial per (task, revision, run, family), the Kish design effect per "
          "task over its trials with rho 0 / 0.5 / 1 (weights scale the evidence: at rho 1 a weighted task is one "
          "trial times its weight), n_eff per task)")


# ------------------------------------------------------------------ main

def _print_append(res) -> int:
    print(f"added {len(res['added'])} · already present {len(res['present'])} · rejected {len(res['rejected'])}")
    for rid, why in res["rejected"][:20]:
        print(f"  REJECTED {rid}: {why}")
    return 1 if res["rejected"] else 0


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="hardness_ledger.py", description="cross-task evidence ledger (see docstring)")
    ap.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    ap.add_argument("--task-dir", type=Path, help="accepted for symmetry; the ledger is cross-task")
    ap.add_argument("--self-test", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("append")
    p.add_argument("file")
    p = sub.add_parser("seed")
    p.add_argument("--season-pass", type=Path, required=True)
    for name in ("priors", "write-priors"):
        p = sub.add_parser(name)
        if name == "write-priors":
            p.add_argument("out", type=Path)
        p.add_argument("--model", required=True)
        p.add_argument("--exclude-task", action="append", default=[])
        p.add_argument("--exclude-revision", action="append", default=[])
        p.add_argument("--include-mixed", action="store_true")
        p.add_argument("--family", action="append")
        p.add_argument("--rho", type=float, default=RHO, help=f"within-task trial correlation for the design effect "
                                                              f"(default {RHO}: an assumption)")
        p.add_argument("--json", action="store_true")
    p = sub.add_parser("transfer")
    p.add_argument("--from-model", required=True)
    p.add_argument("--to-model", required=True)
    p.add_argument("--offset", type=float, required=True)
    p.add_argument("--evidence", required=True)
    p.add_argument("--family")
    p = sub.add_parser("query")
    p.add_argument("--kind")
    p.add_argument("--task")
    p.add_argument("--model")
    p.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        _self_test()
        return 0
    led = Ledger(a.ledger)
    if a.cmd == "append":
        text = sys.stdin.read() if a.file == "-" else Path(a.file).read_text()
        return _print_append(led.append([json.loads(l) for l in text.splitlines() if l.strip()]))
    if a.cmd == "seed":
        return _print_append(led.append(seed_season_pass(a.season_pass)))
    if a.cmd in ("priors", "write-priors"):
        pr = priors(led, a.model, exclude_tasks=a.exclude_task, exclude_revisions=a.exclude_revision,
                    include_mixed=a.include_mixed, families=a.family, rho=a.rho)
        doc = {"kind": "MECHANISM_PRIORS", "label": "UNCALIBRATED", "model": model_family(a.model),
               "ledger": str(a.ledger), "ledger_sha256": hashlib.sha256(a.ledger.read_bytes()).hexdigest() if a.ledger.is_file() else None,
               "exclude_task": a.exclude_task, "exclude_revision": a.exclude_revision, "rho": a.rho,
               "rho_basis": "assumed within-task trial correlation (Kish design effect); not measured", "families": pr}
        if a.cmd == "write-priors":
            from trajectory_ledger import safe_out
            out = safe_out(a.out)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
            print(f"wrote {out}")
            return 0
        if a.json:
            print(json.dumps(doc, indent=1, ensure_ascii=False))
        else:
            print(f"PRIORS for {model_family(a.model)} · UNCALIBRATED · Beta(1,1) + effective counts (one trial per "
                  f"task, revision, run and family; design effect per task, rho {a.rho}: an assumption)")
            for fam, v in pr.items():
                print(f"  {fam}: Beta({v['alpha']}, {v['beta']}) mean {v['mean']:.2f} n_eff {v['n_eff']} from "
                      f"{v['trials']} trial(s) · per task "
                      + ", ".join(f"{task} {x['n_eff']} ({x['trials']} trial(s), deff {x['deff']})"
                                  for task, x in v["tasks"].items())
                      + f" · records {len(v['record_ids'])} excluded {len(v['excluded'])}")
                if v.get("observation_bounds"):
                    lo, up = v["observation_bounds"]["lower"], v["observation_bounds"]["upper"]
                    print(f"     observation bounds: lower Beta({lo['alpha']}, {lo['beta']}) mean {lo['mean']}; "
                          f"upper Beta({up['alpha']}, {up['beta']}) mean {up['mean']}")
        return 0
    if a.cmd == "transfer":
        return _print_append(led.append([{"kind": "transfer", "task": "model-bridge", "revision": "n/a", "source": "forecast",
                                          "model": a.to_model, "harness": {"name": "n/a", "version": "n/a"},
                                          "epistemic": "inferred", "family": a.family, "evidence": {"text": a.evidence},
                                          "features": {"from_model": a.from_model, "to_model": a.to_model,
                                                       "offset": a.offset}}]))
    if a.cmd == "query":
        rows = led.query(kind=a.kind, task=a.task, model=a.model)
        if a.json:
            print(json.dumps(rows, indent=1, ensure_ascii=False))
        else:
            for r in rows:
                print(f"{r['id']} {r['kind']} {r['task']} {r['revision']} {r.get('run') or ''} {r.get('node') or ''} "
                      f"{r.get('verdict') or r.get('counts') or ''} {r['model']} {r['source']}")
        return 0
    ap.print_usage(sys.stderr)
    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (LedgerError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"hardness_ledger: {error}", file=sys.stderr)
        raise SystemExit(2)

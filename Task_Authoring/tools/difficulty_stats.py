#!/usr/bin/env python3
"""Compute assignment-aware V3 baseline difficulty gates from a rubric x rollout matrix.

V3: exactly six rollout slots, Opus 5.5 provenance, fewer than five full passes,
and average weighted pass strictly below the assigned Easy/Medium/Hard cap
(90%/85%/70%). Corrected fair results determine the verdict; raw results remain
visible for audit. Errored slots are excluded from score/SD/horizon averages,
not scored as zero. Existing error, spread, pattern and horizon policy is retained.
Use --task-dir to bind the matrix to the current normalized assignment. A task
folder is otherwise inferred from input paths. --legacy-v2 is explicit archival
compatibility and must not be used to submit a V3 assignment.

Legacy V2 gates (strictest of QC Spec V2 and Evals references/rules/scoring.json —
see setup/GEN_EXECUTION.md §3):
  - Errored runs:        <= 2 errored and >= 4 completed (3+ of 6 errored = Fail).
                         Empty trajectory = errored; empty verifier output is NOT.
  - pass@1:              <= 50% of completed rollouts pass every rubric (<= 3 of 6)
  - Avg weighted pass:   < 75% gate (Evals scoring.json; QC Spec V2 alone allows < 90%)
  - Per-rollout spread:  population standard deviation of the per-rollout weighted pass
                         rates within 0.1-0.3 (Evals scoring.json: > 0.3 suggests ambiguous
                         rubrics, < 0.1 a deterministic task that needs friction)
  - Failure patterns:    >= 2 distinct patterns; largest <= 50% of failing rollouts.
                         Two failing rollouts are the same pattern unless their
                         rubric results differ on >= 2 rubrics. Verdict on single-linkage
                         grouping (strictest); the pairwise-clique reading is shown beside it.
  - Horizon:             counted tool calls of the golden run (100% rollout) if any,
                         else the average over completed rollouts.
                         normal 50-100, long-horizon 100+. Under = Fail,
                         over the normal band = Non-fail (Borderline Horizon).

Two views are computed (WORKFLOW: preserve raw results, never silently change them):
  - platform view: every rubric, raw verifier results (what the platform screen shows);
  - valid view:    rubrics marked "valid": false excluded and explicit per-rollout
                   "judge_corrections" applied (QC pass@1: "pass all valid rubrics";
                   scoring.json: "score only valid rubrics").
For V3 only the corrected view blocks; legacy V2 blocks either view. Without
invalid rubrics or corrections the views are identical and one is printed.

Input JSON (write it with --build, or by hand):

  {
    "spec_version": "V3", "difficulty_mode": "easy",
    "context": {"assignment_hash": "...", "policy_hash": "...", "context_hash": "..."},
    "task_type": "normal" | "long-horizon"   (or "Normal Horizon" | "Long Horizon"),
    "rubrics": [{"id": "R1", "weight": 3, "valid": true}, ...],
    "rollouts": [
      {"id": "run-1", "status": "completed", "tool_calls": 87,
       "models": ["claude-opus-5-5"], "model_source": "trajectory:run-1.json",
       "results": {"R1": true, "R2": false, ...},
       "judge_corrections": {"R2": true}},          # optional, with evidence in 11_
      {"id": "run-6", "status": "errored"}
    ]
  }

Usage:
  python3 Task_Authoring/tools/difficulty_stats.py --build \\
      --verifier Task_Authoring/task_inputs/10_Baseline_Verifier_Results.md \\
      --rubrics Task_Authoring/task_inputs/09_Rubrics.json \\
      --trajectories Task_Authoring/task_inputs/07_Baseline_Trajectories \\
      --task-dir Task_Authoring/task_inputs [--task-type "Long Horizon"] \\
      [--invalid R6,R7] [--judge-correction run-3:R5 ...] \\
      [--out Task_Authoring/task_inputs/Working_Files/12_difficulty_input.json]
  python3 Task_Authoring/tools/difficulty_stats.py <input.json>          # markdown
  python3 Task_Authoring/tools/difficulty_stats.py <input.json> --json   # machine-readable
  python3 Task_Authoring/tools/difficulty_stats.py --self-test

--build parses the platform exports. Verifier results: the "Run verifiers" copy
("Run #N", "X/Y criteria passed", then one tab-separated "title<TAB>Pass|Fail<TAB>
justification" row per criterion). Rows bind to 09_Rubrics.json by normalised title
(markdown autolinks, escaped quotes, curly quotes and whitespace normalised); every
row must bind exactly once and each run's "X/Y criteria passed" header must match its
rows, else the build stops. 09_Rubrics.json that is not valid JSON is read line by
line (a warning names it). Tool calls per trajectory (Claude Code stream-json):
counted = MCP service calls (main thread and sub-agents) minus blocked calls (tool
result is_error), exact repeats (same tool + same input) and set_acting_user; raw and
harness (Bash, Agent, Read, Task*) counts are kept beside it. A trajectory that is
empty, or has no final "result" event or an error result, is errored. ACL-denied reads
look like "not found" and are not detected — check them by hand.
"""
from __future__ import annotations

import itertools
import json
import re
import statistics
import sys
from pathlib import Path
from fractions import Fraction

ALLOWED_WEIGHTS = {1, 3, 5}
EPS = 1e-9  # band edges are inclusive/exclusive exactly as the rules state; floats must not flip them
TIERS = {"normal": (50, 100), "long-horizon": (100, None)}
V3_POLICY = json.loads((Path(__file__).resolve().parent.parent / "references" / "v3_policy.json").read_text())
DIFFICULTY_CAPS = {mode: Fraction(str(cap)) for mode, cap in V3_POLICY["difficulty_caps"].items()}
BASELINE_RUNS = V3_POLICY["baseline_runs"]
FULL_PASS_FAILURE_COUNT = V3_POLICY["full_pass_failure_count"]
CONTEXT_FIELDS = ("spec_version", "task_type", "difficulty_mode", "difficulty_cap", "freeze_utc",
                  "assignment_hash", "policy_hash", "context_hash")


def _fail(message: str) -> None:
    raise ValueError(message)


def _task_type(value) -> str:
    key = re.sub(r"[\s_]+", "-", str(value or "").strip().lower())
    key = {"normal-horizon": "normal", "long": "long-horizon"}.get(key, key)
    if key not in TIERS:
        _fail(f"task_type must be one of {sorted(TIERS)} (or Normal Horizon / Long Horizon); got {value!r}")
    return key


def validate(data: dict) -> None:
    if data.get("spec_version") not in ("V2", "V3"):
        _fail("spec_version must explicitly be V3 (or V2 for archival compatibility)")
    v3 = data["spec_version"] == "V3"
    if v3:
        mode = str(data.get("difficulty_mode") or "").strip().lower()
        if mode not in DIFFICULTY_CAPS:
            _fail("V3 difficulty_mode must be assigned easy, medium or hard; never infer or switch it")
        data["difficulty_mode"] = mode
        cap = data.get("difficulty_cap")
        if cap is not None and Fraction(str(cap)) != DIFFICULTY_CAPS[mode]:
            _fail(f"difficulty_cap {cap!r} disagrees with assigned mode {mode}")
    data["task_type"] = _task_type(data.get("task_type"))
    rubrics = data.get("rubrics") or []
    if not rubrics:
        _fail("rubrics is empty")
    ids = [r["id"] for r in rubrics]
    if len(ids) != len(set(ids)):
        _fail("duplicate rubric ids")
    for r in rubrics:
        if r.get("weight") not in ALLOWED_WEIGHTS:
            _fail(f"rubric {r['id']}: weight must be 1, 3 or 5 (got {r.get('weight')!r})")
    if all(r.get("valid") is False for r in rubrics):
        _fail("every rubric is marked invalid")
    rollouts = data.get("rollouts") or []
    if not rollouts:
        _fail("rollouts is empty")
    run_ids = [ro.get("id") for ro in rollouts]
    if any(not isinstance(rid, str) or not rid.strip() for rid in run_ids) or len(run_ids) != len(set(run_ids)):
        _fail("rollout ids must be nonempty and unique")
    if v3 and len(rollouts) != BASELINE_RUNS:
        _fail(f"V3 requires exactly {BASELINE_RUNS} rollout slots including errored runs; got {len(rollouts)}")
    for ro in rollouts:
        status = ro.get("status")
        if status not in ("completed", "errored"):
            _fail(f"rollout {ro.get('id')}: status must be completed or errored")
        if status == "completed":
            results = ro.get("results") or {}
            missing = [i for i in ids if i not in results]
            if missing:
                _fail(f"rollout {ro['id']}: no result for rubrics {missing}")
            if type(ro.get("tool_calls")) is not int or ro["tool_calls"] < 0:
                _fail(f"rollout {ro['id']}: tool_calls must be a nonnegative integer")
            if any(type(value) is not bool for value in results.values()):
                _fail(f"rollout {ro['id']}: rubric results must be booleans")
            unknown = [i for i in (ro.get("judge_corrections") or {}) if i not in ids]
            if unknown:
                _fail(f"rollout {ro['id']}: judge_corrections name unknown rubrics {unknown}")
            if any(type(value) is not bool for value in (ro.get("judge_corrections") or {}).values()):
                _fail(f"rollout {ro['id']}: judge_corrections must be booleans")


# ------------------------------------------------------------------ model labels (the one owner: trajectory_ledger, the
# model gate, stage_gate's release check and surface_grader all classify labels here; decision 2026-10-25)
SYNTHETIC_MODEL_LABELS = ("<synthetic>",)          # harness messages, not a model: never checked, counted apart
RX_MODEL_ID = re.compile(r"claude-[a-z]+(?:-[a-z0-9]+)+")


def model_id(label) -> str:
    """The label with only a bracketed suffix stripped: claude-opus-5-5[1m] -> claude-opus-5-5. Nothing else changes
    (V1: strip only a bracketed suffix, then compare exactly; whitespace is part of the label)."""
    return re.sub(r"\[[^\[\]]*\]$", "", str(label or ""))


def classify_model(label, expected: str | None = None) -> str:
    """expected · other · synthetic · unknown. The comparison is exact after model_id(): claude-opus-5 is not
    claude-opus-5-5, and neither is claude-opus-5-5-20261001. A label that is not a model id is unknown."""
    raw = str(label or "")
    if raw in SYNTHETIC_MODEL_LABELS:
        return "synthetic"
    mid = model_id(raw)
    if not RX_MODEL_ID.fullmatch(mid):
        return "unknown"
    return "expected" if mid == model_id(expected or V3_POLICY["model"]) else "other"


def is_opus_55(model: str) -> bool:
    return classify_model(model) == "expected"


def check_models(labels, expected: str | None = None) -> dict:
    """A run's model labels against the expected model: {verdict: VALID | INVALID | UNKNOWN | MISSING, models,
    off_model, unknown, synthetic}. Synthetic labels never decide; an unknown label is never valid."""
    expected = expected or V3_POLICY["model"]
    cls = [(str(m), classify_model(m, expected)) for m in labels or []]
    real = sorted({model_id(m) for m, c in cls if c in ("expected", "other")})
    off = sorted({m for m, c in cls if c == "other"})
    unknown = sorted({m for m, c in cls if c == "unknown"})
    verdict = ("UNKNOWN" if unknown else "INVALID" if off else "VALID" if real else "MISSING")
    return {"verdict": verdict, "expected": expected, "models": real, "off_model": off, "unknown": unknown,
            "synthetic": sum(1 for _, c in cls if c == "synthetic")}


def message_models(events: list) -> list[dict]:
    """Every model label an export carries, with where it came from: the init event, and each assistant message
    (main thread, or the subagent of a brief through parent_tool_use_id)."""
    out = []
    for i, event in enumerate(events if isinstance(events, list) else []):
        if not isinstance(event, dict):
            continue
        # a label is collected whenever the field is present: an explicit "" or null is a label (UNKNOWN), which is
        # different from a message that carries no model field at all (V1)
        if event.get("type") == "system" and event.get("subtype") == "init" and "model" in event:
            out.append({"event": i, "label": str(event["model"]), "source": "init", "parent": None})
        message = event.get("message")
        if event.get("type") == "assistant" and isinstance(message, dict) and "model" in message:
            parent = event.get("parent_tool_use_id")
            out.append({"event": i, "label": str(message["model"]), "source": "subagent" if parent else "main",
                        "parent": parent})
    return out


def model_provenance(events: list, expected: str | None = None) -> dict:
    """Run-level model provenance from every message label. mixed_model and validity are separate outcomes:
      mixed_model     two or more distinct model ids among the messages (synthetic labels excluded)
      valid           VALID / INVALID / UNKNOWN / MISSING against `expected` (default: the V3 policy model)
      v3_valid        True / False / None (UNKNOWN or MISSING) against the V3 policy model
    off_model lists each off-model label with its source (main thread or subagent), count, first and last event and
    the fallback event before it, if any."""
    expected = expected or V3_POLICY["model"]
    msgs = message_models(events)
    falls = [i for i, e in enumerate(events if isinstance(events, list) else []) if isinstance(e, dict)
             and e.get("type") == "system" and e.get("subtype") == "model_refusal_fallback"]
    labels = [m["label"] for m in msgs]
    mine, v3 = check_models(labels, expected), check_models(labels, V3_POLICY["model"])
    groups = {}
    for m in msgs:
        if classify_model(m["label"], expected) != "other":
            continue
        g = groups.setdefault((m["label"], m["source"]), {"label": m["label"], "id": model_id(m["label"]),
                                                         "source": m["source"], "count": 0, "first_event": m["event"],
                                                         "last_event": m["event"], "subagent_briefs": set()})
        g["count"] += 1
        g["last_event"] = m["event"]
        if m["parent"]:
            g["subagent_briefs"].add(m["parent"])
    off = []
    for g in groups.values():
        before = [f for f in falls if f <= g["first_event"]]
        off.append(dict(g, subagent_briefs=len(g["subagent_briefs"]), after_fallback_event=before[-1] if before else None))
    v3_valid = {"VALID": True, "INVALID": False}.get(v3["verdict"])
    if falls or len(mine["models"]) > 1:
        v3_valid = False
    return {"expected_model": expected, "models": mine["models"], "mixed_model": len(mine["models"]) > 1,
            "valid": mine["verdict"], "v3_valid": v3_valid,
            "v3_verdict": v3["verdict"], "off_model": sorted(off, key=lambda x: x["first_event"]),
            "unknown_labels": mine["unknown"], "synthetic_messages": mine["synthetic"], "fallback_events": falls,
            "rule": "labels compared exactly after stripping a bracketed suffix; <synthetic> is a harness message, "
                    "counted apart; an unrecognised label is UNKNOWN, never valid"}


def trajectory_models(path: Path) -> list[str]:
    """Read actual run metadata, including assistant/subagent model identifiers."""
    if not path.stat().st_size:
        return []
    events = json.loads(path.read_text(encoding="utf-8"))
    models = set()
    for event in events if isinstance(events, list) else []:
        if not isinstance(event, dict):
            continue
        # An explicit empty/null label is a label (UNKNOWN), not an absent field. The pre-check gate and the
        # baseline model gate use this reader, so it must agree with message_models/model_provenance.
        if event.get("type") == "system" and event.get("subtype") == "init" and "model" in event:
            models.add(str(event["model"]))
        if event.get("type") == "system" and event.get("subtype") == "model_refusal_fallback" and "fallback_model" in event:
            models.add(str(event["fallback_model"]))
        message = event.get("message")
        if event.get("type") == "assistant" and isinstance(message, dict) and "model" in message:
            models.add(str(message["model"]))
    return sorted(models)


def precheck_provenance(events: list) -> dict:
    """The pre-check gate's provenance decision in one testable place: completed/current check_models is VALID,
    model_provenance is v3-valid, not mixed, and has no fallback events."""
    ev = events if isinstance(events, list) else []
    prov = model_provenance(ev)
    labels = [m["label"] for m in message_models(ev)]
    ok = (check_models(labels)["verdict"] == "VALID" and prov["v3_valid"] is True
          and not prov["mixed_model"] and not prov["fallback_events"])
    return {"ok": ok, "provenance": prov, "models": labels}


def trajectory_provenance(path: Path) -> dict:
    """Run-level provenance from the same events used by the pre-check and baseline gates. A missing/blank label,
    a fallback event or a mixed label set is never accepted as clean Opus 5.5 provenance."""
    if not path.stat().st_size:
        return {"models": [], "mixed_model": False, "v3_valid": None, "fallback_events": [],
                "unknown_labels": [], "valid": "MISSING"}
    events = json.loads(path.read_text(encoding="utf-8"))
    return model_provenance(events if isinstance(events, list) else [])


def model_gate(rollouts: list[dict]) -> dict:
    missing, wrong, unknown, mixed = [], [], [], []
    for ro in rollouts:
        models = ro.get("models") or ([ro["model"]] if "model" in ro else [])
        c = check_models(models if isinstance(models, list) else [])
        if not isinstance(models, list) or c["verdict"] == "MISSING" or not str(ro.get("model_source") or "").strip():
            missing.append(ro["id"])
        elif c["verdict"] == "UNKNOWN":
            unknown.append(f"{ro['id']}: {c['unknown']}")
        elif c["verdict"] == "INVALID":
            wrong.append(f"{ro['id']}: {c['models']}")
        mc = ro.get("model_check")
        if not isinstance(mc, dict):
            if ro["id"] not in missing:
                missing.append(ro["id"])
            continue
        if mc.get("mixed_model") or mc.get("fallback_events") or mc.get("v3_valid") is not True:
            mixed.append(f"{ro['id']}: mixed/fallback provenance"
                         + (f" (fallbacks {mc.get('fallback_events')})" if mc.get("fallback_events") else "")
                         + (f" (models {mc.get('models')})" if mc.get("models") else ""))
    detail = "; ".join((["missing provenance: " + ", ".join(missing)] if missing else [])
                       + (["unrecognised model labels (UNKNOWN, never valid): " + "; ".join(unknown)] if unknown else [])
                       + (["other/mixed models: " + "; ".join(wrong)] if wrong else [])
                       + (["mixed/fallback provenance: " + "; ".join(mixed)] if mixed else []))
    return {"value": detail or f"all {BASELINE_RUNS} rollout slots have {V3_POLICY['model']} provenance",
            "rule": f"{V3_POLICY['model']} for all {BASELINE_RUNS} baseline rollouts; missing model evidence and "
                    "fallback/mixed provenance block",
            "verdict": "FAIL (Model Provenance)" if detail else "PASS"}


def group_patterns(failing: list[dict], ids: list[str]) -> list[list[str]]:
    """Single-linkage grouping: rollouts differing on <= 1 rubric share a pattern."""
    failed_sets = {ro["id"]: {i for i in ids if not ro["results"][i]} for ro in failing}
    names = list(failed_sets)
    parent = {n: n for n in names}

    def find(n: str) -> str:
        while parent[n] != n:
            parent[n] = parent[parent[n]]
            n = parent[n]
        return n

    for i, a in enumerate(names):
        for b in names[i + 1:]:
            if len(failed_sets[a] ^ failed_sets[b]) <= 1:
                parent[find(a)] = find(b)
    groups: dict[str, list[str]] = {}
    for n in names:
        groups.setdefault(find(n), []).append(n)
    return sorted(groups.values(), key=len, reverse=True)


def largest_clique(failing: list[dict], ids: list[str]) -> list[str]:
    """Pairwise reading: the largest set of failing rollouts that all differ on <= 1 rubric."""
    failed_sets = {ro["id"]: {i for i in ids if not ro["results"][i]} for ro in failing}
    names = list(failed_sets)
    for size in range(len(names), 0, -1):
        for combo in itertools.combinations(names, size):
            if all(len(failed_sets[a] ^ failed_sets[b]) <= 1 for a, b in itertools.combinations(combo, 2)):
                return list(combo)
    return []


def _gates(completed: list[dict], errored: list[str], total_runs: int, rubrics: list[dict],
           task_type: str, difficulty_mode: str | None = None) -> dict:
    ids = [r["id"] for r in rubrics]
    weights = {r["id"]: r["weight"] for r in rubrics}
    total_weight = sum(weights.values())
    per_rollout = []
    for ro in completed:
        passed_weight = sum(weights[i] for i in ids if ro["results"][i])
        failed = [i for i in ids if not ro["results"][i]]
        per_rollout.append({
            "id": ro["id"],
            "tool_calls": ro["tool_calls"],
            "weighted_pass_rate": passed_weight / total_weight,
            "unweighted_pass_rate": (len(ids) - len(failed)) / len(ids),
            "failed_rubrics": failed,
            "full_pass": not failed,
        })

    n = len(completed)
    full_passes = [r["id"] for r in per_rollout if r["full_pass"]]
    pass_at_1 = len(full_passes) / n if n else 0.0
    rates = [r["weighted_pass_rate"] for r in per_rollout]
    avg_weighted = sum(rates) / n if n else 0.0
    # Compare exact rational rubric scores so equality fails without rounding or
    # a tolerance that accidentally rejects a score just below the assigned cap.
    exact_average = (sum((Fraction(sum(weights[i] for i in ids if ro["results"][i]), total_weight)
                          for ro in completed), Fraction(0)) / n) if n else Fraction(0)
    sd = statistics.pstdev(rates) if n >= 2 else 0.0
    sd_sample = statistics.stdev(rates) if n >= 2 else 0.0
    sd_unweighted = statistics.pstdev([r["unweighted_pass_rate"] for r in per_rollout]) if n >= 2 else 0.0

    failing = [ro for ro in completed if any(not ro["results"][i] for i in ids)]
    groups = group_patterns(failing, ids)
    failed_sets = {r["id"]: set(r["failed_rubrics"]) for r in per_rollout}
    chained = [[a, b] for g in groups for i, a in enumerate(g) for b in g[i + 1:]
               if len(failed_sets[a] ^ failed_sets[b]) >= 2]
    clique = largest_clique(failing, ids)
    largest_share = (len(groups[0]) / len(failing)) if failing else 0.0
    clique_share = (len(clique) / len(failing)) if failing else 0.0

    all_fail = [i for i in ids if completed and all(not ro["results"][i] for ro in completed)]

    lo, hi = TIERS[task_type]
    if full_passes:
        basis = "golden run(s)"
        counts = [r["tool_calls"] for r in per_rollout if r["full_pass"]]
    else:
        basis = "average of completed rollouts"
        counts = [sum(r["tool_calls"] for r in per_rollout) / n] if n else [0]
    # "If more than one scored 100%, the lowest count among them is used" (Reaching the Tool-Call Minimum,
    # 2026-10): one governing count for both the under-tier and the above-tier test
    horizon_low = horizon_high = min(counts)
    if horizon_low < lo - EPS:
        horizon = "FAIL (Wrong Horizon)"
    elif hi is not None and horizon_high > hi + EPS:
        horizon = "NON-FAIL (Borderline Horizon — above the tier)"
    else:
        horizon = "PASS"

    if not failing:
        patterns = "FAIL (Too Few Signatures)"
    elif len(groups) < 2:
        patterns = "FAIL (Too Few Signatures)"
    elif largest_share > 0.5 + EPS:
        patterns = "FAIL (Signature Over-Concentrated)"
        if clique_share <= 0.5 + EPS:
            patterns += (f" — single-linkage chain; the pairwise reading gives {clique_share:.0%}"
                         " and would pass: confirm on the platform statistics screen")
    else:
        patterns = "PASS"

    def in_band(x: float) -> bool:
        return 0.1 - EPS <= x <= 0.3 + EPS

    sd_verdict = ("PASS" if in_band(sd)
                  else "FAIL (Spread Too Low — deterministic; add friction)" if sd < 0.1
                  else "FAIL (Spread Too High — check rubric ambiguity)")
    alt = [x for x in (sd_sample, sd_unweighted) if in_band(x) != in_band(sd)]
    if alt:
        sd_verdict += " — at the band edge: sample or unweighted SD reads the other way"

    gates = {
        "errored_runs": {
            "value": f"{len(errored)} errored, {n} completed of {total_runs}",
            "rule": "<= 2 errored and >= 4 completed (3+ errored = Fail)",
            "verdict": "PASS" if len(errored) <= 2 and n >= 4 else "FAIL (Too Many Erroneous Runs)",
        },
        "pass_at_1": {
            "value": f"{len(full_passes)}/{n} = {pass_at_1:.0%}",
            "rule": "<= 50% (<= 3 of 6)",
            "verdict": "PASS" if pass_at_1 <= 0.5 + EPS
            else "FAIL (Too Easy" + (" — percentage reading; the count reading '<= 3 runs' would pass" if len(full_passes) <= 3 else "") + ")",
        },
        "avg_weighted_pass_rate": {
            "value": f"{avg_weighted:.1%}",
            "rule": "< 75% (Evals); QC Spec V2 alone < 90%",
            "verdict": "PASS" if avg_weighted < 0.75 - EPS
            else "FAIL (Avg Pass Rate Too High — Evals < 75%; still under the QC Spec V2 90% gate)" if avg_weighted < 0.90 - EPS
            else "FAIL (Avg Pass Rate Too High)",
        },
        "per_rollout_sd": {
            "value": f"{sd:.3f} (sample {sd_sample:.3f}; unweighted {sd_unweighted:.3f})",
            "rule": "0.1-0.3 (population SD of per-rollout weighted pass rates)",
            "verdict": sd_verdict,
        },
        "failure_patterns": {
            "value": (f"{len(groups)} pattern(s); largest {largest_share:.0%} of {len(failing)} failing"
                      f" (pairwise reading {clique_share:.0%})"),
            "rule": ">= 2 patterns (differ on >= 2 rubrics); largest <= 50%",
            "verdict": patterns,
        },
        "horizon": {
            "value": f"{basis}: " + ", ".join(f"{c:.0f}" for c in counts),
            "rule": f"{task_type} tier {lo}-{hi if hi else '500+'}",
            "verdict": horizon,
        },
    }
    if difficulty_mode is not None:
        cap = DIFFICULTY_CAPS[difficulty_mode]
        gates["pass_at_1"] = {
            "value": f"{len(full_passes)}/{total_runs} full passes; {len(full_passes)}/{n} completed = {pass_at_1:.0%}",
            "rule": (f"V3 operational pass@k: fewer than {FULL_PASS_FAILURE_COUNT} full passes out of "
                     f"{BASELINE_RUNS} slots ({FULL_PASS_FAILURE_COUNT}+ fails)"),
            "verdict": "PASS" if len(full_passes) < FULL_PASS_FAILURE_COUNT else "FAIL (Too Easy)",
        }
        gates["avg_weighted_pass_rate"] = {
            "value": f"{avg_weighted:.1%} ({n} completed; {len(errored)} errored excluded)",
            "rule": f"V3 {difficulty_mode}: strictly < {float(cap):.0%}; equality fails",
            "verdict": "PASS" if exact_average < cap else "FAIL (Avg Pass Rate Too High)",
        }
    return {
        "rubrics": ids,
        "per_rollout": per_rollout,
        "golden_runs": full_passes,
        "all_fail_rubrics": all_fail,
        "patterns": groups,
        "pairwise_largest_pattern": clique,
        "chained_pattern_merges": chained,
        "gates": gates,
    }


def compute(data: dict) -> dict:
    validate(data)
    rubrics = data["rubrics"]
    completed = [ro for ro in data["rollouts"] if ro["status"] == "completed"]
    errored = [ro["id"] for ro in data["rollouts"] if ro["status"] == "errored"]
    total = len(data["rollouts"])
    v3 = data["spec_version"] == "V3"
    mode = data["difficulty_mode"] if v3 else None
    platform = _gates(completed, errored, total, rubrics, data["task_type"], mode)

    invalid = [r["id"] for r in rubrics if r.get("valid") is False]
    corrections = {ro["id"]: ro["judge_corrections"] for ro in completed if ro.get("judge_corrections")}
    views = {"platform": platform}
    if invalid or corrections:
        valid_rubrics = [r for r in rubrics if r.get("valid") is not False]
        corrected = [dict(ro, results={**ro["results"], **corrections.get(ro["id"], {})}) for ro in completed]
        views["valid"] = _gates(corrected, errored, total, valid_rubrics, data["task_type"], mode)
    if v3:
        for view in views.values():
            view["gates"]["baseline_models"] = model_gate(data["rollouts"])
    record = views.get("valid", platform)

    blocking = []
    for name in platform["gates"]:
        verdict_views = {"valid": record} if v3 and "valid" in views else views
        failed_in = [v for v, res in verdict_views.items() if res["gates"][name]["verdict"].startswith("FAIL")]
        if failed_in:
            blocking.append(name if len(views) == 1 else f"{name} ({' + '.join(failed_in)} view)")
    return {
        "spec_version": data["spec_version"],
        "difficulty_mode": mode,
        "context": data.get("context"),
        "verdict_view": "valid" if "valid" in views else "platform",
        "denominators": {"rollout_slots": total, "completed_scores": len(completed),
                         "errored_excluded": len(errored), "full_pass_gate": total if v3 else len(completed)},
        "completed": len(completed),
        "errored": errored,
        "invalid_rubrics": invalid,
        "judge_corrections": corrections,
        "views": views,
        # Top-level keys mirror the view of record (valid view when it exists).
        "per_rollout": record["per_rollout"],
        "golden_runs": record["golden_runs"],
        "all_fail_rubrics": platform["all_fail_rubrics"],
        "patterns": record["patterns"],
        "chained_pattern_merges": record["chained_pattern_merges"],
        "gates": record["gates"],
        "blocking": blocking,
    }


def to_markdown(result: dict, data: dict | None = None) -> str:
    views = result["views"]
    detail = {ro["id"]: ro.get("tool_call_detail") for ro in (data or {}).get("rollouts", [])}
    platform = views["platform"]
    valid = views.get("valid")
    head = "| Rollout | Counted tool calls | Raw / harness / blocked / repeats | Weighted pass (platform) |"
    sep = "|---|---|---|---|"
    if valid:
        head += " Weighted pass (valid view) |"
        sep += "---|"
    lines = []
    if result["spec_version"] == "V3":
        lines += [f"V3 difficulty mode: {result['difficulty_mode']} · verdict view: {result['verdict_view']}",
                  f"Denominators: {result['denominators']['rollout_slots']} rollout slots; {result['completed']} completed score(s); "
                  f"{len(result['errored'])} errored excluded from averages (never zero-scored)."]
        context = result.get("context") or {}
        if context:
            lines += ["Assignment context: " + " · ".join(f"{key}={context[key]}" for key in
                      ("assignment_hash", "policy_hash", "context_hash", "freeze_utc") if key in context)]
        lines += [""]
    lines += [head + " Failed rubrics (platform) |", sep + "---|"]
    vrates = {r["id"]: r["weighted_pass_rate"] for r in (valid or platform)["per_rollout"]}
    for r in platform["per_rollout"]:
        d = detail.get(r["id"]) or {}
        raw = (f"{d.get('raw', '—')} / {d.get('harness', '—')} / {d.get('blocked', '—')} / {d.get('repeats', '—')}"
               if d else "—")
        failed = ", ".join(r["failed_rubrics"]) or "— (golden run)"
        row = f"| {r['id']} | {r['tool_calls']} | {raw} | {r['weighted_pass_rate']:.1%} |"
        if valid:
            row += f" {vrates[r['id']]:.1%} |"
        lines.append(row + f" {failed} |")
    for e in result["errored"]:
        lines.append(f"| {e} | — | — | errored (excluded) |" + (" — |" if valid else "") + " — |")

    if valid:
        lines += ["", f"Valid view excludes invalid rubrics {', '.join(result['invalid_rubrics']) or 'none'}"
                  f" and applies judge corrections {json.dumps(result['judge_corrections']) if result['judge_corrections'] else 'none'}.",
                  ("V3 verdict uses corrected fair results; platform results above remain audit evidence."
                   if result["spec_version"] == "V3" else "Legacy V2: a failure in either view blocks."),
                  "", "| Gate | Platform view | Valid view | Rule | Verdict (platform / valid) |", "|---|---|---|---|---|"]
        for name, g in platform["gates"].items():
            v = valid["gates"][name]
            lines.append(f"| {name} | {g['value']} | {v['value']} | {g['rule']} | {g['verdict']} / {v['verdict']} |")
    else:
        lines += ["", "| Gate | Value | Rule | Verdict |", "|---|---|---|---|"]
        for name, g in platform["gates"].items():
            lines.append(f"| {name} | {g['value']} | {g['rule']} | {g['verdict']} |")

    rec = valid or platform
    lines += ["", "Failure patterns (single-linkage, same pattern if they differ on <= 1 rubric"
              + ("; valid view" if valid else "") + "):"]
    for i, g in enumerate(rec["patterns"], 1):
        lines.append(f"- Pattern {i}: {', '.join(g)}")
    lines.append(f"- Pairwise reading (largest set all within 1 rubric of each other): {', '.join(rec['pairwise_largest_pattern']) or 'none'}")
    if rec["chained_pattern_merges"]:
        pairs = "; ".join(" vs ".join(p) for p in rec["chained_pattern_merges"])
        lines.append(f"- Note: chained merge — these pairs differ on >= 2 rubrics but were joined through an intermediate rollout: {pairs}.")
    lines.append(f"All-fail rubrics (completed rollouts, platform view): {', '.join(result['all_fail_rubrics']) or 'none'}")
    lines.append(f"Blocking gates: {', '.join(result['blocking']) or 'none'}")
    return "\n".join(lines)


# --------------------------------------------------------------------------- build

_LINK = re.compile(r"\[([^\]]+)\]\((?:https?://|mailto:)[^)]*\)")
_HEADER = re.compile(r"^(\d+)\s*/\s*(\d+)\s+criteria passed\s*$", re.I)
_DECISIONS = {"pass": True, "passed": True, "fail": False, "failed": False}


def norm_title(text: str) -> str:
    text = _LINK.sub(r"\1", text.replace('\\"', '"'))
    text = text.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'", " ": " "}))
    return re.sub(r"\s+", " ", text).strip()


def parse_rubrics(path: Path) -> tuple[list[dict], list[str]]:
    text = path.read_text(encoding="utf-8")
    warnings = []
    try:
        items = json.loads(text)
        if isinstance(items, dict):
            items = items.get("rubrics") or items.get("criteria") or []
        rubrics = [{"title": it["title"], "weight": it.get("weight"), "category": it.get("category")} for it in items]
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        warnings.append(f"{path.name} is not valid JSON ({error}); read line by line — re-export it from the builder")
        rubrics, current = [], None
        for line in text.splitlines():
            m = re.match(r'\s*"title":\s*"(.*)",?\s*$', line)
            if m:
                current = {"title": m.group(1), "weight": None, "category": None}
                rubrics.append(current)
                continue
            m = re.match(r'\s*"category":\s*"(.*?)"', line)
            if m and current is not None:
                current["category"] = m.group(1)
            m = re.match(r'\s*"weight":\s*(\d+)', line)
            if m and current is not None:
                current["weight"] = int(m.group(1))
    if not rubrics:
        _fail(f"{path}: no criteria found")
    for i, r in enumerate(rubrics, 1):
        r["id"] = f"R{i}"
        if r["weight"] not in ALLOWED_WEIGHTS:
            _fail(f"{path}: criterion {i} has weight {r['weight']!r} (must be 1, 3 or 5)")
    return rubrics, warnings


def parse_verifier(path: Path) -> dict[int, list[dict]]:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    if not text.strip():
        _fail(f"{path}: verifier results are empty or missing — the verifier has not run or the export is "
              "missing. Stop and ask for it; empty results are not errored rollouts")
    runs: dict[int, dict] = {}
    current = None
    for raw in text.splitlines():
        line = raw.rstrip()
        m = re.match(r"^Run\s*#\s*(\d+)\s*$", line.strip())
        if m:
            if int(m.group(1)) in runs:
                _fail(f"{path}: Run #{m.group(1)} appears twice — paste each run's block once")
            current = {"header": None, "rows": []}
            runs[int(m.group(1))] = current
            continue
        if current is None:
            continue
        m = _HEADER.match(line.strip())
        if m and current["header"] is None:
            current["header"] = (int(m.group(1)), int(m.group(2)))
            continue
        if "\t" in line:
            parts = line.split("\t")
            if parts[0].strip().lower() == "rubric":
                continue
            decision = parts[1].strip().lower() if len(parts) > 1 else ""
            if decision not in _DECISIONS:
                _fail(f"{path}: run {len(runs)} row has decision {parts[1] if len(parts) > 1 else ''!r} (expected Pass/Fail): {parts[0][:80]}")
            current["rows"].append({"title": parts[0], "passed": _DECISIONS[decision],
                                    "justification": "\t".join(parts[2:])})
        elif current["rows"] and line.strip() and not re.match(r"^\d+\s*/\s*\d+\s+passed$", line.strip()):
            current["rows"][-1]["justification"] += "\n" + line  # wrapped justification
    if not runs:
        _fail(f"{path}: no 'Run #N' blocks — the file holds a template or notes, not verifier output. "
              "Stop and ask for it; missing results are not errored rollouts")
    for n, run in runs.items():
        if run["header"] and run["rows"]:
            passed = sum(r["passed"] for r in run["rows"])
            if run["header"] != (passed, len(run["rows"])):
                _fail(f"{path}: Run #{n} header says {run['header'][0]}/{run['header'][1]} but parsed "
                      f"{passed}/{len(run['rows'])} rows — the copy is incomplete or wrapped; re-copy it")
    return {n: run["rows"] for n, run in runs.items()}


def _run_number(path: Path) -> int | None:
    m = re.search(r"run[\s_-]*(\d+)", path.name, re.I) or re.match(r"(\d+)[_\s-]", path.name)
    return int(m.group(1)) if m else None


def count_tool_calls(events: list) -> dict:
    uses, results = [], {}
    for e in events:
        content = (e.get("message") or {}).get("content") if isinstance(e, dict) else None
        if not isinstance(content, list):
            continue
        for b in content:
            if not isinstance(b, dict):
                continue
            if e.get("type") == "assistant" and b.get("type") == "tool_use":
                uses.append(b)
            elif e.get("type") == "user" and b.get("type") == "tool_result":
                results[b.get("tool_use_id")] = str(b.get("is_error")).lower() == "true"
    service = [u for u in uses if str(u.get("name", "")).startswith("mcp__")]
    acting = [u for u in service if str(u["name"]).endswith("set_acting_user")]
    blocked = [u for u in service if results.get(u.get("id")) and u not in acting]
    seen, repeats = set(), 0
    for u in service:
        if u in acting or u in blocked:
            continue
        key = (u["name"], json.dumps(u.get("input"), sort_keys=True))
        if key in seen:
            repeats += 1
        seen.add(key)
    counted = len(service) - len(acting) - len(blocked) - repeats
    return {"raw": len(uses), "service": len(service), "harness": len(uses) - len(service),
            "blocked": len(blocked), "repeats": repeats, "set_acting_user": len(acting), "counted": counted}


def read_trajectory(path: Path) -> tuple[str, str, dict | None]:
    if path.stat().st_size == 0:
        return "errored", "empty trajectory file", None
    try:
        events = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        _fail(f"{path}: not valid JSON ({error}) — re-download it; a truncated export is not an errored run")
    if not isinstance(events, list) or not events:
        return "errored", "no events", None
    last = events[-1] if isinstance(events[-1], dict) else {}
    detail = count_tool_calls(events)
    if last.get("type") != "result":
        return "errored", "no final result event", detail
    if str(last.get("is_error")).lower() == "true" or last.get("subtype") not in (None, "success"):
        return "errored", f"result {last.get('subtype')} (is_error={last.get('is_error')})", detail
    return "completed", "", detail


def build(verifier: Path, rubrics_path: Path, trajectories: Path, task_type: str,
          invalid: list[str] | None = None, corrections: list[str] | None = None,
          *, context: dict | None = None, spec_version: str = "V3") -> tuple[dict, list[str]]:
    if spec_version == "V3" and context is None:
        _fail("V3 build requires the normalized task context (CLI: --task-dir <task folder>)")
    rubrics, warnings = parse_rubrics(rubrics_path)
    runs = parse_verifier(verifier)
    by_title: dict[str, list[str]] = {}
    for r in rubrics:
        by_title.setdefault(norm_title(r["title"]), []).append(r["id"])

    files = {}
    for p in sorted(trajectories.glob("*.json")):
        n = _run_number(p)
        if n is None:
            _fail(f"{p.name}: cannot read a run number from the file name")
        if n in files:
            _fail(f"two trajectory files for run {n}: {files[n].name}, {p.name}")
        files[n] = p
    if not files:
        _fail(f"{trajectories}: no trajectory JSON files")
    if spec_version == "V3" and set(files) != set(range(1, BASELINE_RUNS + 1)):
        _fail(f"V3 needs trajectory slots run-1 through run-{BASELINE_RUNS} including errored exports; got {sorted(files)}")
    missing = sorted(set(runs) - set(files))
    if missing:
        _fail(f"verifier graded runs {missing} but no trajectory file exists for them")

    rollouts = []
    for n in sorted(files):
        status, reason, detail = read_trajectory(files[n])
        rows = runs.get(n) or []
        rid = f"run-{n}"
        provenance = ({"models": trajectory_models(files[n]), "model_source": f"trajectory:{files[n].name}",
                       "model_check": trajectory_provenance(files[n])}
                      if spec_version == "V3" else {})
        if status == "errored":
            if rows:
                _fail(f"{rid}: trajectory is errored ({reason}) but the verifier graded it — confirm the "
                      "platform record (re-download the trajectory) before computing")
            rollouts.append({"id": rid, "status": "errored", "reason": reason, "file": files[n].name, **provenance})
            continue
        if not rows:
            _fail(f"{rid}: completed trajectory but no verifier rows — the verifier copy is incomplete")
        results, unbound, used = {}, [], {}
        for row in rows:
            ids = by_title.get(norm_title(row["title"]), [])
            k = used.get(norm_title(row["title"]), 0)
            if k >= len(ids):
                unbound.append(row["title"][:100])
                continue
            used[norm_title(row["title"])] = k + 1
            results[ids[k]] = row["passed"]
        absent = [r["id"] for r in rubrics if r["id"] not in results]
        if unbound or absent:
            _fail(f"{rid}: verifier rows do not bind to 09_Rubrics.json — unbound rows {unbound}; "
                  f"criteria without a row {absent}. The verifier ran on a different rubric version or "
                  "the copy is damaged; never bind by guesswork")
        rollouts.append({"id": rid, "status": "completed", "tool_calls": detail["counted"],
                         "tool_call_detail": detail, "results": results, "file": files[n].name, **provenance})

    ids = {r["id"] for r in rubrics}
    for rid in invalid or []:
        if rid not in ids:
            _fail(f"--invalid names unknown rubric {rid}")
    out_rubrics = [{"id": r["id"], "weight": r["weight"], "category": r["category"], "title": r["title"],
                    **({"valid": False} if r["id"] in (invalid or []) else {})} for r in rubrics]
    by_run = {ro["id"]: ro for ro in rollouts}
    for item in corrections or []:
        run, _, rub = item.partition(":")
        if run not in by_run or by_run[run]["status"] != "completed" or rub not in ids:
            _fail(f"--judge-correction {item!r}: expected <completed run id>:<rubric id>")
        by_run[run].setdefault("judge_corrections", {})[rub] = True
    data = {"spec_version": spec_version, "task_type": _task_type(task_type), "rubrics": out_rubrics, "rollouts": rollouts}
    if context is not None:
        bind_context(data, context, require_existing=False)
    validate(data)
    return data, warnings


def bind_context(data: dict, context: dict, *, require_existing: bool = True) -> None:
    """Bind new matrices, and refuse to reinterpret stale matrices after an assignment change."""
    expected = {key: context[key] for key in CONTEXT_FIELDS if key in context}
    expected["spec_version"] = "V3"
    expected["task_type"] = _task_type(context["task_type"])
    if require_existing:
        recorded = data.get("context") or {}
        for key in ("assignment_hash", "policy_hash", "context_hash"):
            if not expected.get(key) or recorded.get(key) != expected[key]:
                _fail(f"difficulty matrix has missing/stale {key}; rebuild it for the current assignment and policy")
    for key in ("spec_version", "task_type", "difficulty_mode", "difficulty_cap"):
        actual, wanted = data.get(key), expected.get(key)
        if actual is not None and actual != wanted:
            _fail(f"difficulty matrix {key} {actual!r} disagrees with current assignment {wanted!r}")
        if wanted is not None:
            data[key] = wanted
    data["context"] = expected


def infer_task_dir(*paths: Path) -> Path:
    candidates = []
    for path in paths:
        current = path if path.is_dir() else path.parent
        for candidate in (current, *current.parents):
            if (candidate / "00_Assigments.md").is_file():
                candidates.append(candidate.resolve())
                break
    roots = set(candidates)
    if len(roots) != 1:
        _fail("cannot infer one task folder from input paths; supply --task-dir <task folder>")
    return roots.pop()


# --------------------------------------------------------------------------- self-test

def _self_test() -> None:
    # These archival regression cases intentionally exercise the old V2 policy.
    calculate = globals()["compute"]

    def compute(data):
        return calculate(dict(data, spec_version="V2"))

    rubrics = [{"id": f"C{i}", "weight": 3} for i in range(1, 9)]

    def run(rid: str, failed: set[str], calls: int = 80) -> dict:
        return {"id": rid, "status": "completed", "tool_calls": calls,
                "results": {r["id"]: r["id"] not in failed for r in rubrics}}

    # QC Spec V2 example 1: {2,4,6} x3 and {4,6,8} x3 -> two patterns, 50% each -> PASS
    ex1 = {"task_type": "normal", "rubrics": rubrics, "rollouts": [
        run("R1", {"C2", "C4", "C6"}), run("R2", {"C4", "C6", "C8"}), run("R3", {"C2", "C4", "C6"}),
        run("R4", {"C4", "C6", "C8"}), run("R5", {"C4", "C6", "C8"}), run("R6", {"C2", "C4", "C6"})]}
    r1 = compute(ex1)
    assert len(r1["patterns"]) == 2, r1["patterns"]
    assert r1["gates"]["failure_patterns"]["verdict"] == "PASS"
    assert list(r1["views"]) == ["platform"]

    # QC Spec V2 example 2: {2,4,6} and {4,6} differ on one rubric -> one pattern -> FAIL
    ex2 = {"task_type": "normal", "rubrics": rubrics, "rollouts": [
        run("R1", {"C2", "C4", "C6"}), run("R2", {"C4", "C6"}), run("R3", {"C2", "C4", "C6"}),
        run("R4", {"C4", "C6"}), run("R5", {"C4", "C6"}), run("R6", {"C2", "C4", "C6"})]}
    assert compute(ex2)["gates"]["failure_patterns"]["verdict"].startswith("FAIL (Too Few")

    # 4 of 6 full passes -> Too Easy; golden runs set the horizon basis
    ex3 = {"task_type": "long-horizon", "rubrics": rubrics, "rollouts": [
        run("R1", set(), 130), run("R2", set(), 120), run("R3", set(), 110), run("R4", set(), 140),
        run("R5", {"C1", "C2"}, 60), {"id": "R6", "status": "errored"}]}
    r3 = compute(ex3)
    assert r3["gates"]["pass_at_1"]["verdict"].startswith("FAIL (Too Easy)")
    assert r3["gates"]["horizon"]["verdict"] == "PASS"
    assert r3["completed"] == 5 and r3["errored"] == ["R6"]

    # Normal task averaging 120 calls -> Borderline Horizon (non-fail)
    ex4 = {"task_type": "Normal Horizon", "rubrics": rubrics, "rollouts": [
        run(f"R{i}", {"C1", f"C{i + 1}"} if i % 2 else {"C3", "C4", "C5"}, 120) for i in range(1, 7)]}
    assert compute(ex4)["gates"]["horizon"]["verdict"].startswith("NON-FAIL")

    # Identical scores -> SD 0 -> deterministic; mixed scores -> SD inside the band
    assert compute(ex1)["gates"]["per_rollout_sd"]["verdict"].startswith("FAIL (Spread Too Low")
    ex5 = {"task_type": "Long Horizon", "rubrics": rubrics, "rollouts": [
        run("R1", set(), 300), run("R2", {"C1", "C2", "C3", "C4"}, 400), run("R3", {"C5", "C6"}, 350),
        run("R4", {"C1", "C2", "C7", "C8", "C3"}, 500), run("R5", {"C6", "C7"}, 420), run("R6", {"C2", "C3", "C4"}, 380)]}
    r5 = compute(ex5)
    assert r5["gates"]["per_rollout_sd"]["verdict"] == "PASS", r5["gates"]["per_rollout_sd"]
    assert r5["gates"]["avg_weighted_pass_rate"]["verdict"] == "PASS", r5["gates"]["avg_weighted_pass_rate"]

    # Chained shape: single-linkage chains 4 of 6 (FAIL); pairwise reading 50%
    ex6 = {"task_type": "long-horizon", "rubrics": rubrics, "rollouts": [
        run("R1", {"C1", "C2", "C3", "C8"}), run("R2", {"C1", "C2", "C8"}, 90),
        run("R3", {"C1", "C2", "C3", "C8", "C4"}), run("R4", {"C1", "C2", "C3"}),
        run("R5", {"C1", "C2", "C3", "C5", "C6", "C7", "C8"}), run("R6", {"C1", "C2", "C3", "C8", "C4"})]}
    r6 = compute(ex6)
    fp = r6["gates"]["failure_patterns"]["verdict"]
    assert fp.startswith("FAIL (Signature Over-Concentrated") and "pairwise reading gives 50%" in fp, fp
    assert r6["chained_pattern_merges"]

    # Invalid all-fail rubrics: excluded in the valid view; a gate failing only there still blocks
    ex7 = {"task_type": "normal", "rubrics": [dict(r, valid=(r["id"] not in ("C7", "C8"))) for r in rubrics],
           "rollouts": [run(f"R{i}", {"C7", "C8"} | ({f"C{i}"} if i <= 2 else set()), 70) for i in range(1, 7)]}
    r7 = compute(ex7)
    assert r7["views"]["platform"]["gates"]["pass_at_1"]["verdict"] == "PASS"
    assert r7["views"]["valid"]["gates"]["pass_at_1"]["verdict"].startswith("FAIL (Too Easy)")
    assert "pass_at_1 (valid view)" in r7["blocking"], r7["blocking"]
    assert r7["all_fail_rubrics"] == ["C7", "C8"] and r7["invalid_rubrics"] == ["C7", "C8"]

    # Judge correction flips one result in the valid view only
    ex8 = json.loads(json.dumps(ex5))
    ex8["rollouts"][2]["judge_corrections"] = {"C5": True}
    r8 = compute(ex8)
    assert r8["views"]["platform"]["per_rollout"][2]["failed_rubrics"] == ["C5", "C6"]
    assert r8["views"]["valid"]["per_rollout"][2]["failed_rubrics"] == ["C6"]

    # ---- rule edges (QC Spec V2 rows, Evals scoring.json, taxonomy screens 59-61) ----
    def gate(data, name, view="platform"):
        return compute(data)["views"][view]["gates"][name]["verdict"]

    def six(failed_sets, calls=80, tt="normal"):
        return {"task_type": tt, "rubrics": rubrics,
                "rollouts": [run(f"X{i}", f, calls) for i, f in enumerate(failed_sets, 1)]}

    # Patterns: rubric results differing on exactly 2 -> different; on 1 or 0 -> same
    assert len(compute(six([{"C1"}, {"C2"}, {"C1"}, {"C2"}, {"C3", "C4"}, {"C5", "C6"}]))["patterns"]) == 4
    assert len(compute(six([{"C1"}, {"C1", "C2"}, {"C1"}, {"C1", "C2"}, {"C1"}, {"C1"}]))["patterns"]) == 1
    # Largest pattern exactly 50% passes; 4 of 6 fails; one failing rollout = one pattern
    assert gate(six([{"C1"}] * 3 + [{"C5", "C6"}, {"C7", "C8"}, {"C2", "C3"}]), "failure_patterns") == "PASS"
    assert gate(six([{"C1"}] * 4 + [{"C5", "C6"}, {"C7", "C8"}]), "failure_patterns").startswith(
        "FAIL (Signature Over-Concentrated")
    assert gate(six([set()] * 5 + [{"C1"}]), "failure_patterns").startswith("FAIL (Too Few")
    # pass@1: 3 of 6 golden passes, 4 of 6 fails; 3 of 5 completed fails on the percentage reading
    assert gate(six([set()] * 3 + [{"C1"}, {"C2", "C3"}, {"C4", "C5"}]), "pass_at_1") == "PASS"
    assert gate(six([set()] * 4 + [{"C1"}, {"C2", "C3"}]), "pass_at_1").startswith("FAIL (Too Easy")
    five = six([set()] * 3 + [{"C1"}, {"C2", "C3"}])
    five["rollouts"].append({"id": "X6", "status": "errored"})
    assert "count reading" in gate(five, "pass_at_1")
    # Errored runs: 2 of 6 passes, 3 of 6 fails; the AF denominator ignores errored runs
    e2 = six([{"C1"}, {"C1", "C2"}, {"C1", "C3"}, {"C1", "C4"}])
    e2["rollouts"] += [{"id": "X5", "status": "errored"}, {"id": "X6", "status": "errored"}]
    assert gate(e2, "errored_runs") == "PASS" and compute(e2)["all_fail_rubrics"] == ["C1"]
    e3 = json.loads(json.dumps(e2))
    e3["rollouts"][3] = {"id": "X4", "status": "errored"}
    assert gate(e3, "errored_runs").startswith("FAIL (Too Many")
    # A rubric passed by one completed run is not all-fail
    assert compute(six([{"C1"}, {"C1"}, {"C1"}, {"C1"}, {"C1"}, {"C2"}]))["all_fail_rubrics"] == []
    # Average: exactly 75% fails (Evals < 75%); 87.5% fails Evals but notes the QC 90% gate; >= 90% fails
    avg75 = six([{"C1", "C2"}] * 6)                       # 6/8 = 75.0% every run
    assert gate(avg75, "avg_weighted_pass_rate").startswith("FAIL (Avg Pass Rate Too High — Evals")
    assert "QC Spec V2 90%" in gate(six([{"C1"}] * 6), "avg_weighted_pass_rate")
    w = {"task_type": "normal", "rubrics": [{"id": "A", "weight": 1}] + [{"id": f"B{i}", "weight": 3} for i in range(3)],
         "rollouts": [{"id": f"Y{i}", "status": "completed", "tool_calls": 70,
                       "results": {"A": False, "B0": True, "B1": True, "B2": True}} for i in range(6)]}
    assert compute(w)["gates"]["avg_weighted_pass_rate"]["value"] == "90.0%"   # weights, not counts
    assert gate(w, "avg_weighted_pass_rate") == "FAIL (Avg Pass Rate Too High)"
    # SD band edges are inclusive: exactly 0.1 and exactly 0.3 pass (floating point must not flip them)
    rub10 = [{"id": f"D{i}", "weight": 1} for i in range(10)]

    def sd_case(passes):
        return {"task_type": "normal", "rubrics": rub10, "rollouts": [
            {"id": f"Z{k}", "status": "completed", "tool_calls": 70,
             "results": {f"D{i}": i < p for i in range(10)}} for k, p in enumerate(passes)]}
    assert compute(sd_case([4, 6] * 3))["gates"]["per_rollout_sd"]["value"].startswith("0.100")
    assert gate(sd_case([4, 6] * 3), "per_rollout_sd").startswith("PASS")
    assert gate(sd_case([2, 8] * 3), "per_rollout_sd").startswith("PASS")          # SD 0.300
    assert gate(sd_case([1, 9] * 3), "per_rollout_sd").startswith("FAIL (Spread Too High")
    # Horizon: normal 50 and 100 pass, 49 fails, 101 is Borderline; long-horizon 99 fails, 600 passes
    for calls, tt, want in ((50, "normal", "PASS"), (100, "normal", "PASS"), (49, "normal", "FAIL (Wrong"),
                            (101, "normal", "NON-FAIL"), (99, "long-horizon", "FAIL (Wrong"),
                            (600, "long-horizon", "PASS")):
        assert gate(six([{"C1"}, {"C2", "C3"}] * 3, calls, tt), "horizon").startswith(want), (calls, tt)
    # Golden basis: the golden run's count governs, not the average; any golden run under the tier fails
    g = six([set(), {"C1"}, {"C2", "C3"}, {"C4", "C5"}, {"C6", "C7"}, {"C8", "C1"}], 300, "long-horizon")
    g["rollouts"][0]["tool_calls"] = 90
    assert gate(g, "horizon").startswith("FAIL (Wrong") and "golden" in compute(g)["gates"]["horizon"]["value"]
    # Two golden runs at 80 and 110 on a normal task: the lowest (80) governs both bounds -> PASS, not Borderline
    g2 = six([set(), set(), {"C2", "C3"}, {"C4", "C5"}, {"C6", "C7"}, {"C8", "C1"}], 70, "normal")
    g2["rollouts"][0]["tool_calls"], g2["rollouts"][1]["tool_calls"] = 80, 110
    assert gate(g2, "horizon").startswith("PASS"), compute(g2)["gates"]["horizon"]
    # Weights other than 1/3/5, unknown judge-correction rubric, all rubrics invalid: rejected
    for broken in ({"rubrics": [{"id": "C1", "weight": 2}]},
                   {"rollouts": [dict(run("R1", set()), judge_corrections={"Q9": True})]},
                   {"rubrics": [dict(r, valid=False) for r in rubrics]}):
        try:
            compute({**six([{"C1"}] * 6), **broken})
        except ValueError:
            pass
        else:
            raise AssertionError(f"should reject {broken}")

    # --build: platform exports -> input JSON (a unique folder under the scratch root, even outside a sandbox)
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("difficulty_stats_selftest_") as tmp:
        d = Path(tmp)
        (d / "rubrics.json").write_text(            # unescaped inner quotes: not valid JSON
            '[\n {\n  "title": "The Agent reports the "Draft" state of TASK-1.",\n  "category": "outcome",\n'
            '  "weight": 3\n },\n {\n  "title": "The Agent attaches notes.zip to the update.",\n'
            '  "category": "outcome",\n  "weight": 1\n },\n {\n  "title": "The Agent closes TASK-2.",\n'
            '  "category": "outcome",\n  "weight": 5\n }\n]\n')
        verifier = ("Run #1\n2/3 criteria passed\nRubrics grading results\n2/3 passed\nOutcome\n2/3 passed\n"
                    "Rubric\tDecision\tJustification\n"
                    "The Agent reports the “Draft” state of TASK-1.\tPass\tok\n"
                    "The Agent attaches [notes.zip](http://notes.zip) to the update.\tFail\tmissing\n"
                    "continued justification line\n"
                    "The Agent closes TASK-2.\tPass\tok\n\n"
                    "Run #3\n1/3 criteria passed\nRubrics grading results\n1/3 passed\nOutcome\n1/3 passed\n"
                    "Rubric\tDecision\tJustification\n"
                    "The Agent closes TASK-2.\tPass\tok\n"
                    'The Agent reports the \\"Draft\\" state of TASK-1.\tFail\tno\n'
                    "The Agent attaches notes.zip  to the update.\tFail\tno\n")
        (d / "verifier.txt").write_text(verifier)
        traj = d / "trajs"
        traj.mkdir()

        def use(i, name, inp, parent=None):
            return {"type": "assistant", "parent_tool_use_id": parent,
                    "message": {"content": [{"type": "tool_use", "id": f"t{i}", "name": name, "input": inp}]}}

        def res(i, err=False):
            return {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": f"t{i}", "is_error": err}]}}

        done = {"type": "result", "subtype": "success", "is_error": "False", "result": "done"}
        events = [{"type": "system", "subtype": "init"},
                  use(1, "mcp__hg__linear_get_issue", {"id": "TASK-1"}), res(1),
                  use(2, "mcp__hg__linear_get_issue", {"id": "TASK-1"}), res(2),           # exact repeat
                  use(3, "mcp__hg__github_search_code", {"q": "x"}), res(3, "True"),       # blocked
                  use(4, "Bash", {"command": "ls"}), res(4),                                # harness
                  use(5, "mcp__hg__set_acting_user", {"u": 1}), res(5),                     # configuration
                  use(6, "mcp__hg__slack_read_channel", {"c": "a"}, parent="t9"), res(6),   # sub-agent call
                  done]
        (traj / "trajectory-run-1 (1).json").write_text(json.dumps(events))     # duplicate-download name
        (traj / "trajectory-run-2.json").write_text("")                          # errored: empty file
        (traj / "run3.json").write_text(json.dumps(events[:3] + [done]))
        (traj / "README.md").write_text("not a trajectory")
        data, warnings = build(d / "verifier.txt", d / "rubrics.json", traj, "Long Horizon",
                               invalid=["R2"], corrections=["run-3:R1"], spec_version="V2")
        assert warnings and "not valid JSON" in warnings[0]
        by = {ro["id"]: ro for ro in data["rollouts"]}
        assert by["run-2"]["status"] == "errored" and by["run-2"]["reason"] == "empty trajectory file"
        assert by["run-1"]["results"] == {"R1": True, "R2": False, "R3": True}
        assert by["run-3"]["results"] == {"R1": False, "R2": False, "R3": True}
        det = by["run-1"]["tool_call_detail"]
        assert (det["raw"], det["harness"], det["blocked"], det["repeats"], det["set_acting_user"], det["counted"]) == \
            (6, 1, 1, 1, 1, 2), det
        assert by["run-1"]["tool_calls"] == 2 and by["run-3"]["tool_calls"] == 1
        assert data["rubrics"][1]["valid"] is False and by["run-3"]["judge_corrections"] == {"R1": True}
        r9 = compute(data)
        assert r9["errored"] == ["run-2"] and r9["views"]["valid"]["per_rollout"][1]["full_pass"]
        assert r9["views"]["platform"]["per_rollout"][1]["failed_rubrics"] == ["R1", "R2"]   # raw preserved
        assert "Valid view excludes invalid rubrics R2" in to_markdown(r9, data)

        # Error results and missing result events make a trajectory errored
        for name, evs, reason in (("e1", events[:3] + [dict(done, subtype="error_max_turns")], "error_max_turns"),
                                  ("e2", events[:3], "no final result event")):
            p = d / f"{name}.json"
            p.write_text(json.dumps(evs))
            assert read_trajectory(p)[0] == "errored" and reason in read_trajectory(p)[1]

        # Inputs that must stop the build (never guess, never treat missing output as errored runs)
        (d / "bad.txt").write_text(verifier.replace("2/3 criteria passed", "3/3 criteria passed"))
        (d / "other.txt").write_text(verifier.replace("The Agent closes TASK-2.", "The Agent closes TASK-9."))
        (d / "empty.txt").write_text("")
        (d / "template.txt").write_text("RUBRIC VERIFIER RESULTS\nPaste the raw per-run blocks below.\n----\n")
        (d / "graded2.txt").write_text(verifier.replace("Run #3", "Run #2"))
        (d / "twice.txt").write_text(verifier.replace("Run #3", "Run #1"))
        (d / "decision.txt").write_text(verifier.replace("TASK-2.\tPass\tok\n\n", "TASK-2.\tUnclear\tok\n\n"))
        for bad, needle in (("bad.txt", "header says"), ("other.txt", "do not bind"),
                            ("empty.txt", "not errored rollouts"), ("template.txt", "no 'Run #N' blocks"),
                            ("graded2.txt", "verifier graded it"), ("twice.txt", "appears twice"),
                            ("decision.txt", "expected Pass/Fail")):
            try:
                build(d / bad, d / "rubrics.json", traj, "normal", spec_version="V2")
            except ValueError as error:
                assert needle in str(error), (bad, error)
            else:
                raise AssertionError(f"{bad} should stop the build")
        dup = d / "dups"
        dup.mkdir()
        (dup / "trajectory-run-1.json").write_text(json.dumps(events))
        (dup / "trajectory-run-1 (1).json").write_text(json.dumps(events))
        try:
            build(d / "verifier.txt", d / "rubrics.json", dup, "normal", spec_version="V2")
        except ValueError as error:
            assert "two trajectory files for run 1" in str(error), error
        else:
            raise AssertionError("duplicate run files should stop the build")
    _self_test_models()
    print("self-test: ok")


def _self_test_models() -> None:
    """V1: one owner for model labels (planted: the old prefix rule rejected claude-opus-5-5[1m] and <synthetic>)."""
    want = {"claude-opus-5-5": "expected", "claude-opus-5-5[1m]": "expected", "<synthetic>": "synthetic",
            "claude-opus-5": "other", "claude-opus-5[1m]": "other", "claude-opus-4-8[1m]": "other",
            "claude-opus-5-5-20261001": "other", "Opus 5.5": "unknown", "": "unknown", "gpt": "unknown"}
    got = {m: classify_model(m) for m in want}
    assert got == want, got
    assert classify_model("claude-opus-4-8[1m]", "claude-opus-4-8") == "expected"
    ro = lambda i, models: {"id": f"run-{i}", "models": models, "model_source": f"trajectory:run-{i}.json",
                            "model_check": {"v3_valid": True, "mixed_model": False, "fallback_events": [],
                                            "models": ["claude-opus-5-5"]}}  # noqa: E731
    ok = [ro(i, ["<synthetic>", "claude-opus-5-5[1m]"]) for i in range(1, 7)]
    assert model_gate(ok)["verdict"] == "PASS", model_gate(ok)                  # a valid Opus 5.5 run passes
    assert model_gate(ok[:5] + [ro(6, ["claude-opus-5[1m]"])])["verdict"].startswith("FAIL")
    unk = model_gate(ok[:5] + [ro(6, ["claude-opus-5-5", "Opus 5.5"])])
    assert unk["verdict"].startswith("FAIL") and "UNKNOWN" in unk["value"], unk
    assert model_gate(ok[:5] + [ro(6, ["<synthetic>"])])["verdict"].startswith("FAIL")   # synthetic alone is no model
    for blank in ("", None):
        one = dict(ok[0], model=blank, models=None)
        g = model_gate([one] + ok[1:])
        assert g["verdict"].startswith("FAIL") and "UNKNOWN" in g["value"] \
            and "missing" not in g["value"].lower(), g

    def ev(model, parent=None):
        return {"type": "assistant", "parent_tool_use_id": parent, "message": {"model": model, "content": []}}
    init = {"type": "system", "subtype": "init", "model": "claude-opus-5-5[1m]"}
    valid = model_provenance([init, ev("claude-opus-5-5[1m]"), ev("<synthetic>"), ev("claude-opus-5-5[1m]", "t1")])
    assert valid["v3_valid"] is True and not valid["mixed_model"] and valid["synthetic_messages"] == 1, valid
    sub = model_provenance([init, ev("claude-opus-5-5[1m]"), ev("claude-sonnet-5-5", "t9")])
    assert sub["mixed_model"] and sub["v3_valid"] is False and sub["off_model"][0]["source"] == "subagent", sub
    fb = {"type": "system", "subtype": "model_refusal_fallback", "fallback_model": "claude-opus-5[1m]"}
    with_fb = model_provenance([init, ev("claude-opus-5-5[1m]"), fb, ev("claude-opus-5[1m]")])
    assert with_fb["off_model"][0]["after_fallback_event"] == 2 and with_fb["mixed_model"], with_fb
    no_fb = model_provenance([init, ev("claude-opus-5-5[1m]"), ev("claude-opus-5[1m]")])     # audit L4
    assert no_fb["mixed_model"] and no_fb["off_model"][0]["label"] == "claude-opus-5[1m]" and \
        no_fb["off_model"][0]["after_fallback_event"] is None, no_fb
    unknown = model_provenance([init, ev("opus-ish")])
    assert unknown["valid"] == "UNKNOWN" and unknown["v3_valid"] is None and unknown["unknown_labels"] == ["opus-ish"]
    r48 = model_provenance([{"type": "system", "subtype": "init", "model": "claude-opus-4-8[1m]"},
                            ev("claude-opus-4-8[1m]")], expected="claude-opus-4-8")
    assert r48["valid"] == "VALID" and not r48["mixed_model"] and r48["v3_valid"] is False, r48
    # V1-1: an explicitly supplied empty or null label is a label (UNKNOWN), not an absent field; whitespace is part of
    # the label (strip only a bracketed suffix, then compare exactly)
    for label in ("", None):
        blank = model_provenance([init, ev(label)])
        assert blank["valid"] == "UNKNOWN" and blank["v3_valid"] is None and "None" not in blank["models"], blank
    assert classify_model(" claude-opus-5-5 ") == "unknown" and model_id(" claude-opus-5-5 ") == " claude-opus-5-5 "
    padded = model_provenance([{"type": "system", "subtype": "init", "model": " claude-opus-5-5 "}, ev("claude-opus-5-5")])
    assert padded["valid"] == "UNKNOWN" and padded["v3_valid"] is None, padded


def _flag(argv: list[str], name: str) -> str | None:
    if name in argv:
        i = argv.index(name)
        if i + 1 >= len(argv):
            _fail(f"{name} needs a value")
        return argv[i + 1]
    return None


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        _self_test()
        return 0
    if "--build" in argv:
        needed = {k: _flag(argv, k) for k in ("--verifier", "--rubrics", "--trajectories")}
        if not all(needed.values()):
            print(__doc__, file=sys.stderr)
            return 2
        invalid = [x for x in (_flag(argv, "--invalid") or "").split(",") if x]
        corrections = [argv[i + 1] for i, a in enumerate(argv) if a == "--judge-correction" and i + 1 < len(argv)]
        context = None
        task_type = _flag(argv, "--task-type")
        if "--legacy-v2" not in argv:
            context = cli_context(argv, *(Path(value) for value in needed.values()))
            if task_type and _task_type(task_type) != _task_type(context["task_type"]):
                _fail("--task-type disagrees with the current assignment")
            task_type = context["task_type"]
        elif not task_type:
            _fail("--legacy-v2 build requires --task-type")
        data, warnings = build(Path(needed["--verifier"]), Path(needed["--rubrics"]),
                               Path(needed["--trajectories"]), task_type, invalid, corrections,
                               context=context, spec_version="V2" if "--legacy-v2" in argv else "V3")
        for w in warnings:
            print(f"difficulty_stats: warning: {w}", file=sys.stderr)
        text = json.dumps(data, indent=1, ensure_ascii=False)
        out = _flag(argv, "--out")
        if out:
            Path(out).write_text(text + "\n", encoding="utf-8")
            print(f"wrote {out}", file=sys.stderr)
        else:
            print(text)
        return 0
    value_flags = {"--out", "--verifier", "--rubrics", "--trajectories", "--task-type", "--invalid", "--judge-correction",
                   "--task-dir"}
    paths = [a for i, a in enumerate(argv) if not a.startswith("--") and (i == 0 or argv[i - 1] not in value_flags)]
    if len(paths) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    data = json.loads(Path(paths[0]).read_text())
    if "--legacy-v2" in argv:
        if data.get("spec_version") not in (None, "V2"):
            _fail("--legacy-v2 cannot reinterpret a V3 matrix")
        data["spec_version"] = "V2"
    else:
        bind_context(data, cli_context(argv, Path(paths[0])))
    result = compute(data)
    print(json.dumps(result, indent=2) if "--json" in argv else to_markdown(result, data))
    return 1 if result["blocking"] else 0


def cli_context(argv: list[str], *paths: Path) -> dict:
    from task_context import load_context, ContextError

    task_dir = _flag(argv, "--task-dir")
    try:
        return load_context(Path(task_dir) if task_dir else infer_task_dir(*paths))
    except ContextError as error:
        _fail(str(error))


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"difficulty_stats: {error}", file=sys.stderr)
        raise SystemExit(2)

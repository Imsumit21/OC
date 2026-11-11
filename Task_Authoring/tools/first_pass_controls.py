#!/usr/bin/env python3
"""first_pass_controls.py - the first-pass checks the V3 stage gates run (plan of 2026-11-10).

`stage_gate.run_stage` calls `check_stage(gate, ctx)` for a real V3 gate, after the existing checks and never in the
fixture self-test. Each check reads an artifact one of the first-pass tools wrote, or runs that tool in process, and
adds one line to the gate:

  stage           check id                   tool                         what it asks
  scenario        fit.census                 assignment_fit.py            was the fit census run for this assignment?
  scenario        budget.design              difficulty_budget.py         can the planned misses pass the baseline gates?
  injection       budget.injection           difficulty_budget.py         the same, on the injected revision
  injection       exposure.units             path_exposure.py             is any deciding record on a path the model sweeps?
  injection       sweep.forks                coherence_sweep.py           fork sweep on the current SQL, none open
  injection       skeleton.present           rubric_skeleton.py           do the misses carry enough weight on the rubric shape?
  hardening       precheck.budget_outcome    budget_outcome.py            did the pre-check open the anchors?
  hardening       precheck.stop_rule         budget_outcome.py            two failed pre-checks on one design: redesign
  prompt-writing  structure.accepted_outcomes  coherence_sweep.py         fork sweep ran, no open material fork
  prompt-check    sweep.forks                coherence_sweep.py           the same, bound to the prompt as well
  prompt-check    prompt.assignment_fit      (reads 04_Prompt_Check.md)   C4 clean: competency and task skill fit
  oe-check        oe.qualifiers              oe_qualifier_check.py        every Expected qualifier matches its record
  rubric-check    rubric.eval_lint           hg.py rubric-lint            the eval's own rubric lint
  rubric-check    rubric.delta_lint          platform_delta_lint.py       platform-only rubric rules
  rubric-check    budget.rubric              rubric_skeleton.py           the final rubric still carries the budget

Mode per check comes from `references/first_pass_policy.json` (`modes`): `off` (not run), `warn` (a failure prints
WARN and never blocks) or `block` (a failure fails the stage). A check starts in `warn` and moves to `block` only
after its backtest on the archived tasks and one task in warn mode (plan section 5). A missing policy file or an
unknown check id means `warn`. A tool that raises is reported under the check's id with the same mode: a crash never
passes, and in warn mode it never blocks either.

This file is not part of any certificate digest: changing a mode does not make a pasted PASS block stale.

  python3 -B Task_Authoring/tools/first_pass_controls.py modes            # the mode of every check
  python3 -B Task_Authoring/tools/first_pass_controls.py run <stage> --task-dir T [--json]   # these checks alone
  python3 -B Task_Authoring/tools/first_pass_controls.py --self-test
"""
from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
POLICY = BUNDLE / "references" / "first_pass_policy.json"
MODES = ("off", "warn", "block")
WARN_NOTE = " [first-pass check in warn mode: reported, not blocking]"

FIT = "00_Assignment_Fit.json"
BUDGET = "01_Difficulty_Budget.json"
SKELETON = "01_Rubric_Skeleton.json"
EXPOSURE = "01e_Path_Exposure.json"
SWEEP = "01d_Coherence_Sweep.json"
OUTCOME = "06_Budget_Outcome.json"
PRECHECK_LOG = "precheck_log.json"


# ------------------------------------------------------------------ policy


def policy(path: Path = POLICY) -> dict:
    """The policy file, or {} when it is missing or unreadable (every check then runs in warn mode)."""
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def mode(cid: str, pol: dict | None = None) -> str:
    value = ((pol if pol is not None else policy()).get("modes") or {}).get(cid, "warn")
    return value if value in MODES else "warn"


# ------------------------------------------------------------------ helpers


def _tool(name: str):
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    return importlib.import_module(name)


def _sha(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def _json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def _emit(ctx, cid: str, state: str, detail: str, pol: dict) -> None:
    """state: PASS, WARN (advisory in every mode) or FAIL (blocks only in block mode)."""
    m = mode(cid, pol)
    if m == "off":
        return
    if state == "PASS":
        ctx.add(cid, True, detail)
    elif state == "WARN":
        ctx.add(cid, False, detail, block=False)
    else:
        ctx.add(cid, False, detail + ("" if m == "block" else WARN_NOTE), block=(m == "block"))


def _summary(result: dict, limit: int = 3) -> str:
    """One line from a tool result: its verdict and the first failing or warning checks."""
    rows = [c for c in result.get("checks") or [] if c.get("status") in ("FAIL", "WARN")]
    rows.sort(key=lambda c: 0 if c.get("status") == "FAIL" else 1)
    parts = [f"{c.get('id')}: {str(c.get('detail') or '')[:140]}" for c in rows[:limit]]
    more = f" (+{len(rows) - limit} more)" if len(rows) > limit else ""
    return f"{result.get('verdict')}" + (": " + "; ".join(parts) + more if parts else "")


def _from_tool(ctx, cid: str, pol: dict, result, ok_detail: str, run_hint: str) -> None:
    """Map a tool's result object ({verdict, checks}) to one gate line."""
    if not isinstance(result, dict) or result.get("verdict") not in ("PASS", "WARN", "FAIL"):
        _emit(ctx, cid, "FAIL", f"no usable result from the tool — run {run_hint}", pol)
        return
    verdict = result["verdict"]
    if verdict == "PASS":
        _emit(ctx, cid, "PASS", ok_detail, pol)
    else:
        _emit(ctx, cid, verdict, _summary(result) + f" — {run_hint}", pol)


def _bound(ctx, record: dict, names: dict) -> list:
    """Files whose current sha256 differs from the record's `bound_to` ({label or file name: sha256}).

    `names` maps a slot file name to the keys a record may use for it. A file the record does not bind is not
    reported: each tool decides what it binds."""
    bound = record.get("bound_to") or {}
    if not isinstance(bound, dict):
        return ["bound_to is not an object"]
    flat = {}
    for key, value in bound.items():
        flat[str(key)] = value.get("sha256") if isinstance(value, dict) else value
    stale = []
    for slot, keys in names.items():
        now = _sha(ctx.p(slot))
        for key in keys:
            hit = next((flat[k] for k in flat if k == key or k.endswith("/" + key)), None)
            if hit is not None:
                if hit != now:
                    stale.append(f"{slot} ({'missing' if now is None else 'changed'} since it was checked)")
                break
    return stale


# ------------------------------------------------------------------ checks


def fit_census(gate, ctx, pol) -> None:
    cid, hint = "fit.census", "python3 Task_Authoring/tools/assignment_fit.py census --task-dir <task_dir> --write"
    rec = _json(ctx.p(FIT))
    if rec is None:
        _emit(ctx, cid, "FAIL", f"no Working_Files/{FIT}: the fit census was not run before the design — {hint}", pol)
        return
    verdict = str(rec.get("verdict") or rec.get("fit") or "").strip()
    want = (ctx.context or {}).get("assignment_hash")
    got = rec.get("assignment_hash") or (rec.get("assignment") or {}).get("assignment_hash")
    if want and got and str(got)[:12] != str(want)[:12]:
        _emit(ctx, cid, "FAIL", f"{FIT} was written for another assignment (hash {str(got)[:12]}, now "
              f"{str(want)[:12]}) — {hint}", pol)
        return
    if not verdict or verdict.upper() == "FAIL" or str(rec.get("status") or "").upper() == "FAIL":
        _emit(ctx, cid, "FAIL", f"{FIT} carries no census verdict (the census did not run to the end) — {hint}", pol)
        return
    limits = rec.get("limits") or []
    note = f"; limits: {'; '.join(str(x)[:80] for x in limits[:3])}" if limits else ""
    route = (" — the scenario is built by injection (playbook 01_Scenario_Design, injection-built scenario)"
             if "NO NATURAL COHORT" in verdict.upper() else "")
    _emit(ctx, cid, "PASS", f"fit census: {verdict}{note}{route}", pol)


def _budget(gate, ctx, pol, cid: str) -> None:
    hint = "python3 Task_Authoring/tools/difficulty_budget.py check --task-dir <task_dir>"
    if not ctx.p(BUDGET).is_file():
        _emit(ctx, cid, "FAIL", f"no Working_Files/{BUDGET}: the design has no difficulty budget (one row per planned "
              f"miss: carrier, deciding record, find-rate range, rows and weight) — write it, then {hint}", pol)
        return
    result = _tool("difficulty_budget").evaluate(ctx.td)
    _from_tool(ctx, cid, pol, result, "difficulty budget PASS: anchors, four or more independent coin-flip units, "
               "average, full passes and the signature gate hold at both ends of the find-rate ranges", hint)


def budget_design(gate, ctx, pol) -> None:
    _budget(gate, ctx, pol, "budget.design")


def budget_injection(gate, ctx, pol) -> None:
    _budget(gate, ctx, pol, "budget.injection")


def exposure_units(gate, ctx, pol) -> None:
    cid = "exposure.units"
    hint = "python3 Task_Authoring/tools/path_exposure.py check --task-dir <task_dir> --write"
    rec = _json(ctx.p(EXPOSURE))
    if rec is None:
        _emit(ctx, cid, "FAIL", f"no Working_Files/{EXPOSURE}: no unit's deciding record was checked for exposure — "
              f"{hint}", pol)
        return
    stale = _bound(ctx, rec, {"01_Universe_Inject.sql": ("01_Universe_Inject.sql", "sql"),
                              BUDGET: (BUDGET, "budget"),
                              "01_Hardness_Manifest.json": ("01_Hardness_Manifest.json", "manifest")})
    if stale:
        _emit(ctx, cid, "FAIL", "the path-exposure record is stale: " + "; ".join(stale) + f" — {hint}", pol)
        return
    _from_tool(ctx, cid, pol, rec, "path exposure PASS: every anchor and coin-flip unit's deciding record is off the "
               "paths the model sweeps, on the current SQL and budget", hint)


def _sweep(gate, ctx, pol, cid: str, with_prompt: bool) -> None:
    hint = "python3 Task_Authoring/tools/coherence_sweep.py check --task-dir <task_dir>"
    if not ctx.p(SWEEP).is_file():
        _emit(ctx, cid, "FAIL", f"no Working_Files/{SWEEP}: no fork sweep was recorded for this universe, so an "
              f"unresolved material fork would reach /prompt unseen (20 of 30 archived /prompt FAILs) — run the sweep "
              f"(playbook 01_Universe_Injection, coherence sweep), then {hint}", pol)
        return
    result = _tool("coherence_sweep").evaluate(ctx.td)
    scope = "the current SQL and prompt" if with_prompt and ctx.p("04_Prompt.txt").is_file() else "the current SQL"
    _from_tool(ctx, cid, pol, result, f"fork sweep PASS on {scope}: no open material fork, every open set has a rule "
               f"and a census", hint)


def sweep_forks(gate, ctx, pol) -> None:
    _sweep(gate, ctx, pol, "sweep.forks", with_prompt=ctx.stage == "prompt-check")


def accepted_outcomes(gate, ctx) -> None:
    """prompt-writing: replaces the unconditional V3 pass of `structure.accepted_outcomes` (plan WS4 item 5).

    V3 accepts several fair outcomes; it does not accept an unresolved material fork. The fork sweep is the
    evidence. The mode is that of `sweep.forks`."""
    cid, pol = "structure.accepted_outcomes", policy()
    m = mode("sweep.forks", pol)
    if m == "off":
        ctx.add(cid, True, "V3 accepts multiple fair outcomes; see v3.fair_outcomes_review (fork sweep check is off)")
        return
    probe = _Probe(ctx)
    try:
        _sweep(gate, probe, {"modes": {cid: m}}, cid, with_prompt=True)
    except Exception as exc:  # noqa: BLE001 - reported under the check id, never raised into the gate
        probe.add(cid, False, f"fork sweep check could not run: {type(exc).__name__}: {exc}" +
                  ("" if m == "block" else WARN_NOTE), block=(m == "block"))
    for row in probe.rows:
        detail = row["detail"]
        if row["ok"]:
            detail = "V3 accepts multiple fair outcomes (v3.fair_outcomes_review); " + detail
        ctx.add(cid, row["ok"], detail, block=row["block"])


class _Probe:
    """Collects ctx.add calls so a caller can rewrite the detail before adding them to the real context."""

    def __init__(self, ctx):
        self._ctx, self.rows = ctx, []
        self.td, self.stage, self.context = ctx.td, ctx.stage, ctx.context

    def p(self, name):
        return self._ctx.p(name)

    def add(self, cid, ok, detail, locs=(), block=True, status=None):
        self.rows.append({"ok": ok, "detail": detail, "block": block})


def skeleton_present(gate, ctx, pol) -> None:
    cid = "skeleton.present"
    hint = "python3 Task_Authoring/tools/rubric_skeleton.py build --task-dir <task_dir> --write"
    if not ctx.p(SKELETON).is_file():
        _emit(ctx, cid, "FAIL", f"no Working_Files/{SKELETON}: the rubric's shape (one row per write target, weights "
              f"by kind of work) was not derived, so the budget is still measured on the surface, not on what will be "
              f"graded — {hint}", pol)
        return
    result = _tool("rubric_skeleton").evaluate(ctx.td, command="check")
    _from_tool(ctx, cid, pol, result, "rubric skeleton PASS: on the expanded row set the anchors still carry the "
               "mode's loss and the coin-flip share holds", hint.replace("build", "check").replace(" --write", ""))


def budget_rubric(gate, ctx, pol) -> None:
    cid = "budget.rubric"
    hint = "python3 Task_Authoring/tools/rubric_skeleton.py drift --task-dir <task_dir>"
    budget = _json(ctx.p(BUDGET))
    if budget is None:
        _emit(ctx, cid, "FAIL", f"no Working_Files/{BUDGET}: the final rubric cannot be compared with the design "
              f"budget", pol)
        return
    if not budget.get("rubric_rows"):
        _emit(ctx, cid, "FAIL", f"{BUDGET} has no `rubric_rows`: map each unit to the final 09_Rubrics.json rows it "
              f"flips, then {hint} (rubric growth alone moved two tasks' predicted average by 7 to 10 points)", pol)
        return
    result = _tool("rubric_skeleton").evaluate(ctx.td, command="drift")
    _from_tool(ctx, cid, pol, result, "the final rubric still carries the budget: anchors at or above the mode's "
               "loss, no unit's share moved by more than five points", hint)


def precheck_outcome(gate, ctx, pol) -> None:
    """hardening: the stored comparison of the pre-check run with the budget (budget_outcome.py compare --write)."""
    cid = "precheck.budget_outcome"
    hint = "python3 Task_Authoring/tools/budget_outcome.py compare --task-dir <task_dir> --write"
    rec = _json(ctx.p(OUTCOME))
    if rec is None:
        _emit(ctx, cid, "FAIL", f"no Working_Files/{OUTCOME}: the pre-check was not compared with the budget (was "
              f"each unit's deciding record opened?) — {hint}", pol)
        return
    stale = _bound(ctx, rec, {"06_PreCheck_Trajectory/trajectory.json": ("06_PreCheck_Trajectory/trajectory.json",
                                                                         "trajectory.json", "trajectory"),
                              BUDGET: (BUDGET, "budget"),
                              "01_Universe_Inject.sql": ("01_Universe_Inject.sql", "sql")})
    if stale:
        _emit(ctx, cid, "FAIL", "the budget-outcome record is stale: " + "; ".join(stale) + f" — {hint}", pol)
        return
    outcome = str(rec.get("outcome") or "").upper().replace("_", "-")
    review = [str(h.get("unit") if isinstance(h, dict) else h) for h in rec.get("hand_review") or []]
    if outcome == "GO":
        _emit(ctx, cid, "PASS", "pre-check against the budget: GO — no anchor's deciding record was opened"
              + (f"; hand review needed only for {review[:6]}" if review else "; no unit contradicts the budget"), pol)
    elif outcome == "NO-GO":
        opened = rec.get("opened_anchors") or []
        _emit(ctx, cid, "WARN", f"pre-check against the budget: NO-GO — anchor(s) opened: {opened[:6]}. Repair with "
              f"one relocation of the exposed record (playbook 01a step 1b), not added rows or prompt rules", pol)
    else:
        _emit(ctx, cid, "FAIL", f"{OUTCOME} carries no GO / NO-GO outcome — {hint}", pol)


def stop_rule(gate, ctx, pol) -> None:
    """hardening: two failed pre-checks on one design send the task back to /create-scenario (budget_outcome owns
    the count; with no pre-check log there is nothing to count)."""
    cid = "precheck.stop_rule"
    if not ctx.p(PRECHECK_LOG).is_file() or not ctx.p(BUDGET).is_file():
        _emit(ctx, cid, "PASS", "no failed pre-check is logged for this design", pol)
        return
    result = _tool("budget_outcome").stop_rule(ctx.td, pol if pol.get("precheck") else None)
    if result.get("verdict") == "FAIL":
        detail = result.get("stop") or _summary(result)
        _emit(ctx, cid, "FAIL", f"{detail} (plan WS6 item 5; a redesign gets a new `design_id` in {BUDGET})", pol)
    else:
        _emit(ctx, cid, "PASS", _summary(result) if result.get("verdict") != "PASS" else
              f"{result.get('no_go', 0)} failed pre-check(s) on design {result.get('design_id')}; the stop rule "
              f"applies at {result.get('limit')}", pol)


RX_C4_ROW = re.compile(r"^\|\s*C4\s*\|\s*([^|]*)\|", re.M)
RX_CLEAN = re.compile(r"^\s*(?:clean|pass|ok|none|no finding)\b", re.I)
RX_RESULTS = re.compile(r"^#{1,6}[^\n]*check results[^\n]*\n(.*?)(?=^#{1,6}\s|\Z)", re.I | re.M | re.S)
RX_FINDINGS = re.compile(r"^#{1,6}[^\n]*findings[^\n]*\n(.*?)(?=^#{1,6}\s|\Z)", re.I | re.M | re.S)
RX_C4_CELL = re.compile(r"(?<![\w-])C4(?![\w-])")
RX_OPEN_SEVERITY = re.compile(r"(?<![\w-])(?:non-?fail|fail)(?![\w-])", re.I)
RX_SETTLED = re.compile(r"\bresolved\b|\badvisory\b|\bfixed\b|\bclosed\b", re.I)


def assignment_fit(gate, ctx, pol) -> None:
    """prompt-check: C4 (competency, task skill) must be clean. Eval 1 applies a hard FAIL to a clear mismatch.

    C4's result is read from the check-results table when the report has one ('| C4 | clean | ...'); otherwise from
    the Findings table, where an open Fail or Non-fail finding on C4 is the mismatch. A Self-review row that argues
    a counter-reading of C4 is not a result. `structure.c_checks` already requires C4 to be recorded somewhere."""
    cid = "prompt.assignment_fit"
    text = ctx.doc("04_Prompt_Check.md").text
    if not RX_C4_CELL.search(text):
        _emit(ctx, cid, "FAIL", "04_Prompt_Check.md never mentions C4 (competency, task skill, business function)",
              pol)
        return
    why = ("/prompt applies a hard FAIL to a clear competency mismatch or an assigned skill that is not a real part "
           "of the work: change the work, not the label")
    section = RX_RESULTS.search(text)
    rows = RX_C4_ROW.findall(section.group(1) if section else "")
    if rows:
        bad = [r.strip() for r in rows if not RX_CLEAN.match(r)]
        if bad:
            _emit(ctx, cid, "FAIL", f"C4 is not clean in the check results of 04_Prompt_Check.md: '{bad[0][:60]}'. "
                  + why, pol)
        else:
            _emit(ctx, cid, "PASS", "C4 clean in the check results: the work fits the assigned competency and task "
                  "skill", pol)
        return
    findings = RX_FINDINGS.search(text)
    open_rows = []
    for line in (findings.group(1) if findings else "").splitlines():
        if line.lstrip().startswith("|") and RX_C4_CELL.search(line) and RX_OPEN_SEVERITY.search(line) \
                and not RX_SETTLED.search(line):
            open_rows.append(line.strip())
    if open_rows:
        _emit(ctx, cid, "FAIL", f"an open C4 finding in 04_Prompt_Check.md: '{open_rows[0][:90]}'. " + why, pol)
    else:
        _emit(ctx, cid, "PASS", "no open C4 finding: the work fits the assigned competency and task skill", pol)


def oe_qualifiers(gate, ctx, pol) -> None:
    """oe-check: every qualifier on an Expected line against the record its event reads.

    The tool's own verdict is WARN whenever any qualifier is unverifiable, which was true of all 13 archived files the
    platform passed at 5 (1-74 unverifiable each), so it cannot separate good files from bad. The gate reads the counts
    instead: a contradicted qualifier fails, an unsupported one warns, unverifiable ones are reported as a count."""
    cid = "oe.qualifiers"
    hint = "python3 Task_Authoring/tools/oe_qualifier_check.py check --task-dir <task_dir>"
    if getattr(ctx, "rerun", "all") != "all":
        # The base reads take about 10-20 s warm and up to ~2.5 min cold; `--rerun lint` is the gate's fast mode and
        # skips its other expensive re-runs too. Cheaper base modes were measured to give false contradictions.
        if mode(cid, pol) != "off":
            ctx.add(cid, True, f"skipped under --rerun lint (base reads take 10-150 s) — {hint}", status="SKIP")
        return
    result = _tool("oe_qualifier_check").evaluate(ctx.td)
    counts = result.get("counts") if isinstance(result, dict) else None
    if not isinstance(counts, dict) or result.get("verdict") not in ("PASS", "WARN", "FAIL"):
        _from_tool(ctx, cid, pol, result, "", hint)
        return
    bad = {k: int(counts.get(k) or 0) for k in ("contradicted", "unsupported", "unverifiable", "checked")}
    parse = [c for c in result.get("checks") or [] if c.get("id") == "oe.parse" and c.get("status") == "FAIL"]
    tail = f"{bad['checked']} qualifiers checked; {bad['unverifiable']} unverifiable (reported, not judged)"
    if parse:
        _emit(ctx, cid, "FAIL", f"the Oracle Events could not be parsed: {parse[0].get('detail', '')[:160]} — {hint}", pol)
    elif bad["contradicted"]:
        _emit(ctx, cid, "FAIL", f"{bad['contradicted']} qualifier(s) on Expected lines contradict the record the event "
              f"reads; {bad['unsupported']} unsupported; {tail} — {hint}", pol)
    elif bad["unsupported"]:
        _emit(ctx, cid, "WARN", f"{bad['unsupported']} qualifier(s) on Expected lines are in no record read; {tail} — "
              f"{hint}", pol)
    else:
        _emit(ctx, cid, "PASS", f"no qualifier contradicted or unsupported; {tail}", pol)


LINT_BLOCKING = ("gate", "major", "critical", "fail")


def rubric_eval_lint(gate, ctx, pol) -> None:
    """The eval's own rubric lint (hg.py rubric-lint). No gate ran it before (plan RC4)."""
    cid = "rubric.eval_lint"
    hint = "python3 Task_Authoring/tools/hg.py rubric-lint <task_dir>/09_Rubrics.json --task-dir <task_dir>"
    rc, out, err = gate.run_tool([HERE / "hg.py", "rubric-lint", ctx.p("09_Rubrics.json"), "--task-dir", ctx.td])
    data = gate._json_stdout(out)
    if rc != 0 or not isinstance(data, dict) or "findings" not in data:
        tail = ((err or out).strip().splitlines() or ["no output"])[-1][:160]
        _emit(ctx, cid, "FAIL", f"hg.py rubric-lint did not run (exit {rc}): {tail} — {hint}", pol)
        return
    findings = [f for f in data.get("findings") or [] if isinstance(f, dict)]
    hard = [f for f in findings if str(f.get("severity") or "").lower() in LINT_BLOCKING]
    soft = [f for f in findings if f not in hard]
    names = lambda rows: ", ".join(sorted({f"{f.get('check')} (row {f.get('row')})" for f in rows})[:5])  # noqa: E731
    if hard:
        _emit(ctx, cid, "FAIL", f"the eval's rubric lint has {len(hard)} gate/Major finding(s): {names(hard)}"
              + (f"; plus {len(soft)} to review" if soft else "") + f" — {hint}", pol)
    elif soft:
        doc = ctx.doc("09_Rubric_Check.md").text
        open_ = [f for f in soft if not re.search(r"\b" + re.escape(str(f.get("check"))) + r"\b", doc)]
        if open_:
            _emit(ctx, cid, "WARN", f"the eval's rubric lint has {len(soft)} finding(s) to review; "
                  f"09_Rubric_Check.md never names {sorted({str(f.get('check')) for f in open_})[:5]} — {hint}", pol)
        else:
            _emit(ctx, cid, "PASS", f"the eval's rubric lint: 0 gate/Major findings; {len(soft)} review finding(s), "
                  f"each kind named in 09_Rubric_Check.md", pol)
    else:
        _emit(ctx, cid, "PASS", "the eval's rubric lint: no findings", pol)


def rubric_delta_lint(gate, ctx, pol) -> None:
    cid = "rubric.delta_lint"
    hint = "python3 Task_Authoring/tools/platform_delta_lint.py rubric --task-dir <task_dir>"
    mod = _tool("platform_delta_lint")
    fn = getattr(mod, "evaluate_rubric", None)
    result = fn(ctx.td) if fn else mod.evaluate(ctx.td, artifact="rubric")
    _from_tool(ctx, cid, pol, result, "platform-only rubric rules: no finding (one row per separate write, no count "
               "over separate writes, no guard without a trap)", hint)


def task_folder(gate, ctx, pol) -> None:
    """Every stage: a task works in its own named folder (plan WS7 item 1). A bare `task_inputs` folder is the one
    two sessions both default to; a Leonard report was once saved into S2's folder that way."""
    cid = "task.folder"
    name = Path(ctx.td).resolve().name
    if name == "task_inputs":
        _emit(ctx, cid, "FAIL", "the task folder is the bare default `task_inputs`: give each task its own folder "
              "(`Task_Authoring/task_inputs<Label>`) and pass it to every command, so two tasks never share one", pol)
    else:
        _emit(ctx, cid, "PASS", f"task folder `{name}` is named for this task", pol)


EVERY_STAGE = (("task.folder", task_folder),)

STAGE_CHECKS = {
    "scenario": (("fit.census", fit_census), ("budget.design", budget_design)),
    "injection": (("budget.injection", budget_injection), ("exposure.units", exposure_units),
                  ("sweep.forks", sweep_forks), ("skeleton.present", skeleton_present)),
    "hardening": (("precheck.budget_outcome", precheck_outcome), ("precheck.stop_rule", stop_rule)),
    "prompt-check": (("sweep.forks", sweep_forks), ("prompt.assignment_fit", assignment_fit)),
    "oe-check": (("oe.qualifiers", oe_qualifiers),),
    "rubric-check": (("rubric.eval_lint", rubric_eval_lint), ("rubric.delta_lint", rubric_delta_lint),
                     ("budget.rubric", budget_rubric)),
}


def check_stage(gate, ctx) -> None:
    """Run this stage's first-pass checks. Never raises: a tool error is one line under the check's id."""
    pol = policy()
    for cid, fn in EVERY_STAGE + STAGE_CHECKS.get(ctx.stage, ()):
        if mode(cid, pol) == "off":
            continue
        try:
            fn(gate, ctx, pol)
        except Exception as exc:  # noqa: BLE001 - a broken first-pass tool must not take the gate down
            _emit(ctx, cid, "FAIL", f"check could not run: {type(exc).__name__}: {str(exc)[:200]}", pol)


# ------------------------------------------------------------------ CLI


def _modes_text(pol: dict) -> str:
    lines = [f"FIRST-PASS CHECKS ({POLICY.name}{'' if pol else ' missing: every check is in warn mode'})"]
    for cid, _fn in EVERY_STAGE:
        lines.append(f"  {'every stage':<15} {cid:<26} {mode(cid, pol)}")
    for stage, checks in STAGE_CHECKS.items():
        for cid, _fn in checks:
            lines.append(f"  {stage:<15} {cid:<26} {mode(cid, pol)}")
    lines.append(f"  {'prompt-writing':<15} {'structure.accepted_outcomes':<26} {mode('sweep.forks', pol)} (follows sweep.forks)")
    return "\n".join(lines)


def _run(stage: str, task_dir: Path, as_json: bool) -> int:
    gate = _tool("stage_gate")
    ctx = gate.Ctx(stage, task_dir)
    if not gate.assignment_context(ctx):
        print("\n".join(f"[{r['status']}] {r['id']}: {r['detail']}" for r in ctx.res))
        return 1
    start = len(ctx.res)
    check_stage(gate, ctx)
    if stage == "prompt-writing":
        accepted_outcomes(gate, ctx)
    rows = ctx.res[start:]
    blocking = any(r["blocking"] for r in rows)
    verdict = "FAIL" if blocking else "WARN" if any(r["status"] == "WARN" for r in rows) else "PASS"
    if as_json:
        print(json.dumps({"tool": "first_pass_controls", "version": 1, "stage": stage, "verdict": verdict,
                          "checks": [{"id": r["id"], "status": r["status"], "detail": r["detail"]} for r in rows]},
                         indent=2, ensure_ascii=False))
    else:
        print(f"FIRST-PASS CHECKS ({stage}): {verdict}")
        for r in rows:
            print(f"[{r['status']}] {r['id']}: {r['detail']}")
    return 1 if blocking else 0


class _FakeCtx:
    def __init__(self, td: Path, stage: str, context=None):
        self.td, self.stage, self.context, self.res = Path(td), stage, context or {}, []

    def p(self, name):
        direct = self.td / name
        return direct if direct.exists() else self.td / "Working_Files" / name

    def doc(self, name):
        path = self.p(name)
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        return type("Doc", (), {"text": text})()

    def add(self, cid, ok, detail, locs=(), block=True, status=None):
        st = status or ("PASS" if ok else ("FAIL" if block else "WARN"))
        self.res.append({"id": cid, "status": st, "blocking": bool(block and st == "FAIL"), "detail": detail})


def _self_test() -> None:
    sb = _tool("selftest_sandbox")
    with sb.scratch_tmp("first_pass_controls_") as tmp:
        td = Path(tmp) / "task"
        (td / "Working_Files").mkdir(parents=True)
        warn = {"modes": {}}
        block = {"modes": {c: "block" for checks in STAGE_CHECKS.values() for c, _ in checks}}
        off = {"modes": {c: "off" for checks in STAGE_CHECKS.values() for c, _ in checks}}
        assert mode("anything", {}) == "warn" and mode("x", {"modes": {"x": "bogus"}}) == "warn"

        # a missing artifact warns in warn mode, blocks in block mode, and is silent when off
        for pol, want in ((warn, ("WARN", False)), (block, ("FAIL", True))):
            ctx = _FakeCtx(td, "scenario")
            fit_census(None, ctx, pol)
            assert (ctx.res[0]["status"], ctx.res[0]["blocking"]) == want, ctx.res
        ctx = _FakeCtx(td, "scenario")
        fit_census(None, ctx, off)
        assert ctx.res == []

        # fit census: verdict read, another assignment's file refused, NO NATURAL COHORT routed to injection
        (td / "Working_Files" / FIT).write_text(json.dumps({"verdict": "NO NATURAL COHORT", "assignment_hash": "a" * 64}))
        ctx = _FakeCtx(td, "scenario", {"assignment_hash": "a" * 64})
        fit_census(None, ctx, block)
        assert ctx.res[0]["status"] == "PASS" and "built by injection" in ctx.res[0]["detail"], ctx.res
        ctx = _FakeCtx(td, "scenario", {"assignment_hash": "b" * 64})
        fit_census(None, ctx, block)
        assert ctx.res[0]["blocking"], ctx.res

        # a stored record bound to other bytes is stale
        (td / "01_Universe_Inject.sql").write_text("-- sql\n")
        (td / "Working_Files" / EXPOSURE).write_text(json.dumps(
            {"verdict": "PASS", "bound_to": {"01_Universe_Inject.sql": "0" * 64}, "checks": []}))
        ctx = _FakeCtx(td, "injection")
        exposure_units(None, ctx, block)
        assert ctx.res[0]["blocking"] and "stale" in ctx.res[0]["detail"], ctx.res
        good = hashlib.sha256(b"-- sql\n").hexdigest()
        (td / "Working_Files" / EXPOSURE).write_text(json.dumps(
            {"verdict": "FAIL", "bound_to": {"01_Universe_Inject.sql": good},
             "checks": [{"id": "exposure.unit.U1", "status": "FAIL", "detail": "EXPOSED: keyword"}]}))
        ctx = _FakeCtx(td, "injection")
        exposure_units(None, ctx, warn)
        assert ctx.res[0]["status"] == "WARN" and "exposure.unit.U1" in ctx.res[0]["detail"], ctx.res

        # stop rule: two NO-GO on the same design stop; a new design id starts the count again
        (td / "Working_Files" / BUDGET).write_text(json.dumps({"design_id": "D1", "units": []}))
        (td / "Working_Files" / PRECHECK_LOG).write_text(json.dumps(
            {"entries": [{"design_id": "D1", "verdict": "NO-GO"}, {"design_id": "D1", "verdict": "NO-GO"}]}))
        ctx = _FakeCtx(td, "hardening")
        stop_rule(None, ctx, dict(block, precheck={"stop_after_no_go": 2}))
        assert ctx.res[0]["blocking"] and "/create-scenario" in ctx.res[0]["detail"], ctx.res
        (td / "Working_Files" / BUDGET).write_text(json.dumps({"design_id": "D2", "units": []}))
        ctx = _FakeCtx(td, "hardening")
        stop_rule(None, ctx, block)
        assert ctx.res[0]["status"] == "PASS", ctx.res

        # C4: a clean row passes, a mismatch row fails, a missing result fails
        check = td / "Working_Files" / "04_Prompt_Check.md"
        check.write_text("## Check results (C1-C24)\n\n| C4 | clean | Finance work |\n\n## Self-review\n\n"
                         "| C4 | Business Function could read 3 | the platform scored it 5 |\n")
        ctx = _FakeCtx(td, "prompt-check")
        assignment_fit(None, ctx, block)
        assert ctx.res[0]["status"] == "PASS", ctx.res          # a Self-review counter-reading is not a result
        check.write_text("## Check results\n\n| C4 | Non-fail | reads as Engineering Ops, not Finance |\n")
        ctx = _FakeCtx(td, "prompt-check")
        assignment_fit(None, ctx, block)
        assert ctx.res[0]["blocking"], ctx.res
        check.write_text("## Findings\n\n| 6 | C4 | Assigned Task Skill - Fail | the skill is incidental |\n\n## Route\n")
        ctx = _FakeCtx(td, "prompt-check")
        assignment_fit(None, ctx, block)
        assert ctx.res[0]["blocking"], ctx.res
        check.write_text("## Findings\n\n| 6 | C4 | Assigned Task Skill - resolved (linter FAIL on revision 2) | x |\n")
        ctx = _FakeCtx(td, "prompt-check")
        assignment_fit(None, ctx, block)
        assert ctx.res[0]["status"] == "PASS", ctx.res
        check.write_text("nothing here\n")
        ctx = _FakeCtx(td, "prompt-check")
        assignment_fit(None, ctx, warn)
        assert ctx.res[0]["status"] == "WARN", ctx.res

        # a tool that raises is one line under its id, in the check's mode, and never escapes
        def boom(gate, ctx, pol):
            raise RuntimeError("tool exploded")
        saved = STAGE_CHECKS["oe-check"]
        STAGE_CHECKS["oe-check"] = (("oe.qualifiers", boom),)
        try:
            real = globals()["policy"]
            for pol, want in ((warn, "WARN"), (block, "FAIL")):
                globals()["policy"] = lambda path=POLICY, _p=pol: _p
                ctx = _FakeCtx(td, "oe-check")
                check_stage(None, ctx)
                rows = [r for r in ctx.res if r["id"] == "oe.qualifiers"]
                assert [r["status"] for r in rows] == [want] and "tool exploded" in rows[0]["detail"], ctx.res
        finally:
            STAGE_CHECKS["oe-check"] = saved
            globals()["policy"] = real
    print("self-test: ok (modes off / warn / block, missing artifacts, stale bindings, fit census routing, stop rule, "
          "C4 result, a tool error contained)")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="First-pass checks run by the V3 stage gates.")
    ap.add_argument("command", nargs="?", choices=("modes", "run"))
    ap.add_argument("stage", nargs="?")
    ap.add_argument("--task-dir", type=Path)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        _self_test()
        return 0
    if args.command == "modes":
        print(_modes_text(policy()))
        return 0
    if args.command == "run":
        if not args.stage or not args.task_dir:
            ap.error("run needs a stage and --task-dir")
        if args.stage not in STAGE_CHECKS and args.stage != "prompt-writing":
            ap.error(f"no first-pass check for stage {args.stage!r}")
        return _run(args.stage, args.task_dir, args.json)
    ap.error("give a command (modes, run) or --self-test")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""preflight_report.py - Working_Files/01c_Preflight_Report.json (+ .md): the /create-injection preflight (plan §4.3).

One report records what /create-injection S4b-S5e established, bound by sha256 to every file it checked:
  solver_contract  tools/oracle_kit.py contract                                                      blocking
  surface          tools/gradable_surface.py validation; each slot's expected value (from the solver) and the
                   mutants that flip it (flipped_by). They are recorded here, so the scenario-certified surface file is
                   never rewritten by injection (rewriting it would make the scenario certificate stale).  blocking
  mutation         tools/difficulty_mutation.py rule / degrade mutants, interventions, and a written disposition for
                   every one of them                                                                  blocking
  geometry         U per gate view (blocking: U <= 1 - cap) and L_max (advisory)
  liveness         tools/trap_liveness.py flags with their written dispositions                       advisory
  forecast         the pre-registered tools/hardness_forecast.py record, or "not run"                 advisory
verdict FAIL when a blocking part fails; advisory parts are reported and never gate. Probabilistic parts are
UNCALIBRATED.

Dispositions are the author's, in Working_Files/01c_Dispositions.json:
  {"mutation": {"rule:<id>" | "degrade:<op>" | "intervention:<kind>:<id>": {"disposition": one of
                difficulty_mutation.DISPOSITIONS, "reason": "..."}},
   "liveness": {"<node>:<flag>": {"disposition": "...", "reason": "..."}}}

Usage:
  python3 -B Task_Authoring/tools/preflight_report.py --task-dir DIR [--solver S] [--sql SQL] [--surface S]
      [--manifest M] [--prompt P] [--dispositions D.json] [--previous-sql P --previous-truth T] [--forecast F.json]
      [--views auto|v2|v3|both] [--max-k 8 [--allow-max-k N for N > 8: disclosed]] [--out Working_Files/01c_Preflight_Report.json]
  python3 -B Task_Authoring/tools/preflight_report.py --self-test
Exit 0 = PASS, 1 = FAIL (a blocking part), 2 = usage error.
"""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path


def _bundle() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "difficulty_stats.py").is_file():
            return parent
    raise SystemExit("preflight_report: cannot find the Task_Authoring bundle (no tools/difficulty_stats.py above)")


HERE = Path(__file__).resolve().parent
BUNDLE = _bundle()
for _p in (BUNDLE / "tools", HERE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import difficulty_mutation as dm  # noqa: E402
import gradable_surface as gs  # noqa: E402
import oracle_kit as ok  # noqa: E402
import trajectory_ledger as tl  # noqa: E402
import trap_liveness as tlv  # noqa: E402

VERSION = "preflight_report/1"
KIND = "PREFLIGHT_REPORT"


def _sha(p) -> str | None:
    return tl.sha256_file(Path(p)) if p and Path(p).is_file() else None


def _where(p, task_dir):
    """A path relative to the task folder when it is inside it (the report stays valid when the folder moves)."""
    if not p:
        return None
    try:
        return str(Path(p).resolve().relative_to(Path(task_dir).resolve())) if task_dir else tl._rel(Path(p))
    except ValueError:
        return tl._rel(Path(p))


def build(*, solver: Path, sql: Path, surface_path: Path, manifest_path: Path | None, prompt: Path | None,
          dispositions_path: Path | None, previous_sql: Path | None = None, previous_truth: Path | None = None,
          forecast: Path | None = None, views: str = "auto", context=None, max_k: int = dm.MAX_K, task_dir=None) -> dict:
    sql_text = sql.read_text()
    manifest = json.loads(manifest_path.read_text()) if manifest_path and manifest_path.is_file() else None
    surface = gs.load(surface_path)
    disp = json.loads(dispositions_path.read_text()) if dispositions_path and dispositions_path.is_file() else {}
    mod = ok.load_solver(solver)
    contract = ok.contract(solver, sql_text, previous_sql=previous_sql.read_text() if previous_sql else None,
                           previous_truth=previous_truth, manifest=manifest, surface=surface, task_dir=task_dir)
    eng = dm.Engine(mod, sql_text, None, max_k)
    slots = dm.Slots(surface["slots"], surface)
    sval = gs.validate(surface, manifest, list(mod.RULES))
    mut = dm.mutants(eng, slots)
    inter = dm.interventions(eng, slots)
    geo = dm.geometry(eng, slots, surface, dm.caps_for(views, context))
    results = mut["rules"] + mut["degrades"] + [x for x in inter if "status" in x]
    mdisp = dm.dispositions(results, disp.get("mutation") or {})
    gdisp = dm.geometry_dispositions(geo, disp.get("geometry") or {})
    flipped_by = {}
    for x in mut["rules"] + mut["degrades"]:
        for sid in x["flipped_slots"]:
            flipped_by.setdefault(sid, []).append(x["id"])
    expected = {}
    for s in surface["slots"]:
        v = gs.solver_value(s, eng.truth, surface)
        expected[s["id"]] = "graded from the writes" if v is gs.NOT_SOLVER else v
    live = tlv.run(manifest or {}, sql_text, prompt.read_text() if prompt and prompt.is_file() else "")
    ldisp = tlv.dispositions(live, disp.get("liveness") or {})
    fc = {"status": "not run", "note": "advisory: pre-register a forecast with tools/hardness_forecast.py --preregister"}
    if forecast and forecast.is_file():
        f = json.loads(forecast.read_text())
        fc = {"status": "recorded", "file": _where(forecast, task_dir), "sha256": _sha(forecast), "label": f.get("label"),
              "preregistration": f.get("preregistration"), "summary": f.get("summary")}
    blocking = {
        "solver_contract": contract["verdict"] == "PASS",
        "surface_validation": sval["verdict"] == "PASS",
        "mutation_dispositions": not mdisp["missing"],
        "geometry_upper_bound": all(v["U"]["verdict"] in ("PASS", "UNVERIFIED") for v in geo["views"].values())
        and not gdisp["missing"],                     # UNVERIFIED only with its written disposition (M2)
    }
    advisory = {
        "geometry_margin": {v: x["L_max"]["verdict"] for v, x in geo["views"].items()},
        "geometry_bound_verdict": {v: x["U"].get("bound_verdict") for v, x in geo["views"].items()},
        "liveness_dispositions_missing": ldisp["missing"],
        "forecast": fc["status"],
    }
    return {
        "kind": KIND, "version": 1, "tool": VERSION, "label": "probabilistic parts UNCALIBRATED · advisory",
        "revision": eng.revision, "verdict": "PASS" if all(blocking.values()) else "FAIL",
        "blocking": blocking, "advisory": advisory,
        "bound_to": {"sql": {"path": _where(sql, task_dir), "sha256": _sha(sql)},
                     "solver": {"path": _where(solver, task_dir), "sha256": _sha(solver)},
                     "surface": {"path": _where(surface_path, task_dir), "sha256": _sha(surface_path)},
                     "manifest": {"path": _where(manifest_path, task_dir), "sha256": _sha(manifest_path)},
                     "dispositions": {"path": _where(dispositions_path, task_dir), "sha256": _sha(dispositions_path)}},
        "solver_contract": {k: contract.get(k) for k in ("verdict", "checks", "solver_sha256", "sql_sha256", "truth_sha256",
                                                         "rules")},
        "surface": {"validation": sval, "expected": expected, "flipped_by": flipped_by},
        "mutation": {"key_locality": eng.locality(), "mutants": mut["rules"] + mut["degrades"],
                     "shards": {"count": len(mut["shards"]), "source": mut["shard_source"],
                                "diagnostics": {d: sum(1 for x in mut["shards"] if x["diagnostic"] == d)
                                                for d in ("KILLED", "WEAK", "SURVIVED", "EQUIVALENT")}},
                     "interventions": inter, "dispositions": mdisp},
        "geometry": dict(geo, dispositions=gdisp),
        "liveness": {"label": live["label"], "summary": live["summary"], "nodes": [
            {"id": n["id"], "flagged": n["flagged"]} for n in live["nodes"]] + [
            {"id": n["id"], "flagged": n["flagged"]} for n in live.get("authority_decoys", [])], "dispositions": ldisp},
        "forecast": fc,
    }


def to_markdown(rep: dict) -> str:
    b, a = rep["blocking"], rep["advisory"]
    lines = [f"# 01c Preflight Report — {rep['verdict']}", "",
             f"Revision {rep['revision']}; SQL `{rep['bound_to']['sql']['sha256'][:12]}`, solver "
             f"`{(rep['bound_to']['solver']['sha256'] or '')[:12]}`, surface `{(rep['bound_to']['surface']['sha256'] or '')[:12]}`."
             " Probabilistic parts are UNCALIBRATED and advisory.", "",
             "| Part | Status | Blocking |", "|---|---|---|",
             f"| Solver contract (S4b) | {'PASS' if b['solver_contract'] else 'FAIL'} | yes |",
             f"| Gradable surface validation | {'PASS' if b['surface_validation'] else 'FAIL'} | yes |",
             f"| Mutation dispositions (S5b) | {len(rep['mutation']['dispositions']['recorded'])}/"
             f"{len(rep['mutation']['dispositions']['required'])} recorded | yes |",
             f"| Geometry U (S5b′) | " + ", ".join(f"{v} U {rep['geometry']['U']:.3f} {x['U']['verdict']}"
                                                    for v, x in rep["geometry"]["views"].items()) + " | yes |",
             f"| Geometry margin L_max | {a['geometry_margin']} | no |",
             f"| Liveness dispositions (S5c) | {len(a['liveness_dispositions_missing'])} missing | no |",
             f"| Forecast (S5e) | {a['forecast']} | no |", ""]
    lines.append("## Mutants")
    for x in rep["mutation"]["mutants"]:
        d = rep["mutation"]["dispositions"]["recorded"].get(x["id"])
        lines.append(f"- `{x['id']}` {x['diagnostic']} (flipped weight {x['flipped_weight']}) — "
                     + (f"{d['disposition']}: {d['reason']}" if d else "**disposition missing**"))
    for x in rep["mutation"]["interventions"]:
        d = rep["mutation"]["dispositions"]["recorded"].get(x["id"])
        lines.append(f"- `{x['id']}` {x.get('status')} — " + (f"{d['disposition']}: {d['reason']}" if d else
                                                                "**disposition missing**" if "status" in x else ""))
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------ self-test

def _self_test() -> None:
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("preflight_report_selftest_") as tmp:
        t = Path(tmp)
        (t / "solver.py").write_text(dm._SOLVER)
        (t / "inject.sql").write_text(dm._SQL)
        surf = dm._surface()
        surf["deliverables"] = {"register": {"kind": "table", "name_regex": "register", "key_column": "key",
                                             "key_regex": r"K-\d{2}", "columns": ["key", "count", "note", "flag", "class"],
                                             "class_column": "class"},
                                # the group slot needs a written source for surface.gradeable's dry run
                                "tracker": {"kind": "text", "tool": "linear_update_issue", "issue": "T-1",
                                            "key_regex": r"K-\d{2}", "groups": [["counted", "counted"]]}}
        for s in surf["slots"]:
            s.update(work_kind={1: "lookup", 3: "interpretation", 5: "multi_source_reconciliation"}[s["weight"]],
                     work_reason="fixture")
            if s["id"] in ("S1", "S2", "S5"):
                s["role"] = "sample"
        surf["slots"].append({"id": "S8", "weight": 1, "work_kind": "lookup", "work_reason": "fixture", "class": "delivery",
                              "selector": ["delivery", "register_keys_exact"], "role": "volume", "volume_for": ["register:*"]})
        surf["truth_keys"] = ["K-01"]                 # surface.gradeable needs an explicit register key set
        (t / "surface.json").write_text(json.dumps(surf))
        man = {"traps": [{"id": f"T{i}"} for i in range(1, 5)], "chains": []}
        (t / "manifest.json").write_text(json.dumps(man))
        kw = dict(solver=t / "solver.py", sql=t / "inject.sql", surface_path=t / "surface.json",
                  manifest_path=t / "manifest.json", prompt=None, dispositions_path=t / "d.json",
                  context={"spec_version": "V3", "difficulty_mode": "hard"})
        rep = build(**kw)
        assert rep["verdict"] == "FAIL" and rep["blocking"] == {"solver_contract": True, "surface_validation": True,
                                                                 "mutation_dispositions": False,
                                                                 "geometry_upper_bound": True}, rep["blocking"]
        need = rep["mutation"]["dispositions"]["required"]
        (t / "d.json").write_text(json.dumps({"mutation": {i: {"disposition": "live", "reason": "fixture"} for i in need}}))
        rep = build(**kw)
        assert rep["verdict"] == "PASS", rep["blocking"]
        assert rep["surface"]["flipped_by"]["S1"] == ["rule:late"] and rep["surface"]["expected"]["S1"] == "HOLD", rep["surface"]
        assert rep["surface"]["expected"]["S6"] == "graded from the writes"
        assert rep["bound_to"]["dispositions"]["sha256"] and rep["forecast"]["status"] == "not run"
        thin = dict(surf, slots=surf["slots"] + [{"id": f"D{i}", "weight": 5, "work_kind": "multi_source_reconciliation",
                                                  "work_reason": "fixture", "class": "delivery",
                                                  "selector": ["delivery", "slide_updated"]} for i in range(9)])
        (t / "surface.json").write_text(json.dumps(thin))
        rep = build(**kw)
        assert rep["verdict"] == "FAIL" and not rep["blocking"]["geometry_upper_bound"], rep["blocking"]
        assert "# 01c Preflight Report — FAIL" in to_markdown(rep)
    # planted: --max-k above 8 without --allow-max-k is UNSUPPORTED before any work (exit 2)
    import contextlib
    import io
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        assert main(["--max-k", "12"]) == 2
    assert "UNSUPPORTED" in err.getvalue() and "--allow-max-k 12" in err.getvalue(), err.getvalue()
    print("self-test: ok (contract + surface + mutation dispositions + geometry block, expected values and flipped_by, "
          "file bindings, advisory parts never gate)")


# ------------------------------------------------------------------ main

def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="preflight_report.py", description="the injection preflight report (see docstring)")
    ap.add_argument("--task-dir", type=Path)
    ap.add_argument("--solver", type=Path)
    ap.add_argument("--sql", type=Path)
    ap.add_argument("--surface", type=Path)
    ap.add_argument("--manifest", type=Path)
    ap.add_argument("--prompt", type=Path)
    ap.add_argument("--dispositions", type=Path)
    ap.add_argument("--previous-sql", type=Path)
    ap.add_argument("--previous-truth", type=Path)
    ap.add_argument("--forecast", type=Path)
    ap.add_argument("--views", choices=("auto", "v2", "v3", "both"), default="auto")
    ap.add_argument("--max-k", type=int, default=dm.MAX_K)
    ap.add_argument("--allow-max-k", type=int, metavar="N", help="the explicit, disclosed override for --max-k N > 8")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        _self_test()
        return 0
    try:
        max_k, disclosure = dm.resolve_max_k(a.max_k, a.allow_max_k)        # default 8; above only disclosed
    except dm.Unsupported as exc:
        print(f"preflight_report: {exc}", file=sys.stderr)
        return 2
    if disclosure:
        print(f"preflight_report: {disclosure}", file=sys.stderr)
    td = a.task_dir
    wf = td / "Working_Files" if td else None
    solver = a.solver or (wf / "solver" / "solver.py" if wf else None)
    sql = a.sql or (td / "01_Universe_Inject.sql" if td else None)
    surface = a.surface or (wf / "01_Gradable_Surface.json" if wf else None)
    manifest = a.manifest or (wf / "01_Hardness_Manifest.json" if wf else None)
    prompt = a.prompt or (td / "04_Prompt.txt" if td else None)
    disp = a.dispositions or (wf / "01c_Dispositions.json" if wf else None)
    for name, p in (("solver", solver), ("sql", sql), ("surface", surface)):
        if not p or not p.is_file():
            print(f"preflight_report: no {name} (give --{name} or --task-dir)", file=sys.stderr)
            return 2
    rep = build(solver=solver, sql=sql, surface_path=surface, manifest_path=manifest, prompt=prompt, dispositions_path=disp,
                previous_sql=a.previous_sql, previous_truth=a.previous_truth, forecast=a.forecast, views=a.views,
                context=dm._context(td), max_k=max_k, task_dir=td)
    rep["max_k"], rep["max_k_override"] = max_k, disclosure
    out = a.out or (wf / "01c_Preflight_Report.json" if wf else None)
    if out:
        out = tl.safe_out(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rep, indent=1, ensure_ascii=False, default=sorted) + "\n")
        out.with_suffix(".md").write_text(to_markdown(rep))
    if a.json:
        print(json.dumps(rep, indent=1, ensure_ascii=False, default=sorted))
    else:
        print(f"PREFLIGHT: {rep['verdict']} · blocking {rep['blocking']} · advisory {rep['advisory']}")
        if out:
            print(f"wrote {tl._rel(out)} and {tl._rel(out.with_suffix('.md'))}")
    return 0 if rep["verdict"] == "PASS" else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"preflight_report: {error}", file=sys.stderr)
        raise SystemExit(2)

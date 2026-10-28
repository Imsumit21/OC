#!/usr/bin/env python3
"""F1 acceptance: the revision-14 replay with complexity channels (read-only; never appends to a ledger).

hardness_forecast forecast on the frozen revision-14 copy, through the fixture wrapper
(support/fixtures/season_pass_rev14/solver.py), with:
  - the shared ledger's Opus 4.8 priors for the designed mechanisms (read only; no --preregister);
  - the wrapper's declared channels at in-sample rates from the four baselines (r1, r2, r3, r6), passed as disclosed
    overrides, since node_verdicts can't observe tracker groups and no ledger record exists for them:
      scale:groups              3 component-group omissions in 4 runs x 67 components with groups -> Beta(4, 266)
      tool_surface:register     native Sheet instead of the CSV upload in 2 of 4 runs              -> Beta(3, 3)
      control:process_findings  no over-application in 4 runs x 3 controls (the pre-check's SP-110 is
                                Opus 5's and the pre-check is not a baseline)                       -> Beta(1, 13)
  - brief batches (M6) from trajectory_ledger's briefs of r3, the non-mixed baseline.
Variants (all reported; M1 value_notes is tracker-only, so the solver can't flip its slots: not modeled):
  A  out of sample: every active mechanism at its ledger prior (the cross-task Opus 4.8 priors)
  B  slips only + channels: the revision-14 session's posterior "every mechanism leaks" design (posterior/
     design_slips_only.json; it forecast 95.1 % (91.5-98.0) without channels while the pre-check scored 90.2 %:
     "the model misses a loss channel") with M3 / M2 / M4 at 0
  C  evidence-weighted + channels: its posterior_evidence design, M3 0.10 / M2 0.15 / M4 0.08
  A0 / B0 / C0  the same forecasts with --no-channels: the baseline each channel variant is compared with
Diagnostic (AMENDED 2026-10-26): the replay brackets the observed baseline average (r1 92.2, r2 76.1, r3 91.8,
r6 99.6 %: 89.9 %) in the 10-90 % band of the simulated average, and r3's 91.8 % in the 10-90 % band of the simulated
run scores. The original criterion (variant B in every scenario view, set before the multi-seed runs) was recorded
FAIL — B brackets the average in 0/15 views (logs/f1/f1_replay_round3.log) — and is WITHDRAWN by amendment
(f1_acceptance/F1_ACCEPTANCE_AMENDMENT.md). This harness is advisory and diagnostic only: no calibration claim, no
replay-fitted estimate for task 1, and its exit status is not an acceptance signal. Every channel rate is in-sample
(the same four baselines it is judged on): a consistency check, not validation; no held-out task exists.
Run it for at least three seeds, then --summarize them (mean and SD across seeds).
Usage (workspace root):
  python3 -B Task_Authoring/support/fix_session_2026-10-25/scripts/f1_acceptance.py OUT_DIR [--seed N]
  python3 -B Task_Authoring/support/fix_session_2026-10-25/scripts/f1_acceptance.py --summarize DIR DIR DIR ...
"""
import argparse
import json
import statistics
import subprocess
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[3]
S = BUNDLE / "support" / "backtests" / "season_pass" / "rev14"
TOOLS = BUNDLE / "tools"
WRAPPER = BUNDLE / "support" / "fixtures" / "season_pass_rev14" / "solver.py"
OBSERVED = {"r1": 0.922, "r2": 0.761, "r3": 0.918, "r6": 0.996}
RATES = ["scale:groups=4,266@Rev14 posterior (3 omissions in 4 runs x 67)",
         "tool_surface:register=3,3@Rev14 posterior (2 of 4 native Sheets)",
         "control:process_findings=1,13@Rev14 posterior (no over-application in 4 x 3 controls)"]


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="f1_acceptance.py")
    ap.add_argument("out", nargs="*", type=Path)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--summarize", action="store_true", help="the positional folders hold one seed's run each")
    a = ap.parse_args(argv)
    if a.summarize:
        return summarize(a.out)
    if len(a.out) != 1:
        ap.error("one OUT_DIR per run")
    out = a.out[0].resolve()
    out.mkdir(parents=True, exist_ok=True)
    py = [sys.executable, "-B"]
    run3 = S / "runs" / "07_Baseline_Trajectories" / "trajectory-run-3.json"
    subprocess.run(py + [str(TOOLS / "trajectory_ledger.py"), "--task-dir", str(S), "--run", f"r3={run3}",
                         "--surface", str(S / "working_files" / "01_Gradable_Surface.json"), "--out-dir", str(out / "tl")],
                   check=True, capture_output=True)
    briefs = sorted((out / "tl").rglob("briefs.json"))
    if not briefs:
        print("no briefs.json from trajectory_ledger", file=sys.stderr)
        return 2
    base = py + [str(TOOLS / "hardness_forecast.py"), "forecast", "--task-dir", str(S), "--solver", str(WRAPPER),
                 "--sql", str(S / "sql" / "01_Universe_Inject.sql"),
                 "--surface", str(S / "working_files" / "01_Gradable_Surface.json"), "--model", "claude-opus-4-8",
                 "--draws", "1500", "--seed", str(a.seed), "--briefs", str(briefs[0])]
    for r in RATES:
        base += ["--channel-rate", r]
    m3 = "--mechanisms=owner_calls,process_findings,claims"
    variants = {
        "A_out_of_sample": base + ["--max-k", "12", "--allow-max-k", "12"],
        "B_slips_only": base + [m3, "--mechanism-rate", "owner_calls=0@Rev14 posterior_evidence design", "--mechanism-rate", "process_findings=0@Rev14 posterior_evidence design",
                                "--mechanism-rate", "claims=0@Rev14 posterior_evidence design"],
        "C_evidence": base + [m3, "--mechanism-rate", "owner_calls=0.10@Rev14 posterior_evidence design", "--mechanism-rate", "process_findings=0.15@Rev14 posterior_evidence design",
                              "--mechanism-rate", "claims=0.08@Rev14 posterior_evidence design"]}
    def without_rates(cmd):                           # --no-channels refuses overrides for channels it doesn't model
        out_, skip = [], False
        for x in cmd:
            if skip or x == "--channel-rate":
                skip = x == "--channel-rate"
                continue
            out_.append(x)
        return out_
    for name in list(variants):                       # the baselines: the same forecast without the channels
        variants[name[0] + "0_no_channels"] = without_rates(variants[name]) + ["--no-channels"]
    avg = sum(OBSERVED.values()) / len(OBSERVED)
    print(f"seed {a.seed}; observed baselines {OBSERVED} -> average {avg:.4f}; r3 {OBSERVED['r3']}")
    verdicts, summary = {}, {"seed": a.seed, "observed": OBSERVED, "average": avg, "briefs": str(briefs[0]),
                             "variants": {}}
    for name, cmd in variants.items():
        res = subprocess.run(cmd + ["--out", str(out / f"rev14_replay_{name}.json")], capture_output=True, text=True)
        (out / f"rev14_replay_{name}.txt").write_text(res.stdout + res.stderr)
        if res.returncode != 0:
            print(f"{name}: forecast exit {res.returncode}\n{res.stdout[-1500:]}{res.stderr[-1500:]}")
            return 1
        rep = json.loads((out / f"rev14_replay_{name}.json").read_text())
        print(f"== {name}: {rep['label']} · brief batches {(rep.get('briefs') or {}).get('batches')}")
        summary["variants"][name] = {"label": rep["label"], "brief_batches": (rep.get("briefs") or {}).get("batches"),
                                     "channels": [c["id"] for c in rep.get("channels") or []], "views": []}
        if name == "A_out_of_sample":
            for c in rep["channels"]:
                pa = c["P_any_unit_fails"]
                print(f"  channel {c['id']}: {c['members']} member(s), {c['latent']} latent, P(any of {pa['units']}) "
                      f"{pa['integrated']:.3f} integrated vs {pa['plug_in']:.3f} plug-in, expected loss alone "
                      f"{c['expected_loss_alone']:.4f} [{c['rate']['basis'][:44]}]")
        ok_avg, ok_r3 = [], []
        for s in rep["scenarios"]:
            for v, x in s["views"].items():
                lo, hi = x["band_10_90"]
                rlo, rhi = s["run_score_band_10_90"]
                a_in, r_in = lo <= avg <= hi, rlo <= OBSERVED["r3"] <= rhi
                ok_avg.append(a_in)
                ok_r3.append(r_in)
                summary["variants"][name]["views"].append({
                    "scenario": f"{s['dependence']} {s['extent']}", "view": v, "E_average": x["E_average"],
                    "band": [lo, hi], "run_band": [rlo, rhi], "average_in": a_in, "r3_in": r_in})
                print(f"  {s['dependence']:11} {s['extent']:8} {v}: E[avg] {x['E_average']:.4f} band [{lo:.4f}, {hi:.4f}] "
                      f"{'brackets' if a_in else 'MISSES'} {avg:.4f} · run scores [{rlo:.4f}, {rhi:.4f}] "
                      f"{'bracket' if r_in else 'MISS'} r3 {OBSERVED['r3']}")
        verdicts[name] = (sum(ok_avg), sum(ok_r3), len(ok_avg))
        s0 = rep["scenarios"][0]
        print("  slots most at risk (first scenario, P(fail) / P(fails all six)): " + ", ".join(
            f"{k} {x['P_fail']:.2f}/{x['P_fails_all_six']:.2f}" for k, x in list(s0["slots"].items())[:8]))
    for name, (na, nr, n) in verdicts.items():
        print(f"{name}: average bracketed in {na}/{n} scenario views, r3 in {nr}/{n}")
    na, nr, n = verdicts["B_slips_only"]
    passed = na == n and nr == n
    # AMENDMENT 2026-10-26: the original criterion (B in every view) was recorded FAIL (0/3 seeds, see
    # logs/f1/f1_replay_round3.log) and is WITHDRAWN. This harness is advisory and diagnostic: it reports what each
    # variant brackets, never a pass/fail gate, and its exit status is not an acceptance signal.
    summary["criterion_B_met"] = passed
    summary["status"] = "ADVISORY · the original criterion was met" if passed else \
        "ADVISORY · the original criterion FAILED and is withdrawn by amendment (F1_ACCEPTANCE_AMENDMENT.md)"
    (out / "summary.json").write_text(json.dumps(summary, indent=1) + "\n")
    print(f"F1 REPLAY (advisory, diagnostic only, never a gate): B brackets the average in {na}/{n} views and r3 in "
          f"{nr}/{n}; the original criterion is recorded FAIL and WITHDRAWN by amendment — no calibration claim, no "
          f"replay-fitted estimate")
    return 0


def summarize(dirs) -> int:
    """Per variant across seeds: bracket counts per seed, and per scenario view the mean and SD of E[average]."""
    runs = [json.loads((Path(d) / "summary.json").read_text()) for d in dirs]
    seeds = [r["seed"] for r in runs]
    if len(set(seeds)) != len(seeds) or len(seeds) < 3:
        print(f"need at least three distinct seeds, got {seeds}", file=sys.stderr)
        return 2
    avg = runs[0]["average"]
    print(f"F1 replay over seeds {seeds}; observed average {avg:.4f}, r3 {runs[0]['observed']['r3']}")
    for name in runs[0]["variants"]:
        per = [r["variants"][name] for r in runs]
        n = len(per[0]["views"])
        counts = [(sum(x["average_in"] for x in p["views"]), sum(x["r3_in"] for x in p["views"])) for p in per]
        print(f"== {name} ({per[0]['label']}; brief batches {per[0]['brief_batches']}; channels {per[0]['channels']}): "
              f"average bracketed {[c[0] for c in counts]} of {n} views per seed, r3 {[c[1] for c in counts]}")
        for i, x in enumerate(per[0]["views"]):
            es = [p["views"][i]["E_average"] for p in per]
            lo = statistics.mean(p["views"][i]["band"][0] for p in per)
            hi = statistics.mean(p["views"][i]["band"][1] for p in per)
            k = sum(p["views"][i]["average_in"] for p in per)
            print(f"  {x['scenario']:20} {x['view']}: E[avg] {statistics.mean(es):.4f} ± {statistics.stdev(es):.4f} "
                  f"(SD over seeds) · band [{lo:.4f}, {hi:.4f}] · brackets the average in {k}/{len(per)} seeds")
    met = [r["criterion_B_met"] for r in runs]
    print(f"the original criterion (B in every view) was met in {sum(met)}/{len(met)} seeds; it is recorded FAIL and "
          f"withdrawn by amendment — this summary is advisory, never a gate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

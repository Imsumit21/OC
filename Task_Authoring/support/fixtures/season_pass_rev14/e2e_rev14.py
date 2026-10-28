#!/usr/bin/env python3
"""Season Pass revision-14 end-to-end check (E2E, 2026-10-25).

One command runs the five revision-14 platform runs through trajectory_ledger -> node_verdicts -> surface_grader ->
a temp hardness_ledger -> hardness_forecast. Every tool runs inside one selftest_sandbox workspace, and the outcomes
of record are asserted.

Read-only on every input:
  - the frozen copies support/backtests/season_pass/rev14 (runs, SQL, surface, manifest, assignment, context) and
    rev13 (its SQL, so each run binds on evidence between two revisions). Both SHA256SUMS are verified before and
    after, and no file there may be newer than the start;
  - the revision-14 solver: this folder's wrapper over the frozen oracle.
Every output, the task folder the tools read and the temp ledger (the sandbox's copy of support/hardness_ledger) stay
in the sandbox, which is removed afterwards unless --keep. The shared ledger is never written.

Asserts
  surface_grader     the failed-slot sets of rev14/README.md; r3's S43/S44 (8-character SHA prefixes) and S69-S71
                     (slack_conversations_add_message) pass
  trajectory_ledger  every run BOUND to rev14 on evidence; the pre-check v3-invalid and mixed
  node_verdicts      the pre-check: no designed mechanism LANDED and a go-rule count of 0; SP-110 a control trial of
                     M2 (process_findings) OVER-APPLIED, decided by an Opus 5 brief (event 5017 or 6049)
  hardness_ledger    the proposals append, except verdicts pending review (mechanism?), which are refused; control
                     and channel records leave every prior unchanged
  hardness_forecast  a forecast on the temp ledger for the register mechanisms M3, M2 and M4 (independent; whole and
                     r3's brief batches), labelled UNCALIBRATED; its channels take their rates from the control and
                     channel records just appended (scale:groups, invisible in the register, stays UNPARAMETERIZED)

Usage (workspace root): python3 -B Task_Authoring/support/fixtures/season_pass_rev14/e2e_rev14.py [--keep] [--draws N]
Exit 0 = every assertion holds; 1 = one failed; 2 = usage; 3 = a sandbox leak.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parents[2]
S = BUNDLE / "support" / "backtests" / "season_pass"
R14, R13 = S / "rev14", S / "rev13"
sys.path.insert(0, str(BUNDLE / "tools"))
import selftest_sandbox as sx  # noqa: E402
import hardness_ledger as hl  # noqa: E402  (record ids, the design-effect formula: the E2E recomputes them)

SOLVER = HERE / "solver.py"
SQL14, SQL13 = R14 / "sql" / "01_Universe_Inject.sql", R13 / "sql" / "01_Universe_Inject.sql"
RUNS = [("pre", R14 / "runs/06_PreCheck_Trajectory/trajectory-run-1.json")] + \
       [(f"r{i}", R14 / f"runs/07_Baseline_Trajectories/trajectory-run-{i}.json") for i in (1, 2, 3, 6)]
RECORD = {"pre": ["S04", "S05", "S07", "S08", "S40"], "r1": ["S43", "S46", "S47", "S52"],
          "r2": ["S04", "S05", "S07", "S08"] + [f"S{i}" for i in range(38, 47)],
          "r3": ["S01", "S47", "S49", "S52", "S54"], "r6": ["S01"]}          # rev14/README.md, grades of record
MECHANISMS = "owner_calls,process_findings,claims"          # M3, M2, M4; M1 (value_notes) is tracker-only: inert to
                                                            # the solver, so the forecast can't move it (reported)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def verify_frozen(since: float | None = None) -> list:
    """SHA256SUMS of both frozen copies; with `since`, also every file in them modified after it."""
    bad = []
    for root in (R13, R14):
        for line in (root / "SHA256SUMS").read_text().splitlines():
            if line.strip():
                want, name = line.split(None, 1)
                if sha256(root / name.strip().lstrip("*")) != want:
                    bad.append(f"{root.name}/{name.strip()}: hash differs")
        if since is not None:
            for d, _, files in os.walk(root):
                bad += [f"{Path(d, f).relative_to(S)}: modified during the check" for f in files
                        if Path(d, f).stat().st_mtime > since]
    return bad


class Check:
    def __init__(self):
        self.rows = []

    def __call__(self, name: str, ok: bool, detail: str = "") -> bool:
        self.rows.append((bool(ok), name, detail))
        print(f"{'ok  ' if ok else 'FAIL'} {name}" + (f": {detail}" if detail else ""), flush=True)
        return bool(ok)


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="e2e_rev14.py", description=__doc__.split("\n")[0])
    ap.add_argument("--keep", action="store_true", help="keep the sandbox (its path is printed)")
    ap.add_argument("--draws", type=int, default=2000)
    a = ap.parse_args(argv)
    if not sys.dont_write_bytecode:
        print("e2e_rev14: run with python3 -B (the frozen oracle must not get a __pycache__)", file=sys.stderr)
        return 2
    bad = verify_frozen()
    if bad:
        print(f"e2e_rev14: the frozen copies don't verify: {bad[:5]}", file=sys.stderr)
        return 2
    start = time.time()
    check = Check()
    try:
        # Evals/task_inputs is the authoring session's own input folder, never read by this E2E; a concurrent
        # authoring session may write it, so it is excluded from the leak scan (every other linked entry is checked)
        with sx.Sandbox("live", keep=a.keep, ignore_newer=("Evals/task_inputs",)) as sb:
            print(f"[e2e_rev14] sandbox {sb.root.relative_to(BUNDLE)}; inputs read in place from {S.relative_to(BUNDLE)}",
                  flush=True)
            work = sb.bundle / "support" / "scratch" / "e2e_rev14"
            task, out = work / "task", work / "out"
            (task / "Working_Files").mkdir(parents=True)
            out.mkdir(parents=True)
            for src, dst in ((R14 / "00_Assigments.md", "00_Assigments.md"), (R14 / "04_Prompt.txt", "04_Prompt.txt"),
                             (R14 / "working_files/00_Task_Context.json", "Working_Files/00_Task_Context.json"),
                             (R14 / "working_files/01_Gradable_Surface.json", "Working_Files/01_Gradable_Surface.json"),
                             (R14 / "working_files/01_Hardness_Manifest.json", "Working_Files/01_Hardness_Manifest.json")):
                shutil.copy2(src, task / dst)
            surface, manifest = task / "Working_Files/01_Gradable_Surface.json", task / "Working_Files/01_Hardness_Manifest.json"
            ledger = sb.bundle / "support" / "hardness_ledger" / "ledger.jsonl"
            run_args = [f"--run={lab}={p}" for lab, p in RUNS]

            def tool(name, *args, expect=(0,)):
                rc = sb.run([name, *map(str, args)], quiet=True)
                if rc not in expect:
                    print(f"     {name} exit {rc}:\n{sb.last['stdout'][-1500:]}{sb.last['stderr'][-1500:]}", flush=True)
                return rc, sb.last["stdout"]

            # 1. trajectory_ledger: provenance and binding on evidence
            rc, so = tool("trajectory_ledger.py", "--task-dir", task, *run_args, "--surface", surface,
                          "--sql", f"rev14={SQL14}", "--sql", f"rev13={SQL13}", "--prompt", task / "04_Prompt.txt",
                          "--out-dir", out / "forensics", "--json")
            led = {s["label"]: s for s in json.loads(so)} if rc == 0 else {}
            check("trajectory_ledger ran", rc == 0 and set(led) == {lab for lab, _ in RUNS})
            binds = {lab: (s["binding"]["verdict"], s["binding"].get("bound_to")) for lab, s in led.items()}
            check("every run BOUND to rev14 on evidence", binds and all(v == ("BOUND", ["rev14"]) for v in binds.values()),
                  str(binds))
            pre = (led.get("pre") or {}).get("provenance") or {}
            check("the pre-check is v3-invalid and mixed", pre.get("v3_valid") is False and pre.get("mixed_model") is True,
                  f"v3_valid {pre.get('v3_valid')}, mixed {pre.get('mixed_model')}, models "
                  f"{(pre.get('model_check') or {}).get('models')}")

            # 2. node_verdicts: landings, control trials, the go rule
            rc, _ = tool("node_verdicts.py", "--task-dir", task, "--solver", SOLVER, "--sql", f"rev14={SQL14}",
                         "--sql", f"rev13={SQL13}", *run_args, "--surface", surface, "--manifest", manifest,
                         "--task", "season_pass", "--ledger-out", out / "proposals.jsonl", "--out", out / "verdicts.json")
            nv = json.loads((out / "verdicts.json").read_text()) if rc == 0 else {"runs": {}}
            check("node_verdicts ran", rc == 0 and set(nv["runs"]) == {lab for lab, _ in RUNS})
            pv = nv["runs"].get("pre") or {}
            landed = {r: v["landed_keys"] for r, v in (pv.get("rules") or {}).items() if v["verdict"] == "LANDED"}
            go = pv.get("go_rule") or {}
            check("the pre-check has 0 designed landings", pv and not landed and go.get("independent_channels") == 0,
                  f"LANDED {landed or 'none'}; go rule {go.get('independent_channels')} "
                  f"{go.get('not_counted', {}).get('control_over_applications')}")
            trials = {x["key"]: x for x in ((pv.get("controls") or {}).get("process_findings") or {}).get("trials", [])}
            t110 = trials.get("SP-110") or {}
            check("SP-110 is an M2 control record from an Opus 5 brief",
                  t110.get("outcome") == "OVER-APPLIED" and t110.get("via") == "brief"
                  and t110.get("deciding_event") in (5017, 6049) and t110.get("deciding_model") == "claude-opus-5"
                  and (pv.get("rules") or {}).get("process_findings", {}).get("mechanism") == "M2",
                  f"{t110.get('outcome')} {t110.get('written')} (truth {t110.get('truth')}), decided by the "
                  f"{t110.get('via')} at event {t110.get('deciding_event')} ({t110.get('deciding_model')}); briefs "
                  f"{t110.get('briefs')}")
            for lab in ("r1", "r2", "r3", "r6"):
                rv = nv["runs"].get(lab) or {}
                print(f"     {lab}: LANDED "
                      f"{ {r: v['landed_keys'] for r, v in (rv.get('rules') or {}).items() if v['verdict'] == 'LANDED'} or 'none'}"
                      f"; controls over-applied "
                      f"{ {r: c['over_applied'] for r, c in (rv.get('controls') or {}).items() if c['over_applied']} or 'none'}"
                      f"; pending review "
                      f"{ {r: v['pending_review_keys'] for r, v in (rv.get('rules') or {}).items() if v['pending_review_keys']} or 'none'}"
                      f"; go rule {(rv.get('go_rule') or {}).get('independent_channels')}", flush=True)

            # 3. surface_grader: the grades of record
            rc, _ = tool("surface_grader.py", "--task-dir", task, "--surface", surface, "--solver", SOLVER, "--sql", SQL14,
                         *run_args, "--views", "both", "--out", out / "grades.json")
            gr = json.loads((out / "grades.json").read_text()) if rc == 0 else {"runs": {}}
            failed = {lab: r["failed_slots"] for lab, r in gr["runs"].items()}
            check("surface_grader: the failed-slot sets of record", failed == RECORD,
                  "; ".join(f"{lab} {r['score']:.1%} {r['failed_slots']}" for lab, r in gr["runs"].items()))
            r3 = (gr["runs"].get("r3") or {}).get("results") or {}
            check("r3's S43/S44 and S69-S71 pass", all(r3.get(s) is True for s in ("S43", "S44", "S69", "S70", "S71")),
                  str({s: r3.get(s) for s in ("S43", "S44", "S69", "S70", "S71")}))

            # 4. the temp ledger (the sandbox's copy): control and channel records never move a prior
            recs = [json.loads(x) for x in (out / "proposals.jsonl").read_text().splitlines() if x.strip()] if \
                (out / "proposals.jsonl").is_file() else []
            side = [x for x in recs if x["kind"] in ("control", "channel")]
            verdicts = [x for x in recs if x["kind"] == "verdict"]
            (out / "side.jsonl").write_text("".join(json.dumps(x) + "\n" for x in side))
            (out / "verdicts.jsonl").write_text("".join(json.dumps(x) + "\n" for x in verdicts))
            models = sorted({x["model"] for x in recs})

            def priors():
                got = {}
                for m in models:
                    rc_, so_ = tool("hardness_ledger.py", "--ledger", ledger, "priors", "--model", m, "--json")
                    fams = json.loads(so_)["families"] if rc_ == 0 else None
                    got[m] = {f: (v["alpha"], v["beta"], tuple(v["record_ids"])) for f, v in fams.items()} \
                        if fams is not None else None
                return got
            p0 = priors()
            rc, so = tool("hardness_ledger.py", "--ledger", ledger, "append", out / "side.jsonl")
            side_ids = {hl.record_id(x) for x in side}
            side_ok = rc == 0 and side_ids <= {json.loads(x)["id"] for x in ledger.read_text().splitlines() if x.strip()}
            p1 = priors()
            before_ids = {json.loads(x)["id"] for x in ledger.read_text().splitlines() if x.strip()}
            check("the temp ledger takes the control and channel records; no prior moves",
                  rc == 0 and side_ok and p0 == p1 and all(v is not None for v in p0.values())
                  and bool(p0.get("claude-opus-4-8")),
                  f"{len(side)} record(s) ({sum(x['kind'] == 'control' for x in side)} control, "
                  f"{sum(x['kind'] == 'channel' for x in side)} channel); models {models}; "
                  f"{len(p0.get('claude-opus-4-8') or {})} Opus 4.8 families compared")
            rc, so = tool("hardness_ledger.py", "--ledger", ledger, "append", out / "verdicts.jsonl", expect=(0, 1))
            pending = sorted(f"{x['run']}:{x['node']}" for x in verdicts if (x.get("features") or {}).get("pending_review"))
            expected_pending = {"r2:acceptance", "r2:history"}       # the fixture's known pending reviews
            pend_ids = {hl.record_id(x) for x in verdicts if (x.get("features") or {}).get("pending_review")}
            ok_ids = {hl.record_id(x) for x in verdicts if not (x.get("features") or {}).get("pending_review")}
            rejected_lines = [line for line in so.splitlines() if "REJECTED " in line]
            pending_refused = len(rejected_lines) == len(pend_ids) and \
                all("pending review" in line for line in rejected_lines)
            in_ledger = {json.loads(x)["id"] for x in ledger.read_text().splitlines() if x.strip()}
            after_exact = in_ledger == before_ids | ok_ids and not (pend_ids & in_ledger)
            head = next((line for line in so.splitlines() if line.startswith("added ")), "")
            nums = [int(x) for x in re.findall(r"\d+", head)]
            counts_ok = len(nums) >= 3 and nums[0] + nums[1] == len(ok_ids) and nums[2] == len(pend_ids)
            check("the verdict proposals append; exactly the pending reviews are refused",
                  rc == (1 if pending else 0) and set(pending) == expected_pending and pending_refused and counts_ok
                  and after_exact,
                  f"{len(verdicts)} verdict(s); accepted {len(ok_ids)}, pending {pending or 'none'} (known: "
                  f"{sorted(expected_pending)}); rejected lines {len(rejected_lines)} all pending review: "
                  f"{pending_refused}; ledger ids exactly before + accepted: {after_exact}; append head {head[:80]!r}")
            p2 = priors()
            moved = {m: {f: [(p1.get(m) or {}).get(f, (None, None))[:2], p2[m][f][:2]] for f in (p2.get(m) or {})
                         if (p2[m] or {}).get(f) != (p1.get(m) or {}).get(f)} for m in models}
            r3_fams = sorted({x["family"] for x in verdicts if x["run"] == "r3" and x["verdict"] != "NOT-REACHED"})
            check("the verdicts move only the families of the non-mixed run r3 (mixed runs stay out by default)",
                  set(moved.get("claude-opus-4-8") or {}) == set(r3_fams) and not moved.get("claude-opus-5"),
                  f"moved {moved}; r3 families {r3_fams}")

            # 5. hardness_forecast on the temp ledger
            briefs = sorted(p for p in (out / "forensics").rglob("briefs.json") if "r3" in p.parts)
            rc, _ = tool("hardness_forecast.py", "forecast", "--task-dir", task, "--model", "claude-opus-4-8",
                         "--solver", SOLVER, "--sql", SQL14, "--surface", surface, "--ledger", ledger,
                         "--mechanisms", MECHANISMS, "--draws", a.draws, "--task", "season_pass", "--out", out / "forecast.json",
                         "--dependence", "independent", "--extent", "whole", "--extent", "batches",
                         *([f"--briefs={briefs[0]}"] if briefs else []))
            fc = json.loads((out / "forecast.json").read_text()) if rc == 0 else {}
            sc = (fc.get("scenarios") or [{}])[0]
            views = {v: {"P_all": x.get("P_all"), "E_average": x.get("E_average") or x.get("e_average")}
                     for v, x in (sc.get("views") or {}).items()}
            check("hardness_forecast ran on the temp ledger, UNCALIBRATED", rc == 0 and "UNCALIBRATED" in json.dumps(fc),
                  f"mechanisms {[(m['id'], m['family']) for m in fc.get('mechanisms') or []]}; first scenario "
                  f"{sc.get('dependence')}/{sc.get('extent')}: {views}; brief batches {(fc.get('briefs') or {}).get('batches')}")
            # F1: each channel's rate must be exactly the eligible ledger records of its family, with the Beta the
            # documented formula gives (recomputed here, not read from the tool); cross-task pooling allowed, a stale
            # or wrong-family record is not
            current = [json.loads(x) for x in ledger.read_text().splitlines() if x.strip()]
            current = [r for r in current if r["kind"] in ("channel", "control")]
            fed = {c["id"]: c for c in fc.get("channels") or []}
            unpar = [c["id"] for c in fc.get("unparameterized_channels") or []]
            expected_family = {"tool_surface:register": "tool_surface", "control:process_findings": "A15"}

            def eligible(family):
                return [r for r in current if r.get("family") == family
                        and hl.model_family(r.get("model")) == "claude-opus-4-8"
                        and not (r.get("features") or {}).get("mixed_model")]

            def expected_beta(recs, channel):
                groups = {}
                for r in recs:
                    groups.setdefault(r["task"], set()).add((r.get("revision"), r.get("run")))
                a = b = 0.0
                for task, runs in groups.items():
                    deff = hl.design_effect(len(runs), hl.RHO)
                    for r in [x for x in recs if x["task"] == task]:
                        c = r.get("counts") or {}
                        n = int(c.get("n") if c.get("n") is not None else (c.get("members") or 1))
                        f = int(c.get("failed") or 0) if channel else int(r["verdict"] == "OVER-APPLIED")
                        a += f / deff
                        b += (n - f) / deff
                return round(1 + a, 4), round(1 + b, 4)

            exact = {}
            for cid, c in fed.items():
                recs = eligible(expected_family.get(cid, ""))
                want = {r["id"] for r in recs}
                got = set(c["rate"]["records"])
                beta = expected_beta(recs, c["kind"] != "control") if recs else None
                exact[cid] = (got == want, beta, (round(c["rate"].get("alpha", -1), 4), round(c["rate"].get("beta", -1), 4)))
            check("hardness_forecast: each channel's rate is exactly the eligible records of its family (F1)",
                  set(fed) == set(expected_family) and set(unpar) == {"scale:groups"}
                  and all(ok and beta is not None and beta == gotb for ok, beta, gotb in exact.values()) and bool(briefs)
                  and ((fc.get("briefs") or {}).get("batches") or 0) > 0,
                  "; ".join(f"{k} records match {v[0]}, Beta {v[2]} vs expected {v[1]}" for k, v in exact.items())
                  + f"; UNPARAMETERIZED {unpar}; briefs {[b.parent.name for b in briefs]} "
                  f"({(fc.get('briefs') or {}).get('batches')} brief batches)")
            if a.keep:
                print(f"[e2e_rev14] kept: {sb.root}")
    except sx.Leak as exc:
        print(f"[e2e_rev14] LEAK: {exc}", file=sys.stderr)
        return 3
    after = verify_frozen(since=start)
    check("the frozen copies are unchanged (SHA256SUMS, nothing newer than the start)", not after, "; ".join(after[:4]))
    failed = [n for ok, n, _ in check.rows if not ok]
    print(f"E2E {'PASS' if not failed else 'FAIL'}: {len(check.rows) - len(failed)}/{len(check.rows)} checks"
          + (f"; failed: {failed}" if failed else ""))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

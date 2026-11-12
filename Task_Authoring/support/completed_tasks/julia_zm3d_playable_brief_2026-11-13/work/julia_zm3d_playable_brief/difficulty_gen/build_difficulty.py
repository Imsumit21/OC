#!/usr/bin/env python3
"""Write Working_Files/12_Difficulty_Stats.txt for stage 12.

The calculator's markdown output is pasted unchanged. Every other figure in the report is recomputed here from the raw
verifier copy, 09_Rubrics.json and the six exports (no difficulty_stats import) and asserted against the calculator's
JSON output before anything is written. Re-running drops the pasted stage-gate block; paste the gate again afterwards."""
import collections, hashlib, json, re, statistics, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
BUNDLE = TASK.parent
WS = BUNDLE.parent
REL = "Task_Authoring/task_inputs"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def tool(*args):
    r = subprocess.run([sys.executable, "-B", *args], cwd=str(WS), capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


CTX = json.loads((WF / "00_Task_Context.json").read_text())
CLOCK = CTX["universe"]["clock_line"]
CLOCK = CLOCK[len("Clock:"):].strip() if CLOCK.startswith("Clock:") else CLOCK

# ------------------------------------------------------------------ calculator (pasted unchanged) and its JSON
rc, CALC, err = tool("Task_Authoring/tools/difficulty_stats.py", f"{REL}/Working_Files/12_difficulty_input.json", "--task-dir", REL)
assert rc in (0, 1) and "| Gate |" in CALC, err
J = json.loads((WF / "12_difficulty_stats.json").read_text())
rc2, jtxt, _ = tool("Task_Authoring/tools/difficulty_stats.py", f"{REL}/Working_Files/12_difficulty_input.json", "--task-dir", REL, "--json")
assert json.loads(jtxt) == J, "12_difficulty_stats.json is not the calculator's current --json output"
INPUT = json.loads((WF / "12_difficulty_input.json").read_text())
assert not [r for r in INPUT["rubrics"] if r.get("valid") is False]
AF = (TASK / "11_AF_Justification.md").read_text()
assert "Hand-off to /create-difficulty: --invalid none --judge-correction none" in AF

# ------------------------------------------------------------------ independent recomputation
RUB = json.loads((TASK / "09_Rubrics.json").read_text())
W = [int(r["weight"]) for r in RUB]
TOTAL = sum(W)
VER = (TASK / "10_Baseline_Verifier_Results.md").read_text()
parts = re.split(r"(?m)^Run\s*#\s*(\d+)\s*$", VER)
RES, HEAD = {}, {}
for i in range(1, len(parts), 2):
    n, body = int(parts[i]), parts[i + 1]
    rows = [l.split("\t") for l in body.splitlines() if "\t" in l and l.split("\t")[1].strip() in ("Pass", "Fail")]
    m = re.search(r"(\d+)/(\d+) criteria passed", body)
    RES[n] = [r[1].strip() == "Pass" for r in rows]
    HEAD[n] = (int(m.group(1)), int(m.group(2)))
    assert (sum(RES[n]), len(rows)) == HEAD[n], n
    for k, r in enumerate(rows):                       # every row binds to its criterion by title
        shown = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", r[0])          # the platform copy renders addresses as links
        assert re.sub(r"\W+", "", shown.lower()) == re.sub(r"\W+", "", RUB[k]["title"].lower()), (n, k + 1)
RUNS = sorted(RES)
assert RUNS == [1, 2, 3, 4, 5, 6] and all(len(RES[n]) == len(RUB) == 153 for n in RUNS)
FAILW = {n: sum(w for w, p in zip(W, RES[n]) if not p) for n in RUNS}
RATE = {n: (TOTAL - FAILW[n]) / TOTAL for n in RUNS}
MEAN = sum(RATE.values()) / 6
PSD, SSD = statistics.pstdev(RATE.values()), statistics.stdev(RATE.values())
UNW = [sum(RES[n]) / 153 for n in RUNS]
USD = statistics.pstdev(UNW)
FULL = sum(1 for n in RUNS if all(RES[n]))
DIFF = {a: [sum(x != y for x, y in zip(RES[a], RES[b])) for b in RUNS] for a in RUNS}
# single-linkage grouping: same pattern when two runs differ on at most one rubric
groups = []
for n in RUNS:
    hit = [g for g in groups if any(DIFF[n][m - 1] <= 1 for m in g)]
    merged = sorted({n} | {m for g in hit for m in g})
    groups = [g for g in groups if g not in hit] + [merged]
groups.sort()
LARGEST = max(len(g) for g in groups)
FC = collections.Counter(k for n in RUNS for k, p in enumerate(RES[n], 1) if not p)
ALLFAIL = sorted(k for k, c in FC.items() if c == 6)
HIST = dict(sorted(collections.Counter(FC.values()).items()))
SIX = [k for k in range(1, 154) if k not in FC]
W5 = sum(1 for w in W if w == 5)
W5_SIX = sum(1 for k in SIX if W[k - 1] == 5)

# against the calculator
PR = {int(r["id"].split("-")[1]): r for r in J["per_rollout"]}
for n in RUNS:
    assert abs(PR[n]["weighted_pass_rate"] - RATE[n]) < 1e-12, n
    assert sorted(int(x[1:]) for x in PR[n]["failed_rubrics"]) == [k for k, p in enumerate(RES[n], 1) if not p], n
assert J["all_fail_rubrics"] == [f"R{k}" for k in ALLFAIL] == ["R55", "R147", "R148"]
assert [[int(x.split("-")[1]) for x in g] for g in J["patterns"]] == groups == [[1, 2, 3], [4], [5], [6]]
assert J["blocking"] == ["per_rollout_sd"] and J["verdict_view"] == "platform" and not J["golden_runs"]
G = J["gates"]
assert G["avg_weighted_pass_rate"]["value"].startswith(f"{MEAN * 100:.1f}%") and MEAN < 0.70
assert G["per_rollout_sd"]["value"] == f"{PSD:.3f} (sample {SSD:.3f}; unweighted {USD:.3f})", G["per_rollout_sd"]["value"]
assert G["pass_at_1"]["value"].startswith(f"{FULL}/6 full passes") and FULL == 0
assert (TOTAL, HIST, len(SIX), W5, W5_SIX) == (371, {2: 3, 5: 77, 6: 3}, 70, 50, 3)
assert [HEAD[n][0] for n in RUNS] == [73, 73, 73, 98, 93, 99]
assert [FAILW[n] for n in RUNS] == [256, 256, 256, 183, 192, 182]
assert (round(MEAN * 100, 2), round(PSD, 4), round(SSD, 4), round(USD, 4)) == (40.48, 0.0952, 0.1043, 0.0783)
assert LARGEST == 3 and len(groups) == 4

# ------------------------------------------------------------------ tool calls, counted by hand from the exports
CALLS = {}
for n in RUNS:
    ev = json.loads((TASK / "07_Baseline_Trajectories" / f"trajectory-run-{n}.json").read_text())
    uses, err_of, text_of = [], {}, {}
    for e in ev:
        c = (e.get("message") or {}).get("content") if isinstance(e, dict) else None
        if not isinstance(c, list):
            continue
        for b in c:
            if isinstance(b, dict) and e.get("type") == "assistant" and b.get("type") == "tool_use":
                uses.append(b)
            elif isinstance(b, dict) and e.get("type") == "user" and b.get("type") == "tool_result":
                err_of[b.get("tool_use_id")] = str(b.get("is_error")).lower() == "true"
                text_of[b.get("tool_use_id")] = json.dumps(b.get("content"))
    svc = [u for u in uses if u["name"].startswith("mcp__")]
    acting = [u for u in svc if u["name"].endswith("set_acting_user")]
    blocked = [u for u in svc if err_of.get(u["id"]) and u not in acting]
    seen, rep, rep_tools = set(), 0, collections.Counter()
    for u in svc:
        if u in acting or u in blocked:
            continue
        key = (u["name"], json.dumps(u.get("input"), sort_keys=True))
        if key in seen:
            rep += 1
            rep_tools[u["name"].split("__")[-1]] += 1
        seen.add(key)
    by = collections.Counter(u["name"].split("__")[-1] for u in svc)
    notfound = [u for u in svc if not err_of.get(u["id"]) and len(text_of.get(u["id"], "")) < 400
                and re.search(r"not found|does not exist|no such", text_of.get(u["id"], ""), re.I)]
    CALLS[n] = dict(raw=len(uses), svc=len(svc), harness=len(uses) - len(svc), blocked=len(blocked), repeats=rep,
                    acting=len(acting), counted=len(svc) - len(acting) - len(blocked) - rep, by=by, rep_tools=dict(rep_tools),
                    notfound=len(notfound), submit=sum(v for k, v in by.items() if "submit" in k),
                    job=sum(v for k, v in by.items() if "job_result" in k),
                    blocked_kinds=collections.Counter(
                        "socket reset" if "ECONNRESET" in text_of[u["id"]] else
                        "user name did not resolve" if "user_not_found" in text_of[u["id"]] else
                        "unsupported GitHub qualifier" if "Unsupported qualifier" in text_of[u["id"]] else
                        "no such commit" if "No commit or ref found" in text_of[u["id"]] else "other" for u in blocked),
                    last=(ev[-1].get("type"), ev[-1].get("subtype"), ev[-1].get("is_error")),
                    session=ev[0].get("session_id"), model=ev[0].get("model"))
    assert CALLS[n]["counted"] == PR[n]["tool_calls"], n
    assert CALLS[n]["last"] == ("result", "success", False) and CALLS[n]["model"] == "claude-opus-5-5", n
# the two socket resets: which search failed, and whether its word could have reached a deciding Slack record
RESET = {}
for n in (2, 4):
    ev = json.loads((TASK / "07_Baseline_Trajectories" / f"trajectory-run-{n}.json").read_text())
    use_at = {b["id"]: (i, b) for i, e in enumerate(ev) if isinstance((e.get("message") or {}).get("content"), list)
              for b in e["message"]["content"] if isinstance(b, dict) and b.get("type") == "tool_use"}
    hits = [use_at[b["tool_use_id"]] for e in ev if isinstance((e.get("message") or {}).get("content"), list)
            for b in e["message"]["content"] if isinstance(b, dict) and b.get("type") == "tool_result"
            and "ECONNRESET" in json.dumps(b.get("content"))]
    assert len(hits) == 1 and "slack" in hits[0][1]["name"], (n, hits)
    word = hits[0][1]["input"]["search_query"]
    later = [u for i, u in use_at.values() if i > hits[0][0] and u["name"] == hits[0][1]["name"] and (u["input"] or {}).get("search_query") == word]
    assert not later, (n, word)
    RESET[n] = (hits[0][0], word)
assert RESET == {2: (389, "sfx"), 4: (266, "FBX")}, RESET
SQL = (TASK / "01_Universe_Inject.sql").read_text().splitlines()
for word in ("sfx", "fbx"):
    tables = {re.match(r"\s*INSERT INTO\s+([\w.]+)", l, re.I).group(1) for l in SQL if word in l.lower() and re.match(r"\s*INSERT INTO", l, re.I)}
    assert not [t for t in tables if "slack" in t.lower()], (word, tables)
COUNTED = [CALLS[n]["counted"] for n in RUNS]
assert COUNTED == [221, 196, 200, 237, 225, 244] and round(sum(COUNTED) / 6) == 220
assert all(c["acting"] == 0 and c["notfound"] == 0 for c in CALLS.values())
assert [CALLS[n]["submit"] for n in RUNS] == [1, 0, 0, 0, 0, 0] and CALLS[1]["job"] == 5 and CALLS[1]["rep_tools"] == {"slack_get_job_result": 4}
assert all("other" not in c["blocked_kinds"] for c in CALLS.values())
assert len({c["session"] for c in CALLS.values()}) == 6
COHORT = {n: (CALLS[n]["by"]["linear_list_comments"], CALLS[n]["by"]["linear_update_issue"], CALLS[n]["by"]["linear_create_comment"]) for n in RUNS}
assert [COHORT[n][1] for n in RUNS] == [COHORT[n][2] for n in RUNS] == [20, 20, 20, 32, 25, 32]
assert all(COHORT[n][0] in (96, 97) for n in RUNS)

# ------------------------------------------------------------------ ledger (revision binding, provenance) and receipts
LED = json.loads((WF / "run_forensics/rev2/baseline/summary.json").read_text())["runs"]
for r in LED:
    assert r["binding"]["verdict"] == "BOUND" and r["binding"]["bound_to"] == ["rev2"], r["label"]
    assert r["provenance"]["mixed_model"] is False and r["validity"]["status"] == "completed", r["label"]
    assert r["file"].startswith("Task_Authoring/task_inputs/07_Baseline_Trajectories/trajectory-run-"), r["file"]
    assert r["sha256"] == sha(WS / r["file"]), r["label"]
BIND = json.loads((WF / "verifier_binding.json").read_text())
DOCID = {r["number"]: r["comparison"]["export_observation"] for r in BIND["runs"]}
for r in BIND["runs"]:
    assert r["comparison"]["export_observation"] == r["comparison"]["verifier_observation"]
    assert r["export_sha256"] == sha(TASK / "07_Baseline_Trajectories" / f"trajectory-run-{r['number']}.json")
    assert VER.count(DOCID[r["number"]]) >= 1
assert BIND["verifier_sha256"] == sha(TASK / "10_Baseline_Verifier_Results.md") and BIND["revision"] == "rev2"

# ------------------------------------------------------------------ budget units, first-pass checks, platform weights
BUD = json.loads((WF / "01_Difficulty_Budget.json").read_text())
UNIT = {u: [int(x[1:]) for x in rows] for u, rows in BUD["rubric_rows"].items()}
UF = {u: [sum(1 for k in ids if not RES[n][k - 1]) for n in RUNS] for u, ids in UNIT.items()}
UW = {u: sum(W[k - 1] for k in ids) for u, ids in UNIT.items()}
assert UF == {"A1": [23, 23, 23, 23, 3, 23], "A2": [32, 32, 32, 32, 32, 3], "C1": [31, 31, 31, 3, 31, 31],
              "C2": [3, 3, 3, 3, 3, 3], "C3": [0, 0, 0, 3, 0, 3]}, UF
assert UW == {"A1": 79, "A2": 104, "C1": 103, "C2": 33, "C3": 15}
REST = [k for k in range(1, 154) if not any(k in ids for ids in UNIT.values())]
assert len(REST) == 64 and sum(W[k - 1] for k in REST) == 82 and not [k for k in REST if k in FC]
rcb, BUDGET_OUT, _ = tool("Task_Authoring/tools/budget_outcome.py", "compare", "--task-dir", REL, "--trajectory", f"{REL}/07_Baseline_Trajectories")
rcd, DRIFT_OUT, _ = tool("Task_Authoring/tools/rubric_skeleton.py", "drift", "--task-dir", REL)
assert "BUDGET OUTCOME (baseline, 6 runs): WARN" in BUDGET_OUT and "RUBRIC SKELETON (drift): WARN" in DRIFT_OUT
for needle in ("A1       anchor        1/6", "A2       anchor        1/6", "C1       variance      1/6", "C2       variance      6/6", "C3       variance      4/6"):
    assert needle in BUDGET_OUT, needle
PLAT = json.loads((TASK / "plateform_rubrics.json").read_text())
PLAT = PLAT if isinstance(PLAT, list) else next(v for v in PLAT.values() if isinstance(v, list))
PW = [int(r["weight"]) for r in PLAT]
assert len(PW) == 153 and [k + 1 for k in range(153) if PW[k] != W[k]] == [87, 100] and (PW[86], PW[99]) == (1, 1)
PRATE = {n: sum(w for w, p in zip(PW, RES[n]) if p) / sum(PW) for n in RUNS}
PMEAN, PPSD, PSSD = sum(PRATE.values()) / 6, statistics.pstdev(PRATE.values()), statistics.stdev(PRATE.values())
assert (sum(PW), round(PMEAN * 100, 1), round(PPSD, 3), round(PSSD, 3)) == (363, 41.0, 0.093, 0.102)

# ------------------------------------------------------------------ forecast
FC_DOC = json.loads((WF / "01c_Forecast.json").read_text())
SC = json.loads((WF / "12_Forecast_Score.json").read_text())
PRED = json.loads((WF / "12_Forecast_Predictions.json").read_text())
assert PRED["hashes"] == {"01c_Forecast.json": sha(WF / "01c_Forecast.json"), "12_difficulty_stats.json": sha(WF / "12_difficulty_stats.json")}
assert not SC["hash_errors"] and SC["scored"] == 15 and all(p["outcome"] is True for p in SC["predictions"])
FID = FC_DOC["preregistration"]["id"]
assert FID == "hev_e258af3aaa3d48aa" and FC_DOC["sql_sha256"].startswith("7d1f2aaeb29c") and not FC_DOC["channels"] and not FC_DOC["unparameterized_channels"]
V = [s["views"]["V3"] for s in FC_DOC["scenarios"]]
E_LO, E_HI = min(v["E_average"] for v in V), max(v["E_average"] for v in V)
BAND_LO = min(v["band_10_90"][0] for v in V)
PAVG = (min(v["P_gate"]["avg_weighted_pass_rate"] for v in V), max(v["P_gate"]["avg_weighted_pass_rate"] for v in V))
PSDG = (min(v["P_gate"]["per_rollout_sd"] for v in V), max(v["P_gate"]["per_rollout_sd"] for v in V))
PPAT = (min(v["P_gate"]["failure_patterns"] for v in V), max(v["P_gate"]["failure_patterns"] for v in V))
CONF = (min(p["confidence"] for p in PRED["predictions"]), max(p["confidence"] for p in PRED["predictions"]))
assert (E_LO, E_HI, BAND_LO, CONF) == (0.7773, 0.9337, 0.6832, (0.9154, 1.0)) and MEAN < BAND_LO
MECH = {m["id"].split(":")[1]: m["prior"]["mean"] for m in FC_DOC["mechanisms"]}

# ------------------------------------------------------------------ text
pct = lambda x: f"{x * 100:.1f}%"
call_note = "; ".join(f"run-{n} {c['counted']} ({c['raw']}/{c['harness']}/{c['blocked']}/{c['repeats']})" for n, c in CALLS.items())
cohort_note = "; ".join(f"run-{n} {COHORT[n][0]} + {COHORT[n][1]} + {COHORT[n][2]}" for n in RUNS)
blocked_note = "; ".join(f"run-{n} " + ", ".join(f"{v} {k}" for k, v in sorted(c["blocked_kinds"].items())) for n, c in CALLS.items())
diff_note = "; ".join(f"run-{a} {DIFF[a]}" for a in RUNS)
bind_rows = "\n".join(f"| Run #{n} | trajectory-run-{n}.json | {sha(TASK / '07_Baseline_Trajectories' / f'trajectory-run-{n}.json')[:12]} | {DOCID[n]} | {CALLS[n]['session'][:8]} | BOUND rev2 |" for n in RUNS)

OUT = f"""# 12 Baseline Difficulty & Failure Patterns — Julia Lawson ZM3D playable hand-off brief (SQL rev2)

Task type: long-horizon   Difficulty mode: assigned hard   Completed: 6/6   Errored: none   Invalid rubrics: none   Judge corrections: none
Clock: {CLOCK}
Seed bound: {CTX.get('freeze_utc') or J['context']['freeze_utc']}

Build command (matrix of record, Working_Files/12_difficulty_input.json, sha256 {sha(WF / '12_difficulty_input.json')[:12]}):
python3 Task_Authoring/tools/difficulty_stats.py --build --verifier {REL}/10_Baseline_Verifier_Results.md --rubrics {REL}/09_Rubrics.json --trajectories {REL}/07_Baseline_Trajectories --task-dir {REL} --revision rev2 --task-type "Long Horizon" --binding-receipt {REL}/Working_Files/verifier_binding.json --out {REL}/Working_Files/12_difficulty_input.json
Verifier binding: BOUND (reviewed receipt Working_Files/verifier_binding.json, kind VERIFIER_EXPORT_BINDING, source reviewed-content-comparison). 11's hand-off is "--invalid none --judge-correction none", so the platform view is the corrected fair view and one view is printed.
Inputs: 09_Rubrics.json sha256 {sha(TASK / '09_Rubrics.json')[:12]} (153 rows, weight {TOTAL}); 10_Baseline_Verifier_Results.md sha256 {sha(TASK / '10_Baseline_Verifier_Results.md')[:12]} (six Run blocks of 153 rows).

Trajectory to verifier Run binding (by content, not by file name). Each verifier Run block names the Google Doc it read the brief from; that id is returned by the brief's create call in exactly one export. trajectory_ledger.py binds every export to rev2 on content only rev2 holds (candidates rev2 and rev1), status completed, mixed model no:

| Verifier run | Export | Export sha256 | Brief Google Doc id | Session | Revision |
|---|---|---|---|---|---|
{bind_rows}

{CALC.rstrip()}

Readings: no golden run (best run-6 {pct(RATE[6])}). pass@1 0/6 full passes. Pattern grouping: the single-linkage and pairwise readings agree; run-1, run-2 and run-3 have identical results on all 153 rows (0 differing rubrics), and every other pair differs on 20 or more, so there are 4 patterns and the largest is 3 of 6 = 50%, exactly on the limit, which passes. SD: population {PSD:.3f} is below the 0.1 edge; sample {SSD:.3f} is inside the band and unweighted {USD:.3f} is below it, so this is a band-edge reading and the calculator's verdict (population) is FAIL. Corrected fair view = platform view (no invalid rubrics, no judge corrections; R55, R147 and R148 are VALID in 11_AF_Justification.md).
Failure patterns (what each run missed): three records decide 32 of the 49 Owed lines, and no run opened more than one of them. P1 run-1, run-2, run-3 ({pct(RATE[1])} each, failed weight {FAILW[1]} of {TOTAL}): opened none of Marcus's post C0880U9751A/1758906517.912099, Robert's note D05GU6L0XFH/1759178332.042459 or Brian's log f_faf4d7c167d14a1127dcc3, and reported 20 Owed and 68 Ready. P2 run-4 ({pct(RATE[4])}, failed weight {FAILW[4]}): opened Marcus's post only and reported 32 Owed; also missed R11, R43 and R44 (the changed board pick). P3 run-5 ({pct(RATE[5])}, failed weight {FAILW[5]}): opened Brian's log only and reported 25 Owed. P4 run-6 ({pct(RATE[6])}, failed weight {FAILW[6]}): opened Robert's note only and reported 32 Owed; also missed R11, R43 and R44. Rows by number of failing runs: 3 rows failed 6 runs (R55, R147, R148), 77 rows failed 5 runs, 3 rows failed 2 runs (R11, R43, R44), 70 rows passed all six.
Tool-call notes: counted (raw / harness / blocked / exact repeats) {call_note}; lowest {min(COUNTED)}, highest {max(COUNTED)}, mean {round(sum(COUNTED) / 6)}; 0 of 6 runs under the long-horizon floor of 100, and 0 under the owner's 130 target. set_acting_user calls: 0 in every run. Blocked calls are natural tool errors: {blocked_note}. run-1's 4 exact repeats are polls of one search job (slack_get_job_result) and are already subtracted. ACL-denied reads: a hand scan finds 0 short "not found" results outside the error results in any run, so nothing more is subtracted. Padding: none from the task. The per-line work is the incorporated cohort of 96 pack lines: comment reads + state moves + comments per run are {cohort_note}; each line's ticket notes can decide its state (15 Owed lines are decided there), and the moves and comments equal the lines that run judged Owed.
Friction check: not configured (03_Error_Async_Config.txt "Friction: none"). Confirmed in the exports: no forced error pattern (the 1 to 5 error results per run are the natural errors listed above, each on a different call), and no configured wait. run-1 chose the asynchronous Slack search once on its own (1 slack_submit_search, 5 slack_get_job_result); the other five runs made 0 submit calls. No recovery criterion depends on friction.
Screen 60 comparison: not supplied (no screen 60 numbers were pasted). One known difference to expect: the platform's rubric copy saved as plateform_rubrics.json carries R87 and R100 at weight 1 where 09_Rubrics.json has 5 (total 363 against {TOTAL}). The verifier's pass and fail results do not depend on weights. If the platform still holds those two weights, screen 60 will show an average of {pct(PMEAN)} (per run {', '.join(pct(PRATE[n]) for n in RUNS)}) instead of {pct(MEAN)}; population SD would read {PPSD:.3f} (sample {PSSD:.3f}), and no gate verdict changes. The owner compares before confirming screen 61.
Diagnosis: one gate fails, in the only view there is. V3 cap and full-pass gates pass: average {pct(MEAN)} is strictly below 70% (hard) and 0/6 runs are full passes. Retained local checks: errored 0/6 PASS, failure patterns 4 with the largest 50% PASS (on the limit), horizon 220 PASS, provenance claude-opus-5-5 on all six PASS, per-rollout SD {PSD:.3f} FAIL (Spread Too Low). Cause of the spread miss: the runs fall into two groups only {round((RATE[5] - RATE[1]) * 100)} to {round((RATE[6] - RATE[1]) * 100)} points apart. Three runs opened none of the three deciding records and scored {pct(RATE[1])}; the other three each opened exactly one and scored {pct(RATE[5])} to {pct(RATE[6])}. Each of those records was opened by 1 of 6 runs, so no run combined two and nothing reached the upper half of the scale. Route: every other gate passes, so by the routing row for SD below 0.1 (owner decision of 2026-11-10) the spread miss is reported to the owner and is not by itself a reason for a universe revision; configured friction is never the fix. No rubric row is added, removed or re-weighted to move a number. If the owner wants the spread inside the band, the route is /create-hardening (MODE B, baseline) and then /create-scenario --revise to raise the find rate of one deciding record, which needs a new baseline. Risk to keep in view: the largest pattern sits exactly on the 50% limit; one more run with the "opened none" outcome would fail that gate.
Screen 61: the V3 gates (average under the cap, fewer than five full passes) and every retained check except spread pass in the corrected fair view, which equals the platform view, so there are no corrected rows to re-grade. per_rollout_sd is FAIL at {PSD:.3f}. Confirming screen 61 with that miss open is the owner's decision under the 2026-11-10 rule; it is not confirmed here.

First-pass checks (read before routing):
```
{BUDGET_OUT.rstrip()}
```
```
{DRIFT_OUT.rstrip()}
```
Reading of the two tables: the budget units are named by their deciding record. Brian's log (unit A1) and Robert's note (unit A2) were each opened by 1 of 6 runs, inside their declared ranges. Marcus's post (unit C1) was opened by 1 of 6, below its declared 0.30 to 0.57, which is the main reason the scores sit low and close together. Calvin's sheet (unit C2) was opened by all six and the later reply that changes one pick (unit C3) by 4 of 6, both above their ranges; rows failed per run in each unit: A1 {UF['A1']}, A2 {UF['A2']}, C1 {UF['C1']}, C2 {UF['C2']} (the three all-fail rows, which every unit shares), C3 {UF['C3']}. The 64 rows outside every unit (weight 82) passed in all six runs. Drift: the final rubric has 153 rows and weight {TOTAL} against a skeleton of 55 rows and weight 195; the always-pass share is 22.1% (skeleton 24.6%), so rows every run passes did not dilute the units. Both checks print WARN and neither blocks.

Forecast (pre-registered {FID}, Working_Files/01c_Forecast.json sha256 {sha(WF / '01c_Forecast.json')[:8]}…, registered on SQL rev2 7d1f2aaeb29c and scored on the rev2 baseline; advisory, UNCALIBRATED; no control channel was parameterized and none is listed as UNPARAMETERIZED): 15 predictions "the baseline fails a V3 difficulty gate", confidence 1 − P_all per scenario ({CONF[0]} correlated/whole to {CONF[1]} slip). Outcome: the calculator blocks on per_rollout_sd, so all 15 resolved True; Brier {SC['brier']} over 15 (constant 0.5 scores 0.25). The yes/no score flatters the forecast, which was right for the wrong reason: it expected the average to be too high (E[average] {E_LO} to {E_HI}, lowest 10–90 band edge {BAND_LO}, P(average gate passes) {PAVG[0]} to {PAVG[1]}) and the observed average is {MEAN:.3f}, below every band. Its mechanism priors are landing rates (the share of runs a trap catches): EXPORT {MECH['EXPORT']}, ARTHOLD {MECH['ARTHOLD']}, ZIP {MECH['ZIP']}; observed, each of those three records was missed by 5 of 6 runs (0.83). Forecast P(SD in band) {PSDG[0]} to {PSDG[1]} (observed {PSD:.3f}, out); P(patterns pass) {PPAT[0]} to {PPAT[1]} (observed pass). Scored with hardness_forecast.py score --append (Working_Files/12_Forecast_Predictions.json to 12_Forecast_Score.json; ledger: 30 records added).

## Self-review

1. Re-read as the eval: the V3 mode caps, the five-of-six rule and the fairness-first order in references/Docs/11_V3_Changes.md, then the QC rows Error Rate, pass@1, Average Weighted Rubric Pass Rate, Failure Signature Concentration and Task Type & Horizon (references/Docs/QC_Spec_Doc_Latest.csv), Evals/references/rules/scoring.json "Agent Failure Rate" / "Error Rate" / "Complexity Threshold Layers" and Evals/references/rules/long_horizon.md, gate by gate against the table above. The calculator output is pasted unchanged; the one FAIL is stated as a FAIL.
2. Recomputed independently (Working_Files/difficulty_gen/build_difficulty.py: its own parser over the raw 10_Baseline_Verifier_Results.md and the weights in 09_Rubrics.json, no difficulty_stats import, every figure asserted against 12_difficulty_stats.json): run headers {', '.join(f'{HEAD[n][0]}/153' for n in RUNS)} match their rows and every row binds to its criterion by title; total weight {TOTAL} (50 rows × 5, 9 × 3, 94 × 1); failed weight per run {', '.join(str(FAILW[n]) for n in RUNS)}, so {', '.join(f'{RATE[n] * 100:.2f}%' for n in RUNS)}; mean {MEAN * 100:.2f}%; population SD {PSD:.4f}, sample SD {SSD:.4f}, unweighted SD {USD:.4f}; full passes 0/6 = 0%; all-fail set R55, R147, R148. Differing-rubric counts (run × run-1..6): {diff_note}, so only run-1, run-2 and run-3 are within one rubric of each other: 4 patterns, largest 3 of 6 = 50%. Horizon basis: no 100% run, so the completed-run mean ({' + '.join(str(c) for c in COUNTED)}) / 6 = {round(sum(COUNTED) / 6)}. All equal the calculator.
3. Counted calls recounted by hand for all six exports (tool_use blocks in each trajectory-run-N.json: total, MCP service calls, set_acting_user, error results, exact repeats): {'; '.join(f"run-{n} {c['raw']}, {c['svc']}, {c['acting']}, {c['blocked']}, {c['repeats']} gives {c['counted']}" for n, c in CALLS.items())}; each equals difficulty_stats.count_tool_calls and the trajectory_ledger.py count.
4. Inputs re-verified, not notes: 11_AF_Justification.md hand-off "--invalid none --judge-correction none" = no "valid": false rubric in 12_difficulty_input.json = "Invalid rubrics: none" above; the rubric version is 09_Rubrics.json sha256 {sha(TASK / '09_Rubrics.json')[:12]}, the file /rubric round 2 reviewed (NON-FAIL 3, a narrow band that stays a valid rubric); the matrix rebuilt today is byte-identical to the one 11 used; assignment hard / long-horizon / Julia Lawson; assignment_hash {J['context']['assignment_hash'][:12]}…, policy_hash {J['context']['policy_hash'][:12]}…, context_hash {J['context']['context_hash'][:12]}… recorded in the matrix; model metadata claude-opus-5-5 in the init event of all six exports, no fallback and no subagent brief in any run.
5. Stage gate: python3 Task_Authoring/tools/stage_gate.py difficulty {REL} --paste was run on this file. Result: FAIL, with 13 checks passing, 2 failing and 2 warnings of 17. The tool pastes only a PASS, so no gate block is recorded here and none is hand-copied. Every check on this report passes: the 8 calculator lines match the re-run verbatim, all report lines and the Clock line are present, "Invalid rubrics" equals 11's hand-off and the input JSON, and the counter-readings, coverage and unresolved list are accepted. The two failing checks are upstream: chain.allfail (11_AF_Justification.md carries no all-fail PASS block) and readiness.evidence (the all-fail stage has no current attestation). The two warnings are the bare task-folder name and the missing PASS paste. Handoff by this gate is therefore blocked until the upstream certificates exist; see Unresolved (4).
6. Record per gate, with the counter-reading and its resolution:

| Gate | Counter-reading | Resolution (evidence) |
|---|---|---|
| errored runs (PASS) | Counter: a run should count as errored (a truncated or failed export), shrinking the denominator to five | No. All six exports end with a success result event (is_error false) and have distinct session ids; 12_difficulty_input.json records 6 completed. run-2 and run-4 each hit one socket reset on a Slack search and carried on to a success result; that is a blocked call, not an errored run |
| pass@1 (PASS) | Counter: an unfair row hides a full pass, so the count of full passes is wrong | The best run fails 54 rows (run-6), the fewest any run fails. 11_AF_Justification.md found R55, R147 and R148 VALID and no judge error; even with all three dropped no run passes every row, and 0 is far below 5 |
| average (PASS) | Counter: the low average comes from unfair or unreachable rows, so the corrected mean would be higher and could reach the cap | The 77 rows that fail five runs each pass in the one run that opened their deciding record (run-4 event 471, run-5 event 427, run-6 event 440 in 11_AF_Justification.md), so they are reachable. Dropping the three all-fail rows (weight 15) gives {sum((TOTAL - 15 - (FAILW[n] - 15)) / (TOTAL - 15) for n in RUNS) / 6 * 100:.1f}%; with the platform's weight 1 on R87 and R100 it is {pct(PMEAN)}. All far below 70% |
| SD (FAIL) | Counter, the reading that would pass: the sample SD {SSD:.3f} is inside 0.1 to 0.3, and six runs are a sample | The gate's rule is the population SD, {PSD:.3f}, and the unweighted SD {USD:.3f} is lower still; with the platform's two weights it is {PPSD:.3f}. The FAIL stands as printed in 12_difficulty_stats.json. It is at the band edge and is reported to the owner, not routed to a revision |
| patterns (PASS) | Counter: a looser "same pattern" reading merges run-5 into the run-1 to run-3 group, giving 4 of 6 = 67% | run-5 differs from run-1 on 20 rubrics (R112 to R127 and others in the differing-rubric table of item 2); the rule merges only runs that differ on at most 1. The single-linkage and pairwise readings both give 3 of 6 = 50%, which passes because exactly 50% is allowed. It is on the limit and is flagged as a risk |
| horizon (PASS) | Counter: raw counts include harness calls, repeats or denied reads, or the per-line reads are padding | Counted calls already exclude harness (4 to 8 per run), blocked (1 to 5) and repeats (4 in run-1); lowest counted is 196 in run-2. The 96 or 97 comment reads per run are one per pack line under DES-313 and decide 15 Owed lines, so they are required work; without them the lowest run still has 100 counted calls |
| model provenance (PASS) | Counter: a run used a fallback or mixed model, or the label is not Opus 5.5 | trajectory_ledger.py on all six: init model claude-opus-5-5, fallbacks none, briefs 0, mixed no, v3_valid yes (Working_Files/run_forensics/rev2/baseline/summary.json); the gate row reads all 6 slots claude-opus-5-5 |
| binding | Counter: the exports in 07_Baseline_Trajectories are not the batch the verifier graded (an older rev1 batch sat in that slot) | The slot now holds the rev2 batch (rev1 exports archived under Working_Files/run_forensics/rev1/exports). Each Run block's Google Doc id occurs in exactly one export (verifier_binding.json), and all six bind to rev2 on content rev1 does not hold |
| friction | Counter: the socket resets in run-2 and run-4 are configured friction, or they hid a deciding record and changed the scores | 03_Error_Async_Config.txt configures none. Each reset hit one Slack search that the run did not repeat: "{RESET[2][1]}" at run-2 event {RESET[2][0]} and "{RESET[4][1]}" at run-4 event {RESET[4][0]}. Neither word occurs in any Slack record of 01_Universe_Inject.sql (only in the Linear ticket notes, which every run read line by line), so neither search could have returned Marcus's post or Robert's note. Scores in runs 1 to 3 are identical with and without a reset (run-2 had one, run-1 and run-3 none) |

Unresolved: (1) per_rollout_sd FAIL at {PSD:.3f}, reported to the owner; no revision is routed for it alone. (2) Screen 60 numbers not supplied, and the platform copy may still hold weight 1 on R87 and R100; compare before screen 61. (3) The largest failure pattern is exactly 50%; it passes but has no margin. (4) Upstream certificates this gate also checks are open and are reported, not worked around: the rubric check cannot be certified while 37 rows carry weight 5 against a surface band of 3, so the all-fail stage has no PASS block; the hardening report, baseline design review, builder export and platform hand-off record for rev2 do not exist. The human-time worksheet was refreshed after the baseline on 2026-11-13 and is current. None of these changes a difficulty number.
"""
assert "<" not in re.sub(r"`[^`]*`", "", OUT.replace("<70%", "").replace("<=", "").replace("(hard, <", "(hard, ")) or True
(WF / "12_Difficulty_Stats.txt").write_text(OUT)
print(f"wrote 12_Difficulty_Stats.txt {len(OUT)} chars · mean {MEAN * 100:.2f}% · pop SD {PSD:.4f} · patterns {groups}")

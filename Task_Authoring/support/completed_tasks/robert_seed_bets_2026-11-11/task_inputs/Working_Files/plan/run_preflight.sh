#!/bin/bash
# /create-injection preflight chain for task_inputsS2: solver, final manifest, gates, dispositions, liveness, forecast, report.
# Stops at the first failing step, so a failing chain never spends a forecast. Each full run appends one forecast to the
# ledger: run it once, on the final SQL. `--no-forecast` runs everything before the forecast and appends nothing.
set -u
cd /Users/sumit/Source/OC || exit 2
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputsS2
PY=~/.local/bin/python3.12
T=Task_Authoring/task_inputsS2
W=$T/Working_Files
TOOLS=Task_Authoring/tools

step() {
  echo "== $1"; shift
  "$@" || { echo "STOPPED: failed at the step above; no forecast was run"; exit 1; }
}

step "final manifest (binds the solver digest)" $PY -B $W/plan/build_final_manifest.py
step "1 solver contract" $PY -B $TOOLS/oracle_kit.py check --task-dir $T
step "1 truth" $PY -B $TOOLS/oracle_kit.py truth --task-dir $T --out $W/solver/truth.json
step "1 truth equals plan/truth_sketch.json; the method gates all seven rules" $PY -B - <<'PY'
import json, re, sys
sys.path.insert(0, "Task_Authoring/tools")
import oracle_kit as ok
W = "Task_Authoring/task_inputsS2/Working_Files"
sql = open("Task_Authoring/task_inputsS2/01_Universe_Inject.sql").read()
mod = ok.load_solver(W + "/solver/solver.py")
rows = json.load(open(W + "/solver/truth.json"))
s = json.load(open(W + "/plan/truth_sketch.json"))
agg = mod.aggregates(rows)["totals"]
names = {"DD": mod.DD, "ZM": mod.ZM, "CF": mod.CF}
bad = [(k, b) for k, r in rows.items() for b, f in names.items() if round(s["cell"][k][b], 2) != r[f]]
bad += [(k, "paid") for k, r in rows.items() if s["payee_total"][k] != r["paid"]]
bad += [(k, "plain") for k, r in rows.items() if s["plain"][k] != r["notices_sum"]]
bad += [(k, "n") for k, r in rows.items() if s["cell"][k]["n"] != r["notices"]]
bad += [b for b, f in names.items() if agg["build"][f] != s["build"][b] or agg["revenue"][f] != s["revenue"][b]]
bad += ["company"] if agg["company_usd"] != s["company_usd"] or agg["company_bgn"] != 1999.0 else []
state = mod.load_state(sql)
state["method"] = ""
gone = [k for k, r in mod.solve(state).items() if {x: v for x, v in r.items() if x != "evidence"} != {x: v for x, v in rows[k].items() if x != "evidence"}]
want = sorted(mod.TOUCHED.values())
print("truth vs sketch:", bad or "equal", "| method removed moves:", sorted(gone))
sys.exit(1 if bad or sorted(gone) != want else 0)
PY
step "3 hardness gate" $PY -B $TOOLS/hardness_gate.py $W/01_Hardness_Manifest.json $T/01_Universe_Inject.sql
step "3 fact check" $PY -B $TOOLS/fact_check.py $T/01_Universe_Inject.sql --manifest $W/01_Hardness_Manifest.json --no-leak
step "3 base claims" $PY -B $TOOLS/base_claims.py $T/01_Universe_Inject.sql --task-dir $T
step "4 dispositions" $PY -B $W/plan/build_dispositions.py
step "4 mutate" $PY -B $TOOLS/difficulty_mutation.py mutate --task-dir $T --dispositions <($PY -B -c "import json;print(json.dumps(json.load(open('$W/01c_Dispositions.json'))['mutation']))") --require-dispositions
step "4 geometry" $PY -B $TOOLS/difficulty_mutation.py geometry --task-dir $T --dispositions $W/01c_Dispositions.json
step "5 liveness" $PY -B $TOOLS/trap_liveness.py --task-dir $T --dispositions <($PY -B -c "import json;print(json.dumps(json.load(open('$W/01c_Dispositions.json'))['liveness']))") --require-dispositions

if [ "${1:-}" = "--no-forecast" ]; then
  echo "chain through liveness passed; no forecast, no preflight report"
  exit 0
fi
# Forecast rates (disclosed overrides: no ledger record has these families). The tool's `e` is a per-member failure rate,
# the same direction as the design's miss rates (design section 6: they sum to 3.85 traps landing per run), so nothing is
# flipped. But a channel stacks on its rule's own landing rate on the same key: miss = 1 - (1 - theta)(1 - e), with theta
# the ledger's Beta(1,2), mean 1/3, for all seven families. So e = 1 - 1.5(1 - prior) makes the combined miss equal the
# prior. Recompute if the ledger's priors for A11, A15, A17 or A24 change.
RATES=(
  --channel-rate "CH-RET=0.55@residual of design miss .70; sc4_habits s9 says .85 (M routes, G method), lowered because ENG-2442 now names MotMot"
  --channel-rate "CH-OFF=0.40@residual of design miss .60; sc4_habits s9 .60 (M analogs, G wording)"
  --channel-rate "CH-ORPH=0.25@residual of design miss .50; sc4_habits s9 .50 (M)"
  --channel-rate "CH-CORR=0.325@residual of design miss .55; sc4_habits s9 .60, about .50 for a late mail (M)"
  --channel-rate "CH-ALIAS=0.325@residual of design miss .55; sc4_habits s9 Node .55 (mostly G: no task had an opaque payee)"
  --channel-rate "CH-CLASS=0.325@residual of design miss .55; sc4_habits s9 OVR .50, .35 to .65 by issue wording (M and G)"
  --channel-rate "CH-CURR=0.10@residual of design miss .40; sc4_habits s9 .45 row level (G: no task tested currency)"
  --channel-rate "control:RET=0.03@GUESS: sc4_habits s10 nets out with no record .03 (G); s9 the rule step never failed in 35 of 35"
  --channel-rate "control:OFF=0.03@GUESS: same basis as control:RET, no measured over-application for this rule"
  --channel-rate "control:ORPH=0.03@GUESS: same basis as control:RET, no measured over-application for this rule"
  --channel-rate "control:CORR=0.03@GUESS: same basis as control:RET, no measured over-application for this rule"
  --channel-rate "control:ALIAS=0.03@GUESS: same basis as control:RET, no measured over-application for this rule"
  --channel-rate "control:CLASS=0.03@GUESS: same basis as control:RET, no measured over-application for this rule"
  --channel-rate "control:CURR=0.03@GUESS: same basis as control:RET, no measured over-application for this rule"
)
step "forecast (appends to the ledger)" $PY -B $TOOLS/hardness_forecast.py forecast --task-dir $T --model claude-opus-5-5 "${RATES[@]}" --preregister --out $W/01c_Forecast.json
step "preflight report" $PY -B $TOOLS/preflight_report.py --task-dir $T --forecast $W/01c_Forecast.json

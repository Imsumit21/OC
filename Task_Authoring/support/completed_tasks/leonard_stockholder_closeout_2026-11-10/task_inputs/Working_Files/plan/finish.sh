#!/usr/bin/env bash
# Rebuild every generated artifact in order and run the gates. Usage: bash .../plan/finish.sh [--scenario]
set -u
cd "$(dirname "$0")/../../../.." || exit 2
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs
PY="$HOME/.local/bin/python3.12"
T=Task_Authoring/task_inputs; W=$T/Working_Files; P=$W/plan
"$PY" -B $P/build_scenario.py > /dev/null
if [ "${1:-}" = "--scenario" ]; then
  "$PY" -B $P/policy_scores.py > $P/policy_scores_output.txt 2>&1
  bash $P/run_forecast.sh --preregister > $P/forecast_output.txt 2>&1
  grep -o "hev_[0-9a-f]*" $P/forecast_output.txt | tail -1 | tr -d '\n' > $P/forecast_id.txt
  "$PY" -B $P/assemble_design.py | tail -1 | cut -c1-120
  "$PY" -B $P/write_evidence.py | cut -c1-80
  "$PY" -B Task_Authoring/tools/stage_gate.py scenario $T --paste 2>&1 | grep -E 'STAGE GATE|FAIL\]' | cut -c1-220
fi
"$PY" -B $P/build_sql.py | cut -c1-40
touch $W/solver/solver.py
"$PY" -B $P/seed_snapshot.py > /dev/null
"$PY" -B $P/build_final_manifest.py
bash $P/run_checks.sh 2>&1 | cut -c1-170
"$PY" -B $P/build_dispositions.py
bash $P/run_checks.sh --preflight 2>&1 | grep -E 'FAIL' | cut -c1-200
mkdir -p $W/run_forensics/rev2
cp $T/01_Universe_Inject.sql $W/run_forensics/rev2/01_Universe_Inject.sql
"$PY" -B $P/assemble_dossier.py
"$PY" -B Task_Authoring/tools/stage_gate.py injection $T --paste 2>&1 | grep -E 'STAGE GATE|FAIL\]|WARN\]' | cut -c1-300
# prompt-stage artifacts that bind the SQL and dossier
"$PY" - <<'PYEOF'
p="Task_Authoring/task_inputs/03_Error_Async_Config.txt"; s=open(p).read()
i=s.find("```\nSTAGE GATE error-async")
if i>0: open(p,"w").write(s[:i].rstrip()+"\n")
PYEOF
"$PY" -B Task_Authoring/tools/stage_gate.py error-async $T --paste 2>&1 | grep -E 'STAGE GATE|FAIL\]' | cut -c1-160
"$PY" -B $P/assemble_brief.py
"$PY" -B $P/write_brief_evidence.py
"$PY" -B Task_Authoring/tools/stage_gate.py prompt-writing $T --paste 2>&1 | grep -E 'STAGE GATE|FAIL\]' | cut -c1-200

#!/usr/bin/env bash
# Re-run every /create-injection check on the current SQL and save the outputs the dossier pastes (plan/*.txt).
# Usage: bash Task_Authoring/task_inputs/Working_Files/plan/run_checks.sh [--preflight]
set -u
cd "$(dirname "$0")/../../../.." || exit 2
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs
PY="$HOME/.local/bin/python3.12"
T=Task_Authoring/task_inputs
W=$T/Working_Files
P=$W/plan
SQL=$T/01_Universe_Inject.sql
TOOLS=Task_Authoring/tools
"$PY" -B $TOOLS/sql_lint.py $SQL > $P/sql_lint.txt 2>&1
"$PY" -B $TOOLS/hg.py lint --sql $SQL > $P/hg_lint.json 2>&1
"$PY" -B $TOOLS/base_check.py $SQL > $P/base_check.txt 2>&1
"$PY" -B $TOOLS/base_claims.py $SQL --task-dir $T > $P/base_claims.txt 2>&1
"$PY" -B $TOOLS/fact_check.py $SQL --manifest $W/01_Hardness_Manifest.json --no-leak > $P/fact_check.txt 2>&1
"$PY" -B $TOOLS/hardness_gate.py $W/01_Hardness_Manifest.json $SQL > $P/hardness_gate.txt 2>&1
"$PY" -B $TOOLS/persona_view.py check-sql leonard_hayes $SQL --load-bearing $P/load_bearing_ids.txt > $P/checksql.txt 2>&1
"$PY" -B $TOOLS/oracle_kit.py check --task-dir $T > $P/oracle_kit.txt 2>&1
"$PY" -B $TOOLS/oracle_kit.py truth --task-dir $T --out $W/solver/truth.json > $P/oracle_truth.txt 2>&1
"$PY" -B $TOOLS/difficulty_mutation.py mutate --task-dir $T --max-k 10 --allow-max-k 10 > $P/mutation.txt 2>&1
"$PY" -B $TOOLS/difficulty_mutation.py geometry --task-dir $T --max-k 10 --allow-max-k 10 > $P/geometry.txt 2>&1
"$PY" -B $TOOLS/trap_liveness.py --task-dir $T --dispositions $W/01c_Dispositions.json > $P/trap_liveness_sql.txt 2>&1
if [ "${1:-}" = "--preflight" ]; then
  "$PY" -B $TOOLS/hardness_forecast.py forecast --task-dir $T --model claude-opus-5-5 --channel-rate "CH-LIVE=0.05@design-prior-plan-policy_scores-rev2" --preregister --max-k 10 --allow-max-k 10 --out $W/01c_Forecast.json > $P/forecast.txt 2>&1
  "$PY" -B $TOOLS/preflight_report.py --task-dir $T --forecast $W/01c_Forecast.json --max-k 10 --allow-max-k 10 > $P/preflight.txt 2>&1
fi
for f in sql_lint base_check base_claims fact_check hardness_gate checksql oracle_kit mutation geometry trap_liveness_sql; do
  printf '%-18s %s\n' "$f" "$(grep -m1 -E 'PASS|FAIL|errors:|verdict|geometry: U|MUTATION' $P/$f.txt | cut -c1-150)"
done
"$PY" -c "import json;d=json.load(open('$P/hg_lint.json'));print('hg_lint           ', d.get('counts'))" 2>/dev/null || tail -2 $P/hg_lint.json

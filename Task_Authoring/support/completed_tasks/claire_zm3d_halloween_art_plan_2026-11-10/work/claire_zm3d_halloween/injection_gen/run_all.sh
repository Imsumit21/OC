#!/bin/zsh
# Rebuild the injection stage end to end (from the workspace root). Never executes SQL.
set -e
py() { python3 -B "$@"; }
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputsN2
T=Task_Authoring/task_inputsN2; W=$T/Working_Files; S=$T/01_Universe_Inject.sql; 
touch $W/solver/solver.py
py $W/injection_gen/gen_sql.py
py $W/injection_gen/build_final_manifest.py
py Task_Authoring/tools/oracle_kit.py check --task-dir $T | head -1
py Task_Authoring/tools/oracle_kit.py truth --task-dir $T --out $W/solver/truth.json | tail -1
py $W/injection_gen/write_dispositions.py
py -c "import json;d=json.load(open('$W/01c_Dispositions.json'));json.dump(d['mutation'],open('$W/scratch/disp_mutation.json','w'));json.dump(d['liveness'],open('$W/scratch/disp_liveness.json','w'))"
py Task_Authoring/tools/difficulty_mutation.py mutate --task-dir $T --max-k 11 --allow-max-k 11 --dispositions $W/scratch/disp_mutation.json | grep -E "locality|U =|cap|dispositions"
py Task_Authoring/tools/trap_liveness.py --task-dir $T --dispositions $W/scratch/disp_liveness.json --require-dispositions | tail -1
if [ "$1" = "forecast" ]; then
  py Task_Authoring/tools/hardness_forecast.py forecast --task-dir $T --model claude-opus-5-5 --mode medium --max-k 11 --allow-max-k 11 --preregister --out $W/01c_Forecast.json > $W/01c_Forecast.txt 2>&1
  grep -E "ledger: forecast|independent whole" $W/01c_Forecast.txt | sort -u
fi
py Task_Authoring/tools/preflight_report.py --task-dir $T --max-k 11 --allow-max-k 11 --forecast $W/01c_Forecast.json | head -1
mkdir -p $W/run_forensics/rev3 && cp $S $W/run_forensics/rev3/01_Universe_Inject.sql
py $W/injection_gen/build_dossier.py

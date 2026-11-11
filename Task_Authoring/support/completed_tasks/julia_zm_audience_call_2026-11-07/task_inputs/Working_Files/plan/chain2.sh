#!/bin/bash
# Post-amendment chain, run from the workspace root. SQL is unchanged (rev1).
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs MSYS_NO_PATHCONV=1
T=Task_Authoring/tools; I=Task_Authoring/task_inputs; W=$I/Working_Files; O=$W/plan/out
cmp $I/01_Universe_Inject.sql $W/run_forensics/rev1/01_Universe_Inject.sql && echo sql-unchanged
python3 -B $T/preflight_report.py --task-dir $I > $O/preflight0.txt 2>&1; echo pf0 $?
D=$(sha256sum $W/01c_Preflight_Report.json | cut -d' ' -f1)
python3 -B $W/plan/build_manifest.py --preflight-digest $D
M=R_K1,R_K3,R_K4,R_K5,R_F,R_D,R_E
python3 -B $T/hardness_forecast.py forecast --task-dir $I --model claude-opus-5-5 --design --mechanisms $M --manifest $W/01_Hardness_Manifest.json --preregister --freeze $W/01_Hardness_Manifest.json --freeze $W/solver/truth.json --freeze $I/01_Universe_Inject.sql --freeze $W/01_Gradable_Surface.json --out $W/01c_Forecast.json > $O/forecast.txt 2>&1; echo fc $?
python3 -B $T/difficulty_mutation.py mutate --task-dir $I --dispositions $O/mut_disp.json > $O/mutation.txt 2>&1; echo mutation $?
python3 -B $T/difficulty_mutation.py geometry --task-dir $I > $O/geometry.txt 2>&1
python3 -B $T/trap_liveness.py --task-dir $I --dispositions $O/live_disp.json > $O/liveness.txt 2>&1
python3 -B $T/hardness_v2_check.py --task-dir $I > $O/v2.txt 2>&1
python3 -B $T/oracle_kit.py check --task-dir $I > $O/oracle_kit.txt 2>&1; echo kit $?
python3 -B $T/hardness_gate.py $W/01_Hardness_Manifest.json $I/01_Universe_Inject.sql > $O/hardness_gate.txt 2>&1; echo hgate $?
python3 -B $T/fact_check.py $I/01_Universe_Inject.sql --manifest $W/01_Hardness_Manifest.json --no-leak > $O/fact_check.txt 2>&1; echo fact $?
python3 -B $T/preflight_report.py --task-dir $I --forecast $W/01c_Forecast.json > $O/preflight.txt 2>&1; echo pf $?
echo chain-done

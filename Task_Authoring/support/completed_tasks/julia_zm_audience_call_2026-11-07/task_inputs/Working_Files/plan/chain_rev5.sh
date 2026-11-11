#!/bin/bash
# rev5 check chain (timezone-neutral relative-time wording). Run from the workspace root.
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs MSYS_NO_PATHCONV=1
T=Task_Authoring/tools; I=Task_Authoring/task_inputs; W=$I/Working_Files; O=$W/plan/out; SQL=$I/01_Universe_Inject.sql
mkdir -p $O
python3 -B $W/plan/gen_lb.py
python3 -B $T/sql_lint.py $SQL --task-dir $I > $O/sql_lint.txt 2>&1; echo sql_lint $?
python3 -B $T/hg.py lint > $O/lint.json 2>$O/lint.err; echo lint $?
python3 -B $T/base_check.py $SQL > $O/base_check.txt 2>&1; echo base_check $?
python3 -B $T/base_check.py $SQL --manifest $W/01_Hardness_Manifest.json > $O/base_check_manifest.txt 2>&1; echo base_check_manifest $?
python3 -B $T/base_claims.py $SQL --task-dir $I > $O/base_claims.txt 2>&1; echo base_claims $?
python3 -B $T/persona_view.py check-sql julia_lawson $SQL --load-bearing $W/plan/load_bearing.txt > $O/check_sql.txt 2>&1; echo check_sql $?
python3 -B $W/plan/audience_check.py > $O/audience_check.txt 2>&1; echo audience_check $?
python3 -B $W/plan/sweep.py > $O/sweep.txt 2>&1; echo sweep $?
python3 -B $W/plan/parent_check.py > $O/parent_check.txt 2>&1; echo parent_check $?
python3 -B $T/fact_check.py $SQL --manifest $W/01_Hardness_Manifest.json --no-leak > $O/fact_check.txt 2>&1; echo fact_check $?
python3 -B $T/hardness_gate.py $W/01_Hardness_Manifest.json $SQL > $O/hardness_gate.txt 2>&1; echo hardness_gate $?
python3 -B $T/oracle_kit.py check --task-dir $I > $O/oracle_kit.txt 2>&1; echo oracle_kit $?
python3 -B $T/difficulty_mutation.py mutate --task-dir $I --dispositions $O/mut_disp.json > $O/mutation.txt 2>&1; echo mutation $?
python3 -B $T/trap_liveness.py --task-dir $I --dispositions $O/live_disp.json > $O/liveness.txt 2>&1; echo liveness $?
python3 -B $T/hardness_v2_check.py --task-dir $I > $O/v2.txt 2>&1; echo v2 $?
python3 -B $T/preflight_report.py --task-dir $I --forecast $W/01c_Forecast.json > $O/preflight.txt 2>&1; echo preflight $?
echo chain-done

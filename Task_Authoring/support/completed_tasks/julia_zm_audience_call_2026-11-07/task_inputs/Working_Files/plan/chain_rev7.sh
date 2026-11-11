#!/bin/bash
# rev7 check chain (S0r delta, rev7 SQL). Run from the workspace root.
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs MSYS_NO_PATHCONV=1
T=Task_Authoring/tools; I=Task_Authoring/task_inputs; W=$I/Working_Files; O=$W/plan/out_rev7; SQL=$I/01_Universe_Inject.sql
mkdir -p $O
python -X utf8 -B $W/plan/gen_lb.py
python -X utf8 -B $T/sql_lint.py $SQL --task-dir $I > $O/sql_lint.txt 2>&1; echo sql_lint $?
python -X utf8 -B $T/hg.py lint > $O/lint.json 2>$O/lint.err; echo lint $?
python -X utf8 -B $T/base_check.py $SQL > $O/base_check.txt 2>&1; echo base_check $?
python -X utf8 -B $T/base_check.py $SQL --manifest $W/01_Hardness_Manifest.json > $O/base_check_manifest.txt 2>&1; echo base_check_manifest $?
python -X utf8 -B $T/base_claims.py $SQL --task-dir $I > $O/base_claims.txt 2>&1; echo base_claims $?
python -X utf8 -B $T/persona_view.py check-sql julia_lawson $SQL --load-bearing $W/plan/load_bearing.txt > $O/check_sql.txt 2>&1; echo check_sql $?
python -X utf8 -B $W/plan/audience_check.py > $O/audience_check.txt 2>&1; echo audience_check $?
python -X utf8 -B $W/plan/sweep.py > $O/sweep.txt 2>&1; echo sweep $?
python -X utf8 -B $W/plan/parent_check.py > $O/parent_check.txt 2>&1; echo parent_check $?
python -X utf8 -B $T/fact_check.py $SQL --manifest $W/01_Hardness_Manifest.json --no-leak > $O/fact_check.txt 2>&1; echo fact_check $?
python -X utf8 -B $T/hardness_gate.py $W/01_Hardness_Manifest.json $SQL > $O/hardness_gate.txt 2>&1; echo hardness_gate $?
python -X utf8 -B $T/oracle_kit.py check --task-dir $I > $O/oracle_kit.txt 2>&1; echo oracle_kit $?
python -X utf8 -B $T/difficulty_mutation.py mutate --task-dir $I --dispositions $O/mut_disp.json > $O/mutation.txt 2>&1; echo mutation $?
python -X utf8 -B $T/trap_liveness.py --task-dir $I --dispositions $O/live_disp.json > $O/liveness.txt 2>&1; echo liveness $?
python -X utf8 -B $T/hardness_v2_check.py --task-dir $I > $O/v2.txt 2>&1; echo v2 $?
python -X utf8 -B $T/hardness_gate.py $W/01_Hardness_Manifest.draft.json --design > $O/hardness_gate_design.txt 2>&1; echo hardness_gate_design $?
python -X utf8 -B $T/time_order_check.py $SQL > $O/time_order.txt 2>&1; echo time_order $?
echo chain-done

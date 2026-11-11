#!/bin/bash
# rev4 solver contract, mutation, liveness, v2 and preflight. Run from the workspace root.
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs MSYS_NO_PATHCONV=1
T=Task_Authoring/tools; I=Task_Authoring/task_inputs; W=$I/Working_Files; O=$W/plan/out
python3 -B $T/oracle_kit.py check --task-dir $I > $O/oracle_kit.txt 2>&1; echo oracle_kit $?
python3 -B $T/difficulty_mutation.py mutate --task-dir $I --dispositions $O/mut_disp.json > $O/mutation.txt 2>&1; echo mutation $?
python3 -B $T/trap_liveness.py --task-dir $I --dispositions $O/live_disp.json > $O/liveness.txt 2>&1; echo liveness $?
python3 -B $T/hardness_v2_check.py --task-dir $I > $O/v2.txt 2>&1; echo v2 $?
python3 -B $T/preflight_report.py --task-dir $I --forecast $W/01c_Forecast.json > $O/preflight.txt 2>&1; echo preflight $?
echo chain-done

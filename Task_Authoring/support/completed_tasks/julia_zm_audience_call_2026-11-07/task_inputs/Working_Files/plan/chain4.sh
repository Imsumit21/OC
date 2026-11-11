#!/bin/bash
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs MSYS_NO_PATHCONV=1
T=Task_Authoring/tools; I=Task_Authoring/task_inputs; W=$I/Working_Files; O=$W/plan/out
P="--previous-sql $W/run_forensics/rev1/01_Universe_Inject.sql --previous-truth $W/run_forensics/rev1/truth.json"
python3 -B $W/plan/build_manifest.py --preflight-digest 0000000000000000000000000000000000000000000000000000000000000000
python3 -B $T/preflight_report.py --task-dir $I --forecast $W/01c_Forecast.json $P > $O/preflight0.txt 2>&1; echo pf0 $?
D=$(sha256sum $W/01c_Preflight_Report.json | cut -d' ' -f1)
python3 -B $W/plan/build_manifest.py --preflight-digest $D
python3 -B $T/fact_check.py $I/01_Universe_Inject.sql --manifest $W/01_Hardness_Manifest.json --no-leak > $O/fact_check.txt 2>&1; echo fact $?
python3 -B $T/hardness_gate.py $W/01_Hardness_Manifest.json $I/01_Universe_Inject.sql > $O/hardness_gate.txt 2>&1; echo hgate $?
python3 -B $T/oracle_kit.py check --task-dir $I $P > $O/oracle_kit.txt 2>&1; echo kit $?
python3 -B $T/preflight_report.py --task-dir $I --forecast $W/01c_Forecast.json $P > $O/preflight.txt 2>&1; echo pf $?
python3 -B $W/plan/gen_dossier.py
python3 -B $T/stage_gate.py injection $I --paste > $O/gate.txt 2>&1; echo gate $?
grep -v '^\[PASS\]' $O/gate.txt | cut -c1-400; grep -c '^\[PASS\]' $O/gate.txt
echo chain-done

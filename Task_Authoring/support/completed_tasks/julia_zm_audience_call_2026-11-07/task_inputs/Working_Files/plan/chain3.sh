#!/bin/bash
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs MSYS_NO_PATHCONV=1
T=Task_Authoring/tools; I=Task_Authoring/task_inputs; W=$I/Working_Files; O=$W/plan/out
python3 -B $W/plan/build_manifest.py --preflight-digest 0000000000000000000000000000000000000000000000000000000000000000
python3 -B $T/oracle_kit.py truth --solver $W/solver/solver.py --sql $I/01_Universe_Inject.sql --out $W/solver/truth.json
python3 -B $T/preflight_report.py --task-dir $I --forecast $W/01c_Forecast.json --previous-sql $W/run_forensics/rev1/01_Universe_Inject.sql --previous-truth $W/run_forensics/rev1/truth.json > $O/preflight0.txt 2>&1; echo pf0 $?
D=$(sha256sum $W/01c_Preflight_Report.json | cut -d' ' -f1)
python3 -B $W/plan/build_manifest.py --preflight-digest $D
python3 -B $W/plan/gen_lb.py
python3 -B $T/sql_lint.py $I/01_Universe_Inject.sql > $O/sql_lint.txt 2>&1; echo sql_lint $?
python3 -B $T/base_check.py $I/01_Universe_Inject.sql > $O/base_check.txt 2>&1; echo base_check $?
python3 -B $T/base_claims.py $I/01_Universe_Inject.sql --task-dir $I > $O/base_claims.txt 2>&1; echo base_claims $?
python3 -B $T/hg.py lint > $O/lint.json 2>$O/lint.err; echo lint $?
python3 -B $T/fact_check.py $I/01_Universe_Inject.sql --manifest $W/01_Hardness_Manifest.json --no-leak > $O/fact_check.txt 2>&1; echo fact $?
python3 -B $T/persona_view.py check-sql julia_lawson $I/01_Universe_Inject.sql --load-bearing $W/plan/load_bearing.txt > $O/check_sql.txt 2>&1; echo checksql $?
python3 -B $T/hardness_gate.py $W/01_Hardness_Manifest.json $I/01_Universe_Inject.sql > $O/hardness_gate.txt 2>&1; echo hgate $?
python3 -B $T/oracle_kit.py check --task-dir $I --previous-sql $W/run_forensics/rev1/01_Universe_Inject.sql --previous-truth $W/run_forensics/rev1/truth.json > $O/oracle_kit.txt 2>&1; echo kit $?
python3 -B $T/difficulty_mutation.py mutate --task-dir $I --dispositions $O/mut_disp.json > $O/mutation.txt 2>&1; echo mutation $?
python3 -B $T/difficulty_mutation.py geometry --task-dir $I > $O/geometry.txt 2>&1
python3 -B $T/trap_liveness.py --task-dir $I --dispositions $O/live_disp.json > $O/liveness.txt 2>&1; echo live $?
python3 -B $T/hardness_v2_check.py --task-dir $I > $O/v2.txt 2>&1; echo v2 $?
python3 -B $T/preflight_report.py --task-dir $I --forecast $W/01c_Forecast.json --previous-sql $W/run_forensics/rev1/01_Universe_Inject.sql --previous-truth $W/run_forensics/rev1/truth.json > $O/preflight.txt 2>&1; echo pf $?
echo chain-done

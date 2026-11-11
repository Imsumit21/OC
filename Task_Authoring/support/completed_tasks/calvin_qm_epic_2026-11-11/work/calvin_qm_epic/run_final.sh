#!/bin/sh
# After run_checks.sh: dispositions, forecast, preflight report, dossier (run from the workspace root). Pass --preregister to register the forecast.
TD=Task_Authoring/task_inputs; W=$TD/Working_Files; S=$TD/01_Universe_Inject.sql; P=$W/plan; O=$P/out/inj; T=Task_Authoring/tools
export TASK_AUTHORING_TASK_DIR=$PWD/$TD
python3 $P/write_dispositions.py > $O/dispositions.txt 2>&1
python3 -B $T/difficulty_mutation.py mutate --task-dir $TD > $O/mutation.txt 2>&1
python3 -B $T/trap_liveness.py --task-dir $TD > $O/liveness.txt 2>&1
python3 -B $T/hardness_forecast.py forecast --task-dir $TD --model claude-opus-5-5 --draws ${DRAWS:-3000} --out $W/01c_Forecast.json --channel-rate CH-ALIAS=0.20@scenario-prior-scope_alias-no-ledger-record "$@" > $O/forecast_inj.txt 2>&1
python3 -B $T/preflight_report.py --task-dir $TD --forecast $W/01c_Forecast.json > $O/preflight.txt 2>&1
python3 $P/assemble_dossier.py > $O/dossier.txt 2>&1
cat $O/dispositions.txt | cut -c1-200; grep -E "dispositions:" $O/mutation.txt $O/liveness.txt | cut -c1-160; wc -l $O/forecast_inj.txt; grep -E "P\(all|UNPARAM|UNSUPPORTED|ledger" $O/forecast_inj.txt | tail -4 | cut -c1-220; tail -3 $O/preflight.txt | cut -c1-220; cat $O/dossier.txt

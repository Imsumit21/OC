#!/bin/sh
# Full rebuild from the workspace root: scenario, scenario gate, SQL, checks, preflight, dossier, injection gate.
TD=Task_Authoring/task_inputs; P=$TD/Working_Files/plan; O=$P/out
export TASK_AUTHORING_TASK_DIR=$PWD/$TD
sh $P/run_scenario.sh || exit 1
python3 Task_Authoring/tools/stage_gate.py scenario $TD --paste > $O/stage_scenario.txt 2>&1
grep "STAGE GATE" $O/stage_scenario.txt | cut -c1-60
python3 $P/build_sql.py | head -1 | cut -c1-30
touch $TD/Working_Files/solver/solver.py
sh $P/run_checks.sh
sh $P/run_final.sh "$@"
python3 Task_Authoring/tools/stage_gate.py injection $TD ${PASTE:-} > $O/inj/stage_injection.txt 2>&1
grep -v "^\s*\[PASS\]\|^\s*\[ok\]" $O/inj/stage_injection.txt | cut -c1-900 | head -40

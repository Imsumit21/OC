#!/bin/sh
# Rebuilds every /create-injection output in dependency order and re-runs the tools whose output the dossier pastes.
# Run from the workspace root: sh Task_Authoring/task_inputs/Working_Files/scenario_gen/rebuild_injection.sh
# Never edits the scenario artifacts (01_Scenario_Design.md, the draft manifest, the gradable surface).
set -e
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs
T=Task_Authoring/task_inputs
W=$T/Working_Files
G=$W/scenario_gen
O=$W/research/tool_out
S=$T/01_Universe_Inject.sql
python3 -B $G/build_sql.py
mkdir -p $W/run_forensics/rev1
if [ -f $W/run_forensics/rev1/01_Universe_Inject.sql ] && ! cmp -s $S $W/run_forensics/rev1/01_Universe_Inject.sql; then
  echo "rev1 is stored and differs: a changed SQL is a new revision (store it as rev2)"; exit 1
fi
cp $S $W/run_forensics/rev1/01_Universe_Inject.sql
python3 -B $G/build_solver.py
python3 -B $G/make_lb.py
python3 -B $G/build_final_manifest.py
python3 -B Task_Authoring/tools/oracle_kit.py truth --task-dir $T --out $W/solver/truth.json
python3 -c "import pathlib,json; p=pathlib.Path('$W/01c_Dispositions.json'); p.write_text(json.dumps(json.loads(p.read_text()), indent=1, ensure_ascii=False) + '\n')"
python3 Task_Authoring/tools/sql_lint.py $S > $O/sql_lint.txt 2>&1 || true
python3 Task_Authoring/tools/base_check.py $S > $O/base_check.txt 2>&1 || true
python3 Task_Authoring/tools/base_claims.py $S --task-dir $T > $O/base_claims.txt 2>&1 || true
python3 Task_Authoring/tools/hg.py lint > $O/hglint.json 2> $O/hglint.err || true
python3 Task_Authoring/tools/fact_check.py $S --manifest $W/01_Hardness_Manifest.json --no-leak > $O/fact_check.txt 2>&1 || true
python3 Task_Authoring/tools/persona_view.py check-sql vincent_parker $S --load-bearing $O/lb_ids.txt > $O/check_sql.txt 2>&1 || true
python3 Task_Authoring/tools/hardness_gate.py $W/01_Hardness_Manifest.json $S > $O/hardness_gate_sql.txt 2>&1 || true
python3 -B Task_Authoring/tools/oracle_kit.py check --task-dir $T > $O/oracle.txt 2>&1 || true
python3 -B Task_Authoring/tools/difficulty_mutation.py mutate --task-dir $T > $O/mutation.txt 2>&1 || true
python3 Task_Authoring/tools/trap_liveness.py --task-dir $T > $O/liveness_sql.txt 2>&1 || true
python3 -B Task_Authoring/tools/preflight_report.py --task-dir $T --forecast $W/01c_Forecast.json > $O/preflight.txt 2>&1 || true
python3 -B $G/build_dossier.py
head -1 $O/base_check.txt $O/base_claims.txt $O/fact_check.txt $O/hardness_gate_sql.txt $O/oracle.txt $O/preflight.txt
grep -E "^verdict" $O/check_sql.txt

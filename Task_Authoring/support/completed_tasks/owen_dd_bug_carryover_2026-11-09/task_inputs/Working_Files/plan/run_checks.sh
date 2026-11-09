#!/usr/bin/env bash
# Rebuilds every generated artifact and re-runs each /create-injection check, saving the outputs the dossier pastes (plan/out/*).
# Usage: bash Task_Authoring/task_inputs/Working_Files/plan/run_checks.sh
set -u
cd "$(dirname "$0")/../../../.." || exit 2
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs
T=Task_Authoring/task_inputs; W=$T/Working_Files; P=$W/plan; O=$P/out; TOOLS=Task_Authoring/tools; SQL=$T/01_Universe_Inject.sql
python3 $P/build_sql.py > $O/build_sql.txt
python3 -B $TOOLS/oracle_kit.py truth --solver $W/solver/solver.py --sql $SQL --revision rev9 --out $W/solver/truth.json > $O/oracle_truth.txt 2>&1
python3 $P/build_final_manifest.py > $O/final_manifest.txt 2>&1
python3 $P/id_lookups.py > $O/id_lookups.txt 2>&1
python3 $TOOLS/sql_lint.py $SQL > $O/sql_lint.txt 2>&1
python3 $TOOLS/hg.py lint --sql $SQL > $O/hg_lint.json 2>&1
python3 $TOOLS/fact_check.py $SQL --manifest $W/01_Hardness_Manifest.json --no-leak > $O/fact_check.txt 2>&1
python3 $TOOLS/persona_view.py check-sql owen_baker $SQL --load-bearing $P/load_bearing_ids.txt > $O/checksql.txt 2>&1
python3 -B $TOOLS/oracle_kit.py check --task-dir $T --previous-sql $W/run_forensics/rev8/01_Universe_Inject.sql --previous-truth $W/run_forensics/rev8/truth.json > $O/oracle_kit.txt 2>&1
python3 -B $TOOLS/difficulty_mutation.py mutate --task-dir $T > $O/mutation.txt 2>&1
python3 -B $TOOLS/difficulty_mutation.py geometry --task-dir $T > $O/geometry.txt 2>&1
python3 -B $TOOLS/trap_liveness.py --task-dir $T > $O/trap_liveness_sql.txt 2>&1
python3 $P/build_dispositions.py > $O/dispositions.txt 2>&1
python3 $TOOLS/base_claims.py $SQL --task-dir $T > $O/base_claims.txt 2>&1
python3 $TOOLS/base_check.py $SQL > $O/base_check.txt 2>&1
python3 $TOOLS/hardness_gate.py $W/01_Hardness_Manifest.json $SQL > $O/hardness_gate.txt 2>&1
for f in sql_lint base_check base_claims fact_check hardness_gate checksql oracle_kit mutation geometry; do
  printf '%-16s %s\n' "$f" "$(grep -m1 -E 'PASS|FAIL|errors:|verdict|geometry: U' $O/$f.txt | cut -c1-150)"
done

#!/bin/sh
# Re-run the injection checks on the final SQL and save their output under plan/ (workspace root). Order per playbook S5.
TD=Task_Authoring/task_inputsK; W=$TD/Working_Files; S=$TD/01_Universe_Inject.sql; P=$W/plan; T=Task_Authoring/tools
export TASK_AUTHORING_TASK_DIR=$PWD/$TD
python3 $P/build_final_manifest.py > $P/manifest_build.txt 2>&1
python3 -B $T/sql_lint.py $S > $P/sql_lint.txt 2>&1
python3 -B $T/base_check.py $S > $P/base_check.txt 2>&1
python3 -B $T/base_claims.py $S --task-dir $TD > $P/base_claims.txt 2>&1
python3 -B $T/fact_check.py $S --manifest $W/01_Hardness_Manifest.json --no-leak > $P/fact_check.txt 2>&1
python3 -B $T/persona_view.py check-sql samuel_turner $S --load-bearing $P/load_bearing_scoped.txt > $P/checksql.txt 2>&1
python3 -B $T/hardness_gate.py $W/01_Hardness_Manifest.json $S > $P/hardness_gate.txt 2>&1
python3 -B $T/hg.py lint > $P/hg_lint.txt 2>&1
python3 -B $T/oracle_kit.py check --task-dir $TD > $P/oracle_kit.txt 2>&1
python3 -B $T/oracle_kit.py truth --task-dir $TD --out $W/solver/truth.json > $P/truth_out.txt 2>&1
python3 -B $T/difficulty_mutation.py mutate --task-dir $TD > $P/mutation.txt 2>&1
python3 -B $T/difficulty_mutation.py geometry --task-dir $TD > $P/geometry.txt 2>&1
python3 -B $T/trap_liveness.py --task-dir $TD > $P/liveness.txt 2>&1
tail -1 $P/manifest_build.txt | cut -c1-120
for f in sql_lint base_check base_claims fact_check checksql hardness_gate oracle_kit; do echo "== $f: $(grep -E -m1 'errors:|BASE CHECK|BASE CLAIMS|FACT CHECK|^verdict|HARDNESS GATE|SOLVER CONTRACT' $P/$f.txt | cut -c1-110)"; done
grep -E 'counts' $P/hg_lint.txt | cut -c1-120
grep -E 'key-locality|U = |V3 cap' $P/geometry.txt | cut -c1-130

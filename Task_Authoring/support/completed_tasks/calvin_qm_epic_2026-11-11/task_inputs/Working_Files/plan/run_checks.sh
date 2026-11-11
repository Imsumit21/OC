#!/bin/sh
# Re-run the injection checks on the final SQL and save their output under plan/out/ (run from the workspace root). Order per playbook S5.
TD=Task_Authoring/task_inputs; W=$TD/Working_Files; S=$TD/01_Universe_Inject.sql; P=$W/plan; O=$P/out/inj; T=Task_Authoring/tools
mkdir -p $O
export TASK_AUTHORING_TASK_DIR=$PWD/$TD
python3 $P/build_final_manifest.py > $O/manifest_build.txt 2>&1
python3 -B $T/sql_lint.py $S > $O/sql_lint.txt 2>&1
python3 -B $T/base_check.py $S > $O/base_check.txt 2>&1
python3 -B $T/base_claims.py $S --task-dir $TD > $O/base_claims.txt 2>&1
python3 -B $T/fact_check.py $S --manifest $W/01_Hardness_Manifest.json --no-leak > $O/fact_check.txt 2>&1
python3 -B $T/persona_view.py check-sql calvin_price $S --load-bearing $P/load_bearing_scoped.txt > $O/checksql.txt 2>&1
python3 -B $T/hardness_gate.py $W/01_Hardness_Manifest.json $S > $O/hardness_gate.txt 2>&1
python3 -B $T/hg.py lint > $O/hg_lint.txt 2>&1
python3 -B $T/oracle_kit.py check --task-dir $TD > $O/oracle_kit.txt 2>&1
python3 -B $T/oracle_kit.py truth --task-dir $TD --out $W/solver/truth.json > $O/truth_out.txt 2>&1
python3 -B $T/difficulty_mutation.py mutate --task-dir $TD > $O/mutation.txt 2>&1
python3 -B $T/difficulty_mutation.py geometry --task-dir $TD > $O/geometry.txt 2>&1
python3 -B $T/trap_liveness.py --task-dir $TD > $O/liveness.txt 2>&1
tail -1 $O/manifest_build.txt | cut -c1-160
for f in sql_lint base_check base_claims fact_check checksql hardness_gate oracle_kit; do echo "== $f: $(grep -E -m1 'errors:|BASE CHECK|BASE CLAIMS|FACT CHECK|^verdict|HARDNESS GATE|SOLVER CONTRACT' $O/$f.txt | cut -c1-110)"; done
grep -E 'counts' $O/hg_lint.txt | cut -c1-120
grep -E 'key-locality|U = |V3 cap|L_max' $O/geometry.txt | cut -c1-160

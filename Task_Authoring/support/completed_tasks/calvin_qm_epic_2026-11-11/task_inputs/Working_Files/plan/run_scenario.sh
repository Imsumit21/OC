#!/bin/sh
# Rebuild the scenario artifacts and re-run the design-stage tools (run from the workspace root).
TD=Task_Authoring/task_inputs; W=$TD/Working_Files; P=$W/plan; O=$P/out; T=Task_Authoring/tools
export TASK_AUTHORING_TASK_DIR=$PWD/$TD
python3 $P/build_scenario.py > $O/build_scenario.txt 2>&1
python3 -B $T/hardness_gate.py $W/01_Hardness_Manifest.draft.json --design > $O/gate.txt 2>&1
python3 -B $T/gradable_surface.py validate --task-dir $TD > $O/surface.txt 2>&1
python3 -B $T/gradable_surface.py gradeable-report --task-dir $TD > $O/gradeable.txt 2>&1
python3 -B $T/trap_liveness.py --design --task-dir $TD > $O/liveness.txt 2>&1
python3 -B $T/hardness_v2_check.py --design --task-dir $TD > $O/v2.txt 2>&1
python3 $P/assemble_design.py > $O/assemble_design.txt 2>&1
python3 $P/build_reviews.py > $O/build_reviews.txt 2>&1
for f in gate surface gradeable; do echo "== $f: $(grep -E -m1 'HARDNESS GATE|SURFACE|GRADEABLE|PASS|FAIL' $O/$f.txt | cut -c1-120)"; done
tail -2 $O/assemble_design.txt $O/build_reviews.txt | cut -c1-200

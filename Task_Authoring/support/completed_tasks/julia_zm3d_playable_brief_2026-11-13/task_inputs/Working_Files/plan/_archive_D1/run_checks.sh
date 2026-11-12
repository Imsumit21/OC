#!/bin/zsh
# Rebuild the design artifacts in dependency order and capture every tool output the design document pastes.
# Usage: zsh Task_Authoring/task_inputs/Working_Files/plan/run_checks.sh   (from the workspace root)
set -u
ROOT=/Users/sumitkumar/Source/Outlier/OC
cd $ROOT
export TASK_AUTHORING_TASK_DIR=$ROOT/Task_Authoring/task_inputs
T=Task_Authoring/task_inputs
P=$T/Working_Files/plan
O=$P/out
TOOLS=Task_Authoring/tools
mkdir -p $O

python3 -B $P/build_surface.py   > $O/_build_surface.log 2>&1   || { echo "build_surface failed"; cat $O/_build_surface.log; exit 1; }
python3 -B $P/build_manifest.py  > $O/_build_manifest.log 2>&1  || { echo "build_manifest failed"; cat $O/_build_manifest.log; exit 1; }
python3 -B $P/build_budget.py surface  > $O/_build_budget.log 2>&1 || { echo "build_budget surface failed"; cat $O/_build_budget.log; exit 1; }
python3 -B $TOOLS/rubric_skeleton.py build --write --task-dir $T > $O/_skeleton_build.log 2>&1
python3 -B $P/build_budget.py skeleton >> $O/_build_budget.log 2>&1 || { echo "build_budget skeleton failed"; cat $O/_build_budget.log; exit 1; }
python3 -B $TOOLS/rubric_skeleton.py build --write --task-dir $T >> $O/_skeleton_build.log 2>&1

python3 -B $TOOLS/hardness_gate.py $T/Working_Files/01_Hardness_Manifest.draft.json --design > $O/hardness_gate_design.txt 2>&1; echo "hardness_gate rc=$?"
( python3 -B $TOOLS/gradable_surface.py validate --task-dir $T; python3 -B $TOOLS/gradable_surface.py gradeable-report --task-dir $T ) > $O/gradable_surface.txt 2>&1; echo "surface rc=$?"
python3 -B $TOOLS/rubric_skeleton.py check --task-dir $T > $O/rubric_skeleton_check.txt 2>&1; echo "skeleton rc=$?"
python3 -B $TOOLS/difficulty_budget.py table --task-dir $T > $O/difficulty_budget_table.md 2>&1; echo "budget table rc=$?"
python3 -B $TOOLS/difficulty_budget.py check --task-dir $T > $O/difficulty_budget_check.txt 2>&1; echo "budget check rc=$?"
python3 -B $TOOLS/hardness_v2_check.py --design --task-dir $T > $O/hardness_v2_check.txt 2>&1; echo "v2 rc=$?"
python3 -B $TOOLS/trap_liveness.py --design --task-dir $T > $O/trap_liveness.txt 2>&1; echo "liveness rc=$?"
python3 -B $P/policy_scores.py > $O/policy_scores.txt 2>&1; echo "policy rc=$?"
head -1 $O/hardness_gate_design.txt; tail -1 $O/hardness_gate_design.txt
head -1 $O/gradable_surface.txt | cut -c1-90
head -1 $O/rubric_skeleton_check.txt
head -1 $O/difficulty_budget_check.txt
python3 -B $P/build_review.py > $O/_build_review.log 2>&1 || { echo "build_review failed"; cat $O/_build_review.log; exit 1; }

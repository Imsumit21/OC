#!/bin/bash
# Rebuild the plan, shortcut probe, self-review and check from rows.json, then run both stage gates (no --paste).
# Usage: run_pipeline.sh [--rubric]   (--rubric first runs build_rubric.py so rows.json is regenerated)
cd /Users/sumit/Source/OC || exit 1
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs
G=Task_Authoring/task_inputs/Working_Files/plan/rubric
PLAN=Task_Authoring/task_inputs/Working_Files/09_Rubric_Writing_Plan.md
PY="python3.12 -B"
if [ "$1" = "--rubric" ]; then
  (cd $G && python3.12 -B build_rubric.py) 2>&1 | tail -1 | cut -c1-160
fi
$PY $G/build_plan.py --visibility 2>&1 | tail -1 | cut -c1-160
$PY $G/build_plan.py 2>&1 | tail -1 | cut -c1-160
$PY Task_Authoring/tools/shortcut_probe.py leonard_hayes $PLAN > $G/probe_raw.txt 2> $G/probe_err.txt
grep -m1 "SHORTCUT PROBE" $G/probe_raw.txt | cut -c1-170
grep "^verdict" $G/probe_raw.txt | cut -c1-120
$PY $G/build_selfreview.py --probe 2>&1 | tail -1 | cut -c1-200
$PY $G/build_selfreview.py 2>&1 | tail -1 | cut -c1-200
$PY $G/build_plan.py 2>&1 | tail -1 | cut -c1-160
$PY $G/build_check.py 2>&1 | tail -1 | cut -c1-200
echo PIPELINE_DONE
$PY Task_Authoring/tools/stage_gate.py rubric-writing Task_Authoring/task_inputs > $G/gate_writing.txt 2>&1
tail -3 $G/gate_writing.txt | cut -c1-240
$PY Task_Authoring/tools/stage_gate.py rubric-check Task_Authoring/task_inputs > $G/gate_check.txt 2>&1
tail -3 $G/gate_check.txt | cut -c1-240
echo GATES_DONE

#!/bin/bash
# Rebuild the plan, probe, self-review and check from rows.json, then run both stage gates.
cd /Users/sumit/Source/OC || exit 1
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputsN2
G=Task_Authoring/task_inputsN2/Working_Files/rubric_gen
PY="$HOME/.local/bin/python3.12 -B"
PLAN=Task_Authoring/task_inputsN2/Working_Files/09_Rubric_Writing_Plan.md
$PY $G/build_plan.py --visibility 2>&1 | tail -1 | cut -c1-160
$PY $G/build_plan.py 2>&1 | tail -1 | cut -c1-160
$PY Task_Authoring/tools/shortcut_probe.py claire_morgan $PLAN > $G/probe_raw.txt 2>$G/probe_err.txt
grep -m1 "SHORTCUT PROBE" $G/probe_raw.txt | cut -c1-170
grep "^verdict" $G/probe_raw.txt | cut -c1-120
$PY $G/build_selfreview.py --probe 2>&1 | tail -1 | cut -c1-160
$PY $G/build_selfreview.py 2>&1 | tail -1 | cut -c1-160
$PY $G/build_plan.py 2>&1 | tail -1 | cut -c1-160
$PY $G/build_check.py 2>&1 | tail -1 | cut -c1-160
echo PIPELINE_DONE
$PY Task_Authoring/tools/stage_gate.py rubric-writing Task_Authoring/task_inputsN2 --paste > $G/gate_writing.txt 2>&1
tail -3 $G/gate_writing.txt | cut -c1-240
grep -n "FAIL\|BLOCK\|WARN" $G/gate_writing.txt | cut -c1-260 | head -10
$PY Task_Authoring/tools/stage_gate.py rubric-check Task_Authoring/task_inputsN2 --paste > $G/gate_check.txt 2>&1
tail -3 $G/gate_check.txt | cut -c1-240
grep -n "FAIL\|BLOCK\|WARN" $G/gate_check.txt | cut -c1-260 | head -10
echo GATES_DONE

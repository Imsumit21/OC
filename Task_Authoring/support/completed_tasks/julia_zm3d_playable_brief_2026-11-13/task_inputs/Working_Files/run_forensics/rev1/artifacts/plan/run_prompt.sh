#!/bin/zsh
# After phase2 of run_all.sh (injection gate PASS on the current SQL): friction slot, prompt brief, prompt check.
# Usage: zsh .../plan/run_prompt.sh            (the prompt text in 04_Prompt.txt is never written here)
set -u
ROOT=/Users/sumitkumar/Source/Outlier/OC
cd $ROOT
export TASK_AUTHORING_TASK_DIR=$ROOT/Task_Authoring/task_inputs
T=Task_Authoring/task_inputs
W=$T/Working_Files
P=$W/plan
O=$P/out
TOOLS=Task_Authoring/tools
gate() { python3 -B $TOOLS/stage_gate.py $1 $T --paste > $O/stage_gate_$2.txt 2>&1; python3 -B $TOOLS/stage_gate.py $1 $T 2>&1 | grep -E "STAGE GATE|^\[FAIL\]" | cut -c1-${3:-100}; }
python3 -B $P/write_friction.py && gate error-async error_async
python3 -B $P/brief_search.py | tail -1
python3 -B $P/assemble_brief.py || exit 1
gate prompt-writing prompt_writing
python3 -B $TOOLS/hardness_v2_check.py --task-dir $T > $O/hardness_v2_prompt.txt 2>&1
python3 -B $P/assemble_prompt_check.py || exit 1
python3 -B $P/build_review_prompt.py || exit 1
gate prompt-check prompt_check 600

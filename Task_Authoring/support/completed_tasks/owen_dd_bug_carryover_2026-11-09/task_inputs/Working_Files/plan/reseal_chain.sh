#!/usr/bin/env bash
# Re-seals the local gate chain after a dossier-only change: dossier, injection, error-async, brief, prompt check.
set -u
cd "$(dirname "$0")/../../../.." || exit 2
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs
T=Task_Authoring/task_inputs; W=$T/Working_Files; O=$W/plan/out; G=Task_Authoring/tools/stage_gate.py
python3 $W/plan/assemble_dossier.py
python3 $G injection $T --paste > $O/stage_gate_injection.txt 2>&1; echo "injection $?"
touch $T/03_Error_Async_Config.txt; python3 $G error-async $T --paste > $O/stage_gate_error_async.txt 2>&1; echo "error-async $?"
touch $W/04_Prompt_Writing_Brief.md; python3 $G prompt-writing $T --paste > $O/stage_gate_brief.txt 2>&1; echo "brief $?"
touch $W/04_Prompt_Check.md; python3 $G prompt-check $T --paste > $O/stage_gate_check.txt 2>&1; echo "check $?"

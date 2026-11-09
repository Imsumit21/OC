#!/bin/bash
cd /Users/sumit/Source/OC
"$HOME/.local/bin/python3.12" -B Task_Authoring/tools/hardness_forecast.py forecast --design --task-dir Task_Authoring/task_inputs --model claude-opus-5-5 --mechanisms ADV,LETTER,TOLD,ASOF,FAM,BOARD,ASK,BOUNCE,EXT,ALIAS --max-k 10 --allow-max-k 10 "$@"

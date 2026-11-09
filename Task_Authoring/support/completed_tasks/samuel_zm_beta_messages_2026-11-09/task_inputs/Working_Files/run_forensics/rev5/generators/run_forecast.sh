#!/bin/sh
# usage: run_forecast.sh [--preregister]  (workspace root). Rates are disclosed design overrides, UNCALIBRATED.
S="placement-measured-on-stored-runs"
exec python3 -B Task_Authoring/tools/hardness_forecast.py forecast --design --task-dir Task_Authoring/task_inputsK --model claude-opus-5-5 \
  --mechanisms DONE,CORR,DEP,QA,ALIAS,FILT,BUILT,FOLLOW \
  --mechanism-rate rule:DONE=0.45@douglas-inline-comments-opened-1of6 \
  --mechanism-rate rule:CORR=0.55@bridge-reply-under-unrelated-root-caught-20to30pct \
  --mechanism-rate rule:DEP=0.25@julia-judgement-traps-rarely-land \
  --mechanism-rate rule:QA=0.55@julia-dm-thread-replies-discriminated \
  --mechanism-rate rule:ALIAS=0.30@ledger-scope_alias-mean-0.33 \
  --mechanism-rate rule:FILT=0.45@q4-rev3-item-outside-filter-landed \
  --mechanism-rate rule:BUILT=0.50@julia-get_file_contents-4of6 \
  --mechanism-rate rule:FOLLOW=0.35@douglas-trello_get_comments-3of6 \
  --draws ${DRAWS:-3000} "$@"

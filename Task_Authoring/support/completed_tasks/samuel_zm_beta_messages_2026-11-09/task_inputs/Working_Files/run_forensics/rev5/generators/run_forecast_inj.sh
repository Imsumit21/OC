#!/bin/sh
# usage: run_forecast_inj.sh [--preregister]  (workspace root). Rates are disclosed overrides, each sourced from stored runs. UNCALIBRATED.
TD=Task_Authoring/task_inputsK
exec python3 -B Task_Authoring/tools/hardness_forecast.py forecast --task-dir $TD --model claude-opus-5-5 --draws ${DRAWS:-3000} --out $TD/Working_Files/01c_Forecast.json \
  --channel-rate CH-DONE=0.45@douglas-inline-comments-opened-1of6 \
  --channel-rate CH-CORR=0.55@bridge-reply-under-unrelated-root-caught-20to30pct \
  --channel-rate CH-DEP=0.25@julia-judgement-traps-rarely-land \
  --channel-rate CH-QA=0.55@julia-dm-thread-replies-discriminated \
  --channel-rate CH-ALIAS=0.30@ledger-scope_alias-mean-0.33 \
  --channel-rate CH-FILT=0.45@q4-rev3-item-outside-filter-landed \
  --channel-rate CH-BUILT=0.50@julia-get_file_contents-4of6 \
  --channel-rate CH-FOLLOW=0.35@douglas-trello_get_comments-3of6 \
  --channel-rate CH-SLIP=0.10@ledger-control-slip-base-rate "$@"

#!/bin/sh
# usage: run_forecast_inj.sh [--preregister]  (workspace root). Rates are disclosed overrides, each sourced from stored runs. UNCALIBRATED.
TD=Task_Authoring/task_inputsK
exec python3 -B Task_Authoring/tools/hardness_forecast.py forecast --task-dir $TD --model claude-opus-5-5 --max-k 9 --allow-max-k 9 --draws ${DRAWS:-3000} --out $TD/Working_Files/01c_Forecast.json \
  --channel-rate CH-DONE=0.10@rev5-precheck-source-read-leaked \
  --channel-rate CH-CORR=0.60@rev5-precheck-zero-gcal-calls \
  --channel-rate CH-DEP=0.05@rev5-precheck-source-read-leaked \
  --channel-rate CH-QA=0.65@rev5-precheck-caveat-removed \
  --channel-rate CH-PULL=0.60@rev5-precheck-no-vincent-slack-search \
  --channel-rate CH-ALIAS=0.10@rev5-precheck-name-search-leaked \
  --channel-rate CH-FILT=0.45@rev5-precheck-landed-per-member-of-four \
  --channel-rate CH-BUILT=0.05@rev5-precheck-source-read-leaked \
  --channel-rate CH-FOLLOW=0.25@runs-ask-for-card-desc-attention-unmeasured \
  --channel-rate CH-SLIP=0.02@rev5-precheck-no-substantive-slips "$@"

#!/bin/sh
# usage: run_forecast.sh [--preregister]  (workspace root). Rates are disclosed design overrides, UNCALIBRATED.
S="placement-measured-on-stored-runs"
exec python3 -B Task_Authoring/tools/hardness_forecast.py forecast --design --task-dir Task_Authoring/task_inputsK --model claude-opus-5-5 \
  --mechanisms DONE,CORR,DEP,QA,PULL,ALIAS,FILT,BUILT,FOLLOW \
  --mechanism-rate rule:DONE=0.10@rev5-precheck-source-read-leaked \
  --mechanism-rate rule:CORR=0.60@rev5-precheck-zero-gcal-calls \
  --mechanism-rate rule:DEP=0.05@rev5-precheck-source-read-leaked \
  --mechanism-rate rule:QA=0.65@rev5-precheck-caveat-removed \
  --mechanism-rate rule:PULL=0.60@rev5-precheck-no-vincent-slack-search \
  --mechanism-rate rule:ALIAS=0.10@rev5-precheck-name-search-leaked \
  --mechanism-rate rule:FILT=0.65@rev5-precheck-landed-one-run \
  --mechanism-rate rule:BUILT=0.05@rev5-precheck-source-read-leaked \
  --mechanism-rate rule:FOLLOW=0.40@runs-ask-for-card-desc-attention-unmeasured \
  --max-k 9 --allow-max-k 9 --draws ${DRAWS:-3000} "$@"

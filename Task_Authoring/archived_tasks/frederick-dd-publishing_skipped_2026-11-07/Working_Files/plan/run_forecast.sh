#!/bin/sh
# UNCALIBRATED. Disclosed mechanism rates, each with its measured source.
python3 -B Task_Authoring/tools/hardness_forecast.py forecast --design --task-dir Task_Authoring/task_inputs --model claude-opus-5-5 \
 --mechanisms DONE,CORR,ALIAS,FILT,EXC,INPUT,DATE,FOLLOW \
 --mechanism-rate "DONE=0.50@done_gap ledger prior 0.50 n_eff 4" \
 --mechanism-rate "CORR=0.55@calendar note found by name search 3 of 7, frederick_q4_commitments rev4" \
 --mechanism-rate "ALIAS=0.55@deep Slack name sweep in 1 of 6 Q4 baselines, contact search 1-9 calls per run" \
 --mechanism-rate "FILT=0.60@either of two: Copperleaf 0.35 and Redwood 0.55, from the Linear-only fact 0 of 6 on Q4 and a reply under an unrelated post caught 20-30 percent, each given a pointer word" \
 --mechanism-rate "EXC=0.30@judgment after retrieval rarely lands, Julia 28 runs, Q4 keep-running rule" \
 --mechanism-rate "INPUT=0.45@card comment read only where the card is named, trello_get_comments 6 of 6 on bridge" \
 --mechanism-rate "DATE=0.40@lawyer thread names no publisher, boundary_date prior 0.67 n_eff 1 discounted" \
 --mechanism-rate "FOLLOW=0.50@reply under an unrelated root caught 20-30 percent, raised for the outreach sheet column" "$@"

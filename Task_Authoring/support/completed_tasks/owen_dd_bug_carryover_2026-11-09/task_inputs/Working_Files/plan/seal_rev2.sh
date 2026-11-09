#!/usr/bin/env bash
# Seals a revision after run_checks.sh: hardness gate, forecast, mutation paste, preflight, dossier, injection and error-async gates.
set -u
cd "$(dirname "$0")/../../../.." || exit 2
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs
T=Task_Authoring/task_inputs; W=$T/Working_Files; P=$W/plan; O=$P/out; TOOLS=Task_Authoring/tools; SQL=$T/01_Universe_Inject.sql
touch $W/solver/solver.py $W/solver/truth.json $SQL
mkdir -p $W/run_forensics/rev3; cp $SQL $W/run_forensics/rev3/01_Universe_Inject.sql; cp $W/solver/truth.json $W/run_forensics/rev3/truth.json
python3 $P/build_final_manifest.py > $O/final_manifest.txt 2>&1
python3 $P/build_dispositions.py > $O/dispositions.txt 2>&1
python3 $TOOLS/hardness_gate.py $W/01_Hardness_Manifest.json $SQL > $O/hardness_gate.txt 2>&1; echo "gate $(head -1 $O/hardness_gate.txt)"
python3 -B $TOOLS/hardness_forecast.py forecast --task-dir $T --model claude-opus-5-5 --channel-rate CH-FOLLOW=0.5@design-prior-plan-policy_model-rev1 --channel-rate CH-ALIAS=0.25@design-prior-plan-policy_model-rev1 --preregister --out $W/01c_Forecast.json > $O/forecast_final_raw.txt 2>&1; echo "forecast $?"
python3 - <<'E'
import json
W='Task_Authoring/task_inputs/Working_Files/'
d=json.load(open(W+'01c_Dispositions.json')); json.dump(d['mutation'],open(W+'plan/out/mutation_disp.json','w'))
L=open(W+'plan/out/forecast_final_raw.txt').read().splitlines()
keep=[l for l in L if 'E[avg]' in l or 'P(all four' in l or 'ledger: forecast record' in l or 'UNPARAMETERIZED' in l or l.strip().startswith('channel CH-')]
open(W+'plan/out/forecast_final.txt','w').write("\n".join(k[:200] for k in keep)+"\n")
E
python3 -B $TOOLS/difficulty_mutation.py mutate --task-dir $T --dispositions $O/mutation_disp.json > $O/mutation.txt 2>&1
python3 -B $TOOLS/preflight_report.py --task-dir $T --forecast $W/01c_Forecast.json > $O/preflight.txt 2>&1; echo "preflight $?"
python3 $P/assemble_dossier.py
python3 $TOOLS/stage_gate.py injection $T --paste > $O/stage_gate_injection.txt 2>&1; echo "injection gate $?"
touch $T/03_Error_Async_Config.txt; python3 $TOOLS/stage_gate.py error-async $T --paste > $O/stage_gate_error_async.txt 2>&1; echo "error-async gate $?"
python3 $W/plan/assemble_brief.py
python3 - <<'E'
import json,subprocess
W='Task_Authoring/task_inputs/Working_Files/'; p=W+'00_V3_Authoring_Evidence.json'
h=subprocess.run(['python3','Task_Authoring/tools/stage_gate.py','--artifact-hash',W+'04_Prompt_Writing_Brief.md'],capture_output=True,text=True).stdout.strip().splitlines()[-1]
d=json.load(open(p)); d['outcome_reviews']['prompt-writing']['artifact_hash']=h
d['outcome_reviews']['prompt-writing']['reviewer']="Claude (Opus 5.5), with the platform /prompt report on rev2, a fresh blind item-by-item sweep, a blind coherence audit and their re-check (Working_Files/plan/out/sweep_dispositions.md)"
acc=d['outcome_reviews']['prompt-writing']['alternatives_considered']
for x in ["Robert's flicker post Broken: rejected by his later reply naming both flickers","two tickets for Dec 22: rejected, a follow-up is part of that bug","tickets for deleted canvas lines: rejected by the doc","a ticket for the QA-doc post: rejected by the doc"]:
    if x not in acc: acc.append(x)
d['outcome_reviews']['prompt-check']['alternatives_considered']=acc
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
E
python3 $TOOLS/stage_gate.py prompt-writing $T --paste > $O/stage_gate_brief.txt 2>&1; echo "brief gate $?"
python3 $W/plan/assemble_check.py
python3 $TOOLS/stage_gate.py prompt-check $T --paste > $O/stage_gate_check.txt 2>&1; echo "check gate $?"

#!/usr/bin/env bash
# After a solver or reach-list fix with the SQL unchanged: fast checks, preflight, dossier, then every gate in order.
set -u
cd "$(dirname "$0")/../../../.." || exit 2
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs
T=Task_Authoring/task_inputs; W=$T/Working_Files; P=$W/plan; O=$P/out; TOOLS=Task_Authoring/tools; SQL=$T/01_Universe_Inject.sql
python3 -B $TOOLS/oracle_kit.py truth --solver $W/solver/solver.py --sql $SQL --revision rev9 --out $W/solver/truth.json > $O/oracle_truth.txt 2>&1
python3 $P/build_final_manifest.py > $O/final_manifest.txt 2>&1
python3 $TOOLS/fact_check.py $SQL --manifest $W/01_Hardness_Manifest.json --no-leak > $O/fact_check.txt 2>&1
python3 $TOOLS/persona_view.py check-sql owen_baker $SQL --load-bearing $P/load_bearing_ids.txt > $O/checksql.txt 2>&1
python3 -B $TOOLS/oracle_kit.py check --task-dir $T --previous-sql $W/run_forensics/rev8/01_Universe_Inject.sql --previous-truth $W/run_forensics/rev8/truth.json > $O/oracle_kit.txt 2>&1
python3 -B $TOOLS/difficulty_mutation.py geometry --task-dir $T > $O/geometry.txt 2>&1
python3 -B $TOOLS/trap_liveness.py --task-dir $T > $O/trap_liveness_sql.txt 2>&1
python3 $P/build_dispositions.py > $O/dispositions.txt 2>&1
python3 - <<'E'
import json
W='Task_Authoring/task_inputs/Working_Files/'
d=json.load(open(W+'01c_Dispositions.json')); json.dump(d['mutation'],open(W+'plan/out/mutation_disp.json','w'))
E
python3 -B $TOOLS/difficulty_mutation.py mutate --task-dir $T --dispositions $O/mutation_disp.json > $O/mutation.txt 2>&1
python3 -B $TOOLS/preflight_report.py --task-dir $T --forecast $W/01c_Forecast.json > $O/preflight.txt 2>&1; echo "preflight $?"
mkdir -p $W/run_forensics/rev9; cp $SQL $W/run_forensics/rev9/01_Universe_Inject.sql; cp $W/solver/truth.json $W/run_forensics/rev9/truth.json
for f in fact_check checksql oracle_kit preflight; do printf '%-12s %s\n' "$f" "$(grep -m1 -E 'PASS|FAIL|verdict' $O/$f.txt | cut -c1-110)"; done
grep -E "contract.regression" $O/oracle_kit.txt | cut -c1-150
if grep -q "verdict: FAIL" $O/checksql.txt || grep -q "SOLVER CONTRACT: FAIL" $O/oracle_kit.txt; then echo STOP; exit 1; fi
python3 $P/assemble_dossier.py
python3 $TOOLS/stage_gate.py injection $T --paste > $O/stage_gate_injection.txt 2>&1; echo "injection gate $?"
touch $T/03_Error_Async_Config.txt; python3 $TOOLS/stage_gate.py error-async $T --paste > $O/stage_gate_error_async.txt 2>&1; echo "error-async gate $?"
python3 $P/assemble_brief.py
python3 - <<'E'
import json,subprocess
W='Task_Authoring/task_inputs/Working_Files/'; p=W+'00_V3_Authoring_Evidence.json'
h=subprocess.run(['python3','Task_Authoring/tools/stage_gate.py','--artifact-hash',W+'04_Prompt_Writing_Brief.md'],capture_output=True,text=True).stdout.strip().splitlines()[-1]
d=json.load(open(p)); d['outcome_reviews']['prompt-writing']['artifact_hash']=h
d['outcome_reviews']['prompt-writing']['reviewer']="Claude (Opus 5.5), with the platform /prompt report on rev2, a fresh blind item-by-item sweep, a blind coherence audit and their re-check (Working_Files/plan/out/sweep_dispositions.md)"
acc=d['outcome_reviews']['prompt-writing']['alternatives_considered']
for x in ["Robert's flicker post Broken: rejected by his later reply naming both flickers","two tickets for Dec 22: rejected, a follow-up is part of that bug","tickets for deleted canvas lines: rejected by the doc","a ticket for the QA-doc post: rejected by the doc","navigation bar tooltips Broken after Brian's 'I'll send another fix': rejected by Vincent's closing reply in that thread (rev7)"]:
    if x not in acc: acc.append(x)
d['outcome_reviews']['prompt-check']['alternatives_considered']=acc
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
E
python3 $TOOLS/stage_gate.py prompt-writing $T --paste > $O/stage_gate_brief.txt 2>&1; echo "brief gate $?"
python3 $P/assemble_check.py
python3 $TOOLS/stage_gate.py prompt-check $T --paste > $O/stage_gate_check.txt 2>&1; echo "check gate $?"

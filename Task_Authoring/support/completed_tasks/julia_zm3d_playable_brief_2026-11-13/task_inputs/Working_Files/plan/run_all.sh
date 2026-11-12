#!/bin/zsh
# One fix round, in dependency order. Use after any change to plan/planned_texts.py, plan/design_model.py or a builder.
#   zsh .../plan/run_all.sh phase1   design artifacts -> scenario gate -> SQL and every injection check -> new reviewer briefs
#   zsh .../plan/run_all.sh phase2   (after the two reviewers wrote findings_<n>.json for the new briefs)
#                                    sweep record + check -> injection review record -> dossier -> injection gate
# Nothing is executed against a database; platform commands stay with the user.
set -u
ROOT=/Users/sumitkumar/Source/Outlier/OC
cd $ROOT
export TASK_AUTHORING_TASK_DIR=$ROOT/Task_Authoring/task_inputs
T=Task_Authoring/task_inputs
W=$T/Working_Files
P=$W/plan
O=$P/out
TOOLS=Task_Authoring/tools
PHASE=${1:-phase1}

if [[ $PHASE == phase1 ]]; then
  echo "== design artifacts"
  zsh $P/run_checks.sh || exit 1
  python3 -B $P/reach_table.py > /dev/null || { echo "reach_table failed"; exit 1; }
  python3 -B $P/assemble_design.py > /dev/null || { echo "assemble_design failed"; exit 1; }
  python3 -B $P/build_evidence.py > /dev/null || { echo "build_evidence failed"; exit 1; }
  python3 -B $TOOLS/stage_gate.py scenario $T --paste > $O/stage_gate_scenario.txt 2>&1
  head -1 $O/stage_gate_scenario.txt | cut -c1-60
  grep -q "STAGE GATE scenario: PASS" $O/stage_gate_scenario.txt || { grep -E "^\[FAIL\]" $O/stage_gate_scenario.txt | cut -c1-400; exit 1; }
  echo "== injection"
  # the solver reads its rules from the draft manifest at run time; its contract is re-checked below on the current inputs
  touch $W/solver/solver.py
  zsh $P/run_injection.sh build forecast || exit 1
  python3 -B $P/natural_retrieval_injection.py > /dev/null || { echo "natural retrieval failed"; exit 1; }
  # keep the earlier round (briefs and findings) before the briefs are rebuilt from the new SQL bytes
  C=$W/local_reviews/coherence
  if ls $C/findings_*.json > /dev/null 2>&1; then
    n=1; while [[ -d $C/round$n ]]; do n=$((n+1)); done
    mkdir -p $C/round$n && mv $C/findings_*.json $C/round$n/ && cp $C/brief_*.md $C/round$n/
    echo "archived the earlier briefs and findings in round$n"
  fi
  for r in 1 2; do python3 -B $TOOLS/coherence_sweep.py brief --task-dir $T --reviewer $r 2>&1 | tail -1 | cut -c1-160; done
  echo "phase1 done: hand brief_1.md and brief_2.md to the two reviewers, then run phase2"
else
  python3 -B $P/build_findings_map.py || exit 1
  python3 -B $P/build_settlements.py || exit 1
  python3 -B $P/build_sweep.py || exit 1
  python3 -B $TOOLS/coherence_sweep.py check --task-dir $T > $O/sweep_check.txt 2>&1; echo "sweep check rc=$? $(head -1 $O/sweep_check.txt | cut -c1-100)"
  grep -vE "^\[PASS\]" $O/sweep_check.txt | sed -n 2,20p | cut -c1-400
  python3 -B $P/build_review_injection.py || exit 1
  python3 -B $P/assemble_dossier.py || exit 1
  python3 -B $TOOLS/stage_gate.py injection $T --paste > $O/stage_gate_injection.txt 2>&1
  head -1 $O/stage_gate_injection.txt | cut -c1-70
  grep -E "^\[(FAIL|WARN)\]" $O/stage_gate_injection.txt | cut -c1-500
fi

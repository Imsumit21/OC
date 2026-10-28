#!/bin/zsh
cd /Users/sumitkumar/Source/Outlier/OC
L=Task_Authoring/support/fix_session_2026-10-25/logs/f1
FP=Task_Authoring/support/fix_session_2026-10-25/scripts/fingerprint.py
F1=Task_Authoring/support/fix_session_2026-10-25/scripts/f1_acceptance.py
mkdir -p $L/round2
python3 -B $FP $L/fp_before_round2.tsv --only support/local_search support/hardness_ledger > /dev/null
date '+start %H:%M:%S'
for s in 7 8 9; do (python3 -B $F1 $L/round2/seed$s --seed $s > $L/round2/seed$s.txt 2>&1; echo "seed $s exit=$?") & done
wait
date '+end %H:%M:%S'
python3 -B $F1 --summarize $L/round2/seed7 $L/round2/seed8 $L/round2/seed9; echo "summarize exit=$?"
python3 -B $FP $L/fp_after_round2.tsv --only support/local_search support/hardness_ledger > /dev/null
python3 -B $FP --diff $L/fp_before_round2.tsv $L/fp_after_round2.tsv
(cd Task_Authoring/support/backtests/season_pass/rev14 && shasum -a 256 -c SHA256SUMS --quiet && echo "rev14 SHA256SUMS ok")
echo DONE

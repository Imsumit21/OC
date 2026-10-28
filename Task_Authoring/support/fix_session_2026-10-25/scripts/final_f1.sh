#!/bin/zsh
# The F1 replay for seeds 7, 8 and 9 (in parallel), then the cross-seed summary; shared-cache fingerprints and the
# rev14 SHA256SUMS around it (run from the workspace root, through detach.py).
L=Task_Authoring/support/fix_session_2026-10-25/logs/f1
FP=Task_Authoring/support/fix_session_2026-10-25/scripts/fingerprint.py
F1=Task_Authoring/support/fix_session_2026-10-25/scripts/f1_acceptance.py
mkdir -p $L/final3
python3 -B $FP $L/fp_before_final3.tsv --only support/local_search support/hardness_ledger > /dev/null
date '+start %H:%M:%S'
for s in 7 8 9; do (python3 -B $F1 $L/final3/seed$s --seed $s > $L/final3/seed$s.txt 2>&1; echo "seed $s exit=$?") & done
wait
date '+end %H:%M:%S'
python3 -B $F1 --summarize $L/final3/seed7 $L/final3/seed8 $L/final3/seed9; echo "summarize exit=$?"
python3 -B $FP $L/fp_after_final3.tsv --only support/local_search support/hardness_ledger > /dev/null
python3 -B $FP --diff $L/fp_before_final3.tsv $L/fp_after_final3.tsv
(cd Task_Authoring/support/backtests/season_pass/rev14 && shasum -a 256 -c SHA256SUMS --quiet && echo "rev14 SHA256SUMS ok")
echo DONE

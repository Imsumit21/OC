#!/bin/zsh
# The final move suite, with shared-cache fingerprints around it (run from the workspace root, through detach.py).
L=Task_Authoring/support/fix_session_2026-10-25/logs
FP=Task_Authoring/support/fix_session_2026-10-25/scripts/fingerprint.py
python3 -B $FP $L/fp_p1_suite4_before.tsv --only support/local_search support/hardness_ledger > /dev/null
date '+start %H:%M:%S'
python3 -B Task_Authoring/tools/selftest_sandbox.py --suite move; echo "exit=$?"
date '+end %H:%M:%S'
python3 -B $FP $L/fp_p1_suite4_after.tsv --only support/local_search support/hardness_ledger > /dev/null
python3 -B $FP --diff $L/fp_p1_suite4_before.tsv $L/fp_p1_suite4_after.tsv
echo DONE

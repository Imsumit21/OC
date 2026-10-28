#!/bin/zsh
# Suite acceptance on the final P1 tree: the 14 move self-tests, with the shared-cache fingerprint around them.
cd /Users/sumitkumar/Source/Outlier/OC
L=Task_Authoring/support/fix_session_2026-10-25/logs
FP=Task_Authoring/support/fix_session_2026-10-25/scripts/fingerprint.py
python3 -B $FP $L/fp_suite_round5_before.tsv --only support/local_search support/hardness_ledger > /dev/null
date '+start %H:%M:%S'
python3 -B Task_Authoring/tools/selftest_sandbox.py --suite move; echo "exit=$?"
date '+end %H:%M:%S'
python3 -B $FP $L/fp_suite_round5_after.tsv --only support/local_search support/hardness_ledger > /dev/null
python3 -B $FP --diff $L/fp_suite_round5_before.tsv $L/fp_suite_round5_after.tsv
echo DONE

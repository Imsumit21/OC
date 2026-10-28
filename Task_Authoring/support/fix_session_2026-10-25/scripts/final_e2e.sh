#!/bin/zsh
# The final E2E run, with shared-cache fingerprints around it (run from the workspace root, through detach.py).
L=Task_Authoring/support/fix_session_2026-10-25/logs/e2e
FP=Task_Authoring/support/fix_session_2026-10-25/scripts/fingerprint.py
python3 -B $FP $L/fp_before7.tsv --only support/local_search support/hardness_ledger > /dev/null
date '+start %H:%M:%S'
python3 -B Task_Authoring/support/fixtures/season_pass_rev14/e2e_rev14.py; echo "exit=$?"
date '+end %H:%M:%S'
python3 -B $FP $L/fp_after7.tsv --only support/local_search support/hardness_ledger > /dev/null
python3 -B $FP --diff $L/fp_before7.tsv $L/fp_after7.tsv
echo DONE

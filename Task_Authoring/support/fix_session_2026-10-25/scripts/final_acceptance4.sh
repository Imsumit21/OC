#!/bin/zsh
# Round-4 acceptance on the final tree, in the order the session requires: self-tests (suite), falsification, E2E.
D=Task_Authoring/support/fix_session_2026-10-25; L=$D/logs; S=$D/scripts
date '+start %H:%M:%S'
echo "== suite (14 move self-tests), sandboxed"
python3 -B Task_Authoring/tools/selftest_sandbox.py --suite move > $L/p1_suite_round16.log 2>&1; echo "exit=$?"
grep -c "^  ok " $L/p1_suite_round16.log | sed 's/^/ok lines: /'
echo "== falsify_g1"
python3 -B $S/falsify_g1.py > $L/g1/falsify_g1.round16.txt 2>&1; echo "exit=$?"; tail -1 $L/g1/falsify_g1.round16.txt
echo "== falsify_h1"
python3 -B $S/falsify_h1.py > $L/h1/falsify_h1.round16.txt 2>&1; echo "exit=$?"; tail -1 $L/h1/falsify_h1.round16.txt
echo "== E2E rev14"
python3 -B Task_Authoring/support/fixtures/season_pass_rev14/e2e_rev14.py > $L/e2e/e2e_round22.log 2>&1; echo "exit=$?"; tail -1 $L/e2e/e2e_round22.log
date '+end %H:%M:%S'
echo DONE

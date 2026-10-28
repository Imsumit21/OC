#!/bin/zsh
cd /Users/sumitkumar/Source/Outlier/OC
python3 -B Task_Authoring/support/fix_session_2026-10-25/scripts/falsify_g1.py > Task_Authoring/support/fix_session_2026-10-25/logs/g1/falsify_g1.round2.txt 2>&1; echo "g1=$?"
python3 -B Task_Authoring/support/fix_session_2026-10-25/scripts/falsify_h1.py > Task_Authoring/support/fix_session_2026-10-25/logs/h1/falsify_h1.round2.txt 2>&1; echo "h1=$?"
echo DONE

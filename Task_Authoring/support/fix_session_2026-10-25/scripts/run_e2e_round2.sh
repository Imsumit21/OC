#!/bin/zsh
cd /Users/sumitkumar/Source/Outlier/OC
python3 -B Task_Authoring/support/fixtures/season_pass_rev14/e2e_rev14.py --draws 400
echo "E2E_RC=$?"
echo DONE

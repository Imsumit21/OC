#!/bin/zsh
# F1 acceptance protocol, fourth revision: seeds 1/2/3 at the pre-registered 20,000 draws, then the 13-id summary.
cd /Users/sumitkumar/Source/Outlier/OC
L=Task_Authoring/support/fix_session_2026-10-25/logs/f1/protocol4
for s in 1 2 3; do
  date "+seed $s start %H:%M:%S"
  python3 -B Task_Authoring/support/fix_session_2026-10-25/scripts/f1_protocol.py "$L/seed$s" --seed $s
  date "+seed $s end %H:%M:%S"
done
date "+summarize %H:%M:%S"
python3 -B Task_Authoring/support/fix_session_2026-10-25/scripts/f1_protocol.py --summarize "$L/seed1" "$L/seed2" "$L/seed3"
echo DONE

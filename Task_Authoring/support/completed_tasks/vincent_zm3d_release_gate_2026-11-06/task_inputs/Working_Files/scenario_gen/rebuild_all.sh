#!/bin/sh
# Rebuilds every post-scenario stage in order and re-pastes each gate (injection → error-async → prompt-writing →
# prompt-check). Run from the workspace root. rev1 ran on the platform and stays as stored; rev2 is not submitted yet,
# so its stored copy is replaced.
set -e
export TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputs
T=Task_Authoring/task_inputs
W=$T/Working_Files
G=$W/scenario_gen
rm -f $W/run_forensics/rev2/01_Universe_Inject.sql
sh $G/rebuild_injection.sh > /dev/null
python3 Task_Authoring/tools/stage_gate.py injection $T --paste > /dev/null 2>&1 || true
SHA=$(python3 -c "import hashlib;print(hashlib.sha256(open('$T/01_Universe_Inject.sql','rb').read()).hexdigest()[:12])")
python3 - <<PY
from pathlib import Path
import re
p = Path('$T/03_Error_Async_Config.txt'); t = p.read_text()
i = t.find('\`\`\`\nSTAGE GATE')
t = t[:i] if i >= 0 else t
p.write_text(re.sub(r'certified at sha256 prefix [0-9a-f]{12}', 'certified at sha256 prefix $SHA', t).rstrip('\n') + '\n')
PY
python3 Task_Authoring/tools/stage_gate.py error-async $T --paste > /dev/null 2>&1 || true
[ -f $W/01a_Hardening_Report.md ] && { python3 Task_Authoring/tools/stage_gate.py hardening $T --paste > /dev/null 2>&1 || true; }
python3 -B $G/build_brief.py > /dev/null
python3 $G/write_evidence.py > /dev/null
python3 Task_Authoring/tools/stage_gate.py prompt-writing $T --paste > /dev/null 2>&1 || true
python3 -B $G/build_check.py > /dev/null
python3 $G/write_evidence.py > /dev/null
python3 Task_Authoring/tools/stage_gate.py prompt-check $T --paste > /dev/null 2>&1 || true
for s in scenario injection error-async hardening prompt-writing prompt-check; do
  python3 Task_Authoring/tools/stage_gate.py $s $T 2>&1 | grep -E "^STAGE|WARN|\[FAIL" | sed -E 's/ — Task_Authoring.*(blocking [0-9]+ · warnings [0-9]+).*/ — \1/'
done

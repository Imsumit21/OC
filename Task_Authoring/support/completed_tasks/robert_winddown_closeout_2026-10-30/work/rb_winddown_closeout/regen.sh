#!/bin/sh
# Regenerate ids, manifest, gate capture and the design doc. Arg 1 = capture dir (reach/coll/resolve/hardness text).
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
WS=$(cd "$HERE/../../../.." && pwd)
CAP=$1
python3 "$HERE/mint_ids.py" >/dev/null
python3 "$HERE/build_manifest.py" >/dev/null
cd "$WS"
python3 Task_Authoring-2/tools/hardness_gate.py Task_Authoring-2/task_inputs/Working_Files/01_Hardness_Manifest.draft.json --design > "$CAP/hardness.txt" || true
python3 "$HERE/build_design.py" "$CAP"
head -1 "$CAP/hardness.txt"

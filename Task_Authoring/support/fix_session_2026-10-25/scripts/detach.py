#!/usr/bin/env python3
"""Start a shell script in its own session, so a kill of the client's process group (a "location shut down") doesn't
end it. Its output is appended to LOG; the script prints DONE as its last line. Prints the PID.

Usage (workspace root): python3 -B Task_Authoring/support/fix_session_2026-10-25/scripts/detach.py LOG SCRIPT.sh
"""
import subprocess
import sys

log, script = sys.argv[1], sys.argv[2]
with open(log, "ab") as fh:
    p = subprocess.Popen(["/bin/zsh", script], stdin=subprocess.DEVNULL, stdout=fh, stderr=subprocess.STDOUT,
                         start_new_session=True)
print(p.pid)

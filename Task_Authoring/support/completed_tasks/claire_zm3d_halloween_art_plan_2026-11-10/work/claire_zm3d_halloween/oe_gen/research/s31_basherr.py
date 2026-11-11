import sys, json, re
sys.path.insert(0, ".")
import traj_lib as T
for r in T.RUNS:
    for c in T.load(r)[1]:
        if c["name"] in ("Bash","Read"):
            t = T.text(c["out"]) or ""
            m = re.search(r"(Traceback \(most recent call last\)|BrokenPipeError|[A-Za-z]*Error: |command not found|No such file|Permission denied|Killed)", t)
            if m:
                i = t.find(m.group(1))
                tail = t[-170:].replace("\n"," / ")
                print(f"{r}#{c['seq']} {c['name']} match={m.group(1)!r} cmd={json.dumps(c['input'])[:110]}\n    tail={tail}")

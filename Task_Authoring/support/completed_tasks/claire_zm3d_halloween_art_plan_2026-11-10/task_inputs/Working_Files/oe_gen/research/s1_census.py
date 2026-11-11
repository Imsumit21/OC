import sys, json, collections
sys.path.insert(0, "/Users/sumit/Source/OC/Task_Authoring/task_inputsN2/Working_Files/oe_gen/research")
import traj_lib as T
tot = collections.Counter(); byrun = collections.defaultdict(collections.Counter); raws=set()
for r in T.RUNS:
    ev, calls = T.load(r)
    print(r, "events", len(ev), "calls", len(calls), "types", collections.Counter(e.get("type") for e in ev if isinstance(e, dict)).most_common(6), "unresolved", sum(1 for c in calls if c["out"] is None), "is_error", sum(1 for c in calls if c["err"]))
    for c in calls:
        tot[c["name"]] += 1; byrun[c["name"]][r] += 1; raws.add(c["raw"])
print()
for n, k in tot.most_common():
    print(f"{n:42s} {k:5d} " + " ".join(f"{r}:{byrun[n][r]}" for r in T.RUNS))
print(sorted(raws)[:10])

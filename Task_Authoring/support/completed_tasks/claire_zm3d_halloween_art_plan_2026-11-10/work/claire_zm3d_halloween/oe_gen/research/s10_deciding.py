import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
TARGETS = {
 "A Frederick Fri Oct 10 (C0880U9751A reply)": ["not the 15th", "Fri Oct 10", "manual review for the next few weeks"],
 "A0 parent thread 1759211437.306779": ["1759211437.306779"],
 "B Marcus re-recorded 3": ["re-recorded 3 of the old ua cuts"],
 "C Robert We can't ship these": ["ship these"],
 "D1 Martin vacation": ["on vacation Oct 6-15", "1759243286.478812"],
 "D2 Leonard julia on the ad statics": ["julia on the ad statics"],
 "E Unity retention restart": ["Unity retention restart"],
 "E2 retention body": ["iOS retention campaigns went back on"],
 "F Trello end card 001": ["end card 001 still has the old zombies"],
 "F2 Marketing Video Refresh": ["Marketing Video Refresh"],
 "G Julia 4:5 Trello note": ["never made it onto the live creatives sheet"],
}
for name, pats in TARGETS.items():
    print("\n#####", name, pats)
    for r in T.RUNS:
        ev, calls = T.load(r)
        hits = []
        for c in calls:
            t = T.text(c["out"])
            if any(p.lower() in t.lower() for p in pats):
                inp = c["input"]
                if c["name"] in ("Bash",): inp = {"command": (inp.get("command") or "")[:90]}
                hits.append(f'#{c["seq"]} {c["name"]} {json.dumps(inp, ensure_ascii=False)[:150]}')
        print(f"  {r}: {len(hits)} hit(s)")
        for h in hits[:8]: print("     ", h)

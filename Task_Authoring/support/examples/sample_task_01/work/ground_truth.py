#!/usr/bin/env python3
"""Ground truth for sample_task_01 (iteration 4): cohort, folding, tiers, fix status, current-build status, totals."""
import collections
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
co = json.loads((HERE / "cohort.json").read_text())
plan = {p["key"]: p for p in json.loads((HERE / "retest_plan.json").read_text())}
co.append(dict(key="ENG-2438", state="Bugs", prio=1, labels=["DD 2.1", "Bug"], created="2026-02-10T19:41:12Z",
               title="Stuck at 8% on the loading screen after updating to 0.3.309 from the App Store", parent=None))
co.append(dict(key="ENG-2440", state="Bugs", prio=2, labels=["DD 2.1", "Bug"], created="2026-02-13T20:31:40Z",
               title="Restore Purchases does nothing after reinstall on 0.3.309", parent=None))
CUT = {"v1_fri_noon_pt": "2026-02-13T20:00:00Z", "v3_mon_9am_pt": "2026-02-16T17:00:00Z"}

# fix references: ticket -> evidence of a merged PR that says it fixes/addresses it
# in-window (merged on/after 2025-10-13) references only; ENG-1866 (#1583, #1773) and ZOM-359 (#316) fall outside
FIX_REF = {"ENG-2331", "ZOM-542", "ZOM-616", "ZOM-614", "ENG-2277", "ENG-2400",
           "ZOM-608", "ZOM-610", "ZOM-611", "ENG-2345", "ENG-2242"}
OUT_OF_WINDOW_REF = {"ENG-1866", "ZOM-359"}
# written report dated between two merged references (counts only under the wrong "any merge" reading)
REPORT_BETWEEN_MERGES = {"ZOM-611"}
LABEL = {"Y": "still happens", "N": "could not make it happen", "I": "could not finish", "B": "not retested", "-": "not retested"}
# written reports after the merge that are not retests (Slack/DM) + Regression state
LATER_REPORT = {"ENG-2277", "ZOM-359", "ZOM-608"}


def final(code):
    return {"NY": "Y"}.get(code, code)


def retest(k):
    p = plan.get(k)
    if not p:
        return ("-", "-")
    return final(p["ios"]), final(p["android"])


def current_build(k):
    ios, andr = retest(k)
    return "NOT REPRODUCED" if (ios == "N" and andr == "N") else "REPRODUCES"


def fix_status(c, any_merge=False, ignore_window=False):
    k = c["key"]
    if k not in FIX_REF and not (ignore_window and k in OUT_OF_WINDOW_REF):
        return "NO FIX"
    ios, andr = retest(k)
    if c["state"] == "Regression" or k in LATER_REPORT or "Y" in (ios, andr) or (any_merge and k in REPORT_BETWEEN_MERGES):
        return "FIX MERGED - REPRODUCED"
    return "FIX MERGED - UNVERIFIED"


def tier(c, amended=True):
    t = {1: 1, 2: 2, 3: 3, 4: 4, 0: 3}[c["prio"]]
    if "Hot Fix - Global Launch" in c["labels"] and (not amended or c["prio"] in (1, 2)):
        t = 1
    if c["state"] == "Regression":
        t = max(1, t - 1)
    return t


def build(cutoff=CUT["v3_mon_9am_pt"], amended=True, use_retest=True, any_merge=False):
    inc = [c for c in co if "Acceptable Behavior" not in c["labels"] and c["created"] <= cutoff]
    keys = {c["key"] for c in inc}
    folded = {c["key"]: c["parent"] for c in inc if c.get("parent") in keys}
    rows = []
    for c in inc:
        if c["key"] in folded:
            continue
        grp = [c] + [x for x in inc if folded.get(x["key"]) == c["key"]]
        lot = "Not in lot - Web" if "WebGL" in c["labels"] else ("Lot A - Domino Delights" if c["key"].startswith("ENG") else "Lot B - Zombie Match 3D")
        cb = "NOT REPRODUCED" if use_retest and all(current_build(x["key"]) == "NOT REPRODUCED" for x in grp) else "REPRODUCES"
        rows.append(dict(key=c["key"], sub=[x["key"] for x in grp[1:]], lot=lot, tier=min(tier(x, amended) for x in grp),
                         fix=fix_status(c, any_merge),   # folded row takes the parent's fix status (Trello card)
                         current=cb, retest={x["key"]: tuple(LABEL[v] for v in retest(x["key"])) for x in grp}))
    return inc, rows


def totals(rows):
    t = collections.Counter((r["lot"], r["tier"]) for r in rows if r["current"] == "REPRODUCES")
    return {lot: [t[(lot, i)] for i in (1, 2, 3, 4)] for lot in ("Lot A - Domino Delights", "Lot B - Zombie Match 3D", "Not in lot - Web")}


if __name__ == "__main__":
    inc, rows = build()
    (HERE / "schedule_truth.json").write_text(json.dumps(rows, indent=1))
    print("tickets", len(inc), "rows", len(rows), "rows per lot", collections.Counter(r["lot"] for r in rows))
    print("NOT REPRODUCED rows", [r["key"] for r in rows if r["current"] == "NOT REPRODUCED"])
    print("TOTALS (rows that still reproduce):", totals(rows))
    print("fix status by lot", collections.Counter((r["lot"][:5], r["fix"]) for r in rows))
    print("-- variants --")
    print("ignoring retest:", totals(build(use_retest=False)[1]))
    print("pre-amendment tiers:", totals(build(amended=False)[1]))
    print("Friday cut-off:", totals(build(cutoff=CUT["v1_fri_noon_pt"])[1]), len(build(cutoff=CUT["v1_fri_noon_pt"])[0]))

    def ios_only(k):
        ios, _ = retest(k)
        return "NOT REPRODUCED" if ios == "N" else "REPRODUCES"
    one = [r for r in rows if r["current"] == "REPRODUCES" and all(ios_only(x) == "NOT REPRODUCED" for x in [r["key"]] + r["sub"])]
    print("rows an iOS-only reader would wrongly drop:", [r["key"] for r in one])
    flips = [r["key"] for r in rows if r["fix"] == "FIX MERGED - REPRODUCED" and r["key"] in {"ENG-2345", "ZOM-611"}]
    print("fix-status flips from retest:", flips)
    print("ignoring the window would flip:", [x for x in ("ENG-1866", "ZOM-359")])
    print("any-merge reading:", totals(build(any_merge=True)[1]), [r["key"] for r in build(any_merge=True)[1] if r["fix"] != dict((x["key"], x["fix"]) for x in rows)[r["key"]]])

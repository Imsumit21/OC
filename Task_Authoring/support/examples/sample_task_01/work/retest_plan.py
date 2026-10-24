#!/usr/bin/env python3
"""Single source for the seeded pre-sale retest (iteration 2). Writes work/retest_plan.json.

Codes per platform thread: Y = tester says it still happens; N = tester could not make it happen;
I = retest could not be finished; NY = first reply could not make it happen, a later reply in the
same thread says it happened after all; '-' = no thread on that platform (not retested).
The view the testers worked from = open ENG/ZOM tickets with label Bug or state Bugs, minus the
WebGL-labelled ones (no web build on a phone) — so ENG-1866 and ZOM-542 (Regression, no Bug label),
ENG-2406/2407/2408 and ENG-2440 (filed after the sweep) have no retest threads.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
co = json.loads((HERE / "cohort.json").read_text())
view = [c["key"] for c in co if (("Bug" in c["labels"]) or c["state"] == "Bugs") and "WebGL" not in c["labels"]]
view.append("ENG-2438")
titles = {c["key"]: c["title"] for c in co}
titles["ENG-2438"] = "Stuck at 8% on the loading screen after updating to 0.3.309 from the App Store"

special = {
    # both platforms could not make it happen -> NOT REPRODUCED
    "ENG-1853": ("N", "N"), "ENG-1854": ("B", "N"), "ENG-1878": ("N", "N"), "ENG-1928": ("N", "N"),
    "ENG-2017": ("N", "N"), "ENG-2181": ("N", "N"), "ENG-2200": ("N", "N"), "ENG-2130": ("N", "N"),
    "ZOM-237": ("N", "N"), "ZOM-591": ("N", "N"), "ZOM-598": ("N", "N"), "ZOM-610": ("N", "N"), "ZOM-611": ("N", "N"),
    "ZOM-614": ("N", "N"), "ZOM-599": ("N", "N"), "ENG-1877": ("N", "N"), "ZOM-616": ("N", "Y"),
    # one platform only -> still counts
    "ENG-1762": ("N", "Y"), "ENG-2094": ("Y", "N"), "ENG-1839": ("N", "Y"), "ENG-2191": ("Y", "N"),
    "ZOM-559": ("N", "Y"), "ZOM-606": ("Y", "N"), "ZOM-458": ("N", "Y"), "ENG-2438": ("Y", "N"),
    "ZOM-608": ("Y", "N"), "ENG-2110": ("Y", "N"),
    # could not finish -> counts
    "ENG-2400": ("I", "I"), "ENG-2190": ("N", "I"), "ENG-2242": ("I", "I"), "ZOM-517": ("N", "I"),
    "ZOM-483": ("I", "N"), "ZOM-535": ("N", "I"),
    # no android thread -> counts
    "ZOM-667": ("N", "-"), "ZOM-670": ("Y", "-"), "ENG-2402": ("N", "-"), "ENG-2349": ("Y", "-"),
    # in-thread correction -> counts
    "ENG-2109": ("NY", "Y"), "ZOM-546": ("Y", "NY"), "ENG-2350": ("NY", "N"), "ENG-2274": ("N", "NY"),
}
Y = ["still happens", "yep, same as the ticket", "happens every time", "still there", "got it first try",
     "yes, still like that", "same thing on this build", "still broken", "happens, same steps as the ticket",
     "yeah its there"]
N = ["couldn't get this to happen", "no luck after a bunch of tries", "looks fine now", "didn't see it, tried ~10x",
     "seems gone on this build", "tried a few ways, nothing", "can't make it happen anymore", "looks ok to me now"]
I_ = {"ENG-2400": ("can't check this one, it needs a 10 day gap", "same, can't wait 10 days for it"),
      "ENG-2190": (None, "need a low-end android for this, don't have one"),
      "ENG-2242": ("test account has no epic levels left, couldn't get to it", "same account problem, couldn't get there"),
      "ZOM-517": (None, "endless mode is locked on my test account, couldn't get in"),
      "ZOM-483": ("can't do a fresh install of that old build on iOS anymore", None),
      "ZOM-535": (None, "couldn't finish, game crashed on me before the boss twice")}
FIRST_N = "can't get it"
LATER_Y = "nvm, got it on the third try"

plan = []
for i, k in enumerate(view):
    ios, andr = special.get(k, ("Y", "Y"))
    entry = {"key": k, "title": titles[k], "ios": ios, "android": andr, "texts": {}}
    for plat, code, bank, off in (("ios", ios, None, i), ("android", andr, None, i + 3)):
        if code == "Y":
            entry["texts"][plat] = [Y[off % len(Y)]]
        elif code == "N":
            entry["texts"][plat] = [N[off % len(N)]]
        elif code == "I":
            entry["texts"][plat] = [I_[k][0 if plat == "ios" else 1]]
        elif code == "B":
            entry["texts"][plat] = ["only had the 0.3.307 testflight build on my phone for this one, couldn't get it to happen there"]
        elif code == "NY":
            entry["texts"][plat] = [FIRST_N, LATER_Y]
    plan.append(entry)
(HERE / "retest_plan.json").write_text(json.dumps(plan, indent=1))
print(len(plan), "tickets in the retest view;",
      sum(1 for p in plan if p["ios"] != "-"), "iOS threads;", sum(1 for p in plan if p["android"] != "-"), "android threads")

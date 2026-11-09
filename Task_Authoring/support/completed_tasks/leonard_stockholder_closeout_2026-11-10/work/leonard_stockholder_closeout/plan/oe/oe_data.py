#!/usr/bin/env python3
"""Holder data and the event list for the Leonard close-out Oracle Events. Asserted against solver/truth.json."""
import json
import os

import oe_lib as L

TRUTH = json.load(open(os.path.join(L.WF, "solver", "truth.json")))


def n(x):
    return f"{x:,}"


# issue, title, email, carta id of the option line (or None)
STOCK = [
    ("ENG-2438", "GRIFFIN GAMING PARTNERS II, L.P.", "PERSON_4337_EMAIL", None),
    ("ENG-2439", "GRIFFIN GAMING PARTNERS II SIDE FUND, L.P.", "PERSON_4337_EMAIL", None),
    ("ENG-2440", "[PERSON_NAME_0089] [PERSON_NAME_25152]", "PERSON_3336_EMAIL", "ES-8"),
    ("ENG-2441", "Arthur PERSON_3083_NAME", "PERSON_3063_EMAIL", None),
    ("ENG-2442", "[PERSON_NAME_4468]", "PERSON_0693_EMAIL", None),
    ("ENG-2443", "[PERSON_NAME_52949]", "PERSON_2260_EMAIL", None),
    ("ENG-2444", "Patrick Lewis", "patrick@harmonygames.co", None),
    ("ENG-2445", "[PERSON_NAME_27652]", "PERSON_2275_EMAIL", None),
    ("ENG-2446", "PERSON_3941_NAME [PERSON_NAME_0127]", "PERSON_3941_EMAIL", "ES-11"),
    ("ENG-2447", "Husnu Matthew Collins", "matthew.collins@harmonygames.co", "ES-9"),
    ("ENG-2448", "TOR Capital Limited", "PERSON_5275_EMAIL", None),
    ("ENG-2449", "PERSON_1287_NAME", "PERSON_1287_EMAIL", "ES-10"),
]
LIST_FIG = {"ENG-2438": "2,746,693, both funds on one line", "ENG-2439": "2,746,693, both funds on one line", "ENG-2440": "81,383",
            "ENG-2441": "25,432", "ENG-2442": "25,432", "ENG-2443": "25,432", "ENG-2444": "25,432", "ENG-2445": "25,432",
            "ENG-2446": "31,536", "ENG-2447": "86,470", "ENG-2448": "50,865", "ENG-2449": "31,536", "ENG-2450": "30,519",
            "ENG-2452": "8,138", "ENG-2453": "7,630", "ENG-2454": "10,173", "ENG-2455": "30,519", "ENG-2456": "22,889",
            "ENG-2457": "16,277", "ENG-2458": "3,866", "ENG-2459": "3,866", "ENG-2460": "10,173", "ENG-2461": "35,605",
            "ENG-2462": "127,162", "ENG-2463": "15,259"}
# issue, title, email, ES id, thread id, Carta name, granted, vested, as of, last day (as Carta prints them)
OPTION = [
    ("ENG-2450", "[PERSON_NAME_0043]", "PERSON_2361_EMAIL", "ES-1", "1856960433624350836", "[PERSON_NAME_0043]", 30519, 17802, "Dec. 31, 2025", "March 31, 2026"),
    ("ENG-2451", "[PERSON_NAME_0100]", "PERSON_3641_EMAIL", "ES-2", "1808666480668498098", "[PERSON_NAME_0100]", 12208, 3052, "Aug. 1, 2024", "Nov. 1, 2024"),
    ("ENG-2452", "Calvin Price", "[EMAIL_0801]", "ES-3", "1847333347700620793", "Calvin Price", 8138, 4408, "Oct. 24, 2025", "Jan. 24, 2026"),
    ("ENG-2453", "Claire Morgan", "PERSON_2360_EMAIL", "ES-4", "1856960410709778333", "Claire Morgan", 7630, 4450, "Dec. 31, 2025", "March 31, 2026"),
    ("ENG-2454", "[PERSON_NAME_0612]", "PERSON_4194_EMAIL", "ES-5", "1847333395311994879", "[PERSON_NAME_0612]", 10173, 5298, "Oct. 24, 2025", "Jan. 24, 2026"),
    ("ENG-2455", "Victor [PERSON_NAME_2770] [PERSON_NAME_0086]", "victor.barnes@harmonygames.co", "ES-6", "1830952527208439510", "Victor [PERSON_NAME_2770] [PERSON_NAME_0086]", 30519, 12716, "April 16, 2025", "July 16, 2025"),
    ("ENG-2456", "Marcus Bennett", "marcus.bennett@harmonygames.co", "ES-7", "1856960351896429942", "Marcus Bennett", 22889, 12875, "Jan. 30, 2026", "April 30, 2026"),
    ("ENG-2457", "[PERSON_NAME_0068]", "PERSON_3140_EMAIL", "ES-12", "1856960504234892536", "[PERSON_NAME_0068]", 16277, 8477, "Jan. 30, 2026", "April 30, 2026"),
    ("ENG-2458", "Martin [PERSON_NAME_7250] Walsh", "PERSON_4363_EMAIL", "ES-13", "1856960563574318616", "Martin [PERSON_NAME_7250] Walsh", 3866, 2013, "Jan. 30, 2026", "April 30, 2026"),
    ("ENG-2459", "[PERSON_NAME_0051]", "PERSON_2684_EMAIL", "ES-14", "1856960478782792748", "[PERSON_NAME_0051]", 3866, 1530, "Nov. 21, 2025", "Feb. 21, 2026"),
    ("ENG-2460", "Brian Foster", "PERSON_4243_EMAIL", "ES-15", "1856960532806250145", "[PERSON_NAME_2769] [PERSON_NAME_0093]", 10173, 3391, "Dec. 31, 2025", "March 31, 2026"),
    ("ENG-2461", "[PERSON_NAME_2768] [PERSON_NAME_0011]", "cameron@harmonygames.co", "ES-16", "1847333318158821452", "[PERSON_NAME_2768] [PERSON_NAME_0011]", 35605, 10384, "Oct. 24, 2025", "Jan. 24, 2026"),
    ("ENG-2462", "[PERSON_NAME_0038]", "PERSON_2314_EMAIL", "ES-17", "1847333272519888206", "[PERSON_NAME_0038]", 127162, 34439, "Oct. 24, 2025", "Jan. 28, 2026"),
    ("ENG-2463", "[PERSON_NAME_0022] [PERSON_NAME_2767] [PERSON_NAME_2763]", "PERSON_1174_EMAIL", "ES-18", "1856960382677662910", "[PERSON_NAME_0022] [PERSON_NAME_2767] [PERSON_NAME_2763]", 15259, 5404, "Jan. 30, 2026", "April 30, 2026"),
]
TITLE = {r[0]: r[1] for r in STOCK} | {r[0]: r[1] for r in OPTION}
EMAIL = {r[0]: r[2] for r in STOCK} | {r[0]: r[2] for r in OPTION}
ES = {r[0]: r[3] for r in OPTION}
ES_STOCK = {r[0]: r[3] for r in STOCK if r[3]}
LAST = {r[0]: r[9] for r in OPTION}
LAST["ENG-2452"] = "Feb. 20, 2026"
LABEL = {"Already told": "Already told", "Covered": "Covered", "Date note": "Last day", "First note": "Closing",
         "Full note": "Closing and last day", "Nothing": "Nothing"}
ISSUES = [r[0] for r in STOCK] + [r[0] for r in OPTION]

# told evidence per issue, for reason comments
WHY = {
    "ENG-2438": "already told: Leonard's Feb 9 mail to Griffin's partner",
    "ENG-2439": "already told: Leonard's Feb 9 mail to Griffin's partner",
    "ENG-2440": "already told: Leonard's Feb 9 DM to the holder",
    "ENG-2444": "Covered: the note to [PERSON_NAME_52949] on ENG-2443 covers this family line",
    "ENG-2445": "Covered: the note to [PERSON_NAME_52949] on ENG-2443 covers this family line",
    "ENG-2446": "already told: Robert's Feb 12 mail to the holder, Leonard copied",
    "ENG-2447": "already told: Leonard's Feb 12 mail to the holder as Husnu Akin",
    "ENG-2451": "holds nothing: its last day, Nov. 1, 2024, has passed",
    "ENG-2454": "holds nothing: its last day, Jan. 24, 2026, has passed",
    "ENG-2455": "holds nothing: its last day, July 16, 2025, has passed",
    "ENG-2461": "holds nothing: its last day, Jan. 24, 2026, has passed",
    "ENG-2462": "holds nothing: its last day, Jan. 28, 2026, has passed",
}


def label(k):
    return LABEL[TRUTH[k]["Owed"]]


def holds_text(k):
    """What the line holds today, in the words the sheet and notes use."""
    t = TRUTH[k]
    bits = []
    if t["Shares held now"]:
        bits.append(f"{n(t['Shares held now'])} Series Seed shares")
    if k in ES_STOCK:
        bits.append(f"{n(t['Options now'])} vested options ({ES_STOCK[k]})")
    elif k in ES and t["Options now"]:
        bits.append(f"{n(t['Options now'])} vested options ({ES[k]})")
    return " and ".join(bits) or "nothing"


def dec31_lines():
    out = []
    for k in ISSUES:
        v = TRUTH[k]["Options at Dec 31"]
        if v:
            cid = ES_STOCK.get(k) or ES.get(k)
            out.append((int(cid.split("-")[1]), cid, TITLE[k], v))
    return [x[1:] for x in sorted(out)]


# internal consistency with the solver truth
S = TRUTH["SUMMARY"]
assert sum(TRUTH[k]["Shares held now"] for k in ISSUES) == S["Series Seed total"] == 3051879
assert sum(TRUTH[k]["Options now"] for k in ISSUES) == S["Options outstanding now"] == 164114
assert sum(v for _, _, v in dec31_lines()) == S["Options outstanding at Dec 31"] == 243757
assert S["Common"] + S["Series Seed total"] + S["Options outstanding at Dec 31"] == S["Issued plus options at Dec 31"] == 9295636
for r in OPTION:
    t = TRUTH[r[0]]
    assert t["Options now"] in (0, r[7]), r
assert len(dec31_lines()) == 16

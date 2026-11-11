#!/usr/bin/env python3
"""Revision rev3 (/create-hardening MODE B moves 1-6, /create-scenario --revise S5a): patch roster_final.json. Run after
finalize_roster.py; idempotent. Every change is one a hardening move requires:
  move 1  due date: working ads on Android US phone are due Fri Oct 10 (Frederick's reply in the fake-installs thread)
  move 2  three re-capture notes leave their tickets for Marcus's #zm-animations note; the export tickets stop naming them
  move 3  Marcus's cheer fastcouch test is turned down by Robert: Reuse becomes Halloween version, assigned to Marcus
  move 4  the working ad statics go to Julia Lawson (Martin's vacation post, Leonard's reply); store art stays with Martin
  move 5  squirrelfail landscape and mrfluffernot landscape left iOS UK tablet, so only Android US tablet remains: Skip
  move 6  end card 001 and its three cuts still show the old zombies on the packs: Halloween version becomes Refresh first
The report's proposed cut of ART-831's "Not on the live creatives sheet yet." was declined at S0r: the prior /injection and
/prompt rely on that sentence and it buys no difficulty (the ticket list's set difference finds the ticket anyway).
    python3 -B Task_Authoring/task_inputsN2/Working_Files/scenario_gen/apply_rev3.py
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
P = HERE / "roster_final.json"
doc = json.loads(P.read_text())
S = {r["key"]: r for r in doc["surfaces"]}

for key in ("couch alpha 50", "barrel marketing2 4:5", "balloons alpha 50 (1)"):        # move 2
    r = S[key]
    r["recapture_note"] = "slack_marcus_recapture"
    for f in ("comment_2", "comment_2_by", "comment_2_at"):
        r[f] = None
for key, old, new in (("barrel marketing2 1:1", "the Android #1896 re-capture of the 4:5", "Android #1896"),
                      ("couch alpha 50 4:5", "the Android #1935 re-capture of the 9:16", "Android #1935"),
                      ("balloons alpha 50 (1) 16:9", "the Android #1966 re-capture of the 9:16", "Android #1966")):
    S[key]["comment_1"] = S[key]["comment_1"].replace(old, new)

r = S["marcus portrait UA end card"]                                                     # S0r: keep the sentence
if "Not on the live creatives sheet yet." not in r["comment_2"]:
    r["comment_2"] += " Not on the live creatives sheet yet."

for key in ("cheer fastcouch 9:16", "cheer fastcouch 16:9"):                             # move 3
    r = S[key]
    r.update(call="Halloween version", status="to make", assign_to="Marcus Bennett", owner="Marcus Bennett",
             already_made_halloween=False,
             notes="Marcus's test sits on the July capture and Robert turned it down; dress it from the Sep 16 re-capture",
             route="with Frederick for the Oct 18-31 flight")

for key in ("squirrelfail landscape", "mrfluffernot landscape"):                         # move 5
    r = S[key]
    r.update(call="Skip October", status="none", assign_to=None, due=None,
             campaigns_now=["Android US tablet"], notes="left iOS UK tablet on Sep 29, so it runs only on Android US tablet, which ends Oct 12",
             route="no Halloween version (Android US tablet ends Oct 12)")

for key in ("end card 001", "end card 16:9 from 001", "end card 1:1 from 001", "end card 4:5 from 001"):   # move 6
    r = S[key]
    r.update(call="Refresh first", notes="still shows the old zombies on the packs: re-render before any seasonal pass")

for r in doc["surfaces"]:
    if r["kind"] == "static" and r["call"] != "Skip October":                            # move 4
        r["owner"], r["assign_to"] = "Julia Lawson", "Julia Lawson"
    if r.get("ticket") and r["call"] in ("Halloween version", "Refresh first"):          # move 1
        android = "Android US phone" in (r.get("campaigns") or [])
        r["due"] = "2025-10-10" if android else "2025-10-15"
        by = "Fri Oct 10 (Unity reviews new Android creatives by hand)" if android else "Wed Oct 15"
        r["route"] = f"with Frederick by {by} for the Oct 18-31 flight"

P.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
ads = [r for r in doc["surfaces"] if r.get("ticket")]
print("rev3 roster:", dict(Counter(r["call"] for r in ads)), "| assigned", dict(Counter(r["assign_to"] for r in ads if r["assign_to"])),
      "| due", dict(Counter(r["due"] for r in ads if r["due"])))

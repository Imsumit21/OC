#!/usr/bin/env python3
"""Write Working_Files/01c_Dispositions.json: a written disposition for every mutation result (rule, degrade,
intervention) and every injection-stage liveness flag. Liveness entries are read from
research/01_trap_liveness_dispositions.json (design-stage reasons, re-checked on the SQL) plus the injection-only ones
below. Re-run after the mutation or liveness output changes.

    python3 -B Task_Authoring/task_inputsN2/Working_Files/injection_gen/write_dispositions.py
"""
from __future__ import annotations

import json
from pathlib import Path

WF = Path(__file__).resolve().parents[1]

M = {
    "rule:R_BUILD_CUT": ("weak-accepted",
        "SURVIVED on the surface by design: the build cut decides due dates (icon Thu Oct 16 vs Leonard's 'around the 24th'; "
        "iPad and iPhone sets by the same cut), which the deterministic surface cannot grade (a due window needs a date "
        "comparison; reason_matches has no solver value). It flips the weight-5 rubric-only facts RO9 and RO8 and the "
        "weight-3 RO6 (scenario_gen/rubric_only_facts.json); the solver's due field moves for the icon, iPad and iPhone rows"),
    "rule:R_DONE_EXPORT": ("live", "KILLED: believing Martin's 'exported' post makes the iPad 12.9-inch set Reuse and flips S03; "
        "deciding record: the Store folder d_74a7c95c28097dd9777e01, whose listing holds iPhone 6.5 and Google Play files only"),
    "rule:R_TEST_TURNED_DOWN": ("live", "KILLED: missing Robert's review keeps both cheer fastcouch cuts as Reuse and flips S05 and S06; "
        "deciding record: his thread reply under Marcus's #zombie-art test post"),
    "rule:R_FLIGHT_CHANGE": ("live", "KILLED: reading the Sep 12 draft instead of the Sep 30 changes mail keeps the eight "
        "Android-US-tablet-only ads (no Skip) and moves every ad due date to Oct 17; flips S08 and S29 (and the rubric-only RO2, RO10)"),
    "rule:R_SCOPE_SERVING": ("live", "KILLED: taking the sheet's rows as the scope drops Julia's 4:5 static (named only in "
        "Frederick's Trello comment) and the portrait end card (its own ticket ART-831) and flips S10 and S11"),
    "rule:R_ART_CURRENT": ("live", "KILLED: dressing every serving cut as it is (no refresh-first rule from Robert's deck) "
        "flips the Refresh first rows that rest on the deck, eight of them graded (S09, S10, S11, S14, S15, S16, S21, S22)"),
    "rule:R_REVIEW_WINDOW": ("weak-accepted", "SURVIVED on the solver-read slots by design: the rule moves the due field of 30 working ads, and the surface "
        "reads that field from the written cell through reason_matches (S37, S38, S39), which the mutant's direct-slot pass does not evaluate; U counts them as "
        "flippable. Deciding record: his reply in the Sep 30 fake-installs thread. Also graded by the rubric-only RO2 and RO10"),
    "rule:R_RECAPTURE_NOTE": ("live", "KILLED: missing Marcus's #zm-animations note leaves the April captures in force and flips S17, S18 and S30"),
    "rule:R_STATICS_COVER": ("live", "KILLED: missing Martin's #company-internal post keeps the working statics on Martin and flips S31 and S32"),
    "rule:R_TABLET_TRIM": ("live", "KILLED: missing Frederick's restart mail keeps both landscape cuts on iOS UK tablet and flips S33 and S34"),
    "rule:R_OLD_PACKS": ("live", "KILLED: missing Frederick's card comment leaves end card 001 and its cuts as Halloween versions and flips S35 and S36"),
    "degrade:over:every-store-piece-due-oct16": ("weak-accepted",
        "control trial for R_BUILD_CUT: putting the Google Play set on the Oct 16 cut moves only its due date, which the "
        "surface does not grade; the rubric-only RO9 states the Play set has no fixed date"),
    "degrade:over:every-store-set-missing": ("live", "control trial for R_DONE_EXPORT: treating the iPhone and Google Play "
        "sets as missing flips S24 (the iPhone set is Reuse)"),
    "degrade:over:every-current-cut-reused": ("live", "control trial for R_TEST_TURNED_DOWN: reusing every current cut flips S28 "
        "(cheer fastcouch 4:5, outside Marcus's 'both 9:16 and 16:9'), S17 and S23"),
    "degrade:over:every-tablet-cut-skipped": ("live", "control trial for R_FLIGHT_CHANGE: skipping every tablet cut flips S09 "
        "(couch alpha 50 16:9 also runs on iOS UK tablet); balloons alpha 50 (1) 16:9 is the second control"),
    "degrade:over:archive-rows-serving": ("weak-accepted",
        "control trial for R_SCOPE_SERVING: giving the Archive tab's paused creatives a row moves only out-of-scope rows; "
        "the surface's exact-key delivery slot V01 grades extra rows from the writes, not from the solver"),
    "degrade:over:every-pre-august-post-refreshed": ("live", "control trial for R_ART_CURRENT: refreshing by the sheet's "
        "'live since' date flips S17 and S18 (couch alpha 50 and barrel marketing2 4:5 were re-captured in September)"),
    "degrade:over:every-ad-due-oct10": ("weak-accepted", "control trial for R_REVIEW_WINDOW: moving every ad to Oct 10 moves the due field of the iOS-only cuts; S39 reads it from the written cell, outside the direct-slot pass"),
    "degrade:over:every-april-cut-recaptured": ("live", "control trial for R_RECAPTURE_NOTE: treating every April capture as re-captured flips S21 (couch boss 30)"),
    "degrade:over:every-martin-piece-to-julia": ("weak-accepted", "control trial for R_STATICS_COVER: giving Julia the store art moves the owner of the icon and the iPad set; no slot reads a store owner, so it stays a control trial only"),
    "degrade:over:every-landscape-cut-skipped": ("weak-accepted", "control trial for R_TABLET_TRIM: skipping cuts still on iOS UK tablet moves boris alin2 16:9 and couch boss 30 16:9, which no slot reads, so it stays a control trial only"),
    "degrade:over:every-august-render-refreshed": ("live", "control trial for R_OLD_PACKS: refreshing every August capture flips S23 (marcus.bennett 4:5)"),
}
for r in ("R_BUILD_CUT", "R_DONE_EXPORT", "R_TEST_TURNED_DOWN", "R_FLIGHT_CHANGE", "R_SCOPE_SERVING", "R_ART_CURRENT",
          "R_REVIEW_WINDOW", "R_RECAPTURE_NOTE", "R_STATICS_COVER", "R_TABLET_TRIM", "R_OLD_PACKS"):
    M[f"intervention:rule:{r}"] = ("live", "load-bearing: removing the rule's injected deciding record from an in-memory "
                                   "copy of the SQL moves its own keys only (no escaped coupling)")
for op in ("every-store-piece-due-oct16", "every-store-set-missing", "every-current-cut-reused", "every-tablet-cut-skipped",
           "archive-rows-serving", "every-pre-august-post-refreshed", "every-ad-due-oct10", "every-april-cut-recaptured",
           "every-martin-piece-to-julia", "every-landscape-cut-skipped", "every-august-render-refreshed"):
    M[f"intervention:degrade:over:{op}"] = ("redundant", "no-injected-records: an over-application operator is a control "
                                            "trial with no deciding records of its own, so there is nothing to remove")


def main() -> None:
    out = {"mutation": {k: {"disposition": d, "reason": why} for k, (d, why) in M.items()}}
    live = json.loads((WF / "research" / "01_trap_liveness_dispositions.json").read_text())
    extra = WF / "injection_gen" / "liveness_injection.json"
    if extra.exists():
        live.update(json.loads(extra.read_text()))
    out["liveness"] = live
    (WF / "01c_Dispositions.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print("01c_Dispositions.json:", len(out["mutation"]), "mutation,", len(out["liveness"]), "liveness")


if __name__ == "__main__":
    main()

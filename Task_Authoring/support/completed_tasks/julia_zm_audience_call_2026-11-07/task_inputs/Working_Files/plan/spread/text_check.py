#!/usr/bin/env python3
"""Check the proposed K1, K5 and gate-Doc texts against the sweep avoid lists, the solver parse phrases,
the no-tester-name rule, and compute the K1 snippet and size the generator would emit. Read-only."""
import re, sys
from pathlib import Path

PLAN = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLAN))
import data as D  # noqa: E402

K1_SUBJECT_NEW = "quick catch-up"
K1_BODY_NEW = D.K1_BODY.replace(
    "How is the level work going? I keep missing you on Slack, last week was all items for me.\n\n"
    "Something has been on my mind about Friday at my place.",
    "Hope the level work is going well. I keep missing you on Slack, last week was all items for me and this "
    "week is starting the same way, so mail it is.\n\n"
    "One thing has been on my mind about Friday at my place.")
assert K1_BODY_NEW != D.K1_BODY, "K1 anchor text not found"

K5_TEXT_NEW = ("for repros like this one, and for anyone watching people play it: careful with android 1943, the one "
               "that’s been passed around. it never went through a store, so anyone on it isn’t seeing what a "
               "player gets")
GATE_OLD = "What a pass does and doesn't cover gets discussed on his Vision Bot PR."
GATE_NEW = "What a pass does and doesn't cover gets discussed in the review comments on his Vision Bot PR."
assert GATE_OLD in D.GATE_DOC
GATE_DOC_NEW = D.GATE_DOC.replace(GATE_OLD, GATE_NEW)

AVOID = {
    "K1": (K1_BODY_NEW + " " + K1_SUBJECT_NEW, ["playtest", "beta", "session", "form", "walked through", "helped", "coach",
                                               "explained", "hint", "doesn't count", "exclude", "duplicate"]),
    "K5": (K5_TEXT_NEW, ["dev build", "session", "sektör", "re-run"]),
    "GATE": (GATE_DOC_NEW, ["no session blocker", "sit in review", "for the branch the job ran on", " a iphone"]),
}
# Cross-record disjointness: words of F and K4 that must not appear in K5, and K5's key words absent from F.
CROSS = {"K5 vs F": (K5_TEXT_NEW, ["device", "build", "technical", "dropped", "re-run", "observer"]),
         "K5 vs K4": (K5_TEXT_NEW, ["kadıköy", "oyun", "ekib"]),
         "K1 vs F/K5": (K1_BODY_NEW + " " + K1_SUBJECT_NEW, ["1943", "store", "re-run", "device", "build"])}
names = ["Oliver", "Owen", "Samuel", "Calvin", "Marcus", "Martin", "Douglas", "Vincent", "Brian", "Robert"]
ok = True
for k, (t, words) in {**AVOID, **CROSS}.items():
    for w in words:
        if w in t.lower():
            ok = False
            print(f"FAIL {k}: carries {w!r}")
for k, t in (("K1", K1_BODY_NEW), ("K5", K5_TEXT_NEW)):
    for n in names:
        if n.lower() in t.lower():
            ok = False
            print(f"FAIL {k} names {n}")
# Solver parse phrases (solver/solver.py _k1_scope, _k5_builds)
b = " ".join(K1_BODY_NEW.split()).lower()
for p in ("before anyone touched their phone", "friday at my place"):
    if p not in b:
        ok = False
        print("FAIL K1 solver phrase missing:", p)
if "never went through a store" not in K5_TEXT_NEW or re.findall(r"android (\d{4})", K5_TEXT_NEW) != ["1943"]:
    ok = False
    print("FAIL K5 solver parse")
if "anything that never went through a store" not in GATE_DOC_NEW:
    ok = False
    print("FAIL gate store clause")
crlf = K1_BODY_NEW.replace("\n", "\r\n")
snip_old = " ".join(D.K1_BODY.replace("\n", "\r\n").split())[:140]
snip_new = " ".join(crlf.split())[:140]
print("K1 snippet old:", snip_old)
print("K1 snippet new:", snip_new)
print("K1 'fri' in new snippet:", "fri" in snip_new.lower())
print("K1 size old/new:", len(D.K1_BODY.replace("\n", "\r\n").encode()), len(crlf.encode()))
print("K1 friday offset old/new (chars into normalised body):",
      " ".join(D.K1_BODY.split()).find("Friday"), " ".join(K1_BODY_NEW.split()).find("Friday"))
print("RESULT", "PASS" if ok else "FAIL")

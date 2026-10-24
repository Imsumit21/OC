#!/usr/bin/env python3
"""sample_task_02 (iteration 6): plan the change-list layer = Arthur's release-audit notes on Linear.

Deterministic (fixed seed). Input (cached base extract made with tools/hg.py):
  done_since_may1.json - ENG/ZOM issues in state Done, completed on/after 2025-05-01 (599; 504 not archived)
Leonard's Feb 11 ask covers tickets closed since May 1; Arthur works from the default Linear views, so archived
tickets get no note. Sunset's change list = Done, completed on/after June 1, 2025, not archived (424 tickets).
Output: changes_plan.json (one audit note per audited ticket) for gen_sql.py, ground_truth.py, build_manifest.py.
No PR comments are planned here: PR comments in the lot repos are mirrored into Slack (not per-record volume).
"""
import collections
import datetime as dt
import hashlib
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALL = json.loads((HERE / "done_since_may1.json").read_text())
DONE = [d for d in ALL if not d["is_archived"]]          # what Arthur's audit covers
WINDOW = "2025-06-01"

# Store updates (date the update went live, both platforms). Grounded where the base speaks:
#  DD: short versions in Arthur's Crashlytics digests (0.2.144 May 4 ... 0.2.152 May 18, 0.2.161 Jun 3, 0.2.162 Jun 7,
#      0.2.164 Jun 9, 0.2.170/0.2.248 Jun 19-20, 0.2.249 Jun 24, 0.2.171/0.2.253 Jul 31-Aug 1, 0.2.172 Aug 7,
#      0.2.179/0.2.259 Oct 23-25, 0.2.180/0.2.260 Nov 1-3, 0.3.196 Dec 12, 0.3.205/0.3.267 Dec 27); 0.3.309 Feb 9 (Leonard, ENG-2438).
#  ZM: 0.1.500 May 22; "ZM builds submitted" Jun 5; Jun 17 submission approved; Jul 11 hot fix; 0.3.3 Jul 24; 0.3.7/0.3.87 Jul 30;
#      Aug 1 public build; 0.3.99 Aug 7; 0.3.22 Aug 15; 0.3.24 live by Aug 28; 0.3.28 live by Sep 3; Sep 11 submission;
#      0.3.139 Oct 5; 0.3.154 Oct 23; 0.3.157 Nov 6.
ZM = ["2025-05-22", "2025-06-06", "2025-06-18", "2025-07-11", "2025-07-24", "2025-07-30", "2025-08-01", "2025-08-07",
      "2025-08-15", "2025-08-27", "2025-09-02", "2025-09-12", "2025-10-05", "2025-10-23", "2025-11-06"]
DD = ["2025-05-04", "2025-05-08", "2025-05-15", "2025-05-18", "2025-06-03", "2025-06-07", "2025-06-09", "2025-06-19",
      "2025-06-24", "2025-07-31", "2025-08-07", "2025-10-23", "2025-11-03", "2025-12-12", "2025-12-27", "2026-02-09"]
# decisive picks whose base Slack context could read as contradicting a rollback / hold (re-drawn)
AVOID = {"ZOM-563", "ZOM-530"}


def md(d):
    t = dt.date.fromisoformat(d)
    return t.strftime("%b ") + str(t.day)


def cal(key):
    return ZM if key.startswith("ZOM") else DD


rng = random.Random(20261004)
cohort = [d for d in DONE if d["completed_at"] >= WINDOW]
outside = [d for d in DONE if d["completed_at"] < WINDOW]


def first_update(d, skip):
    later = [u for u in cal(d["id"]) if u > d["completed_at"][:10]]
    if not later:
        return None, None
    if skip and len(later) > 1:
        return later[1], later[0]
    return later[0], None


def pick(pool, n):
    pool = [d for d in pool if d["id"] not in AVOID]
    rng.shuffle(pool)
    return pool[:n]


plan = {}
for members, nrb, nnr, nnm in [([d for d in cohort if d["id"].startswith("ZOM")], 48, 26, 20),
                               ([d for d in cohort if d["id"].startswith("ENG")], 4, 2, 2),
                               (outside, 8, 4, 4)]:
    shippable = [d for d in members if first_update(d, False)[0]]
    rb = pick(shippable, nrb)
    rest = [d for d in shippable if d not in rb]
    nr = pick(rest, nnr)
    rest = [d for d in rest if d not in nr]
    nm = pick([d for d in rest if [u for u in cal(d["id"]) if u > first_update(d, False)[0]]], nnm)
    for d in members:
        k = d["id"]
        if not first_update(d, False)[0]:
            plan[k] = {"kind": "late"}
        elif d in rb:
            plan[k] = {"kind": "rolled_back"}
        elif d in nr:
            plan[k] = {"kind": "held"}
        elif d in nm:
            plan[k] = {"kind": "off_on"}
        else:
            plan[k] = {"kind": "plain", "skip": rng.random() < 0.12}

REASONS = ["crash spike on low-end android", "retention dipped in the first sessions", "it broke the event rewards",
           "memory warnings on older iphones", "players said it made the levels too hard", "store review complaints",
           "it doubled the ad frequency by mistake", "server load during the event"]


def add_days(d, n):
    return (dt.date.fromisoformat(d) + dt.timedelta(days=n)).isoformat()


def note_for(d, p):
    k, kind = d["id"], p["kind"]
    c = cal(k)
    if kind == "late":
        game = "ZM" if k.startswith("ZOM") else "DD"
        return {"status": "NOT RELEASED", "store_update": None,
                "text": f"audit: finished after the last {game} store update ({md(c[-1])}), never went out"}
    first, missed = first_update(d, p.get("skip", False))
    if kind == "plain":
        opts = [f"release audit: went out in the {md(first)} store update",
                f"audit: shipped with the {md(first)} store update",
                f"audit: {md(first)} store update",
                f"audit: in the {md(first)} update, ios and android same day",
                f"audit: shipped in the {md(first)} store update, nothing changed after",
                f"audit: {md(first)} store update. checked it is still in the current build"]
        if missed:
            opts = [f"audit: missed the {md(missed)} cut, went out with the {md(first)} store update",
                    f"audit: not in {md(missed)} (cut was the day before), shipped {md(first)}"]
        return {"status": "RELEASED", "store_update": first, "text": rng.choice(opts)}
    later = [u for u in c if u > first]
    if kind == "held":
        return {"status": "NOT RELEASED", "store_update": None,
                "text": rng.choice(["audit: merged but it sat behind the feature flag, the flag was never on in a store build",
                                    "audit: only ever went to the internal test track, never in a store update",
                                    f"audit: held back from the {md(first)} update for the event and never shipped after",
                                    "audit: built and merged, but we kept it out of every store build (waiting on art that never came)"])}
    if kind == "rolled_back":
        reason = rng.choice(REASONS)
        if later and rng.random() < 0.5:
            nxt = later[0]
            return {"status": "ROLLED BACK", "store_update": first,
                    "text": rng.choice([f"audit: shipped {md(first)}. backed out of main afterwards ({reason}), so the {md(nxt)} update and everything after went out without it",
                                        f"audit: {md(first)} store update, taken out again in the {md(nxt)} update ({reason})"])}
        off = add_days(first, rng.randint(3, 11))
        return {"status": "ROLLED BACK", "store_update": first,
                "text": rng.choice([f"audit: went out in the {md(first)} store update, then turned off with the remote config kill switch on {md(off)} ({reason}). never turned back on",
                                    f"audit: {md(first)} store update. kill switch flipped on {md(off)} after {reason}, still off"])}
    if kind == "off_on":
        nxt = later[0]
        off = add_days(first, rng.randint(2, 6))
        if off >= nxt:
            off = add_days(first, 1)
        return {"status": "RELEASED", "store_update": first,
                "text": rng.choice([f"audit: went out in the {md(first)} store update. turned off with the kill switch on {md(off)} while we looked at {rng.choice(REASONS)}, back on in the {md(nxt)} update",
                                    f"audit: shipped {md(first)}. left out of the {md(nxt)} build by mistake and put back the same week, so it never actually went away for players",
                                    f"audit: {md(first)} store update. kill switch on {md(off)} for a day during the event, turned back on {md(add_days(off, 1))}"])}
    raise ValueError(kind)


notes = {}
for d in DONE:
    notes[d["id"]] = note_for(d, plan[d["id"]]) | {"kind": plan[d["id"]]["kind"], "cohort": d["completed_at"] >= WINDOW}
# held tickets whose commits appear in Jenkins #builds change lists (ZOM-289 even in a Match3D Android Submission build):
# the code shipped, the feature did not - only the feature-flag wording is consistent with that
FLAG_TEXT = "audit: merged but it sat behind the feature flag, the flag was never on in a store build"
for k in ("ZOM-289", "ZOM-372"):
    assert notes[k]["kind"] == "held"
    notes[k]["text"] = FLAG_TEXT

# audit timing: Feb 11 16:40Z -> 23:55Z, then Feb 12 13:20Z onward; ZOM first then ENG, oldest completion first
order = sorted(DONE, key=lambda d: (0 if d["id"].startswith("ZOM") else 1, d["completed_at"], d["id"]))
t = dt.datetime(2026, 2, 11, 16, 40, 12, tzinfo=dt.timezone.utc)
s1_end = dt.datetime(2026, 2, 11, 23, 55, 0, tzinfo=dt.timezone.utc)
for d in order:
    if s1_end < t < dt.datetime(2026, 2, 12, 13, 20, tzinfo=dt.timezone.utc):
        t = dt.datetime(2026, 2, 12, 13, 20, 31, tzinfo=dt.timezone.utc)
    notes[d["id"]]["at"] = t.strftime("%Y-%m-%dT%H:%M:%SZ")
    notes[d["id"]]["comment_id"] = "cmt_" + hashlib.sha256(f"{d['id']}|audit|0".encode()).hexdigest()[:20]
    t += dt.timedelta(seconds=rng.randint(55, 125))

out = {"window": WINDOW, "audit_scope": "2025-05-01", "zm_updates": ZM, "dd_updates": DD, "notes": notes, "pr_comments": []}
(HERE / "changes_plan.json").write_text(json.dumps(out, indent=1))
coh = [k for k, v in notes.items() if v["cohort"]]
print("audited", len(notes), "cohort", len(coh), collections.Counter(notes[k]["status"] for k in coh),
      collections.Counter(notes[k]["kind"] for k in coh))
print("outside", len(notes) - len(coh), collections.Counter(v["status"] for v in notes.values() if not v["cohort"]))
print("audit span", min(v["at"] for v in notes.values()), max(v["at"] for v in notes.values()))

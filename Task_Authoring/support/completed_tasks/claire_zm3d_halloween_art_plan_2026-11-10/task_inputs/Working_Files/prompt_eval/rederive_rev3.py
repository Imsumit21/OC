#!/usr/bin/env python3
"""Independent re-derivation of the rev3 answer from the records, for the prompt check. It never imports the solver or
reads solver/truth.json until the end, when the two are compared. Reads 01_Universe_Inject.sql as text (never executes it).
The rules below are written from the deck, the mails, the thread replies and the ticket comments as Claire would read them.

    python3 -B Task_Authoring/task_inputsN2/Working_Files/prompt_eval/rederive_rev3.py
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
sys.path.insert(0, str(TASK.parents[1] / "Task_Authoring" / "tools"))
from base_check import parse_sql  # noqa: E402

rows = [r for r in parse_sql((TASK / "01_Universe_Inject.sql").read_text()) if r["op"] == "insert"]
issues = {r["row"]["identifier"]: r["row"] for r in rows if r["table"] == "linear.linear_issues"}
comments = {}
for r in rows:
    if r["table"] == "linear.linear_comments":
        comments.setdefault(r["row"]["issue_id"], []).append(r["row"])
for v in comments.values():
    v.sort(key=lambda c: c["created_at"])
slack = {f'{r["row"]["channel_id"]}/{r["row"]["ts"]}': r["row"]["text"] for r in rows if r["table"] == "slack.slack_messages"}
sheets = {r["row"]["title"]: json.loads(r["row"]["grid_json"]) for r in rows if r["table"] == "gsheets.sheets_sheets"}
mails = [r["row"] for r in rows if r["table"] == "gmail.gmail_messages" and r["row"].get("user_email") == "claire.morgan@harmonygames.co"]
trello = [json.loads(r["row"]["data_json"]).get("text", "") for r in rows if r["table"] == "trello.trello_actions"]

# scope: the sheet's Unity tab, minus nothing; plus the two off-sheet serving tickets
scope = {row[0]: row[3] for row in sheets["Unity"][1:]}
assert not set(scope) & {row[0] for row in sheets["Archive"][1:]}
assert any("Julia's 4:5 static" in t and "count it in" in t for t in trello)                       # adds ART-826
assert any("Not on the live creatives sheet yet." in c["body"] for c in comments["ART-831"])       # adds ART-831
for tid, key in (("ART-826", "julia 4:5"), ("ART-831", "marcus portrait UA end card")):
    scope.setdefault(key, tid)

note = next(t for t in slack.values() if t.startswith("re-recorded 3 of the old ua cuts"))
recaptured = dict((k.strip(), int(n)) for k, n in re.findall(r"([a-z0-9 :().]+?) on (?:android )?#(\d+)", note.split("no music: ")[1].replace(", ", ",").replace(",", " ,")))
recaptured = {k.lstrip(", "): v for k, v in recaptured.items()}
restart_body = next(m for m in mails if m["subject"] == "Unity retention restart")
restart_text = " ".join(str(v) for v in restart_body.values() if isinstance(v, str))
left_off = re.search(r"I left (.+?) off iOS UK tablet", restart_text).group(1).split(" and ")
packs = next(t for t in trello if t.startswith("end card 001 still has the old zombies"))
assert all(x in packs for x in ("16:9", "1:1", "4:5"))
old_packs = {"end card 001", "end card 16:9 from 001", "end card 1:1 from 001", "end card 4:5 from 001"}
baked_thread = {"marcus.bennett 9:16"}        # ART-809 points at Frederick's Aug 13 thread: 'the background music is baked in'
SWAP_BUILD, SWAP_DATE = 1452, (7, 29)
MONTHS = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}


def campaigns(key, tid):
    last = []
    for c in comments[tid]:
        m = re.search(r"Unity(?: Sep \d+)?: ([^.(]+)", c["body"]) or re.search(r"Still running on Unity: ([^(]+)", c["body"])
        if m:
            last = [x.strip() for x in m.group(1).split(",")]
    if key in left_off:
        last = [x for x in last if x != "iOS UK tablet"]
    return last


def newest_build(key, tid):
    """(build number or None, capture date (m, d) or None): the newest capture on record, the ticket's or Marcus's note."""
    build, date = None, None
    for c in comments[tid]:
        b = re.search(r"Android #(\d+)", c["body"])
        if b:
            build = max(build or 0, int(b.group(1)))
        d = re.search(r"(?:Captured|footage \(|captures \()(?: from Android #\d+ on )?\s*([A-Z][a-z]{2}) (\d+)", c["body"])
        if d:
            date = (MONTHS[d.group(1)], int(d.group(2)))
        if "before the first Match3D build" in c["body"]:
            date = (1, 1)
    if key in recaptured:
        build = max(build or 0, recaptured[key])
    return build, date


derived = {}
for key, tid in scope.items():
    camp = campaigns(key, tid)
    build, date = newest_build(key, tid)
    body = " ".join(c["body"] for c in comments[tid])
    pre_swap = (build is not None and build < SWAP_BUILD) or (build is None and date is not None and date < SWAP_DATE)
    music = "music baked into the master" in body and key not in recaptured
    music = music or key in baked_thread
    if camp == ["Android US tablet"]:
        call = "SKIP"
    elif pre_swap or music or key in old_packs:
        call = "REFRESH FIRST"
    else:
        call = "HALLOWEEN VERSION"
    owner = due = None
    if call != "SKIP":
        owner = "Julia Lawson" if "static)" in issues[tid]["title"] else "Marcus Bennett"
        due = "Fri Oct 10" if "Android US phone" in camp else "Wed Oct 15"
    derived[key] = dict(call=call, owner=owner, due=due)

truth = json.loads((WF / "solver" / "truth.json").read_text())
ads = {k: v for k, v in truth.items() if k in derived}
diff = [(k, f, derived[k][f], ads[k][f]) for k in sorted(ads) for f in ("call", "owner", "due") if derived[k][f] != ads[k][f]]
print("derived ads:", len(derived), "| calls", dict(Counter(v["call"] for v in derived.values())),
      "| owners", dict(Counter(v["owner"] for v in derived.values() if v["owner"])),
      "| due", dict(Counter(v["due"] for v in derived.values() if v["due"])))
print("missing from truth:", sorted(set(derived) - set(truth)), "| truth rows not derived:",
      sorted(k for k, v in truth.items() if k not in derived and v["call"] and "calls" in v.get("groups", []) and k not in
             ("app icon", 'iPad 12.9" set', 'iPhone 6.5" set', "Google Play phone set")))
print("re-captures read from Marcus's note:", recaptured, "| left off iOS UK tablet:", left_off)
print("field differences from solver/truth.json:", len(diff))
for d in diff:
    print("  ", d)
print("VERDICT:", "MATCH" if not diff and len(derived) == 58 else "DIFFERS")

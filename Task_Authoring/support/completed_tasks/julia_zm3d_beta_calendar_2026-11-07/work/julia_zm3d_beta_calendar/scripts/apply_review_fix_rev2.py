#!/usr/bin/env python3
"""Targeted post-/prompt-review edits (v2: item-naming records only, GEN_EXECUTION §3 Review repair) to 01_Universe_Inject.sql (task_inputsS).
Usage: apply_sql_fix.py <in.sql> <out.sql>   (pure text transform; asserts every anchor count)"""
import hashlib, json, re, sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()

def rep(old, new, count):
    global s
    n = s.count(old)
    assert n == count, f"expected {count} of {old[:70]!r}, found {n}"
    s = s.replace(old, new)

# ---- 1. Frederick's ask gets one thread reply (settles the push-plan scope and Zombie Lane) ----
CH, ROOT_TS, ROOT_ID = "D05SD5QLG94", "1759263600.418207", "8b090dec472117f4598b9ad84318272e"
REPLY_TS = "1759263878.305127"                     # 2025-09-30T20:24:38Z, 4 min 38 s after the ask
REPLY_ID = hashlib.sha256(f"{CH}|{REPLY_TS}".encode()).hexdigest()[:32]
assert hashlib.sha256(f"{CH}|{ROOT_TS}".encode()).hexdigest()[:32] == ROOT_ID
REPLY_TEXT = ("Two things the brief does not spell out. Pushes: plan the PNs Beta tab as it stands, one line per row, "
              "local notifications included. Leave off the four rows for things that are not in the beta: Hourly Coins, "
              "Nathan''s Treasure Hunt, Streak Fever and Axe Arena, just those four. Copy that does not name the game at "
              "all is fine to go out, the naming rule is only about wrong names. And keep Zombie Lane off the calendar, "
              "it is a permanent track with no window or reset to plan.")
root_tail_old = "NULL, '1759263600.418207', 0, 0, NULL, false, NULL, '[]', '[]', '[]', '2025-09-30T20:20:00.418207Z', '{}');"
root_tail_new = (f"NULL, '1759263600.418207', 1, 1, '{REPLY_TS}', false, NULL, '[]', '[]', '[]', '2025-09-30T20:20:00.418207Z', '{{}}');\n\n"
    "INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, "
    "reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) "
    f"VALUES ('{REPLY_ID}', '{REPLY_TS}', '{CH}', 'message', 'EMPLOYEE_0008_SLACK_ID', '{REPLY_TEXT}', '{ROOT_ID}', '{ROOT_TS}', "
    "0, 0, NULL, false, NULL, '[]', '[]', '[]', '2025-09-30T20:24:38.305127Z', '{}');")
rep(root_tail_old, root_tail_new, 1)

# ---- 2. Release event: only the windows still on DEV ride this release (4 calendar copies) ----
rep("Prod backend deploy for the beta. The live-ops server windows go live with this release; release window 18:00-19:00 Istanbul time.",
    "Prod backend deploy for the beta. The server windows that are still on the DEV stack go live with this release; release window 18:00-19:00 Istanbul time.", 4)

# ---- 3. Arthur's #470 inline note (+ its #zombie-prs mirror): the other schedules are already on prod ----
rep("Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next backend release. The client side in this PR is fine as it is.",
    "Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next backend release. The Plague Race, leagues, Endless and Season Pass schedules are already running on prod. The client side in this PR is fine as it is.", 2)

# ---- 4. Samuel's #471 note (+ mirror): the frame is in both Sep 30 submission builds ----
rep("The daily-gift frame went out with this PR — it is in submission 135, so that one can be closed.",
    "The daily-gift frame went out with this PR — it is in both submission builds from today, iOS 50 and Android 135, so nothing is left on it and that one can be closed.", 2)

# ---- 5. Brian's mails: no season numbering in the base, so 'the November season' ----
rep("Season 2 opens on Sat Nov 1. The config handoff we agreed with Product is for Wed Oct 29",
    "The November season opens on Sat Nov 1. The config handoff we agreed with Product is for Wed Oct 29", 3)
rep("Season 2 still opens on Sat Nov 1.", "The November season still opens on Sat Nov 1.", 3)
def snippet(body, n):
    return re.sub(r"\s+", " ", body).strip()[:n]
BODY1 = ("Julia, Handing over the November Season Pass config, Frederick in copy so we all have it in one place. "
         "The November season opens on Sat Nov 1. The config handoff we agreed with Product is for Wed Oct 29, so that is the date I am committing to")
assert BODY1.replace("Julia, ", "Julia,\n\n", 1).split("Product is")[0].split("\n\n")[1][:20] in s
rep("Julia, Handing over the November Season Pass config, Frederick in copy so we all have it in one place. Season 2 opens on Sat Nov 1. The config handoff we agreed with Product i",
    snippet(BODY1, 175), 6)

assert "Season 2" not in s

# ---- 6. Frederick's brief: three clause edits, then recompute the heading runs ----
i = s.index("'ZM3D beta live-ops calendar - working rules\nFrederick, Sep 24")
j = s.index("', '[{\"start\":0", i)
k = s.index("]', '4c1a7e9b02'", j)
body = s[i + 1:j]
assert "''" not in body
def brep(old, new):
    global body
    assert body.count(old) == 1, old
    body = body.replace(old, new)
brep("For quest and login-calendar rollovers put down whether the beat is in and whether its push is ready, not its window dates.",
     "For the quest rollover and the daily gift (the Login Calendar row on the push sheet) put down whether the beat is in and whether its push is ready, not its window dates.")
brep("so a window the release instant pre-empts does not count.",
     "so a window the release instant pre-empts does not count. A beat that is only waiting on that release starts late, it is not held.")
HEADS = ["Span and time base", "Scope", "When a beat starts", "Held or not", "One-offs", "Still to do", "Push copy", "Config locks"]
title = body.split("\n", 1)[0]
runs = [{"start": 0, "end": len(title), "named_style": "TITLE", "list_id": None, "list_nesting": 0}]
for h in HEADS:
    assert body.count("\n" + h + "\n") == 1, h
    a = body.index("\n" + h + "\n") + 1
    runs.append({"start": a, "end": a + len(h), "named_style": "HEADING_2", "list_id": None, "list_nesting": 0})
for r in runs:                                   # every run covers exactly one whole line
    assert (r["start"] == 0 or body[r["start"] - 1] == "\n") and body[r["end"]] == "\n"
s = s[:i + 1] + body + "', '" + json.dumps(runs, separators=(",", ":")) + s[k + 1:]

# ---- 7. Two Linear comments that ran ahead of the base record ----
rep("The endless start screen vfx went in with build #2023 (commit f7e971b0). Claim button glow and the new bar are both live now, can close.",
    "The endless start screen vfx is in (commit f7e971b0). Claim button glow and the new bar are both live now, can close.", 1)
rep("'2025-09-29T18:20:00Z', '2025-09-29T18:20:00Z', 1);", "'2025-09-30T16:20:00Z', '2025-09-30T16:20:00Z', 1);", 1)
rep("UPDATE linear.linear_issues SET updated_at = '2025-09-29T18:20:00Z' WHERE id = 'ZOM-543';",
    "UPDATE linear.linear_issues SET updated_at = '2025-09-30T16:20:00Z' WHERE id = 'ZOM-543';", 1)
assert "cmt_zom543_1" in s and "#2023" not in s

open(dst, "w", encoding="utf-8").write(s)
print("reply id", REPLY_ID, "| brief chars", len(body), "| runs", [(r["start"], r["end"]) for r in runs])
print("statements", len(re.findall(r"^(?:INSERT|UPDATE) ", s, re.M)) + s.count(";INSERT INTO"))

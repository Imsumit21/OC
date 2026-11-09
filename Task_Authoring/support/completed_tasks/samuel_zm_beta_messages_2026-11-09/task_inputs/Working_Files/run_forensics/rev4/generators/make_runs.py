#!/usr/bin/env python3
"""Spot-decode: write one realistic correct run and two weaker ones through the real tool shapes, for tools/surface_grader.py.
Synthetic trajectories for checking the surface only; never platform evidence."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PLAN = os.path.dirname(HERE)
WF = os.path.dirname(PLAN)
P = json.load(open(os.path.join(PLAN, "ids.json")))
T = json.load(open(os.path.join(WF, "solver", "truth.json")))
T = T.get("rows", T)
TK = P["tickets"]
FOLDER, CARD, DM = P["base"]["folder"], P["base"]["pn_card"], P["ids"]["hub"].split("/")[0]
ROWS = {k: v for k, v in T.items() if v.get("Call")}
ASKS = {"brian.foster@harmonygames.co": ["Endless entries back", "Endless weekly result", "Season Pass premium nudge", "Comeback gift", "Boss Arena attempts refilled"],
        "calvin.price@harmonygames.co": ["Win & Collect start", "Daily chest ready"], "julia.lawson@harmonygames.co": ["Plague Race last hour", "Plague Race result", "New levels added", "Daily gift about to reset"],
        "martin.walsh@harmonygames.co": ["Free shop coins ready"], "oliver.brooks@harmonygames.co": ["Season Pass last 48 hours"],
        "owen.baker@harmonygames.co": ["Zombie Lane reward ready", "Achievement reward waiting", "Support reply waiting"], "robert@harmonygames.co": ["Boss Arena open", "Boss Arena last hours", "Lapsed 14 days", "Rewarded ad ready"]}
HEAD = ["Message", "Ticket", "Call", "What's missing", "Audience", "Final headline", "String change"]
MISS = {"Weekly Leaderboard reset": "Fires on the wrong day: it counts seven days from the last leave, so it isn't tied to the rollover", "Finish first mission": "Cannot reach its players: our own ask is after level 20",
        "Plague Race": "Not seen on both platforms: the iPhone pass was a test build, the store build never came through on iOS", "Lapsed 14 days": "Covered by Lapsed 7 days, the weekly batch repeats"}


def plan(overrides=None, drop_keys=()):
    out = [HEAD]
    for k, v in ROWS.items():
        if k in drop_keys:
            continue
        r = dict(v)
        r.update((overrides or {}).get(k, {}))
        miss = r.get("What's missing") if (overrides or {}).get(k) else MISS.get(k, v.get("What's missing") or "")
        out.append([k, r.get("Ticket") or "DES-347", r["Call"], miss or "", r["Audience"], r.get("Final headline") or "", r.get("String change") or ""])
    return out


def run(path, rows, comment_extra, hold_state="Backlog", asks_found=True, move_done=True):
    ev = [{"type": "system", "subtype": "init", "model": "claude-opus-5-5", "claude_code_version": "synthetic", "tools": [], "mcp_servers": []}]
    n = [0]

    def call(name, inp, res):
        n[0] += 1
        ev.append({"type": "assistant", "message": {"model": "claude-opus-5-5", "content": [{"type": "tool_use", "id": f"t{n[0]}", "name": "mcp__hg__" + name, "input": inp}]}})
        ev.append({"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": f"t{n[0]}", "content": json.dumps({"result": json.dumps(res)})}]}})
    call("gsheets_create_spreadsheet", {"title": "Beta player messages plan", "initialSheetTitle": "Plan"}, {"spreadsheetId": "plan1"})
    call("gsheets_values_update", {"spreadsheetId": "plan1", "range": "Plan!A1", "valueInputOption": "RAW", "values": rows}, {"updatedRows": len(rows)})
    call("gdrive_move_file", {"fileId": "plan1", "newParentId": FOLDER}, {"id": "plan1"})
    note = ("Beta retention note. Sep 15 cohort week: iOS D1 31.65%, D7 9.28%; Android D1 37.86%, D7 10.68%. Who hears from us once they stop: players past our own ask. "
            "Anyone who stops before level 20 hears nothing unless they switched messages on from settings. Lapsed reminders go out on days 1, 7, 14, 21 and 28.")
    call("gdocs_create_document", {"title": "Beta player messages note", "content": note}, {"documentId": "note1"})
    call("gdrive_move_file", {"fileId": "note1", "newParentId": FOLDER}, {"id": "note1"})
    for k, v in ROWS.items():
        t = TK.get(k)
        if not t:
            continue
        r = next((x for x in rows[1:] if x[0] == k), None)
        if not r:
            continue
        call("linear_create_comment", {"issueId": t, "body": f"Call: {r[2]}. {r[3]}" + comment_extra}, {"id": "c"})
        if r[2] == "Drop":
            call("linear_update_issue", {"id": t, "state": "Canceled"}, {"id": t})
        elif r[2] == "Hold":
            call("linear_update_issue", {"id": t, "state": hold_state, "assignee": None}, {"id": t})
    if not asks_found:
        call("linear_create_issue", {"team": "Design", "title": "PN: Win & Collect start", "description": "Row 7 had no ticket."}, {"id": "DES-347"})
    if asks_found:
        call("linear_create_issue", {"team": "Design", "title": "PN ask: Boss Arena attempts refilled", "description": "Hold: not scheduled in the client.", "state": "Backlog"}, {"id": "DES-347"})
        call("linear_create_issue", {"team": "Design", "title": "PN ask: Daily gift about to reset", "description": "Hold: not scheduled in the client.", "state": "Backlog"}, {"id": "DES-348"})
    if next((x for x in rows[1:] if x[0] == "Lapsed 7 days"), [0] * 7)[6] == "Yes":
        call("linear_create_issue", {"team": "Design", "parentId": P["parent"], "title": "String change: Lapsed 7 days", "description": "Change the headline to " + P["new_line"]}, {"id": "DES-349"})
    call("trello_create_checklist", {"idCard": CARD, "name": "Beta Go messages"}, {"id": "cl1"})
    for r in rows[1:]:
        if r[2] == "Go":
            call("trello_create_check_item", {"checklistId": "cl1", "name": r[0]}, {"id": "ci"})
    for to, ks in ASKS.items():
        call("gmail_send_message", {"user_email": "me", "to": [to], "subject": "What happened to your phone message asks", "body": "\n".join(f"{k}: {ROWS[k]['Call']}" for k in ks)}, {"id": "m"})
    c = {x: sum(1 for r in rows[1:] if r[2] == x) for x in ("Go", "Hold", "Drop")}
    call("slack_send_message", {"channel_id": DM, "message": f"Done. Go {c['Go']}, Hold {c['Hold']}, Drop {c['Drop']}."}, {"ok": True})
    ev.append({"type": "result", "subtype": "success", "is_error": False, "stop_reason": "end_turn"})
    json.dump(ev, open(path, "w"))


G = os.path.join(HERE, "runs")
os.makedirs(G, exist_ok=True)
run(os.path.join(G, "golden.json"), plan(), "")
nat = {"Weekly Leaderboard reset": {"Call": "Go", "What's missing": "", "Final headline": "Weekly Rankings Reset!", "String change": "No"},
       "Plague Race": {"Call": "Go", "What's missing": "", "Final headline": "Plague Race Is On!", "String change": "No"},
       "Finish first mission": {"Call": "Go", "What's missing": "", "Final headline": "Finish Your First Mission!", "String change": "No"},
       "Lapsed 14 days": {"Call": "Hold", "What's missing": "not scheduled in the client"},
       "Lapsed 7 days": {"Final headline": "They've Taken Over... Can You Stop Them?", "String change": "No"}}
run(os.path.join(G, "natural_reading.json"), plan(nat, ("Boss Arena attempts refilled", "Daily gift about to reset")), "", hold_state="Todo", asks_found=False)
print("wrote", os.listdir(G))

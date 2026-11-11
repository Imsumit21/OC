#!/usr/bin/env python3
"""Draft mode: write task_inputs/09_Rubrics.json from the plan rows (rubric_rows.py) and record the V3 rubric_rows evidence in
Working_Files/00_V3_Authoring_Evidence.json (calvin_qm_epic, rev3b). Every source_value is re-read in this run: seeded fields from
the parsed SQL (never executed), base fields from plan/oe_base.json (tools/hg.py reads by oe_reads.py)."""
import hashlib, importlib.util, json, os, re, shutil, sys
from collections import Counter
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools")); sys.path.insert(0, HERE)
from base_check import parse_sql
import stage_gate as SG
import reports as RP
spec = importlib.util.spec_from_file_location("rubric_rows", os.path.join(HERE, "rubric_rows.py")); RR = importlib.util.module_from_spec(spec); spec.loader.exec_module(RR)
ROWS = RR.R
ST = [x for x in parse_sql(open(os.path.join(TI, "01_Universe_Inject.sql")).read()) if x["op"] == "insert"]
OB = json.load(open(os.path.join(HERE, "oe_base.json")))
SEED = json.load(open(os.path.join(HERE, "seed_text.json"))); ID = {k: v["id"] for k, v in SEED.items()}
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
T = {r["n"]: r for r in RP.truth()}
def tr(n): return TRUTH[T[n]["report"]]
REVIEWER = "Claude (model-drafted under GEN_EXECUTION §2; for the human author's review)"
HUB_ID = ID["hub"]; HUB_STEP = {"service": "slack", "id": HUB_ID}
NOTE_STEP = {"service": "linear", "id": "ZOM-543"}
FREEZE = "the freeze 2025-10-01T07:00:00Z"
def sqlrow(table, **ident):
    rs = [x["row"] for x in ST if x["table"] == table and all(x["row"].get(k) == v for k, v in ident.items())]
    assert len(rs) == 1, (table, ident, len(rs)); return rs[0]
def sql_slack(rid, why, path=None):
    chan, ts = rid.split("/"); r = sqlrow("slack.slack_messages", channel_id=chan, ts=ts)
    return {"service": "slack", "id": rid, "source_file": "01_Universe_Inject.sql", "table": "slack.slack_messages", "identity": {"channel_id": chan, "ts": ts}, "column": "text", "source_value": r["text"],
            "evidence_path": [HUB_STEP] + (path or []) + ([{"service": "slack", "id": rid}] if rid != HUB_ID else []), "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": "created_at", "rationale": f"Seeded Slack message; created_at {r['created_at']} is before {FREEZE}; a posted message with no edit."}}
def sql_on(service, rid, table, ident, column, recorded, why, path=None):
    r = sqlrow(table, **ident)
    return {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table, "identity": ident, "column": column, "source_value": r[column], "evidence_path": [HUB_STEP] + (path or []) + [{"service": service, "id": rid}],
            "reachability_rationale": why, "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": recorded, "rationale": f"Seeded {table} row on {rid}; {recorded} {r[recorded]} is before {FREEZE}; a posted record with no edit."}}
def sql_mutable(service, table, ident, column, rid, recorded, why, extra, path=None):
    r = sqlrow(table, **ident)
    return {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table, "identity": ident, "column": column, "source_value": r[column], "evidence_path": [HUB_STEP] + (path or []) + [{"service": service, "id": rid}], "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": True, "recorded_at_column": recorded, "rationale": f"Seeded {table} row; {recorded} {r[recorded]} is before {FREEZE}.",
                                  "state_at_freeze_review": {"reviewer": REVIEWER, "rationale": extra, "evidence_ids": [rid, HUB_ID]}}}
def base_build(rid, why):
    v = OB["slack"][rid]
    return {"service": "slack", "id": rid, "source_file": v["file"], "pointer": f"{v['pointer']}/attachments/0/fallback", "source_value": v["rec"]["attachments"][0]["fallback"], "evidence_path": [HUB_STEP, NOTE_STEP, {"service": "slack", "id": rid}],
            "reachability_rationale": why, "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_pointer": f"{v['pointer']}/ts", "rationale": f"Base #builds post; ts {v['rec']['ts']} is before {FREEZE}; a posted bot message."}}
def base_pr(n, why):
    v = OB["github"][n]; rid = f"harmonygames-Games/match3d#{n}"
    return {"service": "github", "id": rid, "source_file": v["file"], "pointer": f"{v['pointer']}/merged_at", "source_value": v["rec"]["merged_at"], "evidence_path": [HUB_STEP, NOTE_STEP, {"service": "github", "id": rid}], "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": True, "recorded_at_pointer": f"{v['pointer']}/merged_at", "rationale": f"Base pull request; merged_at {v['rec']['merged_at']} is before {FREEZE}, and a merge does not change afterwards.",
                                  "state_at_freeze_review": {"reviewer": REVIEWER, "rationale": f"#{n} was merged before the freeze; the SQL changes only its updated_at (and, for #472, its description), not the merge.", "evidence_ids": [rid]}}}
def base_linear(k, why):
    v = OB["linear"][k]
    return {"service": "linear", "id": k, "source_file": v["file"], "pointer": f"{v['pointer']}/state_id", "source_value": v["rec"]["state_id"], "evidence_path": [HUB_STEP, {"service": "linear", "id": k}], "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": True, "recorded_at_pointer": f"{v['pointer']}/updated_at", "rationale": f"Base Linear issue; updated_at {v['rec']['updated_at']} is before {FREEZE}, so the exported state is its state at the freeze.",
                                  "state_at_freeze_review": {"reviewer": REVIEWER, "rationale": f"The SQL touches only {k}'s updated_at (a comment was added); the base state_id is the state at the freeze.", "evidence_ids": [k]}}}
W_NOTE = "The prompt names the Queue Manager ticket and Brian's DM says he left a note on it; the comment sits on ZOM-543."
def lin_comment(key, issue, why): return sql_on("linear", issue, "linear.linear_comments", {"id": ID[key]}, "body", "created_at", why, [NOTE_STEP] if issue != "ZOM-543" else None)
def tick(k): return sql_mutable("linear", "linear.linear_issues", {"id": k}, "state_id", k, "updated_at", f"Vincent's flow pass sheet names {k} in its Ticket column; the note sends the Agent to the tickets that already hold a report.",
                                f"{k} was filed by Vincent on Sep 30 2025 and last touched before the freeze; its seeded state_id is its state at the freeze.", [NOTE_STEP])
CAT = {
 "HUB": sql_slack(HUB_ID, "The prompt names Brian's message from yesterday; Calvin is a party to the DM."),
 "NOTE": lin_comment("epic_note", "ZOM-543", W_NOTE),
 "SHEETF": sql_mutable("gsheets", "gdrive.drive_files", {"id": ID["sheet"]}, "name", ID["sheet"], "modified_time", "Brian's note names Vincent's flow pass sheet; it is shared with Calvin.", "The sheet was last modified 2025-09-30T19:30:52Z, before the freeze; the grid in the SQL is its content at the freeze.", [NOTE_STEP]),
 "RULE": sql_mutable("gdocs", "gdocs.docs_documents", {"document_id": ID["rule_doc"]}, "body_text", ID["rule_doc"], "modified_time", "Brian's note names Arthur's rule for QA passes; the doc is shared with Calvin.", "The doc's modified time is before the freeze, so its body is its state at the freeze.", [NOTE_STEP]),
 "INLINE": sql_on("github", "harmonygames-Games/match3d#472", "github.github_review_comments", {"id": ID["inline"]}, "body", "created_at", "The sheet's Fix column names #472 and the note asks whether a fix is in main; the review comment sits on that pull request.", [NOTE_STEP]),
 "INLINE2": sql_on("github", "harmonygames-Games/match3d#475", "github.github_review_comments", {"id": ID["inline2"]}, "body", "created_at", "The sheet's Fix column names #475 and the note asks whether a fix is in main; the review comment sits on that pull request.", [NOTE_STEP]),
 "ELSE": sql_on("github", "harmonygames-Games/match3d#473", "github.github_pr_comments", {"id": ID["else_pr"]}, "body", "created_at", "The note asks whether a fix is in main; #473 merged into main on Sep 30 and Oliver's comment sits in its conversation.", [NOTE_STEP]),
 "REOPEN": sql_slack(ID["reopen"], "Arthur's rule ends a pass when the bug is seen again on a later main build; Vincent's reply is in #zombie-bugs, which Calvin is in.", [NOTE_STEP]),
 "BACK": sql_slack(ID["back"], "Arthur's rule ends a pass when the bug is seen again on a later main build; Robert's reply is in #zombie-bugs, which Calvin is in.", [NOTE_STEP]),
 "OLDER": sql_slack(ID["older"], "Arthur's rule ends a pass only on a later main build; Robert's post is in #zombie-match3d, which Calvin is in.", [NOTE_STEP]),
 "GLOW": sql_slack(ID["filt_dm"], "Brian's note takes in a bug told to Calvin in a DM since the 26th; Marcus's message is in Calvin's DM with him.", [NOTE_STEP]),
 "REOPEN2": lin_comment("reopen2", "ZOM-585", "The sheet names ZOM-585 for row 17; Samuel's later note sits on that ticket."),
 "BACK2": lin_comment("back2", "ZOM-586", "The sheet names ZOM-586 for row 24; Owen's later note sits on that ticket."),
 "ALIAS_GIFT": lin_comment("alias_gift", "ZOM-556", "The note asks whether a ticket already has the report; Vincent's note on ZOM-556 ties row 11 to it."),
 "ALIAS_STREAK": lin_comment("alias_streak", "ZOM-560", "The note asks whether a ticket already has the report; Vincent's note on ZOM-560 ties row 20 to it."),
 "Z556": base_linear("ZOM-556", "A search of the ZM tickets for the daily gift reaches ZOM-556."), "Z560": base_linear("ZOM-560", "A search of the ZM tickets for the freezer reaches ZOM-560."),
 "B1718": base_build("C05433XK267/1758817549.151639", "Arthur's rule says the branch is in the build's #builds post; Calvin is in #builds."),
 "B135": base_build("C05433XK267/1759263189.219529", "The later sightings name Android Submission 135; its #builds post gives its branch and time."),
 "B2006": base_build("C05433XK267/1759160363.685759", "Robert's post names Android 2006; its #builds post gives its time."),
 "B2013": base_build("C05433XK267/1759188882.419789", "Row 18's re-test names Android #2013; its #builds post gives its time."),
 "B1757": base_build("C05433XK267/1759257787.502039", "Row 34's re-test names iOS Internal #1757; its #builds post gives its time."),
 "B1745": base_build("C05433XK267/1759162758.968639", "Several re-tests name iOS Internal #1745; its #builds post gives its branch."),
 "PR465": base_pr("465", "The sheet's Fix column names #465."), "PR472": base_pr("472", "The sheet's Fix column names #472."), "PR475": base_pr("475", "The sheet's Fix column names #475."), "PR473": base_pr("473", "#473 is one of the pull requests merged into main since the pass began."),
 "INVITE": sql_on("gmail", ID["invite_v2"], "gmail.gmail_messages", {"id": ID["invite_v2"]}, "body_text", "date", "The prompt and Brian's DM name the review invite; it is in Calvin's inbox."),
 "EVT": sql_mutable("gcal", "gcal.gcal_events", {"event_id": ID["event"]}, "attendees_json", ID["event"], "updated", "The prompt names everyone on the review invite; the event is on Calvin's calendar.", "The event was last updated 2025-09-30T17:24:03Z, before the freeze, so its attendee list is the list at the freeze; the review itself starts after the clock."),
 "FOLDER": sql_mutable("gdrive", "gdrive.drive_files", {"id": ID["folder"]}, "name", ID["folder"], "modified_time", "The prompt names 'my ZM queue manager folder'; Calvin owns it.", "The folder was created on Sep 23 2025 and not modified after; its name is its state at the freeze."),
 "DECK": sql_mutable("gslides", "gdrive.drive_files", {"id": ID["deck"]}, "name", ID["deck"], "modified_time", "The prompt names 'my queue manager deck'; Calvin owns it and it sits in that folder.", "The deck was last modified on Sep 23 2025, before the freeze."),
}
for k in [x["row"]["id"] for x in ST if x["table"] == "linear.linear_issues"]: CAT["K_" + k] = tick(k)
def rep(n): return f"\"{T[n]['report']}\"" if n <= 38 else "Marcus Bennett's report that the season pass icon glow stays on after everything is claimed"
def decsrc(n):
    r = T[n]; t = r["trap"]
    if t == "BRANCH": return ["NOTE", "RULE", "B1718", "PR465"], f"Arthur's rule doc {ID['rule_doc']} ('For ZM a QA pass only counts on a build of the main branch'); the #builds post C05433XK267/1758817549.151639 (iOS Internal #1718, a feature-branch build); #465 merged into main"
    if t == "INLINE": k = "INLINE2" if n == 32 else "INLINE"; return ["NOTE", k], f"Arthur's review comment {ID['inline2' if n == 32 else 'inline']} on #{'475' if n == 32 else '472'} (the fix is not in that pull request)"
    if t == "ELSE": return ["NOTE", "ELSE", "PR473"], f"Oliver's comment {ID['else_pr']} on #473, merged into main Sep 30 2025 15:41 UTC (it lists this fix)"
    if t == "BODY": return ["NOTE", "PR472"], "the description of harmonygames-Games/match3d#472, merged into main Sep 30 2025 15:53 UTC ('this also holds the pre-level panel until the level-end coins have landed')"
    if t in ("REOPEN", "BACK"):
        k = {9: "REOPEN", 29: "BACK", 17: "REOPEN2", 24: "BACK2"}[n]; rid = {9: ID["reopen"], 29: ID["back"], 17: ID["reopen2"] + " on ZOM-585", 24: ID["back2"] + " on ZOM-586"}[n]
        return ["NOTE", "RULE", k, "B135"], f"the later sighting {rid} on Android Submission 135 (#builds C05433XK267/1759263189.219529, a main build made after the one it passed on); Arthur's rule doc {ID['rule_doc']} ('A pass stands until somebody sees the bug again on a main build made after the one it passed on')"
    if t == "FILT": return ["NOTE", "GLOW"], f"Marcus's DM {ID['filt_dm']} (Sep 30 2025) and the note's 'any bug somebody else on the team saw in a build and told you about in a DM'; no fix and no pass"
    if n == 27: return ["NOTE", "RULE", "OLDER", "B2006", "B1745"], f"Robert's post {ID['older']} is on Android #2006 (C05433XK267/1759160363.685759), posted before iOS Internal #1745 (C05433XK267/1759162758.968639), the build it passed on"
    if n == 18: return ["NOTE", "PR472", "B2013"], "the again was on Android #2013 (C05433XK267/1759188882.419789, Sep 29 23:34 UTC), before #472 merged (Sep 30 15:53 UTC), and Arthur's review comment says #472 has this fix"
    if n == 34: return ["NOTE", "PR475", "B1757"], "the again was on iOS Internal #1757 (C05433XK267/1759257787.502039, Sep 30 18:43 UTC), a main build made after #475 merged (16:09 UTC)"
    if r["status"] == RP.P: return ["NOTE", "RULE", "SHEETF"], f"row {n} of Vincent's sheet {ID['sheet']} ({r['retest']}, a main build per its #builds post) and Arthur's rule doc {ID['rule_doc']}"
    if n in (11, 20): return ["NOTE", "SHEETF", "ALIAS_GIFT" if n == 11 else "ALIAS_STREAK"], f"row {n} of Vincent's sheet {ID['sheet']} (no fix, no re-test) and Vincent's note on {'ZOM-556' if n == 11 else 'ZOM-560'}"
    return ["NOTE", "SHEETF"], f"row {n} of Vincent's sheet {ID['sheet']} (no fix named, no pass)"
WORD = {RP.P: "Passed (any wording with that meaning: pass, passed, done)", RP.Q: "Waiting on QA (any wording with that meaning: waits on QA, ready for QA, to re-test)", RP.F: "Waiting on a fix (any wording with that meaning: waits on a fix, needs a fix, fix pending)"}
OTHER = {RP.P: "Waiting on QA or Waiting on a fix", RP.Q: "Passed or Waiting on a fix", RP.F: "Passed or Waiting on QA"}
STATE = {RP.P: "Done", RP.Q: "In Validation", RP.F: "Todo"}
NOTE_SRC = f"Brian's note {ID['epic_note']} on ZOM-543"
def text(r):
    """(title, source text, catalog keys, reject line) for a plan row."""
    f = r["fact"]; kind, _, arg = f.partition(":")
    if f == "child_count": return ("The Agent creates exactly 10 child issues under the Linear ticket ZOM-543 (Queue Manager), one titled for each of Tutorials, Level-end rewards, Daily Gift, Season Pass, Collect & Win, Win Streak, Zombie Lane, Boss Arena, Endless Mode and Card packs (extra words around the area name are fine)",
                                    NOTE_SRC + " ('Children: Tutorials, Level-end rewards, Daily Gift, Season Pass, Collect & Win, Win Streak, Zombie Lane, Boss Arena, Endless Mode, Card packs. One child each, same team, no assignee.')", ["HUB", "NOTE"], "fewer or more than ten children, or a child on another ticket.")
    if kind == "child_assignee": return ("The Agent creates the Tutorials child issue under ZOM-543 with no assignee", NOTE_SRC + " ('One child each, same team, no assignee.')", ["NOTE"], "an assignee on the Tutorials child, or no Tutorials child.")
    if kind == "child_state": return (f"The Agent puts the {arg} child issue it creates under ZOM-543 in the state Todo (created in Todo or set to it)", NOTE_SRC + f" ('Set the child to Done if it is Clear and to Todo if it is Open'); {arg} has a report that is not Passed" + {"Zombie Lane": f" ({ID['back2']} on ZOM-586)", "Boss Arena": " (the ok on C05433XK267/1758817549.151639 was a feature-branch build)"}.get(arg, ""),
                                      ["NOTE"] + {"Zombie Lane": ["BACK2"], "Boss Arena": ["B1718", "RULE"]}.get(arg, ["SHEETF"]), f"the {arg} child in Done, or no {arg} child.")
    if kind in ("state", "note", "sheet_status"):
        n = int(arg); t = tr(n); keys, src = decsrc(n); tk = t["Ticket"]; st = STATE[t["Status"]]
        if kind == "state" and tk: return (f"The Agent sets {tk} (the report {rep(n)}) to the state {st}", NOTE_SRC + " ('put Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix'); status " + t["Status"] + ": " + src, keys + (["K_" + tk] if "K_" + tk in CAT else ["Z556" if tk == "ZOM-556" else "Z560"]),
                                           f"{tk} left in {t['Ticket state as found']} or set to another state.")
        if kind == "state": return (f"The Agent puts the sub-issue it creates for {rep(n) if n == 39 else 'the report ' + rep(n)} in the state {st}", NOTE_SRC + " ('make a sub-issue under the child with the report as the title and the state the same way'); status " + t["Status"] + ": " + src, keys, "that sub-issue in another state, or no sub-issue for that report.")
        if kind == "note": return (f"The Agent adds a note on {tk} (a comment, or text added to its description) that gives the status of the report {rep(n)} as {WORD[t['Status']]}", NOTE_SRC + " ('leave a note with the status and why'); " + src, keys, f"a note giving {OTHER[t['Status']]}, or no new note on {tk}.")
        return (f"The Agent gives {rep(n) if n == 39 else 'the report ' + rep(n)} the Status {WORD[t['Status']]} in the Reports tab of the stock-take sheet", NOTE_SRC + "; " + src, keys, f"{OTHER[t['Status']]} in that cell, or no row for that report.")
    if kind == "note_why":
        n = int(arg); tk = tr(n)["Ticket"]; keys, src = decsrc(n)
        why = {17: "the reason that the bug was seen again on Android Submission 135 after its pass (135 or Submission #135)", 24: "the reason that the bug was seen again on Android Submission 135 after its pass (135 or Submission #135)", 12: "the reason that pull request #472 does not have the fix (any wording with that meaning: not in #472, needs its own PR)",
               6: "the reason that the fix is in merged pull request #472 and QA has not tried it yet (any wording with that meaning)", 34: "the reason that it still happened on iOS Internal #1757, a build made after pull request #475 merged (any wording naming that build or that the fix did not hold)"}[n]
        return (f"The Agent gives, in its note on {tk}, {why}", NOTE_SRC + " ('leave a note with the status and why'); " + src, keys, f"a note on {tk} with no reason or another reason.")
    if f == "state_change_count": return ("The Agent changes the state of exactly 8 of the existing ZOM tickets it moves under the area child issues it creates under ZOM-543", NOTE_SRC + " ('If its state does not match the status, put Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix'); ZOM-568, ZOM-572, ZOM-573 and ZOM-584 to In Validation, ZOM-571, ZOM-574, ZOM-581 and ZOM-585 to Todo", ["NOTE", "INLINE", "INLINE2", "ELSE", "REOPEN2"], "fewer or more than eight tickets with a changed state.")
    if kind == "review_marked": c = {"Level-end rewards": 3, "Collect & Win": 4}[arg]; return (f"The Agent marks exactly {c} reports of the area {arg} as on the review list in the Reports tab of the stock-take sheet (any affirmative mark: Yes, Y, TRUE, a tick or x)", NOTE_SRC + f" ('Review list: a report that is not Passed, in an area on the agenda of Thursday's review'); the updated invitation {ID['invite_v2']} and the roadmap card 68daad83bacf52c6ea7e1593 (Collect & Win, Level-end rewards); " + ("rows 6, 8 and 36" if c == 3 else f"rows 15, 17, 18 and 19 (row 17 came back: {ID['reopen2']} on ZOM-585)"), ["NOTE", "INVITE"] + (["REOPEN2"] if c == 4 else []), f"another number of marked {arg} rows.")
    if kind == "sheet_area": n = int(arg); return (f"The Agent gives {rep(n) if n == 39 else 'the report ' + rep(n)} the Area {T[n]['area']} in the Reports tab of the stock-take sheet", (f"Marcus's DM {ID['filt_dm']} (the pass icon)" if n == 39 else f"row {n} of {ID['sheet']}"), ["NOTE", "GLOW" if n == 39 else "SHEETF"], "another area on that row, or no row for that report.")
    if f == "new_count": return ("The Agent creates exactly 17 new sub-issues under the area child issues it creates under ZOM-543", NOTE_SRC + " ('If no ticket has it, make a sub-issue under the child with the report as the title', 'No priority and no assignee on the new ones'); 39 reports, 22 held by a ticket (ZOM-567 to ZOM-586, ZOM-556, ZOM-560)", ["NOTE", "ALIAS_GIFT", "ALIAS_STREAK", "GLOW"], "16, 18 or 19 new sub-issues.")
    if kind == "new_parent": n = int(arg); return (f"The Agent creates the sub-issue for {rep(n) if n == 39 else 'the report ' + rep(n)} under the {T[n]['area']} child issue of ZOM-543", NOTE_SRC + f" ('make a sub-issue under the child'); area {T[n]['area']}" + (f" (Marcus's DM {ID['filt_dm']}: the pass icon)" if n == 39 else f" (row {n} of {ID['sheet']})"), ["NOTE", "GLOW" if n == 39 else "SHEETF"], "that sub-issue under another child or straight under ZOM-543.")
    if kind == "new_priority": n = int(arg); return (f"The Agent creates the sub-issue for the report {rep(n)} with no priority set (No priority, none or 0)", NOTE_SRC + " ('No priority and no assignee on the new ones')", ["NOTE"], "a priority on that sub-issue, or no sub-issue for that report.")
    if kind == "new_assignee": n = int(arg); return (f"The Agent creates the sub-issue for the report {rep(n)} with no assignee", NOTE_SRC + " ('No priority and no assignee on the new ones')", ["NOTE"], "an assignee on that sub-issue, or no sub-issue for that report.")
    if f == "moved_count": return ("The Agent moves exactly 22 existing ZOM tickets under the area child issues it creates under ZOM-543 (a ticket counts when its parent becomes one of those children)", NOTE_SRC + " ('if a ticket already has the report, move that ticket under the child'); the 20 keys in the Ticket column of " + ID["sheet"] + f" plus ZOM-556 ({ID['alias_gift']}) and ZOM-560 ({ID['alias_streak']})", ["NOTE", "SHEETF", "ALIAS_GIFT", "ALIAS_STREAK"], "20 or 21 tickets moved.")
    if kind == "move": n = int(arg); tk = tr(n)["Ticket"]; return (f"The Agent moves {tk} under the {T[n]['area']} child issue of ZOM-543", NOTE_SRC + f"; row {n} of {ID['sheet']} (area {T[n]['area']})" + (f"; Vincent's note {ID['alias_gift' if n == 11 else 'alias_streak']} on {tk}" if n in (11, 20) else ""), ["NOTE"] + (["ALIAS_GIFT" if n == 11 else "ALIAS_STREAK", "Z556" if n == 11 else "Z560"] if n in (11, 20) else ["SHEETF", "K_" + tk]), f"{tk} with no parent or under another child.")
    if f == "sheet_folder": return ("The Agent puts a new spreadsheet holding the stock-take in Calvin's Drive folder ZM queue manager (created there or moved in)", f"the prompt ('the stock-take sheet in my ZM queue manager folder'); folder {ID['folder']}", ["HUB", "FOLDER"], "the sheet outside that folder, or no new sheet.")
    if kind == "sheet_cols_reports": return ("The Agent gives the stock-take sheet a tab named Reports whose header has the columns Report, Area, Status, Ticket, Review list and Why (any order)", NOTE_SRC + " ('Sheet: tab Reports with Report, Area, Status, Ticket, Review list, Why.')", ["NOTE"], "a missing column or no tab named Reports.")
    if kind == "sheet_cols_areas": return ("The Agent gives the stock-take sheet a tab named Areas whose header has the columns Area, Status and Open reports (any order)", NOTE_SRC + " ('Tab Areas with Area, Status, Open reports.')", ["NOTE"], "a missing column or no tab named Areas.")
    if f == "sheet_rows": return ("The Agent lists exactly 39 reports in the Reports tab of the stock-take sheet, one row each (the 38 rows of Vincent's flow pass sheet and Marcus Bennett's pass icon glow report)", NOTE_SRC + f" ('Reports: the rows of Vincent's flow pass sheet, all of them', 'Plus any bug somebody else on the team saw in a build and told you about in a DM'); 38 rows in {ID['sheet']}; Marcus's DM {ID['filt_dm']}", ["NOTE", "SHEETF", "GLOW"], "38 or 40 report rows.")
    if kind == "sheet_ticket": n = int(arg); tk = tr(n)["Ticket"]; return (f"The Agent puts {tk} in the Ticket cell of the report {rep(n)} in the Reports tab of the stock-take sheet (the key or a link to it)", (f"Vincent's note {ID['alias_gift']} on ZOM-556" if n == 11 else f"row {n} of {ID['sheet']}"), (["ALIAS_GIFT", "Z556"] if n == 11 else ["SHEETF", "K_" + tk]), "another key or an empty Ticket cell on that row.")
    if kind == "sheet_review": n = int(arg); return (f"The Agent marks the report {rep(n)} as on the review list in the Reports tab of the stock-take sheet (any affirmative mark: Yes, Y, TRUE, a tick or x)", NOTE_SRC + f"; area {T[n]['area']} is on the agenda of the roadmap card 68daad83bacf52c6ea7e1593 (updated invitation {ID['invite_v2']}); the report is not Passed" + (f" ({ID['reopen2']} on ZOM-585)" if n == 17 else ""), ["NOTE", "INVITE"] + (["REOPEN2"] if n == 17 else []), "that row unmarked, or no row for that report.")
    if kind == "sheet_why": n = int(arg); return ((f"The Agent gives, in the Why cell of the report {rep(n)} in the Reports tab of the stock-take sheet, the reason that it was seen again after its pass (Vincent Parker's Sep 30 sighting on Android Submission 135; any wording with that meaning)", f"Vincent's reply {ID['reopen']}", ["NOTE", "REOPEN"], "a reason that leaves out the later sighting, or an empty Why cell.") if n == 9 else
                                                  (f"The Agent gives, in the Why cell of the report {rep(n)} in the Reports tab of the stock-take sheet, the reason that no fix for it is in main (any wording with that meaning: no fix yet, no pull request, not fixed)", f"row {n} of {ID['sheet']} (blank Fix and Re-test cells)", ["NOTE", "SHEETF"], "an empty Why cell on that row, or a reason saying it passed or was fixed."))
    if f == "area_rows": return ("The Agent lists exactly 10 areas in the Areas tab of the stock-take sheet, one row each", NOTE_SRC + " (the ten areas; 'Tab Areas with Area, Status, Open reports')", ["NOTE"], "fewer or more than ten area rows.")
    if kind == "area_status": return (f"The Agent gives {arg} the Status Open in the Areas tab of the stock-take sheet", NOTE_SRC + " ('A child is Clear when all its reports are Passed, otherwise Open'); " + ("row 24 came back (" + ID["back2"] + " on ZOM-586)" if arg == "Zombie Lane" else "row 25's ok was on the feature-branch build C05433XK267/1758817549.151639"), ["NOTE"] + (["BACK2"] if arg == "Zombie Lane" else ["B1718", "RULE"]), f"Clear for {arg}.")
    if kind == "area_open_count": c = RR.AO[arg]; return (f"The Agent shows {c} open report{'s' if c != 1 else ''} for {arg} in the Open reports column of the Areas tab of the stock-take sheet (the number {c}, or a list of exactly its {c} report{'s' if c != 1 else ''} that {'are' if c != 1 else 'is'} not Passed)", NOTE_SRC + f" ('Tab Areas with Area, Status, Open reports'); {arg}: {c} of its reports are not Passed", ["NOTE", "SHEETF"], f"another number for {arg}.")
    if kind == "share": nm = RR.names[arg]; return (f"The Agent shares the stock-take sheet with {nm} ({arg}@harmonygames.co) at any role", f"the review event {ID['event']} (attendee {arg}@harmonygames.co); Brian's DM {HUB_ID} ('share it with everyone on the review invite, Leonard too')", ["HUB", "EVT"], f"the sheet not shared with {nm}.")
    if f == "slide_new": return ("The Agent adds one new slide to Calvin's ZM queue manager presentation to carry the stock-take numbers", f"Brian's DM {HUB_ID} ('add one slide with the numbers to your queue manager deck'); deck {ID['deck']}", ["HUB", "DECK"], "the numbers written onto an existing slide, or no change to the deck.")
    if f == "dm_place": return ("The Agent sends a message in Calvin's Slack DM with Brian Foster (a new message or a reply in the thread under Brian's Sep 30 message)", f"the prompt ('message him in our DM'); Brian's DM {HUB_ID}", ["HUB"], "a message somewhere other than that DM.")
    if kind in ("dm", "slide"):
        lit, label = {k: (l, lab) for k, l, lab, _, _ in RR.NUM}[arg]
        extra = " (0, zero, none or no areas)" if arg == "clear" else ""
        art = "in its message to Brian Foster in Calvin's Slack DM with him" if kind == "dm" else "on the slide it adds to Calvin's ZM queue manager presentation"
        return (f"The Agent gives {lit} as the number of {label}{extra} {art}", f"Brian's DM {HUB_ID} ('how many reports are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many reports are on the review list'); computed over the 39 reports under " + NOTE_SRC, ["HUB", "NOTE"], f"another number for {label}.")
    if f == "dm_after_writes": return ("The Agent sends its message with the numbers to Brian Foster only once its Linear, stock-take sheet, sharing and slide writes are finished (at least one such write before the message and none after it)", f"the prompt ('Once that's done, message him in our DM'); Brian's DM {HUB_ID} ('When it is done tell me here')", ["HUB"], "the message sent before the set-up is finished.")
    raise KeyError(f)
crit, rows = [], []
for i, r in enumerate(ROWS, 1):
    title, src, keys, rej = text(r)
    title = title.replace("the stock-take sheet", "the stock-take spreadsheet it creates")
    assert title.startswith("The Agent ") and "sheet's" not in title, r["p"]
    just = r["kind"][0].upper() + r["kind"][1:] + "."
    crit.append({"title": title, "category": "Process" if r["cat"].startswith("Process") else "Outcome", "weight": r["band"], "justification": just, "evidence": f"Source: {src}. Accept: {title[len('The Agent '):]}. Reject: {rej}"})
    rows.append({"criterion_id": f"C{i}", "plan_row": r["p"], "fact_id": r["dup"].split(" ×")[0] if "×2" in r["dup"] else r["fact"], "prompt_span": r["span"], "accepted_outcomes": [r["valid"]], "alternatives_review": "Reject: " + rej + " Counter-reading: " + r["cr"],
                 "source_records": [CAT[k] for k in dict.fromkeys(keys)], "oe_steps": [f"OE {n}" for n in sorted(set(r["oe"]))], "valid_case": r["valid"], "do_nothing_case": r["idle"], "reachability": r["reach"]})
assert len({c["title"] for c in crit}) == len(crit)
out = os.path.join(TI, "09_Rubrics.json")
open(out, "w").write(json.dumps(crit, indent=1, ensure_ascii=False) + "\n")
ev_path = os.path.join(WF, "00_V3_Authoring_Evidence.json"); ev = json.load(open(ev_path))
ev["rubric_hash"] = SG.file_digest(Path(out)); ev["prompt_hash"] = SG.file_digest(Path(TI) / "04_Prompt.txt"); ev["rubric_rows"] = rows
open(ev_path, "w").write(json.dumps(ev, indent=1, ensure_ascii=False) + "\n")
keep = os.path.join(WF, "run_forensics", "rev3", "rubric"); os.makedirs(keep, exist_ok=True)
sha = hashlib.sha256(open(out, "rb").read()).hexdigest()[:12]; shutil.copy(out, os.path.join(keep, f"09_Rubrics_{sha}.json"))
fc = Counter(x["fact_id"] for x in rows); assert max(fc.values()) <= 2, [k for k, v in fc.items() if v > 2]
print("criteria", len(crit), "weights", dict(Counter(c["weight"] for c in crit)), "total", sum(c["weight"] for c in crit), "process", sum(c["category"] == "Process" for c in crit), "sha", sha)

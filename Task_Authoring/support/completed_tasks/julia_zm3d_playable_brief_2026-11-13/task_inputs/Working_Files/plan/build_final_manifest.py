#!/usr/bin/env python3
"""Build Working_Files/01_Hardness_Manifest.json (final, /create-injection rev2) from the scenario-certified draft and the SQL.
Every draft id is kept; changes are listed in design_delta. Adds what only the SQL settles: Slack row ids, the notes' real
times in version_records, the facts sheet with home_ids, integration_exceptions, solver {path, digest}. Re-run after any SQL
or solver change (the preflight binds this file by sha256, so no preflight digest is written back here)."""
import copy, hashlib, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
TI = WF.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(TI.parent / "tools"))
import design_model as M
import planned_texts as TXT
from base_check import parse_sql

draft = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())
man = copy.deepcopy(draft)
DRAFT_SHA = hashlib.sha256((WF / "01_Hardness_Manifest.draft.json").read_bytes()).hexdigest()[:12]
man["_note"] = (f"Final manifest (/create-injection {M.REV}, design {M.DESIGN}). Draft 01_Hardness_Manifest.draft.json ({DRAFT_SHA}, scenario-certified) "
                "plus the ids, facts and bindings only the SQL settles; every change is in design_delta.")
SQL_TEXT = (TI / "01_Universe_Inject.sql").read_text()
SLACK_ID, CMT_AT = {}, {}
for x in parse_sql(SQL_TEXT):
    if x.get("op") != "insert": continue
    r = x["row"]
    if x["table"] == "slack.slack_messages": SLACK_ID[f"{r['channel_id']}/{r['ts']}"] = r["id"]
    if x["table"] == "linear.linear_comments": CMT_AT[r["id"]] = r["created_at"]
S = M.SEED
def sl(x): return SLACK_ID.get(x, x) if isinstance(x, str) else x
def sl_list(xs): return [sl(x) for x in xs or []]
delta = []
for f in man["ask_fragments"]:
    f["seeded_ids"] = sl_list(f.get("seeded_ids"))
    if f.get("delegated_by_record") in SLACK_ID: f["delegated_by_record"] = SLACK_ID[f["delegated_by_record"]]
    if f["service"] == "slack" and f["container"] in SLACK_ID: f["container"] = SLACK_ID[f["container"]]
    if f["service"] == "slack" and f["locator"] in SLACK_ID: f["locator"] = SLACK_ID[f["locator"]]
for a in man["anchors"]:
    if a["service"] == "slack" and a["record"] in SLACK_ID:
        old = a["record"]; a["record"] = a["locator"] = SLACK_ID[old]
        delta.append({"id": f"anchor {a['id']}", "change": f"record/locator {old} -> {a['record']}",
                      "reason": "the gate reads a Slack message by its 32-hex row id (sha256 of channel|ts)"})
for a in man["authorities"]:
    a["seeded_ids"] = sl_list(a.get("seeded_ids")); a["decoy_seeded_ids"] = sl_list(a.get("decoy_seeded_ids"))
for t in man["traps"]:
    t["seeded_ids"] = sl_list(t.get("seeded_ids"))
    for v in t.get("version_records") or []:
        if not v.get("seeded"): continue
        vid = str(v.get("id"))
        if vid in SLACK_ID: v["id"] = SLACK_ID[vid]
        if vid in CMT_AT and v["at"] != CMT_AT[vid]:
            delta.append({"id": f"{t['id']} version_records", "change": f"note {vid}: at {v['at']} -> {CMT_AT[vid]}",
                          "reason": "the note's real created_at in the SQL (the draft carried the planned minute)"})
            v["at"] = CMT_AT[vid]
    if t.get("version_records"): t["version_records"] = sorted(t["version_records"], key=lambda v: v["at"])
for c in man["chains"]:
    for h in c["hops"]: h["record"] = sl(h["record"])
man["cohort"]["definition_source"] = sl_list(man["cohort"].get("definition_source"))
delta.append({"id": "record ids (all elements)", "change": "Slack 'channel/ts' pointers to seeded messages -> the messages' 32-hex row ids",
              "reason": "the gate reads text and timestamps from SQL rows, and a Slack message row is keyed by its id"})

def nid(name): return M.comment_id("note_" + name)
def notes_of(cls): return [nid(l["name"]) for l in M.members(cls)]
A1, A2, C3, PICKS, ZP = (SLACK_ID[S[k]["id"]] for k in ("a1_post", "a2_dm", "c3_reply", "picks", "zpicks"))
ev = json.loads((HERE / "out" / "sql_ids.json").read_text())
facts = [
    {"key": "files saved out of Unity are the text kind", "value": "the text kind", "kind": "status", "home_ids": [A1]},
    {"key": "bathroom UVs being redone", "value": "is redoing the UVs on the bathroom objects from scratch", "kind": "status", "home_ids": [A2]},
    {"key": "Friday's bathroom files are the old version", "value": "the bathroom files she gave <@EMPLOYEE_0026_SLACK_ID> on Friday are the old version too", "kind": "status", "home_ids": [A2]},
    {"key": "bow replaces the last pick", "value": "in place of the last one on my list", "kind": "status", "home_ids": [C3]},
    {"key": "instruments' zip will not unpack", "value": "won't unpack", "kind": "status", "home_ids": [S["c4_log"]["id"]]},
    {"key": "three recoloured items sent again", "value": "Claire sent the three recoloured models again", "kind": "status", "home_ids": [S["c4_log"]["id"]]},
    {"key": "re-sent items open and look right", "value": "Opened them, they look right, and they replace Thursday's", "kind": "status", "home_ids": [S["c4_log"]["id"]]},
    {"key": "rocket sound source", "value": "Soundly library (Robert's seat)", "kind": "status", "home_ids": [S["c2_sheet"]["id"]]},
    {"key": "explosion sound source", "value": "Universal Sound FX pack (Unity Asset Store, Robert's)", "kind": "status", "home_ids": [S["c2_sheet"]["id"]]},
    {"key": "the eight of 25 Sep", "value": "Shuriken, Cute Axe, Gift Box, Cactus Plant and Dynamite", "kind": "status", "home_ids": [PICKS]},
    {"key": "the four zombies", "value": "Party Girl, Plumber, Magician, Football Player", "kind": "status", "home_ids": [ZP]},
    {"key": "saved out of the project (twelve notes)", "value": "FBX saved out of the project, Thu 25 Sep", "kind": "status", "home_ids": notes_of("A1")},
    {"key": "zipped with the other instruments (eight notes)", "value": "Zipped with the other instruments", "kind": "status", "home_ids": notes_of("C4")},
    {"key": "handed over first thing on 25 Sep (three notes)", "value": "FBX from Claire, Thu 25 Sep, first thing", "kind": "status", "home_ids": notes_of("C1")},
    {"key": "PlayableX intake address", "value": TXT.CONTACT["email"], "kind": "status", "home_ids": [S["contact"]["id"]]},
    {"key": "kickoff hold", "value": TXT.HOLD_SUMMARY, "kind": "status", "must_appear_in": sorted(ev["events"].values())},
    {"key": "pack ticket rule", "value": "A line's ticket closes when PlayableX have the file", "kind": "status", "must_appear_in": [M.PACK_TICKET]},
]
man["facts"] = facts
FILES = [S[k]["id"] for k in ("notes", "tracker", "c2_sheet", "deck", "c4_log")]
man["integration_exceptions"] = [
    {"service": "gdrive", "int": "INT-13", "record_id": x,
     "reason": "integrations.json INT-13 seeding rule 'DM-only; seeded doc comments need not have one': the share is mirrored in the drive sharing rows and no Drive-app DM is seeded"}
    for x in FILES] + [
    {"service": "linear", "int": "INT-04", "record_id": f"{M.PACK_TICKET} and its children",
     "reason": "integrations.json INT-04: the team-channel posts are for ZOM and ENG tickets (#zombie-match3d, #god-bugs) and its seeding rule says a seeded Linear state change does not require a Slack notice; the pack tickets are Design-team tickets, created and noted outside Slack, so no Linear-app post is seeded"},
    {"service": "linear", "int": "INT-05", "record_id": f"{M.PACK_TICKET} and its children",
     "reason": "integrations.json INT-05 seeding rule: 'Digest mails are aggregate; a seeded Linear comment does not need a mail'"},
    {"service": "slack", "int": "INT-22", "record_id": SLACK_ID[S["ask"]["id"]],
     "reason": "integrations.json INT-22 seeding rule: 'Optional; never load-bearing'; none is seeded for the two DMs"},
]
man["solver"] = {"path": "Working_Files/solver/solver.py", "digest": hashlib.sha256((WF / "solver" / "solver.py").read_bytes()).hexdigest()}
man["gradable_surface"] = "01_Gradable_Surface.json"
man["design_delta"] = delta
(WF / "01_Hardness_Manifest.json").write_text(json.dumps(man, indent=1, ensure_ascii=False) + "\n")
print("wrote 01_Hardness_Manifest.json:", len(facts), "facts,", len(delta), "design_delta entries")

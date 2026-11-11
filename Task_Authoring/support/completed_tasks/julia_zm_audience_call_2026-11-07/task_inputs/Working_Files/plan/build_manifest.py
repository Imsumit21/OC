"""Write the final 01_Hardness_Manifest.json from the draft and the generated SQL. The draft is never changed.

Run: python3 plan/build_manifest.py [--preflight-digest HEX]. Reads the delegation quotes, version timestamps and home ids
from the SQL rows through base_check.parse_sql, so a quote or time that differs from the seeded record fails here.
"""
import copy
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
WF = HERE.parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "Task_Authoring" / "tools"))
sys.path.insert(0, str(HERE))
from base_check import parse_sql  # noqa: E402
import data as D  # noqa: E402

SQL = (WF.parent / "01_Universe_Inject.sql").read_text(encoding="utf8")
ROWS = [x for x in parse_sql(SQL) if x["op"] == "insert"]
draft = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text(encoding="utf8"))
m = copy.deepcopy(draft)
pr = m.pop("planned_records")
m.pop("_note", None)
m["_note"] = ("Final manifest for rev1, written by plan/build_manifest.py from the draft and the generated SQL. "
              "planned_records stay in the draft; the changes from it are in design_delta. No prompt, Oracle Event or "
              "criterion text.")


def slack(rid):
    return next(x["row"] for x in ROWS if x["table"] == "slack.slack_messages" and x["row"]["id"] == rid)


def unesc(s):
    return str(s).replace("''", "'")


ASK = PR_ASK = pr["ask"]["row"]
ask_text = unesc(slack(ASK)["text"])
delta = []
# 1. delegation quotes: verbatim from the seeded ask
for f in m["ask_fragments"]:
    q = f.get("delegation_quote")
    if q in D.QUOTE_CHANGES:
        new = D.QUOTE_CHANGES[q]
        assert new in (ask_text if f["delegated_by_record"].startswith("C090N54TG79/") else unesc(SQL)), new
        f["delegation_quote"] = new
        why = ("rev2 review M4: the gate Doc names Arthur's Vision Bot PR as where pass coverage is discussed, without the branch riddle"
               if f["id"] == "F-LIMIT" else
               "the note and Vincent's post have no base thread, so the rule records went top-level (NOTES D1); "
               "Robert, not Julia, asked who the panel players were at C090N54TG79/1758691397.679889")
        delta.append({"id": f["id"], "change": f"delegation_quote {q!r} -> {new!r}", "reason": why})
# 2. top-level records are their own containers
TOP = {"F-AGE": "1758554405.774120", "F-INDUSTRY": "1758733233.117446", "F-GATE": "1758728411.540327", "F-RET": "1759167008.881274"}
for f in m["ask_fragments"]:
    if f["id"] in TOP:
        old, f["container"] = f["container"], f"C090N54TG79/{TOP[f['id']]}"
        delta.append({"id": f["id"] + ":container", "change": f"container {old} -> {f['container']}",
                      "reason": "seeded top-level in C090N54TG79, not as a reply: its root has no base thread (NOTES D1)"})
for t in m["traps"]:
    for v in t.get("version_records") or []:
        if v.get("id") == pr["R5_retention_rule"]["row"]:
            v["container"] = "slack:C090N54TG79/1759167008.881274"
    if t["id"] == "T-RET":
        t["resolver"] = t["resolver"].replace("Robert's reply under Vincent's retention post", "Robert's channel post after Vincent's retention post")
        t["expected_wrong_reading"] = t["expected_wrong_reading"]
for c in m["cohort"].get("evidence_surfaces", []):
    pass
delta += [
    {"id": "R1_question,R1_answer,R2b_pointer,R3_industry_rule,R5_retention_rule",
     "change": "five records seeded top-level in C090N54TG79 with the design's ts and row ids; note_root_counters and R5 reply_count no longer apply",
     "reason": "C090N54TG79/1758517286.431379 and C090N54TG79/1759165414.829399 have reply_count 0 and no thread; replies under them would invent a thread (NOTES D1)"},
    {"id": "R4_panel_definition", "change": "the draft opening 'julia asked me the same thing so this is for both of you.' is not seeded",
     "reason": "the ask quote now says Robert asked, so the added clause is void (coordinator decision)"},
    {"id": "panel_forward.leonard_copy",
     "change": "leonard.hayes@harmonygames.co/<CAe46b4091acf4d325ec499084142670a7ee70@mail.gmail.com> -> leonard.hayes@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>",
     "reason": "both copies carry one Message-ID; base pattern is <mailbox>/<same Message-ID>"},
    {"id": "sender_mail_copies", "change": "17 sender mailbox copies added (15 forms, the re-sent form, Claire's later mail), each with a minted thread id and the Message-ID of Julia's copy",
     "reason": "Integrations row: the sender's copy sits in the sender's mailbox; the draft minted Julia's copies only"},
    {"id": "leonard_forward_thread", "change": "Leonard's forward copy gets its own minted thread row",
     "reason": "per-mailbox thread ids differ in base (NOTES D2)"},
    {"id": "claire_calendar_copy", "change": f"Claire's copy of the Friday event added as {D.CLAIRE_EVT}, ical_uid {D.ICAL_UID}",
     "reason": "one row per attendee calendar; base keeps a distinct event_id per calendar (NOTES D5)"},
    {"id": "harmonygames-Games/match3d#476#rc_28", "change": "rev2: the CodeRabbit reply rc_28 and its #zombie-prs mirror 2386636f2f828606f470fa38df201f16 are removed; root C093LEZGF6J/1759258475.735779 goes to reply_count 30, latest 1759263026.184402; PR updated_at 2025-09-30T20:10:26Z",
     "reason": "review 01d M3: base CodeRabbit replies carry their own empty review and an @mention and keep in_reply_to_id null; the reply also restated the deciding K3 fact"},
    {"id": "D076RBM29JS/1758658884.207315", "change": "rev2 adds Julia's Turkish question before Brian's line in D076RBM29JS",
     "reason": "review 01d m7: Brian's line answered nothing; the question anchors it to the Docs shared that morning"},
    {"id": "K3 membership", "change": "rev2 swaps session content (group, audience, stars, device, build, age, relation, notes) for ZOM-589/601, 592/603, 595/606, 597/620; K3 is ZOM-587, 588, 590, 591, 593, 594, 596, 601, 603, 606, 620; counts and means unchanged; rule controls moved to sessions the truth counts",
     "reason": "review 01d m6: each K3 observer's first round was all Samsung and the second had none"},
    {"id": "harmonygames-Games/match3d#476#rev_4", "change": "the empty CodeRabbit review row is not seeded, and its integration exception is dropped with it (rc_28 itself is removed in rev2)",
     "reason": "stage_gate re-runs base_check without --manifest, so rev_4 failed INT-01 (99% of 167) even with its exception; review-comment rows carry no review link, so nothing dangles; rc_28 keeps in_reply_to_id on rc_27. Reviewer note: 43 base review comments across #455, #460, #463, #466, #470 and 26 on #476 hold no in_reply_to_id, so a reply row has no base example in that sample"},
    {"id": "F_root_update", "change": "UPDATE of D05GU6L0XFH/1758901945.292269 keyed on channel_id and ts",
     "reason": "the root is a raw-shape export row with no id field, so an id-keyed UPDATE would match nothing"},
]
m["design_delta"] = delta

# 3. version timestamps from the rows
OWN = {"slack.slack_messages": "created_at", "gmail.gmail_messages": "date", "linear.linear_comments": "created_at",
       "github.github_review_comments": "created_at", "gslides.slides_presentations": "modified_time",
       "gsheets.sheets_spreadsheets": "modified_time", "gdocs.docs_documents": "modified_time"}
index = {}
for x in ROWS:
    r = x["row"]
    for k in ("id", "document_id", "spreadsheet_id", "presentation_id"):
        if r.get(k) and x["table"] in OWN:
            index[str(r[k])] = r[OWN[x["table"]]][:19] + "Z"
for t in m["traps"]:
    last = ""
    for v in t.get("version_records") or []:
        if v.get("seeded"):
            v["at"] = index[v["id"]]
        assert v["at"] > last, (t["id"], v)
        last = v["at"]

# 4. facts with home rows
docs = {s["ticket"]: s["notes_doc"] for s in pr["sessions"]}
cmts = {s["ticket"]: s["comment"] for s in pr["sessions"]}
kadikoy = [s["notes_doc"] for s in pr["sessions"] if s["group"] == "K4"]
facts = m["facts"]
facts += [
    {"key": "Kadıköy ekibi", "value": "Kadıköy ekibi", "kind": "id", "home_ids": kadikoy + [pr["K4_line"]["row"], D.row_id("D076RBM29JS", "1758658884.207315")]},
    {"key": "editor play mode limit", "value": "no phone in the loop", "kind": "status",
     "home_ids": ["harmonygames-Games/match3d#476#rc_27", pr["mirror_rc27"]["row"]]},
    {"key": "tie band", "value": "0.25", "kind": "amount", "home_ids": [D.PR["audience_deck"]["id"]]},
]
for s in D.SESSIONS:
    if s["group"] == "K3":
        facts.append({"key": f"device of {s['ticket']}", "value": s["device"], "kind": "id", "home_ids": [s["comment"]]})
m["facts"] = facts

# 5. exceptions, artifacts
m["integration_exceptions"] = [e for e in m["integration_exceptions"] if not e["record_id"].endswith("#rev_4")]
m["integration_exceptions"].append({"record_id": D.CLAIRE_EVT, "reason": "no_notify: Claire's copy of the same personal event; no invitation mail seeded"})
m["integration_exceptions"].append({"record_id": D.ICAL_UID, "reason": "no_notify: a personal event Julia declined; no invitation mail seeded"})
sys.path.insert(0, str(WF / "solver"))
import solver as SOLVER  # noqa: E402
for p in m["mechanism_portfolio"]:
    p["controls"] = list(SOLVER.RULES[p["id"]].get("controls") or [])
solver = WF / "solver" / "solver.py"
m["solver"] = {"path": "Working_Files/solver/solver.py", "digest": hashlib.sha256(solver.read_bytes()).hexdigest()}
surface = WF / "01_Gradable_Surface.json"
m["gradable_surface"] = {"path": "01_Gradable_Surface.json", "digest": hashlib.sha256(surface.read_bytes()).hexdigest()}
digest = sys.argv[sys.argv.index("--preflight-digest") + 1] if "--preflight-digest" in sys.argv else "0" * 64
m["preflight"] = {"report": "Working_Files/01c_Preflight_Report.json", "digest": digest}
(WF / "01_Hardness_Manifest.json").write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n", encoding="utf8")
print("final manifest written;", len(delta), "delta rows;", len(facts), "facts")

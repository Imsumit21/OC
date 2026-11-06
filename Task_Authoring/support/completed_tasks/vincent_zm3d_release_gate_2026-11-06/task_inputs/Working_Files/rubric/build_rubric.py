#!/usr/bin/env python3
"""Build 09_Rubrics.json, the V3 rubric_rows evidence and rows.json for vincent-zm3d-release-gate (injection rev18,
sha256 5a8d995238f3). Every quoted value is checked against its record here (seeded rows through base_check.parse_sql,
base records through hg.py get-many), never typed blind. Run from the workspace root."""
import json, re, subprocess, sys
from pathlib import Path

WS = Path(__file__).resolve().parents[4]
TI = WS / "Task_Authoring/task_inputs"
sys.path.insert(0, str(WS / "Task_Authoring/tools"))
from base_check import parse_sql  # noqa: E402

SQL = parse_sql((TI / "01_Universe_Inject.sql").read_text())
ROOTS = json.loads((TI / "Working_Files/00_Task_Context.json").read_text())["source"]["paths"]
PROMPT = (TI / "04_Prompt.txt").read_text()
REVIEWER = "Claude Opus 5.5 (model-drafted under GEN_EXECUTION section 2; for the human author's review)"


def sql_row(table, identity):
    rows = [x["row"] for x in SQL if x["table"] == table and x["op"] == "insert"
            and all(x["row"].get(k) == v for k, v in identity.items())]
    assert len(rows) == 1, (table, identity, len(rows))
    return rows[0]


_cache = {}


def get_json(service, rel, pointer):
    key = (service, rel, pointer)
    if key in _cache:
        return _cache[key]
    req = {"items": [{"service": service, "file": rel, "id": "v", "pointer": pointer, "max_chars": 65536}]}
    out = subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/hg.py"), "search", "get-many", "--request", "-",
                          "--task-dir", str(TI)], input=json.dumps(req), capture_output=True, text=True, cwd=WS)
    item = json.loads(out.stdout)["items"]["v"]
    assert item.get("encoding") == "rendered-json" and item.get("truncated") is False, (rel, pointer, item)
    _cache[key] = json.loads(item["text"])
    return _cache[key]


def has(text, quote):
    """Assert a quote is verbatim in a record's text (the evidence quotes are re-read, not typed)."""
    assert quote in text, (quote, text[:300])
    return quote


def path(*hops):
    return [{"service": s, "id": i} for s, i in hops]


def review(ids, why):
    return {"reviewer": REVIEWER, "rationale": why, "evidence_ids": ids}


SNAP = ("The synth-cut snapshot is cut at the freeze (2025-09-30 23:59:59 PT); the record's own last change is before "
        "the freeze, so the exported body is its state at the freeze. ")


def S_sql(service, rid, table, identity, column, rec_col, hops, why, semantics="fact", mutable=False, rev=None):
    row = sql_row(table, identity)
    src = {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table,
           "identity": identity, "column": column, "source_value": row[column],
           "evidence_path": path(*hops), "reachability_rationale": why,
           "temporal_evidence": {"value_semantics": semantics, "mutable_state": mutable, "recorded_at_column": rec_col,
                                 "rationale": f"Seeded {table} row; {rec_col} = {row[rec_col]} (before the freeze)."}}
    if mutable:
        src["temporal_evidence"]["state_at_freeze_review"] = rev
    return src


def S_json(service, rid, rel, pointer, rec_pointer, hops, why, semantics="fact", mutable=False, rev=None):
    root = Path(ROOTS[service])
    value = get_json(service, rel, pointer)
    recorded = get_json(service, rel, rec_pointer)
    src = {"service": service, "id": rid, "source_file": str((root / rel).relative_to(WS)), "pointer": pointer,
           "source_value": value, "evidence_path": path(*hops), "reachability_rationale": why,
           "temporal_evidence": {"value_semantics": semantics, "mutable_state": mutable, "recorded_at_pointer": rec_pointer,
                                 "rationale": f"Base record; {rec_pointer} = {recorded} (before the freeze)."}}
    if mutable:
        src["temporal_evidence"]["state_at_freeze_review"] = rev
    return src


# ---- anchors the prompt names -------------------------------------------------------------------------------------
THREAD = ("slack", "C08R27X0EAH/1759263900.484190")      # "Arthur's candidates thread in #zombie-bugs"
SHEET = ("gsheets", "f_0ebfccf33076f9dbf086bc")           # "my release gate sheet"
RUNBOOK = ("confluence", "page_qa_runbook")               # "the QA regression runbook"
RULES = ("gdocs", "f_632c44650df44fe252ee59")             # ZOM-570: "Leonard's submission rules ... shared with you"
CUTDOC = ("gdocs", "f_a038a576ca8db6955fae95")            # ZOM-570: "my note on how we cut submissions"
CARD = ("trello", "68d1eb90bef538c7c5c5599d")             # ZOM-570: "the tech-issues card"
UPDOC = ("gdocs", "f_5e40215b7d4d24b0455412")
DM_UPDATE = ("slack", "D0770ET1HV2/1759272300.342229")

# ---- seeded sources (scoped, persona-visible) ---------------------------------------------------------------------
s_thread = S_sql("slack", THREAD[1], "slack.slack_messages", {"id": "4fa3fdf1ee07241aa316b91d1944af4d"}, "text",
                 "created_at", [THREAD], "The prompt names Arthur's candidates thread in #zombie-bugs (Vincent is a member); "
                 "the post says 'details on ZOM-570'.")
s_vpost = S_sql("slack", "C08R27X0EAH/1759274400.792657", "slack.slack_messages", {"id": "d9ed6d99a7b4fef0175ab2e3277a8615"},
                "text", "created_at", [THREAD, ("slack", "C08R27X0EAH/1759274400.792657")],
                "Vincent's own Sep 30 re-check post in the same #zombie-bugs channel as the prompt's thread.")
s_v133 = S_sql("slack", "C08R27X0EAH/1759140300.935009", "slack.slack_messages", {"id": "ae66526624c68d840fe3cd4eb15b876d"},
               "text", "created_at", [THREAD, ("slack", "C08R27X0EAH/1759140300.935009")],
               "Vincent's Sep 29 post in the same #zombie-bugs channel (re-test on the older #133 / #49 builds).")
s_rules = S_sql("gdocs", RULES[1], "gdocs.docs_documents", {"document_id": RULES[1]}, "body_text", "modified_time",
                [THREAD, RULES], "Arthur's post points to ZOM-570, whose description says Leonard's submission rules apply "
                "and are shared with Vincent; a Drive search for 'submission' finds the doc.", mutable=True,
                rev=review([RULES[1], THREAD[1]], SNAP + "The doc was created and last modified 2025-09-23T09:10:00Z; "
                           "Arthur's Sep 30 post and ZOM-570 point to it as the rules in force."))
s_cut = S_sql("gdocs", CUTDOC[1], "gdocs.docs_documents", {"document_id": CUTDOC[1]}, "body_text", "modified_time",
              [THREAD, CUTDOC], "ZOM-570's description names Arthur's note on how submissions are cut, shared with Vincent; "
              "a Drive search for 'submission' finds it.", mutable=True,
              rev=review([CUTDOC[1], THREAD[1]], SNAP + "Created and last modified 2025-09-24T14:20:00Z, before the Sep 30 "
                         "candidates; ZOM-570 names it as in force."))
s_update = S_sql("gdocs", UPDOC[1], "gdocs.docs_documents", {"document_id": UPDOC[1]}, "body_text", "modified_time",
                 [THREAD, DM_UPDATE, UPDOC], "Brian's DM tells Vincent the update-path rows are in a doc shared with him; a "
                 "Drive search for 'Update-path' finds it (the runbook's update rows send the gate there).", mutable=True,
                 rev=review([UPDOC[1], DM_UPDATE[1]], SNAP + "Modified 2025-09-30T22:35:00Z; Brian's 22:45 UTC DM points to "
                            "it as finished."))
s_dm458 = S_sql("slack", "D0770ET1HV2/1759160460.731000", "slack.slack_messages", {"id": "062eb44cc80d3720d2902cca36178133"},
                "text", "created_at", [THREAD, ("linear", "ZOM-458"), ("slack", "D0770ET1HV2/1759160460.731000")],
                "The ZOM-458 and ZOM-535 comments say 'same as Brian found'; a Slack search for 'ZOM-458' finds this DM "
                "between Vincent and Brian.")
s_dm535 = dict(s_dm458, evidence_path=path(THREAD, ("linear", "ZOM-535"), ("slack", "D0770ET1HV2/1759160460.731000")))
s_dm473 = S_sql("slack", "D0770ET1HV2/1759267800.858041", "slack.slack_messages", {"id": "80f2a1385b02b6138522f7cf7adf5bed"},
                "text", "created_at", [THREAD, ("linear", "ZOM-473"), ("slack", "D0770ET1HV2/1759267800.858041")],
                "Brian's DM to Vincent names ZOM-473; a Slack search for 'ZOM-473' finds it.")
s_doug36 = S_sql("slack", "D079SNE2TL4/1759269712.483915", "slack.slack_messages", {"id": "ea5e1f0622bf3da5154f00c7fe5426f7"},
                 "text", "created_at", [THREAD, ("slack", "D079SNE2TL4/1759269712.483915")],
                 "Vincent's DM with Douglas; ZOM-567's comment names match3d-backend #36 and a Slack search for '#36' finds "
                 "Douglas's rollout note.")
s_cobalt = S_sql("gmail", "vincent.parker@harmonygames.co/1844730396672762606", "gmail.gmail_messages",
                 {"id": "vincent.parker@harmonygames.co/<CAMqj9qxCY/UrgcY+k8V+eQN9o/J+VewHirZkOrQC4RSCncTWeC@mail.gmail.com>"},
                 "body_text", "date", [THREAD, ("linear", "ZOM-562"),
                                       ("gmail", "vincent.parker@harmonygames.co/1844730396672762606")],
                 "In Vincent's inbox; a Gmail search for 'TestFlight 50' (the iOS candidate) finds the vendor's session notes.")
s_sheet = S_sql("gsheets", SHEET[1], "gsheets.sheets_spreadsheets", {"spreadsheet_id": SHEET[1]}, "title", "modified_time",
                [SHEET], "The prompt names 'my release gate sheet'; Vincent owns ZM3D Release Gate.", mutable=True,
                rev=review([SHEET[1]], SNAP + "Last modified 2025-09-23T10:05:00Z; the title is the one the prompt refers to."))

# ---- base sources -------------------------------------------------------------------------------------------------
LIN = {"ZOM-293": 3347, "ZOM-435": 3502, "ZOM-449": 3517, "ZOM-458": 3527, "ZOM-473": 3543, "ZOM-483": 3554,
       "ZOM-535": 3609, "ZOM-546": 3621, "ZOM-554": 3630, "ZOM-559": 3635, "ZOM-560": 3637, "ZOM-562": 3639,
       "ZOM-429": 3495, "ZOM-434": 3501, "ZOM-503": 3576, "ZOM-506": 3579, "ZOM-517": 3591, "ZOM-557": 3633,
       "ZOM-558": 3634, "ZOM-561": 3638, "ZOM-563": 3640, "ZOM-564": 3641, "ZOM-481": 3552, "ZOM-477": 3547,
       "ZOM-536": 3610, "ZOM-513": 3587}


def s_lin(key, field="title", extra=()):
    n = LIN[key]
    assert get_json("linear", "data.json", f"/issues/{n}/id") == key
    return S_json("linear", key, "data.json", f"/issues/{n}/{field}", f"/issues/{n}/created_at",
                  [THREAD, RULES, *extra, ("linear", key)],
                  f"{key} is a team ZOM ticket in Leonard's scope (open, or Done after the Sep 22 cut); linear_list_issues "
                  f"for team ZOM lists it.", mutable=True,
                  rev=review([key, RULES[1]], SNAP + "Linear ticket as exported at the freeze; its state and fields are "
                             "the ones the gate reads."))


def s_builds(idx, ts, why):
    assert get_json("slack", "messages/C05433XK267/2025-09.json", f"/{idx}/ts") == ts
    return S_json("slack", f"C05433XK267/{ts}", "messages/C05433XK267/2025-09.json", f"/{idx}/ts", f"/{idx}/ts",
                  [THREAD, CUTDOC, ("slack", f"C05433XK267/{ts}")], why)


def s_doug(idx, ts, why):
    assert get_json("slack", "messages/D079SNE2TL4/2025-09.json", f"/{idx}/ts") == ts
    return S_json("slack", f"D079SNE2TL4/{ts}", "messages/D079SNE2TL4/2025-09.json", f"/{idx}/text", f"/{idx}/ts",
                  [THREAD, ("linear", "ZOM-563"), ("slack", f"D079SNE2TL4/{ts}")], why)


s_b50 = s_builds(1120, "1759257812.041449", "Public #builds (Vincent is a member); Arthur's note says the Started line in "
                 "#builds decides what a submission holds. This is iOS Submission #50's Started post.")
s_b135 = s_builds(1122, "1759257934.076209", "Public #builds; Android Submission #135's Started post.")
s_b2028 = s_builds(1129, "1759268201.182309", "Public #builds; Match3D Android #2028's Started post, the first main build "
                   "whose Changes carry the season-pass join-popup fix.")
s_b1974 = s_builds(902, "1758755609.200489", "Public #builds; Match3D Android #1974's main Changes post (2025-09-24 "
                   "23:13:29 UTC), the only change that may be ZOM-473's fix, before both candidates' Started lines.")
s_doug_deploy = s_doug(263, "1759256193.859279", "Vincent's DM with Douglas; Vincent sent him the ZOM-563 link and a Slack "
                       "search for 'ZOM-563' finds the thread.")
s_doug_ok = s_doug(265, "1759269524.769369", "Same DM; Vincent's confirmation on prod.")
s_runbook = S_json("confluence", RUNBOOK[1], "confluence_working.json", "/pages/7/body", "/pages/7/updated_at", [RUNBOOK],
                   "The prompt names the QA regression runbook; confluence_search finds the page.", mutable=True,
                   rev=review([RUNBOOK[1]], SNAP + "Page version 2, updated 2025-08-04T10:00:00Z."))
assert get_json("confluence", "confluence_working.json", "/pages/7/id") == RUNBOOK[1]
s_card = S_json("trello", CARD[1], "data.json", "/cards/802/name", "/cards/802/dateLastActivity", [THREAD, CARD],
                "ZOM-570's description names 'the tech-issues card'; trello_search for 'TECH ISSUES' finds 'Fix TECH ISSUES' "
                "on the ZM ROADMAP board, whose comments hold the reuse rule and Leonard's #135 re-test.", mutable=True,
                rev=review([CARD[1], THREAD[1]], SNAP + "The card name as exported at the freeze."))
assert get_json("trello", "data.json", "/cards/802/id") == CARD[1]

# ---- seeded record texts used in quotes (re-read here) ------------------------------------------------------------
CMT = {r["row"]["id"]: r["row"] for r in SQL if r["table"] == "linear.linear_comments" and r["op"] == "insert"}
ISS = {r["row"]["id"]: r["row"] for r in SQL if r["table"] == "linear.linear_issues" and r["op"] == "insert"}
TRELLO = {r["row"]["id"]: json.loads(r["row"]["data_json"])["text"] for r in SQL if r["table"] == "trello.trello_actions"}
RC1 = sql_row("github.github_review_comments", {"id": "harmonygames-Games/match3d-backend#36#rc_1"})["body"]
CONTACT = sql_row("contacts.contacts", {"contact_id": "29016e2ba1a844a2509b847b"})["job"]
SHEET0 = json.loads(sql_row("gsheets.sheets_sheets", {"spreadsheet_id": SHEET[1], "sheet_id": "0"})["grid_json"])
SHEET1 = json.loads(sql_row("gsheets.sheets_sheets", {"spreadsheet_id": SHEET[1], "sheet_id": "1"})["grid_json"])
HOW = json.dumps(SHEET0, ensure_ascii=False)
RULES_T = s_rules["source_value"]
CUT_T = s_cut["source_value"]
UPD_T = s_update["source_value"]
RUN_T = s_runbook["source_value"].replace("&amp;", "&")
VPOST = s_vpost["source_value"]
Z570 = ISS["ZOM-570"]["description"]


def c(cid, quote):
    return has(CMT[cid]["body"], quote)


def d(key, quote):
    return has(ISS[key]["description"], quote)


# ---- prompt spans -------------------------------------------------------------------------------------------------
SPAN_TAB = "Put the gate register in a new tab of my release gate sheet"
SPAN_BLOCK = "add the blockers to the release ticket's description"
SPAN_FILE = "file a new ZM ticket in Linear for anything the checks in the QA regression runbook turn up that nobody has filed yet"
SPAN_REPLY = "Reply in Arthur's candidates thread in #zombie-bugs with the QA call"
for s in (SPAN_TAB, SPAN_BLOCK, SPAN_FILE, SPAN_REPLY):
    assert s in PROMPT, s

TAB = "its new tab of the ZM3D Release Gate spreadsheet"
CL_FREEZE = has(RULES_T, "Blocker = crash, freeze, player stuck or can't finish a level")
CL_LOST = has(RULES_T, "lost progress / coins / lives (infinite-lives time included) / boosters / inventory items")
CL_PURCH = has(RULES_T, "or a purchase that doesn't deliver")
CLAUSE = {"ZOM-293": CL_LOST, "ZOM-435": CL_FREEZE, "ZOM-449": CL_FREEZE, "ZOM-458": CL_LOST, "ZOM-473": CL_LOST,
          "ZOM-483": CL_LOST, "ZOM-535": CL_FREEZE, "ZOM-546": CL_FREEZE, "ZOM-554": CL_FREEZE, "ZOM-559": CL_FREEZE,
          "ZOM-560": CL_PURCH, "ZOM-562": CL_LOST, "ZOM-567": CL_LOST, "ZOM-569": CL_FREEZE, "ZOM-573": CL_FREEZE,
          "ZOM-576": CL_LOST, "ZOM-578": CL_FREEZE, "DES-313": CL_FREEZE}
BLOCKER_RULE = has(RULES_T, "Blocker = crash, freeze, player stuck or can't finish a level (like the orange juice one), lost "
                   "progress / coins / lives (infinite-lives time included) / boosters / inventory items, or a purchase "
                   "that doesn't deliver.")
KNOWN_RULE = has(RULES_T, "Any other bug a player can see is a known issue, even if it doesn't change play, visual and sound "
                 "glitches included.")
SCOPE_RULE = has(RULES_T, "every ZM ticket that's still open (any state but Done, Canceled or Duplicate), whatever team or "
                 "label (ART or DES tickets with ZM in the title count too), plus everything that moved to Done after the "
                 "last gate's builds were cut (Android #127 / iOS #40 on Sep 22)")
FIX_RULE = has(RULES_T, "A ticket counts as fixed when Vincent or Brian saw it working on the candidate builds, or on prod if "
               "the fix is server side.")
LATEST_RULE = has(RULES_T, "if the latest check on the candidates still shows the bug, call it on how bad it is whatever the "
                  "ticket says")
NOCALL_ART = has(RULES_T, "replacing an outdated model or icon with its new version included), even with a Bug label and even "
                 "once it's Done")
REUSE = has(TRELLO["68dc3ef455344e471b1d2ea9"], "anything that blocks goes on ZOM-570 under the ticket that already exists, no "
            "duplicate tickets")
BY_KEY = has(Z570, "Blockers go on this ticket by key, the existing ticket if there is one")
EVID_DEF = has(HOW, "id or link of the record that decides the row")
assert SHEET1[2][0] == "ZOM-559" and SHEET1[2][3] == "not reproduced on #127 (Pixel)" and SHEET1[2][4] == "KNOWN ISSUE"

R = []


def row(**k):
    k.setdefault("cat", "Outcome")
    R.append(k)


# =====================================================================================================================
# Register: tab, name, volume
# =====================================================================================================================
row(tag="tab", t="The Agent adds exactly one new spreadsheet tab while running the gate, in Vincent's ZM3D Release Gate "
    "spreadsheet (f_0ebfccf33076f9dbf086bc)", w=1, kind="lookup", why="direct: the prompt names the sheet and asks for a new tab",
    fact="register.tab", span=SPAN_TAB, oe=["OE 7", "OE 32"], fids="F9 F41", vals="`ZM3D Release Gate` `f_0ebfccf33076f9dbf086bc`",
    verify="One new tab in ZM3D Release Gate", final="Third tab of f_0ebfccf33076f9dbf086bc",
    acc=["one new tab added to ZM3D Release Gate, any name"],
    alt="Writing the register into the existing 'Sep 22 - Android #127 / iOS #40' tab, into a separate new spreadsheet, or "
        "across two new tabs fails ('One tab per gate'). The tab's name is graded separately.",
    srcs=[s_sheet],
    just="Lookup: the prompt asks for 'a new tab of my release gate sheet', and the sheet's How we gate tab says 'One tab "
         "per gate'.",
    ev="Sources: Vincent's spreadsheet ZM3D Release Gate f_0ebfccf33076f9dbf086bc, How we gate tab ('One tab per gate, named "
       "after the candidate builds. One row per ticket.'). Accept: exactly one tab added in the run, and it is in that "
       "spreadsheet; a tab added to any other spreadsheet, a new spreadsheet, or a second tab fails.",
    dist="T12 (the Sep 22 tab): writing over it fails", amb="none", dec="H2", grp="none", valid="One tab 'Sep 30 - Android "
    "#135 / iOS #50' added by addSheet", idle="No tab added to ZM3D Release Gate")
row(tag="tabname", t="The Agent names its new ZM3D Release Gate tab after the candidate builds: the name carries the build "
    "numbers 135 and 50, and any platform labels in it pair 135 with Android and 50 with iOS", w=1, kind="lookup", why="direct: one line in the sheet's How we gate tab",
    fact="register.tab_name", span=SPAN_TAB, oe=["OE 7", "OE 32"], fids="F9 F41", vals="`135` `50`",
    verify="Tab name", final="Title of the new tab",
    acc=["Sep 30 - Android #135 / iOS #50", "Oct 1 - Android #135 / iOS #50", "Android Submission #135 / iOS Submission #50",
         "#135 / #50"],
    alt="A name without the candidate builds ('Gate register', 'Oct 1 gate') fails; any date prefix, platform names, '#' "
        "or 'Submission' wording passes.", srcs=[s_sheet, s_thread],
    just="Lookup: the How we gate tab says 'One tab per gate, named after the candidate builds', and the candidates are "
         "Android Submission #135 and iOS Submission #50.",
    ev="Sources: How we gate tab of ZM3D Release Gate f_0ebfccf33076f9dbf086bc ('One tab per gate, named after the "
       "candidate builds.'); Arthur Blake's post C08R27X0EAH/1759263900.484190 ('Android Submission #135 and iOS "
       "Submission #50'). Accept: the new tab's name contains 135 and 50, with or without a date, '#' or 'Submission'; platform labels, when "
       "present, read Android #135 and iOS #50 (a name that swaps them fails).",
    dist="none", amb="none", dec="H2", grp="none", valid="'Oct 1 - Android #135 / iOS #50'",
    idle="No new tab, so no tab name")
row(tag="regonly", t="The Agent writes this gate's register rows only into its new tab of the ZM3D Release Gate spreadsheet",
    w=1, kind="lookup", why="direct: the prompt and the How we gate tab put the register in one new tab per gate",
    fact="register.target", span=SPAN_TAB, oe=["OE 7", "OE 33"], fids="F9 F10 F41", vals="`ZM3D Release Gate`",
    verify="Register write target", final="Cells written for the register",
    acc=["register rows written to the new tab only, in one or several writes"],
    alt="Also writing the register over the 'Sep 22 - Android #127 / iOS #40' tab, the How we gate tab or another file fails.",
    srcs=[s_sheet],
    just="Lookup: the prompt says 'Put the gate register in a new tab of my release gate sheet' and the How we gate tab "
         "says 'One tab per gate'; the Sep 22 tab is the previous gate's register.",
    ev="Sources: ZM3D Release Gate f_0ebfccf33076f9dbf086bc, How we gate tab ('One tab per gate, named after the candidate "
       "builds. One row per ticket.') and the previous gate's tab 'Sep 22 - Android #127 / iOS #40'. Accept: every write of "
       "this gate's register rows targets the new tab; writes to the Sep 22 tab, the How we gate tab or any other file "
       "fail.",
    dist="T12 (the Sep 22 tab)", amb="none", dec="H2 T12", grp="none", valid="values_update and values_append on the new "
    "tab only", idle="No register rows written")
row(tag="count133", t="The Agent writes exactly 133 ticket rows, one per ticket, in its new tab of the ZM3D Release Gate "
    "spreadsheet for Leonard's gate scope: every ZM ticket in any team (ART and DES tickets with ZM in the title included) "
    "whose state is anything but Done, Canceled or Duplicate, every ZM ticket moved to Done after the last gate's cut "
    "(Android Submission #127 Started 2025-09-22 12:30:43 UTC), and the new ticket it files, with the release ticket "
    "ZOM-570, ZOM-359 and ZOM-475 left out (header row not counted)", w=5,
    kind="multi-source",
    why="the count only follows from the full scope audit: every open ZM ticket of every team, the Done-after-cut set "
        "dated by the #127 / #40 Started lines in #builds, the named exclusions and the ticket filed during the gate",
    fact="register.keys", span=SPAN_TAB, oe=["OE 5", "OE 9", "OE 10", "OE 31", "OE 33"], fids="F6 F12 F13 F14 F38",
    vals="`133`", verify="Register row count", final="Ticket rows on the new tab",
    acc=["133 rows: the 112 open in-scope tickets, the 20 Done after 2025-09-22 12:30:43 UTC and the ticket the Agent files"],
    alt="The Bug-label view (the Sep 22 scope), a list that keeps ZOM-570, ZOM-359 or ZOM-475, one that drops ART-790, "
        "ART-792, ART-793 or DES-313, or one that leaves out the new update-path ticket gives another count and fails.",
    srcs=[s_rules, s_b135],
    just="Multi-source: Leonard's scope ('every ZM ticket that's still open ..., whatever team or label ..., plus everything "
         "that moved to Done after the last gate's builds were cut', release tickets, ZOM-359 and ZOM-475 out, tickets "
         "filed while the gate runs in) gives 112 open plus 20 Done after the #127 / #40 cut plus the new ticket.",
    ev="Sources: Leonard's 'ZM submission rules' doc f_632c44650df44fe252ee59 (scope sentence and 'tickets filed while the "
       "gate is running get a row too, including the ones you file yourself'); #builds C05433XK267/1758544243.280239 "
       "(Android #127 Started 2025-09-22 12:30:43 UTC); Linear teams ZOM, ART and DES. Accept: exactly 133 rows that each "
       "give one in-scope ticket its own entry; a row for ZOM-570, ZOM-359 or ZOM-475 fails, and so does any other count.",
    dist="T6, T14, T17 (the Bug view, the 'Minor Bugs to Fix' card, the release tickets)", amb="none", dec="H2 T6 T14 CH6",
    grp="volume row for G1-G5", valid="133 rows: 112 open, 20 Done since the cut, ZOM-581", idle="No register rows written")

# =====================================================================================================================
# Register: call column. BLOCKER and FIXED classes are graded in full; KNOWN ISSUE and NO CALL are sampled (G1).
# =====================================================================================================================
BLK = []   # (tag, key, weight, kind, oe, fids, dec, srcs, reason, records, accept_extra)

BLK.append(("293", "ZOM-293", 3, "interpretation", ["OE 11", "OE 13", "OE 14", "OE 33"], "F18", "T17 H2",
            [s_lin("ZOM-293"), s_rules],
            "the ticket's description is only 'Dynamic Difficulty Tiering', but Vincent's comment says what goes wrong: "
            "the glue and trampoline taken for the retry were gone after the tier reload; lost boosters is a blocker and "
            "the open ticket was never re-checked on the candidates",
            f"ZOM-293 comment cmt_zom293_1 (Vincent Parker, 2025-07-03T17:42:00Z: '{c('cmt_zom293_1', 'both gone, 600 coins worth')}')"))
BLK.append(("435", "ZOM-435", 5, "multi-source", ["OE 8", "OE 19", "OE 25", "OE 33"], "F11 F23", "T3 CH2 H2",
            [s_card, s_lin("ZOM-435"), s_v133],
            "the ticket is Done and Vincent's Sep 29 post on #133 / #49 says the trophy path claim spam is ok, but "
            "Leonard's later re-test on Android #135 on the Trello card Fix TECH ISSUES got stuck again; a player stuck on "
            "the candidate is a blocker",
            f"Trello comment 68dc63484a5b2d0a869e758f on card 68d1eb90bef538c7c5c5599d 'Fix TECH ISSUES' (Leonard Hayes, "
            f"2025-09-30T23:10:00Z: '{has(TRELLO['68dc63484a5b2d0a869e758f'], 'tapped claim twice fast and got stuck on the path again, only killing the app got me out. same as ZOM-435')}'); "
            f"Vincent's post C08R27X0EAH/1759140300.935009 (2025-09-29, on #133 / #49)"))
BLK.append(("449", "ZOM-449", 3, "interpretation", ["OE 11", "OE 14", "OE 33"], "F18", "H2", [s_lin("ZOM-449", "description"), s_rules],
            "Brian's latest check on the candidate is a freeze, which Leonard's rules make a blocker",
            f"ZOM-449 comment cmt_zom449_2 (Brian Foster, 2025-09-30T22:20:00Z: '{c('cmt_zom449_2', 'Android #135 on the same low-end device: cold start into level 3 froze again')}')"))
BLK.append(("458", "ZOM-458", 5, "multi-source", ["OE 17", "OE 20", "OE 33"], "F21 F24", "T16 H2", [s_dm458, s_lin("ZOM-458")],
            "the ticket and Vincent's #135 note read as a wrong level-pass animation, but the note points to what Brian "
            "found, and Brian's Sep 29 DM says the level's chest showed as claimed while nothing reached the inventory; "
            "lost inventory items is a blocker",
            f"ZOM-458 comment cmt_zom458_1 ('{c('cmt_zom458_1', 'same as Brian found on #133 / #49')}'); Brian Foster's DM "
            f"D0770ET1HV2/1759160460.731000 (2025-09-29, Turkish: \"{has(s_dm458['source_value'], 'o levelın chesti claimed görünüyor, envantere hiçbir şey gelmedi')}\": "
            f"the chest shows claimed and nothing reached the inventory)"))
BLK.append(("473", "ZOM-473", 5, "multi-source", ["OE 17", "OE 20", "OE 25", "OE 33"], "F14 F25", "T3b H2",
            [s_dm473, s_lin("ZOM-473", "completed_at")],
            "the ticket is Done (2025-09-22), but Brian's Sep 30 re-test on iOS #50 in his DM shows the end screen can "
            "still be tapped away and half the run's coins are lost; lost coins is a blocker",
            f"Brian Foster's DM D0770ET1HV2/1759267800.858041 (2025-09-30T21:30 UTC, Turkish: \"{has(s_dm473['source_value'], 'endless bitiş ekranı iOS #50' + chr(39) + 'de hala geçilebiliyor.')}\" and "
            f"\"{has(s_dm473['source_value'], 'coinler x2 olmadan geldi, run' + chr(39) + 'ın coinlerinin yarısı gitti')}\": on iOS #50 the end screen can still be skipped, the coins came without the x2 and half the run's coins were lost); ZOM-473 Done 2025-09-22T15:11:51Z"))
BLK.append(("483", "ZOM-483", 3, "interpretation", ["OE 11", "OE 14", "OE 33"], "F18", "H2", [s_lin("ZOM-483"), s_rules],
            "the latest check on #135 shows lost infinite-lives time, which Leonard's rules list as a blocker",
            f"ZOM-483 comment cmt_zom483_1 (2025-09-30T22:14:00Z: '{c('cmt_zom483_1', 'The 20 min are gone.')}')"))
BLK.append(("535", "ZOM-535", 5, "multi-source", ["OE 17", "OE 20", "OE 33"], "F21 F24", "T16 H2", [s_dm535, s_lin("ZOM-535")],
            "the ticket and Vincent's #135 note read as a matching inefficiency, but the note points to what Brian found, "
            "and Brian's Sep 29 DM says the boss arena could not be finished in three tries; a level that can't be finished "
            "is a blocker",
            f"ZOM-535 comment cmt_zom535_1 ('{c('cmt_zom535_1', 'same as Brian found on #133')}'); Brian Foster's DM "
            f"D0770ET1HV2/1759160460.731000 (2025-09-29, Turkish: \"{has(s_dm458['source_value'], '3 denemede de boss arenayı bitiremedim')}\": could not finish the boss arena in 3 tries)"))
BLK.append(("546", "ZOM-546", 3, "interpretation", ["OE 11", "OE 14", "OE 33"], "F18", "H2", [s_lin("ZOM-546"), s_rules],
            "the latest check on #135 / #50 shows the endless run can't go on, which Leonard's rules make a blocker",
            f"ZOM-546 comment cmt_zom546_1 (2025-09-30T21:48:00Z: '{c('cmt_zom546_1', 'the run can' + chr(39) + 't go on.')}')"))
BLK.append(("554", "ZOM-554", 3, "interpretation", ["OE 11", "OE 14", "OE 33"], "F18", "H2", [s_lin("ZOM-554"), s_rules],
            "the latest check on #50 leaves the next level unplayable until a force-quit (player stuck), a blocker",
            f"ZOM-554 comment cmt_zom554_2 (2025-09-30T21:54:00Z: '{c('cmt_zom554_2', 'had to force-quit again.')}')"))
BLK.append(("559", "ZOM-559", 3, "comparison", ["OE 7", "OE 11", "OE 14", "OE 33"], "F10 F18", "T12 H2",
            [s_lin("ZOM-559", "description"), s_rules],
            "the Sep 22 tab called it KNOWN ISSUE from a Pixel check, but its latest check, Brian's Sep 29 run on a Samsung "
            "S22, froze at the victory screen; nobody saw it working on the candidates, so it is called on the freeze",
            f"ZOM-559 comment cmt_zom559_1 (Brian Foster, 2025-09-29T15:20:00Z: '{c('cmt_zom559_1', 'the victory screen froze with the reward panel half drawn for about 20 seconds; only a force-quit got me out')}'); "
            f"the Sep 22 tab of f_0ebfccf33076f9dbf086bc ('not reproduced on #127 (Pixel)', KNOWN ISSUE) is older"))
BLK.append(("560", "ZOM-560", 3, "interpretation", ["OE 11", "OE 14", "OE 33"], "F18", "H2", [s_lin("ZOM-560"), s_rules],
            "the latest check on #135 shows a purchase that doesn't deliver, a blocker",
            f"ZOM-560 comment cmt_zom560_1 (2025-09-30T22:06:00Z: '{c('cmt_zom560_1', 'the win streak freezer time still didn' + chr(39) + 't.')}')"))
BLK.append(("562", "ZOM-562", 5, "multi-source", ["OE 17", "OE 21", "OE 22", "OE 33"], "F21 F26 F27", "T5 CH4 T13 H2",
            [s_cobalt, s_lin("ZOM-562")],
            "Vincent's #135 note reads cosmetic, but the playtest vendor's notes on TestFlight build 50 (the game under its "
            "old name, Puzzles vs Zombies) say the boss-fight orphan items cost players a life; lost lives is a blocker",
            f"Cobalt Playtesting's email 'Session notes - Sep 30 (Puzzles vs Zombies, TestFlight 50)' in Gmail thread "
            f"vincent.parker@harmonygames.co/1844730396672762606 ('{has(s_cobalt['source_value'], 'Each of them lost a life and had to start the fight again.')}'); "
            f"sender's contact 29016e2ba1a844a2509b847b ('{CONTACT}'); ZOM-562 'Orphan items in boss arena'"))
BLK.append(("567", "ZOM-567", 5, "multi-source", ["OE 17", "OE 23", "OE 24", "OE 33"], "F21 F29 F30", "T2 H1 H2",
            [s_doug36, s_cut],
            "the ticket is Done, backend PR #36 is merged and Douglas says it is rolled out ('the code side'), but Arthur's "
            "later review comment on the PR says the chest rows were never loaded on prod and his claimed chest did not "
            "land; inventory items are still lost on prod, a blocker",
            f"Arthur Blake's review comment harmonygames-Games/match3d-backend#36#rc_1 (2025-09-30T22:35:00Z: "
            f"'{has(RC1, 'runs by hand per environment and hasn' + chr(39) + 't been run on prod')}'); Douglas's DM "
            f"D079SNE2TL4/1759269712.483915 ('{has(s_doug36['source_value'], 'that' + chr(39) + 's the code side')}')"))
BLK.append(("569", "ZOM-569", 5, "multi-source", ["OE 6", "OE 17", "OE 25", "OE 33"], "F7 F21 F31", "T1 CH1 H1 H2",
            [s_b2028, s_b135, s_b50, s_cut],
            "the ticket was closed at 18:05 UTC after 'fixed on my branch', but a submission holds only what was on main "
            "when its job started, and the fix first lands in Match3D Android #2028, started after both candidates; the "
            "empty Season Pass screen that only killing the app escapes is a blocker",
            f"#builds Started posts C05433XK267/1759257812.041449 (iOS Submission #50, 18:43:32 UTC) and "
            f"C05433XK267/1759257934.076209 (Android Submission #135, 18:45:34 UTC); Match3D Android #2028, Started "
            f"C05433XK267/1759268201.182309 (21:36:41 UTC), whose Changes post C05433XK267/1759268589.049939 lists 'Fix season "
            f"pass main screen instance from join popup'; Arthur's doc f_a038a576ca8db6955fae95 ('{has(CUT_T, 'A submission has exactly what was on main when its job started')}'); "
            f"ZOM-569 description ('{d('ZOM-569', 'the only way out is killing the app')}')"))
BLK.append(("573", "ZOM-573", 3, "interpretation", ["OE 10", "OE 18", "OE 33"], "F22", "H2", [s_rules],
            "the ticket filed on Android #135 describes a crash, a blocker",
            f"ZOM-573 description ('{d('ZOM-573', 'claiming the 5th chest in Collect&Win closes the app straight to the home screen')}')"))
BLK.append(("576", "ZOM-576", 3, "interpretation", ["OE 10", "OE 18", "OE 33"], "F22", "H2", [s_rules],
            "the ticket filed on iOS #50 describes lost boosters from a premium claim, a blocker",
            f"ZOM-576 description ('{d('ZOM-576', 'only the gems land and the tier is marked claimed, so the boosters are gone.')}')"))
BLK.append(("578", "ZOM-578", 3, "interpretation", ["OE 10", "OE 18", "OE 33"], "F22", "T6 CH6 H2", [s_rules],
            "the unlabeled ticket is an open ZM ticket in scope ('whatever team or label') and its report on Android #135 "
            "is a player stuck, a blocker",
            f"ZOM-578 description ('{d('ZOM-578', 'Can' + chr(39) + 't get past it, killed the app twice and it comes back to the same step.')}')"))
BLK.append(("des313", "DES-313", 3, "interpretation", ["OE 10", "OE 11", "OE 14", "OE 33"], "F13 F18", "T6 CH6 H2", [s_rules],
            "the Design-team ticket has ZM in its title, so Leonard's scope brings it in, and its latest check on #135 is a "
            "level that can't be finished, a blocker",
            f"DES-313 'ZM level 214 can't be completed', comment cmt_des313_1 (2025-09-30T22:38:00Z: '{c('cmt_des313_1', 'level 214 still only spawns 2 jars, can' + chr(39) + 't finish it.')}')"))

for tag, key, w, kind, oe, fids, dec, srcs, reason, records in BLK:
    row(tag=f"reg_{tag}", t=f"The Agent records the call BLOCKER for {key} in {TAB}", w=w, kind=kind, why=reason,
        fact=f"{key}.call", span=SPAN_TAB, oe=oe, fids=fids, vals=f"`{key}` `BLOCKER`", verify=f"{key} call",
        final=f"{key}'s call cell on the new tab", acc=[f"{key} call BLOCKER"],
        alt=f"Any other call for {key} (KNOWN ISSUE, FIXED or NO CALL), or no {key} row, fails.", srcs=srcs,
        just=f"{kind.capitalize()}: {reason}.",
        ev=f"Sources: {records}; Leonard's 'ZM submission rules' doc f_632c44650df44fe252ee59 (\"{CLAUSE[key]}\"). "
           f"Accept: {key}'s call cell reads BLOCKER.",
        dist="T-ID " + dec.split()[0] if dec.split()[0].startswith("T") else "none", amb="none", dec=dec,
        grp="BLOCKER class, graded in full (19)", valid=f"{key} | ... | BLOCKER", idle=f"No register, so no {key} row")

NEWT = "the new ticket it files for the iOS N-1 update save reset"
new_srcs = [s_update, s_runbook]
new_records = (f"Brian Foster's doc 'Update-path run - iOS #50 / Android #135' f_5e40215b7d4d24b0455412 "
               f"('{has(UPD_T, 'After the update the save came back at level 1 with 500 coins')}'); the QA Regression "
               f"Runbook page_qa_runbook ('{has(RUN_T, 'A failure in any UPDATE column blocks the release')}'); Leonard's doc "
               f"f_632c44650df44fe252ee59 ('{has(RULES_T, 'including the ones you file yourself')}')")
row(tag="reg_new", t=f"The Agent records the call BLOCKER for {NEWT} in {TAB}", w=5, kind="multi-source",
    why="the ticket only exists after the runbook's update rule, Brian's update-path doc and the existing-ticket check; "
        "Leonard's scope gives it a row and its lost progress and coins make it a blocker",
    fact="newticket.call", span=SPAN_TAB, oe=["OE 26", "OE 28", "OE 31", "OE 33"], fids="F6 F33 F35 F40", vals="`BLOCKER`",
    verify="New ticket's register row", final="The new ticket's row on the new tab", acc=["the new ZOM key with call BLOCKER"],
    alt="Leaving the new ticket out of the register, or calling it anything but BLOCKER, fails.", srcs=new_srcs,
    just="Multi-source: Leonard's rules give tickets filed while the gate runs a row ('including the ones you file "
         "yourself'), and the update-path failure (save back at level 1 with 500 coins) is lost progress and coins, a "
         "blocker; the runbook also makes any update-column failure block the release.",
    ev=f"Sources: {new_records}. Accept: the row for the new update-path ticket, by its new ZOM key, has the call BLOCKER.",
    dist="T4, T10 (Brian's 'regression matrix green')", amb="none", dec="T4 CH3 T10 H2", grp="BLOCKER class, graded in full (19)",
    valid="ZOM-581 | iOS #50 over N-1 resets the save | n/a | ... | BLOCKER", idle="No new ticket and no register")

FIX = [("429", "ZOM-429", ["OE 16", "OE 33"], "F20", "H2", [s_lin("ZOM-429"), s_rules],
        "the ticket is still open (Backlog), but Vincent re-tested both candidates and could not reproduce it, which counts "
        "as seen working",
        f"ZOM-429 comment cmt_zom429_1 (Vincent Parker, 2025-09-30T20:48:00Z: '{c('cmt_zom429_1', 'Couldn' + chr(39) + 't reproduce on #135 or #50')}')", 3),
       ("434", "ZOM-434", ["OE 19", "OE 33"], "F23", "H2", [s_vpost, s_lin("ZOM-434")],
        "the ticket moved to Done after the Sep 22 cut and Vincent's Sep 30 re-check on #135 / #50 lists it as working",
        f"Vincent's post C08R27X0EAH/1759274400.792657 ('{has(VPOST, 'ZOM-434 no flying items after backgrounding during load')}')", 3),
       ("503", "ZOM-503", ["OE 19", "OE 33"], "F23", "H2", [s_vpost, s_lin("ZOM-503")],
        "the ticket moved to Done after the Sep 22 cut and Vincent's Sep 30 re-check on #135 / #50 lists it as ok",
        f"Vincent's post C08R27X0EAH/1759274400.792657 ('{has(VPOST, 'ZOM-503 giving lives ok')}')", 3),
       ("506", "ZOM-506", ["OE 19", "OE 33"], "F23", "H2", [s_vpost, s_lin("ZOM-506")],
        "the ticket moved to Done after the Sep 22 cut and Vincent's Sep 30 re-check on #135 / #50 lists it as ok",
        f"Vincent's post C08R27X0EAH/1759274400.792657 ('{has(VPOST, 'ZOM-506 zombie lane text ok')}')", 3),
       ("517", "ZOM-517", ["OE 16", "OE 33"], "F20", "H2", [s_lin("ZOM-517"), s_rules],
        "the ticket is still open (Backlog), but Vincent could not reproduce it on either candidate, which counts as seen "
        "working",
        f"ZOM-517 comment cmt_zom517_1 (Vincent Parker, 2025-09-30T21:24:00Z: '{c('cmt_zom517_1', 'Can' + chr(39) + 't reproduce on #135 or #50 any more')}')", 3),
       ("557", "ZOM-557", ["OE 19", "OE 33"], "F23", "H2", [s_vpost, s_lin("ZOM-557")],
        "the ticket moved to Done after the Sep 22 cut and Vincent's Sep 30 re-check on #135 / #50 lists it as ok",
        f"Vincent's post C08R27X0EAH/1759274400.792657 ('{has(VPOST, 'ZOM-557 consecutive login ok')}')", 3),
       ("558", "ZOM-558", ["OE 12", "OE 19", "OE 33"], "F16 F23", "H2", [s_vpost, s_lin("ZOM-558")],
        "the ticket reads like a UI-layout ask that Leonard's rules call no call, but Leonard's own comment on the ticket "
        "overrides that rule ('Gate it like any other bug'), and Vincent's separate Sep 30 re-check post in Slack shows it "
        "working on #135 / #50",
        f"Leonard Hayes's ZOM-558 comment cmt_zom558_1 ('{c('cmt_zom558_1', 'Gate it like any other bug.')}'); Vincent's post "
        f"C08R27X0EAH/1759274400.792657 ('{has(VPOST, 'ZOM-558 weekly board says Level: now')}')", 5),
       ("561", "ZOM-561", ["OE 19", "OE 33"], "F23", "H2", [s_vpost, s_lin("ZOM-561")],
        "the ticket moved to Done after the Sep 22 cut and Vincent's Sep 30 re-check on #135 / #50 lists it as ok",
        f"Vincent's post C08R27X0EAH/1759274400.792657 ('{has(VPOST, 'ZOM-561 low-end black surfaces ok')}')", 3),
       ("563", "ZOM-563", ["OE 23", "OE 33"], "F28", "T7 CH5 H2", [s_doug_deploy, s_doug_ok, s_lin("ZOM-563")],
        "the ticket is still In Progress, but the fix is server side: Douglas updated prod and Vincent then saw it working "
        "on prod, which Leonard's rules count as fixed",
        f"Vincent's DM with Douglas: D079SNE2TL4/1759256193.859279 ('{has(s_doug_deploy['source_value'], 'Ok, I updated the prod environment with the latest teams/social changes')}') "
        f"and D079SNE2TL4/1759269524.769369 ('{has(s_doug_ok['source_value'], 'Yep it works as expected')}')", 5),
       ("564", "ZOM-564", ["OE 16", "OE 33"], "F20", "T15 H2", [s_lin("ZOM-564"), s_rules],
        "the ticket is still Todo, but Brian checked it on both candidates and it worked",
        f"ZOM-564 comment cmt_zom564_1 (Brian Foster, 2025-09-30T21:20:00Z: '{c('cmt_zom564_1', 'Checked on iOS #50 and Android #135')}' ... "
        f"'{c('cmt_zom564_1', 'Used one and it took one, as it should.')}')", 3)]
FIX = [f for f in FIX if f[0] in ("429", "558", "563")]
for tag, key, oe, fids, dec, srcs, reason, records, w in FIX:
    kind = "multi-source" if w == 5 else "interpretation"
    row(tag=f"fix_{tag}", t=f"The Agent records the call FIXED for {key} in {TAB}", w=w, kind=kind, why=reason,
        fact=f"{key}.call", span=SPAN_TAB, oe=oe, fids=fids, vals=f"`{key}` `FIXED`", verify=f"{key} call",
        final=f"{key}'s call cell on the new tab", acc=[f"{key} call FIXED"],
        alt=f"Any other call for {key}, or no {key} row, fails.", srcs=srcs,
        just=f"{kind.capitalize()}: {reason}.",
        ev=f"Sources: {records}; Leonard's doc f_632c44650df44fe252ee59 ('{FIX_RULE}'). Accept: {key}'s call cell reads FIXED.",
        dist="T-ID " + dec.split()[0] if dec.split()[0].startswith("T") else "none", amb="none", dec=dec,
        grp="FIXED class, graded in full (10)", valid=f"{key} | ... | FIXED", idle=f"No register, so no {key} row")

SAMP = [("art793", "ART-793", "KNOWN ISSUE", 3, "interpretation", ["OE 10", "OE 11", "OE 15", "OE 33"], "F13 F19", "T6 CH6 H2",
         [s_rules], "the Art-team ticket has ZM in its title, so Leonard's scope brings it in, and its latest check on #50 "
         "is a visible flicker with play unaffected, a known issue",
         f"ART-793 'ZM3D - boss arena background flickers on iPhone 12', comment cmt_art793_1 (2025-09-30T22:34:00Z: "
         f"'{c('cmt_art793_1', 'the backdrop still flickers in the boss arena.')}'); description '{d('ART-793', 'Gameplay is fine')}'; "
         f"Leonard's doc f_632c44650df44fe252ee59 ('{KNOWN_RULE}')", "edge: another team"),
        ("481", "ZOM-481", "KNOWN ISSUE", 3, "interpretation", ["OE 11", "OE 15", "OE 33"], "F19", "H2", [s_lin("ZOM-481"), s_rules],
         "the latest check on #135 shows a visible bug that does not stop the level, a known issue",
         f"ZOM-481 comment cmt_zom481_2 (2025-09-30T22:10:00Z: '{c('cmt_zom481_2', 'the health bar still hangs around for a second after the death animation. Level finishes.')}'); "
         f"Leonard's doc f_632c44650df44fe252ee59 ('{KNOWN_RULE}')", "ordinary"),
        ("477", "ZOM-477", "NO CALL", 1, "lookup", ["OE 12", "OE 13", "OE 33"], "F16 F17", "H2", [s_lin("ZOM-477"), s_rules],
         "Leonard's comment on the ticket rules it a tuning ask with no call for the store gates",
         f"Leonard Hayes's ZOM-477 comment cmt_zom477_1 (2025-09-24T09:20:00Z: '{c('cmt_zom477_1', 'No call for the store gates.')}')",
         "edge: reads like a bug; a ruling decides"),
        ("536", "ZOM-536", "NO CALL", 3, "interpretation", ["OE 12", "OE 13", "OE 33"], "F16 F17", "H2", [s_lin("ZOM-536"), s_rules],
         "the ticket asks for an updated icon and 3D model; Leonard's rules make such asks no call even with a Bug label "
         "and even once Done",
         f"ZOM-536 'Trampoline icon is not consistent and model should be updated.' (label Bug, Done 2025-09-30T12:40:23Z); "
         f"Leonard's doc f_632c44650df44fe252ee59 ('{NOCALL_ART}')", "edge: Bug label and Done after the cut"),
        ("513", "ZOM-513", "NO CALL", 1, "lookup", ["OE 13", "OE 33"], "F17", "H2", [s_lin("ZOM-513", "labels"), s_rules],
         "the ticket is an art request (labels 3D Art and Improvement), no call",
         f"ZOM-513 'Convert Maracas into multi-color variant-enabled', labels 3D Art and Improvement; Leonard's doc "
         f"f_632c44650df44fe252ee59 ('{has(RULES_T, 'Art/VFX requests, requests for design, balance or tuning changes, analytics, tools, backend endpoints and new features aren' + chr(39) + 't bugs, no call.')}')",
         "ordinary")]
SAMP = [x for x in SAMP if x[0] != "513"]
for tag, key, call, w, kind, oe, fids, dec, srcs, reason, records, why_s in SAMP:
    row(tag=f"smp_{tag}", t=f"The Agent records the call {call} for {key} in {TAB}", w=w, kind=kind, why=reason,
        fact=f"{key}.call", span=SPAN_TAB, oe=oe, fids=fids, vals=f"`{key}` `{call}`", verify=f"{key} call",
        final=f"{key}'s call cell on the new tab", acc=[f"{key} call {call}"],
        alt=f"Any other call for {key}, or no {key} row, fails.", srcs=srcs, just=f"{kind.capitalize()}: {reason}.",
        ev=f"Sources: {records}. Accept: {key}'s call cell reads {call}.",
        dist="T-ID T6" if "T6" in dec else "none", amb="none", dec=dec, grp=f"G1 sample ({why_s})", valid=f"{key} | ... | {call}",
        idle=f"No register, so no {key} row")

# =====================================================================================================================
# Register: other columns (G2 build status, G3 QA result, G4 evidence, G5 title), sampled
# =====================================================================================================================
HOW_NOT_IN = has(HOW, "a Done bug whose fix landed after the Started line")
HOW_NOT_LIVE = has(HOW, "a server-side fix with any part not on prod yet, even if its code is deployed")
HOW_LIVE = has(HOW, "a server-side fix that's fully on prod, including any migration or data it needs")
HOW_IN = has(HOW, "a Done bug whose fix was on main at the job's Started line, even if the re-test still shows the bug "
             "(if nothing shows when the fix landed, go by when the ticket was closed)")
HOW_NA = has(HOW, "everything else: open bugs that still show up or nobody re-tested, no-call tickets")
HOW_QA = has(HOW, "a bug QA re-tested on the candidates and saw working or couldn't reproduce")
BS = [("569", "ZOM-569", "not in candidate", "the fix is not in Android Submission #135 or iOS Submission #50", 5, "multi-source",
       ["OE 6", "OE 25", "OE 33"], "F7 F9 F31", "T1 CH1 H1", [s_b2028, s_b135, s_cut],
       "the season-pass fix first lands on main in Match3D Android #2028 (Started 21:36:41 UTC), after both candidates' "
       "Started lines (18:43:32 and 18:45:34 UTC)", HOW_NOT_IN,
       "#builds C05433XK267/1759268201.182309 (#2028 Started 21:36:41 UTC) and its Changes post C05433XK267/1759268589.049939 "
       "('Fix season pass main screen instance from join popup'), "
       "C05433XK267/1759257812.041449 and C05433XK267/1759257934.076209 (the candidates' Started lines)"),
      ("567", "ZOM-567", "server - not live", "part of the server-side fix is not on prod yet", 5, "multi-source",
       ["OE 23", "OE 24", "OE 33"], "F9 F29 F30", "T2 H1", [s_doug36, s_cut],
       "the backend code is deployed but Arthur found the chest rows load it needs has not been run on prod", HOW_NOT_LIVE,
       f"Arthur Blake's review comment harmonygames-Games/match3d-backend#36#rc_1 ('{has(RC1, 'the new grant path does nothing on prod yet')}'); "
       f"Douglas's DM D079SNE2TL4/1759269712.483915 ('that's the code side')"),
      ("563", "ZOM-563", "server - live", "the server-side fix is fully on prod", 5, "multi-source", ["OE 23", "OE 33"],
       "F9 F28", "T7 CH5", [s_doug_deploy, s_doug_ok],
       "Douglas deployed the teams/social changes to prod and Vincent then confirmed it works there", HOW_LIVE,
       "Vincent's DM with Douglas D079SNE2TL4/1759256193.859279 and D079SNE2TL4/1759269524.769369"),
      ("473", "ZOM-473", "in candidate", "its fix was on main before the candidates were cut", 3, "comparison",
       ["OE 25", "OE 33"], "F9 F14 F31 F32", "T3b", [s_lin("ZOM-473", "completed_at"), s_b1974, s_b50, s_b135],
       "the ticket was closed 2025-09-22T15:11:51Z, eight days before both Started lines, and the only #builds change that "
       "may be its fix ('Adding input blocker during Level-end animations', Match3D Android #1974 on main, 2025-09-24) also "
       "landed before them, so its fix is in the candidates either way, even though Brian's re-test still shows the bug",
       HOW_IN,
       "ZOM-473 (Done 2025-09-22T15:11:51Z); #builds C05433XK267/1758755609.200489 (Match3D Android #1974 - main, 2025-09-24 "
       "23:13:29 UTC, Changes 'Adding input blocker during Level-end animations'); C05433XK267/1759257812.041449 and "
       "C05433XK267/1759257934.076209 (Started 2025-09-30 18:43:32 and 18:45:34 UTC)"),
      ("477", "ZOM-477", "n/a", "it is a no-call ticket", 3, "limited reconciliation", ["OE 7", "OE 12", "OE 33"], "F9 F16 F17", "H2",
       [s_lin("ZOM-477"), s_rules], "Leonard's ruling makes ZOM-477 no call, and the How we gate tab maps no-call tickets to "
       "build status n/a",
       HOW_NA, f"Leonard Hayes's ZOM-477 comment cmt_zom477_1 ('{c('cmt_zom477_1', 'No call for the store gates.')}')"),
      ("429", "ZOM-429", "in candidate", "QA re-tested it on the candidates and could not reproduce it", 3, "interpretation",
       ["OE 16", "OE 33"], "F9 F20", "H2", [s_lin("ZOM-429"), s_rules],
       "the ticket is open, but Vincent's re-test on #135 and #50 could not reproduce it, the How we gate tab's QA-confirmed "
       "branch of in candidate", HOW_QA,
       f"ZOM-429 comment cmt_zom429_1 (Vincent Parker, 2025-09-30T20:48:00Z: '{c('cmt_zom429_1', 'Couldn' + chr(39) + 't reproduce on #135 or #50')}')")]
for tag, key, val, meaning, w, kind, oe, fids, dec, srcs, reason, howq, records in BS:
    row(tag=f"bs_{tag}", t=f"The Agent records the build status {val} for {key} in {TAB} (or wording that {meaning})", w=w,
        kind=kind, why=reason, fact=f"{key}.build_status", span=SPAN_TAB, oe=oe, fids=fids, vals=f"`{key}` `{val}`",
        verify=f"{key} build status", final=f"{key}'s build status cell on the new tab", acc=[val, meaning],
        alt=f"Another How we gate value for {key}, or an empty build status, fails.", srcs=srcs,
        just=f"{kind.capitalize()}: {reason}.",
        ev=f"Sources: {records}; How we gate tab of f_0ebfccf33076f9dbf086bc ({val} = '{howq}'). Accept: {key}'s build "
           f"status cell reads {val}, or says that {meaning}.",
        dist="T-ID " + dec.split()[0] if dec.split()[0].startswith("T") else "none", amb="none", dec=dec,
        grp="G2 sample (build status)", valid=f"{key} | ... | {val} | ...", idle=f"No register, so no {key} build status")

row(tag="title_546", t=f"The Agent records ZOM-546's Linear title, 'Bug: refill algorithm spawns fewer items over time' "
    f"(the 'Bug:' prefix optional), in ZOM-546's title cell of {TAB}", w=1, kind="lookup", why="direct: the ticket's own Linear title",
    fact="ZOM-546.title", span=SPAN_TAB, oe=["OE 10", "OE 33"], fids="F13", vals="`ZOM-546` `Bug: refill algorithm spawns fewer items over time`",
    verify="ZOM-546 title", final="ZOM-546's title cell", acc=["Bug: refill algorithm spawns fewer items over time", "the same title without the 'Bug:' prefix or in another letter case"],
    alt="A paraphrase that changes the title's meaning, or an empty title cell, fails.", srcs=[s_lin("ZOM-546")],
    just="Lookup: the How we gate columns include title, and ZOM-546's Linear title is 'Bug: refill algorithm spawns fewer "
         "items over time'.",
    ev="Sources: Linear ZOM-546 (title 'Bug: refill algorithm spawns fewer items over time'); How we gate tab of "
       "f_0ebfccf33076f9dbf086bc (columns ticket, title, build status, QA result, call, evidence). Accept: that title in "
       "ZOM-546's title cell, with or without the 'Bug:' prefix.",
    dist="none", amb="none", dec="H2", grp="G5 sample (title, ordinary)", valid="ZOM-546 | Bug: refill algorithm spawns fewer items over time | ...",
    idle="No register, so no ZOM-546 title")

row(tag="qa_449", t=f"The Agent records in ZOM-449's QA result cell of {TAB} that its latest check on Android #135 "
    f"still fails (reproduced)", w=1, kind="lookup", why="direct: the latest comment on the ticket",
    fact="ZOM-449.qa_result", span=SPAN_TAB, oe=["OE 14", "OE 33"], fids="F18", vals="`ZOM-449` `level 3`",
    verify="ZOM-449 QA result", final="ZOM-449's QA result cell", acc=["repro on #135: cold start into level 3 froze", "FAIL: reproduced on #135"],
    alt="A pass, 'could not reproduce', 'not re-tested' or an empty QA result fails.", srcs=[s_lin("ZOM-449", "description")],
    just="Lookup: the QA result is the result of the ticket's latest check, Brian's Sep 30 comment on Android #135.",
    ev=f"Sources: ZOM-449 comment cmt_zom449_2 (Brian Foster, 2025-09-30T22:20:00Z: '{c('cmt_zom449_2', 'cold start into level 3 froze again, taps did nothing until I force-quit.')}'). "
       f"Accept: a QA result that the latest check on Android #135 reproduced the bug or failed, in any wording, with or "
       f"without the level 3 freeze detail.",
    dist="none", amb="none", dec="H2", grp="G3 sample (QA result, ordinary)", valid="ZOM-449 | ... | repro on #135: level 3 cold start froze | ...",
    idle="No register, so no QA result")
row(tag="qa_559", t=f"The Agent records in ZOM-559's QA result cell of {TAB} that its latest check failed (the "
    f"victory screen froze on Android Submission #133) or that it is not yet re-tested on Android #135 / iOS #50", w=3, kind="comparison",
    why="the Sep 29 Samsung check must be told apart from the older Sep 22 Pixel note and the Sep 22 tab's 'not reproduced'",
    fact="ZOM-559.qa_result", span=SPAN_TAB, oe=["OE 7", "OE 14", "OE 33"], fids="F10 F18", vals="`ZOM-559` `victory screen`",
    verify="ZOM-559 QA result", final="ZOM-559's QA result cell", acc=["victory screen froze (Samsung S22, #133)", "not re-tested on #135 / #50 (last check on #133 failed)"],
    alt="Copying the Sep 22 tab's 'not reproduced on #127 (Pixel)' or Vincent's Sep 22 'Can't reproduce here' fails.",
    srcs=[s_lin("ZOM-559", "description"), s_rules],
    just="Comparison: three checks exist; Brian's 2025-09-29 comment is newer than Vincent's 2025-09-22 Pixel note and the "
         "Sep 22 tab, so it is the latest result.",
    ev=f"Sources: ZOM-559 comments cmt_zom559_1 (Brian Foster, 2025-09-29T15:20:00Z: '{c('cmt_zom559_1', 'the victory screen froze with the reward panel half drawn')}') "
       f"and cmt_zom559_0 (Vincent Parker, 2025-09-22T16:30:00Z, older: '{c('cmt_zom559_0', 'Can' + chr(39) + 't reproduce here')}'); the Sep 22 tab "
       f"of f_0ebfccf33076f9dbf086bc ('not reproduced on #127 (Pixel)'). Accept: a QA result that the latest check failed "
       f"(froze), or that the ticket has no check on #135 / #50 yet; 'not reproduced', a pass or an empty cell fails.",
    dist="T12 (the Sep 22 tab)", amb="none", dec="T12 H2", grp="G3 sample (QA result, edge)",
    valid="ZOM-559 | ... | #133 S22: victory screen froze, force-quit | ...", idle="No register, so no QA result")

row(tag="ev_435", t=f"The Agent puts an id or link of the Trello card Fix TECH ISSUES (68d1eb90bef538c7c5c5599d, link "
    f"trello.com/c/pTbZYXdb) or of Leonard Hayes's Sep 30 comment on it (68dc63484a5b2d0a869e758f) in ZOM-435's evidence "
    f"cell of {TAB}", w=5, kind="multi-source",
    why="the deciding record is a Trello comment off the Linear and Slack path, found only through ZOM-570's tech-issues card",
    fact="ZOM-435.evidence", span=SPAN_TAB, oe=["OE 8", "OE 33"], fids="F9 F11", vals="`ZOM-435` `68dc63484a5b2d0a869e758f`",
    verify="ZOM-435 evidence", final="ZOM-435's evidence cell", acc=["comment id 68dc63484a5b2d0a869e758f", "card id 68d1eb90bef538c7c5c5599d", "a link to the card (pTbZYXdb)"],
    alt="Citing only ZOM-435, Vincent's #133 post C08R27X0EAH/1759140300.935009, or the card by name with no id or link, "
        "fails.", srcs=[s_card],
    just="Multi-source: the How we gate evidence column holds the 'id or link of the record that decides the row', and "
         "ZOM-435's call is decided by Leonard's #135 re-test on the Trello card, not by the Done ticket or Vincent's #133 post.",
    ev=f"Sources: Trello comment 68dc63484a5b2d0a869e758f on card 68d1eb90bef538c7c5c5599d 'Fix TECH ISSUES' (Leonard Hayes, "
       f"2025-09-30T23:10:00Z); How we gate tab of f_0ebfccf33076f9dbf086bc (evidence = '{EVID_DEF}'). Accept: ZOM-435's "
       f"evidence cell holds the comment id 68dc63484a5b2d0a869e758f, the card id 68d1eb90bef538c7c5c5599d or a link to "
       f"the card (short link pTbZYXdb), alone or beside other records.",
    dist="T3 (Vincent's #133 post)", amb="none", dec="T3 CH2", grp="G4 sample (evidence, edge)",
    valid="ZOM-435 | ... | Trello Fix TECH ISSUES comment 68dc63484a5b2d0a869e758f", idle="No register, so no evidence cell")
row(tag="ev_563", t=f"The Agent puts an id or link of Vincent's Sep 30 DM with Douglas that settles ZOM-563 (channel "
    f"D079SNE2TL4, Douglas's prod update ts 1759256193.859279 or Vincent's confirmation ts 1759269524.769369) in ZOM-563's "
    f"evidence cell of {TAB}", w=5, kind="multi-source",
    why="the deciding record is a DM outside Linear that overrides the ticket's In Progress state",
    fact="ZOM-563.evidence", span=SPAN_TAB, oe=["OE 23", "OE 33"], fids="F9 F28", vals="`ZOM-563` `1759269524.769369`",
    verify="ZOM-563 evidence", final="ZOM-563's evidence cell",
    acc=["D079SNE2TL4 with ts 1759269524.769369", "D079SNE2TL4 with ts 1759256193.859279", "a Slack link to either message"],
    alt="Citing only ZOM-563, or the DM by description with no channel id, ts or link, fails.", srcs=[s_doug_deploy, s_doug_ok],
    just="Multi-source: ZOM-563's FIXED call is decided by Douglas's prod update and Vincent's confirmation in their DM, not by "
         "the ticket, and the How we gate evidence column holds the 'id or link of the record that decides the row'.",
    ev=f"Sources: Vincent's DM with Douglas, D079SNE2TL4/1759256193.859279 ('Ok, I updated the prod environment with the latest "
       f"teams/social changes') and D079SNE2TL4/1759269524.769369 ('Yep it works as expected'); How we gate tab of "
       f"f_0ebfccf33076f9dbf086bc (evidence = '{EVID_DEF}'). Accept: ZOM-563's evidence cell holds the channel D079SNE2TL4 "
       f"with either ts, or a Slack link to either message (p1759256193859279 or p1759269524769369), alone or beside other "
       f"records.",
    dist="T7 (ZOM-563 In Progress)", amb="none", dec="T7 CH5", grp="G4 sample (evidence, edge)",
    valid="ZOM-563 | ... | Slack DM D079SNE2TL4 1759269524.769369", idle="No register, so no evidence cell")

# =====================================================================================================================
# Release ticket ZOM-570 description: the blocker list, graded in full
# =====================================================================================================================
row(tag="z_keep", t="The Agent adds its blocker list to the description of the release ticket ZOM-570 while keeping Arthur "
    "Blake's existing description text in it, from 'Store push for ZM.' through 'Other push notes go in the comments here.'",
    w=1, kind="lookup", why="direct: the prompt asks to add to the description, and the description's text is on the ticket",
    fact="zom570.arthur_text", span=SPAN_BLOCK, oe=["OE 2", "OE 34"], fids="F2", vals="`Store push for ZM.`",
    verify="ZOM-570 description kept", final="ZOM-570 description after the update",
    acc=["Arthur's text with the blocker list appended, prepended or inserted"],
    alt="Replacing the description with only the blocker list fails; the list's position and layout are free.",
    srcs=[s_thread],
    just="Lookup: the prompt says 'add the blockers to the release ticket's description', so Arthur's description stays "
         "and the list is added to it.",
    ev=f"Sources: Linear ZOM-570 description by Arthur Blake (2025-09-30T20:20:00Z), from 'Store push for ZM.' through "
       f"'{has(Z570, 'Other push notes go in the comments here.')}'; Arthur's post C08R27X0EAH/1759263900.484190 ('details "
       f"on ZOM-570'). Accept: after the update, ZOM-570's description holds Arthur's text and the added blocker list.",
    dist="none", amb="none", dec="H2", grp="none", valid="Arthur's text, then a '## QA gate blockers' list",
    idle="No description update, so no blocker list is added")
row(tag="z_only", t="The Agent writes its blocker list into the description of the release ticket ZOM-570 and into no "
    "other Linear issue's description", w=1, kind="lookup", why="direct: the prompt names the release ticket's description",
    fact="zom570.target", span=SPAN_BLOCK, oe=["OE 2", "OE 34"], fids="F2", vals="`ZOM-570`",
    verify="Blocker list write target", final="Linear description updates in the run",
    acc=["the blocker list in ZOM-570's description only"],
    alt="Also writing the blocker list into another ticket's description (an earlier release ticket, a blocker ticket) fails.",
    srcs=[s_thread],
    just="Lookup: the prompt says 'add the blockers to the release ticket's description' and ZOM-570 says 'Blockers go on "
         "this ticket by key'.",
    ev=f"Sources: Arthur Blake's ZOM-570 description ('{BY_KEY}'); Arthur's post C08R27X0EAH/1759263900.484190 ('details on "
       f"ZOM-570'). Accept: the blocker list is written into ZOM-570's description, and no other issue's description gets a "
       f"blocker list.",
    dist="none", amb="none", dec="H2", grp="none", valid="One description update, on ZOM-570",
    idle="No description update, so no blocker list is written")
row(tag="z_count", t="The Agent lists exactly 19 tickets as blockers in the description of the release ticket ZOM-570",
    w=5, kind="multi-source", why="the count follows only from the full gate across Linear, Slack, Gmail, GitHub, Trello, "
    "#builds and the runbook, plus the one new ticket",
    fact="zom570.blocker_count", span=SPAN_BLOCK, oe=["OE 33", "OE 34"], fids="F38 F39", vals="`19`",
    verify="Blocker count on ZOM-570", final="ZOM-570 description", acc=["19 tickets listed as blockers"],
    alt="A list that adds known issues, misses blockers or adds duplicate tickets gives another count and fails.",
    srcs=[s_rules, s_card],
    just="Multi-source: the BLOCKER calls of the full register (18 existing tickets plus the new update-path ticket) are "
         "the list Arthur asks for 'by key, the existing ticket if there is one'.",
    ev=f"Sources: Arthur Blake's ZOM-570 description ('{BY_KEY}'); Arthur's comment 68dc3ef455344e471b1d2ea9 on the Trello "
       f"card Fix TECH ISSUES ('{REUSE}'); Leonard's doc f_632c44650df44fe252ee59 ('{BLOCKER_RULE}'). Accept: exactly 19 "
       f"distinct tickets listed as blockers in ZOM-570's description.",
    dist="T9-T13", amb="none", dec="H2", grp="volume row for the blocker list", valid="19 keys listed under 'QA gate blockers'",
    idle="No description update")
for tag, key, w, kind, oe, fids, dec, srcs, reason, records in BLK:
    row(tag=f"z_{tag}", t=f"The Agent lists {key} as a blocker in the description of the release ticket ZOM-570", w=w,
        kind=kind, why=reason, fact=f"{key}.call", span=SPAN_BLOCK, oe=[o for o in oe if o != "OE 33"] + ["OE 34"], fids=fids + " F39",
        vals=f"`{key}`", verify=f"{key} on ZOM-570", final="ZOM-570 description", acc=[f"{key} listed as a blocker"],
        alt=f"Leaving {key} off the list, or listing it under another heading (known issues, fixed), fails.", srcs=srcs + [s_thread],
        just=f"{kind.capitalize()}: {reason}.",
        ev=f"Sources: {records}; Leonard's doc f_632c44650df44fe252ee59 (\"{CLAUSE[key]}\"); Arthur Blake's ZOM-570 "
           f"description ('{BY_KEY}'). Accept: {key} is listed as a blocker in ZOM-570's description.",
        dist="T-ID " + dec.split()[0] if dec.split()[0].startswith("T") else "none", amb="none", dec=dec,
        grp="blocker list, graded in full (19)", valid=f"- {key}: ...", idle="No description update")
row(tag="z_new", t=f"The Agent lists {NEWT}, by its new ZOM key, as a blocker in the description of the release ticket "
    f"ZOM-570", w=5, kind="multi-source",
    why="the ticket exists only after the runbook check, Brian's update-path doc and the existing-ticket search",
    fact="newticket.call", span=SPAN_BLOCK, oe=["OE 26", "OE 28", "OE 29", "OE 31", "OE 34"], fids="F33 F35 F36 F39 F40",
    vals="`BLOCKER`", verify="New ticket on ZOM-570", final="ZOM-570 description", acc=["the new ZOM key listed as a blocker"],
    alt="Listing the failure without the new key, or leaving it off, fails.", srcs=new_srcs + [s_thread],
    just="Multi-source: the update-path failure is a blocker under the runbook and Leonard's rules, and Arthur wants "
         "blockers on ZOM-570 by key, so the new ticket goes on the list by its new key.",
    ev=f"Sources: {new_records}; Arthur Blake's ZOM-570 description ('{BY_KEY}'). Accept: the new update-path ticket's ZOM "
       f"key is listed as a blocker in ZOM-570's description.",
    dist="T4, T10", amb="none", dec="T4 CH3 H2", grp="blocker list, graded in full (19)", valid="- ZOM-581: iOS N-1 update "
    "resets the save", idle="No new ticket and no description update")

# =====================================================================================================================
# The new ticket
# =====================================================================================================================
row(tag="new_issue", t="The Agent files a new Linear issue in the ZOM (Zombie Match 3D) team for the save reset found on the "
    "runbook's update path: updating from the N-1 App Store build to iOS Submission #50 (TestFlight 50) brings the save "
    "back at level 1", w=5, kind="multi-source",
    why="the failure is found only by reading the runbook's update rule, seeing that Brian's 'green' matrix has empty "
        "update columns, opening his update-path doc and checking Linear for an existing ticket",
    fact="updatepath.bug", span=SPAN_FILE, oe=["OE 26", "OE 27", "OE 28", "OE 29", "OE 31"], fids="F33 F34 F35 F36 F40",
    vals="`N-1` `iOS Submission #50` `level 1`", verify="New ticket", final="New ZOM issue",
    acc=["a new ZOM issue whose title or description says the N-1 to iOS #50 update resets the save to level 1"],
    alt="No new ticket (trusting Brian's 'regression matrix green'), reusing ZOM-424 (a different July update bug), or "
        "filing in another team fails.", srcs=[s_update, s_runbook],
    just="Multi-source: the runbook makes both update rows mandatory, Brian's matrix leaves them empty, his update-path doc "
         "records the iOS N-1 to #50 FAIL, and no Linear ticket covers it (ZOM-424 is a different bug), so it needs a new "
         "ticket.",
    ev=f"Sources: QA Regression Runbook page_qa_runbook ('{has(RUN_T, 'Both update rows are mandatory - N-1 and N-2 are the last two shipped store versions.')}'); "
       f"Brian Foster's matrix f_b91db376f65604b8602657 (update columns empty); his doc f_5e40215b7d4d24b0455412 "
       f"('{has(UPD_T, 'iPhone 13 | iOS 18.6 | N-1 | iOS Submission #50 | FAIL')}'); ZOM-424 'Updating the game from earlier "
       f"build breaks the core game.' (Done 2025-07-23, a different bug). Accept: a new issue in team ZOM describing that "
       f"update and the save coming back at level 1.",
    dist="T4, T10, T16 (ZOM-424)", amb="none", dec="T4 CH3 T10", grp="none",
    valid="ZOM-581 'iOS: updating from the N-1 store build to iOS Submission #50 resets the save to level 1'",
    idle="No Linear issue created")
for tag, val, quote, why in [("device", "the device iPhone 13", "iPhone 13", "device"),
                             ("os", "the OS version iOS 18.6", "iOS 18.6", "OS version")]:
    row(tag=f"new_{tag}", t=f"The Agent names {val} in its new update-path save-reset issue in Linear", w=1, kind="lookup",
        why=f"direct: the {why} on the failing row of Brian's update-path doc", fact=f"updatepath.{tag}", span=SPAN_FILE,
        oe=["OE 26", "OE 28", "OE 31"], fids="F33 F35 F40", vals=f"`{quote}`", verify=f"New ticket {why}",
        final="New issue title, description or the Agent's comment on it", acc=[quote], alt=f"Another {why}, or none, fails.", srcs=[s_update, s_runbook],
        just=f"Lookup: the runbook says 'File the bug with device, OS version, source build and repro steps', and the failing "
             f"row names {quote}.",
        ev=f"Sources: QA Regression Runbook page_qa_runbook ('{has(RUN_T, 'File the bug with device, OS version, source build and repro steps')}'); "
           f"Brian Foster's doc f_5e40215b7d4d24b0455412 ('{has(UPD_T, 'iPhone 13 | iOS 18.6 | N-1 | iOS Submission #50 | FAIL')}'). "
           f"Accept: {quote} recorded as the affected {why} in the new issue's title, description or a comment the Agent "
           f"adds on it.",
        dist="none", amb="none", dec="T4 CH3", grp="none", valid=f"'Device / OS: iPhone 13, iOS 18.6'", idle="No Linear issue created")
row(tag="new_repro", t="The Agent gives repro steps in its new update-path save-reset issue in Linear that install the N-1 "
    "build from the App Store, play past level 200, install TestFlight 50 (iOS Submission #50) over it and launch the game",
    w=1,
    kind="lookup", why="direct: the repro line of Brian's update-path doc", fact="updatepath.repro", span=SPAN_FILE,
    oe=["OE 26", "OE 28", "OE 31"], fids="F33 F35 F40", vals="`play past level 200` `TestFlight 50`", verify="New ticket repro",
    final="New issue description", acc=["the four steps in any wording, numbered or in one sentence"],
    alt="No repro, or steps that skip the N-1 install, the progress past level 200, the update over it or the launch, fail.", srcs=[s_update, s_runbook],
    just="Lookup: the runbook asks for repro steps when a check fails, and Brian's doc gives them.",
    ev=f"Sources: Brian Foster's doc f_5e40215b7d4d24b0455412 ('{has(UPD_T, 'install the N-1 build from the App Store, play past level 200, install TestFlight 50 over it, launch.')}'); "
       f"QA Regression Runbook page_qa_runbook ('File the bug with device, OS version, source build and repro steps'). "
       f"Accept: those four steps in the new issue's title, description or a comment the Agent adds on it, in any wording, "
       f"numbered or in one sentence.",
    dist="none", amb="none", dec="T4 CH3", grp="none", valid="'Repro: 1. Install N-1 from the App Store 2. Play past level 200 "
    "3. Install TestFlight 50 over it 4. Launch'", idle="No Linear issue created")
row(tag="new_one", t="The Agent creates exactly one new Linear issue while running the gate", w=5, kind="multi-source",
    why="every other failure the gate finds must be matched to its existing ticket under Arthur's reuse rule",
    fact="linear.new_issue_count", span=SPAN_FILE, oe=["OE 8", "OE 29", "OE 31"], fids="F11 F36", vals="`1`",
    verify="Number of new issues", final="linear issues created in the run", acc=["one new issue"],
    alt="A second ticket for an already-filed problem (the TestFlight boss-fight report that is ZOM-562, Leonard's trophy "
        "path re-test that is ZOM-435) fails.", srcs=[s_card, s_update],
    just="Multi-source: every failure the gate finds (Linear comments, Slack DMs, the vendor mail, Leonard's Trello "
         "re-test, the runbook's update rows) is matched to the existing tickets under Arthur's reuse rule; only the iOS N-1 "
         "to Submission #50 save reset has no ticket, so exactly one issue is new.",
    ev=f"Sources: Arthur Blake's comment 68dc3ef455344e471b1d2ea9 on the Trello card Fix TECH ISSUES 68d1eb90bef538c7c5c5599d "
       f"('{REUSE}'); the prompt's 'nobody has filed yet'. Accept: exactly one issue created.",
    dist="T5, T3", amb="none", dec="T5 T3 H2", grp="none", valid="One create: the update-path ticket", idle="No issue created")

# =====================================================================================================================
# The QA call in Arthur's thread
# =====================================================================================================================
row(tag="s_thread", t="The Agent posts its QA call in Slack only as a reply in Arthur Blake's candidates thread in "
    "#zombie-bugs (thread ts 1759263900.484190); a thread reply also sent to the channel passes", w=1, kind="lookup",
    why="direct: the prompt names the thread and Leonard's note on ZOM-570 asks for a reply, not a new post",
    fact="signoff.thread", span=SPAN_REPLY, oe=["OE 1", "OE 3", "OE 35"], fids="F1 F3 F41", vals="`1759263900.484190`",
    verify="Reply destination", final="Message with thread_ts 1759263900.484190 in C08R27X0EAH",
    acc=["a reply in that thread", "a thread reply also sent to the channel"],
    alt="A top-level post in #zombie-bugs, a DM to Arthur or a reply under another post fails.", srcs=[s_thread],
    just="Lookup: the prompt says 'Reply in Arthur's candidates thread in #zombie-bugs', and Leonard's ZOM-570 comment asks "
         "for the sign-off 'as a reply on Arthur's candidate thread ... not a new post'.",
    ev="Sources: Arthur Blake's post C08R27X0EAH/1759263900.484190 ('ZM store candidates are up: Android Submission #135 and "
       "iOS Submission #50'); Leonard Hayes's ZOM-570 comment cmt_zom570_1 ('sign-off as a reply on Arthur's candidate "
       "thread in #zombie-bugs please, not a new post'). Accept: every Slack message carrying the QA call is a reply in "
       "that thread (one or more replies; also sent to the channel is fine); a top-level Slack post or a reply in another "
       "thread fails. The Agent's final chat answer to Vincent is not a Slack post and is not graded here.",
    dist="none", amb="none", dec="H2", grp="none", valid="Reply with thread_ts 1759263900.484190", idle="No message posted")
s_gcal = S_sql("gcal", "evt_81e6dc4dbfd331f1a6a317", "gcal.gcal_events",
               {"event_id": "evt_81e6dc4dbfd331f1a6a317", "calendar_id": "vincent.parker@harmonygames.co"}, "start_ts",
               "created", [THREAD, ("gcal", "evt_81e6dc4dbfd331f1a6a317")],
               "Arthur's post asks for the QA gate 'before friday's go/no-go'; the invite is on Vincent's own calendar.",
               semantics="scheduled_event", mutable=True,
               rev=review(["evt_81e6dc4dbfd331f1a6a317", THREAD[1]], SNAP + "Created 2025-09-30T20:22:00Z; the meeting itself "
                          "is a future scheduled event at the clock."))
assert s_gcal["source_value"] == "2025-10-03T16:00:00Z"
row(tag="s_time", t="The Agent posts its reply with the QA call in Arthur Blake's candidates thread in #zombie-bugs before the "
    "go/no-go on Friday, October 3, 2025 at 9:00 AM PDT (16:00 UTC)",
    w=1, kind="lookup", why="direct: the meeting time on Vincent's calendar", fact="signoff.timing", span=SPAN_REPLY,
    oe=["OE 30", "OE 35"], fids="F37", vals="`2025-10-03T16:00:00Z`", verify="Reply timing",
    final="Send time of the thread reply", acc=["any reply sent before 2025-10-03T16:00:00Z"],
    alt="A reply scheduled or sent after the go/no-go starts fails.", srcs=[s_gcal],
    dates={"instant_utc": "2025-10-03T16:00:00Z", "pacific": "2025-10-03", "utc": "2025-10-03",
           "accepted_dates": ["2025-10-03"], "prompt_timezone": None},
    just="Lookup: the prompt says 'before Friday's go/no-go', and Vincent's calendar has 'ZM store push - go/no-go' on Fri Oct "
         "3, 2025 at 16:00 UTC (9:00 AM PDT).",
    ev="Sources: calendar event evt_81e6dc4dbfd331f1a6a317 'ZM store push - go/no-go' (start 2025-10-03T16:00:00Z, organizer "
       "arthur.blake@harmonygames.co, 'Go/no-go for the ZM store push (ZOM-570).'). Accept: the QA call reply in thread "
       "C08R27X0EAH/1759263900.484190 is sent before 2025-10-03T16:00:00Z (9:00 AM PDT); the Pacific and UTC dates are the "
       "same day.",
    dist="none", amb="none", dec="H2", grp="none", valid="Reply sent during the run on Oct 1", idle="No reply posted")
assert has(CMT["cmt_zom570_1"]["body"], "sign-off as a reply on Arthur's candidate thread in #zombie-bugs please, not a new post")
row(tag="s_call", t="The Agent states in its reply in Arthur Blake's candidates thread in #zombie-bugs that the QA call on "
    "Android Submission #135 and iOS Submission #50 is no-go (the candidates are not ready to ship)", w=3,
    kind="interpretation", why="the call follows from the blockers the gate finds",
    fact="signoff.call", span=SPAN_REPLY, oe=["OE 33", "OE 34", "OE 35"], fids="F33 F39", vals="`no-go`",
    verify="QA call", final="Thread reply text", acc=["NO-GO", "not ready to ship", "blocked until the blockers are fixed"],
    alt="A go, a conditional go on the current builds, or a reply with no call fails.", srcs=[s_runbook, s_rules],
    just="Interpretation: open blockers on the candidates (including the update-path save reset, which the runbook says "
         "blocks the release) mean the QA call is no-go.",
    ev=f"Sources: QA Regression Runbook page_qa_runbook ('A failure in any UPDATE column blocks the release - fresh-install-only "
       f"regressions do not pass the gate.'); Leonard's doc f_632c44650df44fe252ee59 ('{BLOCKER_RULE}'); open blockers "
       f"ZOM-546 (cmt_zom546_1) and ZOM-560 (cmt_zom560_1). Accept: the reply calls the candidates no-go, in any wording "
       f"that they are not ready to ship.",
    dist="T10 (Brian's 'regression matrix green')", amb="none", dec="T10 CH3 H2", grp="none",
    valid="'QA call on Android #135 / iOS #50: NO-GO. 19 blockers on ZOM-570.'", idle="No reply posted")
assert has(RUN_T, "A failure in any UPDATE column blocks the release - fresh-install-only regressions do not pass the gate.")

# =====================================================================================================================
# Outputs
# =====================================================================================================================
GRP = {"fix_429": "G1 sample (edge: open in Linear, QA could not reproduce)", "fix_434": "G1 sample (ordinary fixed)",
       "fix_558": "G1 direct exception (Leonard's per-ticket ruling)", "fix_563": "G1 sample (edge: server-side fix "
       "confirmed on prod while In Progress)", "smp_477": "G1 direct exception (Leonard's per-ticket ruling)",
       "bs_569": "G2 direct exception (fix after the Started lines)", "bs_567": "G2 direct exception (server fix not live)",
       "bs_563": "G2 direct exception (server fix live)", "bs_473": "G2 sample (edge: Done, re-test fails)",
       "bs_429": "G2 sample (edge: open, QA could not reproduce)", "bs_477": "G2 sample (ordinary n/a)"}
for r in R:
    r["grp"] = GRP.get(r["tag"], r["grp"])
rubric = [{"title": r["t"], "category": r["cat"], "weight": r["w"], "justification": r["just"], "evidence": r["ev"]} for r in R]
text = json.dumps(rubric, indent=1, ensure_ascii=False) + "\n"
bad = [m.group(0) for m in re.finditer(r"[\u2013\u2014]|\.sql|SQL|Working_Files|task_inputs|data\.json|/issues/|\.md\b|"
                                       r"solver|truth\.json|Universe_|Task_Authoring", text)]
assert not bad, f"forbidden text in the rubric JSON: {sorted(set(bad))}"
(TI / "09_Rubrics.json").write_text(text)


def ahash(p):
    return subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/stage_gate.py"), "--artifact-hash", str(p)],
                          capture_output=True, text=True, cwd=WS).stdout.strip()


ev_path = TI / "Working_Files/00_V3_Authoring_Evidence.json"
ev = json.loads(ev_path.read_text())
ev["rubric_hash"] = ahash(TI / "09_Rubrics.json")
ev["prompt_hash"] = ahash(TI / "04_Prompt.txt")
ev["rubric_rows"] = [dict({"criterion_id": f"C{i + 1}", "fact_id": r["fact"], "prompt_span": r["span"],
                           "accepted_outcomes": r["acc"], "alternatives_review": r["alt"], "source_records": r["srcs"]},
                          **({"dates": r["dates"]} if r.get("dates") else {}))
                     for i, r in enumerate(R)]
ev_path.write_text(json.dumps(ev, indent=1, ensure_ascii=False) + "\n")
json.dump([{k: v for k, v in r.items() if k != "srcs"} for r in R], open(Path(__file__).with_name("rows.json"), "w"),
          indent=1, ensure_ascii=False)
from collections import Counter
fc = Counter(r["fact"] for r in R)
assert max(fc.values()) <= 2, [k for k, v in fc.items() if v > 2]
print(len(R), "rows; weight", sum(r["w"] for r in R), "; bands", Counter(r["w"] for r in R), "; rubric_hash", ev["rubric_hash"])

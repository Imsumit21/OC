#!/usr/bin/env python3
"""Apply the /rubric round-1 Fix List (platform_reports/rubric_r1_FAIL.md, reviewed JSON afbc830d0cbb) to the reviewed rows.
Unchanged rows keep title, weight, justification and evidence byte for byte (lock = reviewed row number). Writes plan/rubric_final.json:
one dict per criterion with its plan fields, criterion text and V3 source keys."""
import copy, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import reports as RP
src = open(os.path.join(HERE, "out", "rubric_rows.draft1.py")).read()
g = {"__file__": os.path.join(HERE, "rubric_rows.py"), "__name__": "draft1"}
exec(compile(src, "rubric_rows.draft1.py", "exec"), g)
D1 = g["R"]; F = g["F"]; E = g["E"]; Es = g["Es"]; work = g["work"]; T = g["T"]; tr = g["tr"]
NOTE, SHEET, DEC, TIX, DMS, ALIAS, CARD, INV, FOLD, HUB = g["NOTE"], g["SHEET"], g["DEC"], g["TIX"], g["DMS"], g["ALIAS"], g["CARD"], g["INV"], g["FOLD"], g["HUB"]
S_LIN, S_SHEET, S_SLIDE = g["S_LIN"], g["S_SHEET"], g["S_SLIDE"]
REV = json.load(open(os.path.join(HERE, "out", "09_Rubrics.draft1_afbc830d0cbb.json")))
assert len(D1) == len(REV) == 121 and all(D1[i]["band"] == REV[i]["weight"] for i in range(121))
SEED = json.load(open(os.path.join(HERE, "seed_text.json"))); ID = {k: v["id"] for k, v in SEED.items()}
FL = open(os.path.join(WF, "platform_reports", "rubric_r1_FAIL.md")).read()
FL = FL[FL.index("## Fix List"):FL.index("### Phase 1: Structural Validation")]
TITLES = [m.group(1).strip() for m in re.finditer(r"(The Agent [^\n]+)", FL)]
def ft(start, must=None):
    c = [t for t in TITLES if t.startswith(start) and (must is None or must in t)]
    assert len(c) == 1, (start, must, len(c)); return re.sub(r"\s+\(template/volume row for R69 and R70\)$", "", c[0])
NOTE_SRC = f"Brian's note {ID['epic_note']} on ZOM-543"
def acc(t): return t[len("The Agent "):]
def keys_for(n):
    r = T[n]; t = r["trap"]
    if t == "BRANCH": return ["NOTE", "RULE", "B1718", "PR465"]
    if t == "INLINE": return ["NOTE", "INLINE2" if n == 32 else "INLINE"]
    if t == "ELSE": return ["NOTE", "ELSE", "PR473"]
    if t == "BODY": return ["NOTE", "PR472"]
    if t in ("REOPEN", "BACK"): return ["NOTE", "RULE", {9: "REOPEN", 29: "BACK", 17: "REOPEN2", 24: "BACK2"}[n], "B135"]
    if t == "FILT": return ["NOTE", "GLOW"]
    if n == 27: return ["NOTE", "RULE", "OLDER", "B2006", "B1745"]
    if n == 18: return ["NOTE", "PR472", "B2013"]
    if n == 34: return ["NOTE", "PR475", "B1757"]
    if r["status"] == RP.P: return ["NOTE", "RULE", "SHEETF"]
    if n in (11, 20): return ["NOTE", "SHEETF", "ALIAS_GIFT" if n == 11 else "ALIAS_STREAK"]
    return ["NOTE", "SHEETF"]
def d1keys(r):
    """V3 source keys for a reviewed row, by its fact."""
    f = r["fact"]; k, _, a = f.partition(":")
    if k in ("state", "note", "sheet_status"):
        n = int(a); tk = tr(n)["Ticket"]; ks = keys_for(n)
        return ks + ([("K_" + tk) if tk not in ("ZOM-556", "ZOM-560") else ("Z556" if tk == "ZOM-556" else "Z560")] if k == "state" and tk else [])
    return {"child_state": ["NOTE"], "new_parent": ["NOTE"], "new_priority": ["NOTE"], "new_assignee": ["NOTE"], "move": ["NOTE"] + ({"11": ["ALIAS_GIFT", "Z556"], "20": ["ALIAS_STREAK", "Z560"]}.get(a, ["SHEETF"])), "sheet_folder": ["HUB", "FOLDER"], "sheet_cols_reports": ["NOTE"], "sheet_cols_areas": ["NOTE"],
            "sheet_rows": ["NOTE", "SHEETF", "GLOW"], "sheet_ticket": ["ALIAS_GIFT", "Z556"] if a == "11" else ["SHEETF"], "review_count_sheet": ["NOTE", "INVITE", "REOPEN2"], "sheet_review": ["NOTE", "INVITE"] + (["REOPEN2"] if a == "17" else []), "sheet_why": ["NOTE", "REOPEN"] if a == "9" else ["NOTE", "SHEETF"],
            "area_rows": ["NOTE"], "area_status": ["NOTE"] + (["BACK2"] if a == "Zombie Lane" else ["B1718", "RULE"]), "area_open_count": ["NOTE", "SHEETF"], "share": ["HUB", "EVT"], "slide_new": ["HUB", "DECK"], "dm_place": ["HUB"], "dm": ["HUB", "NOTE"], "slide": ["HUB", "NOTE"], "dm_after_writes": ["HUB"]}[k if k in ("dm", "slide", "share") or ":" in f else f]
OUT = []
def keep(i, title=None, weight=None, fact=None, just=None, **plan):
    """Reviewed row i (1-based), optionally retitled / reweighted per the Fix List."""
    r = copy.deepcopy(D1[i - 1]); rv = REV[i - 1]; r.update(plan)
    if fact: r["fact"] = fact
    changed = (title is not None and title != rv["title"]) or (weight is not None and weight != rv["weight"])
    r["band"] = weight if weight is not None else rv["weight"]
    r["title"] = title or rv["title"]
    r["just"] = just or rv["justification"]
    r["evidence"] = rv["evidence"] if not changed or title is None else re.sub(r"Accept: .*?\. Reject:", "Accept: " + acc(r["title"]) + ". Reject:", rv["evidence"], flags=re.S)
    r["lock"] = None if changed else i
    r.setdefault("srcs", d1keys(D1[i - 1])); r["was"] = i; OUT.append(r); return r
def new(title, weight, fact, span, oe, what, final, vals, kind, srcs, source, reject, grp="direct", dup=None, valid=None, idle=None, cr=None, dec="—", dis="—"):
    r = dict(span=span, oe=oe, fact=fact, what=what, final=final, vals=vals, cat="Outcome", phr="no — must not hard-code wording", dis=dis, amb="—", kind=kind, band=weight, dec=dec, grp=grp, dup=dup or f"{fact} ×1", af="none · not over-specific",
             valid=valid or final, idle=idle or "the write is missing → REJECT", reach="PROMPT_LINKED", cr=cr or "(a) a valid run could word it differently — any wording with that meaning passes; (b) a wrong run could skip this write or give another value",
             title=title, just=kind[0].upper() + kind[1:] + ".", evidence=f"Source: {source}. Accept: {acc(title)}. Reject: {reject}", lock=None, srcs=srcs, was=None)
    OUT.append(r); return r
CH = Es("Create the ")[:10]
# ---- item 1: R1 -> 10 creates, Boss Arena team / assignee, template row
for a in RP.AREAS:
    new(ft(f"The Agent creates a child issue of ZOM-543 (Queue Manager) for the {a} area"), 1, f"child_create:{a}", S_LIN, [HUB, NOTE, CH[RP.AREAS.index(a)]], f"the {a} child exists", f"a child issue of ZOM-543 titled with the area name {a}", f"the {a} child of `ZOM-543` (note: 'Children: … One child each') · " + F("note", "epic"),
        "lookup: one area named in Brian's note", ["HUB", "NOTE"], NOTE_SRC + " ('Children: Tutorials, Level-end rewards, Daily Gift, Season Pass, Collect & Win, Win Streak, Zombie Lane, Boss Arena, Endless Mode, Card packs. One child each, same team, no assignee.')", f"no child for {a}, or a child titled with a bug report.", idle=f"no {a} child → REJECT")
for fact, start, what in (("child_team:Boss Arena", "The Agent creates the Boss Arena child issue of ZOM-543 in team ZOM", "team ZOM"), ("child_assignee:Boss Arena", "The Agent creates the Boss Arena child issue of ZOM-543 with no assignee", "no assignee")):
    new(ft(start), 1, fact, S_LIN, [NOTE, CH[RP.AREAS.index("Boss Arena")]], f"one template field on the Boss Arena child: {what}", f"the Boss Arena child has {what}", f"{what} on the Boss Arena child (note on `ZOM-543`: 'same team, no assignee') · " + F("note"), "lookup: one sentence of Brian's note", ["NOTE"],
        NOTE_SRC + " ('One child each, same team, no assignee.')", f"the Boss Arena child without {what}, or no Boss Arena child.", grp="G1 child template sample", dup=f"{fact} ×1 (the template row @@P:child_template@@ is the control)", idle="no Boss Arena child → REJECT")
new(ft("The Agent gives the 10 child issues it creates under ZOM-543 the template of Brian's note"), 1, "child_template", S_LIN, [NOTE] + CH, "the template of the ten children", "all ten children are in team ZOM with no assignee", "team ZOM and no assignee on the 10 children of `ZOM-543` · " + F("note", "epic"), "lookup: one sentence of Brian's note", ["NOTE"],
    NOTE_SRC + " ('One child each, same team, no assignee.')", "a child in another team or with an assignee.", grp="G1 children (template volume row)", idle="no children → REJECT")
# ---- item 2: child states
ST_T = {a: ft(f"The Agent has the {a} child issue it creates under ZOM-543 in the state Todo at the end of the run") for a in RP.AREAS}
for i, a in ((2, "Zombie Lane"), (3, "Boss Arena"), (4, "Tutorials")): keep(i, ST_T[a], grp="direct (one row per child)")
for a in RP.AREAS:
    if a in ("Zombie Lane", "Boss Arena", "Tutorials"): continue
    new(ST_T[a], 3, f"child_state:{a}", S_LIN, [NOTE, DEC, CH[RP.AREAS.index(a)]], f"the state of the {a} child", f"the {a} child is in Todo at the end of the run", f"Todo for the {a} child (note: 'Set the child to Done if it is Clear and to Todo if it is Open'; {a} has an open report) · " + F("areas", "note"),
        "interpretation: the area's state from its reports under the note's rule", ["NOTE", "SHEETF"], NOTE_SRC + f" ('Set the child to Done if it is Clear and to Todo if it is Open'); {a} has a report that is not Passed", f"the {a} child in Done, or no {a} child.", grp="direct (one row per child)", idle=f"no {a} child → REJECT")
# ---- item 3 and reviewed state rows R5..R43
CHG = {10: 6, 16: 12, 17: 13, 18: 14, 19: 15, 21: 17, 36: 32, 41: 37}
MOVE_ONLY = {12: 8, 14: 10, 20: 16, 22: 18, 23: 19, 25: 21, 28: 24, 32: 28, 34: 30, 38: 34, 40: 36}
def move_title(n): return ft(f"The Agent moves {tr(n)['Ticket']} (the report")
def move_row_new(n):
    tk = tr(n)["Ticket"]; a = T[n]["area"]
    new(move_title(n), 1, f"move:{n}", S_LIN, [NOTE, SHEET, E(f"Move {tk} (report {n})")], f"where {tk} ends up", f"{tk} has the {a} child as its parent", f"`{tk}` under the {a} child (row {n}, area {a}) · " + F(f"rep:{n}", "tickets"), "lookup: the row's Ticket and Area cells", ["NOTE", "SHEETF", "K_" + tk],
        NOTE_SRC + f" ('move that ticket under the child'); row {n} of {ID['sheet']} (area {a})", f"{tk} with no parent or under another child.", grp="direct (one row per moved ticket)", idle=f"{tk} still has no parent → REJECT")
for i in range(5, 44):
    n = i - 4
    if i in (8, 15, 24): continue
    if i in CHG:
        keep(i, ft(f"The Agent sets {tr(n)['Ticket']} (the report"), final=f"{tr(n)['Ticket']} is set to {g['STATE'][tr(n)['Status']]}"); move_row_new(n)
    elif i in MOVE_ONLY:
        tk = tr(n)["Ticket"]; a = T[n]["area"]
        keep(i, move_title(n), 1, fact=f"move:{n}", just="Lookup: the row's Ticket and Area cells.", what=f"where {tk} ends up", final=f"{tk} has the {a} child as its parent", vals=f"`{tk}` under the {a} child (row {n}, area {a}) · " + F(f"rep:{n}", "tickets"), kind="lookup: the row's Ticket and Area cells", band=1, dec="—", dis="—",
             grp="direct (one row per moved ticket)", dup=f"move:{n} ×1", valid=f"{tk} re-parented to the {a} child", idle=f"{tk} still has no parent → REJECT", srcs=["NOTE", "SHEETF", "K_" + tk], cr=f"(a) a valid run could set the state in the same update — the parent is what counts; (b) a wrong run could put {tk} under another area's child")
        OUT[-1]["evidence"] = f"Source: {NOTE_SRC} ('move that ticket under the child'); row {n} of {ID['sheet']} (area {a}). Accept: {acc(move_title(n))}. Reject: {tk} with no parent or under another child."
    else: keep(i)
# ---- item 4: notes R44..R65 each followed by its reason row
for i in range(44, 66):
    r = keep(i); n = int(r["fact"].split(":")[1]); tk = tr(n)["Ticket"]
    t = ft(f"The Agent gives, in its comment on {tk}, the reason"); w = int(re.search(rf"\(weight (\d)\): The Agent gives, in its comment on {tk},", FL).group(1))
    band, kind, dec, oes, fs, wrong = work(n)
    new(t, w, f"note_why:{n}", S_LIN, [NOTE, DEC] + oes[:2] + [E(f"Leave the status note on {tk} ")], f"the reason the Agent's comment on {tk} gives", "the comment gives that reason", f"why on `{tk}`: {tr(n)['Why']} (note: 'leave a note with the status and why') · " + F(f"rep:{n}", *fs),
        ("multi-source: the reason is the record that decides the status" if w == 5 else "interpretation: the reason read from the sheet row's blank cells"), keys_for(n), NOTE_SRC + " ('leave a note with the status and why'); " + tr(n)["Why"] + f" (report {n}, row of {ID['sheet']})", "no reason, or a reason other than the one in this row.",
        grp="direct (one row per note: the reason differs per ticket)", dec=dec, dis=(f"{dec} → graded by the reason" if dec != "—" else "—"), idle=f"no new comment on {tk} → REJECT")
# ---- items 5, 6: R66 deleted; sub-issue creates; R69, R70; template; R71 deleted; R72..R74
def sub_title(n): return ft("The Agent creates a sub-issue titled with Marcus Bennett's report") if n == 39 else ft("The Agent creates a sub-issue titled with the report wording", f'"{T[n]["report"]}"')
keep(67, sub_title(3), 1, fact="sub_create:3", grp="direct (one row per new sub-issue)", dup="sub_create:3 ×1")
keep(68, sub_title(39), 3, fact="sub_create:39", grp="direct (one row per new sub-issue)", dup="area_of:39 ×2 (this and the sheet Area row @@P:sheet_area:39@@)")
NEWN = g["NEWN"]
for n in NEWN:
    if n in (3, 39): continue
    a = T[n]["area"]
    new(sub_title(n), 1, f"sub_create:{n}", S_LIN, [NOTE, SHEET, E(f"Create the sub-issue for report {n} ")], f"the sub-issue for report {n}: its title and parent", f"a sub-issue titled with that report under the {a} child", f"a sub-issue for report {n} under the {a} child (note on `ZOM-543`: 'make a sub-issue under the child with the report as the title') · " + F(f"rep:{n}", "note"),
        "lookup: the row's What happens and Area cells", ["NOTE", "SHEETF"], NOTE_SRC + f" ('make a sub-issue under the child with the report as the title'); row {n} of {ID['sheet']} (area {a})", "no such sub-issue, or one under another child.", grp="direct (one row per new sub-issue)", idle="no sub-issue for that report → REJECT")
keep(69); keep(70)
new(ft("The Agent gives the 17 report sub-issues it creates under the area children the template of Brian's note"), 3, "sub_template", S_LIN, [NOTE, ALIAS, DMS, DEC] + [E(f"Create the sub-issue for report {n} ") for n in NEWN], "the template of the new sub-issues", "the 17 report sub-issues have no priority and no assignee",
    "17 report sub-issues with no priority and no assignee (note: 'No priority and no assignee on the new ones') · " + F("totals", "note", "alias_gift", "alias_streak", "glow"), "interpretation: the template applied over the set of reports no ticket holds", ["NOTE", "ALIAS_GIFT", "ALIAS_STREAK", "GLOW"],
    NOTE_SRC + " ('No priority and no assignee on the new ones'); 39 reports, 22 held by a ticket", "a report sub-issue with a priority or an assignee.", grp="G2 new sub-issues (template volume row)", idle="no sub-issue → REJECT")
for i in (72, 73, 74): keep(i, grp="direct (one row per moved ticket)")
# ---- item 7: the sheet
for i in range(75, 86): keep(i)
new(ft("The Agent puts the key of the sub-issue it creates for the report"), 1, "sheet_ticket:9", S_SHEET, [NOTE, DEC, E("Write the Reports tab"), E("Create the sub-issue for report 9 ")], "the Ticket cell of a report with a new sub-issue", "that row's Ticket cell holds the new sub-issue's key", "the new sub-issue's key in report 9's Ticket cell · " + F("rep:9", "note"),
    "lookup: the key of the sub-issue the run created", ["NOTE", "SHEETF"], NOTE_SRC + " ('Sheet: tab Reports with Report, Area, Status, Ticket, Review list, Why'); report 9 has no existing ticket", "an empty Ticket cell on that row, or the key of another ticket.", grp="G5 Ticket cell sample (a new sub-issue's key)", idle="no stock-take sheet → REJECT")
new(ft("The Agent gives Marcus Bennett's report that the season pass icon glow stays on after everything is claimed the Area Season Pass"), 3, "sheet_area:39", S_SHEET, [NOTE, DMS, DEC, E("Write the Reports tab")], "the Area cell of Marcus's report", "that row's Area is Season Pass", "Area Season Pass for report 39 · " + F("rep:39", "glow"),
    "interpretation: the area read from Marcus's wording", ["NOTE", "GLOW"], f"Marcus's DM {ID['filt_dm']} (the pass icon glow)", "another area on that row, or no row for that report.", grp="G10 Area cell sample", dup="area_of:39 ×2 (this and the sub-issue row @@P:sub_create:39@@)", idle="no stock-take sheet → REJECT", dec="T11")
keep(86, ft("The Agent marks 7 report rows in all as on the review list"))
keep(87, ft("The Agent marks the report \"Reward animation waits too long before the event bar fills\" as on the review list"))
keep(88, ft("The Agent marks the report \"Level-end coins fly while the pre-level panel is already open\" as on the review list"))
keep(89, ft("The Agent marks the report \"Level-end rewards do not show at all right after an app update\" as on the review list"), 5, just="Multi-source: an open Level-end rewards row against the changed agenda on the card.", kind="multi-source: an open Level-end rewards row against the changed agenda on the card", dec="T9")
keep(90, ft("The Agent gives, in the Why cell of the report \"Season pass popup comes up on top of the daily gift when both are due\""), 5, just="Multi-source: the reason joins Vincent's later reply with the order of the two builds.", kind="multi-source: the reason joins Vincent's later reply with the order of the two builds")
keep(91, ft("The Agent gives, in the Why cell of the report \"Win streak tutorial at level 20 freezes the home screen\""), 3, just="Interpretation: no fix has to be checked against the merged pull requests, not only the blank cell.", kind="interpretation: no fix has to be checked against the merged pull requests, not only the blank cell")
for i in range(92, 95): keep(i)
for i in range(95, 105):
    a = D1[i - 1]["fact"].split(":")[1]; w = 5 if i in (96, 104) else None
    r = keep(i, ft(f"The Agent shows {g['AO'][a]} open report{'s' if g['AO'][a] != 1 else ''} for {a} in the Open reports column"), w, **({"just": "Multi-source: the area's Passed rows need the build's branch checked in #builds.", "kind": "multi-source: the area's Passed rows need the build's branch checked in #builds"} if w else {}))
    if i in (101, 102): r["evidence"] = r["evidence"].replace("1 of its reports are not Passed", "1 of its reports is not Passed")
for i in range(105, 121): keep(i)
new("The Agent gives 7 as the number of reports on the review list on the slide it adds to Calvin's ZM queue manager presentation", 5, "slide:review", S_SLIDE, [HUB, DEC, E("Add one slide")], "the number of reports on the review list on the new slide", "the new slide gives 7 reports on the review list",
    "7 reports on the review list (hub: 'how many reports are on the review list'; note: 'Slide: the five numbers I asked you for') · " + F("totals", "reopen2", "card"), "multi-source: the count joins every report's decision", ["HUB", "NOTE"],
    f"Brian's DM {ID['hub']} ('how many reports are on the review list'); " + NOTE_SRC + " ('Slide: the five numbers I asked you for'); computed over the 39 reports", "another number for reports on the review list.", dup="count:review ×2 (the DM and the slide each carry it)", idle="no new slide → REJECT", dec="T6, T9", dis="T6, T9 → graded by the number")
keep(121)
# R47 evidence tidy-up
for r in OUT:
    if r.get("was") == 47: r["evidence"] = r["evidence"].replace("(no fix named, no pass)", "(no fix named; re-test 'again Android #2013')"); r["lock"] = None
# ---- /rubric round 2 (platform_reports/rubric_r2_FAIL.md, reviewed JSON f03edcef1022): two edits, nothing else touched
for r in OUT:
    if r["fact"].startswith("state:") and r["title"].startswith("The Agent sets ZOM-"):
        tk = r["title"].split()[3]
        r["evidence"] = r["evidence"][:r["evidence"].index("Reject:")] + f"Reject: {tk} left in its old state or set to another state (where {tk} sits is graded by its own move row, not here)."
    if r["fact"] == "sub_create:39":
        r["band"] = 5; r["just"] = "Multi-source: the note's scope sentence joined with Marcus's 1:1 chat outside the sheet, plus the area read from his wording."; r["kind"] = "multi-source: the note's scope sentence joined with Marcus's 1:1 chat outside the sheet, plus the area read from his wording"
for i, r in enumerate(OUT, 1): r["p"] = f"P{i}"
PN = {r["fact"]: r["p"] for r in OUT}; assert len(PN) == len(OUT), [f for f in set(r["fact"] for r in OUT) if sum(x["fact"] == f for x in OUT) > 1]
STALE = {"child_count": "child_template", "new_count": "sub_template", "moved_count": "move:4", "new_parent:3": "sub_create:3", "new_parent:39": "sub_create:39"}
def resolve(v):
    v = re.sub(r"\bP\d+\b", lambda m: m.group(0), v)
    return re.sub(r"@@P:(.+?)@@", lambda m: PN.get(m.group(1)) or PN.get(STALE.get(m.group(1), ""), "the row for " + m.group(1)), v)
d1p = {r["p"]: r["fact"] for r in D1}
for r in OUT:
    for k, v in list(r.items()):
        if isinstance(v, str) and k not in ("title", "just", "evidence"):
            v = re.sub(r"\bP(\d+)\b", lambda m: "@@P:" + d1p.get("P" + m.group(1), "?") + "@@" if r.get("was") else m.group(0), v) if k in ("dup", "cr", "vals", "grp") and r.get("was") else v
            r[k] = resolve(v)
assert len({r["title"] for r in OUT}) == len(OUT)
json.dump(OUT, open(os.path.join(HERE, "rubric_final.json"), "w"), indent=1, ensure_ascii=False)
import collections
print("rows", len(OUT), "locked", sum(1 for r in OUT if r["lock"]), collections.Counter(r["band"] for r in OUT), "weight", sum(r["band"] for r in OUT), "max words", max(len(r["title"].split()) for r in OUT))

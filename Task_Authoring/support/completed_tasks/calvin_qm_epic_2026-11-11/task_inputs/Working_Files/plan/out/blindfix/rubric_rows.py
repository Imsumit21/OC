"""Rubric plan rows for calvin_qm_epic (rev3b). One dict per criterion; consumed by assemble_rubric_plan.py and the draft/check builders.
Keys: p, span (exact 04_Prompt.txt span), oe (OE numbers), fact (stable fact id), what, final, cat, vals (probe literals + pointers +
accepted alternatives; F-ids), phr, dis, amb, kind, band, dec (ledger trap ids), grp, dup, af, valid, idle, reach, cr."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import reports as RP
FID = json.load(open(os.path.join(HERE, "oe_ledger_ids.json")))["fid"]
IDX = json.load(open(os.path.join(HERE, "oe_events_index.json")))
TRUTH = json.load(open(os.path.join(os.path.dirname(HERE), "solver", "truth.json")))
ROWS_T = RP.truth()
def F(*ks): return ", ".join(FID[k] for k in ks)
def E(prefix):
    m = [e["n"] for e in IDX if e["action"].startswith(prefix)]
    assert len(m) == 1, (prefix, m); return m[0]
def Es(prefix): return [e["n"] for e in IDX if e["action"].startswith(prefix)]
HUB, NOTE, SHEET, LEG, RULE, CHAT, TIX, BLD, PRS, RC472, RC475, MERGED, ALIAS, S135, SIGHT, DMS, INV, EVT, CARD, FOLD = range(1, 21)
DEC = E("Work out each report")
assert IDX[TIX - 1]["action"].startswith("Read the 20 tickets") and IDX[BLD - 1]["action"].startswith("Read the #builds") and DEC == 21
S_ALL = "I need you to set it all up as he asked"
S_LIN = "the children and report lines in Linear"
S_SHEET = "the stock-take sheet in my ZM queue manager folder"
S_SHARE = "shared with everyone on the review invite"
S_SLIDE = "a slide with the numbers in my queue manager deck"
S_DM = "message him in our DM with the numbers he wants back"
S_ONCE = "Once that's done, message him in our DM"
NOPHR = "no — must not hard-code wording"
R = []
def row(**k):
    for a, b in (("cat", "Outcome"), ("phr", NOPHR), ("dis", "—"), ("amb", "—"), ("grp", "—"), ("dec", "—"), ("af", "none · not over-specific"), ("reach", "PROMPT_LINKED")): k.setdefault(a, b)
    k["p"] = f"P{len(R) + 1}"; R.append(k)
T = {r["n"]: r for r in ROWS_T}
def tr(n): return TRUTH[T[n]["report"]]
STATE = {RP.P: "Done", RP.Q: "In Validation", RP.F: "Todo"}
# deciding work per report: (band, kind, trap ids, extra OEs, extra fact keys, the wrong answer the row rejects)
def work(n):
    r = T[n]; t = r["trap"]
    if t == "BRANCH": return 5, "multi-source: the sheet's ok, the chat, the build's branch in #builds and Arthur's rule", "T1", [CHAT, BLD, RULE, PRS], ["chat", "build:iOS Internal #1718", "rule", "pr465"], "Passed (the ok was on a feature-branch build)"
    if t == "INLINE": return 5, "multi-source: the sheet's Fix cell against the reviewer's comment on that pull request", "T2", [PRS, RC475 if n == 32 else RC472], ["inline2" if n == 32 else "inline"], "Waiting on QA (the review comment says the fix is not in that pull request)"
    if t == "ELSE": return 5, "multi-source: a blank Fix cell against the dev's comment on a merged pull request the sheet does not name", "T3", [MERGED], ["else", "pr473"], "Waiting on a fix (the fix is in merged #473)"
    if t == "BODY": return 5, "multi-source: a blank Fix cell against the description of a merged pull request", "T4", [PRS], ["body", "pr472"], "Waiting on a fix (the fix is in merged #472)"
    if t in ("REOPEN", "BACK"):
        lin = n in (17, 24)
        return 5, "multi-source: a pass on a main build against a later sighting on a later main build" + (" in the ticket's own notes" if lin else " in a Slack thread reply"), "T6" if lin else "T5", [TIX if lin else S135, BLD, RULE], [{9: "reopen", 29: "back", 17: "reopen2", 24: "back2"}[n], "build:Android Submission #135", "rule"], "Passed (the bug was seen again on Android Submission 135)"
    if t == "FILT": return 5, "multi-source: the note's scope sentence joined with a 1:1 chat outside the sheet", "T11", [DMS], ["glow"], "left out (it is not a sheet row)"
    if n == 27: return 5, "multi-source: a pass against a sighting on a build made before the one it passed on", "T7", [SIGHT, BLD, RULE], ["older", "build:Android #2006", "build:iOS Internal #1745", "rule"], "Waiting on a fix (the sighting was on an older build)"
    if n == 18: return 5, "multi-source: the re-test build's time against the pull request's merge time", "T8", [BLD, PRS, RC472], ["build:Android #2013", "pr472", "inline"], "Waiting on a fix (the again was before #472 merged)"
    if n == 34: return 5, "multi-source: the re-test build's time against the pull request's merge time", "T8", [BLD, PRS], ["build:iOS Internal #1757", "pr475"], "Waiting on QA (QA tried a main build made after #475 merged)"
    if r["status"] == RP.P:
        b = re.search(r"(?:ok|nr) (.+)", r["retest"]).group(1)
        return 5, "multi-source: the sheet's re-test, the build's branch in #builds and Arthur's rule", "—", [BLD, RULE, LEG], ["build:" + b, "rule", "legend"], "Waiting on a fix or Waiting on QA"
    return 3, "interpretation: the note's rule applied to one sheet row with no fix and no pass", "T10" if n in (11, 20) else "—", [LEG] + ([ALIAS] if n in (11, 20) else []), ["legend"] + ([{11: "alias_gift", 20: "alias_streak"}[n]] if n in (11, 20) else []), "Passed or Waiting on QA"
def short(n): return T[n]["report"]
# ================================================================== Linear: the ten children
CH = Es("Create the ")[:10]
row(span=S_LIN, oe=[HUB, NOTE] + CH, fact="child_count", what="how many child issues the Agent creates under the Queue Manager ticket, and what each is", final="exactly 10 new issues with parent ZOM-543, one titled for each area in Brian's note",
    vals="10 children under `ZOM-543` (note: 'Children: Tutorials, Level-end rewards, Daily Gift, Season Pass, Collect & Win, Win Streak, Zombie Lane, Boss Arena, Endless Mode, Card packs. One child each, same team, no assignee.') · " + F("note", "epic"),
    phr="yes — the note names the ten areas", kind="lookup: one sentence of Brian's note", band=1, grp="G1 children (volume row stating the template)", dup="child_count ×1",
    valid="ten issues under ZOM-543 titled with the ten area names (a prefix such as 'Queue Manager:' is fine)", idle="no new issue under ZOM-543 → REJECT",
    cr="(a) a valid run could prefix each title with the epic's name — the area name in the title is what counts; (b) a wrong run could create children only for areas with open reports — every area has one, and the note says one child each")
for a, band, dec, kind, why in (("Zombie Lane", 5, "T6", "multi-source: the area's state rolls up from a pass that Owen's later note on ZOM-586 ends", "edge: the area reads as Clear from the sheet"),
                                ("Boss Arena", 5, "T1", "multi-source: the area's state rolls up from an ok that was on a feature-branch build", "edge: the area reads as Clear if the chat ok counts"),
                                ("Tutorials", 3, "—", "interpretation: the area's state from its reports under the note's rule", "ordinary")):
    row(span=S_LIN, oe=[NOTE, DEC, CH[RP.AREAS.index(a)]], fact=f"child_state:{a}", what=f"the state of the {a} child", final=f"the {a} child is in Todo",
        vals=f"Todo for the {a} child (note: 'Set the child to Done if it is Clear and to Todo if it is Open'; {a} has an open report) · " + F("areas", "note"), dis=(f"{dec} → graded by the state" if dec != "—" else "—"), kind=kind, band=band, dec=dec,
        grp=f"G1 child state sample ({why})", dup=f"area_open:{a} ×2 (this and the Areas-tab row @@P:area_status:{a}@@)" if a != "Tutorials" else f"child_state:{a} ×1", valid=f"the {a} child created in Todo (or created and then set to Todo)", idle=f"no {a} child → REJECT",
        cr=f"(a) a valid run could leave the state at the team's default if that is Todo — the end state is what counts; (b) a wrong run could set the {a} child to Done because the sheet shows its rows as passed — a report in it is open")
row(span=S_LIN, oe=[NOTE, CH[0]], fact="child_assignee:Tutorials", what="one template field on the Tutorials child", final="the Tutorials child has no assignee", vals="no assignee on the Tutorials child (note on `ZOM-543`: 'One child each, same team, no assignee.') · " + F("note"), phr="yes — the note fixes the field",
    kind="lookup: one sentence of Brian's note", band=1, grp="G1b child assignee sample", dup="child_assignee:Tutorials ×1 (the volume row @@P:child_count@@ is the control)", valid="the Tutorials child created with no assignee", idle="no Tutorials child → REJECT",
    cr="(a) a valid run could show the field as unassigned or empty — any rendering passes; (b) a wrong run could assign the children to Calvin")
# ================================================================== Linear: one state row per report
NEWN = [n for n in sorted(T) if not tr(n)["Ticket"]]; OLDN = [n for n in sorted(T) if tr(n)["Ticket"]]
assert len(NEWN) == 17 and len(OLDN) == 22
def write_oes(n):
    t = tr(n)
    if t["Ticket"]: return [E(f"Move {t['Ticket']} (report {n})"), E(f"Leave the status note on {t['Ticket']} ")]
    return [E(f"Create the sub-issue for report {n} ")]
CHANGED = [n for n in OLDN if tr(n)["Ticket state as found"] != STATE[tr(n)["Status"]]]; assert len(CHANGED) == 8
STATEN = [n for n in sorted(T) if n in NEWN or n in CHANGED]
for n in STATEN:
    t = tr(n); band, kind, dec, oes, fs, wrong = work(n); st = STATE[t["Status"]]; tk = t["Ticket"]
    name = f"`{tk}`" if tk else f"the sub-issue for report {n}"
    row(span=S_LIN, oe=[NOTE, SHEET, DEC] + oes + write_oes(n)[:1], fact=f"state:{n}", what=f"the Linear state of the line for \"{short(n)}\"", final=(f"{tk} is set to {st}" if tk else f"a sub-issue titled with that report exists in {st}"),
        vals=f"{st} on {name} (status {t['Status']}: {t['Why']}; note: 'put Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix') · " + F(f"rep:{n}", *fs),
        dis=(f"{dec} → graded by the state" if dec != "—" else "—"), kind=kind, band=band, dec=dec, grp="direct (one row per report)", dup=f"status:{n} ×2 (this and " + (f"the note row @@P:note:{n}@@)" if tk else (f"the sheet row @@P:sheet_status:{n}@@)" if n in (1, 9, 38, 39, 3) else "no other row; ×1)")),
        valid=(f"{tk} in {st} after the run" + (f" (it was {t['Ticket state as found']})" if t["Ticket state as found"] != st else " (it already was)") if tk else f"a new sub-issue for that report in {st}"),
        idle=(f"{tk} still {t['Ticket state as found']} and not under a child → REJECT" if tk and t["Ticket state as found"] != st else (f"{tk} not moved under a child and with no note → the row asks for the line under the child in {st} → REJECT" if tk else "no sub-issue for that report → REJECT")),
        cr=f"(a) a valid run could word the title or the state's name as the tool returns it — the state is what counts; (b) a wrong run could reach {wrong} — the records above decide against it")
# ================================================================== Linear: the status note on each existing ticket
for n in OLDN:
    t = tr(n); band, kind, dec, oes, fs, wrong = work(n); tk = t["Ticket"]
    row(span=S_LIN, oe=[NOTE, DEC] + oes[:2] + [E(f"Leave the status note on {tk} ")], fact=f"note:{n}", what=f"the status the Agent's note on {tk} gives", final=f"a comment on {tk} gives the status {t['Status']}",
        vals=f"{t['Status']} in a comment on `{tk}` (note: 'leave a note with the status and why') · " + F(f"rep:{n}", *fs), dis=(f"{dec} → graded by the status in the note" if dec != "—" else "—"), kind=kind, band=band, dec=dec,
        grp="direct (one row per existing ticket: the note's content differs per ticket)", dup=(f"status:{n} ×2 (this and the state row @@P:state:{n}@@)" if n in CHANGED else f"status:{n} ×1"), valid=f"a comment on {tk} saying {t['Status']} with any reason", idle=f"no new comment on {tk} → REJECT",
        cr=f"(a) a valid run could put the status in its own words (waits on a fix, needs a fix) — any wording with that meaning passes; (b) a wrong run could note {wrong}")
for n, v, band, kind, why in ((17, "that the bug was seen again on Android Submission 135 after its pass", 3, "interpretation: the reason read from Samuel's later note", "edge: a pass ended by a ticket note"),
                              (24, "that the bug was seen again on Android Submission 135 after its pass", 3, "interpretation: the reason read from Owen's later note", "edge: same"),
                              (12, "that pull request #472 does not have the fix", 3, "interpretation: the reason read from the reviewer's comment", "edge: a merged PR without the fix"),
                              (6, "that the fix is in merged pull request #472 and QA has not tried it", 3, "interpretation: the reason read from the pull request's description", "edge: a fix the sheet does not name"),
                              (34, "that it still happened on iOS Internal #1757, a build made after #475 merged", 3, "comparison: the re-test build against the merge", "ordinary: the reason is in the sheet and the ticket")):
    tk = tr(n)["Ticket"]; fs = work(n)[4]
    row(span=S_LIN, oe=[NOTE, DEC, E(f"Leave the status note on {tk} ")], fact=f"note_why:{n}", what=f"the reason the Agent's note on {tk} gives", final=f"the note on {tk} says {v}", vals=f"why on `{tk}`: {v} (any wording with that meaning; note: 'leave a note with the status and why') · " + F(f"rep:{n}", *fs),
        kind=kind, band=band, dec=work(n)[2], grp=f"G9 note reason sample ({why})", dup=f"note_why:{n} ×1", valid=f"a note on {tk} giving that reason in any wording", idle=f"no new note on {tk} → REJECT",
        cr="(a) a valid run could name the build or the pull request in another form (135, PR 472) — any form passes; (b) a wrong run could give the sheet's own cell as the reason")
# ================================================================== Linear: new sub-issue template and moves
row(span=S_LIN, oe=[NOTE, ALIAS, DMS, DEC] + [x for n in NEWN for x in write_oes(n)], fact="new_count", what="how many new sub-issues the Agent creates for reports, and the template each follows", final="exactly 17 new sub-issues under the area children",
    vals="17 new sub-issues (39 reports − 22 held by a ticket; note: 'If no ticket has it, make a sub-issue under the child with the report as the title', 'No priority and no assignee on the new ones') · " + F("totals", "alias_gift", "alias_streak", "glow", "note"),
    dis="T10, T11 → graded by the count (a new sub-issue for row 11 or 20 makes 18 or 19; leaving Marcus's report out makes 16)", kind="multi-source: the count joins the sheet's Ticket column, the two older tickets and Marcus's DM", band=5, dec="T10, T11", grp="G2 new sub-issues (volume row stating the template)", dup="new_count ×1",
    valid="17 sub-issues, one per report with no ticket, under the ten children", idle="no sub-issue under any child → REJECT", cr="(a) a valid run could title Marcus's report in its own words — the count is what this row grades; (b) a wrong run could file new sub-issues for rows 11 and 20 — ZOM-556 and ZOM-560 already hold them")
for fact, n, v, kind, grp in (("new_parent:3", 3, "under the Tutorials child", "lookup: the row's Area cell", "G2a parent sample (ordinary)"), ("new_parent:39", 39, "under the Season Pass child", "multi-source: the report comes from Marcus's DM and its area from his wording", "G2a parent sample (edge: no Area cell)"),
                              ("new_priority:22", 22, "no priority", "lookup: one sentence of the note", "G2b priority sample"), ("new_assignee:26", 26, "no assignee", "lookup: one sentence of the note", "G2c assignee sample")):
    row(span=S_LIN, oe=[NOTE, SHEET] + write_oes(n), fact=fact, what=f"one template field on the sub-issue for \"{short(n)}\"", final=f"that sub-issue is {v}" if "under" in v else f"that sub-issue has {v}",
        vals=f"{v} on the sub-issue for report {n} (note on `ZOM-543`) · " + F(f"rep:{n}", "note"), phr="yes — the note fixes the field", kind=kind, band=5 if n == 39 else 1, grp=grp, dup=f"{fact} ×1 (the volume row @@P:new_count@@ is the control)",
        valid=f"the sub-issue for that report {v}", idle="no sub-issue for that report → REJECT", cr="(a) a valid run could show the field as the tool returns it (No priority, 0, unassigned) — any rendering passes; (b) a wrong run could copy the priority or assignee of a neighbouring ticket")
row(span=S_LIN, oe=[NOTE, SHEET, ALIAS, DEC] + [write_oes(n)[0] for n in OLDN], fact="moved_count", what="how many existing tickets the Agent moves under a child", final="exactly 22 existing tickets end with one of the ten children as their parent",
    vals="22 existing tickets (the 20 in the sheet's Ticket column `ZOM-567` to `ZOM-586`, plus `ZOM-556` and `ZOM-560`; note: 'if a ticket already has the report, move that ticket under the child') · " + F("tickets", "alias_gift", "alias_streak"),
    dis="T10 → graded by the count (20 without the two older tickets)", kind="multi-source: the sheet's Ticket column joined with Vincent's notes on two older tickets", band=5, dec="T10", grp="G3 moves (volume row)", dup="moved_count ×1",
    valid="22 tickets re-parented", idle="no ticket re-parented → REJECT", cr="(a) a valid run could move a ticket and set its state in one update — the parent is what counts; (b) a wrong run could move only the 20 the sheet names")
for n, v, band, kind, grp in ((11, "Daily Gift", 5, "multi-source: a blank Ticket cell against Vincent's note on an older ticket under other words", "G3 move sample (edge: an older ticket the sheet does not name)"),
                              (20, "Win Streak", 5, "multi-source: a blank Ticket cell against Vincent's note on an older ticket under other words", "G3 move sample (edge: same)"), (4, "Tutorials", 1, "lookup: the row's Ticket and Area cells", "G3 move sample (ordinary)"),
                              (17, "Collect & Win", 1, "lookup: the row's Ticket and Area cells", "G3 move sample (a ticket filed last)"), (24, "Zombie Lane", 1, "lookup: the row's Ticket and Area cells", "G3 move sample (a ticket filed last)")):
    tk = tr(n)["Ticket"]
    row(span=S_LIN, oe=[SHEET, ALIAS, E(f"Move {tk} (report {n})")], fact=f"move:{n}", what=f"where {tk} ends up", final=f"{tk} has the {v} child as its parent",
        vals=f"`{tk}` under the {v} child (row {n}, area {v}) · " + F(f"rep:{n}", "tickets") + (", " + F({11: "alias_gift", 20: "alias_streak"}[n]) if n in (11, 20) else ""), dis=("T10 → graded by the move" if n in (11, 20) else "—"), kind=kind, band=band, dec="T10" if n in (11, 20) else "—", grp=grp,
        dup=f"move:{n} ×1", valid=f"{tk} re-parented to the {v} child", idle=f"{tk} still has no parent → REJECT", cr=f"(a) a valid run could also link the ticket to the sheet row — the parent is what counts; (b) a wrong run could file a new sub-issue for row {n} and leave {tk} where it is")
row(span=S_LIN, oe=[NOTE, TIX, DEC] + [E(f"Move {tr(n)['Ticket']} (report {n})") for n in CHANGED], fact="state_change_count", what="how many of the moved tickets the Agent changes the state of", final="exactly 8 of the 22 moved tickets end in a different state from the one they started in",
    vals="8 state changes (`ZOM-568`, `ZOM-572`, `ZOM-573`, `ZOM-584` to In Validation; `ZOM-571`, `ZOM-574`, `ZOM-581`, `ZOM-585` to Todo; note: 'If its state does not match the status, put Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix') · " + F("tickets", "totals", "inline", "inline2", "else", "body", "reopen2"),
    dis="T2, T3, T4, T6 → graded by the count", kind="multi-source: the count joins every moved ticket's status with the state it was found in", band=5, dec="T2, T3, T4, T6", grp="G3 moves (state-change volume row)", dup="state_change_count ×1",
    valid="eight tickets with a changed state after the run", idle="no ticket's state changed → REJECT", cr="(a) a valid run could set a state in the same update as the move — the end state is what counts; (b) a wrong run could change only the tickets whose sheet row shows a pass")
# ================================================================== the stock-take sheet
SH = [E("Create the stock-take sheet"), E("Write the Reports tab"), E("Add a second tab"), E("Write the Areas tab"), E("Put the stock-take sheet")]
row(span=S_SHEET, oe=[HUB, FOLD, SH[0], SH[4]], fact="sheet_folder", what="where the stock-take sheet lives", final="a new spreadsheet sits in Calvin's ZM queue manager folder", vals="folder `d_36cdb0374c4aad3b8bf741` (ZM queue manager) · " + F("folder"), phr="yes — the prompt names the folder",
    kind="lookup: the folder the prompt names", band=1, dup="sheet_folder ×1", valid="a new Google Sheet whose parent is that folder (created there or moved in)", idle="no new sheet in the folder → REJECT", cr="(a) a valid run could create the sheet directly in the folder — either route passes; (b) a wrong run could leave it in My Drive")
for fact, tab, cols, oe_ in (("sheet_cols_reports", "Reports", "Report, Area, Status, Ticket, Review list, Why", SH[1]), ("sheet_cols_areas", "Areas", "Area, Status, Open reports", SH[3])):
    row(span=S_SHEET, oe=[NOTE, oe_] + ([SH[2]] if tab == "Areas" else []), fact=fact, what=f"the {tab} tab and its columns", final=f"the stock-take sheet has a tab {tab} with the columns {cols}", vals=f"tab {tab}: {cols} (note on `ZOM-543`: 'Sheet: tab Reports with Report, Area, Status, Ticket, Review list, Why. Tab Areas with Area, Status, Open reports.') · " + F("note"),
        phr="yes — the note names the tab and its columns", kind="lookup: one sentence of Brian's note", band=1, dup=f"{fact} ×1", valid=f"a tab named {tab} whose header row has those columns in any order", idle=f"no stock-take sheet, so no {tab} tab → REJECT",
        cr="(a) a valid run could order the columns differently or add one — the named columns must be there; (b) a wrong run could put everything on one tab")
row(span=S_SHEET, oe=[NOTE, SHEET, DMS, DEC, SH[1]], fact="sheet_rows", what="how many reports the Reports tab lists", final="the Reports tab has exactly 39 report rows",
    vals="39 report rows (38 sheet rows + Marcus's report; note: 'Reports: the rows of Vincent's flow pass sheet, all of them', 'Plus any bug somebody else on the team saw in a build and told you about in a DM') · " + F("totals", "sheet", "glow"),
    dis="T11 → graded by the count (38 without Marcus's report; 40 with the remark from Vincent's chat)", kind="multi-source: the sheet's rows joined with the note's scope sentence and a 1:1 chat", band=5, dec="T11", grp="G4–G7 sheet cells (volume row)", dup="report_count ×1",
    valid="39 rows under the header", idle="no stock-take sheet → REJECT", cr="(a) a valid run could add a totals line under the rows — the report rows are what is counted; (b) a wrong run could list 38")
for n, why in ((1, "edge: an ok on a feature-branch build"), (9, "edge: a pass ended by a thread reply"), (38, "edge: a fix named only in a dev's PR comment"), (39, "edge: the report that is not a sheet row"), (3, "ordinary: passed on a main build")):
    t = tr(n); band, kind, dec, oes, fs, wrong = work(n)
    row(span=S_SHEET, oe=[NOTE, SHEET, DEC] + oes + [SH[1]], fact=f"sheet_status:{n}", what=f"the Status cell of \"{short(n)}\" in the Reports tab", final=f"that row's Status is {t['Status']}",
        vals=f"{t['Status']} in the Status cell of report {n} ({t['Why']}) · " + F(f"rep:{n}", *fs), dis=(f"{dec} → graded by the cell" if dec != "—" else "—"), kind=kind, band=band, dec=dec, grp=f"G4 Status cell sample ({why})",
        dup=f"status:{n} ×2 (this and the state row @@P:state:{n}@@)", valid=f"the row for that report with Status {t['Status']}", idle="no stock-take sheet → REJECT", cr=f"(a) a valid run could shorten the status (QA, Fix) — any wording that names the same one of the three passes; (b) a wrong run could write {wrong}")
for n, v, band, kind, why in ((11, "ZOM-556", 5, "multi-source: a blank Ticket cell against Vincent's note on an older ticket", "edge: the key is not in Vincent's sheet"), (4, "ZOM-567", 1, "lookup: the key copied from Vincent's sheet", "ordinary")):
    row(span=S_SHEET, oe=[SHEET, ALIAS, DEC, SH[1]], fact=f"sheet_ticket:{n}", what=f"the Ticket cell of \"{short(n)}\" in the Reports tab", final=f"that row's Ticket is {v}", vals=f"`{v}` in the Ticket cell of report {n} · " + F(f"rep:{n}") + (", " + F("alias_gift") if n == 11 else ""),
        dis=("T10 → graded by the key" if n == 11 else "—"), kind=kind, band=band, dec="T10" if n == 11 else "—", grp=f"G5 Ticket cell sample ({why})", dup=f"sheet_ticket:{n} ×1", valid=f"the row for that report with {v} in its Ticket cell (key or link)", idle="no stock-take sheet → REJECT",
        cr=f"(a) a valid run could write the key as a link — the key is what counts; (b) a wrong run could put the key of a new sub-issue there" if n == 11 else "(a) a valid run could write the key as a link — the key is what counts; (b) a wrong run could leave the cell blank")
REV = [n for n in sorted(T) if tr(n)["Review list"] == "Yes"]; assert REV == [6, 8, 15, 17, 18, 19, 36]
for a, c, dec, kind in (("Level-end rewards", 3, "T9", "multi-source: the area's open rows joined with the changed agenda on the Trello card"), ("Collect & Win", 4, "T6", "multi-source: the area's open rows, one of them a pass ended by a later ticket note, joined with the agenda")):
    row(span=S_SHEET, oe=[NOTE, INV, CARD, DEC, SH[1]], fact=f"review_marked:{a}", what=f"how many {a} reports the Reports tab marks for the review list", final=f"exactly {c} report rows of the area {a} are marked as on the review list",
        vals=f"{c} marked rows in {a} (not Passed, in an area on the agenda of the card `68daad83bacf52c6ea7e1593`; note: 'Review list: a report that is not Passed, in an area on the agenda of Thursday's review') · " + F("areas", "card") + (", " + F("reopen2") if a == "Collect & Win" else ""),
        dis=f"{dec} → graded by the count", kind=kind, band=5, dec=dec, grp="G6 Review list cells (volume row per agenda area)", dup=f"review_marked:{a} ×1", valid=f"{c} rows of {a} with an affirmative mark in Review list", idle="no stock-take sheet → REJECT",
        cr=f"(a) a valid run could mark with Yes, Y, TRUE, a tick or x — any affirmative mark passes; (b) a wrong run could mark " + ("no Level-end rewards row because Brian's Sep 29 line named collect&win and daily gift" if a == "Level-end rewards" else "three, leaving out the row that reads as passed in the sheet"))
for n, yes, band, dec, kind, why in ((17, True, 5, "T6", "multi-source: a pass ended by a later ticket note, in an agenda area", "edge: reads as passed in the sheet"), (6, True, 5, "T9", "multi-source: an open Level-end rewards row against the changed agenda on the card", "edge: its area is only on the changed agenda"),
                                     (36, True, 5, "T9", "multi-source: an open Level-end rewards row against the changed agenda on the card", "ordinary for its area")):
    row(span=S_SHEET, oe=[NOTE, CARD, DEC, SH[1]] + ([TIX] if n == 17 else []), fact=f"sheet_review:{n}", what=f"the Review list cell of \"{short(n)}\" in the Reports tab", final=f"that row is {'marked as on' if yes else 'shown as not on'} the review list",
        vals=f"Review list {'Yes' if yes else 'No'} for report {n} (area {T[n]['area']}; card `68daad83bacf52c6ea7e1593`: 'Collect & Win, Level-end rewards') · " + F(f"rep:{n}", "card"), dis=(f"{dec} → graded by the cell" if dec != "—" else "—"), kind=kind, band=band, dec=dec,
        grp=f"G6 Review list cell sample ({why})", dup=f"sheet_review:{n} ×1", valid=f"the row for that report with {'Yes or a mark' if yes else 'No, or an empty Review list cell while other rows are marked'}", idle="no stock-take sheet, so no row for that report → REJECT",
        cr="(a) a valid run could use any mark — the meaning is what counts; (b) a wrong run could " + ("leave it unmarked because the sheet says ok" if n == 17 else "leave it unmarked because Brian's Sep 29 line named collect&win and daily gift" if n == 6 else "leave it unmarked"))
for n, v, band, why in ((9, "that it was seen again on Android Submission 135", 3, "edge: the reason is a later record"), (4, "that it has no fix and no pass", 1, "ordinary")):
    row(span=S_SHEET, oe=[NOTE, DEC, SH[1]] + ([S135] if n == 9 else []), fact=f"sheet_why:{n}", what=f"the Why cell of \"{short(n)}\" in the Reports tab", final=f"that row's Why says {v}", vals=f"Why for report {n}: {v} (any wording with that meaning) · " + F(f"rep:{n}") + (", " + F("reopen") if n == 9 else ""),
        kind=("interpretation: the reason read from Vincent's reply" if n == 9 else "lookup: the row's blank cells"), band=band, dec="T5" if n == 9 else "—", grp=f"G7 Why cell sample ({why})", dup=f"sheet_why:{n} ×1", valid=f"a Why cell on that row saying {v}", idle="no stock-take sheet → REJECT",
        cr="(a) a valid run could name the build as 135 or Submission #135 — either passes; (b) a wrong run could give 'nr on a main build' as the reason" if n == 9 else "(a) a valid run could say 'not fixed yet' — any wording with that meaning passes; (b) a wrong run could leave the cell empty")
for n, v, band, kind, why in ((39, "Season Pass", 5, "multi-source: the report comes from Marcus's DM and its area from his wording", "edge: no Area cell to copy"), (9, "Daily Gift", 1, "lookup: the row's Area cell", "ordinary (the wording names another area)")):
    row(span=S_SHEET, oe=[NOTE, SHEET, DEC, SH[1]] + ([DMS] if n == 39 else []), fact=f"sheet_area:{n}", what=f"the Area cell of \"{short(n)}\" in the Reports tab", final=f"that row's Area is {v}", vals=f"Area {v} for report {n} · " + F(f"rep:{n}") + (", " + F("glow") if n == 39 else ""),
        kind=kind, band=band, dec="T11" if n == 39 else "—", grp=f"G10 Area cell sample ({why})", dup=(f"area_of:{n} ×2 (this and the parent row @@P:new_parent:39@@)" if n == 39 else f"sheet_area:{n} ×1"), valid=f"the row for that report with Area {v}", idle="no stock-take sheet → REJECT",
        cr="(a) a valid run could write the area in another case — the area is what counts; (b) a wrong run could put the report under " + ("Card packs or leave Area empty" if n == 39 else "Season Pass because of its wording"))
row(span=S_SHEET, oe=[NOTE, DEC, SH[3]], fact="area_rows", what="how many areas the Areas tab lists", final="the Areas tab has exactly 10 area rows", vals="10 area rows (the ten areas of the note on `ZOM-543`) · " + F("areas", "note"), kind="lookup: the ten areas the note names", band=1, grp="G8 Areas tab (volume row)", dup="area_rows ×1",
    valid="ten rows, one per area", idle="no stock-take sheet → REJECT", cr="(a) a valid run could add a total row — the area rows are what is counted; (b) a wrong run could list only areas with open reports")
for a, band, dec, kind in (("Zombie Lane", 5, "T6", "multi-source: the area rolls up from a pass that a later ticket note ends"), ("Boss Arena", 5, "T1", "multi-source: the area rolls up from an ok on a feature-branch build")):
    row(span=S_SHEET, oe=[NOTE, DEC, SH[3]] + ([TIX] if a == "Zombie Lane" else [BLD]), fact=f"area_status:{a}", what=f"the Status of {a} in the Areas tab", final=f"the {a} row's Status is Open", vals=f"Open for {a} (note: 'A child is Clear when all its reports are Passed, otherwise Open') · " + F("areas") + ", " + F("back2" if a == "Zombie Lane" else "chat"),
        dis=f"{dec} → graded by the cell", kind=kind, band=band, dec=dec, grp="G8 area Status sample (edge: reads as Clear)", dup=f"area_open:{a} ×2 (this and the child row @@P:child_state:{a}@@)", valid=f"the {a} row with Status Open", idle="no stock-take sheet → REJECT",
        cr=f"(a) a valid run could write 'Open (1)' — the status word is what counts; (b) a wrong run could write Clear for {a}")
AO = {a: sum(1 for r in ROWS_T if r["area"] == a and r["status"] != RP.P) for a in RP.AREAS}
for a in RP.AREAS:
    hard = {"Zombie Lane": ("T6", "back2"), "Collect & Win": ("T6", "reopen2"), "Daily Gift": ("T5", "reopen"), "Endless Mode": ("T5", "back"), "Season Pass": ("T11", "glow"), "Boss Arena": ("T1", "chat"), "Tutorials": ("T1", "chat")}.get(a)
    row(span=S_SHEET, oe=[NOTE, DEC, SH[3]], fact=f"area_open_count:{a}", what=f"the Open reports of {a} in the Areas tab", final=f"the {a} row shows {AO[a]} open report{'s' if AO[a] != 1 else ''}",
        vals=f"{AO[a]} open in {a} (as a count, or as a list of exactly those {AO[a]} reports) · " + F("areas") + (", " + F(hard[1]) if hard else ""), dis=(f"{hard[0]} → graded by the count" if hard else "—"), amb="ledger risk 1 → a count or the list of the open reports both pass",
        kind=("multi-source: the count depends on a status decided outside the sheet" if hard else "calculation: the area's open rows counted"), band=5 if hard else 3, dec=hard[0] if hard else "—", grp="direct (one row per area: the value differs per area)", dup=f"area_open_count:{a} ×1",
        valid=f"the {a} row with {AO[a]} in Open reports, or with the {AO[a]} open reports listed", idle="no stock-take sheet → REJECT", cr=f"(a) a valid run could list the open reports in the cell — a list of exactly those passes; (b) a wrong run could show {AO[a] - 1} for {a}")
# ================================================================== shares, slide, DM
names = {"arthur.blake": "Arthur Blake", "brian.foster": "Brian Foster", "julia.lawson": "Julia Lawson", "leonard.hayes": "Leonard Hayes", "vincent.parker": "Vincent Parker"}
for k, nm in names.items():
    row(span=S_SHARE, oe=[HUB, INV, EVT, E(f"Share the stock-take sheet with {nm}")], fact=f"share:{k}", what=f"the stock-take sheet is shared with {nm}", final=f"{k}@harmonygames.co can open the stock-take sheet", vals=f"{k}@harmonygames.co on the sheet's sharing list (attendee of `evt_342a813cb7765d4a6fce8d`) · " + F("event"),
        amb="ledger risk 2 → any role passes", kind="lookup: one attendee of the review event", band=1, grp="direct (one row per recipient)", dup=f"share:{k} ×1", valid=f"the sheet shared with {k}@harmonygames.co at any role", idle="no stock-take sheet to share → REJECT",
        cr="(a) a valid run could share as reader, commenter or writer — any role passes; (b) a wrong run could share only with Brian and Vincent")
SL, DM = E("Add one slide"), E("Message Brian")
row(span=S_SLIDE, oe=[HUB, FOLD, SL], fact="slide_new", what="the slide is a new one in Calvin's deck", final="the ZM queue manager presentation has one more slide than before, carrying the numbers", vals="one new slide in `f_637e63ae6c1b4a7eb016aa` (hub: 'add one slide with the numbers') · " + F("deck"), phr="yes — 'add one slide'",
    kind="lookup: the deck the prompt names", band=1, dup="slide_new ×1", valid="a new slide appended to the deck", idle="the deck unchanged → REJECT", cr="(a) a valid run could place the slide anywhere in the deck — position is free; (b) a wrong run could overwrite an existing slide")
NUM = (("passed", "10", "reports passed", "T1, T5, T6", ("reopen", "back", "reopen2", "back2", "chat")), ("qa", "9", "reports waiting on QA", "T1, T2, T3, T4", ("inline", "inline2", "else", "body", "chat")), ("fix", "20", "reports waiting on a fix", "T2, T3, T5, T6, T11", ("inline", "else", "reopen2", "glow")),
       ("clear", "0", "areas clear", "T6, T1", ("back2", "chat")), ("review", "7", "reports on the review list", "T6, T9", ("reopen2", "card")))
for where, span, oe_, art in (("dm", S_DM, DM, "the Agent's message in Calvin's DM with Brian"), ("slide", S_SLIDE, SL, "the new slide in the ZM queue manager deck")):
    if where == "dm":
        row(span=S_DM, oe=[HUB, DM], fact="dm_place", what="where the Agent reports back", final="a message from the Agent in Calvin's DM with Brian Foster", vals="the DM D0770ET6WBW (Calvin and Brian) · " + F("hub"), phr="yes — 'in our DM'", amb="ledger risk 4 → a new message or a thread reply under Brian's message both pass",
            kind="lookup: the DM the prompt names", band=1, dup="dm_place ×1", valid="a message in that DM, top-level or in the thread under Brian's Sep 30 message", idle="no message in the DM → REJECT", cr="(a) a valid run could reply in the thread — it is the same DM; (b) a wrong run could post in a channel")
    for key, lit, label, dec, fs in NUM:
        row(span=span, oe=[HUB, DEC, oe_], fact=f"{where}:{key}", what=f"the number of {label} on {art}", final=f"{art} gives {lit} {label}", vals=f"{lit} {label} (computed over the 39 reports; hub: 'how many reports are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many reports are on the review list') · " + F("totals", *fs),
            dis=f"{dec} → graded by the number", kind="multi-source: the count joins every report's decision", band=5, dec=dec, dup=f"count:{key} ×2 (the DM and the slide each carry it; no third row)",
            valid=f"'{label}: {lit}' in any wording" + (" (none, zero or 0 of 10)" if key == "clear" else ""), idle=("no message in the DM → REJECT" if where == "dm" else "no new slide → REJECT"), cr=f"(a) a valid run could write the number in words — any rendering passes; (b) a wrong run could give the sheet-only number for {label}")
row(span=S_ONCE, oe=[DM], fact="dm_after_writes", cat="Process candidate → C", what="the message comes after the other writes", final="the message with the numbers is posted after the run's last Linear, sheet, share and slide write", vals="Once that's done (prompt) · " + F("hub"), phr="yes — 'Once that's done'",
    kind="lookup: the prompt orders the message last", band=1, dup="dm_after_writes ×1", valid="the message with the numbers is the run's last write", idle="no message in the run → REJECT", cr="(a) a valid run could send a short heads-up first and the numbers last — the row grades the message with the numbers; (b) a wrong run could message first and build after")
PN = {r["fact"]: r["p"] for r in R}
assert len(PN) == len(R), (len(PN), len(R))
for r in R:
    for k, v in list(r.items()):
        if isinstance(v, str): r[k] = re.sub(r"@@P:(.+?)@@", lambda m: PN[m.group(1)], v)
if __name__ == "__main__":
    import collections
    print("rows", len(R), collections.Counter(r["band"] for r in R), "weight", sum(r["band"] for r in R))

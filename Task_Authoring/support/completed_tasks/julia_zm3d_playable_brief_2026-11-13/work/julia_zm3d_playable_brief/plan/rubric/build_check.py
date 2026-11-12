#!/usr/bin/env python3
"""Write the rubric check (Working_Files/09_Rubric_Check.md) and the per-criterion rows of 00_V3_Authoring_Evidence.json.

Check mode only: 09_Rubrics.json is read, never edited. The report records the platform /rubric round 2 verdict on this
exact file (NON-FAIL 3) and the baseline verifier's results, and adds the local per-row review. Run from the workspace
root with TASK_AUTHORING_TASK_DIR set; then `stage_gate.py rubric-check <task_dir> --paste`."""
import collections, hashlib, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_model as C                     # noqa: E402
import stage_gate as SG                     # noqa: E402  (file_digest only)
M, ROWS, TASK, WF = C.M, C.ROWS, C.TASK, C.WF
ASK, NOTES, PACK, LOG, SOUND, A1, A2 = C.ASK, C.NOTES, C.PACK, C.LOG, C.SOUND, C.A1, C.A2
RULE = "C08H78VJG80/1758022459.227279"
RECOLOUR = "C090N54TG79/1759189466.554739"
PICKS, ZPICKS, BOW = M.PICKS["id"], M.ZPICKS["id"], M.C3["id"]
RSHA = hashlib.sha256((TASK / "09_Rubrics.json").read_bytes()).hexdigest()
assert RSHA.startswith("ea8009a35949"), RSHA          # the file /rubric round 2 reviewed and the verifier graded

# ------------------------------------------------------------------ verifier tallies (bound matrix of stage 11)
MAT = json.loads((WF / "12_difficulty_input.json").read_text())
PASSED = {int(r["id"][1:]): [ro["id"] for ro in MAT["rollouts"] if ro["results"][r["id"]]] for r in MAT["rubrics"]}
assert collections.Counter(len(v) for v in PASSED.values()) == {1: 77, 6: 70, 4: 3, 0: 3}
def tally(k):
    p = PASSED[k]
    if len(p) == 6: return "verifier: passed in 6/6 runs"
    if not p: return "verifier: failed in 6/6 runs (stage 11: a real miss, each deciding record was opened by one run)"
    return f"verifier: passed in {len(p)}/6 ({', '.join(p)})"
# rows decided by one hidden record pass only in the run that opened it (stage 11 evidence)
FOUND_BY = {"A1": "run-4", "A2": "run-6", "C4": "run-5"}
for r in ROWS:
    l = r["line"]
    if l and l["cls"] in FOUND_BY and r["fam"] in ("state", "owed_cell", "holder_cell", "move", "comment_owed", "comment_holder"):
        assert PASSED[r["k"]] == [FOUND_BY[l["cls"]]], (r["cid"], PASSED[r["k"]])

# ------------------------------------------------------------------ per-row review: valid alternative, near miss, resolution
DECIDER = {"A1": f"Marcus's post {A1} read with PlayableX's format rule {RULE}", "A2": f"Robert's note {A2}", "C4": f"Brian's log {LOG}",
           "C2": f"Calvin's sheet {SOUND} with the notes' sound rule {NOTES}", "C1": f"Brian's log {LOG} (the recoloured models sent again), after Robert's recolour message {RECOLOUR}",
           "VIS": "Brian's own note on the ticket", "READY": "Brian's note on the ticket, with no later record about the line", "W": "the ticket's Done state and Brian's note"}
OWED_ALT = {"A1": "'re-export as binary', a .glb or a .blend (the title's own alternatives)", "A2": "'the file again after the UV redo', 'resend once the UVs are done'",
            "C4": "'re-upload the file' or 're-zip' (accepted in the evidence; the /rubric round 2 Minor finding on this widening is under Findings)",
            "C2": "'a replacement made here', 'our own recording of it'"}
OWED_MISS = {"A1": "the UV redo or the cut-off zip given as what is owed, or 'Ready'", "A2": "a binary export given as what is owed (the Thursday-saves reason), or 'Ready'",
             "C4": "a binary re-export given as what is owed (the decoy from Marcus's post), or 'Ready'", "C2": "'send the .wav again', which hands over the library sound"}

def other(who): return {"Brian": "Claire", "Claire": "Brian", "Calvin": "Brian", "Martin": "Brian"}[who]

def review(r):
    f, l = r["fam"], r["line"]
    name = l["name"] if l else None; t = l["ticket"] if l else None; cls = l["cls"] if l else None
    if f == "brief_doc":
        return ("a brief saved in a folder of Julia's Drive, or under another title", "a Word file uploaded to Drive, or a Google Doc someone else owns",
                f"the evidence accepts her Drive root or any folder she owns and fixes no title; 'Google Doc owned by Julia' rejects the upload and the other owner (ask {ASK})")
    if f == "sheet_doc":
        return ("a sheet saved in a folder of Julia's Drive, or under another title", "a CSV file, or a new tab added to Brian's pack list",
                f"the evidence accepts her Drive root or any folder she owns; 'Google Sheet owned by Julia' rejects the CSV and Brian's file {PACK} (ask {ASK})")
    if f == "b_scenario":
        return ("'scenario one' or 'the first scenario'", "Scenario 2 or Scenario 3, the vendor's other proposals", "the title names Scenario 1 (Frederick's reply C08H78VJG80/1757956024.883249)")
    if f == "b_purpose":
        return ("Frederick's wording, Robert's wording or a paraphrase of either", "a hardcore-friendly or tailored version given as the purpose",
                "the title quotes both accepted wordings and the evidence accepts a paraphrase; the tailored version is in the Reject clause (round 1 fix, passed in round 2)")
    if f == "b_eight":
        item = re.search(r"lists (?:the )?(.+?) in its brief", r["title"]).group(1)
        if item == "Bow":
            return ("'the bow' or 'Bow (as it is now)'", "Dynamite kept in the eight and the Bow left out, which is Robert's list before his reply",
                    f"the title names the Bow among the eight; Robert's reply {BOW} puts it in place of the last item on his list {PICKS}")
        return (f"{item} named in a list or in a sentence", f"{item} left out of the eight, or listed only among the extras", f"the title names {item} among the eight (Robert's picks {PICKS})")
    if f == "b_extras":
        return ("'the other board items are extras', 'they can swap in any of the others'", "only the eight listed, with no word on the rest of the list",
                f"the title carries the statement itself; the notes {NOTES} ask for it")
    if f == "b_zombie":
        z = re.search(r"names (.+?) in its brief", r["title"]).group(1)
        return (f"{z} named in any order among the four", f"another zombie from the platform in place of {z}", f"the title names {z} (Robert's zombie picks {ZPICKS})")
    if f == "b_anim":
        return ("'walk' or 'walking'", "an attack or idle animation, or several animations", f"the title names walk as the one animation ({ZPICKS})")
    if f == "b_win":
        return ("'kill all the zombies', 'clear every zombie'", "a score or a timer given as the win condition", "the title states the condition; the evidence accepts the paraphrases (C08H78VJG80/1758717625.209649)")
    if f == "b_lose":
        return ("zero health, with or without the word 'only'", "a full tray given as a way to lose", "the title names health running out as the only way and says 'only' need not appear; the full tray is in the Reject clause (page_zm3d_gdd)")
    if f == "b_tray":
        return ("'7', 'seven', 'a 7-slot tray'", "6 slots, from Julia's soft-test comment on the design page", "the title names 7; the 6-slot comment is in the Reject clause (page_zm3d_gdd)")
    if f == "b_use":
        s = re.search(r"lists the (.+?) in its brief", r["title"]).group(1)
        return (f"the {s} named in a list or in a sentence", f"the {s} left out of the usable sounds",
                f"the title names the {s}; Calvin's sheet {SOUND} marks it 'yes'. A brief that also lists the Rocket and Explosion sounds as usable still passes: the Minor overly_broad finding below, scored by /rubric round 2")
    if f == "b_music":
        return ("first click, tap, touch or other first interaction", "music from the start of the playable, or after the first match", "the title lists the accepted wordings (PlayableX's rule C08H78VJG80/1744637266.363689)")
    if f == "b_start":
        return ("'Nov 3', '3 November', '2025-11-03', with or without the year", "September 29 or October 6, the earlier dates in the thread",
                "the title gives November 3, 2025 and accepts it without the year; a date only, no time (C08H78VJG80/1759226395.551469)")
    if f == "sheet_header":
        return ("'What is owed' for 'What's owed', any letter case", "a column left out, or 'Status' in place of State", f"the title lists the seven names from the notes {NOTES}")
    if f == "sheet_volume":
        return ("the 96 rows in any order", "49 rows (only the Owed lines) or 88 (the Delivered lines left out)", f"the title gives 96; the pack list {PACK} has 96 lines and the notes ask for one row per line")
    if f == "state":
        val = re.search(r"the State '(\w+)'", r["title"]).group(1)
        miss = {"A1": "'Ready', the reading from Brian's note alone", "A2": "'Ready', the reading from Brian's note alone",
                "C1": "'Owed', the reading from Robert's recolour message without Brian's log", "READY": "'Owed' or 'Delivered'", "W": "'Ready', the ticket's Done state not read"}[cls]
        return (f"no other word: the notes fix three State words, so '{val}' is the only valid value", miss, f"the title names '{val}' for {name} ({t}); decided by {DECIDER[cls]}")
    if f == "owed_cell":
        return (OWED_ALT[cls], OWED_MISS[cls], f"the title names what is owed for {name} ({t}); decided by {DECIDER[cls]}")
    if f == "holder_cell":
        who = l["who"]
        return (f"'{who}' or '{C.FULL[who]}'", f"{other(who)}, or nobody named", f"the title names {who} for {name} ({t}); the notes: whoever has to do the next thing; decided by {DECIDER[cls]}")
    if f == "board_set":
        if name == "Cannon":
            return ("an empty cell", "'Extra', the Cannon read as a board item", f"the title asks for an empty Board set; the pack list {PACK} gives Cannon ({t}) the Kind Weapon and the notes leave Board set empty for anything that isn't a board item")
        val = re.search(r"Board set '(\w+)'", r["title"]).group(1)
        miss = {"Bow": "'Extra', Robert's list before his reply about the bow", "Dynamite": "'Default', Robert's list before his reply about the bow"}.get(name, f"'{'Extra' if val == 'Default' else 'Default'}' or an empty cell")
        return (f"no other word: the notes fix Default, Extra or empty, so '{val}' is the only valid value", miss, f"the title names '{val}' for {name} ({t}); Robert's picks {PICKS} and his reply {BOW}")
    if f == "ticket_cell":
        return (f"'{t}' as text or as a link to the ticket", "a neighbouring line's ticket", f"the title names {t} for {name}; the pack list {PACK}")
    if f == "category_cell":
        return ("'Bathroom' in any letter case", "another category, or the Kind value in that cell", f"the title names Bathroom for {name}; the pack list {PACK}")
    if f == "move":
        return ("the state change before or after the comment, at any point among the 49", f"a comment added while {t} stays In Progress, or a move to Backlog",
                f"the title names {t} and Todo; the notes {NOTES} send an Owed line's ticket to Todo; decided by {DECIDER[cls]}")
    if f == "move_volume":
        return ("the 49 moves in any order", "20, 25 or 32 moves (what the six baseline runs made), or 52 with the three recoloured models",
                f"the title gives exactly 49 under DES-313; it is the one volume row of the move group (C50 to C54 are its samples); the notes {NOTES}")
    if f == "comment_owed":
        return (OWED_ALT[cls], OWED_MISS[cls], f"the title names {t} and what is owed; decided by {DECIDER[cls]}")
    if f == "comment_holder":
        who = l["who"]
        return (f"'{who}' or '{C.FULL[who]}'", f"{other(who)}, or nobody named", f"the title names {who} and {t}; the notes: whoever has to do the next thing; decided by {DECIDER[cls]}")
    if f == "comment_both":
        who = l["who"]
        return ("any wording of Brian's note", f"only one half (what is owed without {who}, or {who} without what is owed)",
                f"one ticket note states both, so the row grades one record of {t} (coherent_record; /rubric round 2 kept these rows combined); Brian's note on {t}")
    if f == "share":
        who = re.search(r"gives (\S+) view-only", r["title"]).group(1)
        src = f"the notes {NOTES} and the kickoff hold {M.HOLD_ID}" if "playablex" not in who else f"the notes {NOTES} (the intake address in Contacts)"
        return ("the share made with or without a notification", "commenter or editor access, or a link open to anyone in place of the named share", f"the title names {who} and reader access; {src}")
    if f == "dm":
        st, n = re.search(r"the (\w+) count is (\d+)", r["title"]).groups()
        miss = {"Owed": "15, the count from Brian's notes alone, or the baseline runs' 20, 25 and 32", "Ready": "73, the count from Brian's notes alone, or the baseline runs' 68, 63 and 56",
                "Delivered": "another number for Delivered"}[st]
        return (f"'{n} {st}' or '{st}: {n}', in a new DM message or a reply in the thread of the ask", miss,
                f"the title names {st} and {n} in the DM; the ask {ASK} says 'give me the count for each state here'; the verifier read both a new message and a thread reply")
    if f == "post":
        return ("one message carrying both links, or one message per link", "the link sent only in the DM, or a link to Brian's pack list",
                f"the title names the file and the channel C08H78VJG80; the ask {ASK} says 'post both links in the PlayableX channel'")
    if f == "order":
        return ("the file created, filled and shared, then the link posted, with any gap between", "the link posted while the file is still empty, with the content written afterwards",
                "Process row: every valid path writes the file before posting its link, no Outcome row can see the order, and the row describes a behaviour (the prompt's 'once they're ready'); /rubric round 2 passed both (2 of 2 valid)")
    raise KeyError(f)

REV = {r["k"]: review(r) for r in ROWS}

# ------------------------------------------------------------------ V3 evidence rows
def derivation(r):
    f, l = r["fam"], r["line"]
    if f in ("state", "owed_cell", "holder_cell", "board_set", "ticket_cell", "category_cell") and l:
        return (f"Row '{l['name']}' of the pack list grid (grid_json of the gsheets.sheets_sheets row of {PACK}): Kind {l['kind']}, Category {l['category']}, "
                f"Went out '{l['went_out']}', Ticket {l['ticket']}; ticket state {l['ticket_state']}; model class {l['cls']}, State {l['state']}"
                + (f", owed: {l['owed']}, who has it: {l['who']}" if l["state"] == "Owed" else "")
                + (f", Board set {l['board'] or 'empty'}" if f == "board_set" else ""))
    if f in ("dm", "move_volume", "sheet_volume"):
        return ("96 lines on the pack list: Delivered 8 (ticket Done), Ready 39 (36 with no later word and the 3 recoloured models sent again), Owed 49 "
                "(15 by Brian's own note, 12 Unity saves, 12 bathroom files, 8 instruments, 2 library sounds); computed in oe_gen/model.py from the SQL rows")
    if f == "share" and "playablex" in r["title"]:
        return (f"intake@playablex.ai is the email of the seeded Contacts row {C.CONTACT_ID} (contacts.contacts, PlayableX intake). The table has no time column and the "
                "gate's Contacts lookup reads base data only, so the row is named here and the notes that point to it are the cited source")
    return None

def v3_rows():
    out = []
    for r in ROWS:
        a, b, res = REV[r["k"]]
        srcs, _ = C.sources_for(r)
        assert r["accept"], r["cid"]
        row = {"criterion_id": r["cid"], "plan_row": f"P{r['from'][1:]}" if r["from"] else "round 1 Fix List row", "fact_id": r["fact"], "prompt_span": r["span"],
               "accepted_outcomes": [r["accept"]],
               "alternatives_review": f"Reject: {r['reject']} Counter-reading: (a) a valid answer that could fail: {a}; accepted. (b) a wrong answer that could pass: {b}; rejected. Basis: {res}.",
               "source_records": srcs}
        d = derivation(r)
        if d: row["derivation"] = d
        out.append(row)
    return out

EV_PATH = WF / "00_V3_Authoring_Evidence.json"
ev = json.loads(EV_PATH.read_text())
ev["prompt_hash"] = SG.file_digest(TASK / "04_Prompt.txt")
ev["rubric_hash"] = SG.file_digest(TASK / "09_Rubrics.json")
ev["rubric_rows"] = v3_rows()
facts = collections.Counter(x["fact_id"] for x in ev["rubric_rows"])
assert max(facts.values()) <= 2, facts.most_common(3)
EV_PATH.write_text(json.dumps(ev, indent=1, ensure_ascii=False) + "\n")

# ------------------------------------------------------------------ report pieces
def rng(ks):
    ks = sorted(ks); out = []; s = p = ks[0]
    for k in ks[1:] + [None]:
        if k is not None and k == p + 1: p = k; continue
        out.append(f"C{s}" if s == p else f"C{s}–C{p}"); s = p = k
    return ", ".join(out)
def ks(*fams): return [r["k"] for r in ROWS if r["fam"] in fams]
def cls_ks(fam, cls): return [r["k"] for r in ROWS if r["fam"] == fam and r["line"] and r["line"]["cls"] == cls]

COVERAGE = [
    ("Brief as a Google Doc in Julia's Drive (prompt 'The files he wants should end up in my Drive'; ask 'Brief as a doc')", ks("brief_doc"), "an idle run has no doc; a doc someone else owns fails"),
    ("Brief: which scenario was picked and what it is for (notes)", ks("b_scenario", "b_purpose"), "no brief fails both; Scenario 2 or a tailored purpose fails"),
    ("Brief: the eight items on the board, and every other board item as an extra (notes; Robert's picks and his bow reply)", ks("b_eight", "b_extras"), "each item has its own row; the Bow left out fails C11"),
    ("Brief: the four zombies and the one animation (notes)", ks("b_zombie", "b_anim"), "a zombie or the animation left out or swapped fails its row"),
    ("Brief: how a level is won and lost and how many slots the tray has (notes; design page)", ks("b_win", "b_lose", "b_tray"), "a full tray as a loss, or 6 slots, fails"),
    ("Brief: what they can use for sound (notes; Calvin's sheet)", ks("b_use"), "each usable sound left out fails its row; the held-back sounds are graded on the list and the tickets (finding 2)"),
    ("Brief: when the music may start, and the start date (notes)", ks("b_music", "b_start"), "music from the start, or an earlier date, fails"),
    ("Hand-off list as a Google Sheet in Julia's Drive (ask 'the hand-off list as a sheet')", ks("sheet_doc"), "an idle run has no sheet; a CSV or Brian's own file fails"),
    ("Hand-off list: the seven columns and one row per line of Brian's pack list (notes)", ks("sheet_header", "sheet_volume"), "a dropped column or a row count other than 96 fails"),
    ("Hand-off list cells: State (5 samples), What's owed (4), Who has it (5), Board set (5), Ticket (1), Category (1), with the 96-row volume row (table rule)", ks("state", "owed_cell", "holder_cell", "board_set", "ticket_cell", "category_cell"), "each sampled cell with the stale or neighbouring value fails its row"),
    ("Tickets: each Owed line's ticket to Todo (notes): 5 samples and the volume row of 49", ks("move", "move_volume"), "a ticket left In Progress fails its sample; any count other than 49 fails C55"),
    ("Tickets: a comment on each of the 49 Owed tickets saying what is owed and who has it (notes); one row per write, split where the two parts come from different records", ks("comment_owed", "comment_holder", "comment_both"), "no comment fails; the wrong owed item or the wrong person fails that part's row"),
    ("Sharing: both files, view only, with everyone on the kickoff hold and PlayableX's intake address (notes)", ks("share"), "no share, or editor access, fails the row for that person and file"),
    ("The count for each state in the DM with Frederick (ask)", ks("dm"), "no message fails; another number fails that state's row"),
    ("Both links posted in the PlayableX channel (ask; prompt 'the links go in the PlayableX channel')", ks("post"), "a link sent only in the DM fails"),
    ("Links only once the files are ready (prompt 'once they're ready'): ordering", ks("order"), "a link posted before the file was written fails; no Outcome row can see the order"),
]
assert sorted(k for _, kk, _ in COVERAGE for k in kk) == list(range(1, 154))

PLAN = (WF / "09_Rubric_Writing_Plan.md").read_text()
gi = PLAN.index("## G"); G = PLAN[gi:]; gj = G.find("\n## ", 5); G = G[:gj] if gj > 0 else G
NEW_OF = collections.defaultdict(list)
for e in C.FIX:
    if e["from"] and e["new"]: NEW_OF[int(e["from"][1:])].append(int(e["new"][1:]))
SLOTS = json.loads((WF / "01_Gradable_Surface.json").read_text())["slots"]
PLAN_G = {}
for line in G.split("\n"):
    if line.startswith("| ") and not line.startswith("| Slot") and not line.startswith("|---"):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        PLAN_G[c[0]] = (c[1], [int(x) for x in re.findall(r"P(\d+)", c[5])], c[6])
def line_rows(name, fams=("comment_owed", "comment_holder", "comment_both", "move")):
    return [r["k"] for r in ROWS if r["line"] and r["line"]["name"] == name and r["fam"] in fams]
SAMPLED_OUT = {   # slot -> (line, note): State samples the round 1 Fix List cut to keep five per group
    "X3": ("Cactus Plant", "its recoloured class is sampled by Chainsaw (C31)"), "X3b": ("Cone", "its recoloured class is sampled by Chainsaw (C31)"),
    "X4": ("Cello", None), "X4b": ("Trumpet", None), "X5": ("Rocket sound", None), "X5b": ("Explosion sound", None), "X1b": ("Retro TV", None),
    "X2b": ("Iron", None), "C2": ("Fly Zapper", None)}
surface_lines, n_cov, n_disp = [], 0, 0
for s in SLOTS:
    sid = s["id"]; fact, ps, disp = PLAN_G[sid]
    news = sorted({k for p in ps for k in NEW_OF.get(p, [])})
    if sid in ("K1", "K2", "K4", "K5"):
        news = [k for k in news if ROWS[k - 1]["fam"] == "comment_owed"]     # the slot's selector reads the owed reason
    if news:
        surface_lines.append(f"| {sid} | {fact} | {', '.join(f'C{k}' for k in news)} | covered | — |"); n_cov += 1
    elif sid in SAMPLED_OUT:
        name, note = SAMPLED_OUT[sid]; lr = line_rows(name)
        why = note or f"the line's standing is still graded on its ticket by {', '.join(f'C{k}' for k in lr)}"
        surface_lines.append(f"| {sid} | {fact} | — | dispositioned | sampled out: the /rubric round 1 Fix List cut the State group to five samples (C29 to C33; cap of five per group, gate 15), "
                             f"so the {name} State cell has no row of its own; {why} |"); n_disp += 1
    elif sid == "B6":
        held = [r["k"] for r in ROWS if r["line"] and r["line"]["cls"] == "C2" and r["fam"] in ("owed_cell", "holder_cell", "comment_owed", "comment_holder")]
        surface_lines.append(f"| {sid} | {fact} | — | dispositioned | duplicate fact: the held-back Rocket and Explosion sounds are graded on the hand-off list and the tickets "
                             f"({', '.join(f'C{k}' for k in held)}). In the brief the only possible row accepts by absence, which fails Negative Criteria: the /rubric round 1 Fix List "
                             f"deleted both such rows and round 2 keeps the brief side as the Minor note on C21 to C23 (gate 7) |"); n_disp += 1
    else:
        assert disp, sid
        d2 = re.sub(r"P(\d+)", lambda m: " and ".join(f"C{k}" for k in NEW_OF[int(m.group(1))]), disp)
        surface_lines.append(f"| {sid} | {fact} | — | dispositioned | {d2} |"); n_disp += 1
assert len(surface_lines) == 52
TOTAL_W = sum(r["weight"] for r in ROWS)
MECH_W = sum(r["weight"] for r in ROWS if r["decided"] not in ("—", "", None))
assert TOTAL_W == 371

instr = cls_ks("comment_owed", "C4")
assert instr == [112, 114, 116, 118, 120, 122, 124, 126]
SPAN1 = "(also accepted: re-upload; re-zip or send the eight again)"
SPAN2 = "among the sounds PlayableX can use"
for k in instr + [36]: assert SPAN1 in ROWS[k - 1]["evidence"], k
for k in (21, 22, 23): assert SPAN2 in ROWS[k - 1]["title"], k
FINDINGS = [
    f"| 1 | {', '.join(f'C{k}' for k in instr)} (C36 carries the same wording and is not scored) | \"{SPAN1}\" | Eval 3 §2.1, a supporting field that widens acceptance | The evidence accepts 'send the eight again', which the title's 'owed back in the outgoing folder' does not: Brian's log {LOG} says the eight were only ever put in the folder, never sent. The answer path is unlikely, which is why the platform scored it Minor | P98 to P105 (the instrument comment rows) | `not_self_contained` | Minor, as /rubric round 2 scored it (the local table's default for the type is Major) |",
    f"| 2 | C21, C22, C23 | \"{SPAN2}\" | Eval 3 §2.7, the overly-broad test on each row alone | A brief that lists all five exported sounds as usable, the Rocket and Explosion sounds included, still passes each row. No brief row can close it: a row on the two held-back sounds accepts by absence (Negative Criteria) and a closed list rejects correct briefs, because Calvin's sheet {SOUND} also marks Background music and the combo-meter cue 'yes' | P23 to P25 | `overly_broad` | Minor, as /rubric round 2 scored it (carried from round 1 as an open problem; the local table's default for the type is Major) |",
]

GROUPS = [
    ("State cells (spot-check group)", f"{rng(ks('state'))}; volume row C28 (96 rows)", "five samples: two Owed by a later record, one recoloured Ready, one plain Ready, one Delivered; within the cap of five"),
    ("What's owed cells (spot-check group)", f"{rng(ks('owed_cell'))}; volume row C28", "four samples, one per later record (Marcus's post, Robert's note, Brian's log, Calvin's sheet)"),
    ("Who has it cells (spot-check group)", f"{rng(ks('holder_cell'))}; volume row C28", "five samples across Brian, Claire and Calvin"),
    ("Board set cells (spot-check group)", f"{rng(ks('board_set'))}; volume row C28", "five samples: the Bow swap both ways, one Default, one Extra, one empty"),
    ("Ticket and Category cells (spot-check groups of one)", f"{rng(ks('ticket_cell', 'category_cell'))}; volume row C28", "one sample each, copied from the pack list"),
    ("Moves to Todo (one template: one state change to Todo per Owed line)", f"{rng(ks('move'))}; volume row C55 (49)", "five samples and the one volume row of the group; the count row is the group's control, not a count over separate writes (count-bundle-v1)"),
    ("Ticket comments", f"{rng(ks('comment_owed', 'comment_holder', 'comment_both'))}", "not sampled: each of the 49 comments has its own row or rows (one row per write), so there is no group"),
    ("Shares", f"{rng(ks('share'))}", "not sampled: one row per person and file"),
    ("Overlap or cascade groups", "none", "rows that fail together share a root cause (one missed record), not one embedded condition; /rubric round 2 found no duplicate, overlap or cascade group"),
    ("Predicted all-fail", "none (0 rows)", "every deciding record is readable by Julia and was opened by a baseline run; the three rows that failed all six runs (C55, C147, C148) are real misses, classified VALID in stage 11"),
]

n_minor = len(instr) + 3
DIMS = [
    ("Overall Rubric Quality", f"0 Major · 0 Moderate · Minor on {n_minor} of 153 rows ({n_minor / 153:.1%})", "any Major or Moderate fails; Minor over 10% fails; 5 to 10% is NON-FAIL 3", "NON-FAIL 3 (the /rubric round 2 score)"),
    ("Criteria Weights", "0 rows one level off by the platform's reading (round 2: every row's weight matches its work kind). The scenario's surface bands differ on 37 rows; see Certification status", "over 10% one level off, or any row two levels off, fails", "PASS"),
    ("Known data issue", "0 rows rest on a listed card", "any row on a Don't-grade value fails", "PASS"),
    ("Category Balance", "151 Outcome · 2 Process", "at least 1 Outcome, Process at most 50%", "PASS"),
    ("Process Rubrics", "2 Process rows (C152, C153), both pass the three conditions; no ordering dependency without a check", "2 or more absent, or any invalid, fails", "PASS"),
    ("Agent-Centric Phrasing", "153 of 153 titles are 'The Agent' and an action; no tool name in a title", "an artifact subject or a tool name fails", "PASS"),
    ("Negative Criteria", "0 of 153 rows an idle Agent passes; no prohibition-only title", "1 or more fails", "PASS"),
    ("Predicted all-fail", "0", "tolerance 0", "PASS"),
    ("Schema · coverage · accuracy · contradiction (repair gates)", "schema pass (153 of 153, five fields) · 0 coverage holes · 0 incorrect literals · 0 contradictions", "any failure blocks", "PASS"),
]

SELF_GENERAL = [
    ("Re-read as /rubric, phases 1 to 5", "done", "the local check could be softer than /rubric because it knows the verdict", f"The verdict is on record for this exact file: eval_reports/6aea4c201e1fa1ddfdd0a25d_3_rubric (1).md, Reviewed JSON SHA-256 {RSHA[:12]}; both of its findings are copied here with its severities, nothing is dropped", "none"),
    ("Pre-verdict sweep (5.0)", "done", "one absent requirement, one non-atomic row, one category mislabel, one hard-coded title, one cascade group, one vague exemplar or one prohibition-only title could still be in the 153 rows", "Coverage table: 16 requirement groups, each with rows; the 34 split comment rows now grade one part each; C152 and C153 are the only Process rows; hg.py rubric-lint returns 0 findings; no title has a negation that carries the acceptance", "none"),
    ("Validity gate", "clean", "a validity defect (incorrect, unauthorized, unobservable, contradiction, coverage hole, predicted all-fail) could hide behind the NON-FAIL score", "v3.rubric_evidence re-reads every cited source value and path; persona_view shows YES for every scoped deciding record; the baseline runs opened each one (stage 11, 11_AF_Justification.md)", "none"),
    ("Verifier results against the rows", "consistent", "a row could be failing correct runs (a false negative of the rubric) rather than grading a real miss", "Pass patterns follow the records each run opened: rows decided by Marcus's post pass only in run-4, by Robert's note only in run-6, by Brian's log only in run-5 (asserted in plan/rubric/build_check.py); 70 rows pass in all six runs; C11, C43 and C44 fail in run-4 and run-6, which kept Dynamite in the eight", "none"),
    ("Recount", "done", "the tally could double count a row or skip the not-scored one", f"Minor rows: {', '.join(f'C{k}' for k in instr)} and C21 to C23 = {n_minor} of 153 = {n_minor / 153:.1%}; C36 is noted, not scored, as in the platform report; predicted all-fail recounted from recorded defects: 0", "none"),
    ("Fixes", "none proposed", "the two Minor findings could be fixed locally before the next stage", "Not applied: the platform marked the instrument-row fix optional and 'revised after check' with an open problem, it changes no baseline grade (runs 1 to 4 and 6 wrote no comment on DES-379 to DES-386; run-5's wording passes both versions), and any rubric edit now would need the verifier again. The sound-row note has no rubric fix (it needs a data change upstream)", "none"),
]


def esc(s): return s.replace("|", "/").replace("\n", " ")

self_rows = []
for r in ROWS:
    a, b, res = REV[r["k"]]
    verdict = "finding 1 (Minor)" if r["k"] in instr else "finding 2 (Minor)" if r["k"] in (21, 22, 23) else "cleared"
    self_rows.append(f"| {r['cid']} | {verdict} | (a) could a valid answer fail? {esc(a)}. (b) could a wrong answer pass? {esc(b)} | {esc(res)}; {tally(r['k'])} | none |")

change_counts = collections.Counter(e["change"] for e in C.FIX)
doc = f"""# 09 Rubric Check — julia_zm3d_playable_brief (rev2; after /rubric round 2 and the baseline verifier)
Checked 2026-11-13 · Criteria 153 (builder minimum 5: ok) · Plan 2026-11-12 (09_Rubric_Writing_Plan.md, rubric-writing gate PASS; written for the 126-row draft and carried to the 153 rows through plan/rubric/fix_round1_map.json) · 09_Rubrics.json sha256 {RSHA[:12]}

JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass (153 objects, five non-blank fields each, category Outcome/Process, weight 1/3/5)
Readiness for /rubric: NON-FAIL-RISK — /rubric has already given its verdict on this exact file: round 2, NON-FAIL, Score 3 (eval_reports/6aea4c201e1fa1ddfdd0a25d_3_rubric (1).md). This check records that verdict, re-verifies the rows locally and adds the baseline verifier's results; it changes nothing in 09_Rubrics.json.

Order of work on this task: the rubric was drafted (126 rows), sent to /rubric (round 1 FAIL), repaired from the Fix List (153 rows: {change_counts['split']} split parts, {change_counts['added']} added, {change_counts['deleted']} deleted), passed /rubric round 2 as NON-FAIL 3, and graded by the baseline verifier (six runs). This local check was run after those steps, on 2026-11-13, because stage 11 needs it; it is a check of the final file, not a prediction made before the platform review.

## Coverage
| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |
|---|---|---|
""" + "\n".join(f"| {req} | {rng(kk)} | covered: {how} |" for req, kk, how in COVERAGE) + f"""

Unauthorized criteria: none

Every requirement comes from the prompt or from what it hands over: Frederick's message {ASK} (the prompt's 'Frederick's playable message from yesterday') and his hand-off notes {NOTES} (the message's 'My hand-off notes say what goes in the brief, what counts as ready, what to do with the tickets and who gets the files').

## Coverage — gradable surface
| Surface slot | Stable fact ID | Criteria | Covered / dispositioned / gap | Disposition reason (evidence) |
|---|---|---|---|---|
""" + "\n".join(surface_lines) + f"""

{len(SLOTS)} slots: {n_cov} covered, {n_disp} dispositioned. Nine State slots lost their row when the platform's round 1 Fix List cut the State group to five samples; one brief slot (B6) lost its rows when the Fix List deleted the two accept-by-absence rows; three count slots were already dispositioned in the plan.
Mechanism share: {MECH_W / TOTAL_W:.0%} of the criteria weight ({MECH_W} of {TOTAL_W}; reported, not gated)

## Findings
| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |
|---|---|---|---|---|---|---|---|
""" + "\n".join(FINDINGS) + f"""

Both findings are the platform's own (round 2, Issues Found 1 and 2), copied with its severities. No other finding: the eval lint (`hg.py rubric-lint`) returns 0 findings and the platform-rule lint (`platform_delta_lint.py rubric`) passes.

## Round history
| Round | Result | What changed |
|---|---|---|
| /rubric round 1 (126 rows, sha256 1c44f4afdac1) | FAIL, Score 1 | possessive titles, two accept-by-absence rows, a 13-row State group, bundled owed-and-holder comment rows, 16 weights |
| Repair (plan/rubric/apply_rubric_fix_round1.py) | 153 rows | Fix List titles pasted unchanged; 11 rows deleted, 34 comment rows split, 4 rows added, 16 weights moved; the 30 rows the report did not list kept their bytes |
| /rubric round 2 (153 rows, sha256 {RSHA[:12]}) | NON-FAIL, Score 3 | two Minor findings (above); every other dimension 5; predicted all-fail PASS |
| Baseline verifier (six runs on rev2) | 73, 73, 73, 98, 93, 99 of 153 | three rows failed all six runs (C55, C147, C148), all VALID in stage 11 |

## Overlap groups · Spot-check groups · Predicted all-fail
| Group / row | Members / basis | Shared condition / reason |
|---|---|---|
""" + "\n".join(f"| {a} | {b} | {c} |" for a, b, c in GROUPS) + f"""

## Dimensions
| Dimension | Count / % | Threshold | Status |
|---|---|---|---|
""" + "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in DIMS) + f"""
Threshold margin: with 153 rows, 15 Minor rows is the last count inside the NON-FAIL band (16 would be over 10%); one Major or Moderate row would fail Overall Quality; 16 one-level weight differences would fail Weights.

## Self-review

**1. Re-read as /rubric** (3_Rubrics_Eval.md phases 1 to 5, in order), with the pre-verdict sweep, on the file the platform reviewed. Schema: 153 objects, five fields each. Coverage: the 16 requirement groups above. Per-row lint: every title re-read alone for its value, its accepted alternatives and a near miss (table below). Set level: spot-check groups within five samples, each with its volume row; no count over separate writes except the move group's one volume row; comments and shares have one row per write. Calibration against Evals/references/rules/rubric_qc_examples.md: do-nothing (every row needs a write or a message; an idle Agent fails all 153), count format (C28, C55 and the three DM counts are exact numbers), LITERAL keys (DES keys and the channel id are in the titles), PT or UTC day (C25 grades a date only, with or without the year), reachability (every deciding source is PROMPT_LINKED through Frederick's notes and re-checked by v3.rubric_evidence), OE conflict (the /oe-passed path, 08_Oracle_Events.md, passes every row: OE 22 writes the 96 rows, OE 31 to 128 the 49 moves and comments, OE 129 the counts, OE 130 the links).

**2. Counter-readings.** One row per criterion below: a valid alternative tried against the title alone (false negative?) and a plausible near miss (false positive?), each resolved with the record that decides it. The two findings are checked the other way (false positive?): finding 1 is real but its answer path is unlikely (no baseline run wrote 'send the eight again'; run-5's comments say the file is owed back in the outgoing folder); finding 2 is real and has no rubric fix.

**3. Re-verified values.** Every value a finding or a clearance rests on was read again from its record: seeded rows from 01_Universe_Inject.sql through the gate's own reader (tools/v3_artifact_checks.py, the same parse the gate uses), base records through tools/hg.py (PlayableX's rule slack messages/C08H78VJG80/2025-09.json pointer /6; the design page confluence_working.json pointer /pages/16). The values, their paths from the prompt and their dates are in Working_Files/00_V3_Authoring_Evidence.json ({len(ev['rubric_rows'])} rows, {len(C._cache)} distinct source records, {len(facts)} fact ids, {sum(1 for v in facts.values() if v == 2)} graded twice across the list and the ticket, none three times).

**4. Recount.** Predicted all-fail from recorded defects: 0. Tally from the Findings table: 0 Major, 0 Moderate, Minor on {n_minor} rows ({n_minor / 153:.1%}); C36 not scored; no overlap group.

**5. Fixes.** None proposed here (see the last general row).

| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |
|---|---|---|---|---|
""" + "\n".join(f"| {a} | {b} | {c} | {d} | {e} |" for a, b, c, d, e in SELF_GENERAL) + "\n" + "\n".join(self_rows) + """

Unresolved: none in the rows; the certification item below is open upstream.

## Certification status
Run on 2026-11-13, `stage_gate.py rubric-check` passes its content checks (of 28 checks, 24 pass, 3 are warnings and 1 blocks; passing: structure, criteria count, category balance, quoted spans, issue types, dimensions, readiness line, the validity gate, surface coverage, v3.rubric_evidence on all 153 rows, fact duplication, the 153 counter-readings, the eval lint and the platform-rule lint). It is not certified. `readiness.hardness_review` refuses the rubric-stage design review (Working_Files/hardness_reviews/rubric.json) with one kind of blocker, 37 times: a row carries weight 5 while the scenario's gradable surface gives the slot it covers a band of 3. The rows are the move of DES-367 (C50; slot W4, interpretation), the 34 what-is-owed comment rows (slots K1, K2, K4 and K5, interpretation) and the Owed and Ready counts in the DM (C147, C148; slots W1, W2, A1 and A2, calculation). These weights are the platform's: the /rubric round 1 Fix List set them to 5 and round 2 scored Criteria Weights 5. The surface is a scenario artifact, so bringing its bands in line is a `/create-scenario --revise` decision, and it re-gates every stage that hashes the surface. Nothing in 09_Rubrics.json is changed here, and no PASS block is pasted.

## Reminders
- An all-Outcome set is normal; the two Process rows are the ordering checks the platform's Fix List wrote.
- The rubric is not edited after the verifier ran. If the optional instrument-row fix is ever applied, re-run this check, /rubric and the verifier.
"""
(WF / "09_Rubric_Check.md").write_text(doc)
print(f"wrote 09_Rubric_Check.md ({len(doc)} chars) · V3 evidence: {len(ev['rubric_rows'])} rows, {len(C._cache)} source records, facts {len(facts)} (twice: {sum(1 for v in facts.values() if v == 2)})")
print(f"surface: {n_cov} covered, {n_disp} dispositioned · mechanism share {MECH_W}/{TOTAL_W} = {MECH_W / TOTAL_W:.0%} · Minor rows {n_minor} ({n_minor / 153:.1%})")

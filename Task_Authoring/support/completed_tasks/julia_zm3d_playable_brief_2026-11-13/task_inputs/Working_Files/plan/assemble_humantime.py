#!/usr/bin/env python3
"""Assemble Working_Files/05_Human_Time_Worksheet.md (first pass, after the prompt). Volumes are read from
plan/out/humantime_volumes.json (measured through tools/hg.py as the persona) and from the injected SQL rows; minutes
are volume x a stated rate and must sum to an hours figure on a 0.25 step, or the script stops."""
import hashlib, json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
ROOT = TASK.parents[1]
OUT = HERE / "out"
TOOLS = TASK.parent / "tools"
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(TOOLS))
import design_model as M
import planned_texts as TXT
from base_check import parse_sql

ctx = json.loads((WF / "00_Task_Context.json").read_text())
man = json.loads((WF / "01_Hardness_Manifest.json").read_text())
vol = json.loads((OUT / "humantime_volumes.json").read_text())
prompt = (TASK / "04_Prompt.txt").read_text()
sql = (TASK / "01_Universe_Inject.sql").read_bytes()
rows = [r for r in parse_sql(sql.decode()) if r["op"] == "insert"]
def n_rows(table): return sum(1 for r in rows if r["table"] == table)
S, B, C = M.SEED, M.BASE, M.COUNTS
sl = vol["slack"]
def w(ch, key): return sl[ch]["windows"][key]
SKIM = {"the PlayableX channel (all of it)": w(M.VENDOR_CH, "all"), "#zombie-design": w(M.DESIGN_CH, "22 to 30 Sep"), "#zombie-art": w(M.ART_CH, "22 to 30 Sep"),
        "#zombie-match3d": w(M.MATCH3D_CH, "22 to 30 Sep"), "#zm-animations": w(M.ANIM_CH, "22 to 30 Sep"), "DM with Frederick (Sep)": w(M.DM_FRED, "Sep 2025"),
        "DM with Robert": w(M.DM_ROBERT, "22 to 30 Sep"), "DM with Brian": w(M.DM_BRIAN, "22 to 30 Sep")}   # rev2: Robert's note is in his DM; Claire's DM holds nothing seeded
seeded_slack = n_rows("slack.slack_messages")
skim_total = sum(SKIM.values()) + seeded_slack
reach = subprocess.run([sys.executable, "-B", str(TOOLS / "persona_view.py"), "reach", "julia_lawson"], capture_output=True, text=True, cwd=ROOT).stdout
import re
owned = int(re.search(r"DRIVE\s+owned=(\d+)", reach).group(1)); shared = int(re.search(r"shared-with=(\d+)", reach).group(1))
seeded_files = n_rows("gdrive.drive_files")
drive_total = owned + shared + seeded_files
n_lines, n_owed = M.N_LIST, C["Owed"]
over = {c: len(M.members(c)) for c in ("A1", "A2", "C1", "C2", "C4")}
n_over = sum(over.values())
prs = vol["github"]["prs_created_22_to_30_sep_all_repos"]
zom97 = vol["linear"]["children_of_ZOM-97"]
def r5(x): return int(5 * round(x / 5))     # rate-derived minutes to the nearest 5: the rates are approximate
skim_min = r5(skim_total / 3000 * 60)
drive_min = r5(drive_total / 450 * 60)

T = [   # (sub-task, kind, volume, rate, minutes)
 ("Read the request, Frederick's DM and his hand-off notes", "read", f"3 records: prompt {len(prompt)} chars, DM {len(TXT.ASK)} chars, notes {len(TXT.NOTES)} chars with 3 state tests", "careful read: the tests are applied to every line", 30),
 ("Read Brian's pack list row by row", "read", f"{n_lines} rows, 5 columns", "about half a minute per row", 45),
 ("Skim Slack where the playable and its assets are discussed", "read", f"{skim_total} messages: " + ", ".join(f"{k} {v}" for k, v in SKIM.items()) + f"; {seeded_slack} seeded (Julia is a member of each)", "≈ 3,000 messages/h (worked-example skim anchor)", skim_min),
 ("Read the vendor's threads past their apparent end: formats and asset list, the pause and the new start, the first playable's sound exchange", "read", f"3 threads in a channel of {w(M.VENDOR_CH, 'all')} messages ({w(M.VENDOR_CH, 'Mar to Apr 2025')} of them from March and April)", "≈ 20 min each (decisive-thread anchor)", 60),
 ("Open each pack ticket, read Brian's note, apply the three tests", "read", f"{n_lines + 1} tickets (the pack ticket and {n_lines} children), {n_rows('linear.linear_comments')} notes", "3 min each: one ticket, one short note (below the 8 to 15 min anchor, which is for 2 to 3 surfaces)", r5(3 * n_lines)),
 ("List Julia's Drive for the notes, the pack list, the deck and anything else about the pack", "read", f"{drive_total} files ({owned} owned, {shared} shared, {seeded_files} seeded)", "≈ 450 items/h", drive_min),
 ("Read Calvin's sound sources sheet and Brian's log of the outgoing folder against the tickets", "read", f"{len(TXT.C2_SHEET_GRID) - 1} sheet rows, {len(TXT.C4_LOG.splitlines()) - 2} dated log lines", "15 min for both", 15),
 ("Find the pull requests since the first zip and confirm what each changed", "read", f"{prs} pull requests created 22 to 30 Sep", "≈ 40 min (worked-example PR anchor)", 40),
 ("Read the design page and its comments for the tray and the loss rule; the reference-level deck", "read", f"1 page, 2 comments, {len(TXT.DECK_SLIDES)} slides", "20 min", 20),
 ("Find the kickoff hold and its attendees, and the vendor's intake address", "read", "1 event with 4 attendees, 1 contact", "10 min", 10),
 ("T1 Thursday's exports look ready until a colleague's post is read against the vendor's format rule", "dead end", f"{over['A1']} tickets, 1 post, 1 rule message", "≈ 20 min (decisive-thread anchor)", 20),
 ("T2 Friday's bathroom files look ready until Robert's note", "dead end", f"{over['A2']} tickets, 1 DM message", "15 min", 15),
 ("T3 three recoloured models: Owed on Robert's post until the log says they went again", "dead end", f"{over['C1']} tickets, Robert's post, the log entry", "15 min", 15),
 ("T7 the zipped instruments: the folder log says the zip will not unpack", "dead end", f"{over['C4']} tickets, 1 log line", "10 min", 10),
 ("T4 two sounds are not ours to pass on", "dead end", f"{over['C2']} tickets, 2 sheet rows", "10 min", 10),
 ("T5 the board's eight: the first list against a later reply under another post", "dead end", "2 posts, 1 thread of 3 messages", "≈ 20 min (decisive-thread anchor)", 20),
 ("T8, T12 stale start dates and the first playable's format rule", "dead end", "3 dates, 2 rule messages", "5 min each pair", 10),
 ("T9 the six-slot proposal on the design page", "dead end", "2 comments", "5 min", 5),
 ("T10, T16 the zombie pack 'not exported correctly', the duck and the rocket launcher", "dead end", "3 vendor messages, 2 tickets", "5 min each", 15),
 ("T11, T17 Leonard's Playable Kickoff card and his Playable Feedback doc", "dead end", "1 card, 1 doc", "5 min each", 10),
 ("T13, T14, T15 the board on the reference-level deck and earlier board ideas", "dead end", "1 slide, 3 messages", "10 min", 10),
 ("T18 other objects in the recolour pull requests", "dead end", f"3 object names checked against {n_lines} lines", "5 min", 5),
 ("T19 object tickets with the same titles as pack lines", "dead end", f"{zom97} tickets under one parent", "≈ 450 items/h, then 3 opened", 10),
 ("T6 board set for the lines that are not board items", "dead end", "12 lines", "5 min", 5),
 ("Go back over the lines each later statement overturns: state, what is owed, who has it", "re-read", f"{n_over + 2} lines ({' + '.join(str(v) for v in over.values())} states, 2 board-set cells)", "2 min each", r5(2 * (n_over + 2))),
 ("Type the hand-off list", "write", f"1 sheet, {n_lines} rows × 7 columns", "1.25 min per row", int(1.25 * n_lines)),
 ("Write the brief", "write", "1 doc, 10 required facts", "60 min", 60),
 ("Move each Owed line's ticket to Todo and write its comment", "write", f"{n_owed} state changes, {n_owed} comments", "3 min per ticket (comments repeat within a group)", r5(3 * n_owed)),
 ("Share both files", "write", "2 files × 4 recipients = 8 shares", "1 min each", r5(8)),
 ("Send Frederick the count for each state; post both links in the vendor channel", "write", "2 messages", "5 min each", 10),
]
total = sum(t[4] for t in T)
hours = total / 60
assert abs(hours * 4 - round(hours * 4)) < 1e-9, f"{total} min = {hours} h is not on a 0.25 step"
def table(head, rws): return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(str(c) for c in r) + " |" for r in rws])
def grp(kind, pred=lambda t: True): return sum(t[4] for t in T if t[1] == kind and pred(t))
reads = grp("read"); dead = grp("dead end"); reread = grp("re-read"); writes = grp("write")
cond = [
 f"- Rules and list: the message, the notes, {n_lines} pack-list rows {T[0][4] + T[1][4]} min",
 f"- Slack: skim {skim_total} messages at 3,000/h, 3 vendor threads read through {T[2][4] + T[3][4]} min",
 f"- {n_lines} tickets, one note each, 3 min each {T[4][4]} min",
 f"- Drive listing {drive_total} files, sound sheet, folder log {T[5][4] + T[6][4]} min",
 f"- {prs} pull requests, design page, deck, kickoff hold, contact {T[7][4] + T[8][4] + T[9][4]} min",
 f"- 14 dead ends: notes that look ready, the first board list, stale dates, look-alike tickets and card {dead} min",
 f"- Re-deciding {n_over + 2} overturned lines {reread} min",
 f"- Sheet of {n_lines} rows and the brief {T[25][4] + T[26][4]} min",
 f"- {n_owed} ticket moves with comments, 8 shares, 2 messages {T[27][4] + T[28][4] + T[29][4]} min",
 f"- Total {total:,} min = {hours:.2f} h",
]
assert sum(int(re.search(r"(\d[\d,]*) min$", l).group(1).replace(",", "")) for l in cond[:-1]) == total, "condensed lines do not add up"
cond_text = "\n".join(cond)
calls = sum(x["calls"] for x in man["call_budget"])
CLOCK = ctx["universe"]["clock_line"].replace("Clock: ", "")
sha = hashlib.sha256(prompt.encode()).hexdigest()[:12]
sqlsha = hashlib.sha256(sql).hexdigest()[:12]

doc = f"""# Human Time Worksheet — {M.SLUG}

Pass: first        Tier: Long-Horizon
Universe: synth-cut · Clock: {CLOCK}
Hours: {hours:.2f}

Basis:
- The work 04_Prompt.txt asks for (sha256 {sha}): do everything Frederick's Sep 30 message asks, which covers a brief, a hand-off list with a state for every line of the pack, ticket moves and comments for the lines that are owed, sharing, the count for each state, and the two links.
- The work is done by hand in Julia's own accounts: no search, scripts or AI.
- Counts come from {M.REV} (01_Universe_Inject.sql {sqlsha}, solver/truth.json): {n_lines} lines, Delivered {C['Delivered']}, Ready {C['Ready']}, Owed {C['Owed']}. The person does not start out knowing where anything is.
- Friction: none (03_Error_Async_Config.txt), so there is no workaround line.
- Rows computed as volume × rate are rounded to the nearest 5 minutes (the rates are approximate); the others are stated estimates.

""" + table(["Sub-task", "Kind (read / dead end / workaround / re-read / write)", "Volume (measured, persona view)", "Rate", "Minutes"], T + [("Total", "", "", "", f"{total} = {hours:.2f} h")]) + f"""

Tier check: in band (Long-Horizon ≈ 12–24 h; {hours:.2f} h). No trigger.
- Reads {reads} min, dead ends {dead} min, re-reading {reread} min, writes {writes} min.
- The manifest's call budget is {calls}; most of the hours are {n_lines} manual decisions, a {n_lines}-row sheet typed by hand and {2 * n_owed} per-ticket writes, which an agent makes in far fewer minutes each.

Condensed breakdown (one line per sub-task group, facts only; the human types the reasoning in their own words):
{cond_text}

Condensed breakdown length: {len(cond_text)} characters (field accepts 50–2,000)

Sources measured: hg.py and persona_view.py, listed here.
- hg.py search search slack '17' --key ts with --file messages/CHANNEL/*.json for {M.VENDOR_CH}, {M.DESIGN_CH}, {M.ART_CH}, {M.ANIM_CH}, {M.DM_FRED}, {M.DM_CLAIRE} and {M.DM_BRIAN}, and '175' on messages/{M.MATCH3D_CH}/2025-09.json; windows are Pacific days (22 Sep 00:00 PT to 1 Oct 00:00 PT). Scan complete for each.
- persona_view.py can-see julia_lawson slack for those conversations (reach table, YES for each); persona_view.py reach julia_lawson: Drive owned {owned}, shared {shared}.
- hg.py search search github '2025-09-' --pointer /pull_requests --key created_at ({prs} created 22 to 30 Sep); hg.py search search linear ZOM-97 --key parent_id ({zom97}).
- 01_Universe_Inject.sql rows ({M.REV}), parsed with tools/base_check.parse_sql, never run: {n_rows('linear.linear_issues')} Design-team tickets, {n_rows('linear.linear_comments')} notes, {seeded_slack} Slack messages, {seeded_files} Drive files, 1 sheet of {n_lines} rows.
- Raw figures: plan/out/humantime_volumes.json.

## Self-review

Checked in order against `10_Long Horizon Guidelines - V2.md` §5 and §10, the Pre-QC list and the field's own text.

""" + table(["Area", "Counter-reading", "Evidence that resolves it", "Verdict"], [
    ("Inflated", f"Three minutes for each of {n_lines} tickets and {3 * n_owed} minutes of ticket writes are padding.", f"each line has its own ticket and note ({M.BY_NAME[M.LINES[0]['name']]['ticket']} to {M.LAST_CHILD}) and every Owed line needs a move and a comment (hand-off notes {S['notes']['id']}); the per-record rate is below the 8 to 15 min anchor because there is one surface, and the reason is stated on the row", "holds"),
    ("Solution-path estimate", "The table assumes the person already knows where the six later statements are.", f"each has a dead-end line (T1, T2, T3, T4, T5, T7) and the places are found by the skim and listing rows: {skim_total} messages, {drive_total} Drive files, {prs} pull requests ({S['a1_post']['id']}, {S['c4_log']['id']})", "holds"),
    ("Evaluator-wide volume", "The Slack and Drive counts could be universe-wide, not Julia's.", f"only conversations she is a member of are counted (persona_view can-see YES for {M.VENDOR_CH}, {M.MATCH3D_CH}, {M.DM_CLAIRE}); Drive is her owned and shared files from persona_view reach, plus the seeded files shared with her ({S['notes']['id']})", "holds"),
    ("Tier mismatch", f"{hours:.2f} h could sit outside Long-Horizon.", f"12 to 24 h is the band; the manifest's call budget is {calls} with {n_lines} per-line reads ({M.PACK_TICKET}); no trigger, nothing tuned", "holds"),
    ("Linter reading", "From a 46-word prompt and the SQL alone, 19 hours could look more than three times too high.", f"the SQL shows {n_rows('linear.linear_issues')} tickets with {n_rows('linear.linear_comments')} notes under {M.PACK_TICKET} and a {n_lines}-row list ({S['tracker']['id']}); the condensed breakdown names those volumes, the {n_owed} ticket writes and the dead ends", "holds; the reasoning must name the volumes"),
]) + f"""

Every volume was measured in this run (sources above); nothing is carried from the dossier. The sum was recomputed by the generator ({total} min) and the character count taken from the condensed lines as printed. Unresolved: none. To refresh after the Oracle Events exist and again after the baseline.
"""
out = WF / "05_Human_Time_Worksheet.md"
out.write_text(doc)
print("wrote", out.name, "·", total, "min =", f"{hours:.2f} h ·", len(cond_text), "chars · skim", skim_total, "msgs · drive", drive_total)

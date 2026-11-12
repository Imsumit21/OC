#!/usr/bin/env python3
"""Post-baseline refresh of the human-time estimate.

Writes Working_Files/05_Human_Time_Worksheet.md (facts and arithmetic) and the task slot 05_Human_Time.md (the hours
and the sub-task justification for the Human Time Estimate screen). Every volume is measured again in this run through
tools/hg.py and tools/persona_view.py as Julia (raw figures: humantime_gen/out/volumes.json); nothing is carried from
the first pass. Minutes are volume x a stated rate and must sum to an hours figure on a 0.25 step, or the script stops.
Re-running drops the pasted stage-gate block; paste the gate again afterwards."""
import datetime as D, hashlib, json, os, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
BUNDLE = TASK.parent
ROOT = BUNDLE.parent
TOOLS = BUNDLE / "tools"
sys.path.insert(0, str(WF / "plan")); sys.path.insert(0, str(TOOLS))
import design_model as M          # noqa: E402
import planned_texts as TXT       # noqa: E402
from base_check import parse_sql  # noqa: E402

ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(TASK))
SLACK_DIR = ROOT / "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages"
PT = D.timezone(D.timedelta(hours=-7))          # Pacific daylight time holds for every window used here
ts = lambda y, m, d: D.datetime(y, m, d, tzinfo=PT).timestamp()
SEP22, OCT1, SEP1 = ts(2025, 9, 22), ts(2025, 10, 1), ts(2025, 9, 1)


def run(*args):
    p = subprocess.run([sys.executable, "-B", *[str(a) for a in args]], capture_output=True, text=True, cwd=ROOT, env=ENV)
    return p.stdout


def hg(*args):
    d = json.loads(run(TOOLS / "hg.py", "search", "search", *args, "--limit", "20000", "--compact"))
    assert d.get("scan_complete") is True and not d.get("errors"), (args, "scan incomplete")
    return [m["text"] for m in d["matches"]]


def slack_ts(ch):
    out = []
    for f in sorted((SLACK_DIR / ch).glob("*.json")):          # listing the month files is a read; counts come from hg.py
        out += [float(t) for t in hg("slack", "17", "--key", "ts", "--file", f"messages/{ch}/{f.name}")]
    return out


def can_see(ch):
    out = run(TOOLS / "persona_view.py", "can-see", "julia_lawson", "slack", ch)
    assert re.search(rf"julia_lawson slack {ch}: YES", out), (ch, out[:200])
    return "YES"


# ------------------------------------------------------------------ measure
CHANNELS = [(M.VENDOR_CH, "the PlayableX channel (all of it)", "all"), (M.DESIGN_CH, "#zombie-design", "w"),
            (M.ART_CH, "#zombie-art", "w"), (M.MATCH3D_CH, "#zombie-match3d", "w"), (M.ANIM_CH, "#zm-animations", "w"),
            (M.DM_FRED, "DM with Frederick (Sep)", "sep"), (M.DM_ROBERT, "DM with Robert", "w"), (M.DM_BRIAN, "DM with Brian", "w")]
VOL = {"windows": "Pacific days: 22 Sep 2025 00:00 PT to 1 Oct 2025 00:00 PT; September = 1 Sep 00:00 PT to 1 Oct 00:00 PT", "slack": {}}
SKIM = {}
for ch, label, mode in CHANNELS:
    stamps = [t for t in slack_ts(ch) if t < OCT1]
    n = len(stamps) if mode == "all" else sum(1 for t in stamps if (SEP1 if mode == "sep" else SEP22) <= t)
    SKIM[label] = n
    VOL["slack"][ch] = {"label": label, "counted": n, "total_before_1_oct_pt": len(stamps), "can_see": can_see(ch)}
vend = [t for t in slack_ts(M.VENDOR_CH) if t < OCT1]
MAR_APR = sum(1 for t in vend if ts(2025, 3, 1) <= t < ts(2025, 5, 1))
VOL["slack"][M.VENDOR_CH]["mar_apr_2025"] = MAR_APR
reach = run(TOOLS / "persona_view.py", "reach", "julia_lawson")
owned = int(re.search(r"DRIVE\s+owned=(\d+)", reach).group(1)); shared = int(re.search(r"shared-with=(\d+)", reach).group(1))
pr_dates = hg("github", "2025-09-", "--pointer", "/pull_requests", "--key", "created_at")
prs = sum(1 for s in pr_dates if SEP22 <= D.datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp() < OCT1)
zom97 = len(hg("linear", "ZOM-97", "--key", "parent_id"))
VOL.update(drive={"owned": owned, "shared": shared}, github={"prs_created_sep_2025": len(pr_dates), "prs_created_22_to_30_sep_pt": prs},
           linear={"children_of_ZOM-97": zom97})

sql = (TASK / "01_Universe_Inject.sql").read_bytes()
rows = [r for r in parse_sql(sql.decode()) if r["op"] == "insert"]
n_rows = lambda table: sum(1 for r in rows if r["table"] == table)
seeded_slack, seeded_files = n_rows("slack.slack_messages"), n_rows("gdrive.drive_files")
VOL["sql"] = {"slack_messages": seeded_slack, "drive_files": seeded_files, "linear_issues": n_rows("linear.linear_issues"),
              "linear_comments": n_rows("linear.linear_comments")}
(HERE / "out").mkdir(exist_ok=True)
(HERE / "out" / "volumes.json").write_text(json.dumps(VOL, indent=1) + "\n")

# first-pass figures are leads only: report where the fresh measurement differs
OLD = json.loads((WF / "plan/out/humantime_volumes.json").read_text())
old_skim = {M.VENDOR_CH: OLD["slack"][M.VENDOR_CH]["windows"]["all"], M.DM_FRED: OLD["slack"][M.DM_FRED]["windows"]["Sep 2025"]}
old_skim.update({ch: OLD["slack"][ch]["windows"]["22 to 30 Sep"] for ch in (M.DESIGN_CH, M.ART_CH, M.MATCH3D_CH, M.ANIM_CH, M.DM_ROBERT, M.DM_BRIAN)})
MOVED = [(label, old_skim[ch], SKIM[label]) for ch, label, _ in CHANNELS if old_skim[ch] != SKIM[label]]

# ------------------------------------------------------------------ baseline and Oracle Events (refresh inputs)
ctx = json.loads((WF / "00_Task_Context.json").read_text())
man = json.loads((WF / "01_Hardness_Manifest.json").read_text())
prompt = (TASK / "04_Prompt.txt").read_text()
DS = json.loads((WF / "12_difficulty_stats.json").read_text())
CALLS = [r["tool_calls"] for r in DS["per_rollout"]]
assert len(CALLS) == 6 and not DS["golden_runs"] and DS["gates"]["horizon"]["verdict"] == "PASS"
AVG_CALLS = round(sum(CALLS) / 6)
assert DS["gates"]["horizon"]["value"] == f"average of completed rollouts: {AVG_CALLS}"
OE = (TASK / "08_Oracle_Events.md").read_text()
OE_STEPS = [l for l in OE.splitlines() if re.match(r"OE \d+\s", l)]
OE_N = len(OE_STEPS)
oe_moves = sum(1 for l in OE_STEPS if re.match(r"OE \d+\s+Move DES-\d+ .* to Todo", l))
oe_comments = sum(1 for l in OE_STEPS if re.match(r"OE \d+\s+Comment on DES-\d+", l))
oe_shares = sum(1 for l in OE_STEPS if re.match(r"OE \d+\s+Share the ", l))
assert not re.search(r"pull request|github|gmail|trello", OE, re.I), "the Oracle path now touches a service the table treats as a detour"
LED = json.loads((WF / "run_forensics/rev2/baseline/summary.json").read_text())["runs"]
svc_calls = lambda r, s: sum(v for k, v in r["counts"]["by_tool"].items() if k.startswith(s + "_"))
GH_RUNS = sum(1 for r in LED if svc_calls(r, "github"))
MAIL = [svc_calls(r, "gmail") for r in LED]
READS = [r["counts"]["by_tool"]["linear_list_comments"] for r in LED]

# ------------------------------------------------------------------ the table
S, C = M.SEED, M.COUNTS
skim_total = sum(SKIM.values()) + seeded_slack
drive_total = owned + shared + seeded_files
n_lines, n_owed = M.N_LIST, C["Owed"]
over = {c: len(M.members(c)) for c in ("A1", "A2", "C1", "C2", "C4")}
n_over = sum(over.values())
assert (n_lines, n_owed, C["Ready"], C["Delivered"]) == (96, 49, 39, 8) and (oe_moves, oe_comments, oe_shares) == (n_owed, n_owed, 8)
assert all(n in (n_lines, n_lines + 1) for n in READS)
r5 = lambda x: int(5 * round(x / 5))          # rate-derived minutes to the nearest 5: the rates are approximate
skim_min, drive_min = r5(skim_total / 3000 * 60), r5(drive_total / 450 * 60)

T = [   # (sub-task, kind, volume, rate, minutes)
 ("Read the request, Frederick's DM and his hand-off notes", "read", f"3 records: prompt {len(prompt)} chars, DM {len(TXT.ASK)} chars, notes {len(TXT.NOTES)} chars with 3 state tests", "careful read: the tests are applied to every line", 30),
 ("Read Brian's pack list row by row", "read", f"{n_lines} rows, 5 columns", "about half a minute per row", 45),
 ("Skim Slack where the playable and its assets are discussed", "read", f"{skim_total} messages: " + ", ".join(f"{k} {v}" for k, v in SKIM.items()) + f"; {seeded_slack} seeded (Julia is a member of each)", "≈ 3,000 messages/h (worked-example skim anchor)", skim_min),
 ("Read the vendor's threads past their apparent end: formats and asset list, the pause and the new start, the first playable's sound exchange", "read", f"3 threads in a channel of {SKIM['the PlayableX channel (all of it)']} messages ({MAR_APR} of them from March and April)", "≈ 20 min each (decisive-thread anchor)", 60),
 ("Open each pack ticket, read Brian's note, apply the three tests", "read", f"{n_lines + 1} tickets (the pack ticket and {n_lines} children), {n_rows('linear.linear_comments')} notes", "3 min each: one ticket, one short note (below the 8 to 15 min anchor, which is for 2 to 3 surfaces)", r5(3 * n_lines)),
 ("List Julia's Drive for the notes, the pack list, the deck and anything else about the pack", "read", f"{drive_total} files ({owned} owned, {shared} shared, {seeded_files} seeded)", "≈ 450 items/h", drive_min),
 ("Read Calvin's sound sources sheet and Brian's log of the outgoing folder against the tickets", "read", f"{len(TXT.C2_SHEET_GRID) - 1} sheet rows, {len(TXT.C4_LOG.splitlines()) - 2} dated log lines", "15 min for both", 15),
 ("Read the design page and its comments for the tray and the loss rule; the reference-level deck", "read", f"1 page, 2 comments, {len(TXT.DECK_SLIDES)} slides", "20 min", 20),
 ("Find the kickoff hold and its attendees, and the vendor's intake address", "read", "1 event with 4 attendees, 1 contact", "10 min", 10),
 ("T1 Thursday's exports look ready until a colleague's post is read against the vendor's format rule", "dead end", f"{over['A1']} tickets, 1 post, 1 rule message", "≈ 20 min (decisive-thread anchor)", 20),
 ("T2 Friday's bathroom files look ready until Robert's note", "dead end", f"{over['A2']} tickets, 1 DM message", "15 min", 15),
 ("T3 three recoloured models: Owed on Robert's post until the log says they went again", "dead end", f"{over['C1']} tickets, Robert's post, the log entry", "15 min", 15),
 ("T7 the zipped instruments: the folder log says the zip will not unpack", "dead end", f"{over['C4']} tickets, 1 log line", "10 min", 10),
 ("T4 two sounds are not ours to pass on", "dead end", f"{over['C2']} tickets, 2 sheet rows", "10 min", 10),
 ("T18 the pull requests since the first zip, checked for the recoloured models", "dead end", f"{prs} pull requests created 22 to 30 Sep", "≈ 40 min (worked-example PR anchor)", 40),
 ("T18 other objects named in the recolour pull requests", "dead end", f"3 object names checked against {n_lines} lines", "5 min", 5),
 ("T5 the board's eight: the first list against a later reply under another post", "dead end", "2 posts, 1 thread of 3 messages", "≈ 20 min (decisive-thread anchor)", 20),
 ("T8, T12 stale start dates and the first playable's format rule", "dead end", "3 dates, 2 rule messages", "5 min each pair", 10),
 ("T9 the six-slot proposal on the design page", "dead end", "2 comments", "5 min", 5),
 ("T10, T16 the zombie pack 'not exported correctly', the duck and the rocket launcher", "dead end", "3 vendor messages, 2 tickets", "5 min each", 15),
 ("T11, T17 Leonard's Playable Kickoff card and his Playable Feedback doc", "dead end", "1 card, 1 doc", "5 min each", 10),
 ("T13, T14, T15 the board on the reference-level deck and earlier board ideas", "dead end", "1 slide, 3 messages", "10 min", 10),
 ("T19 object tickets with the same titles as pack lines", "dead end", f"{zom97} tickets under one parent", "≈ 450 items/h, then 3 opened", 10),
 ("T6 board set for the lines that are not board items", "dead end", "12 lines", "5 min", 5),
 ("Go back over the lines each later statement overturns: state, what is owed, who has it", "re-read", f"{n_over + 2} lines ({' + '.join(str(v) for v in over.values())} states, 2 board-set cells)", "2 min each", r5(2 * (n_over + 2))),
 ("Type the hand-off list", "write", f"1 sheet, {n_lines} rows × 7 columns", "1.25 min per row", int(1.25 * n_lines)),
 ("Write the brief", "write", "1 doc, 10 required facts", "60 min", 60),
 ("Move each Owed line's ticket to Todo and write its comment", "write", f"{n_owed} state changes, {n_owed} comments", "3 min per ticket (comments repeat within a group)", r5(3 * n_owed)),
 ("Share both files", "write", "2 files × 4 recipients = 8 shares", "1 min each", r5(8)),
 ("Send Frederick the count for each state; post both links in the vendor channel", "write", "2 messages", "5 min each", 10),
]
mins = lambda name: next(t[4] for t in T if t[0].startswith(name))
grp = lambda kind: sum(t[4] for t in T if t[1] == kind)
total = sum(t[4] for t in T)
hours = total / 60
assert abs(hours * 4 - round(hours * 4)) < 1e-9, f"{total} min = {hours} h is not on a 0.25 step"
reads, dead, reread, writes = grp("read"), grp("dead end"), grp("re-read"), grp("write")
assert reads + dead + reread + writes == total
n_dead_rows = sum(1 for t in T if t[1] == "dead end")
traps = sorted({int(x) for t in T if t[1] == "dead end" for x in re.findall(r"T(\d+)", t[0])})
assert traps == list(range(1, 20)) == sorted(int(t["id"][1:]) for t in man["traps"]), traps      # every manifest trap has a line

# groups used by both the condensed lines and the justification
R_RULES = mins("Read the request") + mins("Read Brian's pack list")
R_SLACK = mins("Skim Slack") + mins("Read the vendor's threads")
R_TICKETS = mins("Open each pack ticket")
R_DRIVE = mins("List Julia's Drive") + mins("Read Calvin's sound")
R_OTHER = mins("Read the design page") + mins("Find the kickoff hold")
D_NOTES = mins("T1 ") + mins("T2 ") + mins("T3 ") + mins("T7 ") + mins("T4 ")
D_PRS = mins("T18 the pull requests") + mins("T18 other objects")
D_REST = dead - D_NOTES - D_PRS
W_FILES = mins("Type the hand-off list") + mins("Write the brief")
W_TICKETS = mins("Move each Owed")
W_SEND = mins("Share both files") + mins("Send Frederick")
assert R_RULES + R_SLACK + R_TICKETS + R_DRIVE + R_OTHER == reads and W_FILES + W_TICKETS + W_SEND == writes

cond = [
 f"- Rules and list: the message, the notes, {n_lines} pack-list rows {R_RULES} min",
 f"- Slack: skim {skim_total} messages at 3,000/h, 3 vendor threads read through {R_SLACK} min",
 f"- {n_lines} tickets, one note each, 3 min each {R_TICKETS} min",
 f"- Drive listing {drive_total} files, sound sheet, folder log {R_DRIVE} min",
 f"- Design page, deck, kickoff hold, contact {R_OTHER} min",
 f"- {n_dead_rows} dead ends: notes that look ready, {prs} pull requests, the first board list, stale dates, look-alike tickets and card {dead} min",
 f"- Re-deciding {n_over + 2} overturned lines {reread} min",
 f"- Sheet of {n_lines} rows and the brief {W_FILES} min",
 f"- {n_owed} ticket moves with comments, 8 shares, 2 messages {W_TICKETS + W_SEND} min",
 f"- Total {total:,} min = {hours:.2f} h",
]
assert sum(int(re.search(r"(\d[\d,]*) min$", l).group(1).replace(",", "")) for l in cond[:-1]) == total, "condensed lines do not add up"
cond_text = "\n".join(cond)
assert 50 <= len(cond_text) <= 2000

# ------------------------------------------------------------------ the justification for the screen (task slot 05_Human_Time.md)
skim_round = int(round(skim_total, -1))
_parts = []
def m(n, suffix=""):
    """A sub-task's minutes as written in the paragraph; recorded so the sum can be checked against the table."""
    _parts.append(n)
    return f"{n}{suffix}"


HOUR_WORDS = {19: "Nineteen"}
assert hours == int(hours) and int(hours) in HOUR_WORDS
REASON = " ".join([
    f"{HOUR_WORDS[int(hours)]} hours by hand, and most of it is deciding the state of {n_lines} pack lines one at a time, not typing.",
    f"I'd start with Frederick's message, his hand-off notes with the three state tests and the {n_lines} rows of Brian's pack list ({m(R_RULES, ' minutes')}),",
    f"then skim about {skim_round:,} Slack messages across the PlayableX channel, four Zombie Match channels and three DMs and read 3 vendor threads to the end ({m(R_SLACK, ' minutes')}).",
    f"The biggest chunk is opening the {n_lines} pack tickets one by one, reading Brian's note on each and applying the tests, about 3 minutes each, {m(R_TICKETS, ' minutes')}.",
    f"Listing my {drive_total} Drive files and reading the sound sources sheet and Brian's log of the outgoing folder is {m(R_DRIVE, ' minutes')},",
    f"and the design page with its comments, the reference-level deck, the kickoff hold and the vendor's intake contact another {m(R_OTHER)}.",
    f"Dead ends take {dead} minutes: notes that look Ready until a later post, DM or log line says otherwise (Thursday's exports, Friday's bathroom files, three recoloured models, the zipped instruments, two sounds) cost {m(D_NOTES)},",
    f"checking {prs} pull requests for the recolours {m(D_PRS)},",
    f"and the first board list against Robert's later reply, stale start dates, the old format rule, the six-slot proposal, look-alike tickets and Leonard's card and doc {m(D_REST)}.",
    f"Going back over the {n_over + 2} lines a later record overturned is {m(reread, ' minutes')}.",
    f"Writing is {writes} minutes: the hand-off sheet of {n_lines} rows by 7 columns ({m(mins('Type the hand-off list'))}), the brief ({m(mins('Write the brief'))}),",
    f"{n_owed} ticket moves to Todo with {n_owed} comments at 3 minutes a ticket ({m(W_TICKETS)}), and 8 shares and 2 Slack messages ({m(W_SEND)}).",
    "No forced errors or waits were set up, so there is no workaround time.",
    f"That adds up to {total:,} minutes, or {hours:.2f} hours.",
])
assert "\n" not in REASON                                                                             # one paragraph, as in the completed tasks
assert 50 <= len(REASON) <= 2000, len(REASON)
assert not re.search(r"OpenAI|Scale AI|Remotasks|knowledge cutoff|[—–]", REASON)
assert not re.search(r"\b(?:DES-\d+|[CDG][A-Z0-9]{8,11}|f_[0-9a-f]{22}|T\d{1,2})\b", REASON)          # no internal ids in the field text
assert sum(_parts) == total and len(_parts) == 13, (_parts, sum(_parts))                               # every sub-task's minutes add to the total
assert all(re.search(rf"\b{n}\b", REASON) for n in _parts)
(TASK / "05_Human_Time.md").write_text(f"Hours: {hours:.2f}\n\nReasoning (type it in; the field blocks pasting):\n\n{REASON}\n")

# ------------------------------------------------------------------ worksheet
def table(head, rws):
    return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(str(c) for c in r) + " |" for r in rws])


calls = sum(x["calls"] for x in man["call_budget"])
CLOCK = ctx["universe"]["clock_line"].replace("Clock: ", "")
sha = hashlib.sha256(prompt.encode()).hexdigest()[:12]
sqlsha = hashlib.sha256(sql).hexdigest()[:12]
moved_note = ("Counts that differ from the first pass: " + "; ".join(f"{l} {a} then, {b} now" for l, a, b in MOVED) + ". The first pass cut some windows on UTC days; this pass cuts every window on Pacific days."
              if MOVED else "Every Slack count equals the first pass.")
ids = ", ".join(ch for ch, _, _ in CHANNELS)

doc = f"""# Human Time Worksheet — {M.SLUG}

Pass: post-baseline refresh        Tier: Long-Horizon
Universe: synth-cut · Clock: {CLOCK}
Hours: {hours:.2f}

Basis:
- The work 04_Prompt.txt asks for (sha256 {sha}): do everything Frederick's Sep 30 message asks, which covers a brief, a hand-off list with a state for every line of the pack, ticket moves and comments for the lines that are owed, sharing, the count for each state, and the two links.
- The work is done by hand in Julia's own accounts: no search, scripts or AI.
- Counts come from {M.REV} (01_Universe_Inject.sql {sqlsha}, solver/truth.json): {n_lines} lines, Delivered {C['Delivered']}, Ready {C['Ready']}, Owed {C['Owed']}. The person does not start out knowing where anything is.
- Friction: none (03_Error_Async_Config.txt), so there is no workaround line.
- Rows computed as volume × rate are rounded to the nearest 5 minutes (the rates are approximate); the others are stated estimates.
- Refresh inputs: 08_Oracle_Events.md ({OE_N} events: {oe_moves} moves, {oe_comments} comments, {oe_shares} shares, 2 messages, the sheet and the brief) and the six rev2 baseline runs in 07_Baseline_Trajectories (12_Difficulty_Stats.txt).
- What changed from the first pass: the hours did not (19.00 then, {hours:.2f} now). One row changed kind: the pull-request check was a read and is now a dead end, because no Oracle Event and no criterion uses a pull request, while {GH_RUNS} of 6 baseline runs still went to the repository; its minutes are unchanged. {moved_note}

""" + table(["Sub-task", "Kind (read / dead end / workaround / re-read / write)", "Volume (measured, persona view)", "Rate", "Minutes"], T + [("Total", "", "", "", f"{total} = {hours:.2f} h")]) + f"""

Tier check: in band (Long-Horizon ≈ 12–24 h; {hours:.2f} h). No trigger.
- Reads {reads} min, dead ends {dead} min, re-reading {reread} min, writes {writes} min.
- The manifest's call budget is {calls}; most of the hours are {n_lines} manual decisions, a {n_lines}-row sheet typed by hand and {2 * n_owed} per-ticket writes, which an agent makes in far fewer minutes each.
Baseline count basis (post-baseline only): no golden run, so the average of the six completed runs, {AVG_CALLS} counted calls ({min(CALLS)} to {max(CALLS)}), against the Long-Horizon tier of 100 to 500+. In band, the same tier the hours give.

Condensed breakdown (one line per sub-task group, facts only; the screen text is in the task slot 05_Human_Time.md, built from this table by the same script):
{cond_text}

Condensed breakdown length: {len(cond_text)} characters (field accepts 50–2,000)
Screen text in 05_Human_Time.md: one paragraph, {len(REASON)} characters, hours {hours:.2f}; its sub-task minutes add to {total:,}.

Sources measured: hg.py and persona_view.py, listed here, all run again in this pass.
- hg.py search search slack '17' --key ts with --file messages/CHANNEL/MONTH.json for every month file of {ids}; windows are Pacific days (22 Sep 00:00 PT to 1 Oct 00:00 PT; September for the DM with Frederick; the whole PlayableX channel). Scan complete for each.
- persona_view.py can-see julia_lawson slack for those eight conversations (YES for each); persona_view.py reach julia_lawson: Drive owned {owned}, shared {shared}.
- hg.py search search github '2025-09-' --pointer /pull_requests --key created_at ({len(pr_dates)} in September, {prs} created 22 to 30 Sep); hg.py search search linear ZOM-97 --key parent_id ({zom97}).
- 01_Universe_Inject.sql rows ({M.REV}), parsed with tools/base_check.parse_sql, never run: {n_rows('linear.linear_issues')} Design-team tickets, {n_rows('linear.linear_comments')} notes, {seeded_slack} Slack messages, {seeded_files} Drive files, 1 sheet of {n_lines} rows.
- Raw figures: humantime_gen/out/volumes.json (this pass); plan/out/humantime_volumes.json holds the first pass and was used only to report differences.

## Self-review

Checked in order against `10_Long Horizon Guidelines - V2.md` §5 and §10, the Pre-QC list and the field's own text.

""" + table(["Area", "Counter-reading", "Evidence that resolves it", "Verdict"], [
    ("Inflated", f"Three minutes for each of {n_lines} tickets and {3 * n_owed} minutes of ticket writes are padding.", f"each line has its own ticket and note ({M.BY_NAME[M.LINES[0]['name']]['ticket']} to {M.LAST_CHILD}) and every Owed line needs a move and a comment (hand-off notes {S['notes']['id']}); the six baseline runs each read {min(READS)} or {max(READS)} ticket comment lists, one per line (run-1 to run-6 in run_forensics/rev2/baseline/summary.json); the per-record rate is below the 8 to 15 min anchor because there is one surface, and the reason is stated on the row", "holds"),
    ("Solution-path estimate", "The table assumes the person already knows where the later statements are, and the pull-request check is not on the Oracle path at all.", f"every manifest trap T1 to T19 has a dead-end line ({n_dead_rows} rows, {dead} min), and the places are found by the skim and listing rows: {skim_total} messages, {drive_total} Drive files ({S['a1_post']['id']}, {S['c4_log']['id']}). The {prs} pull requests are counted as a dead end, not as required reading: 08_Oracle_Events.md never opens one, and {GH_RUNS} of 6 baseline runs still did", "holds"),
    ("Evaluator-wide volume", "The Slack and Drive counts could be universe-wide, not Julia's.", f"only conversations she is a member of are counted (persona_view can-see YES for all eight, e.g. {M.VENDOR_CH}, {M.MATCH3D_CH}, {M.DM_ROBERT}); Drive is her owned and shared files from persona_view reach, plus the seeded files shared with her ({S['notes']['id']}); counts stop at 1 Oct 00:00 PT", "holds"),
    ("Tier mismatch", f"{hours:.2f} h could sit outside Long-Horizon, or the baseline could show a different tier than the hours.", f"12 to 24 h is the band and {hours:.2f} h is inside it; the baseline average is {AVG_CALLS} counted calls, lowest {min(CALLS)} (12_Difficulty_Stats.txt), inside the Long-Horizon tier as well; no trigger, nothing tuned", "holds"),
    ("Linter reading", "From a 46-word prompt and the SQL alone, 19 hours could look more than three times too high.", f"the SQL shows {n_rows('linear.linear_issues')} tickets with {n_rows('linear.linear_comments')} notes under {M.PACK_TICKET} and a {n_lines}-row list ({S['tracker']['id']}); the screen text in 05_Human_Time.md names those volumes, the {n_owed} ticket writes and the dead ends in plain words, with no internal ids", "holds; the reasoning names the volumes"),
    ("Unlisted work", f"All six baseline runs searched mail ({', '.join(str(x) for x in MAIL)} calls for run-1 to run-6), so a mail sweep is missing from the table.", "no Oracle Event reads mail and no manifest trap sits there; adding a line would count work the prompt does not require (gate 1 of the playbook), so none is added and the hours are not stretched", "holds; counter-reading recorded"),
]) + f"""

Every volume was measured in this run (sources above); the first-pass figures were leads only. The sum was recomputed by the generator ({total} min) and both character counts were taken from the text as written. The screen text is one paragraph, as in the completed tasks, and is checked by the generator: 50 to 2,000 characters, its sub-task minutes add to the total, no banned phrase and no internal id. Unresolved: none.
"""
(WF / "05_Human_Time_Worksheet.md").write_text(doc)
print(f"wrote 05_Human_Time_Worksheet.md · {total} min = {hours:.2f} h · condensed {len(cond_text)} chars · skim {skim_total} msgs · drive {drive_total} · PRs {prs}")
print(f"wrote 05_Human_Time.md · reasoning {len(REASON)} chars · moved: {MOVED}")

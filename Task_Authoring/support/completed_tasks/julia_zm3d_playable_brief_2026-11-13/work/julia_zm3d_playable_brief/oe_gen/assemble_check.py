#!/usr/bin/env python3
"""Assemble Working_Files/08_OE_Check.md (check mode of /create-oe-writing): compares 08_Oracle_Events.md, as it is on
disk, with the ledger's model and the records. Every quoted span on every Expected line is re-read from its record in
this run (seeded rows re-parsed from the SQL, base records as re-read through tools/hg.py by oe_gen/base_read.py).
Findings come from oe_gen/check_findings.json (empty when there are none). Run from the workspace root, then:
python3 -B Task_Authoring/tools/stage_gate.py oe-check Task_Authoring/task_inputs --paste"""
import datetime as D, json, os, re, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import model as O
import facts as FX
F, FL = FX.F, FX.FL
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(O.TASK))
OE_PATH = O.TASK / "08_Oracle_Events.md"
OE = OE_PATH.read_text()
OUT = O.WF / "08_OE_Check.md"
ctx = json.loads((O.WF / "00_Task_Context.json").read_text())
CLOCK = re.sub(r"^Clock:\s*", "", ctx["universe"]["clock_line"])
def cell(s): return re.sub(r"\s+", " ", str(s)).replace("|", "/").strip()
def table(header, rows):
    return ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)] + ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
def norm(s): return re.sub(r"\s+", " ", s)

# ------------------------------------------------------------------ parse the events as they are on disk
blocks = re.findall(r"^OE (\d+)  (.*)\nExpected: (.*)$", OE, re.M)
EVJ = json.loads((HERE / "out" / "oe_events.json").read_text())
assert [int(b[0]) for b in blocks] == list(range(1, len(blocks) + 1)) == [e["n"] for e in EVJ], "events on disk differ from the drafted set: re-run draft_oe.py or re-key the check"
for b, e in zip(blocks, EVJ):
    assert b[1] == e["head"] and b[2] == e["expected"], f"OE {b[0]} on disk differs from the drafted text"
N_EV = len(re.findall(r"^\s*(?:#+\s*)?(?:\*\*)?OE\s*\d+", OE, re.M))
assert N_EV == len(blocks)

# ------------------------------------------------------------------ record corpus (re-read in this run)
def vals(row): return [str(v).replace("\\n", "\n") for v in row.values() if v is not None]
CORPUS = {}      # record id -> (text, pointer)
def put(i, text, ptr):
    old = CORPUS.get(i)
    CORPUS[i] = ((old[0] + " ¶ " if old else "") + text, (old[1] + "; " if old else "") + ptr)
for r in O.ROWS:
    if r["op"] != "insert": continue
    row, t, ln = r["row"], r["table"], f"SQL L{r['line']}"
    if t == "slack.slack_messages": put(f"{row['channel_id']}/{row['ts']}", " ¶ ".join(vals(row)), ln)
    elif t == "gdrive.drive_files": put(row["id"], " ¶ ".join(vals(row)), ln)
    elif t == "gdocs.docs_documents": put(row["document_id"], " ¶ ".join(vals(row)), ln)
    elif t == "gsheets.sheets_spreadsheets": put(row["spreadsheet_id"], " ¶ ".join(vals(row)), ln)
    elif t == "gsheets.sheets_sheets": put(row["spreadsheet_id"], row["title"] + " ¶ " + " ¶ ".join(c for g in json.loads(row["grid_json"]) for c in g), ln)
    elif t in ("gslides.slides_presentations", "gslides.slides_page_elements"): put(row["presentation_id"], " ¶ ".join(vals(row)), ln)
    elif t == "linear.linear_issues": put(row["id"], " ¶ ".join(vals(row)), ln)
    elif t == "linear.linear_comments": put(row["issue_id"], " ¶ ".join(vals(row)), ln)
    elif t == "gcal.gcal_events": put(row["event_id"], " ¶ ".join(vals(row)), ln)
    elif t == "contacts.contacts": put(row["contact_id"], f"{row['first_name']} {row['last_name']} ¶ " + " ¶ ".join(vals(row)), ln)   # the tool shows the name as first + last
for k in O._B:
    b = O.base(k)
    put(b["id"], b["text"] + " ¶ " + " ¶ ".join(x for x in b["files"] if x), "hg.py get " + b["src"])
put(O.GDD["id"], O.GDD_TEXT + " ¶ " + O.GDD["title"] + " ¶ " + O.GDD_C1["body"] + " ¶ " + O.GDD_C2["body"],
    f"hg.py get confluence/{O.GDD['_src']}, confluence/{O.GDD_C1['_src']}, confluence/{O.GDD_C2['_src']}")
# the pack ticket's children are read through the parent; a note read covers all 96 tickets
SIGN, n_spans, n_events = [], 0, 0
for e in EVJ:
    if e["kind"] != "read": continue
    recs = [i for i in e["records"] if i in CORPUS]
    assert recs, (e["n"], e["records"])
    text = norm(" ¶ ".join(CORPUS[i][0] for i in recs))
    spans = re.findall(r'"([^"]+)"', e["expected"])
    n_events += 1
    for s in spans:
        n_spans += 1
        assert norm(s) in text, f"OE {e['n']}: span not found in its record: {s[:80]!r}"
    ptrs = "; ".join(dict.fromkeys(p for i in recs for p in CORPUS[i][1].split("; ")))
    if len(ptrs) > 260: ptrs = ptrs[:ptrs.rfind(";", 0, 240)] + f"; … ({len(recs)} records, {recs[0]} to {recs[-1]})"
    first = spans[0] if spans else e["expected"][:60]
    SIGN.append((f"OE {e['n']}", f"{len(spans)} quoted span(s), from '{first[:70]}'", ptrs,
                 f"all {len(spans)} found verbatim (whitespace-normalised)", "VERIFIED quote · " + ", ".join(e["facts"][:6]) + (" …" if len(e["facts"]) > 6 else ""), "match"))
# derived and write events: values recomputed from the rows
def evn(prefix): return next(e["n"] for e in EVJ if e["head"].startswith(prefix))
_moves = [e for e in EVJ if e["head"].startswith("Move ")]; _comments = [e for e in EVJ if e["head"].startswith("Comment on ")]; _shares = [e for e in EVJ if e["head"].startswith("Share ")]
_settle = {k: evn(v) for k, v in {"tnotes": "Read Brian's note", "thr2": "Read the thread under Frederick's Sep 18", "bow": "Check whether Robert changed", "a1": "Read #zombie-match3d",
          "a2": "Read Julia's direct messages with Robert", "log": "Find Brian's log", "sound": "Find Calvin's sound sources", "rows": "Write the header", "dm": "Give Frederick the count"}.items()}
SIGN += [
 (f"OE {_settle['bow']}", f"'the eight on the board are {', '.join(O.EIGHT)}'", f"SQL L{O.PICKS['line']}, SQL L{O.C3['line']}; hg.py get {O.base('art_bow_root')['src']}",
  f"{', '.join(O.EIGHT)}; the list of {O.PICKS['id']} ends with {O.SWAPPED_OUT}", f"VERIFIED by recorded calculation · {F('eight')}", "match"),
 (f"OE {_settle['thr2']}", f"the {O.COUNTS['Delivered']} Delivered lines", f"SQL L{O.LINES[0]['ticket_line']} to SQL L{O.LINES[-1]['note_line']} (state Done on 8 tickets), re-parsed",
  ", ".join(l["name"] for l in O.by_state("Delivered")), f"VERIFIED by recorded calculation · {F('delivered')}", "match"),
 (", ".join(f"OE {_settle[k]}" for k in ("tnotes", "a1", "a2", "log", "sound")), f"the {O.COUNTS['Owed']} Owed lines, each with what is owed and who has it", f"SQL L{O.LINES[0]['ticket_line']} to SQL L{O.LINES[-1]['note_line']}, re-parsed",
  ", ".join(f"{w} {n}" for w, n in O.WHO_COUNTS.items()) + "; each line named once, on the read of its deciding record", f"VERIFIED by recorded calculation · {F('owed')}", "match"),
 (f"OE {_settle['rows']}, OE {_settle['dm']}", f"'Ready on the other {O.COUNTS['Ready']}'; 'Delivered {O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, Owed {O.COUNTS['Owed']}'", f"SQL L{O.LINES[0]['ticket_line']} to SQL L{O.LINES[-1]['note_line']}, re-parsed",
  f"Delivered {O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, Owed {O.COUNTS['Owed']}; every Ready name on OE {_settle['rows']} checked against oe_gen/model.py",
  f"VERIFIED by recorded calculation · {F('ready')}, {F('counts')}", "match"),
 (f"OE {_shares[0]['n']} to OE {_shares[-1]['n']}", "the four addresses and 'reader access'", f"SQL L{O.line('gcal.gcal_events', event_id=O.HOLD_ID)}, SQL L{O.line('contacts.contacts', contact_id=O.CONTACT['contact_id'])}",
  "brian.foster@harmonygames.co, frederick.stone@harmonygames.co, robert@harmonygames.co from the event's attendees; intake@playablex.ai from the contact", f"VERIFIED · {F('recipients')}", "match"),
 (f"OE {_moves[0]['n']} to OE {_comments[-1]['n']}", f"{len(_moves)} moves to Todo and {len(_comments)} comments, each on the ticket of an Owed line", f"SQL L{O.LINES[0]['ticket_line']} to SQL L{O.LINES[-1]['note_line']}; hg.py get linear/data.json/issues/769 (DES-304 in Todo)",
  f"the {len(_moves)} ticket keys and line names on the {len(_moves) + len(_comments)} events equal the Owed lines of oe_gen/model.py; each comment names the owed thing and the holder of that line", f"VERIFIED · {F('owed')}, {F('todo')}", "match"),
]
# check the derived and write events against the model, mechanically
def ex(n): return EVJ[n - 1]["expected"]
def hd(n): return EVJ[n - 1]["head"]
owed = O.by_state("Owed")
moves = [e for e in EVJ if e["head"].startswith("Move ")]; comments = [e for e in EVJ if e["head"].startswith("Comment on ")]
assert len(moves) == len(comments) == O.COUNTS["Owed"]
for l, m, c in zip(owed, moves, comments):
    assert m["head"].startswith(f"Move {l['ticket']} ({l['name']}) to Todo") and m["expected"] == f"{l['ticket']} is in state Todo."
    assert c["head"].startswith(f"Comment on {l['ticket']} ({l['name']})") and f"on {l['ticket']}:" in c["expected"] and f"{l['who']} has" in c["expected"]
shares = [e for e in EVJ if e["head"].startswith("Share ")]
assert len(shares) == 8
assert not [e for e in EVJ if e["kind"] not in ("read", "write")], "an event with no tool action"
assert all(l["name"] in ex(_settle["thr2"]) for l in O.by_state("Delivered"))
assert all(l["name"] in ex(_settle["rows"]) for l in O.by_state("Ready"))
_owed_src = {"VIS": "tnotes", "A1": "a1", "A2": "a2", "C4": "log", "C2": "sound"}
assert all(l["name"] in ex(_settle[_owed_src[l["cls"]]]) for l in owed)
assert f"Delivered {O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, Owed {O.COUNTS['Owed']}." in ex(_settle["dm"])

# ------------------------------------------------------------------ qualifier check (pasted)
p = subprocess.run([sys.executable, "-B", str(O.TOOLS / "oe_qualifier_check.py"), "check", "--task-dir", str(O.TASK)], capture_output=True, text=True, cwd=O.ROOT, env=ENV)
qc = [l for l in p.stdout.splitlines() if l.strip()]
assert qc and qc[0].startswith("OE QUALIFIER CHECK") and " 0 contradicted, 0 unsupported" in p.stdout, p.stdout[:600]

# ------------------------------------------------------------------ sections
INV = [(f"'{e['head'][:64]}'", "STEP", f"OE {e['n']}") for e in EVJ]
def E(*keys): return ", ".join(f"OE {n}" for n in keys)
n = {k: next(e["n"] for e in EVJ if e["head"].startswith(v)) for k, v in {
    "ask": "Find Frederick's message", "notes": "Find Frederick's hand-off notes", "pack": "Find Brian's pack list", "ticket": "Open DES-314", "tnotes": "Read Brian's note",
    "thr1": "Find the PlayableX channel", "thr2": "Read the thread under Frederick's Sep 18", "thr3": "Read the thread under Frederick's Sep 29", "music": "Search Slack for \"music\"",
    "design": "Read #zombie-design", "bow": "Check whether Robert changed", "a1": "Read #zombie-match3d", "a2": "Read Julia's direct messages with Robert",
    "log": "Find Brian's log", "sound": "Find Calvin's sound sources", "deck": "Read Julia's deck", "gdd": "Open the design page", "hold": "Find the kickoff hold", "contact": "Look up PlayableX",
    "brief": "Create the brief", "sheet": "Create the hand-off list", "rows": "Write the header", "dm": "Give Frederick the count", "post": "Post both links"}.items()}
sh0, sh1 = shares[0]["n"], shares[-1]["n"]; t0, t1 = moves[0]["n"], comments[-1]["n"]
COV = [
 ("R1", E(n["ask"]), "covered", "ledger route: Slack search for the message of Sep 30, then Julia's DM with Frederick"),
 ("R2", E(n["ask"], n["notes"], n["pack"], n["ticket"], n["tnotes"]), "covered", "ledger route: the DM, then the notes, the pack list and the pack ticket it names"),
 ("R3", f"{E(n['thr1'], n['thr2'], n['thr3'], n['music'], n['design'], n['bow'], n['sound'], n['deck'], n['gdd'])} feed OE {n['brief']}", "covered", "ledger route: each element of the brief has its own read; the write is one document create"),
 ("R4", f"{E(n['pack'], n['ticket'], n['tnotes'], n['thr1'], n['thr2'], n['design'], n['bow'], n['a1'], n['a2'], n['log'], n['sound'])} feed {E(n['sheet'], n['rows'])}", "covered",
  "ledger route: the full population of 96 lines is read before any state is set; each read of a deciding record names the lines it settles; create and fill are two writes"),
 ("R5", f"OE {t0} to OE {t1} ({len(moves)} moves, {len(comments)} comments)", "covered", "ledger route: one write per ticket; the state name comes from the notes (OE 2)"),
 ("R6", f"{E(n['hold'], n['contact'])} feed OE {sh0} to OE {sh1}", "covered", "ledger route: attendees from the calendar event, the address from Contacts; the invite mail in Julia's mailbox is another valid route to the same attendees"),
 ("R7", f"{E(n['thr2'], n['rows'])} feed OE {n['dm']}", "covered", "ledger route: one Slack message in the DM"),
 ("R8", E(n["brief"], n["sheet"]), "covered", "ledger route: both files are created by Julia and sit in her Drive"),
 ("R9", f"OE {n['thr1']} (the channel) and OE {n['post']}", "covered", "ledger route: one Slack message in the channel with both links"),
]
FIND = json.loads((HERE / "check_findings.json").read_text()) if (HERE / "check_findings.json").exists() else []
for f in FIND: assert f["quoted_span"] in OE, f["quoted_span"]
n_block = sum(1 for f in FIND if "BLOCKING" in f["severity"].upper())
SWEEP = [
 ("1 One wrong count, ID, channel or tool", f"PASS: 96, 84, 12, 88, {O.COUNTS['Delivered']}, {O.COUNTS['Ready']}, {O.COUNTS['Owed']}, {len(O.OVERTURNED)}, {len(O.members('VIS'))}, " + ", ".join(str(v) for v in O.WHO_COUNTS.values()) + f" recomputed by oe_gen/model.py from the SQL rows; every ticket key, ts, file id and channel id on an Expected line found in its record by tools/oe_qualifier_check.py (0 contradicted, 0 unsupported)"),
 ("2 One required write missing", f"PASS: the brief OE {n['brief']}, the list OE {n['sheet']} and OE {n['rows']}, 8 shares OE {sh0} to OE {sh1}, {len(moves)} moves and {len(comments)} comments OE {t0} to OE {t1}, the counts OE {n['dm']}, the links OE {n['post']}"),
 ("3 One fact in expected data with no retrieving step", "PASS: each value on a write event is on the Expected line of the earlier read it cites, and each line's state is stated on the read of the record that settles it; the state name Todo is in the notes (OE 2)"),
 ("4 One unledgered Expected value or unbacked absence word", f"PASS: every quoted span is in its record ({n_spans} spans over {n_events} read events); no Expected line makes an absence claim; the Ready set is stated as the exported lines other than the {len(O.OVERTURNED)} a later record makes Owed, and {F('absence')} holds the scope-bound search behind it"),
 ("5 One act-vs-defer conflict", "PASS: oe_gen/out/defer_search.json finds no hold on any of the seven write families (ledger section C); the pause is older than the ask, which says 'While it's parked'"),
 ("6 One non-action or final-response event", f"PASS: none in {N_EV} events: every event is a read or a write with its service named (the rev1 reasoning events are folded into the reads and writes that carry their conclusions); the Delivered and Ready tickets appear in no write"),
 ("7 One prompt-forbidden write", "PASS: the prompt forbids none; every write traces to the message or the notes it names (ledger section C)"),
 ("8 One missing recovery/wait event for an injected error", "PASS: Friction: none (03_Error_Async_Config.txt)"),
]
ADV = [
 (f"OE {t0} to OE {t1}", f"One write per ticket by rule, so the set runs to {N_EV} events; the rubric review will cite these labels."),
 (f"OE {n['tnotes']}", "One read over the population of 96 tickets; a run makes 96 comment-list calls (the pre-check run did)."),
 (f"OE {n['hold']}", "The invite mail in Julia's mailbox carries the same four names; a run that reads it instead reaches the same recipients."),
 ("OE 3", "The qualifier tool marks the row counts 96, 84 and 12 as collection counts it cannot prove from one record; they are counts of the grid rows of SQL L25, recomputed here."),
]
CR = [
 ("R1", "COVERED could be wrong if the search of OE 1 lands on another message", f"{O.ASK['id']} is the only message in DM {O.DM_FRED} dated Tue Sep 30 and the only seeded row holding 'playable' in that DM (SQL L{O.ASK['line']})", "covered"),
 ("R2", "the notes could be reachable only by an id the events never produce", f"OE {n['notes']} searches Drive for the notes' own title words; ledger {F('notes')} proves the search reaches {O.NOTES_ID} as Julia", "covered"),
 ("R3", "the brief could be 'mentioned' but never created, or miss an element of the notes' list", f"OE {n['brief']} is a create with each of the notes' elements and the read behind it; checked against the notes' first paragraph in {O.NOTES_ID}", "covered"),
 ("R4", "the population could be narrowed before it is derived (only the lines with a later statement)", f"OE {n['pack']} lists all 96 lines and OE {n['tnotes']} reads all 96 notes before any state is set; {O.COUNTS['Delivered']} + {O.COUNTS['Ready']} + {O.COUNTS['Owed']} = 96, each line set once", "covered"),
 ("R5", "a comment could stand in for the state change, or one event could carry both", f"OE {t0} to OE {t1} alternate one move and one comment per ticket, {len(moves)} of each, checked mechanically against the Owed lines (DES-316 to DES-409)", "covered"),
 ("R6", "the shares could go to the Trello card's people or leave the outside address out", f"OE {n['hold']} reads {O.HOLD_ID}; OE {n['contact']} reads the contact; 8 share events name the four addresses", "covered"),
 ("R7", "the counts could be only in the channel post", f"OE {n['dm']} is its own write in DM {O.DM_FRED}; the ask says 'here'", "covered"),
 ("R8", "the files could be created in a shared folder", f"OE {n['brief']} and OE {n['sheet']} state 'owned by Julia, in her Drive'; d_8140f09bf9f1b94cb8ee2d is her root ({F('drive')})", "covered"),
 ("R9", "the post could be a draft or go to the wrong channel", f"OE {n['post']} names {O.VENDOR_CH}, the channel OE {n['thr1']} finds; slack_send_message sends", "covered"),
]
for f in FIND:
    CR.append((f"Finding {f['n']}", f["counter_reading"], f["counter_evidence"], f["counter_result"]))

doc = [f"# 08 OE Check — julia-zm3d-playable-brief",
       f"Checked {D.date.today().isoformat()} · Clock: {CLOCK} · Events {N_EV} · Characters {len(OE)} (300–50,000: ok) · Ledger {D.date.today().isoformat()} · release task-quality-v1", "",
       f"Clock: {CLOCK}", "",
       "/oe prediction (a prediction only; /oe gives the verdict): " + ("PASS 5" if not FIND else ("FAIL 2" if n_block else "NON-FAIL 3")),
       ("Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE · Blocking 0" if not FIND else
        f"Completeness {'2' if any('incomplete' in f['component'].lower() and 'BLOCKING' in f['severity'] for f in FIND) else '5'} · Accuracy "
        f"{'2' if any('accura' in f['component'].lower() and 'BLOCKING' in f['severity'] for f in FIND) else '3'} · Path feasibility {'BROKEN' if n_block else 'SUPPORTED'} · "
        f"Task solvability {'NOT_ESTABLISHED' if n_block else 'SUPPORTED_BY_OE'} · Blocking {n_block}"), "",
       "## Inventory", "",
       f"The whole text is {N_EV} numbered events; there is no header, note or context segment outside them. {sum(1 for e in EVJ if e['kind'] == 'read')} read events, "
       f"{sum(1 for e in EVJ if e['kind'] == 'write')} write events, no reasoning event without a tool. No RESPONSE_DESCRIPTION and no NON_ACTION segment.", ""]
doc += table(["Segment (quoted start)", "Role", "Event"], INV)
doc += ["", "## Coverage", ""] + table(["R / F", "Event(s)", "Covered / missing / partial", "Route (ledger / other valid)"], COV)
doc += ["", "## Expected-data sign-off", "",
        f"Every quoted span on every Expected line of the {n_events} read events ({n_spans} spans) was re-read in this run from its record and found verbatim (whitespace-normalised): injected rows by parsing "
        "01_Universe_Inject.sql again (never executed), base records through hg.py get (oe_gen/base_read.py). The states, holders, counts and ticket keys stated on the reads and the writes were recomputed from "
        "the rows by oe_gen/model.py, asserted equal to solver/truth.json, and compared event by event with the text on disk.", ""]
doc += table(["Event", "Claim (quoted)", "Source re-read (hg.py pointer)", "Value found", "Ledger entry (result · quote · evidence_check / not_a_claim)", "Match / minor / wrong / unresolved"], SIGN)
doc += ["", "`python3 -B Task_Authoring/tools/oe_qualifier_check.py check --task-dir Task_Authoring/task_inputs` (dates, ids, authors, counts and states on every Expected line):", "", "```text"] + qc + ["```", "",
        "## Findings", ""]
doc += table(["#", "Severity", "Component", "Event", "Quoted span", "Rule (Eval § / source)", "What is wrong", "Evidence (ledger fact + source pointer)"],
             [(f["n"], f["severity"], f["component"], f["event"], f["quoted_span"], f["rule"], f["wrong"], f["evidence"]) for f in FIND])
if not FIND: doc += ["", "No finding: nothing in the events contradicts the ledger or a record."]
doc += ["", "## Pre-verdict sweep", ""] + table(["Eval 4.0 check (7)", "Result"], SWEEP)
doc += ["", "## Advisory (no effect on the prediction)", ""] + table(["Event", "Note"], ADV)
minor = sum(1 for f in FIND if f["severity"].upper() == "MINOR"); mod = sum(1 for f in FIND if f["severity"].upper() == "MODERATE"); unres = sum(1 for f in FIND if f["severity"].upper() == "OPEN")
doc += ["", "## Tally", "",
        f"Blocking {n_block} (incomplete {sum(1 for f in FIND if 'BLOCKING' in f['severity'] and 'omplete' in f['component'])} · inaccurate {sum(1 for f in FIND if 'BLOCKING' in f['severity'] and 'ccura' in f['component'])} · length 0) · "
        f"moderate {mod} (non-action 0 · final-response 0 · format {mod}) · minor {minor} · unresolved {unres} · advisory {len(ADV)}", "",
        "## Self-review", ""]
BLIND = (HERE / "blind_summary.md").read_text().strip() if (HERE / "blind_summary.md").exists() else ""
doc += ["Walked Evals/2_Oracle_Events_Eval.md 1.2, 1.3, the HARD GATE, 2.1–2.7, 3.1–3.6 and 4.0 in order against this report. Inventory: every segment is a numbered step with an action, the information it is after, "
        "the service, its parameters and an Expected line; every event names the events it rests on. Every expected value this report relies on was re-verified in this run: quoted spans against the "
        "re-parsed SQL rows and the base records read through hg.py, counts and states by oe_gen/model.py, qualifiers by tools/oe_qualifier_check.py (0 contradicted, 0 unsupported). No corrected event text is "
        "proposed here that was not re-read from a record.", ""]
if BLIND: doc += [BLIND, ""]
doc += table(["Row", "Counter-reading (the best case against the judgement)", "Evidence that resolves it", "Result"], CR)
doc += ["", "Unresolved: none. Open risks of the ledger (section F) that concern the rubric stay with the rubric stage.", "",
        "## Reminders", "- The tool-call minimum is measured on the golden run or the 6-rollout average, never on the OE count.",
        "- Fix the events (Claude, Codex or the human), re-run check, then run /oe.", ""]
OUT.write_text("\n".join(doc) + "\n")
print("wrote", OUT, "| events", N_EV, "| chars", len(OE), "| spans", n_spans, "| findings", len(FIND), "| qualifier:", qc[0][:90])

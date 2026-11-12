#!/usr/bin/env python3
"""rev2 edit of oe_gen/assemble_check.py: the events no longer include reasoning ('derive') steps, so the sign-off,
the mechanical checks, coverage, sweep and counter-readings point at the read or write event that now carries each
conclusion; counts come from the model; Robert's DM replaces Claire's. Idempotent."""
from pathlib import Path
P = Path(__file__).resolve().parent / "assemble_check.py"
s = P.read_text()
E = [
 # sign-off rows for the values that used to sit on derive events
 ('''SIGN += [
 ("OE 12", "'The eight: Grenade, Couch, Plushie Chick, Shuriken, Cute Axe, Gift Box, Cactus Plant, Bow'", f"SQL L{O.PICKS['line']}, SQL L{O.C3['line']}; hg.py get {O.base('art_bow_root')['src']}",
  f"{', '.join(O.EIGHT)}; the list of {O.PICKS['id']} ends with {O.SWAPPED_OUT}", f"VERIFIED by recorded calculation · {F('eight')}", "match"),
 ("OE 21 to OE 24", "'Delivered 8, Ready 36, Owed 52; 96 lines. Owed by person: Brian 27, Claire 21, Calvin 3, Martin 1.'", f"SQL L{O.LINES[0]['ticket_line']} to SQL L{O.LINES[-1]['note_line']} (the 96 tickets and notes), re-parsed",
  f"Delivered {O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, Owed {O.COUNTS['Owed']}; " + ", ".join(f"{w} {n}" for w, n in O.WHO_COUNTS.items()) + "; every line name on the four Expected lines checked against oe_gen/model.py",
  f"VERIFIED by recorded calculation · {F('delivered')}, {F('ready')}, {F('owed')}, {F('counts')}", "match"),
 ("OE 28 to OE 35", "the four addresses and 'reader access'", f"SQL L{O.line('gcal.gcal_events', event_id=O.HOLD_ID)}, SQL L{O.line('contacts.contacts', contact_id=O.CONTACT['contact_id'])}",
  "brian.foster@harmonygames.co, frederick.stone@harmonygames.co, robert@harmonygames.co from the event's attendees; intake@playablex.ai from the contact", f"VERIFIED · {F('recipients')}", "match"),
 ("OE 36 to OE 139", "52 moves to Todo and 52 comments, each on the ticket of an Owed line", f"SQL L{O.LINES[0]['ticket_line']} to SQL L{O.LINES[-1]['note_line']}; hg.py get linear/data.json/issues/769 (DES-304 in Todo)",
  "the 52 ticket keys and line names on the 104 events equal the Owed lines of oe_gen/model.py; each comment names the owed thing and the holder of that line", f"VERIFIED · {F('owed')}, {F('todo')}", "match"),
]''',
  '''def evn(prefix): return next(e["n"] for e in EVJ if e["head"].startswith(prefix))
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
]'''),
 # mechanical checks
 ('''assert len(moves) == len(comments) == 52''', '''assert len(moves) == len(comments) == O.COUNTS["Owed"]'''),
 ('''for s in ("Delivered", "Ready"):
    names_ = [l["name"] for l in O.by_state(s)]
    src = next(e["expected"] for e in EVJ if e["kind"] == "derive" and e["expected"].startswith(f"{s} {len(names_)}"))
    assert all(n in src for n in names_), s
derive_owed = " ".join(e["expected"] for e in EVJ if e["kind"] == "derive")
assert all(l["name"] in derive_owed for l in owed)''',
  '''assert not [e for e in EVJ if e["kind"] not in ("read", "write")], "an event with no tool action"
assert all(l["name"] in ex(_settle["thr2"]) for l in O.by_state("Delivered"))
assert all(l["name"] in ex(_settle["rows"]) for l in O.by_state("Ready"))
_owed_src = {"VIS": "tnotes", "A1": "a1", "A2": "a2", "C4": "log", "C2": "sound"}
assert all(l["name"] in ex(_settle[_owed_src[l["cls"]]]) for l in owed)
assert f"Delivered {O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, Owed {O.COUNTS['Owed']}." in ex(_settle["dm"])'''),
 # event lookup
 ('''    "design": "Read #zombie-design", "bow": "Check whether Robert changed", "eight": "Work out the eight", "a1": "Read #zombie-match3d", "a2": "Read Julia's direct messages with Claire",
    "log": "Find Brian's log", "sound": "Find Calvin's sound sources", "deck": "Read Julia's deck", "gdd": "Open the design page", "hold": "Find the kickoff hold", "contact": "Look up PlayableX",
    "del": "Work out the Delivered lines", "later": "Work out which exported lines", "vis": "Work out the lines Brian's own note", "counts": "Work out the Ready lines",
    "brief": "Create the brief",''',
  '''    "design": "Read #zombie-design", "bow": "Check whether Robert changed", "a1": "Read #zombie-match3d", "a2": "Read Julia's direct messages with Robert",
    "log": "Find Brian's log", "sound": "Find Calvin's sound sources", "deck": "Read Julia's deck", "gdd": "Open the design page", "hold": "Find the kickoff hold", "contact": "Look up PlayableX",
    "brief": "Create the brief",'''),
 # coverage
 ('''("R3", f"{E(n['thr1'], n['thr3'], n['music'], n['design'], n['bow'], n['eight'], n['sound'], n['deck'], n['gdd'])} feed OE {n['brief']}",''',
  '''("R3", f"{E(n['thr1'], n['thr2'], n['thr3'], n['music'], n['design'], n['bow'], n['sound'], n['deck'], n['gdd'])} feed OE {n['brief']}",'''),
 ('''("R4", f"{E(n['pack'], n['ticket'], n['tnotes'], n['thr1'], n['thr2'], n['design'], n['a1'], n['a2'], n['log'], n['sound'], n['del'], n['later'], n['vis'], n['counts'])} feed {E(n['sheet'], n['rows'])}", "covered",
  "ledger route: the full population of 96 lines is read before any state is set; create and fill are two writes"),''',
  '''("R4", f"{E(n['pack'], n['ticket'], n['tnotes'], n['thr1'], n['thr2'], n['design'], n['bow'], n['a1'], n['a2'], n['log'], n['sound'])} feed {E(n['sheet'], n['rows'])}", "covered",
  "ledger route: the full population of 96 lines is read before any state is set; each read of a deciding record names the lines it settles; create and fill are two writes"),'''),
 ('''("R5", f"OE {t0} to OE {t1} (52 moves, 52 comments)",''', '''("R5", f"OE {t0} to OE {t1} ({len(moves)} moves, {len(comments)} comments)",'''),
 ('''("R7", f"OE {n['counts']} feeds OE {n['dm']}", "covered", "ledger route: one Slack message in the DM"),''',
  '''("R7", f"{E(n['thr2'], n['rows'])} feed OE {n['dm']}", "covered", "ledger route: one Slack message in the DM"),'''),
 # sweep
 ('''("1 One wrong count, ID, channel or tool", f"PASS: 96, 84, 12, 88, 8, 36, 52, 37, 15, 27, 21, 3, 1 recomputed''',
  '''("1 One wrong count, ID, channel or tool", f"PASS: 96, 84, 12, 88, {O.COUNTS['Delivered']}, {O.COUNTS['Ready']}, {O.COUNTS['Owed']}, {len(O.OVERTURNED)}, {len(O.members('VIS'))}, " + ", ".join(str(v) for v in O.WHO_COUNTS.values()) + f" recomputed'''),
 ('''("2 One required write missing", f"PASS: the brief OE {n['brief']}, the list OE {n['sheet']} and OE {n['rows']}, 8 shares OE {sh0} to OE {sh1}, 52 moves and 52 comments OE {t0} to OE {t1}, the counts OE {n['dm']}, the links OE {n['post']}"),''',
  '''("2 One required write missing", f"PASS: the brief OE {n['brief']}, the list OE {n['sheet']} and OE {n['rows']}, 8 shares OE {sh0} to OE {sh1}, {len(moves)} moves and {len(comments)} comments OE {t0} to OE {t1}, the counts OE {n['dm']}, the links OE {n['post']}"),'''),
 ('''("3 One fact in expected data with no retrieving step", "PASS: each value on a derived or write event is on the Expected line of the earlier read it cites; the state name Todo is in the notes (OE 2)"),''',
  '''("3 One fact in expected data with no retrieving step", "PASS: each value on a write event is on the Expected line of the earlier read it cites, and each line's state is stated on the read of the record that settles it; the state name Todo is in the notes (OE 2)"),'''),
 ('''no Expected line makes an absence claim; the Ready set is stated as the exported lines other than the 37 overturned ones, and {F('absence')} holds the scope-bound search behind it"),''',
  '''no Expected line makes an absence claim; the Ready set is stated as the exported lines other than the {len(O.OVERTURNED)} a later record makes Owed, and {F('absence')} holds the scope-bound search behind it"),'''),
 ('''("6 One non-action or final-response event", f"PASS: none in {N_EV} events; the Delivered and Ready tickets appear in no event"),''',
  '''("6 One non-action or final-response event", f"PASS: none in {N_EV} events: every event is a read or a write with its service named (the rev1 reasoning events are folded into the reads and writes that carry their conclusions); the Delivered and Ready tickets appear in no write"),'''),
 ('''(f"OE {t0} to OE {t1}", "One write per ticket by rule, so the set runs to 141 events; the rubric review will cite these labels."),''',
  '''(f"OE {t0} to OE {t1}", f"One write per ticket by rule, so the set runs to {N_EV} events; the rubric review will cite these labels."),'''),
 ('''f"OE {n['pack']} lists all 96 lines and OE {n['tnotes']} reads all 96 notes before OE {n['del']} to OE {n['counts']} set a state; 8 + 36 + 52 = 96", "covered"),''',
  '''f"OE {n['pack']} lists all 96 lines and OE {n['tnotes']} reads all 96 notes before any state is set; {O.COUNTS['Delivered']} + {O.COUNTS['Ready']} + {O.COUNTS['Owed']} = 96, each line set once", "covered"),'''),
 ('''f"OE {t0} to OE {t1} alternate one move and one comment per ticket, 52 of each, checked mechanically against the Owed lines (DES-316 to DES-409)", "covered"),''',
  '''f"OE {t0} to OE {t1} alternate one move and one comment per ticket, {len(moves)} of each, checked mechanically against the Owed lines (DES-316 to DES-409)", "covered"),'''),
 ('''       f"{sum(1 for e in EVJ if e['kind'] == 'derive')} reasoning events with no tool, {sum(1 for e in EVJ if e['kind'] == 'write')} write events. No RESPONSE_DESCRIPTION and no NON_ACTION segment.", ""]''',
  '''       f"{sum(1 for e in EVJ if e['kind'] == 'write')} write events, no reasoning event without a tool. No RESPONSE_DESCRIPTION and no NON_ACTION segment.", ""]'''),
 ('''"the service, its parameters and an Expected line; the reasoning events name the events they rest on. Every expected value''',
  '''"the service, its parameters and an Expected line; every event names the events it rests on. Every expected value'''),
 ('''"01_Universe_Inject.sql again (never executed), base records through hg.py get (oe_gen/base_read.py). The states, holders, counts and ticket keys on the reasoning and write events were recomputed from "''',
  '''"01_Universe_Inject.sql again (never executed), base records through hg.py get (oe_gen/base_read.py). The states, holders, counts and ticket keys stated on the reads and the writes were recomputed from "'''),
]
done, skipped, missing = 0, 0, []
for a, b in E:
    if s.count(a) == 1:
        s = s.replace(a, b); done += 1
    elif b.split("\n")[0] in s:
        skipped += 1
    else:
        missing.append(a[:100])
P.write_text(s)
left = [w for w in ("Work out", "'derive'", "Ready 36", "52 moves", "Robert changed\", \"eight\"", "with Claire\"") if w in s]
print(f"applied {done}, already {skipped}, missing {missing}; leftovers {left}")

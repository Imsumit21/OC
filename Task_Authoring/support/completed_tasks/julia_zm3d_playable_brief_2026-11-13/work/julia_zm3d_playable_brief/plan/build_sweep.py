#!/usr/bin/env python3
"""Write Working_Files/01d_Coherence_Sweep.json (coherence-sweep-v1) for the current SQL.

Inputs: the tool's own template (hashes, quantifier spans, seeded facts), the two cold reviewers' findings files, the
base searches of `coherence_sweep.py candidates --run-base yes` (plan/out/sweep_candidates_base.json), and the hand-written
settlements in plan/sweep_settlements.json (forks, defects, dismissals: what each reviewer finding led to).
Run after the SQL is final; `coherence_sweep.py check` then reads the record."""
import hashlib, json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
ROOT = TASK.parents[1]
TOOLS = TASK.parent / "tools"
sys.path.insert(0, str(HERE))
import design_model as M
S, B = M.SEED, M.BASE
REVIEW = WF / "local_reviews" / "coherence"
MODEL = "claude-fable-5-2 (cold subagent: saw only its brief and the universe through tools/hg.py)"

tpl = json.loads(subprocess.run([sys.executable, "-B", str(TOOLS / "coherence_sweep.py"), "template", "--task-dir", str(TASK)],
                                capture_output=True, text=True, cwd=ROOT, check=True).stdout)
sql_sha = tpl["bound_to"]["01_Universe_Inject.sql"]

# ---------------------------------------------------------------- reviewers
reviewers = []
for rid in ("1", "2"):
    brief = REVIEW / f"brief_{rid}.md"
    reviewers.append({"id": rid, "model": MODEL, "brief_sha256": hashlib.sha256(brief.read_bytes()).hexdigest(),
                      "brief": f"Working_Files/local_reviews/coherence/brief_{rid}.md",
                      "findings": f"Working_Files/local_reviews/coherence/findings_{rid}.json"})

# ---------------------------------------------------------------- open sets (every quantifier span in a record that carries the ask)
LISTED = [l for l in M.LINES if l["on_list"]]
def tk(pred): return [l["ticket"] for l in LISTED if pred(l)]
board = lambda l: l["kind"] == "Board item"
default = set(M.DEFAULT_FINAL)
EXTRA = tk(lambda l: board(l) and l["name"] not in default)
NON_BOARD = tk(lambda l: not board(l))
ALL = tk(lambda l: True)
OWED = [l["ticket"] for l in LISTED if l["state"] == "Owed"]
SOUND_NO = [M.BY_NAME[n]["ticket"] for n in ("Rocket sound", "Explosion sound")]
import json as _j
HOLD = sorted(_j.loads((HERE / "out" / "sql_ids.json").read_text())["events"].values())
assert len(EXTRA) == 76 and len(NON_BOARD) == 12 and len(ALL) == 96 and len(HOLD) == 4, (len(EXTRA), len(NON_BOARD), len(ALL), len(HOLD))
def census(ids, base_ids=()): return {"count": len(ids) + len(base_ids), "ids": list(ids), "base_ids": list(base_ids)}
C1 = [M.BY_NAME[n]["ticket"] for n in ("Chainsaw", "Cone", "Cactus Plant")]
RULES = [   # (words of the span, rule, injected ids, base ids)
 ("every other board item on the list is an extra", "a board item of the pack list (Kind: Board item) that is not one of the eight on the board as they stand after Robert's 26 Sep reply", EXTRA, []),
 ("Extra for every other board item", "Extra: a row whose Kind is Board item and which is not one of the eight (76); empty: a row whose Kind is not Board item (12: Cannon, Background, Zombie characters, six sound cues, Item visuals, UI elements, Fonts)", EXTRA + NON_BOARD, []),
 ("Owed: anything else", "a line that meets neither the Delivered test nor every part of the Ready test, as things stand at the clock (solver/truth.json: 52 lines)", OWED, []),
 ("note on each ticket", "each child ticket of the pack ticket carries exactly one note by Brian", ALL, []),
 ("it sits with whoever the file came from", "the person named as the file's source in the line's own note; three lines' art changed after their file was handed over, and all three notes say 'FBX from Claire'", C1, []),
 ("Anything from a library or a bought pack", "a sound cue of the pack list whose source in Calvin's sheet is a library or a bought pack ('no' under 'OK outside the game'): Rocket sound, Explosion sound. The sheet's third 'no' row (laptop error and shutdown, Windows system sounds) is not a line of the pack list", SOUND_NO, []),
 ("Everyone on the kickoff hold", "an attendee of the kickoff hold on 3 Nov: Frederick Stone, Julia Lawson, Brian Foster, Robert (one event copy per attendee calendar)", HOLD, []),
 ("every line of the playable pack", "a row of the pack list = a child ticket of the pack ticket; the list and the tickets hold the same 96 lines", ALL, []),
 ("a note on each one", "each child ticket of the pack ticket carries exactly one note by Brian", ALL, []),
 ("Everything else", "a board item of Brian's pack list (Kind: Board item) that is not one of Robert's eight as they stand after his 26 Sep reply; the lines Brian sends are the rows of the pack list, nothing else", EXTRA, []),
 ("everything he's asking for", "every instruction of Frederick's message and of the notes that message names: the brief, the hand-off list, the ticket follow-through, the sharing, the count for each state and the two links", [S["ask"]["id"], S["notes"]["id"]], []),
 ("All four are in the pack Marcus sent", "the four zombies named in the same post (Party Girl, Plumber, Magician, Football Player), four of the nine in the pack Brian asked Marcus for", [], [B["anim_zombies"]]),
]
NOT_POP = [("whoever has to do the next thing", "a definition of the value of 'Who has it' for one line (one person per Owed line), not a set of records to enumerate"),
           ("the count for each state", "three numbers computed from the hand-off list, one per state word; not a set of records")]
# every quantifier sentence of the prompt and of the records that carry the ask (the tool's own list; the template only
# lists the prompt's once a prompt exists)
sys.path.insert(0, str(TOOLS))
import coherence_sweep as _cs, revision_scope as _rs
_files = _cs.task_files(TASK)
_records = _rs.load_records(_files["sql_text"])["records"]
_spans, _seen = [], set()
for q in _cs.quantifier_candidates(_files, _records, None):
    key = (q["where"], q["sentence"])
    if key not in _seen:
        _seen.add(key); _spans.append({"where": q["where"], "span": q["sentence"]})
open_sets, unmatched = [], []
for entry in _spans:
    span = entry["span"]
    hit = [(k, r, ids, bids) for k, r, ids, bids in RULES if k.casefold() in span.casefold()]
    np = [(k, why) for k, why in NOT_POP if k.casefold() in span.casefold()]
    if np and not hit:
        open_sets.append({"span": span, "where": entry.get("where"), "not_a_population": np[0][1]})
    elif hit:
        ids, bids = [], []
        for _, _, i, b in hit:
            ids += [x for x in i if x not in ids]; bids += [x for x in b if x not in bids]
        open_sets.append({"span": span, "where": entry.get("where"), "sources": [], "rule": " · ".join(r for _, r, _, _ in hit), "census": census(ids, bids)})
    else:
        unmatched.append(span[:90])
assert not unmatched, unmatched

# ---------------------------------------------------------------- base consistency (one entry per seeded fact)
base_path = HERE / "out" / "sweep_candidates_base.json"
base = json.loads(base_path.read_text()) if base_path.is_file() and base_path.stat().st_size else {}
settle_path = HERE / "sweep_settlements.json"
settle = json.loads(settle_path.read_text()) if settle_path.is_file() else {}
base_notes = settle.get("base_consistency", {})
base_consistency = []
for entry in tpl["base_consistency"]:
    assert entry["fact"] in base_notes, ("no base check written for the fact", entry["fact"])     # plan/build_settlements.py
    note = base_notes[entry["fact"]]
    base_consistency.append({"fact": entry["fact"], "search": note["search"], "result_count": note["result_count"],
                             "conflicts": note.get("conflicts", []), "disposition": note.get("disposition", "")})

record = {"schema": "coherence-sweep-v1", "bound_to": dict(tpl["bound_to"]), "scope": "full", "universe": tpl.get("universe", "synthcut"),
          "reviewers": reviewers, "forks": settle.get("forks", []), "open_sets": open_sets + settle.get("open_sets_reviewed", []),
          "siblings": settle.get("siblings", []), "base_consistency": base_consistency,
          "known_issues": settle.get("known_issues", [
              {"card": "SC-49", "disposition": "touched by name only: the prompt and the seeded records name Frederick as the sender of a message and the author of the notes; no founder count and no statement of his role is seeded, cited or graded"},
              {"card": "SC-54", "disposition": "touched by name only: nothing about Frederick's pay or the ledger is read, cited or graded"},
              {"card": "SC-70", "disposition": "touched by name only: no seeded text states a time zone or a place; the hold is stored in UTC with the organiser's calendar zone, and the dossier gives UTC with one PST conversion. No value depends on a Slack profile's time zone."}]),
          "conflicts": settle.get("conflicts", []), "dismissed": settle.get("dismissed", [])}
for f in record["forks"]:
    if f.get("status") == "settled_in_data": f.setdefault("rechecked_sql_sha256", sql_sha)
(WF / "01d_Coherence_Sweep.json").write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n")
print("wrote 01d_Coherence_Sweep.json:", len(reviewers), "reviewers,", len(record["forks"]), "forks,", len(record["open_sets"]), "open sets,",
      len(record["siblings"]), "defects,", len(base_consistency), "facts,", len(record["dismissed"]), "dismissed")

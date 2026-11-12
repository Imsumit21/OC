#!/usr/bin/env python3
"""Every seeded record that names another record (seeded or base) is at least as late as the record it names.
Reads the times from 01_Universe_Inject.sql (never executed) and the base times from plan/design_model.py pointers.
Writes out/citation_chronology.txt; exit 1 on any record that cites a later one."""
import datetime as D, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
TASK = HERE.parents[1]
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(TASK.parent / "tools"))
import design_model as M
from base_check import parse_sql
S, B = M.SEED, M.BASE
rows = [r for r in parse_sql((TASK / "01_Universe_Inject.sql").read_text()) if r["op"] == "insert"]
def row(table, **kv):
    for r in rows:
        if r["table"] == table and all(str(r["row"].get(k)) == str(v) for k, v in kv.items()): return r["row"]
    raise KeyError((table, kv))
def iso(s): return D.datetime.fromisoformat(str(s).replace("Z", "+00:00")).astimezone(D.timezone.utc)
def slack_ts(ptr): return D.datetime.fromtimestamp(float(ptr.split("/")[1]), D.timezone.utc)
def doc(i): return row("gdocs.docs_documents", document_id=i)
def drive(i): return row("gdrive.drive_files", id=i)
def note(name): return row("linear.linear_comments", id=M.comment_id("note_" + name))
T = {
 "the ask (sent)": slack_ts(S["ask"]["id"]),
 "the notes (last edit)": iso(doc(S["notes"]["id"])["modified_time"]),
 "the kickoff hold (created)": iso(row("gcal.gcal_events", event_id=S["hold"]["id"])["created"]),
 "the pack list (created)": iso(drive(S["tracker"]["id"])["created_time"]),
 "the pack list (last edit)": iso(drive(S["tracker"]["id"])["modified_time"]),
 "the pack ticket (created)": iso(row("linear.linear_issues", id=M.PACK_TICKET)["created_at"]),
 "the deck (last edit)": iso(drive(S["deck"]["id"])["modified_time"]),
 "Robert's eight (posted)": slack_ts(S["picks"]["id"]),
 "Robert's zombie answer (posted)": slack_ts(S["zpicks"]["id"]),
 "Robert's reply on the bow (posted)": slack_ts(S["c3_reply"]["id"]),
 "Marcus's post": slack_ts(S["a1_post"]["id"]),
 "Robert's note on the bathroom objects": slack_ts(S["a2_dm"]["id"]),
 "base: Robert's new colour versions": slack_ts(B["robert_new_colours"]),
 "Brian's log (last edit)": iso(doc(S["c4_log"]["id"])["modified_time"]),
 "Calvin's sheet (last edit)": iso(drive(S["c2_sheet"]["id"])["modified_time"]),
 "Leonard's Trello comment": iso(row("trello.trello_actions", id=S["trello_note"]["id"])["date"]),
 "note: Zombie characters": iso(note("Zombie characters")["created_at"]),
 "note: Bow": iso(note("Bow")["created_at"]),
 "notes on the three recoloured lines (latest)": max(iso(note(n)["created_at"]) for n in ("Cactus Plant", "Chainsaw", "Cone")),
 "notes on the twelve Thursday exports (latest)": max(iso(note(l["name"])["created_at"]) for l in M.members("A1")),
 "notes on the twelve bathroom files (latest)": max(iso(note(l["name"])["created_at"]) for l in M.members("A2")),
 "notes on the eight zipped instruments (latest)": max(iso(note(l["name"])["created_at"]) for l in M.members("C4")),
 "notes on the two library sounds (latest)": max(iso(note(l["name"])["created_at"]) for l in M.members("C2")),
 "notes on lines not exported (earliest)": min(iso(note(l["name"])["created_at"]) for l in M.members("VIS")),
 "notes on Monday's files (latest)": max(iso(note(l["name"])["created_at"]) for l in M.LINES if l["cls"] == "READY" and l["day"] == M.MON),
 "base: vendor's question on the zombies": slack_ts(B["vendor_zombie_ask"]),
 "base: vendor's new start date": slack_ts(B["vendor_nov3"]),
 "base: Frederick asks for the pause": slack_ts(B["fred_pause"]),
 "base: Julia's bow post": slack_ts(B["art_bow_root"]),
 "base: Claire's answer in the bow thread": slack_ts(B["art_bow_claire"]),
 "base: match3d#462 created": iso("2025-09-25T11:43:06Z"),
 "base: Marcus hands over the zombie pack": slack_ts(B["anim_pack"]),
 "base: Brian sends the pack to the vendor": slack_ts(B["brian_pack3"]),
}
PAIRS = [   # (later record, earlier record it names or answers, why)
 ("the ask (sent)", "the notes (last edit)", "the ask names 'my hand-off notes'"),
 ("the ask (sent)", "the pack list (last edit)", "the ask names Brian's pack list"),
 ("the ask (sent)", "base: vendor's new start date", "the ask names Nov 3"),
 ("the ask (sent)", "Robert's zombie answer (posted)", "the ask names Robert's picks for the zombies"),
 ("the notes (last edit)", "the kickoff hold (created)", "the notes name the kickoff hold"),
 ("the notes (last edit)", "the deck (last edit)", "the notes name Julia's deck"),
 ("the notes (last edit)", "the pack ticket (created)", "the notes name Brian's pack ticket"),
 ("the kickoff hold (created)", "base: vendor's new start date", "the hold is on the vendor's date"),
 ("the pack ticket (created)", "the pack list (created)", "the ticket's description names the pack list"),
 ("the pack list (last edit)", "the pack ticket (created)", "the list's Ticket column holds the children's keys"),
 ("Robert's reply on the bow (posted)", "Robert's eight (posted)", "'the last one on my list'"),
 ("Robert's reply on the bow (posted)", "base: Claire's answer in the bow thread", "reply in the thread"),
 ("note: Bow", "Robert's reply on the bow (posted)", "the bow's file is exported after the arrow thread"),
 ("Robert's zombie answer (posted)", "base: vendor's question on the zombies", "'for PlayableX's question'"),
 ("note: Zombie characters", "base: vendor's question on the zombies", "the note reports their question"),
 ("note: Zombie characters", "base: Brian sends the pack to the vendor", "the note says the pack was sent"),
 ("Marcus's post", "notes on the twelve Thursday exports (latest)", "a later word on Thursday's exports"),
 ("Marcus's post", "base: Marcus hands over the zombie pack", "posted after his own pack"),
 ("Robert's note on the bathroom objects", "notes on the twelve bathroom files (latest)", "a later word on Friday's bathroom files"),
 ("base: match3d#462 created", "notes on the three recoloured lines (latest)", "the art changed after the files were handed over"),
 ("base: Robert's new colour versions", "notes on the three recoloured lines (latest)", "new colour versions after the files were handed over"),
 ("Brian's log (last edit)", "base: Robert's new colour versions", "'Claire sent the three recoloured models again'"),
 ("Brian's log (last edit)", "notes on the eight zipped instruments (latest)", "a later word on Friday's zip"),
 ("Brian's log (last edit)", "base: Frederick asks for the pause", "'when we pick this up again'"),
 ("Brian's log (last edit)", "notes on lines not exported (earliest)", "'a few are still mine to do'"),
 ("notes on lines not exported (earliest)", "notes on Monday's files (latest)", "written after Monday's batch"),
 ("Leonard's Trello comment", "the ask (sent)", "'Julia is pulling the brief ... together for Frederick'"),
 ("Leonard's Trello comment", "base: vendor's new start date", "'the new start PlayableX gave us'"),
]
out, bad = ["Citation chronology (UTC): each record against the record it names or answers", ""], 0
for later, earlier, why in PAIRS:
    ok = T[later] >= T[earlier]
    bad += not ok
    out.append(f"[{'ok' if ok else 'FAIL'}] {later} {T[later]:%d %b %H:%M:%S}  >=  {earlier} {T[earlier]:%d %b %H:%M:%S}  ({why})")
out.append(""); out.append(f"CITATION CHRONOLOGY: {'PASS' if not bad else 'FAIL'} · {len(PAIRS)} pairs · {bad} out of order")
(HERE / "out" / "citation_chronology.txt").write_text("\n".join(out) + "\n")
print(out[-1])
sys.exit(1 if bad else 0)

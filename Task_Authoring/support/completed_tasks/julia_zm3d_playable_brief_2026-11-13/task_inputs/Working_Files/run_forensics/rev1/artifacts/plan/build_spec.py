#!/usr/bin/env python3
"""Write Working_Files/spec/spec.json and texts/ for Task_Authoring/generators (Linear and Slack emitters).
Every value carries its origin; texts are pinned by sha256. The cohort (pack ticket, its children, Brian's notes) and the
six Slack records come from here; the other services are written by plan/build_sql.py. Nothing is executed."""
import datetime as D, hashlib, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
ROOT = WF.parents[2]
sys.path.insert(0, str(HERE))
import design_model as M
import planned_texts as TXT

SPEC = WF / "spec"; TEXTS = SPEC / "texts"
TEXTS.mkdir(parents=True, exist_ok=True)
ctx = json.loads((WF / "00_Task_Context.json").read_text())
UNI = ROOT / "Universe_SynthCut" / "SynthCut_HarmonyGames_Other_Services" / "Services_Data"
BRIAN = "usr_fc22d5941b2aeb5c"

def lit(v, **kw): return {"origin": "authored", "construction": "literal", "value": v, **kw}
def ref(key): return {"origin": "authored", "construction": "reference", "ref": key}
def lbase(coll, rec, field="id"): return {"origin": "base", "construction": "reference", "base": {"service": "linear", "collection": coll, "record": rec, "field": "/" + field}}
def sbase(coll, rec, field="id"): return {"origin": "base", "construction": "reference", "base": {"service": "slack", "collection": coll, "record": rec, "field": "/" + field}}
written = set()
def text(name, body):
    data = body.encode("utf-8")
    (TEXTS / name).write_bytes(data); written.add(name)
    return {"origin": "authored", "construction": "literal", "text": f"texts/{name}", "sha256": hashlib.sha256(data).hexdigest()}
def jit(label, span):
    """A stable 0..span-1 offset in seconds for a label, so stamps do not fall on round seconds."""
    return int(hashlib.sha256(("jit|" + label).encode()).hexdigest()[:8], 16) % span
def at(day, hhmm, label, span=50):
    d = D.datetime.fromisoformat(f"{day}T{hhmm}:00+00:00") + D.timedelta(seconds=jit(label, span) + 5)
    return d.strftime("%Y-%m-%dT%H:%M:%SZ")

DAYS = {M.THU: "2025-09-25", M.FRI: "2025-09-26", M.MON: "2025-09-29"}
def note_time(l, i):
    """When Brian wrote the note on a line's ticket (UTC, inside his posting hours)."""
    n, cls = l["name"], l["cls"]
    def run(day, start, k, step=95):          # notes written one after another, about a minute and a half apart
        base = D.datetime.fromisoformat(f"{day}T{start}:00+00:00") + D.timedelta(seconds=k * step + jit(n, 40))
        return base.strftime("%Y-%m-%dT%H:%M:%SZ")
    if n == "Zombie characters": return "2025-09-29T10:21:17Z"      # after the vendor's 10:16 UTC message of 29 Sep that it had reviewed the pack
    if cls == "W": return run("2025-09-25", "07:23", ORDER["W"].index(n), 58)
    if cls == "C1": return run("2025-09-25", "08:05", ORDER["C1"].index(n), 40)
    if cls == "A1": return run("2025-09-25", "15:21", ORDER["A1"].index(n), 100)
    if cls == "A2": return run("2025-09-26", "11:08", ORDER["A2"].index(n), 75)
    if cls == "C4": return run("2025-09-26", "13:04", ORDER["C4"].index(n), 85)
    if l["kind"] == "Sound" and cls != "VIS": return run("2025-09-26", "14:11", ORDER["SND"].index(n), 70)
    if cls == "VIS": return run("2025-09-29", "12:31", ORDER["VIS"].index(n), 105)     # Monday, after that day's batch: what is still not exported
    return run(DAYS[l["day"]], {M.THU: "08:09", M.FRI: "09:37", M.MON: "11:06"}[l["day"]], ORDER[l["day"]].index(n), 110)
LISTED = [l for l in M.LINES if l["on_list"]]
ORDER = {c: [l["name"] for l in LISTED if l["cls"] == c] for c in ("W", "C1", "A1", "A2", "C4", "VIS")}
ORDER["SND"] = [l["name"] for l in LISTED if l["kind"] == "Sound" and l["cls"] != "VIS"]
for d in (M.THU, M.FRI, M.MON): ORDER[d] = [l["name"] for l in LISTED if l["cls"] == "READY" and l["day"] == d]

records = []
PARENT_CREATED = "2025-09-25T07:05:12Z"
records.append({"key": "PACK", "kind": "linear.issue", "role": "structural", "manifest": ["K4"], "fields": {
    "id": lit(M.PACK_TICKET), "team": lbase("teams", M.TEAM_ID), "title": lit(TXT.PACK_TICKET_TITLE), "state": lit("In Progress"),
    "creator": lbase("users", BRIAN), "assignee": lbase("users", BRIAN), "description": text("PACK.txt", TXT.PACK_TICKET_DESC),
    "project": lit(None), "parent": lit(None), "priority": lit(0), "labels": lit([]), "relations": lit([]),
    "created_at": lit(PARENT_CREATED), "started_at": lit("2025-09-25T07:21:48Z"), "completed_at": lit(None), "canceled_at": lit(None)}})
NOTE_AT = {}
for i, l in enumerate(LISTED):
    key = f"L{i + 1:03d}"
    created = (D.datetime(2025, 9, 25, 7, 6, 3, tzinfo=D.timezone.utc) + D.timedelta(seconds=i * 8 + jit("c" + l["name"], 5))).strftime("%Y-%m-%dT%H:%M:%SZ")
    started = (D.datetime(2025, 9, 25, 7, 21, 52, tzinfo=D.timezone.utc) + D.timedelta(seconds=i // 12 * 3)).strftime("%Y-%m-%dT%H:%M:%SZ")
    nt = note_time(l, i); NOTE_AT[l["name"]] = nt
    done = l["ticket_state"] == "Done"
    completed = None
    if done:   # Brian notes the delivered line, then closes it: no comment falls after the close
        completed = (D.datetime.fromisoformat(nt.replace("Z", "+00:00")) + D.timedelta(seconds=41 + jit("d" + l["name"], 30))).strftime("%Y-%m-%dT%H:%M:%SZ")
    records.append({"key": key, "kind": "linear.issue", "role": "cohort", "manifest": ["cohort"], "fields": {
        "id": lit(l["ticket"]), "team": lbase("teams", M.TEAM_ID), "title": lit(l["name"]), "state": lit(l["ticket_state"]),
        "creator": lbase("users", BRIAN), "assignee": lbase("users", BRIAN), "description": lit(None), "project": lit(None),
        "parent": ref("PACK"), "priority": lit(0), "labels": lit([]), "relations": lit([]), "created_at": lit(created),
        "started_at": lit(started), "completed_at": lit(completed), "canceled_at": lit(None)}})
    records.append({"key": f"N{i + 1:03d}", "kind": "linear.comment", "role": "cohort_evidence", "manifest": ["cohort"], "fields": {
        "id": lit(M.comment_id("note_" + l["name"])), "issue": ref(key), "author": lbase("users", BRIAN),
        "created_at": lit(nt), "body": text(f"N{i + 1:03d}.txt", l["note"])}})

def msg(key, seed, user, body, role, manifest, parent=None):
    ch, _ = M.SEED[seed]["id"].split("/")
    f = {"channel": sbase("channels", ch), "user": sbase("users", user), "at": lit(M.SEED[seed]["at"]), "text": text(f"{key}.txt", body)}
    if parent: f["parent"] = parent
    records.append({"key": key, "kind": "slack.message", "role": role, "manifest": manifest, "fields": f})
U = M.SLACK_USER
msg("ASK", "ask", U["Frederick Stone"], TXT.ASK, "hub", ["A1"])
msg("PICKS", "picks", U["Robert"], TXT.PICKS, "ask_fragment", ["K3"])
msg("ZPICKS", "zpicks", U["Robert"], TXT.ZPICKS, "ask_fragment", ["K10"])
msg("A1POST", "a1_post", U["Marcus Bennett"], TXT.A1_POST, "deciding", ["C1", "T1"])
msg("A2DM", "a2_dm", U["Claire Morgan"], TXT.A2_DM, "deciding", ["C2", "T2"])
bow_ch, bow_ts = M.BASE["art_bow_root"].split("/")
msg("C3REPLY", "c3_reply", U["Robert"], TXT.C3_REPLY, "deciding", ["K11", "T5"], parent=sbase("messages", f"{bow_ch}:{bow_ts}"))

lin_manifest = json.loads((UNI / "linear" / "source_manifest.json").read_text())
lin_pin = next(f for f in lin_manifest["files"] if f["path"] == "data.json")["sha256"]
slack_pin = hashlib.sha256((UNI / "slack" / "source_manifest.json").read_bytes()).hexdigest()
spec = {"spec_version": "hg-gen/1",
        "task": {"slug": M.SLUG, "revision": "rev1", "universe": ctx["universe"]["key"], "freeze_utc": ctx["freeze_utc"],
                 "clock_utc": ctx["universe"]["clock_utc"], "context_hash": ctx["context_hash"]},
        "library": {"emitters": {"linear": "linear/1.0", "slack": "slack/1.0"}},
        "snapshot": {"linear": {"file": "data.json", "sha256": lin_pin}, "slack": {"file": "source_manifest.json", "sha256": slack_pin}},
        "records": records}
(SPEC / "spec.json").write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
for f in TEXTS.iterdir():
    if f.name not in written: f.unlink()
# no two notes in the same second, and two notes with different wording at least 20 s apart (one person typing)
_seq = sorted((NOTE_AT[l["name"]], l["note"], l["name"]) for l in LISTED)
_gap = lambda a, b: (D.datetime.fromisoformat(b.replace("Z", "+00:00")) - D.datetime.fromisoformat(a.replace("Z", "+00:00"))).total_seconds()
_bad = [(a[2], b[2], _gap(a[0], b[0])) for a, b in zip(_seq, _seq[1:]) if _gap(a[0], b[0]) < (1 if a[1] == b[1] else 20)]
assert not _bad, ("note times too close", _bad)
(HERE / "out" / "note_times.json").write_text(json.dumps(NOTE_AT, indent=0) + "\n")
print("spec:", len(records), "records;", len(written), "texts; note times", min(NOTE_AT.values()), "to", max(NOTE_AT.values()))

#!/usr/bin/env python3
"""Build Working_Files/01_Hardness_Manifest.json (final, /create-injection) from the certified draft + the SQL ids.

Every draft element id is kept; changes are listed in design_delta. Adds what only the SQL settles: Slack 32-hex row ids
and Gmail message rows for seeded records, the records' real timestamps, the facts sheet with home_ids, solver
{path, digest} and gradable_surface. Note-based facts are found by their words in plan/sql_ids.json, so a reworded note
drops its fact (printed) instead of breaking the build. preflight {report, digest} is not written back: the preflight
report binds this file by sha256, so a digest written here would make the report stale.
"""
import copy, hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from hardness_gate import RecordText  # noqa: E402

draft = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json")))
S = json.load(open(os.path.join(HERE, "sql_ids.json")))
I = json.load(open(os.path.join(HERE, "ids.json")))
IDS, BASE = I["IDS"], I["BASE"]
SQL_TEXT = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
ROB, LEO, ART = "robert@harmonygames.co", "leonard.hayes@harmonygames.co", "arthur.blake@harmonygames.co"
man = copy.deepcopy(draft)
man["_note"] = ("Final manifest (/create-injection rev1). Draft 01_Hardness_Manifest.draft.json (scenario-certified design-1) plus "
                "the ids, timestamps, facts and bindings only the SQL settles; every change is in design_delta.")
delta = []
rt = RecordText(SQL_TEXT)


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


# ---------------------------------------------------------------- id maps
SLACK = {v["locator"]: v["id"] for v in S["slack"].values()}            # 'C/ts' -> 32-hex row id (seeded messages only)
GM_THREAD_TO_MSG = {}                                                    # a seeded thread id -> its first message row
for key, boxes in S["gmail"].items():                                    # (Leonard's reply shares the thread of Arthur's mail)
    for box, ids in boxes.items():
        GM_THREAD_TO_MSG.setdefault(ids["thread"], ids["message"])
# base Robert threads whose single time the gate reads: the message, by file pointer (a Gmail thread has no one time)
GM_BASE_MSG = {BASE["n_ban_first"]: "gmail:threads/00004088.json /messages/0", BASE["n_ban_resend"]: "gmail:threads/00004124.json /messages/0",
               BASE["lb_await"]: "gmail:threads/00001577.json /messages/0", BASE["jpm_notice"]: "gmail:threads/00006272.json /messages/0"}


def map_id(x):
    if not isinstance(x, str):
        return x
    return SLACK.get(x) or GM_THREAD_TO_MSG.get(x) or x


def map_list(xs):
    out = []
    for x in xs or []:
        m = map_id(x)
        for y in ([m, x] if m != x and x in GM_THREAD_TO_MSG else [m]):
            if y not in out:
                out.append(y)
    return out


def iso(when):
    return when.strftime("%Y-%m-%dT%H:%M:%SZ")


ANCHOR_LOCS = {a["locator"] for a in man["anchors"]}
for f in man["ask_fragments"]:
    f["seeded_ids"] = map_list(f.get("seeded_ids"))
    if f.get("delegated_by_record") not in ANCHOR_LOCS:                  # a delegation by the anchor keeps the anchor's own locator
        f["delegated_by_record"] = map_id(f.get("delegated_by_record"))
    if f["service"] == "gmail":
        f["locator"] = map_id(f["locator"])
for a in man["authorities"]:
    a["seeded_ids"] = map_list(a.get("seeded_ids"))
    a["decoy_seeded_ids"] = map_list(a.get("decoy_seeded_ids"))
moved_at = []
for t in man["traps"]:
    t["seeded_ids"] = map_list(t.get("seeded_ids"))
    for v in t.get("version_records") or []:
        if v.get("seeded"):
            v["id"] = map_id(v.get("id"))
        elif v.get("base_pointer") in GM_BASE_MSG:
            v["base_pointer"] = GM_BASE_MSG[v["base_pointer"]]
        when, why = rt.time_of(v.get("id") or v.get("base_pointer"))
        if when is None:
            raise SystemExit(f"{t['id']}: no timestamp for {v}: {why}")
        if iso(when) != v.get("at"):
            moved_at.append(f"{t['id']} {str(v.get('id') or v.get('base_pointer'))[:40]} {v.get('at')} -> {iso(when)}")
        v["at"] = iso(when)
    if t.get("version_records"):
        t["version_records"] = sorted(t["version_records"], key=lambda v: v["at"])
for c in man["chains"]:
    for h in c["hops"]:
        h["record"] = map_id(h["record"])
for s_ in man["cohort"].get("evidence_surfaces", []):
    s_["seeded_ids"] = map_list(s_.get("seeded_ids"))
for p in man["mechanism_portfolio"]:
    if p["id"] == "ALIAS" and "Leapblock" not in p["controls"]:
        p["controls"].append("Leapblock")

delta += [
    {"id": "record ids (all elements)",
     "change": "Slack 'channel/ts' pointers to seeded messages -> their 32-hex row ids; Gmail thread pointers to seeded mail -> the "
               "message row that carries the text (thread ids kept alongside in seeded_ids)",
     "reason": "the gate reads text and timestamps from SQL rows: a Slack row is keyed by its id and a Gmail thread row holds only a snippet"},
    {"id": "version_records base mail", "change": "Gmail base pointers in T1, T3, T4 and T10 -> 'gmail:threads/<file>.json /messages/<n>'",
     "reason": "a Gmail thread has no single time (hardness_gate supersession_chronology); the file pointer names the message that dates the version"},
    {"id": "version_records at", "change": "'at' read from each record: " + ("; ".join(moved_at) or "no value moved"),
     "reason": "the draft's times were planned; the gate compares the records' own timestamps (a Drive-family record dates by modified_time)"},
    {"id": "ALIAS controls", "change": "controls ['Adjoe'] -> ['Adjoe', 'Leapblock']",
     "reason": "alias_over moves a studio such as Leapblock into Marketing; Adjoe is already Marketing, so the operator can't move it and "
               "oracle_kit contract.controls needs a control it moves. Adjoe stays as a member that holds"},
    {"id": "seeded ids not cited (c_helper)", "change": "IDS c_helper (cnt_7f7ab446e59c) has no row in the SQL and no manifest element cites it",
     "reason": "the design's record plan seeds one contact, cnt_df6a482c50c0 for ENG-2455; ids.json keeps a minted spare"},
    {"id": "hold copies and invitations", "change": f"K6 cites Robert's copy {S['gcal'][ROB]} only; the other calendar copies "
     f"({', '.join(v for k_, v in sorted(S['gcal'].items()) if k_ != ROB)}) and the invitation threads "
     f"({', '.join(b['thread'] for k_, v in sorted(S['gmail'].items()) if k_.startswith('invite') for b in v.values())}) are in the SQL, cited by no element",
     "reason": "reach is proven on the persona's own copy; the design relies on neither (section 11, invitation optional)"},
    {"id": "issue notes", "change": "comment ids are not cited by any element; the issue keys are, and the notes are read through plan/sql_ids.json",
     "reason": "a note's wording and count can change with the row plan; the issue is the stable record"},
]

# ---------------------------------------------------------------- facts (fact_check --no-leak)
L, GM = S["linear"], S["gmail"]
MAIL = [GM["arthur_mail"][b]["message"] for b in (ART, ROB, LEO)]
STATEMENT, METHOD, SHEET, DECK = S["slack"]["statement"]["id"], IDS["method"], IDS["sheet"], IDS["deck"]
facts = [
    {"key": "the first one", "value": "33,290", "kind": "status", "home_ids": [STATEMENT]},
    {"key": "wires Leapblock received", "value": "407,944", "kind": "status", "home_ids": [STATEMENT]},
    {"key": "the wire count", "value": "over 30 wires", "kind": "status", "home_ids": [STATEMENT]},
    {"key": "the JPMorgan wire", "value": "$4,000", "kind": "amount", "home_ids": MAIL},
    {"key": "JPMorgan account", "value": "that was our own Chase account", "kind": "status", "home_ids": MAIL},
    {"key": "returned wire rule", "value": "Take a notice as paid unless one of us has said the money came back", "kind": "status", "home_ids": [METHOD]},
    {"key": "receipt rule", "value": "it goes in only if a receipt for it reached your mail, at the amount sent, not the fee", "kind": "status", "home_ids": [METHOD]},
    {"key": "own accounts rule", "value": "Money we moved between our own accounts isn’t spending", "kind": "status", "home_ids": [METHOD]},
    {"key": "bucket rule", "value": "Marketing is anything made or bought to get installs", "kind": "status", "home_ids": [METHOD]},
    {"key": "date rule", "value": "Go by the Transaction Date on the notice, the whole payment to one bet", "kind": "status", "home_ids": [METHOD]},
    {"key": "currency rule", "value": "Anything not paid in dollars stays in its own currency next to the line", "kind": "status", "home_ids": [METHOD]},
    {"key": "Domino Delights up to", "value": "Jan 8, 2025", "kind": "date", "home_ids": [METHOD]},
    {"key": "ZM from", "value": "Jan 9, 2025", "kind": "date", "home_ids": [METHOD]},
    {"key": "Combo Fighter from", "value": "Nov 24, 2025", "kind": "date", "home_ids": [METHOD]},
    {"key": "quick pass Domino Delights", "value": "984,888.21", "kind": "status", "home_ids": [SHEET]},
    {"key": "quick pass ZM", "value": "608,820.50", "kind": "status", "home_ids": [SHEET]},
    {"key": "quick pass Combo Fighter", "value": "73,685.61", "kind": "status", "home_ids": [SHEET]},
    {"key": "deck Domino Delights", "value": "$985K", "kind": "status", "home_ids": [DECK]},
    {"key": "deck ZM", "value": "$609K", "kind": "status", "home_ids": [DECK]},
    {"key": "deck Combo Fighter", "value": "$74K", "kind": "status", "home_ids": [DECK]},
]
NOTE_FACTS = [("MotMot", "MotMot note", "that's MotMot"), ("Lucas", "Lucas note", "that's Lucas, mini games dev"),
              ("Node Media", "Node note", "one payment when we closed the account"), ("JPMorgan", "JPMorgan note", "think it was an advance to one of the contractors"),
              ("Lauren Brooks", "Brooks note", "the contract I sent out in Oct"), ("Martin Walsh", "Martin note", "paid him direct for this one"),
              ("4X helper", "proposal helper note", "not one of the three games")]
dropped = []
for payee, key, words in NOTE_FACTS:
    hits = [c for c in L[payee]["comments"] if words in c["text"].replace("\u2019", "'")]     # Leonard types curly apostrophes
    if hits:
        at = hits[0]["text"].replace("\u2019", "'").index(words)
        facts.append({"key": key, "value": hits[0]["text"][at:at + len(words)], "kind": "status", "home_ids": [c["id"] for c in hits]})
    else:
        dropped.append(key)
man["facts"] = facts

# ---------------------------------------------------------------- bindings
man["solver"] = {"path": "Working_Files/solver/solver.py", "digest": sha(os.path.join(WF, "solver", "solver.py"))}
man["gradable_surface"] = "01_Gradable_Surface.json"
man["design_delta"] = delta
with open(os.path.join(WF, "01_Hardness_Manifest.json"), "w") as out:
    json.dump(man, out, indent=1)
    out.write("\n")

# ---------------------------------------------------------------- self-check: every seeded id is an exact token outside comments
body = "\n".join(l for l in SQL_TEXT.splitlines() if not l.startswith("--"))
miss = []
for sec in ("ask_fragments", "authorities", "traps"):
    for el in man[sec]:
        for k in ("seeded_ids", "decoy_seeded_ids"):
            for x in el.get(k) or []:
                if x and not re.search(r"(?<![\w-])" + re.escape(x) + r"(?![\w-])", body):
                    miss.append(f"{sec}:{el['id']}:{k}:{x}")
        for v in el.get("version_records") or []:
            if v.get("seeded") and not re.search(r"(?<![\w-])" + re.escape(str(v.get("id"))) + r"(?![\w-])", body):
                miss.append(f"{sec}:{el['id']}:version_records:{v.get('id')}")
print("wrote 01_Hardness_Manifest.json:", len(facts), "facts,", len(delta), "design_delta entries; seeded ids not in the SQL:", miss or "none",
      "; note facts dropped:", dropped or "none")

#!/usr/bin/env python3
"""Build Working_Files/01_Hardness_Manifest.json (final, /create-injection) from the certified draft + the SQL ids.

Every draft id is kept; changes are listed in design_delta. Adds what only the SQL settles: real ids for placeholder
version records, the facts sheet with home_ids, integration_exceptions, solver {path, digest}, gradable_surface and
(when 01c_Preflight_Report.json exists) preflight {report, digest}. Re-run after any SQL/solver/preflight change.
"""
import copy
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
draft = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json")))
ids = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
man = copy.deepcopy(draft)
man["_note"] = ("Final manifest (/create-injection rev4). Draft 01_Hardness_Manifest.draft.json (scenario-certified "
                "design-2, 84fea705bc87) plus the ids, facts and bindings only the SQL settles; every change is in design_delta.")


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


FRED = "frederick.stone@harmonygames.co"
MBOX = [FRED, "leonard.hayes@harmonygames.co", "robert@harmonygames.co", "arthur.blake@harmonygames.co"]
PILOT_PAPER = ids["papers"]["Clipforge"]
NOTICE_MSG = ids["msg"]["clipforge_notice"]
WELCOME_MSG = ids["msg"]["Clipforge:0"]
ESG_NOTE_MID = ids["msg"]["esg_note"].split("/", 1)[1]
ESG_ACK_MID = ids["msg"]["esg_ack"].split("/", 1)[1]
SLACK = ids["slack_mid"]

delta = [dict(e, reason=e.get("why", "")) for e in draft.get("design_delta", [])]   # the scenario's design-2 entries

# ---- SQL row ids: Slack messages are keyed by their 32-hex id, Gmail text lives on message rows (not thread rows)
import sys  # noqa: E402
import datetime as _dt  # noqa: E402
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402

SQL_TEXT = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
SLACK_ID, MSGS = {}, {}
for x in parse_sql(SQL_TEXT):
    if x.get("op") != "insert":
        continue
    r = x["row"]
    if x["table"] == "slack.slack_messages":
        SLACK_ID[f"{r['channel_id']}/{r['ts']}"] = r["id"]
    elif x["table"] == "gmail.gmail_messages":
        MSGS.setdefault(r["thread_id"], []).append(r)
for v in MSGS.values():
    v.sort(key=lambda r: int(r["internal_date"]))


def _ms(iso):
    return int(_dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp() * 1000)


def msg_for(thread, quote=None, at=None):
    """The message row in `thread` that carries `quote` (or was sent at `at`; else the first one)."""
    ms = MSGS.get(thread) or []
    if quote:
        q = " ".join(quote.split()).lower()
        hit = [r for r in ms if q in " ".join(f"{r.get('subject') or ''} {r.get('body_text') or ''}".split()).lower()]
        if hit:
            return hit[0]["id"]
    if at:
        hit = [r for r in ms if abs(int(r["internal_date"]) - _ms(at)) < 60000]
        if hit:
            return hit[0]["id"]
    return ms[0]["id"] if ms else None


def sl(x):
    return SLACK_ID.get(x, x) if isinstance(x, str) else x


def sl_list(xs):
    return [sl(x) for x in xs or []]


for f in man["ask_fragments"]:
    f["seeded_ids"] = sl_list(f.get("seeded_ids"))
    rec = f.get("delegated_by_record")
    if rec in SLACK_ID:
        f["delegated_by_record"] = SLACK_ID[rec]
    elif rec in MSGS:
        f["delegated_by_record"] = msg_for(rec, f.get("delegation_quote"))
    if f["service"] == "gmail":
        thread = f["container"] if f["container"] in MSGS else None
        quotes = [f.get("delegation_quote")] + [n["quote"] for n in f.get("names_authorities") or []]
        mids = []
        for q in quotes:
            m = msg_for(thread, q) if thread else None
            if m and m not in mids:
                mids.append(m)
        # every message of the container thread in Frederick's mailbox belongs to the fragment (a later fragment may
        # be delegated by another message of the same thread, e.g. Leonard's acknowledgement under ESG's note)
        rest = [r["id"] for r in MSGS.get(thread, []) if r["id"].startswith(FRED + "/") and r["id"] not in mids]
        if mids:
            f["locator"] = mids[0]
            f["seeded_ids"] = mids + rest + [x for x in f["seeded_ids"] if x not in mids and x not in rest]
for a in man["anchors"]:
    if a["service"] == "gmail" and a["record"] in MSGS:
        hub_msg = msg_for(a["record"])
        delta.append({"id": f"anchor {a['id']}", "change": f"record/locator {a['record']} -> {hub_msg} (the thread is kept "
                      "in every fragment's seeded_ids)", "reason": "the anchor's text is on Leonard's message row"})
        a["record"] = a["locator"] = hub_msg
for a in man["authorities"]:
    a["seeded_ids"] = sl_list(a.get("seeded_ids"))
    a["decoy_seeded_ids"] = sl_list(a.get("decoy_seeded_ids"))
    a["seeded_ids"] = [m for t in a["seeded_ids"] for m in ([msg_for(t)] if t in MSGS else []) + [t]]
for t in man["traps"]:
    t["seeded_ids"] = sl_list(t.get("seeded_ids"))
    for v in t.get("version_records") or []:
        if v.get("seeded") and v.get("id") in SLACK_ID:
            v["id"] = SLACK_ID[v["id"]]
        elif v.get("seeded") and v.get("id") in MSGS:
            v["id"] = msg_for(v["id"], at=v.get("at"))
for c in man["chains"]:
    for h in c["hops"]:
        h["record"] = sl(h["record"])
for s_ in man["cohort"].get("evidence_surfaces", []):
    s_["seeded_ids"] = sl_list(s_.get("seeded_ids"))
delta.append({"id": "record ids (all elements)",
              "change": "Slack 'channel/ts' pointers to seeded messages -> the messages' 32-hex row ids; Gmail fragment "
                        "locators, delegating records, authority records and version records -> the message row that "
                        "carries the quoted words or was sent at the declared time (thread ids kept alongside)",
              "reason": "the gate reads text and timestamps from SQL rows: a Slack message row is keyed by its id, and "
                        "a Gmail thread row holds only a snippet"})

# ---- T5: the pilot agreement's real id (the draft named it by a placeholder before the SQL minted it)
for t in man["traps"]:
    if t["id"] == "T5":
        for v in t["version_records"]:
            if v["id"] == "clipforge-pilot-agreement":
                v["id"] = PILOT_PAPER
                v["container"] = f"file:{PILOT_PAPER}"
        delta.append({"id": "T5 version_records[0]", "change": f"placeholder 'clipforge-pilot-agreement' -> {PILOT_PAPER}",
                      "reason": "the pilot agreement's Drive id is minted by the SQL builder (f_ + 22 hex)"})

# ---- T7's acknowledgement and T17's Retainly terms: placeholders in the draft, minted by the SQL builder
for t in man["traps"]:
    if t["id"] == "T7":
        for v in t["version_records"]:
            if str(v["id"]).endswith("#ack"):
                old = v["id"]
                v["id"] = ids["msg"]["esg_ack"]
                delta.append({"id": "T7 version_records[2]", "change": f"placeholder {old} -> {v['id']}",
                              "reason": "Leonard's acknowledgement is its own message row in the ESG thread"})
    if t["id"] == "T17":
        new = ids["papers"]["Retainly"]
        t["seeded_ids"] = [new if x == "retainly-terms" else x for x in t["seeded_ids"]]
        delta.append({"id": "T17 seeded_ids", "change": f"placeholder 'retainly-terms' -> {new}",
                      "reason": "Retainly's trial terms doc id is minted by the SQL builder"})

# ---- rev2: K7's delegation quote follows the guardrails doc's forward-looking wording (platform /injection C-adv 1)
NEW_K7 = "comes back at the January commitments review I'll put on our calendars"
for f in man["ask_fragments"]:
    if f["id"] == "K7" and f.get("delegation_quote") != NEW_K7:
        delta.append({"id": "K7 delegation_quote", "change": f"{f['delegation_quote']!r} -> {NEW_K7!r}",
                      "reason": "rev2: the guardrails doc (Sep 26) predates the review event (Sep 29); it now announces the "
                                "review instead of citing it as already on the calendars (platform /injection C-adv 1)"})
        f["delegation_quote"] = NEW_K7

# ---- rev3: descriptive texts follow the rev3 records (blind fork sweep, brief stage)
for t in man["traps"]:
    if t["id"] == "T3":
        t["resolver"] = t["resolver"].replace("no new publishing deals before the raise", "Southeast Asia has to wait until after the raise")
for c in man["chains"]:
    for h in c["hops"]:
        h["finding"] = h["finding"].replace("no new publishing deals before the raise", "Southeast Asia waits until after the raise")
if isinstance(man.get("requirements"), dict) and "R1" in man["requirements"]:
    man["requirements"]["R1"] = man["requirements"]["R1"].replace("ad networks and Singular", "ad networks, PlayableX, Craftsman+ and Singular")
delta.append({"id": "rev4 record wording", "change": "Framewell's waiver names Maren and the Pro plan; Leonard's Lanternfly answer is a reply in the DM thread under his Sep 17 'we have no localization though' (root counters updated) and names Wen and the Southeast Asia deal; Robert's Spotlight note names the Dec 5 indie showcase and Rina; the Spotlight call's description no longer states the answer; Hootline's ask moves to Aug 12 and its filed paper is dropped (terms in the Aug 5 mail)",
              "reason": "the rev3 Opus pre-check found every named correction by a company-name or 'told'/'vendor' Slack search and built its cohort from the Aug 15+ inbox, the paperwork folder and the July tracker (01a_Hardening_Report.md §10 M1-M4); truth values are unchanged"})
delta.append({"id": "rev3 record wording", "change": "hub names PlayableX and Craftsman+ with the UA exclusions; guardrails say offers to take up before January count as cash and offers open after January park; Framewell's hold has nothing to sign; Leonard's Lanternfly DM is region-specific; Arthur's ZOM-567 comment settles the officer step, Oct 15 and no ESG triggers; Spotlight and Motive Forge answers are plain noes; explicit dates for Brightlane, Ascendo, Reviewly, Playfuse; Markward has no rolling term; Bundlehouse needs signing; Retainly, Benchmarkly, Driftwood ask a question; UA doc and Playfuse template wording match the base",
              "reason": "a blind fork sweep of Frederick-visible records (brief stage) found readings no record settled; each change keeps the solver's truth (the Lanternfly told text is read from the DM)"})

# ---- controls: the over-application targets named in the draft are control members too
EXTRA_CONTROLS = {
    "DONE": "Retainly (analytics trial, converts Jan 12, nothing to accept: Park)",
    "COMPL": "Glyphworks (font quote nobody has answered: Park, gets a written answer)",
    "FILT": "Playable Factory (cold pitch nobody answered: off the log)",
    "SIGN": "Echohall (free plan continues, nothing to accept: Park)",
}
for e in man["mechanism_portfolio"]:
    if e["id"] in EXTRA_CONTROLS:
        e["controls"] = list(e.get("controls") or []) + [EXTRA_CONTROLS[e["id"]]]
        delta.append({"id": f"mechanism_portfolio.{e['id']}.controls",
                      "change": f"added {EXTRA_CONTROLS[e['id']].split(' (')[0]} as a control member",
                      "reason": "the draft's over_application already acts on this member; the solver contract "
                                "(contract.controls) needs the operator to move a declared control"})

# ---- facts (per-record facts carry home_ids; values chosen so each is stated only in its carrier rows)
B_IDS = json.load(open(os.path.join(HERE, "ids.json")))
B_IDS = B_IDS.get("ids", B_IDS)
facts = [
    {"key": "Nintendo officer step", "value": "Global ToS and NDA", "kind": "status",
     "home_ids": ["cmt_c9a6660d81e067ad1de7"]},
    {"key": "ZOM-567 lapse date", "value": "Oct 15", "kind": "date", "must_appear_in": ["cmt_c9a6660d81e067ad1de7"]},
    {"key": "Framewell waiver", "value": "no charge until Feb 1", "kind": "status",
     "home_ids": [SLACK["framewell_waiver_reply"]]},
    {"key": "Lanternfly call-back", "value": "Southeast Asia has to wait until after the raise", "kind": "status",
     "home_ids": [SLACK["lanternfly_dm"]]},
    {"key": "keep-running night pager", "value": "night pager for backend outages", "kind": "status",
     "home_ids": [ids["keep_items"][2]]},
    {"key": "Clipforge workspace", "value": "HG-2291", "kind": "id",
     "must_appear_in": [PILOT_PAPER, NOTICE_MSG, WELCOME_MSG]},
    {"key": "Paylane cancellation address", "value": "billing@paylane.io", "kind": "id", "home_ids": [NOTICE_MSG]},
    {"key": "Pixel Harbor deposit", "value": "$2,400", "kind": "amount",
     "home_ids": [ids["papers"]["Pixel Harbor Events"], ids["msg"].get("Pixel Harbor Events:0", "")]},
    {"key": "partner-booked travel", "value": "even when a partner books them", "kind": "status",
     "home_ids": [SLACK["amendment_root"]]},
    {"key": "July signing note superseded", "value": "This replaces what I said in July", "kind": "status",
     "home_ids": [f"{mb}/{ESG_ACK_MID}" for mb in MBOX]},
    {"key": "ESG officer rule", "value": "Only an officer, you or Arthur, accepts terms", "kind": "status",
     "home_ids": [f"{mb}/{ESG_NOTE_MID}" for mb in MBOX]},
    {"key": "keep-running card", "value": "Keep-running list (don't cut)", "kind": "status",
     "must_appear_in": [B_IDS["keep_card"]]},
    {"key": "Spotlight answer", "value": "sitting this one out this year", "kind": "status",
     "home_ids": [SLACK["spotlight_note"]]},
    {"key": "Hootline ask", "value": "would you like to keep the scheduler after that", "kind": "status",
     "home_ids": [ids["msg"]["Hootline:1"]]},
    {"key": "log sheet name", "value": "Q4 commitments log", "kind": "status", "home_ids": [B_IDS["readme_doc"]]},
]
man["facts"] = facts
man["integration_exceptions"] = [
    {"record_id": "24cbd5ab34e4c9c132384aae9cf0a03c@hg4",
     "reason": "no_notify: Frederick organized the Jul 14 UGC Studio kickoff himself; the only other attendee is "
               "Clipforge's Priya Raman (external), so no invitation mail lands in any HarmonyGames mailbox"}]
man["solver"] = {"path": "Working_Files/solver/solver.py", "digest": sha(os.path.join(WF, "solver", "solver.py"))}
man["gradable_surface"] = "01_Gradable_Surface.json"
# No preflight {report, digest} here: tools/preflight_report.py binds this manifest by sha256, so a digest of the report
# written back into the manifest would make the preflight stale (the binding runs report -> manifest; dossier §Self-review).
man["design_delta"] = delta
json.dump(man, open(os.path.join(WF, "01_Hardness_Manifest.json"), "w"), indent=1)
open(os.path.join(WF, "01_Hardness_Manifest.json"), "a").write("\n")
print("wrote 01_Hardness_Manifest.json:", len(facts), "facts,", len(delta), "design_delta entries,",
      "(preflight binds this file; see the note above)")

# ---- every seeded id cited must be an exact SQL token
import re as _re  # noqa: E402
_body = "\n".join(l for l in SQL_TEXT.splitlines() if not l.startswith("--"))
_miss = []
for sec in ("ask_fragments", "authorities", "traps"):
    for el in man[sec]:
        for k in ("seeded_ids", "decoy_seeded_ids"):
            for x in el.get(k) or []:
                if x and not _re.search(r"(?<![\w-])" + _re.escape(x) + r"(?![\w-])", _body):
                    _miss.append(f"{sec}:{el['id']}:{k}:{x}")
        for v in el.get("version_records") or []:
            if v.get("seeded") and not _re.search(r"(?<![\w-])" + _re.escape(str(v.get("id"))) + r"(?![\w-])", _body):
                _miss.append(f"{sec}:{el['id']}:version_records:{v.get('id')}")
print("seeded ids not in the SQL:", _miss or "none")

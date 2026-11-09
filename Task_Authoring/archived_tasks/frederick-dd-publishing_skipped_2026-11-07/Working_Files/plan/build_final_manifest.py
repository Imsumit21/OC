#!/usr/bin/env python3
"""Build Working_Files/01_Hardness_Manifest.json (final, /create-injection) from the certified draft + the SQL ids.

Every draft id is kept; changes are listed in design_delta. Adds what only the SQL settles: Slack and Gmail row ids, the
facts sheet with home_ids, solver {path, digest} and gradable_surface. No preflight digest here: preflight_report.py binds
this manifest by sha256, so a digest of the report written back would make the preflight stale.
Re-run after any SQL or solver change.
"""
import copy, datetime as _dt, hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
sys.path.insert(0, os.path.join(WF, "solver"))
from base_check import parse_sql  # noqa: E402
import solver as SV  # noqa: E402

draft = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json")))
ids = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
man = copy.deepcopy(draft)
man["_note"] = ("Final manifest (/create-injection rev2). Draft 01_Hardness_Manifest.draft.json plus the ids, facts and "
                "bindings only the SQL settles; every change is in design_delta.")
FRED = "frederick.stone@harmonygames.co"
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
delta = []


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def _ms(iso):
    return int(_dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp() * 1000)


def msg_for(thread, quote=None, at=None):
    ms = MSGS.get(thread) or []
    if quote:
        q = " ".join(quote.split()).lower()
        hit = [r for r in ms if q in " ".join(f"{r.get('subject') or ''} {r.get('body_text') or ''}".replace("\\r", " ").replace("\\n", " ").split()).lower()]
        if hit:
            return hit[0]["id"]
    if at:
        hit = [r for r in ms if abs(int(r["internal_date"]) - _ms(at)) < 60000]
        if hit:
            return hit[0]["id"]
    return ms[-1]["id"] if ms else None


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
        rest = [r["id"] for r in MSGS.get(thread, []) if r["id"].startswith(FRED + "/") and r["id"] not in mids]
        if mids:
            f["locator"] = mids[0]
            f["seeded_ids"] = mids + rest + [x for x in f["seeded_ids"] if x not in mids and x not in rest]
for a in man["anchors"]:
    if a["service"] == "gmail" and a["record"] in MSGS:
        hub_msg = msg_for(a["record"])
        delta.append({"id": f"anchor {a['id']}", "change": f"record/locator {a['record']} -> {hub_msg} (thread kept in the fragments' seeded_ids)",
                      "reason": "the anchor's text is on Leonard's message row"})
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
              "change": "Slack 'channel/ts' pointers to seeded messages -> the messages' 32-hex row ids; Gmail fragment locators, delegating records and version records -> the message row that carries the quoted words or was sent at the declared time (thread ids kept alongside)",
              "reason": "the gate reads text and timestamps from SQL rows: a Slack message row is keyed by its id, and a Gmail thread row holds only a snippet"})

# ---- controls and channels: the portfolio's descriptive strings become solver keys and operators
for e in man["mechanism_portfolio"]:
    r = SV.RULES[e["id"]]
    e["description_controls"] = e.get("controls")
    e["controls"] = list(r["controls"])
    e["over_application"] = r["over_application"]
man["channels"] = [dict(id=k, **v) for k, v in SV.CHANNELS.items()]
delta.append({"id": "mechanism_portfolio controls and channels",
              "change": "controls name solver keys (FILT's are Homa and NCsoft, two out-of-scope rows); over_application names the solver operator; the draft's wording stays in description_controls; each channel gets its own operator, kind scale and latent member, and CH-SLIP's slot id V12_PF follows the surface id V12_Harbor",
              "reason": "contract.controls needs declared members to be solver keys and operators solve() accepts; three members sit on two channels, so one shared operator would not be separable"})

# ---- facts
SL, MSG, I = ids["slack_mid"], ids["msg"], SV.I
facts = [
    {"key": "Oakline wire returned", "value": "never hit the account", "kind": "status", "home_ids": [SL["arthur_cash"]]},
    {"key": "Tallwater advance", "value": "The advance is $40,000 now", "kind": "status", "home_ids": list(ids["events"]["pb_event"].values())},
    {"key": "Kestrel freeze", "value": "frozen every outside signing", "kind": "status", "home_ids": [SL["kestrel_post"]]},
    {"key": "Copperleaf terms", "value": "28% of net", "kind": "status", "home_ids": [SL["copperleaf_relay"]]},
    {"key": "Redwood terms", "value": "24% of net", "kind": "status", "home_ids": [I["eng2362_comment"]]},
    {"key": "Sunfold installs", "value": "only commit 30,000 installs a month", "kind": "status", "home_ids": [I["sunfold_comment"]]},
    {"key": "signing date", "value": "Nov 14", "kind": "date", "must_appear_in": [MSG["esg_note"], MSG["esg_leo"]]},
    {"key": "organic figure line", "value": "hears the organic figure from us", "kind": "status", "home_ids": [SL["standing_line"]]},
    {"key": "Northglow grant", "value": "all digital storefronts and platforms", "kind": "status", "home_ids": [SV.B.term("Northglow Publishing")]},
    {"key": "Pinegrove grant", "value": "full source code and build pipeline", "kind": "status", "home_ids": [SV.B.term("Pinegrove Games")]},
    {"key": "model sheet name", "value": "DD publishing model", "kind": "status", "must_appear_in": [I["rule_doc"]]},
]
man["facts"] = facts
man["integration_exceptions"] = [
    {"record_id": ids["uid"][k], "reason": f"no_notify: Frederick organized the {n} himself; the only other attendee is external, so no invitation mail lands in any HarmonyGames mailbox"}
    for k, n in (("harbor_event", "Harbor Lane call"), ("wavecrest_event", "Wavecrest call"))]

# ---- gate readers: quotes sit on a record the gate can read, version records on message rows
BOARD_MSG = "gmail:threads/frederick@harmonygames.co_1830890312657338682.json /messages/0"
for f in man["ask_fragments"]:
    if f["id"] == "K1":
        f["names_authorities"] = [{"id": "H1", "quote": "ground rules"}]
    if f["id"] == "K3":
        f["seeded_ids"] = [I["rule_doc"]]
for t in man["traps"]:
    if t["id"] == "T13":
        for v in t["version_records"]:
            if v.get("base_pointer", "").endswith("/1830890312657338682"):
                v["base_pointer"] = BOARD_MSG
delta.append({"id": "K1, K3, T13 record pointers", "change": "K1 names H1 by the words in its own title; K3 carries the rule doc whose sentence names the August position beside the base sync doc; T13's first version points at the Apr 30 message row inside the board thread",
              "reason": "the gate reads a name from the fragment's own record and a timestamp from a message row, not a thread"})
man["solver"] = {"path": "Working_Files/solver/solver.py", "digest": sha(os.path.join(WF, "solver", "solver.py"))}
man["gradable_surface"] = "01_Gradable_Surface.json"
man["design_delta"] = list(draft.get("design_delta") or []) + delta
out = os.path.join(WF, "01_Hardness_Manifest.json")
json.dump(man, open(out, "w"), indent=1, ensure_ascii=False)
open(out, "a").write("\n")
print("wrote 01_Hardness_Manifest.json:", len(facts), "facts,", len(man["design_delta"]), "design_delta entries")

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
print("seeded ids not in the SQL:", miss or "none")

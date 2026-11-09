#!/usr/bin/env python3
"""Builds Working_Files/01_Hardness_Manifest.json (final) from the draft plus the ids, facts and bindings only the SQL settles.
Every draft id is kept; changes are listed in design_delta. preflight {report, digest} is not written back: the report binds this file."""
import copy, hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
sys.path.insert(0, os.path.join(WF, "solver"))
from base_check import parse_sql  # noqa: E402
import solver  # noqa: E402

draft = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json")))
SEED = json.load(open(os.path.join(HERE, "seed_text.json")))
SEED6 = json.load(open(os.path.join(HERE, "seed_text_rev6.json")))
SEED7 = json.load(open(os.path.join(HERE, "seed_text_rev7.json")))
SEED9 = json.load(open(os.path.join(HERE, "seed_text_rev9.json")))
SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
rows = [x for x in parse_sql(SQL) if x["op"] == "insert"]
man = copy.deepcopy(draft)
man["_note"] = "Final manifest (/create-injection rev9; rev8 passed /injection and /prompt 5, then /hardness scored 2 (one cause): the pre-check run again swept Brian's messages; rev9 removes Brian's Tavern line so Tavern rests on Marcus's DM and Apple on Vincent's mail, and moves Brian's Daily Gift note from ENG-2437 into his DM. rev7 passed /injection and /prompt 5, then /hardness scored 1 because one from:Brian sweep returned the Dec 11 DM lines and settled Tavern, Apple and both popups; rev8 drops the Apple line so Apple rests on Vincent's mail alone. rev6 passed /injection, then /prompt scored Unique Ground Truth and Clarity 2 on the navigation bar tooltips thread, which ended at Brian's 'I'll send another fix'; rev7 adds Vincent's closing reply there. rev5 passed /injection, /prompt 5 and /hardness 4, then two baseline batches failed the spread and pattern gates; rev1 and rev2 passed the platform /injection, rev2 failed /prompt on four forks and NB-1, NB-14). Draft 01_Hardness_Manifest.draft.json plus the ids, facts and bindings only the SQL settles; every change is in design_delta."
sha32 = lambda ch, ts: hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]
SLACK = {f'{r["row"]["channel_id"]}/{r["row"]["ts"]}': r["row"]["id"] for r in rows if r["table"] == "slack.slack_messages"}
MAILMSG = {r["row"]["thread_id"]: r["row"]["id"] for r in rows if r["table"] == "gmail.gmail_messages"}


def map_id(x):
    if isinstance(x, str):
        return SLACK.get(x, MAILMSG.get(x, x))
    return x


def map_list(xs):
    out = []
    for x in xs or []:
        m = map_id(x)
        for y in ([m, x] if m != x and x in MAILMSG else [m]):
            if y not in out:
                out.append(y)
    return out


for f in man["ask_fragments"]:
    f["seeded_ids"] = map_list(f.get("seeded_ids"))
    f["delegated_by_record"] = map_id(f.get("delegated_by_record")) if f.get("delegated_by_record") not in {a["locator"] for a in man["anchors"]} else f.get("delegated_by_record")
    if f["service"] == "gmail":
        f["locator"] = map_id(f["locator"])
for a in man["authorities"]:
    a["seeded_ids"] = map_list(a.get("seeded_ids"))
    a["decoy_seeded_ids"] = map_list(a.get("decoy_seeded_ids"))
for t in man["traps"]:
    t["seeded_ids"] = map_list(t.get("seeded_ids"))
    for v in t.get("version_records") or []:
        if v.get("seeded"):
            v["id"] = map_id(v.get("id"))
    if t.get("version_records"):
        t["version_records"] = sorted(t["version_records"], key=lambda v: v["at"])
# rev6: second carriers for three corrections, placed by measured baseline exposure (run_forensics/rev5/baseline/exposure.py)
_s6 = lambda n: map_id(SEED6[n]["id"])
REV6 = {"T_INLINE_TD": ([_s6("brian_popups")], ["slack"], "; Brian names the same popup in his DM with Owen on Dec 11", "; Brian's DM line reads only from DM history past early December"),
        "T_INLINE_AXE": ([_s6("brian_popups")], ["slack"], "; Brian names the same popup in his DM with Owen on Dec 11", "; Brian's DM line reads only from DM history past early December")}
for t in man["traps"]:
    if t["id"] in REV6:
        ids, svcs, res, disc = REV6[t["id"]]
        t["seeded_ids"] += [i for i in ids if i not in t["seeded_ids"]]
        t["services"] += [x for x in svcs if x not in t["services"]]
        t["resolver"] += res
        if t.get("discovery_order"):
            t["discovery_order"] += disc
# rev9: Brian's Daily Gift note left ENG-2437 for his DM with Owen (D07E9PSQB6W)
_g9 = map_id(SEED9["brian_gift"]["id"])
for f in man["ask_fragments"]:
    if "comment_3e81bf306c58746580a9cfa0ca12bd60" in f["seeded_ids"]:
        f.update(service="slack", container="D07E9PSQB6W", locator=SEED9["brian_gift"]["id"], seeded_ids=[_g9])
for s in man["cohort"].get("evidence_surfaces", []):
    s["seeded_ids"] = [x for x in s.get("seeded_ids") or [] if x != "comment_3e81bf306c58746580a9cfa0ca12bd60"]
for c in man["chains"]:
    for h in c["hops"]:
        h["record"] = map_id(h["record"])
for s in man["cohort"].get("evidence_surfaces", []):
    s["seeded_ids"] = map_list(s.get("seeded_ids"))

CTRL = {r: v["controls"] for r, v in solver.RULES.items()}
for p in man["mechanism_portfolio"]:
    p["controls"] = CTRL[p["id"]]
    if p["id"] == "FOLLOW":
        p["over_application"] = None
man["channels"] = [{"id": k, "kind": v["kind"], "rule": v["rule"], "degrade": v["degrade"], "latent": v["latent"], "family": v["family"], "source": v["source"], "members": v["members"], "description": v["description"]}
                   for k, v in solver.CHANNELS.items()]

S = lambda n: map_id(SEED[n]["id"])
MIR = {r["row"]["attachments_json"]: r["row"]["id"] for r in rows if r["table"] == "slack.slack_messages" and r["row"].get("attachments_json") not in (None, "[]")}
mirror_of = lambda text: [i for a, i in MIR.items() if text[:40] in a]
RC1, RC2 = SEED["inline_td"], SEED["inline_axe"]
mail_rows = [r["row"]["id"] for r in rows if r["table"] == "gmail.gmail_messages" and r["row"]["subject"] == "sign in lines on my list"]
man["facts"] = [
    {"key": "title prefix", "value": "[2231]", "kind": "status", "home_ids": [S("amend")]},
    {"key": "Tile Dozer held piece", "value": "how-to-play popup", "kind": "status", "home_ids": [RC1["id"]] + mirror_of(RC1["text"]) + [_s6("brian_popups")]},
    {"key": "Axe Arena held piece", "value": "info popup", "kind": "status", "home_ids": [RC2["id"]] + mirror_of(RC2["text"]) + [_s6("brian_popups")]},
    {"key": "shop icons came back", "value": "the round icons on the River Tile and Memory Tile shops are there again", "kind": "status", "home_ids": [S("brian_reply")]},
    {"key": "Tavern frame went again", "value": "the Tavern buttons lost their frame again", "kind": "status", "home_ids": [S("vincent_note")]},   # rev9: Brian's Tavern line removed
    {"key": "Season Pass reward track", "value": "the reward track still uses the old frames", "kind": "status", "home_ids": [S("season_note")]},
    {"key": "Daily Gift last pass", "value": "the panel never got its last pass", "kind": "status", "home_ids": [map_id(SEED9["brian_gift"]["id"])]},   # rev9: moved to Brian's DM
    {"key": "Apple line tie", "value": "same sync problem as ENG-2073", "kind": "status", "home_ids": mail_rows},   # rev8: Brian's Apple line removed
    {"key": "manual sign-in tie", "value": "same thing as here", "kind": "status", "home_ids": [S("alias_note")]},
    {"key": "build in the note", "value": "every one gets a note naming the current public build", "kind": "status", "home_ids": [S("rule_comment")]},
    {"key": "version number", "value": "0.3.310", "kind": "status", "home_ids": [S("rule_doc")]},
    {"key": "music and acid", "value": "music plays normally on my side", "kind": "status", "home_ids": [S("brian_dm")]},
    {"key": "Robert's two flickers", "value": "both on the play button and coming out of a level", "kind": "status", "home_ids": [S("flick_reply")]},
    {"key": "bottom bar closed", "value": "the bottom bar and the top panel both show", "kind": "status", "home_ids": [S("bar_reply")]},
    {"key": "tooltip gap closed", "value": "the 1 pixel gap is gone", "kind": "status", "home_ids": [map_id(SEED7["tooltip_reply"]["id"])]},   # rev7
]
man["integration_exceptions"] = json.load(open(os.path.join(HERE, "integration_exceptions.json")))
man["solver"] = {"path": "Working_Files/solver/solver.py", "digest": hashlib.sha256(open(os.path.join(WF, "solver", "solver.py"), "rb").read()).hexdigest()}
man["gradable_surface"] = "01_Gradable_Surface.json"
man["design_delta"] = json.load(open(os.path.join(HERE, "design_delta.json")))
json.dump(man, open(os.path.join(WF, "01_Hardness_Manifest.json"), "w"), indent=1, ensure_ascii=False)
print("final manifest", len(man["facts"]), "facts", len(man["design_delta"]), "delta entries")

#!/usr/bin/env python3
"""Final manifest (injection rev1) from the draft + what only the SQL settles. Keeps every draft id or lists the change
in design_delta."""
import hashlib, json
from pathlib import Path

WF = Path(__file__).resolve().parents[1]
m = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())
ids = json.loads((WF / "plan/sql_ids.json").read_text())["ids"]
FRED = "frederick.stone@harmonygames.co"
SHA = {"C07C2866011/1758303600.418207": "4921f321db5d08f936aac24a6a1d2af8",
       "C07C2866011/1759168800.117903": "7fef94264090696760180223fc8265e7",
       "C096HFA5Z8W/1759161600.226431": "3f2d8f04b29a78808033543c740bb669",
       "C096HFA5Z8W/1759184040.552871": "cf10d4f7f88143dc7ab976df27513790"}
OLD_KW, NEW_KW = "68c6b2a4f19e03d7c5a81b2e", ids["TR_KW_CMT"]
NEW_DECKCARD = ids["TR_DECKCARD"]
SHEET_ANG = ids["SHEET_ANGELS"]


def sub(x):
    if isinstance(x, str):
        return SHA.get(x, NEW_KW if x == OLD_KW else x)
    if isinstance(x, list):
        return [sub(y) for y in x]
    if isinstance(x, dict):
        return {k: (sub(v) if k not in ("locator", "record", "container", "base_pointers") else
                    ([NEW_KW if y == OLD_KW else y for y in v] if isinstance(v, list) else
                     (v.replace(OLD_KW, NEW_KW) if isinstance(v, str) else v))) for k, v in x.items()}
    return x


m = sub(m)
m["_note"] = "final manifest (/create-injection rev3); every draft id kept or listed in design_delta"
# exact delegation words as written in the seeded records (case-exact substrings)
Q = {"K8": "pass one of us heard by phone counts once it is written in #bridge-pitch",
     "K9": "the Existing Investor Update card says to do for firms that pass, do that too",
     "K10": "Board Deck card says which numbers the slide takes",
     "K11": "Slide 9 of the draft deck lists the table's columns",
     "K14": "Arthur tracks the tester adds"}
for f in m["ask_fragments"]:
    if f["id"] in Q:
        f["delegation_quote"] = Q[f["id"]]
    for na in f.get("names_authorities", []):
        if na["id"] == "H2":
            na["quote"] = "the Existing Investor Update card says to do for firms that pass"
    if f["id"] == "K10":
        f["container"] = NEW_DECKCARD
        f["locator"] = f"trello:{NEW_DECKCARD}"
        f["seeded_ids"] = [NEW_DECKCARD, "68d81f30a6c94e2b7d05e1f4"]
    if f["id"] == "K9":
        f["seeded_ids"] = [NEW_KW]
for t in m["traps"]:
    if t["id"] == "T3":
        t["version_records"] = [
            {"service": "gmail", "base_pointer": f"{FRED}/1842285743246816270", "seeded": False,
             "at": "2025-09-18T03:27:31Z", "container": f"gmail:{FRED}/1842285743246816270"},
            {"service": "slack", "id": SHA["C096HFA5Z8W/1759184040.552871"], "seeded": True, "at": "2025-09-29T22:14:00Z",
             "container": "slack:C096HFA5Z8W/1757716998.377299"}]
    if t["id"] == "T4":
        t["seeded_ids"] = [SHA["C07C2866011/1758303600.418207"], SHEET_ANG, ids["G_ANTON"]]
        t["version_records"] = [
            {"service": "slack", "id": SHA["C07C2866011/1758303600.418207"], "seeded": True, "at": "2025-09-19T17:40:00Z",
             "container": "slack:C07C2866011/1758303600.418207"},
            {"service": "gsheets", "id": SHEET_ANG, "seeded": True, "at": "2025-09-20T03:15:00Z", "container": f"file:{SHEET_ANG}"},
            {"service": "gmail", "id": ids["G_ANTON"], "seeded": True, "at": "2025-09-24T16:10:00Z",
             "container": f"gmail:{ids['G_ANTON']}"}]
        t["services"] = ["slack", "gsheets", "gmail"]
    if t["id"] == "T1":
        t["seeded_ids"] = [SHA["C07C2866011/1758303600.418207"], SHEET_ANG, ids["G_DS_PAUL"], ids["G_DS_ANTON"]]
        t["resolver"] = ("no DocuSign Completed notice for Paul's SAFE (Anton's arrived Sep 26) and Leonard's Sep 29 nudge says it "
                         "is still with Paul; the template counts only signed SAFEs")
    if t["id"] == "T8":
        t["seeded_ids"] = [NEW_KW]
    for v in t.get("version_records", []):
        if v.get("id") in SHA:
            v["id"] = SHA[v["id"]]
for c in m["chains"]:
    for hp in c["hops"]:
        hp["record"] = SHA.get(hp["record"], NEW_KW if hp["record"] == OLD_KW else hp["record"])
m["authorities"][1]["seeded_ids"] = [NEW_KW]
# channels as the solver declares them (kinds from the oracle_kit vocabulary)
m["channels"] = [
    {"id": "CH-FILT-HOMA", "kind": "scale", "rule": "FILT", "degrade": "filt_miss", "members": ["Homa"], "latent": "member",
     "family": "exact_predicate"},
    {"id": "CH-FILT-BRIGHT", "kind": "scale", "rule": "FILT", "degrade": "filt_miss", "members": ["Brightwater Games Fund"],
     "latent": "member", "family": "exact_predicate"}]
m["hazard_acknowledgements"] = []
m["integration_exceptions"] = []
m["facts"] = [
    {"key": "Paul Heydon", "value": "50000", "kind": "amount", "home_ids": [SHA["C07C2866011/1758303600.418207"], SHEET_ANG],
     "must_appear_in": [SHA["C07C2866011/1758303600.418207"]]},
    {"key": "Anton Bernstein", "value": "25000", "kind": "amount", "home_ids": [ids["G_ANTON"]],
     "version_records": [SHA["C07C2866011/1758303600.418207"], SHEET_ANG]},
    {"key": "keep-warm rule", "value": "Keep warm", "kind": "name", "must_appear_in": [NEW_KW]},
]
MSG = ids["MSGIDS"]
HUB_MSG = f"{FRED}/{MSG['g_hub']}"
ANTON_MSGS = [f"{FRED}/{MSG['g_anton']}", f"leonard.hayes@harmonygames.co/{MSG['g_anton']}"]
m["anchors"][0]["record"] = m["anchors"][0]["locator"] = HUB_MSG
for f in m["ask_fragments"]:
    if f["delegated_by_record"] == ids["G_HUB"]:
        f["delegated_by_record"] = HUB_MSG
    if f["id"] in ("K1", "K2", "K3"):
        f["seeded_ids"] = [HUB_MSG, ids["G_HUB"]]
        f["locator"] = HUB_MSG
    if f["id"] == "K9":
        f["names_authorities"] = [{"id": "H2", "quote": "a Keep warm checklist on this card"}]
for t in m["traps"]:
    for v in t.get("version_records", []):
        if v.get("base_pointer") == f"{FRED}/1842285743246816270":
            v["base_pointer"] = "gmail:threads/frederick@harmonygames.co_1842285743246816270.json /messages/1"
        if v.get("id") == ids["G_ANTON"]:
            v["id"] = ANTON_MSGS[0]
    if t["id"] == "T10":
        t["version_records"] = [
            {"service": "gsheets", "base_pointer": "gsheets:data.json /sheets_spreadsheets/96", "seeded": False,
             "at": "2025-09-15T19:27:01Z", "container": "file:f_48247af79428823c3cac92"},
            {"service": "gmail", "base_pointer": "gmail:threads/frederick@harmonygames.co_1842283406259093714.json /messages/0",
             "seeded": False, "at": "2025-09-22T17:40:07Z", "container": f"gmail:{FRED}/1842283406259093714"}]
OLD_DENTSU = f"{FRED}/1844347876147200047"
EVT_HIRO = ids["EVT_HIRO"][FRED]
for t in m["traps"]:
    t["seeded_ids"] = [ids["G_DENTSU"] if x == OLD_DENTSU else x for x in t.get("seeded_ids", [])]
    if t["id"] == "T5":
        t["seeded_ids"] = list(dict.fromkeys(t["seeded_ids"] + [EVT_HIRO]))
        t["resolver"] = ("Edith Vane's Sep 26 pass (no firm name; cc the Investment Director from the Sep 3 Hiro thread) after the "
                         "Sep 23 Hiro pitch call on the calendar; Contacts: Partner, Hiro Capital")
for c in m["chains"]:
    for hp in c["hops"]:
        if hp["record"] == OLD_DENTSU:
            hp["record"] = ids["G_DENTSU"]
    if c["id"] == "C3" and not any(h["record"] == EVT_HIRO for h in c["hops"]):
        c["hops"].insert(1, {"service": "gcal", "record": EVT_HIRO,
                             "finding": "Tue Sep 23 call 'PERSON_5487_NAME and Leonard Hayes' (Hiro partner + Edith)"})
for w in m.get("writes", []):
    w["depends_on"] = [ids["G_DENTSU"] if x == OLD_DENTSU else x for x in w["depends_on"]]
for fct in m["facts"]:
    if fct["key"] == "Anton Bernstein":
        fct["home_ids"] = ANTON_MSGS
m["design_delta"] = [
    {"id": "K9/H2/T8 trello comment", "change": f"comment id {OLD_KW} -> {NEW_KW}",
     "reason": "Trello ids carry the action's Unix seconds; the comment is dated 2025-09-14T04:20Z (Leonard's evening hours)"},
    {"id": "K10", "change": f"container 67f446b4b0817af30d2d63f6 -> new card {NEW_DECKCARD} 'Board Deck - Oct 14'",
     "reason": "the base Board Deck card is the April deck in Done; the Oct 14 note belongs on a new card"},
    {"id": "T1", "change": "the Paul record frederick.stone@harmonygames.co/1844610859008000037 is Leonard's Sep 29 nudge mail; Paul's state is shown by the absence of a DocuSign Completed notice beside Anton's",
     "reason": "the base DocuSign notices (SVC_1302) have Completed/request/viewed shapes but no reminder shape"},
    {"id": "T4", "change": f"added Leonard's 'Bridge angels' sheet {SHEET_ANG} as the middle version (3 versions)",
     "reason": "stale tracker in a third service; supplies the >= 3-version supersession"},
    {"id": "T3", "change": "version_records reduced to the SciPlay thread and Robert's reply",
     "reason": "both earlier entries were the same base thread (one timestamp per record)"},
    {"id": "ZOM-567", "change": "created 2025-09-30T17:10Z, comments 17:25Z and 18:40Z (design: Sep 24 / Sep 29)",
     "reason": "Linear numbers follow creation order: ZOM-566 was created 2025-09-30T16:26Z"},
    {"id": "channels", "change": "CH-SLIP dropped; FILT channels use kind 'scale'",
     "reason": "oracle_kit channel kinds; control rows are slips, not a complexity channel"},
    {"id": "hazard_acknowledgements", "change": "Q01 entry removed",
     "reason": "the SQL updates the root's reply counters (companion); Q hazards need no acknowledgement"},
    {"id": "companions", "change": "invitation mails for the Brightwater call (Frederick, Robert, Arthur) and the Oct 6 review (Frederick); Ilse's reply in the follow-up thread; deck-card Sections checklist",
     "reason": "INT-11 base rate; Brightwater's firm name in a reply signature; deck coordination record"},
]
m["design_delta"] += [
    {"id": "T5 / R6 (rev2)", "change": f"seeded the Hiro pitch call {EVT_HIRO} (Tue 2025-09-23 16:00-16:45Z, Leonard, the founders, "
     "PERSON_5487 and Edith Vane) on four calendars with invitation mails; Edith's pass now thanks Leonard for 'the session on Tuesday'",
     "reason": "platform /injection rev1 advisory 2: the Sep 3 Hiro thread is a re-intro email, not a call, so the base held no Hiro "
               "pitch call this round; the keep-warm rule (passes after a call or meeting) and Edith's wording need one"},
    {"id": "T2 Dentsu thread (rev2)", "change": f"thread {OLD_DENTSU} -> {ids['G_DENTSU']}: Ryo-san's Sep 26 03:10Z mail with the "
     "three tester addresses starts the thread; Leonard's 'invites are out' mail is its reply",
     "reason": "platform /injection rev1 advisory 4: Leonard's 'thank you for sending your emails' and Arthur's 'came in Fri' now "
               "point at a recorded message"},
    {"id": "H1 template population rule (rev2)", "change": "'one row per firm … a firm that shows up twice is one row' -> 'one row per name on the 2025 game investor list, angels included … a repeated name is still one row'",
     "reason": "known data issue SC-33 (watch): the list repeats Acterra, Progression Fund and BITKRAFT Ventures; the rule now settles the count and names the five angels' rows explicitly (the money rows sit on two of them)"},
    {"id": "Brightwater follow-up (rev2)", "change": "Leonard says he will send the deck and engine doc separately; Ilse will brief the partners",
     "reason": "platform /injection rev1 advisory 3: the mail claimed attachments that carry no attachment metadata"},
]
m["design_delta"] += [
    {"id": "K11 (rev3)", "change": "the register's columns moved from slide 9's speaker notes into its visible text; the Board Deck - Oct 14 card comment now reads 'Slide 9 of the draft deck lists the table's columns'",
     "reason": "platform /injection rev2 advisory 1: speaker-notes rendering is unverified (Ask_Carriers §5; no baseline trajectory shows notes), so the pointer could dangle"},
    {"id": "ZOM-567 Dentsu comment (rev3)", "change": "'came in Fri' -> 'came in Thursday night'",
     "reason": "platform /injection rev2 advisory 2: Ryo-san's mail is 2025-09-26T03:10Z = Thu Sep 25 20:10 PT"},
    {"id": "T6 Brightwater call (rev3)", "change": "2025-09-25 16:00-16:45Z -> 15:30-16:15Z (invitations 8:30-9:15am PDT)",
     "reason": "platform /injection rev2 advisory 3: clear of Leonard's base 1:1 evt_c6d85261f1e1dc58ddf1ad (16:30Z)"},
    {"id": "Trello board (rev3)", "change": "UPDATE trello_boards 640643a3fd8f3ca308d9318e dateLastActivity -> 2025-09-27T17:30:24Z",
     "reason": "platform /injection rev2 advisory 4: board activity follows the seeded card actions"},
]
sp = WF / "solver/solver.py"
m["solver"] = {"path": "Working_Files/solver/solver.py", "digest": hashlib.sha256(sp.read_bytes()).hexdigest()}
m["gradable_surface"] = "01_Gradable_Surface.json"
(WF / "01_Hardness_Manifest.json").write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n")
print("final manifest written;", len(m["design_delta"]), "design_delta entries")

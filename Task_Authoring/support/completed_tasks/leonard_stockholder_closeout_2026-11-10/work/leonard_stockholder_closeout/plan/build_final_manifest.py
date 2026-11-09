#!/usr/bin/env python3
"""Build Working_Files/01_Hardness_Manifest.json (final, /create-injection) from the draft and the SQL ids.

Every draft id is kept; changes are listed in design_delta. Adds what only the SQL settles: Slack row ids, Gmail message rows
for seeded records, the fact sheet with home_ids, integration exceptions, solver {path, digest} and gradable_surface.
preflight {report, digest} is not written back: the report binds this file by sha256, so a digest here would make it stale;
it is cited in the dossier."""
import copy, hashlib, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
draft = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json")))
S = json.load(open(os.path.join(HERE, "sql_ids.json")))
SQL_TEXT = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
man = copy.deepcopy(draft)
man["_note"] = ("Final manifest (/create-injection rev2). Draft 01_Hardness_Manifest.draft.json plus the ids, facts and bindings only the SQL "
                "settles; every change is in design_delta.")
delta = []


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


SLACK = dict(S["slack"])                                  # 'C/ts' -> 32-hex row id (seeded messages only)
GM = S["gmail"]
THREAD_TO_MSG = {GM["kpmg"]["thread"]: GM["kpmg"]["message"], GM["sunset"]["thread"]: GM["sunset"]["message"]}


def map_id(x):
    if not isinstance(x, str):
        return x
    return SLACK.get(x) or THREAD_TO_MSG.get(x) or x


def map_list(xs):
    out = []
    for x in xs or []:
        for y in ([map_id(x), x] if x in THREAD_TO_MSG else [map_id(x)]):
            if y not in out:
                out.append(y)
    return out


# hardness_gate reads a thread's first `files` match, which is an attachment on these threads, so they are cited by file and pointer
MB = "leonard.hayes@harmonygames.co"
FILE_POINTERS = {
    f"{MB}/<BY3PR13MB48333BC5C19C3EC4EC8B3F28A6F2A@BY3PR13MB4833.namprd13.prod.outlook.com>": "gmail:threads/leonard@harmonygames.co_1775602109531090463.json /messages/4",
    f"{MB}/<BL0PR1501MB20995F0276101A153B2CC9DC99F7A@BL0PR1501MB2099.namprd15.prod.outlook.com>": "gmail:threads/leonard@harmonygames.co_1775602109531090463.json /messages/2",
    f"{MB}/<CAPBs_a46H9SCR=PBn1EP4RvCL+HO3XqOma4mTNu0WdnWv17ZuA@mail.gmail.com>": "gmail:threads/leonard@harmonygames.co_1777052222643175480.json /messages/7",
    f"{MB}/<LV3PR19MB8524A7F34357829DDCA90153CA302@LV3PR19MB8524.namprd19.prod.outlook.com>": "gmail:threads/leonard@harmonygames.co_1817557789846606177.json /messages/6",
}
for a in man["anchors"]:
    a["locator"] = map_id(a["locator"])
for f in man["ask_fragments"]:
    f["seeded_ids"] = map_list(f.get("seeded_ids"))
    f["delegated_by_record"] = map_id(f.get("delegated_by_record"))
    if f["service"] == "gmail":
        f["locator"] = map_id(f["locator"])
for a in man["authorities"]:
    a["seeded_ids"] = map_list(a.get("seeded_ids"))
    a["decoy_seeded_ids"] = map_list(a.get("decoy_seeded_ids"))
    a["decoy_base_pointers"] = [FILE_POINTERS.get(x, x) for x in a.get("decoy_base_pointers") or []]
for t in man["traps"]:
    t["seeded_ids"] = map_list(t.get("seeded_ids"))
    for v in t.get("version_records") or []:
        if v.get("seeded"):
            v["id"] = map_id(v.get("id"))
        elif v.get("base_pointer") in FILE_POINTERS:
            v["base_pointer"] = FILE_POINTERS[v["base_pointer"]]
    if t.get("version_records"):
        t["version_records"] = sorted(t["version_records"], key=lambda v: v["at"])
for c in man["chains"]:
    for h in c["hops"]:
        h["record"] = map_id(h["record"])
delta.append({"id": "record ids (all elements)", "change": "Slack 'channel/ts' pointers to seeded messages -> their 32-hex row ids; Gmail thread pointers -> the message row "
              "that carries the text (thread ids kept alongside in seeded_ids)", "reason": "the gate reads text and timestamps from SQL rows; a Gmail thread row holds only a snippet"})
delta += json.load(open(os.path.join(HERE, "design_delta.json")))

L = S["linear"]
facts = [
 {"key": "as-of date", "value": "December 31, 2025", "kind": "date", "home_ids": [GM["kpmg"]["message"], GM["kpmg_ack"]["message"]]},
 {"key": "told rule", "value": "Told means a written message about the closing, sent to them directly and delivered, from one of the three of us (a post in a channel doesn't count); for a fund, its partner.", "kind": "status",
  "home_ids": ["f_a37b403d5200d4f0a31d31"]},
 {"key": "line rule", "value": "If a line's last day has passed, it holds nothing.", "kind": "status", "home_ids": ["f_a37b403d5200d4f0a31d31"]},
 {"key": "owed rule", "value": "the closing if they have not been told, their last day if they have one", "kind": "status", "home_ids": ["f_a37b403d5200d4f0a31d31"]},
 {"key": "family rule", "value": "covers the rest of the family's lines", "kind": "status", "home_ids": [SLACK["C0ADGSZKR3R/1770949310.220519"]]},
 {"key": "state rule", "value": "Canceled where the line holds nothing", "kind": "status", "home_ids": ["ec2ea957-fc8e-4958-b809-0fb735b1e916"]},
 {"key": "closing told", "value": "we're closing the company", "kind": "status", "home_ids": [GM["robert_leo"]["message"], GM["robert_rob"]["message"]]},
 {"key": "board after Feb 12", "value": "That leaves Leonard and me on the board", "kind": "status", "home_ids": [GM["board_leo"]["message"], GM["board_rob"]["message"], GM["board_art"]["message"]]},
 {"key": "Owen's letter not delivered", "value": "Your message wasn't delivered to PERSON_3140_EMAIL", "kind": "status", "home_ids": [GM["bounce"]["message"]]},
 {"key": "ES-3 last day", "value": "Last day to exercise Feb. 20, 2026", "kind": "date", "home_ids": [GM["ext"]["message"]]},
 {"key": "Collins told", "value": "Harmony is shutting down", "kind": "status", "home_ids": [GM["akin"]["message"]]},
]
man["facts"] = facts
man["integration_exceptions"] = [
 {"integration": "INT-11", "record_id": "evt_6f1a2c9e4b7d3a58c0e1d2", "reason": "no_notify: a solo hold on Leonard's own calendar, no guests, so no invitation mail"},
 {"integration": "INT-13", "record_id": "f_a37b403d5200d4f0a31d31", "reason": "nothing is shared at seed time, and the Drive-app DM mirror ends 2026-01-19"},
]
man["solver"] = {"path": "Working_Files/solver/solver.py", "digest": sha(os.path.join(WF, "solver", "solver.py"))}
man["gradable_surface"] = "01_Gradable_Surface.json"
man["design_delta"] = delta
json.dump(man, open(os.path.join(WF, "01_Hardness_Manifest.json"), "w"), indent=1, ensure_ascii=False)
open(os.path.join(WF, "01_Hardness_Manifest.json"), "a").write("\n")

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
print("wrote 01_Hardness_Manifest.json:", len(facts), "facts,", len(delta), "design_delta entries; seeded ids not in the SQL:", miss or "none")

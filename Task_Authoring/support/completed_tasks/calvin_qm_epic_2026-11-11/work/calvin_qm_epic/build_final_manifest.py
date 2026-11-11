#!/usr/bin/env python3
"""Build Working_Files/01_Hardness_Manifest.json (final, /create-injection) from the certified draft + the SQL ids.
Every draft id is kept; changes are listed in design_delta. Adds what only the SQL settles: row ids, the facts sheet with
home_ids, solver {path, digest} and gradable_surface. Re-run after any SQL or solver change. No preflight {report, digest}
is written here: preflight_report.py binds this manifest by sha256, so a digest written back would make it stale."""
import copy, hashlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402
draft = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json")))
ids = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
SEED = json.load(open(os.path.join(HERE, "seed_text.json")))
ID = {k: v["id"] for k, v in SEED.items()}
man = copy.deepcopy(draft)
man["_note"] = "Final manifest (/create-injection rev2). The scenario-certified draft plus the ids, facts and bindings only the SQL settles; every change is in design_delta."
SQL_TEXT = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
SLACK_ID = {}
for x in parse_sql(SQL_TEXT):
    if x.get("op") == "insert" and x["table"] == "slack.slack_messages":
        r = x["row"]
        SLACK_ID[f"{r['channel_id']}/{r['ts']}"] = r["id"]
sl = lambda x: SLACK_ID.get(x, x) if isinstance(x, str) else x       # noqa: E731
sll = lambda xs: [sl(x) for x in xs or []]                            # noqa: E731
for a in man["anchors"]:
    a["locator"] = sl(a["locator"])
for f in man["ask_fragments"]:
    f["seeded_ids"] = sll(f.get("seeded_ids"))
    f["delegated_by_record"] = sl(f.get("delegated_by_record"))
for a in man["authorities"]:
    a["seeded_ids"], a["decoy_seeded_ids"] = sll(a.get("seeded_ids")), sll(a.get("decoy_seeded_ids"))
for t in man["traps"]:
    t["seeded_ids"] = sll(t.get("seeded_ids"))
    for v in t.get("version_records") or []:
        if v.get("seeded") and v.get("id") in SLACK_ID:
            v["id"] = SLACK_ID[v["id"]]
for c in man["chains"]:
    for hop in c["hops"]:
        hop["record"] = sl(hop["record"])
for s_ in man["cohort"].get("evidence_surfaces", []):
    s_["seeded_ids"] = sll(s_.get("seeded_ids"))
man["cohort"]["definition_source"] = sll(man["cohort"].get("definition_source"))
m, gh, tr = ids["slack_mid"], ids["gh"], ids["trello"]
delta = [{"id": "record ids (all elements)", "change": "Slack channel/ts pointers to seeded messages became the messages' 32-hex row ids",
          "reason": "the gate reads text and timestamps from SQL rows, and a Slack row is keyed by its id"},
         {"id": "companion records", "change": "added at implementation: a Hello! line before Brian's DM, Marcus's second line, two lines from Vincent to Calvin about his pass, a COMMENTED review row and a GitHub notification mail for each of Arthur's two inline comments, the #zombie-prs copies of the three GitHub comments, invitation mail copies in four other attendees' mailboxes, the card's create, first description and rename actions, and one or two notes on each of Vincent's 18 tickets",
          "reason": "each follows a base habit read at this stage: Brian and Marcus write in short bursts; Calvin's mailbox already holds GitHub's mails for #472 and #475, including Arthur's approvals with no comment in them, so his inline comments are separate reviews with their own mails; the GitHub app copies every match3d comment to #zombie-prs; the tickets' comment surface is the per-ticket read the cohort declares"}]
facts = [
    {"key": "which builds count for a pass", "value": "a QA pass only counts on a build of the main branch", "kind": "status", "home_ids": [ID["rule_doc"]]},
    {"key": "review on #472", "value": "That one isn't in this diff", "kind": "status", "home_ids": [ID["inline"], gh["inline"]["mail"], m["mirror_inline"]]},
    {"key": "review on #475", "value": "Don't see the pack sound stop anywhere in here", "kind": "status", "home_ids": [ID["inline2"], gh["inline2"]["mail"], m["mirror_inline2"]]},
    {"key": "pass popup is back", "value": "the pass popup came up on top of the gift again", "kind": "status", "home_ids": [m["reopen"]]},
    {"key": "home intro is back", "value": "the home intro animation played again every single time", "kind": "status", "home_ids": [m["back"]]},
    {"key": "Oliver's merged fixes", "value": "this also has the fix for the pass start popup coming back after every level and for the pass bar filling before the tokens land", "kind": "status", "home_ids": [ID["else_pr"], m["mirror_else"]]},
    {"key": "Marcus's report", "value": "the pass icon glow stays on after i claimed everything", "kind": "status", "home_ids": [m["filt_dm"]]},
    {"key": "review areas", "value": "Collect & Win, Level-end rewards", "kind": "status", "home_ids": [ID["rev_card"], ID["rev_card_update"]]},
    {"key": "tie to the gift ticket", "value": "Saw this one myself in my home screen pass on 1727", "kind": "status", "home_ids": [ID["alias_gift"]]},
    {"key": "tie to the freezer ticket", "value": "Still there on Android 1984 in my home screen pass", "kind": "status", "home_ids": [ID["alias_streak"]]},
]
man["facts"] = facts
man["solver"] = {"path": "Working_Files/solver/solver.py", "digest": hashlib.sha256(open(os.path.join(WF, "solver", "solver.py"), "rb").read()).hexdigest()}
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
# load-bearing scoped ids for persona_view check-sql (scoped services only)
lb = [m[k] for k in ("gate_old", "hub", "filt_dm", "reopen", "back", "mirror_else", "mirror_inline", "mirror_inline2")]
lb += [ID[k] for k in ("sheet", "legend", "rule_doc", "dd_doc", "deck", "folder", "event", "invite_v1", "invite_v2")]
lb += [gh["inline"]["mail"], gh["inline2"]["mail"]]
open(os.path.join(HERE, "load_bearing_scoped.txt"), "w").write("\n".join(lb) + "\n")
print("facts", len(facts), "delta", len(delta), "seeded ids not in the SQL:", miss or "none")

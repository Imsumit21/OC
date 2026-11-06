#!/usr/bin/env python3
"""Build Working_Files/01_Hardness_Manifest.json (final, /create-injection) from the certified draft + the SQL ids.

Every draft id is kept; changes are listed in design_delta. Adds what only the SQL settles: Slack 32-hex row ids and
Gmail message rows for seeded records, Robert's own calendar copy, the facts sheet with home_ids, the integration
exceptions, solver {path, digest} and gradable_surface. preflight {report, digest} is not written back: the preflight
report binds this file by sha256, so a digest written here would make the report stale (it is cited in the dossier).
"""
import copy, hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402

draft = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json")))
S = json.load(open(os.path.join(HERE, "sql_ids.json")))
I = json.load(open(os.path.join(HERE, "ids.json")))
IDS, T = I["IDS"], I["T"]
SQL_TEXT = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
ROB, LEO, ART = "robert@harmonygames.co", "leonard.hayes@harmonygames.co", "arthur.blake@harmonygames.co"
man = copy.deepcopy(draft)
man["_note"] = ("Final manifest (/create-injection rev2; rev1 passed the platform /injection review, attempt 6adfee3b47f7621feba5b96c). Draft 01_Hardness_Manifest.draft.json (scenario-certified design-1) plus "
                "the ids, facts and bindings only the SQL settles; every change is in design_delta.")
delta = []


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


# ---------------------------------------------------------------- id maps
SLACK = {v["locator"]: v["id"] for v in S["slack"].values()}            # 'C/ts' -> 32-hex row id (seeded messages only)
GM_THREAD_TO_MSG = {}                                                    # Robert's thread id -> Robert's message row
for key, boxes in S["gmail"].items():
    for box, ids in boxes.items():
        GM_THREAD_TO_MSG[ids["thread"]] = ids["message"]


def map_id(x):
    if not isinstance(x, str):
        return x
    if x in SLACK:
        return SLACK[x]
    if x in GM_THREAD_TO_MSG:
        return GM_THREAD_TO_MSG[x]
    return x


def map_list(xs, keep_thread=True):
    out = []
    for x in xs or []:
        m = map_id(x)
        for y in ([m, x] if keep_thread and m != x and x in GM_THREAD_TO_MSG else [m]):
            if y not in out:
                out.append(y)
    return out


ROB_EVT = S["gcal"][ROB]
ANCHOR_LOCS = {a["locator"] for a in man["anchors"]}
for f in man["ask_fragments"]:
    f["seeded_ids"] = map_list(f.get("seeded_ids"))
    if f.get("delegated_by_record") not in ANCHOR_LOCS:                  # a delegation by the anchor keeps the anchor's own locator
        f["delegated_by_record"] = map_id(f.get("delegated_by_record"))
    if f["service"] == "gmail":
        f["locator"] = map_id(f["locator"])
    if f["service"] == "gcal":
        old = f["locator"]
        f["container"] = f["locator"] = ROB_EVT
        f["seeded_ids"] = [ROB_EVT] + [x for x in f["seeded_ids"] if x != ROB_EVT]
        delta.append({"id": f"{f['id']} locator", "change": f"{old} (Leonard's copy) -> {ROB_EVT} (Robert's own calendar copy); "
                      "Leonard's and Arthur's copies share ical_uid", "reason": "reach is proven on the persona's own copy"})
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
for c in man["chains"]:
    for h in c["hops"]:
        h["record"] = map_id(h["record"])
for s_ in man["cohort"].get("evidence_surfaces", []):
    s_["seeded_ids"] = map_list(s_.get("seeded_ids"))
delta.append({"id": "record ids (all elements)",
              "change": "Slack 'channel/ts' pointers to seeded messages -> their 32-hex row ids; Gmail thread pointers in Robert's "
                        "mailbox -> the message row that carries the text (thread ids kept alongside in seeded_ids)",
              "reason": "the gate reads text and timestamps from SQL rows: a Slack message row is keyed by its id, a Gmail thread "
                        "row holds only a snippet"})

# ---------------------------------------------------------------- record-level changes made while writing the SQL
delta += [
    {"id": "linear project links", "change": "no linear_project_teams / linear_project_members rows (planned: team link and three members)",
     "reason": "not among the 64 writable tables (Injection Schema Guideline 2026-10-22, sql_lint); the project keeps team_id and lead_id"},
    {"id": "#1917 branches", "change": "merged into Blake/boombitWithEcon (head Blake/supportEmail; the branches table row is "
     "arthur.blake/supportEmail, the base's NB-13 form split), not develop; Jenkins #218 builds 'Blake/boombitWithEcon'; a merge commit row "
     "follows the base merge shape (commits/4580)", "reason": "base DD submissions build from that branch (#builds 2026-01 /1236-/1238; GitHub "
     "branches/981); #1916 also targeted a feature branch, not develop"},
    {"id": "store notice wording", "change": "subject 'We noticed an issue with your submission.' and Apple's review template (App Name, "
     "Submission ID, the guideline item)", "reason": "the base INT-08 rejection family in Robert's mailbox (threads/00013785.json, "
     "00014520.json)"},
    {"id": "deck line 2", "change": "'Keep the video campaign ...' -> 'Run the VO campaign at $100/day (~$3k a month) through May', dated Feb 8 03:00Z; playables line -> 'No playables beyond the one in production until D1 is over 35%'",
     "reason": "the deck first predated the campaign (C09UHHN6PFZ/1770404397.819789, Feb 6); 'VO' is event/value optimization, not video "
     "(C09UHHN6PFZ/1770404397.819789, C07C2866011/1770438169.228649); Robert pushed one playable that week (C07C2866011/1770264360.331789)"},
    {"id": "project description", "change": "'Todo when ...' -> 'move it to Todo if ...' (same states and rule)",
     "reason": "eval lint grader_language (state_rules) on the 'Todo when' phrasing"},
    {"id": "blind fork sweep (rev1)", "change": "settled by dated records: campaign capped at $3,000 a month and moving to the LLC from March; the split "
     "mail counts what a founder already pays inside 'what the LLC costs'; GitHub's org stays HG's while Arthur pays the bill; the build boxes go "
     "with Sunset's sale and CF's Jenkins job moves to Arthur's machine; AppsFlyer free tier from March; CF on Unity Personal; DD owner Leonard "
     "and no BoomBit status claim; ground rules: hosting 'bills now', a game brings its accounts and player support, monthly bills only, the LLC "
     "is for the three of us; CF stacks and DD prod are on HG's AWS bill till March", "reason": "a blind fork sweep of Robert-visible records "
     "found readings no record settled (plan/sweep_dispositions.md); the truth is unchanged"},
    {"id": "blind coherence sweep (rev1)", "change": "VO (event-optimization) campaign, not 'video'; Leonard's status names only the Meta "
     "campaigns, says Meta barely bills the VO one while it learns and that it runs at $100/day capped at $3,000 a month from March; deck dated "
     "Feb 8 with the playables line reworded; project (23:24Z) and issues before the card (23:42Z) before the ground rules (23:46Z); notes doc "
     "Feb 9 23:55Z; GitHub back to the $48 plan after dropping the extra seat (Feb 3 receipt $52 + Copilot $38), bills move 'from the next "
     "bill'; CF's own account (auth, nakama, backend) no longer calls ZM's phoenix; ZM's account 'well over $1k a month'; Slack note 'three paid "
     "members'; the Metabase note drops 'needs a payer'; the hub drops its opening 'ok,'; App Review mail copied to all three founders; "
     "Arthur's invitation in EST with his display name; PR refs Blake/… with a merge commit row", "reason": "a blind coherence sweep of every "
     "seeded claim against the full base (plan/sweep_dispositions.md); each finding re-checked through hg.py"},
    {"id": "rev2: notes doc title (platform /injection rev1 advisory A-1)", "change": "the notes doc is 'LLC notes (Monday)' with its text "
     "as the body (it was one line, so the whole note became the title and the body run was empty)", "reason": "the platform /injection review of "
     "rev1 (PASS, run_forensics/rev1/0_injection_PASS_r1.md) flagged the zero-length style run; the 155-character title was unnatural"},
    {"id": "rev2: coherence re-check", "change": "ZM's account note drops 'well over $1k a month' (it bills every month); Arthur's and "
     "Leonard's App Review copies greet them by name with their base labels; the Metabase note reads 'more or less'; layer.ai 'character source "
     "art'; 'the build boxes at my place are HG's'; project start_date 2026-02-12", "reason": "the coherence reviewer's re-check of the rev2 "
     "wording (HG's whole AWS line is $1,485 in Jan and Feb 2026, snowflake FINANCE.EXPENSES.MONTHLY_BURN; plan/sweep_dispositions.md)"},
    {"id": "rev2: second blind fork sweep", "change": "the App Review item describes the email-draft support option doing nothing without a "
     "mail account (only the #218 support-email build has it); Arthur moves 'our jenkins jobs' (CF and DD); ENG-2445 names the auth and backend "
     "stacks only; Arthur's mail counts GitHub as his 'like the other two' and puts CF's BigQuery/Firebase on the free tier once the data's out; "
     "Leonard's status adds 'so count it in what the LLC costs'", "reason": "a second blind fork sweep of the rev2 records (fresh agent, no answer "
     "key) reproduced the plan and totals and listed the readings still open; truth unchanged (plan/sweep_dispositions.md)"},
    {"id": "rev3: platform /prompt forks F1-F3", "change": "the project description's scope reads 'One issue per thing the LLC might take "
     "from HG or pay for' (the VO campaign the LLC pays from March is in scope and gets an issue); Leonard's AppsFlyer note ends 'I'll set CF up "
     "on it' (he moves it); Leonard's Google Analytics note adds 'nothing for the LLC to take or pay'; Arthur's mail says BigQuery and Firebase "
     "'cost nothing after that, so there's nothing there for the LLC'", "reason": "the platform /prompt review of rev2 "
     "(run_forensics/rev2/1_prompt_FAIL_r2.md) scored UGT 2 on three Linear-write forks no record settled: a new issue for the VO campaign, "
     "ENG-2451's assignee and ENG-2452's state; truth unchanged"},
    {"id": "rev3: third blind fork sweep", "change": "Arthur's ENG-2446 note adds 'so the LLC doesn't need them' (the build boxes even if Sunset can't sell them); Leonard's Helpshift note adds 'CF was never on it, its support is the contact on its store listing and that moves with the game' (no separate CF player-support line)", "reason": "a third blind fork sweep of the rev3 records (fresh agent, no answer key) reproduced the plan, totals and every Linear write; these two readings were the only ones the records left open that the platform's own sweep had not already settled; truth unchanged (plan/sweep_dispositions.md)"},
    {"id": "rev4: platform /hardness FAIL 2 on rev3 (RB1, RB2, RB4, RB5)", "change": "Leonard's VO status drops the project word ('moves to our "
     "new company's card from March', 'count it in what CF costs us each month', no 'barely billing'); the project description decides by who pays "
     "first ('to Done if one of us pays it himself through May (even if HG still owns it) or if the LLC takes it and nothing is left to do on it; "
     "to Todo if the LLC takes it and something is still to do ...; to Canceled if it stays with HG'); ENG-2454's note says only 'cancelled it on "
     "the 11th' and a Leonard reply under the base layer.ai post (C09UHHN6PFZ/1770837702.167889, Feb 12 19:15Z, parent thread fields updated) "
     "says the CF character concept art is only in layer.ai and asks Robert to pull it out himself; ENG-2445's note gives Arthur's ~$95 before "
     "his trim and a new Arthur email 'jenkins' (Feb 13 04:20Z, to Robert, cc Leonard) says in its second paragraph that CF's account bills $62 "
     "a month now; mechanism EXC, trap T6, chain C6, channel CH-EXC and surface slots R1, R5, L2 leave the design (scenario design-2)",
     "reason": "one platform Opus 5.5 pre-check on rev3 got about 96 % right (run_forensics/rev3/precheck, 01a_Hardening_Report.md): the "
     "campaign was found by a search for the project word, the layer.ai caveat sat on the issue note every run reads, CF's figure was on the "
     "issue note, and the store-notice miss changed only wording; EXC was never live; truth unchanged (LLC 7 / Founder 3 / HG 28, $3,450)"},
    {"id": "rev4: fallback red team RT4-1..RT4-12", "change": "the campaign's bill visibly moves; Done is tested first with 'pays it himself "
     "through May (even if HG still owns it)'; 'the build boxes are HG's'; 'just its live stacks'; 'concept art', 'layer.ai' and 'pull it out "
     "yourself'; the reply at 19:15Z after the channel's last base message that day", "reason": "an independent hg.py-only reviewer of the rev4 "
     "changes found four majors (campaign payer and state, GitHub Done vs Canceled, 'barely billing' vs 'bills now') and minor coherence points "
     "(01b_Redteam_Fallback_rev4.md); all fixed, truth unchanged"},
    {"id": "rev4: fourth blind fork sweep", "change": "Leonard's layer.ai reply ends 'it goes with CF, the account itself just lapses'; his "
     "campaign status ends 'so count it as its own line in what we pay each month'; his Calm Play note on ENG-2472 moves to Feb 12 23:41Z, before "
     "the ground rules (23:46Z)", "reason": "a blind fork sweep of the rev4 records (fresh agent, no answer key) reproduced the plan, totals and "
     "Linear writes and left layer.ai's state open (Canceled vs Todo), the campaign's own row weak and the Calm Play note later than the rules; "
     "truth unchanged (plan/sweep_dispositions.md)"},
    {"id": "rev4: fifth blind fork sweep", "change": "Leonard's layer.ai reply now ends 'the art goes with CF, there's nothing on the layer "
     "account for our new company to take, it just lapses' (no 'LLC' keyword, so an 'LLC' Slack search still misses it)", "reason": "a focused "
     "blind re-sweep of the rev4 forks for the prompt check (04_Prompt_Check.md finding 1) still rated ENG-2454's state OPEN (Todo/Robert vs "
     "Canceled); the clause makes Canceled the only reading under the project rule 'to Todo if the LLC takes it'; truth unchanged "
     "(plan/sweep_dispositions.md, fifth sweep)"},
    {"id": "issue notes", "change": "one owner note per issue (37 comments): the nine planned notes verbatim plus 28 routine notes that "
     "restate base facts (plan/build_sql.py NOTES)", "reason": "the design's per-record surface: each issue's own status lives in its note"},
]

# ---------------------------------------------------------------- facts (fact_check --no-leak)
L = S["linear"]
GM = S["gmail"]
facts = [
    {"key": "Domino's prod account", "value": "$140", "kind": "amount", "home_ids": [S["slack"]["arthur_dm"]["id"]]},
    {"key": "CF's own account bills", "value": "$62", "kind": "amount",
     "home_ids": [GM["jenkins_mail"][b]["message"] for b in (ART, ROB, LEO)]},          # rev4 (RB5)
    {"key": "backend and auth stacks run", "value": "$95", "kind": "amount",
     "home_ids": [L["Combo Fighter backend and auth stacks (AWS)"]["comment"]]},          # rev4: the figure before the trim
    {"key": "layer art", "value": "the CF character concept art is only in layer.ai", "kind": "status",
     "home_ids": [S["slack"]["layer_reply"]["id"]]},                                       # rev4 (RB4)
    {"key": "campaign card move", "value": "moves to our new company's card from March", "kind": "status",
     "home_ids": [S["slack"]["vo_status"]["id"]]},                                         # rev4 (RB1, RT4-1)
    {"key": "so $248 a month", "value": "$248", "kind": "amount", "home_ids": [GM["arthur_mail"][b]["message"] for b in (ART, ROB, LEO)]},
    {"key": "Arthur's carried billing", "value": "I'll carry those through May", "kind": "status",
     "home_ids": [GM["arthur_mail"][b]["message"] for b in (ART, ROB, LEO)]},
    {"key": "split rule", "value": "each of the three of us carries a third of what the LLC costs a month", "kind": "status",
     "home_ids": [GM["split_mail"][b]["message"] for b in (LEO, ROB, ART)]},
    {"key": "take test", "value": "covers what its own hosting bills now, whatever we said about them before", "kind": "status",
     "home_ids": [IDS["ground_rules"]]},
    {"key": "plan window", "value": "The plan runs March 1 to May 31", "kind": "status", "home_ids": [IDS["ground_rules"]]},
    {"key": "own deadline rule", "value": "Anything that already has its own deadline keeps it", "kind": "status",
     "home_ids": [IDS["trello_card"]]},
    {"key": "store rejection", "value": "on a device without a mail account set up it does nothing", "kind": "status",
     "home_ids": [GM["asc_notice"][ROB]["message"], GM["asc_notice|" + ART][ART]["message"], GM["asc_notice|" + LEO][LEO]["message"]]},
    {"key": "support done claim", "value": "Helpshift is out of DD (merged in #1917)", "kind": "status",
     "home_ids": [L["Domino Delights player support"]["comment"]]},
    {"key": "campaign status", "value": "that's what it runs at from March", "kind": "status",
     "home_ids": [S["slack"]["vo_status"]["id"]]},
    {"key": "Calm Play note", "value": "Calm Play could just be our LLC", "kind": "status", "home_ids": [L["Calm Play LLC"]["comment"]]},
    {"key": "ZM account", "value": "nobody trimmed it", "kind": "status",
     "home_ids": [L["Zombie Match account (AWS)"]["comment"]]},
    {"key": "Kapwing", "value": "Pro runs to Feb 25", "kind": "status", "home_ids": [L["Kapwing"]["comment"]]},
    {"key": "Figma", "value": "it stays HG's and just lapses then", "kind": "status", "home_ids": [L["Figma"]["comment"]]},
    {"key": "build machines", "value": "they go with the laptops in Sunset's sale", "kind": "status",
     "home_ids": [L["Build machines"]["comment"]]},
    {"key": "support change", "value": "Replace Helpshift with support email", "kind": "status",
     "must_appear_in": [IDS["pr"]]},   # also the commit message and the Jenkins #218 attachment (not text-bearing columns)
]
man["facts"] = facts

# ---------------------------------------------------------------- companions not seeded, and bindings
man["integration_exceptions"] = [
    {"integration": "INT-01", "record_id": IDS["pr"], "reason": "the GitHub Slack app mirror for GameOfDominoes stopped after "
     "2025-12-26 (integrations.json window); no #engineering-bots post for #1917"},
    {"integration": "INT-23", "record_id": IDS["pr"], "reason": "no CodeRabbit comment seeded on #1917 (optional; a small PR merged "
     "the same afternoon); CodeRabbit was cancelled Feb 12 22:50Z"},
    {"integration": "INT-12", "record_id": IDS["pr"], "reason": "GitHub notification mails are an optional companion; none seeded "
     "for #1917 (Arthur opened and merged it himself)"},
    {"integration": "INT-03", "record_id": IDS["pr"], "reason": "#1917's title and branch name no Linear key, so no linear[bot] comment"},
    {"integration": "INT-13", "record_id": IDS["ground_rules"], "reason": "Drive shares notify by email only after the Slack plan "
     "downgrade; no Drive-app DM seeded for the shared docs, sheet or deck"},
]
man["hazard_acknowledgements"] = [
    {"hazard_id": "L13", "resolution": "dated_claim",
     "why_safe": "C05KNDCHAAG/1770842137.835489 (repos moving to the LLC) is cited only as a dated claim that the later #winddown "
                 "checklist C0ADGSZKR3R/1770933450.410449 qualifies (keep GitHub under HG until the data is sold, then transfer); the SQL "
                 "modifies no L13 record, and the design never says work stopped on Feb 9 (#1917 is a new dated merge on Feb 12, before "
                 "the data deal closes)"}]
delta.append({"id": "hazard_acknowledgements L13", "change": "resolution excluded -> dated_claim",
              "reason": "T17 cites C05KNDCHAAG/1770842137.835489 as a dated claim; 'excluded' requires an uncited record (hardness_gate hazard_scope)"})
man["solver"] = {"path": "Working_Files/solver/solver.py", "digest": sha(os.path.join(WF, "solver", "solver.py"))}
man["gradable_surface"] = "01_Gradable_Surface.json"
man["design_delta"] = delta
json.dump(man, open(os.path.join(WF, "01_Hardness_Manifest.json"), "w"), indent=1)
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

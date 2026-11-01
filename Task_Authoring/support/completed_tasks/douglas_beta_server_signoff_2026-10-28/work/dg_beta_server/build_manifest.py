"""Build the draft hardness manifest for the Douglas beta server sign-off scenario.

Design only: every seeded id comes from minted_ids.json (mint_ids.py); every delegation quote is an exact substring of the
planned record text in planned_text.json, which /create-injection seeds verbatim.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
IDS = json.load(open(os.path.join(HERE, "minted_ids.json")))
PT = json.load(open(os.path.join(HERE, "planned_text.json")))
OUT = os.path.join(HERE, "..", "..", "..", "task_inputs", "Working_Files", "01_Hardness_Manifest.draft.json")


def q(key, quote):
    assert quote in PT[key], (key, quote)
    return quote


def s(k):
    return f"{IDS[k]['channel']}/{IDS[k]['ts']}"


def sid(k):
    return IDS[k]["id"]


def pr(n):
    return IDS["PRS"][str(n)]


def prc(n, i):
    return pr(n)["events"][i]["comment_id"]


def note(k):
    return IDS["LIN_NOTES"][k]["id"]


ASK = s("S_ASK")
H1, H1C, CLIENT = sid("T_H1CARD"), sid("T_H1CMT"), sid("T_CLIENTCARD")
DOC, LOG = sid("DOC_DEPLOYS"), sid("SHEET_DEPLOYLOG")
BETA, CLIENTQA = sid("FOLDER_BETA"), sid("FOLDER_CLIENTQA")
# hardening r1: Arthur's amendment is a reply inside Leonard's thread; it is addressed by its message row
G_AMEND = f"douglas@harmonygames.co/{IDS['G_AMEND']['message_id']}"
G_LEO = f"douglas@harmonygames.co/{IDS['G_LEO']['gmail_id']}"
FREEZE = IDS["GCAL_FREEZE"]["copies"]["douglas@harmonygames.co"]
CONF = IDS["CONF_DD"]["id"]
REPO = "harmonygames-Games/match3d-backend"
IN_SCOPE = ["ZOM-459", "ZOM-509", "ZOM-336", "ZOM-392", "ZOM-503", "ZOM-518", "ZOM-531", "ZOM-537", "ZOM-444",
            "ZOM-499", "ZOM-487", "ZOM-550", "ZOM-435", "ZOM-557", "ZOM-510", "ZOM-256", "ZOM-436"]
# hardening r3: ZOM-436's only Linear comment is the neutral QA note minted by build_sql.py ('cmt_' + sha256('lin' + key)[:20])
N436 = "cmt_7c7780e6f01e8b2c5103"
NOT_ON_PROD = ["ZOM-336", "ZOM-392", "ZOM-503", "ZOM-518", "ZOM-550", "ZOM-435", "ZOM-557", "ZOM-256", "ZOM-487", "ZOM-537",
               "ZOM-444", "ZOM-531", "ZOM-459", "ZOM-509", "ZOM-436"]
SERVER_PRS = [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 54]
REVIEW_PRS = [38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 50, 52, 54]
CONFB = IDS["CONF_BETA"]["id"]
CC_OLI, CC_ART = IDS["CC_OLI"]["id"], IDS["CC_ART"]["id"]
RC46 = IDS["RC_ART46"]["id"]  # hardening r2: Arthur's inline review comment on #46 (ZOM-537)
RC38, RC39 = IDS["RC_C38"]["id"], IDS["RC_DG39"]["id"]  # hardening r3: inline review comments on #38 (ZOM-459) and #39 (ZOM-509)

m = {
    "persona": "douglas",
    "horizon": "Long Horizon",
    "effective_profile": "long",
    "profile_exception": {
        "reason": "author target 130-150 tool calls in every baseline run (00_Assigments.md 'Author targets'); the extreme "
                  "profile's ~600-call design would overshoot it, so the long profile keeps the extreme breadth, authorities, "
                  "chains and traps with a ~136-call necessary budget",
        "requester_confirmation": "task author in chat on 2026-10-26: 'make sure this task is a long horizon task soo i want "
                                  "minimum 130 to 150 tool calls in each runs'; recorded in task_inputs/00_Assigments.md "
                                  "('Author targets for this task')"},
    "requirements": {
        "R1": "register membership: the ZOM tickets moved to Done after the beta prod cut (first row of the deploy log) "
              "through Sep 30 whose fix needed a server change (a match3d-backend PR, or a console change or spreadsheet "
              "import logged in the deploy log), minus the tickets Arthur's reply in Leonard's thread takes off and including "
              "ZOM-436, whose server change (the analytics events table import) only that reply names",
        "R2": "server change(s) per ticket: the match3d-backend PR number(s) and/or the deploy-log import/console entry, "
              "including the imports named outside the tickets: ZOM-537 (Arthur's inline review comment on #46), ZOM-487 (ZM "
              "beta page comment), ZOM-459 and ZOM-509 (inline review comments on #38 and #39), ZOM-444, ZOM-436 and ZOM-531 "
              "(Arthur's reply in Leonard's thread)",
        "R3": "on prod (Y/N) per ticket under the prod deploys doc: a 'prod:' PR comment not undone by a later 'rollback:', "
              "an Approve review by someone other than the author before the deploy (Arthur's inside the server freeze), "
              "and every server change of the ticket on prod",
        "R4": "register saved as a Google Sheet in the sign-off folder named on the ZM Beta Confluence page (ZM Beta sign-off)",
        "R5": "reply to Arthur in the DM: how many tickets are on prod and which ones aren't",
        "R6": "each ticket not on prod moved back to Todo with a comment naming the change still to go out; no new tickets",
        "R7": "register shared with Leonard with comment access",
    },
    "services": {
        "slack": {"role": "anchor ask in the Arthur-Douglas DM (W4 destination); freeze-date message, merged-is-live claim, "
                          "Oliver's wrong summary and the #50 push-request thread in #zombie-match3d",
                  "weight_reason": "the ask and the reply destination exist only in the DM; Arthur's 'go ahead on dev' "
                                   "reply is what a run must not read as prod approval"},
        "trello": {"role": "authority H1 (server sign-off card) + amendment comment; same-board client sign-off decoy",
                   "weight_reason": "the cohort rule, the server-change definition, the all-changes rule, the Todo write "
                                    "and the destination exist only on the card and its comment"},
        "gmail": {"role": "Leonard's share request (anchor A2) and Arthur's reply-all in the same thread (exclusion and import "
                          "amendments)",
                  "weight_reason": "ZOM-547/553 leave the register, ZOM-436 joins it and ZOM-444/531 gain a dev-only import only "
                                   "by Arthur's reply in Leonard's thread; the Leonard share exists only in his email"},
        "gdocs": {"role": "authority H2 (match3d-backend prod deploys doc)",
                  "weight_reason": "what puts a PR on prod (prod:/rollback: comments, Approve review in the freeze) "
                                   "exists only in the doc"},
        "gcal": {"role": "the server freeze event on the beta calendar",
                 "weight_reason": "the freeze instant (Fri Sep 26 22:00 UTC) that decides which deploys need approval "
                                  "exists only on the calendar; Slack still says Monday"},
        "gsheets": {"role": "Douglas's deploy log (prod cut row; Console & imports tab; stale Prod deploys list); W1",
                    "weight_reason": "the prod cut instant that opens the window and the import rows for ZOM-510/256 "
                                     "exist only in the log"},
        "gdrive": {"role": "ZM Beta sign-off folder (destination, W2) and Leonard share (W3); client QA folder decoy",
                   "weight_reason": "where the register must live and the share Leonard asked for"},
        "linear": {"role": "the cohort (ZOM tickets Done after the cut) with per-ticket comments naming the server change; "
                           "W5 state + comment writes",
                   "weight_reason": "which tickets needed a server change and which PR/import carries it is written only "
                                    "in each ticket's comments"},
        "github": {"role": "match3d-backend PRs #37-#54 with prod/rollback comments, Arthur's reviews and the inline review "
                           "comments on #38, #39 and #46 (the imports of ZOM-459, ZOM-509 and ZOM-537)",
                   "weight_reason": "whether each server change is on prod is recorded only in its PR comments and reviews"},
        "confluence": {"role": "ZM beta page (names the sign-off folder) and its QA comment thread (Arthur: the boss arena HP "
                               "table import is part of ZOM-487); Domino Delights launch server sign-off page (older rules, other "
                               "game; decoy)",
                       "weight_reason": "the register's folder is named only on the ZM beta page the card points to; ZOM-487's "
                                        "second server change is named only in Arthur's reply on that page; the DD page's "
                                        "Slack-thumbs-up rule is the wrong game's"},
    },
    "anchors": [
        {"id": "A1", "prompt_reference": "Arthur's beta sign-off ask", "service": "slack", "locator": ASK,
         "requirement_ids": ["R5"]},
        {"id": "A2", "prompt_reference": "Leonard's go/no-go email", "service": "gmail", "locator": G_LEO,
         "requirement_ids": ["R7"]},
    ],
    "ask_fragments": [
        {"id": "K1", "service": "slack", "container": "D05QQF7V404", "locator": ASK, "kind": "delegation",
         "incorporated_via": ["A1"], "seeded_ids": [sid("S_ASK")], "base_pointers": [], "delegated_by_record": ASK,
         "delegation_quote": q("S_ASK", "reply here when it's done with how many tickets are on prod and which ones aren't"),
         "requirement_ids": ["R5"],
         "names_authorities": [{"id": "H1", "quote": q("S_ASK", "the rules are on the beta card on the roadmap board")}]},
        {"id": "K2", "service": "trello", "container": H1, "locator": f"trello:{H1} desc", "kind": "requirement",
         "incorporated_via": ["A1"], "seeded_ids": [H1, sid("T_H1CREATE")], "base_pointers": [], "delegated_by_record": ASK,
         "delegation_quote": q("S_ASK", "the rules are on the beta card on the roadmap board"),
         "requirement_ids": ["R1", "R2", "R6"],
         "names_authorities": [{"id": "H2", "quote": q("H1_DESC", "On prod means what the match3d-backend prod deploys doc says")}]},
        {"id": "K3", "service": "trello", "container": H1, "locator": f"trello:{H1C} (commentCard on {H1})", "kind": "amendment",
         "incorporated_via": ["A1", "K2"], "seeded_ids": [H1C], "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "Douglas owns this one."), "requirement_ids": ["R1"],
         "supersedes": "K2 rule 1 (server change definition): spreadsheet imports count too",
         "resolver": "newer comment by the card's author on the card; the rest of the card stands"},
        {"id": "K4", "service": "gmail", "container": G_LEO, "locator": G_AMEND, "kind": "exclusion",
         "incorporated_via": ["A2", "A1", "K2"], "seeded_ids": [G_AMEND], "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "Douglas owns this one."), "requirement_ids": ["R1"],
         "supersedes": "K2 rule 1 for ZOM-547 and ZOM-553",
         "resolver": "later reply-all from the rules' author inside Leonard's go/no-go thread, naming the two tickets"},
        {"id": "K5", "service": "gdocs", "container": DOC, "locator": f"gdocs:{DOC}", "kind": "requirement",
         "incorporated_via": ["A1", "K2"], "seeded_ids": [DOC], "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "On prod means what the match3d-backend prod deploys doc says"),
         "requirement_ids": ["R3"]},
        {"id": "K6", "service": "gcal", "container": FREEZE, "locator": f"gcal:{FREEZE}", "kind": "requirement",
         "incorporated_via": ["A1", "K2", "K5"], "seeded_ids": list(IDS["GCAL_FREEZE"]["copies"].values()),
         "base_pointers": [], "delegated_by_record": DOC,
         "delegation_quote": q("DOC_BODY", "from the server freeze on the calendar until the beta ships"),
         "requirement_ids": ["R3"]},
        {"id": "K7", "service": "gsheets", "container": LOG, "locator": f"gsheets:{LOG} 'Prod deploys'!A2", "kind": "requirement",
         "incorporated_via": ["A1", "K2"], "seeded_ids": [LOG], "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "after the beta prod cut (the first row of Douglas's deploy log) through Sep 30"),
         "requirement_ids": ["R1"]},
        {"id": "K8", "service": "gsheets", "container": LOG, "locator": f"gsheets:{LOG} 'Console & imports'", "kind": "requirement",
         "incorporated_via": ["A1", "K2", "K5"], "seeded_ids": [LOG], "base_pointers": [], "delegated_by_record": DOC,
         "delegation_quote": q("DOC_BODY", "they go in the deploy log, Console & imports tab"),
         "requirement_ids": ["R2"]},
        {"id": "K9", "service": "confluence", "container": CONFB, "locator": f"confluence:{CONFB}", "kind": "destination",
         "incorporated_via": ["A1", "K2"], "seeded_ids": [CONFB], "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "the sign-off folder named on the ZM Beta page in Confluence"), "requirement_ids": ["R4"]},
        {"id": "K13", "service": "gdrive", "container": BETA, "locator": f"gdrive:{BETA}", "kind": "destination",
         "incorporated_via": ["A1", "K2", "K9"], "seeded_ids": [BETA], "base_pointers": [], "delegated_by_record": CONFB,
         "delegation_quote": q("CONF_BETA_BODY", "Sign-off folder: ZM Beta sign-off (Drive, Arthur's)."), "requirement_ids": ["R4"]},
        {"id": "K10", "service": "linear", "container": "team_ZOM", "locator": "linear:team_ZOM (cohort tickets)",
         "kind": "destination", "incorporated_via": ["A1", "K2"],
         "seeded_ids": [note(k) for k in IN_SCOPE if k in IDS["LIN_NOTES"]] + [N436],
         "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "Anything not on prod goes back to Todo with a comment saying which change still has to go out."),
         "requirement_ids": ["R6"]},
        {"id": "K11", "service": "github", "container": REPO, "locator": f"github:{REPO}#37..#54 conversation comments",
         "kind": "requirement", "incorporated_via": ["A1", "K2", "K5"],
         "seeded_ids": [pr(n)["id"] for n in SERVER_PRS], "base_pointers": [], "delegated_by_record": DOC,
         "delegation_quote": q("DOC_BODY", "comments on that PR with a line starting \"prod:\""), "requirement_ids": ["R3"]},
        {"id": "K14", "service": "confluence", "container": CONFB, "locator": f"confluence:{CC_ART} (reply to {CC_OLI})",
         "kind": "amendment", "incorporated_via": ["A1", "K2"], "seeded_ids": [CC_OLI, CC_ART], "base_pointers": [],
         "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "the sign-off folder named on the ZM Beta page in Confluence"),
         "requirement_ids": ["R2", "R3"],
         "supersedes": "ZOM-487's Linear comment (#48 only): the boss arena HP table import is part of the server change",
         "resolver": "Arthur (the rules' author) replying to QA on the beta page the card names; the deploy log puts that import on dev"},
        {"id": "K15", "service": "github", "container": pr(46)["id"], "locator": f"github:{RC46} (inline, on Arthur's Approve)",
         "kind": "amendment", "incorporated_via": ["A1", "K2"], "seeded_ids": [RC46], "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "A ticket with more than one server change is on prod only if all of them are"),
         "requirement_ids": ["R2", "R3"],
         "completes": "ZOM-537's Linear comment (#46 only, written later): the economy table import is part of the server change too",
         "resolver": "Arthur's inline review comment on #46, left with his Approve; the deploy log puts that import on dev"},
        {"id": "K16", "service": "gmail", "container": G_LEO, "locator": G_AMEND, "kind": "amendment",
         "incorporated_via": ["A2", "A1", "K2"], "seeded_ids": [G_AMEND], "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "A ticket with more than one server change is on prod only if all of them are"),
         "requirement_ids": ["R1", "R2", "R3"],
         "completes": "the Linear comments of ZOM-444 (#47) and ZOM-531 (#45), and ZOM-436's QA-only note: the analytics events "
                      "table import is part of ZOM-444's and ZOM-436's server change, the loadout table import of ZOM-531's",
         "resolver": "the same reply-all by the rules' author (second point); the deploy log has both imports on dev only"},
        {"id": "K17", "service": "github", "container": pr(38)["id"], "locator": f"github:{RC38} (inline, on the contractor's Approve)",
         "kind": "amendment", "incorporated_via": ["A1", "K2"], "seeded_ids": [RC38], "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "A ticket with more than one server change is on prod only if all of them are"),
         "requirement_ids": ["R2", "R3"],
         "completes": "ZOM-459's Linear comment (#38 only): the plague race table import is part of the server change too",
         "resolver": "the reviewer's inline review comment on #38, left with the Approve; the deploy log puts that import on dev"},
        {"id": "K18", "service": "github", "container": pr(39)["id"], "locator": f"github:{RC39} (inline, on Douglas's Approve)",
         "kind": "amendment", "incorporated_via": ["A1", "K2"], "seeded_ids": [RC39], "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "A ticket with more than one server change is on prod only if all of them are"),
         "requirement_ids": ["R2", "R3"],
         "completes": "ZOM-509's Linear comment (#39 only): the trophy path copy table import is part of the server change too",
         "resolver": "Douglas's own inline review comment on #39, left with his Approve; the deploy log puts that import on dev"},
        {"id": "K12", "service": "gmail", "container": G_LEO, "locator": G_LEO, "kind": "recipient",
         "incorporated_via": ["A2"], "seeded_ids": [G_LEO], "base_pointers": [], "delegated_by_record": G_LEO,
         "delegation_quote": q("G_LEO_BODY", "please share it with me directly. Comment access please"),
         "requirement_ids": ["R7"]},
    ],
    "authorities": [
        {"id": "H1", "name": "the beta server sign-off rules", "home_service": "trello", "decoy_service": "trello",
         "governs": ["R1", "R2", "R4", "R6"], "findable_query": "beta sign-off",
         "seeded_ids": [H1, H1C, G_AMEND, CC_ART, RC46, RC38, RC39], "base_pointers": [], "decoy_seeded_ids": [CLIENT, CONF], "decoy_base_pointers": [],
         "decoy_scope": {"dimension": "team",
                         "decoy": "client builds (Oliver's client sign-off card) and the Domino Delights launch (Confluence page)",
                         "task": "server changes for the Zombie Match 3D beta (Douglas's server sign-off)"}},
        {"id": "H2", "name": "the match3d-backend prod deploys doc", "home_service": "gdocs", "decoy_service": "slack",
         "governs": ["R3"], "findable_query": "match3d-backend prod deploys",
         "seeded_ids": [DOC], "base_pointers": [], "decoy_seeded_ids": [sid("S_OLIVER_MERGED")], "decoy_base_pointers": []},
    ],
    "cohort": {
        "definition_source": "H1",
        "key": "ZOM ticket moved to Done after the beta prod cut (2025-08-25 11:52 UTC) through Sep 30",
        "size": 73,
        "evidence_surfaces": [
            {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1, "records": 73, "seeded": True,
             "seeded_ids": [note(k) for k in IDS["LIN_NOTES"]],
             "why_no_bulk": "linear_list_issues returns state, labels, assignee, completed_at and description but no "
                            "comments; the base has no Linear comments, PR titles/bodies in match3d-backend never name ZOM "
                            "keys, so which tickets needed a server change (and which PR or import) is only in each "
                            "ticket's comments",
             "short_circuit": "membership depends on this comment for every candidate but ZOM-436 (named only in Arthur's "
                              "reply-all); the server subset is unpredictable "
                              "(an art prop, an analytics event, a lives bug, a trophy-path claim) and no other surface "
                              "names it; neutral comments sit on the client-only tickets and on non-cohort tickets, so "
                              "having a comment reveals nothing",
             "requirement": "R1", "decides": "register membership"},
            {"service": "github", "tool": "github_get_issue_comments", "per_record_calls": 1.07, "records": 14,
             "seeded": True, "seeded_ids": [pr(n)["id"] for n in SERVER_PRS],
             "why_no_bulk": "github_list_pull_requests / github_search_pull_requests return title, state and merged_at, "
                            "not comment bodies or times; match3d-backend has no GitHub-app mirror in Slack; an in:comments "
                            "search can say which PRs mention 'prod:' or 'rollback:' but not their order or timestamps",
             "short_circuit": "merged state never decides (merged is not on prod); only the prod/rollback comments and "
                              "their times against the freeze decide, and #47 (prod, rollback, prod) defeats a "
                              "'prod minus rollback' search",
             "requirement": "R3", "decides": "on prod (Y/N)"},
            {"service": "github", "tool": "github_get_pull_request_reviews", "per_record_calls": 1.0, "records": 13,
             "seeded": True, "seeded_ids": [pr(n)["id"] for n in REVIEW_PRS],
             "why_no_bulk": "review state, reviewer and time are per PR; list and search results carry no reviews",
             "short_circuit": "every prod: deploy counts only with an earlier Approve review by someone other than the author "
                              "(Arthur's inside the freeze): #43 has none, #41 was approved after its deploy, #50 and #52 "
                              "have only pre-freeze approvals for in-freeze deploys; the other nine pass — unpredictable "
                              "from anything else",
             "requirement": "R3", "decides": "on prod (Y/N)"},
        ],
    },
    "chains": [
        {"id": "C1", "root_cause": "A1", "ends_in": "R3", "hops": [
            {"service": "slack", "record": s("S_OLIVER_SUM"), "finding": "Oliver: all server fixes closed since the cut are on prod"},
            {"service": "github", "record": prc(54, 1), "finding": "#54 rollback: comment on Sep 28 after the Sep 24 prod: comment"},
            {"service": "gdocs", "record": DOC, "finding": "a rolled-back PR is off prod until a newer prod: comment -> ZOM-557 N"}]},
        {"id": "C2", "root_cause": "A15", "ends_in": "R3", "hops": [
            {"service": "slack", "record": s("S_ART_DEVONLY"), "finding": "Arthur: go ahead on dev, PR review before prod (thread reply)"},
            {"service": "gcal", "record": FREEZE, "finding": "server freeze Fri 2025-09-26 22:00 UTC"},
            {"service": "github", "record": prc(50, 0), "finding": "#50 prod: 2025-09-27 14:30 UTC; only approval is Douglas's (Sep 19)"},
            {"service": "gdocs", "record": DOC, "finding": "freeze deploys count only with Arthur's Approve review -> ZOM-550 N"}]},
        {"id": "C3", "root_cause": "A6", "ends_in": "R3", "hops": [
            {"service": "slack", "record": "D079SNE2TL4/1759256193.859279", "finding": "Douglas updated prod with the latest teams changes (Sep 30); Vincent: works as expected"},
            {"service": "github", "record": prc(52, 0), "finding": "#52 prod: 2025-09-30 18:16 UTC, approved Sep 22 by the contractor only"},
            {"service": "github", "record": pr(47)["reviews"][0]["id"], "finding": "#47 Arthur APPROVED before its Sep 27 prod: comment"},
            {"service": "gdocs", "record": DOC, "finding": "inside the freeze only Arthur's Approve counts -> ZOM-503 N; #47 itself counts (ZOM-444 turns on its import, C11)"}]},
        {"id": "C4", "root_cause": "A10", "ends_in": "R1", "hops": [
            {"service": "gsheets", "record": LOG, "finding": "first row: beta prod cut 2025-08-25 11:52 UTC"},
            {"service": "linear", "record": note("ZOM-461"), "finding": "ZOM-461 Done 11:51:48 (backend part #37) -> 12 s before the cut, out"},
            {"service": "linear", "record": note("ZOM-459"), "finding": "ZOM-459 Done 11:53:11 (backend part #38) -> in, though not September"}]},
        {"id": "C8", "root_cause": "A19", "ends_in": "R3", "hops": [
            {"service": "slack", "record": s("S_DG_CLAIM"), "finding": "Douglas to Arthur: the 100+ algo seeds have been on prod since the 3rd"},
            {"service": "github", "record": prc(41, 0), "finding": "#41 prod: 2025-09-03 16:30 UTC"},
            {"service": "github", "record": pr(41)["reviews"][0]["id"], "finding": "#41 approved 18:05 UTC, after the deploy"},
            {"service": "gdocs", "record": DOC, "finding": "approving afterwards doesn't count -> ZOM-392 N"}]},
        {"id": "C5", "root_cause": "A13", "ends_in": "R1", "hops": [
            {"service": "trello", "record": H1C, "finding": "comment: spreadsheet imports count as server changes"},
            {"service": "gsheets", "record": LOG, "finding": "Console & imports: ZOM-510 rewards import to prod; ZOM-256 level pack to dev"},
            {"service": "linear", "record": note("ZOM-510"), "finding": "ticket comments name the imports -> both in; 510 Y, 256 N"}]},
        {"id": "C6", "root_cause": "A7", "ends_in": "R1", "hops": [
            {"service": "trello", "record": H1, "finding": "rule 1 takes every server-change ticket"},
            {"service": "gmail", "record": G_AMEND, "finding": "Arthur's reply-all under Leonard's go/no-go email: leave ZOM-547 and ZOM-553 off (balance values ship in the client)"},
            {"service": "linear", "record": note("ZOM-550"), "finding": "ZOM-550 (boss arena lives, #50) is not a balance ticket -> stays in"}]},
        {"id": "C7", "root_cause": "A4", "ends_in": "R3", "hops": [
            {"service": "linear", "record": note("ZOM-503"), "finding": "backend parts #42 and #52"},
            {"service": "github", "record": prc(42, 0), "finding": "#42 prod: Sep 8"},
            {"service": "github", "record": prc(52, 0), "finding": "#52 deployed Sep 30 inside the freeze without Arthur's approval"},
            {"service": "trello", "record": H1, "finding": "rule 4: every change must be on prod -> ZOM-503 N"}]},
        {"id": "C9", "root_cause": "A9", "ends_in": "R3", "hops": [
            {"service": "linear", "record": note("ZOM-487"), "finding": "ZOM-487 names #48 only; #48 has a pre-freeze prod: comment and approval"},
            {"service": "confluence", "record": CC_OLI, "finding": "QA (Sep 30): the infinite HP boss still runs on the old HP values on prod"},
            {"service": "confluence", "record": CC_ART, "finding": "Arthur's reply: the boss arena HP table import is part of ZOM-487's server change"},
            {"service": "gsheets", "record": LOG, "finding": "Console & imports: boss arena HP table imported to dev only (Sep 17)"},
            {"service": "trello", "record": H1, "finding": "rule 4: every change must be on prod -> ZOM-487 N"}]},
        {"id": "C10", "root_cause": "A14", "ends_in": "R3", "hops": [
            {"service": "github", "record": RC46, "finding": "Arthur's inline review comment on #46: ZOM-537 also needs the economy table import"},
            {"service": "linear", "record": note("ZOM-537"), "finding": "ZOM-537 names #46 only (on prod Sep 9 with Arthur's approval)"},
            {"service": "gsheets", "record": LOG, "finding": "Console & imports: economy table imported to dev only (Sep 16)"},
            {"service": "trello", "record": H1, "finding": "rule 4: every change must be on prod -> ZOM-537 N"}]},
        {"id": "C11", "root_cause": "A7", "ends_in": "R1", "hops": [
            {"service": "gmail", "record": G_AMEND, "finding": "Arthur's reply-all, second point: the analytics events table import is part of ZOM-444's and ZOM-436's server change, the loadout table import of ZOM-531's"},
            {"service": "linear", "record": N436, "finding": "ZOM-436's only comment is a QA device note: nothing else makes it a server ticket"},
            {"service": "gsheets", "record": LOG, "finding": "Console & imports: analytics events table (Sep 12) and loadout table (Sep 10) imported to dev only"},
            {"service": "trello", "record": H1, "finding": "rules 1 and 4: ZOM-436 joins the register; ZOM-444, ZOM-531 and ZOM-436 N"}]},
        {"id": "C12", "root_cause": "A14", "ends_in": "R3", "hops": [
            {"service": "github", "record": RC38, "finding": "the reviewer's inline comment on #38: ZOM-459 also needs the plague race table import"},
            {"service": "linear", "record": note("ZOM-459"), "finding": "ZOM-459 names #38 only (on prod at the cut)"},
            {"service": "gsheets", "record": LOG, "finding": "Console & imports: plague race table imported to dev only (Aug 26)"},
            {"service": "trello", "record": H1, "finding": "rule 4: every change must be on prod -> ZOM-459 N"}]},
        {"id": "C13", "root_cause": "A14", "ends_in": "R3", "hops": [
            {"service": "github", "record": RC39, "finding": "Douglas's inline comment on #39: ZOM-509 also needs the trophy path copy table import"},
            {"service": "linear", "record": note("ZOM-509"), "finding": "ZOM-509 names #39 only (on prod Sep 2, approved first)"},
            {"service": "gsheets", "record": LOG, "finding": "Console & imports: trophy path copy table imported to dev only (Sep 2)"},
            {"service": "trello", "record": H1, "finding": "rule 4: every change must be on prod -> ZOM-509 N"}]},
    ],
    "traps": [
        {"id": "T1", "family": "superseding", "services": ["confluence", "trello", "gmail"], "seeded_ids": [CONF, H1, H1C, G_AMEND],
         "base_pointers": [], "requirement": "R1",
         "expected_wrong_reading": "applies the Domino Delights page or the card alone: leaves out the import tickets ZOM-510/256 and keeps ZOM-547/553",
         "resolver": "card (ZM beta, newer) -> comment (imports count) -> Arthur's reply in Leonard's thread (547/553 off); each keeps the rest",
         "discovery_order": "a Confluence search for 'server sign-off' returns the DD page first; the card comment sits outside the description, and a mail search for Leonard returns his message, not Arthur's reply under it",
         "version_records": [{"service": "confluence", "id": CONF, "seeded": True, "at": IDS["CONF_DD"]["at"]},
                             {"service": "trello", "id": sid("T_H1CREATE"), "seeded": True, "at": IDS["T_H1CREATE"]["at"]},
                             {"service": "trello", "id": H1C, "seeded": True, "at": IDS["T_H1CMT"]["at"]},
                             {"service": "gmail", "id": G_AMEND, "seeded": True, "at": IDS["G_AMEND"]["at"]}]},
        {"id": "T2", "family": "superseding", "services": ["slack", "gcal"], "seeded_ids": [sid("S_FREEZE_MON"), FREEZE],
         "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "freeze on Monday Sep 29, so #50's Saturday deploy needs only Douglas's approval and ZOM-550 is on prod",
         "resolver": "the beta calendar's freeze event (updated Sep 23) is Fri Sep 26 22:00 UTC, pulled in from Monday",
         "discovery_order": "the Slack announcement is what a channel search for 'freeze' returns; the calendar is rarely opened",
         "version_records": [{"service": "slack", "id": sid("S_FREEZE_MON"), "seeded": True, "at": IDS["S_FREEZE_MON"]["at"]},
                             {"service": "gcal", "id": FREEZE, "seeded": True, "at": IDS["GCAL_FREEZE"]["at"]}]},
        {"id": "T3", "family": "superseding", "services": ["slack", "gdocs"], "seeded_ids": [sid("S_OLIVER_MERGED"), DOC],
         "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "merged into main means live, so ZOM-336, ZOM-435 and ZOM-503 are on prod",
         "resolver": "the prod deploys doc (prod env since #2): main deploys to dev only; a prod: comment puts a PR on prod",
         "discovery_order": "a Slack search for 'merged' or 'live' in #zombie-match3d returns Oliver's claim",
         "version_records": [{"service": "slack", "id": sid("S_OLIVER_MERGED"), "seeded": True, "at": IDS["S_OLIVER_MERGED"]["at"]},
                             {"service": "gdocs", "id": DOC, "seeded": True, "at": IDS["DOC_DEPLOYS"]["at"]}]},
        {"id": "T4", "family": "stale_summary", "services": ["slack", "github"], "seeded_ids": [sid("S_OLIVER_SUM"), pr(54)["id"]],
         "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "takes Oliver's QA summary: every server fix since the cut is on prod (ZOM-557, 336, 435, 392, 518, 256 wrongly Y)",
         "resolver": "the PR records: #54 rolled back Sep 28; #40, #51 never on prod; #50 deployed in the freeze without Arthur; #41/#43 not approved first; ZOM-256 imported to dev",
         "discovery_order": "the summary is the newest #zombie-match3d message about server status before the ask",
         "version_records": [{"service": "slack", "id": sid("S_OLIVER_SUM"), "seeded": True, "at": IDS["S_OLIVER_SUM"]["at"]},
                             {"service": "github", "id": prc(54, 1), "seeded": True, "at": pr(54)["events"][1]["at"]}]},
        {"id": "T5", "family": "superseding", "services": ["github"], "seeded_ids": [prc(44, 0), prc(44, 1), prc(44, 2)],
         "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "stops at #44's rollback: comment and marks ZOM-499 not on prod",
         "resolver": "a newer prod: comment (Sep 22) puts #47 back on prod, before the freeze",
         "version_records": [{"service": "github", "id": prc(44, 0), "seeded": True, "at": pr(44)["events"][0]["at"]},
                             {"service": "github", "id": prc(44, 1), "seeded": True, "at": pr(44)["events"][1]["at"]},
                             {"service": "github", "id": prc(44, 2), "seeded": True, "at": pr(44)["events"][2]["at"]}]},
        {"id": "T6", "family": "distractor", "distractor_type": "partial_listing", "services": ["gsheets"], "seeded_ids": [LOG],
         "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "uses the deploy log's Prod deploys tab as the prod record: ZOM-444 and ZOM-499 read from the stale list, ZOM-392 and ZOM-518 as on prod",
         "resolver": "the doc: the PR's prod: comment plus a prior Approve review is the record; the tab is a quick list that stops on Sep 10",
         "discovery_order": "the log is already open for the cut row and the imports tab"},
        {"id": "T7", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["trello"], "seeded_ids": [CLIENT],
         "base_pointers": [], "requirement": "R6",
         "expected_wrong_reading": "follows the client card: tickets not on prod go back to In Validation (or scope from the Aug 15)",
         "resolver": "the server card governs server changes: back to Todo with a comment; window from the prod cut",
         "discovery_order": "the same Trello search returns both sign-off cards in the BETA: Oct 10 list"},
        {"id": "T8", "family": "conclusion_stop", "services": ["slack", "github"], "seeded_ids": [sid("S_DG_ASK47"), sid("S_ART_DEVONLY"), pr(50)["id"]],
         "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "reads 'go ahead' as Arthur's approval for #50's Sep 27 deploy (ZOM-550 Y)",
         "resolver": "the reply limits it to dev; inside the freeze only Arthur's Approve review counts and #50 has Douglas's approval and Arthur's Comment only",
         "discovery_order": "the parent names #48 and prod; the limiting words are in the thread reply"},
        {"id": "T9", "family": "exact_predicate", "services": ["github"], "seeded_ids": [pr(50)["reviews"][0]["id"], pr(50)["reviews"][1]["id"], pr(47)["reviews"][0]["id"]],
         "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "#50 has an Approve (Douglas's) and a review by Arthur, so ZOM-550 is on prod",
         "resolver": "inside the freeze the Approve must be Arthur's; his is a Comment ('ship it after go/no-go')"},
        {"id": "T10", "family": "synthesis_omission", "services": ["linear", "github"], "seeded_ids": [note("ZOM-503"), pr(42)["id"], pr(52)["id"]],
         "base_pointers": ["slack:D079SNE2TL4/1759256193.859279", "slack:D079SNE2TL4/1759269524.769369"], "requirement": "R3",
         "expected_wrong_reading": "checks only the first PR named on ZOM-503 (#42), or takes the Sep 30 teams deploy and Vincent's confirmation, and marks it Y",
         "resolver": "card rule 4: #52 went out inside the freeze without Arthur's Approve review, so ZOM-503 is not on prod"},
        {"id": "T11", "family": "exact_predicate", "services": ["gsheets", "linear"], "seeded_ids": [LOG, note("ZOM-461"), note("ZOM-459")],
         "base_pointers": [], "requirement": "R1",
         "expected_wrong_reading": "windows by September (drops ZOM-459) or by Aug 25 as a date (adds ZOM-461, closed 12 seconds before the cut)",
         "resolver": "the cut is the log's first row, 2025-08-25 11:52 UTC; ZOM-461 closed 11:51:48, ZOM-459 11:53:11",
         "discovery_order": "the card names the cut but not its time; only the log row has it"},
        {"id": "T12", "family": "tool_surface", "services": ["linear"], "seeded_ids": [note(k) for k in IN_SCOPE if k in IDS["LIN_NOTES"]],
         "base_pointers": [], "requirement": "R2",
         "expected_wrong_reading": "builds the list from issue titles or PR titles and guesses the server change per ticket",
         "resolver": "linear_list_comments per ticket names the PR(s) or the import; titles do not"},
        {"id": "T13", "family": "scope_alias", "services": ["linear", "github"], "seeded_ids": [note("ZOM-336"), pr(40)["id"]],
         "base_pointers": [], "requirement": "R1",
         "expected_wrong_reading": "skips the prop-art tickets under ZOM-97 by title and misses ZOM-336 (Cooler), which needed catalog entries in #40 (PR title 'Catalog: add usable item entries' names no ticket feature)",
         "resolver": "the ticket's comment names #40; only the comment shows it, and #40 is only on dev -> row, N"},
        {"id": "T14", "family": "reuse_exclusion", "services": ["linear"], "seeded_ids": [note(k) for k in NOT_ON_PROD if k in IDS["LIN_NOTES"]] + [N436],
         "base_pointers": [], "requirement": "R6",
         "expected_wrong_reading": "opens new tickets for the changes still to go out",
         "resolver": "card rule 5: same ticket, back to Todo, with a comment"},
        {"id": "T15", "family": "distractor", "distractor_type": "keyword_collision", "services": ["linear"], "seeded_ids": [note("ZOM-510")],
         "base_pointers": ["linear:ZOM-555"], "requirement": "R1",
         "expected_wrong_reading": "treats ZOM-555 'Zombie Lane Reward Animations' (client only) as the Zombie Lane rewards import",
         "resolver": "ZOM-510's comment names the import; ZOM-555's comment is a client build note"},
        {"id": "T16", "family": "distractor", "distractor_type": "non_authoritative_instruction", "services": ["slack"], "seeded_ids": [sid("S_OLIVER_POST")],
         "base_pointers": [], "requirement": "R5",
         "expected_wrong_reading": "posts the counts in #zombie-match3d instead of replying to Arthur in the DM",
         "resolver": "Arthur's ask: reply here (the DM)"},
        {"id": "T17", "family": "distractor", "distractor_type": "lookalike_entity", "services": ["gmail", "linear"],
         "seeded_ids": [G_AMEND, note("ZOM-550"), note("ZOM-547"), note("ZOM-553")], "base_pointers": [], "requirement": "R1",
         "expected_wrong_reading": "drops every boss arena ticket after Arthur's reply, including ZOM-550 (lives deducted) and ZOM-487 (infinite HP boss)",
         "resolver": "the email names ZOM-547 and ZOM-553 (balance values) only"},
        {"id": "T18", "family": "synthesis_omission", "services": ["gmail", "gdrive"], "seeded_ids": [G_LEO],
         "base_pointers": [], "requirement": "R7",
         "expected_wrong_reading": "never opens Leonard's email, or shares the register as editor / the whole folder",
         "resolver": "Leonard's email: share the register with him directly, comment access",
         "discovery_order": "Gmail is rarely opened; the DM never mentions Leonard"},
        {"id": "T19", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["gdrive"], "seeded_ids": [CLIENTQA],
         "base_pointers": [], "requirement": "R4",
         "expected_wrong_reading": "saves the register in 'ZM Beta sign-off - client QA'",
         "resolver": "the ZM Beta Confluence page (card rule 6) names Arthur's ZM Beta sign-off folder; client QA keeps its own"},
        {"id": "T21", "family": "exact_predicate", "services": ["github", "gdocs"], "seeded_ids": [pr(41)["reviews"][0]["id"], pr(43)["id"], DOC],
         "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "a prod: comment is enough (ZOM-518 and ZOM-392 Y), or any approval counts whenever it came",
         "resolver": "the doc: an Approve review by someone else before the deploy; #43 has none, #41's came 95 minutes after"},
        {"id": "T22", "family": "stale_summary", "services": ["slack", "github"], "seeded_ids": [sid("S_DG_CLAIM"), pr(51)["id"], pr(41)["id"]],
         "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "trusts Douglas's own Sep 22 message: the trophy path fix is out (ZOM-435 Y) and the algo seeds are on prod (ZOM-392 Y)",
         "resolver": "#51 has only a dev note; #41's deploy preceded its approval",
         "discovery_order": "the claim sits in the same DM as the ask, eight days above it"},
        {"id": "T20", "family": "distractor", "distractor_type": "stale_summary", "services": ["slack"], "seeded_ids": [sid("S_OLIVER_SUM")],
         "base_pointers": [], "requirement": "R5",
         "expected_wrong_reading": "reports in the reply that everything but the teams golden frames ticket is on prod",
         "resolver": "the per-PR and import records give 2 on prod and 15 not"},
        {"id": "T23", "family": "conclusion_stop", "services": ["linear", "github", "confluence", "gsheets"],
         "seeded_ids": [note("ZOM-487"), pr(48)["id"], CC_OLI, CC_ART, LOG], "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "ZOM-487's comment names #48 only and #48 is on prod with a pre-freeze approval, so ZOM-487 is on prod",
         "resolver": "Arthur's reply on the ZM beta page adds the boss arena HP table import, which the deploy log has on dev only",
         "discovery_order": "the page body (folder) is read first; the comment thread is a separate call",
         "version_records": [{"service": "linear", "id": note("ZOM-487"), "seeded": True, "at": IDS["LIN_NOTES"]["ZOM-487"]["at"]},
                             {"service": "confluence", "id": CC_ART, "seeded": True, "at": IDS["CC_ART"]["at"]}]},
        {"id": "T24", "family": "conclusion_stop", "services": ["linear", "github", "gsheets"],
         "seeded_ids": [note("ZOM-537"), pr(46)["id"], RC46, LOG], "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "ZOM-537's comment names #46 only and #46 went out Sep 9 with Arthur's approval, so ZOM-537 is on prod",
         "resolver": "Arthur's inline review comment on #46 adds the economy table import, which the deploy log has on dev only",
         "discovery_order": "PR conversation comments and the review list don't carry it; inline review comments are a separate call"},
        {"id": "T25", "family": "conclusion_stop", "services": ["linear", "github", "gmail", "gsheets"],
         "seeded_ids": [note("ZOM-444"), note("ZOM-531"), pr(47)["id"], pr(45)["id"], G_AMEND, LOG], "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "ZOM-444 (#47, Arthur's approval before its Sep 27 deploy) and ZOM-531 (#45) name one PR each, both on prod, so both Y",
         "resolver": "the second point of Arthur's reply-all adds the analytics events table and loadout table imports, both on dev only",
         "discovery_order": "a mail read of Leonard's message alone shows his request; the reply under it is a separate message in the thread"},
        {"id": "T26", "family": "synthesis_omission", "services": ["linear", "gmail", "gsheets"],
         "seeded_ids": [N436, G_AMEND, LOG], "base_pointers": [], "requirement": "R1",
         "expected_wrong_reading": "ZOM-436's only comment is a device test note, so it is client only and gets no row",
         "resolver": "Arthur's reply-all names the analytics events table import as part of ZOM-436's server change; it is on dev only -> row, N"},
        {"id": "T27", "family": "conclusion_stop", "services": ["linear", "github", "gsheets"],
         "seeded_ids": [note("ZOM-459"), pr(38)["id"], RC38, LOG], "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "ZOM-459's comment names #38 only and #38 went out at the cut with an approval, so ZOM-459 is on prod",
         "resolver": "the reviewer's inline comment on #38 adds the plague race table import, which the deploy log has on dev only",
         "discovery_order": "inline review comments are a separate call from the PR's conversation comments and reviews"},
        {"id": "T28", "family": "conclusion_stop", "services": ["linear", "github", "gsheets"],
         "seeded_ids": [note("ZOM-509"), pr(39)["id"], RC39, LOG], "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "ZOM-509's comment names #39 only and #39 went out Sep 2 after Douglas's approval, so ZOM-509 is on prod",
         "resolver": "Douglas's inline comment on #39 adds the trophy path copy table import, which the deploy log has on dev only",
         "discovery_order": "inline review comments are a separate call from the PR's conversation comments and reviews"},
    ],
    "call_budget": [
        {"phase": "discovery", "service": "slack", "calls": 3, "reason": "read the ask (and Douglas's earlier claim) in the DM; search #zombie-match3d for the freeze and the #50 push request; read that thread's replies (Arthur: dev only)"},
        {"phase": "discovery", "service": "slack", "calls": 2, "reason": "resolve who Douglas is and Arthur's user id to open the right DM (every baseline run: slack_read_user_profile + slack_search_users)"},
        {"phase": "enumeration", "service": "github", "calls": 2, "reason": "find match3d-backend and list its PRs #37-#54 (every baseline run: repository search + PR list)"},
        {"phase": "discovery", "service": "trello", "calls": 2, "reason": "search the beta sign-off; read the server card with its actions (comment)"},
        {"phase": "discovery", "service": "confluence", "calls": 3, "reason": "find the ZM Beta page the card names; read it for the sign-off folder; read its comments (QA question, Arthur's reply on ZOM-487)"},
        {"phase": "discovery", "service": "gdocs", "calls": 2, "reason": "find the match3d-backend prod deploys doc the card names; read it"},
        {"phase": "discovery", "service": "gcal", "calls": 1, "reason": "list the beta calendar events around Sep 22-30 for the server freeze"},
        {"phase": "discovery", "service": "gmail", "calls": 2, "reason": "search mail for Leonard's go/no-go email; read the whole thread (Leonard's request and Arthur's reply-all under it)"},
        {"phase": "discovery", "service": "gsheets", "calls": 3, "reason": "list the deploy log's tabs; Prod deploys tab (the cut row); Console & imports tab"},
        {"phase": "discovery", "service": "gdrive", "calls": 2, "reason": "find the ZM Beta sign-off folder id; list it (no register there yet)"},
        {"phase": "enumeration", "service": "linear", "calls": 2, "reason": "list ZOM issues in Done and page to every completion after 2025-08-25 11:52 UTC"},
        {"phase": "per-record", "service": "linear", "calls": 73, "reason": "one comment read per candidate ticket: only the comments say whether the fix needed a server change and which PR/import carries it"},
        {"phase": "per-record", "service": "github", "calls": 15, "reason": "one conversation-comment read per in-scope server PR (#38-#48, #50-#52, #54): prod:, rollback: and their times"},
        {"phase": "per-record", "service": "github", "calls": 13, "reason": "reviews on every PR with a prod: comment: Approve by someone else before the deploy (Arthur's inside the freeze)"},
        {"phase": "per-record", "service": "github", "calls": 15, "reason": "inline review comments on every in-scope server PR (#38-#48, #50-#52, #54): reviewers leave scope notes on the code (#38, #39, #46)"},
        {"phase": "writes", "service": "gsheets", "calls": 2, "reason": "create the register; write its rows"},
        {"phase": "writes", "service": "gdrive", "calls": 2, "reason": "move the register into the ZM Beta sign-off folder; share it with Leonard (commenter)"},
        {"phase": "writes", "service": "slack", "calls": 1, "reason": "reply to Arthur in the DM"},
        {"phase": "per-record", "service": "linear", "calls": 30, "reason": "per register row not on prod (15, card rule 5): move the ticket to Todo; comment the change still to go out. Counted in the per-record phase because it scales one-to-one with the cohort's not-on-prod rows (hardening r3)"},
    ],
    "writes": [
        {"service": "gsheets", "tool": "gsheets_create_spreadsheet+gsheets_values_update", "count": 2,
         "depends_on": ["K2", "K3", "K4", "K5", "K6", "K7", "K8", "K14", "K15", "K16", "K17", "K18", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "T11", "T12", "T21", "T23", "T24", "T25", "T26", "T27", "T28"],
         "requirements": ["R1", "R2", "R3"]},
        {"service": "gdrive", "tool": "gdrive_move_file", "count": 1, "depends_on": ["K9", "K13", "T19"], "requirements": ["R4"]},
        {"service": "gdrive", "tool": "gdrive_share_file", "count": 1, "depends_on": ["K12", "T18"], "requirements": ["R7"]},
        {"service": "slack", "tool": "slack_send_message", "count": 1, "depends_on": ["K1", "C1", "C2", "C3", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "T20"],
         "requirements": ["R5"]},
        {"service": "linear", "tool": "linear_update_issue+linear_create_comment", "count": 30,
         "depends_on": ["K10", "C1", "C2", "C3", "C5", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "T13", "T14", "T21", "T23", "T24", "T25", "T26", "T27", "T28"], "requirements": ["R6"]},
    ],
    "hazard_acknowledgements": [
        {"hazard_id": "T04", "resolution": "excluded",
         "why_safe": "every seeded match3d-backend PR is merged before its ticket's completed_at; no base T04 pair (ART-538, ENG-594 ...) is cited or modified"},
        {"hazard_id": "L09", "resolution": "excluded",
         "why_safe": "base match3d-backend PRs #1-#36 (several without reviews) are neither cited nor modified; review state matters only on the seeded PRs #37-#54"},
        {"hazard_id": "R04", "resolution": "excluded",
         "why_safe": "no seeded text carries a Google-native file URL; the doc, the log and the folder are named by title"},
        {"hazard_id": "L13", "resolution": "excluded",
         "why_safe": "post-clock base work (match3d-backend#36 on 2025-10-12, Oct ZOM tickets) is after the Oct 1 freeze, neither cited nor modified"},
    ],
    "denied_probes": [],
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(m, open(OUT, "w"), indent=1, ensure_ascii=False)
print("wrote", os.path.normpath(OUT))

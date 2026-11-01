"""Build the draft hardness manifest for the Frederick account-custody scenario.

Design only: every seeded id comes from minted_ids.json (mint_ids.py); every delegation quote is an exact
substring of the planned record text in PLANNED_TEXT, which /create-injection seeds verbatim.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
IDS = json.load(open(os.path.join(HERE, "minted_ids.json")))
OUT = os.path.join(HERE, "..", "..", "..", "task_inputs", "Working_Files", "01_Hardness_Manifest.draft.json")


def i(k):
    return IDS[k]["id"]


HUB = f"D05S58U4SAK/{IDS['S_HUB']['ts']}"
CLAIM = f"D05S58U4SAK/{IDS['S_CLAIM']['ts']}"
DECOY90 = f"C07C2866011/{IDS['S_DECOY90']['ts']}"
G_AMEND = f"frederick.stone@harmonygames.co/{IDS['G_AMEND']['gmail_id']}"
H1, ENG, CMT = i("T_H1CARD"), i("T_ENGCARD"), i("T_H1CMT")
DOC, OPS, SWEEP, MARCH = i("DOC_CASH"), i("FOLDER_OPS"), i("FOLDER_SWEEP"), i("SHEET_MARCH")
CONF = IDS["CONF_PAGE"]["id"]
HANDLES = "67cf1b506d78ad3c72e02a35"
ARTHUR_SUM = f"C07C2866011/{IDS['S_ARTHUR_SUM']['ts']}"
SW = {k[3:]: v["id"] for k, v in IDS.items() if k.startswith("SW_")}
IN_SCOPE = ["meta", "gads_569", "gads_449", "unity_ads", "applovin", "adjoe", "tiktok", "youtube", "linkedin", "x",
            "instagram", "discord", "admob"]

# Planned record text (seeded verbatim by /create-injection); quotes below are substrings of these.
PLANNED_TEXT = json.load(open(os.path.join(HERE, "planned_text.json")))


def q(key, quote):
    assert quote in PLANNED_TEXT[key], (key, quote)
    return quote


m = {
    "persona": "frederick_stone",
    "horizon": "Normal Horizon",
    "effective_profile": "normal",
    "requirements": {
        "R1": "register membership: exactly the in-scope marketing, UA, ad-monetization and social accounts from Arthur's Sep 30 sweep that have Fred on them",
        "R2": "company holders per account (Owner/Admin/Super admin on a person's harmonygames.co login)",
        "R3": "custody class per account (OUTSIDE ACCESS / SINGLE / COMPANY-HELD)",
        "R4": "money moving (Y/N) per account under Leonard's cash notes",
        "R5": "action per account (REVOKE / CLOSE / TRANSFER / KEEP) under the handover rules and their amendments",
        "R6": "reply to Leonard in the DM: how many accounts are marked TRANSFER and which outside party still has access",
        "R7": "register saved as a Google Sheet in the Company Ops folder",
        "R8": "social accounts that need a transfer added as a checklist on the existing social-handles card",
    },
    "services": {
        "slack": {"role": "hub (A1) in the Leonard-Frederick DM; Leonard's wrong admin claim; Unity/Meta campaign state; the Adjoe waiver reply; the superseded 90-day remark; write W3",
                  "weight_reason": "the ask, the reply destination and the Adjoe written waiver exist only in Slack (the waiver only in a thread reply)"},
        "trello": {"role": "authority H1 (handover rules card) + its amendment comment + same-board engineering decoy; the existing handles card (write W4)",
                   "weight_reason": "the holder definition, classes, action order and the socials exemption exist only on the card and its comment"},
        "gmail": {"role": "Arthur's Google Ads amendment; Meta receipts, AppLovin payouts, Google Ads account mails as money evidence",
                  "weight_reason": "the Harmony Games, Inc. Google Ads KEEP exception exists only in Arthur's email; September receipts/payouts decide money moving"},
        "gsheets": {"role": "the 15 per-platform user exports (sweep); Fred's stale March logins sheet; write W1",
                    "weight_reason": "who holds Owner/Admin on each account exists only in the per-platform exports"},
        "gdocs": {"role": "authority H2 (Leonard's cash notes)",
                  "weight_reason": "the definition of money moving, including the written-waiver and payout clauses, exists only in the doc"},
        "gdrive": {"role": "sweep folder (cohort container) and Company Ops folder (destination, write W2)",
                   "weight_reason": "which exports form the sweep and where the register must be saved"},
        "snowflake": {"role": "AD_REVENUE (ad revenue paid to us by network and month)",
                  "weight_reason": "AdMob's September money exists only as paid ad revenue in the warehouse"},
    "confluence": {"role": "superseded 2024 Company Accounts & Access page (decoy and oldest rules version)",
                       "weight_reason": "older one-owner-plus-backup rule the card replaces; a run that follows it misclassifies SINGLE accounts"},
    },
    "anchors": [
        {"id": "A1", "prompt_reference": "Leonard's account handover ask", "service": "slack", "locator": HUB,
         "requirement_ids": ["R6"]},
    ],
    "ask_fragments": [
        {"id": "K1", "service": "slack", "container": "D05S58U4SAK", "locator": HUB, "kind": "delegation",
         "incorporated_via": ["A1"], "seeded_ids": [IDS["S_HUB"]["id"]], "base_pointers": [], "delegated_by_record": HUB,
         "delegation_quote": q("S_HUB", "reply here with how many you've marked TRANSFER and anything an outsider still has access to"),
         "requirement_ids": ["R6"],
         "names_authorities": [{"id": "H1", "quote": q("S_HUB", "arthur's handover rules are on the ops board")}]},
        {"id": "K2", "service": "trello", "container": H1, "locator": f"trello:{H1} desc", "kind": "requirement",
         "incorporated_via": ["A1"], "seeded_ids": [H1, i("T_H1CREATE")], "base_pointers": [], "delegated_by_record": HUB,
         "delegation_quote": q("S_HUB", "arthur's handover rules are on the ops board, they decide the action"),
         "requirement_ids": ["R1", "R2", "R3", "R5"],
         "names_authorities": [{"id": "H2", "quote": q("H1_DESC", "Money moving is whatever Leonard defined it as for the cuts")}]},
        {"id": "K3", "service": "trello", "container": H1, "locator": f"trello:{CMT} (commentCard on {H1})", "kind": "amendment",
         "incorporated_via": ["A1", "K2"], "seeded_ids": [CMT], "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "For Fred's accounts before the cuts."),
         "requirement_ids": ["R5"], "supersedes": "K2 rule 5 for social accounts", "resolver": "newer comment by the card's author; the rest of the card stands"},
        {"id": "K4", "service": "gmail", "container": G_AMEND, "locator": G_AMEND, "kind": "amendment",
         "incorporated_via": ["A1", "K2"], "seeded_ids": [G_AMEND], "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "For Fred's accounts before the cuts."),
         "requirement_ids": ["R5"], "supersedes": "K2 rule 5 for the Harmony Games, Inc. Google Ads account", "resolver": "later email from the rules' author naming the account by customer ID"},
        {"id": "K5", "service": "gdocs", "container": DOC, "locator": f"gdocs:{DOC} section 'Money still moving'", "kind": "requirement",
         "incorporated_via": ["A1", "K2"], "seeded_ids": [DOC], "base_pointers": [], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "Money moving is whatever Leonard defined it as for the cuts"),
         "requirement_ids": ["R4"]},
        {"id": "K6", "service": "gdrive", "container": SWEEP, "locator": f"gdrive:{SWEEP}", "kind": "requirement",
         "incorporated_via": ["A1"], "seeded_ids": [SWEEP] + [SW[p] for p in SW], "base_pointers": [], "delegated_by_record": HUB,
         "delegation_quote": q("S_HUB", "arthur's sweep from today is the list"),
         "requirement_ids": ["R1", "R2"]},
        {"id": "K7", "service": "gdrive", "container": OPS, "locator": f"gdrive:{OPS}", "kind": "destination",
         "incorporated_via": ["A1"], "seeded_ids": [OPS], "base_pointers": [], "delegated_by_record": HUB,
         "delegation_quote": q("S_HUB", "save the register in the Company Ops folder"),
         "requirement_ids": ["R7"]},
        {"id": "K8", "service": "trello", "container": HANDLES, "locator": f"trello:{HANDLES}", "kind": "destination",
         "incorporated_via": ["A1", "K2"], "seeded_ids": [], "base_pointers": [f"trello:{HANDLES}"], "delegated_by_record": H1,
         "delegation_quote": q("H1_DESC", "Socials that need a transfer go as a checklist on Fred's"),
         "requirement_ids": ["R8"]},
    ],
    "authorities": [
        {"id": "H1", "name": "Arthur's account handover rules", "home_service": "trello", "decoy_service": "confluence",
         "governs": ["R1", "R2", "R3", "R5", "R8"], "findable_query": "account handover rules",
         "seeded_ids": [H1, CMT], "base_pointers": [], "decoy_seeded_ids": [ENG, CONF], "decoy_base_pointers": [],
         "decoy_scope": {"dimension": "team", "decoy": "engineering, store and data-tool accounts (Arthur's own list)",
                         "task": "marketing, UA, ad-monetization and social accounts that have Fred on them"}},
        {"id": "H2", "name": "Leonard's definition of money moving for the cuts", "home_service": "gdocs", "decoy_service": "slack",
         "governs": ["R4"], "findable_query": "money still moving cuts",
         "seeded_ids": [DOC], "base_pointers": [], "decoy_seeded_ids": [IDS["S_DECOY90"]["id"]], "decoy_base_pointers": []},
    ],
    "cohort": {
        "definition_source": "H1",
        "key": "platform user export in Arthur's Sep 30 sweep folder (one spreadsheet per account)",
        "size": 13,
        "evidence_surfaces": [
            {"service": "gsheets", "tool": "gsheets_values_get", "per_record_calls": 1.4, "records": 13, "seeded": True,
             "seeded_ids": [SW[p] for p in IN_SCOPE],
             "why_no_bulk": "one spreadsheet per platform export; gsheets_values_batch_get reads ranges of one spreadsheet only, gdrive_list_files returns names, not users or roles, and five exports keep partners, linked managers, removed users or invites on a second tab",
             "short_circuit": "holders that count are their own register column for every account and decide the class; Leonard's admin claim is wrong for three accounts, so no other record replaces the export",
             "requirement": "R2", "decides": "company holders"},
            {"service": "gmail", "tool": "gmail_search_messages", "per_record_calls": 1, "records": 7, "seeded": False,
             "why_no_bulk": "receipts, payouts and account mails come from a different sender per platform; no one query returns September money evidence for every account",
             "short_circuit": "money moving is its own Y/N column for every account and decides CLOSE against TRANSFER/KEEP independently of the holders",
             "requirement": "R4", "decides": "money moving (Y/N)"},
            {"service": "slack", "tool": "slack_conversations_replies", "per_record_calls": 0.5, "records": 10, "seeded": False,
             "why_no_bulk": "campaign on/off state and the Adjoe waiver live in the DM, #executives and the adjoe channel thread replies; channel history returns parents only",
             "short_circuit": "a switched-on campaign or a written waiver flips money moving whatever the receipts show",
             "requirement": "R4", "decides": "money moving (Y/N)"},
            {"service": "snowflake", "tool": "snowflake_execute_query", "per_record_calls": 0.3, "records": 13, "seeded": False,
             "why_no_bulk": "one GROUP BY returns paid revenue by network, but only for networks; the agent must map each account to its network row (admob, applovin, meta_audience, unity)",
             "short_circuit": "AdMob has no September money anywhere else; without the revenue row it reads N -> CLOSE",
             "requirement": "R4", "decides": "money moving (Y/N)"},
        ],
    },
    "chains": [
        {"id": "C1", "root_cause": "A1", "ends_in": "R5", "hops": [
            {"service": "slack", "record": ARTHUR_SUM, "finding": "Arthur: only YouTube and TikTok are on Fred alone, everything else has two of us"},
            {"service": "gsheets", "record": SW["unity_ads"], "finding": "Unity: Leonard is Manager; Arthur's Owner invite is pending"},
            {"service": "trello", "record": H1, "finding": "managers and pending invites don't count -> SINGLE -> TRANSFER (campaign on)"}]},
        {"id": "C2", "root_cause": "A9", "ends_in": "R4", "hops": [
            {"service": "slack", "record": "C07UCC631A6/1757346020.196019", "finding": "Adjoe campaign accidentally on from Sep 1 (thread parent)"},
            {"service": "slack", "record": "C07UCC631A6/1757349668.681539", "finding": "Adjoe rep confirms in a reply that we won't be charged"},
            {"service": "gdocs", "record": DOC, "finding": "a charge the vendor agreed in writing to drop doesn't count -> money N -> CLOSE"}]},
        {"id": "C3", "root_cause": "A13", "ends_in": "R5", "hops": [
            {"service": "trello", "record": H1, "finding": "no money moving -> CLOSE (both Google Ads accounts)"},
            {"service": "gmail", "record": G_AMEND, "finding": "reply on the rules: keep Harmony Games, Inc. 569-350-5790; Calm Play 449-481-1590 still follows the card"},
            {"service": "gsheets", "record": SW["gads_569"], "finding": "the export carrying 569-350-5790 is the Harmony Games, Inc. account"}]},
        {"id": "C5", "root_cause": "A19", "ends_in": "R4", "hops": [
            {"service": "trello", "record": H1, "finding": "money moving is whatever Leonard defined it as"},
            {"service": "gdocs", "record": DOC, "finding": "ad revenue paid to us counts; the warehouse has it by network and month"},
            {"service": "snowflake", "record": "ANALYTICS.MONETIZATION.AD_REVENUE", "finding": "admob September 2025 rows paid -> AdMob money Y -> KEEP"}]},
        {"id": "C4", "root_cause": "A17", "ends_in": "R1", "hops": [
            {"service": "gsheets", "record": MARCH, "finding": "March logins sheet lists AdMob, Singular and PlayableX; lacks the Calm Play Google Ads, X, Instagram, Discord"},
            {"service": "gdrive", "record": SWEEP, "finding": "Sep 30 sweep folder holds 15 exports"},
            {"service": "trello", "record": H1, "finding": "store and data-tool exports are out of scope; 12 accounts remain"}]},
    ],
    "traps": [
        {"id": "T1", "family": "superseding", "services": ["slack", "gsheets"], "seeded_ids": [IDS["S_CLAIM"]["id"], SW["unity_ads"], SW["meta"], SW["gads_449"]],
         "base_pointers": [], "requirement": "R2",
         "expected_wrong_reading": "counts Leonard as an admin holder on Meta, the Calm Play Google Ads and Unity",
         "resolver": "the Sep 30 exports, newer than the Sep 29 claim, list him as Advertiser, Standard and Manager",
         "discovery_order": "the claim sits in the same DM as the hub, a few messages above it",
         "version_records": [{"service": "slack", "id": IDS["S_CLAIM"]["id"], "seeded": True, "at": IDS["S_CLAIM"]["at"]},
                             {"service": "gsheets", "id": SW["unity_ads"], "seeded": True, "at": "2025-09-30T19:58:00Z"}]},
        {"id": "T2", "family": "superseding", "services": ["confluence", "trello", "gmail"], "seeded_ids": [CONF, H1, CMT, G_AMEND],
         "base_pointers": [], "requirement": "R5",
         "expected_wrong_reading": "applies the 2024 one-owner-plus-backup page, or the card alone (closes dormant socials and the Harmony Games, Inc. Google Ads)",
         "resolver": "card (replaces the page) -> comment (socials never CLOSE) -> Arthur's email (keep 569-350-5790); each keeps the rest",
         "discovery_order": "a Confluence search for accounts returns the 2024 page first; the comment and the email sit outside the card description",
         "version_records": [{"service": "confluence", "id": CONF, "seeded": True, "at": IDS["CONF_PAGE"]["at"]},
                             {"service": "trello", "id": i("T_H1CREATE"), "seeded": True, "at": IDS["T_H1CREATE"]["at"]},
                             {"service": "trello", "id": CMT, "seeded": True, "at": IDS["T_H1CMT"]["at"]},
                             {"service": "gmail", "id": G_AMEND, "seeded": True, "at": IDS["G_AMEND"]["at"]}]},
        {"id": "T3", "family": "superseding", "services": ["slack", "gdocs"], "seeded_ids": [IDS["S_DECOY90"]["id"], DOC],
         "base_pointers": [], "requirement": "R4",
         "expected_wrong_reading": "treats anything paid in the last 90 days as money still moving (Adjoe stays open)",
         "resolver": "Leonard's cash notes (newer, named in the hub) define September activity and drop written waivers",
         "discovery_order": "a Slack search for money/cuts hits the #executives remark before the doc",
         "version_records": [{"service": "slack", "id": IDS["S_DECOY90"]["id"], "seeded": True, "at": IDS["S_DECOY90"]["at"]},
                             {"service": "gdocs", "id": DOC, "seeded": True, "at": "2025-09-30T17:48:00Z"}]},
        {"id": "T4", "family": "distractor", "distractor_type": "partial_listing", "services": ["gsheets"], "seeded_ids": [MARCH],
         "base_pointers": [], "requirement": "R1",
         "expected_wrong_reading": "builds the register from Fred's March logins sheet (adds Singular, PlayableX and the old AdMob; misses the Calm Play Google Ads, X, Instagram, Discord)",
         "resolver": "the hub: arthur's sweep from today is the list (the March sheet predates it)"},
        {"id": "T5", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["trello"], "seeded_ids": [ENG],
         "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "uses the engineering card's one-owner-plus-break-glass rule and marks single-holder accounts KEEP",
         "resolver": "the engineering card is scoped to engineering, store and data-tool accounts; the marketing card governs Fred's"},
        {"id": "T6", "family": "exact_predicate", "services": ["gsheets", "slack"], "seeded_ids": [SW["unity_ads"], SW["youtube"], SW["tiktok"], SW["instagram"]],
         "base_pointers": ["slack:D05S58U4SAK/1759096868.688389", "slack:D05S58U4SAK/1759170013.491159"], "requirement": "R3",
         "expected_wrong_reading": "counts managers, pending invites, shared logins or a personal address as company holders (Unity, YouTube, TikTok, Instagram look COMPANY-HELD)",
         "resolver": "card rule 2 and 3: only Owner/Admin on a harmonygames.co login counts"},
        {"id": "T7", "family": "eliminating_evidence", "services": ["slack"], "seeded_ids": [],
         "base_pointers": ["slack:C07UCC631A6/1757346020.196019", "slack:C07UCC631A6/1757349668.681539"], "requirement": "R4",
         "expected_wrong_reading": "Adjoe ran in September, so money is moving and the account stays open",
         "resolver": "the rep's thread reply waives the cost in writing; the campaign was paused Sep 8",
         "discovery_order": "the channel history shows Leonard's complaint; the waiver is only in the thread replies"},
        {"id": "T8", "family": "entity_collision", "distractor_type": "lookalike_entity", "services": ["gsheets", "gmail"], "seeded_ids": [SW["gads_569"], SW["gads_449"]],
         "base_pointers": ["gmail:frederick.stone@harmonygames.co/1835153849970828373", "gmail:frederick.stone@harmonygames.co/1838369017520543217"],
         "requirement": "R5",
         "expected_wrong_reading": "treats Google Ads as one account, or keeps the Calm Play one and closes Harmony Games, Inc.",
         "resolver": "Arthur's email names Harmony Games, Inc. 569-350-5790; the exports carry both customer IDs",
         "discovery_order": "the March sheet and most Google mails name only 'Google Ads'"},
        {"id": "T9", "family": "tool_surface", "services": ["gsheets"], "seeded_ids": [SW["meta"]], "base_pointers": ["trello:670010236b89198587ca45b6"],
         "requirement": "R3",
         "expected_wrong_reading": "reads only the People block of the Meta export and classifies Meta SINGLE -> TRANSFER",
         "resolver": "the Partners block lower in the export: Node Media LLC still has partner admin on the ad account -> OUTSIDE ACCESS -> REVOKE"},
        {"id": "T10", "family": "scope_alias", "services": ["gsheets", "gmail"], "seeded_ids": [SW["play_console"], SW["app_store_connect"], SW["singular"]],
         "base_pointers": ["gmail:frederick.stone@harmonygames.co/1837038650805365569"], "requirement": "R1",
         "expected_wrong_reading": "adds Play Console, App Store Connect, Singular or ironSource/LevelPlay to the register",
         "resolver": "card rule 1: stores and data tools are on the engineering card; MAX-only bidders are not separate accounts"},
        {"id": "T11", "family": "reuse_exclusion", "services": ["trello"], "seeded_ids": [], "base_pointers": [f"trello:{HANDLES}"],
         "requirement": "R8",
         "expected_wrong_reading": "opens a new Trello card for the social transfers",
         "resolver": "card rule 7: checklist on Fred's existing 'Lock up social handles and domain?' card"},
        {"id": "T12", "family": "distractor", "distractor_type": "keyword_collision", "services": ["slack", "gmail"], "seeded_ids": [],
         "base_pointers": ["slack:C08H78VJG80/1759174925.309129", "gmail:frederick.stone@harmonygames.co/1840501641217286806"],
         "requirement": "R1",
         "expected_wrong_reading": "lists PlayableX (paused vendor project) or Balancy (prospect) as accounts",
         "resolver": "neither has an export in the sweep; they are vendor conversations, not accounts with Fred as a holder"},
        {"id": "T13", "family": "distractor", "distractor_type": "stale_summary", "services": ["slack"], "seeded_ids": [],
         "base_pointers": ["slack:C07C2866011/1759110509.707539", "slack:D05S58U4SAK/1759170013.491159"], "requirement": "R1",
         "expected_wrong_reading": "drops TikTok because Leonard said the account doesn't exist anymore",
         "resolver": "the same day's DM recovers it (tied to frederick.stone@harmonygames.co) and the sweep has a TikTok export"},
        {"id": "T14", "family": "stale_summary", "services": ["slack", "gsheets"], "seeded_ids": [IDS["S_ARTHUR_SUM"]["id"], SW["unity_ads"], SW["x"], SW["instagram"], SW["meta"]],
         "base_pointers": [], "requirement": "R3",
         "expected_wrong_reading": "takes Arthur's summary: only YouTube and TikTok SINGLE, everything else two holders",
         "resolver": "the exports under card rules 2-4: Unity (pending invite), X and Instagram are SINGLE; Meta has an outside partner",
         "discovery_order": "a #executives read or a 'sweep' search returns the summary before the exports"},
        {"id": "T15", "family": "entity_collision", "distractor_type": "lookalike_entity", "services": ["gmail", "slack", "gsheets"], "seeded_ids": [SW["admob"]],
         "base_pointers": ["gmail:frederick.stone@harmonygames.co/1841349862518331350", "slack:D05S58U4SAK/1756147086.813789"], "requirement": "R1",
         "expected_wrong_reading": "drops AdMob because 'Your AdMob account has been deactivated' (Aug 24)",
         "resolver": "that was pub-2341961509332343; Leonard's active AdMob account (Aug 25, D05S58U4SAK/1756147086.813789) is the one in the sweep"},
    ],
    "call_budget": [
        {"phase": "discovery", "service": "slack", "calls": 3, "reason": "the hub and the DM around it; #executives for the sweep and the Unity budget; find the adjoe channel"},
        {"phase": "discovery", "service": "trello", "calls": 3, "reason": "search for the handover rules; read the marketing card; read the engineering card the same search returns"},
        {"phase": "discovery", "service": "gdrive", "calls": 3, "reason": "find the sweep folder; list its 16 exports; find the Company Ops folder"},
        {"phase": "discovery", "service": "gdocs", "calls": 2, "reason": "find where Leonard defined money moving for the cuts; read the doc section"},
        {"phase": "discovery", "service": "gmail", "calls": 2, "reason": "search for replies on the handover rules; read Arthur's reply"},
        {"phase": "discovery", "service": "confluence", "calls": 1, "reason": "the accounts page the card says it replaces"},
        {"phase": "discovery", "service": "snowflake", "calls": 2, "reason": "find the ad revenue table; query paid revenue by network for September"},
        {"phase": "discovery", "service": "gsheets", "calls": 1, "reason": "Fred's March logins sheet (found by any 'logins' search)"},
        {"phase": "rules", "service": "trello", "calls": 1, "reason": "the card's comments (socials exemption)"},
        {"phase": "per-record", "service": "gsheets", "calls": 18, "reason": "one export per in-scope account (13) plus the second tab of five exports: Meta Partners, Google Ads 569 and 449 Linked managers, YouTube Removed users, Unity Invites (each needed to rule outside access or a holder in or out)"},
        {"phase": "per-record", "service": "gmail", "calls": 7, "reason": "September money evidence for the paid accounts: Meta receipts, AppLovin payouts, both Google Ads IDs, Adjoe invoices, Unity, AdMob"},
        {"phase": "per-record", "service": "slack", "calls": 5, "reason": "Unity campaigns on; Meta campaign off; Adjoe thread replies; YouTube and TikTok ownership"},
        {"phase": "per-record", "service": "trello", "calls": 1, "reason": "the old 'access shared with Node' card behind the Meta partner entry"},
        {"phase": "reads-before-writes", "service": "trello", "calls": 2, "reason": "find the handles card on the UA/BD board; check it has no checklist yet"},
        {"phase": "writes", "service": "gsheets", "calls": 3, "reason": "create the register; write its rows; read it back"},
        {"phase": "writes", "service": "gdrive", "calls": 1, "reason": "move the register into Company Ops"},
        {"phase": "writes", "service": "slack", "calls": 1, "reason": "reply to Leonard in the DM"},
        {"phase": "writes", "service": "trello", "calls": 5, "reason": "create the checklist on the handles card; one item per social transfer (4)"},
    ],
    "writes": [
        {"service": "gsheets", "tool": "gsheets_create_spreadsheet+gsheets_values_update", "count": 2,
         "depends_on": ["K2", "K3", "K4", "K5", "K6", "C1", "C2", "C3", "C4", "T6", "T9"], "requirements": ["R1", "R2", "R3", "R4", "R5"]},
        {"service": "gdrive", "tool": "gdrive_move_file", "count": 1, "depends_on": ["K7"], "requirements": ["R7"]},
        {"service": "slack", "tool": "slack_send_message", "count": 1, "depends_on": ["K1", "C1", "T6", "T9"], "requirements": ["R6"]},
        {"service": "trello", "tool": "trello_create_checklist+trello_create_check_item", "count": 5,
         "depends_on": ["K3", "K8", "T6", "T11"], "requirements": ["R8"]},
    ],
    "hazard_acknowledgements": [
        {"hazard_id": "Q08", "resolution": "excluded", "why_safe": "warehouse UA spend (AD_SPEND_DAILY) is neither modified nor cited; only AD_REVENUE paid rows are read, for AdMob, where no other record disagrees"},
        {"hazard_id": "Q09", "resolution": "excluded", "why_safe": "no mirrored warehouse table is modified or cited"},
        {"hazard_id": "S06", "resolution": "excluded", "why_safe": "Contacts job titles are neither modified nor cited"},
        {"hazard_id": "T07", "resolution": "excluded", "why_safe": "post-clock base records (Adjoe Oct 1 invoice, Google Ads 449 cancellation Oct 16) are not cited; the designed answers agree with them"},
    ],
    "denied_probes": [],
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(m, open(OUT, "w"), indent=1, ensure_ascii=False)
print("wrote", os.path.normpath(OUT))

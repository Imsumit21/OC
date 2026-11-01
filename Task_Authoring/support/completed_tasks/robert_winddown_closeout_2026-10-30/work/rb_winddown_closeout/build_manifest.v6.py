"""Writes task_inputs/Working_Files/01_Hardness_Manifest.draft.json from minted_ids.json / planned_text.json / accounts.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
M = json.load(open(os.path.join(HERE, 'minted_ids.json')))
T = json.load(open(os.path.join(HERE, 'planned_text.json')))
ACC = json.load(open(os.path.join(HERE, 'accounts.json')))
A, ADDED = ACC['accounts'], ACC['added']
issue = {a['vendor']: a for a in A}

WD = 'C0ADGSZKR3R'
ANCHOR_LOC = M['S_ANCHOR']['locator']
S = lambda k: M[k]['id']                       # slack message id (sha256(channel|ts)[:32])
G = lambda k: M[k]['robert_message']           # Robert's copy of a seeded mail
B = lambda ts: f"{WD}/{ts}"                    # base #winddown message

KEEP, ACTIONS, P_AND_L = B('1770933601.686309'), B('1770933903.645709'), B('1770933999.157259')
LLC, CR_SAID, CUR_SAID = B('1770937232.664809'), B('1770936655.574079'), B('1770937188.477219')
GUSTO_DOCS, SLACK_FREE, SLACK_FREE_OK = B('1770839729.441789'), B('1770839825.928989'), B('1770840054.486779')
CLOSE_CARD = B('1770927223.969899')
HS_1500 = B('1770673467.186629')
COSTS_TAB = 'f_605121f4a36752645e0ac3'
LEDGER = 'FINANCE.EXPENSES.FINANCE_LEDGER'
SING_THREAD = 'robert@harmonygames.co/1853470745017478863'
SING_DEC = 'robert@harmonygames.co/1850283027022457279'
IPOSTAL = 'robert@harmonygames.co/1854432461283937829'
TRELLO_ENDED = 'robert@harmonygames.co/1849420841999587093'
AWS_PAGE = 'page_aws_infra'
SUPPORT_PAGE = 'page_support_after_helpshift'

req = {
    "R1": "register membership: one row per vendor account — the Linear shutdown project's issues minus duplicates and "
          "the conventions doc's exclusions, plus every account still charging us in the ledger, sharing a costs-tab "
          "line, or on Sunset's list that the project lacks",
    "R2": "action per account (Cancel, Keep, Move to Arthur's LLC, Hold for Sunset)",
    "R3": "status for Cancel rows (Closed, Requested, Open)",
    "R4": "deadline per account",
    "R5": "owner per account",
    "R6": "monthly cost per account and the two monthly totals",
    "R7": "reply in Leonard's #winddown thread with the two monthly totals and the clashes with earlier decisions "
          "(Slack free plan, cutting Slack seats to guests, Google account archiving)",
    "R8": "register sheet shared with Leonard and Arthur as editors",
    "R9": "Linear issues settled: Done, Canceled or left open per the project description, a comment on each, and a new "
          "issue for each added account",
}

services = {
    "slack": {"role": "anchor A1 in #winddown (Leonard → Robert); base keep list, action items, Arthur's LLC-card move, the "
                      "Slack free-plan decision and the 'P&L covers everything' claim; Arthur's Gusto reply in the keep-list "
                      "thread; reply destination",
              "weight_reason": "the ask, the keep list and its amendment (Gusto → cancel), the LLC moves and both clashes "
                               "exist only in #winddown; the reply write lands there"},
    "gmail": {"role": "authority H1 (Sunset's data checklist + its in-thread correction); Sherwood decoy; vendor billing "
                      "mail through the billing group (next charge dates, Soundly's confirmation, Pond5/ElevenLabs receipts, "
                      "iPostal closure, Singular invoices and termination thread)",
              "weight_reason": "which accounts are held for Sunset, the next-charge dates behind most deadlines and the only "
                               "vendor confirmation for Soundly live only in Robert's mailbox"},
    "linear": {"role": "cohort: the 40 issues of the 'Shutdown – accounts' project; per-issue comments (status, owner "
                       "handover, billing notes); write targets (state, comment, 5 new issues)",
               "weight_reason": "membership starts from the project; per-issue comments decide status/owner/deadline for an "
                                "unpredictable subset; R9 writes"},
    "trello": {"role": "authority H2 'SVB card payoff + closure' on the founders' board; same-board Chase decoy",
               "weight_reason": "the Feb 19 card-move deadline for every Keep row and every Hold row that charges before the "
                                "review call exists only on that card"},
    "gdocs": {"role": "authority H3 'Close-out register conventions' in the Wind Down folder",
              "weight_reason": "exclusions, the ledger check, status vocabulary, deadline and cost rules and both totals"},
    "gdrive": {"role": "Wind Down folder holds the conventions doc; Arthur's superseded 'Subscriptions' sheet (decoy); "
                       "sharing write for the register",
               "weight_reason": "R8: the register must be shared with Leonard and Arthur as editors"},
    "gsheets": {"role": "January P&L 'HG Costs' tab (Dec-25 column) — cost source; 'Sound (Pond5, Soundly,Elevenlabs)' line; "
                        "register write",
                "weight_reason": "monthly cost for 15 rows comes from the tab (column AF); the shared Sound line hides two accounts"},
    "snowflake": {"role": "FINANCE_LEDGER Jan/Feb lines: meta and applovin UA charges (rule 3 membership, rule 8 cost for cloud/ad-spend accounts with their own ledger line: AWS, meta, applovin)",
                  "weight_reason": "Meta Ads and AppLovin (UA) are still charging and are absent from the P&L and the project; "
                                   "their monthly cost is their January ledger line"},
    "gcal": {"role": "'Sunset – data delivery review' (Mar 12, 2026) on Robert's calendar",
             "weight_reason": "the deadline for every Hold row that does not have to move cards"},
    "confluence": {"role": "'Support handover after Helpshift' page and its comment (export and switch-over logged); Growth/UA close-out conventions decoy page",
                   "weight_reason": "whether Helpshift still has an export pending before Feb 28 (its deadline) is only in the "
                                    "page comments"},
    "github": {"role": "CodeRabbit's subscription notice on Combo-Fighters#38",
               "weight_reason": "the only vendor confirmation that CodeRabbit is cancelled (Closed vs Requested)"},
}

anchors = [{"id": "A1", "prompt_reference": "Leonard's close-out register ask", "service": "slack", "locator": ANCHOR_LOC,
            "requirement_ids": ["R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"]}]


def frag(fid, service, container, locator, kind, via, delegated_by, quote, reqs, seeded=(), base=(), names=None):
    d = {"id": fid, "service": service, "container": container, "locator": locator, "kind": kind,
         "incorporated_via": via, "seeded_ids": list(seeded), "base_pointers": list(base),
         "delegated_by_record": delegated_by, "delegation_quote": quote, "requirement_ids": reqs}
    if names:
        d["names_authorities"] = names
    return d


frags = [
    frag("K2", "linear", "project Shutdown – accounts", M['L_PROJECT']['id'], "requirement", ["A1"], ANCHOR_LOC,
         "Arthur put every account into the Linear shutdown project last night", ["R1", "R9"],
         seeded=[M['L_PROJECT']['id']]),
    frag("K3", "gmail", "thread Harmony Games – data delivery checklist", G('G_SUNSET1'), "requirement", ["A1"], ANCHOR_LOC,
         "Sunset's data checklist", ["R2", "R7"], seeded=[G('G_SUNSET1')]),
    frag("K4", "gmail", "thread Harmony Games – data delivery checklist", G('G_SUNSET2'), "amendment", ["A1", "K3"],
         G('G_SUNSET1'), "If our engineers change anything on this list, we'll reply on this thread.", ["R2"],
         seeded=[G('G_SUNSET2')]),
    frag("K5", "gcal", "event Sunset – data delivery review", M['E_REVIEW']['robert_copy'], "requirement", ["A1", "K3"],
         G('G_SUNSET1'), "the delivery review call Leonard booked with us", ["R4"], seeded=[M['E_REVIEW']['robert_copy']]),
    frag("K6", "trello", "card SVB card payoff + closure", M['T_SVB']['id'], "requirement", ["A1"], ANCHOR_LOC,
         "SVB's card terms", ["R4"], seeded=[M['T_SVB']['id']]),
    frag("K7", "gdocs", "doc Close-out register conventions", M['DOC_CONV']['id'], "format", ["A1"], ANCHOR_LOC,
         "the conventions doc I just put in the Wind Down folder", ["R1", "R3", "R4", "R5", "R6"],
         seeded=[M['DOC_CONV']['id']]),
    frag("K8", "slack", WD, KEEP, "requirement", ["A1"], ANCHOR_LOC, "my keep list from last night", ["R2"], base=[KEEP]),
    frag("K9", "slack", f"{WD}/1770933601.686309 thread", M['S_GUSTO_REPLY']['locator'], "amendment", ["A1"], ANCHOR_LOC,
         "the replies under it", ["R2", "R4"], seeded=[S('S_GUSTO_REPLY')]),
    frag("K10", "slack", WD, LLC, "requirement", ["A1"], ANCHOR_LOC, "Arthur's moves to his LLC card", ["R2"], base=[LLC]),
    frag("K11", "gsheets", f"{COSTS_TAB} HG Costs", COSTS_TAB, "format", ["A1", "K7"], M['DOC_CONV']['id'],
         "the Dec-25 column of the costs tab in the January P&L", ["R6"], base=[COSTS_TAB]),
    frag("K12", "snowflake", LEDGER, LEDGER, "requirement", ["A1", "K7"], M['DOC_CONV']['id'],
         "anything else still charging us in the January and February lines of the finance ledger", ["R1", "R6"], base=[LEDGER]),
    frag("K13", "confluence", SUPPORT_PAGE, M['CONF_C1']['id'], "requirement", ["A1", "K3"], G('G_SUNSET1'),
         "Oliver said he'll log the export on your support handover page", ["R4"], seeded=[M['CONF_C1']['id']]),
]

authorities = [
    {"id": "H1", "name": "Sunset's data checklist", "home_service": "gmail", "decoy_service": "gmail",
     "governs": ["R2", "R7"], "findable_query": "data delivery checklist",
     "seeded_ids": [G('G_SUNSET1'), G('G_SUNSET2')], "base_pointers": [],
     "decoy_seeded_ids": [G('G_SHERWOOD')], "decoy_base_pointers": [],
     "decoy_scope": {"dimension": "issuer", "decoy": "Sherwood Partners (assignment-for-benefit-of-creditors firm, not engaged)",
                     "task": "Sunset (wind-down and data agreements signed Feb 12)"}},
    {"id": "H2", "name": "SVB's card terms", "home_service": "trello", "decoy_service": "trello",
     "governs": ["R4"], "findable_query": "SVB card",
     "seeded_ids": [M['T_SVB']['id']], "base_pointers": [],
     "decoy_seeded_ids": [M['T_CHASE']['id']], "decoy_base_pointers": [],
     "decoy_scope": {"dimension": "issuer", "decoy": "Chase (operating account closed Apr 2023)",
                     "task": "SVB (company card closing Feb 20 2026)"}},
    {"id": "H3", "name": "the close-out register conventions", "home_service": "gdocs", "decoy_service": "confluence",
     "governs": ["R1", "R3", "R6"], "findable_query": "close-out register conventions",
     "seeded_ids": [M['DOC_CONV']['id']], "base_pointers": [],
     "decoy_seeded_ids": [M['CONF_UA']['id']], "decoy_base_pointers": [],
     "decoy_scope": {"dimension": "team", "decoy": "Growth/UA team's UA vendor tracker (2025)",
                     "task": "founders' company close-out register (Feb 2026)"}},
]

cohort = {
    "definition_source": "K2 + H3",
    "key": "vendor account: an issue of the Linear project 'Shutdown – accounts' (46) or an account the project lacks that "
           "still charges us in the Jan/Feb ledger, shares a costs-tab line, or is on Sunset's corrected list (5)",
    "size": 51,
    "evidence_surfaces": [
        {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1, "records": 47, "seeded": True,
         "seeded_ids": [c for a in A for c in a['comment_ids']],
         "why_no_bulk": "linear_list_issues returns description, state and assignee but no comments; there is no "
                        "workspace-wide comment listing, so each issue's comments take their own call",
         "short_circuit": "a decisive comment sits on an unpredictable 59% of issues (27 of 46: handovers, never-paid notes, "
                          "LLC moves, 'nothing back yet') and neutral notes on others; neither the description nor the "
                          "state tells which, and the status, owner and exclusion columns are written per issue whatever "
                          "the other surfaces say",
         "requirement": "R3", "decides": "status for Cancel rows"},
        {"service": "gmail", "tool": "gmail_search_messages + gmail_get_message", "per_record_calls": 1, "records": 9,
         "seeded": True, "seeded_ids": [G(k) for k in ('G_LINEAR', 'G_FIGMA', 'G_LAYER', 'G_POND5', 'G_UNITY', 'G_SOUNDLY')],
         "why_no_bulk": "billing mail is spread over 16,000 threads in Robert's mailbox from a dozen tokenised senders; "
                        "a search snippet does not carry the next-charge date or the card, so each vendor's latest "
                        "receipt has to be found by name and opened",
         "short_circuit": "the next charge date decides the deadline of every Cancel row that is not Closed and whether a "
                          "Hold row must move cards; no Linear comment or Slack message carries those dates for these 9 "
                          "accounts",
         "requirement": "R4", "decides": "deadline per account"},
        {"service": "gsheets", "tool": "gsheets_values_get (HG Costs)", "per_record_calls": 0.05, "records": 51,
         "seeded": False,
         "why_no_bulk": "one read returns the tab, but the tab carries no row for the #winddown-only and added accounts, its header dates are a year off (Dec-25 is column AF) and one "
                        "line for three sound accounts; the per-account cost has to be matched row by row against the "
                        "conventions' fallbacks",
         "short_circuit": "the cost column is its own output for every row and feeds both totals; no other surface states "
                          "the Dec-25 figure",
         "requirement": "R6", "decides": "monthly cost per account"},
    ],
}

H = lambda svc, rec, finding: {"service": svc, "record": rec, "finding": finding}
chains = [
    {"id": "C1", "root_cause": "A1", "ends_in": "R1", "hops": [
        H("slack", P_AND_L, "Leonard: 'I looked at the P&L and I think this covers everything'"),
        H("linear", M['L_PROJECT']['id'], "Arthur's project: one issue per vendor from the P&L and the lists (Soundly only)"),
        H("gsheets", COSTS_TAB, "costs tab line 'Sound (Pond5, Soundly,Elevenlabs)' = three accounts"),
        H("gmail", G('G_POND5'), "Pond5 renews Mar 2 on the SVB card; ElevenLabs is prepaid to Jul 9 2026 (base receipt robert@harmonygames.co/1837122624854744558)")]},
    {"id": "C2", "root_cause": "A13", "ends_in": "R1", "hops": [
        H("gdocs", M['DOC_CONV']['id'], "rule 3: check the Jan/Feb ledger lines for anything still charging"),
        H("snowflake", "FIN-000689", "meta marketing_ua -2,843.84 (Jan) and -956.45 (Feb 13); applovin -9.80/-9.83"),
        H("linear", M['L_PROJECT']['id'], "no Meta Ads or AppLovin issue in the project"),
        H("gsheets", COSTS_TAB, "the UA line (610 in Dec-25, column AF) is one line for two ad accounts")]},
    {"id": "C3", "root_cause": "A14", "ends_in": "R2", "hops": [
        H("gmail", G('G_SUNSET1'), "hold list: Slack, Google Workspace, Figma, Linear, GitHub, Confluence, Metabase"),
        H("gmail", G('G_SUNSET2'), "in-thread correction: Trello in, Metabase out, BigQuery and dbt in"),
        H("linear", issue['Metabase']['issue'], "Metabase billing already on the KubLLC card → Move, not Hold"),
        H("slack", LLC, "Arthur moves Metabase to his KubLLC card")]},
    {"id": "C4", "root_cause": "A12", "ends_in": "R4", "hops": [
        H("slack", CLOSE_CARD, "'pay SVB fully and close the credit card' — no date"),
        H("trello", M['T_SVB']['id'], "card closes Feb 20; anything kept that charges again must move by Feb 19"),
        H("linear", issue['Slack']['comment_ids'][0], "Slack renews on the 3rd and Google Cloud charges on the 1st, both on the SVB card — before the Mar 12 review"),
        H("gcal", M['E_REVIEW']['robert_copy'], "review call Mar 12 — holds that need no move stay until then")]},
    {"id": "C5", "root_cause": "A15", "ends_in": "R3", "hops": [
        H("gdocs", M['DOC_CONV']['id'], "rule 5: Closed only when the vendor itself confirmed"),
        H("slack", CR_SAID, "Arthur: 'coderabbit is cancelled'; 'cursor and … cancelled'"),
        H("github", M['GH_CR']['id'], "CodeRabbit's own notice: subscription canceled Feb 12 → Closed"),
        H("linear", issue['Cursor']['comment_ids'][0], "Cursor: cancelled in the dashboard, no vendor word → Requested, renews the 5th")]},
    {"id": "C6", "root_cause": "A16", "ends_in": "R7", "hops": [
        H("slack", SLACK_FREE_OK, "Arthur: 'yeah free version' (Slack downgrade)"),
        H("slack", ACTIONS, "Leonard to archive the Google accounts after Feb 15"),
        H("slack", B('1770842405.931359'), "Leonard: keep only the three founders as paid Slack accounts, the rest as guests"),
        H("gmail", G('G_SUNSET1'), "keep Slack on the paid plan; don't archive or delete any Google account"),
        H("gcal", M['E_REVIEW']['robert_copy'], "no closing, downgrading or archiving before Mar 12")]},
    {"id": "C7", "root_cause": "A19", "ends_in": "R6", "hops": [
        H("gsheets", COSTS_TAB, "Dec-25 costs (column AF; the header dates are a year off) e.g. Unity 2,172, Workspace 316.56"),
        H("snowflake", "FIN-000687", "AWS 1,485 (Jan), Meta 2,843.84, AppLovin 9.80"),
        H("gmail", G('G_FIGMA'), "annual/quarterly charges brought to a month (Figma 1,212/12, Singular 6,250/3)"),
        H("gdocs", M['DOC_CONV']['id'], "two totals: all rows today, Keep + Hold after the plan")]},
]


def vr(svc, ref, seeded, at, base=False):
    d = {"service": svc, "seeded": seeded, "at": at}
    d["base_pointer" if base else "id"] = ref
    return d


traps = [
    {"id": "T1", "family": "superseding", "services": ["slack"], "seeded_ids": [S('S_GUSTO_REPLY')],
     "base_pointers": [GUSTO_DOCS, KEEP], "requirement": "R2",
     "expected_wrong_reading": "keeps Gusto through the shutdown (Leonard's keep list) with a Feb 19 card move",
     "resolver": "Arthur's reply in the keep-list thread: docs pulled, renews Mar 1, cancel before the 1st → Cancel, Open, Feb 28",
     "discovery_order": "the keep list is a top-level #winddown message every run reads; the reply only shows as reply_count 1",
     "version_records": [vr("slack", GUSTO_DOCS, False, "2026-02-11T20:02:09Z", True),
                         vr("slack", KEEP, False, "2026-02-12T22:00:01Z", True),
                         vr("slack", S('S_GUSTO_REPLY'), True, M['S_GUSTO_REPLY']['at'])]},
    {"id": "T2", "family": "superseding", "services": ["slack", "gmail"], "seeded_ids": [G('G_SUNSET1')],
     "base_pointers": [SLACK_FREE, SLACK_FREE_OK], "requirement": "R7",
     "expected_wrong_reading": "plans the Slack downgrade to free (agreed Feb 11) without flagging it",
     "resolver": "Sunset's checklist (Feb 12 23:58Z) requires the paid plan with full history and every user in place until the review; the reply must name the downgrade and the cut to guest seats (C0ADGSZKR3R/1770842405.931359)",
     "discovery_order": "the downgrade agreement sits in the #winddown history the anchor points at; the checklist is in Gmail",
     "version_records": [vr("slack", SLACK_FREE, False, "2026-02-11T20:03:45Z", True),
                         vr("slack", SLACK_FREE_OK, False, "2026-02-11T20:07:34Z", True),
                         vr("gmail", G('G_SUNSET1'), True, M['G_SUNSET1']['at'])]},
    {"id": "T3", "family": "superseding", "services": ["slack", "gmail"], "seeded_ids": [G('G_SUNSET1')],
     "base_pointers": [ACTIONS], "requirement": "R2",
     "expected_wrong_reading": "puts Google Workspace down for archiving after Feb 15 (Leonard's action item)",
     "resolver": "Sunset: don't archive or delete any Google account before the review → Hold for Sunset; the archive plan is a clash to report",
     "version_records": [vr("slack", ACTIONS, False, "2026-02-12T22:05:03Z", True),
                         vr("gmail", G('G_SUNSET1'), True, M['G_SUNSET1']['at'])]},
    {"id": "T4", "family": "superseding", "services": ["slack", "gmail"], "seeded_ids": [G('G_SUNSET1'), G('G_SUNSET2')],
     "base_pointers": [LLC], "requirement": "R2",
     "expected_wrong_reading": "holds Metabase for Sunset (first checklist) or leaves its card move open",
     "resolver": "the in-thread correction takes Metabase off the list; Arthur's issue comment confirms the KubLLC card → Move, dash",
     "discovery_order": "the first checklist names Metabase; the correction is the second message of the same thread",
     "version_records": [vr("slack", LLC, False, "2026-02-12T23:00:32Z", True),
                         vr("gmail", G('G_SUNSET1'), True, M['G_SUNSET1']['at']),
                         vr("gmail", G('G_SUNSET2'), True, M['G_SUNSET2']['at'])]},
    {"id": "T5", "family": "conclusion_stop", "services": ["gmail"], "seeded_ids": [G('G_SUNSET2')], "base_pointers": [],
     "requirement": "R2",
     "expected_wrong_reading": "stops at the first checklist: cancels Trello (paid plan ended Nov 2025), dbt and BigQuery",
     "resolver": "the correction adds Trello, BigQuery and dbt → Hold for Sunset (Trello despite its pre-Feb-9 downgrade)"},
    {"id": "T6", "family": "stale_summary", "services": ["slack", "linear"], "seeded_ids": [M['L_PROJECT']['id']],
     "base_pointers": [P_AND_L], "requirement": "R1",
     "expected_wrong_reading": "treats Arthur's 40 issues as the complete account list",
     "resolver": "conventions rule 3 (ledger lines, shared costs-tab lines) and Sunset's list add Pond5, ElevenLabs, Meta Ads, AppLovin (UA) and Confluence",
     "discovery_order": "Leonard's 'covers everything' and the project are met before the ledger or the costs tab"},
    {"id": "T7", "family": "scope_alias", "services": ["gsheets", "gmail"], "seeded_ids": [G('G_POND5')],
     "base_pointers": [COSTS_TAB], "requirement": "R1",
     "expected_wrong_reading": "one Sound row (or Soundly at $15) because the tab has one line",
     "resolver": "rule 1 + rule 8: one row per vendor account, each at its own charge — Soundly 10, Pond5 60/12, ElevenLabs 50/12 (prepaid to Jul 9)"},
    {"id": "T8", "family": "eliminating_evidence", "services": ["snowflake"], "seeded_ids": [],
     "base_pointers": ["FIN-000688", "FIN-000689", "FIN-000699", "FIN-000700"], "requirement": "R1",
     "expected_wrong_reading": "no UA account on the register (no issue for it, Frederick left in October)",
     "resolver": "ledger marketing_ua rows in Jan and Feb: meta and applovin are still charging → two Cancel rows, usage-billed → Feb 28"},
    {"id": "T9", "family": "authority", "services": ["trello", "slack"], "seeded_ids": [M['T_SVB']['id'], M['T_CHASE']['id']],
     "base_pointers": [CLOSE_CARD], "requirement": "R4",
     "expected_wrong_reading": "no card deadline (Slack never dates the closure) or Chase's Apr 25 cut-over",
     "resolver": "SVB card on the founders' board: closes Feb 20, move kept charging accounts by Feb 19",
     "discovery_order": "a board search for 'card' returns the Chase closure card in Done next to the SVB card in To Do"},
    {"id": "T10", "family": "authority", "services": ["gmail"], "seeded_ids": [G('G_SUNSET1'), G('G_SHERWOOD')],
     "base_pointers": [], "requirement": "R2",
     "expected_wrong_reading": "applies Sherwood's 'cancel every subscription now except payroll and accounting'",
     "resolver": "Sunset is the provider signed on Feb 12 (#winddown 1770931777.561519); Sherwood was not engaged",
     "discovery_order": "a mailbox search for 'checklist' returns Sherwood's (Feb 11) before Sunset's (Feb 12) in date order"},
    {"id": "T11", "family": "authority", "services": ["gdocs", "confluence"], "seeded_ids": [M['DOC_CONV']['id'], M['CONF_UA']['id']],
     "base_pointers": [], "requirement": "R6",
     "expected_wrong_reading": "costs Meta Ads at trailing 30-day spend or treats it closed once spend reads $0",
     "resolver": "the conventions doc governs the founders' register: last full month (January) from the ledger"},
    {"id": "T12", "family": "reuse_exclusion", "services": ["linear", "gmail"], "seeded_ids": [issue['QuickBooks']['comment_ids'][0]],
     "base_pointers": [], "requirement": "R1",
     "expected_wrong_reading": "two rows (QuickBooks and Intuit) or Canceled on the older issue",
     "resolver": "rule 1: one row 'Intuit QuickBooks' (invoice name); ENG-2461 (newer) is the duplicate → Canceled"},
    {"id": "T13", "family": "near_miss_mention", "services": ["slack", "github", "gmail"],
     "seeded_ids": [M['GH_CR']['id'], issue['Cursor']['comment_ids'][0]], "base_pointers": [CR_SAID, CUR_SAID], "requirement": "R3",
     "expected_wrong_reading": "Closed for CodeRabbit and Cursor because Arthur said they're cancelled (and Done in Linear)",
     "resolver": "rule 5: CodeRabbit's own notice on Combo-Fighters#38 (canceled Feb 12) → Closed; Cursor has no vendor word → Requested, Mar 4",
     "discovery_order": "Arthur's 'cancelled' messages are in the #winddown history; the bot notice is on a PR"},
    {"id": "T14", "family": "cross_reference_gap", "services": ["gcal", "gmail"],
     "seeded_ids": [M['E_REVIEW']['robert_copy'], G('G_SUNSET1')], "base_pointers": [], "requirement": "R4",
     "expected_wrong_reading": "Hold rows with no date, Feb 15, or 'until Sunset confirms'",
     "resolver": "the review call Leonard booked is on Robert's calendar for 2026-03-12 → deadline for Linear, Figma, Trello, GitHub, Confluence"},
    {"id": "T15", "family": "synthesis_omission", "services": ["confluence", "gmail"],
     "seeded_ids": [M['CONF_C1']['id'], M['CONF_C2']['id']], "base_pointers": [], "requirement": "R4",
     "expected_wrong_reading": "Helpshift deadline Feb 27 (export still pending) or no export check at all",
     "resolver": "Oliver's comment on the support handover page: export done and buttons switched Feb 13 → Closed row gets a dash"},
    {"id": "T16", "family": "unit_or_timezone", "services": ["gmail", "gsheets"],
     "seeded_ids": [G('G_FIGMA'), G('G_POND5'), issue['Docusign']['comment_ids'][0]], "base_pointers": [SING_DEC, COSTS_TAB], "requirement": "R6",
     "expected_wrong_reading": "Singular at 6,250 or 0, Figma at 0 or 1,212, Carta/Docusign/Linear at their annual price",
     "resolver": "rule 8: quarterly ÷ 3 (2,083.33), annual ÷ 12 (Figma 101, Carta 321, Linear 40, Docusign 25, Pond5 5, ElevenLabs 4.17); GitHub at its last invoice 90"},
    {"id": "T17", "family": "exact_predicate", "services": ["linear", "gsheets", "gmail"],
     "seeded_ids": [M['L_PROJECT']['id'], M['DOC_CONV']['id']], "base_pointers": [TRELLO_ENDED, IPOSTAL], "requirement": "R1",
     "expected_wrong_reading": "keeps never-paid, one-off or pre-Feb-9 accounts, or drops Trello for its Nov 2025 downgrade",
     "resolver": "rule 2 exclusions (21 issues → Canceled) with the Sunset exception (Trello stays as a Hold)"},
    {"id": "T18", "family": "superseding", "services": ["linear"],
     "seeded_ids": [issue['Docusign']['issue'], issue['Docusign']['comment_ids'][0]], "base_pointers": [], "requirement": "R5",
     "expected_wrong_reading": "Leonard as Docusign's owner (the assignee)",
     "resolver": "Leonard's comment hands Docusign to Robert (rule 7)",
     "version_records": [vr("linear", issue['Docusign']['issue'], True, issue['Docusign']['created']),
                         vr("linear", issue['Docusign']['comment_ids'][0], True, issue['Docusign']['comments'][0][1])]},
    {"id": "T19", "family": "distractor", "distractor_type": "already_done", "services": ["gsheets", "gmail"],
     "seeded_ids": [], "base_pointers": [COSTS_TAB, IPOSTAL], "requirement": "R1",
     "expected_wrong_reading": "iPostal as a Cancel row at $34.79 (Dec-25 on the tab)",
     "resolver": "iPostal1 closed the mailbox on Jan 16 (Robert's mail) → cancelled before Feb 9 → excluded"},
    {"id": "T20", "family": "distractor", "distractor_type": "partial_listing", "services": ["gsheets"],
     "seeded_ids": [M['SHEET_SUBS']['id']], "base_pointers": [], "requirement": "R1",
     "expected_wrong_reading": "uses Arthur's 18-row 'Subscriptions' sheet (rounded figures) as the list",
     "resolver": "the project description says it replaces that sheet"},
    {"id": "T21", "family": "distractor", "distractor_type": "non_authoritative_instruction", "services": ["slack"],
     "seeded_ids": [S('S_OLIVER_CURSOR')], "base_pointers": [], "requirement": "R2",
     "expected_wrong_reading": "keeps Cursor for Oliver",
     "resolver": "Oliver asks; the founders cancelled it (Feb 11 list, Arthur Feb 12) → Cancel"},
    {"id": "T22", "family": "distractor", "distractor_type": "scope_adjacent", "services": ["gmail"],
     "seeded_ids": [], "base_pointers": [SING_THREAD, SING_DEC], "requirement": "R4",
     "expected_wrong_reading": "Singular deadline Mar 14 (the past-due extension to Mar 15)",
     "resolver": "Mar 15 is the due date of the overdue balance; the next quarterly invoice is Mar 1 (Sep 1, Dec 1) → Feb 28"},
    {"id": "T23", "family": "distractor", "distractor_type": "keyword_collision", "services": ["slack"],
     "seeded_ids": [], "base_pointers": [HS_1500], "requirement": "R6",
     "expected_wrong_reading": "Helpshift at $1,500 / $300 (balances owed) instead of its monthly 150",
     "resolver": "rule 8: Dec-25 column = 150"},
    {"id": "T24", "family": "distractor", "distractor_type": "stale_summary", "services": ["confluence", "snowflake"],
     "seeded_ids": [], "base_pointers": [AWS_PAGE, "FIN-000687"], "requirement": "R6",
     "expected_wrong_reading": "AWS at ~$1,550 (page) or ~$1k (Arthur's DD prod estimate) or 0 (tab)",
     "resolver": "rule 8: a cloud account with its own ledger line takes its January line (FIN-000687, 1,485), whatever the tab shows; Arthur's issue comment gives the same 1,485"},
]

budget = [
    {"phase": "discovery", "service": "slack", "calls": 4, "reason": "read the ask and the #winddown history it points at (2 pages), the keep-list thread replies, one search for Arthur's LLC message"},
    {"phase": "discovery", "service": "linear", "calls": 3, "reason": "find the 'Shutdown – accounts' project, read its description, list its 46 issues"},
    {"phase": "rules", "service": "gmail", "calls": 3, "reason": "search for Sunset's checklist, read the thread (checklist + correction), search for SVB's terms (none in mail)"},
    {"phase": "rules", "service": "trello", "calls": 3, "reason": "search the boards for the SVB terms, open the card, read its description"},
    {"phase": "rules", "service": "gdocs", "calls": 2, "reason": "find and read the conventions doc"},
    {"phase": "rules", "service": "gdrive", "calls": 1, "reason": "search Drive for the doc Leonard named by title (the Wind Down folder itself is not shared; its files are)"},
    {"phase": "rules", "service": "gcal", "calls": 2, "reason": "find the review call Sunset's mail refers to and read its date"},
    {"phase": "rules", "service": "confluence", "calls": 3, "reason": "find the support handover page, read it, list its comments for the Helpshift export"},
    {"phase": "enumeration", "service": "gsheets", "calls": 2, "reason": "find the January P&L and read the HG Costs tab"},
    {"phase": "enumeration", "service": "snowflake", "calls": 3, "reason": "find FINANCE_LEDGER, read its columns, query the Jan/Feb lines"},
    {"phase": "per-record", "service": "linear", "calls": 46, "reason": "linear_list_comments on each of the 46 issues: a decisive comment sits on an unpredictable 27 of them"},
    {"phase": "per-record", "service": "gmail", "calls": 9, "reason": "the billing mail in Robert's own mailbox: Figma, Layer, Pond5, Linear, Soundly, Unity, ElevenLabs, Singular, iPostal (the other accounts' billing facts are in their Linear comments)"},
    {"phase": "per-record", "service": "linear", "calls": 71, "reason": "settle each issue: 25 state changes (5 Done, 20 Canceled) and one comment on each of the 46"},
    {"phase": "reconciliation", "service": "github", "calls": 2, "reason": "look for CodeRabbit's own word (search PR comments by the bot, read #38's comments)"},
    {"phase": "reads-before-writes", "service": "linear", "calls": 2, "reason": "workflow state ids and the project id needed by the writes"},
    {"phase": "writes", "service": "gsheets", "calls": 2, "reason": "create the register and write its 31 rows and two totals"},
    {"phase": "writes", "service": "gdrive", "calls": 2, "reason": "share the register with Leonard and with Arthur as editors"},
    {"phase": "writes", "service": "linear", "calls": 5, "reason": "a new issue in the project for each added account"},
    {"phase": "writes", "service": "slack", "calls": 1, "reason": "reply in Leonard's thread with the totals and the clashes"},
]

writes = [
    {"service": "gsheets", "tool": "gsheets_create_spreadsheet + gsheets_values_update", "count": 2,
     "depends_on": ["K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9", "K10", "K11", "K12", "C1", "C2", "C3", "C4", "C5", "C7",
                    "T1", "T5", "T6", "T7", "T8", "T12", "T13", "T14", "T15", "T16", "T17"],
     "requirements": ["R1", "R2", "R3", "R4", "R5", "R6"]},
    {"service": "gdrive", "tool": "gdrive_share_file", "count": 2, "depends_on": ["A1"], "requirements": ["R8"]},
    {"service": "linear", "tool": "linear_update_issue + linear_create_comment", "count": 71,
     "depends_on": ["K2", "K7", "T12", "T13", "T17", "C5"], "requirements": ["R9"]},
    {"service": "linear", "tool": "linear_create_issue", "count": 5, "depends_on": ["C1", "C2", "T6", "T7", "T8"],
     "requirements": ["R9", "R1"]},
    {"service": "slack", "tool": "slack_post_message (thread reply)", "count": 1, "depends_on": ["C6", "C7", "T2", "T3"],
     "requirements": ["R7"]},
]

hazards = [
    {"hazard_id": "L13", "resolution": "excluded", "why_safe": "Combo-Fighters#37 and its CodeRabbit comment #37#c_1 are neither modified nor cited; the CodeRabbit notice is seeded on a new PR #38"},
    {"hazard_id": "Q07", "resolution": "excluded", "why_safe": "the Helpshift balance messages are cited only as a distractor (balances owed); the register cost is the costs-tab figure 150; no seeded row restates a balance", "requirement": "R6"},
    {"hazard_id": "Q01", "resolution": "excluded", "why_safe": "the seeded Gusto reply's parent (1770933601.686309) gets reply_count 1, reply_users 1 and latest_reply = the reply in its UPDATE companion; no Q01 example record is touched"},
    {"hazard_id": "R04", "resolution": "excluded", "why_safe": "seeded text names the Wind Down folder by title only, never by the native folder id"},
]

manifest = {
    "persona": "robert",
    "horizon": "Long Horizon",
    "effective_profile": "long",
    "profile_exception": {
        "reason": "author target: more than 150 tool calls in every baseline run and an average under 80% "
                  "(00_Assigments.md 'Author targets'); the extreme profile's ~600-call design would overshoot the band "
                  "several times over, so the long profile keeps the extreme breadth, authorities, chains and traps with a "
                  "~@@BUDGET@@-call necessary budget sized so the leanest correct run still clears 150",
        "requester_confirmation": "task author in chat on 2026-10-28: 'make sure my task is a long-horizon task so i want "
                                  "minimum above 150 tool calls in each also i want difficulty under 80%'; recorded in "
                                  "task_inputs/00_Assigments.md ('Author targets')"},
    "requirements": req, "services": services, "anchors": anchors, "ask_fragments": frags, "authorities": authorities,
    "cohort": cohort, "chains": chains, "traps": traps, "call_budget": budget, "writes": writes,
    "hazard_acknowledgements": hazards, "denied_probes": [],
    "integration_exceptions": [
        {"record_id": M['E_REVIEW']['ical_uid'], "reason": "no_notify: Leonard created the review call without sending invitation mails, so no Invitation: mail carries its date"},
    ],
}
dst = os.path.join(BUNDLE, 'task_inputs', 'Working_Files', '01_Hardness_Manifest.draft.json')
tot = sum(b['calls'] for b in budget)
manifest['profile_exception']['reason'] = manifest['profile_exception']['reason'].replace('@@BUDGET@@', str(tot))
json.dump(manifest, open(dst, 'w'), indent=1, ensure_ascii=False)
print('wrote', dst, 'budget', sum(b['calls'] for b in budget))

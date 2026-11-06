#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Writing_Brief.md (brief mode) from the SQL ids, the cohort, the solver truth, the
persona searches (plan/brief_searches.json/.txt) and the entity output (plan/brief_entity.txt). Facts and locators only;
no rubric or OE text. Re-run after any SQL / truth change, then the stage gate."""
import importlib.util, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
S = json.load(open(os.path.join(HERE, "sql_ids.json")))
I = json.load(open(os.path.join(HERE, "ids.json")))
IDS, BASE, T = I["IDS"], I["BASE"], I["T"]
C = json.load(open(os.path.join(HERE, "cohort.json")))
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
spec = importlib.util.spec_from_file_location("solver_mod", os.path.join(WF, "solver", "solver.py"))
SOLV = importlib.util.module_from_spec(spec)
spec.loader.exec_module(SOLV)
TOT = SOLV.aggregates(TRUTH)["totals"]
SRCH = json.load(open(os.path.join(HERE, "brief_searches.json")))
ROB, LEO, ART = "robert@harmonygames.co", "leonard.hayes@harmonygames.co", "arthur.blake@harmonygames.co"
SL = {k: v["locator"] for k, v in S["slack"].items()}
GM = {k: v[ROB]["message"] for k, v in S["gmail"].items() if ROB in v}
GT = {k: v[ROB]["thread"] for k, v in S["gmail"].items() if ROB in v}
LN = S["linear"]
EV = S["gcal"][ROB]
HUB_TS = SL["hub"].split("/")[1]


def rd(n):
    p = os.path.join(HERE, n)
    return open(p).read().rstrip() if os.path.exists(p) else f"({n} missing)"


L = []
A = L.append


def table(head, rows):
    A("| " + " | ".join(head) + " |")
    A("|" + "---|" * len(head))
    for r in rows:
        A("| " + " | ".join(str(c).replace("|", "/") for c in r) + " |")
    A("")


A("# Prompt Brief — robert_llc_takeover · prep")
A(f"> Built 2026-11-06 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Grounding_Dossier.md (injection rev4, SQL sha256 f1a290ced176 with the layer.ai reply fix; rev3 passed the platform /injection and /prompt reviews, "
  f"then failed /hardness at 2 on its Opus pre-check; rev4 moves four corrections off the swept path, Working_Files/01a_Hardening_Report.md and 01_Scenario_Design.md §14"
  f"), 01_Universe_Inject.sql, 03_Error_Async_Config.txt (Friction: none), 01_Scenario_Design.md, 01_Hardness_Manifest.json "
  f"· Persona view verified: all (check-sql PASS on every seeded load-bearing record; base records by persona_view search, §5a) · Clock: 2026-02-14 00:00 UTC, "
  f"Feb 14, 2026 (normal) · Robert's today: Saturday Feb 14, 2026.")
A("> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human. The rev3 prompt (sha256 ccd229a59a17) is unchanged for rev4: "
  "the hardening report found no prompt-side defect (RULE_IN_PROMPT CLEAN). No 02_Reference_Files_Manifest.md (no attachment).")
A("")

# ---------------------------------------------------------------- 1
A("## 1 · Assignment fit")
A("")
table(["Axis", "Assigned value", "What it requires here (cited)"], [
    ["Business function", "Executive", "Founders / Exec / Strategy in `Evals/references/rules/task_categories.md` (strategic decisions, executive coordination). "
     "The work also sits in Finance / Legal / HR / Ops (the competency): a founders' decision on what the new LLC takes, its three-month running cost and each founder's share."],
    ["Persona", "Robert · robert@harmonygames.co · Co-founder & Creative Director (roster.json persona_key robert, department Executive)",
     "Voice: short, plain, first person to his assistant, lower-key than Leonard (base posts e.g. C09UHHN6PFZ/1770865575.541589 'Daily challenges has 14 levels now'). "
     "Remit: one of three founders running the wind-down in #winddown (C0ADGSZKR3R/1770839322.836779 'Soundly canceled'); Combo Fighter is his game and he wants it self-sustaining "
     "(C07C2866011/1770084297.911029). Read scope: member of D04UP2L3E3S (Leonard DM), D04V95AAAHW (Arthur DM), C0ADGSZKR3R, C07C2866011, C09UHHN6PFZ, C05433XK267, "
     "C04UEQVDVB7, C09SWTHEMEW; his own mailbox and calendar; Drive files he owns or that are shared with him; Linear, GitHub, Trello, Confluence, Snowflake unscoped."],
    ["Competency", "Finance", "Budget and cost planning for the founders' LLC: monthly running cost of what it takes (March–May), who carries which bill, each founder's cash share "
     "(split email " + GM["split_mail"] + "). Expected outputs: a cost plan sheet and the decision record on each candidate item."],
    ["Task skill", "Planning and decision support", "Exercised by: the take/stay/carried decision per item under the ground rules (" + IDS["ground_rules"] + "), "
     "the three-month plan sheet, and the recommendation with per-founder monthly cost in the reply to Leonard. Authoring: the plan sheet is an authored artifact."],
    ["Task type", "long-horizon (Long Horizon; difficulty mode easy, V3 cap < 90 %; requester target < 85 % average, > 130 counted calls per run)",
     "Services carrying weight: Slack (hub, Arthur's DM reply, #prototype status and the layer.ai reply, #winddown lists, #executives posts, #admin_foundersonly 2023 posts, Jenkins #builds), "
     "Linear (37 issues, 37 notes, 74 per-issue writes), Gmail (split, billing, Jenkins, App Review), Drive/Docs/Sheets/Slides (ground rules, notes doc, draft, deck, the new sheet), "
     "Snowflake (REVENUE_DAILY, 2,284 rows), Trello (the moving rule), GitHub (#1917), GCal (Monday's call), Confluence (page_aws_infra). call_budget 190 "
     "(01_Hardness_Manifest.json); hardness_gate (extreme): PASS in the dossier."],
])

# ---------------------------------------------------------------- 2
A("## 2 · Situation")
A("")
table(["Symptom", "Seen by", "Where it shows (locator)", "Relevant records the persona cannot see"], [
    [f"Leonard asks Robert, on Thursday night (Feb 12 21:40 PT), to decide what the founders' LLC takes from HG to keep Combo Fighter going, what it costs March–May and who pays, "
     f"and to reply before Monday's call.", "Robert (DM recipient)", f"{SL['hub']} (row {S['slack']['hub']['id']})",
     "Arthur's own Kapwing notice (blake@harmonygames.co_1856962040028188034.json) and receipts; none is needed (each is restated in a Robert-visible note)"],
    ["Leonard's candidate list is a Linear project with one issue per item, each with an owner note; the issues carry titles and short descriptions only.",
     "Robert (Linear, unscoped)", f"{IDS['project']}; ENG-2438…ENG-2474", "—"],
    ["The monthly figures Robert meets first in #winddown, the notes doc and the draft are older than what the item owners say now.", "Robert",
     "C0ADGSZKR3R/1770680984.725779, C0ADGSZKR3R/1770933903.645709, " + IDS["notes_doc"] + ", " + IDS["draft_sheet"] + ", the ENG-2445 and ENG-2454 notes (" + LN["Combo Fighter backend and auth stacks (AWS)"]["comment"] + ", " + LN["layer.ai"]["comment"] + ")", "—"],
])

# ---------------------------------------------------------------- 3
A("## 3 · Investigation → action")
A("")
A("Questions to resolve (no answers here):")
for q in ["Which candidates does the LLC take, which does a founder already carry, and which stay with HG, under the ground rules' tests and the keep-or-cancel decisions in #winddown?",
          "Does each of Domino Delights and Zombie Match pass the take test (January income from the warehouse's daily revenue table against what its hosting bills now)?",
          "What does each taken item bill per month now, going by whoever runs it — and is any monthly charge for a taken game missing from the project?",
          "What does each founder already pay personally, and what is each founder's monthly cash under Leonard's split email?",
          "Which items are claimed done but still owe a step, and what date does each step carry under the moving rule (own deadline, the sale, or March 1)?",
          "Is anything that looks like the founders' own actually a Harmony Games asset that goes through Sunset's sale?"]:
    A(f"- {q}")
A("")
A("Writes those answers feed: the plan sheet (rows, costs, payers, steps, owners, dates, the per-month shares); a call and a state on each project issue; a new issue for any "
  "plan line the project lacks; the reply to Leonard (recommendation, monthly cost each, link). Every write depends on the investigation.")
A("")

# ---------------------------------------------------------------- 4
A("## 4 · Pinned final state (UGT anchor)")
A("")
table(["Deliverable", "Required contents", "Destination", "Recipients", "Catalog write", "Fed by"], [
    ["Plan sheet (Google Sheet) (layout from " + IDS["draft_sheet"] + ")", "one row per item (the 37 issues + any missing monthly line) with Item, Game, Decision, Monthly cost, Paid by, Next step, Owner, By (the draft's "
     "columns, " + IDS["draft_sheet"] + "); the three founders' shares per month", "Robert's Drive root d_9f7ba94f7526d54d8482ba", f"shared with {LEO} and {ART}",
     "gsheets create + values update; gdrive move/share", "every §3 question"],
    ["Call on each issue", "a comment with the decision (and why) on each of ENG-2438…ENG-2474; the state per the project description (Done if a founder pays it himself through May or the LLC takes it with nothing left to do; Todo + assignee if the LLC takes it with a step left; Canceled if it stays with HG)",
     f"Linear project {IDS['project']}", "— (Leonard and Arthur read the project)", "linear comment + issue update ×37", "decisions"],
    ["Missing plan line", "a new issue for any monthly line on the plan that the project lacks", f"Linear project {IDS['project']} (team_ENG)", "—", "linear create issue", "scope question"],
    ["Reply to Leonard", "what Robert would do and what it costs each founder a month; a link to the sheet", f"thread of {SL['hub']} (thread_ts {HUB_TS}) in D04UP2L3E3S",
     f"Leonard ({LEO})", "slack send message (thread reply)", "decisions, totals, the sheet"],
])
A("Alternatives a careful run could defend (settled or accepted in §4b): a new top-level DM message instead of a thread reply (settled by the prompt: 'in that thread'); "
  "shares as the even third ($1,150) vs cash after carried costs (both accepted); GitHub's Linear state Done vs Canceled (settled Done: the project description's Done test comes first, 'even if HG still owns it', "
  f"and Arthur counts it 'as mine like the other two', {GM['arthur_mail']}); the VO campaign's payer, Leonard (his card) vs the LLC (settled LLC: 'it's on my card till the end of Feb and moves to our new company's card from March', "
  f"{SL['vo_status']}); CF's stacks at $95 vs $62 (settled $62: Arthur's later email {GM['jenkins_mail']} 'bills $62 a month now' under the costing rule's 'what it bills now'); "
  f"DD player support Done vs Todo (settled Todo: the App Review notice {GM['asc_notice']} is later than Arthur's 'done' note, so a step is left); "
  f"layer.ai's owner Leonard vs Robert and its state Todo vs Canceled (settled: the reply {SL['layer_reply']} asks Robert to 'pull it out yourself before then' and says 'there's nothing on the layer account for our new company to take, it just lapses', so the sheet's Owner is Robert and the issue is Canceled; Todo is only for what the LLC takes); "
  f"the export step on the layer.ai row vs the Combo Fighter row ('the art goes with CF'; both accepted: same step, owner and date on the same sheet); "
  f"the VO campaign's new issue, AppsFlyer's assignee and Google Analytics' state (settled by the project description, "
  f"Leonard's ENG-2451 and ENG-2452 notes and Arthur's mail); share role writer vs commenter/reader (delegated: 'share it with Blake and me'); one combined Metabase + dbt row (draft layout) vs two rows (both accepted).")
A("")
A("### 4b · Canonical outcome (all fair outcomes)")
A("")
cls = SOLV.aggregates(TRUTH)["classes"]
rows4b = [
    ["Plan sheet", "location", "in Robert's Drive root d_9f7ba94f7526d54d8482ba", "'keep it in your drive' (hub)", "any subfolder of his root is not accepted; the root itself", "material"],
    ["Plan sheet", "title", "—", "hub: 'lay the sheet out like my draft'", "any title (e.g. 'LLC 90 days', 'LLC plan')", "representational"],
    ["Plan sheet", "columns", "Item · Game · Decision · Monthly cost · Paid by · Next step · Owner · By", "hub: 'like my draft from Tuesday'", "same columns; order and extra columns free", "material (columns) / representational (order)"],
    ["Plan sheet", "rows", f"{len(TRUTH)} items: ENG-2438…ENG-2474 by title + the CF VO campaign", "—", "Metabase + dbt as one combined row also accepted (draft layout); non-charges (BoomBit test, CrazyGames licence) may appear as $0 HG lines", "material"],
    ["Plan sheet", "Decision per row", f"LLC {cls.get('LLC')} · Founder {cls.get('Founder')} · HG {cls.get('HG')} (solver/truth.json)", "—", "labels LLC / founder (Arthur) / HG or 'stays with HG' / 'Sunset's sale'", "material"],
    ["Plan sheet", "Monthly cost", "DD prod account 140 · CF backend and auth stacks 62 · CF VO campaign 3,000 · Metabase 100 · dbt 100 · GitHub 48 · every other row 0",
     "—", "$-formatted or plain; 3000 / 3,000 (the cap); Metabase + dbt combined 200", "material"],
    ["Plan sheet", "Paid by", "LLC for the three LLC-billed lines (DD prod account, CF backend and auth stacks, CF VO campaign: Leonard's card only through Feb, the new company's card from March); Arthur for Metabase, dbt, GitHub; HG or blank for HG rows", "—", "'the LLC', 'the new company', 'Arthur (Kub card)'; for HG rows 'HG', 'none' or blank; not Leonard for the campaign (the plan runs Mar 1–May 31)", "material"],
    ["Plan sheet", "Next step / By", "DD player support: get a support build approved and released before Helpshift stops (by Feb 28); layer.ai: pull CF's character concept art out before access ends Mar 3 (Leonard's reply " + SL["layer_reply"] + "); "
     "GitHub: repos transfer after the data is sold/delivered; CF and DD: through Sunset's sale, when it closes; LLC billing moves: by Mar 1", "Trello card " + IDS["trello_card"] + " (moving rule)",
     "support: any Feb 15–28 date, 'by Feb 28' or 'before Feb 28'; layer.ai: 'by Mar 3', 'before Mar 3', Mar 1–3 or an earlier date from Feb 20, with export / download / save / pull / back up wording, on the layer.ai row or the Combo Fighter row ('the art goes with CF'); 'when the sale closes' or a date tied to it for CF/DD", "material (support, layer.ai, GitHub) / representational (others)"],
    ["Plan sheet", "Owner", "LLC rows: Combo Fighter Robert · Domino Delights Leonard · DD prod account Arthur · CF backend and auth stacks Arthur · AppsFlyer Leonard · DD player support Arthur · CF VO campaign Leonard (each runner's own note or post); layer.ai Robert (the reply asks him to pull the art out himself)", "Trello: 'Whoever runs an item today moves it'", "first names or emails; other rows any owner or blank", "material (LLC rows, layer.ai) / representational (other rows)"],
    ["Plan sheet", "shares per month", f"total ${TOT['total_per_month']:,} (LLC cash ${TOT['llc_cash_per_month']:,} + Arthur's carried ${TOT['carried_per_month'].get('Arthur', 0)}); "
     f"third ${TOT['third']:,.0f}; cash Leonard ${TOT['cash_shares_per_month']['Leonard']:,.0f}, Robert ${TOT['cash_shares_per_month']['Robert']:,.0f}, Arthur ${TOT['cash_shares_per_month']['Arthur']:,.0f}",
     "split email " + GM["split_mail"], "per-month figures, optionally with Mar–May totals (×3); any placement on the sheet", "material"],
    ["Plan sheet", "sharing", f"{LEO}, {ART}", "'share it with Blake and me' (hub)", "writer or commenter/reader", "material (people) / representational (role)"],
    ["Issue calls", "comment per issue", "the row's decision with a reason, on each of the 37 issues", "'leave your call on each issue too' (hub)", "wording free", "material (decision) / representational (wording)"],
    ["Issue calls", "state per issue", "Todo + assignee for the 7 LLC rows (each still has a step: the sale, a billing move, the free tier, the support build); Done for the 3 Founder rows (Arthur pays them through May); Canceled for the 28 HG rows (project description)", "—",
     "ENG-2462 DD player support: Todo, not Done (the App Review notice leaves the support build to ship); GitHub: Done ('even if HG still owns it'; Arthur's mail 'count it as mine like the other two'); layer.ai, Calm Play LLC and Google Analytics: Canceled (stay with HG)", "material"],
    ["Issue calls", "assignee per Todo issue", "ENG-2438 Robert ('robert's game') · ENG-2439 Leonard ('I'll handle it with Sunset') · ENG-2441 and ENG-2445 Arthur (runs the AWS accounts; 'I keep an eye on them') · ENG-2451 Leonard ('I'll set CF up on it') · ENG-2462 Arthur (his support change) · the new VO campaign issue Leonard (on his card)", "project description: 'assign whoever moves it'; Trello: 'Whoever runs an item today moves it'", "—", "material"],
    ["Missing plan line", "new issue", f"one issue for the CF VO campaign in {IDS['project']}, Todo, assigned to Leonard", "prompt: the project matches the sheet; project description: 'One issue per thing the LLC might take from HG or pay for'", "title naming the VO/Meta campaign or CF ads", "material"],
    ["Reply", "destination", f"thread reply under {SL['hub']} (D04UP2L3E3S, thread_ts {HUB_TS})", "prompt: 'in that thread'", "—", "material"],
    ["Reply", "monthly cost each", f"${TOT['third']:,.0f} each (a third of ${TOT['total_per_month']:,}); optionally Arthur's ${TOT['cash_shares_per_month']['Arthur']:,.0f} cash after the ${TOT['carried_per_month'].get('Arthur', 0)} he already carries (cash Leonard ${TOT['cash_shares_per_month']['Leonard']:,.0f}, Robert ${TOT['cash_shares_per_month']['Robert']:,.0f}); "
     f"LLC cash ${TOT['llc_cash_per_month']:,} a month", "hub: 'what it costs each of us a month'", f"the third with or without the cash split; ${TOT['cash_shares_per_month']['Arthur']:,.0f} given as Arthur's cost is not accepted (split email: what one already pays counts toward his third; platform rev3 /prompt DR1)", "material"],
    ["Reply", "what Robert would do", "DD comes over, ZM stays; the campaign is most of the cost; the support build still has to ship before Feb 28", "hub: 'what you'd do'", "wording free; extra items fine (e.g. Robert pulling CF's concept art out of layer.ai before Mar 3)", "material (calls) / representational (wording)"],
    ["Reply", "link", "a link to (or the name of) the plan sheet", "hub: 'share it… tell me here'", "a Drive link or the sheet's title", "representational"],
]
SRC4B = {"location": SL["hub"], "title": SL["hub"], "columns": IDS["draft_sheet"], "rows": "ENG-2438", "Decision per row": IDS["ground_rules"],
         "Monthly cost": GM["jenkins_mail"], "Paid by": SL["vo_status"], "Next step / By": IDS["trello_card"], "Owner": IDS["trello_card"], "assignee per Todo issue": IDS["trello_card"],
         "shares per month": GM["split_mail"], "sharing": SL["hub"], "comment per issue": SL["hub"], "state per issue": "ENG-2438",
         "new issue": "team_ENG", "destination": SL["hub"], "monthly cost each": GM["split_mail"], "what Robert would do": SL["hub"], "link": SL["hub"]}
rows4b = [r + [SRC4B.get(r[1], SL["hub"])] for r in rows4b]
table(["Deliverable", "Field", "Fixed value (or closed accepted set, with sources)", "Delegated by (quoted span, or —)", "Allowed equivalence class", "Material / representational", "Source"], rows4b)

# ---------------------------------------------------------------- 5
F = {r["fid"]: r for r in SRCH}
DM = [
    ("F1", "Leonard's ask (scope, the ground rules, layout, Drive, split email, reply)", "hub text", SL["hub"], "YES (DM member)", "met first (the anchor)", "—", "Yes (anchor AN1: 'Leonard's DM')"),
    ("F2", "the candidate list", "37 issues ENG-2438…ENG-2474", IDS["project"], "YES (unscoped)", "met first", "agents list issues but must open each issue's comments", "Yes (anchor AN2: 'the LLC project in Linear')"),
    ("F3", "the rules: vehicle, window, take test, costing, keep/cancel, pay out, monthly only", "ground rules", IDS["ground_rules"], "YES (shared)", "named by the hub", "the older notes doc F4 also matches 'LLC'", "No (hub incorporates it)"),
    ("F4", "older notes ('DD and ZM come with CF', '$1k')", "superseded", IDS["notes_doc"], "YES (shared)", "met first by a Drive 'LLC' search / overturned by F3", "stops at a conclusion-sounding note", "No"),
    ("F5", "the layout (8 columns)", "draft rows ~1000/300 (stale)", IDS["draft_sheet"], "YES (shared)", "named by the hub ('my draft from Tuesday')", "numbers copied as truth", "No"),
    ("F6", "the split rule", "a third each; carried costs count; shares per month", GT["split_mail"], "YES (INBOX)", "named by the hub ('I'll email you')", "—", "No"),
    ("F7", "the moving rule (owner, own deadline, sale close, Mar 1)", "Trello card", IDS["trello_card"], "YES (unscoped)", "named by the ground rules", "Trello rarely opened", "No"),
    ("F8", "Monday's call", "Mon Feb 16 18:00–18:45Z", EV, "YES (own calendar)", "—", "—", "No (the prompt may say 'Monday's call')"),
    ("F9", "DD prod account $140 a month (never in the prompt)", "$140", SL["arthur_dm"], "YES (DM member)", "overturns C0ADGSZKR3R/1770680984.725779 (~$1k), C0ADGSZKR3R/1770682219.100789 (300), ENG-2441 note", "reply under an unrelated Feb 2 root", "No"),
    ("F10", "January income per game (never in the prompt)", "DD 183.11 · CF 7.36 · ZM 0.00", "snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY", "YES (unscoped)", "decoy C09SWTHEMEW/1770725775.479449 (BoomBit's test view)", "Snowflake rarely opened; sum the grain rows", "No"),
    ("F11", "Arthur carries $248 (never in the prompt)", "Metabase 100 · dbt 100 · GitHub 48", GT["arthur_mail"], "YES (INBOX)", "overturns C0ADGSZKR3R/1770933903.645709 (~$300) and ENG-2447 note", "mail searched by tool name", "No"),
    ("F12", "the VO campaign at $3,000 a month cap from March; on Leonard's card till the end of Feb, then the new company's card; its own line (never in the prompt)", "$3,000", SL["vo_status"], "YES (#prototype member)", "overturns C07C2866011/1770489896.754049 (both live)", "outside every list; a thread reply; no 'LLC' keyword", "No"),
    ("F13", "Robert's deck (campaign rate)", "~$3k a month", IDS["cf_deck"], "YES (owner)", "supports F12", "—", "No"),
    ("F14", "App Review rejection (never in the prompt)", "email-draft support does nothing without a mail account", GT["asc_notice"], "YES (INBOX)", "overturns ENG-2462 'done' note", "buried among App Store mail", "No"),
    ("F15", "the 'done' claim on DD player support", "Arthur's note " + LN["Domino Delights player support"]["comment"], LN["Domino Delights player support"]["issue"], "YES (unscoped)", "met first / overturned by F14", "stops at 'done'; under the project's Done test the miss also flips the issue to Done", "No"),
    ("F16", "PR #1917 merged", "Replace Helpshift with support email", IDS["pr"], "YES (unscoped)", "supports the claim", "merge read as release", "No"),
    ("F17", "Jenkins DD iOS Submission #218 with the change", "#218", SL["builds_result"], "YES (#builds member)", "ties F14 to the change", "—", "No"),
    ("F18", "Calm Play is HG's subsidiary (never in the prompt)", "fully owned by Harmony Games", BASE["calm_owned"], "YES (#admin_foundersonly member)", "overturns the ENG-2472 note", "an older-channel search", "No"),
    ("F19", "Calm Play note 'could just be our LLC'", "claim (control row since rev4)", LN["Calm Play LLC"]["issue"], "YES (unscoped)", "met first / overturned by F18 and the ground rules' new-LLC vehicle", "face value", "No"),
    ("F20", "layer.ai access until March 3rd", "Mar 3", BASE["layer_mar3"], "YES (#prototype member)", "own deadline beats Mar 1; its thread holds F33", "dated everything Mar 1", "No"),
    ("F21", "the subscription checklist (GitHub after data sold; Slack 3; Google Feb 15)", "checklist", BASE["checklist"], "YES (#winddown member)", "—", "—", "No"),
    ("F22", "Helpshift stops; DD/ZM off before Feb 28", "Feb 28", BASE["helpshift_feb28"], "YES (#winddown member)", "the support item's deadline", "NB-5 vendor date never used", "No"),
    ("F23", "Arthur moves github, dbt, Metabase to his KubLLC card", "payer", BASE["arthur_kub"], "YES (#winddown member)", "connects F11", "—", "No"),
    ("F24", "the lifestyle-route post", "route", BASE["lifestyle"], "YES (#executives member)", "cited by the ground rules", "—", "No"),
    ("F25", "IP to auction; the LLC buys what is left", "vehicle", BASE["auction"], "YES (#executives member)", "cited by the ground rules", "—", "No"),
    ("F26", "AWS account layout (DD dev/prod, ZM one account, analytics)", "layout", "confluence:page_aws_infra", "YES (unscoped)", "—", "Confluence rarely opened", "No"),
    ("F27", "CF backend and auth stacks 'about $95' (Arthur's ENG-2445 note)", "$95 (stale)", LN["Combo Fighter backend and auth stacks (AWS)"]["issue"] + " " + LN["Combo Fighter backend and auth stacks (AWS)"]["comment"], "YES (unscoped)", "met first / overturned by F32", "the note every run reads", "No"),
    ("F28", "Sunset liquidates laptops and build machines", "HG asset", "C07C2866011/1770839126.382429", "YES (#executives member)", "with Arthur's ENG-2446 note", "—", "No"),
    ("F29", "Figma prepaid to Sep 11", "HG", BASE["figma_sep11"], "YES (#winddown member)", "overturns the draft's Figma LLC row", "—", "No"),
    ("F30", "AppsFlyer free up to 15K installs", "$0", BASE["appsflyer"], "YES (#winddown member)", "with Leonard's ENG-2451 note", "—", "No"),
    ("F31", "the Unity Ads $100 (one-off)", "one-off", BASE["unity_100"], "YES (#prototype member)", "control (not monthly)", "added as monthly", "No"),
    ("F32", "CF's own account bills $62 now (never in the prompt)", "$62", GT["jenkins_mail"] + " (message " + GM["jenkins_mail"] + ")", "YES (INBOX; to Robert, cc Leonard)", "overturns F27 ($95)", "subject 'jenkins'; the figure is in the second paragraph, past a snippet", "No"),
    ("F33", "CF's concept art is only in layer.ai; Robert pulls it out himself before access ends (never in the prompt)", "Owner Robert, by Mar 3", SL["layer_reply"], "YES (#prototype member; @-mentions Robert)", "overturns the ENG-2454 note " + LN["layer.ai"]["comment"] + " ('cancelled it on the 11th', no step)", "a thread reply under F20; 'layer' alone is swamped by 'player'", "No"),
]
A("## 5 · Discovery map")
A("")
A("Root cause and findings appear only here and never in the prompt.")
A("")
table(["Fact", "Value", "Locator", "Persona-readable", "Met first / overturned by", "Search risk", "Name in prompt?"],
      [[f"{fid} {fact}", val, loc, pr, mf, risk, nm] for fid, fact, val, loc, pr, mf, risk, nm in DM])

# ---------------------------------------------------------------- 5a
A("## 5a · Search-as-persona proof")
A("")
A("`persona_view.py search robert <service> \"<query>\"` reads base data; seeded rows Robert can see are counted from the SQL overlay "
  "(check-sql PASS for every scoped seeded record, dossier 1.E). Outputs verbatim below the table.")
A("")
rows5a = []
for fid, *_ in DM:
    r = F.get(fid, {})
    rows5a.append([fid, r.get("service", "?"), r.get("query", "?"), f"{r.get('base', 0)} base + {r.get('seeded', 0)} seeded", r.get("hidden", "?"),
                   r.get("first") or "—", r.get("found", "NO")])
table(["Fact (§5 row)", "Service", "Natural query", "Visible hits", "Hidden by ACL", "First visible hit (id)", "Found?"], rows5a)
A("```")
A(rd("brief_searches.txt"))
A("```")
A("")

# ---------------------------------------------------------------- 6
A("## 6 · Triggers, incorporation and implicit requirements")
A("")
table(["Graded requirement", "Seeded where", "Trigger category the prompt must carry", "Incorporating source (locator · persona-readable · unique · instructions-not-answer)", "Inferable"], [
    ["decide each candidate under the ground rules", f"{IDS['ground_rules']}", "scope (the LLC project; Leonard's ask)", f"hub {SL['hub']} names 'the ground rules doc' · YES · one doc titled 'LLC ground rules' · rules, no answers", "yes, once the hub is followed"],
    ["the take test from the warehouse", "snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY", "none in the prompt (the ground rules name 'the warehouse's daily revenue table')", f"{IDS['ground_rules']} · YES · one daily revenue table (REVENUE_DAILY_V2 agrees) · names the table, not the sums", "gotcha with a record trigger"],
    ["cost each item at what it bills now, by its runner", "ground rules", "none", f"{IDS['ground_rules']} · YES · unique · rule only", "gotcha with a record trigger"],
    ["the split (a third each; carried counts)", GT["split_mail"], "deliverable (what it costs each of us a month)", f"hub 'I'll email you how we split the money' · YES · one mail 'LLC money' · rule, no figures", "yes"],
    ["owners and dates (own deadline, sale, Mar 1)", IDS["trello_card"], "none", f"ground rules 'How things move is on the LLC card on our board' · YES · one card · rule only", "gotcha with a record trigger"],
    ["sheet layout", IDS["draft_sheet"], "deliverable (the sheet, like the draft)", f"hub 'lay the sheet out like my draft from Tuesday' · YES · one draft · layout (its numbers are stale)", "yes"],
    ["sheet in Robert's Drive, shared with Leonard and Arthur", "hub", "destination + recipients", "hub · YES · — · instruction", "yes (prompt restates it)"],
    ["a call and a state on each issue", f"{IDS['project']} description", "deliverable (leave the call on each issue)", "project description · YES · one project · state tests only (who pays first, then whether a step is left)", "yes"],
    ["the campaign as its own plan line", SL["vo_status"], "deliverable (what it costs us March through May)", f"{SL['vo_status']} 'count it as its own line in what we pay each month' · YES · one status reply · instruction, the figure is the campaign's own cap", "gotcha with a record trigger (the status reply)"],
    ["the layer.ai export step, its owner and date", SL["layer_reply"], "none", f"ground rules → Trello card 'Anything that already has its own deadline keeps it'; the reply {SL['layer_reply']} @-mentions Robert · YES · unique (the only reply under the access-date post) · asks for the step, not the sheet value", "gotcha with a record trigger"],
    ["a new issue for the missing line", "—", "deliverable: the project ends up matching the sheet (prompt)", f"prompt sentence, plus the project description {IDS['project']} 'One issue per thing the LLC might take from HG or pay for' (no record names the campaign as missing)", "yes, once the campaign row is found"],
    ["reply in Leonard's thread with the per-founder cost", "hub", "destination (that thread) + content", f"hub 'tell me here' · YES · thread {HUB_TS} · instruction", "yes (prompt pins the thread)"],
])
A("Anchor-name table (noun phrases of at most 6 words; `;` separates synonyms):")
A("")
table(["Anchor", "May be named"], [
    ["AN1", "Leonard's DM; Leonard's message from Thursday night"],
    ["AN2", "the LLC project in Linear; the LLC take-over project"],
])

# ---------------------------------------------------------------- 7
A("## 7 · Dates and constraints")
A("")
table(["Item", "Absolute date or value", "Source", "Past fact or deadline"], [
    ["Robert's today", "Saturday Feb 14, 2026 (clock 2026-02-14T00:00Z = Fri Feb 13 16:00 PT)", "00_Task_Context.json universe.persona_today; last #winddown post before the clock C0ADGSZKR3R/1770937460.360699", "—"],
    ["Leonard's ask", "Thu Feb 12, 2026 21:40 PT (2026-02-13T05:40Z)", SL["hub"], "past fact"],
    ["the draft 'from Tuesday'", "Tue Feb 10, 2026 10:30 PT (2026-02-10T18:30Z)", IDS["draft_sheet"], "past fact"],
    ["Monday's call", "Mon Feb 16, 2026 10:00–10:45 PT (18:00–18:45Z)", EV, "deadline (future event)"],
    ["the plan window", "Mar 1 – May 31, 2026", IDS["ground_rules"], "plan field"],
    ["Helpshift stops", "before Feb 28, 2026", BASE["helpshift_feb28"], "deadline"],
    ["layer.ai access ends", "Mar 3, 2026", BASE["layer_mar3"], "deadline"],
    ["Leonard's layer.ai reply", "Thu Feb 12, 2026 11:15 PT (19:15Z)", SL["layer_reply"], "past fact"],
    ["Arthur's 'jenkins' email", "Thu Feb 12, 2026 20:20 PT (2026-02-13T04:20Z)", GM["jenkins_mail"], "past fact"],
    ["App Review notice", "Thu Feb 12, 2026 23:30 PT (2026-02-13T07:30Z)", GM["asc_notice"], "past fact"],
    ["Kapwing Pro ends", "Feb 25, 2026", "ENG-2456 note " + LN["Kapwing"]["comment"], "past decision / plan field"],
    ["Figma prepaid", "to Sep 11, 2026", BASE["figma_sep11"], "plan field"],
    ["shutdown premise", "decided Feb 9–11, 2026; Sunset signed Feb 12 (wind-down acknowledged, no business as usual)", "C0ADGSZKR3R/1770931777.561519", "past fact"],
])

# ---------------------------------------------------------------- 8
A("## 8 · Difficulty levers")
A("")
table(["Lever", "Used", "Load-bearing", "Where it lives", "Prompt-side condition"], [
    ["Ambiguity", "yes", "yes", "the plan's population and figures live across Linear notes, Slack, Gmail, Snowflake (F9–F14)", "the prompt names the anchors only, never where an answer lives"],
    ["Dynamic change", "yes", "yes", "older figures met first (#winddown, notes doc, draft, issue notes) and overturned later (F9, F11, F12, F14)", "the prompt names neither the summary nor the correction"],
    ["Multi-source", "yes", "yes", "Slack, Linear, Gmail, Drive family, Snowflake, Trello, GitHub, Confluence", "no source named as an exact artifact beyond the two anchors"],
    ["Async", "no", "no", "Friction: none (03_Error_Async_Config.txt)", "—"],
    ["Error recovery", "no", "no", "Friction: none", "—"],
    ["Access control", "no", "no", "every load-bearing record is Robert-visible (check-sql PASS)", "no ask to read someone else's scoped data"],
])

# ---------------------------------------------------------------- 9
A("## 9 · Must not appear in the prompt")
A("")
for grp, items in [
    ("Tool and server names (catalog.json)", "slack_send_message, slack_read_thread, slack_search_public_and_private, linear_list_issues, linear_list_comments, linear_create_comment, linear_update_issue, "
     "linear_create_issue, gsheets_create_spreadsheet, gsheets_values_update, gdrive_share_file, gdrive_move_file, gmail_search_messages, snowflake_execute_query, snowflake_list_tables, "
     "trello_get_card, github_get_pull_request, confluence_get_page, gcal_list_events; any MCP server name; 'the X tool'"),
    ("Opaque ids and filenames", f"{IDS['ground_rules']}, {IDS['notes_doc']}, {IDS['draft_sheet']}, {IDS['cf_deck']}, {IDS['trello_card']}, {IDS['project']}, ENG-2438…ENG-2474, "
     f"{SL['hub']}, D04V95AAAHW, C09UHHN6PFZ, {GT['split_mail']}, {GT['arthur_mail']}, {GT['asc_notice']}, {IDS['pr']}, #218, REVENUE_DAILY, page_aws_infra"),
    ("Findings and root causes (01 dossier)", "DD's $140; DD's $183.11 January income; ZM's $0.00; Arthur's $248 and its parts; the VO campaign or any ad spend; the $3,000 cap; the App Store "
     "rejection or that support is not done; Calm Play's subsidiary status; layer.ai, CF's art or its Mar 3; CF's stacks figure ($62 or $95); GitHub after the data sale; any issue state (Todo, Done, Canceled) or assignee; every decision, total, share ($3,202, $3,450, $1,150, $902) or count (7/3/28)"),
    ("Hidden authorities and rules", "the ground rules' contents (take test, costing rule, vehicle rule, window, pay out, monthly only), the warehouse or 'revenue table', the split rule, the "
     "Trello card or its moving rule, the project description's state tests, Arthur's DM or mails (billing, 'jenkins'), Leonard's #prototype status or layer.ai reply, the Jenkins build"),
    ("Format and choreography", "markdown, numbered steps, a per-column content list, a service list, a call count, 'first … then …'"),
    ("Friction and files", "none configured; no reference files or /app/artifact paths"),
]:
    A(f"- **{grp}:** {items}.")
A("")

# ---------------------------------------------------------------- 10
A("## 10 · Entity traps")
A("")
A("`entity.py collisions` and `entity.py resolve` for every name the prompt could use, verbatim:")
A("```")
A(rd("brief_entity.txt"))
A("```")
table(["Correct entity (exact)", "Lookalike(s)", "How they differ", "Locator (email or record id)"], [
    ["Leonard Hayes", "'Leonard' alone (no other Leonard)", "co-founder; the hub's sender", LEO],
    ["Arthur Blake ('Blake')", "'Blake' used in Slack and docs; GitHub token EMPLOYEE_0025_GITHUB_USERNAME; mailbox alias blake@ (I03)", "one person", ART],
    ["Robert", "Linear id usr_Robert (I10)", "the persona", ROB],
    ["the LLC project", "base projects 'GoD - Beta', 'Zombie Match 3D'", "the only project named LLC", IDS["project"] + " (ENG-2438…ENG-2474, team_ENG)"],
    ["LLC ground rules (doc)", "'LLC notes (Monday)' (older)", "the hub names the ground rules", IDS["ground_rules"]],
    ["Calm Play LLC", "'the LLC' (the founders' new one)", "Calm Play is HG's subsidiary (C04UEQVDVB7/1701383740.580749)", LN["Calm Play LLC"]["issue"]],
    ["ENG-2438…ENG-2474", "ZOM-### series (ZM team)", "the project's issues are ENG", IDS["project"]],
    ["Arthur's 'jenkins' email", "Jenkins Builder mail and #builds bot posts (thousands of 'jenkins' hits)", "a person's mail, To Robert, cc Leonard, Feb 13 04:20Z", GT["jenkins_mail"]],
    ["<@EMPLOYEE_0016_SLACK_ID> in the layer.ai reply", "<@EMPLOYEE_0033_SLACK_ID> tagged on the parent post", "EMPLOYEE_0016_SLACK_ID is Robert (entity.py resolve Robert, above)", SL["layer_reply"]],
])

# ---------------------------------------------------------------- 11
A("## 11 · Pre-submit checklist")
A("")
for b in ["Persona voice: Robert, first person, plain; no spec-sheet layout", "Names only the two anchors (§6 table); no §9 item",
          "States the deliverables: the sheet in his Drive like Leonard's draft, shared with Leonard and Blake; the call on each issue; the project matching the sheet; a reply in Leonard's thread",
          "No tool or server name; no step list; no count", "Wind-down acknowledged (no business as usual); Monday's call as the deadline",
          "Clean spelling and punctuation; no riddle, hint, hedge or if-chain", "20–4,000 words", "Run `/create-prompt-writing check` before `/prompt`"]:
    A(f"- [ ] {b}")
A("")

# ---------------------------------------------------------------- 12
A("## 12 · Blockers and routed defects")
A("")
A("None blocking. No fact is routed to /create-injection: every §5 fact is found by a natural search or reached by reading the anchor's thread, table or project (§5a); "
  "the rev4 facts F32 (gmail 'jenkins') and F33 (slack 'layer.ai', re-run on the fixed reply) were searched as Robert. "
  "The rev4 prompt check (04_Prompt_Check.md finding 1) routed ENG-2454's open state to /create-injection; the reply now ends 'there's nothing on the layer account for our new company to take, it just lapses' (SQL f1a290ced176), and a fresh blind re-check rated the state SETTLED. "
  "The platform /hardness review of rev3 (run_forensics/rev3/precheck/1a_hardness_FAIL_r3.md) failed at 2 (too easy; failure-pattern risk); rev4 changes only records, never the prompt, and §4b now pins "
  "the layer.ai Owner and By, ENG-2462's state under the new Done test, the campaign's payer and CF's stacks at $62. "
  "Unverified: none. The platform /injection review of rev2 left A-4/A-5/A-6 for /prompt; each is settled by a dated record (dossier, Platform review section). "
  "The platform /prompt review of rev2 (run_forensics/rev2/1_prompt_FAIL_r2.md) failed UGT on three Linear writes (F1 the VO campaign's new issue, F2 ENG-2451's assignee, "
  "F3 ENG-2452's state); rev3 settles each with a dated record (dossier, Platform /prompt review section) and §4b pins every state, Todo assignee and the new issue.")
A("")

# ---------------------------------------------------------------- 13
A("## 13 · Self-review")
A("")
table(["Area", "Counter-reading (strongest argument it fails)", "Evidence that resolves it", "Verdict"], [
    ["Fair readings (C6)", "Reading B reports Arthur's monthly cost as $902.", f"split email {GM['split_mail']}: each carries a third and what one already pays 'counts toward his third'; Arthur's cost is $1,150 ($248 carried + $902 cash); the platform's rev3 /prompt review rejected '$902 as Blake's cost' (run_forensics/rev3/1_prompt_PASS_r3.md DR1)", "settled"],
    ["Fair readings (C6)", "Reading B leaves the campaign off, or keeps it on Leonard's card as his carried cost.", f"{SL['vo_status']} 'it's on my card till the end of Feb and moves to our new company's card from March … so count it as its own line in what we pay each month'; the plan runs Mar 1–May 31 (ground rules); §4b fixes it as an LLC row", "settled"],
    ["Fair readings (C6)", "GitHub is HG (the org stays HG's) rather than Founder.", f"project description: Done 'if one of us pays it himself through May (even if HG still owns it)'; {GM['arthur_mail']} 'count it as mine like the other two'; §4b pins Done", "settled"],
    ["Fair readings (C6)", "ENG-2462 goes to Done: Arthur's note says 'done' and the PR merged.", f"the App Review notice {GM['asc_notice']} (Feb 13 07:30Z) is later than the note (01:30Z) and says the email-draft support does nothing without a mail account, so a step is left: Todo, Arthur", "settled"],
    ["Fair readings (C6)", "layer.ai belongs to Leonard (he cancelled it) and goes to Todo (the export is still to do).", f"the reply {SL['layer_reply']} asks Robert 'can you pull it out yourself before then?' and says 'there's nothing on the layer account for our new company to take, it just lapses'; Todo is only for what the LLC takes (project description); §4b: Owner Robert, Canceled; a fresh blind re-check rated the state SETTLED (plan/sweep_dispositions.md)", "settled"],
    ["Fair readings (C6)", "The export step belongs on the Combo Fighter row ('the art goes with CF'), not the layer.ai row.", f"both placements give the same step, owner (Robert) and date (Mar 3) on the same sheet; §4b accepts either row (representational); the surface's C4 pattern reads either row", "accepted outcomes"],
    ["Fair readings (C6)", "CF's stacks cost $95 (Arthur's ENG-2445 note).", f"Arthur's later email {GM['jenkins_mail']} (04:20Z vs the 00:58Z note): 'CF's own account bills $62 a month now'; the costing rule counts what it bills now", "settled"],
    ["Clarity (C7)", "'tell me here' could be a new DM message, not a thread reply.", f"the prompt says 'in that thread' (§4b destination); thread_ts {HUB_TS}", "settled"],
    ["Clarity (C7)", "'share it with Blake and me' leaves the share role open.", "§4b: writer or reader accepted (representational)", "accepted outcomes"],
    ["Incorporation (C8)", "the ground rules doc could be confused with the older notes doc.", f"one doc titled 'LLC ground rules' ({IDS['ground_rules']}); the notes doc is 'LLC notes (Monday)' ({IDS['notes_doc']}) and older", "unique"],
    ["Incorporation (C8)", "the new-issue requirement has no record trigger.", "the prompt carries it as 'the project ends up matching the sheet' (§6); no record states the campaign is missing", "trigger in the prompt"],
    ["Truthfulness (C17)", "'Thursday night' or 'Tuesday' could be the wrong day.", f"hub {SL['hub']} = Thu Feb 12 21:40 PT; draft {IDS['draft_sheet']} = Tue Feb 10 10:30 PT", "true"],
    ["Truthfulness (C17)", "naming 'Blake' could resolve to someone else.", f"entity.py resolve 'Blake' → {ART} only (§10)", "true"],
    ["Feasibility / ACL (C18–C19)", "the sheet must be in Robert's Drive root and shared; a copy of Leonard's draft would be owned by Leonard.", "gsheets create (owner = Robert) + gdrive move to d_9f7ba94f7526d54d8482ba + gdrive share; never edit Leonard's draft", "feasible"],
    ["Feasibility / ACL (C18–C19)", "a deciding fact could sit in a mailbox Robert cannot read.", "check-sql PASS (dossier 1.E): the split, billing and App Review mails are Robert's INBOX copies", "feasible"],
    ["Contrived register (C15–C16)", "'make sure the project matches the sheet' could read as a hint that something is missing.", "it is a completeness instruction for a deliverable (the project is the decision record), names no item, cause or count (prompt_qc_cases trap_hint_or_riddle: naming a symptom or a deliverable is fine)", "ordinary"],
    ["Contrived register (C15–C16)", "listing four deliverables could read as a command list.", "deliverables and who to tell are the screen-24 skeleton, not sequenced method steps (C15)", "ordinary"],
])
A("Fair readings, clarity, incorporation, truthfulness, feasibility / ACL and the contrived register are each addressed above with evidence. "
  "Unresolved: none; the prompt is not yet written (draft or human), and check mode re-tests every point on the actual text.")
A("")
open(os.path.join(WF, "04_Prompt_Writing_Brief.md"), "w").write("\n".join(L) + "\n")
print("wrote 04_Prompt_Writing_Brief.md", len("\n".join(L)))

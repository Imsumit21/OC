#!/usr/bin/env python3
"""Assemble Working_Files/01_Scenario_Design.md from the builder's ids, manifest and surface and the pasted tool outputs.
Design only: contains no prompt, Oracle Event or criterion text. Re-run after build_scenario.py."""
import json, os, subprocess, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
sys.path.insert(0, HERE)
import build_scenario as B
man = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json")))
surf = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))
I, BASE, T, Q = B.IDS, B.BASE, B.T, B.Q
ENV = {**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"}
def run(a): p = subprocess.run(a, cwd=WS, capture_output=True, text=True, env=ENV); return (p.stdout + p.stderr).rstrip()
def rd(rel): return open(os.path.join(WF, rel)).read().rstrip()
term, thr = B.term, B.thr
reach = rd("00_PreScenario/reach_frederick.txt")
ent_c, ent_r, ent_f = rd("plan/entity_collisions.txt"), rd("plan/entity_resolve.txt"), rd("00_PreScenario/entity_frederick.txt")
gate = run(["python3", "-B", "Task_Authoring/tools/hardness_gate.py", "Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.draft.json", "--design"])
gsv = run(["python3", "-B", "Task_Authoring/tools/gradable_surface.py", "validate", "--task-dir", "Task_Authoring/task_inputs"])
gsr = run(["python3", "-B", "Task_Authoring/tools/gradable_surface.py", "gradeable-report", "--task-dir", "Task_Authoring/task_inputs"])
v2, liv, pol = rd("plan/hardness_v2_check.txt"), rd("plan/trap_liveness.txt"), rd("plan/policy_scores_output.txt")
fc = rd("plan/forecast_output.txt")
fc_id = [l for l in fc.splitlines() if "forecast record" in l][-1].split("'id': '")[1].split("'")[0]
fc_lines = "\n".join(sorted({l for l in fc.splitlines() if "whole    V3" in l or l.strip().startswith("V3:")}))
cansee = rd("00_PreScenario/cansee_anchors.txt")
import re as _re
_row = lambda k: next(l for l in pol.splitlines() if l.strip().startswith(k))
LAZY = _re.search(r"([\d.]+%)", _row("") if False else next(l for l in pol.splitlines() if "only" in l and "Inbox" in l)).group(1).replace("%", " %")
_p7 = _row("0.7x  ").split(); _led = _row("ledger priors  ").split()
POLNOTE = f"at 0.7× the rates E[avg] is {_p7[1]} and P(all gates) {_p7[-1]}; the ledger view is {_led[2]} (`plan/policy_scores_output.txt`)"
extra = lambda n: rd("plan/" + n) if os.path.exists(os.path.join(WF, "plan", n)) else ""
review_notes = extra("design_review_dispositions.md")
L = []; A = L.append
def table(head, rows):
    A("| " + " | ".join(head) + " |"); A("|" + "---|" * len(head))
    for r in rows: A("| " + " | ".join(str(x).replace("|", "/") for x in r) + " |")
    A("")
U = B.CTX["universe"]
A("# Scenario Design — frederick_dd_publishing · design only · contains no prompt, OE or criterion text"); A("")
A("Written 2026-11-06 by `/create-scenario` (Claude Opus 5.5). Builders: `Working_Files/plan/build_scenario.py` (manifest, surface, ids, planned wording), `plan/assemble_design.py` (this file), `plan/policy_scores.py` (UNCALIBRATED scores). Learnings applied: `00_Pre_Scenario_Analysis.md` §1a (the four completed Frederick tasks) and the root `learnings` file."); A("")
A("## 0 Assignment, persona census and horizon note"); A("")
table(["Field", "Value"], [
 ("Universe", f"key `{U['key']}`, label {U['label']}, `{U['clock_line']}`; seed bound `freeze_utc` {B.CTX['freeze_utc']} (Tue Sep 30 17:00 PT); `shutdown_rules_apply` {str(U['shutdown_rules_apply']).lower()}; build {U['build_label']}"),
 ("Assignment", f"Executive · Frederick Stone (Co-founder, `frederick.stone@harmonygames.co`) · Finance · Analysis and synthesis · long-horizon · medium · October 1, 2025 07:00 (context_hash `{B.CTX['context_hash'][:12]}`)"),
 ("Evals category", "Founders / Exec / Strategy (`Evals/references/rules/task_categories.md`: strategic decisions, pitches, priorities and executive coordination) inside Finance (models, budgets, forecasts)"),
 ("Loss budget", "Medium cap < 85 %; requester target < 80 % (`author_targets` in the draft manifest); design target E[avg] ≤ 72 % (requester cap minus 8 points)"),
 ("Horizon", f"Long Horizon → `effective_profile: extreme`; requester target over 130 counted calls in every run; `volume_exception` call floor 180, per-record floor 60; `cohort_exception` floor 24 (honest budget {B.TOTAL_BUDGET}, per-record {B.PER_RECORD}, about 85 single-object writes)"),
 ("Theme screen", "Domino Delights is a tile game with no bio-adjacent theme; no seeded text uses one"),
 ("Role remit", f"Frederick is a co-founder (roster) and Commercial Lead (Contacts `175c0d7bc72ed244b944cb90`). Leonard put the publishing-rights question to him by name on Aug 25 (`{BASE['rights_post']}`), Frederick ran the Appodeal talks (`{BASE['appodeal_thread']}`) and opened outreach on Sep 24 (`{BASE['tranche']}`, `{BASE['partners_doc']}`)"),
])
A("Persona reach census (`persona_view.py reach frederick_stone --top 40`, verbatim):"); A(""); A("```"); A(reach); A("```"); A("")
A("Identities (`entity.py resolve \"Frederick Stone\"`): Linear `usr_175c0d7bc72ed244`, Trello `4b4a68fc0fec0b254e4f9d8e`, Confluence `user_EMPLOYEE_0008`, Drive root `d_175c0d7bc72ed244b944cb` (owned). GitHub shows 'Ryan' (hazard S04), and the sync doc lists him as Ryan too: GitHub carries no row."); A("")
A("## 1 Storyline"); A("")
A(f"Leonard asked the founders on Aug 25 whether to give up Domino Delights' mobile publishing rights while keeping code, IP and non-mobile rights (`{BASE['rights_post']}`, `{BASE['sync_doc']}`). The bridge is going badly by Sep 30 (`C07C2866011/1759196260.965849`, `C07C2866011/1759182620.491829`), so he hands Frederick the model: where each publisher stands, what each Live offer brings in over 12 months and in Q4, what the game earns if kept, and which offer goes first. One publisher takes the rights, so offers are compared, never summed. 26 publishers, 7 Live."); A("")
A(f"- Timeline (`references/universe_kb/by_universe/synthcut/timeline.md`): the window sits after the Sep 3 bridge launch (`C07C2866011/1756749288.785249`) and the Aug 28 sync (`{BASE['sync_doc']}`). No shutdown premise: Leonard's line about closing costs (`C07C2866011/1758739428.647609`) and his Oct 1 banker line (`C07C2866011/1759290197.446099`) are never used.")
A("- cohorts.json: no fit — every KB cohort is a Linear or service record set, and this cohort is outside publishers defined by the rule doc and the outreach sheet (`" + I["rule_doc"] + "`, `" + I["outreach_sheet"] + "`).")
A(f"- trap_catalog precedents: C01 (thread replies that correct: Arthur's cash note `{I['arthur_cash']}`), B02 (automated senders: Summit's acknowledgement `{thr('Summit Mobile')}`, base Tilting Point `{BASE['tilting_ack']}`), K02 (app-name lineage: Calm Play to Harmony Games, behind the wrong beneficiary on the returned wire; the account is in Harmony Games' name `{BASE['svb_name']}`, and Calm Play never held one `{BASE['calm_play_bank']}`), D03 (deck families: the May one-pager `{I['onepager_deck']}`), P01 (shared first names: no seeded person shares an HG first name, §1c).")
A(f"- Base anchors Frederick can see: rights position `{BASE['rights_post']}`, the sync `{BASE['sync_doc']}`, his numbers question `{BASE['numbers_question']}`, Leonard's organic figure `{BASE['organic_arpi']}`, the tranche line `{BASE['tranche']}`, Appodeal `{BASE['appodeal_thread']}`, Rayking `{BASE['rayking_thread']}`, the UA/BD board `{B.UABD_BOARD}` and its BD Follow Up list `{B.BD_LIST}`.")
A(f"- Natively spans gmail, slack, gdocs, gdrive, trello, snowflake, gcal, gsheets, gslides (9, e.g. `{BASE['appodeal_thread']}`, `{BASE['sync_doc']}`, `{B.BD_LIST}`, `ANALYTICS.MONETIZATION.REVENUE_DAILY`); injection adds contacts and linear with load-bearing roles (`{I['anika_contact']}`, `{I['eng2362_comment']}`)."); A("")
A("## 1a Coherence audit"); A("")
A("Scope = every record a correct run opens. Walked against `references/universe_kb/by_universe/synthcut/coherence_hazards.json` and the known-data-issue cards `references/known_data_issues/synthcut.md`."); A("")
table(["Record", "Category", "Fields", "Pointer", "Hazard / card", "Disposition"], [
 ("Rayking thread message order", "temporal", "message dates", BASE["rayking_thread"], "hazard T02", "fold: no seed appended; the run reads dates"),
 ("Seeded threads' date format", "identifier/format", "date header", thr("Tallwater Games"), "hazard I04", "fold: seeded Gmail rows use the RFC-2822 form of their mailbox's neighbours"),
 ("Frederick's mailbox file alias", "identifier/format", "file name", "frederick@harmonygames.co_1842348778705877030.json", "hazard I03", "fold: seeded threads follow the frederick@ file alias with frederick.stone@ ids"),
 ("Drive name vs Docs title extension", "identifier/format", "name", BASE["partners_doc"], "hazard I15", "fold: seeded docs keep the same title in Drive and Docs"),
 ("Frederick's GitHub display name", "semantic", "name", "frederick.stone@harmonygames.co/1842359398719557772", "hazard S04", "avoid: GitHub carries no row"),
 ("Seeded calendar events and invitation mails", "cross-service referential", "summary ±1 day", I["pb_event"], "hazard R08", "fold: each seeded event gets its INT-11 invitation mail in every attendee mailbox"),
 ("Slack links to Docs", "cross-service referential", "doc ids in links", I["standing_line"], "hazard R04", "avoid: seeded Slack names documents by title, never by link"),
 ("Reply counters on three base roots", "quantitative", "reply_count / latest_reply", BASE["banker_root"], "hazard Q01, Q03", "fold: SQL updates counters on the banker, 70 % D1 and Matthew roots (manifest hazard_acknowledgements Q01, dated_claim)"),
 ("REVENUE_DAILY mirror", "quantitative", "total_revenue_usd", "snowflake.wh_analytics__monetization__revenue_daily", "hazard Q09", "fold: the rule doc names one table; V2 mirrors it; the sum is by month, never per network"),
 ("Copies of the ESG note", "quantitative", "body", I["esg_thread"], "hazard Q10", "fold: one identical body per mailbox copy"),
 ("ENG-2362 assignee", "state/lifecycle", "assignee, state", "ENG-2362", "hazard L08", "avoid: assigned to Arthur (active), state Todo; the comment is his own, on an open ticket, so no closed-ticket activity"),
 ("BD Follow Up list on the UA/BD board", "state/lifecycle", "list / activity", B.BD_LIST, "hazard L12", "fold: seeded cards sit in an open list; board dateLastActivity is updated with them"),
 ("DD September installs", "quantitative", "installs", "snowflake.wh_analytics__monetization__revenue_daily", "card SC-1", "excluded: no row reads installs from the warehouse; monthly installs are publisher commitments"),
 ("Warehouse revenue against P&L workbooks", "quantitative", "monthly revenue", "f_a5e9fc9c8a3188faf66784", "cards SC-35, SC-3", "excluded: Frederick can open none of the P&L workbooks (persona_view: 12 hidden, the one visible hit is the 4X budget), so a correct run never meets a second figure; the rule doc names the table. No cell-level comparison was made"),
 ("Ad-revenue payouts per network", "quantitative", "payouts", "snowflake.wh_analytics__monetization__revenue_daily", "card SC-17", "excluded: keep value uses total_revenue_usd, never a network figure"),
 ("Runway, burn, cash balance", "quantitative", "cash", "C07C2866011/1758739428.647609", "cards SC-3, SC-5, SC-73", "excluded: cash means deal inflows only; no deliverable asks for runway, burn or balance"),
 ("Singular and Griffin lines in the sync doc", "quantitative", "plan terms", BASE["sync_doc"], "cards SC-39, SC-63", "excluded: only the rights line is cited"),
 ("Vendor mail from brian.foster@", "semantic", "sender", "C08MCEP1B9B", "card SC-6", "excluded: no vendor mail is on the path"),
 ("Frederick's founder status and pay", "semantic", "role", "Contacts 175c0d7bc72ed244b944cb90", "cards SC-49, SC-54", "excluded: no row grades either"),
 ("Investor sheet rows", "other", "status", "f_48247af79428823c3cac92", "cards SC-9, SC-10, SC-33, SC-34", "excluded: investor work is out of scope"),
 ("Homa path", "semantic", "co-dev or publishing", BASE["homa_codev"], "bridge /prompt r1 fork", "settled: the rule doc names Homa with the co-dev talks, out of scope"),
 ("Rayking 'reply'", "other", "X-Gmail-Labels", BASE["rayking_thread"], "Q4 /oe r1 finding", f"settled: an unsent draft addressed to Leonard; his Sep 4 LinkedIn line (`{BASE['rayking_linkedin']}`) is closed by a seeded Sep 5 DM (`{I['rayking_dm']}`), so Waiting on us"),
 ("Tamatem", "semantic", "publisher name", BASE["tamatem"], "design review F9", f"settled: Julia passed a name along and nobody came to us; the rule doc excludes that (`{I['rule_doc']}`)"),
 ("Term sheets against Frederick's Sep 24 words", "temporal", "dates", BASE["numbers_question"], "design review B1", "settled: every term sheet is dated Sep 25 or later, after his DM and the new tranche"),
 ("Tilting Point form", "semantic", "which title", BASE["tilting_ack"], "none", f"settled: the rule doc names the form as out of scope (`{I['rule_doc']}`)"),
])
A("Six hazard categories in scope: temporal T02; semantic S04; referential R08, R04; quantitative Q01, Q03, Q09, Q10; state/lifecycle L08, L12; identifier/format I03, I04, I15."); A("")
A(f"**Sibling-defect sweep.** Designed defects are a changed advance (Tallwater), a changed commitment (Sunfold), a claimed wire (Oakline), a moved date (ESG). Siblings checked: Harbor Lane and Wavecrest have calls with no change, so a found call doesn't by itself mark a trap (`{I['pb_event']}` is the only note that moves a term). No base publisher thread holds terms: Appodeal's proposal states no rev share or advance (`{BASE['appodeal_thread']}`). Whole-universe Slack scan for Aug and Sep shows no publisher reply or term (`00_PreScenario/whole_universe_publisher_sept.txt`); name census in `plan/name_census.json` with a positive control."); A("")
A("## 1b Active speakers"); A("")
A("Status from `references/universe_kb/by_universe/synthcut/activity.json` (status_at_clock)."); A("")
table(["Person", "Email", "status_at_clock", "Seeding role"], [
 ("Leonard Hayes", "leonard.hayes@harmonygames.co", "active_sep_2025_quiet_in_oct", "the hub mail, ground rules doc, DD publishing card, standing line, Tallwater call note, ESG reply"),
 ("Arthur Blake", "arthur.blake@harmonygames.co", "active_sep_2025_quiet_in_oct", "cash note, #analytics pointer, ENG-2362 comment"),
 ("Robert", "robert@harmonygames.co", "active_sep_2025_quiet_in_oct", "Copperleaf relay, Kestrel post"),
 ("Frederick Stone", "frederick.stone@harmonygames.co", "active_sep_2025_quiet_in_oct", "persona: outreach sheet, one-pager, folder, co-dev doc, sent mail, two card comments, the Rayking DM"),
 ("ESG Law partner", "PERSON_2694_EMAIL", "external (not in activity.json; base signature in mailbox file frederick@harmonygames.co_1841636073974841484.json)", "the signing-date note"),
 ("Publisher people", "marek@oaklinegames.com, paola@tallwatergames.com, lena@sunfoldmobile.com and the others", "external, seeded with no base footprint (plan/name_census.json)", "terms, passes and acknowledgements"),
])
A("## 1c Identity traps"); A(""); A("```"); A(ent_c); A(""); A(ent_f); A(""); A(ent_r); A("```"); A("")
A("- Seeded external first names avoid every HG first name and every shared name above: Marek, Paola, Lena, Diego, Sofia, Jonas, Mei, Anika, Callum, Elena, Rhys, Nadia, Yuki, Tessa, Omar, Greta, Ivo.")
A("- `brian.foster@` is reused by Node's and Craftsman+'s people in base (SC-6): no seed uses it.")
A(f"- ESG reuses the base token PERSON_2694, whose role is stated in `{BASE['esg_engagement']}` (learnings §14)."); A("")
A("## 2 Cohort spine"); A("")
A(f"- Rule (rule doc `{I['rule_doc']}`): {man['cohort']['definition']}.")
A(f"- Size 26: Live {B.COUNTS['Live']} · Withdrawn {B.COUNTS['Withdrawn']} · Out on rights {B.COUNTS['Out on rights']} · Passed {B.COUNTS['Passed']} · Waiting on us {B.COUNTS['Waiting on us']} · No reply {B.COUNTS['No reply']}. Key = publisher. `cohort_exception` floor 24: no natural 40-record cohort exists, and padding it would add always-pass rows that cut the SD (`00_Pre_Scenario_Analysis.md` §1a).")
A("- Surfaces and shortcut audit (manifest cohort.evidence_surfaces):")
for s in man["cohort"]["evidence_surfaces"]:
    A(f"  - {s['service']} · `{s['tool']}` · {s['per_record_calls']} × {s['records']} · decides: {s['decides']} · no bulk: {s['why_no_bulk']} · short-circuit: {s['short_circuit']} (`{I['rule_doc']}`)")
A(f"- Predicate: six statuses, a closed set in the rule doc, first that fits, top to bottom (`{I['rule_doc']}`).")
A(f"- House rule over the natural reading (A15): the rights position (`{BASE['sync_doc']}`) overrides the highest value.")
A(f"- Boundary records (A17): Copperleaf `{I['copperleaf_relay']}` and Redwood `{I['eng2362_comment']}` are in although off the sheet; Summit `{thr('Summit Mobile')}` is No reply although a message exists; Rayking `{BASE['rayking_thread']}` is Waiting on us although a draft exists.")
A(f"- Necessity: every term sheet decides rights, net terms or an input; every thread decides status. Volume is honest because the board, contacts and reminders are one write per publisher the founders asked for (`{I['dd_card']}`, `{I['hub_thread']}`)."); A("")
A("## 3 Hidden authorities"); A("")
rows = []
for a in man["authorities"]:
    dec = ", ".join(a["decoy_seeded_ids"] + a["decoy_base_pointers"]); sc = a["decoy_scope"]
    home = (a["seeded_ids"] + a["base_pointers"])[0]
    rows.append((a["id"], a["name"], f"{a['home_service']} `{home}`", f"{a['decoy_service']} `{dec}` ({sc['dimension']}: decoy '{sc['decoy']}' vs task '{sc['task']}')", ", ".join(a["governs"]), f"\"{a['findable_query']}\" (`{home}`)"))
table(["Id", "Name", "Home", "Decoy (scope)", "Governs", "Findable query"], rows)
A(f"Each authority is named by a fragment (K1 names H1 in `{I['hub_thread']}`; K3 names H2 in `{I['rule_doc']}`; K4 names H3 on `{I['dd_card']}`). The hub delegates by role and links none. `governs` lists don't overlap (hardness_gate hidden_authorities)."); A("")
A("## 4 Delegation lattice"); A("")
table(["Anchor", "Anchor name (noun phrase, ≤ 6 words)", "Record"], [(a["id"], a["prompt_reference"], f"`{a['record']}`") for a in man["anchors"]])
A(f"Hub: Leonard's Sep 30 23:10Z mail to Frederick (`{I['hub_thread']}`), delegating by role to the ground rules doc, the folder and the card. It lists no publisher, link or location."); A("")
rows = []
for f in man["ask_fragments"]:
    na = ", ".join(f"{x['id']} ('{x['quote']}')" for x in f["names_authorities"]) or "—"
    rows.append((f["id"], f"{f['service']} · `{f['container']}`", f["kind"], " → ".join(f["incorporated_via"]), f"`{f['delegated_by_record']}`", f"\"{f['delegation_quote']}\"", ", ".join(f["requirement_ids"]), na))
table(["Fragment", "Service · container", "Kind", "Chain", "Delegated by", "Delegation quote (verbatim, planned wording)", "Requirements", "Names authorities"], rows)
A(f"- Amendments in another service, later in time: K6 gmail `{I['esg_thread']}` (Sep 30) changes the signing date in `{I['rule_doc']}` (Sep 29); K7 gcal `{I['pb_event']}` (Sep 29) changes Tallwater's advance in `{term('Tallwater Games')}` (Sep 26); K8 trello `{I['sunfold_comment']}` (Sep 30) changes Sunfold's commitment in `{term('Sunfold Mobile')}` (Sep 25). Each keeps the rest.")
A(f"- Non-authoritative distractors: the co-dev doc (`{I['codev_doc']}`, H1 decoy, another game); Frederick's candidate lists (`{BASE['partners_doc']}`, `{BASE['bizdev_doc']}`); Appodeal's programme line (`{BASE['appodeal_fwd']}`)."); A("")
A("## 5 Chains and trap register"); A("")
table(["Chain", "Root cause", "Hops (service: record → finding)", "Ends in"], [(c["id"], c["root_cause"], " → ".join(f"{h['service']}: `{h['record']}` ({h['finding']})" for h in c["hops"]), c["ends_in"]) for c in man["chains"]])
rows = []
for t in man["traps"]:
    recs = ", ".join(f"`{x}`" for x in (t["seeded_ids"] + t["base_pointers"])) or "—"
    fam = t["family"] + (f" ({t['distractor_type']})" if t.get("distractor_type") else "")
    rows.append((t["id"], fam, recs, t["requirement"], t["expected_wrong_reading"], t["resolver"], t.get("discovery_order", "—")))
table(["Trap", "Family", "Records", "Requirement", "Expected wrong reading", "Resolver", "Discovery order"], rows)
A("Hardness v2 traps used as separate cross-source decisions (guide Part 3), each with the convincing wrong source and the record that beats it:"); A("")
table(["Channel", "v2 trap", "Convincing wrong source (who, when)", "Record that beats it (who, when, authority)", "Weight-5 rows it moves"], [
 ("DONE", "1 · proving done across services", f"Marek's Sep 29 wire confirmation (`{thr('Oakline Games')}`) and the card comment (`{I['oakline_card_comment']}`)", f"Arthur, checking SVB with Leonard, Sep 30 (`{I['arthur_cash']}`)", "B_PA, VQ_Oakline, K_r_banked"),
 ("CORR", "2 · a correction somewhere else", f"Tallwater's term sheet, Sep 26 (`{term('Tallwater Games')}`)", f"Leonard's note on the Sep 29 call (`{I['pb_event']}`)", "A_adv_PB, V12_Tallwater"),
 ("ALIAS", "6 · different names for the same thing", f"Moonrail's open term sheet under its trading name (`{term('Moonrail Studios')}`)", f"Robert's Sep 29 post on Kestrel (`{I['kestrel_post']}`), joined by Anika's signature and Contacts `{I['anika_contact']}`", "S_out_PC, T_item_PC"),
 ("FILT", "7 · items outside the obvious filter", f"the outreach sheet and Frederick's inbox (`{I['outreach_sheet']}`)", f"Robert's relay (`{I['copperleaf_relay']}`) and Arthur's ENG-2362 comment (`{I['eng2362_comment']}`), brought in by the rule doc", "S_in_PH, S_in_PI, V12_Copperleaf, V12_Redwood, T_item_PH, T_item_PI, S_total"),
 ("EXC", "5 · a rule hidden in the data", f"Northglow's numbers, the largest on the table (`{term('Northglow Publishing')}`)", f"Leonard's Aug 25 rights position, adopted at the Aug 28 sync (`{BASE['rights_post']}`, `{BASE['sync_doc']}`)", "S_out_PD, S_out_PJ, R_top"),
 ("INPUT", "8 · wrong inputs to a total", f"Sunfold's term sheet, Sep 25 (`{term('Sunfold Mobile')}`)", f"Frederick's Sep 30 comment after Lena's call (`{I['sunfold_comment']}`)", "A_com_PE, V12_Sunfold, R_top"),
 ("DATE", "4 · dates, windows and dependencies", f"Oct 31 in the rule doc (`{I['rule_doc']}`)", f"ESG's Sep 29 note and Leonard's Sep 30 reply (`{I['esg_thread']}`)", "VQ_Harbor, VQ_Wavecrest"),
 ("FOLLOW", "3 · follow-through a rule requires", "the model, the board and the reply look like the whole job", f"Leonard's standing line (`{I['standing_line']}`), joined to the sheet's What we sent column (`{I['outreach_sheet']}`)", "W_count, W_1, W_2, W_3"),
])
A("### Mechanism portfolio (S5a)"); A("")
A("Priors from `tools/hardness_ledger.py priors --model claude-opus-5-5` (UNCALIBRATED; never pooled across models). Rates used by the forecast are disclosed overrides sourced from measured placements on the completed Frederick tasks (`plan/run_forecast.sh`)."); A("")
table(["#", "Candidate (anchor records)", "Coupling", "Findability term", "Prior (family)", "Design rate", "Survives complete retrieval", "Selected"], [
 ("DONE", f"the returned first-look wire (`{I['arthur_cash']}`)", "paid claim → banked → Q4 cash", "'SVB', 'first-look' or 'wire', under an older root; the note doesn't name Oakline", 'done_gap Beta(3,3) mean 0.50 · hev_7f44d83eaad625e9, hev_522f1ca2bc9062de, hev_b8f28a892a74b855', "0.50", "yes: needs the banked definition", "yes"),
 ("CORR", f"Tallwater call note (`{I['pb_event']}`)", "advance → value → Q4 cash", "calendar search by name", 'superseding Beta(1,5) mean 0.17 · hev_e61e07235eadbd24, hev_1ceea0e7e912f48b, hev_ebc012c844829411', "0.55", "no: placement, measured 3 of 7 caught", "yes"),
 ("ALIAS", f"Kestrel's freeze (`{I['kestrel_post']}`)", "group → studio → withdrawn", "'Kestrel', not 'Moonrail' or 'Anika'", 'scope_alias Beta(1,4) mean 0.20 · hev_ab2508cad060b0ac, hev_ace612d2f2268cdf, hev_9cefe52f59fd5be5', "0.55", "yes: needs the join", "yes"),
 ("FILT", f"Copperleaf and Redwood (`{I['copperleaf_relay']}`, `{I['eng2362_comment']}`)", "rule → off-sheet offer → value → pick", "generic search, then the ticket", 'exact_predicate Beta(2,4) mean 0.33 · hev_9c403cae42eb4df8, hev_c2297d21ba5cbc7b, hev_0148aad4d8a4eb2d', "0.35 and 0.55", "no: placement", "yes"),
 ("EXC", f"rights position (`{BASE['sync_doc']}`)", "grant clause → status → pick", "'publishing rights'", 'authority Beta(1,4) mean 0.20 · hev_d17e4abe74f0e7e0, hev_1de494f0682754d6, hev_633340c96ebfc696', "0.30", "yes: storefront wording against non-mobile", "yes"),
 ("INPUT", f"Sunfold comment (`{I['sunfold_comment']}`)", "installs → value → pick", "card by first name", 'superseding Beta(1,5) mean 0.17 · hev_e61e07235eadbd24, hev_1ceea0e7e912f48b, hev_ebc012c844829411', "0.45", "no: placement", "yes"),
 ("DATE", f"signing date (`{I['esg_thread']}`)", "date → net terms → Q4 cash", "thread names no publisher", 'boundary_date Beta(2,1) mean 0.67 · hev_3d96146a0a8b19a5', "0.40", "yes: the arithmetic stays", "yes"),
 ("FOLLOW", f"standing line (`{I['standing_line']}`)", "rule → sheet column → status → draft", "'one-pager', 'organic'", 'authority Beta(1,4) mean 0.20 · hev_d17e4abe74f0e7e0, hev_1de494f0682754d6, hev_633340c96ebfc696', "0.50", "no: placement", "yes"),
 ("REUSE", f"first-name cards (`{I['oakline_card']}`, `{I['sunfold_card']}`)", "contact → publisher → comment, not a card", "card title by first name", "reuse: no record", "0.25", "yes", "secondary (T10, no rule: eight-rule limit)"),
 ("ACK", f"Summit's acknowledgement (`{thr('Summit Mobile')}`)", "message → No reply", "the thread", "near_miss_mention: no record", "0.10", "yes", "control (T11)"),
 ("COMPL", "a publisher already turned down in a cancelled invite", "completion elsewhere", "calendar", "completion_elsewhere Beta(1,4) mean 0.20", "0.20", "no", "rejected: low prior, and the eight-rule limit"),
 ("TOTALS", "Q4 cash across all offers", "aggregate of every channel", "—", "—", "—", "—", "rejected: rights go to one publisher, so a total is meaningless, and it would fail every run"),
 ("COUNT", "number of Live offers in the reply", "aggregate of four channels", "—", "—", "—", "—", "rejected for the reply (Q4's COUNTS lesson); kept on the board only"),
 ("WAREHOUSE-KPI", "a test gate checked in USER_COHORT_RETENTION", "warehouse join", "—", "—", "—", "—", "rejected: a stated rule is caught every run, and SC-1 sits beside it"),
 ("SDK-BUILD", f"a tranche tied to an SDK in the store build", "git claim", "—", "—", "—", "—", "rejected: invites a base git contradiction (learnings §49), and ENG-2367+ can't be seeded (SC-26)"),
])
A("Each selected rule's controls and over-application operator are in the draft manifest (`mechanism_portfolio[].controls`, `over_application`), and its channel in `channels`."); A("")
A("### Liveness flags (S5b)"); A(""); A("`trap_liveness.py --design` (verbatim):"); A(""); A("```"); A(liv); A("```"); A("")
table(["Flag", "Nodes", "Disposition"], [
 ("breadcrumb", "T21", f"structural at design time: T21 is the co-dev decoy, which the entry set reaches by search; it decides nothing (`{I['codev_doc']}`)"),
 ("SAME_PLACE (hardness_v2_check)", "T7", f"clean, but the tool can't see that Sunfold's card sits on an anchor's list: the comment stays on one card (`{I['sunfold_card']}`) and never in the list or the DD publishing card"),
])
A("## 6 Failure-diversity plan"); A("")
table(["Channel", "Behaviour that finds the deciding record", "Measured analog (completed tasks)", "Rows", "Independent of"], [
 ("DONE", "a Slack search for SVB, wire or first-look", "bridge SciPlay reply under an unrelated post: 3 of 6", "B_PA, VQ_Oakline, K_r_banked", f"calendar and Trello (`{I['arthur_cash']}`)"),
 ("CORR", "a calendar search per publisher, or opening the event", "Q4 calendar note found 3 of 7", "A_adv_PB, V12_Tallwater, VQ_Tallwater", f"Slack behaviour (`{I['pb_event']}`)"),
 ("ALIAS", "joining a signature or Contacts row to a post", "handover id join: 5 of 6 missed, halved for fairness", "S_out_PC, T_item_PC, W_count", f"name searches (`{I['kestrel_post']}`)"),
 ("FILT, Copperleaf", "a 'publisher' Slack search that reaches a reply", "bridge reply under an unrelated post: 2 of 8 then 3 of 6, higher here because the reply says publisher", "seven rows and the pick", f"mail behaviour (`{I['copperleaf_relay']}`)"),
 ("FILT, Redwood", "a 'publisher' Slack search, then opening Linear", "Q4 Linear-only fact: 0 of 6; pointer added", "six rows", f"thread reading (`{I['arthur_analytics']}`)"),
 ("EXC", "applying the sync position to grant wording", "judgment rows rarely land", "S_out_PD, S_out_PJ, R_top", f"retrieval habits (`{BASE['sync_doc']}`)"),
 ("INPUT", "reading comments on a first-name card", "trello_get_comments ran where the card was named", "A_com_PE, V12_Sunfold", f"Slack and calendar (`{I['sunfold_comment']}`)"),
 ("DATE", "opening a thread that names no publisher", "handover mail outside the money window: 2 of 6 missed", "VQ_Harbor, VQ_Wavecrest", f"Slack and Trello (`{I['esg_thread']}`)"),
 ("FOLLOW", "a search for the one-pager or the organic figure", "reply under an unrelated root: 20–30 % caught", "W_count, W_1, W_2, W_3", f"mail (`{I['standing_line']}`)"),
])
A("Each channel moves at least two rows, so one trap can't chain patterns (bridge rev12 batch 1). Most trap rows hang on one channel, because a row on several channels fails nearly every run and adds no spread (`00_Pre_Scenario_Analysis.md` §1a: mixed weight tracks SD)."); A(""); A("```"); A(pol); A("```"); A("")
A("Correlation risk named: DONE, FILT and FOLLOW all reward thorough Slack searching, on different containers. The rho sweep above is the check on it."); A("")
A("## 7 Deliverables and dependent writes"); A("")
tg = {"gsheets": f"new sheet moved into `{I['dd_folder']}` (owner Frederick, Drive and Sheets rows agree)", "trello": f"UA/BD board list `{B.BD_LIST}`, card `{I['dd_card']}`; checklists and items proven there by all six handover baselines (card `67cf1b506d78ad3c72e02a35`)",
      "contacts": "Contacts (unscoped)", "gcal": "Frederick's own calendar", "gmail": f"drafts in his mailbox; the reply on `{I['hub_thread']}`"}
table(["Write", "Tool", "Count", "Depends on", "Requirements", "Target and access"], [(w["service"], f"`{w['tool']}`", w["count"], ", ".join(w["depends_on"]), ", ".join(w.get("requirements", [])), tg.get(w["service"], "")) for w in man["writes"]])
A(f"Reuse vs create (A8): Oakline and Sunfold already have follow-up cards under their contacts' first names (`{I['oakline_card']}`, `{I['sunfold_card']}`), and Anika and Lena already have contacts (`{I['anika_contact']}`, `{I['lena_contact']}`)."); A("")
A("## 8 Service role map"); A("")
car = {"gmail": I["hub_thread"], "gdocs": I["rule_doc"], "gdrive": I["dd_folder"], "gsheets": I["outreach_sheet"], "gslides": I["onepager_deck"], "slack": I["arthur_cash"], "gcal": I["pb_event"], "trello": I["dd_card"], "contacts": I["anika_contact"], "linear": "ENG-2362", "snowflake": "ANALYTICS.MONETIZATION.REVENUE_DAILY"}
table(["Service", "Role", "Load-bearing fact or write", "Carrier"], [(k, v["role"], v["weight_reason"], f"● (`{car[k]}`)") for k, v in man["services"].items()] + [
 ("github", "not used", "none (S04 name mismatch; code claims invite a git contradiction)", "— (`frederick.stone@harmonygames.co/1842359398719557772`)"), ("confluence", "not used", "never carries a fact (learnings §26)", "—")])
A("## 9 Call budget"); A("")
table(["Phase", "Service", "Calls", "Necessity reason"], [(r["phase"], r["service"], r["calls"], r["reason"]) for r in man["call_budget"]] + [("**total**", "10 services", f"**{B.TOTAL_BUDGET}**", "unconditional")])
A("Golden-run note: a lean correct run still needs every term sheet, about 82 single-object writes and the discovery reads, which is about 145 counted calls. Reads never fell below 54 on a Frederick task; bridge's 53–55 writes left its weakest run at 109, and Q4's 88–93 held its weakest at 151 (`00_PreScenario/stored_runs_counted_output.txt`). High-count writes are template-identical, so they are sampled in the rubric."); A("")
A("## 10 QC rails"); A(""); A("### Two-reading table"); A("")
DP = [
 ("Oakline banked", "$0: it never hit SVB", "$10,000: Marek confirms the wire", f"Arthur's later note (`{I['arthur_cash']}`); rule doc: banked means in the SVB account (`{I['rule_doc']}`)"),
 ("Oakline Q4 cash", "$30,000: the resend and the net-30 balance land in Q4", "$20,000: the first $10,000 already came", f"same note: resending next week; Dec 14 for the balance (`{I['arthur_cash']}`, `{term('Oakline Games')}`)"),
 ("Tallwater advance", "$40,000", "$60,000 in the term sheet", f"Leonard's later call note (`{I['pb_event']}`); rule doc: latest terms, wherever they are"),
 ("Moonrail status", "Withdrawn", "Live: its sheet is open", f"Robert's post on Kestrel (`{I['kestrel_post']}`), Anika's signature (`{thr('Moonrail Studios')}`), Contacts `{I['anika_contact']}`"),
 ("Copperleaf in", "in, Live", "out: not on the sheet, no term sheet", f"rule doc: came to one of the four of us, however it reached us; their note pasted in by one of us counts (`{I['copperleaf_relay']}`)"),
 ("Redwood in", "in, Live", "out: an engineering note", f"same rule; Arthur pastes her note (`{I['eng2362_comment']}`)"),
 ("Northglow", "Out on rights", "Live: the best numbers", f"grant covers PC and web (`{term('Northglow Publishing')}`); founders keep non-mobile rights (`{BASE['rights_post']}`)"),
 ("Pinegrove", "Out on rights", "Live: mobile stores only", f"ownership of the code passes to Pinegrove (`{term('Pinegrove Games')}`); founders keep code (`{BASE['rights_post']}`)"),
 ("Sunfold installs", "30,000 a month", "50,000 in the term sheet", f"Frederick's later comment (`{I['sunfold_comment']}`); rule doc: latest terms"),
 ("Signing date", "Nov 14", "Oct 31", f"rule doc: if ESG gives a later date, use theirs; Leonard's reply (`{I['esg_thread']}`)"),
 ("Harbor Lane and Wavecrest Q4 cash", "$0: net 60 from Nov 14 lands Jan 13", "their full advances", f"term sheets (`{term('Harbor Lane Games')}`, `{term('Wavecrest Play')}`) with the date above"),
 ("Who gets a draft", "Tallwater, Harbor Lane, Wavecrest", "Moonrail too, or everyone", f"standing line: got it and still Live (`{I['standing_line']}`); sheet column (`{I['outreach_sheet']}`)"),
 ("Rayking", "Waiting on us", "No reply, or answered", f"they wrote and the last message is theirs: Frederick's is an unsent draft to Leonard (`{BASE['rayking_thread']}`), and his LinkedIn line (`{BASE['rayking_linkedin']}`) is closed by his Sep 5 DM (`{I['rayking_dm']}`)"),
 ("Appodeal", "Waiting on us", "Live: it made a proposal", f"no rev share or advance in writing, and the last message is theirs (`{BASE['appodeal_thread']}`)"),
 ("Summit", "No reply", "answered", f"automatic acknowledgement (`{thr('Summit Mobile')}`); rule doc says it doesn't count"),
 ("Tilting Point", "out", "No reply", f"the rule doc names its form as out of scope (`{BASE['tilting_ack']}`, `{I['rule_doc']}`)"),
 ("Tamatem", "out", "a publisher to add", f"rule doc: a name someone passed along doesn't count (`{BASE['tamatem']}`)"),
 ("Homa and NCsoft", "out", "publishers in talks", f"rule doc: co-dev, engine or investment talks aren't part of this (`{BASE['homa_codev']}`, `{BASE['ncsoft_question']}`)"),
 ("Sep 24 lead", "out", "add him", f"Leonard's mail (`{I['hub_thread']}`) over the DM (`{BASE['lead']}`)"),
 ("Apple Arcade", "out", "a dominoes lead", f"not on the sheet, and no one came to us (`{BASE['apple_arcade']}`)"),
 ("Existing cards", "comment on Lena's and Marek's", "new cards", f"the card says so (`{I['dd_card']}`); first names map through the threads (`{I['sunfold_card']}`, `{I['oakline_card']}`)"),
 ("Contacts present", "16 people gave terms or said no; skip Anika and Lena, so 14 adds", "add again, or add Appodeal and Rayking people", f"Leonard's mail (`{I['hub_thread']}`); Contacts `{I['anika_contact']}`, `{I['lena_contact']}`"),
 ("Nudges", "all seven No reply publishers, Summit included", "skip Summit because it acknowledged", f"the card (`{I['dd_card']}`) and the rule that an acknowledgement isn't a reply (`{I['rule_doc']}`)"),
 ("First pick", "Copperleaf, $67,200", "Northglow or Sunfold", f"rule doc ranks Live offers by 12-month value (`{I['rule_doc']}`)"),
]
table(["Decision point", "Best reading", "Strongest alternative", "Resolution (record)"], DP)
A("No decision forks on a reported figure; one reading per point. Dates: every graded date is a plan date with the same PT and UTC day."); A("")
A("### Reach table (load-bearing records)"); A("")
A("Base records, `persona_view.py can-see frederick_stone …` (verbatim, `00_PreScenario/cansee_anchors.txt`):"); A("")
for l in cansee.splitlines():
    if ": YES" in l: A(f"- {l}")
A("")
A("Probes (never load-bearing, and not cited by any fragment): Leonard's DMs `D04UC0UEN2V`, `D04UGG61DUM` are NO for Frederick and are used only as coherence support. DENIAL-INTENDED: outside his reach; alternate_evidence_ids: C07C2866011/1756140953.197759, D05S58U4SAK/1758736827.548589"); A("")
A("Planned seeds (verified at the injection gate; owner, invitee or member Frederick):")
for k in ["hub_thread", "esg_thread", "rule_doc", "outreach_sheet", "onepager_deck", "dd_folder", "pb_event", "arthur_cash", "copperleaf_relay", "kestrel_post", "standing_line", "arthur_analytics", "rayking_dm"]:
    A(f"- LB `{I[k]}` ({k})")
for k in B.TERM_DOCS: A(f"- LB `{term(k)}` ({k} term sheet)")
A("")
A(f"Unscoped load-bearing records: Trello `{I['dd_card']}`, `{I['oakline_card']}`, `{I['sunfold_card']}`; Linear ENG-2362 and `{I['eng2362_comment']}`; Contacts `{I['anika_contact']}`, `{I['lena_contact']}`; Snowflake `ANALYTICS.MONETIZATION.REVENUE_DAILY`."); A("")
A(f"**Feasibility.** Every write exists in `Evals/references/tools/catalog.json` (`gsheets_create_spreadsheet`, `gsheets_values_update`, `gdrive_move_file`, `trello_create_checklist`, `trello_create_check_item`, `trello_create_card`, `trello_add_comment`, `contacts_add_new_contact`, `gcal_create_event`, `gmail_create_draft`, `gmail_reply_to_message`). Frederick owns the folder `{I['dd_folder']}` and his calendar; Trello and Contacts are unscoped. `trello_create_card` on this board is unproven: confirm it in the pre-check. "
  "**Precedence.** Load-bearing facts sit in ● carriers (mail bodies, Docs bodies, Slack messages, Linear comments, Trello descriptions and comments), never only in an attachment. Tallwater's note is a calendar description, a ○ carrier in `Ask_Carriers.md`; stored runs show `gcal_search_events` returns descriptions, so the pre-check must prove the route. "
  "**Naturalness.** The prompt names Leonard's email, the folder and the card; it never names publishers, rules, statuses or where evidence sits. "
  "**Grading devices.** ≤ 5 samples per group plus volume rows; exclusions graded as exact counts on required writes, never as leave-alone rows. The reply carries a pick and three figures, never a list. Cap: 75 rows, at least 45 % mixed weight."); A("")
A("### Coherence rail"); A("")
A(f"Every 1a row is dispositioned; every designed disagreement is a dated human claim overturned by a named later record (T1 `{I['arthur_cash']}`, T2 `{I['pb_event']}`, T7 `{I['sunfold_comment']}`, T9 `{I['esg_thread']}`); no system field is modified. Companions are planned in §11."); A("")
A("## 11 Record plan for /create-injection"); A("")
plan = [
 ("hub", "gmail · gmail_messages/threads", I["hub_thread"], T["hub"], "Leonard → Frederick", Q["hub"].replace("\n\n", " ¶ ")),
 ("ground rules doc", "gdocs + gdrive (owner Leonard, shared Frederick, Robert, Arthur)", I["rule_doc"], T["rule_doc"], "Leonard", Q["rules"].replace("\n\n", " ¶ ").replace("\n", " · ")),
 ("co-dev doc (H1 decoy)", "gdocs + gdrive (owner Frederick)", I["codev_doc"], T["codev_doc"], "Frederick", "co-dev terms we'd accept, not DD; scope: another game; no publisher terms"),
 ("outreach sheet", "gsheets + gdrive (owner Frederick, in the folder)", I["outreach_sheet"], T["outreach_sheet"], "Frederick", "columns Publisher, Contact, First contact, Tranche, What we sent; 24 rows, Appodeal and Rayking among them as came to us; no outcomes; note: " + B.BODIES["sheet_note"]),
 ("May one-pager", "gslides + gdrive (owner Frederick)", I["onepager_deck"], T["onepager"], "Frederick", f"the numbers from the Apr 30 board note (`{BASE['board_followup']}`): D1 50%+, D7 20%+, ARPDAU about $0.13, marked as incentivized traffic"),
 ("DD publishing folder", "gdrive · drive_files (owner Frederick)", I["dd_folder"], T["folder"], "Frederick", "destination"),
 ("DD publishing card", "trello · cards (BD Follow Up list)", I["dd_card"], T["dd_card"], "Leonard", Q["card"]),
 ("F/up with Marek", "trello · cards, comment action", I["oakline_card"] + " / " + I["oakline_card_comment"], T["oakline_card"] + " / " + T["oakline_card_comment"], "Frederick", Q["oak_card"]),
 ("F/up with Lena", "trello · cards, comment action", I["sunfold_card"] + " / " + I["sunfold_comment"], T["sunfold_card"] + " / " + T["sunfold_comment"], "Frederick", Q["sunfold_note"]),
 ("Tallwater follow-up", "gcal · events (one copy per attendee)", I["pb_event"], T["pb_event"] + ", updated " + T["pb_event_update"], "Leonard (Frederick, Paola invited)", Q["pb_note"]),
 ("Monday sit-down", "gcal · events (one copy per attendee)", I["monday_event"], T["hub"], "Leonard (founders)", "DD publishing, Mon Oct 6"),
 ("Harbor Lane call (control)", "gcal · events (one copy per attendee)", I["harbor_event"], T["harbor_event"], "Frederick (Diego invited)", B.BODIES["harbor_note"]),
 ("Wavecrest call (control)", "gcal · events (one copy per attendee)", I["wavecrest_event"], T["wavecrest_event"], "Frederick (Sofia invited)", B.BODIES["wavecrest_note"]),
 ("Rayking DM", "slack (DM root)", I["rayking_dm"], T["rayking_dm"], "Frederick", Q["rayking_dm"]),
 ("Arthur's cash note", "slack (reply under the banker root + counter UPDATE)", I["arthur_cash"], T["arthur_cash"], "Arthur", Q["arthur_cash"]),
 ("Robert's relay", "slack (reply under the 70 % D1 root + counter UPDATE)", I["copperleaf_relay"], T["copperleaf_relay"], "Robert", Q["relay"]),
 ("Kestrel post", "slack (root)", I["kestrel_post"], T["kestrel_post"], "Robert", Q["kestrel"]),
 ("standing line", "slack (reply under the Matthew root + counter UPDATE)", I["standing_line"], T["standing_line"], "Leonard", Q["standing"]),
 ("analytics pointer", "slack (root)", I["arthur_analytics"], T["arthur_analytics"], "Arthur", Q["analytics"]),
 ("ENG-2362 comment", "linear · comments", I["eng2362_comment"], T["eng2362_comment"], "Arthur", Q["eng"]),
 ("ESG thread", "gmail (Leonard, Frederick copies)", I["esg_thread"], T["esg_note"] + " / " + T["esg_leonard"], "PERSON_2694 → Leonard, cc Frederick; Leonard", Q["esg_note"] + " ¶ " + Q["esg_leo"]),
 ("Anika, Lena contacts", "contacts · contacts", I["anika_contact"] + " / " + I["lena_contact"], "—", "—", "Anika Rao, Partnerships, Kestrel Group; Lena Fischer, Sunfold Mobile"),
]
for k, v in B.TERM_DOCS.items():
    plan.append((f"{k} term sheet", "gdocs + gdrive (shared with Frederick)", term(k), "same day as its mail", k, v))
for m in B.M:
    if m.get("base"): continue
    if m["key"] in ("Copperleaf Games", "Redwood Arcade"): continue
    who = (m["person"][0] + " " + m["person"][1]) if m["person"] else "—"
    plan.append((f"{m['key']} thread", "gmail (Frederick's mailbox)", thr(m["key"]), "2025-05..09 by tranche", who, f"{m['status']}; sent: {m['sent']}" + ("; automatic acknowledgement only" if m.get("ack") else "")))
table(["Record", "Service · table", "Planned id", "Time (UTC)", "Author", "Content (planned)"], plan)
A(f"Oakline's Sep 29 message says: '{Q['oak_paid']}' Moonrail's signature reads '{B.BODIES['moonrail_sig']}'."); A("")
table(["Thread class", "Planned wording"], [("Tranche 1 outbound (May, one-pager) `" + I["onepager_deck"] + "`", B.BODIES["out_t1"]), ("Tranche 2 outbound (Sep 8–12) `" + I["outreach_sheet"] + "`", B.BODIES["out_t2"]), ("Tranche 3 outbound (Sep 24–25) `" + I["outreach_sheet"] + "`", B.BODIES["out_t3"]),
 ("Pass `" + thr("Fernhollow Media") + "`", B.BODIES["pass"]), ("Term cover note `" + thr("Tallwater Games") + "`", B.BODIES["terms"]), ("Kitebridge `" + thr("Kitebridge Games") + "`", B.BODIES["kitebridge"]), ("Summit acknowledgement `" + thr("Summit Mobile") + "`", B.BODIES["summit_ack"])])
A("### Integrations and companions"); A(""); A("Companions from `references/universe_kb/by_universe/synthcut/integrations.json`:"); A("")
table(["Service", "INT id", "Companion", "Decision"], [
 ("gcal", "INT-11", f"invitation mails for `{I['pb_event']}`, `{I['monday_event']}` in each attendee mailbox", "seed them, plus one GCal copy per attendee calendar"),
 ("gdrive", "INT-13", "Google Drive Slack app DMs for shares", f"integration_exceptions at injection: shares of `{I['rule_doc']}` and the term sheets sit in drive sharing rows only"),
 ("linear", "INT-03, INT-04, INT-05", "linear[bot] PR comment; Slack DM notifications; digests", f"no PR for the comment; declared exception for `{I['eng2362_comment']}`"),
 ("slack", "INT-22", "'[Slack] … sent you a message' mails", "optional, none seeded: replies are in channels"),
 ("trello", "INT-21", "Trello → Slack: no integration exists", "none"),
 ("gmail", "—", "no INT source maps to gmail itself", "none"),
 ("gdocs / gsheets / gslides", "INT-13 (google_drive)", "as gdrive", "as gdrive"),
 ("contacts", "—", "no integration", "none"),
 ("snowflake", "—", "not writable, not seeded", "none"),
])
A("## 12 Self-test results"); A("")
A("`hardness_gate.py 01_Hardness_Manifest.draft.json --design` (verbatim):"); A(""); A("```"); A(gate); A("```"); A("")
A("`gradable_surface.py validate` and `gradeable-report` (verbatim):"); A(""); A("```"); A(gsv); A(gsr); A("```"); A("")
A("`hardness_v2_check.py --design` (verbatim; dispositions in §5 Liveness flags):"); A(""); A("```"); A(v2); A("```"); A("")
A(f"S9b prior forecast (UNCALIBRATED, advisory, pre-registered): ledger id `{fc_id}`; mechanism rates are disclosed overrides sourced from the completed tasks (`plan/run_forecast.sh`)."); A(""); A("```"); A(fc_lines); A("```"); A("")
A(f"**Lazy-solver pass.** One broad search per service, first hits, no thread opens, stop at the first conclusion: it reads the hub, the rule doc, the sheet, each thread and term sheet, and loses every channel, scoring {LAZY} on the surface (`plan/policy_scores_output.txt`). Every point it scores comes from controls; no leak found.")
A("")
A(f"**Literal-value sweep (planned text).** '$40,000' for Tallwater only in the call note; '30,000' for Sunfold only in the card comment; 'Nov 14' only in the ESG thread; 'beneficiary' only in Arthur's note; 'Kestrel' only in the post, Anika's signature and her contact. **Wording sweep.** Arthur's note and the standing line don't use the word 'publisher'; Robert's relay and the #analytics pointer do, on purpose, so the two off-sheet offers stay findable (`{I['copperleaf_relay']}`, `{I['arthur_analytics']}`). **The rest stands.** No later record re-asserts an amended clause.")
A("")
A("### Self-review"); A("")
A("Walked `Evals/1_Prompt_Eval.md` §2.1 (UGT), §2.2 (feasibility), §3.2 (cross-service coherence) and `Evals/0_Injection_Quality_Eval.md` Check C against this design."); A("")
SR = [
 ("temporal", "the Sep 30 hub falls after the seed bound in PT or UTC", f"23:10Z Sep 30 is before freeze 2025-10-01T00:00Z, and every T value in build_scenario.py is earlier (`{I['hub_thread']}`)"),
 ("semantic", "'given us terms or told us no' could leave out a person who only reached a founder", f"Jonas and Mei gave terms to Robert and Arthur, so they count; their addresses are in the relay and the comment (`{I['copperleaf_relay']}`, `{I['eng2362_comment']}`)"),
 ("cross-service referential", "Kestrel maps to no record Frederick can see", f"her signature and Contacts row carry it (`{I['anika_contact']}`, `{thr('Moonrail Studios')}`)"),
 ("quantitative", "seeded replies leave base reply counters stale", f"hazard Q01 acknowledged; SQL updates them (`{BASE['banker_root']}`)"),
 ("state/lifecycle", "a comment on a closed or stale ticket fails the task", "ENG-2362 is Todo, assigned to Arthur, and the comment is his (ENG-2362)"),
 ("identifier/format", "a seeded Linear comment id breaks the contract", f"minted to the base form and checked at injection (`{I['eng2362_comment']}`)"),
 ("other", "advances this size look implausible for a game earning $381 in September", f"publishers buy on the one-pager and fund UA themselves; figures are modest, and Leonard's own line prices 1 million installs at $500K (`{BASE['organic_arpi']}`)"),
] + [(d[0], f"the strongest alternative holds: {d[2]}", d[3]) for d in DP] + [
 ("volume", "about 145 calls in a lean run is padding-driven", f"each write is one per publisher the founders asked for, and most are template-identical; reads decide status or terms (`{I['dd_card']}`)"),
 ("difficulty", "eight channels near 0.5 is optimistic; measured pre-checks missed about 1 of 3", POLNOTE),
 ("HARDNESS GATE output", "a PASS at --design proves nothing about the SQL", "true: injection re-runs hardness_gate on the SQL with every seeded id; this PASS covers structure only (§12)"),
]
table(["#", "Category or decision point", "Counter-reading (strongest argument it fails)", "Resolution and evidence"], [(i, *r) for i, r in enumerate(SR, 1)])
A(f"HARDNESS GATE (design) result is pasted verbatim above. Forecast `{fc_id}` is advisory and UNCALIBRATED."); A("")
A("Unresolved: no independent red-team review of this design (REDTEAM_* unset; fallback in §13); landing rates are UNCALIBRATED placement priors; `trello_create_card` on the UA/BD board and the calendar-description route are unproven until the pre-check; INT-13 and INT-05 companion choices are decided at injection with base_check."); A("")
A("## 13 Red team (dual)"); A("")
A("RED TEAM UNAVAILABLE: REDTEAM_* is not set in this environment, so `tools/redteam_review.py --mode redteam --dual` cannot reach a reviewer endpoint."); A("")
A("RED TEAM FALLBACK: a fresh-context agent reviewed this design blind to the author's reasoning, with `hg.py`-only access to the base, hunting forks, base contradictions and leaks (findings and dispositions below). The counter-reading table in §12, the whole-universe name census with a positive control (`plan/name_census.json`) and the policy scores back it up. Two blind sweeps run at `/create-injection` before preflight. The requester delegated this choice on 2026-11-06. The waiver stays in Unresolved until a review or the pre-check covers it (learnings §44)."); A("")
if review_notes: A(review_notes); A("")
open(os.path.join(WF, "01_Scenario_Design.md"), "w").write("\n".join(L) + "\n")
print("wrote 01_Scenario_Design.md", len(L), "lines; forecast", fc_id)

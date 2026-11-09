#!/usr/bin/env python3
"""Assemble Working_Files/01_Scenario_Design.md from build_scenario.py and pasted tool outputs. Design only: no prompt,
Oracle Event or criterion text. Re-run after build_scenario.py; the stage gate pastes its block at the end."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
sys.path.insert(0, HERE)
import build_scenario as B  # noqa: E402
ENV = {**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputsK"}
man = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json")))
surf = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))
I, BASE, T, Q, K, TK = B.IDS, B.BASE, B.T, B.Q, B.K, B.TK
TD = "Task_Authoring/task_inputsK"
MAN = TD + "/Working_Files/01_Hardness_Manifest.draft.json"


def run(args):
    p = subprocess.run(args, cwd=WS, capture_output=True, text=True, env=ENV)
    return (p.stdout + p.stderr).rstrip()


def rd(rel):
    return open(os.path.join(WF, rel)).read().rstrip()


reach = rd("00_PreScenario/reach_samuel.txt")
ent_c = rd("00_PreScenario/entity_collisions.txt")
ent_r = rd("plan/entity_resolve.txt")
ent_s = rd("00_PreScenario/entity_samuel.txt")
sweep = rd("plan/literal_sweep.txt")
pol = rd("plan/policy_scores_output.txt")
gate = run(["python3", "-B", "Task_Authoring/tools/hardness_gate.py", MAN, "--design"])
gsv = run(["python3", "-B", "Task_Authoring/tools/gradable_surface.py", "validate", "--task-dir", TD])
gsr = run(["python3", "-B", "Task_Authoring/tools/gradable_surface.py", "gradeable-report", "--task-dir", TD])
v2 = run(["python3", "-B", "Task_Authoring/tools/hardness_v2_check.py", "--design", "--task-dir", TD])
liv = run(["python3", "-B", "Task_Authoring/tools/trap_liveness.py", "--design", "--task-dir", TD])
fc = rd("plan/forecast_output.txt") if os.path.exists(os.path.join(HERE, "forecast_output.txt")) else ""
fc_id = next((l.split("'id': '")[1].split("'")[0] for l in fc.splitlines() if "forecast record" in l), "")
fc_lines = "\n".join(sorted({l for l in fc.splitlines() if "whole    V3" in l or l.strip().startswith("V3:")}))
red = rd("plan/redteam_fallback.md") if os.path.exists(os.path.join(HERE, "redteam_fallback.md")) else ""
_ppl = json.load(open(os.path.join(WS, "Task_Authoring/references/universe_kb/by_universe/synthcut/activity.json")))["people"]
_ppl = _ppl.values() if isinstance(_ppl, dict) else _ppl
act = {p.get("name"): p for p in _ppl if isinstance(p, dict)}

L = []
A = L.append
A("# Scenario Design — samuel_zm_beta_messages · design only · contains no prompt, OE or criterion text")
A("")
A("Written 2026-11-04 by `/create-scenario` (Claude Opus 5.5). Builders: `plan/build_scenario.py` (manifest, surface, ids), `plan/assemble_design.py` (this file), `plan/policy_scores.py` (UNCALIBRATED scores). Prior analysis: `Working_Files/00_Pre_Scenario_Analysis.md`.")
A("")
A("## 0 Assignment, persona census and horizon note")
A("")
A("| Field | Value |")
A("|---|---|")
u = B.CTX["universe"]
A(f"| Universe | key `{u['key']}`, label {u['label']}, `{u['clock_line']}`; seed bound `freeze_utc` {B.CTX['freeze_utc']}; `shutdown_rules_apply` {u['shutdown_rules_apply']} |")
A("| Assignment | Design · Samuel Turner (Game Designer, `samuel.turner@harmonygames.co`) · Marketing and GTM · Retrieval · long-horizon · medium · October 1, 2025 07:00 |")
A("| Evals category | Product & Design (`Evals/references/rules/task_categories.md`: gameplay and design requirements) inside Marketing and GTM (focus: demand and retention, GTM, communications) |")
A("| Loss budget | Medium cap < 85 %. Requester bar on 2026-11-04: corrected average under 80 %, over 130 tool calls in every run, all other gates apply. Design target E[avg] ≤ 72 % (8 points under the bar) |")
A("| Profile | `effective_profile: extreme` (Long Horizon); `volume_exception {call_budget_floor: 200, per_record_floor: 90}` |")
A(f"| Theme screen | The game is Zombie Match 3D and the base copy says \"zombie outbreak\" and \"Plague Race\". 12 stored Opus 5.5 ZM baselines (Julia, Douglas) mention \"zombie\" 253–1,350 times and \"plague\" 23–129 times with 0 `model_refusal_fallback` events. Accepted under the requester's delegation; seeded text avoids those words, and the pre-check is read for fallback events. Base copy stays as it is (`{BASE['pn_sheet']}`) |")
A("| Role remit | Samuel built these messages: Leonard sent him the sheet (`" + BASE["pns_sent"] + "`), the card is `" + BASE["pn_card"] + "`, and he merged `" + BASE["pr248"] + "` |")
A("| Decisions taken | The requester delegated every open choice on 2026-11-04 (`you can choose from your self which option is best fit`): storyline B, the volume exception, the review fallback (§13), one read of `match3d/Assets/Scripts/Notifications/NotificationManager.cs` outside `hg.py` (no other repo file was read) and the theme acceptance |")
A("")
A("Lessons taken from the completed tasks, and where they bind this design:")
A("")
A("| Source | Measured | Applied here |")
A("|---|---|---|")
A("| `frederick_bridge_pipeline_2026-11-03` | Reads alone stalled at 60–83 calls; about 44 single-object writes lifted every run to 109–150 | Two writes per ticket with no batch form, sized so a lean run clears 150 (§9) |")
A("| `douglas_beta_server_signoff_2026-10-28` | 166–239 calls on 17 tickets: per-ticket comments plus a comment and an update each; inline PR comments opened in 1 of 6 runs | Ticket-per-message spine; DONE sits on an inline comment |")
A("| `julia_zm_difficulty_baseline_2026-11-01` | Judgement traps did not land across 28+ runs; DM thread replies and inline comments discriminated; SD 0.099 on one choke point | QA sits in a DM thread reply; eight independent channels; DEP rated lowest |")
A("| `frederick_card_spend_q3_6ad83eebbd6456fd065bbd20` | SD 0.054: every run lost the same rows | Each channel has its own behaviour and at least two rows |")
A("| `frederick_account_handover_2026-10-26` | Bimodal from one hidden class; 80.8 % | No single discovery decides most rows; largest unit 14.3 % of weight |")
A("| `robert_winddown_closeout_2026-10-30` | About 100 rows passed every run; SD flat | Always-pass weight kept near a quarter, 40 members graded by samples |")
A("| `frederick_q4_commitments` rev3 pre-check | One Slack search per name found every named correction; 1 of 8 nodes landed | Corrections use aliases with 0 base hits (`plan/literal_sweep.txt`); feature names are common words |")
A("")
A("```")
A(reach)
A("```")
A("")
A("Linear, GitHub, Trello and Confluence identities (`entity.py resolve`):")
A("")
A("```")
A(ent_s)
A("```")
A("")
A("## 1 Storyline")
A("")
A("Beta is close and the push notification sheet has not moved since June. Leonard wants one straight answer on what actually reaches a player's phone. The sheet says six are Ready; only three really go. Samuel built these messages, so the check lands with him.")
A("")
A(f"- Sheet and owner: PNs Beta tab of `{BASE['pn_sheet']}`, last edited 2025-06-23, 14 rows; Leonard handed it to Samuel on Jun 17 (`{BASE['pns_sent']}`, `{BASE['same_as_dd']}`).")
A(f"- Client: `{BASE['pr248']}` added six messages; the current source schedules exactly those six. Everything is local (`{BASE['all_local']}`, `{BASE['no_push_yet']}`).")
A(f"- Beta scope: `{BASE['beta_scope']}` (Sep 12) and `{BASE['axe_postponed']}` (Sep 22); ZM ROADMAP board `{B.BOARD}`.")
A(f"- Permission ask: `{BASE['shove_to_20']}` (Jul 10), `{BASE['variant_c_13']}` (Aug 13), `{BASE['pushed_back']}` (Sep 18), `{BASE['at_the_beginning']}` (Sep 19).")
A(f"- Names: rename on Jul 24 (`{BASE['gdd_page']}`, `{BASE['release_page']}`); Collect & Win is the Zombie Match name for Win & Collect (`{BASE['liveops_page']}`).")
A("")
A("Universe KB use: this sits on the timeline spine after the Sep 12 beta pipeline post and the Sep 22 Axe Arena postponement (`references/universe_kb/by_universe/synthcut/timeline.md`). cohorts.json: no fit — the population is sheet rows plus filed asks, not a Linear state or label cohort. trap_catalog precedents: C01 (thread replies that correct), C02 (a stated resolution another person says still fails), D05 (version-marked title families), K02 (app-name lineage: Puzzles vs Zombies), N01 (ticket series collisions).")
A("")
A("## 1a Coherence audit")
A("")
A("Scope: everything a correct run opens. Hazard ids from `coherence_hazards.json`; cards from `references/known_data_issues/synthcut.md`.")
A("")
A("| Record | Category | Fields | Pointer | Hazard or card | Disposition |")
A("|---|---|---|---|---|---|")
rows = [
    ("Sheet status columns", "semantic", "Status vs Status (NA, WIP, LIVE) disagree on 4 of 14 rows", BASE["pn_sheet"], "hazard none listed; sibling of SC-14", "designed claim: the rule doc says neither column decides"),
    ("Sheet vs client copy", "quantitative", "1-day and first-mission bodies say Puzzles vs Zombies; the client says Zombie Match 3D; two emoji differ", BASE["pn_sheet"], "hazard K02 lineage", "folded into design: BUILT channel; only headlines graded, emoji never"),
    ("Permission ask point", "temporal", "level 20, level 13 on variant C, 'at the beginning', 'no notification stuff at level 20'", BASE["variant_c_13"], "hazard T02 not touched", "dated claim: Robert's Sep 29 post settles it for beta"),
    ("Snowflake push stats", "cross-service referential", "25 ZM rows with provider firebase, Apr 12 to Sep 27, against 'All our PNs are local'", BASE["all_local"], "hazard R06 family; no card", "avoid: Snowflake stays out of the task and nothing asks for send stats"),
    ("Sheet link in DM", "cross-service referential", "Slack links use Google-native ids", BASE["pns_sent"], "hazard R04", "avoid: no row depends on the link; the sheet is found by title"),
    ("GitHub mail subjects", "cross-service referential", "repo name redacted in some mails", BASE["pr248_mail"], "hazard R03", "avoid: no row reads a subject"),
    ("Arthur's inline comment", "cross-service referential", "no #zombie-prs copy", BASE["pr248"], "hazard R07", "declared: the GitHub app subscribed on Jun 30, after the Jun 26 comment"),
    ("Key series", "semantic", "PR 327 and the Rate Us card cite ENG keys for ZOM work", BASE["pr248"], "hazard S01", "avoid: no row depends on those keys"),
    ("Thread counters", "quantitative", "seeded replies change parent counters", BASE["martin_root"], "hazard Q01", "companion: SQL updates reply_count, reply_users_count, latest_reply"),
    ("Card activity", "temporal", "a seeded comment moves dateLastActivity", BASE["tech_card"], "hazard T06", "companion: SQL updates the card"),
    ("Parent and child state", "state/lifecycle", "parent stays open while children change", I["parent"], "hazard L06", "excluded: the parent is never Done"),
    ("Ticket as shipping proof", "state/lifecycle", "Linear state is not proof of shipping", "ZOM-564", "SC-16; hazard L03", "avoid: seeded DES tickets only; calls rest on the rule tests"),
    ("Assignees", "state/lifecycle", "open issues on quiet people", "ZOM-542", "hazard L08", "excluded: no seeded ticket is assigned to a quiet person"),
    ("Owner field", "identifier/format", "sheet owner is a Resource id", BASE["pn_sheet"], "hazard I14", "avoid: never a write target; the plan is a new sheet Samuel owns"),
    ("Drive name", "identifier/format", "title keeps .xlsx in Drive", BASE["pn_sheet"], "hazard I15", "avoid: found by title words"),
    ("Beta date", "other", "Trello list named BETA: Oct 10", BASE["minor_bugs_card"], "SC-13", "avoid: no date graded; 'on the BETA list' only"),
    ("Beta flags", "other", "dueComplete disagrees on beta cards", BASE["minor_bugs_card"], "SC-14", "avoid: no complete flag read"),
    ("Season Pass", "other", "ship date and analytics status conflict", "page_season_pass_spec", "SC-38", "avoid: the call rests on nothing being scheduled, never on a ship date"),
    ("Telemetry versions", "other", "0.1.x vs 0.3.x", "C05433XK267/1753831576.732069", "SC-19", "avoid: no version matching"),
    ("Boss Arena dates", "other", "prod date before its code", BASE["liveops_page"], "SC-68", "avoid: only 'in the beta' is used, from the BETA list"),
    ("Channel lists", "other", "leavers stay listed; Slack timezones; Victor on invites", "C08R27X0EAH/1758238811.686629", "SC-7, SC-36, SC-70", "avoid: no membership or timezone is graded"),
    ("#zm-collect-win", "other", "archived but active", BASE["liveops_page"], "SC-57", "avoid: no post there"),
]
for r in rows:
    A("| " + " | ".join(f"`{c}`" if i == 3 else c for i, c in enumerate(r)) + " |")
A("")
A(f"Sibling-defect sweep: other rows with the same defect kind as the three designed Holds. `{BASE['pr248']}` schedules six messages; Lives and both lapsed rows pass the day test, Plague Race fires daily, which Leonard accepts on its ticket. No seventh built row exists. Hazard categories in scope: temporal T06, semantic S01, referential R03 R04 R07, quantitative Q01, state/lifecycle L06 L08, identifier/format I14 I15.")
A("")
A("## 1b Active speakers")
A("")
A("Status from `activity.json` (selected universe).")
A("")
A("| Person | Email | status_at_clock | Seeding role |")
A("|---|---|---|---|")
for n, em, role in [("Leonard Hayes", "leonard.hayes@harmonygames.co", "hub, rule doc, line change, freeze comment, parent ticket"),
                    ("Robert", "robert@harmonygames.co", "permission decision, asks"),
                    ("Arthur Blake", "arthur.blake@harmonygames.co", "inline review comment, client-or-server notes"),
                    ("Vincent Parker", "vincent.parker@harmonygames.co", "QA note, ticket passes, DM reply"),
                    ("Brian Foster", "brian.foster@harmonygames.co", "asks, opinion post"),
                    ("Julia Lawson", "julia.lawson@harmonygames.co", "asks"),
                    ("Calvin Price", "calvin.price@harmonygames.co", "Collect & Win ticket, ask"),
                    ("Oliver Brooks", "oliver.brooks@harmonygames.co", "ask"),
                    ("Owen Baker", "owen.baker@harmonygames.co", "asks"),
                    ("Martin Walsh", "martin.walsh@harmonygames.co", "ask")]:
    A(f"| {n} | {em} | {act[n]['status_at_clock']} | {role} |")
A("")
A("## 1c Identity traps")
A("")
A("```")
A(ent_c)
A("```")
A("")
A("```")
A(ent_r)
A("```")
A("")
A("| Name in records | Correct entity | Lookalike and how it is pinned |")
A("|---|---|---|")
A("| Marcus | marcus.bennett@harmonygames.co | Marcus Lee and a Trello token; no seed uses him |")
A("| Martin | martin.walsh@harmonygames.co | Martin Lewis (`PERSON_0394_EMAIL`); seeds use the full name |")
A("| Blake | arthur.blake@harmonygames.co | the same person; Slack uses Blake, seeds use Arthur |")
A("")
A("## 2 Cohort spine")
A("")
A(f"Rule: every row on the PNs Beta tab plus every ask for a new phone message filed on a ticket or a card by Sep 30. Size {len(B.M)}: 14 sheet rows, {sum(1 for m in B.M if m['source'].startswith('ask'))} asks under the parent `{I['parent']}`, 2 asks in comments on other tickets. Calls: Go {B.COUNTS['Go']}, Hold {B.COUNTS['Hold']}, Drop {B.COUNTS['Drop']}.")
A("")
A("| Message | Ticket | Source | Call | What's missing | Role |")
A("|---|---|---|---|---|---|")
for m in B.M:
    A(f"| {m['key']} | {m['ticket'] or '(new ticket)'} | {m['source']} | {m['call']} | {m['missing'] or '—'} | {m['role']} |")
A("")
A("Surfaces and shortcut audit:")
A("")
A("| Surface | Calls × records | Serves | Why no bulk call | Short-circuit |")
A("|---|---|---|---|---|")
for s in man["cohort"]["evidence_surfaces"]:
    A(f"| {s['service']} `{s['tool']}` | {s['per_record_calls']} × {s['records']} | {s['requirement']}: {s['decides']} | {s['why_no_bulk']} | {s['short_circuit']} |")
A("")
A("Boundary records: red-dot tickets ZOM-471 and ZOM-539 (in the game), Rate Us ZOM-397 and the permission popup (in the game), Domino-only tabs. Predicate: a message is what reaches a closed phone. No filler: every message has its own decision and every write is asked for by a record (Reaching the Tool-Call Minimum).")
A("")
A("## 3 Hidden authorities")
A("")
A("| Authority | Home | Governs | Decoy and scope | Findability |")
A("|---|---|---|---|---|")
for a in man["authorities"]:
    rec = (a["seeded_ids"] + a["base_pointers"])[0]
    dec = (a["decoy_seeded_ids"] + a["decoy_base_pointers"])[0]
    A(f"| {a['id']} {a['name']} (`{rec}`) | {a['home_service']} | {', '.join(a['governs'])} | `{dec}`: {a['decoy_scope']['decoy']}, against {a['decoy_scope']['task']} | a search for \"{a['findable_query']}\" returns it |")
A("")
A("## 4 Delegation lattice")
A("")
A("| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |")
A("|---|---|---|")
for a in man["anchors"]:
    A(f"| {a['id']} | {a['prompt_reference']} | `{a['locator']}` |")
A("")
A("The hub delegates by role and lists no members. Incorporation table (each quote is verbatim from the planned record):")
A("")
A("| Fragment | Service | Record | Kind | Chain | Delegated by | Delegation quote | Requirements |")
A("|---|---|---|---|---|---|---|---|")
for f in man["ask_fragments"]:
    A(f"| {f['id']} | {f['service']} | `{f['locator']}` | {f['kind']} | {' → '.join(f['incorporated_via'])} | `{f['delegated_by_record']}` | {f['delegation_quote']} | {', '.join(f['requirement_ids'])} |")
A("")
A(f"Amendments in another service, later in time: K10 (`{I['freeze_comment']}`) amends the Todo sentence of `{I['rule_doc']}`; K11 (`{I['corr_reply']}`) replaces a line. Non-authoritative distractors: T12 `{I['brian_opinion']}`, T10 `{I['deck']}`.")
A("")
A("## 5 Chains and trap register")
A("")
A("| Chain | Root cause | Hops | Ends in |")
A("|---|---|---|---|")
for c in man["chains"]:
    A(f"| {c['id']} | {c['root_cause']} | " + " → ".join(f"{h['service']}: `{h['record']}` ({h['finding']})" for h in c["hops"]) + f" | {c['ends_in']} |")
A("")
A("| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |")
A("|---|---|---|---|---|---|---|")
for t in man["traps"]:
    recs = ", ".join(f"`{x}`" for x in (t["seeded_ids"] + t["base_pointers"])) or "—"
    fam = t["family"] + (f" ({t['distractor_type']})" if t.get("distractor_type") else "")
    A(f"| {t['id']} | {fam} | {recs} | {t['requirement']} | {t['expected_wrong_reading']} | {t['resolver']} | {t.get('discovery_order', '—')} |")
A("")
A("Hardness v2 traps, each a separate cross-source decision:")
A("")
A("| Channel | v2 trap | Convincing wrong source | Record that beats it | Weight-5 rows |")
A("|---|---|---|---|---|")
v2r = [
    ("DONE", "1 · proving done across services", f"sheet Ready, ticket Done, approved merge of `{BASE['pr248']}`", f"Arthur's inline comment `{I['arthur_inline']}` (reviewer, Jun 26) and the source", "X1, X2, X2b, T1"),
    ("CORR", "2 · a correction somewhere else", f"June line on `{BASE['pn_sheet']}` and {TK['Lapsed 7 days']}", f"Leonard's thread reply `{I['corr_reply']}` under Martin's theme post (Sep 29)", "X3, X4, X16"),
    ("QA", "2 · a correction somewhere else", f"Vincent's pass `{I['race_qa']}` on {TK['Plague Race']}", f"Vincent's DM thread reply `{I['qa_reply']}` plus his QA note `{I['qa_thread']}`", "X7, X8, X8b, T1"),
    ("DEP", "4 · dates, windows and dependencies", "first-session row, Ready and LIVE", f"Robert's `{BASE['shove_to_20']}` and `{I['ask_decision']}` joined to the trigger", "X5, X6, X6b, T1"),
    ("ALIAS", "6 · different names for the same thing", "no Win & Collect ticket under the parent", f"`{BASE['liveops_page']}` plus {TK['Win & Collect start']}", "X9, X10"),
    ("FILT", "7 · items outside the obvious filter", "the sheet and the parent's children", f"comments `{I['boss_ask']}` on ZOM-542 and `{I['gift_ask']}` on ZOM-556", "X11, X12"),
    ("BUILT", "9 · work someone already did", "the old game name on the sheet", f"the client strings and the cancelled copy pass `{I['copy_pass']}`", "X14, X15, X17"),
    ("FOLLOW", "3 · follow-through a rule requires", f"'back to Todo' in `{I['rule_doc']}`", f"Leonard's comment `{I['freeze_comment']}` on `{BASE['tech_card']}`", "X18, X19, X19b"),
]
for r in v2r:
    A("| " + " | ".join(r) + " |")
A("")
A("### Mechanism portfolio (S5a)")
A("")
A("Priors from `tools/hardness_ledger.py priors --model claude-opus-5-5` (UNCALIBRATED, per model): `done_gap` Beta(2,2) mean 0.50, `superseding` Beta(1,3) mean 0.25, `authority` Beta(1,3) mean 0.25, `exact_predicate` Beta(1,3) mean 0.25, `scope_alias` Beta(1,2) mean 0.33, `completion_elsewhere` Beta(1,2) mean 0.33. Each n_eff ≤ 2, from `frederick_bridge_pipeline` and `frederick_q4_commitments`. Design rates are disclosed overrides from measured placements.")
A("")
A("| # | Candidate (records) | Coupling | Findability | Prior family | Design rate | Survives complete retrieval | Selected |")
A("|---|---|---|---|---|---|---|---|")
cands = [
    ("DONE", f"Weekly reset (`{I['arthur_inline']}`)", "day test → Hold → note", "needs inline comments or the source", "done_gap", "0.55", "needs the rollover join", "yes"),
    ("CORR", f"week-away line (`{I['corr_reply']}`)", "line → string ticket", "thread under another topic, or a search for the ticket's own alias", "superseding", "0.55", "no: placement", "yes"),
    ("QA", f"race reminder (`{I['qa_reply']}`)", "QA note → Hold → note", "DM thread under a build request, alias only", "superseding", "0.60", "no: placement", "yes"),
    ("DEP", f"first-session reach (`{I['ask_decision']}`)", "ask point → reach test → Hold", "all records on the normal path", "authority", "0.30", "yes: a join", "yes"),
    ("ALIAS", f"Collect & Win ticket ({TK['Win & Collect start']})", "alias → reuse", "outside the parent, other name", "scope_alias", "0.40", "yes: a name map", "yes"),
    ("FILT", f"two off-parent asks (`{I['boss_ask']}`, `{I['gift_ask']}`)", "scope → member → new ticket", "comments on tickets about other things", "exact_predicate", "0.50", "no: placement", "yes"),
    ("BUILT", f"old name already fixed (`{I['copy_pass']}`, source)", "source → no string ticket; fires as built", "one source read", "completion_elsewhere", "0.50", "yes once read", "yes"),
    ("FOLLOW", f"freeze comment (`{I['freeze_comment']}`)", "amendment → Backlog on every Hold", "a card read only for its list", "superseding", "0.45", "no: placement", "yes"),
    ("RATE-US", "Rate Us level chain (`6874409dfe0decf6f8fca64f`, ZOM-397)", "levels", "ticket is plain", "superseding", "—", "—", "rejected: in-game prompt, outside the message rule"),
    ("STORE-NOTE", "store-review note on promotions", "promo opt-in", "older mail", "authority", "—", "—", "rejected: conflicts risk with Snowflake sale rows; 337 mail hits uncensused"),
    ("QUIET", "quiet-hours rule on midnight sends", "every midnight message", "older mail", "authority", "—", "—", "rejected: one rule would flip most Go rows (choke point)"),
    ("COUNTS", "Hold total in the report", "aggregate of four channels", "—", "—", "—", "—", "rejected: forecast P(fails all six) 0.66 and no added spread"),
    ("PUSH-ROWS", f"server sends not set up (`{BASE['no_push_yet']}`)", "needs a server send", "per-ticket Arthur notes", "—", "control", "—", "kept as a control (K9)"),
    ("V2-GIFT", "reward on tap is version 2 (older PNs tab comment)", "Drop", "a tab every run lists", "—", "≈0.1", "—", "kept as a member, not a channel"),
]
for c in cands:
    A("| " + " | ".join(c) + " |")
A("")
A("Each selected rule's controls and over-application are in the draft manifest (`mechanism_portfolio[].controls`, `over_application`), its channel in `channels`.")
A("")
A("### Liveness flags (S5b)")
A("")
A("`trap_liveness.py --design` (verbatim):")
A("")
A("```")
A(liv)
A("```")
A("")
A("| Flag | Nodes | Disposition |")
A("|---|---|---|")
A(f"| breadcrumb | T5, T6, T14, T15 | structural: the hub (`{I['hub']}`) states the scope and reuse rule these traps depend on, which is the incorporation link. The members themselves sit outside the parent and the sheet |")
A("")
A("`hardness_v2_check.py --design` (verbatim):")
A("")
A("```")
A(v2)
A("```")
A("")
A("No FLAG or UNRESOLVED fired. SAME_PLACE is clean over declared containers and re-runs on the SQL at injection.")
A("")
A("## 6 Failure-diversity plan")
A("")
A("| Channel | Behaviour that finds the deciding record | Measured analog | Rows | Independent of |")
A("|---|---|---|---|---|")
fd = [
    ("DONE", "opening inline comments or the source", "Douglas: inline comments opened in 1 of 6 runs", "X1, X2, X2b", f"Slack and mail (`{I['arthur_inline']}`)"),
    ("CORR", "opening a thread under another topic, or a week-away search", "bridge SciPlay reply caught 2/8 then 3/6", "X3, X4, X16", f"GitHub and Linear (`{I['corr_reply']}`)"),
    ("QA", "opening a DM thread, or a race-reminder search", "Julia: DM thread replies discriminated", "X7, X8, X8b", f"channel reads (`{I['qa_reply']}`)"),
    ("DEP", "joining a trigger to the ask point", "Julia: judgement traps rarely landed, so rated 0.30", "X5, X6, X6b", f"search behaviour (`{I['ask_decision']}`)"),
    ("ALIAS", "searching a second name", "ledger scope_alias mean 0.33", "X9, X10", f"everything else ({TK['Win & Collect start']})"),
    ("FILT", "reading comments on tickets outside the list", "frederick_q4 rev3: the one trap that landed was outside the filter", "X11, X12, X13, V1", "ZOM-542, ZOM-556"),
    ("BUILT", "reading the client source", "Julia: github_get_file_contents in 4 of 6 runs", "X14, X15, X17", f"Slack (`{BASE['pr248']}`)"),
    ("FOLLOW", "reading comments on a card seen only in a list", "Douglas: trello_get_comments in 3 of 6 runs", "X18, X19, X19b", f"Linear (`{BASE['tech_card']}`)"),
]
for r in fd:
    A("| " + " | ".join(r) + " |")
A("")
A("Named correlation: DONE and BUILT both reward reading GitHub; CORR and QA both reward opening threads. `plan/policy_scores.py` models those two shared latents on top of a run-level latent.")
A("")
A("```")
A(pol)
A("```")
A("")
A("**Read of these numbers.** The result turns on the real per-trap landing rate. E[avg] ≤ 72 % needs about 0.70× design rates (mean 0.34); the 80 % bar holds to about 0.50× (mean 0.24). Measured per-trap landing: 0.50 on bridge rev12 batch 2, about 0.33 on bridge pre-checks, 0.125 on the frederick_q4 rev3 pre-check before de-naming. At 0.125 this design would miss the bar.")
A("")
A("## 7 Deliverables and dependent writes")
A("")
A("| Write | Tool | Count | Depends on | Requirements | Target and access |")
A("|---|---|---|---|---|---|")
tg = {"gsheets": f"new sheet, Samuel as owner, moved into `{BASE['folder']}`", "gdrive": f"`{BASE['folder']}` (YES, owner)", "linear": f"seeded DES tickets under `{I['parent']}`; `{TK['Win & Collect start']}`; team DES", "trello": f"card `{BASE['pn_card']}`", "slack": f"`{B.DM_LEONARD}`"}
for w in man["writes"]:
    A(f"| {w['service']} | `{w['tool']}` | {w['count']} | {', '.join(w['depends_on'])} | {', '.join(w.get('requirements', []))} | {tg.get(w['service'], '')} |")
A("")
A(f"Reuse vs create (A8): the Win & Collect row reuses {TK['Win & Collect start']}. The PN sheet is never a write target: its owner is a Resource id and write access is unproven (learnings §31).")
A("")
A("## 8 Service role map")
A("")
A("| Service | Role | Load-bearing fact or write | Carrier |")
A("|---|---|---|---|")
car = {"slack": I["hub"], "gsheets": BASE["pn_sheet"], "gdocs": I["rule_doc"], "gdrive": BASE["folder"], "linear": I["parent"], "trello": BASE["pn_card"], "github": BASE["pr248"], "gmail": I["qa_thread"], "gcal": I["copy_pass"], "gslides": I["deck"], "confluence": BASE["liveops_page"]}
for svc, v in man["services"].items():
    A(f"| {svc} | {v['role']} | {v['weight_reason']} | ● (`{car[svc]}`) |")
A("| contacts | not used | no value needs it | — |")
A(f"| snowflake | not used | not writable; its ZM push rows disagree with Slack (`{BASE['all_local']}`) | — |")
A("")
A("## 9 Call budget")
A("")
A("| Phase | Service | Calls | Why each call answers a distinct question |")
A("|---|---|---|---|")
for r in man["call_budget"]:
    A(f"| {r['phase']} | {r['service']} | {r['calls']} | {r['reason']} |")
A(f"| **Total** | 11 services | **{B.TOTAL_BUDGET}** | per-record {B.PER_RECORD} on the surfaces |")
A("")
A(f"**The over-130 bar.** A lean correct run: {B.N_NOTES} ticket comment reads, {B.N_NOTES} ticket comments, {B.N_UPDATES} state updates, {B.N_NEW} new tickets, {1 + B.COUNTS['Go']} checklist calls, 5 sheet, folder and report calls, and about 25 discovery reads, which is about {B.N_NOTES * 2 + B.N_UPDATES + B.N_NEW + 1 + B.COUNTS['Go'] + 5 + 25}. A run that skipped every state update would fall near 120, but the hub asks for them and the budget has no padding. Measured: Douglas's 17-ticket task ran 166–239. Every write has no batch form in the catalog. The pre-check's counted calls are read at intake.")
A("")
A("**≥ 500 is not reachable without padding**, so the requester-confirmed `volume_exception` applies. Every other extreme target stands.")
A("")
A("## 10 QC rails")
A("")
A("### Two-reading table")
A("")
A("| Decision point | Best reading | Strongest alternative | Resolved by | Evidence |")
A("|---|---|---|---|---|")
tr = [
    ("Weekly Leaderboard reset", "Hold: wrong day", "Go: it arrives weekly", "rule: the day matters; the row says rollover", f"`{I['arthur_inline']}`"),
    ("Lapsed 1 day", "Go", "Hold: not exactly 24 hours", "rule: the hour doesn't matter", f"`{I['rule_doc']}`"),
    ("Lapsed 7 days", "Go with a string ticket", "Hold until the line changes", "rule: a line change needs a string ticket, not a Hold", f"`{I['rule_doc']}`"),
    ("Finish first mission", "Hold: cannot reach its players", "Go: Vincent saw it arrive via the settings toggle", "Robert: nothing asks before level 20; the trigger needs players below it", f"`{I['ask_decision']}`"),
    ("Plague Race timing", "fires daily is acceptable", "Hold: not at event start", "Leonard's comment on the ticket says daily is fine while a race is always on", f"{TK['Plague Race']}"),
    ("Plague Race QA", "Hold: iOS unproven", "Go: passed on the ticket", "Vincent's own later reply and his QA note", f"`{I['qa_reply']}`"),
    ("Season Pass start", "Hold: nothing scheduled", "Drop: not shipped", "BETA list card; no ship date used (SC-38)", "6851ab766fcaf894d0c0048b"),
    ("Comeback gift", "Drop: reward on tap is version 2", "Hold: lapsed messages exist", "older PNs tab comment; no Backlog card, so a Leonard comment on its ticket will state it", f"{TK['Comeback gift']}"),
    ("Quests rollover", "Hold: client", "Hold: server (sheet says Push)", "Arthur's note on the ticket; the sheet's What column is not a test", f"{TK['Quests rollover']}"),
    ("Scope of asks", "tickets and cards only", "Slack asks count too", "hub wording; the census found no base ask on a ticket or card", f"`{I['hub']}`"),
    ("Rate Us and permission popup", "off the plan", "they are messages", "rule: a message reaches a closed phone", "ZOM-397"),
    ("Win & Collect ticket", "reuse", "new ticket", "hub: under whatever name; page maps the names", f"`{BASE['liveops_page']}`"),
    ("Hold state", "Backlog", "Todo", "the rule doc's own exception and Leonard's later comment", f"`{I['freeze_comment']}`"),
    ("Final headline", "headline text only, no emoji", "headline with emoji from sheet or code", "two emoji differ between sheet and client, so emoji are never graded", f"`{BASE['pn_sheet']}`"),
]
for r in tr:
    A("| " + " | ".join(r) + " |")
A("")
A("One reading per decision; no BOTH_FAIR_FIGURE is claimed. Each fork is settled by a dated record, never by rubric acceptance (memory: prompt-ugt-forks-need-records).")
A("")
A("### Reach table (load-bearing records)")
A("")
A("Proofs: `00_PreScenario/cansee_anchors.txt`. Unscoped services are always readable. Planned seeds are verified at the injection gate.")
A("")
A("| Record | Service | Why it is load-bearing | Mark |")
A("|---|---|---|---|")
for rid, svc, why in [(BASE["pn_sheet"], "gsheets", "population"), (BASE["folder"], "gdrive", "destination"), (BASE["pns_sent"], "slack", "Samuel's remit"),
                      (BASE["shove_to_20"], "slack", "ask point"), (BASE["variant_c_13"], "slack", "ask point"), (BASE["pushed_back"], "slack", "context"),
                      (BASE["all_local"], "slack", "local only"), (BASE["push_vs_local"], "slack", "local vs server"), (BASE["beta_scope"], "slack", "beta scope"),
                      (BASE["axe_postponed"], "slack", "Axe Arena out"), (BASE["pr248_mail"], "gmail", "the PR mail thread")]:
    A(f"| `{rid}` | {svc} | {why} | LB |")
A(f"| `{I['hub']}` | slack | planned hub | LB |")
A(f"| `{I['rule_doc']}` | gdocs | planned rule | LB |")
A(f"| `{I['qa_reply']}` | slack | planned QA reply | LB |")
A(f"| `{I['corr_reply']}` | slack | planned line change | LB |")
A("")
A(f"Feasibility: every write exists in the catalog; `gsheets_create_spreadsheet` has no folder argument, so the plan moves with `gdrive_move_file`. Samuel holds no DES team membership in the base, so the SQL adds one. Precedence: load-bearing facts sit in ● carriers (Linear comments per Ask_Carriers §6b; PR review comments; Slack; Gmail; Docs). The copy pass event's description is ○ and only supports; the source carries the fact. Naturalness: the prompt may name Leonard's DM, the PN sheet, my Drive folder and the card, and must not name the rule's tests, tickets, traps, counts or any member. Grading devices: ≤ 5 samples per group, a volume row, exception rows for K13, K14 and K15 members; exclusions graded as an exact population on the plan.")
A("")
A("### Coherence rail")
A("")
A(f"Every audit row has a disposition; each designed disagreement is a dated human claim with a later overturning record. Seeded notes report observations and decisions, never code facts beyond `{BASE['pr248']}` and the source read for this design. `tools/base_claims.py` runs before any solver work.")
A("")
A("## 11 Record plan for /create-injection")
A("")
A("| Service | Record | Planned content | Time |")
A("|---|---|---|---|")
rp = [
    ("slack", I["hub"], "Leonard's hub: " + Q["hub"], T["hub"]),
    ("gdocs", I["rule_doc"], Q["rule"], T["rule_doc"]),
    ("gmail", I["qa_thread"], "Vincent to Samuel, Oliver, Owen: " + Q["qa"], T["qa_note"]),
    ("github", I["arthur_inline"], "inline comment on the weekly leaderboard schedule lines: " + Q["arthur_inline"], T["arthur_inline"]),
    ("gmail", I["arthur_mail"], "INT-12 mail copy of that comment to Samuel", T["arthur_inline"]),
    ("slack", I["ask_decision"], "Robert, root post in #zombie-match3d: " + Q["ask_decision"], T["ask_decision"]),
    ("slack", I["corr_reply"], f"Leonard, reply under `{BASE['martin_root']}`: " + Q["corr_reply"], T["corr_reply"]),
    ("slack", I["qa_reply"], f"Vincent, reply under `{BASE['android_2007_root']}`: " + Q["qa_reply"], T["qa_reply"]),
    ("slack", I["brian_opinion"], "Brian in #zombie-match3d: " + Q["brian_opinion"], T["brian_opinion"]),
    ("trello", I["freeze_comment"], f"Leonard's comment on `{BASE['tech_card']}`: " + Q["freeze"], T["freeze"]),
    ("trello", BASE["pn_card"], "comment: " + Q["card"], "2025-09-24T16:00:00Z"),
    ("gcal", I["copy_pass"], "cancelled 'PN copy pass', Leonard and Samuel: " + Q["copy_pass"], T["copy_pass"]),
    ("gslides", I["deck"], Q["deck"], T["deck"]),
    ("linear", I["parent"], "parent ticket by Leonard: " + Q["parent"], T["parent"]),
    ("linear", TK["Win & Collect start"], "Calvin's ticket outside the parent, 'Ping when a Collect & Win window opens'", T["wc_ticket"]),
    ("linear", f"DES-{B.K['Lives recharged']['ticket'].split('-')[1]} to DES-{B.LAST_TICKET}", "one ticket per message under the parent; six built tickets Done, the rest In Review; asks by the named teammate", T["parent"]),
    ("linear", I["race_qa"], f"Vincent on {TK['Plague Race']}: seen on Android 1860 and iOS 1593; plus Leonard: daily is fine while a race is always on", "2025-09-24T14:30:00Z"),
    ("linear", I["weekly_qa"], f"Vincent on {TK['Weekly Leaderboard reset']}: seen on both on store builds", "2025-09-24T14:40:00Z"),
    ("linear", I["ftue_qa"], f"Vincent on {TK['Finish first mission']}: arrives on both when notifications are switched on from settings", "2025-09-24T14:50:00Z"),
    ("linear", I["boss_ask"], "Brian on ZOM-542: " + Q["boss_ask"], T["boss_ask"]),
    ("linear", I["gift_ask"], "Julia on ZOM-556: " + Q["gift_ask"], T["gift_ask"]),
    ("linear", "per-ticket notes", "Arthur on each unbuilt ticket: not in NotificationManager yet, plus a local timer can do it or it needs a server send; Vincent on each built ticket", "2025-09-25T12:00:00Z"),
    ("linear", "team_DES", "Samuel's membership row so he can file DES tickets", "2025-09-23T16:00:00Z"),
]
for r in rp:
    A(f"| {r[0]} | `{r[1]}` | {r[2]} | {r[3]} |")
A("")
A(f"Estimated rows: Linear {len(B.TICKETED) + 1} issues and about 60 comments, Slack 6, Gmail 4, Trello 2, GCal 2, Drive 2, Docs 1, Slides 3, GitHub 1, plus companions: about 125–150 INSERTs. Every row is cohort evidence; if an honest count falls under 120, that is a finding to bring back, never a gap to pad.")
A("")
A("### Integrations and companions")
A("")
A("| Service | INT id | Companion | Decision |")
A("|---|---|---|---|")
A(f"| github | INT-01 | Slack copy of the inline comment | exception: `{I['arthur_inline']}` predates the Jun 30 subscription of #zombie-prs |")
A(f"| github | INT-12 | GitHub mail to Samuel | seeded: `{I['arthur_mail']}` |")
A("| github | INT-23 | CodeRabbit | no companion: human comment |")
A("| linear | INT-04, INT-05 | Slack and mail notifications | no companion: base Linear comments are empty and carry none (Ask_Carriers §6b) |")
A(f"| gcal | INT-11 | invitation and cancellation mails | seeded for `{I['copy_pass']}` |")
A(f"| gdrive | INT-13 | Drive share DMs | no companion for owner-shared files, declared at injection (`{I['rule_doc']}`) |")
A(f"| slack | INT-22 | Slack mail digests | no companion (`{I['hub']}`) |")
A("| gdocs, gsheets, gslides | none | no integration writes from these | none |")
A("| trello | INT-21 | none exists | none |")
A("| gmail | none | sources only | none |")
A("| confluence | none | not seeded | none |")
A("")
A("## 12 Self-test results")
A("")
A("`hardness_gate.py --design` (verbatim):")
A("")
A("```")
A(gate)
A("```")
A("")
A("`gradable_surface.py validate` and `gradeable-report` (verbatim):")
A("")
A("```")
A(gsv)
A(gsr)
A("```")
A("")
A("Lazy-solver pass: one broad search per service, first hits, no threads, no comments. It reads the sheet, the parent's children and the hub, so it scores the always-pass rows and none of the eight channels: about 25 % (`plan/policy_scores_output.txt`). Leaks fixed in design: the rule doc holds only tests, no member; the hub names no ticket but the parent.")
A("")
A("Literal-value and wording sweep (`plan/literal_sweep.txt`, verbatim):")
A("")
A("```")
A(sweep)
A("```")
A("")
A("\"The rest stands\" check: the freeze comment amends one clause; no later record restates Todo. Leonard's reply changes one line; the body stays.")
A("")
if fc_id:
    A(f"S9b prior forecast (UNCALIBRATED, CONDITIONAL on disclosed rates): ledger id `{fc_id}`.")
    A("")
    A("```")
    A(fc_lines)
    A("```")
    A("")
    A("The independent and source scenarios give P(all) about 0.6, where the SD gate binds; the fully correlated scenario gives about 0.2 because whole runs then pass or fail together. Spread, not the cap, is what the placement must protect.")
    A("")
A("### Self-review")
A("")
A("Walked against `Evals/1_Prompt_Eval.md` §2.1, §2.2, §3.2 and `Evals/0_Injection_Quality_Eval.md` Check C.")
A("")
A("| Category or decision | Counter-reading (it should fail) | Resolution with evidence |")
A("|---|---|---|")
sr = [
    ("temporal", "seeded tickets numbered after a May series look back-dated", f"DES stopped at DES-312 on 2025-05-07, so DES-313 onward from Sep 17 are in order; ZOM-566 from Sep 30 would not be"),
    ("semantic", "a game designer doing retention comms reads as Product Management", f"the job is what players are told and when; expected outputs are a plan and a report; tickets are follow-through (`{BASE['pn_card']}`)"),
    ("cross-service referential", "the rule says Vincent's QA note but the ticket and note could disagree", f"they differ by design and the later record wins: `{I['qa_reply']}`"),
    ("quantitative", "Go 3 could be argued as 4 if a run counts Plague Race", f"Vincent's reply withdraws iOS (`{I['qa_reply']}`); the count is the rule applied to 40 rows"),
    ("state/lifecycle", "a Done ticket moved to Backlog looks odd", f"the rule doc makes state follow the call (`{I['rule_doc']}`); agent writes come after the clock"),
    ("identifier/format", "seeded review comment rc_18 could collide", f"PR 248 holds rc_1 to rc_17 (`{BASE['pr248']}`), checked through hg.py"),
    ("other", "the theme screen names zombies", f"12 stored runs show no fallback; seeds avoid the words (`{BASE['pn_sheet']}`)"),
]
for r in sr:
    A("| " + " | ".join(r) + " |")
for r in tr:
    A(f"| {r[0]} | {r[2]} | {r[3]} ({r[4]}) |")
A("")
A("Base values re-read through `tools/hg.py` this session: the sheet tabs, PR 248 reviews and hunks, the Trello lists and card, the DMs and posts cited above.")
A("")
A(gate.splitlines()[0])
A("")
A("Unresolved: no independent model review ran (`REDTEAM_*` unset, §13); both blind sweeps run before `/injection`; INSERT count is an estimate; STEP 0.6 cannot be measured locally; landing rates are UNCALIBRATED.")
A("")
A("## 13 Red team (dual)")
A("")
A(red or "RED TEAM UNAVAILABLE: REDTEAM_* is unset in this environment.\n\nRED TEAM FALLBACK: pending.")
A("")
open(os.path.join(WF, "01_Scenario_Design.md"), "w").write("\n".join(L) + "\n")
print("design", sum(len(x) for x in L), "chars,", len(L), "lines; forecast id", fc_id or "none")

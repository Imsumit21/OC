#!/usr/bin/env python3
"""Assemble Working_Files/01_Scenario_Design.md from the builder's ids/manifest/surface and the pasted tool outputs.
Design only: contains no prompt, Oracle Event or criterion text. Re-run after build_scenario.py."""
import json, os, subprocess, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
sys.path.insert(0, HERE)
import build_scenario as B  # noqa: E402  (re-runs the builder: same deterministic output)

man = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json")))
surf = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))
I, BASE, T, Q = B.IDS, B.BASE, B.T, B.Q
ENV = {**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"}


def run(args):
    p = subprocess.run(args, cwd=WS, capture_output=True, text=True, env=ENV)
    return (p.stdout + p.stderr).rstrip()


def rd(rel):
    return open(os.path.join(WF, rel)).read().rstrip()


# per-member minted ids (record plan)
PAPER = {}
THREAD = {}
for m in B.M:
    if m["decision"] == "out" or m.get("base"):
        continue
    k = m["key"]
    THREAD[k] = {"Framewell": I["framewell_thread"], "Pingwise": I["pingwise_thread"], "Clipforge": I["clipforge_thread"],
                 "Pixel Harbor Events": I["pixel_thread"], "Lanternfly Publishing": I["lanternfly_thread"],
                 "Motive Forge": I["motive_thread"], "Spotlight Fest": I["spotlight_thread"]}.get(k) or B.gm(B.thread("member:" + k, "2025-09-01T16:00:00Z"))
    if m["paper"]:
        PAPER[k] = I["lanternfly_deck"] if k == "Lanternfly Publishing" else B.drive("paper:" + k)
json.dump({"threads": THREAD, "papers": PAPER}, open(os.path.join(HERE, "member_ids.json"), "w"), indent=1)

reach = rd("00_PreScenario/reach_frederick.txt")
ent_c = open(os.path.join(HERE, "entity_collisions.txt")).read().rstrip()
ent_r = open(os.path.join(HERE, "entity_resolve.txt")).read().rstrip()
ent_f = rd("00_PreScenario/entity_frederick.txt")
gate = run(["python3", "-B", "Task_Authoring/tools/hardness_gate.py", "Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.draft.json", "--design"])
gsv = run(["python3", "-B", "Task_Authoring/tools/gradable_surface.py", "validate", "--task-dir", "Task_Authoring/task_inputs"])
gsr = run(["python3", "-B", "Task_Authoring/tools/gradable_surface.py", "gradeable-report", "--task-dir", "Task_Authoring/task_inputs"])
v2 = open(os.path.join(HERE, "hardness_v2_check.txt")).read().rstrip()
liv = open(os.path.join(HERE, "trap_liveness.txt")).read().rstrip()
pol = open(os.path.join(HERE, "policy_scores_output.txt")).read().rstrip()
fc = open(os.path.join(HERE, "forecast_output.txt")).read()
fc_id = [l for l in fc.splitlines() if "forecast record" in l][-1].split("'id': '")[1].split("'")[0]
fc_lines = "\n".join(sorted({l for l in fc.splitlines() if "whole    V3" in l or l.strip().startswith("V3:")}))
cansee = rd("00_PreScenario/cansee_anchors.txt")

L = []
A = L.append
A("# Scenario Design — frederick_q4_commitments · design only · contains no prompt, OE or criterion text")
A("")
A("Written 2026-11-03 by `/create-scenario` (Claude Opus 5.5); revised 2026-11-04 by `/create-scenario --revise` (design-2, after the rev3 Opus pre-check: §14). Builders: `Working_Files/plan/build_scenario.py` (manifest, "
  "surface, ids), `plan/assemble_design.py` (this file), `plan/policy_scores.py` (UNCALIBRATED scores). Learnings applied: "
  "`Working_Files/00_Completed_Task_Learnings.md` (the three completed Frederick tasks) and `00_Pre_Scenario_Analysis.md`.")
A("")
A("## 0 Assignment, persona census and horizon note")
A("")
A("| Field | Value |")
A("|---|---|")
A(f"| Universe | key `{B.CTX['universe']['key']}`, label {B.CTX['universe']['label']}, `{B.CTX['universe']['clock_line']}`; seed bound `freeze_utc` {B.CTX['freeze_utc']} (Tue Sep 30 17:00 PT); `shutdown_rules_apply` {str(B.CTX['universe']['shutdown_rules_apply']).lower()} |")
A(f"| Assignment | Executive · Frederick Stone (Co-founder, `frederick.stone@harmonygames.co`) · Corporate Ops · Actions · long-horizon · easy · October 1, 2025 07:00 (context_hash `{B.CTX['context_hash'][:12]}`) |")
A("| Evals category | Founders / Exec / Strategy (`Evals/references/rules/task_categories.md`: strategic decisions, priorities and executive coordination) inside Corporate Ops (vendor, legal/contracts) |")
A("| Loss budget | Easy cap < 90 %; requester target < 80 % (author_targets in the draft manifest); design target E[avg] ≤ 72 % |")
A("| Horizon | Long Horizon → `effective_profile: extreme`; requester target > 130 counted calls in every run; `volume_exception {call_budget_floor 200, per_record_floor 90}` (honest budget 237, lean correct run ≈ 150) |")
A("| Theme screen | no bio-adjacent theme in the storyline or seeded text (vendors, partners, contracts) |")
A("| Role remit | Frederick is a co-founder (roster) and the Commercial Lead who owns the external vendor and partner portfolio (persona brief; Contacts `175c0d7bc72ed244b944cb90` 'Commercial Lead, Marketing & Business Development'). Leonard is in LA on Oct 1 for the Dentsu meeting (`C07C2866011/1758739727.864319`) and hands him the vendor/partner side under the founders' Sep 15 and Sep 24 runway decisions (`C07C2866011/1757961037.465799`, `C07C2866011/1758739409.488879`) |")
A("")
A("Persona reach census (`persona_view.py reach frederick_stone --top 10`, verbatim):")
A("")
A("```")
A(reach)
A("```")
A("")
A("Identities (`entity.py resolve \"Frederick Stone\"`): Linear `usr_175c0d7bc72ed244`, Trello `4b4a68fc0fec0b254e4f9d8e`, Confluence "
  "`user_EMPLOYEE_0008`, Drive root `d_175c0d7bc72ed244b944cb` (owned). GitHub login shows 'Ryan' (S04): GitHub carries no row.")
A("")
A("## 1 Storyline")
A("")
A("Before flying to LA, Leonard hands Frederick everything outside the investor work that is waiting on Harmony Games: offers, trials, quotes, terms and partner asks "
  "that one of the founders engaged with. Frederick applies the founders' runway guardrails to each (Answered / End / Keep / Sign / Park), answers each "
  "company, routes signatures to Leonard or Arthur and counsel, sets revisit reminders, files contacts, logs it in his Q4 commitments folder and reports "
  "what stays and what waits on a signature. 46 companies are looked at; 36 pass the scope rule.")
A("")
A("- Timeline (`references/universe_kb/by_universe/synthcut/timeline.md`): the window sits after the Sep 3 bridge launch "
  "(`C07C2866011:1756749288.785249`) and inside the founders' late-September runway discussion (`C07C2866011/1758739409.488879`). Synth-cut, no shutdown premise: the company operates normally and only freezes new cash commitments.")
A("- cohorts.json: no fit — every KB cohort is a Linear issue set (LIN-*), and this cohort is outside companies with offers in mail, papers and calls (defined by the hub `" + I["hub_thread"] + "`).")
A("- trap_catalog precedents: C01 (thread replies that correct: Framewell `" + I["framewell_waiver_reply"] + "`), B02 (automated senders: Clipforge's processor notice `" + I["clipforge_notice_thread"] + "`), "
  "D04 (spreadsheets with lookalike titles: the template `" + I["template_sheet"] + "` vs the July tracker `" + I["tracker_sheet"] + "`), P01 (shared first names: no seeded external person shares an HG first name, entity output §1c).")
A("- Base anchors Frederick can see: Balancy `" + BASE["balancy_thread"] + "`, Nintendo `" + BASE["nintendo_regdone"] + "` and `" + BASE["nintendo_ndareq"] + "`, his Switch post `" + BASE["fred_nintendo_post"] + "`, "
  "the Playtestcloud root `" + BASE["playtestcloud_root"] + "`, the ESG engagement `" + BASE["esg_engagement"] + "`, founders' board `" + BASE["browserstack_card"] + "` (card on board `640643a3fd8f3ca308d9318e`).")
A("- Boundary anchors (excluded by the hub's rule): Rayking `" + BASE["rayking_thread"] + "` (Frederick's Sep 4 reply went to Leonard), Playable Factory `" + BASE["playable_factory_thread"] + "`, Gamesforum `" + BASE["gamesforum_thread"] + "`, "
  "InterCo `" + BASE["interco_thread"] + "`, Google partner `" + BASE["google_thread"] + "`, Singular `" + BASE["singular_renewal"] + "` (SC-39), NCsoft `" + BASE["ncsoft_report"] + "`, Dentsu `" + BASE["dentsu_thread"] + "`, Mattel `" + BASE["mattel_rfp_post"] + "`.")
A("- Natively spans gmail, slack, gcal, gdrive, gdocs, gsheets, trello, contacts (8: e.g. `" + BASE["balancy_thread"] + "`, `C07C2866011`); injection adds linear (ZOM-567) and gslides (`" + I["lanternfly_deck"] + "`) with load-bearing roles (10 injected, all used; Confluence never carries a fact, learnings §26).")
A("")
A("## 1a Coherence audit")
A("")
A("Scope = every record a correct run opens. Walked against `references/universe_kb/by_universe/synthcut/coherence_hazards.json` and the known-data-issue cards `references/known_data_issues/synthcut.md`.")
A("")
A("| Record | Category | Fields | Pointer | Hazard / card | Disposition |")
A("|---|---|---|---|---|---|")
rows = [
    ("Balancy thread message order", "temporal", "message dates", BASE["balancy_thread"], "hazard T02", "fold: no seed appended; the agent reads dates, not order"),
    ("seeded threads' date format", "identifier/format", "date header", I["framewell_thread"], "hazard I04", "fold: seeded Gmail rows use the RFC-2822 form of their mailbox's neighbours"),
    ("Frederick's GitHub display name", "semantic", "name", "frederick.stone@harmonygames.co/1842359398719557772", "hazard S04", "avoid: GitHub carries no row"),
    ("seeded calendar events with invitation mails", "cross-service referential", "summary ±1 day", I["review_event"], "hazard R08", "fold: each seeded event gets its INT-11 invitation mail in every attendee mailbox"),
    ("Slack links to Docs", "cross-service referential", "doc ids in links", I["amendment_root"], "hazard R04", "avoid: seeded Slack names documents by title, never by link"),
    ("Playtestcloud root reply counters", "quantitative", "reply_count / latest_reply", BASE["playtestcloud_root"], "hazard Q01", "fold: SQL updates the root's counters for Leonard's reply (manifest hazard_acknowledgements Q01, dated_claim)"),
    ("DM localization root reply counters (rev4)", "quantitative", "reply_count / latest_reply", BASE["dm_localization_root"], "hazard Q01", "fold: SQL updates the Sep 17 DM root's counters for Leonard's Sep 29 thread reply (second Q01 acknowledgement)"),
    ("Spotlight call description (rev4)", "cross-service referential", "description", I["spotlight_call"], "none (○ carrier)", "fold: the description no longer states the answer; Robert's ● note carries it alone, so the two cannot disagree"),
    ("Hootline thread without a filed paper (rev4)", "cross-service referential", "attachments / paper", I["hootline_thread"], "none", "fold: the terms are in the mail body, and no message says 'attached', so no missing-attachment claim exists"),
    ("ESG note copies in four mailboxes", "quantitative", "body", I["esg_thread"], "hazard Q10", "fold: one identical body per mailbox copy"),
    ("ZOM-567 assignee at the clock", "state/lifecycle", "assignee", "ZOM-567", "hazard L08", "avoid: ZOM-567 has no assignee (creator Arthur), so no open issue sits on a person quiet after the clock"),
    ("keep-running card list", "state/lifecycle", "list / checklist", I["keep_card"], "hazard L12", "avoid: the card sits in Doing with open checklist items, never in Done"),
    ("Frederick's mailbox file alias", "identifier/format", "file name", "frederick@harmonygames.co_1842348778705877030.json", "hazard I03", "fold: seeded threads follow the frederick@ file alias with frederick.stone@ ids"),
    ("Singular payment plan", "quantitative", "plan terms", BASE["singular_renewal"], "card SC-39", "excluded: the hub keeps Singular off the log; no row grades its plan"),
    ("Frederick's founder status", "semantic", "role", "Contacts 175c0d7bc72ed244b944cb90", "card SC-49", "excluded: no row grades founder status"),
    ("channel membership", "state/lifecycle", "members", "C07C2866011", "card SC-7", "excluded: no row grades who is in a channel"),
    ("Frederick's pay", "quantitative", "ledger", "snowflake.FINANCE_LEDGER", "card SC-54", "excluded: no money row reads payroll"),
    ("Rayking 'reply' addressed to Leonard", "other", "To header", BASE["rayking_thread"], "none (base quirk)", "designed boundary: the hub's 'only forwarded around internally' clause settles it (T18)"),
    ("Mattel RFP open at the clock", "other", "deadline", BASE["mattel_rfp_post"], "none in scope", "excluded by the hub (Leonard keeps it)"),
    ("Dentsu meeting at 13:30 PT Oct 1", "temporal", "start", BASE["dentsu_thread"], "none in scope", "excluded: investor work"),
]
for r in rows:
    A("| " + " | ".join(r) + " |")
A("")
A("Six hazard categories in scope: temporal T02; semantic S04; referential R08, R04; quantitative Q01, Q10; state/lifecycle L08, L12; identifier/format I04, I03.")
A("")
A("**Sibling-defect sweep.** Designed defects are a superseded price (Framewell), an unanswered follow-up already answered elsewhere (Lanternfly), a moved pilot end (Clipforge), "
  "a done claim with a missing acceptance (Nintendo). Siblings checked: other vendor threads in Frederick's mailbox with an unanswered follow-up "
  "(Playable Factory `" + BASE["playable_factory_thread"] + "`, InterCo `" + BASE["interco_thread"] + "`) are cold pitches and stay off by the scope rule; "
  "no other base portal mail claims registration (`" + BASE["nintendo_ndareq"] + "`); no base vendor has a waiver or a moved end date (name census `plan/name_census.json`, positive control Balancy found in gmail/slack/gdrive).")
A("")
A("## 1b Active speakers")
A("")
A("Status from `references/universe_kb/by_universe/synthcut/activity.json` (status_at_clock).")
A("")
A("| Person | Email | status_at_clock | Seeding role |")
A("|---|---|---|---|")
A("| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | hub mail, guardrails doc, Sep 29 amendment, Framewell thread reply (names Maren), Lanternfly DM thread reply (names Wen), Jan 5 review event, July signing note, ESG reply, folder README and template |")
A("| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | keep-running card (Aug 12), ZOM-567 and its Sep 25 comment, Motive Forge decline |")
A("| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | 'cancel everything' #executives post (distractor), Sep 17 showcase note (names the Dec 5 indie showcase and Rina) |")
A("| Frederick Stone | frederick.stone@harmonygames.co | active_sep_2025_quiet_in_oct | persona: July tracker sheet, UA-buckets decoy doc, Lanternfly Sep 10 reply, the Q4 commitments folder |")
A("| ESG Law partner | PERSON_2694_EMAIL | external (not in activity.json; base signature 'PARTNER, ESG Law' in mailbox file frederick@harmonygames.co_1841636073974841484.json) | signing note, intake checklist |")
A("| 33 counterparty people | e.g. maren@framewell.io, dana@pingwise.io | external, seeded with no base footprint (plan/name_census.json) | offers, notices, follow-ups |")
A("")
A("## 1c Identity traps")
A("")
A("```")
A(ent_c)
A("")
A(ent_f)
A("")
A(ent_r)
A("```")
A("")
A("- Leonard Hayes (leonard.hayes@harmonygames.co) vs the subject 'Leonard Hayes from SEMC' (`frederick.stone@harmonygames.co/1842279098258817066`): no seed names SEMC.")
A("- Seeded external first names avoid every HG first name (Leonard, Arthur, Robert, Frederick, Julia, Brian, Douglas, Owen, Oliver, Martin, Claire, Calvin, Marcus, Simon, Samuel, Oscar, Felix, Vincent, Victor, Thomas, Tim, Elliot, Lucas, Matthew) — P01.")
A("- ESG reuses the base tokens PERSON_2694 (partner) and PERSON_2599 (group intake), whose roles are stated in `frederick.stone@harmonygames.co/1841636073974841484` (learnings §14).")
A("")
A("## 2 Cohort spine")
A("")
A("- Rule (hub `" + I["hub_thread"] + "`): every outside company with an offer, a trial, a quote, terms or an ask in front of HG that one of the founders engaged with (a call, a reply, a sign-up or paper); off: cold pitches nobody answered (including ones only forwarded internally), ad networks and Singular, investors, Mattel, withdrawn offers.")
A(f"- Size: 46 looked at, 36 kept (Answered 4 · End 10 · Keep 3 · Sign 7 · Park 12); key = company; planned ids `plan/member_ids.json`.")
A("- Surfaces and shortcut audit (manifest cohort.evidence_surfaces):")
for s in man["cohort"]["evidence_surfaces"]:
    A(f"  - {s['service']} · `{s['tool']}` · {s['per_record_calls']} × {s['records']} · decides: {s['decides']} · no bulk: {s['why_no_bulk']} · short-circuit: {s['short_circuit']} (`{I['hub_thread']}`)")
A("- Predicate: the five decisions are a closed set in the guardrails doc `" + I["guardrails_doc"] + "`, applied top to bottom: already answered → cash test (unless on Arthur's keep-running list) → signing → park.")
A("- House rule over the natural reading (A15): the keep-running exemption (`" + I["keep_card"] + "`) and the Sep 29 travel amendment (`" + I["amendment_root"] + "`).")
A("- Boundary records (A17): Pixel Harbor's June quote `" + I["pixel_thread"] + "` (in, outside the September window), Hootline `" + I["hootline_thread"] + "` (in: Aug 5 sign-up and Aug 12 ask, no paper, nothing later — WIN), Rayking (out, forwarded internally), Nova Rewards `" + I["nova_thread"] + "` (out, withdrawn), July tracker `" + I["tracker_sheet"] + "` (stale shorter list).")
A("- Necessity: 13 of 32 papers decide their company's decision (cost, conversion date, auto-renewal, exclusivity, IP, term); the rest confirm the mail. Papers are per-document reads with no bulk body call, so a run that skips one is wrong on the ones that flip (Hardness_Mastery §2.5).")
A("")
A("## 3 Hidden authorities")
A("")
A("| Id | Name | Home | Decoy (scope) | Governs | Findable query |")
A("|---|---|---|---|---|---|")
for a in man["authorities"]:
    dec = ", ".join(a["decoy_seeded_ids"] + a["decoy_base_pointers"])
    sc = a.get("decoy_scope")
    scs = f"{sc['dimension']}: decoy '{sc['decoy']}' vs task '{sc['task']}'" if sc else "superseded: older entry of T7's version_records"
    A(f"| {a['id']} | {a['name']} | {a['home_service']} `{a['seeded_ids'][0]}` | {a['decoy_service']} `{dec}` ({scs}) | {', '.join(a['governs'])} | \"{a['findable_query']}\" (proved at injection with hg.py search on the overlay; `{a['seeded_ids'][0]}`) |")
A("")
A("Each authority is named by a fragment (K1 names H1 and H2 in `" + I["hub_thread"] + "`; K4 names H3 in `" + I["guardrails_doc"] + "`) and none is linked by the hub. `governs` lists do not overlap (hardness_gate hidden_authorities).")
A("")
A("## 4 Delegation lattice")
A("")
A("| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |")
A("|---|---|---|")
for a in man["anchors"]:
    A(f"| {a['id']} | {a['prompt_reference']} | `{a['record']}` |")
A("")
A("Hub: Leonard's Sep 30 23:20Z mail to Frederick (`" + I["hub_thread"] + "`), in Leonard's voice, delegating by role: the guardrails doc, the Monday #executives change, ESG's note, the folder README. It never lists companies, links or locations of evidence.")
A("")
A("| Fragment | Service · container | Kind | Chain | Delegated by | Delegation quote (verbatim, planned wording) | Requirements | Names authorities |")
A("|---|---|---|---|---|---|---|---|")
for f in man["ask_fragments"]:
    na = ", ".join(f"{x['id']} ('{x['quote']}')" for x in f["names_authorities"]) or "—"
    A(f"| {f['id']} | {f['service']} · `{f['container']}` | {f['kind']} | {' → '.join(f['incorporated_via'])} | `{f['delegated_by_record']}` | \"{f['delegation_quote']}\" | {', '.join(f['requirement_ids'])} | {na} |")
A("")
A("- Amendments in another service, later in time: K10 Slack `" + I["amendment_root"] + "` (Sep 29, travel counts as cash) changes one clause of K2 (`" + I["guardrails_doc"] + "`, Sep 26); K7 gcal `" + I["review_event"] + "` (created Sep 29) pins the revisit date the doc gives as 'the first week of January'. The rest of the doc stands (no later record restates the amended clauses).")
A("- Non-authoritative distractors: Robert's 'just cancel every marketing tool' (`" + I["robert_cancel_all"] + "`, T10); Frederick's UA-buckets doc (`" + I["ua_buckets_doc"] + "`, H1 decoy, another scope); Leonard's July 'sign small stuff yourself' (`" + I["july_sign_note"] + "`, superseded by ESG, T7).")
A("")
A("## 5 Chains and trap register")
A("")
A("| Chain | Root cause | Hops (service: record → finding) | Ends in |")
A("|---|---|---|---|")
for c in man["chains"]:
    hops = " → ".join(f"{h['service']}: `{h['record']}` ({h['finding']})" for h in c["hops"])
    A(f"| {c['id']} | {c['root_cause']} | {hops} | {c['ends_in']} |")
A("")
A("| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |")
A("|---|---|---|---|---|---|---|")
for t in man["traps"]:
    recs = ", ".join(f"`{x}`" for x in (t["seeded_ids"] + t["base_pointers"])) or "—"
    fam = t["family"] + (f" ({t['distractor_type']})" if t.get("distractor_type") else "")
    A(f"| {t['id']} | {fam} | {recs} | {t['requirement']} | {t['expected_wrong_reading']} | {t['resolver']} | {t.get('discovery_order', '—')} |")
A("")
A("Hardness v2 traps used as separate cross-source decisions (guide Part 3), each with the convincing wrong source and the record that beats it:")
A("")
A("| Channel | v2 trap | Convincing wrong source (who, when) | Record that beats it (who, when, authority) | Weight-5 rows it moves |")
A("|---|---|---|---|---|")
v2rows = [
    ("DONE", "1 · proving done across services", f"portal 'Registration Completed' (Nintendo, Sep 4, `{BASE['nintendo_regdone']}`) + Frederick's post (`{BASE['fred_nintendo_post']}`)", f"Arthur's ZOM-567 comment (Sep 25, CTO) + ESG's signing rule (`{I['esg_thread']}`, counsel)", "X1, X2, X17"),
    ("CORR", "2 · a correction somewhere else", f"Framewell's quote thread (Sep 18, `{I['framewell_thread']}`) and order form", f"Leonard's thread reply under his Sep 22 Playtestcloud post (Sep 26, `{I['framewell_waiver_reply']}`), naming Maren and the Pro plan, not Framewell", "X3, X4, X14"),
    ("COMPL", "9 · work someone already did", f"Lanternfly's unanswered Sep 22 follow-up in its thread (`{I['lanternfly_thread']}`)", f"Leonard's Sep 29 reply in the DM thread under his Sep 17 localization message (`{I['lanternfly_dm']}` under `{BASE['dm_localization_root']}`): he rang Wen back", "X5, X6, X15, X19"),
    ("NOTE", "9 · work someone already did", f"Spotlight Fest's Dec 5 invitation with a $750 stand fee (`{I['spotlight_thread']}`)", f"Robert's Sep 17 #executives note (`{I['spotlight_note']}`): sitting the Dec 5 indie showcase out, let Rina know", "X20, C3"),
    ("EXC", "5 · a rule or exception hidden in the data", f"the cash test (guardrails `{I['guardrails_doc']}`) against Pingwise's Nov 1 bill (`{I['pingwise_thread']}`)", f"Arthur's Aug 12 keep-running checklist (`{I['keep_card']}`), item named by function", "X7, X16, P1"),
    ("DATE", "4 · dates, windows and dependencies", "Clipforge's pilot agreement: free through Jan 15, 2026", f"processor notice for workspace HG-2291 (Sep 12, `{I['clipforge_notice_thread']}`): pilot ends Oct 15, billing from Oct 16", "X9, X10, X11"),
    ("FILT", "7 · items outside the obvious filter", "September-window mail searches (the recent backlog)", f"Pixel Harbor's June 18 quote (`{I['pixel_thread']}`) with a deposit due Oct 10, in scope by the hub's undated rule", "X12, X13, V1"),
    ("WIN", "7 · items outside the obvious filter", "the recent inbox, the paperwork folder and the July tracker (rev3 pre-check events 66, 282, 284)", f"Hootline's Aug 5 sign-up and Aug 12 unanswered ask (`{I['hootline_thread']}`), no filed paper, in scope by the hub's undated rule", "X18, X21, V1"),
]
for r in v2rows:
    A("| " + " | ".join(r) + " |")
A("")
A("### Mechanism portfolio (S5a)")
A("")
A("Priors from `tools/hardness_ledger.py priors --model claude-opus-5-5` (UNCALIBRATED; never pooled across models). Rates used by the forecast are disclosed overrides from measured placements on the completed Frederick tasks (00_Completed_Task_Learnings.md).")
A("")
A("| # | Candidate (anchor records) | Coupling | Findability term | Prior (family · record ids) | Design rate | Survives complete retrieval | Selected |")
A("|---|---|---|---|---|---|---|---|")
cands = [
    ("DONE", f"Nintendo done-gap (`{BASE['nintendo_regdone']}`, ZOM-567)", "registration → officer acceptance → card", "'Nintendo' finds mail; comment needs linear_list_comments", "done_gap Beta(1,2) · hev_7f44d83eaad625e9, hev_522f1ca2bc9062de", "0.50", "yes: judgment needs the comment + ESG rule", "yes"),
    ("CORR", f"Framewell waiver (`{I['framewell_waiver_reply']}`)", "waiver → Park → revisit", "rev4: 'Framewell' and 'vendor' searches return nothing; found by 'Maren', 'Pro plan' or opening the Playtestcloud thread", "superseding Beta(1,3) · hev_1ceea0e7e912f48b, hev_ebc012c844829411", "0.70", "yes: the reply is a later dated claim", "yes (rebuilt)"),
    ("COMPL", f"Lanternfly answered by phone (`{I['lanternfly_dm']}`)", "answered → no second answer → log who", "rev4: a DM thread reply naming Wen and the Southeast Asia deal; found by opening the thread or a 'Southeast Asia'/'Wen' search", "completion_elsewhere Beta(1,2) · hev_13d86dcf23442708", "0.65", "yes: 'answered elsewhere' is a judgment", "yes (rebuilt)"),
    ("NOTE", f"Spotlight answered by Robert (`{I['spotlight_note']}`)", "answered → no second answer → log who", "a full September #executives read, a 'showcase'/'Rina' search or Robert's history", "completion_elsewhere Beta(1,2) · hev_13d86dcf23442708", "0.60", "yes", "yes (new, rev4)"),
    ("WIN", f"Hootline outside the filter (`{I['hootline_thread']}`)", "undated scope → in → Park → revisit", "an undated mail search or a June-onward listing; not the folder, the tracker or an Aug 15+ listing", "exact_predicate Beta(1,3) · hev_9c403cae42eb4df8, hev_c2297d21ba5cbc7b", "0.55", "partly: once found, the decision is plain", "yes (new, rev4)"),
    ("EXC", f"Pingwise on the keep-running list (`{I['keep_card']}`)", "exemption → Keep → next bill date", "'keep-running' finds the card; item names a function", "authority Beta(1,2) · hev_d17e4abe74f0e7e0", "0.40", "yes: function-to-vendor join", "yes"),
    ("DATE", f"Clipforge moved pilot end (`{I['clipforge_notice_thread']}`)", "moved end → in window → End → cancellation address", "notice names workspace HG-2291, not the company", "superseding Beta(1,2) · hev_e61e07235eadbd24", "0.50", "yes: id join + window", "yes"),
    ("FILT", f"Pixel Harbor June quote (`{I['pixel_thread']}`)", "undated scope → in → End", "its filed paper and the July tracker name it (rev3 events 284, 296)", "exact_predicate Beta(1,3) · hev_9c403cae42eb4df8, hev_c2297d21ba5cbc7b", "0.10", "partly: once found, the decision is plain", "yes (kept; leaks via its paper)"),
    ("SIGN", f"July note vs ESG (`{I['july_sign_note']}` → `{I['esg_thread']}`)", "supersession → Markward card", "on the delegation path", "superseding · hev_e61e07235eadbd24", "0.15", "yes", "yes (secondary)"),
    ("AMEND", f"travel counts as cash (`{I['amendment_root']}`)", "amendment → Wishwave End", "named by the hub", "superseding · hev_1ceea0e7e912f48b", "0.10", "yes", "yes (secondary)"),
    ("ALIAS-DD", f"Rayking 'explore for DD' (`{BASE['rayking_thread']}`)", "DD = Domino Delights or due diligence", "—", "scope_alias: no record", "—", "no: an unsettled fork", "rejected (UGT fork; Rayking made a boundary, T18)"),
    ("CAL-ONLY", "a member visible only through a calendar call", "calendar listing → inclusion", "the listing every run reads", "exact_predicate · hev_9c403cae42eb4df8", "≈0.05 (bridge Homa/Brightwater caught 6/6)", "no", "rejected (measured leak)"),
    ("SAME-THREAD", f"Balancy's in-thread answer (`{BASE['balancy_thread']}`)", "answered", "the thread itself", "completion_elsewhere: none", "≈0", "—", "kept as a control (T13)"),
    ("TRACKER", f"July tracker as the population (`{I['tracker_sheet']}`)", "stale list", "Drive search 'vendor'", "stale_summary: none", "≈0.1", "—", "kept as a distractor (T14)"),
    ("CMP-SDK", "a paid consent SDK the live game needs", "exemption", "—", "—", "—", "no: GitHub review comment on deferred crash reporting (`C093LEZGF6J`) invites a git-level contradiction", "rejected (coherence)"),
    ("COUNTS", "report counts per decision", "aggregate of every channel", "—", "—", "—", "P(fails all six) 0.45–0.58 in the first forecast (`hev_02816c7ce07c1dbb`)", "rejected (predicted all-fail rows)"),
]
for c in cands:
    A("| " + " | ".join(c) + " |")
A("")
A("Each selected rule's controls and over-application operator are in the draft manifest (`mechanism_portfolio[].controls`, `over_application`), and its channel in `channels` (CH-DONE … CH-FILT, CH-NOTE, CH-WIN, CH-SLIP). Design rates for EXC, DATE, SIGN and AMEND were cut to 0.05–0.10 after the rev3 pre-check caught them on the delegation path or in the swept inbox (§14).")
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
A(f"| breadcrumb | T1, T2, T4, T5, T6, T7, T9, T10, T11, T12, T15, T16, T17, T18, T20 | structural at design time: the entry set reaches the governing authority or the hub's scope rule for the trap's requirement (`{I['guardrails_doc']}`, `{I['esg_thread']}`, `{I['hub_thread']}`) — the incorporation link, never removed. No hub sentence names a trap's deciding record (the reply `{I['framewell_waiver_reply']}`, the DM `{I['lanternfly_dm']}`, ZOM-567's comment, the notice `{I['clipforge_notice_thread']}`, the checklist `{I['keep_card']}`, the June thread `{I['pixel_thread']}`, Robert's note `{I['spotlight_note']}`, the August Hootline thread `{I['hootline_thread']}`); injection S5c re-runs the flag on the SQL text |")
A(f"| order | T6, T11, T12, T15, T16, T18, T20 | the hub (`{I['hub_thread']}`) is decisive because it states the scope rule (R1); every company's own state sits in its own thread, never in the hub thread |")
A(f"| SAME_PLACE (hardness_v2_check) | T7 | ESG's note and Leonard's confirming reply share `{I['esg_thread']}`; both are the governing side and the superseded July note sits in Slack (`{I['july_sign_note']}`). SIGN is a secondary on-path rule, not a landing channel |")
A("| DECISION_FLIP (hardness_v2_check) | SIGN, AMEND | secondary rules moving weight-3 rows (C10, P2, C11) by kind of work; the six landing rules each move three weight-5 rows. Weights are never raised (`09_Rubric_Writing.md` gate 8) |")
A("")
A("## 6 Failure-diversity plan")
A("")
A("| Channel | Behaviour that finds the deciding record | Measured analog (completed Frederick tasks) | Rows | Independent of |")
A("|---|---|---|---|---|")
fd = [
    ("DONE", "opening ZOM-567's comments (Linear rarely opened in commercial tasks)", "bridge build access in a later #zombie-match3d post: 0/7 then 3/6 caught", "X1, X2, X17", f"Slack and mail behaviour (`{I['zom567_cmt']}`)"),
    ("CORR", "opening the thread under an unrelated #executives root, or a 'Maren'/'Pro plan' search (rev4: no company name)", "bridge SciPlay reply under an a16z post: 2/8 then 3/6 caught; rev3's named reply caught by name (precheck event 444)", "X3, X4, X14", f"Linear, Trello (`{I['framewell_waiver_reply']}`)"),
    ("COMPL", "opening a thread inside the 1:1 DM, or a 'Southeast Asia'/'Wen' search", "rev3's newest-root DM read at precheck event 428; DM threads are not shown by history (roots only)", "X5, X6, X15, X19", f"thread-opening behaviour is shared with CORR, but in a different container (`{I['lanternfly_dm']}`)"),
    ("NOTE", "reading every September #executives root, or a 'showcase'/'Rina' search", "rev3 read #executives from Sep 27 only (precheck event 30)", "X20, C3", f"name searches (`{I['spotlight_note']}`)"),
    ("WIN", "an undated mail search or a June-onward listing", "rev3 listed after:2025/08/15 (precheck event 66) and built the cohort from the folder and the tracker", "X18, X21, V1", f"Slack and Linear behaviour (`{I['hootline_thread']}`)"),
    ("EXC", "joining a checklist item named by function to a vendor's paper", "handover rules card + comment: caught by most runs; the function join is new (design 0.40)", "X7, X16, P1", f"mail and Slack (`{I['keep_card']}`)"),
    ("DATE", "reading a processor notice keyed by workspace id", "handover deactivation mail keyed by publisher id: 5/6 missed (halved to 0.50 for a fairer id join)", "X9, X10, X11", f"name searches (`{I['clipforge_notice_thread']}`)"),
    ("FILT", "mail searches with no September date filter", "handover Arthur's email outside the money window: 2/6 missed", "X12, X13, V1", f"everything else (`{I['pixel_thread']}`)"),
]
for r in fd:
    A("| " + " | ".join(r) + " |")
A("")
A("Each landing channel moves two to four rows (a 1-row trap chains patterns: bridge rev12 batch 1). Five rebuilt or new channels (DONE, CORR, COMPL, NOTE, WIN) at ~0.55–0.70 give 0–5 landings per run; P(a run misses at most one of them) ≈ 0.1 (UNCALIBRATED). Replaying the rev3 pre-check's own behaviour on this surface scores 48.6 % (policy row below). Policy scores on the real surface (`plan/policy_scores.py`, UNCALIBRATED):")
A("")
A("```")
A(pol)
A("```")
A("")
A(f"Correlation risk named: CORR and COMPL both reward opening Slack threads (different containers: #executives vs the DM); NOTE rewards a full #executives read. The forecast's correlated scenario is the pessimistic view (P(all) {next((l.split('P(all) ')[1] for l in fc_lines.splitlines() if 'correlated' in l), 'see §12')}). DONE (Linear) and WIN (undated mail) use distinct behaviours. SIGN and AMEND (rate 0.05) are left out of the forecast's exact combinations (8-mechanism limit).")
A("")
A("## 7 Deliverables and dependent writes")
A("")
A("| Write | Tool | Count | Depends on | Requirements | Target and access |")
A("|---|---|---|---|---|---|")
tg = {"gsheets": f"new sheet in Frederick's folder `{I['q4_folder']}` (owner Frederick, Drive and Sheets rows agree)", "gmail": f"threads in Frederick's mailbox (`{I['hub_thread']}` and each company's); ESG intake from Contacts `{I['esg_intake_contact']}`",
      "gcal": "Frederick's own calendar `frederick.stone@harmonygames.co`", "contacts": "Contacts (unscoped)", "trello": f"founders' board To Do list `{B.TODO_LIST}`"}
for w in man["writes"]:
    A(f"| {w['service']} | `{w['tool']}` | {w['count']} | {', '.join(w['depends_on'])} | {', '.join(w.get('requirements', []))} | {tg.get(w['service'], '')} |")
A("")
A("Reuse vs create (A8): three counterparties already have contacts (Kinetic Arcade, Lumencloud, Markward) — reuse, no duplicate.")
A("")
A("## 8 Service role map")
A("")
A("| Service | Role | Load-bearing fact or write | Carrier |")
A("|---|---|---|---|")
for svc, v in man["services"].items():
    A(f"| {svc} | {v['role']} | {v['weight_reason']} | ● (`{I['hub_thread'] if svc == 'gmail' else I['guardrails_doc'] if svc == 'gdocs' else I['q4_folder'] if svc == 'gdrive' else I['template_sheet'] if svc == 'gsheets' else I['lanternfly_deck'] if svc == 'gslides' else I['amendment_root'] if svc == 'slack' else I['review_event'] if svc == 'gcal' else I['keep_card'] if svc == 'trello' else I['esg_intake_contact'] if svc == 'contacts' else 'ZOM-567'}`) |")
A("| github | not used | none (S04 name mismatch; nothing in scope) | — (`frederick.stone@harmonygames.co/1842359398719557772`) |")
A("| confluence | not used | never carries a fact (injected pages may not load, learnings §26) | — |")
A("| snowflake | not used | not writable; no money row reads the warehouse | — |")
A("")
A("## 9 Call budget")
A("")
A("| Phase | Service | Calls | Necessity reason |")
A("|---|---|---|---|")
for r in man["call_budget"]:
    A(f"| {r['phase']} | {r['service']} | {r['calls']} | {r['reason']} |")
A(f"| **total** | 10 services | **{B.TOTAL_BUDGET}** | unconditional; largest share outside the per-record phase 37 % (gmail) |")
A("")
A("Golden-run note: a lean correct run still needs every paper read (13 decide) and every per-company write (31 answers, 14 reminders, 32 contacts, 7 cards, 3 ESG emails, the log, the report) ≈ 150 counted calls; the requester's > 130 floor sits under it. Measured analogs: bridge (44 per-entry writes) 109–150; card spend (per-document reads) 554–573.")
A("")
A("## 10 QC rails")
A("")
A("### Two-reading table")
A("")
A("| Decision point | Best reading | Strongest alternative | Resolution (record) |")
A("|---|---|---|---|")
tr = [
    ("Rayking in scope", "out: nothing from HG reached them", "in: Frederick wrote 'Hi …, Leonard forwarded me your email'", f"the reply's To is leonard.hayes (`{BASE['rayking_thread']}`); hub: pitches only forwarded around internally stay off (T18)"),
    ("Pixel Harbor in scope", "in: a June quote still waiting (deposit by Oct 10)", "out: stale, before the September backlog", f"hub scope has no date limit; the quote's hold runs to Oct 10 (`{I['pixel_thread']}`)"),
    ("Balancy", "Answered by Leonard, revisit Jan 5", "Park with a new reply", f"Leonard answered in-thread Sep 11 'we'll circle back' (`{BASE['balancy_thread']}`); guardrails: already answered with 'later' → revisit"),
    ("Lanternfly", "Answered by Leonard, revisit Jan 5", "Sign (2-year exclusivity) or Park with a reply to the follow-up", f"Leonard's Sep 29 DM thread reply (`{I['lanternfly_dm']}`): 'rang Wen back … about their Southeast Asia deal' — Wen Halvorsen signs Lanternfly's thread (`{I['lanternfly_thread']}`)"),
    ("Framewell", "Park to Jan 5", "End: Pro billed from Nov 1", f"Leonard's Sep 26 reply: 'Maren called me back about the Pro plan … no charge until Feb 1' (`{I['framewell_waiver_reply']}`) — Maren Holt sends Framewell's order form (`{I['framewell_thread']}`), and the reply is later"),
    ("Spotlight Fest", "Answered by Robert, no second answer", "End: say no to the $750 stand fee", f"Robert's Sep 17 note: the call about the Dec 5 indie showcase, sitting it out, let Rina know (`{I['spotlight_note']}`) — Rina Takeda's invitation is for the Dec 5 indie showcase (`{I['spotlight_thread']}`)"),
    ("Hootline", "in: Park, revisit Jan 5", "out: nothing recent and no filed paper", f"hub scope has no date limit and counts a sign-up as engagement; Gemma's Aug 12 question is unanswered (`{I['hootline_thread']}`)"),
    ("Pingwise", "Keep, confirm staying", "End (cash test) or Sign (new terms)", f"keep-running checklist (`{I['keep_card']}`); the Team plan continues under the existing agreement, so no new acceptance (`{I['pingwise_thread']}`)"),
    ("Clipforge", "End, cancel in writing by Oct 15 to the notice's address", "Park: free through Jan 15", f"processor notice Sep 12 for workspace HG-2291 (`{I['clipforge_notice_thread']}`) is later than the agreement; workspace id is on the agreement and the Jul 14 kickoff (`{I['clipforge_kickoff']}`)"),
    ("Nintendo", "Sign: card for Leonard/Arthur, next date Oct 15", "nothing waiting (registration completed)", f"Arthur's ZOM-567 comment (`{I['zom567_cmt']}`) + ESG (`{I['esg_thread']}`)"),
    ("Markward click-through", "Sign: an officer accepts", "Frederick accepts it himself (small, free)", f"ESG Sep 24 'whatever the amount, including click-through terms' + Leonard's Sep 25 reply 'this replaces what I said in July' (`{I['esg_thread']}`) over `{I['july_sign_note']}`"),
    ("Playfuse NDA", "Sign card only, no ESG email", "also send to ESG", f"ESG: mutual NDAs on our template need no review (`{I['esg_thread']}`)"),
    ("Kinetic Arcade", "ESG email and a card", "ESG email only", f"ESG: anything waiting on a signature gets a card, including the ones sent to us (`{I['esg_thread']}`)"),
    ("Wishwave", "End: partner-booked travel counts as cash", "Park: we book nothing", f"Sep 29 amendment (`{I['amendment_root']}`) later than the doc (`{I['guardrails_doc']}`)"),
    ("Retainly", "Park: converts Jan 12, 2026", "End: a trial that converts", f"the conversion date is outside Oct 1–Dec 31 (guardrails `{I['guardrails_doc']}`)"),
    ("Portal with no person (Nintendo)", "no reply, no contact; the card is the action", "write to the portal", f"guardrails: portals and no-reply notices need no answer (`{I['guardrails_doc']}`)"),
    ("Revisit date", "Mon Jan 5, 2026 (the review)", "any day in the first week of January", f"Leonard's review event created Sep 29 (`{I['review_event']}`)"),
    ("Contacts already present", "reuse: no new contact", "add again", f"README: add only when missing (`{I['readme_doc']}`)"),
]
for r in tr:
    A("| " + " | ".join(r) + " |")
A("")
A("No decision forks on a reported figure; one reading per point (BOTH_FAIR_FIGURE not needed). Dates: every graded date is a plan date (Oct 10, Oct 15, Nov 1, Jan 5) with the same PT and UTC day.")
A("")
A("### Reach table (load-bearing records)")
A("")
A("Base records, `persona_view.py can-see frederick_stone …` (verbatim, `00_PreScenario/cansee_anchors.txt`):")
A("")
for l in cansee.splitlines():
    A(f"- {l}")
A("")
A("Planned seeds (verified at the injection gate; owner or invitee Frederick): ")
for k in ["hub_thread", "esg_thread", "framewell_thread", "pingwise_thread", "clipforge_notice_thread", "pixel_thread", "lanternfly_thread", "guardrails_doc", "readme_doc", "template_sheet", "esg_checklist_doc", "lanternfly_deck", "q4_folder", "review_event", "clipforge_kickoff", "spotlight_call", "amendment_root", "framewell_waiver_reply", "lanternfly_dm", "spotlight_note", "spotlight_thread", "hootline_thread"]:
    A(f"- LB `{I[k]}` ({k})")
A("")
A("Unscoped load-bearing records: Trello `" + I["keep_card"] + "` (board `640643a3fd8f3ca308d9318e`), Linear ZOM-567 and `" + I["zom567_cmt"] + "`, Contacts `" + I["esg_intake_contact"] + "`.")
A("")
A("**Feasibility.** Every write exists in `Evals/references/tools/catalog.json` (`gmail_reply_to_message`, `gmail_send_message`, `gcal_create_event`, `contacts_add_new_contact`, `trello_create_card`, `gsheets_create_spreadsheet`, `gsheets_values_update`, `gdrive_move_file`); "
  "Frederick owns the folder `" + I["q4_folder"] + "` and his calendar; Trello and Contacts are unscoped. "
  "**Precedence.** Load-bearing facts sit in ● carriers (mail bodies, Docs/Slides bodies, Slack messages, Linear comments, Trello checklist, calendar descriptions of events Frederick attends), never only in an attachment. "
  "**Naturalness.** The prompt names Leonard's email and the folder; it never names companies, rules, decisions, authorities or locations of evidence. "
  "**Grading devices.** ≤ 5 samples per group (decision, next date, answered by, told) plus the membership volume row; exclusions graded as the exact log membership, never as leave-alone rows.")
A("")
A("### Coherence rail")
A("")
A(f"Every 1a row is dispositioned; every designed disagreement is a dated human claim overturned by a named later record (T2 `{I['framewell_waiver_reply']}`, T5 `{I['clipforge_notice_thread']}`, T7 `{I['esg_thread']}`, T8 `{I['review_event']}`, T9 `{I['amendment_root']}`); no system field is modified. Companions are planned in §11.")
A("")
A("## 11 Record plan for /create-injection")
A("")
A("| Record | Service · table | Planned id | Time (UTC) | Author | Content (planned) |")
A("|---|---|---|---|---|---|")
plan = [
    ("hub", "gmail · gmail_messages/threads", I["hub_thread"], T["hub"], "Leonard → Frederick", "the backlog handoff: " + "; ".join(f"'{Q[k]}'" for k in ["hub_scope", "hub_cold", "hub_guardrails", "hub_amend", "hub_esg", "hub_answer", "hub_contacts", "hub_readme", "hub_report"])),
    ("guardrails doc", "gdocs · docs_documents + gdrive · drive_files", I["guardrails_doc"], T["guardrails"], "Leonard (shared Robert, Arthur, Frederick)", "decisions top to bottom; cash window Oct 1–Dec 31 PT incl. trial conversions; '" + Q["doc_keep"] + "'; travel counts only when we book it; portals and no-reply notices need no answer; already answered → log who and when, revisit if 'later'; park '" + Q["doc_review"] + "' (first week of January)"),
    ("UA-buckets doc (H1 decoy)", "gdocs + gdrive", I["ua_buckets_doc"], T["ua_buckets_doc"], "Frederick", "fundraising bucket vs real UA bucket for ad-network spend (scope: UA)"),
    ("ESG signing note + Leonard's reply", "gmail (Frederick, Leonard, Robert, Arthur copies)", I["esg_thread"], T["esg_note"] + " / " + T["esg_ack"], "PERSON_2694 → founders; Leonard", "only Leonard or Arthur accept terms, whatever the amount, including click-through and portal NDAs; auto-renewal, exclusivity, IP licence or > 12 months → '" + Q["esg_intake"] + "', one email per agreement; '" + Q["esg_checklist"] + "'; mutual NDAs on our template need no review; '" + Q["esg_board"] + "', including the ones sent to us · reply: 'Agreed. This replaces what I said in July about Fred signing small stuff himself.'"),
    ("ESG intake checklist", "gdocs + gdrive (owner PERSON_2694, shared founders)", I["esg_checklist_doc"], T["esg_checklist"], "PERSON_2694", "per agreement: counterparty, what it is, term, renewal, cost, who signs"),
    ("ESG Law intake contact", "contacts · contacts", I["esg_intake_contact"], "—", "—", "ESG Law intake, email PERSON_2599_EMAIL (base token)"),
    ("July signing note (superseded)", "slack · slack_messages", I["july_sign_note"], T["july_sign_note"], "Leonard", "for small stuff under $500 a year Fred can accept the terms himself"),
    ("Robert's cancel-everything post", "slack", I["robert_cancel_all"], T["robert_cancel_all"], "Robert", "honestly just cancel every marketing tool, all of it"),
    ("travel amendment (root)", "slack", I["amendment_root"], T["amendment"], "Leonard", "one change to the guardrails: travel and event costs count as cash even when a partner books them"),
    ("Framewell waiver (reply under Playtestcloud root; rev4 wording)", "slack (+ root counter UPDATE)", I["framewell_waiver_reply"], T["framewell_waiver"], "Leonard", "'" + Q["framewell_waiver_v4"] + "' (no 'Framewell', no 'vendor')"),
    ("Lanternfly answer (rev4: DM thread reply under " + BASE["dm_localization_root"] + ")", "slack (+ DM root counter UPDATE)", I["lanternfly_dm"], T["lanternfly_dm"], "Leonard → Frederick", "'" + Q["lanternfly_note_v4"] + "' (no 'Lanternfly', no 'told')"),
    ("Robert's Spotlight note (rev4 wording)", "slack", I["spotlight_note"], T["spotlight_note"], "Robert", "'" + Q["spotlight_note_v4"] + "' (no 'Spotlight', no 'told', no 'booth')"),
    ("keep-running card", "trello · cards/checklists/check_items/actions", I["keep_card"], T["keep_card"], "Arthur", "Doing list; checklist: Vaultline nightly DB backups · Certwell SSL for the API domain · the night pager for backend outages (whatever wakes me at 3am) · App Store and Play developer accounts"),
    ("ZOM-567 + comment", "linear · issues/comments", "ZOM-567 / " + I["zom567_cmt"], T["zom567"] + " / " + T["zom567_cmt"], "Arthur (no assignee)", "'Switch: order dev kits' · comment: can't order kits, the org account stays limited until a company officer accepts the Global ToS and NDA from their own login; Fred's sign-up doesn't count; the request lapses Oct 15"),
    ("Jan 5 commitments review", "gcal · events (one copy per attendee)", I["review_event"], T["review_event"], "Leonard (attendees founders)", "Mon Jan 5, 2026 09:00 PT: everything we parked comes back here"),
    ("Clipforge kickoff", "gcal", I["clipforge_kickoff"], T["clipforge_kickoff"], "Priya Raman (Frederick invited)", "UGC Studio kickoff — workspace HG-2291"),
    ("Spotlight Fest call", "gcal", I["spotlight_call"], T["spotlight_call"], "Robert (Frederick invited)", "rev4 description: '" + Q["spotlight_desc_v4"] + "' (no answer)"),
    ("Hootline thread (rev4)", "gmail (Frederick's mailbox)", I["hootline_thread"], T["hootline_signup"] + " / " + T["hootline_ask"], "Gemma Doyle", "Aug 5 welcome (promo free until Jan 31, then $39/month) · Aug 12: '" + Q["hootline_ask_v4"] + "'; the filed paper is dropped (terms in the body)"),
    ("Q4 commitments folder", "gdrive · drive_files (owner Frederick, shared Leonard as writer)", I["q4_folder"], T["folder"], "Frederick", "destination"),
    ("folder README", "gdocs + gdrive (in the folder)", I["readme_doc"], T["readme"], "Leonard", "columns Company · Contact · What's waiting · Decision · Answered by · What we told them · Next date; Next date = End: the last day to cancel or say no · Park and 'later' answers: the January review · Keep: when it next bills · Sign: the date they need it by, if any; contacts: company in the job field, add only when missing; '" + Q["readme_template"] + "'"),
    ("log template", "gsheets + gdrive (in the folder)", I["template_sheet"], T["template"], "Leonard", "header row only"),
    ("July vendor tracker (stale)", "gsheets + gdrive (owner Frederick)", I["tracker_sheet"], T["tracker"], "Frederick", "19 offers as of Jul 31 (D04 lookalike of the template)"),
    ("Clipforge processor notice", "gmail (sender billing@paylane.io)", I["clipforge_notice_thread"], T["clipforge_notice"], "Paylane on behalf of workspace HG-2291 (UGC Studio)", "pilot cap reached: pilot ends Oct 15; $1,800/month from Oct 16 unless cancelled in writing to billing@paylane.io"),
]
for k, v in sorted(THREAD.items()):
    m = next(x for x in B.M if x["key"] == k)
    who = f"{m['person'][0]} {m['person'][1]} <{m['person'][2]}>" if m["person"] else "—"
    plan.append((f"{k} thread", "gmail (Frederick's mailbox)", v, m["first_at"] if isinstance(m["first_at"], str) and "T" in m["first_at"] else "2025-08..09 (dated per member)", who, f"{m['kind']}: {m['deciding']}"))
for k, v in sorted(PAPER.items()):
    m = next(x for x in B.M if x["key"] == k)
    plan.append((f"{k} paper", f"{m['paper']} + gdrive (owner the counterparty, shared with Frederick)", v, "same day as its thread", m["person"][0] + " " + m["person"][1] if m["person"] else "—", f"terms: {m.get('cost') or m['deciding'][:120]}"))
for r in plan:
    A("| " + " | ".join(str(x).replace("|", "/") for x in r) + " |")
A("")
A("Existing contacts seeded: Kinetic Arcade (Noor Haddad), Lumencloud (Aiden Clarke), Markward (Leah Brennan), company in the job field (`" + B.contact("existing:Kinetic Arcade") + "`, `" + B.contact("existing:Lumencloud") + "`, `" + B.contact("existing:Markward") + "`).")
A("")
A("### Integrations and companions")
A("")
A("Companions from `references/universe_kb/by_universe/synthcut/integrations.json`:")
A("")
A("| Service | INT id | Companion | Decision |")
A("|---|---|---|---|")
A(f"| gcal | INT-11 | invitation / update mails for `{I['review_event']}`, `{I['clipforge_kickoff']}`, `{I['spotlight_call']}` in each attendee mailbox | seed them (one GCal copy per attendee calendar too) |")
A(f"| gdrive | INT-13 | Google Drive Slack app DMs for shares | integration_exceptions: shares of `{I['guardrails_doc']}`, `{I['readme_doc']}` and the papers are mirrored only in drive sharing rows (no Drive-app DM), declared at injection |")
A("| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment (no PR exists: none); Slack DM notifications (ZOM-567 has no assignee or subscriber: none); unread-notification digests | INT-03/04: none; INT-05: declared exception for ZOM-567's comment |")
A(f"| slack | INT-22 | '[Slack] … sent you a message' mail for the DM thread reply `{I['lanternfly_dm']}` | seed the notification mail in Frederick's mailbox or declare it; decided at injection with base_check (the rev3 decision carries over) |")
A("| trello | INT-21 | Trello → Slack: no integration exists | none |")
A("| gmail | — | no INT source maps to gmail itself | none |")
A("| gdocs / gsheets / gslides | INT-13 (google_drive) | as gdrive | as gdrive |")
A("| contacts | — | no integration | none |")
A("")
A("## 12 Self-test results")
A("")
A("`hardness_gate.py 01_Hardness_Manifest.draft.json --design` (verbatim):")
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
A("`hardness_v2_check.py --design` (verbatim; dispositions in §5 Liveness flags):")
A("")
A("```")
A(v2)
A("```")
A("")
A(f"S9b prior forecast (UNCALIBRATED, advisory, pre-registered): ledger id `{fc_id}`; mechanism rates are disclosed overrides sourced from the completed Frederick tasks.")
A("")
A("```")
A(fc_lines)
A("```")
A("")
A("**Lazy-solver pass.** One broad search per service, first hits, no thread opens, stop at the first conclusion: it reads the hub, the guardrails doc and each company's own thread and paper → loses DONE, CORR, COMPL, EXC (no checklist join), DATE (notice not returned by name), FILT (September window) → 52.0 % on the surface (`plan/policy_scores_output.txt`). Every point it scores comes from controls; no leak found.")
A("")
A("**Literal-value sweep (planned text).** 'Feb 1' appears only in Framewell's waiver reply; 'Oct 15' for Clipforge only in the processor notice; 'night pager' only on the checklist; 'lapses Oct 15' only in the ZOM-567 comment; 'pick it up again in January' for Lanternfly only in the DM thread reply; 'sitting this one out' only in Robert's note. **Wording sweep (rev4).** None of the three moved corrections names its company or uses the rev3 pre-check's search words ('told', 'vendor', 'trial', 'quote', 'booth', 'retainer'; precheck events 386–480); each names the company's own contact (Maren, Wen, Rina) who signs that company's thread, so the alias resolves from a record the persona reads. 'SEA deal', 'indie showcase' and 'Halvorsen' have 0 base hits (hg.py search slack/gmail/contacts); 'Maren' matches only inside 'gsmarena'. **The rest stands.** No later record re-asserts the amended travel clause or the doc's 'first week of January'.")
A("")
A("### Self-review")
A("")
A("Walked `Evals/1_Prompt_Eval.md` §2.1 (UGT), §2.2 (feasibility), §3.2 (cross-service coherence) and `Evals/0_Injection_Quality_Eval.md` Check C against this design.")
A("")
A("| # | Category or decision point | Counter-reading (strongest argument it fails) | Resolution and evidence |")
A("|---|---|---|---|")
sr = [
    ("temporal", "seeded Sep 30 hub is after the seed bound in PT or UTC", f"23:20Z Sep 30 < freeze 2025-10-01T00:00Z; every T value in build_scenario.py T is earlier (`{I['hub_thread']}`)"),
    ("semantic", "'answered' could mean any reply, so Frederick's Sep 10 'we'll take a look' answers Lanternfly", f"guardrails define already answered as an answer to what they asked; Leonard's DM gives that answer (`{I['lanternfly_dm']}`); the follow-up shows 'take a look' was not an answer"),
    ("cross-service referential", "Clipforge's workspace HG-2291 maps to no record the persona can see", f"the agreement and the Jul 14 kickoff (`{I['clipforge_kickoff']}`) carry HG-2291 and UGC Studio (C5)"),
    ("quantitative", "Leonard's reply under the Playtestcloud root leaves its reply_count stale", f"hazard Q01 acknowledged; SQL updates the counters (`{BASE['playtestcloud_root']}`)"),
    ("state/lifecycle", "ZOM-567 open and assigned to someone quiet in October (L08)", "no assignee; creator Arthur; open is its true state at the clock (ZOM-567)"),
    ("identifier/format", "ESG intake address as a token breaks the send", f"base already uses PERSON_2599_EMAIL as the group address (`{BASE['esg_engagement']}`); the Contacts entry reuses it (`{I['esg_intake_contact']}`)"),
    ("other", "seeding 33 vendor relationships never mentioned in base Slack reads as contrived", f"they are trials, quotes and proposals with no spend history (name census plan/name_census.json); Frederick's base mailbox already holds many such inbound offers (`{BASE['playable_factory_thread']}`)"),
    ("Rayking in scope", "Frederick's 'Hi …' message makes Rayking engaged", f"To: leonard.hayes in `{BASE['rayking_thread']}`; the hub excludes pitches only forwarded internally (T18)"),
    ("Pixel Harbor", "June quote is stale and could be ignored", f"deposit due Oct 10 is still pending and the scope has no date limit (`{I['pixel_thread']}`, C6)"),
    ("Balancy", "Leonard's 'we'll circle back' is not an answer, so it needs a reply", f"it answers the trial offer (`{BASE['balancy_thread']}`); Balancy acknowledged on Sep 15; guardrails: 'later' answers get a revisit"),
    ("Lanternfly", "the DM reply could be about another publisher (it no longer names Lanternfly)", f"it names Wen and 'their Southeast Asia deal'; Wen Halvorsen signs Lanternfly's Southeast Asia proposal thread (`{I['lanternfly_thread']}`); dated after the Sep 22 follow-up (T3)"),
    ("Spotlight Fest", "Robert's note could be about another showcase (Wishwave's partner showcase)", f"it names the Dec 5 indie showcase and Rina; Rina Takeda's invitation is for the Dec 5 indie showcase (`{I['spotlight_thread']}`), Wishwave's is a pre-registration push with Sven (T19)"),
    ("Hootline", "with no paper and nothing after Aug 12 it is a stale sign-up, not something waiting", f"Gemma's Aug 12 question is unanswered and the promo decision falls at Jan 31; the hub's scope counts a sign-up and has no date limit (`{I['hub_thread']}`, T20)"),
    ("rev4 rebuild", "de-naming the corrections makes them unfair (a reviewer cannot tie Maren or Wen to the company)", "each contact signs its own company's thread; the rev3 /prompt review accepted the alias-by-function night pager (run_forensics/rev3/platform_prompt_review.md F7); the blind fork sweep at injection re-checks it"),
    ("Framewell", "'treat it like the other free ones' could mean Keep", f"guardrails: free until January → Park (`{I['guardrails_doc']}`); Keep is only for Arthur's list (`{I['keep_card']}`)"),
    ("Pingwise", "staying on Team means accepting new paid terms → Sign", f"the notice says the Team plan continues under the existing agreement unless downgraded (`{I['pingwise_thread']}`); nothing to accept (T4)"),
    ("Clipforge", "the agreement (free through Jan 15) still governs", f"the Sep 12 notice is later and reports the cap the agreement allows (`{I['clipforge_notice_thread']}`, T5 version_records)"),
    ("Nintendo", "Frederick's registration is a sign-up, so it is done", f"Arthur's comment: org account limited until an officer accepts (`{I['zom567_cmt']}`); ESG: only Leonard or Arthur accept terms (`{I['esg_thread']}`)"),
    ("Markward", "Leonard's July note lets Frederick accept small free terms", f"ESG's Sep 24 note and Leonard's Sep 25 'this replaces what I said in July' (`{I['esg_thread']}`, T7)"),
    ("Playfuse", "an NDA is legal paper, so it goes to ESG", "ESG: mutual NDAs on our template need no review; an officer signs (K5)"),
    ("Kinetic Arcade", "counsel items wait on counsel, not a signature: no card", f"ESG: anything waiting on a signature gets a card, including the ones sent to us (`{I['esg_thread']}`)"),
    ("Wishwave", "the partner books travel, so the doc's rule parks it", f"the Sep 29 amendment is later and changes that clause (`{I['amendment_root']}`, T9)"),
    ("Retainly", "a converting trial should end like Reviewly", "Retainly converts Jan 12, 2026, outside Oct 1–Dec 31 (T17)"),
    ("portal (Nintendo)", "everyone waiting gets a written answer, so write to Nintendo", f"guardrails: portals and no-reply notices need no answer (`{I['guardrails_doc']}`)"),
    ("revisit date", "the doc's 'first week of January' allows any day", f"Leonard's review event fixes Mon Jan 5 (`{I['review_event']}`, T8)"),
    ("contacts present", "a duplicate contact is harmless, so the dedupe read is padding", "three counterparties exist; README says add only when missing (K8); the lookup changes the result"),
    ("volume", "~150 calls in a lean run is padding-driven", "every read decides or confirms a company's own decision; every write is one per company the hub or an authority asks for (K1, K8, K5); no record exists only for count (§2 necessity)"),
    ("difficulty", "six channels at 0.35–0.50 is optimistic; measured pre-checks missed ~1 of 3 traps", "at 0.6× the rates P(all, < 80 %) is 0.48 (`plan/policy_scores_output.txt`); the correlated forecast view is the floor (§12)"),
    ("HARDNESS GATE output", "a PASS at --design proves nothing about the SQL", "true: injection re-runs hardness_gate on the SQL with every seeded id; this design PASS covers structure only (§12)"),
]
for i, r in enumerate(sr, 1):
    A(f"| {i} | {r[0]} | {r[1]} | {r[2]} |")
A("")
A(f"HARDNESS GATE (design) result is pasted verbatim above. Forecast `{fc_id}` is advisory and UNCALIBRATED.")
A("")
A("Amendment, 2026-11-03 (found at `/create-injection` S4b, re-certified here): the five \"What we told them\" slots (X13, X15, C5, C6, C11) use the `reason_matches` selector, which `surface_grader.py` scores by regex against the written reason cell, never against a solver value; `oracle_kit.py` has no solver reading for it, so as class `direct` they failed `contract.slots`. They are now class `write_content` (graded from the written log, like the other written-content slots); weights, keys, groups and mechanisms are unchanged. X15's pattern now keys on the part only Leonard's DM holds (no new publishing deals / before the raise): the old pattern also matched the guardrails' own Park wording (\"we'll pick it up in January\"), so a run that missed the DM still passed it. The draft manifest is byte-identical (db7e2c16e5a8).")
A("")
A("Amendment, 2026-11-04 (`--revise`, design-2): §14 takes in the rev3 pre-check. T2 and T3 are rebuilt (de-named corrections; Lanternfly's answer moves into a DM thread), T19/NOTE (Spotlight) and T20/WIN (Hootline outside the filter) are added, X7 leaves the decision group for X20, X18/X19/X21 are added, and the told/answered-by/next-date matchers are loosened (manifest design_delta). truth.json values do not change.")
A("")
A("Unresolved: no independent red-team review of this design (REDTEAM_* unset; fallback in §13); the rev4 landing rates are UNCALIBRATED estimates from one pre-check plus bridge analogs, and the stop rule allows one more pre-check for this scenario; INT-13/INT-05/INT-22 companion choices are decided at injection with base_check.")
A("")
A("## 13 Red team (dual)")
A("")
A("RED TEAM UNAVAILABLE: REDTEAM_* is not set in this environment, so `tools/redteam_review.py --mode redteam --dual` cannot reach a reviewer endpoint.")
A("")
A("RED TEAM FALLBACK: Claude (Opus 5.5) self-review only, plus (for design-2) the rev3 platform Opus 5.5 pre-check and its /hardness review as independent evidence of where the design leaked (run_forensics/rev3/platform_hardness_review.md) — the counter-reading table in §12, the whole-universe name census with a positive control (`plan/name_census.json`), the id-collision check (`plan/id_checks.json`, positive controls found), the policy scores and the pre-registered forecast. The requester delegated the review choice in chat on 2026-11-03 ('you can choose from your self'). No independent review of this design exists; it stays in every Unresolved line until a review or the Opus pre-check covers it (learnings §44).")
A("")
A("## 14 Revision intake (S0r)")
A("")
A("Verdicts file consumed: `run_forensics/rev3/precheck.node_verdicts.json` (node_verdicts.py on the rev3 pre-check; dispositioned records `run_forensics/rev3/precheck.dispositioned.jsonl`, ledger ids hev_b8f28a892a74b855 … hev_0791c57922eeb614; report `01a_Hardening_Report.md`).")
A("")
A("Export binding: the one export, label `precheck` (`06_PreCheck_Trajectory/trajectory.json`, sha256 d5dc726b6150), is BOUND to rev3 on discriminating content (sql 2176eb708f74; binding basis and seen needles in the verdicts file). It certifies nothing about design-2; rev4 needs its own pre-check.")
A("")
A("| Node | Runs | Proposed verdict | Disposition | Evidence |")
A("|---|---|---|---|---|")
for r in [
    ("DONE", "1", "BYPASSED (dispositioned LANDED)", "keep: Nintendo stays as designed; the run never opened the portal mails or Linear", "precheck event 66 (Nintendo threads listed, not opened); register write precheck event 533 has no Nintendo row; no Linear call in 265"),
    ("CORR", "1", "LEAKED (mechanism? pending: Framewell Next date)", "rebuild: de-name Leonard's reply (Maren, the Pro plan), keep it under the Playtestcloud root (T2). CONFOUNDED candidate rejected: the flagged value '2026-01-05 (January commitments review)' is the right date (representation), so no tool, fairness, verifier or run cause", "precheck event 444 ('Framewell' search) and event 480 ('vendor after:'), thread opened at precheck event 455"),
    ("COMPL", "1", "LEAKED (mechanism? pending: Lanternfly Answered by)", "rebuild: the answer becomes a DM thread reply under Leonard's Sep 17 localization root, naming Wen and the Southeast Asia deal (T3). CONFOUNDED candidate rejected: 'Leonard Hayes, Sep 27 (call)' is the right person (representation)", "precheck event 387 ('Lanternfly'), event 426 ('told after:'), DM history newest root at precheck event 428/430"),
    ("EXC", "1", "LEAKED", "keep: the keep-running card is an incorporated authority (guardrails step 3); rate cut to 0.05; X7 leaves the decision group", "card opened directly at precheck event 50"),
    ("DATE", "1", "LEAKED", "keep: an incorporated cash-test decision on a swept notice; rate cut to 0.10", "notice in the Aug 15+ listing at precheck event 66, opened at precheck event 187"),
    ("FILT", "1", "LEAKED", "keep Pixel Harbor (its paper and the tracker lead to it); the filter move is rebuilt on Hootline as the new rule WIN (T20)", "tracker at precheck event 284, paper at precheck event 296, name search at precheck event 309"),
    ("SIGN", "1", "LEAKED", "keep: on the delegation path by design (the hub names ESG's note); SAME_PLACE T7 accepted", "ESG thread opened at precheck event 43"),
    ("AMEND", "1", "LEAKED", "keep: named by the hub (the Monday post)", "#executives history read at precheck event 35"),
]:
    A("| " + " | ".join(r) + " |")
A("")
A("Controls (7) and channels (6) in the verdicts file are HELD in the dispositioned records; CH-SLIP's flagged slips are representational (the brief's §4b classes) and the loosened matchers (issue_key for Answered by and Next date; wider told patterns) stop the proxy from counting them.")
A("")
A("Routing: universe changes → `/create-injection` rev4 (design_delta in the draft manifest); prompt-side defects: none (rev3 /prompt scored 5 on every dimension; `04_Prompt.txt` 32f7ab0cabd6 stays); OE/rubric notes (accept the §4b classes, grade negative writes, require the Priya note) → `/create-oe-writing`, `/create-rubric-writing`; no verifier or all-fail findings (no baseline yet).")
A("")
open(os.path.join(WF, "01_Scenario_Design.md"), "w").write("\n".join(L) + "\n")
print("wrote 01_Scenario_Design.md", len(L), "lines; forecast", fc_id)

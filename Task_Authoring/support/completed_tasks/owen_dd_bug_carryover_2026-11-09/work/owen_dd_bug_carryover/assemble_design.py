#!/usr/bin/env python3
"""Assembles 01_Scenario_Design.md from the manifest, surface, seed texts, tool outputs and sweep dispositions."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); O = os.path.join(HERE, "out")
M = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json")))
SF = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))
SEED = json.load(open(os.path.join(HERE, "seed_text.json")))
TR = json.load(open(os.path.join(HERE, "truth_sketch.json")))
rd = lambda f, d="": open(os.path.join(O, f)).read().rstrip() if os.path.exists(os.path.join(O, f)) else d
fence = lambda t: "```\n" + t + "\n```"
coll = open(os.path.join(WF, "00_PreScenario", "entity_collisions.txt")).read().rstrip()
ent = open(os.path.join(WF, "00_PreScenario", "entity_owen.txt")).read().rstrip()
tbl = lambda head, rows: "| " + " | ".join(head) + " |\n|" + "---|" * len(head) + "\n" + "\n".join("| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in r) + " |" for r in rows)
FORK = rd("sweep_dispositions.md", "Pending.")
S = []
A = S.append
A("# Scenario Design — owen_dd_bug_carryover · design only · contains no prompt, OE or criterion text\n")
A("Storyline: Domino Delights' bug record moves out of Slack into Linear before Slack loses its history. Planned seed texts live in `plan/seed_text.json`; planned outcomes for all 89 graded items in `plan/truth_sketch.json`. Every number marked UNCALIBRATED is a design aid. All open choices were delegated by the requester on 2026-11-07 (`00_Pre_Scenario_Analysis.md` §11).\n")
A("## 0 Assignment, persona census and horizon note\n")
A(tbl(["Field","Value"],[
 ["Universe key","normal"],["Universe label","Feb 14, 2026 (normal)"],["Clock line","Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)"],["Seed bound","freeze_utc 2026-02-14T00:00:00Z"],["shutdown_rules_apply","true"],
 ["Persona","Owen Baker, Game Engineer (Unity), owen.baker@harmonygames.co, roster owen_baker"],["Function · competency · skill","Engineering · Engineering Ops · Actions"],["Evals category","Engineering & Live-Ops (`Evals/references/rules/task_categories.md`)"],
 ["Task type · mode","long-horizon · medium, platform cap under 85 %"],["Requester targets","over 130 counted calls in every run; average strictly under 80 %; all other difficulty guidelines"],["Loss budget","E[average] ≤ 72 % (requester line less 8 points)"],
 ["Effective profile","extreme (Long Horizon)"],["Volume exception","call_budget_floor 250, per_record_floor 100, requester-delegated; ≥ 500 needs padding. The per-record floor is 100, not the 200 in the analysis, because the gate counts read surfaces only"],
 ["Theme screen","Domino Delights: no bio-adjacent theme. The ZM canvas is a scoped-out decoy and no seed uses zombie, infection or outbreak words"]]))
A("\nPersona census, `persona_view.py reach owen_baker --top 10`, verbatim:\n")
A(fence(rd("reach.txt")))
A("\nRemit, from before-freeze sources: Owen holds 16 of the 28 UI children (for example ENG-2417, ENG-2432); his fixes sit in the canvas threads (CE156FDFB428/1763549617.765149); he owns open items such as the mega tile (C05V5FNLB9V/1764262971.568809). He is still active: harmonygames-Games/Combo-Fighters#37 merged Feb 13 and his last DM to Arthur is D05S1S2AB5M/1770934881.073719. Linear ticket work on a live game is squarely his, and `role_reviews.scenario` is recorded in `00_V3_Authoring_Evidence.json`.\n")
A("## 1 Storyline\n")
A("Leonard can't drop Slack yet but will (C09UHHN6PFZ/1770842590.881439), Linear stays through the transition, and DD's bug record exists only in Slack: Vincent's canvas and #god-bugs. Linear went quiet on Nov 7. BoomBit wants a sync next week (C09SWTHEMEW/1770977006.104929), so Arthur asks Owen to move the whole list into Linear and close out the UI tree.\n")
A("Anchors and spine (every id YES for Owen, or planned):\n")
A(tbl(["Service","Record","Role"],[
 ["slack",M["anchors"][0]["locator"]+" (planned)","hub: Arthur's DM (AN1)"],["linear","ENG-2401","UI Changes master ticket (AN2), 3 masters and 28 children"],
 ["slack","CE156FDFB428/1763041126.468099 to /1763737449.845379","63 canvas lines, 55 ticked, 8 unticked"],["slack","C05V5FNLB9V/1763042988.277099","Vincent posts the list"],
 ["slack","C05V5FNLB9V/1764256187.655299 to /1766415326.501939","7 later bugs"],["slack","C05433XK267/1765310004.760809","build log: fix line in a submission build"],
 ["slack","C09SWTHEMEW/1764659626.614679","Leonard: lives removed for tickets"],["slack","C05KNDCHAAG/1770839984.194409","Feb 11 shutdown post, Google archive by Feb 15"],
 ["gdocs","f_948768f5a462e7037d17c9","economy doc"],["github","harmonygames-Games/GameOfDominoes#1913","open PR"],["github","harmonygames-Games/GameOfDominoes#1914","open economy PR; its commit list defines the economy line"]]))
A("\nKB placement: `universe_kb/by_universe/normal/timeline.json` rows 2025-11-02 (web port and UI work), 2025-11-07 (planning tools go quiet), 2026-02-09 and 2026-02-11 (wind-down), 2026-02-13 (work continues). Cohorts from `cohorts.json`: LIN-EPIC (children of epics), LIN-OPEN-ENG (open ENG issues, source of reuse candidates), SL-T05 (#god-bugs 2025 roots), GH-Q08 (GameOfDominoes 2025-Q4 PRs). `trap_catalog.json` entries: K01 (canvas pseudo-channels), N03 (branch keys), C01 and C02 (thread corrections and parent resolutions), D07 (Trello stale against Linear), B04 (Jenkins in #builds).\n")
A("Natural services (11): slack, gmail, gcal, gdrive, gdocs, gsheets, linear, github, trello, confluence, snowflake. Injected (10): slack, gmail, gcal, gdrive, gdocs, gsheets, gslides, linear, github, trello. Confluence and Snowflake stay out of the graded path (NB-21 and learnings §26).\n")
A("Coupling seams: a mail changes which ticket a canvas line lands on (C5); a spec in Docs voids three lines read in Slack (C2); an inline review changes a Linear state (C1); a DM reverses a tick (C3); a commit closes an open thread (C4).\n")
A("## 1a Coherence audit\n")
A("Scope: every record a correct run opens. Hazards from `coherence_hazards.json`; cards from `references/known_data_issues/normal.md`.\n")
A(tbl(["Record","Category","Fields","Pointer","Hazard / card","Disposition"],[
 ["Seeded Slack near the export end","temporal","ts",M["anchors"][0]["locator"],"T07, NB-6","avoid: all seeded Slack ts before Feb 13 10:03 UTC"],
 ["Trello board quiet since Nov","temporal","dateLastActivity","card "+M['ask_fragments'][4]['container'],"T06, D07","fold into design: the card and comment date from Nov 5, before the board went quiet"],
 ["Linear activity after Nov 7","temporal","created_at","ENG-2401 comment "+[s for s in SEED.values() if s['service']=='linear'][0]['id'],"T04","fold into design: Arthur's Feb note is on an open master"],
 ["Seeded notes on closed children","temporal","created_at","ENG-2417","T05","avoid: no seeded comment on a child after completed_at; closed children take none"],
 ["Labels mix sprints and codenames","semantic","labels","ENG-2410","S03","avoid: only the Bug label is used"],
 ["Contacts job titles","semantic","job","ENG-2401 authors are not titled; contact 4e13bd40cc73d0fc76f87c7d","S06","avoid: no title is graded"],
 ["Canvas title date against comment dates","semantic","title","CE156FDFB428/1763041126.468099","K01","avoid: no build number or canvas date is graded (NB-21)"],
 ["Slack cites keys or PRs not in export","cross-service referential","text","C05V5FNLB9V/1763042988.277099","R01, R02","avoid: seeds cite only keys and PRs proved by records"],
 ["Google-native doc links in Slack","cross-service referential","url","C05V5FNLB9V/1764662837.138929","R04","avoid: Robert's QA doc link is not used; the rule doc scopes population by post"],
 ["Thread reply counters","quantitative","reply_count","C05V5FNLB9V/1766415326.501939","Q01, Q03","fold into design: a seeded reply updates the parent's counters"],
 ["Tree children in state PR with merged PRs","state/lifecycle","state","ENG-2417 and harmonygames-Games/GameOfDominoes#1901","L01, L07","fold into design: the SQL leaves these states alone; closing them out is the job Arthur gives, so PR on a merged ticket is the stale status it reconciles"],
 ["ENG-2405 Todo with merged PR","state/lifecycle","state","ENG-2405 and harmonygames-Games/GameOfDominoes#1905","L03","fold into design: the SQL leaves it alone and the rule doc keeps the masters as they are"],
 ["Master checklists against child states","state/lifecycle","description","ENG-2404","NB-14","repaired: the SQL clears the ENG-2403 and ENG-2404 checklists, so they can't disagree with the child tickets"],
 ["Message ids and mailbox aliases","identifier/format","id",SEED["mail"]["id"]+" style ids; base files use owen@harmonygames.co","I02, I03","fold into design: seeded ids follow `id_contracts.json`"],
 ["Branch names differ between lists and Slack","identifier/format","name","C05433XK267/1765310004.760809 against the branch list","NB-13","avoid: no exact branch name is graded"],
 ["Owen left #god-bugs on Feb 11","other","membership","C09UHHN6PFZ/1770842566.250369","NB-1","repaired: Arthur puts Owen on a spare paid seat, and he rejoins the DD channels on Feb 12 before Arthur's DM; the platform /prompt failed rev2 on this"],
 ["Slack DM member lists","other","members","D05S1S2AB5M/1770934881.073719","NB-31","avoid: no access argument rests on member lists"],
 ["Linear base comments","other","comments","ENG-2401","NB-24","fold into design: every Linear comment here is seeded"],
]))
A("\nSibling-defect sweep: the designed 'merged but not done' defect has siblings across the tree. All 19 open children were reviewed; their planned states are in `plan/truth_sketch.json`, and the blind fork sweep (section 13) re-read them.\n")
A("## 1b Active speakers\n\nStatus from `universe_kb/by_universe/normal/activity.json`:\n")
A(tbl(["Person","Email","status_at_clock","Seeding role"],[
 ["Arthur Blake","arthur.blake@harmonygames.co","active_feb_2026","hub DM, rule doc, master note, inline reviews, invite"],
 ["Brian Foster","brian.foster@harmonygames.co","active_feb_2026","check notes on three Validation children, thread replies, DM, Trello comment and checklist, deck; dated Sep–Dec 2025"],
 ["Vincent Parker","vincent.parker@harmonygames.co","quiet_since_2025-12","mail, ticket note and canvas replies, all dated by Nov 23, 2025"],
 ["Oliver Brooks","oliver.brooks@harmonygames.co","active_feb_2026","Season Pass note; invited"],
 ["Robert","robert@harmonygames.co","active_feb_2026","invited; base bug posts only"],
 ["Leonard Hayes","leonard.hayes@harmonygames.co","active_feb_2026","not seeded; base posts only"],
 ["Marcus Bennett","marcus.bennett@harmonygames.co","active_feb_2026","1:1 note to Owen on Dec 11; base #1913 and thread"],
 ["Owen Baker","owen.baker@harmonygames.co","active_feb_2026","the persona; recipient of seeds"]]))
A("\n## 1c Identity traps\n\n`entity.py collisions`, verbatim:\n")
A(fence(coll)); A("\n`entity.py resolve \"Owen Baker\"`, verbatim:\n"); A(fence(ent))
A("\nPinned: Marcus is Marcus Bennett (marcus.bennett@harmonygames.co), not Marcus Lee or the `marcus@` mailbox. Owen Baker is not Thomas Baker. Brian is Brian Foster. No second account is created for anyone.\n")
A("## 2 Cohort spine\n")
A(f"Rule: {M['cohort']['definition']}. Source: the hub and H1. Size {M['cohort']['size']}; the design stays inside 40–150.\n")
A(tbl(["Surface","Tool","Records","Calls each","Requirement","Why no bulk","Short circuit"],[[s["service"],s["tool"],s["records"],s["per_record_calls"],s["requirement"],s["why_no_bulk"],s["short_circuit"]] for s in M["cohort"]["evidence_surfaces"]]))
A("\nPredicate: four outcomes, closed vocabulary, in H1 f_3ca9e15d7b20f4e681ad52: Fixed, Broken, Gone, Covered. House rule that overrides the natural reading: a tick stands only until a later record about that bug. Effective-date regime: the economy change removes lives from the build players have (C09SWTHEMEW/1764659626.614679). Boundary records: 7 later bugs (C05V5FNLB9V/1764256187.655299), and the shortlist of Robert's sub-250 reports the rule folds into the canvas (C09Q4S613CN/1764013026.858409).\n")
A("Shortcut audit: `slack_search_public_and_private` can sweep canvas replies, so that surface counts at half. No call returns Linear comments or inline PR comments in bulk. The writes have no batch form.\n")
A("## 3 Hidden authorities\n")
A(tbl(["Id","Name","Home","Record","Decoy","Governs","Findable by"],[[a["id"],a["name"],a["home_service"],", ".join(a["seeded_ids"]),", ".join(a["decoy_seeded_ids"])+f" ({a['decoy_scope']['dimension']}: {a['decoy_scope']['decoy']})",", ".join(a["governs"]),a["findable_query"]] for a in M["authorities"]]))
A("\nBoth are named by role. H1 is named in the hub; H2 is named in H1 without saying where it sits. Findability proof runs at injection, because both are planned seeds.\n")
A("## 4 Delegation lattice\n")
A(tbl(["Anchor","Anchor name (noun phrase, ≤ 6 words)","Record"],[[a["id"],a["prompt_reference"],a["locator"]] for a in M["anchors"]]))
A("\nHub: AN1 in Arthur's voice delegates by role. It names no bug, no authority location and no channel.\n")
A("Fragments and incorporation (quotes are exact substrings of the planned record in `plan/seed_text.json`):\n")
A(tbl(["Id","Service","Container","Kind","Via","Delegated by","Quote","Requirements"],[[f["id"],f["service"],f["container"],f["kind"],">".join(f["incorporated_via"]),f["delegated_by_record"],f["delegation_quote"],", ".join(f["requirement_ids"])] for f in M["ask_fragments"]]))
A("\nAmendment: K4, Arthur's later note on ENG-2401, adds the title prefix and leaves the rest of H1 standing. Distractors outside the chain are in section 5.\n")
A("## 5 Chains and trap register\n")
A(tbl(["Chain","Root cause","Hops","Ends in"],[[c["id"],c["root_cause"]," → ".join(f"{h['service']} {h['record']}" for h in c["hops"]),c["ends_in"]] for c in M["chains"]]))
A("\n")
A(tbl(["Trap","Family","Records","Requirement","Expected wrong reading","Resolver","Discovery order"],[[t["id"],t["family"]+(f" ({t['distractor_type']})" if t.get("distractor_type") else ""),", ".join((t.get("seeded_ids") or [])+(t.get("base_pointers") or [])),t["requirement"],t["expected_wrong_reading"],t["resolver"],t.get("discovery_order","-")] for t in M["traps"]]))
A("\nHardness v2 selection (`Hardness_Mastery.md` §13): trap 1 (INLINE, LINE), trap 2 (REPLY, BACK), trap 3 (FOLLOW), trap 5 (GONE), trap 6 (ALIAS), trap 9 (ELSE). Each names its convincing wrong source and beating record in the table above and flips a weight-5 slot.\n")
A("### Mechanism portfolio (S5a)\n\nCandidates, grounded in records. Priors are from `hardness_ledger.py priors --model claude-opus-5-5`.\n")
A(tbl(["#","Anchor storyline (cited)","Coupling","Characteristic","Discovery-order proof","Reach","Findability term","Gradable fact","Services","Walk Δ vs tier","Risks"],[
 ["1","tree child, harmonygames-Games/GameOfDominoes#1905","inline review changes a Linear state","done gap","PR merged is read first","YES","how-to-play","child stays open","github, linear","+13 reads","all-fail rows; selected"],
 ["2","ticked line CE156FDFB428/1763549455.195819","reply reverses a tick","correction off path","tick read first","YES","round icons","line Broken","slack","none","selected"],
 ["3","ticked line CE156FDFB428/1763642831.967359","DM reverses a tick","correction off path","tick read first","YES","Tavern","line Broken","slack","none","DM sweeps; selected"],
 ["4","rule comment on card "+M['ask_fragments'][4]['container'],"rule changes every note","follow-through","rule doc read first","planned","close these out","note names the build","trello, linear","none","board actions call; selected"],
 ["5","line CE156FDFB428/1763548856.943389","spec voids a bug","rule in older records","line read first","YES","lives","line Gone","slack, gdocs","none","judgement; selected"],
 ["6","window post C05V5FNLB9V/1764329192.159229","open PR denies a fix","done gap","reply reads as closed","YES","tile dozer","line Broken","slack, github","+1","stated rule; selected"],
 ["7","flicker post C05V5FNLB9V/1764659550.713509","commit closes a thread","completion elsewhere","thread read first","YES","flicker","bug Fixed","slack, github","+2","selected"],
 ["8","line CE156FDFB428/1763041538.186339","mail ties line to ticket","alias","title search first","YES","sign in","reuse ENG-2073","slack, gmail, linear","+2","selected"],
 ["9","later posts C05V5FNLB9V/1764256187.655299","rule widens the list","outside the filter","canvas read first","YES","bug channel","bug present","slack","+9","rule doc must name the channel, so it leaks: kept as a trap with control rows, no rule"],
 ["10","deck "+"f_d15a8c70e3f2b94a61c8d3","summary against records","stale summary","deck is short","planned","wrap","children stay","gslides, linear","+1","kept as a distractor"],
 ["11","Robert's sub-250 reports C09Q4S613CN/1764013026.858409","scope edge","scope adjacent","search hits them","YES","sub-250","not filed","slack","none","kept as a distractor"],
 ["12","iOS-only line CE156FDFB428/1763642769.995649","platform scope","exception","thread shows ios","YES","ios","filed anyway","slack","none","rejected: adds a fork, no landing"],
 ["13","build numbers in C05433XK267/1765310004.760809","boundary date","date window","log is long","YES","build","qualifies or not","slack","+6","rejected: NB-21 and SC-67-style joins are unsafe"],
]))
A("\nSelected rules:\n")
EV={"INLINE":"harmonygames-Games/GameOfDominoes#1905","REPLY":"CE156FDFB428/1763549455.195819","BACK":"CE156FDFB428/1763642831.967359","FOLLOW":"ENG-2417","ELSE":"C05V5FNLB9V/1764659550.713509","GONE":"C09SWTHEMEW/1764659626.614679","LINE":"harmonygames-Games/GameOfDominoes#1913","ALIAS":"ENG-2073"}
A(tbl(["Rule","Record","Mechanism","Prior family","Why it applies","Nodes","Natural reading","Prior (record ids)","Controls","Over-application","After complete retrieval","Slots"],[[p["id"],EV[p["id"]],p["mechanism"],p["prior_family"],p["prior_family_reason"],", ".join(p["nodes"]),p["natural_reading"],(f"Beta({p['prior']['alpha']},{p['prior']['beta']}) "+", ".join(p['prior']['record_ids'][:3])) if p.get("prior") else "none",", ".join(p["controls"]),p["over_application"],{"GONE":"join needed","ALIAS":"join needed","LINE":"claim must be doubted"}.get(p["id"],"retrieval-shaped, placement decides"),", ".join(p["decides"])] for p in M["mechanism_portfolio"]]))
A("\nFour A5b checks per rule: **incorporated** (each chain runs from AN1 through H1 or a fragment); **tool-surface proof** (each deciding record is returned by the natural call for its service, checked in the pre-check); **graded weight** (slots above); **survives retrieval** (column above).\n")
A("### Liveness flags (S5b)\n\n`trap_liveness.py --design`, verbatim:\n")
A(fence(rd("liveness.txt"))); A("\n"+rd("liveness_disp.md","")+"\n")
A("`hardness_v2_check.py --design`, verbatim:\n"); A(fence(rd("v2.txt")))
A("\nDispositions: no FLAG or UNRESOLVED. The tool reads declared containers, so it re-runs on the SQL. BACK and REPLY are Slack-to-Slack: cross-container, not cross-service.\n")
A("## 6 Failure-diversity plan\n")
A("Each channel is found by a different habit, so runs fail different subsets: INLINE (reading inline comments on PRs), REPLY (opening a thread under an unrelated post), BACK (reading a 1:1 with Marcus), ELSE (reading #builds or a DM with Brian), FOLLOW (reading a card comment), GONE (asking what the live build contains), LINE (looking a PR up), ALIAS (searching mail and ticket notes). No discovery gates most requirements: the largest channel, GONE, moves about 20.5 % of the weight (`plan/policy_model_output.txt`). Trap independence: each rule has its own member, so a run that beats the others can still fail it. Records: C05V5FNLB9V/1764329192.159229, CE156FDFB428/1763642831.967359, harmonygames-Games/GameOfDominoes#1905.\n")
A("## 7 Deliverables and dependent writes\n")
A(tbl(["Write","Tool","Count","Depends on","Requirements"],[[w["service"],w["tool"],w["count"],", ".join(w["depends_on"]),", ".join(w["requirements"])] for w in M["writes"]]))
A("\nReuse-versus-create: two lines reuse ENG-2073 and ENG-2363. High-count writes are template-identical, so the rubric can sample them: the tick-line tickets, the child moves and the child notes. Full plan in `plan/truth_sketch.json`.\n")
A("## 8 Service role map\n")
rows=[[k,v["role"],v["weight_reason"],"●"] for k,v in M["services"].items()]
rows+= [["contacts","not used","no load-bearing fact","○"],["confluence","base only, off the graded path","no load-bearing fact","○"],["snowflake","off the graded path","NB-21 joins are unsafe","○"]]
A(tbl(["Service","Role","Load-bearing fact or write","Carrier"],rows))
A("\n## 9 Call budget\n")
A(tbl(["Phase","Service","Calls","Reason"],[[b["phase"],b["service"],b["calls"],b["reason"]] for b in M["call_budget"]]))
tot=sum(b["calls"] for b in M["call_budget"])
A(f"\nTotal {tot} unconditional calls over 10 services. The requester's floor is over 130 in every run: about 120 per-entry writes happen whichever traps land, and reads have not fallen below 54 on comparable stored runs, so the model's mean six-run minimum is about 182 (`plan/policy_model_output.txt`, UNCALIBRATED). The golden-run rule still applies: a correct run needs these calls. Filing only unfixed lines would cut about 55 writes and put the weakest run near 116, which is why the whole list goes over.\n")
A("## 10 QC rails\n\n### Two-reading table\n")
TWO=[
 ["What 'still broken' tests","the build players have (H1)","develop","H1 f_3ca9e15d7b20f4e681ad52 states it"],
 ["A tick with no later record","Fixed","re-verify every line","H1: a tick stands unless a later record says otherwise"],
 ["Lives lines","Gone","Broken, or covered by ENG-2277","C09SWTHEMEW/1764659626.614679, f_948768f5a462e7037d17c9 and C05KNDCHAAG January no-lives post"],
 ["Tile dozer window","Broken","Fixed on Marcus's word","harmonygames-Games/GameOfDominoes#1913 open; H1: an open PR doesn't count"],
 ["Flicker thread","Fixed","Broken, nobody closed it","commit a6fb440f0c in #1914 and C05433XK267/1765310004.760809"],
 ["Apple sync line","Covered by ENG-2073","new ticket, or ENG-2280","Vincent's mail "+SEED['mail']['id']],
 ["Population edge","canvas plus bug channel","Robert's sub-250 reports too","H1 folds them in; base C09Q4S613CN/1764092109.741509"],
 ["Child with a merged PR and an inline hold","stays","Done","Arthur's inline comment "+SEED['inline_td']['id']+" says it must be done first"],
 ["Which note wording","names the build","any line","H2 "+SEED['rule_comment']['id']],
 ["Share list","Arthur, Robert, Oliver","everyone on the DM","invite "+SEED['invite']['id']],
 ["Ticked line about lives or Win & Collect","Fixed","Gone","H1: take the first outcome that fits, and Fixed comes first; CE156FDFB428/1763042343.632569"],
 ["Unticked lives line against open ENG-2277","Gone","Covered","H1 order puts Gone before Covered; ENG-2277"],
 ["Train and team lines with a fix commit","Broken","Fixed by the commit","Vincent's later replies "+SEED['train_reply']['id']+" and "+SEED['team_reply']['id']+" say they still happen; H1: nothing later says otherwise is the test"],
 ["ENG-2424 with no hold note","stays","Done","Owen's Dec 16 post C9CA62B5180A/1765927876.696389 says the event is disabled; no re-enable is on record"],
 ["A broken bug on an open child's screen","child still moves","child held","H1: a bug on a screen doesn't hold its child; ENG-2432"],
]
A(tbl(["Decision point","Best reading","Strongest alternative","Resolved by"],TWO))
A("\n### Reach table (load-bearing records)\n\nEvery scoped base record below is YES for Owen (`persona_view.py can-see owen_baker …`); planned seeds are checked by `check-sql` at injection:\n")
A(fence(rd("reach_lb.txt")))
A("\nFeasibility: `linear_create_issue` (team, parentId, labels, state), `linear_update_issue`, `linear_create_comment`, `gsheets_create_spreadsheet`, `gdrive_move_file`, `gdrive_share_file` and `slack_send_message` are all in `Evals/references/tools/catalog.json`. Owen owns the folder d_9b41e7c2a05d36f8e1c7a4 and the sheet he creates (learnings §31). Linear is unscoped.\n")
A("Precedence: load-bearing facts sit only in ● carriers, with Linear comments ● per `Ask_Carriers.md` §6b. No fact lives only in a GCal description or on Confluence. Naturalness: the prompt names the DM, the tree, the folder and the reply; it names no bug, channel, rule or count. Grading devices: exact counts, ≤ 5 samples per group plus a volume slot, one row per trap member, exclusions as a state or count on a required write, never 'leaves X alone'.\n")
A("### Coherence rail\n\nEvery section 1a row is dispositioned. Every designed disagreement is a dated human claim with a later record. Companions are planned in section 11. Claims about base artifacts stay observational: `00_PreScenario/git_containment_check.txt` shows #1913's commit 4e344c5291 is not in #1914's list, and fix commits a6fb440f0c, 9afe3918b5 and d0b222c9cf are. The git export holds only 50 commits on main, so branch containment comes from the PR commit lists. No exact branch name is graded (NB-13).\n")
A("## 11 Record plan for /create-injection\n")
HOME={"amend":"ENG-2401","alias_note":"ENG-2363","season_note":"ENG-2428","gift_note":"ENG-2437","rule_comment":M['ask_fragments'][4]['container'],"zm_comment":"6851a6569f3bf818760632ab","bar_reply":"C05V5FNLB9V/1766415326.501939","brian_reply":"C09Q4S613CN/1764042435.541279","train_reply":"CE156FDFB428/1763394823.486369","team_reply":"CE156FDFB428/1763549817.580759","lives_reply1":"CE156FDFB428/1763548856.943389","lives_reply2":"CE156FDFB428/1763642552.651279","inline_td":"harmonygames-Games/GameOfDominoes#1905","inline_axe":"harmonygames-Games/GameOfDominoes#1908"}
A(tbl(["Seed","Service","Id","Home record","Author","At","Purpose"],[[k,v["service"],v["id"],HOME.get(k,v["id"]),v["author"],v["at"],v["text"][:90]] for k,v in SEED.items()]))
A("\nAlso planned, each with a stated purpose: Brian's check notes on the Validation children ENG-2410, ENG-2429 and ENG-2430; Brian's 28-item screen checklist on the Trello card, the per-screen record for the children in PR state; triage notes on open ENG bug tickets (reuse controls, for example ENG-2280); PR conversation comments on the 13 merged tree PRs with INT-01 copies in #engineering-bots C050WGU41HR; control replies on ticked lines in CE156FDFB428; Drive and Docs rows for f_3ca9e15d7b20f4e681ad52, f_72e0b4c3d91a5f68c2b7e4, f_d15a8c70e3f2b94a61c8d3 and d_9b41e7c2a05d36f8e1c7a4; the Trello card and its comment on list 66c38013d3990617429e50e3 with the ZM decoy card on board 6851a6569f3bf818760632ab; GCal copies of evt_6e2c91d4b07f3a58c1d2e4 per attendee; SQL UPDATEs moving the 14 PR-state tree tickets and ENG-2405 to Validation. Estimated 110–135 INSERTs. If honest evidence falls short, that comes back to the requester rather than being padded.\n")
A("### Integrations and companions\n")
A(tbl(["Service","INT id","Companion","Decision"],[
 ["github","INT-01, INT-02, INT-12","Slack app mirror; push notices; notification mails","INT-01 copies for each seeded PR comment in C050WGU41HR under the PR's opened message; review containers declared per learnings §53"],
 ["linear","INT-03, INT-04, INT-05","linear[bot] on PRs; Slack posts; digests","none needed for comments on open tickets; declared at injection"],
 ["gcal","INT-11","invitation mails","seed invitations for attendees, or no_notify"],
 ["gdrive","INT-13","Drive app DMs","none: shares by notice only; declared"],
 ["slack","INT-22","Slack email notices","none for DMs after the plan change; declared"],
 ["trello","INT-21","no Trello to Slack integration","none"],
 ["gmail","none","Vincent's mail is ordinary mail","none"],
 ["jenkins (slack)","INT-06","#builds job posts","none seeded: base posts only"],
]))
A("\n## 12 Self-test results\n\n`hardness_gate.py --design`, verbatim:\n"); A(fence(rd("gate.txt")))
A("\n`gradable_surface.py validate`, verbatim:\n"); A(fence(rd("surface.txt")))
A("\n`gradable_surface.py gradeable-report`, verbatim:\n"); A(fence(rd("gradeable.txt")))
A("\nLazy-solver pass: a run that reads the canvas once and files ticks as written scores about a quarter of the surface (`plan/policy_model_output.txt`); the points it keeps are sampled lookups and delivery rows, with no leak on a trap row. Literal-value sweep: `0.3.310` appears only in H1 and in notes the run writes. Wording sweep: the corrections avoid 'canvas' and ticket words (C09Q4S613CN thread, D05USBTQY1F). 'The rest stands': K4 changes one clause and no later record restates it.\n")
A("Requester targets, whole policies and six-run model, UNCALIBRATED:\n"); A(fence(open(os.path.join(HERE,"policy_model_output.txt")).read().rstrip()))
A("\nS9b prior forecast (advisory, UNCALIBRATED): "+rd("forecast_line.txt","not yet run")+"\n")
A("### Self-review\n\nRe-read `Evals/1_Prompt_Eval.md` §2.1, §2.2 and §3.2 and `Evals/0_Injection_Quality_Eval.md` Check C in order.\n")
A(tbl(["Area","Counter-reading (strongest argument it fails)","Resolution (evidence)"],[
 ["temporal","the hub could postdate the export and read as invented",f"hub {M['anchors'][0]['locator']} is before Feb 13 10:03 UTC; NB-6; T07 hazard avoided"],
 ["temporal","Vincent's replies could postdate his exit","CE156FDFB428/1763845212.507119 is Nov 22; his last Slack is C09Q4S613CN/1763890610.357549"],
 ["semantic","'Gone' could read as deleted from the backlog","H1 f_3ca9e15d7b20f4e681ad52 defines it as a bug in something the live build lacks"],
 ["semantic","a tick might mean only 'looked at'","H1 says a tick stands; Vincent's own words at C05V5FNLB9V/1763042988.277099 call the list remaining issues"],
 ["cross-service referential","the mail names ENG-2073, which must fit the line","ENG-2073 'Sign-In Account Synchronization Issues' is open; line CE156FDFB428/1763041538.186339"],
 ["cross-service referential","a seeded inline comment needs a PR that took reviews","harmonygames-Games/GameOfDominoes#1905 has Arthur's APPROVED review; the comment predates merge"],
 ["quantitative","the counts could cancel out","V1 and the reply rows sit beside named member rows; CE156FDFB428/1763642831.967359"],
 ["quantitative","68 new tickets assumes 63 plus 7 less 2","plan/truth_sketch.json: 70 items, 2 Covered; ENG-2073 and ENG-2363 take notes"],
 ["state/lifecycle","tree tickets in PR state fail coherence on presence","L01, L03, L07 left as they are: the job reconciles them, so the SQL updates no such ticket; ENG-2417"],
 ["state/lifecycle","a Done child could need reopening","no closed child is touched; ENG-2411 stays Done"],
 ["identifier/format","a seeded id could collide","every minted id was checked with `hg.py records` and scoped Slack searches, with a positive control: `plan/out/id_collisions.txt`, 0 hits; f_3ca9e15d7b20f4e681ad52"],
 ["other","Owen can't read #god-bugs as a guest","the SQL seeds his rejoin in each DD channel on Feb 12, and C05V5FNLB9V/1764256187.655299 predates Feb 11"],
 ["other","filing 58 fixed lines is padding","hub gives the reason: the list exists only in Slack; each is a distinct bug; long_horizon.md; CE156FDFB428/1763041126.468099"],
]+[[f"decision: {r[0]}",f"the alternative '{r[2]}' could be a fair answer",f"{r[3]}"] for r in TWO]))
A("\nSources re-read through `tools/hg.py` this stage: every base pointer in sections 1 and 5. `hardness_gate.py --design` output is pasted in section 12: HARDNESS GATE (extreme (design)): PASS.\n")
A("Unresolved: no independent model review of the design (RED TEAM FALLBACK in section 13); rubric growth is the main risk to the 80 % target; `linear_create_issue` at volume and a direct read of the canvas channel are to be confirmed in the pre-check; ≥ 120 INSERTs is tight.\n")
A("## 13 Red team (dual)\n\nRED TEAM UNAVAILABLE: REDTEAM_* is unset (0 variables), so tools/redteam_review.py --dual cannot reach a reviewer.\n")
A("RED TEAM FALLBACK: two independent fresh Claude agents (general-purpose subagents, hg.py only, no prompt and no solver) ran blind sweeps: one tried to break every planned outcome as the /prompt UGT reviewer, one tried to fail every seed against the whole base as the /injection and coherence reviewer. Chosen under the requester's delegation of 2026-11-07 because no second model family is reachable. Their reports are `plan/sweeps/fork_sweep.md` and `plan/sweeps/coherence_sweep.md`.\n")
A(FORK+"\n")
open(os.path.join(WF,"01_Scenario_Design.md"),"w").write("\n".join(S))
print("design written",sum(len(x) for x in S))

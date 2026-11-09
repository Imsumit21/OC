#!/usr/bin/env python3
"""Assembles Working_Files/04_Prompt_Writing_Brief.md from the solver, the seeds, the persona searches and the entity output."""
import hashlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
sys.path.insert(0, os.path.join(WF, "solver"))
import solver  # noqa: E402
SEED = json.load(open(os.path.join(HERE, "seed_text.json")))
SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
st = solver.load_state(SQL)
rows = solver.solve(st)
AGG = solver.aggregates(rows)
C, R = AGG["classes"], AGG["reply"]
SAP = json.load(open(os.path.join(HERE, "sap", "summary.json")))
sid = lambda n: hashlib.sha256("|".join(SEED[n]["id"].split("/")).encode()).hexdigest()[:32]
MAIL = st["mail"]
HUB = SEED["hub"]["id"]
DOC = SEED["rule_doc"]["id"]
FOLDER = "d_9b41e7c2a05d36f8e1c7a4"
L = []
A = L.append
A("# Prompt Brief — owen_dd_bug_carryover · prep")
A("> Built 2026-11-08 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Grounding_Dossier.md (injection rev7; rev2 and rev4 failed /prompt on data findings, rev3 failed /injection on two join rows, rev5 passed both, rev6 added second carriers for four corrections and failed /prompt on the tooltips thread, rev7 closed that thread and passed /prompt 5 but failed /hardness 1, rev8 removed Brian's Apple line and failed /hardness 2, rev9 removes his Tavern line and moves his Daily Gift note into his DM), 01_Scenario_Design.md, 01_Hardness_Manifest.json, 03_Error_Async_Config.txt (Friction: none) · Persona view verified: all (check-sql PASS, §5a)")
A("> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human. No 02_Reference_Files: the scenario needs no attachment.\n")

A("## 1 · Assignment fit\n")
A("| Axis | Assigned value | What it requires here (cited) |\n|---|---|---|")
A("| Business function | Engineering | Engineering & Live-Ops in `Evals/references/rules/task_categories.md` (engineering delivery, releases, incidents, live game operations): Domino Delights' bug record and its live build. |")
A("| Persona | Owen Baker · owen.baker@harmonygames.co · Game Engineer (Unity) (roster.json persona_key owen_baker, department Engineering) | Voice: short and plain, first person to his assistant, as in CE156FDFB428/1763549617.765149 'Should be fixed now'. Remit: he holds 16 of the 28 UI children (ENG-2417, ENG-2432), fixed canvas lines himself and owns the flicker and music threads (C05V5FNLB9V/1764659550.713509). Read scope: his DMs D05S1S2AB5M, D05USBTQY1F, D07E9PSQB6W, the group DM C9CA62B5180A, channels CE156FDFB428, C05V5FNLB9V, C05433XK267, C09Q4S613CN, C09SWTHEMEW, his mailbox, calendar and Drive. |")
A("| Competency | Engineering Ops | Epic and task management: the bug record moves into the tracker and the ENG-2401 tree is closed out. Arthur asks him because he worked the list (hub " + HUB + "). |")
A("| Task skill | Actions | Exercised by 68 new tickets, 2 notes on reused tickets, 14 child moves, 28 child notes, the sheet, its sharing and the reply. Retrieval and reconciliation stack under it. |")
A("| Task type | long-horizon (Long Horizon; difficulty mode medium, V3 cap < 85 %; requester target < 80 % average, > 130 counted calls per run) | Services carrying weight: Slack (63 canvas lines, 7 later posts, corrections), Linear (28 children, 13 notes, every write), GitHub (10 PRs, 2 inline comments), Docs (rule doc, economy doc), Drive, Sheets, Slides, Trello, Gmail, Calendar. Call budget 285 (01_Hardness_Manifest.json); the prompt states no count. |\n")

A("## 2 · Situation\n")
A("| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |\n|---|---|---|---|")
A(f"| Slack is about to drop to the free plan and take DD's bug history with it; Arthur asks Owen to move the whole list into Linear. | Owen (DM recipient) | {HUB} | — |")
A(f"| The list lives as a Slack canvas comment channel and later posts, with ticks that may not match where each bug stands today. | Owen | CE156FDFB428/1763041126.468099; C05V5FNLB9V/1764256187.655299 | — |")
A("| The UI Changes tree never got closed out: children sit in PR, Validation or In Progress long after the work ended. | Owen (Linear, unscoped) | ENG-2401; ENG-2417 | — |")
A("| Only one record names the public build by number, and Owen can't see it. | Arthur, Leonard | the rule doc names 0.3.310 for Owen: " + DOC + " | D04UGG61DUM/1770846601.876869 (not needed: the rule doc is the authority) |\n")

A("## 3 · Investigation → action\n")
A("Questions to resolve (no answers here):")
for q in ["Which lines and posts are in scope, and which channels stay out?", "Which outcome does each bug get under the carry-over notes' first-fit order, going by the build players have?",
          "Does any later record, in any channel, DM or mailbox, change what a tick or an open thread says?", "Which fixes actually reached that build?", "Is any line already covered by an open ticket?",
          "Which open UI children have part of their screen missing from that build?", "What does each child's note have to say?", "Who is on Sunday's review?", "Has anything changed since the notes were written?"]:
    A("- " + q)
A("\nWrites those answers feed: one Linear record per bug, a note on any reused ticket, a state and a line on each child, the sheet and its sharing, the reply. Every write depends on the investigation.\n")

A("## 4 · Pinned final state (UGT anchor)\n")
A("| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |\n|---|---|---|---|---|---|")
A(f"| New tickets | one per bug that gets a new record, fields per {DOC} and comment_49b5ac4788465f72ddf245e34f2b7034 | Linear team_ENG, parent ENG-2401 | — | linear_create_issue | outcome of each line |")
A("| Notes on reused tickets | the canvas wording | ENG-2073, ENG-2363 | — | linear_create_comment | ties to open tickets |")
A("| Child moves | open children whose screen is all in the build go Done | children of ENG-2403, ENG-2404, ENG-2405 | — | linear_update_issue | tree question |")
A("| A line on every child | where it landed, naming the build (690b29bc3c7d2e51b0f86a47) | all 28 children, ENG-2409 to ENG-2437 | — | linear_create_comment | tree question |")
A(f"| Sheet | columns Bug, Outcome, Ticket, Why; one row per bug | Owen's folder {FOLDER} | arthur.blake@harmonygames.co, robert@harmonygames.co, oliver.brooks@harmonygames.co (evt_6e2c91d4b07f3a58c1d2e4) | gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file, gdrive_share_file | every outcome |")
A(f"| Reply to Arthur | how many are still broken, how many new tickets, how many of the 28 children are Done | thread of {HUB} | arthur.blake@harmonygames.co | slack_send_message | the three counts |\n")
A("Alternatives a careful run could defend are settled or accepted in §4b. The forks a blind sweep found, and how each was closed, are in plan/out/sweep_dispositions.md.\n")

A("### 4b · Canonical outcome (all fair outcomes)\n")
A("| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by (quoted span, or —) | Allowed equivalence class | Material / representational | Source |\n|---|---|---|---|---|---|---|")
B4 = [
 ("New tickets", "count", f"{R['new_tickets']}: {C['Fixed']} Fixed, {C['Gone']} Gone, {C['Broken']} Broken (solver/truth.json)", "—", "—", "material", DOC),
 ("New tickets", "team, label, parent, assignee", "Engineering, Bug, ENG-2401, none", "—", "—", "material", DOC),
 ("New tickets", "title", "[2231] then the line without its tick box, or the first line of the post, as written", "—", "emoji codes and mentions kept or dropped; trailing spaces free", "material (prefix, wording) / representational (codes)", "ENG-2401 note comment_49b5ac4788465f72ddf245e34f2b7034; the bottom bar bug takes the first line of its first post, C05V5FNLB9V/1766415211.386389"),
 ("New tickets", "state", "Done for Fixed, Canceled for Gone, Bugs for Broken", "—", "—", "material", DOC),
 ("New tickets", "description", "empty", "—", "—", "material", DOC),
 ("Reused tickets", "note", "on ENG-2073 for the Apple line, on ENG-2363 for the manual sign-in line, carrying the canvas wording", "—", "wording around it free", "material", "owen.baker@harmonygames.co/1849333980856689601"),
 ("Children", "state", f"{R['children_done']} of {R['children_total']} Done: 9 already plus 14 moved; ENG-2424, ENG-2426, ENG-2428, ENG-2434, ENG-2437 stay in their current state; masters untouched", "—", "—", "material", DOC),
 ("Children", "line on each", "where it landed, on all 28", "hub: 'leave a line on every child saying where it landed'", "wording free", "material (presence) / representational (wording)", HUB),
 ("Children", "build in the note", "0.3.310 on all 28 lines: Brian's rule asks for the current public build, and the doc says that is 0.3.310", "—", "'0.3.310' or 'build 0.3.310'", "material", "690b29bc3c7d2e51b0f86a47"),
 ("Sheet", "location", f"in {FOLDER}", "—", "—", "material", HUB),
 ("Sheet", "title", "—", "hub: 'Put a sheet in your DD bug carry-over folder'", "any title", "representational", HUB),
 ("Sheet", "columns", "Bug, Outcome, Ticket, Why", "—", "order free", "material", DOC),
 ("Sheet", "rows", f"70: {C['Fixed']} Fixed, {C['Broken']} Broken, {C['Gone']} Gone, {C['Covered']} Covered", "—", "Outcome may read as the state (Done, Bugs, Canceled)", "material", DOC),
 ("Sheet", "sharing", "Arthur, Robert, Oliver", "—", "any role", "material (people) / representational (role)", "evt_6e2c91d4b07f3a58c1d2e4"),
 ("Reply", "destination", f"thread of {HUB}", "—", "—", "material", HUB),
 ("Reply", "still broken", f"{R['still_broken']} (Broken plus Covered)", "—", "may also give the 7 and 2 split", "material", DOC),
 ("Reply", "new tickets", str(R["new_tickets"]), "—", "—", "material", HUB),
 ("Reply", "children Done", f"{R['children_done']} of {R['children_total']}", "—", "—", "material", HUB),
]
for r in B4:
    A("| " + " | ".join(r) + " |")
A("")

A("## 5 · Discovery map\n")
A("Root cause and findings appear only here and never in the prompt.\n")
A("| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |\n|---|---|---|---|---|---|---|")
F = json.load(open(os.path.join(HERE, "brief_facts.json")))
for f in F:
    A(f"| {f['id']} {f['fact']} | {f['value']} | {f['locator']} | {f['reach']} | {f['order']} | {f['risk']} | {f['name']} |")
A("")

A("## 5a · Search-as-persona proof\n")
A("`persona_view.py search owen_baker <service> \"<query>\"` reads base data; seeded rows Owen can see are counted from the SQL overlay (check-sql PASS for every scoped seeded record, dossier 1.E). Outputs verbatim below the table.\n")
A("| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |\n|---|---|---|---|---|---|---|")
for f in F:
    s = SAP[f["id"]]
    seeded = f.get("seeded", 0)
    hidden = "n/a (--no-hidden)" if s["service"] in ("slack", "gmail") else s["hidden"]
    found = f"YES (seeded; {'check-sql YES' if f.get('scoped') else 'unscoped'})" if seeded else "YES (base hit)"
    A(f"| {f['id']} | {s['service']} | {s['query']} | {s['visible']} base + {seeded} seeded | {hidden} | {f['hit']} | {found} |")
A("\n```")
for f in F:
    t = open(os.path.join(HERE, "sap", f["id"] + ".txt")).read().strip().splitlines()
    A("\n".join(x[:230] for x in t[:3]))
A("```\n")

A("## 6 · Triggers, incorporation and implicit requirements\n")
A("| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |\n|---|---|---|---|---|")
T6 = [
 ("outcome of each bug", DOC, "scope (Arthur's ask)", f"hub {HUB} names 'the carry-over notes doc' · YES · one doc with that title · rules, no answers", "yes, once the hub is followed"),
 ("population: canvas lines and later posts", DOC, "scope", f"{DOC} · YES · unique · scope sentence, no list", "yes"),
 ("ticket fields", DOC, "none", f"{DOC} · YES · unique · instruction", "gotcha with a record trigger"),
 ("title prefix", "comment_49b5ac4788465f72ddf245e34f2b7034", "none", f"{DOC} 'If anything changes after this I'll put it on the master ticket' · YES · ENG-2401 · instruction", "gotcha with a record trigger"),
 ("build in each child note", "690b29bc3c7d2e51b0f86a47", "none", f"{DOC} 'Brian's closing rule from the UI work applies to the line on every child, Done or not' · YES · one card comment · rule, no answers", "gotcha with a record trigger"),
 ("a line on every child", HUB, "deliverable", "hub · YES · — · instruction", "yes"),
 ("sheet in the folder, shared with the review", HUB, "destination + recipients", "hub 'share it with everyone on Sunday's bug review' · YES · one event evt_6e2c91d4b07f3a58c1d2e4 · names people, no answers", "yes"),
 ("three counts in the reply", HUB, "deliverable", f"hub · YES · thread of {HUB} · instruction", "yes"),
]
for r in T6:
    A("| " + " | ".join(r) + " |")
A("\nAnchor-name table (noun phrases of at most 6 words; `;` separates synonyms):\n\n| Anchor | May be named |\n|---|---|\n| AN1 | Arthur's DM from Thursday |\n| AN2 | the UI Changes master ticket |\n")

A("## 7 · Dates and constraints\n")
A("| Item | Absolute date or value | Source | Past fact or deadline |\n|---|---|---|---|")
for r in [("Owen's today", "Saturday Feb 14, 2026 (clock 2026-02-14T00:00Z = Fri Feb 13 16:00 PT)", "00_Task_Context.json universe.persona_today; last hub record " + HUB, "—"),
          ("Arthur's ask", "Thu Feb 12, 2026 15:10 PT (23:10Z)", HUB, "past fact"),
          ("carry-over notes", "Thu Feb 12, 2026 14:48 PT (22:48Z)", DOC, "past fact"),
          ("title note", "Thu Feb 12, 2026 16:40 PT (Feb 13 00:40Z)", "ENG-2401 comment_49b5ac4788465f72ddf245e34f2b7034", "past fact"),
          ("Sunday's bug review", "Sun Feb 15, 2026 09:00–09:30 PT (17:00–17:30Z)", "evt_6e2c91d4b07f3a58c1d2e4", "deadline (future event)"),
          ("shutdown premise", "decided Feb 9–11, 2026; wind-down acknowledged, no business as usual", "C09UHHN6PFZ/1770842566.250369", "past fact")]:
    A("| " + " | ".join(r) + " |")
A("")

A("## 8 · Difficulty levers\n")
A("| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |\n|---|---|---|---|---|")
A("| Ambiguity | yes | yes | outcomes live across Slack, Linear, GitHub, Gmail and Docs (F7 to F23) | the prompt names the anchors only, never where an answer lives |")
A("| Dynamic change | yes | yes | ticks, merged PRs and the deck are met first and overturned later (F7, F8, F20 to F23) | the prompt names neither the summary nor the correction |")
A("| Multi-source | yes | yes | Slack, Linear, GitHub, Docs, Drive, Sheets, Slides, Trello, Gmail, Calendar | no source named as an exact artifact beyond the two anchors |")
A("| Async | no | no | Friction: none (03_Error_Async_Config.txt) | — |\n| Error recovery | no | no | Friction: none | — |\n| Access control | no | no | every load-bearing record is Owen-visible (check-sql PASS) | no ask to read someone else's scoped data |\n")

A("## 9 · Must not appear in the prompt\n")
A("- **Tool and server names (catalog.json):** linear_create_issue, linear_update_issue, linear_create_comment, linear_list_issues, linear_list_comments, slack_send_message, slack_read_thread, slack_search_public_and_private, github_get_pull_request_comments, github_get_pull_request_reviews, gsheets_create_spreadsheet, gsheets_values_update, gdrive_share_file, gdrive_move_file, gmail_search_messages, gcal_list_events, trello tools, any MCP server name.")
A(f"- **Opaque ids and filenames:** {DOC}, {FOLDER}, evt_6e2c91d4b07f3a58c1d2e4, 690b27282f4c1b7a6e93d512, CE156FDFB428, C05V5FNLB9V, D05USBTQY1F, D07E9PSQB6W, every ENG key (the master ticket goes by its name).")
A("- **Findings and root causes:** any outcome, any count (9, 68, 23, 58, 7, 3, 2, 70, 63), the build 0.3.310, the [2231] prefix, the Tavern, shop icons, train, team, lives or window lines, #1913, the inline comments, the popups, Win & Collect being off, the Season Pass and Daily Gift notes, ENG-2073, ENG-2363.")
A("- **Hidden authorities and rules:** the four outcomes, the first-fit order, what counts, the ticket fields, the tree rule, the sheet columns, Brian's closing rule, the Trello card, Vincent's mail or note, Marcus's DM, Brian's reply and DM, the economy doc, the wrap deck, the tracker.")
A("- **Format and choreography:** markdown, numbered steps, a per-column content list, a service list, a call count, 'first … then …'.")
A("- **Friction and files:** none configured; no reference files or /app/artifact paths.\n")

A("## 10 · Entity traps\n")
A("`entity.py collisions` and `entity.py resolve` for every name the prompt could use, verbatim:\n```")
A(open(os.path.join(HERE, "out", "entity_brief.txt")).read().rstrip()[:9000])
A("```\n")
A("| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |\n|---|---|---|---|")
A("| Arthur Blake | 'Blake' in base talk | one person | arthur.blake@harmonygames.co |")
A("| Marcus Bennett | Marcus Lee, Oscar Bennett, github and trello 'Marcus' | Owen's DM partner is Bennett; the prompt need not name him | marcus.bennett@harmonygames.co |")
A("| Robert (one name) | none | co-founder; on the review invite | robert@harmonygames.co |")
A("| Oliver Brooks | Lauren Brooks | Oliver is on the invite | oliver.brooks@harmonygames.co |")
A("| Owen Baker | Thomas Baker | the persona | owen.baker@harmonygames.co |")
A("| ENG tickets | ZOM tickets, ZM canvases | DD is on ENG; the decoy doc f_72e0b4c3d91a5f68c2b7e4 is about ZM | ENG-2401 |\n")

A("## 11 · Pre-submit checklist\n")
for b in ["Persona voice: Owen, first person, plain; no spec-sheet layout", "Names only the two anchors (§6 table); no §9 item", "States the deliverables at the level Arthur's DM does, or simply points at it; destination named", "No tool or server name; no step list; no count", "Wind-down acknowledged (no business as usual)", "Clean spelling and punctuation; no riddle, hint, hedge or if-chain", "20–4,000 words", "Run `/create-prompt-writing check` before `/prompt`"]:
    A("- [ ] " + b)
A("")

A("## 12 · Blockers and routed defects\n")
A(open(os.path.join(HERE, "brief_blockers.md")).read().strip() + "\n")

A("## 13 · Self-review\n")
A("| Area | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |\n|---|---|---|---|")
for r in json.load(open(os.path.join(HERE, "brief_review.json"))):
    A("| " + " | ".join(r) + " |")
A("\nFair readings, clarity, incorporation, truthfulness, feasibility / ACL and the contrived register are each addressed above with evidence. Unresolved: the prompt is not yet written, and check mode re-tests every point on the actual text.\n")
out = "\n".join(L) + "\n"
open(os.path.join(WF, "04_Prompt_Writing_Brief.md"), "w").write(out)
print("brief", len(out))

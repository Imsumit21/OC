"""Writes task_inputs/Working_Files/01_Grounding_Dossier.md from the builder data and the captured tool outputs."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SP = pathlib.Path(sys.argv[1])
M = json.load(open(HERE / 'minted_ids.json'))
P = json.load(open(HERE / 'planned_text.json'))
T = json.load(open(HERE / 'truth.json'))
S = json.load(open(HERE / 'sql_ids.json'))
MAN = json.load(open(ROOT / 'task_inputs/Working_Files/01_Hardness_Manifest.json'))
out = lambda n: (SP / n).read_text().rstrip()
JL = 'julia.lawson@harmonygames.co'
N = M['LIN_NOTES']
G1 = f"{JL}/{M['G_BUILD']['message_id']}"
G2 = f"{JL}/{M['G_BUILD_RE']['message_id']}"
GT = f"{JL}/{M['G_BUILD']['gmail_id']}"
CARD, CMT, DD = M['T_H1CARD']['id'], M['T_H1CMT']['id'], M['T_DDCARD']['id']
SH, AG, FO = M['SHEET_KNOBS']['id'], M['DOC_AGENDA']['id'], M['FOLDER_ZMDIFF']['id']
EVT = M['GCAL_TUNING']['copies'][JL]
ASK = f"{M['S_ASK']['channel']}/{M['S_ASK']['ts']}"
SUM = f"{M['S_ROBERT_SUM']['channel']}/{M['S_ROBERT_SUM']['ts']}"
VIN = f"{M['S_BRIAN_POST']['channel']}/{M['S_BRIAN_POST']['ts']}"
MIR = f"C093LEZGF6J/{M['S_MIRROR_401']['ts']}"
PRC = M['PRC_244']['id']
members = [r for r in T['rows'] if r['member']]
c = T['counts']

L = []
w = L.append
w("# 01 Grounding Dossier — jl-zm-difficulty-baseline (design v6) · contains no prompt, OE or criterion text\n")
w(f"Persona Julia Lawson <{JL}> (Product Manager) · Long Horizon · `effective_profile: long` · clock 2025-10-01T00:00:00Z (the "
  "assignment's universe date read as 00:00 UTC; `tools/hg_clock.py`). SQL: `task_inputs/01_Universe_Inject.sql` (built by "
  "`support/task_work/jl_difficulty/build_sql.py`; 158 INSERT, 1 UPDATE, 10 schemas). Final manifest: "
  "`task_inputs/Working_Files/01_Hardness_Manifest.json` (draft ids kept; four `design_delta` entries).\n")

w("## 1.A Structural\n")
w("| Table | Columns used (NOT NULL from `references/universe_schema_live.json`) | Base sample ids | Rows seeded |\n|---|---|---|---|")
w("| slack.slack_messages | id, ts, channel_id, type, user_id, text, thread_parent_id, reply_count, attachments_json, created_at | C090N54TG79/1759176983.189479; C093LEZGF6J/1756140119.128149 (GitHub-app mirror shape) | 5 + 1 UPDATE (parent counters 1c181040768a5650a30ad1e68cf1b9b4) |")
w(f"| trello.trello_cards / trello_actions | id, name, \"idBoard\", \"idList\", \"desc\", \"idShort\", url, badges_json; actions data_json | trello:68c457c45f9e302837332bf4 (ZM ROADMAP card), its createCard 68c457c45f9e302837332c13 | 2 cards ({CARD}, {DD}), 4 actions (createCard ×2, updateCard {M["T_H1UPD"]["id"]} 2025-09-30T14:04:31Z, commentCard) |")
w(f"| gmail.gmail_threads / gmail_messages | id = mailbox + thread id, mailbox + RFC Message-ID; in_reply_to; internal_date = date | gmail:leonard@harmonygames.co_1842219327413774622.json | 5 threads, 10 messages ({G1}, {G2} in Julia's mailbox) |")
w(f"| gdrive.drive_files / gdocs.docs_documents / gsheets.* | f_/d_ + 22 hex; same id and sharing on drive and doc/sheet rows | f_34f0950581934de1278969 (base sheet), d_8140f09bf9f1b94cb8ee2d (Julia's root) | folder {FO}, doc {AG}, sheet {SH} + 3 tabs |")
w("| gslides.slides_presentations / slides_pages / slides_page_elements | presentation_id = drive f_ id; page object_id slide_ + 12 hex; element el_ + 12 hex, kind TEXT_BOX, 9144000x5143500 | f_44566b6f0e293b4cc3097a (Robert's deck, slide_3d6a2f2461a0 / el_4c7286d51d6f) | f_048bf5e69f8e7f1a659a5c: 3 slides, 3 text boxes |")
w(f"| gcal.gcal_events | event_id evt_+22 hex per calendar, ical_uid 32hex@hg4, start/end ts + json | evt_f07c2d5d56f5110a888cef (Julia's BoomBit kickoff) | 5 copies ({EVT} on Julia's calendar) |")
w(f"| github.github_pr_comments / timeline_events | PR id + #c_n, PR id + #ev_n; every comment has a `commented` event | harmonygames-Games/match3d#401#c_1, #401#ev_1 to #ev_6 | {PRC}, harmonygames-Games/match3d#401#ev_7 |")
w("| linear.linear_comments | id cmt_+20 hex, issue_id, author_id (linear users), body, created_at | base has 0 comments (the `linear/data.json` comments list is empty) | 109 |\n")

w("## 1.B Entity\n")
w("| Entity | Spelling / id | Services (cited) | Agreement |\n|---|---|---|---|")
w(f"| Julia Lawson | julia.lawson@harmonygames.co; Slack EMPLOYEE_0005_SLACK_ID; Linear usr_8140f09bf9f1b94c; Trello 793af7ca6940bf18eb516c75 | `entity.py resolve \"Julia Lawson\"`; owner of {SH} | AGREE |")
w(f"| Arthur Blake (\"Blake\") | arthur.blake@ (files blake@…); Linear usr_cc3e90160f490686; Confluence user_EMPLOYEE_0025; GitHub EMPLOYEE_0025_GITHUB_USERNAME | C090N54TG79/1756751373.593569 (\"Blake\"); {G1}; {PRC} | AGREE |")
w("| Leonard Hayes | leonard.hayes@; Slack EMPLOYEE_0038_SLACK_ID; Trello PERSON_6094_TRELLO_USER_ID; Drive root d_63fffeb4fab5233ed5bb73 | trello:68c457c45f9e302837332c13 (his createCard); " + ASK + " | AGREE |")
w(f"| Brian Foster | brian.foster@; Slack EMPLOYEE_0026_SLACK_ID (member of C090N54TG79) | {SUM}; {M['GCAL_TUNING']['copies']['brian.foster@harmonygames.co']} | AGREE |")
w(f"| Vincent Parker | vincent.parker@; Slack EMPLOYEE_0012_SLACK_ID (member of C090N54TG79); Linear usr_65c76e0b87aa7e9b | {VIN}; {N['ZOM-254']['id']} | AGREE |")
w("| Robert | robert@; Linear usr_Robert; Confluence user_EMPLOYEE_0016 | f_048bf5e69f8e7f1a659a5c; " + N['ZOM-293']['id'] + " | AGREE |")
w("| Zombie Match 3D store builds | iOS 0.3.49 / Android 0.3.133 | C0880U9751A/1759182908.627389 (iOS); C07C2866011/1759075866.111309 (Android; Julia NO); " + G1 + " | AGREE |")
w("| Starting tier threshold | > 90 (code, ZOM-42) vs >= 90 (ZOM-199) | ZOM-42, ZOM-199 descriptions; " + G2 + " | DISAGREE (designed: dated reply settles it) |")
w("| PR #401 | harmonygames-Games/match3d#401 \"Split enrage parameter into separate ones\" merged 2025-08-25T16:42:14Z | github data.json; " + PRC + " | AGREE |")
w("| ZOM-n vs ENG-n | ZOM-199 / ENG-199 twins (N01) | linear data.json | AGREE (task names ZOM only) |\n")

w("## 1.C Voice and realism\n")
w("Lengths, hours and style from `references/universe_kb/conventions.json` (`slack.length_chars_by_channel_type`, "
  "`slack.per_person_hours_and_style`, `gmail.internal_subject_len_chars`, `linear` one- or two-line comments); seeded speakers with "
  "`status_at_clock` from `references/universe_kb/activity.json` (computed for the Feb 2026 clock; every speaker posted in Sep 2025).\n")
w("| Speaker | status_at_clock | Real samples (pointer) | Seeded rows |\n|---|---|---|---|")
w("| leonard.hayes@harmonygames.co | active_feb_2026 (activity.json) | C08R27X0EAH/1756922313.032399 \"I think we really need to adjust rage by Friday\"; C0880U9751A/1759182908.627389 \"I just released 0.3.49 on IOS\"; C090N54TG79/1756751169.213249 | " + f"{ASK}; card {CARD} + comment {CMT}; {DD}; invite; agenda {AG}; {N['ZOM-30']['id']} |")
w("| arthur.blake@harmonygames.co | active_feb_2026 (activity.json) | D05H5QL09PX/1755800367.839589 \"I think it just looks at the item it replaced\"; D05H5QL09PX/1757434464.819109 \"Can you test Android 1804?\"; C08R27X0EAH/1756749623.058599 | " + f"{G1}; {G2}; C090N54TG79/1756912929.304417; {PRC}; 94 Linear notes |")
w("| brian.foster@harmonygames.co | active_feb_2026 (activity.json) | C08R6BF4ENN/1756835318.028769 \"Recently I tested the latest Season Pass build\"; C08R6BF4ENN/1756999375.251619; C08R6BF4ENN/1757671069.174799 | " + SUM + " |")
w("| vincent.parker@harmonygames.co | quiet_since_2025-12 (activity.json) | C08R27X0EAH/1756922710.548259 \"no not at all, I haven't experienced such thing\"; C0880U9751A/1750165444.708639; C090N54TG79/1756753434.723599 | " + f"{VIN}; notes on ZOM-246/254/263/274/280 |")
w("| robert@harmonygames.co | active_feb_2026 (activity.json) | C090N54TG79/1756751305.466159; C0880U9751A/1758921802.962539; C090N54TG79/1759176983.189479 | f_048bf5e69f8e7f1a659a5c (Jun 16); notes on ZOM-23, ZOM-288, ZOM-293 |")
w("| oliver.brooks@harmonygames.co | active_feb_2026 (activity.json) | C08R6BF4ENN/1756960785.464819 \"Builds for testing SP\"; C08R6BF4ENN/1756996117.185929; C08R6BF4ENN/1757646802.623469 | notes on ZOM-49, ZOM-161, ZOM-262, ZOM-275 |")
w("| owen.baker@harmonygames.co | active_feb_2026 (activity.json) | harmonygames-Games/match3d#271 (author); harmonygames-Games/match3d#258 | note on ZOM-295 |")
w("| marcus.bennett@harmonygames.co | active_feb_2026 (activity.json) | C090N54TG79/1756748966.836219 \"the new material has 3001 rendering que\"; harmonygames-Games/match3d#238 | note on ZOM-258 |\n")
w("Posting hours: Leonard's ask 19:48Z and card 18:05Z/15:41Z fall in his 14:00–23:00Z band; Blake's mail 09:12Z/13:26Z and notes follow each "
  "ticket's own completion time (the base closed those tickets at those hours, several on UTC weekends — see warning dispositions); "
  "Brian 22:31Z and Vincent 16:12Z inside their Sep 2025 hours.\n")

w("## 1.D Keyword\n")
w("| Term | Base hits | Seeded / reached via |\n|---|---|---|")
w(f"| \"difficulty baseline\" | NEW TERM — introduced in trello:{CARD} and trello:{DD}, reached via the ask {ASK} | the ask names the card |")
w(f"| \"store builds\" | NEW TERM — introduced in {G1}, reached via card rule 3 (trello:{CARD}) | Gmail search |")
w(f"| \"monster enrage\" | NEW TERM — introduced in gsheets:{SH}, reached via card rule 5 | Sheets search |")
w("| \"dynamic difficulty\" | base: ZOM-42 title; C08GLSV8Z7W (Domino Delights) messages | NEW TERM page title f_048bf5e69f8e7f1a659a5c, reached via card rule 5 |")
w(f"| \"tiers:\" (note tag) | NEW TERM — introduced in {N['ZOM-305']['id']} and the other 3 tagged notes, reached via card rule 1 | per-ticket comment reads |")
w(f"| \"tuning\" | NEW TERM — introduced in gcal:{EVT} and gdocs:{AG}, reached via card rule 7 / rule 2 | Calendar / Docs search |\n")

w("## 1.E Persona reach\n")
w("| Record | Service | Visibility path | Role |\n|---|---|---|---|")
w(f"| {M['S_ASK']['id']} ({ASK}) | slack | Julia is a member of DM D05HB64NMQU | LB anchor |")
w(f"| {G1} | gmail | Julia's own mailbox copy (INBOX) | LB H2 |")
w(f"| {G2} | gmail | Julia's own mailbox copy (INBOX), thread {GT} | LB H2 reply |")
w(f"| {SH} | gsheets | Julia owns it | LB H3 |")
w(f"| {AG} | gdocs | shared with Julia (reader) | LB format |")
w(f"| {FO} | gdrive | shared with Julia (writer) | LB destination |")
w(f"| {EVT} | gcal | Julia's own calendar copy | LB recipients |")
w(f"| {M['CONF_DDA']['id']} | gslides | shared with Julia (reader) | LB tier rules (card rule 5) |")
w(f"| {M['CC_ART']['id']} (C090N54TG79/{M['CC_ART']['ts']}) | slack | Julia is a member of private C090N54TG79 | LB correction |")
w(f"| {M['S_ROBERT_SUM']['id']} ({SUM}) | slack | Julia is a member of private C090N54TG79 | decoy |")
w(f"| {M['S_BRIAN_POST']['id']} ({VIN}) | slack | Julia is a member of private C090N54TG79 | distractor |")
w(f"| {M['S_MIRROR_401']['id']} ({MIR}) | slack | UNVERIFIED-OK: integration companion in public #zombie-prs (Julia not a member); alternate_evidence_ids: {PRC} | companion, not load-bearing |\n")
w("`python3 Task_Authoring/tools/persona_view.py check-sql julia_lawson Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing <lb ids>` (verbatim):\n")
w("```\n" + out('checksql.txt') + "\n```\n")

w("## 1.F Collision\n")
w("Every minted id was checked against the full base collection (script in this session over `linear/data.json` comments, "
  "`trello/data.json` cards+actions, `gdrive/data.json` drive_files, the GCal export and the "
  "Gmail export file names): 0 hits each. Slack `(channel, ts)` pairs are asserted unique in `build_design.py`; PR comment "
  f"{PRC} and event harmonygames-Games/match3d#401#ev_7 continue the base numbering (#c_1, #ev_1 to #ev_6). Identity tokens: no new "
  "external person; every author is a base user id.\n")

w("## Record ledger\n")
w("| # | Service · table | Id | Manifest element | Carrier | Reach | Discovery role |\n|---|---|---|---|---|---|---|")
rows = [
    ("slack.slack_messages", M['S_ASK']['id'], "A1 / K1", "●", "DM member", "first link"),
    ("slack.slack_messages", M['S_ROBERT_SUM']['id'], "H2 decoy / T7", "●", "channel member", "decoy"),
    ("slack.slack_messages", M['S_BRIAN_POST']['id'], "T16", "●", "channel member", "distractor"),
    ("slack.slack_messages", M['S_MIRROR_401']['id'], "INT-01 companion of " + PRC, "●", "UNVERIFIED-OK", "companion"),
    ("trello.trello_cards", CARD, "H1 / K2", "●", "unscoped", "connecting"),
    ("trello.trello_actions", M['T_H1CREATE']['id'], "T1 v1", "●", "unscoped", "connecting"),
    ("trello.trello_actions", CMT, "K3 / T1", "●", "unscoped", "overturning"),
    ("trello.trello_cards", DD, "H1 decoy / T12", "●", "unscoped", "decoy"),
    ("trello.trello_actions", M['T_DDCREATE']['id'], "T12", "●", "unscoped", "decoy"),
    ("gmail.gmail_messages", G1, "H2 / K4 / T7 / T19", "●", "Julia's mailbox", "connecting"),
    ("gmail.gmail_messages", G2, "K5 / T6 / C5 / C8", "●", "Julia's mailbox", "overturning"),
    ("gmail.gmail_threads", GT, "H2 thread", "●", "Julia's mailbox", "container"),
    ("gsheets.sheets_spreadsheets", SH, "H3 / K6 / T8 / T9 / T11", "●", "Julia owns", "authority"),
    ("gdocs.docs_documents", AG, "K11", "●", "shared", "format"),
    ("gdrive.drive_files", FO, "K10", "●", "shared (writer)", "write target"),
    ("gslides.slides_presentations", "f_048bf5e69f8e7f1a659a5c", "K7 / T6 / T10 / T11", "●", "shared with Julia", "claim met first"),
    ("slack.slack_messages", "C090N54TG79/1756912929.304417", "K8 / T11 / C1", "●", "channel member", "overturning"),
    ("gcal.gcal_events", EVT, "K9 / T13 / C4", "●", "Julia's calendar", "connecting"),
    ("github.github_pr_comments", PRC, "T8 / T21", "●", "unscoped", "overturning"),
    ("linear.linear_comments", N['ZOM-305']['id'], "K13 / C2 (tagged)", "●", "unscoped", "connecting"),
    ("linear.linear_comments", N['ZOM-277']['id'], "C3 / T5", "●", "unscoped", "connecting"),
    ("linear.linear_comments", N['ZOM-45']['id'], "T5", "●", "unscoped", "connecting"),
    ("linear.linear_comments", N['ZOM-173']['id'], "T15", "●", "unscoped", "connecting"),
    ("linear.linear_comments", N['ZOM-312']['id'], "T15", "●", "unscoped", "connecting"),
    ("linear.linear_comments", N['ZOM-282']['id'], "T8 v1", "●", "unscoped", "claim met first"),
]
for i, (svc, rid, el, car, reach, role) in enumerate(rows, 1):
    w(f"| {i} | {svc} | {rid} | {el} | {car} | {reach} | {role} |")
w(f"| {len(rows) + 1} | linear.linear_comments | 103 further cmt_ ids (`minted_ids.json` LIN_NOTES, e.g. {N['ZOM-24']['id']}) | cohort surface (neutral / decisive) | ● | unscoped | per-record |")
w(f"| {len(rows) + 2} | other rows | the other 4 gmail copies per message, 4 calendar copies, page version, 3 sheet tabs, timeline event harmonygames-Games/match3d#401#ev_7, slack parent UPDATE 1c181040768a5650a30ad1e68cf1b9b4 | companions of the rows above | ● | per row | companion |\n")

w("## Findability and discovery-order proofs\n")
for rec, q_, svc, pos in [
        (f"trello.trello_cards · {CARD}", "difficulty baseline", "trello search", "first link (named by the ask)"),
        (f"gmail.gmail_messages · {G1}", "store builds", "gmail search", "connecting (card rule 3)"),
        (f"gmail.gmail_messages · {G2}", "Re: store builds for monday", "the same thread", "terminal (reply under the first message)"),
        (f"gsheets.sheets_spreadsheets · {SH}", "monster enrage", "sheets/drive search", "connecting (card rule 5)"),
        ("gslides.slides_presentations · f_048bf5e69f8e7f1a659a5c", "dynamic difficulty deck", "slides / drive search", "connecting (card rule 5)"),
        (f"gcal.gcal_events · {EVT}", "ZM difficulty tuning", "calendar search / list Oct 6", "connecting (card rule 7)"),
        (f"gdocs.docs_documents · {AG}", "ZM difficulty tuning", "docs search", "connecting (card rule 2)")]:
    w(f"```\nRecord:              {rec}\nAgent's likely query: \"{q_}\" via {svc}\nTerm present:        seeded text in the record (planned_text.json)\n"
      f"Competing base hits: decoys share the terms (DD card \"Difficulty baseline\"; base DD sheet \"Parameter Optimization\")\nChain position:      {pos}\n```")
w(f"Dynamic-change seeds: Brian's summary {SUM} (claim met first: #zombie-design is the busiest difficulty channel) → overturned by the "
  f"store builds mail {G1}; the deck's \"90 or more\" (f_048bf5e69f8e7f1a659a5c) → overturned by Blake's reply {G2} (decisive: it names "
  f"the code's check); ZOM-282's note {N['ZOM-282']['id']} (replaces ZOM-254; speed and damage share one value) → {PRC} (split into separate values) → the sheet {SH}. Hidden-authority proofs: "
  f"H1 by the ask's \"difficulty baseline card\" (decoy {DD} returned by the same query, other game); H2 by \"store builds\" (decoy "
  f"{SUM} found by a channel search); H3 by \"monster enrage\" (decoy base gsheets:f_34f0950581934de1278969, other game).\n")

w("## Self-validation table\n")
w("| QC category | Tool-enforced | Manual evidence |\n|---|---|---|")
w("| Missing Universe Data | — | every needed fact exists and is readable (1.E check-sql PASS); the agent's write tools exist in `Evals/references/tools/catalog.json` |")
w(f"| Temporal Field | sql_lint/base_check PASS (created ≤ updated, replies after parents, notes before each issue's updated_at) | text dates: \"Leonard released it yesterday\" in {G1} (2025-09-30) = iOS 0.3.49 on 2025-09-29 (C0880U9751A/1759182908.627389); \"Sep 26\" cut; History tab dates match commit 84780b8d (2025-08-09) and #401 (2025-08-25) |")
w(f"| Cross-service Referential | base_check Check A PASS | names spelled as in the base (Blake, Leonard, Robert); PR numbers in notes point at the PR meant (facts ZOM-173→match3d#243 … verified by fact_check) |")
w(f"| Quantitative / Reconciliation | Slack parent counters updated (1c181040768a5650a30ad1e68cf1b9b4 reply_count 3); Trello badges comments 1 | sheet Live values = VarC prefab values at commit 85d1a406 (re-check, `01b_Redteam_Recheck_v3.md` #4) |")
w("| State / Lifecycle | base_check PASS; L03 acknowledged (dated_claim) | ZOM-303 Live in code at the clock (TierManager at 85d1a406); no designed ticket status contradicts its activity |")
w(f"| Identifier / Format | ids per scheme (sha Slack ids, f_/d_ 22 hex, evt_/ical, #c_/#ev_ continuation, Trello timestamped ids) | emails from the base; Robert's usr_Robert reused |")
w("| Semantic / Category | — | card on list \"Oct 21\" of ZM ROADMAP; DD card on \"March/April\" of the Product Roadmap board; titles match content |")
w("| Other | — | voice per 1.C; no record states a status; the reply states a code fact, not a verdict |\n")

w("## Integrations and companions\n")
w("| Service | INT id | Companion | Decision |\n|---|---|---|---|")
w(f"| github | INT-01 | Slack mirror in #zombie-prs | seeded: {M['S_MIRROR_401']['id']} threaded under #401's opened post; parent counters updated |")
w("| github | INT-03 | linear[bot] PR comment | none: #401's title/branch name no Linear key |")
w("| github | INT-23 | CodeRabbit | none seeded |")
w("| linear | INT-04 | Linear Slack app notifications | none: base has no Linear comments, so no notification precedent |")
w("| linear | INT-05 | Linear e-mail digests | none: same reason |")
w(f"| gcal | INT-11 | invitation mails | none: `integration_exceptions` no_notify for {M['GCAL_TUNING']['ical_uid']} (base_check warning dispositioned) |")
w("| gdrive / gsheets / gdocs | INT-13 | Drive Slack app DMs | none: DM-only and optional for shares |")
w("| trello | INT-21 | Slack bot posts | none: no Trello integration exists |")
w("| slack | INT-22 | Slack e-mail notifications | none: sparse in the base |")
w("| gmail | — | label counters | not modelled in the base export; none |")
w("| gslides | — | Drive row | the deck's drive_files row with identical sharing |\n")

w("## Touched-data census and coherence hazards\n")
w("Census: the 109 candidates and their PRs (#243, #258, #265, #267, #271, #282, #283, #289, #296, #319), #401, ZOM-42/199/254/282/303, the "
  "#zombie-design and #zombie-bugs / #zombie-match3d messages the storyline cites, the DD sheet, the ZM ROADMAP and Product Roadmap boards.\n")
w("Hazards walked from `references/universe_kb/coherence_hazards.json` (all six categories):\n")
w("| Category | Hazard ids in scope | Disposition |\n|---|---|---|")
w("| temporal | T04 (ZOM-282 vs #401), T05 (ZOM-282 closes before ZOM-254), T08 | dated claims (ZOM-282 note; #401 comment); rule 4 orders by creation; authors active |")
w("| semantic_category | S02 (nested parents ZOM-50/ZOM-30), S03 (labels), S08 (page_zm3d_gdd post-clock versions) | children keep own rows; no rule uses labels; page_zm3d_gdd not cited |")
w("| cross_service_referential | R01 (keys in text), R04 (Google ids), R06/R07 (mirrors), R08 (invite mails) | every cited key/PR exists; titles only; #401 mirror seeded; no_notify exception |")
w("| quantitative | Q01 (thread counters), Q10 (copies per mailbox), Q11 (calendar copies) | parent counters updated; identical copies |")
w("| state_lifecycle | L03 (ZOM-292, ZOM-387 Todo with merged PRs), L06 (ZOM-201/ZOM-293), L10 (#244 bot-only reviews) | L03 dated_claim acknowledged in the manifest; L06 folded in; L10 not cited |")
w("| identifier_format | I03 (mailbox aliases), I05 (EMPLOYEE_0032), I08 (token logins), I10 (usr_Robert) | base forms reused |\n")
w("Warning dispositions: base_check warns on the L03 hazard touch — acknowledged as `dated_claim` (notes before each issue's updated_at; "
  "SQL modifies neither issue nor PR); base_check warns on the tuning session's missing invitation mail — `integration_exceptions` "
  "no_notify.\n")

w("## Intended disagreements\n")
w("| # | Disagreement | Why realistic | Resolved by |\n|---|---|---|---|")
w(f"| 1 | ZOM-199 / the deck say >= 90; the code and ZOM-42 say > 90 | a ticket restating the spec loosely; the code kept the original | Blake's reply {G2} (2025-09-30) |")
w(f"| 2 | ZOM-282 (06-21) asks +50% to both; #401 (08-25) gives speed and damage separate values | tuning after the mechanic shipped | ZOM-282 note {N['ZOM-282']['id']} (replaces ZOM-254; hp off since 06-19, commit b511fcbcd5); {PRC}; card rule 4 (only a closing note saying so makes a ticket Replaced) |")
w(f"| 3 | Brian's summary: editor bits in the store builds, +50% for every monster | a live-ops engineer's confident recap | {G1} (tooling stripped); sheet {SH} (per monster) |")
w(f"| 4 | The deck's +25% blunder line | written from ZOM-254 on Jun 16 | C090N54TG79/1756912929.304417 (2025-09-03); {SH} |")
w(f"| 5 | DD card \"Difficulty baseline\" | the same rules card idea for the other game, March 2025 | scope: Domino Delights; the ask names the ZM ROADMAP card |\n")
w("Best argument each is unintended, and why not: (1) two system fields would be a defect — here one is ticket prose and the other the "
  "code, and a dated human mail names which governs; (2) a Done ticket with later work — card rule 4 makes only a replacing note count, and #401 "
  "only splits numbers; (3) a teammate's summary is a human claim, the mail is later; (4) a stale page is dated and retired by a newer comment; (5) a "
  "decoy merely called a decoy would not resolve it — it differs by game scope, stated in its own text.\n")

w("## Constraints for the prompt brief\n")
w("| Anchor | May be named (noun phrases only) | Record |\n|---|---|---|")
w(f"| A1 | Leonard's difficulty baseline ask; Leonard's DM; Monday's tuning session | {ASK} |\n")
w("Never name: the card, the mail, the sheet, the page, the folder, the agenda, any ticket or PR id, the tag, the > 90 check, the "
  "attack-power amendment, any count or status. Deadline: Monday's tuning session (2025-10-06). Deliverable kinds: a register, a reply "
  "to Leonard, ticket updates.\n")

w("## Fact sheet\n")
w("| Key | Value | Kind | Must appear in | Home ids |\n|---|---|---|---|---|")
for f in MAN['facts']:
    w(f"| {f['key']} | {f['value']} | {f['kind']} | {', '.join(f.get('must_appear_in', []))} | {', '.join(f.get('home_ids', []))} |")
w("\n`python3 Task_Authoring/tools/fact_check.py … --no-leak` (verbatim):\n")
w("```\n" + out('fact.txt') + "\n```\n")

w("## Facts for the human\n")
w("| Locator | Base/seeded | Fact | Reach | Role |\n|---|---|---|---|---|")
w(f"| {ASK} | seeded | Leonard 2025-09-30T19:48:26Z: baseline before Monday; rules on the difficulty baseline card; reply with counts and when a new player gets the starting tier | DM | anchor |")
w(f"| linear:{N['ZOM-281']['id']} | seeded | Blake 2025-06-27: 'tiers: closing. checked on the dev build' on ZOM-281 (assigned EMPLOYEE_0032, no card word) -> member, Live | unscoped | per-record (hardening L3) |")
w("| ZOM-42 vs match3d TierManager.cs / WinHistory.cs (base) | base | ZOM-42 and ZOM-199 say 'first 10 level'; the build's starting tier: bucketing at totalGames == 10, GetTotalGames = wins + losses -> after the first 10 games, won or lost, not level 10; CPM > 90 | unscoped | rules / reply fact (hardening L4) |")
w(f"| trello:{CARD} | seeded | rules 1–7 (Leonard 2025-09-29T18:05:12Z); comment {CMT} 2025-09-30T15:41:55Z adds attack power | unscoped | authority |")
w(f"| {M['S_ASK_REPLY']['channel']}/{M['S_ASK_REPLY']['ts']} | seeded | Leonard 2025-09-30T20:07:18Z, thread reply under the ask: drop ZOM-30, ZOM-49, ZOM-50, ZOM-161 (analytics) and ZOM-262, ZOM-275 (tutorial); the reply also lists the Not shipped and Editor only keys | DM | amendment (hardening L1) |")
w(f"| trello:{M['T_H1CL']['id']} | seeded | checklist \"Before Monday\" on the card (addChecklistToCard 2025-09-30T16:20:11Z): rule 6 change (a comment on each Editor only and Not shipped ticket), rule 7 change (Brian edits) | unscoped | amendment (hardening L2) |")
w(f"| {G1} | seeded | Blake 2025-09-30T09:12:44Z: store builds iOS 0.3.49 / Android 0.3.133, cut Sep 26; level editor, Editor folders and debug menu stripped | Julia's mailbox | authority |")
w(f"| {G2} | seeded | Blake 2025-09-30T13:26:05Z: the build checks cpm > 90, not >= 90; ZOM-199 is wrong | Julia's mailbox | overturning evidence |")
w(f"| gsheets:{SH} | seeded | Julia's sheet (modified 2025-09-08, after #417 brought the VarC values to main on 09-06): Live per-monster speed/damage (Boxer 0.5/0.4 … MonsterBase base prefab 0.8/0.8; Mailman, Mayor2, PartyGirl 'not copied yet', copied as is per card rule 5), hp 0 | owner | authority |")
w("| gslides:f_048bf5e69f8e7f1a659a5c | seeded | Robert 2025-06-16: tier rules (90 or more; 80% over 10; 4 losses) and ZOM-254's +25% line | unscoped | claim met first |")
w("| slack:C090N54TG79/1756912929.304417 | seeded | Blake 2025-09-03 in #zombie-design: the deck's blunder line is old; speed and damage per monster, no hp | channel member | overturning evidence |")
w(f"| gcal:{EVT} | seeded | ZM difficulty tuning 2025-10-06T17:00Z; attendees Leonard, Julia, Robert, Arthur, Brian | Julia's calendar | recipient list |")
w(f"| gdocs:{AG} | seeded | agenda: one sheet, tabs Tickets and Rules in force | shared | format |")
w(f"| gdrive:{FO} | seeded | ZM Difficulty folder (Leonard; Julia writer) | shared | write target |")
w(f"| {PRC} | seeded | Blake 2025-08-25: #401 gives speed and damage separate values; drops the unused EnrageHealth method | unscoped | evidence |")
w(f"| {SUM} | seeded | Brian 2025-09-29: everything incl. editor bits in store builds; +50% for every monster | channel | decoy |")
w(f"| {VIN} | seeded | Vincent 2025-09-30: drop the list in #zombie-design | channel | distractor |")
w(f"| trello:{DD} | seeded | Domino Delights card, 2025-06-02 | unscoped | decoy |")
w("| linear ZOM-42 | base | full spec: > 90; promotion 80% over up to 10; demotion 4 straight losses or <= 50% over up to 10; record resets | unscoped | authority text |")
w(f"| linear notes | seeded | 109 notes; tagged \"tiers:\": ZOM-221, ZOM-300, ZOM-305, ZOM-378 ({N['ZOM-305']['id']}); members {T['members']} ({c.get('Live')} Live, {c.get('Editor only')} Editor only, {c.get('Not shipped')} Not shipped, {c.get('Replaced')} Replaced) | unscoped | per-record evidence |\n")

w("## Platform follow-ups\n")
w("- Confirm in the Opus pre-check that the seeded Linear notes render through `linear_list_comments` (●, §6b) and that "
  "`linear_list_issues`' query does not search comment text (budget `conditional_on`).\n- Confirm whether the platform shows the 9 Blake "
  "tickets changed after the clock in their pre-clock state (non-members either way).\n- Slides: the deck text is in element text (●); confirm it renders through gslides_get_presentation_text in the "
  "pre-check.\n- No ○ carrier is load-bearing (GCal description unused).\n")

w("## Self-review\n")
w("`python3 Task_Authoring/tools/sql_lint.py Task_Authoring/task_inputs/01_Universe_Inject.sql` (verbatim):\n")
w("```\n" + out('lint.txt') + "\n```\n")
w("Warning dispositions: clock warnings (gcal start/end 2025-10-06) — a not-yet-happened future meeting, allowed as a deadline; weekend "
  "warnings (Linear notes at UTC weekend times) — each note sits minutes before its ticket's own base completion/update time, which the "
  "base already records at that hour; no Confluence statement remains (`/injection` F1).\n")
w("`python3 Task_Authoring/tools/base_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql` (verbatim):\n")
w("```\n" + out('base.txt') + "\n```\n")
w("`python3 Task_Authoring/tools/hardness_gate.py …/01_Hardness_Manifest.json …/01_Universe_Inject.sql` (verbatim):\n")
w("```\n" + out('hg.txt') + "\n```\n")
w("**Check A–C walk** (`Evals/0_Injection_Quality_Eval.md`): inventory 170 INSERT / 2 UPDATE (no DELETE, no upsert). Check A (references, "
  "uniqueness over the full collections, identities, id contracts): PASS (base_check A; 1.F 0 collisions). Check B (structure, literal "
  "JSON, generated/NOT NULL columns): PASS (sql_lint 0 errors; no *_fts column written). Check C (dates, parent/reply, statuses, counts, "
  "superseding records): PASS (base_check C; replies after parents; counters updated).\n")
w("| # | Category | Counter-reading (strongest case it FAILS) | Evidence that resolves it | Verdict |\n|---|---|---|---|---|")
w(f"| 1 | Temporal | Blake's mail says \"Leonard released it yesterday\" — if the release was on another day it contradicts | C0880U9751A/1759182908.627389 at 2025-09-29T21:55Z; {G1} at 2025-09-30T09:12Z | PASS |")
w(f"| 2 | Semantic / Category | the DD card and the ZM card share the title root \"Difficulty baseline\" | trello:{DD} on the Product Roadmap board, text scoped to Domino Delights | PASS |")
w(f"| 3 | Cross-service Referential | a note cites a PR whose files contradict it | fact_check PASS on ZOM-173→match3d#243 etc.; notes name no file (`01b_Redteam_Recheck_v3.md` R2/R3 fixed) | PASS |")
w(f"| 4 | Quantitative | the sheet's per-monster values differ from the prefabs | Live tab copied from the VarC prefabs at commit 85d1a406 (re-check #4 values) in gsheets:{SH} | PASS |")
w(f"| 5 | State / Lifecycle | ZOM-292 / ZOM-387 Todo with merged PRs (L03), a sibling of a status defect | notes {N['ZOM-292']['id']}, {N['ZOM-387']['id']} explain the umbrella tickets; neither is a member | PASS |")
w(f"| 6 | Identifier / Format | the mirror id or parent update breaks the Slack scheme | {M['S_MIRROR_401']['id']} = sha256(C093LEZGF6J|ts)[:32]; parent 1c181040768a5650a30ad1e68cf1b9b4 from the base | PASS |")
w(f"| 7 | People status | Vincent (quiet_since_2025-12) voiced on Sep 30 | Vincent posts in C08R27X0EAH through Sep 2025 (C08R27X0EAH/1758546048.524829, 2025-09-22) | PASS |")
w(f"| 8 | Other | the reply reads as stating the answer | {G2} states the code's check, not a register value; the rules row and ZOM-199 comment still need the agent | PASS |")
w(f"| 9 | Intended disagreement 1 | >= 90 vs > 90 is two silent fields | ZOM-199 prose vs ZOM-42 prose + code; a dated human mail ({G2}) names the governing one | PASS |")
w(f"| 10 | Intended disagreement 2 | ZOM-282 Done, #401 later splits its value | ZOM-282 note {N['ZOM-282']['id']} (hp off since 06-19, b511fcbcd5) and {PRC} | PASS |")
w(f"| 11 | Intended disagreement 3 | Brian's summary contradicts Robert's Sep 3 per-monster message | Brian is wrong by design; C08R27X0EAH/1756922765.033199 and {SH} agree | PASS |")
w(f"| 12 | Intended disagreement 4 | the deck contradicts Robert's own Jun 19 \"+100%\" | the deck is dated 2025-06-16, before that change (C0880U9751A/1750370473.240179) | PASS |")
w(f"| 13 | Intended disagreement 5 | the DD card is a same-scope rival | its text names Domino Delights and ENG tickets; trello:{DD} | PASS |\n")
w("Prior `/injection` (attempt 6adfee3ef9092601a61245bb, FAIL): F1 Confluence rows removed — the write-up is the Slides deck f_048bf5e69f8e7f1a659a5c and Blake's correction the Slack message C090N54TG79/1756912929.304417; F2 the DD card re-dated 2025-06-02T15:10:44Z (after #210, 2025-05-27); A1 `sequence` kept — listed in `references/universe_schema_live.json` for linear.linear_comments.\n")
w("Unresolved: none blocking; platform follow-ups listed above.\n")
(ROOT / 'task_inputs/Working_Files/01_Grounding_Dossier.md').write_text('\n'.join(L) + '\n')
print('written', len(L))

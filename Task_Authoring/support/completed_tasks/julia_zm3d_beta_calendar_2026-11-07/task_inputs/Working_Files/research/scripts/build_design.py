#!/usr/bin/env python3
"""Generate Working_Files/01_Scenario_Design.md for julia-zm3d-beta-liveops-calendar.

Re-runnable: reads the draft manifest + gradable surface and emits the 19-section design doc the scenario stage gate
checks, with an evidence pointer on every table row / bullet in the pointer-gated sections. Re-run after any manifest,
surface or prose change (the stage gate wants every output newer than 00_Assigments.md):
  python3 -B Task_Authoring/task_inputsS/Working_Files/research/scripts/build_design.py

Verbatim tool blocks (REACH, HARDNESS GATE head, SHARED_FIRST_NAMES, hardness v2, forecast) are embedded from the
captured research/*.txt runs; the stage gate re-runs persona_view reach and hardness_gate --design and compares.
"""
import json
from pathlib import Path

WF = Path(__file__).resolve().parents[2]
M = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())
S = json.loads((WF / "01_Gradable_Surface.json").read_text())
REQ, SV, AN = M["requirements"], M["services"], M["anchors"]
FR, AU, CO = M["ask_fragments"], M["authorities"], M["cohort"]
CH, TR, CB = M["chains"], M["traps"], M["call_budget"]
WR, PF = M["writes"], M["mechanism_portfolio"]

L = []


def w(*xs):
    for x in xs:
        L.append(x)


# ------------------------------------------------------------------ header
w("# 01 — Scenario Design — Julia Lawson · Product · Marketing and GTM · Planning and decision support · "
  "Long Horizon · Medium · Oct 1 2025 (synth-cut)",
  "",
  "Command `/create-scenario`. Universe synth-cut; Clock 2025-10-01 00:00 PT (07:00Z); seed bound "
  "`2025-10-01T00:00:00Z`; `context_hash 7b0cc66ffd451f41aff7b1db7367e86f141b0d1fa444f1839482cf2e5839dc5e`. "
  "Profile extreme (Long Horizon), with a requester-confirmed `volume_exception` (floors 130/75) recorded in the "
  "manifest; the enriched 47-member cohort meets the extreme ≥ 40 cohort rule with no cohort exception. This file "
  "designs the scenario, records and difficulty "
  "only; the prompt, Oracle Events and rubric criteria come later.",
  "",
  "Method note. All discovery ran read-only through `tools/hg.py` and `tools/persona_view.py`; cached pulls live in "
  "`Working_Files/research/raw/`. Four research workers (R-A gate contract, R-B spine facts, R-C carriers/ids, R-D "
  "coherence audit) produced `research/R_*.md`. One early worker (S7) read backend files outside `hg.py`; its leads "
  "are unverified and used only to REMOVE design dependencies (no Plague Race/Endless window dates are graded, the "
  "dropped C5 reward-cut channel), never to add a graded fact. No SQL is executed at this stage.",
  "")

# ------------------------------------------------------------------ 0 assignment / census
w("## 0 · Assignment, persona census and method",
  "",
  "Assignment (V3, verbatim from `00_Assigments.md`): Business Function Product; Persona Julia Lawson, Role Product "
  "Manager; Competency Marketing and GTM; Task Skill Planning and decision support; Task Type long-horizon; "
  "Difficulty Mode medium; Universe Date October 1, 2025 07:00. `task_context.py --write --require-source` resolves "
  "`source.mode=universe`, universe `synthcut`, `context_hash 7b0cc66f…`.",
  "",
  "Persona reach (`persona_view reach julia_lawson`, re-run by the gate; verbatim):",
  "",
  "```text",
  "REACH  Julia Lawson <julia.lawson@harmonygames.co>  Product Manager / Product",
  "clock 2025-10-01",
  "",
  "SLACK  user=EMPLOYEE_0005_SLACK_ID  visible channels=147 {'mpim': 52, 'public': 23, 'private': 47, 'im': 25}  "
  "messages=238131  public-not-member (UNVERIFIED)=44",
  "  persona posts=31848 last post=2025-09-30  last activity in visible channels=2025-10-01",
  "GMAIL  mailbox=julia.lawson@harmonygames.co threads=253 messages=304 range=2023-07-16..2025-09-17",
  "DRIVE  owned=28 {'application/vnd.google-apps.spreadsheet': 12, "
  "'application/vnd.google-apps.document': 10, 'folder': 2, 'application/vnd.google-apps.presentation': 2, "
  "'application/pdf': 2}",
  "UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence",
  "LAST ACTIVITY (days before clock): slack_persona_post=2025-09-30 (1d), slack_visible_channels=2025-10-01 (0d), "
  "gmail=2025-09-17 (14d), gcal_last_event_before_clock=2025-09-29 (2d), drive_last_modified_visible=2025-09-30 (1d)",
  "```",
  "",
  "Julia is a member of every Slack channel, DM and Drive folder the design uses, her own Gmail mailbox and (unscoped) "
  "Linear / GitHub / Trello; the one channel she is NOT in, `#zombie-prs` (C093LEZGF6J), carries only companion "
  "mirrors, never evidence (§16). Writes: her own Drive/Sheets, a reply in a DM she is a member of, Linear (unscoped) "
  "and a Gmail reply — all confirmed in §10 and §14.",
  "")

# ------------------------------------------------------------------ 1 storyline
AURec = {a["id"]: a for a in AN}
w("## 1 · Storyline",
  "",
  "On Oct 1 2025 the Zombie Match 3D (ZM3D) beta is about to buy its first users. Frederick Stone — owner of the "
  "beta buy and of the calendar — asked Julia in their DM yesterday for the live-ops calendar of the four beta buy "
  "weeks (Mon Oct 6 – Sun Nov 2): which beats run in which windows, what is held and until when, the push for each "
  "beat, what is still to do before each runs and by whom, and her recommendation with the tradeoffs. The calendar "
  "goes in a sheet in her Drive folder, is linked from the calendar ticket, and the recommendation goes back to him "
  "in the DM. The whole task is one PM planning deliverable; every hard call survives complete retrieval. "
  "(KB anchors: `timeline` 2025-09 live-ops entries; cohort `LIN-OPEN-ZOM`; `trap_catalog` families `C01`/`C02` "
  "thread corrections, `N01` ticket-series collisions, `P01` lookalike people.)",
  "",
  "The storyline's load-bearing records (each a seeded or base locator):")
story = [
    ("The ask", "Frederick's DM to Julia (the anchor, scope and reply destination)", "slack:" + AURec["A1"]["locator"]),
    ("The rulebook", "Frederick's beta brief — the calendar owner's working rules (R1-R6, R8)", "f_7c3e91a4d2b85f60e1a9c4"),
    ("The span", "Frederick's beta UA plan deck — the four buy weeks (R9)", "f_2b9d4e7a1c63f08d5e7b21"),
    ("Done-not-deployed", "Collect & Win client PRs merged before the Sep 30 cut", "harmonygames-Games/match3d#470"),
    ("The deploy date", "Douglas's backend release plan event, Wed Oct 8 (C&W's first prod window)", "evt_9a4c2e7f1b3d58e06c7a2f"),
    ("The one-off", "Robert's #zombie-art approval of Martin's Halloween one-off, later withdrawn in his DM", "slack:C08R8CHB0QL/1758121809.236839"),
    ("The prod re-test", "Vincent's Sep 30 re-test, a #zombie-match3d root (cross-channel), weekly leagues do not start on the current prod build even after a restart (an established prod failure -> held; an unverified build would instead be a still-to-do)", "slack:C0880U9751A/1759265412.481907"),
    ("The config slip", "Brian's Season Pass November handoff, slipped to Fri Oct 31 in a later thread (R8)", "julia.lawson@harmonygames.co/1844835127305531392"),
    ("The push sheet", "the shared 'PNs Beta' tab — Ready flags, wiring column and old-title copy (R6)", "f_a325dd4af80afc5994d5dc"),
    ("The calendar ticket", "ZOM-78 'Event Calendar For Zombie Match 3D' (Backlog) — reuse, do not file new (R7)", "ZOM-78"),
]
for role, txt, ptr in story:
    w(f"- **{role}.** {txt} — `{ptr}`")
w("",
  "Anchor names (noun phrases, ≤ 6 words; the prompt may name the work only through these):",
  "",
  "| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |",
  "|---|---|---|")
for a in AN:
    w(f"| {a['id']} | {a['prompt_reference']} | `{('slack:' + a['locator']) if a['service']=='slack' else a['locator']}` |")
w("",
  "Distinctness. Vincent's `vincent-zm3d-release-gate` decides whether two Sep 30 submission builds may ship; Claire's "
  "`claire-zm3d-october-object-handoff` decides which art objects go to level design. This task decides the live-ops "
  "and push calendar for the bought-user beta — a calendar, a push plan and a recommendation. No ticket or PR gets a "
  "ship/defect verdict here (`harmonygames-Games/match3d#470`); the issue and PR spine is a readiness surface, not a "
  "release gate.",
  "")

# ------------------------------------------------------------------ 2 coherence
w("## 2 · Coherence audit",
  "",
  "Source: `coherence_hazards.json` (6 categories, 59 emitted hazards), the synth-cut `known_data_issues` cards, and "
  "R-D's probe over every record a correct run opens (`research/R_D_coherence_audit.md`). The design requires and "
  "cites no artifact that carries an ungoverned contradiction; where a required artifact holds an odd state, a dated "
  "owner statement in the brief explains it (never a silent edit). Each row below is a real record pointer.",
  "",
  "Per `coherence_hazards` category (all six covered):")
w("- **temporal** hazard `T01`: `reviewed` timeline events have null `created_at` and empty actor on every in-scope PR "
  "(`harmonygames-Games/match3d#470`) — the design never dates a review from the timeline; review dates come from the "
  "review's own `submitted_at`.",
  "- **semantic/category** hazard `S01`: cross-game copy reuse; the push sheet's `PN BETA Translated` tab holds "
  "Domino Adventures / River Rush rows (`f_a325dd4af80afc5994d5dc`) — the brief scopes beta pushes to the English "
  "`PNs Beta` tab only, so the translated tab is out of scope by a dated owner rule.",
  "- **cross-service referential** hazard `R07`: Snowflake/Confluence live-ops pages disagree with warehouse rows "
  "(`page_liveops_calendar`) — excluded; no Snowflake or Confluence record is on the required path (`f_a325dd4af80afc5994d5dc` "
  "is the only required sheet).",
  "- **quantitative** hazard `Q02`: `reply_users_count` vs distinct repliers mismatch — the only in-universe example "
  "sits in July, outside the Sep 15-30 read window (`slack:C0880U9751A/1750724624.203279`); none in scope.",
  "- **state/lifecycle** hazards `L03`/`L09`/`L10`: open ZOM issues whose fix shipped, and merged PRs with no human "
  "APPROVED (`ZOM-429`, `harmonygames-Games/match3d#470`) — these ARE the designed decisions (R3, R5); each is "
  "governed by a dated record (Vincent's re-test, the per-PR review list), never left as a bare contradiction.",
  "- **identifier/format** hazards `I01`/`I10`: raw-shaped Slack rows in DMs and non-`usr_<16hex>` Linear ids "
  "(`usr_Robert`) (`slack:D05GU6L0XFH/1759248350.473459`) — cosmetic; no graded value reads an id's shape.",
  "")
w("Required-artifact contradictions and their governed treatment (each a dated owner statement, not a silent edit):",
  "- Push sheet title 'Push Notifications Zombie Match' vs its two internal status columns and cross-game translated "
  "tab (`f_a325dd4af80afc5994d5dc`): the brief reads the first 'Status' column as the copy/readiness flag and the "
  "second 'Status (NA, WIP, LIVE)' as wiring; the translated tab is the old Domino set awaiting ZM3D localization.",
  "- The Sep 22 leaderboard report 'killing the app doesn't help' vs the same thread ending 'working fine right now' "
  "(`slack:C08R27X0EAH/1758546119.789009`): a fault on a test build fixed by a revert; the governing record is "
  "Vincent's LATER Sep 30 prod re-test, a root in #zombie-match3d (`slack:C0880U9751A/1759265412.481907`) — a "
  "different channel from the Sep 22 recovery, so the reconciliation is cross-channel, not a same-thread correction.",
  "- Robert's DM holds an auto-battler topic on Oct 1 03:32Z after the seed bound (`slack:D05GU6L0XFH/1759289577.628399`): "
  "the seeded withdrawal sits before it on its own topic and reads naturally.",
  "")

# ------------------------------------------------------------------ 3 active speakers
w("## 3 · Active speakers",
  "",
  "Every person the design puts words in the mouth of is active in Sep 2025 and quiet in Oct (`activity.json` "
  "`status_at_clock`), so a seeded Sep-dated record is in character and a reader will not expect Oct chatter from them. "
  "Each row carries the speaker's email (RX_EMAIL) and `activity` status.")
w("", "| Speaker | Email | activity.json status_at_clock | Seeds they carry |",
  "|---|---|---|---|")
speakers = [
    ("Frederick Stone", "frederick.stone@harmonygames.co", "the ask, the beta brief, the UA deck"),
    ("Robert", "robert@harmonygames.co", "the #zombie-art one-off approval and its DM withdrawal"),
    ("Vincent Parker", "vincent.parker@harmonygames.co", "the Sep 30 prod re-test on weekly leagues"),
    ("Douglas", "douglas@harmonygames.co", "the ZOM-429 owner note and the Oct 8 backend release event"),
    ("Brian Foster", "brian.foster@harmonygames.co", "the Season Pass November handoff and its slip; the Axe Arena card comment"),
    ("Owen Baker", "owen.baker@harmonygames.co", "a #470 conversation comment (companion); Oct 8 release attendee"),
    ("Arthur Blake", "arthur.blake@harmonygames.co", "inline review notes on #470/#370/#438"),
    ("Samuel Turner", "samuel.turner@harmonygames.co", "the #471 note that the daily-gift frame shipped"),
    ("Marcus Bennett", "marcus.bennett@harmonygames.co", "the #454 conversation note on the Collect & Win icon"),
    ("Oliver Brooks", "oliver.brooks@harmonygames.co", "the Sep 22 leaderboard thread (base, unchanged)"),
    ("Leonard Hayes", "leonard.hayes@harmonygames.co", "the base beta pipeline and tech-stable call (base, unchanged)"),
    ("Martin Walsh", "martin.walsh@harmonygames.co", "the base #zombie-art Halloween icon post (base, unchanged)"),
]
for name, email, carry in speakers:
    w(f"| {name} | {email} | active_sep_2025_quiet_in_oct | {carry} |")
w("")

# ------------------------------------------------------------------ 4 identity
w("## 4 · Identity traps",
  "",
  "`entity.py collisions` (verbatim head). The design never relies on a bare first name or a token; every seeded "
  "speaker is pinned by a full service id (§3, R-C §2). `trap_catalog` family `P01` (lookalike people) and `N01` "
  "(ENG-n / ZOM-n share 521 numbers) are live in this universe.",
  "",
  "```text",
  "SHARED_FIRST_NAMES (4)",
  "  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']",
  "  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <trello:c48a210d5c5a4b59231c6873>']",
  "  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']",
  "  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']",
  "SHARED_LAST_NAMES (5)",
  "  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']",
  "  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']",
  "  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']",
  "  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']",
  "```",
  "",
  "Design consequences: Martin Walsh (the Halloween post) is distinct from Martin Lewis (`martin.walsh@harmonygames.co`); "
  "Owen Baker (the #470 comment) from Thomas Baker (`owen.baker@harmonygames.co`); Marcus Bennett (the #454 icon note) "
  "from Marcus Lee and the Trello Marcus (`marcus.bennett@harmonygames.co`). The persona Julia Lawson is distinct from "
  "Peter Lawson (`julia.lawson@harmonygames.co`). Frederick Stone's GitHub login renders as 'Ryan' "
  "(`PERSON_2314_GITHUB_USERNAME`) — never cross-attributed.",
  "")

# ------------------------------------------------------------------ 5 cohort
surf = CO["evidence_surfaces"]
w("## 5 · Cohort spine",
  "",
  f"The honest live-ops work-item population is **{CO['size']} records of two types** under one readiness rule "
  f"(cohort `LIN-OPEN-ZOM`): {len([x for x in CO['members'] if x.startswith('ZOM')])} open ZOM issues whose title "
  "bear on an in-scope beat's readiness or live-ops infrastructure (Boss Arena / Axe Arena / Win Streak out) and "
  f"{len([x for x in CO['members'] if not x.startswith('ZOM')])} merged match3d PRs (Jul 1 – Sep 30) each carrying a "
  "post-merge still-to-do, deploy or scope fact, outside "
  "Boss Arena and not misfiled. The enriched cohort reaches 47 members (≥ 40 with no exception; the earlier borderline "
  "36-member spine is superseded), and every member carries a genuine per-record readiness, deploy or scope decision — "
  "no 'nothing-outstanding' padding (`research/EXPAND_cohort_feasibility.md`). The ≥ 3 surfaces over ≥ 2 services, each "
  "surface's `why_no_bulk` and the extreme `short_circuit` analysis apply and are satisfied below. Definition source: "
  "fragment "
  f"`{CO['definition_source']}` (the brief's scope rule).",
  "",
  "| Surface | Service · tool | Records × per-record | why_no_bulk (abridged) | short_circuit (abridged) |",
  "|---|---|---|---|---|")
for s in surf:
    w(f"| {s['decides']} ({s['requirement']}) | {s['service']} · `{s['tool']}` | {s['records']} × {s['per_record_calls']} | "
      f"{s['why_no_bulk'][:90]}… | {s['short_circuit'][:90]}… |")
pr = sum(float(s["per_record_calls"]) * int(s["records"]) for s in surf)
w("",
  f"Σ per-record calls × records = **{int(pr)}** (floor 75). Four surfaces over two services (Linear, GitHub); none "
  "can be bulk-read — Linear issue notes come only from `linear_list_comments` (base holds 0 comments), and a PR's "
  "review state, inline review comments and conversation comments are three separate per-PR calls that search never "
  "returns (R-C §1, R-B §4). A run that skips them cannot tell a hold from a known issue (`ZOM-429` vs `ZOM-534`) or "
  "find the still-to-do notes (`harmonygames-Games/match3d#370`).",
  "")

# ------------------------------------------------------------------ 6 hidden authorities
w("## 6 · Hidden authorities",
  "",
  "Three hidden authorities, each homed in a rarely-opened service, each governing a disjoint set of requirements, "
  "each with a same- or cross-service decoy that a targeted search also meets. Every row carries a seeded pointer.",
  "",
  "| Authority | Home | Governs | findable_query | Authority record | Decoy record (scope) |",
  "|---|---|---|---|---|---|")
dec = {"H1": "`slack:C05KNDCHAAG/1757704290.799329` (Leonard's beta pipeline — a feature list, not the rulebook)",
       "H2": "`julia.lawson@harmonygames.co/1844470925517303296` (Brian's earlier Oct 29 mail — superseded)",
       "H3": "`slack:C05KNDCHAAG/1758558302.777379` (Julia's own Sep 22 'feature completed' note — dev-side)"}
for a in AU:
    sid = (a.get("seeded_ids") or ["—"])[0]
    w(f"| {a['id']} {a['name']} | {a['home_service']} | {', '.join(a['governs'])} | \"{a['findable_query']}\" | "
      f"`{sid}` | {dec[a['id']]} |")
w("",
  "The brief (`H1`, `f_7c3e91a4d2b85f60e1a9c4`) states rules and never names a held or late beat — it is the rulebook, "
  "not an answer key. Brian's handoff (`H2`, `julia.lawson@harmonygames.co/1844835127305531392`) and Douglas's release "
  "event (`H3`, `evt_9a4c2e7f1b3d58e06c7a2f`) each decide exactly one requirement (R8, R2). Decoy scopes are disjoint "
  "(a feature list vs the rulebook; an earlier vs later mail; a dev-side note vs the prod deploy), so no "
  "identical-scope contradiction can arise.",
  "")

# ------------------------------------------------------------------ 7 delegation lattice
w("## 7 · Delegation lattice",
  "",
  "Every ask fragment chains back to an anchor through explicit delegations whose words appear in the delegating "
  "record. The hub is the ask (`A1`, " + f"`slack:{AURec['A1']['locator']}`); the brief is one hop from it and most "
  "rules delegate from the brief. Each row carries the delegating record pointer.",
  "",
  "| Fragment | Service | Reqs | incorporated_via | delegated_by_record | quote |",
  "|---|---|---|---|---|---|")
for f in FR:
    by = f["delegated_by_record"]
    byp = ("slack:" + by) if (by.startswith("C") or by.startswith("D")) and "/" in by else by
    w(f"| {f['id']} | {f['service']} | {','.join(f['requirement_ids'])} | {'→'.join(f['incorporated_via'])} | "
      f"`{byp}` | \"{f['delegation_quote']}\" |")
w("")

# ------------------------------------------------------------------ 8 chains and trap register
w("## 8 · Chains and trap register",
  "",
  f"{len(CH)} independent chains (distinct root-cause mechanisms), each ≥ 3 hops over ≥ 2 services ending in a graded "
  "fact. Then the trap register: 13 traps in multiple families plus 6 distractors. Each row carries a record pointer.",
  "",
  "### Chains",
  "",
  "| Chain | Root cause | Ends in | Hops (service: finding) |",
  "|---|---|---|---|")
for c in CH:
    hops = "; ".join(f"{h['service']} `{h['record']}`: {h['finding'][:34]}" for h in c["hops"])
    w(f"| {c['id']} | {c['root_cause']} | {c['ends_in']} | {hops} |")
w("",
  "### Trap register",
  "",
  "| Trap | Family · mech | Req | Expected wrong reading | Resolver (deciding record) | Pointer |",
  "|---|---|---|---|---|---|")
for t in TR:
    ids = (t.get("seeded_ids") or []) + (t.get("base_pointers") or [])
    ptr = ids[0] if ids else "—"
    mech = t.get("mechanism", t.get("distractor_type", ""))
    w(f"| {t['id']} | {t['family']} · {mech} | {t.get('requirement','')} | {t['expected_wrong_reading'][:70]}… | "
      f"{t['resolver'][:80]}… | `{ptr}` |")
w("",
  "Supersession families (`superseding`/`effective_date`) carry ordered `version_records`; the "
  "`hardness_v2_check` SAME_PLACE check is CLEAN (every correction sits in a different container from the claim it "
  "beats — `slack:C08R8CHB0QL/1758121809.236839` vs `slack:D05GU6L0XFH/1759270200.638114`).",
  "")

# ------------------------------------------------------------------ 9 failure diversity
w("## 9 · Failure-diversity plan",
  "",
  "The 14 portfolio mechanisms flip slots on different surfaces, so runs fail different subsets through "
  "reconciliation errors that survive complete retrieval, not concealment (forecast reports the failure-pattern "
  "spread; the operative gate is largest-pattern ≤ 50%; `hev_10c8bb5be00ab2cf`). Mapping mechanism → requirement → carrier:",
  "",
  "| Mechanism | Req | Carrier surface (the reconciliation once retrieved) | Prior family |",
  "|---|---|---|---|")
for p in PF:
    w(f"| {p['id']} | {p['requirement']} | {p['signature']} / {p['source']} | {p['prior_family']} |")
w("",
  "The heaviest single discovery is the scope rule (`R_SCOPE_BEATS`: omitting the two rollovers fails S04/S05/S06/S07 "
  "and V01, ~22% of the weight — corrected from an earlier ~15% claim after the review); next are the three "
  "still-to-do review-flag slots (`R_REVIEW_FLAGS`, per-PR inline/conversation notes, `harmonygames-Games/match3d#370`), "
  "the carrier the completed-task hardening report proved lands misses. The hold rule is attacked from two independent "
  "directions — under-hold (`R_TECH_HOLD`, the cross-channel leagues re-test) and over-hold (`R_HOLD_SCOPE`, a "
  "cosmetic/perf/iOS-verify fault read as a hold on Endless/Zombie Lane/Season Pass) — which spread the failures. "
  "Carriers span a Slack DM thread, a cross-channel #zombie-match3d root, Gmail, GCal, Trello, Linear comments and "
  "per-PR GitHub calls; every deciding record is retrievable, so the difficulty is reconciliation, not hiding.",
  "")

# ------------------------------------------------------------------ 10 deliverables
w("## 10 · Deliverables",
  "",
  "Two table deliverables in Julia's Drive, plus three message writes. Key regexes are disjoint so each table decodes "
  "its own sheet (forensics note: §13 QC rails).")
w("- **Calendar** (table, keyed by beat): columns Beat / First window (UTC) / Weeks running / Status / Still to do "
  "(owner); class column Status ∈ {Run, Hold}. Julia-owned sheet in her 'ZM Live Ops' folder "
  "(`f_e4a17c90b3d25f6a8c1d73` in `d_5f2c8e1b7a94d03c6e2b58`).",
  "- **Pushes** (table, keyed by push): columns Push / Send or hold / What is missing (owner); class column Send-or-"
  "hold ∈ {Send, Hold}. Separate Julia-owned sheet titled with 'Push' (`f_e4a17c90b3d25f6a8c1d73` folder).",
  "- **Recommendation** reply in Frederick's DM (`slack_send_message` to `D05SD5QLG94`).",
  "- **Calendar link** on `ZOM-78` and a **hold note** on `ZOM-429` (`linear_create_comment`, unscoped).",
  "- **Reply to Brian** on the Season Pass November config (`gmail_reply_to_message`, "
  "`julia.lawson@harmonygames.co/1844835127305531392`).",
  "")

# ------------------------------------------------------------------ 11 service role map
w("## 11 · Service role map",
  "",
  f"{len(SV)} services, each carrying its own fact (companion-only rows are counted separately, §16). Each row names "
  "the service's weight reason.",
  "",
  "| Service | Role | Weight reason |",
  "|---|---|---|")
for k, v in SV.items():
    w(f"| {k} | {v['role']} | {v['weight_reason'][:110]} |")
w("")

# ------------------------------------------------------------------ 12 call budget
unc = sum(r["calls"] for r in CB if not r.get("conditional_on"))
per = sum(r["calls"] for r in CB if r["phase"] == "per-record" and not r.get("conditional_on"))
w("## 12 · Call budget",
  "",
  f"Unconditional floor **{unc}** counted calls over {len({r['service'] for r in CB if r['calls']})} services "
  f"({per} per-record); the requester-confirmed `volume_exception` floor is 130/75. Conditional rows (unverified tool "
  "behaviour) count 0. Largest share outside the per-record phase ≤ 50% (gate `call_budget_spread` PASS).",
  "",
  "| Phase | Service | Calls | Why necessary |",
  "|---|---|---|---|")
for r in CB:
    flag = " *(conditional, counts 0)*" if r.get("conditional_on") else ""
    w(f"| {r['phase']} | {r['service']} | {r['calls']} | {r['reason'][:84]}{flag} |")
w("")

# ------------------------------------------------------------------ 13 qc rails
w("## 13 · QC rails",
  "",
  "- **No graded fact rests on Confluence, Snowflake or backend code** — context only, never cited (Pre-Scenario §5.5). "
  "No Plague Race or Endless window dates are graded (the warehouse's 5-day series and an unverified backend lead "
  "disagree; `page_liveops_calendar`).",
  "- **Boundaries accepted in full**: row layout (one row per beat or window), labels, PT or UTC renderings of the "
  "same instant, order of the recommendation; owner names only where a record names one (`cmt_zom429_1`).",
  "- **Writes the rubric will not loosen**: the reply goes in the DM not a channel; the link goes on `ZOM-78` not a "
  "new ticket; a failing push is held, not rewritten in place.",
  "- **Local-grader forensics note (not a platform rule)**: the two table deliverables use disjoint, case-insensitive "
  "key regexes (beats vs push names) and disjoint title patterns ('calendar' vs 'push'), so each decodes its own "
  "sheet even when both are seeded; a run that writes both tabs into one spreadsheet at overlapping A1 ranges is "
  "hand-normalized in `/create-hardening` (`f_e4a17c90b3d25f6a8c1d73`). Likewise the local `surface_grader` regex is an advisory forensic proxy only: the platform rubric (09) is authoritative for decision polarity, timezone, destination-issue binding and deliverable completeness (the regex matches the decision keyword, not its negation/instant/owner), so the measured difficulty at `/create-difficulty` rests on the rubric verdicts, not on these regexes.",
  "- **Known-issue cards kept off the path**: SC-13/14/18/38/62/68 are near but never required or cited "
  "(`f_a325dd4af80afc5994d5dc` is the only required sheet, used for English `PNs Beta` copy only).",
  "")

# ------------------------------------------------------------------ 14 reach table
w("## 14 · Reach table (load-bearing records)",
  "",
  "Every scoped load-bearing id re-verified with `persona_view can-see julia_lawson` (base = YES; planned seeds = "
  "UNVERIFIED (U4), verified at the injection gate). Linear / GitHub / Trello are unscoped (always readable).",
  "",
  "| Record | Service | Visibility path | LB |",
  "|---|---|---|---|")
reach = [
    ("slack:C08R8CHB0QL/1758121809.236839", "slack", "YES — member of #zombie-art", "LB"),
    ("slack:C08R27X0EAH/1758546048.524829", "slack", "YES — member of #zombie-bugs", "LB"),
    ("slack:C08R27X0EAH/1758546119.789009", "slack", "YES — member of #zombie-bugs", "LB"),
    ("slack:C05KNDCHAAG/1757704290.799329", "slack", "YES — member of #company-internal", "LB"),
    ("slack:C05KNDCHAAG/1758558302.777379", "slack", "YES — member of #company-internal", "LB"),
    ("slack:C090N54TG79/1758517286.431379", "slack", "YES — member of #zombie-design", "LB"),
    ("slack:C05433XK267/1759263189.219529", "slack", "YES — member of #builds", "LB"),
    ("slack:C0880U9751A/1759265412.481907", "slack", "UNVERIFIED (U4; if injected, use check-sql) — planned seed: Vincent's cross-channel leagues re-test root (channel C0880U9751A is a Julia-visible base channel)", "LB"),
    ("f_a325dd4af80afc5994d5dc", "gsheets", "YES — shared with Julia (base push sheet)", "LB"),
    ("d_8140f09bf9f1b94cb8ee2d", "gdrive", "YES — Julia's own Drive root", "LB"),
    ("ZOM-78", "linear", "YES — unscoped service", "LB"),
    ("ZOM-429", "linear", "YES — unscoped service", "LB"),
    ("harmonygames-Games/match3d#470", "github", "YES — unscoped service", "LB"),
    ("6851a724601a61857a1b202f", "trello", "YES — unscoped service (ZM ROADMAP quests card)", "LB"),
    ("f_7c3e91a4d2b85f60e1a9c4", "gdocs", "UNVERIFIED (U4; if injected, use check-sql) — planned seed: Frederick's brief", "LB"),
    ("f_2b9d4e7a1c63f08d5e7b21", "gslides", "UNVERIFIED (U4; if injected, use check-sql) — planned seed: UA deck", "LB"),
    ("f_e4a17c90b3d25f6a8c1d73", "gsheets", "UNVERIFIED (U4; if injected, use check-sql) — planned seed: Julia's calendar sheet", "LB"),
    ("d_5f2c8e1b7a94d03c6e2b58", "gdrive", "UNVERIFIED (U4; if injected, use check-sql) — planned seed: ZM Live Ops folder", "LB"),
    ("evt_9a4c2e7f1b3d58e06c7a2f", "gcal", "UNVERIFIED (U4; if injected, use check-sql) — planned seed: Oct 8 release", "LB"),
    ("julia.lawson@harmonygames.co/1844835127305531392", "gmail", "UNVERIFIED (U4; if injected, use check-sql) — planned seed: Brian's slip thread", "LB"),
]
for rec, svc, path, lb in reach:
    w(f"| `{rec}` | {svc} | {path} | {lb} |")
w("")

# ------------------------------------------------------------------ 15 record plan
w("## 15 · Record plan for /create-injection",
  "",
  "What `/create-injection` must seed (≥ 10 services; companions counted separately). Each row carries its planned or "
  "base pointer.")
recplan = [
    ("Slack", "Frederick's ask DM; Robert's #zombie-art approval reply + his DM withdrawal; Vincent's Sep 30 re-test root in #zombie-match3d (C0880U9751A/1759265412.481907)", "slack:D05SD5QLG94/1759263600.418207"),
    ("gdocs", "Frederick's beta brief (rules R1-R6, R8), shared with Julia", "f_7c3e91a4d2b85f60e1a9c4"),
    ("gslides", "Frederick's beta UA plan deck (the four buy weeks)", "f_2b9d4e7a1c63f08d5e7b21"),
    ("gcal", "Douglas's backend release plan event Wed Oct 8 + per-attendee copies + INT-11 invitation mails", "evt_9a4c2e7f1b3d58e06c7a2f"),
    ("gmail", "Brian's Oct 29 handoff thread and his Oct 31-Istanbul slip thread (Frederick cc)", "julia.lawson@harmonygames.co/1844835127305531392"),
    ("gdrive+gsheets", "Julia's 'ZM Live Ops' folder; her calendar sheet and push sheet (owner Julia in both rows)", "d_5f2c8e1b7a94d03c6e2b58"),
    ("linear", "owner notes on the open live-ops issues (e.g. Douglas on ZOM-429); the ZOM-78 reuse comment", "cmt_zom429_1"),
    ("github", "Arthur's inline note on #470; post-merge review notes on #370/#438; Marcus's #454 conversation note; Samuel's #471 note", "harmonygames-Games/match3d#470#rc_10"),
    ("trello", "Brian's comment on the quests roadmap card (new set from Oct 13)", "6851a724601a61857a1b202f"),
]
w("", "| Service | Seeds | Pointer |", "|---|---|---|")
for svc, seeds, ptr in recplan:
    w(f"| {svc} | {seeds} | `{ptr}` |")
w("",
  "Every seed lands at or before `2025-10-01T00:00:00Z` and after the base events it names (chronology in Pre-Scenario "
  "§5.6). Planned ids are collision-checked free (R-C §7): next free Linear key `ZOM-567`; the `#470` conversation-"
  "comment suffix avoids the PR's commit ids by using `#rc_10`/`#c_18`.",
  "")

# ------------------------------------------------------------------ 16 integrations
w("## 16 · Integrations and companions",
  "",
  "Companion rows (counted separately from the 10 services) and the `integrations.json` sources that mirror each "
  "seeded record. `#zombie-prs` (C093LEZGF6J) is NOT visible to Julia, so any GitHub→Slack mirror is a companion, "
  "never evidence.")
w("- github → Slack mirror of a PR comment: `INT-01` (GitHub Slack app) — companion in `#zombie-prs`, not load-bearing. "
  "Injection constraint (H3, `research/H3_reviewblocker_companion_audit.md`): the base INT-01 mirror carries the FULL "
  "comment body verbatim; because Julia is NOT a member of #zombie-prs (ACL), `/create-injection` seeds the faithful "
  "INT-01 mirror for integration parity (suppressing it would make the seeded comment the only PR comment without a mirror); it stays non-load-bearing by the ACL, not by suppression, and the deciding text goes in `review_comments` (human `reviews.body` are empty in this cohort).",
  "- github → Gmail notification of a PR comment: `INT-12` — companion in Julia's mailbox.",
  "- linear → Slack DM notification of an issue comment: `INT-04` — a generic 'commented on' notice, no comment text.",
  "- gcal → invitation / update / RSVP mails for the Oct 8 release event: `INT-11` — per-attendee companion mails.",
  "- gdrive → Slack app DMs (shares, comments): `INT-13` — companion when the brief/sheet is shared.",
  "- slack → Slack email notifications: `INT-22` — companion, never required.",
  "- github CodeRabbit reviews: `INT-23` — base bot content on every PR, never the deciding human note.",
  "- trello → Slack: `INT-21` — NO integration exists; no companion for the quests-card comment.",
  "- gdocs / gslides / gsheets: no dedicated integration source beyond the gdrive share (INT-13); no companion of "
  "their own — none.",
  "- gmail: a destination of INT-11/INT-12, not a source; no companion of its own — none.",
  "")

# ------------------------------------------------------------------ 17 red team
w("## 17 · Red team",
  "",
  "RED TEAM FALLBACK: the dual red team ran as two independent GPT-6.1 Sol subagents (an adversarial `redteam` pass "
  "and a `methodologist` pass) on this design and the draft manifest, because no `REDTEAM_*` environment is "
  "configured; their findings and dispositions are recorded in `01b_Redteam_Review.md` and "
  "`01b_Redteam_Review.second.md`, and the requester approved this fallback (decision D4). See §18 for the "
  "disposition of every finding.",
  "")

# ------------------------------------------------------------------ 18 self-review
w("## 18 · Self-review",
  "",
  "Hardness gate (re-run verbatim head; the stage gate re-runs and must agree):",
  "",
  "```text",
  "HARDNESS GATE (extreme (design)): PASS",
  "```",
  "",
  "Hardness v2 (Opus 5.5) self-checks (advisory; `research/hardness_v2_check_design.txt`): SAME_PLACE, DONE_CHECK, "
  "TWO_DECISIONS, INPUT_CHECK, FILTER_CHECK all CLEAN; DECISION_FLIP FLAG on `R_COPY_CURRENT`, `R_WIRED` and "
  "`R_HOLD_SCOPE` (each flips only weight-3 slots). Disposition: all three are intentionally secondary "
  "interpretation-band (weight-3) mechanisms whose honest work kind is applying one stated rule to one row — "
  "`R_COPY_CURRENT` (old-title copy rule, P01/P02/P06), `R_WIRED` (the second 'Status (NA, WIP, LIVE)' wiring column, "
  "P03 Plague Race start and P07 Weekly Leaderboard reset, both Ready-but-WIP) and `R_HOLD_SCOPE` (the over-application "
  "twin of the hold rule, flipping the Endless/Zombie Lane/Season Pass "
  "'runs' samples C02/C03/C04 when a run over-holds a cosmetic/perf/iOS-verify fault). Raising any of their weights "
  "would violate the QC weight-by-work-kind rule. The weight-5 difficulty is carried by the nine reconciliation "
  "mechanisms that DO flip weight-5 slots (R_DONE_DEPLOY, R_WITHDRAWN, R_SCOPE_BEATS, R_TECH_HOLD, R_HANDOFF_SLIP, "
  "R_LOCK_BOUNDARY, R_DONE_ELSEWHERE, R_REVIEW_FLAGS, R_QUEST_SET); these three add distinct failure patterns — an "
  "over-hold direction independent of the under-hold R_TECH_HOLD — at weight 3.",
  "",
  "Trap liveness (advisory; `research/trap_liveness_design.txt`): breadcrumb flags on T3, T4, T5, T6, T9, T11, T13 and "
  "an order flag on T6.")
w("", "| Flag | Disposition |", "|---|---|")
w("| T4/T5 breadcrumb (brief) | Intended — the brief (`f_7c3e91a4d2b85f60e1a9c4`) is the rulebook the ask names; an "
  "authority must be findable. The difficulty is applying its rule against a convincing wrong reading elsewhere "
  "(Ready flags, merged PRs), not hiding the brief. |",
  "| T3/T9/T11/T13 breadcrumb | The flagged record is the brief or a base pipeline post one hop from the hub; the "
  "deciding records that beat each trap sit deep (per-PR inline notes `harmonygames-Games/match3d#470`, a DM thread "
  "reply, a UTC computation). |",
  "| T6 breadcrumb + order | Intended — the ask names the calendar ticket (`ZOM-78`); reuse-vs-new is a weight-1 "
  "destination check, not a difficulty carrier. |")
w("",
  "Forecast (pre-registered `hev_10c8bb5be00ab2cf`, UNCALIBRATED, frozen to the final manifest+surface; "
  "`research/hardness_forecast_design.txt`): E[avg] 0.660-0.672, P(all four difficulty gates) 0.479-0.533 - "
  "E[avg] is comfortably under the 0.77 goal bar, but P(all) STRADDLES the 0.5 bar (independent 0.479, "
  "correlated 0.533). After the round-3 repairs this matches the round-2 borderline (0.658/0.520): the "
  "enrichment added length (the 47-member cohort, ~255 evidence units, >=150 unbatched reads) and one clean "
  "weight-5 reconciliation (the S11 Collect & Win icon scope gap on `R_ICON_SCOPE`), but did NOT raise the "
  "forecast difficulty - the apparent gain in an earlier draft came from an over-reaching `R_INFRA_SCOPE` "
  "attribution that both reviewers correctly flagged, now narrowed to one honest over-hold (Plague Race via "
  "the un-queued queue-manager panel). The LIMITER is the SD-band gate (expected six-run SD ~0.106, just "
  "above the 0.10 floor), not the difficulty: E[avg] 0.66 clears avg < 85% with ~0.99 probability. Binding "
  "risk (both independent reviewers, `01b_Redteam_Review.md` / `01b_Redteam_Review.second.md`): four "
  "mechanisms (R_WITHDRAWN A11, R_LOCK_BOUNDARY A19, R_REVIEW_FLAGS A3, R_QUEST_SET A13) have no Opus 5.5 "
  "ledger record and sit on a flat Beta(1,1)=0.50 prior (~33/108 of the weight); the methodologist's "
  "independent sensitivity (those four at ~10%) gives E[avg] ~0.756 and P(all) ~0.480, so a thorough Opus "
  "that reconciles the retrieval-bound carriers could clear the 85% cap. The enrichment does not by itself "
  "turn retrieval VOLUME into harder performance (both reviewers): more records can aid enumeration as much "
  "as burden it, so the ~50% miss on the flat-prior carriers is an unhedged assumption, not a proven "
  "bigger-haystack fact. This is UNCALIBRATED and resolved only by the six real Opus 5.5 baselines at "
  "`/create-difficulty`; first-time pass is a coin-flip on the SD gate. The difficulty rests on reconciliation "
  "that survives complete retrieval - the deploy/lock computations (S01/S10), the cross-channel leagues "
  "re-test (S03), the certify-absence review clause, the icon scope gap (S11: ZOM-465 struck 'all icons' done "
  "vs #454/#456/#475 omitting C&W, reachable via EITHER the Marcus #454 note OR the #456 enumeration, so it "
  "fails only when both are missed), and two over-application patterns over DISJOINT beats (fault-thread "
  "`R_HOLD_SCOPE` on Endless/ZL/SP, infra-gap `R_INFRA_SCOPE` on Plague Race; the addressables/#473 and "
  "token/ZOM-526 tickets are retrieval-context distractors, not graded) - not concealment. Highest predicted "
  "all-six-fail: S10 0.25 (Season Pass config), S06 0.21 (quests Oct 13 rollover), S08/S09 0.15 - all "
  "reachable (`julia.lawson@harmonygames.co/1844835127305531392`, `6851a724601a61857a1b202f`); VALID all-fail "
  "workload if they occur, not a block - for `/create-allfail`.",
  "",
  "### Two-reading tests (decision points)",
  "",
  "| # | The two readings | What decides |",
  "|---|---|---|")
tworead = [
    ("Merged client PRs 'done' vs live on prod", "the deploy rule + Arthur's #470 inline note + the Oct 8 release event → Fri Oct 10 00:00 UTC (`evt_9a4c2e7f1b3d58e06c7a2f`)"),
    ("Robert's thread approval vs his later DM", "the later call by the same Product owner stands (`slack:D05GU6L0XFH/1759270200.638114`)"),
    ("Ready flag vs the copy rule", "held for the copy owner; 'send with corrected copy' is not accepted (`f_a325dd4af80afc5994d5dc`)"),
    ("The obvious event list vs the brief's scope", "the brief governs; the two rollovers are in (`f_7c3e91a4d2b85f60e1a9c4`)"),
    ("Restart-clearing faults vs the hold rule", "ZOM-534/556 are known issues, not holds (`ZOM-534`)"),
    ("Douglas's restart note vs Vincent's cross-channel prod re-test", "the later #zombie-match3d prod re-test decides; leagues held (`slack:C0880U9751A/1759265412.481907`)"),
    ("Lock day vs lock instant", "Oct 31 07:00 UTC is 7h late vs the Oct 31 00:00 UTC lock (`julia.lawson@harmonygames.co/1844835127305531392`)"),
    ("ZOM-432 open vs the frame shipped elsewhere", "Samuel's #471 note + Submission #135 → nothing left (`harmonygames-Games/match3d#471`)"),
]
for i, (tr, dec) in enumerate(tworead, 1):
    w(f"| {i} | {tr} | {dec} |")
w("",
  "### Strongest counter-readings",
  "",
  "A counter-reading per trap/mechanism: the most convincing wrong reading and the record that overturns it. "
  "Coverage of the seven QC categories and the hardness gate is stated after the table.",
  "",
  "| # | Strongest counter-reading (why a careful run could still fail it) | Overturning record |",
  "|---|---|---|")
counters = [
    ("C&W 'feature completed' + merged PRs read as live on Mon Oct 6", "Arthur's inline #470 note: server windows on dev only (`harmonygames-Games/match3d#470#rc_10`)"),
    ("Robert's documented #zombie-art approval read as final", "his later DM thread reply withdrawing it (`slack:D05GU6L0XFH/1759270200.638114`)"),
    ("The brief read as the event list everyone names", "the brief's scope sentence brings in the two rollovers (`f_7c3e91a4d2b85f60e1a9c4`)"),
    ("Push Ready flag read as sendable", "the copy rule + the August rename: 1-day lapse still says the old title (`f_a325dd4af80afc5994d5dc`)"),
    ("Plague Race push Ready read as wired", "the second 'Status (NA, WIP, LIVE)' column reads WIP (`f_a325dd4af80afc5994d5dc`)"),
    ("The Sep 22 thread 'working fine' read as resolved", "Vincent's Sep 30 prod re-test, a #zombie-match3d root in another channel (`slack:C0880U9751A/1759265412.481907`)"),
    ("Brian's first handoff date (Oct 29) read as the commitment", "his later slip mail (Oct 31 Istanbul) in another thread (`julia.lawson@harmonygames.co/1844835127305531392`)"),
    ("Oct 31 10:00 Istanbul read as before the Nov 1 season", "the 24h-before-00:00-UTC lock from base `page_season_pass_spec` (the brief only points to 'before its lock'): 07:00 UTC is 7h late (`…/1844835127305531392`)"),
    ("ZOM-432 open read as still-to-do for daily login", "Samuel's #471 note + Submission #135 frame shipped (`harmonygames-Games/match3d#471`)"),
    ("A merged PR with an APPROVED read as nothing-left", "post-merge inline notes add still-to-do art/config (`harmonygames-Games/match3d#370`)"),
    ("A PR comment count of 1-2 read as no human flag", "Marcus's #454 conversation note on the C&W icon (`harmonygames-Games/match3d#454#c_4`)"),
    ("Quests rollover read as running its new set from week 1", "Brian's Trello comment: new set from Oct 13 (`6851a724601a61857a1b202f`)"),
    ("Boss Arena on Leonard's pipeline read as a beta beat", "the brief keeps Boss Arena off this calendar (`slack:C05KNDCHAAG/1757704290.799329`)"),
    ("Martin's Halloween app-icon read as a live-ops beat", "an app icon is not a window/reset/push (`slack:C08R8CHB0QL/1758121809.236839`)"),
    ("The translated push tab read as ZM3D beta pushes", "the brief scopes beta pushes to English PNs Beta (`f_a325dd4af80afc5994d5dc`)"),
    ("'Win & Collect' (Domino name) copy read as fine for ZM3D", "the ZM3D event is Collect & Win; held under the copy rule (`f_a325dd4af80afc5994d5dc`)"),
    ("An open or diagnosed fault thread read as a beat hold", "the hold rule needs an enter/score/claim failure after a restart; a shader / heating / iOS-verify fault is a still-to-do, not a hold (`slack:C08R27X0EAH/1759249488.495439`)"),
    ("The un-queued Plague Race panel (queue manager in progress) read as a Plague Race hold", "the queue orders panel animations additively; an un-ordered panel is engineering wiring, not an enter/score/claim blocker - Plague Race runs (`ZOM-543`, `harmonygames-Games/match3d#459`/`#472`)"),
    ("ZOM-465's 'all event icons' struck done read as every icon animated", "the three animation PRs enumerate a subset that omits Collect & Win, so its icon animation is still to do (`harmonygames-Games/match3d#456`)"),
]
for i, (c, o) in enumerate(counters, 1):
    w(f"| {i} | {c} | {o} |")
w("",
  "QC-category coverage of this review. temporal: seed chronology and the review-timestamp hazard T01 "
  "(`harmonygames-Games/match3d#470`). semantic/category: cross-game push copy (`f_a325dd4af80afc5994d5dc`). "
  "referential (cross-service): the deploy chain spans GitHub, GCal and the brief (`evt_9a4c2e7f1b3d58e06c7a2f`). "
  "quantitative: the UTC lock conversion, the only computed instant (`julia.lawson@harmonygames.co/1844835127305531392`). "
  "state/lifecycle: open issues vs shipped fixes (`ZOM-429`, `ZOM-432`). identifier/format: lookalike people and "
  "ZOM/ENG id collisions (§4). other: the local-grader two-table forensics caveat (§13). HARDNESS GATE: extreme "
  "(design) PASS, re-run above.",
  "",
  "Correct-reading count: 19 counter-readings above, each with an overturning record, exceeding the floor of "
  "7 + 9 decision points = 16. Unresolved: the difficulty is UNCALIBRATED and BORDERLINE (the enrichment added "
  "length but matches the round-2 difficulty) - P(all four gates) 0.479 (independent) to 0.533 (correlated), "
  "pessimistic ~0.480, resting partly on four flat-prior mechanisms (~33/108); the SD-band gate is the fragile "
  "one (expected six-run SD ~0.106, just above 0.10) and the forecast's `source` scenario does not test "
  "shared physical sources; a thorough Opus is the binding risk (forecast paragraph above), resolved only by "
  "the `/create-difficulty` baseline. The ~255 evidence units / >=150 unbatched reads is a workload estimate, "
  "not a necessary-call claim; the ~130 counted floor is confirmed only by an efficient correct trajectory at "
  "the baseline. The S10 (0.25), S06 (0.21) and S08/S09 (0.15) all-six-fail risks are recorded as VALID "
  "all-fail workload for `/create-allfail` (all values reachable); the two-table local-decode caveat is a "
  "forensics hand-normalization item for `/create-hardening`. None is a blocking defect at this stage.",
  "")

out = WF / "01_Scenario_Design.md"
out.write_text("\n".join(L) + "\n")
print(f"wrote {out}: {len(L)} lines, {sum(len(x) for x in L)} chars")

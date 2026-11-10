# Pre-scenario analysis — Claire Morgan · Design · Marketing and GTM · Authoring · Long Horizon · Medium · synth-cut

Analysis only. This file contains no prompt, Oracle Event or criterion text. Everything below is an input to
`/create-scenario`, which re-reads every load-bearing value through `tools/hg.py` before it designs anything.

| Item | Value |
|---|---|
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Seed bound | `freeze_utc` 2025-10-01T00:00:00Z (every seeded event timestamp at or before it; `sql_lint.py` enforces it) |
| Persona today | Wednesday, October 1, 2025 (Claire works on GMT+3; persona-written dates are Pacific, both given when the days differ) |
| Universe | `synthcut`, hg4-synth-sep30cut v16, KB `bound` (`references/universe_kb/by_universe/synthcut/`); no shutdown rules; Victor Barnes cannot act |
| Assignment | Claire Morgan, Art Lead · Design · Marketing and GTM · Authoring · long-horizon (Long Horizon) · medium (cap < 85 %) |
| Context | `task_context.py --task-dir Task_Authoring/task_inputsN2 --write --require-source` → `source.status: ready`; `context_hash` 90d7959d79c8…; `assignment_hash` fb0a0d31ccbc… |
| Evidence files | `Working_Files/research/`: `persona_reach.txt`, `entity_claire.txt`, `can_see.txt`, `00_sketch_manifest.json` (+ `_control`), `00_sketch_surface.json`, `hardness_v2_check_sketch.txt`, `hardness_v2_check_control.txt`, `geometry_mc.py`, `00_geometry_config.json` (+ `_stress`), `geometry_mc_output.txt` (+ `_stress`). Request files for the reads are in `Working_Files/scratch/`. |
| Inputs read | `setup/GEN_EXECUTION.md`; `learnings` §1–59; `support/completed_tasks/README.md` + all 7 folder READMEs; `task_inputs/Working_Files/00_Pre_Scenario_Analysis.md` (Vincent; structure, gate table and Part 7 method reused after re-checking against the Evals and the medium cap; his facts are about another persona and were not reused); `references/Scenario_Atlas.md`; `playbooks/01_Scenario_Design.md`, `12_Difficulty.md`; `references/Docs/13_Hardness_v2_Opus55.md`; Evals 0/1/1A/2/3, `ENVIRONMENT.md`, `rules/task_categories.md`, `long_horizon.md`, `scoring.json`; `references/known_data_issues/synthcut.md`; `Ask_Carriers.md`; the 2026-10 Injection Schema Guideline (64 writable tables) |

## 1. What a 5 needs at each gate

| Gate | A 5 / PASS needs | What this task must do |
|---|---|---|
| `/injection` (`Evals/0_Injection_Quality_Eval.md`) | Lint clean (no `future_date`, `id_contract`, `drive_unreadable`, `duplicate_account`, `actor_name`, `generated_column`, `text_time_format`, `missing_required`); Check A every reference resolves (actors, parents, channels, owners), no key collision, one account per person; Check B valid against the live schema (generated `text_fts` / `body_text_fts` never written, Linear text dates `YYYY-MM-DDTHH:MM:SSZ`, NOT NULL columns such as `state_history_json` set); Check C every seed after the base events it relies on, at or before the clock, no introduced contradiction, no grader-facing or padding text | Census every seeded fact against the **whole** universe (every mailbox, channel, sheet, repo), not Claire's view (learnings §10, §12). Only the 64 writable tables (no Snowflake, no `public._changelog`). Every Drive file a Docs body or real `content_path` bytes. Companions: Slack thread counters, Linear `updated_at`, Trello `badges`/`dateLastActivity`, one GCal row per attendee, Gmail INBOX/SENT copies per mailbox, INT-01 `#zombie-prs` mirrors for any GitHub review. `base_claims.py` for every build/branch claim (learnings §49) |
| `/prompt` (`Evals/1_Prompt_Eval.md`) | Every scored dimension 5, lowest wins: UGT (two-reading table, five checks, or BOTH_FAIR_FIGURE), Feasibility (tools, data, dimensional, numeric observability, persona-scoped reads), role plausibility, Cross-Service Coherence (fails on the **presence** of an inconsistency in task-touched data, pre-existing included; any State/Lifecycle or Quantitative one fails), naturalness (no trap hint, no spec-sheet register, no tool names, no opaque ids), truthfulness at the clock, assignment fit (business function 5, competency 5, task skill 5), complexity and seeding (a short trigger over seeded context), originality | An ordinary ask in Claire's voice naming its destinations; no rules, traps or contents lists in it. Touched data audited in all seven coherence categories; every designed disagreement a dated human claim that a later record overturns. Fit: Product & Design work (art evaluation, product decision about what ships how) on a Marketing & GTM problem (seasonal demand, store and ad creative, player communications), with a real authored artifact (Authoring "needs an authored artifact", `scoring.json:Assigned Task Skill`) |
| `/hardness` (`Evals/1A_Hardness_Eval.md`) | Score 5: "Genuine model failures invalidate the central result/delivery or defeat much of the core task"; 3–4 proceed; 1–2 hold. Call count, cohort size and design complexity are not evidence | The unhinted Opus run must make material, consequential errors that survive complete retrieval, spread over several independent decisions (section 6). The pre-check is one run: an early warning |
| `/oe` (`Evals/2_Oracle_Events_Eval.md`) | Completeness and Accuracy both 5: full critical path (discovery, dependency chains, writes); following the steps literally produces a correct trajectory; every `Expected:` value quoted from a cited record; one action per event; no non-action or final-response events; act-vs-defer checked | Every deciding record reachable from a prompt noun through records Claire can open; no value seen only in run output; the write steps match the authorized destinations |
| `/rubric` (`Evals/3_Rubrics_Eval.md`, `hg-strict-overrides-v1`) | No Major or Moderate, Minor < 5 %; weights 1/3/5 by kind of work; ≥ 1 Outcome, Process ≤ 50 % and each Process row passing the three-condition test; one fact per row, no fact in ≥ 3 rows; ≤ 5 samples per group + a volume row + direct exception rows; no row passable by doing nothing; no predicted all-fail row (local tolerance 0) | The gradable surface (section 6.4) is designed so every trap lands on weight-5 multi-source rows, guards are exact counts or scopes inside required writes, and every fair reading is accepted |
| `/create-difficulty` (`playbooks/12_Difficulty.md`) | Six Opus 5.5 slots, ≤ 2 errored; corrected weighted average **< 85 %**; **< 5** full passes; population SD 0.10–0.30; ≥ 2 failure patterns, largest ≤ 50 %; ≥ 100 counted calls (golden run, else the mean) | Design E[avg] ≤ 77 % (cap − 8), ≥ 4 independent loss channels with different findability so runs fail different subsets; honest volume ≥ 110 counted calls with no padding |
| Local gates | `stage_gate.py` per stage; `hardness_gate.py` at `effective_profile: extreme` (Long Horizon); dual red team or a recorded `RED TEAM FALLBACK:` | Section 10 records the decisions these need (volume exception, review fallback) |

## 2. Claire's reach at the clock

`python3 Task_Authoring/tools/persona_view.py reach claire_morgan --top 10` (full output in `research/persona_reach.txt`):

```text
REACH  Claire Morgan <claire.morgan@harmonygames.co>  Art Lead / Design
clock 2025-10-01

SLACK  user=EMPLOYEE_0009_SLACK_ID  visible channels=78 {'mpim': 17, 'public': 11, 'private': 27, 'im': 23}  messages=153666  public-not-member (UNVERIFIED)=56
  persona posts=9824 last post=2025-09-30  last activity in visible channels=2025-10-01
GMAIL  mailbox=claire.morgan@harmonygames.co threads=846 messages=923 range=2023-03-30..2025-09-30
  threads by last-message month (recent): {'2025-04': 60, '2025-05': 48, '2025-06': 35, '2025-07': 28, '2025-08': 20, '2025-09': 27}
GCAL  own=['claire.morgan@harmonygames.co'] shared=[] events=553 (distinct ical_uid 157, cancelled 67)
  last event before clock=2025-09-29T16:00:00Z  next after clock=2025-10-01T16:00:00Z
DRIVE  owned=69 {'application/json': 37, 'folder': 31, 'application/vnd.google-apps.spreadsheet': 1}
  shared-with=115 ... native visible: {'gdocs': 35, 'gsheets': 19, 'gslides': 1}  last modified visible=2025-09-30T16:30:39Z
  UNVERIFIED (domain/anyone, not owned/shared)=108
UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence
```

Identities (`entity.py resolve "Claire Morgan"`, `research/entity_claire.txt`): Slack `EMPLOYEE_0009_SLACK_ID`; Gmail
`claire.morgan@harmonygames.co` (thread files use the alias `claire@harmonygames.co_*`, hazard I03); GCal own calendar;
Drive `user_7fe31e7ec819`, root `d_7fe31e7ec81996189e1f14`, newest owned item 2024-07-08; Linear `usr_7fe31e7ec8199618`
(last activity 2025-09-03); GitHub `EMPLOYEE_0009_GITHUB_USERNAME` (last 2025-09-25; her commits author as a different
"claire" login, `entity.py collisions`); Trello `4bc5d398e54226f344ad3abc`; Confluence `user_EMPLOYEE_0009`; contact
`7fe31e7ec81996189e1f14d6`, job "Art Lead". KB `activity.json`: `active_sep_2025_quiet_in_oct`.

`can-see` on the records the storylines need (`research/can_see.txt`):

| Record | Claire |
|---|---|
| `#zombie-art` C08R8CHB0QL (public, 23), `#zombie_marketing` C06DJBJL798 (private, 17; she joined 2025-06-09 and never posted), `#zombie-match3d` C0880U9751A, `#builds` C05433XK267 | YES (member) |
| DM with Marcus Bennett D05V2N6PZNU, DM with Leonard Hayes D04V187QSTY | YES |
| Sheets `Push Notifications Zombie Match` f_a325dd4af80afc5994d5dc, `Keywords` f_ccf81b1512ef542fac5f8d; Doc `App Description` f_73432fbbce6c78fd648a87 | YES (shared_with) |
| `#executives` C07C2866011, `#zombie-design` C090N54TG79 | NO (not a member) |
| `Video Production Plan for Zombie Match` f_27a041fdb116695b01c566, `Zombie Match UA Creative Ideas` f_8dd9f174bdd22042103200 | NO (Resource-owned, empty sharing: visible to no persona) |

What matters for an Authoring task:
- **She owns no Doc, no Slides and one 2023 "Untitled spreadsheet"**, so every write target is a file she creates at
  run time (`gdocs_create_document`, `gsheets_create_spreadsheet`: the creator is the owner). A seeded "shared with
  writer" target resolves as a reader at run time and 403s (learnings §31; the archived Claire storefront task lost
  both sheet writes this way).
- Her marketing surface is `#zombie_marketing` (quiet since 2025-09-04) plus `#zombie-art`, where she is active to
  2025-09-30. Every UA manager (Victoria Lane, George Miller, Megan Wilson) shares no channel with her; Frederick Stone
  (Commercial Lead, Marketing & BD) shares 21.
- Gmail is a receiving surface (7 sent messages in her life). No agency, store-console or ad-network mail reaches her
  mailbox; the Sep 2025 "Notes: POD: PROTOTYPE" mails do (`claire@harmonygames.co_1842079678971290552`,
  `…_1842170562118420974`, `…_1842351877756275528`, `…_1844625524254242367`).
- Her calendar after the clock holds only the Wed 2025-10-01T16:00Z Mid Week Art Sync (`evt_db8e6bc32e4038ac7063f6`),
  which is the sibling task's deadline anchor; this task avoids it.
- Records between 2025-10-01 00:00Z and 07:00Z exist and are visible, but are context only, never completed facts
  (Frederick's 00:45Z `#company-internal` post that he is flying to LA and will miss the internal meetings; the 05:44–05:51Z
  `#builds` jobs).

## 3. Fit (rule 2)

- **Business function, Design → Product & Design** (`Evals/references/rules/task_categories.md`): "Product decisions,
  gameplay/design requirements, art and prototype evaluation." The work must be judging art (which seasonal concepts and
  existing assets are usable) and deciding the product route (what can change without a build).
- **Competency, Marketing and GTM** (Taxonomy Screen 7): "Demand and retention, GTM, communications"; typical personas
  include "Artist"; outputs "Decks, memos, spreadsheets, emails". The problem must be a demand or retention or
  communications problem: store listing and ad creative, seasonal campaign, player-facing pushes.
- **Task skill, Authoring**: "Produce a deliverable: an email or message, document, slide deck, spreadsheet, or report."
  A chat reply does not establish Authoring; a Google Doc plus a tracker Sheet does.
- **Role**: an Art Lead owning the art side of a marketing moment is the defensible non-obvious match the CB example
  describes ("Marcus is an artist, not a marketer — but … the GTM work genuinely went through him"). It fails if the work
  drifts into featuring applications, ad-account setup or campaign economics (Frederick's and Leonard's work), or into
  in-game object production (the sibling task's scope).

## 4. Storylines

All three are distinct from `vincent-zm3d-release-gate` (QA gate on the Sep 30 store candidates) and
`claire-zm3d-october-object-handoff` (in-game 3D objects for Julia's October levels), and from the archived Claire
storefront pack (Domino Delights Q4 screenshot submissions; `/hardness` FAIL 2). They are also distinct from Julia's live
Marketing and GTM design in `task_inputsS` (its `00_Pre_Scenario_Analysis.md` at 18:00 today recommends a ZM3D beta-weeks
live-ops and player-push calendar for Oct 6 – Nov 2). That design seeds a Halloween one-off approval and withdrawal on
Martin's Halloween thread and grades the "PNs Beta" push rows and the Collect & Win / Plague Race windows; B1 keeps all
of those out of scope. Five more candidates were checked and rejected (4.4).

### 4.1 B1 (recommended) — ZM3D Halloween art plan: what gets a seasonal look, how it ships, who makes it

**Situation, verified in base.**
- Halloween 2025 is Friday Oct 31, 30 days after the clock. Zombie Match 3D (renamed from "Puzzles vs Zombies" on
  24 Jul 2025, `confluence page_zm3d_gdd` v2 2025-09-30) has no seasonal campaign anywhere (`LIVE_EVENT_PERFORMANCE`
  has no seasonal event; `PUSH_NOTIFICATION_STATS` campaign keys are `event_live`, `new_levels`, `daily_reward`,
  `comeback_7d`, `sale_weekend`).
- Martin Walsh posted a Halloween app-icon concept in `#zombie-art`, re-read for this analysis:
  `C08R8CHB0QL` ts `1758121809.236839` (2025-09-17), "*Halloween theme* for an app icon or an event", tagging Robert,
  Leonard and Julia, `AppIconHalloween.png` 2048×2048, `reply_count 0`; Claire reacted 👻 and 🎃. Nobody decided it.
- Robert: "we have the Halloween pack which has the tombstones and the mausoleum" (`C0880U9751A` ts
  `1738109783.735889`, 2025-01-28, re-read) and "The graveyard one can be from the halloween pack" (`2025-02.json /200`).
  The pack is in the repo: `match3d/…/KayKit - Halloween Bits (For Unity)/Prefabs` (90+ prefabs in the first 400 file
  matches, `hg.py search files github "Halloween Bits"`).
- Store spec: `ART-774` description (Done 2025-04-15) gives Play phone ≥ 1080×1920, tablet ≥ 1920×1080, ≤ 8, no
  transparency. Apple sizes include iPhone 6.5″ 1284×2778 and 5.5″, and iPad 12.9″ 2048×2732, 10.5″ and 8.3″ (re-read).
  It says one screenshot set per *required* display size without naming which displays are required, so it cannot by
  itself decide which sets a release needs. That needs a dated required-set record (5.1).
- The app icon is configured per build target in `match3d/ProjectSettings/ProjectSettings.asset`, and targeted searches
  found no alternate-icon implementation. The red team noted the read file is truncated, so this is corroboration, not
  proof. The route must be decided by an incorporated, dated release-owner record (C1), with the code as supporting
  evidence. Base also says the store icon should match the phone icon (`C06DJBJL798/2024-09 /52–53`).
  `ZOM-427` "App icon is too zoomed in for android" is open (Todo, 2025-07-22, re-read) and consistent: no record shows
  it fixed. Store listing art and UA creatives can change without a build.
- The last store submissions before the clock: `iOS Submission #50` 2025-09-30T18:43Z, `Android Submission #135`
  18:45Z (`#builds`). No later build is scheduled in any record.
- Rules already in the data that a seasonal pack must respect: Leonard's test hygiene ("same flat background, same pose,
  same order of zombies, very similar expression, same CTA / ad copy", `C06DJBJL798` 1749234411.792129) and the audio
  lesson ("record all our in-game videos with SFX but without music baked in", 1755116786.755519).
- Decoys already in the data: Domino Delights' Halloween icons (`#god-gameart C04V7N09LE7/2024-01 /19`, `2024-09
  /13–14`), the Sep 29 POD action "Martin Walsh will try another theme, possibly a cemetery, cave, or ice cave … for the
  endless mode" (an in-game theme, not a marketing asset), and the stale `Trello UA/BD` cards (untouched since March).
  ART-790 (Todo) and ART-792 (Team Epic) carry SC-16 lifecycle defects and stay off the path. They are never ownership
  or status evidence, so a correct run need not open them (red-team finding 1).

**The work (design level).** Claire turns Leonard's (or Frederick's, before he flies) Sep 30 Halloween ask into the
art side of the Halloween push. For every ZM3D player-facing marketing surface serving players on Sep 30, she evaluates
the art and decides:
- whether the surface can take Halloween dressing as it is, needs its art refreshed first, or is out for October;
- what the seasonal version reuses: Martin's concept, the KayKit pack, existing masters;
- when its art is due against the applicable cutoff, and who makes it.

She authors:
- a Google Doc plan for Leonard, Frederick, Martin and Marcus, carrying the per-surface art requirements and counts;
- a tracker Sheet with one row per surface;
- Linear tickets for the new art pieces;
- a reply to the asker with the links.

The build cut and the network plan are supplied constraints she applies, not her decisions. The art direction wording
is free; the required contents (which surfaces, the art call, the reuse, the cutoffs, the owners) are fixed by records
she can open.

**Services.** Slack, Gmail, Drive, Docs, Sheets, Slides, Linear, Trello, GitHub, Confluence, Snowflake, Contacts, GCal
(13 available; 10–12 carry weight).

**Hardness opportunities (section 6):**
- a build cut that decides which surfaces can be live by Oct 31;
- a "Halloween screens exported" claim with the iPad set missing;
- a UA cut already made, recorded away from the ask;
- an ad network paused for October in a later email from the UA owner;
- in-use surfaces outside the ask's list;
- a vendor's "new" Halloween pack that is the KayKit set already in the repo;
- Robert's seasonal art direction, under which cuts captured before the summer art refresh are refreshed first.

**Hazards.** SC-11/12/23 (never grade UA spend), SC-13 (no beta date from the Trello list name), SC-16 (no Linear status
as proof: deciding facts sit in dated comments), SC-27 (no deciding message in `#god-gameart`; the DD decoy is
read-only), SC-31/38/47/57/58 (no live-ops outage, Season Pass, Weekly Quests, `#zm-collect-win` or monster-roster
facts), SC-70 (Slack timezones read Los Angeles: seeded dates say PT). Theme screen: keep seeded text on "Halloween /
seasonal / theme" and away from bio-adjacent words. The App Description's "Survive the Outbreak" is base text; it is
not quoted or seeded. Measured: 13 Opus 5.5 runs on ZM3D data, zero refusals (`task_inputsH/.../R3_opus_failure_modes.md`).

**Sibling exclusions.** None of `ZOM-567`, `ART-793`, `f_3f40599bbc9095352d47ab`, `f_da218fea555af2d7ea40f3`,
`f_a2ebb8732a0c87fe4db5d0`, Trello `68d18fcc316524c02741d4ed`, the 2025-10-01T16:00Z art sync, match3d object PRs
#344–#462 or `C0880U9751A/2025-09 /401–402` (seasonal **object** ideas) is load-bearing. The same holds for Vincent's
`ZOM-570`, `f_0ebfccf33076f9dbf086bc` and his Sep 30 candidate threads, the archived storefront ids (`ART-794…869`,
`DES-313…372`, `C083AEASRPC`, `page_store_locales`, `f_b5fb884dc96261846b6c2c` as a source), and every completed task's
cohort and vocabulary. Against Julia's design, B1 adds nothing to Martin's Halloween thread
(`C08R8CHB0QL/1758121809.236839` is cited as base context only). It also makes no in-game event, live-ops window or push
row decision and does not use the "PNs Beta" tab.

### 4.2 A — ZM3D creative refresh after the rename and the summer art overhaul

Claire decides keep / redo / retire for every live store and UA creative family and writes the round-3 brief.

**Native evidence (richest of the three).** 24 creative families and 105 dated 2025 creative files in `#zombie_marketing`.
- Trello `688c4c7a522ad6c5a953a1c0` "Upload New Screenshots to Apple" moved to Done on 2025-08-07, after a rename on
  2025-08-01 dropped "and Google". This is a native done-gap.
- The end card was requested as L/P/S but delivered portrait-only (1753806161 → 1753806995 → 1753968186).
- The "paly" typo was fixed only in Slack (1756917181.043289).
- The audio and test-hygiene rules above apply.

**Against it.**
- Most statuses are contested in base: ART-790 is Todo after delivery and ART-792 is "Team Epic" after it shipped
  (SC-16). That is task-touched State/Lifecycle data, which fails Cross-Service Coherence on presence.
- The two plan docs that state the creative rules are readable by no persona.
- The acceptance of the Sep 3 export is in `#executives` (Claire NO).
- What is live on Google Play is underdetermined.
- Only about 10–12 families have three independent surfaces, so the cohort needs about 20 seeded members.

### 4.3 C — Collect & Win launch: event art and player-communications kit

Claire audits the event's variant art against its schedule and writes the launch beats.

**Native traps (crisp, code-level).**
- 3 scheduled colours (orange / blue / green, server whitelist in `match3d-backend` `win_and_collect_controller.ex`)
  against 5 art variants (`Blue2, Green2, Orange2, Pink2, Red1`).
- Client index 3 is "purple" but the prefab is `Pink2`.
- "Magical Wings" vs "Magical Winds".
- PR #477 "title change" is still open.
- Claire authored the potion items herself (match3d PR #370, merged 2025-08-13).

**Against it.**
- It reads as live-ops / Product Management, not Marketing and GTM.
- Claire cannot read the spec (`f_7989a718d6be1e4428b143`), the reward sheet or `#zm-collect-win`.
- No push copy, store beat or banner for the event exists.
- The best cohort is about 29 records on one service.
- Hazards: SC-18, SC-57, SC-13, SC-16.

### 4.4 Rejected after a records check

| Candidate | Why rejected |
|---|---|
| Marketing-art request backlog → Q4 plan | 32 requests natively, 9 with three surfaces; 12 of 32 statuses contested in base (SC-16 coherence risk); acceptance records in `#executives` and a Frederick–Leonard DM Claire cannot read |
| Q4 UA gameplay-capture brief | Claire has never directed capture (role); SC-58 makes the character layer ungradable; about a 15-row native key |
| Store-listing / ASO messaging refresh | Overlaps the archived storefront pack; reviews are one bulk Snowflake query (no per-record work) |
| Push-notification re-engagement kit | Copy work fits a PM or marketer better than an Art Lead (role 3–4); 105 stat rows collapse to one query |
| Community / influencer kit | `#zombie-social` and `marketing_partnerships` exclude Claire; no contacts to build on |

### 4.5 Comparison and recommendation

| | B1 Halloween art plan | A Creative refresh | C Collect & Win kit |
|---|---|---|---|
| Fit (Product & Design × Marketing and GTM, Art Lead) | Clear: art evaluation and a ship-route decision on a seasonal demand moment | Clear | At risk (reads as live-ops) |
| Base anchors in Claire's reach | Medium; the decision spine (build-bound vs build-free) is rich in code | Rich, but contested | Thin for Claire |
| Touched-data coherence | Mostly clean: forward-looking, new dated asks, with ART-790/792 and the stale UA/BD cards kept off the path (S1 audit to confirm) | Contested statuses (SC-16) on the main path | Several known cards |
| Cross-source trap types available | 6 v2 types over 7 channels (traps 1, 2, 4, 5, 6, 7, 9) | 5 | 4, mostly one service |
| Native ≥ 40 × 3 cohort | No: about 25–35 seeded records | No: about 20 seeded | No |
| Honest minimum necessary calls (unique evidence) | about 90–135 (horizon risk; see 7) | about 110–160 | about 70–110 (under the tier) |
| Distinctness from siblings | High (no objects, no release gate, no storefront slots) | Medium (store screens) | High |

**Recommendation: B1.** It centres the graded work on Claire's own art calls (art currency, reuse, done-gaps,
aliases), with joins that remain after retrieval (6.1). It also keeps the touched data off the contested base statuses,
which A cannot avoid. The cohort and the asks have to be seeded, as in the sibling (121 INSERTs); that is the cost. The
red team's review (section 11) changed the plan in ten places.

## 5. UGT plan (rule 1)

### 5.1 Decisions, the rule that settles each, where the rule lives, and the census

| Decision | Settled by | Home (planned, Claire-visible) | Census before SQL |
|---|---|---|---|
| Which surfaces are in scope | "every player-facing ZM3D marketing surface serving players on Sep 30 PT": census date, qualifying states (live on a store or running on a network on that date) and grain (the rotation tab's own per-network rows; one row per store set) all stated by the asker. In-game events and push rows are out | the Halloween ask (Slack) + the dated rotation tab | Enumerate every surface serving on Sep 30 across both stores, the UA rotation, end cards, statics and web. Each member needs dated usage evidence; nothing serving may be left out (§21 sweep, positive control per learnings §35). Paused-network rows stay in the tracker with a "no cut this month" call, never silently absent (red-team finding 2) |
| Which store screenshot sets a release needs | a dated required-set record naming the displays (iPhone 6.5″, iPad 12.9″, Play phone, Play tablet), superseding `ART-774`'s general size list | a Linear comment or store-upload checklist (seeded, owner Leonard or Martin) | Each set checked against the record; `ART-774` cited as background only (red-team finding 3) |
| Each surface's art call (dress as is / refresh art first / out for October) | Robert's seasonal art direction + the art-currency rule (capture date vs the summer art refresh) + the network plan | Slides deck (hidden authority) + the per-cut origin posts | Every rule sentence × every surface class (store set, icon, UA cut, end card, static, web). No two sentences may give opposite answers on one surface (learnings §21). Graded by capture date, never by which zombies a cut shows (SC-58) |
| Ship route and live-by date | the release owner's dated record: icon changes ride a store build, plus the last Halloween-safe submission cutoff and the review allowance, all in PT. Store listing and network uploads are console-side | a dated comment off the ask's path (e.g. on `ZOM-427`) | Every date checked against `#builds` cadence and base git (`base_claims.py`); no claim of a build that does not exist. Code is corroboration only (red-team finding 5) |
| What is reused | completion records + pack identity | Linear comment, GitHub repo path, Contacts record, Robert's Jan message | Every "new art" item checked against existing deliveries and masters |
| Owners | the ask names who makes what by role (Martin: icon and stills; Marcus: video), consistent with base roles (`ART-774` assignee Martin; `ZOM-467` owner Marcus). ART-790/792 stay off the path | the ask | Owner tokens graded only where a record names the person |
| Art due dates | due on or before the **applicable cutoff**: the submission cutoff for build-bound art; the upload lead before the live-by date for console and network art. The live-by date is a separate fact (red-team finding 4) | the release-owner record + the ask | Each due date has a stated latest-acceptable date; earlier dates are accepted |

### 5.2 Two-reading tests, each resolved by a record

1. **Do both ad networks get Halloween cuts?**
   - A: Unity only. A later email from Frederick (UA owner) pauses AppLovin from a stated date that covers the Halloween
     window.
   - B: both, because the ask says both.
   - Resolved by newer source and authority (same item, same owner, dated after the ask). The AppLovin rows stay in the
     tracker with a "no cut" call, so A and B differ only on those rows' calls, which the mail settles.
2. **Is the icon a store-page swap?**
   - A: it ships in a store build.
   - B: change the 512×512 Play listing icon in the console.
   - Resolved by the release owner's dated record and the base best-practice record that store and phone icons match
     (`C06DJBJL798/2024-09 /52–53`).
   - The two readings write different things, so this is not a BOTH_FAIR_FIGURE fork. If `/create-scenario` cannot make
     B clearly wrong with a Claire-visible record, it stops grading the icon's route and keeps only its dates.
3. **Which UA creatives are serving?**
   - A: the dated rotation tab.
   - B: the stale Trello UA/BD cards.
   - Resolved by newer source and authority (a dated tab vs cards untouched since March). The cards stay off the path.
4. **Halloween source art?**
   - A: reuse the KayKit set.
   - B: buy the vendor pack.
   - Resolved by source identity (same pack, same items, already in the repo).
5. **Does "screens exported" mean ready?**
   - A: partly ready (a required set absent).
   - B: ready.
   - Resolved by scope: the dated required-set record plus the delivery folder contents.
6. **Does a cut take Halloween dressing as it is?**
   - A: refresh first, because it was captured before the summer art refresh.
   - B: dress as is.
   - Resolved by authority (Robert's direction) and the dated origin post of each cut.

### 5.3 Boundaries the rubric accepts in full

- Any art due date on or before the applicable cutoff.
- Any owner who matches the record that names the owner.
- Free wording of the Halloween art direction.
- File titles and tab names.
- Order of rows.
- Whether the summary counts also appear in the Sheet (they must appear in the Doc).

### 5.4 Known-data-issue dispositions

| Card | Disposition |
|---|---|
| SC-11, SC-12, SC-23 | Excluded: no spend, CPI or ROAS anywhere in the surface. The network plan is a dated decision, not a spend fact |
| SC-13, SC-14 | Excluded: no Trello list-name dates or `dueComplete` flags |
| SC-16 | Excluded and folded: ART-790/792 off the path; Linear status is never proof; deciding facts are dated comments on tickets whose state is consistent (`ZOM-427` open defect; `ZOM-467` ongoing umbrella; S1 audit to confirm) |
| SC-18 | Excluded: PR #477 |
| SC-27, SC-57 | Excluded: no posting or deciding message in `#god-gameart` or `#zm-collect-win` |
| SC-31, SC-38, SC-47 | Excluded |
| SC-36 | Excluded: share lists come from the ask, never from channel membership |
| SC-58 | Excluded: art currency graded by capture date, never by roster |
| SC-70 | Folded: PT stated in every seeded date |
| K02 | Folded: name lineage used only as context |

`/create-scenario` walks all 73 cards again over the final scope and cites each it touches.

### 5.5 Chronology and data horizon

Every seed sits after the base events it relies on and before 2025-10-01T00:00Z. For example:
- the ask after Martin's Sep 17 post and the Sep 30 18:45Z submissions;
- the release-owner comment after `ZOM-427` was created (2025-07-22) and after the Sep 30 submissions it plans beyond;
- the Marcus completion note after `ZOM-467` was opened (2025-08-12);
- Frederick's network mail after the ask;
- the rotation tab's date after the newest base cut it lists (`boris_fastcouch_9-16`, 2025-09-11).

Base records between 00:00Z and 07:00Z on Oct 1 are context only and are checked as possible supersessions of anything
a "current" answer depends on. None touch the B1 scope; re-checked at scenario.

## 6. Hardness plan (rule 4)

### 6.1 Loss channels

Seven independent channels on six distinct named v2 trap types (`references/Docs/13_Hardness_v2_Opus55.md` Part 3).
Each is a cross-source decision and names the convincing wrong source and the record that beats it. Each needs a
**join after retrieval**: the deciding record does not state the graded answer by itself (red-team finding 6).

Each flips at least one row weighted 5 by kind of work; C1, C2, C4, C5 and C7 flip two (red-team finding 10). The
largest channel decides 11 % of the planned weight.

| Ch | v2 trap type (Part 3) | Convincing wrong source (who, when, authority) | Record that beats it (who, when, authority) | Join that remains after retrieval | Findability | Rows it flips |
|---|---|---|---|---|---|---|
| C1 | 4 · Dates, windows and dependencies | The ask (Sep 30) to "swap the icon for Halloween", plus Martin's finished 2048² concept (Sep 17): reads as a store-page upload, any day | Arthur Blake's dated comment off the ask's path (e.g. on `ZOM-427`, release owner): icon changes ride a store build, with the last Halloween-safe submission cutoff and a review allowance in PT | cutoff × review allowance × the icon row → the art due date and the live-by date (knowing a build is needed is general knowledge; these dates are not) | Low–medium: `linear_list_comments` on a bug ticket the ask does not name | icon route (C1a); icon art due and live-by (C1b) |
| C2 | 1 · Proving "done" across services | Martin's seeded `#zombie-art` post "Halloween store screens exported" (owner of the screens) | the dated required-set record names four sets; the delivery folder holds three | the claim × the required-set record × the folder listing → which set is missing, then an owner and due date for it | Medium | store-screens status; missing-set owner and due |
| C3 | 9 · Work someone already did | The ask lists a new Halloween UA video | Marcus's comment on `ZOM-467` (his ticket) naming a delivered no-music cut by its **file name**, not as "the Halloween video" | the file name × the rotation tab rows (both networks) → that cut is ready, not requested | Medium | UA cut status (5); new-request count (3) |
| C4 | 2 · A correction somewhere else | The ask: Halloween cuts "for both networks"; base `AD_SPEND_DAILY` shows ZM3D on applovin and unity_ads through Sep 30 | Frederick's later email to Claire and Marcus (UA owner, in Claire's inbox): AppLovin paused from a stated date | pause date × the Halloween window → the AppLovin rows get "no cut this month" (kept in the tracker, not dropped) | Low–medium: `gmail_search_messages` returns ids only, so the body needs a read | AppLovin rows' call; plan states Unity only for October |
| C5 | 7 · Items outside the obvious filter | The ask's list and the `#zombie_marketing` history define the set | The scope rule ("serving players on Sep 30") brings in two serving surfaces named in neither (candidates: the live website's hero banner, `website` repo; the end card if the rotation tab lists it apart from its video). Pinned at scenario; push rows stay out | the scope rule × each surface's dated usage evidence | Medium for one, low for the other: runs miss one, both or neither | two member rows; tracker volume (3) |
| C6 | 6 · Different names for the same thing | A vendor mail (Claire's inbox) quoting a "Halloween asset pack" under a product name | The Contacts record links the vendor to KayKit; the same Halloween Bits set is in `match3d`; Robert calls it "the Halloween pack" (2025-01-28) | quote × contact × repo path → reuse, no purchase | Medium | plan reuses the pack (5); quote declined (3) |
| C7 | 5 · A rule or exception hidden in the data | The rotation tab lists every cut as serving; the ask wants "Halloween versions of our ads" | Robert's seasonal art-direction deck (Slides, rarely searched; decoy: his 2024 Domino Delights Halloween asks in `#god-gameart`, other game): dressing only on creatives showing the current art | each cut's origin-post date × the summer art-refresh date → "refresh first" for the older cuts. This is Claire's art evaluation | Low: a deck plus per-cut dates | two sampled exception cuts |

The load-bearing pair for the guide's "at least two" is C1 (trap 4) and C2 (trap 1); the other five add independent loss.

The heaviest work is Claire's art evaluation (C2, C3, C6, C7). C1 and C4 are supplied constraints she must apply, which
keeps the role and function fit centred on Product & Design (red-team finding 9).

The authorities are clear and incorporated: the ask delegates by role ("the release rules", "Frederick's UA plan for
October", "Robert's direction for seasonal art"), never by location. No hub lists the deciding records, and no
checklist carries an answer.

### 6.2 Not relied on

- Volume, routine writes, clean totals: there is no weight-5 aggregate.
- Visible caveats.
- Same-thread corrections: every correction sits in another service or container.
- Rules in the prompt.
- Keyword-findable wording: hidden texts say what happened in plain language (learnings §54).
- Base status-vs-status disagreements.
- Records only Claire-invisible channels carry.
- A deciding fact only on an injected Confluence page (learnings §26, §32).
- Anything Julia's `task_inputsS` design grades: in-game events, live-ops windows, push rows, replies in Martin's
  Halloween thread.
- A channel that is hard only because nobody searches (red-team finding 6): each needs the join above.

### 6.3 Part 7 self-checks, run by `tools/hardness_v2_check.py`

Run on the pre-scenario sketch (`research/00_sketch_manifest.json`, `research/00_sketch_surface.json`; planned ids,
containers declared explicitly; `research/hardness_v2_check_sketch.txt`):

```text
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      3 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 7 requirements: {'R2': ['R_BUILD_ROUTE'], 'R1': ['R_DONE_EXPORT'], 'R3': ['R_ALREADY_CUT'], 'R4': ['R_NETWORK_PAUSED'], 'R5': ['R_SCOPE_IN_USE'], 'R6': ['R_PACK_ALIAS'], 'R8': ['R_ART_CURRENT']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   7 of 7 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Earlier sketch runs shaped this one:
- The first counted only 5 cross-source requirements, because C3's completion note was a Slack DM reply, the same
  service as the ask. Moving it to a Linear comment made C3 cross-source.
- The second re-homed C4 (an in-game event dropped in a page comment) and C5's push-image member, because both collide
  with Julia's design.
- The third added C7 after the red team.

Positive control (`research/00_sketch_manifest_control.json`, C4's correction moved into the ask's own thread) proves
the check is live (`research/hardness_v2_check_control.txt`):

```text
  FLAG       SAME_PLACE      3 trap(s) with two or more version records; 1 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  SAME_PLACE T_C4 (same_container): the correction and a superseded version share slack:C06DJBJL798/planned-halloween-ask
```

Part 7 in words:
- **Done check**: Martin's "exported" claim vs the required-set record and the folder (C2).
- **Same place**: C1, C3 and C4 corrections sit in Linear or Gmail, never in the ask's thread.
- **Filter**: the obvious list misses two serving surfaces (C5).
- **Input**: no graded total depends on a changed input, so trap 8 is unused.
- **Decision flip**: every channel flips at least one weight-5 row.

`/create-scenario` S5b re-runs the tool on the real draft manifest and surface; injection re-runs it on the SQL.

### 6.4 Planned surface and policy scores (UNCALIBRATED, conditional; rule 5)

The planned surface (`research/00_sketch_surface.json`) has 23 slots, total weight 87 and 12 weight-5 slots:
- weights by kind of work, never raised;
- 5 ordinary samples plus one volume slot;
- exceptions are the members the authorities single out;
- three delivery slots.

It was scored by `research/geometry_mc.py`. The script grades simulated six-run baselines with the bundle's own gate
math (`difficulty_stats._gates`, **medium**, long-horizon). Output, verbatim (`research/geometry_mc_output.txt`, 20,000
draws per scale):

```text
  weight decided by channel: {'C1a': '5/87=6%', 'C1b': '5/87=6%', 'C2': '10/87=11%', 'C3': '8/87=9%', 'C4': '10/87=11%', 'C5': '10/87=11%', 'C6': '8/87=9%', 'C7': '10/87=11%', 'multi': '3/87=3%', 'ordinary': '18/87=21%'}

WHOLE POLICIES (deterministic, no slips)
   26.4%  P0 lazy: the ask + #zombie_marketing only
   37.9%  P1 + Slack-wide search and the delivery folders (no Linear comments, mail bodies, Trello, GitHub)
   75.9%  P2 + every Linear comment and every mail body (no Trello, no GitHub)
   90.8%  P3 everything retrieved, pack alias not connected
   85.1%  P4 everything retrieved, scope kept to the ask's list
   94.3%  P5 everything retrieved, build cut date not applied
  100.0%  P6 perfect
   88.5%  P7 everything retrieved, art-currency rule not applied

SINGLE MISSES (everything else right): 85.1–94.3 % (C5 both members 85.1 %; C2, C4, C7 88.5 %; C3, C6 90.8 %; C1a, C1b 94.3 %)

SIX-RUN BASELINES (20000 draws per scale; gate math = difficulty_stats._gates, medium, long-horizon)
  scale 1.00: E[avg] 61.3% (p10-p90 51.3%-71.5%)  E[SD] 0.167  P(avg<85%) 1.00  P(<5 full) 1.00  P(SD band) 0.82  P(patterns) 1.00  P(all four) 0.82  E[full passes] 0.12
  scale 0.75: E[avg] 69.6% (p10-p90 59.8%-79.1%)  E[SD] 0.161  P(avg<85%) 0.98  P(<5 full) 1.00  P(SD band) 0.79  P(patterns) 1.00  P(all four) 0.79  E[full passes] 0.30
  scale 0.60: E[avg] 74.7% (p10-p90 65.3%-83.7%)  E[SD] 0.151  P(avg<85%) 0.93  P(<5 full) 1.00  P(SD band) 0.73  P(patterns) 1.00  P(all four) 0.71  E[full passes] 0.48
  scale 0.55: E[avg] 76.5% (p10-p90 67.4%-85.1%)  E[SD] 0.147  P(avg<85%) 0.89  P(<5 full) 1.00  P(SD band) 0.70  P(patterns) 1.00  P(all four) 0.67  E[full passes] 0.57
  scale 0.50: E[avg] 78.2% (p10-p90 69.3%-86.6%)  E[SD] 0.142  P(avg<85%) 0.84  P(<5 full) 1.00  P(SD band) 0.67  P(patterns) 1.00  P(all four) 0.62  E[full passes] 0.66
  scale 0.35: E[avg] 83.6% (p10-p90 75.9%-91.0%)  E[SD] 0.124  P(avg<85%) 0.57  P(<5 full) 1.00  P(SD band) 0.51  P(patterns) 0.99  P(all four) 0.39  E[full passes] 1.06
  scale 0.25: E[avg] 87.3% (p10-p90 80.5%-93.7%)  E[SD] 0.108  P(avg<85%) 0.30  P(<5 full) 1.00  P(SD band) 0.37  P(patterns) 0.98  P(all four) 0.21  E[full passes] 1.46
```

Dependence stress test (`research/00_geometry_config_stress.json`: per-run thoroughness loading 1.0 instead of 0.5,
member ρ 0.9; `research/geometry_mc_output_stress.txt`):

```text
  scale 1.00: E[avg] 61.1% (p10-p90 47.7%-74.9%)  E[SD] 0.226  P(avg<85%) 0.99  P(<5 full) 1.00  P(SD band) 0.76  P(patterns) 0.99  P(all four) 0.75  E[full passes] 0.49
  scale 0.75: E[avg] 67.8% (p10-p90 54.6%-80.8%)  E[SD] 0.220  P(avg<85%) 0.96  P(<5 full) 1.00  P(SD band) 0.76  P(patterns) 1.00  P(all four) 0.74  E[full passes] 0.74
  scale 0.60: E[avg] 72.0% (p10-p90 59.2%-84.5%)  E[SD] 0.211  P(avg<85%) 0.91  P(<5 full) 1.00  P(SD band) 0.76  P(patterns) 1.00  P(all four) 0.71  E[full passes] 0.94
  scale 0.50: E[avg] 74.9% (p10-p90 62.5%-86.8%)  E[SD] 0.202  P(avg<85%) 0.85  P(<5 full) 1.00  P(SD band) 0.75  P(patterns) 0.99  P(all four) 0.68  E[full passes] 1.10
  scale 0.35: E[avg] 79.6% (p10-p90 67.8%-90.6%)  E[SD] 0.184  P(avg<85%) 0.71  P(<5 full) 1.00  P(SD band) 0.71  P(patterns) 0.99  P(all four) 0.58  E[full passes] 1.41
```

**Assumptions.**
- Design miss rates: C1a 0.25, C1b 0.55, C2 0.50, C3 0.50, C4 0.45, C5 0.50 (two members), C6 0.45, C7 0.45 (two
  members). Slips are 0.03–0.06. A per-run thoroughness latent (loading 0.5) correlates the channels.
- Correction (red-team finding 8): with the member-sharing scheme in `geometry_mc.py`, the two members of a channel
  co-miss with a conditional correlation of about ρ² (0.36 for C5, 0.49 for C7), plus the shared thoroughness term. It
  is not ρ.
- Every probability is conditional on six completed runs: no errored runs, horizon not modelled.
- The Opus 5.5 ledger holds Beta(1,2) for A7 and A14–A17 (one robert-vendor-schedule trial each) and Beta(1.86,2) for
  the A1 family, and nothing for A11, A24 or A25 (`hardness_ledger.py priors --model claude-opus-5-5`).

**Reading.**
- Rule 5's bar (E[avg] ≤ 77 %, P(all gates) ≥ 0.5) holds down to a miss-rate scale of about **0.55** (76.5 %, P(all)
  0.67). At 0.5 the base model gives 78.2 %, just above the bar; the stress variant gives 74.9 %.
- At the design rates the model gives 61.3 % with P(all four) 0.82, or 0.75 under the stress variant.
- Every single miss leaves a run at 85–94 %. The cap therefore needs at least two misses per run on average, which is
  why there are seven channels.
- Retrieval policies P0–P2 score 26–76 %. A run that retrieves everything and slips on one join still scores 85–94 %. The
  joins in 6.1 are what `/create-scenario` must keep hard.
- `A3` now depends on C3 only. The highest P(row fails all six) at scale 1.0 is the tracker volume row (0.069, any C5
  member). Keep the volume row on the C5 cohort count, or give it one member, so the all-fail workload stays near zero.

### 6.5 Spread (rule 5)

Each channel is decided in a different service:
- Linear comment (C1, C3)
- the required-set record against the Drive folder (C2)
- Gmail body (C4)
- dated usage records in the rotation tab and repo (C5)
- Gmail plus Contacts plus GitHub (C6)
- Slides deck plus per-cut Slack dates (C7)

The findability tiers differ (6.1), so runs fail different subsets. In the model P(patterns) is 1.00 and P(SD band) is
0.67–0.82 at scales 0.5–1.0, or 0.75–0.76 under stress. No row is unreachable, so no row is a predicted all-fail in the
validity sense.

### 6.6 Difficulty target

The judged gate is Medium < 85 %, and the mode stays medium. Recommended design target: E[avg] ≈ 65–72 % with the
seven channels above, inside rule 5's 77 % ceiling (decision D4).

## 7. Volume plan

Scope: about 40–45 surfaces serving on Sep 30. The planned split is:
- store listing about 6 (icon, iPhone set, iPad set, Play phone set, Play tablet set, store video);
- UA creatives about 26 rotation rows (about 16 unique cuts, some on both networks);
- end cards about 3;
- statics about 5;
- web about 2–4.

Push rows and in-game surfaces are out of scope (Julia's task). The unit is a surface, not a pixel slot; per-network rows
are the rotation tab's own grain. `/create-scenario` must show the tab is the UA owner's real working record, not a list
made for the task.

Recomputed after red-team finding 7. Calls are counted on **unique** evidence:
- cuts on both networks share one master read;
- one network-wide pause settles all of a network's rows in one read;
- Slack replies are reachable by filtered search, so they are not counted as no-bulk per-record work;
- writes are counted at their minimum.

| Phase | Services | Necessary calls (min–likely) | Why necessary (no bulk call replaces it) |
|---|---|---|---|
| Discovery and anchors | Slack (ask thread, `#zombie_marketing` and `#zombie-art` Sep pages, searches), Gmail (search + bodies), Drive/Docs/Sheets search | 22–32 | The ask, the delegated rules and the delivery records live in different containers |
| Rules and authorities | Slides (seasonal direction), Linear (icon-ticket and video-ticket comments, required-set record), GitHub (repo pack path, icon settings), `#builds`, Contacts, Confluence (release checklist) | 12–20 | Each authority is its own record; `linear_get_issue` returns no comments (learnings §56) |
| Enumeration | Sheets (rotation tab), Drive (delivery folders), web (repo or site record) | 6–10 | Sources of the serving set |
| Per-record (unique evidence) | about 16 cut origin posts or files (capture date, audio master), 4–5 store sets (folder listing per set), 3 end cards, 5 statics, 2–4 web surfaces | 35–55 | The art-currency, reuse and readiness facts sit on each item's own record (`Ask_Carriers.md` §4) |
| Writes and read-back | Docs create + 2–3 `batch_update`; Sheets create + `addSheet` + 2–4 value writes; Linear 4–6 issues; Drive share 1–2; Slack reply 1; read-backs 2 | 14–20 | Every write is required content; no bolt-on |
| **Total** | 11–12 services | **about 90–135 minimum necessary** | |

**What this means.**
- The honest minimum is close to the 100-call tier, so the horizon is the binding risk, not the 500 target.
- Measured Opus 5.5 counts on comparable synth-cut long-horizon tasks ran above their minimum paths: Douglas 163–238;
  Julia 329–1,209; the archived Claire storefront pre-check 252. Arthur's 78–95 on a normal-universe task fell under the
  tier.
- `/create-scenario` must raise the per-record need only with honest per-item evidence: one origin record per cut and
  dated usage per surface. It must never add steps, records or services for volume (padding fails on its own,
  learnings §50). The pre-check's counted calls are the early warning: below about 130, revise before baselines.

≥ 500 necessary calls are not reachable without padding. A volume exception is needed (`GEN_EXECUTION.md` §3a,
`references/Hardness_Manifest_Spec.md`). The analysis recommended `{call_budget_floor: 120, per_record_floor: 40}`; the
requester chose a floor **above 150** (D2, section 10). `/create-scenario` designs the extra necessary calls from honest
per-item evidence or asks again. Every other extreme target stays:
- ≥ 10 services weighted / injected;
- cohort ≥ 40 × ≥ 3 surfaces over ≥ 2 services, by rule, with a shortcut audit per surface;
- ≥ 12 fragments over ≥ 7 services and ≥ 10 containers;
- 2–4 hidden authorities with decoys;
- ≥ 3 chains;
- ≥ 12 traps in ≥ 7 families;
- ≥ 120 INSERTs.

Golden-run rule: a correct run needs the per-record phase too, since each surface's call depends on its own evidence.

## 8. Writes and ownership (rule 6)

| Write | Trigger (authorized) | Destination | Access |
|---|---|---|---|
| Plan document | the asker's Sep 30 ask | new Google Doc Claire creates | owner (create); `gdrive_share_file` works for the owner |
| Tracker | same ask | new Google Sheet Claire creates (named tabs via `gsheets_batch_update addSheet`) | owner |
| New-art tickets | same ask (owners and dates) | Linear ART team, reusing an existing ticket where one exists (A8) | unscoped write |
| Reply | same ask | the ask's own thread (`#zombie_marketing`, Claire a member) | member |

There are no writes to base files: the push sheet, rotation tab, App Description and Keywords are read-only sources.
Docs cannot hold tables (`gdocs_batch_update` has no table kind), so the per-surface table lives in the Sheet and the Doc
carries the plan and counts. The trigger never asks for something Claire cannot do: no featuring application, no
console upload, no ad-network action.

## 9. Alignment (rule 7), risks and open items

**Alignment.** The ask is the anchor. Its incorporated delegations by role reach the rotation tab, the required-set
record, Robert's seasonal direction, the release rule, Frederick's network plan and the pack. Every OE step and
gradable slot traces to one of those records or to a base record. The prompt stays an ordinary request naming its
destinations: a plan doc, a tracker, a reply, tickets for new art. It names no rules, traps, ids or contents lists.

**Risks and open items.**
1. **Horizon is the binding risk.** The honest minimum path is about 90–135 calls (section 7), and the requester set the
   floor above 150 (D2). `/create-scenario` must close that gap with honest per-item evidence or come back. Opus runs on
   comparable tasks counted 163–252+, but one fast golden run under 100 fails Wrong Horizon. Watch the pre-check count.
2. **Cohort is seeded.** About 25–35 records and 150–250 rows. Each seed must be checked against the whole universe;
   for example, rotation rows must match base creative files (`cheer_fastcouch_9-16`, `boris_fastcouch_9-16`, the 30 s
   UA cut, the barrel 4:5 and 16:9 cuts, the portrait end card). The tab must read as the UA owner's working record.
3. **Icon route evidence.** It is corroboration only, because the `ProjectSettings` read is truncated. The deciding record
   is the release owner's dated comment. `/create-scenario` records the alternate-icon search with a positive control.
4. **C1a is general knowledge.** Only C1b's dates are weighted as hard. If the pre-check passes C1b, deepen the join
   (cutoff × review allowance × per-asset due) rather than adding rows (v2 Part 8).
5. **Leonard vs Frederick as asker.** Frederick is GTM owner but flies to LA on Oct 1 (base, context only). Leonard ran
   the icon and store-asset asks. `/create-scenario` picks the asker with a cited activity window.
6. **No red-team endpoint.** `REDTEAM_*` is unset (`env | grep -c ^REDTEAM` = 0); decision D3.
7. **Julia's live design in `task_inputsS` uses the same month, Martin's Halloween thread and the push sheet.** B1 stays
   on store, ad and web art and never decides an in-game event, live-ops window or push row. Each task's SQL is applied
   to its own runs, so no seed collides. Re-read her latest analysis at `/create-scenario` in case it moves.
8. **The C5 members are candidates.** The live website's hero banner depends on the site serving at the clock (POD notes
   Sep 1: "expected to go live by the end of the week"; `website` repo). `/create-scenario` verifies each member's dated
   usage or picks another serving surface outside the ask's list.
9. **Advisory only.** The geometry is advisory, UNCALIBRATED and conditional on six completed runs. `/create-scenario`
   replaces it with `hardness_forecast.py forecast --design --preregister` on the real surface.

## 10. Decisions needed from you

| # | Decision | Options | Recommendation |
|---|---|---|---|
| D1 | Storyline | B1 Halloween art plan · A creative refresh · C Collect & Win kit | **B1** |
| D2 | Volume exception (§3a) | `{call_budget_floor: 120, per_record_floor: 40}` · `{150, 60}` only if `/create-scenario` finds that much honest per-item evidence · none (forces padding toward 500, which fails) | **120 / 40** |
| D3 | Scenario red team (`REDTEAM_*` unset) | Recorded `RED TEAM FALLBACK:` with the `redteam` and `oracle` GPT-6.1 Sol subagents reviewing the design and manifest (as `task_inputsH` did) · waive (as Vincent did) · set `REDTEAM_*` and run `--dual` | **Fallback with the two subagents** |
| D4 | Design difficulty target (mode stays medium, < 85 % judged) | E[avg] ≤ 77 % (rule 5) · ≈ 65–72 % with ≥ 4 channels · ≤ 62 % (the Hard-tier tightening line in `00_Session_Goal.md`) | **≈ 65–72 %** |

Your answers (requester, 2026-11-04, through the question tool in this session):

- **D1: B1 Halloween art plan** (the recommendation).
- **D2: a call-budget floor of more than 150** (answered "more then 150"). This is above the honest minimum estimated in
  section 7 (about 90–135). `/create-scenario` therefore:
  - designs a `volume_exception` with `call_budget_floor` ≥ 151 (160 unless the design supports more) and a
    `per_record_floor` derived from the honest per-record rows (60 suggested);
  - reaches it only with real per-item evidence: one dated origin record per cut, dated usage per surface, a per-set
    delivery record, and more serving cuts if the rotation genuinely holds them;
  - never pads (filler records, steps or services fail on their own, learnings §50).

  If the honest per-record design cannot reach the floor, `/create-scenario` stops and asks you again rather than pad.
- **D2′ (2026-11-04, at `/create-injection`): over 180 tool calls in every run** (requester: "i want over 180+ tool
  calls in each runs"; pass rate under 80 %, under 70 % preferred). The completed tasks show the lowest run lands at
  0.93–1.01 × the unconditional floor when per-ticket writes are the deliverable (douglas 163 / 175, robert 116 / 115)
  and as low as 0.50 × when runs may skip per-ticket reads (arthur 78 / 155). Scenario revision 02 therefore raises
  `call_budget_floor` to **181** and lifts the unconditional floor from 173 to about 205 with real per-record work only:
  twelve more serving exports Frederick ticketed after Sep 12 (each with its own ticket, its own deciding comment, its
  own follow-through comment and, when it needs new work, its own assignment). No filler record, step or service.
- **D3: Waive review.** `/create-scenario` records
  `RED TEAM FALLBACK: requester waived the scenario red team on 2026-11-04 (D3 'Waive review'; REDTEAM_* not set, so redteam_review.py --dual cannot run)`
  in its section 13. The stand-ins are `hardness_gate --design`, `hardness_v2_check`, `trap_liveness`,
  `gradable_surface validate`, the pre-registered forecast and the self-review. The waiver stays on the `Unresolved:`
  line until the Opus pre-check covers it (learnings §44). This analysis itself had an independent `redteam` review
  (section 11).
- **D4: E[avg] ≈ 65–72 %** with the seven channels; the mode stays medium and < 85 % is the judged gate.

## 11. Independent review of this analysis

An adversarial `redteam` subagent (GPT-6.1 Sol, read-only, bounded source inspection; its shell checks were denied)
reviewed the first draft and returned **FAIL** with 2 BLOCKER, 7 MAJOR and 1 MINOR findings. Every finding was taken;
none was rebutted.

| # | Finding (severity) | Disposition in this revision |
|---|---|---|
| 1 | ART-790/792 used as ownership evidence while their lifecycle states are known defects (BLOCKER) | Taken. Removed from the path; owners come from the ask, consistent with `ART-774` / `ZOM-467` (4.1, 5.1, 5.4). S1 audit to confirm every touched record |
| 2 | "In use" had no census date, states or grain; paused-network rows ambiguous (BLOCKER) | Taken. "Serving players on Sep 30 PT", qualifying states and the rotation tab's grain are stated by the asker; paused rows stay with a "no cut" call; every member needs dated usage evidence (5.1, 5.2) |
| 3 | `ART-774` does not name the required screenshot sets (MAJOR) | Taken. Confirmed on re-read; a dated required-set record now decides C2 (4.1, 5.1) |
| 4 | "Any due date on or before live-by" accepts dates that miss the build (MAJOR) | Taken. Art due by the applicable cutoff; live-by is a separate fact (5.1, 5.3) |
| 5 | Alternate-icon absence overstated; `ProjectSettings` read truncated (MAJOR) | Taken. The route is decided by the release owner's dated record; the code is corroboration (4.1, 5.1, 9) |
| 6 | Several channels resolve directly once retrieved (MAJOR) | Taken. Each channel now needs a join after retrieval; C3's note names a file, not the answer; C4's pause has a date to compare; C7 added for Claire's art evaluation (6.1) |
| 7 | Call estimate double-counted shared evidence and searchable replies (MAJOR) | Taken. Recomputed on unique evidence: about 90–135; floor lowered to 120 / 40; horizon named the binding risk (7, 9, D2) |
| 8 | Geometry overstated (77.9 % at scale 0.5 is above 77 %); ρ is not the co-miss correlation; probabilities ignore errors and horizon (MAJOR) | Taken. Bar restated at about 0.55; ρ² corrected; stress test added; conditional label added (6.4) |
| 9 | Function and role 5 not established by the graded work (MAJOR) | Taken. Graded work re-centred on Claire's art calls (C2, C3, C6, C7); route and network are supplied constraints (4.1, 6.1) |
| 10 | Prose said every channel flips two weight-5 rows; C3 and C6 have one (MINOR) | Taken. Prose corrected; no weight raised (6.1) |

**Not established either way**, and carried forward to `/create-scenario`:
- an executable shortest-path audit;
- whole-universe seed checks;
- full Slack-body spot-checks;
- actual write success.

The reviewer found no sibling clone and no catalog-level blocker for own-file authoring, issue creation or threaded
replies.

Next step: run `/create-scenario` (with `TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputsN2`).

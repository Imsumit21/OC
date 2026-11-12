# Pre-scenario analysis: Julia Lawson · Product · Marketing and GTM · Authoring · Long Horizon · Hard

Analysis only. It contains no prompt, Oracle Event or rubric text. It covers what a 5 needs at each gate, the
fit census verdict and its route, Julia's reach at the clock, three storylines with a recommendation, the UGT,
hardness and volume plans, and my decisions. It stops before `/create-scenario`.

Two labels are used throughout. **Read** means I opened the base record in this session through
`Task_Authoring/tools/hg.py` or `persona_view.py`. **Planned** (`NEW-…`) means a record the injection would add;
nothing planned exists yet, and every planned record is re-derived at `/create-scenario` S1–S5.

## 0. Assignment and context (verified)

```
business_function:  Product                     persona:      Julia Lawson, Product Manager (julia_lawson)
competency:         Marketing and GTM           task_skill:   Authoring
task_type:          long-horizon                difficulty:   hard (cap: corrected weighted average < 70 %)
universe:           synthcut, Oct 1, 2025       seed bound:   2025-10-01T00:00:00Z (Sep 30, 17:00 PT)
eval clock:         2025-10-01 07:00 UTC        persona day:  Wednesday 1 Oct 2025; "yesterday" = Tuesday 30 Sep
source.status:      ready (fingerprint 35ef23cd…) kb_status:  bound      context_hash: 3246c54345b9…
```

`task_context.py --task-dir Task_Authoring/task_inputs --write --require-source` ran clean (no `SOURCE BLOCKED`).
Shutdown rules do not apply on synth-cut. Victor Barnes cannot act (left April 2025).

Design target from the mode (`playbooks/01_Scenario_Design.md` S0): cap 70 %, design to E[average] ≤ 62 %.

## 1. What a 5 needs at each gate

| Gate | What decides a 5 | What this design has to do |
|---|---|---|
| `/injection` | Static: every seeded id, reference, date and field agrees with the whole base, and no seeded event is after the seed bound. | Census every person, item name, ticket key and vendor fact across all services before seeding (learnings §10–§17). Date each seed after the base event it relies on. Keep all seeds before 2025-10-01T00:00Z. Confirm each seed comes back through the agent's own tools, not only in the SQL. |
| `/prompt` | PASS 5 needs every dimension at 5: assignment fit (a clear competency or task-skill mismatch is a hard FAIL; a function mismatch blocks a 5), Unique Ground Truth, feasibility, truthfulness, natural voice, cross-service coherence (fails on any inconsistency in touched data, even one that was already in base). | A real authored deliverable whose contents are fixed by records Julia can open. Product-and-design work inside a marketing job. Every rule sentence applied to every cohort member before SQL. No touched base conflict (§8). An ordinary request that names its destinations and nothing else. |
| `/hardness` | One unhinted Opus 5.5 run. Score 5 = "genuine model failures invalidate the central result or defeat much of the core task"; 3–4 proceed; 1–2 hold. | The single run must miss records it never opens, enough to make the central deliverable wrong. Two anchor records carry that (§6). The requester's message must not index where the rules live (learnings §79). |
| `/oe` | Passes or blocks. Any wrong or missing step, non-action or final-response event blocks. | Every graded fact reachable by a natural step from a prompt noun; side-record writes marked optional. |
| `/rubric` | PASS 5: no Major or Moderate issue, Minor on under 5 % of rows. ≥ 1 Outcome row, ≤ 50 % Process, weights 1/3/5 by kind of work, at most five samples per group plus a volume row, direct rows only for members a record singles out, no fact in three or more rows, no row an idle agent passes. | Decide the row shape at design time (§6.4): sampled plain members, one direct row pair per singled-out member, exact-set rows for writes. No per-member write for plain members, so the portal's one-row-per-write rule does not multiply plain rows. |
| `/create-difficulty` | Six Opus 5.5 slots; corrected weighted average < 70 %; fewer than 5 full passes; population SD 0.10–0.30; ≥ 2 failure patterns with the largest ≤ 50 % of failing runs; ≤ 2 errored; ≥ 100 counted calls. | Two anchors from two causes plus at least four coin-flip records behind different retrieval habits. The spread gate is the binding one (§6.5). |

## 2. Fit census verdict and route

`Working_Files/00_Assignment_Fit.json` (written by `/create-goal`, bound to this assignment hash):

- **Verdict: `NO NATURAL COHORT`** (status WARN; the check is in warn mode). Base holds no closed, live collection
  of 40 or more for Marketing and GTM in Julia's view. Listed but not counted: `#zombie_marketing` (62 threads, open
  rule), Trello UA/BD (40 cards, dormant since 2025-03-18), `#company-website` (53 threads, dormant since 2023-11).
- **Limit: Gmail is thin** (9 threads in the 90 days before the clock; 11 sent, last sent 2024-04-17). No anchor
  and no coin-flip record goes in her mailbox: a search there returns so little that every run reads all of it.
- **Open population: yes.** The membership rule must be written as a closed rule and censused before any design
  rests on it (learnings §63).
- **Route: build the scenario by injection** (playbook S2x). Design backwards from the difficulty budget, let one
  injected record define the cohort with a closed rule, give every member its own records, and hide the deciding
  records in dense base containers Julia can read.
- **Earlier tasks for this persona, not to be reused:** `dd-q4-claims-register` (skipped), `julia_zm_difficulty_baseline`
  (110 ZOM tickets), `julia_zm3d_beta_calendar` (41 open ZOM issues; live-ops and push calendar), `julia_zm_audience_call`
  (82 friend-session tickets), `julia_dd_closeout`. Other personas' tasks in the same area: Samuel's beta push
  messages, Claire's Halloween art plan (ads and store art on ART tickets), Frederick's Q4 creative slate (§4).

## 3. Julia's reach at the clock

`persona_view.py reach julia_lawson --top 25`, trimmed to the lines that matter:

```
REACH  Julia Lawson <julia.lawson@harmonygames.co>  Product Manager / Product
clock 2025-10-01
SLACK  user=EMPLOYEE_0005_SLACK_ID  visible channels=147 {'mpim': 52, 'public': 23, 'private': 47, 'im': 25}  messages=238131
  persona posts=31848 last post=2025-09-30  last activity in visible channels=2025-10-01
GMAIL  mailbox=julia.lawson@harmonygames.co threads=253 messages=304 range=2023-07-16..2025-09-17
GCAL   own=['julia.lawson@harmonygames.co'] shared=[] events=748 (distinct ical_uid 253, cancelled 46)
DRIVE  owned=28 {...spreadsheet: 12, document: 10, folder: 2, presentation: 2, pdf: 2}
  shared-with=158   native visible: {'gdocs': 60, 'gsheets': 44, 'gslides': 10}  last modified visible=2025-09-30T16:30:39Z
UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence
```

Access proofs (`persona_view.py can-see julia_lawson …`, all run this session):

| Record | Verdict | Why it matters |
|---|---|---|
| `slack C08H78VJG80` (PlayableX vendor channel, private, 19 members, 198 messages, 2025-03-06 to 2025-09-30) | YES, member | hub of the recommended storyline; she can post there |
| `slack C090N54TG79` `#zombie-design` (2,709 messages) | YES, member | where the playable's content was argued |
| `slack C08R8CHB0QL` `#zombie-art` (2,650), `C09ATAJ220H` `#zm-animations` (246), `C0880U9751A` `#zombie-match3d` (16,250), `C08R27X0EAH` `#zombie-bugs` (3,830) | YES, member | dense base containers for off-path records |
| `slack C07C2866011` `#executives` | **NO** | the playable budget talk and the store-featuring post there are not evidence for her |
| `gdocs f_05bedd1540d3e01a90ab16` "Playable Feedback" (Leonard's, 2025-04-09) | YES, shared | base precedent for a playable document |
| `gdrive d_8140f09bf9f1b94cb8ee2d` (her root folder), `d_10809994aaf374642abff9` "Zombie Art" | YES, owner | write targets she owns |

**Her remit, from dated base records (the fit evidence):**

- She wrote the brief for the first playable. On 2025-03-14 she posted the finalized storyboard to the vendor
  (`C08H78VJG80/1741963515.221549`); the vendor thanked her "for this detailed brief" (`…/1742063341.276529`); she sent
  the asset pack on 2025-03-18 (`…/1742315789.059509`) and handled the sound question (`…/1743772445.340109`).
- For the second playable she was asked for the reference level: Brian, 2025-09-22, "could you prepare a test level
  as a reference for both the Playable team and myself?" (`C090N54TG79/1758568735.563539`); she answered "Yep, I'll make
  your level ASAP" (`…/1758568988.777449`).
- The Confluence design page names her: `page_zm3d_gdd` v2 (updated 2025-09-30T17:00Z) ends "Owner: Robert (Product).
  Design: Julia Lawson."

Identities used below: `EMPLOYEE_0005` Julia, `0008` Frederick Stone, `0016` Robert, `0026` Brian Foster, `0038`
Leonard Hayes, `0012` Vincent Parker, `0009` Claire Morgan (the last two resolved with `entity.py`). The vendor's
product manager is `PERSON_6078_SLACK_ID`: `entity.py` finds no email and no record in any other service, so the
vendor is reachable only in the shared Slack channel.

## 4. Storylines

Frederick's task (`task_inputs-uselater`, `frederick_q4_ua_vendor_plan`) ended as a Q4 creative slate: Leonard's
`#executives` post, a call on each cut of the video refresh, 44 seeded ART tickets under ZOM-467. Its SQL has no
record in the PlayableX channel (0 hits for `C08H78VJG80`, 0 for "playable"). The three storylines below differ
from it in requester, artifact, vendor and cohort.

### A. Content brief for the Zombie Match 3D playable ad (recommended)

**What the base says (all read):**

- 2025-08-26: Leonard opens the second playable with the vendor (`C08H78VJG80/1756223629.429589`) and asks them to
  play to level 40 (`…/1756223785.608099`).
- 2025-09-15: Frederick picks Scenario 1 and names the open design questions: which items are on the board and
  which enemies are hit (`…/1757956024.883249`). 2025-09-16: the vendor offers editable items "aside from the 8-item
  set that you will provide" and a 29 Sep start (`…/1758022459.227279`).
- 2025-09-19: the vendor lists the assets it expects, by group (`…/1758283671.878269`). 2025-09-22: Brian says the
  item and enemy choice must be finalized on the design side first (`…/1758552921.729409`).
- 2025-09-24 to 09-29: the start slips to 6 Oct for late assets (`…/1758701898.919999`); a pack goes out and comes
  back as incomplete (`…/1758808234.045839`); a second pack follows (`…/1758906043.375719`); the vendor says it will
  re-rig the characters in its own pipeline (`…/1759140968.965099`).
- 2025-09-29 19:42 UTC: Frederick pauses development "for a month or so" because a change to the core game is
  being considered (`…/1759174925.309129`). 2025-09-30 09:59 UTC: the vendor sets the new start for 3 November
  (`…/1759226395.551469`). No Slack message says "playable" after Frederick's pause post: none in any September file
  after it, none in any October file.

**The job.** While development is paused, Julia writes the content brief the vendor needs on 3 November, for the
game as it stands in the beta build: the default board items for the reference level, the pool of items the vendor
makes editable, the design line for each (what it does to enemies, as shipped), the non-item assets (sound,
interface, background), and what Harmony Games still owes. That is the gap the base records name as the cause of
two slipped starts. A planned message from Frederick on Tuesday 30 Sep (after the vendor's 09:59 UTC reply, before
the seed bound) asks her for it.

**Fit.** Product and design: gameplay and design requirements for a prototype, product decisions on what the ad
shows, evaluation of art and of the vendor's scenario. Marketing and GTM: a playable is a user-acquisition
creative. Authoring: the deliverable is a document and a sheet, with the messages that send them. The base shows
her doing exactly this in March 2025.

**Natural services before injection:** Slack, Confluence (the design page: 7-slot tray, win and fail rules),
Docs (Playable Feedback), Drive, Trello (card `688c4d14c312a27fa2747e40` "Playable Kickoff", open, last activity
2025-09-13), GitHub (match3d), Sheets. Injection adds Linear, Calendar and Contacts to reach ten or more.
Snowflake and Confluence cannot be injected; Gmail carries nothing that decides a row.

**Weak points.** (1) The pause: the brief must be scoped to the current build, and nothing in it may depend on the
undecided change (§8). (2) The base item roster is real but Julia's access to it is unverified, and it is a July
snapshot (§7). (3) The product's name contains a word the theme screen lists (§8).

### B. Store page brief for the beta (alternate)

Julia writes what the App Store and Google Play pages show and say for the beta build: screenshot list, feature
lines, what was descoped. Base hooks: Axe Arena descoped on 2025-09-22 (`C090N54TG79/1758517286.431379`); footprint and
store conversion (`C08R27X0EAH`, September). Weaker than A: the store-asset update and the Google Play Indie
featuring application sit in `#executives`, which Julia cannot read; it sits close to the skipped claims register
(same persona) and to Claire's store art; the natural cohort is about a dozen claims, so it would also need a
cohort exception.

### C. Domino Delights product sheet for a publisher (alternate)

Julia writes the product sheet a publisher needs to evaluate Domino Delights, starting from the lead she raised
herself on 2025-06-03 (Tamatem, MENA; `C48D58CD7FBD/1748974617.722599`) and Leonard's line that the game will grow
"with a publisher or organically" (`C08H78VJG80/1756223629.429589`). It avoids the listed theme word. Weaker than A:
the fit leans toward founder and business-development work; the publisher canvass in the Atlas is post-cut and
does not exist on synth-cut, so reviewers may read the premise as borrowed from it; the evidence ("what is live in
Domino Delights") is the ground her claims register and close-out tasks already covered, including the Season
Pass conflict (learnings §3).

**Rejected:** a gameplay-capture brief for UA videos (base precedent `f_b5fb884dc96261846b6c2c`, 2024) is too close
to Frederick's video cuts; a push or live-ops calendar repeats Samuel's and Julia's own tasks.

**Recommendation: A.** It is the only one whose requester, vendor thread and prior deliverable are all in base
records that name Julia, and its hub channel has no record from any earlier task.

## 5. UGT plan (storyline A)

**Deliverables.** A brief (Google Doc) and an asset hand-off list (Google Sheet), both created in Julia's own
Drive; tickets for the assets still owed; a reply to Frederick with the counts he asked for; a note to the vendor
in the shared channel with the link and the outstanding list. Each write is asked for in Frederick's message; the
vendor has no other reachable address (§3).

| Content | Fixed by |
|---|---|
| Scenario and mechanic count | base: Frederick's choice (`…/1757956024.883249`); the vendor's limit from March (`…/1741705164.913899`) |
| Default board items (eight) | planned decision record in `#zombie-design`, as amended by a later reply elsewhere |
| Editable pool: which items are in | one planned rule sentence from Frederick with closed clauses (in the named build, art signed off, met by a stated level), applied to every candidate |
| Design line per item | the item's own ticket, as amended by the review of its change |
| Hand-off state per asset | Brian's planned tracker, the vendor's replies, the art lead's word |
| Format owed for 3D assets, sound rules | base: the vendor's March rules (`…/1742892985.601399`, `…/1742899453.589669`, `…/1744059855.381899`) |
| Tray size, win and fail | base: `page_zm3d_gdd` (7 slots; loss only at zero health) and Brian's 2025-09-24 statement (`…/1758717625.209649`); the 6-slot proposal in the page comments is settled on the page ("keep the GDD at 7") |
| Start date | base: 3 November (`…/1759226395.551469`) |
| Counts in the reply | the corrected pool and owed sets, nothing else |

**Rules I will hold the design to:**

1. Before SQL, a table of every rule clause against every member, with the record that states each clause. Any
   member where two clauses disagree is fixed in the data (learnings §21, §63, §80).
2. "The beta build" is one named build in one planned record. The beta date itself is never graded (card SC-13).
3. Completeness is claimed only for the closed cohort (the tracker's rows plus the members the rule adds), after a
   census. Frederick's message scopes the rest out in his own words.
4. Free-text parts of the brief are bounded: the rubric accepts any wording that states the recorded facts.
5. Nothing in the brief depends on the undecided change to the core game. Frederick's message says the brief is
   for the current build; the base supports that reading (Robert, `C090N54TG79/1758569655.409719`).
6. The enemy roster and boss rules are not graded (card SC-58). Enemies appear in the brief only as the content of
   the reference level, fixed by a planned record; S1 decides whether even that row stays.

## 6. Hardness plan (storyline A)

### 6.1 Loss channels

Seven channels on separate rows; the largest carries 17 % of the sketch weight. Each names the convincing wrong
source and the record that beats it. The trap names are the guide's Part 3 types.

| Channel | Guide trap | Convincing wrong source | Record that beats it (author, authority, date order) | Carrier (measured opened/runs) |
|---|---|---|---|---|
| **BUILD** (anchor) | 1 · proving done across services | Brian's tracker marks the item "in build"; its ticket is Done | a comment by the engineer who owns the build, on the beta memory ticket (not an item ticket), listing item models taken out of that build; dated after the tracker | ticket outside the set, 6/33 |
| **ARTFIX** (anchor) | 2 · a correction somewhere else | the art ticket reads final; the tracker says sent | a later direct message from the art lead (Claire) to Julia withdrawing sign-off for one item family | DM with someone who does not own the rule, 6/46 |
| **ABIL** | 2 · correction in a review | the item ticket's description of its effect; the linked pull request is merged | an inline review comment on that pull request recording the effect as shipped | inline PR review comment, 21/51 |
| **ALIAS** | 6 · different names for the same thing | tracker says sent; a search for the item's name in the vendor channel finds no objection | the vendor's acceptance note uses its own labels (base precedent: the vendor's "duck asset", `…/1758723504.085039`, against the roster's "Plushie Chick"); a second record maps labels to items | alias, 15/28 |
| **SWAP** | 2 · a correction somewhere else | the default set in the design-channel decision | Robert's later reply under another post in `#zombie-art`, naming both items | reply under an unrelated parent that names the item, 16/26 |
| **LATE** | 7 · items outside the obvious filter | the tracker's shortlist tab is the candidate list | Frederick's rule covers every item met by a stated level; the level list places a class of items there that the shortlist tab does not carry | outside the obvious filter, 12/21 |
| **AUDIO** | 5 · a rule hidden in the data | the tracker lists the sound cues as ready; in March sounds were zipped and sent as they were | a root post in `#zombie-sfx` (`C09A7PDFYCV`, a channel the ask does not name) saying which cues may leave the studio | root post in a channel nothing names, 8/13 |
| FMT (not budgeted) | 5 · exception in older records | the September asset list names no format | base: the vendor's March 2025 rules, on the older page of the same channel | old base record nothing points to, 0/14 on one task |

Two further guide traps are used without budget weight: trap 8 (the counts in the reply change with their inputs;
graded as the corrected input and the final figure) and trap 9 (some owed assets already have an open ticket, so
the write is "tickets for exactly the owed assets").

Checks against the never-live patterns (learnings §28, §45, §52, §79), to be proven on the SQL: no deciding record
sits in the hub thread, in Frederick's ask or in the container of the record it corrects; no bulk listing carries
the answer; Frederick's message names the job and the destinations, not where the rules are; each off-path text
keeps the rule's meaning without its keywords; plain members sit beside every exception, so finding a comment does
not mark a trap.

### 6.2 Part 7 self-checks

`python3 -B Task_Authoring/tools/hardness_v2_check.py --design --task-dir Task_Authoring/task_inputs --manifest
Working_Files/00_PreScenario/sketch_manifest.json --surface Working_Files/00_PreScenario/sketch_surface.json`, verbatim:

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      3 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 4 requirements: {'R2': ['BUILD', 'LATE'], 'R5': ['ARTFIX', 'ALIAS'], 'R4': ['ABIL'], 'R3': ['AUDIO']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   8 of 8 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     2 weight-5 total(s); 2 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Dispositions. SAME_PLACE is clean only over the containers the sketch declares; it is re-run on the draft manifest
at S5b and on the SQL. RULE_IN_PROMPT runs once the prompt exists. The run is a sketch: it shows the shape can
clear the checks, not that the records do.

### 6.3 Difficulty budget on the sketch

An **anchor** is a deciding record the model almost never opens; a **coin-flip** record is one about half the
runs open. `difficulty_budget.py check` on the sketch (`00_PreScenario/sketch_budget_basis`), blocking lines all
PASS, verbatim extract:

```
DIFFICULTY BUDGET (hard): WARN
[PASS] budget.anchors: 2 anchors from 2 causes carry 32.8% (needs 32.0%); largest cause 16.4%; highest find rate 0.20.
[PASS] budget.variance: 5 independent coin-flip habits, every find-rate range inside 0.35-0.65 (needs 4).
[PASS] budget.average: P(six-run average strictly under 70.0%) is 1.000 with every unit at its low find rate and 0.993 at its high find rate (needs 0.90 at both).
[PASS] budget.full_passes: P(fewer than 5 full passes) is 1.000 with every unit at its low find rate and 1.000 at its high find rate (needs 0.90 at both).
[PASS] budget.signature: P(largest signature at most 50% of failing runs, two or more signatures) is 0.999 with every unit at its low find rate and 0.999 at its high find rate (needs 0.90 at both).
[PASS] budget.signature_one_error: P(signature gate with 5 completed runs) is 0.986 with every unit at its low find rate and 0.992 at its high find rate (needs 0.90 at both).
[WARN] budget.spread: P(SD inside 0.1-0.3) is 0.579 / 0.698 / 0.733 at the low / middle / high find rates; the design carries 46.0% of weight on coin-flip (variance) units and 32.8% on anchors. Below 0.70: a spread miss is likely; move more weight onto coin-flip units (about 60% of weight reaches 0.8) or accept that the miss is reported.
[WARN] budget.hard_mode: Hard mode: the 30.0% loss figure is 1 - cap, not a line from a platform /hardness report, so the anchor share target is unverified.
```

The full output and the unit table are in `00_PreScenario/difficulty_budget_check_output.txt` and
`difficulty_budget_table.md`.

| Unit | Role | Members in the sketch | Habit that finds it | Find rate used | Share of weight |
|---|---|---|---|---|---|
| A1 BUILD | anchor | 10 items | Linear, comments on a ticket outside the set | 0.05–0.20 | 16.4 % |
| A2 ARTFIX | anchor | 10 items | Slack, reading a DM | 0.05–0.20 | 16.4 % |
| C1 ABIL | coin flip | 7 items | GitHub, inline review comments | 0.35–0.60 | 9.2 % |
| C2 ALIAS | coin flip | 8 items | Slack, search under another name | 0.40–0.65 | 10.5 % |
| C3 SWAP | coin flip | 2 items, 2 brief rows | Slack, opening a thread | 0.40–0.65 | 3.0 % |
| C4 LATE | coin flip | 8 items | Sheets, a second list | 0.40–0.65 | 17.1 % |
| C5 AUDIO | coin flip | 3 sound cues | Slack, reading a channel nothing names | 0.40–0.65 | 6.2 % |

### 6.4 Whole policies and single misses on the sketch (UNCALIBRATED)

`00_PreScenario/policy_scores.py`, verbatim. The find rates are ranges from `references/carrier_find_rates.json`
(104 units over 11 archived tasks); they are not measurements of this task.

```
SKETCH surface: 141 rows, total weight 609  (UNCALIBRATED)

Whole policies (rows failed = rows of every unit the policy never opens):
  100.0 %  P0 reads everything
   17.4 %  P1 hub, shortlist and item tickets only (no comments on other tickets, no DMs, no PR reviews, no other channels)
   37.1 %  P2 P1 + pull-request reviews and vendor-channel search
   55.5 %  P3 P1 + every thread and channel the ask's people post in (no DMs, no off-set tickets)
   64.7 %  P4 everything except the two anchor records
   51.6 %  P5 both anchors found, every coin-flip record missed

Single misses (everything else found):
   82.8 %  miss A1 (BUILD, non_set_ticket)
   81.1 %  miss A2 (ARTFIX, dm_with_non_owner)
   90.8 %  miss C1 (ABIL, inline_pr_review_comment)
   87.8 %  miss C2 (ALIAS, alias)
   97.0 %  miss C3 (SWAP, reply_under_unrelated_parent)
   82.1 %  miss C4 (LATE, outside_obvious_filter)
   93.8 %  miss C5 (AUDIO, root_post_in_unnamed_channel)
   97.9 %  miss R1 (FMT, realism: old base vendor rules)

Six-run simulation, 20,000 trials per setting:
  setting   E[avg]   P(avg<70)  P(<5 full)  P(SD band)  P(patterns)  P(ALL GATES)   mean SD
  low find   32.2 %   1.000      1.000       0.579       0.999        0.579        0.108
  midpoint   42.2 %   1.000      1.000       0.698       1.000        0.698        0.122
  high find  52.4 %   0.998      1.000       0.733       1.000        0.732        0.127
```

Reading it:

- **E[average] is 32–52 %**, under the 62 % target at every setting. **P(all gates) is 0.58–0.73**, over the 0.5
  target at every setting.
- **The spread gate is the binding one.** The mean six-run SD is 0.11–0.13, just above the 0.10 edge. The anchors
  lower the average but add little spread; the coin-flip weight does that. An earlier sketch (37.5 % anchors,
  40.5 % coin-flip) gave P(all gates) 0.43 at the low end and was rejected for it.
- **No single miss clears the cap.** A run that misses only one record scores 81–98 %. The average stays under
  70 % only when a run misses both anchors, or one anchor and several coin-flip records. That matches how the
  archived runs lost points, but it is the main risk and it is stated here rather than averaged away.
- **The average has room.** If S1 cannot ground this many exception members honestly, the design can give up 10
  points and still meet 62 %; it cannot give up coin-flip weight without failing the spread target.

### 6.5 Row shape the numbers assume

The sketch grades plain members by sample (five per group and a volume row) and gives each singled-out member a
direct pair of rows: its call (in the default set, in the pool, or out) and its hand-off state. Both are weight 5
by kind of work, because each joins the tracker, the member's ticket and a third record; no weight is raised for a
trap. Exception members are 48 of about 72. If the portal instead requires a row per plain member, the anchor share
falls below 32 % and the budget fails; that is why plain members get no write of their own. `/create-scenario`
repeats the budget on the planned rubric rows (`weight_basis: skeleton`), not only on the surface.

## 7. Volume plan (storyline A)

**Cohort.** Every asset line of the playable pack: board items (the tracker's shortlist plus the class the rule
adds), and the non-item lines the vendor's list names (sound cues, interface elements, background, launcher,
projectile). About 72 members in the sketch (60 items and about 12 non-item lines). The rule is closed and one planned record (Brian's tracker, with
Frederick's rule sentence) defines it.

**The base roster (read).** Robert's sheet "ExportedLevelItems First Appearence" (`f_7efae6c05be5c2414e8798`,
modified 2025-07-23) lists 151 distinct board objects with the level each first appears in, over 74 levels
(`PR_0001FTUE` to `PR_0101`); 83 objects first appear in levels numbered 40 or lower. Its second block lists 170
sized variants with quantities ("Plushie Chick Medium", "Dutch Oven Medium"). Brian's "ExportedLevelItems"
(`f_e4926ec5851a82d7909e6b`, 2025-07-15) is the fuller export. Three consequences:

- Every cohort member takes a real base object name. No name is invented, and 83 candidates by level 40 is more
  than the sketch's 60, so no cohort exception is needed.
- Both sheets are shared by domain only, so `can-see` returns UNVERIFIED for Julia and they are not reach. The
  roster reaches her through a planned record (Brian's tracker), which must agree with these sheets on every name.
- They are a July snapshot. The level order changed on 2025-09-29 (`C090N54TG79/1759171957.791499`, "17 -> level 5 …
  everything else moves up"). Any "met by level N" fact comes from the task's own dated list; where that list
  differs from the July export, a base event must explain the difference.

**Per-member surfaces** (three, over two services, none with a bulk call): the member's ticket comments in Linear;
the review comments of the pull request that changed it, where one exists; the member's row in the vendor's
acceptance record. Base Linear has no comments and no ticket about the playable ad (the twelve hits for
"playable" fall on ten ENG tickets from 2023–2024 about an unplayable or offline-playable game), so seeded tickets
and comments stand alone. To stay clear of Frederick's
and Claire's cohorts, member tickets are not ART tickets under ZOM-467.

**Provisional necessary calls** (a desk estimate; S2's shortcut audit replaces it):

| Phase | Calls |
|---|---|
| Discovery (ask, vendor channel both pages, design threads, Drive, Trello card, calendar) | 30–40 |
| Rules (vendor's March rules, the rule sentence, design page, Playable Feedback) | 10–15 |
| Enumeration (tracker tabs, ticket listing, level list) | 10–15 |
| Per member (about 70 × comments, plus about 20 pull requests × 2) | 110–190 |
| Reconciliation (DMs, art, sound and animation channels, build posts) | 25–35 |
| Reads before writes | 8–12 |
| Writes and read-back (doc, sheet, 15–25 tickets, two messages, sharing) | 30–50 |
| **Total** | **about 225–355** |

Five hundred necessary calls are not reachable here without padding: a list call returns ticket descriptions in
bulk, so only comments and reviews are honestly per-member, and doubling the cohort would mean inventing members.

## 8. Hazards to carry into `/create-scenario`

| Hazard | Source | Disposition |
|---|---|---|
| The playable is paused and a core-game change is undecided | `C08H78VJG80/1759174925.309129`; Leonard's options, `C090N54TG79/1758517286.431379` | The brief is for the current build and for the 3 November start. No row depends on which option is chosen. S1 reads every record from 2025-09-29 to the 07:00 UTC data horizon in the six channels above, not by keyword (learnings §65). |
| Why write the brief during a pause | I listed every Slack message from 27 Sep on that says "playable", in all conversations. The last are 29 Sep: Leonard expects a change and does not want the vendor's work wasted (`CADCE44A365D/1759171993.180879`, `…/1759172018.976319`); Brian says a playable of the game "in its current form" would not be needed after a change (`D076PSEBC4D/1759171889.924089`), and that the vendor's optimizations of the animations, panels and objects would carry over (`CADCE44A365D/1759172311.343939`). Julia is in neither conversation (`can-see` NO for both). | Frederick's planned message must agree with these: it asks for what holds up the 3 November start and carries over, and it does not claim the playable will ship as specified. This is the storyline's main coherence risk; if S1 cannot word the ask so that it agrees with all four lines, switch to B or C before any SQL. |
| Beta date | card SC-13 (13 FAILs) | Not graded; the build is named by a planned record. |
| Enemy roster and boss rules | card SC-58 | Not graded (§5 rule 6). This replaced an enemy-based unit in the first sketch. |
| Season Pass ship date; glass crash fixed or not | cards SC-38, SC-8 (both stated on `page_zm3d_gdd`) | Those sentences of the page are not touched or cited. |
| Linear status as proof of shipping | card SC-16 (ZOM-564, ZOM-513/514, ZOM-563, ART-790/792) | Those tickets stay out; the done-gap uses seeded tickets. |
| Product name on the theme screen | playbook S0; `Hardness_Mastery.md` §12 ("suspected, not proven") | The name cannot be avoided for this game and recent tasks on it ran on Opus 5.5. No seeded text uses infection or outbreak vocabulary, and the pre-check is read for model-fallback events. Storyline C is the fallback if a fallback event appears. |
| `#executives` is closed to Julia | `can-see` NO | Nothing the task needs may live only there. |
| Vendor replies after the pause | none in base after 2025-09-30 09:59 UTC | Planned vendor posts are dated between that reply and the seed bound, or before the pause. |
| Injected Confluence and Snowflake | not writable | Both carry weight through base content only. |

## 9. My decisions

1. **Storyline: A**, the content brief for the Zombie Match 3D playable ad, requested by Frederick on Tuesday 30
   Sep, for the vendor's 3 November start. B and C stay as fallbacks in that order of preference for fit; C first
   if the theme screen bites.
2. **Volume exception: yes, and it needs your confirmation** (GEN_EXECUTION §3a; the manifest field
   `requester_confirmation` must quote you). Proposed floors: `call_budget_floor` 220 and `per_record_floor` 110,
   in place of 500 and 300. Reason: about 70 source-defined members with two honest per-member reads give about
   225–355 necessary calls; more would be padding. Every other extreme target still applies. The platform floor is
   100 counted calls; the design aims for at least 130 in every run. If S2's audit lands lower than 220, I will
   come back with the audited number instead of adding calls.

   **Requester confirmation, received in this session on 2026-11-11, verbatim:** "220 calls are good with required
   failure". It reached me appended to a stop-hook message, not as a separate chat message. It names the call floor
   of 220. It does not name the per-record floor of 110, so that number is still unconfirmed. My reading, not the
   requester's words: "with required failure" makes the exception conditional on the task still failing the model
   as the Hard gates require.
3. **Cohort exception: not needed.** The base roster supports 83 named candidates by level 40 (§7).
4. **Review waiver: none requested.** `REDTEAM_*` is not set in this session, so the dual red team cannot run as
   things stand. Either configure it before S9, or I record `RED TEAM UNAVAILABLE` with a fallback: two cold
   reviewers with no design context, one briefed as the platform's static injection reviewer and one as the
   `/prompt` fork and coherence reviewer, plus the cold-solver rehearsal S2x already requires. In that case "no
   review by a second model family" stays on the Unresolved line until the pre-check covers it.
5. **Spread target.** I accept a design whose spread chance is about 0.6–0.7 rather than the tool's 0.8, because
   reaching 0.8 needs about 60 % of the weight on coin-flip records on top of 32 % on anchors, which leaves no
   plain work. If the six runs pass every gate except spread, that is reported to you, not repaired by a revision
   (owner decision of 2026-11-10).
6. **Carried forward:** the requester's message stays to the ask and its destinations; Julia owns both Drive
   targets and the pre-check confirms each write returns ok; every rubric row is costed on the portal's row shape
   before SQL; the builder export is diffed against `09_Rubrics.json` before the verifier runs.

## 9a. Requester requirements and delegated choices (2026-11-11)

Stated by the requester in chat after the first draft, verbatim: "my task is a long horizon task soo i want over
130+ tool calls in each runs and also i want difficulty pass rate under 70% and also have to folllow all other
difficulty guidelines soo you can choose from your self which option is best fit for my requirements in this task."

| Requirement | Target the design is held to |
|---|---|
| More than 130 counted calls in every run | A lean correct path of at least 190 calls, so the lowest of six runs stays over 130 (§9b, lesson G) |
| Corrected weighted average under 70 % | Design to E[average] ≤ 62 % |
| Every other difficulty gate | Fewer than 5 full passes; population SD 0.10–0.30; two or more failure patterns, the largest at most half of the failing runs; at most 2 errored runs |

Choices the requester left to me, made here:

- **Per-record floor: 110**, beside the confirmed 220-call floor. About 95 members with at least one read each
  that no bulk call replaces gives 110 or more; S2's audit replaces the number if it comes out lower.
- **Independent review: the recorded fallback.** `REDTEAM_*` is not set, so `/create-scenario` records
  `RED TEAM UNAVAILABLE` and uses two cold reviewers with no design context (one as the static injection reviewer,
  one as the `/prompt` fork and coherence reviewer) plus the cold-solver rehearsal. "No review by a second model
  family" stays on the Unresolved line until the pre-check covers it.
- **Storyline: A**, unchanged.

## 9b. Lessons from the completed tasks, and what each changes here

Read from every `README.md` under `support/completed_tasks/` (19 folders; Julia's four in full). The numbers are the
archived baselines.

**What the baselines show about the gates.** Eighteen tasks have a six-run baseline. Five reached a population SD
of 0.10 or more: Julia's audience call (0.177), Frederick's account handover (0.161), Douglas's server sign-off
(0.117), Frederick's bridge pipeline (0.106) and Robert's LLC takeover (0.103). The other thirteen sat between
0.016 and 0.099. Four averaged under 70 %: Douglas 56.3 %, Claire 64.1 %, Calvin 64.4 % and Julia's close-out 69.7 %.
Only Douglas's did both, on 163–238 calls per run. It is the model for this task.

| # | Lesson (source task) | What it changes in this design |
|---|---|---|
| A | A cluster no run finds lowers the average and removes the spread: Claire 25.3 % of weight on two unread records, SD 0.033; Samuel 23.5 %, SD 0.060; Frederick's Q4 commitments five de-named records, SD 0.016. | The two anchors stay at the policy minimum (about 16 % each) and no single cause goes above 20 %. Each anchor gets one route a few runs take, so its find rate is about 0.15 and not zero. |
| B | Spread came from records about half the runs open, on rows of their own: a thread reply (Calvin 3 of 6; Julia's close-out 4 of 6), a later message from the same person that contradicts their earlier record (Julia's audience call, missed by 4 of 6), a "done" claim against a base note in another service with both on the read path (Arthur, 3 of 6), a pull-request body (Calvin, missed by 2 of 6), a payee under another name (Robert's seed bets, 23–77 %). | Coin-flip units use these carriers. At least 45 % of the weight sits on them, the largest unit at 15 % or more. |
| C | Inline pull-request review comments are not a coin flip. Every run missed them in Douglas's and Calvin's tasks, and five of six in Julia's close-out (the measured table agrees: 0 of 26 when the pull request is not linked from the item, 12 of 13 when it is). A seeded review comment also needs a real diff hunk of that pull request (Calvin, `/prompt` NON-FAIL 3). | The ABIL unit moves off an inline review comment. Its deciding text goes in the pull request's description or a thread reply; the sketch's "inline PR review comment, 0.35–0.60" row is superseded and S5c re-runs the budget. No seeded inline review. |
| D | A requester message or hand-over note that points at each rule leaks all of them: Julia's audience call rev 6 (`/hardness` FAIL 1), Calvin rev 1 (FAIL 2). | Frederick's message holds the ask and the destinations. Each rule sits in one deciding record elsewhere, in plain definitions. |
| E | Misses must move the headline numbers. On Calvin's rev 2 two swaps cancelled and every run reported the right totals (about 79 %). | Every unit moves a count in the reply in one direction; no pair of units cancels in the pool count or the owed count. |
| F | Per-target rows for members every run gets right raise the average and flatten the spread: Douglas (three rounds of wrong projections), Robert's LLC takeover (73 to 130 rows, 76 % to 83.6 %), Calvin (121 to 184 rows). The portal still requires one row per target for writes and per fact in a requested list. | Plain members get no write of their own. Tickets change only where a member's state changes. The budget is costed on that per-target shape before SQL. |
| G | Runs clear 130 calls when the work has per-target writes and per-record reads: Claire 211–237 (58 comments, 48 assignments), Owen 230–326, Leonard 203–251, Samuel 175–193, Douglas 163–238, Robert's LLC takeover 149–162, Calvin 138–189. They fall short without them: Arthur 78–95, Robert's seed bets 116–140, Frederick's bridge 109–150; Julia's beta calendar forecast under 5 % for "every run at 130+" on a 154-call budget with four write kinds. | The cohort is the full closed set, about 95 members (83 base objects by level 40 plus the vendor's non-item lines), each with a comment read that fills a required column of the hand-off sheet. At least 25 ticket writes are ones every run makes (members the tracker itself shows as owed). The pre-check is read against 150 calls; under that, the design is revised before any baseline. |
| H | An open set cannot be patched item by item (Julia's beta calendar: fourteen revisions, no `/prompt` pass). A clause no answer depends on is a fork. A passed dimension is not clearance. Cold reviewers find what resumed ones do not. Keyword searches miss records a channel census finds. | Closed rule with a cutoff from the start; every rule clause traced to a truth value; whole-channel census from 2025-09-22 to the data horizon; cold reviewers only; after a second `/prompt` failure in one family the rule changes, not the items. |
| I | A collective label is a fork ("the friend sessions", `/prompt` FAIL 2). A rule the answer relies on must be stated in a record. | "The pool", "the beta build", "owed" and "sent" are each defined in one record, and the sweep in §5 rule 1 covers them. |
| J | Judgement traps did not land (Julia's difficulty baseline: 28 or more runs; Pacific-time conversion met by every run). Only hard-to-reach records separated runs. | No budget weight on judgement, dates or time zones. |
| K | A correct answer no run can reach is a defect, not difficulty (Arthur: a group-DM hand-over, 0 of 6, one row). A Slack DM thread reply was unreachable through the tool in Julia's difficulty baseline. | Each anchor is a top-level message or comment the agent's tools return, reached by a natural step, and proven in the cold-solver rehearsal. No weight-5 fact sits on a single row. |
| L | Moving a record to a quieter place is not harder if the search runs make still finds it (Arthur: three of five moves had no effect; an app-name mail search found them). Wording must be tested against the runs' own search terms (Julia's close-out). | Each off-path text is checked against a name search and a recent-window search on the SQL, and keeps the rule's meaning without its keywords. |
| M | Rubric shape the portal enforced: no count bundles, no multi-target writes, a guard as one bare count, labels defined inside each title, accepted name forms in the title; copy a Fix List word for word; diff the builder paste field by field (two wrong weights moved Frederick's SD from 0.106 to 0.098). | Carried to the rubric stage unchanged. |
| N | Bind verifier runs to trajectories by content; take all-fail rows from `difficulty_stats.py`; write all-fail narratives from each run's write payload. | Carried to the baseline stage unchanged. |
| O | A second draw on unchanged inputs is legitimate when one pattern dominates, if it is disclosed as that (Julia's close-out). | Available as a last step, never as a design substitute. |

## 10. Files written by this analysis

All under `Working_Files/00_PreScenario/`. They are sketches for the tool runs above and are not stage artifacts.

| File | Purpose |
|---|---|
| `build_sketch.py` | generates the sketch surface and budget |
| `sketch_surface.json` (sha256 cc71f428f203…), `sketch_budget.json` (20cb83a69e63…), `sketch_manifest.json` (f16626784ea9…) | inputs to the tool runs |
| `sketch_budget_basis/` | a copy of the assignment plus the sketch surface and budget, so `difficulty_budget.py` can resolve its weight basis; not a task folder |
| `difficulty_budget_check_output.txt`, `difficulty_budget_table.md`, `hardness_v2_check_output.txt` | tool output, unchanged |
| `policy_scores.py`, `policy_scores_output.txt` | whole-policy and single-miss scores and the six-run simulation |

Checked after the first draft, all read:

- **Vendor channel by month:** March 76 messages (43 top-level), April 43 (30), June 3, August 50 (49), September
  26 (6); 198 in all. The 100 newest reach into April, so the March rules sit past a first page. Whether channel
  history returns thread replies is a tool behaviour I could not test here, which is why FMT carries no budget weight.
- **`#zombie-sfx`:** 66 messages, 2025-08-13 to 08-18, posted by Robert (36), `EMPLOYEE_0006` (25), Julia (3),
  Leonard (1) and `EMPLOYEE_0002` (1). A planned post there in late September would be its first in six weeks; S1
  resolves `EMPLOYEE_0006` and decides whether that is natural or the unit moves to another channel.
- **"Playable Feedback":** 1,290 characters of P0, P1 and P2 feedback on the first playable. It is a precedent for
  a playable document, and holds no rule this task needs.

Still not verified: every find rate (ranges from archived tasks, never measured on this task); whether Julia can be
given the two export sheets by a share; the identity and status of `EMPLOYEE_0006`.

---

**Next step: run `/create-scenario`.**

# Pre-scenario analysis: Frederick Stone · bridge-round investor pipeline (analysis only)

Contains no prompt, Oracle Event or criterion text. Written 2026-11-01 for `/create-scenario`.
Probabilistic numbers are labelled **UNCALIBRATED**: they are design aids, not measured rates (learnings §9).

## 0. Assignment and context (verified)

| Field | Value |
|---|---|
| Persona | Frederick Stone, Co-founder, `frederick.stone@harmonygames.co` (roster `frederick_stone`) |
| Business function / competency / skill | Executive · Corporate Ops · Retrieval |
| Horizon / mode | Long Horizon (`effective_profile: extreme` under GEN §3a) · **medium** (cap: corrected weighted average < 85 %; design target E[avg] ≤ 77 %) |
| Universe | `synthcut`, hg4-synth-sep30cut v16, clock 2025-10-01 07:00Z (00:00 PT), seed bound `freeze_utc` 2025-10-01T00:00:00Z, shutdown rules do not apply |
| Persona today | Wednesday, October 1, 2025; "yesterday" is Tue Sep 30 |
| Source | `task_context.py --write --require-source`: status `ready`, KB `bound` (`references/universe_kb/by_universe/synthcut`), context_hash `f1f763cb8cb4…` |
| Evals input store | Not touched (goal instruction; learnings §37). Read through `Task_Authoring/tools/hg.py` and read-only Python over the synth-cut exports only |

**Originality constraint.** Frederick already has two submitted synth-cut tasks
(`support/completed_tasks/`): the Q3 card-spend breakdown (Finance-flavoured, investor reporting) and the
marketing/UA account handover (Corporate Ops, Leonard DM `D05S58U4SAK`, Trello UA/BD board). The new task must not
reuse either cohort, the card or ad-account vocabulary, the DM destination or the UA/BD board.

## 1. What a 5 needs at each gate

| Gate | What scores 5 / passes | Specific risks for this persona and universe |
|---|---|---|
| `/injection` (Checks A/B/C) | No seeded fact contradicts any base record anywhere in the universe; every seed is dated after the base events it relies on; schema/ID contracts; no timestamp after 2025-10-01T00:00Z (local `sql_lint` seed bound); companions (thread snippets, GCal per-attendee copies, Drive-family sharing mirrors) | Investor firms, partners and amounts recur across Leonard's mailbox, `#bridge-pitch`, `#executives`, the Game Investor List and DocSend mail. Every seeded firm, person token and amount needs a whole-universe census (learnings §10, §12, §14), not only Frederick's view. The "15 % chance to raise" (#bridge-pitch `1758767624.533779`) and "$225K in the bank" (`1757548092.670219`) lines bound any seeded commitment: keep seeded amounts small and framed as soft or verbal |
| `/prompt` | Assignment fit (Founders/Exec + Corporate Ops), UGT, feasibility, cross-service coherence, natural voice, originality, no rules or traps in the prompt | Role field: Contacts lists Frederick as "Commercial Lead, Marketing & BD" (`/contacts` `175c0d7bc72ed244b944cb90`) while the roster says Co-founder. Fundraising and board prep are plausible for both titles: he is on every investor cc, in `#bridge-pitch`, and invited to the Oct 14 board (`evt_bd61f3209523d19fdd6ba2`). Relative dates are computed against Wed Oct 1 (learnings §20) |
| `/hardness` (pre-check, single run) | PROCEED (3–5): the pre-check must miss weight-5 rows for real reasons | dd-2024 and Robert rev 6 scored 1 because every correction sat on the first-read path (learnings §27–28, §45). Every correction must sit off the hub, the anchor and the superseded record's own container |
| `/oe` | Every step discoverable from the prompt or an earlier step's Expected data; accurate tools and parameters; feasible path | Investor counterparties are tokenised (`PERSON_0787_NAME` for GFR, `PERSON_3242_NAME` for T-Accelerate). Expected values must be reachable values, never tokens the persona can't map |
| `/rubric` | Atomic rows, "The Agent …" titles, weights by kind of work (1/3/5), ≤ 5 samples per group plus a volume row, direct exception rows, no negative or `leaves X alone` rows, no predicted all-fail | Lessons from the Julia, Douglas and Frederick tasks: never bundle status with citation; one row per write target; apply /rubric Fix Lists verbatim |
| `/create-difficulty` | 6 Opus 5.5 slots; corrected avg < 85 %; < 5 full passes; population SD 0.10–0.30; ≥ 2 failure patterns (largest ≤ 50 %); ≥ 100 counted calls; ≤ 2 errored | Prior Frederick tasks landed at 78.3 % (SD 0.054, failed spread) and 80.8 %. Julia sat at 83.8 % with SD 0.099. The repeated cause was one dominant choke point. This design needs ≥ 3 independent channels with graded findability |

## 2. Frederick's reach at the clock (`persona_view.py reach frederick_stone`, `entity.py resolve`)

- **Slack:** 105 visible channels (34 private, 42 IMs), 4,780 own posts, last post 2025-09-30. Key memberships:
  `#executives` `C07C2866011` (members include Leonard, Robert, Arthur, Frederick) and `#bridge-pitch`
  `C096HFA5Z8W` (persona-view YES; 8 members, Jul–Sep 2025, Sep the busiest). **Not** a member of
  `#admin_foundersonly` `C04UEQVDVB7` (persona-view NO): no rule or fact may live there.
- **Gmail:** 4,656 threads (2024-06-25 → 2025-10-01). Frederick is cc'd on almost every bridge thread:
  LVP `1842277743427687737`, GFR `1843547312959065138`, Dentsu `1843473831194478743`, NCsoft
  `1832208184829815962`, T-Accelerate `1842283406259093714` (+ Bubbles AI action items `1843978997950200606`), SciPlay
  `1842285743246816270`, a16z re-intro `1842277213140775733`, GRx (Grishin) `1842278603974731778`, Homa intro
  `1843169166284025277` / `1843552279434086285`, and Speedrun feedback `1844748127814183717`. The 18 Sep 2025 "bridge"
  hits come from a census over threads last active from Jul 2025.
- **Calendar:** 316 events, own calendar only. The September pitch calls are on it: LVP `evt_e59dc0a675d0c407b79acf`,
  NCsoft `evt_d2044af06de4e892ce1d0a`, SciPlay `evt_25c9ee60d4b6c8f6d39a74` (+ prep `evt_546b97980cf40c73445670`),
  Homa/PERSON_5173 `evt_89381fe5a15b802c5652a9`, T-Accelerate `evt_be57cd7ca86d925fb5900c`, GFR Sep 30
  `evt_2204ffea306847eea6e5b0` (Sep 29 copy `evt_38bdf82a0d337c4d82695e` cancelled), Speedrun interview
  `evt_e802a3583ee79ff6087f76`, two Dentsu Oct 1 copies (`evt_3671b9a924ccba550e51fa`, `evt_eeca6fc7670fe1acd94440`)
  and the Oct 14 board meeting `evt_bd61f3209523d19fdd6ba2`. Titles often show only person tokens, a natural
  alias surface.
- **Drive family:** owns 46 files (root folder `d_175c0d7bc72ed244b944cb`, persona-view YES: a write target he
  owns, learnings §31). Shared and visible: Game Investor List 2025 `f_48247af79428823c3cac92` (89 firms, columns
  Status / Latest Status "as of 09/11", modified 2025-09-15), Internal Game Investor List 2024 `f_0b29566cd7932a205d54d2`
  (KB trap D04 lookalike), Bridge Narrative `f_17e6175e84e745f92b3415`, Reachout Template `f_2e3969eb7c39ae04b99e3f`,
  Executives Biweekly Sync `f_26e1f9a86761e35049192a`, Board Meeting Jul 25 doc `f_af99b76ff4da59a710edba`, Pitch MASTER
  `f_7e68dfdc57ea569d7688a1`, FAQ `f_36adfec7ed33bea26dbf8b`, BoD Jul 16 deck `f_7793bb93e59e9c0dee5129`.
  **Not visible:** the Bridge Round VC reach-out sheet `f_efaec72066ee44e5888bd7`, the internal Jul 16 BoD deck
  `f_0421912301531f11c54686`, the Employees-Contractors folder `d_2af93116d8dc22dba2323e` and the salary-freeze consent
  `f_b5cac6b6428ae5268e9d46` (all persona-view NO).
- **Unscoped:** Trello. The founders' board `640643a3fd8f3ca308d9318e` has "Existing Investor Update"
  `68c5a49e8491a9d7faf869d0` (last activity 2025-09-13), "Follow up on ZM investor video and UA creative"
  `688c4d0ca1f8e701b89a9700`, "Paperwork for the Board" `680ee5d709c2d601148c25ff` and three "Board Deck" cards.
  Contacts has 170 entries and **no investor contacts** (only internal people and Matthew Collins), a natural gap
  for alias mappings. Linear has **no** investor or tester-access ticket after Jun 2025. GitHub and Confluence are thin
  for this storyline. Frederick's identities are Linear `usr_175c0d7bc72ed244`, Trello `4b4a68fc0fec0b254e4f9d8e`
  and Confluence `user_EMPLOYEE_0008`. Entity flag: his GitHub login shows the name "Ryan"; keep GitHub off any
  identity-dependent row.
- **Clock hazards inside his view:** the Speedrun pass (`1844748127814183717`) was sent at 19:30 PT on Sep 30, which is
  Oct 1 02:30Z, between the seed bound and the data horizon. GEN §0a: never rely on it as a completed fact, and drop
  any graded dependency on a16z's status. Dentsu's in-person meeting is Oct 1 13:30 PT (future). GFR's first meeting
  was moved and its cancelled copy remains.

## 2a. Storylines (2–3) and recommendation

| # | Storyline | Fit (Exec/Founders × Corporate Ops) | Native services in Frederick's view | Hardness raw material | Verdict |
|---|---|---|---|---|---|
| **A** | **Bridge-round investor pipeline for the Oct 14 board pre-read.** Leonard launched the $2.5M bridge on Sep 3 (`#executives` `1756749288.785249`; `#bridge-pitch` lists `1756941551.539229` and `1757345124.546449`). By Sep 25 he gave it a "15 % chance" (`1758767624.533779`) and is in LA on Oct 1 for the Griffin AGM and Dentsu. Frederick owns bringing the pipeline current as of end of Sep 30 PT: every firm pitched, where it stands, what is still owed to whom, the committed amount, and the board-facing write-up | Strong: fundraising, board and investor coordination, pitches, co-founder strategy. Frederick's own strategic comment on the Homa co-dev path (`1758210489.170809`, `1758212400.974029`) | gmail, slack, gsheets, gdocs, gslides, gcal, gdrive, trello (8 natural); contacts and linear by injection; snowflake and confluence peripheral | A stale "Latest Status as of 09/11" list vs later mail; tokenised partners in calendar titles; GRx ↔ Grishin; Homa and T-Accelerate outside or only loosely on the list; investor build-access asks vs Arthur's "I have to add them by email for google play" (`#bridge-pitch` `1758677722.184129`); Bubbles AI action items vs what was sent | **Recommended** |
| B | Board housekeeping for Oct 14 (consents, 409A approval, option grants, "Paperwork for the Board") | Strong on paper (board/legal) | Weak: the consents and the Employees-Contractors folder are persona-view NO; Trello cards are stale (Apr–Aug); little Gmail | Few verifiable done/not-done pairs Frederick can open | Reject: reach |
| C | Strategic co-dev / publishing options (Homa, Rollic, TapNation, NCsoft pilot, Playable Factory) | Good (strategy and partnerships) but drifts into BD/Marketing, Frederick's other two tasks' territory | gmail, slack, gcal; thin elsewhere | Overlaps A's sub-cohort; Homa/TapNation names partly tokenised; TapNation has 0 hits in his mailbox | Fold into A as the "strategic / co-dev" subset rather than a task of its own |

**Why A.** It is the one live, high-stakes Corporate Ops thread on Oct 1. Frederick is on the cc of nearly every
record, the board date gives a natural deadline, and no completed or calibration task uses it (the Atlas lists it as
Rank 6 for Leonard and Robert in the normal universe only). The deciding facts can sit in different services by
nature: mail threads, Slack thread replies, calendar, the shared list, Contacts and a Linear ticket.

## 3. UGT plan (rule 1)

1. **Population is defined in an incorporated record, never by the solver.** Leonard's ask (the hub, a seeded mail
   to Frederick before 2025-10-01T00:00Z) defines the register's population in source-checkable terms: every firm or
   strategic the team pitched or had a call with since the Sep 3 kickoff, on the list or not. The list's 89 rows
   are not the population, and firms with no outreach this round are excluded. A census of pitched firms is built
   from the calendar, the cc'd threads and `#bridge-pitch`; completeness is claimed only over that census.
2. **Status vocabulary and as-of time are defined once, in the hub**: a closed set of statuses (for example
   passed / in active talks / awaiting first call / no reply) with a one-line test each, and an as-of time of end
   of day Tue Sep 30 Pacific. Each seeded deciding record is timestamped well inside that day (never 00:00–07:00Z
   Oct 1). a16z stays out of graded rows: its pass arrives at 02:30Z Oct 1 (§2). The as-of rule and both readings
   for a16z are accepted.
3. **Units and money.** Committed and soft-circled amounts are USD and whole dollars, and "committed" is defined
   (signed instrument) in the same incorporated record. The base has no bridge commitments, so seeded amounts are
   new, small and person-level. Census every name and amount before seeding (learnings §10, §12).
4. **Apply every rule sentence to every firm** (learnings §21): a fork sweep runs every status test over every
   census member, including Dentsu (meeting on Oct 1, future), GFR (moved meeting), LVP (pass Sep 25) and
   T-Accelerate (call Sep 22, deliverables sent). Any firm where two sentences disagree is fixed before SQL.
5. **Tokens.** No graded value is an anonymised token the persona can't map. Where a firm appears only as a partner
   token, a persona-visible mapping (a seeded Contacts entry, or the firm name in the thread or calendar body)
   carries it (Evals `1_Prompt_Eval.md` §2.1).
6. **Known destinations.** The register goes into a Board folder Frederick owns (seeded `gdrive` folder, owner
   Frederick, mirrored in the Drive and Sheets rows; learnings §31). The board-facing reply goes on Leonard's ask
   thread. The keep-warm follow-through writes go on the existing Trello "Existing Investor Update" card. All three
   are unique in his view.

## 4. Hardness plan (rule 4, Hardness v2)

Eight candidate channels, each a cross-source decision with a named convincing wrong source and the record that
beats it. Five use distinct named v2 traps; the core is the first four rows plus the filter pair.

| Channel | v2 trap (guide Part 3) | Convincing wrong source (who, when, authority) | Record that beats it | Weight-5 row it flips | Findability tier |
|---|---|---|---|---|---|
| DONE1 | **1 · Proving "done" across services** (A24, `done_gap`) | Leonard's `#executives` post (seeded, mid-Sep) that an angel "is in for $X" | Signing-service mail in Frederick's inbox: the SAFE is still awaiting signature on Sep 30. The hub defines committed as signed | That angel's status row; the committed-$ total | Medium (Gmail notification sender, not the angel) |
| DONE2 | **1 · Proving "done"** (A24) | Leonard's follow-up mail to a firm saying test-build invites went out (base pattern: T-Accelerate `1842283406259093714`, Dentsu `1843473831194478743`) | Seeded Linear ticket (Arthur) for the Android internal-track adds, still open, consistent with Arthur's base "I have to add them by email" (`1758677722.184129`) | "Still owed to the firm" row for that firm | Low (Linear rarely opened for fundraising) |
| CORR | **2 · A correction somewhere else** (A11, `superseding`) | The firm's own cc'd thread ends with the investor promising to "continue to play and let you know" (SciPlay `1842285743246816270`, Sep 18) | Seeded later **thread reply** by Robert under a different `#bridge-pitch` root, reporting the verbal pass. Channel history does not return thread replies, so it is off the first-read path | That firm's status row; passed count | Medium-low |
| INPUT | **8 · Wrong inputs to a total** (A11) | The first stated soft-circle amount in `#executives` | Seeded later mail from the angel lowering the amount, in another service | Committed / soft-circled total (graded as the corrected input plus the final figure, learnings §48) | Medium |
| ALIAS | **6 · Different names for the same thing** (A7, `scope_alias`) | The list row under the fund's brand name shows "no response as of 09/11" | Pass mail from a partner signing under the fund's legal or other name; a seeded Contacts entry maps partner → firm (base precedent: "GRx Feedback" ↔ Grishin Robotics, `1842278603974731778`) | That firm's status row | Medium |
| FILT1 / FILT2 | **7 · Items outside the obvious filter** (A17, `exact_predicate` / `near_miss_mention`) | The Game Investor List as the obvious population | Calendar calls with firms absent from the list: the Homa call (`evt_89381fe5a15b802c5652a9`, "HOMA" in `1843169166284025277`; Frederick's own Slack comment `1758210489.170809`) and one more pitched firm reachable only through a person-titled calendar event plus Contacts. The hub's population rule brings them in | Inclusion row per firm; volume row | Two tiers (Homa medium; the second low) |
| FOLLOW | **3 · Follow-through a rule requires** (A15) | None needed: the natural reading is no extra write | Seeded comment by Leonard on Trello `68c5a49e8491a9d7faf869d0`: every firm that passes goes on its keep-warm checklist | Checklist count row; one sample row | Medium-low (Trello is rarely opened) |

**Independence.** DONE1/INPUT (money), DONE2 (owed deliverables), CORR/ALIAS (status) and FILT (population) sit on
separate outputs and are decided by different records in different services. No unit of discovery decides more than
half the weight: the largest, CORR + ALIAS on status, is about 19 % of the sketch surface.

**Survives complete retrieval.** Every deciding record is the natural return of an ordinary call (the firm's mail,
the calendar, the card, the ticket). Each trap is lost by accepting a convincing source, not by failing to search.
Rules live in the hub and the card, never in the prompt (Part 8).

**Never-live checks (learnings §28, §45).** No correction is in the hub thread, the superseded record's container or a
delegating record's container. No bulk call (list rows, channel history) carries an answer. Decoys get same-term
names: the 2024 list (KB `D04`) and the duplicate Dentsu events.

**Controls (learnings §41).** Routine firms whose mail agrees with the list (for example the LVP pass, GRx pass and
GFR call), so finding a firm's mail does not by itself flag a trap.

### Part 7 checks: `hardness_v2_check.py --design` on a pre-scenario sketch

The sketch (`Working_Files/00_PreScenario/sketch_manifest.json` + `sketch_surface.json`; **not** the /create-scenario
manifest or surface) declares the channels above with planned containers. Output, verbatim
(`00_PreScenario/hardness_v2_check_output.txt`):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      2 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 4 requirements: {'R2': ['CORR', 'ALIAS'], 'R1': ['FILT1', 'FILT2'], 'R3': ['DONE1', 'INPUT'], 'R4': ['DONE2']}  [Part 5 rule 1]
  FLAG       DECISION_FLIP   7 of 8 rules can flip a weight-5 slot; not: ['FOLLOW']  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     1 weight-5 total(s); 1 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']

Flags (each needs a written disposition; redesign the difficulty, never weaken a fairness link or raise a weight):
  DECISION_FLIP FOLLOW: rule FOLLOW (A15) can flip slots of weight [3], no weight-5 slot
```

**Disposition, FLAG DECISION_FLIP FOLLOW:** keep FOLLOW as a secondary channel; it is not one of the required v2
decisions. /create-scenario either (a) reshapes the follow-through so its content needs the reconciled passed set
(CORR + ALIAS + FILT), which makes it honest 5-band multi-source work, or (b) leaves it at weight 3 and records the
FLAG. The weight is never raised. SAME_PLACE is CLEAN only on declared containers. It must be re-run on the SQL at
injection, and the CORR reply must be a thread reply, never a channel-level post.

## 5. Spread and score plan (rule 5, UNCALIBRATED)

`00_PreScenario/policy_model.py` scores a 19-slot sketch surface (total weight 69; 75 % flippable by mechanisms;
weights by kind of work). It models a Gaussian-copula run latent so findability varies across runs, and 3 % base
slips. Output is in `00_PreScenario/policy_model_output.txt`.

| Policy (whole) | Score |
|---|---|
| Perfect | 100 % |
| Reads every cc'd thread, no off-thread checks (CORR, DONE1, DONE2, FOLLOW land) | 50.7 % |
| List-bound (FILT1, FILT2, ALIAS land) | 65.2 % |
| Trusts "done" sources (DONE1, DONE2, INPUT land) | 71.0 % |
| Everything except follow-through | 91.3 % |

Single misses: DONE1 78.3 %, CORR 84.1 %, ALIAS 84.1 %, INPUT 85.5 %, FILT1/FILT2 88.4 %, FOLLOW 91.3 %, DONE2 92.8 %.
**One single miss alone does not clear the cap,** so a run must miss ≥ 2 channels to score under 85 %. That is the
design's main risk, the same one learnings §42 named.

Six-run Monte Carlo (design landing rates DONE1 .55, DONE2 .50, CORR .50, ALIAS .35, FILT1 .45, FILT2 .30, INPUT .40,
FOLLOW .55):

| Landing scale × rho | E[avg] | P(cap) | P(SD 0.10–0.30) | P(patterns) | P(all gates) |
|---|---|---|---|---|---|
| 1.00 × 0.3 | 59.1 % | 1.00 | 0.94 | 0.99 | 0.93 |
| 0.75 × 0.6 | 69.6 % | 0.93 | 0.89 | 0.96 | 0.81 |
| 0.60 × 0.6 | 75.2 % | 0.82 | 0.88 | 0.96 | 0.73 |
| 0.50 × 0.3 | 77.8 % | 0.81 | 0.91 | 0.98 | 0.76 |
| 0.50 × 0.6 | 79.0 % | 0.71 | 0.86 | 0.94 | 0.64 |

The targets (E[avg] ≤ 77 %, P(all gates) ≥ 0.5) hold until the landing rates fall to about 0.55× the design priors.
The ledger has **no Opus 5.5 family priors** (`hardness_ledger.py priors --model claude-opus-5-5` returns the
header only). The rates are borrowed from Hardness v2's 46-task account and are optimistic. Past Frederick tasks
landed lower than designed, which argues for keeping all eight channels rather than trimming. The forecast at
/create-scenario S9b replaces this sketch.

## 6. Volume plan

Honest necessary calls (no padding), from the census sizes above:

| Phase | Services | Calls |
|---|---|---|
| Discovery and rules: hub, list, `#bridge-pitch` Sept history (~3 pages at 100), `#executives` Sept pages, card, board invite | gmail, gsheets, slack, trello, gcal | ~45 |
| Population census: calendar Sep 3–30 listing, list rows, `#bridge-pitch` tracker posts, intros | gcal, gsheets, slack, gmail | ~25 |
| Per-firm (≈ 40–45 firms × ~4: mail search, thread read, Slack thread or search, calendar or contact check) | gmail, slack, gcal, contacts | ~170–190 |
| Cross-checks (signing-service mail, Linear tickets, Contacts aliases, Drive/Docs pre-read materials) | gmail, linear, contacts, gdocs, gdrive | ~20 |
| Writes and read-back: sheet create + values, reply, Trello checklist items (one per passed firm) | gsheets, gdrive, gmail, trello | ~25–30 |
| **Total** | 11 services | **≈ 285–310** |

**≥ 500 necessary calls are not reachable without padding:** the census is about 45 firms, and Slack replies are
search-sweepable (Hardness_Mastery §2.5). Seeding per-firm comments only to add reads would be manufactured work
(red team A, R1 #7). A volume exception (GEN §3a) is proposed below. Every other extreme target still applies (≥ 10
services carrying weight, ≥ 10 injected schemas without Confluence (learnings §26), ≥ 120 INSERTs, ≥ 12 traps,
2–4 hidden authorities, ≥ 3 chains). The planned injected schemas are slack, gmail, gcal, gdrive, gsheets, gdocs,
contacts, trello, linear and gslides (a board-pre-read deck stub or decoy), all ten used. The platform's 100-call
Long Horizon floor is comfortably met (observed Opus runs: 163–1,209 on comparable tasks).

## 7. Writes (rule 6)

| Write | Trigger the persona owns | Access proof needed |
|---|---|---|
| Register sheet in the Board folder | Leonard's ask to Frederick (hub) | Folder and file owned by Frederick (seeded Drive + Sheets rows agree); confirm the write returns ok in the pre-check (learnings §31) |
| Board-facing reply on the ask thread | Same ask | Mail thread in Frederick's mailbox; reply-all recipients pinned by the hub |
| Keep-warm checklist items on Trello `68c5a49e8491a9d7faf869d0` | Leonard's card comment (incorporated by the hub's "anything the investor-update card says") | Trello is unscoped; `trello_*` checklist tools exist in `Evals/references/tools/catalog.json` (verify the exact names at scenario) |

## 8. Decisions for you

1. **Storyline:** A, the bridge-round investor pipeline for the Oct 14 board pre-read, with C folded in as its
   strategic and co-dev subset. **Recommended.**
2. **Volume exception (GEN §3a):** the honest necessary-call total is about 285–310, below the ≥ 500 floor.
   Proposed: `volume_exception {call_budget_floor: 280, per_record_floor: 160}`, with the reason "investor census is
   ~45 firms; padding would be manufactured work". It needs your `requester_confirmation`. Without it, the only way
   to 500 is padding, which the goal forbids.
3. **Review waiver:** `REDTEAM_*` is not set in this environment, so `tools/redteam_review.py --dual` cannot run. At
   scenario I will record `RED TEAM UNAVAILABLE` plus a `RED TEAM FALLBACK:` line naming what stands in (the fork
   sweep, the whole-universe census, the policy scores). It stays in every Unresolved line until a review or the
   pre-check covers it (learnings §44). You can instead set `REDTEAM_*` before /create-scenario.
4. **a16z:** keep it in the register but ungraded (its pass lands after the seed bound). Confirm, or drop it from
   the population.

**Next step:** run `/create-scenario`.

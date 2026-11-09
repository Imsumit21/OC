# Pre-scenario analysis: Frederick Stone · Executive · Finance · Analysis and synthesis (analysis only)

Contains no prompt, Oracle Event or criterion text. Written 2026-11-06 for `/create-scenario`; revised the same day after your targets and a full pass over the completed Frederick tasks (§1a).
Probabilistic numbers are labelled **UNCALIBRATED**: they are design aids, not measured rates (learnings §9).
Evidence is in `Working_Files/00_PreScenario/`: reach census, identity resolution, can-see proofs, publisher census, warehouse months, exposure counts from stored runs, the sketch manifest and surface, the Hardness v2 checker output, and the policy, sensitivity and volume models with their outputs.

## 0. Assignment and context (verified)

| Field | Value |
|---|---|
| Persona | Frederick Stone, Co-founder, `frederick.stone@harmonygames.co` (roster `frederick_stone`) |
| Function / competency / skill | Executive · Finance · **Analysis and synthesis** |
| Horizon / mode | Long Horizon (`effective_profile: extreme`, GEN §3a) · **medium**: V3 cap is a corrected weighted average < 85 % |
| **Your targets (2026-11-06)** | **More than 130 counted calls in every run. Corrected average under 80 %.** Every other difficulty guideline still applies. Design target E[avg] ≤ 72 % (your cap minus 8 points). These replace the goal's 100-call and 85 % / 77 % figures wherever they differ |
| Universe | `synthcut`, hg4-synth-sep30cut v16. Eval clock 2025-10-01 07:00Z (00:00 PT). Seed bound `freeze_utc` 2025-10-01T00:00:00Z, which is Tue Sep 30 17:00 PT. Shutdown rules do not apply |
| Persona today | Wednesday, October 1, 2025; "yesterday" is Tue Sep 30 |
| Source | `task_context.py --task-dir Task_Authoring/task_inputs --write --require-source`: status `ready`, KB `bound`, context_hash `ec895c36b5f1…` |
| Tools | Last `Task_Authoring/tools` commit is c16c7a1. Universe content was read through `hg.py`, `persona_view.py` and `entity.py`. The one other touch was an `ls -la` of the Snowflake export folder, which read file sizes only. The Evals input store was not touched (learnings §37) |
| Red team | `REDTEAM_*` is unset (0 variables), so `redteam_review.py --dual` cannot run (§10, decision 3) |

**What I could not do.**
- A full Drive listing through `hg.py` was too slow at 12 KB per page, so I stopped it. Drive facts come from the census and targeted reads. His second owned folder is not identified.
- Table comments in Snowflake timed out through `get-many`. Row reads worked, so I have `REVENUE_DAILY` but no column comments.
- I did not compare the warehouse revenue against the P&L revenue lines. That check gates the baseline (§4).
- I could not confirm Frederick's membership of the UA/BD board from the board record. Stored handover runs did write there (§9), but no run has created a new card on it.
- STEP 0.6 cannot be measured locally (`hg_similarity.py` is not in the bundle).

**Originality constraint.** Frederick already has four submitted tasks, so the job has to differ from all of them and from what other contributors took:

| Neighbour | Its job | Why it matters here |
|---|---|---|
| `frederick_card_spend_q3` | Card spend breakdown for the Q3 Standard Metrics submission | Rules out a UA spend reconciliation |
| `frederick_account_handover` | Who holds each marketing and UA account | Rules out an account register |
| `frederick_bridge_pipeline` | Bridge-round send list for the Q4 investor update | Rules out investor status work; an L12 task sits at 0.804 on the board pre-read job |
| `frederick_q4_commitments` | Vendor and partner backlog | Rules out a vendor list; L12 "Leonard's vendor list" tasks are also taken |
| `samuel_zm_beta_messages` | Which Zombie Match player messages go out at beta | The goal's named exclusion. Different game, different job |

## 1. What a 5 needs at each gate

| Gate | What a 5 / PASS needs | Risks specific to this task |
|---|---|---|
| `/injection` | No seed contradicts any base record anywhere in the universe. Each seed is dated after the base events it relies on, follows schema and id contracts, and has no event timestamp after 2025-10-01T00:00Z. Companions are seeded (thread counters, GCal attendee copies, Drive and Sheets mirrors, Trello badges) | Publisher facts are the main exposure: 19 of the 22 names I censused have hits Frederick can't see (raw substring counts, unread; "Genera" and "Homa" are mostly noise), and Tilting Point has 10. Prefer minted publishers with no base footprint (learnings §10). Any seeded DD revenue claim must match `REVENUE_DAILY`. Never inject new ENG-2367+ issues (SC-26) |
| `/prompt` | Fit (hard gate), UGT, feasibility, cross-service coherence, natural voice, originality below 0.80, and no rules, traps or answers in the prompt | **Fit:** must read as a model and forecast for a founders' decision, not a BD log. **UGT:** a forecast is a fork unless every assumption sits in a record, and the base has six competing DD metrics (§4). **Coherence:** every deliverable section is checked for what the warehouse could answer instead (memory: base-disagreement-question-is-the-path) |
| `/hardness` (one pre-check) | PROCEED (3–5): the run misses weight-5 rows for real reasons. A 5 needs failures that invalidate the central result, and the eval says one root cause can justify it. The platform's narrow-miss rule scores 2 when a single cause fails less than the mode's loss (15 % on Medium) | Opus reads the hub and every record it names, bulk-reads mail and calendars, and resolves names through Contacts. On Q4 rev3 it caught 7 of 8 traps. Any Slack correction naming the publisher will leak in a run that sweeps names |
| `/oe` | Each step discoverable from the prompt or an earlier step's Expected data, with accurate tools, parameters and values | Expected lines use only values the agent can see. Never make a step read a Gmail attachment. Base docs hold anonymized tokens (`[USERNAME_52305]`), so they can't be Expected values or define the population |
| `/rubric` | Atomic "The Agent …" rows, weights by kind of work, ≤ 5 samples per group plus a volume row, no count bundled with an identity, one order row per write kind, no do-nothing rows, no predicted all-fail | Apply learnings §60–62 from the start. Keep Accept lines equal to titles. No fact in 3 or more rows, which limits how many rows one trap can move. Row growth is the largest risk to the spread gate (§6) |
| `/create-difficulty` | Six Opus 5.5 slots, corrected average **under your 80 %**, < 5 full passes, population SD 0.10–0.30, ≥ 2 failure patterns (largest ≤ 50 %), **over 130 counted calls in every run**, ≤ 2 errored | **SD is the gate at risk.** Recent results sit on the floor: bridge 0.106, Robert 0.103, Julia 0.099, Samuel 0.065. §1a gives the measured cause |

## 1a. What your completed Frederick tasks teach

Read for this section: each task's README, its stored baselines, its rubric, and for bridge and Q4 every failing platform report. Card spend and handover have no stored reports, so their rounds come from their READMEs. Output: `00_PreScenario/stored_runs_counted_output.txt`.

**What each task did** (counted calls from the stored difficulty input; "mixed" means weight that passed in some runs and failed in others):

| Task | Rows | Always-pass | Mixed | Always-fail | Average | SD | Counted calls | Writes per run |
|---|---|---|---|---|---|---|---|---|
| Account handover (Normal) | 37 | 50.4 % | **49.6 %** | 0 % | 80.8 % | **0.161** | 68–100 | 6–11 |
| Bridge pipeline | 40 | 61.3 % | **38.7 %** | 0 % | 77.7 % | **0.106** | 109–150 | 53–55 |
| Card spend Q3 | 63 | 65.0 % | **26.7 %** | 8.2 % | 78.3 % | **0.054** | 554–573 | 12–22 |
| Q4 commitments | 102 | 61.1 % | **15.1 %** | 23.7 % | 71.0 % | **0.016** | 151–212 | 88–93 |

**Three measured rules come out of this table.**

1. **SD follows mixed weight.** Across these four, SD ≈ −0.053 + 0.0042 × mixed %, so SD reaches 0.10 at about 36 % and 0.13 at about 43 % (n = 4, rough). **Target: at least 45 % mixed weight on the final rubric.** Row count drives it: only the two tasks with about 40 rows cleared the SD floor.
2. **Over 130 calls comes from writes.** Reads never fell below 54 on a Frederick task, and bridge's 53–55 writes left its weakest run at 109. Q4's 88–93 writes held its weakest run at 151. My first plan of 66 writes would have failed your floor, so the plan is now 86 (§7). Card spend's 554+ calls came from 533 `gdrive_read_file` calls on a big folder, not from design choices I can reuse here.
3. **High-count writes must be template-identical.** Bridge made 55 writes on 40 rows, because cards and checklist items were sampled. Q4's written answers differed per company, which took its rubric from 57 to 102 rows and failed coverage at 58 of 106.

**Gate history. No task has passed all five first time, and `/rubric` has never passed in round 1.**

| Gate | Bridge | Q4 | Card spend | Handover | What made the good rounds good |
|---|---|---|---|---|---|
| `/injection` | PASS r1 | PASS r1 | PASS | Not recorded | Census of seeds; every revision passed |
| `/prompt` | FAIL r1, r2, r4; NON-FAIL r5; PASS 5 r10 | **PASS 5 r1** | PASS | Not recorded | Q4 ran both blind sweeps before submitting. Bridge didn't, and failed on unsettled forks |
| `/hardness` | FAIL 1, NF 4, FAIL 1, NF 3 ×3 | FAIL 2, NF 4 | NF 3 | Not recorded | Corrections off the swept path, with several independent causes |
| `/oe` | 3 rounds | 2 rounds | PASS 5 | 2 rounds | Samuel's passed in round 1 after a blind reviewer raised 26 items first |
| `/rubric` | FAIL 1, FAIL 2, PASS 5 | FAIL 1, FAIL 1, PASS 5 | 4 rounds | Not recorded | Copying the Fix List word for word |

**What each failure teaches, applied to this task:**

| Gate | What failed | Rule for this task |
|---|---|---|
| `/prompt` | Bridge r1: ten forks, including Homa ("co-dev investment path", in or out?) and a written no against a later "didn't respond" | Run both blind sweeps **before** `/prompt`, as Q4 did. Settle Homa with a dated record, not a scope assumption |
| `/prompt` | Bridge r1: a "last two-way contact" column needed a judgment on every row | Drop any column that needs judgment and isn't graded |
| `/prompt` | Bridge r2: a seeded Linear comment contradicted base `#executives` | Blind coherence sweep over the full base, including every seed on Linear and Slack |
| `/prompt` | Bridge r4: 0.804 dataset duplicate | The job has to differ; rewording doesn't help. Avoid "board pre-read" and per-firm status wording |
| `/hardness` | Bridge r1 and r3: Opus caught everything. Q4 r1: one cause, 5 % failed, so score 2 | At least two causes in one run, and traps that flip the central result |
| `/oe` | Q4 r1: a search window with no source skipped Appodeal, and Frederick's Rayking message was called a reply when it's an **unsent draft** | The population rule states its own start date. Check `X-Gmail-Labels` on every base thread relied on |
| `/oe` | Bridge r1, r2: threads credited to the wrong firm; "the rest" lists left members out; a quote attached to the wrong firm | Confirm each thread's firm by recipient and signature. Enumerate sub-cases, never "the rest" |
| `/rubric` | Count bundled with identity, folder with file type, two order checks in one row, names only in the evidence | Check all of these before round 1 (learnings §60) |
| `/rubric` | Evidence and title disagreed: wider than the title in 13 Q4 rows, narrower in 2 bridge rows | Every Accept line equals its title, by construction |
| `/rubric` | Missing outcomes: every written answer, every list member in a reply, every column | The reply carries counts and a pick, never a list. Few columns. Distinct-content writes only where a trap needs them |
| `/rubric` | Overlap group: two rows failing on one error (Moderate, so a FAIL) | Trap rows must be different facts; never a count that one member's row implies |
| `/rubric` | One order row per write action, missing or bundled | One Process row per write kind, four here |
| Baseline | Q4: de-named corrections caught 0 of 6, so runs failed identically | Traps at about 30–60 %, on different habits, with at most one near-certain miss |
| Baseline | Handover's split (three runs 60–72 %, three 93–100 %) came from one heavy discovery | Heavy channels at about 50 % make spread. Small ones don't |
| Baseline | Builder weights drifted, moving bridge's SD from 0.106 to 0.098 | Diff the builder export field by field before the verifier runs |

## 2. Frederick's reach at the clock

Census output is in `00_PreScenario/reach_frederick.txt` and `entity_frederick.txt`. Proofs are in `cansee_anchors.txt`: every load-bearing record below is YES.

- **Slack.** 105 visible channels (12 public, 34 private, 17 mpim, 42 IM), 4,780 own posts, last post 2025-09-30. 55 more public channels are UNVERIFIED and not counted.
  - YES: `#executives` `C07C2866011`, `#bridge-pitch` `C096HFA5Z8W`, `#analytics` `C069FF9Q57S`, `#company-internal` `C05KNDCHAAG`, `#zombie-match3d` `C0880U9751A`, the PlayableX channel `C08H78VJG80`, and the DM with Leonard `D05S58U4SAK` (4,233 messages).
  - **NO:** `D04UC0UEN2V` and `D04UGG61DUM`, where Leonard says he is chasing publishers. Those two are coherence support only, never evidence.
- **Gmail.** 4,656 threads, 5,474 messages (2024-06-25 → 2025-10-01), 185 threads last active in Sep 2025. Base thread files are named `frederick@harmonygames.co_*`.
- **Calendar.** 316 events, 27 cancelled. Last before the clock 2025-09-30T17:30Z, next after it 2025-10-01T20:30Z. Board meeting Oct 14 is `evt_bd61f3209523d19fdd6ba2`.
- **Drive family.** He owns 46 items, including his root folder `d_175c0d7bc72ed244b944cb` (YES, owner), the only proven write home. 189 items are shared with him. The ones that matter:
  - "Publishing Partners" `f_10dfa1b4236a7c35dcb632`: owner, created 2025-09-24T17:08:16Z;
  - "Biz Dev Notes" `f_0d17fc08eddaf231cf7f28`: owner, regional publisher list and an outreach template;
  - "Publishing on Switch" `f_37fba7a0a1500b6731dc83`: owner;
  - "Executives Biweekly Sync" `f_26e1f9a86761e35049192a`: shared, last modified 2025-08-28.
- **Unscoped.** Linear `usr_175c0d7bc72ed244` (last active 2025-08-26). Trello `4b4a68fc0fec0b254e4f9d8e`; UA/BD board `66da196af476ab78deaa0cef`, with a "BD Follow Up" list `670015c2ecd45b634d5eec81` holding four cards from October 2024. Confluence `user_EMPLOYEE_0008`. Contacts lists him as "Commercial Lead, Marketing & Business Development" and holds no publisher entries: searches for Tilting, Appodeal, publisher and Publishing all came back empty.
- **Identity hazards.** His GitHub account shows the name "Ryan", and the sync doc lists him as "Ryan". His mail signature uses tokens. SC-49: don't grade his founder status.
- **His remit at the clock.** He owns the external commercial side. He ran the Appodeal publishing conversation in April–May, was handed the Rayking mail by Leonard on Sep 4, and on Sep 24 opened publishing outreach and created his own partner doc. His Sep 4 Rayking message is an **unsent draft** (`X-Gmail-Labels: Opened,Drafts`), so nothing went back to Rayking. He then said he'd try LinkedIn (`D05S58U4SAK/1757009185.631739`), which `/create-scenario` settles with a dated record. That is the role argument: it's his workstream, and the founders' question is addressed to him by name.
- **Clock hazards.** Seeds stop at Sep 30 17:00 PT. The September shard of `#executives` ends about 21:26Z, so the trigger lands after that and before 00:00Z. That channel also has an October shard. Oct 1 base events exist but are never completed facts.
- **Records between the seed bound and the clock.** The agent can read `#executives` from 00:00Z to 07:00Z on Oct 1. It holds the a16z rejection (`C07C2866011/1759288987.503349`) and Leonard's post that an NCsoft engine deal and/or co-dev covering "$25K/$50K a month" could keep a skeleton crew (`/1759290145.061509`), with bankers next if nothing lands in 7–10 days (`/1759290197.446099`). They fit the urgency and contradict nothing here. No seed can cite them, because they postdate the seed bound, and the design must not rely on them. The monthly figure is not a test in the model; if a reviewer reads it as one, the rule doc has to say what the model measures.

## 3. Storylines and recommendation

| # | Storyline | Fit (Exec inside Finance) | Reach and data | Originality | Hardness raw material | Verdict |
|---|---|---|---|---|---|---|
| **A** | **Domino Delights publishing-rights model.** The founders asked whether to give up DD's mobile publishing rights. With the bridge going badly, Frederick models what each publisher's terms would bring in over 12 months and inside Q4, against keeping the game, and recommends one | Strong on both. A founders' strategic decision, built as a forecast model with cash timing, as a non-dilutive alternative to a round | Best of the three: his own docs, threads and DM, all YES. Warehouse gives the keep baseline. Terms are seeded | No completed task and no pre-cut Atlas storyline. The Atlas publisher canvass is `[normal-only]`. Unmeasured | Real rights position in old records, a real dispute over which numbers to quote, publishers outside any list, aliases | **Recommended** |
| B | Co-dev versus bridge comparison: what each money path costs the founders in dilution and time | Strong, and the debate is live (`C096HFA5Z8W/1758210489.170809`, `/1758770975.016159`, `/1758772901.803289`) | Good, but only 4–6 paths | Weak: closest to the 0.804 neighbour | Touches SC-3, SC-5, SC-63, SC-73, and needs a runway figure. Too few members for spread | Alternate |
| C | Engine go-to-market budget and licence forecast: the $5K–$7.5K website ask and engine prospects | Good on pitch and budget | Weak: Leonard and Arthur own it, no prices in base, cohort almost entirely seeded | Good | A seeded-only world gives few real forks, which reads as contrived | Weak alternate |

Also screened and rejected:
- **ZM UA test budget** (Frederick's own Unity and Facebook tests). Rich Slack, but it sits on SC-4, SC-11, SC-12 and SC-23, four of the most-failed cards, and overlaps his card spend task.
- **Q4 cash forecast or runway.** SC-3, SC-5, SC-35, SC-73 and P&L version forks, plus a common pick.
- **Cap table.** He can't reach it: 0 visible docs and sheets, 5 visible Slack hits against 50 hidden, the last from 2025-07-29.
- **Pitch metrics claims pack.** The claims-register pattern was skipped after failing `/prompt` (dd-q4).
- **Closure reserve.** Leonard's line about saving cash to close the company (`C07C2866011/1758739428.647609`) is a wind-down premise, which the playbook bars on synth-cut.

**Why A.**

- It's the best fit for your targets: a decision model has one central result, so traps can flip it, which helps `/hardness`, the average and the spread at once (§6).
- The job is real at the clock. Leonard put the question to the founders on Aug 25 and at the Aug 28 sync, and Frederick was working it on Sep 24.
- It's Finance by output: a forecast with stated assumptions, cash timing and a recommendation, which is the competency's "models/budgets/forecasts".
- It's Analysis and synthesis by nature: no single record holds any answer, and each figure joins a term record, a rule and a later record.
- It's on Domino Delights, so it clears the theme screen outright and avoids Samuel's zombie decision.
- It stays off the runway and payroll cards by scoping the cash question to deal inflows only.

**Base facts behind A (all read through `hg.py`).**

| Fact | Record |
|---|---|
| "should we consider giving up global publishing rights?" … "I want to retain code, IP and non-mobile distribution rights but anything else is up for grabs" | `C07C2866011/1756140953.197759`, `/1756251167.453019`; `f_26e1f9a86761e35049192a` (Aug 28) |
| "we'll grow that game either with a publisher or organically" | `C08H78VJG80/1756223629.429589` |
| "The game is now being positioned with a publisher" | `C096HFA5Z8W/1757542591.718649` |
| Frederick asks about quoting incent numbers ($0.87 ARPDAU, 45 % D1r) and leaving out organic ($0.27, 25 %) | `D05S58U4SAK/1758735778.095599` |
| Leonard: pure organics, $0.50 D30 ARPI. Frederick: new tranche of potential publishers today | `D05S58U4SAK/1758736747.409459`, `/1758736827.548589` |
| Appodeal offered publishing with no game transfer or IP rights; thread ends on its unanswered nudge of May 21 | `frederick.stone@harmonygames.co/1829687508014442264`, `/1830012626042968381` |
| Rayking wrote about China publishing; Leonard asked "Should we explore for DD?"; Frederick's reply was never sent | `frederick.stone@harmonygames.co/1842348778705877030` |
| Tilting Point acknowledged a UA funding request on Sep 5; the title is not stated | `frederick.stone@harmonygames.co/1842443183462721250` |
| Apple Arcade had already signed a dominoes game | `C07C2866011/1756261199.570279` |
| DD revenue by month: Jun $3,401.73, Jul $2,078.33, Aug $721.55, Sep $381.11 | `ANALYTICS.MONETIZATION.REVENUE_DAILY`; `dd_revenue_months.txt` |
| The bridge is going badly: a16z out, Turkish VC "gonna be a no" | `C07C2866011/1759196260.965849`, `/1759182620.491829` |

A whole-universe scan of Slack for Aug and Sep 2025 found 19 hits for "publisher" and "publishing", and none contradicts a publisher outreach running in that window (`whole_universe_publisher_sept.txt`). I scanned Slack only, so Gmail outside Frederick's mailbox still needs the census.

## 4. UGT plan (rule 1)

1. **Population from a record.** A seeded outreach sheet that Frederick owns lists who was approached, when, by which tranche and with which numbers. It carries no outcomes. A rule record adds anyone who came to the company about DD, and states the start date, Apr 1, 2025, so Appodeal is in and the window has a source (the Q4 `/oe` lesson). Base lists aren't used as the population, because they hold anonymized tokens. Completeness is claimed only over a census of those two sources (learnings §23).
2. **One rule record, not the hub.** A seeded doc holds plain definitions: what counts as terms in writing, each status, the 12-month formula, the period, what counts as Q4 cash, and how to rank. Item-level resolvers stay out (memory: hardness-opus-sweep-pattern).
3. **Every assumption is named in a record.** The agent never estimates. Per-install value, period and start date are stated once. A forecast with one undefined input is a fork.
4. **Boundary for a stated limit.** Cash means deal inflows only. No deliverable asks for runway, burn, cash balance, installs by month or a per-network figure, because the warehouse answers those differently from other records (SC-1, SC-3, SC-5, SC-17, SC-73).
5. **Forks to settle with dated records before `/prompt`:**

   | Fork | Settled by |
   |---|---|
   | Which DD metric feeds the model ($0.87, $0.27, $0.34, $0.09 ARPDAU; $0.50 D30 ARPI; "LTV of $7") | Rule doc names one as the model's stated assumption, never as DD's true figure |
   | What the game earns if kept | Rule doc names the warehouse table and months. **Blocked until** warehouse revenue is checked against the P&L revenue lines |
   | Rights position | Base line above; rule doc points to it by role |
   | Is Appodeal live? (May proposal, last nudge unanswered) | A status definition plus a dated note |
   | Is Tilting Point about DD at all? (Sep 9 mail links UA funding to the second title) | Dated row in the outreach sheet |
   | Rayking (Frederick's reply is an unsent draft, so we never answered) | A status definition that covers it, plus a dated record if it needs more |
   | "a dude from [USERNAME_34104] looking for games" (`D05S58U4SAK/1758736842.534589`) | Row or dated close-out; it's an open base lead |
   | Apple Arcade | Rule test: no terms, already signed elsewhere |
   | Homa, NCSOFT, Mattel | Out of scope: co-dev or investment on another title. Homa was a bridge `/prompt` fork, so this needs a dated record that names the co-dev path as Zombie Match work, not a scope assumption. Rule doc scopes to DD publishing (`C07C2866011/1757516293.887729`, "So is NCsoft publishing?  investing?", is itself a fork) |
   | The Sep 30 trigger against base posts that day | Seeds dated after Sep 30 21:26Z |

6. **Apply each rule sentence to every item.** Before SQL, run the fork sweep over every publisher, status and boundary, and include every card, contact, draft and reminder decision in the sweep brief (memory: prompt-ugt-forks-need-records).
7. **Keep off the graded path.** Exec sync lines on Singular and Griffin pro-rata (SC-39, SC-63) sit in the same doc as the rights line, so cite that line only. Investor sheet rows (SC-9, SC-10, SC-33, SC-34). Vendor mail from `brian.foster@` (SC-6, and Craftsman+ uses the same address). Frederick's pay and founder count (SC-49, SC-54).
8. **Two blind sweeps before `/injection`** (memory: injection-stage-tool-gotchas, blind-sweeps-catch-base-contradictions): forks from persona-visible dumps only, then seeded-versus-base coherence over the full base. Restate the `hg.py`-only rule in both briefs.

## 5. Hardness plan (rule 4, Hardness v2)

Eight channels over seven of the guide's trap types. Each is a cross-source decision, names the convincing wrong source and the record that beats it, and moves ≥ 2 rows including a weight-5 row. `NEW` marks a planned seed, not yet checked against the whole universe. PA–PI are publishers to mint at `/create-scenario`. Weight shares are on the v2 surface in §6.

| Channel | v2 trap | Convincing wrong source (who, when) | Record that beats it (who, when, authority) | Weight share | Placement and landing rate |
|---|---|---|---|---|---|
| DONE | **1 · Proving "done" across services** (A24) | NEW PA partner manager's mail says the KPI test cleared and the first tranche is released (Sep 26); NEW BD card says test passed | NEW later `#analytics` reply by whoever ran the test: the window filled from the incent campaign, and the term mail ties the tranche to non-incent installs | 6.7 % | Reply under a root about another topic. 0.50; `done_gap` prior 0.50 (n_eff 4) |
| CORR | **2 · A correction somewhere else** (A11) | NEW PB term mail, advance figure (Sep 22) | NEW Leonard's note on the calendar entry for the follow-up call, with PB's lower figure (Sep 29) | 13.5 % | Measured habit: a calendar note found by name search 3 of 7. 0.55 |
| ALIAS | **6 · Different names for the same thing** (A7) | NEW PC term mail, unanswered, under its trading name (Sep 18) | NEW founder post that the parent group's person pulled out (Sep 28); her signature and a seeded Contacts row tie her to PC | 11.9 % | A trading-name search misses it. Deep name sweeps ran in 1 of 6 Q4 baselines. 0.50 |
| FILT1 | **7 · Items outside the obvious filter** (A17) | The outreach sheet plus Frederick's inbox as the population | NEW Robert's relay of PH's terms in a founders' thread; the rule record brings in anyone who came to the company | 17.1 % | Reply under an unrelated `#executives` post was caught 20–30 %, but a generic search can reach it. 0.45 |
| FILT2 | **7 · Items outside the obvious filter** (A17) | Same | NEW Arthur's comment on an open DD Linear ticket, recording PI's terms from an SDK question | 17.1 % | A Linear-only fact was 0 of 6 on Q4, so one pointer is added. 0.60 |
| EXC | **5 · A rule hidden in the data** (A15) | NEW PD's terms: largest 12-month value, clean mobile rev share | Base rights position (Aug 25 and 28, Leonard, founders): PD's grant is worded across all digital storefronts, so it fails | 16.1 % | Survives complete retrieval. Judgment rarely lands: 0.30 |
| INPUT | **8 · Wrong inputs to a total** (A11 on an aggregate) | NEW PE term mail, monthly install commitment (Sep 19) | NEW later comment on PE's existing BD card with the lower commitment PE confirmed (Sep 30) | 9.3 % | Card comments are read when the card is named, and this one isn't. 0.45. Graded as input and total on separate rows |
| FOLLOW | **3 · Follow-through a rule requires** (A15) | The model and the reply look like the whole job | NEW Leonard's standing line in a reply under a root about deck numbers: anyone quoted paid-traffic numbers gets the organic figures first; the outreach sheet shows who | 10.4 % | 0.50. A count and three per-target rows, never dozens |

**The central result is the point.** First pick, second pick and Q4 total each depend on two different channels, so a miss in any of DONE, CORR, EXC, INPUT or FILT2 corrupts what the founders asked for. That's what the eval's band 5 describes.

**Controls and decoys** (learnings §41): PF and PG are clean offers. Routine passes and silences give natural mail that agrees with the sheet, so finding a publisher's mail never marks a trap. Base Publishing Partners and Biz Dev Notes act as stale lists. Homa, NCSOFT and Mattel act as out-of-scope lookalikes.

**Reserves, held because the engines take at most eight rules** (learnings §41): trap 9 (a publisher already turned down in a cancelled invite note; `completion_elsewhere` prior 0.20) and trap 4 (a payment term landing a tranche just past Dec 31; `boundary_date` prior 0.67, n_eff 1).

**Independence.** Each channel has its own member, service pair and root cause. The largest unit decides 17.1 % of the sketch weight, far under half. No correction sits in the hub, an anchor, the superseded record's container or a delegating record's container. `/create-scenario` must still reach the extreme floors (≥ 12 traps, ≥ 7 families, ≥ 4 supersessions, ≥ 6 distractors); these eight are not yet counted against them.

**Survives complete retrieval.** EXC, ALIAS and DONE stay hard after every record is read, because each needs a join. CORR, INPUT, FILT1, FILT2 and FOLLOW are retrieval-shaped and depend on placement, which is why they carry different rates. Corrections are worded in plain language without the term mail's keywords (learnings §54).

**No row passes by doing nothing.** Exclusions are graded as exact counts on required writes, never as "leaves X" rows (playbook S8).

### Part 7 checks: `hardness_v2_check.py --design` on the pre-scenario sketch

The sketch (`00_PreScenario/sketch_manifest.json` + `sketch_surface.json`) is **not** the `/create-scenario` manifest or surface. Output, verbatim (`hardness_v2_check_output.txt`):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      4 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 7 requirements: {'R3': ['DONE'], 'R2': ['CORR'], 'R1': ['ALIAS', 'FILT1'], 'R7': ['FILT2'], 'R4': ['EXC'], 'R5': ['INPUT'], 'R6': ['FOLLOW']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   8 of 8 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     12 weight-5 total(s); 12 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

**Dispositions.** No FLAG or UNRESOLVED fired, but this is weak evidence: the tool reads what I declared. SAME_PLACE is clean only over declared containers and must be re-run on the SQL. INPUT's card sits on an anchor list, which the tool can't see, so treat it as a live same-place risk: the design keeps the comment on one card and off the list itself. RULE_IN_PROMPT re-runs once a prompt exists.

## 6. Spread and score plan (rule 5, UNCALIBRATED)

`00_PreScenario/policy_model.py` scores the v2 sketch surface against your 80 % cap: 57 slots, total weight 193, 67.4 % flippable by mechanisms, using a Gaussian-copula run latent and 3 % base slips. The surface is shaped like bridge and handover, per §1a. The first-pass surface (76 slots, 51.4 % flippable) is kept in `00_PreScenario/v1_first_pass/`. Output: `policy_model_output.txt`.

| Whole policy | Score |
|---|---|
| Perfect | 100 % |
| Inbox and outreach sheet only, nothing else opened | 32.6 % |
| Thorough except anything not under the trading name | 68.4 % |
| Term mails at face value, otherwise thorough | 74.6 % |
| Thorough except the population (sheet plus own inbox) | 75.1 % |
| Thorough except calendar and card comments | 77.2 % |
| Thorough except Slack beyond name searches | 82.9 % |
| Picks on value alone, misses the rights position | 83.9 % |
| Thorough on deals, finishes at the model and the reply | 89.6 % |

| Single miss | DONE | CORR | ALIAS | FILT1 | FILT2 | EXC | INPUT | FOLLOW |
|---|---|---|---|---|---|---|---|---|
| Score | 93.3 % | 86.5 % | 88.1 % | 82.9 % | 82.9 % | 83.9 % | 90.7 % | 89.6 % |

**No single miss gets a run under 80 %**, and 6 of the 28 pairs stay at or above it. A run needs two or three landings, so the design relies on several landing per run: 3.85 expected at design rates, and P(one run catches everything) about 0.005.

Six-run Monte Carlo at the rates in §5 (mean 0.48), all gates against your 80 % cap:

| Landing scale × rho | Mean landing rate | E[avg] | E[SD] | P(under 80 %) | P(SD 0.10–0.30) | P(all gates) |
|---|---|---|---|---|---|---|
| 1.00 × 0.20 | 0.48 | 60.1 % | 0.145 | 1.00 | 0.84 | 0.84 |
| 1.00 × 0.35 | 0.48 | 60.8 % | 0.170 | 0.99 | 0.92 | 0.92 |
| 1.00 × 0.60 | 0.48 | 62.0 % | 0.207 | 0.97 | 0.96 | 0.92 |
| 0.80 × 0.35 | 0.39 | 67.5 % | 0.175 | 0.94 | 0.94 | 0.89 |
| 0.70 × 0.35 | 0.34 | 71.0 % | 0.174 | 0.87 | 0.94 | 0.83 |
| 0.60 × 0.35 | 0.29 | 74.7 % | 0.169 | 0.75 | 0.93 | 0.71 |
| 0.50 × 0.35 | 0.24 | 78.4 % | 0.161 | 0.57 | 0.90 | 0.55 |
| 0.40 × 0.35 | 0.19 | 82.2 % | 0.149 | 0.36 | 0.84 | 0.35 |

**Targets.** E[avg] ≤ 72 % holds down to about 0.67× (a mean landing rate of about 0.32). P(all gates) ≥ 0.5 holds down to about 0.47× (about 0.23).

**Stress tests (`sensitivity_output.txt`).** Row growth from `/rubric` is the main risk: Q4 went from 57 to 102 rows and Robert from 73 to 130.

| Change (rho 0.35) | Flippable | E[avg] | E[SD] | P(all gates) |
|---|---|---|---|---|
| Design surface | 67.4 % | 60.7 % | 0.170 | 0.92 |
| +40 always-pass weight | 55.8 % | 67.5 % | 0.140 | 0.82 |
| +80 always-pass weight | 47.6 % | 72.2 % | 0.120 | 0.65 |
| +120 always-pass weight | 41.5 % | 75.8 % | 0.105 | 0.44 |
| 0.7× rates, +40 | 55.8 % | 75.9 % | 0.144 | 0.65 |
| 0.7× rates, +80 | 47.6 % | 79.4 % | 0.123 | 0.43 |
| Ledger priors | 67.4 % | 74.4 % | 0.164 | 0.72 |
| Ledger priors, +40 | 55.8 % | 78.8 % | 0.136 | 0.50 |

**Row budget.** The design holds up to about +80 weight, which is about 27 more rows at weight 3, or about 85 rows. The §1a floor of 45 % mixed weight lands at the same place, and flippable weight overstates mixed weight. So the line, with margin, is **no more than 75 rows** on the final rubric.

**The honest read.**
- The ledger view misses the 72 % target at 74.4 %, though it stays under your 80 %. `superseding` carries a prior of 0.17 (n_eff 4), against the 0.45–0.55 I placed CORR and INPUT at. The placement rates assume these carriers beat that family average.
- Flippable weight overstates mixed weight, because some rows will pass or fail in all six runs. Bridge's real mixed share was 38.7 %.
- The model's P(patterns) reads 1.00 only because misses are drawn independently given the latent. Bridge rev12 batch 1 failed patterns at 80 % when two traps were caught by the same run, so treat it as an upper bound.
- Landing rates are placement priors. Measured per-trap rates ran 0.125 (Q4 rev3, named), 0.46 (Samuel rev6), 0.50 (bridge rev12 batch 2) and near 1.0 (Q4 rev4, de-named).

**Pre-check odds (one run, rho 0.35).**

| Landing scale | P(no trap lands) | P(two or more land) | P(a central figure is wrong) |
|---|---|---|---|
| 1.00 | 0.07 | 0.82 | 0.88 |
| 0.70 | 0.17 | 0.65 | 0.75 |
| 0.50 | 0.28 | 0.49 | 0.62 |

**Consequences for `/create-scenario`.**
- Rebuild the surface at the expected final row count before SQL, rerun this model, and stop if mixed weight falls under 45 %.
- Keep routine members to about 24 publishers, sampled at ≤ 5 per group plus a volume row.
- Few columns, forecast figures for qualifying offers only, and a reply with counts and a pick.
- Give each trap ≥ 2 distinct facts, on different habits.

**Calibration caveats.** Opus 5.5 ledger priors are thin: `done_gap` 0.50 (n_eff 4), `exact_predicate` 0.33 (n_eff 4), `superseding` 0.17 (n_eff 4), `completion_elsewhere` 0.20 (n_eff 3), `boundary_date` 0.67 (n_eff 1), and none for `house_rule` or `alias`. Exposure counts come from stored runs on other tasks, and memory records that exposure moves between revisions. `/create-scenario` S9b's pre-registered forecast replaces this sketch.

## 7. Volume plan

Honest necessary calls from the planned cohort, with no padding:

| Phase | Services | Calls |
|---|---|---|
| Discovery and rules: the trigger, rule doc, sync doc, his two docs, outreach sheet, board and list, warehouse describe and queries | gmail, gdocs, gsheets, gdrive, trello, snowflake, slack | ~22 |
| Census: mail listing and searches, generic Slack searches, calendar, contacts, Linear, other Trello | gmail, slack, gcal, contacts, linear, trello | ~20 |
| Per record (~26 publishers × ~3: thread, Slack search, calendar or contact lookup) | gmail, slack, gcal, contacts | ~78 |
| Writes (table below) | gsheets, gdrive, contacts, trello, gmail, gcal | ~86 |
| Read-backs | gsheets, trello | ~3 |
| **Total** | 10 services | **≈ 209** |

**Writes are the lever for your 130 floor.** Stored Frederick runs never read fewer than 54 times, so every run clears 130 only with about 80 or more writes. These are per-publisher writes with no batch form. All but the three drafts are template-identical, so they count as calls without adding rubric rows:

| Write | Calls | Why the job needs it |
|---|---|---|
| Contact per publisher with a named person | 22 | Contacts holds no publisher entries, and Leonard and Robert need to reach them |
| Group checklists and one item per publisher | 30 | The founders review the outcome by group on the board. Bridge's pattern |
| Follow-up card per live or silent publisher, one comment on an existing card | 17 | Each has a next step and an owner. Bridge's pattern |
| Reminder per offer's response date | 8 | Offers lapse. Q4 made 10–13 of these per run |
| Follow-through drafts | 3 | The FOLLOW channel |
| Model sheet and reply | 6 | The deliverable |

`volume_model.py` (UNCALIBRATED, reads anchored on stored runs): per-run mean 174. With all writes made, the six-run minimum has median 155 and p5 144. If a run skips 10 writes through misses, the p5 is 134. **P(every run over 130) is 1.000, or 0.995 in the 10-write case.** Check the pre-check's counted calls at intake, because a run under 140 there means the plan needs more writes.

**≥ 500 necessary calls are not reachable without padding.** The job has about 26 publishers and 9 sets of terms. Reaching 500 would mean inventing publishers or work the founders don't need.

**Floors the exception does not lower**, with where each stands:

| Target | Plan | Status |
|---|---|---|
| Cohort ≥ 40 × ≥ 3 surfaces over ≥ 2 services | About 26 publishers, 3 surfaces | **Fails without a cohort exception.** GEN §3a allows one down to 10, and §1a argues for the smaller number anyway |
| ≥ 10 injected schemas, without Confluence or Snowflake | slack, gmail, gcal, gdrive, gsheets, gslides, gdocs, trello, linear, contacts: the same ten `frederick_q4_commitments` shipped | Reachable. Gslides has a natural role: the one-pager his outreach template offers, which carries the numbers that were quoted |
| ≥ 120 INSERTs | Publisher threads and messages alone run past this | Comfortable |
| ≥ 12 fragments over ≥ 7 services, 2–4 authorities, ≥ 3 chains, ≥ 12 traps | Rule doc, standing line and rights position as authorities; eight channels plus base forks | To be built at `/create-scenario` |

## 8. Injection plan (rule 3)

- **Census every seeded entity across the whole universe**: every publisher, person token and claim, hits read rather than counted, every mailbox included (learnings §10, §38). Absence checks carry a positive control (§35).
- **Prefer minted publishers** with no base footprint for anything financial. Real names stay as controls with minimal claims.
- **Date each seed after the base events it relies on**: nothing on the numbers debate before Sep 24 17:42Z, no second tranche before Frederick's Sep 24 line, the trigger after Sep 30 21:26Z and before 00:00Z.
- **Keep Frederick's own words consistent.** His Sep 9 mail (`frederick.stone@harmonygames.co/1823332883409810377`) says the company isn't spending on UA and that UA funding is for the second title. Seeds must not contradict either.
- **Stay off the Oct 1 posts.** The trigger and every seed predate Leonard's Oct 1 posts, so none may repeat the $25K–$50K figure or the bankers line. Check at `/create-scenario` that nothing in the model reads as a wind-down premise.
- **No comment on a closed ticket.** PI's Linear ticket must be open at the time of the comment, because later activity on a closed ticket fails the task (§50).
- **No fact only on Confluence** (§26). CORR sits in a calendar description, which is a ○ carrier in `Ask_Carriers.md`, though stored runs show `gcal_search_events` returns descriptions. Prove the route in the pre-check and keep a fallback.
- **Companions:** thread counters, one GCal copy per attendee, Drive and Sheets mirrors, Trello badges, and the Gmail `snippet` on any appended thread (§18).
- **Confirm the agent's tools return each seed** in the pre-check, and read it for fallback events.

## 9. Writes (rule 6)

| Write | Authorized trigger | Access proof needed |
|---|---|---|
| Model sheet in his own folder | Leonard's request | New file under `d_175c0d7bc72ed244b944cb`, or a seeded folder he owns, with Frederick as owner in both Drive and Sheets rows. `gdrive_move_file` ran in 5 of 6 bridge runs; confirm at scenario |
| Contact per publisher | Leonard's request | `contacts_add_new_contact`, 30–31 calls per run on Q4 |
| Group checklists, items and follow-up cards | A seeded record the prompt points at, as on bridge | Checklists and items are **proven on this board**: all 6 handover baselines wrote them to card `67cf1b506d78ad3c72e02a35`, every call returning without error. New cards on this board are unproven (bridge proved `trello_create_card` on the Harmony Games board). Confirm in the pre-check |
| Follow-through drafts | Leonard's standing line (the FOLLOW channel) | `gmail_create_draft`. Drafts, not sends, so nothing external goes out unreviewed |
| Reminder per offer's response date | Rule doc | `gcal_create_event` on his own calendar, 10–13 calls per run on Q4 |
| Reply to Leonard | Leonard's request | `gmail_reply_to_message` on his thread |

## 10. Decisions, made under your delegation

You wrote on 2026-11-06: "you can choose from your self which option is best fit for my requirements in this task". I've made each choice on that basis. Tell me if you want any of them changed before `/create-scenario`.

1. **Storyline: A**, the Domino Delights publishing-rights model. It has the best fit to your targets, because traps can flip a central result. It clears the theme screen outright, and nothing in the completed tasks does this job.
2. **Volume and cohort exceptions (GEN §3a).** Honest necessary calls are about 209, below the ≥ 500 floor, and the natural cohort is about 26, below 40. Recorded with your line above as the `requester_confirmation`:
   - `volume_exception`, reason "about 26 publishers and 9 sets of terms; reaching 500 would need padding, which fails on its own". Proposed here at floors 200 and 130; `/create-scenario` set them to **180 and 60** once the manifest was built, because the gate counts only evidence surfaces as per-record calls (70 honest calls), not the per-publisher writes;
   - `cohort_exception {cohort_floor: 24}`, reason "no natural 40-record publisher cohort exists; padding it would add always-pass rows that cut the SD".
3. **Review waiver.** `REDTEAM_*` is unset, so I'll record `RED TEAM UNAVAILABLE` and a `RED TEAM FALLBACK:` line. The fallback is stronger than a waiver alone: a fresh-agent design review at `/create-scenario` (on the Robert LLC task that found 8 major forks the gates missed), the two blind sweeps, the whole-universe census and the policy scores. The waiver stays in every Unresolved line until a review or the pre-check covers it (learnings §44).

**On submitting first time.** I've designed for it, but I can't promise it. No completed task passed all five reviews first time, `/rubric` has never passed in round 1, and `/hardness` judges a single run: even at design rates, P(two or more traps land) is 0.82. The steps most likely to save a round are the blind sweeps before `/prompt`, the §1a checks before `/rubric`, and holding the rubric to 75 rows.

**Next step:** done. `/create-scenario` has run; `01_Scenario_Design.md` holds the current design and overrides this sketch where they differ.

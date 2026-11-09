# Pre-scenario analysis: Samuel Turner · Design · Marketing and GTM · Retrieval (analysis only)

Contains no prompt, Oracle Event or criterion text. Written 2026-11-04 for `/create-scenario`.
Probabilistic numbers are labelled **UNCALIBRATED**: they are design aids, not measured rates (learnings §9).
Evidence is in `Working_Files/00_PreScenario/`: reach census, identity resolution, can-see proofs, exposure counts from
stored runs, the sketch manifest and surface, the Hardness v2 checker output, the policy model and its output.

## 0. Assignment and context (verified)

| Field | Value |
|---|---|
| Persona | Samuel Turner, Game Designer, `samuel.turner@harmonygames.co` (roster `samuel_turner`) |
| Function / competency / skill | Design · Marketing and GTM · **Retrieval** |
| Horizon / mode | Long Horizon (`effective_profile: extreme`, GEN §3a) · **medium**: corrected weighted average < 85 %; design target E[avg] ≤ 77 % |
| Universe | `synthcut`, hg4-synth-sep30cut v16. Eval clock 2025-10-01 07:00Z (00:00 PT). Seed bound `freeze_utc` 2025-10-01T00:00:00Z, which is Tue Sep 30 17:00 PT. Shutdown rules do not apply |
| Persona today | Wednesday, October 1, 2025; "yesterday" is Tue Sep 30 |
| Source | `task_context.py --task-dir Task_Authoring/task_inputsK --write --require-source`: status `ready`, KB `bound`, context_hash `72168f70a409…` |
| Tools | Last `Task_Authoring/tools` commit is 58c37b1. All universe content was read through `Task_Authoring/tools/hg.py` or `persona_view.py`; the only other touches were read-only directory listings. The Evals input store was not touched. Frederick's analysis supplied the format and the model code only; no fact was carried over from it |
| Red team | `REDTEAM_*` is unset (0 variables), so `redteam_review.py --dual` cannot run (decision 3) |

**What I could not do.** `hg.py get` only parses JSON, so it cannot open repo source files under `root/`. I did not read
`match3d/Assets/Scripts/Notifications/NotificationManager.cs`, because the goal and GEN §4 route universe access through
`hg.py` (decision 4). What the code does is known only from PR #248's review hunks, commit messages and Slack.

**Originality constraint.** Other work to stay clear of: Frederick's vendor and partner commitments
(`frederick_q4_commitments`), Julia's ZM difficulty register and Douglas's ZM beta server sign-off. The last two share
the game and the beta but not the job. STEP 0.6 cannot be measured locally (`hg_similarity.py` is not in the bundle).

## 1. What a 5 needs at each gate

| Gate | What a 5 / PASS needs | Risks specific to this task |
|---|---|---|
| `/injection` | No seed contradicts any base record anywhere in the universe. Each seed is dated after the base events it relies on, follows schema and id contracts, and has no event timestamp after 2025-10-01T00:00Z. Companions are seeded (INT-01 Slack copies of GitHub comments, GCal attendee copies, Drive and Sheets mirrors, Trello badges). A closed ticket takes no later activity | Claims about the client code are the main exposure: `/prompt`'s deep recheck reads git, so seeded QA notes must report observations, never code facts I have not verified. Store-review mail needs a whole-universe census first: 131 "App Review" and 206 "Guideline" hits sit in other mailboxes, unread |
| `/prompt` | Fit (hard gate), UGT, feasibility, cross-service coherence, natural voice, originality below 0.80, and no rules, traps or answers in the prompt | Fit: the job must read as retention communications, not Engineering Ops, so tickets stay follow-through and the plan stays the main artifact. UGT: ten base forks in §4 need dated records. Coherence: Snowflake's push table disagrees with Slack (§4 item 6) |
| `/hardness` (one pre-check) | PROCEED (3–5): the run misses weight-5 rows for real reasons | Opus reads the hub and every record it names, bulk-reads mail and calendars, and searches Slack per name. It caught 7 of 8 designed traps on the Frederick rev3 pre-check. Common feature names help on some rows: as Samuel, "Plague Race" returns 201 Slack hits, "Season Pass" 335 and "Leaderboard" 709. They do not help everywhere: "Win & Collect" returns 13 and "Collect & Win" 8 |
| `/oe` | Each step discoverable from the prompt or an earlier step's Expected data, with accurate tools, parameters and values | Expected lines use only values the agent can see. Base tokens (`[PERSON_NAME_…]` inside copy) must never be Expected values, which rules out three PNs Beta bodies as verbatim graded text |
| `/rubric` | Atomic "The Agent …" rows, weights by kind of work, ≤ 5 samples per group plus a volume row, no count bundled with an identity, one order row per write kind, no do-nothing rows, no predicted all-fail | Apply learnings §60–62 from the start. Cross-service joins are weight 5. No fact in 3 or more rows, which caps how many rows one trap can move |
| `/create-difficulty` | Six Opus 5.5 slots, corrected average < 85 %, < 5 full passes, population SD 0.10–0.30, ≥ 2 failure patterns (largest ≤ 50 %), ≥ 100 counted calls, ≤ 2 errored | The cap is at real risk here, not only the spread (§6). Julia's medium task landed 83.8 % with SD 0.099. Each trap needs ≥ 2 rows and a different catch rate |

## 2. Samuel's reach at the clock

Census output is in `00_PreScenario/reach_samuel.txt`, `reach_samuel_full.txt` and `entity_samuel.txt`. Proofs are in
`cansee_anchors.txt`: every load-bearing record below is YES.

- **Slack.** 84 visible channels (17 public, 24 private, 17 mpim, 26 IM), 4,586 own posts, last post 2025-09-29.
  - YES: `#zombie-match3d` `C0880U9751A`, `#zombie-bugs` `C08R27X0EAH`, `#zombie-art` `C08R8CHB0QL`, `#zombie-ops`
    `C08R6BF4ENN`, `#company-internal` `C05KNDCHAAG`, `#analytics` `C069FF9Q57S`, `#builds` `C05433XK267`, `#zombie-prs`
    `C093LEZGF6J`, and DMs with Leonard `D06L58XCVKK`, Robert `D06KPMDV2JZ`, Arthur `D06KV30TPL4`, Vincent `D06UFE81RF0`.
  - **NO:** `#executives` `C07C2866011`, `#zombie-design` `C090N54TG79`, `#bridge-pitch` `C096HFA5Z8W` and the PlayableX
    channel `C08H78VJG80`. The casual-versus-hardcore debate and Leonard's Sep 22 feedback note live there.
- **Gmail.** 3,870 threads, 4,504 messages (2024-02-20 → 2025-10-01), 31 threads last active in Sep 2025. Mostly GitHub and
  crash-report notices, so the mailbox is noisy. Base thread files are named `samuel@harmonygames.co_*`.
- **Calendar.** 344 events (9 in Sep 2025), last before the clock 2025-09-29: "POD: PROTOTYPE", "Engineering Focused Weekly
  Planning". Nothing after the clock.
- **Drive family.** He owns 24 items, including his root folder `d_caafeec2804b3a67ce46aa` (YES, owner): the only proven write home.
  108 items are shared with him. The ones that matter:
  - "Push Notifications Zombie Match" `f_a325dd4af80afc5994d5dc`: owner is a `Resource:` id, Samuel is on the share list, so **readable but write access is unproven**;
  - "Zombie Match Data Dictionary Firebase" `f_12b4105f4b64c3ad374a9f`;
  - "GTM - Beta" `f_ffbe775ff72a994c5d6b7c` (2024, Domino era);
  - "Playtestcloud learnings" `f_151b8f3952d3101dd82174` (2024);
  - "A_B testing significance calculator" `f_13decec676011bf400e4e7`.
- **Unscoped.** Linear: `usr_caafeec2804b3a67`, 183 issues assigned, with Rate Us ZOM-397, permission fixes ZOM-320/366/414 and open
  ZOM-453, ZOM-471, ZOM-539, ZOM-542. Trello: `4ac40f0fbbad94d9e0e2df2a`; ZM ROADMAP `6851a6569f3bf818760632ab`. GitHub: `EMPLOYEE_0004_GITHUB_USERNAME`,
  his name shows correctly. Confluence: `user_STAFF_18`. Contacts: "Game Designer".
- **His remit at the clock.** He built the ZM messages: Leonard sent him the sheet on Jun 17 (`D06L58XCVKK/1750138057.452159`),
  the card is "[Feature] Push Notifications - Samuel + Leonard" (`6851a769c65dc0017a227bb7`), and he merged match3d#248 on Jun 26,
  #292 on Jul 10, #327 on Jul 22 and #333 on Jul 28. He also fixed the permission timing and the Rate Us popup. That is the role argument: it is his own work.
- **Clock hazards.** Seeds stop at Sep 30 17:00 PT. Base `#builds` and `#zombie-prs` activity runs to Oct 1. So far this is only a spot check: no notification mention in `#builds` on Sep 30, and one commit push in `#zombie-prs` on Oct 1. The full check belongs to `/create-scenario`.

## 3. Storylines and recommendation

| # | Storyline | Fit (Product & Design inside Marketing and GTM) | Reach and data | Originality | Hardness raw material | Verdict |
|---|---|---|---|---|---|---|
| **B** | **Zombie Match beta player messages.** Before the beta, Samuel works out which push and local messages actually go out: which feature each depends on, its final line, trigger and audience, and what is missing for the rest | Strong on both sides. Retention communications with the design requirements behind them (triggers, level gates, permission timing, copy). Output is a plan sheet and a report, the competency's expected outputs | Best of the three: his own sheet, card, PRs and DMs, all YES. 14 rows on PNs Beta, 7 on the older tab, 16 translated | No Atlas storyline; a job the ZM neighbours do not ask for. Unmeasured | Real base forks: Ready vs LIVE, a June sheet against a July rename, Domino leftovers, a permission ask that post-dates the first-session trigger, event aliases | **Recommended** |
| A | Beta audience-fit register. Samuel compiles PlaytestCloud sessions and team friend-tests so the founders can pick casual or hardcore for the beta | Strong on prototype evaluation and demand. The live debate is real (Robert's Sep 22 four questions, Leonard's Sep 29 "lean into hardcore") | Weak: all of it sits in `#zombie-design` and `#executives`, both NO for him, so a seeded relay has to carry it. Cohort of ≥ 40 testers is easy but almost entirely seeded | Good | Unique tester names leak to per-name Slack search (memory: precheck-name-search-sweep, all 36 company names searched). A long register adds always-pass rows, which pulls SD down | Alternate |
| C | Store listing refresh: check each store-page claim against what the beta contains | Good on GTM communications | Weak: Leonard and Martin own it; asset updates are in `#executives` (NO) | Low: the claims-register pattern was skipped after failing `/prompt` (dd-q4) | Status questions run straight into SC-16, SC-38 and SC-68 | Reject |

Also screened and rejected: Domino localization (`#localization-round-two` went quiet in July, no live ask); a Q4 live-ops calendar (Frederick owns the page; SC-31 and SC-47); retention by creative (records are in `#zombie-design`, NO).

**Why B.**

- The job is real at the clock. `#zombie-bugs` carries Robert's Sep 18 "Push notification needs to be pushed back" (`C08R27X0EAH/1758238811.686629`), and the sheet has not changed since Jun 23.
- It is Retrieval by nature: every value is found in a record. The agent writes no new copy, so UGT stays reachable.
- The traps come from base history rather than from invention, and they need joining records across services.
- Common feature names give natural cover on the rows that carry them against per-name search, the behaviour that beat Frederick's rev3 (§1 has the counts, and the rows it does not protect).

**Base facts behind B (all read through `hg.py`).**

| Fact | Record |
|---|---|
| 14 PNs Beta rows: Status 6 Ready / 8 Not Ready; second column 6 LIVE / 8 WIP. The two columns disagree on 4 rows (Quests, Hourly Coins, Plague Race, Weekly Leaderboard) | `f_a325dd4af80afc5994d5dc`, last modified 2025-06-23 |
| The six Ready rows match strings in PR #248's review hunks (lives, 1-day and 7-day lapsed, first mission, race, weekly reset) | `harmonygames-Games/match3d#248` |
| Two bodies still say "Puzzles vs Zombies"; the game was renamed on Jul 24 | sheet rows; `page_zm3d_gdd`, `page_release_checklist` |
| Every message is local: "All our PNs are local", "We aren't using Push notifications yet" | `C08R27X0EAH/1758239520.618939`; `D06KV30TPL4/1750979784.704799`, `/1750979856.324639` |
| Permission ask: Robert "Let's shove it to level 20" (Jul 10); Vincent saw level 13 on variant C (Aug 13); Leonard "PNs are at the beginning" (Sep 19) | `D06KPMDV2JZ/1752162738.497679`; `C08R27X0EAH/1755084279.518809`; `C08R27X0EAH/1758291802.756889` |
| Rate Us levels: 25/50/100/250 on the card; 26/50/75/100/150 then 26/50/100/250 in the DM; 26/50/100/250 on the ticket | `6874409dfe0decf6f8fca64f`; `D06L58XCVKK/1752706696.644399`, `/1752707383.162659`; ZOM-397 |
| Beta scope: Win & Collect, Reward Animations, Season Pass, Infinite HP Boss Mode (Sep 12); Axe Arena postponed (Sep 22) | `C05KNDCHAAG/1757704290.799329`, `/1758558164.541689` |
| Collect & Win is "Same feature as Win & Collect on Domino Delights, under a different name"; hourly coins are only a Backlog card | `page_liveops_calendar`; Trello `68c45bba5d2c25a3a5c26a8c` |

## 4. UGT plan (rule 1)

1. **Population from a record.** Leonard's seeded DM (before Sep 30 17:00 PT) defines the population in checkable terms: the PNs Beta rows plus asks made in named kinds of place. It names no members. Completeness is claimed only over a census of those places (learnings §23).
2. **One closed decision set in a rule record, not the hub.** A seeded doc holds Go, Hold and Drop, a one-line test for each, and their order. It must say neither sheet column decides on its own. Plain definitions only; item-level resolvers stay out (memory: hardness-opus-sweep-pattern).
3. **Every graded value comes from a record.** Final lines are found, never written by the agent. Bodies with `[PERSON_NAME_…]` tokens are not graded verbatim.
4. **Forks to settle with dated records before `/prompt`:**

   | Fork | Settled by |
   |---|---|
   | Ready vs LIVE on 4 rows | rule doc wording |
   | Permission ask point (level 13, level 20, "at the beginning") | a seeded decision dated after Sep 25, consistent with Robert's stated preference for late |
   | Local vs server label | Arthur's Jun 26 definition, restated by the rule |
   | Rate Us levels | ticket ZOM-397, which Leonard's Jul 16 DM says to follow |
   | Beta scope | Sep 12 and Sep 22 posts; the Trello list name is never used (SC-13) |
   | Current game name | a record stating which name goes in copy |
   | Collect & Win vs Win & Collect | live-ops page |
   | Domino-only rows (Nathan's Treasure Hunt, Streak Fever) | rule test plus live-ops page |
   | Season Pass | decided by the opt-in, never by ship date (SC-38) |
   | Hourly coins vs Hourly Collection | Backlog card |

5. **Apply each rule sentence to every item.** Before SQL, run the fork sweep over all rows, asks and boundaries (learnings §21–22).
6. **Keep off the graded path.**
   - Snowflake `PUSH_NOTIFICATION_STATS`: 25 ZM rows with provider `firebase` from 2025-04-12 to 2025-09-27, against "All our PNs are local". This conflict is not on the SC cards, so Snowflake stays out of the task and the prompt asks for no send stats.
   - Feature unlock levels: they vary by A/B variant (`C08R27X0EAH` Aug thread; `page_season_pass_spec` calls the level an active A/B variable; leaderboard 22 vs 28 in DMs). Never grade them.
   - Cards touched: SC-13, SC-14, SC-16, SC-19, SC-38, SC-57, SC-68, SC-7, SC-36, SC-70. Each is avoided: no beta date, no "complete" flags, no Linear state as proof of shipping, no build-number matching, no Boss Arena dates, no share list built from membership, no Slack timezones.
   - Hazards to cite at scenario: S01 (match3d PRs cite ENG keys, as #327 and the Rate Us card do) and R03 (redacted repo names in GitHub mail).
7. **Two blind sweeps before `/injection`** (memory: injection-stage-tool-gotchas): forks from persona-visible dumps only, then seeded-versus-base coherence over the full base.

## 5. Hardness plan (rule 4, Hardness v2)

Seven channels. Each is a cross-source decision on a distinct v2 trap type, names the convincing wrong source and the record that beats it, and moves ≥ 2 rows including a weight-5 row. `NEW` marks a planned seed, not yet checked against the whole universe.

| Channel | v2 trap | Convincing wrong source (who, when) | Record that beats it (who, when, authority) | Rows it moves | Placement and findability |
|---|---|---|---|---|---|
| DONE | **1 · Proving "done" across services** (A24) | Sheet says Ready (Jun); the string shipped in merged, approved match3d#248 (Samuel, Arthur, Jun 26); NEW QA ticket closed Done | NEW inline review comment on a later match3d PR by Vincent, the QA owner on `page_release_checklist`: the race reminder did not fire on one platform on a current build | Decision (5), blocker (5), go count (5) | Low: inline comments opened in 1 of 6 Douglas runs and only 1–9 calls in Julia's. Its `#zombie-prs` bot copy gives a second, noisy route |
| CORR | **2 · A correction somewhere else** (A11) | The 7-day lapsed headline on PNs Beta (Jun) | NEW later thread reply by Leonard under an unrelated `#zombie-art` post, using a nickname for the line rather than the sheet's words | Final line on the plan (5), same line on its string ticket (3) | Low–medium: a reply under an unrelated root was caught about 20–30 % of the time |
| DATE | **4 · Dates, windows and dependencies** (A4) | First-session row: Ready, LIVE, "Level 20 not completed", 12 hours; `AddHours(12)` in the #248 hunks | Robert's Jul 10 DM plus NEW beta ask-point decision: the players this trigger selects have not been asked for permission yet | Decision (5), named gap (3), go count (5) | High findability: both records are on the normal path, so it stays hard only as a judgment. Measured judgment traps rarely land, so I rate it lowest |
| EXC | **5 · A rule hidden in older records** (A15) | Paid-pass row: finished copy, audience Everyone, feature named in the Sep 12 beta scope | NEW older store-review note in Samuel's own mailbox: promotional messages need an explicit opt-in. ZOM-314 and match3d#263 show one general Notification On/Off toggle and no separate promotional one, so **the note must say whether that toggle counts**, or this is an open fork | Decision (5), missing piece (3), go count (5) | Medium: older mail is reached by name search, and his mailbox is noisy |
| ALIAS | **6 · Different names for the same thing** (A7) | No ticket carries the sheet's "Win & Collect" name, so a new one looks needed | `page_liveops_calendar` (Sep 29, Frederick) plus NEW ZOM ticket under the Collect & Win name | Reuse (5), event name in copy (3), new-ticket count (5) | Medium: a search by the sheet's name misses it, but both names return few hits (13 and 8), so a run that tries the other name finds it at once |
| FILT | **7 · Items outside the obvious filter** (A17) | PNs Beta as the whole population | NEW ask in a comment on ZOM-542 (Regression, home screen for game modes), brought in by Leonard's scope | Row present (5), trigger (3), counts (3, 5) | Medium: a ticket with no notification word; item outside the sheet. Same family as Frederick's one landed trap |
| FOLLOW | **3 · Follow-through a rule requires** (A15) | The plan records why each message is held, so nothing else seems owed | NEW standing rule on a roadmap card other than the named one: a held item gets a note on its own ticket | Notes count (5), sample note (3) | Medium: `trello_get_comments` ran in 3 of 6 Douglas runs and in 6 of 6 bridge runs, where the prompt named the card. This rule sits on a card the prompt does not name |

**Controls and decoys** (learnings §41): lives-recharged and 1-day lapsed (Go), Axe Arena, Streak Fever, Nathan's Treasure Hunt, Hourly Coins (out), the Rate Us chain, the older PNs tab, PN BETA Translated (Domino copy) and a seeded beta deck as stale lists. Finding a feature's records never marks a trap by itself.

**Independence.** Each channel has its own member, service pair and root cause. The largest unit (FILT) decides 16.8 % of the sketch weight, far under half. No correction sits in the hub, an anchor, the superseded record's container or a delegating record's container. The hub delegates by role and lists no members. `/create-scenario` must still reach the extreme floors (≥ 12 traps, ≥ 7 families, ≥ 4 supersessions, ≥ 6 distractors); the base chains above supply candidates, and they are not yet counted.

**Survives complete retrieval.** DATE, EXC and ALIAS stay hard after every record is read, because each needs a join. DONE, CORR, FILT and FOLLOW are retrieval-shaped and depend on placement, which is why they carry different catch rates.

### Part 7 checks: `hardness_v2_check.py --design` on the pre-scenario sketch

The sketch (`00_PreScenario/sketch_manifest.json` + `sketch_surface.json`) is **not** the `/create-scenario` manifest or surface. Output, verbatim (`hardness_v2_check_output.txt`):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      1 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 7 requirements: {'R2': ['DONE'], 'R4': ['CORR'], 'R3': ['DATE'], 'R6': ['EXC'], 'R5': ['ALIAS'], 'R1': ['FILT'], 'R7': ['FOLLOW']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   7 of 7 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     3 weight-5 total(s); 3 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

**Dispositions.** No FLAG or UNRESOLVED fired, but this is weak evidence: the tool reads what I declared. SAME_PLACE is clean only over declared containers and must be re-run on the SQL. RULE_IN_PROMPT re-runs once a prompt exists. The three totals are graded as counts, each with its own named-member rows.

## 6. Spread and score plan (rule 5, UNCALIBRATED)

`00_PreScenario/policy_model.py` scores the 27-slot sketch surface: total weight 95, 74.7 % flippable by mechanisms, using a Gaussian-copula run latent and 3 % base slips. Output: `policy_model_output.txt`.

| Whole policy | Score |
|---|---|
| Perfect | 100 % |
| Sheet flags taken at face value | 25.3 % |
| Thorough except anything outside the sheet's own names | 74.7 % |
| Trusts Ready plus a merged PR, otherwise thorough | 75.8 % |
| Reads everything, applies the flags literally | 77.9 % |
| Thorough except PR inline comments | 84.2 % |
| Thorough except mail older than the beta window | 86.3 % |
| Thorough except Slack thread replies | 91.6 % |
| Right calls, misses the ticket-note rule | 91.6 % |

| Single miss | DONE | CORR | DATE | EXC | ALIAS | FILT | FOLLOW |
|---|---|---|---|---|---|---|---|
| Score | 84.2 % | 91.6 % | 86.3 % | 86.3 % | 86.3 % | 83.2 % | 91.6 % |

Only DONE and FILT clear the 85 % cap alone. **No pair of misses stays at or above the cap**, so any run with two landings is under it.

Six-run Monte Carlo. Design landing rates: DONE 0.60, CORR 0.55, FILT 0.50, FOLLOW 0.50, EXC 0.45, ALIAS 0.35, DATE 0.25 (mean 0.46).

| Landing scale × rho | Mean landing rate | E[avg] | P(cap) | P(SD 0.10–0.30) | P(< 5 full) | P(patterns) | P(all gates) |
|---|---|---|---|---|---|---|---|
| 1.00 × 0.30 | 0.46 | 62.1 % | 1.00 | 0.94 | 1.00 | 1.00 | 0.94 |
| 0.80 × 0.35 | 0.37 | 69.2 % | 0.97 | 0.95 | 1.00 | 1.00 | 0.92 |
| 0.60 × 0.35 | 0.27 | 76.5 % | 0.85 | 0.92 | 1.00 | 0.99 | 0.81 |
| 0.50 × 0.35 | 0.23 | 80.1 % | 0.72 | 0.87 | 1.00 | 0.98 | 0.69 |
| 0.40 × 0.35 | 0.18 | 83.8 % | 0.53 | 0.79 | 0.99 | 0.97 | 0.51 |
| 0.30 × 0.35 | 0.14 | 87.6 % | 0.31 | 0.66 | 0.97 | 0.94 | 0.30 |

**Targets.** E[avg] ≤ 77 % holds down to about 0.60× (a mean landing rate of 0.27). P(all gates) ≥ 0.5 holds down to about 0.40× (0.18). Both targets are met at design rates.

**The honest read.** The result turns on the real per-trap landing rate, and the evidence points both ways:

| Measured | Per-trap landing | Scale |
|---|---|---|
| Bridge rev12 batch 2: three traps, each missed 3 of 6 | 0.50 | about 1.0, passed all gates |
| Bridge rev10–12 pre-checks: one trap missed per run from about three | about 0.33 | about 0.7 |
| Frederick rev3 pre-check: 1 of 8 landed, before de-naming | 0.125 | about 0.27, **would fail the cap** |

So a B built with Frederick rev3's placements would probably fail. The placement rules in §5 and the common-word cover are what separate them, and neither is proven for this task. Adding the seventh channel barely moved these numbers, so more traps are not the fix; better placement is.

**Calibration caveats.** Opus 5.5 ledger priors are thin: `done_gap` 0.50 (n_eff 2), `superseding` 0.25 (n_eff 2), `completion_elsewhere` 0.33 (n_eff 1), `exact_predicate` 0.25 (n_eff 2), and none for `house_rule` or `boundary_date`. Exposure counts come from 18 stored runs on other tasks (`exposure_stored_runs_output.txt`), and memory records that exposure moves between revisions. `linear_list_comments` ran 74–942 times per run on the ticket tasks, so Linear comments on in-scope tickets are volume, not a hiding place. That is why FILT's ticket must sit outside the obvious set. `/create-scenario` S9b's pre-registered forecast replaces this sketch.

## 7. Volume plan

Honest necessary calls from the planned cohort, with no padding:

| Phase | Services | Calls |
|---|---|---|
| Discovery and rules: Leonard's DM, rule doc, sheet tabs, PN card and BETA list, live-ops and GDD pages, scope posts, the `#zombie-bugs` PN thread | slack, gdocs, gsheets, trello, confluence | ~24 |
| Census: asks, tickets, PRs, older mail, calendar notes, decks | linear, slack, github, gmail, gcal, gdrive, gslides | ~26 |
| Per record (~24 in scope × ~5: issue, comments, PR reviews, inline comments, Slack search) | linear, github, slack | ~120 |
| Writes: plan sheet (3), new tickets (~8), held-ticket notes (~8), card checklist and items (~11), report (1) | gsheets, gdrive, linear, trello, slack | ~31 |
| Read-backs | gsheets, trello, linear | ~4 |
| **Total** | 11 services | **≈ 205** |

**≥ 500 necessary calls are not reachable without padding.** Julia's runs reached 370–1,215 calls only because about 109 candidate tickets each needed comment reads. This job has about 24 in-scope messages, and growing it to match would be manufactured work. A volume exception is proposed below.

**Platform floor.** Long Horizon needs ≥ 100 counted calls in the golden run. Stored runs made 166–239 service calls on Douglas's 17-ticket register and 109–150 on the bridge send list (raw counts, before removing repeats and errors). The single-object writes (`linear_create_issue`, `linear_create_comment`, `trello_create_check_item`) have no batch form and are the honest lever. Check the pre-check's counted calls at intake.

**Floors the exception does not lower**, with where each stands:

| Target | Plan | Status |
|---|---|---|
| Cohort ≥ 40 × ≥ 3 surfaces over ≥ 2 services | About 48 records looked at: 21 sheet rows, 19 BETA-list cards, about 8 asks. About 24 in scope | **Passes only on the "looked at" reading** Frederick used (46 looked at, 36 in scope). Sheet rows and cards overlap, so the real distinct count needs a census |
| ≥ 10 injected schemas, without Confluence or Snowflake | slack, gmail, gcal, gdrive, gsheets, gdocs, trello, linear, github, gslides | Reachable; each must carry a real role |
| ≥ 120 INSERTs | Estimated 125–150, including companions | **Tight.** Filler records fail on their own, so if honest evidence falls short that is a finding to bring back, not a gap to pad |
| ≥ 12 fragments over ≥ 7 services, 2–4 authorities, ≥ 3 chains, ≥ 12 traps | Rule doc, older store note and roadmap rule as authorities; seven channels plus base chains | To be built at `/create-scenario` |

## 8. Injection plan (rule 3)

- **Census every seeded entity across the whole universe**: every ticket, PR, person and claim, with hits read rather than counted (learnings §10, §38). Absence checks carry a positive control (§35).
- **Date each seed after the base events it relies on**: nothing about the ask point before Sep 25, nothing about the name before Jul 24, nothing on a closed ticket after it closed (§50).
- **Claims about code stay observational**, and `tools/base_claims.py` runs before any solver work (§49).
- **Pair each inline GitHub comment with its Slack copy** in `#zombie-prs` and declare exceptions (§53).
- **No fact only on Confluence or only in a GCal description** (§26; memory: injection-stage-tool-gotchas).
- **Confirm the agent's tools return each seed** in the pre-check, and read the pre-check for fallback events.

## 9. Writes (rule 6)

| Write | Authorized trigger the persona owns | Access proof needed |
|---|---|---|
| Plan sheet in his own folder | Leonard's DM | New file under `d_caafeec2804b3a67ce46aa`, Samuel as owner in both Drive and Sheets rows. `gsheets_create_spreadsheet` has no folder parameter, so it probably needs `gdrive_move_file`; confirm at scenario. **The PN sheet is never a target** |
| New tickets for held messages | Rule doc | Team ZOM; `linear_create_issue` is in the catalog; Linear is unscoped |
| Note on each held message's ticket | Roadmap card rule (the FOLLOW channel) | `linear_create_comment` is in the catalog |
| Checklist items on the PN card | Leonard's DM | `trello_create_checklist` and `trello_create_check_item` are in the catalog. Write success on this board is unproven; confirm in the pre-check |
| Report to Leonard | Leonard's DM | DM `D06L58XCVKK`, YES; `slack_send_message` |

## 10. Decisions for you

1. **Storyline: B**, the Zombie Match beta player messages. **Recommended.** A is the fallback if you would rather have the audience debate, at the cost of a seeded relay into channels Samuel can't see. C is rejected.
2. **Volume exception (GEN §3a).** Honest necessary calls are about 205, below the ≥ 500 floor. Proposed: `volume_exception {call_budget_floor: 200, per_record_floor: 120}` with the reason "about 24 in-scope messages; reaching 500 would need padding, which fails on its own". It needs your `requester_confirmation`. Please also confirm you accept the cohort floor being met on the "looked at" reading.
3. **Review waiver.** `REDTEAM_*` is unset, so the dual red team cannot run. Either set it before `/create-scenario`, or I record `RED TEAM UNAVAILABLE` plus a `RED TEAM FALLBACK:` line naming the two blind sweeps, the whole-universe census and the policy scores. The waiver stays in every Unresolved line until a review or the pre-check covers it (learnings §44).
4. **One repo file outside `hg.py`?** `hg.py` can't open `match3d/Assets/Scripts/Notifications/NotificationManager.cs`. **I recommend allowing that single read-only file**: `/prompt`'s deep recheck reads git, and it would show which messages are really scheduled and whether the old game name is still in the strings. If you say no, truth stays at sheet and PR level, and that check waits for the platform.
5. **Theme screen.** Playbook S0 lists zombies as a screened theme, and all three storylines are on Zombie Match; the base copy itself says "zombie outbreak" and "Plague Race". Evidence it is safe: 12 stored ZM baselines, all led by `claude-opus-5-5` (two also carry 10–13 `sonnet` tags), mention "zombie" 253–1,350 times and "plague" 23–129 times, with 0 `model_refusal_fallback` events. That is the string `difficulty_stats.py` matches, and the same grep finds it in the tool's test fixtures. "Outbreak" appears only 0–6 times, so that word is less tested. **I recommend accepting it**, keeping those words out of seeded text and checking the pre-check for fallback events.

**Next step:** answer the decisions above, then run `/create-scenario`.

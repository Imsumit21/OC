# Pre-scenario analysis: Julia Lawson · Marketing and GTM · Analysis and synthesis (rev 3.1, score-5 target)

Analysis only. This file holds no prompt, Oracle Event or criterion text.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Seed bound 2025-10-01T00:00:00Z.
Assignment: Product · Julia Lawson (Product Manager) · Marketing and GTM · Analysis and synthesis · long-horizon · `difficulty_mode: medium` (unchanged).
Context hash `048d929174496dc6f2066c15a23e50e480ad61b94e618dc7821acaa53b92c142`, source status `ready`, KB `bound`.

## 1. Summary

- **Read `00_Hardness_Deep_Analysis.md` first.** It supersedes section 7 below where they differ (rev 4: a wall, fewer independent parts, K5 moved to a thread reply, K2 and S dropped), and adds two decisions.
- **Target:** `/hardness` score 5, about 300 necessary calls, real six-run average below 70 %. Scores 3–5 all clear the gate, so 5 is margin, not a requirement.
- **Honest odds for one run (reviewer judgement, not measured):** 5 about 25–30 % with the repairs below, 3 or above about 75 %. No stored report has scored above 4.
- **Storyline:** S1, Julia's read on which audience the ZM beta push should target, built from the team's friend sessions, the Playtestcloud panel and retention. It feeds Leonard's later iterate-or-pivot call.
- **What a 4 takes:** one hidden record must break a block across several outputs, including writes that have to be undone. A one-item miss has only ever scored 3 (section 3).
- **Design:** four reversal blocks, each able to **flip the audience answer**, plus side channels. Every session ticket takes a state write, so a miss leaves wrong writes behind.
- **Review:** an independent reviewer predicted a 3 on rev 2 and found four blockers (`00_Design_Review.md`). On rev 3 it found no blocker to starting `/create-scenario`, with three first acts before SQL (section 14).
- **Forecast:** a single run lands at least one reversal block 76–91 % of the time. That is not the same as scoring 4: one block alone is uncertain, two are much safer (39–64 %). The six-run average is 64–71 % on the probe but 75–80 % if the rubric gains 40 weight of easy rows, so **below 70 % depends on keeping the rubric concentrated** (section 8).
- **If the pre-check falls short:** section 9 fixes the moves in advance and caps revisions at two.
- **Your decisions are in section 12.**

## 2. What a 5 needs at each gate

| Gate | What a 5 needs | What it means for this task |
|---|---|---|
| `/injection` | Every seeded fact agrees with the whole universe, chronology holds, ids follow base schemes, no `confluence.*` or `snowflake.*` statement | Check each seeded person and build across all mailboxes and channels. Date each seed after the base event it relies on. Pair each GitHub comment with its Slack copy (INT-01) |
| `/prompt` | Assignment fit, ordinary request, unique ground truth, feasibility, truthfulness, coherence | Keep traps and rules out of the prompt. Close every answer-key fork with a dated record. Relative dates count from Wednesday 1 Oct |
| `/hardness` | You've set 4 as the target: material failures needing substantial correction across the result, with substantial correct work still usable | Section 3 |
| `/oe` | PASS 5: complete, accurate, feasible path | Every Expected value comes from a cited record, never run output |
| `/rubric` | No Major or Moderate issue, weights by kind of work, one fact per row, no fact in three or more rows, zero predicted all-fail rows | Trap rows must be 5-band by nature. Exclusions are graded as exact counts on a required write |
| `/create-difficulty` | Six Opus 5.5 slots, corrected average below 85 %, fewer than 5 full passes, SD 0.1–0.3, at least 2 patterns, at least 100 calls | Design target overrides: E[avg] ≤ 62 %, real average below 70 %. Blocks must split runs, or they lower the mean without adding spread |

## 3. What actually separates a 3 from a 4

From the stored `/hardness` reports (10 unique, this table shows the main ones):

| Report | Score | The miss | Why that band |
|---|---|---|---|
| Julia r5 | **4** | One retrieval miss: 10 of 34 rows wrong, a wrong share, 4 forbidden comments, wrong counts to Leonard | "the correction runs across the whole result" |
| Julia r4 | 3 | 6 extra rows and a wrong DM | "one cause and two outputs" |
| Julia r6, r7 | 3 | One row off, one DM | "nothing has to be deleted or reverted" |
| Douglas | 3 | 2 rows, one count | "the correction is bounded" |
| Robert | 3 | Clash list and one Linear miss | Correction not substantial across the result |
| Julia r1–r3 | 2 | One wording choice | Changed no artifact |

So the requirements are:
1. **Block size is not enough alone.** r5 was 29 % of rows, while r4's 18 % stayed at 3. Blocks here are 15–22 %, so one block is r4-sized and two landing is r5-sized.
2. **Output breadth:** every block reaches the register, the memo figures, the reply to Leonard and the ticket writes.
3. **Reversal:** a miss must leave positive wrong writes. Every session ticket gets a state write, counted or not counted, so a missed block leaves 9–13 tickets to reverse. An omission alone would read as r6/r7.
4. **The answer must move.** Each block is built so keeping it flips which audience rates the game higher. That is what lifts a miss above "bounded and mechanical".
5. **Correct work stays usable for a 4.**

**What a 5 adds.** The eval's band: failures "invalidate the central result/delivery or defeat much of the core task". r5 stayed at 4 because "the central result is not invalidated". A flipped audience answer alone is probably still a 4 (about 15 % chance of 5), because 47–51 of 60 verdicts, retention and the panel stand. **The real route is two blocks landing:** that makes 53–59 % of the counted base invalid and flips the answer. To raise the odds, the audience call is the memo's single decision, and no block depends on another, since linking them would break the spread.

## 4. Julia's reach at the clock

`persona_view reach julia_lawson`: 147 channels, 253 mail threads, 748 calendar events, 28 owned and 158 shared Drive items.

| Surface | Reach | Use |
|---|---|---|
| `#zombie-design` `C090N54TG79`, `#zombie-bugs` `C08R27X0EAH`, `#zombie-match3d` `C0880U9751A` | YES | Anchor and thread roots |
| DMs with Robert `D05GU6L0XFH`, Leonard `D05HB64NMQU`, Frederick `D05SD5QLG94`, Marcus `D05TZ6N1QBH`, Brian `D076RBM29JS` | YES | Hidden carriers. Only Robert's DM has thread roots in the window |
| `#zombie-prs` `C093LEZGF6J` | UNVERIFIED | Mirror only. The PR comment itself is the carrier |
| `#executives`, `#bridge-pitch`, Leonard–Robert DM `D04UP2L3E3S` | **NO** | Nothing load-bearing |
| Playtestcloud mail | **0 visible** | Must reach Julia through a seeded forward |
| GitHub, Linear, Trello, Contacts, Confluence, Snowflake | Unscoped | Confluence and Snowflake are read-only for injection |

Write tools confirmed in the catalog: `gsheets_values_update`, `gsheets_values_append`, `gdocs_create_document`, `gdocs_batch_update`, `slack_send_message`, `linear_create_comment`. Ticket state uses `linear_update_issue`. Julia owns every seeded Sheet and Doc target.

## 5. Storylines

**S1 (recommended): evidence pack for the iterate-or-pivot call.** Leonard's note `C090N54TG79/1758517286.431379` (Sep 22 05:01 UTC, Sep 21 22:01 PT): Playtestcloud at 3–3.5 stars, everyone gathers reactions from "25–45 casual and/or RPG gamer friends (not kids)" with "No coaching", then after 15–20 days of tech-stable data they iterate or pivot. Supporting base: Leonard's order `1758487506.451859`, Robert's four questions `1758569995.343159`, Robert's "I need an average score from player test cloud" `1758581488.969679`, and `USER_COHORT_RETENTION` (51 ZM rows).

- **Work:** Julia consolidates about 60 sessions from about 12 observers, decides which count, reads the panel and retention numbers, closes out the session tickets and tells Leonard and Robert which audience the beta push should target. Base supports this question: audience direction is unsettled (`1759173459.621579`, the Sep 29 debate).
- **Fit:** the memo's single decision is audience and demand (Marketing and GTM), answered by prototype evaluation (Product & Design). The pivot tally is supporting context. Build and QA detail stays evidence, not the deliverable.
- **Base limits:** the clock is day 9 of 15–20 and the beta had not shipped. Leonard sequenced the pivot call after tech-stable beta data, so this is an interim read feeding that call, never the call itself, and seeds never call it beta data. Friend feedback from after the note does not exist in base, so seeded sessions contradict nothing.

**S2 (reserve):** beta push and messaging retention plan. Only 14 rows in the base sheet, and the copy is full of bio-adjacent words.
**S3 (rejected):** creative slate review. It leans towards Growth/UA, and ZM spend cannot be graded (SC-11, SC-12).

## 6. UGT plan

| Fork | Status | How it closes |
|---|---|---|
| "25–45": age or head count | **Settled by base as age** (`D04UP2L3E3S/1758515667.845849`), but Julia can't see that | A seeded Leonard reply says the same |
| Which sessions are stable enough | Open. Leonard's "tech-stable" qualifies the beta, not friend sessions | A dated seeded rule: a device group clears only on a clean QA pass on that device. The ZOM-559 sound bug is not a session blocker, and ZOM-559 stays Todo |
| Store builds only | Open | Part of the same rule record: sessions on dev builds don't count |
| Coached, off-audience | Open | "No coaching" is base. A seeded audience rule says game-industry people don't count. Apply each sentence to each session class. Support: Julia's "They are playing to please us" `1758582083.678989` |
| Pre- and post-tutorial sessions | Open | A seeded rule that **groups** them, a side split only. Excluding would drop nearly all iOS sessions |
| Follow-through and memo access | Open | The seeded ask delegates by owner: Robert sets how not-counted sessions are handled and who gets the memo. Without that chain, `/hardness` gives a miss no credit (`prompt-incorporation-v1`) |
| Log dates | Open | Tickets are dated Sep 30 by the ID floor, so each ticket transcribes a dated observer form. Later records then post-date the form, and the newer-source check favours them |
| Panel average | Open | Define stars per player and how a void is treated. State platform in the seed, since base doesn't map `-3` and `-4` |
| Retention read | Open | Seeded rule in Docs or Slack: install-weighted, mature cohorts |
| Hardcore 1–10 score | Avoid | No record defines it. Don't grade one. Julia's "a solid 6" stays her opinion |
| Audience answer | **Designed, proven on provisional numbers** (`00_PreScenario_Audience_Table.txt`) | Rule to seed: the lead is the higher mean star rating over counted sessions, one audience label per session, at least 6 sessions per audience, a gap under 0.25 means no clear lead, and sessions decide, since panel and retention have no audience cut. Truth: RPG leads 3.83 to 3.38 (n 9 and 8). All 15 miss combinations wrongly put casual ahead by more than the tie band, smallest gap 0.278. Coached and dev-build batches are casual and high, Samsung and industry batches are RPG and low, which fits each story. A first run of the table failed 4 of 15 at a 0.94 true lead, which is why the lead is smaller |
| Ticket states | **Settled** | Counted goes to Done and not counted to Canceled. Both exist on ZOM (427 and 20 issues), and `linear_update_issue` takes `state`. Julia created the tickets, her seeded log note states the mapping, and the prompt will name the close-out as the trigger. A run may comment before or after the state write, and rows must accept both orders |
| Recommendation | Open | Anything on the pivot sits in a stated boundary the rubric accepts in full |

Known-issue cards:

| Card | Disposition |
|---|---|
| SC-8, SC-16, SC-30, SC-32 | Avoid. ZOM-559 stays Todo and is never contradicted |
| SC-1, SC-11, SC-12, SC-23 | No spend or CPI row |
| SC-13, SC-14 | Avoid the BETA list and flags on ZM ROADMAP |
| SC-19 | Name builds as Slack does, never match to `RAW_EVENTS` versions |
| SC-26 | Never inject ENG-2367 or later |
| SC-28, SC-38, SC-44, SC-65 | Avoid OKR numbers, Season Pass ship claims, tutorial funnel, playtime |
| SC-5, SC-6, SC-7, SC-24, SC-36, SC-60, SC-70 | No Victor, Josh Dempsey or Tim. Keep Brian out of Gmail. Don't grade membership. Use calendar zones |

Base facts seeds must respect:
- Don't anchor on Robert's level 3–4 or iPad claim: it is anecdotal and later withdrawn.
- No seed may call crashes the proven churn driver (`1758312927.981069`).
- Don't rewrite real friend feedback. Exclude Leonard's friend (S23 Ultra), or seed that row with exactly the base facts.
- Martin has no sessions Sep 23–25.
- The panel must average 3–3.5 before correction. Leonard also said 2.5–3 in a DM Julia can't see, so a corrected figure below 3 is fine.

## 7. Hardness plan

**Measured carrier rates** (`00_Carrier_Calibration.md`, 30 runs, 5 tasks): PR inline comment 21/30 (but 18/18 on one task and 3/12 on another), unpointed separate mail 41/72, deep channel page 8/18, reply in a mail thread 4/12, channel thread reply 4/18, DM thread reply 4/24. Never or almost never missed: comments on cohort tickets 0/150, Trello 0/36, Doc bodies 0/24, Calendar notes 0/18, date rules 0/12, warehouse 0/6, named-vendor mail 0/78. Almost every miss was a record the run never surfaced, so **placement decides more than cleverness**. Rates rest on few records that survived hardening, so they likely run high.

**Reversal blocks** (disjoint, 43 of 60 sessions, leaving about 17 counted):

| Ch | v2 trap type | Block | Convincing wrong source | Record that beats it (carrier) |
|---|---|---|---|---|
| K1 | #2 Correction elsewhere | 13 sessions: one hosted gathering, one date, no other session by that observer that day | Observer's form says no coaching, transcribed to ticket and log (Linear, Sheets) | Observer's later mail, dated after the form, saying plainly they walked the group through first. It sits among about 15 routine form mails, each sourcing a ticket's form date, because Julia's sparse mailbox would otherwise put it on top (Gmail) |
| K3 | #1 Done across services | 11 Samsung sessions | Ticket closed Done citing a clean pass of the full QA matrix, whose base runbook lists Samsung, so "not cleared" isn't the default reading (Linear) | The same QA owner's inline comment on real PR #463, dated after the close: that pass had no Samsung device. A real missing part, no fix or build claim (GitHub) |
| K4 | #5 Exception in older records | 9 sessions, Brian's batch | Form says RPG and casual gamers (Linear, Sheets). Brian's form is a dated Doc he owns and shares with Julia, with no mail, since `brian.foster@` is the SC-6 address. A Slack notice would point runs at his DM, which would weaken K4 | Unambiguous Turkish line in the Julia–Brian DM, matching 23 of its last 37 messages, naming the batch and saying they work in games. Base hook `1758570425.654109` (Slack) |
| K5 | #7 Outside the filter | 10 sessions | Form and log look complete (Linear, Sheets) | Observer's post in `#zombie-design` around Sep 25, 73–89 parents back, naming the batch's build by id rather than saying "dev build", so a keyword search misses it. Base support: Brian asked which build to send friends (Slack) |

**Side channels:** K2 tutorial split, Android cut in a thread reply (weight 3 only). F re-run request and S memo access in Robert's replies, reached through the ask's delegation. D (panel forward) and C (linked contact) are mandatory reads, so they count as correct work, not traps. E retention is correct work: a miss is unlikely.

**Search collisions:** Slack search returns thread replies, including DM replies, so each carrier gets its own vocabulary. An offline test runs the 15 likeliest queries over the seeded text before any run is spent.

**Weak points to accept:** K3 needs the agent to read inline comments, and rates split sharply by task. K1 and D share the mailbox, though routine mails dilute that. K4 depends on opening Brian's DM at all.

**Part 7 checks** (`00_PreScenario_V2Check.txt`): SAME_PLACE, DONE_CHECK, TWO_DECISIONS, INPUT_CHECK and FILTER_CHECK are CLEAN. RULE_IN_PROMPT is SKIP. DECISION_FLIP flags R_K2, R_C, R_F and R_S, which flip only weight 3. Disposition: all are genuine 3-band work, weights stay, and none counts as a required weight-5 decision. These checks prove structure only.

## 8. Policy scoring (UNCALIBRATED)

Surface: 25 slots, total weight 89, 10 weight-5 rows. Each block can flip 25.8 %, under the half-weight limit. Full output: `00_PreScenario_Policy.txt`.

| Whole policy | Score |
|---|---|
| Log, tickets, notes, warehouse only | 25.8 % |
| Plus every mail | 46.1 % |
| Plus thread replies | 56.2 % |
| Plus inline PR comments | 65.2 % |
| Plus Brian's DM | 74.2 % |
| Perfect | 100 % |

A single block miss scores 74.2 %, so one miss never clears 70 %.

| Rates (ρ = 0.6) | E[avg] | P(< 70 %) | E[avg], +40 easy weight | P(< 70 %) | One run ≥ 1 block | ≥ 2 blocks |
|---|---|---|---|---|---|---|
| Author prior | 64.2 % | 81 % | 75.3 % | 12 % | 87 % | 56 % |
| Measured carriers | 63.5 % | 87 % | 74.8 % | 10 % | 91 % | 64 % |
| Harder case (my reduced rates) | 70.9 % | 46 % | 79.9 % | 1 % | 76 % | 39 % |
| Strong Opus | 82.7 % | 3 % | 88.0 % | 0 % | 50 % | 14 % |

**How to read this:**
- E[avg] ≤ 62 % is not met on any row. The closest are 63.5–64.2 %. I don't see an honest way to reach 62 % on the evidence, and I'd rather say so than tune rates.
- **The rubric is now the biggest lever on the average.** Stored tasks passed 282 of 393 rows 6/6. If easy rows pile up, the average rises 9–11 points. Weights stay by kind of work and nothing gets raised, so the fix is restraint: few rows outside the blocks.
- Padded rows also hurt the gates: P(all gates) drops to 12–47 %, and the strong-Opus row at 88 % would fail even the 85 % cap.
- Only the "≥ 2 blocks" column is a confident route to a 4, and it is the route to a 5.
- The reviewer's own rates, run separately, give 73.7 %, or 81.9 % with 40 easy weight, so it rates below 70 % as still unlikely.
- **Cost of the 5 push:** H1, G1 and G2 need all four blocks, so the chance they fail all six runs can pass .7. Those rows are legal when valid, but their `/create-allfail` reasons must be pre-registered. If every run lands 2–3 blocks, SD can drop below .1. Failure patterns stay safe.

## 9. Not getting stuck: the pre-check plan

Every SQL change costs `/injection`, `/prompt`, a new Opus run and `/hardness`, so moves are fixed in advance and the prompt stays unchanged.

**Before spending a run:** the offline search-collision test, plus a fresh subagent solving from the seeded records alone. These test logic, not findability, and are not evidence of Opus behaviour. Pre-register one probe phrase per deciding record, since subagent reads can be hidden from main-trajectory matching.

| Pre-check result | Next move |
|---|---|
| Score 4–5 | Continue to OE and rubric |
| Score 3, one block landed | Land a second block using its move below. Don't widen the first |
| Score 3, only side channels landed | Treat as no block landed |
| Score 1–2, records surfaced and applied | Apply the moves for those blocks |
| `/hardness` rules a miss a task defect | Fix the rule or chain, never the placement. This is the costliest case, so it comes first |
| Near miss | One same-SQL rerun is allowed as a diagnostic, since it needs no `/injection` or `/prompt`. Never use it to pick the better run |

**Moves, one per block, built as reserves now:**

| Block | Move |
|---|---|
| K1 | Move the statement from mail to the observer's DM with Julia, under a non-session root |
| K3 | Move the comment to a second real PR the ticket doesn't cite |
| K4 | Move the line to a different DM or group DM. It stays after Brian's form date |
| K5 | Move the post to a reply under a non-session root in `#zombie-design` |

**Cap:** two revisions, then I come back to you. The earlier Julia task took seven rounds and still sat near 84 %.
**After baseline:** a 4 followed by an average of 70–85 % passes the Medium gate, so section 12 asks whether that ships.
**Never:** add rows, add steps, raise weights, or put rules in the prompt.

## 10. Volume plan

§3a exception to about 300 necessary calls. Other extreme targets still apply.

| Phase | Calls | Why it is necessary |
|---|---|---|
| Discovery: note, thread, log, workbook tabs | 18 | Sets scope and rules |
| Rules and definitions | 18 | Settles each rule |
| Per-session ticket comments × 60 | 60 | No bulk call returns these |
| Per-session notes doc × 60 | 60 | One read per doc |
| Cross-checks: mail, DMs, contacts, Trello | 36 | Real reconciliation |
| Build check: PRs, reviews | 14 | Channel K3 |
| Warehouse queries | 10 | Retention read |
| Per-session ticket state writes × 60 | 60 | Real close-out, and the source of reversal |
| Other writes and read-back | 24 | Register, memo, reply, follow-through |
| **Total** | **300** | |

Ticket reads no longer count: `linear_list_issues` takes a caller-set `maxDescriptionChars`, so they are replaceable. `linear_show_data` still needs testing at scenario, and each field must live on a named surface so the log can't replace all reads. Floors: `call_budget_floor: 260`, `per_record_floor: 160`. 500 would need about 150 sessions, which is padding.

## 11. Service map and injection notes

- **Carrying weight (11):** Slack, Gmail, Calendar, Drive, Docs, Sheets, Contacts, GitHub, Linear, Trello, Snowflake. Confluence is dropped: it defines nothing we need.
- **Injected (10):** all except Snowflake. Calendar and Trello must carry a real role, not padding. Check they still do at scenario.
- **ID floors:** next ZOM-567, and ZOM-566 was created Sep 30 16:26Z. All 60 session tickets must be dated Sep 30 16:26Z–23:59Z, as Julia's batch log of the week's sessions, so the sessions themselves are dated in the ticket text. Avoid gaps 416, 460, 522, 529. Next PR #478, so no seeded PR. Next Trello idShort 80.
- **Closed tickets:** a seeded comment after close fails, so date seeded notes before any close. The not-counted state must let a run comment after its state write.
- **Inline comment:** `harmonygames-Games/match3d#463#rc_9`, with its `#zombie-prs` mirror under root `1758818922.529299`, dated after the ticket closes. It would be the only human comment on #463, so it needs a reason: #463 hosts the tracking used on the QA pass. No fix, branch or build claim (`tools/base_claims.py` is blocking).
- **Threads:** bump root `reply_count`, `reply_users_count` and `latest_reply` on each seeded reply.
- **Panel forward:** real subject and SVC_2646 sender, dated after Sep 22 03:44, with a copy in Leonard's mailbox. The base mail has no per-player stars, so all 10 ratings are seeded, and the void needs a stated reason. No invented receipt or refund.
- **Observers:** check each author's channel membership. Douglas and Frederick are thin in the window.

## 12. Your decisions

**Accepted by the requester on 2026-11-07 ("accept all"), with my recommendation on each, plus the three decisions in `00_Hardness_Deep_Analysis.md`:** S1 as reframed; volume floors 260 and 160; ZM theme exception; `RED TEAM FALLBACK:` citing the independent subagent reviews; two-revision cap; 62 % as the aim with about 64 % acceptable; ship if `/hardness` clears and the baseline passes the Medium gate; the narrower deliverable; the wall approach with valid all-fail rows; truth reversed so casual leads.

1. **Storyline.** I recommend S1 as reframed: audience read feeding the later pivot call.
2. **Volume floors.** Confirm `call_budget_floor: 260` and `per_record_floor: 160` for your approx 300 calls.
3. **Theme exception.** ZM is the only live product at the clock, and the earlier ZM baseline runs I sampled show only `claude-opus-5-5`. I recommend accepting ZM as a product name and keeping outbreak, infection and plague words out of seeded text.
4. **Red-team waiver.** `REDTEAM_*` is not set. I recommend a recorded `RED TEAM FALLBACK:` citing the independent subagent review, kept visible in every Unresolved line (§44).
5. **Revision cap.** Do you accept two revisions? A 3 or 4 clears the gate, so I would not spend a revision purely to turn a 4 into a 5.
6. **The 62 % target.** No honest row reaches it. Do you accept about 64 % as the design figure, or should I look for more loss before SQL?
7. **Shipping rule.** If `/hardness` is 4 and the baseline average lands at 70–85 %, it passes the Medium gate. Does that ship, or do you want another round?

## 13. Not verified yet

- Every rate in section 8. The stored data covers other tasks.
- Why inline comments were 18/18 missed on Douglas but 3/12 on Julia. K3 depends on which behaviour we get.
- The audience table uses provisional ratings. The solver must re-prove it on the final seeds, and duplicates (channel C) must not change the counted sets.
- `linear_show_data` behaviour.
- Whether a single block reaches a 4. The evidence is one report.

## 14. Independent review

Rev 2 review: `00_Design_Review.md` predicted 3, with four blockers. Repairs: B1 state write on every ticket; B2 K2 demoted to a side channel; B3 stability rule plus a QA-pass gap; B4 dated observer forms. The major and minor findings are folded into sections 5–11.

Rev 3 delta (`00_Design_Review.md`): closed B2, M1, M4, M5, M8, M9, M11. Partly closed B1, B3, B4, M2, M3, M7, M10. Open M6, the shared aggregates, handled by pre-registered all-fail reasons. No blocker to starting `/create-scenario`. All three first acts are now done at design level: the audience rule and number table, Brian's form carrier, and the Linear state mapping (section 6, section 7). The solver must re-prove the table on the final seeded ratings.

Predicted one-run band (reviewer judgement, medium-low confidence): 5 about 20 %, rising to 25–30 % with the repairs and under 10 % if the audience row is ruled ambiguous; 4 about 40 %; 3 about 15 %; 2 or below about 25 %.

Evidence files in this folder: `00_Carrier_Calibration.md`, `00_Base_Feasibility.md`, `00_Design_Review.md`, `00_PreScenario_Probe.manifest.json`, `00_PreScenario_Probe.surface.json`, `00_PreScenario_V2Check.txt`, `00_PreScenario_Policy.py`, `00_PreScenario_Policy.txt`, `00_PreScenario_Audience_Table.py`, `00_PreScenario_Audience_Table.txt`.

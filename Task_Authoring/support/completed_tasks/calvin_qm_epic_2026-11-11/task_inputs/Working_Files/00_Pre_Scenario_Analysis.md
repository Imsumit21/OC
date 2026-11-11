# Pre-scenario analysis: Calvin Price · Engineering · Engineering Ops · Analysis and synthesis (analysis only)

Written 2026-11-10. This file holds no prompt, Oracle Event or criterion text. Every base fact below was read through `Task_Authoring/tools/hg.py` in this session; ids starting `NEW-` are planned seeds that do not exist yet. Supporting files are in `Working_Files/00_PreScenario/`.

**Bottom line.** Storyline A is chosen: the Queue Manager roll-out stock-take (ticket ZOM-543 turned into a real epic). It is Calvin's own live work at the clock, it sits squarely in epic and task management, and the base already holds a believable "done" that another service contradicts. The design is sized to your targets of 2026-11-10: average under 60 %, over 130 calls in every run, largest failure pattern under 50 %. On the sketch surface the model gives an expected average of about 48 % and about 0.84 for all gates at my placement rates. That figure is UNCALIBRATED and optimistic: it falls to 0.40 if my rates are 30 % too high, and to 0.29 and 0.20 on two harsher views (section 6). Only one of our eleven completed tasks has ever averaged under 60 % (`00_Completed_Task_Learnings.md`). The choices you delegated are recorded in section 11.

## 0. Assignment and context (verified)

| Field | Value |
|---|---|
| Persona | Calvin Price, Game Engineer (Unity VFX), `calvin_price`, calvin.price@harmonygames.co |
| Function, competency, skill | Engineering · Engineering Ops · Analysis and synthesis |
| Horizon, mode | Long Horizon · hard (cap: corrected average strictly under 70 %) |
| Your targets (2026-11-10) | Average under 60 % · over 130 counted calls in every run · largest failure pattern under 50 % · every other difficulty guideline |
| Universe | Oct 1, 2025 (synth-cut), build hg4-synth-sep30cut v16 |
| Clock line | `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)` |
| Seed bound | 2025-10-01T00:00:00Z. No seeded event timestamp after it |
| Persona's today | Wednesday 1 October 2025; "yesterday" is Tuesday 30 September |
| Shutdown rules | do not apply. Victor Barnes left in April 2025 and cannot act |
| Context | `task_context.py --write --require-source` returned `ready`; context hash 7be566a0936c |
| Tools | last change to `Task_Authoring/tools` is commit 7302355 (2026-11-08) |

## 1. What a 5 needs at each gate

| Gate | What it checks | What this task must do |
|---|---|---|
| /injection | Seeds against the whole universe: ids, references, dates, lifecycle | Census every person, ticket, PR and build number a seed names. Date each seed after the base event it relies on and before the seed bound. No comment on a ticket after it closed. Brian Foster stays out of Gmail (card SC-6) |
| /prompt | Fit, Unique Ground Truth, feasibility, cross-service coherence, originality | One fair answer per finding, or a boundary the rubric accepts in full. No touched known-data card. Seeded build and branch claims agree with base #builds and git. A short ordinary request that names its destinations |
| /hardness | One unhinted Opus 5.5 run | The run must miss two independent causes, or lose 30 % or more. Three near-certain channels on different carriers and authors give that without relying on luck |
| /oe | Complete, accurate, feasible path | Every expected value quoted from a cited record. No value seen only in run output. No Gmail attachment read |
| /rubric | Atomic, self-contained rows, weights by kind of work | One fact per row. Samples of 5 plus a volume row. No count bundled with an identity. Keep always-pass per-target rows out by making routine writes template-identical |
| /create-difficulty | Six Opus 5.5 slots | Gate: corrected average under 70 %, fewer than 5 full passes, population SD 0.1–0.3, at least 2 failure patterns with the largest at most 50 %, at least 100 counted calls. Your targets on top: average under 60 %, every run over 130 calls, largest pattern under 50 % |

The spread gate is the one this workspace has failed most often: Q4 0.016, Owen 0.029, close-out 0.034, Vincent 0.049, card spend 0.054, Samuel 0.065 and Julia 0.099 all failed; Douglas (0.117), bridge (0.106), Robert LLC (0.103) and handover (0.161) passed. The lessons from all eleven completed tasks are in `00_Completed_Task_Learnings.md`, and section 6 is built around them.

## 2. Calvin's reach at the clock

Source: `00_PreScenario/reach_calvin.txt` (`persona_view.py reach calvin_price`).

| Service | Reach |
|---|---|
| Slack | 107 visible channels (22 public, 31 private, 28 group, 26 direct). 12,017 posts, the last on 2025-09-29 |
| Gmail | 8,142 threads, mostly service senders. 49 threads in September 2025 |
| Calendar | Own calendar only, 442 events, last before the clock 2025-09-29 |
| Drive | Owns 1,918 items (root `d_49b9dfa5208d400d9b3937`); 128 shared with him. Native visible: 54 Docs, 27 Sheets, 5 Slides |
| Linear | `usr_49b9dfa5208d400d`. 356 assigned issues; 25 open (8 ZOM, 4 ART, 1 EPI and 12 old Domino Delights ENG tickets) |
| GitHub | Two logins resolve to him: `PERSON_0003_GITHUB_USERNAME` (email match, author of the PRs below) and `PERSON_2137_GITHUB_USERNAME` (name match only) |
| Trello, Contacts, Confluence, Snowflake | Unscoped. Trello user `ca5bb4c09fbf2a437f04531e` |

Channels this storyline needs, each `can-see` YES: Brian's chat `D0770ET6WBW`, Vincent's chat `D06UPGF5PQV`, the Spanish chat with the Collect & Win owner `D05S1S2H55M`, Julia's chat `D05HYDTG5TJ`, #builds `C05433XK267`, #zombie-prs `C093LEZGF6J`, #zombie-bugs `C08R27X0EAH`, #zombie-match3d `C0880U9751A`, #zm-animations `C09ATAJ220H`, #company-internal `C05KNDCHAAG`. #zombie-design `C090N54TG79` is NO, so nothing load-bearing goes there.

Write tools in the catalog: `linear_create_issue`, `linear_update_issue`, `linear_create_comment`, `gdocs_create_document`, `gdocs_batch_update`, `gsheets_*`, `slack_conversations_add_message`. None has a batch form for Linear, which is what gives honest per-item calls.

## 3. Storylines and recommendation

### A. Queue Manager roll-out stock-take (recommended)

**The real situation.** Brian Foster opened ZOM-543 "Queue Manager" on 15 Sep and gave it to Calvin. It is In Progress, has no sub-issues and no comments. Its description lists six things the system must orchestrate on the main menu. On 17 Sep Brian told Calvin he wanted it ahead of the card animation "if you can complete it by this Friday. When we publish Collect&Win, we'll need to orchestrate the flow" (`D0770ET6WBW/1758125053`).

| Date (UTC) | Record | What it shows |
|---|---|---|
| 24 Sep 23:06 | match3d PR #459 merged by Calvin | Queue for level-end animations, daily gift, season pass, tutorial |
| 25 Sep 13:59 | Brian in `D0770ET6WBW/1758808795` | The input blocker "is not a problem right now", to be checked again once Collect & Win is in the queue |
| 25 Sep 16:25 | #builds: Match 3D iOS Internal #1718 | Built from Calvin's QueueManager branch, not main |
| 25 Sep 17:15 | Vincent in `D06UPGF5PQV`: "Looks ok to me", "Boss arena as well" | QA's word, given on that branch build |
| 25 Sep 22:15 | PR #465 merged | Coin animation replay and queued tutorials |
| 30 Sep 15:53 | PR #472 merged by Arthur | Collect & Win hooked into the queue; touches the reward animation flow again |
| 30 Sep 20:13 | #builds: Android Submission #135 from main | The store candidate |

Julia's note, relayed to Calvin on 2 Sep (`D05HYDTG5TJ/1756838837`), says he struggles with priorities because his tickets are small and scattered. That is the natural reason to turn one loose ticket into an epic.

**The job.** Brian asks Calvin for the state of the roll-out before Collect & Win is published. Calvin hands it over: a write-up in his Drive of where each flow stands and what QA's reports still leave open, ZOM-543 reshaped into an epic (sub-issues for what is left, existing tickets moved under it), and a reply to Brian with the numbers.

**Why it fits.** It is epic and task management on live engineering delivery, by the engineer who owns the ticket. The skill is analysis and synthesis: scattered QA reports, merges, builds and messages become one status picture and a work breakdown.

**Services.** Native: Slack, Linear, GitHub, Docs, Drive, Calendar, Gmail, Trello. Injection adds Sheets and Confluence to reach ten.

### B. Calvin's October queue

Take all 25 of Calvin's open tickets plus asks made only in chat, and produce one ordered plan with stale tickets closed. It fits the competency well. I rank it second because every one of the 25 base tickets is a possible fork (is an eight-month-old Domino Delights ticket still wanted?), and an ordering is subjective unless a rule document fixes it, which is the hub-checklist shape that has leaked before.

### C. VFX handoff turnaround review

Measure how long Marcus's VFX handoffs take to land, using the 131 tickets labelled VFX Integration. Rejected. It touches card SC-15 (the ZOM-521 checklist), SC-30 and SC-32. The hardness guide also cites a task where runs "called VFX work ready", so this storyline is already in the dataset and risks the duplicate check. Every date choice on 131 tickets is a fork.

### Originality

Three submitted tasks of ours use Zombie Match engineering records: Vincent's store-candidate QA gate (the same category and date), Douglas's server sign-off register and Julia's difficulty register. Storyline A shares none of their populations, authorities or deliverables: its population is the main-menu flows and the reports against them, and its output is an epic. It does share build names with Vincent's task (Android Submission #135). I will keep the request about the epic, never about a release gate. The platform's duplicate score cannot be computed here, so this stays a named risk.

## 4. UGT plan (rule 1)

**Two populations, both source-defined.**
- *Flows*: the six items in ZOM-543's description plus each live-op the home screen shows. The description is the list for the first six. The live-ops need a census at `/create-scenario` (code, PR bodies, Brian's records), and Brian's note on the epic then names them, so membership is explicit and not a trap.
- *Reports*: what QA raised against the main-menu flow since #459 merged, about 30 rows. Base reports are loose chat lines ("the input blocker happens after every level"), and counting loose lines forks. So Vincent's reports get a structured home: a seeded QA pass sheet in his voice, one row per finding, with the base chat lines as the same findings in his own words. Reports outside the sheet come in only through a scope sentence of Brian's, and each one is graded on its own row.

**Definitions that must sit in records, not in the request.**

| Term | Planned basis | Fork to close first |
|---|---|---|
| "In the queue" | Merged to main. The merge is the record | A flow hooked on a branch that has not merged |
| "Cleared" | QA's written word on a build cut from main, later than the last merge that touched the flow | The rule needs a home in a real record. Candidate: Arthur Blake, who merges and cuts submission builds. Check his base messages for an existing statement before seeding one |
| "Open report" | Not cleared, and not withdrawn by the person who raised it | Brian's "not a problem right now" on the input blocker: parked, not closed. The definition must give that one answer |
| "Before publish" | The publish review on the calendar | Card SC-13 (beta date in a Trello list name) is near this topic. Use a dated calendar record of Calvin's and never the Trello list |
| "Covered by an existing ticket" | A dated message tying the two names | Each alias must map through a record Calvin can see |

**Rule-sentence sweep (learning §21).** Before any SQL, apply every rule sentence to every flow and every report in a table: rule × item → answer → deciding record → competing rule. Any cell with two answers is a fork to fix. Vincent's task needed six /prompt rounds for lack of this sweep.

**Completeness.** No seeded record claims "all reports" or "every live-op" unless the census proves it. Brian's scope sentence carries a boundary instead (what he does not want counted), and the rubric accepts the boundary in full.

**Base hazards to stay clear of.**

| Card | Hazard | Disposition |
|---|---|---|
| SC-15 | ZOM-521 checklist against its children | Excluded. No seed cites or edits ZOM-521, ZOM-526 or ZOM-528 |
| SC-16 | ZOM-564, 513, 514, 563 open after work shipped | Excluded from both populations. ZOM-564 mentions a tutorial, so the scope sentence must leave it out by rule |
| SC-6 | Mail from Brian Foster's address | Brian acts only in Slack and Linear |
| SC-56, SC-67 | Commit title case; the build #1621 post | Never grade a commit title or build #1621. Grade a build's branch, which the post states outright |
| SC-19 | Telemetry versions against Slack builds | No Snowflake version matching |
| SC-38, 57, 58, 68 | Season Pass ship date, #zm-collect-win, monsters, Boss Arena on prod | Flows are graded only on queue facts (merge, QA word, open reports), never on ship dates or prod state. No post in #zm-collect-win |
| SC-44 | Tutorial events empty in Snowflake | No tutorial funnel |
| SC-30, SC-32 | Parent and In Review states | New sub-issues only; no claim rests on a parent's state |

A blind coherence sweep with the card list in its brief runs before the injection is sealed.

## 5. Hardness plan (rule 4, Hardness v2)

Eight channels on eight carriers, written by seven different people. None can flip more than 16.5 % of the sketch weight. Four are near-certain misses and set the floor for the average; four are lotteries and give the spread. Each lands on its own rows, and each row is multi-source work (weight 5 by kind, never raised).

| Channel | v2 trap type | Convincing wrong source | Record that beats it | Tier |
|---|---|---|---|---|
| BRANCH | 1. Proving done across services | Vincent's "Looks ok to me" and Calvin's "tested already" in their chat (base) | The #builds post: build #1718 came from the QueueManager branch; main then took #465 and #472 | Lottery |
| INLINE | 1. Proving done (second, independent case) | A merged PR whose summary lists the flow | The human reviewer's inline comment that one hook was left out; the review body is silent | Near-certain |
| REOPEN | 2. A correction somewhere else | A report closed out in the QA chat | Vincent's later reply under an unrelated #zombie-bugs post, in player-facing words | Lottery |
| ELSE | 9. Work someone already did | Brian's line that one live-op is still to hook | The feature owner's Spanish message to Calvin plus the merge on GitHub | Near-certain |
| MAIL | 7. Outside the obvious filter | The QA sheet and chat look complete | A report that reached Calvin only by mail | Near-certain |
| FILT | 7. Outside the obvious filter | The same | A report the VFX artist sent Calvin directly in their own 1:1 chat, never ticketed | Near-certain |
| ALIAS | 6. Different names for one thing | No ticket under the epic has that title | An open ticket under the feature's other name (Daily Gift and Daily Login; Win Streak and Nathan's Treasure) | Mixed |
| DATE | 4. Dates and dependencies | The publish day said in chat | The publish review moved on the calendar afterwards; two items change sides | Mixed |

A ninth, the follow-through rule (what each new ticket of Calvin's must carry, from Julia's base note), is held as a spare. The tools take at most eight rules.

**What keeps each channel fair.** Each correction names its item in ordinary words, is dated, and is returned by a natural call for that carrier. No correction sits in the anchor's thread, the epic's own comments, or the record that delegates to it. Brian's ask names what governs by role and lists no locations.

**What past runs say about these carriers.**
- Inline review comments: 0 reads in 12 runs (Owen) and 0 in 6 (Douglas).
- Mail: 0 of 8 runs (Owen); most runs missed the vendor mail (Vincent).
- A chat in another language: most runs missed Brian's Turkish messages (Vincent).
- A 1:1 chat the run was not pointed at: 0 of 12 (Owen). ELSE and FILT both use one, with different people; a run that lists all of Calvin's recent chats could catch both, so they are partly one habit.
- A reply under an unrelated post: between 1 of 6 and 6 of 8.
- Linear comments on listed tickets and the rule owner's own chat: read by almost every run. Nothing deciding goes there.
- Runs sweep the author of the closing rule by date. So no two channels share an author, and Brian writes no correction.

**Open design questions for `/create-scenario`.**
- BRANCH turns on the build's branch, which sits in the bot post's attachment text. Confirm that the agent's Slack history and search calls return that text. If they do not, the channel is confounded by the tool and must move.
- A stated rule plus a done claim is usually caught. BRANCH stays a lottery only if QA's "ok" does not name the build and the build number sits in Calvin's earlier line, as it does in the base today.
- INLINE needs a merged PR with a human inline comment, paired with its #engineering-bots copy (learning §53). Base #459 and #465 carry only CodeRabbit comments, so this is a seeded PR by another engineer, checked against base git.

### Part 7 checks: `hardness_v2_check.py --design` on the pre-scenario sketch

Run on `00_PreScenario/sketch_manifest.json` and `sketch_surface.json`. Output saved as `hardness_v2_check_output.txt`.

| Check | Result |
|---|---|
| SAME_PLACE | CLEAN: 5 traps with two or more version records, 0 flagged, 0 unresolved |
| DONE_CHECK | CLEAN: a done-gap node exists |
| TWO_DECISIONS | CLEAN: cross-source rules decide 4 requirements (R2: BRANCH, INLINE; R3: FILT; R4: ALIAS, ELSE; R5: DATE) |
| DECISION_FLIP | CLEAN: 8 of 8 rules can flip a weight-5 slot |
| INPUT_CHECK | CLEAN: 4 weight-5 totals, each with an input a rule can change |
| FILTER_CHECK | CLEAN: an in-scope item sits outside the obvious filter |
| RULE_IN_PROMPT | SKIP: no prompt yet |

This is a check of the sketch, where seeded containers are declared by me. It runs again on the real manifest at `/create-scenario` S5b and on the SQL at injection.

## 6. Spread and score plan (rule 5 and your targets, UNCALIBRATED)

`00_PreScenario/policy_model.py` scores the 48-slot sketch surface: total weight 182, of which 79.1 % can be flipped by a channel. It tests your targets, not the looser gate: average under 60 %, weakest run over 130 calls, largest pattern strictly under 50 %. Output: `policy_model_output.txt`. Earlier sketches are kept in `superseded_v1/` and `superseded_v2/`.

| Whole policy | Score |
|---|---|
| Perfect | 100 % |
| Takes every "done" and "ok" at face value, stays in the QA chat and the epic | 20.9 % |
| Never opens mail, inline comments or 1:1 chats it was not pointed at; otherwise perfect | 57.1 % |
| Thorough in Slack and Linear; never opens mail, inline comments or threads under other posts | 63.7 % |
| Checks builds; never reads inline comments or mail | 73.6 % |
| English keyword searches only, no calendar | 79.1 % |
| Reads everything it is pointed at; never checks which build QA looked at | 83.5 % |
| Finds every record; files a new sub-issue per item | 91.8 % |

| Single miss | BRANCH | INLINE | MAIL | ELSE | FILT | REOPEN | ALIAS | DATE |
|---|---|---|---|---|---|---|---|---|
| Score | 83.5 % | 84.6 % | 86.3 % | 86.3 % | 86.3 % | 87.4 % | 91.8 % | 92.9 % |

**No single miss and no pair gets a run under 60 %.** Only 7 of 56 triples do. The four near-certain channels together give 57.1 %, so the floor alone is just under your line, and each lottery miss takes a run further down.

Six-run Monte Carlo. Rates are the chance a run misses the deciding record.

| View | Scale × rho | E[avg] | P(< 60 %) | P(SD in band) | Median SD | P(pattern < 50 %) | P(every run > 130) | P(all) |
|---|---|---|---|---|---|---|---|---|
| Placement rates | 1.00 × 0.35 | 47.5 % | 0.94 | 0.90 | 0.164 | 0.99 | 1.00 | 0.84 |
| Placement rates | 0.80 × 0.35 | 57.0 % | 0.64 | 0.94 | 0.187 | 1.00 | 1.00 | 0.60 |
| Placement rates | 0.70 × 0.35 | 61.8 % | 0.42 | 0.94 | 0.191 | 1.00 | 1.00 | 0.40 |
| Placement rates | 0.60 × 0.35 | 66.7 % | 0.22 | 0.94 | 0.190 | 0.99 | 1.00 | 0.20 |
| Bimodal carriers | 1.00 × 0.35 | 47.7 % | 0.88 | 0.45 | 0.095 | 0.61 | 1.00 | 0.29 |
| Ledger family means | 1.00 × 0.35 | 66.9 % | 0.21 | 0.95 | 0.187 | 0.99 | 1.00 | 0.20 |

**Against the targets.** E[avg] ≤ 52 % holds at placement rates only. P(all) ≥ 0.5 holds down to about 0.75×. The assignment's own gate (under 70 %) is far safer: it holds on every placement-rate row down to 0.60×.

**The honest read.**
- Under 60 % is the hard one. It has been reached once in eleven tasks. This plan gets there only if the four near-certain carriers behave as they did on Owen's, Douglas's and Vincent's runs.
- The same kind of model said 60.5 % for Owen's task and the baselines came in at 74–85 %. Placement rates have been too high before.
- The bimodal view (every carrier read by all runs or by none) is the pattern that failed spread on Owen's task. It gives 0.29 here, mostly on spread and on pattern concentration.
- The ledger view uses family means from thin records (three to four trials each) and ignores placement. It still clears the 70 % gate most of the time, but your 60 % line only 0.21 of the time.
- Every always-pass row /rubric adds raises the average. Adding 40 weight moves the headline to 57.0 % and 0.52; adding 70 moves it to 62.1 % and 0.19.

**What I will do about it at `/create-scenario`.**
1. Keep the four near-certain channels on four carriers with four authors, and check each against the stored exposure of real runs before trusting its rate.
2. Give every lottery channel a stated reason to vary inside one batch (a record some natural search words return and others do not, or one past a paging boundary).
3. Keep the rubric lean, near 48 rows: routine writes template-identical so they are sampled, the reply carrying counts and never a member list.
4. Score each placement on both gates together, and compute the spread ceiling from the pre-check's real signature before any baseline.
5. If the pre-check shows a near-certain channel was caught, stop and revise before spending six baselines.

**One pre-check.** A run needs two or more causes, or one cause losing 30 % or more. Under independence that is 1.00 at placement rates, 0.92 at 0.70× and 0.76 at 0.50×.

## 7. Volume plan (over 130 calls in every run)

**The ≥ 500 necessary-call floor is not reachable here without padding**, so a volume exception is taken (section 11). The weakest run is set by writes, so the plan fixes the writes first. The report population is sized at about 30 (the rows of Vincent's QA pass) and the flows at 12, which makes a 42-record cohort and needs no cohort exception.

| Writes that happen in every run | Calls | Why one call each |
|---|---|---|
| One child issue per flow under ZOM-543 | 12 | `linear_create_issue` has no batch form |
| One line in Linear per report: a new sub-issue, or a note on the ticket that already holds it | 30 | The same; this is the answer QA gets on each report |
| Existing tickets moved under the epic, each with a note saying why | 32 (16 × 2) | `linear_update_issue` plus `linear_create_comment` |
| Re-check items for QA, one per flow that needs another look | about 8 | One call per item |
| The write-up, the epic's own text, the reply | 6 | |
| **Total** | **about 88** | A missed report costs one write, so a weak run still makes about 83 |

| Reads | Calls |
|---|---|
| Orientation: Brian's chat, the epic, its comments, Julia's note | 8–10 |
| Per PR (about 6): detail, files, reviews, inline comments, conversation | 24–30 |
| #builds and #zombie-prs for each build QA named | 8–12 |
| QA sheet, QA chat, #zombie-bugs with threads | 12–18 |
| Linear: about 30 related tickets and their comments (`linear_get_issue` returns no comments) | 30–45 |
| Mail, calendar, other 1:1 chats | 6–10 |
| **Total** | **about 90–125** |

Stored ticket tasks made 69–211 reads per run (Robert LLC at the low end, Douglas at the high end). With 83–90 writes the model's weakest of six runs clears 130 in every simulated batch; the lowest plausible run is about 150. The per-report line and the per-ticket note must be template-identical in shape so /rubric samples them (five plus a volume row) and does not add 60 always-pass rows.

No call is added for count. Each write above is something Brian's ask or the epic needs; if the census at `/create-scenario` finds fewer real reports or tickets, I will report the lower figure and not fill the gap.

## 8. Rubric shape plan (no criterion text)

- Target about 48 rows. Planned split on the sketch: about 21 % controls, about 45 % on the four near-certain channels, about 35 % on the four lotteries (some rows are shared). Douglas, the only task under 60 %, had 44.6 % always passed, 29.0 % mixed and 26.4 % always failed.
- Rows that fail every run are legal when valid, and each needs a justification at `/create-allfail`. Expect 15–20 of them, as on Douglas (17).
- Each channel gets three to five rows on different facts (a status, an inclusion, a write, a figure). No channel repeats one downstream effect across many rows.
- Controls are sampled: five flows, five reports, a volume row. No per-target rows for routine sub-issues.
- Exclusions are graded as an exact count on a required write (new sub-issues created), never as "left alone".
- Three aggregates only: flows cleared, reports open, sub-issues created. Each is graded apart from its inputs.
- Rows that join records across services weigh 5. Lookups from one record weigh 1.

## 9. Injection plan (rule 3)

- Census first, for every name a seed uses: Brian, Vincent, Arthur, Julia, the Collect & Win owner, each ticket key, each PR and build number, across all mailboxes and channels, not only Calvin's view.
- Every seed is dated after the base event it relies on (#459 merged 24 Sep 23:06Z, #465 on 25 Sep 22:15Z, #472 on 30 Sep 15:53Z) and before 2025-10-01T00:00:00Z. Nothing may claim a QA result on a build that did not exist yet.
- Build and branch claims are checked against base #builds posts and git before any solver work (`tools/base_claims.py`).
- Companions: a #zombie-prs copy for each seeded PR event, #engineering-bots copies for inline comments, thread counters, Linear `updated_at`, one calendar copy per attendee.
- No rule or fact lives only on an injected Confluence page.
- Findability is proven through the agent's own tools for every deciding record, and the persona view is re-run on the SQL.
- Seeded text uses "ZM" and "match3d". The game's full name carries a theme word that once triggered a model fallback, and any non-Opus-5.5 run is invalid.

## 10. Writes (rule 6)

| Write | Trigger Calvin owns | Access |
|---|---|---|
| Write-up in Calvin's Drive | The request names it; the folder is his | He owns root `d_49b9dfa5208d400d9b3937`. The target folder is seeded with Calvin as owner in both the Drive and Docs rows |
| Sub-issues under ZOM-543 | He is the assignee; Brian's ask calls for the breakdown | `linear_create_issue`; Linear is unscoped |
| Existing tickets moved under the epic, with a note | The same ask | `linear_update_issue`, `linear_create_comment` |
| Reply to Brian | Brian asked him directly | Calvin is a member of `D0770ET6WBW` |

No write goes to a file someone else owns; Vincent's QA sheet is read-only for Calvin by design. No state change on a ticket assigned to someone else unless Brian's ask covers it by name. The pre-check must show each write returning ok.

## 11. Choices made under your delegation

You wrote on 2026-11-10: "you can choose from your self which option is best fit for my requirements in this task". Each choice below is made under that sentence.

| # | Choice | Made | Why it fits your targets |
|---|---|---|---|
| 1 | Storyline | **A, the Queue Manager stock-take** | The only one of the three with a natural done-gap in the base, no touched known-data card, and enough honest per-item writes for 130 calls |
| 2 | Volume exception (GEN_EXECUTION §3a) | **Taken: call-budget floor 200, per-record floor 120** | At least 500 necessary calls are not reachable without padding. 200 keeps the weakest run well over your 130 |
| 3 | Cohort exception | **Not needed** | 12 flows plus about 30 reports is a 42-record cohort |
| 4 | Dual red team | **Waived; a fallback is recorded** | No `REDTEAM_*` reviewer is configured. In its place: the rule-by-item fork sweep, a blind coherence sweep with the known-data card list, and the policy model. "No independent review" stays in every Unresolved line until the pre-check covers it |
| 5 | Design target for the average | **E[avg] ≤ 52 %** | Eight points under your 60 % line |
| 6 | Pattern target | **At most 2 of 6 runs alike** | Your "under 50 %" is stricter than the gate's "at most 50 %" |
| 7 | Friction | **None** | Configured errors and waits are realism only, never a difficulty or call lever |

Risks that stay open: the under-60 % average (section 6), the platform duplicate score against our own ZM tasks, and the spread gate under the bimodal view. If the Opus pre-check comes back with a near-certain channel caught, I will say so and propose a revision before any baseline is spent.

**Next step:** run `/create-scenario`.

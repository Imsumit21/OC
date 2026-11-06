# Pre-scenario analysis: Robert · Executive · Finance · Planning and decision support (analysis only)

Contains no prompt, Oracle Event or criterion text. Written 2026-11-05 for `/create-scenario`; revision 3 the same day,
after the requester's targets and the review of every completed task (§0a, §0b). Revision 2 is kept in
`Working_Files/00_PreScenario/rev2/`. Probabilistic numbers are labelled **UNCALIBRATED**: they are design aids, not
measured rates (learnings §9).

Evidence is in `Working_Files/00_PreScenario/`:
- the reach census, identity resolution and can-see proofs;
- exposure counts from the six stored Opus 5.5 baselines on Robert's own Feb 14 task;
- warehouse revenue sums;
- the v3 sketch manifest and surface, and the Hardness v2 checker output;
- the policy model, the per-run call model and their outputs.

## 0. Assignment and context (verified)

| Field | Value |
|---|---|
| Persona | Robert, Co-Founder & Creative Director, `robert@harmonygames.co` (roster `robert`) |
| Function / competency / skill | Executive · Finance · **Planning and decision support** |
| Horizon / mode | Long Horizon (`effective_profile: extreme`, GEN §3a) · **easy** (V3 cap < 90 %), designed to the **requester's stricter cap < 85 %** (§0a); design target E[avg] ≤ 77 % (cap − 8, playbook S0) |
| Universe | `normal`, hg4-2026-08-31 v37. Eval clock and seed bound both 2026-02-14 00:00 UTC (Fri Feb 13, 4:00 PM PT). Shutdown rules apply |
| Persona today | Saturday, February 14, 2026; "yesterday" is Fri Feb 13 (learnings §20) |
| Source | `task_context.py --task-dir Task_Authoring/task_inputs --write --require-source`: status `ready`, KB `bound`, context_hash `226493b2011a…` |
| Tools | Last `Task_Authoring/tools` commit 58c37b1 (2026-11-03). All universe content was read through `Task_Authoring/tools/hg.py` or `persona_view.py`; the Evals input store was not touched |
| Red team | `REDTEAM_*` is unset (0 variables), so `redteam_review.py --dual` cannot run (§10, decision 3) |

**Clock limits that shape every seed.**
- The Slack export stops at Feb 13 10:03 UTC (NB-6), so seeded Slack messages go before it (Thursday evening to early Friday Pacific).
- After Feb 11 20:40 UTC, Oliver, Owen, Martin and Marcus are single-channel guests in `#prototype` (`C09UHHN6PFZ/1770842566.250369`; NB-1).
- Terminations are backdated to Dec 25, 2025, and Google accounts are archived after Feb 15 (`C05KNDCHAAG/1770839984.194409`).

**What I could not do.** STEP 0.6 (dataset duplicate) cannot be measured locally: `hg_similarity.py` is not in the bundle.
Gmail and Slack attachments return no bytes, so the signed CrazyGames and BoomBit agreements stay unread and ungraded.

### 0a. Requester targets (chat, 2026-11-05)

The requester asked for four things, and left the open choices to me ("you can choose from your self which option is
best fit"):
- learn from the completed tasks, Robert's first;
- more than **130 tool calls in each run**;
- a pass rate **strictly under 85 %**;
- every other difficulty guideline.

This analysis therefore designs to:

| Target | Value used here | Stricter than |
|---|---|---|
| Counted calls (MCP; Bash, errors and exact repeats don't count) | > 130 in **every** baseline run, not only the golden run; design mean ~155, every run ≥ ~140 | V3 Long Horizon ≥ 100 (golden run or average) |
| Corrected weighted average | < 85 %; design target E[avg] ≤ 77 %; aim for a band of about 65–77 % so the SD and all-fail risks stay low | Easy < 90 % |
| Other gates | < 5 full passes; population SD 0.10–0.30; ≥ 2 failure patterns with the largest ≤ 50 %; ≤ 2 errored; no unit of discovery over half the weight; each trap ≥ 2 graded rows and a 30–60 % catch rate; at most one or two near-certain misses | unchanged |

The same requester set targets of this kind on `frederick_q4_commitments` (more than 130 calls per run, average under
80 %). Its runs met the call target (151–212) but failed the SD gate (0.016). Hitting the calls is not enough; the
spread has to be designed too.

### 0b. Learnings from the completed tasks, and what each changes here

Robert's own task comes first: same persona, same date, same easy mode.

| Source | What happened | What this design does about it |
|---|---|---|
| `robert_winddown_closeout` `/prompt` (8 rounds) | Business Function scored 3: "vendor close-out bookkeeping fits Finance / Legal / HR / Ops at least as well" | The job is a founder's strategic call: whether and how to carry a game on through a new LLC, funded by the three founders. Account rows are inputs, never the deliverable |
| same, `/prompt` and `/injection` (10 rounds) | Cross-Service Coherence 2 for several rounds (the P&L costs tab against seeded figures). Seeded comments contradicted the costs tab (Dailybot, UA Assets); one revision edited a base sheet | The P&L sheet is never cited (NB-2). Every seeded amount supersedes a dated record of the same item and agrees with receipts in every mailbox. No base file is edited. A whole-universe vendor census happens before SQL (learnings §10–12) |
| same, `/prompt` UGT 2 | Three unresolved forks and one both-fair figure | §4 settles 12 forks with dated records before `/prompt`; no both-fair figure is graded |
| same, `/oe` (9 rounds) | An amount that sat only in a Gmail PDF; a reviewer's count that was wrong | No load-bearing value in an attachment; every count is verified by a full scan |
| same, baselines | Average 85.7 %, SD 0.034 (fail): about 100 of 136 rows passed every run. Calls 116–143, so it would miss > 130 per run. Measured catches: an `#executives` root 1/6; a GitHub bot comment 0/6; a `#prototype` reply found by name search 4/6; a judgment clash 3/6; a swept-channel clash 6/6 | Few always-pass rows (≤ 5 samples per group). Traps placed at measured ~40–60 % habits. No sole carrier in GitHub. A per-item lever sized for > 130 in the weakest run (§7) |
| `frederick_q4_commitments` | Calls 151–212 (≈ 87 per-entry writes), average 71 %, SD 0.016, 17 all-fail rows. Five items missed 6/6; de-named corrections were caught 0/6 | Corrections keep the item's own name (findable) but sit off the swept path. At most one or two near-certain misses |
| `frederick_bridge_pipeline` | Passed every gate on batch 2: 77.7 %, SD 0.106, 4 patterns. Horizon came from per-entry writes (min 109). Corrections in a DM, a thread under another topic and a calendar-only item discriminated. Builder drift (two rows typed at weight 1) alone would have failed the SD | Same placement recipe. Three or more independent traps, each with ≥ 2 rows. Diff the builder export before the verifier runs |
| `julia_zm_difficulty_baseline` | Judgment-only traps never landed in 28+ runs. One scope choke point left the SD at 0.099 | Every trap has a findable deciding record; no channel is judgment-only. Three to four independent partial-source traps before the first baseline |
| `douglas_beta_server_signoff` | Per-ticket status rows that every run passes flattened the SD. Inline PR comments were never used | The per-issue work is graded as ≤ 5 samples plus one volume row, not one row per issue |
| `frederick_account_handover` | Runs that found every partner notice passed nearly all rows. A second independent hidden authority was needed | Four authorities on separate services: ground rules, warehouse, Arthur's DM figure, the billing note |
| `frederick_card_spend_q3` | SD 0.054; vendors that were findable leaked | Base-grep every injected vendor; spread the catch rates |
| learnings §60–62, memory | Fix Lists copied verbatim passed `/rubric`; count + identity and cross-service order rows are non-atomic | Applied from the first rubric draft |

**Write access proven for Robert.** All six wind-down baselines (as Robert, same universe) succeeded with
`linear_create_comment`, `linear_update_issue`, `gsheets_create_spreadsheet`, `gdrive_share_file` and
`slack_send_message`. Moving a sheet into a Resource-owned folder returned 404 (that task's pre-check). Robert has
**0 Trello actions** (member `3d06b73654d0c8940792514c`; the founders' board went quiet 2025-11-13), so Trello writes
are unproven for him. **Linear is the per-item lever; Trello is not used for writes.**

**Originality constraint.** The neighbours to stay clear of:
- `robert_winddown_closeout`: same persona and date; its job was an account close-out register, a Linear issue settled per account, and two monthly totals;
- `robert-vendor-schedule` (Robert · Finance · Retrieval, Feb 14);
- the L12 "Leonard's vendor list" tasks;
- Frederick's investor send-list tasks.

This design reuses the per-issue Linear mechanics that measurably produce volume for this persona. So the prompt must
describe a different job (§10, decision 5).

## 1. What a 5 needs at each gate

| Gate | What a 5 / PASS needs | Risks specific to this task |
|---|---|---|
| `/injection` | No seed contradicts any base record anywhere in the universe. Seeds are dated after the base events they rely on, and before Feb 13 10:03 UTC for Slack. Schema and id contracts hold. Companions are seeded: one GCal copy per attendee, Drive rows for Docs and Sheets, Linear project, issue and comment stamps. No activity on a closed issue | Hosting, tools and cards already exist in several versions (Q07: AWS ~$1k / $1,550 / $1,485 / 0). Every seeded amount must postdate and agree with the record it supersedes. About 38 seeded candidate issues each need a base-consistent status (the wind-down task's Dailybot lesson) |
| `/prompt` | Fit, UGT, feasibility, coherence; natural voice; originality under 0.80; no rules, traps or answers in the prompt | Fit: a strategic continuation decision, not account bookkeeping. UGT: the 12 forks in §4. Coherence: never ask what NB-3, NB-4, NB-5 or NB-8 answer two ways |
| `/hardness` (one pre-check) | PROCEED (3–5): the run misses weight-5 rows for real reasons | On this persona Opus swept `#winddown` 6/6 and its key threads 6/6. It read `#executives` 1/6 (roots from Feb 11), DMs 0/6, Snowflake 1/6 (list only), GitHub 1/6, Calendar 1/6, and ran per-name Slack and Gmail searches. P(one run catches every trap) ≈ 0.02 at design rates |
| `/oe` | Each step discoverable from the prompt or an earlier step's Expected data, with accurate tools, parameters and values | No attachment reads. The warehouse step names the table and the January filter. Per-issue steps are enumerated, never "the rest" |
| `/rubric` | Atomic "The Agent …" rows; weights by kind of work; ≤ 5 samples per group plus a volume row; no count bundled with an identity; one order row per write kind; no do-nothing rows; no predicted all-fail | learnings §60–62 from the start; Fix Lists copied verbatim |
| `/create-difficulty` | Six Opus 5.5 slots; the V3 gates; plus the requester's < 85 % and > 130 calls in every run | The two Robert/Frederick failures were SD (too many identical rows) and horizon (one run at 116). §6 and §7 size both |

## 2. Robert's reach at the clock

Census output is in `00_PreScenario/reach_robert.txt` and identity in `entity_robert.txt`. Every load-bearing base record
below is YES in `cansee_anchors.txt`.

- **Slack.** 224 visible channels (37 public, 82 private, 66 mpim, 39 IM), 129,939 own posts, last post 2026-02-13.
  - YES: `#winddown` `C0ADGSZKR3R`, `#executives` `C07C2866011`, `#prototype` `C09UHHN6PFZ`, `#company-internal` `C05KNDCHAAG`, `#admin_foundersonly` `C04UEQVDVB7`, `#founders` `C04UTBZL6AX`, the BoomBit channel `C09SWTHEMEW` (channel-level YES).
  - DMs: Leonard `D04UP2L3E3S`, Arthur `D04V95AAAHW`, Oliver `D07H86MV4DN`, Marcus `D05UDNCCFEW`, Julia `D05GU6L0XFH`. DM member lists are unreliable (NB-31), so reach is argued from `can-see`.
- **Gmail.** 16,233 threads and 19,169 messages (2023-03-15 → 2026-02-13). 250 threads have February 2026 mail, mostly cold outreach. Finance notices that do reach him:
  - Deel "payments due" ($9,717.90 for 3 contractor invoices; `robert@harmonygames.co/1855892533860895614`);
  - SVB payment notices (Deel $9,889.90 and Eveline Art S.R.L. $3,720 on Feb 2; `…/1856009245020615882`);
  - App Store Connect TestFlight and review mail for Combo Fighter (1.0.84–1.0.91 in February) and for Domino Delights;
  - the CrazyGames thread copy (24 messages; `…/1847444686342952172`).
- **Calendar.** 1,229 events, last before the clock 2026-02-12 16:30Z (the Sherwood call). Nothing after the clock.
- **Drive family.** He owns 223 items. His root `d_9f7ba94f7526d54d8482ba` is YES (owner), the only proven write home.
  - **Not visible:** the seed papers (Investors' Rights Agreement `f_12bdc5faa19583b4b5138a`, the disclosure schedule `f_2471b5a89bab1b9e97701a`), Leonard's mailbox (Sunset, vendor invoices, Carta) and the Wind Down folder.
- **Unscoped.**
  - Linear `usr_Robert`, with proven writes (§0b); GitHub `EMPLOYEE_0016_GITHUB_USERNAME`; Trello `3d06b73654d0c8940792514c` (0 actions); Confluence `user_EMPLOYEE_0016`; Snowflake.
  - Contacts gives a different title ("Co-founder & Chief Product Officer"); never seed or grade a title.
- **Who is active.** Leonard, Arthur, Robert, Oliver, Owen, Martin and Marcus are all `active_feb_2026` (KB `activity.json`).
- **His remit: this is his decision.**
  - Feb 3: he wants Combo Fighter "self sustaining, so you don't have to make it a side biz" (`C07C2866011/1770084297.911029`).
  - Feb 4: Leonard says Combo Fighter "needs another 3-6 months" (`/1770237771.839399`).
  - Feb 9: the "lifestyle biz" route, "buying its assets under an LLC we own" (`/1770612982.268919`).
  - Feb 11: "we will put our IP to auction and if no one buys it we can buy via our LLC" (`/1770850800.723979`).
  - Feb 12: Leonard keeps "Metabase and dbt until Robert stops caring about combo fighter data" (`C0ADGSZKR3R/1770933903.645709`).
  - Feb 12: Robert tells Oliver "the only thing that's missing is a budget" (`D07H86MV4DN/1770873696.684969`).

## 3. Storylines and choice

| # | Storyline | Fit (Exec / strategy inside Finance) | Reach and data | Originality | Hardness and volume | Verdict |
|---|---|---|---|---|---|---|
| **A** | **The LLC take-over plan for Combo Fighter, March–May.** Leonard lists every Harmony Games item the LLC might take in a Linear project. Robert decides per item what the LLC takes if Sunset can't sell it (Combo Fighter, and Domino Delights only if it covers its own hosting), sets the monthly cash need and the founders' split, records each decision on its issue, and recommends the plan to Leonard and Arthur with the tradeoffs | Strong. A go/no-go on continuing a title, a three-month budget and forecast, founder funding. Robert is the natural owner | Strong. Channels and DMs he reads, the warehouse, his own mailbox, Linear (proven writes) and his Drive root | No Atlas storyline. The LLC thread appears in no stored task. The per-issue mechanics resemble the wind-down task, so the prompt must describe a continuation job | Seven channels from real base forks. Per-issue reads and writes on ~38 candidates give a modelled ~155 calls per run | **Chosen** |
| B | Dissolution notice to stockholders, with the order and holdings | Good: cap table plus investor coordination | Weak. The stockholder list is private to Leonard and Arthur. Robert sees only a summary (Griffin 2,662,255 + Side Fund 84,438 of 3,051,881 Seed shares at $0.9830, `C07C2866011/1768415499.678309` to `/1768418266.528599`). Angels are tokenized, and Leonard owns the task (`C0ADGSZKR3R/1770934638.035469`) | Near the investor send-list neighbours (0.804 precedent) | Volume from per-investor drafts is easy, but the deciding facts would have to be seeded onto papers Robert can't verify | Alternate, not chosen |
| C | Wind-down cash plan for the $22,500 | Good on paper | Already decided by Leonard (`C0ADGSZKR3R/1770927223.969899`) | Lowest: the vendor-list neighbours | Every input is a known card (NB-3, NB-4, NB-5, NB-8, NB-23, Q07) | Reject |

Also screened and rejected:
- the R&D tax credit (payroll-offset only, `C07C2866011/1770780604.709459`);
- Leapblock's ~$600 gesture (`C0ADGSZKR3R/1770922731.444009`);
- Combo Fighter metrics plans (NB-7, NB-9 and NB-26 make levels, Android and sales ungradeable).

**Why A meets the requester's targets.**
- **Fit.** It is a strategic, finance-led decision that Robert owns, which directly answers the wind-down task's Business Function 3.
- **Calls.** The candidate project gives a source-defined cohort of ~38 issues. Each needs its own comment read (`linear_list_comments` has no bulk form) and gets a decision comment and a state. That is the per-item pattern that gave 116–143 calls on 28 issues for this persona, scaled to the > 130-in-every-run target (§7).
- **Difficulty.** The deciding facts sit off the issues, in places Opus visits at measured 40–60 % rates, so the average can land in the 65–77 % band with a healthy spread (§6).

**Base facts behind A (all read through `hg.py`).**

| Fact | Record |
|---|---|
| Lifestyle-biz LLC: buy HG's assets under an LLC we own; DD makes a small amount; team part-time | `C07C2866011/1770612982.268919` (Leonard, Feb 9) |
| IP to auction through Sunset; if unsold, buy via our LLC | `C07C2866011/1770850800.723979` (Feb 11) |
| Combo Fighter needs 3–6 months; self-sustaining; "the only thing that's missing is a budget" | `C07C2866011/1770237771.839399`, `/1770084297.911029`; `D07H86MV4DN/1770873696.684969` |
| DD production AWS "~$1k a month"; "Might be easy to get to 300"; "We make way less than $1K"; not worth keeping the lights up unless BoomBit supports it | `C0ADGSZKR3R/1770680984.725779`, `/1770682219.100789`, `/1770686243.781429`, `/1770686219.875929` |
| Confluence AWS guide (updated 2025-12-31): DD has separate dev and prod accounts; cost note "estimates only" (Fargate ~$650, Aurora ~$420, analytics ~$300, ALB etc. ~$180) | `confluence:page_aws_infra` |
| Warehouse income in `ANALYTICS.MONETIZATION.REVENUE_DAILY`, January 2026: domino_delights $183.11, combo_fighter $7.36, zombie_match_3d $0.00. February is partial to Feb 9. SUM over grain rows | `snowflake_revenue_by_month.txt`; the mirrors agree (KB Q09) |
| Shutdown keep list: Deel, Gusto, Intuit; Figma can't charge before renewal; Linear kept during transition; Metabase and dbt ~$300 a month for a month or two | `C0ADGSZKR3R/1770933601.686309`, `/1770933903.645709` |
| Arthur: moving github, `[USERNAME_30019]` and Metabase to his KubLLC card; repos to "my LLC" with seats for whoever still works | `C0ADGSZKR3R/1770937232.664809`; `C05KNDCHAAG/1770842137.835489` |
| Combo Fighter video campaign: "Budget is $100/day" (Feb 6); "I will keep both campaigns live" (Feb 7); nothing later turns it off | `C09UHHN6PFZ/1770404445.795829`; `C07C2866011/1770489896.754049` |
| Cut-offs: Google archive after Feb 15; DD and ZM off Helpshift before Feb 28; layer.ai until Mar 3; Figma paid until Sep 11; AppsFlyer free up to 15K installs | `C05KNDCHAAG/1770839984.194409`; `C0ADGSZKR3R/1770789534.434749`; `C09UHHN6PFZ/1770837702.167889`; `C0ADGSZKR3R/1770859313.592649`, `/1770932709.222409` |
| Calm Play LLC: "fully owned by Harmony Games" (Nov 30, 2023), a "full subsidiary" (Dec 25, 2023). ZM moved from it to Harmony Games on both stores in July 2025. It still owes a $300 Delaware tax (paid May 15, 2025) and a $125 registered-agent fee (Oct 4, 2025). Leonard (2023): "Calm Play is something we can also use in the future" | `C04UEQVDVB7/1701383740.580749`, `/1703492127.063049`; `C07C2866011/1752548116.304169`, `/1752622453.361899`, `/1752726128.862409`; `C04UEQVDVB7/1747349657.711009`, `/1759615469.061409`; `C04UTBZL6AX/1701126533.617549` |
| Publisher ties: the CrazyGames (MAXFLOW BV) draft, as summarized Nov 17, covers DD and ZM with a 6-month tail (the signed version is PDF-only, never graded); DD "is with boombit" | `C07C2866011/1763421018.863089`; `C09UHHN6PFZ/1770844309.583109` |
| Robert gets App Store Connect review mail for Domino Delights ("Review of your Domino Delights (iOS) submission is complete") | `gmail threads/00015709.json`, `00015817.json` (Robert's mailbox) |

## 4. UGT plan (rule 1)

1. **Population from a record.** Leonard's seeded DM (Thursday night PT, before Feb 13 10:03 UTC) asks for the plan and points to the LLC project in Linear. The project holds one issue per candidate item, seeded by Leonard with his and Arthur's notes.
   - The ground rules define what counts: everything that still bills each month for a game the LLC takes.
   - Completeness is claimed only over a census of those charges (learnings §23). An item the project lacks gets a new issue (the FILT channel). Anything else goes to Monday as a question.
2. **One closed decision set, plain definitions, outside the hub and the issues.** A seeded ground-rules record holds:
   - the take test (a game comes over if January's income covers its own hosting; Combo Fighter comes over regardless);
   - the window (March 1 – May 31);
   - the costing rule (what an item bills now, per whoever runs it);
   - the vehicle (the new LLC; anything Harmony Games owns comes to it only through Sunset's sale);
   - the split rule (equal thirds of the cash need; what a founder already pays personally counts toward that share);
   - the states each issue ends in.

   No item-level resolver goes here (memory `hardness-opus-sweep-pattern`).
3. **Every graded value comes from a record:** a warehouse sum, a dated statement, a base cut-off. No figure is estimated by the agent.
4. **Forks to settle with dated records before `/prompt`:**

   | Fork | Settled by |
   |---|---|
   | Which LLC: "an LLC we own" vs Arthur's KubLLC vs Calm Play LLC | ground rules name the vehicle; Calm Play is HG-owned (2023 records), so it goes through Sunset (the EXC channel) |
   | Window: "3–6 months" vs "a month or 2" | ground rules: March–May |
   | DD in or out ("small amount of money" vs "not worth keeping the lights up") | take test plus January warehouse income |
   | Hosting figure (Q07) | Arthur's dated statement of what the trimmed DD account bills now, made authoritative by the costing rule |
   | Income month and grain | ground rules name January; the table comment says SUM |
   | Campaign still running, and its rate | a dated status record after Feb 7 |
   | Metabase, dbt, GitHub: HG's ~$300 vs Arthur's card | Arthur's dated completion note with the amount |
   | DD player support: "email now" vs the store build | the dated App Store Connect notice |
   | Leonard's participation and any cap | dated hub sentence (his Jan 6 "$25K" was for the recap, now stale) |
   | People costs | out of scope by the hub (NB-15 and the Dec 25 backdating) |
   | Each of the ~38 candidate issues | its status from base records, applied by every rule sentence (§4.5); the census must match the base for every vendor (the wind-down Dailybot lesson) |
   | Unity licence for builds | not graded (Q07 Unity amounts) |

5. **Apply each rule sentence to every issue** in a fork sweep before SQL (learnings §21–22).
6. **Keep off the graded path:**
   - NB-2, NB-3, NB-4, NB-5, NB-8: no P&L-sheet costs, cash balances, February paid-vs-accrued or Helpshift amounts.
   - NB-6, NB-1: no Slack after Feb 13 10:03 UTC; no channel access after Feb 11.
   - NB-7, NB-9, NB-11, NB-26: no Combo Fighter levels, Android, GDD status or sales.
   - NB-12: no tokenized vendor; `[USERNAME_30019]` is spelled out by a seed.
   - NB-21, NB-29, NB-31: no version-to-build joins, no shutdown date as a window start, no access argued from DM members.
   - KB hazards: Q07 (resolved by the costing rule), Q08 (no CPI), Q09 (mirrors agree), L13 (work after the announcement is relied on, never graded), I03.
7. **Two blind sweeps before `/injection`** (memory `blind-sweeps-catch-base-contradictions`), by fresh agents restricted to `hg.py`: a fork sweep from persona-visible dumps, then a seeded-versus-base coherence sweep over the full base, including Leonard's and Arthur's mailboxes.

## 5. Hardness plan (rule 4, Hardness v2)

Seven channels.
- **Four are cross-source decisions on distinct v2 trap types** (1, 2, 7, 9), and a fifth, EXC, is trap 5. Each names the convincing wrong source and the record that beats it, and moves ≥ 2 rows including a weight-5 row.
- **AUTH** is a rarely-opened authority.
- **DATE** is trap 4, but it moves only weight-3 rows (see the FLAG).

The convincing wrong source usually sits on the candidate issue every run reads (believable and easy to find). The
beating record sits off the issues, at a measured habit rate. Each channel is reached by a different habit (no shared
behaviour), so the traps fail independently. `NEW` marks a planned seed, not yet checked against the whole universe.

| Channel | v2 trap | Convincing wrong source | Record that beats it | Rows it moves | Placement (measured) | Prior |
|---|---|---|---|---|---|---|
| CORR | 2 · correction elsewhere (A11) | DD-hosting issue: Leonard's note "~$1k, Blake thinks 300", which echoes `#winddown` Feb 9–10 and Confluence's estimate | NEW Arthur reply in his DM with Robert, under a root about something else (Feb 13): what the trimmed DD account bills now | DD decision 5, DD hosting 5, March cash need 5, split 3, recommendation 3 | DMs were read 0/6, but name searches cover DMs; a named reply off the swept path was caught 4/6 | 0.40 |
| FILT | 7 · outside the filter (A17) | The project's issue list and the `#winddown` keep list read as every monthly charge | Base `#prototype` Feb 6 ($100/day) and `#executives` Feb 7 (kept live), plus a NEW dated status after Feb 7 | Campaign line 5, new campaign issue 5, March cash need 5, split 3, tradeoff 3 | `#executives` read 1/6; `#prototype` history 1/6. Found by a run that asks what else bills Combo Fighter | 0.55 |
| COMPLETE | 9 · work already done (A25) | Metabase issue: Leonard's "~$300/month, needs a payer"; Arthur's future-tense `#winddown` post | NEW Arthur billing-switch note: the description of a Feb 13 calendar event, with a ● copy in his short email to Robert and Leonard. It says the three bill his card and he carries them through May as his part | Cash-need scope 5, Arthur's share 5, March cash need 5, Metabase issue 3, shares in reply 3 | Calendar 1/6 here and 3/7 on Frederick runs; Gmail is searched 10–25 times per run by name. A different habit from CORR (DMs) and FILT (channel history) | 0.40 |
| DONE | 1 · proving done (A24) | DD player-support issue: NEW Arthur comment "done, support goes to email now" | NEW App Store Connect notice in Robert's own mailbox (Feb 13), worded by date: the DD submission carrying the change was rejected, so the live build still opens Helpshift past Feb 28 | Support-release step 5, reply names it 3 | Robert's mailbox already holds DD review mail. Moved out of GitHub (0/6 on this persona) | 0.50 |
| EXC | 5 · rule hidden in older records (A15) | Calm Play issue: NEW Leonard comment "use Calm Play as the LLC? it already has the Singular org and an Apple team" | Base Nov 30 and Dec 25, 2023: Calm Play is a full subsidiary of Harmony Games. The ground rules say HG-owned items come only through Sunset | Vehicle 5, Calm Play issue 3 | A "calm play" search returns the 2023 notes in `#admin_foundersonly` (read 0/6) and `#founders`; the issue makes the search natural | 0.40 |
| AUTH | rarely-opened authority (A13) | "We make way less than $1K"; BoomBit's "retention looks a lot better"; February's partial month | `REVENUE_DAILY` January sums (DD $183.11, ZM $0.00), named by role in the ground rules | DD decision 5, ZM left 3, DD income 3, recommendation 3 | Snowflake 1/6 with no pointer; the ground rules point to it by role, so what remains is the month and grain | 0.30 |
| DATE | 4 · dates and windows (A4) | Steps dated anywhere in March | Google archive after Feb 15; Helpshift by Feb 28; layer access to Mar 3 | Step dates (3 each) | Feb 15 and Feb 28 are swept; Mar 3 is in `#prototype` ("layer" searched 2–3/6) | 0.35 |

**Controls and decoys** (learnings §41):
- about 25 routine candidate issues decided straight from their own notes or base records (Figma $0 to Sep 11; Helpshift, layer, Soundly, Cursor, CodeRabbit and Zapier cancelled; Unity Pro terminated; ZM left with Sunset; attribution on the free tier);
- the one-off "$100 we have" Unity playable (`C09UHHN6PFZ/1770845002.610529`), which is not monthly;
- Leonard's Jan 6 $25K pledge (stale), the Confluence estimate, and the BoomBit optimism;
- routine Deel and SVB notices that agree with the records.

Finding a record about an item never marks a trap by itself.

**Independence and share.**
- Distinct root causes: A11, A17, A25, A24, A15, A13, A4.
- CORR and AUTH meet only on the DD decision row; each also has its own rows.
- The largest units (CORR, FILT, COMPLETE) each decide 25.3 % of the sketch weight (24 of 95), under half.
- No correction sits in the hub, an anchor, the superseded record's container or a delegating record's container. The hub and the project delegate by role.

**Survives complete retrieval.** CORR, COMPLETE, EXC and AUTH need a rule applied across two records even after
everything is read: the newest figure must outrank the estimate, and a subsidiary is not the founders' own. FILT and
DONE are retrieval-shaped and depend on placement, which is why their priors differ.

### Part 7 checks: `hardness_v2_check.py --design` on the v3 sketch

The sketch (`00_PreScenario/sketch_manifest.json` + `sketch_surface.json`, v3) is **not** the `/create-scenario` manifest
or surface. Output, verbatim (`hardness_v2_check_output.txt`):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      2 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 4 requirements: {'R3': ['CORR'], 'R1': ['AUTH', 'EXC'], 'R4': ['COMPLETE'], 'R2': ['DONE']}  [Part 5 rule 1]
  FLAG       DECISION_FLIP   6 of 7 rules can flip a weight-5 slot; not: ['DATE']  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     3 weight-5 total(s); 3 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']

Flags (each needs a written disposition; redesign the difficulty, never weaken a fairness link or raise a weight):
  DECISION_FLIP DATE: rule DATE (A4) can flip slots of weight [3], no weight-5 slot
```

**Dispositions.**
- **DECISION_FLIP DATE.** Kept as a weight-3 complexity channel, not counted among the v2 decisions. Dating a step against a cut-off is interpretation, so raising the weight would break the work-kind rule. `/create-scenario` gives it a money consequence or drops it if the rule budget (k ≤ 8; seven rules now) runs short.
- **FILT's two Slack containers.** The tool counts FILT as single-service, so TWO_DECISIONS lists four requirements. That is enough.
- **Weak evidence.** CLEAN only covers the containers I declared. Re-run on the SQL; RULE_IN_PROMPT re-runs once a prompt exists.

## 6. Spread and score plan (rule 5, UNCALIBRATED)

`00_PreScenario/policy_model.py` scores the v3 sketch surface:
- 33 slots, total weight 95, 85.3 % flippable;
- the requester cap of 85 %;
- a Gaussian-copula run latent and 3 % base slips.

Output: `policy_model_output.txt`.

| Whole policy | Score |
|---|---|
| Perfect | 100 % |
| Linear project and `#winddown` only (issue notes and `#winddown` figures as final) | 14.7 % |
| Every Slack channel, DM and issue, nothing else | 51.6 % |
| Thorough except Feb `#prototype` / `#executives` history | 68.4 % |
| Thorough except DMs | 74.7 % |
| Right calls, never searches mail or calendar by tool name | 74.7 % |
| Thorough except the warehouse | 85.3 % |
| Thorough except store notices in the mailbox | 91.6 % |
| Takes issue comments about Calm Play at face value | 91.6 % |
| Thorough, dates steps loosely | 93.7 % |

| Single miss | CORR | AUTH | FILT | COMPLETE | DONE | DATE | EXC |
|---|---|---|---|---|---|---|---|
| Score | 74.7 % | 85.3 % | 74.7 % | 74.7 % | 91.6 % | 93.7 % | 91.6 % |

- Three single misses (CORR, FILT, COMPLETE) take a run under 85 % alone.
- AUTH, DONE, DATE and EXC need a second landing.
- Two pairs stay at or above 85 %: DONE + DATE (85.3 %) and DATE + EXC. Both include the weight-3 DATE channel.
- P(one run catches every trap) ≈ 0.02, so E[full passes of 6] ≈ 0.13.

Six-run Monte Carlo at design landing rates: CORR 0.40, AUTH 0.30, FILT 0.55, COMPLETE 0.40, DONE 0.50, DATE 0.35, EXC 0.40 (mean 0.41, 2.9 per run).

| Landing scale × rho | E[avg] | P(< 85 %) | P(SD 0.10–0.30) | P(< 5 full) | P(patterns) | P(all gates) |
|---|---|---|---|---|---|---|
| 1.00 × 0.30 | 58.4 % | 1.00 | 0.91 | 1.00 | 1.00 | 0.91 |
| 0.80 × 0.35 | 66.1 % | 0.97 | 0.91 | 1.00 | 1.00 | 0.88 |
| 0.70 × 0.35 | 70.0 % | 0.94 | 0.91 | 1.00 | 0.99 | 0.86 |
| 0.60 × 0.35 | 73.9 % | 0.88 | 0.92 | 1.00 | 0.99 | 0.81 |
| 0.60 × 0.60 | 74.8 % | 0.81 | 0.74 | 0.99 | 0.98 | 0.59 |
| 0.50 × 0.35 | 78.0 % | 0.77 | 0.91 | 0.99 | 0.98 | 0.72 |
| 0.40 × 0.35 | 82.1 % | 0.61 | 0.87 | 0.99 | 0.96 | 0.58 |
| 0.35 × 0.35 | 84.2 % | 0.51 | 0.84 | 0.98 | 0.95 | 0.49 |

**Targets against the requester's cap.**
- E[avg] ≤ 77 % holds down to about 0.53× (about 1.5 traps landing per run).
- P(all gates) ≥ 0.5 holds down to about 0.36×.

**The honest read.**

| Measured | Traps landing per run | Scale on this sketch |
|---|---|---|
| Robert wind-down baselines (same persona and universe): 2.67 of 5 per run | about 0.53 per trap | about 1.0 → ~58 % |
| Frederick bridge rev12 batch 2: three traps each missed 3/6 | 0.50 per trap | about 1.0 |
| Frederick bridge rev10–12 pre-checks: about one per run | about 0.33 per trap | about 0.35 → ~84 % |

At this persona's measured rate the average sits near 58–66 %. That is well under the cap, with P(SD) about 0.9. The
remaining risk is the low end, where Opus catches nearly everything: at 0.35× the cap holds only about half the time.

Hedges `/create-scenario` must keep:
- **Placement.** Keep each beating record at a measured ~40–60 % habit, and keep the habits different (DM, channel history, mail/calendar, warehouse, older channels).
- **Rows.** Every trap keeps ≥ 2 rows. Routine issues stay at ≤ 5 samples plus one volume row, so the always-pass weight stays low (14 of 95 here).
- **Calibration.** Read the pre-check against these priors before the baseline (memory `hardness-opus-sweep-pattern`).

**All-fail watch.** The March cash need passes a run only when CORR, FILT and COMPLETE all fail to land (0.60 × 0.45 ×
0.60 ≈ 0.16), so P(it fails all six) is about 0.35. A VALID all-fail is legal with a justification, but it lowers the
SD. `/create-scenario` should consider grading the March need through its inputs only.

**Revision history.** Every revision is kept in `00_PreScenario/rev2/` and its outputs.
- v1: three totals and two share rows off the same inputs; one CORR miss gave 62 %.
- v2: de-coupled, DONE moved out of GitHub.
- v3:
  - the 85 % cap;
  - the Linear candidate project (the per-item lever);
  - EXC (Calm Play);
  - COMPLETE's copy moved from `#prototype` into mail, after a first v3 run showed it shared a habit with FILT (that policy scored 51.6 % with three landings).

**Calibration caveats.**
- Opus 5.5 ledger priors are thin: `superseding` 0.25 (n_eff 2), `exact_predicate` 0.25 (n_eff 2), `completion_elsewhere` 0.33 (n_eff 1), `done_gap` 0.50 (n_eff 2), and none for `boundary_date` or `house_rule`.
- Exposure moves between revisions.
- `/create-scenario` S9b's pre-registered forecast replaces this sketch.

## 7. Volume plan (requester: > 130 counted calls in every run)

`00_PreScenario/volume_model.py` models per-run counted calls from the measured habits on Robert's wind-down task (UNCALIBRATED):

| Phase | Services | Calls per run |
|---|---|---|
| Discovery and rules: the DM, the ground rules, `#winddown` (3 pages), threads, Feb `#executives` / `#prototype`, `#company-internal`, the Arthur and Oliver DMs | slack, gdocs | 14–24 |
| Warehouse: list, describe, January query | snowflake | 2–6 |
| Linear project meta (team, project, states) | linear | 2–4 |
| **Per candidate issue (36–40): read its comments, write the decision comment, set its state** | linear | **~95–120** (reads 82–100 % of issues as measured; one comment each; states on 55–100 %) |
| New issue for each item the project lacks (the campaign) | linear | 0–2 |
| Off-issue checks: name searches in Slack and Gmail, the calendar, GitHub, Drive, Confluence | slack, gmail, gcal, github, gdrive, confluence | 10–28 |
| Plan sheet: create, move, two shares, value updates, read-back | gsheets, gdrive | 5–8 |
| Reply | slack | 1 |
| **Modelled total** | 11 services | **mean 155, p5 140, p95 171**; P(one run ≤ 130) = 0.002; **P(all six > 130) = 0.99**; median six-run minimum 144 |

**No padding.** Each issue is a distinct item Leonard listed. Each comment read answers that item's own question, with
no bulk alternative (Ask_Carriers §3: `list_issues` omits comments). Each write is one the hub asks for (a decision and
a state per candidate). The measured habit: one `linear_create_comment` per issue in 6/6 runs, and
`linear_list_comments` on 23–28 of 28.

**Risks to the call target.**
- A run that skips state changes on unchanged issues drops about 15 calls; the model includes that.
- Fewer than ~34 candidates would push the p5 under 135. Keep the cohort at 36–40 honest items. The base names about 45 candidates for scenario to census: the keep list and `#winddown` cancellations, Arthur's card moves, the AWS accounts in the Confluence guide, the store listings and developer accounts, the repos, the campaigns, the two publisher ties and Calm Play LLC.
- Read the pre-check's counted calls at intake. If it is under ~140, add per-entry work tied to a real ask, never padding.

**The ≥ 500 floor is still not reachable** without padding. A volume exception is recorded in §10 (decision 2).

**Floors the exception does not lower**, with where each stands:

| Target | Plan | Status |
|---|---|---|
| Cohort ≥ 40 × ≥ 3 surfaces over ≥ 2 services | 36–40 candidate issues plus the item outside the list, about 50 looked at. Surfaces: the issue comments, off-issue base records, the warehouse or mail | Passes on the "looked at" reading; at least 3 surfaces only for the trap members |
| ≥ 10 injected schemas, without Confluence or Snowflake | slack, gmail, gcal, linear, gdocs (ground rules), gdrive (companion rows), gsheets (Leonard's stale Feb 10 draft budget, an A1 wrong summary), github (a control note on the Combo Fighter repo), contacts, trello (a read-only pointer card on the founders' board, never a write target) | **Tight.** github, contacts and trello need real roles or the floor is short |
| ≥ 120 INSERTs | ~38 issues + ~45 comments + lifecycle rows + DMs, mail, calendar copies and docs: about 130–170 | **Reachable** now that the candidate project exists |
| ≥ 12 fragments over ≥ 7 services, 2–4 authorities, ≥ 3 chains, ≥ 12 traps | Authorities: ground rules (gdocs), warehouse, Arthur's DM figure, billing note (gcal + gmail). Seven channels plus about ten decoys and four supersessions | Fragments over 7 services is tight; the rest reachable |

## 8. Injection plan (rule 3)

- **Census every seeded entity across the whole universe**, including Leonard's and Arthur's mailboxes: every vendor on a candidate issue, KubLLC, Calm Play, Metabase, dbt, GitHub billing, the campaign, DD support, Helpshift and the App Store notices. Read the hits; give every absence check a positive control (learnings §10, §35, §38; the Dailybot lesson).
- **Date each seed after the base events it relies on and before Feb 13 10:03 UTC** for Slack:
  - Arthur's figure after `1770682219.100789`;
  - the billing note after `1770937232.664809`;
  - the campaign status after `1770489896.754049`;
  - the support claim after `1770789534.434749`;
  - the project and its issues after `1770933601.686309` (the "linear we keep during transition" line).
- **Tokens**: spell out `[USERNAME_30019]`; keep BoomBit's token off graded rows (NB-12).
- **Carriers**: no fact only on Confluence, in a GCal description or in an attachment. The billing note's ● copy is the email; Snowflake is base-only.
- **Companions**: GCal copies per attendee; Drive rows; Linear project, issue and comment stamps; no activity on a closed issue (learnings §50).
- **Confirm the agent's tools return each seed** in the pre-check, and read it for fallback events.

## 9. Writes (rule 6)

| Write | Authorized trigger | Access proof |
|---|---|---|
| LLC plan sheet in Robert's own folder | Leonard's DM | New file under `d_9f7ba94f7526d54d8482ba`, Robert the owner in the Drive and Sheets rows. `gsheets_create_spreadsheet` then `gdrive_move_file` (proven create; the move goes into his own root, never a Resource folder) |
| Share it with Leonard and Arthur | Leonard's DM | `gdrive_share_file` (proven 6/6 as Robert); the role pinned by the hub |
| Decision comment and state on each candidate issue | Leonard's DM, which names the project, plus the ground rules' states | `linear_create_comment` and `linear_update_issue` (proven 6/6 as Robert on this universe) |
| New issue for the item the project lacks | the ground rules (anything still billing a taken game) | `linear_create_issue` (in the catalog; seen once in the wind-down runs; confirm it returns ok in the pre-check) |
| Reply to Leonard, with Arthur informed | Leonard's DM | `D04UP2L3E3S` YES; `slack_send_message` in the hub thread (proven 6/6) |

## 10. Decisions (made under the requester's delegation, 2026-11-05)

1. **Storyline: A**, the LLC take-over plan for Combo Fighter, March–May, using the Linear candidate project as the per-item surface. B and C are not pursued.
2. **Volume exception (GEN §3a): `volume_exception {call_budget_floor: 150, per_record_floor: 100}`.**
   - **Reason:** "36–40 candidate items; the per-issue read, decision and state give about 155 honest calls per run; reaching 500 would need padding, which fails on its own."
   - **requester_confirmation:** the requester's 2026-11-05 chat set "over 130 tool calls in each runs" and delegated the choice ("you can choose from your self which option is best fit").
   - The cohort floor is met on the "looked at" reading.
3. **Review waiver:** `REDTEAM_*` is unset.
   - Section 13 will record `RED TEAM UNAVAILABLE` and a `RED TEAM FALLBACK:` line. The fallback is the two blind sweeps by fresh `hg.py`-only agents (fork, then coherence), the whole-universe census, and the policy and volume models.
   - It stays in every Unresolved line until a review or the pre-check covers it (learnings §44).
   - If you set `REDTEAM_*` before `/create-scenario`, the dual review runs instead.
4. **Theme screen: accepted with mitigation.** Zombie Match appears only as a title left with Sunset. Samuel's check of 12 stored ZM baselines found 0 refusal fallbacks. Seeds say "ZM", keep "zombie" and "outbreak" out of seeded text, and the pre-check is read for fallback events.
5. **Neighbour risk at STEP 0.6.** The prompt will ask for funding a continuation: what the LLC takes, what it costs, who puts in what, recorded on Leonard's candidates. It will not use the wind-down vocabulary ("register", "close-out", "accounts", "settle each issue", "two monthly totals"). The score can only be read on the platform.
6. **Requester targets bound into the design:** > 130 counted calls in every run (modelled p5 140) and an average < 85 % (design target ≤ 77 %), alongside every other V3 and Evals gate (§0a).

**Next step:** run `/create-scenario`. It will turn this sketch into the draft manifest, the gradable surface and the
design dossier, then run the blind sweeps (§4.7) before any SQL.

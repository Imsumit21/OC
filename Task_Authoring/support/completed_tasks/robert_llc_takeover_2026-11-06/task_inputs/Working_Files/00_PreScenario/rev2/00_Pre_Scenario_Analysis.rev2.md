# Pre-scenario analysis: Robert · Executive · Finance · Planning and decision support (analysis only)

Contains no prompt, Oracle Event or criterion text. Written 2026-11-05 for `/create-scenario`.
Probabilistic numbers are labelled **UNCALIBRATED**: they are design aids, not measured rates (learnings §9).
Evidence is in `Working_Files/00_PreScenario/`: reach census, identity resolution, can-see proofs, exposure counts from
the six stored Opus 5.5 baselines on Robert's own Feb 14 task, warehouse revenue sums, the sketch manifest and surface,
the Hardness v2 checker output, the policy model and its output.

## 0. Assignment and context (verified)

| Field | Value |
|---|---|
| Persona | Robert, Co-Founder & Creative Director, `robert@harmonygames.co` (roster `robert`) |
| Function / competency / skill | Executive · Finance · **Planning and decision support** |
| Horizon / mode | Long Horizon (`effective_profile: extreme`, GEN §3a) · **easy**: corrected weighted average < 90 %; design target E[avg] ≤ 82 % |
| Universe | `normal`, hg4-2026-08-31 v37. Eval clock and seed bound both 2026-02-14 00:00 UTC (Fri Feb 13, 4:00 PM PT). Shutdown rules apply |
| Persona today | Saturday, February 14, 2026; "yesterday" is Fri Feb 13 (learnings §20) |
| Source | `task_context.py --task-dir Task_Authoring/task_inputs --write --require-source`: status `ready`, KB `bound`, context_hash `226493b2011a…` |
| Tools | Last `Task_Authoring/tools` commit is 58c37b1 (2026-11-03). All universe content was read through `Task_Authoring/tools/hg.py` or `persona_view.py`; the Evals input store was not touched. Samuel's analysis supplied the format and the model code only; no fact was carried over from it |
| Red team | `REDTEAM_*` is unset (0 variables), so `redteam_review.py --dual` cannot run (decision 3) |

**Clock limits that shape every seed.**
- The Slack export stops at Feb 13 10:03 UTC (NB-6). Seeded Slack messages go before that, which is Thursday evening to early Friday Pacific.
- After Feb 11 20:40 UTC, Oliver, Owen, Martin and Marcus are single-channel guests in `#prototype` (`C09UHHN6PFZ/1770842566.250369`; NB-1). Seeded posts by them belong there or before Feb 11.
- Terminations are backdated to Dec 25, 2025, and Google accounts are archived after Feb 15 (`C05KNDCHAAG/1770839984.194409`).

**What I could not do.** STEP 0.6 (dataset duplicate) cannot be measured locally: `hg_similarity.py` is not in the bundle.
Gmail and Slack attachments return no bytes, so the signed CrazyGames and BoomBit agreements (PDF only) stay unread and
are never graded.

**Originality constraint.** The nearest neighbours to stay clear of:
- `robert_winddown_closeout` (submitted 2026-10-30): same persona and date, Corp Ops. Its job was the account close-out register, a Linear issue settled per account, and two monthly totals.
- `robert-vendor-schedule`: Robert · Finance · Retrieval on Feb 14, the vendor notice list for Sunset. It may sit in the platform library.
- The L12 "Leonard's vendor list" tasks the Q4-commitments STEP 0.6 report named as nearest.
- Frederick's investor send-list tasks.

A job that is "list our vendors and total them" will score near these. The recommended job is a different one: what
the founders' LLC takes over and how it is funded.

## 1. What a 5 needs at each gate

| Gate | What a 5 / PASS needs | Risks specific to this task |
|---|---|---|
| `/injection` | No seed contradicts any base record anywhere in the universe. Each seed is dated after the base events it relies on and before Feb 13 10:03 UTC for Slack. Schema and id contracts hold. Companions are seeded (one GCal copy per attendee, Drive rows for every Docs/Sheets file, Linear lifecycle stamps). No activity lands on a closed ticket | Every figure about hosting, tools and cards already exists in several versions in the base (Q07: AWS "~$1k" / $1,550 / $1,485 / 0). Seeded amounts must agree with the record each one supersedes, and must postdate it. The prior Robert task's SQL already used "moved to the KubLLC card" wording; re-check every such claim against Arthur's own Feb 12 23:00 post (`C0ADGSZKR3R/1770937232.664809`) |
| `/prompt` | Hard gates first: fit, UGT, feasibility, cross-service coherence. Then a natural voice, originality under 0.80 and no rules, traps or answers in the prompt | Fit: the job must read as a founder's funding and take-over decision (Finance: budget, forecast, fundraising), not as Corp Ops account admin. UGT: §4 lists 11 forks that need dated records. Coherence: the cash, February-payment and Helpshift cards (NB-3, NB-4, NB-5, NB-8) sit next to the job, so no deliverable may ask them |
| `/hardness` (one pre-check) | PROCEED (3–5): the run misses weight-5 rows for real reasons | On this persona and universe Opus swept `#winddown` 6/6 and its key threads 6/6. It read `#executives` 1/6 (roots from Feb 11 only), DMs 0/6, Snowflake 1/6 (table list only), GitHub 1/6 and Calendar 1/6. It ran per-account Slack name searches in most runs (`exposure_robert_runs.txt`). A correction placed in `#winddown` is caught every time |
| `/oe` | Each step discoverable from the prompt or an earlier step's Expected data, with accurate tools, parameters and values | No OE may read a Gmail attachment (the wind-down task took 9 `/oe` rounds over one PDF-only amount). Warehouse steps name the table and the January filter. Expected lines use only persona-visible values |
| `/rubric` | Atomic "The Agent …" rows; weights by kind of work; ≤ 5 samples per group plus a volume row; no count bundled with an identity; one order row per write kind; no do-nothing rows; no predicted all-fail | Apply learnings §60–62 from the start. Rows joining records across services are weight 5. Keep each channel's direct row separate from the totals, so one miss cannot dominate (§6, revision 1 vs 2) |
| `/create-difficulty` | Six Opus 5.5 slots, corrected average < 90 %, < 5 full passes, population SD 0.10–0.30, ≥ 2 failure patterns (largest ≤ 50 %), ≥ 100 counted calls, ≤ 2 errored | The binding gates here are spread and horizon, not the cap. The wind-down task landed 85.7 % with SD 0.034, because about 100 of its 136 rows passed every run. This design has the opposite risk: a heavily coupled surface. §6 shows both. The ≥ 100-call golden run is the tightest gate (§7) |

## 2. Robert's reach at the clock

Census output is in `00_PreScenario/reach_robert.txt` and identity in `entity_robert.txt`. Every load-bearing base record
below is YES in `cansee_anchors.txt`.

- **Slack.** 224 visible channels (37 public, 82 private, 66 mpim, 39 IM), 129,939 own posts, last post 2026-02-13.
  - YES: `#winddown` `C0ADGSZKR3R`, `#executives` `C07C2866011`, `#prototype` `C09UHHN6PFZ`, `#company-internal` `C05KNDCHAAG`, `#admin_foundersonly` `C04UEQVDVB7`, `#founders` `C04UTBZL6AX`, the BoomBit channel `C09SWTHEMEW` (channel-level YES).
  - DMs: Leonard `D04UP2L3E3S`, Arthur `D04V95AAAHW`, Oliver `D07H86MV4DN`, Marcus `D05UDNCCFEW`, Julia `D05GU6L0XFH`. DM member lists are unreliable (NB-31), so reach is argued from `can-see`, never from members.
- **Gmail.** 16,233 threads and 19,169 messages (2023-03-15 → 2026-02-13). 250 threads have February 2026 mail, mostly cold outreach and newsletters.
  - Finance notices that do reach him: Deel "payments due" ($9,717.90 for 3 contractor invoices, `robert@harmonygames.co/1855892533860895614`), and SVB payment notices (Deel $9,889.90 and Eveline Art S.R.L. $3,720 on Feb 2, `…/1856009245020615882`).
  - App Store Connect TestFlight and App Review mail for both Combo Fighter (builds 1.0.84–1.0.91 in February) and Domino Delights.
  - The CrazyGames thread copy, 24 messages, `…/1847444686342952172`.
- **Calendar.** 1,229 events (547 distinct ical_uid, 118 cancelled), last before the clock 2026-02-12 16:30Z (the Sherwood call). Nothing after the clock.
- **Drive family.** He owns 223 items. His root folder `d_9f7ba94f7526d54d8482ba` is YES (owner), the only proven write home. 464 items are shared with him.
  - **Not visible:** the seed papers (Investors' Rights Agreement `f_12bdc5faa19583b4b5138a`, the stock-purchase disclosure schedule `f_2471b5a89bab1b9e97701a`; both private to Leonard or Arthur), Leonard's mailbox (Sunset, vendor invoices, Carta) and the Wind Down folder.
- **Unscoped.**
  - Linear `usr_Robert` (last activity 2025-10-27); GitHub `EMPLOYEE_0016_GITHUB_USERNAME` (2026-01-16); Trello `3d06b73654d0c8940792514c`; Confluence `user_EMPLOYEE_0016`; Snowflake.
  - Contacts lists him as "Co-founder & Chief Product Officer", which differs from the roster; never seed or grade a title.
- **Who is active.** Leonard, Arthur, Robert, Oliver, Owen, Martin and Marcus are all `active_feb_2026` (KB `activity.json`).
- **His remit at the clock: this is his decision.**
  - Feb 3 he wants Combo Fighter "self sustaining, so you don't have to make it a side biz" (`C07C2866011/1770084297.911029`).
  - Feb 4 Leonard says Combo Fighter "needs another 3-6 months" (`/1770237771.839399`).
  - Feb 9 Leonard proposes the "lifestyle biz" route: "shutting down Harmony Games and buying its assets under an LLC we own" (`/1770612982.268919`).
  - Feb 11: "we will put our IP to auction and if no one buys it we can buy via our LLC" (`/1770850800.723979`).
  - Feb 12 Leonard keeps "Metabase and dbt until Robert stops caring about combo fighter data" (`C0ADGSZKR3R/1770933903.645709`).
  - Feb 12 Robert tells Oliver "the only thing that's missing is a budget" (`D07H86MV4DN/1770873696.684969`).

## 3. Storylines and recommendation

| # | Storyline | Fit (Exec / strategy inside Finance) | Reach and data | Originality | Hardness raw material | Verdict |
|---|---|---|---|---|---|---|
| **A** | **The LLC take-over plan for Combo Fighter, March–May.** Robert decides what the founders' LLC takes from Harmony Games if Sunset can't sell it: Combo Fighter, plus Domino Delights only if it covers its own hosting. He sets the monthly running cost and the cash need month by month, how the three founders split it, and the dated transfer steps with owners. Then he recommends it to Leonard and Arthur with the tradeoffs | Strong on both sides. It is a strategic go/no-go on continuing a title, a three-month budget and forecast, and founder funding. Robert is the natural owner (§2) | Strong. Every base fact is in channels and DMs he can read, the warehouse and his own mailbox. His own Drive root is the write home | No Atlas storyline. The LLC thread appears in no stored task. Neighbour risk is the wind-down task's "monthly totals", so the job must read as funding a continuation, not closing accounts | Real base forks become designed traps: hosting quoted five ways; a $100/day campaign on no keep list; Arthur's card moves; Calm Play LLC, the dormant 100 % subsidiary that held the store accounts until July 2025 | **Recommended** |
| B | Dissolution notice to stockholders. Robert plans which investors he and Leonard tell, in what order, before the announcement email, and what each holds | Good: cap table plus investor coordination | Weak. The stockholder list is in seed papers private to Leonard and Arthur. Robert sees only a summary: Griffin 2,662,255 + Side Fund 84,438 of 3,051,881 Seed shares at $0.9830 (`C07C2866011` Jan 14, `/1768415499.678309` to `/1768418266.528599`). Angels are tokenized. Leonard owns the task ("Reaching out to our angels properly", `C0ADGSZKR3R/1770934638.035469`) | Close to the investor send-list neighbours (0.804 precedent, memory `prompt-dataset-duplicate-gate`) | Seeding a cap table invites contradiction with the private papers. There is little done-vs-missing material | Alternate |
| C | Wind-down cash plan: what the $22,500 data money pays and in what order | Good on paper | Leonard already decided it: "as soon as the money hits the account we pay SVB fully and close the credit card" (`C0ADGSZKR3R/1770927223.969899`) | Lowest: it is "Leonard's vendor list" with a total | Every input is a known card: NB-3 cash, NB-4 paid or accrued, NB-5 and NB-8 Helpshift, NB-23 Singular, Q07 amounts | Reject |

Also screened and rejected:
- The R&D tax credit: it is payroll-offset only, so nothing to plan (`C07C2866011/1770780604.709459`).
- Leapblock's ~$600 gesture: one line (`C0ADGSZKR3R/1770922731.444009`).
- Combo Fighter metrics plans: NB-7, NB-9 and NB-26 make levels, Android and sales ungradeable.

**Why A.**
- The decision is live at the clock and unmade, and it is Robert's. Leonard asked whether "you guys are ready to … explore lifestyle biz route" (Feb 9), and on Feb 11 said the LLC can buy what doesn't sell. No base record sizes or funds it.
- It is Planning and decision support by nature: a recommendation, a schedule with owners and dates, and the tradeoff the numbers force. The campaign is most of the burn against about $7 a month of Combo Fighter income.
- The traps come from base history (five hosting figures, a forgotten campaign, Arthur's card moves, Calm Play LLC) rather than from invention, and each needs records joined across services.

**Base facts behind A (all read through `hg.py`).**

| Fact | Record |
|---|---|
| Lifestyle-biz LLC proposal: buy HG's assets under an LLC we own; DD makes a small amount; team part-time | `C07C2866011/1770612982.268919` (Leonard, Feb 9) |
| IP to auction through Sunset; if unsold, buy via our LLC | `C07C2866011/1770850800.723979` (Feb 11) |
| Combo Fighter needs another 3–6 months; Robert wants it self-sustaining; "the only thing that's missing is a budget" | `C07C2866011/1770237771.839399`, `/1770084297.911029`; `D07H86MV4DN/1770873696.684969` |
| DD production AWS "~$1k a month", then "Might be easy to get to 300"; Leonard: "We make way less than $1K" | `C0ADGSZKR3R/1770680984.725779`, `/1770682219.100789`, `/1770686243.781429` |
| Confluence AWS guide (updated 2025-12-31): DD has separate dev and prod accounts; cost note "estimates only": Fargate ~$650, Aurora ~$420, analytics ~$300, ALB etc. ~$180 | `confluence:page_aws_infra` |
| Warehouse income, `ANALYTICS.MONETIZATION.REVENUE_DAILY`, January 2026: domino_delights $183.11, combo_fighter $7.36, zombie_match_3d $0.00. February is partial to Feb 9. The table comment says SUM over grain rows | `snowflake_revenue_by_month.txt`; mirrors agree (KB Q09) |
| Keep list for the shutdown: Deel, Gusto, Intuit; Figma can't charge before renewal; Linear kept during transition; Metabase and dbt about $300 a month for a month or two | `C0ADGSZKR3R/1770933601.686309`, `/1770933903.645709` |
| Arthur: "I'll be moving github, [USERNAME_30019], and Metabase to my KubLLC card"; repos to "my LLC" with seats for whoever still works | `C0ADGSZKR3R/1770937232.664809`; `C05KNDCHAAG/1770842137.835489` |
| Combo Fighter video campaign: "Budget is $100/day" (Feb 6); "I will keep both campaigns live" (Feb 7). No later record turns it off | `C09UHHN6PFZ/1770404445.795829`; `C07C2866011/1770489896.754049` |
| Cut-offs: Google accounts archived after Feb 15; DD and ZM off Helpshift before Feb 28; layer.ai access until March 3; Figma paid until September 11; AppsFlyer free up to 15K installs if Singular closes | `C05KNDCHAAG/1770839984.194409`; `C0ADGSZKR3R/1770789534.434749`; `C09UHHN6PFZ/1770837702.167889`; `C0ADGSZKR3R/1770859313.592649`, `/1770932709.222409` |
| Calm Play LLC: "fully owned by Harmony Games", the stealth publisher. ZM moved from it to Harmony Games on Apple and Android in July 2025. It still owes a $300 Delaware tax (paid May 15, 2025) and a $125 registered-agent fee (Oct 4, 2025). Leonard in 2023: "Calm Play is something we can also use in the future" | `C04UEQVDVB7/1701383740.580749`, `/1703492127.063049`; `C07C2866011/1752548116.304169`, `/1752622453.361899`, `/1752726128.862409`; `C04UEQVDVB7/1747349657.711009`, `/1759615469.061409`; `C04UTBZL6AX/1701126533.617549` |
| Publisher ties on DD: the CrazyGames (MAXFLOW BV) draft, as Leonard summarized it on Nov 17, covers DD and ZM with a 6-month transition tail (the signed Dec 3 version is PDF-only, so never graded); DD "is with boombit" | `C07C2866011/1763421018.863089`; `C09UHHN6PFZ/1770844309.583109` |

## 4. UGT plan (rule 1)

1. **Population from a record.** A seeded hub (Leonard's DM, dated Thursday night PT, before Feb 13 10:03 UTC) asks for the plan. It names no items.
   - A seeded ground-rules record defines the scope in checkable terms: everything that still bills each month for a game the LLC takes (subscriptions, servers and anything running for the game).
   - Completeness is claimed only over a census of those charges (learnings §23). Anything else found goes to Monday as a question.
2. **One closed decision set, plain definitions, outside the hub.** The ground rules hold:
   - the take test (a game comes over if January's income covers its own hosting; Combo Fighter comes over regardless);
   - the window (March 1 – May 31);
   - the costing rule (what an item bills now, per whoever runs it);
   - the split rule (equal thirds of the cash need; what one of us already pays personally counts toward that share).

   No item-level resolver goes here (memory `hardness-opus-sweep-pattern`).
3. **Every graded value comes from a record:** a warehouse sum, a dated Slack or Calendar statement, or a base cut-off. No figure is estimated by the agent.
4. **Forks to settle with dated records before `/prompt`:**

   | Fork | Settled by |
   |---|---|
   | Which LLC: "an LLC we own" (Feb 9) vs Arthur's KubLLC ("my LLC") vs Calm Play LLC (HG's 100 % subsidiary) | hub wording; Calm Play stays a named decoy |
   | Window: "3–6 months" vs "a month or 2" | ground rules: March–May |
   | DD in or out: "small amount of money" vs "not worth keeping the lights up" unless BoomBit supports it (`C0ADGSZKR3R/1770686219.875929`) | take test plus January warehouse income |
   | Hosting figure (Q07: ~$1k, $300 hoped, $1,550 estimate, $1,485 ledger, $0 P&L) | Arthur's dated statement of what the trimmed DD account bills now, made authoritative by the costing rule |
   | Income month and grain | ground rules name January; the table comment says SUM over rows |
   | Campaign still running and at what rate | a dated status record after Feb 7 |
   | Metabase, dbt, GitHub: HG's ~$300 vs Arthur's card | Arthur's dated completion note with the amount |
   | Leonard's participation and any cap | dated hub sentence (his Jan 6 "$25K" was for the recap and is now stale) |
   | People costs (part-time team) | out of scope by the hub; NB-15 and the Dec 25 backdating make any rate a fork |
   | Unity licence for builds | not graded; Q07 Unity amounts |
   | Figma, layer, Helpshift, Singular | base records already settle each one (paid to Sep 11; cancelled to Mar 3; off by Feb 28; free tier) |

5. **Apply each rule sentence to every item.** Before SQL, run the fork sweep over every charge, title and cut-off (learnings §21–22).
6. **Keep off the graded path:**
   - Known-data-issue cards touched, each avoided: no cash balances (NB-3); no February paid-vs-accrued (NB-4); no Helpshift amounts or dates (NB-5, NB-8); no P&L-sheet costs (NB-2; the sheet is never cited); no Slack after Feb 13 10:03 UTC (NB-6); no channel access after Feb 11 (NB-1); no Combo Fighter levels, Android or sales (NB-7, NB-9, NB-26); no Combo Fighter GDD status (NB-11); no tokenized vendor (NB-12, so `[USERNAME_30019]` is spelled out by a seed); no shutdown date as a window start (NB-29); no access argued from DM member lists (NB-31); no join of review versions to build numbers (NB-21).
   - KB hazards to cite at scenario: Q07 (amounts quoted several ways; resolved by the costing rule), Q08 (no CPI asked), Q09 (mirrors agree), L13 (work after the announcement; the plan relies on it, never grades it), I03 (mailbox aliases).
7. **Two blind sweeps before `/injection`** (memory `blind-sweeps-catch-base-contradictions`): forks first, from persona-visible dumps only; then seeded-versus-base coherence over the full base, including Leonard's and Arthur's mailboxes.

## 5. Hardness plan (rule 4, Hardness v2)

Six channels. Four are cross-source decisions on distinct v2 trap types (1, 2, 7 and 9). Each names the convincing
wrong source and the record that beats it, and moves ≥ 2 rows including a weight-5 row. AUTH is a rarely-opened
authority, a complexity channel that also moves a weight-5 row. DATE is v2 trap 4 but moves only weight-3 rows (see the
FLAG). `NEW` marks a planned seed, not yet checked against the whole universe.

| Channel | v2 trap | Convincing wrong source (who, when) | Record that beats it (who, when, authority) | Rows it moves | Placement and findability (measured) | Prior |
|---|---|---|---|---|---|---|
| CORR | **2 · A correction somewhere else** (A11) | Arthur in `#winddown`: "~$1k a month" (Feb 9), then "Might be easy to get to 300" (Feb 10). The Confluence estimate (Dec 31) backs a high figure | NEW Arthur reply in his DM with Robert, under a root about something else (Feb 13). It gives what the trimmed DD account bills now; the costing rule makes the person who runs it the authority | DD decision (5), DD hosting line (5), March cash need (5), recommendation (3) | `#winddown` is swept 6/6, so the stale figures are always met. DMs were read 0/6, but name searches cover DMs: a `#prototype` reply found by name search was caught 4/6. Word it in the account's own words, not "AWS" | 0.40 |
| FILT | **7 · Items outside the obvious filter** (A17) | The `#winddown` keep list and Arthur's card moves read as the full set of monthly charges | Base `#prototype` Feb 6 ($100/day) and `#executives` Feb 7 (kept live), plus a NEW dated status after Feb 7. The ground rules count everything still billing for a taken game | Campaign line (5), March cash need (5), tradeoff named (3), split (3) | Neither list names it. `#executives` read 1/6; `#prototype` history 1/6. Found only by a run that asks what else bills Combo Fighter | 0.55 |
| COMPLETE | **9 · Work someone already did** (A25) | Leonard's keep list: Metabase and dbt "~$300/month" (Feb 12 22:05); Arthur's future tense "I'll be moving …" (23:00) | NEW Arthur billing-switch note: the description of a Feb 13 calendar event, with a ● copy as a comment in the Linear transition project. It says the three already bill his card and he carries them through May as his part | Cash need excludes them (5), Arthur's share credited (5), shares in reply (3) | Calendar 1/6 here, 3/7 on Frederick runs (search returns descriptions). The Linear copy sits in the destination project, which every run opens to write | 0.40 |
| DONE | **1 · Proving "done" across services** (A24) | NEW Arthur in `#winddown` (Feb 13): DD support goes to email now, so Helpshift is out | NEW App Store Connect notice in Robert's own mailbox (Feb 13): the DD submission carrying the change was rejected, or is still waiting. The live build still opens Helpshift past Feb 28 (`C0ADGSZKR3R/1770789534.434749`), so a release step is owed | Support-build step before Feb 28, owner Arthur (5); reply names the unreleased build as an open step (3) | Robert's mailbox already holds DD TestFlight and review mail. Runs ran 10–25 Gmail searches each. Moved from GitHub, where the same persona's runs caught a PR bot comment 0/6. Worded by date, never by build number (NB-21) | 0.50 |
| AUTH | Hidden authority in a rarely opened service (A13), complexity channel | "We make way less than $1K" (Feb 10); BoomBit's "retention looks a lot better" (`C09SWTHEMEW`, Feb); February's partial month | `REVENUE_DAILY` summed for January: DD $183.11, ZM $0.00. The ground rules name the month and the table | DD decision (5, with CORR), ZM left (3), DD income line (3), what is left to Sunset (3) | Snowflake was opened 1/6 here with no pointer. The ground rules point to the warehouse by role, so the remaining difficulty is the month and grain choice | 0.30 |
| DATE | **4 · Dates and windows** (A4) | Steps dated anywhere in March | Google archive after Feb 15; Helpshift by Feb 28; layer access to Mar 3 | Step dates (3 each) | Feb 15 and Feb 28 are in swept channels; Mar 3 is in `#prototype` ("layer" searched 2–3/6) | 0.35 |

**Controls and decoys** (learnings §41):
- Figma at $0 (paid to Sep 11); attribution on the free tier; Helpshift and layer cancelled; ZM left with Sunset. These are visible-evidence rows that a careful run gets.
- Calm Play LLC as "our LLC", backed by Leonard's 2023 line. It is HG's subsidiary, so it is a decoy for the vehicle, never the answer.
- The one-off "$100 we have" Unity playable (`C09UHHN6PFZ/1770845002.610529`), a lookalike that is not monthly.
- Leonard's Jan 6 $25K pledge (recap context, stale), and the Confluence estimate.
- Routine Deel and SVB notices that agree with the records.

Finding a record about an item never marks a trap by itself.

**Independence.**
- Each channel has its own item, service pair and root cause: A11, A17, A25, A24, A13, A4.
- CORR and AUTH meet on the DD decision row only; each also has its own row.
- The largest unit (CORR) decides 29.6 % of the sketch weight (24 of 81), under half.
- No correction sits in the hub, an anchor, the superseded record's container or a delegating record's container. The hub delegates by role and lists no items.

**Survives complete retrieval.** CORR, COMPLETE and AUTH stay hard after every record is read, because each needs a
rule applied across two records. Even a run that reads the DM still has to rank Arthur's newest figure over the
Confluence estimate. FILT and DONE are retrieval-shaped and depend on placement, which is why they get different priors.

### Part 7 checks: `hardness_v2_check.py --design` on the pre-scenario sketch

The sketch (`00_PreScenario/sketch_manifest.json` + `sketch_surface.json`, revision 2) is **not** the `/create-scenario`
manifest or surface. Output, verbatim (`hardness_v2_check_output.txt`):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      2 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 4 requirements: {'R3': ['CORR'], 'R1': ['AUTH'], 'R4': ['COMPLETE'], 'R2': ['DONE']}  [Part 5 rule 1]
  FLAG       DECISION_FLIP   5 of 6 rules can flip a weight-5 slot; not: ['DATE']  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     3 weight-5 total(s); 3 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']

Flags (each needs a written disposition; redesign the difficulty, never weaken a fairness link or raise a weight):
  DECISION_FLIP DATE: rule DATE (A4) can flip slots of weight [3], no weight-5 slot
```

**Dispositions.**
- **DECISION_FLIP DATE.** Kept as a complexity channel at weight 3. Dating a step against a cut-off is interpretation, not multi-source work, so raising it would break the weight rule. It is not counted among the v2 decisions. `/create-scenario` either gives it a money consequence, or drops it if the rule budget (k ≤ 8) runs short.
- **FILT's two Slack containers.** The tool counts FILT as single-service (two Slack containers), so TWO_DECISIONS lists four rules, not five. That is enough for the "two or more" rule.
- **Weak evidence.** CLEAN here only covers the containers I declared. Re-run on the SQL. RULE_IN_PROMPT re-runs once a prompt exists.

## 6. Spread and score plan (rule 5, UNCALIBRATED)

`00_PreScenario/policy_model.py` scores the sketch surface (revision 2): 29 slots, total weight 81, 84.0 % flippable by
mechanisms. It uses a Gaussian-copula run latent and 3 % base slips; output is in `policy_model_output.txt`.

| Whole policy | Score |
|---|---|
| Perfect | 100 % |
| Hub and `#winddown` only (keep list and Arthur's `#winddown` figures as final) | 16.0 % |
| Every Slack channel and DM, nothing outside Slack | 69.1 % |
| Thorough except the Feb `#prototype` / `#executives` history | 69.1 % |
| Thorough except DMs | 70.4 % |
| Right calls, ignores the billing-switch note | 74.1 % |
| Thorough except the warehouse | 79.0 % |
| Thorough except store notices in the mailbox | 90.1 % |
| Thorough, dates steps loosely | 92.6 % |

| Single miss | CORR | AUTH | FILT | COMPLETE | DONE | DATE |
|---|---|---|---|---|---|---|
| Score | 70.4 % | 79.0 % | 76.5 % | 74.1 % | 90.1 % | 92.6 % |

Four of the six single misses take a run under the 90 % cap on their own; DONE (90.1 %) and DATE (92.6 %) do not.
**No pair of misses stays at or above the cap.** The highest-scoring pair, DONE + DATE, is 82.7 %, so any run with two
landings is under it.

Six-run Monte Carlo at design landing rates: CORR 0.40, AUTH 0.30, FILT 0.55, COMPLETE 0.40, DONE 0.50, DATE 0.35 (mean 0.42).

| Landing scale × rho | E[avg] | P(cap) | P(SD 0.10–0.30) | P(< 5 full) | P(patterns) | P(all gates) |
|---|---|---|---|---|---|---|
| 1.00 × 0.30 | 59.0 % | 1.00 | 0.91 | 1.00 | 1.00 | 0.91 |
| 1.00 × 0.60 | 60.5 % | 0.99 | 0.70 | 1.00 | 0.98 | 0.69 |
| 0.80 × 0.35 | 66.6 % | 0.99 | 0.90 | 1.00 | 0.99 | 0.89 |
| 0.60 × 0.35 | 74.1 % | 0.96 | 0.92 | 1.00 | 0.98 | 0.88 |
| 0.50 × 0.35 | 78.1 % | 0.90 | 0.91 | 0.99 | 0.97 | 0.84 |
| 0.40 × 0.35 | 82.1 % | 0.82 | 0.88 | 0.98 | 0.95 | 0.76 |
| 0.30 × 0.35 | 86.3 % | 0.66 | 0.81 | 0.95 | 0.91 | 0.62 |

**Targets.** E[avg] ≤ 82 % holds down to about 0.45× (a mean landing rate of about 0.19); at 0.40× it is 82.1 %.
P(all gates) ≥ 0.5 holds over the whole range shown, and is 0.62 at 0.30×. Both targets are met at design rates.

**The honest read.** The answer turns on the real per-trap landing rate, and the measured anchors disagree:

| Measured | Per-trap landing | Scale |
|---|---|---|
| Robert wind-down baselines (same persona, same universe): Unity root in `#executives` missed 5/6; GitHub bot comment missed 6/6; `#prototype` reply missed 2/6; judgment clash missed 3/6; swept clash missed 0/6 | about 0.53 (2.67 of 5 per run) | about 1.0 |
| Frederick bridge rev12 batch 2: three traps, each missed 3/6 | 0.50 | about 1.0 |
| Frederick bridge rev10–12 pre-checks: about one trap missed per run of three | about 0.33 | about 0.7 |

So at this persona's measured rate (scale ~1.0) the average lands near 60 %. That is far under the 90 % cap, so the
risk is the opposite of the wind-down task's. Three risks follow:
- **All-fail rows.** P(the March cash need fails all six) is about 0.35 at design rates (it passes a run only when CORR, FILT and COMPLETE all miss landing: 0.60 × 0.45 × 0.60). VALID all-fails are legal with a justification, but they lower the SD.
- **Fairness.** A very low score invites a "too hard because unfair" reading.
- **One run catching everything.** P is about 0.04, so `/hardness` should PROCEED.

**Revision 1 vs 2 (kept in the evidence).** The first sketch graded three totals and two share rows off the same
inputs: mechanism share 89.9 %, a single CORR miss at 62.0 %, E[avg] 54.2 % at design rates. Revision 2 de-coupled it
(one cash total, one split row, five visible-evidence rows, a second DONE row) and moved DONE's missing piece out of
GitHub. The lesson for
`/create-scenario`: let each channel own its direct row, grade one aggregate per deliverable, and add honest
visible-evidence work so the average sits near 75–82 %, not 60 %.

**Calibration caveats.**
- Opus 5.5 ledger priors are thin: `superseding` 0.25 (n_eff 2), `exact_predicate` 0.25 (n_eff 2), `completion_elsewhere` 0.33 (n_eff 1), `done_gap` 0.50 (n_eff 2), and none for `boundary_date` or `house_rule`.
- Exposure moves between revisions (memory `baseline-signature-concentration`).
- `/create-scenario` S9b's pre-registered forecast replaces this sketch.

## 7. Volume plan

Honest necessary calls for a correct run (golden-run basis), with no padding:

| Phase | Services | Calls |
|---|---|---|
| Discovery and rules: the DM, the ground rules, `#winddown` (3 pages), Feb `#executives` and `#prototype` with 2–3 threads, `#company-internal`, the Arthur and Oliver DMs | slack, gdocs | ~17 |
| Warehouse: list, describe, January revenue by game | snowflake | ~5 |
| Census of monthly charges and assets: name searches per charge; Deel, SVB and store mail; the calendar; the Linear transition project; the game repos; Drive; the Confluence AWS page; the founders' Trello board | slack, gmail, gcal, linear, github, gdrive, confluence, trello | ~38 |
| Per item (16–20 in scope × ~1.5 verification reads) | slack, gmail, linear | ~25–30 |
| Writes: plan sheet (create, move, two shares, 2–3 value updates), one Linear issue per transfer step (14–18, no batch form), the reply | gsheets, gdrive, linear, slack | ~22–26 |
| Read-backs | gsheets, linear | ~3 |
| **Total** | 11 services | **≈ 110–135** |

**≥ 500 necessary calls are not reachable without padding.** This job has 16–20 in-scope items. Growing it to 500 would
be manufactured work, which fails on its own. A volume exception is proposed below.

**Platform floor: the binding gate.** Long Horizon needs ≥ 100 counted calls in the golden run (the lowest count among
100 % runs).
- The Robert wind-down baselines made 118–144 counted calls, of which 56 were per-issue Linear reads and writes. Without them they made about 62–88.
- This design's honest per-entry lever is one Linear issue per transfer step, a natural "who and by when" schedule with no batch form.
- Expected golden run: about 105–125 calls. Check the pre-check's counted calls at intake. If it comes in under about 110, add per-entry work tied to a real ask (for example one check item per Monday decision on the founders' Trello board, memory `baseline-horizon-lever`), never padding.

**Floors the exception does not lower**, with where each stands:

| Target | Plan | Status |
|---|---|---|
| Cohort ≥ 40 × ≥ 3 surfaces over ≥ 2 services | About 50 items looked at: the keep list, Arthur's moves, the `#winddown` cancellations, the SaaS lines named in Slack, campaigns, repos and store listings for three titles, two publisher ties. 16–20 are in scope | **Passes only on the "looked at" reading** that Frederick and Samuel used |
| ≥ 10 injected schemas, without Confluence or Snowflake | slack, gmail, gcal, linear, gdocs, gdrive, gsheets (a stale Feb 10 draft budget, an A1 wrong summary), github (a control on the Combo Fighter repo), trello (founders' board), contacts | **Tight.** contacts and github need real roles, or the floor is short; Snowflake cannot be written |
| ≥ 120 INSERTs | Estimated 70–110 including companions | **Probably short.** Filler fails on its own, so a shortfall is a finding to bring back, not a gap to pad |
| ≥ 12 fragments over ≥ 7 services, 2–4 authorities, ≥ 3 chains, ≥ 12 traps | Authorities: ground rules (gdocs), the warehouse table, Arthur's DM figure, the billing-switch note. Six channels plus about ten base decoys and four supersessions | Fragments over 7 services is tight; the rest reachable |

## 8. Injection plan (rule 3)

- **Census every seeded entity across the whole universe**, including Leonard's and Arthur's mailboxes: KubLLC, Calm Play, Metabase, dbt, GitHub billing, the campaign, DD support, Helpshift and the App Store notices. Read the hits rather than counting them (learnings §10, §38). Every absence check carries a positive control (§35).
- **Date each seed after the base events it relies on and before Feb 13 10:03 UTC** for Slack:
  - Arthur's hosting figure after `1770682219.100789`;
  - the billing note after `1770937232.664809`;
  - the campaign status after `1770489896.754049`;
  - the DONE claim after `1770789534.434749`.
- **Settle the tokenized names**: spell out `[USERNAME_30019]` and keep BoomBit's token (`[USERNAME_48456]`) off every graded row (NB-12).
- **No fact only on Confluence, only in a GCal description or only in an attachment** (§26; memory `injection-stage-tool-gotchas`). The billing note gets its ● Linear copy. Snowflake is base-only and read-only.
- **Companions**: one GCal copy per attendee; Drive rows for every Docs and Sheets seed; Linear project and issue stamps. Check the INT ids in `integrations.json` at scenario.
- **Confirm the agent's tools return each seed** in the pre-check. Read it for fallback events.

## 9. Writes (rule 6)

| Write | Authorized trigger the persona owns | Access proof needed |
|---|---|---|
| LLC plan sheet in Robert's own folder | Leonard's DM | New file under `d_9f7ba94f7526d54d8482ba`, Robert as owner in both the Drive and Sheets rows. `gsheets_create_spreadsheet` has no folder parameter, so it needs `gdrive_move_file`. No base sheet is ever a target |
| Share the sheet with Leonard and Arthur | Leonard's DM ("where Blake and I can open it" or similar) | `gdrive_share_file` as the owner; the role pinned by the hub (learnings §43) |
| One Linear issue per transfer step, with owner and date | Leonard's DM, which names the transition project | NEW project seeded by Leonard. Linear is unscoped and `linear_create_issue` is in the catalog; confirm a write returns ok in the pre-check |
| Reply to Leonard, with Arthur informed | Leonard's DM | DM `D04UP2L3E3S` is YES; `slack_send_message` in the hub thread. The destination must be unique in his view |

## 10. Decisions for you

1. **Storyline: A, the LLC take-over plan for Combo Fighter, March–May.** **Recommended.** B (the stockholder notice plan) is the fallback if you would rather have a cap-table job, at the cost of seeding a stockholder list Robert can't verify. C is rejected.
2. **Volume exception (GEN §3a).** Honest necessary calls are about 110–135, below the ≥ 500 floor.
   - Proposed: `volume_exception {call_budget_floor: 110, per_record_floor: 40}`, with the reason "16–20 in-scope items; reaching 500 would need padding, which fails on its own".
   - It needs your `requester_confirmation`.
   - Please also confirm two things: the cohort floor met on the "looked at" reading, and that a ≥ 120-INSERT shortfall is reported, not padded.
3. **Review waiver.** `REDTEAM_*` is unset, so the dual red team cannot run. Either set it before `/create-scenario`, or I record `RED TEAM UNAVAILABLE` plus a `RED TEAM FALLBACK:` line. The fallback names the two blind sweeps, the whole-universe census and the policy scores, and stays in every Unresolved line until a review or the pre-check covers it (learnings §44).
4. **Theme screen.** Playbook S0 screens zombie themes, and Zombie Match appears here only as a title left with Sunset. Samuel's check of 12 stored ZM baselines found 0 `model_refusal_fallback` events. **I recommend accepting it.** Seeds would say "ZM", keep "zombie" and "outbreak" out of seeded text, and I would check the pre-check for fallback events.
5. **Neighbour risk at STEP 0.6.** The wind-down task shares the persona, the date and "monthly totals". **I recommend framing the job as funding a continuation** (what the LLC takes, what it costs, who puts in what) and keeping "register", "close-out" and "accounts" out of the prompt. The score can only be read on the platform.

**Next step:** answer the decisions above, then run `/create-scenario`.

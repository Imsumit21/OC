# Pre-scenario analysis: Frederick Stone · Corporate Ops · Actions (analysis only)

Contains no prompt, Oracle Event or criterion text. Written 2026-11-03 for `/create-scenario`.
Probabilistic numbers are labelled **UNCALIBRATED**: they are design aids, not measured rates (learnings §9).
Evidence files: `Working_Files/00_PreScenario/` (reach census, identity resolution, can-see proofs, the sketch
manifest and surface, the Hardness v2 checker output, the policy model and its output, raw searches in `search/`).

## 0. Assignment and context (verified)

| Field | Value |
|---|---|
| Persona | Frederick Stone, Co-founder, `frederick.stone@harmonygames.co` (roster `frederick_stone`) |
| Function / competency / skill | Executive · Corporate Ops · **Actions** |
| Horizon / mode | Long Horizon (`effective_profile: extreme`, GEN §3a) · **easy**: corrected weighted average < 90 %; design target E[avg] ≤ 82 % |
| Universe | `synthcut`, hg4-synth-sep30cut v16. Eval clock 2025-10-01 07:00Z (00:00 PT). Seed bound `freeze_utc` 2025-10-01T00:00:00Z, which is Tue Sep 30 17:00 PT. Shutdown rules do not apply |
| Persona today | Wednesday, October 1, 2025; "yesterday" is Tue Sep 30 |
| Source | `task_context.py --write --require-source`: status `ready`, KB `bound`, context_hash `db8af19cc1c3…` |
| Tools | Last `Task_Authoring/tools` commit is 58c37b1 (2026-11-03). Every search ran through `Task_Authoring/tools/hg.py`. The Evals input store was not touched (learnings §37) |
| Red team | `REDTEAM_*` is unset in this environment, so `redteam_review.py --dual` cannot run (decision 3 below) |

**Originality constraint.** Frederick has three submitted synth-cut tasks (`support/completed_tasks/`):

- the Q3 card-spend breakdown (finance and investor reporting);
- the marketing/UA account handover (ad accounts, KEEP/CLOSE/REVOKE/TRANSFER, Leonard DM `D05S58U4SAK`);
- the bridge-round Q4 investor-update send list (investor firms, Existing Investor Update card).

The platform library also holds an L12 "fundraising part of the Oct 14 board pre-read" task and two "2025 investor
list before LA" tasks (memory: prompt-dataset-duplicate-gate, STEP 0.6 fails at ≥ 0.80). The new task must avoid
investor statuses, the ad-account cohort, the board pre-read, the DM destination and the Existing Investor Update card.

## 1. What a 5 needs at each gate

| Gate | What a 5 / PASS needs | Risks specific to this task |
|---|---|---|
| `/injection` (Checks A/B/C) | No seeded fact contradicts any base record anywhere in the universe. Each seed is dated after the base events it relies on, follows the schema and ID contracts, and has no event timestamp after 2025-10-01T00:00Z. Companions are seeded: thread snippets, one GCal copy per attendee, Drive and Sheets sharing mirrors, Trello badges | Every vendor and partner named needs a whole-universe census (Leonard's, Arthur's and Robert's mailboxes too), because Balancy, Playable Factory and Rayking may also have Leonard-side threads (learnings §10, §12, §16). Seeded vendors with money states must have **no base footprint** (§10). The Singular plan is known-data-issue **SC-39**: never grade it |
| `/prompt` | Fit to Founders/Exec × Corporate Ops, UGT, feasibility, cross-service coherence, natural voice, originality (STEP 0.6 < 0.80), and no rules, traps or answers in the prompt | Fit: the work must read as founder priorities and executive coordination over **vendor and contract** commitments, not UA performance. Taxonomy: vendor performance belongs to Growth/UA, while board/legal/HR/vendor is Corporate Ops (`Evals/1_Prompt_Eval.md` competency alignment). Frederick's founder status is known-data-issue **SC-49**: never grade it. Relative dates are computed against Wed Oct 1 (§20). UGT: every decision is settled by a dated record (memory: prompt-ugt-forks-need-records), with both blind sweeps run before submit |
| `/hardness` (one pre-check) | PROCEED (3–5): the run misses weight-5 rows for real reasons | Opus reads the hub, the authority and every record they name first. It bulk-reads Gmail and the calendar, and opens threads it reaches through its own searches (memory: hardness-opus-sweep-pattern). Every correction sits off the hub, the anchor and the superseded record's container, and is worded without the pointer's keywords |
| `/oe` | Each step is discoverable from the prompt or an earlier step's Expected data, with accurate tools, parameters and values and a feasible path | Counterparty names are often tokenized (`PERSON_5367_NAME` for Playable Factory, `PERSON_5681_NAME` for Google). Expected values use the company names that bodies and subjects show. Never read a Gmail attachment |
| `/rubric` | Atomic rows titled "The Agent …", weights by kind of work, ≤ 5 samples per group plus a volume row, no count bundled with an identity, one order row per write kind, no do-nothing rows, no predicted all-fail | Apply memory rubric-platform-round1-lessons from the start: cross-service joins are weight 5, every accepted name form goes in the title, and every count population has a named-member row |
| `/create-difficulty` | Six Opus 5.5 slots, corrected avg < 90 %, < 5 full passes, population SD 0.10–0.30, ≥ 2 failure patterns (largest ≤ 50 %), ≥ 100 counted calls in the golden run, ≤ 2 errored | Easy makes **spread, not the cap, the binding gate**: Robert's Easy task averaged 85.7 % but SD 0.034, because about 100 rows passed every run. It needs ≥ 4 independent channels, each caught roughly 30–60 % of the time and each moving ≥ 2 rows, with distinct root causes (memory: baseline-signature-concentration) |

## 2. Frederick's reach at the clock

Census output verbatim in `00_PreScenario/reach_frederick.txt` (`persona_view.py reach frederick_stone --top 10`) and
`entity_frederick.txt` (`entity.py resolve "Frederick Stone"`). Proofs are in `cansee_anchors.txt`: 22 records, all YES.

- **Slack.** 105 visible channels (12 public, 34 private, 17 mpim, 42 IM), 4,780 own posts, last post 2025-09-30.
  - YES: `#executives` `C07C2866011` (9 members, 1,198 messages in Sep 2025), `#zombie-match3d` `C0880U9751A`,
    `#zombie-art` `C08R8CHB0QL` and the Fred–Leonard DM `D05S58U4SAK`.
  - NO: `#admin_foundersonly` `C04UEQVDVB7`, the artist and contractor DMs (`D05UDNCCFEW`, `D05TZ6N23F1`,
    `D076V3NEA7P`), the PlayableX DM `D08JRD3TQE8` and `D08RQSCFKJ9`.
  - UNVERIFIED: `#zombie-prs` `C093LEZGF6J` (public, not a member).
- **Gmail.** 4,656 threads (2024-06-25 → 2025-10-01), 185 last active in Sep 2025. **Frederick sent only 7 external
  messages from Jun to Sep 2025** (`search/r_fred_sent.json`), so as in every earlier Frederick task the work arrives
  as a handoff from Leonard. Vendor and partner threads he can see (all YES):
  - Balancy `1840501641217286806`: Leonard parked it in-thread on Sep 11 ("company priorities have shifted").
  - Rayking Game (Chinese publishing) `1842348778705877030`: Leonard asks "Should we explore for DD?"; Frederick
    replies Sep 4.
  - Google partner check-in `1817715521687421486`: "set up a call when we have timing".
  - Playable Factory `1843000993076735547`: Sep 24 follow-up, unanswered.
  - Gamesforum SF speaker invite `1842890197572292911`: Oct 22–23.
  - Nintendo Developer Portal "NDA Acceptance Required" `1842358947604469113` and "Registration Completed"
    `1842359398719557772` (both Sep 4).
  - Singular payment-plan request `1837914783244638008` (Jul 17) and the ETL/Extract notice `1844214653847908044`.
  - ESG Law engagement `1841636073974841484` (Aug 27; counsel on standby; group address for requests).
  - Board invites `1843553829515378870` (Oct 14 and three 2026 dates) and the Griffin AGM agenda
    `1844166352857573845`.
- **Calendar.** 316 events on his own calendar (22 in Sep 2025). The last one before the clock is 2025-09-30 17:30Z.
  Quarterly board meetings (Oct 2024–Jul 2025) plus "Board Meeting Warmup" and "founders Board Meeting Sync" prep
  events.
- **Drive family.** He owns 46 items, and his root folder `d_175c0d7bc72ed244b944cb` is YES and owned: a write target
  he controls (learnings §31). 189 items are shared with him, including the July board doc `f_af99b76ff4da59a710edba`
  (YES; speaker notes on runway, the downsizing options and the salary-for-equity idea) and Executives Biweekly Sync
  `f_26e1f9a86761e35049192a` (YES; the Aug 28 entry is the SC-39 Singular source, never graded).
- **Unscoped.**
  - Trello: founders' board "Harmony Games" `640643a3fd8f3ca308d9318e`, with lists To Do, Doing, Done and Backlog
    (Recruiting is closed). It is Leonard's personal to-do list: "Playable Kickoff" `688c4d14c312a27fa2747e40`
    (To Do, 2025-09-13) and an empty "Paperwork for the Board" `680ee5d709c2d601148c25ff` (Backlog, 2025-08-01).
  - Contacts: 170 entries and no vendor or partner contacts. Frederick's own entry is "Commercial Lead, Marketing &
    Business Development".
  - Linear, GitHub and Confluence carry little for this storyline.
  - His identities: Linear `usr_175c0d7bc72ed244`, Trello `4b4a68fc0fec0b254e4f9d8e`, Confluence
    `user_EMPLOYEE_0008`. His GitHub login shows the name "Ryan" (entity FLAG), so keep GitHub off identity rows.
- **Founders' context at the clock** (`#executives`, all YES):
  - Frederick's Sep 15 "survival mode" framing: two buckets of UA spend, "nothing in the real spend bucket will move
    the needle" (`1757961037.465799`, `1757961282.621099`).
  - Leonard on Sep 24: "we have 2 months left before letting everyone go" and "save some cash aside … legal fees"
    (`1758739409.488879`, `1758739428.647609`); bankers if nothing lands (`1758739382.896799`).
  - Leonard flies to LA for the Oct 1 Dentsu meeting (`1758739727.864319`).
  - Mattel's RFP, with a proposal due "by end of September" (`1756832039.396149`): Leonard's thread, open at the
    clock, so never graded.
- **Clock hazards.** Base records between 00:00Z and 07:00Z Oct 1 exist (for example the a16z Speedrun pass at 02:30Z),
  but none touches this cohort. Seeds stop at Sep 30 17:00 PT, the persona's "yesterday".

## 3. Storylines (2–3) and recommendation

| # | Storyline | Fit (Exec × Corporate Ops) | Reach / data | Originality | Hardness raw material | Verdict |
|---|---|---|---|---|---|---|
| **A** | **Vendor and partner commitments under the founders' runway rule.** Before flying to LA, Leonard hands Frederick everything outside the investor work that is waiting on HG: renewals, trials, partner asks, developer terms. Frederick decides each one under the founders' Q4 runway rule, answers each counterparty, routes anything that needs a founder signature or counsel, sets revisit reminders, files contacts, logs it, and reports the shortlist | Strong. Founders priorities and executive coordination (the Sep 15 and Sep 24 runway decisions; routing signatures to Leonard or Arthur and counsel) applied to **vendor + legal/contracts** commitments. Frederick is the Commercial Lead who owns the vendor and partner portfolio (persona brief; Contacts title) | gmail, slack, gcal, gdocs, gdrive, gsheets, contacts and trello natively; linear and gslides by injection. Base members: Balancy, Rayking, Google, Playable Factory, Gamesforum, Nintendo; the rest seeded with no base footprint | New job: no investor statuses, no ad-account custody, no board pre-read. Nearest neighbours are the account handover and Robert's (normal-universe) vendor close-out, so expect the "same scenario" band (0.70–0.80) at worst, under the 0.80 fail line (UNCALIBRATED; `hg_similarity.py` is not local) | Natural done-claims (registration completed vs terms still unaccepted), answers given off-thread (Leonard's call notes), trial terms that convert inside the cash window, an exemption for what the live game needs, and members visible only through calendar calls | **Recommended** |
| B | Oct 14 board governance follow-through (open board asks from the Apr and Jul meetings, consents, prep-meeting series, materials) | Strongest on paper (board + executive coordination) | Weak. The consents, Carta and the Employees-Contractors folder are NO for Frederick; "Paperwork for the Board" is empty; Leonard already sent all four invites on Sep 17 | Low: same meeting, persona and deliverable family as the L12 "Oct 14 board pre-read" neighbour (likely ≥ 0.75) | Few done/not-done pairs Frederick can open | Reject (reach, STEP 0.6 risk) |
| C | Brand and trademark obligations after the Toon Boom co-existence agreement (Aug 13: amend the USPTO application within 5 days of signing, provide the executed consent, usage limits on "Harmony Games") | Good (legal/contracts; Frederick owns brand naming and trademark) | Poor. The summary sits in `#admin_foundersonly` (NO, `1755063509.040609`) and the lawyers' thread in Leonard's mailbox. The usage clause collides with every later base record that uses the name (coherence fail on presence) | High | Aliases, but the cohort is 2–4 marks | Reject (reach, coherence, volume) |

Also screened and rejected:

- the ZM3D IP and asset-licence audit: the evidence sits in the engineers' mailboxes, and its owner is Arthur;
- the salary-for-equity grants: HR records are in `#admin_foundersonly` and the payroll ledger, a coherence risk;
- the NCsoft engine partnership: thin, and a member of the bridge cohort;
- the Superplay/TYZ patent dispute: early-2024 history;
- grants and accelerators: no live record.

**Why A.**

- It is the one Corporate Ops thread that is live at the clock and sits in Frederick's own remit. The runway decisions
  are dated founder records he can open (`#executives`, Sep 15 and Sep 24), and Leonard's LA trip on Oct 1 is a
  natural handoff moment.
- It is Actions by nature: each member ends in a write of its own (a reply on its thread, a routed signature card, a
  revisit reminder, a contact), plus the log and the report.
- The deciding facts can sit in different services by construction (calendar call notes, thread replies under
  unrelated posts, vendor terms mail, the guardrails doc), which is exactly what Hardness v2 says beats Opus 5.5.

## 4. UGT plan (rule 1)

1. **The population comes from an incorporated record.** The hub (Leonard's seeded handoff mail, before Sep 30 17:00 PT)
   defines the population in source-checkable terms: every outside company waiting on HG for an answer, a renewal or
   trial decision, or a signature, where HG has had a call, an email exchange or paper. It names its exclusions:
   - investors (the bridge work);
   - ad networks (they stay on the UA budget call);
   - Mattel (Leonard keeps it);
   - cold pitches nobody answered.

   A census over Frederick's view plus the seeds fixes membership. Completeness is claimed only over that census
   (learnings §23).
2. **One closed decision set and its precedence, in the authority, not the hub.** A seeded guardrails doc (owner
   Leonard, shared with the founders, last edited before the hub) defines:
   - the decisions: keep, park to the revisit date, end or decline now, route for a founder signature or counsel,
     already answered;
   - a one-line test for each;
   - the order: already answered → signature or counsel route → live-game exemption → cash test → park;
   - the cash window, Oct 1–Dec 31, 2025 PT, where a trial's conversion date counts as cash.
3. **Signing rule from counsel.** A seeded ESG Law note says who may accept terms for the company (Leonard or Arthur
   only) and what goes to ESG first (auto-renewal, exclusivity, IP, terms over 12 months).
4. **Each write is defined once, where Frederick would read it:**
   - the reply goes on the counterparty's own thread, or to the address on the call invite when there is no thread;
   - the revisit reminder goes on his calendar on the stated date, titled with the company;
   - a contact is added only when missing (check first);
   - each routed signature gets one card on the founders' board To Do list, naming the counterparty;
   - the log sheet goes in his Q4 commitments folder, owned by him in both the Drive and Sheets rows (learnings §31).
5. **Apply every rule sentence to every member** (learnings §21–22). Before SQL, run the fork sweep over every census
   member and the boundaries:
   - a trial converting after Dec 31;
   - an answer Leonard gave by phone that said "later";
   - a vendor present in both Leonard's and Frederick's mail;
   - a member with paper and an exemption.

   Give every date-keyed rule its date on every member.
6. **Tokens.** No graded value is a token the persona can't map. Seeded vendors get readable company names; base
   members are graded by the company name their bodies show (Playable Factory, Rayking Game, Balancy, Gamesforum).
7. **Known data issues.** Never grade SC-39 (the Singular plan), SC-49 (Frederick's founder status), SC-7 (channel
   membership) or SC-54 (pay). Singular is out of the cohort under the ad-tech/UA exclusion.
8. **Settle every residual fork with a dated record**, never with rubric acceptance (memory:
   prompt-ugt-forks-need-records). Run both blind sweeps (forks, then seeded-vs-base coherence against the full base)
   before `/prompt`.

## 5. Hardness plan (rule 4, Hardness v2)

Six channels. Each is a cross-source decision on a distinct, named v2 trap type, names the convincing wrong source and
the record that beats it, and moves ≥ 2 weight-5 rows. All six sit on separate members and outputs.

| Channel | v2 trap (Part 3) | Convincing wrong source (who, when) | Record that beats it (who, when, authority) | Weight-5 rows it moves | Placement and findability (from measured rates in memory) |
|---|---|---|---|---|---|
| DONE | **1 · Proving "done" across services** (A24) | Frederick's own `#executives` "I registered an account for harmonygames" (`1757011358.730529`, Sep 4) and the portal's "Registration Completed" (`1842359398719557772`) | A later portal notice (seeded, Gmail) that the company account stays limited until an authorized officer accepts the Global ToS and NDA, plus ESG's signing note that only Leonard or Arthur accept terms | Nintendo's decision (route for officer acceptance); the signature card naming it | Medium: the notice's subject carries neither "Nintendo" nor "NDA" |
| CORR | **2 · A correction somewhere else** (A11) | A seeded tool vendor's own thread ends with its quote: renews Nov 1 at a paid rate, no answer | Leonard's later **thread reply under an unrelated `#executives` post** (Sep 26): the vendor waived Q4 and bills nothing until Feb 1. Cash in the window is zero, so park, not end | That vendor's decision; its revisit reminder | Low–medium: a reply under an unrelated post was caught about 20–30 % of the time on the bridge task. Worded without the vendor's pointer keywords |
| COMPL | **9 · Work someone already did** (A25) | Rayking's seeded "any news?" follow-up in Frederick's own thread (base `1842348778705877030`), unanswered | A calendar call Leonard held with them (seeded on Leonard's calendar with Frederick as an optional invitee, so his own copy carries it; calendar is persona-scoped). The description says he already told them: no China publishing until after the raise, talk in January | Rayking logged as already answered; the exact reply-recipient count (aggregate) | Medium: the calendar listing is read by most runs, but the note is off the mail thread |
| FILT | **7 · Items outside the obvious filter** (A17) | Frederick's inbox as "the backlog" | The hub's scope (a call or paper). One seeded vendor is visible to Frederick only through a calendar call he attended and a `#zombie-match3d` mention; its mail went to Arthur | Its inclusion; its answer (to the invite address); the member count and contacts count (aggregates) | Medium–low |
| EXC | **5 · A rule or exception hidden in the data** (A15) | The cash test: every paid commitment before January is cut | The guardrails doc exempts what the live game needs to keep running. An **older** `#executives` decision (seeded, August) ties one paid tool to that exemption | Its decision (keep); the kept list in the report | Low: needs the older record joined to the doc |
| DATE | **4 · Dates, windows and dependencies** (A4) | The trial's welcome mail ("free for 30 days") reads as costing nothing before January, so park | The vendor's own later terms mail: the trial converts to paid on Oct 15, inside the window, so it ends now | Its decision (end now); the cancellation sent | High findability: the decision stays hard after complete retrieval |

**Controls and decoys** (learnings §41).

- Balancy (Leonard's in-thread answer, `1840501641217286806`): the already-answered control.
- Google (waiting on timing, `1817715521687421486`): the park control.
- Gamesforum SF (travel cost): the decline control.
- A second trial that converts after Dec 31: the DATE decoy.
- A paid tool that looks needed but isn't: the EXC decoy.
- A vendor whose calendar call also has a thread in Frederick's inbox: the FILT control.

Finding a vendor's records therefore never marks a trap by itself.

**Independence and diversity.** Each channel has its own member, service pair and root cause. The largest unit, FILT,
decides about 19 % of the sketch weight (none over half). No correction sits in the hub thread, an anchor's container,
the superseded record's container or a delegating record's container (learnings §28, §45). The hub delegates by role
("the runway rule", "counsel's signing note") and never lists members, so no hub or checklist carries the answers.

**Survives complete retrieval.** Each deciding record is the natural return of an ordinary call: the member's mail,
the calendar listing, the doc, a search for the company. Each trap is lost by accepting a convincing source or by
misapplying the precedence, not by failing to search. DATE and EXC stay hard even when every record is read.

### Part 7 checks: `hardness_v2_check.py --design` on the pre-scenario sketch

The sketch (`00_PreScenario/sketch_manifest.json` + `sketch_surface.json`; **not** the /create-scenario manifest or
surface) declares the channels above with planned containers. Output, verbatim (`hardness_v2_check_output.txt`):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      1 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 5 requirements: {'R6': ['DONE'], 'R2': ['CORR'], 'R4': ['COMPL'], 'R1': ['FILT'], 'R3': ['EXC', 'DATE']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   6 of 6 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     2 weight-5 total(s); 2 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

**Dispositions.** No FLAG or UNRESOLVED fired.

- SAME_PLACE is CLEAN only over declared containers; injection must re-run it on the SQL. CORR must be a thread
  reply under an unrelated root, never a channel-level post or a reply in the vendor's own thread.
- RULE_IN_PROMPT re-runs once the prompt exists.
- The two weight-5 totals (member count, reply count) are graded as counts. Each count gets its own named-member
  rows, never bundled with an identity (memory: rubric-platform-round1-lessons).

## 6. Spread and score plan (rule 5, UNCALIBRATED)

`00_PreScenario/policy_model.py` scores the 25-slot sketch surface: total weight 103, 67 % flippable by mechanisms,
weights by kind of work (cross-service joins are 5). It uses a Gaussian-copula run latent and 3 % base slips. Output:
`policy_model_output.txt`.

| Whole policy | Score |
|---|---|
| Perfect | 100 % |
| Inbox and doc only (no Slack thread replies, no calendar) | 55.3 % |
| Trusts "done" sources (registration, unanswered follow-up, free trial) | 68.0 % |
| Thorough except calendar | 72.8 % |
| Reads everything, applies the cash test literally | 82.5 % |
| Thorough except Slack thread replies | 87.4 % |

Single misses:

| Mechanism | DONE | CORR | COMPL | FILT | EXC | DATE |
|---|---|---|---|---|---|---|
| Score | 87.4 % | 87.4 % | 90.3 % | 77.7 % | 92.2 % | 90.3 % |

**No pair of misses stays above the 90 % cap.** Three single misses (COMPL, DATE, EXC) do not clear the cap alone, so
a run needs ≥ 2 landings to score under 90 %. P(a run catches every trap) ≈ 0.027 under independence, so E[full
passes] ≈ 0.16 of 6.

Six-run Monte Carlo. Design landing rates: DONE 0.40, CORR 0.60, COMPL 0.55, FILT 0.45, EXC 0.35, DATE 0.30.

| Landing scale × rho | E[avg] | P(cap) | P(SD 0.10–0.30) | P(< 5 full) | P(patterns) | P(all gates) |
|---|---|---|---|---|---|---|
| 1.00 × 0.30 | 67.6 % | 1.00 | 0.94 | 1.00 | 0.99 | 0.93 |
| 0.80 × 0.35 | 73.7 % | 0.99 | 0.93 | 1.00 | 0.99 | 0.92 |
| 0.60 × 0.35 | 79.9 % | 0.92 | 0.88 | 1.00 | 0.97 | 0.84 |
| 0.50 × 0.35 | 83.0 % | 0.84 | 0.82 | 0.99 | 0.96 | 0.75 |
| 0.40 × 0.35 | 86.2 % | 0.71 | 0.72 | 0.98 | 0.94 | 0.62 |
| 0.30 × 0.35 | 89.3 % | 0.51 | 0.57 | 0.96 | 0.90 | 0.44 |

**Targets.** E[avg] ≤ 82 % holds down to about 0.55× the design rates; P(all gates) ≥ 0.5 holds down to about 0.33×.

**Calibration caveats.**

- The ledger's Opus 5.5 priors carry one trial each for `done_gap`, `superseding` and `exact_predicate` (mean 0.33,
  n_eff 1, all from frederick_bridge_pipeline). It has none for `completion_elsewhere`, `house_rule` or
  `boundary_date`, so the rates come from the measured placements in memory instead: on the bridge baselines,
  well-placed traps landed about 50 % of the time; records on the run's own search path about 0 %.
- The real risk is placement drift: a pre-check that catches a trap predicts the baselines will too.
- Spread is protected by giving each trap ≥ 2 rows and keeping the always-pass weight at about one third.
  `/create-scenario` S9b's pre-registered forecast replaces this sketch.

## 7. Volume plan

Honest necessary calls from the planned census (about 22 members: 6 base, about 16 seeded with no base footprint),
with no padding:

| Phase | Services | Calls |
|---|---|---|
| Discovery and rules: hub thread, guardrails doc, ESG note, `#executives` Sep searches and thread opens, calendar Sep–Oct listing, founders' board lists and cards, Contacts list, Drive folder | gmail, gdocs, slack, gcal, trello, contacts, gdrive | ~22 |
| Census: vendor and partner mail searches, Slack and calendar searches for members without mail | gmail, slack, gcal | ~12 |
| Per member (~22 × ~3: mail search or thread read, Slack or calendar check, contact lookup before adding) | gmail, slack, gcal, contacts | ~66 |
| Writes: one reply per member owed an answer (~13), contacts for members missing one (~16), revisit reminders for parked members (~6), signature or counsel cards (~4), log sheet create + values (~3), report reply (1) | gmail, contacts, gcal, trello, gsheets, gdrive | ~43 |
| Read-backs and checks | gsheets, trello, gcal | ~6 |
| **Total** | 9–10 services | **≈ 150** |

**≥ 500 necessary calls are not reachable without padding.** The cohort is about 22 real counterparties, and Opus
bulk-reads mail and calendars (memory: baseline-horizon-lever). A volume exception (GEN §3a) is proposed below.

Every other extreme target still applies:

- ≥ 10 injected schemas without Confluence (learnings §26). Planned: slack, gmail, gcal, gdrive, gsheets, gdocs,
  contacts, trello, linear (the developer-account task Arthur would own) and gslides (the board-deck vendor slide as a
  decoy). All ten are used.
- ≥ 120 INSERTs, ≥ 12 traps, 2–4 hidden authorities (guardrails doc, ESG signing note, the older exemption decision),
  ≥ 3 chains.

**Platform floor risk.** The Long-Horizon floor is ≥ 100 counted calls in the golden run (the lowest of the 100 %
runs). The about 43 single-object writes have no batch form in the catalog (`gmail_reply_to_message`,
`contacts_add_new_contact`, `gcal_create_event`, `trello_create_card`); they are the honest lever. With bulk reads, a
lean perfect run lands at about 100–130 calls. `/create-scenario` must keep the cohort at ≥ 20 members, each owed at
least one write of its own, and check the pre-check's counted calls at intake.

## 8. Writes (rule 6)

| Write | Authorized trigger the persona owns | Access proof needed |
|---|---|---|
| Log sheet in his Q4 commitments folder | Leonard's handoff (hub) | Folder and sheet owned by Frederick in both the Drive and Sheets rows; a can-see YES on the root `d_175c0d7bc72ed244b944cb` is already proven. Confirm the write returns ok in the pre-check (learnings §31) |
| Reply on each counterparty's thread | Hub + guardrails doc ("everyone waiting on us gets a written answer") | Each thread sits in Frederick's mailbox (base threads YES; seeded threads mirrored there). For calendar-only members, the invite's address is on an event he attended |
| Revisit reminders | Guardrails doc (parked → revisit date) | His own calendar (owner) |
| Contacts entries | Hub ("so nobody digs through mail next time") | Contacts is unscoped; `contacts_add_new_contact` is in the catalog |
| Signature and counsel cards on the founders' board | ESG signing note + hub | Trello is unscoped. Frederick has a member record (`4b4a68fc0fec0b254e4f9d8e`), and the bridge task's runs wrote to this board without error |
| Report reply to Leonard | Hub | Hub thread in his mailbox |

## 9. Decisions for you

1. **Storyline: A**, the vendor and partner commitments under the founders' runway rule. **Recommended.** B and C are
   rejected for reach, STEP 0.6 risk and coherence (§3).
2. **Volume exception (GEN §3a).** The honest necessary-call total is about 150, below the ≥ 500 floor. Proposed:
   `volume_exception {call_budget_floor: 140, per_record_floor: 66}` with the reason "about 22 real counterparties,
   bulk-readable mail and calendar; padding would be manufactured work". It needs your `requester_confirmation`.
   Without it, the only way to 500 is padding, which the goal forbids.
3. **Review waiver.** `REDTEAM_*` is unset, so the dual red team cannot run. At scenario I will record
   `RED TEAM UNAVAILABLE` plus a `RED TEAM FALLBACK:` line naming what stands in: the two blind fork and coherence
   sweeps, the whole-universe census and the policy scores. It stays in every Unresolved line until a review or the
   pre-check covers it (learnings §44). Alternatively, set `REDTEAM_*` before `/create-scenario`.
4. **Scope exclusions to confirm:** investors, ad networks (including Singular, SC-39), Mattel and unanswered cold
   pitches stay out of the population. Confirm, or name any you want in.

**Next step:** run `/create-scenario`.

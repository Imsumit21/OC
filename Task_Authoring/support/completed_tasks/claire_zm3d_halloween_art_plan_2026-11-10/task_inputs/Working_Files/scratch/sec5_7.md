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

≥ 500 necessary calls are not reachable without padding. Recommended volume exception (`GEN_EXECUTION.md` §3a,
`references/Hardness_Manifest_Spec.md`): `{call_budget_floor: 120, per_record_floor: 40}`. Every other extreme target
stays:
- ≥ 10 services weighted / injected;
- cohort ≥ 40 × ≥ 3 surfaces over ≥ 2 services, by rule, with a shortcut audit per surface;
- ≥ 12 fragments over ≥ 7 services and ≥ 10 containers;
- 2–4 hidden authorities with decoys;
- ≥ 3 chains;
- ≥ 12 traps in ≥ 7 families;
- ≥ 120 INSERTs.

Golden-run rule: a correct run needs the per-record phase too, since each surface's call depends on its own evidence.


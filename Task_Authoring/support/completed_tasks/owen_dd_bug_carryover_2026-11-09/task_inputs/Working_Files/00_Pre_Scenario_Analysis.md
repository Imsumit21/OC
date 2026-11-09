# Pre-scenario analysis: Owen Baker · Engineering · Engineering Ops · Actions (analysis only)

Contains no prompt, Oracle Event or criterion text. Written 2026-11-07 for `/create-scenario`; revised the same day after the requester set stricter targets.
Probabilistic numbers are labelled **UNCALIBRATED**: they are design aids, not measured rates (learnings §9).
Evidence is in `Working_Files/00_PreScenario/`: reach census, identity resolution, can-see proofs, stored-run exposure, the eight-task table, the sketch builder, sketch manifest and surface, the Hardness v2 checker output, and the policy model with its output. The first sketch is kept in `00_PreScenario/superseded_v1/`. Cross-task lessons are in `Working_Files/00_Completed_Task_Learnings.md`.

**Terms used below.**
- **Canvas:** Vincent's Slack bug list "Bugs on Android 2231", read through its comment channel `CE156FDFB428`.
- **Tree:** `ENG-2401`, its three UI masters (`ENG-2403`, `-2404`, `-2405`) and their 28 children.
- **Public line:** the branches Domino Delights (DD) Android submission builds are cut from.

**What changed in this revision.**

| Area | First analysis | Now | Why |
|---|---|---|---|
| Targets | < 85 %, ≥ 100 calls on the golden run | **< 80 %, over 130 calls in every run**, E[avg] ≤ 72 % | Requester, 2026-11-07 |
| Job | Only still-broken bugs go to Linear | **Every canvas line and later bug gets a Linear record**, and every tree child gets a one-line note | Writes set the weakest run; about 46 writes gave a weakest run near 110 |
| Traps | Eight, rates from design judgement | Eight, rates from measured carriers. Inline PR comment and unrelated-thread reply added; the deck-only tree trap and the unproven flicker trap dropped (flicker is a spare) | Julia's judgement traps never landed; Douglas's inline comments did |
| Rubric shape | Controls at weight 3 | Sampled controls at weight 1, a mean lever plus a spread lever, and a row budget | Only Douglas met all three targets; per-target rows lifted Robert LLC to 83.6 % |
| Decisions | Six open | **All six made under the requester's delegation** (§11) | Requester, 2026-11-07 |

## 0. Assignment and context (verified)

| Field | Value |
|---|---|
| Persona | Owen Baker, Game Engineer (Unity), `owen.baker@harmonygames.co` (roster `owen_baker`) |
| Function / competency / skill | Engineering · Engineering Ops · **Actions** |
| Horizon / mode | Long Horizon (`effective_profile: extreme`, GEN §3a) · **medium**: platform cap < 85 % |
| Requester targets | **Over 130 counted calls in each run; average strictly under 80 %; every other difficulty guideline.** Design target E[avg] ≤ 72 % |
| Universe | `normal`, hg4-2026-08-31 v37. Clock and seed bound 2026-02-14 00:00 UTC (Fri Feb 13, 4:00 PM PT). Shutdown rules apply |
| Persona today | Saturday, February 14, 2026; "yesterday" is Fri Feb 13 |
| Source | `task_context.py --task-dir Task_Authoring/task_inputs --write --require-source`: status `ready`, KB `bound`, context_hash `ba6bb23d4a12…` |
| Tools | Last `Task_Authoring/tools` commit is c16c7a1. Universe content was read through `hg.py` and `persona_view.py`. The only other touch was one read-only directory listing of the Slack export. The Evals input store was not touched |
| Red team | `REDTEAM_*` is unset (0 variables), so `redteam_review.py --dual` cannot run (§11) |

**What I could not do.**
- `/prompt`'s deep recheck reads git, but I ran no git, as GEN §1 requires. Two trap facts therefore rest on PR records, #builds and Slack, not on branch containment (§11, item 6).
- Canvas bodies are not in the export (`F09GAFM2DRR` has `content_inline: None`). Only canvas lines that drew a comment can be seen.
- The STEP 0.6 duplicate check cannot be run locally.

**Originality.** Samuel's analysis supplied the format and the model engine only; no fact came from it. Neighbours to stay clear of are Robert's two close-outs, Douglas's server sign-off and Julia's difficulty register. A bug list moved out of Slack is a different job from each, but the score is unmeasured.

## 1. What a 5 needs at each gate

| Gate | What a 5 / PASS needs | Risks specific to this task |
|---|---|---|
| `/injection` | No seed contradicts any base record anywhere. Each seed is dated after the base events it relies on, follows schema and id contracts, and has no event timestamp after the clock. Companions are seeded, and no closed ticket takes later activity | NB-1 and NB-6: seeds go in DMs or before Feb 11, all before Feb 13 10:03 UTC. Vincent's Slack voice stops at Nov 23, 2025 (his last record of any kind is Dec 2). Tree children closed Nov 14 take no later comment. INT-01 mirrors stop Dec 26, so PR comments dated before that need Slack copies |
| `/prompt` | Fit (hard gate), UGT, feasibility, cross-service coherence, natural voice, originality below 0.80, and no rules, traps or answers in the prompt | Coherence is the main exposure: tree tickets sit in state PR with merged PRs (hazards L01, L03, L07). The shutdown must be acknowledged, never business as usual. Owen's channel access after Feb 11 is the top-failing card (NB-1, 37 FAILs). A reviewer must see a real reason for filing already-fixed lines, or calls it padding (§7) |
| `/hardness` (one pre-check) | PROCEED (3–5): the run misses weight-5 rows for real reasons | One cause under 15 % loss caps the score at 2 (memory: hardness-opus-sweep-pattern). Only INLINE (17.0 %) and FILT (15.6 %) clear 15 % alone (§6). A rule doc that names sources sent Opus straight to the answers on Samuel's and Robert's tasks, so it stays plain definitions |
| `/oe` | Each step discoverable from the prompt or an earlier step's Expected data, with accurate tools, parameters and values | Canvas lines contain tokens (`[PERSON_NAME_1711]'s treasure hunt`), so they are never Expected values. Branch names follow NB-13. About 110 write events must stay under the field limit |
| `/rubric` | Atomic "The Agent …" rows, weights by kind of work, ≤ 5 samples per group plus a volume row, no count bundled with an identity, one order row per write kind, no do-nothing rows, no predicted all-fail | The largest risk to the average: one row per target where write content differs. Template-identical writes keep it sampled (§8). Apply learnings §60–62 from the start |
| `/create-difficulty` | Six Opus 5.5 slots, **corrected average under 80 %**, < 5 full passes, population SD 0.10–0.30, ≥ 2 failure patterns (largest ≤ 50 %), **every run over 130 counted calls**, ≤ 2 errored | Only 1 of 8 completed tasks met all three targets (§6). Near-certain misses add no spread, so they are capped at about 15 % of the weight |

## 2. Owen's reach at the clock

Census output is in `00_PreScenario/reach_owen.txt` and `entity_owen.txt`. Proofs are in `cansee_anchors.txt`.

- **Slack.** 116 visible channels (25 public, 34 private, 30 mpim, 27 IM), 16,295 own posts, last post 2026-02-12.
  - YES: DM with Arthur `D05S1S2AB5M`, DM with Vincent `D06ULGYJHJS`, canvas `CE156FDFB428`, #god-bugs `C05V5FNLB9V`, #builds `C05433XK267`, #prototype `C09UHHN6PFZ`, the BoomBit channel `C09SWTHEMEW`, #dd-road-to-sub-250mb `C09Q4S613CN`.
  - **NO:** #winddown `C0ADGSZKR3R` and #executives `C07C2866011`. Leonard's "linear we keep during transition" (`C0ADGSZKR3R/1770933601.686309`) is in #winddown, so a seeded record must restate it.
  - **Feb 11 change (NB-1).** Owen left six channels on Feb 11: #god-gameart, #engineering-bots, #company-internal, #god-bugs, #zombie-match3d and #zombie-bugs. Leonard then made him a single-channel guest (`C09UHHN6PFZ/1770842566.250369`), but `channels.json` still lists him. No leave message exists for the canvas, #builds or the BoomBit channel. The card's safer ground is "#prototype, their DMs, or anything before Feb 11". Every Slack record this task relies on is dated before Feb 11 or sits in a DM.
- **Gmail.** 1,595 threads, 1,633 messages (2023-09-14 → 2026-02-10), 7 threads last active in Feb 2026. Mostly automated notices. Base thread files are named `owen@harmonygames.co_*`.
- **Calendar.** 511 event rows, 143 distinct, last before the clock 2026-01-01. Nothing after it, so a Monday invite must be seeded.
- **Drive family.** He owns 10 items, including his root `d_4e13bd40cc73d0fc76f87c` (YES, owner): the proven write home. 134 items are shared with him, including "Economy Changes for Domino Delights" `f_948768f5a462e7037d17c9` (YES, and it names him for the play button). "DD QA Checklist" `f_5ad74e75c94ee1fe949b4f` is UNVERIFIED (domain only), so it is never load-bearing.
- **Unscoped.** Linear `usr_4e13bd40cc73d0fc`: 404 issues assigned, 36 open. GitHub `PERSON_5877_GITHUB_USERNAME`: 508 PRs. Trello `919ee44a0d5157b7839f66a8`. Confluence `user_EMPLOYEE_0021`. Contacts `4e13bd40cc73d0fc76f87c7d`.
- **His remit at the clock.**
  - He holds 16 of the 28 tree children.
  - The canvas mentions him, and his fixes are in its threads ("Should be fixed now", `CE156FDFB428`, Nov 19).
  - He owns open loose ends: "I think I forgot to exclude them from the MegaTile" (`C05V5FNLB9V/1764262971.568809`), plus the flicker and music threads under Robert's Dec 2 posts.
  - He is still working: `Combo-Fighters#37` merged Feb 13, and his last DM to Arthur is Feb 12.
- **Who can speak in seeds.** Active in Feb 2026: Arthur, Leonard, Robert, Oliver, Brian, Julia, Martin, Marcus. Quiet: Vincent and Douglas (Dec 2025), Samuel and Calvin (Oct 2025).

## 3. Storylines and recommendation

| # | Storyline | Fit (Engineering & Live-Ops inside Engineering Ops) | Reach and data | Originality | Hardness raw material | Verdict |
|---|---|---|---|---|---|---|
| **A** | **DD bug record moved out of Slack.** Slack history is going and DD's bug record lives only there. Owen files every canvas line and later bug in Linear with the right state, and brings the UI tree up to date | Strong on both sides: tickets and epics for a live game. Linear tickets are the competency's expected output | Best of the three. 63 canvas lines, 7 later bugs and 32 tree records, all real and reachable | A job the neighbours don't ask for. Unmeasured | Real base decisions: ticks against later facts, "did a PR" against an open PR, a system the live build no longer has, existing tickets under other words | **Chosen** |
| B | Owen's ticket hand-over. All 36 open tickets on his name get a state, a new owner and a note | Strong | Good, but 22 of the 36 have no linked PR and 9 have not moved since before October, so most calls would rest on one rule | Weak: closest to Robert's "settle each issue" jobs | Thin. State lag is the main source, and it is base noise rather than a decision | Rejected |
| C | Repo move sweep. Open PRs and unmerged work before Arthur moves the repos (`C05KNDCHAAG/1770842137.835489`) | Good on tooling support | Only 16 repos and 9 open PRs. `github_list_branches` and `github_compare_commits` ran in 0 of 48 stored runs, so feasibility is unproven | Low: too close to the banned 133-PR residue register | Volume-shaped | Rejected |

Also screened and rejected:
- Combo Fighter backlog into Linear: "Combo Unlocking Specs" `F0ADJNKH5JN` has no body in the export, and 12,172 #prototype messages leave status undecidable.
- Crash triage: redaction noise.
- A Remote Config audit: banned by the calibration list.
- Helpshift removal: its records are in #winddown, which Owen can't see.

**Why A.**
- The need is real at the clock. Leonard can't drop Slack yet ("can't switch to free account yet", `C09UHHN6PFZ/1770842590.881439`) and asked about going to free with no history (`C0ADGSZKR3R/1770839825.928989`). Linear went quiet on Nov 7, so the record lives in Slack.
- BoomBit wants a sync mid next week (`C09SWTHEMEW/1770977006.104929`), so DD stays live.
- It is the only storyline with about 110 honest per-entry writes that survive every trap, which is what the 130 floor needs.
- Most traps come from base records rather than invention, so seeds are few.
- Domino Delights clears the theme screen, which the Zombie Match storylines do not.

**Base facts behind A (all read through `hg.py`).**

| Fact | Record |
|---|---|
| 63 canvas lines: 55 ticked, 8 unticked. They are `document_comment_root` messages, and thread replies carry the fixes | `CE156FDFB428` (Nov 13–21) |
| Vincent posted the list as "the new issues or the remaining ones"; Julia later called #god-bugs the place to see where things stand | `C05V5FNLB9V/1763042988.277099`, `/1764091385.285289` |
| Android submission builds came from `Blake/boombitWithEcon` from December (10 of 13 that month, then every build to #309), then `Blake/boombitFixAddressables` (#310). None names `develop` | #builds Dec–Feb; `C09SWTHEMEW/1770753609.436139` names 0.3.305 as the latest public build |
| The economy change replaces lives with tickets. PR #1914 from `EconomyChanges` is still open, and the BoomBit channel describes the change in December | `f_948768f5a462e7037d17c9`; `GameOfDominoes#1914`; `C09SWTHEMEW` Dec 2025 |
| Three unticked canvas lines are about lives | `CE156FDFB428/1763548856.943389`, `/1763642552.651279`, `/1763642659.467529` |
| Marcus says he fixed the tile dozer window and did a PR; that PR is still open | `C05V5FNLB9V/1764329192.159229`; `GameOfDominoes#1913` |
| Open tickets cover canvas lines under other words: sign-in sync, splash hang, addressables, lives | `ENG-2073`, `ENG-2280`, `ENG-2363`, `ENG-2345`, `ENG-2277`, `ENG-2400` |
| 19 tree children are open. 12 trace to merged PRs (10 by key, 2 by the #1907 branch name); 7 have no linked PR | `ENG-2424`, `-2427`, `-2428`, `-2429`, `-2430`, `-2431`, `-2437` |
| Bugs raised after the canvas stopped: mega tile, tile dozer window, flicker, music, acid animation, treasure button, Android bottom bar | `C05V5FNLB9V` Nov 27–Dec 22 |

## 4. UGT plan (rule 1)

1. **Population from a record.** Arthur's seeded DM defines it by role: lines on the canvas, plus DD bugs raised since. It lists no members. Completeness is claimed only over the 63 commented lines and a census of later bug posts, never over the canvas body (learnings §23).
2. **One closed decision set in a rule record, not the hub.** A seeded doc maps each outcome to a Linear state with a one-line test: fixed, still broken, no longer in the live build, already covered by a ticket. Plain definitions only; item-level resolvers stay out (memory: hardness-opus-sweep-pattern).
3. **Every created or updated value comes from a record.** Team, parent, label, state and the note template are fixed by the rule doc. Canvas wording is never graded verbatim.
4. **Forks to settle with dated records before `/prompt`:**

   | Fork | Settled by |
   |---|---|
   | What "still broken" means: `develop` or the build players have | Rule doc, in plain words |
   | Whether a tick is a status | Rule doc: a tick stands unless a later record about that bug says otherwise |
   | Lives lines against open `ENG-2277` and `ENG-2400` | Rule doc on systems no longer in the live build, plus whether those two tickets change at all |
   | Reuse target among `ENG-2073`, `-2280`, `-2363`, `-2345` | A dated note on the right ticket tying the line to it |
   | iOS-only lines ("Core game music", thread says ios) | Rule doc: platform scope |
   | Robert's music, acid and flicker threads, which never closed | A dated record each, or they stay carried under the tick rule. The #builds flicker fix is not yet proven to be the same bug, or to be on the public Android line |
   | Android bottom bar (60 replies, unresolved; Leonard's Feb 12 post is vague) | A dated record naming the outcome |
   | Which open children may go Done, and the 7 with no linked PR | Rule doc test, then a census of each child. Season Pass is not proven: Brian listed it as not started on Nov 19, yet #builds shows a Season Pass text fix (DD Android #2240) |
   | Master states and checklists | Never graded (NB-14); child states only |
   | Other canvases | ZM Collect & Win (27 lines) is another game. Economy Bugs and Bug Checklist are channels Owen isn't on. The rule doc scopes them out |
   | Share list for the sheet | The seeded Monday invite's attendees |

5. **Apply each rule sentence to every item.** Before SQL, run the fork sweep over all 63 lines, the 7 later bugs and 32 tree records, including a whole-universe search for later records on each line (learnings §21–22).
6. **Keep off the graded path.**
   - Snowflake and Confluence stay out. `CLIENT_ERROR_EVENTS` would join warehouse versions to Slack builds (NB-21).
   - No exact branch name is graded (NB-13).
   - No claim about DD's owner after the shutdown: IP goes to auction (`C07C2866011/1770850800.723979`), so seeds say only that the bug record must outlive Slack.
   - Cards touched: NB-1, NB-6, NB-13, NB-14, NB-21, NB-24 (all Linear comments are seeded), NB-31. Hazards: L01, L03, L07, K01.
7. **Two blind sweeps before `/injection`** (memory: blind-sweeps-catch-base-contradictions): forks from persona-visible dumps only, then seeded-versus-base coherence over the full base.

## 5. Hardness plan (rule 4, Hardness v2)

Eight channels, the limit for the mutation and forecast tools. Each moves ≥ 2 rows including a weight-5 row. `BASE` marks a real record and `NEW` a planned seed not yet checked against the whole universe. The landing rate is the chance a run misses it, taken from the nearest measured carrier in `00_Completed_Task_Learnings.md`.

| Channel | v2 trap | Convincing wrong source (who, when) | Record that beats it (who, when, authority) | Rows it moves | Placement | Landing |
|---|---|---|---|---|---|---|
| INLINE | **1 · Proving "done" across services** (A24) | BASE merged tree PR; NEW Brian's sprint wrap deck (Nov) | NEW inline review comment on that PR (Nov) showing a required piece never landed; the review body stays silent | Two children held (5, 5), ticket for the piece (5), names it (3), tree total (5) | Inline comments were read 1–4 of 20 on Douglas; review bodies are swept | 0.85 |
| REPLY | **2 · A correction somewhere else** (A11) | BASE a ticked line, picked after the fork sweep | NEW Brian's later reply under an unrelated sub-250 MB post, without canvas words | Carried (5), reason (3), still-broken total (5) | Caught 2 of 8, then 3 of 6 on Bridge | 0.60 |
| BACK | **2 · A correction somewhere else**, separate line and carrier (A11) | BASE a second ticked line | NEW Vincent's last 1:1 note to Owen (by Nov 23), using the screen's nickname | Carried (5), reason (3), still-broken total (5) | 1:1 DM, about 3 of 6 on Bridge | 0.50 |
| FOLLOW | **3 · Follow-through a rule requires** (A15) | NEW the rule doc asks for a note on each child, so any note seems enough | NEW comment by Brian on a sprint Trello card (Nov): the note must name the build checked | Note volume (5), two samples (3, 3) | Card not named; `trello_get_comments` ran in 18 of 48 stored runs | 0.50 |
| GONE | **5 · A rule hidden in older records** (A15) | BASE unticked lives lines (Vincent, Nov 19–20) and open `ENG-2277`, `ENG-2400` | BASE economy doc (Leonard, last modified Dec 12) plus #builds showing the public line | Three line calls (5, 5, 3), still-broken total (5) | Survives retrieval, but judgement joins rarely land (Julia), so rated low | 0.35 |
| LINE | **1 · Proving "done" across services**, second member (A24) | BASE Marcus: fixed and did a PR (Nov 28) | BASE `GameOfDominoes#1913`, still open | Carried (5), names the PR (3), still-broken total (5) | A done claim against a stated rule is usually caught (Bridge) | 0.30 |
| FILT | **7 · Items outside the obvious filter** (A17) | BASE the canvas as the whole list | BASE later #god-bugs posts, brought in by Arthur's scope | Mega tile (5), bottom bar (3), acid (3), both totals (5, 5) | Opus reads #god-bugs if nothing stops it | 0.30 |
| ALIAS | **6 · Different names for the same thing** (A7) | BASE no ticket carries the canvas wording | BASE `ENG-2073` and `ENG-2363`, plus NEW dated notes tying each line to its ticket | Two reuse rows (5, 5), tickets-filed total (5) | Titles share "sign in"; ledger mean 0.20 | 0.20 |

**Spare channel (not modelled).** ELSE, v2 trap 9: Owen's flicker thread stops at "testing a fix now", while #builds shows a fix (`C05433XK267/1764977839.069349`, `/1765310004.760809`). It replaces a weak channel only if the fork sweep proves it is the same bug.

**Two levers.** INLINE is the mean lever: runs will usually miss it, so it pulls the average down but adds little spread. REPLY, BACK, FOLLOW, GONE, LINE and FILT are the spread lever, each found by a different habit: opening a thread under an unrelated post, reading a 1:1 DM, reading a card comment, asking what the live build contains, looking a PR up, reading past the canvas.

**Controls and decoys** (learnings §41): ticked lines with no later record, unticked lines still carried, children whose merged PR really is done, the ZM Collect & Win canvas, the wrap deck, and ticket lookalikes on sign-in. Finding a bug's records never marks a trap by itself.

**Independence.** GONE and LINE share one habit, asking what the live build contains; REPLY and BACK share "a tick means fixed" but need different reads. The model tests correlation at rho 0.6. No single channel is above 18 % of the sketch weight even with its totals. The hub delegates by role and names no location.

**Survives complete retrieval.** GONE and ALIAS need a join after every record is read. LINE needs the run to treat a claim as unproven. INLINE, REPLY, BACK, FOLLOW and FILT are retrieval-shaped and depend on placement, which is the measured route to a landing.

### Part 7 checks: `hardness_v2_check.py --design` on the pre-scenario sketch

The sketch (`00_PreScenario/sketch_manifest.json` and `sketch_surface.json`) is **not** the `/create-scenario` manifest or surface. Output, verbatim:

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      4 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 5 requirements: {'R5': ['INLINE'], 'R2': ['REPLY', 'GONE', 'LINE'], 'R6': ['FOLLOW'], 'R1': ['FILT'], 'R3': ['ALIAS']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   8 of 8 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     4 weight-5 total(s); 4 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

**Dispositions.** No FLAG or UNRESOLVED fired, but this is weak evidence: the tool reads what I declared.
- SAME_PLACE covers declared containers only and must be re-run on the SQL. LINE and ALIAS declare no version records, so it did not judge them.
- TWO_DECISIONS omits BACK because the sketch lists it in Slack only (a canvas line against a DM). It is cross-container, not cross-service, so count seven cross-source channels, not eight.
- RULE_IN_PROMPT re-runs once a prompt exists.

## 6. Spread and score plan (rule 5, UNCALIBRATED)

**What the completed tasks say.** Only Douglas met all three targets (56.3 %, SD 0.117, weakest run 163). Bridge met the first two but had a 109 run. Both kept all-pass weight near or below about 60 %, and Douglas paired all-fail weight with mixed weight. The full table is in `00_Completed_Task_Learnings.md`.

`00_PreScenario/policy_model.py` scores the 47-slot sketch surface: total weight 135, 75.6 % flippable by mechanisms, using a Gaussian-copula run latent and 3 % base slips. Output: `policy_model_output.txt`.

| Whole policy | Score |
|---|---|
| Perfect | 100 % |
| Canvas ticks at face value, nothing else | 24.4 % |
| Thorough, never opens threads under unrelated posts or other DMs | 67.4 % |
| Stays inside the canvas, otherwise thorough | 72.6 % |
| Reads everything, never asks what the live build contains | 80.7 % |
| Reads PR reviews but never inline comments, otherwise perfect | 83.0 % |
| Right calls, misses the note rule | 91.9 % |

| Single miss | INLINE | FILT | GONE | ALIAS | REPLY | BACK | LINE | FOLLOW |
|---|---|---|---|---|---|---|---|---|
| Score | 83.0 % | 84.4 % | 86.7 % | 88.9 % | 90.4 % | 90.4 % | 90.4 % | 91.9 % |

**No single miss gets under 80 %.** Ten pairs stay at or above it. **Every set of three misses is under 80 %.** Expected misses per run are 3.60 at carrier rates.

Six-run Monte Carlo at carrier rates (mean 0.45). P(> 130) is the chance all six runs clear the floor, and P(all gates) includes both requester targets.

| Landing scale × rho | Mean landing rate | E[avg] | P(< 80 %) | P(SD 0.10–0.30) | P(< 5 full) | P(patterns) | P(> 130) | P(all gates) |
|---|---|---|---|---|---|---|---|---|
| 1.00 × 0.30 | 0.45 | 60.5 % | 1.00 | 0.88 | 1.00 | 1.00 | 1.00 | 0.88 |
| 1.00 × 0.60 | 0.45 | 61.0 % | 0.98 | 0.95 | 1.00 | 1.00 | 1.00 | 0.93 |
| 0.80 × 0.35 | 0.36 | 67.9 % | 0.93 | 0.93 | 1.00 | 1.00 | 1.00 | 0.87 |
| 0.70 × 0.35 | 0.32 | 71.7 % | 0.85 | 0.93 | 1.00 | 1.00 | 1.00 | 0.80 |
| 0.60 × 0.35 | 0.27 | 75.5 % | 0.70 | 0.91 | 1.00 | 1.00 | 1.00 | 0.67 |
| 0.60 × 0.60 | 0.27 | 75.9 % | 0.65 | 0.92 | 1.00 | 0.99 | 1.00 | 0.62 |
| 0.50 × 0.35 | 0.23 | 79.3 % | 0.51 | 0.87 | 1.00 | 0.99 | 1.00 | 0.49 |
| 0.40 × 0.35 | 0.18 | 83.2 % | 0.30 | 0.80 | 1.00 | 0.99 | 1.00 | 0.29 |

**Targets.** E[avg] ≤ 72 % holds down to about 0.70×, and P(all gates) ≥ 0.5 down to about 0.50×. A second view using ledger family means gives 69.9 % and 0.85 at 1.00×, and 78.3 % and 0.53 at 0.70×.

**One pre-check.** Under the narrow-miss rule, a run needs two causes or one cause losing ≥ 15 %. Under independence that happens with P = 0.98 at carrier rates, 0.86 at 0.70× and 0.68 at 0.50×.

**The biggest threat is rubric growth, not traps.** If /rubric forces always-pass per-target rows, the same runs score higher and SD falls:

| Always-pass weight added | At 1.00×: E[avg] / P(all) | At 0.70×: E[avg] / P(all) |
|---|---|---|
| +30 | 67.7 % / 0.78 | 76.8 % / 0.59 |
| +60 | 72.7 % / 0.59 | 80.4 % / 0.36 |
| +100 | 77.3 % / 0.29 | 83.7 % / 0.12 |

**The honest read.** The under-80 % target is likely but not assured.

| Measured | Per-trap landing | Scale here |
|---|---|---|
| Bridge rev12 batch 2: three traps, each missed 3 of 6 | 0.50 | about 1.1, passes |
| Bridge rev10–12 pre-checks: one trap missed per run from about three | about 0.33 | about 0.7, passes at P(all) about 0.80 |
| Frederick rev3 pre-check: 1 of 8 landed, before de-naming | 0.125 | about 0.28, **would fail** |

**Calibration caveats.**
- Ledger priors are thin: `done_gap` 0.50 (n_eff 4), `superseding` 0.17 (n_eff 4), `completion_elsewhere` 0.20 (n_eff 3), `exact_predicate` 0.33 (n_eff 4), `scope_alias` 0.20 (n_eff 3). `house_rule` has no prior.
- Carrier rates come from other tasks, and memory records that exposure moves between revisions. REPLY and BACK sit above the `superseding` prior because of placement, which is a judgement.
- INLINE assumes runs keep reading review bodies but not inline comments. If this task's PR reads go further, its weight comes back and the average rises.
- `/create-scenario` S9b's pre-registered forecast replaces this sketch.

## 7. Volume plan

Honest necessary calls, with no padding:

| Phase | Services | Calls |
|---|---|---|
| Discovery and rules: Arthur's DM, rule doc, note rule, invite, tree parents, labels, statuses, users | slack, gdocs, gdrive, trello, gcal, linear | ~16 |
| Census: canvas pages, #god-bugs, #builds searches, open ENG tickets, PR search, economy doc, BoomBit posts, wrap deck | slack, linear, github, gdrive, gdocs, gslides | ~28 |
| Per record: comments on 32 tree records and ~12 reuse candidates; PR, reviews and inline comments on ~13 merged PRs; ~20 thread reads | linear, github, slack | ~103 |
| Writes: a Linear record per line (63) and later bug (7), child moves (~14), child notes (28), sheet and move (3), share (1), reply (1) | linear, gsheets, gdrive, slack | ~117 |
| Read-backs | linear, gsheets | ~6 |
| **Total** | 10 services | **≈ 270** |

**Over 130 in every run.** Writes set the weakest run: the lowest read counts were 54 on Bridge, 61 on Q4 and 69 on Robert LLC. The 70 records and 28 notes have no batch form and do not depend on any trap, apart from 7 lost if FILT lands. The model resamples stored read counts and gives a mean six-run minimum of about 177, with P(all six over 130) = 1.00 in every scenario.

**Why this is not padding.** Each record is a distinct bug, and each note a distinct ticket. The reason is real: the fix history exists only in Slack, and Slack history is going. Arthur's record must say so, because the Evals anti-inflation check (`long_horizon.md`) asks that every repeated call answers a distinct question no bulk result can replace.

**If a reviewer rejects filing fixed lines.** Filing only the still-broken lines cuts about 55 writes, and the weakest run falls to about 116, under your floor. That is why I keep it, and it is the first thing to watch at `/prompt`.

**≥ 500 necessary calls are still not reachable without padding.** A volume exception is taken in §11.

**Floors the exception does not lower**, with where each stands:

| Target | Plan | Status |
|---|---|---|
| Cohort ≥ 40 × ≥ 3 surfaces over ≥ 2 services | 102 records: 63 lines, 7 later bugs, 32 tree records. Surfaces: Slack line, Linear ticket and comments, GitHub PR, #builds | **Passes** on real records |
| ≥ 10 injected schemas, without Confluence or Snowflake | slack, gmail, gcal, gdrive, gdocs, gsheets, gslides, trello, linear, github | Reachable. Gmail's role is the thinnest and needs a real one at `/create-scenario` |
| ≥ 120 INSERTs | Estimated 110–135, mostly per-child sign-off notes, PR comments with Slack copies, and control notes | **Tight, and no exception covers it.** If honest evidence falls short I will bring that back, not pad |
| ≥ 12 fragments over ≥ 7 services, 2–4 authorities, ≥ 3 chains, ≥ 12 traps, ≥ 4 supersessions, ≥ 6 distractors | Rule doc, note rule and economy doc as authorities; eight channels plus base chains | To be built at `/create-scenario`; not yet counted |

## 8. Rubric shape plan (no criterion text)

The sketch surface has 47 slots. These rules keep the final rubric near it:

- **Row budget:** about 50–60 rows, with no more than about 30 weight of always-pass rows beyond the sketch (§6). Re-run the model on the real row count before any baseline.
- **Template-identical high-count writes:** fixed lines share one template, and child moves and notes share one each, so each group is sampled at ≤ 5 plus a volume row.
- **Per-target rows only for trap members.** Everything else stays in a sampled group.
- **Reply carries counts, never a member list.**
- **Weight mix to aim for:** about 45 % all-pass, 40 % mixed, 10–15 % near-certain miss. Weights follow kind of work and are never raised.
- **All-fail budget:** INLINE's rows may fail all six runs. That is legal when VALID, and `/create-allfail` will need to justify them.

## 9. Injection plan (rule 3)

- **Census every seeded entity across the whole universe**, with hits read rather than counted (learnings §10, §38). Absence checks carry a positive control (§35).
- **Date each seed after the base events it relies on.** Arthur's ask goes after Owen's last DM (Feb 12 22:21 UTC) and before Feb 13 10:03 UTC. Thursday afternoon PT keeps the PT and UTC days equal.
- **Sprint-era seeds stay in the sprint.** Trello went quiet Nov 13 and Linear Nov 7, so notes date from November, and none lands on a ticket after it closed (§50).
- **Claims about code stay observational**, and `tools/base_claims.py` runs before any solver work (§49).
- **Pair each GitHub comment with its INT-01 copy** in #engineering-bots and declare exceptions (§53). That copy is a second, noisy route to INLINE.
- **Keep the task's own words out of hidden corrections**, such as canvas, Android 2231 and bug (memory: hardness-opus-sweep-pattern).
- **No fact only on Confluence or only in a GCal description** (§26; memory: injection-stage-tool-gotchas).
- **Confirm the agent's tools return each record.** Canvas lines came back through `slack_search_public_and_private` in a stored run, and FC channels appear in channel listings, but a direct read of this channel is unproven. Check it in the pre-check, along with write results and fallback events.

## 10. Writes (rule 6)

| Write | Authorized trigger the persona owns | Access proof needed |
|---|---|---|
| A Linear record per line and later bug | Arthur's DM | `linear_create_issue` (team, parentId, labels, state). Only 2 stored calls, both clean, so confirm volume in the pre-check |
| Note on a reused ticket | Rule doc | `linear_create_comment`: 523 stored calls, 0 errors |
| Tree child state moves | Arthur's DM | `linear_update_issue`: 339 stored calls, 0 errors; confirm state names |
| Note on every tree child | Arthur's DM (FOLLOW sets what it must name) | `linear_create_comment` |
| Bug sheet in Owen's Drive | Arthur's DM | New file under `d_4e13bd40cc73d0fc76f87c`, Owen as owner in Drive and Sheets rows. `gsheets_create_spreadsheet` takes `driveFileId`, and `gdrive_move_file` is the fallback; confirm at scenario |
| Share with Monday's attendees | Seeded invite | `gdrive_share_file`; Owen owns the file |
| Reply to Arthur | Arthur's DM | DM `D05S1S2AB5M`, YES; `slack_send_message` |

## 11. Choices made under the requester's delegation

The requester wrote on 2026-11-07: "you can choose from your self which option is best fit for my requirements in this task". Each choice below is made under that delegation.

| # | Choice | Reason |
|---|---|---|
| 1 | **Storyline A**, in its whole-canvas form | The only one with honest writes for the 130 floor and real cross-source decisions |
| 2 | **Volume exception:** `volume_exception {call_budget_floor: 250, per_record_floor: 200}`, reason "about 102 cohort records and 270 honest calls; reaching 500 would need padding, which fails on its own", `requester_confirmation` quoting the line above | ≥ 500 is not reachable honestly |
| 3 | **Review waiver:** record `RED TEAM UNAVAILABLE` and a `RED TEAM FALLBACK:` line naming the two blind sweeps, the whole-universe census and the policy scores. It stays in every Unresolved line until a review or the pre-check covers it (learnings §44) | `REDTEAM_*` is unset |
| 4 | **Accept the NB-1 position.** Every Slack record relied on predates Feb 11 or sits in a DM, and nothing grades who could read what | The card's own safer ground. Still the largest `/prompt` risk |
| 5 | **Repair L01 and L03 in the SQL:** merged tree tickets move from PR to Validation | `repaired` is the only verifiable resolution for tickets the task touches |
| 6 | **One read-only check through `base_claims.py`'s own helper at `/create-scenario`**, for two facts: that #1913's change never reached the public line, and that the public line carries the economy change. No hand-run git. If the helper can't answer, the check moves to `/create-injection` | A wrong answer changes LINE and GONE |

**Next step:** run `/create-scenario`.

**Updated at `/create-scenario` (2026-11-07).** The two blind sweeps changed the design after this analysis: the Tavern correction moved to Marcus, FILT became a control with the three-member ELSE rule in its place, ENG-2424 stays open because Win & Collect was disabled on Dec 16, so 23 children end Done, the rule doc gained a first-fit outcome order, and `per_record_floor` is 100, not 200, because the gate counts read surfaces only. `01_Scenario_Design.md` is the current record.

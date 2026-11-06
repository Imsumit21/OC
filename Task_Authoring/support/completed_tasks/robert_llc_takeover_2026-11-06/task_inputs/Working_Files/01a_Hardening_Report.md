# 01a Hardening Report: robert_llc_takeover rev3, platform pre-check intake

## 1. Mode, inputs and run validity

**MODE B (pre-check).** This is one platform Opus 5.5 run on rev3. The platform `/hardness` scored it 2 (FAIL, HOLD, INSUFFICIENT_DIFFICULTY). No baseline exists yet.

Assignment: Robert, Co-founder & Creative Director · Executive / Finance / Planning and decision support · Long Horizon · Easy · Feb 14, 2026, normal universe. The universe manifest is `Evals/references/universes/normal/universe_manifest.json`, and `Working_Files/00_Task_Context.json` has context_hash 226493b2011a.

**Inputs read**
- `00_Assigments.md`
- `01_Universe_Inject.sql`: rev3, sha256 4236a0301de9.
- `01_Grounding_Dossier.md`, `01_Hardness_Manifest.json`, `01_Gradable_Surface.json`, `solver/truth.json` and `solver/solver.py` (bd2aeedab6f8).
- `04_Prompt.txt`: sha256 ccd229a59a17.
- `03_Error_Async_Config.txt`: Friction: none.
- `06_PreCheck_Trajectory/trajectory.json`: sha256 53c30765e132. The user uploaded it as `Run1_trajectory.json`, and it is byte-identical to the file `/hardness` reviewed.
- The `/hardness` report, archived as `run_forensics/rev3/precheck/1a_hardness_FAIL_r3.md`. Its clock line is `Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)`.

**Inputs missing** (expected before a baseline):
- `07_Baseline_Trajectories/`
- `10_Baseline_Verifier_Results.md`
- `12_Difficulty_Stats.txt`
- `08_Oracle_Events.md` and `09_Rubrics.json` (both are still empty templates)

**Run validity (B0)**, from `trajectory_ledger.py` (`run_forensics/rev3/summary.json`):
- Harness claude-code 2.1.280, cwd /app, session 6832431f.
- Every message comes from claude-opus-5-5: no fallback, no subagent, mixed_model false. v3_valid is VALID.
- The run completed: 496 events, a result event at 495, no compaction and nothing after the result.
- The prompt matches by content (event 3 reads Leonard's DM `D04UP2L3E3S/1770961200.890407`).
- Binding: BOUND to rev3 on discriminating content (12 rev3-only needles seen; rev1 7573eb1a6bca and rev2 edf1fd903611 were passed and excluded).

**The intake's six results**
1. Binding: BOUND:rev3.
2. Mixed model: none.
3. Proposals: `node_verdicts` proposed BYPASSED for all 7 mechanisms. Every proposal was rejected on review and dispositioned by hand (section 4). The cause is a decoder keying defect: the run's sheet keys carry an ` (ENG-n)` suffix, so no register component matched.
4. Deliverable diff: `surface_grader` reported 48.8%. After confirming each failed slot against the write payloads, the corrected score is 77.4%, or 85.5% clean (section 2).
5. Ledger: 15 records. Seven are verdicts:
   - `hev_3a71c99557336ba6` CORR
   - `hev_2da16037a402bf13` AUTH
   - `hev_b76760802056e969` FILT
   - `hev_d2253957e65e0329` COMPLETE
   - `hev_f9b2298b6c9739d4` DONE
   - `hev_9cefe52f59fd5be5` EXC
   - `hev_3d96146a0a8b19a5` DATE

   Eight are control trials, all HELD: `hev_18c2a36c3a23255a`, `hev_6f55bab68d100cea`, `hev_aac1a9ad3a3ae51f`, `hev_0113860a70c7256d`, `hev_1da52d9f1038274a`, `hev_f0e8cf90a2d0b077`, `hev_041489b38be208ad` and `hev_7abcab0748fdbb60`.
6. Posterior forecast: `hev_51611d00e3779d1d`, pre-registered. V3 E[avg] is 0.876–0.901 and P(all gates) is 0.000–0.005 (UNCALIBRATED). The call is **NO-GO**; see section 13.

## 2. Gate status and clean average

There is no baseline, so no figures exist from a `12_Difficulty_Stats.txt`. The pre-check is graded only as a design check and never enters the six-run gates.

| View | Score | Basis |
|---|---|---|
| `/hardness` reviewer (platform) | about 96% right, 1 independent cause, failed share about 4% | its requirement map of about 45 core items |
| `surface_grader` raw | 48.8% (41/84) | decoder output, see below |
| surface, decoder corrected | 77.4% (65/84) | every failed slot checked against the write payloads |
| surface, clean | 85.5% (65/76) | R1 and R5 removed as CONFOUNDED-fairness: the rev3 prompt never asks for them |

**Decoder corrections**, each confirmed against the sheet write (opus · event 316) and the reply (opus · event 492):
- **Wrongly failed:** G1, G2, G3, I3, I4, I5, P1, V1 and D1, plus I1 and I2 on labels.
  - G1/G2/G3: the CF, DD and ZM rows read LLC, LLC and HG.
  - I1: Metabase is labelled "One of us", the project description's own wording for Founder.
  - I2: Calm Play is labelled "Not used" and set to Canceled at event 482, which is the HG class.
  - I3/I4/I5: Figma, Helpshift and Cursor are all HG.
  - V1: there are 7 LLC rows.
  - P1: CF stacks read 62. The `[ $]62` pattern misses CSV-joined text.
  - D1: the sheet was created by `gsheets_create_spreadsheet` with owners robert@ and no parent, which is My Drive root. The decoder cannot see the parent, so this slot is UNGRADED, not failed.
- **Wrongly passed: C4.** The layer.ai pattern ran across rows and matched "Feb 25" in the Kapwing row. The layer.ai row carries no date.
- **Genuinely failed: C3, R6 and C4.**
- **Confounded: R1 and R5.** R1 asks for "$3,202 March cash need" and R5 for "campaign is most of the cash". The rev3 prompt asks only "what it costs each of us a month", and brief §4b accepts the thirds or the cash. Neither slot is incorporated.

**Mechanism weight share:** 88% of the clean surface weight sits on mechanism slots (67/76). Slots that depend on a node that landed (DONE or DATE) hold 18.4% (14/76). The surface weights traps far more heavily than the reviewer's per-item map does. That is one reason the pre-run forecast (E[avg] 0.852–0.881) was far too pessimistic against a run that got about 96% right.

## 3. Predicted /hardness band

**Predicted band: 2 (HOLD)**, the same as the platform score.

| # | Requirement | Expected source | Run (opus · event) | Outcome |
|---|---|---|---|---|
| Q1 | Find the request and its inputs | DM `D04UP2L3E3S/1770961200.890407`, ground rules `f_1e468a9d69ea0f0a2001f5`, draft `f_d996e4c434ce160dc52596`, split email `robert@harmonygames.co/1856989298688559716`, card 456 | events 6–35, 168 | MET |
| Q2 | DD and ZM take test | REVENUE_DAILY January: DD 183.11 vs $140, ZM 0.00 | event 180; writes 316, 358, 432 | MET |
| Q3 | Hidden VO campaign, plus a new issue | `C09UHHN6PFZ/1770938400.370665` | found at event 44; ENG-2475 created at 319 | MET |
| Q4 | Items already carried | Arthur's $248 email `robert@harmonygames.co/1856975772058401508` | event 256; Done at 368–372 | MET |
| Q5 | Monthly only, #winddown decisions, Calm Play, Figma | ground rules and #winddown `C0ADGSZKR3R` | events 405–486 | MET |
| Q6 | DD player support | App Store notice `robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com>` | snippet only at 269; "already live" at 316, 342, 405, 492 | MATERIAL_FAIL (F1) |
| Q7 | layer.ai export date | base #prototype `C09UHHN6PFZ` 2026-02 /575: "access until March 3rd" | never seen (0 hits); no date at 316, 336 | MINOR_GAP (F2) |
| Q8 | Sheet, shares and reply | split email: $1,150 each, $902 cash | events 314–330, 492 | MET |

Grouped causes:
- **F1** is the only material cause.
- **F2** keeps the substance: "pull ... out before that access ends" at event 336. The `/hardness` reviewer scored the matching requirement R9 MET.

On Easy, one cause below 10% loss is capped at 2. A score of 3 needs a second independent material miss, or a loss of 10% or more.

## 4. Designed-difficulty register

All seven mechanisms were dispositioned by hand. The tool's BYPASSED proposals were all rejected, for the reason given in section 1. The run has one rollout, so each verdict covers 1/1.

| Mechanism (nodes) | Verdict | Evidence (opus · event) | v2 failure kind |
|---|---|---|---|
| CORR A11 (T1, T8, T15) | LEAKED | opus · event 211: the search `from:Arthur after:2026-02-08` returned the seeded $140 reply `D04V95AAAHW/1770952200.665739` first, even though it sits under an older thread root. The ground rules' "going by whoever runs it" (event 22) sent the run to the owner. The draft was used only for layout (event 24), and Confluence (T15) was never opened. | on_delegation_path: the rule named the authority, and an owner search carried it |
| AUTH A13 (T2, T11, T12) | LEAKED | opus · event 180: the ground rules (event 22) name "January" and "the warehouse's daily revenue table", and one query returned DD 183.11 / ZM 0.00. The February partial month (T12) and BoomBit (T11) were never used. | on_delegation_path |
| FILT A17 (T3, T9, T16) | LEAKED | opus · event 44: the run's second Slack search was the project word "LLC". Hit 2 was the seeded VO reply ("moves to the LLC from March ... count it in what the LLC costs"). New issue at 319, $3,000 row at 316. Unity's $100 and the $3,750 vendor were kept off the plan (events 427, 429). | keyword: the hidden record repeats the task's anchor word |
| COMPLETE A25 (T4, T14) | LEAKED | opus · event 44: the same search returned base #winddown `C0ADGSZKR3R/1770937232.664809` ("moving github, dbt and Metabase to my KubLLC card"). Gmail search at event 247 and the $248 thread at event 256 followed. Done + Arthur at events 368–372; $902 cash in the reply at 492. | keyword, via a base lead that cannot be reworded |
| DONE A24 (T5) | LANDED | opus · event 269: the App Store notice was listed at event 265 and fetched as metadata only (snippet "Thank you for submitting your items for review"). Its Guideline 1.5 body was never read. Arthur's "done" comment (read at event 141) was taken as final, and the run wrote "already live" or "already met" at events 316, 342, 405 and 492. That is one cause with four outputs. Status Todo / Arthur / Feb 28 is correct (event 362). | live: a bland vendor snippet, off the keyword path |
| EXC A15 (T6, T13) | FALSE | opus · event 425: the ground rules read at event 22 say "The LLC is the new one Blake and I are setting up for the three of us", which rules Calm Play out before its issue note is met. The 2023 #admin_foundersonly ownership records were never opened. Decision HG / Canceled is correct (event 482). | on_delegation_path, never live |
| DATE A4 (T7, T17) | LANDED (minor) | opus · event 316: the layer.ai row has no owner or date, and the CF row dates the move "When Sunset's sale closes". The ENG-2454 comment's "before the access ends" (read at event 125) did not send the run looking for the date. T17 held: the GitHub repos move after the data is delivered (event 354). | live, low weight |

**Per-node counts** (completed rollouts: 1)

| Node | Count |
|---|---|
| CORR | leaked 1 (opus · event 211) |
| AUTH | leaked 1 (opus · event 180) |
| FILT | leaked 1 (opus · event 44) |
| COMPLETE | leaked 1 (opus · event 256) |
| DONE | landed 1 (opus · event 269) |
| EXC | false 1 (opus · event 425) |
| DATE | landed 1, minor (opus · event 316) |
| Confounded | none (opus · event 2 to event 492, every call read) |
| Not reached | none (opus · event 492, the run completed) |

## 5. Per-rollout ledgers

The call ledger is `run_forensics/rev3/precheck/calls.jsonl`, with decoded writes in `writes.json` and briefs in `briefs.json` (none, since there were no subagents).

| Phase | Events | Calls | What the run did |
|---|---|---|---|
| Request and hub | 2–35 | 14 | DM read (spilled result, read back with Bash at events 8–10), LLC project, ground rules, draft, Monday notes, issue list, split email |
| Sweep | 42–86 | 15 | Gmail and Slack searches for "LLC"; #winddown read in full in concise form (events 64, 69); #executives from Feb 7 (event 79); "lifestyle" search; one #prototype thread |
| Linear comments | 92–166 | 37 | `linear_list_comments` on every issue, ENG-2438 to ENG-2474 |
| Data | 168–182 | 6 | Trello search for "LLC"; Snowflake: tables, a failed query (event 176), describe, the January query (event 180), MONTHLY_BURN |
| Owner checks | 211–274 | 16 | `from:Arthur` search (event 211), Arthur DM, Calm Play search (event 231), ledger queries (event 239 failed), github/metabase/dbt mail, mail list since Feb 9 (event 264), batch metadata fetch (event 269) |
| Writes | 293–492 | 87 | sheet create and fill (314–330), shares (326, 328), new issue (319), 38 comments, 37 state updates, backlog check (489), threaded reply (492) |

Where it stopped looking: it never opened #prototype history or the 2023 Calm Play ownership threads, never ran a Slack search for "layer", "campaign" or "support", and never opened a Gmail body from Apple.

## 6. Friction, tool defects and horizon

- **Friction:** none was configured (`03_Error_Async_Config.txt`). No async or forced-error paths apply.
- **Tool defects that changed no outcome:**
  - Two Snowflake query errors from invalid column names (events 176 and 239); the run recovered at events 180 and 242.
  - Two result spills ("exceeds maximum allowed tokens", events 6 and 44), read back with Bash.
  - The sheet's own `#NAME?` formula, fixed at events 324 and 330.
- **Horizon:** 175 raw calls, of which 5 are harness Bash and 2 are blocked (errored). That leaves 168 counted calls (`counts.counted`), above the Long Horizon minimum of 100 and the requester's target of over 130.
  - 112 of the 168 are per-issue Linear calls (37 list-comments, 38 comments, 37 state updates). The horizon therefore comes from the 37-issue structure itself and should hold across runs.

## 7. Verifier sanity

There are no verifier results yet. One reviewer-level observation: the `/hardness` reviewer scored R9 (dates) MET, but the layer.ai row has no date (Q7/F2). Its R11 attribution (F1) matches this report. Two decoder issues (section 2) are routed to the gradable surface, not the verifier.

## 8. Why Opus passed

`hardness_v2_check.py --task-dir Task_Authoring/task_inputs` (rev3):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      6 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 6 requirements: {'R3': ['CORR'], 'R10': ['AUTH'], 'R6': ['FILT'], 'R11': ['COMPLETE'], 'R2': ['DONE', 'DATE'], 'R8': ['EXC']}  [Part 5 rule 1]
  FLAG       DECISION_FLIP   6 of 7 rules can flip a weight-5 slot; not: ['DATE']  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

DECISION_FLIP DATE disposition: confirmed. The run shows it too. DATE landed, but the platform did not count it, because the miss changes no status or number. Rebuild RB4 in section 10 addresses it.

**Each trap that was caught, and how** (all citations are opus · event):

| Trap | Classification | How it was settled |
|---|---|---|
| T1 | universe leak, on_delegation_path | The ground rules' "going by whoever runs it" plus a `from:` owner search (event 211) returned the correction directly. |
| T2 | universe leak, on_delegation_path | The ground rules name the table and the month; one query (event 180). |
| T3 | universe leak, keyword | The hidden record contains "LLC" twice; the first keyword search returned it (event 44). |
| T4 | universe leak, keyword, base lead | Base "KubLLC card" post (event 44), then a Gmail search by item names (event 247). The lead is base data and cannot be reworded. |
| T6 | never live | The ground rules state the vehicle (event 22). |
| T8 | genuine capability | The draft was used only for layout; the costs came from the owners' later records (events 211, 256). |
| T9 | rule stated | The ground rules say "no one-offs or yearly fees" (event 22, write 427). |
| T16 | same_container | The VO reply itself says only the VO campaign is still on (event 44). |
| T17 | genuine capability | The #winddown checklist was read in full (events 64, 69). |
| T10–T15, T18 | not reached | The $25K recap (January #executives), BoomBit, the February partial month, the 2023 lookalike, the Confluence estimate and Leapblock were never met. The run's direct route made them unnecessary. |

**Heavy rows (weight 5) that passed:** G2 DD decision, I1 Metabase, I2 Calm Play, C1 campaign $3,000, C2 DD $140, L1 new issue, R2 Arthur's $902. The rebuilds below add none of these.

**Measured habits of this run:**
- Its first two searches use the project word: Gmail "LLC OR Sunset ..." and Slack "LLC".
- It reads the comments on every Linear issue.
- It reads #winddown in full.
- It searches by owner (`from:`) when a rule names the owner as the authority.
- It lists all of Robert's mail since Feb 9 but fetches bodies only for mail whose snippet looks relevant.

## 9. Purge list

This is a proposal; `/create-scenario --revise` decides.
- **EXC (T6): rebuild, not purge.** It is FALSE in this run because the ground-rules sentence "The LLC is the new one Blake and I are setting up for the three of us" (`f_1e468a9d69ea0f0a2001f5`) settles Calm Play on the delegation path. The Calm Play row and its decision stay, so it is a rebuild (RB3), not a purge.
- **T10–T15, T18: no purge yet.** They were never reached, and one run cannot show whether they are dead. A purge decision waits for the baseline.

## 10. Proposed rebuilds

These are Hardness v2 moves only: no added rows, items, steps or volume, and nothing spelled out in the prompt. Every change must also keep each fork settled by a dated record, so `/prompt` keeps its 5.

- **RB1, FILT T3: take the project word out of the hidden record.**
  - Reword the seeded #prototype reply `C09UHHN6PFZ/1770938400.370665` (row `6908b2f17c379e809aafa6b2b169f4bf`) so it no longer says "LLC". It must still name the VO campaign, Meta, $100/day and the $3,000 cap. It must still say the cost leaves Leonard's card in March and that the founders carry it if CF continues.
  - This is a mechanism fix, not a block on one query: "LLC" is the anchor word every run searches first (event 44).
  - Facts changed: none.
- **RB2, DONE T5: make the miss change a status.**
  - Redefine Done in the LLC project description (project `0fa95761-d59b-4ff4-a8a3-15df3210ca6e`) as "nothing left to do, because one of us already carries it or it has already moved". Arthur's "done" comment on ENG-2462 then reads as Done unless the App Store notice is read. With the notice, the answer stays Todo / Arthur / Feb 28.
  - Keep the notice's bland snippet; it is what worked.
  - Alternative (B): the fix carries a monthly cost, so the miss changes the total and all three shares. That is heavier, but it ties DONE to the total and share cells.
  - Facts changed under the recommended option: the project description wording only. Each Done item must be re-checked: GitHub, Metabase and dbt stay Done.
- **RB3, EXC T6: move the vehicle answer off the delegation path.**
  - Drop "the new one ... setting up" from the ground rules, and say the LLC is the one the three founders will own together.
  - Keep "anything Harmony Games owns ... comes only through Sunset's sale". The 2023 #admin_foundersonly records (`C04UEQVDVB7/1701383740.580749`, `C04UEQVDVB7/1703492127.063049`) then decide that Calm Play is an HG subsidiary, against the ENG-2472 note and the Monday notes doc `f_a7af6f358dd5648c11a608`.
  - The miss would flip a status (Canceled vs Todo) and the LLC row count.
  - The brief must re-check that "which LLC" stays settled (Arthur's KubLLC, Blake LLC).
- **RB4, DATE T7: remove the visible caveat.**
  - Change the ENG-2454 comment to state only the cancellation.
  - Move "CF's character source art only lives in layer.ai" into a dated record off the swept path, for example a reply under the base layer.ai post `C09UHHN6PFZ` 2026-02 /575. The art export and its Mar 3 date then depend on a record the run does not sweep.
  - The miss would drop a required action, not just its date.
  - The fairness link stays: the ground rules say "brings what it needs to keep running", and card 456 says an item keeps its own deadline.
- **RB5, a correction elsewhere for an item already costed (from the `/hardness` advice).**
  - The CF stacks figure ($62) comes from Arthur's own comment on ENG-2445, which the run reads (event 106). A later, dated correction off the swept path, from the same owner and naming the stacks, would replace it.
  - A run stops hunting once it has a figure, so this lands more often than a hidden-only answer.
  - Facts changed: the CF stacks cost, the total, the thirds and Arthur's cash.
- **Keep CORR, AUTH and COMPLETE as they are.**
  - CORR and AUTH carry the DD decision, which is about 35% of the reviewer's answer. Making them harder would concentrate failures on one cascade, which is the failure-pattern risk the platform flagged.
  - The COMPLETE lead is base data.
  - The failure-pattern risk should instead fall as RB2–RB5 move weight onto statuses and numbers that other traps decide.

**Expected effect** (UNCALIBRATED, guessed from this run's habits, not measured):

| Rebuild | Guessed catch rate |
|---|---|
| RB1 | about 0.5 (the run's "card" search could still reach the reply) |
| RB2 | about 0.3 |
| RB3 | about 0.6 (the run did search "Calm Play" at event 231) |
| RB4 | about 0.4 |
| RB5 | about 0.5 |

That gives P(perfect run) of about 0.02 and about 2.4 expected misses per run. Each miss changes a status or a number.

## 11. Routing

This is a proposal; `/create-scenario --revise` (S0r) decides.
- **Universe changes (RB1–RB5):** go to `/create-scenario --revise` from S5a with a `design_delta`, then `/create-injection` as rev4, then `/injection` and `/prompt` as a pair. Before `/prompt`, run both blind sweeps again: the fork sweep, then the base-coherence sweep.
- **Gradable-surface defects.** These go to `/create-scenario --revise`, which owns `01_Gradable_Surface.json`:
  - R1 and R5 are not incorporated in the rev3 prompt. Retire them, or tie them to an asked output.
  - The Decision comparator needs the labels the project and draft use ("One of us", "Not used").
  - Register keys need to tolerate ` (ENG-n)` and ", AWS" spellings.
  - C4 and P1 need per-row matching, not matching across rows or joined CSV text.
- **Prompt-side defects:** none. `RULE_IN_PROMPT` is CLEAN, and the prompt passed `/prompt` with every dimension at 5. The over-findable rules sit in the ground-rules doc, which is a universe record.

| # | Quoted span | Rule (doc §) | Defect | Evidence (rollout · step) |
|---|---|---|---|---|
| 1 | "the ground rules doc has how we decide" | none | none: the delegation is fair, and its target is fixed universe-side by RB3 | opus · event 22 |

- **OE and rubric (later stages):**
  - Accept "One of us", "Founder" and "Not used" as labels.
  - Do not require $3,202 or the tradeoff in the reply.
  - Grade the DD support next step (a support build approved before Feb 28) and the layer.ai date.
  - Never grade wording, row order or branch names.

## 12. Self-review

Walked against `Evals/1A_Hardness_Eval.md` §3–§5 and playbook 01a Self-review.

| Verdict | Counter-reading | Resolution (evidence) |
|---|---|---|
| DONE LANDED | Strongest counter: tool. Maybe the batch fetch could not return the body. | Event 269 asked for `format: minimal`; the run then used `gmail_get_message`, which returns the body, for one calendar mail at event 271, but not for the Apple notice. The body is in rev3 SQL line 86 ("Guideline 1.5 ... only opens an email draft"). This is a genuine retrieval failure. |
| DONE LANDED | Fairness counter: maybe "already live" is a fair reading of Arthur's comment plus PR #1917. | The App Store notice is dated Feb 13 07:30 UTC, after the comment (2026-02-13T01:30:00Z, event 141), and it is in Robert's inbox, listed at event 265. The ground rules say a game that comes over brings "its player support". The fair answer is the open release step. |
| DATE LANDED | Counter: it would pass, because "before that access ends" (event 336) keeps the substance. | Agreed for `/hardness`: graded MINOR_GAP and not counted toward the band. It stays LANDED on the surface, since C4 failed once the decoder was corrected. The date is in base `C09UHHN6PFZ` 2026-02 /575, re-verified with hg.py search-many ("March 3rd"). |
| CORR LEAKED | Counter: never live, because the ground rules point to the owner. | It was live: the stale ~$1k (notes doc `f_a7af6f358dd5648c11a608`) and "maybe 300" (draft) were on the path first (events 24, 26). The run beat them with an owner search (event 211). This is LEAKED, not FALSE. |
| AUTH LEAKED | Counter: FALSE, because the rule names the table. | The decision still needed a query and a comparison (event 180), and it drives G2, G3, R4 and R7. It is coupled, not trivially satisfied, so it stays LEAKED. |
| FILT LEAKED | Counter: a decoy was never on the path. | The "turn the VO campaigns off?" decoy (T16, `C07C2866011/1770438169.228649`) was never met, and the run took the answer from the reply that came back at event 44. The leak is the keyword, which RB1 addresses. |
| COMPLETE LEAKED | Counter: the lead is base data, so the trap was never live. | The lead `C0ADGSZKR3R/1770937232.664809` is base, re-verified with hg.py search-many ("KubLLC"). The $248 amount and "counts toward his third" exist only in the seeded email `robert@harmonygames.co/1856975772058401508`, which needed its own Gmail search (event 247). This is LEAKED; no rebuild is proposed. |
| EXC FALSE | Counter: it would pass as LEAKED, since the run did search "Calm Play" (event 231). | Its comment at event 425 cites the ground rules, not ownership, and the "new one" sentence is in `f_1e468a9d69ea0f0a2001f5` (rev3 SQL line 17). The resolver was verbatim on the delegation path, so it was never live: FALSE. |
| Proposals BYPASSED | Counter: the tool might be right that the register held none of the components. | The sheet at event 316 holds all 38 rows; keys such as "Combo Fighter (ENG-2438)" do not match the truth key "Combo Fighter". This is a decoder keying defect, so every proposal was rejected. |
| R1/R5 CONFOUNDED | Counter: they would fail fairly, since brief §4b line 66 lists "LLC cash $3,202". | The prompt (`04_Prompt.txt`) asks only "what it costs each of us a month", and §4b accepts "either or both share readings". A row requiring $3,202 or a tradeoff is unauthorized, so CONFOUNDED-fairness is confirmed. |
| Band 2 | Neighbouring band 3: F2 is a second independent cause (a different item and source). | The run's ENG-2454 and ENG-2438 comments say to pull the art "before the access ends", so no wrong instruction results. The platform scored the matching R9 MET. One material cause below Easy's 10% loss stays at 2. |
| Band 2 | Neighbouring band 1: the run is fully correct. | F1 leaves a false "solved" statement in four outputs while App Review blocks support with the Helpshift cut-off on Feb 28 (`C0ADGSZKR3R/1770789534.434749`). That is consequential, so the band is 2, not 1. |

- **Cascade check:** F1 is counted once, although four outputs carry it (events 316, 342, 405, 492). No CONFOUNDED item is counted toward the band.
- **Write-payload grep:** a search of all 38 comment bodies, the sheet and the reply for "layer", "Mar 3", "support build", "App Review" and "rejected" found only the four F1 lines and the two layer.ai lines without a date.
- **Re-verified records:**
  - Through hg.py search-many on Slack: the "March 3rd" note at `C09UHHN6PFZ` 2026-02 /575, and the KubLLC post at `C0ADGSZKR3R` 2026-02 /204.
  - In the rev3 SQL: the seeded App Store body (line 86), the ground-rules sentence (line 17) and the VO reply (line 46).
  - The $140 reply text, from the run's own result at event 211.
- **Mechanical checks:** `trajectory_ledger.py` and `node_verdicts.py` were re-run once, after the output folder was corrected; their inputs are unchanged since. `surface_grader.py` was run once. Nothing in the SQL, solver or surface changed, so no injection check needed re-running beyond the gate's own re-run.
- **Calls not reviewed:** none. All 175 calls and every write payload were read; the queue's register events 316 and 324 were reviewed.

Unresolved:
- The posterior forecast still grades R1 and R5 as natural failures; it becomes usable once the surface is fixed.
- The catch rates for RB1–RB5 are guesses from one run.
- Whether T10–T15 and T18 are live needs the baseline.

```
STAGE GATE hardening: PASS — Task_Authoring/task_inputs · 01a_Hardening_Report.md#ea55f2ba0d17 · 01_Universe_Inject.sql#4236a0301de9 · 01_Hardness_Manifest.json#5852f07809be · 00_Assigments.md#97be9960492b · 01_Grounding_Dossier.md#6d460491b510 · 06_PreCheck_Trajectory#8ffe5b572b0e · 07_Baseline_Trajectories#ad7848c1ad99 · 10_Baseline_Verifier_Results.md#e3b0c44298fc · __context__#226493b2011a · __assignment__#b4220a529c0a · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#ee46d7814b64 · blocking 0 · warnings 0 · checks 17
[PASS] assignment.v3_context: Robert / Co-founder & Creative Director; easy cap <90%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#4236a0301de9, 01_Hardness_Manifest.json#5852f07809be, 01_Grounding_Dossier.md#6d460491b510, solver/solver.py#bd2aeedab6f8, 01c_Dispositions.json#9849267e3b62, 01c_Preflight_Report.json#03c79f55e534, 00_Assigments.md#97be9960492b, 01_Scenario_Design.md#a99f8c32e6f5, 01_Hardness_Manifest.draft.json#a0c1e6ecaa00, 01_Gradable_Surface.json#ba791eaea9ec, __context__#226493b2011a, __assignment__#b4220a529c0a, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#ee46d7814b64)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 16/16 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 11 evidenced counter-readings (of 12 found; need ≥ 7) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13. Next steps

1. **Go / no-go: NO-GO.** Spending the baseline needs all of the following, and three fail:
   - `/hardness` of 3 or more: it is 2.
   - Corrected proxy at most cap − 5 = 85%: the clean surface is 85.5%.
   - At least 2 independent loss channels landed: DONE and DATE do (they share no key or source). This one holds.
   - P(all gates) of 0.8 or more: it is 0.000–0.005.

   This was pre-check 1 of the 2 allowed for this scenario.
2. `/create-scenario --revise` takes in this report's verdicts, dispositions RB1–RB5, and fixes the gradable surface (section 11).
3. `/create-injection` makes rev4. Then run `/injection` and `/prompt` together, after the fork sweep and the base-coherence sweep.
4. Re-apply the rev4 SQL on the platform, run one new Opus 5.5 pre-check, and send `/hardness` again.

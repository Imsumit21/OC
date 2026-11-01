# Hardening Report — fs-paid-ua-trueup (revision N+1)

## 1 · Mode, inputs and run validity

MODE B (pre-check): one Opus 5.5 trajectory, no baseline. Verdicts below are for this run only, and no gate statistics are computed.

| Input | State |
|---|---|
| `06_PreCheck_Trajectory/trajectory.json` | read in full: 513 events, 148 tool calls (121 main agent, 27 subagent). sha256 97ab2a788f77, the same run the platform `/hardness` report reviewed (Evals key `opus` rev 13) |
| `04_Prompt.txt` | sha256 0b197d44d6af, unchanged |
| `01_Universe_Inject.sql` (v7, sha256 c983da3d0a7d) | the state the run saw. Backed up to `Working_Files/pre_hardening/01_Universe_Inject.v7.sql` |
| Platform `/hardness` report (2026-10-22) | NON-FAIL, Execution PARTIAL, Gate HOLD, INSUFFICIENT_EVIDENCE. Defects D1 and D2 |
| `07_Baseline_Trajectories/`, `10_Baseline_Verifier_Results.md`, `12_Difficulty_Stats.txt`, `08_Oracle_Events.md`, `09_Rubrics.json` | not present (pre-check stage), so parts B3d and B3e are skipped |
| `03_Error_Async_Config.txt` | Friction: none |

Run validity (B0):
- **Model and route:** `claude-opus-5-5` on every assistant message. One background general-purpose subagent, also Opus, extracted the Meta receipts (run-1 · event 200 → result used at event 434). Not a mixed run.
- **Hint status and source match:** the export has no user prompt. The first calls match the saved prompt (run-1 · event 2 `#executives` search, event 6 hub thread). The run saw SQL v7: the brief at run-1 · event 261 reads "Update Apr 28: ran on and off until April, now off.".
- **Injection applied:** seeded records come back. Examples: the hub at run-1 · event 7, the rules doc at event 16, the Unity statements at events 95–147, and the injected receipts showing `[IDENTIFIER_3125]` at event 308.
- **Completeness:** the run ends with a result event (run-1 · event 510) after its last writes (events 501–508). The subagent finished before the table was built (event 434 → event 483). There is no compaction.
- **Scope:** the export is complete, so omissions in it are evidence.

## 2 · Gate status

Pre-check only: no `12_Difficulty_Stats.txt`, so no pass@1, average or spread. The platform `/hardness` verdict is HOLD and does not clear the gate.

## 3 · Predicted `/hardness` band (B3c)

Requirement map for run-1. Requirements come from the prompt and the incorporated sources: hub C07C2866011/1759176840.271025, rules doc f_4591ef30be4f920ba1ed14, amendment C07C2866011/1759255500.938286, card 68c99c40e5d9eb6f3a988838 and its comment 68d195a805df8c30c455f99c.

| Req | Expected | Run-1 (event) | Outcome |
|---|---|---|---|
| Rules found, incl. amendment and tablet change | doc, reply, card 42 + comment, GCal review | events 7, 16, 37, 159, 242 | MET |
| Unity from statements, both accounts | 25 statements | events 95–147, sums at event 341 | MET |
| Adjoe ledger amount in invoice month | Apr 10,733.60 · May 20,537.92 · Jun 14,930.02 | events 243, 484 | MET |
| AppLovin / Google from ledger, game split | ledger rows + AD_SPEND_DAILY split | events 61, 66, 484 | MET |
| Buckets: card 42, tablet from Sep 18 | Fundraising $3,485.20 net | events 340–341, 506 | MET |
| Meta: credit = $0, duplicates once, PT month | rules applied | event 434 (credit 61.73, dup 2886.4), event 510 | MET |
| Meta account scope | every company-account charge (82 base + 20 seeded) | 82 base charges dropped as "non-3125" (events 434, 510) | MATERIAL_FAIL, CONFOUNDED (D1) |
| Register in the Q4 pack Marketing tab | rows in f_0cd1e1402e8052d3d4e903 | 403 PERMISSION_DENIED (event 358). Staging sheet written instead (event 501) | UNASSESSED (D2) |
| Thread reply + card comment with bucket totals | Fundraising 3,485.20 · Real UA 111,387.92 | events 506 and 508: Fundraising correct, Real UA 85,036.31 (follows D1) | MET on Fundraising. Real UA follows D1 |
| Accountant email after the sheet | mail to PERSON_6098_EMAIL | held (event 510) | UNASSESSED (D2) |

**Band for run-1: 1–2 (HOLD) once the confounded failures are dropped.** Every assessable requirement is MET, and the only material miss (account scope) is confounded by D1. Not band 3: band 3 needs one genuine consequential failure, and the account miss doesn't qualify because the incorporated wording "ending 3125" matched no company receipt the agent saw (run-1 · event 391).

**Predicted band for the hardened revision: most likely 1–2, with 3 possible.** D1 and D2 are fixed, and the only new lever is T23 (§10).
- **If T23 lands:** a run counts Leonard's personal receipts. Fundraising is then overstated by $426.15 (13%) and Real UA by $430.55, in the sheet, the thread reply and the card comment. That is one consequential failure with a bounded correction, so band 3.
- **If T23 leaks:** Opus grouped receipts by account in run-1 (event 434), and its extraction already flagged "different card: MasterCard · 4655" on Leonard's old receipts (event 422). It is therefore more likely than not to filter the decoys out, which gives band 1–2 again.

The honest reading is that this design now has one live lever for Opus. The other 21 designed traps leaked or were bypassed in run-1 (§4).

## 4 · Designed-difficulty register

Counts are out of 1 completed run. Leaked, bypassed and new nodes each carry their run-1 event.

| Node | Mechanism | Run-1 evidence | Verdict | L · C · Lk · B · NR |
|---|---|---|---|---|
| T1 'RE: meta Invoice' self-billing | keyword collision | never returned: no result in run-1 contains "meta Invoice"; receipts found by `subject:"ads receipt"` (run-1 · event 172) | BYPASSED | 0·0·0·1·0 |
| T2 Tipalti payouts | keyword collision | never returned (run-1 · event 172 search; no "Tipalti" in any result) | BYPASSED | 0·0·0·1·0 |
| T3 'Payment from AppLovin failed' | distractor | never returned; AppLovin taken from the ledger (run-1 · event 61) | BYPASSED | 0·0·0·1·0 |
| T4 duplicate receipt notifications | exact predicate | met and handled: duplicate refs counted once (run-1 · event 434 "dup 2886.4"; event 510 "counted it once") | LEAKED | 0·0·1·0·0 |
| T5 $224.59 Apr 6 not a duplicate | exact predicate | kept as a separate charge (run-1 · event 415 row with $224.59) | LEAKED | 0·0·1·0·0 |
| T6 Sep 19 rough rules / Adjoe wire month | superseding | read the old mail (run-1 · event 205) and the amendment (run-1 · event 242); invoice month used (event 484) | LEAKED | 0·0·1·0·0 |
| T7 tablet effective date | effective date | comment (run-1 · event 37) + GCal review (run-1 · event 159) → Sep 18 | LEAKED | 0·0·1·0·0 |
| T8 Snowflake $81,169 summary | stale summary | queried (run-1 · event 68), reported only as the comparison (event 510) | LEAKED | 0·0·1·0·0 |
| T9 Unity $0 in Snowflake | tool surface | read all 25 statements (run-1 · event 95 through event 147) | LEAKED | 0·0·1·0·0 |
| T10 Adjoe September spike thread | conclusion stop | the rep's reply was never returned; no September Adjoe row was built (run-1 · event 484) | BYPASSED | 0·0·0·1·0 |
| T11 PvZ / ADV / Node naming | scope alias | read all 18 briefs (run-1 · event 257 through event 291) | LEAKED | 0·0·1·0·0 |
| T12 Sep 30 4:40 PM PT charge | exact predicate | included (run-1 · event 308) | LEAKED | 0·0·1·0·0 |
| T13 Robert's Singular suggestion | non-authoritative instruction | read (run-1 · event 7), not followed (event 510) | LEAKED | 0·0·1·0·0 |
| T14 April DD incent split card | distractor | read both cards (run-1 · event 31), chose card 42 (event 510) | LEAKED | 0·0·1·0·0 |
| T15 reuse the true-up card | reuse exclusion | comment on 68dae1bc8ec7eb683dc15a8d (run-1 · event 508) | LEAKED | 0·0·1·0·0 |
| T16 Q3 pack format | superseding | used the Q4 header (run-1 · event 48 → event 501) | LEAKED | 0·0·1·0·0 |
| T17 Aug 6 ZM_UK near-miss | near-miss mention | the Aug 6 charge sits on 907669287942378, which the run excluded wholesale (run-1 · event 434), so the bucket call was never made | CONFOUNDED (fairness, D1) | 0·1·0·0·0 |
| T18 'Fb spend is like $20/day' | superseding | never returned (no "20/day" in any result); receipts used (run-1 · event 434) | BYPASSED | 0·0·0·1·0 |
| T19 Sep Unity phone/tablet split | synthesis omission | split by day (run-1 · event 341 "1630.75 1099.85") | LEAKED | 0·0·1·0·0 |
| T20 Unity top-ups as spend | exact predicate | top-up forward seen (run-1 · event 230), statements used (event 510) | LEAKED | 0·0·1·0·0 |
| T21 invoice PDF $12,005 vs ledger | superseding | PDF never opened; ledger 10,733.60 used directly (run-1 · event 243) | BYPASSED | 0·0·0·1·0 |
| T22 Calm Play stranded balance | distractor | never returned; Calm Play statements included (run-1 · event 109 through event 147) | BYPASSED | 0·0·0·1·0 |
| R1 Meta account scope ("ending 3125") | scope | runtime shows 907669287942378 on the 82 base receipts (run-1 · event 391); the run excluded them (event 510) | CONFOUNDED (fairness / tool surface, D1) | 0·1·0·0·0 |
| W1 Marketing-tab write | capability | 403 PERMISSION_DENIED (run-1 · event 358) | CONFOUNDED (tool / capability, D2) | 0·1·0·0·0 |
| T23 Leonard's personal Meta account (new) | lookalike entity | the "test account stays out" clause had no in-window record in run-1: only 907669287942378, 1096548511793203 (out of window) and the token appear (run-1 · event 434) | NOT-REACHED (new in this revision) | 0·0·0·0·1 |

Totals over 25 nodes: LANDED 0 · CONFOUNDED 3 · LEAKED 14 · BYPASSED 7 · NOT-REACHED 1.

## 5 · Per-rollout ledger (run-1)

| Step (event) | Tool | Input | What came back | Agent's decision | Requirement |
|---|---|---|---|---|---|
| 2, 6 | slack search / read_thread | `in:#executives UA`; hub ts 1759176840.271025 | hub with rules pointers (claim met first: Snowflake $81,169) | follows the hub | R1 |
| 15, 17 | gdrive read / list | rules doc; data-room folder | rules doc; folder listing showing Frederick as **reader** on the Q4 pack | rules adopted | R1–R12 |
| 19–37 | trello search / board / comments | "true-up"; UA/BD board | true-up card, card 41 (decoy), card 42 + tablet comment | card 42 governs | R4 |
| 38–50 | gsheets get / values_get | Q4 pack, Marketing, Summary | header A1:H1; Summary owner Frederick | target fixed | R9 |
| 54–68 | snowflake | ledger + AD_SPEND_DAILY | $81,168.77; ledger rows | Snowflake only for ledger networks | R6–R8 |
| 73–147 | gdrive search / read | Unity statements ×25 | all statements | Unity = statements | R6 |
| 155–159 | slack / gcal | "bucket review" | evt_2f9b60002516e45ff04160 Sep 18 | tablet from Sep 18 | R4 |
| 172–193 | gmail search / batch | `subject:"ads receipt"` | 107 receipts; three 400 errors (batch limit), recovered | hands off to subagent | R1–R2 |
| 200–434 | subagent (Opus) | full receipt extraction | CSV with account ids 907669287942378 ×85, token ×20, 1096548511793203 ×2 | groups by account; flags token-only as "3125" | R1 (D1) |
| 204–209 | gmail thread / confluence | Sep 19 mail; Singular page | old rules; connector gaps | doc supersedes mail; gap list | R5, R12 |
| 239–243 | slack search / snowflake | "adjoe invoice"; ledger | amendment reply; ledger Adjoe rows | invoice month, ledger amounts | R2 |
| 256–291 | gdocs ×18 | every brief | game per campaign | titles mapped | R3 |
| 312 | contacts | "accountant" | PERSON_6098 contact | recipient fixed | R11 |
| 358 | gsheets_values_update | Q4 pack Marketing!A1:H1 | **403 PERMISSION_DENIED** | staging sheet instead | R9 (D2) |
| 445–460 | slack / gmail search | "907669287942378", "meta test account", "ad account 3125" | adsmanager link (Node); 0 hits for test account and 3125 | excludes 907669287942378, flags the risk | R1 (D1) |
| 489–504 | gsheets create / update; drive share | staging sheet 68 rows; share to Leonard | written | new sharing (the doc says none) — caused by D2 | R9, R11 |
| 506, 508 | slack reply; trello comment | totals | posted | Real UA 85,036.31 (D1), Fundraising 3,485.20 | R10, R13 |
| 510 | final answer | — | — | email held; account risk stated | R11 |

Write payloads read: event 501 (68 rows + gap list, July Meta missing because of D1), event 506 (thread reply text), event 508 (card comment text).

## 6 · Friction, tool-defect and horizon checks

- **Friction:** none configured (`03_Error_Async_Config.txt`), so there is nothing to check.
- **Unconfigured tool behaviour:**
  - Gmail `format=full` is capped at 10 ids (run-1 · events 179, 181, 183), recovered by smaller batches. No outcome change.
  - Large results spill to file (events 25, 76, 227, 322 …), all read back. No outcome change.
  - `jq` is missing (event 27), recovered with python. No outcome change.
  - Wrong Snowflake column name (event 55), corrected. No outcome change.
  - **Outcome-changing:** the Gmail tool returns the raw Subject header (907669287942378), not the export's tokenised subject (D1, event 391). The Drive role for `shared_with_emails` is reader (D2, events 18 and 358).
- **Horizon:** 148 calls in the one run, all before the final answer. That meets the Long-Horizon floor of 100. There is no baseline count basis yet.

## 7 · Verifier sanity (B3e)

Not applicable: no verifier results exist at the pre-check stage.

## 8 · Why Opus passed

Each point Opus scored, and what made it possible:

- **Genuine capability:**
  - Read every thread reply (amendment, run-1 · event 242) and every card comment (event 37).
  - Opened the calendar for the tablet date (event 159).
  - Read all 25 statements and all 18 briefs instead of trusting Snowflake (events 95–147, 257–291).
  - Scripted the 107-receipt extraction, with dedupe, credit and PT month handled (event 434).
- **Universe leak:**
  - The rules doc states each house rule verbatim where the agent reads first (event 16).
  - The supersessions (Sep 19 mail → doc → reply; card 41 → card 42) are each announced in the newer record: "This replaces the rough rules", "This replaces the DD incent test split".
  - That converts every trap into reading comprehension, which Opus does well.
  - The seven BYPASSED distractors sit off the path a careful agent takes (ledger, statements, `subject:"ads receipt"`).
- **Prompt leak:** none found. The prompt names destinations only (`/prompt` NON-FAIL 3, every prompt dimension 5).

## 9 · Purge list

| Node | Evidence | Disposition |
|---|---|---|
| T1, T2, T3 | never returned (run-1 · event 172 route) | base records, so they can't be deleted. They stay as realism and are no longer counted as hardness levers |
| T10, T18, T22 | never returned (run-1 · events 242, 434, 109–147 routes) | base records. Same as above |
| T21 | PDF never opened; ledger read directly (run-1 · event 243) | seeded dispute thread kept (the Adjoe chain needs it). Not counted as a lever |

The manifest keeps these entries so `hardness_gate` structure checks still run. This report is the record that they carried no difficulty in run-1.

## 10 · Candidates and selection (rebuilds)

| # | Candidate | Coupling | Decision |
|---|---|---|---|
| 1 | Doc names Meta as "the company ad account Node runs for us"; seeded receipts carry the runtime id 907669287942378 | removes D1; identity checkable from the receipts (Node_/NM_ campaigns) and the base Slack adsmanager link act=907669287942378 (C07C2866011, 2024-10) | **selected (D1)** |
| 2 | Frederick owns the Q4 pack | removes D2; the Summary tab already lists Frederick as owner of the Paid UA section (f_0cd1e1402e8052d3d4e903 Summary!B5) | **selected (D2)** |
| 3 | Make the "my own test account stays out" clause live: Leonard's personal ad account 4417730962158804 (Jul 2 add-notice + five in-window receipts on Visa 7731 with ZM_UK names) | two incorporated rules interact. Card 42's name rule ("Meta ZM_UK campaigns, from Sep 12 on") pulls the decoys into Fundraising; the doc's account rule excludes them. One end state: excluded | **selected (T23)** |
| 4 | Reuse 1096548511793203 as the test account | the base names it "Domino Adventure" (gmail frederick.stone@harmonygames.co/1809398442244933472), a company game | rejected: coherence conflict |
| 5 | Doc says "ending 2378" | a trivial filter, with no judgement left | rejected: adds nothing for Opus |
| 6 | Stale account number in the doc plus a later migration mail | authoritative-but-wrong doc | rejected: Cross-Service Coherence and Unique Ground Truth risk at `/prompt` |
| 7 | Corrected Unity statement beside the original | the supersession would show in the folder listing (run-1 · event 85) | rejected: leaks the same way T16 did |

Lazy-solver pass on candidate 3: a solver that sums every "ads receipt" overcounts by $856.70 and fails. A solver that buckets by campaign name moves $426.15 into Fundraising and fails. Only a per-receipt account check passes, and the rules doc incorporates that check.

## 11 · Routing

**Universe changes made** (revision 1, sha256 cf3b678204ac; superseded by revision 2 below, now sha256 f941928e986a; `stage_gate injection` PASS pasted in the dossier):

| Change | Statements | Fact that changed (re-check prompt, OEs, criteria) |
|---|---|---|
| D1 | 40 occurrences of `[IDENTIFIER_3125]` in the 20 seeded receipt subjects and headers → 907669287942378; rules doc f_4591ef30be4f920ba1ed14 "Meta (our ad account ending 3125)" → "Meta (the company ad account Node runs for us)", style run end 1583 → 1596 | the Meta scope is the company account 907669287942378. Every in-window receipt on it counts |
| D2 | drive_files + sheets_spreadsheets f_0cd1e1402e8052d3d4e903: owner Frederick; shared with Leonard, Arthur, PERSON_6098_EMAIL | Frederick can write the Marketing tab. The accountant still needs no new sharing |
| T23 | +6 gmail threads and messages in Frederick's mailbox: notice frederick.stone@harmonygames.co/1836556159549956945; receipts frederick.stone@harmonygames.co/1838001810309861113 ($187.40), /1840483663872198178 ($243.15), /1843339041178378696 ($96.20), /1843719233863958066 ($158.65), /1844370651218486865 ($171.30) | these $856.70 are excluded. Revision 1 ground truth was Real UA $111,387.92, Fundraising $3,485.20; revision 2 corrects it (below) |

Manifest: R1 wording, fact `Meta company ad account` = 907669287942378, new fact `Leonard Hayes personal ad account`, new trap T23, and design_delta D1/D2/T23. `hardness_gate` (long) PASS; `fact_check --no-leak` PASS; `sql_lint` 0 errors; `base_check` PASS; persona check-sql PASS (175 load-bearing ids).

**Prompt-side defects:** none.

| # | Quoted span | Rule (doc §) | Defect | Evidence (rollout · step) |
|---|---|---|---|---|
| — | none | 1A §4 | the prompt was not a cause of any confounded failure; both causes are universe-side | run-1 · events 358, 391 |

**Routed OE and rubric observations (for later):**
- Grade Real UA at $95,612.56 and Fundraising at $3,376.20 (revision 2).
- Accept the D1 account by id or by description.
- Do not credit counting any 4417730962158804 receipt.
- No Sep 30 Unity figure exists (run-1 · event 510).


### 11b · Revision 2 (after `/prompt` rev 14 FAIL, Cross-Service Coherence 2)

The rev-14 review found two State / Lifecycle defects.
- **Revision 1 introduced the first.** "the company ad account Node runs for us" contradicts Frederick's Dec 20, 2024 termination of the Node agreement (gmail frederick@harmonygames.co_1818984698708007419.json /messages/8).
- **The second dates from the original design.** The Calm Play Unity statements billed full spend through the Aug 5 – 12 pause.

A full audit of the seeded spend against every dated on/off message in base #executives (C07C2866011) and the Leonard–Frederick DM (D05S58U4SAK) found the same pattern in more places. All are fixed from the source model (`support/task_work/fs_ua_trueup/model.py`; each window's deciding message is cited in `UNITY_CAMPAIGNS`):

| Fix | Deciding base record (PT) | SQL effect |
|---|---|---|
| Doc: "Node used to run for us" (style run end 1603) | Dec 20 2024 Node termination mail | wording only |
| Unity HG: iOS off Oct 12, Oct 22, after Nov 6; CPI off after Dec 2 18:30 and Dec 27 ("$1 ... to effectively stop", no rows) | C07C2866011 Oct 12 13:42, Oct 22 10:52, Nov 7 08:57, Dec 2 18:30; DM Dec 27 09:18 | HG statements 2024-10 … 2025-04 rebuilt |
| Unity Calm Play: on only Apr 18–20, Apr 23–25, May 3–7, May 16–20, May 28–31, Jun 3–6, Jun 11–23, Jun 29 – Jul 3, Jul 12–17, Jul 25–27, Jul 30 – Aug 4, Aug 13–21, Sep 12–19, Sep 29 | Apr 23 "live again", Apr 25 "paused", May 6/7, May 21 "paused yesterday", May 31 "Campaigns paused", Jun 6 20:54, Jun 11, Jun 24 "Pausing all UA now.", Jul 3/6, Jul 12, Jul 17 "$100 left", Jul 25, Jul 27 "campaign is paused", Jul 30 "Confirming UK Unity iOS is live", Aug 5, Aug 13, Aug 22 | 18 Calm Play statements rebuilt; Aug 22–31 and Sep 1–7 now $0.00 |
| Meta Aug 31 receipt covers Jul 18 – Jul 27 3:24 PM (was Aug 18 – 31) | Jul 27 15:24 "campaign is paused"; Aug 5 / Aug 22 pauses | same charge date and amount, so the August row is unchanged |
| Meta: no spend after Sep 26 14:35; daily receipts for Sep 26/27/28 removed; the Sep 30 4:40 PM charge is the month-end bill for the Sep 26 partial day ($25.60, "Ad costs since your last bill.") | DM D05S58U4SAK Sep 26 14:35 "I turned off the FB campaign" | −6 rows; T12 kept; fact `Sep 30 Meta charge` 57.85 → 25.60 |
| Meta Sep 16 receipt covers Sep 15 – 16 | DM Sep 15 18:47 "FB spend has been modest out of the gate"; Sep 16 07:43 "FB reports $80 of spend" | text only |
| T23 decoy receipt moved to Jul 18 – 24 (was Aug 8 – 14) | Aug 5 pause | text and dates only |

Balance cross-checks after the rebuild:
- HG spend Oct 2024 – Apr 2025 is now below the $13,000 of base top-ups (Oct 9, Oct 25, Nov 13, Nov 22, Dec 24, Apr 7). The old schedule exceeded them.
- Calm Play Jul 14 – 17 spend is $223.36, against "$333" → "$100 left" (Jul 14 / Jul 17).

**Ground truth now:**
- Real UA **$95,612.56**, Fundraising **$3,376.20**, all $98,988.76.
- Gap list unchanged (17).
- T23 receipts excluded.

Checks: `sql_lint` 0 errors (6 weekend warnings on automated receipts); `base_check` PASS (225 inserts); `fact_check --no-leak` PASS; `hardness_gate` (long) PASS; check-sql PASS (172 load-bearing ids); `stage_gate injection` PASS.

Residual risks, named:
- **Unconfirmed retention runs:** the base data does not confirm whether the Unity DD Android retention campaign ran Jan – Mar 2025 (Dec 31 "You okay with pausing Unity retention campaign?" has no visible answer). The model keeps it at low budget.
- **Base metadata:** the FINANCE_LEDGER table comment still caps Cross-Service Coherence at 3.

## 12 · Self-review

Walked: `Evals/1A_Hardness_Eval.md` §3 (attribution and confounds), §4 (source and access conflicts) and §5 (bands), against the register and the band.

| Verdict | Counter-reading | Resolution (evidence) |
|---|---|---|
| T4 LEAKED | Counter: the duplicate trap was never live, because the extraction script deduped mechanically | It was live. The extraction listed the repeated references ('dup refs: [TAX_ID_4752] 2, [USERNAME_5810] 2, [TAX_ID_6901] 2, M4RKD8XFY2 2', run-1 · event 422), and the dedupe was the doc's rule (event 16) applied at event 434. LEAKED stands |
| T5 LEAKED | Counter: $224.59 was never checked as a near-duplicate | The row is in the CSV (run-1 · event 415) beside $273.26 from the same thread. Kept on purpose. LEAKED |
| T6 LEAKED | Counter: the amendment was found only by luck | The search "adjoe invoice" (run-1 · event 239) is the natural query once the doc names Adjoe. LEAKED |
| T7 LEAKED | Counter: Sep 18 vs Sep 19 makes no difference, so the trap was never live | The comment date (Sep 22) was a live wrong reading. The run chose the review date via GCal (run-1 · event 159). LEAKED |
| T8 LEAKED | Counter: Snowflake was not used, so it was never met | It was met first in the hub and queried (run-1 · event 68). LEAKED |
| T9 LEAKED | Counter: the statements are the only Unity source, so there was no choice | Snowflake shows $0 Unity cost (snowflake.json /tables/0, re-verified through `hg.py search search snowflake "AD_SPEND_DAILY"`). The trap was live and passed at run-1 · events 95–147. LEAKED |
| T11 LEAKED | Counter: the briefs say the game outright, so there's no alias left | True; it is reading comprehension. It stays LEAKED and adds nothing for Opus (§8) |
| T12 LEAKED | Counter: the cut-off is 00:00 UTC, which would drop the 4:40 PM PT charge | The doc's "charge date in Pacific time" governs. Included at run-1 · event 308. LEAKED |
| T13 LEAKED | Counter: Robert is a co-founder | His reply carries no rule (C07C2866011/1759178460.557708, read at run-1 · event 7). LEAKED |
| T14 LEAKED | Counter: the Confluence decoy page was never returned | Card 41 (the same decoy) was returned and rejected (run-1 · event 31). LEAKED, not BYPASSED |
| T15 LEAKED | Counter: no run would create a card | The design said so too. Leaked at run-1 · event 508 |
| T16 LEAKED | Counter: the Q3 pack was never opened | Returned in the Drive search (run-1 · event 241). The run used the Q4 header (event 48). LEAKED |
| T19 LEAKED | Counter: no evidence the split was by day | The phone and tablet figures 1,630.75 and 1,099.85 at run-1 · event 341 equal the per-day split (dossier §9.2). LEAKED |
| T20 LEAKED | Counter: the top-up forward was only skimmed | It was read (run-1 · event 230) and the doc's "a top-up is not spend" applied (event 510). LEAKED |
| R1 CONFOUNDED | Counter: Opus should have inferred that 907669287942378 is the company account | The incorporated wording named "3125". No company receipt the agent saw showed 3125 (run-1 · event 391), and a literal reading was defensible. 1A §3 counts a reasonable reading of conflicting sources as no proven error. Re-verified through `hg.py`: the raw Subject header of frederick@harmonygames.co_1812262106647207041.json /messages/0/headers/18 reads "Account ID: 907669287942378" |
| W1 CONFOUNDED | Counter: the agent could have asked for access first | The write is the prompt's central deliverable and the persona's role made it impossible (run-1 · event 358). It is excluded as UNSUPPORTED (1A output capability) |
| T23 NOT-REACHED | Counter: the decoy creates a second end state (a literal reader might keep ZM_UK on any account) | The doc excludes the test account outright, and Meta means the company account. The Jul 2 notice names the account 'Leonard Hayes' (personal). The receipts bill Visa 7731, not the company MasterCard, and no brief lists their campaigns. One end state |
| Band (run-1, 1–2) | Counter: argue band 3, since the Real UA headline is 24% low in three writes | That miss has one root cause, D1, which is confounded, so it is not counted. A cascade is one cause, not three. With it removed, nothing material remains. Neighbouring band 3 is rejected |
| Band (hardened, 1–2 likely) | Counter: argue band 3–4, since T23 hits the Fundraising headline in the sheet, the reply and the card | It hits only if T23 lands, and run-1 grouped receipts by account (event 434). Band 3 is possible, band 4 needs more than one root cause. Kept at 1–2 likely and 3 possible |

Re-verified records (through `hg.py search`): 907669287942378 in the base receipt header (above); "ad account for Domino Adventure (ID: 1096548511793203)" in gmail frederick@harmonygames.co_1809398442244933472.json /messages/0/body; the Slack adsmanager link act=907669287942378 in C07C2866011 2024-10.json /1653/text. Mechanical checks after the SQL change: `sql_lint` 0 errors, `base_check` PASS, `hardness_gate` (long) PASS, `fact_check --no-leak` PASS, `stage_gate injection` PASS.

Unresolved: whether T23 lands on Opus is unknown until the next run. Only one live lever remains for Opus, so a further redesign may be needed if the next `/hardness` still returns 1–2. The seven BYPASSED and 14 LEAKED traps are recorded in §9 and §4.

```
STAGE GATE hardening: PASS — Task_Authoring-2/task_inputs · 01a_Hardening_Report.md#6837f971491a · 01_Universe_Inject.sql#f941928e986a · 01_Hardness_Manifest.json#6e05b57736fd · blocking 0 · warnings 0 · checks 14
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#f941928e986a, 01_Hardness_Manifest.json#6e05b57736fd, 01_Grounding_Dossier.md#e7a27d7d590e)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 25/25 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 19 evidenced counter-readings (of 19 found; need ≥ 17) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```


## 13 · Next steps

1. On the platform, run `/injection` on the hardened SQL (revision 2, sha256 f941928e986a), then `/prompt`. The prompt is unchanged, but the doc wording changed, so the account fork F16 must be rechecked.
2. Re-apply the SQL in the runner and run one fresh unhinted Opus pre-check, then `/hardness`.
3. If `/hardness` returns 1–2 again, run `/create-hardening` on that run. The next lever has to be a new independent chain, not more rules stated in the doc.
4. The human-time worksheet: no volume change is needed beyond the +5 decoy receipts. Refresh it after Oracle Events exist.

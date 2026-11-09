# 01a Hardening Report: leonard_stockholder_closeout, platform pre-check intake (run on platform SQL bc72db9c)

## 1. Mode, inputs and run validity

**MODE B (pre-check).** One platform Opus 5.5 run, attempt 6aed9d01a1cb8067d8ac7dee. The platform `/hardness` scored it 2
(FAIL, HOLD, INSUFFICIENT_DIFFICULTY, "Easy"). No baseline exists.

Assignment: Leonard Hayes, Co-founder & Creative Director · Executive · Finance · Authoring · Long Horizon · medium (cap
< 85 %, requester target < 70 %, 130+ calls) · Feb 14, 2026, normal universe. Universe manifest
`Evals/references/universes/normal/universe_manifest.json`; `Working_Files/00_Task_Context.json` context_hash 1280066650a1.
The /hardness report's clock line: `Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)`.

**Inputs read**
- `00_Assigments.md`, `01_Grounding_Dossier.md`, `01_Hardness_Manifest.json`, `01_Gradable_Surface.json`, `solver/truth.json`,
  `solver/solver.py`, `03_Error_Async_Config.txt` (Friction: none).
- `01_Universe_Inject.sql`: local rev1, sha256 fd51afbf63aa (101,094 B), stored as `run_forensics/rev1/`. **This is not
  the SQL the run used.**
- `04_Prompt.txt`: sha256 45766344a3e4 (711 B). The platform prompt 424c70d34fdf (712 B) is the same text plus a trailing
  newline (checked by hashing both forms).
- `06_PreCheck_Trajectory/trajectory-run-1.json`, copied byte-for-byte to `trajectory.json`: sha256 f059ce8331b7, the
  file the /hardness report reviewed.
- `plateform_reports/6aed9d01a1cb8067d8ac7dee_1a_hardness.md` (/hardness), `_0_injection.md` and `_1_prompt.md` (both PASS on
  bc72db9c).

**Inputs missing** (expected before a baseline): `07_Baseline_Trajectories/` (README only), `10_Baseline_Verifier_Results.md`
(empty), `12_Difficulty_Stats.txt`; `08_Oracle_Events.md` and `09_Rubrics.json` are templates.

**Revision binding: the gap.** The run executed on the platform input-store SQL **bc72db9c31e9…** (74,125 B), which is not
stored locally. The nearest local copy is the first input of the local /prompt round,
`run_forensics/rev1p/01_Universe_Inject.sql` (6f3b18994e1a, 74,274 B). No header-strip or trailing-newline variant of it
hashes to bc72db9c (brute force over every subset of the first six lines and three line-ending forms), and the forensics
read found it differs from what the run saw in two notes-doc phrases ("once the sheet is right", "only go in the
totals"). `trajectory_ledger` reads the binding as **AMBIGUOUS** (`run_forensics/rev1p/precheck/summary.json`): rev1p shows 4
of 6 discriminating text windows, and rev1 (fd51afbf63aa) shows 2 of 26. Both rev1 hits are the two owner-list UPDATE rows,
whose bodies are the base text minus one sentence, so they match base text the run read and are not evidence that it ran
on rev1. **The pre-check export `precheck` is therefore historical: bound by the platform hash bc72db9c (the run's own
/hardness and /injection reports), never by a stored revision; it certifies no revision.** `node_verdicts` refused it
("NOT EVALUATED – binding AMBIGUOUS"), so every verdict below is by hand from a full read.

**Run validity (B0)** from `trajectory_ledger.py`:
- Harness claude-code 2.1.280, cwd /app, session 6ae2a995; init model claude-opus-5-5[1m]. Every message comes from
  claude-opus-5-5: no fallback, no subagent (0 briefs), mixed_model false, v3_valid VALID.
- Completed: 957 events, result at 956 (success, 239 turns, $19.17, 22.5 min). One auto-compaction at event 834 (its summary
  quotes the user message word for word); nothing after the result.
- Calls: 237 raw, 26 harness (Bash), 2 blocked, 0 repeats → **209 counted**.

**The intake's six results**
1. Binding: AMBIGUOUS by the tool → historical, bound by the platform hash bc72db9c (above).
2. Mixed model: none.
3. Proposals: none (node_verdicts refused); 7 mechanism verdicts and 21 trap verdicts by hand
   (`research/rev2/forensics_nodes.md`, every one of the 237 calls read).
4. Deliverable diff: `surface_grader` 27.8 % (decoder artifact: it overlays the three sheet tabs); hand diff **79.5 %**
   (186/234), one root cause (`research/rev2/surface_handdiff.md`).
5. Ledger: 7 verdict records appended (`run_forensics/rev1p/precheck.dispositioned.jsonl`): `hev_2c7d80f9afd78ff0` ADV,
   `hev_dcd66cefd992f553` LETTER, `hev_c4c5bad2a50acca6` TOLD, `hev_b4772a0e7f69754f` ASOF, `hev_5deeab873eba21ce` FAM,
   `hev_d21262720f5bb54d` BOARD, `hev_5398649b22d310ba` ASK; each carries `sql_sha256` bc72db9c and the binding note.
6. Posterior forecast `hev_5a4b392d664feb03` (pre-registered, UNCALIBRATED): V3 E[avg] 0.913–0.965, P(all gates)
   0.000–0.002. The solver view never fails write-content slots, so it reads high, but the run itself scored 79.5 % by hand.
   **Call: NO-GO** (section 13).

## 2. Gate status and clean average

No baseline, so nothing comes from `12_Difficulty_Stats.txt`. The pre-check is a design check only.

| View | Score | Basis |
|---|---|---|
| `/hardness` reviewer (platform) | 2 (Easy), failed share ≈ 3 % | its 14-requirement map; ADV left "unassessed" because it found no grant sizes |
| `surface_grader` raw | 27.8 % | decoder overlays the Holders, Summary and KPMG tabs on one grid |
| surface by hand | **79.5 % (186/234)**, 84 of 96 slots met | every slot checked against the write payloads (opus · event 771, 783, 785, 818–852, 944, 950) |
| surface, clean | 79.5 % | no slot confounded (section 4) |

The 12 failed slots (K1, K4–K8, P1, A1, B2, AL_vol, NC_Collins, NC_Deepak; 48 weight) are one cause: ADV. Mechanism weight
share of LANDED nodes: 48/234 = 20.5 %. Against the medium cap (85 %), one run at 79.5 % would pass the average gate, but
the requester's 70 % target needs about 10 more points of genuine loss per run.

## 3. Predicted /hardness band

Requirement map (the platform's R1–R14, re-judged): R1 holder sheet **MATERIAL_FAIL** (four advisor-angel rows book option
grants as Series Seed; Series Seed 3,155,643 not 3,051,879); R13 KPMG **MATERIAL_FAIL** on items 1 and 2 (3,155,643 Series
Seed; options 139,993 without the 103,764 advisor lines; item 3's 9,295,636 is right only because the errors offset); R7
notes **MINOR_GAP** (Collins's and Deepak's notes state the merged figure "according to Carta"); every other requirement MET
as the platform found.

- Grouped by root cause: one material cause (ADV), fair (section 7). No CONFOUNDED failure.
- **Predicted band: 3** (one consequential failure with a bounded correction) if the reviewer finds the advisor table;
  **2** if, as on the platform, it cannot find the grant sizes and leaves ADV unassessed. Not 4: no second independent
  material cause exists; every other rule was met on its first read or in a bulk pull.

## 4. Designed-difficulty register

Verdicts by hand (node_verdicts refused the historical binding). One run: counts are provisional, out of 1 completed run.

| Mechanism | Verdict | Counts (L · C · Lk · B · NR) | Deciding record came back | Decision written | v2 kind |
|---|---|---|---|---|---|
| ADV (A17) | LANDED | 1·0·0·0·0 | sizes mail "Re: Follow up items" (thread 1773160163779741845) as an id at opus · event 496, metadata only at opus · event 502; the 3,051,881 seed total at opus · event 562, explained away at opus · event 835 | owner-list totals as stock at opus · event 771, 783, 785, 944, 950 | — (fair miss) |
| LETTER (A24) | LEAKED | 0·0·1·0·0 | "All termination letters are sent" at opus · event 35; six letters by one sent-mail window (opus · event 381) and one batch (opus · event 394); Carta entries in the 78-message pull (opus · event 221–237) | Vincent and Oliver "Closing and last day" at opus · event 771 | bulk |
| TOLD (A25) | LEAKED | 0·0·1·0·0 | SEMC Feb 9 DM at opus · event 523 (pointer from the after:2026-02-08 Slack search, opus · event 414); Robert's Feb 12 reply at opus · event 314 (id in the after:2026/02/08 listing, opus · event 295) | ENG-2440/2446 Already told at opus · event 771 | bulk |
| ASOF (A19) | LEAKED | 0·0·1·0·0 | FY25 request and its clarification in one KPMG thread at opus · event 61; effective dates at opus · event 250 | KPMG lines at opus · event 944, 950 | same_container / first_read |
| FAM (A7) | LEAKED | 0·0·1·0·0 | family rule in the #winddown list thread at opus · event 28; Enes's Jun 30 2023 mail at opus · event 540 | ENG-2444/2445 Covered at opus · event 771; one note at opus · event 846 | first_read |
| BOARD (A11) | BYPASSED | 0·0·0·1·0 | resignation mail only as ids (opus · event 59, 609); board read off Carta consent recipient lists at opus · event 250 | "Leonard Hayes, Robert" at opus · event 783 | off the true path |
| ASK (A9) | LEAKED | 0·0·1·0·0 | Claire's question and the partial reply at opus · event 419 (print of the spilled DM search, opus · event 416) | Claire's draft answers it at opus · event 818 | bulk / same_container |

Chains: C1 lands at hop 2 (the advisor table never read); C2, C3, C4 (rule), C7, C8 leak; C5 bypassed.

## 5. Per-rollout ledgers

`run_forensics/rev1p/precheck/precheck/calls.jsonl` (237 calls, event and result_event for each), `writes.json` (decoded
writes), `briefs.json` (none). The search-term table, the container-read table and the trap-level verdicts are in
`research/rev2/forensics_nodes.md` §1–§8; the slot-by-slot diff is `research/rev2/surface_handdiff.md`. Calls not reviewed:
none (all 237 were read, input and result; two spilled results were seen only as previews: opus · event 85, the label list,
and opus · event 563, the "shares" Slack search).

Path summary: anchors first (notes doc opus · event 11, #winddown opus · event 13, the 26 issues opus · event 14 and their
52 comments), then bulk pulls: every Carta notice (opus · event 124–237), Leonard's mail after Feb 8 (opus · event 294, 381),
Slack after Feb 8 in channels and DMs (opus · event 413, 416), name-token ORs (opus · event 494, 524); writes from
opus · event 767.

## 6. Friction, tool defects and horizon

- Friction: none configured; none observed.
- Tool defects: the 10-id cap on `gmail_get_messages_batch format=full` (opus · event 216) was recovered at opus · event 221;
  an ECONNRESET on `gmail_get_thread` (opus · event 940) was recovered at opus · event 942. `gmail_reply_to_message
  reply_all` dropped the cc's on the KPMG thread (opus · event 944) but not on Griffin's; the run re-sent to all four
  (opus · event 950). None changed an outcome.
- Horizon: 209 counted calls (long-horizon minimum 100; requester 130+). Met without padding.

## 7. Verifier sanity

No verifier exists. The /hardness reviewer's "unassessed scope" is an evaluator miss, not a task defect: the grant sizes are
in two persona-visible bodies, re-verified through `tools/hg.py`:
- gdocs `/docs_documents/262` "Due Diligence Disclosures" (owner leonard.hayes): "Total | | 1.7% | 103,764 shares".
- Gmail thread 1773160163779741845 ("RE: Follow up items"): "Matthew Collins / Board member / 1% / 61,038 shares", with
  30,518 / 6,104 / 6,104 under the Linear title names.
- gdocs `/docs_documents/40` (term sheet): "Series Seed Preferred (all non-founder investors): 3,051,879". Ties:
  3,155,643 − 103,764 = 3,051,879.
The Nov 2023 board-consent PDFs (thread 1782034095239486005) return no bytes to the agent, so they are not a fair path; the
design never relies on them. Residual fairness note for the rubric: no persona-visible record gives the advisor grants'
vesting terms, so "options now" for the advisor lines must grade the outstanding grant (Carta shows no termination), never a
vested-only figure.

## 8. Why Opus passed

`hardness_v2_check.py --task-dir Task_Authoring/task_inputs` (fd51afbf63aa; the platform-era SQL has the same traps):
CLEAN on SAME_PLACE (5 traps with versions), DONE_CHECK, TWO_DECISIONS (7 rules), DECISION_FLIP (7/7), INPUT_CHECK,
FILTER_CHECK and RULE_IN_PROMPT. The checks were clean and the run still met six of seven rules, because the v2 failure is
in how the run reads, which the static check cannot see:
- **Bulk calls carried the answers.** One sent-mail date window plus one batch returned every termination letter (LETTER);
  date-window Slack and Gmail searches after Feb 8 returned the Segerstråle DM, Robert's reply and Claire's question
  (TOLD, ASK); the full Carta pull returned every effective date and the consent recipient lists (ASOF, BOARD).
- **First-read containers.** The KPMG clarification sits in the KPMG thread the prompt names (ASOF); the family rule is a
  reply in the #winddown thread every run opens (FAM); the superseding notes doc says so in its first line (T18).
- **Decoys never on the path.** T3, T8, T15, T16, T21, T22 came back only as ids or never; the default answer was right.
- **Rules spelled out.** The notes doc and the project state every rule, label and state mapping; the hardness reviewer's
  own advice is to move deciding facts out of plain view.

Heavy rows (weight 5) that passed: C_ES14, C_ES18, C_SEG, C_NEB, B1, F1, N_Vincent, Q1, and A2 (only through offsetting
errors). These are told/not-told and family calls whose deciding record sits on a bulk path; the rebuilds below add none
of them.

## 9. Purge list (proposed; S0r decides)

- BOARD (BYPASSED): keep as a gradable fact (B1, weight 5), but it is not a difficulty; drop it from the hardness claims.
  Robert's reply-all that states the board stays (the leak audit found the run reached the board without it).
- T3, T8, T15, T16, T21, T22: decoys never on the path; no SQL change (they cost nothing and settle forks), but they count
  for nothing in the forecast or the trap tally.

## 10. Proposed rebuilds (each a Hardness v2 move; no added holders, rows or volume)

Census reports: `research/rev2/census_a_bounce.md`, `census_b_carta.md`, `census_c_alias.md`, `census_d_adv.md`.
1. **A done source with a missing piece (Part 3.1):** Owen Baker's Feb 11 letter (ES-12, ENG-2457) bounced. A Gmail
   delivery-failure notice in that letter's thread (where base Gmail puts every bounce) makes Owen untold, so he moves from
   Last day to Closing and last day. The run read the letters by message id (opus · event 394) and never opened their
   threads. Estimated miss rate about 50 %.
2. **A correction somewhere else (Part 3.2):** Calvin Price (ES-3, ENG-2452) forwards Carta's own holder notice (Jan 23)
   that moved his last day from Jan 24 to Feb 20, in his own thread from his issue address. Under "Carta is the record" his
   line is live, he gets a note, and he goes first (before Vincent's Feb 21). The run fetched only Carta-generated
   message ids from its "carta" results (opus · event 207–237), and its date windows started at Feb 8. Estimated miss rate
   55–60 %.
3. **An alias (Part 3.6):** a Feb 10 mail from Leonard to "Akin" at a personal address tells Collins about the closing;
   only old mail ("best / akin") ties Akin to Matthew Collins. The run never searched "Akin" and called Contacts
   "heavily anonymized" (opus · event 374). Estimated miss rate about 30 %. Conditional on the cold attack review.
4. **Un-point ADV:** remove the two sentences the local /prompt round added that state the split (Leonard's Jan 14
   #executives note "the owner list counts the advisor options in with the stock" with its figures; KPMG's item-1
   sentence giving 3,051,879), leaving the advisor table and the ledger as the deciding records, with a numberless
   "go by the ledger" reply under the ChatGPT post as the only bridge. Estimated miss rate 50–65 %.

## 11. Routing (proposed; S0r decides)

- **Universe changes** (to `/create-scenario --revise` S5a, then `/create-injection` rev2): items 1–4 above. Facts they would
  change: ENG-2457 Told/Owed; ENG-2452 live (4,408, last day Feb 20, Todo, a note); first to go Calvin; options now
  164,114; ENG-2447 Already told (conditional); notes, Last day and Closing-and-last-day counts; KPMG unchanged
  (243,757; 9,295,636); Series Seed 3,051,879 unchanged.
- **Prompt-side defects:** none. The prompt names only the three anchors and no rule; keep it byte-identical.
- **OE / rubric observations** (for `/create-oe-writing check` and `/create-rubric-writing check` later): grade advisor
  "options now" as the outstanding grant; do not grade Owen's draft To address (his issue email bounced); grade per holder,
  not per ES id, for ES-8/ES-10; A2 is invariant under ADV (tag it ASOF only).

## 12. Self-review

| # | Verdict or claim | Counter-reading | Resolution (evidence) |
|---|---|---|---|
| 1 | ADV LANDED | Tool: maybe no ordinary call could return the sizes. | Two bodies hold them (re-verified via `tools/hg.py search gdocs "103,764"` → /docs_documents/262; `search gmail "61,038"` → thread 1773160163779741845); the run held that thread's id at opus · event 496 and fetched it metadata-only at opus · event 502. Genuine retrieval failure. |
| 2 | ADV LANDED | Fairness: the split may not be incorporated. | "Carta is the record" (notes doc) plus Carta's digest naming ES-9/ES-11 (read at opus · event 245) make the advisor lines Carta lines; the ledger's 3,051,879 (re-verified, /docs_documents/40) ties only after subtracting 103,764. Incorporated and unique. |
| 3 | ADV LANDED | Run: compaction at opus · event 834 may have dropped the evidence. | The write-off "3,051,881 was the initial close only" sits in the compaction summary (opus · event 835) and the post-compaction KPMG reply repeats 3,155,643 (opus · event 944); the decision predates the compaction. |
| 4 | LETTER LEAKED | The trap may never have been live (C0ADGSZKR3R/1770841239.761999 is the done claim). | The done claim (opus · event 35) and all six letters (opus · event 394) and all eight Carta entries came back; the join was made, so it was live and leaked through bulk calls. |
| 5 | TOLD LEAKED | Was the completion (D04UC0UEN2V/1770664988.379119) met before the claim? | The Feb 12 list came first (opus · event 13); the Feb 9 DM came later (opus · event 523) from a date-window search, so the order held and the bulk search carried it. |
| 6 | ASOF LEAKED | Verbatim supersession where the agent reads first (thread leonard.hayes@harmonygames.co/1857029474983245439)? | Yes: the clarification is in the KPMG thread the prompt names (opus · event 61): same_container / first_read. Leaked, not FALSE, because the rule still had to be applied to 14 lines (all right at opus · event 944). |
| 7 | FAM LEAKED | Verbatim on the delegation path (C0ADGSZKR3R/1770949310.220519)? | The rule is a reply in the #winddown thread the notes delegate to (opus · event 28): first_read; the link needed one targeted search (opus · event 540). |
| 8 | ASK LEAKED | Did a bulk call carry it (C51ECE5102ED/1770903714.600249)? | Yes: the DM date-window search (opus · event 416, printed at opus · event 419) returned the question with the told record. |
| 9 | BOARD BYPASSED | It may count as LEAKED (resolver leonard.hayes@harmonygames.co/1830959847543474636). | The designed resolver was never opened (ids only, opus · event 59, 609); the answer came from Carta consent recipient lists (opus · event 250), a path the design did not build. BYPASSED stands. |
| 10 | Band 3 (or 2) | Neighbouring band 4: the KPMG reply and the sheet are both wrong (forensics_nodes.md §1). | Both errors are one cascade from one root cause (1A §3); no second independent material cause. Neighbouring band 2 applies only if the reviewer cannot find the sizes, as happened. |
| 11 | Hand score 79.5 % | The decoder's 27.8 % (precheck.surface_grades.json) may be right on some slots. | Every slot it failed was checked against the write payloads (surface_handdiff.md); 57 of its failures are met; no slot it passed fails by hand. |
| 12 | Binding historical | The run might be bindable to rev1p (summary.json binding AMBIGUOUS). | rev1p differs from what the run saw in two notes-doc phrases, and no rev1p variant hashes to bc72db9c; marking `precheck` historical is the only honest binding. |

Re-verified records through `tools/hg.py`: gdocs /docs_documents/262 and /docs_documents/40; Gmail thread 1773160163779741845
(`threads/00001361.json /messages/0/body`); base delivery-failure threading (census_a §2: Robert 1769337688765186323,
Leonard 1810030685221873164).

Unresolved: the exact bc72db9c bytes (not stored); the advisor grants' vesting terms (no persona-visible record).

```
STAGE GATE hardening: PASS — Task_Authoring/task_inputs · 01a_Hardening_Report.md#670f1dc013d5 · 01_Universe_Inject.sql#fd51afbf63aa · 01_Hardness_Manifest.json#02c893f5a3c3 · 00_Assigments.md#c790db463281 · 01_Grounding_Dossier.md#8a5ebfea5f53 · 06_PreCheck_Trajectory#1c54fc1cffe1 · 07_Baseline_Trajectories#ad7848c1ad99 · 10_Baseline_Verifier_Results.md#e3b0c44298fc · __context__#1280066650a1 · __assignment__#49d5e1d57a30 · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#b745609eff39 · blocking 0 · warnings 0 · checks 17
[PASS] assignment.v3_context: Leonard Hayes / Co-founder & Creative Director; medium cap <85%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#fd51afbf63aa, 01_Hardness_Manifest.json#02c893f5a3c3, 01_Grounding_Dossier.md#8a5ebfea5f53, solver/solver.py#d5d3e4148cb5, 01c_Dispositions.json#52fd7f0c1ba3, 01c_Preflight_Report.json#d4c27b76ceb5, 00_Assigments.md#c790db463281, 01_Scenario_Design.md#df5467ee8455, 01_Hardness_Manifest.draft.json#651273eb6fb4, 01_Gradable_Surface.json#e3278465b792, __context__#1280066650a1, __assignment__#49d5e1d57a30, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#b745609eff39)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 7/7 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 10 evidenced counter-readings (of 12 found; need ≥ 7) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13. Next steps

- Call: **NO-GO** for the six-run baseline (/hardness 2; one landed mechanism; posterior P(all gates) ≈ 0).
- `/create-scenario --revise` (S0r): disposition the verdicts above and take rebuilds 1–4 from S5a; then `/create-injection`
  as rev2 (store `run_forensics/rev2/`), the blind fork sweep and delta reviews, then `/create-prompt-writing check` (prompt
  unchanged) and a local blind /prompt round.
- Then the platform `/injection` and `/prompt` on the rev2 SQL, a new unhinted Opus pre-check, and `/hardness`.

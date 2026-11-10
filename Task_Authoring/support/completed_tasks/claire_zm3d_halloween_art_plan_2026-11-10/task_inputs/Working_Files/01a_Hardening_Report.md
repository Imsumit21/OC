# 01a Hardening Report — ZM3D Halloween art plan (Claire Morgan) · rev2 pre-check

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe manifest: `Evals/references/universes/synthcut/universe_manifest.json`.

## 1 Mode, inputs and run validity

**MODE B (pre-check).** One platform Opus 5.5 run, taken in against the rev2 solver. No baseline exists yet: `07_Baseline_Trajectories/` holds no runs and `10_Baseline_Verifier_Results.md` and `12_Difficulty_Stats.txt` are empty, so section 2 records no gate statistics.

Inputs read:
- `06_PreCheck_Trajectory/trajectory-run-1.json` (sha256 `8ef0af2a473dc10fae7cf26de86deb1e896dd845d7631ddb6a134272c896fea9`, 575 events), copied byte for byte to the slot name `06_PreCheck_Trajectory/trajectory.json`. Every tool call and result was read.
- `plateform_reports/6aea4c1eea32a6fa98b9b1d9_1a_hardness.md` (`/hardness` FAIL, score 2, HOLD, `Clock:` 2025-10-01 00:00 PT (2025-10-01 07:00 UTC)), `..._0_injection-1.md` (PASS) and `..._1_prompt-1.md` (PASS 5).
- `04_Prompt.txt`, `01_Universe_Inject.sql`, `Working_Files/01_Hardness_Manifest.json`, `01_Scenario_Design.md`, `01_Grounding_Dossier.md`, `01_Gradable_Surface.json`, `solver/solver.py`, `solver/truth.json`, `03_Error_Async_Config.txt`.
- The base universe through `tools/hg.py` and two read-only reconnaissance passes (section 10 cites the records they found).

Inputs missing: `07_Baseline_Trajectories/` runs, `10_Baseline_Verifier_Results.md`, `12_Difficulty_Stats.txt`, `08_Oracle_Events.md`, `09_Rubrics.json` (none are due at a pre-check).

The six intake results:

| Intake result | Value |
|---|---|
| Binding | `BOUND:rev2` on discriminating content (`trajectory_ledger.py`; the `--sql` set is rev2 and rev1). The platform SQL `d8cb3dd4…eed8c` is rev2 (`28b0cdad…e4d4`) minus its first seven comment lines (`tail -n +8` reproduces the hash), so every statement the run saw is rev2's |
| Model flags | `mixed=False`, `v3_valid=True`, `valid_for_claude-opus-5-5=VALID`; every message `claude-opus-5-5` (init `claude-opus-5-5[1m]`), no fallback, no subagent, no compaction, nothing after the result event (574) |
| Proposals and dispositions | 6 rule verdicts, all LEAKED, all confirmed by hand; R_PACK_ALIAS is SURFACE-ONLY and is dispositioned FALSE in section 9. Review coverage: all 233 calls read, `review_queue` events 287, 294 and 296 reviewed, 0 unclassified, 0 not reviewed. CONFOUNDED: none |
| Deliverable diff | Hand diff of the tracker tabs against `solver/truth.json`: 58 of 58 ad calls match, 4 of 4 store calls match, 0 archive rows included. Only spelling differences: `julia 4:5 (They're coming, stop them!)` for `julia 4:5`, and `-` for the two Reuse owners. `surface_grader.py` reads 6.8% (10.2% on the normalised copy); section 7 shows that number is a decoder artifact and it is not used |
| Ledger | `hev_d0b07f60c129c96b` R_BUILD_CUT, `hev_852b065152ade635` R_DONE_EXPORT, `hev_5607371363107ea5` R_ALREADY_MADE, `hev_fe1047effcd69fe4` R_FLIGHT_CHANGE, `hev_6b01d1489ea05d94` R_SCOPE_SERVING, `hev_cdb4202aec019c58` R_ART_CURRENT (`run_forensics/rev2/precheck.dispositioned.jsonl`). The ledger file is gitignored and absent from this machine before this run, so these are its first records and every other prior is Beta(1,1) |
| Posterior forecast | `hev_383f40b9839a2bf4`, pre-registered, UNCALIBRATED: P(all four gates) 0.000–0.531 across scenarios, whole-policy E[avg] 0.757 and 0.902–0.973 for the partial-policy scenarios. It predates any rev3 change and it is built on six records; read it as a floor on uncertainty, not a rate |

**Go / no-go: NO-GO (UNCALIBRATED).** The go rule needs `/hardness` ≥ 3, a corrected proxy at most cap − 5, at least two independent loss channels and a valid run. `/hardness` is 2, the proxy is about 97% (the platform's failed share is about 3%), `go_rule.independent_channels` is 0, and only the run-valid condition holds. Spending the six-run baseline on rev2 is not justified; next is `/create-scenario --revise`.

## 2 Gate status

Not applicable: a pre-check produces no `12_Difficulty_Stats.txt`. For reference only, the assigned mode is Medium (strictly below 85%), and the session goal designs to E[avg] ≤ 62% with at least four independent loss channels.

## 3 Predicted /hardness band

The platform has already scored this run, so B3c was done blind and then compared. Requirement map, from the prompt and the incorporated sources:

| Requirement | Outcome | Evidence |
|---|---|---|
| Call for all 58 ads | MET | opus · event 287 |
| ART-831 and ART-826 included | MET | opus · event 54, event 43 |
| ART-809 music, ART-840 capture date | MET | opus · event 207, event 287 |
| ART-808 / ART-816 Reuse | MET | opus · event 217, event 287 |
| Sep 30 changes applied (8 Skips, Oct 15) | MET | opus · event 27, event 287 |
| Makers: 6 Martin, 42 Marcus | MET | opus · event 465 onward (48 `linear_update_issue`) |
| Store calls and 2 new tickets | MET | opus · event 272, event 274, event 294 |
| Store ticket due dates | MINOR_GAP: Oct 15 with the Oct 16 cut stated | opus · event 272 |
| Interim date | MINOR_GAP: an unsourced "Refresh by Wed Oct 8" on 34 rows | opus · event 287 |
| 58 comments, doc, tracker, shares, reply | MET | opus · event 299, event 568 |

Failures grouped by root cause: 0 material, 3 minor. Predicted band **2 (HOLD)**, which matches the platform's score 2. Not 1: the store-ticket date is a real, if small, deviation from Arthur's calendar. Not 3: nothing needs a consequential correction, so no call, inclusion, maker, write or destination is wrong.

## 4 Designed-difficulty register

Counts per node, out of the one completed run: LANDED 0 · CONFOUNDED 0 · BYPASSED 0 · NOT-REACHED 0 · 6 LEAKED · 1 FALSE.

| Rule (nodes) | Verdict | Why, with the step |
|---|---|---|
| R_DONE_EXPORT (T1, CH1) | LEAKED | opus · event 225 read Martin's thread, opus · event 231 listed the Store folder in one call; the iPad gap was then plain, ticket written at opus · event 272 |
| R_ALREADY_MADE (T3, CH4, T19) | LEAKED | opus · event 217: one `halloween` Slack search returned Claire's DM root and Marcus's thread reply together; ART-851 kept apart at opus · event 287 |
| R_FLIGHT_CHANGE (T4, CH3, T18) | LEAKED | opus · event 17: one Gmail search returned both mails, read at opus · event 27 and event 29, because Leonard's ask points straight at the plan |
| R_SCOPE_SERVING (T6, CH7, T5, T10, T14) | LEAKED | opus · event 54: ART-831 announces itself; opus · event 43: `trello_search` Halloween returned the ART-826 comment; opus · event 60: the ticket list gave the set difference |
| R_ART_CURRENT (T8, CH2, T9, T17, T11, T12) | LEAKED | opus · event 106 read the deck, 58 `linear_list_comments` calls brute-forced each ticket's capture note, opus · event 207 followed ART-809's pointer to the Aug 13 thread; re-captures sat on the same ticket as the capture they replace |
| R_BUILD_CUT (T2, CH6, T16, T13) | LEAKED | opus · event 25 read the calendar, opus · event 274 tied the icon to the build rather than Oct 24; the Oct 15 ticket date is the only deviation |
| R_PACK_ALIAS (T7, CH5) | FALSE | opus · event 227 read the quote and the plan at opus · event 299 turned the bundle down in one line without the Contacts or GitHub hops; no graded row depends on it, so it never coupled |

## 5 Per-rollout ledger (pre-check run)

Full ledger: `run_forensics/rev2/precheck/calls.jsonl`, `writes.json`, `ledger.json`. 233 calls, 225 counted, 0 subagents. By phase:

| Events | What it did | Came back | Stopped or skipped |
|---|---|---|---|
| 2–33 | Slack ask, Drive search for the sheet and calendar, Gmail `october UA plan`, Linear teams, calendar doc, both mails | Ask, sheet, calendar, draft and changes mail | Calendar window Oct 1–4 only (opus · event 19); the result spilled and was read by script at opus · event 50 |
| 33–60 | Sheet tabs, ART-793, Trello `Halloween`, ART-826, ART-831, ART ticket list since Sep 1 | Read me, 62 library tickets, Frederick's card comment | No base ticket older than Sep 1 |
| 62–99 | Review invite, then 58 `linear_list_comments` | Attendees, every capture, master and campaign note | Nothing outside the ticket comments |
| 100–111 | `from:Robert seasonal`, Drive and Confluence `seasonal`, deck, two Confluence pages | The deck rules | Never searched by creative name |
| 207–232 | Aug 13 thread, `halloween` in Linear, Drive, Slack and Gmail, Martin's thread, vendor mail, Halloween and Store folders | Marcus's reply, Martin's reply thread, Store folder listing | Never opened #zombie-art, #zm-animations, #zombie-match3d, #company-internal, #random, UA masters folder |
| 267–299 | Linear users, 2 new tickets, tracker tabs, plan doc | Writes | |
| 300–568 | 12 shares, 58 comments, 50 updates, thread reply | Writes | |

Where it relied on one source: every capture, master and campaign fact came from the ticket comments, as the sheet's Read me says. Where it committed to a framing: at event 277 it built the whole call table from those facts in one script, with no check against any other service.

## 6 Friction, tool-defect and horizon checks

- Async and forced errors: none configured (`03_Error_Async_Config.txt`, `Friction: none`).
- Unconfigured tool defects: none changed an outcome. `gcal_list_events` spilled at opus · event 19 and the run read the saved file; `jq` was absent at opus · event 45 and it switched to Python at opus · event 50.
- Horizon: 225 counted calls against the Long Horizon minimum of 100, and the 181 floor in `volume_exception`. No padding: 58 reads and 58 comments are per-ticket work.

## 7 Verifier sanity

No verifier exists yet. The local proxy is defective for this run and must not be read as a score:
- `surface_grader.py` printed 6.8% and `node_verdicts.py` proposed BYPASSED for all rules on the raw export. Cause 1: the decoder keys rows on the surface's `surface` header, while the run labelled that column `Creative` and so fell back to column 0 (ART ids). Cause 2: it overlays every tab of a spreadsheet on one grid, so the `Store` and `Key dates` writes (opus · event 294, event 296) replace the `Ads` header row (opus · event 287).
- `run_forensics/rev2/precheck/trajectory.header_normalized.json` is a derived copy with only the header labels, two key spellings and the tab layout normalised; the export is untouched. On it `node_verdicts.py` gives LEAKED for all six rules, which matches the hand diff. `surface_grader.py` stays at 10.2% on the copy; all 19 failed slots were checked against the write payload and each is met, so every one is a grader artifact (playbook step 3). Renaming the table deliverable from `tracker` did not change that (`Working_Files/scratch/sg_register.json`). Its cause was not found, and no result here depends on it.
- The shared tools are out of scope for this task (session goal), so the fix is routed, not made.

## 8 Why Opus passed

`hardness_v2_check.py` on the bound revision:

```text
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  FLAG       SAME_PLACE      4 trap(s) with two or more version records; 2 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 5 requirements: {'R4': ['R_BUILD_CUT'], 'R2': ['R_DONE_EXPORT', 'R_ART_CURRENT'], 'R7': ['R_ALREADY_MADE', 'R_PACK_ALIAS'], 'R5': ['R_FLIGHT_CHANGE'], 'R1': ['R_SCOPE_SERVING']}  [Part 5 rule 1]
  FLAG       DECISION_FLIP   5 of 7 rules can flip a weight-5 slot; not: ['R_BUILD_CUT', 'R_PACK_ALIAS']  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Each settled trap, by v2 failure kind, from the call ledger:

| Trap | v2 failure kind | Evidence |
|---|---|---|
| T1 done gap | a bulk call carried the answer: one folder listing shows the missing set | opus · event 231 |
| T3 already made | the deciding record contains the task's own keyword, so one search returned it | opus · event 217 |
| T4 flight change | `on_delegation_path`: the ask points at the plan and one search returned draft and correction | opus · event 17 |
| T6 off-sheet items | set difference over one ticket family, plus a self-announcing comment | opus · event 54, event 60 |
| T8 deck rule | volume brute-forced: the per-ticket facts sit where a 58-call sweep lands | opus · event 287 |
| T9 re-captures | `same_container`: the correction shares `linear:ART-795` with the capture it replaces | opus · event 287 |
| T2 icon date | a clear rule in a named source | opus · event 25 |

Heavy rows that passed (weight 5): S03, S05, S06, S08, S28, S10, S11, S14, S15, S16, S17. These are what Opus finds easy on this task, so no rebuild adds more of the same: ticket-comment facts, named-source rules, and anything whose record contains the word Halloween.

The common cause: every deciding fact sat on one of three swept paths. Those are the ticket comments (read for all 58), the sources Leonard names, and any record containing `halloween` or `seasonal`. The run never searched by creative name and never opened a channel it was not sent to.

## 9 Purge list (proposed; S0r decides)

| Node | Proposal | Evidence |
|---|---|---|
| R_PACK_ALIAS (T7, CH5) | Purge as a rule: FALSE, no graded row, turned down in one line. Keep the vendor mail as a plain distractor, so no record changes | opus · event 299 |
| R_ALREADY_MADE (T3, CH4) | Rebuild: its keyword-bearing DM reply makes it a one-search find. Keep the DM and the two files as the convincing "done" source, and put the missing piece elsewhere | opus · event 217 |
| T9 re-capture on the same ticket | Rebuild: `same_container` | opus · event 287 |
| ART-831's "Not on the live creatives sheet yet." | Drop that one sentence, so the ticket stops announcing itself | opus · event 54 |

## 10 Proposed rebuilds (candidates for `/create-scenario --revise` S5a)

Every candidate is a Hardness v2 move (§13.4): a correction moved off the swept path, a done source with a missing piece, or a completion note elsewhere. None adds a cohort item, a graded write type or a step: the cohort stays 58 ads and 4 store surfaces. Each carrier avoids the words the run searched, is findable by an ordinary search on the creative's name or on `Unity`, and sits in a channel Claire belongs to. Evidence that this class lands: `completed_tasks` lessons, "corrections off Opus's swept path (a later post in another channel, a DM, a calendar-only firm) are what discriminated", and judgement traps "never landed across 28+ runs".

| # | v2 move | Wrong source | Record that beats it | Base anchor | Facts it changes |
|---|---|---|---|---|---|
| 1 | Correction elsewhere + date window (traps 2, 4) | Frederick's Sep 30 mail: every ad by Wed Oct 15 | Frederick's reply, same evening, in the Sep 30 fake-installs thread: Unity manually reviews new Android creatives, so anything on Android US phone is due Fri Oct 10 | `C0880U9751A/1759211437.306779`, Frederick in it at `1759248267.162909` | Due date of each working ad on Android US phone |
| 2 | Work someone already did, moved off the ticket (trap 9); repairs T9 | The ticket's April capture note | Marcus's note in #zm-animations naming the three re-captures | `C09ATAJ220H` (Marcus's busiest channel, 73 posts in Sep) | Evidence for couch alpha 50, barrel marketing2 4:5, balloons alpha 50 (1); their calls stay Halloween version |
| 3 | Done source with a missing piece (trap 1); rebuilds T3 | Marcus's DM and the two Halloween files | Robert's review in a #zombie-art thread: the test sits on the July capture, so it cannot ship | Robert's review style, `C08R8CHB0QL/1758211038.665909` | cheer fastcouch 9:16 and 16:9: Reuse becomes Halloween version, assigned to Marcus |
| 4 | Correction elsewhere, changes a write (trap 2) | Leonard's split: Martin has the stills | Martin's vacation post in #company-internal, with Leonard's reply: Julia takes the ad statics | Leave convention `C05KNDCHAAG/1756717965.570179`, cover precedent `C05KNDCHAAG/1719394673.875309`, Julia's statics `C06DJBJL798/1749230960.644899` | Maker and assignee of the six working statics |
| 5 | Wrong input to a decision (trap 8 shape) | Ticket campaign notes | Frederick's Sep 29 restart mail: two landscape cuts left off iOS UK tablet | iOS retention restart Sep 29 (`/injection` §8.2) | squirrelfail landscape, mrfluffernot landscape: only Android US tablet remains, so Refresh first becomes Skip |
| 6 | Hidden exception in another service (trap 5) | "Rendered from Android #1529" on the tickets | Frederick's comment on the Marketing Video Refresh card: Unity flagged the old logo on end card 001 and its three cuts | Card `68768a1501ae552dbee94b8a` (no comments yet), rename Jul 24 (`C0880U9751A/1738109783.735889` lineage K02) | Four end cards: Halloween version becomes Refresh first |

Rejected:
- "Fewer screens in the iPhone set": base shows 5 live iPhone and 6 Google Play screens (`C06DJBJL798/1753779950.636719`, `C06DJBJL798/1756393931.415699`), which match the folder, so this would need a false base claim. Move 3 covers the same trap.
- Moving Leonard's store-ticket reply: Opus would likely open two tickets regardless, and `/prompt` issue 1 depends on that reply.
- Capture build behind an alias: an unknown label is a visible caveat, and Opus looks those up.

Expected effect if every carrier is missed: 11 of 58 calls wrong, 6 assignees wrong and about 30 due dates wrong, from six independent root causes in six containers. No single record decides more than about a quarter of the answer. All numbers are design targets, not measurements.

## 11 Routing (proposed; S0r decides)

Universe changes proposed: moves 1–6 and the ART-831 sentence, with these facts changing:
- Calls: cheer fastcouch 9:16 and 16:9 (Reuse to Halloween version); squirrelfail landscape and mrfluffernot landscape (Refresh first to Skip); end card 001, end card 16:9 from 001, end card 1:1 from 001, end card 4:5 from 001 (Halloween version to Refresh first). New ad totals: 36 Refresh first, 12 Halloween version, 10 Skip, 0 Reuse.
- Owners: the six working julia statics move from Martin to Julia. Assignments stay 48: 6 Julia, 42 Marcus.
- Due dates: Fri Oct 10 for working ads on Android US phone, Wed Oct 15 for the rest.

Prompt-side defects: none. `/prompt` scored 5 on every dimension (`Clock:` 2025-10-01 00:00 PT (2025-10-01 07:00 UTC)) and `04_Prompt.txt` stays byte-identical, because "every ad we're running", "who makes what by when" and "whoever's making them" already reach each change.

| # | Quoted span | Rule (doc §) | Defect | Evidence (rollout · step) |
|---|---|---|---|---|
| none | none | none | no prompt-side defect found | opus · event 2 onward |

OE and rubric observations: neither exists yet. When written, keep them off Unity CPI and spend (SC-11), ART-790, go-live dates and ticket state, as `/prompt` advises. `overly_broad` rows, idle-pass rows and Trash or attachment-only evidence do not apply: every new carrier is a normal Slack, Gmail or Trello record.

S0r outcome (`/create-scenario --revise`, design section 14), after two blind reviews; sections 9–11 above stay as proposed:
- Move 6's reason changed. "Old logo" contradicted base (older end cards had no logo, Martin supplied it on Jul 31), so the record now says the old zombies are on the packs, which base confirms (`C08R8CHB0QL/1754310794.907609`, `C08R8CHB0QL/1754316299.381419`). The rule is R_OLD_PACKS.
- The proposed cut to ART-831 was declined: the prior `/injection` and `/prompt` rely on that sentence and it buys no difficulty.
- Leonard's base line about LA (`C05KNDCHAAG/1759279503.256079`) was resolved at rev3: the review invite now says he dials in, because rev3's path into #company-internal puts that line in front of a reader.
- Martin's post moved before Leonard's ask to match his working hours; Leonard's reply stays last, so the correction still lands after the ask.

## 12 Self-review

| # | Item | Strongest counter-reading | Resolution |
|---|---|---|---|
| 1 | R_DONE_EXPORT LEAKED | Argue the trap was never live: if the folder listing is the only natural check, the decoy may be off the path | It was live: Martin's post was met first at run-1 · event 225, and the listing at run-1 · event 231 corrected it. LEAKED stands, because a bulk call carried the answer |
| 2 | R_ALREADY_MADE LEAKED | Argue FALSE: the reply contains the task keyword, so nothing could be missed | The natural search did return it at run-1 · event 217, and the wrong reading was available until then. LEAKED, with a rebuild in section 10 |
| 3 | R_FLIGHT_CHANGE LEAKED | Argue the rule was stated verbatim where the agent reads first | It was: both mails came back in one call at run-1 · event 17. It stays LEAKED rather than FALSE because the draft is a real claim the run had to discard at run-1 · event 29 |
| 4 | R_SCOPE_SERVING LEAKED | Argue a bulk call carried the answer | Yes: run-1 · event 60 listed every library ticket. Kept LEAKED; the sentence in section 9 goes |
| 5 | R_ART_CURRENT LEAKED | Argue it could have failed for a tool reason | No: 58 of 58 `linear_list_comments` calls returned at run-1 (`calls.jsonl`, `error` false on all). Volume was brute-forced, so LEAKED stands |
| 6 | R_BUILD_CUT LEAKED | Argue the Oct 15 ticket date is a landing | The ticket text states the Oct 16 cut at run-1 · event 272 and `/hardness` calls it minor, so it is not a material miss and not LANDED |
| 7 | R_PACK_ALIAS FALSE | Argue LEAKED, since the plan reached the right answer | The rule decides no slot (`hardness_v2_check.py` DECISION_FLIP) and the run skipped both alias hops at run-1 · event 299, so it never coupled. FALSE |
| 8 | Band 2 | Argue the neighbouring band 3 from the same map: 34 rows carry an invented Oct 8 date | The Oct 15 date is present on every row (run-1 · event 287), so the extra milestone adds and replaces nothing. A cascade counted once is one MINOR_GAP. Argue band 1: the store date is a real deviation (doc `f_fdd6d2d2f4a4d2f5b908fb`). Band 2 holds and matches the platform |
| 9 | Surface grader 6.8% | Argue the run really failed those 19 slots | Each was read in the write payload at run-1 · event 287 and run-1 · event 294 and each is met, so no CONFOUNDED or failed slot is counted (section 7) |

Re-verified through the tools, not from notes: Frederick's Aug 13 cut (`hg.py search` `messages/C06DJBJL798/2025-08.json` `/22/text`, "the background music is baked in"); Frederick's retention line (`messages/C0880U9751A/2025-09.json` `/472/text`); and, through `base_check.parse_sql` on the SQL, Martin's post `1759245641.309714`, Marcus's reply `1759166437.080255`, Leonard's reply `1759247246.453725`, `cmt_art795_2`, `cmt_art831_2`, Trello `68dc65a0f2d7fb28743f5860`, 11 Halloween store files and no iPad file. The band check grepped the write payloads for every designed flag, and none was missed.

Mechanical checks re-run: `trajectory_ledger.py`, `node_verdicts.py` and `surface_grader.py` on the final inputs. `difficulty_stats.py` does not apply before a baseline.

New-release FAIL classes (B3f): no rubric or OE exists, so nothing is attributable yet. The prompt has no Contrived or false-premise finding (`/prompt` PASS 5).

Unresolved:
- The `surface_grader.py` residual in section 7, whose cause was not found. It does not affect any verdict.
- The ledger holds only this task's six records, so the forecast is close to prior.

```
STAGE GATE hardening: PASS — Task_Authoring/task_inputsN2 · 01a_Hardening_Report.md#b39c57050122 · 01_Universe_Inject.sql#0a08dedecd60 · 01_Hardness_Manifest.json#a1d69c31fa21 · 00_Assigments.md#6a3ab458705a · 01_Grounding_Dossier.md#c6af9569529d · 06_PreCheck_Trajectory#18993d4b5edf · 07_Baseline_Trajectories#ad7848c1ad99 · 10_Baseline_Verifier_Results.md#e3b0c44298fc · __context__#215120f48d25 · __assignment__#fb0a0d31ccbc · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#98dc80681d27 · blocking 0 · warnings 0 · checks 17
[PASS] assignment.v3_context: Claire Morgan / Art Lead; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#0a08dedecd60, 01_Hardness_Manifest.json#a1d69c31fa21, 01_Grounding_Dossier.md#c6af9569529d, solver/solver.py#debf4347f85a, 01c_Dispositions.json#1e36d090cbb4, 01c_Preflight_Report.json#c050112218fe, 00_Assigments.md#6a3ab458705a, 01_Scenario_Design.md#220b3403cb4c, 01_Hardness_Manifest.draft.json#014850c608bc, 01_Gradable_Surface.json#054fd42a239c, __context__#215120f48d25, __assignment__#fb0a0d31ccbc, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#98dc80681d27)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 7/7 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 9 evidenced counter-readings (of 9 found; need ≥ 9) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```



## 13 Next steps

1. `/create-scenario --revise`: disposition these verdicts (section 14 of the design) and take moves 1–6 from S5a.
2. `/create-injection`: implement rev3, then the local gates.
3. User: upload the rev3 SQL, run `/injection` and `/prompt`, take a fresh unhinted Opus 5.5 run, then `/hardness`.
4. Only after `/hardness` is 3 or more: the six-run baseline, `/oe`, `/rubric`.

5. Status of rev3, for the record: SQL sha256 `0a08dedecd603c6c32f6b58a0ba6c0bddfffee097d54a2218857bb1bd6c08637` is stored at `run_forensics/rev3/01_Universe_Inject.sql`; `stage_gate.py scenario` and `injection` both PASS. Forecasts `hev_4f4ab9376646ceac` (design) and `hev_a770340179dc5aec` (injection) are pre-registered and UNCALIBRATED: E[avg] 0.701–0.722, P(all gates) up to 0.585, from Beta(1,1) priors on the new families. Replaying this run's search path through the rev3 solver (all six carriers missed) gives 52.9% on the surface, with 38 of 62 items wrong in at least one field. That is a model of one path, not a measurement.

Stop rule: this was platform pre-check 1 of 2 for this scenario.

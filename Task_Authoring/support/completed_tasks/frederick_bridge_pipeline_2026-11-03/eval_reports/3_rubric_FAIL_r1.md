## RUBRIC EVALUATION REPORT

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## Fix List

Row numbers are your current rubric's. "New row" means an added row; copy the text exactly. The fixed rubric has 38 rows.

- **R1** (bundles two checks: folder from the prompt, native Google format from the README): split it into two rows. **R1:** "The Agent puts the bridge-round send list in Frederick's Drive folder "Q4 2025 investor update" (created there or moved there)" (Outcome, 1). **New row:** "The Agent creates the bridge-round send list as a native Google Sheet or Google Doc" (Outcome, 1). (checked)
- **R6** (weight too low; the other Awaiting reply placements need several sources): set weight 5. Title: "The Agent puts Treo VC (or Treo, Treeo VC) in the Awaiting reply group on the bridge-round send list". (checked)
- **R7** (name forms only in the evidence): "The Agent adds Homa (or HOMA, Homa Games, [PERSON_NAME_0854] as it appears in mail) to the bridge-round send list in the In talks group". (checked)
- **R8** (name forms only in the evidence): "The Agent adds Brightwater Games Fund (or Brightwater) to the bridge-round send list in the In talks group". (checked)
- **R9** (weight too low; calendar interview + doc rule + the Gmail speedrun mail to discount): set weight 5. (checked)
- **R10** (weight too low; the Slack signed rule + the Gmail Completed notice): set weight 5. (checked)
- **R12** (bundles "exactly one angel" with "Anton", and never says who counts as an angel): replace it with "The Agent lists exactly one angel (an individual investor, not a firm) on the bridge-round send list" (Outcome, 5). Anton is already checked by R10 and R11. (checked)
- **R13, R14, R16** (name forms only in the evidence): put them in the title: "…for Dentsu Ventures (or Dentsu)…", "…for T-accelerate (or T-Accelerate, T-Accelerate Capital)…", "…for Brightwater Games Fund (or Brightwater)…". (checked)
- **New row after R16** (all four build-access rows test only "iOS only"; optional repair that adds the "none" value): "The Agent records the build access for Homa (or HOMA, Homa Games, [PERSON_NAME_0854]) on the bridge-round send list as none" (Outcome, 5; sources: ZOM-567 comments, Arthur's post C0880U9751A/1759274400.518306, call evt_89381fe5a15b802c5652a9). (checked)
- **R17, R19, R20** (evidence says "close variants" without defining them): change the Accept line to "a checklist whose name contains the group name <Keep warm / In talks / Awaiting reply> (any letter case, spacing or plural; other words around it are allowed) with exactly <3 / 7 / 14> items". (checked)
- **R18** (bundles the item count with "Anton Bernstein"): split it. **R18:** "The Agent creates a New investor checklist on the Existing Investor Update Trello card holding exactly 1 item" (Outcome, 5; same Accept wording as R17). **New row:** "The Agent adds Anton Bernstein as an item on the New investor checklist of the Existing Investor Update Trello card" (Outcome, 5). (checked)
- **New row after R20** (no row checks who is on the 14-item Awaiting reply checklist): "The Agent adds Sony Mobile (or Sony) as an item on the Awaiting reply checklist of the Existing Investor Update Trello card" (Outcome, 5; sources: list f_48247af79428823c3cac92 No. 83, #bridge-pitch C096HFA5Z8W/1757345124.546449, the send-list doc, card comment 68db03b86054eff7e8e92474). (checked)
- **R21, R22** (weight too low; the same multi-source placement as R4 and R7): set weight 5. (checked)
- **R23** (evidence cites Leonard's Dentsu email; the deciding record is the calendar event): cite Dentsu meeting evt_3671b9a924ccba550e51fa (Oct 1) and make the Accept line "exactly 18 new cards in To Do named 'F/up with' and a firm or contact name". (checked)
- **R24** ("its contact's name" isn't named anywhere a judge can see): "The Agent creates a follow-up card for GFR Fund in the To Do list of the Harmony Games Trello board (named "F/up with" and GFR Fund, GFR, PERSON_0787_NAME or [PERSON_NAME_2306])", weight 5. (checked)
- **R25** (weight too low; same work as the GFR and Brightwater cards): set weight 5. (checked)
- **R26** (weight too low; the closed name list misses "Brightwater" and "Ilse"): weight 5, "…(named "F/up with" and Brightwater Games Fund, Brightwater, Ilse Marrow or Ilse)". (checked)
- **R33, send-list part** (two order checks across two services, and "sheet" although a Doc is valid): replace it with "The Agent sends its reply on Leonard's thread only once its writes to the send list file are finished (at least one write to that file comes before the reply and none after it)" (Process, 1). (checked)
- **R33, Trello part:** this row needs your own rewrite. The open problem: an order row for the Trello work has to (a) fail a run that does no Trello work at all, (b) not bundle the three Trello write kinds (checklists, follow-up cards, the NCsoft comment) into one check, and (c) not require every write to be complete, because that would fail along with every Trello row. The version I tested ("…once its writes on the Harmony Games Trello board are finished…") still drew a bundling finding after the restructure round. (revised after check, needs your own rewrite)

### Task: Bridge-round Q4 investor update send list (Drive file, Trello checklists and follow-up cards, reply to Leonard)
### Persona: Frederick Stone - Co-founder
### Total Rubrics: 33 (Outcome: 32, Process: 1)

---

### Phase 1: Structural Validation
- Five-field completeness: 33 of 33
- Category distribution: Outcome 32, Process 1
- Requirement coverage: 37 of 38 outcomes (the Awaiting reply checklist's item names have no row)
- Code checks (`hg_rubric_lint.py`): 4 `anon_token` hits on R7 and R22, resolved: `[PERSON_NAME_0854]` is accepted as shown and bound as a literal. No vague exemplar, tool name, prohibition or format-lock hits.

### Phase 2: Per-Rubric Quality
| Row | Issue | Type | Severity |
|---|---|---|---|
| R1 | Folder placement (prompt) and native Google format (README) bundled | non_atomic | Major |
| R12 | Angel count and the identity "Anton Bernstein" bundled | non_atomic | Major |
| R12 | Who counts as an angel comes only from the 2025 list | not_self_contained | Major |
| R18 | Checklist item count and its item "Anton Bernstein" bundled | non_atomic | Major |
| R24 | "its contact's name" is not named anywhere a judge can see | not_self_contained | Major |
| R33 | Two order checks (after the sheet writes, after the Trello writes) | non_atomic | Major |
| R33 | "send list sheet" although a Google Doc is valid | harmless_specificity | Minor |
| R10, R12 | Both fail on one error (Anton left off) | duplicate (overlap group) | Moderate |

Atomicity decomposition: R1 (folder | native type: independent), R12 (count | identity: independent), R18 (count | identity: independent), R33 (after sheet | after Trello: independent). Every other row is one destination with one fact or value.
Over-specificity triage: all rows accept the prompt's valid alternatives (Sheet or Doc, firm or contact card titles, reply or reply-all). R33's "sheet" wording is harmless_specificity.

Fact check: every expected value is correct. The 25-recipient partition (New investor 1, In talks 7, Awaiting reply 14, Keep warm 3), Anton Bernstein's 25,000, the four "iOS only" build-access values and the 18 follow-up cards were recomputed independently by F1, F2, F3 and R2 from the injection SQL and the base exports.

### Phase 3: Set-Level Quality
- Coverage gaps: no row names any item on the 14-item Awaiting reply checklist (R20 counts only).
- Process audit: 1 of 1 valid (R33 passes the three-condition test; its bundling is scored under Overall Quality).
- Duplicates / overlap / cascade groups: `anton-listed` (R10, R12).
- Spot-check groups: send-list group column (R4–R9 plus protected R10), build access (R13–R16), checklist items (R18, R21, R22), follow-up cards (R24–R26); volume rows R3, R17–R20, R23 present. Selection notes are under "Worth a look".
- OE cross-check: every row maps to OE steps; no OE conflict.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 6 rows + 1 missing outcome | 21% | any | FAIL |
| Moderate | 1 (overlap group) | 3% | any | FAIL |
| Minor | 0 counted (R33's Minor is absorbed by its Major) | 0% | ≥ 5% | — |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 1 | Major non_atomic, not_self_contained and missing_coverage issues, plus one Moderate overlap group |
| Criteria Weights | 2 | 8 of 33 rows (24%) one level low: R6, R9, R10, R21, R22, R24, R25, R26 should be 5 |
| Rubric Category Balance | 5 | 32 Outcome rows |
| Process Rubrics | 5 | R33 is a valid ordering check |
| Agent-Centric Phrasing | 5 | Every title starts "The Agent" and names no tool |
| Negative Criteria | 5 | No prohibition titles; an idle Agent fails every row |
| Predicted All-Fail gate | PASS | No row predicted to fail every run |

**Lowest Sub-Dimension:** Overall Rubric Quality - 1 - bundled rows, two rows that aren't self-contained and one missing outcome.

## All Findings

**R1** · non_atomic · Major · F1, R7, F2, F3 (unsure). Folder (prompt: "Please put the send list in my Q4 2025 investor update folder") and native format (README f_c61a0e93b7d24f58a2e917: "Google Sheets or Docs only, no uploads") fail apart: an uploaded .xlsx in the folder passes one and fails the other. Fix: split (Fix List).

**R6, R9, R10, R21, R22, R24, R25, R26** · Criteria Weights, one level low · R4, F2, F3 (R6 and R25 from the fix-check R4 pass). Each placement needs a join across sources: R9 calendar interview evt_e802a3583ee79ff6087f76 + doc accelerator rule + the Sep 30 speedrun mail; R10 #executives rule C07C2866011/1758911700.336170 + Completed notice 1844354293432320031; R21 and R22 the same work as R4 and R7 (weighted 5); R24 the Sep 12 outreach + the Sep 30 call evt_2204ffea306847eea6e5b0 + the Trello rule; R25 Latest Status + #bridge-pitch + calendar + To Do; R26 call evt_2f86b0d4c9e17a35b64e0d + Ilse's signed mail + To Do and calendar checks; R6 Slack Sep 3 posts + doc rule + no call. 8 of 33 rows (24%) is over the 10% band. Fix: weight 5.

**R12** · non_atomic + not_self_contained · Major · F1, R7, F3, F2. "exactly one angel … : Anton Bernstein" bundles a count with an identity. Anton plus Paul passes the identity and fails the count; Paul alone passes the count and fails the identity. Who counts as an angel comes only from the list (list f_48247af79428823c3cac92, angels No. 1–5). Fix: a bare count that defines "angel" in the title.

**R10, R12** · duplicate (OVERLAP_GROUP `anton-listed`) · Moderate · F3. Both embed "Anton is on the send list", so leaving him off fails both. Removed by the R12 fix.

**R18** · non_atomic · Major · F1, R7, F3. A New investor checklist holding only Paul Heydon has exactly 1 item but the wrong one. Fix: split into the count row and an Anton item row.

**R24** · not_self_contained · Major · F1, R6, F2, F3. "its contact's name" isn't in the title, the prompt or any other title; the records show two forms (list Partner `[PERSON_NAME_2306]`; Gmail and calendar `PERSON_0787_NAME`, thread "Re: GFR Fund <> [SOURCE_ORG_0001]"). Fix: name both.

**R33** · non_atomic · Major · R7 (F2, F3 unsure). "after its last write to the send list sheet and to the Harmony Games Trello board" is two order checks across two services. **Also harmless_specificity · Minor** · R1, R4, F2, F3: "sheet", although R1 accepts a Google Doc. Fix: split; the Trello half needs your own rewrite (Fix List).

**Missing outcome: Awaiting reply checklist items** · missing_coverage · Major · F1, R3, F2 (F3 as a repair). R20 only counts 14 items and no row names any of them, so a checklist naming Play Ventures instead of Makers Fund passes every row (comment 68db03b86054eff7e8e92474: "its own checklist on this card, one item per firm or angel"). Fix: one item sample row (Sony Mobile, the advisor's-read edge case).

**R23** · evidence repair, not scored · R2, F2, F3. The card exemption is "on Fred's calendar after Sep 30"; the evidence cites Leonard's Dentsu email 1843473831194478743 instead of event evt_3671b9a924ccba550e51fa (2025-10-01 20:30 UTC). The value 18 is correct.

**R19, R20** · wording, not scored (QC B12) · F2, F3. "a In talks", "a Awaiting reply" in the evidence.

### Worth a look (not scored)
- Build access: all four samples (R13–R16) test the same "iOS only" edge; the "none" value (GFR Fund, Andreessen Horowitz, Homa) is never sampled (R3, F2, F3). Eval 3 §3.6 treats a weak selection as a repair; the Fix List adds an optional Homa "none" row.
- Send-list groups: R4–R9 are all edge cases. Sony Mobile (an advisor's read isn't a no) and Initial Capital (wrote back, still Awaiting reply) are good extra samples; up to 5 per group is allowed (R3, F2).
- Keep warm checklist: Hiro Capital (the unnamed-pass edge) could be a second item sample (F2).
- "Leave it blank for angels": no row checks Anton's build-access cell. A row worded "leaves … blank" would fail Negative Criteria, so keep it off (R3).
- R29–R32 accept a single number per group; Leonard asks for firms and angels, but the prompt says "how many ended up in each group", so both readings are fine (R3, F2).

### Rejected findings
- R7 pass: R17, R19, R20 bundle "creates a checklist" with its item count. Rejected: one destination plus one fact is one result (Eval 3 §2.2 decision rule).
- R5 pass: R3–R16 don't name the file. Rejected: sibling R1 defines "the bridge-round send list" as the file in the folder, and QC B3 lets sibling titles supply it.
- R6 pass: "Treeo VC" appears in no source. Rejected under (a): base #bridge-pitch C096HFA5Z8W/1756941551.539229 reads "Treeo VC (inbound b2b AI, Leonard responded on linkedin)".
- R4 pass: R11 should be weight 3 because "every source is Slack". Rejected under (a): the Bridge angels sheet f_6e1d93a0c4b72f85d39a0e (Sheets, 40000) is also overridden, so it is a cross-service reconciliation.
- F3: R4–R10 exceed five samples in one group. Rejected: R7 and R8 (off-list firms with calls) and R10 (New investor, "Get the new investors right") are distinct outcomes covered directly (rubric_sampling: "If an exception is itself a core/distinct outcome, cover it directly"), leaving four samples.
- R3 pass: R29–R32 should require the firms/angels split. Rejected: the prompt asks "how many ended up in each group"; accepting both renderings rejects no valid answer.
- F2: R13–R16 form a cascade. Rejected: each row grades a different firm's value; rows that share a likely root cause aren't a group (Eval 3 §3.3).
- Fix-check R4 (round 4): the two order rows overlap. Rejected: they check different conditions (the file versus the board) under "different services → always independent" (§2.2); a shared root cause isn't a group.
- Fix-check R3: an angel blank-cell row. Rejected: the "leaves … blank" form fails Negative Criteria (§2.9).

### Recommended Fixes
Every fix above was checked with `hg_rubric_ledger.py fixcheck` (no title over 120 words), `hg_rubric_lint.py` on the candidate (only anonymised-token hits, accepted as shown) and R1–R7 on the changed rows and their siblings, including the opposite-pair test. Rounds until clean: R1 split, R9, R10, Anton item, Sciplay and Homa items: 1. R12 count, R24 GFR, R25 BBQ, Sony row: 2. R6 Treo, R23 cards, R26 Brightwater card, Homa "none" row: 3. R7, R8, R13, R14, R16 names, the checklist Accept lines, the send-list order row: 4 (after a restructure). The Trello order row: 4 rounds, restructured, still open (needs your own rewrite).

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7, Opus 5.5 (this skill's model), each blind to the main review. Two more independent full reviewers (F2, F3) ran alongside.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 33 rows | 1 | 1 |
| R2 | 33 rows | 1 | 1 (evidence repair) |
| R3 | 33 rows | 5 | 1 (others repairs or rejected) |
| R4 | 33 rows | 8 | 5 |
| R5 | 33 rows | 1 | 0 |
| R6 | 33 rows | 2 | 1 |
| R7 | 33 rows | 7 | 4 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R1 | R33 "send list sheet" | README f_c61a0e93b7d24f58a2e917 "Google Sheets or Docs only" | Overly specific | harmless_specificity | CONFIRMED | R1 accepts a Doc |
| DR1 | R2 | R23 evidence "Dentsu mail …1843473831194478743" | gcal evt_3671b9a924ccba550e51fa | Incorrect | evidence citation | CONFIRMED | Evidence-only repair; the value is correct |
| DR1 | R3 | R13–R16 only "iOS only" | ZOM-567 has no GFR, a16z or Homa entry | Coverage | sampling selection | REJECTED | Weak selection, reported as a repair (§3.6) |
| DR2 | R3 | "Leave it blank for angels" | doc f_3b9e61c04d7a52e8f1a6c2 | Coverage | missing_coverage | REJECTED | The row it implies fails Negative Criteria |
| DR3 | R3 | R29–R32 single number | Leonard's email | Coverage | missing_coverage | REJECTED | The prompt allows the group count |
| DR4 | R3 | R20 count only | comment 68db03b86054eff7e8e92474 | Coverage | missing_coverage | CONFIRMED | No AR item row |
| DR5 | R3 | R6 sole AR sample | C096HFA5Z8W/1757345124.546449 | Coverage | sampling selection | REJECTED | Repair note |
| DR1 | R4 | R21 weight 3 | R4 weight 5, same sources | Weights | weight | CONFIRMED | Multi-source |
| DR2 | R4 | R22 weight 3 | R7 weight 5 | Weights | weight | CONFIRMED | Multi-source |
| DR3 | R4 | R26 weight 3 | evt_2f86b0d4c9e17a35b64e0d + mail | Weights | weight | CONFIRMED | Multi-source |
| DR4 | R4 | R24 weight 3 | evt_2204ffea306847eea6e5b0 + Slack | Weights | weight | CONFIRMED | Multi-source |
| DR5 | R4 | R10 weight 3 | C07C2866011/1758911700.336170 + 1844354293432320031 | Weights | weight | CONFIRMED | Join across Slack and Gmail |
| DR6 | R4 | R9 weight 3 | evt_e802a3583ee79ff6087f76 + doc + Gmail | Weights | weight | CONFIRMED | Multi-source |
| DR7 | R4 | R11 weight 5 | DMs D05S58U4SAK | Weights | weight | REJECTED | The Bridge angels sheet is also a source |
| DR8 | R4 | R33 "sheet" | README | Process | harmless_specificity | CONFIRMED | Merged with R1 DR1 |
| DR1 | R5 | R3–R16 destination | prompt folder sentence | Destination | overly_broad | REJECTED | R1 defines the send list |
| DR1 | R6 | R24 "its contact's name" | list No. 7 [PERSON_NAME_2306]; evt_2204ffea306847eea6e5b0 | Self-contained | not_self_contained | CONFIRMED | Contact not named |
| DR2 | R6 | R6 evidence "Treeo VC" | C096HFA5Z8W/1756941551.539229 | Self-contained | not_self_contained | REJECTED | The source spelling exists; a rendering of the same firm |
| DR1 | R7 | R12 count + Anton | list angels No. 1–5 | Atomic | non_atomic | CONFIRMED | Fails apart |
| DR2 | R7 | R18 count + Anton | comment 68db03b86054eff7e8e92474 | Atomic | non_atomic | CONFIRMED | Fails apart |
| DR3 | R7 | R17 checklist + count | — | Atomic | non_atomic | REJECTED | Destination plus one fact |
| DR4 | R7 | R19 checklist + count | — | Atomic | non_atomic | REJECTED | Destination plus one fact |
| DR5 | R7 | R20 checklist + count | — | Atomic | non_atomic | REJECTED | Destination plus one fact |
| DR6 | R7 | R33 sheet and Trello | Leonard's email | Atomic | non_atomic | CONFIRMED | Two services |
| DR7 | R7 | R1 type + folder | README | Atomic | non_atomic | CONFIRMED | Two sources |

Effect on verdict: the confirmed findings are in the scoring record (Overall Rubric Quality 1, Criteria Weights 2); the verdict stays FAIL.

Platform defects: none

### FINAL VERDICT: FAIL
Score: 1
Execution status: COMPLETE
Next action: Apply the Fix List (rewrite the Trello order row yourself), update the rubric in your Outlier task, then send /rubric again.
Evidence limits: none
Evaluator model: claude-opus-5-5
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Review policy: rubric-revision-v10
Review mode: AUDIT
Ready for prefill: No
Reviewed JSON SHA-256: 5875117a9b71841f03b0ec44c304763290563893e875809f9e8e93b540591d02
Review context SHA-256: 9e2242d6f66f50ee9219f9a5ea1ecd8448bbd4863929295eecdf52d979bc17c9
Scoring record SHA-256: 4e0249e8c1220f0cb20c8b69d2512e022f8784463b33f4cf9c2022e497d79914
Gate tier: localized
Coverage ratio: 37/38
Repairs: R1, R6, R9, R10, R12, R18, R21, R22, R24, R25, R26, R33
Eval version: task-quality-v1
Eval release SHA-256: a6d0d5849af43fa85dc1c2d9bf598b27771ddcb6c23e39cc14c4eba835fe3225

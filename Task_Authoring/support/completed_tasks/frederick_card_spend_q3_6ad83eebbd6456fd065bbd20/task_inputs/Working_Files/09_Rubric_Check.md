# 09 Rubric Check — card-spend breakdown (Frederick Stone, Q3 Standard Metrics)
Checked 2026-10-24 (re-run after fixes) · Criteria 54 (builder minimum 5: ok) · Plan 09_Rubric_Writing_Plan.md (stale: 40 rows, pre-hardening; see Reminders)
JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass (54 rows, five non-blank fields each, all `Outcome`, weights 1/3/5 only)
Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict

Inputs read: 04_Prompt.txt (sha 3ffe1dd1…), 08_Oracle_Events.md (38 OEs, /oe PASS 5 on 2026-10-24), 01_Universe_Inject.sql (sha 7b3552ae971b), 09_Rubrics.json (sha daf860cb6bab…, 54 rows, weight 208), Evals/3_Rubrics_Eval.md, rubric_flow_v2.md (scope checklist), coherent_record.md, rubric_sampling.md.

What changed since the first check (previous file kept at Working_Files/09_Rubrics.pre_check_fix.json): old C2 deleted; C12 and C24 name the eight categories; C19 drops "on the Lite plan"; C23 adds "exactly"; C31, C32, C33 trimmed to the finding; C36–C39 drop the unrequested amounts; weights C24, C28, C34 3→5; new C51–C55 (disputed count/total, checklist preserved, board cards unchanged, ENG-2370 count, Informa 2025-03 cell). Second /rubric round (report 6ad83eebbd6456fd065bbd20_3_rubric.md, schema-only FAIL): key `criterion` renamed to `title`; old C53 (board cards unchanged) folded into C30 as its target scope; C52 tied to the posted comment so a run that writes nothing fails (platform lint `disguised_negative`); C10, C15, C28 evidence now cite record ids (`evidence_no_record`). Backups: Working_Files/09_Rubrics.pre_title_rename.json. Numbering below is the new file's.

## Coverage
| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |
|---|---|---|
| Workbook in the Q3 2025 investor reporting folder (prompt; SQL L9) | C1 | Covered: Q2 folder (SQL L7) fails on the id |
| Rule 11 tab names (close notes, SQL L19) | C2, C7, C12, C16 | Covered by the tab-named content rows |
| By vendor, Jan–Sep, month by month (SQL L3050) | C7 volume; C8–C11 totals; C54 monthly cell | Covered |
| By Griffin's categories, month by month | C12 volume; C13, C14, C15, C42 | Covered |
| Tie each month to the ledger | C2 volume; C3–C6 | Covered |
| Q4 monthly run-rate by vendor (rule 9) | C16 total; C17–C21, C40, C44–C46 | Covered; the total rejects the bank-rule vendors |
| Cancelled but still charged, in the reply (rule 8) | C29, C43, C47, C48; C51 count/total | Covered; refunded decoys fail C51 |
| Reply on Leonard's thread | C22 | Covered |
| Reply recipients (DM D05S58U4SAK) | C23 | Covered, extra recipients fail |
| Reply: totals by category | C24 volume; C25, C26, C27, C41 | Covered |
| Reply: monthly run-rate | C28 | Covered |
| Comment on #481 with findings | C30; C31–C34, C49, C50 | Covered |
| #481 checklist left to Leonard (scope checklist) | C52 | Covered |
| No new card (scope checklist) | C30 | Covered: "rather than starting a new card" in the write row |
| Arthur's still-charged items on ENG-2370 | C35; C36–C39 | Covered |
| ENG-2370 wrong targets (scope checklist) | C53 | Covered: Backtrace listed as still charged fails |
Unauthorized criteria: none

## Findings
| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |
|---|---|---|---|---|---|---|---|
| 0 | all | "The Agent's reply lists exactly four disputed charges, totaling 195.99" | Eval Phases 1–5 | No defect found on re-check; the 17 findings of the first check are fixed in this file | OE 27 / OE 38 | none | — |

Note (not tallied): C14 (Hosting 2025-09) is a weak discriminator for Griffin's Unity answer, since September has no Unity seat charge; C25 and C26 cover that answer.

## Overlap groups · Spot-check groups · Predicted all-fail
| Group / row | Members / basis | Shared condition / reason |
|---|---|---|
| Overlap groups | none | C16/C28, C40 (tab) and C47/C49, C48/C50 are one fact on two prompt-required deliverables (gate 6); C51 and C53 are aggregate controls beside their items (Eval 3.3) |
| Spot-check: By vendor | C8, C9, C10, C11, C54 (5) + volume C7 | ≤ 5 samples |
| Spot-check: Category by month | C13, C14, C15, C42 (4) + volume C12 | ok |
| Spot-check: reply categories | C25, C26, C27, C41 (4) + volume C24 | ok |
| Spot-check: ledger tie-out | C3, C4, C5, C6 (4) + volume C2 | ok |
| Run-rate tab | direct rule-8 exceptions C17, C19, C40, C44, C45, C46; annual-plan samples C18, C20, C21 (3) + total C16 | exceptions direct (gate 15) |
| Predicted all-fail (four Eval 5.1 bases) | 0 rows | Every value is reachable by Frederick (SQL L3094–L3150 inbox mail, feed folder, DM, Trello, Linear, Snowflake) |
| Observed all-fail in the six baselines | C16, C28, C44, C46 | Model misses of reachable mail (SQL L3142, L3150); justify in /create-allfail |

## Dimensions
| Dimension | Count / % | Threshold | Status |
|---|---|---|---|
| Overall Rubric Quality | 0 Major, 0 Moderate, 0 Minor of 54 | any Major or Moderate fails | PASS 5 |
| Criteria Weights | 0 rows off | ≤ 10% one-level = NON-FAIL 4 | PASS 5 |
| Category Balance | 54 Outcome, 0 Process | ≥ 1 Outcome | PASS 5 |
| Process Rubrics | 0 Process rows; no ordering dependency in the prompt | none invalid | PASS 5 |
| Agent-Centric Phrasing | 0 artifact subjects, 0 tool names | — | PASS 5 |
| Negative Criteria | 0 prohibition-only titles (pre-scan for not / no / never / without / avoid: 0 hits) | 0 | PASS 5 |
| Predicted all-fail | 0 | tolerance 0 | PASS |
| Coverage repair gate | 0 missing outcomes | 0 | PASS |
| Schema, accuracy, contradiction repair gates | 0 incorrect, 0 unobservable, 0 contradictions | 0 | PASS |

Pre-verdict sweep (Eval 5.0): missing requirement = pass · phrasing mismatch = pass · non-atomic = pass · category mislabel = pass · over-specific = pass · duplicate/cascade = pass · vague exemplar = pass (0 hits in any field) · prohibition-only = pass.

Mutation tests (Eval 3.7): run-rate 3,226.80 → C16, C28 · Webflow 29.00 → C44 · Murf 22.00 → C46 · Midjourney Aug 2 added as disputed → C51 · SavvyCal missing → C47, C49, C51 · checklist item ticked → C52 · new Trello card → C30 · Backtrace on ENG-2370 → C53 · Griffin copied → C23 · Robert missing → C23 · June folded into July on Category by month → C13 · Informa refund booked in Feb → C54 · Unity seats under Software → C25, C26. A complete valid solution passes every row.

Effect on the six baselines (local estimate, weight 208): run-1 to run-4 ≈ 76.0%, run-5 ≈ 71.2%, run-6 ≈ 88.0%; average ≈ 77.2%. The platform verifier decides.

## Self-review
| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |
|---|---|---|---|---|
| C1 | CLEARED | Valid: a workbook created anywhere then moved into the folder passes. Near miss: Q2 2025 folder (SQL L7, d_89db817086de1e12427175) fails on the id. Evidence pointer now SQL L9. | Re-verified against the SQL lines and hg.py reads cited | none |
| C2 | CLEARED | Valid: June as its own tie-out row still totals 97,968.21 (OE 12). Near miss: calendar months fail. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C3 | CLEARED | Valid: June folded into July or listed separately both state 12,222.02 + 12,132.35 = 24,354.37 (FIN-000580, snowflake.json /tables/38/rows/579). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C4 | CLEARED | Near miss: Unity Ads under Marketing leaves 22,090.21 and fails (rule 7, SQL L19). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C5 | CLEARED | Near miss: including the Sep 29 postings fails (rule 3, FIN-000618). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C6 | CLEARED | Near miss: calendar January fails (rule 3, SQL L19). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C7 | CLEARED | 43/42 is a closed set of valid layouts (Eval 2.10), not an overly broad or. Near miss: unmerged OpenAI descriptors fail (rule 12). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C8 | CLEARED | Near miss: AppMagic without its fee rows fails (feed notes f_0230719d3dcc16f12821d7). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C9 | CLEARED | Near miss: 1,150.00 ignoring the credit on f_ae25c0c1cae08271c73609 fails. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C10 | CLEARED | OpenAI / ChatGPT naming variants accepted; the justification does not widen the value (Eval 2.1). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C11 | CLEARED | Near miss: Unity 18,970.00 with Unity Ads merged fails (f_e5bd3c66de846ccd52eb65). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C12 | CLEARED | Fixed: the eight category names from SQL L3042 are now in the title (Eval 2.1). Counter-reading: categories + months + sum bundled; kept as qualifiers of one aggregate (coherent_record.md). | Re-verified against the SQL lines and hg.py reads cited | none |
| C13 | CLEARED | Near miss: June folded into July gives 0 for 2025-06 and fails (rule 4, SQL L19). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C14 | CLEARED | Weak discriminator (no Unity charge in Sep) but valid sample (rubric_sampling.md). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C15 | CLEARED | Near miss: Carta under Software fails (SQL L3042). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C16 | CLEARED | All six baselines failed it (run-1 to run-6), but every input is in Frederick's INBOX (SQL L3110, L3122, L3134, L3142, L3150); not an Eval 5.1 basis. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C17 | CLEARED | Near miss: 600.00 from ENG-2370 fails; Sep 29 Edgegap email SQL L3098 confirms 420.00. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C18 | CLEARED | 'one twelfth of the 10,200.00 annual prepay' is an operand of the value (coherent_record.md). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C19 | CLEARED | Fixed: 'on the Lite plan' removed; 250.00 alone is graded (SQL L3086). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C20 | CLEARED | ±0.01 covers 27.035 rounding (rule 11, Eval 2.10). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C21 | CLEARED | Near miss: 300.00 per month fails; rule 9 names Cogency annual (SQL L19). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C22 | CLEARED | Either Gmail send path passes; no tool named in the title (Eval 2.9). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C23 | CLEARED | Fixed: 'exactly' now rejects extra recipients (Griffin). Robert at contacts.json /contacts/108 re-read with hg.py. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C24 | CLEARED | Fixed: eight names in the title (SQL L3042) and weight 5 to match C12. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C25 | CLEARED | Near miss: Unity seats left in Software (26,331.12) fails (DM 1759248472.204417, SQL L3186). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C26 | CLEARED | Near miss: 9,335.36 without Unity seats fails. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C27 | CLEARED | Near miss: Carta under Software fails (SQL L3042). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C28 | CLEARED | Fixed: weight 5, the same reconciliation as C16 (Eval 2.12). All baselines failed it; model miss, not an Eval 5.1 basis. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C29 | CLEARED | Near miss: naming the refunded Aug 2 charge fails on the date (f_64e214d78ad44085744dad). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C30 | CLEARED | Write row with its target scope: a comment on #481 plus a new card fails; a run that writes nothing fails, so it is not a disguised negative (Eval 2.9). Content graded by C31–C34, C49, C50 (Eval 3.1). Board 68d2dafdbfcc777cc630fad0 re-read. | Re-verified against the SQL lines and hg.py reads cited | none |
| C31 | CLEARED | Fixed: citation clause removed; 'kept rather than cancelled' is the finding (Slack C07C2866011/1758910840.227619). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C32 | CLEARED | Fixed: date removed (SQL L3090). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C33 | CLEARED | Fixed: one claim, the 99.99 Sep 3 dispute (SQL L3094, f_9c2cecbd35b55e83151f42), same form as C34. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C34 | CLEARED | Fixed: weight 5 to match C29, C49, C50 (Eval 2.12). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C35 | CLEARED | Write row; content graded by C36–C39 and C54. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C36 | CLEARED | Fixed: amount removed; Unity Pro is Owner: Arthur (SQL L3247) and on the Aug 8 prepay. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C37 | CLEARED | Fixed: amounts removed; run-6 would now pass, and the 420.00 fact stays graded on C17. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C38 | CLEARED | Fixed: amount removed; Google Cloud Owner: Arthur, billed Sep 2 (f_8eeb88266f2fd9e9f26737). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C39 | CLEARED | Fixed: amount removed; 23.97 stays graded on C40 (Trello 68dac5f2a1b3c4d5e6f70812). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C40 | CLEARED | Near miss: 31.96 from Arthur's Sep 25 note fails; Leonard's Sep 29 comment SQL L3257 supersedes. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C41 | CLEARED | Near miss: GDC under Travel gives 1,020.00 and fails (DM 1759248472.204417). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C42 | CLEARED | Near miss: 0 for 2025-02 fails. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C43 | CLEARED | Near miss: LinkedIn left active (run-5) fails (SQL L3094). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C44 | CLEARED | All baselines show 29.00; the Sep 12 forward SQL L3150 is reachable; model miss. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C45 | CLEARED | The appositive is the reason for 0.00; a tab showing 0.00 passes (SQL L3110). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C46 | CLEARED | All baselines show 22.00; the Sep 25 Murf email SQL L3142 is reachable. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C47 | CLEARED | Near miss: SavvyCal listed active fails (SQL L3122). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C48 | CLEARED | Near miss: Buttondown listed active fails (SQL L3134). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C49 | CLEARED | Same fact as C47 on the #481 comment, a second required deliverable (gate 6). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C50 | CLEARED | Same fact as C48 on the #481 comment (gate 6). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C51 | CLEARED | New guard: count and total are coupled (coherent_record.md: operands of one metric). Near miss: adding the refunded Aug 2 Midjourney (f_64e214d78ad44085744dad) or Jul 9 Loom (f_5f0fdcceb9f524b65bdbfc) fails. Not a duplicate of C29/C43/C47/C48: aggregate control vs items (Eval 3.3). | Re-verified against the SQL lines and hg.py reads cited | none |
| C52 | CLEARED | Preserved state tied to the posted comment, so a do-nothing run fails (platform disguised_negative). Counter-reading: comment + checklist read as two claims; the comment is a precondition, the graded claim is the checklist state (Eval 2.2). Notion, ChatGPT, 1Password complete; the other five incomplete (SQL L3333–L3341). Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C53 | CLEARED | New count guard: Backtrace (Owner: Arthur, SQL L3259, cancelled Feb 28) listed as still charged fails. A comment that mentions Backtrace as stopped still passes. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| C54 | CLEARED | New monthly sample: -399.00 posted 2025-03-04 on the adjustments tab (SQL L441), in the March cycle under rule 5. Near miss: netting it into February fails. Cleared. | Re-verified against the SQL lines and hg.py reads cited | none |
| Re-verify | DONE | A value could be stale after the Edgegap rename or the Fiverr OE | Re-read SQL L3042, L3050, L3086–L3150, L3247–L3259, L3333–L3341, L441, L9; hg.py: contacts.json /contacts/108, trello data.json /boards/1/name | none |
| Predicted all-fail recount | 0 | The four rows every baseline failed could be read as impossible | Values sit in Frederick's INBOX (SQL L3142, L3150); no Eval 5.1 basis | none |
| Tally recount | 0 / 0 / 0 | C45's appositive or C18/C20/C21 operand clauses could read as extra requirements | Each describes the graded value (coherent_record.md operands); a tab with the value alone passes | none |
| Stage gate | see paste | The chain block needs a gated rubric plan | Upstream plan and OE check are stale (pre-hardening); see Reminders | Unresolved: rubric-writing plan not regated |

## Reminders
- An all-Outcome set is normal; Process is not added to look thorough.
- Enter the 54 criteria in the builder, export, and run /rubric.
- The local gate chain is stale: `08_OE_Writing_Ledger.md` (gate not pasted), `08_OE_Check.md` (35 events, pre-Fiverr) and `09_Rubric_Writing_Plan.md` (40 rows, pre-hardening). `stage_gate.py rubric-check` blocks on that chain until they are refreshed; the platform `/rubric` does not read them.

# 09 Rubric Check — Frederick account handover register (fs-account-custody)
Checked 2026-10-26 · Criteria 29 (builder minimum 5: ok) · Plan 2026-10-26 (29 rows P1–P29)
JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass (29 objects, all five fields non-blank, category Outcome, weights 1/3/5)
Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict

Claude drafted these criteria on the user's explicit request (2026-10-26). Fixes made in this check, before the report (backup Working_Files/09_Rubrics.pre_check_fix.json):
- C4, C5, C6, C7, C8, C12, C13: removed the "because …" / "treating … as …" clauses. A register action column states the action, not the reason; a title that bundles the verdict with its grounding is non_atomic (Eval 2.2) and would fail a correct register that gives no reasons. The reasons stay in the justification.
- C8 also dropped "with Leonard Hayes and Frederick Stone as the company holders" (a second claim on another column).
- C18 dropped "leaving Frederick Stone off because he is a Manager"; "exactly Arthur Blake, Robert and Leonard Hayes" already rejects Fred.
- C26 dropped "through its Google Brand Account": a reply naming Node's YouTube access without the mechanism answers Leonard's ask (overly_specific risk).
- C3 reworded so the count is the claim and the rule-1 exclusions explain it (the @harmonygames.app row is inside the TikTok export, not a separate account).
- C29 no longer says "that checklist" (vague reference); it names the card.
- C23 accepts "1 (one)".
- New C21 (plan P29): one class-column sample (Google Ads 569 COMPANY-HELD). Without it no criterion rejected a wholesale class-column error; this cell varies independently of its action, which Arthur's email sets.

## Coverage
| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |
|---|---|---|
| P1 register in Company Ops (R6) | C1 | Covered — rejects a run with no sheet and a sheet in another folder |
| P2 rule-6 columns (R6) | C2 | Covered — rejects a header lacking one of the five |
| P3 13 rows (R2) | C3 | Covered — rejects 14 rows (pub-2341961509332343 kept) and 12 |
| P4–P16 action per account (R5) | C4–C16 | Covered — each rejects the trap action (KEEP for Meta/Unity, TRANSFER for TikTok/YouTube/Instagram, CLOSE for 569/socials, KEEP for adjoe/AdMob) |
| P17, P18 holders (R3) | C17, C18 | Covered — rejects a holder list short of the named people and Fred on Unity |
| P19, P20 money moving (R4) | C19, C20 | Covered — rejects N |
| P29 class sample (R3) | C21 | Covered — rejects SINGLE or OUTSIDE ACCESS |
| P21 reply sent in the DM (R7) | C22 | Covered — rejects a reply in another channel or by email |
| P22 TRANSFER count (R7) | C23 | Covered — rejects 2, 3, 4 |
| P23–P26 outsider access (R7) | C24–C27 | Covered — each rejects a reply that leaves that account out |
| P27 checklist on the handles card (R8) | C28 | Covered — rejects a new card |
| P28 checklist items (R8) | C29 | Covered — rejects YouTube, TikTok or Instagram items |
| R9 "you don't need to wait on me" | C22, C28 | Covered by the writes existing |
Unauthorized criteria: none

## Findings
| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |
|---|---|---|---|---|---|---|---|

None open. Every defect found in this check was fixed in 09_Rubrics.json before this report (list above).

## Overlap groups · Spot-check groups · Predicted all-fail
| Group / row | Members / basis | Shared condition / reason |
|---|---|---|
| Overlap groups | none | Same-account rows sit in different deliverables (register C4–C16, reply C24–C27, checklist C29); they share a root cause, not an embedded acceptance condition (playbook set-level rule) |
| Spot-check G1 (actions) | C14 sample; C4–C13, C15, C16 exceptions; volume C3 | ≤ 5 samples; exceptions graded directly |
| Spot-check G2 (holders) | C17, C18; volume C3 | 2 samples |
| Spot-check G3 (money) | C19, C20; volume C3 | 2 samples |
| Spot-check G4 (checklist) | C29 (whole one-member set) | — |
| Spot-check G5 (class) | C21; volume C3 | 1 sample |
| Predicted all-fail | none | Every value is persona-visible (plan visibility proof), every write is cataloged (ledger §C), friction none; baseline run-5 passes all 29 |

## Dimensions
| Dimension | Count / % | Threshold | Status |
|---|---|---|---|
| Overall Rubric Quality | Major 0 · Moderate 0 · Minor 0 of 29 | Major ≤ 10%, Major+Moderate ≤ 15%, all ≤ 20% | PASS (one Major would be 3.4%) |
| Criteria Weights | 29/29 match the plan bands (5 ×8 · 3 ×16 · 1 ×5) | ≥ 15% two-level or ≥ 30% one-level off fails | PASS |
| Category Balance | 29 Outcome | ≥ 1 Outcome | PASS |
| Process Rubrics | 0 Process; no ordering the Outcomes miss | 2+ invalid fails | PASS |
| Agent-Centric Phrasing | 29/29 "The Agent" + verb; no tool name in a title | 1+ artifact subject fails | PASS |
| Negative Criteria | 0 prohibition-only titles (lexical scan: no "not", "no", "never", "without", "avoid") | 1+ fails | PASS |
| Predicted all-fail | 0 | 1+ blocks | PASS |
| Schema and repair gates | schema pass; self-containment, accuracy, atomicity, coverage, duplicates, weights, contradiction all pass | — | PASS |

## Self-review
| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |
|---|---|---|---|---|
| C1 | clear | A run creates the file with gdrive_create_file and parentId | Same parent d_21f9e11d43739eaef26b38 (SQL L129); title names the folder only | none |
| C2 | clear | "money moving Y/N" header worded "Money still moving?" | Title accepts equivalent header wording and any order (rule 6, trello 68dc406c7b0d03e53b334bab) | none |
| C3 | clear | The exclusion list makes the row non-atomic | The claim is the count 13; the exclusions explain where 13 comes from (17 files in d_6cae3483dd469c189a528e minus 4). A 13-row register that swaps an account still fails C4–C16 | none |
| C4 | clear | A valid run writes "Revoke Node's access" instead of REVOKE | Same meaning; the card's verb is the class label, and the title names the account and the action (F9, SQL L13) | none |
| C5 | clear | A run treats the Unity Ads advertiser as a separate account | The sweep has one Unity export with two tabs (f_1191b7f8c96419e1f4dc88); /oe O3 noted this as a prompt question, not a rubric defect | none |
| C6 | clear | Near miss: TRANSFER from the login-only export | Rejected: REVOKE required (notice frederick.stone@harmonygames.co/1843622639043434721) | none |
| C7 | clear | Near miss: TRANSFER because Node was removed in Studio | Rejected (notice frederick.stone@harmonygames.co/1842801580966444617) | none |
| C8 | clear | Near miss: TRANSFER from the personal-gmail login | Rejected (notice frederick.stone@harmonygames.co/1843339075781206004) | none |
| C9 | clear | Near miss: CLOSE (no money) | Rejected (comment 68dc529406d8087e5a6b8403) | none |
| C10 | clear | Near miss: CLOSE under rule 5 | Rejected (frederick.stone@harmonygames.co/1844732985606656293) | none |
| C11 | clear | Valid alternative: KEEP because the Confluence page says don't close | The card replaces the page (SQL L141); CLOSE is the only valid action | none |
| C12 | clear | Near miss: KEEP because the campaign ran Sep 1 | Rejected (C07UCC631A6/1757349668.681539) | none |
| C13 | clear | Near miss: KEEP from $38.70 paid revenue | Rejected (D05S58U4SAK/1759272498.304117; snowflake.json /tables/35 re-summed 38.6967) | none |
| C14 | clear | AppLovin revenue might be under $100 | AD_REVENUE applovin paid 136.33 and the Sep 14 payout (frederick.stone@harmonygames.co/1843223812315546201) → KEEP | none |
| C15 | clear | Near miss: CLOSE (no money) | Rejected (comment 68dc529406d8087e5a6b8403) | none |
| C16 | clear | Near miss: CLOSE | Rejected (same comment) | none |
| C17 | clear | A run lists addresses instead of names | Title accepts names or harmonygames.co addresses (SQL L11) | none |
| C18 | clear | A run adds Fred | "exactly" rejects him (Manager, SQL L35); all six baseline runs excluded him | none |
| C19 | clear | Near miss: N because the FB campaign was turned off Sep 26 | Rejected; $0.05 billed Sep 15 (frederick.stone@harmonygames.co/1843428112007517388) | none |
| C20 | clear | Near miss: N because the warehouse has no Unity cost | Rejected; cash notes go by campaign state (C07C2866011/1759186080.203099) | none |
| C21 | clear | Cascade with C10? | No: C10's KEEP comes from Arthur's email, so class and action vary independently (SQL L19, L21) | none |
| C22 | clear | A run replies by email to Leonard | Rejected; the prompt says "in that DM" (D05S58U4SAK/1759272012.507134); thread or top level both pass | none |
| C23 | clear | A run writes "just X" without a number | Naming one account as the TRANSFER set states the count; "1 (one)" accepted. Judge reads meaning | none |
| C24 | clear | A run says "an agency" without naming Node | The title needs Node Media LLC; the Partners tab names it (SQL L13) | none |
| C25 | clear | A run writes "Unity Ads" | Title says Unity (the Unity Ads advertiser); both names pass | none |
| C26 | clear | A run names the Brand Account but not "YouTube" | The Brand Account is the channel's (notice subject "Review who can manage Harmony Games"); the title names the channel | none |
| C27 | clear | A run says Node manages TikTok via a shared login | Naming Node with TikTok passes; the notice is the source (SQL L192) | none |
| C28 | clear | A run puts the checklist on a new card | Rejected: the title names the existing card 67cf1b506d78ad3c72e02a35 (hg.py get trello /cards/671) | none |
| C29 | clear | A run adds an item per social | Rejected by "exactly one item, naming X" (F33) | none |
| Re-verified values | done | A literal drifted from the record | Every literal re-read this session: SQL rows via base_check.parse_sql (L11–L99, L129, L137, L139, L141, L149, L154, L188, L192, L196); base via hg.py get-many (adjoe, #executives, Gmail receipts) and hg.py get trello /cards/671; AD_REVENUE re-summed | none |
| Upstream chain | open | The rubric-writing plan gate does not PASS | Its only failing check is diversity.authority_share (rules card 98%, sweep folder 90%), a structural design finding recorded in the plan; it is not a /rubric dimension | human acceptance |

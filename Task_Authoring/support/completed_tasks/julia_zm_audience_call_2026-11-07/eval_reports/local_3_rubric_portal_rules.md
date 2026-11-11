## RUBRIC EVALUATION REPORT (portal rules)

### Task: Leonard's audience call on the friend sessions (Register tab, memo, ticket close-out, thread reply, note to Brian)
### Persona: Julia Lawson - Product Manager
### Total Rubrics: 108 (Outcome: 108, Process: 0)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Rules: the portal's rubric-revision-v10 rules (release 95724d0c) as the portal applied them in report 6aeed824…_3_rubric.md (count-bundle-v1, one row per write target, 120-word title cap, Eval 3 §2.7/§2.10 rounding, §3.3 duplicates, QC B11), with local Eval 3 as the base. The local eval package (3d51ac28) is older and lacks these rules, so this run did not use the local score-record writer. The verdict below is this review's own, not a portal verdict.

Mode: AUDIT (all 108 rows). Reviewers: main review plus blind F2 and F3 full reviewers and deep-recheck passes R1–R7, then one fix-check round on every changed row.

## Fix List (all applied to the rubric; each marked after the fix-check round)

1. **R18 casual mean.** Removed "3.83 given with 26 counted casual sessions or 99.5 stars fails". It tied the rounded correct value to R22's count, which made it overly_specific and a cascade group with R22/R24. The 3.8 backer is now "the memo also states". The ZOM-625-dropped 3.83 is recorded as an accepted path (Eval 3 §2.10). (checked, then revised after check: the recording now covers "beside 26 sessions")
2. **R24 gap.** The title now passes "a third of a star" (exact), and the 0.3 backer accepts means of 3.83 or 3.833. Removed the "given with 26 / 3.827" clause. Title and evidence now agree. (checked, then revised after check: recording widened)
3. **R10/R11 late sessions.** The rule for finding the added row moved into the title, and the fallback is tied to Owen Baker's Sep 28 sessions, so rows from Marcus's resent form no longer match. The R11 justification now names Contacts. (checked)
4. **R17 call.** Any wording that makes casual the call passes. A memo that offers casual lead and another call as alternatives fails. (checked)
5. **R21 retention.** The method backer now reads "install weighting over cohorts with a D14 figure". The sheet is named ('ZM KPI snapshot', Vincent's). Evidence now says a figure labelled as a different method is context. The d7-filter path (10.5142%) and the KPI iOS mean (10.6314%) are recorded. 107 words. (checked)
6. **R19.** The evidence records 3.533 (every Fri Sep 26 session dropped) showing as 3.5, which is exact and must pass. (checked)
7. **R22/R23 justifications.** Corrected which drops hit which audience: the coached drops are all RPG, the 1943 drops are all casual, and the ZOM-622/ZOM-598 drops come from Contacts. (checked)
8. **R34–R43, R94, R102 justifications.** The gate doc does not mention 1943. Only Leonard's thread reply does; the gate doc says dev-build sessions do not count. (checked)
9. **R106.** Hold, holding, held or on hold all pass. Removed the reference to another row. (checked)
10. **R108.** Holding the cards earlier change as a whole passes, and a go-ahead for any part fails. (checked)

## Findings (version fb5ad5f9 → fixed in 878972a8)

| Rows | Issue | Severity | Found by | Status |
|---|---|---|---|---|
| R18, R24 | Rounded correct value blocked by a co-stated count | Major overly_specific / non_atomic | R1, R7, F2, F3 | Fixed |
| R18, R22, R24 | One count fails three rows | Moderate overlap | R4, F3 | Fixed |
| R24 | Title 3.833 vs evidence 3.83 | Major not_self_contained | R6, R5, F2, F3 | Fixed |
| R18 | "rounding to it" reads two ways (3.827) | Major not_self_contained | F2, F3 | Fixed |
| R10, R11 | Locator only in evidence; fallback too wide | Major not_self_contained | R6, F2, F3 | Fixed |
| R21 | Sheet identity, backer reading, context carve-out not in title | Major not_self_contained | R6 | Fixed |
| R22, R23 | Wrong drop attribution in justification | Major incorrect | R2, F3 | Fixed |
| 12 dev-build rows | Gate doc credited with naming 1943 | Minor (12 rows = 11%) / Major strict | R2, F3 | Fixed |
| R17 | Pass list closed; two-call memo passes | Minor/Major overly_broad | R5, R6, F3 | Fixed |
| R106 | "held" / "on hold" fail | Minor overly_specific | R1 | Fixed |
| R108 | Two readings of the scope of the work | Minor not_self_contained | R6 | Fixed |
| R19 | 3.533 path not recorded | Minor | R5 | Fixed (recorded) |
| R18, R24 evidence | Pointed at a sibling row | Minor (P13) | R4, F2, F3 | Fixed |

### Rejected
- **Verdict column has 7 rows, over the 5 cap (R4, F3 conditional).** The portal's own report treats Owen's two sessions as "direct (protected) outcomes", so the group has five samples.
- **Drop R21's method backer (R5-DR1).** The portal's finding was that R21 rejected a correct 10.5% stated with Robert's method; its checked fix 9 restored the backer. The d7-filter path is recorded instead.
- **R16 weight.** d_8140f09bf9f1b94cb8ee2d is Julia's root Drive folder, so this is a single-service lookup.

### Confirmed clean
- **Count bundles:** none. R1 (82 rows) is the volume row; R22/R23 are counts the card asks the memo to report.
- **Close-out rows:** 80 rows, one per ticket. 43 Done and 37 Canceled. Every observer, weekday and cited id was verified against the SQL by R2, F2 and F3.
- **Coverage:** complete (R3).
- **Weights:** 103 rows at 5 with "Multi-source:" justifications; 5 single-source rows at 1.
- **Title length:** maximum 107 words.
- **Phrasing:** agent-centric, no tool names, lint 0.

### FINAL VERDICT (this review, portal rules): PASS expected on the fixed version 878972a8
Every confirmed finding is fixed. The fix-check round's two Minor recording gaps are also applied. Not proven: the portal's grader is a different run and may find new edges. Re-upload 09_Rubrics.json and run the portal /rubric.
Reviewed JSON SHA-256 (fixed): 878972a8… · SQL 3a98aa36 · Prompt c3da944d · OE 7f0aa81e (unchanged)

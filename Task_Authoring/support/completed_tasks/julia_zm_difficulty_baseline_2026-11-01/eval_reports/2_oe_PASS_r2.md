## OE EVALUATION REPORT

### Task: Julia takes over Leonard's ZM difficulty baseline: build the two-tab register under the rules on his Trello card, file and share it, comment on the tickets his rules name, and reply to him in their DM
### Persona: Julia Lawson - Product Manager (julia.lawson@harmonygames.co, Product)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Inputs reviewed: the 41 Oracle Events (new upload "08_Oracle_Events (2).md", saved as the current OE input), the exact prompt, the task details and the saved injection SQL (read as an overlay, never executed). Base data comes from Universe_SynthCut. The SQL supplies every Linear comment: the base Linear export has no comments.

What changed since the last /oe: the deck step moved from OE 13 to OE 16 and now cites the right record for each out-of-date part. Blake's note, ZOM-42 and the build became OE 13, 14 and 15. OE 19 now checks all four title-match PRs (243, 244, 265, 271). OE 22 now gives the reason for each row that isn't Live. Facts verified last round on unchanged text were re-checked against the current SQL and base hashes through the bound record.

### Phase 1: Structure & Alignment
- **Derived critical path (built from the prompt, without looking at the OEs):**
  1. Read Leonard's Sep 30 DM ask, its thread reply and his later 21:16 reply in the same DM.
  2. Find the "Difficulty baseline (Julia)" card on ZM ROADMAP. Read rules 1–7, the comment, the checklist and the attached "notes for monday" doc.
  3. Read Blake's "store builds for monday" mail and his reply, the session agenda and the tuning invite.
  4. Find the ZM Difficulty folder. Read the enrage sheet's Live tab, Blake's deck note, ZOM-42, the starting-tier code and Robert's deck.
  5. List the ZOM issues created up to Aug 31 and match titles, including the "attack power" amendment.
  6. Read every closing note to find the "tiers:" tickets, the statuses and the replacements. Check each title match's PR for a "not tiers" review. Apply rule 4 to PR 401. Read ZOM-303.
  7. Compute the 24-row register.
  8. Create the sheet with Tickets and Rules in force tabs. Write both tabs, move the sheet into the folder and share it four ways.
  9. Post the comments rule 6 requires on ZOM-199 and ZOM-254, plus the checklist's 7 Editor only / Not shipped comments.
  10. Reply to Leonard in the DM.
- **Segments:** 41 STEP, 0 CONTEXT, 0 RESPONSE_DESCRIPTION, 0 NON_ACTION.

### Phase 2: Accuracy
| Step | Field | Result | Evidence |
|---|---|---|---|
| OE 1–3 | all | VERIFIED | DM D05HB64NMQU is an IM between Julia and Leonard. The ask (2025-09-30T19:48:26Z = 12:48 PM PDT, reply_count 1), the 20:07 thread reply, Julia's 2025-09-29T21:38 message and the 21:16 reply all match the SQL word for word. |
| OE 4–7 | all | VERIFIED | Card "Difficulty baseline (Julia)" on ZM ROADMAP (created 2025-09-29T18:05:12Z, description edited 2025-09-30T14:04:31Z). It has 1 comment (15:41), the checklist "Before Monday" (16:20) and the attachment linking Leonard's "notes for monday" doc (15:47, shared with Julia). The decoy card sits on the Domino Delights board (created 2025-06-02). The attack power titles are ZOM-246, 250, 263, 277 and 315; ZOM-271 says only "ATK POWER". |
| OE 8–12 | all | VERIFIED | Julia's INBOX copies of Blake's mail (09:12) and reply (13:26). The agenda doc (2025-09-29T18:31). The invite on 2025-10-06 at 17:00 UTC with 5 attendees. The folder, where Julia is writer. Every row of the Live tab, plus the Next pass tab. |
| OE 13 | all | VERIFIED | Blake's #zombie-design note, 2025-09-03T15:22 UTC (Julia is a member): "enrage adds speed and damage only (split since match3d#401), hp doesn't change, and the values are per monster". |
| OE 14 | all | VERIFIED | The ZOM-42 quotes match its description: the tier-2 exception, "UP TO THE MOST RECENT 10 attempts", the 80% promotion rule, "Lose 4 in a row", the 50%-or-lower demotion rule and the reset. |
| OE 15 | all | VERIFIED | TierManager.cs: `if (totalGames == 10)` and `cpm > 90.0f`. WinHistory.cs: `GetTotalWins() + GetTotalLosses()`. |
| OE 16 | expected_data | VERIFIED (fixed) | The deck text matches all three slides. Each out-of-date part now cites the right record: "90 or more" via Blake's reply (cpm > 90, so 90 exactly stays on tier 0); "first 10 levels" via the build (OE 15); the blunder line via Blake's note (OE 13). The rule 5 sentence paraphrases the card's "For which games promotion and demotion look at, write it the way ZOM-42 words it". Following it gives the same Rules in force content. |
| OE 17–18 | all | VERIFIED | Recounted: 31 title matches that are not Duplicates; ZOM-203 and ZOM-276 are Duplicates; ZOM-271 doesn't match. The states are right. Exactly five Linear comments start with "tiers:" (ZOM-221, 281, 300, 305, 378). The quoted closing notes match the SQL. |
| OE 19 | parameters, expected_data | VERIFIED (fixed) | A complete search of the GitHub export for "ZOM-" finds PRs only for title matches ZOM-173 (#243), ZOM-295 (#271), ZOM-303 (#244) and ZOM-312 (#265). A complete review scan (2,230 reviews, 1,387 review comments) plus the SQL gives these results. PR 243: no reviews. PR 244: rev_1 and rev_2, both CodeRabbit ("Actionable comments posted: 1"). PR 271: rev_1, CodeRabbit ("Actionable comments posted: 0"). PR 265: Blake's injected rev_8 (2025-07-03T17:50:12Z, empty body) and rc_7 on LevelSettings.cs, quoted exactly. "not tiers" appears in no other GitHub review or comment. |
| OE 20–21 | all | VERIFIED | Blake's PR 401 comment (2025-08-25T17:02). Rule 4 says a PR that splits numbers is not a replacement. ZOM-303's solution sentence matches. |
| OE 22 | expected_data | VERIFIED | 31 − 12 exclusions + 5 "tiers:" tickets = 24 rows: 16 Live, 4 Editor only, 3 Not shipped and 1 Replaced. The new reasons match the records: ZOM-173 "the set count in the level objects panel"; ZOM-200's title "Need debug menu for dynamic difficulty…" (Blake's mail says the debug menu is stripped); ZOM-277 and ZOM-315 "nothing changes in the game itself"; ZOM-202 "nothing merged yet"; ZOM-280 Canceled; ZOM-293 Todo; ZOM-282 "replaces the blunder 2.0 boost from ZOM-254". |
| OE 23–31 | all | VERIFIED | One sheet with Tickets and Rules in force tabs, as the agenda sets out. The Rules in force content matches ZOM-42, the build, ZOM-303 and the Live tab. Shares: Robert writer, Brian commenter (the 21:16 DM), Leonard commenter, Arthur reader (notes doc). |
| OE 32–40 | all | VERIFIED | ZOM-199's text says `>= 90` and Blake's reply corrects it. ZOM-282's note replaces ZOM-254. Checklist item 1 adds comments on the 4 Editor only and 3 Not shipped tickets. |
| OE 41 | all | VERIFIED | The reply content follows the ask, the thread reply and the notes doc. |

Numeric observability: every count (31, 24, 16/4/3/1) and every enrage value can be read directly through list/read tools.

### Format & Standardization
No shape defects. Every OE is numbered, has one action, names its service, and has an Expected: line. OE 22 is a declared no-tool reasoning step. OE 19 reads one kind of record (reviews) across four PRs, which counts as one action.

### Phase 3: Completeness
| Requirement | Covered by | Result |
|---|---|---|
| DM ask, thread reply, later 21:16 amendment | OE 1–3 | COVERED |
| Rules card (decoy avoided), comment, checklist, notes doc | OE 4–7 | COVERED |
| Store builds mail + reply, agenda, invite, folder | OE 8–11 | COVERED |
| Live tab, Blake's deck note, ZOM-42, starting-tier code, deck | OE 12–16 | COVERED |
| Title-match population; "tiers:" notes; closing notes | OE 17–18 | COVERED |
| "not tiers" exclusion on every title-match PR | OE 19 | COVERED |
| Rule 4 / PR 401; level drop after a demotion | OE 18, 20, 21 | COVERED |
| Register computation | OE 22 | COVERED |
| Sheet + two tabs + contents; folder; four shares | OE 23–31 | COVERED |
| Rule 6 comments; checklist comments | OE 32–40 | COVERED |
| DM reply with everything asked | OE 41 | COVERED |

- **Path feasibility:** SUPPORTED. **Task solvability:** SUPPORTED_BY_OE. **Prompt follow-up:** NONE.
- **Outcome-first mapping:** every step maps to an Outcome check on the register tabs, the sheet's folder and permissions, the ticket comments or the DM reply. No step needs a Process row.

### Issues Found
None. Both issues from the last round are fixed: OE 16 (formerly OE 13) now cites the right records, and OE 19 checks every title-match PR.

### Recommended Fixes
No required fixes.

### Readability (advice only, no score impact)
- OE 24 says "with their Linear titles" but doesn't write them out. The register titles (for example ZOM-221 "Fix monster spawning issues with long gaps in tracks") come from the OE 17 listing. Writing them out in OE 22 or OE 24 would make the rubric rows easier to build. Likewise, OE 17's Expected line could say that the five "tiers:" tickets (ZOM-221, 281, 300, 305, 378) are all Done.
- Two decoys in the data aren't named in any OE. Brian's #zombie-design message says the editor bits ship and gives enrage as "+50% speed and damage for every monster". Vincent asks for the list to be posted in #zombie-design, but he isn't on the invite and the prompt asks only for the DM reply. A clause in OE 8 or OE 12 and in OE 41 would flag them.

## Deep Recheck

Passes: O1, O2, O3, Opus 5.5 (claude-opus-5-5) subagents, each blind to the main review. O3 did not see the OE file.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 41 events | 0 | 0 |
| O2 | 41 events, 7 prompt sentences | 1 | 0 |
| O3 | 4 open instructions, 63 items | 63 inventory items | 63 matched, 0 missing |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | O2 | "then the 24 rows of OE 22 with their Linear titles" (OE 24); "ZOM-221 (Done) … ZOM-378 (Done)" (OE 22) | linear/data.json /issues/3268, 3334, 3355, 3360, 3440: state_id "Done", titles as listed | Expected data not stated | Completeness | REJECTED | Not missing and not wrong. OE 17 lists every ZOM issue created up to Aug 31, paging to the end, so it returns the title and state of all five "tiers:" tickets. All five are Done in the records, so OE 22's "(Done)" values are correct. Unwritten titles are a readability point (Eval 2: "Values not written out" goes to 2.4 and the readability note), and every value the OE does state checks out. |

Effect on verdict: unchanged. No finding was confirmed, so the record saved before the passes stands.

- G1: build the register (rows) | Tickets tab | 24 items (M2–M25) | Covered by: OE 17, 18, 22, 24
- G2: register scope and exclusions (title rule with attack power, "tiers:" notes, DM and notes-doc exclusions, "not tiers", Duplicates, ATK only, Aug 31 cutoff, decoy card) | Tickets tab scope | 9 items (M1, M26–M33) | Covered by: OE 2, 3, 4, 5, 7, 17, 19, 22
- G3: layout and status counts | Tickets tab | 2 items (M34–M35) | Covered by: OE 9, 22, 23, 24, 25
- G4: Rules in force (starting-tier threshold and timing by the build, promotion and demotion in ZOM-42 wording, level drop, enrage model) | Rules in force tab | 6 items (M36–M41) | Covered by: OE 8, 13, 14, 15, 16, 21, 26
- G5: copy the Live tab as it stands | Rules in force tab | 11 items (M42–M52) | Covered by: OE 12, 26
- G6: rule 6 ticket comments | ZOM-199, ZOM-254 | 2 items (M53–M54) | Covered by: OE 32, 33
- G7: checklist rule 6 change | ZOM-173, 200, 277, 315, 202, 280, 293 | 2 items (M55–M56) | Covered by: OE 6, 34–40 (O3 notes that the checklist item is still marked incomplete. OE 6 resolves it with Leonard's 21:16 DM, which withdraws only the rule 7 item. Any doubt about that reading belongs to /prompt.)
- G8: folder and sharing | ZM Difficulty folder, invite | 6 items (M57–M62) | Covered by: OE 10, 11, 27, 28, 29, 30, 31 (M62, Vincent's request, needs no action)
- G9: reply with what he asked for | DM to Leonard | 1 item (M63) | Covered by: OE 41

Scope: "build the register the way he set it up" covers 33 confirmed items (24 rows and 9 scope items). Leonard's card and DMs name the sources exactly. /prompt owns any Feasibility or Clarity judgment on this, and it doesn't affect this score.

Platform defects: none

### FINAL VERDICT: PASS
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Score: 5
Execution status: COMPLETE
Completeness score: 5
Accuracy score: 5
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Review policy: oracle-events-v2
Reviewed OE SHA-256: 2da4c9bee3794a9d496dd024e4c38bc0a5bc115ae134356eb85aa71aff57628f
Review context SHA-256: 49944375055569a60b26ad8b31ffb81d0504b9c41df9dce74b4e5b6f090e734b
OE record SHA-256: a9e532ecc2c48f7289c9030ff9b67a28f27b591f7eb6a915c083694aae727460
Eval version: task-quality-v1
Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Next action: Review complete. The OEs can go forward; next is /rubric
Evidence limits: Static universe, SQL overlay and catalog evidence; no live writes were executed.

## OE EVALUATION REPORT

### Task: Julia takes over Leonard's ZM difficulty baseline: build the two-tab register under the rules on his Trello card, file and share it, comment on the tickets his rules name, and reply to him in their DM
### Persona: Julia Lawson - Product Manager (julia.lawson@harmonygames.co, Product)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Inputs reviewed: the 41 Oracle Events (08_Oracle_Events.md), the exact prompt, the task details and the saved injection SQL (172 INSERTs and 3 UPDATEs, read as an overlay and never executed). Base data comes from Universe_SynthCut. The SQL supplies every Linear comment: the base Linear export has no comments.

### Phase 1: Structure & Alignment
- **Derived critical path (built from the prompt, without looking at the OEs):**
  1. Read Leonard's Sep 30 DM ask, its thread reply and his later 21:16 reply in the same DM.
  2. Find the "Difficulty baseline (Julia)" card on ZM ROADMAP. Read rules 1–7, the comment, the checklist and the attached "notes for monday" doc.
  3. Read Blake's "store builds for monday" mail and his reply, the session agenda and the tuning invite.
  4. Find the ZM Difficulty folder. Read the enrage sheet's Live tab, Robert's deck, ZOM-42 and the starting-tier code.
  5. List the ZOM issues created up to Aug 31 and match titles, including the "attack power" amendment.
  6. Read every closing note to find the "tiers:" tickets, the statuses and the replacements. Check PR reviews for "not tiers". Apply rule 4 to PR 401. Read ZOM-303.
  7. Compute the 24-row register.
  8. Create the sheet with Tickets and Rules in force tabs. Write both tabs, move the sheet into the folder and share it four ways.
  9. Post the comments rule 6 requires on ZOM-199 and ZOM-254, plus the checklist's 7 Editor only / Not shipped comments.
  10. Reply to Leonard in the DM.
- **Segments:** 41 STEP, 0 CONTEXT, 0 RESPONSE_DESCRIPTION, 0 NON_ACTION.

### Phase 2: Accuracy
| Step | Field | Result | Evidence |
|---|---|---|---|
| OE 1–3 | all | VERIFIED | DM D05HB64NMQU is an IM whose members include Julia and Leonard. The ask (2025-09-30T19:48:26Z = 12:48 PM PDT, reply_count 1), the 20:07:18Z thread reply, Julia's 2025-09-29T21:38:52Z message and the 21:16:42Z reply all match the SQL word for word. The DM has no base messages in Sep 2025. |
| OE 4 | all | VERIFIED | Card 68daca58… is on ZM ROADMAP. createCard is 2025-09-29T18:05:12Z and updateCard is 2025-09-30T14:04:31Z. The description matches. The badges show 1 comment, 2 check items and 1 attachment. The decoy card 683dbef4… sits on "DD Product Roadmap" and was created 2025-06-02. |
| OE 5–7 | all | VERIFIED | Comment at 15:41:55Z; addChecklistToCard at 16:20:11Z with both items; the attachment links f_f494073f…, which Leonard created at 15:47:03Z and shared with Julia as reader. The texts match. The attack power titles are ZOM-246, 250, 263, 277 and 315; ZOM-271 says only "ATK POWER". |
| OE 8 | all | VERIFIED | Julia's INBOX copies of the mail at 09:12:44Z (Arthur Blake to Julia, Leonard, Robert and Brian) and the reply at 13:26:05Z. Both bodies match. |
| OE 9–12 | all | VERIFIED | Agenda doc created 2025-09-29T18:31:09Z. Invite at 2025-10-06T17:00Z with 5 attendees. Folder created 2025-06-13, where Julia is writer. Live tab: header plus all 11 rows; the Next pass tab holds Leonard's 0.3/0.8 proposal. |
| OE 13 | expected_data | **MINOR** | The deck text matches. But "(OE 8 reply; OE 14)" is the wrong source for "first 10 levels". Blake's reply covers only `> 90` vs `>= 90`, and his Slack note covers only the blunder line. Only the build (TierManager.cs `if (totalGames == 10)`, read in OE 16) shows the trigger is the 10th game, not level 10. The values are right, so the outcome can't change. |
| OE 14–16 | all | VERIFIED | Blake's #zombie-design note at 2025-09-03T15:22:09Z (Julia is a member). The ZOM-42 quotes match the description. TierManager.cs has `totalGames == 10` and `cpm > 90.0f`; WinHistory.cs has `GetTotalWins() + GetTotalLosses()`. |
| OE 17 | all | VERIFIED | Recounted: 498 ZOM issues were created before 2025-09-01. 31 title matches are not Duplicates; ZOM-203 and ZOM-276 are Duplicates; ZOM-271 doesn't match. The states are right (202 In Progress, 280 Canceled, 293 Todo, the rest Done). |
| OE 18 | all | VERIFIED | All quoted notes match the SQL comment rows, written by usr_cc3e90160f490686 (arthur.blake). Exactly five comments start with "tiers:": ZOM-221, 281, 300, 305 and 378. ZOM-281's assignee is usr_EMPLOYEE_0032. |
| OE 19 | parameters | **MINOR** | Rule 1 drops any title match Blake marked "not tiers" on its PR. OE 18 itself names three more title-match PRs: match3d#243 (ZOM-173), #244 (ZOM-303) and #271 (ZOM-295). OE 19 reads only PR 265. Those three PRs have no "not tiers" review (243 has no reviews; 244 and 271 have only CodeRabbit reviews), so the register doesn't change. |
| OE 19 | expected_data | VERIFIED | Review rev_8 at 2025-07-03T17:50:12Z has an empty body. The inline comment on LevelSettings.cs matches. |
| OE 20–21 | all | VERIFIED | The PR 401 comment by Arthur Blake at 2025-08-25T17:02:28Z. Rule 4 says a PR that splits numbers is not a replacement. The ZOM-303 solution sentence matches. |
| OE 22 | all | VERIFIED | 31 title matches minus 12 excluded = 19, plus 5 "tiers:" tickets = 24. That is 16 Live, 4 Editor only, 3 Not shipped and 1 Replaced (ZOM-254 by ZOM-282). ZOM-200 is Editor only because it is the debug menu, which Blake's mail says is stripped. ZOM-263 is Live because the ricochet fix is in runtime code (EffectsData.cs). |
| OE 23–31 | all | VERIFIED | One sheet with Tickets and Rules in force tabs, as the agenda sets out. The Rules in force content matches ZOM-42, the build (WinRateRule.cs: the 50% / 10-game rule and the 4-loss rule), ZOM-303 and the Live tab. Shares: Robert writer (rule 7), Brian commenter (the 21:16 DM), Leonard commenter, Arthur reader (notes doc). |
| OE 32–40 | all | VERIFIED | ZOM-199's text says `>= 90` and Blake's reply corrects it. ZOM-282's note replaces ZOM-254. Checklist item 1 adds comments on the Editor only tickets (173, 200, 277, 315) and the Not shipped tickets (202, 280, 293). |
| OE 41 | all | VERIFIED | The reply content follows the ask (folder, count, counts per status, starting-tier timing), the thread (Not shipped and Editor only keys) and the notes doc (which ticket replaced which). |

Numeric observability: every count (31, 24, 16/4/3/1) and every enrage value is directly visible through list/read tools. No step promises precision a tool can't show.

### Format & Standardization
No shape defects. Every OE is numbered, has one action, names its service, and has an Expected: line. OE 22 is a declared no-tool reasoning step, which is allowed.

### Phase 3: Completeness
| Requirement | Covered by | Result |
|---|---|---|
| DM ask, thread reply, later 21:16 amendment | OE 1–3 | COVERED |
| Rules card (decoy avoided), comment, checklist, notes doc | OE 4–7 | COVERED |
| Store builds mail + reply, agenda, invite, folder | OE 8–11 | COVERED |
| Live tab, deck, Blake's deck note, ZOM-42, starting-tier code | OE 12–16 | COVERED |
| Title-match population; "tiers:" notes; closing notes | OE 17–18 | COVERED |
| "not tiers" exclusion | OE 19 | COVERED (scope too narrow; MINOR on OE 19) |
| Rule 4 / PR 401; level drop after a demotion | OE 18, 20, 21 | COVERED |
| Register computation | OE 22 | COVERED |
| Sheet + two tabs + contents; folder; four shares | OE 23–31 | COVERED |
| Rule 6 comments; checklist comments | OE 32–40 | COVERED |
| DM reply with everything asked | OE 41 | COVERED |

- **Path feasibility:** SUPPORTED. **Task solvability:** SUPPORTED_BY_OE. **Prompt follow-up:** NONE.
- **Outcome-first mapping:** every step maps to an Outcome check on the register tabs, the sheet's folder and permissions, the ticket comments or the DM reply. No step needs a Process row.

### Issues Found
| # | Step | Issue | Component | Effect |
|---|---|---|---|---|
| 1 | OE 13 | The Expected line cites "(OE 8 reply; OE 14)" for why "first 10 levels" is out of date. Neither record shows that; only the build (OE 16) does. | Accuracy | MINOR (NON-FAIL 3) |
| 2 | OE 19 | It checks only PR 265 for a "not tiers" review. Rule 1 covers every title match's PR, and PRs 243, 244 and 271 (named in OE 18) go unchecked. | Accuracy | MINOR (NON-FAIL 3) |

### Recommended Fixes
1. **OE 13:** replace the last sentence of its Expected line with:
   "Out of date in the deck: "90 or more", because Blake's reply (OE 8) says the build checks cpm > 90, so 90 exactly stays on tier 0; "first 10 levels", because the build (OE 16) sets the tier when the player's 10th game ends, wins and losses both counting; and the blunder line, because Blake's #zombie-design note (OE 14) says enrage adds speed and damage only, hp doesn't change, and the values are per monster."
2. **OE 19:** replace it with:
   "OE 19  Check every title match's PR for a "not tiers" review, since rule 1 drops a title match Blake marked "not tiers" on its PR. Only four title matches have a PR in match3d, and their closing notes (OE 18) name them: 243 (ZOM-173), 244 (ZOM-303), 265 (ZOM-312) and 271 (ZOM-295) (GitHub: reviews and review comments on each PR).
   Expected: Only PR 265 has one. Blake's review of Thu Jul 3 2025 17:50 UTC has an empty body, and its inline comment on Assets/Scripts/LevelEditor/UI/LevelSettings.cs says "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work". PR 243 has no reviews, and PRs 244 and 271 have only automated CodeRabbit reviews. So ZOM-312 stays off the register, and ZOM-173, ZOM-295 and ZOM-303 stay on."

### Readability (advice only, no score impact)
- The set already reads goal-first with values written out. Two traps in the data aren't named in any OE. Naming them would make the rubric easier to build:
  - Brian's #zombie-design message of 2025-09-29 claims "the editor bits too" are in the store builds and that enrage is "+50% speed and damage for every monster". Blake's mail and the Live tab both contradict it.
  - Vincent's 2025-09-30 request to post the list in #zombie-design. The prompt asks only for the DM reply.
  A clause in OE 8 and OE 41 would cover them.
- OE 22 could give one reason per non-Live status, for example "ZOM-200 Editor only: debug menu". This one is a suggestion, not a required fix.

## Deep Recheck

Passes: O1, O2, O3, Opus 5.5 (claude-opus-5-5) subagents, each blind to the main review. O3 did not see the OE file.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 41 events | 1 | 1 |
| O2 | 41 events, 7 prompt sentences | 3 | 1 |
| O3 | 4 open instructions, 78 items | 78 inventory items | 78 matched, 0 missing |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | O1 | "are out of date (OE 8 reply; OE 14)" (OE 13) | Blake's reply: "cpm > 90, not >= 90"; SQL slack 6995ba10…: "speed and damage only"; TierManager.cs `if (totalGames == 10)` | Qualifiers / attribution | Minor OE inaccuracy | CONFIRMED | Neither cited record shows "first 10 levels" is wrong; only the build does. The values are correct and the outcome can't change. Recorded MINOR on OE 13 expected_data. |
| DR2 | O2 | "or name the PR it merged with (ZOM-295 match3d#271, ZOM-303 match3d#244)" (OE 18) → "ZOM-295 (Done) Live … ZOM-303 (Done) Live" (OE 22) | github pull_request_comments on #271/#244: debug files alongside runtime files (MonsterSpawner.cs, TierManager.cs) | Missing retrieval | Completeness | REJECTED | Live is correct, and it can be reached another valid way. The ticket text (ZOM-295's title; ZOM-303's description, read in OE 21) shows player-facing behavior, and Blake's mail says everything difficulty related was merged before the Sep 26 cut. Reading the PR file lists is one route, not a missing critical step. Even those file lists show runtime changes. |
| DR3 | O2 | "Read Blake's review on pull request 265 … that ZOM-312's note names" (OE 19) | Card rule 1: "a title match Blake marked 'not tiers' in his review on its PR stays off"; #243 has no reviews; #244 and #271 have only CodeRabbit reviews | Exclusion check | Minor OE inaccuracy | CONFIRMED | The step exists but its scope is narrower than rule 1. The skipped PRs hold no "not tiers", so the register doesn't change. Recorded MINOR on OE 19 parameters, not as a missing step. |
| DR4 | O2 | "Demotion: 4 losses in a row, or a win rate of 50% or lower over up to the last 10 games" (OE 26) vs the deck line in OE 13 | ZOM-42: "we demote someone when their win rate for up to the last 10 games is 50% or lower"; WinRateRule.cs agrees | Dependency | Completeness | REJECTED | Rule 5 names the deck and ZOM-42 as the tier write-ups and sends the Agent to the build only for starting-tier timing. ZOM-42 (OE 15) states both demotion triggers; the deck gives a subset and doesn't contradict it. No extra step is needed. |

Effect on verdict: Accuracy drops to the NON-FAIL band because of DR1 and DR3. Completeness is unchanged.

- G1: build the register (rows) | register Tickets tab | 24 items (M1–M24) | Covered by: OE 17, 18, 22, 24
- G2: build the register (exclusions: Duplicates, DM/notes exclusions, "not tiers", date cutoff, ATK) | register scope | 16 items (M25–M40) | Covered by: OE 2, 3, 5, 7, 17, 19, 22
- G3: rule 6 ticket comments | ZOM-199, ZOM-254 | 2 items (M41–M42) | Covered by: OE 32, 33
- G4: checklist rule 6 change | Editor only and Not shipped tickets | 7 items (M43–M49) | Covered by: OE 34–40 (O3 marks whether the checklist item applies as a reading question; OE 6 resolves it with Leonard's 21:16 DM. Any doubt about that reading belongs to /prompt.)
- G5: Rules in force (go by the build for starting-tier timing, ZOM-42 wording for windows) | Rules in force tab | 8 items (M50–M57) | Covered by: OE 13–16, 21, 26
- G6: copy the Live tab as it stands | enrage sheet Live tab | 11 items (M58–M68) | Covered by: OE 12, 26
- G7: folder and sharing | ZM Difficulty folder, invite | 5 items (M69–M73) | Covered by: OE 11, 23, 27–31
- G8: reply with what he asked for | DM to Leonard | 5 items (M74–M78) | Covered by: OE 41

Scope: the "build the register the way he set it up" instruction covers 40 confirmed items (24 rows and 16 exclusions). Leonard's card and DMs name the sources exactly. /prompt owns any Feasibility or Clarity judgment on this, and it doesn't affect this score.

Platform defects: none

### FINAL VERDICT: NON-FAIL
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Score: 3
Execution status: COMPLETE
Completeness score: 5
Accuracy score: 3
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Review policy: oracle-events-v2
Reviewed OE SHA-256: f6c72ea72bcbd81335338124f7c5a51cfae77a2d3f4b4dfdedda7f8bf44ee13c
Review context SHA-256: e4a5c0cac01b7ef83f674ad803775944309689ff652c5851ba78ebd53e77b25b
OE record SHA-256: d8cc45365887a83f1df29062c1374b6229d683ed8593769a903c2ff802805526
Eval version: task-quality-v1
Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Next action: Apply the two fixes to OE 13 and OE 19, then send /oe again (/oe needs a PASS)
Evidence limits: Static universe, SQL overlay and catalog evidence; no live writes executed. The deep recheck passes started before the record's first save; they were given no record or findings either way.

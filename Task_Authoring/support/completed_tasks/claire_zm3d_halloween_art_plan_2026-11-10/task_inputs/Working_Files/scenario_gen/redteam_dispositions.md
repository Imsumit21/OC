Independent review: `redteam` subagent (GPT-6.1 Sol), static adversarial pass over `planned_texts.json`,
`roster_final.json`, the draft manifest and the gradable surface, 2026-11-04. Round 1: FAIL with 8 findings. Round 2 (re-check of the fixes): RT3–RT8 adequate, RT1 and RT2 still FAIL (text
selectors pass one comment for 46 and cannot read both Docs write paths). Round 3: the rubric hand-off accepted for
the scenario stage; four slot titles claimed more than their selectors (RT9–RT12). Round 4: two selector edge
cases (RT13, RT14); no other failure in the call-field, exact-key or delivery predicates. Round 5: the round-4
regressions confirmed fixed; one length cap (RT15) removed. Each finding is dispositioned here with the
round-2 resolution; the artifacts were regenerated (`finalize_roster.py`, `build_design.py`).

| # | Severity | Finding | Disposition | Evidence after the fix |
| --- | --- | --- | --- | --- |
| RT1 | BLOCKER | the surface did not check the follow-through that carries the volume; round 2: a single comment passed the coverage slots and a description mentioning Martin passed the assignment slot | fixed by scope: every slot whose selector could pass wrong work was removed from the surface (S19, S20, S27); the surface keeps only deterministic checks (S04 iPad ticket, S26 icon ticket with the Oct 16 cut); per-ticket coverage and the issue-to-owner mapping are rubric-only facts RO1–RO3 (46 comments; exactly 38 assignments, 32 Marcus / 6 Martin; Reuse and Skip unassigned) handed to /create-rubric-writing | scenario_gen/rubric_only_facts.json; ART-793 … ART-842 |
| RT2 | BLOCKER | plan text read through one Docs tool only; round 2: switching to the create call reversed the defect | fixed by scope: the plan-text slots (S02, S12, S13) left the surface; the facts are rubric-only RO4–RO6 graded on the doc's final text whichever write path a run uses; R_PACK_ALIAS keeps weight 5 in the rubric by kind of work (the advisory DECISION_FLIP flag on it is dispositioned in section 12) | scenario_gen/rubric_only_facts.json |
| RT3 | MAJOR | "note each ad's call" let a run fold the note and the assignment into one issue update, and Skip ads need no comment read, so the floor could fall below 130 | fixed: the ask now says "drop a comment on each ad's ART ticket with its call and due date" and assignments stay a separate field; the budget counts only the 38 reads that decide a call (the 6 Skip and 2 Reuse reads are conditional): unconditional floor 173 (round 2: a minimal complete honest route is about 132 calls before sharing, discovery, tracker population or verification, so >130 survives) | ask C06DJBJL798/1759269913.882683 (planned_texts.json); 01_Hardness_Manifest.draft.json call_budget |
| RT4 | MAJOR | "Reuse: ready" mixed production status with the Oct 15 hand-off deadline; Play upload had no unique date | fixed: Reuse ads are due with Frederick by Wed Oct 15 (status "made" kept separately); the iPhone set is due with the Oct 16 12:00 PT cut; the Play set has no graded date; the calendar now says new iOS screenshots are due by the same cut | roster_final.json due/status; doc text f_fdd6d2d2f4a4d2f5b908fb (planned_texts.json doc_release) |
| RT5 | MAJOR | ART-841 (boris alin2) had a "checked Sep 9" comment before its Sep 12 ticket | fixed: the note moved to ART-812 (mrfluffernot portrait, live since Dec 2024); finalize_roster.py now asserts every second comment is later than its ticket | ART-841, ART-812, cmt_art812_2 |
| RT6 | MAJOR | the due date inside ticket comments was not asked for | fixed: the ask requests the call and the due date in the comment | ask C06DJBJL798/1759269913.882683 |
| RT7 | MINOR | the worker's roster_notes.md and per-surface notes still described the first-pass answer key | fixed: roster_notes.md carries a superseded banner; per-surface notes are regenerated from the final fields; store sets cite the Sep 3 export | roster_final.json notes; C06DJBJL798/1756914854.743319 |
| RT8 | MINOR | trap count is not difficulty; several distractors are low-yield and T2/T16 overlap | accepted: T10–T16 are the ≥ 6-distractor coverage floor, not load-bearing; the load-bearing channels are the seven portfolio rules; the forecast is UNCALIBRATED and the difficulty claim is open until the baseline | research/01_forecast_design.json |
| RT9 | MAJOR (round 3) | S04 / S26 passed an unrelated "Fix iPad icon crash" ticket | fixed: both now require "halloween" next to "ipad" / "icon"; S26 is a weight-1 naming check, and the icon ticket's cut date moved to rubric-only RO8 | 01_Gradable_Surface.json S04, S26; rubric_only_facts.json RO8 |
| RT10 | MAJOR (round 3) | S01 / S07 matched a date anywhere in the due cell ("Not Oct 15; due Oct 17") and missed "16 October" | fixed: the due cell must start with the date (optional weekday), day-first forms are accepted, Oct 1–5 never pass; the slot titles now claim only the date window, and the 12:00 PT time of day is rubric-only (RO8) | 01_Gradable_Surface.json S01, S07 |
| RT11 | MAJOR (round 3) | D01 passed "On it." as link delivery | fixed by narrowing: D01 claims only "a reply is posted in Leonard's thread"; D02 is now the `link` selector (the decoded tracker's own id in a Slack message, with the tracker shared); the plan-doc link is rubric-only RO7 | 01_Gradable_Surface.json D01, D02 |
| RT12 | MAJOR (round 3) | D02 share_reader bound to the tracker and the reader role, not the plan or comment access | fixed: share_reader removed; sharing both artifacts with comment access is rubric-only RO7 | rubric_only_facts.json RO7 |
| RT13 | MAJOR (round 4) | S04 / S26 matched "ipad" in one ticket and "halloween" in another across the concatenated text | fixed: `[^\n]` between the words keeps the match inside one string (each title and description is its own newline-joined string); titles now say "one new-ticket field" | 01_Gradable_Surface.json S04, S26 |
| RT15 | MINOR (round 5) | S04 / S26 capped the same-line distance (120 / 200 characters) and missed long single-line descriptions | fixed: uncapped `[^\n]*`; the newline boundary still blocks cross-ticket matches | 01_Gradable_Surface.json S04, S26 |
| RT14 | MINOR (round 4) | S01 / S07 rejected ordinal dates ("Oct 16th", "Oct 15th") | fixed: ordinals and "16th of October" accepted; "Not Oct 15; due Oct 17", "Oct 1" and "Oct 24" still fail | 01_Gradable_Surface.json S01, S07 |

Not demonstrated as forks by the reviewer (kept): Android #1450 vs #1452, the iOS Internal #1452 collision,
newest-capture vs Marcus's Halloween cuts, Skip vs Refresh, cheer fastcouch 16:9 campaigns, the two balloons cuts,
Julia's statics with explicit June sources, and the owner split. The freeze (2025-10-01T00:00Z seed bound) and the
07:00Z eval clock differ by policy (`00_Task_Context.json` freeze_basis), not by error.

### Revision 02 (2026-11-04, at /create-injection; requester D2': over 180 tool calls in every run)

Changes, all generated (`finalize_roster.py`, `build_design.py`): twelve more serving exports ticketed after Sep 12
(ART-843 … ART-850 in a Sep 15 catch-up batch for placements live since the Sep 9 tablet / feed launch; ART-851 …
ART-854 cut from the September re-captures and ticketed the day they went live), so the cohort is 62 surfaces (16
Halloween version, 34 Refresh first, 4 Reuse, 8 Skip) and 58 ad tickets; 48 decisive comment reads + 58 comments + 48
assignments; unconditional floor 205, `call_budget_floor` 181. New trap T19 (cheer fastcouch 4:5 is not covered by
Marcus's "both 9:16 and 16:9"; slot S28, weight 5) and slot S29 (a still that runs only on Android US tablet is skipped).
S01 and S07 left the surface: `reason_matches` has no solver value (`oracle_kit.py check_slots`) and a due window needs a
date comparison the comparators lack; the due facts are rubric-only RO9 and RO10 (weight 5). Re-checked by the
independent red team below.

| # | Severity | Finding (revision 02 review) | Disposition | Evidence after the fix |
| --- | --- | --- | --- | --- |
| RT16 | MAJOR | the claimed 205-call floor was a planned route; a catalog-supported complete route reached exactly 180 (one full-grid sheet read, batched mail, the doc created with its body, Reuse settled from the UA masters folder, Skip settled from the sheet's campaign column) | fixed (revision 02b): the sheet no longer carries campaigns; each ad's Unity campaigns are only in its ticket's comments (Frederick's catalogue note, or his upload note on the four re-exports), so every one of the 58 comment reads decides a call, Skip and Reuse included; the call budget's unconditional rows are now the shortest complete route (one sheet batch read, one mail read, the doc created with its body, no read-backs) and everything else is conditional: unconditional floor 192 > 181 | 01_Hardness_Manifest.draft.json call_budget; planned_texts.json sheet_live Read me / Unity; roster_final.json comment_1 ("Unity: ...") |
| RT17 | MINOR | stale current-count prose (floor 151 in section 0, "6 Skip" in the shortcut audit) | fixed: both computed from the manifest and the roster | 01_Scenario_Design.md sections 0 and 2 |

Not demonstrated (kept): no answer-key fork among ART-843 … ART-854 (cheer fastcouch 4:5 is not covered by "both 9:16 and 16:9"; boris alin2 16:9 names Android #1427; balloons alpha 50 (1) 16:9 also serves iOS UK tablet; the tablet-only still is Skip); no chronology inversion. Padding risk judged unproven: each added export is a separately serving placement with its own campaign and source note, three change their parent's call, and every one is a graded per-ticket write (RO1, RO3).

### Revision 03 (2026-11-04, at /create-prompt-writing: two universe-rooted forks found while writing the brief)

| # | Severity | Finding | Disposition | Evidence after the fix |
| --- | --- | --- | --- | --- |
| PW1 | MAJOR (UGT fork) | Martin's base Sep 17 post "*Halloween theme* for an app icon or an event" (AppIconHalloween.png, no replies) supports reading the app icon as already made (Reuse, no icon ticket) against the design's Halloween version | fixed: Robert's thread reply, Sep 17 16:52Z, "Nice for an event, but not for the app icon, it gets too busy at that size. A Halloween icon should stay as simple as the one we have"; the base parent's reply counters are bumped by one UPDATE | C08R8CHB0QL/1758127951.679146; UPDATE on 9025d428af1f551a20e303c3acbc545b; trap T13 seeded_ids |
| PW2 | MODERATE (scope fork) | the portrait end card ART-831 is off the sheet and only its description says it plays after every Android US phone video, against Leonard's "the live creatives sheet is what's running" | fixed: Frederick's Sep 29 note on ART-831 "Still running on Unity: Android US phone (checked Sep 29). Not on the live creatives sheet yet." | cmt_art831_2; trap T6 seeded_ids |

Both fixes settle a fork with a dated, persona-visible record from the rule's owner (the art director; the sheet's owner); neither names a call, a date or a count.

| # | Severity | Finding (GPT /prompt emulation, main pass, open item ART-809) | Disposition | Evidence after the fix |
| --- | --- | --- | --- | --- |
| PW3 | MAJOR (UGT fork, S16 weight 5) | the base Aug 13 thread `C06DJBJL798/1755114007.441789` that ART-809's note points to says the 30 s cut's music is baked in, but Marcus posts no-music exports in the same thread (InvestorFacing_Seq3_NoMusic.zip, 21:00Z), so "the re-export is already done → Halloween version" was defensible against the deck's "re-exported from the project first" | fixed: the deck's rule now reads "A video whose master has the music baked in is re-cut first from a master without music (re-export one from the project if there is none)" and the Refresh first definition "re-capture, re-render or re-cut before any seasonal pass"; the serving 9:16 is still the music-baked VEED cut (Leonard in the thread: "start with this video and we'll do others without music"), so it is re-cut first whether or not a no-music master exists | deck `f_5ebf55ad29e815d46243c8` slides 2 and 4; solver truth unchanged |

| PW4 | MAJOR (Cross-Service Coherence, GPT /prompt main pass round 2) | base ART-792 (Team Epic, on the store-screenshot path) carries time_in_status_minutes 246277, above its 51,123-minute lifetime at the clock (SC-22) | fixed: one overlay UPDATE sets it NULL like ART-774 / ART-790; updated_at untouched; confirmed by the reviewer (round 3 PASS) | SQL L165 (sha256 29bc98c6e28b); `Working_Files/prompt_eval/1_prompt_redteam.md` |

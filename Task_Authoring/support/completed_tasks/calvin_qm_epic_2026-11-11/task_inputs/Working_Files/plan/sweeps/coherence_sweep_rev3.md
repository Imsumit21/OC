# Blind coherence sweep, rev3

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Scope: `Task_Authoring/task_inputs/01_Universe_Inject.sql` (all 285 lines) against base data read only through `hg.py search`. Nothing was executed or edited. Line numbers below are SQL line numbers.

Verdict: 1 BLOCKING, 5 MAJOR, 9 MINOR. The timeline itself is clean: no build is tested before it exists, no ticket is mentioned before it is created, no reply precedes its parent, and nothing is dated after 2025-09-30T22:07:44Z except the Oct 2 calendar event.

## Base facts used

Build posts in #builds (C05433XK267, `messages/C05433XK267/2025-09.json`), UTC:

| Build | Branch | Posted | Note |
|---|---|---|---|
| iOS Internal #1698 | Calvin's QueueManager branch | 09-24 18:07 | /854 |
| Android #1974 | main | 09-24 23:13 | /902 |
| iOS Internal #1713 | main | 09-25 11:27 | /913 |
| iOS Internal #1718 | QueueManager branch | 09-25 | /926, the build named in the "ok" chat |
| iOS Internal #1727 | main | 09-25 22:21 | merge of #465, /959 |
| Android #1984 | main | 09-25 22:21 | /960 |
| Android Submission #129 | main | 09-26 02:39 | /972 |
| Android #2006 | main | 09-29 15:39 | /1053 |
| iOS Internal #1745 | main | 09-29 16:19 | /1058 |
| iOS Internal #1746 | AnimatedIcons branch | 09-29 19:24 | /1068 |
| Android #2010 | main | 09-29 19:26 | /1069 |
| Android #2013 | main | 09-29 23:34 | /1075 |
| iOS Internal #1750 | main | 09-30 01:55 | /1084 |
| iOS Internal #1752 | main | 09-30 15:50 | merge of #473, /1101 |
| iOS Internal #1754 | main | 09-30 16:01 | merge of #472, /1107 |
| Android #2023 | main | 09-30 16:03 | lists commit "Implement Win&Collect into Queue Manager", /1109 |
| iOS Internal #1756 | main | 09-30 16:14 | merge of #475, /1115 |
| Android #2025 | main | 09-30 16:16 | lists #475 commits "Adding card pack animation", "Fix not allowing multiple tap during card animation", /1116 |
| iOS Internal #1757 | main | 09-30 18:43 | /1119 |
| Android Submission #135 | main | started 18:45, done 09-30 20:13 | /1122, /1124 |

Pull requests (github `data.json`):

| PR | Author | Opened | Approved | Merged | Shape |
|---|---|---|---|---|---|
| #465 | Calvin | 09-25 18:35:53 | | 09-25 22:15:51 | 3 files |
| #472 | Calvin | 09-29 22:36:36 | Arthur 09-30 15:52:58 | 09-30 15:53:04 | 1 commit, 3 files, +36/-21 |
| #473 | Oliver | 09-30 15:41:05 | none | 09-30 15:41:20 (self-merge) | 2 commits, 34 files |
| #475 | Calvin | 09-30 15:59:05 | Arthur 09-30 16:09:09 | 09-30 16:09:15 | 4 commits, 2 files, +6663/-1135 |

Linear: ZOM-566 is the last base ticket (created 09-30 16:26:02). ZOM-543 is "Queue Manager", In Progress, assignee Calvin, creator Brian, no base comments. ZOM-556 and ZOM-560 are both Todo and both created by Vincent on 09-22. All six Linear user ids in the SQL exist and are ZOM team members: `usr_fc22…` Brian, `usr_65c7…` Vincent, `usr_49b9…` Calvin, `usr_bdf0…` Oliver, `usr_4e13…` Owen, `usr_caaf…` Samuel.

## BLOCKING

### B1. PR #475 body now claims a fix the PR cannot contain (line 170)

The UPDATE adds "Fix level stars flying to the wrong corner on tablets" to #475. Everything else on the PR says it is a card-pack change only:

- Title "[PERSON_NAME_0029]/animated icons", head branch AnimatedIcons, 2 changed files.
- The CodeRabbit summary kept in the same body lists only card-pack prompts and the close sequence.
- The base CodeRabbit walkthrough (Slack C093LEZGF6J /623) names one code file, `CardPackOpenScreen.cs`.
- The base #builds post for Android #2025 lists the PR's commits as "Adding card pack animation" and "Fix not allowing multiple tap during card animation".
- The injected review comment sits on `CardPackOpenScreen.cs` (line 169).

Level stars flying to the star counter is level-end reward VFX on the home screen, not the card-pack screen. In base, Calvin's PR body lines are his commit messages (#465, #472, #475 all follow this), so the new line reads as a commit that the build post shows does not exist. This body line is the only record that decides the status of row 8 / ZOM-569, so the contradiction lands on a graded fact.

Smallest fix: remove the #475 body UPDATE and carry the stars fix on a record where it fits. Two options:

- Put the line in #472's body. `RewardVFXManager.cs` is the reward-flight code, and #472 already takes the other hidden fix.
- Tie it to the base commit "fixed end reward path on main screen [Samuel Turner]", which is already in main in Android #2023 (/1109), for example through a short comment by Samuel on ZOM-569.

## MAJOR

### M1. Oliver's #473 comment refers to a list he cannot see and tickets that do not exist yet (lines 172, 82)

At 09-30 15:42:10 Oliver writes "For the flow list, this also has four fixes" and names four reports: rows 13, 38, 14 and 37.

- The sheet (lines 8, 28) is shared only with Brian, Calvin, Leonard and Arthur. Oliver is not on it and is not on the review invite.
- Three of the four have tickets, all filed after his comment: ZOM-572 at 17:13, ZOM-573 at 17:18, ZOM-584 at 18:44. Row 38 has no ticket at all.
- No injected or base record tells Oliver about these reports.

Smallest fix: add `oliver.brooks@harmonygames.co` as reader on the sheet in lines 8 and 28. Brian's "everyone on the review invite" ask is about the new sheet, so it is unaffected.

### M2. "The ticket keys are in it where I opened one" is false for two rows (lines 68, 21, 30)

Vincent's DM and his legend ("Ticket: the Linear key if I filed one") both say the Ticket column holds every ticket he filed. Rows 11 and 20 have a blank Ticket cell, yet their tickets ZOM-556 and ZOM-560 were created by Vincent himself (base creator `usr_65c76e0b87aa7e9b`). He also comments on both during the pass (lines 219, 221). A reviewer will read this as the sheet contradicting its own legend.

Smallest fix: narrow both sentences to the pass.

- Legend: "Ticket: the Linear key if I opened a new one in this pass."
- DM: "the keys of the tickets I opened for it are in there".

### M3. "That is Julia's point about your tickets" has no source (line 217)

Brian's note cites a point by Julia about priority and assignee on Calvin's tickets. I found no such record. Searched: the Brian–Calvin DM for 2025-07 to 09, the zombie channels for September, and the Linear text fields for "your tickets". The only base record on that subject is Calvin's own complaint to Brian on 09-02 (D0770ET6WBW /11: "my major complain about tickets … better understanding and priority for assigned tickets"). This was a targeted search, not proof of absence across the whole export.

Smallest fix: drop the clause ("No priority and no assignee on the new ones, I will set them"), or point it at the real record ("that is your own point from earlier this month").

### M4. Row 25 does not describe the bug the "ok, chat" refers to (line 30)

Row 25 reads "Boss arena tutorial does not play when another tutorial is queued before it", Fix #465, Re-test "ok, chat". The base chat says the opposite symptom:

- D06UPGF5PQV /150, 09-25 13:45: "the boss arena tutorial plays again even if I completed it and it spawns after finishing the event".
- /170, 09-25 17:15: "Boss arena as well" (the ok).

The #465 summary also says "reducing stuck or repeated tutorials". Rows 1, 2 and 5 match their chat lines well; row 25 is the odd one.

Smallest fix: reword row 25 to "Boss arena tutorial plays again after the event even when it was completed".

### M5. PR #472 body gains a second fix line with no commit behind it (line 165)

The added line "Fix pre-level panel opening while the level-end coins are still flying" fits the subject of the PR (`RewardVFXManager.cs`; summary bullet "Prevents premature progression during reward animations"). But #472 has exactly one commit, and Android #2023 lists that commit as "Implement Win&Collect into Queue Manager". By Calvin's base convention a body line is a commit message. There is also no trace of when the body changed: `updated_at` is set to Arthur's comment time, 15:53:40.

The content is plausible, so this is weaker than B1, but it is the same pattern on the other graded hidden fix (row 6 / ZOM-568).

Smallest fix: phrase it as part of the one commit rather than a new commit-style line, for example "Implement Win&Collect into Queue Manager (also stops the pre-level panel opening while the level-end coins are still flying)".

## MINOR

1. **Review ids run backwards (lines 157, 159).** The injected #472 review email has id `review/3285698310`, lower than the base approval that came 42 s earlier (`review/3285702920`). Same on #475: injected `3285755391` against base approval `3285759222`. Fix: use ids above the base approvals, for example 3285705xxx and 3285762xxx.
2. **iPad on an Android build (line 229).** ZOM-569 is "Seen on Android Submission 129", and Vincent's comment says "Tab S7 and the old iPad both". Fix: "Tab S7 and the Tab A8 both".
3. **"Saw this one myself" on his own ticket (line 219).** Vincent created ZOM-556. Fix: "Saw this again in my home screen pass on 1727…".
4. **Mailboxes that do not exist in base (lines 140–155).** Base Gmail has no thread files for Julia or Arthur (0 each; Brian 297, Calvin 8142, Leonard 15339). The four invite emails create two mailboxes holding only these two mails each. Fix: drop the Julia and Arthur gmail rows; the gcal rows already carry the attendee list.
5. **Invite body format.** Base Calendar invites carry a "Join by phone … PIN" block after the Meet link; the injected ones omit it.
6. **Staged regularity.**
   - All 20 tickets are filed in one 2 h 10 min burst, and every one gets a Vincent comment 1–4 minutes after creation.
   - Arthur's two review comments land 36 s and 35 s after his own approve-and-merge.
   - Calvin never answers in any of the three DMs across four days.
   Fix: drop or delay a few self-comments, and move one Arthur comment a few minutes later.
7. **Samuel diagnosing code (line 253).** Samuel is a Game Designer in contacts, though he does commit UI fixes. "Looks like the counter runs twice when the queue plays, checking" reads like an engineer. Acceptable; Owen or Oliver would be a safer assignee.
8. **Pre-pass rows.** Rows 1, 2, 5 and 25 were found and okayed on 09-24/25, before the pass and the sheet started on 09-26 (lines 8, 66). Reads as back-fill; harmless.
9. **Review agenda card on a roadmap board (line 92).** A meeting-agenda card in the Backlog list of ZM ROADMAP, next to feature cards ("PvP Event", "Fake PvE Coop"), is unusual but plausible for Leonard.

## Checked and consistent

- **Sheet against tickets.** All 20 ticket titles and "Seen on" builds match their sheet rows exactly. ZOM-567 to 586 are created in number order, 16:43:18 to 18:53:41, all after ZOM-566. Every `updated_at` equals the last comment time. No ticket is closed, so no comment follows a close. The five In Validation tickets (571, 574, 576, 581, 585) are the five that carry a Fix PR. In Validation exists as a state in base.
- **Re-test builds.** Every "ok / nr / again" build exists, is a main build, and postdates the Found-on build. Rows 31 and 33 are okayed on #1757, which is after the #475 merge build #1756. "Again Android #2013" on rows 10 and 18 predates the #472 merge, as the story intends. The later sightings on Submission #135 (lines 74, 77, 275, 281; 21:20 to 22:07) all follow its 20:13 finish. Robert's Android #2006 sighting was built 40 min before #1745.
- **GitHub, Slack and Gmail copies.** The three comment texts are identical across GitHub, the #zombie-prs bot replies and Gmail (Slack escapes `&` as `&amp;`). Times step correctly: 15:42:10 → 15:42:12, 15:53:40 → :42 → :59, 16:09:50 → :52 → 16:10:09. New ids do not collide with base (`#472#rev_2`, `rc_1`; `#475#rev_2`, `rc_1`; `#473#c_2`, `ev_5`). The Gmail thread ids are Calvin's existing base threads for #472 and #475. The bot pretext format and PR titles match base.
- **Thread parents.** All five reply-count updates are right: zombie-bugs 11→12 with 3 users and 4→5 with 1 user; zombie-prs 2→3, 3→4, 3→4. All posters are members of the channels they post in. The three DMs are Calvin with Brian, Vincent and Marcus respectively.
- **Meeting.** Trello card created 16:02, invite sent 16:05, Brian's DM 16:41; card changed 17:22, invite updated 17:24; Brian's note 20:25, his DM 20:40. Trello action ids encode their own dates. Leonard is the base creator id used. idShort 80 is the next free number on the board. 18:00Z is 12pm CST, 2pm EDT and 9pm GMT+3, matching base invites for Calvin, Vincent and Brian.
- **Brian's note.** The "input blocker I parked" (base DM 09-25 13:59), Oliver's skip-tutorial exception in #zombie-bugs (/1057) and the Bug Checklist and Collect&Win canvases all exist in base.
- **Docs and timestamps.** Doc style-run offsets equal body lengths (430, 608, 223). Slack `ts` matches `created_at` on all 13 messages. Gmail `internal_date` matches `date` on every mail.

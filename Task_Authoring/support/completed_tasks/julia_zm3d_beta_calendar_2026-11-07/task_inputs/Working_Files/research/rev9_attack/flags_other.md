# Rev 9 census: "flagged since this brief", everything outside Slack

Window: 2025-09-24T17:40:52Z (brief `modified_time`) to 2025-10-01T07:00:00Z (clock). SQL reviewed: sha 892f7edd... (checked, matches the brief).

## Result

- **Set proved closed outside Slack.** Six items qualify and all six are in truth.json. Nothing extra, nothing missing.
- **No graded item is pushed out** by the new wording.
- **Two defects in truth.json** (owner text, F2). No SQL change needed for them.
- **One residual exposure** (F1): ZOM-565 meets the inclusion words and only its author's own sentence keeps it out.
- No item is left OPEN. F1 is OUT by quote, but it is the one a reviewer can press.

## Findings, most serious first

### F1. ZOM-565: the only record that literally meets the inclusion clause (exposed, not OPEN)

- For listing it: opened Sep 25 inside the window, labelled VFX, about the Endless start screen, still Todo. Marcus, Sep 29: "The new bar is still hidden in there for you to hook up, and the glow still shows on every box until it is tied to the Claim state."
  - That is player-facing art, flagged as not done, since the brief.
  - The brief's exclusion "not polish nobody flagged" does not reach it, because it was flagged.
- Against: the same comment continues "This is the P1/P2 endless polish from the list Brian gave me, the screen already works without it, so it is not needed for the beta." The rule's lead is "what still has to land before it runs for bought users".
- Basis label: under the brief's definitions this is **SCOPE_GAP** (only the author's own claim covers it). In its favour:
  - Nobody says it is needed.
  - The list he cites is real and Julia-reachable: #zm-animations, Sep 12, Brian: "*P1/P2 – Endless mode remaining VFX*".
  - The last platform report accepted the same quote: F24 "Settled by: 'not needed for the beta' (both comments)". That text has not changed since.
- Smallest fix (optional, one row): a comment by Brian on ZOM-565 after Sep 29 14:34Z, the same pattern rev 9 used on ZOM-566. For example: "Agreed, the bar and the glow can follow after the beta, the start screen is fine as it is." Brian wrote the list but not the ticket, so the label moves to RECORD.

### F2. truth.json does not resolve two owners, and the rule asks "and who owns it"

- Weekly Leagues reads "(league owner)". ZOM-429's `assignee_id` is douglas@harmonygames.co. The platform's Reading A wrote "(Douglas)".
- Collect & Win's "server windows reach prod with the Oct 8 backend release" has no owner at all. The release event's organizer and creator is douglas@harmonygames.co. The platform's F20 settled the same point: "Prod deploy owner | Douglas | Arthur / Owen".
- Smallest fix: change both strings in `solver.py` lines ~606 and ~619 and regenerate truth.json. No SQL change. Check the rubric and Oracle Events carry the same names.

### F3. Confluence "not yet live" (Sep 29) could seed an extra Collect & Win item: store approval (OUT)

- For listing it: Live-Ops calendar v3: "Built for the end-of-September beta submission (QA blockers cleared 26 Sep 2025); not yet live." Separately, Samuel puts the daily gift frame "in both submission builds from today", so Sep 30 work is in submission, not yet on the stores. The UA deck says the buy starts "once the stores approve the Sep 30 builds".
- Against:
  - The deck is Sep 23, before the brief, and is a condition on the buy, not on a beat.
  - The only dated cause given for Collect & Win is Arthur's server-windows note.
  - The brief ties the start to server windows, "not when its client PRs merged".
  - "Nothing else goes in."
- Treat the Confluence row as corroboration of the graded server-windows item. No fix needed. If the Slack pass finds a beat-named store-approval flag that Julia can read, this reopens.

### F4. "Before it runs for bought users" against the two Season Pass items (low)

- The attack: Season Pass already runs when bought users arrive on Oct 6, so items needed only for Nov 1 do not land "before it runs".
- The config is safe on a separate rule: "Every config a beat needs lands before its lock."
- The strip rests on Arthur: "It needs the November range before that season opens". The Nov 1 season is inside the calendar span, and the brief's start section says "Season Pass seasons open on the 1st at 00:00 UTC".
- No fix.

### F5. Trello "Win and Collect" tick lands after Arthur's three notes (low)

- Leonard set `dueComplete` on the card at 2025-09-30T16:40:13Z, after #470 rc_10 (15:51:06Z), #472 rc_1 (15:52:58Z) and #468 rc_38 (Sep 29).
- It does not close them:
  - The card has no description and says nothing about vials or windows.
  - Marcus's 18:05Z note shows open art after the tick.
  - The Oct 8 event is still ahead.
  - On main, no asset has "vial" in its name. #468 merged 37 minutes after Arthur's note, but its last branch commit is Sep 26. After that merge, Collect & Win changes on main are scripts and two UI prefabs only.
- The ZOM-521 line "[X] Live-ops icons appearing on the screen and animations on these icons" (updated 16:27:38Z) is likewise older than Marcus's 18:05Z note.
- No fix. Keep the rubric off the Trello tick.

## (1) Every flag that qualifies, compared with truth.json

| Beat | Item | Record, UTC | Quote | Kind | Owner | Closed later? | truth.json |
|---|---|---|---|---|---|---|---|
| Collect & Win | Server windows to prod | match3d#470 rc_10, Sep 30 15:51:06. Also GCal `evt_...` (updated Sep 26 17:20:09) and Confluence (Sep 29) | "Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next backend release." | Prod deploy | Douglas (event organizer) | No | Yes, owner missing (F2) |
| Collect & Win | Final vial models | match3d#468 rc_38, Sep 29 15:36:41 | "The final vial models are missing, Claire has those on her list." | Art | Claire Morgan (Art Lead) | No; git shows no vial change | Yes |
| Collect & Win | Event icon animation | ZOM-465 cmt_zom465_2, Sep 30 18:05:02 | "The Collect & Win event icon animation is still to do on my side, the other event icons are finished." | Art | Marcus | No | Yes |
| Season Pass | November config | Brian's mail, Sep 26 07:40:26 | "moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time ... I just need the two extra days on the premium track." | Config | Brian | No later mail in Julia's box | Yes |
| Season Pass | Premium strip | match3d#472 rc_1, Sep 30 15:52:58 | "still set to the October range. It needs the November range before that season opens, Oliver is taking the date change." | Config or art (either qualifies) | Oliver | No; his later commits touch the popup flow only | Yes |
| Weekly Leagues | Held beat's fix | ZOM-429 (first limb of the rule, no date test) | Vincent's Sep 30 re-test (Slack) | Held fix | Douglas (assignee) | No; ticket still Backlog | Yes, owner vague (F2) |

Plague Race, Endless, Quests and Daily Login: nothing qualifies, and truth.json is empty for all four. Correct.

### The specific checks you named

- **Brian's Sep 26 mail:** in the window, config, names Season Pass, owner stated, no later reply. Qualifies. Sep 22 is pre-brief but is superseded by it. Julia's mailbox holds no other mail in the window.
- **Oct 8 release:** the event's Sep 24 16:05Z creation does not matter. The event was updated Sep 26 17:20:09Z, inside the window, and the flag itself is Arthur's Sep 30 note. The event supplies only the date and the owner. The brief also reaches it directly: "A beat whose server windows are waiting on that release starts late".
- **Arthur's three notes:** all in the window, each names its beat. The rule's passive "has been flagged" takes a reviewer, so the old "an owner has flagged" problem is gone.
- **Marcus's Sep 30 note:** qualifies. It overrides his Sep 26 "every event icon on the main menu has its animation now". No later record.

### Does a ticket opened in the window count as a flag by itself?

Yes, the words allow it: a ticket saying work is needed is a flag, and the passive excludes nobody. Only two tickets were opened in the window across all 3,687 Linear issues and five teams. The SQL adds none.

- **ZOM-565** (Sep 25, Endless Horde Start Screen Vfx): out by "so it is not needed for the beta" (F1).
- **ZOM-566** (Sep 30, Collect&Win Analytics): out by "not analytics", and the title and info text are out by Brian: "they do not have to land before the beta". Brian is not the assignee, so this is RECORD.

## (2) Borderline items

| Item | Record, UTC | Why it could go in | Quote that keeps it out | Call |
|---|---|---|---|---|
| Endless start screen VFX | ZOM-565, Sep 25 and 29 | Art, flagged, in window | "so it is not needed for the beta" | OUT, exposed (F1) |
| Endless gameplay VFX "wip" | Commit 1a92f8810b, Sep 30 12:44, branch only | "infiniteBoss and endless mode core gameplay ui vfx wip", 22h after Marcus's note | "the P1/P2 endless polish from the list Brian gave me". That list line points at ZOM-465 and reads "Endless mode remaining VFX", so it covers all of it | OUT |
| ZOM-465 leftover "Refill Timer ticking" | Undated description, base `updated_at` Sep 23 | Unstruck on an open ticket; post-SQL `updated_at` is Sep 30 | Pre-brief, and it asks "do we still need to do that?" | OUT |
| Card VFX | ZOM-521 cmt 2, Sep 30 16:27 | "leaving this item, ZOM-528 and ZOM-541 open until Brian has seen it in a build" | Cards are not a beat ("flagged for that beat"); "Card pack animation went in with #475" | OUT |
| Token travel | ZOM-526, Sep 26 and 30 | Unticked on the master ticket | "it does not have to land before the beta"; "Only the Axe Arena travel is left here" (Axe Arena is off) | OUT |
| #477 header title and info text | Commits Sep 30 21:34 and 22:24 | Open PR, player-visible text | "they do not have to land before the beta" | OUT |
| Queue manager / Plague Race panel | ZOM-543 cmt, Sep 30 16:20 | "in progress"; flow omits Plague Race | Not prod deploy, config or art. Trello "Queue Manager" ticked 16:40:22, later | OUT |
| New quests and balance | Trello #61, Sep 29 17:55:44 | "go in with the Mon Oct 13 rollover if they are ready" | "The rollover does not wait on them, the current quests keep running either way." Leonard is named on the card, but the platform's F30 settled on this quote | OUT |
| ZOM-534 edge case | Douglas, Sep 25 | "keeping this open to watch one timing edge case" | Leonard, Sep 30: "it is good on prod now". Commit 47c65623e7 (Sep 10) is in Submission_Android builds from 119 | OUT |
| Daily gift sprite GUID | CodeRabbit #471 rc_2, Sep 29 22:04 | "will surface as missing sprites across the UI" | Samuel, Sep 30 21:07, on the Daily Gift art: "so nothing is left here". #471 approved and merged. Apart from the sprite's own .meta, no text file under Assets on main contains either GUID, so nothing points at the changed ID | OUT |
| C&W grand prize header placeholders | CodeRabbit #470 rc_8 and review, Sep 30 03:44 | "can show placeholders". The code on main is unchanged | Arthur, later, as reviewer: "The client side in this PR is fine as it is." Not prod deploy, config or art | OUT |
| Leaderboard toggle shadow | CodeRabbit #471, Sep 29 22:04 | Names a beat's UI | Cosmetic code suggestion, not prod deploy, config or art | OUT |
| Season Pass fixes after the submission builds | Oliver: 93f45ebbfc (Sep 30 21:36), 0ff577550e "Fix end popup" (Oct 1 05:44); tags Dev only | ZOM-534-shaped: on main, not in iOS 50 / Android 135 | SILENCE: nobody flags them, and "Nothing else goes in". They are also absent from the export's commit table (git tree only) | OUT |
| Store approval | See F3 | "not yet live" | "not when its client PRs merged"; the deck is pre-brief | OUT |
| Season Pass analytics | ZOM-552, Sep 26 | "keeping this open until the data is checked" | "not analytics" | OUT |
| Endless left_level field | ZOM-549, Sep 26 | "does not send total_equipped_power yet" | "not analytics" | OUT |
| Apple sign-in restore | ZOM-544, Sep 29 | "progress does not restore yet" | Not a beat. Scope: "an event window, a reset or a start push" | OUT |
| Bot items on #477 | CodeRabbit, Sep 30 22:33 | "Event will never fire" | Analytics events | OUT |

### The date reading of "since this brief"

The doc shows "Frederick, Sep 24", so a run may cut at the date, not at 17:40:52Z. It changes nothing. The records earlier that day:

- cmt_zom432_1: closed by Samuel.
- cmt_zom526_1: closed by Brian and Calvin.
- cmt_zom556_1: says claiming works.
- ZOM-564: "Free" booster label, not a beat.
- The GCal creation.

### For the Slack pass to reconcile (I only ran targeted searches there)

- #zm-animations (Julia is a member), Sep 25 15:53, Marcus: "I also need to add few text animations like for the combo". Same Endless polish; covered by the P1/P2 quote.
- #zm-animations, Sep 30 18:16 and 22:25, Robert: "better 'enraged' effects"; "that was a placeholder". Art, but not beat-specific.
- DM D076V3NB6P7, Sep 30 16:33, Brian to Marcus: "Could you polish the bottle vfx for Collect&win?" Julia is not a member, so it cannot be graded. It is still the one place a Collect & Win art request exists outside truth.json.

## (3) Graded items the new wording could push out

None. Lowest margins:

- Both Season Pass items on "before it runs" (F4).
- The icon animation, if a reader reasons "Brian's list made icons P1, and Marcus called P1/P2 not needed". That fails: Marcus's reason is "the screen already works without it", about Endless. The list line for icons is struck through as done, and his Sep 30 note reopens only Collect & Win with no such disclaimer.
- Brian's mail as a "flag" rather than a commitment: "I just need the two extra days" says not done, and the Config locks rule requires it regardless.
- The held fix needs no date test (first limb).

## What I scanned

Every item below was read in full unless noted.

- **Linear:** all 3,687 issues filtered on created, updated, started, completed and canceled. 12 base issues in the window; 22 after the SQL. The base has no comments. All 29 injected comments read; 19 are in the window. All 96 open ZOM tickets listed.
- **GitHub (15 repos):** 19 PRs, 27 base reviews plus 1 injected, 92 inline comments plus 3 injected, 17 conversation comments, 63 timeline events, 118 commits. The real git trees add 35 match3d commits not in the export (mostly merges, plus 2 Oliver fixes after the submission builds), 1 match3d-backend commit (a0e4a21, Sep 29, C&W schedule split prod/dev) and 1 liveops-dashboard-buddy commit.
- **Trello:** 5 base actions, 1 injected comment, whole ZOM ROADMAP board read. No attachments dated in the window.
- **Gmail:** Julia's base mailbox is 253 threads and 304 messages, the latest Sep 17, so none in the window. The only mail in the window is Brian's injected Sep 26 mail. Across all 81,404 threads, 361 messages fall in the window; 3 name Julia, all a "Match 3D Defense" share notice in other people's mailboxes.
- **GCal:** 30 event rows created or updated in the window. On Julia's view that is one event (Engineering Focused Weekly Planning, Sep 29, no description), plus the injected release event.
- **Drive family:**
  - Drive: 9 base files. Only the Data Dictionary is Julia-reachable; it is analytics, scanned for not-done wording, nothing qualifying.
  - Injected: the ZM Live Ops folder and the calendar sheet, headers only.
  - Docs: 3 and Slides: 1, none Julia's. The POD notes of Sep 29 are private to Leonard, unreachable, and agree with truth: "needs to be deployed to production servers".
- **Confluence:** 4 pages dated in the window, all read: Live-Ops calendar, Season Pass spec, ZM3D GDD, API Reference. No comments or attachments in the window.

## What I did not scan

- Slack in full (targeted closure searches only).
- Snowflake and Contacts.
- Linear attachment media (undated images and videos).
- CodeRabbit inline bodies past about 420 characters, except those on the Daily Gift GUID, placeholders and #477. Bot review bodies on #468 and #470 were read by item title. #476 (vision bot) by headline only.
- Earlier versions of Confluence pages: the export holds one "Imported" row per page, so I could not diff them.

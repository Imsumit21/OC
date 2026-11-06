# Grounding: iOS #49 / Android #133 gate-skip coherence (rev2)

Universe: synth-cut, clock 2025-10-01T07:00Z. Persona: Vincent Parker (QA), Linear `usr_65c76e0b87aa7e9b` / Slack `EMPLOYEE_0012_SLACK_ID`.
Sources: base exports under `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/`, injected SQL `Task_Authoring/task_inputs/01_Universe_Inject.sql`. No SQL executed.

Persona channel membership (base `slack/channels.json`): #builds C05433XK267 ✓, #zombie-bugs C08R27X0EAH ✓, #zombie-match3d C0880U9751A ✓, #qa C06UCHM7RRQ ✓, **#executives C07C2866011 ✗ (9 members, no EMPLOYEE_0012)**.

---

## 1. Current seeded text: Leonard's rules doc, ZOM-570, records naming #133 / #49 / #127 / #40 / "last gate" / "every ZM store submission"

### 1a. Leonard's rules doc — `gdrive` row at SQL line 221, `gdocs` body at SQL lines 222–233

File: `f_632c44650df44fe252ee59`, "ZM submission rules", owner leonard.hayes, shared with Vincent as **reader**, `created_time = modified_time = 2025-09-23T09:10:00Z`.

Body, sentence by sentence with SQL line numbers (blank lines are 224/226/228/230/232):

- **L222** title line: `ZM submission rules`
- **L223** `Leonard, Sep 23`
- **L225** ¶1 (the sentence under review): "After the orange juice one on Sunday I want the gate tighter **for every ZM store submission from now on**, not just the Bug view in Linear."
- **L227** ¶2 (scope, the boundary sentence): "Scope: every ZM ticket that's still open (any state but Done, Canceled or Duplicate), whatever team or label (ART or DES tickets with ZM in the title count too), plus everything that moved to Done after **the last gate's builds were cut (Android #127 / iOS #40 on Sep 22)**. Release tickets, ZOM-359 and ZOM-475 stay out, that work is separate. From the next gate on, tickets filed while the gate is running get a row too, including the ones you file yourself."
- **L229** ¶3 (definition of fixed): "A ticket counts as fixed when Vincent or Brian saw it working on the candidate builds, or on prod if the fix is server side. A Done ticket for a bug nobody has re-checked yet also counts as fixed if its fix is actually in the candidate builds (or live on prod), noted as not re-checked. Done in Linear or a dev saying fixed isn't enough by itself, and if the latest check on the candidates still shows the bug, call it on how bad it is whatever the ticket says."
- **L231** ¶4 (blocker / known issue): "Blocker = crash, freeze, player stuck or can't finish a level (like the orange juice one), lost progress / coins / lives (infinite-lives time included) / boosters / inventory items, or a purchase that doesn't deliver. Any other bug a player can see is a known issue, even if it doesn't change play, visual and sound glitches included. Art/VFX requests, requests for design, balance or tuning changes, analytics, tools, backend endpoints and new features aren't bugs, no call. The same goes for a ticket that only asks for new or updated art, animation, VFX, text style or UI layout (replacing an outdated model or icon with its new version included), even with a Bug label and even once it's Done, and for a ticket that doesn't say what goes wrong."
- **L233** ¶5: "Blockers go on the release ticket. If in doubt ask me before the go/no-go, not after."

Note the doc is dated **Sep 23**, i.e. **after** the #127 / #40 cut (Sep 22) and **before** the #133 / #49 cut (Sep 26).

### 1b. ZOM-570 (injected, SQL line 11)

Title: `ZM store push - Android Submission #135 / iOS Submission #50`. State In Progress, assignee `usr_65c76e0b87aa7e9b` (Vincent), creator Arthur. Description, verbatim:

> Store push for ZM.
>
> Candidates: Android Submission #135 and iOS Submission #50, both started from main today. We decide at the go/no-go on Friday, invite coming.
>
> Vincent - QA gate as usual: Leonard's submission rules and my note on how we cut submissions both apply, the docs are shared with you. Blockers go on this ticket by key, the existing ticket if there is one (I'm putting the reuse rule on the tech-issues card). I'll post the candidates in #zombie-bugs.
>
> Other push notes go in the comments here.

Key: Arthur's own vocabulary for the Oct 3 event is **"store push"**; he calls the Oct 3 gate "QA gate as usual".

### 1c. Every other seeded record naming #133 / #49 / #127 / #40 / "last gate" / "every ZM store submission"

| SQL line | Record | Text |
|---|---|---|
| 116 | Slack #zombie-bugs `1759140300.935009`, Vincent (`EMPLOYEE_0012`), 2025-09-29T10:05Z | "re-tested on Android #133 / iOS #49: trophy path claim spam is ok now (ZOM-435), consecutive login quest ok too (ZOM-557) ✅" |
| 117 | Slack #zombie-bugs `1758563100.005758`, Vincent, 2025-09-22T17:45Z | "gate for #127 / #40 done, Bug tickets only this time. tab is in my release sheet" |
| 118 | Slack #zombie-bugs `1759263900.484190`, Arthur, 2025-09-30T20:25Z | "ZM store candidates are up: Android Submission #135 and iOS Submission #50, both from main. @Vincent QA gate before friday's go/no-go please, details on ZOM-570" |
| 33–45, 59 | `linear_comments` cmt_zom237_1 … cmt_zom559_1, cmt_zom535_1 | QA notes phrased "Tested on Android Submission #133 / iOS #49 …", "Android Submission #133 …", "#135: … same as Brian found on #133." (Vincent and Brian). These are re-test notes, never called a gate. |
| 123–125 | Slack DM Vincent↔Brian `1759160460.731000`, 2025-09-29T15:41Z | "abi bugün #133 ve #49'da iki tane buldum … ZOM-458 … ZOM-535" (two new bugs found on #133/#49) |
| 258 | `gsheets` "ZM3D Release Gate" tab 1 | `Sep 22 - Android #127 / iOS #40` — **the only gate tab; there is no #133/#49 tab** |

There is **no seeded record anywhere that names #133 / #49 as a gated build**, and none that says why it shipped without one. Nothing in the injection mentions #133/#49 except Vincent's re-test note and the QA comments — all of which read as re-tests, not gates.

---

## 2. Base facts: Android #133 / iOS #49

### 2a. #builds cut lines (base `C05433XK267/2025-09.json`, message bodies in `attachments[].fallback`)

- idx 1036, ts `1758928027.384209`, **2025-09-26T23:07:07Z**: `Match3D Android Submission - #132 Failure after 9.6 sec` — `No Changes.` (the run immediately before; failed)
- idx 1037, ts `1758928063.629989`, **2025-09-26T23:07:43Z**: `Match 3D iOS Submission - #49 Started by user Arthur Blake`
- idx 1038, ts `1758928165.960339`, **2025-09-26T23:09:25Z**: `Match3D Android Submission - #133 Started by user Arthur Blake`
- idx 1039, ts `1758928386.414939`, **2025-09-26T23:13:06Z**:
  `Match 3D iOS Submission - #49 - main Success after 5 min 56 sec`
  `Match 3D iOS Submission - #49 - main Changes:`
  `- Disabling tutorial skip [[PERSON_NAME_0022]]`
- idx 1040, ts `1758928853.095259`, **2025-09-26T23:20:53Z**:
  `Match3D Android Submission - #133 - main  Success after 11 min`
  `Match3D Android Submission - #133 - main  Changes:`
  `- Disabling tutorial skip [[PERSON_NAME_0022]]`

Both **branch `main`**, both **started by Arthur Blake**, both carrying exactly **one** delta commit ("Disabling tutorial skip"). Cut on a **Friday night (Sep 26)**.

Immediately preceding submission pair: iOS #48 `2025-09-26T20:07:22Z` (Success 6 min 8 sec) and Android #131 `2025-09-26T20:12:58Z` (Success 11 min). Preceding successful Android submission before #131 was #129 (`2025-09-26T02:25:52Z`, ~60-change list). So **several submission jobs ran between the Sep 22 gate and Sep 30 with no gate**: Android #129, #131, #133 and iOS #48, #49.

### 2b. The Sep 29 release record, full context (base #zombie-match3d `C0880U9751A/2025-09.json`)

No thread: message idx 463 has `thread_ts = null`, `reply_count = 0`, and no base message carries `thread_ts = 1759182908.627389`. So "/463" is a **standalone message, zero replies** — there is nothing to quote beyond it.

±5 messages:

- 458 `2025-09-28T17:58:34Z` Tunc(EMPLOYEE_0016): "Downloads app, launches it, starts level, homes out, uninstall. He didn't even play the first level tutorial..."
- 459 `2025-09-28T17:59:01Z` Tunc: "In fact, the first level tutorial didn't even load for him"
- 460 `2025-09-28T18:47:30Z` **Leonard**: "He didn't like the game I guess. Saw the splash screen and decided this game is too cute for his taste? :)"
- 461 `2025-09-29T19:45:29Z` **Arthur**: "@here can all Unity users please download this Unity version. We will be upgrading the project shortly."
- 462 `2025-09-29T20:51:52Z` Tunc: "when do I switch it over?"
- **463 `2025-09-29T21:55:08Z` Leonard (`EMPLOYEE_0038`): "I just released 0.3.49 on IOS"** ← the record under review
- 464 `2025-09-29T23:09:04Z` Tunc: "@Arthur Can I switch over to new Unity? Or wait?"
- 465 `2025-09-29T23:42:41Z` Arthur: "we haven't merged it yet. I'll let you know"
- 466 `2025-09-29T23:43:08Z` Arthur: "just install the latest version. Unity hub will automatically open the project using the correct one when it is time."
- 467 `2025-09-30T05:50:37Z` Tunc: "@… Unity is sending us a lot of bot installs…"

The only thing on the surrounding timeline is **Unity-version chatter**. /463 sits in a **quiet gap** (no other ZM release/QA message between 21:55Z and 23:09Z; the adjacent messages are Unity install questions).

### 2c. App Store or TestFlight?

**App Store**, after review — three base quotes fix the pipeline:

- Leonard, #zombie-bugs `2025-09-25T02:37:38Z`: "Once it's merged we can trigger a testflight build and then can submit to Apple. **It will take a few days to go live**" — TestFlight is the QA path, Apple review is the store path.
- Arthur, **#executives** `2025-09-27T01:16:08Z`: "**we are now waiting for review for both platforms**"
- Leonard, **#executives** `2025-09-28T17:05:53Z`: "**Zombie IOS is still waiting for review**"
- Leonard, /463: "I just released 0.3.49 on IOS"

So #49 sat in App Store review from Sep 27 to Sep 29 and was released to the App Store at `2025-09-29T21:55:08Z`. (Separately, the Sep 30 playtest-vendor email refers to "TestFlight build 50" — that is the **next** candidate #50 on TestFlight.)

### 2d. Was Android #133 released, and by whom?

Yes — released to Play by **Leonard**, but **the only evidence is in #executives, which Vincent is not a member of**:

- `2025-09-27T00:36:08Z` Leonard (#executives): "I just rolled out Android"
- `2025-09-27T00:41:02Z` Leonard: "will turn on IOS when it gets approved"
- `2025-09-27T15:51:47Z` Leonard: "I just published Android @Arthur @Tunc"
- `2025-09-28T16:11:06Z` Leonard: "this is the latest Android - **0.3.133** <metabase link …app_version=0.3.133…>"

Persona-visible evidence for #133 is therefore only: the #builds Submission #133 Success line (§2a), Vincent's own Sep 29 re-test note (SQL L116) and the QA comments. **"Android #133 was released" is not a fact Vincent can read in base** — the iOS half is (via /463), the Android half is not.

### 2e. Base messages Sep 23–30 about a ZM hotfix / quick iOS release / skipping QA

Only these, none of which announces or authorises a gate skip:

- Leonard, #zombie-bugs `2025-09-25T02:37:38Z`: "Yeah go for it. Once it's merged we can trigger a testflight build and then can submit to Apple. It will take a few days to go live"
- Arthur, #executives `2025-09-27T01:16:08Z`: "we are now waiting for review for both platforms"
- Leonard, #executives `2025-09-28T17:05:53Z`: "Zombie IOS is still waiting for review"
- Leonard, #zombie-match3d `2025-09-29T21:55:08Z` (/463): "I just released 0.3.49 on IOS"

No base message in Sep 23–30 contains "hotfix" for ZM, and none says anything about skipping QA or skipping a gate. In fact the word "gate" (as the release gate) appears **nowhere in base Slack** for Sep 2025 — the three literal hits are unrelated idioms ("out of the gate", "a gate for cards"). Every gate record in this universe is seeded: Leonard's Sep 23 doc, the sheet's "Sep 22 - …" tab, and Vincent's Sep 22 post "#127 / #40 done, tab is in my release sheet". So both candidate terms ("store submission" and "store push") are equally seeded vocabulary; narrowing to "push" introduces no ungrounded word.

---

## 3. Base facts: Android #127 / iOS #40

- Cut **2025-09-22**, both from `main`, both started by Arthur Blake:
  - Android Submission **#127** Started `2025-09-22T12:30:43Z`, `Success after 9 min 12 sec` at `12:39:43Z`, Changes: `- Fix pear and orange juice [Arthur Blake]`
  - iOS Submission **#40** Started `2025-09-22T12:32:20Z`, `Success after 7 min 40 sec` at `12:38:18Z`, Changes: `- Fix pear and orange juice [Arthur Blake]`
- Gate (**seeded**, SQL L117): Vincent, #zombie-bugs `2025-09-22T17:45:00Z`: "**gate for #127 / #40 done, Bug tickets only this time. tab is in my release sheet**". Sheet tab `Sep 22 - Android #127 / iOS #40` exists (SQL L258); **no other tab exists**. Neither the tab nor that post exists in base — the Sep 22 gate is established only by the injection.
- Released (`0.3.127` / `0.3.40`), Leonard in **#executives** `2025-09-22T21:04:40Z`: "**0.3.127 on AnDroid (we just published it) and 0.3.40 is in review on IOS right now**".
- iOS 0.3.40 went live the next day — Arthur→Vincent DM `D06477JGUKT` `2025-09-23T16:02:13Z`: "**iOS I just released**", Vincent `16:04:38Z`: "**then it's live**".
- Arthur, #zombie-match3d `2025-09-23T16:02:45Z` (thread `1758643365.607149`, 1 reply): "@Douglas can you update the match3d required versions: **Android: 0.3.127 / iOS: 0.3.40**" → Douglas `2025-09-23T17:30:38Z`: "Done!"

Note the **timing shape is identical to #133 / #49**: Android published immediately, iOS after review ~1–3 days later. The difference is only that #127 / #40 had a gate tab and #133 / #49 did not.

---

## 4. Fix options evaluated

### (a) Narrow Leonard's one sentence — RECOMMENDED

Replace **SQL line 225 only**; lines 227–233 untouched (so the scope boundary, the fixed definition and the blocker/known-issue rules are bit-identical).

Narrowed sentence:

> After the orange juice one on Sunday I want the gate tighter for **every planned ZM store push from now on (not the drop-in builds)**, not just the Bug view in Linear.

Test against every base fact in §2–3:

| Fact | Under the narrowed sentence |
|---|---|
| #127 / #40 cut Sep 22, gated Sep 22, published Sep 22–23 | Covered: that *was* the planned push; it is "the last gate" and stays the scope boundary. |
| #133 / #49 cut Sep 26 23:07Z from `main`, released Sep 27 (Android, Leonard "I just rolled out/published" — #executives only) and Sep 29 21:55Z (iOS, /463) with no gate tab, no ZOM ticket, no go/no-go invite and no pre-release push announcement in the ZM channels | **Not covered** — a drop-in release off the submission job, exactly the class the parenthetical excludes. Nothing has to explain it; it is simply out of the rule's trigger. |
| #135 / #50 (Oct 3) | Covered — ZOM-570 is titled "ZM store push", the calendar is "ZM store push - go/no-go", Arthur posts "QA gate before friday's go/no-go". It is plainly a planned push, so the parenthetical cannot be misread to exclude it. |
| Android #129 / #131, iOS #48 (also ungated, also between gates) | Not covered — same drop-in class. This is an **extra** coherence gain: the literal "every ZM store submission" was already violated ≥5 times in base, not just once by #49. |
| Vincent's Sep 29 note (SQL L116) | Unchanged: he **re-tested** #133/#49; re-tests are not gates and the sentence never claims they are. |
| Scope boundary reads naturally? | Yes: "plus everything that moved to Done after the last gate's builds were cut (Android #127 / iOS #40 on Sep 22)" is untouched and still names #127 / #40. |
| Doc title "ZM submission rules" / ZOM-570's "Leonard's submission rules" | Still fine — the title and Arthur's reference are unchanged. |

Residual weakness: "planned" is a judgement word, so a determined reader could ask "wasn't 133/49 planned on Friday night?". It is answerable from base (no ticket, no invite, no announcement, Leonard's own "I just released" with no prior notice), but it is not zero-risk like a hard field would be.

### (b) Add one dated record instead

Proposed record (rejected as primary, kept as fallback):

- Service/container: Slack **#zombie-match3d** (`C0880U9751A`) — Vincent is a member; it is the channel that already carries /463.
- Author: **Leonard Hayes** (`EMPLOYEE_0038_SLACK_ID`) — active that week (Sep 26 17:15Z, Sep 28 18:47Z, Sep 29 21:55Z).
- ts: `1759183260.000000` = **2025-09-29T22:01:00Z**, posted 6 minutes after /463 — quiet gap, between /463 (21:55Z) and /464 (23:09Z). (Would require updating /463's `reply_count`→1, `reply_users_count`→1, `latest_reply`→`1759183260.000000`.)
- Text (draft in §6B).

Why it is weaker:

1. It **documents a deviation from "every ZM store submission"** instead of removing the contradiction. The rules doc would still say every submission is gated; the record would say this one was not. That converts a wording defect into an admitted process breach — a reviewer can call it a *worse* coherence state.
2. Any honest wording must avoid the false claim that #133/#49 was "just the tutorial-skip fix on top of the gated builds": the #builds Changes list is only the delta since the **previous submission job** (#131 / #48 at 20:07–20:12Z the same evening), and #129 two days earlier carried ~60 main changes that were never in #127 / #40. Claiming "one change on top of what we gated Tuesday" would be **factually wrong** and create a new cross-service contradiction with `How ZM submission builds are cut.docx` ("a submission has exactly what was on main when its job started").
3. Because the only gated builds are #127 / #40, the record must also explain #129 / #131 / #48 — one record cannot cover five ungated releases convincingly.
4. It adds a new discoverable record near /463, which invites solvers to cite it as a "deciding source" for a register row; (a) touches nothing a row can cite.

Additional constraint checked for (b): the truth is only that the **iOS** half is persona-visible. Vincent cannot see the #executives posts that show Android #133 going out (he is not a member), so a record written as "the 133/49 drop" would assert an Android release he cannot verify; a record would have to be iOS-scoped.

### Recommendation

**Take (a).** One clause changes, no register row moves, no new deciding source appears, and it fixes the whole class (five ungated submission releases between Sep 22 and Sep 30), not just #49. The scope boundary "#127 / #40 on Sep 22" and Vincent's Sep 29 re-test note both survive untouched. If the platform insists on (b) instead, use §6B and **do not** also apply (a).

---

## 5. Risk checks for the recommendation

1. **Does it make QA's Sep 29 #133 / #49 check look like a gate?** No. The narrowed sentence says nothing about #133/#49; SQL L116 stays "re-tested on Android #133 / iOS #49 …". If anything the change *reduces* the temptation to read the re-test as a gate, because the rule now keys on pushes, and no push is attached to #133/#49 anywhere.
2. **Does it contradict Leonard's Sep 29 "I just released 0.3.49 on IOS"?** No. Under the narrowed rule, /463 is a drop-in release of a submission build; the rule simply does not claim a gate for it. The sentence "not the drop-in builds" is the only place the concept appears, and /463 is the natural referent.
3. **Does it let a solver argue the Oct 3 gate is optional?** This is the main risk of any narrowing, and it is why the parenthetical is worded "not the drop-in builds" rather than a job-type carve-out ("not the submission jobs"). Oct 3 is a *push* with a ticket, an invite and Arthur's explicit "QA gate" request — the carve-out cannot reach it. Wording that excluded "submission builds" would have been a trap, since #135/#50 **are** submission builds; that variant is rejected.
4. **Does it weaken the scope paragraph?** No — L227 is unchanged, so "everything that moved to Done after the last gate's builds were cut (Android #127 / iOS #40 on Sep 22)" still carries the register boundary, and "the last gate" still resolves to the Sep 22 tab that exists in the sheet.
5. **Does it collide with Arthur's doc `How ZM submission builds are cut.docx`?** No. Arthur's doc explains *how* submissions are cut ("every store submission … is cut straight from main"); Leonard's sentence now explains *when a gate is required*. Previously the two docs used "store submission" for two different things (Arthur: the Jenkins job; Leonard: the release event), which is itself the root defect.
6. **Does it collide with ZOM-570's "Leonard's submission rules … both apply"?** No; the doc is still the submission-rules doc, and it still binds the Oct 3 push.
7. **Does anything in Rubrics/register depend on the literal string "every ZM store submission"?** Not in the register scope (L227) or the blocker/known-issue definitions (L231). Checked the design surfaces: the only other place that phrase appears is **Arthur's** Sep 24 doc (`f_a038a576ca8db6955fae95`, untouched) and it is the resolver for trap **T8** ("since the hotfix train ended every ZM store submission is cut straight from main"). No trap resolver in `01_Hardness_Manifest.json` cites Leonard's L225; T3 (Vincent's #133 re-test ⇒ "ships fixed") and T12/T16 (Brian's #133 re-test ⇒ severity calls) all use the Sep 29 re-tests, which this change leaves exactly as they are. The phrase only sets the gate's cadence. Regenerate/verify with `tools/hg.py lint` after the edit; the change is one string inside one `body_text` of one `gdocs` row (the sibling `gdrive` row at L221 carries no body copy, so its `modified_time = 2025-09-23T09:10:00Z` can stay — a wording fix inside the same Sep 23 revision).
8. **Persona reach**: the doc is shared with Vincent as reader (`shared_with_emails_json` L221), so he can open it; no new container, no new membership needed.
9. **If (b) were chosen instead**: risks are (i) it admits a breach of the un-narrowed rule, (ii) #executives invisibility forces an iOS-only claim, (iii) it must not use the word "gate" for Vincent's Sep 29 re-test.

---

## 6. Drafted text, ready to paste

### 6A. Recommended — one-sentence replacement at SQL line 225

Old (exact, inside the `body_text` literal at L225, note the `''` escaping used for apostrophes in the SQL):

```
After the orange juice one on Sunday I want the gate tighter for every ZM store submission from now on, not just the Bug view in Linear.
```

New:

```
After the orange juice one on Sunday I want the gate tighter for every planned ZM store push from now on (not the drop-in builds), not just the Bug view in Linear.
```

Nothing else in lines 221–233 changes. No other row, comment, Slack message, sheet tab or register row is touched.

### 6B. Fallback only (if (b) is chosen instead) — one Slack reply in #zombie-match3d

Channel `C0880U9751A`, author Leonard Hayes, `ts = 1759183260.000000` (2025-09-29T22:01:00Z), `thread_ts = 1759182908.627389` (reply to /463), reply_count 1 / reply_users_count 1 on /463, `latest_reply = 1759183260.000000`:

```
iOS only, and it was a drop-in: no gate on this one, the gate rides on the store pushes. Next one is the October push.
```

If a Linear comment is preferred over Slack, put the same sentence at `cmt_zom570_*` on ZOM-570 with `created_at = 2025-09-29T22:01:00Z` — but note ZOM-570 is created `2025-09-30T20:20:00Z`, so a comment dated Sep 29 on it is **impossible**; a Slack reply (as above) is the only dated-before-Sep-30 option that works, and it is the only container where Vincent can read it next to /463.

Do not apply 6A and 6B together.

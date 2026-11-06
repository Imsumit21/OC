# Grounding: ZM store-version facts (synth-cut, clock 2025-10-01T07:00Z)

Scope: base records 2025-08-15 → 2025-09-30 that state a Zombie Match 3D / "ZM" / match3d store
version, a store/beta release, the 1.3.24 hotfix, or a TestFlight/App Store/Play release.
Readers used: `hgget.py`, `hg.py search search`, plus a read-only slice of
`Universe_SynthCut/.../slack/messages/*/2025-0[89].json` (pointers below are array indexes in
those files). No SQL was executed and nothing outside this file was changed.

---

## 1. Base records stating ZM store versions / store releases (Aug 15 – Sep 30 2025)

### 1.0 The two version schemes (answer to the second half of Q1)

Two labels are used for the same build, and the base uses them consistently:

* **iOS store label `1.3.N`** — only ever used by Leonard, only for iOS store releases:
  * `#executives C07C2866011 /72`, 2025-08-02 08:40Z, Leonard Hayes: "released 1.3.10 on IOS as well"
  * `#executives C07C2866011 /654`, 2025-09-17 04:12Z, Leonard Hayes: "@Arthur feel free to submit 1.3.38 equivalent to Android tomorrow morning"
  * `#zombie-match3d C0880U9751A /286`, 2025-09-17 20:34Z, Leonard Hayes: "1.3.38 is out!"
  * `#zombie-bugs C08R27X0EAH /860`, 2025-09-19 14:23Z, Leonard Hayes: "I just downloaded from the App Store. This is 1.3.38."
* **Build/Store version `0.3.N`** — the label used everywhere else (Crashlytics, Metabase, backend
  "required versions", Arthur, QA, Play Console). Android is **only ever** `0.3.N`; iOS is `0.3.N`
  in every analytics/backend record (`versions=0.3.38 (38)` on `ios:com.calmplay.zombie`,
  `app_version=0.3.49&platform=IOS`, "iOS: 0.3.40").
* The **release branch** `release/1.3.24_HotFix` carries the `1.3.N` label and was used by **both**
  platforms' jobs (Android #107/#108/#112/#114 and iOS #28/#29/#31/#33 all report branch
  `release/1.3.24_HotFix`), so "1.3.24" is a *release-line/branch* name, not an Android version.
* **`0.3.N` ↔ Submission `#N`**: base supports this 1:1 for both platforms (see 1.3 and 1.8).
  `#zombie-bugs /878` (2025-09-20 23:03Z, Arthur Blake) — "testflight 39 is the submission
  candidate" — is the clearest statement that the Submission job number *is* the TestFlight/build
  number of the same `0.3.N`.
  Checkpoints: iOS Sub #24→0.3.24, #28→0.3.28, #36→"testflight 36"/0.3.36, #39→0.3.39,
  #40→0.3.40, #49→0.3.49; Android Sub #106→0.3.106, #119→0.3.119, #122→0.3.122,
  #127→0.3.127, #133→0.3.133.

**Consequence for the injected doc:** `1.3.24` is the *iOS* label of the late-August build
`0.3.24` (= iOS Submission #24, built 2025-08-19/20). It is not, and never was, an Android label,
and by 2025-09-30 it is five store releases old.

### 1.1 Store-build statements, chronological

**2025-08-16 00:28Z — `#D04UGG61DUM /103`, Leonard Hayes** ("0.3.22 seems stable. I think we should
Push out the corresponding Android submission build"). ±3: /100–/102 analytics chatter on 0.3.22
A/B groups; /104–/106 no version content. Shows Android store submissions lagged iOS.

**2025-08-21 16:32Z — `#D04UGG61DUM /202`, Leonard Hayes**: "just released 0.3.24 on IOS".
±3: /199 "what's in 0.3.24?"; /200–/201 build contents; /204 Arthur Blake "we released it on
android yesterday"; /205 no version content.

**2025-08-23 00:00Z — `#issuefeed C083AEP6NBA /73` (Zapier support mirror)**: "…Ik zie dat je nog
op versie 0.3.90 zit, terwijl de nieuwste 0.3.106 is." ±3: /71–/72 Dutch support thread about the
hotfix; /74–/75 follow-ups. Customer-facing statement that Android store version 0.3.106 had
shipped by Aug 23 (matches Android Submission #106, 2025-08-19/20).

**2025-08-28 14:32Z — `#live-incidents C080X4GTZ0E /75`, Leonard Hayes**: "This is the build that's
live right now on App Store - 0.3.24 -> we are still suffering performance issues". ±3: /72–/74
incident thread with logs; /76–/78 triage. Direct proof 0.3.24 was the live **App Store** build on
Aug 28 (and that iOS 0.3.24 = "1.3.24").

**2025-09-02 15:08–15:15Z — `#builds C05433XK267 /16, /17, /18, /19`** (hotfix train, branch
`release/1.3.24_HotFix`):
* /16 15:08Z "Match 3D iOS Submission - #28 Started by user Arthur Blake"
* /17 15:08Z "Match3D Android Submission - #107 Started by user Arthur Blake"
* /18 15:14Z "Match3D Android Submission - #107 - release/1.3.24_HotFix Success after 6 min 35 sec … No Changes."
* /19 15:15Z "Match 3D iOS Submission - #28 - release/1.3.24_HotFix Success after 7 min 15 sec … No Changes."
±3 for /18–/19: /14–/15 unrelated jobs; /20–/22 two short human replies, no version content.

**2025-09-03 03:17Z — `#executives C07C2866011 /85`, Leonard Hayes**: "I released 0.3.28 on IOS".
±3: /83–/84 same-thread scheduling; /87 "I'll test the build once I download it from app stores
tonight"; /89 "It got stuck at 99% for the first time load on 0.3.28. We have to resubmit - damn it".

**2025-09-03 04:51–06:45Z — `#live-incidents C080X4GTZ0E /0, /1, /3`**:
* /0 Leonard: "This is live build from app store 0.3.28 … do you see a login errors on server side?"
* /1 Leonard: "Can someone try to play the game on prod build on the previous App Store builds like 0.3.22 or 0.3.24"
* /3 Vincent Parker: "0.3.24 was okay"
±3 for /1–/3: /4–/6 continuation of the same prod-load incident.

**2025-09-03 15:35–19:19Z — `#builds C05433XK267 /40, /42, /43, /46, /54, /55, /69, /70, /73`**:
iOS #29 (`release/1.3.24_HotFix`, Failure), Android #108 (Success, changes list), iOS Internal
#1524, Android #1774, iOS #31, Android #112, iOS #33, Android #114, iOS Internal #1526 — the last
jobs on `release/1.3.24_HotFix`. ±3 for /42–/43: /39 start of #108, /40–/41 #29 failure + comment;
/44–/45 iOS #30 start. Base therefore shows the **hotfix train ending 2025-09-03 19:19Z**, which
matches injected line 240 ("the hotfix train ended on Sep 3").

**2025-09-03 16:00–16:20Z — `#executives C07C2866011 /127, /135`; `#D04UGG61DUM /0, /6`; `#zombie-design C090N54TG79 /88`**:
"testflight 0.3.29 for testing" (/127); "so 0.3.30 is just the main branch. 0.3.29 is the release
hot fix" (/6); "I'm testing 0.3.29 on testflight" (/88). Establishes beta (TestFlight) builds are
distinct from store builds and carry the same 0.3.N scheme.

**2025-09-10 01:35Z — `#zombie-match3d C0880U9751A /98`, Leonard Hayes**: "Played 50 levels on
0.3.35 - no major bugs". ±3: /95–/97 bug triage; /99–/101 unrelated.

**2025-09-11 00:17Z — `#executives C07C2866011 /345`, Arthur Blake**: "Released android this
morning". ±3: /343–/344 thread; /356 Leonard "ok, can you then make a testflight build?";
/377 Arthur "testflight 36 is building now". Also `#zombie-match3d /125` (Leonard, 03:31Z)
"submitted to app store, when it's approved we'll start buying users at small scale", and
`#zombie-bugs /613` (Arthur, 12:20Z) Crashlytics link `versions=0.3.119 (119)` on Android — so
**Android 0.3.119** (Submission #119, built 00:23Z that day) was the Android store build.

**2025-09-17 04:12–20:34Z** — iOS 0.3.38 ships:
* `#executives /654` Leonard: "feel free to submit 1.3.38 equivalent to Android tomorrow morning"
* `#zombie-match3d /222` Leonard 15:48Z: "IOS is submitted last night to the app stores - it's under review"
* `#zombie-match3d /286` Leonard 20:34Z: "1.3.38 is out!"
* `#D05QQF7V404 /21` Arthur 22:09Z: "Can we update required versions for ZM: Android 0.3.122 iOS 0.3.38"
* `#builds /548` iOS Submission #38 started 01:29Z, `/563` Android #122 started 12:12Z

**2025-09-19 14:23Z — `#zombie-bugs C08R27X0EAH /860`, Leonard Hayes**: "Yeah PNs are at the
beginning. I just downloaded from the App Store. This is 1.3.38. It's not PNs @…". ±3: /855
Vincent "On ios notfication pop ups are at the start of app not lvl 20"; /856–/859 Robert/Vincent
clarify push vs ATT permission; /861–/863 Robert posts the funnel sheet. Confirms the App Store
build on Sep 19 read **1.3.38** (= 0.3.38).

**2025-09-22 21:04Z — `#executives C07C2866011 /908`, Leonard Hayes**: "0.3.127 on AnDroid (we just
published it) and 0.3.40 is in review on IOS right now". ±3: /902 "I played 32 level on 0.3.40 - no
isses"; /904 "I'll add it to the testflight as well"; /910–/911 follow-ups.

**2025-09-23 16:02Z — `#D06477JGUKT /183`, Arthur Blake**: "iOS I just released"; **`#zombie-match3d
/407`, Arthur Blake**: "can you update the match3d required versions: Android: 0.3.127 iOS: 0.3.40"
→ **`/408` Douglas: "Done!"**. ±3 for /407: /404–/406 ZOM status bot + Oliver; /409 Robert asks
for a UI tweak. So on Sep 23 the two shipped store versions were **Android 0.3.127 / iOS 0.3.40**.

**2025-09-26 23:07–23:20Z — `#builds C05433XK267 /1036, /1037, /1038, /1039, /1040`**:
Android #132 Failure (23:07Z) · iOS Submission **#49 Started** (23:07Z) · Android Submission
**#133 Started** (23:09Z) · "iOS Submission - #49 - main Success after 5 min 56 sec … Changes:
- Disabling tutorial skip" (23:13Z) · "Android Submission - #133 - main Success after 11 min"
(23:20Z). ±3 beyond those: /1035 ancillary job; /1041–/1043 next-day build jobs.

**2025-09-28 16:11Z — `#executives C07C2866011 /1093`, Leonard Hayes**: "this is the latest Android
- 0.3.133" (+ Metabase link `app_version=0.3.133&…=ANDROID`); /1096 and /1102 are further
0.3.133 Android queries. ±3: /1090–/1092 and /1094–/1095 unrelated exec chatter. Since Metabase
`app_version` comes from live client events, Android **0.3.133** was live by Sep 28.

**2025-09-29 21:55Z — `#zombie-match3d C0880U9751A /463` and `#executives C07C2866011 /1152`,
Leonard Hayes**: "I just released 0.3.49 on IOS" / "I just released IOS 0.3.49". ±3 for /463:
/461 Arthur "can all Unity users please download this Unity version…"; /462 Robert "when do I
switch it over?"; /464 Robert "Can I switch over to new Unity? Or wait?"; /465–/466 Arthur "we
haven't merged it yet…". No doubt this is the store release of iOS 0.3.49.

**2025-09-30 15:44Z — `#executives /1174`, Leonard Hayes**: Metabase dashboard link filtered
`app_version=0.3.49&…` and suffixed "- IOS" — live players on iOS 0.3.49 the day after the release.

**2025-09-30 18:43–20:13Z — `#builds C05433XK267 /1120, /1122, /1123, /1124`**: "Match 3D iOS
Submission - **#50** Started" (18:43Z), "Match3D Android Submission - **#135** Started" (18:45Z),
"iOS Submission - #50 - main Success after 32 min" (19:15Z), "Android Submission - #135 - main
Success after 1 hr 28 min" (20:13Z). This is the `#50`/`#135` the injected doc refers to.

### 1.2 1.3.24 hotfix (base statements)

* `#builds /16, /17, /18, /19, /40, /42, /43, /46, /54, /55, /69, /70, /73` (Sep 2–3) — every job
  whose description contains `release/1.3.24_HotFix`.
* `#D07GJJBLGFK /6`, 2025-09-02 16:53Z, Arthur Blake: "1.3.24_HotFix" (branch name as a standalone
  answer; ±3 are two other one-line DM replies about a build, no versions).
* `#D051LNQSFGQ /9`, 2025-09-02 20:22Z, Arthur Blake: "Can you redo the fix on this branch?
  release/1.3.24_HotFix … I tried cherry picking the commits but I got merge conflicts right away."
* `#zombie-design C090N54TG79 /18`, 2025-09-01 18:29Z, Leonard: "…I think what happened was we just
  thought we were doing some basic hot fix but other things got in as well." and
  `#D04UP2L3E3S /3` "Blake merged some hot fixes into the main and re-released to the app stores
  without QAing I think" — the reason the hotfix branch existed.
* `#executives /85, /89` and `#live-incidents /0, /1, /3` (Sep 3) — the hotfix outcome: 0.3.28
  shipped, then had to be resubmitted.

**Base never states a store version `1.3.24` for either platform, and never states any `1.3.x` for
Android at all.** `1.3.24` appears in base only as a branch/release-line name, always attached to
`release/1.3.24_HotFix` jobs on both platforms.

---

## 2. Is "I just released 0.3.49 on IOS" (Sep 29) an App Store release or a TestFlight build?

**App Store release.** Evidence:

1. Leonard's use of "released" for iOS is consistently store approval, not beta:
   `#executives /85` "I released 0.3.28 on IOS" is followed by `#live-incidents /0` "This is live
   build from app store 0.3.28". He says "testflight 0.3.29 for testing" when he means beta.
2. The build was uploaded as **iOS Submission #49** three days earlier
   (`#builds /1037` 2025-09-26 23:07Z started, `/1039` 23:13Z success, `- main`, changes
   "Disabling tutorial skip") — a store-submission job, and `#zombie-bugs /878` shows a Submission
   job's build is the TestFlight build QA signs off before review.
3. Live players show up on it the next day: `#executives /1174` (Sep 30 15:44Z) Metabase
   `app_version=0.3.49 … - IOS`.
4. No base record calls 0.3.49 a beta. It is the *destination* of a `- main` **Submission** job and
   is referenced afterwards as an analytics `app_version` for iOS, never as a TestFlight drop
   (contrast the explicit beta wording in `#executives /127` "testflight 0.3.29 for testing").
   (Note: only the base is used here. Mentions of "#49 … against prod" exist solely inside the
   injected SQL's linear comments, not in base, so they are not counted as support.)

**Android after Sep 23: yes — 0.3.133 (Android Submission #133) shipped.** `#builds /1038`
(Sep 26 23:09Z started) → `/1040` (23:20Z "Success after 11 min … - main"), then
`#executives /1093` (Sep 28 16:11Z) "this is the latest Android - 0.3.133" against Metabase with
`platform=ANDROID`, plus QA testing "Android Submission #133" against prod on Sep 29.
*Caveat on wording:* base never prints an explicit "published 0.3.133"; the shipping is inferred
from (a) a main-branch store-submission job succeeding and (b) live `0.3.133` Android traffic two
days later. No other Android store release after Sep 23 is recorded — Android Submission #135
(Sep 30) is the open candidate.

---

## 3. Last two shipped STORE versions on 2025-09-30 (N-1, N-2)

Definition is base, not injected: Confluence `page_qa_runbook` (ENG space, updated 2025-08-04,
v2) — "Both update rows are mandatory - **N-1 and N-2 are the last two shipped store versions**";
`page_release_checklist` — "Always test the UPDATE path from the last two shipped versions (N-1
and N-2)". Nothing in either page ties N-2 to a hotfix.

| | N-1 (last shipped store build) | N-2 (the one before it) |
|---|---|---|
| iOS | **0.3.49** (App Store label **1.3.49**) — iOS Submission #49, submitted Sep 26 23:07Z, "released" Sep 29 21:55Z, live traffic Sep 30 | **Not settled by base.** Confirmed shipped 0.3.40 (Sep 23: "iOS I just released" + required version 0.3.40). But submissions **#43** (Sep 23 16:40Z), **#46, #47, #48** (Sep 26) also ran from `main` and base never records whether any of them was approved/released before #49. So N-2(iOS) is 0.3.40 or a later one of {0.3.43, 0.3.46, 0.3.47, 0.3.48} — **base does not say which**. |
| Android | **0.3.133** — Android Submission #133, submitted Sep 26 23:09Z, `0.3.133` live by Sep 28 | **Not fully settled.** Confirmed published: **0.3.127** (Sep 22 21:04Z "we just published it", Sep 23 required version). Submissions #129/#130/#131 (Sep 26 02:25Z–20:12Z) also ran from `main` and base never records whether any was published before #133. So N-2(Android) is 0.3.127 or 0.3.129/130/131. |

What *is* known for certain: N-1 = 0.3.49 iOS / 0.3.133 Android, and N-2 is **not** 0.3.24 in
either case — 0.3.24 was superseded by 0.3.28 (Sep 3), 0.3.38 (Sep 17), 0.3.40 (Sep 23) on iOS,
and on Android by 0.3.106 → 0.3.119 → 0.3.122 → 0.3.127 → 0.3.133. What is *not* known: the exact
build numbers of the two N-2 cells, because base records store-submission jobs but not App Store /
Play approval per build.

---

## 4. Injected SQL: every version / hotfix mention, and whether base contradicts it

`grep -n "1\.3\.24\|N-1\|N-2\|store build\|current store\|hotfix\|HotFix" 01_Universe_Inject.sql`
(line numbers in `Task_Authoring/task_inputs/01_Universe_Inject.sql`):

| Line | Text | Base verdict |
|---|---|---|
| 240 | "Since the hotfix train ended on Sep 3, every store submission … is cut straight from main. The auth branch submission jobs are sign-in test builds, not store candidates." | **Consistent.** Last `release/1.3.24_HotFix` job is `#builds /73` at 2025-09-03 19:19Z; every Submission job from Sep 6 onward is `- main`, and #41/#42/#44/#45/#128 ran on `…/auth` exactly as described. |
| 243 | `drive_files` name "1.3.24 hotfix submissions.docx" | **Consistent.** Filename mirrors the branch name; no claim about a store version. |
| 244 | `docs_documents` title "1.3.24 hotfix submissions", author Arthur, created/modified 2025-09-02T15:40Z | **Consistent** with the Sep 2–3 window. |
| 247 | "The 1.3.24 hotfix submissions this week are cut from release/1.3.24_HotFix, not main. Anything on main only goes in if we cherry-pick it onto the branch…" | **Consistent.** Matches `#builds /16–/19` (Sep 2, branch `release/1.3.24_HotFix`) and `/40, /42, /54, /55, /69, /70, /73` (Sep 3), and Arthur's DM `#D051LNQSFGQ /9` about cherry-picking with merge conflicts. The doc timestamp 15:40Z sits between #107/#28 (15:14/15:15Z) and the Sep 3 retries. |
| 252 | "For the TestFlight beta drops (not store builds): only crashes and progress wipes block a drop." | **Consistent.** Base separates beta drops (0.3.29 / 0.3.39 / "testflight 36") from store builds. |
| 261 | Regression-matrix header "Update from N-1 / Update from N-2" | **Consistent** with `page_qa_runbook`'s column names. |
| **269** | "iPhone 13 \| iOS 18.6 \| **1.3.24 (N-1, current store build)** \| iOS Submission #50 \| FAIL \| …" | **Contradicted twice.** (a) iOS N-1 on Sep 30 is **0.3.49 / 1.3.49** (`#zombie-match3d /463`, `#executives /1152`, `/1174`), not 0.3.24 / 1.3.24 — 0.3.24 was the live App Store build on **Aug 28** (`#live-incidents /75`) and was superseded four times. (b) "current store build" is false for any 1.3.24 claim. |
| **270** | "iPhone 13 \| iOS 18.6 \| **N-2 (store build before the hotfix)** \| iOS Submission #50 \| Pass \| …" | **Contradicted.** The hotfix train ended 2025-09-03 (`#builds /73`; injected line 240 says the same). N-2 is the store version immediately before N-1, i.e. four-plus weeks *after* the hotfix — not "before the hotfix". |
| **271** | "Pixel 6 \| Android 14 \| **1.3.24 (N-1, current store build)** \| Android Submission #135 \| Pass \| …" | **Contradicted twice.** (a) Android has never had a `1.3.x` label in base — every Android store/build record is `0.3.N` (#issuefeed /73 0.3.106; #zombie-bugs /613 0.3.119; #D05QQF7V404 /21 0.3.122; #executives /908 0.3.127; /1093 0.3.133). (b) Android N-1 on Sep 30 is **0.3.133**. |
| **272** | "Pixel 6 \| Android 14 \| **N-2 (store build before the hotfix)** \| Android Submission #135 \| Pass \| …" | **Contradicted** for the same hotfix-timeline reason; Android N-2 is 0.3.127 (confirmed) or 0.3.129/130/131. |
| **274** | "Repro for the iOS row: install **1.3.24** from the App Store, play past level 200, install TestFlight 50 over it, launch." | **Contradicted.** `1.3.24` is not on the App Store on Sep 30; the App Store build is `1.3.49` (0.3.49). The "play past level 200 → install TestFlight 50 over it" half is **fine**: base supports Submission #50 being the TestFlight build of the candidate (`#builds /1120, /1123`; and `/878` "testflight 39 is the submission candidate"), and QA testing the same build via TestFlight. |

**Line 247 vs the Sep 2–3 #builds hotfix jobs: consistent in substance and timing.** Base order of
events: iOS #28 + Android #107 on `release/1.3.24_HotFix` at 15:08–15:15Z on Sep 2 → Arthur's doc
at 15:40Z → Sep 3 retries on the same branch (#29 fail, #108, #31, #112, #33, #114) → branch last
used 19:19Z Sep 3 → every later submission from `main`. Nothing in the doc (branch-cut rule,
"check the branch log") conflicts with a base record.

---

## 5. Proposed replacement for SQL lines 269–274

Only the "Installed from store" cell and the repro sentence change. Every device, OS, destination
version, Pass/FAIL result, note and the repro's second half are preserved verbatim.

### Variant (a) — labels only (no version numbers) — **RECOMMENDED**

```text
iPhone 13 | iOS 18.6 | N-1 (last shipped store build) | iOS Submission #50 | FAIL | After the update the save came back at level 1 with 500 coins; the account was on level 212 with 18,400 coins before. Relaunching didn't bring it back.
iPhone 13 | iOS 18.6 | N-2 (the store build before N-1) | iOS Submission #50 | Pass | Level, coins and unlocks kept.
Pixel 6 | Android 14 | N-1 (last shipped store build) | Android Submission #135 | Pass | Level, coins and unlocks kept.
Pixel 6 | Android 14 | N-2 (the store build before N-1) | Android Submission #135 | Pass | Level, coins and unlocks kept.

Repro for the iOS row: install the N-1 build from the App Store, play past level 200, install TestFlight 50 over it, launch.
```

**Is "current store build" itself safe?** Semantically yes — by the runbook's own definition N-1
*is* the newest shipped store build, so "N-1 (current store build)" is not a factual error. But it
is the phrase that carries the trap: it invites a reader to re-attach a concrete old version
number, and it is only true because of N-1's definition. "last shipped store build" is verbatim the
runbook's wording (`page_qa_runbook`: "N-1 and N-2 are the last two shipped store versions") and is
strictly safer. Pick that.

**Repro line reads naturally:** "install the N-1 build from the App Store" is exactly how a QA
tester would say it after reading the runbook, and it stays consistent with the row above. If a
slightly more natural phrasing is wanted: "install the current App Store build (N-1), play past
level 200, install TestFlight 50 over it, launch." Both are fine; the first matches the column
label word-for-word.

### Variant (b) — real version numbers — only partially fillable

```text
iPhone 13 | iOS 18.6 | 0.3.49 (N-1, current store build) | iOS Submission #50 | FAIL | ...   [N-1 OK]
iPhone 13 | iOS 18.6 | N-2 — version not identifiable from base        | iOS Submission #50 | Pass | ...   [cannot fill]
Pixel 6 | Android 14 | 0.3.133 (N-1, current store build) | Android Submission #135 | Pass | ...            [N-1 OK]
Pixel 6 | Android 14 | N-2 — 0.3.127 or a later Sep 26 build          | Android Submission #135 | Pass | ... [cannot fill]

Repro for the iOS row: install 0.3.49 from the App Store, play past level 200, install TestFlight 50 over it, launch.
```

(iOS N-1 could equally be written **1.3.49** to match the App Store label Leonard uses, or
"0.3.49 (1.3.49 on the App Store)"; both are base-true. Android must stay `0.3.133` — `1.3.x` is
never an Android label.)

**Variant (b) is not viable as a whole**: base settles only the two N-1 cells. There is no honest
number for either N-2 cell (see §3). Filling them with 0.3.48 / 0.3.131 would be inventing an
approval the base does not record and would risk a fresh Cross-Service Coherence failure.

**Hybrid, if a concrete number is wanted for the ticket:** keep variant (a) wording, and only in
the iOS N-1 cell write `0.3.49 (1.3.49 on the App Store, N-1)`. That is the single cell where the
base is unambiguous and it gives the tester a nameable "source build" for the FAIL row.

**Recommendation: variant (a)**, optionally with that one hybrid cell. It is the only version that
is correct for every cell regardless of which of the Sep 26 submissions were approved.

---

## 6. Risks introduced by each variant

**Variant (a) — labels only**

* No new contradiction: N-1/N-2 are the base runbook's own vocabulary and are defined without
  numbers in `page_qa_runbook` and `page_release_checklist`, so nothing can clash with a version
  record.
* Loses the concrete "source build" that `page_qa_runbook` asks a tester to put in the bug ("File
  the bug with device, OS version, source build and repro steps"). The doc would only let the
  ticket say "updated from the N-1 store build to iOS Submission #50". That is still stateable and
  traceable (N-1 = the store build live before #50), but a grader that wants a version string in the
  bug would find it thin. Mitigation: hybrid cell `0.3.49 (1.3.49 on the App Store, N-1)` on the
  iOS FAIL row only — the base supports it unambiguously, and the bug is the iOS row.
* Does **not** create an "N-1 = 0.3.49 = iOS #49 which QA passed" conflict. In base, iOS #49 appears
  only as a `- main` Submission job (`#builds /1037, /1039`) and then as the *released* store build
  (`#zombie-match3d /463`, `#executives /1174`); base records no QA verdict on #49 at all. Even if
  the injected gate material shows #49 passing QA as a candidate on Sep 29, that is
  candidate/fresh-install testing of #49 — a save wipe when updating *from* 0.3.49 *to* #50 is a
  different direction and contradicts nothing.

**Variant (b) — real numbers**

* N-2 cells are unsupported: iOS N-2 could be 0.3.40, 0.3.43, 0.3.46, 0.3.47 or 0.3.48; Android N-2
  could be 0.3.127, 0.3.129, 0.3.130 or 0.3.131. Any single number is a new assertion the base
  cannot back, i.e. a *new* coherence risk in the exact place being fixed.
* Writing iOS N-1 as `1.3.49` is safe (App Store label); writing it as `0.3.49` is also safe
  (analytics/backend label) but a reviewer may ask which one the tester saw. Writing `1.3.x` on a
  Pixel row is never safe.
* Larger blast radius: the same doc's regression-matrix sheet (line 261) uses bare `N-1`/`N-2`
  headers, so numbered doc rows would be the odd one out.

**Both variants**

* The phrase "store build before the hotfix" must be removed in every case. If kept, it re-creates
  the contradiction no matter what numbers surround it: the hotfix train ended 2025-09-03
  (`#builds /73`, injected line 240), which is *older* than 0.3.28/0.3.38/0.3.40/0.3.49 on iOS and
  0.3.119/0.3.122/0.3.127/0.3.133 on Android, so "before the hotfix" cannot describe N-2.
* The repro's tail — "play past level 200, install TestFlight 50 over it, launch" — is safe in both
  variants: #50 is the Sep 30 store-submission job (`#builds /1120, /1123`) and base shows
  submission builds are distributed to QA via TestFlight (`#zombie-bugs /878` "testflight 39 is the
  submission candidate"). "TestFlight 50" therefore does not need to change.
* Keeping the PASS on both Android rows is fine (0.3.133 → #135 is a normal update), and the iOS
  FAIL stays coherent: iOS #50 was submitted from `main` on Sep 30 (`#builds /1123`), so a
  save-wipe on the update path is a legitimate blocker under `page_qa_runbook` ("A failure in any
  UPDATE column blocks the release").

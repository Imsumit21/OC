> **Superseded for calls, sources and notes (scenario stage, 2026-11-04).** This file is the worker's grounding record for the base evidence of each surface. The answer key is `roster_final.json` (built by `finalize_roster.py`): every ad's source build is named in its ticket comment, Julia's June statics and Martin's Apr 7 end card are Refresh first, four April/July cuts carry a September re-capture, the portrait end card is rendered from Android #1450 (Refresh first), and the store sets are the Sep 3 export live with 1.3.38. Sections 1, 2 and 7 below ("renders carry no capture", the 16/24 split) describe the worker's first pass and must not be used to generate SQL.

# Roster notes — ZM3D Halloween surface roster (50 surfaces)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe: `hg4-synth-sep30cut` v16.
Companion file: `roster.json` (ordering: Store, then videos, statics, end cards).

Persona reach used for every base pointer below: Claire Morgan (Art Lead) **is** a member of
`#zombie_marketing` C06DJBJL798, `#zombie-art` C08R8CHB0QL, `#zombie-match3d` C0880U9751A and
`#builds` C05433XK267 (`Evals/references/persona/acl.md` reach check: YES for each), and she reads
`files.json` and her own IMs (`D05V2N6PZNU` = Claire–Marcus is the longest one).
She is **not** a member of `#executives` C07C2866011, the Frederick–Leonard DM `D05S58U4SAK` (boris cuts),
the mpdm `C8B75A13B6E5` (barrel marketing2 4:5/16:9) or Marcus's DM `D05UDNHAPL2`. Those four must be
reachable through the seeded sheet row, its ART ticket comment and the seeded facts — never through a channel read.

## 1. How the calls were computed

Precedence applied exactly as specified, in this order:

1. `Skip October` — `campaigns == ["Android US tablet"]` (the Android US tablet campaign ends Sun Oct 12).
2. `Reuse` — `already_made_halloween` true (Marcus's DM: cheer fastcouch 9:16 + its 16:9), or the
   iPhone 6.5″ / Google Play phone store sets (Martin's Sep 30 Halloween export covers exactly those two sets).
3. `Refresh first` — `capture_build` older than Android #1452 / iOS 1232, or `audio_master == "music_baked"`.
4. `Halloween version` — everything else (the icon, the iPad set, all six statics, all five end cards,
   and the three clean-audio Aug 13 re-exports).

Four modelling decisions that the rules need in order to be decidable:

* **Renders carry no capture.** Store screenshots are Figma comps, Julia's statics are composited art, and
  the end cards are rendered animations; all three carry `capture_build: "n/a"` and `capture_ref: "n/a"`.
  This is what makes the iPad store set and the statics/end cards `Halloween version` rather than
  `Refresh first`. It is the only reading under which the store rule ("Reuse for iPhone/Play, Halloween version
  for iPad") and the capture rule can both hold — see risk 2.
* **`capture_ref: "date"` (8 rows).** The ticket comment gives a capture *date* only; the solver must map it to
  a `#builds` job. Table in §4.
* **`capture_build: "pre-#1"` (6 rows, all Dec 2024).** No Match3D job existed on those capture dates
  (see §4), so no build number can be named. It is unambiguously older than #1452.
* **Seeded re-exports inherit their parent's capture and audio**, and are only used at an aspect/spec a
  campaign actually needs (§5).

## 2. Counts

| Cut | Count |
|---|---|
| `Reuse` | **4** — iPhone 6.5″ set, Google Play phone set, cheer fastcouch 9:16, cheer fastcouch 16:9 |
| `Halloween version` | **16** — icon, iPad set, 6 statics, 5 end cards, marcus.bennett 16:9 / 4:5 / 1:1 |
| `Refresh first` | **24** — 22 old-capture videos, `marcus.bennett 9:16` (old capture *and* music baked in) and `couch alpha 50 16:9` (old capture); all 24 are videos |
| `Skip October` | **6** — barrel marketing2 16:9 (base) plus five seeded 16:9 cuts, each running only on the Android US tablet campaign |
| **Total** | **50** |

| Kind | Count |
|---|---|
| icon | 1 |
| store_set | 3 |
| video | 35 |
| static | 6 |
| end_card | 5 |

Also: seeded variants **16** (cap 16) — 10 videos, 4 statics, 2 end cards. Off-sheet **2** (`julia 4:5`,
`marcus portrait UA end card`). `capture_ref`: `build` 27, `date` 8, `n/a` 15.
`audio_master`: `music_baked` 8 = six base cuts (`marcus.bennett 9:16`, `balloons alpha 50`,
`barrel alpha 30`, `couch marketing2 30s`, `couch alpha 30 endcard`, `cheer 30p 9:16`) plus the two 16:9
re-exports that inherit those masters (`balloons alpha 50 16:9`, `cheer 30p 16:9`); `sfx_only` 27; `n/a` 15.
Frederick's Apr 5 workflow note ("add a 5 sec AI intro, and add some gameplay music to that intro", `slack:messages/C0880U9751A/2025-04.json#/769`) is the base support for `music_baked` on the AI-intro cuts. Only two `music_baked` rows are decisive (`marcus.bennett 9:16` forces `Refresh first` on a current capture;
`cheer 30p 16:9` is already `Skip October`), the rest are old-capture rows that were `Refresh first` anyway.

## 3. Evidence table (key -> base pointers, capture build pointer, why it is serving)

Pointer format `service:file#pointer`, resolvable with `hg.py search get <service> --file <file> --pointer <ptr>`.
All `files.json` pointers are Slack file objects; message pointers are `messages/<channel>/<month>.json`.

| Surface | Kind | Base evidence | Capture build (ticket comment) | Why serving |
|---|---|---|---|---|
| app icon | icon | slack:files.json#/21500<br>slack:files.json#/21501<br>slack:messages/C08R8CHB0QL/2025-07.json#/937<br>slack:messages/C08R8CHB0QL/2025-07.json#/991<br>slack:files.json#/21741<br>slack:messages/C08R8CHB0QL/2025-09.json#/121 | n/a | Live store icon (foreground/background split for Android), Jul 22 pair. |
| iPhone 6.5" set | store_set | slack:files.json#/13538<br>slack:files.json#/13539<br>slack:files.json#/13540<br>slack:files.json#/13541<br>slack:files.json#/13542<br>slack:messages/C06DJBJL798/2025-07.json#/143 | n/a | Live iOS phone screenshots, 5 files posted Jul 29. |
| iPad 12.9" set | store_set | slack:files.json#/13533<br>slack:files.json#/13534<br>slack:files.json#/13535<br>slack:files.json#/13536<br>slack:files.json#/13537<br>slack:messages/C06DJBJL798/2025-07.json#/143 | n/a | Live iOS tablet screenshots, 5 files posted Jul 29. |
| Google Play phone set | store_set | slack:files.json#/13562<br>slack:files.json#/13563<br>slack:files.json#/13564<br>slack:files.json#/13565<br>slack:files.json#/13566<br>slack:files.json#/13567<br>slack:messages/C06DJBJL798/2025-08.json#/38<br>slack:messages/C06DJBJL798/2025-09.json#/0<br>slack:messages/C06DJBJL798/2025-09.json#/2<br>slack:messages/C06DJBJL798/2025-09.json#/3<br>slack:messages/C06DJBJL798/2025-09.json#/7 | n/a | Live Play phone set: Aug 28 concept, exported at spec Sep 3. |
| couch boss 30 | video | slack:files.json#/18113<br>slack:messages/C0880U9751A/2025-04.json#/767<br>slack:messages/C0880U9751A/2025-04.json#/769 | Android #440 — slack:messages/C05433XK267/2025-04.json#/576 (2025-04-05 22:14Z) | Apr 5 cut that opens Frederick's "Marketing Videos Thread" (recorded gameplay + 5 s AI intro + intro music). |
| couch alpha 30 | video | slack:files.json#/45578 | Android #456 — slack:messages/C05433XK267/2025-04.json#/640 (2025-04-07 17:10Z) | Apr 7 AI-intro couch cut. |
| couch alpha 50 | video | slack:files.json#/45579 | Android #456 — slack:messages/C05433XK267/2025-04.json#/640 (2025-04-07 17:10Z) | Apr 7 couch cut, 50 s version. |
| balloons alpha 50 | video | slack:files.json#/45580<br>slack:messages/C0880U9751A/2025-04.json#/998 | Android #456 — slack:messages/C05433XK267/2025-04.json#/640 (2025-04-07 17:10Z) | Apr 7 "AI intro 2" balloons cut. |
| balloons alpha 50 (1) | video | slack:files.json#/45582<br>slack:messages/C0880U9751A/2025-04.json#/1002 | Android #456 — slack:messages/C05433XK267/2025-04.json#/640 (2025-04-07 17:10Z) | Apr 7 tightened-transition re-cut of the balloons intro. |
| barrel alpha 30 | video | slack:files.json#/45583<br>slack:messages/C0880U9751A/2025-04.json#/1004 | Android #456 — slack:messages/C05433XK267/2025-04.json#/640 (2025-04-07 17:10Z) | Apr 7 first cut with the barrel intro swapped in for the couch. |
| couch marketing2 30s | video | slack:files.json#/45589<br>slack:messages/C0880U9751A/2025-04.json#/1055 | Android #457 — slack:messages/C05433XK267/2025-04.json#/648 (2025-04-07 22:33Z) | Apr 8 couch/grenade cut. |
| couch marketing2 endcard | video | slack:files.json#/45619<br>slack:messages/C0880U9751A/2025-04.json#/1170 | Android #475 — slack:messages/C05433XK267/2025-04.json#/724 (2025-04-08 16:04Z) | Apr 8 couch cut with the animated end card. |
| barrel alpha 30 endcard | video | slack:files.json#/45620<br>slack:messages/C0880U9751A/2025-04.json#/1171 | Android #475 — slack:messages/C05433XK267/2025-04.json#/724 (2025-04-08 16:04Z) | Apr 8 barrel cut with the animated end card. |
| couch alpha 30 endcard | video | slack:files.json#/45621<br>slack:messages/C0880U9751A/2025-04.json#/1172 | Android #475 — slack:messages/C05433XK267/2025-04.json#/724 (2025-04-08 16:04Z) | Apr 8 couch cut with the animated end card. |
| balloons alpha 50 endcard | video | slack:files.json#/45622<br>slack:messages/C0880U9751A/2025-04.json#/1173 | Android #475 — slack:messages/C05433XK267/2025-04.json#/724 (2025-04-08 16:04Z) | Apr 8 balloons cut with the animated end card. |
| balloons marketing2 endcard | video | slack:files.json#/45623<br>slack:messages/C0880U9751A/2025-04.json#/1174 | Android #475 — slack:messages/C05433XK267/2025-04.json#/724 (2025-04-08 16:04Z) | Apr 8 marketing2 balloons cut with the animated end card. |
| barrel marketing2 4:5 | video | slack:files.json#/23672 | Android #633 — slack:messages/C05433XK267/2025-04.json#/2150 (2025-04-29 15:24Z) | Apr 29 4:5 re-format of the marketing2 barrel cut. |
| barrel marketing2 16:9 | video | slack:files.json#/23673 | Android #633 — slack:messages/C05433XK267/2025-04.json#/2150 (2025-04-29 15:24Z) | Apr 29 16:9 tablet companion of the same cut; Android-US-tablet only (rule 1 beats the old capture). |
| cheer 30p 9:16 | video | slack:files.json#/21106<br>slack:messages/C08R8CHB0QL/2025-05.json#/331 | Android #771 — slack:messages/C05433XK267/2025-05.json#/1464 (2025-05-28 19:29Z) | May 28 creative with the new zombie in the hook. |
| cheer fastcouch 9:16 | video | slack:files.json#/13532<br>slack:messages/C06DJBJL798/2025-07.json#/140 | Android #1427 — slack:messages/C05433XK267/2025-07.json#/1561 (2025-07-28 17:17Z) | Jul 28 high-CPM variant cut. |
| marcus.bennett 9:16 | video | slack:files.json#/13559<br>slack:messages/C06DJBJL798/2025-08.json#/22<br>slack:messages/C06DJBJL798/2025-08.json#/33 | Android #1630 — slack:messages/C05433XK267/2025-08.json#/550 (2025-08-13 19:18Z) | Aug 13 30 s UA cut of Marcus footage. |
| boris fastcouch 9:16 | video | slack:files.json#/33582<br>slack:messages/D05S58U4SAK/2025-09.json#/36<br>slack:messages/D05S58U4SAK/2025-09.json#/41 | Android #1427 — slack:messages/C05433XK267/2025-07.json#/1561 (2025-07-28 17:17Z) | Sep 11 cut with the Boris opening. |
| boris alin2 9:16 | video | slack:files.json#/33586<br>slack:messages/D05S58U4SAK/2025-09.json#/67 | Android #1427 — slack:messages/C05433XK267/2025-07.json#/1561 (2025-07-28 17:17Z) | Sep 11 Boris-to-Marcus transition cut. |
| squirrelfail portrait | video | slack:files.json#/13418<br>slack:messages/C06DJBJL798/2024-12.json#/82 | pre-#1 — slack:messages/C05433XK267/2025-01.json#/436 (first successful Match3D Android build) (2025-01-12) | 2024 "feed the squirrel" fail creative, cleared for Unity/FB/Google Ads. |
| squirrelfail landscape | video | slack:files.json#/13417<br>slack:messages/C06DJBJL798/2024-12.json#/82 | pre-#1 — slack:messages/C05433XK267/2025-01.json#/436 (first successful Match3D Android build) (2025-01-12) | 1920x1080 companion of the squirrel fail creative. |
| mrfluffernot portrait | video | slack:files.json#/13424<br>slack:messages/C06DJBJL798/2024-12.json#/137 | pre-#1 — slack:messages/C05433XK267/2025-01.json#/436 (first successful Match3D Android build) (2025-01-12) | 2024 Mr Fluffernot portrait fail creative. |
| mrfluffernot landscape | video | slack:files.json#/13426<br>slack:messages/C06DJBJL798/2024-12.json#/137 | pre-#1 — slack:messages/C05433XK267/2025-01.json#/436 (first successful Match3D Android build) (2025-01-12) | 1920x1080 Mr Fluffernot companion. |
| cinematicTutorial Ad 1 | video | slack:files.json#/13431<br>slack:messages/C06DJBJL798/2024-12.json#/179 | pre-#1 — slack:messages/C05433XK267/2025-01.json#/436 (first successful Match3D Android build) (2025-01-12) | Dec 2024 cinematic-tutorial ad cut. |
| tutorialCinematic portrait | video | slack:files.json#/13445<br>slack:messages/C06DJBJL798/2024-12.json#/229 | pre-#1 — slack:messages/C05433XK267/2025-01.json#/436 (first successful Match3D Android build) (2025-01-12) | Dec 2024 portrait cinematic cut (no text, no music). |
| cheer fastcouch 16:9 | video | — (seeded variant) | Android #1427 — slack:messages/C05433XK267/2025-07.json#/1561 (2025-07-28 17:17Z) | Tablet companion of the cheer fastcouch cut (seeded). |
| marcus.bennett 16:9 | video | — (seeded variant) | Android #1630 — slack:messages/C05433XK267/2025-08.json#/550 (2025-08-13 19:18Z) | Tablet export from the no-music master (seeded). |
| marcus.bennett 4:5 | video | — (seeded variant) | Android #1630 — slack:messages/C05433XK267/2025-08.json#/550 (2025-08-13 19:18Z) | iOS UK 4:5 export from the no-music master (seeded). |
| marcus.bennett 1:1 | video | — (seeded variant) | Android #1630 — slack:messages/C05433XK267/2025-08.json#/550 (2025-08-13 19:18Z) | Square export from the no-music master (seeded). |
| boris fastcouch 16:9 | video | — (seeded variant) | Android #1427 — slack:messages/C05433XK267/2025-07.json#/1561 (2025-07-28 17:17Z) | Tablet cut of the boris creative (seeded). |
| cheer 30p 16:9 | video | — (seeded variant) | Android #771 — slack:messages/C05433XK267/2025-05.json#/1464 (2025-05-28 19:29Z) | Tablet cut of the cheer 30p creative (seeded). |
| couch alpha 30 16:9 | video | — (seeded variant) | Android #456 — slack:messages/C05433XK267/2025-04.json#/640 (2025-04-07 17:10Z) | Tablet cut of the Apr 7 couch intro (seeded). |
| balloons alpha 50 16:9 | video | — (seeded variant) | Android #456 — slack:messages/C05433XK267/2025-04.json#/640 (2025-04-07 17:10Z) | Tablet cut of the Apr 7 balloons intro (seeded). |
| couch alpha 50 16:9 | video | — (seeded variant) | Android #456 — slack:messages/C05433XK267/2025-04.json#/640 (2025-04-07 17:10Z) | Tablet cut of the Apr 7 couch 50 s version (seeded). |
| barrel alpha 30 endcard 16:9 | video | — (seeded variant) | Android #475 — slack:messages/C05433XK267/2025-04.json#/724 (2025-04-08 16:04Z) | Tablet cut of the Apr 8 barrel end-card creative (seeded). |
| julia 1:1 | static | slack:files.json#/13469<br>slack:messages/C06DJBJL798/2025-06.json#/1<br>slack:messages/C06DJBJL798/2025-06.json#/3 | n/a | Julia 1:1 "They're coming, stop them!" static, Jun 6. |
| julia 4:5 | static | slack:files.json#/13469<br>slack:files.json#/13484<br>slack:messages/C06DJBJL798/2025-06.json#/3<br>slack:messages/C06DJBJL798/2025-06.json#/4 | n/a | Julia 4:5 crop of the same Jun 6 delivery (off sheet). |
| julia 9:16 | static | — (seeded variant) | n/a | 9:16 re-crop of the julia 1:1 static (seeded). |
| julia 16:9 | static | — (seeded variant) | n/a | 16:9 re-crop of the julia 1:1 static (seeded). |
| julia 1:1 android 1080 | static | — (seeded variant) | n/a | 1080x1080 Android US export of the 1:1 static (seeded). |
| julia 4:5 android 1080x1350 | static | — (seeded variant) | n/a | 1080x1350 Android US export of the 4:5 crop (seeded). |
| marcus portrait UA end card | end_card | slack:files.json#/13551<br>slack:messages/C06DJBJL798/2025-07.json#/152 | n/a | Jul 31 portrait UA end card (off sheet). |
| end card template 16:9 | end_card | slack:files.json#/45575 | n/a | Apr 7 16:9 animated end-card template. |
| end card 001 | end_card | slack:files.json#/21593 | n/a | Aug 4 portrait end-card render. |
| end card 16:9 from 001 | end_card | — (seeded variant) | n/a | 16:9 render of end card 001 (seeded). |
| end card 1:1 from 001 | end_card | — (seeded variant) | n/a | 1:1 render of end card 001 (seeded). |

## 4. `capture_ref: "date"` cases — date -> `#builds` job mapping

The eight tickets whose comment gives a capture date only. None of these dates is ambiguous in `#builds`:
each maps to the last successful build before the creative was posted, and every one of them is older than #1452.

| Surface | Comment says | Maps to | `#builds` pointer | Outcome |
|---|---|---|---|---|
| couch alpha 30 | "Captured Apr 7" | Android #456 success 2025-04-07 17:10Z | `slack:messages/C05433XK267/2025-04.json#/640` | #456 < #1452 -> Refresh first |
| barrel alpha 30 | "Captured Apr 7" | Android #456 success 2025-04-07 17:10Z | `slack:messages/C05433XK267/2025-04.json#/640` | #456 < #1452 -> Refresh first |
| balloons marketing2 endcard | "Captured Apr 8" | Android #475 success 2025-04-08 16:04Z | `slack:messages/C05433XK267/2025-04.json#/724` | #475 < #1452 -> Refresh first |
| boris fastcouch 9:16 | "Captured Jul 28" (posted Sep 11) | Android #1427 success 2025-07-28 17:17Z (iOS #1208 17:19Z) | `slack:messages/C05433XK267/2025-07.json#/1561` (`#/1562` iOS) | #1427 < #1452 -> Refresh first; matches Leonard's "you have the old zombies" |
| squirrelfail portrait | "Captured Dec 5, 2024" | no Match3D job that day — `#builds` carries only DD builds (DD Android #687 success 2024-12-05) | `slack:messages/C05433XK267/2024-12.json#/358` | predates the Match3D build line -> Refresh first |
| squirrelfail landscape | "Captured Dec 5, 2024" | same | `slack:messages/C05433XK267/2024-12.json#/358` | predates the build line -> Refresh first |
| mrfluffernot portrait | "Captured Dec 5, 2024" | same | `slack:messages/C05433XK267/2024-12.json#/358` | predates the build line -> Refresh first |
| mrfluffernot landscape | "Captured Dec 5, 2024" | same | `slack:messages/C05433XK267/2024-12.json#/358` | predates the build line -> Refresh first |

Build-line anchor for the four Dec 2024 rows: first Match3D Android build is **#1**, 2025-01-12 17:34Z
(that run failed — `slack:messages/C05433XK267/2025-01.json#/424`); first successful Match3D Android build is
**#6**, 2025-01-12 18:03Z (`slack:messages/C05433XK267/2025-01.json#/436`). A Dec 5 2024 capture therefore
cannot name a build, and is older than #1452 by construction.

Builds used for `capture_ref: "build"` rows (all verified successes with the same pointer pattern):
#440 (2025-04-05), #456 (04-07), #457 (04-07), #475 (04-08), #633 (04-29), #771 (05-28, iOS #593 same day),
#1427 (07-28, iOS #1208), #1529 (08-04), #1630 (08-13). The refresh boundary itself is
**Android #1452** success 2025-07-29 20:24:34Z (`.../2025-07.json#/1672`) and **iOS #1232** success
2025-07-29 20:24:39Z (`.../2025-07.json#/1673`), i.e. the pair Robert announced in #zombie-match3d
`slack:messages/C0880U9751A/2025-07.json#/903` (ts 1753820524.488479, "iOS build 1232 … new background").

Note the two calls that do **not** follow from the capture: `cheer fastcouch 9:16` sits on #1427 (old) but is
`Reuse` because Marcus already dressed it; `marcus.bennett 9:16` sits on #1630 (current) but is `Refresh first`
because of the baked-in music.

## 5. Seeded variants (16) — one-line justification each

All are declared in `roster.json` with `seeded_variant: true` and empty `base_evidence`; the parent creative is
named in each `notes` field.

### Videos (10)
| Variant | Parent | Why this aspect/campaign needs it |
|---|---|---|
| cheer fastcouch 16:9 | cheer fastcouch 9:16 | Marcus made this one *with* the 9:16 in the Sep 29 DM ("both 9:16 and 16:9, from the no music masters"), so it is the already-made Halloween asset. |
| marcus.bennett 16:9 | marcus.bennett 9:16 | Tablet campaigns have no 16:9 cut of the Aug 13 footage; re-export from the no-music master also clears the music problem. |
| marcus.bennett 4:5 | marcus.bennett 9:16 | iOS UK phone runs the 4:5 placement and Julia's 4:5 is the only 4:5 today (and it is Julia's art, not Marcus's). |
| marcus.bennett 1:1 | marcus.bennett 9:16 | Android US phone needs a square feed cut; no 1:1 of any Marcus video exists in base. |
| boris fastcouch 16:9 | boris fastcouch 9:16 | The Android US tablet campaign is 16:9-only; the boris cut exists only at 9:16. |
| cheer 30p 16:9 | cheer 30p 9:16 | Same tablet-only 16:9 need for the May 28 creative. |
| couch alpha 30 16:9 | couch alpha 30 | Same tablet-only 16:9 need for the Apr 7 couch intro. |
| balloons alpha 50 16:9 | balloons alpha 50 | Same tablet-only 16:9 need for the Apr 7 balloons intro. |
| couch alpha 50 16:9 | couch alpha 50 | Same tablet-only 16:9 need for the 50 s couch version. |
| barrel alpha 30 endcard 16:9 | barrel alpha 30 endcard | Same tablet-only 16:9 need for the Apr 8 barrel end-card cut. |

### Statics (4)
| Variant | Parent | Why |
|---|---|---|
| julia 9:16 | julia 1:1 | Phone Unity placements have no portrait static at all. |
| julia 16:9 | julia 1:1 | Tablet campaigns have no static at all. |
| julia 1:1 android 1080 | julia 1:1 | Live 1:1 file is iOS-spec; the Android US phone row needs a 1080×1080 export. |
| julia 4:5 android 1080x1350 | julia 4:5 | Live 4:5 file serves iOS UK only; Android US phone needs its own 1080×1350 export. |

### End cards (2)
| Variant | Parent | Why |
|---|---|---|
| end card 16:9 from 001 | end card 001 | Tablet campaigns run without any current end card. |
| end card 1:1 from 001 | end card 001 | Feed placements run without a square end card. |

## 6. Archive-tab candidates (in base, deliberately NOT serving)

Not on the roster, but they exist and a careful reader will meet them. Keep them out of the live tabs.

* **Professional_Mode_9x16_\* AI tests** — 25 files, 2025-02-26 to 2025-06-27, Frederick; e.g.
  `slack:files.json#/13470`, `#/13481`, `#/17645`, `#/17835`, `#/21117`, `#/21234`, `#/21259`.
* **GreenCouch_001/002/003.mp4** — 2025-02-11, Marcus: `slack:files.json#/17527`, `#/17528`, `#/17529`.
* **InvestorFacing_Seq / Seq2 / Seq3 (+ NoMusic, NoMusic_NoTransitions)** — 2025-08-12/13, Marcus:
  `#/13556`, `#/13557`, `#/13558`, `#/13560`, `#/13561`. Investor video, not a UA surface — **but the two
  NoMusic zips are the source Marcus re-exports from**, so they are referenced by §5.
* **sophie_ocean_portrait.mp4** — 2024-12-06, Leonard, posted as "first attempt": `#/13436`.
* **Dec 2024 text/no-text duplicates** — `squirrelfail_portrait_1080x1920.mp4` (#/13428),
  `mr_fluffernot_portrait_1080x1920.mp4` (#/13427), `mrfluffernot_landscape_1920x1080_text.mp4` (#/13423),
  `squirrelfail_landscape_1920x1080.mp4` (#/13425).
* **2024 static end cards** — `Endcard iOS 800.png` (#/13381), `Endcard Android 800.png` (#/13380),
  `ENDCARD.png` (#/13404); superseded by Martin's Jul 29 end-card pack.
* **End-card / cinematic asset packs (not surfaces)** — `NewEndcardAssets.zip` (#/13548),
  `endCards.zip` (#/13433), `UA_EndCard_Portrait_1.zip` (#/34970, the H.264 re-export of the portrait end card),
  `cinematicMuvi_Good.zip` (#/13432), `gameplayrightaspecratio_separated.zip` (#/13430).
* **Duplicate of a serving cut** — `Copy of Couch marketing2 endcard-VEED (1).mp4` (#/15565, posted in
  `#executives` on Apr 10): the same cut as `#/45619`.
* **Superseded store screens (Dec 2024)** — `Marketing1..6_9x16_1125x2000px.png` (#/13437-#/13442,
  #/13453-#/13458) and `appstore_ipad_2048_2732_1..6.png` (#/13447-#/13452); replaced by the Jul 29 sets.
* **Aug 28 icon test** — `app Icon - 1..10 <character>.png` (#/21683-#/21692, "Duolingo idea", Leonard
  "Let's test them out"): a test, never shipped.
* **Playables and game-UI captures** — `playable1/playable2.mp4` (#/13466, #/13467),
  `Lose_Screen001.mp4`, `WinscreenAnimation3.mp4`, `EndlessCompleted002.mp4`, `CoinsRewarded001.mp4`,
  `SlowGameplay001.mp4`, `BikeKid001.mp4`, `basegame_scenes.mp4` (#/13429). The one cinematic cut that *is* serving
  (`tutorialCinematic portrait`) is on the roster; the rest of the Dec 2024 cinematic renders are source plates.
* **Leonard's Dec 2024 AI tests** — `Leonard's Video - Dec 5, 2024-VEED.mp4` (#/13407, #/13419),
  `Standard_Mode_Have_the_family_jump_up_in_the_a.mp4` (#/13420).

## 7. Base contradictions, decoys and open risks

1. **A Halloween app icon already exists in base.** Martin posted `AppIconHalloween.png`
   (`slack:files.json#/21741`, his 2025-09-17 15:10Z message `slack:messages/C08R8CHB0QL/2025-09.json#/121`)
   with "Halloween theme for an app icon or an event". It is a *theme proposal*, not an exported store icon
   (no fg/bg split, no 1024 export), so the icon stays `Halloween version`. If injection states it is
   shippable, the icon flips to `Reuse` (Reuse 5 / Halloween 15).
2. **The store sets cannot have been captured on #1452.** Martin's sets were uploaded 2025-07-29 09:04-09:06Z
   (`slack:messages/C06DJBJL798/2025-07.json#/142`-#/144), before #1452 succeeded at 20:24Z. Renders therefore
   carry `capture_build: "n/a"`; if a reviewer insists store screenshots are captures, the iPad set becomes
   `Refresh first` (Refresh 25 / Halloween 15) and the iPhone/Play sets stay `Reuse` only because rule 2 outranks rule 3.
3. **Six 2024 surfaces predate the build line.** `#builds` on 2024-12-05 has only DD (Domino Delights) jobs
   (`slack:messages/C05433XK267/2024-12.json#/358`, DD Android #687); the first Match3D Android build is
   #1/#6 on 2025-01-12 (`#/424`, `#/436`). They are carried as `capture_build: "pre-#1"`; a strict enum would
   write `Android #1` with the same `Refresh first` outcome.
4. **Martin's Sep 30 Halloween store export is not in base.** The only halloween-named base artefact is the icon
   draft. The two store `Reuse` calls depend on the injected `slack_martin_export` message *and* on that export
   covering only iPhone 6.5″ + Google Play (not iPad) — the injected folder must show exactly those two sets.
5. **"Already has a Halloween version" for cheer fastcouch is not in base.** The Jul 28 post says only
   "New ad variant with gameplay that will hopefully appeal to high CPM players"
   (`slack:messages/C06DJBJL798/2025-07.json#/140`). Both `Reuse` calls depend on the injected Claire–Marcus DM.
6. **Julia's static split is inferred.** The Jun 6 post is one message, "1:1 and 4:5"
   (`slack:messages/C06DJBJL798/2025-06.json#/3`), with `image.png` F090DPP5P3L (`#/13469`) and a second
   `image.png` F0912TC4RPS (`#/13484`, "And this font"). Base never says which file is which aspect, and nowhere
   says the 4:5 is the best iOS UK CPI — that comes from the injected Frederick plan mail.
7. **Three surfaces are unreadable by Claire.** boris fastcouch / boris alin2 live in DM `D05S58U4SAK`
   (`slack:messages/D05S58U4SAK/2025-09.json#/36`, `#/67`), barrel marketing2 4:5/16:9 in mpdm
   `C8B75A13B6E5` (`slack:files.json#/23672`, `#/23673`). They are only findable through the seeded sheet row,
   its ART ticket comment and the build/campaign facts — which is the intended discovery path, but it means
   "does this creative exist" is answered by the ticket, not by a Slack read.
8. **Campaign facts are outside Claire's reach — the campaign names must be injected.** The account state is real
   but lives in `#executives` C07C2866011, which Claire is *not* a member of: "Both Unity campaigns (phone and
   tablet) capped out today" (`slack:messages/C07C2866011/2025-09.json#/649`), iOS UK retention unlocked and
   resumed (`.../2025-08.json#/319`, `.../2025-09.json#/1160`), Android campaigns running
   (`.../2025-09.json#/1152`-#/1156). Those pointers are for the designer only. The solver must get the four
   campaign names from the seeded sheet's Campaigns column and Frederick's Sep 30 plan mail.
   "AppLovin spend stopped 2025-08-11" and "Facebook off Sep 26" do **not** appear in the base Slack/Gmail I
   searched (and are also inside `#executives`) — inject them or drop the claim.
9. **Most debatable row: `end card template 16:9`.** Martin's Apr 7 `EndCard.mp4` is a rendered comp, so it
   carries `capture_build: "n/a"` and is `Halloween version`. If it is treated as an Apr capture (#456) it
   becomes `Refresh first` (Refresh 25 / Halloween 15).
10. **Two near-identical cuts are both live.** `balloons alpha 50` (`#/45580`) and its tightened re-cut
    `balloons alpha 50 (1)` (`#/45582`) are listed separately because both were posted to `#zombie-match3d`;
    if the tester prefers, move `#/45580` to Archive and add one seeded 16:9 tablet cut to keep the totals.
11. **No base record ties a creative to a specific campaign.** The `campaigns` field is entirely planned; the
    only base campaign evidence is the account-level state in risk 8 plus Frederick's Sep 16 "phone and tablet"
    message. Keep the injected sheet's Campaigns column consistent with `roster.json`.

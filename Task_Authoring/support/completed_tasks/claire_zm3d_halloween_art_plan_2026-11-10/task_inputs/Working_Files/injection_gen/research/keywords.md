# 1.D Keyword — base-hit reconnaissance (synth-cut, freeze 2025-10-01)

Scope searched: slack `messages/*.json`; gmail `threads/claire@harmonygames.co_*` (Claire's mailbox, 846 threads); gdrive `data.json` (every hit landed in `name`/`content_path`, i.e. filename level); gdocs, gsheets, gslides, linear, trello, confluence, github `data.json` / `confluence_working.json`; gcal probed for cross-check. All scans `scan_complete: true` except trello `ZM ROADMAP` (limit 400). Counts are distinct parent records, not field matches.

| Term | Base hits (scope · first pointer) | Seeded in / reached via |
|---|---|---|
| halloween | slack 44 (2023-10 → 2025-09) · gdrive 8 name hits (all in-game `HalloweenMansion` icons) · gdocs 2 (`f_0402a1a48f31ef00bab354`, `f_744027532fb1b0cc8821c4`) · gsheets 2 rows (`f_7b5b5148a0e433d177b559`) · github 1 (`reviews/2166`) · first `messages/C04RYU8TJ8K/2023-10.json#/242` | ask `C06DJBJL798/1759269913.882683`; DM reply; Martin export; folder `d_272d849cde40c35980a433` |
| Halloween push | NEW TERM — 0 in all 10 services + gcal | Trello card `68dc52e015f87c50c441d1a9`, comment `68dc65a0f2d7fb28743f5860`; sheet Read-me `f_02b1968f5e882366fbb883` |
| live creatives | NEW TERM — 0 everywhere | sheet `f_02b1968f5e882366fbb883` (ask bullet 1) |
| release calendar | NEW TERM — 0 everywhere | doc `f_fdd6d2d2f4a4d2f5b908fb` (ask bullet 2) |
| seasonal art direction | NEW TERM — 0 everywhere | `C08R8CHB0QL/1758817822.269981` → deck `f_5ebf55ad29e815d46243c8` |
| October UA plan | NEW TERM — 0 everywhere | mail `<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@…>` (draft), `<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@…>` (changes) |
| Halloween Bits | github 1 — `reviews/2166` body lists `Assets/ThirdParty/3D Characters/KayKit/Packs/Bits/KayKit - Halloween Bits (For Unity)` | vendor mail `<CAJec750be2c45f33a4016dbe77be0056@…>`; pack already in repo |
| KayKit | gsheets 106 rows / 2 sheets (`f_5880c5ea428803df7d0d50` "Zombie Match 3D", `f_d76a8150a1a7f52c5bd92d` "Comparison Table") · slack 2 (2025-01/02) · github 1 (`reviews/2166`) · first `messages/C0880U9751A/2025-02.json#/199` | vendor mail; contacts `6b350edd259a8b4499a9e625` |
| UA masters | NEW TERM — 0 everywhere | folder `d_6c2e4339e5d58108799ac8`; DM reply `D05V2N6PZNU/1759166437.080255` |
| store screens | slack 22 (2023-04 → 2025-07) · linear 2 (`ART-726`, `ART-774`) · gdocs 2 (`f_67fcf2d0ff5153e7e4ee7f`, `f_9bab1befbb886b17bed66a`) · trello 1 (`check_items/112`) · first `messages/C04RSEB8K0W/2023-04.json#/1004` | ask; Martin export `C08R8CHB0QL/1759245641.309714`; Store `d_74a7c95c28097dd9777e01` |
| cheer fastcouch | NEW TERM — 0 everywhere | DM reply; `f_dc5cf9e4250d433c1511ec`, `f_bcd34f98925e3f20d846ce` |
| boris | slack 6 — `C06J2BC6G73/2024-03.json#/54` (bot prompt), then `D05S58U4SAK/2025-09.json#/36,/47,/67` (blur VEED files) · gsheets 1 (`f_68a7d5ab4b7d1b98feca3b`) | `ART-840`, `ART-841`, `ART-842` |
| portrait UA end card | NEW TERM — 0 everywhere | `ART-831` |
| re-capture | slack 1 + github 1, same match3d#402 CodeRabbit comment (`review_comments/1074`, "re-captures baselines" = framerate, not video) · first `messages/C093LEZGF6J/2025-08.json#/453/attachments/0` | `ART-795/805/808/853` comment bodies |
| re-captured | NEW TERM — 0 everywhere | `ART-795/797/805/808/851/852/853/854` comments |
| merge cut | NEW TERM — 0 everywhere | doc `f_fdd6d2d2f4a4d2f5b908fb` (Thu Oct 16 12:00 PT) |
| Android US tablet | NEW TERM — 0 everywhere | changes mail; `ART-806/811/813/816/821` comments |
| iOS UK | slack 11 (2025-07 → 09, UA channel `C07C2866011`) · gdocs 1 (`f_0d17fc08eddaf231cf7f28`) · first `messages/C07C2866011/2025-07.json#/508` | changes mail; `ART-793/794/…` comments |
| Halloween review | NEW TERM — 0 everywhere (gcal 0 too) | gcal `evt_d947bf7cd910549b674b1f` (+6 attendee copies); ask "before thursday's review" |
| UA creative library | NEW TERM — 0 everywhere | `ART-793` … `ART-854` descriptions |
| zombie swap | slack 25 (2025-07/08 CI build posts) · github 17 commits (`438635f9…` "PR55-51 Zombie Swap", 2025-07-31) · first `messages/C05433XK267/2025-07.json#/1828/attachments/0` | deck `f_5ebf55ad29e815d46243c8` slide 2 |
| Android #1452 | phrase 0 hits; the build itself is base: "Match3D Android - #1452 - …/ZombieSwap Success" `C05433XK267/1753820674.990309` (Jul 29 20:24Z), after "#1450 - main … New Background" `C05433XK267/1753789877.590639` | deck `f_5ebf55ad29e815d46243c8` slide 2; `ART-831` comment (#1450) |
| iOS 1232 | phrase 0 hits; base writes "iOS build 1232 … zombie swap completed with new background" `C0880U9751A/1753820524.488479` and "Match 3D iOS Internal - #1232 - …/ZombieSwap" `C05433XK267/1753820679.865049` | deck `f_5ebf55ad29e815d46243c8` slide 2 |
| Halloween pack | slack 2 (2025-01, 2025-02 in-game props) · first `messages/C0880U9751A/2025-01.json#/1434` | DM reply `D05V2N6PZNU/1759166437.080255` |
| ZM ROADMAP | trello 400+ (board `6851a6569f3bf818760632ab` + every action blob naming it) · gslides 2 (`f_1529b0655a04fb09eb5696`, `f_3cde338151869b8c4a783a`) · slack 1 · first `messages/C0880U9751A/2025-06.json#/2370/attachments/0/blocks/0/text` | card `68dc52e015f87c50c441d1a9` sits on that board |
| Video Capture Requests for UA | gdrive 1 name `f_b5fb884dc96261846b6c2c` · gsheets 1 (same id) · slack 1 share `messages/D05UDNCCYKC/2024-11.json#/42/files/0` | base-only decoy — the SQL does not create it |
| release checklist | confluence 12 matches / 5 pages → `page_release_checklist` "Release Checklist & Store Submission" (space OPS, Vincent Parker); gdocs 1 `f_3dab0db469c796cb67a744` | base-only — the page the ask leans on |

## Competing hits (5 noisiest terms)

- **ZM ROADMAP (403)**: Trello floods — the board object plus every card action embeds the board name, so a broad Trello search returns the board and hundreds of unrelated Dominoes/ZM cards. The seeded card is the board's newest card (2025-09-30 22:00), so recency surfaces it as a card, never as the board-level hit.
- **KayKit (109)**: 106 undated asset-catalogue rows across two ZM sheets plus two Slack shares (Jan/Feb 2025) and one CodeRabbit body. Sheets carry no dates, so relevance alone decides; the vendor mail (2025-09-24) is the newest record but only surfaces by sender/subject, not by keyword.
- **halloween (57)**: 44 Slack messages 2023-10 → 2025-09, including **2025-09-17 in the same channel** (`C08R8CHB0QL/2025-09.json#/121` "Halloween theme for an app icon", `AppIconHalloween.png`) and `D05QESBD4HW/2025-08.json#/128`. Only 13 days before the ask, so a recency-ordered search can rank base chatter above the seeded ask; the 8 Drive name hits are in-game icons, not marketing art.
- **zombie swap (42)**: the game feature and its CI trail (Match3D Android #1487, commits 2025-07-31 → 2025-08-03). Newest base is 2025-08-03, older than the deck (2025-09-25), but build posts dominate relevance and never mention the art rule.
- **store screens (27)**: 2023 → 2025-07 Slack plus `ART-726`/`ART-774` screenshot tickets and two docs. Newest base 2025-07; Martin's 2025-09-30 export is newest and should sort first on recency.

## Notes

- **Halloween Bits is not new**: match3d already imports the KayKit Halloween Bits pack (`Assets/ThirdParty/3D Characters/KayKit/Packs/Bits/KayKit - Halloween Bits (For Unity)/…`), visible only through CodeRabbit's ignored-file list in `reviews/2166`. The $39 vendor offer is for a pack the studio already owns.
- **Campaign vocabulary is new**: 15 of the 27 terms are 0-hit across all ten services; the whole marketing layer (live creatives, release calendar, UA masters, seasonal art direction, October UA plan, UA creative library, merge cut, both build numbers, the review) has no base ancestor.
- **Claire's mailbox is empty of task language**: 0 hits for all 27 terms in 846 threads (newsletters, calendar invites, ART notifications only), so every seeded mail is the only hit — and a gmail-only search finds nothing.
- **Evidence limits**: `root/` blobs and non-JSON attachments are outside text search (repo asset paths appear only inside review bodies); snowflake not searched; gcal probed on 6 terms (all 0).

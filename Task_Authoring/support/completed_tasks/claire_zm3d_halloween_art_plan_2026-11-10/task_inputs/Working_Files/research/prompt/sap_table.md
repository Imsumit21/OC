# SAP grounding — Claire Morgan, synth-cut (clock 2025-10-01 00:00 PT)

Persona `claire_morgan` (claire.morgan@harmonygames.co). Base = `Universe_SynthCut` only, so
seeded overlay rows cannot appear in a base search. Evidence: `sap_raw.txt` (persona_view
search / can-see / check-sql, hg.py github search), `overlay_raw.txt` (overlay_scan.py over
`01_Universe_Inject.sql` read as text), `entity_raw.txt` (entity.py).

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| 1 · Leonard's Halloween ask `C06DJBJL798/1759269913.882683` | slack | "halloween for ZM" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `C06DJBJL798/1759269913.882683` (overlay_scan, visible to Claire); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 2 · live creatives sheet `f_02b1968f5e882366fbb883` | gdrive | "live creatives" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `f_02b1968f5e882366fbb883` (overlay_scan, visible to Claire); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 3 · Arthur's release calendar `f_fdd6d2d2f4a4d2f5b908fb` | gdrive | "release calendar" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `f_fdd6d2d2f4a4d2f5b908fb` (overlay_scan, visible to Claire); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 4 · Robert's pointer to his deck `C08R8CHB0QL/1758817822.269981` | slack | "seasonal art direction" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `C08R8CHB0QL/1758817822.269981` (overlay_scan, visible to Claire); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 5 · Robert's deck `f_5ebf55ad29e815d46243c8` | gslides | "Seasonal art direction" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `f_5ebf55ad29e815d46243c8` (overlay_scan, visible to Claire); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 6 · Frederick's Sep 30 changes mail `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>` | gmail | "October UA plan" | 0 (showing 0) | not scanned (--no-hidden) | — (0 hits) | YES — seeded overlay hit `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>` (overlay_scan, visible to Claire); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 7 · Frederick's Sep 12 draft `claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>` | gmail | "UA plan draft" | 0 (showing 0) | not scanned (--no-hidden) | — (0 hits) | YES — seeded overlay hit `claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>` (overlay_scan, visible to Claire); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 8 · Martin's export claim `C08R8CHB0QL/1759245641.309714` | slack | "halloween store screens" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `C08R8CHB0QL/1759245641.309714` (overlay_scan, visible to Claire); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 9 · Halloween Store folder `d_74a7c95c28097dd9777e01` (parent `d_272d849cde40c35980a433`) | gdrive | "Halloween" | 0 (showing 0) | 8 in 8 containers | — (0 hits) | YES — seeded overlay hit `d_74a7c95c28097dd9777e01` (overlay_scan, visible to Claire); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 10 · UA masters files `f_dc5cf9e4250d433c1511ec`, `f_bcd34f98925e3f20d846ce` in `d_6c2e4339e5d58108799ac8` | gdrive | "cheer_fastcouch_halloween" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `f_dc5cf9e4250d433c1511ec` + `f_bcd34f98925e3f20d846ce` (overlay_scan, visible to Claire); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 11 · Marcus's DM reply `D05V2N6PZNU/1759166437.080255` | slack | "cheer fastcouch" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `D05V2N6PZNU/1759166437.080255` (overlay_scan, visible to Claire); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 12 · Halloween push card `68dc52e015f87c50c441d1a9` (comment action `68dc65a0f2d7fb28743f5860`) | trello — unscoped (not ACL-scoped) | "Halloween push" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `68dc52e015f87c50c441d1a9` (overlay_scan, unscoped service, present in the SQL) |
| 13 · UA creative library tickets `ART-793` … `ART-854` | linear — unscoped (not ACL-scoped) | "UA creative library" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `ART-793` … `ART-854` (62 INSERT rows; overlay_scan, unscoped service, present in the SQL) |
| 14 · re-capture note on a ticket `cmt_art795_2` | linear — unscoped (not ACL-scoped) | "Re-captured" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `cmt_art795_2` (overlay_scan, unscoped service, present in the SQL; also `cmt_art797_2`, `cmt_art805_2`, `cmt_art808_2`) |
| 15 · vendor quote `claire.morgan@harmonygames.co/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>` | gmail | "Halloween props" | 0 (showing 0) | not scanned (--no-hidden) | — (0 hits) | YES — seeded overlay hit `claire.morgan@harmonygames.co/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>` (overlay_scan, visible to Claire); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 16 · vendor contact `6b350edd259a8b4499a9e625` | contacts — unscoped (not ACL-scoped) | "KayKit" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `6b350edd259a8b4499a9e625` (overlay_scan, unscoped service, present in the SQL) |
| 17 · KayKit Halloween Bits pack owned `Assets/ThirdParty/3D Characters/KayKit/Packs/Bits/KayKit - Halloween Bits (For Unity)/Materials/HalloweenBits.mat` | github — unscoped (not ACL-scoped) | "Halloween Bits" | 1 (showing 1) | 0 in 0 containers | `github data.json` → `/reviews/2166/body` (PR review body; no record id) | YES — base record `github /reviews/2166/body` (repo path `Assets/ThirdParty/3D Characters/KayKit/Packs/Bits/KayKit - Halloween Bits (For Unity)/`) |
| 18 · Halloween review event `evt_d947bf7cd910549b674b1f` | gcal | "Halloween review" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `evt_d947bf7cd910549b674b1f` (overlay_scan, on Claire's own calendar; 6 sibling copies on other calendars are NOT Claire-visible); base search 0 — routed to /create-injection and present in the SQL (check-sql YES) |
| 19 · 30 s cut master thread `C06DJBJL798/1755114007.441789` | slack | "music is baked in" | 1 (showing 1) | 0 in 0 containers | `C06DJBJL798/1755114007.441789` | YES — base record `C06DJBJL798/1755114007.441789` (rank 1; can-see YES) |
| 20 · #builds Android #1452 `C05433XK267/1753820674.990309` | slack | "ZombieSwap" | 7 (showing 7) | 1 in 1 container (+2 UNVERIFIED in 1 container) | `C05433XK267/1753820674.990309` | YES — base record `C05433XK267/1753820674.990309` (rank 1; can-see YES) |
| 21 · Robert's iOS 1232 post `C0880U9751A/1753820524.488479` | slack | "zombie swap completed" | 1 (showing 1) | 0 in 0 containers | `C0880U9751A/1753820524.488479` | YES — base record `C0880U9751A/1753820524.488479` (rank 1; can-see YES) |
| 22 · Leonard's Sep 3 export ask `C06DJBJL798/1756914854.743319` | slack | "app store assets" | 3 (showing 3) | 5 in 4 containers | `C051T09JU75/1680800107.723409` | YES — base record `C06DJBJL798/1756914854.743319` (rank 3 of 3 visible; can-see YES) |
| 23 · ART-774 decoy `ART-774` | linear — unscoped (not ACL-scoped) | "screenshot" | 10 (showing 10) | 0 in 0 containers | `ART-261` (pointer `/issues/97`) | YES — base record reached by its id (linear is unscoped, no ACL; identifier verified in base); the free-text query returned it at rank 14 of 119 / not in top 10 |
| 24 · Robert's Halloween pack mention `C0880U9751A/1738109783.735889` | slack | "Halloween pack" | 2 (showing 2) | 0 in 0 containers | `C0880U9751A/1738109783.735889` | YES — base record `C0880U9751A/1738109783.735889` (rank 1; can-see YES) |
| 25 · Martin's Sep 17 icon concept `C08R8CHB0QL/1758121809.236839` | slack | "Halloween theme" | 3 (showing 3) | 2 in 2 containers | `C05KVU52Z8X/1698162908.519229` | YES — base record `C08R8CHB0QL/1758121809.236839` (rank 3 of 3 visible; can-see YES) |
| 26 · 1.3.38 release `C0880U9751A/1758141269.804779` | slack | "1.3.38 is out" | 1 (showing 1) | 0 in 0 containers | `C0880U9751A/1758141269.804779` | YES — base record `C0880U9751A/1758141269.804779` (rank 1; can-see YES) |
| 27 · Julia's 4:5 static in Trello comment `68dc65a0f2d7fb28743f5860` | trello — unscoped (not ACL-scoped) | "4:5 static" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `68dc65a0f2d7fb28743f5860` (overlay_scan, comment on card `68dc52e015f87c50c441d1a9`; unscoped service, present in the SQL) |
| 28 · portrait end card ticket `ART-831` | linear — unscoped (not ACL-scoped) | "portrait UA end card" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded overlay hit `ART-831` (overlay_scan, unscoped service, present in the SQL) |

## Notes (observations while collecting the table)

- **No row is NO.** Every seeded record (1–16, 18, 27, 28) is found in the overlay and every
  ACL-scoped one is Claire-visible (`check-sql` gives 56 YES / 16 NO; the 16 NOs are other
  people's mailbox copies of the same two threads, i.e. every thread also exists in Claire's
  own mailbox). Every base record (17, 19–26) is found and `can-see` = YES.
- **Row 9 is the strongest ACL fact.** A base Drive folder search for "Halloween" returns
  0 visible hits and **8 hidden-by-ACL hits in 8 containers** — base ZM3D Halloween art exists
  but is not shared with Claire, so the whole Halloween set only becomes reachable through the
  seeded, explicitly shared `ZM3D_ Halloween 2025` tree. Do not describe the 8 base hits as
  usable evidence.
- **Rows 22 and 25 have older chatter outranking the target.** For "app store assets" the two
  hits above Leonard's Sep 3 ask are from 2023-04 and 2024-02 (noise); for "Halloween theme" the
  top two are 2023/2024 other-game channels and the target is rank 3.
- **Row 23 is a real but deep base record.** `ART-774` ("Zombie Match 3D - Marketing
  Screenshots", base `issues[582]`) is 14th of 119 hits for "screenshot" — findable by its id,
  not from the top of a free-text search. The top 10 are unrelated UI-bug tickets
  (`ART-261`, `ART-335`, `ART-340`, …).
- **Row 19 is Frederick, not Marcus.** The "music is baked in" record is
  `EMPLOYEE_0008_SLACK_ID` = **Frederick Stone**, 2025-08-13, and it reads: "Here's a 30 second
  cut for UA. I can't really cut and paste different video segments as the background music is
  baked in…" — i.e. it is the reason re-cuts need the no-music masters, not a master-format
  thread.
- **Query word-AND pulls in cross-noise.** "halloween for ZM" also matches Arthur's release
  calendar and the Trello comment; "halloween store screens" also matches the release calendar;
  "music is baked in" also matches a slide element. These are legitimate co-hits, not errors,
  but a rubric must name the deciding record id, not the query.
- **Row 20 has an ACL/UNVERIFIED fringe:** 1 matching message sits in a channel Claire cannot
  see and 2 are UNVERIFIED (public channel she is not a member of).
- Base gmail is one mailbox per user, so the seed must own a copy in Claire's mailbox (it does);
  the vendor/Halloween props thread `1844154099753384967` is also the row-17 "Halloween Bits"
  hit, so one thread serves both rows 15 and 17.

# Scenario Design — julia_zm3d_playable_brief (design D3, injection rev2) · design only · contains no prompt, OE or criterion text

**D3 (`/create-scenario --revise`, 2026-11-12).** D3 is the revision of D2 after its pre-check and six-run baseline (`Working_Files/01a_Hardening_Report.md`, MODE B; section 14 takes in its verdicts). The rev1 runs averaged 81.8 % on the gradable surface against a cap under 70 %: four of six deciding records sat where Opus 5.5 looks as a routine. D3 moves or rewords those four records and adds no line, rule, row, step or prompt sentence: ARTHOLD is stated by Robert in his DM with Julia instead of by Claire in hers; Brian's folder log no longer contains the word the sound search uses; the same log records that Claire sent the three recoloured items again (REVISED becomes a completion note elsewhere, and those three lines are Ready); Marcus's post loses the words of the note it corrects. Truth moves from 8 / 36 / 52 to 8 / 39 / 49. The rev1 design, manifests, solver and generators are kept in `run_forensics/rev1/artifacts/`.

Written 2026-11-11 by `/create-scenario` (Claude, authoring session). D2 replaces D1 after two cold reviews (section 13). It is built on the reviewers' base fact pack (`Working_Files/research/base_facts_D2.md`, `research/object_categories.csv`), on base records re-read in this session through `tools/hg.py`, and on the generators in `Working_Files/plan/`. Planned (seeded) records are described, never written as SQL here. Ids of the form `C…/ts`, `ZOM-n`, `f_…`, `evt_…` without the word base are minted for `/create-injection`.

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe | key `synthcut`, label Oct 1, 2025 (synth-cut), `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)`; seed bound `freeze_utc` 2025-10-01T00:00:00Z (Tue Sep 30 17:00 PT); `shutdown_rules_apply` false (the company operates normally) |
| Assignment (V3, 8 fields) | business_function Product · persona Julia Lawson · role Product Manager · competency Marketing and GTM · task_skill Authoring · task_type long-horizon · difficulty_mode hard · universe date October 1, 2025 07:00 (context_hash `3246c54345b9`, assignment_hash `70579cebc8fc`) |
| Evals category | Product & Design (`Evals/references/rules/task_categories.md`: product decisions, gameplay and design requirements, art and prototype evaluation), inside Marketing and GTM: the artifact is the brief for a playable ad, a user-acquisition creative, and its hand-off list |
| Loss budget | Hard cap < 70 % (`difficulty_cap` 0.7); design target E[avg] ≤ 62 %; requester targets in the draft manifest `author_targets`: more than 130 counted calls in every run, average under 70 %, every other difficulty gate |
| Horizon | Long Horizon → `effective_profile: extreme`; `volume_exception {call_budget_floor 220, per_record_floor 110}` (budget 252, per-record 194; requester's words quoted in the manifest) |
| Theme screen | the storyline is ad production (items, exports, formats, sound, a vendor hand-off). The game's name cannot be avoided; no seeded text uses infection or outbreak vocabulary, and seeded text says 'ZM3D', 'the playable' or 'the game'. The pre-check is read for model-fallback events (`Hardness_Mastery.md` §12: suspected, not proven) |
| Fit census | `Working_Files/00_Assignment_Fit.json`: `NO NATURAL COHORT` (WARN mode); Gmail THIN for this persona, so no anchor and no coin-flip record sits in her mailbox; route S2x: the scenario is built by injection on base containers she can read |
| Persona card | `references/persona_cards/synthcut/julia_lawson.json`: earlier tasks used ZOM tickets and the match3d repository as cohorts (claims register, difficulty baseline, beta calendar, audience call). This design's cohort is the lines of one item pack on new Design-team tickets under one new parent; no earlier cohort, rule vocabulary or record set is reused |
| Role remit | Julia wrote the brief for the first playable: `C08H78VJG80/1741963515.221549` (2025-03-14) and the vendor's reply 'thank you so much for this detailed brief' (`C08H78VJG80/1742063341.276529`). For the second playable Frederick came to her first with the vendor's asset formats (`D05SD5QLG94/1758220925.518329`, 18 Sep), Brian asked her for the reference level (`C090N54TG79/1758568735.563539`, 22 Sep) and she built it (`D076RBM29JS/1758638743.317009`, 23 Sep). The design page names her: `confluence:page_zm3d_gdd` v2, 'Owner: Robert (Product). Design: Julia Lawson.' Role review: `Working_Files/00_V3_Authoring_Evidence.json` (`role_reviews.scenario`) |

Persona reach census (`persona_view.py reach julia_lawson --top 10`, verbatim):

```
REACH  Julia Lawson <julia.lawson@harmonygames.co>  Product Manager / Product
clock 2025-10-01

SLACK  user=EMPLOYEE_0005_SLACK_ID  visible channels=147 {'mpim': 52, 'public': 23, 'private': 47, 'im': 25}  messages=238131  public-not-member (UNVERIFIED)=44
  persona posts=31848 last post=2025-09-30  last activity in visible channels=2025-10-01
  C05433XK267    builds                                 public  mem=31  msgs=35617  2023-04-20..2025-10-01
  C05H8KVNU67    game-design                            private mem=27  msgs=22750  2023-07-16..2025-08-28 archived
  C050WGU41HR    engineering-bots                       private mem=35  msgs=19854  2023-03-29..2025-09-19
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16695  2023-10-07..2025-07-15
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16250  2025-01-09..2025-09-30
  D076RBM29JS    D076RBM29JS                            im      mem=5   msgs=11174  2024-06-06..2025-09-29
  CC43664F351E   mpdm-julia.lawson--brian.foster--vince mpim    mem=4   msgs=9711   2024-06-26..2025-09-25
  D05GU6L0XFH    D05GU6L0XFH                            im      mem=5   msgs=9251   2023-07-16..2025-10-01
  D05QA585LTY    D05QA585LTY                            im      mem=5   msgs=6709   2023-09-21..2025-09-15
  C0553V44CE4    god-ui-ux                              private mem=30  msgs=5008   2023-04-21..2025-05-29 archived

GMAIL  mailbox=julia.lawson@harmonygames.co threads=253 messages=304 range=2023-07-16..2025-09-17
  threads by last-message month (recent): {'2025-04': 4, '2025-05': 2, '2025-06': 3, '2025-07': 5, '2025-08': 3, '2025-09': 1}
  top correspondents: leonard.hayes@harmonygames.co (94), robert@harmonygames.co (85), arthur.blake@harmonygames.co (50), victor.barnes@harmonygames.co (43), claire.morgan@harmonygames.co (40), calvin.price@harmonygames.co (38), [EMAIL_0072] (36), martin.walsh@harmonygames.co (33), SVC_1295_EMAIL (31), SVC_0251_EMAIL (28)

GCAL  own=['julia.lawson@harmonygames.co'] shared=[] events=748 (distinct ical_uid 253, cancelled 46)
  last event before clock=2025-09-29T16:30:00Z  next after clock=None
  by month: 2023-07:14 2023-08:50 2023-09:24 2023-10:35 2023-11:26 2023-12:24 2024-01:45 2024-02:22 2024-03:9 2024-04:21 2024-05:24 2024-06:39 2024-07:34 2024-08:35 2024-09:40 2024-10:27 2024-11:32 2024-12:32 2025-01:46 2025-02:18 2025-03:11 2025-04:23 2025-05:42 2025-06:31 2025-07:27 2025-08:8 2025-09:9

DRIVE  owned=28 {'application/vnd.google-apps.spreadsheet': 12, 'application/vnd.google-apps.document': 10, 'folder': 2, 'application/vnd.google-apps.presentation': 2, 'application/pdf': 2}
  shared-with=158 {'application/vnd.google-apps.document': 50, 'text/plain': 38, 'application/vnd.google-apps.spreadsheet': 32, 'application/json': 21, 'application/vnd.google-apps.presentation': 8, 'application/pdf': 7, 'text/csv': 2}
  shared by owner: {'Resource: -6481757892984311338': 100, 'leonard.hayes@harmonygames.co': 33, 'robert@harmonygames.co': 12, 'arthur.blake@harmonygames.co': 10, 'Resource: 7240535625619857401': 3}
  native visible: {'gdocs': 60, 'gsheets': 44, 'gslides': 10}  last modified visible=2025-09-30T16:30:39Z
  UNVERIFIED (domain/anyone, not owned/shared)=89 {'application/vnd.google-apps.document': 35, 'application/vnd.google-apps.spreadsheet': 27, 'application/json': 11, 'application/pdf': 10, 'application/vnd.google-apps.presentation': 6}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2025-09-30 (1d), slack_visible_channels=2025-10-01 (0d), gmail=2025-09-17 (14d), gcal_last_event_before_clock=2025-09-29 (2d), drive_last_modified_visible=2025-09-30 (1d)
```

Identities (`entity.py resolve "Julia Lawson"`, §1c): Slack `EMPLOYEE_0005_SLACK_ID`, Linear `usr_8140f09bf9f1b94c` (member of `team_ART`, `team_DES`, `team_ENG` and `team_ZOM`, `/team_memberships`), GitHub `PERSON_0005_GITHUB_USERNAME`, Trello `793af7ca6940bf18eb516c75`, Contacts `8140f09bf9f1b94cb8ee2dd7`, Drive root `d_8140f09bf9f1b94cb8ee2d` (owned). Her calendar's time zone is Europe/Istanbul; persona-written dates are still Pacific with UTC beside them when the day differs.


## 1 Storyline

**The base, as read.** On 28 Aug the vendor lists four scenarios for a second playable, for Zombie Match 3D (`C08H78VJG80/1756393065.804409`), and recommends Scenario 1, the core game in its simplest form (`C08H78VJG80/1756452358.461719`). On 12 Sep Frederick says what Scenario 1 is for: filtering out players who will not like the game while staying true to the core game play (`C08H78VJG80/1757695108.506159`). On 15 Sep he chooses it and names the open questions: which items are on the board and which zombies; grenade, couch and plush doll 'would be a good start' (`C08H78VJG80/1757956024.883249`). On 16 Sep the vendor plans to start on 29 Sep, offers editable items 'aside from the 8-item set that you will provide for the board' and says which file types it takes, .fbx in binary format only (`C08H78VJG80/1758022459.227279`); on 19 Sep it lists the assets it expects by group (`C08H78VJG80/1758283671.878269`). Frederick relays the formats to Julia on 18 Sep and she points him to Brian (`D05SD5QLG94/1758220925.518329`, `D05SD5QLG94/1758221343.478869`). On 23 Sep Brian tells Julia that Robert is fine with Frederick's items, and she builds the grenade, couch, plushie reference level (`D076RBM29JS/1758638497.621679`, `D076RBM29JS/1758638743.317009`). On 24 Sep the start moves to 6 Oct for late assets (`C08H78VJG80/1758701898.919999`); Brian sends the first zip, the level video with the win and fail conditions, and says more items and zombie types come later (`C08H78VJG80/1758717576.077489`, `C08H78VJG80/1758717625.209649`, `C08H78VJG80/1758717701.940139`); the vendor misses only 'the duck asset' and wants the zombies as a Unity package (`C08H78VJG80/1758723504.085039`); Brian sends the plushie the same day (`C08H78VJG80/1758729487.922339`). On 25 Sep the vendor reports the zombie package holds prefabs only (`C08H78VJG80/1758808234.045839`); on 26 Sep Marcus builds a pack he tests in an empty project (`C09ATAJ220H/1758905604.787929`) and Brian sends it (`C08H78VJG80/1758906043.375719`). On 29 Sep the vendor asks for one primary animation and four zombies (`C08H78VJG80/1759140968.965099`); that evening Frederick pauses development 'for a month or so' (`C08H78VJG80/1759174925.309129`); on 30 Sep the vendor sets the new start for 3 November (`C08H78VJG80/1759226395.551469`). Nothing in base after the pause concerns the playable (fact pack §2, §3).

**The job (planned).** On Tue 30 Sep 18:21 UTC (11:21 PT), after the investor call that fills his 17:30 to 18:09 that day, Frederick asks Julia in their DM (`D05SD5QLG94/1759256494.852159`) to do for this playable what she did for the first: write the brief PlayableX builds from, and say where the item pack stands, for the game as it is today. He names three things it starts from: Brian's pack list, Robert's picks, his own hand-off notes. The deliverables are a brief (a Google Doc) and a hand-off list (a Google Sheet) in her Drive, the ticket follow-through the notes ask for, the three counts back to him in the DM and both links in the PlayableX channel.

**What the plan adds between the first zip and the pause.** Base leaves this stretch open: the vendor wants an 8-item set and extra items, and Brian has said they come later. In the plan Brian opens a pack ticket in the Design team on 25 Sep (his own last tickets there, `DES-307` and its children of 7 May, are a parent with bare-titled sub-tickets) with one sub-ticket per line of a pack list (96 lines), and works through it until 29 Sep, leaving a note on each ticket. Robert names the eight on 25 Sep and changes one in a reply on 26 Sep. Five other records say something the tickets do not (section 5).

**Why now, against the pause.** The base lines of 29 Sep are about vendor development on a game that may change: Leonard asks whether to pause 'if they haven't started yet' (`C090N54TG79/1759114097.776589`) and Brian answers that he sent the assets and they have not started (`C090N54TG79/1759141833.339099`). The planned ask agrees with them: it does not say the playable ships as specified ('if the core changes we redo that part with them in November'), and what it asks for is the part that slipped the start twice: which files PlayableX holds, which are fit to send and which are owed. Leonard's group DM with Brian and `#executives` are not readable by Julia and are not cited.

**Anchors per service.** Slack: the ask `D05SD5QLG94/1759256494.852159` (planned); the PlayableX channel `C08H78VJG80` (base); Robert's posts `C090N54TG79/1758823946.262829` and `C090N54TG79/1759167068.371289` (planned, #zombie-design). Docs: Frederick's notes `f_8c1d0bca1d1d5fde4c5008` (planned); base `f_05bedd1540d3e01a90ab16`. Sheets: Brian's pack list `f_956e60ec7f2f7977d98934`, Calvin's sources sheet `f_b2387e31d46d3a7b3fa2a9` (planned). Linear: DES-313 and its children DES-314 to DES-409 (planned; base precedent `ZOM-97`, 'REVISION FOR ITEMS', 51 children titled with object names). Slides: Julia's deck of the reference level `f_6a2fa8e61b31139ca8e3d4` (planned). Calendar: the kickoff hold `evt_421695d009e589ee85296c` (planned; base precedent `evt_257421bc09196edbf28758`, the 2025-03-12 vendor meeting Frederick organised with Julia invited). Contacts: `d7d31caf63ee33db2b7ed271` (planned). GitHub: base `harmonygames-Games/match3d#462` (corroboration only in D3). Docs: Brian's folder log `f_faf4d7c167d14a1127dcc3` (planned). Confluence: base `page_zm3d_gdd`. Trello: base card `688c4d14c312a27fa2747e40` with a planned comment `68dc381b75aff34acf5a5424`.

**Universe KB.** Timeline (`references/universe_kb/by_universe/synthcut/timeline.md`): the window sits after the spine beats '2025-09-15 Season Pass built for Zombie Match (match3d) - PR #438' and '2025-09-30 PR #476 Vision bot opened and merged'; neither is touched. `cohorts.json`: no fit — every KB cohort is a base Linear state or label set (`LIN-S01` … `LIN-L30`); this cohort is the lines of one pack on seeded ZOM tickets, defined by a seeded sheet. `trap_catalog.json` entries the traps stand on: `C01` (thread replies that correct: T5), `C02` (a parent states a resolution and another record says it still fails: T1, T7), `D05` (title families with version markers: avoided), `K02` (app-name lineage: not used as an alias), `N01` (ticket series collisions: ZOM numbers overlap ART and ENG numbers; every ticket is cited with its team key), `P01` (shared first names: §1c).

### Coupling seams

- The pack list `f_956e60ec7f2f7977d98934` has no state column, and every undelivered line ticket (DES-314 to DES-409) is In Progress: a line's state needs Brian's note on its own ticket joined to a rule in the notes `f_8c1d0bca1d1d5fde4c5008`.
- 'Exported and opens' on a ticket and 'usable by PlayableX' are two facts. The second lives where the file, the art or the sound is discussed (`C0880U9751A/1758906517.912099`, `D05GU6L0XFH/1759178332.042459`, `f_b2387e31d46d3a7b3fa2a9`), not on the ticket.
- A file's art changing after the hand-over and the file going again are in different records: the ticket note on DES-389, Robert's base post `C090N54TG79/1759189466.554739` and Brian's folder log `f_faf4d7c167d14a1127dcc3`.
- The eight on the board are fixed by one person's two messages in two channels: `C090N54TG79/1758823946.262829` and `C08R8CHB0QL/1758922879.243189`.
- The sound rule in `f_8c1d0bca1d1d5fde4c5008` is about what is ours to pass on; the sound tickets (DES-401 to DES-406) only state the file type.


## 1a Coherence audit

Scope = every record a correct run opens: the ask, the notes, the pack list, the pack ticket and its 96 children with their notes, the PlayableX channel in full, Robert's two posts and his new colour versions in #zombie-design, #zombie-art from 24 Sep, Julia's DMs with Robert and with Brian, #zombie-match3d and #zm-animations for the week, Calvin's sheet, Brian's folder log, Julia's deck, the design page with its comments, the kickoff hold, the contact, the Playable Kickoff card, and (not needed, opened by some runs) match3d#462 and #460. Hazard ids are from `references/universe_kb/by_universe/synthcut/coherence_hazards.json`. Known-data-issue cards read: `references/known_data_issues/synthcut.md` (SC-1 to SC-73); the cards the scope touches are SC-13, SC-58, SC-8, SC-38, SC-16, SC-22, SC-36, SC-7, SC-50, SC-49 and SC-70, each with its disposition below.

| Record | Category | Fields | Pointer | Hazard / card | Disposition |
|---|---|---|---|---|---|
| PlayableX channel thread order | temporal | three start dates in one channel | `C08H78VJG80/1758022459.227279`, `C08H78VJG80/1758701898.919999`, `C08H78VJG80/1759226395.551469` | hazard T02 (files not in chronological order): none of these; card SC-13 (ZM3D beta date) | fold: a dated claim sequence, the last stands (T8); the beta date is never cited or graded |
| Leonard's Playable Kickoff card | temporal | dateLastActivity against its actions | `688c4d14c312a27fa2747e40` (created 2025-08-01, moved 2025-09-13, no comment) | hazard T06 | fold: the planned comment moves the card's and the board's dateLastActivity and the badge's comment count |
| the vendor's name | semantic | 'PlayableX' in Slack text, a masked token in mail and calendar titles | `C08H78VJG80/1758022459.227279`; gcal `evt_257421bc09196edbf28758` | hazard S03: none in scope; trap catalog X04 (uneven masking) | fold: seeded text uses the Slack spelling Julia sees; no row depends on a mail or calendar title |
| masked names in Slack text | semantic | one token stands for both Julia and Claire | `D05SD5QLG94/1758220925.518329`; fact pack §0 | none listed | avoid: no seeded text uses a masking token; people are named or mentioned by Slack id |
| design page against its comments | cross-service referential | tray 7 on the page, a 6-slot proposal in a comment | `page_zm3d_gdd` with `confluence:comment_zm3d_gdd_c1`, `confluence:comment_zm3d_gdd_c2` | cards SC-8, SC-38, SC-58 (other sentences of the same page) | fold: Robert's reply on the page keeps 7 (T9); the page's sentences on the glass crash, the Season Pass date and the monster roster are neither cited nor graded |
| Slack links to Google files | cross-service referential | native ids never equal export ids | planned Slack records, e.g. the ask `D05SD5QLG94/1759256494.852159` | hazard R04 | excluded: no seeded Slack text carries a document link; the ask names the notes in words |
| calendar invitations and share lists | cross-service referential | invitation mails without a calendar row; a departed person on base invites | the planned hold `evt_421695d009e589ee85296c` | hazard R08; card SC-36 | fold: the hold is seeded, single, with four attendees who are all active at the clock, one row per attendee calendar and one invitation mail each (INT-11); no base invite or channel roster is used for the share list |
| channel membership | cross-service referential | leavers stay listed | `C0880U9751A`, `C08H78VJG80` | card SC-7 | not graded: membership is used only to show Julia can read a container (persona_view can-see), never as an answer |
| thread counters | quantitative | reply_count, reply_users_count, latest_reply of Julia's bow post | `C08R8CHB0QL/1758904025.123869` (1 reply in base: `C08R8CHB0QL/1758904103.894649`) | hazards Q01, Q02, Q03 | fold: the planned reply updates the three counters as companions |
| counts in the deliverables | quantitative | 8 Delivered, 39 Ready, 49 Owed of 96 lines | `plan/design_model.py`; the pack list `f_956e60ec7f2f7977d98934` and DES-314 to DES-409 | hazard Q01 kind (a stated count against the rows): none in base for these records | fold: every count comes from the model; no base figure is restated |
| merged pull request without review | state/lifecycle | match3d#462 merged with no human review | `harmonygames-Games/match3d#462` | hazard L09; card SC-50 (bot comment authorship) | fold: the task uses its times and the models its comment names, never its review state or which account commented |
| Linear state against shipped work | state/lifecycle | tickets open after the work shipped | `ZOM-513`, `ZOM-514`, `ZOM-564`, `ZOM-563`, `ART-790`, `ART-792` | card SC-16; card SC-22 (time_in_status_minutes); hazard L06: none in scope | avoid: Maracas (ZOM-513) and Helmet (ZOM-514) are not on the list, nor any object with an open ticket under ZOM-97 (Gas Can, Indoor Plant, Curling Iron, Bagel, the plates); new tickets carry no time_in_status value |
| ids of seeded records | identifier/format | Slack message id, Linear keys and comment ids (97 keys after `DES-312` of 7 May 2025, the Design team's last base ticket, so numbers and dates run in order), Drive ids, Trello action id | `plan/check_ids.py` output: DES-313 to DES-409, `f_8c1d0bca1d1d5fde4c5008`, `68dc381b75aff34acf5a5424` | hazards I01, I02, I10 (`usr_Robert`), I15 | fold: ids follow the base schemes and the generators' conventions; Robert's Linear id is `usr_Robert` as in base; no collision (§12) |
| object names and categories | other | the July export's names differ from the game's; four masked zombie names | `research/object_categories.csv` (the repository tree); `C09ATAJ220H/1758881579.188609` | none listed | fold: every board item takes the tree's name and category; the zombies are one line; Robert's planned answer uses the four unmasked names |
| people and roles | other | Frederick's founder status; time zones | `D05SD5QLG94/1758220925.518329` | cards SC-49, SC-70 | not stated and not graded: no seeded text gives anyone a title or a time zone; seeded times are within each author's September posting hours (fact pack §5) |

**Sibling-defect sweep.** Designed defect kinds and their base siblings: (a) an export that is 'done' and unusable: base has the 24 Sep zombie package ('Only the prefabs were included', `C08H78VJG80/1758808234.045839`), repaired on 26 Sep and kept as a control (T10); (b) art changed after a hand-over: base has match3d#462 (Cactus Plant, Chainsaw, Cone on the list; Kettlebell, Dart Board and Candy off it) and the rocking chair rework of 29 to 30 Sep (`C08R8CHB0QL/1759190391.487809`), not a game object yet; (c) a pick changed in a reply: base has Julia's own grenades-and-shuriken idea, answered 'remain as is' (T13); (d) a rights question on sound: base has two system sounds to be swapped (`D05GU6L0XFH/1757519060.984519`), which are on Calvin's sheet and not on the pack list. Windows read in full: the PlayableX channel from 28 Aug, #zombie-design and #zombie-art from 22 Sep, #zm-animations 24 to 30 Sep, Julia's DMs with Frederick, Claire and Brian for September (fact pack §2, §3, §6).

**Base facts the plan must not contradict** (each checked against the fact pack and the records cited): the first zip held the reference level's six item variants, the zombies, the background and the cannon (`D07G5QWN3TM/1758712833.442809`, `C08H78VJG80/1758717576.077489`); Claire holds the FBX files and sends them, and colours are assigned in Unity (`D076Y0SDV18/1758713188.374029`), which is why twelve planned lines came out of Unity's exporter; the vendor does not use Unity for playables (`C08H78VJG80/1759140968.965099`) and takes .fbx only in binary; no export tool exists in base and none is planned; object work is ticketed in ZOM (`ZOM-97`), where Brian created 13 issues in September; Dart Board and Candy have models and no object data, so they are not lines; match3d#460 (merged 21:51 UTC on 24 Sep) adds new objects and touches the two shared texture atlases without naming a line; Robert asked for the thicker health bar before the zip (`C0880U9751A/1758691270.557429`) and no UI piece is planned as sent; the combo scale was pitched by Calvin from a sample Robert gave (`C09A7PDFYCV/1755464752.078539`), which Calvin's planned sheet repeats; the vendor's price and bundle choice are open in a DM Julia cannot read and no seeded text states a price. One base record holds a credential (`D05UDNCCFEW/1757008285.488349`); it is neither cited as evidence nor copied.


## 1b Active speakers

Status from `references/universe_kb/by_universe/synthcut/activity.json` (`status_at_clock`); seeded times sit inside each person's September posting hours (fact pack §5). The PlayableX staff (`PERSON_6078_SLACK_ID`, `PERSON_3937_SLACK_ID`) are Slack-only ids with no status row and get no seeded voice: every vendor statement the design uses is a base message.

| Person | Email | status_at_clock | Seeding role |
|---|---|---|---|
| Frederick Stone | frederick.stone@harmonygames.co | active_sep_2025_quiet_in_oct | the ask `D05SD5QLG94/1759256494.852159`, the notes `f_8c1d0bca1d1d5fde4c5008`, the hold `evt_421695d009e589ee85296c`, the contact |
| Brian Foster | brian.foster@harmonygames.co | active_sep_2025_quiet_in_oct | the pack list `f_956e60ec7f2f7977d98934`, the pack ticket DES-313 and its 96 children with a note on each, his log of the outgoing folder `f_faf4d7c167d14a1127dcc3` |
| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | the eight `C090N54TG79/1758823946.262829`, the zombie answer `C090N54TG79/1759167068.371289`, the reply `C08R8CHB0QL/1758922879.243189`, the note to Julia on the bathroom objects `D05GU6L0XFH/1759178332.042459` (D3) |
| Claire Morgan | claire.morgan@harmonygames.co | active_sep_2025_quiet_in_oct | no seeded voice in D3 (her D2 message to Julia is removed); tagged in Robert's note and Marcus's post, named in Brian's notes and log |
| Marcus Bennett | marcus.bennett@harmonygames.co | active_sep_2025_quiet_in_oct | the #zombie-match3d post `C0880U9751A/1758906517.912099` |
| Calvin Price | calvin.price@harmonygames.co | active_sep_2025_quiet_in_oct | the sound sources sheet `f_b2387e31d46d3a7b3fa2a9` |
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | the Trello comment `68dc381b75aff34acf5a5424` |
| Julia Lawson | julia.lawson@harmonygames.co | active_sep_2025_quiet_in_oct | her deck of the reference level `f_6a2fa8e61b31139ca8e3d4` (23 Sep) |
| Martin Walsh | martin.walsh@harmonygames.co | active_sep_2025_quiet_in_oct | named on the Fonts ticket as holder of the font files; no seeded voice |

## 1c Identity traps

`entity.py collisions` (verbatim):

```

SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <trello:c48a210d5c5a4b59231c6873>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']

SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']

LOOKALIKE_HANDLES_AND_ALIASES (15)
  - Gmail thread files of arthur.blake@harmonygames.co are named 'blake@harmonygames.co_*'
  - Gmail thread files of brian.foster@harmonygames.co are named 'brian@harmonygames.co_*'
  - Gmail thread files of calvin.price@harmonygames.co are named 'calvin@harmonygames.co_*'
  - Gmail thread files of claire.morgan@harmonygames.co are named 'claire@harmonygames.co_*'
  - Gmail thread files of frederick.stone@harmonygames.co are named 'frederick@harmonygames.co_*'
  - Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*'
  - Gmail thread files of leonard.hayes@harmonygames.co are named 'leonard@harmonygames.co_*'
  - Gmail thread files of oliver.brooks@harmonygames.co are named 'oliver@harmonygames.co_*'
  - Gmail thread files of owen.baker@harmonygames.co are named 'owen@harmonygames.co_*'
  - Gmail thread files of samuel.turner@harmonygames.co are named 'samuel@harmonygames.co_*'
  - Gmail thread files of simon.walker@harmonygames.co are named 'simon@harmonygames.co_*'
  - Gmail thread files of vincent.parker@harmonygames.co are named 'vincent@harmonygames.co_*'
  - Gmail thread files of felix.young@harmonygames.co are named 'felixyoung@harmonygames.co_*'
  - Gmail thread files of oscar.bennett@harmonygames.co are named 'oscar@harmonygames.co_*'
  - Slack handle 'thomas' (U05F0A0D12F) belongs to Thomas Baker <thomas.baker@harmonygames.co> but equals the mailbox local part of Thomas <thomas@harmonygames.co> [persona thomas]

LOOKALIKE_EMAIL_LOCAL_PARTS (1)
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>']

TOKENS_MAPPING_TO_SEVERAL_ENTITIES (9)
  EMPLOYEE_0024: {'entities': ['scott <employee_0024@harmonygames.co>', '? <slack:EMPLOYEE_0024_SLACK_ID>', '? <trello:3d36d70154e6a715614e0d75>'], 'records': ['gcal.calendar_id=employee_0024@harmonygames.co', 'gcal.owner_email=employee_0024@harmonygames.co', 'linear.id=usr_EMPLOYEE_0024', 'linear.email=employee_0024@harmonygames.co', 'contacts.email=employee_0024@harmonygames.co', 'email.email=employee_0024@harmonygames.co', 'slack.id=EMPLOYEE_0024_SLACK_ID', 'trello.username=employee_0024']}
  EMPLOYEE_0032: {'entities': ['? <EMPLOYEE_0032_EMAIL>', 'Josh Dempsey <josh.dempsey@harmonygames.co>', '? <github:EMPLOYEE_0032_GITHUB_USERNAME>', '? <slack:EMPLOYEE_0032_SLACK_ID>'], 'records': ['confluence.id=user_EMPLOYEE_0032', 'gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME', 'slack.id=EMPLOYEE_0032_SLACK_ID']}
  PERSON_2218: {'entities': ['? <PERSON_2218_EMAIL>', '? <github:PERSON_2218_GITHUB_USERNAME>'], 'records': ['linear.id=usr_PERSON_2218', 'linear.email=PERSON_2218_EMAIL', 'contacts.email=PERSON_2218_EMAIL', 'email.email=PERSON_2218_EMAIL', 'github.login=PERSON_2218_GITHUB_USERNAME']}
  PERSON_2360: {'entities': ['? <PERSON_2360_EMAIL>', 'Claire <github:PERSON_2360_GITHUB_USERNAME>'], 'records': ['github.login=PERSON_2360_GITHUB_USERNAME', 'email.email=PERSON_2360_EMAIL']}
  PERSON_3233: {'entities': ['? <PERSON_3233_EMAIL>', '? <github:PERSON_3233_GITHUB_USERNAME>', '? <slack:PERSON_3233_SLACK_ID>'], 'records': ['linear.id=usr_PERSON_3233', 'linear.email=PERSON_3233_EMAIL', 'contacts.email=PERSON_3233_EMAIL', 'email.email=PERSON_3233_EMAIL', 'github.login=PERSON_3233_GITHUB_USERNAME', 'slack.id=PERSON_3233_SLACK_ID']}
  PERSON_3335: {'entities': ['? <PERSON_3335_EMAIL>', '? <slack:PERSON_3335_SLACK_ID>'], 'records': ['contacts.email=PERSON_3335_EMAIL', 'email.email=PERSON_3335_EMAIL', 'slack.id=PERSON_3335_SLACK_ID']}
  PERSON_3935: {'entities': ['? <PERSON_3935_EMAIL>', '? <slack:PERSON_3935_SLACK_ID>'], 'records': ['email.email=PERSON_3935_EMAIL', 'slack.id=PERSON_3935_SLACK_ID']}
  PERSON_5275: {'entities': ['? <PERSON_5275_EMAIL>', '? <slack:PERSON_5275_SLACK_ID>'], 'records': ['contacts.email=PERSON_5275_EMAIL', 'email.email=PERSON_5275_EMAIL', 'slack.id=PERSON_5275_SLACK_ID']}
  PERSON_5360: {'entities': ['? <PERSON_5360_EMAIL>', '? <slack:PERSON_5360_SLACK_ID>'], 'records': ['email.email=PERSON_5360_EMAIL', 'slack.id=PERSON_5360_SLACK_ID']}

SEVERAL_IDS_IN_ONE_SERVICE (1)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: 2 github identities ['PERSON_0003_GITHUB_USERNAME', 'PERSON_2137_GITHUB_USERNAME'] (joins: ['exact_email', 'exact_name'])

PERSONA_ROLE_VS_CONTACTS_JOB (5)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: roster role 'Game Engineer (Unity VFX)' vs Contacts job 'Game Engineer (Unity/VFX)'
  - Frederick Stone <frederick.stone@harmonygames.co> [persona frederick_stone]: roster role 'Co-founder' vs Contacts job 'Commercial Lead, Marketing & Business Development'
  - Leonard Hayes <leonard.hayes@harmonygames.co> [persona leonard_hayes]: roster role 'Co-founder & Creative Director' vs Contacts job 'Co-founder & CEO'
  - Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]: roster role 'Artist' vs Contacts job 'Artist (VFX & Animation)'
  - Robert <robert@harmonygames.co> [persona robert]: roster role 'Co-Founder & Creative Director' vs Contacts job 'Co-founder & Chief Product Officer'

SHARED_CONTACT_JOB_TITLES (5)
  Game Designer: ['Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]', 'Samuel Turner <samuel.turner@harmonygames.co> [persona samuel_turner]']
  Game Developer: ['Thomas <thomas@harmonygames.co> [persona thomas]', 'Lucas <lucas@harmonygames.co>']
  Game Engineer: ['Brian Foster <brian.foster@harmonygames.co> [persona brian_foster]', 'Victor Barnes <victor.barnes@harmonygames.co> [persona victor_barnes]']
  General Counsel: ['Michelle Carter <michelle.carter@harmonygames.co>', 'Thomas Baker <thomas.baker@harmonygames.co>']
  User Acquisition Manager: ['George Miller <george.miller@harmonygames.co>', 'Megan Wilson <megan.wilson@harmonygames.co>', 'Victoria Lane <victoria.lane@harmonygames.co>']

UNRESOLVED (11)
  [ambiguous_name] github: mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co'] -> candidates ['email:claire.morgan@harmonygames.co']
  [ambiguous_name] trello: mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  [token_link] EMPLOYEE_0024: same token number across services but no shared exact email/name: not joined -> candidates ['email:employee_0024@harmonygames.co', 'slack:EMPLOYEE_0024_SLACK_ID', 'trello:3d36d70154e6a715614e0d75']
  [token_link] EMPLOYEE_0032: same token number across services but no shared exact email/name: not joined -> candidates ['email:EMPLOYEE_0032_EMAIL', 'email:josh.dempsey@harmonygames.co', 'github:EMPLOYEE_0032_GITHUB_USERNAME', 'slack:EMPLOYEE_0032_SLACK_ID']
  [token_link] PERSON_2218: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2218_EMAIL', 'github:PERSON_2218_GITHUB_USERNAME']
  [token_link] PERSON_2360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2360_EMAIL', 'github:PERSON_2360_GITHUB_USERNAME']
  [token_link] PERSON_3233: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3233_EMAIL', 'github:PERSON_3233_GITHUB_USERNAME', 'slack:PERSON_3233_SLACK_ID']
  [token_link] PERSON_3335: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3335_EMAIL', 'slack:PERSON_3335_SLACK_ID']
  [token_link] PERSON_3935: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3935_EMAIL', 'slack:PERSON_3935_SLACK_ID']
  [token_link] PERSON_5275: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5275_EMAIL', 'slack:PERSON_5275_SLACK_ID']
  [token_link] PERSON_5360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5360_EMAIL', 'slack:PERSON_5360_SLACK_ID']

INTEGRITY FLAGS (2)
  {'type': 'id_with_space', 'service': 'linear', 'id': 'usr_Victor Barnes'}
  {'type': 'name_mismatch_on_email_join', 'service': 'github', 'id': 'PERSON_2314_GITHUB_USERNAME', 'detail': "GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frederick Stone)"}
```

`entity.py resolve` for the people the design names (first lines of each):

```
### Julia Lawson
ENTITY email:julia.lawson@harmonygames.co  name=Julia Lawson  kind=person  emails=['julia.lawson@harmonygames.co']
  persona: julia_lawson - Product Manager / Product
  slack      id=EMPLOYEE_0005_SLACK_ID, name=Julia Lawson, real_name=Julia Lawson, email=julia.lawson@harmonygames.co, is_bot=False, deleted=False, messages=31848, first_post=2023-07-16, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=julia.lawson@harmonygames.co, threads=253, messages=304, first=2023-07-16, last=2025-09-17, thread_filename_alias=['jlawson@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=julia.lawson@harmonygames.co, owner_email=julia.lawson@harmonygames.co, summary=Julia Lawson — primary, events=748, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_8140f09bf9f1, email=julia.lawson@harmonygames.co, display_name=julia.lawson@harmonygames.co, root_folders=['d_8140f09bf9f1b94cb8ee2d'], owned_items=28, last_modified=2025-09-11, files_shared_with=158   [join: exact_email]
  linear     id=usr_8140f09bf9f1b94c, email=julia.lawson@harmonygames.co, name=julia.lawson@harmonygames.co, is_active=True, last_activity=2025-09-23   [join: exact_email]
### Frederick Stone
ENTITY email:frederick.stone@harmonygames.co  name=Frederick Stone  kind=person  emails=['frederick.stone@harmonygames.co']
  persona: frederick_stone - Co-founder / Executive
  slack      id=EMPLOYEE_0008_SLACK_ID, name=Frederick Stone, real_name=Frederick Stone, email=frederick.stone@harmonygames.co, is_bot=False, deleted=False, messages=4780, first_post=2023-09-15, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=frederick.stone@harmonygames.co, threads=4656, messages=5474, first=2024-06-25, last=2025-10-01, thread_filename_alias=['frederick@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=frederick.stone@harmonygames.co, owner_email=frederick.stone@harmonygames.co, summary=Frederick Stone — primary, events=316, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_175c0d7bc72e, email=frederick.stone@harmonygames.co, display_name=frederick.stone@harmonygames.co, root_folders=['d_175c0d7bc72ed244b944cb'], owned_items=46, last_modified=2025-09-24, files_shared_with=213   [join: exact_email]
  linear     id=usr_175c0d7bc72ed244, email=frederick.stone@harmonygames.co, name=frederick.stone@harmonygames.co, is_active=True, last_activity=2025-08-26   [join: exact_email]
### Brian Foster
ENTITY email:brian.foster@harmonygames.co  name=Brian Foster  kind=person  emails=['brian.foster@harmonygames.co']
  persona: brian_foster - Game Engineer / Engineering
  slack      id=EMPLOYEE_0026_SLACK_ID, name=Brian Foster, real_name=Brian Foster, email=brian.foster@harmonygames.co, is_bot=False, deleted=False, messages=28951, first_post=2024-06-06, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=brian.foster@harmonygames.co, threads=297, messages=307, first=2024-06-05, last=2025-09-30, thread_filename_alias=['brian@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=brian.foster@harmonygames.co, owner_email=brian.foster@harmonygames.co, summary=Brian Foster — primary, events=417, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_fc22d5941b2a, email=brian.foster@harmonygames.co, display_name=brian.foster@harmonygames.co, root_folders=['d_fc22d5941b2aeb5c03ad32'], owned_items=101, last_modified=2025-09-17, files_shared_with=127   [join: exact_email]
  linear     id=usr_fc22d5941b2aeb5c, email=brian.foster@harmonygames.co, name=brian.foster@harmonygames.co, is_active=True, last_activity=2025-09-30   [join: exact_email]
### Claire Morgan
ENTITY email:claire.morgan@harmonygames.co  name=Claire Morgan  kind=person  emails=['claire.morgan@harmonygames.co']
  persona: claire_morgan - Art Lead / Design
  slack      id=EMPLOYEE_0009_SLACK_ID, name=Claire Morgan, real_name=Claire Morgan, email=claire.morgan@harmonygames.co, is_bot=False, deleted=False, messages=9824, first_post=2023-03-22, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=claire.morgan@harmonygames.co, threads=846, messages=923, first=2023-03-30, last=2025-09-30, thread_filename_alias=['claire@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=claire.morgan@harmonygames.co, owner_email=claire.morgan@harmonygames.co, summary=Claire Morgan — primary, events=553, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_7fe31e7ec819, email=claire.morgan@harmonygames.co, display_name=claire.morgan@harmonygames.co, root_folders=['d_7fe31e7ec81996189e1f14'], owned_items=69, last_modified=2024-07-08, files_shared_with=115   [join: exact_email]
  linear     id=usr_7fe31e7ec8199618, email=claire.morgan@harmonygames.co, name=claire.morgan@harmonygames.co, is_active=True, last_activity=2025-09-03   [join: exact_email]
### Robert
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=110334, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=robert@harmonygames.co, threads=14813, messages=17363, first=2023-03-15, last=2025-10-01   [join: exact_email]
  gcal       calendar_id=robert@harmonygames.co, owner_email=robert@harmonygames.co, summary=Robert — primary, events=1133, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_9f7ba94f7526, email=robert@harmonygames.co, display_name=Robert, root_folders=['d_9f7ba94f7526d54d8482ba'], owned_items=190, last_modified=2025-09-25, files_shared_with=412   [join: exact_email]
  linear     id=usr_Robert, email=robert@harmonygames.co, name=Robert, is_active=True, last_activity=2025-09-30   [join: exact_email]
### Leonard Hayes
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=129898, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=leonard.hayes@harmonygames.co, threads=15339, messages=19668, first=2023-03-15, last=2025-10-01, thread_filename_alias=['leonard@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=leonard.hayes@harmonygames.co, owner_email=leonard.hayes@harmonygames.co, summary=Leonard Hayes — primary, events=1382, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_63fffeb4fab5, email=leonard.hayes@harmonygames.co, display_name=leonard.hayes@harmonygames.co, root_folders=['d_63fffeb4fab5233ed5bb73'], owned_items=752, last_modified=2025-09-30, files_shared_with=365   [join: exact_email]
  linear     id=usr_63fffeb4fab5233e, email=leonard.hayes@harmonygames.co, name=leonard.hayes@harmonygames.co, is_active=True, last_activity=2025-09-22   [join: exact_email]
### Marcus Bennett
ENTITY email:marcus.bennett@harmonygames.co  name=Marcus Bennett  kind=person  emails=['marcus.bennett@harmonygames.co']
  persona: marcus_bennett - Artist / Design
  slack      id=EMPLOYEE_0002_SLACK_ID, name=Marcus Bennett, real_name=Marcus Bennett, email=marcus.bennett@harmonygames.co, is_bot=False, deleted=False, messages=25786, first_post=2023-09-28, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=marcus.bennett@harmonygames.co, threads=4219, messages=4245, first=2023-09-28, last=2025-09-29, thread_filename_alias=['marcus.bennett@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=marcus.bennett@harmonygames.co, owner_email=marcus.bennett@harmonygames.co, summary=Marcus Bennett — primary, events=604, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_c77c50cc15c5, email=marcus.bennett@harmonygames.co, display_name=marcus.bennett@harmonygames.co, root_folders=['d_c77c50cc15c5342d638ebb'], owned_items=47335, last_modified=2025-09-10, files_shared_with=132   [join: exact_email]
  linear     id=usr_c77c50cc15c5342d, email=marcus.bennett@harmonygames.co, name=marcus.bennett@harmonygames.co, is_active=True, last_activity=2025-09-25   [join: exact_email]
### EMPLOYEE_0006_SLACK_ID
ENTITY email:calvin.price@harmonygames.co  name=Calvin Price  kind=person  emails=['calvin.price@harmonygames.co']
  persona: calvin_price - Game Engineer (Unity VFX) / Engineering
  slack      id=EMPLOYEE_0006_SLACK_ID, name=Calvin Price, real_name=Calvin Price, email=calvin.price@harmonygames.co, is_bot=False, deleted=False, messages=12017, first_post=2023-03-29, last_post=2025-09-29   [join: exact_email]
  gmail      mailbox=calvin.price@harmonygames.co, threads=8142, messages=9856, first=2023-03-29, last=2025-09-30, thread_filename_alias=['calvin@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=calvin.price@harmonygames.co, owner_email=calvin.price@harmonygames.co, summary=Calvin Price — primary, events=442, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_49b9dfa5208d, email=calvin.price@harmonygames.co, display_name=calvin.price@harmonygames.co, root_folders=['d_49b9dfa5208d400d9b3937'], owned_items=1918, last_modified=2025-02-14, files_shared_with=128   [join: exact_email]
  linear     id=usr_49b9dfa5208d400d, email=calvin.price@harmonygames.co, name=calvin.price@harmonygames.co, is_active=True, last_activity=2025-09-25   [join: exact_email]
```

Pinned entities and their lookalikes: Claire Morgan (`EMPLOYEE_0009_SLACK_ID`, Linear `usr_7fe31e7ec8199618`) against the GitHub-only 'Claire' login; Robert (Linear `usr_Robert`, hazard I10) has no surname in any service; Calvin Price has two GitHub logins and one Slack id (`EMPLOYEE_0006_SLACK_ID`); Marcus Bennett is `EMPLOYEE_0002_SLACK_ID` (Linear `usr_c77c50cc15c5342d`), not the two other Marcuses of the roster; `EMPLOYEE_0032_SLACK_ID`, the engineer Brian asked about assets on 24 Sep, is unidentified in every service and gets no seeded voice. Victor Barnes left in April 2025 and has no seeded voice. No second account is created for anyone and no trap depends on a malformed id. The PlayableX intake contact is a role address, not a person, so it duplicates nobody.


## 2 Cohort spine

**Rule (closed).** A line is one row of Brian's pack list `f_956e60ec7f2f7977d98934` (96 rows: 84 board items in seven of the game's categories, the cannon, the background, the zombie characters, six sound cues, the item visuals, the UI elements, the fonts). The list has 96 lines; key = the line's name, spelled as the pack list spells it. Nothing adds a line: the ask has no clause about the vendor's requests, the vendor's 'duck asset' is the Plushie Chick line and its 'rocket launcher' the Cannon line (T16), and the choice of animation and zombies goes in the brief.

**Truth by class** (`plan/design_model.py`; Delivered 8, Ready 39, Owed 49; without the five hidden records: 8 / 73 / 15 of 96):

| State | Lines | Why | Members |
|---|---|---|---|
| Delivered | 8 | in PlayableX's hands and usable: the two zips of 24 Sep and the 26 Sep pack (base) | Couch, Couch and Pillow, Grenade, Plushie Bunny, Plushie Chick, Cannon, Background, Zombie characters |
| Ready | 36 | FBX from Claire (or .wav from the project), opens or plays, current, nobody changing it | Desk Lamp, Small Lamp, Cute Axe, Cute Hammer, Dynamite, Shuriken, Saber, Safe, Flashlight, Bow, Dice, Gift Box, Plushie Dog, Plushie Whale, Whistle, Wooden Tower, Toy Car, Toy Boat, Toy Airplane, Dutch Oven, Rolling Pin, Round Kettle, Round Pan, Spatula, Whisk, Ladle, Music Keyboard, Barrel, Bench, Flower Pot, Garden Shears, Watering Can, Wooden Bucket, Matching sound, Success sound, Failure sound |
| Owed, stated on the line's own ticket | 15 | not exported or not sent, in Brian's words, with who has it | Fly Zapper, Fire Extinguisher, Propane Tank, Toy Train, Beach Ball, Rubber Ducky, Small Kettle, Tall Kettle, Grand Piano, Wheelbarrow, Wooden Crate, Background music, Item visuals, UI elements, Fonts |
| Owed, EXPORT | 12 | FBX saved out of the Unity project on 25 Sep: the text kind, which the vendor does not take (Marcus's post) | Alarm Clock, Record Player, Retro TV, Coffee Machine, Cooler, Ice Cream Machine, Kitchen Mixer, Microwave, Oven, Refrigerator, Stove, Toaster |
| Owed, ARTHOLD | 12 | category Bathroom: Claire is redoing the UVs; Friday's files are the old version (Robert's note to Julia) | Bathroom Scale, Bathtub, Cabinet Sink, Flip Flops, Iron, Ironing Board, Plunger, Slippers, Toilet, Toilet Paper, Wash Basin, Washing Machine |
| Ready, REVISED (sent again) | 3 | recoloured after the 25 Sep hand-over (Robert, base, 29 Sep) and sent again with the new colours, opening and looking right (Brian's log, 30 Sep) | Chainsaw, Cone, Cactus Plant |
| Owed, ZIP | 8 | in Friday's zip of instruments, which will not unpack (Brian's own log of the outgoing folder) | Acoustic Guitar, Cello, Cymbals, Electric Guitar, Harp, Tambourine, Trumpet, Xylophone |
| Owed, AUDIO | 2 | from a library seat or a bought pack (Calvin's sheet); the notes hand over only what is ours | Rocket sound, Explosion sound |

**Every category is mixed** (class counts per category on the pack list; W delivered, READY, VIS owed on its own note, A1 / A2 / C1 / C2 / C4 the hidden classes):

| Category | Lines | Classes |
|---|---|---|
| Living Room | 8 | W 2, A1 3, READY 2, VIS 1 |
| Survival | 11 | W 1, C1 1, READY 7, VIS 2 |
| Toys | 15 | W 2, READY 10, C1 1, VIS 2 |
| Bathroom | 13 | A2 12, VIS 1 |
| Kitchen | 18 | A1 9, READY 7, VIS 2 |
| Music Instruments | 10 | C4 8, READY 1, VIS 1 |
| Garden | 9 | C1 1, READY 6, VIS 2 |
| (not a board item) | 12 | W 3, READY 3, C2 2, VIS 4 |

**Surfaces and shortcut audit** (manifest `cohort.evidence_surfaces`):

| Surface | Records | Calls each | Bulk call that does not cover it | Why it cannot be skipped | Serves |
|---|---|---|---|---|---|
| linear `linear_list_comments` | 96 | 1.0 | linear_list_issues and linear_get_issue return no comments; Brian's note on a line (where the file came from, when, whether it opens, or that it is not exported) is only in that ticket's comments | the pack list has no state column and every undelivered ticket is In Progress; each category holds Ready lines, lines Owed on their own note and lines from different exports, so no ticket can stand for its neighbours | R2: state per line: Delivered, Ready or Owed |
| linear `linear_update_issue + linear_create_comment` | 49 | 2.0 | no batch write exists for state changes or comments; each ticket takes its own calls | the notes require the Todo state and the comment on every Owed line's ticket; the sheet does not replace them | R6: an Owed line's ticket to Todo with a comment saying what is owed and who has it |
| gdocs `gdrive_search + gdocs_get_document_text` | 11 | 0.18 | nothing on the eleven tickets, on the pack list or in the notes says the zip will not unpack or that the three were sent again; only Brian's own log of the outgoing folder records it | the eight tickets say the files are zipped in the outgoing folder and the three say they were handed over on 25 Sep, before Robert's 29 Sep colours; no other record says what is in the folder now | R2: state per line: Delivered, Ready or Owed |

**Predicate.** The notes define the three states: Delivered, PlayableX has the current file and can use it; Ready, exported in a format they take, it opens, it is the current version and nobody is changing it; Owed, anything else, with what is owed and who has it (whoever has to do the next thing). Brian's note stands unless something later says otherwise. **House rule that overrides the natural reading:** a ticket that says 'exported, opens' is not Ready when the file is in a format the vendor refuses, the art is being redone, the art changed afterwards and the file has not gone again, the zip it sits in will not unpack, or the sound is not ours to pass on. (The board set is a separate column: PICKS changes which two lines are Default and Extra, not a state.) **Dual regime by date:** the three recoloured lines' notes (25 Sep) predate Robert's new colour versions (29 Sep, base `C090N54TG79/1759189466.554739`), which predate the re-send in Brian's log (30 Sep, `f_faf4d7c167d14a1127dcc3`): the latest record decides, and it says Ready. **Boundary records:** the Plushie Chick delivered in a second zip the same day (`C08H78VJG80/1758729487.922339`); the zombie pack sent twice (T10); Kettlebell, Dart Board and Candy, touched by the same pull request and not lines (T18).

**Necessity of the per-line read.** 49 of the 96 listed lines are Owed and nothing upstream says which: the pack list has no state column, every undelivered ticket is In Progress, ticket titles and descriptions carry the line's name only, and no category is of one class. The 15 lines that are Owed on their own note sit in ten groups, so a run that samples a few tickets per category gets the three totals and its sampled states wrong. Notes state raw facts (where the file came from, when, whether it opens), never the state. Purpose of the volume, per group: 84 board items because the vendor asked for an 8-item set plus extra items it can make editable and Brian promised more items later; six sound cues, the item visuals, the UI elements and the fonts because the vendor's 19 Sep list names them; the cannon, the background and the zombies because they went. No line exists to raise a count, and each line's state is a cell of the hand-off list. Base holds no Linear comment at all, so every comment a run reads here is one of this task's notes; that is named for the injection dossier.

**Ids.** DES-313 is the pack ticket; children DES-314 to DES-409 follow the list order (`plan/design_model.py`). Base highest Design number is `DES-312` (`conventions.json` linear.max_number; every minted key looked up in `plan/check_ids.py`, scan complete). Collision check: §12.


## 3 Hidden authorities

| Id | Name (what it governs) | Home | Record | Governs | Decoy and its scope | Findability |
|---|---|---|---|---|---|---|
| H1 | Frederick's hand-off notes | gdocs | `f_8c1d0bca1d1d5fde4c5008` | R2, R3, R5, R6 | gdocs: `gdocs:f_05bedd1540d3e01a90ab16` — game: Domino Delights (the first playable, April 2025: Leonard's Playable Feedback) | a search for 'hand-off notes' returns it; the ask names it in words |
| H2 | Brian's pack list | gsheets | `f_956e60ec7f2f7977d98934` | R1 | slack: `C08H78VJG80/1758283671.878269` — issuer: PlayableX's request (asset groups they expect, no lines) | a search for 'playable pack list' returns it; the ask names it in words |
| H3 | the kickoff hold | gcal | `evt_421695d009e589ee85296c` | R7 | trello: `trello:688c4d14c312a27fa2747e40`, `68dc381b75aff34acf5a5424` — issuer: Leonard's own to-do card (no attendees) | a search for 'playable kickoff' returns it; the ask names it in words |

`governs` lists do not overlap (H1: R2, R3, R5, R6; H2: R1; H3: R7). H1 has a same-service decoy with an adjacent scope: Leonard's 'Playable Feedback' (`f_05bedd1540d3e01a90ab16`, the first playable). Each authority is named by what it governs or who issued it ('my hand-off notes', 'Brian's pack list', 'the kickoff hold'); no decoy carries a self-advertising cue. Findability of planned records is proven on the SQL at `/create-injection` (`persona_view.py check-sql`); the base decoys are YES in the reach table (§10).


## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Frederick's playable message | `D05SD5QLG94/1759256494.852159` |
| A2 | the PlayableX channel | `C08H78VJG80` |
| A3 | my Drive | `d_8140f09bf9f1b94cb8ee2d` |

**Hub.** Frederick's DM `D05SD5QLG94/1759256494.852159` (planned wording in `plan/planned_texts.py`). It delegates by role: 'Brian's pack list', 'Robert's picks', 'My hand-off notes'. It names no location, no id and none of the records in §5 that decide a row. The notes `f_8c1d0bca1d1d5fde4c5008` say what the brief covers, name the list's columns and the three state words, give the rule for later statements and changed art, the sound rule, the ticket follow-through and the sharing; they point at the pack ticket, the design page, the deck, the kickoff hold and Contacts by name, and at nothing that decides a hidden row.

**Incorporation table** (every `delegation_quote` is an exact substring of the delegating record's planned or base text; the gate reads them):

| Fragment | Service · container | Kind | Chain | Delegated by | Words (verbatim) | Requirements | Names |
|---|---|---|---|---|---|---|---|
| K1 | gdocs · `f_8c1d0bca1d1d5fde4c5008` | delegation | A1 → K1 | `D05SD5QLG94/1759256494.852159` | 'My hand-off notes say what goes in the brief, what counts as ready, what to do with the tickets and who gets the files' | R2, R3, R5, R6 | H3 |
| K2 | gsheets · `f_956e60ec7f2f7977d98934` | requirement | A1 → K2 | `D05SD5QLG94/1759256494.852159` | 'Brian's pack list is where it starts' | R1 | — |
| K3 | slack · `C090N54TG79/1758823946.262829` | requirement | A1 → K3 | `D05SD5QLG94/1759256494.852159` | 'Robert's picks for the board and the zombies stand' | R4 | — |
| K4 | linear · `DES-313` | destination | A1 → K1 → K4 | `f_8c1d0bca1d1d5fde4c5008` | 'Tickets live under Brian's pack ticket, one per line' | R6 | — |
| K5 | slack · `C08H78VJG80/1757695108.506159` | format | A1 → K1 → K5 | `f_8c1d0bca1d1d5fde4c5008` | 'What they told us about formats still holds' | R2 | — |
| K6 | confluence · `page_zm3d_gdd` | requirement | A1 → K1 → K6 | `f_8c1d0bca1d1d5fde4c5008` | 'How the level plays is on the design page' | R5 | — |
| K7 | gcal · `evt_421695d009e589ee85296c` | recipient | A1 → K1 → K7 | `f_8c1d0bca1d1d5fde4c5008` | 'Everyone on the kickoff hold' | R7 | — |
| K8 | contacts · `d7d31caf63ee33db2b7ed271` | recipient | A1 → K1 → K8 | `f_8c1d0bca1d1d5fde4c5008` | 'their intake address, which is in Contacts' | R7 | — |
| K9 | gslides · `f_6a2fa8e61b31139ca8e3d4` | requirement | A1 → K1 → K9 | `f_8c1d0bca1d1d5fde4c5008` | 'your deck of the reference level has what we built for them' | R5 | — |
| K10 | slack · `C090N54TG79/1759167068.371289` | requirement | A1 → K10 | `D05SD5QLG94/1759256494.852159` | 'Robert's picks for the board and the zombies stand' | R5 | — |
| K11 | slack · `C08R8CHB0QL/1758904025.123869` | amendment | A1 → K11 | `D05SD5QLG94/1759256494.852159` | 'unless he's changed them since' | R4 | — |
| K12 | slack · `C08H78VJG80/1744637266.363689` | requirement | A1 → K1 → K12 | `f_8c1d0bca1d1d5fde4c5008` | 'so does their rule from last time about when the music may start' | R5 | — |
| K13 | slack · `C08H78VJG80/1759226395.551469` | requirement | A1 → K13 | `D05SD5QLG94/1759256494.852159` | 'PlayableX are holding Nov 3 for us' | R5 | — |
| K15 | slack · `C08H78VJG80/1757695108.506159` | requirement | A1 → K1 → K15 | `f_8c1d0bca1d1d5fde4c5008` | 'which scenario we picked and what it is for' | R5 | — |
| K16 | slack · `D05SD5QLG94/1759256494.852159` | requirement | A1 → K16 | `D05SD5QLG94/1759256494.852159` | 'write the brief they build from, and tell me where the item pack actually stands' | R1, R7 | H1, H2 |

15 fragments over 8 services. **Amendment:** K11, Robert's 26 Sep reply, in another channel and a day after K3; it changes one item (the dynamite) and the ask keeps his latest word ('unless he's changed them since'); nothing later re-asserts the dynamite. **Non-authoritative instruction distractors:** Julia's own grenades-and-shuriken idea (T13), Frederick's three-item 'good start' and the reference level (T14), the March FBX rule from the first playable (T12), Leonard's card (T11).


## 5 Chains and trap register

**Chains** (six, six distinct root causes):

| Chain | Root cause | Hops (service: record — finding) | Ends in |
|---|---|---|---|
| C1 | A24 | slack: `C08H78VJG80/1758022459.227279` — the vendor takes .fbx only in binary format, not ASCII (16 and 19 Sep; Frederick relayed it to Julia on 18 Sep)<br>linear: `DES-367` — Brian's note: FBX saved out of the project, Thu 25 Sep, so the colours come along; opens, looks right, in the outgoing folder (twelve lines in two categories say this)<br>slack: `C0880U9751A/1758906517.912099` — Marcus, 26 Sep, #zombie-match3d: the models Brian saved out of Unity on Thursday are the text kind, the setting was wrong that day; Claire's are fine | R2 |
| C2 | A11 | gsheets: `f_956e60ec7f2f7977d98934` — thirteen lines carry the category Bathroom, the iron, the ironing board and the washing machine among them<br>linear: `DES-349` — Brian's note: FBX from Claire, Fri 26 Sep, opens, looks right<br>slack: `D05GU6L0XFH/1759178332.042459` — Robert to Julia, 29 Sep, in their DM: Claire is redoing the UVs on the bathroom objects; the bathroom files she gave Brian on Friday are the old version | R3 |
| C3 | A25 | linear: `DES-389` — Brian's note, written 25 Sep 08:06 UTC: FBX from Claire first thing, opens, looks right (also Chainsaw and Cone)<br>slack: `C090N54TG79/1759189466.554739` — Robert, 29 Sep 23:44 UTC, #zombie-design: new coloured versions of the cactus, the chainsaw and the cones (base)<br>gdocs: `f_8c1d0bca1d1d5fde4c5008` — if the art changed after a file went out or was exported, it goes again<br>gdocs: `f_faf4d7c167d14a1127dcc3` — Brian's log of the outgoing folder, Tue 30 Sep: Claire sent the three recoloured models again; they open, look right and replace Thursday's (which three: Robert's post) | R2 |
| C4 | A14 | gslides: `f_6a2fa8e61b31139ca8e3d4` — Julia's deck: the reference level as built on 23 Sep has three item types<br>slack: `C090N54TG79/1758823946.262829` — Robert, 25 Sep: the eight for the board, the dynamite among them; everything else is an extra<br>slack: `C08R8CHB0QL/1758922879.243189` — Robert, 26 Sep, under Julia's bow post in #zombie-art: it goes in the eight in place of the last item on his list, as it is | R4 |
| C5 | A13 | linear: `DES-402` — Brian's note: exported .wav from the project, plays, in the outgoing folder<br>gdocs: `f_8c1d0bca1d1d5fde4c5008` — we only hand over what is ours to hand over; anything from a library or a bought pack stays until we have our own version<br>gsheets: `f_b2387e31d46d3a7b3fa2a9` — Calvin's sources sheet: the rocket sound is from a library seat and the explosion from a bought pack; our own versions are not made yet | R2 |
| C6 | A3 | gsheets: `f_956e60ec7f2f7977d98934` — ten lines carry the category Music Instruments<br>linear: `DES-380` — Brian's note: FBX from Claire, Fri 26 Sep, opens, looks right, zipped with the other instruments (eight lines say this)<br>gdocs: `f_faf4d7c167d14a1127dcc3` — Brian's own log of the outgoing folder, 30 Sep: the zip with Friday's instruments was cut off on upload and will not unpack, and the eight are not in the folder any other way; he will put the files back | R3 |

**Trap register:**

| Trap | Family | Services | Records | Req. | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|---|
| T1 | done_gap | linear, slack | `DES-367`, `DES-318`, `C0880U9751A/1758906517.912099`, `C08H78VJG80/1758022459.227279` | R2 | the twelve lines saved out of the project are Ready: each ticket says FBX, opens, looks right, in the outgoing folder | Marcus's 26 Sep post in #zombie-match3d: those files are the text kind (the setting was wrong that day); the vendor takes binary only, so each is Owed (export again as binary, Brian) | each ticket's note is read while building the list; the post is in the game's dev channel, which the ask never names, and carries none of the ask's words |
| T2 | superseding | linear, slack | `DES-349`, `D05GU6L0XFH/1759178332.042459` | R3 | the twelve exported bathroom lines are Ready: FBX from Claire on Friday, opens, looks right | Robert's 29 Sep note to Julia: Claire is redoing the UVs on the bathroom objects and the files she gave Brian on Friday are the old version, so each is Owed (the art, Claire: the file came from her) | Brian's note (26 Sep) is on every bathroom ticket; Robert's note is three days later, in Julia's DM with him among his other messages of that day, naming the category and no line, with Claire and Brian tagged rather than named |
| T3 | superseding | linear, slack, gdocs | `DES-389`, `f_faf4d7c167d14a1127dcc3`, `C090N54TG79/1759189466.554739`, `C08R8CHB0QL/1758752145.583769` | R2 | Cactus Plant, Chainsaw and Cone are Owed: Robert showed new colour versions on 29 Sep, after their 25 Sep files, and the notes send a changed file again | Brian's log of the outgoing folder, Tue 30 Sep: Claire sent the three recoloured models again, they open and look right and they replace Thursday's; Robert's post says which three; so each is Ready | Robert's post sits in #zombie-design next to his picks and is met early; the completion is a later entry in a second document by the list's owner that nothing links, found by looking for the outgoing folder the notes speak of |
| T4 | authority | linear, gdocs, gsheets | `DES-402`, `f_8c1d0bca1d1d5fde4c5008`, `f_b2387e31d46d3a7b3fa2a9`, `D05GU6L0XFH/1757519060.984519` | R2 | all five exported sound cues are Ready: .wav is a format the vendor takes and each plays | the notes hand over only sound that is ours; Calvin's sources sheet says the rocket sound is from a library seat and the explosion from a bought pack, so both are Owed (our own version, Calvin) | the tickets state the file type only; the sheet is found by looking for where the sounds came from |
| T5 | superseding | slack | `C090N54TG79/1758823946.262829`, `C08R8CHB0QL/1758922879.243189`, `C08R8CHB0QL/1758904025.123869` | R4 | the eight are Robert's 25 Sep post, with the dynamite | Robert's own reply of 26 Sep under Julia's bow post: it goes in the eight in place of the last item on his list, the dynamite; the ask keeps his latest word | a search for the playable returns the 25 Sep post in #zombie-design; the reply is in #zombie-art under a post about an arrow |
| T6 | exact_predicate | gdocs, gsheets | `f_8c1d0bca1d1d5fde4c5008`, `f_956e60ec7f2f7977d98934` | R4 | every line outside the eight is an Extra, the cannon, the zombies, the sound cues and the fonts included | the notes: Board set is Default for the eight, Extra for every other board item, and empty for anything that is not a board item; the pack list's Kind column says which lines are board items | the rule and the Kind column are both on the first-read path; the trap is applying 'Extra' to all 88 other lines |
| T7 | completion_elsewhere | linear, gdocs | `DES-380`, `f_faf4d7c167d14a1127dcc3` | R3 | the eight instruments in Friday's zip are Ready: each ticket says FBX from Claire, opens, looks right, zipped, in the outgoing folder | Brian's own log of the outgoing folder (30 Sep): that zip was cut off on upload, will not unpack and is the only copy in the folder, so each is Owed (put the files back, Brian) | the tickets say the files are in the outgoing folder; the log is a second document by the list's owner that nothing links, found by looking for that folder |
| T8 | effective_date | slack | `C08H78VJG80/1758022459.227279`, `C08H78VJG80/1758701898.919999`, `C08H78VJG80/1759226395.551469` | R5 | the project starts on 29 September, or on 6 October | base: the vendor's last message sets 3 November | all three dates are in the PlayableX channel; the latest is the last message |
| T9 | distractor (withdrawn_ask) | confluence | `confluence:page_zm3d_gdd`, `confluence:comment_zm3d_gdd_c1`, `confluence:comment_zm3d_gdd_c2` | R5 | the tray has six slots (Julia's July proposal in the design page's comments) | base: Robert's reply on the page keeps it at seven | — |
| T10 | completion_elsewhere | slack | `DES-400`, `C08H78VJG80/1758808234.045839`, `C09ATAJ220H/1758905604.787929`, `C08H78VJG80/1758906043.375719` | R2 | the zombie characters are Owed: the vendor said the package was not exported correctly | base: Marcus's pack, tested in an empty project, went on 26 Sep; the vendor reviewed it on 29 Sep and asked for a choice, not for files | the complaint (25 Sep) comes before the pack (26 Sep) in the same thread |
| T11 | scope_alias | trello, gcal | `68dc381b75aff34acf5a5424`, `evt_421695d009e589ee85296c`, `trello:688c4d14c312a27fa2747e40` | R7 | the files are shared with whoever is on Leonard's Playable Kickoff card | the notes name the kickoff hold: its attendees are Frederick, Julia, Brian and Robert | a search for the kickoff returns the Trello card by its title before the calendar hold |
| T12 | distractor (other_title) | slack | `C08H78VJG80/1742892985.601399` | R2 | everything has to be FBX (the March rule from the first playable) | base: for this playable the vendor takes .fbx (binary), .glb or .blend for 3D (16 and 19 Sep) | — |
| T13 | distractor (non_authoritative_instruction) | slack | `C090N54TG79/1758569824.148029`, `C090N54TG79/1758569885.985319` | R4 | a board of grenades and shuriken (Julia's own 22 Sep idea) | base: Robert answered 'remain as is'; his eight are the board | — |
| T14 | distractor (partial_listing) | slack, gslides | `f_6a2fa8e61b31139ca8e3d4`, `C08H78VJG80/1757956024.883249`, `D076RBM29JS/1758638743.317009` | R4 | the board is grenade, couch and plush doll (Frederick's 15 Sep 'good start', and the reference level as built) | that was the reference level; the vendor asked for an 8-item set and Robert's 25 Sep post names the eight | — |
| T15 | mutable_pointer | gslides, slack | `f_6a2fa8e61b31139ca8e3d4`, `C090N54TG79/1758823946.262829` | R4 | the items on Julia's deck are the board the vendor builds | the deck is the level as built on 23 Sep; Robert's eight came two days later | the notes send the reader to the deck for what was built |
| T16 | scope_alias | slack, gsheets | `f_956e60ec7f2f7977d98934`, `C08H78VJG80/1758723504.085039`, `C08H78VJG80/1758729487.922339`, `C08H78VJG80/1758283671.878269` | R1 | PlayableX's 'duck asset' and 'rocket launcher' are lines missing from the list | base: the duck is the Plushie Chick Brian sent the same day; the launcher is the Cannon line | — |
| T17 | distractor (lookalike_entity) | gdocs | `gdocs:f_05bedd1540d3e01a90ab16` | R2 | Leonard's Playable Feedback (P0, P1, P2) is the rule for what is ready | that doc is feedback on the first playable; the notes for this one are Frederick's | — |
| T18 | near_miss_mention | github | `harmonygames-Games/match3d#462#c_1`, `harmonygames-Games/match3d#460` | R2 | every item match3d#462 or #460 touches has to go again (Kettlebell, Dart Board, Candy; the shared texture atlases) | Kettlebell, Dart Board and Candy are not lines of the pack; #460 adds new objects and names no line's art as changed | — |
| T19 | distractor (keyword_collision) | linear | `ZOM-97` | R6 | the object tickets under ZOM-97 (REVISION FOR ITEMS: Bathtub, Iron, Washing Machine, ...) are the lines' tickets | the pack list names each line's ticket; the notes say tickets live under Brian's pack ticket | — |

Supersession chronology (oldest first, timestamps from the records): T2 Brian's note on DES-349 2025-09-26T11:20Z → `D05GU6L0XFH/1759178332.042459` 2025-09-29T20:38:52Z; T3 Brian's note on DES-389 2025-09-25T08:05Z → base `C090N54TG79/1759189466.554739` 2025-09-29T23:44Z → `f_faf4d7c167d14a1127dcc3` 2025-09-30T09:12:26Z (three versions; the pull request `harmonygames-Games/match3d#462`, merged 2025-09-25T23:15Z, is the change behind the second); T5 `C090N54TG79/1758823946.262829` 2025-09-25T18:12:26Z → `C08R8CHB0QL/1758922879.243189` 2025-09-26T21:41:19Z; T8 `C08H78VJG80/1758022459.227279` 2025-09-16 → `C08H78VJG80/1758701898.919999` 2025-09-24 → `C08H78VJG80/1759226395.551469` 2025-09-30 (three versions); T15 `f_6a2fa8e61b31139ca8e3d4` 2025-09-23T19:55:00Z → `C090N54TG79/1758823946.262829`. Every seeded timestamp is before the seed bound; the only later value is the plan field of the hold (start 2025-11-03T17:00Z).

**Hardness v2 trap selection.** Two separate cross-source decisions carry the difficulty, each naming the convincing wrong source and the record that beats it: (1) trap 1, proving done across services — EXPORT: the ticket note on DES-367 (Brian, 25 Sep: .fbx, opens, in the outgoing folder) against Marcus's 26 Sep post in #zombie-match3d `C0880U9751A/1758906517.912099` (he tested the zombie pack that day; later; another service), joined to the vendor's binary-only rule `C08H78VJG80/1758022459.227279`; (2) trap 2, a correction somewhere else — ARTHOLD: Brian's note on DES-349 (Friday's file looks right) against Robert's 29 Sep note to Julia `D05GU6L0XFH/1759178332.042459` (he follows the art; later; another service; the artist tagged, not named). Four more are used: a completion note elsewhere (REVISED, v2 move A25: the re-send in `f_faf4d7c167d14a1127dcc3` undoes Robert's base post), trap 5 a rule in the data (AUDIO, `f_b2387e31d46d3a7b3fa2a9`), trap 2 again (PICKS: a later reply `C08R8CHB0QL/1758922879.243189` that names no item), a second document by the list's owner (ZIP, `f_faf4d7c167d14a1127dcc3`), trap 9 work already done (T10: the zombie pack `C08H78VJG80/1758906043.375719`). No correction sits in the superseded record's container, in an anchor's container or on a delegation path (`hardness_v2_check` SAME_PLACE below). Volume and arithmetic carry no difficulty.

### Mechanism portfolio (S5a)

Candidates considered (grounded in the fact pack and the census files) and the selection:

| # | Candidate | Coupling | Verdict | Reason (record) |
|---|---|---|---|---|
| 1 | EXPORT: FBX files saved out of the Unity project are the text kind | ticket 'FBX, opens, looks right' → format the vendor refuses → Owed | selected | the vendor's rule is base (`C08H78VJG80/1758022459.227279`, `C08H78VJG80/1758283671.878269`) and reached Julia herself (`D05SD5QLG94/1758220925.518329`); colours are assigned in Unity in base, which is why Brian would export from the project |
| 2 | ARTHOLD: the artist is redoing one category's UVs, said by someone else | ticket note → Robert's DM with Julia → Owed (art, Claire) | selected (D3 carrier) | Robert follows the art (`C08R8CHB0QL/1758752145.583769`, `C090N54TG79/1759189466.554739`) and talks with Julia daily in `D05GU6L0XFH`; in D2 Claire's own DM was returned by a search for her messages in 6 of 7 rev1 runs (01a_Hardening_Report.md §4) |
| 3 | REVISED: the three recoloured items were sent again (completion note elsewhere) | note → Robert's base post (Owed) → Brian's log (Ready) | selected (D3 rebuild) | in D2 the change itself decided (base `harmonygames-Games/match3d#462`, `C090N54TG79/1759189466.554739`) and 7 of 7 rev1 runs read it in #zombie-design; the completion sits in `f_faf4d7c167d14a1127dcc3`, which no rev1 run found by its own name |
| 4 | AUDIO: only sound that is ours is handed over | file type passes → sources sheet → Owed | selected | base: Robert sources sound from a Soundly seat and bought packs (`C07JYF2CFFU/1737054449.137119`) and two sounds were already a copyright problem (`D05GU6L0XFH/1757519060.984519`) |
| 5 | PICKS: Robert changes one pick in a reply elsewhere, naming no item | the eight → reply → board set and the brief | selected | parent `C08R8CHB0QL/1758904025.123869` is Julia's own base post about the bow; the reply says 'it' and 'the last one on my list', so no item name makes it a search hit (path exposure, §12) |
| 6 | ZIP: one zip that will not unpack, noted in the packer's own log of the outgoing folder | tickets say in the folder and fine → the log → Owed | selected | a comment on the pack ticket DES-313 would sit on a named record (path exposure flagged it); the log `f_faf4d7c167d14a1127dcc3` is a second document by the list's owner that nothing links |
| 15 | six items Robert adds to the list in his reply (D2 before the path-exposure run) | reply → six new lines and tickets | rejected | a reply that names items is the newest Slack hit for each name (`path_exposure.py`: EXPOSED on `C08R8CHB0QL/1758922879.243189`), so it would be found by every keyword sweep |
| 7 | an 'object browser' whose batch export writes empty shells (D1) | ticket 'exported' → tool bug → Owed | rejected | no such tool exists in base and Arthur has no such post (reviewer 1, finding 4; `C0880U9751A/1738678859.796159` is the kind of post base does have) |
| 8 | Unity packages with prefabs only, as with the zombies | ticket 'exported' → hollow package → Owed | rejected | a Unity package is not a format the vendor takes for 3D (`C08H78VJG80/1758022459.227279`), so the lines would be Owed on the hub's own text with nothing to find |
| 9 | item effects as shipped (a design line per item) | ticket text → pull request review | rejected | effects are spread over dozens of base messages in #zombie-design `C090N54TG79`; any seeded effect risks a base contradiction |
| 10 | which zombies have full animation sets | enemy set → animations channel | rejected | five of the nine zombie names are masked in base (`C09ATAJ220H/1758881579.188609`) and card SC-58 covers the roster on `page_zm3d_gdd` |
| 11 | UI pieces changed after the first zip | sent UI → later pull request | rejected | base does not say UI went in the zip, and `harmonygames-Games/match3d#460` and the later UI pull requests do not name pieces: a fork |
| 12 | a due date on a calendar hold against 'a week before' | rule arithmetic → hold | rejected | two fair dates with no resolving record; the hold `evt_421695d009e589ee85296c` is kept only for its attendees |
| 13 | open art tickets as 'somebody is changing it' (Maracas, Helmet, Indoor Plant) | ticket state elsewhere → Owed | rejected | card SC-16: `ZOM-513` and `ZOM-514` are open after the work shipped; those objects are kept off the list instead |
| 14 | a brief that is valid under each pivot option | pivot options → brief | rejected | the options are undecided in base (`C090N54TG79/1759114097.776589`): no truth value |
| 16 | D3: Claire's UV note as a comment on the bathroom tickets | ticket comment → Owed | rejected | every rev1 run read all 96 tickets' comments: a correction there is on the first-read path |
| 17 | D3: the bathroom redo in a reply under a #zombie-art post | thread reply → Owed | rejected | PICKS already uses a thread reply; a second unit behind the same habit would not be independent (difficulty_budget independence) |

**Selected rules** (one per solver rule; draft manifest `mechanism_portfolio`). Ledger priors for `claude-opus-5-5`, UNCALIBRATED (`hardness_ledger.py priors`; `plan/out/ledger_priors.txt`):

| Rule | Mechanism | Prior family · prior · record ids | Natural reading | Decides | Control · over-application | Stays hard after complete retrieval | Natural call that returns the decider | Slots only it flips |
|---|---|---|---|---|---|---|---|---|
| EXPORT | A24 | done_gap · Beta(1.0, 2.86) mean 0.26 · `hev_7af7471ca0d3855f`, `hev_bdb9590893044914`, `hev_e30a8c13fa044076` | the twelve are Ready | State, What's owed, Who has it | Rolling Pin (a kitchen line from Claire) · export_over | reading 'the text kind' as ASCII against the vendor's binary-only rule, and joining 'saved out of unity on thursday' to the twelve notes that say 'saved out of the project, Thu 25 Sep' in two categories | `slack_read_channel` on #zombie-match3d for the week → `C0880U9751A/1758906517.912099` | X1, X1b, X6, X16, W4, K1 |
| ARTHOLD | A11 | superseding · see `plan/out/ledger_priors.txt` (now with the rev1 runs) | the twelve are Ready | State, What's owed, Who has it | Desk Lamp (a Friday file from Claire outside Bathroom) · art_over | mapping 'the bathroom objects' to the list's category, the iron and the washing machine included, and the tagged artist to the holder | reading Julia's DM with Robert for 29 Sep → `D05GU6L0XFH/1759178332.042459` | X2, X2b, X7, X11, X11b, K2 |
| REVISED | A25 | completion_elsewhere · see `plan/out/ledger_priors.txt` (ZIP's rev1 runs are in it) | the three are Owed (the file again, Claire) | State, What's owed, Who has it | Fly Zapper (a line waiting on Claire's FBX) · revised_over | joining 'the three recoloured models' through Robert's post to three lines in three categories, and letting the latest record win over Robert's post | a Drive search for the outgoing folder, then the document → `f_faf4d7c167d14a1127dcc3` | X3, X3b, X8 |
| AUDIO | A13 | authority · Beta(1.0, 2.86) mean 0.26 · `hev_c4bbc05b4e9b08ea`, `hev_923eb1fef7d8dc20`, `hev_0eec4f03fda7d5a4` | all five exported cues are Ready | State, What's owed, Who has it | Success sound (made here) · audio_over | applying the rule to a source column and carrying it into the brief | a Drive search for the sound sheet, then its rows → `f_b2387e31d46d3a7b3fa2a9` | X5, X5b, X10, X12, K5, B6 |
| PICKS | A14 | superseding · same prior and records as ARTHOLD | dynamite in the eight | Board set | Grenade (unchanged pick) · picks_over | resolving 'it' through the thread parent and 'the last one on my list' through the order of his 25 Sep post | `slack_read_thread` on Julia's bow post `C08R8CHB0QL/1758904025.123869` → `C08R8CHB0QL/1758922879.243189` | X13, X14, B1 |
| ZIP | A25 | completion_elsewhere · no ledger record for this family: UNPARAMETERIZED (prior Beta(1,1)) | the eight are Ready | State, What's owed, Who has it | Music Keyboard (an instrument outside Friday's zip) · zip_over | joining 'Friday's music instruments' to the eight notes that say zipped | a Drive search for the outgoing folder, then the document → `f_faf4d7c167d14a1127dcc3` | X4, X4b, X9, X17, K4 |

A5b checks per rule: **incorporated** — each state follows from the notes (K1) applied to records Julia can read; **survives complete retrieval** — each needs a join after the record is found (note or category → lines); **tool-surface proof** — every decider is a top-level message, a ticket comment, a sheet or a base pull request comment that the named call returns (no DM thread reply, no attachment body); **graded weight** — each flips at least two weight-5 slots. No liveness flag is resolved by removing an incorporation link.

### Liveness flags (S5b)

`trap_liveness.py --design` (advisory, UNCALIBRATED; verbatim):

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · DESIGN (no SQL: record text unavailable, only manifest-structure flags can fire) · on the Season Pass backtests these are development fixtures, not validation
  hub D05SD5QLG94/1759256494.852159 · direct delegations 7 · rule placement: SKIP for every node: the mechanism_portfolio declares no A15 node
  T1   done_gap           -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T2   superseding        -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T3   superseding        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T4   authority          breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T5   superseding        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T6   exact_predicate    -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T7   completion_elsewhe breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T8   effective_date     breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T9   distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T10  completion_elsewhe -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T11  scope_alias        -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T12  distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T13  distractor         breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T14  distractor         breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T15  mutable_pointer    breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T16  scope_alias        breadcrumb, order  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T17  distractor         breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T18  near_miss_mention  -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T19  distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  dispositions: 0/11 recorded
```

Dispositions:

| Traps | Flag | Disposition |
|---|---|---|
| T1 | breadcrumb | the vendor's binary-only rule is on the hub path (`C08H78VJG80/1758022459.227279`) and the notes say a later word from someone who knows the file counts: both are the fairness path, kept. Neither names #zombie-match3d or Marcus, and the post `C0880U9751A/1758906517.912099` shares no word with the ask. |
| T2, T7 | breadcrumb | the notes `f_8c1d0bca1d1d5fde4c5008` give the rule (later statements count; nobody changing it) and no place. Kept. |
| T4 | breadcrumb | the notes carry the sound rule, as they must for incorporation; they do not name Calvin's sheet `f_b2387e31d46d3a7b3fa2a9`, its title or its owner. Kept. |
| T5, T6, T15 | breadcrumb | the ask `D05SD5QLG94/1759256494.852159` says 'unless he's changed them since' and the notes add Robert's later items: they authorise a later change and give no place, date or word of it. The reply is under a post about an arrow in another channel. Kept; the wording sweep on the SQL checks that the reply shares no rare word with the ask. |
| T3, T8 | breadcrumb | T3: the changed-art rule is in the notes and Robert's post is base (`C090N54TG79/1759189466.554739`); the completion is in Brian's log `f_faf4d7c167d14a1127dcc3`, which nothing links. T8's dates are base (`C08H78VJG80`); a realism trap with no budget weight. |
| T9 to T19 (distractors and aliases) | breadcrumb | on the read path by design (`C08H78VJG80`, `C090N54TG79`, `page_zm3d_gdd`); none carries budget weight. |

A trap the tool flags and the table does not name is covered by the last row.

`hardness_v2_check.py --design` (verbatim):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      5 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 3 requirements: {'R2': ['EXPORT', 'REVISED', 'AUDIO'], 'R3': ['ARTHOLD', 'ZIP'], 'R4': ['PICKS']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   6 of 6 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Dispositions: no FLAG and no UNRESOLVED. SAME_PLACE is re-run on the SQL. INPUT_CHECK reports no weight-5 total: the three counts are weight 3 (calculation) and five rules move two of them, so neither is plain arithmetic on clean inputs. RULE_IN_PROMPT runs when the prompt exists.


## 6 Failure-diversity plan

Each unit is one deciding record behind its own retrieval habit; in D3 Brian's folder log carries two rules (ZIP and REVISED), so a run's misses are a subset of five independent records. Find rates are the counts measured in the seven rev1 runs, adjusted only where D3 removes a route (each basis names the runs and events). The comment, move, create and share writes are declared templates, so the rubric skeleton is the surface plus volume rows (55 rows, weight 195): the budget is computed on the sampled shape a rubric can defend, not on one row per comment. Budget table (`difficulty_budget.py table`):

| Unit | Role | Carrier | Decider | Habit | Find rate | Rows (weight) | Weight share |
|---|---|---|---|---|---|---|---|
| A1 | anchor | second_carrier_by_rule_owner | gdocs f_faf4d7c167d14a1127dcc3 (injected) | gdocs / get_document_text | 0.10-0.40 | S4 (5), S10 (5), S16 (5), S22 (5), S37 (3), S3 (5), S8 (5), S9 (5), S28 (3), S31 (3) | 22.6% (44 of 195) |
| A2 | anchor | dm_with_non_owner | slack D05GU6L0XFH/1759178332.042459 (injected) | slack / read_dm | 0.15-0.45 | S2 (5), S7 (5), S15 (5), S19 (5), S20 (5), S36 (3), S29 (3), S32 (3) | 17.4% (34 of 195) |
| C1 | variance | de_named_root_record | slack C0880U9751A/1758906517.912099 (injected) | slack / read_channel | 0.30-0.57 | S1 (5), S6 (5), S14 (5), S18 (5), S34 (3), S35 (3) | 13.3% (26 of 195) |
| C2 | variance | second_carrier_by_rule_owner | gsheets f_b2387e31d46d3a7b3fa2a9 (injected) | gsheets / values_get | 0.70-0.95 | S5 (5), S11 (5), S17 (5), S21 (5), S38 (3), S46 (5) | 14.4% (28 of 195) |
| C3 | variance | reply_under_unrelated_parent | slack C08R8CHB0QL/1758922879.243189 (injected) | slack / read_thread | 0.30-0.57 | S23 (5), S24 (5), S39 (5) | 7.7% (15 of 195) |
| R1 | realism | same_container_supersession | n/a | n/a | n/a | not counted | 0% (realism) |

Mode hard (cap 70.0%, loss 30.0%); weights from skeleton, total 195. Anchors: 40.0% of weight from 2 cause(s) (needs 32.0%). Coin-flip units: 35.4% of weight over 3 independent habit(s), 0 inside the find-rate window (needs 4).

`difficulty_budget.py check` (verbatim):

```
DIFFICULTY BUDGET (hard): FAIL
[PASS] budget.schema: 6 units (2 anchor, 3 variance, 1 realism), design D3, revision D3-design.
[PASS] budget.context: mode hard is the assigned difficulty mode.
[PASS] budget.rows: Every row matches its basis. Weights and total come from 01_Rubric_Skeleton.json: 33 rows over 5 units, total weight 195. Realism units ignored: R1.
[PASS] budget.carriers: All 5 anchor and variance units use carriers that produced misses.
[PASS] budget.unit_rows: Each of the 5 anchor and variance units flips at least 2 rows, one of weight 5.
[PASS] budget.independence: 5 units, 5 independent habits; no two units share a habit.
[FAIL] budget.anchors: find rate above 0.20: A1 (up to 0.40), A2 (up to 0.45) (a record found that often is a variance unit).
[FAIL] budget.variance: 0 independent coin-flip habit(s) with a find-rate range inside 0.35-0.65, needs 4 (3 variance units over 3 habits; outside the range: C1 (0.30-0.57); C2 (0.70-0.95); C3 (0.30-0.57)). Four independent coin flips are what keeps the largest signature at or under half of the failing runs.
[FAIL] budget.average: P(six-run average strictly under 70.0%) is 1.000 with every unit at its low find rate and 0.764 at its high find rate (needs 0.90 at both). Put more weight on anchor and variance rows, or lower the weight of rows every run passes.
[PASS] budget.full_passes: P(fewer than 5 full passes) is 1.000 with every unit at its low find rate and 1.000 at its high find rate (needs 0.90 at both).
[PASS] budget.signature: P(largest signature at most 50% of failing runs, two or more signatures) is 0.950 with every unit at its low find rate and 0.985 at its high find rate (needs 0.90 at both).
[FAIL] budget.signature_one_error: P(signature gate with 5 completed runs) is 0.842 with every unit at its low find rate and 0.959 at its high find rate (needs 0.90 at both). One errored run would sink the signature gate; add an independent coin-flip unit.
[WARN] budget.spread: P(SD inside 0.1-0.3) is 0.626 / 0.796 / 0.840 at the low / middle / high find rates; the design carries 35.4% of weight on coin-flip (variance) units and 40.0% on anchors. Below 0.70: a spread miss is likely; move more weight onto coin-flip units (about 60% of weight reaches 0.8) or accept that the miss is reported.
[WARN] budget.hard_mode: Hard mode: the 30.0% loss figure is 1 - cap, not a line from a platform /hardness report, so the anchor share target is unverified.
```

`rubric_skeleton.py check` (verbatim):

```
RUBRIC SKELETON (check): PASS
[PASS] skeleton.present: Working_Files/01_Rubric_Skeleton.json: 55 rows
[PASS] skeleton.bound: bound to 4 current input file(s)
[PASS] skeleton.share: anchors 78 of 195 = 40.0% (needs 32.0%: hard loss 30.0% + margin 2.0%); coin-flip 35.4% (budget declared 35.4%); always-pass 24.6%
```

Whole policies and single misses on the skeleton, and the six-run simulation (`plan/policy_scores.py`, UNCALIBRATED; verbatim):

```
Rubric skeleton: 55 rows, total weight 195; budget basis skeleton  (UNCALIBRATED)

Whole policies:
  100.0 %  reads everything
   24.6 %  the ask, the notes, the pack list, the channel and every line's own ticket; nothing else
   39.0 %  that, plus a Drive search for where the sounds came from (6 of 7 rev1 runs)
   60.0 %  that, plus #zombie-match3d for the week and Julia's bow thread
   60.0 %  everything except the two anchor records
   58.5 %  both anchors found, every coin-flip record missed

Single misses (everything else found):
   74.4 %  miss A1 (ZIP, second_carrier_by_rule_owner)
   79.5 %  miss A2 (ARTHOLD, dm_with_non_owner)
   80.5 %  miss C1 (EXPORT, de_named_root_record)
   79.5 %  miss C2 (AUDIO, second_carrier_by_rule_owner)
   92.3 %  miss C3 (PICKS, reply_under_unrelated_parent)

Six-run simulation, 20,000 trials per setting:
  setting    E[avg]   P(avg<70)  P(<5 full)  P(SD band)  P(patterns)  P(ALL GATES)  mean SD
  low find    40.1 %   1.000      1.000       0.564       0.949        0.553       0.107
  midpoint    51.5 %   0.998      1.000       0.721       0.987        0.711       0.127
  high find   63.2 %   0.853      1.000       0.776       0.983        0.633       0.136
  anchors@0.5 56.1 %   0.976      1.000       0.831       0.998        0.807       0.146
  all@0.65    67.2 %   0.655      1.000       0.851       0.986        0.537       0.148

Targets: E[avg] <= 62 %, P(all gates) >= 0.5. The last two rows are sensitivity runs outside the budget's ranges.
```

**Reading (D3).** The budget check fails in warn mode, and the failures are honest: the rates are measured, not chosen. The two anchors are found more often than 0.20 at their high ends (the log up to 0.40, Robert's DM up to 0.45), and no coin-flip unit sits wholly inside 0.35 to 0.65 (EXPORT and PICKS 0.30 to 0.57; AUDIO is found 0.70 to 0.95 and is kept as designed, since no v2 move was chosen for it). What matters for the gates is the simulation above: at the midpoint E[average] is about half and P(all gates) about 0.7; at the high find rates the average still clears the cap in most trials; the spread chance is the weakest figure, as in D2. The family-prior forecast in §12 is more pessimistic (E[average] about two thirds), because its completion_elsewhere prior holds the rev1 runs that found the log through the sound search D3 removes. Both are uncalibrated; the next pre-check measures D3. No single miss clears the cap by itself (single-miss table above), and a run that finds both anchors and misses every coin flip scores under 60 %.

**Which runs miss what (rev1 habits, 01a_Hardening_Report.md §8).** A1, the folder log, is found by a run that looks in Drive for the outgoing folder the notes and tickets name (no rev1 run did; three searched Slack for it). A2, Robert's note, by a run that reads Julia's DM with Robert around 29 Sep or sweeps her DMs by date (three of seven); a search for Robert's own messages stops at the newest fifty, which do not reach it. C1, Marcus's post, by a run that reads #zombie-match3d for the week or searches Marcus's messages (three of seven once the note's own words are gone). C2, Calvin's sheet, by a Drive search for where the sounds came from (six of seven). C3, Robert's reply, by a run that opens Julia's bow thread (three of seven). The five habits are different calls in three services. No single record decides more than 44 of 195 weight.

**Lessons applied** (`00_Pre_Scenario_Analysis.md` §9b; Frederick's rev10 forensics, `task_inputs-uselater/Working_Files/01a_Hardening_Report.md` §8): in twelve runs a broad Slack search on the task's key noun returned every correction that held it. Here no deciding record contains 'playable', 'PlayableX', 'pack', 'brief', 'hand-off', 'asset', 'FBX' or 'vendor'; the SQL wording sweep at `/create-injection` enforces it. Inline review comments are not used. Every miss moves the counts in one direction (Owed up, Ready down), so misses cannot cancel in the reply.


## 7 Deliverables and dependent writes

| Write | Tool | Count | Depends on | Requirements |
|---|---|---|---|---|
| gsheets | `gsheets_create_spreadsheet+gsheets_values_update` | 2 | K1, K2, C1, C2, C3, C4, C5, C6, T6 | R1, R2, R3, R4, R7 |
| gdocs | `gdocs_create_document` | 1 | K3, K6, K9, K10, K12, K13, K15, C4, C5 | R5, R7 |
| linear | `linear_create_comment` | 49 | K1, K4, C1, C2, C3, C5, C6 | R6 |
| linear | `linear_update_issue` | 49 | K1, K4, C1, C2, C3, C5, C6 | R6 |
| gdrive | `gdrive_share_file` | 8 | K7, K8 | R7 |
| slack | `slack_send_message` | 2 | A1, A2, C1, C2, C3, C5, C6 | R7 |

- **Hand-off list** (Google Sheet in Julia's Drive `d_8140f09bf9f1b94cb8ee2d`): one row per line of Brian's list (96); the notes name the columns: Line, Category, Board set, State, What's owed, Who has it, Ticket. The truth of 'Who has it' is the person's first name (`plan/design_model.py` field `who`), compared as a whole word, so 'Brian' and 'Brian Foster' both pass. Totals 8 / 39 / 49. Board set is Default for the eight (Grenade, Couch, Plushie Chick, Shuriken, Cute Axe, Gift Box, Bow, Cactus Plant), Extra for every other board item, empty otherwise.
- **Brief** (Google Doc in her Drive), covering what the notes list: Scenario 1 and what it is for (filtering for players who will like the game, true to the core game play); the eight on the board and the extras they can swap in; the four zombies (Party Girl, Plumber, Magician, Football Player) and the one animation (walk); a level is won when every zombie is eliminated and lost when they take the player's health to zero; a 7-slot tray; sound: the cues that are ours, the rocket and explosion cues held back until we have our own, and when the music may start (after the first click, the vendor's rule of 14 Apr); start 3 November. Free-text parts are bounded: any wording that states these facts is accepted.
- **Tickets:** the 49 Owed lines that have a ticket go to Todo (each starts In Progress) with a comment saying what is owed and who has it; no ticket is created. The 47 Delivered and Ready tickets are left as they are. The surface grades one named ticket's final state, comment and ticket text by content, and the counts on the list; the exclusion and the per-ticket targets are rubric rows the grader cannot decode (selector guide §2, §3), named here for the rubric stage.
- **Shares:** both files, view only, to the three other attendees of the kickoff hold and to PlayableX's intake address (eight share calls).
- **Messages:** the three counts to Frederick in `D05SD5QLG94`; both links in `C08H78VJG80`.

Every write's content depends on findings (`depends_on`); none is a bolt-on. Each is asked for by the ask or the notes (a trigger Julia owns), and each target is hers to write: she owns both new files, is a member of both Slack conversations (`can-see` YES), and is a member of `team_DES` in Linear (`/team_memberships`).


## 8 Service role map

| Service | Role | Load-bearing fact or write | Carrier |
|---|---|---|---|
| slack | the ask (Frederick's DM); the PlayableX channel; Robert's eight, his zombie answer and his later reply; Marcus's post in #zombie-match3d; Robert's note to Julia about the bathroom objects; writes: the counts and the links | the hub, three of the six deciding records and both messages | ● message text, thread replies, DMs |
| linear | Brian's pack ticket DES-313 and its 96 children with his note on each; writes: Todo moves and comments | the per-line evidence and the ticket follow-through | ● title, state, parent; comments ● per §6b |
| gsheets | Brian's pack list; Calvin's sound sources sheet; write: the hand-off list | the line set, the sound decision and the main deliverable | ● grid |
| gdocs | Frederick's hand-off notes; Brian's log of the outgoing folder (the broken zip and the three re-sent items); write: the brief | every rule of the task, the deciding record of two rules and the second deliverable | ● body_text |
| gdrive | where the notes, the list and the deck are found; write: view-only shares of both files | discovery of the shared files and the sharing | ● name, parents, sharing |
| gslides | Julia's deck of the reference level (the three item types as built on 23 Sep) | what was built for the vendor; the older state of the board | ● element text |
| gcal | Frederick's kickoff hold on 3 Nov (attendees) | who both files are shared with | ● summary, start, attendees |
| contacts | PlayableX's intake contact | the address both view links are shared with | ● email, job |
| github | base pull request match3d#462 and its comment (the 25 Sep model change behind Robert's new colour versions) | corroboration only; no line's state rests on it | ● PR title, dates, comment (base) |
| confluence | the design page and its comments (7-slot tray, loss only at zero health) | two facts of the brief | ● page body, comments (base) |
| trello | Leonard's Playable Kickoff card with his comment | the decoy for 'the kickoff'; a status mirror of the pause | ● card, commentCard action |
| gmail | invitation mails for the kickoff hold in the attendees' mailboxes | companions of the hold; carry the same attendee list | ● invitation mails (companions) |
| snowflake | not used | none: nothing in the pack is measured in the warehouse, and Snowflake cannot be injected | — |

## 9 Call budget

| Phase | Service | Calls | Reason |
|---|---|---|---|
| discovery | slack | 10 | the ask in Frederick's DM; the PlayableX channel (two pages and its two long threads); Robert's two posts in #zombie-design; the 22 Sep playable thread; Julia's DM with Brian about the reference level |
| discovery | gdocs | 2 | Frederick's hand-off notes; Leonard's Playable Feedback (rejected: the first playable) |
| discovery | gdrive | 3 | find the notes, the pack list and the deck shared with Julia; look at her own root for the destination |
| discovery | gsheets | 2 | Brian's pack list: sheet metadata and its rows |
| discovery | gslides | 1 | Julia's deck of the reference level |
| discovery | confluence | 2 | the design page and its comments (tray size, how a level is lost) |
| discovery | gcal | 2 | find the kickoff hold and read its attendees |
| discovery | contacts | 1 | PlayableX's intake address |
| discovery | trello | 2 | the Playable Kickoff card and its comment (rejected as the recipient source) |
| enumeration | linear | 3 | the pack ticket and two pages of its 96 children (keys, states) |
| per-record | linear | 96 | each line's ticket comments: Brian's note on what he did with the line |
| reconciliation | gdocs | 2 | Brian's log of the outgoing folder: find it and read it |
| reconciliation | slack | 8 | #zombie-art since 24 Sep and Julia's bow thread; her DM with Robert; #zombie-match3d for the week; #zm-animations for the zombie pack |
| reconciliation | gsheets | 2 | Calvin's sound sources sheet: find it and read its rows |
| reads-before-writes | linear | 3 | team, states and users for the ticket writes |
| per-record | linear | 98 | each of the 49 Owed lines with a ticket: a state write (In Progress to Todo) and a comment saying what is owed and who has it |
| writes | gsheets | 2 | create the hand-off list in Julia's Drive and write its 96 rows |
| writes | gdocs | 1 | create the brief with its text |
| writes | gdrive | 8 | share both files view-only with the three other people on the hold and PlayableX's intake address |
| writes | slack | 2 | the three counts to Frederick in his DM; both links in the PlayableX channel |
| read-back | gsheets | 1 | read the list back against the pack list's rows |
| read-back | linear | 1 | list the pack ticket's children to confirm the Todo set |

Total 252 unconditional calls over 11 services; per-record 194 in these rows (the gate output in §12 also counts the folder-log surface's two calls). No row is conditional on an unverified tool behaviour; one unverified tool is on the pre-check list by name: `linear_show_data` (Ask_Carriers marks it a possible bulk read), with the `query` parameter of `linear_list_issues`. **Golden-run rule:** a correct run needs the volume: 96 comment reads fill the state column, 49 moves and 49 comments are the follow-through. **Every-run floor:** a run that finds no hidden record still reads the 96 tickets' notes, because nothing else says which lines are exported, and moves and comments the 15 lines that are Owed on their own note: about 40 discovery and rule calls + 96 reads + 30 ticket writes + 13 for the two files, the shares and the messages ≈ 179 counted calls, over the requester's 130. A run that samples tickets instead of reading them loses the totals and falls under the floor; if the pre-check comes in under 150 calls the design is revised before any baseline.


## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by | Evidence |
|---|---|---|---|---|
| How many lines | 96: the rows of Brian's list | more, with the vendor's asks or the reference level's variants added | the notes: one row per line of Brian's pack list; the ask has no clause about the vendor's requests | `f_8c1d0bca1d1d5fde4c5008`, `f_956e60ec7f2f7977d98934` |
| Twelve lines saved out of the project | Owed, export again as binary (Brian) | Ready: FBX, opens, looks right, in the outgoing folder; or Owed on suspicion, without the post | Marcus: those files are the text kind; the vendor takes binary only; the notes: a format they take, and a later word from someone who knows the file counts. Without the post the note passes every Ready test on its face and 'take it as it stands' applies, so suspicion alone is not a fair Owed | `C0880U9751A/1758906517.912099`, `C08H78VJG80/1758022459.227279` |
| Twelve exported bathroom lines | Owed, the art (Claire) | Ready: Friday's files open and look right; or Owed with Robert or Brian | Robert says later that Claire is redoing the UVs and Friday's files are the old version; the notes leave a changed file with whoever it came from, and the twelve notes say 'FBX from Claire' | `D05GU6L0XFH/1759178332.042459` |
| Cactus Plant, Chainsaw, Cone | Ready: sent again with the new colours, opens, looks right | Owed, the file again (Claire): Robert's new colour versions came after their 25 Sep files | Brian's log of 30 Sep, the latest record: Claire sent the three recoloured models again, they open, look right and replace Thursday's (Robert's post says which three). A reader who takes colour versions as additions also arrives at Ready | `f_faf4d7c167d14a1127dcc3`, `C090N54TG79/1759189466.554739`, `f_8c1d0bca1d1d5fde4c5008` |
| Kettlebell, Dart Board, Candy; the shared atlases | not lines; nothing to do | lines to add or delivered files to send again | they are not on Brian's list and Robert did not add them; #460 adds objects and names no line's art | `harmonygames-Games/match3d#462`, `harmonygames-Games/match3d#460` |
| Eight instruments in Friday's zip | Owed, put the files back (Brian) | Ready: each file opens and looks right, and Brian still has it | the notes: Ready is 'sitting in the outgoing folder, it opens'; Brian's log: that zip will not unpack and the eight are not in the folder any other way | `f_faf4d7c167d14a1127dcc3` |
| Rocket sound and Explosion sound | Owed, our own version (Calvin) | Ready: .wav is a type the vendor takes and it plays | the notes hand over only what is ours; Calvin's sheet marks both 'no' and names him for our own version | `f_b2387e31d46d3a7b3fa2a9` |
| The eight on the board | with the bow, without the dynamite | with the dynamite (25 Sep); or the reference level's three; or the bow in place of some other item | Robert's own later reply: 'it' is the bow of the post he answers, 'the last one on my list' is the dynamite, the last item of his 25 Sep post; the ask keeps his latest word | `C08R8CHB0QL/1758922879.243189`, `C090N54TG79/1758823946.262829` |
| The bow's own state | Ready | Owed: Claire agreed to add an arrow | Robert's reply: the bow as it is now, the arrow as its own item later; and the bow's file is of Mon 29 Sep, after Friday's thread | `C08R8CHB0QL/1758922879.243189`, `C08R8CHB0QL/1758904103.894649`, DES-335 |
| The zombie characters | Delivered | Owed: the vendor said the package was not exported correctly; or the project's shaders changed | base: Marcus's tested pack went on 26 Sep and the vendor reviewed it on 29 Sep and asked for a choice, not files; the pack's files did not change | `C08H78VJG80/1758906043.375719`, `C08H78VJG80/1759140968.965099` |
| What the first zip held | the reference level's items, the cannon, the background, the zombies | everything on the vendor's list, since 'the only missing piece' was the duck | the pack ticket says what the first zip was and the sound, 2D and font tickets say in words that they did not go; the vendor's sentence is about the reference | DES-313, `C08H78VJG80/1758723504.085039` |
| The cannon and the zombies after match3d#469 | Delivered | to send again: #469 (30 Sep) touches the import settings of the cannon's and the monsters' source files | its own comment: default importer fields added, no existing field changed; the delivered files are not art that changed | `C08H78VJG80/1758906043.375719`, `harmonygames-Games/match3d#469` |
| Music Keyboard, Grenade and the open rendering ticket | Ready and Delivered as their notes say | somebody is changing them: ZOM-449 (Backlog since July) names them among items with artifacts on low-end devices | that ticket is about rendering on low-end Android, assigned to engineering, untouched since July; nobody is changing the models | `ZOM-449`, DES-387 |
| Tray size | seven slots | six (Julia's July proposal) | base: Robert's reply keeps the page at seven | `page_zm3d_gdd`, `confluence:comment_zm3d_gdd_c2` |
| Start date | 3 November | 6 October | base: the vendor's latest message | `C08H78VJG80/1759226395.551469` |
| Who the files are shared with | both files, view only: the three other attendees of the hold and the intake address | the brief only; or Leonard (his card is the 'kickoff') | the notes: 'Sharing: both files, view only', the kickoff hold and Contacts | `evt_421695d009e589ee85296c`, `d7d31caf63ee33db2b7ed271` |
| Where the counts go | Frederick's DM, as a message or a thread reply under his ask | the PlayableX channel | the ask: 'give me the count for each state here'; both forms in the DM are accepted | `D05SD5QLG94/1759256494.852159` |
| Ticket follow-through on an Owed line | Todo plus a comment, also for the lines Owed on their own note | a description edit, or a new ticket; or nothing for a line whose note already says not exported | the notes: every Owed line's ticket goes to Todo with a comment saying what is owed and who has it; every line of the list has a ticket, so none is opened | `f_8c1d0bca1d1d5fde4c5008` |
| Who has an ARTHOLD line | Claire: the file came from her and she is redoing it | Robert (he wrote the note) or Brian (he packs) | the notes: a changed file sits with whoever the file came from; Robert's note tags Claire as the one redoing the UVs. The surface grades 'who has it' only where the deciding record names the person | `f_8c1d0bca1d1d5fde4c5008`, `D05GU6L0XFH/1759178332.042459`, DES-349 |

No figure forks: no BOTH_FAIR_FIGURE is declared. Dates: every graded date has the same Pacific and UTC day (3 November 17:00 UTC is 09:00 PT).

### Reach table (load-bearing records)

Base records (`persona_view.py can-see julia_lawson …`, run by `plan/reach_table.py`):

| Service | Record | Verdict | Why it is load-bearing |
|---|---|---|---|
| slack | `C08H78VJG80/1756393065.804409` LB | YES | the four scenarios as the vendor described them (R5) |
| slack | `C08H78VJG80/1757695108.506159` LB | YES | what Scenario 1 is for (K15) |
| slack | `C08H78VJG80/1757956024.883249` LB | YES | Scenario 1 chosen; grenade, couch, plush doll 'a good start' (K15, T14) |
| slack | `C08H78VJG80/1758022459.227279` LB | YES | formats (binary fbx), the 8-item set and editable extras (K5, C1) |
| slack | `C08H78VJG80/1758283671.878269` LB | YES | what PlayableX expects, by group (H2 decoy, T16) |
| slack | `C08H78VJG80/1758701898.919999` LB | YES | start 6 October (T8 older version) |
| slack | `C08H78VJG80/1758717576.077489` LB | YES | the first zip, 24 Sep (Delivered lines) |
| slack | `C08H78VJG80/1758717625.209649` LB | YES | win and fail as told to PlayableX (R5) |
| slack | `C08H78VJG80/1758717701.940139` LB | YES | more items later on (the extras) |
| slack | `C08H78VJG80/1758723504.085039` LB | YES | the 'duck asset' (T16) |
| slack | `C08H78VJG80/1758729487.922339` LB | YES | the plushie zip the same day (T16) |
| slack | `C08H78VJG80/1758808234.045839` LB | YES | the 25 Sep complaint about the zombie package (T10) |
| slack | `C08H78VJG80/1758906043.375719` LB | YES | the zombie pack, 26 Sep (T10) |
| slack | `C08H78VJG80/1759140968.965099` LB | YES | the question Robert's zombie picks answer (K10, T10) |
| slack | `C08H78VJG80/1759174925.309129` LB | YES | the pause |
| slack | `C08H78VJG80/1759226395.551469` LB | YES | start 3 November (K13) |
| slack | `C08H78VJG80/1744637266.363689` LB | YES | music starts after the first click (K12) |
| slack | `C08H78VJG80/1742892985.601399` LB | YES | the March FBX rule (T12) |
| slack | `C08H78VJG80/1741963515.221549` LB | YES | Julia's brief for the first playable (role remit) |
| slack | `C08H78VJG80/1742063341.276529` LB | YES | the vendor's thanks for that brief (role remit) |
| slack | `D05SD5QLG94/1758220925.518329` LB | YES | Frederick relays the vendor's formats to Julia, 18 Sep (C1 fairness) |
| slack | `C090N54TG79/1758568735.563539` LB | YES | Brian asks Julia for the reference level (role remit) |
| slack | `C090N54TG79/1758569824.148029` LB | YES | Julia's own idea (T13) |
| slack | `C090N54TG79/1758569885.985319` LB | YES | Robert: remain as is (T13) |
| slack | `D076RBM29JS/1758638497.621679` LB | YES | Robert was fine with Frederick's items for the reference level (T14) |
| slack | `D076RBM29JS/1758638743.317009` LB | YES | Julia builds the grenade, couch, plushie level (T14, deck) |
| slack | `C090N54TG79/1759189466.554739` LB | YES | new coloured cactus, chainsaw and cones, 29 Sep (C3 chain, T3) |
| slack | `C08R8CHB0QL/1758752145.583769` LB | YES | Robert asks for a recoloured cactus plant (T3) |
| slack | `C08R8CHB0QL/1758754866.994649` LB | YES | recoloured cone (T3) |
| slack | `C08R8CHB0QL/1758808937.107229` LB | YES | Claire pushed the changes (T3) |
| slack | `C08R8CHB0QL/1758904025.123869` LB | YES | Julia's bow post, parent of Robert's reply (K11, K14) |
| slack | `C08R8CHB0QL/1756813716.024339` LB | YES | the bounce items thread of 2 Sep (T6) |
| slack | `C09ATAJ220H/1758881579.188609` LB | YES | the nine zombies of the pack (zombie picks) |
| slack | `C09ATAJ220H/1758905604.787929` LB | YES | Marcus's zombie pack, tested in an empty project (T10) |
| slack | `D05GU6L0XFH/1757519060.984519` LB | YES | two sounds to be swapped for copyright (sound sheet's origin) |
| slack | `D05SD5QLG94` LB | YES | the DM the ask and the reply sit in |
| slack | `D05HMBQUC8Z` LB | YES | the DM Claire's message sits in |
| slack | `C0880U9751A` LB | YES | the channel Marcus's post sits in |
| slack | `C08H78VJG80` LB | YES | the PlayableX channel (anchor A2, the links) |
| gdocs | `f_05bedd1540d3e01a90ab16` LB | YES | Leonard's Playable Feedback (H1 decoy, T17) |
| gdrive | `d_8140f09bf9f1b94cb8ee2d` LB | YES | destination of both deliverables |
| github | `harmonygames-Games/match3d#462` LB | YES (unscoped service) | the 25 Sep model change and its comment (C1 unit) |
| github | `harmonygames-Games/match3d#460` LB | YES (unscoped service) | new objects, merged after the first zip (T18) |
| confluence | `page_zm3d_gdd` LB | YES (unscoped service) | tray size and how a level is lost (K6, T9) |
| linear | `ZOM-97` LB | YES (unscoped service) | the object revision tickets (T19) |
| trello | `688c4d14c312a27fa2747e40` LB | YES (unscoped service) | Leonard's card (H3 decoy, T11) |

Planned records are checked at the injection gate (`persona_view.py check-sql`). Their planned access: the ask and Robert's note are in Julia's own DMs; Robert's posts and reply and Marcus's post are in channels she is a member of; the notes, the pack list and Calvin's sheet are shared with her and the deck is hers; the hold has her as an attendee; Linear, Trello and Contacts are unscoped. Records she cannot read are never load-bearing: Brian's DMs with Claire and with the engineer are cited in §1a and §13 as whole-base consistency checks only, and the Slack mirror of the pull request comment in #zombie-prs is not relied on.

### Feasibility, precedence, naturalness, grading devices

- **Feasibility.** Tools in `Evals/references/tools/catalog.json`: `gsheets_create_spreadsheet`, `gsheets_values_update`, `gdocs_create_document`, `gdrive_share_file`, `linear_update_issue`, `linear_create_comment`, `linear_create_issue`, `slack_send_message`. One sheet with one tab. The outside recipient has an authorised path: the notes name the intake address in Contacts and the sharing level (view only).
- **Explicit rules.** Multi-version evidence: Brian's note stands unless something later says otherwise, and a later word from someone who knows the file or the art counts (notes); Robert's latest word on the picks (ask). What 'now' means: how things stand today (notes), the game as it is today (ask). Each write's end state is in the notes. Every cross-reference postdates its target (Robert's reply after Julia's post; Brian's comment after his zip; Marcus's post after Thursday's save; Robert's note after Friday's files; Brian's log entry after Robert's new colours and after the pause).
- **Precedence.** Load-bearing facts sit only in ● carriers (Ask_Carriers §5 as amended by §6b): Slack text, Linear comments, Sheets grids, Docs body, Slides element text, calendar summary and attendees, Contacts email, base PR comment text. Nothing load-bearing is in a calendar description, slide notes, a Drive `content_text` or a Slack file.
- **Prompt naturalness.** The human's trigger needs: Frederick's message as the starting point, that the job is all of it, that both files go in her Drive, the PlayableX channel. It must not carry: the three state words, any rule, any category or item name, any count, any ticket key, the places of §5, or where the notes and the list live. The surface's spans are the three anchor names only.
- **Grading devices.** Exact key set of the list (96); three totals; at most five samples per group (state, a second line of each hidden set, two controls, what is owed, who has it, board set, ticket comments) with a volume row; one tracked ticket. Brief rows are 29 of 192 surface weight. No graded count, format or limit that the ask or the notes do not state.

### Coherence rail

Every §1a row is dispositioned. Designed disagreements are dated human claims with a named later record: Brian's notes (25 and 26 Sep) against Marcus's post (26 Sep), Robert's note (29 Sep) and his own log (30 Sep); Robert's new colour versions (29 Sep) against the re-send in that log (30 Sep); Robert's eight (25 Sep) against his reply (26 Sep). No two system fields disagree: undelivered tickets are In Progress until the run moves the Owed ones, which is the task, and a ticket's state never contradicts its own note. Companions planned with each record are in §11. No seeded text names a git branch, a build number or a release; the one base artifact the plan relies on is match3d#462 (title, created and merged times, the models its comment names), cited as base states it. Ids follow the base schemes (§2, §11).


## 11 Record plan for /create-injection

| Key | Service | Id | At (UTC) | By | What |
|---|---|---|---|---|---|
| ask | slack | `D05SD5QLG94/1759256494.852159` | 2025-09-30T18:21:34Z | Frederick Stone | Frederick's DM to Julia: the job, its destinations, and the three things it starts from |
| notes | gdocs | `f_8c1d0bca1d1d5fde4c5008` | 2025-09-30T16:58:00Z | Frederick Stone | Frederick's hand-off notes (created 2025-09-30 16:25, before his 17:30 investor call): what the brief covers, the list's columns, the three states, tickets, sharing |
| tracker | gsheets | `f_956e60ec7f2f7977d98934` | 2025-09-26T17:25:00Z | Brian Foster | Brian's pack list (created 2025-09-25): one row per line: Line, Kind, Category, Went out, Ticket; no state column |
| picks | slack | `C090N54TG79/1758823946.262829` | 2025-09-25T18:12:26Z | Robert | Robert's eight for the board, the vendor's '8-item set': the reference level's three plus five (root post in #zombie-design) |
| zpicks | slack | `C090N54TG79/1759167068.371289` | 2025-09-29T17:31:08Z | Robert | Robert's answer to the vendor's 29 Sep question: walk as the one animation; Party Girl, Plumber, Magician, Football Player |
| ticket_parent | linear | `DES-313` | 2025-09-25T07:05:00Z | Brian Foster | Brian's pack ticket in the Design team; children DES-314 to DES-409, one per line of the pack list |
| tickets | linear | `DES-314` … `DES-409` | 2025-09-25 07:06 to 07:20 (created); notes 2025-09-25 to 2025-09-29 | Brian Foster (creator, assignee, one note each) | one ticket per listed line, title = the line's name, parent DES-313, team DES; state Done for the eight delivered lines, In Progress for the rest; one comment by Brian on each saying what he did with the line |
| deck | gslides | `f_6a2fa8e61b31139ca8e3d4` | 2025-09-23T19:55:00Z | Julia Lawson | Julia's deck of the reference level as built on 23 Sep: grenade, couch, plushies; mixed zombies; win and fail |
| hold | gcal | `evt_421695d009e589ee85296c` | 2025-09-30T16:41:00Z | Frederick Stone | kickoff hold Mon 3 Nov 2025 17:00 UTC; attendees Frederick, Julia, Brian, Robert (one row per calendar) |
| contact | contacts | `d7d31caf63ee33db2b7ed271` | 2025-09-19T16:40:00Z | Frederick Stone | PlayableX intake contact (outside partner): the address a view link is shared with |
| trello_note | trello | `68dc381b75aff34acf5a5424` | 2025-09-30T20:05:47Z | Leonard Hayes | Leonard's comment on his Playable Kickoff card: parked until 3 November, Julia is pulling the brief and the pack status together for Frederick |
| a1_post | slack | `C0880U9751A/1758906517.912099` | 2025-09-26T17:08:37Z | Marcus Bennett | A1: root post in #zombie-match3d: the models Brian saved out of Unity on Thursday are the text kind (the setting was wrong that day); Claire's are fine |
| a2_dm | slack | `D05GU6L0XFH/1759178332.042459` | 2025-09-29T20:38:52Z | Robert | A2: Robert to Julia in their DM (English, between his messages of 29 Sep): Claire is redoing the UVs of the bathroom objects; the bathroom files she gave Brian on Friday are the old ones |
| c3_reply | slack | `C08R8CHB0QL/1758922879.243189` | 2025-09-26T21:41:19Z | Robert | C3: Robert's reply under Julia's bow post: the bow goes in the eight in place of the last item on his list (the dynamite), as it is; the reply names no item |
| c4_log | gdocs | `f_faf4d7c167d14a1127dcc3` | 2025-09-30T09:12:26Z | Brian Foster | C4: Brian's own log of what he put in the outgoing folder (a Google Doc, created 25 Sep): on Tue 30 Sep Claire re-sent the three recoloured items, which open and look right; the zip with Friday's music instruments was cut off on upload and will not unpack, and the eight are not in the folder any other way |
| c2_sheet | gsheets | `f_b2387e31d46d3a7b3fa2a9` | 2025-09-26T20:10:00Z | Calvin Price | C2: Calvin's sound sources sheet (created 2025-09-12): where each cue came from, whether it is ours to pass on, who makes our own version |

Planned wording: `plan/planned_texts.py` (the ask, the notes, the pack ticket's description, Robert's three messages, Marcus's post, Robert's note on the bathroom objects (D3), Brian's log of the outgoing folder, Calvin's grid, the deck's slides, the hold, the contact, Leonard's comment). Brian's note per class (`plan/design_model.py` NOTE, VIS_NOTE): Delivered — 'In the first zip, 24 Sep.'; Ready — 'FBX from Claire', the day, 'Opens, looks right. In the outgoing folder.'; EXPORT — 'FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.' (no tool is named on a ticket); Bathroom — the Ready wording, Fri 26 Sep; instruments — the Ready wording plus 'Zipped with the other instruments'; REVISED — 'FBX from Claire, Thu 25 Sep, first thing', stamped 08:05 UTC, superseded by the log's re-send; sound — 'Exported .wav from the project, Fri 26 Sep. Plays.'; Owed on its own note — 'Not exported yet' or 'Not sent', with who has it. Haystack: routine traffic around each deciding record is base (#zombie-match3d 64 messages in the week, Julia's DM with Robert 712 in September, #zombie-art, DES-313's neighbours); `path_exposure.py` at injection decides whether more is needed. Seeded Slack text names nobody by plain first name: base text carries a mention or a masking token where a person is meant, so a plain 'Brian' or 'Claire' would be a unique search key (re-check, row F3); mentions are used instead and names are added to the SQL wording sweep. Size about 330 rows over ten schemas (slack, linear, gsheets, gdocs, gdrive, gslides, gcal, gmail, trello, contacts); Snowflake, Confluence and GitHub are not injected.

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| slack | INT-13 (Drive app DMs), INT-04 (Linear app posts) | share and ticket notifications | none seeded: the Linear app's team-channel posts are for ZOM and ENG tickets (INT-04), and Design-team tickets created outside Slack carry no bot post, and the shares are covered by mail (INT-11 below); the thread counters of Julia's bow post `C08R8CHB0QL/1758904025.123869` are updated with the reply |
| linear | INT-04, INT-05 | Slack posts, e-mail digests | none: digests are not per ticket; `updated_at` follows the newest note (generator convention) |
| gcal | INT-11 | invitation mails | seeded: one event row per attendee calendar (same `ical_uid`) and one invitation mail per attendee mailbox |
| gmail | INT-11, INT-22 | the invitation mails themselves | seeded as companions only; no deciding fact in mail (Gmail is THIN for the persona) |
| gdrive, gdocs, gsheets, gslides | INT-13 | Drive rows mirror Docs, Sheets and Slides ids and sharing | seeded: one `drive_files` row per file with identical sharing; Julia owns the deck |
| trello | INT-21 | none exists | trello: none — the card's and the board's dateLastActivity move with the comment and the card's badge counts one comment |
| contacts | — | none | contacts: none — a single row in the base shape (15 fields) |
| github | INT-01, INT-03 | Slack mirror, linear[bot] | github: none — nothing is seeded in GitHub; match3d#462's comment already has its base mirror in #zombie-prs |

## 12 Self-test results

`hardness_gate.py … --design` (verbatim):

```
HARDNESS GATE (extreme (design)): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: skipped (--design: no SQL yet)
  [ok] base_consistency: skipped (--design: no SQL yet)
  [ok] services_injected: skipped (--design: no SQL yet)
  [ok] rows: skipped (--design: no SQL yet)
  [ok] services_carrying_weight: 12 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: skipped (--design: no SQL yet)
  [ok] seeded_ids_exist_in_sql: skipped (--design: no SQL yet)
  [ok] anchors: 3 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 15 fragments; need ≥ 12
  [ok] ask_fragment_services: 8 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 14 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 7 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 96; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 2 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 195; need ≥ 110
  [ok] call_budget: unconditional (verified) floor 252 of 252 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 220 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 34% (≤ 50%)
  [ok] traps: 19 traps across 10 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 7 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (2 with versions in ≥ 2 services, 2 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 6 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 11 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 6 chains with 6 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 6 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 6 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 7 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 6 writes over 5 services; each must depend on findings
  [note] volume_exception: call-budget floor 220 and per-record floor 110 replace 500 and 300; every other extreme target applies — reason: the cohort is the 96 lines of one playable pack; honest necessary calls are abou; requester confirmation: task author in chat on 2026-11-11: '220 calls are good with required failure'; a
```

`gradable_surface.py validate` and `gradeable-report` (verbatim):

```
GRADABLE SURFACE (01_Gradable_Surface.json): PASS · 52 slots · weight 192 · mechanism share 76.6% (reported, not gated) · weight by class {'direct': 102, 'write_content': 70, 'delivery': 11, 'aggregate': 9}
SURFACE.GRADEABLE PASS · 52 slot(s) · {'GRADABLE': 52}
```

Id collision check (`plan/check_ids.py`, `hg.py search lookup`; verbatim):

```
linear issues    ids  97 hits 0 scan_complete=True 
linear comments  ids  96 hits 0 scan_complete=True 
drive files      ids   5 hits 0 scan_complete=True 
gcal events      ids   1 hits 0 scan_complete=True 
trello actions   ids   1 hits 0 scan_complete=True 
contacts         ids   1 hits 0 scan_complete=True 
slack message ids ids   6 hits 0 scan_complete=True 
minted slack: {'D05SD5QLG94/1759256494.852159': '7e84f1cf59f8e95fef961268fbf37cc1', 'C090N54TG79/1758823946.262829': 'da6776f77288224ec67847a799bbde5a', 'C090N54TG79/1759167068.371289': '0b7f656a96c5cc50d1f6924e089bf8ba', 'C0880U9751A/1758906517.912099': 'a5ee6e90923eeab380e6730f674240d2', 'D05GU6L0XFH/1759178332.042459': '8a1b1c6d448eecb7ccc81f796c95d5ce', 'C08R8CHB0QL/1758922879.243189': '1d55b38831d7517fe403e4f2a906a897'}
```

**Lazy-solver pass.** An agent that makes one broad search per service, reads first hits, opens no thread, stops at the first conclusion and uses every bulk call: it finds the ask, the notes, the pack list and the PlayableX channel's last page; lists the 96 children with their states in two calls; reads no comments. It scores the delivery rows and the brief rows that come from the hub (scenario, start date), about 8 % of the surface weight; it cannot fill the state column, because no bulk call returns a ticket's notes. Leaks looked for and closed: the pack list has no state or note column; ticket state marks only the eight delivered lines, which the list's 'Went out' column already shows; ticket titles and descriptions carry the line's name only; no label marks a class; no category is of one class; the notes name no deciding record. Still open by design and named for the pre-check: `linear_show_data`.

**Literal-value sweep and wording sweep** (base, `plan/literal_sweep.py` through `tools/hg.py search-many` over eleven services; the SQL repeats both):

```
    linear music_instruments: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json /issues/3678/description | 'Goods\n 2. Bathroom\n 3. Bedroom\n 4. Beverages\n 5. Breakfast\n 6. Dining Room\n 7. Fast Food\n 8. Fresh Produce\n 9. Garden\n10. Kitchen\n11. Living'
    linear kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json /issues/1886/title | 'Kickoff API v1 implementation'
    linear kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json /issues/3645/description | 'ew of a 5-lane highway leading to a different city with each event milestone. \n3. See the spec for details (in progress by [PERSON_NAME_0019'
linear: scan_complete=None text_kind=0 got_out_of_unity=0 setting_wrong=0 redoing_the_uvs=0 bathroom_objects=0 recoloured_models=0 wav_exports=0 replace_thursdays=0 wont_unpack=0 music_instruments=1 in_place_of_the_last=0 go_boom=0 pack_list=0 handoff_notes=0 sound_sources=0 ok_outside_the_game=0 outgoing_folder=0 intake=0 playable_pack=0 eight_item=0 kickoff=2
    gdocs kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gdocs/data.json /docs_documents/264/body_text | 'll icons will have VFXs that can be grown into other icons as well. So they should be generic. To be discussed with the art team to figure o'
    gdocs kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gdocs/data.json /docs_documents/321/body_text | ' activated | - Retention and economy KPIs - Token sinks tested - Crafting + token yield loop validated and in Alpha |\n| Production | 7 | M7 '
gdocs: scan_complete=None text_kind=0 got_out_of_unity=0 setting_wrong=0 redoing_the_uvs=0 bathroom_objects=0 recoloured_models=0 wav_exports=0 replace_thursdays=0 wont_unpack=0 music_instruments=0 in_place_of_the_last=0 go_boom=0 pack_list=0 handoff_notes=0 sound_sources=0 ok_outside_the_game=0 outgoing_folder=0 intake=0 playable_pack=0 eight_item=0 kickoff=3
    gsheets music_instruments: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gsheets/data.json /sheets_spreadsheets/118/sheets/9/grid/13/4 | 'Music Instruments'
    gsheets music_instruments: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gsheets/data.json /sheets_spreadsheets/118/sheets/9/grid/13/38 | 'Music Instruments'
    gsheets kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gsheets/data.json /sheets_spreadsheets/24/sheets/0/grid/9/2 | 'M7 - Phase 2 Kickoff Prep'
    gsheets kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gsheets/data.json /sheets_spreadsheets/139/sheets/1/grid/3/1 | 'Medium Blog Kickoff'
gsheets: scan_complete=None text_kind=0 got_out_of_unity=0 setting_wrong=0 redoing_the_uvs=0 bathroom_objects=0 recoloured_models=0 wav_exports=0 replace_thursdays=0 wont_unpack=0 music_instruments=5? in_place_of_the_last=0 go_boom=0 pack_list=0 handoff_notes=0 sound_sources=0 ok_outside_the_game=0 outgoing_folder=0 intake=0 playable_pack=0 eight_item=0 kickoff=5?
    gslides kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gslides/data.json /slides_presentations/26/pages/33/elements/0/text | 'TEAM RAMP-UP & PRODUCTION PLAN\nM1 ? Pre-Production Kickoff (~11 FTEs)\n\nFocus: Core loop R&D, token economy, backend scaffolding, art directi'
    gslides kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gslides/data.json /slides_presentations/29/pages/7/elements/0/text | '1\n\nQ2\n\nQ3\n\nLIVEOPS ENGINE: DOMINO DELIGHTS\n\nDOMINO DELIGHTS LIMITED BETA\n\nMATCH 3D\n\nGLOBAL LAUNCH: DOMINO DELIGHTS\n\nMATCH 3D BETA\n\nDOMINOES '
gslides: scan_complete=None text_kind=0 got_out_of_unity=0 setting_wrong=0 redoing_the_uvs=0 bathroom_objects=0 recoloured_models=0 wav_exports=0 replace_thursdays=0 wont_unpack=0 music_instruments=0 in_place_of_the_last=0 go_boom=0 pack_list=0 handoff_notes=0 sound_sources=0 ok_outside_the_game=0 outgoing_folder=0 intake=0 playable_pack=0 eight_item=0 kickoff=4
confluence: scan_complete=None text_kind=0 got_out_of_unity=0 setting_wrong=0 redoing_the_uvs=0 bathroom_objects=0 recoloured_models=0 wav_exports=0 replace_thursdays=0 wont_unpack=0 music_instruments=0 in_place_of_the_last=0 go_boom=0 pack_list=0 handoff_notes=0 sound_sources=0 ok_outside_the_game=0 outgoing_folder=0 intake=0 playable_pack=0 eight_item=0 kickoff=0
    trello kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json /cards/765/name | 'Playable Kickoff'
    trello kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json /cards/765/url | 'https://PERSON_6092_TRELLO_USERNAME.com/c/XIcVS41B/447-playable-kickoff'
trello: scan_complete=None text_kind=0 got_out_of_unity=0 setting_wrong=0 redoing_the_uvs=0 bathroom_objects=0 recoloured_models=0 wav_exports=0 replace_thursdays=0 wont_unpack=0 music_instruments=0 in_place_of_the_last=0 go_boom=0 pack_list=0 handoff_notes=0 sound_sources=0 ok_outside_the_game=0 outgoing_folder=0 intake=0 playable_pack=0 eight_item=0 kickoff=5?
    github music_instruments: Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json /pull_request_comments/413/body | '!**/*.asset`\n* `Assets/Data/Objects/Living Room/Record Player/Record Player Medium Yellow2.asset` is excluded by `!**/*.asset`\n* `Assets/Dat'
    github music_instruments: Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json /pull_request_comments/461/body | '*.asset`\n* `Assets/Data/Objects/Bathroom/Wash Basin Cabinet/Wash Basin Cabinet Large Pink2.asset` is excluded by `!**/*.asset`\n* `Assets/Dat'
    github pack_list: Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json /pull_requests/1339/body | 'er to load the puzzle packs json files since those are smaller compared to the binary packs. Eventually it would be better to only require t'
github: scan_complete=None text_kind=0 got_out_of_unity=0 setting_wrong=0 redoing_the_uvs=0 bathroom_objects=0 recoloured_models=0 wav_exports=0 replace_thursdays=0 wont_unpack=0 music_instruments=5? in_place_of_the_last=0 go_boom=0 pack_list=1 handoff_notes=0 sound_sources=0 ok_outside_the_game=0 outgoing_folder=0 intake=0 playable_pack=0 eight_item=0 kickoff=0
    gcal kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gcal/data.json /events/2/summary | 'Castle Climb Art Kickoff'
    gcal kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gcal/data.json /events/123/summary | 'Streak Fever Art Kickoff'
gcal: scan_complete=None text_kind=0 got_out_of_unity=0 setting_wrong=0 redoing_the_uvs=0 bathroom_objects=0 recoloured_models=0 wav_exports=0 replace_thursdays=0 wont_unpack=0 music_instruments=0 in_place_of_the_last=0 go_boom=0 pack_list=0 handoff_notes=0 sound_sources=0 ok_outside_the_game=0 outgoing_folder=0 intake=0 playable_pack=0 eight_item=0 kickoff=5?
contacts: scan_complete=None text_kind=0 got_out_of_unity=0 setting_wrong=0 redoing_the_uvs=0 bathroom_objects=0 recoloured_models=0 wav_exports=0 replace_thursdays=0 wont_unpack=0 music_instruments=0 in_place_of_the_last=0 go_boom=0 pack_list=0 handoff_notes=0 sound_sources=0 ok_outside_the_game=0 outgoing_folder=0 intake=0 playable_pack=0 eight_item=0 kickoff=0
    gmail music_instruments: Universe_SynthCut/SynthCut_HarmonyGames_Gmail/Services_Data/gmail/threads/00014164.json /messages/1/body | 'dModels/Toys/Toy_Xylophone.fbx.meta (109)\n    M Assets/MyAssets/3dModels/SmoothedModels/match3dModels_Texture_01.png (4)\n    A Assets/Prefab'
    gmail music_instruments: Universe_SynthCut/SynthCut_HarmonyGames_Gmail/Services_Data/gmail/threads/00014394.json /messages/0/body | 'asset`\r\n> * `Assets/Data/Objects/Living Room/Record Player/Record Player medium Yellow2.asset` is excluded by `!**/*.asset`\r\n> * `Assets/Dat'
    gmail kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Gmail/Services_Data/gmail/threads/00003518.json /messages/0/subject | 'Invitation: Quest UI/UX Kickoff @ Fri Mar 1, 2024 8:30am - 9am (PST) (robert@harmonygames.co)'
    gmail kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Gmail/Services_Data/gmail/threads/00003518.json /messages/0/body | 'Quest UI/UX Kickoff\r\nFriday Mar 1, 2024 ⋅ 8:30am – 9am\r\nPacific Time - Los Angeles\r\n\r\nJoin with Google Meet\r\nhttps://meet.google.com/fgi-hmo'
gmail: scan_complete=None text_kind=0 got_out_of_unity=0 setting_wrong=0 redoing_the_uvs=0 bathroom_objects=0 recoloured_models=0 wav_exports=0 replace_thursdays=0 wont_unpack=0 music_instruments=5? in_place_of_the_last=0 go_boom=0 pack_list=0 handoff_notes=0 sound_sources=0 ok_outside_the_game=0 outgoing_folder=0 intake=0 playable_pack=0 eight_item=0 kickoff=5?
    slack text_kind: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages/D07G5QWT20K/2025-05.json /3/text | 'and text kinda overlaps icon'
    slack music_instruments: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages/C05H8KVNU67/2025-07.json /0/text | "tion just to keep things easy. (No more day 0, you'll see why in a minute) Each collection will have ~44 cards.\n4. Our first expansion for e"
    slack music_instruments: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages/C08R8CHB0QL/2025-05.json /196/text | 'mbargo some specific categories:\nbeverages, breakfast, fast food, fresh produce, garden, sports, survival, baked good, bedroom.\n\nThen I woul'
    slack pack_list: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages/C050WGU41HR/2024-04.json /583/attachments/0/text | 'er to load the puzzle packs json files since those are smaller compared to the binary packs. Eventually it would be better to only require t'
    slack pack_list: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages/D0770ET1HV2/2024-07.json /225/text | 'ya şeyde silindi muhtemeln pack listesini temizlediler ya'
    slack eight_item: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages/C08H78VJG80/2025-09.json /6/text | 'be able to start the optimization and animation processes in advance.\nFor the items on the board, we can make them editable. This way, aside'
    slack kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/files.json /6017/name | 'UX Kickoff (2024-03-01 08:38 GMT-8)'
    slack kickoff: Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/files.json /6017/title | 'Quest UI/UX Kickoff (2024-03-01 08:38 GMT-8)'
slack: scan_complete=None text_kind=1 got_out_of_unity=0 setting_wrong=0 redoing_the_uvs=0 bathroom_objects=0 recoloured_models=0 wav_exports=0 replace_thursdays=0 wont_unpack=0 music_instruments=5? in_place_of_the_last=0 go_boom=0 pack_list=2 handoff_notes=0 sound_sources=0 ok_outside_the_game=0 outgoing_folder=0 intake=0 playable_pack=0 eight_item=1 kickoff=5?
```

Reading of the sweep: a planned phrase with no base hit cannot contradict base; a hit is listed above with its record and is unrelated to this pack unless stated in §1a. None of the six deciding records is planned with a word of the rule it triggers ('format', 'binary', 'current version', 'changing', 'ours', 'picks') or with one of the swept nouns of §6.

**'The rest stands' check.** Robert's reply changes one item; no later planned record re-lists the eight. The deck (23 Sep) is the reference level and is not edited after his posts.

**S9b prior forecast** (advisory, UNCALIBRATED, pre-registered before any platform run of D3: `hardness_forecast.py forecast --design --manifest Working_Files/01_Hardness_Manifest.draft.json … --preregister`; ledger id `hev_930ca8da536b9595`; output verbatim except that the ledger line's empty 'rejected' list is left out):

```
HARDNESS FORECAST · UNCALIBRATED · advisory · DESIGN (declared attributions) · model claude-opus-5-5 · design · model outputs, not measurements; the Season Pass backtests are development fixtures, not validation
  rule:EXPORT                                  family done_gap                                 Beta(1.75, 3.8571) mean 0.31 n_eff 3.6071 records 20
  rule:ARTHOLD                                 family superseding                              Beta(3.8214, 1.7857) mean 0.68 n_eff 3.6071 records 39
  rule:REVISED                                 family completion_elsewhere                     Beta(1.6429, 3.9643) mean 0.29 n_eff 3.6071 records 20
  rule:AUDIO                                   family authority                                Beta(1.25, 4.3571) mean 0.22 n_eff 3.6071 records 20
  rule:PICKS                                   family superseding                              Beta(3.8214, 1.7857) mean 0.68 n_eff 3.6071 records 39
  rule:ZIP                                     family completion_elsewhere                     Beta(1.6429, 3.9643) mean 0.29 n_eff 3.6071 records 20
  independent whole    V3 E[avg] 0.657 [0.557, 0.759] P(all) 0.396
  independent whole    V3 E[avg] 0.657 [0.557, 0.759] P(all) 0.396
  independent whole    V3 E[avg] 0.657 [0.557, 0.759] P(all) 0.396
  independent whole    V3 E[avg] 0.657 [0.557, 0.759] P(all) 0.396
  independent whole    V3 E[avg] 0.657 [0.557, 0.759] P(all) 0.396
  source      whole    V3 E[avg] 0.658 [0.555, 0.763] P(all) 0.450
  source      whole    V3 E[avg] 0.658 [0.555, 0.763] P(all) 0.450
  source      whole    V3 E[avg] 0.658 [0.555, 0.763] P(all) 0.450
  source      whole    V3 E[avg] 0.658 [0.555, 0.763] P(all) 0.450
  source      whole    V3 E[avg] 0.658 [0.555, 0.763] P(all) 0.450
  correlated  whole    V3 E[avg] 0.670 [0.516, 0.822] P(all) 0.360
  correlated  whole    V3 E[avg] 0.670 [0.516, 0.822] P(all) 0.360
  correlated  whole    V3 E[avg] 0.670 [0.516, 0.822] P(all) 0.360
  correlated  whole    V3 E[avg] 0.670 [0.516, 0.822] P(all) 0.360
  correlated  whole    V3 E[avg] 0.670 [0.516, 0.822] P(all) 0.360
  V3: P(all four difficulty gates) 0.360-0.450 across scenarios; value of information (first scenario): ['rule:AUDIO', 'rule:EXPORT', 'rule:ZIP']
  slots most at risk (independent whole; P(fail) / P(fails all six) - all-fail justification workload, never a block): A1 0.92/0.63, A2 0.92/0.63, W1 0.92/0.63, W2 0.92/0.63, X2 0.68/0.21, X2b 0.68/0.21, X7 0.68/0.21, X11 0.68/0.21
  ledger: forecast record {'id': 'hev_930ca8da536b9595', 'added': True, 'present': False}
```

A first run of the same command without `--manifest` (ledger id `hev_3e0dcc1b55a608ac`) read the rev1 final manifest, which the tool prefers when it exists, and so used REVISED's rev1 family; it is superseded by the record above and is not cited anywhere else. D2's forecast was `hev_1072a8a9540b0640` (kept in `run_forensics/rev1/artifacts/forecast_design_D2.txt`). The priors are per-family miss rates for `claude-opus-5-5` and now include the seven rev1 runs (`plan/out/ledger_priors.txt`); the task-specific simulation of §6 uses the measured habits instead. Both are uncalibrated.

### Self-review

Gate output re-read after the last change: `HARDNESS GATE (extreme (design)): PASS` (pasted above with its ok lines and the volume-exception note). Re-read as the eval: `Evals/1_Prompt_Eval.md` §2.1 (Unique Ground Truth), §2.2 (Feasibility), §3.2 (Cross-Service Coherence) and `Evals/0_Injection_Quality_Eval.md` Check C, walked against §1a, §7 and §10. Load-bearing base values were re-read through `tools/hg.py` in this session: the PlayableX channel from 15 Sep, Julia's DM with Brian of 23 Sep, Brian's two DMs of 24 Sep, the pull requests #459 to #471 (titles, times), the open ZOM tickets that name objects, the ZOM number range and team memberships; the rest is the reviewers' fact pack with record ids.

| Item | Counter-reading (the best case that it fails) | Resolution (evidence) | Verdict |
|---|---|---|---|
| temporal | The ask is dated after the pause and asks for prep the pause was meant to stop. | the base lines of 29 Sep are about vendor development on a game that may change (`C090N54TG79/1759114097.776589`, `C08H78VJG80/1759174925.309129`); the ask scopes to the game as it is today and to what PlayableX hold and are owed (`D05SD5QLG94/1759256494.852159`) | holds |
| semantic | 'Owed' could mean owed by the vendor, or money; 'who has it' could mean who holds the file. | the notes define the three states and 'who has it, meaning whoever has to do the next thing' (`f_8c1d0bca1d1d5fde4c5008`); learnings §80: each label defined in a record | holds |
| cross-service referential | The pack list and the tickets can disagree on a line's name or ticket. | both are generated from one model (`plan/design_model.py`: the pack list `f_956e60ec7f2f7977d98934`, tickets DES-314 to DES-409); the injection gate's `fact_check` holds them to it | holds, enforced at injection |
| quantitative | 8 / 39 / 49 could fork on a line whose note is unclear. | every listed line's note says where the file came from and that it opens, or that it is not exported (`plan/design_model.py` NOTE, VIS_NOTE); the two-reading table covers the bow, the zombies and the first zip (`C08H78VJG80/1758723504.085039`) | holds |
| state/lifecycle | In Progress tickets whose files are 'in the outgoing folder' could be read as a State/Lifecycle inconsistency. | the pack ticket DES-313 says a line's ticket closes when PlayableX have the file, so In Progress is right for every undelivered line, exported or not; card SC-16's tickets are not touched | holds |
| identifier/format | DES-313 to DES-409 could collide or break the series. | base highest in the Design team is `DES-312` (7 May 2025) and the range is free (`plan/check_ids.py`: 0 hits, scan complete), so the keys follow in number and in date | holds |
| other | A reviewer reads the cohort as padding: 96 lines for one ad. | the vendor asked for an 8-item set plus extra items it makes editable (`C08H78VJG80/1758022459.227279`), its list names sound, 2D and fonts (`C08H78VJG80/1758283671.878269`), and Brian promised more items later (`C08H78VJG80/1758717701.940139`); every line is a cell of the list the ask requests | holds |
| decision: How many lines | the alternative: more, with the vendor's asks or the reference level's variants added | the notes: one row per line of Brian's pack list; the ask has no clause about the vendor's requests (`f_8c1d0bca1d1d5fde4c5008`, `f_956e60ec7f2f7977d98934`) | best reading stands |
| decision: Twelve lines saved out of the project | the alternative: Ready: FBX, opens, looks right, in the outgoing folder; or Owed on suspicion, without the post | Marcus: those files are the text kind; the vendor takes binary only; the notes: a format they take, and a later word from someone who knows the file counts. Without the post the note passes every Ready test on its face and 'take it as it stands' applies, so suspicion alone is not a fair Owed (`C0880U9751A/1758906517.912099`, `C08H78VJG80/1758022459.227279`) | best reading stands |
| decision: Twelve exported bathroom lines | the alternative: Ready: Friday's files open and look right; or Owed with Robert or Brian | Robert says later that Claire is redoing the UVs and Friday's files are the old version; the notes leave a changed file with whoever it came from, and the twelve notes say 'FBX from Claire' (`D05GU6L0XFH/1759178332.042459`) | best reading stands |
| decision: Cactus Plant, Chainsaw, Cone | the alternative: Owed, the file again (Claire): Robert's new colour versions came after their 25 Sep files | Brian's log of 30 Sep, the latest record: Claire sent the three recoloured models again, they open, look right and replace Thursday's (Robert's post says which three). A reader who takes colour versions as additions also arrives at Ready (`f_faf4d7c167d14a1127dcc3`, `C090N54TG79/1759189466.554739`, `f_8c1d0bca1d1d5fde4c5008`) | best reading stands |
| decision: Kettlebell, Dart Board, Candy; the shared atlases | the alternative: lines to add or delivered files to send again | they are not on Brian's list and Robert did not add them; #460 adds objects and names no line's art (`harmonygames-Games/match3d#462`, `harmonygames-Games/match3d#460`) | best reading stands |
| decision: Eight instruments in Friday's zip | the alternative: Ready: each file opens and looks right, and Brian still has it | the notes: Ready is 'sitting in the outgoing folder, it opens'; Brian's log: that zip will not unpack and the eight are not in the folder any other way (`f_faf4d7c167d14a1127dcc3`) | best reading stands |
| decision: Rocket sound and Explosion sound | the alternative: Ready: .wav is a type the vendor takes and it plays | the notes hand over only what is ours; Calvin's sheet marks both 'no' and names him for our own version (`f_b2387e31d46d3a7b3fa2a9`) | best reading stands |
| decision: The eight on the board | the alternative: with the dynamite (25 Sep); or the reference level's three; or the bow in place of some other item | Robert's own later reply: 'it' is the bow of the post he answers, 'the last one on my list' is the dynamite, the last item of his 25 Sep post; the ask keeps his latest word (`C08R8CHB0QL/1758922879.243189`, `C090N54TG79/1758823946.262829`) | best reading stands |
| decision: The bow's own state | the alternative: Owed: Claire agreed to add an arrow | Robert's reply: the bow as it is now, the arrow as its own item later; and the bow's file is of Mon 29 Sep, after Friday's thread (`C08R8CHB0QL/1758922879.243189`, `C08R8CHB0QL/1758904103.894649`, DES-335) | best reading stands |
| decision: The zombie characters | the alternative: Owed: the vendor said the package was not exported correctly; or the project's shaders changed | base: Marcus's tested pack went on 26 Sep and the vendor reviewed it on 29 Sep and asked for a choice, not files; the pack's files did not change (`C08H78VJG80/1758906043.375719`, `C08H78VJG80/1759140968.965099`) | best reading stands |
| decision: What the first zip held | the alternative: everything on the vendor's list, since 'the only missing piece' was the duck | the pack ticket says what the first zip was and the sound, 2D and font tickets say in words that they did not go; the vendor's sentence is about the reference (DES-313, `C08H78VJG80/1758723504.085039`) | best reading stands |
| decision: The cannon and the zombies after match3d#469 | the alternative: to send again: #469 (30 Sep) touches the import settings of the cannon's and the monsters' source files | its own comment: default importer fields added, no existing field changed; the delivered files are not art that changed (`C08H78VJG80/1758906043.375719`, `harmonygames-Games/match3d#469`) | best reading stands |
| decision: Music Keyboard, Grenade and the open rendering ticket | the alternative: somebody is changing them: ZOM-449 (Backlog since July) names them among items with artifacts on low-end devices | that ticket is about rendering on low-end Android, assigned to engineering, untouched since July; nobody is changing the models (`ZOM-449`, DES-387) | best reading stands |
| decision: Tray size | the alternative: six (Julia's July proposal) | base: Robert's reply keeps the page at seven (`page_zm3d_gdd`, `confluence:comment_zm3d_gdd_c2`) | best reading stands |
| decision: Start date | the alternative: 6 October | base: the vendor's latest message (`C08H78VJG80/1759226395.551469`) | best reading stands |
| decision: Who the files are shared with | the alternative: the brief only; or Leonard (his card is the 'kickoff') | the notes: 'Sharing: both files, view only', the kickoff hold and Contacts (`evt_421695d009e589ee85296c`, `d7d31caf63ee33db2b7ed271`) | best reading stands |
| decision: Where the counts go | the alternative: the PlayableX channel | the ask: 'give me the count for each state here'; both forms in the DM are accepted (`D05SD5QLG94/1759256494.852159`) | best reading stands |
| decision: Ticket follow-through on an Owed line | the alternative: a description edit, or a new ticket; or nothing for a line whose note already says not exported | the notes: every Owed line's ticket goes to Todo with a comment saying what is owed and who has it; every line of the list has a ticket, so none is opened (`f_8c1d0bca1d1d5fde4c5008`) | best reading stands |
| decision: Who has an ARTHOLD line | the alternative: Robert (he wrote the note) or Brian (he packs) | the notes: a changed file sits with whoever the file came from; Robert's note tags Claire as the one redoing the UVs. The surface grades 'who has it' only where the deciding record names the person (`f_8c1d0bca1d1d5fde4c5008`, `D05GU6L0XFH/1759178332.042459`, DES-349) | best reading stands |

Required items addressed: the two v2 decisions and their sources (§5); corrections off the first-read path (§5, v2 check); reach (§10); feasibility (§10, §7); volume and the every-run floor (§9); budget and spread (§6); known-data-issue cards (§1a); padding (§2); both cold reviews (§13).

Unresolved: none that blocks the design. Carried to `/create-injection` as checks, not open questions: the SQL wording sweep; the haystack decision; the cold-solver rehearsal; `persona_view.py check-sql` on every planned record; the final wording of Robert's note against his base register in the DM (English, lower case, people tagged). UNVERIFIED-OK items that no row depends on: the binary contents of the three base zips, the five masked zombie names, and whether `github_get_pull_request_files` returns files at run time (the comment route is the one relied on).

```
STAGE GATE scenario: PASS — Task_Authoring/task_inputs · 01_Scenario_Design.md#75b70f53c84a · 01_Hardness_Manifest.draft.json#eeb7fafe905a · 01_Gradable_Surface.json#bfc0af31ecfd · 00_Assigments.md#82494197a841 · __context__#3246c54345b9 · __assignment__#70579cebc8fc · __policy__#dc4ab5df3cdd · __gate_policy__#cc8d944b3feb · __review__#6ba4eb7ccff8 · blocking 0 · warnings 2 · checks 41
[PASS] assignment.v3_context: Julia Lawson / Product Manager; hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 3 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 5/5 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 15/15 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 18/18 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 52/54 items carry a source pointer (min 90%); unsourced e.g. L436: "16 | D3: Claire's UV note as a comment on the bathroom tickets | ticket comment → Owed | r"
[PASS] evidence.record_plan: 23/24 items carry a source pointer (min 80%); unsourced e.g. L790: 'contacts | — | none | contacts: none — a single row in the base shape (15 fields)'
[PASS] evidence.active_speakers: 9/9 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for julia.lawson@harmonygames.co and matches the re-run (147 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 16 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 9 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (8 INT ids, services ['confluence', 'contacts', 'gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts ['LIN-L30', 'LIN-S01']; trap_catalog ['C01', 'C02', 'D05', 'K02', 'N01', 'P01']
[PASS] boundary.anchor_naming: 6 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: dual red team present (01b_Redteam_Review.md + .second.md)
[PASS] surface.valid: 52 slots, weight 192; geometry report-only, never gated: mechanism share 77%, always-pass share 23%
[PASS] forecast.preregistered: prior forecast pre-registered in the ledger: ['hev_1072a8a9540b0640', 'hev_3e0dcc1b55a608ac'] (UNCALIBRATED, advisory)
[PASS] revise.intake: revision intake consumes Working_Files/run_forensics/rev1/node_verdicts.json
[PASS] revise.verdict_dispositions: 6 proposed node verdict(s) dispositioned; 0 CONFOUNDED candidate(s) addressed
[PASS] revise.revision_binding: every export is bound on evidence to the revision it ran on, or marked historical (historical evidence never certifies a revision)
[PASS] evidence.register_run_step: 6/6 items carry a source pointer (min 100%)
[PASS] reach.scenario: 41 scoped load-bearing ids YES for julia_lawson
[PASS] review.counter_readings: 26 evidenced counter-readings (of 26 found; need ≥ 26) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.draft.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] readiness.hardness_review: current evidenced review; deferred: [{'mechanism': 'EXPORT', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'EXPORT', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'ARTHOLD', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'ARTHOLD', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'REVISED', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'REVISED', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'AUDIO', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'AUDIO', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'PICKS', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'PICKS', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'ZIP', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'ZIP', 'evidence': 'natural retrieval', 'required_at': 'injection'}]
[WARN] task.folder: the task folder is the bare default `task_inputs`: give each task its own folder (`Task_Authoring/task_inputs<Label>`) and pass it to every command, so two tasks never share one [first-pass check in warn mode: reported, not blocking]
[PASS] fit.census: fit census: NO NATURAL COHORT; limits: Gmail is thin: no anchor or variance unit there (9 threads dated in the 90 days  — the scenario is built by injection (playbook 01_Scenario_Design, injection-built scenario)
[WARN] budget.design: FAIL: budget.anchors: find rate above 0.20: A1 (up to 0.40), A2 (up to 0.45) (a record found that often is a variance unit).; budget.variance: 0 independent coin-flip habit(s) with a find-rate range inside 0.35-0.65, needs 4 (3 variance units over 3 habits; outside the range: C1 (0.; budget.average: P(six-run average strictly under 70.0%) is 1.000 with every unit at its low find rate and 0.764 at its high find rate (needs 0.90 at both).  (+3 more) — python3 Task_Authoring/tools/difficulty_budget.py check --task-dir <task_dir> [first-pass check in warn mode: reported, not blocking]
[PASS] handoff.pasted: pasted into the Self-review by --paste
```


## 13 Red-team findings

RED TEAM UNAVAILABLE: `redteam_review: set REDTEAM_MODEL or pass --model` (no `REDTEAM_*` variable is set in this environment; the tool was run once on 2026-11-11 and wrote no review).

RED TEAM FALLBACK: two cold reviewer subagents with fresh context and no sight of the author's reasoning reviewed design D1 on 2026-11-11, reviewer 1 against the base universe through tools/hg.py and reviewer 2 for forks, fairness, shortcuts and grader semantics, because the dual red-team tool cannot run without REDTEAM_* credentials.

Their reports are `Working_Files/01b_Redteam_Review.md` (17 findings: 1 blocker, 6 major) and `Working_Files/01b_Redteam_Review.second.md` (22 findings: 1 blocker, 10 major). Both are about D1. Design D2, this document, is the rebuild that answers them; I re-read the base records behind the blocker and the majors myself before changing anything (the vendor channel from 15 Sep, Julia's DM with Brian, Brian's DMs of 24 Sep, the pull requests around the first zip). The same reviewers then supplied the base fact pack (`research/base_facts_D2.md`, `research/object_categories.csv`) and the selector guide (`research/selector_guide_D2.md`) that D2 is built on.

### Reviewer 1: are the planned records consistent with the base?

| # | Severity | Finding (D1) | Disposition in D2 (evidence) |
|---|---|---|---|
| 1 | BLOCKER | The board-object story contradicted base: the reference level was grenade, couch, plushie; the first zip carried only those | Rebuilt. Delivered lines are what base shows went out (`D07G5QWN3TM/1758712833.442809`, `C08H78VJG80/1758717576.077489`, `C08H78VJG80/1758729487.922339`). Robert's eight are dated 25 Sep, after the zip, as the vendor's '8-item set' (`C08H78VJG80/1758022459.227279`). Julia's deck shows the three item types as built (`D076RBM29JS/1758638743.317009`). The other items are later exports. Counts recomputed: 8 / 36 / 58 |
| 2 | MAJOR | The four zombie lines did not match the nine-zombie pack | One line, 'Zombie characters', Delivered on the 26 Sep pack (`C09ATAJ220H/1758905604.787929`, `C08H78VJG80/1758906043.375719`). Robert's planned answer picks four of the names base shows unmasked (`C09ATAJ220H/1758881579.188609`) |
| 3 | MAJOR | Claire's ticket notes predated the day Brian first asked her | Claire writes no ticket note in D2. The pack ticket and the list are created 25 Sep; Brian's notes run 25 to 29 Sep; Claire's message (29 Sep) is after the export it concerns (`D076Y0SDV18/1758712787.694299` is the base start) |
| 4 | MAJOR | No 'object browser' or export tool exists in base; Arthur never posts at that hour | Dropped. EXPORT now rests on the vendor's own rule (binary .fbx, not ASCII: `C08H78VJG80/1758022459.227279`, `C08H78VJG80/1758283671.878269`) and a post by Marcus, who built and tested the zombie pack that day and posts about export settings in that channel (`C0880U9751A/1738678859.796159`), at 17:08 UTC on Fri 26 Sep, a quarter of an hour after his base post of 16:53. No code change is implied |
| 5 | MAJOR | 'The bathroom ones' did not match the game's Bathroom category | The pack list's Category column is the game's category (`research/object_categories.csv`, 246 rows read from the repository tree). All thirteen Bathroom objects are lines, the iron, the ironing board and the washing machine among them; `plan/design_model.py` asserts every board item against the tree |
| 6 | MAJOR | The 'art changed' rule forked on UI lines (match3d#461, #471) and the shared atlas (#460) | No UI piece is Delivered or Ready: 'Item visuals' and 'UI elements' are Owed on their own notes (not exported). #460 and #461 are in the two-reading table and trap T18; #460's comment speaks only of additions (`harmonygames-Games/match3d#460`). Objects #460 seems to modify (Toy Truck, Strawberry, Clef, Music Note 1 and 2) are not on the list |
| 7 | MAJOR | #462's changed objects are in its comment, not a file list; it also touches Kettlebell | The decider is the pull request with its comment `harmonygames-Games/match3d#462#c_1`; the surface names `github_get_pull_request_comments`. Kettlebell, Dart Board and Candy are not lines (the last two are not game objects in the tree). REVISED is three lines: Cactus Plant, Chainsaw, Cone |
| 8 | MINOR | The vendor's 'only missing piece is the duck' read against Owed and Ready lines | The pack ticket says what the first zip was; sound, 2D and font tickets say in words that they did not go. Two-reading row 'What the first zip held' |
| 9 | MINOR | Julia's DM with Claire is Turkish | The planned message is in Turkish, in Claire's register (`D05HMBQUC8Z/1758555266.534569` as the model); the base sweep was re-run on the D2 wording, 'banyo' included |
| 10 | MINOR | Cards SC-36, SC-7, SC-22, SC-50, SC-49, SC-70 without a disposition | Each has a row in section 1a |
| 11 | MINOR | The bow thread asks for an arrow | Robert's planned reply settles it: the bow as it is now, the arrow as its own item later (`C08R8CHB0QL/1758904025.123869`) |
| 12 | MINOR | Names and sets that collide or drift | Names are the tree's (Grand Piano, Cone, Retro TV, Cabinet Sink). The sound line is 'Background music'. 'Round' is gone and the six carry no label: Robert's reply says 'add these six' (their names are attested in `C08R8CHB0QL/1756813716.024339`) |
| 13 | MINOR | Census A read 81 of 203 September messages in #zm-animations | The channel was re-read for 24 to 30 Sep by the reviewer (`C09ATAJ220H/1758881478.985769` to `C09ATAJ220H/1758905816.794149`); the sibling sweep in section 1a uses the fact pack |
| 14 | MINOR | The ask is only narrowly believable after the pause | Kept 'while it's parked' and the reason (no third slip; redo that part in November). Leonard's Trello comment is at 20:05 UTC and does not name Julia |
| 15 | NOTE | Base has no Linear comments; Brian has one ART ticket | Tickets moved to ZOM, where Brian created 13 issues in September and where object tickets live (`ZOM-97` and its 51 children). Comment ids are the generator's uuid5 form. The volume's purpose is stated per group in section 2 |
| 16 | NOTE | Every minted time on second :00; Trello badge companion missing | Slack and Trello times carry arbitrary seconds; the badge is in the companions table. Ticket notes get jittered seconds at injection |
| 17 | NOTE | Calvin's sheet must agree with base on the match scale | The sheet says 'made here: pitched in Reaper from the sample Robert generated' (`C09A7PDFYCV/1755464752.078539`). The two held-back cues are the rocket sound (library seat) and the explosion (bought pack), consistent with `C07JYF2CFFU/1737054449.137119`; the sentence 'no base record states a licence' is gone |

### Reviewer 2: forks, fairness, shortcuts

| # | Severity | Finding (D1) | Disposition in D2 (evidence) |
|---|---|---|---|
| 1 | BLOCKER | The ask's 'anything they've asked us for in the channel' clause forked the line set | The clause is gone (`plan/planned_texts.py` ASK). The line set is Brian's list plus Robert's additions; 'Item visuals' has its own line, and the animation and zombie choice goes in the brief by the notes |
| 2 | MAJOR | Delivered-then-changed met the Delivered definition | 'Delivered: PlayableX has the current file and can use it.' No Delivered line changes in D2 |
| 3 | MAJOR | Buttons had three defensible states | No Buttons line. Every Owed-on-its-own-note line says 'Not exported' or 'Not sent' in Brian's words, with who has it |
| 4 | MAJOR | 'It opens' and 'nobody is changing it' had no positive evidence | Every exported line's note says it opens (or plays). The notes add: 'Take it as it stands unless something later says otherwise'. PARENT's failure is a zip that will not unpack |
| 5 | MAJOR | Nine Done tickets whose note said not done | Delivered tickets are Done; every other ticket is In Progress; the pack ticket says a line's ticket closes when PlayableX have the file. Workflow state is consistent with every note and says nothing about Ready or Owed |
| 6 | MAJOR | The list was dated before events it recorded | Last modified 26 Sep 17:25 UTC, after the 17:00 pack; it names no zombie; Robert's reply is at 21:41 UTC |
| 7 | MAJOR | Board set column and three brief rows were graded but not asked for | The notes name the list's columns and what the brief covers (scenario and purpose, the eight and the extras, zombies and animation, won and lost, tray, sound, start date) |
| 8 | MAJOR | Calvin as owner of the two cues was in no record | Calvin's sheet carries 'not made yet, Calvin' under 'Our own version'. Graded owner samples are only those a deciding record names |
| 9 | MAJOR | The under-70 forecast rested on 47 per-comment rows | The comment, move, create and share writes are declared templates; the skeleton is the surface plus four volume rows (56 rows, 196). The budget and the policy table are computed on that shape (section 6) |
| 10 | MAJOR | Selectors that could not pass, or passed on wrong answers | The surface follows `research/selector_guide_D2.md`: one tracked ticket, comment and create rows by body words, the brief on `gdocs_create_document`, labelled count regexes, explicit key names, `issue_key` comparator for people, `""` for the Slack posts; the Drive-root slot is dropped. `gradeable-report`: 52 of 52 |
| 11 | MAJOR | A sampler could finish near 95 calls | Every category mixes Ready lines, lines Owed on their own note and lines from different exports; 15 self-stated Owed lines sit in ten groups, so the totals and three sample rows punish sampling. `linear_show_data` is on the pre-check list |
| 12 | MINOR | Each deciding record was one search away through a unique token | The D2 records share no rare token with the ticket notes (sweep in section 12); `path_exposure.py` and the haystack decision are injection-stage work. Section 6 reports a sensitivity run with the anchors found as often as a coin flip |
| 13 | MINOR | Two statements about #462 were wrong | Corrected (reviewer 1, row 7) |
| 14 | MINOR | Arthur's post had no stated path | The path is the vendor's binary-only rule on the hub, Frederick's relay of it to Julia, and the two kinds of note ('saved out of the project' against 'FBX from Claire'); the post is in a channel Julia posts in |
| 15 | MINOR | Claire's DM: a private withdrawal that left ticket notes saying the opposite | Claire wrote no ticket note; her message is about Julia's levels and says she will note the tickets when done |
| 16 | MINOR | The parent of Robert's reply is about changing the bow | Settled in the reply (reviewer 1, row 11) |
| 17 | MINOR | Export method missing on some notes | Every note states source and day (`plan/design_model.py` NOTE) |
| 18 | MINOR | The vendor's 'only missing piece' sentence | Reviewer 1, row 8 |
| 19 | MINOR | Category labels and one name for two things | Reviewer 1, rows 5 and 12 |
| 20 | MINOR | Numbers and ids that disagreed across artifacts | The document is assembled from the model after every change (`plan/run_checks.sh`, `plan/assemble_design.py`); spans are the three anchor names |
| 21 | NOTE | Fit: the brief was 12.8 % of the surface | The brief has nine rows (29 of 192) with marketing substance from base: what Scenario 1 is for, the eight and the swappable extras, the zombies and animation, sound, the first-click rule. The list is an authored document too; ticket work is follow-through |
| 22 | NOTE | The start-date row cannot discriminate; comments are a carrier base never uses | The start date is one weight-1 row. The comment volume is named in section 2 for the injection dossier |

### Focused re-check of D2 (same two reviewers, 2026-11-11)

Reports: `Working_Files/research/recheck_D2_base.md` (no blocker, five majors) and `Working_Files/research/recheck_D2_forks.md` (no blocker, six majors). Every major is fixed in this document and its generators.

| # | Finding on D2 | Fix (evidence) |
|---|---|---|
| B1 | Frederick's notes and hold were stamped inside an investor call on his calendar; the ask followed it by 73 seconds | Notes created 16:25 and last edited 16:58 UTC, hold created 17:05 UTC, ask at 18:21 UTC (`evt_2204ffea306847eea6e5b0`, `C07C2866011/1759255794.996929`) |
| B2 | Brian's comment said 'when we pick this back up' ten hours before the pause was decided | Dated Tue 30 Sep 09:12 UTC, the morning after the pause (`C08H78VJG80/1759174925.309129`) |
| B3 | Robert's eight landed one second after his own message in another channel | Moved to 18:12:26 UTC on 25 Sep, inside his silent half hour (`C09ATAJ220H/1758822640.844519`) |
| B4 | 'The bounce ones' is a longer set in base, three of them on the sheet | The reply says 'add these six' and lists them; no label (`C08R8CHB0QL/1756813716.024339`) |
| B5 | A file named for the Armchair went to Brian for the first zip | Armchair is off the list; Cooler takes its place among the lines saved out of the project (`D076Y0SDV18/1758715979.943409` is the base file) |
| B+ | Below the bar: an open rendering ticket naming listed items; match3d#469; Marcus's tools; the scale's label; the zombie answer's timing | First Aid Kit is off the list (Ladle added); Music Keyboard, Grenade and #469 have two-reading rows (`ZOM-449`, `harmonygames-Games/match3d#469`); Marcus's post no longer mentions Blender; Calvin's sheet lists the combo-meter scale as its own row; Robert's answer says 'in case we carry on with them' |
| F1 | EXPORT passed on suspicion: the twelve notes named the tool and dropped 'looks right' | The twelve notes read 'FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.'; only Marcus's post says Unity and the exporter (`plan/design_model.py` NOTE) |
| F2 | The eight instruments met the Ready definition word for word | The notes' Ready test now reads 'exported in a format they take and sitting in the outgoing folder, it opens …'; Brian's comment says the eight are not in the outgoing folder any other way (`plan/planned_texts.py`) |
| F3 | Plain first names in planned Slack text were unique search keys | Mentions replace names in Marcus's post and Robert's reply; Claire's message names nobody ('cuma verdiğim banyo dosyaları'); the sheet's fourth column is 'Replacement'; names join the SQL wording sweep |
| F4 | The owner slots compared a first name against a full name | The truth of 'Who has it' is the first name (`plan/design_model.py` field `who`) |
| F5 | Six regex slots misgraded natural answers | K1, K3, B1, B3, B4, B6 and X6 use the tested patterns from the re-check; `gradeable-report` re-run (§12) |
| F6 | The first-click row was not in the notes' list | The notes' list now ends 'what they can use for sound and when the music may start, and the start date' |

### Path exposure at injection (D2.2)

`tools/path_exposure.py` on the first SQL of D2 reported two coin-flip records on a swept path. Robert's reply named list items (the bow, the dynamite and six items to add), so it was the newest Slack hit for each of those names; and Brian's note on the instruments' zip was a comment on the pack ticket, a record the notes name. Both were moved, not excused: the reply now names no item (the bow comes from the post it answers, the dynamite is 'the last one on my list') and adds no line, and the zip problem is in Brian's own log of the outgoing folder, a Google Doc that nothing links (`f_faf4d7c167d14a1127dcc3`). The six added lines, their tickets and the new-ticket write are gone with it; the list is Brian's 96 lines. Re-run: all six deciding records OFF-PATH (`Working_Files/01e_Path_Exposure.json`). The mechanism PARENT is renamed ZIP.

### Coherence sweep at injection (D2.3)

Two cold reviewers read the ask and the injected records against the base (`Working_Files/local_reviews/coherence/round1/`). Both reached the designed counts on their own. Their findings were settled in the data, not in wording for the prompt: nobody waits on the requester (the background music waits on Calvin's loop); a changed file sits with whoever it came from; the notes name one statement about sound (the rule on when music may start); Line, Category and Ticket are copied from Brian's list; extras are board items; the sentence about a line without a ticket is gone (every line has one); Brian's log no longer says Claire has finished, and the lines still not exported are noted on Monday after that day's batch; the bow's file is of Monday, after Friday's arrow thread; the cannon's note covers its projectile and the background's note says which background went; the zombie note agrees with the vendor's 29 Sep message; the hold exists before the notes that name it were last edited; Leonard's comment agrees with the channel and the ask; the ask asks for the count for each state. No mechanism, deciding record, slot or weight changed.

The same sweep moved the pack tickets from ZOM to the Design team. In ZOM the 97 keys sat above `ZOM-566`, a base ticket created five days after them; both reviewers named that order as the most visible tell. In the Design team the last base ticket is `DES-312` (Brian, 7 May 2025), so `DES-313` to `DES-409` follow in number and in date, and Brian's own last tickets there are a parent (`DES-307`) with bare-titled children made seconds apart. Julia, Brian, Claire and Robert are members of that team (`/team_memberships`). The pack ticket's description says why it is there. The playable's music is now a new track made for the ad (the in-game track was a found file in base), and no two notes share a second.

With the prompt written, both reviewers read it with the records: nothing untrue, no hint, no finding handed over, six outputs under every reading. Both noted that the share instruction sat only in the notes while the message named the notes for three other things; the message now also says the notes cover 'who gets the files'.

### D3 (rev2) red team

RED TEAM FALLBACK (D3): the dual red-team tool still cannot run here (no `REDTEAM_*` variable is set). D3 changes four records and no rule, line or row, so the review that fits the change is on the rendered records: the two cold coherence-sweep reviewers of `/create-injection` (`coherence_sweep.py brief`, fresh context, no sight of this document) read the rev2 SQL and the prompt for forks, contradictions with base and planted-record tells, and every finding is settled in data before the injection gate. The D2 reviews above stand for the unchanged design; the rev1 runs themselves (one pre-check, six baseline runs, `01a_Hardening_Report.md`) are the strongest review of D2 there is.

## 14 Revision intake (S0r)

Verdicts file consumed: `Working_Files/run_forensics/rev1/node_verdicts.json` (the six baseline runs, each BOUND to rev1 as the sole revision: basis 'sole revision', 282 seeded needles seen per run); the pre-check's verdicts are in `Working_Files/run_forensics/rev1/precheck.node_verdicts.json`. Report: `Working_Files/01a_Hardening_Report.md` (MODE B, `STAGE GATE hardening: PASS`); dispositioned ledger records: 126 (the eleven misses are recorded as landed). No export is historical: all seven are bound on evidence to rev1, the revision they ran on, and none certifies rev2.

| Rule | Runs | Proposed verdict | Disposition | Evidence (run · event) |
|---|---|---|---|---|
| EXPORT | run-1 to run-6 (2 missed, 4 found); precheck missed (event 528) | tool: NOT-REACHED in 2, LEAKED in 4; dispositioned: a miss of a reachable record is LANDED (playbook 01a gate 8) | rebuild: keep the post's place, author and time; reword it so it does not repeat the note it corrects (D3: 'got out of unity'; rev2 sweep: 'the setting was wrong that day', so the 24 Sep zip is not drawn in) | run-4 event 440; run-5 event 452; two of the four finds came through the note's own words ('saved out', run-2 event 424; 'export', run-3 event 304) |
| ARTHOLD | run-1 to run-6 (1 missed, 5 found); precheck found (event 528) | tool: NOT-REACHED in 1, LEAKED in 5; dispositioned: a miss of a reachable record is LANDED (playbook 01a gate 8) | rebuild: move the statement from Claire's DM to Robert's DM with Julia, people tagged (D3 record `a2_dm`) | run-1 event 555; six of seven runs reached Claire's DM by a search for her recent messages (precheck event 322, run-2 event 466, run-3 event 284, run-4 event 347, run-5 event 270, run-6 event 478) |
| REVISED | run-1 to run-6 (0 missed, 6 found); precheck found (event 528) | tool: NOT-REACHED in 0, LEAKED in 6; dispositioned: a miss of a reachable record is LANDED (playbook 01a gate 8) | rebuild: turn the unit into a completion note elsewhere: Brian's log records the re-send, so the three lines are Ready and a run that stops at Robert's base post writes them Owed | no miss (e.g. run-1 event 555); every run settled it from #zombie-design (precheck event 80, run-1 event 512, run-6 event 281): FALSE as a retrieval unit |
| AUDIO | run-1 to run-6 (1 missed, 5 found); precheck found (event 528) | tool: NOT-REACHED in 1, LEAKED in 5; dispositioned: a miss of a reachable record is LANDED (playbook 01a gate 8) | keep: unchanged; it is a lookup (the notes state the rule and the sheet's title holds the noun) and stays for realism | run-1 event 555; found in six of seven runs, missed once (run-1, register write event 555) |
| PICKS | run-1 to run-6 (3 missed, 3 found); precheck missed (event 528) | tool: NOT-REACHED in 3, LEAKED in 3; dispositioned: a miss of a reachable record is LANDED (playbook 01a gate 8) | keep: unchanged: a live coin flip | run-3 event 409; run-4 event 440; run-5 event 452; missed in four of seven runs (precheck event 528, run-3 event 409, run-4 event 440, run-5 event 452) |
| ZIP | run-1 to run-6 (1 missed, 5 found); precheck missed (event 528) | tool: NOT-REACHED in 1, LEAKED in 5; dispositioned: a miss of a reachable record is LANDED (playbook 01a gate 8) | rebuild: take the word 'sound' out of the log ('The .wav exports.') so the AUDIO search no longer lists it | run-1 event 555; five of six baseline finds came through the full-text search for 'sound' (run-2 event 406, run-3 event 333, run-4 event 307, run-5 event 384, run-6 event 419) |

CONFOUNDED: none assigned. No rule carries a tool flag; the counter-readings of the report (§12 there) found no tool, fairness, verifier or run cause for any miss: every deciding record is body text Julia can open, returned by an ordinary call in other runs, incorporated through the ask and the notes, and the failed slots were confirmed against the write payloads. One grader defect was found and corrected outside the design (run-5's shares gave no role; the tool grants reader).

**Routing.** Universe: the four rebuilds above, implemented by `/create-injection` as rev2 (records `a2_dm`, `a1_post`, `c4_log`; Claire's D2 DM row removed). Prompt: no defect found (`/prompt` PASS, all dimensions 5); the prompt is unchanged. Oracle Events: the rev1 draft is regenerated on rev2 (`/create-oe-writing`). Rubric and verifier: none exist yet; for the rubric stage, accept a share without a role argument when the tool returns reader.

**Purged:** REVISED as a retrieval unit on the pull request (rebuilt as a completion note); the Turkish wording as a difficulty (it goes with the ARTHOLD move). **Kept as realism:** AUDIO, the Trello kickoff card (no rev1 run opened Trello).


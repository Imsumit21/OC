# Scenario Design — julia_zm3d_playable_brief (design D1) · design only · contains no prompt, OE or criterion text

Written 2026-11-11 by `/create-scenario` (Claude, authoring session) from `00_Pre_Scenario_Analysis.md`, three read-only censuses of the synth-cut base (`Working_Files/research/census_A_design_channels.md`, `census_B_build_art_channels.md`, `census_C_other_services.md`) and the generators in `Working_Files/plan/`. Planned (seeded) records are described, never written as SQL here. Ids of the form `C…/ts`, `ART-n`, `f_…`, `evt_…`, `cmt_…` without the word base are minted for `/create-injection`.

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe | key `synthcut`, label Oct 1, 2025 (synth-cut), `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)`; seed bound `freeze_utc` 2025-10-01T00:00:00Z (Tue Sep 30 17:00 PT); `shutdown_rules_apply` false (the company operates normally) |
| Assignment (V3, 8 fields) | business_function Product · persona Julia Lawson · role Product Manager · competency Marketing and GTM · task_skill Authoring · task_type long-horizon · difficulty_mode hard · universe date October 1, 2025 07:00 (context_hash `3246c54345b9`, assignment_hash `70579cebc8fc`) |
| Evals category | Product & Design (`Evals/references/rules/task_categories.md`: product decisions, gameplay/design requirements, art and prototype evaluation), inside Marketing and GTM: the artifact is a playable ad, a user-acquisition creative |
| Loss budget | Hard cap < 70 % (`difficulty_cap` 0.7); design target E[avg] ≤ 62 %; requester targets in the draft manifest `author_targets`: more than 130 counted calls in every run, average under 70 %, every other difficulty gate |
| Horizon | Long Horizon → `effective_profile: extreme`; `volume_exception {call_budget_floor 220, per_record_floor 110}` (budget 258, per-record 193; requester's words quoted in the manifest) |
| Theme screen | the storyline is ad production (objects, exports, formats, sound, a vendor hand-off). The game's name cannot be avoided; no seeded text uses infection or outbreak vocabulary, and seeded text says 'ZM3D' or 'the game'. The pre-check is read for model-fallback events (`Hardness_Mastery.md` §12: suspected, not proven) |
| Fit census | `Working_Files/00_Assignment_Fit.json`: `NO NATURAL COHORT` (WARN mode); Gmail THIN for this persona, so no anchor and no coin-flip record sits in her mailbox; route S2x: the scenario is built by injection on base containers she can read |
| Persona card | `references/persona_cards/synthcut/julia_lawson.json`: earlier tasks used ZOM tickets and the match3d repository as cohorts (claims register, difficulty baseline, beta calendar, audience call). This design's cohort is the lines of one asset pack on new ART tickets; no earlier cohort, rule vocabulary or record set is reused |
| Role remit | Julia wrote the brief for the first playable: `C08H78VJG80/1741963515.221549` (2025-03-14, her storyboard to PlayableX) and the vendor's reply 'thank you so much for this detailed brief' (`C08H78VJG80/1742063341.276529`). For the second playable Brian asked her for the reference level on 2025-09-22 (`C090N54TG79/1758568735.563539`). The design page names her: `confluence:page_zm3d_gdd` v2, 'Owner: Robert (Product). Design: Julia Lawson.' Role review: `Working_Files/00_V3_Authoring_Evidence.json` (`role_reviews.scenario`) |

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

Identities (`entity.py resolve "Julia Lawson"`, §1c): Slack `EMPLOYEE_0005_SLACK_ID`, Linear `usr_8140f09bf9f1b94c`, GitHub `PERSON_0005_GITHUB_USERNAME`, Trello `793af7ca6940bf18eb516c75`, Contacts `8140f09bf9f1b94cb8ee2dd7`, Drive root `d_8140f09bf9f1b94cb8ee2d` (owned). Her calendar's time zone is Europe/Istanbul (gcal `/calendars/13`); persona-written dates are still Pacific with UTC beside them when the day differs.


## 1 Storyline

**The base, as read.** On 2025-08-26 Leonard opens a second playable with PlayableX, for Zombie Match 3D (`C08H78VJG80/1756223629.429589`). On 2025-09-15 Frederick picks Scenario 1 and names the open questions: which objects are on the board and which zombies are hit (`C08H78VJG80/1757956024.883249`). The vendor offers editable items 'aside from the 8-item set that you will provide' and says which file types it takes (`C08H78VJG80/1758022459.227279`), then lists the assets it expects by group (`C08H78VJG80/1758283671.878269`). Brian packages: a zip on 24 Sep (`C08H78VJG80/1758717576.077489`), the plushie the vendor called 'the duck asset' the same day (`C08H78VJG80/1758723504.085039`, `C08H78VJG80/1758729487.922339`), a corrected zombie pack on 26 Sep after the vendor asked for a package tested 'in a blank Unity project' (`C08H78VJG80/1758808234.045839`, `C08H78VJG80/1758906043.375719`). On 29 Sep the vendor asks for one primary animation and four zombies (`C08H78VJG80/1759140968.965099`); the same evening Frederick pauses development 'for a month or so' (`C08H78VJG80/1759174925.309129`); on 30 Sep 09:59 UTC the vendor sets the new start for 3 November (`C08H78VJG80/1759226395.551469`). The start had already moved from 29 Sep to 6 Oct for late assets (`C08H78VJG80/1758701898.919999`). No Slack message says 'playable' after the pause post, and no record of any service is dated between the vendor's reply and the data horizon that touches it (census A §G, census B §I).

**The job (planned).** On Tue 30 Sep 18:10 UTC (11:10 PT) Frederick asks Julia in their DM (`D05SD5QLG94/1759255800.418239`) to do for this playable what she did for the first: write what PlayableX builds from, and say where the pack stands, for the game as it is today. He names three things it starts from: Brian's pack list, Robert's picks, his own hand-off notes. The deliverables are a brief (a Google Doc) and a hand-off list (a Google Sheet) in her Drive, the ticket follow-through the notes ask for, the three counts back to him in the DM and both links in the PlayableX channel.

**Why now, against the pause.** The four latest base lines about the playable are of 29 Sep: Leonard expects a change to the core game and does not want the vendor's work wasted (`CADCE44A365D/1759171993.180879`, `CADCE44A365D/1759172018.976319`); Brian says a playable of the game in its current form would not be needed after a change (`D076PSEBC4D/1759171889.924089`) and that the vendor's optimizations of animations, panels and objects would carry over (`CADCE44A365D/1759172311.343939`). Julia is in neither conversation (`can-see` NO). The planned ask agrees with all four: it does not say the playable will ship as specified ('if the core changes we redo that part with them in November'), and what it asks for is the part that slipped the start twice and that carries over: which files PlayableX holds, which are fit to send and which are owed. Robert's base line that the playable tests 'the current form' (`C090N54TG79/1758569655.409719`) is the same scoping.

**Anchors per service.** Slack: the ask `D05SD5QLG94/1759255800.418239` (planned); the vendor channel `C08H78VJG80` (base, 198 messages); Robert's picks `C090N54TG79/1758646800.552319` and `C090N54TG79/1759167000.736119` (planned, #zombie-design). Docs: Frederick's notes `f_8c1d0bca1d1d5fde4c5008` (planned); base `f_05bedd1540d3e01a90ab16`. Sheets: Brian's pack list `f_956e60ec7f2f7977d98934`, Calvin's source sheet `f_b2387e31d46d3a7b3fa2a9` (planned). Linear: ART-793 and children ART-794 to ART-890 (planned; base precedent ART-792, Frederick's marketing-screenshots epic). Slides: Julia's reference-level deck `f_6a2fa8e61b31139ca8e3d4` (planned). Calendar: the kickoff hold `evt_421695d009e589ee85296c` (planned; base precedent `evt_257421bc09196edbf28758`, the 2025-03-12 vendor meeting Frederick organised with Julia invited). Contacts: `d7d31caf63ee33db2b7ed271` (planned). GitHub: base `harmonygames-Games/match3d#462`. Confluence: base `page_zm3d_gdd`. Trello: base card `688c4d14c312a27fa2747e40` with a planned comment `68dc207c75aff34acf5a5424`.

**Universe KB.** Timeline (`references/universe_kb/by_universe/synthcut/timeline.md`): the window sits after the spine beats '2025-09-15 Season Pass built for Zombie Match (match3d) - PR #438' and '2025-09-30 PR #476 Vision bot opened and merged'; neither is touched. `cohorts.json`: no fit — every KB cohort is a base Linear state or label set (`LIN-S01` … `LIN-L30`); this cohort is the lines of one pack on seeded ART tickets, defined by a seeded sheet. `trap_catalog.json` entries the traps stand on: `C01` (thread replies that correct or retract: T5), `C02` (a parent states a resolution and another record says it still fails: T1, T7), `D05` (title families with version markers: the 'old' item docs, avoided), `K02` (app-name lineage, 'Puzzles vs Zombies': not used as an alias), `N01` (ticket series collisions: ART numbers overlap ZOM and ENG numbers; every ticket is cited with its team key), `P01` (shared first names: §1c).

### Coupling seams

- The pack list `f_956e60ec7f2f7977d98934` has no state column, and every line ticket (ART-794 to ART-890) is Done: a line's state needs the note on its own ticket (how and when it was exported) joined to a rule in the notes `f_8c1d0bca1d1d5fde4c5008`.
- 'Exported' on a ticket and 'the file is usable' are two facts. The second lives where the tool, the art or the sound is discussed (`C08R27X0EAH/1758963900.284719`, `D05HMBQUC8Z/1758874200.613049`, `f_b2387e31d46d3a7b3fa2a9`), not on the ticket.
- The delivery date of a file and the date the art last changed are in different services: Slack `C08H78VJG80/1758717576.077489` and GitHub `harmonygames-Games/match3d#462`.
- The default eight are fixed by one person's two messages in two channels: `C090N54TG79/1758646800.552319` and `C08R8CHB0QL/1758906300.447189`.
- The sound rule in `f_8c1d0bca1d1d5fde4c5008` is about ownership; the sound tickets (ART-884 to ART-889) only state the file type.


## 1a Coherence audit

Scope = every record a correct run opens: the ask, the notes, the pack list, the pack ticket and its 97 children with their comments, the vendor channel in full, the #zombie-design playable thread and Robert's two posts, #zombie-art from 23 Sep, Julia's DM with Claire, #zombie-bugs from 25 Sep, Calvin's sheet, Julia's deck, the design page with its comments, the kickoff hold, the contact, the Playable Kickoff card, match3d#462. Hazard ids are from `references/universe_kb/by_universe/synthcut/coherence_hazards.json`. Known-data-issue cards read: `references/known_data_issues/synthcut.md` (SC-1 to SC-73); cards the scope touches are SC-13, SC-58, SC-8, SC-38 and SC-16, each with its disposition below.

| Record | Category | Fields | Pointer | Hazard / card | Disposition |
|---|---|---|---|---|---|
| vendor channel thread order | temporal | three start dates in one channel | `C08H78VJG80/1758022459.227279`, `C08H78VJG80/1758701898.919999`, `C08H78VJG80/1759226395.551469` | hazard T02 (not chronological files): none of these; card SC-13 | fold: a dated claim sequence, the last stands (T8); the beta date is never graded |
| Leonard's Playable Kickoff card | temporal | dateLastActivity vs actions | `688c4d14c312a27fa2747e40` (actions 2025-08-01, 2025-09-13) | hazard T06 | fold: the planned comment moves the card's and the board's dateLastActivity to the comment's time |
| vendor's name | semantic | 'PlayableX' in Slack text, '[USERNAME_36301]' in mail and calendar titles | `C08H78VJG80/1741284538.488439`; gcal `evt_257421bc09196edbf28758` | hazard S03: none in scope; trap catalog X04 (uneven masking) | fold: seeded text uses the Slack spelling Julia sees; no row depends on a mail or calendar title |
| roles in Slack vs roster | semantic | Julia called 'our lead designer' and Brian 'Product Manager' in one vendor-channel message | `C08H78VJG80/1741796408.361009` | none listed | avoid: no seeded text states either title; the assignment's role governs |
| design page vs its comments | cross-service referential | tray 7 on the page, a 6-slot proposal in a comment | `page_zm3d_gdd` with `confluence:comment_zm3d_gdd_c1`, `confluence:comment_zm3d_gdd_c2` | cards SC-8, SC-38, SC-58 (other sentences of the same page) | fold: Robert's reply on the page keeps 7 (T9); the page's sentences on the glass crash, the Season Pass date and the monster roster are neither cited nor graded |
| Slack links to Google files | cross-service referential | native ids never equal export ids | planned Slack records, e.g. the ask `D05SD5QLG94/1759255800.418239` | hazard R04 | excluded: no seeded Slack text carries a document link; the ask names the notes in words |
| calendar invitations | cross-service referential | invitation mails without a calendar row | hazard R08 | hazard R08 | fold: the hold is seeded with one row per attendee calendar and its invitation mails (INT-11) |
| thread counters | quantitative | reply_count, reply_users_count, latest_reply of Julia's bow post | `C08R8CHB0QL/1758904025.123869` (1 reply in base) | hazards Q01, Q02, Q03 | fold: the planned reply updates the three counters as companions |
| counts in the deliverables | quantitative | 19 Delivered, 30 Ready, 54 Owed of 103 lines | `plan/design_model.py`; the pack list `f_956e60ec7f2f7977d98934` and ART-794 to ART-890 | hazard Q01 kind (a stated count against the rows): none in base for these records | fold: every count comes from the model; no base figure is restated |
| merged pull request without review | state/lifecycle | match3d#462 merged with no human review | `harmonygames-Games/match3d#462` | hazard L09 | fold: the task uses its merge time and the objects it changed, never its review state |
| Linear state vs shipped work | state/lifecycle | tickets open after work shipped | ZOM-564, ZOM-513, ZOM-514, ZOM-563, ART-790, ART-792 | card SC-16; hazard L06 (parent Done while child open): none in scope | avoid: none of those tickets is cited; the pack ticket is a new Team Epic with its own children |
| ids of seeded records | identifier/format | Slack message id, Linear keys, Drive ids, Trello action id | `plan/check_ids.py` output: ART-793 to ART-890, `f_8c1d0bca1d1d5fde4c5008`, `68dc207c75aff34acf5a5424` | hazards I01, I02, I10 (`usr_Robert`), I15 | fold: ids follow the base schemes; Robert's Linear id is `usr_Robert` as in base; no collision (§12) |
| object names | other | the July export lists 151 objects; a 23 Sep commit shortened long names | gsheets `f_7efae6c05be5c2414e8798`; census B §A.4 | none listed | fold: every line takes a name attested in base; no row grades a prefab or file name |

**Sibling-defect sweep.** Designed defect kinds and their base siblings: (a) a 'done' ticket whose file is unusable: base has the 25 Sep zombie package ('Only the prefabs were included', `C08H78VJG80/1758808234.045839`), repaired in base on 26 Sep and kept as a control (T10); (b) art changed after a hand-off: base has exactly the five lines of match3d#462 and the rocking chair rework of 29–30 Sep (`C08R8CHB0QL/1759190391.487809`), which is not on the pack list; (c) a pick changed in a reply: base has Julia's own grenades-and-shuriken idea, answered 'remain as is' (T13). No other sibling was found in the windows read in full (census A: #zombie-design from 1 Sep, the vendor channel, #zm-animations, #zombie-sfx; census B: #zombie-art and #zombie-match3d September, #zombie-bugs by filter and from 27 Sep).

**Base facts the plan must not contradict** (each checked): no board object was stripped from a build and the game has no addressables for objects (`C08R27X0EAH/1758905363.341129`), so no line's state depends on a build; the September clone items 'don't work yet' (`C05433XK267/1758854356.576719`) and none is on the pack list; no base record states an art sign-off rule, a licence or a rule on sharing source art (census A §C, §F; census B §D, §G), so the planned notes, Claire's DM and Calvin's sheet add facts and overturn none; the vendor's price and bundle choice are open in a DM Julia cannot read (`D08JRD3TQE8/1756322075.746289`, `D08JRD3TQE8/1759115937.979409`) and no seeded text states a price or a signed order.


## 1b Active speakers

Status from `references/universe_kb/by_universe/synthcut/activity.json` (`status_at_clock`). The PlayableX staff (`PERSON_6078_SLACK_ID`, `PERSON_3937_SLACK_ID`) are Slack-only ids with no status row and get no seeded voice: every vendor statement the design uses is a base message.

| Person | Email | status_at_clock | Seeding role |
|---|---|---|---|
| Frederick Stone | frederick.stone@harmonygames.co | active_sep_2025_quiet_in_oct | the ask `D05SD5QLG94/1759255800.418239`, the notes `f_8c1d0bca1d1d5fde4c5008`, the pack ticket ART-793, the hold `evt_421695d009e589ee85296c`, the contact |
| Brian Foster | brian.foster@harmonygames.co | active_sep_2025_quiet_in_oct | the pack list `f_956e60ec7f2f7977d98934`, the 97 child tickets and their export notes, the pack-ticket comment `cmt_8b590c43980032fc5d02` |
| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | the picks `C090N54TG79/1758646800.552319`, the zombie answer `C090N54TG79/1759167000.736119`, the reply `C08R8CHB0QL/1758906300.447189` |
| Claire Morgan | claire.morgan@harmonygames.co | active_sep_2025_quiet_in_oct | art notes on tickets; the DM `D05HMBQUC8Z/1758874200.613049` |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | the #zombie-bugs post `C08R27X0EAH/1758963900.284719` |
| Calvin Price | calvin.price@harmonygames.co | active_sep_2025_quiet_in_oct | the sound source sheet `f_b2387e31d46d3a7b3fa2a9`; notes on the sound tickets |
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | the Trello comment `68dc207c75aff34acf5a5424` |
| Julia Lawson | julia.lawson@harmonygames.co | active_sep_2025_quiet_in_oct | her reference-level deck `f_6a2fa8e61b31139ca8e3d4` (23 Sep) |
| Martin Walsh | martin.walsh@harmonygames.co | active_sep_2025_quiet_in_oct | named as holder of the fonts; no seeded voice |

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
### Arthur Blake
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=35266, first_post=2023-03-20, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=arthur.blake@harmonygames.co, threads=3320, messages=5134, first=2023-03-23, last=2025-10-01, thread_filename_alias=['blake@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=arthur.blake@harmonygames.co, owner_email=arthur.blake@harmonygames.co, summary=Arthur Blake — primary, events=756, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_cc3e90160f49, email=arthur.blake@harmonygames.co, display_name=arthur.blake@harmonygames.co, root_folders=['d_cc3e90160f490686039986'], owned_items=246, last_modified=2025-09-19, files_shared_with=403   [join: exact_email]
  linear     id=usr_cc3e90160f490686, email=arthur.blake@harmonygames.co, name=arthur.blake@harmonygames.co, is_active=True, last_activity=2025-09-15   [join: exact_email]
### EMPLOYEE_0006_SLACK_ID
ENTITY email:calvin.price@harmonygames.co  name=Calvin Price  kind=person  emails=['calvin.price@harmonygames.co']
  persona: calvin_price - Game Engineer (Unity VFX) / Engineering
  slack      id=EMPLOYEE_0006_SLACK_ID, name=Calvin Price, real_name=Calvin Price, email=calvin.price@harmonygames.co, is_bot=False, deleted=False, messages=12017, first_post=2023-03-29, last_post=2025-09-29   [join: exact_email]
  gmail      mailbox=calvin.price@harmonygames.co, threads=8142, messages=9856, first=2023-03-29, last=2025-09-30, thread_filename_alias=['calvin@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=calvin.price@harmonygames.co, owner_email=calvin.price@harmonygames.co, summary=Calvin Price — primary, events=442, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_49b9dfa5208d, email=calvin.price@harmonygames.co, display_name=calvin.price@harmonygames.co, root_folders=['d_49b9dfa5208d400d9b3937'], owned_items=1918, last_modified=2025-02-14, files_shared_with=128   [join: exact_email]
  linear     id=usr_49b9dfa5208d400d, email=calvin.price@harmonygames.co, name=calvin.price@harmonygames.co, is_active=True, last_activity=2025-09-25   [join: exact_email]
```

Pinned entities and their lookalikes: Claire Morgan (`EMPLOYEE_0009_SLACK_ID`, Linear `usr_7fe31e7ec8199618`) against the GitHub-only 'Claire' login; Robert (Linear `usr_Robert`, hazard I10) has no surname in any service; Calvin Price has two GitHub logins and one Slack id (`EMPLOYEE_0006_SLACK_ID`); 'Blake' in base text is Arthur Blake. Victor Barnes (`EMPLOYEE_0030_SLACK_ID`), introduced to the vendor in March as the art director, left in April 2025 and has no seeded voice. No second account is created for anyone and no trap depends on a malformed id. The PlayableX intake contact is a role address, not a person, so it duplicates nobody.


## 2 Cohort spine

**Rule (closed).** A line is one row of Brian's pack list `f_956e60ec7f2f7977d98934` (97 rows: 78 board objects, 4 zombies, the cannon and its shot, 5 interface pieces, the board background, 6 sound cues, the fonts), plus any board object Robert has added since Brian made the list (the notes' sentence 'If Robert has added objects since Brian made the list, they go on it too'). Robert added six in one reply, so the list has 103 lines. The vendor's own requests add no line: its groups (`C08H78VJG80/1758283671.878269`) are all on the pack list, the 'duck asset' is the plushie line and the 'rocket launcher' is the cannon line (T16). Size 103; key = the line's name.

**Truth by class** (`plan/design_model.py`; Delivered 19, Ready 30, Owed 54):

| State | Lines | Why | Members |
|---|---|---|---|
| Delivered | 19 | in PlayableX's hands and usable (the 24 Sep zip, the plushie zip, the 26 Sep zombie pack) | Grenade, Couch, Iron, Shuriken, Bow, Cute Axe, Cute Hammer, Gift Box, Plushie Chick, Zombie Chef, Zombie Bike Kid, Zombie Boxer, Zombie Mayor, Cannon, Cannon shot, Tray, Monster HP bar, Item frame, Win and lose panels |
| Ready | 30 | exported on its own in a file type they take, current, nobody changing it | Rolling Pin, Patterned Teapot, Dutch Oven, Round Pan, Square Pan, Spatula, Whisk, Round Kettle, Small Kettle, Tall Kettle, Cup, Mug, Plate, Fancy Plate, Wine Bottle, Milk Carton, Armchair, RetroTV, Small Lamp, Desk Lamp, Alarm Clock, Record Player, Flower Pot, Watering Can, Dynamite, Garden Shears, Dice, Cannon sound, Win stinger, Lose stinger |
| Owed, stated on the line's own ticket | 9 | prefab only, not exported, flat PNG, PSD only, no track chosen, no font files | Wooden Crate, Wooden Bucket, Large Barrel, GrandPiano, Wheelbarrow, Buttons, Board background, Music, Fonts |
| Owed, EXPORT | 12 | exported in one go on 25 Sep: empty shells (Arthur's post) | Washing Machine, Oven, Refrigerator, Toaster, Coffee Machine, Microwave, Stove, Kitchen Mixer, Ice Cream Machine, Safe, Ironing Board, Square Table |
| Owed, ARTHOLD | 12 | set Bathroom: Claire is redoing the UVs (her DM) | Bathroom Scale, Bathtub, Hair Dryer, Wash Basin, Wash Basin Cabinet, Toilet, Toilet Paper, Plunger, Wooden Hairbrush, Electric Hair Trimmer, Slippers, Paper Towel |
| Owed, REVISED | 5 | the art changed on 25 Sep after the file went out or was exported (base) | Cactus Plant, Chainsaw, Traffic Cone, Dartboard, Candy |
| Owed, PARENT | 8 | set Music: the 26 Sep export comes in without textures (Brian's pack-ticket comment) | Acoustic Guitar, Electric Guitar, Cello, Harp, Trumpet, Tambourine, Cymbals, Xylophone |
| Owed, AUDIO | 2 | cut from a bought pack (Calvin's source sheet); the notes let only owned sound leave | Match scale, Explosion |
| Owed, PICKS | 6 | added by Robert in a later reply; not on the list, no ticket, not exported | Soccer Ball, Basketball, Toy Drum, Scooter, Bicycle, Toy Hammer |

**Surfaces and shortcut audit** (manifest `cohort.evidence_surfaces`):

| Surface | Records | Calls each | Bulk call that does not cover it | Why it cannot be skipped | Serves |
|---|---|---|---|---|---|
| linear `linear_list_comments` | 97 | 1.0 | linear_list_issues and linear_get_issue return no comments; each line's export note (file type, date, how it was exported) and art note are only in its own ticket's comments | the pack list has no state column: delivery says what went out, not whether the file is in a format they take or is still current; no other record states a line's export | R2: state per line: Delivered, Ready or Owed |
| linear `linear_update_issue + linear_create_comment` | 48 | 2.0 | no batch write exists for state changes or comments; each ticket takes its own calls | the notes require the Todo state and the comment on every Owed line's ticket; the sheet does not replace them | R6: an Owed line's ticket back to Todo with a comment saying what is owed and who has it |
| github `github_get_pull_request + github_get_pull_request_files` | 5 | 0.4 | a pull request search returns titles and bodies; #462's body is empty, so the objects it changed are only in its file list | the pack list and the tickets predate the 25 Sep change; nothing on them says the art moved after the files went out | R2: state per line: Delivered, Ready or Owed |

**Predicate.** Delivered: PlayableX has the file and can use it. Ready: exported in a format they take, it opens, it is the current version and nobody is changing it. Owed: anything else, with what is owed and who has it. The three words and their tests are in the notes; the facts are on the tickets and in the records of §5. **House rule that overrides the natural reading:** a Done ticket that says 'exported' is not Ready when the file is an empty shell, the art is being redone, the art changed afterwards, or the sound is not ours. **Dual regime by date:** a file that went out on 24 Sep or was exported on the morning of 25 Sep predates the art change merged at 23:15 UTC that day (`harmonygames-Games/match3d#462`). **Boundary records:** six lines outside the list (Robert's reply); the plushie delivered in a second zip the same day (`C08H78VJG80/1758729487.922339`); the zombie pack sent twice (T10); the nine lines that are Owed on their own ticket's note (Buttons went out in the zip as a flat PNG and is still Owed).

**Necessity of the per-line read.** 48 of the 97 listed lines are Owed and nothing upstream says which: the pack list has no state column. Every line ticket is Done (Brian closed each as he dealt with it, 23 to 26 Sep), so workflow state marks nothing either; the notes tell the reader that 'Brian's note on each says what he did with it'. Every ticket carries that note; art notes by Claire sit on 31 tickets across five sets, so a note by itself marks nothing. Notes state raw facts (how, when, what file type), never the state. Padding check: every line is an asset the vendor asked for by group or Robert put on the board or among the extras; none exists to raise a count, and each line's state is a cell of the hand-off list.

**Ids.** Tickets ART-794 to ART-890 follow the list order (`plan/design_model.py`); ART-793 is the pack ticket. Base highest ART number is ART-792 (census C §1). Collision check: §12.


## 3 Hidden authorities

| Id | Name (what it governs) | Home | Record | Governs | Decoy and its scope | Findability |
|---|---|---|---|---|---|---|
| H1 | Frederick's hand-off notes | gdocs | `f_8c1d0bca1d1d5fde4c5008` | R2, R3, R6 | gdocs: `gdocs:f_05bedd1540d3e01a90ab16` — game: Domino Delights (the first playable, April 2025: Leonard's Playable Feedback) | a search for 'hand-off notes' returns it; the ask names it in words |
| H2 | Brian's pack list | gsheets | `f_956e60ec7f2f7977d98934` | R1 | slack: `C08H78VJG80/1758283671.878269` — issuer: PlayableX's request (asset groups they expect, no lines) | a search for 'playable pack' returns it; the ask names it in words |
| H3 | the kickoff hold | gcal | `evt_421695d009e589ee85296c` | R7 | trello: `trello:688c4d14c312a27fa2747e40`, `68dc207c75aff34acf5a5424` — issuer: Leonard's own to-do card (no attendees) | a search for 'PlayableX kickoff' returns it; the ask names it in words |

`governs` lists do not overlap (H1: R2, R3, R6; H2: R1; H3: R7). H1 has a same-service decoy with an adjacent scope: Leonard's 'Playable Feedback' (`f_05bedd1540d3e01a90ab16`, the first playable, P0/P1/P2 feedback on dominoes). Each authority is named by what it governs or who issued it ('my hand-off notes', 'Brian's pack list', 'the kickoff hold'); no decoy carries a self-advertising cue. Findability of planned records is proven on the SQL at `/create-injection` (`persona_view.py check-sql`); the base decoys are YES in the reach table (§10).


## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Frederick's playable message | `D05SD5QLG94/1759255800.418239` |
| A2 | the PlayableX channel | `C08H78VJG80` |
| A3 | my Drive | `d_8140f09bf9f1b94cb8ee2d` |

**Hub.** Frederick's DM `D05SD5QLG94/1759255800.418239` (planned wording in `plan/planned_texts.py`). It delegates by role: 'Brian's pack list', 'Robert's picks', 'My hand-off notes', 'the channel'. It names no location, no id and none of the records in §5 that decide a row. The notes define the three states, the current-version test, the sound test, the board, the ticket follow-through and the sharing, as plain definitions; they point at the pack ticket, the design page, the deck, the kickoff hold and Contacts by name, and at nothing that decides a hidden row.

**Incorporation table** (every `delegation_quote` is an exact substring of the delegating record's planned or base text; the gate reads them):

| Fragment | Service · container | Kind | Chain | Delegated by | Words (verbatim) | Requirements | Names |
|---|---|---|---|---|---|---|---|
| K1 | gdocs · `f_8c1d0bca1d1d5fde4c5008` | delegation | A1 → K1 | `D05SD5QLG94/1759255800.418239` | 'My hand-off notes say what counts as ready and what to do with the tickets' | R2, R3, R6 | H1 |
| K2 | gsheets · `f_956e60ec7f2f7977d98934` | requirement | A1 → K2 | `D05SD5QLG94/1759255800.418239` | 'Brian's pack list is where it starts' | R1 | H2 |
| K3 | slack · `C090N54TG79/1758646800.552319` | requirement | A1 → K3 | `D05SD5QLG94/1759255800.418239` | 'Robert's picks for the board and the zombies stand' | R4 | — |
| K4 | slack · `C08H78VJG80/1758227288.370029` | requirement | A1 → K4 | `D05SD5QLG94/1759255800.418239` | 'anything they've asked us for in the channel that isn't on it' | R1 | — |
| K5 | linear · `ART-793` | destination | A1 → K1 → K5 | `f_8c1d0bca1d1d5fde4c5008` | 'Tickets live under the pack ticket, one per line' | R6 | — |
| K6 | confluence · `page_zm3d_gdd` | requirement | A1 → K1 → K6 | `f_8c1d0bca1d1d5fde4c5008` | 'How the level plays is on the design page' | R5 | — |
| K7 | gcal · `evt_421695d009e589ee85296c` | recipient | A1 → K1 → K7 | `f_8c1d0bca1d1d5fde4c5008` | 'Everyone on the kickoff hold' | R7 | H3 |
| K8 | contacts · `d7d31caf63ee33db2b7ed271` | recipient | A1 → K1 → K8 | `f_8c1d0bca1d1d5fde4c5008` | 'their intake address, which is in Contacts' | R7 | — |
| K9 | gslides · `f_6a2fa8e61b31139ca8e3d4` | requirement | A1 → K1 → K9 | `f_8c1d0bca1d1d5fde4c5008` | 'your reference-level deck has the layout' | R5 | — |
| K10 | slack · `C090N54TG79/1759167000.736119` | requirement | A1 → K10 | `D05SD5QLG94/1759255800.418239` | 'Robert's picks for the board and the zombies stand' | R5 | — |
| K11 | slack · `C08R8CHB0QL/1758904025.123869` | amendment | A1 → K11 | `D05SD5QLG94/1759255800.418239` | 'unless he's changed them since' | R4 | — |
| K12 | slack · `C08H78VJG80/1757695108.506159` | format | A1 → K1 → K12 | `f_8c1d0bca1d1d5fde4c5008` | 'What they told us about formats in the channel still holds' | R2, R5 | — |
| K15 | slack · `C08R8CHB0QL/1758904025.123869` | requirement | A1 → K1 → K15 | `f_8c1d0bca1d1d5fde4c5008` | 'If Robert has added objects since Brian made the list, they go on it too' | R1 | — |
| K13 | slack · `C08H78VJG80/1744637266.363689` | requirement | A1 → K1 → K13 | `f_8c1d0bca1d1d5fde4c5008` | 'so does what they told us about sound last time' | R5 | — |
| K14 | slack · `C08H78VJG80/1759226395.551469` | requirement | A2 → K14 | `C08H78VJG80` | 'We’re planning the new start date for the game on November 3rd' | R5 | — |

15 fragments over 8 services and 14 containers. **Amendment:** K11, Robert's 26 Sep reply, in another channel and three days after K3; it changes one clause (the iron) and the ask keeps his latest word ('unless he's changed them since'); nothing later re-asserts the iron. **Non-authoritative instruction distractors:** Julia's own grenades-and-shuriken idea (T13), Frederick's three-object 'good start' (T18), the March FBX rule from the first playable (T12), Leonard's card (T11).


## 5 Chains and trap register

**Chains** (six, six distinct root causes):

| Chain | Root cause | Hops (service: record — finding) | Ends in |
|---|---|---|---|
| C1 | A24 | gsheets: `f_956e60ec7f2f7977d98934` — twelve appliance and furniture lines are on the list with no delivery (extras)<br>linear: `ART-806` — Brian's note: model file exported from the object browser, all twelve in one go, 25 Sep, in the outgoing folder; ticket Done<br>slack: `C08R27X0EAH/1758963900.284719` — Arthur, 27 Sep: the browser's new multi-select button writes an empty shell per object; redo by hand anything pushed out with it | R2 |
| C2 | A11 | gsheets: `f_956e60ec7f2f7977d98934` — twelve lines carry the set Bathroom<br>linear: `ART-819` — Brian's note: exported 25 Sep; Claire's earlier note: fine to go<br>slack: `D05HMBQUC8Z/1758874200.613049` — Claire, 26 Sep, to Julia: redoing the UVs on the bathroom ones; what Brian pulled on Thursday is the old unwrap; nothing goes until she says | R3 |
| C3 | A1 | gsheets: `f_956e60ec7f2f7977d98934` — Cactus Plant, Chainsaw and Traffic Cone went in the 24 Sep zip; Dartboard and Candy were exported on the morning of 25 Sep<br>slack: `C08R8CHB0QL/1758808937.107229` — Claire, 25 Sep 14:02 UTC: pushed the changes Robert asked for (cactus, candy, cone, dartboard) in a new pull request<br>github: `harmonygames-Games/match3d#462` — 'Objects Revisions and Changes' merged 25 Sep 23:15 UTC: the art of five sent or exported lines changed afterwards<br>gdocs: `f_8c1d0bca1d1d5fde4c5008` — if the art changed after a file went out, it goes again | R2 |
| C4 | A14 | slack: `C090N54TG79/1758646800.552319` — Robert, 23 Sep: the eight board objects, the iron among them<br>gslides: `f_6a2fa8e61b31139ca8e3d4` — Julia's deck shows the level as built that day, with the iron<br>slack: `C08R8CHB0QL/1758906300.447189` — Robert, 26 Sep, under Julia's bow post in #zombie-art: the bow goes on the board instead of the iron; six round objects are missing from Brian's list | R4 |
| C5 | A13 | linear: `ART-884` — Brian's note: .wav exported, in the outgoing folder<br>gdocs: `f_8c1d0bca1d1d5fde4c5008` — only sound we own outright leaves the studio<br>gsheets: `f_b2387e31d46d3a7b3fa2a9` — Calvin's source sheet: the match scale and the explosion are cut from a bought pack, in-game licence only | R2 |
| C6 | A3 | gsheets: `f_956e60ec7f2f7977d98934` — eight lines carry the set Music<br>linear: `ART-832` — Brian's note: exported .glb, Fri 26 Sep, in the outgoing folder; ticket Done<br>linear: `cmt_8b590c43980032fc5d02` — Brian, 29 Sep, on the pack ticket itself: the music set from Friday's export comes in grey in an empty scene; needs another pass | R3 |

**Trap register:**

| Trap | Family | Services | Records | Req. | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|---|
| T1 | done_gap | gsheets, linear, slack | `f_956e60ec7f2f7977d98934`, `ART-806`, `C08R27X0EAH/1758963900.284719` | R2 | the twelve appliance and furniture lines are Ready: each ticket is Done and says the model file is exported and in the outgoing folder | Arthur's 27 Sep post in #zombie-bugs: the object browser's new multi-select button writes an empty shell per object; the twelve were exported in one go on 25 Sep, so each is Owed (re-export one at a time, Brian) | the pack list and each ticket's comments are read while building the list; the post sits in a channel the ask never names and uses none of the ask's words |
| T2 | superseding | linear, slack | `ART-819`, `D05HMBQUC8Z/1758874200.613049` | R3 | the twelve bathroom lines are Ready: exported 25 Sep, and Claire's ticket note says the art is fine to go | Claire's 26 Sep DM to Julia: she is redoing the UVs on the bathroom ones and what Brian pulled on Thursday is the old unwrap, so each is Owed (art, Claire) | Claire's ticket note (24 Sep) is on every bathroom ticket; her DM is a day and a half later, in a direct message that names no object and no ticket |
| T3 | effective_date | gsheets, slack, github | `f_956e60ec7f2f7977d98934`, `C08H78VJG80/1758717576.077489`, `C08R8CHB0QL/1758808937.107229`, `harmonygames-Games/match3d#462` | R2 | Cactus Plant, Chainsaw and Traffic Cone are Delivered (in the 24 Sep zip) and Dartboard and Candy are Ready (exported 25 Sep) | base: Robert asked for changes on the evening of 24 Sep, Claire pushed them on 25 Sep and match3d#462 merged at 23:15 UTC; the notes send a file again when the art changed after it went out, so all five are Owed | the delivery column is the first thing read for these lines; the change is in #zombie-art and GitHub, a day after the zip |
| T4 | authority | gdocs, gsheets, linear | `f_8c1d0bca1d1d5fde4c5008`, `f_b2387e31d46d3a7b3fa2a9`, `ART-884`, `ART-885` | R2 | all five exported sound cues are Ready (.wav, a format PlayableX takes) | the notes let only sound we own outright leave; Calvin's source sheet marks the match scale and the explosion as cut from a bought pack with an in-game licence, so both are Owed (Calvin) | format is the visible test and all five pass it; the source of each cue is in a sheet no ticket links |
| T5 | superseding | slack | `C090N54TG79/1758646800.552319`, `C08R8CHB0QL/1758906300.447189`, `C08R8CHB0QL/1758904025.123869` | R4 | the default eight are Robert's 23 Sep picks, the iron among them | Robert's 26 Sep reply under Julia's bow post in #zombie-art: the bow goes on the board instead of the iron | the picks are a root post in #zombie-design, found by searching for Robert's picks; the reply is in another channel under a post about an arrow |
| T6 | exact_predicate | gsheets, slack, linear | `f_956e60ec7f2f7977d98934`, `C08R8CHB0QL/1758906300.447189` | R1 | the list is the 97 rows of Brian's pack list | the ask adds anything Robert added that is not on it; his 26 Sep reply names six round objects missing from Brian's list, so the list has 103 lines and six new tickets | the pack list presents itself as complete; the six are named only in the same reply as the swap |
| T7 | tool_surface | linear, gsheets | `cmt_8b590c43980032fc5d02`, `ART-832` | R3 | the eight music lines are Ready: each ticket is Done and says exported .glb on 26 Sep | Brian's 29 Sep comment on the pack ticket itself: the music set from Friday's export comes in grey in an empty scene and needs another pass, so each is Owed (Brian) | the children's comments are read line by line; the pack ticket's own comments are returned only by a comment read on the parent |
| T8 | superseding | slack | `C08H78VJG80/1758022459.227279`, `C08H78VJG80/1758701898.919999`, `C08H78VJG80/1759226395.551469` | R5 | the start is 29 September, or 6 October | base: the vendor's 30 Sep message sets 3 November | — |
| T9 | distractor (withdrawn_ask) | confluence | `confluence:page_zm3d_gdd`, `confluence:comment_zm3d_gdd_c1`, `confluence:comment_zm3d_gdd_c2` | R5 | the tray has six slots (Julia's July proposal in the design page comments) | base: Robert's reply keeps the page at seven; the page body says a 7-slot tray | — |
| T10 | completion_elsewhere (already_done) | slack, linear | `ART-872`, `C08H78VJG80/1758808234.045839`, `C08H78VJG80/1758906043.375719` | R6 | the zombie lines are Owed because PlayableX said the first package was not exported correctly | base: Brian sent the full Unity pack on 26 Sep and PlayableX reviewed it on 29 Sep; the four lines are Delivered and their tickets are not touched | the 25 Sep complaint is met before the 26 Sep pack when the thread is read in order |
| T11 | near_miss_mention (scope_adjacent) | trello, gcal | `68dc207c75aff34acf5a5424`, `evt_421695d009e589ee85296c`, `trello:688c4d14c312a27fa2747e40` | R7 | the kickoff is Leonard's card, so the brief goes to Leonard | the notes name the kickoff hold: its attendees are Frederick, Julia, Brian and Robert | a search for the kickoff returns the Trello card by its title before the calendar hold |
| T12 | distractor (other_title) | slack | `C08H78VJG80/1742892985.601399` | R5 | everything must be FBX (the March rule from the Domino Delights round) | base: for this playable the vendor takes .fbx, .glb or .blend for 3D (16 and 19 Sep) | — |
| T13 | distractor (non_authoritative_instruction) | slack | `C090N54TG79/1758569824.148029`, `C090N54TG79/1758569885.985319` | R4 | a board of grenades and shuriken (Julia's own 22 Sep idea) | base: Robert answered 'remain as is'; his picks are the board | — |
| T14 | distractor (stale_summary) | trello | `trello:67bdf36fa1136aff58740a55` | R5 | playables are 'Not Started' (the UA/BD board card, untouched since March) | the channel record: scenario chosen, assets sent, start set for 3 November | — |
| T15 | mutable_pointer | gslides, slack | `f_6a2fa8e61b31139ca8e3d4`, `C08R8CHB0QL/1758906300.447189` | R4 | the default eight are the eight objects on Julia's deck (the level as built on 23 Sep) | the deck shows the layout; Robert's later reply changes one object | the notes send the reader to the deck for the layout, where the eight are listed |
| T16 | scope_alias | slack, gsheets | `f_956e60ec7f2f7977d98934`, `C08H78VJG80/1758723504.085039`, `C08H78VJG80/1758729487.922339`, `C08H78VJG80/1758283671.878269` | R1 | PlayableX's 'duck asset' and 'rocket launcher' are lines missing from the list | base: the duck is the plushie Brian sent the same day (Plushie-and-zombies.zip); the launcher is the cannon line | — |
| T18 | distractor (partial_listing) | slack | `C08H78VJG80/1757956024.883249` | R4 | the board is grenade, couch and plush doll (Frederick's 15 Sep suggestion 'would be a good start') | that message names three objects as a start; Robert's picks list the eight | — |
| T19 | distractor (keyword_collision) | slack | `C090N54TG79/1756730298.517369` | R1 | objects 'removed from the pool' (1 Sep) are lines to drop from the list | base: that message is about the card pool in the game's progression, not the pack; the list is Brian's rows plus Robert's six | — |
| T17 | distractor (lookalike_entity) | gdocs | `gdocs:f_05bedd1540d3e01a90ab16` | R2 | Leonard's Playable Feedback (P0, P1, P2) is the rule for what is ready | that doc is feedback on the Domino Delights playable; the notes for this one are Frederick's | — |

Supersession chronology (oldest first, timestamps from the records): T2 `cmt_5570d67a5cbb499daea7` 2025-09-24T09:20Z → `D05HMBQUC8Z/1758874200.613049` 2025-09-26T08:10Z; T3 `C08H78VJG80/1758717576.077489` 2025-09-24T12:39Z → `harmonygames-Games/match3d#462` created 2025-09-25T11:43Z, merged 23:15Z; T5 `C090N54TG79/1758646800.552319` 2025-09-23T17:00Z → `C08R8CHB0QL/1758906300.447189` 2025-09-26T17:05Z; T8 `C08H78VJG80/1758022459.227279` 2025-09-16 → `C08H78VJG80/1758701898.919999` 2025-09-24 → `C08H78VJG80/1759226395.551469` 2025-09-30 (three versions); T15 `f_6a2fa8e61b31139ca8e3d4` 2025-09-23T19:50Z → `C08R8CHB0QL/1758906300.447189`. Every seeded timestamp is before the seed bound; the only later value is the plan field of the hold (start 2025-11-03T17:00Z).

**Hardness v2 trap selection.** Two separate cross-source decisions carry the difficulty, each naming the convincing wrong source and the record that beats it: (1) trap 1, proving done across services — EXPORT: the ticket (Brian, 25 Sep, Done, 'exported, in the outgoing folder') against Arthur's 27 Sep post in #zombie-bugs (he wrote the export button; later; another service); (2) trap 2, a correction somewhere else — ARTHOLD: Claire's own 24 Sep ticket note against her 26 Sep DM (same person, later, another service). Four more are used: trap 4 dates (REVISED, base), trap 5 a rule in the data (AUDIO), traps 2 and 7 (PICKS: a later reply and six lines outside the list), trap 9 work already done (T10: the zombie pack; graded as an exact count of tickets moved, never a 'leaves alone' row). No correction sits in the superseded record's container, in an anchor's container or on a delegation path (`hardness_v2_check` SAME_PLACE clean below). Volume and arithmetic carry no difficulty.

### Mechanism portfolio (S5a)

Candidates considered (grounded in the census files) and the selection:

| # | Candidate | Coupling | Verdict | Reason (record) |
|---|---|---|---|---|
| 1 | EXPORT: a multi-select export writes empty shells | ticket 'exported' → file unusable → Owed + re-export | selected | base precedent of a bad package: `C08H78VJG80/1758808234.045839`; survives complete retrieval as a join (ticket note 'all twelve in one go' × the post) |
| 2 | ARTHOLD: the artist withdraws her own 'fine to go' | ticket note → DM → Owed (art) | selected | Claire makes every board object (census B §D: match3d#412 … #462) and is not in the vendor channel (`C08H78VJG80` members) |
| 3 | REVISED: art changed the day after the zip | delivery date → pull request → Owed | selected | all base: `C08R8CHB0QL/1758752145.583769`, `C08R8CHB0QL/1758752921.740419`, `C08R8CHB0QL/1758754866.994649`, `C08R8CHB0QL/1758754916.837729`, `C08R8CHB0QL/1758808937.107229`, `harmonygames-Games/match3d#462`, `C090N54TG79/1759189466.554739` |
| 4 | AUDIO: only owned sound leaves | file type passes → source sheet → Owed | selected | base is silent on sound ownership (census A §E); the cue names come from base (`C09A7PDFYCV/1755541416.578719`) |
| 5 | PICKS: Robert changes a pick and adds lines in a reply elsewhere | picks → reply → board and list | selected | parent `C08R8CHB0QL/1758904025.123869` is Julia's own base post about the bow |
| 6 | PARENT: the export failure of a set noted on the pack ticket | children Done → parent comment → Owed | selected | `linear_get_issue` returns no comments (Ask_Carriers §6b); planned on ART-793, base precedent ART-792 |
| 7 | objects stripped from the beta build | tracker 'in build' → build content | rejected | base contradicts it: no addressables for objects (`C08R27X0EAH/1758905363.341129`) |
| 8 | item effects as shipped (a design line per object) | ticket text → pull request review | rejected | effects are spread over dozens of base messages in #zombie-design `C090N54TG79` and data files (census A §A2); any seeded effect risks a base contradiction; an inline review also needs a real diff hunk (learnings: Calvin) |
| 9 | which enemies have full animation sets | enemy set → animations channel | rejected | card SC-58: the monster roster on `page_zm3d_gdd` is a known conflict; the four zombies are fixed by one seeded answer `C090N54TG79/1759167000.736119` and one light row |
| 10 | a due date on a calendar hold against 'a week before' | rule arithmetic → hold | rejected | two fair dates with no resolving record: a UGT fork; the hold `evt_421695d009e589ee85296c` is kept only for its attendees |
| 11 | vendor labels as an alias for lines | acceptance note → label map | rejected | the note would sit in the hub channel `C08H78VJG80` that every run reads to the end; the map would be the whole trap |
| 12 | interface art changed by match3d#471 | sent UI → later pull request | rejected | 'UI polishes' does not say which pieces: a fork |
| 13 | a brief that is valid under each pivot option | pivot options → brief | rejected | the options are undecided in base (`C090N54TG79/1758517286.431379`): no truth value |
| 14 | lines defined by level number ('by level 40') | level export → list | rejected | level content at the clock is in repository files the tools do not read; the July export `f_7efae6c05be5c2414e8798` is stale and its readability for Julia is not proven |

**Selected rules** (one per solver rule; draft manifest `mechanism_portfolio`). Ledger priors for `claude-opus-5-5`, UNCALIBRATED (`hardness_ledger.py priors`; `plan/out/ledger_priors.txt`):

| Rule | Mechanism | Prior family · prior · record ids | Natural reading | Decides | Control · over-application | Stays hard after complete retrieval | Natural call that returns the decider | Slots it flips |
|---|---|---|---|---|---|---|---|---|
| EXPORT | A24 | done_gap · Beta(1.0, 2.86) mean 0.26 · `hev_7af7471ca0d3855f`, `hev_bdb9590893044914`, `hev_e30a8c13fa044076` | the twelve are Ready | State, What's owed, Who has it | Rolling Pin (exported on its own) · export_over | joining 'all twelve in one go' on the ticket to a post that names no object | `slack_read_channel` or a search of #zombie-bugs → `C08R27X0EAH/1758963900.284719` | X1, X6, X16, W4, A1, A2, W1, W2 |
| ARTHOLD | A11 | superseding · Beta(2.57, 1.29) mean 0.67 · `hev_d4e1db2db22b1a55`, `hev_a9c69a91cf1cefd0`, `hev_01debb8fc63f4c1e` | the twelve are Ready | State, What's owed, Who has it | Armchair (Claire's note stands) · art_over | mapping 'the bathroom ones' to the list's set | reading Julia's DM with Claire → `D05HMBQUC8Z/1758874200.613049` | X2, X7, X11, W5, A1, A2, W1, W2 |
| REVISED | A1 | stale_summary · Beta(1.0, 2.85) mean 0.26 · `hev_5ad302a3d2e2ed5b`, `hev_6aa0e2dc797c1a41`, `hev_8c277ed5dc029ed7` | three Delivered, two Ready | State, What's owed | Grenade (in the same zip, unchanged) · revised_over | comparing each line's send or export time with 25 Sep 23:15 UTC | `github_list_pull_requests` then the file list of `harmonygames-Games/match3d#462`; or #zombie-art | X3, X8, W6, A1, A2, A3, W1, W2, W3 |
| AUDIO | A13 | authority · Beta(1.0, 2.86) mean 0.26 · `hev_c4bbc05b4e9b08ea`, `hev_923eb1fef7d8dc20`, `hev_0eec4f03fda7d5a4` | all five exported cues are Ready | State, What's owed, Who has it | Win stinger (made here) · audio_over | applying an ownership rule to a source column | a Drive search for the sound sheet, then its rows → `f_b2387e31d46d3a7b3fa2a9` | X5, X10, X12, W8, B6, A1, A2, W1, W2 |
| PICKS | A14 | superseding · same prior and records as ARTHOLD | iron in the eight; 97 lines | Board set, Line | Grenade (unchanged pick) · picks_over | the latest word wins; six lines need tickets | `slack_read_thread` on Julia's bow post `C08R8CHB0QL/1758904025.123869`, or a search for the iron → `C08R8CHB0QL/1758906300.447189` | X13, X14, X15, V1, B1, W10, W11, A1, W1 |
| PARENT | A3 | tool_surface · Beta(1,1), no ledger record: UNPARAMETERIZED | the eight are Ready | State, What's owed, Who has it | Record Player (exported on its own, 25 Sep) · parent_over | mapping 'the music set from Friday's export' to eight lines | `linear_list_comments` on ART-793 → `cmt_8b590c43980032fc5d02` | X4, X9, W7, A1, A2, W1, W2 |

A5b checks per rule: **incorporated** — each state follows from the notes (K1) applied to records Julia can read; **survives complete retrieval** — each needs a join after the record is found (set or export method → lines); **tool-surface proof** — every decider is a top-level message, a ticket comment, a sheet or a base pull request that the named call returns (no DM thread reply, no attachment body, no result that depends on a search missing); **graded weight** — each flips at least one weight-5 slot. No liveness flag is resolved by removing an incorporation link.

### Liveness flags (S5b)

`trap_liveness.py --design` (advisory, UNCALIBRATED; `plan/out/trap_liveness.txt`) raises one kind of flag, `breadcrumb`, on eleven traps. Dispositions:

| Trap | Flag | Disposition |
|---|---|---|
| T4 | breadcrumb | the notes `f_8c1d0bca1d1d5fde4c5008` carry the sound rule, as they must for incorporation; they do not name Calvin's sheet `f_b2387e31d46d3a7b3fa2a9`, its title or its owner. Kept. |
| T5, T6, T15 | breadcrumb | the ask `D05SD5QLG94/1759255800.418239` says 'unless he's changed them since': it authorises a later change and gives no place, date or word of it. The reply is under a post about an arrow in another channel. Kept; the wording sweep on the SQL checks that the reply shares no rare word with the ask. |
| T8 | breadcrumb | all three dates are in the channel the ask names (`C08H78VJG80`); this is a realism trap with no budget weight. |
| T12, T13, T16, T17, T18, T19 | breadcrumb | distractors on the read path by design (`C08H78VJG80`, `C090N54TG79`); none carries budget weight. |

`hardness_v2_check.py --design` (verbatim):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      5 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 3 requirements: {'R2': ['EXPORT', 'REVISED', 'AUDIO'], 'R3': ['ARTHOLD', 'PARENT'], 'R4': ['PICKS']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   6 of 6 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Dispositions: no FLAG and no UNRESOLVED. SAME_PLACE is clean over five version chains; it is re-run on the SQL. INPUT_CHECK reports no weight-5 total: the three counts are weight 3 (calculation) and each is moved by at least one rule, so none is plain arithmetic on clean inputs. RULE_IN_PROMPT runs when the prompt exists.


## 6 Failure-diversity plan

Each unit is one deciding record behind its own retrieval habit, so a run's misses are a subset of six independent records. Budget table (`difficulty_budget.py table`, weights from the rubric skeleton `01_Rubric_Skeleton.json`, the rows the portal's rules force):

| Unit | Role | Carrier | Decider | Habit | Find rate | Rows (weight) | Weight share |
|---|---|---|---|---|---|---|---|
| A1 | anchor | de_named_root_record | slack C08R27X0EAH/1758963900.284719 (injected) | slack / read_channel | 0.05-0.20 | S1 (5), S6 (5), S15 (5), S28 (3), S47 (3), S48 (3), S49 (3), S50 (3), S51 (3), S52 (3), S53 (3), S54 (3), S55 (3), S56 (3), S57 (3), S58 (3) | 16.6% (54 of 326) |
| A2 | anchor | dm_with_non_owner | slack D05HMBQUC8Z/1758874200.613049 (injected) | slack / read_dm | 0.05-0.20 | S2 (5), S7 (5), S11 (5), S29 (3), S59 (3), S60 (3), S61 (3), S62 (3), S63 (3), S64 (3), S65 (3), S66 (3), S67 (3), S68 (3), S69 (3), S70 (3) | 16.6% (54 of 326) |
| C1 | variance | outside_obvious_filter | github harmonygames-Games/match3d#462 (base) | github / get_pull_request_files | 0.35-0.60 | S3 (5), S8 (5), S24 (3), S27 (3), S30 (3), S71 (3), S72 (3), S73 (3), S74 (3), S75 (3) | 10.4% (34 of 326) |
| C2 | variance | second_carrier_by_rule_owner | gsheets f_b2387e31d46d3a7b3fa2a9 (injected) | gsheets / values_get | 0.35-0.65 | S5 (5), S10 (5), S12 (5), S32 (3), S42 (5), S76 (3), S77 (3) | 8.9% (29 of 326) |
| C3 | variance | reply_under_unrelated_parent | slack C08R8CHB0QL/1758906300.447189 (injected) | slack / read_thread | 0.40-0.65 | S16 (5), S17 (5), S18 (5), S21 (5), S34 (5), S35 (5), S37 (5), S94 (3), S95 (3), S96 (3), S97 (3) | 14.4% (47 of 326) |
| C4 | variance | reply_under_related_root | linear cmt_8b590c43980032fc5d02 (injected) | linear / list_comments | 0.35-0.60 | S4 (5), S9 (5), S31 (3), S78 (3), S79 (3), S80 (3), S81 (3), S82 (3), S83 (3), S84 (3), S85 (3) | 11.3% (37 of 326) |
| R1 | realism | same_container_supersession | n/a | n/a | n/a | not counted | 0% (realism) |

Mode hard (cap 70.0%, loss 30.0%); weights from skeleton, total 326. Anchors: 33.1% of weight from 2 cause(s) (needs 32.0%). Coin-flip units: 45.1% of weight over 4 independent habit(s), 4 inside the find-rate window (needs 4).

`difficulty_budget.py check` (verbatim):

```
DIFFICULTY BUDGET (hard): WARN
[PASS] budget.schema: 7 units (2 anchor, 4 variance, 1 realism), design D1, revision D1-design.
[PASS] budget.context: mode hard is the assigned difficulty mode.
[PASS] budget.rows: Every row matches its basis. Weights and total come from 01_Rubric_Skeleton.json: 71 rows over 6 units, total weight 326. Realism units ignored: R1.
[PASS] budget.carriers: All 6 anchor and variance units use carriers that produced misses.
[PASS] budget.unit_rows: Each of the 6 anchor and variance units flips at least 2 rows, one of weight 5.
[PASS] budget.independence: 6 units, 6 independent habits; no two units share a habit.
[PASS] budget.anchors: 2 anchors from 2 causes carry 33.1% (needs 32.0%); largest cause 16.6%; highest find rate 0.20.
[PASS] budget.variance: 4 independent coin-flip habits, every find-rate range inside 0.35-0.65 (needs 4).
[PASS] budget.average: P(six-run average strictly under 70.0%) is 1.000 with every unit at its low find rate and 0.995 at its high find rate (needs 0.90 at both).
[PASS] budget.full_passes: P(fewer than 5 full passes) is 1.000 with every unit at its low find rate and 1.000 at its high find rate (needs 0.90 at both).
[PASS] budget.signature: P(largest signature at most 50% of failing runs, two or more signatures) is 0.991 with every unit at its low find rate and 0.997 at its high find rate (needs 0.90 at both).
[PASS] budget.signature_one_error: P(signature gate with 5 completed runs) is 0.943 with every unit at its low find rate and 0.981 at its high find rate (needs 0.90 at both).
[WARN] budget.spread: P(SD inside 0.1-0.3) is 0.549 / 0.689 / 0.730 at the low / middle / high find rates; the design carries 45.1% of weight on coin-flip (variance) units and 33.1% on anchors. Below 0.70: a spread miss is likely; move more weight onto coin-flip units (about 60% of weight reaches 0.8) or accept that the miss is reported.
[WARN] budget.hard_mode: Hard mode: the 30.0% loss figure is 1 - cap, not a line from a platform /hardness report, so the anchor share target is unverified.
```

`rubric_skeleton.py check` (verbatim):

```
RUBRIC SKELETON (check): PASS
[PASS] skeleton.present: Working_Files/01_Rubric_Skeleton.json: 98 rows
[PASS] skeleton.bound: bound to 3 current input file(s)
[PASS] skeleton.share: anchors 123 of 326 = 37.7% (needs 32.0%: hard loss 30.0% + margin 2.0%); coin-flip 45.1% (budget declared 45.1%); always-pass 17.2%
```

Whole policies and single misses on the skeleton, and the six-run simulation (`plan/policy_scores.py`, UNCALIBRATED; verbatim):

```
Rubric skeleton: 98 rows, total weight 326; budget basis skeleton  (UNCALIBRATED)

Whole policies:
  100.0 %  reads everything
   17.2 %  the ask, the notes, the pack list, the channel and every line's own ticket; nothing else
   27.6 %  that, plus pull requests and #zombie-art since the zip
   53.4 %  that, plus every thread Robert posted in and the pack ticket's own comments
   62.3 %  everything except the two anchor records
   50.3 %  both anchors found, every coin-flip record missed

Single misses (everything else found):
   78.8 %  miss A1 (EXPORT, de_named_root_record)
   78.8 %  miss A2 (ARTHOLD, dm_with_non_owner)
   85.0 %  miss C1 (REVISED, outside_obvious_filter)
   86.5 %  miss C2 (AUDIO, second_carrier_by_rule_owner)
   83.7 %  miss C3 (PICKS, reply_under_unrelated_parent)
   84.0 %  miss C4 (PARENT, reply_under_related_root)

Six-run simulation, 20,000 trials per setting:
  setting    E[avg]   P(avg<70)  P(<5 full)  P(SD band)  P(patterns)  P(ALL GATES)  mean SD
  low find    30.4 %   1.000      1.000       0.549       0.991        0.545       0.106
  midpoint    40.2 %   1.000      1.000       0.686       0.998        0.685       0.121
  high find   50.1 %   0.999      1.000       0.727       0.997        0.726       0.127

Targets: E[avg] <= 62 %, P(all gates) >= 0.5.
```

**Reading.** E[average] is 30–50 % and P(all gates) 0.55–0.73 at the budget's find-rate ranges; both targets (≤ 62 %, ≥ 0.5) hold at every setting. The printed spread chance is 0.549 / 0.689 / 0.730 (low / middle / high find rates): the spread gate is the binding one and the tool warns below 0.70. Reaching 0.8 would need about 60 % of the weight on coin-flip records on top of the anchors' 32 %; this design carries 45.1 %. A spread miss on a baseline that passes every other gate is reported to the owner (owner decision of 2026-11-10). No single miss clears the cap: a run that misses one record scores 79–87 %; the average holds only when runs miss several. The ledger-prior forecast (§12) gives a second, less favourable view.

**Which runs miss what.** A1 and A2 are found by few runs: neither record holds a word of the ask, an object name or a ticket key, and neither container is named by anything the run reads. C1 is found by runs that check what changed after the zip (a pull request list or #zombie-art after 24 Sep). C2 by runs that look for where the sound came from. C3 by runs that open Julia's bow thread or search for the iron. C4 by runs that read the pack ticket's own comments. The six habits are different calls in five services, so two runs rarely share a signature. No single discovery decides more than 16.6 % of the weight.

**Lessons applied** (`00_Pre_Scenario_Analysis.md` §9b; Frederick's rev10 forensics, `task_inputs-uselater/Working_Files/01a_Hardening_Report.md` §8): in twelve runs a broad Slack search on the task's key noun returned every correction that held it. Here no deciding record contains 'playable', 'PlayableX', 'pack', 'brief', 'hand-off', 'asset', 'FBX' or 'vendor'; the SQL wording sweep at `/create-injection` enforces it. Inline review comments are not used (found by all or none). Every miss moves a count in one direction (Owed up, Ready or Delivered down), so misses cannot cancel in the reply.


## 7 Deliverables and dependent writes

| Write | Tool | Count | Depends on | Requirements |
|---|---|---|---|---|
| gsheets | `gsheets_create_spreadsheet+gsheets_values_update` | 2 | K1, K2, C1, C2, C3, C5, C6, T6 | R1, R2, R3, R7 |
| gdocs | `gdocs_create_document+gdocs_batch_update` | 2 | K3, K6, K9, K10, K12, K13, K14, C4 | R4, R5, R7 |
| linear | `linear_create_comment` | 48 | K1, K5, C1, C2, C3, C5, C6 | R6 |
| linear | `linear_update_issue` | 48 | K1, K5, C1, C2, C3, C5, C6 | R6 |
| linear | `linear_create_issue` | 6 | K5, K11, T6 | R1, R6 |
| gdrive | `gdrive_share_file` | 8 | K7, K8 | R7 |
| slack | `slack_send_message` | 2 | A1, A2, C1, C2, C3, C5, C6, T6 | R7 |

- **Hand-off list** (Google Sheet in Julia's Drive root `d_8140f09bf9f1b94cb8ee2d`): one row per line (103); columns line, kind, board set (Default / Extra / blank), state, what is owed, who has it, ticket. Totals 19 / 30 / 54.
- **Brief** (Google Doc in her Drive): Scenario 1; the default eight (Grenade, Couch, Plushie Chick, Bow, Shuriken, Cute Axe, Cactus Plant, Gift Box) and the extras; four zombies (Chef, Bike Kid, Boxer, Mayor) and walk as the primary animation; a 7-slot tray, the level is lost when the zombies take the player's health to zero and won when all are cleared; the file types the vendor takes; sound: only owned cues, music starts after the first click; start 3 November. Free-text parts are bounded: any wording that states these facts is accepted.
- **Tickets:** the 48 Owed lines that have a ticket go back to Todo (every line ticket starts Done) with a comment saying what is owed and who has it; the six added lines get a new ticket under ART-793 (reuse-versus-create: no line that has a ticket gets a second one). The 49 Delivered and Ready tickets are not touched: graded as the exact count of tickets moved (48), never as a 'leaves alone' row.
- **Shares:** both files, view only, to the three other attendees of the kickoff hold and to PlayableX's intake address (eight share calls).
- **Messages:** the three counts to Frederick in `D05SD5QLG94`; both links in `C08H78VJG80`.

Every write's content depends on findings (`depends_on`); none is a bolt-on. Each is asked for by the ask or the notes (trigger Julia owns), each target is hers to write: she owns both new files, is a member of both Slack conversations (`can-see` YES), and Linear writes are unscoped for an ART team member (`/team_memberships`: Julia is in ART).


## 8 Service role map

| Service | Role | Load-bearing fact or write | Carrier |
|---|---|---|---|
| slack | the ask (Frederick's DM), the PlayableX channel (what was asked for, sent and when), Robert's picks and his later reply, Arthur's object-browser post, Claire's DM; writes: the reply and the channel post | the ask, the default eight, two withdrawn 'done' states (24 lines) and both message destinations exist only in Slack | ● message text, thread replies, DMs |
| linear | the pack ticket ART-793 and its 97 children with their export and art notes; Brian's comment on the pack ticket; writes: Todo moves, comments, six new tickets | every line's export and art notes are only in its own ticket comments; the music set's failure is only on the pack ticket | ● description, state, parent; comments ● per §6b |
| gsheets | Brian's pack list (membership, set, delivery, ticket); Calvin's sound source sheet; write: the hand-off list | the list of lines and each line's set and delivery; which sound cues are ours | ● grid |
| gdocs | Frederick's hand-off notes (state definitions, current version, sound, tickets, sharing); write: the brief | the three states and the follow-through rule are defined only there | ● body_text |
| gdrive | Julia's Drive root (destination), file metadata and sharing; write: view-only shares | both deliverables are created there and shared from there | ● name, parents, sharing |
| gslides | Julia's reference-level deck (layout, the eight objects as built on 23 Sep, win and fail) | the level layout for the brief; its object list is the older version of the default eight | ● element text |
| gcal | Frederick's kickoff hold on 3 Nov (attendees) | who both files are shared with | ● summary, start, attendees |
| contacts | PlayableX's intake contact | the address both view links are shared with | ● email, job |
| github | base match3d#462 'Objects Revisions and Changes' (merged 25 Sep) | which sent objects changed after they went out | ● PR title, dates, files (base) |
| confluence | base design page (7-slot tray, loss only at zero health) and its comments | how the level plays, for the brief | ● page body, comments (base) |
| trello | Leonard's Playable Kickoff card with his 30 Sep note; the UA/BD 'Playables' card | confirms the parked state and who is sorting the pack; not a rule source | ● card, commentCard action |
| gmail | invitation mails for the kickoff hold in the attendees' mailboxes | companions of the hold; carry the same attendee list | ● invitation mails (companions) |
| snowflake | not used | none: nothing in the pack is measured in the warehouse, and Snowflake cannot be injected | — |

## 9 Call budget

| Phase | Service | Calls | Reason |
|---|---|---|---|
| discovery | slack | 9 | the ask in Frederick's DM; the PlayableX channel (two pages and its two long threads); the #zombie-design playable thread; Robert's picks and his answer on the zombies |
| discovery | gdocs | 2 | Frederick's hand-off notes; Leonard's Playable Feedback (rejected: the first playable) |
| discovery | gdrive | 3 | find the notes, the pack list and the deck shared with Julia; list her own root for the destination |
| discovery | gsheets | 2 | Brian's pack list: sheet metadata and its rows |
| discovery | gslides | 1 | Julia's reference-level deck (layout, win and fail) |
| discovery | confluence | 2 | the design page and its comments (tray size, how a level is lost) |
| discovery | gcal | 2 | find the kickoff hold and read its attendees |
| discovery | contacts | 1 | PlayableX's intake address |
| discovery | trello | 2 | the Playable Kickoff card and its comments (rejected as the recipient source) |
| enumeration | linear | 3 | the pack ticket and two pages of its 97 children (keys, states, assignees) |
| per-record | linear | 97 | each line's ticket comments: how and when it was exported, the art note, what is missing |
| reconciliation | linear | 1 | the pack ticket's own comments (Brian's note on the music set) |
| reconciliation | slack | 7 | #zombie-art since 23 Sep and Julia's bow thread; her DM with Claire; #zombie-bugs for the object browser; the sound channel |
| reconciliation | github | 3 | pull requests on match3d after 24 Sep by the object artist; #462 and its file list |
| reconciliation | gsheets | 2 | Calvin's sound source sheet: find it and read its rows |
| reads-before-writes | linear | 3 | team, states and users for the ticket writes |
| per-record | linear | 96 | each of the 48 Owed lines with a ticket: a state write (Done to Todo) and a comment saying what is owed and who has it |
| writes | linear | 6 | a new ticket under the pack ticket for each of the six lines Robert added |
| writes | gsheets | 2 | create the hand-off list in Julia's Drive and write its 103 rows |
| writes | gdocs | 2 | create the brief and write its text |
| writes | gdrive | 8 | share both files view-only with the three other people on the hold and PlayableX's intake address |
| writes | slack | 2 | the three counts to Frederick in his DM; both links in the PlayableX channel |
| read-back | gsheets | 1 | read the list back against the pack list's rows |
| read-back | linear | 1 | list the pack ticket's children to confirm the Todo set and the six new tickets |

Total 258 unconditional calls over 11 services; per-record 193; the largest share outside the per-record phase is 30 % (gate output, §12). No row is conditional on an unverified tool behaviour. **Golden-run rule:** a correct run needs the volume: 97 comment reads fill the state column, 48 comments and 40 state writes are the follow-through, six tickets are new. **Every-run floor:** a run that finds no hidden record still reads the 97 tickets' comments, because ticket state and the pack list say nothing about a line's state, and moves and comments the nine lines that are Owed on their own note: about 40 discovery and rule calls + 97 reads + 18 ticket writes + 16 for the two files, the shares and the messages ≈ 171 counted calls, over the requester's 130. If the pre-check comes in under 150 the design is revised before any baseline.


## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by | Evidence |
|---|---|---|---|---|
| How many lines | 103: Brian's 97 plus Robert's six | 97: the pack list as it stands | the notes: 'If Robert has added objects since Brian made the list, they go on it too'; Robert's reply names six and says they go over | `f_8c1d0bca1d1d5fde4c5008`, `C08R8CHB0QL/1758906300.447189` |
| Twelve lines exported in one go | Owed, re-export (Brian) | Ready: tickets Done, files in the outgoing folder | Arthur wrote the export button and says every file from a multi-select run is an empty shell; the notes require that a Ready file opens | `C08R27X0EAH/1758963900.284719` |
| Twelve bathroom lines | Owed, art (Claire) | Ready: Claire's own 24 Sep note says fine to go | the same person, later: she is redoing the UVs and what Brian pulled is the old unwrap; the notes require that nobody is changing it | `D05HMBQUC8Z/1758874200.613049` |
| Five lines changed on 25 Sep | Owed, send the current version | Delivered or Ready: new colour versions are additions, the file sent is unchanged | the notes name the case: 'a fix, a retexture, new colour versions', 'so they always hold what the game has' | `f_8c1d0bca1d1d5fde4c5008`, `harmonygames-Games/match3d#462`, `C090N54TG79/1759189466.554739` |
| Eight music lines | Owed, another export pass (Brian) | Ready: tickets Done, .glb is a type the vendor takes | Brian's own later comment: the set comes in grey and needs another pass before it goes | `cmt_8b590c43980032fc5d02` |
| Match scale and Explosion | Owed, a cue we own (Calvin) | Ready: .wav is a type the vendor takes | the notes: only what we own outright leaves; Calvin's sheet marks both as cut from a bought pack | `f_b2387e31d46d3a7b3fa2a9` |
| The default eight | with the bow, without the iron | with the iron (Robert's 23 Sep picks, Julia's deck) | Robert's own later reply; the ask keeps his latest word | `C08R8CHB0QL/1758906300.447189` |
| The four zombie lines | Delivered | Owed: the vendor said the package was not exported correctly | base: the full pack went on 26 Sep and the vendor reviewed it on 29 Sep | `C08H78VJG80/1758906043.375719`, `C08H78VJG80/1759140968.965099` |
| Tray size | seven slots | six (Julia's July proposal) | base: Robert's reply keeps the page at seven | `page_zm3d_gdd`, `confluence:comment_zm3d_gdd_c2` |
| Start date | 3 November | 6 October | base: the vendor's latest message | `C08H78VJG80/1759226395.551469` |
| Who the files are shared with | both files, view only: the three other attendees of the hold and the intake address | the brief only; or Leonard (his card is the 'kickoff') | the notes: 'Sharing: both files, view only', the kickoff hold and Contacts | `evt_421695d009e589ee85296c`, `d7d31caf63ee33db2b7ed271` |
| Where the counts go | Frederick's DM, as a message or a thread reply under his ask | the vendor channel | the ask: 'give me the three counts here'; both forms in the DM are accepted | `D05SD5QLG94/1759255800.418239` |
| Ticket follow-through on an Owed line | Todo plus a comment | a description edit, or a new ticket | the notes: 'goes back to Todo with a comment'; a new ticket only for a line without one | `f_8c1d0bca1d1d5fde4c5008` |
| Buttons | Owed (parts not separated), ticket back to Todo | Delivered: sent on the 24th | its own ticket note; the vendor takes 2D as PNG with parts separated | `ART-882`, `C08H78VJG80/1758283671.878269` |
| The plushie line | Delivered, one line | a missing 'duck' line | base: the vendor's duck is the plushie sent the same day | `C08H78VJG80/1758723504.085039`, `C08H78VJG80/1758729487.922339` |

No figure forks: no BOTH_FAIR_FIGURE is declared. Dates: every graded date has the same Pacific and UTC day (3 November 17:00 UTC is 09:00 PT).

### Reach table (load-bearing records)

Base records (`persona_view.py can-see julia_lawson …`, run by `plan/reach_table.py`):

| Service | Record | Verdict | Why it is load-bearing |
|---|---|---|---|
| slack | `C08H78VJG80/1758283671.878269` LB | YES | what PlayableX expects, by group (K4) |
| slack | `C08H78VJG80/1758022459.227279` LB | YES | formats; the 8-item set and extra items (K12) |
| slack | `C08H78VJG80/1759140968.965099` LB | YES | the question Robert's zombie picks answer (K10) |
| slack | `C08H78VJG80/1758723504.085039` LB | YES | the 'duck asset' (T16) |
| slack | `C08H78VJG80/1758717576.077489` LB | YES | the 24 Sep zip (T3 older version) |
| slack | `C08H78VJG80/1758729487.922339` LB | YES | the plushie zip the same day (T16) |
| slack | `C08H78VJG80/1758906043.375719` LB | YES | the full zombie pack, 26 Sep (T10) |
| slack | `C08H78VJG80/1758717625.209649` LB | YES | win and fail as told to PlayableX (R5) |
| slack | `C08H78VJG80/1758808234.045839` LB | YES | the 25 Sep complaint and the blank-scene request (T10, C4) |
| slack | `C08H78VJG80/1757956024.883249` LB | YES | Scenario 1 chosen (R5, T18) |
| slack | `C08H78VJG80/1759174925.309129` LB | YES | the pause |
| slack | `C08H78VJG80/1759226395.551469` LB | YES | start 3 November (K14) |
| slack | `C08H78VJG80/1758701898.919999` LB | YES | start 6 October (T8 older version) |
| slack | `C08H78VJG80/1744637266.363689` LB | YES | music starts after the first click (K13) |
| slack | `C08H78VJG80/1742892985.601399` LB | YES | the March FBX rule (T12) |
| slack | `C08H78VJG80/1741963515.221549` LB | YES | Julia's brief for the first playable (role remit) |
| slack | `C090N54TG79/1758568735.563539` LB | YES | Brian asks Julia for the reference level (role remit) |
| slack | `C090N54TG79/1758569824.148029` LB | YES | Julia's own idea (T13) |
| slack | `C090N54TG79/1758569885.985319` LB | YES | Robert: remain as is (T13) |
| slack | `C090N54TG79/1759189466.554739` LB | YES | new coloured cactus, chainsaw and cones, 29 Sep (C1) |
| slack | `C08R8CHB0QL/1758752145.583769` LB | YES | Robert asks for a recoloured cactus plant (C1) |
| slack | `C08R8CHB0QL/1758752921.740419` LB | YES | Candy texture issue (C1) |
| slack | `C08R8CHB0QL/1758754866.994649` LB | YES | recoloured cone (C1) |
| slack | `C08R8CHB0QL/1758754916.837729` LB | YES | dartboard colour (C1) |
| slack | `C08R8CHB0QL/1758808937.107229` LB | YES | Claire pushed the changes (C1) |
| slack | `C08R8CHB0QL/1758904025.123869` LB | YES | Julia's bow post, parent of Robert's reply (C3) |
| slack | `D05SD5QLG94` LB | YES | the DM the ask and the reply sit in |
| slack | `D05HMBQUC8Z` LB | YES | the DM Claire's message sits in |
| slack | `C08R27X0EAH` LB | YES | the channel Arthur's post sits in |
| slack | `C09A7PDFYCV` LB | YES | the sound channel (decoy for the source sheet) |
| gdocs | `f_05bedd1540d3e01a90ab16` LB | YES | Leonard's Playable Feedback (H1 decoy, T17) |
| gdrive | `d_8140f09bf9f1b94cb8ee2d` LB | YES | destination of both deliverables |
| github | `harmonygames-Games/match3d#462` LB | YES (unscoped service) | the 25 Sep art change (C1) |
| confluence | `page_zm3d_gdd` LB | YES (unscoped service) | tray size and how a level is lost (K6, T9) |
| trello | `688c4d14c312a27fa2747e40` LB | YES (unscoped service) | Leonard's card (H3 decoy, T11) |
| trello | `67bdf36fa1136aff58740a55` LB | YES (unscoped service) | UA/BD card, Not Started (T14) |

Planned records are checked at the injection gate (`persona_view.py check-sql`). Their planned access: the ask and Claire's message are in Julia's own DMs; the picks, the reply and Arthur's post are in channels she is a member of; the notes, the pack list, Calvin's sheet are shared with her and the deck is hers; the hold has her as an attendee; Linear, Trello and Contacts are unscoped. Records she cannot read are never load-bearing: `#executives`, the Leonard–Frederick–Brian group DM and the vendor's DM with Leonard are cited in §1 and §1a as whole-base consistency checks only, and the July export sheets (UNVERIFIED) are cited only as the source of object names.

### Feasibility, precedence, naturalness, grading devices

- **Feasibility.** Tools in `Evals/references/tools/catalog.json`: `gsheets_create_spreadsheet`, `gsheets_values_update`, `gdocs_create_document`, `gdocs_batch_update`, `gdrive_share_file`, `linear_update_issue`, `linear_create_comment`, `linear_create_issue`, `slack_send_message`. One sheet with one tab; no multi-tab creation is needed. The outside recipient has an authorised path: the notes name the intake address in Contacts and the sharing level (view only).
- **Explicit rules.** Multi-version evidence: the later record by the same or the owning person stands (ask, notes). What 'now' means: the game as it is today (ask). Each write's end state is in the notes. Every cross-reference postdates its target (Robert's reply after Julia's post; Brian's comment after his export; Arthur's post after the export).
- **Precedence.** Load-bearing facts sit only in ● carriers (Ask_Carriers §5 as amended by §6b): Slack text, Linear comments, Sheets grids, Docs body, Slides element text, calendar summary and attendees, Contacts email, base PR fields. Nothing load-bearing is in a calendar description, slide notes, a Drive `content_text` or a Slack file.
- **Prompt naturalness.** The human's trigger needs: Frederick's message as the starting point, that the job is all of it, the two deliverables and that they go in her Drive, the PlayableX channel. It must not carry: the three state words, any rule, any set or object name, any count, any ticket key, the channels of §5, or where the notes and the list live.
- **Grading devices.** Exact key set of the list (103); three totals; at most five samples per group (state, what is owed, who has it, board set, Todo moves) with a volume row; one row per comment target and per new ticket; the exclusion as an exact count (48 tickets moved to Todo). No graded count, format or limit that the ask or the notes do not state.

### Coherence rail

Every §1a row is dispositioned. Designed disagreements are dated human claims with a named later record: Brian's ticket notes (25–26 Sep) against Arthur's post (27 Sep) and his own comment (29 Sep); Claire's note (24 Sep) against her DM (26 Sep); Robert's picks (23 Sep) against his reply (26 Sep). No two system fields disagree: tickets stay Done until the run moves them, which is the task. Companions planned with each record are in §11. No seeded text names a git branch, a build number or a release; the one base artifact the plan relies on is match3d#462 (title, created and merged times, changed objects), cited as base states it. Ids follow the base schemes (§2, §11).


## 11 Record plan for /create-injection

| Key | Service | Id | At (UTC) | By | What |
|---|---|---|---|---|---|
| ask | slack | `D05SD5QLG94/1759255800.418239` | 2025-09-30T18:10:00Z | Frederick Stone | Frederick's DM to Julia: the job, its destinations, and the three things it starts from |
| notes | gdocs | `f_8c1d0bca1d1d5fde4c5008` | 2025-09-30T17:52:00Z | Frederick Stone | Frederick's hand-off notes (created 2025-09-26): what Delivered, Ready and Owed mean; current version; sound; tickets; sharing |
| tracker | gsheets | `f_956e60ec7f2f7977d98934` | 2025-09-26T15:20:00Z | Brian Foster | Brian's pack list (created 2025-09-23): one row per line, set, delivery, ticket; no state column |
| picks | slack | `C090N54TG79/1758646800.552319` | 2025-09-23T17:00:00Z | Robert | Robert's picks for the outside level: the eight board objects (root post in #zombie-design) |
| zpicks | slack | `C090N54TG79/1759167000.736119` | 2025-09-29T17:30:00Z | Robert | Robert's answer to the vendor's question: walk as the primary animation; Chef, Bike Kid, Boxer, Mayor |
| ticket_parent | linear | `ART-793` | 2025-09-19T16:30:00Z | Frederick Stone | pack ticket (Team Epic, assigned Brian); children ART-794 to ART-890, one per line |
| tickets | linear | `ART-794` … `ART-890` | 2025-09-23 to 2025-09-26 | Brian Foster (creator); notes by Brian, Claire, Calvin | one ticket per listed line, title = the line's name, parent ART-793, state Done (all 97, closed by Brian as he dealt with each); one note by Brian on each saying what he did, art notes on 31, raw facts only |
| deck | gslides | `f_6a2fa8e61b31139ca8e3d4` | 2025-09-23T19:50:00Z | Julia Lawson | Julia's reference-level deck: layout, the eight board objects as built, win and fail |
| hold | gcal | `evt_421695d009e589ee85296c` | 2025-09-30T17:40:00Z | Frederick Stone | kickoff hold Mon 3 Nov 2025 17:00 UTC; attendees Frederick, Julia, Brian, Robert (one row per calendar) |
| contact | contacts | `d7d31caf63ee33db2b7ed271` | 2025-09-19T16:40:00Z | Frederick Stone | PlayableX intake contact (outside partner): the address a view link is shared with |
| trello_note | trello | `68dc207c75aff34acf5a5424` | 2025-09-30T18:25:00Z | Leonard Hayes | Leonard's comment on his Playable Kickoff card: parked until 3 November, Frederick and Julia are sorting the brief and the pack |
| a1_post | slack | `C08R27X0EAH/1758963900.284719` | 2025-09-27T09:05:00Z | Arthur Blake | A1: root post in #zombie-bugs: the object browser's new multi-select button writes empty shells; single export is fine |
| a2_dm | slack | `D05HMBQUC8Z/1758874200.613049` | 2025-09-26T08:10:00Z | Claire Morgan | A2: Claire's DM to Julia: she is redoing the UVs on the bathroom ones; what Brian pulled on Thursday is the old unwrap |
| c3_reply | slack | `C08R8CHB0QL/1758906300.447189` | 2025-09-26T17:05:00Z | Robert | C3: Robert's reply under Julia's bow thread: the bow replaces the iron on the board; six round objects are missing from Brian's list |
| c4_comment | linear | `cmt_8b590c43980032fc5d02` | 2025-09-29T08:40:00Z | Brian Foster | C4: Brian's comment on the pack ticket ART-793: the music set from Friday's export comes in grey in an empty scene |
| c2_sheet | gsheets | `f_b2387e31d46d3a7b3fa2a9` | 2025-09-26T13:30:00Z | Calvin Price | C2: Calvin's sound source sheet: where each cue came from (made here / bought pack, in-game licence only) |

Planned wording of the ask and the notes: `plan/planned_texts.py`. Per-line ticket notes by class (`plan/design_model.py`): Delivered — 'In the zip that went over on the 24th'; Ready — 'Exported on its own', with the date and file type; EXPORT — 'Exported, all twelve in one go, 25 Sep'; Bathroom — Claire's 'fine to go' (24 Sep) then Brian's export note (25 Sep); Music — 'Exported as .glb, Fri 26 Sep'; sound — 'Exported .wav'; visible Owed — what is missing. Haystack: routine traffic around each deciding record is base (#zombie-bugs 3,830 messages, Julia's DM with Claire 2,687, #zombie-art 2,650); `path_exposure.py` at injection decides whether more is needed. Size about 330 rows over ten schemas (slack, linear, gsheets, gdocs, gdrive, gslides, gcal, gmail, trello, contacts); Snowflake and Confluence are not injected.

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| slack | INT-13 (Drive app DMs), INT-04 (Linear app posts) | share and ticket notifications | none seeded: base has no Linear-app post for ART tickets (ART-790, ART-792 have none) and the shares are covered by mail (INT-11 pattern below); thread counters of Julia's bow post are updated |
| linear | INT-04, INT-05 | Slack posts, e-mail digests | none: ART tickets created outside Slack have no bot post in base; digests are not per ticket |
| gcal | INT-11 | invitation mails | seeded: one event row per attendee calendar (same `ical_uid`) and one invitation mail per attendee mailbox |
| gmail | INT-11, INT-22 | the invitation mails themselves | seeded as companions only; no deciding fact in mail (Gmail is THIN for the persona) |
| gdrive, gdocs, gsheets, gslides | INT-13 | Drive rows mirror Docs, Sheets and Slides ids and sharing | seeded: one `drive_files` row per file with identical sharing; Julia owns the deck |
| trello | INT-21 | none exists | trello: none — the card's and the board's dateLastActivity move with the comment |
| contacts | — | none | contacts: none — a single row in the base shape (15 fields) |
| github | INT-01, INT-03 | Slack mirror, linear[bot] | github: none — nothing is seeded in GitHub; match3d#462 is base and has no comments to mirror |

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
  [ok] cohort_size: cohort 103; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 2 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 195; need ≥ 110
  [ok] call_budget: unconditional (verified) floor 258 of 258 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 220 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 11 services in budget; largest share outside the per-record phase 28% (≤ 50%)
  [ok] traps: 19 traps across 11 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 7 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (2 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 7 distractors of 7 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 10 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 6 chains with 6 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 6 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 9 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 7 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 7 writes over 5 services; each must depend on findings
  [note] volume_exception: call-budget floor 220 and per-record floor 110 replace 500 and 300; every other extreme target applies — reason: the cohort is the 103 lines of one playable pack; honest necessary calls are abo; requester confirmation: task author in chat on 2026-11-11: '220 calls are good with required failure'; a
```

`gradable_surface.py validate` and `gradeable-report` (verbatim):

```
GRADABLE SURFACE (01_Gradable_Surface.json): PASS · 46 slots · weight 172 · mechanism share 82.0% (reported, not gated) · weight by class {'direct': 67, 'write_content': 87, 'delivery': 9, 'aggregate': 9}
SURFACE.GRADEABLE PASS · 46 slot(s) · {'GRADABLE': 46}
```

Id collision check (`plan/check_ids.py`, `hg.py search lookup`; verbatim):

```
linear issues    ids  98 hits 0 scan_complete=True 
linear comments  ids   2 hits 0 scan_complete=True 
drive files      ids   4 hits 0 scan_complete=True 
gcal events      ids   1 hits 0 scan_complete=True 
trello actions   ids   1 hits 0 scan_complete=True 
contacts         ids   1 hits 0 scan_complete=True 
slack message ids ids   6 hits 0 scan_complete=True 
minted slack: {'D05SD5QLG94/1759255800.418239': 'a4b3397282fff1683ae177c7dab2cfc1', 'C090N54TG79/1758646800.552319': '5740590664f6513d2faae02349105f8c', 'C090N54TG79/1759167000.736119': 'bf092c7d148cb
```

**Lazy-solver pass.** An agent that makes one broad search per service, reads first hits, opens no thread, stops at the first conclusion and uses every bulk call: it finds the ask, the notes, the pack list and the vendor channel's last page; lists the 97 children with descriptions in two calls; reads no comments. It scores the delivery rows and the brief rows that come from the hub (scenario, start date), about 9 % of the skeleton weight; it cannot fill the state column, because no bulk call returns a ticket's notes. Leaks looked for and closed: the pack list has no state or note column; every line ticket has the same workflow state (Done), so state is no proxy for Ready or Owed (an earlier draft left the nine self-stated Owed tickets in Todo: closed); ticket descriptions carry the line's name and kind only; no ticket title or label marks a class; the notes name no deciding record.

**Literal-value sweep and wording sweep** (base, by search; the SQL repeats both): 'empty shell', 'old unwrap', 'bought pack', 'comes in grey' and 'instead of the iron' have no base hit in any service; none of the six deciding records is planned with a word of the rule it triggers ('opens', 'current version', 'changing', 'own outright', 'picks').

**'The rest stands' check.** Robert's reply changes one object; no later planned record re-lists the eight. The deck (23 Sep) is the older version and is not edited after the reply.

**S9b prior forecast** (advisory, UNCALIBRATED, pre-registered): see the forecast block pasted below by `plan/run_gate.sh`.

HARDNESS FORECAST · UNCALIBRATED · advisory · DESIGN (declared attributions) · model claude-opus-5-5 · design · model outputs, not measurements; the Season Pass backtests are development fixtures, not validation
  rule:EXPORT                                  family done_gap                                 Beta(1.0, 2.8571) mean 0.26 n_eff 1.8571 records 13
  rule:ARTHOLD                                 family superseding                              Beta(2.5714, 1.2857) mean 0.67 n_eff 1.8571 records 25
  rule:REVISED                                 family stale_summary                            Beta(1.0, 2.8462) mean 0.26 n_eff 1.8462 records 12
  rule:AUDIO                                   family authority                                Beta(1.0, 2.8571) mean 0.26 n_eff 1.8571 records 13
  rule:PICKS                                   family superseding                              Beta(2.5714, 1.2857) mean 0.67 n_eff 1.8571 records 25
  rule:PARENT                                  family tool_surface                             Beta(1.0, 1.0) mean 0.50 n_eff 0.0 records 0
  independent whole    V3 E[avg] 0.583 [0.471, 0.700] P(all) 0.555
  independent whole    V3 E[avg] 0.583 [0.471, 0.700] P(all) 0.555
  independent whole    V3 E[avg] 0.583 [0.471, 0.700] P(all) 0.555
  independent whole    V3 E[avg] 0.583 [0.471, 0.700] P(all) 0.555
  independent whole    V3 E[avg] 0.583 [0.471, 0.700] P(all) 0.555
  source      whole    V3 E[avg] 0.583 [0.471, 0.700] P(all) 0.555
  source      whole    V3 E[avg] 0.583 [0.471, 0.700] P(all) 0.555
  source      whole    V3 E[avg] 0.583 [0.471, 0.700] P(all) 0.555
  source      whole    V3 E[avg] 0.583 [0.471, 0.700] P(all) 0.555
  source      whole    V3 E[avg] 0.583 [0.471, 0.700] P(all) 0.555
  correlated  whole    V3 E[avg] 0.597 [0.437, 0.762] P(all) 0.440
  correlated  whole    V3 E[avg] 0.597 [0.437, 0.762] P(all) 0.440
  correlated  whole    V3 E[avg] 0.597 [0.437, 0.762] P(all) 0.440
  correlated  whole    V3 E[avg] 0.597 [0.437, 0.762] P(all) 0.440
  correlated  whole    V3 E[avg] 0.597 [0.437, 0.762] P(all) 0.440
  V3: P(all four difficulty gates) 0.440-0.555 across scenarios; value of information (first scenario): ['rule:AUDIO', 'rule:EXPORT', 'rule:REVISED']
  slots most at risk (independent whole; P(fail) / P(fails all six) - all-fail justification workload, never a block): A1 0.98/0.89, W1 0.98/0.89, A2 0.93/0.71, W2 0.93/0.71, W9 0.93/0.71, X13 0.67/0.23, X14 0.67/0.23, X15 0.67/0.23

### Self-review

Gate output re-read after the last change: `HARDNESS GATE (extreme (design)): PASS` (pasted above, with its 37 ok lines and the volume-exception note). Re-read as the eval: `Evals/1_Prompt_Eval.md` §2.1 (Unique Ground Truth), §2.2 (Feasibility), §3.2 (Cross-Service Coherence) and `Evals/0_Injection_Quality_Eval.md` Check C, walked against §1a, §7 and §10. Load-bearing base values were re-read through `tools/hg.py` in this session (the vendor channel in full, the six #zombie-art messages, match3d#462's title and times through census C §3, the design page and its two comments, the Trello card and its three actions, Julia's DM and channel memberships).

| Item | Counter-reading (the best case that it fails) | Resolution (evidence) | Verdict |
|---|---|---|---|
| temporal | The ask is dated after the pause and asks for prep the pause was meant to stop. | the four 29 Sep base lines (§1) object to vendor development on a game that may change, not to knowing what the vendor holds; the ask scopes to 'the game as it is today' and says the part is redone if the core changes (`D05SD5QLG94/1759255800.418239`; `CADCE44A365D/1759172311.343939`) | holds |
| semantic | 'Owed' could mean owed by the vendor, or money. | the notes define the three states in one paragraph and nothing else uses the words (`f_8c1d0bca1d1d5fde4c5008`); learnings §80: each label defined in a record | holds |
| cross-service referential | The pack list and the tickets can disagree on a line's name or ticket. | both are generated from one model (`plan/design_model.py`: the pack list `f_956e60ec7f2f7977d98934`, tickets ART-794 to ART-890); the injection gate's `fact_check` holds them to it | holds, enforced at injection |
| quantitative | 19 / 30 / 54 could fork on Buttons or the plushie. | Buttons is Owed on its own ticket (`ART-882`); the plushie is one Delivered line (`C08H78VJG80/1758729487.922339`); both are in the two-reading table | holds |
| state/lifecycle | Done tickets for files that are unusable are a State/Lifecycle inconsistency in the seeded data. | each is a dated human claim (Brian's note) overturned by a named later record (`C08R27X0EAH/1758963900.284719`, `cmt_8b590c43980032fc5d02`); the task is to move them; card SC-16's tickets are not touched | holds as a designed claim |
| identifier/format | ART-793 to ART-890 could collide or break the series. | base highest is ART-792 with gaps before it (census C §1); `plan/check_ids.py`: 0 hits, scan complete | holds |
| other | A reviewer reads the cohort as padding: 103 lines for one ad. | the vendor asked for each group (`C08H78VJG80/1758283671.878269`), offers extra editable items (`C08H78VJG80/1758022459.227279`) and Brian planned to 'upload all the objects' (`C090N54TG79/1758569323.919359`); every line is a cell of the list the ask requests | holds |
| decision: How many lines | the alternative: 97: the pack list as it stands | the notes: 'If Robert has added objects since Brian made the list, they go on it too'; Robert's reply names six and says they go over (`f_8c1d0bca1d1d5fde4c5008`, `C08R8CHB0QL/1758906300.447189`) | best reading stands |
| decision: Twelve lines exported in one go | the alternative: Ready: tickets Done, files in the outgoing folder | Arthur wrote the export button and says every file from a multi-select run is an empty shell; the notes require that a Ready file opens (`C08R27X0EAH/1758963900.284719`) | best reading stands |
| decision: Twelve bathroom lines | the alternative: Ready: Claire's own 24 Sep note says fine to go | the same person, later: she is redoing the UVs and what Brian pulled is the old unwrap; the notes require that nobody is changing it (`D05HMBQUC8Z/1758874200.613049`) | best reading stands |
| decision: Five lines changed on 25 Sep | the alternative: Delivered or Ready: new colour versions are additions, the file sent is unchanged | the notes name the case: 'a fix, a retexture, new colour versions', 'so they always hold what the game has' (`f_8c1d0bca1d1d5fde4c5008`, `harmonygames-Games/match3d#462`, `C090N54TG79/1759189466.554739`) | best reading stands |
| decision: Eight music lines | the alternative: Ready: tickets Done, .glb is a type the vendor takes | Brian's own later comment: the set comes in grey and needs another pass before it goes (`cmt_8b590c43980032fc5d02`) | best reading stands |
| decision: Match scale and Explosion | the alternative: Ready: .wav is a type the vendor takes | the notes: only what we own outright leaves; Calvin's sheet marks both as cut from a bought pack (`f_b2387e31d46d3a7b3fa2a9`) | best reading stands |
| decision: The default eight | the alternative: with the iron (Robert's 23 Sep picks, Julia's deck) | Robert's own later reply; the ask keeps his latest word (`C08R8CHB0QL/1758906300.447189`) | best reading stands |
| decision: The four zombie lines | the alternative: Owed: the vendor said the package was not exported correctly | base: the full pack went on 26 Sep and the vendor reviewed it on 29 Sep (`C08H78VJG80/1758906043.375719`, `C08H78VJG80/1759140968.965099`) | best reading stands |
| decision: Tray size | the alternative: six (Julia's July proposal) | base: Robert's reply keeps the page at seven (`page_zm3d_gdd`, `confluence:comment_zm3d_gdd_c2`) | best reading stands |
| decision: Start date | the alternative: 6 October | base: the vendor's latest message (`C08H78VJG80/1759226395.551469`) | best reading stands |
| decision: Who the files are shared with | the alternative: the brief only; or Leonard (his card is the 'kickoff') | the notes: 'Sharing: both files, view only', the kickoff hold and Contacts (`evt_421695d009e589ee85296c`, `d7d31caf63ee33db2b7ed271`) | best reading stands |
| decision: Where the counts go | the alternative: the vendor channel | the ask: 'give me the three counts here'; both forms in the DM are accepted (`D05SD5QLG94/1759255800.418239`) | best reading stands |
| decision: Ticket follow-through on an Owed line | the alternative: a description edit, or a new ticket | the notes: 'goes back to Todo with a comment'; a new ticket only for a line without one (`f_8c1d0bca1d1d5fde4c5008`) | best reading stands |
| decision: Buttons | the alternative: Delivered: sent on the 24th | its own ticket note; the vendor takes 2D as PNG with parts separated (`ART-882`, `C08H78VJG80/1758283671.878269`) | best reading stands |
| decision: The plushie line | the alternative: a missing 'duck' line | base: the vendor's duck is the plushie sent the same day (`C08H78VJG80/1758723504.085039`, `C08H78VJG80/1758729487.922339`) | best reading stands |

Required items addressed: the two v2 decisions and their sources (§5); corrections off the first-read path (§5, v2 check); reach (§10); feasibility (§10, §7); volume and the every-run floor (§9); budget and spread (§6); known-data-issue cards (§1a); padding (§2).

Unresolved: none that blocks the design. Carried to `/create-injection` as checks, not open questions: the SQL wording sweep; `path_exposure.py` on the six deciding records; the cold-solver rehearsal; `persona_view.py check-sql` on every planned record.


## 13 Red-team findings

PENDING

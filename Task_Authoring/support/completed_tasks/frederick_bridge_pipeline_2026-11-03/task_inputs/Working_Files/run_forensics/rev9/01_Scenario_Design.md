# Scenario Design — frederick_bridge_pipeline · design only · contains no prompt, OE or criterion text

Built by `Working_Files/plan/build_scenario.py` (manifest + surface) and assembled by
`Working_Files/plan/assemble_design.py`. Every probability below is UNCALIBRATED.

Revision 7 (section 17): the platform `/prompt` of rev6 scored every content dimension 5 but failed the new STEP 0.6 dataset-duplicate gate (0.804 to another contributor's Frederick task on the Oct 14 board pre-read handoff). Rev7 keeps the universe, the traps and every record that decides them, and changes the job to the bridge part of the Q4 investor update send list (section 17). The sections below keep their rev6 wording where the job change does not touch them.

Revision 6 (`--revise`, section 15): the rev5 Opus pre-check solved every trap (platform `/hardness` score 1). Rev6 keeps
the prompt, the population and every graded value except T-Accelerate's build access. It moves three corrections off the
paths that run swept: Anton's amount goes to Leonard's DM D05S58U4SAK, SciPlay's pass to a #executives thread reply under
C07C2866011/1759196326.309469, and the Play tester gap to Arthur's #zombie-match3d post C0880U9751A/1759274400.518306. It
also strips the template's resolver sentences (section 15).

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe | key `synthcut`, label hg4-synth-sep30cut v16, clock line `Clock: 2025-10-01T07:00:00Z (Oct 1, 2025 00:00 PT, synth-cut)`, seed bound `freeze_utc` 2025-10-01T00:00:00Z, `shutdown_rules_apply` false |
| Persona | Frederick Stone, Co-founder, frederick.stone@harmonygames.co (roster `frederick_stone`); today = Wednesday Oct 1, 2025 |
| Business function → Evals category | Executive → Founders / Exec / Strategy (`Evals/references/rules/task_categories.md`) |
| Competency · skill · type · mode | Corporate Ops · Retrieval · long-horizon · medium (cap: corrected weighted average < 85 %; S0 design target ≤ 77 %) |
| Author targets (requester, 2026-11-01 chat) | over 100 tool calls in each run; average weighted pass under 80 %. Design target therefore E[avg] ≤ 72 % (manifest `author_targets`) |
| Horizon / profile | `horizon: Long Horizon` → `effective_profile: extreme`; no profile or volume exception (the 502-call budget below is honest, so none is needed) |
| Theme screen | investor update / fundraising; no bio-adjacent theme |

Remit argument (role review): Frederick is a co-founder on every bridge-round cc
(LVP `frederick.stone@harmonygames.co/1842277743427687737`, GFR `frederick.stone@harmonygames.co/1843547312959065138`,
Dentsu `frederick.stone@harmonygames.co/1843473831194478743`), a member of `#bridge-pitch` C096HFA5Z8W and
`#executives` C07C2866011, gave his own strategic call on the Homa co-dev path (C096HFA5Z8W/1758210489.170809)
and is invited to the Oct 14 board (evt_bd61f3209523d19fdd6ba2). Owning the fundraising section of the board
pre-read while Leonard is in LA for the Griffin meeting and Dentsu on Oct 1 is ordinary co-founder work.

Persona census (verbatim):

```
REACH  Frederick Stone <frederick.stone@harmonygames.co>  Co-founder / Executive
clock 2025-10-01

SLACK  user=EMPLOYEE_0008_SLACK_ID  visible channels=105 {'public': 12, 'private': 34, 'mpim': 17, 'im': 42}  messages=160793  public-not-member (UNVERIFIED)=55
  persona posts=4780 last post=2025-09-30  last activity in visible channels=2025-10-01
  C05H8KVNU67    game-design                            private mem=27  msgs=22750  2023-07-16..2025-08-28 archived
  C07C2866011    executives                             private mem=9   msgs=21836  2024-07-11..2025-10-01
  C050WGU41HR    engineering-bots                       private mem=35  msgs=19854  2023-03-29..2025-09-19
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16695  2023-10-07..2025-07-15
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16250  2025-01-09..2025-09-30
  C04UM32UWKD    investors                              private mem=8   msgs=6581   2023-03-18..2024-10-17
  C0553V44CE4    god-ui-ux                              private mem=30  msgs=5008   2023-04-21..2025-05-29 archived
  C04S28HSD0U    product                                private mem=21  msgs=4365   2023-03-02..2024-05-11 archived
  C069FF9Q57S    analytics                              private mem=28  msgs=4276   2023-12-05..2025-09-19
  D05S58U4SAK    D05S58U4SAK                            im      mem=5   msgs=4233   2023-09-15..2025-09-29

GMAIL  mailbox=frederick.stone@harmonygames.co threads=4656 messages=5474 range=2024-06-25..2025-10-01
  threads by last-message month (recent): {'2025-05': 323, '2025-06': 333, '2025-07': 249, '2025-08': 108, '2025-09': 185, '2025-10': 3}
  top correspondents: SVC_0107_EMAIL (1870), SVC_4131_EMAIL (1476), leonard.hayes@harmonygames.co (528), robert@harmonygames.co (337), arthur.blake@harmonygames.co (266), SVC_0521_EMAIL (192), brian.foster@harmonygames.co (102), SVC_0009_EMAIL (91), PERSON_5681_EMAIL (76), PERSON_1294_EMAIL (75)

GCAL  own=['frederick.stone@harmonygames.co'] shared=[] events=316 (distinct ical_uid 148, cancelled 27)
  last event before clock=2025-09-30T17:30:00Z  next after clock=2025-10-01T20:30:00Z
  by month: 2023-10:1 2024-07:1 2024-08:1 2024-09:65 2024-10:28 2024-11:27 2024-12:25 2025-01:28 2025-02:15 2025-03:7 2025-04:17 2025-05:25 2025-06:23 2025-07:22 2025-08:5 2025-09:22 2025-10:3 2026-01:1

DRIVE  owned=46 {'application/pdf': 12, 'application/vnd.google-apps.presentation': 12, 'application/vnd.google-apps.document': 8, 'application/json': 4, 'application/vnd.google-apps.spreadsheet': 4, 'folder': 2, 'text/plain': 2, 'text/csv': 2}
  shared-with=189 {'application/vnd.google-apps.document': 63, 'application/vnd.google-apps.spreadsheet': 31, 'text/plain': 28, 'application/vnd.google-apps.presentation': 23, 'application/json': 21, 'application/pdf': 21, 'text/csv': 2}
  shared by owner: {'Resource: -6481757892984311338': 100, 'Resource: 7240535625619857401': 40, 'leonard.hayes@harmonygames.co': 39, 'robert@harmonygames.co': 5, 'arthur.blake@harmonygames.co': 3, 'julia.lawson@harmonygames.co': 2}
  native visible: {'gdocs': 71, 'gsheets': 35, 'gslides': 35}  last modified visible=2025-09-30T17:50:11Z
  UNVERIFIED (domain/anyone, not owned/shared)=91 {'application/vnd.google-apps.document': 35, 'application/vnd.google-apps.spreadsheet': 33, 'application/json': 11, 'application/pdf': 8, 'application/vnd.google-apps.presentation': 4}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2025-09-30 (1d), slack_visible_channels=2025-10-01 (0d), gmail=2025-10-01 (0d), gcal_last_event_before_clock=2025-09-30 (1d), drive_last_modified_visible=2025-09-30 (1d)
```

Linear / Trello / Confluence identities (`entity.py resolve`): Linear usr_175c0d7bc72ed244, Trello
4b4a68fc0fec0b254e4f9d8e, Confluence user_EMPLOYEE_0008; GitHub login PERSON_2314 shows "Ryan" (hazard S04), so
no row depends on his GitHub identity.

## 1 Storyline

The September 2025 bridge round (universe_kb `timeline.md`, storyline "2025 fundraising: the Crownfall crypto pivot and
the failed bridge round", beats 2025-07-23 and 2025-09-03; `slack:C07C2866011:1756749288.785249`,
`drive:f_17e6175e84e745f92b3415`). Leonard launched a $2.5M bridge on Sep 3, logged reach-outs in `#bridge-pitch`
(C096HFA5Z8W/1756941551.539229, C096HFA5Z8W/1757345124.546449) and the shared 2025 investor list
(f_48247af79428823c3cac92, Latest Status column frozen "as of 09/11"). By Sep 25 he gave the round a 15 % chance
(C096HFA5Z8W/1758767624.533779). On Oct 1 he is in LA for the Griffin meeting and Dentsu
(frederick.stone@harmonygames.co/1832208184829815962). The task: Frederick brings the pipeline current as of end of
day Sep 30 PT for the Oct 14 board (evt_bd61f3209523d19fdd6ba2), records the money position and build access,
follows the keep-warm rule for passes and reports back to Leonard.

- Anchors by service: gmail hub (planned frederick.stone@harmonygames.co/1844724419788800011); slack C096HFA5Z8W and C07C2866011; gsheets f_48247af79428823c3cac92; gdocs planned template f_3b9e61c04d7a52e8f1a6c2; gcal evt_89381fe5a15b802c5652a9 (Homa), evt_25c9ee60d4b6c8f6d39a74 (SciPlay), evt_e59dc0a675d0c407b79acf (LVP); trello 68c5a49e8491a9d7faf869d0; linear planned ZOM-567; contacts planned e3a91c07d5b48f26a0c7e314; gdrive planned d_5e8a1c3f9b07d2e64a1b93; gslides planned f_a47d0e2c95b18f63e2c0d5.
- Natural span before injection: gmail, slack, gsheets, gdocs (f_17e6175e84e745f92b3415), gslides (f_7e68dfdc57ea569d7688a1), gcal, gdrive (d_175c0d7bc72ed244b944cb), trello (68c5a49e8491a9d7faf869d0) = 8 services; injection lifts it to 10 with contacts and linear (ZOM-567).
- cohorts.json: no fit — the KB cohorts are Linear/GitHub/Slack/Trello record sets; the investor census (f_48247af79428823c3cac92 plus off-list calls) is a sheet-plus-calendar cohort the KB does not catalog. SL-T27 (#investors threads, C04UM32UWKD) is the nearest and is 2023–24, out of window.
- trap_catalog ids used: D04 (investor-list lookalikes: f_0b29566cd7932a205d54d2 vs f_48247af79428823c3cac92), C01 (thread replies that correct: C096HFA5Z8W/1757716998.377299 thread), P01 (shared first names; no seeded voice collides), X01/X04 (redaction tokens and uneven company masking in frederick.stone@harmonygames.co/1843473831194478743), D03 (BoD deck families, f_7793bb93e59e9c0dee5129).
- Originality: no completed or calibration task uses the bridge round (support/completed_tasks README; Evals hardness_calibration.md cases); Frederick's two earlier tasks used card spend and marketing account handover (D05S58U4SAK), neither reused.

## 1a Coherence audit

Scope: every record a correct run opens (the hub, template, list f_48247af79428823c3cac92, every cc'd investor thread, `#bridge-pitch` C096HFA5Z8W and `#executives` C07C2866011 September history, calendar Sep 3–30, the two cards, ZOM-567, Contacts). Hazards walked from coherence_hazards.json (synthcut build).

| Record | Category | Fields / finding | Pointer | Hazard id | Disposition |
|---|---|---|---|---|---|
| Speedrun pass forwarded 20:21 PT Sep 30 (Oct 1 03:21Z) | temporal | exists before data horizon, after the seed bound | frederick.stone@harmonygames.co/1844748127814183717 | T03 none; clock rule GEN §0a | avoid: a16z ungraded; both statuses accepted; keep-warm count accepts 3 or 4 |
| Bubbles AI notes name the fund PXLite; list says T-accelerate | semantic | firm name differs between call notes and list | frederick.stone@harmonygames.co/1843978997950200606, f_48247af79428823c3cac92 | S03 (vocabulary mix) | fold into design: Contacts entry 5d0e8b31f7a29c64e1b0d3a8 ties Karthic to T-Accelerate (PXLite fund) — one row (T11) |
| GitHub display name "Ryan" for Frederick | semantic | identity | entities.json:/github/PERSON_2314 | S04 | avoid: no GitHub row |
| Slack links to Google docs use native ids | cross-service referential | C096HFA5Z8W/1757005515.318709 links a doc by Google id | C096HFA5Z8W/1757005515.318709 | R04 | avoid: seeded records name docs by title, never by Google URL |
| Invitation mails vs calendar copies | cross-service referential | Dentsu invitation mail frederick.stone@harmonygames.co/1844735562296076053 vs evt_3671b9a924ccba550e51fa / evt_eeca6fc7670fe1acd94440 | evt_3671b9a924ccba550e51fa | R08 | fold into design as distractor D7 (one future meeting) |
| Thread counters after a seeded reply | quantitative | reply_count / latest_reply on C07C2866011/1759196326.309469 (rev6; was C096HFA5Z8W/1757716998.377299) change | C07C2866011/1759196326.309469 | Q01, Q03 | repaired by companion UPDATE in the SQL (hazard_acknowledgements Q01); the seeded #zombie-match3d root C0880U9751A/1759274400.518306 carries its own counters |
| Same message in several mailboxes | quantitative | cc'd copies of seeded mails must match | frederick.stone@harmonygames.co/1844724419788800011 | Q10 | avoid: each seeded mail written once per mailbox with identical body |
| Duplicate calendar copies | quantitative | Dentsu Oct 1 twice | evt_eeca6fc7670fe1acd94440 | Q11 | excluded: base rows untouched |
| Open Linear issues assigned to quiet people | state/lifecycle | ZOM-567 assignee Arthur is `active_sep_2025_quiet_in_oct` | arthur.blake@harmonygames.co, ZOM-567 | L08 | dated claim: created and commented Sep 30 while active; Arthur's later Sep 30 post C0880U9751A/1759274400.518306 says the Play list is not live yet, so the open state is consistent |
| Stale list status | state/lifecycle | Latest Status "as of 09/11" vs later mail | f_48247af79428823c3cac92 | L08 none; human claim | designed: T10 (dated human column overturned by frederick.stone@harmonygames.co/1842283406259093714) |
| Mailbox alias in file names | identifier/format | frederick@ files vs frederick.stone@ ids | frederick.stone@harmonygames.co/1842285743246816270 | I03 | avoid: seeds use the roster address |
| Resource-owned files | identifier/format | list owner `Resource: 7240535625619857401` | f_48247af79428823c3cac92 | I14 | accepted: read-only population source, never a write target |
| Re:/Fwd: without references | identifier/format | seeded replies carry in_reply_to/references | frederick.stone@harmonygames.co/1844724419788800011 | I06 | avoid: companions set |
| Other: P&L vs Snowflake cash | other | cash differs ~$37K/month (Atlas Part B) | snowflake.FINANCE | Q05 | excluded: no cash or runway figure graded |

Known data issues (references/known_data_issues/synthcut.md, read at design per learnings §44, checked against the touched list f_48247af79428823c3cac92 and threads; no load-bearing fact, trap or graded slot rests on a card's "Don't grade" value):
- SC-33 (watch, investor sheet lists Acterra twice): touched by V1 (register size). Relied-on side: the incorporated template rule f_3b9e61c04d7a52e8f1a6c2 ("one row per name on the 2025 game investor list, angels included … a repeated name is still one row"), which counts Acterra (rows 71/86), Progression Fund (22/23) and BITKRAFT Ventures (32/33) once each in f_48247af79428823c3cac92; "Treo/Treeo" is a Slack spelling (C096HFA5Z8W/1756941551.539229), not a list duplicate. No raw sheet count is graded.
- SC-34 (row 82 labeled Superplay, contents Supercell): row 82's status is never sampled; it is one register row under either name (f_48247af79428823c3cac92).
- SC-9 (Play Ventures rejected vs no reply): settled in rev4. Leonard's Sep 25 correction C096HFA5Z8W/1758817200.730591 says the Sep 15 no (C096HFA5Z8W/1757955553.793529) was their reply to Griffin, which explains his Sep 23 "they didn't respond" (C096HFA5Z8W/1758671737.632949); the template counts a no sent to Griffin, so Passed, never sampled.
- SC-10 (LVP meeting date Sep 7 vs Sep 9): no date graded; LVP's status comes from its own thread frederick.stone@harmonygames.co/1842277743427687737; the call is evt_e59dc0a675d0c407b79acf (Sep 9).
- SC-40 (July board date 14 vs 16): the seeded July template says "for the Jul 16 board" (f_8d2c47a91e05b3f6d7c418), the card's safer value; not graded.
- SC-49 (founder count, Frederick's role): no founder count or founder status is graded; the role review rests on activity (evt_bd61f3209523d19fdd6ba2, C096HFA5Z8W).
- SC-3 / SC-73 (runway, monthly burn): no cash, runway or burn figure is read or graded (snowflake.FINANCE untouched).
- SC-7 (channel membership): membership is used only for reach (C096HFA5Z8W, C07C2866011), never graded.

Sibling-defect sweep: other list rows whose Latest Status is stale (Makers Fund, Raine Ventures, BBQ Capital in f_48247af79428823c3cac92) are read as "Awaiting reply" unless a later record says otherwise; Play Ventures (C096HFA5Z8W/1757955553.793529 vs C096HFA5Z8W/1758671737.632949) is reconciled by Leonard's rev4 correction C096HFA5Z8W/1758817200.730591; Mattel's Leonard-only RFP exchange is surfaced by his rev4 note C096HFA5Z8W/1758927000.205874; 1AM Gaming is tied to March Gaming Fund by C096HFA5Z8W/1757365500.384216. Every list row is classified once under the rev4 template rules (section 14), restated for rev6 in section 15. Rev6 sibling check: base Play tester messages (#executives C07C2866011/1758558621.032499 "They can join the Google Play Internal Test here", #bridge-pitch C096HFA5Z8W/1758677722.184129 "I have to add them by email for google play to work") agree with Arthur's rev6 post that the email list, not the link, decides access; Leonard's Sep 22 C07C2866011/1758570877.152159 "I'll add it to the testflight as well" agrees with TestFlight being live for T-Accelerate.

## 1b Active speakers

Status from activity.json (synthcut KB) at the clock for leonard.hayes@harmonygames.co, robert@harmonygames.co, arthur.blake@harmonygames.co and frederick.stone@harmonygames.co.

| Person | Email | status_at_clock | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | hub mail (Sep 30 21:05Z), template docs, card comments, angel post (Sep 19), Dentsu and Brightwater follow-ups; rev6: DM to Frederick D05S58U4SAK (Sep 24, Sep 26), thread reply in C0880U9751A (Sep 30) |
| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | rev6: SciPlay reply in the #executives thread C07C2866011/1759196326.309469 (Sep 30 9:06am PT); board-mail suggestion (Sep 29) |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | ZOM-567 and its Sep 30 comments; #executives aside (Sep 29); rev6: #zombie-match3d post C0880U9751A/1759274400.518306 (Sep 30) |
| Frederick Stone | frederick.stone@harmonygames.co | active_sep_2025_quiet_in_oct | persona; Board folder owner; no seeded voice |

External seeded voices (not in activity.json; mail reaches frederick.stone@harmonygames.co): Anton Bernstein and Paul Heydon (angels on f_48247af79428823c3cac92 rows 4–5), Edith Vane (Hiro Capital partner), Ilse Marrow (Brightwater Games Fund), the signing service notices; each gets a census before SQL (record plan).

## 1c Identity traps

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

ENTITY email:frederick.stone@harmonygames.co  name=Frederick Stone  kind=person  emails=['frederick.stone@harmonygames.co']
  persona: frederick_stone - Co-founder / Executive
  slack      id=EMPLOYEE_0008_SLACK_ID, name=Frederick Stone, real_name=Frederick Stone, email=frederick.stone@harmonygames.co, is_bot=False, deleted=False, messages=4780, first_post=2023-09-15, last_post=2025-09-30   [join: exact_email]
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=129898, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=110334, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=35266, first_post=2023-03-20, last_post=2025-10-01   [join: exact_email]
```

Pinned entities: Robert (robert@harmonygames.co) vs Robert in tokens [PERSON_NAME_0055]; Hiro Capital's Investment Director PERSON_5282 (frederick.stone@harmonygames.co/1842278425320449096) vs the new partner Edith Vane (Contacts e3a91c07d5b48f26a0c7e314); Karthic R PERSON_3242 vs PXLite (Contacts 5d0e8b31f7a29c64e1b0d3a8); no shared first name with Marcus, Martin, Claire or Thomas is used.

## 2 Cohort spine

- Rule (hub, planned frederick.stone@harmonygames.co/1844724419788800011): one row per firm on the 2025 game investor list f_48247af79428823c3cac92 (80 rows, 77 unique: Progression Fund, BITKRAFT Ventures and Acterra appear twice) plus every off-list firm with a call or meeting since Sep 3 (Homa evt_89381fe5a15b802c5652a9; Brightwater Games Fund planned evt_2f86b0d4c9e17a35b64e0d) = 79 firms (surface `truth_keys`).
- Per-record surfaces (manifest `cohort.evidence_surfaces`): gmail search + thread (2.1 calls × 79; frederick.stone@harmonygames.co/1842285743246816270 style threads), slack search + thread replies (1.55 × 79; C096HFA5Z8W), contacts (0.5 × 79; planned e3a91c07d5b48f26a0c7e314) = 327 per-record calls.
- Shortcut audit: the list's Latest Status (f_48247af79428823c3cac92) stops at 09/11; Leonard's tracker C096HFA5Z8W/1757345124.546449 stops at Sep 8; `gmail_search` returns ids only; channel history omits replies (rev6: SciPlay's pass lives in a reply under C07C2866011/1759196326.309469) and no channel read returns a DM (Anton's revised amount, D05S58U4SAK). No bulk call returns a firm's state at Sep 30.
- Predicate: template (planned f_3b9e61c04d7a52e8f1a6c2) buckets Passed / In talks / Awaiting reply / Not contacted this round, as of end of Sep 30 PT. Rev6 drops the rev5 house rule (a phone pass counts once written in #bridge-pitch): Passed now reads "they've told us no for this round", so a no heard by phone counts on its natural reading.
- Dual regime: July template (planned f_8d2c47a91e05b3f6d7c418) committed = verbal yes; Oct 14 template = signed SAFE.
- Boundary records: Homa (off list, evt_89381fe5a15b802c5652a9), Brightwater (off list), PXLite/T-Accelerate (one firm, frederick.stone@harmonygames.co/1843978997950200606), Metaplay and Rollic (out: frederick.stone@harmonygames.co/1832208184829815962, C096HFA5Z8W/1758130464.175719), duplicate list rows (f_48247af79428823c3cac92).

## 3 Hidden authorities

| Id | Authority (by what it governs) | Home | Decoy | decoy_scope | Governs | Findability proof |
|---|---|---|---|---|---|---|
| H1 | the Q4 update send-list doc (rev7; the Oct 14 board template in rev1-rev6) | gdocs planned f_3b9e61c04d7a52e8f1a6c2 (Leonard, Sep 26) | gdocs planned f_8d2c47a91e05b3f6d7c418 (July lot; committed = verbal yes) | lot: Q2 July board vs Q3 Oct 14 board | R2, R3, R4 | `hg.py search gdocs "board pre-read"` returns both once seeded (checked at injection); named by the hub (K3) |
| H2 | the keep-warm rule on the Existing Investor Update card | trello comment planned 68c6b2a4f19e03d7c5a81b2e on 68c5a49e8491a9d7faf869d0 | trello 663ea0fc3f231e879cefd5e8 "Investor Update" (Apr 2025) | issuer: existing investors' quarterly update vs bridge prospects | R6 | base card 68c5a49e8491a9d7faf869d0 found by its title; named by the hub (K9) |

`governs` do not overlap (H1 f_3b9e61c04d7a52e8f1a6c2, H2 68c5a49e8491a9d7faf869d0); both homes are rarely-opened services (gdocs, trello); each decoy shares the search terms ("send list", "investor update") with no self-advertising title word (the July send list is dated by its body, not "old" or "draft").

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Leonard's Q4 update email | frederick.stone@harmonygames.co/1844724419788800011 (planned) |

Hub: the anchor itself (frederick.stone@harmonygames.co/1844724419788800011), Leonard's voice, delegating by role (template, list, card, deck card, folder README, review event) and never listing locations of evidence.

| Fragment | Service · container | Requirement | Delegated by | Delegation quote (verbatim, to appear in the delegating record) |
|---|---|---|---|---|
| K1 | gmail · frederick.stone@harmonygames.co/1844724419788800011 | R7 | A1 | "reply here with how many firms and angels are in each group" |
| K2 | gmail · frederick.stone@harmonygames.co/1844724419788800011 | R5 | A1 | "put it in your Q4 investor update folder" |
| K3 | gmail · frederick.stone@harmonygames.co/1844724419788800011 | R1 | A1 | "everyone from the bridge round who should get it" |
| K4 | gdocs · f_3b9e61c04d7a52e8f1a6c2 | R2 | A1 | "with the groups and details in the Q4 update send list doc" |
| K5 | gdocs · f_3b9e61c04d7a52e8f1a6c2 | R3 | A1 | same quote (template money definitions) |
| K6 | gdocs · f_3b9e61c04d7a52e8f1a6c2 | R4 | A1 | same quote (template build-access definition) |
| K7 | gsheets · f_48247af79428823c3cac92 (base) | R1 | K4 | "Every name on the 2025 game investor list" |
| K9 | trello · 68c5a49e8491a9d7faf869d0 + comment 68c6b2a4f19e03d7c5a81b2e | R6 | A1 | "do what I put on the Existing Investor Update card in Trello" (rev9 hub wording) |
| K18 | trello · 68c5a49e8491a9d7faf869d0 + comment 68db03b86054eff7e8e92474 (rev9) | R6, R8 | K9 | same quote (Leonard's Sep 29 comment: a checklist per group, follow-up cards in To Do) |
| K16 | gdrive · d_5e8a1c3f9b07d2e64a1b93 (rev7 folder) | R5 | A1 | "put it in your Q4 investor update folder" |
| K11 | gslides · f_a47d0e2c95b18f63e2c0d5 (rev7 draft Q4 update deck) | R1 | A1 | "The draft update deck shows what each group gets" |
| K12 | gcal · evt_9c41e7a2d05b38f6e1a7c4 (planned) | R5 | A1 | "I put Monday's review on your calendar" |
| K13 | gdocs · f_c61a0e93b7d24f58a2e917 (planned README) | R5 | K2 | "the README in that folder says how to name it" |
| K14 | linear · ZOM-567 (planned) | R4 | K6 | "build access is whatever Arthur's investor tester ticket in Linear shows" (final wording: "Arthur tracks the tester adds") |
| K15 | slack · C0880U9751A/1759274400.518306 (planned, rev6) | R4 | K6 | "Arthur tracks the tester adds" |
| K17 | slack · C07C2866011/1758911700.336170 (planned, rev7) | R3 | K5 | "see my note in #executives on what counts as signed" |

K8 (Robert's #bridge-pitch phone-note root) is dropped in rev6 (section 15, purge P2). K15 is Arthur's later word on the tester adds; the template sentence that delegates to his ticket delegates to it too.

Amendment in a different service, later: the Oct 14 template (gdocs f_3b9e61c04d7a52e8f1a6c2, Sep 26) amends the July template's committed rule (f_8d2c47a91e05b3f6d7c418, Jul 8); the rest of the July buckets stand. Non-authoritative distractors: Arthur's aside (C07C2866011/1759168800.117903), Robert's board-mail suggestion (frederick.stone@harmonygames.co/1844623441920000059), the April Investor Update card (663ea0fc3f231e879cefd5e8).

## 5 Chains and trap register

| Trap | Family | Records | Req | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | done_gap | C07C2866011/1758303600.418207, frederick.stone@harmonygames.co/1844610859008000037 | R3 | Paul Heydon committed $50,000 | reminder: SAFE awaiting Paul's signature Sep 29; template: committed = signed | post read in history; reminder is one automated notice |
| T2 | done_gap | frederick.stone@harmonygames.co/1844347876147200047 → ZOM-567 → C0880U9751A/1759274400.518306 (+ reply C0880U9751A/1759276080.094417) | R4 | T-Accelerate and Dentsu have iOS and Android (ZOM-567 logs both tracks; "invites are out") | Arthur's Sep 30 #zombie-match3d post: the Play tester list was never attached to the internal track, so neither can get the Android build; Arthur attaches it with his Oct 1 build push | the ticket is the record the template points to and reads as done; the correction is a later post in the game channel, not on the ticket |
| T3 | superseding | frederick.stone@harmonygames.co/1842285743246816270 (Sep 12, Sep 18) → C07C2866011/1759248360.377105 (thread C07C2866011/1759196326.309469) | R2 | SciPlay In talks | Robert's Sep 30 thread reply in #executives: SciPlay's contact called, they're out for this round | reply under Leonard's speedrun post, not in channel history; the root names another firm |
| T4 | superseding | C07C2866011/1758303600.418207 → f_6e1d93a0c4b72f85d39a0e → D05S58U4SAK/1758731100.281734 (+ D05S58U4SAK/1758914100.640218) | R3 | Anton $40,000 | Leonard's Sep 24 DM: Anton down to $25,000, SAFE re-sent at 25; Sep 26 DM: Anton signed the 25 one; completed notice frederick.stone@harmonygames.co/1844354293432320031 has no amount | post and sheet agree and are read first; a DM is returned by no channel read |
| T5 | scope_alias | frederick.stone@harmonygames.co/1844318935449600041, e3a91c07d5b48f26a0c7e314, frederick.stone@harmonygames.co/1842278425320449096 | R2 | Hiro Capital Awaiting reply | Edith Vane's pass (cc Hiro's Investment Director); Contacts maps her | "Hiro" search returns only the Sep 3 thread |
| T6 | exact_predicate | evt_2f86b0d4c9e17a35b64e0d, b72f0d6e19c3a84e5d21f9a0, frederick.stone@harmonygames.co/1844276782694400053 | R1 | Brightwater missing | population includes calls since Sep 3; Contacts ties Ilse Marrow to Brightwater | one of ~20 person-titled events |
| T7 | near_miss_mention | evt_89381fe5a15b802c5652a9, frederick.stone@harmonygames.co/1843169166284025277, C096HFA5Z8W/1758210489.170809 | R1 | Homa missing | invitation names HOMA; Frederick's own note | list read first |
| T8 | authority | 68c6b2a4f19e03d7c5a81b2e on 68c5a49e8491a9d7faf869d0 | R6 | no keep-warm items | card comment rule | hub names the card by role |
| T9 | superseding | f_8d2c47a91e05b3f6d7c418 → f_3b9e61c04d7a52e8f1a6c2 | R3 | committed = verbal yes | Oct 14 template | both answer the same search |
| T10 | superseding | f_48247af79428823c3cac92 → frederick.stone@harmonygames.co/1842283406259093714 | R2 | T-Accelerate "first pitch being scheduled" | Sep 22 call recap | list read first |
| T11 | scope_alias | 5d0e8b31f7a29c64e1b0d3a8, frederick.stone@harmonygames.co/1843978997950200606 | R1 | PXLite as an extra firm | Contacts: T-Accelerate (PXLite fund) | notes name only PXLite |
| D1 | distractor · near_duplicate_record | f_0b29566cd7932a205d54d2 | R1 | 2024 list as population | ask names the 2025 list | D04 lookalike |
| D2 | distractor · non_authoritative_instruction | C07C2866011/1759168800.117903 | R1 | only firms Leonard emailed | Leonard's population rule | aside is in channel history |
| D3 | distractor · scope_adjacent | C096HFA5Z8W/1758130464.175719, frederick.stone@harmonygames.co/1843000993076735547 | R1 | Rollic / Playable Factory added | template: service, publishing, competitor talks out | both are September talks |
| D4 | distractor · stale_summary | C096HFA5Z8W/1757345124.546449 | R2 | Sep 8 tracker statuses | later mail and notes | tracker is pinned-looking and complete |
| D5 | distractor · withdrawn_ask | frederick.stone@harmonygames.co/1844623441920000059 | R7 | mail the board | hub: reply to Leonard | Robert's mail is the day before |
| D6 | distractor · other_title | 663ea0fc3f231e879cefd5e8 | R6 | items on the April card | hub and comment name the Existing Investor Update card | same search term |
| D7 | distractor · near_duplicate_record | evt_3671b9a924ccba550e51fa, evt_eeca6fc7670fe1acd94440 | R4 | two Dentsu meetings | one future meeting; Dentsu In talks on its Sep 23 call | both on the calendar |

Chains (root causes distinct): C1 A24 (C07C2866011/1758303600.418207 → f_3b9e61c04d7a52e8f1a6c2 → frederick.stone@harmonygames.co/1844610859008000037, R3); C2 A14 (frederick.stone@harmonygames.co/1842285743246816270 → f_3b9e61c04d7a52e8f1a6c2 → C07C2866011/1759248360.377105, R2); C3 A7 (f_48247af79428823c3cac92 → frederick.stone@harmonygames.co/1844318935449600041 → e3a91c07d5b48f26a0c7e314, R2); C4 A17 (evt_2f86b0d4c9e17a35b64e0d → b72f0d6e19c3a84e5d21f9a0 → frederick.stone@harmonygames.co/1844276782694400053, R1); C5 A15 (frederick.stone@harmonygames.co/1844724419788800011 → 68c6b2a4f19e03d7c5a81b2e → C07C2866011/1759248360.377105, R6).

Hardness v2 selection (named traps, each a cross-source decision flipping weight-5 rows; 01_Gradable_Surface.json):
- v2 trap 1 (done across services, A24) ×2: DONE1 — wrong source Leonard's #executives post C07C2866011/1758303600.418207 (co-founder, Sep 19, says "is in"); beaten by the signing-service reminder frederick.stone@harmonygames.co/1844610859008000037 under the template's definition; flips M1, M2, RP2, RP3. DONE2 (rev6) — wrong source Arthur's own ZOM-567 log (TestFlight and Play adds for T-Accelerate and Dentsu) plus Leonard's Dentsu mail frederick.stone@harmonygames.co/1844347876147200047 ("invites are out to all three"); beaten by Arthur's later post C0880U9751A/1759274400.518306 (the Play tester list was never attached to the internal track); flips AC1, AC2.
- v2 trap 2 (correction somewhere else): CORR — wrong source SciPlay's own thread frederick.stone@harmonygames.co/1842285743246816270; beaten by Robert's rev6 reply C07C2866011/1759248360.377105 in another service, under a root about another firm; flips ST1, RP3 (rev9: and SciPlay's checklist and follow-up card).
- v2 trap 6 (alias): ALIAS — wrong source the list row f_48247af79428823c3cac92 ("no response as of 09/11"); beaten by Edith Vane's pass frederick.stone@harmonygames.co/1844318935449600041 mapped by Contacts e3a91c07d5b48f26a0c7e314; flips ST2, RP3 (rev9: and Hiro's checklist and follow-up card).
- v2 trap 7 (outside the filter): FILT — Homa (evt_89381fe5a15b802c5652a9) and Brightwater (evt_2f86b0d4c9e17a35b64e0d), wrong source the 2025 list f_48247af79428823c3cac92 as the population; flips V1, ST3, ST4.
- v2 trap 8 (wrong inputs to a total): INPUT — wrong source the #executives post and the Bridge angels sheet ($40,000); beaten by Leonard's rev6 DM D05S58U4SAK/1758731100.281734 (Anton down to $25,000, SAFE re-sent and signed at 25); flips M3, M2, RP2.
- v2 trap 3 (follow-through): FOLLOW — card rules 68c6b2a4f19e03d7c5a81b2e and (rev9) 68db03b86054eff7e8e92474; flips CL1.
- v2 trap 6 (alias), rev9: DUP — wrong reading a new "F/up with NCsoft" card; beaten by Leonard's open To Do card 68c99e98737744bd966aed24 "F/up with Anel after the engine deep dive" (Anel Ceman is NCsoft's partner on f_48247af79428823c3cac92) and his Sep 29 rule to comment on an existing To Do card; flips AN1 (FU1 control).
- v2 trap 7 (outside the filter), rev9: BOOKED — wrong reading follow-up cards for Dentsu and Makers Fund; beaten by Fred's calendar after Sep 30 (base evt_3671b9a924ccba550e51fa Oct 1; seeded evt_6b2e94d0c17a3f58e9d2b1 Oct 8, titled by Makers' partner Michael Cheung, mapped by the 2025 list's Partner column) under the same rule; graded by the rubric's exact follow-up set (FU2 control).

### Mechanism portfolio (S5a)

Candidates generated (14), each grounded: DONE1, DONE2, CORR, ALIAS, FILT, INPUT, FOLLOW (selected) and COMPL (LVP already on the keep-warm list, rejected: an exact check-item count is not decodable by the grader, `gradeable-report`), DOCSEND (DocSend view counts, rejected: notices sit in Leonard's mailbox, not Frederick's), CASH (runway line, rejected: hazard Q05, f_605121f4a36752645e0ac3 vs snowflake.FINANCE), TZ (a16z pass at 19:30 PT, rejected: after the seed bound, frederick.stone@harmonygames.co/1844748127814183717), PLAYV (Play Ventures pass, rejected: base contradiction C096HFA5Z8W/1758671737.632949), GFR-MOVE (cancelled Sep 29 copy evt_38bdf82a0d337c4d82695e, rejected: Opus reads both copies in one list call), BUBBLES (T-Accelerate action items frederick.stone@harmonygames.co/1843978997950200606, rejected: "share with the team" reads two ways).

| Rule | Deciding record | Mechanism | Nodes | Natural-reading fallback | Prior family · ledger records | Survives complete retrieval | Tool-surface proof | Weight-5 slots |
|---|---|---|---|---|---|---|---|---|
| DONE1 | frederick.stone@harmonygames.co/1844610859008000037 | A24 | T1, C1 | angels "in" = committed | done_gap · Beta(1,1), 0 Opus 5.5 records | yes: the reminder must be weighed against the post | reminder returned by a Gmail search for the angel's name | M1, M2, RP2 |
| INPUT | D05S58U4SAK/1758731100.281734 | A11 | T4 | Anton $40,000 (post + sheet) | superseding · 1 Opus 5.5 record (rev5 LEAKED, hev_e61e07235eadbd24) | yes: amount reconciliation across a DM | slack search "Anton" returns the DM lines | M3, M2, RP2 |
| DONE2 | C0880U9751A/1759274400.518306 | A24 | T2 | T-Accelerate and Dentsu both platforms | done_gap · 1 record (rev5 LEAKED, hev_522f1ca2bc9062de) | yes: done log vs later post | slack search "TestFlight", "Play", "Dentsu" or "Karthic" returns the post | AC1, AC2 |
| CORR | C07C2866011/1759248360.377105 | A14 | T3, C2 | SciPlay In talks | superseding · 1 record (rev5 LEAKED, hev_1ceea0e7e912f48b) | yes: reply must be placed against the thread | slack search "Sciplay" returns the reply | ST1, RP3 |
| ALIAS | e3a91c07d5b48f26a0c7e314 | A7 | T5, C3 | Hiro Awaiting reply | scope_alias · 0 records | yes: person→firm mapping | contacts_search_contacts returns Edith Vane | ST2, RP3 |
| FILT | evt_2f86b0d4c9e17a35b64e0d | A17 | T6, T7, C4 | list rows only | exact_predicate · 0 records | yes: scope rule must be applied to calendar calls | gcal_list_events returns both calls | ST3, ST4 |
| FOLLOW | 68c6b2a4f19e03d7c5a81b2e, 68db03b86054eff7e8e92474 | A15 | T8, C5 | no checklists on the card | authority · 0 records | yes: rule applies after retrieval | trello_get_comments returns both comments | CL1 |
| DUP (rev9) | 68c99e98737744bd966aed24 | A7 | T12, C6 | a new NCsoft card | scope_alias · 0 records | yes: partner→firm mapping on a To Do card | trello_search "F/up" or the To Do list returns the card; the list's Partner column maps Anel | AN1 |
| BOOKED (rev9) | evt_6b2e94d0c17a3f58e9d2b1 | A17 | T13, C7 | cards for Dentsu and Makers | exact_predicate · 0 records | yes: the exception sits after the listed window | gcal_list_events after Sep 30 returns both | rubric (FU2 control) |

Priors (ledger support/hardness_ledger/ledger.jsonl): rev6 priors include the seven rev5 pre-check records (all LEAKED: hev_7f44d83eaad625e9, hev_e61e07235eadbd24, hev_522f1ca2bc9062de, hev_1ceea0e7e912f48b, hev_ab2508cad060b0ac, hev_9c403cae42eb4df8, hev_d17e4abe74f0e7e0), so each family starts at Beta(1,2); no other model's evidence is transferred. They describe rev5's placements, and rev6 moves INPUT, DONE2 and CORR off the paths that run swept. Controls and over-application per rule (e.g. DONE1 control Anton, frederick.stone@harmonygames.co/1844354293432320031) are in the manifest `mechanism_portfolio[].controls/over_application`; channels CH-FILT-HOMA, CH-FILT-BRIGHT (member channels, latent "calendar sweep") and CH-SLIP (control rows ST5, RP1, DL1; AC2 is a DONE2 slot in rev6) are declared in `channels`.

### Liveness flags (S5b)

`trap_liveness.py --design` (verbatim in section 12; hub frederick.stone@harmonygames.co/1844724419788800011) raised breadcrumb/order flags on T1, T6, T7, T8, T9, T11, D1, D3, D5, D6. Dispositions (also in `plan/liveness_dispositions.json`):
- T1 breadcrumb (frederick.stone@harmonygames.co/1844610859008000037): keep — the hub names the template by role only; the reminder's subject names the SAFE, not the word "committed".
- T6/T7/T11 breadcrumb+order (evt_2f86b0d4c9e17a35b64e0d, evt_89381fe5a15b802c5652a9, 5d0e8b31f7a29c64e1b0d3a8): keep — the population rule must name calls (UGT); the difficulty is applying it to person-titled events, never removed.
- T8 breadcrumb (68c5a49e8491a9d7faf869d0): keep — the hub must name the card for incorporation; the rule itself is a comment.
- T9 breadcrumb (f_3b9e61c04d7a52e8f1a6c2): keep — the template must be incorporated; the decoy shares its terms.
- D1/D3/D5/D6 (f_0b29566cd7932a205d54d2, C096HFA5Z8W/1758130464.175719, frederick.stone@harmonygames.co/1844623441920000059, 663ea0fc3f231e879cefd5e8): distractors are meant to be met; no fairness link removed.

`hardness_v2_check.py --design` (manifest 01_Hardness_Manifest.draft.json, rev6): every check CLEAN (SAME_PLACE 0 flagged over 5 version-record traps; DONE_CHECK; TWO_DECISIONS over R1, R2, R3, R4, R6; DECISION_FLIP 7/7; INPUT_CHECK; FILTER_CHECK; RULE_IN_PROMPT no run of 8 resolver words in the prompt) (`plan/v2_check.txt`). The rev5 run showed what the static check cannot see (section 15): a rulebook on the delegation path and corrections inside containers a run sweeps whole. Rev6 places each moved correction in a container the rev5 run never opened (a DM, a #executives thread, #zombie-match3d).

## 6 Failure-diversity plan

| Channel | Runs likely to miss it | Requirement touched | Findability tier |
|---|---|---|---|
| DONE1 (C07C2866011/1758303600.418207) | runs that take #executives at its word | R3, R7 | medium |
| INPUT (D05S58U4SAK/1758731100.281734) | runs that trust the post and the sheet and never search Slack for Anton (the rev5 run read no DM) | R3, R7 | medium |
| DONE2 (C0880U9751A/1759274400.518306) | runs that stop at the tester ticket and never look for Arthur's later word | R4 | medium |
| CORR (C07C2866011/1759248360.377105) | runs reading #executives history without opening threads (the rev5 run read it in concise form, no replies) | R2, R6 | medium |
| ALIAS (e3a91c07d5b48f26a0c7e314) | runs matching firms by list name only | R2, R6 | medium |
| FILT-Homa (evt_89381fe5a15b802c5652a9) | runs bounded by the list | R1 | medium-high |
| FILT-Brightwater (evt_2f86b0d4c9e17a35b64e0d) | runs that skip person-titled calls | R1 | low |
| FOLLOW (68c6b2a4f19e03d7c5a81b2e) | runs that never read card comments | R6 | medium-low |

No single discovery gates most requirements: the largest unit (DONE1) decides 18 of 71 weight (25 %).
Policy scores on the real surface (`plan/policy_scores_output.txt`, UNCALIBRATED):

```
UNCALIBRATED · surface weight 79
  100.0%  perfect
   70.9%  mail and channel history only, no DMs, thread replies or later posts (INPUT DONE2 CORR)
   73.4%  list-bound (FILT both, ALIAS)
   68.4%  trusts done sources (DONE1 DONE2 INPUT)
   96.2%  all but follow-through
   31.6%  lazy (all land)
single misses: {'DONE1': '87.3%', 'INPUT': '93.7%', 'DONE2': '87.3%', 'CORR': '89.9%', 'ALIAS': '89.9%', 'FILT_HOMA': '89.9%', 'FILT_BRIGHT': '89.9%', 'FOLLOW': '96.2%'}
two misses (lowest/highest): 74.7% ('DONE1', 'DONE2') ... 89.9% ('INPUT', 'FOLLOW')
  scale 1.0 rho 0.3: {'E_avg': 0.773, 'P(avg<80%)': 0.6518333333333334, 'P(avg<85%)': 0.8768333333333334, 'P(SD band)': 0.85, 'P(patterns)': 0.9725, 'P(all gates)': 0.7635}
  scale 1.0 rho 0.6: {'E_avg': 0.775, 'P(avg<80%)': 0.6065, 'P(avg<85%)': 0.8155, 'P(SD band)': 0.9223333333333333, 'P(patterns)': 0.9485, 'P(all gates)': 0.7675}
  scale 0.75 rho 0.3: {'E_avg': 0.828, 'P(avg<80%)': 0.32116666666666666, 'P(avg<85%)': 0.617, 'P(SD band)': 0.7625, 'P(patterns)': 0.953, 'P(all gates)': 0.5373333333333333}
  scale 0.75 rho 0.6: {'E_avg': 0.83, 'P(avg<80%)': 0.329, 'P(avg<85%)': 0.573, 'P(SD band)': 0.845, 'P(patterns)': 0.9315, 'P(all gates)': 0.5456666666666666}
  scale 0.6 rho 0.3: {'E_avg': 0.861, 'P(avg<80%)': 0.14916666666666667, 'P(avg<85%)': 0.3948333333333333, 'P(SD band)': 0.6588333333333334, 'P(patterns)': 0.9375, 'P(all gates)': 0.3441666666666667}
  scale 0.6 rho 0.6: {'E_avg': 0.863, 'P(avg<80%)': 0.1915, 'P(avg<85%)': 0.3895, 'P(SD band)': 0.755, 'P(patterns)': 0.8983333333333333, 'P(all gates)': 0.374}
  scale 0.5 rho 0.3: {'E_avg': 0.883, 'P(avg<80%)': 0.07016666666666667, 'P(avg<85%)': 0.25116666666666665, 'P(SD band)': 0.5636666666666666, 'P(patterns)': 0.9115, 'P(all gates)': 0.22316666666666668}
  scale 0.5 rho 0.6: {'E_avg': 0.885, 'P(avg<80%)': 0.10966666666666666, 'P(avg<85%)': 0.2758333333333333, 'P(SD band)': 0.6603333333333333, 'P(patterns)': 0.8683333333333333, 'P(all gates)': 0.2635}
```

## 7 Deliverables and dependent writes

| Write | Tool | Destination | Depends on | Requirements |
|---|---|---|---|---|
| Send list (rev7: one row per firm or angel kept on the list: group, amount for new investors and unsigned angels, build access for firms in talks) | gsheets_create_spreadsheet + gsheets_values_update | Q4 2025 investor update folder d_5e8a1c3f9b07d2e64a1b93 (owner Frederick) | K3–K7, K11, C1–C4, T1–T7 | R1–R4 |
| File placement | gdrive_move_file (or create with parent) | d_5e8a1c3f9b07d2e64a1b93, named per README f_c61a0e93b7d24f58a2e917 | K2, K13 | R5 |
| Send checklists (rev9: one per group, one item per firm or angel; 4 checklists, 26 items) | trello_create_checklist / trello_create_check_item | card 68c5a49e8491a9d7faf869d0 | K9, K18, C5, T3, T5, T8 | R6 |
| Follow-up cards (rev9: 19 "F/up with" cards in To Do 640643a3fd8f3ca308d93195; a comment on 68c99e98737744bd966aed24 for NCsoft; none for Dentsu, Makers) | trello_create_card / trello_add_comment | Harmony Games board 640643a3fd8f3ca308d9318e | K18, C6, C7, T12, T13, T3, T5 | R8 |
| Reply | gmail_reply_to_message | thread frederick.stone@harmonygames.co/1844724419788800011 (Leonard; cc as on the ask) | K1, C1, C4, T1, T3, T5 | R7 (rev7: how many firms and angels in each group) |

Reuse-vs-create: no checklist pre-exists on the card; Leonard's comments ask for a Keep warm checklist (Sep 13) and one per other group (Sep 29), each created once and then filled. Follow-up cards are created except where a To Do card already exists for the firm (NCsoft: comment on it).

## 8 Service role map

| Service | Role | Load-bearing fact / write | Carrier |
|---|---|---|---|
| gmail | hub, investor threads, signing notices, Hiro, Dentsu, Brightwater, reply | Paul unsigned, Hiro pass, Dentsu "invites out" | ● |
| slack | #executives angel post and Robert's thread reply; Leonard's DM D05S58U4SAK; Arthur's #zombie-match3d post | SciPlay pass, Anton's revised amount, Play tester gap | ● |
| gsheets | 2025 list; register write | population; register | ● |
| gdocs | template, July decoy, README | definitions | ● |
| gcal | pitch calls; review event | off-list calls | ● (titles/attendees); descriptions ○ |
| contacts | partner→firm | Hiro, Brightwater, PXLite mapping | ○ supporting (job title field; verified through contacts_search_contacts at injection) |
| trello | keep-warm rule; deck card numbers | rule; checklist write | ● comments |
| linear | ZOM-567 | the done source for build access (adds logged) | ● (description + comments) |
| gdrive | Board folder | destination | ● |
| gslides | draft deck slide 9 | register columns | ● slide element text (no speaker notes: their rendering is unverified, Ask_Carriers §5) |
| github | none | — | — |
| confluence | none (injected pages never relied on, learnings §26) | — | — |
| snowflake | none (cash hazard Q05 avoided) | — | — |

## 9 Call budget

| Phase | Service | Calls | Reason |
|---|---|---|---|
| discovery | gmail | 8 | read the ask and its thread; Robert's Q4 list mail; find the send-list doc, README, draft deck |
| discovery | gdocs | 5 | read the Q4 send-list doc, the Q3 (July) send list it supersedes, the folder README |
| discovery | gslides | 3 | open the draft Q4 update deck and read what each group gets |
| discovery | trello | 8 | find and read the Existing Investor Update card (and the older Investor Update card), comments and checklists |
| discovery | gdrive | 4 | locate the Q4 2025 investor update folder and list it |
| discovery | gcal | 6 | Monday's review event; list Sep 3-30 events on Frederick's calendar (two pages) |
| enumeration | gsheets | 4 | read the 2025 investor list (80 rows, several ranges) and check the 2024 lookalike |
| enumeration | slack | 22 | #bridge-pitch Jul-Sep history (4 pages at 100) and #executives Sep history (about 12 pages), roots only |
| per-record | gmail | 169 | one search per firm by name (79), a second by partner for the ~40 firms whose list row or mail names one, and a thread read for each of the ~50 firms with hits; search returns ids only, no bulk |
| per-record | slack | 124 | one search per firm and angel (79) plus about 45 thread or DM opens where a hit needs its context; replies and DMs are not in channel history |
| per-record | contacts | 40 | partner lookups for the list's Partner column, person-titled calls and partner-only replies |
| reconciliation | gcal | 18 | open each person-titled pitch event since Sep 3 for its description and attendees |
| reconciliation | gmail | 26 | signing-service notices per angel, Anton's and Paul's mails, Dentsu and Brightwater follow-ups, Hiro decline |
| reconciliation | linear | 6 | find ZOM-567, read it and its comments for each firm in talks |
| reconciliation | slack | 4 | check Arthur's and Leonard's later word on the tester adds (search by firm, TestFlight, Play) |
| reconciliation | slack | 29 | open every replied thread in #executives (22) and #bridge-pitch (7) for September: phone notes and corrections live in replies |
| rules | gdocs | 4 | re-read the send-list doc's definitions while grouping edge firms |
| rules | slack | 2 | read Leonard's #executives note on what counts as signed |
| rules | contacts | 6 | check mapping for Karthic/PXLite and Hiro's Investment Director |
| writes | gsheets | 6 | create the send list and write its 26 rows |
| writes | gdrive | 2 | place the sheet in the Q4 update folder and confirm |
| writes | trello | 50 | 4 checklists on the card (one per group) and 26 items (one per firm or angel); 19 follow-up cards in To Do; 1 comment on the open Anel card (no batch write exists for items or cards) |
| reconciliation | trello | 3 | list the To Do cards and map each open one to a firm before adding cards |
| reconciliation | gcal | 2 | list Fred's calendar after Sep 30 for calls already booked with In talks or Awaiting reply firms |
| writes | gmail | 1 | reply on Leonard's thread |
| read-back | gsheets | 3 | read back the written ranges and the group counts |
| read-back | trello | 2 | read the checklist back |
| read-back | gdrive | 1 | confirm the file's parent folder |

Total 506 necessary calls, all unconditional; per-record 333; 10 services; largest share outside per-record 32 %. (The rev5 Opus run made 107 tool calls by bulk listing; rev6's moved corrections each need a further Slack search or thread/DM read.)
The golden run also needs the volume: every firm's status at Sep 30 needs its own search (no bulk call returns it). Author target "over 100 calls in each run" is met with margin.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolution |
|---|---|---|---|
| a16z status (frederick.stone@harmonygames.co/1844748127814183717) | In talks (speedrun interview evt_e802a3583ee79ff6087f76 is a call) | Passed (19:30 PT Sep 30 is still Sep 30 PT) | settled rev4: the template's accelerator rule (f_3b9e61c04d7a52e8f1a6c2) says a program decision is not a bridge answer; KW stays 3 |
| Play Ventures (C096HFA5Z8W/1757955553.793529) | Passed | Awaiting reply (C096HFA5Z8W/1758671737.632949) | settled rev4 by Leonard's correction C096HFA5Z8W/1758817200.730591 and the template's Griffin rule |
| PXLite vs T-Accelerate (frederick.stone@harmonygames.co/1843978997950200606) | one firm | separate off-list firm | Contacts 5d0e8b31f7a29c64e1b0d3a8 settles one firm |
| Homa in scope (frederick.stone@harmonygames.co/1843552279434086285) | in (co-dev investment talks) | out (publishing) | Frederick's note C096HFA5Z8W/1758210489.170809 + template "investment, incl. strategic" |
| Rollic / Metaplay (C096HFA5Z8W/1758130464.175719) | out | in | template excludes service and competitor talks |
| Dentsu build access (ZOM-567, C0880U9751A/1759274400.518306) | iOS only | iOS and Android (ZOM-567 logs both; Leonard's "invites are out") | rev6: Arthur's Sep 30 post says the Play tester list was never attached to the internal track, so none of the investor testers can get the Android build; Arthur attaches it only with his Oct 1 build push, after the as-of (Leonard's thread reply C0880U9751A/1759276080.094417 asks to be told when it's live); the template's "whether they can get the current internal build" |
| T-Accelerate build access (ZOM-567, C0880U9751A/1759274400.518306) | iOS only | iOS and Android (ZOM-567; base C07C2866011/1758558621.032499 Play link) | the same post names Karthic; TestFlight is live (base C07C2866011/1758570877.152159, ZOM-567), Android is not |
| Anton committed amount (D05S58U4SAK/1758731100.281734) | $25,000 | $40,000 (post C07C2866011/1758303600.418207, sheet f_6e1d93a0c4b72f85d39a0e) | rev6: Leonard's DM voids the $40,000 SAFE and re-sends at 25; his Sep 26 DM D05S58U4SAK/1758914100.640218 says Anton signed the 25 one; the Completed notice frederick.stone@harmonygames.co/1844354293432320031 the same day; only one SAFE can be completed |
| SciPlay status (C07C2866011/1759248360.377105) | Passed | In talks (thread frederick.stone@harmonygames.co/1842285743246816270 ends Sep 18 with "we'll continue to play") | rev6: Robert's Sep 30 reply: SciPlay's contact called, they're out for this round; template Passed = they've told us no for this round (no channel or writing condition) |
| Hiro Capital status (frederick.stone@harmonygames.co/1844318935449600041) | Passed | Awaiting reply (list "no response as of 09/11") | Edith Vane's pass, cc Hiro's Investment Director PERSON_5282 (base thread 1842278425320449096), Contacts e3a91c07d5b48f26a0c7e314 Partner, Hiro Capital; rev6 drops the template's "check contacts" hint, the mapping stays in the data |
| Reply destination (frederick.stone@harmonygames.co/1844724419788800011) | reply on the thread | mail to the board (frederick.stone@harmonygames.co/1844623441920000059) | the hub withdraws Robert's suggestion |

### Reach table (load-bearing records)

Base records proven with `persona_view.py can-see frederick_stone` (all YES, `plan/cansee.txt`); planned seeds are checked at the injection gate (`check-sql`).

| Record | Service | Can-see | Marker |
|---|---|---|---|
| frederick.stone@harmonygames.co/1842285743246816270 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1842277743427687737 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1842278425320449096 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1842283406259093714 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1843978997950200606 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1843473831194478743 | gmail | YES | LB |
| frederick.stone@harmonygames.co/1843169166284025277 | gmail | YES | LB |
| C096HFA5Z8W/1757716998.377299 | slack | YES | LB |
| C096HFA5Z8W/1758210489.170809 | slack | YES | LB |
| C07C2866011 | slack | YES | LB |
| C07C2866011/1759196326.309469 (rev6 thread root) | slack | YES | LB |
| D05S58U4SAK (rev6, Frederick–Leonard DM) | slack | YES (im member) | LB |
| C0880U9751A (rev6, #zombie-match3d) | slack | YES (private, member) | LB |
| C07C2866011/1758558621.032499 (base Play link) | slack | YES | supporting |
| evt_89381fe5a15b802c5652a9 | gcal | YES | LB |
| evt_25c9ee60d4b6c8f6d39a74 | gcal | YES | LB |
| evt_e59dc0a675d0c407b79acf | gcal | YES | LB |
| f_48247af79428823c3cac92 | gsheets | YES | LB |
| d_175c0d7bc72ed244b944cb | gdrive | YES (owner) | LB |
| planned seeds (hub, template, folder, deck, review event, Brightwater event, Dentsu/Hiro/Brightwater mails; rev6 DM lines, #executives reply, #zombie-match3d post and reply) | gmail/gdocs/gdrive/gslides/gcal/slack | planned: owner, addressee or channel member Frederick | checked at injection |

Feasibility: register write via gsheets_create_spreadsheet / gsheets_values_update into a folder Frederick owns (learnings §31); gdrive_move_file; trello_create_checklist / trello_create_check_item (unscoped); gmail_reply_to_message on a thread in his mailbox — all in Evals/references/tools/catalog.json. Precedence: load-bearing facts only in ● carriers (Ask_Carriers §5/§6b); Contacts job titles and slide notes are supporting, each paired with a ● record (Edith Vane's cc of PERSON_5282 in frederick.stone@harmonygames.co/1844318935449600041; the hub restates the columns). Naturalness: the prompt names the ask, the destinations (Board folder, Leonard's thread, the investor update card by role) and the deadline; it never lists firms, rules, buckets, amounts or traps. Grading devices: ≤ 5 status samples + volume (register_keys_exact over 79 truth keys), access samples, money rows, reply rows, keep-warm rows; no "leaves X alone" row.

### Coherence rail

Every 1a row dispositioned; designed disagreements are dated human claims with later overturning records (T1, T3, T4, T5, T9, T10); companions planned per section 11; ids follow the base schemes (Gmail thread = ms << 20, Slack ts, evt_ + 22 hex, f_/d_ + 22 hex, Trello/Contacts 24 hex, ZOM-567 next free).

## 11 Record plan for /create-injection

| Seed | Service | Id | Time (UTC) | Content (design summary; text is written at injection) |
|---|---|---|---|---|
| Hub / anchor | gmail | frederick.stone@harmonygames.co/1844724419788800011 (+ Robert, Arthur copies) | 2025-09-30T21:05:00Z | Leonard asks Frederick to own the fundraising section; carries K1, K2, K3, K4–K6 quote, K9, K10, K12, K13 quotes verbatim |
| Oct 14 template | gdocs | f_3b9e61c04d7a52e8f1a6c2 | 2025-09-26T18:00:00Z | buckets, as-of, committed/soft-circled, build access ("whether they can get the current internal build"), scope exclusions, Arthur's tracking (K14/K15 quote); rev6 removes the phone-note, check-contacts and latest-amount sentences |
| July template (decoy) | gdocs | f_8d2c47a91e05b3f6d7c418 | 2025-07-08T18:00:00Z | committed = verbal yes from a named investor |
| README | gdocs | f_c61a0e93b7d24f58a2e917 | 2025-09-26T18:30:00Z | file naming for the Board folder |
| Board folder | gdrive | d_5e8a1c3f9b07d2e64a1b93 | 2025-09-26T18:20:00Z | owner Frederick; README inside |
| Draft deck | gslides | f_a47d0e2c95b18f63e2c0d5 | 2025-09-27T17:00:00Z | slide 9 text: table columns |
| Review event | gcal | evt_9c41e7a2d05b38f6e1a7c4 (Leonard + Frederick copies) | created 2025-09-30T21:00:00Z, start Oct 6 | description: bring the sheet link |
| Brightwater call | gcal | evt_2f86b0d4c9e17a35b64e0d (Leonard + Frederick copies) | 2025-09-25T15:30:00Z | "Ilse Marrow and Leonard Hayes" |
| Angel post | slack | C07C2866011/1758303600.418207 | 2025-09-19T17:40:00Z | Paul $50K and Anton $40K "are in" |
| Arthur aside | slack | C07C2866011/1759168800.117903 | 2025-09-29T18:00:00Z | non-authoritative suggestion |
| SciPlay reply (rev6) | slack | C07C2866011/1759248360.377105 (thread C07C2866011/1759196326.309469) | 2025-09-30T16:06:00Z (Sep 30 9:06am PT) | Robert: SciPlay's contact called him this morning, they're out for this round; root counters updated (Q01) |
| Anton revised (rev6) | slack | D05S58U4SAK/1758731100.281734 | 2025-09-24T16:25:00Z | Leonard to Frederick: Anton down to 25, voiding the 40 SAFE and re-sending at 25 |
| Anton signed (rev6) | slack | D05S58U4SAK/1758914100.640218 | 2025-09-26T19:15:00Z | Leonard: Anton signed the 25 one |
| Play tester gap (rev6) | slack | C0880U9751A/1759274400.518306 (+ Leonard reply C0880U9751A/1759276080.094417) | 2025-09-30T23:20:00Z / 23:48:00Z | Arthur: the Play tester list (Karthic, the three Dentsu addresses) was never attached to the internal test track, TestFlight fine; ZOM-567 shows them as added; he'll attach it when he pushes tomorrow's build; Leonard: ping me when it's live |
| Signing completed (Anton) | gmail | frederick.stone@harmonygames.co/1844354293432320031 | 2025-09-26T19:02:00Z | envelope completed, no amount in body |
| Signing reminder (Paul) | gmail | frederick.stone@harmonygames.co/1844610859008000037 | 2025-09-29T15:00:00Z | awaiting Paul's signature |
| Hiro pass | gmail | frederick.stone@harmonygames.co/1844318935449600041 | 2025-09-26T09:40:00Z | Edith Vane declines; cc PERSON_5282 |
| Dentsu "invites out" | gmail | frederick.stone@harmonygames.co/1844347876147200047 | 2025-09-26T17:20:00Z | Leonard: invites out to all three |
| Brightwater follow-up | gmail | frederick.stone@harmonygames.co/1844276782694400053 | 2025-09-25T22:30:00Z | deck sent; partner meeting next |
| Robert board mail | gmail | frederick.stone@harmonygames.co/1844623441920000059 | 2025-09-29T18:20:00Z | suggests mailing the board |
| Tester ticket | linear | ZOM-567 + comments | created 2025-09-30T17:10:00Z, comments 17:25Z and 18:40Z | per-firm log: T-Accelerate and Dentsu, TestFlight and Play adds both logged (rev6) |
| Keep-warm rule | trello | comment 68c6b2a4f19e03d7c5a81b2e on 68c5a49e8491a9d7faf869d0 | 2025-09-14T16:20:00Z | passes after a pitch go on the keep-warm checklist |
| Q4 send rule (rev9) | trello | comment 68db03b86054eff7e8e92474 on 68c5a49e8491a9d7faf869d0 | 2025-09-29T22:10:00Z | a checklist per other group; F/up cards in To Do; comment on an existing To Do card; none after a booked call |
| Anel To Do card (rev9) | trello | card 68c99e98737744bd966aed24 (idShort 456, list To Do) + createCard 68c99e98647b81be91f207f2 | 2025-09-16T17:30:00Z | "F/up with Anel after the engine deep dive" (Leonard) |
| Makers call (rev9) | gcal + gmail | evt_6b2e94d0c17a3f58e9d2b1 (Fred) + copies for Leonard, Robert, Arthur; invitation mails to Fred, Robert, Arthur (frederick.stone@harmonygames.co/1844620925337600069) | created 2025-09-29T17:40:00Z; Wed Oct 8 16:00–16:45Z | "Michael Cheung and Leonard Hayes" (booking-page style, as the base and seeded investor calls); Michael Cheung is the Makers Fund partner on f_48247af79428823c3cac92; guest PERSON_9905_EMAIL (unused token) |
| Deck numbers | trello | comment 68d81f30a6c94e2b7d05e1f4 on 67f446b4b0817af30d2d63f6 | 2025-09-27T17:10:00Z | slide takes register size, committed, soft-circled |
| Contacts | contacts | e3a91c07d5b48f26a0c7e314, b72f0d6e19c3a84e5d21f9a0, 5d0e8b31f7a29c64e1b0d3a8 | n/a | Edith Vane (Hiro Capital), Ilse Marrow (Brightwater Games Fund), Karthic R (T-Accelerate Capital, PXLite fund) |

Before SQL (learnings §10–17): census every seeded name (Paul Heydon, Anton Bernstein, Edith Vane, Ilse Marrow, Brightwater) across all services with a positive control ("Grishin Robotics" found in gsheets data.json and gmail 00001934.json); Paul Heydon and Anton Bernstein already show 0 Gmail hits outside the list; "Kestrel" was rejected (3 base Gmail hits, 00013854.json). Collision-check every minted id with `hg.py search lookup` (rev6: the five new Slack ts 1758731100, 1758914100, 1759289460, 1759274400, 1759276080 return 0 base hits). Time every seed after the base events it names (SciPlay Sep 18 mail, Hiro Sep 3 re-intro mail, Dentsu Sep 23 call, T-Accelerate Sep 22 recap). Rev6: Robert's reply (Sep 30 16:06Z) follows Leonard's speedrun root (Sep 30 01:38Z) and stays before the seed bound (2025-10-01T00:00Z); Leonard's Sep 24 DM (16:25Z) precedes the base Frederick–Leonard exchange that day (17:42Z); Arthur's Sep 30 post (23:20Z) follows the ZOM-567 comments (18:40Z). Correction after the platform /injection review of rev1 (advisory 2): the Sep 3 Hiro thread frederick.stone@harmonygames.co/1842278425320449096 is a re-intro email, not a call, so the base holds no Hiro pitch call this round; injection rev2 seeds the call (evt_7d3e19b04a6c25f8e1b9a0, Tue Sep 23 16:00Z, with its invitation mails) that Edith Vane's pass and the keep-warm rule rely on.

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| gcal | INT-11 | invitation mails for the Brightwater call and the Oct 6 review | seed invitation mails in Frederick's and Leonard's mailboxes |
| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment, Slack DM notice, mail digest | INT-03 none (no PR); INT-04/05: seed Arthur-to-Leonard notification mail only if base pattern holds, else record integration_exceptions |
| gdrive | INT-13 | Drive Slack app DM on share | seed the share notice DM to Frederick for the README and template |
| slack | INT-22 | Slack e-mail notifications for mentions | none: seeded posts carry no @mention (rev6 posts name Leonard and Karthic in plain text) |
| trello | INT-21 | no Trello→Slack integration exists | none |
| gmail | none in integrations.json as a source | — | gmail: none |
| contacts, gsheets, gdocs, gslides | not integration sources | — | none |

## 12 Self-test results

Hardness gate (design), verbatim:

```
HARDNESS GATE (extreme (design)): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: skipped (--design: no SQL yet)
  [ok] base_consistency: skipped (--design: no SQL yet)
  [ok] services_injected: skipped (--design: no SQL yet)
  [ok] rows: skipped (--design: no SQL yet)
  [ok] services_carrying_weight: 10 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: skipped (--design: no SQL yet)
  [ok] seeded_ids_exist_in_sql: skipped (--design: no SQL yet)
  [ok] anchors: 1 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 16 fragments; need ≥ 12
  [ok] ask_fragment_services: 9 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 11 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 8 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 79; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 3 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 327; need ≥ 300
  [ok] call_budget: unconditional (verified) floor 558 of 558 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 500 (Long Horizon; plan ~600 for headroom)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 28% (≤ 50%)
  [ok] traps: 20 traps across 7 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 7 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (3 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 7 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 11 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 7 chains with 5 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 9 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 2 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 17 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 8 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 5 writes over 4 services; each must depend on findings
```

Gradable surface: `gradable_surface.py validate` → `GRADABLE SURFACE (01_Gradable_Surface.json): PASS · 17 slots · weight 69 · mechanism share 88.4% (reported, not gated)`; `gradeable-report` → `SURFACE.GRADEABLE PASS · 17 slot(s) · {'GRADABLE': 17}`. Surface revision at /create-injection S4b (design-level fix, re-certified here): ST1's key is the list's spelling `Sciplay` (f_48247af79428823c3cac92 row 81), and V1 (register_keys_exact) is class `delivery`, as the solver contract (oracle_kit `contract.slots`) reads no solver value for a delivery selector.

Hardness v2 (advisory):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      5 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 6 requirements: {'R3': ['DONE1', 'INPUT'], 'R4': ['DONE2'], 'R2': ['CORR', 'ALIAS'], 'R1': ['FILT'], 'R6': ['FOLLOW'], 'R8': ['DUP', 'BOOKED']}  [Part 5 rule 1]
  FLAG       DECISION_FLIP   7 of 9 rules can flip a weight-5 slot; not: ['FOLLOW', 'BOOKED']  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']

Flags (each needs a written disposition; redesign the difficulty, never weaken a fairness link or raise a weight):
  DECISION_FLIP FOLLOW: rule FOLLOW (A15) can flip slots of weight [3], no weight-5 slot
  DECISION_FLIP BOOKED: rule BOOKED (A17) can flip slots of weight [3], no weight-5 slot
```

Trap liveness (advisory, UNCALIBRATED):

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · DESIGN (no SQL: record text unavailable, only manifest-structure flags can fire) · on the Season Pass backtests these are development fixtures, not validation
  hub frederick.stone@harmonygames.co/1844724419788800011 · direct delegations 12 · rule placement: A15 nodes only: ['C5', 'T8'] (mechanism_portfolio); every other node SKIP
  T1   done_gap           breadcrumb  [rule placement SKIP: not an A15 node]
  T2   done_gap           -  [rule placement SKIP: not an A15 node]
  T3   superseding        -  [rule placement SKIP: not an A15 node]
  T4   superseding        -  [rule placement SKIP: not an A15 node]
  T5   scope_alias        -  [rule placement SKIP: not an A15 node]
  T6   exact_predicate    breadcrumb, order  [rule placement SKIP: not an A15 node]
  T7   near_miss_mention  breadcrumb, order  [rule placement SKIP: not an A15 node]
  T8   authority          breadcrumb
  T9   superseding        breadcrumb  [rule placement SKIP: not an A15 node]
  T10  superseding        -  [rule placement SKIP: not an A15 node]
  T11  scope_alias        breadcrumb, order  [rule placement SKIP: not an A15 node]
  T12  scope_alias        breadcrumb  [rule placement SKIP: not an A15 node]
  T13  exact_predicate    breadcrumb  [rule placement SKIP: not an A15 node]
  D1   distractor         -  [rule placement SKIP: not an A15 node]
  D2   distractor         -  [rule placement SKIP: not an A15 node]
  D3   distractor         breadcrumb, order  [rule placement SKIP: not an A15 node]
  D4   distractor         -  [rule placement SKIP: not an A15 node]
  D5   distractor         breadcrumb, order  [rule placement SKIP: not an A15 node]
  D6   distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  D7   distractor         -  [rule placement SKIP: not an A15 node]
  dispositions: 0/16 recorded
```

S9b prior forecast (UNCALIBRATED, pre-registered): ledger id hev_77ceb6bf5eb21f90; V3 E[avg] 0.485–0.508, P(all four difficulty gates) 0.351–0.646 across dependence scenarios; every rule prior Beta(1,1) (no Opus 5.5 records).

Lazy-solver pass (one broad search per service, first hits, no threads, stops early, bulk shortcuts): it reads the hub, the list and #executives history and scores ST5 (LVP, its own thread), AC2 if it opens Linear, RP1, DL1 — 8 of 69 (11.6 %). Leaks found and fixed in the design: (a) the first draft named "Kestrel" for the off-list firm — base hits (00013854.json) — renamed Brightwater; (b) a COMPL rule whose only grade was an undecodable count — dropped; (c) the template no longer names SciPlay, Hiro or Dentsu (rules only).
Literal-value sweep: $25,000 appears only in Anton's trim mail; $50,000 only in the #executives post; "Play internal" only in ZOM-567 and base C096HFA5Z8W/1758677722.184129 (Arthur: needs emails — consistent).
Wording sweep: the template's "signed" never appears in the angel post; "passed" never appears in SciPlay's mail thread.
"The rest stands": the Oct 14 template restates only the committed rule; no later record re-asserts "verbal yes".

### Self-review

1. Re-read Evals/1_Prompt_Eval.md §2.1, §2.2, §3.2 and Evals/0_Injection_Quality_Eval.md Check C against this design.
2–3. Counter-readings, one per QC category and decision point:

| # | Check | Counter-reading (strongest case it fails) | Evidence | Resolution |
|---|---|---|---|---|
| 1 | temporal | a16z's speedrun no (19:30 PT Sep 30) is inside "end of Sep 30 PT", so a16z is Passed | frederick.stone@harmonygames.co/1844748127814183717 | the rev4 template rule: an accelerator decision is not a bridge answer (f_3b9e61c04d7a52e8f1a6c2); In talks |
| 2 | semantic | PXLite could be a distinct fund, so one row undercounts | frederick.stone@harmonygames.co/1843978997950200606 | Contacts 5d0e8b31f7a29c64e1b0d3a8 + list row T-accelerate; T11 |
| 3 | cross-service referential | Robert's rev6 reply sits under a root about a16z speedrun, so it cannot be tied to SciPlay | C07C2866011/1759196326.309469 (root), frederick.stone@harmonygames.co/1842285743246816270 ("-D") | the reply text names Sciplay and "D" (the contact's sign-off in the base thread); one reading |
| 4 | quantitative | committed total could include Paul if "is in" counts as a commitment | C07C2866011/1758303600.418207 | template f_3b9e61c04d7a52e8f1a6c2 defines committed = signed; July template superseded (T9) |
| 5 | state/lifecycle | ZOM-567 open while Arthur is quiet in Oct reads as abandoned | arthur.blake@harmonygames.co status active_sep_2025_quiet_in_oct; L08 | rev6: the ticket logs the adds on Sep 30 and Arthur's later post C0880U9751A/1759274400.518306 says the Play list still needs attaching (Leonard, Oct 1); Todo is consistent |
| 6 | identifier/format | seeded Gmail thread ids could collide or break search | frederick.stone@harmonygames.co/1844724419788800011 | ms << 20 scheme as base; lookup collision check at injection; I06 companions |
| 7 | other | the P&L vs Snowflake cash gap could be "task-touched" | snowflake.FINANCE, Q05 | no cash figure is read or graded; excluded |
| 8 | decision point a16z | count of keep-warm items forks | frederick.stone@harmonygames.co/1844748127814183717 | settled: a16z In talks, so 3 items; KW rows sample SciPlay and Hiro |
| 9 | decision point Play Ventures | the Sep 15 no and the Sep 23 "they didn't respond" contradict | C096HFA5Z8W/1758671737.632949 | Leonard's rev4 correction C096HFA5Z8W/1758817200.730591 reconciles them: Passed |
| 10 | decision point PXLite | register size 80 vs 79 | 5d0e8b31f7a29c64e1b0d3a8 | one firm; truth_keys 79 |
| 11 | decision point Homa | Homa is a publisher, so out of scope | C096HFA5Z8W/1758210489.170809 | Frederick's own "co-dev investment path"; template "investment, including strategic" |
| 12 | decision point Rollic/Metaplay | a careful run includes every call | C096HFA5Z8W/1758130464.175719 | template exclusion; over-application control in the portfolio |
| 13 | decision point Dentsu access | ZOM-567 logs a Play add for Dentsu, so Android counts | ZOM-567 comment, C0880U9751A/1759274400.518306 | rev6: Arthur, who keeps the log, says on Sep 30 the list was never attached to the internal track; Leonard's reply moves the fix to Oct 1; iOS only |
| 14 | decision point Anton amount | $40K stands because the post and the sheet say so and the completed SAFE is the record | frederick.stone@harmonygames.co/1844354293432320031, D05S58U4SAK/1758731100.281734 | rev6: Leonard voids the 40 SAFE and re-sends at 25 (Sep 24), then says Anton signed the 25 one (D05S58U4SAK/1758914100.640218, Sep 26); the completed notice has no amount; $25,000 |
| 15 | decision point reply destination | Robert's suggestion is newer than the template | frederick.stone@harmonygames.co/1844623441920000059 (Sep 29) vs hub (Sep 30) | the hub is newest and explicit |
| 16 | false-positive check on FILT | Brightwater might be found by everyone, so no trap | evt_2f86b0d4c9e17a35b64e0d | person-titled, one of ~20 September events; Homa sits at a higher tier (failure diversity); the rev5 run found both (hev_9c403cae42eb4df8), so FILT is coverage, not load-bearing |
| 17 | decision point T-Accelerate access | base #executives Sep 22 shows Arthur sending the Play internal-test link, so Android counts | C07C2866011/1758558621.032499, C096HFA5Z8W/1758677722.184129 | the base itself says the link alone does not work ("I have to add them by email"); Arthur's rev6 post says the email list was never attached; iOS only |
| 18 | decision point SciPlay | a no heard by phone is not "in writing", so SciPlay stays In talks | C07C2866011/1759248360.377105, f_3b9e61c04d7a52e8f1a6c2 | rev6 template Passed = "they've told us no for this round", with no writing condition; Robert's reply records the call; Passed |
| 19 | decision point Hiro | without the template's "check contacts" sentence, Edith's personal-address pass may not be Hiro's | frederick.stone@harmonygames.co/1844318935449600041, e3a91c07d5b48f26a0c7e314 | cc Hiro's Investment Director PERSON_5282 (base thread frederick.stone@harmonygames.co/1842278425320449096) and Contacts "Partner, Hiro Capital"; "our games fund"; one reading |
| 20 | false-positive check on INPUT | Opus searches Slack for every angel name and finds the DM at once, so no trap | D05S58U4SAK/1758731100.281734, run_forensics/rev5/precheck/calls.jsonl | the rev5 run searched Slack for Paul, angel, Kevin, Demetri and Fischer only after its mail sweep left Paul open; with the post, the sheet and the completed notice agreeing on Anton, nothing prompts a search; a run that does search is correct (fair) |
| 21 | false-positive check on CORR and DONE2 | a threads-only or keyword search in #executives or Slack-wide returns both corrections | C07C2866011/1759196326.309469, C0880U9751A/1759274400.518306 | possible and fair: an ordinary search finds them (tool-surface proof); the rev5 run ran a threads-only search only for #bridge-pitch (call 34) and no Slack search for TestFlight, Play, Sciplay or Karthic |

4. Load-bearing base values re-read through tools/hg.py and the export this session: list rows and Latest Status (f_48247af79428823c3cac92), SciPlay Sep 12/18 mails, Hiro Sep 3 thread and PERSON_5282 Investment Director signature, T-Accelerate Sep 22 recap, Bubbles PXLite notes, Homa invitation, Arthur's Play note C096HFA5Z8W/1758677722.184129.
5. `hardness_gate.py --design` output is pasted above: HARDNESS GATE (extreme (design)): PASS.

Unresolved: no independent (dual red-team) review of this design — REDTEAM_* is not set (section 13); Opus 5.5 priors hold only the seven rev5 LEAKED records, so every forecast number is UNCALIBRATED; whether a fresh Opus run searches Slack per firm is not knowable before the rev6 pre-check.

```
STAGE GATE scenario: PASS — Task_Authoring/task_inputs · 01_Scenario_Design.md#0cb68361b112 · 01_Hardness_Manifest.draft.json#259235eac2a1 · 01_Gradable_Surface.json#1572eef7453d · 00_Assigments.md#8ae66b700bc2 · __context__#f1f763cb8cb4 · __assignment__#827e8afa884d · __policy__#dc4ab5df3cdd · __gate_policy__#0fc4bb90877f · __review__#b4deb3eb30f6 · blocking 0 · warnings 0 · checks 36
[PASS] assignment.v3_context: Frederick Stone / Co-founder; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 3 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 5/5 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 22/22 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 2/2 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 17/17 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 40/40 items carry a source pointer (min 90%)
[PASS] evidence.record_plan: 32/34 items carry a source pointer (min 80%); unsourced e.g. L493: 'gmail | none in integrations.json as a source | — | gmail: none'
[PASS] evidence.active_speakers: 4/4 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for frederick.stone@harmonygames.co and matches the re-run (105 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 16 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 4 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (7 INT ids, services ['contacts', 'gcal', 'gdocs', 'gdrive', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts ['SL-T27']; trap_catalog ['C01', 'D03', 'D04', 'P01', 'X01', 'X04']
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: red team did not run (missing 01b_Redteam_Review.md, 01b_Redteam_Review.second.md); explicit fallback recorded: Claude (Opus 5.5, the author) ran the lazy-solver pass, the literal and wording sweeps, th
[PASS] surface.valid: 21 slots, weight 79; geometry report-only, never gated: mechanism share 86%, always-pass share 14%
[PASS] forecast.preregistered: prior forecast pre-registered in the ledger: ['hev_77b5a028a20fb6ac', 'hev_77ceb6bf5eb21f90'] (UNCALIBRATED, advisory)
[PASS] revise.intake: revision intake consumes Working_Files/run_forensics/rev5/precheck.node_verdicts.json
[PASS] revise.verdict_dispositions: 7 proposed node verdict(s) dispositioned; 0 CONFOUNDED candidate(s) addressed
[PASS] revise.revision_binding: every export is bound on evidence to the revision it ran on, or marked historical (historical evidence never certifies a revision)
[PASS] evidence.register_run_step: 7/7 items carry a source pointer (min 100%)
[PASS] reach.scenario: 21 scoped load-bearing ids YES for frederick_stone (2 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 21 evidenced counter-readings (of 21 found; need ≥ 18) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.draft.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 Red team (dual)

RED TEAM UNAVAILABLE: REDTEAM_* is not set in this environment (`env | grep REDTEAM_` returns nothing), so `tools/redteam_review.py --mode redteam --dual` cannot run.
RED TEAM FALLBACK: Claude (Opus 5.5, the author) ran the lazy-solver pass, the literal and wording sweeps, the fork sweep in the two-reading table and the policy scores on the real surface; the requester chose a recorded fallback on 2026-11-01 because no reviewer endpoint is configured. This is self-review, not an independent review, and stays in every Unresolved line until a reviewer or the Opus pre-check covers it. Rev6: the platform Opus pre-check of rev5 (Platform_Report/hardness_report1, /hardness score 1) acted as an adversarial reader of rev5; its findings drive section 15. REDTEAM_* is still not set (checked 2026-11-02, count 0); rev6 gets the two blind sweeps (forks; seeded-vs-base coherence) before /prompt.

## 14 Rev4 fork settlement (platform /prompt review of rev3)

The platform `/prompt` review of rev3 (Platform_Report/peompt_report1, prompt sha256 cecfad824fd8, SQL 952e12a9ad7a) scored every prompt dimension 5 except Unique Ground Truth 2 and Cross-Service Coherence 2. Rev4 keeps the prompt and the seven mechanisms and settles every fork in a dated, Frederick-visible record or a template rule (solver `accepted_status` is now empty for all 79 keys).

| Fork (platform id) | Rev3 readings | Rev4 settlement | Record |
|---|---|---|---|
| Homa in scope (F1) | co-dev/publishing out vs strategic in | template: a firm pitched the bridge counts even when co-dev or publishing was also on the table; Leonard's Sep 17 mail pitched extension funding | f_3b9e61c04d7a52e8f1a6c2, frederick.stone@harmonygames.co/1843552279434086285 |
| Play Ventures (F2, coherence) | Passed vs Awaiting reply | Leonard's Sep 25 correction: the Sep 15 no was their reply to Griffin; template counts a no sent to Griffin | C096HFA5Z8W/1758817200.730591 |
| connector outreach (F3) | Awaiting reply vs Not contacted for Triptyq, Turkven, Harlem Capital, General Catalyst | template: outreach by anyone introducing us counts as ours | f_3b9e61c04d7a52e8f1a6c2, C096HFA5Z8W/1757716998.377299 |
| a16z (F4) | Passed + keep warm vs In talks | template: an accelerator decision is not a bridge answer; the interview counts as a call | f_3b9e61c04d7a52e8f1a6c2, evt_e802a3583ee79ff6087f76 |
| Paul soft-circled (F5) | $50K vs $0 | template: a yes one of us wrote down counts | f_3b9e61c04d7a52e8f1a6c2, C07C2866011/1758303600.418207 |
| angels' bucket (F6) | In talks vs other | template: angels who said yes are In talks, Build access blank | f_3b9e61c04d7a52e8f1a6c2 |
| last two-way contact (F7, F8) | our trailing reply; no window | column dropped from the template, slide 9 and the gradable surface | f_3b9e61c04d7a52e8f1a6c2, f_a47d0e2c95b18f63e2c0d5 |
| 1AM Gaming (F9) | March Gaming Fund Passed vs unmapped | Leonard's Sep 8 post: 1AM Gaming is the March Gaming Fund row and passed | C096HFA5Z8W/1757365500.384216 |
| Mattel hidden exchange (coherence) | status differs with Leonard-only mail | Leonard's Sep 26 post: RFP/partnership only, not pitched the bridge; template: only bridge outreach counts | C096HFA5Z8W/1758927000.205874 |
| solver two-reading firms not yet flagged | BITKRAFT, Superplay, Treo VC, Transcend Fund, Acterra, Index Ventures | template: only this round counts (the list's Status/comment columns, earlier answers and plans do not); Awaiting reply holds even if they wrote back; an advisor's read is not a firm's answer | f_3b9e61c04d7a52e8f1a6c2, f_48247af79428823c3cac92 |
| keep-warm scope | earlier-round calls (Play 2023, Lakestar May 2025) | comment now says "pitched them on a call or meeting this round" | 68c64270d660c977c4696986 |
| Leonard-only calls (incl. the Sep 29 "Turkish VC") | calls Frederick cannot see | template: a call counts only when it's on Fred's calendar, also for In talks | f_3b9e61c04d7a52e8f1a6c2 |
| reply firm count (author blind sweep) | 79 / 77 / 74 | Board Deck comment "every row, angels included"; slide 9 "Firms on Fred's sheet" | 68d81f30a6c94e2b7d05e1f4, f_a47d0e2c95b18f63e2c0d5 |
| row 69, Initial Capital (author blind sweep) | Latest Status notes as answers or not | template: Latest Status notes count as written; "don't do bridge" is a no | f_3b9e61c04d7a52e8f1a6c2 |
| Treo VC contact date (author blind sweep) | Sep 2 warm-up vs kickoff day | Leonard's Sep 3 post; template: the kickoff day counts | C096HFA5Z8W/1756942260.617302 |
| SVB call, Brightwater pitch, Dentsu access format, Anton's amount (author blind sweep) | open wording | template excludes banks, fixes the access wording and applies "latest amount" to both columns; Brightwater's follow-up names the bridge | f_3b9e61c04d7a52e8f1a6c2, frederick.stone@harmonygames.co/1844276782694400053 |
| Initial Capital (platform /prompt review of rev4, F1) | Awaiting reply vs Not contacted | Leonard's Sep 9 post: pinged them on LinkedIn about the bridge, they answered (won't lead, might write a small check) | C096HFA5Z8W/1757442000.492583 |
| tester records (platform /prompt review of rev4, DR2) | ZOM-567 vs Arthur's Sep 22 #executives invites | T-Accelerate's two adds dated Sep 22; Dentsu TestFlight Sep 26, Play waits on Google account addresses | lc_94eb35d962cfbdd31e1bd496, lc_b549f3057640a5eb08f7581e |
| a16z feedback and Dentsu identity (author coherence sweep) | the speedrun feedback mentions the bridge; Dentsu team vs list row | template: program feedback isn't a bridge answer (only the bridge thread or #bridge-pitch); contact Ryo Ishikawa, Dentsu Ventures | f_3b9e61c04d7a52e8f1a6c2, a4c2e9f07b31d85e6c0f1b29 |

Truth after rev4 (solver/truth.json): 79 rows (Passed 8, In talks 9, Awaiting reply 14, Not contacted this round 48); an author-run blind fork sweep classified all 79 rows independently and, after the fixes above, matches this table row for row; committed $25,000; soft-circled $50,000; keep warm London Venture Partners, Sciplay, Hiro Capital; Dentsu iOS only; T-accelerate iOS and Android. The graded surface keeps its 17 slots and weight 69; the seven mechanisms and their controls are unchanged.

## 15 Revision intake (S0r): rev6 from the rev5 Opus pre-check

Verdicts consumed: `Working_Files/run_forensics/rev5/precheck.node_verdicts.json` (from `/create-hardening` MODE B, report `Working_Files/01a_Hardening_Report.md`). The run is one platform Opus 5.5 run (`06_PreCheck_Trajectory/trajectory.json`, sha 885ed68d96e2), bound BOUND:rev5 on discriminating content and v3-valid. It is evidence for rev5 only. It is historical for rev6 and certifies nothing about rev6. Platform `/hardness` on it: FAIL, score 1, Too easy (`Platform_Report/hardness_report1`).

| Node | Runs | Proposed verdict | Disposition | Evidence | Rev6 change |
|---|---|---|---|---|---|
| DONE1 | precheck | BYPASSED → LEAKED | keep | precheck call 11 (template read: "Completed notice"), call 35 (`docusign` search), call 101 (Paul soft-circled 50000) | unchanged: the definition must stay for UGT (Paul's relayed yes, fork F5); kept as coverage, not load-bearing |
| INPUT | precheck | BYPASSED → LEAKED | rebuild | precheck call 40 (Sep mailbox listing), call 61 (Anton's "SAFE amount" thread), call 101 (25000) | Anton's mail removed (purge P3); the change is now in Leonard's DM D05S58U4SAK (Sep 24, Sep 26); the template's "latest amount" sentence goes (P1) |
| DONE2 | precheck | LEAKED | rebuild | precheck call 93 (Linear search), call 94 (ZOM-567 comments with the "not added yet" caveat), call 101 (Dentsu iOS only) | ZOM-567 now reads as done for both firms (P4); Arthur's Sep 30 #zombie-match3d post C0880U9751A/1759274400.518306 is the missing piece; T-Accelerate becomes iOS only |
| CORR | precheck | BYPASSED → LEAKED | rebuild | precheck call 34 (threads-only #bridge-pitch search returned Robert's reply), call 101 (SciPlay Passed), call 106 (keep-warm item) | Robert's #bridge-pitch root and reply removed (P2); his reply now sits under Leonard's speedrun post in #executives, C07C2866011/1759248360.377105; the template's #bridge-pitch phone rule goes (P1) |
| ALIAS | precheck | LEAKED | keep | precheck call 55 (Edith Vane's mail), call 56 (Contacts lookup), call 105 (Hiro Capital item) | the template's "check contacts" hint goes (P1); the alias stays in the data |
| FILT | precheck | BYPASSED → LEAKED | keep | precheck call 27 (full Sep 3-30 calendar listing), call 59 (Contacts "Ilse"), call 101 (Homa and Brightwater rows) | unchanged (coverage); moving it further would make it a riddle |
| FOLLOW | precheck | LEAKED | keep | precheck call 17 (card read with its rule comment), calls 103-106 (Keep warm checklist) | unchanged; the checklist now depends on CORR's moved record for SciPlay |

No proposal carries a CONFOUNDED flag; none is assigned. The tool's BYPASSED came from its register decoder missing suffixed names ("Paul Heydon (angel)", "Homa (not on list)"); the write payload (precheck event 388) settles each as met, so each is LEAKED.

## 16 Rev6 decisions: purge, rebuild, routing

Purge (decided):
- P1, template sentences:
  - "A pass one of us heard by phone counts once it is written in #bridge-pitch";
  - "A partner writing from their own address counts for their firm. If the name doesn't ring a bell, check contacts and the earlier threads.";
  - "For both, use the latest amount the investor gave us.";
  - "in writing" in Passed.
- P2: K8 root C096HFA5Z8W/1759161600.226431 and reply C096HFA5Z8W/1759184040.552871 (and the root counter update on C096HFA5Z8W/1757716998.377299).
- P3: Anton's mail frederick.stone@harmonygames.co/1844162278195200023.
- P4: the ZOM-567 Dentsu caveat.

Kept for UGT, not difficulty (rev4 fork settlements, section 14):
- the speedrun rule with its tail;
- "as one of us wrote it down";
- the Griffin/advisor rule;
- the population and exclusion rules;
- the Latest Status rule.

Rebuild (decided): RB1 INPUT, RB2 CORR, RB3 DONE2, as in the table. Hardness v2 moves only; no row, item or step is added.

Routing:
- universe changes → S5a onward (this design) and `/create-injection` rev6;
- prompt-side defects → none (the prompt is unchanged, sha cecfad824fd8);
- OE/rubric → T-Accelerate build access changes to "iOS only"; build access, Anton's amount and SciPlay cite new deciding records (route to `/create-oe-writing` and `/create-rubric-writing` when they run).

Values after rev6: 79 firms; committed $25,000; soft-circled $50,000; Keep warm London Venture Partners, Hiro Capital, Sciplay; Dentsu iOS only; T-Accelerate iOS only (was iOS and Android). Statuses unchanged (Passed 8, In talks 9, Awaiting reply 14, Not contacted this round 48).

Design forecast (pre-registered, UNCALIBRATED): `hev_77b5a028a20fb6ac`, P(all four V3 gates) 0.233-0.769, E[avg] 0.626-0.655 against the 0.85 cap. The prior design forecast was hev_77ceb6bf5eb21f90 and the rev5 posterior hev_7b7855d894bf400b.

## 17 Rev7 job change (platform /prompt of rev6: dataset-duplicate gate)

The platform `/prompt` review of rev6 (Platform_Report/prompt_report4, prompt cecfad824fd8, SQL 848189443008) scored all 20 content dimensions 5, Unique Ground Truth and Cross-Service Coherence included, with 30 forks all settled. It failed only on the new STEP 0.6 gate, Originality — Dataset Duplicate. Meaning similarity was 0.804 to an L12 task by another contributor (Frederick / Finance: Leonard hands Fred the fundraising part of the Oct 14 board pre-read, every firm on the 2025 list in a status, totals back), and 0.729 / 0.720 to two completed Frederick tasks on the same handoff. The report says rewording will not move a meaning score, so the job had to change. The requester chose the Q4 investor update direction on 2026-11-02.

| Element | Rev6 (board pre-read) | Rev7 (Q4 update send list) | Record |
|---|---|---|---|
| Hub | "own the fundraising section of the Oct 14 pre-read" | "take the send list for the Q4 investor update off my plate"; reply with how many firms and angels are in each group; Robert's idea (send to everyone on the 2025 list) withdrawn | frederick.stone@harmonygames.co/1844724419788800011 |
| Rules doc | Oct 14 board template (buckets, money, build access) | "Q4 investor update - send list": same population, status and build-access rules; groups New investor (signed SAFE, with amount), In talks (incl. unsigned angels with their amount), Awaiting reply, Keep warm (passed after a pitch call); email-only passes and uncontacted firms stay off | f_3b9e61c04d7a52e8f1a6c2 |
| Decoy | July board template (committed = verbal yes) | Q3 (July) send list (new investor = a yes with an amount) | f_8d2c47a91e05b3f6d7c418 |
| What counts as signed | template sentence | Leonard's #executives note (K17): new investor only once the DocuSign Completed notice is in | C07C2866011/1758911700.336170 |
| Folder / README | Board - Oct 14 2025; "Fundraising - Oct 14 board" | Q4 2025 investor update; "Q4 update - send list" | d_5e8a1c3f9b07d2e64a1b93, f_c61a0e93b7d24f58a2e917 |
| Deck | board deck, slide 9 lists the table's columns | draft Q4 update deck, the bridge slide says what each group gets (K11) | f_a47d0e2c95b18f63e2c0d5 |
| Board Deck card | three slide numbers (K10) | removed | — |
| Deliverable | 79-row register with status, build access, committed, soft-circled | 26-row send list with group, amount, build access; Keep warm checklist; reply with group counts | solver/truth.json |

The traps keep their records and placements:
- DONE1 now decides Paul's group (unsigned, so In talks, not New investor);
- INPUT decides Anton's amount ($25,000);
- DONE2 decides build access (T-Accelerate and Dentsu iOS only);
- CORR and ALIAS decide SciPlay and Hiro as Keep warm;
- FILT puts Homa and Brightwater on the list;
- FOLLOW writes the Keep warm checklist.

Truth (rev7): 26 on the list. New investor 1 (Anton Bernstein, 25,000). In talks 8 (Paul Heydon 50,000, GFR Fund, Andreessen Horowitz, NCsoft, Homa, Brightwater Games Fund, plus Dentsu Ventures and T-accelerate at iOS only). Awaiting reply 14. Keep warm 3 (London Venture Partners, Hiro Capital, Sciplay). The 53 others stay off: 5 email-only passes and 48 not contacted.

## 18 Rev9 revision: horizon and pass rate from the rev8 baseline

Intake: the six Opus 5.5 baseline trajectories of rev8 (SQL 4895577edea8, prompt b5ea6f0ff28c), placed by the author in `07_Baseline_Trajectories/` and copied to `run_forensics/rev8/baseline/runs/` (ledgers `run-N/calls.jsonl`, `summary.json`). Each export stays bound to rev8.

| Run | Counted MCP calls (no Bash, no errors, no exact repeats) | Estimated weighted pass | Misses |
|---|---|---|---|
| 1 | 82 | ~75% | SciPlay In talks (CORR), counts 8/2 off |
| 2 | 60 | ~75% | SciPlay In talks |
| 3 | 70 | 100% | none |
| 4 | 72 | ~68% | SciPlay In talks, Anton $40,000 (INPUT) |
| 5 | 69 | 100% | none |
| 6 | 83 | ~75% | SciPlay In talks |

Average 72.7 counted calls is under Long Horizon (100+, `Evals/references/rules/scoring.json`, Trajectory - Task Type & Horizon). When a rollout scores 100% that rollout's count is used, and runs 3 and 5 sit at 70 and 69. The estimated average pass (~82%) is under the 85% Medium cap but above the author's 80% target. Landed: CORR 4/6, INPUT 1/6; DONE1, DONE2, ALIAS and FILT 0/6.

Cause: Opus reads in bulk (gmail_get_messages_batch, channel histories, one calendar listing for Sep 3 - Oct 1, the whole 2025 list in one range) and writes the sheet in one values_update. The only per-entry writes were 2-3 keep-warm check items. Forcing reads per entry would mean padding.

Decision. The prompt stays b5ea6f0ff28c, unchanged. The per-entry follow-through moves onto the Trello card the prompt already names ("do what he asked on the Existing Investor Update card in Trello"):
- Hub sentence: "Then do what I put on the Existing Investor Update card in Trello." (frederick.stone@harmonygames.co/1844724419788800011).
- Leonard's Sep 29 comment 68db03b86054eff7e8e92474 on card 68c5a49e8491a9d7faf869d0 asks for four things:
  - Besides the Keep warm checklist (his Sep 13 comment), a checklist for each other group (New investor, In talks, Awaiting reply), with one item per firm or angel.
  - An "F/up with" card in To Do for everyone In talks or Awaiting reply.
  - A comment on the existing card instead, if one is already in To Do.
  - No card for anyone with a call or meeting on Fred's calendar after Sep 30.
- Per run that is 4 checklists, 26 items, 19 cards and 1 comment: 50 single-object writes. The catalog has no batch write for check items or cards, and every rev8 run made one trello_create_check_item call per item. Rev8 runs made 3-4 Trello writes. Projected counted calls per run: the rev8 non-Trello calls (57-80), plus 50 writes, plus 3-5 reads (To Do list, Fred's calendar after Sep 30), for about 110-135. Run 2, the lowest, projects to about 110.
- Two new traps sit on the new per-entry work. They lower the pass rate and the chance of a 100% run:
  - DUP: Leonard's open To Do card 68c99e98737744bd966aed24, "F/up with Anel after the engine deep dive", names only NCsoft's partner. The 2025 list's Partner column has Anel Ceman for NCsoft, whose Latest Status is the engine follow-up.
  - BOOKED: Dentsu's base Oct 1 meeting (evt_3671b9a924ccba550e51fa) and the seeded Oct 8 call "Michael Cheung and Leonard Hayes" (evt_6b2e94d0c17a3f58e9d2b1), which names only Makers Fund's partner (the 2025 list's Partner column maps him). Both are outside the Sep 3 - Oct 1 window every rev8 run listed.
- Existing misses now cost more. A run that misses SciPlay's pass also puts SciPlay on the In talks checklist and gives it a follow-up card. A run that misses Hiro's pass gives Hiro a card.
- The sheet, the groups (26: 1 / 8 / 14 / 3), the amounts, build access and the reply are unchanged. Truth f3dd0b9de6e2d3f8 adds the Follow-up field: 19 card, 1 comment (NCsoft), 2 none (Dentsu Ventures, Raine Ventures).

Padding check: every new write is asked for in a seeded record (Leonard's comment), on the card the prompt names, one per send-list entry, each with a purpose (ticking off the sends, chasing replies). Each of the three new records decides an outcome:
- the Sep 29 comment is the rule;
- the Anel card decides NCsoft;
- the Makers call decides Makers.

Coherence:
- Anel card. It is idShort 456 (the base board's highest is 455, the Existing Investor Update card, made Sep 13), created by Leonard on Sep 16. Leonard made 420 of the board's 444 base cards. The To Do list holds one other open card (Playable Kickoff, not a firm).
- Homa's base card. "[USERNAME_34488] send material [PERSON_NAME_0854]" is in Doing, not To Do, so the To Do rule does not reach it.
- Makers status. Makers stays Awaiting reply: its list note is "Reached out - no response as of 09/11", the doc's Awaiting reply holds "even if they've written back", and In talks needs a call that has happened (Oct 8 is future at Sep 30).
- Makers call. It follows the seeded Hiro and Brightwater calls: a booking-page event titled by person ("Michael Cheung and Leonard Hayes"), copies on the four founders' calendars and invitation mails to Fred, Robert and Arthur (base_check INT-11 clean). "Michael Cheung" occurs nowhere in the base except the 2025 list's Makers Fund row (searched gmail, slack, gcal, contacts, gdocs, trello: 0 hits). The guest address is the unused token PERSON_9905_EMAIL. All four copies share one RSVP state (Leonard accepted as organizer, everyone else needsAction), as the review event does and as base events do.

| # | Counter-reading (rev9) | Record | Settled by |
|---|---|---|---|
| 1 | the To Do rule covers any open card for the firm, so Homa's Doing card counts | Homa base card in Doing | "already has a card in To Do" |
| 2 | Makers' Oct 8 call makes Makers In talks | evt_6b2e94d0c17a3f58e9d2b1 | send-list doc: In talks = "we've had a call or meeting", as of end of Sep 30 |
| 8 | "Michael Cheung" could be someone outside the send list | evt_6b2e94d0c17a3f58e9d2b1, f_48247af79428823c3cac92 | the only Michael Cheung in the universe is the Makers Fund partner on the 2025 list |
| 3 | Dentsu's Oct 1 meeting appeared after the clock | evt_3671b9a924ccba550e51fa, created 2025-10-01T00:02:03Z (Sep 30 5:02pm PT) | made on Sep 30 Pacific; Leonard's hub names "the Dentsu meeting" |
| 4 | "Anel" could be someone at another firm | f_48247af79428823c3cac92 (NCsoft row: Partner Anel Ceman) | the name occurs nowhere else in the universe (search: no other Anel) |
| 5 | Keep warm or New investor entries also need follow-up cards | 68db03b86054eff7e8e92474 | "everyone In talks or Awaiting reply" |
| 6 | the new checklists repeat the Keep warm entries | 68db03b86054eff7e8e92474 | "besides the Keep warm one, give every other group ... its own checklist" |
| 7 | a comment on the Anel card must carry particular wording | 68db03b86054eff7e8e92474 | "comment on that card instead": any comment there is the follow-up |

# Scenario Design — frederick_bridge_pipeline · design only · contains no prompt, OE or criterion text

Built by `Working_Files/plan/build_scenario.py` (manifest + surface) and assembled by
`Working_Files/plan/assemble_design.py`. Every probability below is UNCALIBRATED.

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe | key `synthcut`, label hg4-synth-sep30cut v16, clock line `Clock: 2025-10-01T07:00:00Z (Oct 1, 2025 00:00 PT, synth-cut)`, seed bound `freeze_utc` 2025-10-01T00:00:00Z, `shutdown_rules_apply` false |
| Persona | Frederick Stone, Co-founder, frederick.stone@harmonygames.co (roster `frederick_stone`); today = Wednesday Oct 1, 2025 |
| Business function → Evals category | Executive → Founders / Exec / Strategy (`Evals/references/rules/task_categories.md`) |
| Competency · skill · type · mode | Corporate Ops · Retrieval · long-horizon · medium (cap: corrected weighted average < 85 %; S0 design target ≤ 77 %) |
| Author targets (requester, 2026-11-01 chat) | over 100 tool calls in each run; average weighted pass under 80 %. Design target therefore E[avg] ≤ 72 % (manifest `author_targets`) |
| Horizon / profile | `horizon: Long Horizon` → `effective_profile: extreme`; no profile or volume exception (the 502-call budget below is honest, so none is needed) |
| Theme screen | fundraising / board pre-read; no bio-adjacent theme |

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
| Thread counters after a seeded reply | quantitative | reply_count / latest_reply on C096HFA5Z8W/1757716998.377299 change | C096HFA5Z8W/1757716998.377299 | Q01, Q03 | repaired by companion UPDATE in the SQL (hazard_acknowledgements Q01) |
| Same message in several mailboxes | quantitative | cc'd copies of seeded mails must match | frederick.stone@harmonygames.co/1844724419788800011 | Q10 | avoid: each seeded mail written once per mailbox with identical body |
| Duplicate calendar copies | quantitative | Dentsu Oct 1 twice | evt_eeca6fc7670fe1acd94440 | Q11 | excluded: base rows untouched |
| Open Linear issues assigned to quiet people | state/lifecycle | ZOM-567 assignee Arthur is `active_sep_2025_quiet_in_oct` | arthur.blake@harmonygames.co, ZOM-567 | L08 | dated claim: created Sep 24 and commented Sep 29 while active |
| Stale list status | state/lifecycle | Latest Status "as of 09/11" vs later mail | f_48247af79428823c3cac92 | L08 none; human claim | designed: T10 (dated human column overturned by frederick.stone@harmonygames.co/1842283406259093714) |
| Mailbox alias in file names | identifier/format | frederick@ files vs frederick.stone@ ids | frederick.stone@harmonygames.co/1842285743246816270 | I03 | avoid: seeds use the roster address |
| Resource-owned files | identifier/format | list owner `Resource: 7240535625619857401` | f_48247af79428823c3cac92 | I14 | accepted: read-only population source, never a write target |
| Re:/Fwd: without references | identifier/format | seeded replies carry in_reply_to/references | frederick.stone@harmonygames.co/1844724419788800011 | I06 | avoid: companions set |
| Other: P&L vs Snowflake cash | other | cash differs ~$37K/month (Atlas Part B) | snowflake.FINANCE | Q05 | excluded: no cash or runway figure graded |

Known data issues (references/known_data_issues/synthcut.md, read at design per learnings §44, checked against the touched list f_48247af79428823c3cac92 and threads; no load-bearing fact, trap or graded slot rests on a card's "Don't grade" value):
- SC-33 (watch, investor sheet lists Acterra twice): touched by V1 (register size). Relied-on side: the incorporated template rule f_3b9e61c04d7a52e8f1a6c2 ("one row per name on the 2025 game investor list, angels included … a repeated name is still one row"), which counts Acterra (rows 71/86), Progression Fund (22/23) and BITKRAFT Ventures (32/33) once each in f_48247af79428823c3cac92; "Treo/Treeo" is a Slack spelling (C096HFA5Z8W/1756941551.539229), not a list duplicate. No raw sheet count is graded.
- SC-34 (row 82 labeled Superplay, contents Supercell): row 82's status is never sampled; it is one register row under either name (f_48247af79428823c3cac92).
- SC-9 (Play Ventures rejected vs no reply): never graded; both statuses accepted (C096HFA5Z8W/1757955553.793529, C096HFA5Z8W/1758671737.632949).
- SC-10 (LVP meeting date Sep 7 vs Sep 9): no date graded; LVP's status comes from its own thread frederick.stone@harmonygames.co/1842277743427687737; the call is evt_e59dc0a675d0c407b79acf (Sep 9).
- SC-40 (July board date 14 vs 16): the seeded July template says "for the Jul 16 board" (f_8d2c47a91e05b3f6d7c418), the card's safer value; not graded.
- SC-49 (founder count, Frederick's role): no founder count or founder status is graded; the role review rests on activity (evt_bd61f3209523d19fdd6ba2, C096HFA5Z8W).
- SC-3 / SC-73 (runway, monthly burn): no cash, runway or burn figure is read or graded (snowflake.FINANCE untouched).
- SC-7 (channel membership): membership is used only for reach (C096HFA5Z8W, C07C2866011), never graded.

Sibling-defect sweep: other list rows whose Latest Status is stale (Makers Fund, Raine Ventures, BBQ Capital in f_48247af79428823c3cac92) are read as "Awaiting reply" unless a later record says otherwise; Play Ventures (C096HFA5Z8W/1757955553.793529 vs C096HFA5Z8W/1758671737.632949) carries a base contradiction and is never graded (both statuses accepted).

## 1b Active speakers

Status from activity.json (synthcut KB) at the clock for leonard.hayes@harmonygames.co, robert@harmonygames.co, arthur.blake@harmonygames.co and frederick.stone@harmonygames.co.

| Person | Email | status_at_clock | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | hub mail (Sep 30 21:05Z), template docs, card comments, angel post (Sep 19), Dentsu and Brightwater follow-ups |
| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | phone-note root (Sep 29) and SciPlay thread reply; board-mail suggestion (Sep 29) |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | ZOM-567 and its Sep 29 comment; #executives aside (Sep 29) |
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
- Shortcut audit: the list's Latest Status (f_48247af79428823c3cac92) stops at 09/11; Leonard's tracker C096HFA5Z8W/1757345124.546449 stops at Sep 8; `gmail_search` returns ids only; channel history omits replies (SciPlay's pass lives in a reply under C096HFA5Z8W/1757716998.377299). No bulk call returns a firm's state at Sep 30.
- Predicate and house rule: template (planned f_3b9e61c04d7a52e8f1a6c2) buckets Passed / In talks / Awaiting reply / Not contacted this round, as of end of Sep 30 PT; house rule overriding the natural reading: a phone pass counts once written in #bridge-pitch (C096HFA5Z8W).
- Dual regime: July template (planned f_8d2c47a91e05b3f6d7c418) committed = verbal yes; Oct 14 template = signed SAFE.
- Boundary records: Homa (off list, evt_89381fe5a15b802c5652a9), Brightwater (off list), PXLite/T-Accelerate (one firm, frederick.stone@harmonygames.co/1843978997950200606), Metaplay and Rollic (out: frederick.stone@harmonygames.co/1832208184829815962, C096HFA5Z8W/1758130464.175719), duplicate list rows (f_48247af79428823c3cac92).

## 3 Hidden authorities

| Id | Authority (by what it governs) | Home | Decoy | decoy_scope | Governs | Findability proof |
|---|---|---|---|---|---|---|
| H1 | the board pre-read template, fundraising section | gdocs planned f_3b9e61c04d7a52e8f1a6c2 (Leonard, Sep 26) | gdocs planned f_8d2c47a91e05b3f6d7c418 (July lot; committed = verbal yes) | lot: Q2 July board vs Q3 Oct 14 board | R2, R3, R4 | `hg.py search gdocs "board pre-read"` returns both once seeded (checked at injection); named by the hub (K3) |
| H2 | the keep-warm rule on the Existing Investor Update card | trello comment planned 68c6b2a4f19e03d7c5a81b2e on 68c5a49e8491a9d7faf869d0 | trello 663ea0fc3f231e879cefd5e8 "Investor Update" (Apr 2025) | issuer: existing investors' quarterly update vs bridge prospects | R6 | base card 68c5a49e8491a9d7faf869d0 found by its title; named by the hub (K9) |

`governs` do not overlap (H1 f_3b9e61c04d7a52e8f1a6c2, H2 68c5a49e8491a9d7faf869d0); both homes are rarely-opened services (gdocs, trello); each decoy shares the search terms ("board pre-read", "investor update") with no self-advertising title word (the July template is dated by its body, not "old" or "draft").

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Leonard's board pre-read email | frederick.stone@harmonygames.co/1844724419788800011 (planned) |

Hub: the anchor itself (frederick.stone@harmonygames.co/1844724419788800011), Leonard's voice, delegating by role (template, list, card, deck card, folder README, review event) and never listing locations of evidence.

| Fragment | Service · container | Requirement | Delegated by | Delegation quote (verbatim, to appear in the delegating record) |
|---|---|---|---|---|
| K1 | gmail · frederick.stone@harmonygames.co/1844724419788800011 | R7 | A1 | "reply here with the numbers the fundraising slide needs" |
| K2 | gmail · frederick.stone@harmonygames.co/1844724419788800011 | R5 | A1 | "put the sheet in your Board - Oct 14 2025 folder" |
| K3 | gmail · frederick.stone@harmonygames.co/1844724419788800011 | R1 | A1 | "every firm on the 2025 game investor list, plus anyone we've had a call with since the Sep 3 kickoff who isn't on it" |
| K4 | gdocs · f_3b9e61c04d7a52e8f1a6c2 | R2 | A1 | "use the buckets and definitions in the board pre-read template" |
| K5 | gdocs · f_3b9e61c04d7a52e8f1a6c2 | R3 | A1 | same quote (template money definitions) |
| K6 | gdocs · f_3b9e61c04d7a52e8f1a6c2 | R4 | A1 | same quote (template build-access definition) |
| K7 | gsheets · f_48247af79428823c3cac92 (base) | R1 | A1 | "every firm on the 2025 game investor list" |
| K8 | slack · C096HFA5Z8W/1759161600.226431 (planned) | R2 | K4 | "a pass one of us heard by phone counts once it is written in #bridge-pitch" |
| K9 | trello · 68c5a49e8491a9d7faf869d0 + comment 68c6b2a4f19e03d7c5a81b2e | R6 | A1 | "whatever the Existing Investor Update card says to do for firms that pass, do that too" |
| K10 | trello · 67f446b4b0817af30d2d63f6 + comment 68d81f30a6c94e2b7d05e1f4 | R7 | K1 | "the Board Deck card says which numbers the slide takes" |
| K11 | gslides · f_a47d0e2c95b18f63e2c0d5 (planned) | R1 | K10 | "Slide 9 of the draft deck lists the table's columns" |
| K12 | gcal · evt_9c41e7a2d05b38f6e1a7c4 (planned) | R5 | A1 | "I put Monday's review on your calendar" |
| K13 | gdocs · f_c61a0e93b7d24f58a2e917 (planned README) | R5 | K2 | "the README in that folder says how to name it" |
| K14 | linear · ZOM-567 (planned) | R4 | K6 | "build access is whatever Arthur's investor tester ticket in Linear shows" |

Amendment in a different service, later: the Oct 14 template (gdocs f_3b9e61c04d7a52e8f1a6c2, Sep 26) amends the July template's committed rule (f_8d2c47a91e05b3f6d7c418, Jul 8); the rest of the July buckets stand. Non-authoritative distractors: Arthur's aside (C07C2866011/1759168800.117903), Robert's board-mail suggestion (frederick.stone@harmonygames.co/1844623441920000059), the April Investor Update card (663ea0fc3f231e879cefd5e8).

## 5 Chains and trap register

| Trap | Family | Records | Req | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | done_gap | C07C2866011/1758303600.418207, frederick.stone@harmonygames.co/1844610859008000037 | R3 | Paul Heydon committed $50,000 | reminder: SAFE awaiting Paul's signature Sep 29; template: committed = signed | post read in history; reminder is one automated notice |
| T2 | done_gap | frederick.stone@harmonygames.co/1844347876147200047, ZOM-567 | R4 | Dentsu has iOS and Android | ZOM-567: Play track not added (Arthur Sep 29) | mail met with the firm; Linear rarely opened |
| T3 | superseding | frederick.stone@harmonygames.co/1842285743246816270 (Sep 12, Sep 18) → C096HFA5Z8W/1759184040.552871 | R2 | SciPlay In talks | Robert's thread reply: passed by phone | reply under a multi-firm root, not in channel history |
| T4 | superseding | C07C2866011/1758303600.418207 → frederick.stone@harmonygames.co/1844162278195200023 | R3 | Anton $40,000 | Anton trims to $25,000; completed notice frederick.stone@harmonygames.co/1844354293432320031 | post first; mail has no SAFE subject |
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

Chains (root causes distinct): C1 A24 (C07C2866011/1758303600.418207 → f_3b9e61c04d7a52e8f1a6c2 → frederick.stone@harmonygames.co/1844610859008000037, R3); C2 A14 (frederick.stone@harmonygames.co/1842285743246816270 → f_3b9e61c04d7a52e8f1a6c2 → C096HFA5Z8W/1759184040.552871, R2); C3 A7 (f_48247af79428823c3cac92 → frederick.stone@harmonygames.co/1844318935449600041 → e3a91c07d5b48f26a0c7e314, R2); C4 A17 (evt_2f86b0d4c9e17a35b64e0d → b72f0d6e19c3a84e5d21f9a0 → frederick.stone@harmonygames.co/1844276782694400053, R1); C5 A15 (frederick.stone@harmonygames.co/1844724419788800011 → 68c6b2a4f19e03d7c5a81b2e → C096HFA5Z8W/1759184040.552871, R6).

Hardness v2 selection (named traps, each a cross-source decision flipping weight-5 rows; 01_Gradable_Surface.json):
- v2 trap 1 (done across services, A24) ×2: DONE1 — wrong source Leonard's #executives post C07C2866011/1758303600.418207 (co-founder, Sep 19, says "is in"); beaten by the signing-service reminder frederick.stone@harmonygames.co/1844610859008000037 under the template's definition; flips M1, M2, RP2, RP3. DONE2 — wrong source Leonard's Dentsu mail frederick.stone@harmonygames.co/1844347876147200047 ("invites are out to all three"); beaten by Arthur's ZOM-567 (Play track not added, Sep 29); flips AC1.
- v2 trap 2 (correction somewhere else): CORR — wrong source SciPlay's own thread frederick.stone@harmonygames.co/1842285743246816270; beaten by Robert's reply C096HFA5Z8W/1759184040.552871 in another service and another thread; flips ST1, KW1.
- v2 trap 6 (alias): ALIAS — wrong source the list row f_48247af79428823c3cac92 ("no response as of 09/11"); beaten by Edith Vane's pass frederick.stone@harmonygames.co/1844318935449600041 mapped by Contacts e3a91c07d5b48f26a0c7e314; flips ST2, KW2.
- v2 trap 7 (outside the filter): FILT — Homa (evt_89381fe5a15b802c5652a9) and Brightwater (evt_2f86b0d4c9e17a35b64e0d), wrong source the 2025 list f_48247af79428823c3cac92 as the population; flips V1, ST3, ST4.
- v2 trap 8 (wrong inputs to a total): INPUT — Anton's trim frederick.stone@harmonygames.co/1844162278195200023; flips M3, M2, RP2.
- v2 trap 3 (follow-through): FOLLOW — card rule 68c6b2a4f19e03d7c5a81b2e; flips KW1, KW2.

### Mechanism portfolio (S5a)

Candidates generated (14), each grounded: DONE1, DONE2, CORR, ALIAS, FILT, INPUT, FOLLOW (selected) and COMPL (LVP already on the keep-warm list, rejected: an exact check-item count is not decodable by the grader, `gradeable-report`), DOCSEND (DocSend view counts, rejected: notices sit in Leonard's mailbox, not Frederick's), CASH (runway line, rejected: hazard Q05, f_605121f4a36752645e0ac3 vs snowflake.FINANCE), TZ (a16z pass at 19:30 PT, rejected: after the seed bound, frederick.stone@harmonygames.co/1844748127814183717), PLAYV (Play Ventures pass, rejected: base contradiction C096HFA5Z8W/1758671737.632949), GFR-MOVE (cancelled Sep 29 copy evt_38bdf82a0d337c4d82695e, rejected: Opus reads both copies in one list call), BUBBLES (T-Accelerate action items frederick.stone@harmonygames.co/1843978997950200606, rejected: "share with the team" reads two ways).

| Rule | Deciding record | Mechanism | Nodes | Natural-reading fallback | Prior family · ledger records | Survives complete retrieval | Tool-surface proof | Weight-5 slots |
|---|---|---|---|---|---|---|---|---|
| DONE1 | frederick.stone@harmonygames.co/1844610859008000037 | A24 | T1, C1 | angels "in" = committed | done_gap · Beta(1,1), 0 Opus 5.5 records | yes: the reminder must be weighed against the post | reminder returned by a Gmail search for the angel's name | M1, M2, RP2 |
| INPUT | frederick.stone@harmonygames.co/1844162278195200023 | A11 | T4 | Anton $40,000 | superseding · 0 records | yes: amount reconciliation | Anton's mail returned by a name search | M3, M2, RP2 |
| DONE2 | ZOM-567 | A24 | T2 | Dentsu both platforms | done_gap · 0 records | yes: ticket vs mail judgement | linear_list_issues/search returns ZOM-567 | AC1 |
| CORR | C096HFA5Z8W/1759184040.552871 | A14 | T3, C2 | SciPlay In talks | superseding · 0 records | yes: reply must be placed against the thread | slack search "SciPlay" returns the reply | ST1, KW1 |
| ALIAS | e3a91c07d5b48f26a0c7e314 | A7 | T5, C3 | Hiro Awaiting reply | scope_alias · 0 records | yes: person→firm mapping | contacts_search_contacts returns Edith Vane | ST2, KW2 |
| FILT | evt_2f86b0d4c9e17a35b64e0d | A17 | T6, T7, C4 | list rows only | exact_predicate · 0 records | yes: scope rule must be applied to calendar calls | gcal_list_events returns both calls | ST3, ST4 |
| FOLLOW | 68c6b2a4f19e03d7c5a81b2e | A15 | T8, C5 | no checklist writes | authority · 0 records | yes: rule applies after retrieval | trello_get_comments returns the rule | KW1, KW2 |

Priors (ledger support/hardness_ledger/ledger.jsonl): `hardness_ledger.py priors --model claude-opus-5-5` returns no family records for any family (header only), so every rule starts at Beta(1,1); no other model's evidence is transferred. Controls and over-application per rule (e.g. DONE1 control Anton, frederick.stone@harmonygames.co/1844354293432320031) are in the manifest `mechanism_portfolio[].controls/over_application`; channels CH-FILT-HOMA, CH-FILT-BRIGHT (member channels, latent "calendar sweep") and CH-SLIP (control rows ST5, AC2, RP1, DL1) are declared in `channels`.

### Liveness flags (S5b)

`trap_liveness.py --design` (verbatim in section 12; hub frederick.stone@harmonygames.co/1844724419788800011) raised breadcrumb/order flags on T1, T6, T7, T8, T9, T11, D1, D3, D5, D6. Dispositions (also in `plan/liveness_dispositions.json`):
- T1 breadcrumb (frederick.stone@harmonygames.co/1844610859008000037): keep — the hub names the template by role only; the reminder's subject names the SAFE, not the word "committed".
- T6/T7/T11 breadcrumb+order (evt_2f86b0d4c9e17a35b64e0d, evt_89381fe5a15b802c5652a9, 5d0e8b31f7a29c64e1b0d3a8): keep — the population rule must name calls (UGT); the difficulty is applying it to person-titled events, never removed.
- T8 breadcrumb (68c5a49e8491a9d7faf869d0): keep — the hub must name the card for incorporation; the rule itself is a comment.
- T9 breadcrumb (f_3b9e61c04d7a52e8f1a6c2): keep — the template must be incorporated; the decoy shares its terms.
- D1/D3/D5/D6 (f_0b29566cd7932a205d54d2, C096HFA5Z8W/1758130464.175719, frederick.stone@harmonygames.co/1844623441920000059, 663ea0fc3f231e879cefd5e8): distractors are meant to be met; no fairness link removed.

`hardness_v2_check.py --design` (manifest 01_Hardness_Manifest.draft.json): every check CLEAN (SAME_PLACE 0 flagged over 4 version-record traps; DONE_CHECK; TWO_DECISIONS over R1, R2, R3, R4, R6; DECISION_FLIP 7/7; INPUT_CHECK; FILTER_CHECK); RULE_IN_PROMPT SKIP until 04_Prompt.txt exists (`plan/v2_check.txt`).

## 6 Failure-diversity plan

| Channel | Runs likely to miss it | Requirement touched | Findability tier |
|---|---|---|---|
| DONE1 (C07C2866011/1758303600.418207) | runs that take #executives at its word | R3, R7 | medium |
| INPUT (frederick.stone@harmonygames.co/1844162278195200023) | runs that never search Anton by name | R3, R7 | medium |
| DONE2 (ZOM-567) | runs that never open Linear for a fundraising task | R4 | low |
| CORR (C096HFA5Z8W/1759184040.552871) | runs reading channel history without opening threads | R2, R6 | medium-low |
| ALIAS (e3a91c07d5b48f26a0c7e314) | runs matching firms by list name only | R2, R6 | medium |
| FILT-Homa (evt_89381fe5a15b802c5652a9) | runs bounded by the list | R1 | medium-high |
| FILT-Brightwater (evt_2f86b0d4c9e17a35b64e0d) | runs that skip person-titled calls | R1 | low |
| FOLLOW (68c6b2a4f19e03d7c5a81b2e) | runs that never read card comments | R6 | medium-low |

No single discovery gates most requirements: the largest unit (DONE1) decides 18 of 69 weight (26 %).
Policy scores on the real surface (`plan/policy_scores_output.txt`, UNCALIBRATED):

```
UNCALIBRATED · surface weight 69
  100.0%  perfect
   44.9%  every cc'd thread, no off-thread checks (DONE1 DONE2 CORR FOLLOW)
   66.7%  list-bound (FILT both, ALIAS)
   59.4%  trusts done sources (DONE1 DONE2 INPUT)
   85.5%  all but follow-through
   11.6%  lazy (all land)
single misses: {'DONE1': '73.9%', 'INPUT': '78.3%', 'DONE2': '92.8%', 'CORR': '85.5%', 'ALIAS': '85.5%', 'FILT_HOMA': '88.4%', 'FILT_BRIGHT': '88.4%', 'FOLLOW': '85.5%'}
two misses (lowest/highest): 59.4% ('DONE1', 'ALIAS') ... 81.2% ('FILT_HOMA', 'FILT_BRIGHT')
  scale 1.0 rho 0.3: {'E_avg': 0.512, 'P(avg<80%)': 0.999, 'P(avg<85%)': 1.0, 'P(SD band)': 0.8986666666666666, 'P(patterns)': 0.9856666666666667, 'P(all gates)': 0.8885}
  scale 1.0 rho 0.6: {'E_avg': 0.529, 'P(avg<80%)': 0.9833333333333333, 'P(avg<85%)': 0.9943333333333333, 'P(SD band)': 0.6006666666666667, 'P(patterns)': 0.9151666666666667, 'P(all gates)': 0.5723333333333334}
  scale 0.75 rho 0.3: {'E_avg': 0.622, 'P(avg<80%)': 0.9616666666666667, 'P(avg<85%)': 0.9901666666666666, 'P(SD band)': 0.9036666666666666, 'P(patterns)': 0.9926666666666667, 'P(all gates)': 0.8905}
  scale 0.75 rho 0.6: {'E_avg': 0.638, 'P(avg<80%)': 0.9021666666666667, 'P(avg<85%)': 0.9583333333333334, 'P(SD band)': 0.6176666666666667, 'P(patterns)': 0.9555, 'P(all gates)': 0.5761666666666667}
  scale 0.6 rho 0.3: {'E_avg': 0.69, 'P(avg<80%)': 0.8631666666666666, 'P(avg<85%)': 0.9523333333333334, 'P(SD band)': 0.9138333333333334, 'P(patterns)': 0.9848333333333333, 'P(all gates)': 0.8656666666666667}
  scale 0.6 rho 0.6: {'E_avg': 0.706, 'P(avg<80%)': 0.7738333333333334, 'P(avg<85%)': 0.884, 'P(SD band)': 0.6575, 'P(patterns)': 0.9545, 'P(all gates)': 0.5625}
  scale 0.5 rho 0.3: {'E_avg': 0.739, 'P(avg<80%)': 0.7301666666666666, 'P(avg<85%)': 0.8836666666666667, 'P(SD band)': 0.9113333333333333, 'P(patterns)': 0.9755, 'P(all gates)': 0.8103333333333333}
  scale 0.5 rho 0.6: {'E_avg': 0.751, 'P(avg<80%)': 0.642, 'P(avg<85%)': 0.7915, 'P(SD band)': 0.6853333333333333, 'P(patterns)': 0.9365, 'P(all gates)': 0.524}
```

## 7 Deliverables and dependent writes

| Write | Tool | Destination | Depends on | Requirements |
|---|---|---|---|---|
| Register (one row per firm: status, last two-way contact, build access, committed, soft-circled) | gsheets_create_spreadsheet + gsheets_values_update | Board - Oct 14 2025 folder d_5e8a1c3f9b07d2e64a1b93 (owner Frederick) | K3–K7, K11, C1–C4, T1–T7 | R1–R4 |
| File placement | gdrive_move_file (or create with parent) | d_5e8a1c3f9b07d2e64a1b93, named per README f_c61a0e93b7d24f58a2e917 | K2, K13 | R5 |
| Keep-warm items | trello_create_checklist / trello_create_check_item | card 68c5a49e8491a9d7faf869d0 | K9, C5, T3, T5, T8 | R6 |
| Reply | gmail_reply_to_message | thread frederick.stone@harmonygames.co/1844724419788800011 (Leonard; cc as on the ask) | K1, K10, C1, T1, T4 | R7 |

Reuse-vs-create: the keep-warm checklist does not pre-exist; the card's comment says "the keep-warm checklist on this card" (create once, then add items).

## 8 Service role map

| Service | Role | Load-bearing fact / write | Carrier |
|---|---|---|---|
| gmail | hub, investor threads, signing notices, Anton, Hiro, Dentsu, Brightwater, reply | committed/soft, Hiro pass, Dentsu "done" source | ● |
| slack | #bridge-pitch replies, #executives angel post | SciPlay pass (reply), angel post | ● |
| gsheets | 2025 list; register write | population; register | ● |
| gdocs | template, July decoy, README | definitions | ● |
| gcal | pitch calls; review event | off-list calls | ● (titles/attendees); descriptions ○ |
| contacts | partner→firm | Hiro, Brightwater, PXLite mapping | ○ supporting (job title field; verified through contacts_search_contacts at injection) |
| trello | keep-warm rule; deck card numbers | rule; checklist write | ● comments |
| linear | ZOM-567 | Dentsu Play track | ● (description + comments) |
| gdrive | Board folder | destination | ● |
| gslides | draft deck slide 9 | register columns | ● slide element text (no speaker notes: their rendering is unverified, Ask_Carriers §5) |
| github | none | — | — |
| confluence | none (injected pages never relied on, learnings §26) | — | — |
| snowflake | none (cash hazard Q05 avoided) | — | — |

## 9 Call budget

| Phase | Service | Calls | Reason |
|---|---|---|---|
| discovery | gmail | 8 | read the ask and its thread; Robert's board mail; find the template, README, deck via mail links |
| discovery | gdocs | 5 | read the Oct 14 template, the July template it supersedes, the folder README |
| discovery | gslides | 3 | open the draft deck and read slide 9's table columns |
| discovery | trello | 8 | find and read the Board Deck and Existing Investor Update cards, their comments and checklists |
| discovery | gdrive | 4 | locate the Board - Oct 14 2025 folder and list it |
| discovery | gcal | 6 | Monday's review event; list Sep 3-30 events on Frederick's calendar (two pages) |
| enumeration | gsheets | 4 | read the 2025 investor list (80 rows, several ranges) and check the 2024 lookalike |
| enumeration | slack | 22 | #bridge-pitch Jul-Sep history (4 pages at 100) and #executives Sep history (about 12 pages), roots only |
| per-record | gmail | 169 | one search per firm by name (79), a second by partner for the ~40 firms whose list row or mail names one, and a thread read for each of the ~50 firms with hits; search returns ids only, no bulk |
| per-record | slack | 124 | one search per firm (79) plus about 45 thread opens where a hit is a root that mentions the firm; replies are not in channel history |
| per-record | contacts | 40 | partner lookups for the list's Partner column, person-titled calls and partner-only replies |
| reconciliation | gcal | 18 | open each person-titled pitch event since Sep 3 for its description and attendees |
| reconciliation | gmail | 26 | signing-service notices per angel, Anton's and Paul's mails, Dentsu and Brightwater follow-ups, Hiro decline |
| reconciliation | linear | 6 | find ZOM-567, read it and its comments for each firm in talks |
| reconciliation | slack | 29 | open every replied thread in #executives (22) and #bridge-pitch (7) for September: phone notes and corrections live in replies |
| rules | gdocs | 4 | re-read the template's definitions while classifying edge firms |
| rules | contacts | 6 | check mapping for Karthic/PXLite and Hiro's Investment Director |
| writes | gsheets | 6 | create the register, write 79 rows in batches, totals |
| writes | gdrive | 2 | place the sheet in the Board folder and confirm |
| writes | trello | 5 | create or reuse the keep-warm checklist and add one item per passed firm |
| writes | gmail | 1 | reply on Leonard's thread |
| read-back | gsheets | 3 | read back the written ranges and totals |
| read-back | trello | 2 | read the checklist back |
| read-back | gdrive | 1 | confirm the file's parent folder |

Total 502 necessary calls, all unconditional; per-record 333; 10 services; largest share outside per-record 30 %.
The golden run also needs the volume: every firm's status at Sep 30 needs its own search (no bulk call returns it). Author target "over 100 calls in each run" is met with margin.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolution |
|---|---|---|---|
| a16z status (frederick.stone@harmonygames.co/1844748127814183717) | In talks at the seed bound | Passed (19:30 PT Sep 30 is still Sep 30 PT) | both accepted; a16z ungraded; KW count accepts 3 or 4 |
| Play Ventures (C096HFA5Z8W/1757955553.793529) | Passed | Awaiting reply (C096HFA5Z8W/1758671737.632949) | both accepted; never sampled |
| PXLite vs T-Accelerate (frederick.stone@harmonygames.co/1843978997950200606) | one firm | separate off-list firm | Contacts 5d0e8b31f7a29c64e1b0d3a8 settles one firm |
| Homa in scope (frederick.stone@harmonygames.co/1843552279434086285) | in (co-dev investment talks) | out (publishing) | Frederick's note C096HFA5Z8W/1758210489.170809 + template "investment, incl. strategic" |
| Rollic / Metaplay (C096HFA5Z8W/1758130464.175719) | out | in | template excludes service and competitor talks |
| Dentsu build access (ZOM-567) | iOS only | both (mail) | template: the tester ticket decides |
| Anton committed amount (frederick.stone@harmonygames.co/1844162278195200023) | $25,000 | $40,000 | latest amount the investor gave (template) + completed notice |
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
| evt_89381fe5a15b802c5652a9 | gcal | YES | LB |
| evt_25c9ee60d4b6c8f6d39a74 | gcal | YES | LB |
| evt_e59dc0a675d0c407b79acf | gcal | YES | LB |
| f_48247af79428823c3cac92 | gsheets | YES | LB |
| d_175c0d7bc72ed244b944cb | gdrive | YES (owner) | LB |
| planned seeds (hub, template, folder, deck, review event, Brightwater event, Dentsu/Anton/Hiro/Brightwater mails) | gmail/gdocs/gdrive/gslides/gcal | planned: owner or addressee Frederick | checked at injection |

Feasibility: register write via gsheets_create_spreadsheet / gsheets_values_update into a folder Frederick owns (learnings §31); gdrive_move_file; trello_create_checklist / trello_create_check_item (unscoped); gmail_reply_to_message on a thread in his mailbox — all in Evals/references/tools/catalog.json. Precedence: load-bearing facts only in ● carriers (Ask_Carriers §5/§6b); Contacts job titles and slide notes are supporting, each paired with a ● record (Edith Vane's cc of PERSON_5282 in frederick.stone@harmonygames.co/1844318935449600041; the hub restates the columns). Naturalness: the prompt names the ask, the destinations (Board folder, Leonard's thread, the investor update card by role) and the deadline; it never lists firms, rules, buckets, amounts or traps. Grading devices: ≤ 5 status samples + volume (register_keys_exact over 79 truth keys), access samples, money rows, reply rows, keep-warm rows; no "leaves X alone" row.

### Coherence rail

Every 1a row dispositioned; designed disagreements are dated human claims with later overturning records (T1, T3, T4, T5, T9, T10); companions planned per section 11; ids follow the base schemes (Gmail thread = ms << 20, Slack ts, evt_ + 22 hex, f_/d_ + 22 hex, Trello/Contacts 24 hex, ZOM-567 next free).

## 11 Record plan for /create-injection

| Seed | Service | Id | Time (UTC) | Content (design summary; text is written at injection) |
|---|---|---|---|---|
| Hub / anchor | gmail | frederick.stone@harmonygames.co/1844724419788800011 (+ Robert, Arthur copies) | 2025-09-30T21:05:00Z | Leonard asks Frederick to own the fundraising section; carries K1, K2, K3, K4–K6 quote, K9, K10, K12, K13 quotes verbatim |
| Oct 14 template | gdocs | f_3b9e61c04d7a52e8f1a6c2 | 2025-09-26T18:00:00Z | buckets, as-of, committed/soft-circled, build access, scope exclusions, phone-note rule (K8 quote), tester ticket (K14 quote) |
| July template (decoy) | gdocs | f_8d2c47a91e05b3f6d7c418 | 2025-07-08T18:00:00Z | committed = verbal yes from a named investor |
| README | gdocs | f_c61a0e93b7d24f58a2e917 | 2025-09-26T18:30:00Z | file naming for the Board folder |
| Board folder | gdrive | d_5e8a1c3f9b07d2e64a1b93 | 2025-09-26T18:20:00Z | owner Frederick; README inside |
| Draft deck | gslides | f_a47d0e2c95b18f63e2c0d5 | 2025-09-27T17:00:00Z | slide 9 text: table columns |
| Review event | gcal | evt_9c41e7a2d05b38f6e1a7c4 (Leonard + Frederick copies) | created 2025-09-30T21:00:00Z, start Oct 6 | description: bring the sheet link |
| Brightwater call | gcal | evt_2f86b0d4c9e17a35b64e0d (Leonard + Frederick copies) | 2025-09-25T15:30:00Z | "Ilse Marrow and Leonard Hayes" |
| Angel post | slack | C07C2866011/1758303600.418207 | 2025-09-19T17:40:00Z | Paul $50K and Anton $40K "are in" |
| Arthur aside | slack | C07C2866011/1759168800.117903 | 2025-09-29T18:00:00Z | non-authoritative suggestion |
| Robert phone-note root | slack | C096HFA5Z8W/1759161600.226431 | 2025-09-29T16:00:00Z | phone notes go under each firm's thread |
| SciPlay reply | slack | C096HFA5Z8W/1759184040.552871 (thread 1757716998.377299) | 2025-09-29T22:14:00Z | SciPlay passed by phone; root counters updated (Q01) |
| Anton trim | gmail | frederick.stone@harmonygames.co/1844162278195200023 | 2025-09-24T16:10:00Z | $25,000 instead of $40,000 |
| Signing completed (Anton) | gmail | frederick.stone@harmonygames.co/1844354293432320031 | 2025-09-26T19:02:00Z | envelope completed, no amount in body |
| Signing reminder (Paul) | gmail | frederick.stone@harmonygames.co/1844610859008000037 | 2025-09-29T15:00:00Z | awaiting Paul's signature |
| Hiro pass | gmail | frederick.stone@harmonygames.co/1844318935449600041 | 2025-09-26T09:40:00Z | Edith Vane declines; cc PERSON_5282 |
| Dentsu "invites out" | gmail | frederick.stone@harmonygames.co/1844347876147200047 | 2025-09-26T17:20:00Z | Leonard: invites out to all three |
| Brightwater follow-up | gmail | frederick.stone@harmonygames.co/1844276782694400053 | 2025-09-25T22:30:00Z | deck sent; partner meeting next |
| Robert board mail | gmail | frederick.stone@harmonygames.co/1844623441920000059 | 2025-09-29T18:20:00Z | suggests mailing the board |
| Tester ticket | linear | ZOM-567 + comment | created 2025-09-24T02:00:00Z, comment 2025-09-29T20:30:00Z | per-firm TestFlight / Play status; Dentsu Play not added |
| Keep-warm rule | trello | comment 68c6b2a4f19e03d7c5a81b2e on 68c5a49e8491a9d7faf869d0 | 2025-09-14T16:20:00Z | passes after a pitch go on the keep-warm checklist |
| Deck numbers | trello | comment 68d81f30a6c94e2b7d05e1f4 on 67f446b4b0817af30d2d63f6 | 2025-09-27T17:10:00Z | slide takes register size, committed, soft-circled |
| Contacts | contacts | e3a91c07d5b48f26a0c7e314, b72f0d6e19c3a84e5d21f9a0, 5d0e8b31f7a29c64e1b0d3a8 | n/a | Edith Vane (Hiro Capital), Ilse Marrow (Brightwater Games Fund), Karthic R (T-Accelerate Capital, PXLite fund) |

Before SQL (learnings §10–17): census every seeded name (Paul Heydon, Anton Bernstein, Edith Vane, Ilse Marrow, Brightwater) across all services with a positive control ("Grishin Robotics" found in gsheets data.json and gmail 00001934.json); Paul Heydon and Anton Bernstein already show 0 Gmail hits outside the list; "Kestrel" was rejected (3 base Gmail hits, 00013854.json). Collision-check every minted id with `hg.py search lookup`. Time every seed after the base events it names (SciPlay Sep 18 mail, Hiro Sep 3 re-intro mail, Dentsu Sep 23 call, T-Accelerate Sep 22 recap). Correction after the platform /injection review of rev1 (advisory 2): the Sep 3 Hiro thread frederick.stone@harmonygames.co/1842278425320449096 is a re-intro email, not a call, so the base holds no Hiro pitch call this round; injection rev2 seeds the call (evt_7d3e19b04a6c25f8e1b9a0, Tue Sep 23 16:00Z, with its invitation mails) that Edith Vane's pass and the keep-warm rule rely on.

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| gcal | INT-11 | invitation mails for the Brightwater call and the Oct 6 review | seed invitation mails in Frederick's and Leonard's mailboxes |
| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment, Slack DM notice, mail digest | INT-03 none (no PR); INT-04/05: seed Arthur-to-Leonard notification mail only if base pattern holds, else record integration_exceptions |
| gdrive | INT-13 | Drive Slack app DM on share | seed the share notice DM to Frederick for the README and template |
| slack | INT-22 | Slack e-mail notifications for mentions | none: seeded posts carry no @mention of Frederick |
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
  [ok] ask_fragments: 14 fragments; need ≥ 12
  [ok] ask_fragment_services: 8 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 10 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 7 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 79; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 3 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 327; need ≥ 300
  [ok] call_budget: unconditional (verified) floor 502 of 502 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 500 (Long Horizon; plan ~600 for headroom)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 30% (≤ 50%)
  [ok] traps: 18 traps across 7 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 6 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (3 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 7 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 9 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 5 chains with 5 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 7 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 2 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 15 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 7 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 4 writes over 4 services; each must depend on findings
```

Gradable surface: `gradable_surface.py validate` → `GRADABLE SURFACE (01_Gradable_Surface.json): PASS · 17 slots · weight 69 · mechanism share 88.4% (reported, not gated)`; `gradeable-report` → `SURFACE.GRADEABLE PASS · 17 slot(s) · {'GRADABLE': 17}`. Surface revision at /create-injection S4b (design-level fix, re-certified here): ST1's key is the list's spelling `Sciplay` (f_48247af79428823c3cac92 row 81), and V1 (register_keys_exact) is class `delivery`, as the solver contract (oracle_kit `contract.slots`) reads no solver value for a delivery selector.

Hardness v2 (advisory):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      4 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 5 requirements: {'R3': ['DONE1', 'INPUT'], 'R4': ['DONE2'], 'R2': ['CORR', 'ALIAS'], 'R1': ['FILT'], 'R6': ['FOLLOW']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   7 of 7 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Trap liveness (advisory, UNCALIBRATED):

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · DESIGN (no SQL: record text unavailable, only manifest-structure flags can fire) · on the Season Pass backtests these are development fixtures, not validation
  hub frederick.stone@harmonygames.co/1844724419788800011 · direct delegations 11 · rule placement: A15 nodes only: ['C5', 'T8'] (mechanism_portfolio); every other node SKIP
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
  D1   distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  D2   distractor         -  [rule placement SKIP: not an A15 node]
  D3   distractor         breadcrumb, order  [rule placement SKIP: not an A15 node]
  D4   distractor         -  [rule placement SKIP: not an A15 node]
  D5   distractor         breadcrumb, order  [rule placement SKIP: not an A15 node]
  D6   distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  D7   distractor         -  [rule placement SKIP: not an A15 node]
  dispositions: 0/15 recorded
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
| 1 | temporal | a16z's pass (19:30 PT Sep 30) is inside "end of Sep 30 PT", so excluding it is wrong | frederick.stone@harmonygames.co/1844748127814183717 | both readings accepted; a16z never graded; GEN §0a |
| 2 | semantic | PXLite could be a distinct fund, so one row undercounts | frederick.stone@harmonygames.co/1843978997950200606 | Contacts 5d0e8b31f7a29c64e1b0d3a8 + list row T-accelerate; T11 |
| 3 | cross-service referential | Robert's reply names "D" not SciPlay, so it cannot be tied to the firm | C096HFA5Z8W/1757716998.377299 (root names Sciplay), frederick.stone@harmonygames.co/1842285743246816270 ("-D") | reply text names SciPlay explicitly at injection; root already lists Sciplay |
| 4 | quantitative | committed total could include Paul if "is in" counts as a commitment | C07C2866011/1758303600.418207 | template f_3b9e61c04d7a52e8f1a6c2 defines committed = signed; July template superseded (T9) |
| 5 | state/lifecycle | ZOM-567 open while Arthur is quiet in Oct reads as abandoned | arthur.blake@harmonygames.co status active_sep_2025_quiet_in_oct; L08 | comment dated Sep 29 says when the Play adds happen; state Todo is consistent |
| 6 | identifier/format | seeded Gmail thread ids could collide or break search | frederick.stone@harmonygames.co/1844724419788800011 | ms << 20 scheme as base; lookup collision check at injection; I06 companions |
| 7 | other | the P&L vs Snowflake cash gap could be "task-touched" | snowflake.FINANCE, Q05 | no cash figure is read or graded; excluded |
| 8 | decision point a16z | count of keep-warm items forks | frederick.stone@harmonygames.co/1844748127814183717 | accept 3 or 4; KW rows sample SciPlay and Hiro only |
| 9 | decision point Play Ventures | a sampled status could hit the base contradiction | C096HFA5Z8W/1758671737.632949 | Play Ventures never sampled; volume counts it either way |
| 10 | decision point PXLite | register size 80 vs 79 | 5d0e8b31f7a29c64e1b0d3a8 | one firm; truth_keys 79 |
| 11 | decision point Homa | Homa is a publisher, so out of scope | C096HFA5Z8W/1758210489.170809 | Frederick's own "co-dev investment path"; template "investment, including strategic" |
| 12 | decision point Rollic/Metaplay | a careful run includes every call | C096HFA5Z8W/1758130464.175719 | template exclusion; over-application control in the portfolio |
| 13 | decision point Dentsu access | Leonard's mail is newer than the ticket's creation | frederick.stone@harmonygames.co/1844347876147200047 (Sep 26) vs ZOM-567 comment (Sep 29) | the ticket's Sep 29 comment is newer and the template names the ticket |
| 14 | decision point Anton amount | $40K stands because the SAFE is the record | frederick.stone@harmonygames.co/1844354293432320031 | template: latest amount the investor gave; completed notice has no amount |
| 15 | decision point reply destination | Robert's suggestion is newer than the template | frederick.stone@harmonygames.co/1844623441920000059 (Sep 29) vs hub (Sep 30) | the hub is newest and explicit |
| 16 | false-positive check on FILT | Brightwater might be found by everyone, so no trap | evt_2f86b0d4c9e17a35b64e0d | person-titled, one of ~20 September events; Homa sits at a higher tier (failure diversity) |

4. Load-bearing base values re-read through tools/hg.py and the export this session: list rows and Latest Status (f_48247af79428823c3cac92), SciPlay Sep 12/18 mails, Hiro Sep 3 thread and PERSON_5282 Investment Director signature, T-Accelerate Sep 22 recap, Bubbles PXLite notes, Homa invitation, Arthur's Play note C096HFA5Z8W/1758677722.184129.
5. `hardness_gate.py --design` output is pasted above: HARDNESS GATE (extreme (design)): PASS.

Unresolved: no independent (dual red-team) review of this design — REDTEAM_* is not set (section 13); the Gmail census of Edith Vane, Ilse Marrow and Brightwater runs at injection; Opus 5.5 priors are uninformed (Beta(1,1)), so every forecast number is UNCALIBRATED.

```
STAGE GATE scenario: PASS — Task_Authoring/task_inputs · 01_Scenario_Design.md#4d2e27cf58f0 · 01_Hardness_Manifest.draft.json#2a9d201c7c9b · 01_Gradable_Surface.json#c052ab4dedcb · 00_Assigments.md#8ae66b700bc2 · __context__#f1f763cb8cb4 · __assignment__#827e8afa884d · __policy__#dc4ab5df3cdd · __gate_policy__#0fc4bb90877f · __review__#56afc78fef36 · blocking 0 · warnings 0 · checks 33
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
[PASS] evidence.delegation: 15/15 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 36/36 items carry a source pointer (min 90%)
[PASS] evidence.record_plan: 28/30 items carry a source pointer (min 80%); unsourced e.g. L461: 'gmail | none in integrations.json as a source | — | gmail: none'
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
[PASS] surface.valid: 17 slots, weight 69; geometry report-only, never gated: mechanism share 88%, always-pass share 12%
[PASS] forecast.preregistered: prior forecast pre-registered in the ledger: ['hev_77ceb6bf5eb21f90'] (UNCALIBRATED, advisory)
[SKIP] revise.intake: no MODE B report and no revision-intake section: nothing to take in
[PASS] reach.scenario: 16 scoped load-bearing ids YES for frederick_stone (1 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 16 evidenced counter-readings (of 16 found; need ≥ 15) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.draft.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 Red team (dual)

RED TEAM UNAVAILABLE: REDTEAM_* is not set in this environment (`env | grep REDTEAM_` returns nothing), so `tools/redteam_review.py --mode redteam --dual` cannot run.
RED TEAM FALLBACK: Claude (Opus 5.5, the author) ran the lazy-solver pass, the literal and wording sweeps, the fork sweep in the two-reading table and the policy scores on the real surface; the requester chose a recorded fallback on 2026-11-01 because no reviewer endpoint is configured. This is self-review, not an independent review, and stays in every Unresolved line until a reviewer or the Opus pre-check covers it.


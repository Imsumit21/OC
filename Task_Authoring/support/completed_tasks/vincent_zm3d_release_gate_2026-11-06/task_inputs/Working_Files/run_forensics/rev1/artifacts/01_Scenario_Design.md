# Scenario Design — vincent-zm3d-release-gate · design only · contains no prompt, OE or criterion text

Clock: 2025-10-01 00:00 PT (2025-10-01T07:00Z), Oct 1, 2025 (synth-cut). Seed bound 2025-10-01T00:00:00Z; nothing seeded is dated later.

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Persona | Vincent Parker · `vincent_parker` · vincent.parker@harmonygames.co (Game Systems Engineer, Engineering; owns QA per page_qa_runbook) |
| Business function / competency / skill | Engineering · Engineering Ops · Analysis and synthesis |
| Horizon | Long Horizon → extreme profile, requester-confirmed volume_exception 250 / 150 |
| Difficulty mode | Easy (cap: average strictly below 90 %); design target E[avg] 62–77 % (requester: aim medium or hard) |
| Universe | synth-cut, freeze 2025-10-01T00:00:00Z; context_hash fb209f3058d7e399087b2b69e0108dfc9429f64c9c1cb45eeb3e417275bd498a |
| Design basis | 00_Pre_Scenario_Analysis.md (storyline A, decisions D1–D4) |

Persona census (`python3 Task_Authoring/tools/persona_view.py reach vincent_parker --no-correspondents --top 3`):

```
REACH  Vincent Parker <vincent.parker@harmonygames.co>  Game Systems Engineer / Engineering
clock 2025-10-01

SLACK  user=EMPLOYEE_0012_SLACK_ID  visible channels=140 {'mpim': 32, 'public': 40, 'private': 45, 'im': 23}  messages=262653  public-not-member (UNVERIFIED)=27
  persona posts=39854 last post=2025-09-30  last activity in visible channels=2025-10-01
  C05433XK267    builds                                 public  mem=31  msgs=35617  2023-04-20..2025-10-01
  C05H8KVNU67    game-design                            private mem=27  msgs=22750  2023-07-16..2025-08-28 archived
  D0770ET1HV2    D0770ET1HV2                            im      mem=5   msgs=22707  2024-06-06..2025-09-30

GMAIL  mailbox=vincent.parker@harmonygames.co threads=1258 messages=1367 range=2023-08-30..2025-09-30
  threads by last-message month (recent): {'2025-04': 62, '2025-05': 138, '2025-06': 115, '2025-07': 79, '2025-08': 84, '2025-09': 55}

GCAL  own=['vincent.parker@harmonygames.co'] shared=[] events=446 (distinct ical_uid 157, cancelled 52)
  last event before clock=2025-09-29T16:30:00Z  next after clock=2025-10-01T16:00:00Z
  by month: 2023-09:5 2023-10:8 2023-11:12 2023-12:7 2024-01:4 2024-02:1 2024-03:2 2024-04:13 2024-05:12 2024-06:22 2024-07:26 2024-08:27 2024-09:48 2024-10:33 2024-11:31 2024-12:40 2025-01:40 2025-02:22 2025-03:4 2025-04:17 2025-05:30 2025-06:17 2025-07:12 2025-08:7 2025-09:5 2025-10:1

DRIVE  owned=190 {'application/json': 90, 'application/vnd.google-apps.spreadsheet': 48, 'application/vnd.google-apps.document': 23, 'folder': 15, 'text/plain': 7, 'application/pdf': 4, 'application/vnd.google-apps.presentation': 2, 'text/csv': 1}
  shared-with=141 {'application/vnd.google-apps.document': 50, 'application/vnd.google-apps.spreadsheet': 32, 'text/plain': 27, 'application/json': 21, 'application/vnd.google-apps.presentation': 5, 'application/pdf': 4, 'text/csv': 2}
  shared by owner: {'Resource: -6481757892984311338': 100, 'leonard.hayes@harmonygames.co': 27, 'robert@harmonygames.co': 7}
  native visible: {'gdocs': 73, 'gsheets': 80, 'gslides': 7}  last modified visible=2025-09-30T16:30:39Z
  UNVERIFIED (domain/anyone, not owned/shared)=85 {'application/vnd.google-apps.document': 32, 'application/vnd.google-apps.spreadsheet': 25, 'application/json': 11, 'application/pdf': 10, 'application/vnd.google-apps.presentation': 7}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2025-09-30 (1d), slack_visible_channels=2025-10-01 (0d), gmail=2025-09-30 (1d), gcal_last_event_before_clock=2025-09-29 (2d), drive_last_modified_visible=2025-09-30 (1d)
```

Horizon note: Long Horizon assignment, so the extreme profile applies (GEN_EXECUTION §3a). The honest necessary-call count tops out near 260 (≈ 160 per record): only Linear comments are a per-record surface (#zombie-prs C093LEZGF6J mirrors match3d reviews, comments and merges; Slack threads are search-sweepable; base Linear has 0 comments and closed tickets take none after completed_at, learnings §50). The requester chose floors 250 / 150 with the widest natural scope ("go with this", 2026-11-04). Every other extreme target applies unchanged.

Requester decisions carried in: storyline A (ZM3D store release gate); floors 250 / 150; design target 62–77 %; scenario red team waived (recorded in §13).

## 1 Storyline

Zombie Match 3D (ZM, Linear team ZOM) store submission release gate for the builds Arthur Blake cut on Tue Sep 30 2025, placed against the universe_kb timeline (Sep 2025 beats below).

- Candidate builds: iOS Submission #50 job start C05433XK267/1759257812.041449 (18:43:32Z, success C05433XK267/1759259749.259909) and Android Submission #135 job start C05433XK267/1759257934.076209 (18:45:34Z, success C05433XK267/1759263189.219529), both from main.
- Previous gate: iOS Submission #40 C05433XK267/1758544698.778509 and Android Submission #127 C05433XK267/1758544783.817259 (Sep 22, jobs started ≈12:30Z).
- Seeded hub: Arthur's store release ticket ZOM-570 (2025-09-30T20:20Z) and his candidate post C08R27X0EAH/1759263900.484190 in #zombie-bugs, both asking QA for the gate before Friday's go/no-go evt_81e6dc4dbfd331f1a6a317 (2025-10-03T16:00Z).
- Vincent's work: one register row per in-scope ticket in his gate sheet f_0ebfccf33076f9dbf086bc, the blocker list on ZOM-570, a bug for the failed update-path check (page_qa_runbook rule), and the sign-off reply in Arthur's thread C08R27X0EAH/1759263900.484190.
- Cohort: cohorts.json LIN-OPEN-ZOM (99 open ZOM issues, minus perf-pass ZOM-359 and ZOM-475) + ZM tickets in other teams (ART-790, ART-792, seeded ART-793, DES-313) + 18 base tickets Done since the Sep 22 gate (ZOM-536, ZOM-557, ZOM-498 …) + seeded ZOM-567 to ZOM-580 (ZOM-570 excluded as the release ticket) = 132 keys.
- universe_kb timeline beats used: 2025-09-19 ZOM-554 tornado-boost report C08R27X0EAH/1758311440.897499; 2025-09-21 orange-juice submission blocker C08R27X0EAH/1758485492.586459; 2025-09-25 vision bot match3d#476; 2025-09-26 PR match3d#466 merged (ZOM-564 fix); 2025-09-30 ZOM-563 prod deploy D079SNE2TL4/1759256193.859279.
- trap_catalog ids: K02 app-name lineage (vendor mail vincent.parker@harmonygames.co/1844730396672762606 uses Puzzles vs Zombies), C02 fixed then still broken (ZOM-435 re-test 68dc63484a5b2d0a869e758f), D04 stale version (Sep 22 tab of f_0ebfccf33076f9dbf086bc), D06 two runbook versions (page_qa_runbook), N01 ZOM/ENG number twins (ZOM-562), B03 Jenkins Unknown status (C05433XK267/1759248206.832809).

## 1a Coherence audit

Checked against coherence_hazards.json (universe_kb synthcut), scope = every record a correct run opens. Full working notes: research/coherence_audit.md.

| Record | QC category | Fields | Evidence pointer | Hazard id | Disposition |
|---|---|---|---|---|---|
| Vincent's thread files (seeded threads join them) | temporal | messages order | vincent.parker@harmonygames.co/1844730396672762606 | T02 | fold into design: each seeded thread has one message (no ordering claim) |
| ZOM-450 completed before match3d#375 merged | temporal | completed_at vs merged_at | ZOM-450 | T04 | avoid: seeded ZOM-567 completes after match3d-backend#36 merges, ZOM-569 after the 21:36Z commit |
| ZM ROADMAP card dateLastActivity | temporal | dateLastActivity | 68d1eb90bef538c7c5c5599d | T06 | fold into design: seeded comments bump dateLastActivity to 2025-09-30T23:10:00Z |
| match3d PRs citing ENG keys | semantic | title, head_ref | harmonygames-Games/match3d#375 | S01 | avoid: Done fixes traced by ZOM key, #builds change line or SHA only |
| Mixed label vocabulary ("Submission Blocker" is a label) | semantic | labels | ZOM-292 | S03 | fold into design: the call comes from Leonard's rules doc f_632c44650df44fe252ee59, never from a label |
| Slack keys absent from Linear (ENG-2367/2368/2373) | cross-service referential | text | ZOM-436 | R01 | avoid: no seeded message cites a missing key; SC-26 ids never used |
| Slack links to Google files use native ids | cross-service referential | url | f_5e40215b7d4d24b0455412 | R04 | fold into design: seeded Slack text names the test log by exact title, no f_ id link |
| match3d human PR comments without Slack mirror | cross-service referential | review/comment text | C093LEZGF6J | R06 | fold into design: no seeded match3d review; match3d-backend#36 is outside the INT-01 mirror list |
| Seeded GitHub records vs #zombie-prs mirror | cross-service referential | mirror | harmonygames-Games/match3d-backend#36 | R07 | avoid: match3d-backend is not mirrored, so no Slack copy is owed |
| Calendar invites without a GCal row | cross-service referential | invite mail | evt_81e6dc4dbfd331f1a6a317 | R08 | fold into design: the GCal rows and Arthur's invitation mails are seeded together (Vincent, Leonard, Brian, Robert copies) |
| Thread reply counters | quantitative | reply_count, latest_reply | C08R27X0EAH/1759263900.484190 | Q01 | fold into design: Brian's reply C08R27X0EAH/1759266600.265963 updates reply_count / reply_users / latest_reply |
| Parent latest_reply drift | quantitative | latest_reply | C08R27X0EAH/1759263900.484190 | Q03 | fold into design: latest_reply = 1759266600.265963 |
| Raw-shaped parents without counters | quantitative | reply_count absent | C08R27X0EAH | Q04 | avoid: no graded count reads a counter field |
| Same RFC message differs between mailboxes | quantitative | body | vincent.parker@harmonygames.co/1844730396672762606 | Q10 | avoid: the vendor mail has only Vincent's copy; the invite copies carry the same body in every mailbox |
| Open ZOM tickets with merged PRs | state/lifecycle | state | ZOM-292, ZOM-387 | L03 | fold into design: both are rows called NO CALL (tooling / analytics), a call that does not depend on whether the PR shipped |
| Parent Done while child open | state/lifecycle | parent_id | ZOM-16, ZOM-293, ZOM-317, ZOM-453, ZOM-458 | L06 | fold into design: each child is called on its own report (SC-30 safer path) |
| Open issues of quiet assignees | state/lifecycle | assignee_id | ZOM-563 | L08 | none in scope: every assignee is active_sep_2025_quiet_in_oct (activity.json) |
| Thread file alias vs user_email | identifier/format | file name | vincent@harmonygames.co_1844730396672762606.json | I03 | fold into design: seeded thread files use the vincent@ alias, thread_id the full address |
| Token-owned mailboxes | identifier/format | user_email | EMPLOYEE_0011_EMAIL vs vincent.parker@harmonygames.co/1844730396672762606 | I05 | avoid: no evidence placed in token mailboxes; the vendor mail is in Vincent's own mailbox |
| GitHub logins are tokens | identifier/format | author_login | harmonygames-Games/match3d#466 | I08 | fold into design: match3d-backend#36 author uses Douglas's base GitHub identity token |
| GCal copies per calendar | identifier/format | rows per uid | evt_81e6dc4dbfd331f1a6a317 | I11 | fold into design: one row per attendee calendar, no count of rows graded |
| ical_uid shared across meetings | identifier/format | ical_uid | 19c1511dd209208f50aabe12f04a6d44@hg4 | I12 | avoid: fresh uid, never joined on |
| Copies on non-attendee calendars | identifier/format | calendar_id | evt_81e6dc4dbfd331f1a6a317 | I13 | avoid: copies only on attendee calendars |
| Trello list names / members redacted | identifier/format | list name | 6851a674975da1fe76e70d93 | I17 | avoid: the list name "BETA: Oct 10" is never graded (SC-13) |

Known-data-issue cards (known_data_issues/synthcut.md) touching the scope:

| Card | Records | Disposition |
|---|---|---|
| SC-8 glass crash fixed or not | ZOM-475 | excluded: perf pass, outside the register |
| SC-13 beta date in list name | 6851a674975da1fe76e70d93 | never graded; no seeded record names a beta date |
| SC-14 dueComplete flags | 6851a6569f3bf818760632ab | never graded; only card comments on 68d1eb90bef538c7c5c5599d are used |
| SC-15 ZOM-521 checklist | ZOM-521 | not in scope (Done before the Sep 22 gate); children ZOM-526 / ZOM-528 called on their own state |
| SC-16 Linear status vs shipped | ZOM-564, ZOM-563, ZOM-513 | fold into design: the graded calls follow the safer path (PR match3d#466, prod confirm D079SNE2TL4/1759269524.769369); Linear state is never the deciding fact |
| SC-18 PR #477 state | harmonygames-Games/match3d#477 | never graded; post-cut either way |
| SC-19 telemetry vs store versions | C05433XK267/1759263189.219529 | avoid: builds named by submission number and store version 1.3.24 only, no RAW_EVENTS version |
| SC-26 missing ENG-2367+ | ZOM-436 | avoid: no ENG-2367+ key used or seeded |
| SC-30 Done parents | ZOM-457 | fold into design: children called on their own state |
| SC-37 crash-by-level split | snowflake.CLIENT_ERROR_EVENTS | not used: no Snowflake read in the design |
| SC-38 Season Pass ship date | ZOM-552 | never graded; ZOM-529 not used |
| SC-56 commit title case | C05433XK267/1759263189.219529 | fold into design: Done fixes matched by SHA or PR number, not exact title case |
| SC-67 build #1621 header | C05433XK267 | not in scope (Android #1621 is outside Sep 22–30) |
| SC-68 Boss Arena on prod early | D079SNE2TL4 | never graded |
| SC-70 Slack timezones | EMPLOYEE_0012_SLACK_ID, evt_81e6dc4dbfd331f1a6a317 | never graded; all times in UTC |
| SC-71 ZOM-471 priority | ZOM-471 | never graded; priority is not a register column |

Sibling-defect sweep:

- "works in dev, not prod" siblings: ZOM-563 (open, fixed on prod per D079SNE2TL4/1759269524.769369), ZOM-534 (open, prod-only quest reset; settled by a seeded QA comment), ZOM-353 (Done Jul 7, before the gate, outside the register).
- Refill siblings of ZOM-562: ZOM-546 (draining refill, distinct mechanism), ZOM-516 (closed Duplicate, endless mode) and ZOM-553 (Done refill change via harmonygames-Games/match3d#453); the vendor report maps only to ZOM-562 (boss-arena orphan singles).
- Done-then-broken siblings: only the designed ZOM-435 (68dc63484a5b2d0a869e758f) and ZOM-473 (D0770ET1HV2/1759267800.858041) carry a re-test on the candidates; no base Sep 2025 message reports another Done ZOM fix broken on #133–#135 (search over C08R27X0EAH, C08R6BF4ENN, D079SNE2TL4 Sep 2025).
- Old app name: Puzzles vs Zombies has 0 hits in vincent.parker@harmonygames.co (INT-08 TestFlight mails only), so the alias is resolved inside the task by the Contacts entry 29016e2ba1a844a2509b847b and the report's ZM-only features.

## 1b Active speakers

Every seeded speaker with their activity.json status_at_clock:

| Person | Email | status_at_clock (activity.json) | Seeding role |
|---|---|---|---|
| Vincent Parker | vincent.parker@harmonygames.co | active_sep_2025_quiet_in_oct | persona; Sep 22 / Sep 29 / Sep 30 re-test posts, QA comments, gate sheet owner |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | ZOM-570, candidate post, Trello reuse comment, H1 doc and its Sep 2 doc, approval of match3d-backend#36 and its withdrawal in #zombie-ops, go/no-go invite |
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | H2 doc and its Jul 27 doc, ZOM-570 comment, ZOM-578, Trello re-test comment |
| Brian Foster | brian.foster@harmonygames.co | active_sep_2025_quiet_in_oct | regression summary reply, Turkish DM re-test and doc pointer, regression matrix, update-path test log, QA comments |
| Douglas | douglas@harmonygames.co | active_sep_2025_quiet_in_oct | ZOM-567 note, match3d-backend#36 author, 'stays on dev' reply in #zombie-ops |
| Oliver Brooks | oliver.brooks@harmonygames.co | active_sep_2025_quiet_in_oct | fixed-on-main note on ZOM-569 |
| External playtest vendor | PERSON_9701_EMAIL (planned redaction-style token, collision-checked at injection) | not in activity.json (external) | session report mail and its Contacts entry |

All seeded speech is dated Sep 22–30 2025; every person's last base activity is 2025-09-30 or 2025-10-01 before 07:00Z, so no voice is given after the seed bound.

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
ENTITY email:vincent.parker@harmonygames.co  name=Vincent Parker  kind=person  emails=['vincent.parker@harmonygames.co']
  persona: vincent_parker - Game Systems Engineer / Engineering
  slack      id=EMPLOYEE_0012_SLACK_ID, name=Vincent Parker, real_name=Vincent Parker, email=vincent.parker@harmonygames.co, is_bot=False, deleted=False, messages=39854, first_post=2023-08-30, last_post=2025-09-30   [join: exact_email]
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=35266, first_post=2023-03-20, last_post=2025-10-01   [join: exact_email]
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=129898, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
ENTITY email:brian.foster@harmonygames.co  name=Brian Foster  kind=person  emails=['brian.foster@harmonygames.co']
  persona: brian_foster - Game Engineer / Engineering
  slack      id=EMPLOYEE_0026_SLACK_ID, name=Brian Foster, real_name=Brian Foster, email=brian.foster@harmonygames.co, is_bot=False, deleted=False, messages=28951, first_post=2024-06-06, last_post=2025-09-30   [join: exact_email]
ENTITY email:douglas@harmonygames.co  name=Douglas  kind=person  emails=['douglas@harmonygames.co']
  persona: douglas - Software Engineer / Engineering
  slack      id=EMPLOYEE_0031_SLACK_ID, name=Douglas, real_name=Douglas, email=douglas@harmonygames.co, is_bot=False, deleted=False, messages=13832, first_post=2023-09-01, last_post=2025-09-30   [join: exact_email]
ENTITY email:oliver.brooks@harmonygames.co  name=Oliver Brooks  kind=person  emails=['oliver.brooks@harmonygames.co']
  persona: oliver_brooks - Senior Game Engineer / Engineering
  slack      id=EMPLOYEE_0003_SLACK_ID, name=Oliver Brooks, real_name=Oliver Brooks, email=oliver.brooks@harmonygames.co, is_bot=False, deleted=False, messages=13475, first_post=2024-08-12, last_post=2025-09-30   [join: exact_email]
```

| Correct entity | Lookalike | Locator |
|---|---|---|
| Oliver Brooks | Lauren Brooks | oliver.brooks@harmonygames.co vs lauren@harmonygames.co |
| Vincent's mailbox | vincent@ thread-file alias | vincent.parker@harmonygames.co vs vincent@harmonygames.co_1844155357594079551.json |
| Zombie Match 3D | Puzzles vs Zombies (old TestFlight name, trap_catalog K02) | vincent.parker@harmonygames.co/1844730396672762606 + contact 29016e2ba1a844a2509b847b |

## 2 Cohort spine

- Rule source: Leonard's Sep 23 doc f_632c44650df44fe252ee59 (H2): every open ZM ticket (ZOM team in any open state or label, plus other teams' tickets with ZM or ZM3D in the title) and every ticket moved to Done since the last gate; release tickets and the perf pass (ZOM-359, ZOM-475) stay out.
- Members: 97 open ZOM (LIN-OPEN-ZOM minus ZOM-359 / ZOM-475) + ART-790, ART-792 + seeded open ZOM-568, ZOM-571 to ZOM-580, ART-793, DES-313 + 18 base Done since 2025-09-22T12:30Z (ZOM-112 … ZOM-561) + seeded Done ZOM-567, ZOM-569 = 132 (scenario_gen/scope_keys.json).
- Outside: DES-304 to DES-312 (Cookie label, another game), ENG-2258 and ENG-2360 (Domino Delights tickets that only mention ZM features), ZOM-570 (the release ticket).
- Surfaces: Linear comments per ticket (linear_list_comments, 132 reads: QA observations on the candidate builds live only there); fix provenance per Done ticket (harmonygames-Games/match3d#471 style PR or #builds change line, 20 tickets × 0.75); re-test matching per ticket over Slack (C08R27X0EAH, D0770ET1HV2, C08R6BF4ENN; 0.1 per ticket, sweep pages shared).
- Shortcut audit: linear_list_issues returns state, labels and a truncated description, never comments; no filtered search returns comment text; labels never decide the call (ZOM-427 app icon has no label, ZOM-237 is Bug+VFX); PR search finds only PRs that name the key (ZOM-473's fix c6cf8317 landed via harmonygames-Games/match3d#465 without it).
- Cohort spread of calls (cohort_plan.json, before seeding): open base BLOCKER 7, KNOWN ISSUE 17, NO CALL 75; 15 ambiguous bugs get a seeded raw QA observation on a named build (Sep 24–30), never the verdict word; ZOM-562 is deliberately not settled by a comment (its consequence lives in the vendor report, T5).

## 3 Hidden authorities

| Authority | Home | Decoy | Governs | Findability proof |
|---|---|---|---|---|
| H1 Arthur's submission build rules (Sep 24) | gdocs f_a038a576ca8db6955fae95 (shared with Vincent) | same-service older doc f_fcb4f7c9b508088e0d5803 (Sep 2 15:40Z, 1.3.24 hotfix submissions cut from release/1.3.24_HotFix, after C05433XK267/1756826078.213299) | R2 build membership, R4 backend liveness | ZOM-570 delegates to "my note on how we cut submissions"; a Drive search for "submission" returns both docs |
| H2 Leonard's ZM submission rules (Sep 23) | gdocs f_632c44650df44fe252ee59 (shared with Vincent) | same-service older doc f_5ae4332fb6927f84b3afdc (Jul 27, TestFlight beta drops: only crashes and progress wipes block; decoy_scope lot) | R1 scope, R3 verification, R5 severity | ZOM-570 delegates to "Leonard's submission rules"; a Drive search for "ZM" or "blocks" returns both docs |

The two authorities govern disjoint requirements. The runbook page_qa_runbook (update-path rule, sign-off channel) and page_cicd_pipeline ("Run by hand", "CI stops here") are base Confluence rules, verified as exact substrings of the stored bodies.

## 4 Delegation lattice

| Fragment | Service | Container | Delegated by record | Quote (in the delegating record) |
|---|---|---|---|---|
| K1 scope + severity | gdocs | f_632c44650df44fe252ee59 | ZOM-570 | Leonard's submission rules |
| K1b verification | gdocs | f_632c44650df44fe252ee59 | ZOM-570 | Leonard's submission rules |
| K2 build membership | gdocs | f_a038a576ca8db6955fae95 | ZOM-570 | my note on how we cut submissions |
| K2b backend liveness | gdocs | f_a038a576ca8db6955fae95 | ZOM-570 | my note on how we cut submissions |
| K3 manual deploy | confluence | page_cicd_pipeline | f_a038a576ca8db6955fae95 | CI/CD page |
| K4 bug content | confluence | page_release_checklist | page_qa_runbook | tick the QA sign-off on the |
| K6 register format | gsheets | f_0ebfccf33076f9dbf086bc | f_0ebfccf33076f9dbf086bc | How we gate |
| K7 deadline | gcal | 19c1511dd209208f50aabe12f04a6d44@hg4 (evt_81e6dc4dbfd331f1a6a317) | ZOM-570 | go/no-go on Friday |
| K8 reuse rule | trello | 68d1eb90bef538c7c5c5599d (action 68dc3ef455344e471b1d2ea9) | ZOM-570 | tech-issues card |
| K9 destination | slack | C08R27X0EAH/1759263900.484190 | ZOM-570 | post the candidates in #zombie-bugs |
| K10 destination amendment | linear | ZOM-570 comment cmt_zom570_1 | ZOM-570 | push notes go in the comments here |
| K11 severity example | slack | C08R27X0EAH/1758485492.586459 | f_632c44650df44fe252ee59 | like the orange juice one |

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | the store release ticket | ZOM-570 |
| A2 | the QA regression runbook | page_qa_runbook |
| A3 | my release gate sheet | f_0ebfccf33076f9dbf086bc |

12 fragments in 7 services and 10 containers; every fragment chains back to an anchor (hardness_gate incorporation_chains PASS).

## 5 Chains and trap register

| Trap | Family | Records | Requirement | Resolver |
|---|---|---|---|---|
| T1 | done_gap (A24) | ZOM-569 Done + fixed-on-main note; commit enters Android #2028 C05433XK267/1759268201.182309 (21:36Z) | R2 build status | H1 f_a038a576ca8db6955fae95: main at job start (18:43Z / 18:45Z), so not in #135 / #50 |
| T2 | done_gap (A24) + correction elsewhere | ZOM-567 Done; harmonygames-Games/match3d-backend#36 merged with Arthur's APPROVED review harmonygames-Games/match3d-backend#36#rev_1 | R4 liveness | Arthur withdraws that approval in #zombie-ops C08R6BF4ENN/1759261800.335275 (keep it on dev, not to prod with Friday's push) + H1 + page_cicd_pipeline |
| T3 | superseding (A11) | ZOM-435 Done, Vincent's #133 pass C08R27X0EAH/1759140300.935009 | R3 QA result | Leonard's #135 re-test on 68d1eb90bef538c7c5c5599d (action 68dc63484a5b2d0a869e758f) |
| T3b | superseding (A11) | ZOM-473 Done 2025-09-22 | R3 QA result | Brian's iOS #50 re-test D0770ET1HV2/1759267800.858041 |
| T4 | authority (A15) | Brian's "regression green" C08R27X0EAH/1759266600.265963 | R6 matrix verdict | page_qa_runbook update rule + test log f_5e40215b7d4d24b0455412 (update from 1.3.24 resets progress) |
| T5 | scope_alias (A7) | vendor mail vincent.parker@harmonygames.co/1844730396672762606, contact 29016e2ba1a844a2509b847b | R5 call | maps to ZOM-562 (boss-arena orphan singles); stuck + life lost = blocker under H2 |
| T6 | exact_predicate (A17) | ART-793, DES-313, unlabeled ZOM-578 | R1 scope | H2: any team, any label, any state |
| T7 | completion_elsewhere (A25) | ZOM-563 In Progress | R3 QA result | D079SNE2TL4/1759256193.859279 prod update + D079SNE2TL4/1759269524.769369 confirmation |
| T8 | superseding | Sep 2 doc f_fcb4f7c9b508088e0d5803, C05433XK267/1756826078.213299 | R2 build membership | H1 (Sep 24): every ZM store submission now cut from main |
| T9 | distractor lookalike_entity | "testflight 39 is the submission candidate" C08R27X0EAH/1758409417.505029 | R2 | ZOM-570 names #135 / #50 |
| T10 | distractor stale_summary | C08R27X0EAH/1759266600.265963 | R6 | page_qa_runbook + f_5e40215b7d4d24b0455412 |
| T11 | distractor scope_adjacent | Jul 27 beta-drop doc f_5ae4332fb6927f84b3afdc | R5 | H2 governs store submissions; the July doc covers TestFlight beta drops only |
| T12 | superseding | Sep 22 tab of f_0ebfccf33076f9dbf086bc (ZOM-559 known issue) | R5 | Brian's Sep 29 re-test on ZOM-559 (cmt_zom559_1): victory screen freeze = blocker |
| T13 | distractor keyword_collision | ZOM-516 (closed Duplicate, endless refill) | R5 | report is boss arena, ZOM-562 |
| T14 | distractor partial_listing | Trello "Minor Bugs to Fix" 68c451141c69fb8af1b4568e | R1 | H2 scope is every open ZM ticket |
| T15 | distractor already_done | ZOM-564 Todo, harmonygames-Games/match3d#466 merged 2025-09-26T15:14:44Z | R3 | PR in the candidates + Brian's re-test comment on ZOM-564 |

Independent chains (6 mechanisms, each ≥ 3 hops over ≥ 2 services, ending in a graded fact):

| Chain | Mechanism | Hops | Ends in |
|---|---|---|---|
| CH1 | A24 | ZOM-569 → C05433XK267/1759257934.076209 → C05433XK267/1759268589.049939 → f_a038a576ca8db6955fae95 | R2 / ZOM-569 call |
| CH2 | A11 | ZOM-435 → C08R27X0EAH/1759140300.935009 → 68dc63484a5b2d0a869e758f | R3 / ZOM-435 call |
| CH3 | A15 | C08R27X0EAH/1759266600.265963 → f_5e40215b7d4d24b0455412 → page_qa_runbook | R6 / filed bug |
| CH4 | A7 | vincent.parker@harmonygames.co/1844730396672762606 → 29016e2ba1a844a2509b847b → ZOM-562 | R5 / ZOM-562 call |
| CH5 | A25 | ZOM-563 → D079SNE2TL4/1759256193.859279 → D079SNE2TL4/1759269524.769369 | R3 / ZOM-563 call |
| CH6 | A17 | ART-793 → DES-313 → f_632c44650df44fe252ee59 | R1 / scope rows |

## 6 Failure-diversity plan

Seven loss channels, each on a different source and decision, none above half the mechanism weight (70.9 % of 103 points carry a mechanism; the largest channel, R_DONE_BUILD / R_DONE_SERVER / R_CORRECTION, holds 20 points each):

| Channel | Mechanism | Graded slots (weight) | Convincing wrong source | Beating record |
|---|---|---|---|---|
| Build membership | R_DONE_BUILD (A24) | ZOM-569 call + blocker list (10) | ZOM-569 Done state and fix note | #2028 start C05433XK267/1759268201.182309 + H1 |
| Server liveness | R_DONE_SERVER (A24) | ZOM-567 call + blocker list (10) | merged, approved harmonygames-Games/match3d-backend#36 | Arthur's withdrawal C08R6BF4ENN/1759261800.335275 + page_cicd_pipeline |
| Latest re-test | R_CORRECTION (A11) | ZOM-435 call + list, ZOM-473 call (15) | C08R27X0EAH/1759140300.935009 #133 pass; Done state | 68dc63484a5b2d0a869e758f; D0770ET1HV2/1759267800.858041 |
| Update-path rule | R_UPDATE_RULE (A15) | filed bug (5) | C08R27X0EAH/1759266600.265963 | f_5e40215b7d4d24b0455412 + page_qa_runbook |
| Alias | R_ALIAS (A7) | ZOM-562 call + list (10) | ZOM-562 cosmetic wording; ZOM-516 | vincent.parker@harmonygames.co/1844730396672762606 + 29016e2ba1a844a2509b847b |
| Filter | R_FILTER (A17) | ART-793, DES-313, ZOM-578 calls (15) + register keys (3) | team ZOM + label Bug view (and the Sep 22 Bug-only tab) | H2 f_632c44650df44fe252ee59 |
| Completion elsewhere | R_COMPLETION (A25) | ZOM-563 call (5) | ZOM-563 In Progress | D079SNE2TL4/1759269524.769369 |

Cross-source v2 trap types: done_gap (T1, T2), superseding correction off the first-read path (T3, T3b, T12), authority (T4), alias (T5) — each names the convincing wrong source and the beating record above. Every miss flips a weight-5 multi-source row (hardness_v2_check DECISION_FLIP 7 of 7). Trap findability varies: T6 is met by any cross-team search, T7 sits in a DM Vincent is in, T3 sits on a Trello card comment, T5 needs a Contacts lookup.

## 7 Deliverables and dependent writes

| Write | Tool | Depends on | Requirement |
|---|---|---|---|
| Register tab in f_0ebfccf33076f9dbf086bc (132 rows; columns ticket, title, build status, QA result, call, evidence) | gsheets_values_update | every mechanism, K1, K6 | R1–R5, R10 |
| Blocker list on ZOM-570 (existing keys only, reuse rule from 68dc3ef455344e471b1d2ea9) | linear_update_issue | R_DONE_BUILD, R_DONE_SERVER, R_CORRECTION, R_ALIAS, R_FILTER | R7 |
| Update-path bug (device, OS, source build per page_release_checklist) | linear_create_issue | R_UPDATE_RULE, K4 | R6, R9 |
| Sign-off reply in thread C08R27X0EAH/1759263900.484190 | slack_send_message | R_UPDATE_RULE, K9, K10 | R8 |

No write is satisfied by doing nothing: the register tab does not exist before the run, ZOM-570 holds no blocker list, the update-path bug does not exist and the thread has no QA reply.

## 8 Service role map

| Service | Role | Weight reason |
|---|---|---|
| slack | candidate builds, re-tests, sign-off destination | C05433XK267 posts decide R2; C08R27X0EAH/1759263900.484190 is the R8 destination |
| linear | cohort, per-ticket QA notes, writes | 132 register rows; comments decide R5; ZOM-570 carries R7 |
| github | fix provenance | merge times vs 18:43Z; harmonygames-Games/match3d-backend#36 for R4 |
| confluence | QA rules | page_qa_runbook R6/R8, page_release_checklist R9, page_cicd_pipeline R4 |
| gmail | external report | vincent.parker@harmonygames.co/1844730396672762606 (vendor session notes) |
| gsheets | destination and format | f_0ebfccf33076f9dbf086bc |
| gdocs | hidden authorities and update-path evidence | H2 f_632c44650df44fe252ee59, H1 f_a038a576ca8db6955fae95 and their older docs; test log f_5e40215b7d4d24b0455412 |
| gdrive | discovery and ownership | Drive search finds the rule docs; owner / sharing rows of f_0ebfccf33076f9dbf086bc and f_5e40215b7d4d24b0455412 |
| gcal | deadline | evt_81e6dc4dbfd331f1a6a317 |
| trello | reuse rule, off-path re-test | 68d1eb90bef538c7c5c5599d |
| contacts | external reporter identity | 29016e2ba1a844a2509b847b |

## 9 Call budget

251 planned unconditional calls over 11 services (hardness_gate call_budget PASS against the requester floor 250); Σ per-record calls 160 against the floor 150; largest non-per-record share 36 %.

| Phase | Calls | Main reads |
|---|---|---|
| discovery | 12 | ZOM-570 + comments, the candidate thread, three Confluence pages and their comments |
| rules | 20 | Drive searches and the four rule docs (H1, H2 and their older docs), gate sheet tabs, Drive lookups, go/no-go, Trello card, Contacts, vendor mail, test log |
| enumeration | 41 | open ZOM pages, Done since Sep 22, ART/DES, #builds and #zombie-bugs Sep 22–30 pages, DMs, #zombie-ops, PR lists, mailbox search |
| per-record | 160 | 132 linear_list_comments, 15 fix traces, 13 re-test thread reads |
| reconciliation | 9 | post-cut commit / #2028, match3d-backend#36 merge state and review, change lists of #135 / #50 / #2028, existing-ticket checks |
| writes + read-back | 9 | sheet tab + values, ZOM-570 update, new bug, thread reply, read-backs |

## 10 QC rails

### Two-reading table (decision points)

| Decision point | Best reading | Strongest alternative | Resolved by |
|---|---|---|---|
| D1 register destination | new tab in f_0ebfccf33076f9dbf086bc | a new spreadsheet | K6 ("How we gate" tab) and A3 |
| D2 scope | every open ZM ticket any team/label + Done since gate, minus ZOM-570 / ZOM-359 / ZOM-475 | team ZOM + label Bug | H2 f_632c44650df44fe252ee59 |
| D3 build membership | main at job start | release branch (Sep 2 doc) | H1 f_a038a576ca8db6955fae95 supersedes f_fcb4f7c9b508088e0d5803 |
| D4 server fix live | deployed to prod only | merged = live | H1 + page_cicd_pipeline + C08R6BF4ENN/1759261800.335275 |
| D5 QA result | latest re-test on #135 / #50 (or prod) | Done state / older #133 pass | H2 + 68dc63484a5b2d0a869e758f, D0770ET1HV2/1759267800.858041 |
| D6 matrix verdict | update row failure blocks | green summary clears | page_qa_runbook ("A failure in any UPDATE column blocks the release") |
| D7 vendor report | ZOM-562, blocker | new ticket / ZOM-516 | 29016e2ba1a844a2509b847b + report symptoms |
| D8 sign-off location | reply in C08R27X0EAH/1759263900.484190 | new channel post | K9 + K10 cmt_zom570_1 |

### Unique ground truth notes

- Graded calls only on tickets whose call follows from incorporated records: the 14 mechanism slots plus 10 sample slots (ZOM-559, ZOM-560, ZOM-481, ZOM-458, ZOM-564, ZOM-506, ZOM-557, ZOM-561, ZOM-513, ZOM-387).
- Never graded: build status of ZOM-169, ZOM-434, ZOM-507, ZOM-538, ZOM-558 (no fixing change found in base); any beta date (SC-13); ZOM-475 (SC-8); Linear state as proof of shipping (SC-16).
- Call vocabulary (gate sheet, f_0ebfccf33076f9dbf086bc): BLOCKER, KNOWN ISSUE, FIXED, NO CALL; build status: in candidate, not in candidate, server (live / not live).
- Store version 1.3.24 (release/1.3.24_HotFix, C05433XK267/1756826078.213299) is N-1; the N-2 string is chosen at injection after a TestFlight mail check (no 1.3.22/1.3.23/1.3.25 string exists in Slack Jul–Sep 2025).

### Reach table (load-bearing records)

| Record | Service | Visibility path |
|---|---|---|
| C05433XK267/1759257934.076209 | slack | public #builds, member |
| C05433XK267/1759257812.041449 | slack | public #builds, member |
| C05433XK267/1759268201.182309 | slack | public #builds, member |
| C05433XK267/1759263189.219529 | slack | public #builds, member |
| C08R27X0EAH/1758485492.586459 | slack | private #zombie-bugs, member |
| C08R27X0EAH/1758409417.505029 | slack | private #zombie-bugs, member |
| D079SNE2TL4/1759256193.859279 | slack | Vincent's DM with Douglas |
| D079SNE2TL4/1759269524.769369 | slack | Vincent's DM with Douglas |
| C08R27X0EAH/1759263900.484190 | slack | planned seed in #zombie-bugs (member) |
| C08R27X0EAH/1759266600.265963 | slack | planned seed, reply in the candidate thread |
| C08R27X0EAH/1759140300.935009 | slack | planned seed in #zombie-bugs |
| C08R6BF4ENN/1759261800.335275 | slack | planned seed in private #zombie-ops (member, YES at channel level) |
| D0770ET1HV2/1759267800.858041 | slack | planned seed in Vincent's DM with Brian |
| f_632c44650df44fe252ee59 | gdocs | planned seed, shared with Vincent |
| f_a038a576ca8db6955fae95 | gdocs | planned seed, shared with Vincent |
| vincent.parker@harmonygames.co/1844730396672762606 | gmail | planned seed, own mailbox |
| f_0ebfccf33076f9dbf086bc | gsheets | planned seed, owned by Vincent |
| f_5e40215b7d4d24b0455412 | gdocs | planned seed, owned by Brian, shared with Vincent |
| evt_81e6dc4dbfd331f1a6a317 | gcal | planned seed, Vincent's own calendar copy |

Linear, GitHub, Confluence, Trello and Contacts are unscoped (persona_view reach UNSCOPED line).

## 11 Record plan for /create-injection

| Service | Record | Carrier | Id scheme |
|---|---|---|---|
| linear | ZOM-570 release ticket (Arthur, In Progress, 2025-09-30T20:20Z) naming #135 / #50, delegating K1/K2/K7/K8/K9/K10 | ● | next ZOM number (max base ZOM-566) |
| linear | ZOM-567 Done (Vincent reports, Douglas fixes; chest rewards not granted; completed after harmonygames-Games/match3d-backend#36 merges) | ● | next ZOM number |
| linear | ZOM-568 open control (cosmetic, known issue) | ● | next ZOM number |
| linear | ZOM-569 Done 2025-09-30T21:45Z (season pass screen opens twice from the join popup, player stuck; fixed-on-main note before completion) | ● | next ZOM number |
| linear | ZOM-571 to ZOM-580 Sep 30 QA-pass tickets (ZOM-578 by Leonard, no label, tutorial lock) | ● | next ZOM numbers |
| linear | ART-793, DES-313 ZM defects filed in other teams (ZM in the title) | ● | max base ART-792, DES-312 |
| linear | ≈ 60 QA comments (Sep 22 gate notes; Sep 29 #133 notes incl. cmt_zom559_1 Brian; Sep 30 #135 / #50 re-checks; settling notes from cohort_plan.json; re-test on ZOM-564; cmt_zom570_1 Leonard) | ● | cmt_ + lower-case key + _n (cmt_zom559_1); none after a ticket's completed_at |
| gdocs / gdrive | H2 f_632c44650df44fe252ee59, H1 f_a038a576ca8db6955fae95, older docs f_fcb4f7c9b508088e0d5803 and f_5ae4332fb6927f84b3afdc | ● | f_ + 22 hex, absent in 53,631 Drive rows (positive control found) |
| gmail | vendor vincent.parker@harmonygames.co/1844730396672762606 and Arthur's go/no-go invitations | ● | X-GM-THRID ≈ unix_ms << 20; collision-checked (0 hits, positive control found) |
| contacts | vendor entry 29016e2ba1a844a2509b847b (company, ZM3D playtest sessions) | ● | sha256 seed, 24 hex |
| slack | C08R27X0EAH/1759263900.484190, C08R27X0EAH/1759266600.265963, C08R27X0EAH/1759140300.935009, C08R6BF4ENN/1759261800.335275, D0770ET1HV2/1759267800.858041 | ● | ts unique per channel; message id sha256(channel + "\|" + ts)[:32] |
| github | harmonygames-Games/match3d-backend#36 (Douglas, Arthur's APPROVED review 18:42Z, merged 2025-09-30T18:50Z, after Douglas's 18:16Z prod update) | ● | max base #35 |
| gsheets / gdrive | f_0ebfccf33076f9dbf086bc "ZM3D Release Gate" (How we gate + Sep 22 tab) | ● | f_ + 22 hex, absent in 53,631 Drive rows |
| gdocs / gdrive | f_5e40215b7d4d24b0455412 update-path test log (iOS #50 / Android #135 rows) | ● | f_ + 22 hex |
| gcal | evt_81e6dc4dbfd331f1a6a317 (+ copies evt_d34d72261b883c1a285de5, evt_40c763ed7be17970259e98, evt_72891de7fbc58565c320f1, evt_f09b055d3d8c76a549df77), uid 19c1511dd209208f50aabe12f04a6d44@hg4 | ● | evt_ + 22 hex, one row per attendee calendar |
| trello | actions 68dc3ef455344e471b1d2ea9 (Arthur 20:35Z) and 68dc63484a5b2d0a869e758f (Leonard 23:10Z) on 68d1eb90bef538c7c5c5599d | ● | first 8 hex = unix seconds |

Id collision checks: research/tmp_ids/ (lookups with positive controls for gdrive, gsheets, gdocs, gcal, trello, contacts, slack; gmail by literal search over vincent@ thread files with control dgTv2AULAN2Ou0_cjrtPAZlfP5MG4PxZbHbQ4n9ZCQ found, research/tmp_ids/gmail_check.txt).

### Integrations and companions

| Seeded service | Integration (integrations.json) | Companion | Decision |
|---|---|---|---|
| github | INT-01 | #zombie-prs mirror C093LEZGF6J (match3d only) | none: match3d-backend is outside the mirror list |
| github | INT-03 | linear[bot] PR comment | seed one on harmonygames-Games/match3d-backend#36 only if the repo's era carries linear[bot] comments (check at injection) |
| github | INT-12 | GitHub notification mail | none: Vincent is not a reviewer on match3d-backend#36 |
| linear | INT-04 | Linear Slack app notice | none: base rate in C08R27X0EAH is 26 messages, not owed |
| linear | INT-05 | Linear e-mail digest | none: digests are batched, not per issue |
| gcal | INT-11 | invitation mail | Arthur's invitation seeded in the Vincent, Leonard, Brian and Robert mailboxes |
| gdrive | INT-13 | Drive Slack app DM on share | add one share DM to Vincent for f_5e40215b7d4d24b0455412 at injection if the base rate holds for docs shared by Brian |
| slack | INT-22 | Slack e-mail notification | none: low base rate for private channels |
| trello | INT-21 | Trello → Slack | none exists (no bot post seeded) |

## 12 Self-test results

Lazy-solver walk (ZOM-570 → its comments → the candidate thread → the team-ZOM Bug list → Done states):

- It lists team ZOM + Bug and misses ART-793, DES-313, ZOM-578 (T6) and rows for non-Bug tickets (V01 register keys).
- It calls ZOM-569 and ZOM-567 FIXED from their Done states (T1, T2) and ZOM-435 / ZOM-473 FIXED from Done and the #133 pass (T3, T3b).
- It accepts Brian's green summary C08R27X0EAH/1759266600.265963 and files no update-path bug (T4).
- It reads ZOM-562 as cosmetic and never opens Contacts (T5).
- It calls ZOM-563 a blocker from its In Progress state (T7).
- A careful run that opens H1, H2, the runbook, the test log, the Trello card, the DMs and Contacts gets every graded slot; the D02 sign-off holds whatever the traps decide (base blockers ZOM-546, ZOM-560).

## 13 Red team

RED TEAM FALLBACK: requester waived the scenario red team on 2026-11-04 (D4 'Waive review'; REDTEAM_* not set, so redteam_review.py --dual cannot run). Stand-ins: hardness_gate --design, hardness_v2_check, trap_liveness, gradable_surface validate, the pre-registered forecast hev_8e7818337147979b and the self-review below (learnings §44). The prompt and injection stages keep their own reviews.

| Finding | Source | Disposition |
|---|---|---|
| SAME_PLACE T9: correction in the anchor ZOM-570 | hardness_v2_check (first run) | fixed: T9 recast as a lookalike distractor; T12 (ZOM-559, cmt_zom559_1) carries the fourth supersession off the first-read path |
| SAME_PLACE T8 unresolved container for C05433XK267/1756826078.213299 | hardness_v2_check (first run) | fixed: version_records containers declared |
| D02 P(fail) 0.91 in the first forecast | hardness_forecast | fixed: the sign-off call holds on base blockers ZOM-546 / ZOM-560, so its mechanism list was removed |
| breadcrumb flags T1, T5, T6, T8, T11 | trap_liveness | keep the link: each is the hub's delegation to H1 / H2 (fairness link); the difficulty stays in applying the rule per record (commit time vs job start, alias mapping, cross-team filter) |

## 14 Revision at injection intake (design_delta)

Changes made while implementing the SQL (`/create-injection`); the draft manifest and surface were regenerated by `scenario_gen/build_design.py` and every gate below re-run. No element id was dropped.

| Element | Change | Reason (evidence) |
|---|---|---|
| H1, H2, K1, K1b, K2, K2b, T8, T11 | rule notes moved from Gmail to Google Docs shared with Vincent (f_632c44650df44fe252ee59, f_a038a576ca8db6955fae95, older docs f_5ae4332fb6927f84b3afdc, f_fcb4f7c9b508088e0d5803) | no 2025 colleague-to-colleague mail exists in vincent@ / leonard@ / blake@ (research/voice_keywords.md), while Leonard shares 27 files with Vincent (persona_view reach); docs are the realistic home |
| H2 decoy | the July rule now covers ZM TestFlight beta drops (decoy_scope lot) instead of Domino Delights maintenance builds | the DD version would contradict page_release_checklist ("Run full store + update checks even on maintenance-mode builds") |
| T8 | the Sep 2 hotfix doc is dated 15:40Z, after Android Submission #107 C05433XK267/1756826078.213299 | base_claims B2: a release branch is named only once it exists |
| T2 | the correction is now Arthur withdrawing his GitHub approval of harmonygames-Games/match3d-backend#36 in #zombie-ops (C08R6BF4ENN/1759261800.335275), with version_records github → slack | requester learning: a done that isn't, plus a correction elsewhere (GitHub approval withdrawn in Slack), both kept in the data |
| T3, T12 | Vincent's #133 pass C08R27X0EAH/1759140300.935009 and Brian's ZOM-559 note cmt_zom559_1 moved to Mon Sep 29 | #133 / #49 only exist from 2025-09-26T23:20Z; weekend dates warned by sql_lint |
| T4, T10 | Brian's green reply C08R27X0EAH/1759266600.265963 moved to 21:10Z, before his update-path doc (22:05–22:35Z); his fresh-install matrix f_b91db376f65604b8602657 added | the green claim is a dated summary his later doc overturns, never the same person contradicting himself at the same time |
| S22, S25, S27; R_DONE_BUILD, R_CORRECTION, R_ALIAS controls | ZOM-483 → ZOM-481, ZOM-536 → ZOM-506, ZOM-498 → ZOM-561; controls ZOM-506 / ZOM-557 / ZOM-561 and ZOM-546 / ZOM-504 | ZOM-483 (lost infinite-life minutes) and ZOM-536 / ZOM-498 (art and UI polish) admit two fair calls; ZOM-516 is not a register key |
| V01 | class aggregate → delivery | a register_keys_exact selector is graded from the write, not the solver (oracle_kit contract.slots) |
| K9, K10 | delegation quotes settled from the ZOM-570 text | the quotes must be verbatim in the delegating record |
| R1, R5, T3b, T6 (local review, 2026-11-04) | H2's scope sentence now excludes Done / Canceled / Duplicate explicitly and its loss list names lives; ZOM-449's Sep 30 note, Brian's ZOM-473 DM and Vincent's Sep 30 fixes post (now also ZOM-434, ZOM-558) state their outcome plainly; ZOM-570 asks for blockers by key, reusing the existing ticket | the local /prompt deep recheck found second fair calls on ZOM-483, ZOM-449, ZOM-473, ZOM-434 / ZOM-558 and the Duplicate / Canceled rows; each is settled in the records, not the prompt |
| R1, R5, R7, R10, A1 (platform review 6ae9909f7b5249d3148f3707) | H2's severity paragraph separates requests (art, animation, VFX, text style, UI layout, requests for design, balance or tuning changes) and tickets that don't say what goes wrong from bugs, keeps bugs that don't change play as known issues, moves the orange-juice example to the level clause, and limits the Done rule to bugs; ZOM-564's note covers both candidates; H2 (Sep 23) gives tickets filed while a later gate is running a row (the new update-path ticket included); ZOM-570 speaks of the invite, the post and the Trello rule in the future; H1 explains the one-line iOS Changes blocks | the platform /prompt review found second fair calls on ZOM-564, ZOM-536 / ZOM-555 / ZOM-419 / ZOM-498, ZOM-293 / ZOM-453, ZOM-438 / ZOM-443 and the new-ticket row, plus three minor coherence slips; truth moves only on ZOM-453 (KNOWN ISSUE → NO CALL, ungraded) |
| R5 (platform /prompt re-run) | Leonard settles ZOM-558 (a bug, so FIXED on Vincent's check) and ZOM-477 (a tuning ask, NO CALL) in dated comments on the tickets | the two register rows each fit two rule sentences; per-ticket notes avoid rewording rules that other rows depend on |
| R10, A3, R8 (platform /prompt re-run 2 and requester volume / difficulty targets) | How we gate defines each build-status value; T05 grades ZOM-473 on the release ticket as well as in the register | the build-status fork on ZOM-429 / ZOM-517; the requester wants over 130 calls a run and under 80 % pass rate, so the hardest single-slot trap (Brian's Turkish DM re-test) gets a second graded write (V3 §9 caps a fact at two slots) |
| T2 companions (local review) | match3d-backend#36 gets its head commit and commit row, the repo push stamp follows the merge, the ZM ROADMAP board stamp follows the newest comment | base invariants broken by the first SQL (dossier §12) |

## Self-review

Tool outputs (verbatim, re-run after the injection-intake revision):

```
HARDNESS GATE (extreme (design)): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: skipped (--design: no SQL yet)
  [ok] base_consistency: skipped (--design: no SQL yet)
  [ok] services_injected: skipped (--design: no SQL yet)
  [ok] rows: skipped (--design: no SQL yet)
  [ok] services_carrying_weight: 11 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: skipped (--design: no SQL yet)
  [ok] seeded_ids_exist_in_sql: skipped (--design: no SQL yet)
  [ok] anchors: 3 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 12 fragments; need ≥ 12
  [ok] ask_fragment_services: 7 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 10 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 10 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 132; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 3 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 160; need ≥ 150
  [ok] call_budget: unconditional (verified) floor 251 of 251 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 250 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 11 services in budget; largest share outside the per-record phase 36% (≤ 50%)
  [ok] traps: 16 traps across 7 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 6 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (4 with versions in ≥ 2 services, 2 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 6 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 12 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 6 chains with 6 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 7 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 2 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 5 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 10 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 4 writes over 3 services; each must depend on findings
  [note] volume_exception: call-budget floor 250 and per-record floor 150 replace 500 and 300; every other extreme target applies — reason: Honest necessary calls top out near 260 (about 155 per record): only Linear comm; requester confirmation: The requester (task owner) chose floors 250 / 150 with the widest scope in this 
```

```
GRADABLE SURFACE (01_Gradable_Surface.json): PASS · 28 slots · weight 108 · mechanism share 72.2% (reported, not gated) · weight by class {'direct': 71, 'write_content': 33, 'delivery': 4}
```

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      5 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 6 requirements: {'R2': ['R_DONE_BUILD'], 'R4': ['R_DONE_SERVER'], 'R3': ['R_CORRECTION', 'R_COMPLETION'], 'R6': ['R_UPDATE_RULE'], 'R5': ['R_ALIAS'], 'R1': ['R_FILTER']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   7 of 7 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · DESIGN (no SQL: record text unavailable, only manifest-structure flags can fire) · on the Season Pass backtests these are development fixtures, not validation
  hub ZOM-570 · direct delegations 8 · rule placement: A15 nodes only: ['CH3', 'T4'] (mechanism_portfolio); every other node SKIP
  T1   done_gap           breadcrumb  [rule placement SKIP: not an A15 node]
  T2   done_gap           -  [rule placement SKIP: not an A15 node]
  T3   superseding        -  [rule placement SKIP: not an A15 node]
  T3b  superseding        -  [rule placement SKIP: not an A15 node]
  T4   authority          -
  T5   scope_alias        -  [rule placement SKIP: not an A15 node]
  T6   exact_predicate    breadcrumb  [rule placement SKIP: not an A15 node]
  T7   completion_elsewhe -  [rule placement SKIP: not an A15 node]
  T8   superseding        breadcrumb  [rule placement SKIP: not an A15 node]
  T9   distractor         -  [rule placement SKIP: not an A15 node]
  T10  distractor         -  [rule placement SKIP: not an A15 node]
  T11  distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  T12  superseding        -  [rule placement SKIP: not an A15 node]
  T13  distractor         -  [rule placement SKIP: not an A15 node]
  T14  distractor         -  [rule placement SKIP: not an A15 node]
  T15  distractor         -  [rule placement SKIP: not an A15 node]
  dispositions: 0/4 recorded
```

Forecast: the design forecast hev_8e7818337147979b (UNCALIBRATED) was pre-registered before the injection-intake revision (same seven rules, three sample slots swapped): E[avg] 0.70, P(all four gates) 0.52–0.54. The injection forecast on the implemented SQL is hev_f85c6533779173e8 (Working_Files/01c_Forecast.json, reported in the dossier with every view).

| Check | Verdict | Strongest counter-reading | Resolution (evidence) | Unresolved |
|---|---|---|---|---|
| Temporal | PASS | ZOM-569's fix could have landed before 18:45Z | Android #2027 started 21:21Z without it (C05433XK267/1759267266.044859) and #2028 started 21:36Z with it (C05433XK267/1759268201.182309) | none |
| Semantic / category | PASS | "Submission Blocker" label could define blockers | S03: the call follows H2's severity rule; labels never decide (ZOM-427, ZOM-237) | none |
| Cross-service referential | PASS | the vendor report could map to ZOM-516 or ZOM-546 | ZOM-516 is a closed Duplicate about endless mode; ZOM-546 is a draining refill; only ZOM-562 is boss-arena orphan singles (T13) | none |
| Quantitative | PASS | the register key count could differ by one (ZOM-570, ART-792 Team Epic) | scope_keys.json 132 keys; ZOM-570 excluded by H2; ART-792 open (not Done/Canceled/Duplicate) and ZM in title | none |
| State / lifecycle | PASS | ZOM-292 / ZOM-387 (L03) could be called FIXED | both are NO CALL whatever shipped (tooling / analytics), so no state reading changes their row | none |
| Identifier / format | PASS | a seeded id could collide with base | every minted id absent with a positive control (research/tmp_ids/, gmail_check.txt); ZOM-567+ / ART-793 / DES-313 / match3d-backend#36 above base maxima | none |
| Other | PASS | the D0770ET1HV2 "DM" has 5 members, so the re-test could be read as a group post | it is still Vincent's conversation (YES in persona_view); the re-test names iOS #50 and ZOM-473's symptom | none |
| Decision point D1 | PASS | a new spreadsheet could be the register | K6 "How we gate" in f_0ebfccf33076f9dbf086bc fixes a new tab in Vincent's sheet | none |
| Decision point D2 | PASS | ENG-2258 mentions ZM features and could be in scope | H2 limits other teams to tickets with ZM / ZM3D in the title; ENG-2258 is a Domino Delights ticket | none |
| Decision point D3 | PASS | the Sep 2 release-branch note could still apply | H1 (Sep 24) supersedes it; #135 / #50 posts say "main" (C05433XK267/1759263189.219529) | none |
| Decision point D4 | PASS | Arthur's APPROVED review on #36 could be read as still standing | his later #zombie-ops message takes the approval back and keeps #36 on dev; page_cicd_pipeline: deploy is "Run by hand" | none |
| Decision point D5 | PASS | Vincent's own #133 pass could outrank Leonard's comment | H2: the latest result on the candidate builds counts; 68dc63484a5b2d0a869e758f is dated 23:10Z on #135 | none |
| Decision point D6 | PASS | fresh-install-only green could pass the gate | page_qa_runbook: "A failure in any UPDATE column blocks the release" (exact substring verified) | none |
| Decision point D7 | PASS | the vendor report could be a new issue to file | the reuse rule 68dc3ef455344e471b1d2ea9 says existing keys only; symptoms match ZOM-562 | none |
| Decision point D8 | PASS | a fresh #zombie-bugs post could satisfy the sign-off | K10 cmt_zom570_1 and K9 C08R27X0EAH/1759263900.484190 pin a reply in Arthur's thread | none |
| Forecast | PASS | the cap could be breached if Opus reads every DM | E[avg] 0.70 upper interval 0.854 < 0.90 cap; hev_8e7818337147979b | none |
| HARDNESS GATE | PASS | budget padding could carry the 250 floor | every budget row names its decision (research/tool_out/hardness_gate.txt); per-record 160 rests on comment-only QA notes | none |

Unresolved (none blocks the design):

- No independent red team of the scenario or of the implemented records (requester waiver, RED TEAM FALLBACK above); kept here until a review or the Opus pre-check covers it (learnings §44).
- The 21:36Z season pass fix commit is by the redacted [PERSON_NAME_0022]; ZOM-569's note says only that the fix is on main (Oliver Brooks, assignee) and names no author.
- The N-2 store build is named generically in the test log ("store build before the hotfix"); only 1.3.24 has a version string in Slack Jul–Sep 2025, and no slot grades N-2.

```
STAGE GATE scenario: PASS — Task_Authoring/task_inputs · 01_Scenario_Design.md#f833f6b7fc2b · 01_Hardness_Manifest.draft.json#26f87d575654 · 01_Gradable_Surface.json#97ff01c7baf7 · 00_Assigments.md#90d69427cab7 · __context__#fb209f3058d7 · __assignment__#c2f3888d53bd · __policy__#dc4ab5df3cdd · __gate_policy__#835d57ea49b7 · __review__#69c7b8b0a2ca · blocking 0 · warnings 0 · checks 33
[PASS] assignment.v3_context: Vincent Parker / Game Systems Engineer; easy cap <90%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 3 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 7/7 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 44/44 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 2/2 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 15/15 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 22/22 items carry a source pointer (min 90%)
[PASS] evidence.record_plan: 25/25 items carry a source pointer (min 80%)
[PASS] evidence.active_speakers: 7/7 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for vincent.parker@harmonygames.co and matches the re-run (140 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 24 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 6 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (9 INT ids, services ['confluence', 'contacts', 'gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'linear', 'slack', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts ['LIN-OPEN-ZOM']; trap_catalog ['B03', 'C02', 'D02', 'D04', 'D06', 'K02']
[PASS] boundary.anchor_naming: 6 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: red team did not run (missing 01b_Redteam_Review.md, 01b_Redteam_Review.second.md); explicit fallback recorded: requester waived the scenario red team on 2026-11-04 (D4 'Waive review'; REDTEAM_* not set
[PASS] surface.valid: 28 slots, weight 108; geometry report-only, never gated: mechanism share 72%, always-pass share 28%
[PASS] forecast.preregistered: prior forecast pre-registered in the ledger: ['hev_8e7818337147979b', 'hev_f85c6533779173e8'] (UNCALIBRATED, advisory)
[SKIP] revise.intake: no MODE B report and no revision-intake section: nothing to take in
[PASS] reach.scenario: 19 scoped load-bearing ids YES for vincent_parker (11 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 16 evidenced counter-readings (of 17 found; need ≥ 15) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.draft.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] handoff.pasted: pasted into the Self-review by --paste
```











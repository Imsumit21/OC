# Grounding Dossier — julia-zm3d-beta-liveops-calendar · rev14 · contains no prompt, OE or criterion text

Universe synth-cut (`hg4-synth-sep30cut`); Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC); seed bound
`2025-10-01T00:00:00Z`; `context_hash 4bbc727fd48ac35a16b4afeda5430937563f2ce969970841bb4f3f97b6a38a39`. SQL
`01_Universe_Inject.sql` (revision 14, sha256 `edae63f3e838`; 81 INSERT, 30 UPDATE; no DELETE/upsert). Profile extreme,
with a requester-confirmed `volume_exception` (call floor 130 / per-record 75 / rows 70). Every value below is a real
record pointer; this file carries no prompt, Oracle Event or rubric text. What revisions 2 to 14 changed and why is
in §11 (Revision 2 to Revision 14).

## 1.A Structural

Julia Lawson (Product Manager, Product) builds the Zombie Match 3D beta live-ops + push calendar for the four beta buy
weeks (Mon Oct 6 – Sun Nov 2 2025). The injection seeds, across **10 schemas** (slack, gmail, gcal, gdocs, gdrive,
gsheets, gslides, github, linear, trello): Frederick's ask DM, his thread reply under it (the push-plan rows and
Zombie Lane off the calendar) + beta brief Doc + UA plan deck; Julia's "ZM Live Ops"
folder + the Calendar/Pushes sheet skeleton; Robert's #zombie-art Halloween approval and his later DM withdrawal;
Vincent's #zombie-match3d prod re-test; Douglas's Oct 8 backend-release GCal event; Brian's two Season Pass handoff
mails; the live-ops cohort's per-record surfaces (41 members in the manifest since revision 6, 42 in revision 5, 39 in revision 4, 44 in revisions 2 and 3; 32 Linear issue comments on 22 issues: one each on 14, two each on ZOM-563, ZOM-565, ZOM-534, ZOM-566, ZOM-521 and ZOM-432, and three each on ZOM-526 and ZOM-465; GitHub inline
review notes on three cohort PRs (#470, #468, #472) with one seeded review and one timeline event; the three INT-01 `#zombie-prs` mirrors);
Leonard's note on the open Trello quests card (it decides no graded value since revision 5); four thread replies, two in #zombie-bugs, one in #zombie-art and one in #zm-collect-win (none decides a value). The graded deliverable is the two-tab sheet (Calendar keyed by beat, seven beats;
Pushes keyed by push, ten rows), the DM reply to Frederick, the ZOM-78 link, the ZOM-429 hold note (the only held
beat) and the reply to Brian on his slip mail.

## 1.B Entity table

Every seeded author resolves to one person with one account per service (base `entity.py resolve`; no second account).

| Person | Role | Slack | GitHub login (renders) | Other | Source record |
|---|---|---|---|---|---|
| Julia Lawson | Product Manager (persona) | EMPLOYEE_0005_SLACK_ID | PERSON_0005_GITHUB_USERNAME | julia.lawson@harmonygames.co | `slack:D05SD5QLG94/1759263617.418209` |
| Frederick Stone | GM / calendar owner | EMPLOYEE_0008_SLACK_ID | PERSON_2314_GITHUB_USERNAME (renders "Ryan") | frederick.stone@harmonygames.co | `bca784379e7dbca9e64e79a64dfefbba` |
| Robert | Co-Founder & Creative Director (Product) | EMPLOYEE_0016_SLACK_ID | — | `usr_Robert` | `933cee9f6464a80e4b1f05259b595b20` |
| Vincent Parker | QA | EMPLOYEE_0012_SLACK_ID | EMPLOYEE_0012_GITHUB_USERNAME | — | `b5f2955c2e154efc6835946ecfe1758e` |
| Arthur Blake | Eng (reviews) | EMPLOYEE_0025_SLACK_ID | EMPLOYEE_0025_GITHUB_USERNAME | — | `harmonygames-Games/match3d#470#rc_10` |
| Marcus Bennett | Art / VFX | — | PERSON_0396_GITHUB_USERNAME (no seeded GitHub row since revision 4) | `usr_c77c50cc15c5342d` | `cmt_zom465_2` |
| Samuel Turner | Eng | — | EMPLOYEE_0004_GITHUB_USERNAME (no seeded GitHub row since revision 5) | `usr_caafeec2804b3a67` | `cmt_zom432_2` |
| Brian Foster | Live-ops PM | — | — | brian.foster@…, `usr_fc22d5941b2aeb5c` (no seeded Trello row since revision 5) | `cmt_zom526_2` |
| Leonard Hayes | ZM ROADMAP board owner (created card #61) | EMPLOYEE_0038_SLACK_ID | — | trello `PERSON_6094_TRELLO_USER_ID`, `usr_63fffeb4fab5233e` | `68dac8204f1e9a3b7c2d5e61` |
| Douglas | Backend eng | — | — | douglas@harmonygames.co, `usr_cd7849ec043ab3da` | `evt_9a4c2e7f1b3d58e06c7a2f` |
| Calvin Price | Live-ops eng | — | PERSON_0003_GITHUB_USERNAME | `usr_49b9dfa5208d400d` | `cmt_zom543_1` |
| Oliver Brooks | Season Pass owner | — | — | `usr_...` | `cmt_zom552_1` |
| Owen Baker | Analytics | EMPLOYEE_0021_SLACK_ID | PERSON_5877_GITHUB_USERNAME | — | `cmt_zom566_2` |

Identity trap (intended, base pre-existing): GitHub `PERSON_2314_GITHUB_USERNAME` renders the display name **"Ryan"**
but the entity is **Frederick Stone** (`entity.py collisions` INTEGRITY FLAG `name_mismatch_on_email_join`); base
`usr_Victor Barnes` carries an id-with-space. Neither is created by this injection.

## 1.C Voice and realism

Seeded messages match each author's role and the channel register, and follow the base style KB `conventions.json`
(synth-cut). No message addresses a grader or describes the test. Julia posts in 147 visible channels (last post
2025-09-30), so her authorship of the write deliverables is in-character.

Every seeded speaker resolves in `activity.json` with status_at_clock `active_sep_2025_quiet_in_oct` (active through
September, quiet in October — consistent with the Sep 30 synth cut), so each is in-character posting in late September:

- Frederick Stone (`frederick.stone@harmonygames.co`, EMPLOYEE_0008_SLACK_ID) — activity.json `active_sep_2025_quiet_in_oct`; the ask DM `slack:D05SD5QLG94/1759263617.418209` is a PM calendar handoff, and his thread reply under it four minutes later, `slack:D05SD5QLG94/1759263878.305129` (`890dc27f56e8501bd7590ffdfc231057`, 2025-09-30T20:24:38Z, "Two things on top of the brief."), is the same owner adding scope in his own thread.
- Robert (`robert@harmonygames.co`, EMPLOYEE_0016_SLACK_ID) — activity.json `active_sep_2025_quiet_in_oct`; the #zombie-art approval `933cee9f6464a80e4b1f05259b595b20` and the DM withdrawal `669d15f685f158633e56302160957f1e` and, since revision 10, his reply in Martin's desert thread `532747cb5d123a95d13204e57b5a7a38` are terse creative-director calls.
- Vincent Parker (`vincent.parker@harmonygames.co`, EMPLOYEE_0012_SLACK_ID) — activity.json `active_sep_2025_quiet_in_oct`; the prod re-test `b5f2955c2e154efc6835946ecfe1758e` ("I killed the app and reopened it twice"), `cmt_zom556_1`, `cmt_zom563_2` (revision 9, `cmt_zom563_1` until revision 12) and `a08ff7cbfc52008d7dee8457e9385a3c` (revision 10) are QA notes.
- Arthur Blake (`arthur.blake@harmonygames.co`, EMPLOYEE_0025_SLACK_ID) — activity.json `active_sep_2025_quiet_in_oct`; the inline review notes `#470#rc_10`, `#468#rc_38` and `#472#rc_1` are engineering review prose (the last was the conversation note `#473#c_2` in revisions 4 to 7; through revision 3 the last two were `#370#rc_1` and `#438#rc_74`).
- Douglas (`douglas@harmonygames.co`, EMPLOYEE_0031_SLACK_ID) — activity.json `active_sep_2025_quiet_in_oct`; `cmt_zom429_1` is a backend owner progress note, and his one-line reply in #zm-collect-win `7d70c7753179c98b6c8b2b5457a1e5e7` (revision 11) answers Brian's request, and `cmt_zom563_1` (revision 12) is an owner note on his own ticket.
- Calvin Price (`calvin.price@harmonygames.co`, EMPLOYEE_0006_SLACK_ID) — activity.json `active_sep_2025_quiet_in_oct`; `cmt_zom543_1` is a live-ops engineer flow note, and `cmt_zom526_3` (revision 6) and `cmt_zom521_2` (revision 7) are short notes on his own queue-manager and VFX work.
- Marcus Bennett (`marcus.bennett@harmonygames.co`, EMPLOYEE_0002_SLACK_ID) — activity.json `active_sep_2025_quiet_in_oct`; `cmt_zom465_1` and `cmt_zom465_2` are art / VFX notes on his own ticket (the second was the GitHub comment `#454#c_4` through revision 3).
- Samuel Turner (`samuel.turner@harmonygames.co`, EMPLOYEE_0004_SLACK_ID) — activity.json `active_sep_2025_quiet_in_oct`; `cmt_zom432_2` is an engineering ship note on the ticket he closes (through revision 4 it was the PR comment `#471#c_18`).
- Oliver Brooks (`oliver.brooks@harmonygames.co`, EMPLOYEE_0003_SLACK_ID) — activity.json `active_sep_2025_quiet_in_oct`; `cmt_zom552_1` is a Season Pass owner note.
- Owen Baker (`owen.baker@harmonygames.co`, EMPLOYEE_0021_SLACK_ID) — activity.json `active_sep_2025_quiet_in_oct`; `cmt_zom566_2` is an analytics note.
- Brian Foster (`brian.foster@harmonygames.co`, EMPLOYEE_0026_SLACK_ID) — activity.json `active_sep_2025_quiet_in_oct`; the two handoff mails are live-ops PM notes (the Trello quests note is Leonard's since revision 5); `cmt_zom526_1` and the revision-3 `cmt_zom526_2` are his short notes on a ticket he created (Linear `usr_fc22d5941b2aeb5c`), and `cmt_zom566_1` (revision 9), `cmt_zom565_2` (revision 10) and `cmt_zom465_3` (revision 11) are his steers on three others.
- Leonard Hayes (`leonard.hayes@harmonygames.co`, Trello `PERSON_6094_TRELLO_USER_ID`) — activity.json `active_sep_2025_quiet_in_oct`; the Trello note `68dac8204f1e9a3b7c2d5e61` on the open quests card he created is a one-line roadmap note (he has 4,019 base Trello actions); `e343557b2e94a1701251ebd079e6f0ce` and `cmt_zom534_2` (revision 9, moved in revision 10) are his own re-checks of what he reported.

## 1.D Keyword

New seeded identifiers (absent from base; see §1.F). Each bullet lists the ids introduced in that service:

- Slack message ids `bca784379e7dbca9e64e79a64dfefbba`, `890dc27f56e8501bd7590ffdfc231057` (revision 2), `933cee9f6464a80e4b1f05259b595b20`, `669d15f685f158633e56302160957f1e`, `b5f2955c2e154efc6835946ecfe1758e` (= `sha256('<channel>|<ts>')[:32]`; revision 5 re-timed all five, so all five ids are new), and the thread replies `e343557b2e94a1701251ebd079e6f0ce`, `a08ff7cbfc52008d7dee8457e9385a3c` and `532747cb5d123a95d13204e57b5a7a38` (revision 10), and `7d70c7753179c98b6c8b2b5457a1e5e7` (revision 11).
- Gmail `julia.lawson@harmonygames.co/1843954828968533812`, `julia.lawson@harmonygames.co/1844311412966040123` (new in revision 5: thread ids are per mailbox and encode the send time; Brian's and Frederick's copies carry their own).
- GCal `evt_9a4c2e7f1b3d58e06c7a2f` (+ attendee copies `evt_5c1e83a7d94b02f6c8e31a` Julia, `evt_a72f4d9e0c1b58d3e6f40b` Owen, `evt_1d6b9a03e5c27f84b0d92c` Frederick).
- Drive family `f_7c3e91a4d2b85f60e1a9c4` (brief), `f_2b9d4e7a1c63f08d5e7b21` (deck), `f_e4a17c90b3d25f6a8c1d73` (sheet), `d_5f2c8e1b7a94d03c6e2b58` (folder).
- GitHub `#470#rc_10` (inside the base review `#470#rev_9`), `#468#rev_3`/`#468#rc_38`, `#472#rc_1` (inside the base review `#472#rev_1`) (+ timeline event `#468#ev_6`). Revision 8 removed `#473#c_2` and `#473#ev_5`; revision 5 removed `#470#rev_10`, `#470#ev_9`, `#471#c_18` and `#471#ev_8`; revision 4 removed `#370#rev_1`/`#rc_1`, `#438#rev_4`/`#rc_74` and `#454#c_4` with their events.
- Linear 32 comments: 22 first notes, `cmt_zom78_1` … `cmt_zom566_1`, one per issue (`cmt_zom563_1` is new in revision 9 and Douglas's since revision 12, `cmt_zom566_1` is Brian's since revision 9, and `cmt_zom387_1` left in revision 5); eight second notes `cmt_zom526_2` (revision 3), `cmt_zom465_2` (revision 4), `cmt_zom432_2` (revision 5), `cmt_zom521_2` (revision 7), `cmt_zom534_2` and `cmt_zom566_2` (revision 9), `cmt_zom565_2` (revision 10) and `cmt_zom563_2` (revision 12); and the third notes `cmt_zom526_3` (revision 6) and `cmt_zom465_3` (revision 11).
- Trello action `68dac8204f1e9a3b7c2d5e61`.
- NEW TERM: none (all reuse base vocabulary).

## 1.E Persona reach

`persona_view reach julia_lawson`: **SLACK visible channels = 147** (`mpim 52, public 23, private 47, im 25`),
messages 238131, persona posts 31848, last activity 2025-10-01. Linear / Trello / GitHub are unscoped (always readable
per `Evals/references/persona/acl.md`).

Load-bearing scoped records Julia must read (re-verified YES by `persona_view check-sql`, verdict PASS):

| Record | Service | Basis for YES |
|---|---|---|
| `slack:D05SD5QLG94/1759263617.418209` | slack | her own DM with Frederick (im) |
| `slack:D05SD5QLG94/1759263878.305129` | slack | her own DM with Frederick (im); thread reply under the ask |
| `slack:C08R8CHB0QL/1758213623.552919` | slack | member of #zombie-art |
| `slack:D05GU6L0XFH/1759270241.638119` | slack | her own DM with Robert (im) |
| `slack:C0880U9751A/1759265412.481909` | slack | member of #zombie-match3d |
| `julia.lawson@harmonygames.co/1843954828968533812` | gmail | INBOX copy (Brian → Julia) |
| `julia.lawson@harmonygames.co/1844311412966040123` | gmail | INBOX copy (Brian → Julia) |
| `f_7c3e91a4d2b85f60e1a9c4` | gdocs | shared with Julia (reader) |
| `f_2b9d4e7a1c63f08d5e7b21` | gslides | shared with Julia (reader) |
| `f_e4a17c90b3d25f6a8c1d73` | gsheets | owned by Julia |
| `d_5f2c8e1b7a94d03c6e2b58` | gdrive | owned by Julia |
| `evt_5c1e83a7d94b02f6c8e31a` | gcal | her own calendar copy of the release event |

The three `#zombie-prs` (`C093LEZGF6J`) INT-01 mirrors (four in revision 4, five through revision 3) are **NOT load-bearing** — UNVERIFIED-OK: Julia is not a member of the public channel (12 members, no EMPLOYEE_0005), so `check-sql` reports them UNVERIFIED by design; the deciding comment text is reached only through the per-PR GitHub calls (see §9); alternate_evidence_ids: harmonygames-Games/match3d#470#rc_10 harmonygames-Games/match3d#468#rc_38 harmonygames-Games/match3d#472#rc_1 (GitHub unscoped, always readable).

The deciding GitHub comment text is reached through the per-PR review and inline-comment calls, which are unscoped and
always readable; the mirror is therefore inert to both solver and verifier.

## 1.F Collision

All seeded ids are unique in their collections (`base_check` Check A on the revision-10 SQL, PASS, re-run on 2026-11-06: Slack,
Gmail threads and messages, gcal, Drive/Docs/Slides/Sheets, GitHub reviews / review_comments / pr_comments / timeline,
Linear comments and Trello actions; the platform `/injection` complete scans date from revision 2). The eleven Slack ids
(eight messages people wrote, three mirrors) are `sha256('<channel>|<ts>')[:32]` of their ts values, none of
which base holds; GitHub suffixes `#470#rc_10`, `#468#rev_3/#rc_38/#ev_6` and `#472#rc_1` are the next free per PR
(base #470 holds `rc_1`-`rc_9` and the review `rev_9` the note now belongs to; #468 holds `rev_1`-`rev_2`, 37 inline
comments and `ev_1`-`ev_5`; #472 holds the review `rev_1` the note belongs to and no inline comment); Linear comments (`cmt_zom<n>_1`) sit on issues with zero
base comments, `cmt_zom526_2`, `cmt_zom465_2`, `cmt_zom432_2`, `cmt_zom521_2`, `cmt_zom534_2`, `cmt_zom566_2`, `cmt_zom565_2` and `cmt_zom563_2` are second comments (sequence 2) on their issues and
`cmt_zom526_3` and `cmt_zom465_3` are the third on ZOM-526 and ZOM-465;
Brian's two Message-IDs and the six per-mailbox thread ids are absent from base; the Trello action `68dac820…` prefix is
absent from the base action export. No id is a prefix/suffix of a longer id.

## 2 Record ledger

Role legend: DEC = deciding (a graded value reads it); DIST = over-application distractor; CERT = certify-absence read;
AUTH = hidden authority; ANCHOR/DEST = ask/destination; COMP = integration companion; VR = version record.

| Record | Service | Role | Basis |
|---|---|---|---|
| `bca784379e7dbca9e64e79a64dfefbba` (`D05SD5QLG94/1759263617.418209`) | slack | ANCHOR (A1) | Frederick's ask DM, 2025-09-30T20:20:17Z (root; `reply_count` 1, `latest_reply` `1759263878.305129`). Text as reworded in revision 4: the calendar goes in the sheet and on the calendar ticket, "Then send me your recommendation back here, with the trade-offs, on what we run and what we hold in those weeks.", and "The working rules for the calendar are in my brief, shared with you." Re-timed in revision 5 (off the whole minute, ts ending in 9) |
| `890dc27f56e8501bd7590ffdfc231057` (`D05SD5QLG94/1759263878.305129`) | slack | DEC (R_ASK_FOLLOWUP, T15 / K17; push-plan rows, Zombie Lane off) | Frederick's thread reply under his own ask, 2025-09-30T20:24:38Z: PNs Beta tab one line per row, local notifications included, four named rows left off; copy that names no game may go out; Zombie Lane off the calendar |
| `933cee9f6464a80e4b1f05259b595b20` (`C08R8CHB0QL/1758213623.552919`) | slack | VR (T2, superseded) | Robert's Halloween approval, 2025-09-18T16:40:23Z, a reply under Martin's base post `9025d428…` |
| `669d15f685f158633e56302160957f1e` (`D05GU6L0XFH/1759270241.638119`) | slack | DEC (R_WITHDRAWN, T2) | Robert's later withdrawal, 2025-09-30T22:10:41Z, which since revision 9 opens "Coming back on the themed prop set I okayed in Martin's thread: pulling my ok." (his approval says "one themed prop set only"), a top-level message in his DM with Julia (thread fields NULL since revision 4; through revision 3 it was a reply under his Sep 30 pivot question `c5431028…`, an unrelated parent the SQL no longer touches) |
| `b5f2955c2e154efc6835946ecfe1758e` (`C0880U9751A/1759265412.481909`) | slack | DEC (R_TECH_HOLD, T7) | Vincent's prod re-test, 2025-09-30T20:50:12Z, a root post in #zombie-match3d |
| `julia.lawson@harmonygames.co/1843954828968533812` | gmail | VR (T8, superseded) | Brian handoff (Wed Oct 29), sent 2025-09-22T09:12:41Z, message `<CAPT--p4sBC8XnaA7qBDMtZkWqJPiXP0MT3deOQGPusOZhHF+vo@mail.gmail.com>`. Revision 5 gives both mails his base Message-ID shape, a `+0300` Date header, plain addresses in To and Cc, no Reply-To and a thread id per mailbox that encodes the send time; Julia's copy of this one carries the label her mailbox uses for opened mail. Revision 6: its body says "Nothing else changes." (base has no September handoff), `in_reply_to` and `references` are '' on all six rows, and Brian's sent copies carry `["ARCHIVED","SENT","Label_b19fb8d1b3"]` |
| `julia.lawson@harmonygames.co/1844311412966040123` | gmail | DEC (R_HANDOFF_SLIP/R_LOCK_BOUNDARY, T8/T9) | Brian slip (Fri Oct 31 10:00 Istanbul), sent 2025-09-26T07:40:26Z, message `<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>`. A mail of its own since revision 4: subject "ZM3D Season Pass November config handoff: new date", no In-Reply-To or References, snippet cut from its own body, and the body ends "If the new date is a problem on your side, reply on this mail." Revision 5 changes the ids (three mailbox copies, each with its own thread id); Julia's copy is not opened yet and carries no UNREAD label, which her mailbox never uses |
| `evt_9a4c2e7f1b3d58e06c7a2f` (+ 3 attendee copies) | gcal | AUTH H3 / DEC (R_DONE_DEPLOY, T1) | Oct 8 15:00Z backend release; all four copies now read "The server windows that are still on the DEV stack go live with this release"; `transparency` is `opaque` since revision 4, like the base events. Revision 5: the title uses a plain hyphen ("ZM3D backend release - live-ops server windows"), created 2025-09-24T16:05:37Z, updated 2025-09-26T17:20:09Z (Douglas's working hours) |
| `f_7c3e91a4d2b85f60e1a9c4` | gdocs | AUTH H1 (rulebook) | Frederick's beta brief (body 3,170 chars since revision 14, which re-words the lock rule and adds the Endless sentence, §11 Revision 14; 3,100 chars in revision 13, which re-words the shop and Push copy clauses, §11 Revision 13; 3,090 chars in revision 12, which states the close for every window and adds the shop and naming clauses, §11 Revision 12; 2,992 chars in revision 11, which adds the clip, closing and held-row sentences, §11 Revision 11; 2,802 chars in revision 10, which re-words the still-to-do rule, §11 Revision 10; 2,849 chars in revision 9, which closes its rules, §11 Revision 9; 2,807 chars in revision 8, which adds to "Held or not": "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date."; 2,704 chars in revisions 4 to 7; revision 5 moves its Drive and Doc stamps to 2025-09-24 17:15:22 / 17:40:52 UTC with size and content_path NULL (revision 5 added them and revision 6 took them back: a path with no bytes behind it could fail a download); Check-A readable; revision 4 adds Plague Race to the beats planned without window dates, rewords the one-off rule and says the config owner is told "in a reply on the mail where they committed to it", see §11 Revision 4; revision 2 adds the late-start sentence and rewords the rollover line, which reads "the quest rollover, the daily gift (Login Calendar on the push sheet, same beat)" since revision 11) |
| `f_2b9d4e7a1c63f08d5e7b21` | gslides | span source (K8/R9) | UA plan deck, four buy weeks; revision 5 rewords its retention-campaign line ("The Unity retention campaigns are a separate budget and are not part of these buys.") and stamps it 2025-09-23T16:05:43Z |
| `f_e4a17c90b3d25f6a8c1d73` | gsheets | DEST (A2) | Julia's Calendar/Pushes sheet skeleton; since revision 8 its Drive row carries a `web_view_link` in the base form |
| `d_5f2c8e1b7a94d03c6e2b58` | gdrive | container | "ZM Live Ops" folder |
| `harmonygames-Games/match3d#470#rc_10` | github | DEC (R_DONE_DEPLOY, T1) | Arthur, 2025-09-30T15:51:06Z, an inline note on `Assets/Scripts/UI/CollectAndWin/CollectAndWinMainScreenController.cs` inside his BASE approval review `#470#rev_9` (same instant; the PR merged at 15:51:15Z): "Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next backend release. The Plague Race, leagues, Endless and Season Pass schedules are already running on prod. The client side in this PR is fine as it is." Revision 5: the seeded post-merge review `#470#rev_10`, its event `#470#ev_9` and the PR `updated_at` bump are gone |
| `harmonygames-Games/match3d#468#rev_3` + `#rc_38` + `#ev_6` | github | DEC (R_REVIEW_FLAGS, T11) | Arthur, 2025-09-29T15:36:41Z, a COMMENTED review with one inline note on `Assets/Match3D/Game/Levels/GameLoader.cs`, the file that spawns the vials: "The Collect & Win vials that spawn in the levels still need their final models before the event runs. Not a blocker for this PR, Claire has those on her list." Base #468 "Collect And Win" was opened 2025-09-26T20:16:25Z and merged 2025-09-29T16:13:50Z, so the note falls inside its open window. Re-worded in revision 5: Claire owns the 3D vial models; the UI sprites, which this PR already ships in five colours, are Martin's (through revision 4 the note said "final vial sprites" on a sprite file). Revision 13 drops "first-pass" and says they are needed before the event runs and that this is no blocker for the PR |
| `harmonygames-Games/match3d#472#rc_1` | github | DEC (R_REVIEW_FLAGS, T11) | Arthur, 2025-09-30T15:52:58Z, an inline note on `Assets/RewardVFXManager.cs` inside his BASE approval review `#472#rev_1` (same instant; the PR merged at 15:53:04Z): "Fine for this PR. Separately, the Season Pass premium strip art still shows the October range. It needs the November range before that season opens, Oliver is taking the date change." Revision 8, re-worded in revision 11; it replaces `#473#c_2`/`#ev_5`, a conversation note 35 minutes after #473 merged |
| `cmt_zom465_2` | linear | DEC (R_ICON_SCOPE, T14) | Marcus Bennett (`usr_c77c50cc15c5342d`, the ticket's assignee), 2025-09-30T18:05:02Z, sequence 2: "Collect & Win came in after my note above, so its event icon is not animated yet. The Collect & Win event icon animation is still to do on my side, the other event icons are finished." Revision 4; it replaces `#454#c_4`/`#ev_6`, dated 11 days after #454 merged |
| `cmt_zom465_3` | linear | DEC (R_ICON_SCOPE, T14; revision 11) | Brian Foster (`usr_fc22d5941b2aeb5c`), who created the master VFX list `ZOM-521`, 2025-09-30T18:13:41Z, sequence 3: "Marcus, the Collect & Win icon does have to land before the event runs, it is the one event icon with no animation. Keep it on this ticket, the master VFX list was ticked before that event merged." The ZOM-465 `updated_at` follows it. It is the record that makes the icon "still needed", and the one evidence id revision 11 adds (§11 Revision 11) |
| `cmt_zom432_2` | linear | DEC (R_DONE_ELSEWHERE, T10) | Samuel Turner (`usr_caafeec2804b3a67`), 2025-09-30T21:07:26Z, sequence 2, on the ticket he closes at the same instant: "The frame went out with PR #471. It is in both submission builds from today, iOS 50 and Android 135, so nothing is left here. Closing." Revision 5; it replaces `#471#c_18`/`#ev_8` (a note five hours after that PR's merge has no base precedent), and nothing is seeded on #471 any more |
| `cmt_zom429_1` | linear | VR (T7, superseded) | Douglas, 2025-09-16T18:12:04Z: a force-close and reopen lands players in the new week. Revision 5 dates it before the Sep 19 regression that Vincent reported on Sep 22 (it was Sep 23) and leaves the ZOM-429 `updated_at` at its base value |
| `cmt_zom543_1` | linear | DIST (R_INFRA_SCOPE, D10) | Calvin: queue manager flow list (comment and ZOM-543 `updated_at` dated 2025-09-30T16:20:37Z, after PR #472 merged) |
| `cmt_zom465_1` | linear | DIST (R_ICON_SCOPE natural) | Marcus: idle icons "done" (struck); since revision 4 corrected on the same ticket by `cmt_zom465_2` |
| `cmt_zom432_1` | linear | VR (T10, superseded; R_DONE_ELSEWHERE natural) | Calvin, 2025-09-24T16:10:28Z: gift frame "still needed"; the older word on a ticket that `cmt_zom432_2` closes Done at 2025-09-30T21:07:26Z |
| `cmt_zom556_1`, `cmt_zom565_1`, `cmt_zom552_1`, `cmt_zom534_1`, `cmt_zom526_1`, `cmt_zom78_1` | linear | DEC/DEST | owner notes (see §5) |
| `cmt_zom344_1/442_1/471_1/504_1/517_1/521_1/542_1/544_1/546_1/549_1/566_2` | linear | CERT | routine progress notes, no calendar action. Revision 5 re-words or re-times most of them to what base code, commits and messages support (§11 Revision 5) and drops `cmt_zom387_1`; revision 6 shortens `cmt_zom544_1` (§11 Revision 6); revision 9 moves Owen's analytics note from `cmt_zom566_1` to `cmt_zom566_2`. `cmt_zom521_1` also stands in `R_HOLD_SCOPE`'s evidence for Endless |
| `cmt_zom526_2` | linear | CERT (revision 3, the SC-15 repair; decides no value) | Brian Foster on his own ticket ZOM-526, 2025-09-26T15:40:50Z: "Unticked this one on the master ticket, it was marked done too early. What is left is the Collect and Win trigger I mentioned above and, once that event is back, Axe Arena. It is polish on an effect that already ships for Season Pass, and the events run without it, so it does not have to land before the beta." (re-worded in revisions 5 and 6) |
| `cmt_zom526_3` | linear | CERT (revision 6; decides no value) | Calvin Price (`usr_49b9dfa5208d400d`), 2025-09-30T16:24:19Z, sequence 3: "Collect and Win tokens go through the queue manager now (#472). Only the Axe Arena travel is left here, and that waits on the event coming back." The ZOM-526 `updated_at` follows it. Base #472 merged 2025-09-30T15:53:04Z |
| `cmt_zom521_2` | linear | CERT (revision 7; decides no value) | Calvin Price (`usr_49b9dfa5208d400d`), 2025-09-30T16:27:38Z, sequence 2: "Card pack animation went in with #475. I am leaving this item, ZOM-528 and ZOM-541 open until Brian has seen it in a build." The ZOM-521 `updated_at` follows it. Base #475 ("Adding card pack animation") merged 2025-09-30T16:09:15Z |
| `cmt_zom534_2` | linear | CERT (revision 9; decides no value) | Leonard Hayes (`usr_63fffeb4fab5233e`), who reported the fault, 2025-09-30T01:09:52Z, sequence 2: "Stayed online through the 00:00 UTC reset on the store build tonight. Quest points reset on their own, no restart. That was my report, it is good on prod now." The ZOM-534 `updated_at` follows it. Base: client commit `47c65623e7` (Sep 10) and #builds iOS Submission #36 and Android Submission #119 (Sep 11) |
| `cmt_zom566_1` | linear | CERT (revision 9; decides no value) | Brian Foster (`usr_fc22d5941b2aeb5c`), who opened ZOM-566, 2025-09-30T17:53:19Z, sequence 1: "Owen, analytics and the name changes are first on the list, but none of it is a blocker. The event runs fine with the current text, so the header title and the info screen text do not have to land before the beta." Base: Vincent's and Brian's Sep 30 lines in #zm-collect-win, and the post-clock history of #477 (§11 Revision 9) |
| `cmt_zom563_1` | linear | CERT (Douglas's since revision 12; decides no value) | Douglas (`usr_cd7849ec043ab3da`, the ticket's assignee), 2025-09-30T18:17:05Z, sequence 1: "Prod has the teams and social changes now. That update carried only these, the Collect & Win server windows wait for the Oct 8 release." Base: his DM of 18:16:33Z, "Ok, I updated the prod environment with the latest teams/social changes". ZOM-563 is not a cohort member |
| `cmt_zom563_2` | linear | CERT (revision 9, `cmt_zom563_1` until revision 12; decides no value) | Vincent Parker (`usr_65c76e0b87aa7e9b`), 2025-09-30T22:04:33Z, sequence 2: "Checked on prod: teams' lives, golden frames and names all work as expected. Closing." Base: his DM with Douglas of 21:58:44Z, "Yep it works as expected" |
| `e343557b2e94a1701251ebd079e6f0ce` (`C08R27X0EAH/1759187861.318279`) | slack | CERT (revision 9, moved in revision 10; decides no value) | Leonard Hayes, 2025-09-29T23:17:41Z, a reply under his Sep 21 #zombie-bugs post `ede90bc6…`: "Ran this again on an S23 Ultra in the cloud device farm, live Android build, a few endless runs with the airstrike. Could not get it to freeze, so I am leaving this one." Base: `page_qa_runbook` names the cloud device farm (§11 Revision 10) |
| `a08ff7cbfc52008d7dee8457e9385a3c` (`C08R27X0EAH/1759268775.482369`) | slack | CERT (revision 10, D7; decides no value) | Vincent Parker, who raised it, 2025-09-30T21:46:15Z, a reply in the base shader thread `d0dd5d3a…`: "Oliver pushed the lightSweep fix. It only changes how the box looks, the box opens the same with or without it, so it rides the next store build and nothing has to land for the beta." Base: commit `25c6c66b6b` changes `lightSweep Box Variant.mat`. It replaces Oliver's reply of revision 9 |
| `532747cb5d123a95d13204e57b5a7a38` (`C08R8CHB0QL/1759250468.275139`) | slack | CERT (revision 10; decides no value) | Robert, 2025-09-30T16:41:08Z, a reply in Martin's desert thread `a3e78e82…`: "Both look good, the desert and the port. Keep them as options, Endless runs with what it has now and nothing waits on new themes." |
| `cmt_zom565_2` | linear | CERT (revision 10; decides no value) | Brian Foster (`usr_fc22d5941b2aeb5c`), 2025-09-30T16:12:27Z, sequence 2: "Marcus, the endless VFX inside the core game and the refill timer are the same P1/P2 polish from my list. Endless runs fine without them, so they can follow and do not have to land before the beta." The ZOM-565 `updated_at` follows it |
| `7d70c7753179c98b6c8b2b5457a1e5e7` (`C09EVVCFHKR/1758903764.713429`) | slack | CERT (revision 11; decides no value) | Douglas, 2025-09-26T16:22:44Z, a reply in Brian's reward-table thread `0069f614…` in #zm-collect-win: "Both tables are updated." Base: Brian's request of 15:10:00Z, "Could you update them?", had no reply. Julia is not a channel member, so `check-sql` reads it UNVERIFIED; no cell rests on it |
| `ZOM-344`, `ZOM-432`, `ZOM-563`, `ZOM-566` | linear | state follows the ticket's own note (decides no value) | UPDATEs. Done, with `completed_at` = `updated_at` = the note's time: `ZOM-344` at 2025-09-16T16:20:28Z (base Todo; "Art side is signed off on my end.") `ZOM-432` at 2025-09-30T21:07:26Z (base Todo; Samuel's closing note) and `ZOM-563` at 2025-09-30T22:04:33Z (base In Progress; Vincent's closing note). In Progress: `ZOM-566` with `started_at` 2025-09-30T17:20:13Z (base Todo; "Wiring both into the analytics manager now"). Revision 5 takes back three closures and one start that revision 4 made: `ZOM-565`, `ZOM-471` and `ZOM-542` keep their base states (Todo, Todo, Regression), their re-worded notes saying the work is not done and not needed for the beta (revision 11 moves `ZOM-542` to Todo, an UPDATE with its `updated_at`: base `started_at` is NULL, so Regression sat against a ticket never started), and `ZOM-387` is exactly as base has it (Todo, no seeded note, no UPDATE; out of the cohort since revision 6). Every commented issue's `updated_at` follows its newest seeded comment, except `ZOM-429`, whose base `updated_at` (Sep 22) is already later than its note |
| `68dac8204f1e9a3b7c2d5e61` | trello | DIST (T12, ungraded; decides no graded value since revision 5, and since revision 10 supports the ungraded Weeks running cell for Quests) | Leonard Hayes (`PERSON_6094_TRELLO_USER_ID`), 2025-09-29T17:55:44Z, on the open card #61 `68c452a03006277f55d9dc96` "Add more quests and balance quest rewards - (Leonard/Douglas)" (base list record "BETA: Oct 10"; since revision 13 the payload has `idCard`, `list` and `textData`, the key set of 14 base commentCards, and its list name "BETA: Sep 30" is the one 63 base actions carry, the base SC-13 mismatch): "More quests and the reward balance go in with the Mon Oct 13 rollover if they are ready. The weekly rollover does not wait on them, the current quests keep running either way." (words of revision 10; §11 Revision 6 to Revision 10). The card's comment badge goes 0 to 1 and its `dateLastActivity` follows. Through revision 4 the note was Brian's, on card `6851a724601a61857a1b202f`, which base completed on Jun 30 (0 of 45 completed cards carry a later comment), and it decided a Quests still-to-do |
| `73bc730c…`, `78aa8ed7…`, `65564543…` (C093LEZGF6J) | slack | COMP (INT-01) | faithful PR-comment mirrors of `#470#rc_10`, `#468#rc_38` and `#472#rc_1`, non-LB by ACL. Three (no #471 mirror since revision 5; the #473 mirror left in revision 8), in the base shape: subtype NULL, people's GitHub handles in the pretext, each posted 2-3 s after its event, '&' escaped in the text, ts ending in 9 |

Base parents whose counters the injection UPDATEs: `9025d428…` (#zombie-art, +1 reply; revision 5 also sets its
`thread_ts_legacy`, as base parents with replies carry their own thread ts), plus the three `#zombie-prs` mirror parents:
`c2b9c903…` under #470 (16 to 17, `latest_reply` left at the base merge post because the note is older than it),
`4b7c4127…` under #468 (41 to 42, `latest_reply` left at the base merge post; its card's Reviewers field now names Arthur)
and `61f686b8…` under #472 (3 to 4, `latest_reply` left at the base merge post because the note is older than it). No
PR row is updated since revision 8: #470, #471, #472 and #473 are not touched, and #370, #438 and #454 carry no seeded row
since revision 4. The seeded ask root `bca784379e7dbca9e64e79a64dfefbba` is itself an INSERT and carries `reply_count` 1,
`reply_users_count` 1 and `latest_reply` `1759263878.305129` for the thread reply. Brian's two mails (all six mailbox
copies, bodies and the Sep 22 snippet) say "The November season". One base text field is rewritten: the `ZOM-521`
`description` is seeded with two of its six checklist items unticked (Tokens traveling to live-ops; Claimed Cards
traveling to inventory Section; revision 3), its `updated_at` 2025-09-30T16:27:38Z, the time of `cmt_zom521_2`. The
Trello card #61 `68c452a03006277f55d9dc96` gets its comment badge and `dateLastActivity`; the card revision 4 touched
(`6851a724…`) is left as base has it. Revision 9 adds two #zombie-bugs parents: `ede90bc6…` (0 to 1 reply, with its own
`thread_ts_legacy`) and `d0dd5d3a…` (4 to 5 replies, `latest_reply` the seeded reply). Revision 10 adds `a3e78e82…` in #zombie-art (3 to 4 replies, 3 to 4
reply users, `latest_reply` the seeded reply). Revision 11 adds `0069f614…` in #zm-collect-win (2 to 3 replies, 1 to 2 reply users, `latest_reply` the seeded reply).

## 3 Findability and discovery order

The difficulty is **reconciliation across retrievable records, not concealment** — every deciding record is reachable;
the hard part is ordering and composing them (both independent reviewers endorsed this direction). Discovery order per
trap (manifest `traps[].discovery_order`):
- **Ask follow-up (push-plan rows, Zombie Lane)**: the ask root `D05SD5QLG94/1759263617.418209` is met first (DM history
  returns parents only); what the push plan covers and that Zombie Lane stays off live in the thread reply under it,
  `D05SD5QLG94/1759263878.305129`. The root shows `reply_count` 1, so the reply is one thread-open call away; a run that
  reads only the root plans the push tab on its own reading of what a beta push is and lists Zombie Lane as a beat. Honest
  liveness note: this is family A14 ("replies never opened"); the completed `julia_zm_difficulty_baseline` task saw 3 of
  6 Opus 5.5 runs miss DM thread replies, but the local `hardness_v2_check` classes a reply in the anchor's own thread
  as `first_read`, so how often this one lands is uncertain (§11).
- **T1 (C&W first window)**: the merged client PRs + Julia's "feature completed" note are met first; the composition is
  hard — Arthur's `#470#rc_10` (windows DEV-only) + the Oct 8 GCal release (Istanbul→UTC) + the brief's window cadence
  land **Fri Oct 10 00:00 UTC**, a late start and not a hold (brief:
  "A beat whose server windows are waiting on that release starts late, it is not held.").
- **T2 (Halloween one-off)**: the approval is a reply in a #zombie-art thread; the withdrawal is a top-level message in
  Robert's DM with Julia twelve days later. Since revision 9 it says "the themed prop set I okayed in Martin's thread", so
  a "Halloween" or "one-off" search returns the approval and not the withdrawal. A run reaches it through Robert's DM
  history, a search on his messages or a "beta calendar" search, and ties the two together by "themed prop set".
- **T7 (weekly leagues)**: the Linear note + the Sep 22 #zombie-bugs recovery are met first; Vincent's Sep 30
  #zombie-match3d prod re-test (another channel, later date) must be ordered against them under the hold rule.
- **T8/T9 (Season Pass config)**: Brian's Sep 22 handoff mail is met first; the correction is a separate mail four days
  later (its own subject and thread since revision 4), which a read of the handoff thread does not return and a
  "last few days" sweep does not reach; the lock is a UTC computation.
- **Cohort (R_REVIEW_FLAGS / R_ICON_SCOPE)**: the inline notes come only from the per-PR
  `github_get_pull_request_comments` call — a PR search never returns them. The vial note is inline on #468 and, since
  revision 8, the premium-strip note is inline on #472, under an empty-bodied APPROVED review.
- **T10 (daily-gift frame), a trap in name only since revision 5**: ZOM-432 is Done and its own last note (Samuel,
  `cmt_zom432_2`) says the frame went out with PR #471 and is in both submission builds, so one read of the ticket
  settles it and a run that lists open issues never meets it. **T14 (icon animation), weaker since revision 4**: both of
  Marcus's notes sit on ZOM-465 and one per-issue comment call returns them in order.
- **T12 (the quest note), ungraded since revision 5**: Leonard's note on the open quests card says the rollover does
  not wait on the new quests, so nothing is put down for Quests; no slot reads that cell.

## 4 Self-validation

The SQL-only tools were re-run on the revision-14 SQL (`edae63f3…`) on 2026-11-06 on this machine: `sql_lint`, the eval
injection lint, `base_check` (with and without `--manifest`), `base_claims` and `check-sql`; their lines below are the
revision-14 results. The lines bound to the solver and the manifest (hardness gate, solver contract, fact check,
preflight, golden re-verification) are still the revision-1 results from the authoring machine: this machine's
`hardness_gate` does not yet know `volume_exception.rows_floor`, so those lines and the pasted gate block are re-run and
re-pasted once the tools from the authoring machine are synced. The stage gate re-runs and compares each. What those
solver- and manifest-bound tools return on revision 14 on this machine is listed in §11 (Revision 14).

- `sql_lint.py 01_Universe_Inject.sql` → `errors: 0  warnings: 8`, total rows: 111 (81 INSERT, 30 UPDATE).
- sql_lint warning disposition — **clock ×8**: every warning is the gcal Oct 8 15:00–16:00 UTC backend-release, a future / not-yet-happened plan event the deploy rule reads; dispositioned as intended (the clock rule permits a future plan event), not a defect.
- `hg.py lint --sql 01_Universe_Inject.sql` (eval injection lint) → **FAIL 0, CHECK 0, INFO 0**.
- `BASE CHECK (/injection A + C, static): PASS` — 81 inserts, 30 updates; Check A PASS, Check C PASS, with and without
  `--manifest`: the SQL no longer touches `ZOM-387`, so no L03 line is raised either way. With the manifest the GCal
  `no_notify` integration exception is declared; without it the same event is one INT-11 warning, not a failure.
- `BASE CLAIMS (injected text vs base git + #builds): PASS` — 0 branch mentions, 0 fail, 0 warn.
- `HARDNESS GATE (extreme): PASS` — revision-1 run on the authoring machine: cohort 47 (≥40), call budget 208 (floor
  130), per-record 145 (floor 75), rows 76 (floor 70, requester-confirmed `volume_exception.rows_floor`), 14
  mechanisms, incorporation / authority / surface / supersession-chronology / hazard-scope all PASS. On the revision-2
  manifest and SQL as they stood on 2026-11-06, this machine's older `hardness_gate` reads cohort 44 (21 issues + 23
  PRs, the Zombie Lane-only items gone), call budget 200 unconditional of 210 planned, per-record 138, rows 77, 15
  mechanisms, 26 traps and 17 fragments, but it does not return a PASS here: it rejects `volume_exception.rows_floor`
  as an unknown key and so applies the un-excepted extreme floors. The PASS has to be re-established on the synced
  tools before the gate block is re-pasted. On revision 3 the same run reads rows 78 and one more seeded id under
  persona reach (44, the new Linear comment); every other figure is unchanged and the failing lines are the same
  four, all from that key (`effective_profile`, `rows`, `per_record_calls`, `call_budget`). On revision 4 it reads
  cohort 39 (16 issues + 23 PRs), call budget 192 unconditional of 202 planned, per-record 133, rows 75, 39 seeded ids
  under persona reach, and fails a fifth line of its own: `cohort_size` (39, need 40; §11 Revision 4). On revision 5 it
  reads cohort 42 (19 issues + 23 PRs), call budget 194 unconditional of 204 planned, per-record 136, rows 70, 14
  mechanisms, 26 traps (12 of them distractors), 16 fragments, 5 chains and 40 seeded ids under persona reach;
  `cohort_size` passes again and the fifth failing line is `hazard_scope` (L03 through `ZOM-387`; §11 Revision 5). On
  revision 7 it reads cohort 41 (18 issues + 23 PRs), call budget 193 unconditional of 203 planned, per-record 135, rows
  72 and 42 seeded ids under persona reach; `hazard_scope` passes (`ZOM-387` left the cohort in revision 6) and the
  failing lines are the same four, all from that key (§11 Revision 7). On revision 8 it reads cohort 41, call budget 154
  unconditional of 164 planned, per-record 96 (three surfaces), rows 71 and 42 seeded ids under persona reach; the failing
  lines are the same four (§11 Revision 8). On revision 9 it reads the same cohort, budget and per-record figures, rows
  76 and 44 seeded ids under persona reach; the failing lines are the same four (§11 Revision 9). On revision 10 it reads rows 78 and 45 seeded ids under persona
  reach, the same cohort, budget and per-record figures, and the same four failing lines (§11 Revision 10). On revision 11 it reads rows 80 and 46 seeded ids under
  persona reach, the same cohort, budget and per-record figures, and the same four failing lines (§11 Revision 11). On revision 12 it reads rows 81 and 46 seeded ids
  under persona reach, the same cohort, budget and per-record figures, and the same four failing lines (§11 Revision 12). On revision 13 it reads the
  same rows, seeded ids, cohort, budget and per-record figures, and the same four failing lines (§11 Revision 13), and so
  does revision 14 (§11 Revision 14).
- `SOLVER CONTRACT: PASS` — 8/8 (`oracle_kit.py check`): interface, deterministic, rules_nodes (14↔14), slots, controls
  (every over-application moves a control member), golden (0 wrong), digest.
- `FACT CHECK: PASS` — 9 declared facts, 9 superseded records, 0 leaks (`fact_check.py --no-leak`).
- `PREFLIGHT: PASS` — `01c_Preflight_Report.json`, blocking {solver_contract, surface_validation, mutation_dispositions,
  geometry_upper_bound} all true; geometry U = 0.9189 (102/111, needs > 1−0.85 = 0.15; L_max UNSUPPORTED — 14 mechanisms
  exceed the 8-node enumeration, advisory); mutation 50/50 dispositioned (interventions remove only each rule's
  fact-specific records, not the shared brief, so each moves its own key; R_COPY_CURRENT / R_WIRED rest on the base
  push sheet → no-injected-records, load-bearing by the clean disable); liveness 8/8.
- Golden values independently re-verified against the revision-1 SQL and persisted in `research/GOLDEN_verify.md` (all
  8 checks CONFIRM: the Fri Oct 10 window, Weekly Leagues held on the prod re-test, Plague Race four weeks, the Oct 31
  00:00 UTC lock grounded in base `page_season_pass_spec`, the C&W icon gap, Daily Login empty, the push rows that
  were required then, incl. Weekly Leaderboard reset = Ready+WIP→Held, and Endless / Zombie Lane = Runs). Revision 2
  leaves checks 1–7 and the Endless half of check 8 as they are; the Zombie Lane half of check 8 no longer applies
  (Zombie Lane is off the calendar), and what revision 2 adds (four more held push rows, the frame in both builds) is
  listed in §7 and is re-verified with the solver revision. Revision 5 changes what two of those checks rest on (the
  Daily Login check: the closing note is on ZOM-432 itself; the Collect & Win still-to-do: vial models, not sprites) and
  empties the Quests still-to-do; `research/GOLDEN_verify.md` carries a revision-5 note.
- `persona_view.py check-sql julia_lawson 01_Universe_Inject.sql --load-bearing` (the two lines below are the
  revision-1 paste; the revision-2 report-only re-run gives 30 YES, the same 8 other-mailbox copies and 10 mirror rows, and the new reply
  `D05SD5QLG94/1759263878.305129` is YES as an im member; the revision-3 re-run is the same, with 64 unscoped rows
  instead of 63 for the new Linear comment; the revision-4 re-run gives 29 YES (the retraction's old thread parent is no
  longer an UPDATE row), the same 8 other-mailbox copies, 8 mirror rows (four mirrors and their parents) and 61 unscoped rows;
  the revision-5 re-run with the new ids in `research/lb_ids.txt` gives 29 YES, the same 8 other-mailbox copies, 6 mirror rows
  (three mirrors and their parents) and 53 unscoped rows; the revision-7 re-run gives the same with 55 unscoped rows and the revision-8 re-run with 53; the revision-9 re-run gives
  33 YES (the two new replies and their parents), the same 8 and 6, and 57 unscoped rows; the revision-10 re-run gives 35 YES, the same 8 and 6, and 58 unscoped rows, verdict PASS):

CHECK-SQL as julia_lawson <julia.lawson@harmonygames.co>
verdict: PASS (0 load-bearing rows not visible; 29 YES, 8 NO non-load-bearing other-mailbox / other-calendar copies, 10 UNVERIFIED #zombie-prs mirrors non-load-bearing by ACL)

## 5 Intended disagreements

Each is a deliberate two-reading the correct run must resolve from the records (not an authoring defect):
- **Collect & Win**: merged client PRs + "feature completed" (ready now) **vs** Arthur `#470#rc_10` + the Oct 8 release
  (prod only Fri Oct 10 00:00 UTC). Resolves to the later computed window, as a late start: the brief says a beat whose
  server windows are waiting on that release starts late and is not held, so Collect & Win is Runs with no ticket note.
- **Weekly Leagues**: ZOM-429 "a restart gets players in" + Sep 22 "working fine" **vs** Vincent's Sep 30 re-test
  (`b5f2955c…`, fails on the current prod build even after a restart). An established prod failure after a restart is a
  hold by the brief rule ("An established failure holds it; an unverified one does not."); resolves to Held.
- **Plague Race week 4**: Robert's #zombie-art approval (`933cee9f…`) **vs** his later DM withdrawal (`669d15f6…`, a
  top-level DM message since revision 4 that names no Halloween since revision 9).
  Resolves to all four weeks, one-off dropped.
- **Season Pass config**: Brian's Wed Oct 29 handoff **vs** his Fri Oct 31 10:00 Istanbul slip (`…/1844311412966040123`)
  against the 24h lock. The lock offset is the base authority `page_season_pass_spec` ("locked 24h before each season
  opens"); the brief only points to it ("every config lands before its lock"). The November season opens Sat Nov 1
  00:00 UTC, so lock = Fri Oct 31 00:00 UTC; the slip (10:00 Istanbul = 07:00Z) is 7h late. Resolves to "before Oct 31
  00:00 UTC", and Julia tells Brian (the brief: "you tell its owner in a reply on the mail where they committed to it").
- **Daily gift frame** (a disagreement in name only since revision 5): Calvin's Sep 24 note that the frame is still
  needed (`cmt_zom432_1`) **vs** Samuel's closing note on the same ticket (`cmt_zom432_2`, Sep 30 21:07:26Z: the frame went
  out with PR #471 and is in both submission builds from that day, iOS 50 and Android 135) and the ticket's Done state.
  Base #builds `C05433XK267/1759259749.259909` and `C05433XK267/1759263189.219529` show both builds succeeding on main
  after PR #471 merged and agree with it. Resolves to "nothing left" on one read of ZOM-432.
- **Push-plan rows and Zombie Lane**: a run's own reading of what a beta push is on the mixed PNs Beta tab (all 14 rows, only
  the Push Notification rows, or only the Ready ones) and of Zombie Lane as a player-facing beat **vs** Frederick's
  thread reply under his ask (`D05SD5QLG94/1759263878.305129`). Resolves to ten push rows (the tab as it stands, local
  notifications included, minus Hourly Coins, Nathan's Treasure Hunt, Streak Fever and Axe Arena), no-game copy may go
  out, and Zombie Lane is not on the calendar.

## 6 Constraints for the prompt brief

- The reply with tradeoffs goes to **Frederick's DM** (`slack:D05SD5QLG94/…`), not a channel; the calendar lives in
  **Julia's sheet** (`f_e4a17c90…`); the link goes on the existing **ZOM-78** ticket (not a new one); the leagues hold
  is noted on **ZOM-429**, the only ticket note because Weekly Leagues is the only held beat.
- The prompt must **not** name any held/late/run outcome, the Oct 10 window, the Oct 31 lock, or any deciding record —
  those are discovered. It points to Frederick's message for what he wants and to the brief for the working rules; it
  lists neither the beats nor the per-row fields, and it must not mention that the message has a reply.
- The still-to-do rule is closed (revision 9, re-worded in revision 10): a beat's fix if it is held, and anything flagged
  since the brief as still needed for it (prod deploy, config or player-facing art). Nothing else goes in, and every
  still-to-do value in `solver/truth.json` fits it (§11 Revision 9 and Revision 10).
- Scope: seven beats (Plague Race, Collect & Win, Season Pass, Endless Monster Mode, Weekly Leagues, Quests, Daily
  Login = the daily gift); Zombie Lane (Frederick's follow-up), the Halloween one-off, Boss Arena and Axe Arena are off
  this calendar. Push plan: ten PNs Beta rows; Hourly Coins, Nathan's Treasure Hunt, Streak Fever and Axe Arena are not
  listed.

## 7 Facts for the human

(Values a reviewer needs; each from its record. Scoped records here are Julia-visible per §1.E; GitHub/Linear are
unscoped.)
- Collect & Win = **Runs, late start**, first prod window **Fri Oct 10 00:00 UTC** (`#470#rc_10` + `evt_9a4c2e7f1b3d58e06c7a2f`, brief cadence);
  not held (brief `f_7c3e91a4d2b85f60e1a9c4`: "A beat whose server windows are waiting on that release starts late, it is not held.").
- Weekly Leagues = **Held** (`b5f2955c2e154efc6835946ecfe1758e`, an established failure on the current prod build even
  after a restart, supersedes `cmt_zom429_1`). It is the only held beat, so the only ticket note is on `ZOM-429`. Its still-to-do is the weekly reset fix, owner Douglas, the ticket's assignee. Since revision 12 its row reads Mon Oct 6 00:00 UTC and All four weeks, marked held.
- Plague Race = **Runs all four weeks**; Halloween one-off dropped (`669d15f685f158633e56302160957f1e`). Since revision 4
  the brief (`f_7c3e91a4d2b85f60e1a9c4`) asks whether this beat is in, which weeks it runs and whether its push goes out, not for its window dates.
- Season Pass = **Runs**, first window **Mon Oct 6 00:00 UTC** since revision 12 (the clip rule); the October season is already running on prod (`#470#rc_10`) and the November season opens Sat Nov 1 00:00 UTC.
  Still-to-do = premium strip → Nov (`#472#rc_1`, Oliver) + Nov config before **Oct 31 00:00 UTC** (the 24h-lock
  authority is the base `page_season_pass_spec`; the brief only points to "before its lock"; slip mail
  `julia.lawson@harmonygames.co/1844311412966040123` is 7h late, so the date moves to any time before the lock and Julia tells Brian in a reply on that mail, where he committed to the date).
- Collect & Win still-to-do = the final vial models (`#468#rc_38`, Claire) + event icon animation (`cmt_zom465_2`, Marcus, and `cmt_zom465_3`, Brian: it has to land; also absent from the `#456`
  enumeration) + prod deploy with the Oct 8 release (Douglas, who organizes it).
- Quests = **Runs, all four weeks**; still-to-do **nothing** since revision 5: Leonard's note on the open quests card says more quests and the reward balance go in with the Mon Oct 13 rollover if they are ready and the weekly rollover does not wait on them (`68dac8204f1e9a3b7c2d5e61`), so nothing has to land before the beat runs. Not graded: no slot reads this cell.
- Daily Login (the daily gift) = **Runs, all four weeks**, still-to-do **nothing left**: `ZOM-432` is Done and Samuel's closing note on it says the frame went out with PR #471 and is in both Sep 30 submission builds, iOS 50 and Android 135 (`cmt_zom432_2`).
- Endless Monster Mode = **Runs** (`cmt_zom504_1`, `cmt_zom565_1`, `cmt_zom521_1`: its open items are a bot-only visual glitch, start-screen polish its owner says is not needed for the beta and VFX checklist items, none a hold by the brief's hold rule; `ZOM-565` keeps its base Todo state since revision 5).
- Zombie Lane is **not a beat** on this calendar (`D05SD5QLG94/1759263878.305129`: a permanent track with no window or
  reset to plan); the Halloween one-off, Boss Arena and Axe Arena stay off as before. Seven beats in all.
- Pushes (base `f_a325dd4af80afc5994d5dc` tab "PNs Beta"; ten rows, set by `D05SD5QLG94/1759263878.305129`: every row except Hourly Coins,
  Nathan's Treasure Hunt, Streak Fever and Axe Arena, which must not be listed). **Send**: Lives recharged + 7-day
  lapse (Ready + LIVE; copy names no game, which the follow-up allows). **Held**: 1-day lapse + D0-1 FTUE (copy names
  "Puzzles vs Zombies"); Plague Race start + Weekly Leaderboard reset (Ready, but Status (NA, WIP, LIVE) = WIP, not
  LIVE; this is a sheet-status call, not a claim about client wiring, since base `NotificationManager.cs` already
  schedules them locally); Quests rollover push (Not Ready); Win & Collect event start (Not Ready, WIP, Domino name in
  the copy); Login Calendar update (Not Ready, WIP); Season Pass activation (Not Ready, WIP).

## 8 Fact sheet

Manifest `facts` (verified by `fact_check.py --no-leak`, 0 leaks; eight facts since revision 5, when `quests.todo` left with the Quests still-to-do). Each value lives only in its `home_ids`
(the per-record carrier + its #zombie-prs mirror where seeded); dates are mention-gated; superseded carriers are in
`version_records`.

| key | value (anchor) | home_ids |
|---|---|---|
| cw.first_window | 2025-10-10 (date) | `#470#rc_10`, mirror `73bc730c…` |
| cw.todo.vials | final models (the note's words since revision 13) | `#468#rc_38`, mirror `78aa8ed7…` |
| sp.todo.strip | premium strip | `#472#rc_1`, mirror `65564543…` |
| cw.todo.icon | outstanding (status) | `cmt_zom465_2` (a Linear note: no mirror) |
| sp.config_lock | 2025-10-31 (date) | `rfc:<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>`, `f_7c3e91a4d2b85f60e1a9c4` |
| login.todo | daily-gift frame | `cmt_zom432_2` (vr `cmt_zom432_1`; a Linear note: no mirror) |
| leagues.status | new week | `C0880U9751A/1759265412.481909` (vr `cmt_zom429_1`) |
| plague.weeks | themed prop set (alias themed prop) | `D05GU6L0XFH/1759270241.638119` (vr `C08R8CHB0QL/1758213623.552919`) |

## 9 Integrations and companions

- **INT-01** github → `#zombie-prs` (`C093LEZGF6J`): the three seeded bot mirrors carry each deciding PR comment body
  verbatim (base INT-01 behaviour; four in revision 4, five through revision 3). Since revision 4 they follow the base row shape: subtype
  NULL and people's GitHub handles in the pretext. Seeded for integration parity; **non-load-bearing** because Julia is not a member
  (§1.E). H3 constraint: the deciding text lives in `review_comments` / `pr_comments`, never in `reviews.body`.
- **INT-11** gcal → invitation mails: **declared `no_notify`** (manifest `integration_exceptions`,
  `3f8e1c6a9b2d4e7f0a5c8b1d3e6f9a2c@hg4`) — an invitation mail would leak the Oct 8 date into a Gmail subject, which
  would collapse the H3 hidden authority. Base INT-11 coverage is partial (836/941 meetings), so the omission is in-range.
- **INT-12** github → Gmail (PR notifications): base is notification-only (no comment body) → no leak.
- **INT-13** gdrive (share notifications): the seeded Drive items (brief `f_7c3e91a4d2b85f60e1a9c4`, deck
  `f_2b9d4e7a1c63f08d5e7b21`, sheet `f_e4a17c90b3d25f6a8c1d73`, folder `d_5f2c8e1b7a94d03c6e2b58`) are shared read targets
  already in Julia's reach (§1.E); no share-notification companion is seeded — none is needed, since Julia owns or reads
  them directly and no new sharing event is introduced.
- **INT-04** linear → Slack: textless "commented on" notice. **INT-21** trello → Slack: none (no companion for Leonard's
  Trello comment). `linear[bot]` PR comment: not seeded.

## 10 Touched-data census and coherence hazards

Touched base records: the three mirror parents (under `#470`, `#468` and `#472`; no PR row since revision 8); five Slack thread parents (`9025d428…`, `ede90bc6…`, `d0dd5d3a…`, since revision 10 `a3e78e82…` and since revision 11 `0069f614…`; Robert's DM parent `c5431028…` is no longer touched); 21
Linear issues (each `updated_at`; five states since revision 11: `ZOM-344`, `ZOM-432` and `ZOM-563` Done, `ZOM-566` In Progress, `ZOM-542` Todo); one Trello card (`68c452a03006277f55d9dc96`: comment badge, last activity); the base push sheet `f_a325dd4af80afc5994d5dc` and Confluence
`page_liveops_calendar` / `page_season_pass_spec` are **read, not modified**. Since revision 3 one base text field is
rewritten as well: the `ZOM-521` description, with two checklist ticks removed (known-issue card SC-15, below). Per QC coherence category
(`coherence_hazards.json`, synth-cut; locators cited):
- **temporal**: none in scope — base_check's hazard audit flags no temporal hazard among the task-touched records; the
  Oct 8 release is a future plan event (§4), dated consistently against the clock.
  Revision 2 removed two seeded-versus-base ordering slips of our own (`cmt_zom565_1`, `cmt_zom543_1`; §11 Revision 2).
- **semantic/category**: none in scope since revision 4 — the display-name disagreement `S04` (`PERSON_2314_GITHUB_USERNAME`
  renders "Ryan" = Frederick Stone) was touched through revision 3 only through Marcus's GitHub comment, which
  revision 4 removed; base_check no longer reports it.
- **cross-service referential**: none in scope — the cohort's Linear-vs-PR-vs-Slack reconciliations (`cmt_zom543_1` vs
  `#459`/`#472`) are the designed task, not a pre-existing base contradiction; base_check reports no referential hazard touched.
  Revision 2 also dropped the season number from Brian's mails, the one label the platform review found at odds with
  base `page_season_pass_spec` (§11 Revision 2). Revision 4 takes Plague Race's window dates out of the answer: its
  cadence differs between the synthetic Snowflake `LIVE_EVENT_PERFORMANCE` rows (5-day runs) and the backend schedule
  and Slack (daily), Snowflake cannot be injected, and the brief asks whether the beat is in, which weeks it runs and
  whether its push goes out (§11 Revision 4 and Revision 9). The conflict is avoided, not repaired.
- **quantitative/reconciliation**: none in scope — the UTC computations (Fri Oct 10 window from `evt_9a4c…`; the Oct 31
  00:00 lock from the base `page_season_pass_spec` 24h rule minus the Nov 1 open, vs the slip `…/1844311412966040123`)
  reconcile records against the clock, not a base quantitative hazard.
- **state/lifecycle** `L03`: `ZOM-387` is Todo in base while a referencing PR (#319) merged (SC-16). It is out of this
  task: the SQL has not touched it since revision 5, and since revision 6 it is out of the cohort on its merits, because the
  KB's guidance is to keep such issues out of a cohort whose predicate is "open". No manifest section names it, so
  `hardness_gate`'s `hazard_scope` finds nothing to resolve and the acknowledgement list is empty. No graded value reads
  the ticket's state.
- **state/lifecycle**, our own seeds (revision 4): through revision 3 four seeded notes reported work finished on
  tickets that were still Todo (`ZOM-565`, `ZOM-344`, `ZOM-471`, and `ZOM-432` through `#471#c_18`; more weakly
  `ZOM-566`, `ZOM-387`, `ZOM-542`), and three seeded notes were dated 11 to 48 days after their PRs merged (`#370`,
  `#438`, `#454`; the base maximum is 0.26 days). The independent `/prompt` run failed both groups. Revision 4 closes
  or starts each ticket at the time of its own note and moves the three notes to records that are live at their
  dates (§11 Revision 4). Revision 5 corrects the over-reach: the audit found the closures of `ZOM-565`, `ZOM-471` and
  `ZOM-542` and the start of `ZOM-387` at odds with base code, commits and messages, so those four keep their base states
  and their notes say only what base supports (§11 Revision 5; `ZOM-542` is Todo since revision 11, §11 Revision 11). No graded value reads a ticket state.
- **state/lifecycle**, known-issue card SC-15 (revision 3) — touched: SC-15 — repaired; not graded. Base `ZOM-521`
  "Master Ticket - VFX implementation" (`linear/data.json /issues/3596`; In Progress) ticks all six checklist items
  while two of its children are still In Progress: `ZOM-526` "Tokens traveling to live-ops" (`/issues/3600`) and
  `ZOM-528` "Claimed Cards traveling to inventory section" (`/issues/3602`). The seeded notes `cmt_zom526_1` and
  `cmt_zom521_1` sit on those tickets, and the platform `/prompt` review of revision 2 failed Cross-Service Coherence
  on it. Revision 3 repairs it in the SQL: the `ZOM-521` description is seeded with those two items unticked, and
  `cmt_zom526_2`, a dated note from the ticket's creator, says why (records and base evidence in §11, Revision 3).
  Revisions 6 and 7 explain why the two items stay open: `cmt_zom526_3` says only the postponed Axe Arena travel is left on
  `ZOM-526`, and `cmt_zom521_2` says the card pack animation went in with #475 and the item, `ZOM-528` and `ZOM-541` stay open until
  Brian has seen it in a build.
  No value the task grades reads the checklist or token travel.
  The card is not an entry of the KB file, so the manifest's acknowledgement list, which takes KB ids only, does
  not carry it (§11, Revision 3); this line, §11 and the design §2 are its record.
- **identifier/format**: none in scope — all seeded ids are clean and unique (§1.F): Slack ids are
  `sha256('<channel>|<ts>')[:32]`, Linear timestamps exact `YYYY-MM-DDTHH:MM:SSZ`, no generated column written; base_check
  reports no identifier hazard touched.
- **other**: known-issue cards SC-16 (status ≠ shipped), SC-38 (SP analytics) and SC-71 (ZOM-471 priority) are
  navigated, never relied on for a graded value; SC-15 (ZOM-521 checklist) is repaired since revision 3 and not
  graded (state/lifecycle, above). Revision 9 closes `ZOM-563`, which SC-16 names as open after its fix was confirmed in a DM
  Julia cannot read, and seeds nothing on #477, so SC-18 (its open or closed state) stays ungraded.

## 11 Platform follow-ups

- **/prompt**: must not leak any outcome or deciding record (§6); the brief carries the rules, and the ask together
  with its thread reply names the scope. The 2026-11-05 `/prompt` run on revision 1 FAILED; see Revision 2 below.
  The second run, on revision 2, FAILED on Cross-Service Coherence alone; see Revision 3 below. An independent run on
  revision 3 failed Cross-Service Coherence on further items and gave Clarity 3; see Revision 4 below. An independent
  round on revision 4, with a claim-by-claim audit of every injected record, found further statements and field shapes
  that base contradicts; see Revision 5 below. Independent rounds on revisions 5 and 6 left one fork and two advisories;
  see Revision 6 and Revision 7 below. A fresh blind round on revision 7 raised further items; see Revision 8 below. The platform's third failure, on revision 8,
  is repaired in Revision 9 below, a pre-review attack on revision 9 in Revision 10, the formal blind round on revision 10 in Revision 11, the verification round on revision 11 in Revision 12, the cold reviewers' last items in Revision 13, and the last cold P1 in Revision 14.
- **/create-difficulty**: the forecast (`hev_10c8bb5be00ab2cf`, UNCALIBRATED, DESIGN-mode, made on revision 1) is
  **borderline** — E[avg] 0.662, P(all four gates) 0.459 (independent) – ~0.53 (correlated); the limiting gate is the
  SD band (just above 0.10), not difficulty. The independent review flagged SD clustering (shared per-PR reading
  couples the vial/strip/icon findings); the under-hold (R_TECH_HOLD, Weekly Leagues) vs over-hold (R_HOLD_SCOPE,
  Endless/Season Pass, now that Zombie Lane is off the calendar) split is retained to spread failure patterns.
  First-time pass is settled only by the six real Opus 5.5 baselines.
- **New mechanism `R_ASK_FOLLOWUP`** (family A14, "replies never opened"): what the push plan covers and that Zombie
  Lane stays off live in a thread reply under the ask itself (`D05SD5QLG94/1759263878.305129`). The completed
  `julia_zm_difficulty_baseline` task saw 3 of 6 Opus 5.5 runs miss DM thread replies, but the local
  `hardness_v2_check` classes a reply in the anchor's own thread as `first_read` (run on 2026-11-06 on the revision-2
  manifest: SAME_PLACE flag on T15, and a DECISION_FLIP flag because the rule decides weight-3 slots only), so its
  landing rate is uncertain and it must not be counted on as a difficulty carrier before the baselines.
- Exceptions on record: `volume_exception` (call 130 / per-record 75 / rows 70) — the honest lean-injection floors; no
  `cohort_exception` (cohort 44 ≥ 40 in revisions 2 and 3; 47 in revision 1). In revision 4 the cohort was 39, one
  short of 40; revision 5 brought it to 42 (three tickets are open again) and revision 6 to 41 (`ZOM-387` out), so no `cohort_exception` is needed
  (Revision 5 and Revision 6 below).
- The two-table local-decode (Calendar vs Pushes keyed by disjoint regexes) is a `/create-hardening` forensics item;
  the platform rubric is authoritative for decision polarity, timezone, destination and completeness.

### Revision 2 (after the 2026-11-05 /prompt FAIL)

Recorded 2026-11-06. The platform `/prompt` review of revision 1 (`plateform_reports/6aea4c1e9b621f28dc3a5332_1_prompt.md`,
reviewed SQL `4c6328ab2e86`, prompt `b5d6559cdf26`) returned FAIL: Unique Ground Truth 2, Clarity 2, Contrived 2, with
eight issues and seven open forks (F1 to F7). Revision 2 settles each fork in the data, as the review asked, and cuts
the field list from the prompt. Revision 2 SQL: sha256 `3afbf7cbbdb7`, 111 statements (77 INSERT, 34 UPDATE). Prompt:
sha256 `2a23afd87c4c`, 100 words. The task context was re-bound to this machine, so `context_hash` is now
`4bbc727fd48a…` (it was `7b0cc66ffd45…`).

| Issue | What the review found | Record that settles it (revision 2) | Base evidence behind the record |
|---|---|---|---|
| 1 (F1) | Lives recharged and 7-day lapse are Ready + LIVE but their copy names no game; go out or wait was open | Frederick's thread reply `D05SD5QLG94/1759263878.305127`: "Copy that does not name the game at all is fine to go out, the naming rule is only about wrong names." | push sheet `f_a325dd4af80afc5994d5dc`, PNs Beta rows 3 and 5: Ready, LIVE, copy with no game name |
| 2 (F2) | PNs Beta mixes Push Notification and Local Notification rows; whether local ones are beta pushes was open | same reply: "plan the PNs Beta tab as it stands, one line per row, local notifications included" | push sheet `f_a325dd4af80afc5994d5dc`: rows 2 to 6 are Local Notification, rows 1 and 7 to 14 Push Notification |
| 3 | the prompt restated the per-row fields of the ask (enumerated deliverable specs) | not a record: the revised prompt (`04_Prompt.txt`, sha256 `2a23afd87c4c`) drops the field list, points to Frederick's message and brief, and names only the sheet, the calendar ticket and Frederick (its wording is kept out of this file) | the ask `D05SD5QLG94/1759263600.418207` already lists the fields |
| 4 (F3) | four rows on the tab have no ZM3D beat; listed as waiting or left out was open | same reply: "Leave off the four rows for things that are not in the beta" (Hourly Coins, Nathan's Treasure Hunt, Streak Fever, Axe Arena), "just those four" | Brian, #company-internal `C05KNDCHAAG/1758558164.541689`: "decided to postpone Axe Arena for the beta release"; Confluence `page_liveops_calendar` lists Streak Fever, Nathan's Treasure Hunt and Axe Arena under Domino Delights; Hourly Coins has no ZM3D record |
| 5 (F4) | the ticket-note condition could mean held beats only, or also Collect & Win and Season Pass | brief `f_7c3e91a4d2b85f60e1a9c4`: "A beat that is only waiting on that release starts late, it is not held."; the revised prompt ties the ticket note to a held beat | Weekly Leagues is the only held beat and `ZOM-429` its ticket; `ZOM-566` and `ZOM-552` are analytics tickets |
| 6 (F5) | whether the Season Pass October season counts (server windows live before Oct 8 or not) was open | `#470#rc_10` and its mirror: "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod."; release event `evt_9a4c2e7f1b3d58e06c7a2f` (4 copies): "The server windows that are still on the DEV stack go live with this release" | Confluence `page_season_pass_spec`: reached production in the week of September 22-29, 2025; #zombie-bugs August prod reports for Plague Race and Endless (`C08R27X0EAH/1754561478.754139`, `C08R27X0EAH/1756460310.538629`) |
| 7 (F6) | the frame was said to be in one Android submission only; shipped or still to do was open | `#471#c_18` and its mirror: "it is in both submission builds from today, iOS 50 and Android 135, so nothing is left on it" | #builds `C05433XK267/1759259749.259909` (iOS Submission #50, main, success 2025-09-30 19:15:49Z) and `C05433XK267/1759263189.219529` (Android Submission #135, main, success 20:13:09Z), both after PR #471 merged 15:52:24Z |
| 8 | Brian's mails numbered the Nov 1 season as the second one, against the spec's monthly seasons | both mails in all six mailbox copies (and the Sep 22 snippet) now say "The November season" (`julia.lawson@harmonygames.co/1844470925517303296`, `julia.lawson@harmonygames.co/1844835127305531392`) | Confluence `page_season_pass_spec`: seasons reset monthly on the 1st at 00:00 UTC, the initial launch a partial first season; base has no season numbering |
| F7 | whether the brief's login-calendar rollover is the ZM3D daily gift or no beat at all | brief `f_7c3e91a4d2b85f60e1a9c4`: "For the quest rollover and the daily gift (the Login Calendar row on the push sheet)" | PNs Beta row 12 "Login Calendar update" on `f_a325dd4af80afc5994d5dc`; ZM3D daily-gift tickets `ZOM-432`, `ZOM-556` |
| Zombie Lane | the review rejected Zombie Lane as a beat (P1-DR1), but the old truth carried it as one | same reply: "keep Zombie Lane off the calendar, it is a permanent track with no window or reset to plan" | Confluence `page_liveops_calendar`: Zombie Lane, Zombie Match 3D, "Permanent (level-gated reward track)", Live |

Three further changes, each with its reason:

- `cmt_zom565_1` now reads "The endless start screen vfx is in (commit f7e971b0)." The old text named build #2023, but
  that is a Sep 30 build (#builds `C05433XK267`, started 2025-09-30 15:56Z) and the comment is dated 2025-09-29, so the
  seeded text ran ahead of base.
- `cmt_zom543_1` and the `ZOM-543` `updated_at` are re-dated to 2025-09-30T16:20:00Z. The comment lists Collect and Win
  in the queue-manager flow, and PR `harmonygames-Games/match3d#472` (Win & Collect into the queue manager) merged
  2025-09-30T15:53:04Z; the old Sep 29 date put the comment before the merge.
- The brief's new sentence "A beat that is only waiting on that release starts late, it is not held." closes the
  Collect & Win status. Under revision 1 a conditional hold until Oct 10 was accepted next to Runs, and a beat that
  may be called held is a beat that may get a ticket note, so the acceptance itself fed the ticket-note fork (issue 5).
  Collect & Win is now Runs with a late first window (Fri Oct 10 00:00 UTC) and gets no ticket note; the
  conditional-hold reading is no longer accepted.

State of the checks on revision 2 (this machine, 2026-11-06): `sql_lint` 0 errors / 8 warnings / 111 rows; eval
injection lint 0 FAIL / 0 CHECK / 0 INFO; `base_check` PASS (77 inserts, 34 updates; Check A and Check C PASS);
`base_claims` PASS; `check-sql` shows the new reply YES; `hardness_v2_check` flags T15 as `first_read` (expected, see
above). Not re-established here: the hardness gate (the local tool rejects `volume_exception.rows_floor`, §4), the
solver contract, fact check and preflight on the revised solver and manifest, and the stage gates. The pasted gate
block in §12 and the pasted `check-sql` lines in §4 are the revision-1 records (their hashes and the 29-YES count are
stale by design) and are re-pasted after the tool sync. One ordering point for that re-paste: the injection gate wants
its outputs newer than the Scenario Design, and the SQL file (2026-11-05 23:49) is older than the design edits of
2026-11-06.

### Revision 3 (after the second /prompt FAIL)

Recorded 2026-11-06. The platform `/prompt` review of revision 2 (`plateform_reports/6aea4c1e9b621f28dc3a5332_1_prompt-2.md`,
reviewed SQL `3afbf7cbbdb7`, prompt `2a23afd87c4c`; its injection gate records Eval 0 PASS on that SQL) passed every
dimension except Cross-Service Coherence: FAIL 2, one Major issue. The issue is known-issue card SC-15. Base `ZOM-521`
ticks all six checklist items, "Tokens traveling to live-ops" among them, while the child tickets `ZOM-526` and
`ZOM-528` are In Progress, and two seeded notes build on those tickets: `cmt_zom526_1` (the Season Pass part is still
being finished) and `cmt_zom521_1` (the checklist "is down to the last two items"). Under the review-repair rule
(GEN_EXECUTION §3) only that finding was acted on. Revision 3 SQL: sha256 `837d4f5dedbd`, 112 statements (78 INSERT,
34 UPDATE). Revision 2 is stored in `run_forensics/rev2/` and the transform is
`research/scripts/apply_review_fix_rev3.py`. The prompt (`2a23afd87c4c`) and the `context_hash` are unchanged.

The two SQL changes, as the review recommended:

| Change | Record (revision 3) | Base evidence behind it |
|---|---|---|
| 1. The master checklist matches its child tickets | UPDATE of the `ZOM-521` `description`: the base text with two ticks removed, "Tokens traveling to live-ops" and "Claimed Cards traveling to inventory Section"; the other four stay ticked; `updated_at` stays 2025-09-26T17:25:00Z, the time of Calvin's `cmt_zom521_1` ("down to the last two items") | `linear/data.json /issues/3596`: `ZOM-521`, In Progress, assignee Calvin Price, creator Brian Foster, base `updated_at` 2025-09-17T15:50:49Z, all six ticked. Children: `/issues/3597` `ZOM-523` Done, `/issues/3598` `ZOM-524` Done, `/issues/3599` `ZOM-525` Done, `/issues/3600` `ZOM-526` In Progress (started 2025-09-17T15:52:10Z, no assignee), `/issues/3601` `ZOM-527` Done, `/issues/3602` `ZOM-528` In Progress |
| 2. One dated line settles the Season Pass token travel | new `cmt_zom526_2` on `ZOM-526`, author `usr_fc22d5941b2aeb5c` (Brian Foster, the ticket's creator), 2025-09-26T15:40:00Z, sequence 2: "Unticked this one on the master ticket, it was marked done too early. The Season Pass part I mentioned above is polish on an effect that already ships: Season Pass runs without it, so it does not have to land before the beta buy or the November season." The `ZOM-526` `updated_at` follows it (2025-09-26T15:40:00Z, was 2025-09-24T17:30:00Z) | Calvin to Brian, `D0770ET6WBW/1758124315.038369` (2025-09-17T15:51:55Z): "I've updated the Master ticket VFX implementation and the remaining tickets.", with a Linear unfurl of `ZOM-521` that shows five items ticked, the token item among them, and Claimed Cards not ticked; `D0770ET6WBW/1758124394.939409` (15:53:14Z): "Yeah I still have Marcus's card animation ticket, and the queue manager.."; Brian, `D0770ET6WBW/1758658841.260899` (2025-09-23T20:20:41Z): "Does the season pass token animation start at about the same time as the level-end animation?"; Calvin, `D05S1S2H55M/1758228747.901729` (2025-09-18T20:52:27Z, in Spanish): RewardVFXManager already holds the instruction that instantiates the season pass token |

Julia is a member of neither of those two DMs (`persona_view can-see`: NO for both). The four messages are grounding
for the author only: they show that the seeded words agree with base ("marked done too early": the token item was
ticked on Sep 17 before its child ticket was even started, and Brian was still asking about the season pass token
animation on Sep 23; "an effect that already ships": on Sep 18 the client's reward VFX code already held the
instruction that instantiates the season pass token). No run has to read them, and nothing the task grades rests on
them.

Coherence audit line (§10): touched: SC-15 — repaired; not graded. The repair is not silent. The untick is explained
by a dated statement from the ticket's creator (`cmt_zom526_2`) and is recorded here, in §10 and in the design §2.
The manifest's `hazard_acknowledgements` does not list it, because that field takes `coherence_hazards.json` ids
only: a probe entry with the card id made `hardness_gate` fail its scope check on an unknown id, the `repaired`
resolution is verifiable for the Linear issue-state types alone, and no KB entry covers a description checklist
(`ZOM-521` is In Progress, so parent-Done-while-child-open does not apply). `base_check` reports no new touch on the
revision-3 SQL.

What does not change. The answer key: `solver/truth.json` regenerated on the revision-3 SQL is byte for byte the
revision-2 file (sha256 `a353abf56c0a`), and `oracle_kit check` against the stored revision-2 SQL and truth reports
0 field differences. `ZOM-521` and `ZOM-526` stay cohort members that are read per record; no solver rule, gradable
slot, trap, fragment or budget row uses the checklist or token travel, and Season Pass token travel stays outside
the Season Pass still-to-do (the brief leaves out polish nobody flagged, and the new line now says so in the
owner's words). Cohort 44, fragments 17, traps 26, call budget 200 and the 15 portfolio rules are as in revision 2.
The manifest generator (`research/scripts/build_manifest.py`) lists `cmt_zom526_2` with the seeded rows of the
per-issue comment surface and now writes the final manifest as well as the draft; the solver only advances
`REVISIONS` to `rev3`, which changes its digest in the manifest and nothing else.

State of the checks on revision 3 (this machine, 2026-11-06): `sql_lint` 0 errors / 8 warnings / 112 rows (78 INSERT,
34 UPDATE; linear 44); eval injection lint 0 FAIL / 0 CHECK / 0 INFO on sha256 `837d4f5dedbd`; `base_check` PASS (78
inserts, 34 updates; Check A and Check C PASS; the same two warnings); `base_claims` PASS; `fact_check --no-leak`
PASS (62 text-bearing rows, 9 facts, 10 superseded records); `check-sql` PASS (30 YES, 8 NO and 10 UNVERIFIED as
before; 64 unscoped rows); solver contract PASS, 8 of 8, with the regression against revision 2; the mutation and
liveness reports are the revision-2 reports apart from the label and the SQL sha (52 of 52 and 20 of 20 dispositions
recorded, so `01c_Dispositions.json` is unchanged); geometry U = 0.8919 (99/111), L_max UNSUPPORTED; gradable surface
PASS; `01c_Preflight_Report.json` regenerated: PASS, revision `rev3`, bound to the current SQL, solver, surface,
manifest and dispositions, forecast not run. Not re-established here, as before: the hardness gate (it fails on the
four lines that come from the `rows_floor` key this machine's tool does not know, `effective_profile`, `rows`,
`per_record_calls` and `call_budget`, and on nothing else) and the stage gates, whose pasted blocks stay the
revision-1 records. The platform `/injection`, `/prompt` and `/hardness` have to be run again on revision 3
(GEN_EXECUTION §3, re-run matrix).

### Revision 4 (after an independent /prompt run on revision 3)

Recorded 2026-11-06. An independent `/prompt` run on revision 3 (`research/prompt_review_rev3/1_prompt.md`, findings
`P1_findings.md` to `P4_findings.md`; reviewed SQL `837d4f5dedbd`, prompt `2a23afd87c4c`; Eval 0 on that SQL passed,
`0_injection.md`) returned FAIL 2: Cross-Service Coherence 2 and Clarity 3, every other dimension 5. Its nine issues:
(1) seeded notes that say done, live or closable on tickets still Todo; (2) open-work notes on PRs merged 11 to 48
days earlier; (3) Plague Race windows, where the synthetic warehouse rows show 5-day runs and the backend schedule and
Slack say daily; (4) the Halloween retraction threaded under an unrelated DM message; (5) Brian's "Re:" correction
sitting in a thread of its own with a snippet that was not the start of its body; (6) to (8) three wording gaps (how
the config owner is told, what the recommendation is about, two slips in the brief); (9) an advisory for the rubric.
Revision 4 repairs every confirmed item in the SQL. Revision 4 SQL: sha256 `c955d6ca2bca`, 106 statements (75 INSERT,
31 UPDATE). Revision 3 is stored in `run_forensics/rev3/` and the transform is
`research/scripts/apply_review_fix_rev4.py`. The prompt (`2a23afd87c4c`) and the `context_hash` are unchanged.

| Change | Record (revision 4) | Base evidence behind it |
|---|---|---|
| A1. Vial sprites (Claire): the note leaves #370 | removed `#370#rev_1`, `#370#rc_1`, `#370#ev_5`, the #370 `updated_at` bump, mirror `408dca28…` and its parent UPDATE. New `#468#rev_3` (Arthur, COMMENTED, 2025-09-29T15:36:41Z), inline `#468#rc_38`, timeline `#468#ev_6` ('reviewed'), mirror `dacaa8f6a19ad6b982002af8cfcacf0e` | base #370 "Collect&Win Items" merged 2025-08-13T16:12:18Z, so the old note (2025-09-30T19:48:33Z) came 48 days after the merge; base #468 "Collect And Win" was opened 2025-09-26T20:16:25Z and merged 2025-09-29T16:13:50Z and holds `rev_1`-`rev_2`, 37 inline comments and `ev_1`-`ev_5`; its #zombie-prs thread parent `4b7c4127…` has `reply_count` 41 and `latest_reply` at the merge post, which the SQL leaves in place (41 to 42) |
| A2. Premium strip (Oliver): the note leaves #438 | removed `#438#rev_4`, `#438#rc_74`, `#438#ev_9`, the #438 bump, mirror `cc8ce0e4…` and its parent UPDATE. New conversation comment `#473#c_2` (Arthur, 2025-09-30T16:16:33Z, the same sentence), timeline `#473#ev_5` ('commented'), the #473 `updated_at` bump, mirror `c85ccb18d375623f4b06db42e6b2e2c6` | base #438 "Feature/season pass" merged 2025-09-15T23:09:34Z (old note 15 days later); base #473 "Addressables/sp" merged 2025-09-30T15:41:20Z and holds `c_1` and `ev_1`-`ev_4`; its #zombie-prs thread parent `d05a2f8a…` has `reply_count` 2 (2 to 3) |
| A3. Collect & Win icon animation (Marcus): the note leaves #454 | removed `#454#c_4`, `#454#ev_6`, the #454 bump, mirror `8a9a7466…` and its parent UPDATE. New `cmt_zom465_2` on `ZOM-465` (Marcus, 2025-09-30T18:05:00Z, sequence 2); the ZOM-465 `updated_at` follows it | base #454 "Marcus/animated icons" merged 2025-09-19T17:50:52Z (old note 11 days later); base `ZOM-465` "Endless Mode Master VFX Ticket" is In Progress and assigned to Marcus (`usr_c77c50cc15c5342d`), started 2025-09-23T14:16:25Z, so a note on it on Sep 30 sits on a live ticket |
| B. Ticket states follow the tickets' own notes | `ZOM-565`, `ZOM-471`, `ZOM-344`, `ZOM-542`, `ZOM-432` Done; `ZOM-566`, `ZOM-387` In Progress (times in the §2 ledger row) | base states: `ZOM-565` Todo, `ZOM-471` Todo, `ZOM-344` Todo, `ZOM-542` Regression, `ZOM-432` Todo, `ZOM-566` Todo (created 2025-09-30T16:26:02Z), `ZOM-387` Todo (created 2025-07-15). Review: every base ZOM Done ticket has `completed_at` and 401 of 427 have `updated_at` equal to it; every base In Progress ticket has `started_at` |
| C. Halloween retraction | `58d06bd55ea4129eaadb726291967d5a` is a top-level message in DM `D05GU6L0XFH` (thread fields NULL); the `reply_count` UPDATE on `c5431028…` is gone | the old parent is Robert's unrelated Sep 30 question about hardcore players (review P2-DR4); its base `reply_count` is 0 |
| D. Brian's correction | the Sep 26 mail (three mailbox copies) has subject "ZM3D Season Pass November config handoff: new date", no In-Reply-To or References, a snippet cut from its own body, and ends "The November season still opens on Sat Nov 1. If the new date is a problem on your side, reply on this mail." Ids and thread ids unchanged | review P2-DR5: in base a reply's In-Reply-To points inside its own thread (216 of 216), and a snippet is the start of the body, as on the Sep 22 mail |
| E. Shapes | `#470#ev_9` is 'reviewed' with no actor and no time and the commit in its data; mirrors `c778c9b9…` and `a0c26779…` have subtype NULL and the handles arthur.blake and samuel.turner; `a0c26779…` links issuecomment-3353762954 | base 'reviewed' timeline events carry no actor and no time (2,116 of them; #470's own `ev_2`-`ev_6`); base #zombie-prs posts have subtype NULL and people's handles ("Pull request opened by" owen.baker on #468's parent) |
| F. Brief (`f_7c3e91a4d2b85f60e1a9c4`, 2,704 characters) | "For the quest rollover, the daily gift (the Login Calendar row on the push sheet) and Plague Race put down whether the beat is in and whether its push is ready, not its window dates."; "One-offs may overlap recurring beat slots. A one-off may take a recurring beat slot only with the latest dated approval from Product, and if he takes that back his later word is the one that counts."; "A committed date that misses the lock moves earlier and its owner is told in a reply on the mail where they committed to it." | review P2-DR3: the synthetic Snowflake `LIVE_EVENT_PERFORMANCE` rows give Plague Race 5-day runs while the backend schedule and #zombie-ops say every day at 00:00 UTC; Snowflake cannot be injected, so the answer no longer depends on it. The other two sentences fix wording the review flagged (issues 6 and 8) |
| G. Frederick's ask (`8b090dec472117f4598b9ad84318272e`) | "… what still has to land before it runs and who owns that. Put it in the calendar sheet in your ZM Live Ops folder and link it on the calendar ticket. Then send me your recommendation back here, with the trade-offs, on what we run and what we hold in those weeks. The working rules for the calendar are in my brief, shared with you. This goes into the pivot call, so I need your call, not a list of what we have." | review issue 7 (the decision the recommendation answers was not named) and fork F8 (whether the recommendation also goes in the sheet): the calendar and the recommendation are now two sentences with their own destinations |
| H. Release event | the four `gcal_events` rows are `opaque` | review, optional cleanups: base calendar events are `opaque` |

The base facts in the right-hand column for #370, #438, #454, #468, #473, the two #zombie-prs parents and the eight
Linear tickets were re-read through `hg.py` on 2026-11-06 for this entry; the counts quoted from the review (427, 216,
2,116) and the Snowflake rows are taken from its report and were not re-read.

What does not change. The answer key: `solver/truth.json` regenerated on the revision-4 SQL has the same 17 keys and
the same value in every field as the revision-3 file. Two evidence lists differ and nothing else: Collect & Win lists
`#468#rc_38` where it listed `#370#rc_1` and `cmt_zom465_2` where it listed `#454#c_4`; Season Pass lists `#473#c_2`
where it listed `#438#rc_74`. The solver names each of the three notes with both carriers and reads the one the SQL
holds, so on the revision-3 SQL it still gives the revision-3 truth byte for byte (`oracle_kit check`, regression).
Seven beats, ten push rows, 15 rules, 17 fragments, 26 traps and the 31 surface slots (ids, titles, selectors, weights,
accepted outcomes) are as they were; seven slot work reasons were reworded because they named records that moved.

What does change in the design record, said plainly:
- **Cohort 44 to 39.** The cohort is the open ZOM issues that bear on a beat plus the merged PRs that carry a fact for a
  beat in their own body, commits or files. Five of the 21 issues are Done since this revision (`ZOM-344`, `ZOM-432`,
  `ZOM-471`, `ZOM-542`, `ZOM-565`) and so are no longer open work items; 16 stay (`ZOM-78`, `ZOM-387`, `ZOM-429`,
  `ZOM-465`, `ZOM-504`, `ZOM-517`, `ZOM-521`, `ZOM-526`, `ZOM-534`, `ZOM-543`, `ZOM-544`, `ZOM-546`, `ZOM-549`,
  `ZOM-552`, `ZOM-556`, `ZOM-566`). All 23 PRs stay, #370, #438 and #454 included: each is a member for its own
  content (`research/EXPAND_cohort_feasibility.md` §2), never for the note that sat on it. 39 is one short of the
  extreme minimum of 40 and no `cohort_exception` is on record, so `hardness_gate` fails `cohort_size`. This needs the
  requester's confirmation of an exception or a later revision that leaves one of the five open; it is not papered
  over here.
- **Call budget 200 to 192, per-record surfaces 138 to 133.** Minus 5 comment reads on the closed tickets, minus 1
  thread-open call for the retraction, minus 2 for the separate read of PR #471, which nothing requires once ZOM-432
  is Done. Both requester floors hold (130 calls, 75 per-record).
- **Four traps are weaker.** T10: ZOM-432 is itself Done, so the frame question arises only for a run that meets
  Calvin's Sep 24 note and prefers it to the ticket's later closure; it no longer fits "the item looks open", and its
  rule must not be counted as a difficulty carrier (its disposition is now `weak-accepted`). T2: nothing hides the
  retraction any more. T14: the claim and its correction are two comments on one ticket. T8: unchanged in substance,
  the correction was already in another thread.
- **L03 is `repaired`** (ZOM-387 leaves Todo; verified by `base_check`), and S04 is no longer touched.
- **Dispositions.** Four mutation rows were reworded because their deciding record moved or its ticket changed state:
  `rule:R_WITHDRAWN`, `rule:R_DONE_ELSEWHERE` (also `live` to `weak-accepted`), `rule:R_REVIEW_FLAGS` and
  `rule:R_ICON_SCOPE`. No liveness row changed: the flags are the same 20.

State of the checks on revision 4 (this machine, 2026-11-06): `sql_lint` 0 errors / 8 warnings / 106 rows (75 INSERT,
31 UPDATE); eval injection lint 0 FAIL / 0 CHECK / 0 INFO on sha256 `c955d6ca2bca`; `base_check` PASS (75 inserts, 31
updates; Check A and Check C PASS; one warning, the L03 touch, resolution `repaired`, verified on the post-SQL state);
`base_claims` PASS; `fact_check --no-leak` PASS (61 text-bearing rows, 9 facts, 10 superseded records); `check-sql`
PASS (29 YES, 8 NO, 8 UNVERIFIED; 61 unscoped rows); solver contract PASS, 8 of 8, with the regression against
revision 3; mutation and liveness reports the same as on revision 3 apart from the label and the SQL sha (52 of 52
and 20 of 20 dispositions recorded); geometry U = 0.8919 (99/111), L_max UNSUPPORTED; gradable surface PASS (31 slots,
weight 111); `01c_Preflight_Report.json` regenerated: PASS, revision `rev4`, forecast not run. The hardness gate fails
on five lines: the four that come from the `rows_floor` key this machine's tool does not know (`effective_profile`,
`rows`, `per_record_calls`, `call_budget`) and `cohort_size` (39, need 40), which is real. The stage gates were not
re-pasted; their blocks stay the revision-1 records. Read-only, the injection gate fails two lines that are not stale
pastes: `tool.hardness_gate` (the five lines above) and `tool.base_check`. The gate re-runs `base_check` without
`--manifest`, so it never reads the `repaired` resolution, and run that way `base_check` fails Check C on the ZOM-387
UPDATE; with the manifest it passes, as quoted above. That needs the gate to pass the manifest, or a later revision
that leaves ZOM-387's state alone. The platform `/injection`, `/prompt` and `/hardness` have to be run on revision 4
(GEN_EXECUTION §3, re-run matrix).

### Revision 5 (after an independent /prompt run on revision 4 and an audit of every injected record)

An independent `/prompt` round on revision 4 (`research/prompt_review_rev4/1_prompt.md`, passes `P1_findings.md` to
`P4_findings.md`, Eval 0 in `0_injection.md`), a claim-by-claim audit of every injected record against the whole base
(`research/prompt_review_rev4/claims_*.md`: code and git history on main, DMs, notification mails, Trello and Gmail
conventions) and a re-audit of the re-written records (`research/prompt_review_rev5_audits/reaudit_linear.md`,
`reaudit_other.md`) found statements, dates and field shapes that base contradicts. The transform is
`research/scripts/apply_review_fix_rev5.py` (pure text, asserted anchors; input sha256 `c955d6ca2bca`, output
`3c035f2af029`, 70 INSERT and 26 UPDATE). Revision 4 is archived in `run_forensics/rev4/` (SQL, prompt, truth). The
prompt is unchanged (sha256 `2a23afd87c4c`).

**What changes in the answer key (deliberate).** Two cells and nothing else:

- **Quests still-to-do is empty.** The quest note is now Leonard's, on the open quests card #61, and says "the current
  set carries the first week". Nothing has to land before the beat runs, and the brief asks for the quest rollover only
  whether the beat is in and whether its push is ready. Slot S06, rule `R_QUEST_SET` and fragment K11 are retired; T12
  keeps its id as an ungraded distractor; T3 keeps its slots and loses the Trello record.
- **Collect & Win's vial item reads "the final vial models (Claire)".** Arthur's note names Claire's 3D vial models;
  the UI sprites are Martin's and the PR already ships them.
- Daily Login is unchanged in value (nothing left) but is now decided on one record: Samuel's frame note is on the
  ticket it closes. Slot S07 is re-classified from multi-source reconciliation (weight 5) to lookup (weight 1); T10 is a
  trap in name only; chain CH5 is retired; `R_DONE_ELSEWHERE` keeps its id for stability and is no difficulty carrier.
- Unchanged: seven beats, ten push rows, every Status and Send-or-hold value, Collect & Win's Fri Oct 10 00:00 UTC
  first window, Plague Race in all four weeks, the Season Pass and Collect & Win still-to-dos (with the vial wording
  above), and the five writes.

**Ids that changed** (the old values are in `run_forensics/rev4/01_Universe_Inject.sql`):

| Record | Revision 5 id | What moved |
|---|---|---|
| Frederick's ask | `bca784379e7dbca9e64e79a64dfefbba`, ts `1759263617.418209` (20:20:17Z) | ts was `1759263600.418207` |
| his thread reply | `890dc27f56e8501bd7590ffdfc231057`, ts `1759263878.305129` | ts ended in 7; parent id and the root's `latest_reply` follow |
| Robert's approval | `933cee9f6464a80e4b1f05259b595b20`, ts `1758213623.552919` (16:40:23Z) | ts was `1758213600.552913`; the parent also gets `thread_ts_legacy` |
| Robert's retraction | `669d15f685f158633e56302160957f1e`, ts `1759270241.638119` (22:10:41Z) | ts was `1759270200.638114` |
| Vincent's re-test | `b5f2955c2e154efc6835946ecfe1758e`, ts `1759265412.481909` | ts ended in 7 |
| #470, #468, #473 mirrors | `73bc730c620936feba3dcfbba00e2745`, `78aa8ed77c0bd7b8a3fad227b22bc3fb`, `bd1a7d0ac25ccb2ee31db82d61f38607` | each posts 2-3 s after its event; the #471 mirror is gone |
| Brian's Sep 22 mail | `<CAPT--p4sBC8XnaA7qBDMtZkWqJPiXP0MT3deOQGPusOZhHF+vo@mail.gmail.com>`, Julia's thread `1843954828968533812` | Message-ID shape; one thread id per mailbox |
| Brian's Sep 26 mail | `<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>`, Julia's thread `1844311412966040123` | same |
| Samuel's frame note | `cmt_zom432_2` | was `#471#c_18` with `#471#ev_8` |
| the quest note | `68dac8204f1e9a3b7c2d5e61` (unchanged) on card `68c452a03006277f55d9dc96` | card was `6851a724601a61857a1b202f`; author was Brian |

**Records revision 5 re-words, re-times, moves or removes, with the base fact behind each**
(`apply_review_fix_rev5.py` carries the same reasons next to each change):

| Record | Revision 5 | Base grounding |
|---|---|---|
| `#470#rc_10` | part of Arthur's base approval review `#470#rev_9` at 2025-09-30T15:51:06Z; the seeded `#470#rev_10`, `#470#ev_9` and the PR bump are removed; its mirror posts before the base "merged" post, so the thread's `latest_reply` stays base | base `rev_9` is his APPROVED review at that instant and the PR merged at 15:51:15Z; a second review 13 minutes after the merge had no base shape |
| `#468#rc_38` | "the final vial models", on `Assets/Match3D/Game/Levels/GameLoader.cs` | Claire owns the 3D vial objects; Martin owns the UI sprites, which this PR ships in five colours (`claims_github_slack.md`) |
| `#473#c_2` | says which range the strip is on and by when it changes; `updated_at` NULL | every base PR comment has `updated_at` NULL |
| `#471#c_18`, `#471#ev_8`, its mirror, the #471 bump | removed | a note five hours after a merge has no base precedent (`1_prompt.md` C3) |
| `cmt_zom432_2` (new), `ZOM-432` | Samuel's closing note at 2025-09-30T21:07:26Z; `completed_at` and `updated_at` equal it (the closure was 21:20:00Z) | base PR #471 merged on Sep 30 and both submission builds of that day follow it (#builds iOS Submission #50, Android Submission #135) |
| the five Slack messages people wrote | ts off the whole minute and ending in 9; ids and `created_at` follow | every base Slack ts ends in 9; base parents with replies carry their own thread ts |
| the three mirrors and their parents | post 2-3 s after the event, '&' escaped, attachment ts = event time; the #468 card names Arthur as a reviewer, the #473 card counts 2 comments | base GitHub-app rows in `C093LEZGF6J`, 2025-09 |
| `cmt_zom429_1` | dated 2025-09-16T18:12:04Z; the ZOM-429 UPDATE is dropped | the note predates the Sep 19 regression that Vincent reported on Sep 22 ("Killing the app doesn't help"); base `updated_at` is already Sep 22 |
| `cmt_zom556_1` | "the lower day row still carries on ... but claiming works and nothing is lost" | the day row not resetting is the reported bug itself |
| `cmt_zom565_1`, `ZOM-565` | Marcus's note at 2025-09-29T14:34:12Z: the new bar is hidden for Calvin to hook up, "not needed for the beta"; the ticket stays Todo | his commit on `Marcus/EndlessMode_Vfx` at 14:33:08Z and his DM "i wrote a comment on the linear task" at 14:34:25Z |
| `cmt_zom526_1`, `cmt_zom526_2` | Season Pass tokens already fly to the icon; what is left is the Collect and Win trigger | token travel is on main for Season Pass since PR #438 (Sep 15); the Collect and Win trigger sat on its branch until Sep 29 |
| `cmt_zom552_1` | all three events are sent; no "release notes" | the events were in by Sep 19; base has no release notes |
| `cmt_zom465_1` | "every event icon on the main menu has its animation now" | the icons animate when they call for action, not at idle |
| `cmt_zom344_1` | "on the quest screen" | "the hub" is not a term base uses |
| `cmt_zom387_1`, `ZOM-387` | comment and UPDATE removed; the ticket is exactly as base has it | base has it as Arthur's ticket with PR #319 merged on Jul 19; the seeded note named another engineer and a start six days after that merge (`claims_linear_B.md` §3) |
| `cmt_zom442_1` | the event and the two parameters that are in code | three sheet super properties are not sent |
| `cmt_zom471_1`, `ZOM-471` | "Not started ... Parking it, nothing here has to land for the beta"; the ticket stays Todo | nothing is wired on main; in the thread the ticket came from Leonard says to drop it |
| `cmt_zom504_1` | "Still only shows up with the bot running" | Vincent's own base word |
| `cmt_zom517_1`, `ZOM-517` | no "refill flag"; dated 2025-09-18T17:40:54Z | no such flag exists in code; Robert was in another thread at 14:50Z |
| `cmt_zom521_1` | "down to the last two items" | on Sep 26 neither open item was finished (queue integration merged Sep 30, cards reached a test build Sep 29) |
| `cmt_zom542_1`, `ZOM-542` | "Not in the build yet ... not needed for the beta"; the ticket keeps its base state | the new screens are not on main; Julia's own Sep 22 status post has Samuel on the bug list |
| `cmt_zom544_1` | sign-in works from the settings menu, progress does not restore yet | Vincent's base messages since Sep 22 |
| `cmt_zom546_1`, `ZOM-546` | dated 2025-09-24T19:00:57Z | inside Owen's usual hours |
| `cmt_zom549_1` | "left_level does not send total_equipped_power yet" | the field is not sent on main |
| `cmt_zom566_1` | "Wiring both into the analytics manager now, ahead of the beta." | at 19:40Z nothing was committed (first commit 22:23Z; PR #477 opened 22:26Z and is still open) |
| every Linear timestamp | carries seconds | base issue stamps are never on the whole minute as a set |
| Brian's two mails (six copies) | his Message-ID shape, a `+0300` Date header, per-mailbox thread ids, plain To and Cc, no Reply-To; sent copies without Delivered-To; Julia's Sep 22 copy labelled as opened, the correction not opened | base: a thread id shifted right by 20 bits is the mail's time in ms; internal mail carries no Reply-To; her mailbox never uses UNREAD |
| brief, deck, sheet, folder, release event | working-hours stamps with seconds; size and content_path on the Doc and Sheet rows; the folder is modified with its newest child; the event title uses a plain hyphen | Frederick has no base activity between 07:00 and 11:59 UTC; base Doc rows carry size and content_path |
| the deck's retention line | "The Unity retention campaigns are a separate budget and are not part of these buys." | the Unity retention budget was at $1 on Sep 23, so "already running" was not true |
| the quest note and its card | on the open card #61, by Leonard, with "the current set carries the first week"; the card revision 4 touched keeps its base badges | the old card was completed on Jun 30 and 0 of 45 completed cards carry a later comment; card #61 is the only open quests card, Leonard created it and Brian has no Trello activity; every base action on that list names it "BETA: Sep 30" |

**What it does to the design files** (manifest and surface are regenerated from `research/scripts/build_manifest.py`
and `build_surface.py`; the solver is `solver/solver.py`, revision `rev5`):

- Solver: fourteen rules. Every re-keyed record is a tuple of carriers, newest first, and the two cells that changed are
  read from the words of the note the SQL holds, so the same rules give the revision-4 truth byte for byte on the
  revision-4 SQL. `truth.json` differs from `run_forensics/rev4/truth.json` in two values (the Quests still-to-do, the
  vial wording) and in the evidence ids of eleven rows, all of them ids listed above.
- Surface: 30 slots, weight 102 (31 / 111). S06 is dropped, S07 is a weight-1 lookup, S08 reads "the final vial models
  (Claire)". Geometry U = 0.8824 (90/102; it was 0.8919, 99/111).
- Manifest: 14 rules, 16 fragments over 7 services and 10 containers, 26 trap entries (14 traps and 12 distractors,
  T12 now among the distractors), 5 chains, 8 facts.
- Cohort, on the definition in K6: 42 members, 19 open issues + 23 merged PRs. `ZOM-565`, `ZOM-471` and `ZOM-542` are
  open again and are back; `ZOM-344` and `ZOM-432` are Done and out; `ZOM-387` is in as base has it, because it is an
  open ticket that names un-instrumented events of Plague Race and quests, the same class as the analytics members
  `ZOM-549`, `ZOM-552` and `ZOM-566`, and membership does not depend on a seeded note. No exception is needed.
- Call budget: 194 unconditional of 204 planned (192 of 202): +3 per-issue comment reads, −2 Trello calls, +1
  Confluence read. Per-record surfaces 136 (133). Both floors of the `volume_exception` hold (130 / 75).
- Services: Trello carries no weight (no graded value needs a Trello read) and keeps only its role, because the schema is
  injected and T12 lives there. Confluence is declared with its weight reason: the base `page_season_pass_spec` is the
  only source of the 24 h lock offset that the Season Pass config deadline needs. It has been on the required path since
  the brief stopped stating the offset; it had not been listed because ten services were listed without it. Ten
  services still carry weight and ten are in the budget. Without this declaration both lines would read nine.

**Tool results on revision 5 on this machine** (2026-11-06; nothing below is pasted into a gate block):

- `sql_lint`: errors 0, warnings 8 (the Oct 8 plan event), 96 rows. `hg.py lint --sql`: FAIL 0, CHECK 0.
- `base_check`: PASS with and without `--manifest` (70 inserts, 26 updates). `base_claims`: PASS.
- `fact_check --no-leak`: PASS, 8 declared facts. `check-sql` with the new ids: PASS (29 YES).
- `oracle_kit check` against revision 4: PASS, 14 rules, regression byte for byte, 0 field differences from the current
  rules on the revision-4 SQL.
- Mutation: `R_DONE_ELSEWHERE` is now WEAK (it flips only the weight-1 slot S07); the other verdicts are unchanged; 50
  dispositions. Trap liveness: 20 dispositions, no new flag. Surface validation: PASS.
- `hardness_gate`: FAIL on the four lines that follow from `volume_exception.rows_floor` being unknown to this machine's
  tool (`effective_profile`, `rows`, `per_record_calls`, `call_budget`) and on one line of its own, `hazard_scope`.
- Forecast, not pre-registered and UNCALIBRATED: design mode E[avg] 0.614 [0.503, 0.722], P(all four gates) 0.475
  (independent) to 0.542 (correlated); on revision 4 it read 0.596 and 0.510 to 0.536. Solver mode E[avg] 0.808
  [0.739, 0.876], P(all) 0.041 (independent) to 0.452 (correlated); on revision 4, 0.813 and 0.03 to 0.44.

**Open after revision 5, said plainly.**

1. `hazard_scope` fails. `ZOM-387` is a cohort member on the definition, so the manifest cites it; base has it Todo
   with its PR merged; revision 5 neither changes nor explains it. `repaired` is false, `excluded` is false because the
   design cites it, and `dated_claim` is false because no seeded text is about it. The ways out are the designer's: take
   `ZOM-387` out of the cohort by a definition that excludes it on its merits (the cohort would be 41), or seed a dated
   record that base supports.
2. The quests and daily-gift rows carry almost no graded difficulty now. S06 is gone and S07 weighs 1; what is left on
   those rows is that they are on the calendar at all (S04, S05, V01).
3. Three of the fourteen rules are weak by their own records: `R_DONE_ELSEWHERE` (one ticket), `R_WITHDRAWN` (a
   top-level DM message since revision 4) and `R_ICON_SCOPE` (both notes on one ticket). The forecast prices them at
   their family priors, which overstates them.
4. The solver-, manifest- and gate-bound lines in §4 and the pasted gate block are still revision-1 records.
### Revision 6 (after the independent /prompt run on revision 5)

The independent round on revision 5 (`research/prompt_review_rev5/1_prompt.md`, passes `P1_findings.md` to
`P4_findings.md`, `ugt_section.md`, Eval 0 in `0_injection.md`) scored Cross-Service Coherence 5 and every other dimension
5 except Unique Ground Truth, which failed on one fork: nothing said whether the Oct 13 quest set has to land for the
beta. The transform is `research/scripts/apply_review_fix_rev6.py` (pure text, asserted anchors; input sha256
`3c035f2af029`, output `f8d905bdd0c2`, 71 INSERT and 26 UPDATE). Revision 5 is archived in `run_forensics/rev5/`. The
prompt is unchanged. The answer key does not change: `truth.json` is byte for byte the revision-5 file.

| Record | Revision 6 | Base grounding |
|---|---|---|
| the quest note `68dac8204f1e9a3b7c2d5e61` | "New quest set goes in with the Mon Oct 13 rollover if it is ready. Nothing in the beta waits on it, the current set runs the whole time either way." (re-worded again in revision 7) | settles the fork toward "Quests has no still-to-do", which is what the key already says |
| `cmt_zom544_1` | "Apple sign-in works from the settings menu, but progress does not restore yet: levels, currencies and cards are not synced." | drops the Google Play sentence, which read as the brief's "unverified build or platform" case although sign-in is not a beat, and the branch name, which cannot be traced in the repository |
| `cmt_zom526_2` | now ends "What is left is the Collect and Win trigger I mentioned above and, once that event is back, Axe Arena. It is polish on an effect that already ships for Season Pass, and the events run without it, so it does not have to land before the beta." | the token-travel enum on main, `ERewardLiveopsCategory` in `Assets/Scripts/UI/LiveOps/ERewardType.cs`, holds only `SeasonPass` and `WinAndCollect` (re-read in the base export) |
| `cmt_zom526_3` (new), `ZOM-526` | Calvin Price (`usr_49b9dfa5208d400d`), 2025-09-30T16:24:19Z, sequence 3: "Collect and Win tokens go through the queue manager now (#472). Only the Axe Arena travel is left here, and that waits on the event coming back."; the ticket's `updated_at` follows it | base PR #472 "Implement Win&Collect into Queue Manager" merged 2025-09-30T15:53:04Z (re-read); Brian's #company-internal post `C05KNDCHAAG/1758558164.541689`, 2025-09-22T16:22Z, postpones Axe Arena for the beta release; base keeps ZOM-526 In Progress, and this note says why |
| Brian's Sep 22 mail (three copies) | "Nothing else changes." | the phrase "from the September handoff" is gone: no such handoff exists in base |
| Drive rows of the Doc and the Sheet | size and content_path back to NULL | a path with no bytes behind it could fail a download at run time; `id_contracts.json` says NULL means no bytes, and both files are served from their gdocs / gsheets rows |
| Gmail, six rows | `in_reply_to` and `references` are '' ; Brian's sent copies carry `["ARCHIVED","SENT","Label_b19fb8d1b3"]` and "Archived,Sent,Opened" | base non-reply mail carries empty strings, and base sent mail carries the ARCHIVED label |

**The requester's decisions on the three points revision 5 left open.**

1. `ZOM-387` is out of the cohort on its merits. It is a KB `L03` record: its Todo state is not reliable, because its PR
   merged in July, and the KB's guidance is to keep such issues out of cohorts whose predicate is "open". The SQL does
   not touch it, and no manifest section names it any more. The cohort is 41 (18 issues + 23 PRs), the per-record
   surfaces 135 (136) and the call budget 193 unconditional of 203 planned (194 of 204). `hazard_scope` passes with an
   empty acknowledgement list.
2. Confluence stays the tenth weight-carrying service (the 24 h lock on `page_season_pass_spec` is on the required path
   for S10 and W07), and Trello stays a touched schema with no weight.
3. S07 stays a `lookup`, weight 1.

### Revision 7 (after the independent reviews of revision 6)

The Eval 0 run on revision 6 (`research/prompt_review_rev6/0_injection.md`) left two advisories, E1 and the cards half of
D6. The transform is `research/scripts/apply_review_fix_rev7.py` (pure text, asserted anchors; input sha256
`f8d905bdd0c2`, output `091722f6a281`, 72 INSERT and 26 UPDATE). Revision 6 is archived in `run_forensics/rev6/`. The
prompt is unchanged. The answer key does not change: `truth.json` is byte for byte the revision-5 and revision-6 file.

| Record | Revision 7 | Base grounding |
|---|---|---|
| the quest note `68dac8204f1e9a3b7c2d5e61` | "More quests get added with the Mon Oct 13 rollover if they are ready. Nothing in the beta waits on them, the current quests keep running either way." | advisory E1: "goes in ... if it is ready" and "the current set runs the whole time" fit together only if the new quests are additive, as the card's name says ("Add more quests and balance quest rewards") |
| `cmt_zom521_2` (new), `ZOM-521` | Calvin Price (`usr_49b9dfa5208d400d`), 2025-09-30T16:27:38Z, sequence 2: "Card pack animation went in with #475. I am leaving this item and ZOM-528 open until Brian has seen it in a build."; the ticket's `updated_at` follows it | advisory D6 (SC-16 pattern): base PR #475, Calvin Price's, body "Adding card pack animation", merged 2025-09-30T16:09:15Z (re-read), while ZOM-521 keeps the cards item open and child ZOM-528 stays In Progress. No base Slack message between the merge and the clock mentions this work |

Solver: `REVISIONS` advances to rev7 and `_quest_set_waits` tests the words revisions 6 and 7 share. `cmt_zom526_3` and
`cmt_zom521_2` decide no key and are not deciding records. They are listed with the seeded rows of the per-issue comment
surface, because the comment calls on ZOM-526 and ZOM-521 return them.

**ZOM-521 and ZOM-528, stated plainly.** ZOM-528 is not a cohort member and is not read. ZOM-521 has been a cohort member
since revision 1 and stays one: revision 7 adds a note to a ticket that is already in the cohort and moves no number. No
graded slot reads either ticket. `cmt_zom521_1` stays a deciding record of `R_HOLD_SCOPE` for Endless Monster Mode.

**Tool results on revision 7 on this machine** (2026-11-06; nothing below is pasted into a gate block):

- `sql_lint`: errors 0, warnings 8 (the Oct 8 plan event), 98 rows. `hg.py lint --sql`: FAIL 0.
- `base_check`: PASS with and without `--manifest` (72 inserts, 26 updates). `base_claims`: PASS.
- `fact_check --no-leak`: PASS, 8 declared facts. `check-sql`: PASS (29 YES, 8 NO, 6 UNVERIFIED, 55 unscoped rows).
- `oracle_kit check` against revision 6: PASS, 14 rules, regression byte for byte, 0 field differences. The solver also
  reproduces the revision-2 to revision-6 truths on their own SQLs.
- Mutation and trap liveness: every verdict and flag is the same as on revision 5, so `01c_Dispositions.json` is
  unchanged (50 and 20 dispositions). Surface validation: PASS, 30 slots, weight 102, U 0.8824 (90/102).
- `hardness_gate`: `hazard_scope` and `cohort_size` pass; it fails only on the four lines that follow from
  `volume_exception.rows_floor` being unknown to this machine's tool (`effective_profile`, `rows`, `per_record_calls`,
  `call_budget`).
- Forecast, not pre-registered and UNCALIBRATED: unchanged from revision 5. Design mode E[avg] 0.614 [0.503, 0.722],
  P(all four gates) 0.475 (independent) to 0.542 (correlated). Solver mode E[avg] 0.808 [0.739, 0.876], P(all) 0.041
  (independent) to 0.452 (correlated).

**Open after revision 7, said plainly.**

1. The quests and daily-gift rows carry almost no graded difficulty: S06 is gone and S07 weighs 1, so what is left is that
   they are on the calendar at all (S04, S05, V01).
2. Three of the fourteen rules are weak by their own records: `R_DONE_ELSEWHERE`, `R_WITHDRAWN` and `R_ICON_SCOPE`. The
   forecast prices them at their family priors, which overstates them.
3. The solver-, manifest- and gate-bound lines in §4 and the pasted gate block are still revision-1 records.
### Revision 8 (after a fresh blind /prompt round on revision 7)

The round on revision 7 (`research/prompt_review_rev7/`, passes `P1_findings.md` to `P4_findings.md`, Eval 0 in
`0_injection.md`) raised two fail-level forks (P1), four low-impact items (P2) and two optional wording fixes (Eval 0). The
transform is `research/scripts/apply_review_fix_rev8.py` (pure text, asserted anchors; input sha256 `091722f6a281`, output
`0e8c8ad83f3b`, 71 INSERT and 25 UPDATE, 96 statements). Revision 7 is archived in `run_forensics/rev7/`. The prompt is
unchanged. No graded value changes. `truth.json` differs from revision 7 in one evidence id on the Season Pass row:
`#473#c_2` becomes `#472#rc_1`.

| Record | Revision 8 | Base grounding |
|---|---|---|
| brief `f_7c3e91a4d2b85f60e1a9c4`, "Held or not" | adds "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." (body 2,807 chars; later heading offsets shift by the same 103) | P1 DR1, P2 DR3: the ask wants "held and until when" and Weekly Leagues has no dated fix |
| `cmt_zom534_1` | "Quest points rollover now syncs quests-end with the client instead of waiting on a restart. That is on main, so nothing else has to land for the beta. I am keeping this open to watch one backend timing edge case on the day boundary." | P1 DR2: the watched edge case is not a still-to-do. Commit `47c65623e7` (Sep 10), on main since Sep 15 |
| `cmt_zom521_2` | "Card pack animation went in with #475. I am leaving this item, ZOM-528 and ZOM-541 open until Brian has seen it in a build." | Eval 0 F1: base ZOM-541 "Cards Collect Vfx animation", In Progress, is the integration ticket for the same work (re-read) |
| the quest note `68dac8204f1e9a3b7c2d5e61` | "More quests get added with the Mon Oct 13 rollover if they are ready. The rollover does not wait on them, the current quests keep running either way." | Eval 0 F2: PNs Beta row 1 ("Revisit once new quests roll out") does wait on them, so "nothing in the beta" was too broad |
| `cmt_zom542_1` | "Picking this up after the bug list. The home screen and victory score changes for endless and boss arena are a layout refresh on screens that already work, so they are not needed for the beta." | P2 DR2: "not in the build yet / mockup stage" sat against the base state Regression. The ticket stays unstarted |
| `f_e4a17c90b3d25f6a8c1d73` Drive row | `web_view_link` `https://drive.google.com/file/d/1oIsTl3jQeyuTuqudrlGaxEze57_FtuiMHX72lDwtDSE/view` | P2 DR4: 11 of Julia's 12 owned sheets have one, in this form |
| `#472#rc_1` (new), mirror `65564543e4bc8dd707a177aada2337a3` (new), parent `61f686b8…` | Arthur, 2025-09-30T15:52:58Z, inline on `Assets/RewardVFXManager.cs` under his base APPROVED review `#472#rev_1`: "Fine for this PR. Separately, the Season Pass premium strip is still set to the October range. It needs the November range before that season opens, Oliver is taking the date change." The thread goes 3 to 4 replies and `latest_reply` stays at the base "merged" post | P2 DR1: a closed record with later activity always fails. Base #472 merged 2025-09-30T15:53:04Z, six seconds later; base holds `rev_1` and no inline comment on it (re-read). Same shape as `#470#rc_10`. #473 could not take a pre-merge note: it was open for 15 seconds |
| `#473#c_2`, `#473#ev_5`, the #473 PR bump, mirror `bd1a7d0a…`, the #473 card UPDATE | removed | the SQL names #473 nowhere any more |

Row count: 71 INSERT and 25 UPDATE, confirmed by `sql_lint` and by parsing the SQL. The floor is 70.

**What moving the note changes, as measured.** Nothing below was adjusted to keep a number up.

| | revision 7 | revision 8 |
|---|---|---|
| Evidence surfaces | 4 | **3** |
| Per-record surfaces (floor 75) | 135 | **96** (18 + 2 × 39) |
| Unconditional / planned calls (floor 130) | 193 / 203 | **154 / 164** |
| Cohort | 41 | 41 |
| Slots, weight, U | 30, 102, 0.8824 | same |
| Mechanism of `R_REVIEW_FLAGS`, T11 | A3, `tool_surface` | same id and family, weaker node |
| Forecast, design mode | E[avg] 0.614, P(all) 0.475 to 0.542 | same |
| Forecast, solver mode | E[avg] 0.808, P(all) 0.041 to 0.452 | same |

- **Call floor and per-record count.** `#473#c_2` was the only seeded row on the `github_get_issue_comments` surface. The 42
  base conversation comments on the 39 PRs are all bots (38 CodeRabbit, 4 Linear), so all 39 calls now return nothing a
  rule uses. The necessity rule (`Hardness_Mastery.md` §2.5) counts a surface only if it carries a fact the predicate uses,
  so the surface and its 39 budget calls are out. A careful run may still make those calls; they are no longer necessary.
- **Mechanism.** It stays A3: the note is still reached only through a per-PR call, and it now sits inside an empty-bodied
  APPROVED review, as `#470#rc_10` does. The node is weaker in one measured way. Through revision 7 T11 needed two call
  types (inline for the vials, conversation for the strip); one call type now returns both, plus the #470 note.
- **Likelihood of opening #472.** Seeded text names #472 once where a run can read it (`cmt_zom526_3`) and names #473 nowhere.
  Base Slack outside `#zombie-prs` names each once in September, in #builds. The design already reads #472 for T1, D10 and
  `R_INFRA_SCOPE`. Against that, a run hunting Season Pass work by title finds #473 ("Addressables/sp"), not #472
  ("Implement Win&Collect into Queue Manager"). A run that reads all 39 PRs meets the note either way.
- **Forecast.** It does not move, and that says nothing about difficulty: it prices each rule at its family prior, so it
  cannot see which record carries a note. Its fixed call count does not reach it either: solver mode reads the same at
  `--calls` 550, 193 and 154. I expect S09 to be easier than on revision 7 and S08 and S09 to fail or pass together more
  often. That is a judgement, not a measurement; only the baselines can settle it.

**Tool results on revision 8 on this machine** (2026-11-06; nothing below is pasted into a gate block):

- `sql_lint`: errors 0, warnings 8 (the Oct 8 plan event), 96 rows. `hg.py lint --sql`: FAIL 0.
- `base_check`: PASS with and without `--manifest` (71 inserts, 25 updates). `base_claims`: PASS.
- `fact_check --no-leak`: PASS, 8 declared facts. `check-sql`: PASS (29 YES, 8 NO, 6 UNVERIFIED, 53 unscoped rows).
- `oracle_kit check` against revision 7: PASS, 14 rules, regression byte for byte, 0 field differences. The solver also
  reproduces the revision-2 to revision-7 truths on their own SQLs.
- Mutation and trap liveness: every verdict and flag is the same as on revision 7 (50 and 20 dispositions; two reasons in
  `01c_Dispositions.json` re-worded for the new carrier). Surface validation: PASS.
- `hardness_gate`: `hazard_scope`, `cohort_size` and `evidence_surfaces` (3 surfaces over 2 services) pass; it fails only on
  the four lines that follow from `volume_exception.rows_floor` being unknown to this machine's tool.

**Open after revision 8, said plainly.**

1. The call budget has less margin: 154 against a floor of 130 and a per-record count of 96 against 75. Another lost
   surface would break the per-record floor, since each PR surface is 39.
2. Surface 2 and surface 3 now carry one and three seeded rows on 39 PRs. That is below the 15–40 % flip rate the necessity
   rule describes; surface 2 stands on the brief's change-request clause and surface 3 on the three notes it returns.
3. The quests and daily-gift rows carry almost no graded difficulty, and four of the fourteen rules are weak by their own
   records (`R_DONE_ELSEWHERE`, `R_WITHDRAWN`, `R_ICON_SCOPE`, and now `R_REVIEW_FLAGS`). The forecast prices them at family
   priors, which overstates them.
4. The solver-, manifest- and gate-bound lines in §4 and the pasted gate block are still revision-1 records.
### Revision 9 (after the platform's third /prompt failure)

The platform failed revision 8 on Unique Ground Truth and Clarity (`plateform_reports/6aea4c1e9b621f28dc3a5332_1_prompt-3.md`):
ZOM-534, Leonard's S23 freeze and #477 could each be read as a still-to-do. The root cause was that the brief's hold and
still-to-do rules were open sets. A census of every candidate is in `research/rev9_census/`, with the difficulty review in
`difficulty.md`; the local round on revision 8 is in `research/prompt_review_rev8/`. The transform is
`research/scripts/apply_review_fix_rev9.py` (pure text, asserted anchors; input sha256 `0e8c8ad83f3b`, output
`892f7edda809`, 76 INSERT and 28 UPDATE, 104 statements; a `grep` for lines gives 75 INSERT because line 82 holds a thread
and its message, as it did in revision 8). Revision 8 is archived in `run_forensics/rev8/`. The prompt is unchanged.
No graded value changes: `truth.json` is byte for byte the revision-8 file, evidence ids included.

**Brief rule text** (`f_7c3e91a4d2b85f60e1a9c4`, body 2,849 chars). The change-request sentence is untouched, word for word.

| Section | Through revision 8 | Revision 9 |
|---|---|---|
| Held or not | "An established failure holds it; an unverified build or platform is a still-to-do, not a hold." | "An established failure holds it; an unverified one does not." |
| Still to do | "For each beat, what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it. Not what already shipped, not analytics, not polish nobody flagged." | "For each beat, what still has to land before it runs for bought users and who owns it: a held beat's fix, and what has been flagged for that beat as not done since this brief (prod deploy, config or player-facing art). Nothing else goes in: not what already shipped, not analytics, not polish nobody flagged." |
| When a beat starts | "put down whether the beat is in and whether its push is ready, not its window dates." | "put down whether the beat is in, which weeks it runs and whether its push goes out, not its window dates." |
| When a beat starts | "A beat that is only waiting on that release starts late, it is not held." | "A beat whose server windows are waiting on that release starts late, it is not held." |
| When a beat starts, Span and time base | the cadence sat beside the release rule | "Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC." moves to the end of "Span and time base"; "A window the release instant pre-empts does not count." stays |
| Scope | "Not only the events everyone lists." | removed |
| Push copy | "names the game only as Zombie Match 3D and events only by their ZM3D names" | "names the game as Zombie Match 3D and events by their ZM3D names", so Frederick's thread reply alone decides the rows that name no game |

**The still-to-do rule is closed.** A cell holds a held beat's fix, plus what has been flagged for that beat as not done
since the brief (prod deploy, config or player-facing art). Nothing else goes in. Every value in `truth.json` already fits:

| Cell item | Kind | Record, and its date against the brief of Sep 24 |
|---|---|---|
| Weekly Leagues: the weekly reset fix (league owner) | a held beat's fix | `C0880U9751A/1759265412.481909`, Sep 30 |
| Collect & Win: the final vial models (Claire) | player-facing art | `#468#rc_38`, Sep 29 |
| Collect & Win: the event icon animation (Marcus) | player-facing art | `cmt_zom465_2`, Sep 30 |
| Collect & Win: server windows reach prod with the Oct 8 release | prod deploy | `#470#rc_10`, Sep 30 |
| Season Pass: premium strip to the November range (Oliver) | player-facing art | `#472#rc_1`, Sep 30 |
| Season Pass: the November config before Oct 31 00:00 UTC | config | `julia.lawson@harmonygames.co/1844311412966040123`, Sep 26 |

**New and re-worded records, with base grounding.** None is a deciding record: no graded cell reads one, and none enters
`DECIDING` in the solver. All grounding below was re-read in the exports for this revision.

| Record | Revision 9 | Base grounding |
|---|---|---|
| `fb870fca6646cf3c52a60796c5eec38a` (`C08R27X0EAH/1759182097.318279`), parent `ede90bc6…` | Leonard, 2025-09-29T21:41:37Z, a reply under his Sep 21 post: "Ran this again on an S23 Ultra from the remote device list, live Android build, a few endless runs with the airstrike. Could not get it to freeze, so I am leaving this one." No cause or fix is claimed | his DM of 2025-07-30T21:37:51Z (`D04UGG61DUM`): "This is galaxy s23 ultra - I downloaded from Netherlands play store and it looks good"; his own devices are not Samsung, so the remote list is his route to one |
| `cmt_zom534_1` (re-worded), `cmt_zom534_2` (new) | Douglas: "That went out in the client builds, so nothing else has to land for the beta. I am keeping this open to watch one timing edge case on the day boundary." Leonard, 2025-09-30T01:22:46Z: "Stayed online through the 00:00 UTC reset on the store build tonight. Quest points reset on their own, no restart. That was my report, it is good on prod now." | client commit `47c65623e7` (Oliver Brooks, 2025-09-10T23:53:35Z, "Using remaining-time endpoint to sync quests end with client"), listed in #builds iOS Submission #36 (2025-09-11T00:28Z) and Android Submission #119 (00:32Z). A client fix, so the Oct 8 backend release does not apply. Leonard's report opens the base ticket |
| `cmt_zom566_1` (now Brian's), `cmt_zom566_2` (Owen's, same text as before) | Brian, 2025-09-30T17:53:19Z, sequence 1: "Owen, analytics first. The header title and the info screen text can follow with it. The event runs fine with the current text, so they do not have to land before the beta." Owen's note moves to sequence 2 at 19:40:47Z | #zm-collect-win `C09EVVCFHKR`, Sep 30: Vincent 16:47:38Z "none of them blockers and doesn't affect the submission so it's up to you guys"; Brian 16:50:02Z "Analytics and name changes first". Base #477 is open at the clock (opened 22:26:30Z). Post-clock, Normal universe only: iOS 1.3.50 released 2025-10-01T15:21:00Z and #477 merged 2025-10-02T16:43:03Z, so the build with the event shipped without it. Nothing is seeded on #477 |
| `31b154fc2e29e457d9be80c60dfd8226` (`C08R27X0EAH/1759267492.604719`), parent `d0dd5d3a…` | Oliver, 2025-09-30T21:24:52Z: "Pushed the fix for the lightSweep on the box. It is only that sweep on the art, it goes out with the next build and nothing waits on it." | commit `25c6c66b6b` (Oliver Brooks, 2025-09-30T21:20:26Z) changes `…/Materials/Vfx/UI/lightSweep Box Variant.mat`. The thread had his "will work on this asap" at 17:41:38Z |
| `cmt_zom563_1` (new), `ZOM-563` (Done) | Vincent, 2025-09-30T22:04:33Z: "Checked on prod after the update: teams' lives, golden frames and names all work as expected. Closing." | DM `D079SNE2TL4`: Douglas 18:16:33Z "Ok, I updated the prod environment with the latest teams/social changes"; Vincent 21:58:44Z "Yep it works as expected". Julia cannot read that DM, so the ticket now carries it. ZOM-563 stays out of the cohort |
| the quest note `68dac8204f1e9a3b7c2d5e61` | "More quests and the reward balance go in with the Mon Oct 13 rollover if they are ready. The rollover does not wait on them, the current quests keep running either way." | the card is "Add more quests and balance quest rewards" |
| Brian's Sep 22 mail (three copies) | the contents are "reward tiers, the premium track and the season theme." | the spec page's "tiers, rewards, theme"; no quest table reads as a Quests still-to-do |
| Robert's withdrawal `669d15f685f158633e56302160957f1e` | "Coming back on the themed prop set I okayed in Martin's thread: pulling my ok." The rest is word for word | his approval says "one themed prop set only" |
| Pushes tab of `f_e4a17c90b3d25f6a8c1d73` | headers `Beat`, `Push name`, `Send (UTC or trigger)`, `Segment`, `English copy`, `Send or hold`, `What is missing` | what the task asks for |

**What the removed "unverified build or platform" clause took with it.** No `R_` rule and no `T` trap depended on it, so
none is retired: no rule reads brief words and mutation verdicts are unchanged. Its one graded consumer, the revision-1
Zombie Lane iOS cell, left in revision 2. What leaned on the wording is re-worded in place: K13's quote is now "An
established failure holds it"; D7 no longer says "a still-to-do at most"; the tail of D9's wrong reading (an iOS-verification
still-to-do) is gone; R3 is re-written; counter-reading rows 10 and 12 below have new overturning text.

**Renamed id, by meaning.** `cmt_zom566_1` was Owen's analytics note through revision 8 and is Brian's note now; every
reference that meant Owen's note now says `cmt_zom566_2`. The solver's `CMT_ZOM566` follows it. No evidence list cited either.

**Surface.** S04, S05 and C01 also accept "In". The Pushes table has key column `Push name` and columns `Send (UTC or
trigger)`, `Send or hold` and `What is missing`, and "Finish first tutorial" (the row's Details text on the base push
sheet) matches the key regex. The solver keeps its row label `What is missing (owner)`: no tool compares it with the
surface column, and renaming it would change `truth.json` and break `contract.regression` on the archived SQLs.

**Measured** (nothing was adjusted to hold a number):

| | revision 8 | revision 9 |
|---|---|---|
| Rows | 71 INSERT + 25 UPDATE | 76 INSERT + 28 UPDATE (floor 70) |
| Cohort | 41 | 41 |
| Per-record surfaces (floor 75) | 96 | 96 |
| Unconditional / planned calls (floor 130) | 154 / 164 | 154 / 164 |
| Slots, weight, U | 30, 102, 0.8824 | same |
| Forecast, design mode | E[avg] 0.614 [0.503, 0.722], P(all) 0.475 to 0.542 | same |
| Forecast, solver mode | E[avg] 0.808 [0.739, 0.876], P(all) 0.041 to 0.452 | same |

**The forecast does not see the three difficulty changes.** It prices each rule at its family prior from the ledger and
reads slot weights and mechanisms; record text reaches it only through which values the solver produces, and those did
not move. Measured directly: with every other input held and the revision-8 SQL swapped in, it reads the same. So its
silence is no evidence either way. The review's own figures for those three changes (about −1.8, −1.0 and −1.2 points on
the verifier) are judgement, not measurement; only the baselines can test them.

**Tool results on revision 9 on this machine** (2026-11-06; nothing below is pasted into a gate block):

- `sql_lint`: errors 0, warnings 8 (the Oct 8 plan event), 104 rows. `hg.py lint --sql`: FAIL 0.
- `base_check`: PASS with and without `--manifest` (76 inserts, 28 updates). `base_claims`: PASS.
- `fact_check --no-leak`: PASS, 8 declared facts, 5 warnings. One is new: the bare name "Martin" in Robert's withdrawal
  matches Martin Lewis and Martin Walsh; his approval sits in Martin Walsh's thread.
- `check-sql`: PASS (33 YES, 8 NO, 6 UNVERIFIED, 57 unscoped rows).
- `oracle_kit check` against revision 8: PASS, 14 rules, 0 field differences. The solver reproduces the revision-2 to
  revision-8 truths on their own SQLs.
- Mutation and trap liveness: every verdict and flag is the same as on revision 8 (50 and 20 dispositions; one reason in
  `01c_Dispositions.json` re-worded). `R_WITHDRAWN` is still KILLED on S02 and its intervention still load-bearing, so
  Halloween comes off through Robert's DM. Surface validation: PASS.
- `hardness_gate`: `hazard_scope`, `cohort_size` and the incorporation checks pass; it fails only on the four lines that
  follow from `volume_exception.rows_floor` being unknown to this machine's tool.

**Open after revision 9, said plainly.**

1. The call budget still has little margin (154 against 130, 96 against 75). The difficulty review expects real runs to
   make few inline calls, so 154 is a design floor, not a prediction.
2. Three of the difficulty review's points are unmeasured until a run exists: the pass rate, the spread and the calls.
3. Four of the fourteen rules remain weak by their own records (`R_DONE_ELSEWHERE`, `R_ICON_SCOPE`, `R_REVIEW_FLAGS`, and
   `R_WITHDRAWN`, though the de-naming makes that one harder to meet).
4. The solver-, manifest- and gate-bound lines in §4 and the pasted gate block are still revision-1 records.
### Revision 10 (after the pre-review attack on revision 9)

Six agents read the post-brief window in full and tested over 200 candidates (`research/rev9_attack/`, with
`coherence_attack.md` for the record-level findings). The transform is `research/scripts/apply_review_fix_rev10.py` (pure
text, asserted anchors; input sha256 `892f7edda809`, output `ffbac4586fb9`, 78 INSERT and 29 UPDATE, 107 statements; a
`grep` for lines gives 77 INSERT because line 82 holds a thread and its message). Revision 9 is archived in
`run_forensics/rev9/` without a truth file; its truth is byte for byte `run_forensics/rev8/truth.json`, which the regression
check uses. The prompt is unchanged.

**What changes in the answer key (deliberate, and the only value changes).** No evidence id moves.

| Cell | Revision 9 | Revision 10 | Basis |
|---|---|---|---|
| Weekly Leagues, Still to do | the weekly reset fix so a new week starts on prod (league owner) | … (Douglas) | ZOM-429's assignee in base |
| Collect & Win, Still to do | … server windows reach prod with the Oct 8 backend release | … with the Oct 8 backend release (Douglas) | organizer of the release event `evt_9a4c2e7f1b3d58e06c7a2f` |
| Quests, Weeks running | empty | All four weeks | the brief asks which weeks it runs; the Trello note says "weekly rollover" |
| Daily Login, Weeks running | empty | All four weeks | the brief asks; the gift resets daily, and its push row reads "Daily/Monthly Rollover" |

No slot reads these cells, so no accepted outcome changes for them. C05 also accepts "Starts late". The four cells follow a
revision marker in the solver (the brief's new still-to-do sentence), so the same rules still give every older truth on
its own SQL.

**Brief** (`f_7c3e91a4d2b85f60e1a9c4`, body 2,802 chars). The change-request sentence is untouched, word for word.

| Section | Revision 9 | Revision 10 |
|---|---|---|
| Still to do | "a held beat's fix, and what has been flagged for that beat as not done since this brief (prod deploy, config or player-facing art)." | "its fix if it is held, and anything flagged since this brief as still needed for it (prod deploy, config or player-facing art)." The old clause had a second parse, "that beat" could bind to "a held beat", and "as not done" let polish in |
| When a beat starts | "A window the release instant pre-empts does not count." | removed: "the first window that opens after" gives Fri Oct 10 by itself. No fragment quote used the sentence; R2's prose did and is re-written |
| Push copy | "and its English copy names the game" | "and the English copy on that row names the game", so the sheet row, not the client string, is what is judged |

The still-to-do items in the Revision 9 table all still fit: each is a held beat's fix or was flagged after Sep 24 as still needed.

**New, moved and re-worded records, with base grounding.** None is a deciding record. All grounding below was re-read in the exports.

| Record | Revision 10 | Base grounding |
|---|---|---|
| `cmt_zom565_2` (new), `ZOM-565` `updated_at` | Brian, 2025-09-30T16:12:27Z, sequence 2: "Marcus, the endless VFX inside the core game and the refill timer are the same P1/P2 polish from my list. Endless runs fine without them, so they can follow and do not have to land before the beta." | Brian's P1/P2 list in #zm-animations, Sep 12. The work did not stop: base ZOM-567 "Endless Mode Core game Vfx" opens 2025-10-01T12:26:53Z (Normal universe, post-clock). Three audits flagged this as the one record meeting every limb of the rule |
| `532747cb5d123a95d13204e57b5a7a38` (`C08R8CHB0QL/1759250468.275139`, new), parent `a3e78e82…` | Robert, 2025-09-30T16:41:08Z, in Martin's desert thread: "Both look good, the desert and the port. Keep them as options, Endless runs with what it has now and nothing waits on new themes." The parent goes 3 to 4 replies and 3 to 4 reply users | Martin's base post of 2025-09-29T15:30:49Z ("I'm preparing a *desert theme* for the *Endless Mode*"), which tags Robert. The reply does not say the themes are out of the beta |
| `a08ff7cbfc52008d7dee8457e9385a3c` (`C08R27X0EAH/1759268775.482369`), replaces Oliver's `31b154fc…` | Vincent, 2025-09-30T21:46:15Z: "Oliver pushed the lightSweep fix. It only changes how the box looks, the box opens the same with or without it, so it rides the next build and nothing has to land for the beta." | he raised the thread at 16:24:48Z, so it is closed by the reporter, not by the fixer's own word; commit `25c6c66b6b` changes the material at 21:20:26Z |
| `e343557b2e94a1701251ebd079e6f0ce` (`C08R27X0EAH/1759187861.318279`), replaces `fb870fca…` | Leonard, 2025-09-29T23:17:41Z: "Ran this again on an S23 Ultra in the cloud device farm, live Android build, a few endless runs with the airstrike. Could not get it to freeze, so I am leaving this one." | he cancelled BrowserStack on 2025-08-07T22:32:40Z, so "remote device list" had no base support; `page_qa_runbook`, which Julia can read, says "a small physical lab plus a cloud device farm". The move takes it out of his VC call |
| `cmt_zom566_1` | "Owen, analytics and the name changes are first on the list, but none of it is a blocker. The event runs fine with the current text, so the header title and the info screen text do not have to land before the beta." | his own line 63 minutes earlier, "Analytics and name changes first", and Vincent's "none of them blockers" (#zm-collect-win, Sep 30) |
| `cmt_zom534_2` | moves to 2025-09-30T01:09:52Z, with the ZOM-534 `updated_at` | clear of his live DM of 01:14:46Z on; still "tonight" in Pacific time |
| `cmt_zom563_1` | "Checked on prod after Douglas's teams update: teams' lives, golden frames and names all work as expected. Closing." | Douglas's DM of 18:16:33Z, so it cannot be read as the Oct 8 backend release |
| the quest note `68dac8204f1e9a3b7c2d5e61` | "More quests and the reward balance go in with the Mon Oct 13 rollover if they are ready. The weekly rollover does not wait on them, the current quests keep running either way." | the weekly quest reset (Monday 00:00 UTC) in `match3d-quests`; gives "which weeks it runs" a record |

**Measured** (nothing was adjusted to hold a number):

| | revision 9 | revision 10 |
|---|---|---|
| Rows | 76 INSERT + 28 UPDATE | 78 INSERT + 29 UPDATE (floor 70) |
| Cohort | 41 | 41 |
| Per-record surfaces (floor 75) | 96 | 96 |
| Unconditional / planned calls (floor 130) | 154 / 164 | 154 / 164 |
| Slots, weight, U | 30, 102, 0.8824 | same |
| Forecast, design mode | E[avg] 0.614 [0.503, 0.722], P(all) 0.475 to 0.542 | same |
| Forecast, solver mode | E[avg] 0.808 [0.739, 0.876], P(all) 0.041 to 0.452 | same |

The forecast is unchanged for the reason given in Revision 9: it reads family priors and slots, and no slot reads the four
changed cells.

**Tool results on revision 10 on this machine** (2026-11-06; nothing below is pasted into a gate block):

- `sql_lint`: errors 0, warnings 8 (the Oct 8 plan event), 107 rows. `hg.py lint --sql`: FAIL 0.
- `base_check`: PASS with and without `--manifest` (78 inserts, 29 updates). `base_claims`: PASS.
- `fact_check --no-leak`: PASS, 8 declared facts, 5 warnings, the same five as revision 9.
- `check-sql`: PASS (35 YES, 8 NO, 6 UNVERIFIED, 58 unscoped rows).
- `oracle_kit check` against revision 9: PASS, 14 rules, 0 field differences. The solver reproduces the revision-2 to
  revision-9 truths on their own SQLs.
- Mutation and trap liveness: every verdict and flag is the same as on revision 9 (50 and 20 dispositions). Surface
  validation: PASS.
- `hardness_gate`: `hazard_scope`, `cohort_size` and the incorporation checks pass; it fails only on the four lines that
  follow from `volume_exception.rows_floor` being unknown to this machine's tool.

**Open after revision 10, said plainly.**

1. 9 of the 39 read PRs merged before Aug 1, outside the brief's Aug-Sep cohort. If the two per-PR surfaces counted only
   Aug-Sep PRs, the per-record count would be 78 and the budget 136, both still above their floors with little margin.
2. Pass rate, spread and calls stay unmeasured until a run exists.
3. The solver-, manifest- and gate-bound lines in §4 and the pasted gate block are still revision-1 records.
### Revision 11 (after the formal blind round on revision 10)

Three independent P1 passes, two P2 passes, a P3 and a P4 pass, the main `/prompt` draft and an Eval 0 run reviewed revision 10
(`research/prompt_review_rev10/`). The transform is `research/scripts/apply_review_fix_rev11.py` (pure text, asserted anchors;
input sha256 `ffbac4586fb9`, output `1348d287ac4a`, 80 INSERT and 30 UPDATE, 110 statements; a `grep` for lines gives 79
INSERT because line 90 holds a thread and its message). Revision 10 is archived in
`run_forensics/rev10/` with its truth, and `run_forensics/rev9/` now holds a truth copy too. The prompt is unchanged.

**What changes in the answer key.** No value changes: all 17 keys carry the revision-10 values, and Season Pass's First window
stays empty, because no slot reads it. One evidence id is added and no other moves: `cmt_zom465_3` on the Collect & Win row,
through `NOTE_ICON_NEEDED` in the solver. On an older SQL that tuple resolves to Marcus's note and the repeat is dropped, so
the solver still gives the revision-2 to revision-10 truths byte for byte on their own SQLs.

**Brief** (`f_7c3e91a4d2b85f60e1a9c4`, body 2,992 chars; the style runs follow). The change-request sentence is untouched.

| Section | Revision 10 | Revision 11 |
|---|---|---|
| Span and time base | no rule for what starts before or runs past the span | "Clip anything that starts before or runs past that to those two instants." So the October season starts Mon Oct 6 00:00 UTC on the calendar and the November season ends Sun Nov 2 23:59 UTC |
| Span and time base | "each opening 00:00 UTC." | "each opening 00:00 UTC and closing 23:59 UTC on its last day." |
| When a beat starts | "the daily gift (the Login Calendar row on the push sheet)" | "the daily gift (Login Calendar on the push sheet, same beat)", so "login calendar" on the push copy is not a wrong name |
| Held or not | no rule for a held beat's window cells | "A held beat keeps its usual windows on its row, marked held." |
| Config locks | "moves earlier and its owner is told" | "moves to any time before it and its owner is told", which states the acceptance boundary |

These close the review's both-fair window figures. None of them moves a truth value, because no truth cell holds those figures.

**New and re-worded records, with base grounding.** All grounding below was re-read in the exports.

| Record | Revision 11 | Base grounding |
|---|---|---|
| `cmt_zom465_3` (new, DEC), `ZOM-465` `updated_at` | Brian, 2025-09-30T18:13:41Z, sequence 3: "Marcus, the Collect & Win icon does have to land before the beta, it is the one event icon with no animation. Keep it on this ticket, the master VFX list was written before that event came in." | The master VFX list is `ZOM-521` ("Master Ticket - VFX implementation"), which Brian created on 2025-09-02T19:48:09Z and whose base line "Live-ops icons appearing on the screen and animations on these icons" stays ticked. His Sep 12 priority list for Marcus in #zm-animations reads "P0 – Collect & Win → may need your help later, but not clear yet"; #zm-collect-win opens on Sep 15. ZOM-465's creator in base is Vincent and its assignee Marcus. Brian has no Slack line from 17:49:11Z to 19:30Z |
| `7d70c7753179c98b6c8b2b5457a1e5e7` (`C09EVVCFHKR/1758903764.713429`, new), parent `0069f614…` | Douglas, 2025-09-26T16:22:44Z, in #zm-collect-win: "Both tables are updated." It decides no value | Brian's request of 15:10:00Z names Douglas ("Could you update them?") and had no reply. The parent goes from 2 replies by 1 user to 3 by 2. Douglas is a channel member, and his nearest line is 16:06:51Z in #company-internal. Julia is not a member, so `check-sql` reads the row and its parent UNVERIFIED; no cell rests on either |
| `ZOM-542` | `state_id` Todo (was base Regression), `updated_at` unchanged | base `started_at` is NULL, and `cmt_zom542_1` says the work is still to pick up. Todo is still open, so the ticket stays in the cohort |
| `#472#rc_1` and its mirror `65564543…` | "the Season Pass premium strip art still shows the October range." | a date range in code leaves no trace, because the sprites are LFS pointers; the note now speaks of the art |
| `669d15f6…`, `933cee9f…` | The withdrawal ends at "Sorry for the flip."; the approval reads "for one week of the beta" and "if it lands in time" | Robert cannot see the brief, and no record had coined "beta weeks" or "the cut". The brief's own one-off rule says his later word counts |
| `f_2b9d4e7a1c63f08d5e7b21` | Slide 1: "Beta-cohort buy, starting once the stores approve the Sep 30 builds."; slide 2: "Small scale at first, any scale-up comes after the pivot call." | slides 1 and 2 now agree with slide 3 |
| `68dac8204f1e9a3b7c2d5e61` | The payload has `board`, `card` and `text` only: no `list`, `idCard` or `textData`. The note's words are unchanged | One base commentCard has exactly this shape; 54 of 56 carry `list`. The base list is "BETA: Oct 10", so the payload no longer repeats the SC-13 name mismatch |
| `890dc27f…`, `cmt_zom504_1`, `a08ff7cb…`, `cmt_zom563_1` | "Two things on top of the brief."; "Re-tested: it only shows up with the bot running;"; "so it rides the next store build"; "Checked on prod: teams' lives, golden frames and names all work as expected. Closing." | wording only. ZOM-563 no longer names Douglas's prod update, which was a route to arguing the Collect & Win windows shipped early |

**The Trello payload and the tools.** No tool reads the payload's `list` or `idCard`. `base_check`, `base_claims` and
`hardness_v2_check` read `idCard` from the row's own column, which is unchanged; `base_claims` reads `card.desc`, `text` and
`old.desc` with safe lookups; `fact_check`, `trap_liveness`, `node_verdicts` and `trajectory_ledger` read the payload as text;
the solver's `_body` reads the whole `data_json`, so `NOT_WAITING` still finds its words.

**Measured** (nothing was adjusted to hold a number):

| | revision 10 | revision 11 |
|---|---|---|
| Rows | 78 INSERT + 29 UPDATE | 80 INSERT + 30 UPDATE (floor 70) |
| Cohort | 41 | 41 |
| Per-record surfaces (floor 75) | 96 | 96 |
| Unconditional / planned calls (floor 130) | 154 / 164 | 154 / 164 |
| Slots, weight, U | 30, 102, 0.8824 | same |
| Seeded ids under persona reach | 45 | 46 |
| Forecast, design mode | E[avg] 0.614 [0.503, 0.722], P(all) 0.475 to 0.542 | same |
| Forecast, solver mode | E[avg] 0.808 [0.739, 0.876], P(all) 0.041 to 0.452 | same |

The forecast is unchanged for the reason given in Revision 9: it reads family priors and slots, and no slot changed.

**Tool results on revision 11 on this machine** (2026-11-06; nothing below is pasted into a gate block):

- `sql_lint`: errors 0, warnings 8 (the Oct 8 plan event), 110 rows. `hg.py lint --sql`: FAIL 0.
- `base_check`: PASS with and without `--manifest` (80 inserts, 30 updates). `base_claims`: PASS.
- `fact_check --no-leak`: PASS, 8 declared facts, 5 warnings, the same five as revision 10.
- `check-sql`: PASS (35 YES, 8 NO, 8 UNVERIFIED, 59 unscoped rows). The two new UNVERIFIED rows are Douglas's reply and its parent.
- `oracle_kit check` against revision 10: PASS, 14 rules, 0 field differences.
- Mutation and trap liveness: every verdict and flag is the same as on revision 10 (50 and 20 dispositions). Surface
  validation: PASS.
- `hardness_gate`: `hazard_scope`, `cohort_size` and the incorporation checks pass; it fails only on the four lines that
  follow from `volume_exception.rows_floor` being unknown to this machine's tool.

**Open after revision 11, said plainly.**

1. 9 of the 39 read PRs merged before Aug 1, outside the brief's Aug-Sep cohort. If the two per-PR surfaces counted only
   Aug-Sep PRs, the per-record count would be 78 and the budget 136, both still above their floors with little margin.
2. Brian's "the master VFX list was written before that event came in" holds for the VFX work: `ZOM-521` is dated Sep 2, his
   Sep 12 list still has Collect & Win "not clear yet", and its channel opens Sep 15. Base also has PR #370 "Collect&Win
   Items", opened Aug 8, and older Slack mentions of the event, so a reader could take "came in" more narrowly.
3. Pass rate, spread and calls stay unmeasured until a run exists.
4. The solver-, manifest- and gate-bound lines in §4 and the pasted gate block are still revision-1 records.
### Revision 12 (after the verification round on revision 11)

Eval 0 passed revision 11, P3 and P4 were clean, and the P1 and P2 samples converged on a short list
(`research/prompt_review_rev11/`). The transform is `research/scripts/apply_review_fix_rev12.py` (pure text, asserted anchors;
input sha256 `1348d287ac4a`, output `b5ccbfa577fc`, 81 INSERT and 30 UPDATE, 111 statements; a `grep` for lines gives 80
INSERT because line 90 holds a thread and its message). Revision 11 is archived in `run_forensics/rev11/` with its truth. The
prompt is unchanged.

**What changes in the answer key (deliberate, and the only value changes).** No evidence id moves.

| Cell | Revision 11 | Revision 12 | Basis |
|---|---|---|---|
| Weekly Leagues, First window (UTC) | empty | Mon Oct 6 00:00 UTC | "A held beat keeps its usual windows and weeks on its row, marked held."; the league week opens Monday 00:00 UTC |
| Weekly Leagues, Weeks running | empty | All four weeks | the same sentence. The row's Status, Held, is the mark, so neither cell carries extra text |
| Season Pass, First window (UTC) | empty | Mon Oct 6 00:00 UTC | the October season opened Oct 1 and is running (`#470#rc_10`), and the clip sentence holds it to the span's start |

No slot reads these cells, so no accepted outcome on the surface changes. No rule decides them, so they carry no rule gate and
add no evidence. They follow a revision marker in the solver (the held-row sentence's new words), so the same rules still give
the revision-2 to revision-11 truths byte for byte on their own SQLs.

**Brief** (`f_7c3e91a4d2b85f60e1a9c4`, body 3,090 chars; the style runs follow). The change-request sentence is untouched.

| Section | Revision 11 | Revision 12 |
|---|---|---|
| Span and time base | "closing 23:59 UTC on its last day" on Collect & Win only | "Every window is stated in server time (UTC) as a start-end instant, closing 23:59 UTC on its last day."; Collect & Win's sentence ends at "each opening 00:00 UTC." |
| Scope | "Boss Arena is off this calendar until the pivot call." | "..., and the shop rotation is not a beat." |
| Held or not | "keeps its usual windows on its row" | "keeps its usual windows and weeks on its row" |
| Push copy | "events by their ZM3D names. Anything else is held, with what is missing." | "events by their ZM3D names (Login Calendar and Weekly Rankings are fine). Anything else is held, with what its row is missing." |

**New and re-worded records, with base grounding.** All grounding below was re-read in the exports.

| Record | Revision 12 | Base grounding |
|---|---|---|
| `cmt_zom563_1` (now Douglas's), `cmt_zom563_2` (Vincent's, same text as before) | Douglas, 2025-09-30T18:17:05Z, sequence 1: "Prod has the teams and social changes now. That update carried only these, the Collect & Win server windows wait for the Oct 8 release." Vincent, 22:04:33Z, sequence 2 | Douglas is ZOM-563's assignee. His DM of 18:16:33Z says "Ok, I updated the prod environment with the latest teams/social changes", 32 seconds earlier, and he has no other Slack line from 17:30Z to 19:00Z. The ticket still closes on Vincent's note. It stays out of the cohort |
| `#468#rc_38` and its mirror `78aa8ed7…` | "The final vial models are missing and need to be in before the beta, Claire has those on her list." | same record and time; it now says it is needed, as the icon note does |
| `cmt_zom465_3` | "Keep it on this ticket, the master VFX list was ticked before that event merged." | `ZOM-521`'s base `updated_at` is 2025-09-17T15:50:49Z and #468 "Collect And Win" merged 2025-09-29T16:13:50Z. This replaces "written before that event came in", which base's August Collect & Win work made loose (Revision 11, open item 2) |
| `68dac8204f1e9a3b7c2d5e61` | The payload has `board`, `card`, `idCard`, `text` and `textData`, and no `list`. The note's words are unchanged | All 12 comments on this board carry `idCard` and `textData`, so the row matches them there. They also carry `list`, so no base row has this exact key set; leaving it out keeps the SC-13 name mismatch out of the SQL |

**The Trello payload and the tools.** As in Revision 11, no tool reads the payload's `list`, and `idCard` is read from the
row's own column. The checks below ran on this payload.

**Measured** (nothing was adjusted to hold a number):

| | revision 11 | revision 12 |
|---|---|---|
| Rows | 80 INSERT + 30 UPDATE | 81 INSERT + 30 UPDATE (floor 70) |
| Cohort | 41 | 41 |
| Per-record surfaces (floor 75) | 96 | 96 |
| Unconditional / planned calls (floor 130) | 154 / 164 | 154 / 164 |
| Slots, weight, U | 30, 102, 0.8824 | same |
| Seeded ids under persona reach | 46 | 46 |
| Forecast, design mode | E[avg] 0.614 [0.503, 0.722], P(all) 0.475 to 0.542 | same |
| Forecast, solver mode | E[avg] 0.808 [0.739, 0.876], P(all) 0.041 to 0.452 | same |

The forecast is unchanged for the reason given in Revision 9: it reads family priors and slots, and no slot changed.

**Tool results on revision 12 on this machine** (2026-11-06; nothing below is pasted into a gate block):

- `sql_lint`: errors 0, warnings 8 (the Oct 8 plan event), 111 rows. `hg.py lint --sql`: FAIL 0.
- `base_check`: PASS with and without `--manifest` (81 inserts, 30 updates). `base_claims`: PASS.
- `fact_check --no-leak`: PASS, 8 declared facts, 5 warnings, the same five as revision 11.
- `check-sql`: PASS (35 YES, 8 NO, 8 UNVERIFIED, 60 unscoped rows).
- `oracle_kit check` against revision 11: PASS, 14 rules, 0 field differences.
- Mutation and trap liveness: every verdict and flag is the same as on revision 11 (50 and 20 dispositions). Surface
  validation: PASS.
- `hardness_gate`: `hazard_scope`, `cohort_size` and the incorporation checks pass; it fails only on the four lines that
  follow from `volume_exception.rows_floor` being unknown to this machine's tool.

**Open after revision 12, said plainly.**

1. 9 of the 39 read PRs merged before Aug 1, outside the brief's Aug-Sep cohort. If the two per-PR surfaces counted only
   Aug-Sep PRs, the per-record count would be 78 and the budget 136, both still above their floors with little margin.
2. `cmt_zom563_1` supports Collect & Win's first window, but it is not in that row's evidence: revision 12 moves no evidence
   id, and ZOM-563 is outside the per-issue surface.
3. Pass rate, spread and calls stay unmeasured until a run exists.
4. The solver-, manifest- and gate-bound lines in §4 and the pasted gate block are still revision-1 records.
### Revision 13 (after the cold reviewers' last items on revision 12)

P1d and P1f found no open fork, and P1c, P2c, P3, P4 and Eval 0 were clean or advisory (`research/prompt_review_rev12/`). The
transform is `research/scripts/apply_review_fix_rev13.py` (pure text, asserted anchors; input sha256 `b5ccbfa577fc`, output
`1f2175a297fd`, 81 INSERT and 30 UPDATE, 111 statements; a `grep` for lines gives 80 INSERT because line 90 holds a thread and
its message). Revision 12 is archived in `run_forensics/rev12/` with its truth. The prompt is unchanged.

**What changes in the answer key.** Nothing: `solver/truth.json` is byte for byte the revision-12 file, and no rule, value or
evidence id moves. Two things follow the vial note's new words. The solver's `VIAL_WORDS` gains "final models", so the cell stays
"the final vial models (Claire)" by the note's own words rather than by the fallback. The fact `cw.todo.vials` takes the value
"final models": without that, `fact_check` fails on both copies of the note. An alias would pass too, but it would leave the
declared value in no record, so the leak check would test nothing.

**Brief** (`f_7c3e91a4d2b85f60e1a9c4`, body 3,100 chars; the style runs follow). The change-request sentence is untouched.

| Section | Revision 12 | Revision 13 |
|---|---|---|
| Scope | "and the shop rotation is not a beat." | "and the rotating shop is not a beat.", the company's term |
| Push copy | "Anything else is held, with what its row is missing." | "Anything else is held, with which of those its row is missing.", so a row's Details note is not part of that cell |

**Re-worded records.** No record is new.

| Record | Revision 13 | Why |
|---|---|---|
| `#468#rc_38` and its mirror `78aa8ed7…` | "The Collect & Win vials that spawn in the levels still need their final models before the event runs. Not a blocker for this PR, Claire has those on her list." | P2d: the repo holds a model Claire revised in August, so "first-pass" did not fit. Eval 0 ADV-22: the Sep 30 builds were already out, so "before the beta" sat badly. P1d B1: "Not a blocker for this PR" removes the change-request reading |
| `cmt_zom465_3` | "Marcus, the Collect & Win icon does have to land before the event runs, it is the one event icon with no animation." | the same reason as ADV-22. The rest of the note is unchanged |
| `68dac8204f1e9a3b7c2d5e61` | The payload's `list` key is back: id `6851a674975da1fe76e70d93`, name "BETA: Sep 30". The note's words are unchanged | 14 base commentCards have exactly this key set, and 63 base actions carry this list id with this name. The list record itself reads "BETA: Oct 10", the base SC-13 mismatch, which the transform records as not scored |

**The Trello payload and the tools.** No tool reads the payload's `list`, and `idCard` is read from the row's own column. The
checks below ran on this payload.

**Measured** (nothing was adjusted to hold a number):

| | revision 12 | revision 13 |
|---|---|---|
| Rows | 81 INSERT + 30 UPDATE | same (floor 70) |
| Cohort | 41 | 41 |
| Per-record surfaces (floor 75) | 96 | 96 |
| Unconditional / planned calls (floor 130) | 154 / 164 | 154 / 164 |
| Slots, weight, U | 30, 102, 0.8824 | same |
| Seeded ids under persona reach | 46 | 46 |
| Forecast, design mode | E[avg] 0.614 [0.503, 0.722], P(all) 0.475 to 0.542 | same |
| Forecast, solver mode | E[avg] 0.808 [0.739, 0.876], P(all) 0.041 to 0.452 | same |

The forecast is unchanged for the reason given in Revision 9: it reads family priors and slots, and no slot changed.

**Tool results on revision 13 on this machine** (2026-11-06; nothing below is pasted into a gate block):

- `sql_lint`: errors 0, warnings 8 (the Oct 8 plan event), 111 rows. `hg.py lint --sql`: FAIL 0.
- `base_check`: PASS with and without `--manifest` (81 inserts, 30 updates). `base_claims`: PASS.
- `fact_check --no-leak`: PASS, 8 declared facts, 5 warnings, the same five as revision 12.
- `check-sql`: PASS (35 YES, 8 NO, 8 UNVERIFIED, 60 unscoped rows).
- `oracle_kit check` against revision 12: PASS, 14 rules, 0 field differences. The solver reproduces the revision-2 to
  revision-12 truths on their own SQLs.
- Mutation and trap liveness: every verdict and flag is the same as on revision 12 (50 and 20 dispositions). Surface
  validation: PASS.
- `hardness_gate`: `hazard_scope`, `cohort_size` and the incorporation checks pass; it fails only on the four lines that
  follow from `volume_exception.rows_floor` being unknown to this machine's tool.

**Open after revision 13, said plainly.**

1. 9 of the 39 read PRs merged before Aug 1, outside the brief's Aug-Sep cohort. If the two per-PR surfaces counted only
   Aug-Sep PRs, the per-record count would be 78 and the budget 136, both still above their floors with little margin.
2. Pass rate, spread and calls stay unmeasured until a run exists.
3. The solver-, manifest- and gate-bound lines in §4 and the pasted gate block are still revision-1 records.
### Revision 14 (after the last cold P1 on revision 13)

P2e found no fail-level and no low-impact item, Eval 0 passed, and the last cold P1 left two items
(`research/prompt_review_rev13/`). The transform is `research/scripts/apply_review_fix_rev14.py` (pure text, asserted anchors;
input sha256 `1f2175a297fd`, output `edae63f3e838`, 81 INSERT and 30 UPDATE, 111 statements; a `grep` for lines gives 80 INSERT
because line 90 holds a thread and its message). Revision 13 is archived in `run_forensics/rev13/` with its truth. The prompt
is unchanged.

**What changes in the answer key.** Nothing: `solver/truth.json` is byte for byte the revision-13 file, and no rule, value or
evidence id moves. No rule reads either sentence.

**Brief** (`f_7c3e91a4d2b85f60e1a9c4`, body 3,170 chars; the style runs follow). The change-request sentence is untouched.

| Section | Revision 13 | Revision 14 |
|---|---|---|
| Config locks | "moves to any time before it and its owner is told in a reply on the mail where they committed to it." | "moves to any time before it and you tell its owner in a reply on the mail where they committed to it.", so the reply to Brian is plainly Julia's job |
| Span and time base | Collect & Win's sentence ended the section | adds "Endless goes down as its weekly windows, with the daily reset noted.", which says which cadence goes in the Windows cell |

**Measured** (nothing was adjusted to hold a number):

| | revision 13 | revision 14 |
|---|---|---|
| Rows | 81 INSERT + 30 UPDATE | same (floor 70) |
| Cohort | 41 | 41 |
| Per-record surfaces (floor 75) | 96 | 96 |
| Unconditional / planned calls (floor 130) | 154 / 164 | 154 / 164 |
| Slots, weight, U | 30, 102, 0.8824 | same |
| Seeded ids under persona reach | 46 | 46 |
| Forecast, design mode | E[avg] 0.614 [0.503, 0.722], P(all) 0.475 to 0.542 | same |
| Forecast, solver mode | E[avg] 0.808 [0.739, 0.876], P(all) 0.041 to 0.452 | same |

**Tool results on revision 14 on this machine** (2026-11-06; nothing below is pasted into a gate block):

- `sql_lint`: errors 0, warnings 8 (the Oct 8 plan event), 111 rows. `hg.py lint --sql`: FAIL 0.
- `base_check`: PASS with and without `--manifest` (81 inserts, 30 updates). `base_claims`: PASS.
- `fact_check --no-leak`: PASS, 8 declared facts, 5 warnings, the same five as revision 13.
- `check-sql`: PASS (35 YES, 8 NO, 8 UNVERIFIED, 60 unscoped rows).
- `oracle_kit check` against revision 13: PASS, 14 rules, 0 field differences. The solver reproduces the revision-2 to
  revision-13 truths on their own SQLs.
- Mutation and trap liveness: every verdict and flag is the same as on revision 13 (50 and 20 dispositions). Surface
  validation: PASS.
- `hardness_gate`: `hazard_scope`, `cohort_size` and the incorporation checks pass; it fails only on the four lines that
  follow from `volume_exception.rows_floor` being unknown to this machine's tool.

**Open after revision 14, said plainly.**

1. 9 of the 39 read PRs merged before Aug 1, outside the brief's Aug-Sep cohort. If the two per-PR surfaces counted only
   Aug-Sep PRs, the per-record count would be 78 and the budget 136, both still above their floors with little margin.
2. The brief now gives Endless's cadence, but its First window and Weeks running cells stay empty in `solver/truth.json`, as
   this revision moves no value. No slot reads them.
3. Pass rate, spread and calls stay unmeasured until a run exists.
4. The solver-, manifest- and gate-bound lines in §4 and the pasted gate block are still revision-1 records.
## 12 Self-review

**Checks A–C walk** (`base_check` + platform `/injection`; `base_check` re-walked on revision 14; the platform
`/injection` passed revision 2 on 2026-11-05, `plateform_reports/6aea4c1e9b621f28dc3a5332_0_injection-2.md`,
independent Eval 0 runs reviewed revision 3 (`research/prompt_review_rev3/0_injection.md`) and revision 4
(`research/prompt_review_rev4/0_injection.md`), revision 5 (`research/prompt_review_rev5/0_injection.md`) and revision 6
(`research/prompt_review_rev6/0_injection.md`) revision 7 (`research/prompt_review_rev7/0_injection.md`) and revision 8
(`research/prompt_review_rev8/0_injection.md`), revision 10 (`research/prompt_review_rev10/0_injection.md`), revision 11 (`research/prompt_review_rev11/0_injection.md`), revision 12 (`research/prompt_review_rev12/0_injection.md`), revision 13 (`research/prompt_review_rev13/0_injection.md`), and the run on revision 14 is under way), every statement in
`01_Universe_Inject.sql` (81 INSERT, 30 UPDATE; no DELETE/upsert): **Check A** (records, references, ids) PASS — every
actor, channel, parent, PR, review, Linear issue/user, Drive parent and Trello card/board/list/member resolves; every
new id unique on a complete scan. **Check B** (structure/schema) PASS — columns/values match; no omitted NOT NULL; no
generated column written; Linear dates `YYYY-MM-DDTHH:MM:SSZ`, with seconds since revision 5. **Check C**
(dates/relationships) PASS — all event timestamps ≤ the clock except the Oct 8 gcal plan event (future, allowed); reply
counts and parent/child order correct (the thread reply `D05SD5QLG94/1759263878.305129` is dated 2025-09-30T20:24:38Z,
after its root at 20:20:17Z, and the root carries `reply_count` 1); supersession chronology strictly increasing (T1
`JULIA_NOTES` 09-22 → `evt` 09-26 → `#468` 09-26 → `#470#rc_10` 09-30; T7 `cmt_zom429_1` 09-16 → the Sep 22 thread end →
the re-test 09-30). `cmt_zom526_2` (2025-09-26T15:40:50Z) follows `cmt_zom526_1` (2025-09-24T17:30:35Z) on the same
issue, and `cmt_zom526_3` (2025-09-30T16:24:19Z) follows both and PR #472's merge (15:53:04Z); the `ZOM-526` `updated_at`
equals it. `cmt_zom521_2` (2025-09-30T16:27:38Z) follows `cmt_zom521_1` (2025-09-26T17:25:02Z) and PR #475's merge
(16:09:15Z), and the `ZOM-521` `updated_at` equals it. `#468#rev_3` and `#468#rc_38` are dated 2025-09-29T15:36:41Z, inside #468's open window (opened
2025-09-26T20:16:25Z, merged 2025-09-29T16:13:50Z); `#470#rc_10` carries the instant of the base approval review it
belongs to (2025-09-30T15:51:06Z, nine seconds before the merge); `#472#rc_1` likewise carries the instant of its base approval (2025-09-30T15:52:58Z, six seconds before
the merge); `cmt_zom465_2` (2025-09-30T18:05:02Z) follows `cmt_zom465_1`
(2025-09-26T18:10:01Z) and `cmt_zom465_3` (2025-09-30T18:13:41Z) follows it; `cmt_zom432_2` (2025-09-30T21:07:26Z) follows `cmt_zom432_1` (2025-09-24T16:10:28Z), and each
Done ticket's `completed_at` equals its `updated_at` and its closing note's time (ZOM-344, ZOM-432, ZOM-563); `cmt_zom563_2` (2025-09-30T22:04:33Z) follows `cmt_zom563_1` (2025-09-30T18:17:05Z); `cmt_zom534_2`
(2025-09-30T01:09:52Z) follows `cmt_zom534_1`; `cmt_zom565_2` (2025-09-30T16:12:27Z) follows `cmt_zom565_1`; `cmt_zom566_1`
(17:53:19Z) precedes `cmt_zom566_2` (19:40:47Z); the three seeded replies follow their parents and carry ts ending in 9; the retraction has no parent, so no reply counter is involved.

**Touched-data census**: §10; hazards cited per category there; L03 (`ZOM-387`) is neither modified nor cited since
revision 6, so no acknowledgement applies; S04 no longer touched, GCal `no_notify` declared; known-issue card SC-15
repaired in revision 3 and not graded.

**Counter-readings** (category · the strongest wrong reading it would FAIL · the record that overturns it · verdict):

| # | Category | Counter-reading (strongest wrong reading) | Overturning record | Verdict |
|---|---|---|---|---|
| 1 | temporal | C&W starts week 1 because its PRs merged before the cut | `evt_9a4c2e7f1b3d58e06c7a2f` (Oct 8 15:00Z) + `#470#rc_10` | Fri Oct 10 00:00 UTC |
| 2 | temporal | Brian's Oct 31 10:00 Istanbul is on time before Nov 1 | `page_season_pass_spec` 24h lock + `…/1844311412966040123` (07:00Z = 7h late) | before Oct 31 00:00 UTC |
| 3 | quantitative | the lock is Nov 1 00:00 UTC | base `page_season_pass_spec` "locked 24h before each season opens" + brief "before its lock" | Oct 31 00:00 UTC |
| 4 | semantic | "feature completed Win and Collect" means C&W is live | dev-side note vs `#470#rc_10` (prod windows DEV-only) | not live until Oct 10 |
| 5 | semantic/category | GitHub "Ryan" is a different person from Frederick | `entity.py` join `PERSON_2314` = Frederick Stone | same person (S04) |
| 6 | referential | queue manager shipped → every live-ops panel orchestrated | `cmt_zom543_1` + `#459`/`#472` (additive order list) | Plague Race runs (D10) |
| 7 | referential | all event icons animate (ZOM-465 struck done) | `cmt_zom465_2`, Marcus's later note on the ticket (`#454#c_4` through revision 3), `cmt_zom465_3`, Brian's that it has to land, + `#456` enumeration omits C&W (T14) | C&W icon still to do |
| 8 | state/lifecycle | Calvin's Sep 24 note on ZOM-432 → daily gift frame outstanding | `cmt_zom432_2`, Samuel's closing note on the same ticket (both Sep 30 submission builds, iOS 50 and Android 135), and the ticket's Done state (T10; a trap in name only since revision 5) | nothing left |
| 9 | state/lifecycle | ZOM-387's state says whether the analytics work shipped | SC-16 card; the ticket is Todo, exactly as base has it, with no seeded note, and out of the cohort since revision 6 (`L03`) — status never graded | not a graded value |
| 10 | state/lifecycle | leagues "working fine" (Sep 22), or the re-test is an unverified report, so no hold | `b5f2955c2e154efc6835946ecfe1758e` prod re-test fails even after a restart (T7) → an established prod failure; brief: "An established failure holds it; an unverified one does not." | Held |
| 11 | referential | Robert's #zombie-art approval stands → one-off week 4 | `669d15f685f158633e56302160957f1e` DM withdrawal (T2) | all four weeks |
| 12 | other | an open/diagnosed fault thread holds the beat | brief: cosmetic and performance gaps do not hold a beat, and "An established failure holds it; an unverified one does not." (D7–D8) | Endless/SP run |
| 13 | identifier/format | the `#zombie-prs` mirror is a reachable source for Julia | `check-sql` UNVERIFIED (not a member); per-PR calls carry it | mirror non-load-bearing |
| 14 | other | file a new calendar ticket | `cmt_zom78_1` on the existing ZOM-78 (T6) | reuse ZOM-78 |
| 15 | state/lifecycle | (revision 2) Collect & Win is held until Oct 10 because its windows are not on prod at the clock | brief `f_7c3e91a4d2b85f60e1a9c4`: "A beat whose server windows are waiting on that release starts late, it is not held." | Runs, late start, no ticket note |
| 16 | state/lifecycle | (revision 2) store approval, or an Android-only submission, makes the daily-gift frame a still-to-do | `cmt_zom432_2`: "It is in both submission builds from today, iOS 50 and Android 135, so nothing is left here. Closing."; the brief's closed still-to-do is a beat's fix if it is held and anything flagged since the brief as still needed for it, not store approval | nothing left |
| 17 | referential | (revision 2) the premium-strip review note is a change-request hold on Season Pass | `#472#rc_1` sits inside Arthur's APPROVED review `#472#rev_1` since revision 8, so the review state itself says no blocker; while it was the review `#438#rev_4` its state was COMMENTED, and the platform review rejected this fork itself (P1-DR13: no CHANGES_REQUESTED in the Aug–Sep cohort) | still-to-do (Oliver); Season Pass runs |
| 18 | semantic | (revision 2) a beta push means only the Push Notification rows, or all 14 rows of the tab | `D05SD5QLG94/1759263878.305129`: "plan the PNs Beta tab as it stands, one line per row, local notifications included" and "just those four" left off | ten rows |
| 19 | semantic | (revision 2) copy that names no game fails the naming rule, so Lives recharged and 7-day lapse wait | `D05SD5QLG94/1759263878.305129`: "Copy that does not name the game at all is fine to go out, the naming rule is only about wrong names." | both Send |
| 20 | temporal | (revision 2) the Season Pass October season does not count because server windows go live only on Oct 8 | `#470#rc_10`: "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod."; `evt_9a4c2e7f1b3d58e06c7a2f` covers only the windows "still on the DEV stack" | October season runs; November opens Sat Nov 1 00:00 UTC |
| 21 | other | (revision 2) Zombie Lane is a beat players see, so it gets a calendar row | `D05SD5QLG94/1759263878.305129`: "keep Zombie Lane off the calendar, it is a permanent track with no window or reset to plan" (base `page_liveops_calendar` agrees: permanent track) | not a row; seven beats |
| 22 | state/lifecycle | (revision 3) the master checklist's tick means token travel is done, or the open token-travel ticket makes it a Season Pass or Collect & Win still-to-do | `cmt_zom526_2` (2025-09-26T15:40:50Z, the ticket's creator): the tick was taken off as marked done too early, and what is left is polish on an effect that already ships for Season Pass, which does not have to land before the beta; `cmt_zom526_3` (2025-09-30T16:24:19Z): the Collect and Win tokens go through the queue manager now and only the Axe Arena travel is left; the seeded `ZOM-521` description shows the two open items unticked | not a still-to-do and not a graded value (SC-15 repaired) |
| 23 | temporal | (revision 4) Arthur's vial note is one more note left after a merge, so the lifecycle conflict stays | `#468#rev_3` is submitted 2025-09-29T15:36:41Z and base #468 merged at 16:13:50Z: the note is a review note left before the merge | consistent; the final vial models still to do (Claire) |
| 24 | state/lifecycle | (revision 4) closing ZOM-432 leaves Calvin's "still needs the frame" as a live contradiction | `cmt_zom432_1` is dated 2025-09-24, six days before `cmt_zom432_2` closes the ticket at 2025-09-30T21:07:26Z; an older comment on a ticket closed later is ordinary history | the older word; nothing left |
| 25 | referential | (revision 4) Plague Race's windows have to come from the warehouse table, which shows 5-day runs | brief `f_7c3e91a4d2b85f60e1a9c4`: "For the quest rollover, the daily gift (Login Calendar on the push sheet, same beat) and Plague Race put down whether the beat is in, which weeks it runs and whether its push goes out, not its window dates." | no window dates for Plague Race |
| 26 | other | (revision 4) Brian may be told by DM or in a new mail | brief `f_7c3e91a4d2b85f60e1a9c4`: "you tell its owner in a reply on the mail where they committed to it"; the correction mail itself ends "reply on this mail" | a reply on `julia.lawson@harmonygames.co/1844311412966040123` |
| 27 | state/lifecycle | (revision 5) the open quests card and the push row's "Revisit once new quests roll out" mean Quests waits for a new quest set | `68dac8204f1e9a3b7c2d5e61` (Leonard, on the open card #61): "The weekly rollover does not wait on them, the current quests keep running either way."; the brief's still-to-do is what has to land before a beat runs | nothing put down for Quests; not a graded value |
| 28 | state/lifecycle | (revision 5) ZOM-565, ZOM-471 and ZOM-542 are open, so Endless or Plague Race carry a still-to-do or a hold | `cmt_zom565_1` ("not needed for the beta"), `cmt_zom471_1` ("nothing here has to land for the beta"), `cmt_zom542_1` ("not needed for the beta"): each owner says so on the ticket, and the brief leaves out polish nobody flagged | no still-to-do, no hold |
| 29 | temporal | (revision 5) Arthur's note on #470 is dated before the merge, so the windows may have gone live since | `#470#rc_10` says the windows "reach prod with the next backend release", and the release event `evt_9a4c2e7f1b3d58e06c7a2f` (Oct 8 15:00Z) reads "The server windows that are still on the DEV stack go live with this release" | Fri Oct 10 00:00 UTC stands |
| 30 | referential | (revision 6) the Axe Arena travel left on ZOM-526 is something Collect & Win or Season Pass waits for | `cmt_zom526_3`: "Only the Axe Arena travel is left here, and that waits on the event coming back."; base `C05KNDCHAAG/1758558164.541689`: "postpone Axe Arena for the beta release" | not a still-to-do of any beat |
| 31 | state/lifecycle | (revision 7) the card pack animation waiting for Brian's look, or ZOM-528 staying open, is a still-to-do of a beat | `cmt_zom521_2`: "I am leaving this item, ZOM-528 and ZOM-541 open until Brian has seen it in a build."; it names no beat and no calendar row carries card packs, and no slot reads it | not a still-to-do of the seven beats; not a graded value |
| 32 | semantic | (revision 8) Arthur's approval and "Fine for this PR" mean nothing is left, or a note on a Collect & Win PR is about Collect & Win | `#472#rc_1`: "Separately, the Season Pass premium strip art still shows the October range. It needs the November range before that season opens, Oliver is taking the date change." | a Season Pass still-to-do (Oliver) |
| 33 | temporal | (revision 8) the Weekly Leagues hold needs a date, so a run guesses one | brief `f_7c3e91a4d2b85f60e1a9c4`: "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." | held until the fix is confirmed on prod |
| 34 | state/lifecycle | (revision 9) Leonard's S23 freeze is an open failure, so Endless is held or carries a still-to-do | `e343557b2e94a1701251ebd079e6f0ce`: "Could not get it to freeze, so I am leaving this one."; brief: "An established failure holds it; an unverified one does not." | Endless runs; nothing put down |
| 35 | state/lifecycle | (revision 9) the ZOM-534 fix is only on main, so the quest rollover waits on a prod deploy | `cmt_zom534_2`, from the person who reported it: "it is good on prod now"; `cmt_zom534_1`: "That went out in the client builds" | Quests runs; nothing put down |
| 36 | state/lifecycle | (revision 9) open #477's header title and info text have to land for Collect & Win | `cmt_zom566_1`, from the ticket's creator: "the header title and the info screen text do not have to land before the beta" | not a still-to-do |
| 37 | state/lifecycle | (revision 9) the Sep 30 shader thread is flagged player-facing art, so it goes on Season Pass | `a08ff7cbfc52008d7dee8457e9385a3c`, from the person who raised it: "it rides the next store build and nothing has to land for the beta" | not a still-to-do |
| 38 | state/lifecycle | (revision 9) ZOM-563's golden frames are a prod deploy still to do on Season Pass | `cmt_zom563_2`: "Checked on prod", and the ticket is Done | not a still-to-do |
| 39 | state/lifecycle | (revision 10) Marcus's endless core-game VFX and the refill timer are flagged player-facing art for Endless | `cmt_zom565_2`, from the owner of the list: "they can follow and do not have to land before the beta" | not a still-to-do |
| 40 | scope | (revision 10) Martin's desert and port themes are beats, or art Endless waits for | `532747cb5d123a95d13204e57b5a7a38`: "Keep them as options, Endless runs with what it has now and nothing waits on new themes." | not a row and not a still-to-do |
| 41 | temporal | (revision 10) the quest rollover runs only from Oct 13, since that is its one dated rollover | `68dac8204f1e9a3b7c2d5e61`: "The weekly rollover does not wait on them, the current quests keep running either way." | All four weeks |
| 42 | scope | (revision 11) the Collect & Win icon is polish nobody flagged, like the endless VFX Brian released on ZOM-565 | `cmt_zom465_3`: "the Collect & Win icon does have to land before the event runs" | a Collect & Win still-to-do (Marcus) |
| 43 | temporal | (revision 11) a season that starts before Oct 6 or runs past Nov 2 keeps its real dates on the calendar | brief `f_7c3e91a4d2b85f60e1a9c4`: "Clip anything that starts before or runs past that to those two instants." | windows held to Mon Oct 6 00:00 UTC and Sun Nov 2 23:59 UTC |
| 44 | state/lifecycle | (revision 11) a held beat has no windows on its row until the fix lands | brief `f_7c3e91a4d2b85f60e1a9c4`: "A held beat keeps its usual windows and weeks on its row, marked held." | Weekly Leagues keeps its windows and weeks, marked held |
| 45 | scope | (revision 12) the shop's daily rotation is a reset a player sees, so it is a beat | brief `f_7c3e91a4d2b85f60e1a9c4`: "and the rotating shop is not a beat." | no shop row |
| 46 | semantic | (revision 12) "login calendar" and "Weekly Rankings" on a push row are wrong names, so the row is missing a rename | brief `f_7c3e91a4d2b85f60e1a9c4`: "(Login Calendar and Weekly Rankings are fine)" | no rename on either row |
| 47 | temporal | (revision 12) Douglas's Sep 30 prod update put the Collect & Win windows on prod, so the beat starts earlier | `cmt_zom563_1`: "That update carried only these, the Collect & Win server windows wait for the Oct 8 release." | Fri Oct 10 00:00 UTC |
| 48 | semantic | (revision 13) Arthur's vial note is an unresolved change-request blocker on a cohort PR, so Collect & Win is held | `#468#rc_38`: "Not a blocker for this PR", in a COMMENTED review | Collect & Win runs, a late start |
| 49 | semantic | (revision 13) a row's Details note belongs in What is missing, so the Quests push also waits on new quests | brief `f_7c3e91a4d2b85f60e1a9c4`: "with which of those its row is missing" | the row is Not Ready, nothing more |
| 50 | other | (revision 14) Frederick is on Brian's mail in copy, so the reply is his and Julia sends nothing | brief `f_7c3e91a4d2b85f60e1a9c4`: "you tell its owner in a reply on the mail where they committed to it" | Julia replies on `julia.lawson@harmonygames.co/1844311412966040123` |
| 51 | quantitative | (revision 14) Endless's windows are its daily resets, 28 of them | brief `f_7c3e91a4d2b85f60e1a9c4`: "Endless goes down as its weekly windows, with the daily reset noted." | four weekly windows, the daily reset as a note |

Revision-2 counter-readings (rows 15–21): each is a reading the platform review or the earlier acceptance left open,
and each is now refuted by one dated, persona-visible record. Rows 15 and 16 are the two that an agent applying the
brief's own words could still argue (a beat whose windows are not on prod yet is held; a build the stores have not
approved is unverified); the brief's late-start sentence and Samuel's both-builds note answer them directly. Row 17 has no new record on purpose:
the review state on `#438#rev_4` is COMMENTED and the platform already rejected the fork, so adding a record would
have invented a blocker that base does not have. It stays a residual risk for the rubric to word carefully. Since
revision 8 the note is an inline comment inside Arthur's APPROVED review of #472.
Row 22 is the revision-3 one: the platform review listed it as a fork (its F11, token travel as a Season Pass
still-to-do) on the tickets that carry the coherence finding and asked for one dated line that names ZOM-526 and
the Season Pass; the new line gives it without changing any expected value. Rows 23–26 are the revision-4 ones: each
is a reading the independent run on revision 3 raised, answered by a record revision 4 seeds or rewords. Rows 27–29 are the revision-5 ones, each answered by a record
revision 5 re-words or moves. Rows 30 and 31 are the revision-6 and revision-7 ones, rows 32 and 33 the revision-8 ones, rows 34 to 38 the revision-9 ones, rows 39 to 41 the revision-10 ones, rows 42 to 44 the revision-11 ones, rows 45 to 47 the revision-12 ones, rows 48 and 49 the revision-13 ones, and rows 50 and 51 the revision-14 ones.

Correct-reading count: 51 counter-readings, each with an overturning record, exceeding the 7 + 6 (intended
disagreements) floor. **Unresolved**: the difficulty is UNCALIBRATED and **borderline** (the pre-registered forecast,
P(all four gates) 0.479–0.533, was made on revision 1; the unregistered re-runs on revision 14 are in §11 Revision 14, and
the forecast cannot see record text) — resolved only by the `/create-difficulty` baseline (§11); the landing rate of
`R_ASK_FOLLOWUP` is unknown (§11); the solver-, manifest- and gate-bound lines in §4 and the gate block below are
revision-1 records until the tools are synced and the gates re-pasted (§11 Revision 2 to Revision 14); Trello carries no
weight since revision 5 and Confluence is the tenth weight-carrying service (§11 Revision 5 and Revision 6);
the call budget is 154 and the per-record count 96, with little margin over their floors (§11 Revision 8 to Revision 14).
No blocking defect in the records themselves at this stage.

```
STAGE GATE injection: PASS — Task_Authoring/task_inputsS · 01_Universe_Inject.sql#4c6328ab2e86 · 01_Hardness_Manifest.json#cb64fe02fe26 · 01_Grounding_Dossier.md#2ed958107b88 · solver/solver.py#8c25e08e10c3 · 01c_Dispositions.json#777cf02e465b · 01c_Preflight_Report.json#d01a61396e73 · 00_Assigments.md#4844ae9f5ae7 · 01_Scenario_Design.md#d3905efac6f9 · 01_Hardness_Manifest.draft.json#a69a0e4fe2ed · 01_Gradable_Surface.json#f17918c8dfc4 · __context__#7b0cc66ffd45 · __assignment__#e8b8269803d5 · __policy__#dc4ab5df3cdd · __gate_policy__#9b78441396d8 · __review__#16d4d727890d · blocking 0 · warnings 2 · checks 40
[PASS] assignment.v3_context: Julia Lawson / Product Manager; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 6 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md, solver/solver.py, 01c_Dispositions.json, 01c_Preflight_Report.json
[PASS] structure.inputs: 4 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#d3905efac6f9, 01_Hardness_Manifest.draft.json#a69a0e4fe2ed, 01_Gradable_Surface.json#f17918c8dfc4, 00_Assigments.md#4844ae9f5ae7, __context__#7b0cc66ffd45, __assignment__#e8b8269803d5, __policy__#dc4ab5df3cdd, __gate_policy__#9b78441396d8, __review__#31f6b63ef388)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 12/12 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 8/8 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 11/11 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 24/24 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 8/8 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 8, rows 110
[PASS] tool.injection_lint: hg.py lint: 0 FAIL, 0 CHECK dispositioned, 0 INFO; sha256 4c6328ab2e86 matches 01_Universe_Inject.sql
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (clock×8)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.base_claims: base_claims pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 61 draft ids
[PASS] structure.preflight: 01c_Preflight_Report.json bound by sha256 to the current SQL, solver, surface, manifest and dispositions
[PASS] solver.contract: solver contract re-run PASS
[PASS] mutation.dispositions: 50 mutation and intervention results each carry a written disposition (01c_Dispositions.json)
[PASS] geometry.upper_bound: U 0.919 (102/111) vs 1 - cap 0.15 (V3 medium): PASS (bound PASS); re-run U 0.919 PASS (bound PASS)
[WARN] geometry.margin: L_max None vs (1 - cap) + 0.10: UNSUPPORTED (advisory: the margin is a judgment, not a proof)
[PASS] liveness.dispositions: every liveness flag dispositioned (8 flag(s))
[WARN] forecast.preregistered: forecast recorded: pre-register it with tools/hardness_forecast.py --preregister before the platform run (advisory)
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 13 scoped load-bearing ids YES for julia_lawson; 1 denied/unverified probe(s), not load-bearing, each with YES alternate_evidence_ids
[PASS] structure.facts_declared: manifest declares 9 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 2 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 11 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (6 INT ids, services ['gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 13 evidenced counter-readings (of 14 found; need ≥ 12) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

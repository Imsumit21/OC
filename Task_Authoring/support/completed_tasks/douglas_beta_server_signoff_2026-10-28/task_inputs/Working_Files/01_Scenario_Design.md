# Scenario Design — dg-beta-server-signoff · design only · contains no prompt, OE or criterion text

Persona Douglas (Software Engineer, Engineering) · competency Engineering Ops · task skill Retrieval · horizon Long
(platform "Task Type": long-horizon) · difficulty mode medium (V3 cap: six-rollout average strictly under 85%; the author's own
target is under 75%, design target about 65%) · universe date October 1, 2025 (V3 freeze 00:00 UTC = Tue Sep 30, 2025 5:00 PM PT).
Builder scripts: `support/task_work/dg_beta_server/` (`mint_ids.py` mints every id into `minted_ids.json` and writes the seeded
wording into `planned_text.json`; `build_manifest.py` writes the draft manifest; `cohort.json` is the 73-ticket candidate list read
from the Linear export). Reference designs: the two completed tasks in `support/completed_tasks/` (both missed the author's 75% line
at 78.3% and 80.8% because the strong runs found every authority). **v2** applies the dual review of v1 (§13): the PR timeline now
sits on the base deploy events in the Douglas–Vincent DM, prod runs from a per-PR prod branch, every prod deploy needs a prior
Approve review by someone other than the author, the cut moved to a 12-second boundary, the import rows no longer name tickets,
conversation comments are read with `github_get_issue_comments`, and the budget was recounted without decoy reads.

## 0 Assignment, persona census and horizon note

| Field | Assigned (verbatim, `00_Assigments.md`) | Resolution |
|---|---|---|
| persona | Douglas | roster `douglas`, douglas@harmonygames.co, Engineering (`Evals/references/persona/roster.json`) |
| role | Software Engineer | backend lead; owns match3d-backend with a contractor (match3d-backend#2 "Created new env for production", Douglas, 2025-05-30) |
| business function | Engineering | Evals category Engineering & Live-Ops (`Evals/references/rules/task_categories.md`) |
| competency | Engineering Ops | release/deploy verification for the Zombie Match 3D beta (Trello list "BETA: Oct 10" on ZM ROADMAP 6851a6569f3bf818760632ab) |
| task skill | Retrieval | 73 candidate tickets × their Linear comments, 15 server PRs × their comments, 13 × their reviews, a deploy log, a calendar freeze, a Confluence page, two rule sources and two amendments, gathered into one register |
| horizon | long-horizon | manifest `horizon: Long Horizon`, `effective_profile: long` with `profile_exception` (author's 130–150 call target) |
| universe date | October 1, 2025 07:00 | built on the Oct 1, 2025 freeze, treated as 00:00 UTC (V3 §3); latest seed 2025-09-30T21:12:44Z |
| difficulty mode | medium | author target: average under 75% (design ~65%), pass@1 ≤ 2 of 6, ≥ 2 failure patterns, per-rollout SD 0.1–0.3 |

**Remit argument.** Douglas deploys the Zombie Match 3D backend to dev and prod by hand (page_cicd_pipeline "Deploy · Run by hand";
D079SNE2TL4/1757526116.670019 "the deployment to Dev is now finished", D079SNE2TL4/1757449699.464389 economy changes to prod and dev,
D079SNE2TL4/1759256193.859279 "I updated the prod environment with the latest teams/social changes"). QA keeps finding fixes that are
merged but not on prod (D079SNE2TL4/1756395503.763829 "not deployed to prod yet"; C08R27X0EAH/1757449879.885229 Arthur "we need to
deploy changes to prod server — Is that already done?"; C08R27X0EAH/1758014179.489689 "it's fixed and needs prod env deployment"), and
Douglas himself asks whether a merge means a prod deploy (D05SG9H1CFM/1758919727.787169). The ZM ROADMAP board has a "BETA: Oct 10" list
with "Fix TECH ISSUES" (trello:68d1eb90bef538c7c5c5599d). A server-side sign-off register for the beta go/no-go — which closed tickets
needed a server change and whether that change is actually on prod — is the Engineering Ops retrieval work the backend lead is pulled
into on Sep 30, 2025.

**Effective profile.** Long Horizon → normally `extreme` (≥ 500 calls, plan ~600). The requester set a per-run target of 130–150
tool calls with a hard minimum of 130 (`00_Assigments.md` "Author targets", chat 2026-10-26), which an extreme design overshoots by
4×. The manifest therefore uses the gate's `long` profile (extreme breadth, authorities, chains and traps; 100-call floor) with
`profile_exception {reason, requester_confirmation}` quoting the requester. Necessary budget: **139 unconditional calls** (§9),
recounted after review B (decoy reads, a status lookup and a PR listing removed; 13 review reads added by the approval rule).
Reviewer B's lean-run estimate for v1 was 123–128; v2 adds 13 honest review reads, 2 Confluence reads and 2 Linear writes.

Persona reach census (`python3 Task_Authoring/tools/persona_view.py reach douglas --top 10`, verbatim):

```
REACH  Douglas <douglas@harmonygames.co>  Software Engineer / Engineering
clock 2025-10-01

SLACK  user=EMPLOYEE_0031_SLACK_ID  visible channels=124 {'mpim': 37, 'public': 27, 'private': 33, 'im': 27}  messages=203394  public-not-member (UNVERIFIED)=43
  persona posts=14095 last post=2025-10-24  last activity in visible channels=2026-02-13
  C05433XK267    builds                                 public  mem=31  msgs=41107  2023-04-20..2026-02-12
  C05H8KVNU67    game-design                            private mem=27  msgs=22751  2023-07-16..2025-10-06 archived
  C050WGU41HR    engineering-bots                       private mem=35  msgs=20306  2023-03-29..2026-02-11
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16889  2023-10-07..2026-02-11
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16773  2025-01-09..2026-02-11
  D08F3K705EY    D08F3K705EY                            im      mem=5   msgs=10108  2025-02-25..2025-08-07
  C0553V44CE4    god-ui-ux                              private mem=30  msgs=5009   2023-04-21..2025-10-06 archived
  C08R27X0EAH    zombie-bugs                            private mem=23  msgs=4688   2025-05-06..2026-02-11
  C05KNDCHAAG    company-internal                       private mem=38  msgs=4605   2023-07-31..2026-02-11
  C069FF9Q57S    analytics                              private mem=28  msgs=4301   2023-12-05..2026-01-28

GMAIL  mailbox=douglas@harmonygames.co threads=4608 messages=4776 range=2023-08-29..2026-02-12
  threads by last-message month (recent): {'2025-09': 69, '2025-10': 98, '2025-11': 71, '2025-12': 42, '2026-01': 33, '2026-02': 23}
  top correspondents: SVC_0107_EMAIL (2850), SVC_2398_EMAIL (509), arthur.blake@harmonygames.co (287), leonard.hayes@harmonygames.co (273), robert@harmonygames.co (178), julia.lawson@harmonygames.co (165), SVC_4043_EMAIL (161), calvin.price@harmonygames.co (155), owen.baker@harmonygames.co (152), marcus@harmonygames.co (148)

GCAL  own=['douglas@harmonygames.co'] shared=[] events=453 (distinct ical_uid 138, cancelled 43)
  last event before clock=2025-09-29T16:30:00Z  next after clock=2025-10-06T16:00:00Z
  by month: 2023-07:1 2023-08:3 2023-09:11 2023-10:18 2023-11:17 2023-12:18 2024-01:30 2024-02:11 2024-03:4 2024-04:12 2024-05:15 2024-06:22 2024-07:21 2024-08:14 2024-09:27 2024-10:17 2024-11:19 2024-12:26 2025-01:27 2025-02:14 2025-03:5 2025-04:14 2025-05:24 2025-06:29 2025-07:22 2025-08:5 2025-09:12 2025-10:15

DRIVE  owned=9 {'application/vnd.google-apps.spreadsheet': 6, 'folder': 1, 'application/vnd.google-apps.document': 1, 'application/json': 1}
  shared-with=133 {'application/vnd.google-apps.document': 41, 'text/plain': 35, 'application/vnd.google-apps.spreadsheet': 28, 'application/json': 21, 'application/pdf': 3, 'application/vnd.google-apps.presentation': 3, 'text/csv': 2}
  shared by owner: {'Resource: -6481757892984311338': 102, 'leonard.hayes@harmonygames.co': 15, 'arthur.blake@harmonygames.co': 8, 'Resource: 7240535625619857401': 3, 'robert@harmonygames.co': 3, 'julia.lawson@harmonygames.co': 2}
  native visible: {'gdocs': 42, 'gsheets': 34, 'gslides': 3}  last modified visible=2026-01-12T17:47:18Z
  UNVERIFIED (domain/anyone, not owned/shared)=142 {'application/vnd.google-apps.document': 50, 'application/vnd.google-apps.spreadsheet': 37, 'application/pdf': 24, 'application/vnd.google-apps.presentation': 20, 'application/json': 11}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2025-10-24 (-23d), slack_visible_channels=2026-02-13 (-135d), gmail=2026-02-12 (-134d), gcal_last_event_before_clock=2025-09-29 (2d), drive_last_modified_visible=2026-01-12 (-103d)
```

Linear / GitHub / Trello identities (`entity.py resolve Douglas`, §1c): Linear `usr_cd7849ec043ab3da`, GitHub
`PERSON_5760_GITHUB_USERNAME`, Trello `1c0688ee1d9093f5b978c1db`, Confluence `user_EMPLOYEE_0031`. Arthur: Linear
`usr_cc3e90160f490686`, GitHub `EMPLOYEE_0025_GITHUB_USERNAME`, Trello `2162c1ba310341bf318f48b7`. The match3d-backend contractor is
the tokenised GitHub login `PERSON_2967_GITHUB_USERNAME` (17 of the 36 base PRs, e.g. match3d-backend#14; 15 base approvals).

## 1 Storyline

**Arc.** The Zombie Match 3D backend (Elixir/Phoenix on ECS, `page_backend_services`, D05QQF7V404/1757975508.211599) has had a
separate prod environment since 2025-06-01 (match3d-backend#2). Merging deploys nothing; dev is deployed by hand from main; prod runs
from a prod branch onto which each PR is cherry-picked when it goes out (H2 doc). Douglas's deploy log opens with the "beta prod cut"
at 2025-08-25 11:52 UTC. Through September the backend (Douglas and the contractor) ships server parts of ZOM tickets as match3d-backend
PRs #37–#54 and two spreadsheet imports; QA closes tickets when they work on dev. The prod deploys sit on the base deploy events
(Sep 8 17:17Z with the profile changes, Sep 9 20:28Z economy, Sep 10 ~18:10Z, Sep 16 16:35Z "both envs", Sep 30 18:16Z teams/social).
Arthur announces a server freeze for "monday the 29th" in #zombie-match3d (Sep 19), then pulls it in to Fri Sep 26 22:00 UTC with a
calendar event (Sep 23). Over the freeze weekend the contractor deploys #50 on Douglas's earlier approval (Arthur had said "go ahead on
dev") and #47 with Arthur's approval; Douglas rolls #54 back on Sep 28 and pushes the teams changes (#52) on Sep 30. Oliver posts a
confident QA summary on Sep 27. Douglas himself told Arthur on Sep 22 that the trophy-path fix "is out" and the algo seeds "have been on
prod since the 3rd". On Sep 29 Arthur posts the "Beta sign-off - server side" rules on the ZM ROADMAP board (same list as the client
card) and the ZM beta page on Confluence; he amends the rules by card comment (Sep 30 15:05Z) and by email (Sep 30 19:42Z); Leonard
emails Douglas to share the register with him (20:15Z); at 21:12Z Arthur asks Douglas in their DM for the server side of the sign-off.

**Timeline placement** (`references/universe_kb/timeline.md`, clock 2025-10-01): Zombie Match 3D alpha shipped 2025-04-11 with the
beta gated on KPI validation (`slack:C07C2866011:1744565232.971959`, `trello:67cb250fde144c0c37fcf5ad`); the ZM ROADMAP board was
created 2025-06-17 (`trello:6851a6569f3bf818760632d7`); Season Pass merged 2025-09-15 (`github:harmonygames-Games/match3d#438`); the
bridge outreach from 2025-09-03 frames the pressure (`gmail:leonard@harmonygames.co_1842219327413774622.json`). The Oct 10 beta is the
ZM ROADMAP list "BETA: Oct 10" (6851a674975da1fe76e70d93). Post-freeze base work (match3d-backend#36 on 2025-10-12, ZOM-563 Done
2025-10-01T13:40Z) is after the clock and not used.

**Anchors per service.**

| Service | Record | Role |
|---|---|---|
| slack | D05QQF7V404/1759266764.508127 (seed) | anchor A1, Arthur → Douglas, 2025-09-30T21:12:44Z |
| gmail | douglas@harmonygames.co/1844721277206562572 (seed) | anchor A2, Leonard → Douglas cc Arthur, 2025-09-30T20:15:03Z |
| trello | 68dabfe9bc2e8b969782e22d (seed) on 6851a6569f3bf818760632ab list 6851a674975da1fe76e70d93 | H1 "Beta sign-off - server side"; comment 68dbf1b73eba0ba580f67a6e |
| trello | 68dac311754b38be05be7ea9 (seed) | same-list client sign-off decoy |
| gmail | douglas@harmonygames.co/1844719216755416739 (seed) | Arthur's amendment (ZOM-547, ZOM-553 off) |
| gdocs | f_470ae81236d5bd39045dc1 (seed) | H2 "match3d-backend - prod deploys" (Douglas, created 2025-06-01, edited 2025-09-25) |
| gsheets | f_78bedc46245090a160d2dd (seed) | "match3d-backend deploy log": Prod deploys (cut row 2025-08-25 11:52 UTC; stops Sep 10), Console & imports |
| gcal | evt_0f489eb7fb46ada9660881 (seed; Douglas's copy of 5) | "ZM beta - server freeze" Fri 2025-09-26 22:00 UTC |
| confluence | page_zm_beta_oct10 (seed, 2025-09-29) | ZM beta page: names the "ZM Beta sign-off" folder |
| gdrive | d_69fcebc484d472907b0b5c (seed) | "ZM Beta sign-off" folder (Arthur; Douglas writer) — destination |
| gdrive | d_d71300168ca5dffa4db8b3 (seed) | "ZM Beta sign-off - client QA" folder (Oliver) — decoy |
| github | harmonygames-Games/match3d-backend#37 … #54 (seed) | server PRs with CodeRabbit walkthroughs, peer reviews, prod:/rollback: comments |
| linear | ZOM-459 … ZOM-561 (73 base tickets, `cohort.json`) + seeded comments (`minted_ids.json` LIN_NOTES) | the cohort |
| confluence | page_dd_launch_server_signoff (seed, 2025-05-12) | Domino Delights launch server sign-off (older rules, other game) |
| confluence | page_cicd_pipeline (base) | "Deploy · Run by hand"; CI has no deploy step — consistent with H2 |
| slack | C0880U9751A/1758295268.611352, /1758937233.118904, /1758938751.402267, /1758991212.775031, /1759253506.093318, /1748450537.204611; D05QQF7V404/1758571837.284511 (seeds) | freeze Monday, #50 thread + reply, Oliver's summary, post-here ask, merged-is-live claim, Douglas's own claim |
| slack | D079SNE2TL4/1757351863.576949, /1757355159.852859, /1757449699.464389, /1758040504.640159, /1759256193.859279, /1759269524.769369 (base) | the real deploy events the seeded prod: comments sit on |
| slack | C08R27X0EAH/1757307297.870139 (base) | Vincent: "prod servers read the old reward sheet" — the ZOM-510 import's grounding |

**Cohort.** `cohorts.json` LIN-DQ13 ("ZOM issues completed (Done) in 2025-Q3", 228) is the natural parent; the task cohort is its
sub-window completed after 2025-08-25 11:52 UTC through 2025-09-30 (73 issues, every `updated_at` before the clock — `cohort.json`),
source-defined by H1 rule 1 and the deploy log's first row. LIN-DQ14 (Q4) is outside it. `hazards_inside` of LIN-DQ13 ("issue completed
>1 day before first referencing PR merged: 1") is not in the sub-window.

**Natural traps used** (`references/universe_kb/trap_catalog.json`): C02 (a parent says ok/deployed and the reply narrows it — the
#50 thread), C01 (replies that correct — Arthur's "go ahead on dev"), N01 (ZOM-n has an unrelated ENG-n twin: ENG-503, ENG-557 exist),
N02 (match3d-backend#n vs match3d#n), P04 (tokenised contributor PERSON_2967 deploys half the PRs), B03 (CodeRabbit reviews are
COMMENTED, not approvals), X02 (EMPLOYEE_0032 token is the assignee of 6 of the 16 in-scope tickets), K02 (app-name lineage), D04
(lookalike sheets: the deploy log's Prod deploys tab vs the PR record).

**Originality.** Not the Combo Fighters launch record, the 133-PR residue register (merged-PR residue × reviews/commits/flags), the
RC-flag gate or the art-canon handoff; not the two completed Frederick tasks. The cohort is Linear tickets; the per-record question is
"did the fix need a server change, and is that change on prod" under a deploy rule with rollbacks, approvals and a freeze; PRs are the
second, linked cohort (Hardness_Mastery §2.5 pattern 2).

## 1a Coherence audit

Scope = every record a correct run opens: the DM (ask and Douglas's claim), the #zombie-match3d messages and thread, the two cards and
the comment, both emails, the doc, the freeze event, the deploy log, the ZM beta Confluence page, the two folders, the 73 tickets and
their comments, match3d-backend #37–#54 with comments and reviews, the base Douglas–Vincent deploy messages, the DD page and
page_cicd_pipeline. Known hazards walked from `references/universe_kb/coherence_hazards.json` (all six categories).

| Record | Category | Fields | Evidence pointer | Hazard id | Disposition |
|---|---|---|---|---|---|
| match3d-backend#36 (2025-10-12) numbered below the seeded #37–#54 (Aug 21–Sep 22) | temporal | PR number vs created_at | harmonygames-Games/match3d-backend#36 | L13 | avoid: post-clock work, invisible at the Oct 1 freeze; not cited or modified |
| Ticket closed before its server PR merged | temporal | completed_at vs merged_at | ZOM-503 completed 2025-09-22T15:11:03Z vs #52 merge 15:05Z | T04 | fold in: every seeded PR merges before its ticket's completed_at; prod deploys may follow Done (that is the task) |
| Seeded prod: times vs the base deploy messages | temporal | prod: comment times | D079SNE2TL4/1757351863.576949 (Sep 8 17:17Z), /1757449699.464389 (Sep 9 20:28Z), /1758040504.640159 (Sep 16 16:35Z), /1759256193.859279 (Sep 30 18:16Z) | T02 | fold in (review A): #42/#44 prod 17:18Z Sep 8 (profile "yes", /1757355159.852859), #46 economy 20:29Z Sep 9, #48 16:35Z Sep 16, #52 18:16Z Sep 30; Douglas's notes fall in his posting hours (15:00–03:59Z) |
| Seeded Confluence pages by Arthur | temporal | created_at vs author activity | page_dd_launch_server_signoff (2025-05-12), page_zm_beta_oct10 (2025-09-29) | T08 | avoid: Arthur active in both months (activity.json); no later edits |
| Labels used as categories | semantic | labels_json | ZOM-503 labels ["Bug"] | S03 | avoid: no rule uses labels; membership comes from comments |
| Cross-team epic children / parents | semantic | parent_id | ZOM-336 parent ZOM-97; ZOM-457 parent of ZOM-459 | S02 | fold in: card rule 1 says parent tickets get no row of their own (review A); ZOM-97 children are ZOM tickets |
| Slack/mail text citing keys and PRs | cross-service referential | ZOM keys, PR numbers | C0880U9751A/1758937233.118904 cites match3d-backend#50; the amendment cites ZOM-547/553 and #49/#53 | R01 | fold in: every cited key/PR exists (base tickets; seeded PRs) |
| Google URLs in text | cross-service referential | docs.google.com ids | f_470ae81236d5bd39045dc1 and f_78bedc46245090a160d2dd are named by title in every seed (planned_text.json) | R04 | avoid: records named by title only |
| PR comments with no Slack mirror | cross-service referential | GitHub-app copies | match3d-backend#14 (base, no mirror) | R07 | fold in: match3d-backend is not mirrored (INT-01); seeded comments get no Slack copy, like the 36 base PRs |
| Thread counters on the #50 thread parent | quantitative | reply_count / latest_reply | C0880U9751A/1758937233.118904 | Q01 | fold in: seeded parent carries reply_count 2, reply_users 2, latest_reply = Douglas's "ok" |
| Raw-shaped Slack parents | quantitative | counters absent | C0880U9751A/1757618419.809199 | Q04 | avoid: seeded rows use the full shape with counters |
| Deploy log Prod deploys tab vs PR comments | quantitative | rows | f_78bedc46245090a160d2dd | Q09 | fold in: every row the tab has agrees with a prod: comment (#37–#46, through Sep 10); H2 calls it a quick list |
| Peer reviews and CodeRabbit on match3d-backend PRs | state/lifecycle | reviews | match3d-backend#5 (base: Douglas APPROVED), match3d-backend#14 (CodeRabbit COMMENTED + walkthrough) | L09 | fold in (review A): every seeded PR gets a CodeRabbit walkthrough (#c_1) and COMMENTED review (#rev_1); peer approvals as planned; #40 and #43 carry no human review |
| Douglas's Sep 30 prod update; Vincent confirms | state/lifecycle | prod state of teams changes | D079SNE2TL4/1759256193.859279, /1759269524.769369 | L13 | fold in: it is #52's prod: comment (18:16Z), inside the freeze, approved only by the contractor → does not count under H2 (two-reading row, §10) |
| Open issue assigned to a quiet person after the writes | state/lifecycle | assignee status | ZOM-550 (assignee EMPLOYEE_0032_EMAIL) | L08 | fold in: the Todo write keeps the base assignee; no seeded record names the assignee |
| Linear user ids with spaces / tokens | identifier/format | assignee_id | ZOM-20 (usr_Robert) | I10 | fold in: seeded comment authors use exact base ids (`minted_ids.json` LIN_NOTES) |
| GitHub logins are tokens | identifier/format | author_login | match3d-backend#14 (PERSON_2967_GITHUB_USERNAME); CodeRabbit PERSON_6026_GITHUB_USERNAME | I08 | fold in: seeded PRs/comments use the base tokens |
| Gmail mailbox file aliases | identifier/format | thread file names | blake@harmonygames.co_* for arthur.blake@harmonygames.co (base gmail:leonard@harmonygames.co_1842219327413774622.json uses the leonard@ alias) | I03 | fold in (review A): copies filed under the base aliases (blake@, oliver@, leonard@); thread ids carry the roster address |
| EMPLOYEE_0032 token on many tickets | other | assignee token | ZOM-550 assignee EMPLOYEE_0032_EMAIL | I05 | avoid: never named in seeded text; comments on those tickets are by Vincent, Oliver and Douglas |

**Sibling-defect sweep.** For each designed defect, other records with the same kind in scope:
- *Merged but not on prod:* base Slack shows such cases (D079SNE2TL4/1756395503.763829 profile changes on Aug 28, before #44 existed;
  C08R27X0EAH/1758014179.489689 "needs prod env deployment" Sep 16, before the Sep 16 16:35Z deploy; D079SNE2TL4/1758649466.661059
  ZOM-563, closed post-clock). The seeded timeline agrees with each: the profile work reached prod on Sep 8 (#44), the Sep 16 deploy
  carried #48, ZOM-563 is outside the window.
- *Deploy without a prior Approve:* base PRs mostly carry peer approvals (30 of 33 merged; harmonygames-Games/match3d-backend#5, harmonygames-Games/match3d-backend#14); the
  seeded #43 (contractor hotfix) and #41 (approved after the deploy) are the designed exceptions; #40 and #51 never went to prod.
- *Deploy inside the freeze:* base D079SNE2TL4/1759256193.859279 (Sep 30) is folded in as #52; D079SNE2TL4/1759164463.327349 (Sep 29,
  Google login) concerns sign-in (ZOM-544, not Done), outside the cohort.
- *Rollback (D05QQF7V404/1756483262.665079):* no base rollback of a match3d-backend deploy in Aug–Sep (searched "rollback"/"revert" in Slack Aug 22–Sep 30; the only
  hit is Arthur's own game-of-dominoes-backend test deploy, D05QQF7V404/1756483262.665079); the seeded #44 and #54 are the only ones.
- *Data imports to prod:* C08R27X0EAH/1757270187.537249 and /1757307297.870139 (Sep 7–8: prod reads the old reward sheet) and
  D079SNE2TL4/1757350210.055289 (Sep 8 "row limit for prod reward sheet") match the ZOM-510 import to prod on Sep 8 16:45Z; no base
  record covers the algo level pack (ZOM-256), seeded as a dev import.
- *Freeze date:* no base record dates a ZM server freeze; the two seeded versions (C0880U9751A/1758295268.611352 Monday,
  evt_0f489eb7fb46ada9660881 Friday) are the only ones.

## 1b Active speakers

Every person given a seeded voice, with `status_at_clock` from `references/universe_kb/activity.json` (clock 2025-10-01).

| Person | Email | status_at_clock (activity.json) | Seeding role |
|---|---|---|---|
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025 | DM ask; H1 card + comment; client card; amendment email; freeze event; #zombie-match3d freeze message and thread reply; both Confluence pages; APPROVED/COMMENTED reviews; beta folder |
| Douglas | douglas@harmonygames.co | active_sep_2025 | persona; H2 doc; deploy log; Sep 22 DM claim; #50 question in #zombie-match3d; prod:/rollback: comments and approvals in his hours (15:00–03:59Z); ZOM-537 comment |
| Oliver Brooks | oliver.brooks@harmonygames.co | active_sep_2025 | merged-is-live claim (May); QA summary (Sep 27); post-here ask; client QA folder; Linear comments on his tickets |
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025 | anchor A2 email; ZOM-256 comment |
| Vincent Parker | vincent.parker@harmonygames.co | active_sep_2025 | Linear QA comments (EMPLOYEE_0032 tickets); "works on dev" on #51 |
| Owen Baker | owen.baker@harmonygames.co | active_sep_2025 | ZOM-503 comment; freeze attendee |
| Calvin Price | calvin.price@harmonygames.co | active_sep_2025 | ZOM-499 and client-ticket comments |
| Claire Morgan | claire.morgan@harmonygames.co | active_sep_2025 | ZOM-336 (Cooler) and prop-ticket comments |
| Samuel Turner | samuel.turner@harmonygames.co | active_sep_2025 | client-ticket comments (ZOM-470, ZOM-558, ZOM-536, ZOM-498) |
| Marcus Bennett | marcus.bennett@harmonygames.co | active_sep_2025 | VFX-ticket comments (ZOM-464, ZOM-511, ZOM-519, ZOM-538, ZOM-112) |
| Brian Foster | brian.foster@harmonygames.co | active_sep_2025 | ZOM-419 comment |

The contractor (GitHub `PERSON_2967_GITHUB_USERNAME`) and CodeRabbit (`PERSON_6026_GITHUB_USERNAME`) write only on PRs, as on base
PRs (match3d-backend#14). Seeded text follows `references/universe_kb/conventions.json` (Arthur's DMs lowercase and short; Linear
comments one or two lines; PR notes start with the H2 keyword).

## 1c Identity traps

`python3 Task_Authoring/tools/entity.py collisions` (verbatim, first sections) and `resolve` for every person the design names:

```
SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <marcus@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']

SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']

TOKENS_MAPPING_TO_SEVERAL_ENTITIES (9)
  EMPLOYEE_0032: {'entities': ['? <EMPLOYEE_0032_EMAIL>', 'Josh Dempsey <josh.dempsey@harmonygames.co>', '? <github:EMPLOYEE_0032_GITHUB_USERNAME>', '? <slack:EMPLOYEE_0032_SLACK_ID>'], 'records': ['confluence.id=user_EMPLOYEE_0032', 'gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME', 'slack.id=EMPLOYEE_0032_SLACK_ID']}

ENTITY email:douglas@harmonygames.co  name=Douglas  kind=person  emails=['douglas@harmonygames.co']
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
ENTITY email:oliver.brooks@harmonygames.co  name=Oliver Brooks  kind=person  emails=['oliver.brooks@harmonygames.co']
ENTITY email:vincent.parker@harmonygames.co  name=Vincent Parker  kind=person  emails=['vincent.parker@harmonygames.co']
ENTITY email:owen.baker@harmonygames.co  name=Owen Baker  kind=person  emails=['owen.baker@harmonygames.co']
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
ENTITY email:calvin.price@harmonygames.co  name=Calvin Price  kind=person  emails=['calvin.price@harmonygames.co']
ENTITY email:claire.morgan@harmonygames.co  name=Claire Morgan  kind=person  emails=['claire.morgan@harmonygames.co']
```

Correct entity vs lookalikes: Oliver Brooks is oliver.brooks@harmonygames.co (not Lauren Brooks, lauren@harmonygames.co, who has no
authored activity before Oct 10); Owen Baker is owen.baker@harmonygames.co (not Thomas Baker); Arthur's mailbox files are `blake@…`,
Leonard's `leonard@…`, Oliver's `oliver@…`. "Blake" in Slack (Douglas's name for Arthur, D079SNE2TL4/1759164463.327349) is Arthur Blake.
Ticket identity: every ZOM-n has an unrelated ENG-n twin (N01; ENG-503 and ENG-557 exist). PR identity: match3d-backend#n vs match3d#n
(the client repo, mirrored to #zombie-prs) — the H2 doc and every comment say match3d-backend.

## 2 Cohort spine

**Rule (H1 rule 1 + comment + email).** ZOM tickets moved to Done after the beta prod cut (deploy log first row: 2025-08-25 11:52
UTC) through Sep 30, whose fix needed a server change — a match3d-backend PR, a Nakama console change logged in the deploy log, or
(comment) a spreadsheet import on the backend logged there — no rows for parent tickets — minus ZOM-547 and ZOM-553 (email).
Candidates: **73** tickets (`cohort.json`: ZOM-459 … ZOM-561; 10 are prop-art children of ZOM-97; ZOM-457 is a parent). In scope: **16**.

**Per-ticket truth** (planned; every PR/import, time and reviewer from `minted_ids.json`):

| # | Ticket (completed_at) | Server change(s) | Decisive records | On prod |
|---|---|---|---|---|
| 1 | ZOM-459 (2025-08-25T11:53:11Z) | match3d-backend#38 | in the 11:52 cut; contractor APPROVED 09:20 | Y |
| 2 | ZOM-509 (09-04) | #39 | Douglas APPROVED 09-02 15:20; prod: 17:30 | Y |
| 3 | ZOM-336 Cooler (09-03) | #40 ("Items: make the cooler a usable item") | dev note only | N |
| 4 | ZOM-392 (09-04) | #41 | prod: 09-03 16:30; contractor APPROVED 18:05 (after) | N |
| 5 | ZOM-503 (09-22) | #42 + #52 | #42 ok (Sep 8); #52 prod: 09-30 18:16 inside the freeze, approved by the contractor only | N |
| 6 | ZOM-518 (09-04) | #43 | prod: 09-04 12:50; only CodeRabbit's COMMENTED review | N |
| 7 | ZOM-499 (09-17) | #44 | CHANGES_REQUESTED → APPROVED 09-08 15:10; prod: 09-08 17:18 → rollback: 09-20 → prod: 09-22 17:30 | Y |
| 8 | ZOM-531 (09-15) | #45 | CHANGES_REQUESTED → APPROVED 09-10 15:10; prod: 18:20 | Y |
| 9 | ZOM-537 (09-15) | #46 | Arthur APPROVED 09-09 19:40; prod: 20:29 | Y |
| 10 | ZOM-444 (09-15) | #47 | prod: 09-27 16:20 inside the freeze; Arthur APPROVED 16:05 | Y |
| 11 | ZOM-487 (09-17) | #48 | Douglas APPROVED 09-16 15:20; prod: 16:35 (before the freeze) | Y |
| 12 | ZOM-550 (09-19) | #50 | prod: 09-27 14:30 inside the freeze; Douglas APPROVED (Sep 19); Arthur only COMMENTED (Sep 29) | N |
| 13 | ZOM-435 (09-22) | #51 | dev note only (Vincent: "works on dev") | N |
| 14 | ZOM-557 (09-30) | #54 | prod: 09-24 → rollback: 09-28 | N |
| 15 | ZOM-510 (09-11) | Zombie Lane rewards import (log: prod, 09-08 16:45) | comment names the import; log row → prod | Y |
| 16 | ZOM-256 (09-11) | algo levels 2.0 pack import (log: dev, 09-11 16:30) | comment names the import; log row → dev | N |
| — | ZOM-547, ZOM-553 | #49, #53 (on prod) | Arthur's email: off the register, not counted | out |
| — | ZOM-461 (2025-08-25T11:51:48Z) | #37 (in the cut) | closed 12 seconds before the cut | out |
| — | ZOM-457 (11:53:20Z) | parent of ZOM-459 | rule 1: parents get no row | out |
| — | 54 other candidates (e.g. ZOM-555, ZOM-470, ZOM-515) | none (client/art/VFX notes) | comment is a client build note | out |

Totals the deliverables carry: 16 tickets; **8 on prod**, **8 not on prod** (ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-550, ZOM-435,
ZOM-557, ZOM-256); 8 Todo moves + 8 comments.

**Surfaces and shortcut audit.**

| Surface | Per-record call | Bulk call that does not cover it | Requirement · decides |
|---|---|---|---|
| Linear comments on each of the 73 candidates (seeded; base has none) | `linear_list_comments` × 73 | `linear_list_issues` returns no comments; PR titles/bodies in match3d-backend never name ZOM keys (base convention, #1–#35); neutral comments also mention match3d-backend ("nothing needed in match3d-backend"), so a query on that word returns half the cohort | R1 · register membership |
| PR conversation comments on the 15 in-scope server PRs (seeded) | `github_get_issue_comments` × 15 | list/search give merged_at, not comment bodies/times; no Slack mirror (INT-01); an `in:comments` search returns which PRs mention prod/rollback, not the times that decide the freeze and approval comparisons, and #44 (prod, rollback, prod) defeats it | R3 · on prod (Y/N) |
| PR reviews on the 13 PRs with a prod: comment (seeded) | `github_get_pull_request_reviews` × 13 | review state, reviewer and time only per PR; every PR also has a CodeRabbit COMMENTED review | R3 · on prod (Y/N) |

**Short-circuit audit.** Membership is decided only by the comments (an art prop, an analytics event and a trophy-path claim are
server tickets; a "Zombie Lane Reward Animations" ticket is not). On prod needs both the deploy comments and the reviews: the comment
gives the deploy time, the review the approval time and approver — four in-scope rows fail on the review alone (#41 after, #43 none, #50
and #52 not Arthur in the freeze), one on a rollback (#54), two never deployed (#40, #51). A run that reads every comment but skips the
reviews gets four rows wrong; a run that trusts merges, the log tab or a summary gets five or more wrong.

**Predicate details.** Closed vocabulary: on prod Y/N. Window: completed_at > 2025-08-25T11:52:00Z and ≤ 2025-09-30. Server change:
match3d-backend PR or logged console change/import. Aggregation (rule 4): Y only if every server change is on prod. **House rules
overriding the natural reading (A15):** merged is not on prod; a deploy counts only with an earlier Approve review by someone other than
the author; inside the freeze only Arthur's Approve counts (a Slack "go ahead", a Comment review, a peer approval or a working prod deploy
confirmed by QA do not); a rollback takes the PR off prod whenever it happens. **Dual regime (S11):** before vs inside the server freeze
(Fri 2025-09-26 22:00 UTC). **Boundary records (A17/A10):** ZOM-461 (11:51:48, server #37) vs ZOM-459 (11:53:11, server #38); ZOM-457 the
parent; ZOM-336 under the art epic; the two import tickets; the two email-excluded boss-arena tickets vs ZOM-550.

Necessity rule (Hardness_Mastery §2.5): 16 of 73 candidates flip (22%); neutral comments sit on the other 57 and on ~10 non-cohort
tickets (open ZOM tickets and those closed just before the cut), so having a comment reveals nothing; no upstream record lists the server
tickets; comments say "backend part" / "nothing needed in match3d-backend", never the rule's phrase "server change".

## 3 Hidden authorities

| Id | Name (how it is reached) | Home | Governs | Decoy(s) | Decoy scope / supersession | Findability proof |
|---|---|---|---|---|---|---|
| H1 | the beta server sign-off rules ("the rules are on the beta card on the roadmap board", D05QQF7V404/1759266764.508127) | trello 68dabfe9bc2e8b969782e22d + comment 68dbf1b73eba0ba580f67a6e; email douglas@harmonygames.co/1844719216755416739 | R1, R2, R4, R6 | same-list client card 68dac311754b38be05be7ea9; Confluence page_dd_launch_server_signoff | team scope: client builds (Oliver) vs server changes (Douglas); the DD page is another game and the oldest version (T1 version_records) | a Trello search "beta sign-off" returns both cards; proven at injection with `hg.py search search trello "beta sign-off"` |
| H2 | the match3d-backend prod deploys doc (card rule 3: "On prod means what the match3d-backend prod deploys doc says", trello:68dabfe9bc2e8b969782e22d) | gdocs f_470ae81236d5bd39045dc1 | R3 | Oliver's May claim C0880U9751A/1748450537.204611 ("once something is merged into main it's live") | older version, true for the single-environment period before match3d-backend#2 (T3 version_records) | a Docs search "prod deploys" returns it; Slack search "merged" returns the claim |

`governs` lists do not overlap. The anchor names only H1; H2, the freeze event, the deploy log, the ZM beta page, the comment and the
email are reached from the card (rules 1, 3, 6), the doc (freeze, imports tab, prod: comments, approvals) and Gmail on the card's title.

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Arthur's beta sign-off ask | slack D05QQF7V404/1759266764.508127 |
| A2 | Leonard's go/no-go email | gmail douglas@harmonygames.co/1844721277206562572 |

**Hub** = A1 (Arthur's voice) delegating to H1 and the reply; A2 (Leonard) carries the share.

**Incorporation table** (quotes are exact substrings of `planned_text.json`; the gate re-reads them from the SQL at injection):

| Fragment | Service · container | Kind | Chain | delegated_by_record | delegation_quote | Requirements | Names |
|---|---|---|---|---|---|---|---|
| K1 | slack · D05QQF7V404/1759266764.508127 | delegation | A1 | D05QQF7V404/1759266764.508127 | "reply here when it's done with how many tickets are on prod and which ones aren't" | R5 | H1 |
| K2 | trello · 68dabfe9bc2e8b969782e22d | requirement | A1 | D05QQF7V404/1759266764.508127 | "the rules are on the beta card on the roadmap board" | R1 R2 R6 | H2 |
| K3 | trello · 68dbf1b73eba0ba580f67a6e (comment) | amendment | A1→K2 | trello:68dabfe9bc2e8b969782e22d | "Douglas owns this one." (the comment sits on the card) | R1 | — |
| K4 | gmail · douglas@harmonygames.co/1844719216755416739 | exclusion | A1→K2 | trello:68dabfe9bc2e8b969782e22d | "Douglas owns this one." (Arthur's email on the card's title) | R1 | — |
| K5 | gdocs · f_470ae81236d5bd39045dc1 | requirement | A1→K2 | trello:68dabfe9bc2e8b969782e22d | "On prod means what the match3d-backend prod deploys doc says" | R3 | — |
| K6 | gcal · evt_0f489eb7fb46ada9660881 | requirement | A1→K2→K5 | gdocs:f_470ae81236d5bd39045dc1 | "from the server freeze on the calendar until the beta ships" | R3 | — |
| K7 | gsheets · f_78bedc46245090a160d2dd (Prod deploys A2) | requirement | A1→K2 | trello:68dabfe9bc2e8b969782e22d | "after the beta prod cut (the first row of Douglas's deploy log) through Sep 30" | R1 | — |
| K8 | gsheets · f_78bedc46245090a160d2dd (Console & imports) | requirement | A1→K2→K5 | gdocs:f_470ae81236d5bd39045dc1 | "they go in the deploy log, Console & imports tab" | R2 | — |
| K9 | confluence · page_zm_beta_oct10 | destination | A1→K2 | trello:68dabfe9bc2e8b969782e22d | "the sign-off folder named on the ZM Beta page in Confluence" | R4 | — |
| K13 | gdrive · d_69fcebc484d472907b0b5c | destination | A1→K2→K9 | confluence:page_zm_beta_oct10 | "Sign-off folder: ZM Beta sign-off (Drive, Arthur's)." | R4 | — |
| K10 | linear · team_ZOM (cohort tickets) | destination | A1→K2 | trello:68dabfe9bc2e8b969782e22d | "Anything not on prod goes back to Todo with a comment saying which change still has to go out." | R6 | — |
| K11 | github · harmonygames-Games/match3d-backend#37…#54 | requirement | A1→K2→K5 | gdocs:f_470ae81236d5bd39045dc1 | "comments on that PR with a line starting \"prod:\"" | R3 | — |
| K12 | gmail · douglas@harmonygames.co/1844721277206562572 | recipient | A2 | douglas@harmonygames.co/1844721277206562572 | "please share it with me directly. Comment access please" | R7 | — |

**Amendments.** K3 (Trello comment, 2025-09-30T15:05:27Z) adds spreadsheet imports on the backend to rule 1 (any target; the log's
target then decides on prod); K4 (Gmail, 2025-09-30T19:42:18Z, subject "Beta sign-off - server side") takes ZOM-547 and ZOM-553 off and
out of the count. Both say "rest of the card stands". Neither is announced by the card or the ask (later applicable updates supersede
without announcement, `Evals/WORKFLOW.md` `prompt-incorporation-v1`); both are from the card's author, on the card or its title.

**Non-authoritative instruction distractors.** Oliver's "post it here too" (C0880U9751A/1759253506.093318) is not Arthur's
destination; the client card's "back to In Validation" governs client tickets (68dac311754b38be05be7ea9); the DD page's "thumbs-up in
#live-incidents" governs the Domino Delights launch (page_dd_launch_server_signoff); Oliver's summary (C0880U9751A/1758991212.775031) and
Douglas's own Sep 22 message (D05QQF7V404/1758571837.284511) are claims.

## 5 Chains and trap register

**Chains** (manifest `chains`): C1 A1 (Oliver's summary → #54 rollback → H2 → ZOM-557 N); C2 A15 (Arthur's "go ahead on dev" reply →
freeze Fri 22:00 UTC → #50 prod: Sep 27 with Douglas's approval only → H2 → ZOM-550 N); C3 A6 (Douglas's Sep 30 teams deploy confirmed by
Vincent → #52 prod: inside the freeze with the contractor's approval → #47 with Arthur's APPROVED → ZOM-503 N, ZOM-444 Y); C4 A10 (cut
11:52 → ZOM-461 12 s before, out → ZOM-459 in); C5 A13 (card comment → Console & imports rows → ZOM-510 Y, ZOM-256 N); C6 A7 (card
rule 1 → Arthur's email → ZOM-550 stays); C7 A4 (ZOM-503 names #42 and #52 → rule 4 → N); C8 A19 (Douglas's "on prod since the 3rd" →
#41 prod: 16:30 → approval 18:05 → H2 → ZOM-392 N).

| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | superseding (4 versions) | page_dd_launch_server_signoff → 68dabfe93a26ef2186dcec1c → 68dbf1b73eba0ba580f67a6e → douglas@harmonygames.co/1844719216755416739 | R1 | DD page or card alone: no imports, ZOM-547/553 kept | card → comment → email | Confluence search returns the DD page first; comment and email unannounced |
| T2 | superseding | C0880U9751A/1758295268.611352 → evt_0f489eb7fb46ada9660881 | R3 | freeze Monday → #50 needs no Arthur approval → ZOM-550 Y | calendar event (updated Sep 23): Fri 22:00 UTC | Slack search "freeze" hits Monday first |
| T3 | superseding | C0880U9751A/1748450537.204611 → f_470ae81236d5bd39045dc1 | R3 | merged = live → ZOM-336, ZOM-435 Y | doc: prod branch, prod: comment | Slack search "merged" |
| T4 | stale_summary | C0880U9751A/1758991212.775031 → match3d-backend#54#c_3 | R3 | everything since the cut on prod | PR records | newest server-status message |
| T5 | superseding (3 versions) | match3d-backend#44#c_2 → #44#c_3 → #44#c_4 | R3 | stops at rollback → ZOM-499 N | newer prod: Sep 22 | — |
| T6 | distractor · partial_listing | f_78bedc46245090a160d2dd (Prod deploys tab) | R3 | tab as the record → ZOM-487, ZOM-444 N; ZOM-392, ZOM-518 Y | doc: PR comment + prior Approve | log already open for the cut row |
| T7 | distractor · scope_adjacent | 68dac311754b38be05be7ea9 | R6 | back to In Validation / Aug 15 window | server card governs | same search returns both |
| T8 | conclusion_stop | C0880U9751A/1758937233.118904 → /1758938751.402267; match3d-backend#50 | R3 | "go ahead" read as approval → ZOM-550 Y | reply limits to dev | parent names prod; limit is in the reply |
| T9 | exact_predicate | match3d-backend#50#rev_2, #50#rev_3, match3d-backend#47#rev_2 | R3 | an Approve plus a review by Arthur → ZOM-550 Y | inside the freeze only Arthur's Approve | — |
| T10 | synthesis_omission | ZOM-503 comment; match3d-backend#42, match3d-backend#52; D079SNE2TL4/1759256193.859279 | R3 | first PR only, or Vincent's "works as expected" → ZOM-503 Y | rule 4 + freeze approval | — |
| T11 | exact_predicate | f_78bedc46245090a160d2dd; ZOM-461, ZOM-459 | R1 | September window (drops ZOM-459) or date-only Aug 25 (adds ZOM-461) | cut 11:52 UTC | card names the cut, log has the time |
| T12 | tool_surface | ZOM-459 … ZOM-256 comments | R2 | server change guessed from titles | per-ticket comments | — |
| T13 | scope_alias | ZOM-336 comment; match3d-backend#40 | R1 | art props skipped by title | comment names #40 | — |
| T14 | reuse_exclusion | the 8 not-on-prod tickets (ZOM-336 …) | R6 | new tickets created | rule 5: same ticket | — |
| T15 | distractor · keyword_collision | ZOM-510 comment; ZOM-555 | R1 | ZOM-555 taken for the rewards import | comments differ | — |
| T16 | distractor · non_authoritative_instruction | C0880U9751A/1759253506.093318 | R5 | counts posted in the channel instead of the DM | ask: reply here | — |
| T17 | distractor · lookalike_entity | douglas@harmonygames.co/1844719216755416739; ZOM-550, ZOM-547, ZOM-553 | R1 | every boss-arena ticket dropped | email names two tickets | — |
| T18 | synthesis_omission | douglas@harmonygames.co/1844721277206562572 | R7 | Leonard never shared / editor / folder shared | Leonard's email | Gmail rarely opened |
| T19 | distractor · scope_adjacent | d_d71300168ca5dffa4db8b3 | R4 | register in the client QA folder | ZM beta page names Arthur's folder | both folders "ZM Beta sign-off…" |
| T20 | distractor · stale_summary | C0880U9751A/1758991212.775031 | R5 | reply says all but golden frames on prod | per-PR records: 8 / 8 | — |
| T21 | exact_predicate | match3d-backend#41#rev_2, match3d-backend#43; f_470ae81236d5bd39045dc1 | R3 | a prod: comment is enough, or a later approval counts → ZOM-392, ZOM-518 Y | Approve before the deploy, by someone else | — |
| T22 | stale_summary | D05QQF7V404/1758571837.284511; match3d-backend#51, match3d-backend#41 | R3 | Douglas's own claim → ZOM-435, ZOM-392 Y | #51 dev only; #41 approved after | the claim sits in the same DM as the ask |

Trap independence: T2/T8/T9 fail ZOM-550 by three routes but no other row; T21 fails ZOM-392 and ZOM-518 (review timing/absence) and is
independent of the freeze; T10/C3 fail only ZOM-503; T5 and T6 fail ZOM-499/487/444 by different routes; T11, T13, T15, T17 fail
different membership rows. No record states a conclusion: comments name PRs/imports, PR comments are raw deploy events, reviews are
states with times, the doc defines on prod, both summaries are wrong.

## 6 Failure-diversity plan

| Chain / trap | Runs that plausibly miss it | Rows it touches |
|---|---|---|
| C8/T21/T22 (approval timing/absence) | runs that read prod: comments but not reviews, or trust Douglas's own message | ZOM-392, ZOM-518 (and ZOM-435) |
| C2/T2/T8/T9 (freeze + "go ahead" + review type) | runs that never open Calendar (5/131, A13), stop at the thread parent (A14) or count any approval | ZOM-550 |
| C3/T10 (Sep 30 teams deploy) | runs that trust Vincent's confirmation or check one PR per ticket | ZOM-503 |
| C1/T4 (summary vs rollback) | runs that trust QA's summary | ZOM-557 |
| T3/T6/T5 (merged = live; stale tab; rollback then redeploy) | runs that use merge state, the log tab, or stop at the first rollback | ZOM-336, ZOM-435, ZOM-499, ZOM-487, ZOM-444 |
| C4/T11 (12-second cut) | runs that use "September" or the date only | ZOM-459, ZOM-461 |
| C5 (imports) | runs that read the card description only (comment unannounced) | ZOM-510, ZOM-256 |
| C6/T17 (email) | runs that never search Gmail (60/131 used it) | ZOM-547, ZOM-553, ZOM-550 |
| T12/T13/T15 (membership by comments) | runs that sample comments or skip art props | ZOM-336, ZOM-444, ZOM-555 |
| T14/T7 (writes) | runs that create tickets or use In Validation | the 8 Todo moves |
| T18 (share) | runs that never open Leonard's email | R7 |

No single discovery gates more than four of the sixteen rows; the reply's count and keys move with every row error.

## 7 Deliverables and dependent writes

| Write | Tool | Content depends on | Requirements |
|---|---|---|---|
| W1 register (Google Sheet, 16 rows: ticket, server change(s), on prod Y/N) | `gsheets_create_spreadsheet` + `gsheets_values_update` (or `gdrive_create_file` with `parentId`) | K2–K8, C1–C8, T11, T12, T21 | R1–R3 |
| W2 register in the ZM Beta sign-off folder (d_69fcebc484d472907b0b5c) | `gdrive_move_file` | K9, K13 | R4 |
| W3 share the register with Leonard (leonard.hayes@harmonygames.co, commenter) | `gdrive_share_file` | K12 | R7 |
| W4 DM reply to Arthur (D05QQF7V404): 8 on prod; not on prod ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-550, ZOM-435, ZOM-557, ZOM-256 | `slack_send_message` | K1, C1–C3, C7, C8 | R5 |
| W5 for each of the 8: state → Todo + comment naming the change still to go out (#40; #41 redeploy after approval; #52; #43 needs an approval; #50; #51; #54; the algo level pack import) | `linear_update_issue` + `linear_create_comment` | K10, C1–C3, C5, C7, C8, T14, T21 | R6 |

Reuse-vs-create (A8): W5 reuses the existing tickets. Douglas can edit: Linear writes are unscoped; the beta folder is shared with him
as writer (record plan); the DM is his; he owns the sheet he creates and can share it.

## 8 Service role map

| Service | Role | Load-bearing fact / write | Carrier |
|---|---|---|---|
| slack | anchor ask, Douglas's claim, freeze message, #50 thread, summary; W4 | D05QQF7V404/1759266764.508127; C0880U9751A/1758938751.402267 | ● |
| trello | H1 + comment; client card decoy | 68dabfe9bc2e8b969782e22d; 68dbf1b73eba0ba580f67a6e | ● (description, comment) |
| gmail | amendment; Leonard's share request | douglas@harmonygames.co/1844719216755416739; douglas@harmonygames.co/1844721277206562572 | ● |
| gdocs | H2 | f_470ae81236d5bd39045dc1 | ● |
| gcal | freeze instant | evt_0f489eb7fb46ada9660881 (start field) | ● (start/end; description supporting only) |
| gsheets | deploy log (cut row, imports); W1 | f_78bedc46245090a160d2dd | ● |
| gdrive | destination; client QA decoy; W2, W3 | d_69fcebc484d472907b0b5c | ● (metadata) |
| confluence | ZM beta page (folder name); DD decoy; page_cicd_pipeline | page_zm_beta_oct10 | ● (body) |
| linear | cohort + per-ticket comments; W5 | ZOM-503 comment (`minted_ids.json` LIN_NOTES) | ● (Ask_Carriers §6b: Linear comments render) |
| github | prod:/rollback: comments, reviews | match3d-backend#44#c_4; match3d-backend#47#rev_2 | ● |
| gslides, contacts, snowflake | none | — | — |

## 9 Call budget

| Phase | Service | Calls | Reason |
|---|---|---|---|
| discovery | slack | 2 | read the ask (and Douglas's earlier claim) in D05QQF7V404; search #zombie-match3d for the freeze and the #50 thread with replies |
| discovery | trello | 2 | search "beta sign-off"; read the server card 68dabfe9bc2e8b969782e22d with its actions (comment) |
| discovery | confluence | 2 | find the ZM Beta page the card names; read it for the folder |
| discovery | gdocs | 2 | find the prod deploys doc the card names (f_470ae81236d5bd39045dc1); read it |
| discovery | gcal | 1 | list events Sep 22–30 for the freeze |
| discovery | gmail | 3 | search mail on the sign-off; read Arthur's amendment; read Leonard's email |
| discovery | gsheets | 2 | deploy log Prod deploys (cut row) and Console & imports tabs |
| discovery | gdrive | 1 | find the ZM Beta sign-off folder id |
| enumeration | linear | 2 | list ZOM Done issues; page to every completion after the cut |
| per-record | linear | 73 | one comment read per candidate ticket |
| per-record | github | 15 | one conversation-comment read (`github_get_issue_comments`) per in-scope server PR |
| per-record | github | 13 | reviews on every in-scope PR with a prod: comment |
| writes | gsheets | 2 | create; write rows |
| writes | gdrive | 2 | move into the folder; share with Leonard |
| writes | slack | 1 | DM reply |
| writes | linear | 16 | 8 × (state → Todo; comment) |
| **total** | 10 services | **139** unconditional | largest share outside the per-record phase linear 47% |

Golden-run rule: a correct run cannot skip a candidate's comments (16 of 73 flip), a server PR's comments (deploy times, rollbacks) or
its reviews (four rows fail on approval alone), the freeze event, the card comment, the ZM beta page or either email. Collapsing the
sheet create+move into one `gdrive_create_file` saves one call. Ordinary exploration (searches before finding, decoys, the wrong GitHub
comment tool first — review B) adds to the 139; the completed tasks ran +7 to +39 over their necessary budgets, so runs are expected
around 140–175. If the Opus pre-check lands under 130, hardening moves the cut earlier (more candidates), never padding.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by |
|---|---|---|---|
| Window start | after 2025-08-25 11:52 UTC (deploy log row 1) | "September", or the whole of Aug 25 | card rule 1 names the cut as the log's first row (f_78bedc46245090a160d2dd); ZOM-461 closed 11:51:48 |
| ZOM-457 (parent) | no row | it closed after the cut | card rule 1 "Parent tickets don't get a row of their own" (68dabfe9bc2e8b969782e22d) |
| ZOM-336 (prop art) in scope? | yes | art props never touch the server; its nine siblings | its comment names match3d-backend#40 ("make the cooler a usable item", singular); the siblings' comments say nothing needed in match3d-backend |
| Imports in scope (ZOM-510, ZOM-256)? | yes, both | the dev-only import is not a server change | comment 68dbf1b73eba0ba580f67a6e "spreadsheet imports on the backend count as server changes too" (no target condition); target decides on prod |
| ZOM-547/553 in scope or counted? | no | they have match3d-backend PRs (#49, #53) | Arthur's email douglas@harmonygames.co/1844719216755416739 ("not part of the count either way") |
| ZOM-550 in scope? | yes | the email is about boss arena | the email names only ZOM-547 and ZOM-553 |
| Merged = on prod? | no | Oliver's May claim C0880U9751A/1748450537.204611 | H2 doc (prod branch, per-PR picks); page_cicd_pipeline "Run by hand" |
| Later deploys carry earlier merges? | no | prod is a build of main | H2: prod runs from the prod branch; only picked PRs are on prod (review A blocker 2) |
| ZOM-392 (#41 approved after its deploy) | N | it was deployed and approved | H2 "Approving afterwards doesn't fix it; redeploy" |
| ZOM-518 (#43, CodeRabbit review only) | N | it has a review | H2 needs an Approve by someone other than the author; CodeRabbit's is COMMENTED |
| ZOM-499 (#44 prod, rollback, prod) | Y | N (rolled back) | newer prod: comment Sep 22, before the freeze, approval Sep 8 |
| Freeze start | Fri 2025-09-26 22:00 UTC | Mon Sep 29 (C0880U9751A/1758295268.611352) | calendar event evt_0f489eb7fb46ada9660881 updated Sep 23, "Pulled in from Monday" |
| ZOM-550 (#50 deployed Sep 27) | N | Arthur said "go ahead"; Douglas approved; Arthur reviewed | reply C0880U9751A/1758938751.402267 limits to dev; inside the freeze only Arthur's Approve counts; his is COMMENTED |
| ZOM-444 (#47 in the freeze) | Y | freeze deploys roll back | #47 has Arthur's APPROVED review before the prod: comment |
| ZOM-503 teams changes on prod Sep 30 | N | Douglas updated prod and Vincent confirmed it works (D079SNE2TL4/1759256193.859279, /1759269524.769369) | #52's prod: is inside the freeze with only the contractor's approval → does not count (H2) |
| ZOM-557 rollback inside the freeze | N | an unapproved rollback in the freeze doesn't count, so #54 stays on prod | H2 "A rollback takes the PR off prod whenever it happens, freeze or not" (review A) |
| ZOM-487 (#48 Sep 16) | Y | the log tab stops on Sep 10 | #48 prod: Sep 16 16:35 (base D079SNE2TL4/1758040504.640159), approved 15:20 by Douglas, before the freeze |
| Reply placement and content | DM D05QQF7V404 with "8" and the 8 keys | #zombie-match3d (C0880U9751A/1759253506.093318) | ask: "reply here"; posting in both is not wrong |
| Write for not-on-prod tickets | same ticket → Todo + comment | new ticket; In Validation (client card) | card rule 5 (68dabfe9bc2e8b969782e22d) |
| Leonard's access | share the register, commenter | share the folder; editor | Leonard's email douglas@harmonygames.co/1844721277206562572 "Comment access please, I don't need to edit" |

### Reach table (load-bearing records)

Base records verified with `persona_view.py can-see douglas …` (lines pasted in §12). Planned seeds are verified at the injection
gate (`check-sql`): the DM is Douglas's, #zombie-match3d has him as a member, both emails are in his mailbox, the doc and the deploy log
are his, the freeze event has a copy on his calendar, the beta folder is shared with him as writer; Linear, GitHub, Trello and
Confluence are unscoped. LB = load-bearing.

| Record | Service | Verdict | LB |
|---|---|---|---|
| D079SNE2TL4/1759256193.859279 | slack | YES (im member) | LB |
| D079SNE2TL4/1759269524.769369 | slack | YES | LB |
| D079SNE2TL4/1757351863.576949 | slack | YES | LB |
| D079SNE2TL4/1757355159.852859 | slack | YES | LB |
| D079SNE2TL4/1757449699.464389 | slack | YES | LB |
| D079SNE2TL4/1758040504.640159 | slack | YES | LB |
| D079SNE2TL4/1758649466.661059 | slack | YES | supporting |
| D05QQF7V404/1757975508.211599 | slack | YES (im member) | supporting |
| C08R27X0EAH/1757307297.870139 | slack | YES (zombie-bugs member) | supporting |
| ZOM-503 | linear | YES (unscoped) | LB |
| page_cicd_pipeline | confluence | YES (unscoped) | LB |
| 68d1eb90bef538c7c5c5599d | trello | YES (unscoped) | supporting |

**Feasibility.** Writes exist in `Evals/references/tools/catalog.json`: `gsheets_create_spreadsheet` then `gdrive_move_file` (or
`gdrive_create_file` with `parentId`), `gsheets_values_update`, `gdrive_share_file` (role commenter), `slack_send_message`
(D05QQF7V404), `linear_update_issue` (state "Todo"), `linear_create_comment`. Reads: `linear_list_comments`, `github_get_issue_comments`
(conversation comments; `github_get_pull_request_comments` returns inline review comments — review B), `github_get_pull_request_reviews`,
`gcal_list_events`, `trello_get_card`, `confluence_search`/`confluence_get_page`. Douglas is a writer on d_69fcebc484d472907b0b5c (record
plan). Values are categorical (Y/N) and PR numbers.

**Explicit rules.** Window (rule 1 + log row); parents (rule 1); server change (rule 1 + comment); exclusion and count (email); on prod
(doc: prod branch, prod: comment, prior Approve by someone else, rollback any time, merged ≠ prod); freeze (doc + calendar: Arthur's
Approve); aggregation (rule 4); write end state (rule 5); destination (rule 6 → ZM beta page → folder); share (Leonard: commenter). "Now"
is the clock. Every cross-reference postdates its target: the card (Sep 29 17:20Z) postdates the log (Aug 25), the doc (Sep 25), the ZM
beta page (17:15Z) and the folder (17:12Z); the doc's edit (Sep 25) postdates the freeze event (Sep 22/23); the comment, emails and ask
postdate the card; the #50 thread (Sep 27) postdates #50; Douglas's claim (Sep 22) postdates #41 and #51.

**Precedence (carrier eligibility).** Load-bearing facts sit in ● carriers only (Slack messages and replies, Trello description and
comment, Gmail body, Docs body, Sheets values, GCal start/end fields, Drive metadata, Confluence body, Linear comments —
`references/Ask_Carriers.md` §5 as amended by §6b — GitHub PR comments and reviews). The freeze event's description is supporting only.

**Prompt naturalness.** The human's trigger should name the anchors (Arthur's sign-off ask in the DM; Leonard's go/no-go email) and the
deliverable kind; it must not list the tickets, the PRs, the rules, the freeze, the cut, the doc, the folder or where any of them live.

**Grading devices** (for the human's rubric later): the exact 16-ticket set (spot checks ≤ 5 per group + a row-count criterion);
on-prod values for the decisive rows (ZOM-392, ZOM-518, ZOM-550, ZOM-503, ZOM-557, ZOM-499, ZOM-487, ZOM-444); the count 8 and the eight
keys in the reply; the eight Todo moves and comments; no new tickets; the register's folder; Leonard's commenter share.

## 11 Record plan for /create-injection

| Row(s) | Table | Id / key | Time (UTC) | Owner / author | Notes |
|---|---|---|---|---|---|
| 1 | slack.slack_messages | C0880U9751A/1748450537.204611 | 2025-05-28T16:42:17Z | Oliver | S_OLIVER_MERGED |
| 2 | slack.slack_messages | C0880U9751A/1758295268.611352 | 2025-09-19T15:21:08Z | Arthur | S_FREEZE_MON |
| 3 | slack.slack_messages | D05QQF7V404/1758571837.284511 | 2025-09-22T20:10:37Z | Douglas | S_DG_CLAIM |
| 4–6 | slack.slack_messages | C0880U9751A/1758937233.118904 (+ reply /1758938751.402267, + Douglas "ok") | 2025-09-27T01:40–02:07Z | Douglas, Arthur | thread; parent counters reply_count 2 |
| 7 | slack.slack_messages | C0880U9751A/1758991212.775031 | 2025-09-27T16:40:12Z | Oliver | S_OLIVER_SUM |
| 8 | slack.slack_messages | C0880U9751A/1759253506.093318 | 2025-09-30T17:31:46Z | Oliver | S_OLIVER_POST |
| 9 | slack.slack_messages | D05QQF7V404/1759266764.508127 | 2025-09-30T21:12:44Z | Arthur | S_ASK (anchor) |
| 10–11 | trello cards + createCard | 68dabfe9bc2e8b969782e22d / 68dabfe93a26ef2186dcec1c | 2025-09-29T17:20:41Z | Arthur (2162c1ba310341bf318f48b7) | board 6851a6569f3bf818760632ab, list 6851a674975da1fe76e70d93; H1_TITLE/H1_DESC; badges.comments 1 |
| 12–13 | trello cards + createCard | 68dac311754b38be05be7ea9 / 68dac311a286768d02a6385d | 2025-09-29T17:34:09Z | Arthur | CLIENT_TITLE/CLIENT_DESC |
| 14 | trello actions commentCard | 68dbf1b73eba0ba580f67a6e | 2025-09-30T15:05:27Z | Arthur | H1_CMT; card dateLastActivity = comment time |
| 15–20 | gmail threads + messages | douglas@harmonygames.co/1844719216755416739 (+ blake@ sent, oliver@ cc copies) | 2025-09-30T19:42:18Z | Arthur → Douglas cc Oliver | G_AMEND_* |
| 21–26 | gmail threads + messages | douglas@harmonygames.co/1844721277206562572 (+ leonard@ sent, blake@ cc copies) | 2025-09-30T20:15:03Z | Leonard → Douglas cc Arthur | G_LEO_* (anchor A2) |
| 27–28 | gdrive + gdocs | f_470ae81236d5bd39045dc1 | created 2025-06-01T18:30Z, modified 2025-09-25T16:40Z | Douglas | DOC_*; shared Arthur, Oliver, Vincent (reader) |
| 29–32 | gdrive + gsheets (2 tabs) | f_78bedc46245090a160d2dd | created 2025-08-25T12:05Z, modified 2025-09-11T16:35Z | Douglas | Prod deploys: "2025-08-25 11:52 UTC · beta prod cut · prod branch from main (#37, #38)", then #39 (09-02 17:30), #41 (09-03 16:30), #43 (09-04 12:50), #42 + #44 (09-08 17:18), #46 (09-09 20:29), #45 (09-10 18:20); Console & imports: plague race bot names (console, prod, 2025-08-28), Zombie Lane rewards (import, prod, 2025-09-08 16:45), algo levels 2.0 pack (import, dev, 2025-09-11 16:30) — no ticket keys |
| 33–37 | gcal.gcal_events | evt_b6eda0097a341f225ad5d2 (Arthur, organizer), evt_0f489eb7fb46ada9660881 (Douglas), Oliver, Owen, Vincent copies | start 2025-09-26T22:00Z; created 2025-09-22T14:02Z; updated 2025-09-23T16:05Z | Arthur | GCAL_SUMMARY/GCAL_DESC; ical_uid 463338c3d4e070df180b0269037ee17f@hg4 |
| 38–39 | gdrive folders | d_69fcebc484d472907b0b5c "ZM Beta sign-off"; d_d71300168ca5dffa4db8b3 "ZM Beta sign-off - client QA" | 2025-09-29T17:12Z / 17:05Z | Arthur (Douglas, Oliver, Vincent writers) / Oliver (Douglas reader) | Leonard not shared on either |
| 40–43 | confluence pages + versions | page_zm_beta_oct10; page_dd_launch_server_signoff (space_OPS, parent page_ops_home) | 2025-09-29T17:15Z; 2025-05-12T15:04Z | Arthur (user_EMPLOYEE_0025) | version 1 each |
| 44–61 | github pull_requests + branches | match3d-backend#37 … #54 (18 PRs) | per `minted_ids.json` PRS | Douglas / contractor | base_ref main; no ZOM key in title/body/branch; #40 title "Items: make the cooler a usable item" |
| 62–~120 | github pr_comments + timeline (commented) | #n#c_1 CodeRabbit walkthrough on every PR; #n#c_2… prod:/rollback:/dev notes; Vincent "works on dev" on #51 | per `minted_ids.json` | CodeRabbit / deployer | each with a 'commented' timeline event; PR updated_at bumped |
| ~121–160 | github reviews + timeline (reviewed) | #n#rev_1 CodeRabbit COMMENTED on every PR; #n#rev_2… peer/Arthur reviews (APPROVED, CHANGES_REQUESTED, COMMENTED "looks fine, ship it after go/no-go" on #50) | per `minted_ids.json` | CodeRabbit, Douglas, contractor, Arthur | — |
| ~161–250 | linear.linear_comments | 73 cohort tickets (19 decisive in LIN_NOTES + 54 neutral) + 4 non-cohort tickets that are Done in the base (ZOM-461, ZOM-480, ZOM-479, ZOM-489); never on open tickets, whose state a fixed/checked note would contradict | after each ticket's own events, before its completed_at (cohort) | ticket owners / Vincent / Douglas | neutral: "client side, in Android 0.3.12x — nothing needed in match3d-backend", art drop, VFX in scene; decisive: "backend part is match3d-backend#n" or "needs the Zombie Lane rewards imported on the backend" |
| — | linear.linear_issues | no UPDATE: every comment sits before its ticket's completed_at | — | — | no state/stamp changes |

About 250 inserted rows over 10 injected services (slack, trello, gmail, gdocs, gsheets, gdrive, gcal, confluence, github, linear) —
≥ 120 rows and ≥ 10 injected services for the long profile. Snowflake, Slides and Contacts are not touched.

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| github | INT-01 | GitHub Slack app mirror | none: match3d-backend is not a mirrored repo (36 base PRs, no copies in #engineering-bots C050WGU41HR or #zombie-prs C093LEZGF6J) |
| github | INT-23 | CodeRabbit walkthrough comment + COMMENTED review | seeded on every PR (#c_1, #rev_1), as on base match3d-backend#14 |
| github | INT-03 | linear[bot] PR comment | none: seeded PRs name no Linear key in title/branch/body (base match3d-backend convention) |
| github | INT-12 | GitHub notification mails | optional; not seeded (integration exception if base_check asks) |
| linear | INT-04 | Linear Slack app posts | none: comments are not posted by the Linear app (base posts creations/assignments only) |
| linear | INT-05 | Linear e-mail digests | none: digests are optional |
| gcal | INT-11 | invitation mails | none for the freeze event (Arthur's internal hold; integration exception "no_notify") |
| gdrive | INT-13 | Drive Slack DM on share | none: base shares from Arthur to Douglas in Sep carry no Drive DM |
| trello | INT-21 | Trello → Slack | none: no Trello integration exists |
| slack | INT-22 | Slack e-mail notification | none: optional |
| gmail | — | gmail: none (no integration originates in Gmail) | one copy per mailbox under the base file aliases |
| gsheets / gdocs | INT-13 | covered with gdrive | — |
| confluence | — | confluence: none in integrations.json | — |

## 12 Self-test results

`python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.draft.json --design` (verbatim):

```
HARDNESS GATE (long (design)): PASS
  [ok] effective_profile: effective_profile 'long' for 'Long Horizon' → thresholds 'long'
  [ok] sql_lint_clean: skipped (--design: no SQL yet)
  [ok] base_consistency: skipped (--design: no SQL yet)
  [ok] services_injected: skipped (--design: no SQL yet)
  [ok] rows: skipped (--design: no SQL yet)
  [ok] services_carrying_weight: 10 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: skipped (--design: no SQL yet)
  [ok] seeded_ids_exist_in_sql: skipped (--design: no SQL yet)
  [ok] anchors: 2 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 13 fragments; need ≥ 12
  [ok] ask_fragment_services: 10 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 11 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 7 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 73; need ≥ 30 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 2 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 100; need ≥ 30
  [ok] call_budget: unconditional (verified) floor 139 of 139 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 100 (Long Horizon; plan ~600 for headroom)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 47% (≤ 50%)
  [ok] traps: 22 traps across 9 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 7 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (3 with versions in ≥ 2 services, 2 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 7 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 10 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 8 chains with 8 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] hidden_authorities: 2 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 7 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 7 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 5 writes over 4 services; each must depend on findings
```

`persona_view.py can-see` for the base records in the reach table (verbatim):

```
douglas slack D079SNE2TL4/1759256193.859279: YES
douglas slack D079SNE2TL4/1759269524.769369: YES
douglas slack D079SNE2TL4/1757351863.576949: YES
douglas slack D079SNE2TL4/1757355159.852859: YES
douglas slack D079SNE2TL4/1757449699.464389: YES
douglas slack D079SNE2TL4/1758040504.640159: YES
douglas slack D079SNE2TL4/1758649466.661059: YES
douglas slack D05QQF7V404/1757975508.211599: YES
douglas slack C08R27X0EAH/1757307297.870139: YES
douglas linear ZOM-503: YES
douglas confluence page_cicd_pipeline: YES
douglas trello 68d1eb90bef538c7c5c5599d: YES
```

**Lazy-solver pass** (one broad search per service, first hits, no replies, stop at the first conclusion, every bulk shortcut):
- Reads the ask and Douglas's own claim in the same DM, then Oliver's summary → everything on prod. Eight rows wrong.
- Lists Done ZOM tickets in September by title and guesses the server ones → misses ZOM-336, ZOM-444, ZOM-459, ZOM-510/256; includes
  ZOM-547/553 and maybe ZOM-555 or ZOM-461.
- Reads the card description only → no imports; In Validation from the client card if it opens that first.
- Uses merge state or the deploy log's Prod deploys tab → ZOM-336/435 Y; ZOM-487/444 N; ZOM-392/518 Y.
- Reads prod: comments but no reviews → ZOM-392, ZOM-518, ZOM-550, ZOM-503 Y.
- Never opens Calendar → Monday freeze → ZOM-550 Y; reads the #50 parent only → ZOM-550 Y.
- Bulk shortcut check: no list or search returns Linear comments (`linear_show_data` unverified — see Unresolved); no Slack mirror of
  match3d-backend; `in:comments` searches return PR lists, not deploy/approval times; the deploy log stops on Sep 10 and names no tickets;
  no record lists the 16 tickets.

**Literal-value sweep** (planned; re-run at injection on the SQL): "11:52" only in the deploy log's first row and the two cut-day prod:
comments; "22:00" for the freeze only on the calendar event; "Approve review" only in the doc; ZOM-547/ZOM-553 only in the email and
their own comments; no record lists "8" on prod or the eight keys. **Wording sweep:** the card says "server change"; comments say
"backend part" / "nothing needed in match3d-backend"; PR notes use the doc's keywords as raw events with times; Arthur's #50 review says
"looks fine, ship it after go/no-go" (a COMMENTED state, not a verdict). **"The rest stands" check:** no record after the comment
narrows rule 1 back; no record after the email re-adds ZOM-547/553.

### Self-review

Re-read `Evals/1_Prompt_Eval.md` §2.1 (Unique Ground Truth), §2.2 (Feasibility), §3.2 (Cross-Service Coherence),
`Evals/0_Injection_Quality_Eval.md` Check C and `references/Docs/11_V3_Changes.md`, then walked the design in order. Re-read every
load-bearing base value from the exports this session (Linear cohort timestamps and owners, match3d-backend PRs #1–#36 with reviews and
CodeRabbit comments, the Douglas–Vincent DM Sep 8–30 deploy messages, Confluence page_cicd_pipeline and page_nakama_setup, the ZM ROADMAP
board).

| # | Check / category | Verdict | Counter-reading (strongest argument the other way) | Resolution with evidence |
|---|---|---|---|---|
| 1 | temporal | PASS | seeded PRs #37–#54 (Aug–Sep) sit above base #36 (Oct 12) — numbers out of time order | #36 is post-clock (L13), invisible at the Oct 1 freeze; harmonygames-Games/match3d-backend#36 not cited |
| 2 | temporal (base deploys) | PASS | base DMs date the economy deploy Sep 9 and the profile deploy Sep 8, before v1's PRs existed (review A) | v2 PRs sit on those events: #46 prod 20:29Z Sep 9 (D079SNE2TL4/1757449699.464389), #44 17:18Z Sep 8 (/1757355159.852859), #48 16:35Z Sep 16 (/1758040504.640159) |
| 3 | temporal (chronology) | PASS | the card cites the log, the doc and the ZM beta page; a reference could predate its target | log 2025-08-25T12:05Z, doc 2025-09-25T16:40Z, page 2025-09-29T17:15Z, card 17:20:41Z (`minted_ids.json`) |
| 4 | semantic | PASS | "server change" could include a client build calling a new endpoint | rule 1 defines it; comments name the PR (ZOM-503 comment) |
| 5 | semantic (art props) | PASS | ZOM-336 "Cooler" is an art drop; its nine siblings would follow a plural PR (review A) | #40 is singular ("make the cooler a usable item"); sibling comments say nothing needed in match3d-backend; base ZOM-518 shows item data lives server-side |
| 6 | cross-service referential | PASS | the email cites #49 and #53; a dropped seed dangles | both planned (`minted_ids.json` PRS 49, 53) |
| 7 | cross-service referential (mirror) | PASS | PR comments without a Slack copy fail INT-01 | match3d-backend has no mirror (R07; 36 base PRs) |
| 8 | quantitative | PASS | the deploy log's Prod deploys tab disagrees with the PR record | the tab stops on Sep 10 and every row agrees (f_78bedc46245090a160d2dd); H2 calls it a quick list |
| 9 | quantitative (counts) | PASS | 8/8 depends on whether ZOM-547/553 count | email: "not part of the count either way"; 16 rows (§2) |
| 10 | state/lifecycle | PASS | Douglas deployed the teams changes Sep 30 and Vincent confirmed, so ZOM-503 is on prod | D079SNE2TL4/1759256193.859279 is #52's deploy inside the freeze with only the contractor's approval; H2: does not count |
| 11 | state/lifecycle (prod model) | PASS | each prod deploy ships all of main, so later deploys carry #40, #51 (review A blocker 2) | H2: prod runs from the prod branch with per-PR picks; only picked PRs are on prod (planned_text.json DOC_BODY) |
| 12 | state/lifecycle (reviews) | PASS | base PRs have peer approvals and CodeRabbit; seeds without them look planted (review A) | every seed gets CodeRabbit #c_1/#rev_1 and peer reviews; base pattern match3d-backend#14 |
| 13 | identifier/format | PASS | seeded Trello ids could break the timestamp scheme (T06/I16) | minted from their own timestamps: 68dabfe9bc2e8b969782e22d → 2025-09-29T17:20:41Z |
| 14 | identifier/format (PR vs repo) | PASS | "#50" in Slack could mean match3d#50 | the message says "match3d-backend#50" (C0880U9751A/1758937233.118904); N02 |
| 15 | other (persona plausibility) | PASS | Douglas deployed much of this himself, so "retrieval" is odd | the contractor deploys half (PERSON_2967, P04), approvals and freezes span days, QA closes tickets, and Douglas's own Sep 22 claim (D05QQF7V404/1758571837.284511) is wrong |
| 16 | other (wrong summaries) | PASS | Oliver and Douglas contradicting the PR record read as inconsistencies | dated human claims (C0880U9751A/1758991212.775031; D05QQF7V404/1758571837.284511); Atlas rule 12 |
| DP1 | two-reading: window start | PASS | September only, or all of Aug 25 | card rule 1 + log row (f_78bedc46245090a160d2dd); ZOM-461 11:51:48 |
| DP2 | two-reading: ZOM-457 | PASS | closed after the cut | card rule 1 parents (68dabfe9bc2e8b969782e22d) |
| DP3 | two-reading: ZOM-336 | PASS | art is client-only | ZOM-336 comment names match3d-backend#40 |
| DP4 | two-reading: imports | PASS | dev import is not a server change (review A blocker 1) | comment 68dbf1b73eba0ba580f67a6e "imports on the backend", no target condition |
| DP5 | two-reading: ZOM-547/553 | PASS | they have PRs | email douglas@harmonygames.co/1844719216755416739 |
| DP6 | two-reading: ZOM-550 in scope | PASS | boss arena = excluded | email names only two keys (douglas@harmonygames.co/1844719216755416739) |
| DP7 | two-reading: merged = prod | PASS | Oliver's May claim | doc f_470ae81236d5bd39045dc1; page_cicd_pipeline |
| DP8 | two-reading: prod carries main | PASS | later deploys ship earlier merges | DOC_BODY prod branch (planned_text.json) |
| DP9 | two-reading: ZOM-392 | PASS | deployed and approved | match3d-backend#41#rev_2 at 18:05 after the 16:30 prod: |
| DP10 | two-reading: ZOM-518 | PASS | has a review | match3d-backend#43 only CodeRabbit COMMENTED |
| DP11 | two-reading: ZOM-499 | PASS | rolled back → N | match3d-backend#44#c_4 newer prod: |
| DP12 | two-reading: freeze | PASS | Monday | evt_0f489eb7fb46ada9660881 updated Sep 23 |
| DP13 | two-reading: ZOM-550 | PASS | "go ahead"; approved; reviewed | reply C0880U9751A/1758938751.402267; match3d-backend#50#rev_3 COMMENTED |
| DP14 | two-reading: ZOM-444 | PASS | freeze deploys roll back | match3d-backend#47#rev_2 APPROVED by Arthur first |
| DP15 | two-reading: ZOM-503 | PASS | Vincent confirmed Sep 30 | D079SNE2TL4/1759269524.769369 vs match3d-backend#52 approval by the contractor only |
| DP16 | two-reading: ZOM-557 rollback in freeze | PASS | unapproved rollback doesn't count | DOC_BODY "whenever it happens, freeze or not" (planned_text.json) |
| DP17 | two-reading: ZOM-487 | PASS | missing from the log tab | match3d-backend#48 prod: Sep 16; D079SNE2TL4/1758040504.640159 |
| DP18 | two-reading: reply | PASS | post in the channel | ask D05QQF7V404/1759266764.508127 "reply here" |
| DP19 | two-reading: write | PASS | new ticket / In Validation | card rule 5 (68dabfe9bc2e8b969782e22d) |
| DP20 | two-reading: share | PASS | folder or editor | Leonard's email douglas@harmonygames.co/1844721277206562572 |

HARDNESS GATE output: pasted above (long, design PASS).

Unresolved: (1) `linear_show_data` and `linear_list_issues(query)` matching comment text are unverified (Ask_Carriers [U]); if either
returns comment bodies in bulk, the 73-call surface collapses — probe at the Opus pre-check, and if so move per-ticket evidence into PR
reviews/timeline. (2) The 139-call budget against the author's 130–150 per run is measured only at the pre-check. (3) Whether the
platform renders tickets whose state changed after the clock (none in the cohort) is unverified. (4) Findability of the seeded H1/H2
records is proven at injection. (5) Review B predicted 74–84% for v1; v2 adds four approval-decided rows, a 12-second cut, a persona
self-claim and a QA-confirmed unapproved deploy — the new prediction (~62–72%) is unverified until the pre-check.

```
STAGE GATE scenario: PASS — Task_Authoring-2/task_inputs · 01_Scenario_Design.md#66967771208f · 01_Hardness_Manifest.draft.json#781b05e72482 · blocking 0 · warnings 0 · checks 26
[PASS] structure.outputs: 2 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 18/18 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 25/25 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 2/2 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 15/15 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 22/22 items carry a source pointer (min 90%)
[PASS] evidence.record_plan: 32/35 items carry a source pointer (min 80%); unsourced e.g. L575: "— | linear.linear_issues | no UPDATE: every comment sits before its ticket's completed_at "
[PASS] evidence.active_speakers: 11/11 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for douglas@harmonygames.co and matches the re-run (124 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 18 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 11 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (10 INT ids, services ['confluence', 'gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'linear', 'slack', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts ['LIN-DQ13', 'LIN-DQ14']; trap_catalog ['B03', 'C01', 'C02', 'D04', 'K02', 'N01']
[PASS] boundary.anchor_naming: 4 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: dual red team present (01b_Redteam_Review.md + .second.md)
[PASS] reach.scenario: 11 scoped load-bearing ids YES for douglas (1 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 36 evidenced counter-readings (of 36 found; need ≥ 27) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```













## 13 Red team (dual)

RED TEAM UNAVAILABLE: redteam_review: set REDTEAM_MODEL or pass --model (no REDTEAM_* environment configured — error)

Substitute (dual): two independent reviewers (fresh subagents given only the v1 design, manifest, `planned_text.json`,
`minted_ids.json`, `cohort.json`, the eval rules, the tool catalog and read access to the base) red-teamed v1. Reviewer A (validity and
coherence) → `01b_Redteam_Review.md` (25 findings: 2 Blocker, 10 Major, 13 Minor); reviewer B (difficulty and volume) →
`01b_Redteam_Review.second.md` (12 findings). Every finding was re-checked against the base before acting:

| Finding | Source | Disposition with evidence |
|---|---|---|
| A-B1 "imports into the prod tables" excludes the dev-only import ZOM-256 | 01b_Redteam_Review.md | fixed: comment reads "spreadsheet imports on the backend count as server changes too" (68dbf1b73eba0ba580f67a6e, planned_text.json H1_CMT) |
| A-B2 whole-main prod deploys carry earlier merges, contradicting five N rows | 01b_Redteam_Review.md | fixed: H2 now runs prod from a prod branch with per-PR picks (planned_text.json DOC_BODY); rollback reverts the pick |
| A-M "main deploys to dev" contradicts page_cicd_pipeline and Douglas's hand dev deploys | 01b_Redteam_Review.md | verified (D079SNE2TL4/1757526116.670019); fixed: "Merging doesn't deploy anything. Dev is deployed by hand from main" |
| A-M base deploy times (ZOM-537 Sep 9; Sep 8 profile; Sep 16 "these two") | 01b_Redteam_Review.md | verified (D079SNE2TL4/1757449699.464389, /1757355159.852859, /1758040504.640159); fixed: PR timeline rebuilt on those events (§2 truth table) |
| A-M rollback inside the freeze | 01b_Redteam_Review.md | fixed: H2 "A rollback takes the PR off prod whenever it happens, freeze or not" (planned_text.json DOC_BODY) |
| A-M ZOM-336 siblings / plural PR | 01b_Redteam_Review.md | fixed: #40 singular title; sibling comments say nothing needed in match3d-backend (ZOM-336 comment, `minted_ids.json`) |
| A-M parent ZOM-457 | 01b_Redteam_Review.md | fixed: card rule 1 "Parent tickets don't get a row of their own" (68dabfe9bc2e8b969782e22d) |
| A-M "comment access is enough" allows editor | 01b_Redteam_Review.md | fixed: "Comment access please, I don't need to edit" (planned_text.json G_LEO_BODY) |
| A-M / B-Major `in:comments` search collapses PR comment reads | both | partly: the search returns PR lists, not the comment times that decide freeze and approval comparisons, and match3d-backend#44 defeats "prod minus rollback"; reviews (13) are per PR only; residual risk in Unresolved |
| A-M / B-Blocker `linear_show_data` / `linear_list_issues(query)` may return comments in bulk | both | unverified tool behaviour (Ask_Carriers [U]); neutral comments also mention match3d-backend so a keyword query returns half the cohort; probe at pre-check (Unresolved 1) |
| A-M base review conventions (peer approvals, CodeRabbit); #5 pointer wrong | 01b_Redteam_Review.md | verified (match3d-backend reviews: Douglas 15 APPROVED, contractor 15 APPROVED, CodeRabbit 11 COMMENTED); fixed: CodeRabbit #c_1/#rev_1 on every seed; pointer corrected (match3d-backend#5 approved; match3d-backend#14 for CodeRabbit) |
| A-M wording not planned for Linear comments, PR titles/comments, log rows | 01b_Redteam_Review.md | partly: patterns and decisive texts fixed in §11 and `minted_ids.json`; full wording generated at injection and reviewed there |
| A-minor Vincent's Sep 30 confirmation not cited | 01b_Redteam_Review.md | fixed: two-reading row + C3 (D079SNE2TL4/1759269524.769369) |
| A-minor email reason doesn't fit ZOM-553; count unclear | 01b_Redteam_Review.md | fixed: "balance and refill/nuke values … not part of the count either way" (planned_text.json G_AMEND_BODY) |
| A-minor no "beta calendar" exists | 01b_Redteam_Review.md | fixed: doc says "the server freeze on the calendar" (K6 quote updated; evt_0f489eb7fb46ada9660881) |
| A-minor Douglas's planned times outside his posting hours (15:00–03:59Z) | 01b_Redteam_Review.md | fixed: every Douglas event moved into his hours; cut-day deploys are the contractor's (`minted_ids.json` PRS) |
| A-minor Gmail mailbox keys | 01b_Redteam_Review.md | fixed in §11: copies under blake@/oliver@/leonard@ aliases (I03) |
| A-minor self-advertising decoys / "go ahead on dev" states the answer | 01b_Redteam_Review.md | partly: the reply's "on dev" is the A14 narrowing the mechanism needs (C01/C02; C0880U9751A/1758938751.402267); #50's review text no longer gives a verdict |
| B-Blocker wrong GitHub tool (pull_request_comments returns inline review comments) | 01b_Redteam_Review.second.md | accepted: surface and budget use `github_get_issue_comments` (manifest cohort surface 2; catalog.json) |
| B-Major lean run under 130; rows collapse (decoys, card actions, status lookup, PR list, sheet create+move) | 01b_Redteam_Review.second.md | fixed: those rows removed; 13 honest review reads added via the approval rule; floor 139 (§9) |
| B-Major imports tab names the tickets | 01b_Redteam_Review.second.md | fixed: rows name what was imported, not the ticket (f_78bedc46245090a160d2dd plan, §11); the join is via the ticket comment |
| B-Major cut trap weak (no candidate on Aug 22 afternoon) | 01b_Redteam_Review.second.md | fixed: cut 2025-08-25 11:52 between ZOM-461 (11:51:48) and ZOM-459 (11:53:11) |
| B-Major predicted 74–84%; ways under 75% | 01b_Redteam_Review.second.md | applied: approval rule on every prod deploy (+4 decided rows), better cut, a same-persona claim (D05QQF7V404/1758571837.284511), a later QA confirmation that does not change the answer (ZOM-503) |
| B-Major bimodality (77-read surface, GitHub tool) | 01b_Redteam_Review.second.md | mitigated: approval rows add a third independent surface; wrong-tool runs recover via `get_issue_comments`; watched at baseline (SD band, `cohort.json`) |
| B-Minor cohort.json parents missing | 01b_Redteam_Review.second.md | not reproduced: `cohort.json` carries parent ids (10 × ZOM-97, ZOM-459 → ZOM-457) |

## 14 Hardening round 1 (design delta from `01a_Hardening_Report.md`, MODE B on the six baseline runs)

The six baseline runs (134–193 calls) beat every rule trap and failed one fact the same way in all six: Arthur's separate amendment mail was never searched. Three independent decisive facts now sit behind the three reading habits on which the runs split. Each fact flips different register rows.

| Node | Records | Root cause | Rows it decides | Baseline habit it rides |
|---|---|---|---|---|
| K4 / C6 (moved) | Arthur's reply-all inside Leonard's go/no-go thread, `douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>` in `douglas@harmonygames.co/1844721277206562572` | A14 (replies never opened) | ZOM-547, ZOM-553 off; counts | 3/6 runs read the thread (run-3 · step 10, run-4, run-6 `gmail_get_thread`), 3/6 read only Leonard's message (run-1, run-2, run-5 `gmail_get_message`) |
| K14 / C9 / T23 (new) | QA question `comment_zm_beta_oct10_c1` and Arthur's reply `comment_zm_beta_oct10_c2` on page_zm_beta_oct10; deploy-log row 'boss arena HP table' (dev, 2025-09-17 15:50) | A9 (response pairing) | ZOM-487 Y → N | 2/6 runs listed the page's comments (run-5 · step 15, run-6 · step 13) |
| K15 / C10 / T24 (new) | Arthur's thread reply on his ask, D05QQF7V404/1759267192.331870; deploy-log row 'economy table' (dev, 2025-09-16 14:20) | A14 (replies never opened) | ZOM-537 Y → N | every run printed reply_count from the DM history; none read a thread reply (no `slack_get_thread_replies` call in any run) |
| T12 / T13 (leak repaired) | match3d-backend#40 title 'Items: make the cooler a usable item' → 'Catalog: add usable item entries' (branch, commit and CodeRabbit text follow the title) | A18 (needles topical search cannot reach) | ZOM-336 membership | run-3 matched PR titles to ticket titles (25 comment reads instead of 73, run-3 · step 85–111) and still found ZOM-336 because the title named the cooler; the ticket's comment ('needs a catalog entry on the backend too: match3d-backend#40') is now the only link |

Ground truth after hardening: 16 rows, 6 on prod (ZOM-459, ZOM-509, ZOM-499, ZOM-531, ZOM-444, ZOM-510) and 10 not (ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-550, ZOM-435, ZOM-557, ZOM-256, ZOM-487, ZOM-537). Writes: 10 Todo moves, each with a comment. Call budget: 145 (manifest `call_budget`). Incorporation: K4 sits in the thread the prompt names (A2). K14 sits on the page that card rule 6 names (trello:68dabfe9bc2e8b969782e22d). K15 is the requester's own reply on the anchor (A1). Lazy-solver check: each new fact is out of reach of any bulk call. A Linear search on 'boss arena' returns five Done tickets in the window, and the two log rows name no ticket.

## 15 Hardening round 2 (design delta from `01a_Hardening_Report.md` §15, MODE B on the six round-1 baseline runs)

The round-1 baseline (six runs, 163–220 calls) measured the three round-1 levers:
- **K15, the Slack thread reply.** Read in 6/6 runs. Each run first called `slack_read_thread` with Arthur's user id (`channel_not_found`), then retried with D05QQF7V404 (run-1 · step 9, run-3 · step 10). The reply sat on the first message every run reads, with reply_count 1.
- **K4, the email thread.** Read in 5/6 runs. Only run-3 · step 17 used `gmail_get_message`.
- **K14, the page comments.** Read in 1/6 runs (run-6 · step 171).

The result was one dominant failure pattern (ZOM-487 wrong) in runs 1, 2, 4 and 5. Round 2 moves the ZOM-537 fact to a surface the runs split on.

| Node | Records | Root cause | Rows it decides | Round-1 baseline habit it rides |
|---|---|---|---|---|
| K15 / C10 / T24 (moved) | Arthur's inline review comment `harmonygames-Games/match3d-backend#46#rc_1` on lib/zombies_game/economy.ex, attached to his Approve `#46#rev_2` (2025-09-09T19:40:00Z); deploy-log row 'economy table' (dev, 2025-09-16 14:20) unchanged | A14 (replies never opened) | ZOM-537 Y → N | `github_get_pull_request_comments` on #46 in 1/6 runs (run-1 · step 69); run-2 read inline comments on #38–#41 only (run-2 · step 36–125); runs 3–6 never called it |
| Slack ask (reverted) | D05QQF7V404/1759266764.508127 is a plain message again (reply_count 0); the round-1 reply row is removed | none | none | removes the cue that every run followed |
| K4, K14 (kept) | as in §14 | A14, A9 | ZOM-547/553 off; ZOM-487 Y → N | 5/6 and 1/6 |

**Ground truth is unchanged:**
- 16 rows: 6 on prod and 10 not.
- 10 Todo moves, each with a comment.

**Call budget: 159.** This adds 15 inline-review-comment reads, one per in-scope server PR.

**Why the levers are independent:** they catch different runs. In round 1, run-6 caught K14 and run-1 caught K15, and neither caught the other.

**Patterns projected from round 1:**

| Runs | Missed | Share |
|---|---|---|
| run-1 | ZOM-487 | 1/6 |
| runs 2, 4, 5 | ZOM-487 and ZOM-537 | 3/6 |
| run-3 | ZOM-487, ZOM-537 and ZOM-547/553 | 1/6 |
| run-6 | ZOM-537 | 1/6 |

That gives 4 patterns, the largest 3/6 = 50%.

## 16 Hardening round 3 (design delta from `01a_Hardening_Report.md`, MODE B on the six round-2 baseline runs)

The round-2 baseline (six runs, 194–228 calls) applied every rule correctly. It split only on the hidden facts, and five runs missed all three the same way:
- **K4, the email thread.** Read in 1/6 runs (run-6). Runs 1–5 searched `from:leonard` and opened only Leonard's message with `gmail_get_message`.
- **K14, the page comments.** Read in 1/6 runs (run-6).
- **K15, the #46 inline comment.** Read in 0/6 runs. Runs 2 and 3 read inline comments on #37–#41 and #37–#42 only, then stopped.

Replayed through `tools/difficulty_stats.py` with an atomic per-ticket rubric (one status row per ticket, as `Evals/3_Rubrics_Eval.md` §2.2 requires), that baseline gives a per-run SD of about 0.02–0.05 and a 5/6 pattern. The SQL then fails two gates no matter how the rubric is weighted, because the 14 rule-decided tickets add rows every run passes. Round 3 therefore puts more rows behind the two habits that split runs across all three baselines (20 runs):
- Gmail `get_thread` on Leonard's thread: 3/7, 5/6 and 2/7 runs.
- Inline comments on the first PRs (#37–#42): 0/7, 2/6 and 2/7 runs.

| Node | Records | Root cause | Rows it decides | Habit it rides |
|---|---|---|---|---|
| K16 / C11 / T25, T26 (new) | Second point of Arthur's reply-all in Leonard's thread (same message): the analytics events table import is part of ZOM-444's and ZOM-436's server change, the loadout table import of ZOM-531's. Deploy-log rows 'analytics events table' (dev, 2025-09-12 19:20) and 'loadout table' (dev, 2025-09-10 17:40) | A7, A14 | ZOM-444 Y → N; ZOM-531 Y → N; ZOM-436 joins the register (N) | email thread, 10/20 |
| K17 / C12 / T27 (new) | Inline review comment on #38 by its approver, the contractor (lib/zombies_game/plague_race.ex, on rev_2, 2025-08-25T09:20Z); deploy-log row 'plague race table' (dev, 2025-08-26 10:30) | A14 | ZOM-459 Y → N | early inline comments, 4/20 |
| K18 / C13 / T28 (new) | Inline review comment on #39 by its approver, Douglas (lib/zombies_game/trophy_path.ex, on rev_2, 2025-09-02T15:20Z); deploy-log row 'trophy path copy table' (dev, 2025-09-02 18:05) | A14 | ZOM-509 Y → N | early inline comments, 4/20 |
| K4, K14, K15 (kept) | as in §14–§15 | A14, A9 | ZOM-547/553 off; ZOM-487 N; ZOM-537 N | 10/20, 4/20, 1/20 |

**Ground truth:**
- 17 rows: 2 on prod (ZOM-499, ZOM-510) and 15 not.
- 15 Todo moves, each with a comment.
- ZOM-547/553 stay off.

**Call budget: 175.** That is 30 Linear writes plus the observed discovery calls: Slack user lookup (2), GitHub repository and PR list (2), deploy-log tab list (1). The Linear writes are counted per record, because they scale one-to-one with the not-on-prod rows.

**Projection** (replay of all 20 runs, atomic per-ticket rubric, weights 1/3/5 by work; details in `01a_Hardening_Report.md` §2):
- Every 6-run subset of the three real batches (15 subsets): average 0.50–0.71, SD 0.10–0.16, largest pattern ≤ 50%. All three gates pass in 15/15.
- Resampled 6-run batches: P(average < 75%, SD 0.1–0.3 and patterns ≤ 50% all pass) ≈ 78%.
- The current SQL scores 0% on the same test.

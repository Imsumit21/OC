# Scenario Design — jl-zm-difficulty-baseline · design only · contains no prompt, OE or criterion text

Persona Julia Lawson (Product Manager, Product) · competency Engineering Ops · task skill Retrieval · horizon Long (platform
"Task Type": long-horizon) · difficulty mode medium (V3 cap: six-rollout average strictly under 85%; the author's target is under
75%, design target about 62–65%) · universe date October 1, 2025 (V3 freeze 00:00 UTC = Tue Sep 30, 2025 5:00 PM PT; every base
record dated after it is treated as not yet existing). **Design v5** (after `/injection` attempt 6adfee3ef9092601a61245bb: Confluence removed, decoy card re-dated) — v4 rebuilt after the dual red team and a re-check against the match3d git history (§13): no seeded note claims
which files a ticket changed (an agent can read the history with `github_get_file_history` / `github_get_commit_files`); membership
is a human tag in Blake's notes; the promotion-window, global-enrage, MF35, remote-flag and dev-define claims are gone; every value on
the enrage sheet is the prefab value at the clock. Builder scripts: `support/task_work/jl_difficulty/` (`build_design.py`
computes candidates and per-ticket truth from the Linear export into `truth.json`, mints every seeded id into `minted_ids.json` and
writes the seeded wording into `planned_text.json`; `build_manifest.py` writes the draft manifest; v1–v3 kept as `*_v1.py` … `*_v3.py`).
Reference design: the completed Douglas task (`support/completed_tasks/douglas_beta_server_signoff_2026-10-28/`, 56% after hardening);
this task avoids its cohort (ZOM tickets Done Aug 25 – Sep 30) and storyline.

## 0 Assignment, persona census and horizon note

| Field | Assigned (verbatim, `00_Assigments.md`) | Resolution |
|---|---|---|
| persona | Julia Lawson | roster `julia_lawson`, julia.lawson@harmonygames.co, Product (`Evals/references/persona/roster.json`) |
| role | Product Manager | owns the Zombie Match 3D level funnel (C090N54TG79/1758689839.300009 "I will stop level making at 300 … more content for September 30 release") and the per-monster enrage tuning (C08R27X0EAH/1756922765.033199 Robert: "she also change how monsters enrage. Every monster will enrage differently in terms of speed + dmg") |
| business function | Product | Evals category Product & Design (`Evals/references/rules/task_categories.md`) |
| competency | Engineering Ops | what actually shipped to players in the store builds vs what is only tooling or replaced, and where ticket text and the build disagree — release-state retrieval |
| task skill | Retrieval | 109 candidate tickets × their Linear notes, a rules card + amendment, a build mail + reply, a per-monster sheet, a Slides deck + Blake's #zombie-design message, the full ZOM-42 spec, a calendar invite, an agenda doc, three PRs, assembled into one register |
| horizon | long-horizon | manifest `horizon: Long Horizon`, `effective_profile: long` with `profile_exception` (author's ≥ 120-call target) |
| universe date | October 1, 2025 07:00 | built on the Oct 1, 2025 freeze, read as 00:00 UTC (V3 §3); latest seed 2025-09-30T19:48:26Z (the ask) |
| difficulty mode | medium | author target: average under 75% (design ~62–65%), pass@1 ≤ 2 of 6, ≥ 2 failure patterns (largest ≤ 50%), per-rollout SD 0.1–0.3 |

**Remit argument.** Julia builds and balances the Zombie Match 3D levels and their funnel: she replays the first levels after balance
changes (CC43664F351E/1756987085.230719), argues where difficulty should come from (C090N54TG79/1757610131.672669 "I prefer the difficulty
increase to come from monsters primarily"), set the per-monster enrage values (C08R27X0EAH/1756922765.033199), and adjusted the level
difficulty labels herself (match3d commits 737e0278 "0-20 difficulty label adjustment" and 37aaef73 "20-50 difficulty labels adjusted",
2025-09-15, author PERSON_0005 = Julia). On Sep 2 balance changes reached the store build without a QA check (C090N54TG79/1756751169.213249,
/1756751373.593569); on Sep 3 Leonard asks to adjust rage per level (C08R27X0EAH/1756922313.032399); on Sep 26 Robert explains tier moves
(C0880U9751A/1758921802.962539); on Sep 29 Robert asks "what 0.3.22 had and what we're keeping" (C090N54TG79/1759176983.189479). A baseline
of what the difficulty system actually does in the builds players have — before Monday's tuning — is the Engineering Ops retrieval a PM is
pulled into on Sep 30.

**Effective profile.** Long Horizon → normally `extreme` (≥ 500 calls, plan ~600). The requester set a hard minimum of 120 tool
calls in every run and an average under 75% (`00_Assigments.md` "Author targets", chat 2026-10-30), which an extreme design
overshoots ~4×. The manifest uses the gate's `long` profile (extreme breadth, authorities, chains and traps; 100-call floor) with
`profile_exception {reason, requester_confirmation}` quoting the requester. Necessary budget: **147 unconditional calls** (§9). Reviewer
B measured a lean correct run at ~165 and a typical Opus run at ~175–210 calls from the Douglas/Robert trajectories (§13).

Persona reach census (`python3 Task_Authoring/tools/persona_view.py reach julia_lawson --top 10`, verbatim):

```
REACH  Julia Lawson <julia.lawson@harmonygames.co>  Product Manager / Product
clock 2025-10-01

SLACK  user=EMPLOYEE_0005_SLACK_ID  visible channels=158 {'mpim': 52, 'public': 26, 'private': 53, 'im': 27}  messages=267537  public-not-member (UNVERIFIED)=44
  persona posts=34047 last post=2026-02-12  last activity in visible channels=2026-02-13
  C05433XK267    builds                                 public  mem=31  msgs=41107  2023-04-20..2026-02-12
  C05H8KVNU67    game-design                            private mem=27  msgs=22751  2023-07-16..2025-10-06 archived
  C050WGU41HR    engineering-bots                       private mem=35  msgs=20306  2023-03-29..2026-02-11
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16889  2023-10-07..2026-02-11
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16773  2025-01-09..2026-02-11
  D076RBM29JS    D076RBM29JS                            im      mem=5   msgs=12287  2024-06-06..2026-01-28
  C09UHHN6PFZ    prototype                              private mem=18  msgs=12172  2025-11-24..2026-02-12
  D05GU6L0XFH    D05GU6L0XFH                            im      mem=5   msgs=10717  2023-07-16..2026-01-27
  CC43664F351E   mpdm-julia.lawson--brian.foster--vince mpim    mem=4   msgs=10170  2024-06-26..2025-11-21
  D05QA585LTY    D05QA585LTY                            im      mem=5   msgs=6756   2023-09-21..2025-11-10

GMAIL  mailbox=julia.lawson@harmonygames.co threads=304 messages=359 range=2023-07-16..2026-02-13
  threads by last-message month (recent): {'2025-09': 1, '2025-10': 1, '2025-11': 1, '2025-12': 6, '2026-01': 25, '2026-02': 18}
  top correspondents: leonard.hayes@harmonygames.co (105), robert@harmonygames.co (100), arthur.blake@harmonygames.co (61), claire.morgan@harmonygames.co (44), victor.barnes@harmonygames.co (43), calvin.price@harmonygames.co (38), martin.walsh@harmonygames.co (37), [EMAIL_0072] (36), SVC_1295_EMAIL (32), marcus@harmonygames.co (30)

GCAL  own=['julia.lawson@harmonygames.co'] shared=[] events=792 (distinct ical_uid 261, cancelled 50)
  last event before clock=2025-09-29T16:30:00Z  next after clock=2025-10-06T16:00:00Z
  by month: 2023-07:14 2023-08:50 2023-09:24 2023-10:35 2023-11:26 2023-12:24 2024-01:45 2024-02:22 2024-03:9 2024-04:21 2024-05:24 2024-06:39 2024-07:34 2024-08:35 2024-09:40 2024-10:27 2024-11:32 2024-12:32 2025-01:46 2025-02:18 2025-03:11 2025-04:23 2025-05:42 2025-06:31 2025-07:27 2025-08:9 2025-09:9 2025-10:25 2025-11:9 2025-12:6 2026-01:3

DRIVE  owned=45 {'application/vnd.google-apps.spreadsheet': 12, 'application/vnd.google-apps.document': 11, 'application/vnd.google-apps.presentation': 9, 'application/pdf': 9, 'folder': 3, 'application/json': 1}
  shared-with=169 {'application/vnd.google-apps.document': 52, 'text/plain': 38, 'application/vnd.google-apps.spreadsheet': 36, 'application/json': 21, 'application/pdf': 10, 'application/vnd.google-apps.presentation': 10, 'text/csv': 2}
  shared by owner: {'Resource: -6481757892984311338': 102, 'leonard.hayes@harmonygames.co': 37, 'robert@harmonygames.co': 17, 'arthur.blake@harmonygames.co': 10, 'Resource: 7240535625619857401': 3}
  native visible: {'gdocs': 63, 'gsheets': 48, 'gslides': 19}  last modified visible=2026-01-12T17:47:18Z
  UNVERIFIED (domain/anyone, not owned/shared)=117 {'application/vnd.google-apps.document': 45, 'application/vnd.google-apps.spreadsheet': 31, 'application/pdf': 17, 'application/vnd.google-apps.presentation': 13, 'application/json': 11}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2026-02-12 (-134d), slack_visible_channels=2026-02-13 (-135d), gmail=2026-02-13 (-135d), gcal_last_event_before_clock=2025-09-29 (2d), drive_last_modified_visible=2026-01-12 (-103d)
```

Julia's mailbox has only one thread in Sep 2025, so the build mail is a seeded thread with a copy in every recipient mailbox. Linear /
GitHub / Trello / Confluence identities (`entity.py resolve "Julia Lawson"`): Linear `usr_8140f09bf9f1b94c`, GitHub
`PERSON_0005_GITHUB_USERNAME`, Trello `793af7ca6940bf18eb516c75`, Confluence `user_EMPLOYEE_0005`, Drive root `d_8140f09bf9f1b94cb8ee2d`.
Arthur ("Blake" in the team's own voice: C090N54TG79/1756751373.593569 "Blake (or I) shouldn't have released it"): Linear
`usr_cc3e90160f490686`, Confluence `user_EMPLOYEE_0025`, GitHub `EMPLOYEE_0025_GITHUB_USERNAME`. Robert: Linear `usr_Robert`, Confluence
`user_EMPLOYEE_0016`.

## 1 Storyline

**Arc.** Zombie Match 3D's difficulty system was built Apr–Aug 2025 mostly by Arthur ("Blake") on Robert's requests, largely as direct
commits without PRs (base commits 0fdbc2d6 "First dynamic difficulty level", 16c9bed2, 40fdf48f; among the 215 PRs with CodeRabbit file
tables only match3d#244 touches `Assets/Scripts/DynamicDifficulty`): tiers −2…+2 per level, a starting tier from the first-10-level
average CPM (ZOM-42 and the code: `cpm > 90.0f`; ZOM-199's text says >= 90), promotion on ≥ 80% and demotion on 4 straight losses or ≤ 50% over up to 10 attempts with a
record reset (ZOM-42 full spec), the level drop after a demotion (ZOM-303, match3d#244 "lowering level difficulty after repeated
failures" — live in the code at the clock), blunder → enrage instead of an HP penalty with values per monster prefab (ZOM-254;
C0880U9751A/1750165444.708639 Vincent: "u can set any percentage per each monster"), narrowed to speed and damage (ZOM-282; commit b511fcbc
"Disable monster enrage health"), the base value moved 0.6 → 0.8 (commit 84780b8d, 2025-08-09, Robert), then speed and damage split with
the respawn health boost removed (match3d#401, merged 2025-08-25) and the VarC prefab values set by Julia (C08R27X0EAH/1756922765.033199). Much of the rest is level-editor and debug
tooling. The store builds players have are iOS 0.3.49 (C0880U9751A/1759182908.627389, 2025-09-29) and Android 0.3.133. Leonard books the
Oct 6 tuning session (seeded invite + agenda), posts the rules card on ZM ROADMAP (Sep 29) and amends it (Sep 30); Blake sends the
store-builds mail (Sep 30 09:12Z) and a reply-all (13:26Z); Brian posts a confident summary in #zombie-design (Sep 29 22:31Z); Vincent asks
for the list in-channel (Sep 30 16:12Z); Leonard DMs Julia the ask (Sep 30 19:48Z).

**Timeline placement** (`references/universe_kb/timeline.md`, clock 2025-10-01): ZOM Linear team created 2025-04-18
(`linear_team:team_ZOM`, `linear:ZOM-10`) — the window opens with the first ZOM batch (created 2025-04-21); alpha shipped 2025-04-11
(`slack:C07C2866011:1744565232.971959`); ZM ROADMAP created 2025-06-17 (`trello:6851a6569f3bf818760632d7`) — the card goes on it; the
GitHub app was subscribed in #zombie-prs on 2025-06-30 (`slack:C093LEZGF6J:1751317160.968219`), so the seeded match3d#401 comment
(2025-08-25) gets its Slack mirror; Season Pass merged 2025-09-15 (`github:harmonygames-Games/match3d#438`) — not in scope; the Domino
Delights difficulty work of spring 2025 (`github:harmonygames-Games/GameOfDominoes#1781`, `slack:C08GLSV8Z7W:1744310550.428869`,
`linear:ENG-2217`) is the decoy card's scope. Post-clock ZOM work (ZOM-576 2025-10-02, ZOM-593, ZOM-600, ZOM-622) does not exist at the
freeze and is not used.

**Anchors per service.**

| Service | Record | Role |
|---|---|---|
| slack | D05HB64NMQU/1759261706.530914 (seed, id 6f77386571537f0bd88c959bdc216f94) | anchor A1, Leonard → Julia, 2025-09-30T19:48:26Z |
| trello | 68daca5871dba40417a00383 (seed) on ZM ROADMAP 6851a6569f3bf818760632ab, list "Oct 21" 6851a677e090018224fb8c7f | H1 "Difficulty baseline (Julia)"; createCard 68daca5845e48874fb98e25a; comment 68dbfa4362a051efb5e0ae45 |
| trello | 683dbef4e319167a802bd888 (seed) on DD Product Roadmap 65eb4ec525346c8070ca638f, list "Rebirth (June)" 65eb4f4e26cfce07d665a38e | Domino Delights decoy card (2025-06-02) |
| gmail | julia.lawson@harmonygames.co/1844679607844896665 (seed) + reply 1844695547248860585 | H2 "store builds for monday" (Blake); the reply: the build checks CPM > 90; copies in 5 mailboxes |
| gsheets | f_0ba93ae0238d9ed4178212 (seed) | H3 "ZM monster enrage" (Julia's; Live = VarC prefab values at the clock, Next pass, History) |
| gsheets | f_34f0950581934de1278969 (base) | Domino Delights "Parameter Optimization" (Leonard; shared with Julia) — decoy |
| gslides / slack | f_048bf5e69f8e7f1a659a5c (seed deck, Robert 2025-06-16) + C090N54TG79/1756912929.304417 (seed, Blake in #zombie-design 2025-09-03) | tier rules without the 50% demotion rule ("90 or more"); ZOM-254's +25% blunder line; comment retires it |
| gcal | ical 26fce3dc380d9da1343bcccc6072f03e@hg4; Julia's copy evt_91674a9c23d012a9ac34da (+4 attendee copies) | "ZM difficulty tuning" Mon 2025-10-06 17:00Z |
| gdocs | f_9ec79682ff351aa466364a (seed) | "ZM difficulty tuning - Oct 6" agenda (Leonard) |
| gdrive | d_96489e1e00a56685625939 (seed) | "ZM Difficulty" folder (Leonard owner; Julia writer only) — destination |
| github | harmonygames-Games/match3d#401#c_2 (seed) on base match3d#401 (+ Slack mirror in #zombie-prs C093LEZGF6J) | Blake 2025-08-25: "this also finishes the hp part of ZOM-282" |
| github | harmonygames-Games/match3d#243, #265 (base) | real file tables of the shared PRs |
| linear | 109 candidates (`truth.json`) + 109 seeded notes (`minted_ids.json` LIN_NOTES); ZOM-42 full description (base) | the cohort; the full tier rules |
| slack | C090N54TG79/1759185077.402611 (seed, Brian), C090N54TG79/1759248760.118527 (seed, Vincent) | wrong summary; post-it-here distractor |
| slack | C08R27X0EAH/1756922765.033199, C0880U9751A/1758921802.962539, C0880U9751A/1759182908.627389, C090N54TG79/1759176983.189479 (base) | per-monster enrage; tier moves; iOS 0.3.49; motivation |

**Cohort.** `cohorts.json` LIN-CQ12 ("team_ZOM AND created_at in 2025-Q2", 317) and LIN-CQ13 (2025-Q3, 236) are the natural parents;
the task cohort is the source-defined subset created 2025-04-21 – 2025-08-31 (not Duplicate) that matches the card's title vocabulary /
the amendment's "attack power" (31) or is assigned to Arthur (78 more; membership then by his "tiers:" tag): **109 candidates**, **35 members**
(`truth.json`). `hazards_inside`: the L03 examples ZOM-292 and ZOM-387 (both candidates, not members) are acknowledged (§1a).

**Natural traps used** (`references/universe_kb/trap_catalog.json`): N01 (every ZOM-n has an ENG-n twin; ENG-2215–2217 are the Domino
Delights pity tickets), N02 (match3d#243/#244 vs ZOM-243/ZOM-244 exist), D07 (Trello roadmap stale vs
Linear), C01/C02 (thread replies that correct — Robert's per-monster reply under Leonard's question; the mail reply), P02 (Lawson: Julia vs
Peter Lawson), P04 (tokenised contributors — EMPLOYEE_0032 tickets carry Vincent's QA notes), X02 (EMPLOYEE_0032 token), K02 (app-name lineage).

**Originality.** Not the Combo Fighters launch record, the 133-PR residue register, the RC-flag gate or the art-canon handoff; not the
completed Frederick, Douglas or Robert tasks (Douglas's 73 tickets are all Done after 2025-08-25; this cohort is created Apr 21 – Aug 31;
only ZOM-383 is in both, as a non-member here). The per-record question is "did this difficulty change reach players, stay as shipped, or
get replaced", decided from Blake's tags and notes, a build mail, the full ZOM-42 spec and replacing work.

## 1a Coherence audit

Scope = every record a correct run opens: the DM ask, the #zombie-design summary and post, the card + comment + DD card, both mails, the
monster enrage sheet (3 tabs), the DD sheet, Robert's deck + comment, the invite, the agenda, the folder, the 109 candidates and
their notes, ZOM-42's full description, match3d#244 (+ seeded comment), #243, #265, #267, #271, #282, #319, #401, and the base messages
the storyline cites. Known hazards walked from `references/universe_kb/coherence_hazards.json` (all six categories).

| Record | Category | Fields | Evidence pointer | Hazard id | Disposition |
|---|---|---|---|---|---|
| ZOM-282 Done 2025-06-21 says "NOT HP" while match3d#401 (2025-08-25) says "Enrage health boosts have been removed" | temporal | completed_at vs a later PR removing the same thing | ZOM-282 description; harmonygames-Games/match3d#401 body; commit b511fcbc | T04 | designed claim + overturning record: Blake's ZOM-282 note (2025-06-21) "the hp boost still applies on respawned monsters"; Blake's #401 comment (2025-08-25) "this also finishes the hp part of ZOM-282" |
| ZOM-282 (completed 06-21) closes before ZOM-254 (completed 06-23) that it narrows | temporal | completed_at order | ZOM-254, ZOM-282 | T05 | fold in: card rule 4 orders by creation ("a ticket or PR created after this one"); ZOM-282 created 2025-06-19T05:23:06Z after ZOM-254 2025-06-12T21:59:58Z |
| Robert's seeded Slides deck (06-16) and Blake's comment (09-03) | temporal | created_at vs author activity; Robert's own Jun 19 "+100%" (C0880U9751A/1750370473.240179) | f_048bf5e69f8e7f1a659a5c, C090N54TG79/1756912929.304417 | T08 | fold in: the deck is dated before Robert's Jun 19 change and carries ZOM-254's spec; the comment retires it |
| Robert on Sep 26: "if you win 8 out of 10, you move up … Losing 4+ in a row is almost likely gonna get you moved down" | semantic | tier rules in prose | C0880U9751A/1758921802.962539, /1758921729.009549 | S08 | fold in: agrees with ZOM-42 and the deck (80% over 10; 4-loss streak); the 50% rule and the reset are in ZOM-42 only — complementary, not contradictory |
| Leonard Sep 29: "show what multiplier boosts the zombies get (25% more HP 25% more speed etc.)" | semantic | an example in a proposal | C090N54TG79/1759173062.702099 | S08 | fold in: a hypothetical display idea ("we should show … etc."), not a statement of current values; the #zombie-design message and #401 state HP is unchanged |
| match3d#404 (2025-08-27) "increased zombie HP boost, lowered difficulty-based HP scaling" | semantic | HP wording | harmonygames-Games/match3d#404 body | S08 | fold in: the algo-level defaults for generated levels (AlgoLevelSettings), not blunder enrage; the sheet column reads "enrage hp" under the blunder header |
| MF35 is an A/B variant of levels 1–35 with the original list kept for the control group | semantic | level content | C08R27X0EAH/1754000781.512949 | S08 | avoid: no seed claims ZOM-23 was replaced; its note is a neutral QA check |
| Seeded text citing keys / PRs | cross-service referential | ZOM keys, match3d numbers | notes cite harmonygames-Games/match3d#243, #258, #265, #267, #271, #282, #283, #289, #296, #319; Blake's #401 comment names ZOM-282 | R01 | fold in: every cited PR exists and merged before the note (checked in the `build_design.py` truth run) |
| Notes vs the git history | cross-service referential | file lists, commits | harmonygames-Games/match3d#243#c_2, #265#c_2, #282#c_2; commit history of Assets/Scripts/DynamicDifficulty | R06 | fold in: no note names a file; PR-linked notes cite their PR (agreeing with its table); the "tiers:" tag is Blake's judgment, not a code claim |
| Google ids in seeded text | cross-service referential | docs.google.com ids | f_0ba93ae0238d9ed4178212, f_9ec79682ff351aa466364a named by title only | R04 | avoid: seeded text names files by title |
| PR comment and its Slack mirror | cross-service referential | GitHub-app copy | harmonygames-Games/match3d#401#c_2 (2025-08-25) + mirror in C093LEZGF6J | R07 | fold in: inside the match3d mirror window (INT-01, from 2025-06-30); the mirror is seeded threaded under #401's opened post |
| Calendar invite without invitation mails | cross-service referential | invitation mail | evt_91674a9c23d012a9ac34da | R08 | fold in: INT-11 — most base meetings have no invite mail; one copy per attendee calendar |
| Thread counters | quantitative | reply_count / latest_reply | C090N54TG79/1759185077.402611 | Q01 | avoid: both #zombie-design seeds are top-level, reply_count 0 |
| Calendar copies | quantitative | per-copy fields | 5 copies of 26fce3dc380d9da1343bcccc6072f03e@hg4 | Q11 | fold in: identical summary/start/end/attendees |
| Same RFC message per mailbox | quantitative | content per copy | julia.lawson@harmonygames.co/1844679607844896665 and the 4 other copies | Q10 | fold in: one Message-ID per message, identical bodies |
| Enrage value history | quantitative | values; VarC prefabs at commit 85d1a406 | commit 84780b8d "Enrage change 0.6 -> 0.8" (2025-08-09); harmonygames-Games/match3d#401; f_0ba93ae0238d9ed4178212 tab History | Q09 | fold in: the Live tab lists the VarC prefab values at the clock (Boxer 0.5/0.4 … MonsterBase 0.8/0.8); History: base 0.6 -> 0.8 (MonsterBase), #401 split |
| ZOM-292 Todo / match3d#267 merged; ZOM-387 Todo / match3d#319 merged | state/lifecycle | state vs merged PR | ZOM-292, ZOM-387, harmonygames-Games/match3d#319 | L03 | dated claims: notes for ZOM-292 (2025-07-04T03:07:46Z) and ZOM-387 (2025-07-27T20:40:47Z) say each stays open for the rest of its list; not members; not modified |
| Parent Done while child open | state/lifecycle | parent/child states | ZOM-201 (Done) / ZOM-293 (Todo) | L06 | fold in: the child is its own row (Not shipped); Robert's ZOM-293 note "still happens on the dev build, keeping it open" |
| Ticket text vs the build | state/lifecycle | ZOM-199 ">= 90" vs ZOM-42 and code "> 90" | ZOM-199, ZOM-42, match3d TierManager at commit 85d1a406 | L13 | designed claim + overturning record: Blake's reply 1844695547248860585 (2025-09-30) names the code's > 90; the agent's write comments on ZOM-199 |
| Merged PRs with only bot reviews | state/lifecycle | reviews | harmonygames-Games/match3d#244 (CodeRabbit COMMENTED only) | L10 | avoid: no rule uses reviews; #244 not in the hazard index (`base_check.hazard_index`) |
| Linear ids without hex | identifier/format | user ids | usr_Robert (Robert's notes on ZOM-23, ZOM-288, ZOM-293) | I10 | fold in: exact base ids from linear/data.json |
| Gmail mailbox file aliases | identifier/format | thread file names | julia.lawson@harmonygames.co/1844679607844896665 filed as jlawson@…; blake@, leonard@, brian@ | I03 | fold in: copies under the base aliases |
| GitHub logins are tokens | identifier/format | author_login | harmonygames-Games/match3d#401#c_2 (EMPLOYEE_0025_GITHUB_USERNAME, as on base harmonygames-Games/match3d#265#rc_3) | I08 | fold in: base token; the Slack mirror shows the real login (I08) |
| EMPLOYEE_0032 token on 5 members | other | assignee token | ZOM-246, ZOM-254, ZOM-263, ZOM-274, ZOM-280 (assignee EMPLOYEE_0032_EMAIL in linear/data.json) | I05 | avoid: never voiced; Vincent's QA notes |

**Sibling-defect sweep.** For each designed defect, other records with the same kind in scope:
- *Done but players don't have it:* the 8 Editor-only members (ZOM-162, ZOM-163, ZOM-173, ZOM-200, ZOM-201, ZOM-250, ZOM-277, ZOM-312) are the
  same kind by design; no member is behind a define or flag (TierManager at commit 85d1a406 has no `#if`; Leonard Sep 12: no remote config yet).
- *Ticket text that the build contradicts:* ZOM-199's ">= 90" vs the code's "> 90" (ZOM-42 says > 90) — the designed one; no other member's
  text was checked as contradicted except ZOM-282's "+50%" (numbers are excluded by card rule 4 and the rules tab takes the sheet).
- *Replaced by later work:* ZOM-254 → ZOM-282. Other pairs checked and kept Live: ZOM-282 vs #401 (#401 finished ZOM-282's hp part; Blake's #401
  comment); ZOM-199 restates ZOM-42's threshold (rule 4 keeps ZOM-42 Live); ZOM-50 vs ZOM-161 (different event fields); ZOM-295 (#271) vs revert e54e7e4e (2025-07-11, of a different "Monster
  enrage & respawn fix" commit 95c8152d by EMPLOYEE_0032, not #271's 21d00414) — #271 stands.
- *Stale rule text:* the seeded page's +25% blunder line (f_048bf5e69f8e7f1a659a5c, retired by C090N54TG79/1756912929.304417); Brian's seeded summary. Base text agrees with the rules
  in force (C0880U9751A/1758921802.962539; C08R27X0EAH/1756922765.033199); base page_zm3d_gdd's stored versions start 2025-10-02 (not cited).
- *Store build identity:* iOS 0.3.38 submitted Sep 17 (C08R27X0EAH/1758081917.318539), required versions Android 0.3.127 / iOS 0.3.40 on Sep 23
  (C0880U9751A/1758643365.607149), iOS 0.3.49 released Sep 29 (C0880U9751A/1759182908.627389); Android 0.3.133 is posted only in #executives
  (C07C2866011/1759075866.111309, Julia NO) — the mail states it, consistent with the base.

## 1b Active speakers

Every person given a seeded voice, with `status_at_clock` from `references/universe_kb/activity.json` (the file is computed for the
Feb 2026 clock; each person also posted in Sep 2025, so all are active at the Oct 1 freeze).

| Person | Email | status_at_clock (activity.json) | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_feb_2026 | DM ask; H1 card + comment; DD decoy card; tuning invite organizer; agenda doc; ZOM-30 note |
| Arthur Blake | arthur.blake@harmonygames.co | active_feb_2026 | build mail + reply (signs "Blake"); Slack message; #401 comment; 94 closing notes |
| Robert | robert@harmonygames.co | active_feb_2026 | Slides deck (Jun 16); ZOM-23, ZOM-288, ZOM-293 notes |
| Brian Foster | brian.foster@harmonygames.co | active_feb_2026 | #zombie-design summary (wrong); invite attendee |
| Oliver Brooks | oliver.brooks@harmonygames.co | active_feb_2026 | QA notes on ZOM-49, ZOM-161, ZOM-262, ZOM-275 |
| Owen Baker | owen.baker@harmonygames.co | active_feb_2026 | ZOM-295 note |
| Marcus Bennett | marcus.bennett@harmonygames.co | active_feb_2026 | ZOM-258 note |
| Vincent Parker | vincent.parker@harmonygames.co | quiet_since_2025-12 | #zombie-design post-it-here request (Sep 30; member of C090N54TG79); QA notes on the EMPLOYEE_0032 tickets (Jun 2025) |
| Julia Lawson | julia.lawson@harmonygames.co | active_feb_2026 | persona; owner of the monster enrage sheet (modified 2025-09-02, matching C08R27X0EAH/1756922765.033199) |

CodeRabbit is not seeded. Seeded text follows `references/universe_kb/conventions.json`: Leonard's DMs lowercase and run-on; the team
calls Arthur "Blake" (card, ask and mail signature); Linear comments one or two lines; Blake's notes start "closing." as a habit across his
94 tickets, and "tiers: closing." on the ones he counts as tier work. The Leonard–Julia DM is mostly Turkish but carries English work messages (D05HB64NMQU 2025-08 "Hello", "Yes"); the ask is in
English like Leonard's work posts in #zombie-design.

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

ENTITY email:julia.lawson@harmonygames.co  name=Julia Lawson  kind=person  emails=['julia.lawson@harmonygames.co']
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
ENTITY email:brian.foster@harmonygames.co  name=Brian Foster  kind=person  emails=['brian.foster@harmonygames.co']
ENTITY email:oliver.brooks@harmonygames.co  name=Oliver Brooks  kind=person  emails=['oliver.brooks@harmonygames.co']
ENTITY email:owen.baker@harmonygames.co  name=Owen Baker  kind=person  emails=['owen.baker@harmonygames.co']
ENTITY email:marcus.bennett@harmonygames.co  name=Marcus Bennett  kind=person  emails=['marcus.bennett@harmonygames.co']
ENTITY email:vincent.parker@harmonygames.co  name=Vincent Parker  kind=person  emails=['vincent.parker@harmonygames.co']
```

Correct entity vs lookalikes: Julia Lawson is julia.lawson@harmonygames.co (not Peter Lawson); her mailbox files are `jlawson@…`, and
"lawson40" in #zombie-design (C090N54TG79/1756751169.213249) is a level-pack name. "Blake" is Arthur Blake (mailbox files `blake@…`). Brian
Foster is brian.foster@ (files `brian@…`); Marcus is Marcus Bennett (ZOM-258), not the `marcus@` mailbox. Robert's Linear id is `usr_Robert`.
Ticket identity: ZOM-n vs ENG-n twins (N01); PR identity: match3d#243/#244 vs ZOM-243/ZOM-244.

## 2 Cohort spine

**Rule (H1 rule 1 + comment).** ZOM tickets created 2025-04-21 – 2025-08-31, not Duplicate, that changed difficulty: a whole-word title match
on {difficulty, difficult, tier, tiers, tiering, enrage, enraged, blunder, CPM}, or "attack power" in the title (comment), or one of
Blake's tickets whose closing note starts with "tiers:"; open, cancelled and never-merged ones are in as Not shipped. Candidates **109** (31 title/amend + 78 other Blake tickets; 9 of his are changed only after the clock and carry a pre-clock
"parking this, nothing merged yet" note). Members **35** (26 title, 5 attack power, 4 by Blake's tag). Status counts: **23 Live,
8 Editor only, 3 Not shipped, 1 Replaced** (`truth.json`, generated).

**Per-ticket truth** (generated by `build_design.py`):

| # | Ticket | Title (base) | Linear state | Joins by | Note (author · id) | Status | Replaced by |
|---|---|---|---|---|---|---|---|
| 1 | ZOM-23 | Reduce difficulty for first 50 levels | Done | title | robert · cmt_ac0306e8c37188779a29 | Live |  |
| 2 | ZOM-30 | Need to track average blunder (overfilling match platform) | Done | title | leonard.hayes · cmt_74e7511b3cccd02e1209 | Live |  |
| 3 | ZOM-42 | Dynamic Difficulty | Done | title | arthur.blake · cmt_267b4b4b44dc345e4cd6 | Live |  |
| 4 | ZOM-45 | Expose the ability to mark level difficulty in editor also | Done | title | arthur.blake · cmt_bed381141007e04f1aac | Live |  |
| 5 | ZOM-49 | Add Blunder Count by Level to Analytics | Done | title | oliver.brooks · cmt_3907d543ffc60ff10991 | Live |  |
| 6 | ZOM-50 | Track player skill tier in the left_level event | Done | title | arthur.blake · cmt_6fb679dc448e1b2599e4 | Live |  |
| 7 | ZOM-161 | Add difficulty tier assignment for left level event | Done | title | oliver.brooks · cmt_465f32f84344e2903c56 | Live |  |
| 8 | ZOM-162 | Dynamic difficulty tracks are linked across tiers in level | Done | title | arthur.blake · cmt_53dddc2442947df50ec5 | Editor only |  |
| 9 | ZOM-163 | Play button in level editor not loading difficulty tiers | Done | title | arthur.blake · cmt_ca16a83ec7b41cbcf1a8 | Editor only |  |
| 10 | ZOM-173 | Item Set Count in editor not updating with difficulty tier | Done | title | arthur.blake · cmt_bb9c4deb176b2c894ca6 | Editor only |  |
| 11 | ZOM-199 | Conduct difficulty tier assignment based on first 10 level | Done | title | arthur.blake · cmt_c67b7ad42bc8183104aa | Live |  |
| 12 | ZOM-200 | Need debug menu for dynamic difficulty to add the metric o | Done | title | arthur.blake · cmt_229bdb5a27939abf2476 | Editor only |  |
| 13 | ZOM-201 | Dynamic difficulty stat window not functioning. Also turn  | Done | title | arthur.blake · cmt_5ae7bed6255b9daeb25e | Editor only |  |
| 14 | ZOM-202 | Minimize or migrate selection panel for easier difficulty  | In Progress | title | arthur.blake · cmt_d588f677a47bb5cba668 | Not shipped |  |
| 15 | ZOM-221 | Fix monster spawning issues with long gaps in tracks | Done | tiers: tag | arthur.blake · cmt_ad5c9cc21508c9961089 | Live |  |
| 16 | ZOM-246 | Implement an "attack power" line item in the card profile  | Done | attack power | vincent.parker · cmt_79db35d590753f55d547 | Live |  |
| 17 | ZOM-250 | Create faux level timer and add attack power stats in leve | Done | attack power | arthur.blake · cmt_370b572a96173c68048d | Editor only |  |
| 18 | ZOM-254 | Blunder Mechanic 2.0 enrages zombies instead of HP penalty | Done | title | vincent.parker · cmt_9698eebaf0663ba1f7da | Replaced | ZOM-282 |
| 19 | ZOM-258 | Icon for Enraged monster | Done | title | marcus.bennett · cmt_b2d5959477cef5c6c7e3 | Live |  |
| 20 | ZOM-262 | Tutorial for Blunder Locked User | Done | title | oliver.brooks · cmt_264b95c44d6c221420c7 | Live |  |
| 21 | ZOM-263 | Fix attack power calculation for ricochet effect | Done | attack power | vincent.parker · cmt_a19e4e8b9ac4bdffafb4 | Live |  |
| 22 | ZOM-274 | Monsters can only be enraged once bug | Done | title | vincent.parker · cmt_bb3a55390c9a7e976016 | Live |  |
| 23 | ZOM-275 | Update FTUE message to reflect Blunder mechanic 2.0 change | Done | title | oliver.brooks · cmt_c7f092bc3d1f01cd005f | Live |  |
| 24 | ZOM-277 | Correct average attack power calculation for items in leve | Done | attack power | arthur.blake · cmt_b0aa45d307c981ce4487 | Editor only |  |
| 25 | ZOM-280 | Fix monster enraged HP issue causing incorrect death statu | Canceled | title | vincent.parker · cmt_a98740682072cf49a78b | Not shipped |  |
| 26 | ZOM-282 | Optimize enrage mechanic for speed and attack damage only | Done | title | arthur.blake · cmt_912bdd42ad5c8d51521f | Live |  |
| 27 | ZOM-288 | Declutter levels and balance around enrage, player skills, | Done | title | robert · cmt_bc80fab00bc55be3e293 | Live |  |
| 28 | ZOM-293 | Dynamic Difficulty Tiering Down Issue | Todo | title | robert · cmt_7f0329231d8b9f6e2d97 | Not shipped |  |
| 29 | ZOM-295 | Refill health and push monster back should reset ALL enrag | Done | title | owen.baker · cmt_9bd1d3170eb054b18d13 | Live |  |
| 30 | ZOM-300 | Dynamic Item Removal | Done | tiers: tag | arthur.blake · cmt_5919318074e3e3fb7921 | Live |  |
| 31 | ZOM-303 | Dynamic Difficult Design Oversight Fix | Done | title | arthur.blake · cmt_a969dc3dd35c1f4439cb | Live |  |
| 32 | ZOM-305 | Losing a level deducts 2 lives | Done | tiers: tag | arthur.blake · cmt_735d60b29ce006b58217 | Live |  |
| 33 | ZOM-312 | Delete Difficulty Tier and Reassign | Done | title | arthur.blake · cmt_68811c86e67c36e5c2f7 | Editor only |  |
| 34 | ZOM-315 | Use base damage of item if total attack power excludes ite | Done | attack power | arthur.blake · cmt_98027df98af6fb30b763 | Live |  |
| 35 | ZOM-378 | Level 1 is removed and creates tutorial order problems | Done | tiers: tag | arthur.blake · cmt_5209afb9533bec4053ad | Live |  |

**Surfaces and shortcut audit.**

| Surface | Per-record call | Bulk call that does not cover it | Requirement · decides |
|---|---|---|---|
| Linear notes on each of the 109 candidates (seeded; base has 0 Linear comments) | `linear_list_comments` × 109 | `linear_list_issues` returns titles, states, assignees, (truncated) descriptions — no comments; the 4 tagged members have no difficulty word in the title (ZOM-221 "Fix monster spawning issues with long gaps in tracks", ZOM-300 "Dynamic Item Removal", ZOM-305 "Losing a level deducts 2 lives", ZOM-378 "Level 1 is removed and creates tutorial order problems"); 7 difficulty-sounding Blake tickets are not members | R1 · register membership |
| The same notes on the 35 members (where the change lives) | (same call) | titles mislead: ZOM-45 "…in editor also level object in Unity" — note: the level carries the label at runtime (Live); ZOM-277 "Correct average attack power calculation for items in level" — note: the editor's stats panel (Editor only); #243 and #265 also touch runtime folders and only the notes say which part is the ticket's | R2 · status per ticket |
| match3d PRs #401 (seeded conversation comment), #243, #265 | `github_get_pull_request(_comments)` | PR search returns titles/merge state; #401's title does not name ZOM-282 | R2 · status per ticket |

**Short-circuit audit.** Membership of Blake's 94 candidates is decided only by his tag (no title word, label or PR carries it);
a run that triages Blake's tickets by title skips exactly the ones that join (lives, spawn gaps, item removal, level-1 order) and
reads the ones that don't (insertion, replacement, algo, stats panel, spawn limits, CPS/DPS). Once a ticket is a member, its status still needs the
note (editor panel vs runtime; which part of a shared PR). Slack sweeps cannot help: no note is mirrored.

**Predicate details.** Closed vocabulary: Live / Editor only / Replaced / Not shipped. Whole words (ZOM-271 "ATK POWER" is not "attack
power"; "Difficult" in ZOM-303 counts). Window on created_at: ZOM-517 (2025-09-03) is out. Duplicates out (ZOM-203, ZOM-276). **House rules
overriding the natural reading (A15):** Done in Linear is not shipped when the change is only level editor / LevelDesigner / debug tooling
(H2); the build, not the ticket text, decides the starting-tier threshold (H2 reply); ZOM-42 stays Live although ZOM-199 restates its threshold (rule 4);
"replaced" needs a later ticket/PR that changed how it works, not number tuning (rule 4). **Dual regime:** enrage before and after #401
(one enrage percentage per prefab, base 0.6 → 0.8 on 2025-08-09; speed and damage split, no HP after) — the rules tab takes today's. **Boundary records
(A17/A10):** ZOM-517 (window), ZOM-271 (phrase), ZOM-203/276 (duplicates), ZOM-279/284/285/286 (cancelled insertion tickets, "dropping this
one, nothing merged"), ZOM-257/289/383/209/190/96/24 (difficulty-sounding, untagged), ZOM-352 (lives ticket like ZOM-305, but its note cites
match3d#282 with no tag — not a member).

Necessity rule (Hardness_Mastery §2.5): 8 of 109 notes are decisive for membership or status (the 4 tags; ZOM-45, ZOM-277, ZOM-173, ZOM-312),
and every Blake note must be read to know it carries no tag; neutral notes sit on every other Blake ticket and on the owners' tickets; no
upstream record lists the members; notes never use the rule's words "shipped", "live" or "editor only".

## 3 Hidden authorities

| Id | Name (how it is reached) | Home | Governs | Decoy(s) | Decoy scope / supersession | Findability proof |
|---|---|---|---|---|---|---|
| H1 | the difficulty baseline rules ("the rules for the register are on the difficulty baseline card on the zm roadmap board", D05HB64NMQU/1759261706.530914) | trello 68daca5871dba40417a00383 + comment 68dbfa4362a051efb5e0ae45 | R1, R3, R5, R7 | DD card 683dbef4e319167a802bd888 "Difficulty baseline" (Domino Delights, Jun 2) | game scope: Domino Delights April pass vs Zombie Match 3D | a Trello search "difficulty baseline" returns both; proven at injection with `hg.py search search trello "difficulty baseline"` |
| H2 | Blake's store builds mail (card rule 3, trello:68daca5871dba40417a00383) | gmail thread 1844679607844896665 (+ reply 1844695547248860585) | R2 | Brian's summary C090N54TG79/1759185077.402611 ("everything from the june dynamic difficulty push is in the store builds, the editor bits too") | older version in T7 version_records (Sep 29 22:31Z < mail Sep 30 09:12Z) | a Gmail search "store builds" returns the thread |
| H3 | the monster enrage sheet ("your monster enrage sheet has the numbers", card rule 5) | gsheets f_0ba93ae0238d9ed4178212 (tab Live) | R4 | base gsheets f_34f0950581934de1278969 "Parameter Optimization" (Domino Delights, Leonard; Julia YES) | game scope | a Sheets search "monster enrage" returns it; "parameter" returns the DD sheet |

`governs` lists do not overlap. The anchor names only H1; H2, H3, the page, ZOM-42, the invite, the folder and the agenda are reached
from the card (rules 2, 3, 5, 7); the amendment is on the card; the > 90 check is in H2's reply.

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Leonard's difficulty baseline ask | slack D05HB64NMQU/1759261706.530914 |

**Hub** = A1 (Leonard) delegating to H1 and the reply; H1 (Leonard) delegates to H2, H3, the page, ZOM-42, the invite, the folder and the agenda.

**Incorporation table** (quotes are exact substrings of `planned_text.json`; the gate re-reads them from the SQL at injection):

| Fragment | Service · container | Kind | Via | Delegated by record | Delegation quote (verbatim) | Requirements | Names authority |
|---|---|---|---|---|---|---|---|
| K1 | slack D05HB64NMQU | delegation | A1 | D05HB64NMQU/1759261706.530914 | "reply here when it's in the folder with how many tickets made the list and how many" | R6 | H1 "the rules for the register are on the difficulty baseline card on the zm roadmap board" |
| K2 | trello 68daca5871dba40417a00383 | requirement | A1 | D05HB64NMQU/1759261706.530914 | "the rules for the register are on the difficulty baseline card on the zm roadmap board" | R1, R2, R3, R7 | H2 "Blake's store builds mail"; H3 "your monster enrage sheet has the numbers" |
| K3 | trello 68dbfa4362a051efb5e0ae45 (comment) | amendment | A1→K2 | 68daca5871dba40417a00383 | "Julia owns this one." | R1 | — |
| K4 | gmail 1844679607844896665 | requirement | A1→K2 | 68daca5871dba40417a00383 | "Blake's store builds mail" | R2 | — |
| K5 | gmail 1844695547248860585 (reply) | amendment | A1→K2 | 68daca5871dba40417a00383 | "What is in the store builds and what counts as shipped: Blake's store builds mail." | R4, R7 | — |
| K6 | gsheets f_0ba93ae0238d9ed4178212 | requirement | A1→K2 | 68daca5871dba40417a00383 | "Enrage is per monster: your monster enrage sheet has the numbers." | R4 | — |
| K7 | gslides f_048bf5e69f8e7f1a659a5c | requirement | A1→K2 | 68daca5871dba40417a00383 | "The tier rules are written up on Robert's dynamic difficulty deck" | R4 | — |
| K8 | slack C090N54TG79/1756912929.304417 | amendment | A1→K2 | 68daca5871dba40417a00383 | "The tier rules are written up on Robert's dynamic difficulty deck" | R4 | — |
| K9 | gcal evt_91674a9c23d012a9ac34da | recipient | A1→K2 | 68daca5871dba40417a00383 | "Share it with everyone on the tuning session invite: Robert can edit, everyone else comments." | R8 | — |
| K10 | gdrive d_96489e1e00a56685625939 | destination | A1→K2 | 68daca5871dba40417a00383 | "The register goes in the ZM Difficulty folder." | R5 | — |
| K11 | gdocs f_9ec79682ff351aa466364a | format | A1→K2 | 68daca5871dba40417a00383 | "Layout as in the session agenda." | R9 | — |
| K12 | linear ZOM-42 description (base) | requirement | A1→K2 | 68daca5871dba40417a00383 | "in ZOM-42 itself" | R4 | — |
| K13 | linear cmt_735d60b29ce006b58217 (ZOM-305 note) | requirement | A1→K2 | 68daca5871dba40417a00383 | "his closing note on those starts with \"tiers:\"" | R1 | — |

13 fragments over 9 services (slack, trello, gmail, gsheets, gslides, gcal, gdrive, gdocs, linear) and 10 containers. **Amendments**
later in time: K3 (card comment, Sep 30 15:41Z; adds attack power, rest stands), K5 (mail reply, Sep 30 13:26Z; the build checks CPM > 90 — overturns ZOM-199's
">= 90" and the deck's "90 or more"), K8 (#zombie-design message, Sep 3; retires the +25% blunder line). **Non-
authoritative instruction distractors**: Vincent's "drop it in here too" (C090N54TG79/1759248760.118527), the DD card's "Share it with Brian and
Vincent, both can edit" (683dbef4e319167a802bd888), the sheet's Next pass tab (Leonard's per-level proposal).

## 5 Chains and trap register

**Chains** (manifest `chains`; 8 distinct mechanism ids):

| Chain | Root cause | Hops (service · record · finding) | Ends in |
|---|---|---|---|
| C1 | A1 | slack C090N54TG79/1759185077.402611 Brian: the same +50% for every monster → slack C090N54TG79/1756912929.304417 speed and damage only, per monster → gsheets f_0ba93ae0238d9ed4178212 Live (VarC values, MonsterBase 0.8/0.8, hp 0) | R4 (enrage row) |
| C2 | A12 | slack D05HB64NMQU/1759261706.530914 → trello 68daca5871dba40417a00383 vocabulary + Blake's tagged tickets → trello 68dbfa4362a051efb5e0ae45 attack power → linear cmt_735d60b29ce006b58217 (ZOM-305 tagged "tiers:") | R1 (35 members) |
| C3 | A15 | trello 68daca5871dba40417a00383 status vs store builds → gmail 1844679607844896665 tooling stripped → linear cmt_b0aa45d307c981ce4487 ZOM-277 is the editor stats panel average | R2 (Editor only rows) |
| C4 | A13 | trello 68daca5871dba40417a00383 share with the invite → gcal evt_91674a9c23d012a9ac34da attendees incl. Brian → gdrive d_96489e1e00a56685625939 | R8 |
| C5 | A16 | linear ZOM-42 > 90 → linear ZOM-199 >= 90 → gslides f_048bf5e69f8e7f1a659a5c "90 or more" → gmail 1844695547248860585 the build checks > 90 | R4 (starting tier) + R7 |
| C6 | A3 | trello 68daca5871dba40417a00383 rule 5 → gslides f_048bf5e69f8e7f1a659a5c 4-loss streak only → linear ZOM-42 full spec (<= 50% over up to 10; record reset) | R4 (demotion row) |
| C7 | A17 | trello 68daca5871dba40417a00383 window/whole words/duplicates → linear ZOM-517 out → linear ZOM-271 out | R1 |
| C8 | A8 | gmail 1844695547248860585 ZOM-199's >= is not what the build does → trello 68daca5871dba40417a00383 rule 6: comment on that ticket, no new ones → linear ZOM-200 lookalike CPM debug ticket | R7 |

**Trap register** (manifest `traps`, 21 in 8 families over 7 requirements):

| Trap | Family | Records | Req | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | superseding | trello 68daca5845e48874fb98e25a → 68dbfa4362a051efb5e0ae45 | R1 | 26 by the card words; misses ZOM-246/250/263/277/315 | card comment | description first |
| T2 | exact_predicate | linear ZOM-517, ZOM-576, ZOM-593, ZOM-622 | R1 | tickets outside the window | Apr 21 – Aug 31 | title search |
| T3 | distractor (keyword_collision) | linear ZOM-271 | R1 | "ATK POWER" counted | phrase rule | "attack" search |
| T4 | distractor (near_duplicate_record) | linear ZOM-203, ZOM-276 | R1 | duplicates listed | duplicates out | — |
| T5 | scope_alias | linear cmt_bed381141007e04f1aac, cmt_b0aa45d307c981ce4487; gmail 1844679607844896665 | R2 | ZOM-45 Editor only, ZOM-277 Live by title | notes vs stripped tooling | titles before notes |
| T6 | superseding (cross-service; ZOM-199 states the same >= 90) | gslides f_048bf5e69f8e7f1a659a5c → gmail 1844695547248860585 | R4 | starting tier at 90 or more | Blake's reply: > 90 | first mail looks complete |
| T7 | superseding (stale summary) | slack 84ff828e81ba52e8969c580f49944394 → gmail 1844679607844896665 | R2 | editor bits are in the store builds (Brian) | tooling stripped (mail) | #zombie-design hit first |
| T8 | superseding (3 versions, cross-service) | linear cmt_912bdd42ad5c8d51521f (ZOM-282 note: hp boost still on respawns) → github harmonygames-Games/match3d#401#c_2 → gsheets f_0ba93ae0238d9ed4178212 | R4 | +25% / +50% everywhere, hp boost | Live tab | — |
| T9 | distractor (scope_adjacent) | gsheets f_0ba93ae0238d9ed4178212 tab Next pass | R4 | proposal copied | "as they work today" | — |
| T10 | tool_surface | linear ZOM-42; gslides f_048bf5e69f8e7f1a659a5c | R4 | demotion only on 4 straight losses | ZOM-42 in full | list truncates the description |
| T11 | superseding (3 versions, cross-service) | gslides f_048bf5e69f8e7f1a659a5c → gsheets f_0ba93ae0238d9ed4178212 → slack C090N54TG79/1756912929.304417 | R4 | +25% speed/damage/HP from the deck | Live tab; comment retires the line | — |
| T12 | distractor (lookalike_entity) | trello 683dbef4e319167a802bd888 | R8 | Brian/Vincent as editors | the ZM ROADMAP card | Trello search returns both |
| T13 | cross_reference_gap | gcal evt_91674a9c23d012a9ac34da | R8 | shares only with Robert (and Blake) | invite attendees | — |
| T14 | reuse_exclusion | linear ZOM-199, ZOM-200; gmail 1844695547248860585 | R7 | new ticket, or a comment on ZOM-42 / ZOM-200 | comment on ZOM-199 | — |
| T15 | eliminating_evidence | linear cmt_bb9c4deb176b2c894ca6, cmt_68811c86e67c36e5c2f7; github harmonygames-Games/match3d#243, #265 | R2 | ZOM-173/312 Live from their PRs' runtime files | the notes say which part is theirs | — |
| T16 | distractor (non_authoritative_instruction) | slack C090N54TG79/1759248760.118527 | R6 | posts in #zombie-design | "reply here" | — |
| T17 | distractor (scope_adjacent) | gsheets f_34f0950581934de1278969 | R4 | DD parameters | ZM sheet | "parameter" search |
| T18 | exact_predicate | linear ZOM-257, ZOM-289, ZOM-383, ZOM-209, ZOM-190, ZOM-96, ZOM-24 | R1 | difficulty-sounding Blake tickets counted | no "tiers:" tag | titles first |
| T19 | superseding (cross-service) | slack C08R27X0EAH/1758081917.318539 → gmail 1844679607844896665 | R2 | judged against iOS 0.3.38 | iOS 0.3.49 / Android 0.3.133 | — |
| T20 | exact_predicate | linear ZOM-305, ZOM-352 | R1 | both lives tickets in, or both out | ZOM-305 tagged; ZOM-352 not | — |
| T21 | eliminating_evidence | linear ZOM-282; github harmonygames-Games/match3d#401, #401#c_2 | R3 | ZOM-282 Replaced by #401, or ZOM-254 replaced by #401 | #401 finished ZOM-282; "the first one that did" is ZOM-282 | — |

**Trap independence.** T1/T2/T3/T4/T18/T20 fall to rule 1 on different clauses (comment, window, phrase, duplicates, tag, per-ticket
note); T5/T15 need the notes against the mail; T6 needs the thread reply; T7 the mail over the summary; T8/T9/T11/T17 the enrage source; T10
the full ZOM-42 text; T12/T13 the invite; T14 the write rule; T21 what #401 did. No record states a chain's conclusion: the reply names the
code's check, never a status; notes give a tag or where the change lives, never "editor only" or "live".

## 6 Failure-diversity plan

| Lever (habit it tests) | Rows it decides | Who plausibly misses it (evidence) |
|---|---|---|
| Tags on Blake's off-topic tickets (title triage vs reading all 109) | 4 member rows + counts | runs that triage Blake's 78 non-title tickets by title (reviewer B: rational for a lean run) |
| Gmail thread reply | the starting-tier row and the ZOM-199 comment write | runs that read the first message only (B: 0.65–0.8 found) |
| ZOM-42 read in full (truncated list description) | the demotion row (50% rule, reset) | runs that take the deck / list text (A3 tool surface) |
| Note vs PR file table (ZOM-173, ZOM-312) | 2 status rows | runs that open the PR and trust its runtime files over the note |
| The sheet's Live tab vs Brian's summary and the deck | the enrage row | runs that stop at #zombie-design or the deck body |
| Calendar invite attendees | Brian and Leonard shares | runs that never open Calendar (weak: Douglas 6/6 opened it) |
| Card comment | 5 attack-power rows | runs that read the description only (weak: B saw 12/12 read comments) |
| #401 conversation (ZOM-282 Live; ZOM-254's first replacer) | 2 status/cell rows + the ZOM-254 write | runs that call ZOM-282 Replaced or name #401 for ZOM-254 |

The levers reward different habits (triage discipline, thread replies, full descriptions, PR-vs-note trust, channel replies, calendar),
not one "deep reader" trait. Weight concentration and the projection against the per-write rubric are for `/create-rubric-writing`; the
hardening lessons (memory: Douglas rounds 1–3) are the planned fallback if the pre-check shows one pattern.

## 7 Deliverables and dependent writes

| Write | Service · tool | Content depends on | Requirements |
|---|---|---|---|
| W1 register | gsheets_create_spreadsheet + gsheets_values_update | Tickets tab: 35 rows (ticket, title, Linear state as found, status, replaced by); Rules in force tab: starting tier (> 90), promotion, demotion, level drop after demotion (yes), enrage | R1, R2, R3, R4, R9 |
| W2 placement + shares | gdrive_move_file + gdrive_share_file ×4 | ZM Difficulty folder (Leonard owner, Julia writer only); Robert writer; Leonard, Arthur, Brian commenter | R5, R8 |
| W3 reply | slack_send_message (D05HB64NMQU) | 35 tickets — 23 Live, 8 Editor only, 3 Not shipped, 1 Replaced | R6 |
| W4 tickets | linear_create_comment ×2 | ZOM-199: the build checks CPM > 90, not >= 90; ZOM-254: replaced by ZOM-282 | R7 |

Reuse-vs-create (A8): the comment goes on ZOM-199 (card rule 6 "Same tickets, no new ones"); ZOM-42 (already right) and ZOM-200 (a CPM
debug-menu ticket) are the lookalikes. End states are stated in the card (comments; folder; roles) and the agenda (one sheet, two tabs).

## 8 Service role map

| Service | Role | Load-bearing fact / write | Carrier |
|---|---|---|---|
| slack | anchor DM; Brian's summary; Vincent's post; #401 mirror | ask + reply destination; W3 | ● message |
| trello | H1 card + comment; DD decoy | rules 1–7; attack power | ● card desc / comment |
| gmail | H2 thread | stripped tooling; the > 90 check (reply) | ● thread |
| linear | 109 candidates + notes; ZOM-42; W4 | membership (tag), where a change lives, full tier rules | ● comments (§6b verified); description |
| github | #401 + Blake's comment; #243/#265 tables | ZOM-282 Live; shared-PR split | ● PR comments/body |
| gsheets | H3 monster enrage; W1 register; DD decoy | VarC prefab speed/damage, MonsterBase 0.8/0.8, hp 0 | ● tab grid |
| gslides | Robert's deck f_048bf5e69f8e7f1a659a5c | named tier-rules source (card rule 5) | ● element text |
| gcal | tuning invite | attendees (share list) | ● attendees |
| gdrive | ZM Difficulty folder; W2 | destination, shares | ● metadata |
| gdocs | agenda | one sheet, two tabs | ● body |
| contacts | — | not used | — |
| snowflake | — | not used (ZM telemetry app_version 0.1.x disagrees with the 0.3.x store builds — kept off) | — |
| confluence | — | not used: injection SQL can't edit Confluence (`/injection` F1) | — |

## 9 Call budget

| Phase | Service | Calls | Reason |
|---|---|---|---|
| discovery | slack | 2 | read the ask; resolve the DM |
| discovery | trello | 3 | search the card, read it, read its comments |
| discovery | gmail | 2 | search the store builds mail, open the thread (the > 90 reply) |
| discovery | gsheets | 2 | find the monster enrage sheet; read Live |
| discovery | gslides | 2 | find Robert's deck, read its text |
| discovery | slack | 1 | search #zombie-design for the deck (Blake's correction) |
| discovery | gcal | 2 | find the tuning session, read attendees |
| discovery | gdocs | 2 | find and read the agenda |
| discovery | gdrive | 1 | find the ZM Difficulty folder |
| enumeration | linear | 5 | page ZOM issues created Apr 21 – Aug 31 (~470) |
| rules | linear | 1 | ZOM-42 full spec (4,244 chars; > 90, the 50% rule and the reset past the truncation) |
| rules | linear | 3 (conditional) | ZOM-199/254/282 in full — only if the list truncates them |
| per-record | linear | 109 | one `linear_list_comments` per candidate |
| per-record | github | 3 | #401 conversation; #243, #265 tables |
| writes | gsheets | 3 | create with two tabs; write rows |
| writes | gdrive | 5 | move + 4 shares |
| writes | slack | 1 | reply with counts |
| writes | linear | 2 | comments on ZOM-199 and ZOM-254 |
| read-back | gsheets | 1 | read the register back |

**Unconditional floor 147** (planned 150), 10 services; largest share outside the per-record phase ≈ 30% (Linear). Golden-run rule: a
correct run must read all 109 candidates' notes (membership and status depend on them), so the volume is necessary, not padding.
Risks named by reviewer B and carried to the pre-check: a run that delegates the 109 reads to one subagent counts fewer top-level calls [U];
whether `linear_list_issues`' query searches comment text [U] (if it does, a path search shortcuts membership but not status).

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by |
|---|---|---|---|
| D1 starting tier | > 90 (first 10 levels average CPM; 90 exactly stays on tier 0) | >= 90 (ZOM-199, the page) | newer source: Blake's reply (2025-09-30T13:26:05Z) names the code's check; ZOM-42 agrees; card rule 5 "as they work in the store builds today" |
| D2 ZOM-45 status | Live (the level carries the label at runtime) | Editor only (title "in editor") | the mail strips only level editor / LevelDesigner / debug tooling; the note says the game reads it |
| D3 ZOM-277 status | Editor only (the editor's stats panel average) | Live (gameplay-sounding title) | the note vs the mail |
| D4 ZOM-254 replaced by | ZOM-282 (first later ticket that changed how it works: no HP, speed+damage) | match3d#401 (the last change) | card rule 4 "Name the first one that did" |
| D5 ZOM-282 status | Live (#401 finished what 282 asked: speed and damage, no HP; Blake's #401 comment) | Replaced by #401 (split into two values) | card rule 4 "so it no longer works the way the ticket says": it does; numbers are excluded |
| D6 ZOM-42 status | Live | Replaced by ZOM-199 | card rule 4 explicit |
| D7 ZOM-173 / ZOM-312 status | Editor only (notes: the level objects panel set count; the editor's events) | Live (#243 / #265 file tables include runtime files) | the notes say which part of the shared PR is the ticket's (#243's LevelManager/LevelModel are ZOM-307's slider removal) |
| D8 Blake tickets changed after the clock (ZOM-443 "…item removal … win streak") | not members ("parking this, nothing merged yet", no tag) | member (topic sounds like item removal) | rule 1 membership by the tag |
| D9 share list | Robert edit; Leonard, Arthur, Brian comment | Robert only (named on the card) | card rule 7 "everyone on the tuning session invite" |
| D10 demotion row | 4 losses in a row, or ≤ 50% over up to the last 10; record resets after every move | 4 losses only (page; Robert's Sep 26 "Losing 4+ in a row") | ZOM-42 full text, named by card rule 5 ("and in ZOM-42 itself"); Robert's message does not exclude the 50% rule |
| D11 enrage row | speed and damage per monster (Live tab; MonsterBase 0.8/0.8 for the rest), no HP boost | +50% for every monster (ZOM-282, Brian) / +25% (deck) / Next pass | card rule 5 "as they work in the store builds today" + "Enrage is per monster"; base C08R27X0EAH/1756922765.033199 |
| D12 level drop after a demotion | yes: the current level loads one tier down (ZOM-303) | no (ZOM-293 "Tiering Down Issue" is open) | ZOM-303 Done and #244 merged before the Sep 26 cut; ZOM-293 is a separate open bug |
| D13 reply destination | Leonard's DM | #zombie-design (Vincent) | the ask: "reply here" |

### Reach table (load-bearing records)

| Record | Service | Verdict (`persona_view.py can-see julia_lawson …`) | Note |
|---|---|---|---|
| D05HB64NMQU | slack | YES (channel; the seeded ts is checked at injection) | LB anchor DM |
| C08R27X0EAH/1756922765.033199 | slack | YES (member of private zombie-bugs) | per-monster enrage |
| C0880U9751A/1758921802.962539 | slack | YES (member of private zombie-match3d) | tier moves |
| C0880U9751A/1759182908.627389 | slack | YES | iOS 0.3.49 release |
| C08R27X0EAH/1758081917.318539 | slack | YES | T19 older build |
| C090N54TG79/1759176983.189479 | slack | YES (member of private zombie-design) | motivation |
| C07C2866011/1759075866.111309 | slack | DENIAL-INTENDED: Android 0.3.133 is posted in #executives, which Julia cannot read; alternate_evidence_ids: C0880U9751A/1759182908.627389 | probe (never load-bearing) |
| f_34f0950581934de1278969 | gsheets | YES (shared with the persona) | DD decoy |
| d_8140f09bf9f1b94cb8ee2d | gdrive | YES (Julia's root) | — |
| Linear, GitHub, Trello, Confluence records | unscoped | always visible | — |
| seeded DM ask, both mails (Julia's copy), Julia's invite copy, the monster enrage sheet (Julia owner), agenda and folder (shared with Julia) | planned | checked at injection (`persona_view.py check-sql`) | LB seeds |

**Feasibility.** Writes exist in `Evals/references/tools/catalog.json`: `gsheets_create_spreadsheet` (+ `gsheets_batch_update` for a
second tab), `gsheets_values_update`, `gdrive_move_file`, `gdrive_share_file` (writer / commenter), `slack_send_message`,
`linear_update_issue`, `linear_create_comment`. Julia edits the folder (writer) and owns the new sheet; the folder grants no other writer,
so the four shares set the end state (reviewer A #15). **Precedence:** load-bearing facts only in ● carriers (Linear comments verified per
§6b; Trello card desc/comments; Gmail threads; Sheets tabs; Slides element text; GCal attendees); GCal descriptions unused. **Prompt
naturalness:** the prompt names only "Leonard's difficulty baseline ask" (Slack DM), the deadline (Monday's tuning session) and the
deliverable kinds (register, reply, ticket fixes); it must not name the card, the mail, the sheet, the page, the folder, any ticket id, the
attack-power amendment, the > 90 check or any count. **Grading devices:** exact member set (35) and status multiset (23/8/3/1); ≤ 5 spot
checks per group + one volume criterion; one criterion per replaced-by cell (1), per rules row (5), per share (4), the folder, the tabs, the
reply counts and each ticket comment (2).

**Coherence rail.** Every §1a row dispositioned; designed disagreements are dated human claims with named later records (ZOM-199 →
reply; ZOM-282 note → #401 comment; page → comment / sheet; Brian's summary → mail / sheet). Companions planned: Linear notes before each issue's
updated_at (checked: no exceptions); #401 comment + its `commented` timeline event (harmonygames-Games/match3d#401#ev_7) + its Slack
mirror in #zombie-prs, a companion only (PR updated_at 2025-10-24 already covers it); Trello createCard/commentCard actions and badges; one GCal copy per attendee; gmail copy per recipient mailbox with label
counters; Drive sharing for folder, sheet and agenda; Slides deck version row.

## 11 Record plan for /create-injection

| Seed | Table(s) | Id(s) | Time (UTC) | Author | Notes |
|---|---|---|---|---|---|
| DM ask | slack.slack_messages | 6f77386571537f0bd88c959bdc216f94 (D05HB64NMQU/1759261706.530914) | 2025-09-30T19:48:26Z | Leonard | `planned_text.json` S_ASK |
| Brian's summary | slack.slack_messages | 84ff828e81ba52e8969c580f49944394 (C090N54TG79/1759185077.402611) | 2025-09-29T22:31:17Z | Brian | S_ROBERT_SUM (key kept) |
| Vincent's post | slack.slack_messages | 0282d920d9ff69fefb74a4ae417b0e18 (C090N54TG79/1759248760.118527) | 2025-09-30T16:12:40Z | Vincent | S_BRIAN_POST (key kept) |
| #401 mirror | slack.slack_messages | 5313e8da22604987e53ba497dc709655 (C093LEZGF6J/1756141351.508113) | 2025-08-25T17:02:31Z | GitHub app | threaded under #401's opened post |
| H1 card | trello.trello_cards + trello.trello_actions | 68daca5871dba40417a00383; createCard 68daca5845e48874fb98e25a | 2025-09-29T18:05:12Z | Leonard | list "Oct 21" 6851a677e090018224fb8c7f; H1_DESC |
| H1 comment | trello.trello_actions (commentCard) | 68dbfa4362a051efb5e0ae45 | 2025-09-30T15:41:55Z | Leonard | H1_CMT; badges.comments 1 |
| DD decoy card | trello.trello_cards + trello.trello_actions | 683dbef4e319167a802bd888; 683dbef4991df7f0987ddb73 | 2025-06-02T15:10:44Z | Leonard | DD board, list "Rebirth (June)" |
| store builds mail | gmail.gmail_threads + gmail.gmail_messages (×5 mailboxes) | thread 1844679607844896665; reply 1844695547248860585 | 09:12:44Z / 13:26:05Z Sep 30 | Arthur ("Blake") | to Julia, Leonard, Robert, Brian; under jlawson@, leonard@, robert@, blake@, brian@ |
| monster enrage sheet | gdrive.drive_files + gsheets.sheets_spreadsheets + gsheets.sheets_sheets ×3 | f_0ba93ae0238d9ed4178212 | created 2025-08-26T17:40:12Z, modified 2025-09-02T19:12:40Z | Julia | in d_96489e1e00a56685625939; shared with Arthur, Robert, Leonard |
| agenda | gdrive.drive_files + gdocs.docs_documents | f_9ec79682ff351aa466364a | 2025-09-29T18:31:09Z / 2025-09-30T11:04:37Z | Leonard | shared with the 4 attendees |
| folder | gdrive.drive_files | d_96489e1e00a56685625939 | 2025-06-13T15:02:11Z | Leonard | Julia writer only |
| Slides deck | gdrive.drive_files + gslides.slides_presentations / slides_pages / slides_page_elements | f_048bf5e69f8e7f1a659a5c | 2025-06-16T14:10:33Z | Robert (user_EMPLOYEE_0016) | space_PROD |
| Slack message | slack.slack_messages | C090N54TG79/1756912929.304417 | 2025-09-03T15:22:09Z | Arthur | CC_ART_BODY |
| tuning invite | gcal.gcal_events ×5 | evt_dd24af1fb48e6c536f48a4, evt_91674a9c23d012a9ac34da, evt_56b665fee3295cce4b77d3, evt_18d9e925bfe0da49dcc9f5, evt_6a462dfd25e2f70ed73bcf | created/updated 2025-09-29T18:24:51Z; start 2025-10-06T17:00Z | Leonard | ical 26fce3dc380d9da1343bcccc6072f03e@hg4 |
| #401 comment | github.github_pr_comments + github.github_timeline_events | harmonygames-Games/match3d#401#c_2; #ev_7 | 2025-08-25T17:02:28Z | EMPLOYEE_0025_GITHUB_USERNAME | Slack mirror in #zombie-prs (INT-01) |
| 109 notes | linear.linear_comments | `minted_ids.json` LIN_NOTES (cmt_ + 20 hex) | before each issue's completed/canceled/updated time | Blake / owners / Vincent | no file names; PR-linked notes cite their PR; 4 "tiers:" tags |

Rows planned: 4 Slack + 4 Trello (2 cards, 2 create actions) + 1 Trello comment + ≈ 12 Gmail (2 messages × 5 mailboxes + threads) + 6
Drive/Sheets/Docs + 3 sheet tabs + 7 Slides/Drive rows for the deck + 1 Slack message + 5 GCal + 2 GitHub + 109 Linear ≈ **149 INSERTs** (≥ 120), 10 schemas.

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| github | INT-01 | Slack mirror in #zombie-prs | seeded: the #401 comment (2025-08-25) is inside the match3d window; mirror threaded under #401's opened post, real login |
| github | INT-03 | linear[bot] PR comment | none: #401's title/branch names no Linear key |
| github | INT-23 | CodeRabbit | none seeded |
| linear | INT-04 / INT-05 | Slack / mail notifications | none: base has no notification for Linear comments (0 base comments) |
| gcal | INT-11 | invitation mails | none (`no_notify`): most base meetings have none |
| gdrive / gsheets / gdocs | INT-13 | Drive Slack app DMs | none: DM-only, optional for shares |
| trello | INT-21 | Slack bot posts | none: no Trello integration exists |
| slack | INT-22 | Slack e-mail notifications | none: sparse in the base |
| gmail | — | label counters | update gmail_label_user_counters per mailbox |
| gslides | — | Drive row | the deck's drive_files row with identical sharing |

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
  [ok] anchors: 1 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 13 fragments; need ≥ 12
  [ok] ask_fragment_services: 9 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 10 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 9 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 109; need ≥ 30 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 2 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 116; need ≥ 30
  [ok] call_budget: unconditional (verified) floor 147 of 150 planned calls (3 conditional on unverified tool behaviour count 0); need floor ≥ 100 (Long Horizon; plan ~600 for headroom)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 29% (≤ 50%)
  [ok] traps: 21 traps across 8 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 7 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 6 supersessions (5 with versions in ≥ 2 services, 3 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 6 distractors of 5 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 8 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 8 chains with 8 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 10 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 9 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 4 writes over 4 services; each must depend on findings
  [note] call budget: planned total 150, unconditional floor 147 — the conditional rows count once their tool behaviour is verified (then drop conditional_on)
```

**Lazy-solver pass** (one broad search per service, first hits, no replies/comments, stops at the first conclusion, uses every bulk
shortcut). Points it would still score and the fix:
- *Title filter* — 26 of 35 members (31 with the comment); the 4 tagged members need notes on Blake's off-topic tickets.
- *Status by Linear state* — Done → Live scores the 23 Live rows; Editor only (8) and Replaced (1) differ; the status sets are graded
  as exact multisets, so the shortcut fails the set rows. Accepted: per-ticket Live rows are cheap; weighting goes to the decisive rows at
  rubric time (B #1).
- *Brian's summary* — wrong on the editor tooling and enrage; right by accident on nothing graded.
- *First mail message* — gives the stripped tooling, not the > 90 check.
- *Share from the card* — Robert only; the others need the invite.
**Literal-value sweep.** "> 90" as the build's check appears only in the reply (ZOM-42 says it in prose: "> 90"); the per-monster values only on the
Live tab; "attack power" in the card comment and base titles; the 50% demotion rule only in ZOM-42's base description; "Brian" as a
recipient only in the invite attendees. **Wording sweep.** "shipped", "Live", "Editor only", "Replaced" appear in no note; notes name no file. **"The rest stands" check.** The card comment ends "rest of the card stands"; the reply changes
one clause; no later record re-asserts the +25% / +50% enrage or the >= 90 threshold.

### Self-review

Walked in order: `Evals/1_Prompt_Eval.md` §2.1 (Unique Ground Truth), §2.2 (Feasibility), §3.2 (Cross-Service Coherence) and
`Evals/0_Injection_Quality_Eval.md` Check C, against the design above.

| # | Item (QC category / decision point) | Verdict | Counter-reading (strongest case that it FAILS) | Resolution with evidence |
|---|---|---|---|---|
| 1 | temporal | PASS | ZOM-282 closed 06-21 "NOT HP" but #401 removes health boosts on 08-25 | dated claims: Blake's note cmt_912bdd42ad5c8d51521f (06-21) says the boost stays on respawns; his #401 comment harmonygames-Games/match3d#401#c_2 (08-25) says #401 finishes it |
| 2 | semantic | PASS | Leonard's "25% more HP 25% more speed" (C090N54TG79/1759173062.702099) reads as the current values | a proposal ("we should show what multiplier boosts … etc."); the VarC prefab values (commit 85d1a406) and #401 show per-monster speed+damage, HP unchanged |
| 3 | cross-service referential | PASS | notes may contradict the git history (re-check #1–#2, #3, #8) | v4 notes name no file; PR-linked notes cite their PR (harmonygames-Games/match3d#243, #265, #282 …, agreeing with each table); the tag is a judgment, not a code claim |
| 4 | quantitative | PASS | sheet values vs the prefabs and Robert's own messages (C0880U9751A/1750370473.240179 "+100%", C090N54TG79/1754252455.237699 "+60%") | Live tab = VarC prefab values at the clock (re-check #4); History follows commit 84780b8d and harmonygames-Games/match3d#401; the deck is dated before Robert's Jun 19 change |
| 5 | state/lifecycle | PASS | ZOM-199's text (>= 90) disagrees with the build | designed: Blake's reply 1844695547248860585 (a dated human claim) names the code's > 90, as ZOM-42 says; the agent's comment on ZOM-199 records it |
| 6 | state/lifecycle (L03) | PASS | ZOM-292 / ZOM-387 Todo with merged PRs | dated notes (2025-07-04T03:07:46Z; 2025-07-27T20:40:47Z) explain the open umbrella tickets; manifest L03 dated_claim; not modified |
| 7 | identifier/format | PASS | `usr_Robert` breaks the usr_<16hex> scheme | I10 base precedent (ZOM-293 assignee usr_Robert in linear/data.json) |
| 8 | other | PASS | EMPLOYEE_0032 tickets carry Vincent's notes | X02/I05: the token person is never voiced; Vincent's ZOM-254 note makes no number claim |
| 9 | D1 starting tier | PASS | >= 90 is defensible: ZOM-199 and the deck say it, and ZOM-199 is the later ticket | the reply (2025-09-30T13:26:05Z) states the build's check; the code at commit 85d1a406 is `cpm > 90.0f`; ZOM-42 says > 90 |
| 10 | D2 ZOM-45 | PASS | "Editor only" is the natural reading | note cmt_bed381141007e04f1aac: the level carries the label at runtime, the game reads it on load |
| 11 | D3 ZOM-277 | PASS | the attack-power average is a gameplay number | note cmt_b0aa45d307c981ce4487: the editor's stats panel, nothing changes in the game |
| 12 | D4 ZOM-254 replaced by | PASS | #401 is "the" replacement | card rule 4 "Name the first one that did" → ZOM-282 (created 2025-06-19) |
| 13 | D5 ZOM-282 | PASS | Replaced: #401 split one value into speed and damage | rule 4 "so it no longer works the way the ticket says": after #401 it does what ZOM-282 asked; Blake's harmonygames-Games/match3d#401#c_2 |
| 14 | D6 ZOM-42 | PASS | ZOM-199 changed ">" to ">=" | card rule 4 explicit; and the build kept ZOM-42's > 90 |
| 15 | D7 ZOM-173 / ZOM-312 | PASS | #243 includes LevelManager/LevelModel; #265 includes GameEvents | notes cmt_bb9c4deb176b2c894ca6 / cmt_68811c86e67c36e5c2f7 assign the runtime parts (ZOM-307's slider removal; the editor's events) |
| 16 | D8 post-clock Blake tickets | PASS | ZOM-443 may be counted | pre-clock note "parking this, nothing merged yet", no tag |
| 17 | D9 share list | PASS | "everyone else" may mean everyone at the company | rule 7 binds "everyone on the tuning session invite" (evt_91674a9c23d012a9ac34da attendees) |
| 18 | D10 demotion row | PASS | Robert's Sep 26 message (C0880U9751A/1758921729.009549) gives only the 4-loss streak | ZOM-42's full text (and WinRateRule at the clock, re-check) adds the 50% rule and the reset |
| 19 | D11 enrage row | PASS | the Next pass tab is on the same sheet | card rule 5 "as they work in the store builds today" (trello:68daca5871dba40417a00383); f_0ba93ae0238d9ed4178212 Next pass header "proposal" |
| 20 | D12 level drop | PASS | ZOM-293 "Tiering Down Issue" (Todo) suggests tier-down is broken | ZOM-303 Done with match3d#244 merged before the cut; TierManager at commit 85d1a406 applies the drop; ZOM-293 is a separate open bug (Not shipped row) |
| 21 | D13 reply destination | PASS | Vincent's later request | the ask says "reply here" (D05HB64NMQU/1759261706.530914) |

Gate output re-run for this review (`hardness_gate.py --design`, verbatim):

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
  [ok] anchors: 1 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 13 fragments; need ≥ 12
  [ok] ask_fragment_services: 9 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 10 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 9 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 109; need ≥ 30 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 2 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 116; need ≥ 30
  [ok] call_budget: unconditional (verified) floor 147 of 150 planned calls (3 conditional on unverified tool behaviour count 0); need floor ≥ 100 (Long Horizon; plan ~600 for headroom)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 29% (≤ 50%)
  [ok] traps: 21 traps across 8 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 7 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 6 supersessions (5 with versions in ≥ 2 services, 3 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 6 distractors of 5 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 8 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 8 chains with 8 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 10 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 9 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 4 writes over 4 services; each must depend on findings
  [note] call budget: planned total 150, unconditional floor 147 — the conditional rows count once their tool behaviour is verified (then drop conditional_on)
```

**Facts re-read through the tools** (not from notes): ZOM-42 full description, ZOM-199/254/282/292/303/387 fields, match3d#243/#244/#265/#271/
#282/#319/#401/#404 bodies and CodeRabbit file tables, commits 84780b8d/e54e7e4e/737e0278/b511fcbc and the clock tree (85d1a406, via the re-check's
read-only pack reader), Slack C0880U9751A/1758921802.962539,
C08R27X0EAH/1756922765.033199, C090N54TG79/1759173062.702099, C08R27X0EAH/1754000781.512949, and the `persona_view` verdicts in the reach table.

Unresolved: (1) whether the platform renders base tickets changed after the clock (ZOM-359, ZOM-400, ZOM-427, ZOM-438, ZOM-439, ZOM-441,
ZOM-443, ZOM-458, ZOM-468) in their pre-clock state is unverified — non-members either way, never load-bearing; (2) the projected average
(reviewer B: 82–90% on v1; v4 has fewer decisive rows) must be re-projected on the per-write rubric at `/create-rubric-writing` and confirmed by the Opus pre-check;
plan for one hardening round; (3) the 3 conditional rule reads, subagent delegation of the 109 reads, and comment-text search in
`linear_list_issues` are verified only by the pre-check.

```
STAGE GATE scenario: PASS — Task_Authoring-2/task_inputs · 01_Scenario_Design.md#6b5baef65a80 · 01_Hardness_Manifest.draft.json#0c5dc769f675 · blocking 0 · warnings 0 · checks 26
[PASS] structure.outputs: 2 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 15/15 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 29/29 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 14/14 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 29/29 items carry a source pointer (min 90%)
[PASS] evidence.record_plan: 22/26 items carry a source pointer (min 80%); unsourced e.g. L557: 'store builds mail | gmail.gmail_threads + gmail.gmail_messages (×5 mailboxes) | thread 184'
[PASS] evidence.active_speakers: 9/9 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for julia.lawson@harmonygames.co and matches the re-run (158 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 21 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 9 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (9 INT ids, services ['gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts ['LIN-CQ12', 'LIN-CQ13']; trap_catalog ['C01', 'C02', 'D07', 'K02', 'N01', 'N02']
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: dual red team present (01b_Redteam_Review.md + .second.md)
[PASS] reach.scenario: 8 scoped load-bearing ids YES for julia_lawson; 1 denied/unverified probe(s), not load-bearing, each with YES alternate_evidence_ids
[PASS] review.counter_readings: 21 evidenced counter-readings (of 21 found; need ≥ 20) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```




## 13 Red team (dual)

Two independent reviewers ran on v1/v2 as subagents (reviewer A, validity: `01b_Redteam_Review.md`, Blocker 3 · Major 14 · Minor 8; reviewer
B, difficulty and volume: `01b_Redteam_Review.second.md`, Blocker 2 · Major 11 · Minor 5). The external `redteam_review.py` endpoint is not
configured here (no `REDTEAM_*` variables), so the reviews were produced in-session, as for the Douglas task. Dispositions (v3):

| Finding | Source file | Disposition with evidence |
|---|---|---|
| A1 ZOM-282 Live reading | 01b_Redteam_Review.md | adopted in v4: ZOM-282 Live (#401 finished it; Blake's #401 comment); two-reading D5 |
| A2 promotion window 12 contradicted | 01b_Redteam_Review.md | fixed: 12-attempt claim removed; promotion 80% over up to 10 (ZOM-42; C0880U9751A/1758921802.962539) |
| A3 ZOM-23 → #341 conflicts with MF35 A/B | 01b_Redteam_Review.md | fixed: ZOM-23 Live, neutral note (C08R27X0EAH/1754000781.512949) |
| A4 base Slack vs enrage values | 01b_Redteam_Review.md | fixed: enrage per monster (sheet), no global value; Leonard's line dispositioned as a proposal (§1a) |
| A5 demotion ambiguity; rule 4 numbers | 01b_Redteam_Review.md | fixed: demotion row carries both ZOM-42 rules + reset; rule 4 "its rules go on the rules tab" |
| A6 ZOM-254 two replacers | 01b_Redteam_Review.md | fixed: rule 4 "Name the first one that did" → ZOM-282 |
| A7 Vincent's ZOM-254 note | 01b_Redteam_Review.md | fixed: "blunder enrages the monsters on the board now" (no +25% claim) |
| A8 ZOM-312 vs #265 | 01b_Redteam_Review.md | fixed: note cites #265 and says its events are the editor's; mail rule is by tooling; D7 |
| A9 ZOM-173 vs #243 | 01b_Redteam_Review.md | fixed: note cites #243 and claims only the set count in the level objects panel (re-check R8) |
| A10 ZOM-352 vs #282; WinRateRule.cs | 01b_Redteam_Review.md | fixed: ZOM-352 not a member (cites #282, no tag); no note names a file in v4 |
| A11 ZOM-209 Live reading | 01b_Redteam_Review.md | fixed: ZOM-209 not a member (AlgoLevelSettings only) |
| A12 rule 6 ambiguity | 01b_Redteam_Review.md | fixed: rule 6 separates the Todo move from the Replaced comment and leaves Editor only alone |
| A13 remote flag vs base | 01b_Redteam_Review.md | fixed in v4: no flag or define; ZOM-303 Live (re-check R1) |
| A14 DM language; "Blake" | 01b_Redteam_Review.md | partly: card, mail and ask use "Blake"; the ask stays English (Leonard's English work posts; D05HB64NMQU has English lines) — accepted |
| A15 folder shares | 01b_Redteam_Review.md | fixed: folder grants only Julia (writer) under Leonard |
| A16 design/manifest out of sync | 01b_Redteam_Review.md | fixed: this v3 document and manifest regenerated from `truth.json` |
| A17 open tickets as members | 01b_Redteam_Review.md | fixed: rule 1 "open, cancelled and never-merged ones are in, as Not shipped" |
| A18 neutral notes vs PRs | 01b_Redteam_Review.md | fixed: LINKED notes cite their PRs (ZOM-244 #258/#283, ZOM-345 #289, ZOM-387 #319 …); other notes name no file |
| A19 ZOM-303 state cell | 01b_Redteam_Review.md | fixed: "Linear state (as you found it)"; moot in v4 (no state write) |
| A20 rules-row set | 01b_Redteam_Review.md | fixed: rule 5 names the level drop; 5 rows |
| A21 knobs steps | 01b_Redteam_Review.md | fixed: History follows commit 84780b8d and #401's merge date |
| A22 #404 HP boost | 01b_Redteam_Review.md | dispositioned: algo-level defaults, not blunder enrage (§1a) |
| A23 requirement text; K12/K3 quotes | 01b_Redteam_Review.md | requirements carry text; K12 now quotes "in ZOM-42 itself" from the card |
| A24 counts unspecified | 01b_Redteam_Review.md | fixed: the ask asks for the total and each status |
| A25 page_zm3d_gdd visible | 01b_Redteam_Review.md | accepted: not named by any rule; the card names "the dynamic difficulty deck"; its stored versions start 2025-10-02 |
| B1 average 82–90% | 01b_Redteam_Review.second.md | mitigated: tagged off-topic members, ZOM-42 truncation, PR-vs-note, the > 90 thread reply, per-monster sheet; re-projection at rubric time; hardening planned |
| B2 call floor via triage | 01b_Redteam_Review.second.md | fixed: tagged members have off-topic titles and difficulty-sounding ones are untagged, so triage loses rows |
| B3 card comment not a lever | 01b_Redteam_Review.second.md | accepted (weak lever, kept for coverage) |
| B4 rule 6 ambiguity | 01b_Redteam_Review.second.md | fixed (see A12) |
| B5 reply names the answer | 01b_Redteam_Review.second.md | fixed: the reply states the code's > 90 check; the rules row and the ZOM-199 comment still need the agent to apply it |
| B6 replaced-by stated in notes | 01b_Redteam_Review.second.md | fixed: those replacements removed; the remaining one (ZOM-254 → ZOM-282) needs the tickets and #401 |
| B7 self-advertising traps | 01b_Redteam_Review.second.md | partly: Brian's summary is wrong on editor tooling and enrage; Next pass header says proposal (accepted for fairness) |
| B8 thin Confluence lever | 01b_Redteam_Review.second.md | changed: the deck now omits the 50% rule (ZOM-42 lever) and Blake's message retires the blunder line |
| B9 bulk shortcuts [U] | 01b_Redteam_Review.second.md | carried to the pre-check (§9 risks) |
| B10 fake file paths | 01b_Redteam_Review.second.md | fixed in v4: no note names a file (re-check R2/R3 showed even real paths conflict with the history) |
| B11 one or two failure patterns | 01b_Redteam_Review.second.md | mitigated: levers on different habits (§6) |
| B12 more per-ticket decisive facts | 01b_Redteam_Review.second.md | partly: PR-vs-note rows and off-topic members added; more at hardening if needed |
| B13 ZOM-282/254 debatable | 01b_Redteam_Review.second.md | fixed: ZOM-282 Live; ZOM-254 → ZOM-282 by rule 4 "the first one that did" (D4, D5) |
| B14 stated conclusions in the card | 01b_Redteam_Review.second.md | accepted for fairness (ZOM-42 rule, duplicates) |
| B15 tell in note wording | 01b_Redteam_Review.second.md | fixed: no trailing "only"; the tag is the only marker, and only the rule names it |
| B16 subagent risk [U] | 01b_Redteam_Review.second.md | carried to the pre-check |
| B17 count cascade | 01b_Redteam_Review.second.md | for the rubric plan (separate count rows from set rows) |
| B18 window traps cost no marks | 01b_Redteam_Review.second.md | accepted (boundary hygiene, not difficulty) |

**Re-check of v3 against the git history** (`01b_Redteam_Recheck_v3.md`, Blocker 2 · Major 4 · Minor 4) and the v4 dispositions:

| Finding | Source file | Disposition with evidence |
|---|---|---|
| R1 ZOM-303 level drop is live in code (no define anywhere) | 01b_Redteam_Recheck_v3.md | fixed: ZOM-303 Live; the define lever, the #244 comment and the Todo write removed; D12 |
| R2 path members' file claims false against the history (CPMTierManager.cs post-clock; TierManager commit dates) | 01b_Redteam_Recheck_v3.md | fixed: no note names a file; membership is Blake's "tiers:" tag; ZOM-24 dropped |
| R3 StatsPanel.cs commit after ZOM-277/250 closed | 01b_Redteam_Recheck_v3.md | fixed: notes describe the editor's stats panel without a file |
| R4 sheet values vs prefabs; History wording | 01b_Redteam_Recheck_v3.md | fixed: Live tab = VarC prefab values at the clock; History reworded |
| R5 starting tier > 90 vs >= 90 | 01b_Redteam_Recheck_v3.md | turned into the designed source conflict: the reply settles > 90; ZOM-199 gets the correction comment (C5, T6, R7) |
| R6 ZOM-282 Live reading | 01b_Redteam_Recheck_v3.md | adopted: ZOM-282 Live; Blake's #401 comment confirms; only ZOM-254 is Replaced |
| R7 Robert's page/summary vs his messages | 01b_Redteam_Recheck_v3.md | fixed: page dated 2025-06-16 (before his Jun 19 change); the summary is Brian's, no Robert number claims |
| R8 ZOM-173's half of #243 | 01b_Redteam_Recheck_v3.md | fixed: note claims the set count in the level objects panel; slider removal and model changes are ZOM-307's |
| R9 ZOM-312 GameEvents literal reading | 01b_Redteam_Recheck_v3.md | accepted with the note ("the new events are the ones the editor listens to") and the mail's "level editor or debug tooling" |
| R10 "only #244 touches the folder" ignores direct commits | 01b_Redteam_Recheck_v3.md | fixed wording: "among the 215 PRs with file tables"; no claim rests on it now |

**`/injection` review of attempt 6adfee3ef9092601a61245bb (FAIL) and the v5 dispositions:**

| Finding | Source file | Disposition with evidence |
|---|---|---|
| F1 Confluence rows not injectable | /home/sumit/Downloads/6adfee3ef9092601a61245bb_0_injection.md | fixed: the three confluence.* INSERTs removed; Robert's write-up is the Slides deck f_048bf5e69f8e7f1a659a5c (Robert, 2025-06-16, shared with Julia, Leonard, Arthur, Brian); Blake's correction is the #zombie-design message C090N54TG79/1756912929.304417 (2025-09-03, after #401's 2025-08-25 merge); card rule 5 names "Robert's dynamic difficulty deck" |
| F2 Trello idShort 211 before #201–#210 | /home/sumit/Downloads/6adfee3ef9092601a61245bb_0_injection.md | fixed: the DD card 683dbef4e319167a802bd888 and its createCard 683dbef4991df7f0987ddb73 are re-dated 2025-06-02T15:10:44Z (after #210 on 2025-05-27) on list "Rebirth (June)" 65eb4f4e26cfce07d665a38e; text "For the spring difficulty pass" |
| A1 linear_comments.sequence | /home/sumit/Downloads/6adfee3ef9092601a61245bb_0_injection.md | kept: `references/universe_schema_live.json` (platform export) lists `sequence integer` on linear.linear_comments; the eval's 8-column snapshot is the older one |
| A2–A5 advisories | /home/sumit/Downloads/6adfee3ef9092601a61245bb_0_injection.md | no change: not defects by the report's own reading |

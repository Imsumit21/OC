# P2 deep recheck, rev12: services, data and access

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
SQL reviewed: sha256 b5ccbfa577fc9f2c8f6eb3098f8d62a16623d799f41d11285de8227f1bed60d3 (confirmed). Never executed. Prompt unchanged (diff empty).

**Result: 0 fail-level, 0 low-impact, 3 advisory.** From this pass, Cross-Service Coherence moves from NON-FAIL 3 to PASS 5. Feasibility, Persona access, Data exists and Tool use and cross-service stay clean.

- DR1: downgraded from low-impact to advisory only.
- DR2: unchanged, advisory only.
- DR3: new, advisory only.

Checked: 7 changed or new statements of 111 (81 inserts, 30 updates). The other 104 are byte-identical to rev11 and keep their rev11 result. `hg.py lint`: FAIL 0, CHECK 0.

## Diff: every changed and new statement

| Statement | Change | Test | Result |
|---|---|---|---|
| `docs_documents` brief, Span | "closing 23:59 UTC on its last day" now covers every window | Fits the Nov 2 23:59 clip and Season Pass Oct 31 23:59 to Nov 1 00:00 | Clean |
| Brief, Scope | "and the shop rotation is not a beat" | Reference resolves: `Assets/Store/Store/RotatingShopManager.cs`, Vincent 2025-09-08 "rotating shop" | Clean |
| Brief, Held | "keeps its usual windows and weeks" | No data dependency | Clean |
| Brief, Push copy | "(Login Calendar and Weekly Rankings are fine)", "what its row is missing" | PNs Beta row 12 "Login Calendar update", row 14 "Weekly Rankings Reset!". Same-beat line in "When a beat starts" still agrees | Clean |
| Brief, `style_runs` | All offsets moved | All 9 runs land exactly on their headings. Body is 3,090 characters | Clean |
| `harmonygames-Games/match3d#468#rc_38` | Adds "and need to be in before the beta" | See DR3 | Advisory |
| Slack mirror `78aa8ed77c0bd7b8a3fad227b22bc3fb` | Same text | Unescaped mirror text equals rc_38 exactly | Clean |
| `cmt_zom465_3` | "the master VFX list was ticked before that event merged" | See below | Clean |
| `cmt_zom563_1` | Now Douglas, 18:17:05Z | See the Douglas test below | Clean |
| `cmt_zom563_2` | Vincent's closing comment re-keyed, sequence 2 | Same text and time. `updated_at` and `completed_at` still 22:04:33Z | Clean |
| Trello `68dac8204f1e9a3b7c2d5e61` | Adds `idCard` and `textData` | Valid JSON, matches base commentCard shape | Clean |

`cmt_zom465_3` detail:
- ZOM-521 post-SQL still has "- [X] Live-ops icons appearing on the screen and animations on these icons".
- Calvin updated that ticket in base on 2025-09-17 (`D0770ET6WBW`, 15:51:55: "I've updated the Master ticket VFX implementation").
- #468 merged 2025-09-29T16:13:50Z, so "ticked before that event merged" holds.

## Douglas's ZOM-563 comment, tested

Record: `cmt_zom563_1`, author `usr_cd7849ec043ab3da` (Douglas, the assignee), 2025-09-30T18:17:05Z: "Prod has the teams and social changes now. That update carried only these, the Collect & Win server windows wait for the Oct 8 release."

| Against | Quoted evidence | Result |
|---|---|---|
| His DM | `D079SNE2TL4`, 18:16:33: "Ok, I updated the prod environment with the latest teams/social changes, let me know if you are still getting those issues". Ticket started_at 18:14:25 | Agrees, 32 seconds later |
| All his other messages, Sep 29 to Oct 1 | Google login setup and Season Pass dev debugging only. No message says Collect & Win was deployed | No conflict |
| Sep 29 notes | "It doesn't sound like a full day task." / "Uh no it's not." | Later record overrides a plan. See DR1 |
| Owen | `D05SG9H1CFM`, 2025-09-26 21:00:25: "Igual no va para release ahora". 2025-09-30 22:00:12 asks only about `/api/win-and-collect` join timing, then "estoy agregando eventos de analytics". Owen says nothing about prod after Sep 26 | No conflict |
| Confluence calendar | `page_liveops_calendar` (v3, 2025-09-29): "not yet live" and "Windows are cron expressions in the CDK stack and do need a deploy to change." | Agrees |
| "carried only these" vs git | `zombies-game-cdk/bin/zombies-game-cdk.ts` defines separate `ZombiesGameCdkStack` and `NakamaStack`. `constructs/nakama.ts` builds its own image from `../../../nakama`. Douglas, 2025-09-12: "I just need to make a deployment of the Nakama component" | A social-only deploy is possible, and it would not touch the windows |
| GCal and #470 | "Oct 8" and "next backend release" | Agrees |
| Base mentions of Oct 8 | No Slack message since Sep 1, no event dated in October on Douglas's calendar (recurring series not expanded), no out-of-office message from him since Sep 15 | No conflict |

Limit: the latest teams commit 3345557 touches `nakama/js-module/src/player.ts` and also `player_controller.ex`. If the Sep 30 fix had needed that app-stack change, a deploy from main would carry Collect & Win. No record shows that, and the Sep 16 "Deployments are done, ready for testing on both envs" may have already shipped it. Not demonstrated either way.

## Findings

Format: `DR# | pass | checklist section | quoted prompt sentence | record path, id and quoted value | Eval dimension or issue type | proposed score or severity`

**DR1 | P2 | deep_recheck P2, Eval 1 §3.2 | "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." (brief: "A beat starts with the first window that opens after its server windows are live on prod, the backend release instant read in UTC") | records below | Cross-service Referential | ADVISORY ONLY (was low-impact in rev11)**

Injected side:
- #470 `rc_10`, 2025-09-30T15:51:06Z (unchanged): "Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next backend release."
- GCal `evt_5c1e83a7d94b02f6c8e31a` (unchanged), created 2025-09-24, updated 2025-09-26: "The server windows that are still on the DEV stack go live with this release"
- `cmt_zom563_1` (new): "That update carried only these, the Collect & Win server windows wait for the Oct 8 release."

Base side, gdocs `f_b7aae618602a7ccc0cc9a7` (Sep 29 notes, Leonard, private):
- [PERSON_NAME_0357]: "we should probably try to really hard to get the van collect out today."
- [PERSON_NAME_9942]: "Uh for vin collect it needs to be deployed to pro servers."
- [PERSON_NAME_0357]: "Okay, so maybe that's something Douglas can help me with today. Douglas, is There anything else on your plate? It doesn't sound like a full day task."
- [PERSON_NAME_0612]: "Uh no it's not."
- Next step: "[PERSON_NAME_0612] will help [PERSON_NAME_0357] to deploy the win and collect to pro servers"
- Speaker tokens are inferred: 0357 is Leonard per Frederick's mail copy, 0612 answers when Douglas is addressed, 9942 from the QA remarks.

What happened to the three rev11 tension points:

1. **"Next backend release" literally being the 18:16 update: closed.** Douglas now says that update "carried only these".
2. **Sep 29 same-day plan vs Oct 8: closed as an inconsistency, residual oddity only.**
   - The missing record I named in rev11 now exists in substance: dated, from the deployer, after the plan, naming Oct 8.
   - Douglas confirmed the size of the task, not a date. Leonard said "maybe". The next step has no date.
   - A slipped plan that a later owner record supersedes is not a contradiction.
   - Residual: the Oct 8 event predates the meeting and nobody cites it there, and no record says why the plan moved. That is an absence.
3. **"Season Pass on prod, Collect & Win DEV only" having no matching revision on main: residual, base-side.**
   - `SEASON_PASS_SCHEDULE` (d970303, Sep 5) was added after `WIN_AND_COLLECT_GROUP_1_SCHEDULE` (adb56ad, Sep 1).
   - This shows what is in the repo, not what prod runs. No record names the revision on prod.
   - Base itself says DEV only: Vincent on Sep 29, Confluence "not yet live", Douglas's Sep 26 question about deploying.
   - It is not caused by the injection and is not demonstrated.

Why not low-impact: no two records now state different facts. Every persona-visible record agrees on Oct 8, and every hidden record is compatible with it. DR1 would return to low-impact only if a record showed the windows on prod or a dated commitment before Oct 8. I found neither.

**DR2 | P2 | §3.2 | same sentence (brief: "An established failure holds it; an unverified one does not.") | injected Slack `e343557b2e94a1701251ebd079e6f0ce` (unchanged), Leonard: "Ran this again on an S23 Ultra in the cloud device farm, live Android build" vs base #admin_foundersonly, 2025-08-07 22:32:40, Leonard: "I canceled BrowserStack, just to make sure we don't get hit by another $49 for a service that I won't personally use every month" | Semantic / Category | ADVISORY ONLY (unchanged)**

The injected text does not name BrowserStack. Endless stays not held either way, so no task value depends on it. Not scored.

**DR3 (new) | P2 | §3.2 | same sentence (brief: "what still has to land before it runs for bought users") | injected #468 `rc_38`, 2025-09-29T15:36:41Z: "The final vial models are missing and need to be in before the beta" and `cmt_zom465_3`, 2025-09-30T18:13:41Z: "the Collect & Win icon does have to land before the beta" vs injected UA plan slide `el_9d1c74b0a26e`: "Beta-cohort buy, starting once the stores approve the Sep 30 builds." | Semantic / Category | ADVISORY ONLY**

- Base #builds: iOS Submission #50 and Android Submission #135 started 18:43 and 18:45 UTC on Sep 30.
- Git has no later vial or icon-animation commit. The last change to the Collect & Win item prefabs is #468 itself.
- So the art said to be needed "before the beta" is not in the builds the buy waits on, and it needs a further client build.
- This is not a contradiction. No record says another build cannot land, and Collect & Win does not run until Oct 10.
- The gap is what the still-to-do column reports, and no graded value changes.
- The icon half existed in rev11. The vial half is new in rev12.

## Section 3 lines

- **Two services:** unchanged from rev11. Slack, GitHub, Docs, Slides, Sheets, GCal, Gmail, Confluence and Linear each change a graded fact. Trello is a decoy.
- **Hidden record:** none. No required record is hidden from Julia. Linear is unscoped, so the new comment is readable.
- **Derived columns:** none. No Snowflake table is read.
- **Open-instruction scope:** not an open-fix instruction.
- **Date-slip severity:** no wrong date in any new or changed record. All new timestamps sit before the clock.

## No-finding lines by topic

- **Cross-Service Coherence:** advisories only (DR1, DR2, DR3).
- **Feasibility:** no finding. No tool path or data need changed.
- **Persona access:** no finding.
- **Data exists:** no finding. Both new brief references resolve.
- **Tool use and cross-service:** no finding.

## Checked and consistent (rev12)

- `cmt_zom563_1` and `_2` are unique ids, sequence 1 and 2, and both authors resolve.
- Comment times fall between started_at 18:14:25Z and updated_at 22:04:33Z. No activity follows the close.
- Vincent's closure still follows his base "Yep it works as expected" at 21:58:44.
- The ZOM-563 UPDATE is unchanged.
- Thread counts are unchanged, and the #468 thread stays at 42.
- Known issue cards are as in rev11. None is newly touched.

## Platform defects

- Anonymized tokens in PNs Beta copy, as in rev11. Not scored.
- PLATFORM:FD-2880 and PLATFORM:FD-3785 are not triggered.

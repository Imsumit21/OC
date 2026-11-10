# PROMPT Brief Evidence — §5a Search-as-Persona Proof + §10 Entity Traps

Persona: **julia_lawson** (`julia.lawson@harmonygames.co`) · universe **synth-cut** · clock **2025-10-01 07:00Z**
Tools: `Task_Authoring/tools/persona_view.py`, `Task_Authoring/tools/entity.py`, run from the workspace root with `TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputsS`.

**Read first — base vs. overlay.** Ten of the twelve facts are rows of the proposed overlay `01_Universe_Inject.sql`; two (#5, #12) are base records. `persona_view.py search` reads **only the base export**, so it returns 0 hits for every overlay row (documented U4: *"Id not found in the base (it may be injected: use check-sql)"*). Each row therefore carries two pieces of evidence:

1. the verbatim natural **search** a PM would type against the universe, and
2. **ACL visibility** of the row from `persona_view.py check-sql --load-bearing` (which judges final state after the whole SQL), plus a **text-match check** on the row's searchable fields (the same case-folded substring rule `search` uses).

"Found?" is **YES** only where a natural query substring-matches the row's searchable text **and** check-sql says YES. Base-only misses are labelled `NO (base)` and never passed off as hits. Where a suggested query **misses**, the row says so — that is a prompt-wording finding, not a visibility failure.

---

## Section A — Search-as-persona proof (§5a)

| # | Fact | Service | Natural query | Visible hits (base) | Hidden by ACL | First visible hit | Found? |
|---|------|---------|---------------|--------------------|---------------|-------------------|--------|
| 1 | Frederick's beta calendar ask (DM) | slack | `live-ops and push calendar` (also tried `beta calendar`, `live-ops calendar`) | 0 (0 / 0) | 0 | — (overlay row; check-sql YES, IM `D05SD5QLG94` member) | **YES** via `live-ops and push calendar` / `push calendar` / `beta buy` / `calendar`. **`beta calendar` MISSES, `live-ops calendar` MISSES** |
| 2 | Robert's Halloween one-off approval | slack | `Halloween one-off` | 0 | 0 | — (overlay; check-sql YES, public `zombie-art`, member) | **YES** (exact phrase in row text) |
| 3 | Robert's later withdrawal | slack | `pulling my ok` (also `Halloween one-off`) | 0 | 0 | — (overlay; check-sql YES, IM `D05GU6L0XFH` member) | **YES** (`pulling my ok.`, `Halloween one-off`, `my later word`) |
| 4 | Vincent's weekly-leaderboard prod re-test | slack | `weekly leaderboard` | 55 | 61 in 25 | `C050WGU41HR/1736994644.856699` (engineering-bots, 2025-01-16) | **YES** for the topic; the decisive overlay row (`C0880U9751A/1759265412.481907`, #zombie-match3d, private, member) is check-sql YES and its text matches `weekly leaderboard`, `re-tested`, `prod build`, `new week` |
| 5 | Zombie-bugs iOS-build reports thread | slack | `ios build` (also `zombie lane ios`) | 135 (11 in `C08R27X0EAH`) | 132 in 34 | `C04S28HSD0U/1689652524.527049` (product); in-channel first: `C08R27X0EAH/1751049640.470399` (2025-06-27) | **YES (base)** — `can-see` YES (private `zombie-bugs`, member). **`zombie lane ios` = 0 hits**; the channel is `#zombie-bugs`, not a "zombie lane ios" thread |
| 6 | Brian's Nov Season Pass config handoff (original) | gmail | `Season Pass November config` (also `Season Pass config`) | 0 | n/a (`--no-hidden`) | — (overlay; check-sql YES in Julia's mailbox; Brian's and Frederick's copies are correctly NO) | **YES** (subject `ZM3D Season Pass November config handoff` contains the phrase) |
| 7 | Brian's slip of the handoff to Oct 31 | gmail | `Season Pass config` (also `Oct 31`) | 0 (base `Oct 31` = 4 unrelated mails) | n/a | — (overlay; check-sql YES in Julia's mailbox, label `UNREAD`) | **YES** (`Season Pass config`, `Oct 31`, `Oct 29`, `Istanbul`) |
| 8 | Douglas's Oct 8 backend-release event | gcal | `backend release` (also `release`) | 0 (base `release` = 1: `evt_5501d788ce199d4b18bfee`) | 0 | — (overlay; check-sql YES) | **YES** — Julia's own copy `evt_5c1e83a7d94b02f6c8e31a` (owner YES); Frederick's/Owen's copies and `evt_9a4c2e7f1b3d58e06c7a2f` resolve as the **same meeting** (shared `ical_uid 3f8e1c6a9b2d4e7f0a5c8b1d3e6f9a2c`), so one instance in results |
| 9 | The beta "brief" doc | gdocs | `working rules` (also `beta brief`, `live-ops rules`) | 0 | 0 | — (overlay; check-sql YES, shared by Frederick) | **YES** via `working rules` / `beta live-ops` / `calendar`. **`beta brief` MISSES and `live-ops rules` MISSES** — the doc is titled `ZM3D beta live-ops calendar - working rules` |
| 10 | UA plan deck (four buy weeks) | gslides | `UA plan` (also `buy weeks`) | 0 | 0 | — (overlay; check-sql YES, shared) | **YES** — title `ZM3D beta UA plan`; slide 2 text `The four buy weeks` |
| 11 | Julia's live-ops calendar sheet (deliverable) | gsheets | `Live-Ops Calendar` (also `ZM Live Ops`) | 0 | 0 | — (overlay; check-sql YES, owner) | **YES** via `Live-Ops Calendar` / `calendar`. **`ZM Live Ops` MISSES in gsheets** — that is the *folder* name (`d_5f2c8e1b7a94d03c6e2b58`, owned by Julia); sheet title is `ZM3D Beta Live-Ops Calendar` |
| 12 | Base beta push sheet (PNs Beta) | gsheets | `PNs` | 2 | 0 | `f_351b98dfb06f61fb8357d0` (`Push Notifications Domino Adventure.xlsx`) | **YES (base)** — but **two hits**: correct `f_a325dd4af80afc5994d5dc` = `Push Notifications Zombie Match.xlsx`; `f_351b98dfb06f61fb8357d0` = **Domino** decoy |

### Decisive search output (verbatim)

```
$ persona_view.py search julia_lawson slack "live-ops and push calendar" --limit 3
SEARCH slack 'live-ops and push calendar' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

```
$ persona_view.py search julia_lawson slack "beta calendar" --limit 10
SEARCH slack 'beta calendar' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

```
$ persona_view.py search julia_lawson slack "Halloween one-off" --limit 3
SEARCH slack 'Halloween one-off' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

```
$ persona_view.py search julia_lawson slack "pulling my ok" --limit 3
SEARCH slack 'pulling my ok' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

```
$ persona_view.py search julia_lawson slack "weekly leaderboard" --limit 2
SEARCH slack 'weekly leaderboard' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=55 (showing 2)  hidden by ACL=61 in 25 containers  UNVERIFIED=8 in 3 containers
  {"id": "C050WGU41HR/1736994644.856699", "channel": "engineering-bots", "kind": "private", "date": "2025-01-16", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "st tooltips, \"Achievements\" text. • Fix untranslated texts: Weekly leaderboard goals, \"New Character Unlocked,\" currency "}
  {"id": "C050WGU41HR/1739559820.518149", "channel": "engineering-bots", "kind": "private", "date": "2025-02-14", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "names • <@EMPLOYEE_0031_SLACK_ID> to deploy new bot algo to weekly leaderboard • <@EMPLOYEE_0031_SLACK_ID> to update event fre"}
```

```
$ persona_view.py search julia_lawson slack "ios build" --limit 2
SEARCH slack 'ios build' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=135 (showing 2)  hidden by ACL=132 in 34 containers  UNVERIFIED=16 in 3 containers
  {"id": "C04S28HSD0U/1689652524.527049", "channel": "product", "kind": "private", "date": "2023-07-18", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "The latest iOS build with the mini game "}
  {"id": "C04S28HSD0U/1689657594.155149", "channel": "product", "kind": "private", "date": "2023-07-18", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Blake gave an iOS build tonight "}
```
In-channel hits for #5 (`C08R27X0EAH`, `#zombie-bugs`): `1751049640.470399`, `1751632208.799319`, `1751686692.942099`, `1751689575.675059`, `1751734118.966759`, `1751734725.027489`, `1754004612.050359`, `1755399916.176649`, `1756926206.642299`, `1757466704.248729`, `1758917074.996069` ("Can you trigger an ios build", 2025-09-26). Nearby LiveOps context: `1758905363.341129` (Arthur Blake: *"The iOS memory seems like a guess. Will LiveOps to addressables do the trick…"*).

```
$ persona_view.py search julia_lawson gmail "Season Pass November config" --limit 3 --no-hidden
SEARCH gmail 'Season Pass November config' as julia_lawson  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned
```

```
$ persona_view.py search julia_lawson gmail "Season Pass config" --limit 3 --no-hidden
SEARCH gmail 'Season Pass config' as julia_lawson  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned
```

```
$ persona_view.py search julia_lawson gcal "backend release" --limit 3
SEARCH gcal 'backend release' as julia_lawson  scope: GCal event summary (base events carry no description/location)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
note: counted per meeting instance (ical_uid + start), visible if any copy is visible
```

```
$ persona_view.py search julia_lawson gdocs "working rules" --limit 3
SEARCH gdocs 'working rules' as julia_lawson  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

```
$ persona_view.py search julia_lawson gslides "UA plan" --limit 3
SEARCH gslides 'UA plan' as julia_lawson  scope: GSlides title + page element text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

```
$ persona_view.py search julia_lawson gsheets "Live-Ops Calendar" --limit 3
SEARCH gsheets 'Live-Ops Calendar' as julia_lawson  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

```
$ persona_view.py search julia_lawson gsheets "PNs" --limit 3
SEARCH gsheets 'PNs' as julia_lawson  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_351b98dfb06f61fb8357d0", "name": "Push Notifications Domino Adventure.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "PNs"}
  {"id": "f_a325dd4af80afc5994d5dc", "name": "Push Notifications Zombie Match.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "PNs"}
```

### ACL verdicts for the twelve targets (`check-sql --load-bearing`)

```
[YES LB] L2  slack.slack_messages insert 8b090dec…, D05SD5QLG94/1759263600.418207  - persona EMPLOYEE_0005_SLACK_ID is in members of im D05SD5QLG94
[YES LB] L12 slack.slack_messages insert 2e75e232…, C08R8CHB0QL/1758213600.552913  - persona EMPLOYEE_0005_SLACK_ID is in members of public zombie-art
[YES LB] L14 slack.slack_messages insert 58d06bd5…, D05GU6L0XFH/1759270200.638114  - persona EMPLOYEE_0005_SLACK_ID is in members of im D05GU6L0XFH
[YES LB] L16 slack.slack_messages insert fa3eee2c…, C0880U9751A/1759265412.481907  - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-match3d
[YES LB] L32 gmail.gmail_threads  insert julia.lawson@harmonygames.co/1844470925517303296 - row user_email is the persona
[YES LB] L34 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CAH4q9Zb…>, …/1844470925517303296 - row user_email is the persona
[YES LB] L63 gmail.gmail_threads  insert julia.lawson@harmonygames.co/1844835127305531392 - row user_email is the persona
[YES LB] L65 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CAH4q9Zc…>, …/1844835127305531392 - row user_email is the persona
[YES]    L80 gcal.gcal_events insert evt_9a4c2e7f1b3d58e06c7a2f - persona is an attendee and holds its own copy evt_5c1e83a7d94b02f6c8e31a
[YES LB] L82 gcal.gcal_events insert evt_5c1e83a7d94b02f6c8e31a - event is on the persona's own calendar
[YES LB] L90/L92 gdocs f_7c3e91a4d2b85f60e1a9c4 - shared with the persona
[YES LB] L111/L113 gslides f_2b9d4e7a1c63f08d5e7b21 - shared with the persona
[YES LB] L128/L130/L131/L132 gsheets f_e4a17c90b3d25f6a8c1d73 - persona owns the file
[YES LB] base gdrive f_a325dd4af80afc5994d5dc - base record: shared with the persona
verdict: PASS (0 load-bearing rows not visible)
```
(Brian's and Frederick's copies of both Season Pass mails are `[NO]` for Julia — correct; do not route her to them.)

⚠ **One routing hazard found:** 10 injected messages in `#zombie-prs` (`C093LEZGF6J`, lines L171–L189) are **UNVERIFIED (U1)** for Julia — the channel is public and she is **not** a member. Any prompt wording that sends her to `#zombie-prs` is not provably reachable; keep PR review comments in **GitHub** (unscoped) instead.

### Unscoped services (no persona search needed)

Reads are unscoped per `Evals/references/persona/acl.md` (Slack and Confluence confirmed live; unscoped services are always YES), so the cohort PRs **#470 / #370 / #438 / #454 / #471** and their review comments, the Linear comments (**ZOM-429**, `cmt_zom*`), Brian's Trello quests card comment **`68dac8204f1e9a3b7c2d5e61`**, and **`page_season_pass_spec`** are readable without an ACL check — no `persona_view` search required.

---

## Section B — Entity traps (§10)

```
$ entity.py collisions
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

LOOKALIKE_HANDLES_AND_ALIASES (15)  [extract]
  - Gmail thread files of arthur.blake@… are named 'blake@harmonygames.co_*'
  - Gmail thread files of brian.foster@… are named 'brian@harmonygames.co_*'
  - Gmail thread files of calvin.price@… are named 'calvin@harmonygames.co_*'
  - Gmail thread files of claire.morgan@… are named 'claire@harmonygames.co_*'
  - Gmail thread files of frederick.stone@… are named 'frederick@harmonygames.co_*'
  - Gmail thread files of julia.lawson@… are named 'jlawson@harmonygames.co_*'
  - Gmail thread files of leonard.hayes@… are named 'leonard@harmonygames.co_*'
  - Gmail thread files of oliver.brooks@… are named 'oliver@harmonygames.co_*'
  - Gmail thread files of owen.baker@… are named 'owen@harmonygames.co_*'
  - Gmail thread files of samuel.turner@… are named 'samuel@harmonygames.co_*'
  - Gmail thread files of simon.walker@… are named 'simon@harmonygames.co_*'
  - Gmail thread files of vincent.parker@… are named 'vincent@harmonygames.co_*'
  - Gmail thread files of felix.young@… are named 'felixyoung@harmonygames.co_*'
  - Gmail thread files of oscar.bennett@… are named 'oscar@harmonygames.co_*'
  - Slack handle 'thomas' (U05F0A0D12F) belongs to Thomas Baker <thomas.baker@…> but equals the mailbox local part of Thomas <thomas@harmonygames.co> [persona thomas]

LOOKALIKE_EMAIL_LOCAL_PARTS (1)
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>']

SEVERAL_IDS_IN_ONE_SERVICE (1)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: 2 github identities ['PERSON_0003_GITHUB_USERNAME', 'PERSON_2137_GITHUB_USERNAME'] (joins: ['exact_email', 'exact_name'])

UNRESOLVED (11)
  [ambiguous_name] github: mononym 'Claire' -> candidates ['email:claire.morgan@harmonygames.co']
  [ambiguous_name] trello: mononym 'Marcus' -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  [token_link] EMPLOYEE_0024 / EMPLOYEE_0032 / PERSON_2218 / PERSON_2360 / PERSON_3233 / PERSON_3335 / PERSON_3935 / PERSON_5275 / PERSON_5360: same token number across services but no shared exact email/name: not joined

INTEGRITY FLAGS (2)
  {'type': 'id_with_space', 'service': 'linear', 'id': 'usr_Victor Barnes'}
  {'type': 'name_mismatch_on_email_join', 'service': 'github', 'id': 'PERSON_2314_GITHUB_USERNAME', 'detail': "GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frederick Stone)"}
```

### Resolved identities (pin exactly these)

| Correct entity (exact email / id) | Lookalike(s) | How they differ | Locator |
|---|---|---|---|
| **Julia Lawson** `julia.lawson@harmonygames.co` · slack `EMPLOYEE_0005_SLACK_ID` · github `PERSON_0005_GITHUB_USERNAME` · trello `793af7ca6940bf18eb516c75` · confluence `user_EMPLOYEE_0005` | **Peter Lawson** `peter.lawson@harmonygames.co`; gmail file alias `jlawson@harmonygames.co_*` | Same surname, different person; her mailbox files are the only ones prefixed `jlawson@`; `Peter` never appears in the cohort | `entity.py resolve "Julia Lawson"` |
| **Frederick Stone** `frederick.stone@harmonygames.co` (Co-founder) · slack `EMPLOYEE_0008_SLACK_ID` · trello `4b4a68fc0fec0b254e4f9d8e` · confluence `user_EMPLOYEE_0008` | GitHub `PERSON_2314_GITHUB_USERNAME` renders display name **"Ryan"** — it *is* Frederick (joined by exact email `frederick.stone@…`) | Display name lies; the identity is the same human. Any PR/review by "Ryan" is Frederick. Contacts job says "Commercial Lead, Marketing & Business Development" vs roster "Co-founder". Gmail alias `frederick@…` | `entity.py resolve "Frederick Stone"` → `FLAG: GitHub PERSON_2314_GITHUB_USERNAME … shows name 'Ryan'` |
| **Robert** `robert@harmonygames.co` (Co-Founder & Creative Director) · slack `EMPLOYEE_0016_SLACK_ID` · github `EMPLOYEE_0016_GITHUB_USERNAME` · trello `3d06b73654d0c8940792514c` | None exact — but the identity has **no surname**; do not expand to "Robert Stone"/"Robert Lawson" | Mononym across every service; contacts job "Co-founder & Chief Product Officer" vs roster "Co-Founder & Creative Director"; he is the highest-volume Slack author (110k msgs) so name-only hits are noisy | `entity.py resolve "Robert"` |
| **Vincent Parker** `vincent.parker@harmonygames.co` (Game Systems Engineer) · slack `EMPLOYEE_0012_SLACK_ID` · github `EMPLOYEE_0012_GITHUB_USERNAME` | Build-bot credit `43593629+vincent.parker`; gmail alias `vincent@…` | Same person under a git committer form; no other Vincent | `entity.py resolve "Vincent Parker"` |
| **Arthur Blake** `arthur.blake@harmonygames.co` (Co-founder & CTO) · slack `EMPLOYEE_0025_SLACK_ID` · github `EMPLOYEE_0025_GITHUB_USERNAME` · trello `2162c1ba310341bf318f48b7` | Branch/mononym **"Blake"** (e.g. `Blake/boxCollider30`) and gmail alias `blake@…` | "Blake" is his surname, not a separate person; searching "Blake" alone also matches nothing else but reads like a first name | `entity.py resolve "Arthur Blake"` |
| **Marcus Bennett** `marcus.bennett@harmonygames.co` (Artist) · slack `EMPLOYEE_0002_SLACK_ID` · github `PERSON_0396_GITHUB_USERNAME` · trello `7a20445f698bc5871ffd17f5` | **Marcus Lee** `marcus.lee@harmonygames.co`; Trello mononym **`Marcus`** `c48a210d5c5a4b59231c6873` (unresolved); **Oscar Bennett** | Two humans share the first name "Marcus"; Trello "Marcus" is ambiguous and `entity.py` refuses to join it; "Bennett" is shared with Oscar | `entity.py resolve "Marcus Bennett"` → `UNRESOLVED (ambiguous_name)` |
| **Samuel Turner** `samuel.turner@harmonygames.co` (Game Designer) · slack `EMPLOYEE_0004_SLACK_ID` · github `EMPLOYEE_0004_GITHUB_USERNAME` · **confluence `user_STAFF_18`** | Confluence id is `user_STAFF_18`, not `user_EMPLOYEE_0004`; gmail alias `samuel@…` | The Confluence account id does not follow the `EMPLOYEE_000X` pattern — a linkability trap; job title "Game Designer" is also Martin Walsh's | `entity.py resolve "Samuel Turner"` |
| **Brian Foster** `brian.foster@harmonygames.co` (Game Engineer) · slack `EMPLOYEE_0026_SLACK_ID` · github `PERSON_0180_GITHUB_USERNAME` · trello `d1cd0fef645a6c978ae1f068` | gmail alias `brian@…`; job title "Game Engineer" shared with **Victor Barnes** | Only the alias and the shared job title are confusable; no second Brian | `entity.py resolve "Brian Foster"` |
| **Douglas** `douglas@harmonygames.co` (Software Engineer) · slack `EMPLOYEE_0031_SLACK_ID` · github `PERSON_5760_GITHUB_USERNAME` · trello `1c0688ee1d9093f5b978c1db` | None — but **no surname**, and he owns the backend-release calendar (`calendar_id=douglas@…`) | Mononym; he is the gcal organizer of `evt_9a4c2e7f1b3d58e06c7a2f` while Julia holds the copy | `entity.py resolve "Douglas"` |
| **Calvin Price** `calvin.price@harmonygames.co` (Game Engineer, Unity VFX) · slack `EMPLOYEE_0006_SLACK_ID` · **two** GitHub logins `PERSON_0003_GITHUB_USERNAME` (exact-email join) and `PERSON_2137_GITHUB_USERNAME` (exact-name join) · trello `ca5bb4c09fbf2a437f04531e` | **Nathan Price** `nathan@harmonygames.co`; job-title drift "Game Engineer (Unity VFX)" vs "Game Engineer (Unity/VFX)" | Two GitHub identities map to one human → PR/branch attribution can double-count; same surname as Nathan | `entity.py resolve "Calvin Price"` |
| **Oliver Brooks** `oliver.brooks@harmonygames.co` (Senior Game Engineer) · slack `EMPLOYEE_0003_SLACK_ID` · github `EMPLOYEE_0003_GITHUB_USERNAME` · trello `12c4a9dcd2d37a25a8d3b557` | **Lauren Brooks** `lauren@harmonygames.co` (no dot-surname form) | Same surname, different mailbox shape (`lauren@` vs `oliver.brooks@`); alias `oliver@…` | `entity.py resolve "Oliver Brooks"` |
| **Owen Baker** `owen.baker@harmonygames.co` (Game Engineer, Unity) · slack `EMPLOYEE_0021_SLACK_ID` · github `PERSON_5877_GITHUB_USERNAME` · trello `919ee44a0d5157b7839f66a8` | **Thomas Baker** `thomas.baker@harmonygames.co`; also **Thomas** `thomas@harmonygames.co` (different person, `thomas@` vs `thomas.baker@`) and Slack handle `thomas` = Thomas Baker | "Baker" is shared with Thomas; `thomas@` ≠ `thomas.baker@` is the sharpest email trap in the corpus; Owen also holds a copy of the backend-release event | `entity.py resolve "Owen Baker"` |

### Traps the prompt must avoid

1. **GitHub "Ryan" = Frederick Stone.** `PERSON_2314_GITHUB_USERNAME` is Frederick's login but its display name is `Ryan` (integrity flag `name_mismatch_on_email_join`). If the prompt needs Frederick's GitHub activity, it must say "Frederick Stone's GitHub account (display name Ryan)" or name the login, never "Ryan". Do **not** invent a separate Ryan.
2. **Duplicate first names.** "Marcus" alone is ambiguous: **Marcus Bennett** (`marcus.bennett@`) vs **Marcus Lee** (`marcus.lee@`) vs Trello mononym `Marcus` (`c48a210d5c5a4b59231c6873`, unresolved). Always write the full name + email/ID. Same class of risk: Claire (Claire Morgan vs GitHub `Claire`), Martin (Lewis vs Walsh), Thomas (`thomas@` vs `thomas.baker@`), Baker (Owen vs Thomas), Bennett (Marcus vs Oscar), Brooks (Oliver vs Lauren), Price (Calvin vs Nathan), Lawson (Julia vs Peter).
3. **Calvin Price has two GitHub identities** (`PERSON_0003` + `PERSON_2137`). Attribute PRs by login, and do not treat them as two engineers.
4. **Mononyms.** Robert, Douglas, Thomas, Lucas and the Trello `Marcus` have no surname in the data. Never expand them; pin `robert@harmonygames.co` and `douglas@harmonygames.co`.
5. **ENG-### vs ZOM-### ticket series.** Linear has five series: `ENG` (2,270 issues, max ENG-2366), `ART` (597), `ZOM` (**553**, max ZOM-566, team *Zombie Match 3D*), `DES` (247), `EPI` (20). **521 numbers exist in both ENG and ZOM**, so a bare number is ambiguous: **ZOM-429** = *"Leaderboard next session doesn't start without killing the app"* (the relevant bug) while **ENG-429** = *"Push Debug Button For Vanishing Tile"*. The prompt must always write the full key `ZOM-429` and never "ticket 429" or "ENG-429" for the leaderboard bug.
6. **Two "PNs" push sheets.** `f_a325dd4af80afc5994d5dc` = `Push Notifications Zombie Match.xlsx` (correct) vs `f_351b98dfb06f61fb8357d0` = `Push Notifications Domino Adventure.xlsx` (**wrong game**, 21 shares, `visibility=anyone`). Name the game, not just "PNs".
7. **`#zombie-prs` is not reachable for Julia** (public, non-member → UNVERIFIED, 10 injected rows). Route review evidence through GitHub, which is unscoped.
8. **Gmail copies are per-mailbox.** Julia sees `julia.lawson@…/1844470925517303296` and `…/1844835127305531392`; the Brian/Frederick copies of the same threads are NO for her. Cite her thread ids, not the sender's.
9. **Three copies of the Oct 8 release meeting** (`evt_9a4c…` Douglas, `evt_5c1e…` Julia, `evt_a72f…` Owen) share `ical_uid 3f8e1c6a9b2d4e7f0a5c8b1d3e6f9a2c`; count it as **one** event, and use Julia's copy id when citing.
10. **Naming drift in the seek path.** The "beta brief" is `ZM3D beta live-ops calendar - working rules` (query `beta brief` returns 0); "ZM Live Ops" is a **folder**, the sheet is `ZM3D Beta Live-Ops Calendar`; "zombie lane ios" returns 0, the channel is `#zombie-bugs`.

---

## Summary

1. **YES (12 of 12 are reachable)** — but only 2 (#5, #12) are hit by a search over the base export; the other 10 are overlay rows that `search` cannot return, so their proof is `check-sql` YES **plus** a text match on the row.
2. **#1** YES via `live-ops and push calendar` / `push calendar` / `beta buy`; the suggested `beta calendar` and `live-ops calendar` **both MISS** — the prompt must not promise those words.
3. **#2 / #3** YES: `Halloween one-off` and `pulling my ok` are exact phrases in the injected rows (public `#zombie-art` and the Robert DM).
4. **#4** YES, but `weekly leaderboard` has 55 base hits and 61 ACL-hidden elsewhere — the decisive row is the private `#zombie-match3d` re-test, so the prompt must say "Vincent's prod re-test", not just the topic.
5. **#5** YES (base, `#zombie-bugs`, 11 `ios build` hits in-channel); `zombie lane ios` returns 0 — describe it as the zombie-bugs iOS-build reports thread.
6. **#6 / #7** YES in Julia's mailbox only; the final truth is the **Oct 31** slip (`…/1844835127305531392`, UNREAD), the original says Oct 29.
7. **#8** YES — one meeting, three copies; Julia's is `evt_5c1e83a7d94b02f6c8e31a`; do not cite Frederick's or Owen's copy.
8. **#9** YES via `working rules` / `beta live-ops`; `beta brief` and `live-ops rules` **MISS** — rename the artifact in the prompt or accept the doc title.
9. **#10** YES (`UA plan`, `buy weeks`); **#11** YES via `Live-Ops Calendar`, but `ZM Live Ops` finds only the folder.
10. **#12** YES but ambiguous: correct `Push Notifications Zombie Match`, decoy `Push Notifications Domino Adventure`.
11. **Entity traps:** Frederick's GitHub account shows "Ryan"; Marcus is two people plus a Trello mononym; Calvin has two GitHub logins; Robert/Douglas/Thomas are mononyms; `thomas@` ≠ `thomas.baker@`; ZOM-429 ≠ ENG-429.
12. **Routing hazard:** `#zombie-prs` is UNVERIFIED for Julia (public, non-member, 10 injected rows) — route PR evidence through GitHub; and only `#zombie-prs`, not the rest of the overlay, fails visibility (load-bearing verdict PASS).

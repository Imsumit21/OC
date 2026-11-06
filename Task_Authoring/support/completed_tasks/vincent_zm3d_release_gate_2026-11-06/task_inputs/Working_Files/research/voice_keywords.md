# Voice, Realism and Keyword Grounding

Clock: Sep 2025 Slack (all `ts` values are UTC epoch seconds, rendered as UTC hours below). Message corpus for the voice stats: every non-empty Sept-2025 message by that person in the extracted `Working_Files/research/raw/slack_*_2025-09.json` dumps plus the Vincent–Brian DM (`messages/D0770ET1HV2/2025-09.json`).

## 1.C Voice and realism

### Vincent Parker (`EMPLOYEE_0012_SLACK_ID`)
**Verbatim Sep-2025 messages**
1. `C08R27X0EAH/1756755245.855729` — "We definitely need object mass and frictions"
2. `C08R27X0EAH/1757354174.407489` — "<!here> btw the builds are not triggering and fixes can't be tested on builds for now until <@EMPLOYEE_0025_SLACK_ID> fixes it."
3. `C08R27X0EAH/1758014179.489689` — "it's fixed and needs prod env deployment."

**Profile (n=301 messages; 171 of them in the Vincent–Douglas DM `D079SNE2TL4`)**
- Length: p10 9, median 37, p90 147, max 1 824 chars; the DM skews very short (3–30 chars). Band ≈ **5–150 chars, typically one short line or a bulleted list**.
- Capitalisation: mixed and careless — 148 lower-case starts vs 98 upper-case starts; sentences start lower-case inside longer messages ("it's fixed and needs prod env deployment."), typos common ("juiice", "didn2t", "hlep", "bettere", "levellar").
- Emoji: sparse, Slack-shortcode only (`:smile:`, `:warning:`), ~15 in 301 channel messages; never unicode emoji. Occasional `:smile:`/`:disappointed:` at end of a complaint.
- Punctuation: dashes rather than commas ("It was fixed in main and haven't experienced it for a while but"), missing apostrophes, `•` bullets and numbered lists for issue round-ups, `<!here>` pings for build/news announcements.
- Hours UTC: min 03:33 / median 16:57 / max 21:58 (≈ TRT office hours + late evening).
- Language: English in channels with Turkish leakage — "teşekkürler!" (`C08R27X0EAH/1758550133.078849`).

### Arthur Blake (`EMPLOYEE_0025_SLACK_ID`)
**Verbatim Sep-2025 messages**
1. `C08R27X0EAH/1758409417.505029` — "testflight 39 is the submission candidate"
2. `C08R27X0EAH/1757164702.224619` — "Submission builds being made"
3. `C08R27X0EAH/1758559087.016679` — "pear juice and orange juiice were the only ones"

**Profile (n=69)**
- Length: p10 7, median 51, p90 148, max 1 891 chars. Band ≈ **20–120 chars, short declaratives**; long only for object-idea lists.
- Capitalisation: mostly sentence-case, single capital letter at start, no trailing period on short replies ("ill make submission builds", "ok ill chk it out", "Grreat").
- Emoji: **none** in Sept 2025 (0 shortcode, 0 unicode). Dry tone; occasional `:P`-less jokes only.
- Punctuation: minimal, no full stops on one-liners, `<!here>` used to broadcast build numbers ("<!here> iOS Build 33"), links pasted raw.
- Hours UTC: min 00:56 / median 18:49 / max 23:43.
- Language: English only; typos stay English ("juiice", "Grreat").

### Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
**Verbatim Sep-2025 messages**
1. `C08R27X0EAH/1758485492.586459` — "Yup Orange juices are not selectable. Submission blocker <@EMPLOYEE_0016_SLACK_ID> <@EMPLOYEE_0025_SLACK_ID>"
2. `C0880U9751A/1757561459.538129` — "I played 50 levels on ipad and 190 levels on iphone since yesterday"
3. `C08R27X0EAH/1756923414.894889` — "There is no cheat menu on this build - this is submission candidate"

**Profile (n=281)**
- Length: p10 20, median 52, p90 142, max 2 039. Band ≈ **30–120 chars**, very often rapid-fire multi-message bursts (level-by-level QA notes).
- Capitalisation: 187 upper vs 82 lower starts; proper nouns and "Submission blocker"/"Submission candidate" capitalised mid-sentence as a label.
- Emoji: essentially **none** (1 shortcode in 281 messages); tone is blunt/serious. Uses "-" and "->" instead.
- Punctuation: curly apostrophes ("it’s", "I’m", "that’s"), sentence fragments, no emoji softening, occasional "lol" ("Legendary pack doesn't have legendary drop rates lol").
- Hours UTC: min 00:00 / median 17:28 / max 23:59.
- Language: English only; occasional Turkish word ("zzombies" typo, never Turkish sentences).

### Brian Foster (`EMPLOYEE_0026_SLACK_ID`)
**Verbatim Sep-2025 messages**
1. `C08R27X0EAH/1757501227.705059` — "If I match the shampoo bottle on the last move, the game crashes during the kill cam phase. I tested it 4 times, and the same issue happened every time. I couldn’t beat Level 10."
2. `D07GK9QQG7M/1757316986.415459` — "Hey! Is There any build to test?"
3. `C08R27X0EAH/1758311440.897499` — "When I quit the level while the Tornado booster is active, all the objects in the following levels float around the board as if they’re drifting in space. This issue doesn’t just affect the current level, it also affects the objects in the following levels." (the message continues "To fix it, I had to kill the game"; the first quote also carries `Device: Samsung S22` / `OS: Android` lines)

**Profile (n=113)**
- Length: p10 7, median 44, p90 210, max 854. Band ≈ **10–200 chars**; structured bug reports with `Device:` / `OS:` lines.
- Capitalisation: 84 upper vs 21 lower starts; starts with "Hey!" when opening a thread.
- Emoji: rare but present (`:))`, `:laughing:`, `:smile:` — 3 total), used as a friendly sign-off.
- Punctuation: full sentences with final periods in bug reports; capitalises "There" mid-sentence (a tell), curly apostrophes.
- Hours UTC: min 06:28 / median 17:34 / max 20:52.
- Language: English in channels; the DM with Vincent is Turkish (see below).

### Douglas (`EMPLOYEE_0031_SLACK_ID`)
**Verbatim Sep-2025 messages**
1. `C0880U9751A/1756937991.025709` — "yeah, hardcoded in the server configuration"
2. `D079SNE2TL4/1757350234.373819` — "Yes! I’m making the deployment right now"
3. `D079SNE2TL4/1757353992.350099` — "should be up now, can you test please?"

**Profile (n=107)**
- Length: p10 7, median 40, p90 118, max 295. Band ≈ **5–90 chars**, chatty service-reply cadence ("Done!", "ok", "one moment please").
- Capitalisation: nearly even — 44 lower vs 53 upper starts ("yeah, ..." / "Yes! ..." / "should be up now").
- Emoji: light and friendly (`:slightly_smiling_face:`, `:sunglasses:`, 4 total); uses "sir" jokingly ("Whatever you want, sir, I can change it as well"), "Hello [name]! How are you?".
- Punctuation: exclamation marks, no full stops on short confirmations, fenced code blocks when quoting server config (`daily_max_entries: 3`).
- Hours UTC: min 01:09 / median 17:30 / max 23:01.
- Language: English in channels and in the Vincent DM; Turkish only as greetings from Vincent.

### Oliver Brooks (`EMPLOYEE_0003_SLACK_ID`)
**Verbatim Sep-2025 messages**
1. `C0880U9751A/1757616958.621319` — "I'm busy with season pass atm, but let me know if I can help with the tutorial system <@EMPLOYEE_0026_SLACK_ID>"
2. `C0880U9751A/1758130380.217949` — "I think killing one cam would give us back a worthy slice of our rendering time"
3. `C0880U9751A/1758130947.236129` — "thanks!"

**Profile (n=302)**
- Length: p10 6, median 36, p90 85, max 1 437. Band ≈ **5–90 chars**, mostly one-liners and quick engineering answers.
- Capitalisation: strongly **lower-case starts** — 211 lower vs 67 upper; "yes", "all right", "thanks!", "Im gonna research".
- Emoji: practically none (1 shortcode in 302); uses "ty", "atm", "tbh", "we'd".
- Punctuation: almost no full stops, contractions everywhere ("I'm", "we'd", "its"), `"loading step"` in quotes when naming a field, occasional `&gt;` quote blocks.
- Hours UTC: min 00:03 / median 17:58 / max 23:54.
- Language: English only.

### Vincent ↔ Brian DM — Turkish (the outlier)
The `D0770ET1HV2` DM (`messages/D0770ET1HV2/2025-09.json`, 3 154 messages) is **Turkish, informal, lower-case, no punctuation discipline** for both people — completely different from their English channel voice. Examples:
- `D0770ET1HV2/1756807325.734239` Brian: "selam, müsaitliğin varsa bana özet geçebilir"
- `D0770ET1HV2/1756807407.413679` Vincent: "tabi çok bi şey olmadı zaten"
- `D0770ET1HV2/1756807463.571179` Brian: "çok bi şey olmdı sadece oyunu kill ettik.d."
- `D0770ET1HV2/1756807520.463609` Vincent: "• investor için websitesiyle uğrşamaya devam ediyorlar / • variant c'den devam yeni levellar yapılıyor / • monster animasyonları rezil bir şekilde optimize olmadığı için Marcus onu önceliklendirdi"

Other Turkish tells: ".d" and ".d.d" as laughter (Brian), "Anladım abi teşekkür", "yok canının sağlığı", "hahaha no worries" (code-switching mid-DM). Practical consequence for authoring: **Turkish belongs to the Vincent–Brian DM only**; nobody writes Turkish in the channels (only one word: "teşekkürler!" from Vincent).

### Human-written email check — Leonard Hayes and Arthur Blake
Queries run: `threads/leonard@*`, `threads/blake@*`, `threads/vincent@*` for "Vincent,", "Thanks,", "build", "Hi Blake", "Hi Leonard", "ZOM-", "submission", "Linear".

- **No Sep-2025 (or any 2025) internal colleague email from either of them was found.** Everything dated 2025 in those mailboxes is calendar invitations, Linear/GitHub/Google-Sheets notifications, or Recruitee-style intros.
- The only human-written, colleague-to-colleague emails are **2023–2024 recruiting/intro threads**, e.g.:
  1. `threads/leonard@harmonygames.co_1782761793848568560.json` `/messages/6` — subject **"Re: [PERSON_NAME_0101] <> Blake Intro"**, from `leonard.hayes@harmonygames.co`, Thu 16 Nov 2023 14:38 -0800, body "Hi Blake and [PERSON_NAME_0101], As discussed with each of you here is an intro to one another…" — Leonard writing directly to Blake.
  2. Same file `/messages/5` — from `arthur.blake@harmonygames.co`, Tue 28 Nov 2023, "Hi [PERSON_NAME_0101], I have heard good things about you. Are you available to chat next week?" — the Blake reply, so the Blake↔Leonard thread is two-sided.
  3. Same file `/messages/3` — Leonard, Thu 4 Jan 2024, "Hi [PERSON_NAME_0101], Thank you for following up with us. We have been quite busy with our alpha release…" (and `/messages/2` is Leonard switching to Turkish with the same correspondent: "Blake'la konustum, tecrubene ve lokasyonuna gore saati $10'dan bir kontratin uygun oldugu…").
- Gmail is therefore **not** a usable surface for a Sep-2025 release-gate email: it does hold real human-written mail from Leonard and Blake, but only on hiring/intro topics in 2023–2024, and generic terms ("submission", "build", "gate") hit calendar invitations and marketing footers, not internal engineering mail.

## 1.D Keywords

Corpus note: Slack scope is `messages/*/2025-09.json` (all channels, including channels without a local raw dump, e.g. `C096HFA5Z8W`). "limit hit" means the run reached `SM_LIMIT=60`.

### (a) Slack — `messages/*/2025-09.json`

| term | scope | hits | example pointers |
|---|---|---|---|
| go/no-go | slack 2025-09 | 1 | `messages/C096HFA5Z8W/2025-09.json /104/text` — "…scale tests to 2–3k users. Go/No-Go gates are explicit: ≥45%…" |
| submission candidate | slack 2025-09 | 6 | `messages/C08R27X0EAH/2025-09.json /116/text` (Leonard, "There is no cheat menu on this build - this is submission candidate"); `/247/text`; `/663/text` ("Playing submission candidate…") |
| store push | slack 2025-09 | 0 | — |
| regression | slack 2025-09 | 60 (limit hit) | `messages/C093LEZGF6J/2025-09.json /321/attachments/0/text` ("…This is a regression."); `/628/attachments/0/text` ("QA provided regression test list"); `messages/D06477JGUKT/2025-09.json /132/text` ("Full Regression Test") |
| update path | slack 2025-09 | 0 | — |
| update from | slack 2025-09 | 6 | `messages/D0770ET6WBW/2025-09.json /259/text` ("He'll need to update from main"); `messages/D06UPGF5PQV/2025-09.json /87/text`; `messages/D079SNE2TL4/2025-09.json /183/attachments/0/text` |
| release gate | slack 2025-09 | 0 | — |
| ZOM-435 | slack 2025-09 | 2 | `messages/C0880U9751A/2025-09.json /404/attachments/0/blocks/0/text/text` — "Oliver Brooks changed status to Done for …ZOM-435/user-stuck-on-trophy-path-after-clicking-claim-button-too…" ; `/404/attachments/0/fallback` |
| ZOM-473 | slack 2025-09 | 0 | — |
| ZOM-562 | slack 2025-09 | 4 | `messages/D07GJJBFHA5/2025-09.json /770/text` — "…ZOM-562/orphan-items-in-boss-arena"; `/770/attachments/0/app_unfurl_url`; `/770/attachments/0/blocks/0/text/text` ("ZOM-562 Orphan items in boss arena") |
| ZOM-559 | slack 2025-09 | 0 | — |
| ZOM-567 | slack 2025-09 | 0 | — |
| ZOM-569 | slack 2025-09 | 0 | — |
| ZOM-570 | slack 2025-09 | 0 | — |
| backend #36 | slack 2025-09 | 0 | — |
| approval | slack 2025-09 | 11 | `messages/C090N54TG79/2025-09.json /344/text` ("…approvals from app stores to fix it"); `messages/C096HFA5Z8W/2025-09.json /316/text` ("…without board’s approval"); `messages/C093LEZGF6J/2025-09.json /404/attachments/0/text` (poem, false positive) |
| Puzzles vs Zombies | slack 2025-09 | 0 | — |
| TestFlight 50 | slack 2025-09 | 0 | — |
| orange juice | slack 2025-09 | 16 | `messages/C05433XK267/2025-09.json /694/attachments/0/fallback` — "Match 3D iOS Submission - #40 - main Changes: - Fix pear and orange juic…"; `/696/attachments/0/fallback` (Android Submission #127) |

### (b) Gmail — `threads/vincent@*`

| term | scope | hits | example pointers |
|---|---|---|---|
| submission | gmail vincent | 13 | `threads/vincent@harmonygames.co_1803662070217634598.json /messages/0/subject` — "Invitation: Quick Submission Huddle @ Thu Jul 4, 2024 7pm – 7:30pm" (calendar); `/messages/0/body` |
| ZM submissions | gmail vincent | 0 | — |
| submission builds | gmail vincent | 0 | — |
| hotfix | gmail vincent | 7 | `threads/vincent@harmonygames.co_1812226084693622483.json /messages/0/subject` — "Updated invitation: Daily Standup - Hotfix Special @ Mon Oct 7, 2024 7pm - 8pm" (calendar) |
| release/1.3.24_HotFix | gmail vincent | 0 | — |
| beta drop | gmail vincent | 0 | — |
| Puzzles vs Zombies | gmail vincent | 0 | — |
| TestFlight | gmail vincent | 0 | — |
| session notes | gmail vincent | 0 | — |
| playtest | gmail vincent | 60 (limit hit) | `threads/vincent@harmonygames.co_1775868927632411315.json /messages/0/subject` — "Invitation: GoD Weekly Playtest" (recurring calendar series) |
| gate | gmail vincent | 40 | only marketing footers/URLs, e.g. `threads/vincent@harmonygames.co_1785837153307841996.json /messages/0/body` (Lucid Software unsubscribe footer) — no release-gate mail |

### (c) Linear — `data.json`

| term | scope | hits | example pointers |
|---|---|---|---|
| release ticket | linear data.json | 0 | — (Linear uses labels, not "release ticket") |
| store push | linear data.json | 0 | — |
| go/no-go | linear data.json | 0 | — (only the Slack deck in `C096HFA5Z8W/104` uses the phrase) |
| trophy path | linear data.json | 7 | `data.json /issues/3422/title` — "Lock item equipment slots as rewards on trophy path"; `/issues/3455/description` ("Automatically open the trophy path main screen"); `/issues/3422/description` (spreadsheet of trophy path info) |
| orphan | linear data.json | 8 | `data.json /issues/3639/title` — "Orphan items in boss arena" (= Slack ZOM-562); `/issues/3639/description`; `/issues/736/title` ("[Baklava] Place train levels and create a new chapter from orphan puzzles") |
| free label | linear data.json | 0 | — |

Supplementary probes (same scope, `SM_LIMIT=15`):
- `submission` → 15 (limit hit), e.g. `data.json /issues/117/labels/1` = **"Submission Blocker"** label; `/issues/117/description` "…finish for alpha submission on January 10th".
- `hotfix` → 15 (limit hit), e.g. `data.json /issues/749/labels/0` = **"Desire Hotfix"** label (750, 751 same label).
- `store` → 15 (limit hit), e.g. `/issues/139/title` "ART:MARKETING>APP STORE ICON"; `/issues/382/title` "Re-fresh Store Listing screenshots" (store = storefront listing, never "store push").
- `release gate` → 0; `orphan items` → 2 (`/issues/3639/title`, `/issues/3639/description`).

### (d) Trello — `data.json`

| term | scope | hits | example pointers |
|---|---|---|---|
| TECH ISSUES | trello data.json | 3 | `data.json /cards/802/name` — card **"Fix TECH ISSUES"** (id `68d1eb90bef538c7c5c5599d`, list `6851a674975da1fe76e70d93` = **"BETA: Oct 10"** on board `6851a6569f3bf818760632ab` = **"ZM ROADMAP"**, `dateLastActivity` 2025-09-23, empty `desc`, not closed); `/actions/5244/data/card/name`; `/actions/5245/data/card/name` |
| store push | trello data.json | 0 | — |
| trophy | trello data.json | 22 | `data.json /cards/703/name` — "[Feature] Trophy Path ([PERSON_NAME_0022])"; `/cards/703/url`; `/actions/4670/data/card/name` ("Trophy Path - [PERSON_NAME_0022] (link)") |

Context for authoring: the "Fix TECH ISSUES" card sits among the 19 live cards of **"BETA: Oct 10"** (siblings: "Minor Bugs to Fix", "Google/Apple Login", "Bot Scoring Improvements [..]/Douglas", "CPM_history (lt_avg, lt_median, last_30, last_20, last_10) Leonard by next release", "Adaptive Difficulty Learnings to tier players into different buckets"). No Trello list or card anywhere contains "store push".

### (e) Drive / Sheets / Docs — `data.json`

| term | scope | hits | example pointers |
|---|---|---|---|
| Release Gate | gdrive data.json | 0 | — |
| Update-path | gdrive data.json | 0 | — |
| update path | gdrive data.json | 0 | — |
| gate | gdrive data.json | 2 | both are a Unity package doc named `Negate-Node.md` (`/drive_files/25183/name`, `/drive_files/25183/content_path` = `…/com.unity.shadergraph@12.1.13/Documentation~/Negate-Node.md`) — plain substring, not a release gate |
| Release Gate | gsheets data.json | 0 | — |
| Update-path | gsheets data.json | 0 | — |
| update path | gsheets data.json | 0 | — |
| gate | gsheets data.json | 60 (limit hit) | all substring noise from "relegated"/"League": `/sheets_spreadsheets/19/sheets/0/grid/28/4`, `/sheets_spreadsheets/21/sheets/0/grid/28/4`, `/sheets_spreadsheets/27/sheets/0/grid/745/10` |
| Release Gate | gdocs data.json | 0 | — |
| Update-path | gdocs data.json | 0 | — |
| update path | gdocs data.json | 0 | — |
| gate | gdocs data.json | 60 (limit hit) | substring noise, e.g. `/docs_documents/5/body_text`, `/docs_documents/7/body_text` ("…bottom 5 are relegated…"), `/docs_documents/13/body_text` |

Extra probes in the same three scopes (all 0 unless stated): "Update Path" 0/0/0, "store push" 0/0/0, "Release Gate" 0/0/0, "release checklist" 0 / 0 / 1 (`gdocs /docs_documents/144/body_text` — a SteamWorks "Release Readiness" checklist, unrelated to mobile store push).

**Answer to the decisive question:** none of the four phrases **"go/no-go"** (as a *release* gate), **"store push"**, **"Release Gate"** or **"Update-path"** already exists as a base record in the non-Slack services. Base evidence only supports adjacent vocabulary:
- "Go/No-Go gates are explicit: ≥45%…" in a Slack deck (`messages/C096HFA5Z8W/2025-09.json /104/text`);
- "submission candidate" (Leonard, 6 Slack hits), "Submission blocker" (Leonard, repeatedly), Linear label "Submission Blocker";
- "update from main" (branch hygiene, 6 Slack hits) — the closest base phrase to "update path";
- Trello container "Fix TECH ISSUES" (BETA: Oct 10) — a usable ask container;
- Linear "Orphan items in boss arena" (ZOM-562) and "trophy path" issues.
So "store push", "Release Gate" and "Update-path" are greenfield: any use must be introduced by the injection SQL (and mirrored in the prompt's own wording), while "go/no-go" and "submission candidate" already have base footing that can be cited.

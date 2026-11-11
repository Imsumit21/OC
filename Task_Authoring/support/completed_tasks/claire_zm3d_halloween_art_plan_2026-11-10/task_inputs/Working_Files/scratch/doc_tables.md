# Doc tables — ZM3D Halloween art plan (Claire Morgan, synth-cut clock 2025-10-01T07:00Z)

Scratch evidence tables for `01_Scenario_Design.md`. Hazard ids are validated against
`Task_Authoring/references/universe_kb/by_universe/synthcut/coherence_hazards.json`; activity against
`activity.json`; companions against `integrations.json`; storyline against `timeline.json`, `cohorts.json`,
`trap_catalog.json`; data defects against `Task_Authoring/references/known_data_issues/synthcut.md`.
Seed bound 2025-10-01T00:00:00Z.

## 1a Coherence audit

Every base record the storyline relies on, plus every planned seed, walked over the seven QC categories.
Hazard ids below come from coherence_hazards.json; a dash means the category was walked and the record is
clean for it. Dispositions: `kept` (safe to grade), `excluded` (never graded, never deciding),
`folded` (record kept but its defect absorbed into another fact), `dated_claim` (grade only the dated claim,
never the derived state).

| Record | QC category | Fields | Evidence pointer | Hazard id | Disposition |
| --- | --- | --- | --- | --- | --- |
| Leonard's same-variables rule (Jun 6 statics thread) | temporal | message ordering inside `C06DJBJL798` | `C06DJBJL798/1749234411.792129` | T02 | kept — quoted text, no counter fields read |
| Julia's statics / CTA thread (Jun 6) | quantitative | `reply_count`, `latest_reply` on the thread root | `C06DJBJL798/1749223809.524999` | Q01, Q02, Q03 | folded — grade the CTA wording only, never the reply tally |
| Frederick 30 s UA cut (baked-in music) | semantic | attachment wording "music is baked in" vs SFX-only rule | `C06DJBJL798/1755114007.441789` | — | kept |
| Leonard "record all in-game videos with SFX but without music baked in" | referential | reply to the 30 s cut parent | `C06DJBJL798/1755116786.755519` | — | kept — parent ts verified in the export |
| Leonard export iphone/ipad/gp (Sep 3) | semantic | asks for three export sizes; no art state implied | `C06DJBJL798/1756914854.743319` | — | kept |
| Marcus portrait UA end card + optional sfx | temporal | single message, no thread counters | `C06DJBJL798/1753968186.965269` | — | kept |
| cheer_fastcouch ad variant (Jul 28) | identifier | `cheer_fastcouch_9-16_blur-VEED.mp4` file title in a thread root | `C06DJBJL798/1753724236.173759` | I15 | folded — cite the file title as written, never a Drive twin |
| Martin Halloween icon concept (Sep 17) | semantic | post tags three people, names a theme not an asset | `C08R8CHB0QL/1758121809.236839` | — | kept — the "concept exists, ticket does not" gap is the ask |
| Robert: "the Halloween pack" (tombstones, mausoleum) | referential | props named in a next-steps list | `C0880U9751A/1738109783.735889` | — | kept |
| Robert iOS 1232 zombie swap (Jul 30) | temporal | build note, no art decision | `C0880U9751A/1753820524.488479` | — | kept |
| Arthur Sep 19 Halloween prop list | semantic | seasonal item vocabulary (Pumpkin Lantern, Witch Hat, Candy Bucket, Skull, Cauldron) | `C0880U9751A/1758300550.745699` | — | kept — decoy for the icon, real for props |
| ART-774 ZM3D Marketing Screenshots (Done) | state/lifecycle | `state_id=Done`, `completed_at=2025-04-15` | `linear ART-774` | L05 | dated_claim — grade the Apr 15 store-spec delivery only |
| ART-790 Updated ZM Marketing Screenshots | state/lifecycle | state `Todo` while the screens shipped | `linear ART-790` | L03, L05 | excluded — SC-16 state lag, kept off the path |
| ART-792 ZM3D Marketing Screenshots round 3 | state/lifecycle | state `Team Epic`, never completed | `linear ART-792` | L03 | excluded — SC-16 state lag, kept off the path |
| Base Linear ART assignee `usr_51f5f16d46e8cf55` | identifier | assignee token, not `usr_<16hex>` shape in one case | `linear ART-774` | I10 | folded — read the assignee by person, never by token shape |
| Frederick's thread mails (Sep 30 plan, Sep 12 draft) — planned seed | quantitative | one message copied into two mailboxes | planned gmail thread, mailbox claire.morgan@harmonygames.co (U4) | Q10 | folded — only Claire's copy decides |
| Vendor quote mail to Claire (Sep 24) — planned seed | identifier | sender address maps to a Contacts row, not to a Slack id | planned gmail thread, mailbox claire.morgan@harmonygames.co (U4) | I03 | folded — resolve the sender through the Contacts record |
| POD notes mail (Sep 29, Martin cemetery/cave endless-mode) | identifier | mailbox alias in the thread file name vs `user_email` | `claire.morgan@harmonygames.co/1844625524254242367` | I03 | kept — distractor; alias `claire@harmonygames.co_1844625524254242367` is the file name |
| POD notes body | semantic | "cemetery, cave, or ice cave" is endless-mode, not Halloween | `claire.morgan@harmonygames.co/1844625524254242367` | — | excluded — distractor, never a Halloween authority |
| ZM3D Halloween review (Thu Oct 2 16:00Z) — planned seed | temporal | 7 calendar rows for one meeting | planned gcal event on Claire's calendar (U4) | I11, I12, I13 | folded — cite one start time; ignore the duplicate rows |
| ZM3D Halloween review invite mails — planned seed | referential | invite/update mails vs the GCal instance | planned gmail thread, mailbox claire.morgan@harmonygames.co (U4) | R08 | folded — calendar row is the authority, mails are companions |
| Review event attendee copies | quantitative | same `ical_uid`+start, differing copy fields | planned gcal event on Claire's calendar (U4) | Q11 | folded — grade the start time only |
| 'ZM3D live creatives' (Frederick sheet) — planned seed | identifier | sheet title without `.xlsx`, Drive name with it | planned gsheets 'ZM3D live creatives' (U4) | I15 | folded — cite the sheet title, never the Drive file name |
| 'ZM3D live creatives' — planned seed | semantic | columns per creative, not per campaign | planned gsheets 'ZM3D live creatives' (U4) | — | kept — this is the deciding authority |
| 'ZM3D release calendar — Q4' (Arthur doc) — planned seed | referential | Slack/Docs reference to the doc | planned gdocs 'ZM3D release calendar — Q4' (U4) | R04 | folded — resolve the doc by title in Docs, never by the Slack link |
| 'Seasonal art direction — Q4 2025' (Robert deck) — planned seed | semantic | direction names treatments, not creatives | planned gslides 'Seasonal art direction — Q4 2025' (U4) | — | kept — direction only, never a per-creative call |
| Trello 'Halloween push' card + Frederick comment — planned seed | temporal | card `dateLastActivity` vs the comment date | planned trello card on board `6851a6569f3bf818760632ab` (U4) | T06 | folded — grade the comment text, not the card clock |
| Vendor Contacts row (KayKit) — planned seed | identifier | 24-hex contact id, no email alias | planned contacts vendor row (U4) | I14 | folded — owner tokens (`Resource: …`) are not emails |
| GitHub KayKit Halloween Bits prefabs + ProjectSettings.asset — planned seed | semantic | asset path vs app id | planned github match3d path (U4) | — | kept — grounding only, never graded |
| Google Sheet 'Video Capture Requests for UA' | identifier | owner `Resource: -6481757892984311338`, `.xlsx` Drive name | `gsheets f_b5fb884dc96261846b6c2c` | I14, I15 | excluded — 2024 capture list, decoy; owner is not a person |
| Confluence release checklist | state/lifecycle | page versions/edit messages | `page_release_checklist` | — | excluded — decoy; version history is not a release state |
| #god-gameart 2024-09 DD Halloween icon asks | temporal | 2024 asks read at the 2025 clock | `C04V7N09LE7/1726011239.339499` | T02 | excluded — prior-year decoy for the ZM3D icon |
| Snowflake AD_SPEND_DAILY (Unity-only since Aug 11) | quantitative | spend zero for Unity rows | `snowflake.ANALYTICS.MARKETING.AD_SPEND_DAILY` | — | excluded — SC-11/SC-12 spend, never a surface |
| Linear label vocabulary across teams | semantic | 243 labels mixing sprints, releases, platforms | `linear ART-774` | S03 | excluded — the task never reads a label |
| GitHub display name for Frederick ('Ryan') | semantic | profile display name vs person | `github match3d` author of the seed commit | S04 | excluded — identity read from Linear/Slack, never the GitHub display name |
| PR comment mirrors (GitHub → Slack) | referential | mirrored comments inside a repo window | `github match3d` | R07 | excluded — no PR is seeded, so no mirror is expected |
| Invite mails with no GCal instance | referential | dated invitation mails | planned gmail thread, mailbox claire.morgan@harmonygames.co (U4) | R08 | folded — the review event is seeded in GCal as its companion |
| Quiet / departed assignees on open tickets | state/lifecycle | open issues owned by quiet people at the clock | `linear ART-792` | L08 | excluded — never grade who owns an open ticket |
| Claire's mailbox alias `claire@harmonygames.co` | identifier | thread file name alias vs `user_email` | `claire.morgan@harmonygames.co/1844625524254242367` | I03 | kept — resolve every Claire mail through the alias |
| Same-name people (Marcus Bennett vs Marcus Lee; Robert) | identifier | first-name-only addresses | `marcus.bennett@harmonygames.co` | I10 | excluded — address the person by full address only |
| App-name lineage (GoD → DD → ZM3D) | other | surfaces labelled "Zombie Match", "ZM3D", "Puzzle vs Zombies" | `C0880U9751A/1738109783.735889` | K02 | folded — every surface is keyed by id, never by app name |

**Nothing in scope for:** referential R01 (no Slack message cites a Linear key in this path — excluded);
quantitative Q04 (no raw-shaped thread parents on the path — folded). Temporal, semantic, referential,
quantitative, state/lifecycle and identifier/format all carry at least one live hazard id above, so
no category is empty. (Categories with no in-scope hazard: none.)

**Known-data-issue cards touched** (from `Task_Authoring/references/known_data_issues/synthcut.md`):

| Card | What it would corrupt | Disposition |
| --- | --- | --- |
| SC-11 Unity spend $0 | any UA spend read for the Halloween push | excluded — no spend is graded; `snowflake.ANALYTICS.MARKETING.AD_SPEND_DAILY` only proves Unity-only delivery |
| SC-12 Meta spend missing for ZM3D | total ZM3D paid spend | excluded — same, spend never graded |
| SC-13 Trello "BETA: Oct 10" list name | the ZM3D beta date | excluded — due dates come from the sheet and the calendar, never the list name (`6851a6569f3bf818760632ab`) |
| SC-16 tickets open after work shipped | ART state as delivery proof | folded — ART-790 and ART-792 stay off the path; only ART ticket *comments* are graded (`linear ART-790`, `linear ART-792`) |
| SC-23 AppLovin spend dates/geos | regional UA claims | excluded — no geo or spend claim is seeded |
| SC-27 #god-bugs / #god-gameart archive state | posting rights in god-* channels | excluded — every deciding post is in `C06DJBJL798`, `C08R8CHB0QL` or `C0880U9751A` |
| SC-36 Victor Barnes on invites/channels | invite and membership lists | excluded — no roster or invite list is graded (`C04V7N09LE7` membership unused) |
| SC-58 ZM3D monster roster / boss rules | creature naming | excluded — the icon is a theme, not a roster item (`C0880U9751A/1758300550.745699` props only) |
| SC-70 Slack timezones all Los Angeles | any timezone read from Slack | excluded — cutoff times come from the calendar row (`planned gcal event on Claire's calendar (U4)`) |
| K02 app-name lineage (trap_catalog) | which app a surface belongs to | folded — surfaces keyed by id, never by the label "Zombie Match" (`C08R8CHB0QL/1758121809.236839`) |

**Sibling-defect sweep.** Other ART tickets in the same family lag their delivery the same way, and each is
kept off the path: `linear ART-790` ("Updated ZM Marketing Screenshots") is still `Todo` although round-2 screens
shipped; `linear ART-792` ("ZM3D - Marketing Screenshots round 3") sits in `Team Epic` and never completed;
`linear ART-774` carries a clean Apr 15 completion and is safe only for the dated store-spec claim; the June 6
statics thread `C06DJBJL798/1749223809.524999` has counter drift that would mis-state how many replies the CTA
decision got; and the Sep 19 prop list `C0880U9751A/1758300550.745699` is a reply whose parent
`C0880U9751A/1758300545.482979` carries no art decision. No sibling ticket is on the deciding path, so the
state-vs-delivery defect never reaches a grade.

## 1b Active speakers

Every seeded speaker is read against `activity.json` (status_at_clock plus per-service last activity); all eight
people are `active_sep_2025_quiet_in_oct`, so nobody is a leaver and no seeded record needs a departure
justification. Each row states the person's activity per service so a seed can never land outside the window
that service proves — the constraints are Martin and Marcus (no 2025 sent mail), Julia (same), and Martin and
Claire (no 2025 Drive activity).

| Person | Email | status_at_clock | Per-service last activity (activity.json) | Seeding role |
| --- | --- | --- | --- | --- |
| Claire Morgan | claire.morgan@harmonygames.co | active_sep_2025_quiet_in_oct | slack 2025-09-30, gmail_sent 2025-09-30, linear 2025-09-03, github 2025-09-25, drive 2024-07-05 | persona; receives the ask in `C06DJBJL798`, owns the plan doc and tracker sheet, comments on ART tickets, replies in the thread |
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | slack 2025-10-01, gmail_sent 2025-09-30, linear 2025-09-17, confluence 2025-09-29, drive 2025-09-30 | asks Claire in `C06DJBJL798/1749234411.792129` (same-variables rule) and owns the reply thread |
| Frederick Stone | frederick.stone@harmonygames.co | active_sep_2025_quiet_in_oct | slack 2025-09-30, gmail_sent 2025-09-09, linear 2025-08-26, drive 2025-09-24, confluence 2025-09-01 | authority 1: sheet 'ZM3D live creatives' plus the Sep 30 plan mail (planned seed); created ART-793+ |
| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | slack 2025-10-01, gmail_sent 2025-09-23, linear 2025-09-17, confluence 2025-09-30, drive 2025-09-25 | authority 2: Slides 'Seasonal art direction — Q4 2025' (planned seed); base Halloween-pack post `C0880U9751A/1738109783.735889` |
| Martin Walsh | martin.walsh@harmonygames.co | active_sep_2025_quiet_in_oct | slack 2025-09-30, gmail_sent 2024-07-10, linear 2025-08-26, drive 2024-02-16 | exporter of the Halloween store screens (planned seed in `C08R8CHB0QL`); receives mail only — no 2025 sent mail, no 2025 Drive write, so he owns no seeded Drive file |
| Marcus Bennett | marcus.bennett@harmonygames.co | active_sep_2025_quiet_in_oct | slack 2025-09-30, gmail_sent 2024-10-21, linear 2025-09-25, drive 2025-09-10, github 2025-09-30 | DM reply in `D05V2N6PZNU` that cheer_fastcouch Halloween cuts already exist; receives mail only — no 2025 sent mail |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | slack 2025-10-01, gmail_sent 2025-09-30, linear 2025-09-15, drive 2025-09-19, confluence 2025-09-12 | authority 3: Doc 'ZM3D release calendar — Q4' (planned seed) |
| Julia Lawson | julia.lawson@harmonygames.co | active_sep_2025_quiet_in_oct | slack 2025-09-30, gmail_sent 2024-04-17, linear 2025-08-27, drive 2025-09-11 | base statics/CTA precedent `C06DJBJL798/1749223809.524999`; receives mail only — no 2025 sent mail, so she sends no seeded mail |

### Reach table (load-bearing records)

Base rows were checked with `python3 Task_Authoring/tools/persona_view.py can-see claire_morgan SERVICE RECORD-ID`;
the pasted verdict is the re-runnable result. Rows marked `UNVERIFIED (U4 planned seed, not in base)` are the
seeds this design adds — they do not exist in the export yet and are proven at the injection gate.

| Record | Service | Visibility path | persona_view result | Role |
| --- | --- | --- | --- | --- |
| `C06DJBJL798` zombie_marketing | slack | private channel, Claire in 17 members (EMPLOYEE_0009_SLACK_ID) | YES | container for the ask and the reply |
| `C06DJBJL798/1749234411.792129` | slack | message inherits private channel membership | YES | same-variables rule (base) |
| `C06DJBJL798/1749223809.524999` | slack | message inherits private channel membership | YES | Julia statics/CTA precedent (base) |
| `C06DJBJL798/1755114007.441789` | slack | message inherits private channel membership | YES | 30 s cut, music baked in (base) |
| `C06DJBJL798/1755116786.755519` | slack | thread reply inherits channel membership | YES | SFX-without-music lesson (base) |
| `C06DJBJL798/1756914854.743319` | slack | message inherits private channel membership | YES | iphone/ipad/gp export ask (base) |
| `C06DJBJL798/1753968186.965269` | slack | message inherits private channel membership | YES | portrait end card (base) |
| `C06DJBJL798/1753724236.173759` | slack | thread root inherits channel membership | YES | cheer_fastcouch variant (base) |
| `C08R8CHB0QL` zombie-art | slack | public channel, Claire is a member of 23 | YES | container for the icon concept and the store-screen export |
| `C08R8CHB0QL/1758121809.236839` | slack | message inherits public channel membership | YES | Martin Halloween icon concept (base) |
| `C0880U9751A` zombie-match3d | slack | private channel, Claire in 25 members | YES | container for the Halloween-pack posts |
| `C0880U9751A/1738109783.735889` | slack | message inherits private channel membership | YES | Robert: the Halloween pack (base) |
| `C0880U9751A/1753820524.488479` | slack | thread root inherits channel membership | YES | iOS 1232 zombie swap (base) |
| `C0880U9751A/1758300550.745699` | slack | thread reply inherits channel membership | YES | Arthur Sep 19 prop list (base) |
| `C04V7N09LE7` god-gameart | slack | private channel, Claire in 30 members | YES | prior-year DD Halloween decoy (base) |
| `C04V7N09LE7/1726011239.339499` | slack | message inherits private channel membership | YES | 2024 DD Halloween icon ask (base, decoy) |
| `D05V2N6PZNU` Claire–Marcus DM | slack | im with 5 members incl. Claire | YES | container for the cheer_fastcouch reply |
| `linear ART-774` | linear | linear is unscoped for every persona | YES | store-spec delivery dated Apr 15 (base) |
| `gsheets f_b5fb884dc96261846b6c2c` | gsheets | shared with the persona (20 sharees, domain visibility) | YES | 2024 capture list, decoy (base) |
| `claire.morgan@harmonygames.co/1844625524254242367` | gmail | thread is in Claire's own mailbox | YES | POD notes distractor (base) |
| Leonard's Sep 30 ask, `C06DJBJL798` | slack | planned seed: post by EMPLOYEE_0038_SLACK_ID in a channel Claire is in | UNVERIFIED (U4 planned seed, not in base) | the task ask |
| Martin's store-screen export, `C08R8CHB0QL` | slack | planned seed: post by EMPLOYEE_0033_SLACK_ID in a public channel Claire is in | UNVERIFIED (U4 planned seed, not in base) | exported Halloween store screens |
| Robert's deck pointer, `C08R8CHB0QL` | slack | planned seed: post by EMPLOYEE_0016_SLACK_ID in the same public channel | UNVERIFIED (U4 planned seed, not in base) | points at the Slides authority |
| Marcus DM root and reply, `D05V2N6PZNU` | slack | planned seed: im both people are in | UNVERIFIED (U4 planned seed, not in base) | Halloween cuts of cheer_fastcouch already exist |
| 'ZM3D live creatives' | gsheets | planned seed: owned by Frederick, shared to Claire | UNVERIFIED (U4 planned seed, not in base) | authority 1, per-creative state |
| 'ZM3D release calendar — Q4' | gdocs | planned seed: owned by Arthur, shared to Claire | UNVERIFIED (U4 planned seed, not in base) | authority 3, cutoff dates |
| 'Seasonal art direction — Q4 2025' | gslides | planned seed: owned by Robert, shared to Claire | UNVERIFIED (U4 planned seed, not in base) | authority 2, direction per treatment |
| Frederick Sep 12 draft and Sep 30 plan mail | gmail | planned seed: thread in Claire's mailbox claire.morgan@harmonygames.co | UNVERIFIED (U4 planned seed, not in base) | plan changes, supersedes the draft |
| Vendor quote mail (Sep 24) | gmail | planned seed: thread in Claire's mailbox claire.morgan@harmonygames.co | UNVERIFIED (U4 planned seed, not in base) | props bundle cost, sender maps to Contacts |
| ZM3D Halloween review, Thu Oct 2 16:00Z | gcal | planned seed: event on Claire's calendar, 7 rows | UNVERIFIED (U4 planned seed, not in base) | cutoff checkpoint |
| 'ZM3D Halloween 2025' folder and its Store / UA masters subfolders | gdrive | planned seed: folder shared to Claire | UNVERIFIED (U4 planned seed, not in base) | where exported masters live |
| ART-793 and later 'UA creative library' tickets and their comments | linear | planned seed: linear is unscoped | UNVERIFIED (U4 planned seed, not in base) | per-creative Linear surface |
| New icon and iPad-set tickets | linear | planned seed: linear is unscoped | UNVERIFIED (U4 planned seed, not in base) | the two deliverables Claire files |
| 'Halloween push' card and Frederick's comment, board `6851a6569f3bf818760632ab` | trello | planned seed: board visible to Claire's workspace | UNVERIFIED (U4 planned seed, not in base) | rule that every Halloween call goes on its ART ticket |
| Vendor Contacts row for the props bundle sender | contacts | planned seed: contact in Claire's workspace | UNVERIFIED (U4 planned seed, not in base) | identifies KayKit as the sender |
| match3d KayKit Halloween Bits prefabs path and `ProjectSettings.asset` | github | planned seed: repo files readable to the workspace | UNVERIFIED (U4 planned seed, not in base) | grounding that the prefabs exist |

### Integrations and companions

Companions required per `integrations.json`. A service whose records arrive with no automated companion says
so and gives the reason; nothing here creates a bot post the design cannot account for.

| Service | INT id | Companion | Decision |
| --- | --- | --- | --- |
| slack | INT-04 | Linear Slack app personal DM digests and team-channel posts | none needed — no Linear DM or team-channel post is seeded; Claire reads the thread, not notifications |
| slack | INT-13 | Google Drive Slack app DMs (comments, access requests, shares) | none needed — the seeded Drive folder is shared silently, no share DM |
| slack | INT-22 | Slack e-mail notification mails (svc_0240) | optional — omit, because it would add mail nobody needs to read |
| gmail | INT-11 | Calendar invitation / update / RSVP mails | optional — the review event needs no invite mail; recorded as an integration exception (`no_notify`) |
| gcal | INT-11 | Calendar-to-mail invitation companion | satisfied — the event row is the authority, the invite mail is omitted under the same exception |
| gdrive | INT-13 | Drive-to-Slack share/comment DMs | optional — folder seeded without a share DM |
| gdocs | none | no Drive-family integration exists for Docs | none — Doc read directly; no bot copy anywhere |
| gsheets | none | no Drive-family integration exists for Sheets | none — Sheet read directly; no bot copy anywhere |
| gslides | none | no Drive-family integration exists for Slides | none — deck read directly; no bot copy anywhere |
| linear | INT-05 | Linear e-mail notification digests and 'auto-closed' notices | none needed — no Linear mail is seeded; comments are read in Linear |
| linear | INT-03 | linear[bot] comment on PRs naming a Linear key | none — no PR is seeded, so no bot comment is expected |
| trello | INT-21 | Trello-to-Slack: no integration exists | none — the card and comments stay inside Trello |
| contacts | none | no integration exists for Contacts | none — the vendor row is read directly to identify the sender |
| github | none | no GitHub record is seeded | none — the prefab path is grounding only, no commit, PR or issue |
| confluence | none | no Confluence integration exists | none — the release checklist is a decoy, read only |
| snowflake | none | no warehouse integration is injectable | none — AD_SPEND_DAILY is read-only grounding for Unity-only delivery |

### Storyline citations (timeline, cohorts, trap_catalog)

The story sits inside the verified `timeline` spine rather than inventing its own beats: the 2025-09-30 beat
"PR #476 'Vision bot' opened and merged" (`github:harmonygames-Games/match3d#476`) fixes the clock's last
shipping day, and the 2025-09-25 beat "Vision bot tooling matures" (`slack:C05433XK267:1758744281.336569`)
plus the 2025-09-17 beat "Post-launch live-tuning: bugs, analytics, and economy adjustments"
(`linear:ZOM-552`) show the team is in live-tuning, not a new content launch, which is exactly why the Halloween
art call has to be made from existing creatives. cohorts.json: no fit — the cohort is the seeded live creatives
sheet; nearest SL-T32 (zombie_marketing threads) and LIN-S01 (ART Done) do not define serving creatives.
From `trap_catalog.json` the design uses four mechanisms, one line each: K02 (app-name lineage
GoD to Domino Delights to ZM3D) — surfaces are keyed by id so the label "Zombie Match" never decides;
P01 (shared first names) — Marcus Bennett in the DM is not Marcus Lee, so the reply is read by address
`marcus.bennett@harmonygames.co`; P02 (shared surnames) — no Blake or Stone is interchangeable, so the
release-calendar doc is Arthur's and the live-creatives sheet is Frederick's; C02 (a parent states a
resolution another person contradicts) — Frederick's Sep 30 plan mail supersedes his Sep 12 draft, and the
newer message wins; D06 (Confluence pages with readable version history) — the release checklist is a decoy
whose old bodies tempt an out-of-date cutoff.

## Could not verify

- GCal `evt_` id for the Oct 2 review, the Drive `f_` ids for 'ZM3D Halloween 2025' and its two subfolders, the
  Trello card id on board `6851a6569f3bf818760632ab`, and the exact GitHub prefab path — all are planned seeds
  with no base record to cite.
- Whether the three seeded authorities exist under other titles: a title scan of the export found no
  'ZM3D live creatives' sheet, no 'ZM3D release calendar — Q4' doc and no 'Seasonal art direction' deck, so all
  three are treated as planned seeds.
- KayKit: `contacts.json` holds no KayKit row (only one contract-vendor row, "scott",
  `employee_0024@harmonygames.co`), so the vendor identity is a planned Contacts seed.
- `persona_view.py can-see claire_morgan gmail claire.morgan@harmonygames.co_1844625524254242367` returns
  UNVERIFIED; the resolvable forms are the alias file name `claire@harmonygames.co_1844625524254242367` and the
  thread id `claire.morgan@harmonygames.co/1844625524254242367`, which is YES.
- Confluence `page_release_checklist` and Snowflake `ANALYTICS.MARKETING.AD_SPEND_DAILY` were named from the
  brief, not re-read here; the decoy roles are design decisions, not verified content.
- Linear ART-793 and later do not exist in the export (highest base ART is `linear ART-792`), so every
  per-creative comment surface is a planned seed.
- `entity.py` collision output for Marcus Bennett vs Marcus Lee and for `robert@harmonygames.co` still needs to
  be pasted in the identity-trap section; the ids cited here are the ones I confirmed locally.

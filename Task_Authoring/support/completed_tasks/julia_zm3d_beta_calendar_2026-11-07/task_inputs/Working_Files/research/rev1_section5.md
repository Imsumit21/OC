### 5.1 Rules every decision needs, homed in incorporated records

| Decision | Rule (meaning, not wording) | Home (planned; base where possible) | Census / proof needed |
|---|---|---|---|
| Span and time base | the calendar covers Mon Oct 6 00:00 UTC – Sun Nov 2 23:59 UTC (the four buy weeks); windows are stated in server time (UTC), each as start–end instants; PT renderings of the same instant are accepted, a different instant is not | UA plan deck (span) + Frederick's brief (server time) | every graded date is one instant with both renderings precomputed (PDT until Nov 2) |
| Scope | every ZM3D beat players can see in the span: a window, a reset or a start push — not only the events page's rows; **Boss Arena is off this calendar until the pivot call** (a dated decision, not a prod-date claim, so SC-68 is untouched) | Frederick's brief (a second record the anchor points to by role, so the scope rule is off the anchor) | census of every live-ops feature in the beta build (S1b §6) and all 14 "PNs Beta" rows; no completeness claim without it (learnings §23) |
| Window cadence | Collect & Win Mon-Tue / Wed-Thu / Fri-Sun; Plague Race rolling 5-day windows from 00:00 UTC; Endless daily 00:00 UTC + weekly Monday; Season Pass monthly 1st 00:00 UTC with config locked 24 h before | base `page_liveops_calendar`, `page_season_pass_spec`, Endless spec `f_9956263905ddb43d1500ff`; Plague Race cadence from a **seeded dated statement** (Douglas, `#zombie-ops`), because the only base evidence is Snowflake, which stays off the path (§5.5) | each graded window computed from its rule; Plague Race windows: Oct 2–6, 7–11, 12–16, 17–21, 22–26, 27–31, Nov 1–5 (continuing the base 5-day series through EVT-0514, Sep 22–26) |
| "Starts" | a beat starts with the first window that opens after (a) the beta build is live and (b) its server windows are live on prod | base page "Windows are cron expressions in the CDK stack and do need a deploy to change" + Leonard's planned release mail + the backend deploy note | no base record dates a Collect & Win prod deploy (S1b §2 "Negative pins"), so the seeded note conflicts with nothing |
| Held for tech | hold an event whose core loop (enter, score, claim, get its reset) is broken on prod by an open issue, **even after a restart**; cosmetic, VFX and analytics gaps do not hold it; a fault that clears on restart is a known issue, not a hold | Leonard `C090N54TG79/1758517286.431379` ("Beta must be tech stable, no excuses") + Frederick's brief | applied to every cohort issue: ZOM-534 (quest points reset only after an app restart) → known issue, quests run; ZOM-429 → decided by Vincent's re-test (C8); ZOM-556 (daily gift skip) → claim works, reset wrong → known issue; each open issue gets exactly one answer under this sentence (learnings §21) |
| One-offs | may overlap recurring slots; displacing one needs documented Product approval; the approver's latest dated call stands | base page ("Overlapping events are normal…", "should never displace a recurring slot without documented Product approval") + seeded approval and withdrawal | Robert is the Product owner on record (`page_zm3d_gdd`, `page_season_pass_spec` "Owner: Robert (Product)"); census of Robert's records Sep 17 – Sep 30 for any other approval |
| Rewards / setup | reward settings in force are the latest dated change; no setup task for work already done | base thread `C090N54TG79/1757478958.104989` + a seeded completion note in `#zombie-ops` (matches the hidden base "plague stage rewards are fixed" and the 60/120/250 ladder) | every live-ops reward change asked in Sep (Plague Race halved; Endless coins halved, `C090N54TG79` Sep 13) checked for a later record; the Endless one is settled by a record too, or kept ungraded |
| Pushes | a push goes out only if its "PNs Beta" row is Ready **and** its copy names the current game and the right event; a row that fails is **held** until the sheet's copy owner fixes it; the calendar names the change and the owner (Julia may propose wording, but the row stays held) | base rename (`page_season_pass_spec`: "renamed 24 July 2025") + Frederick's brief (copy rule and the copy owner) | all 14 rows read; only the 1-day lapse and D0-1 FTUE rows name the old title; the 7-day lapse row does not and is sendable |
| Destinations | calendar in the Julia-owned sheet; linked from ZOM-78; recommendation as a reply in the ask's DM | prompt (named) + the ask | ZOM-78 is the only calendar ticket (title search) |

### 5.2 Two-reading tests to run at S8

1. Merged vs live on prod (Collect & Win) → the page's deploy rule + the dated deploy note decide; the first window is one
   instant (Fri Oct 10 00:00 UTC if the deploy lands Wed Oct 8, to be fixed by the seeded note).
2. Robert's thread approval vs his later DM → the later call by the same Product owner on the same item stands; no other
   Product approval exists in the census.
3. Ready vs stale copy → the copy rule decides; held, with the change named. "Send with corrected copy" is a different
   action and is not accepted, because the brief says rows go out as the sheet holds them.
4. Events page rows vs the brief's scope → the brief governs scope; the page governs rules. Any row layout accepted.
5. Reward cut pending vs done → the dated completion note decides.
6. Restart-clears faults (ZOM-534) → the held-for-tech sentence names them known issues; no second reading survives.
7. Boss Arena → off this calendar by the brief's dated decision; a run that lists it as "off" or omits it passes; a run
   that schedules it fails the scope rule (one end state).
8. Halloween app icon (Martin's post also mentions an icon) → not a live-ops beat; out of scope, never graded.
9. Sheet layout, wording, date format, PT/UTC rendering of the same instant → any equivalent accepted (learnings §8).

### 5.3 Boundaries the rubric accepts in full

Row layout (one row per beat or per window), labels, PT or UTC (or both) for the same instant, the order of the
recommendation, owner names only where a record names one by name (tokens such as `[PERSON_NAME_0092]` are never graded).

### 5.4 Writes the rubric will not loosen

The reply goes in Frederick's DM (not a channel post); the calendar link goes on ZOM-78 (not a new ticket); pushes that
fail the copy rule are held, not rewritten in place — learnings §5.

### 5.5 Coherence plan for every artifact on the required path (rule 3; `1_Prompt_Eval.md` §3.2 "fails on the presence")

Precedent: learnings §51 treated "never graded" as safe for touched cards; the red-team review (§13, finding 1) and
Claire's analysis (§6.4 there) read §3.2 more strictly. This plan follows the stricter reading: every artifact a correct run
must open is listed with the contradictions it carries, and each is either kept **off** the required path or resolved as a
**dated human claim overturned by a later seeded record** (playbook 01 S1 `dated_claim`; never a silent field edit).

| Required artifact | Known contradictions it carries | Resolution |
|---|---|---|
| `page_liveops_calendar` (Frederick, v3 2025-09-29) | SC-62: "Reward tables are re-imported … hourly in production" vs the CDK stack and Douglas's Sep 8 DM (5 min); DD rows (Streak Fever "Shipped Apr 2025", Weekly Quests "Failed Nov 2024", the weekend-outage note) vs `LIVE_EVENT_PERFORMANCE` and other pages (SC-31, SC-47); "Weekly Leaderboards — DD / ZM3D — Live" vs a warehouse with DD-only rows; "Company-wide sync is the Friday all-hands" vs no 2025 H2 all-hands event (S4 §5) | SC-62: Douglas's seeded `#zombie-ops` note (Sep 30) states the import runs every 5 minutes on prod and asks Frederick to fix the page — a dated claim overturning the page's sentence. DD rows and the leaderboard row: their other side (`LIVE_EVENT_PERFORMANCE`, `page_live_ops_engine`'s DD timeline) stays off the required path (no deciding read, no graded value; Plague Race cadence comes from a seeded statement). All-hands: never cited, no deadline rests on it. **Residual risk:** a reviewer who opens the warehouse can still pair the DD rows with the page; recorded in §10 |
| `page_season_pass_spec` (v2 2025-09-30) | SC-38: "Reached production in the week of September 22-29" vs match3d#438 in builds from Sep 15; "Purchase and tier-claim events are tagged" vs ZOM-552 In Progress | the task uses only the cadence, lock and rename lines. The "tagged" claim gets a seeded dated note on the **open** ZOM-552 ("purchase and claim events are not tagged yet") overturning it. "Production" = the store releases (Android 0.3.127 Sep 22, iOS 0.3.49 Sep 29, `C0880U9751A/1759182908.627389`) vs earlier internal builds — argued as consistent, recorded as residual risk |
| Push sheet `f_a325dd4af80afc5994d5dc` | "PNs" (Domino-era) vs "PNs Beta" tabs; "Win & Collect event start" naming for ZM3D (the page says the two names are one feature) | two tabs with different purposes, not a contradiction; only "PNs Beta" is graded; the stale title on two Ready rows is the designed work item, overturned by the rename record |
| Frederick DM, Robert DM, `#zombie-design`, `#company-internal`, `#zombie-art`, `#zombie-ops`, `#zombie-bugs` | SC-7 (membership), SC-70 (Slack time zones) | membership and time zones never used; seeded DM text only in English DMs |
| ZOM live-ops issues, ZOM-78, ZOM-552 | SC-16 tickets (ZOM-513/514/563/564, ART-790/792) are **not** in the cohort (checked); SC-22 `time_in_status` | never used |
| `match3d` #468/#470/#472; `match3d-backend` | SC-18 (#477 open/closed); SC-56 (commit-title case) | #477 is not on the path; Collect & Win readiness rests on the backend note; no `#builds` title matching |
| Off the path (kept off on purpose) | Trello BETA list "BETA: Oct 10" (SC-13) and cards 54/56/58/67 (SC-14); `LIVE_EVENT_PERFORMANCE`; `page_live_ops_engine`; `page_product_okrs` (SC-28); `page_zm3d_gdd` (SC-8, SC-58) | no deciding fact or graded value; the rename comes from the Season Pass spec instead of the GDD |

Coherence hazards touched (KB `coherence_hazards.json`, S5b §1): T04 (completion vs merge), S01, R07, L03, I15 (Julia's
Zombie Lane doc), I01/I18 (raw-shaped Slack rows, strikethrough retractions), Q01/Q04 (thread counters for appended
replies), L08–L10 (lifecycle stamps). `/create-scenario` S1 cites each with its disposition; all six categories are covered.


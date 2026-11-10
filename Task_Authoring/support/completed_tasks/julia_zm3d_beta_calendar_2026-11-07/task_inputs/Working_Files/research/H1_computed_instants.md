# H1 — Computed Instants (UTC arithmetic seeds)

Clock: 2025-10-01 00:00 PT (07:00Z) · Universe: synth-cut (`hg4-synth-sep30cut`) · Persona: Julia Lawson (PM),
calendar time zone **Europe/Istanbul**. Every instant below is computed with Python `zoneinfo` against the system
tzdata (verified: `Europe/Istanbul` = `+03` at 2025-06-01, 2025-10-08, 2025-10-31, 2025-11-02, 2025-11-15 and
2026-01-15 — no transition anywhere in the task window; `America/Los_Angeles` = `PDT` (−07) through 2025-11-02
08:59Z and `PST` (−08) from 09:00Z).

Status: COMPLETE

---

## 1. Turkey / Istanbul offset in Oct–Nov 2025

**Result: Europe/Istanbul is a fixed UTC+3. There is no DST ambiguity in Oct or Nov 2025. Conversion = subtract
exactly 3 h to reach UTC.**

Basis (three independent legs):

1. **Legal.** Council of Ministers Decision (BKK) **2016/9154**, *Gün Işığından Daha Fazla Yararlanmak Amacıyla Bütün
   Yurtta Yaz Saati Uygulanması Hakkında Karar*, Resmî Gazete **8 Sep 2016, No. 29825** — it kept the country on the
   summer offset (UTC+3) **year-round** and expressly repealed the 30 Oct 2016 04:00 fall-back. A 2018 presidential
   decree reaffirmed UTC+3 as the permanent zone (the 2018 "revert to EET" announcement was withdrawn in Nov 2017).
   The zone is now legislated as **Turkey Time (TRT)**, UTC+3 all year.
2. **IANA / tzdata.** `Europe/Istanbul` carries no DST rule after 2016; the computed offset is `+03` for every date
   probed in this task:
   `2025-06-01T00:00+03`, `2025-10-08T00:00+03`, `2025-10-31T00:00+03`, `2025-11-01T00:00+03`,
   `2025-11-02T00:00+03`, `2025-11-15T00:00+03`, `2026-01-15T00:00+03`.
3. **Base corroboration.** The universe's own calendar metadata and invite mail render this zone as Istanbul time:
   `gcal/data.json` → `calendars[]` entry `calendar_id julia.lawson@harmonygames.co`, `summary "Julia Lawson —
   primary"`, **`time_zone "Europe/Istanbul"`** (`primary: true`, `access_role: owner`). Base GCal invitation mails
   print times as **"Türkiye Time"** and carry the Google Calendar link parameter **`ctz=Europe%2FIstanbul`**
   (e.g. `gmail/threads/vincent@harmonygames.co_1804687682049651007.json`,
   `claire@harmonygames.co_1775041180496662380.json`). So the display label a run will see is "Türkiye Time" /
   "Istanbul", meaning +03.

Cross-check of the other people this task touches (same table): **Douglas = `America/El_Salvador`**, Owen =
`America/El_Salvador`, Frederick = `America/Los_Angeles`, Robert = `UTC`, Leonard = `America/Los_Angeles`,
Vincent = `UTC+03:00`, Brian = `UTC+03:00`. Note that most colleagues' rows hold the literal string `UTC+03:00`
(not an IANA name) while **Julia's is the IANA name `Europe/Istanbul`** — Julia's calendar is the only place in the
universe where the string "Istanbul" appears at all (1 occurrence in the whole 23 MB gcal export).

**No DST trap exists here, and that is deliberate:** the C9 trap is the 3 h conversion *plus* the direction of the
comparison, not a DST question. A run that "helpfully" applies a November DST fall-back to Turkey produces
10:00 TRT = 08:00Z (7 h off in the conversion, still late) — see §3's wrong-answer list.

---

## 2. Collect & Win first prod window

### 2.1 Windows from the cadence rule (all opens `00:00 UTC`)

Cadence: Mon–Tue / Wed–Thu / Fri–Sun, each opening at 00:00 UTC; span Mon Oct 6 00:00Z – Sun Nov 2 23:59Z. The
opens therefore fall on Mon/Wed/Fri only — **nothing opens on a Thursday**:

| Window | Opens (UTC) | Closes (UTC) | Opens (PT) | Opens (Istanbul) |
|---|---|---|---|---|
| Mon–Tue | Mon Oct 6 00:00 | Tue Oct 7 23:59 | Sun Oct 5 17:00 PDT | Mon Oct 6 03:00 |
| Wed–Thu | **Wed Oct 8 00:00** | Thu Oct 9 23:59 | Tue Oct 7 17:00 PDT | Wed Oct 8 03:00 |
| Fri–Sun | **Fri Oct 10 00:00** | Sun Oct 12 23:59 | **Thu Oct 9 17:00 PDT** | Fri Oct 10 03:00 |
| Mon–Tue | Mon Oct 13 00:00 | Tue Oct 14 23:59 | Sun Oct 12 17:00 PDT | Mon Oct 13 03:00 |
| Wed–Thu | Wed Oct 15 00:00 | Thu Oct 16 23:59 | Tue Oct 14 17:00 PDT | Wed Oct 15 03:00 |
| Fri–Sun | Fri Oct 17 00:00 | Sun Oct 19 23:59 | Thu Oct 16 17:00 PDT | Fri Oct 17 03:00 |
| Mon–Tue | Mon Oct 20 00:00 | Tue Oct 21 23:59 | Sun Oct 19 17:00 PDT | Mon Oct 20 03:00 |
| Wed–Thu | Wed Oct 22 00:00 | Thu Oct 23 23:59 | Tue Oct 21 17:00 PDT | Wed Oct 22 03:00 |
| Fri–Sun | Fri Oct 24 00:00 | Sun Oct 26 23:59 | Thu Oct 23 17:00 PDT | Fri Oct 24 03:00 |
| Mon–Tue | Mon Oct 27 00:00 | Tue Oct 28 23:59 | Sun Oct 26 17:00 PDT | Mon Oct 27 03:00 |
| Wed–Thu | Wed Oct 29 00:00 | Thu Oct 30 23:59 | Tue Oct 28 17:00 PDT | Wed Oct 29 03:00 |
| Fri–Sun | Fri Oct 31 00:00 | Sun Nov 2 23:59 | Thu Oct 30 17:00 PDT | Fri Oct 31 03:00 |

(12 windows in the span. Every PT value above is **PDT**, UTC−7 — see §4 caveat.)

### 2.2 The admissible band for the deploy

The brief's rule: *a beat starts with the first window that opens AFTER its server windows are live on prod*, and
the server windows only go live with Douglas's prod backend deploy.

- Condition (a) — the Wed–Thu window must open **before** the deploy. The Wed–Thu window opens
  `2025-10-08 00:00Z` = **`2025-10-08 03:00` Istanbul**. So the deploy must be later than 03:00 local, i.e. later
  than `2025-10-08 00:00Z`.
- Condition (b) — the first window opening **strictly after** the deploy must be Fri–Sun. The next open after
  Wed–Thu is `2025-10-10 00:00Z` = `2025-10-10 03:00` Istanbul; the one after that is Mon Oct 13. So the deploy must
  be earlier than `2025-10-10 00:00Z` (= before Fri 03:00 Istanbul).
- Because no window opens on Thursday, **the whole 48 h interval `(Wed Oct 8 00:00Z, Fri Oct 10 00:00Z)` — i.e.
  `(Wed Oct 8 03:00, Fri Oct 10 03:00)` Istanbul — is admissible.** The only further requirement is plausibility
  (a workday evening).

### 2.3 Recommended seed value

**Seed: `Wed Oct 8 2025 18:00 Europe/Istanbul`** (= 18:00 TRT), one-hour release window 18:00–19:00 local.

```
18:00 Istanbul (UTC+3)  −  3 h  =  15:00 UTC        Wed Oct 8 2025 15:00Z
end 19:00 Istanbul      −  3 h  =  16:00 UTC        Wed Oct 8 2025 16:00Z
```

Comparisons, all shown:

```
Wed–Thu window open   2025-10-08 00:00Z   (Wed 03:00 Istanbul)
deploy                2025-10-08 15:00Z   (Wed 18:00 Istanbul)
→ deploy is 15 h AFTER the Wed–Thu open
→ the Wed–Thu window's opening instant is already in the past when prod goes live:
  it is pre-empted / not a clean post-deploy window   ⇒ condition (a) satisfied

next window open after the deploy
   Thursday?  none (cadence opens Mon/Wed/Fri only)
   Fri–Sun window open  2025-10-10 00:00Z  (Fri 03:00 Istanbul)
→ 33 h after the deploy, and it is the FIRST open after the deploy   ⇒ condition (b) satisfied
```

(Cross-check on the earlier window: Mon–Tue Oct 6 00:00Z is also before the deploy, so it is irrelevant; the
deploy at 15:00Z Oct 8 clears the entire first week of the span, which is why the calendar's first Collect & Win
prod window is the Fri–Sun one.)

**Answer — first Collect & Win prod window:**

```
Fri Oct 10 2025 00:00 UTC   =   Thu Oct 9 2025 5:00 PM PDT   (17:00, UTC−7)
                               Fri Oct 10 2025 03:00 Istanbul
```

PT check: US DST 2025 ends **Sun Nov 2 2025 09:00Z** (02:00 local), so Oct 9 is still **PDT = UTC−7**:
`2025-10-10T00:00Z − 7 h = 2025-10-09T17:00 PDT = Thu Oct 9, 5:00 PM PDT`. Correct.

### 2.4 Accepted renderings (any one passes; all are the same instant)

1. `Fri Oct 10 2025 00:00 UTC`
2. `Fri 10 Oct 2025, 00:00 UTC`
3. `2025-10-10T00:00:00Z`
4. `Thu Oct 9 2025 5:00 PM PDT`
5. `Thursday, October 9, 2025 at 5:00 PM PDT`
6. `Oct 10 00:00 UTC (Thu Oct 9, 17:00 PDT)`
7. `Fri–Sun window, opening Fri Oct 10 00:00 UTC / Thu Oct 9 5:00 PM PT`
8. `Fri Oct 10 03:00 Istanbul (00:00 UTC)` — same instant rendered in Julia's calendar zone

Do **not** accept (different instants / wrong logic): `Wed Oct 8 00:00 UTC` (the Pre-empted window),
`Mon Oct 6 00:00 UTC` (first window in the span), `Thu Oct 9 00:00 UTC` (cadence misread — no Thursday open),
`Fri Oct 10 15:00 UTC` (the deploy time used as the window), `Thu Oct 9 12:00 AM PDT` (00:00Z read as local
midnight), `Thu Oct 9 4:00 PM PST` (PST applied in October — wrong by 1 h), `Fri Oct 10 5:00 PM PDT` (sign error).

### 2.5 Seed-shape notes for the walkthrough event (Wed Oct 8)

- Store `start.dateTime = 2025-10-08T15:00:00Z`, `end.dateTime = 2025-10-08T16:00:00Z`. **Never** `18:00Z`: every
  one of the 10,395 base events stores UTC with a `Z` suffix (0 non-Z, 0 all-day), events carry **no per-event
  time zone field**, and 18:00 local is visible only through Julia's `time_zone` (`Europe/Istanbul`) — so a `18:00Z`
  row would display as 21:00 Istanbul and would still give the same graded answer (18:00Z Wed < Fri 00:00Z) while
  being visibly wrong in the calendar.
- Organizer `douglas@harmonygames.co` is rare but precedented (base: exactly one Douglas-organized event,
  "Quest discussion", 2024-06-05, uid 1, 2 rows). Safe attendees: Douglas (self), Julia, Owen, Frederick
  (+ Vincent/Leonard if the copy needs a release-manager witness). One row per attendee calendar with `self:true`
  on the owner's copy, identical `created`/`updated`, `sequence` 0…n (base precedent 0–11 on a 12-copy event),
  `ical_uid <hex>@hg4`, `status confirmed`, `transparency opaque` (all 10,395 base rows are `opaque`), one-hour
  duration (2,097 base events are 60 min; 30 min is the mode), `rrule []`, `hangout_link` a meet link or `null`
  (267 base nulls).
- `created`/`updated` at or before the seed bound and after the base events it rests on — §5.6 allows
  "release plan event created Sep 30 21:00Z".
- Any other admissible deploy time gives the identical graded answer, e.g. `12:00 Istanbul = 09:00Z`,
  `21:00 Istanbul = 18:00Z`, `23:00 Istanbul = 20:00Z` on Wed Oct 8. The instant only becomes wrong if it moves
  before `Wed 00:00Z` (then the Wed–Thu window would be the first clean window) or after `Fri 00:00Z` (then the
  first clean window would be Mon Oct 13).

---

## 3. Season Pass November config lock

### 3.1 The chain

Rule: config locks **24 h before** the season opens; Season Pass seasons open on the 1st at **00:00 UTC**.

```
season open        Sat Nov 1 2025 00:00 UTC
lock = open − 24h  Fri Oct 31 2025 00:00 UTC
   PT rendering    Thu Oct 30 2025 17:00 PDT   = 5:00 PM PDT   (PDT: Nov 2 has not happened yet)
   Istanbul view   Fri Oct 31 2025 03:00 (+03)

Brian's committed delivery  "Fri Oct 31, 10:00 Istanbul time"
   10:00 TRT − 3 h = 07:00 UTC          Fri Oct 31 2025 07:00Z
   PT rendering                          Fri Oct 31 2025 00:00 PDT (midnight)

comparison  07:00Z  −  00:00Z  =  +7 h   →  SEVEN HOURS LATE
(equivalently in Istanbul terms: 10:00 − 03:00 = 7 h after the lock instant)
```

So Brian's date is right (Fri Oct 31) and even the *day* boundary is right, but the **instant** misses the lock by
7 h. The corrected deadline Julia must state is **at or before `Oct 31 2025 00:00 UTC`** — i.e. she must move
Brian's handoff a day earlier in his local clock, to **Thu Oct 30, 5:00 PM PDT = Fri Oct 31, 03:00 Istanbul**.

### 3.2 Accepted renderings of the corrected deadline (all the same instant)

1. `Oct 31 2025 00:00 UTC`
2. `Fri Oct 31 2025, 00:00 UTC`
3. `2025-10-31T00:00:00Z`
4. `Thu Oct 30 2025 5:00 PM PDT`
5. `Thursday, October 30, 2025 at 5:00 PM PDT`
6. `Oct 30 5:00 PM PT / Oct 31 00:00 UTC (at the latest)`
7. `Fri Oct 31 03:00 Istanbul (= 00:00 UTC)` — same instant in Julia's calendar zone
8. `by end of day Thu Oct 30 Pacific (17:00 PDT), which is 00:00 UTC Oct 31`

### 3.3 Renderings the grader must NOT accept (wrong answer, kept on purpose)

1. **"Fri Oct 31, 10:00 Istanbul time — on time / fits the lock."** The whole trap: 10:00 TRT = 07:00 UTC, 7 h
   after the lock. Any row that marks Brian's delivery as on time, or that keeps 10:00 Istanbul as the deadline,
   fails.
2. **`Oct 31 2025 07:00 UTC` as the deadline** (Brian's instant promoted to the deadline; 7 h late).
3. **`Oct 31 2025 10:00 UTC`** (Moscow-Time-style confusion / Istanbul time read as UTC — 10 h late).
4. **`Nov 1 2025 00:00 UTC` as the deadline** (lock confused with the season open, 24 h late) — and its cousin
   **`Oct 30 2025 21:00 UTC` / `Oct 30 2:00 PM PDT`** that comes from computing the lock off Nov 1 00:00 *Istanbul*
   (= Oct 31 21:00Z, minus 24 h): a different instant, so not accepted even though it is safely early.
5. **`Oct 31 2025 08:00 UTC`** (a November DST fall-back wrongly applied to Turkey).
6. Any **PST** rendering of an Oct instant (`Thu Oct 30 4:00 PM PST`) — wrong by 1 h; PST does not begin until
   Nov 2 09:00Z.

Harmless but still *not* the lock instant (so not accepted as the deadline, only as "safely early"): `Oct 30
00:00 UTC` (24 h early, from double-subtracting).

---

## 4. Coherence check against base

Verified directly in `Universe_SynthCut` (read-only). Nothing contradicts the two computed instants.

**Time zone.** Julia's calendar row is the only `Europe/Istanbul` in the export and it is internally consistent;
invite mails label the same zone "Türkiye Time" with `ctz=Europe/Istanbul`. Caveats: (i) 33 of 38 calendars store
the literal string `UTC+03:00` rather than an IANA name — a run that only looks at colleagues' rows will not learn
the offset, so the graded fact must stay reachable through Julia's own calendar row (it is: `calendar_id`,
`time_zone`, `primary: true`, `access_role: owner`); (ii) the calendars table is the *only* place the string
"Istanbul" occurs in base (1 hit in 23 MB) — no per-event time zone exists to corroborate it, so a rubric row that
demands "Istanbul time" must accept the UTC/PT renderings of the same instant.

**Oct 8 slot is empty.** Between 2025-10-05 and 2025-10-25 the export holds exactly two distinct events
("Portland Marathon" Oct 5 13:30Z, "[SOURCE_ORG_0001] Board Meeting" Oct 14 16:00Z, 4 copies). There is **no event
of any kind on Oct 6–13 2025 in any of the 38 calendars**, hence no pre-existing Douglas, Julia, Owen or Frederick
row at the Oct 8 slot to collide with. Douglas organizes exactly one event in base (2024-06-05 "Quest discussion"),
so a Douglas-organized release-plan event is rare but not unprecedented; the event shape must match the base
16-key schema (§2.5).

**No base record dates a Collect & Win prod deploy.** `#zm-collect-win` (C09EVVCFHKR, 102 messages in Sep 2025)
is dev-build/QA traffic only (build numbers #1887/#1920/#1954/#1982, "current working branch
`…/winAndCollect`", client/server bug reports) and never mentions prod, a deploy date or a window open. The ZM
channels (C0880U9751A `#zombie-match3d`, C08R27X0EAH `#zombie-bugs`, C090N54TG79 `#zombie-design`, C08R6BF4ENN
`#zombie-ops`, C080X4GTZ0E `#live-incidents`, C05433XK267 `#builds`) contain **no** sentence joining "Collect &
Win" to prod/deploy/release; the canvas channel C3DD99314033 (Collect&Win issues) is QA-triage. Gmail: 26 threads
mention Collect & Win — asset/prefab paths, review bots, a 2024 "Collect&Win Onboarding" invite and a Magical
Wings doc notice — none carry a prod date. The only *dated* environment hint in base is Douglas's/Slack phrase
"we deployed to prod yesterday" in unrelated July/Aug 2025 messages, which fixes no cadence and no October date.

**Nothing states the Nov 1 season or a 24 h lock.** No base Slack message in the ZM channels contains
"November"/"Nov 1"/"Nov 2" together with Season Pass, and no mail states a config lock — the lock rule lives only
in the brief, as designed (§5.1 "Still to do and locks"). So C9's arithmetic is uncontradicted by base and the
only competing artefact is Brian's mail (the trap itself).

**Trello corroborates, mildly.** ZM ROADMAP's outside list carries a card whose name reads "BETA: Oct 10" —
consistent with Fri Oct 10 as the first prod window. Caveat carried from R-C §5: a worker read the same card as
"BETA: Sep 30"; build must re-check before citing it. Either reading is coherent (Sep 30 = cut/submission date,
Oct 10 = beta launch) — so cite it nowhere load-bearing.

**PT/PDT caveat (affects grading of every row).** US DST 2025 ends Sun Nov 2 09:00Z. Every instant graded here
(Oct 8, Oct 10, Oct 30, Oct 31) is **PDT = UTC−7**; only the tail of the span flips — `Sun Nov 2 23:59Z` =
`Sun Nov 2 15:59 PST`. A run that renders any October instant in PST, or claims a Nov 1 season open at
"Oct 31 4:00 PM PST", is off by one hour and must not be accepted. The `Nov 1 00:00Z` season open itself renders
as `Fri Oct 31 17:00 PDT`.

**One coincidence worth knowing when writing rows.** The lock instant `Oct 31 00:00Z` is exactly the open of the
last Fri–Sun Collect & Win window in the span. That is not a conflict (different beats), but two rows in the same
sheet will share an instant — a grader must not read one as evidence for the other.

---

### Seed values (copy-ready)

| # | Seed | Local (Europe/Istanbul) | Stored UTC (`start.dateTime`) | End (UTC) | Created/updated |
|---|---|---|---|---|---|
| S1 | Douglas prod backend release (deploy) — Julia's calendar + Owen/Frederick copies | **Wed Oct 8 2025 18:00** | `2025-10-08T15:00:00Z` | `2025-10-08T16:00:00Z` | ≤ 2025-09-30T21:00Z (precedent: "release plan event created Sep 30 21:00Z") |
| S2 | Brian's handoff mail body (seed **text**, not a calendar instant — "Fri Oct 31, 10:00 Istanbul time") | Fri Oct 31 2025 10:00 | `2025-10-31T07:00:00Z` (the *wrong* instant, on purpose) | — | ≤ 2025-09-30T17:30Z (Brian's mail) |

### Computed answers (copy-ready)

| Graded decision | Answer (UTC) | Answer (PT) | Same instant, Julia's zone |
|---|---|---|---|
| Collect & Win first prod window (C1) | **Fri Oct 10 2025 00:00 UTC** | **Thu Oct 9 2025 5:00 PM PDT** | Fri Oct 10 03:00 Istanbul |
| Season Pass November config deadline (C9) | **Fri Oct 31 2025 00:00 UTC** | **Thu Oct 30 2025 5:00 PM PDT** | Fri Oct 31 03:00 Istanbul |

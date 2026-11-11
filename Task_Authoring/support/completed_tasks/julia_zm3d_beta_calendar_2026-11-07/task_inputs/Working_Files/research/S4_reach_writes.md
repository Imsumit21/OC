# S4 — Julia's reach and write targets at the clock (synth-cut)

Sections 1–6 from the S4 worker's report (it ran out of steps before writing; findings copied unchanged). Section 7 was
run by the build session (verbatim `persona_view.py can-see` output).

## 1 · Julia's Drive (28 owned items, root `d_8140f09bf9f1b94cb8ee2d`)

- 27 children; one subfolder `Zombie Art` (`d_10809994aaf374642abff9`). No live-ops sheet exists in her Drive.
- Live-ops artifacts she owns: Docs `[LiveOps] Event Icon Management System` (`f_744027532fb1b0cc8821c4`, 2025-07-28) and
  `[Zombie Ops] Zombie Lane` (`f_023c7331d7e34900bd226f`, 2025-07-18). Owned sheets are older (`FTUE Catalogue`
  `f_b0b363c2af4e4ff5f529b9`, `ZM Bundles` `f_3292ed0d08d8cfbe80f005`, two "DO NOT USE" files).
- Drive ↔ Sheets/Docs owner fields agree for the 9 ids checked; `f_a325dd4af80afc5994d5dc` (Push Notifications Zombie
  Match) is owned by `Resource: -6481757892984311338` and shared with Julia (readable; not a safe write target —
  learnings §31).
- Consequence: any graded write target must be a Julia-owned file created at run time (or seeded with Julia as owner in
  both the Drive and Sheets rows), e.g. inside a seeded Julia-owned folder.

## 2 · Write tools (Evals/references/tools/catalog.json)

- `gsheets_create_spreadsheet(title, initialSheetTitle, driveFileId)` — one tab at creation; more tabs need
  `gsheets_batch_update` with `addSheet`. Values: `gsheets_values_update` / append.
- `gdocs_create_document(title, bodyText, driveFileId)`; `gdrive_share_file`.
- Slack: `slack_send_message` (thread replies via thread_ts), drafts, `slack_read_thread`.
- Linear: `linear_create_issue` (`parentId`, `links`), `linear_create_comment`, `linear_update_issue`.
- `gcal_create_event`; `gmail_send_message` / `gmail_reply_to_message`; `trello_add_comment` / `trello_create_card`.

## 3 · DM language (Aug–Sep 2025)

- English: Robert `D05GU6L0XFH`, Frederick Stone `D05SD5QLG94`, Martin Walsh `D05QESBD4HW`, Marcus Bennett `D05TZ6N1QBH`,
  Calvin Price `D05HYDTG5TJ`, Oliver Brooks `D07GMT8T0AY`.
- Turkish (heavy): Brian Foster `D076RBM29JS`, Vincent Parker `D05QA585LTY`, Claire Morgan `D05HMBQUC8Z`.
  Mixed/Turkish: Leonard Hayes `D05HB64NMQU` (Aug only). Douglas `D05PY755M5L`: no Aug/Sep 2025 messages (last 2025-04).
- Consequence: seeded DM text goes only into English DMs (Robert, Frederick, Martin) or matches the DM's language.

## 4 · Activity at the clock (KB `activity.json`)

14 of 15 checked people `active_sep_2025_quiet_in_oct` (Frederick, Robert, Leonard, Arthur, Douglas, Brian, Martin,
Marcus, Vincent, Oliver, Owen, Claire, Samuel, Calvin); Victor Barnes `quiet_since_2025-04` (cannot act).

## 5 · GCal

- Julia's calendar timezone Europe/Istanbul. No Julia event starts on/after 2025-10-01; her last event 2025-09-29.
- `POD: PROTOTYPE` (organizer Leonard, last 09-29); `Engineering Focused Weekly Planning` (organizer Marcus, last 09-29);
  `(Wednesday) Mid Week Art Sync` (robert@, next 2025-10-01 16:00Z) — Julia not an attendee.
- No recurring Friday all-hands in 2025 H2 ("All Hands" only Jan–Jun 2025). A deadline must not cite "Friday's
  all-hands" unless a record creates it.

## 6 · Gmail

253 threads / 304 messages, last 2025-09-17; Aug–Sep 2025 holds 4 non-work messages. No live-ops, beta, PlaytestCloud,
store or UA mail in her mailbox in the window — Gmail can carry weight only through seeded mail.

## 7 · `persona_view.py can-see julia_lawson …` (verbatim)

```text
julia_lawson slack C090N54TG79/1758517286.431379: YES
julia_lawson slack C05KNDCHAAG/1757704290.799329: YES
julia_lawson slack C05KNDCHAAG/1758558164.541689: YES
julia_lawson slack C08R8CHB0QL/1758121809.236839: YES
julia_lawson slack C08H78VJG80/1759174925.309129: YES
julia_lawson slack C090N54TG79/1757478958.104989: YES
julia_lawson slack C08R6BF4ENN/1756747348.667629: YES
julia_lawson slack D05SD5QLG94/1758220925.518329: YES
julia_lawson gsheets f_a325dd4af80afc5994d5dc: YES
julia_lawson gdocs f_744027532fb1b0cc8821c4: YES
julia_lawson gdocs f_023c7331d7e34900bd226f: YES
julia_lawson gdocs f_9956263905ddb43d1500ff: YES
julia_lawson gsheets f_c0518ab5dacb03dcc8a144: NO
julia_lawson gsheets f_89aebb6083dc44501666c7: NO
julia_lawson gsheets f_d224d9f6fcd6045faeee22: UNVERIFIED
julia_lawson confluence page_liveops_calendar: YES
julia_lawson linear ZOM-566: YES
julia_lawson trello 6851a6fde24742cce9ad7b1c: YES
julia_lawson gdrive d_8140f09bf9f1b94cb8ee2d: YES
```

Reading: the Season Pass reward sheets ("ZM Season Pass Backend" `f_c0518ab5dacb03dcc8a144`, "Zombie Match Economy 1.0"
`f_89aebb6083dc44501666c7`) are NOT readable by Julia; Vincent's "ZM3 - Event and League Bots" is UNVERIFIED (domain
only). None of the three can carry a graded value.

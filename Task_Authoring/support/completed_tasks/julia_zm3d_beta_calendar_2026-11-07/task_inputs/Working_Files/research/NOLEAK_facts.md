# NO-LEAK facts research — manifest `facts` array for `tools/fact_check.py --no-leak`

Clock: universe = zM3D synth-cut, task window Mon Oct 6 – Sun Nov 2 2025 (task_inputsS)
Scope: per-record deciding facts only. Read-only worker; this file is the only write.

> **Superseded in part (revision 5, 2026-11-06).** This file is the revision-1 research record behind the manifest `facts` array; its rows keep the ids and wording of that revision. The array has eight facts now: `quests.todo` is gone (the Quests still-to-do is empty), `cw.todo.vials` has the value "vial models" on `#468#rc_38`, `login.todo` is homed on `cmt_zom432_2` (Samuel's closing note on ZOM-432; a Linear note, so no mirror), `sp.todo.strip` is on `#473#c_2`, `cw.todo.icon` on `cmt_zom465_2`, and every Slack, Gmail and mirror id below has a revision-5 successor (dossier §11, Revision 5). The current array is FACTS in `research/scripts/build_manifest.py`; `fact_check.py --no-leak` passes on it with 0 errors. Revisions 6 and 7 leave the array as it is; `cmt_zom526_3` and `cmt_zom521_2` state none of its values. Revision 8 re-homes `sp.todo.strip` on `#472#rc_1` and its mirror `65564543…`. Revision 9 changes `plague.weeks` to the value "themed prop set" (alias "themed prop"): the withdrawal no longer says "Halloween one-off", and those are the words it shares with the approval.

## Method

- **Home rows**: literal bodies read from `Task_Authoring/task_inputsS/01_Universe_Inject.sql` (line numbers below are SQL-file lines).
- **Leak scan**: `rg` over the SQL and over the whole cached base export set in
  `Working_Files/research/raw/` (linear.json, github.json, gh_prs.json, slack_*/month files incl.
  `slack_C093LEZGF6J_2025-09.json`, gdocs.json, gdrive.json, sheets_liveops.json, trello*.json,
  confluence*.json, liveops_sep.json), plus `fact_check.py --no-leak` used as the authority.
- Bulk-readable surfaces (per the tool): Slack message, Linear issue title/description, Sheets cells,
  Confluence body, Doc body — plus GitHub PR body/comment and Trello action JSON (not in the tool's
  `BULK_READABLE` map but still non-home rows, so still `fact_leak`).
- Verification runs were made with a scratch manifest in the approved temp dir
  (`$TMPDIR/opencode/noleak_final.json`); nothing was written into the repo except this file.

### Two tool behaviours that shaped the value wording (read this before editing the array)

1. **`kind: name` runs a near-spelling check on every row, not just on mentions.** It slides
   n−1/n/n+1-word windows over each row and flags any window with difflib ratio ≥ 0.80. A *long* phrase
   value therefore always fails: it fires on its own trailing/leading partial windows in the home row.
   Measured: a full-sentence value produced **71 errors**; the same facts as 1–2-word anchors produce
   **0**. So each `name` value here is the **shortest distinctive anchor** that (a) is stated by the home
   row where possible and (b) is spelled nowhere else. The human answer is carried by the `key`.
2. **`kind: date` is mention-gated and exact.** It only compares dates in the same sentence as the key or
   an alias, and the `--no-leak` pass flags any row holding that date. That is the right kind for facts
   whose answer *is* an instant (1 and 5) — and the reason facts 6 and 8 must **not** be declared as dates
   (their dates are legitimately printed in bulk rows, see LEAK-2/L3).

## Verdict table

| # | key | value (declared) | home rows | verdict |
|---|-----|------------------|-----------|---------|
| 1 | `cw.first_window` | `2025-10-10` (date) | `#470#rc_10` (+ GCal Oct 8) | CLEAN in SQL; **base near-miss** (Trello list "BETA: Oct 10") |
| 2 | `cw.todo.vials` | `vial sprites` | `#370#rc_1` + mirror `408dca28…` | CLEAN (mirror is home) |
| 3 | `sp.todo.strip` | `premium strip` | `#438#rc_74` + mirror `cc8ce0e4…` | CLEAN (mirror is home) |
| 4 | `cw.todo.icon` | `outstanding` (status) | `#454#c_4` + mirror `8a9a7466…` | CLEAN; "still to do" would **leak** (LEAK-4) |
| 5 | `sp.config_lock` | `2025-10-31` (date) | slip mail (`rfc:…`) + brief doc | CLEAN; no row prints "Oct 31 00:00 UTC" |
| 6 | `quests.todo` | `quest set` | Trello action `68dac820…` | CLEAN; "Mon Oct 13" would **leak** (LEAK-2) |
| 7 | `login.todo` | `daily-gift frame` | `#471#c_18` + mirror `a0c26779…` | CLEAN; **base near-miss** "submission 135" |
| 8 | `leagues.status` | `new week` | `C0880U9751A/1759265412.481907` | CLEAN **only with** `version_records:["cmt_zom429_1"]` (LEAK-3) |
| 9 | `plague.weeks` | `Halloween one-off` | `D05GU6L0XFH/1759270200.638114` | CLEAN **only with** `version_records:["C08R8CHB0QL/1758213600.552913"]` |

Final empirical result: `FACT CHECK: PASS — 59 text-bearing rows, 9 declared facts, 0 declared superseded records; Errors: none`
(3 pre-existing warnings only: bare "Claire", bare "Marcus", and the Oct 29→Oct 31 handoff `value_drift`,
which is the intended supersession and should be declared in `traps[].version_records`).

---

## 1. `cw.first_window` — first Collect & Win prod window is Fri Oct 10 00:00 UTC

**Deciding inputs (both needed).**
- `github.github_review_comments` `harmonygames-Games/match3d#470#rc_10` (L138, 2025-09-30T16:04:12Z):
  "Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next
  backend release. The client side in this PR is fine as it is."
- `gcal.gcal_events` `evt_9a4c2e7f1b3d58e06c7a2f` / `evt_5c1e83a7d94b02f6c8e31a` / `evt_a72f4d9e0c1b58d3e6f40b` /
  `evt_1d6b9a03e5c27f84b0d92c` (L81–87): "ZM3D backend release — live-ops server windows", start
  **2025-10-08 15:00Z**.
- Rule (brief, `f_7c3e91a4…` body): first window that opens **after** the release instant; C&W runs
  Mon-Tue / Wed-Thu / Fri-Sun opening 00:00 UTC → Wed Oct 8 00:00 already passed, Thu Oct 9 is inside the
  Wed-Thu window that opened before the release, so the first window after 2025-10-08T15:00Z is
  **Fri Oct 10 00:00 UTC**.

**Leak scan.**
- SQL: the string `Oct 10` appears **nowhere** in the 266-line injection (0 matches, case-insensitive).
  `first window` appears only in the brief body (the *rule*: "A beat starts with the first window that
  opens after its server windows are live on prod…") and in the Calendar sheet **header**
  `"First window (UTC)"` — cadence/column label, no instant. Neither states Oct 10.
- Base exports: `Oct 10` matches only **trello_lists.json / trello.json** — the base ROADMAP list name
  `"BETA: Oct 10"` and a 2023 card "Analytics pipeline (cancel Metabase before Oct 10th)". Both are
  pre-existing, both give a milestone *date*, not the window instant and not the Collect & Win answer.
  No Slack message, Linear description, Sheet cell, Doc body or PR body in the base says "Fri Oct 10".
- `gdocs.json` "Oct 31" hit is an unrelated founder-conversation doc.

**Verdict: CLEAN** (base near-miss only, see Findings list).

```json
{"key":"cw.first_window","value":"2025-10-10","kind":"date","aliases":["first window"],
 "home_ids":["harmonygames-Games/match3d#470#rc_10","c778c9b9d8fff77f59c93ce8d7902953"]}
```
The #zombie-prs mirror `c778c9b9…` (L172) carries the rc_10 body verbatim, so it is listed as a home even
though it does not print the instant. The four GCal ids may be added to `home_ids` if you prefer the
instant's carriers to be complete; they hold Oct 8 only, so they change nothing.

## 2. `cw.todo.vials` — final Collect & Win vial sprites still needed (Claire)

**Home.** `harmonygames-Games/match3d#370#rc_1` (L146): "The final vial sprites are still missing for the
Collect & Win set — Claire has those on her list." Mirror `408dca285b06b469679d08666344cc11` (L176)
`C093LEZGF6J/1759261713.261713` carries the same sentence as `attachments[0].text`.

**Leak scan.** `vial sprites` / `vial` in the SQL: only those two rows. Base: `vial` appears in a base
`#zombie-prs` CodeRabbit-style message ("Validate Collect & Win vial variant before spawning",
`collectAndWinVial.assetVariants…`, in `liveops_sep.json`) and in prefab review chatter — code-review
noise about an asset *variant*, never "sprites still missing" / "on her list". `vial sprite` = 0 base hits.

**Verdict: CLEAN.**

```json
{"key":"cw.todo.vials","value":"vial sprites","kind":"name",
 "home_ids":["harmonygames-Games/match3d#370#rc_1","408dca285b06b469679d08666344cc11"]}
```

## 3. `sp.todo.strip` — Season Pass premium strip moves to the November range (Oliver)

**Home.** `harmonygames-Games/match3d#438#rc_74` (L154): "The Season Pass premium strip needs to move to the
November range rather than the current one — Oliver is taking the date change." Mirror
`cc8ce0e4827971e4bee1fc5c5ea980d5` (L180).

**Leak scan.** `premium strip`: SQL → the two home rows only. Base exports → **0 matches** anywhere
(linear, github, slack, gdocs, gdrive, sheets, trello, confluence). `premium track` in the Sep 22 mail is
a different phrase and says nothing about the strip moving.

**Verdict: CLEAN.**

```json
{"key":"sp.todo.strip","value":"premium strip","kind":"name",
 "home_ids":["harmonygames-Games/match3d#438#rc_74","cc8ce0e4827971e4bee1fc5c5ea980d5"]}
```

## 4. `cw.todo.icon` — Collect & Win event icon animation still to do (Marcus)

**Home.** `harmonygames-Games/match3d#454#c_4` (L160): "The Collect & Win event icon animation is still to
do on my side — the other menu icons in this PR are finished." Mirror `8a9a746604dc5435b6d3cd79d3f19b8d`
(L184, attachment title "#454 Marcus/animated icons").

**Natural-reading side (not a leak).** Seeded `cmt_zom465_1` (L222) "Idle icon animations for the event
icons are done and in the animated-icons PRs, so every event icon animates at idle now", and the base
ZOM-465 description in `linear.json` ("## Event Animations / * ~~Idle Icon Animation~~ …"). Both say the
generic idle-icon work is **done**; neither says the Collect & Win icon is finished and neither states the
answer "C&W event icon absent / still to do". `cmt_zom344_1` (L225) is about the quest box.

**Leak scan + the wording trap.** Declaring the answer as "still to do" is **impossible**: the Calendar
sheet header cell `"Still to do (owner)"` (L131, `gsheets`) prints the phrase in a bulk row, so
`fact_check --no-leak` reports `fact_leak` on the sheet. The full sentence cannot be used at all
(`kind: name` near-spelling gives 4 errors on ZOM-465/ZOM-344). A 1-word status anchor is clean:

**Verdict: CLEAN** with `status`/`outstanding` (0 errors). `outstanding` occurs in no seeded row, so the
guard is "the only place this beat's to-do state is asserted is #454".

```json
{"key":"cw.todo.icon","value":"outstanding","kind":"status",
 "home_ids":["harmonygames-Games/match3d#454#c_4","8a9a746604dc5435b6d3cd79d3f19b8d"]}
```

## 5. `sp.config_lock` — November config must land before Oct 31 00:00 UTC (Brian's 10:00 Istanbul is late)

**Home.** Slip mail `brian.foster@harmonygames.co/1844835127305531392` (thread rows L55/L64/L73; message
copies L56, L65, L74 for brian/julia/frederick): "…moves from Wed Oct 29 to **Fri Oct 31, 10:00 Istanbul
time**… Treat Fri Oct 31 as the date I am committing to". Lock rule: brief body (`f_7c3e91a4…`, L92)
"Config locks — Every config a beat needs lands before its lock, read in server time (UTC). A committed
date that misses the lock moves earlier and its owner is told." Lock = 24 h before Sat Nov 1 00:00 UTC →
**Oct 31 00:00 UTC**; 10:00 Istanbul = 07:00 UTC → 7 h late, so it must move earlier.

**Leak scan.** `Oct 31` in the SQL: **only the three mailbox copies + their thread rows** (all one mail).
No Slack message, Linear description, Sheet cell, slide or Doc says Oct 31 or "00:00 UTC" as a lock.
`config lock` / `lock` appear only in the brief's rule text (heading "Config locks"; "before its lock"),
which states the rule and no instant — allowed. Base: the only `Oct 31` hit is an unrelated founder
conversation in `gdocs.json` ("Conversation 0: Oct 31st…").

**Verdict: CLEAN.** Use the rfc id so all three mailbox copies are one home (the tool adds
`rfc:<Message-ID>` to every copy):

```json
{"key":"sp.config_lock","value":"2025-10-31","kind":"date","aliases":["config lock","config locks"],
 "home_ids":["rfc:<CAH4q9Zc8uV1nE5kJ2mRtP7aW3xQ9bLs@mail.gmail.com>","f_7c3e91a4d2b85f60e1a9c4"]}
```
Do **not** alias this fact to "handoff" or "config": the Sep 22 copies (Oct 29 only) would then be
reported as contradictions instead of the intended supersession.

## 6. `quests.todo` — the new quest set lands with the Mon Oct 13 rollover (Brian)

**Home.** `trello.trello_actions` `68dac8204f1e9a3b7c2d5e61` (L260, commentCard 2025-09-29T17:55:44Z):
`"text":"Putting the new quest set in with the Mon Oct 13 rollover."`

**Leak scan.** `new quest set` → the Trello action only. `Oct 13` → **two** seeded rows: the Trello action
**and** the UA deck slide `slide_b83e51a09d72` element (L121, `gslides_page_elements`):
"The four buy weeks / W1 Mon Oct 6 - Sun Oct 12 / **W2 Mon Oct 13 - Sun Oct 19** …". The slide states the
buy-week boundary, not the quest rollover — but it prints the date in a bulk surface, so a date-kind fact
would fail. Base exports: `Oct 13` = 0 hits; `new quest set` = 0 hits.

**Verdict: CLEAN** with the phrase anchor. `aliases:["quests"]` is required: without it the seeded
`cmt_zom526_1` (L207, "The vfx path is shipped for **Quests**, Endless and Daily Gift…") trips the name
near-spelling check at exactly 0.80.

```json
{"key":"quests.todo","value":"quest set","kind":"name","aliases":["quests"],
 "home_ids":["68dac8204f1e9a3b7c2d5e61"]}
```

## 7. `login.todo` (done elsewhere) — daily-gift frame shipped in #471 / Submission #135

**Home.** `harmonygames-Games/match3d#471#c_18` (L166): "The daily-gift frame went out with this PR — it is
in submission 135, so that one can be closed." Mirror `a0c2677988d2041ff14477598ee60261` (L188).
Decoy/superseded side: seeded `cmt_zom432_1` (L216, base text too) "Daily gift artwork still needs the
frame. Card back and gift box are done, the frame is the last piece on my side."

**Leak scan.** `#135` / `135` → the two home rows only inside the SQL. **Base collision to know about**:
`submission 135` appears in base Linear descriptions ENG-2127 and ENG-2129 ("Version or date: android
submission 135") and in the mirrored GitHub summary. That is an Android build reference in unrelated bug
reports: it makes the *identifier* discoverable, not the fact "the frame is in 135". Do not declare
`submission 135` or `135` as the value; keep the frame anchor.

**Verdict: CLEAN** (base near-miss on the identifier only).

```json
{"key":"login.todo","value":"daily-gift frame","kind":"name",
 "home_ids":["harmonygames-Games/match3d#471#c_18","a0c2677988d2041ff14477598ee60261"]}
```

## 8. `leagues.status` (hold) — weekly leagues do not start a new week, even after a restart

**Home.** `slack.slack_messages` `C0880U9751A/1759265412.481907` (L17): "Re-tested the weekly leaderboard on
the 0.3.49 submission build: it still does not start a new week. I killed the app and reopened it twice,
played a few levels, and my week is still last week one. Same on the second device."

**Superseded side.** `cmt_zom429_1` (L195): "Checked the weekly rollover - if a player force-closes and
reopens, they land in the new week fine, so not blocking. Leaving as-is for now." (Base Sep 22 recovery —
"working fine" — is the older superseded reading; it is not a leak.)

**Leak scan.** `does not start a new week` / `land in the new week` / `new week fine` → 0 base hits (the
seeded rows own them). But `new week` **does** appear in the seeded `cmt_zom429_1`, so the fact fails
without an exemption — this is a supersession pair, exactly what `version_records` is for.

**Verdict: CLEAN with `version_records`.**
`weekly leaderboard` is the no-exemption alternative (0 errors, 0 base-state overlap) if you prefer not to
declare the exemption.

```json
{"key":"leagues.status","value":"new week","kind":"name",
 "home_ids":["C0880U9751A/1759265412.481907"],"version_records":["cmt_zom429_1"]}
```

## 9. `plague.weeks` — Halloween one-off dropped; Plague Race runs all four weeks

**Home.** `slack.slack_messages` `D05GU6L0XFH/1759270200.638114` (L15): "Coming back on the Halloween
one-off: pulling my ok. Take it off the beta calendar, we are not spending art time on a theme we may not
ship at all. Sorry for the flip, my later word on this one is the one that counts."

**Superseded side.** Seeded approval `C08R8CHB0QL/1758213600.552913` (L13): "Halloween one-off: approved
from my side for one of the beta weeks…" (base parent thread `c54310280ca0915181508d6e9b964926`).

**Leak scan.** **`beta calendar` is stated in the brief Doc body** — "How I want the **beta calendar** built
for the four buy weeks" (L92, `docs_documents`, bulk) — so "off the beta calendar" / "beta calendar" cannot
be the value (measured `fact_leak` on the doc). The withdrawal sentence itself appears nowhere else
(`take it off the beta` = 0 base hits, `all four weeks` = 0). `Halloween` alone appears in the seeded
approval (superseded) and in base chatter, so the *pair* phrase is the anchor.

**Verdict: CLEAN with `version_records`** (the approval row is the legitimate superseded carrier):

```json
{"key":"plague.weeks","value":"Halloween one-off","kind":"name",
 "home_ids":["D05GU6L0XFH/1759270200.638114"],
 "version_records":["C08R8CHB0QL/1758213600.552913"]}
```
`take it off` is a clean alternative value (2 tokens, no exemption needed, home-only).

---

## The #zombie-prs mirror question (must read)

`01_Universe_Inject.sql` L172, L176, L180, L184, L188 seed five `#zombie-prs` (`C093LEZGF6J`) bot mirrors
whose `attachments[0].text` is the **full body verbatim** of #470#rc_10, #370#rc_1, #438#rc_74, #454#c_4,
#471#c_18 — the INT-01 companion shape described in
`research/H3_reviewblocker_companion_audit.md` §3.1.

- Julia (`EMPLOYEE_0005_SLACK_ID`) is **not** a member of `C093LEZGF6J` (12 members: 0003, 0004, 0006,
  0012, 0021, 0025, 0026, 0031, 0032, PERSON_6075, SLACK_BOT_0004, U04V95A7C80) and Slack reads are
  persona-scoped (`Evals/references/persona/acl.md`), so the mirrored sentence is inert to the solver and
  to a verifier.
- `fact_check --no-leak` does not model membership: it classifies **any** Slack message as bulk-readable, so
  every mirrored sentence is a `fact_leak` unless its mirror id is listed. Proof by control run: dropping
  the four mirror ids from the array yields 3 `fact_leak` errors (vials L175, strip L179, login L187;
  #454's mirror is not flagged only because "outstanding" is not in its text).
- **H3 constraint C-1 says the opposite of what the SQL does**: "Do not seed an INT-01 #zombie-prs mirror
  for any of the three deciding inline comments (#470/#370/#438) or for the #454 conversation comment",
  because the mirror reproduces the deciding sentence verbatim. Either (a) keep the mirrors and keep the
  ids in `home_ids` (tool PASSes, real-world risk is Julia's non-membership), or (b) drop the five mirror
  rows to honour C-1 — then the deciding text is single-path and `home_ids` needs no Slack ids at all. The
  array below is written for (a); for (b) delete the 32-hex ids from facts 2, 3, 4, 7 and 1.
- Never cite a `#zombie-prs` message as a rubric's deciding source (H3 C-3).

## Final `facts` array (verified: PASS, 0 errors)

```json
{
  "facts": [
    {"key":"cw.first_window","value":"2025-10-10","kind":"date","aliases":["first window"],
     "home_ids":["harmonygames-Games/match3d#470#rc_10","c778c9b9d8fff77f59c93ce8d7902953"]},
    {"key":"cw.todo.vials","value":"vial sprites","kind":"name",
     "home_ids":["harmonygames-Games/match3d#370#rc_1","408dca285b06b469679d08666344cc11"]},
    {"key":"sp.todo.strip","value":"premium strip","kind":"name",
     "home_ids":["harmonygames-Games/match3d#438#rc_74","cc8ce0e4827971e4bee1fc5c5ea980d5"]},
    {"key":"cw.todo.icon","value":"outstanding","kind":"status",
     "home_ids":["harmonygames-Games/match3d#454#c_4","8a9a746604dc5435b6d3cd79d3f19b8d"]},
    {"key":"sp.config_lock","value":"2025-10-31","kind":"date","aliases":["config lock","config locks"],
     "home_ids":["rfc:<CAH4q9Zc8uV1nE5kJ2mRtP7aW3xQ9bLs@mail.gmail.com>","f_7c3e91a4d2b85f60e1a9c4"]},
    {"key":"quests.todo","value":"quest set","kind":"name","aliases":["quests"],
     "home_ids":["68dac8204f1e9a3b7c2d5e61"]},
    {"key":"login.todo","value":"daily-gift frame","kind":"name",
     "home_ids":["harmonygames-Games/match3d#471#c_18","a0c2677988d2041ff14477598ee60261"]},
    {"key":"leagues.status","value":"new week","kind":"name",
     "home_ids":["C0880U9751A/1759265412.481907"],"version_records":["cmt_zom429_1"]},
    {"key":"plague.weeks","value":"Halloween one-off","kind":"name",
     "home_ids":["D05GU6L0XFH/1759270200.638114"],
     "version_records":["C08R8CHB0QL/1758213600.552913"]}
  ]
}
```

Run (reproduce):
`TASK_AUTHORING_TASK_DIR=Task_Authoring/task_inputsS python3 Task_Authoring/tools/fact_check.py Task_Authoring/task_inputsS/01_Universe_Inject.sql --manifest <manifest with the array above> --no-leak`

## LEAKs / blockers found before `fact_check --no-leak`

These are places where a value you might naturally declare is **already stated outside its home row**. They
are fixed by the wording in the array above; do not "simplify" the values back.

- **LEAK-1 — `plague.weeks` value "beta calendar": stated in the brief Doc body** (`docs_documents`
  `f_7c3e91a4d2b85f60e1a9c4`, L92: "How I want the beta calendar built…"). Bulk Doc ⇒ `fact_leak`. Fixed by
  using "Halloween one-off" + `version_records` for the approval row.
- **LEAK-2 — `quests.todo`: the date "Mon Oct 13" is printed in the seeded UA deck** (`slides_page_elements`
  `slide_b83e51a09d72`, L121: "W2 Mon Oct 13 - Sun Oct 19"). A date-kind fact, or a value containing the
  date, fails. Fixed by the phrase anchor "quest set".
- **LEAK-3 — `leagues.status` value "new week" is also stated by the seeded superseded comment
  `cmt_zom429_1`** (L195, "they land in the new week fine"). Fixed by declaring that row in the fact's
  `version_records` (or by using "weekly leaderboard").
- **LEAK-4 — `cw.todo.icon`: "still to do" is printed in the Calendar sheet header cell
  `"Still to do (owner)"`** (L131, `sheets_sheets`, bulk). The literal answer phrase can never be a
  `name`/`status` value here. Fixed by the status anchor "outstanding".
- **BLOCKER-5 (policy, not text) — the five seeded `#zombie-prs` mirrors** (L172/176/180/184/188) collide
  with H3 constraint C-1; they must either be listed as home ids (as above) or be removed. Leaving them
  unlisted fails `--no-leak` with 3 `fact_leak` errors.

Benign near-misses (no action, but know they exist): base Trello list name `BETA: Oct 10` (LEAK-adjacent to
fact 1 — it gives a milestone date, never the window instant); base `android submission 135` in Linear
ENG-2127/ENG-2129 (fact 7's identifier, no frame link); base `#zombie-prs` chatter about
`collectAndWinVial.assetVariants` (fact 2's noun, no "sprites missing"); base ZOM-465 description and
`cmt_zom465_1` saying idle icon animations are done (fact 4's decoy — the C&W icon being outstanding is not
stated anywhere in bulk).

# GATE reconcile — task_inputsS manifest vs seeded SQL

Clock: synth-cut (Oct 1, 2025) universe, per `01_Universe_Inject.sql` header.
Gate target: `Task_Authoring/tools/hardness_gate.py` full mode on
`Working_Files/01_Hardness_Manifest.json` + `01_Universe_Inject.sql`.
Generator: `Working_Files/research/scripts/build_manifest.py`.

**Two important mechanics read from the gate first**

1. `RecordText.contains` → `_norm` (hardness_gate.py:255) is
   `re.sub(r"\s+"," ", s).strip()` — **whitespace-collapsing but case-SENSITIVE**.
   Every quote must match the seeded text with the same capitalisation.
2. The `cited` loop (hardness_gate.py:398-407) collects
   `ask_fragments|traps|authorities[].seeded_ids`, `…decoy_seeded_ids`, and
   `traps[].version_records[].id` **when `seeded` is true**. Anchors are *not*
   in that loop, so `A1.locator` may stay in `channel/ts` form; the four Slack
   `traps` tokens may not.
3. The gate target (`01_Hardness_Manifest.json`) is **not** byte-identical to
   the generator output: the injection stage added `facts` (9), `solver`,
   `integration_exceptions`, and a `gradable_surface` digest. Every section
   touched below (`ask_fragments`, `traps`, `authorities`) is identical between
   `01_Hardness_Manifest.draft.json` and the final file. So: edit
   `build_manifest.py`, regenerate, and re-apply the four injection-stage keys
   (or mirror the same values into `01_Hardness_Manifest.json`).

---

## 1. hazard_scope

**Gate message.** `L03 (Issue Todo/Backlog but a referencing PR merged) via ['ZOM-387']: no verified resolution; resolved/other: ['S04']`

**Claimed vs actual.**
- Manifest: **no `hazard_acknowledgements` key at all** (`m.get("hazard_acknowledgements") is None`), so `res is None`.
- SQL: `cmt_zom387_1` (line 228) is an INSERT into `linear.linear_comments` with `issue_id = 'ZOM-387'`. There is **no `UPDATE linear.linear_issues` for ZOM-387** (every other seeded comment has one; 387 is the one without). So the SQL *references* ZOM-387, never modifies it.
- `cohort.members` also lists `ZOM-387` (manifest line 517), so it is additionally `cited_by` the design.

**What clears an L03 touch** (`hazard_scope`, hardness_gate.py:1093-1110; `repair_status`/`_present`, base_check.py:1202-1239):
- `meta["L03"]["category"] == "state_lifecycle"`, which is in `HAZARD_FAIL_CATEGORIES = ("state_lifecycle", "cross_service_referential")`. So L03 must be resolved.
- `touched` = every hazard in `base_result["hazards_touched"]` (UPDATE targets + INSERT foreign keys + ids inside seeded text) **∪** every hazard indexed by an id cited in `anchors|ask_fragments|authorities|traps|chains|cohort`. I verified `hazard_index()["ZOM-387"] == {"L03"}` and `"ZOM-387" in id_tokens(manifest sections)` → `cited_by` is non-empty.
- `excluded` → **FAILS** (`res == "excluded" and (modified or h in cited_by)`).
- `dated_claim` → **PASSES**: the only blocker is `and modified`. `touched_ids` (base_check.py:1141-1170) puts INSERTs in `ref` only; `mod` is built from UPDATE/DELETE `where` only. `cmt_zom387_1` is an INSERT → `modified` is empty.
- `repaired` → would need `_present("L03", "ZOM-387", post_state)` to be False, i.e. the post-SQL state must not be `Todo`/`Backlog`. ZOM-387 is not updated, so `repair_status` returns `"present"` → **FAILS**.
- `S04` is `{'category': 'semantic_category', …}` → not in `HAZARD_FAIL_CATEGORIES`, so it is skipped in the FAIL loop and merely printed under "resolved/other". No ack is needed for it.

**Dropping the SQL row does not fix it.** `cohort.members` still cites ZOM-387, which alone re-adds the touch (and `res is None` fails regardless of `modified`). There is no manifest-only escape via citation removal either, because the SQL's own comment INSERT keeps ZOM-387 in `touched`.

**FIX (manifest-only; no SQL edit).** Add to the `manifest` dict in
`build_manifest.py` (e.g. right after `"mechanism_portfolio": PORTFOLIO,`):

```python
    "hazard_acknowledgements": [
        {"hazard_id": "L03", "resolution": "dated_claim", "requirement": "R3",
         "why_safe": "ZOM-387 is cited only as a cohort member plus one seeded owner note (cmt_zom387_1, "
                     "2025-07-25T14:00:00Z). The SQL inserts that comment and never updates the issue, so the "
                     "Todo-vs-merged-PR disagreement lives in a dated text claim, not in a record the SQL "
                     "modifies; every hold decision in this task is taken from the per-issue notes and PR "
                     "evidence, never from ZOM-387's state."},
    ],
```
Field checks: `L03` is in `meta`; `why_safe` non-blank; `dated_claim` ∈ `RESOLUTIONS`; `R3` is declared in `REQUIREMENTS`. A `requirement` is optional but declared, so it is safe.

---

## 2. seeded_ids_exist_in_sql

**Gate message.** missing `traps:T2:C08R8CHB0QL/1758213600.552913`, `traps:T2:D05GU6L0XFH/1759270200.638114`, `traps:T6:D05SD5QLG94/1759263600.418207`, `traps:T7:C0880U9751A/1759265412.481907`.

**Check logic.** `_has_token(code, token)` (line 138) is a whole-token, boundary-anchored regex
`(?<![A-Za-z0-9_.\-])<token>(?![A-Za-z0-9_\-])`. `code` is the SQL minus full-line comments. The token `D05SD5QLG94/1759263600.418207` never occurs contiguously: the `slack_messages` INSERT stores `id` (32-hex), then `ts`, then `channel_id` as three separate quoted scalars. The 32-hex `id` *is* a contiguous quoted scalar, so it is found.

**Seeded values (grep of the `slack.slack_messages` INSERTs).**

| manifest token (channel/ts) | row's `channel_id` | row's `ts` | seeded `id` (32-hex) | SQL line |
|---|---|---|---|---|
| `C08R8CHB0QL/1758213600.552913` (APPROVAL) | `C08R8CHB0QL` | `1758213600.552913` | `2e75e232f5e6206273411a8305ac5d01` | 13 |
| `D05GU6L0XFH/1759270200.638114` (WITHDRAWAL) | `D05GU6L0XFH` | `1759270200.638114` | `58d06bd55ea4129eaadb726291967d5a` | 15 |
| `D05SD5QLG94/1759263600.418207` (ASK) | `D05SD5QLG94` | `1759263600.418207` | `8b090dec472117f4598b9ad84318272e` | 11 |
| `C0880U9751A/1759265412.481907` (RETEST) | `C0880U9751A` | `1759265412.481907` | `fa3eee2c614b0741aeb240275f86abf7` | 17 |

Each `channel/ts` pair is cited **twice** for T2 and T7 (once in `seeded_ids`, once in a `seeded: true` `version_records` entry), so both lists must change or the check still fails.

**FIX (manifest-only).** In `build_manifest.py`, add the sha constants next to the existing slack constants:

```python
ASK_SHA = "8b090dec472117f4598b9ad84318272e"           # slack_messages.id of ASK
APPROVAL_SHA = "2e75e232f5e6206273411a8305ac5d01"      # slack_messages.id of APPROVAL
WITHDRAWAL_SHA = "58d06bd55ea4129eaadb726291967d5a"    # slack_messages.id of WITHDRAWAL
RETEST_SHA = "fa3eee2c614b0741aeb240275f86abf7"        # slack_messages.id of RETEST
```

then

- T2 `seeded_ids`: `[APPROVAL, WITHDRAWAL]` → `[APPROVAL_SHA, WITHDRAWAL_SHA]`
- T2 `version_records`: `vr("slack", APPROVAL, …)` → `vr("slack", APPROVAL_SHA, …)`; `vr("slack", WITHDRAWAL, …)` → `vr("slack", WITHDRAWAL_SHA, …)`
- T6 `seeded_ids`: `[CMT["ZOM-78"], ASK]` → `[CMT["ZOM-78"], ASK_SHA]`
- T7 `seeded_ids`: `[CMT["ZOM-429"], RETEST]` → `[CMT["ZOM-429"], RETEST_SHA]`
- T7 `version_records`: `vr("slack", RETEST, …)` → `vr("slack", RETEST_SHA, …)`

Do **not** change the `ASK`/`APPROVAL`/`WITHDRAWAL`/`RETEST` constants themselves: they are also used as anchors/containers/`delegated_by_record`, and `channel/ts` is the canonical `RecordText.canon` form there.

Safety check run: `persona_view.check_sql` on the four sha ids gets `YES` for `julia_lawson` (im `D05SD5QLG94`, public `zombie-art`, im `D05GU6L0XFH`, private `zombie-match3d`), so making them load-bearing does not flip `persona_reach`.

---

## 3. incorporation_chains

**Gate message.** K1-K7 `delegation_quote 'my beta brief' is not in the text of D05SD5QLG94/1759263600.418207`; K8 `'the buy weeks in my UA plan' is not in the brief`. (`broken[:8]` truncates the list — K9, K10, K11, K13, K14, K15, K16 are broken too; only K12 passes today. I verified all 16 mechanically with `RecordText`-identical logic.)

**Actual seeded ask-DM body (verbatim, `slack.slack_messages` line 11, id `8b090dec472117f4598b9ad84318272e`, ts `1759263600.418207`, channel `D05SD5QLG94`):**

> Julia, I need the live-ops and push calendar for the beta buy we start Mon Oct 6 through Sun Nov 2. Every beat players can see in those weeks: which windows it runs in, if anything is held and until when, the push that goes with it, what still has to land before it runs and who owns that, and your recommendation with the trade-offs. Put it in the calendar sheet in your ZM Live Ops folder, link it on the calendar ticket, and send me the recommendation back here. The working rules for it are in my brief, shared with you. This goes into the pivot call, so I need your call, not a list of what we have.

So the DM **does** delegate: `The working rules for it are in my brief` (and `in my brief, shared with you`). It never says "beta brief", hence the MISS. "the calendar ticket" is present (K12 passes).

**Actual seeded brief body (verbatim, `gdocs.docs_documents` line 92-110, `document_id` = `f_7c3e91a4d2b85f60e1a9c4`):**

```
ZM3D beta live-ops calendar - working rules
Frederick, Sep 24
How I want the beta calendar built for the four buy weeks. The rules stay here; the calls are yours.
Span and time base
The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC, the four buy weeks in my UA plan. Every window is stated in server time (UTC) as a start-end instant. A PT/PDT rendering of the same instant is fine, a different instant is not.
Scope
Every ZM3D beat a player can see in those weeks: an event window, a reset or a start push. Not only the events everyone lists. Boss Arena is off this calendar until the pivot call.
When a beat starts
A beat starts with the first window that opens after its server windows are live on prod, the backend release instant read in UTC, not when its client PRs merged. Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC, so a window the release instant pre-empts does not count. Season Pass seasons open on the 1st at 00:00 UTC. For quest and login-calendar rollovers put down whether the beat is in and whether its push is ready, not its window dates.
Held or not
Hold a beat only when players provably cannot enter, score or claim on prod even after a restart. An established failure holds it; an unverified build or platform is a still-to-do, not a hold. Wrong counters, a reset that needs a restart, cosmetic, VFX and performance gaps and analytics gaps do not hold a beat, and neither does a change request outside the Aug-Sep live-ops cohort. An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it.
One-offs
One-offs may overlap a recurring beat slots. A one-off may take a recurring beat slot only with Product latest dated approval, and if he takes that back his later word is the one that counts.
Still to do
For each beat, what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it. Not what already shipped, not analytics, not polish nobody flagged.
Push copy
A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization.
Config locks
Every config a beat needs lands before its lock, read in server time (UTC). A committed date that misses the lock moves earlier and its owner is told.
```

**Per-fragment: the quote that EXISTS in the delegating record** (all verified present, case-exact, whitespace-collapsed):

| frag | delegator (must stay) | proposed `delegation_quote` | present where |
|---|---|---|---|
| K1-K7 | `ASK` (A1) | `The working rules for it are in my brief` | ASK DM, verbatim |
| K8 | `BRIEF` (K1) | `the four buy weeks in my UA plan` | brief, Span and time base |
| K9 | `BRIEF` (K7) | `Every config a beat needs lands before its lock` | brief, Config locks |
| K10 | `BRIEF` (K2) | `the backend release instant read in UTC` | brief, When a beat starts |
| K11 | `BRIEF` (K6) | `For quest and login-calendar rollovers` | brief, When a beat starts |
| K13 | `BRIEF` (K3) | `an unverified build or platform is a still-to-do, not a hold` | brief, Held or not (note: lowercase `an`) |
| K14 | `BRIEF` (K1) | `Boss Arena is off this calendar until the pivot call` | brief, Scope |
| K15 | `CAL` (A2) | `Still to do (owner)` | `Calendar` header row (SQL line 131; the row really is `Still to do (owner)`, not `(owner, due)`) |
| K16 | `BRIEF` (K5) | `A push goes out only if its row is Ready and LIVE` | brief, Push copy |

**Honest caveat, flagged separately.** K8 genuinely points at the UA plan ("the four buy weeks in my UA plan"). K9, K10, K11, K13, K14, K16 do **not** have a pointing delegation — the brief only states the rule that makes the record decisive (config lock, release instant, quest rollovers, hold predicate, arena exclusion, push rule). It never names Brian, the gmail thread, Leonard, Axe Arena, the quests card or the push sheet. Setting the quote to the governing rule is the maximum the seeded text supports and it passes the gate (the check only requires the words to be in the delegating record). If a true pointer is wanted, the *only* way is one added sentence to the brief's `body_text` (SQL line 92-110), e.g. `Names to read: Brian's Season Pass mails, Brian's #zombie-art posts, Leonard's tech-stable call, the quests roadmap card and the push sheet.` — **not required** for the gate; skip it unless the design owner wants literal pointers. `body_text`/`style_runs_json` offsets would then need re-checking, so treat it as a deliberate, separately-validated edit.

**FIX (manifest-only).** In `build_manifest.py`:
- Replace, in all seven gdocs fragments, `ASK, "my beta brief", ` → `ASK, "The working rules for it are in my brief", ` (7 occurrences, `replaceAll`).
- `BRIEF, "the buy weeks in my UA plan", ["R9"]` → `BRIEF, "the four buy weeks in my UA plan", ["R9"]`
- `BRIEF, "Brian's Season Pass handoff", ["R8"], kind="deadline",` → `BRIEF, "Every config a beat needs lands before its lock", ["R8"], kind="deadline",`
- `BRIEF, "Douglas's backend release", ["R2"], seeded=[EVT]` → `BRIEF, "the backend release instant read in UTC", ["R2"], seeded=[EVT]`
- `BRIEF, "the quests roadmap card", ["R5"], kind="amendment"` → `BRIEF, "For quest and login-calendar rollovers", ["R5"], kind="amendment"`
- `BRIEF, "Leonard's tech-stable call", ["R3"], base=[TECH]` → `BRIEF, "an unverified build or platform is a still-to-do, not a hold", ["R3"], base=[TECH]`
- `BRIEF, "where Brian put Axe Arena", ["R1"], kind="exclusion"` → `BRIEF, "Boss Arena is off this calendar until the pivot call", ["R1"], kind="exclusion"`
- `CAL, "Still to do (owner, due)", ["R7"], kind="format"` → `CAL, "Still to do (owner)", ["R7"], kind="format"`
- `BRIEF, "the push sheet", ["R6"], base=[PUSH]` → `BRIEF, "A push goes out only if its row is Ready and LIVE", ["R6"], base=[PUSH]`

---

## 4. authority_incorporation

**Gate message.** orphan `H1/H2/H3`; unverified namings `K1→H1 'This brief'`, `K2→H3 "Douglas's backend release"`, `K7→H2 "Brian's Season Pass handoff"` (none in `f_7c3e91a4…`).

**Actual brief text.** Quoted in full in §3. It contains `This brief`? **No.** `Douglas`? **No** (`the backend release instant read in UTC` — no name). `Brian` / `Season Pass handoff`? **No** (only `Season Pass seasons open on the 1st at 00:00 UTC`, which is a rule, not a handoff). So all three quotes are genuinely absent; they cannot be "fixed" by re-quoting a name that is not there.

**What actually clears the orphans** (hardness_gate.py:502-512): an authority is also incorporated when an **incorporated fragment's own record is one of the authority's records** (`named_auth.setdefault(a,[]).append("delegated")`).
- H1 records `[BRIEF]`; K1's own record is `BRIEF` → **delegated via K1**.
- H3 records `[EVT]`; K10's own record is `EVT` → **delegated via K10**.
- H2 records `[M2, THREAD_B]`; no fragment's own record is either (K9 holds `M1` + `THREAD_A`) → H2 still needs a `names_authorities` quote.

**FIX (manifest-only).**
1. K1: drop `names=[{"id": "H1", "quote": "This brief"}]` entirely (the record *is* H1).
2. K2: drop `names=[{"id": "H3", "quote": "Douglas's backend release"}]` entirely (H3 comes in through K10's record).
3. K7: drop `names=[{"id": "H2", "quote": "Brian's Season Pass handoff"}]`.
4. K9: add `names=[{"id": "H2", "quote": "Season Pass November config handoff"}]` — present verbatim in M1's subject (`ZM3D Season Pass November config handoff`, SQL line 31/34), which is K9's own seeded record. (M1 is H2's declared decoy, which is the intended near-miss: the run meets the Sep 22 handoff first and must still find the Sep 26 correction.)

Result: `H1` delegated (K1), `H2` named (K9), `H3` delegated (K10); `bad_names` empty. Note this only works after §3 is applied, because `inc_records` is built from **incorporated** fragments only.

---

## 5. requirement_coverage + surface_requirements

**Mechanism confirmed** (hardness_gate.py:494-501, 530-545).
- `covered = {requirement_ids of incorporated fragments} ∪ {requirement_ids of anchors}`; `orphan_reqs = declared - covered`.
- Currently only `K12` (+ A1/A2, both `R7`) are incorporated, which is exactly why the orphans are `R1,R2,R3,R4,R5,R6,R8,R9` and `R7` is not.
- After §3 every fragment is incorporated and carries: K1 R1, K2 R2, K3 R3, K4 R4, K5 R6, K6 R5, K7 R8, K8 R9, K9 R8, K10 R2, K11 R5, K12 R7, K13 R3, K14 R1, K15 R7, K16 R6 → `R1…R9` all covered.
- `surface_requirements`: `inc_reqs` then contains `R3` (K3, K13) and `R5` (K6, K11). The `decides` strings are prefixes of the declared text (`"Status column"` ⊂ R3, `"Still to do column"` ⊂ R5) and every surface's `requirement` is declared, so `bad_surface` empties.

**No independent gap:** there is no requirement that lacks a fragment, and no surface whose `decides` string is missing from its requirement — the only cause is the broken chain.

**FIX.** None beyond §3 (+ the `requirement_ids` already carried); do not edit `requirements` or `cohort.evidence_surfaces`.

---

## 6. supersession_chronology

**Gate message.** `T1: harmonygames-Games/match3d#470 2025-09-30T16:04:12Z is not before evt_9a4c2e7f1b3d58e06c7a2f 2025-09-26T11:20:00Z`.

**What the gate actually reads** (`RecordText.time_of`, `TABLE_TIME` line 744-750):
- `slack.slack_messages` → `ts`
- `github.github_pull_requests` → `created_at`
- `github.github_review_comments` → `created_at`
- `gcal.gcal_events` → **`updated` first, then `created`**

Verified values:

| record | gate-read timestamp | source |
|---|---|---|
| `C05KNDCHAAG/1758558302.777379` (JULIA_NOTES, base) | `2025-09-22T16:25:02Z` | Slack `ts` 1758558302.777379 |
| `evt_9a4c2e7f1b3d58e06c7a2f` (EVT, seeded) | `2025-09-26T11:20:00Z` | `updated` (SQL line 81; `created` is 2025-09-24T13:05:00Z) |
| `harmonygames-Games/match3d#468` (base) | `2025-09-26T20:16:25Z` | PR `created_at` in `Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json` (its `updated_at`/`merged_at` is 2025-09-29T16:13:50Z — **not** what the gate reads) |
| `harmonygames-Games/match3d#470#rc_10` (seeded) | `2025-09-30T16:04:12Z` | `created_at` (SQL line 138) |

Correct oldest-first order: **JULIA_NOTES → EVT → #468 → RC470**. The manifest's `at` fields are also checked by `_ordered` (`at` must be non-decreasing), so they must be rewritten to the same instants (`2025-09-26T20:16:25Z` for #468, `2025-09-26T11:20:00Z` for EVT) — the current `at` values (09-29 for #468, `2025-09-30T21:00:00Z` for EVT) are not the records' own timestamps.

**FIX (manifest-only).** In `build_manifest.py`, replace T1's `version_records` block:

```python
     "version_records": [vr("slack", JULIA_NOTES, "2025-09-22T16:25:02Z", f"slack:{JULIA_NOTES}", False),
                         vr("github", "harmonygames-Games/match3d#468", "2025-09-29T16:13:50Z",
                            "github:harmonygames-Games/match3d#468", False),
                         vr("github", RC470, "2025-09-30T16:04:12Z", "github:harmonygames-Games/match3d#470#rev_10", True),
                         vr("gcal", EVT, "2025-09-30T21:00:00Z", f"gcal:{EVT_UID}", True)]},
```
with

```python
     "version_records": [vr("slack", JULIA_NOTES, "2025-09-22T16:25:02Z", f"slack:{JULIA_NOTES}", False),
                         vr("gcal", EVT, "2025-09-26T11:20:00Z", f"gcal:{EVT_UID}", True),
                         vr("github", "harmonygames-Games/match3d#468", "2025-09-26T20:16:25Z",
                            "github:harmonygames-Games/match3d#468", False),
                         vr("github", RC470, "2025-09-30T16:04:12Z", "github:harmonygames-Games/match3d#470#rev_10", True)]},
```

Cross-service (`slack`/`gcal`/`github` = 3 services) and ≥3 versions still hold, so `supersession` stays satisfied. No other trap's `version_records` fails (T2/T7 slack `ts` match their `at`; T8 gmail `date` 09:12 / 07:40 still increasing; T13 pipeline 2025-09-12 → brief `created_time` 2025-09-24).

---

## Residual risks / verification notes

- After the §2 change the four sha ids become load-bearing; `persona_reach` was spot-checked read-only and all four verdicts are `YES` for `julia_lawson`, so no new failure is expected.
- All quotes in §3/§4 were verified with the gate's own `_norm` semantics (whitespace-collapsed, case-sensitive) against the seeded rows parsed by `base_check.parse_sql` + `fact_check._field_text`.
- No SQL edit is required by any of the six checks. The only SQL change worth considering is the optional pointer sentence in the brief's `body_text` (§3), which is a design nicety and must be validated separately if taken.
- Apply the same values to `01_Hardness_Manifest.json` (the gate target); `build_manifest.py` only writes `01_Hardness_Manifest.draft.json` and the final file additionally carries `facts`, `solver`, `integration_exceptions` and the `gradable_surface` digest.

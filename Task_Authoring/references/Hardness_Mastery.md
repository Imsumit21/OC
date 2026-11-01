# Hardness Mastery — how to build HarmonyGames tasks that strong agents fail

> **V3 use:** this is a historical technique/calibration library. V3 supersedes its
> older <75% score target, unique-answer rejection, duplicated-fact grading and
> prompt-style advice. Use assigned mode caps after fair regrading, accept all fair
> outcomes and never grade one fact in three or more rows. The existing user-set
> extreme/normal design targets remain unchanged (GEN_EXECUTION §3a). The assigned
> universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1,
> 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if
> the date is missing — there is no default. Compiled from the older Feb 14 export:
> reference-only for both universes until re-verified against the selected universe.
> Eval release `task-quality-v1` also fails trap hints and riddles, staged typos, hidden
> destinations the persona would know, audit-form wording and if-chains in the prompt;
> makes Overly Broad a Major rubric issue; and fails any rubric row an idle agent passes.
>
> **Opus 5.5 (Hardness v2, 2026-10-31).** The client's guideline `references/Docs/13_Hardness_v2_Opus55.md`
> (46 Opus 5.5 tasks under 75 %, 270 runs, 2,843 graded rows) is the current evidence for the baseline model and
> outranks the Opus 4.8 measurements below where they disagree. §13 maps its nine traps onto this library (new ids
> A24, A25), lists what no longer works, and states how its rules are reconciled with the local grading rails (§10).
> Run `tools/hardness_v2_check.py` for its self-checks.

The technique library behind `/create-scenario`, `/create-injection` and
`/create-hardening`. It ranks every known hardness technique by **measured** effect on
Opus-class agents, gives the build recipe in this universe, and pairs each with the QC
guard that keeps the task valid. Targets (user-set, `setup/GEN_EXECUTION.md` §3a):
**10–13 of 13 services carrying weight, ≥ 500 necessary agent tool calls, a long deep
injection, asks spread across many services while the human-typed prompt stays a short
trigger.**

Evidence tags: **[M]** measured on strong-model runs (number given) · **[P]** prescribed
by a guideline or reviewer, not isolated · **[X]** measured to NOT work.
Sources: `Evals/references/rules/{hardness_calibration,opus_failure_patterns,long_horizon}.md`
(R-HC, R-OFP, R-LH), `Evals/Docs/Original_Conference_Guidelines_Example_Task.pdf` (the ML-selected example task) (ML-selected task), the Sep-21 "How baseline
runs miss" guideline (GL-2§09), V0/V1 task audits and QMS review summary (31 reviews), V1
long-horizon guide (592-call example), V1 playbooks and the ML team's sub-75% list.

---

## 0 · The physics — read this first

**Opus clears anything that is only a retrieval or reading problem.** In the store-cut
RC-flag task (R-HC `…fea8d`) every "trap" was a search to issue, a file to open, a record
to read or a clause already held. Haiku failed all of them; six Opus 4.8 runs averaged
**95.5%** (four at 100%). Rules stated in one ticket over 12 named keys
(`enumerated_single_source`) are "a compliance checklist a strong model executes reliably
at any length."

**What transferred to Opus** — the only mechanisms with measured strong-model failure:

| # | Mechanism | Measured result |
|---|---|---|
| A1 | **Authoritative-but-wrong summary met first + a thread that continues past its apparent conclusion** | ML-selected Combo Fighters task: pass@1 **0/6**, best 18/31 (recorded as Opus 5.5, but the source doesn't establish the model: Phase 0–1 audit L5); both consequential findings inverted. Opus "found the data, computed it correctly, and then deferred to the most confident-sounding summary" and stopped reading at 21:08 of a thread that ran to 21:54 |
| A2 | **Scale completeness** — an exact predicate with exclusions held across a large cohort where per-record evidence is needed and no bulk call carries it | PR residue register (`…fea91`): 133 PRs × 4 surfaces ≈ 540 retrievals; Opus **306–949 calls**, avg **70.2%**, pass@1 **0/6**, 5 distinct signatures; **0/6** got the two derived totals right (42–46 vs 47; 77–82 vs 78) |
| A3 | **Tool-surface blind spot** — the obvious bulk call does not return the evidence (Slack channel history returns thread parents only; files live in replies) | Art-canon handoff: avg **44.1%** (author-reported). Floor ≈ 4,769 calls once measured on the tool surface |
| A4 | **Forensic chain of eliminating facts** — 4–6 facts, one per message/hop, each ruling out the obvious alternative, that a coherent write-up can silently drop | Marcus **47%**, Martin **52%**; their always-fail weight was 27% / 21%. Neutralising those facts alone lifts them to 74% / 73%. "With zero always-fail weight the average sits near 80% no matter how long the prompt is" |
| A5 | **Category-membership decoy** — several genuine candidates from the same owner, only one in the asked category | Task8 (Arthur's QA tool): **4/6** runs named a different genuine tool; pass@1 **0/6**; avg 202.8 calls over 9–11 services per run |
| A6 | **Sign-off traps + one built-in false positive** — bot approval, CHANGES_REQUESTED, "good to ship" chatter, merged without request; plus a record that truly matches | Task10: pass@1 **0/6** at ~82 calls |
| A7 | **Scope / alias boundary that survives full retrieval** | `win&collect` vs `CollectAndWinEnabled`: **2/6** Opus runs decided the alias did not bind |
| A8 | **Reuse-vs-duplicate write** — an existing record already tracks the work under a different title | Martin: DES-315 opened instead of reusing DES-313 — always-fail weight-5 |
| A9 | **Response pairing** — every dispute/question has a later reply from the other party that changes the answer | Vendor reply validating 1 of 3 charges: **4/5** runs missed it |
| A10 | **Exclusion settled within seconds** — "drop items the publisher opened and closed itself"; the second one was opened and closed 22 s apart | Runs dropped the obvious one, missed the second |
| A11 | **Retraction / failure-before-admission** | Martin (withdrawn 1.25× speed claim) and Marcus (revenue from a placement that should be off, hours before the admission) — weight-5 always-fails |

**Trajectory forensics — 131 baseline Opus 4.8 runs over 22 HarmonyGames tasks** (V0/V1
corpus, deduplicated; every run completed; median 132 calls, max 816; subagents made 55% of
all calls):

| # | Mechanism | Measured result |
|---|---|---|
| A12 | **Governing rule document in a rarely-searched service (Trello card, Docs handbook), plus a plausible decoy in a heavily-searched one** — the prompt names the rule, not where it lives | SB-T2 avg **0.21** (5/6 latched onto a Confluence decoy by call 16–24 and never searched Trello); SB-T3 **0.40**. SB-T1 **0.53** (handbook never opened 6/6) is **not valid A12 evidence**: its prompt never named the handbook, so the 9 all-fail rows built on it are unincorporated. Its clean average is ≈ 0.80 (§11). Hidden-authority tasks avg **0.48** vs **0.84** for the rest (computed before the SB-T1 correction) |
| A13 | **Evidence in a service the model rarely opens** | Services touched per run: Slack 125/131, Linear 118, GitHub 114, Docs 101 … **Gmail 60, Sheets 54, Trello 50, Snowflake 46, Slides 6, Calendar 5**. V0-T10: 0 Gmail calls in 6/6 → two rubrics failed 6/6 |
| A14 | **Replies never opened** | **67/124** Slack-using runs made zero thread-reply calls; **41/60** Gmail runs never opened a thread; pagination "more results" followed only **18%** of the time |
| A15 | **House rule that overrides the natural reading**, applied per record | V7-T1 PR #1081 (CHANGES_REQUESTED then APPROVED counts as a process finding): **5/6** runs wrong on 4 rubrics |
| A16 | **A source conflict the prompt asks to be reported** | V7-T1: **5/6** followed the runbook silently and failed the report rubric |
| A17 | **Cohort-boundary traps** (a later-added child, an unticketed lookalike, a stale shorter list) | FE-6a7e: **23/30** runs reported "19 of 27" instead of "20 of 28" |
| A18 | **Needles topical search cannot reach** | V0-T11: three tickets never appeared in any of 6 runs; V0-T6 ZOM-301 never retrieved |
| A19 | **Retrieved but never computed** — the deliverable needs a derived comparison from structured rows | V0-T4: rows retrieved 5/6, comparison missing **6/6** |
| A20 | **Subagent synthesis loss** — a fact surfaces only inside a subagent's large result and never reaches the deliverable | V0-T1 (6/6), V0-T8 (4/6); subagent-using runs scored lower on V7-T1 (0.65 vs 0.85, small n) |
| A21 | **Per-surface format/redaction rules in an incorporated source** | SB-T1: schema rubrics failed 6/6; forbidden Jenkins IDs in the email 6/6 |

**Volume is not difficulty.** A 116-PR mechanical sweep with explicit rules in a named place
ran **659–816 calls and scored 0.984**; another ran up to 587 calls at 0.928. Within a task
the call count barely predicts score (r = −0.11). Volume only matters when a cohort mandate
forces it — **without one, the main agent plateaus at ~50–100 calls**. So: the cohort mandate
buys the 500+ calls; the A-mechanisms buy the failures. Never confuse the two.

**The bimodality trap.** When one hidden control gates most rubrics (A12), runs split into
near-zero and near-perfect (SB-T2: 2, 4, 3, 2, **54**, 2 of 54). That fails QC: the failing
runs share one signature (concentration > 50%) and the per-rollout spread leaves the SD band.
Use **several independent hidden authorities**, each governing a different subset of outputs,
in different rarely-searched services — runs then miss different ones.

**What did not work** (§9 has the full list): mechanical cohorts with explicit rules in a
named location (0.984 at 659–816 calls) [X]; forced errors and async waits — every run
routed around them [X]; drafts marked RETIRED — always ignored correctly [X]; long prompts
(ρ = +0.21 with score) and many rubrics [X]; ACL scoping — no real denials observed [X];
rules applied once, even conditional or
seniority rules (Opus 6/6) [X]; a verbatim supersession "ignore leonard on the cohort"
(6/6) [X]; one binary trick (80.5%) [X]; off-by-one counting as the engine (77%) [X];
piles of existence/format rubrics (79.5%) [X]; hiding evidence, ACL-only difficulty,
vaguer asks, extra deliverables, padding [X]; a 540-call plan that a code-content search
collapsed to 94 calls [X].

**Calibrated against `/hardness` (§11).** A blind 1A read of one run matched the observed outcome on 3 of 4 V1 tasks. The misses taught three things:
- Read write payloads, not narration.
- A band-4 run can sit beside an average above 75% when little weight depends on the mechanisms.
- Raw verifier averages overstate hardness when all-fail rows rest on unincorporated rules or verifier errors.

The mechanisms that produced genuine Opus failures in the calibration set were A15, A16, A17, per-record findings on records whose state is already correct, and partial resolution read from code. Retrieval traps, decoys and authorities that every run reached leaked.

**Design rule.** Build the task's core out of A1–A21. Use retrieval-shaped traps (first-hit
search, unopened file, page limits) only as **call multipliers** layered on top, never as
the reason the task is hard — except A12–A14, where the evidence shows Opus genuinely does
not look (rarely-searched services, replies, threads).

**The evidence-backed recipe** (B-forensics + calibration): a source-defined cohort of
60–150 records × 3–6 per-record checks (or one dependent write each) → the 500+ calls ·
classification rules held in **2–4 independent authorities** in rarely-searched services,
each with a decoy in a frequently-searched one and a stale/partial version · exact-count and
per-surface-output criteria · one or more decisive facts only in Gmail threads, Calendar
events, Slides, Sheets tabs or Slack replies · a house rule that overrides the natural
reading, applied per record · a reported conflict · boundary records at the cohort edge.

**Update, Oct 25 (§12).** The recipe holds only while the authorities are named by role and found by search. When
Season Pass's hub named every source, Opus 4.8 read them all and every family leaked.

---

## 1 · Blueprint of an extreme task

```
                prompt (4–6 human-typed sentences, names a deadline and 1–3 anchors)
                                   │ incorporates
                 ┌─────────────────┴─────────────────┐
              HUB record(s)  (owner's voice; explicitly delegates)        ← §3 delegation lattice
       ┌──────────┬──────────┬────────────┬──────────┬──────────┐
     spoke      spoke      spoke        spoke      spoke     amendment (later, other service)
   (Confluence)(Linear)  (Drive doc)   (Trello)   (GCal)       supersedes part of a spoke
       │                                                       
   COHORT SPINE: source-defined set of 40–150 records × 3–6 evidence surfaces each   ← §2
       │      (per-record evidence lives in ≥ 3 services; no bulk call carries it)
       ├── Chain 1 → eliminating fact (weight 5)    ┐
       ├── Chain 2 → eliminating fact (weight 5)    │ ≥ 3 INDEPENDENT forensic chains   ← §4
       ├── Chain 3 → eliminating fact (weight 5)    │ each with its own A-family trap
       └── Chain 4 → reuse-vs-duplicate write       ┘
   DELIVERABLES: one register/record (exact totals) + 3–6 dependent writes (≥ 3 services)
```

Every one of the 13 services holds at least one **load-bearing** fact, rule or write on
this structure (§5). Name-dropped services do not count (FM17-18).

### 1.1 Sizing to ≥ 500 necessary calls

```
necessary calls ≈ discovery (find hub, spokes, amendments, cohort definition)      40–80
               + rules reading (hub, spokes, amendment, Confluence versions)          15–30
               + cohort enumeration (paginated listings across services)              10–40
               + records × surfaces (the spine)                                     300–600
               + chain reconciliation reads (Snowflake, Sheets tabs, Gmail threads)   40–100
               + reads-before-writes (contacts, IDs, channels)                        15–30
               + writes + read-back                                                  10–30
```

The gate floor is **≥ 500** necessary calls (≥ 300 of them per-record); plan **~600** so the
rollout average still lands near 500 (rollouts that stop early pull it down). §2.5 shows how
to get there without padding. The 592-call reference: 116 PRs × 5 GitHub surfaces = 580 + 12.
`fea91`: 133 × 4 ≈ 540 → observed 306–949.

**The golden-run trap.** If any rollout scores 100%, its own call count is the horizon
measure. Volume must therefore be **unavoidable for correct runs**, not just for confused
ones. Prove it with the shortcut audit (§2.3).

> **QC note (state it to the requester).** QC Spec V2 counts tiers as Normal 50–100,
> Long-Horizon 100–500+ (Super-Long is paused). A Normal-tier task with 500+ calls is
> **Non-fail "Borderline Horizon" (score 3)**, which caps the overall task score at 3. A
> Long-Horizon task at 500+ is inside its tier (the FM27 linter only warns). Very long runs
> also risk errored rollouts (3+ errored = Fail): `fea91`'s runs took 17–38 minutes and all
> completed.

---

## 2 · The cohort spine (A2, A3) — the 500-call engine

### 2.1 Choose the cohort

A **source-defined** set the agent must reconstruct — never listed in the prompt:
- PRs/commits in a window and branch set (GitHub), tickets in states/labels (Linear),
  cards on lists (Trello), vendor invoices (Gmail attachments + Sheets ledger), calendar
  decisions (GCal), daily rows (Snowflake), Slack thread roots in channels, Confluence
  pages under a parent, Drive files in a folder.
- Size 40–150. The membership rule lives in an incorporated source and is **amended**
  later in another service (a partial supersession: one clause changes, others stand).
- Add a **dual regime**: records before an effective date follow rule v1, records after
  follow v2 (effective-date supersession). The agent must classify each record under the
  regime in force on that record's date. [P; combines A2 + S9]

### 2.2 Choose the evidence surfaces (3–6 per record, ≥ 2 services)

Each surface must be **separately exposed by the tools** and must change the record's
classification. Candidates (verify against `references/Ask_Carriers.md`):

| Service | Per-record surface the bulk view does not carry (● = base precedent) | Bulk shortcut to neutralise |
|---|---|---|
| GitHub | ● reviews (state + body); ● review comments; ● PR conversation comments; ● commits; ● timeline events; files — 5–7 calls per PR | `github_search_code` / `search_pull_requests` content matches (Task9: 540 → 94 calls) |
| Linear | ● description (truncated by `maxDescriptionChars`); ● attachments keyed by identifier; ● relations/parent; ○ comments (0 in base — confirm rendering first) | `linear_show_data` [U] |
| Slack | ● thread replies — channel history returns parents only (A3, A14); ● files posted in replies; reactions | filtered `slack_conversations_search_messages` may return replies [U] |
| Gmail | ● full thread (`get_thread`, later replies, quoted history); ● attachments; one copy per mailbox | `gmail_get_messages_batch` |
| Trello | ● card comments (`commentCard` actions); ● `updateCard` history (old/new); ● check items | `trello_get_checklists_on_board` |
| Confluence | ● version history + per-version bodies + edit messages; ● comments; labels | `confluence_get_page_diff` v1→vN |
| GCal | ● attendees + response status; ● start/end, status (cancelled), rrule; ○ description (absent in all base events) | `gcal_list_events` over a wide window |
| Sheets | ● the specific tab's grid — spread facts across **different spreadsheets**, not tabs of one | `gsheets_values_batch_get`, `get_spreadsheet(includeGridData)` |
| Snowflake | ● day-level rows; ● table/column comments via describe — weak call generator (one GROUP BY collapses it); value is that figures must be *derived* | GROUP BY |
| Docs | ● body text, headings | — (one read per doc) |
| Slides | ● element text; ○ speaker notes | `gslides_get_presentation_text` |
| Drive | ● metadata (owner, sharing, modified), folder path; ○ `content_text` (base content is on disk — injected text may not render) | — |
| Contacts | ● job, email — cheap; not a call generator | `contacts_show_data` |

Put load-bearing facts only in ● carriers; confirm any ○ carrier renders in the Opus
pre-check before a criterion depends on it (`references/Ask_Carriers.md` §5, §7).

### 2.3 Shortcut audit (mandatory, against the tool surface — not the archive)

For every surface ask: **is there one call that returns every predicate-relevant field for
every record?** If yes, the agent will use it and the volume collapses (Task9: 540 → 94
calls via `github_search_code`). Check `Evals/references/tools/catalog.json` for:
content/code search, bulk list endpoints with embedded fields, `get_many`-style calls, a
Snowflake table that already joins the evidence, a Sheet that already summarises it, a
Confluence page that already lists it. Remove the shortcut from the design (move the
evidence to a surface that needs per-record reads) or count it in the budget honestly.
Never rely on a tool being broken ("contingently long-horizon").

### 2.4 Exact predicate with exclusions (A2)

The classification rule is a short, literal, owner-voiced predicate in an incorporated
source: closed vocabulary, whole-word matching, stated exclusions, "NONE stands alone",
cutoff per line. Derived totals (counts per class, per group, combined) are exact and
reconcile with the register. One misread record changes a graded total. Keep every edge
decidable (UGT): if two clauses can bear on one record, the source says which wins.

### 2.5 Reaching 500+ necessary calls honestly (sample-task finding, Oct 4)

A base-data cohort usually yields only 1–2 honest calls per record: list endpoints already
carry most fields (`linear_list_issues` returns state/labels/assignee; PR search returns
titles). The first engine test reached 321 necessary calls with 75 records × 3 surfaces and
refused to pad. The fix is **per-record evidence the injection seeds into no-bulk surfaces** —
which is also what makes the injection long and deep.

**No-bulk per-record reads in the catalog** (one call per record, no list/batch alternative):

**Verified tool behaviour (Oct 4, from ~6,000 recorded calls in 277 V1 Opus trajectories in the V1 task corpus):**

| Surface | Per-record? | Evidence |
|---|---|---|
| **Linear issue comments** — `linear_list_comments(issueId)` | **Yes — verified.** `linear_list_issues` items carry no comments (fields: id, parent_id, relations, links, labels, description, state_history …); injected comments render (8 non-empty returns of a V1-injected comment on ENG-2401) | strongest per-record surface; seed `linear.linear_comments` |
| GitHub PR conversation comments — `github_get_pull_request_comments(pullNumber)` | **Not per-record for the main repos.** PR search matches comments via the `in:comments` qualifier (verified Oct 5; unqualified queries match title/body/branch only), **and the GitHub Slack app mirrors every PR comment and review, text included, into Slack**: GameOfDominoes + game-of-dominoes-backend → `#engineering-bots` `C050WGU41HR`; match3d → `#zombie-prs` `C093LEZGF6J` (~2,000 copies in 2025; e.g. `C093LEZGF6J/2025-10.json` /271 mirrors match3d#486 "Not ready for merge"). A Slack sweep of those channels (~50 per page) replaces the per-PR reads | a seeded PR comment or review in a mirrored repo **must** also get its Slack copy (coherence); treat the pair as trap evidence, not volume |
| Confluence page comments — `confluence_list_comments(page_id)` | Yes (per page) | small cohorts only |
| **Slack thread replies** | **No — sweepable.** `slack_conversations_search_messages` returns replies (596 of 2,663 results had `thread_ts ≠ ts`), and filter-only searches (author + channel, no query text) page through everything at 50 per call with a cursor | keep replies for the A14 *behavioural* trap (most Opus runs never read them), never as budgeted per-record volume |
| Linear parent / relations / links | **No** — in `linear_list_issues` | do not budget `linear_get_issue` for them |
| Linear description | **No** — list returns it (truncated flag + `maxDescriptionChars`) | weak |
| Trello card comments, Gmail threads, Sheets tabs, Calendar events | No — board actions, batch get, batch values, list over a window | weak |

So at scale the honest per-record engine is **Linear comments, one call per issue** — the
only surface with no bulk or mirror path (Confluence comments work for page cohorts of ≤ 31). Large tool results spill to files the agent
must read in chunks (`exceeds maximum allowed tokens … saved to …`) — real friction, but not
per-record volume.

Weak (bulk exists — count them at 0.2–0.5 per record, or not at all): Trello card comments
(`trello_get_board_actions` with a comment filter), Gmail threads (`gmail_get_messages_batch`),
Sheets tabs (`gsheets_values_batch_get`), Calendar events (`gcal_list_events` over a window).

**Necessity rule (passes the Evals anti-inflation check).** A seeded per-record surface counts
only if (a) it carries a fact the classification predicate uses, (b) that fact is decisive for
an **unpredictable subset** of the cohort (≈ 15–40 % of records flip; the rest carry a
neutral or confirming note), and (c) nothing upstream tells the agent which records flip. Then
every record must be read — a run that samples or skips is wrong on the flipped ones it missed.
A note on every record that never changes anything is padding; one note on only the flipped
records is a tell (their existence alone flags them) — seed both kinds. The same tell works
at cohort level: where the base has no records of a kind (Linear comments), notes only on
cohort members reveal the cohort — seed the trail on a **differently defined list** (sample-task:
the testers' list includes two non-cohort tickets and misses six cohort ones). Keep the rule's
vocabulary out of the evidence wording (a rule saying "could not make it happen" and replies
saying "happens" lets one search pull the flips).

Budget rows whose necessity depends on an unverified tool behaviour (does PR search index
comments? does the list call return `parent`?) carry `conditional_on: "<behaviour>"`; the gate
reports the floor if those resolve to bulk. Resolve them in the Opus pre-check.

**Patterns that reach 500+**
1. **Issue spine — the sizing rule (measured, sample_task_01 iterations 3–5).** With verified tool
   behaviour, honest necessary calls ≈ **~50–110 fixed** (discovery, rules, enumeration pages,
   Slack sweeps of the PR-mirror channels, writes) **+ 1 per cohort issue** (its Linear
   comments). PR comments do not add per-record volume (mirrored to Slack). So **≥ 500 needs
   ≈ 400–450 cohort issues**, each with an output-visible fact that lives only in its Linear
   comments (decisive for an unpredictable 15–40 %, neutral notes on the rest, notes also on
   non-cohort issues so having a note reveals nothing). Linear then carries most of the budget —
   the gate's share cap does not apply to the per-record phase. Populations: ENG/ZOM issues
   updated since 2025-08-13 = 374, since 2025-07-01 ≈ 390 incl. open bugs; a 73-issue cohort
   tops out near **135** honest calls (sample_task_01 after the mirror finding).
2. **Two linked cohorts.** Records × their fix PRs (each PR: comments + timeline) — the second
   cohort is reached only through the first.
3. **PR cohorts are allowed** when the selection rule, the surfaces and the vocabulary differ
   from the calibration register (`fea91`: merged-PR residue × reviews/commits/flags). A PR
   cohort selected by a Linear/Slack-defined set and judged on conversation comments + timeline
   events + the linked ticket is a different task.
4. **Effective-date regimes** (S11) double the reading per record without adding records: the
   agent must find which rule version applied on each record's date.

**Realism of a seeded trail.** Hundreds of seeded comments need plausible authors and rates:
spread them over the people who actually own the records (each engineer on their own tickets,
QA on retests), only people active at the clock, at a human pace (tens per person per day, not
hundreds), across several days, timed after each record's own events. A trail written entirely
by the persona in one sitting reads as contrived (sample_task_02: 504 notes by Arthur in ~16 h).

Record each surface in the manifest with `records` (how many cohort records it applies to)
and `per_record_calls`; the gate sums `per_record_calls × records` (≥ 300 for extreme).

### 2.6 Red-team lessons that kill "necessary" calls (Red-team review of sample_task_01, Oct 4)

A design that passes the gate can still be cheap for a strong agent. Check each of these
before claiming a per-record call is necessary:

1. **Logical short-circuit.** An AND/OR predicate lets the agent skip the second surface
   whenever the first already decides the record (both platforms must be negative → read
   Android only when iOS is negative). Make **every surface independently consequential**: its
   value appears in the deliverable per record (a per-platform column, a per-source status) or
   changes the outcome whatever the other surfaces say. Write the skip analysis per surface
   (`short_circuit` in the manifest).
2. **Metadata sweep.** One filtered search (author + channel + date, a label, a board) pages
   through every message in a container regardless of wording — **verified for Slack, replies
   included**. Slack therefore never carries budgeted per-record volume; put per-record facts in
   Linear comments and PR conversation comments (no bulk path, verified), homed on each record.
3. **Breadcrumbs that land directly.** If the hub names each authority by a unique title term,
   one search returns it. Name the authority by **what it governs or who issued it**, and give
   the decoy the same search terms, so a search returns both and the agent must choose by
   authority/date — that is the A12 mechanism. Findability for fairness still holds: the right
   one is reachable and decidable.
4. **Self-advertising decoys.** "draft", "old", "Jan", "placeholder", "superseded", a stale
   date in the file name — the agent discards them for free. Decoys and superseded versions
   must look current and same-purpose; what makes them lose is a precise, incorporated rule
   (newer accepted amendment, issuer authority, scope clause), not a label.
5. **Stated conclusions.** A seeded message that states the chain's answer ("X never shipped")
   lets the agent jump to the end. No record may state a chain's conclusion; the agent must join
   facts (merged scope vs ticket scope, build vs merge time, component vs platform).
6. **One decision table defeats many traps.** Several traps that fall to the same rule are one
   trap. Count a trap only if an agent that has defeated all the others can still fail it, and
   keep any single authority from governing most outputs (failure-pattern concentration).
7. **Temporal and aggregation rules must be explicit.** Multiple fixes per ticket (which merge
   counts: any or latest applicable?), folded/parent records (how statuses aggregate), the build
   or snapshot a check refers to, and what "current" means at the clock — each needs an
   incorporated rule, or the task has two right answers (UGT).
8. **Write end states and permissions.** Every write needs its required end state stated in an
   incorporated record (ticket state, sheet tabs, slide text scope), a target the persona can
   **edit** (shared as writer or owned — read access is not write access), a catalog tool that
   can produce it (e.g. multi-tab sheet creation), and, for an external recipient, an access path
   that the instructions authorize.
9. **Chronology of references.** A record that refers to another ("the tiers I put on the
   board") must postdate it. Check every cross-reference timestamp.
10. **Budget arithmetic.** Do not charge discovery of a uniquely named record more than ~2 calls,
    re-reads of already-fetched records, or pagination you could avoid; count read-backs as
    verification, not hardness. The golden-run horizon is measured, never derived from the
    manifest.
11. **Unwired delegation.** A requirement whose source no record points to is unauthorized, however
    the manifest labels it — and every call it drives disappears (sample_task_02: 424 of 565). Each
    fragment names the record carrying the delegating words (`delegated_by_record`).
12. **Per-record answers in prose.** A per-record note that states the classification ("still in
    the current build", "kept out of every build") makes the volume transcription. Per-record
    facts should be raw events (a build id, a deploy or flag event, a commit ref) that the agent
    must join against an authoritative history to classify — and the rule must settle the
    semantic edge (binary shipped vs feature enabled; per-platform vs first-platform date).
13. **Cross-service decoys only catch the first look.** A decoy where Opus looks first (A12:
    Confluence/Slack) catches runs that latch early, but a service-specific search for the
    authority never returns it. Use both: at least one authority also has a **same-service**
    decoy with an adjacent scope (another lot, another issuer, an earlier effective date), so a
    targeted search must still choose.
14. **Numbers come from the generator.** Every total in the dossier and "Facts for the human" is
    emitted by the ground-truth script from the records; hand-typed totals drift (the red team found
    33 vs 34 and 12 vs 13 in sample_task_02).

### Mechanism id enum (`chains[].root_cause`)

`hardness_gate.py` (`MECHANISM_IDS`) accepts exactly these ids as a chain's `root_cause` — the bare id, nothing
else. Distinct root causes are distinct ids: two chains with the same id count once (harness red team A, R2 #6).

| Id | Mechanism | Id | Mechanism |
|---|---|---|---|
| `A1` | authoritative-but-wrong summary met first | `A12` | governing rule in a rarely-searched service + decoy |
| `A2` | scale completeness over a cohort | `A13` | evidence in a rarely-opened service |
| `A3` | tool-surface blind spot | `A14` | replies never opened |
| `A4` | forensic chain of eliminating facts | `A15` | house rule overriding the natural reading |
| `A5` | category-membership decoy | `A16` | source conflict the prompt asks to report |
| `A6` | sign-off traps + one true match | `A17` | cohort-boundary traps |
| `A7` | scope / alias boundary | `A18` | needles topical search cannot reach |
| `A8` | reuse-vs-duplicate write | `A19` | retrieved but never computed |
| `A9` | response pairing | `A20` | subagent synthesis loss |
| `A10` | exclusion settled within seconds | `A21` | per-surface format/redaction rules |
| `A11` | retraction / failure-before-admission | | |
| `A24` | done across services: a done source plus a missing piece in another service (v2 trap 1) | `A25` | completion elsewhere: work already done, recorded away from the request (v2 trap 9) |
| `2.6.1` | logical short-circuit (independently consequential surfaces) | `2.6.8` | write end states and permissions |
| `2.6.2` | metadata sweep | `2.6.9` | chronology of references |
| `2.6.3` | breadcrumbs that land directly | `2.6.10` | budget arithmetic |
| `2.6.4` | self-advertising decoys | `2.6.11` | unwired delegation |
| `2.6.5` | stated conclusions | `2.6.12` | per-record answers in prose |
| `2.6.6` | one decision table defeats many traps | `2.6.13` | same-service decoy with adjacent scope |
| `2.6.7` | explicit temporal and aggregation rules | `2.6.14` | numbers come from the generator |

---

## 3 · The delegation lattice — spreading asks across 10+ services legally

`prompt-incorporation-v1` (Evals/WORKFLOW.md): a requirement counts only if the prompt
directs the agent to a uniquely identifiable source, **or that source explicitly delegates**
to another. A merely related record adds nothing; an unmentioned handbook adds nothing;
criteria built on unincorporated rules are **Incorrect (Major)**. Later applicable updates
for the same scope supersede earlier ones without announcing it.

**Structure**
1. **Anchors (1–3)** — named in the prompt in plain words: "robert's handoff list", "what
   arthur asked for in his email", "the wind-down page".
2. **Hub** — the anchor record, in the owner's voice, explicitly delegating:
   "cohort rules are on the OPS page", "julia's acceptance notes are on the card", "finance
   wants the totals in the board-pack tab", "copy whoever owns each vendor (contacts)".
3. **Spokes (≥ 10 fragments, ≥ 7 services, ≥ 10 distinct containers)** — each carries one
   requirement: a rule clause, a destination, a recipient subset, a format convention, a
   deadline, an exclusion, a reuse instruction. A destination the persona would know goes
   in the prompt; a spoke may carry it only when finding it is part of the task and the
   record is persona-visible (`Evals/1_Prompt_Eval.md`, hidden-destination rule). An
   exclusion is graded as an exact count or scope on a required write, never as a
   "leaves X as found" row (`Evals/3_Rubrics_Eval.md` §2.9 do-nothing test).
4. **Amendments** — later records in a *different* service that change one clause of one
   spoke (Gmail from the hub owner, a Slack thread reply, a GCal reschedule, a Confluence
   v3). Retain unaffected clauses.
5. **Non-authoritative instruction distractors** — instruction-shaped messages that are NOT
   in the chain (another persona's checklist, a suggestion from someone without authority,
   the same rule for another title). Ignoring them is correct; never grade their mention.

**Carriers by service** (full skeletons in `references/Ask_Carriers.md`): Slack pinned
message / thread reply / DM · Gmail thread from an exec or partner · GCal event description
· Drive folder description or file comment · Docs section · Sheets "notes" tab or a cell
range · Slides speaker notes · Contacts job/description (ownership) · GitHub issue, PR
description or review comment · Linear issue description or comment · Trello card
description / checklist / comment · Confluence page (+ version) or comment · Snowflake (a
config/requests table row, only if a discoverable pointer names it).

**Hidden authorities (A12) — the strongest measured lever, used safely**
- The prompt (or the hub) **names** each governing source unambiguously — "the merge review
  control", "the closeout rules he mailed me", "julia's acceptance notes" — but never says
  where it lives. Under `prompt-incorporation-v1` that is valid incorporation when the name
  leads to **one uniquely discoverable** source through the tools.
- Home each authority in a rarely-searched service (Trello card, Docs handbook, Gmail
  thread, Calendar event, a Slides deck) and place a **plausible decoy** where Opus looks
  first (a Confluence page or Slack thread with a near-matching rule, sounding complete).
- Use **2–4 independent authorities**, each governing a *different* subset of the outputs
  (cohort rule · classification rule · destination/format rule · recipient rule). A run that
  misses one still scores on the others, so failing runs differ (≥ 2 patterns, none > 50%)
  and per-rollout scores spread (SD 0.1–0.3). One authority gating everything produces the
  bimodal 0-or-100 split that fails QC concentration.
- Make each authority findable by a natural search for its own name (proven by
  `hg_search`), and make the decoy *non-equivalent* (it differs on a decisive clause), so the
  task stays fair: a careful run that searches for the named rule finds it.

**Hardness levers inside the lattice**
- Put the rule where the first-read thread does not restate it ("standing rules sit
  further up that channel and the freeze thread never restates them").
- Make one spoke's clause depend on a fact from another service ("anything over the
  threshold in the finance tab needs a second approver" — threshold in Sheets, approver in
  Contacts, approval state in Linear).
- Give two recipients different entitled subsets (cross-recipient boundary, ML5) and one
  internal-only rule (ML4) — graded affirmatively.
- Make at least one amendment arrive *after* an apparent conclusion (A1).

Record every fragment's chain back to the prompt in the manifest (`incorporated_via`).
`tools/hardness_gate.py` fails any fragment whose chain does not end at an anchor.

---

## 4 · Independent forensic chains (A1, A4–A11) — failure diversity

QC needs ≥ 2 distinct failure patterns and no pattern > 50% of failing rollouts. One
cascade from one choke point fails that. Build **≥ 3 chains with different root causes**,
each ending in a weight-5 fact the deliverable must carry:

| Chain type | Built from | Ends in |
|---|---|---|
| Wrong-summary chain | A1: senior summary met first; overturning evidence in a structured system and in a thread past its apparent end | the corrected state of a central fact |
| Eliminating-evidence chain | A4: 4–6 facts, one per message/hop, each ruling out an alternative | the surviving explanation, with the decisive facts |
| Category chain | A5: genuine candidates from one owner; only one in the category | the right member, by name |
| Sign-off chain | A6: bot approval, CHANGES_REQUESTED, chatter, merged-without-request, plus a true match | the correct approval classification per record |
| Scope chain | A7: an alias or adjacent scope that may or may not bind; the incorporated text decides | in/out-of-scope decision |
| Reuse chain | A8: an existing record tracks the work under another title | update the existing record, not a new one |
| Dispute chain | A9/A10: complaint + the other party's later reply; open-and-closed-by-itself items | the validated subset |
| Retraction chain | A11: a claim later withdrawn, or a failure visible before the admission | the true state and when it surfaced |
| Hidden-authority chain | A12: the named rule lives in Trello/Docs/Gmail; a near-matching decoy sits in Confluence/Slack | outputs the authority requires (titles, tabs, structure) |
| Rarely-opened-service chain | A13: the decisive fact only in a Gmail thread, a Calendar event, a Slides deck or a separate Sheet | the fact, carried into the deliverable |
| Reply chain | A14: the decision lives in a Slack thread reply or a later Gmail message | the replied state, not the parent's |
| House-rule chain | A15: a rule that overrides the natural reading, applied per record | per-record classifications + totals |
| Conflict-report chain | A16: two incorporated sources disagree; the prompt asks to flag conflicts | the reported conflict and the governing value |
| Boundary chain | A17: later-added member, unticketed lookalike, stale shorter list | the exact cohort and its count |
| Derivation chain | A19: rows must be aggregated/compared, not read | the derived figure |

Place each chain's evidence in **different services** and make the chains share the
cohort (so they are on one subject — no bolt-ons) but not a root cause.

---

## 5 · The 13-service role map

Each service must hold something the correct answer **cannot do without**.

| Service | Opus opens it (of 131 runs) | Typical load-bearing role | Best traps here |
|---|---|---|---|
| Slack | 125 | decisions, the wrong summary, **thread-reply** evidence, the decoy rule | A1, A3, A14, S1, D4 |
| Linear | 118 | work-of-record, duplicates, follow-up destination | A8, A17, A18, CS3 (no PR link) |
| GitHub | 114 | what shipped: reviews, commits, timeline | A2 surfaces, A6, A15 |
| Docs | 101 | specs, handbooks, meeting notes — a hidden authority home | A12, A21 |
| Drive | 91 | destination folder convention, ownership/sharing, revision dates | UGT destination, D9 |
| Confluence | 79 | versioned conventions; the decoy page Opus latches onto | D4 decoy, S12 |
| **Gmail** | **60** | external confirmations, invoices, disputes + replies, exec asks | A9, A10, A13 |
| **Sheets** | **54** | trackers with stale vs current versions (separate files), the register | D4, S9 |
| **Trello** | **50** | **hidden control / checklist** (A12's strongest home), drifted roadmap | A12, D9 |
| **Snowflake** | **46** | figures that must be derived; table comments that contradict rows | A19, D10 |
| **Slides** | **6** | the stale deck summary; the one place a decisive figure was presented | A13, D4 |
| **Calendar** | **5** | when a decision was taken, who attended (authority), cancellations | A13, S9, authority |
| Contacts | (identity lookups) | owner/role resolution for recipients | D5, ML5 |

Bold rows are where Opus rarely looks — the best homes for decisive facts and hidden
authorities. Pair each with a reason-to-look in the delegation lattice (§3) so the
requirement stays incorporated. Confluence and Snowflake are live and unscoped per the
current Evals (`acl.md`, `service-availability-v1`) and listed in the current agent system
prompt (the V1-era prompt omitted them); agents still open them rarely, so give every
dependence on them a natural pointer from another record. A
Snowflake insert must keep the mirrored warehouse tables in step (`01_Universe_Injection.md`
§S4); prefer existing warehouse rows as the evidence that overturns a claim over a seeded
load-bearing row.

---

## 6 · Technique library

Format: **Mech** (weakness exploited) · **Build** · **Evidence** · **Guard**.

### 6.1 Distractors
| ID | Technique | Build | Ev. | Guard |
|---|---|---|---|---|
| D1 | Keyword collision | same search term, same field, near-identical record; the deciding difference buried | P | decisively outranked by primary evidence; grade the correct value only |
| D2 | Multi-source near-duplicate | same fact in Slack/Gmail/Linear with one detail changed; one matches the system of record | P | list as intended disagreement; one source decisive |
| D3 | Chained decoys | decoy at hop 1 leads to decoy at hop 2 | P | pair with independent chains (signature spread) |
| D4 | Authoritative-but-wrong summary | newest, most senior, addressed to the persona, two claims wrong in opposite directions | **M** (A1) | prompt invites the check, never asserts the wrong claim; character being wrong ≠ truthfulness defect |
| D5 | Lookalike entity | three Marcuses + Oscar Bennett; "Thomas" vs Thomas Baker; ENG-#### vs ZOM-###; per-title channels | P | pin exact IDs/emails; never build UGT on redacted tokens |
| D6 | Category-membership | genuine siblings of one owner, only one in category | **M** (A5) | boundary decidable from evidence a careful reader accepts |
| D7 | Built-in false positive | one record that truly matches in a mismatch audit | **M** (A6) | grade the correct classification affirmatively |
| D8 | Sign-off traps | CodeRabbit APPROVED, CHANGES_REQUESTED, chatter, merged-without-request; rule "only APPROVED counts" incorporated | **M** (A6) | every rule edge resolved in the text (a 3–3 split failed UGT) |
| D9 | Stale lookalike artifacts | `Copy of`, `(2)`, `vX.Y`, drafts, archived/Canceled tickets, another partner's term sheet | P | document intended dual naming |
| D10 | Narrative caveat vs rows | Snowflake table comment / Confluence prose claims a figure the rows contradict | M (V0 T6, T11) | only one magnitude derivable; rubric grades the derived figure |
| D11 | Phantom reference | a review cites a spec that exists nowhere | P | grade an affirmative finding the prompt asks for |
| D12 | Red-herring causal event | a coincident Done card | P | grade the true cause, never "disclaims the herring" |
| D13 | Competing hypotheses | three hunches, one is real history for another title | M (V0 T6) | each confirmable/falsifiable from reachable data |
| D14 | Near-miss exclusion | items that almost satisfy the rule | M (QC) | grade the included set; never require explaining exclusions |
| D15 | Result-limit burial | decoy-adjacent detail behind high-traffic terms | P | never the first link; unreachable = Missing Universe Data |
| D16 | Non-authoritative instruction | instruction-shaped message outside the delegation chain | P | never graded; ignoring it is correct |

### 6.2 Supersessions (prove discovery order for each — the claim must be met first)
| ID | Technique | Ev. |
|---|---|---|
| S1 | Thread continues past the apparent conclusion | **M** (A1) — strongest single lever |
| S2 | Cross-surface later correction (email claim → later Slack correction) | **M5** (v2 trap 2: 28 of 46 Opus 5.5 tasks) — only when the correction is off the first-read path: not in the superseded record's container, an anchor's container or a record that delegates to it (§13; `hardness_v2_check` SAME_PLACE) |
| S3 | Structured-system supersession (Linear comment or merged PR overrides the description) | P |
| S4 | Retraction / withdrawn claim | **M** (A11) |
| S5 | Failure surfaces before the admission | **M** (A11) |
| S6 | Later reply changes the unit or restates a figure | M (77% task — use inside a chain, not alone) |
| S7 | Response pairing | **M** (A9) |
| S8 | Superseded value must be named as superseded (incorporated rule) | M (measured with a prompt hint; a hint aimed at the trap now fails Contrived under `task-quality-v1` — the incorporated rule must carry it) |
| S9 | Moved deadline / newer tab / revised spec / rescheduled event | P |
| S10 | Exclusion settled by the other side within seconds | **M** (A10) |
| S11 | Effective-date dual regime (v1 before date D, v2 after) across the cohort | P — pair with A2 |
| S12 | Versioned rule home (Confluence v2 still linked from older docs; v3 current) | P |
| S13 | Partial amendment (one clause changes; the rest stand) | P — WORKFLOW requires retaining unaffected clauses |
| S14 | Chained supersession (A → B → partial revert C) | P |
| — | Verbatim supersession in the thread the prompt points at | **X** (6/6) — scaffolding only |

### 6.3 The ML team's sub-75% list, made V2-legal
Verbatim list (V1 05 §6): custom "weird" business rules · conditional authority rules
(follow A over B if more senior, EXCEPT if A's decision is older than two months) ·
multi-factor conflict resolution · safety/communication rules (internal-only information)
· cross-recipient information boundaries · conflicting instructions across 4–6 sources.
"Already tried, treat as the floor": 8+ sources/services/deliverables, multiple schemas,
irreversible writes, hundreds of records, strict schemas, sparse data, temporal
conflicts, people conflicts, stacked flags, multi-source reconciliation, exact values,
distractors, 800+-call context pressure, error injection, async waits.

V2 changes two things: every rule must be **incorporated** through the lattice (§3), and
measured runs show these rules applied **once** are solved by Opus (6/6). They become hard
only when (a) applied to every record of a large cohort (A2), (b) a scope/alias question
survives retrieval (A7), or (c) the rule-bearing fact sits past an apparent conclusion
(A1). Build them that way.

### 6.4 Context shifts and context switching
- **Shift = superseding information met in discovery order** (never a live change). For
  each: claim met first · overturned by · why met first · why decisive. The answer must
  change when the correction is found; grade the revised answer.
- **Context switching levers**: cross-title lookalike contexts (CS1); ID-namespace switching
  — one person as `user_EMPLOYEE_00NN` (Confluence), `usr_<Name>` (Linear),
  `EMPLOYEE_00NN_SLACK_ID` (Slack), `PERSON_####` tokens (CS2); Linear↔GitHub joins with no
  link field (CS3); predicate/unit switching inside one rule set (CS4); long-run drift of
  field names, cutoffs and flags (CS5, multiplier only); rarely-opened services (Confluence, Snowflake) that hold
  deciding evidence behind a pointer (CS6); interlocking chains that share records so the
  agent cannot linearise (CS7).

### 6.5 Chaining and cascades
Linked chains (2-link floor; 3-link "filed it on a different ticket" pointer; spines
across services where node N is undecidable until N−1 resolves); forensic chain of
eliminating facts (**M**, A4); cascades are allowed **inside** a chain only — always pair
with ≥ 2 independent chains; reuse-vs-duplicate (**M**, A8); absence-as-evidence graded as
an affirmative finding (**M**, Martin); hops that force a structured system (Snowflake-only
aggregates).

### 6.6 Legitimate volume multipliers
Record × surface matrix (**M**); scale-completeness predicate (**M**); thread-reply opens
(**M**, A3 — scope by window/channel or the count explodes); day-level instead of
total-level data; long-channel reading across a window; per-record cross-service joins
(Linear↔GitHub, vendor invoice↔contract↔approval↔payment↔owner); reads before every write;
add sources, not deliverables. Async search (submit → status → result) adds real calls
only where discovery is unavoidable and the prompt names no artifact.
**Anti-inflation test:** if the call were removed, could correctness, completeness or
verifiability of the deliverable change? If not, it is padding.

### 6.7 Friction and access control
Forced errors on unscoped functions (GitHub/Linear/Trello) with a named alternate path;
rate 1.0 = route around. Async only on searches whose target is not named. Access control:
restricted source summarised where the persona can read; expected source invisible → find
the equivalent; escalation as the correct action. Never hide the only copy behind the ACL
(invalid all-fails), never require the agent to say a record "exists but is restricted".
Every roster persona has a Gmail mailbox in both universes — check `users.json`
for non-roster people before assuming a mailbox, and verify reach per record.

### 6.8 Deliverables and grading levers
One register with closed vocabulary, checked-absence states ("NONE FOUND" vs "NOT
CHECKED"), exact reconciliations; a written record; 3–6 dependent writes across ≥ 3
services; same fact on two prompt-specified artifacts = two criteria (signature
diversity). Always-fail weight on eliminating facts ≈ 20–30% of total; delivery weight
small (sheets/docs/posts "always pass"); spot-check ≤ 5 hard/edge items per group + a
volume row; never tune rubrics to the baseline.

---

## 7 · Placement rules (all mandatory)

1. The **first link of every chain** is findable by a broad search. Difficulty lives in
   connecting links, never in hiding the first one.
2. Every dynamic shift has a **discovery-order proof**. If a plausible path meets the
   correction first, the shift adds nothing.
3. Every trap has **one resolver** a careful reader accepts (newer + applicable + scoped +
   authoritative source). No trap may create a second defensible final state.
4. Traps are spread across **≥ 6 distinct requirements** and **≥ 3 independent root causes**.
5. Every seeded record is **persona-reachable** (or the designed outcome is an affirmative
   denial + alternate/escalation).
6. **Seed the evidence, never the conclusion.** No record states a total, a classification
   or the answer.
7. Inject against what exists (replies on live threads, comments on real tickets) before
   creating free-floating objects.
8. Every write's content depends on the investigation. No bolt-ons.

---

## 8 · QC safety rails (each one can fail the task on its own)

| Rail | Rule |
|---|---|
| Unique Ground Truth | two careful runs must end in the same final state; decision ambiguity (act vs defer, A vs B recipient, X vs Y location) fails, with no middle band |
| Incorporation | every graded requirement traces to the prompt through explicit delegations (§3) |
| Unauthorized criteria | no grading of unstated expectations, distractors, or one side of an unresolved conflict |
| Feasibility / ACL | every required read reachable from the persona's view; every write exists in the catalog; killed tools have alternates |
| Pre-solved / contrived | the prompt names the problem, not the root cause; no spec-sheet register (≥ 2 of: enumerated contents, format rules, prescribed reply format, contents-driven length) — the details live in the hub/spokes |
| Bolt-on / over-stacking | one subject; "~11 actions across 6 services" in one prompt was flagged — keep asks in the lattice and writes dependent |
| Padding | blocked/repeated calls never count; no checkpoint choreography |
| Originality | never mirror the ML-selected example or a supplied sample (≥ 4/7 fingerprint elements fails) |
| Universe coherence | the six seeding rules; `tools/sql_lint.py` clean; intended disagreements documented |
| Horizon | ≥ 500 on Normal = Borderline (non-fail, caps score at 3); a fast 100% rollout sets the count |
| Failure diversity | ≥ 2 patterns (differ on ≥ 2 rubric results), none > 50% of failing runs, per-rollout SD 0.1–0.3 (Evals `scoring.json`) — never let one discovery gate most rubrics (bimodality) |
| Judge reliability | a verifier missed a late write in a long trajectory (V4-NF1 r5) — keep writes few, distinctive and verifiable from the final state |
| Hardness validity (`/hardness` 1A §2–§3) | a failure counts only if four things hold: the rule is incorporated, the evidence was returned by an ordinary call, one end state exists, and the verifier judged it right. Otherwise it is a defect, not hardness (§11: a 48.7% task was ≈ 80% once unincorporated-handbook rows were removed) |
| Run validity | record mixed-model rollouts (Haiku or Sonnet subagents), compaction, background work after the final answer, and missing or duplicate rollout files. Exclude them from the horizon count and from attribution (`01a` B0) |
| Same-place correction (v2) | a correction in the superseded record's container, an anchor's container or a record on the delegation path to the original is read on the way and settled by Opus 5.5 (v2 Part 2; dd-2024 rev1 T1/T3); `tools/hardness_v2_check.py` SAME_PLACE flags it. Advisory, but every flag needs a disposition |
| Evals rubric overrides | prohibition-only titles always fail, and so does any row an agent passes by doing nothing ("leaves X as found"); artifact-subject or tool-named titles = Major + FAIL; overly specific = Major; overly broad = Major (`task-quality-v1`); every row needs a `valid_case` it accepts and a `do_nothing_case` it rejects; predicted all-fail on ≥ 2 rows = FAIL; spot-check groups need a volume criterion (`Evals/3_Rubrics_Eval.md`, `hg-strict-overrides-v1`) |

---

## 9 · Proven not to work (do not build the task on these)

Each "already tried" item in isolation · one binary trick (80.5%) · off-by-one counts as
the engine (77%) · 80+ existence/format rubrics (79.5%) · spec-sheet prompts · rules
enumerated in one source over a small named cohort (95.5%) · retrieval-floor traps
(Opus 6/6) · conditional/seniority rules applied once (6/6) · verbatim supersession in the
pointed thread (6/6) · hiding evidence or hiding the only copy behind ACL · vaguer asks
(18/31 QMS reviews failed UGT) · extra deliverables · bolt-on writes · padding · a long
horizon that a content search or a broken tool decides (540 → 94) · async on a named
artifact · forced errors on a tool never called · corrections met before the claim ·
unincorporated policy rules as graded obligations · grading distractors or requiring
exclusions to be explained · hard-coding one side of an unresolved conflict (Task11:
three correct runs failed) · grading surfaces the prompt never anchors · tuning rubrics to
hit gates · forgetting to re-inject before a run · Haiku pre-checks as hardness proof · graded rules in a handbook the
prompt never names (SB-T1: 9 all-fail rows, all invalid) · grading an open-ended ask ("anything
else still open") on one specific item (NF2 PR #1914, failed 5/6: a fairness risk, not a
mechanism) · a landed mechanism whose criteria carry too little weight to move the average (NF2:
material misses in 5/6 runs, average 88.9%).

Added from Season Pass (§12):
- rules enumerated in a hub-named document: seven rule families leaked in every revision-13 run;
- a plain-words pointer, in a record every run reads, to the deciding record: Opus 4.8 followed it within 26 events;
- a list whose membership rule is stated explicitly (value notes, process findings): exact in every pure run;
- a confident claim contradicted by per-item records the agent reads anyway (0/5);
- counting on model fallbacks or harness failures. These are validity confounds, never levers.

Added from Hardness v2 (§13). Part 4 lists these as passing 6/6 for Opus 5.5 even in tasks that scored low overall:
- long inventories and routine bulk writes (the 31 % Drive task listed exactly 44 files and did every ordinary move);
- straight totals on clean inputs, and clear calls from visible evidence (seven keep/cut calls with CPI and D1);
- pulling facts from one spec page and publishing them; a caveat Opus can see;
- adding steps, services or rows: none lowered scores by itself. Volume is a horizon tool, never a difficulty tool.

Parts 2 and 8 add two more: a correction in the same channel or thread as the original (Opus checks stale-vs-newer
there by default), and rules written into the prompt (one task went from failing to 100 %).

---

## 10 · Where V1 and V2 advice conflict — and the resolution used here

| Conflict | Resolution |
|---|---|
| Hidden rules vs incorporation | incorporate through anchor → hub → explicit delegation; keep the rule located away from the first-read thread |
| Cascades vs signature spread | cascade inside a chain; ≥ 3 independent chains |
| "10+ shifts" vs "seed one message" | one decisive wrong summary per chain + corrections only where they change a graded fact |
| 10+ services / 8+ writes vs QC norms (3–5 writes) | 10–13 services carrying **evidence**; 3–6 dependent writes across ≥ 3 services |
| 500+ vs tiers | target ≥ 500 per the requester; state the Borderline-Horizon consequence on Normal-tier tasks |
| Reference files 6–8 vs "earns its place" | only when the scenario needs an attachment |
| v2 "add a guard row" for an item left unchanged; trap 9 "grade that the agent leaves those items alone" vs the do-nothing rule (§8, `09_Rubric_Writing.md` gate 7, executable in `Evals/tools/hg_rubric_checks.py`) | keep the do-nothing rule: the grader fails any row an idle agent passes. Grade v2's intent as an exact count or scope on the required write ("creates vendor charge records for exactly 17 of the 20 receipts", "labels exactly 17 emails") or as a requirement inside a required artifact. Support: the Agentic Benchmark Checklist (Zhu et al., NeurIPS 2025, arXiv 2507.02825) asks for a do-nothing baseline and a ground-truth state that includes untouched items and that trivial changes cannot satisfy (O.g.2–3) |
| v2 "a task with no mode is treated as Medium" vs "never infer the mode" | authoring keeps refusing a missing V3 mode (`difficulty_stats`, `GEN_EXECUTION` §0); only the advisory geometry (`difficulty_mutation.caps_for`) defaults to Medium, and it says so |
| v2 "put weight 5 on the trap rows" / "raise the weight" vs weight = kind of work, never re-weight (`09_Rubric_Writing.md` gate 8) | same outcome by design: make the trap decide 5-band work (multi-source reconciliation, tracing). Move the evidence onto the decision path or change the work; never raise a weight. `hardness_v2_check` DECISION_FLIP flags a rule that can flip no weight-5 slot |
| v2 "pick at least two of the nine traps" vs the ≥ 12 traps / ≥ 7 families floor | both: the local floor stays; §13 maps the nine traps onto mechanism ids and families, and at least two of the nine must be present (A24 and A25 added for traps 1 and 9) |

---

## 11 · Calibration evidence: `/hardness` band vs observed V1 baselines (Oct 4)

**Method.** For each task, one baseline run was read blind as the `/hardness` stand-in, because V1 had no separate pre-check. Its band was predicted under 1A before the verifier results were opened. Then every designed node was checked in all six runs, and every failed criterion was attributed (`01a` B3, B3d, B3e).

**Sources** (all read-only):
- NF1: V1 QC non-fail task 1 (HarmonyGames)
- NF2: V1 QC non-fail task 2 (HarmonyGames)
- V7-T1: V1 HarmonyGames task 1
- SB-T1: V1 authoring-bundle QC task 1. This one is semi-blind: its 0.53 was already quoted in §0.

All runs are Opus 4.8. The NF1 and NF2 rubrics are unweighted. Scratch work: `support/examples/calibration/hardness/`.

| Task | Blind band (run read) | That run's score | Baseline avg, raw → clean | pass@1 | Agreement |
|---|---|---|---|---|---|
| NF1 Combo PR review audit (normal) | 2 HOLD | 89.7% (100% clean) | 83.9% → ≈ 88% | 0/6 | agree: too easy |
| NF2 tracker cleanup (normal) | 4 PROCEED | 81.0% | 88.9% → 88.9% | 1/6 | band right for the run; the baseline fails the < 75% gate (mechanism weight ≈ 26%) |
| V7-T1 board cleanup (long, 79 tickets) | 3, then 4 after reading comment bodies | 60.0% | 58.3% | 0/6 | under-called by one band until the comment bodies were read |
| SB-T1 store-size recert (normal) | 2 HOLD | 61.1% (100% clean) | 48.7% → ≈ 80% | 0/6 (3/6 clean) | agree under 1A; the raw verifier "hardness" was invalid |

**Mechanism evidence.** Counts are runs out of 6. LANDED means genuine under `01a` gate 8.

| Task | Mechanism | Landed | Confounded | Leaked |
|---|---|---|---|---|
| NF1 | Partial resolution read from shipped code (one file fixed, a sibling file not) | 4 | — | 2 |
| NF1 | House rule "if the reviewer fixed it himself, leave it out" (A15) | 2 (wrong ticket) | 4–5 (rows demanding the exclusion be explained; QC-flagged) | — |
| NF1 | Scope boundary: the other title's board (A7) | 1 (wrote ZOM states) | 1 (verifier error: the judge concedes no write, then fails it) | 4 |
| NF1 | Later APPROVED sign-off (A6) · phantom spec (D11) · bot vs human reviewer | 0 | — | 6 |
| NF1 | Unconfigured tool defect: issue-comment ID collision | — | hit 6/6; no score effect (routed to review comments) | — |
| NF2 | Cohort members without the keyword in the title (A17) | 3 | — | 3 |
| NF2 | Merged PRs whose title carries no ticket key (A18 + Linear↔GitHub join) | 2–3 | — | 3–4 |
| NF2 | "Anything else genuinely open" graded on one PR | — | 5 (fairness: open-ended ask) | 1 |
| NF2 | Decision of record in the executives channel (A13) · checked absence of code | 0–1 | — | 5–6 |
| V7-T1 | Per-record house rule on what counts as landed (A15) | 4 | rule-interaction UGT risk recorded | 2 |
| V7-T1 | Finding on records whose state is already correct (changes-requested merge, A6/A15) | 5 | — | 1 |
| V7-T1 | Channel-vs-runbook conflict the agent must report (A16) | 5 | — | 1 |
| V7-T1 | 120-day owner-exemption split · move off the ship line | 1 · 1 | — | 5 · 5 |
| V7-T1 | Cohort vs stale deck (A17) · revert · calendar authority · parent-child · cross-recipient emails | 0 | — | 6 |
| V7-T1 | Run 2 subagents ran on Haiku 4.5 (scored 50%) | — | 1 (run) | — |
| SB-T1 | Unnamed 2026 handbook (Linear schema, one-decimal email, 14-day lock) | — | 6 (fairness: unincorporated; 9 all-fail rows, 35/90 weight) | — |
| SB-T1 | Correction only in a thread reply (221 − 7, 231 − 25) (A14) | 1–2 | — | 4–5 |
| SB-T1 | Forced errors (3 tools at rate 1.0) + async Drive search | 0 | — | 6 (routed around) |

**Disagreement classes, and the rule each produced**
1. **Payload-blind (V7-T1).** The narration and state changes looked right. The two mechanisms that failed 5/6 were visible only in comment bodies. Rule: `01a` B1 reads write payloads; Self-review step 3.
2. **Band ≠ baseline gate (NF2).** A genuinely material run sat beside an 88.9% average. About 74% of the weight was in always-pass atomic rows, and one run was golden. Rule: `01a` gate 9, the B3d weight share, and the A5b ≥ 30% mechanism-weight check.
3. **Invalid hardness (SB-T1, NF1).** Unincorporated rules, unauthorized rows and verifier errors make raw numbers look hard. Rule: `01a` gate 8, the CONFOUNDED verdict, the B3d clean average and B3e.
4. **Run defects (NF2, V7-T1).** NF2 is missing its run-1 file and has a duplicate run-3. V7-T1 run 2 used Haiku subagents. File order does not match the verifier's `Run #`. Rule: `01a` B0.
5. **Fact drift (V7-T1).** "Title-only" PRs turned out to have merge commits naming the ticket. Rule: Self-review step 4.

**What transferred to Opus here:**
- rules applied per record against the natural reading
- findings on records whose state is already correct
- conflicts the agent must report
- cohort membership not keyed by a keyword
- partial resolution read from code

**What leaked 6/6:**
- decoys and authorities every run reached
- reverts and parent-child callouts
- cross-recipient splits stated in an incorporated write-up
- forced errors and async waits

---

## 12 · Season Pass, revisions 10–14 (Opus 4.8 platform runs, Oct 21–25)

A Hard task (cap 70 %) with a 128-component register, a review slide, a tracking issue and two messages. Across 14
revisions, every designed rule, pointer, list and claim leaked, and the task was skipped. Details:
`plans/Rev13_Results.md`, `support/backtests/season_pass/rev14/working_files/rev14_platform_runs/Rev14_Precheck_Findings.md`.
The full task folder is archived at `support/archive/task_inputs_season_pass_2026-10-25/`.

| Revision | Six-run average (corrected) | Designed mechanisms that landed | Where the loss came from |
|---|---|---|---|
| 10 | 84.69 % raw | issue remap in 1 run (rule in 0 of 8 briefs); row association in 1 | brief transmission, slips |
| 13 | 92.1 % (SD 0.068) | 3 rules once each; 2 of them in fallback runs | about 1 wrong row in 128 per run, cascading through totals |
| 14 | about 90 % (4 of 6 runs) | M1/M2 only through Opus 5 fallback decisions; M3/M4 0/5 | fallback-rewritten briefs and classification; 2 group-membership slips in the one pure run |

**What leaked, and why.** All **[O]** unless marked.
- **Every source the hub names was read, 7/7.** The hub named every source, so retrieval was complete:
  validation comments 330–338 of 338, every review, timeline and PR, and every hub-named source.
- **Stated rules ran as checklists.** Opus 4.8 copied each rule into its subagent briefs. In rev-13 run-4, the 12 briefs
  Opus 4.8 wrote stated the rule; in rev 14, Opus 4.8's briefs kept the dismissal exception.
- **The pointer was followed.** Revision 14 put the owner's calls in tracker comments, with a plain-words pointer in the
  description. Opus 4.8 listed the comments 26 events after reading the description.
- **Lists the agent compiled itself came out exact,** with explicit membership rules: value notes and process findings.
- **A confident non-owner claim lost to the per-item records** in 5 of 5 runs.
- **The contrast that matters [I].** The same families landed on V7-T1 and SB-T2 (§0, §11), where the governing rule
  was named but its location wasn't. Incorporation style, not the mechanism, decided transfer.

**What cost points:**
- slips at scale: a class error cascades to about 8–10 points through the totals and groups;
- tool-surface friction: a native Sheet instead of a CSV in 5 of 12 runs;
- a multi-membership rule slip: "count under every condition" on 2 keys;
- the `model_refusal_fallback` (category bio) in 8 of 12 runs. After it, the fallback model rewrote briefs (dropping an
  exception) or took over classification. Every traced failure in the four revision-14 fallback runs came from those
  decisions; the pure Opus 4.8 run (r3) lost about 8 points to the two slips above.

**Lessons for V3 (Opus 5.5).** See `plans/V3_Opus55_Difficulty_Plan.md`.
1. **Incorporate by role, not by location.** Never let a hub list every authority. V3 allows multi-hop reachability.
2. **Design to the mode's loss budget.** Easy needs more than 10 points of loss, Medium more than 15, Hard more than 30.
   Season Pass was Hard, a band only about 5 % of tasks get.
3. **A fallback run is not Opus 5.5 evidence and is invalid under V3.** Screen themes: bio-adjacent words are suspected,
   not proven. Check every pre-check for fallback events.
4. **Confirm every failed slot against the write payload.** The proxy grader had eight decoder defects on these outputs;
   one run moved 20 points.
5. **Measure on the target model before building.** The pre-registered forecast said 72 %; the observed was about
   90 %.

---

## 13 · Hardness v2 — what beats Opus 5.5 (client guideline, 2026-10-31)

Source: `references/Docs/13_Hardness_v2_Opus55.md`, verbatim. 46 Enterprise Atlas tasks where Opus 5.5 scored under
75 % on the baseline (270 runs, 2,843 graded rows); for every failed row the judge's reasoning was checked against the
author's evidence. Evidence tag **[M5]** = measured on Opus 5.5 by that study. It is the current authority for the
baseline model; the [M] tags above are Opus 4.8 or earlier.

**Scoring (Part 1)** is unchanged: six unhinted Opus 5.5 rollouts, weighted rubric score, average strictly below the
mode cap (Easy 90 %, Medium 85 %, Hard 70 %; `references/v3_policy.json`). Weight-5 rows must depend on what Opus gets
wrong. The pre-check is one run: an early warning, never a verdict.

**What changed (Part 2).** Corrections still work only out of the way; "proving done" is now the top trap; length does
not make a task harder (Normal tasks 66 %, Long-Horizon 67 %); plain volume and arithmetic are easy — Opus fails when
the inputs to a total are wrong, not when it adds.

### 13.1 The nine traps, in order of cost, mapped onto this library

| # | v2 trap | Mechanism ids | Trap families | Build (v2 "How to build it") | Grade | Self-check |
|---|---|---|---|---|---|---|
| 1 | Proving "done" across services | **A24** (new) | `done_gap` | a believable, easy-to-find done source (merged PR, closed ticket, sign-off) and the missing piece in another service, found only by checking each part; the data defines "on prod", "merged", "signed off" | the status / inclusion row at weight 5 | DONE_CHECK |
| 2 | A correction somewhere else | A1, A11, A16 (S1–S4, S7, S9, S13) | `superseding`, `stale_summary`, `conclusion_stop` | a dated correction in a thread reply, page comment, review or another service, tied to the same item and person; it must change a number, status or write. Never in the superseded record's container, an anchor's container or on the delegation path to it | the corrected number / status | SAME_PLACE |
| 3 | Follow-through a rule requires | A15 (+ `writes[]`) | `authority`, `synthesis_omission` | the rule in a real handoff, team rule or earlier promise; an easy destination | a few representative writes plus one count row — never dozens of identical rows | DECISION_FLIP |
| 4 | Dates, windows, dependencies | A10, A17 (S9, S11) | `effective_date`, `unit_or_timezone` | the governing timezone and method in a natural plan or message; one boundary case or changed leave record that moves a real assignment | the qualifying item / scheduled work | FILTER_CHECK |
| 5 | A rule or exception hidden in the data | A12, A15 | `authority` | a natural reason to look for the policy (the request mentions the cleanup, budget or roll-up); the deciding exception in a record reachable from there | each singled-out exception on its own row | RULE_IN_PROMPT |
| 6 | Different names for the same thing | A7, A8 | `scope_alias`, `entity_collision` | a real alias, person-to-company link or differently titled existing ticket, mapped in contacts, an earlier conversation or ticket history; no spelling tricks | inclusion / reuse row | — |
| 7 | Items outside the obvious filter | A17, A18 | `exact_predicate`, `near_miss_mention` | two or three genuinely in-scope items just outside the obvious search, with a rule in the data that brings them in | each item on its own row | FILTER_CHECK |
| 8 | Wrong inputs to a total | A1, A10, A13, A14 feeding an aggregate (no new id) | `superseding`, `cross_reference_gap` | adjustments, refunds, revised claims or rounding rules in normal billing records or messages | the corrected input and the final figure on **two separate rows** (legal: gate 6 forbids three or more) | INPUT_CHECK |
| 9 | Work someone already did | **A25** (new) | `completion_elsewhere` (distractor type `already_done`) | a believable completion note in a different place from the original request | an exact count or scope on the required write ("creates records for exactly 17 of the 20 receipts") — never a "leaves X alone" row (§10) | — |

Pick at least two of the nine (Appendix); the local ≥ 12 traps / ≥ 7 families floor still applies. A24 and A25 have no
ledger records yet: `hardness_ledger.py priors --family A24` returns Beta(1,1), UNCALIBRATED, so a forecast needs a
disclosed `--channel-rate` or reports the rule as UNPARAMETERIZED.

### 13.2 Design rules (Part 5) and the self-checks (Part 7)

Before writing: at least two deciding facts that need checking across sources (two separate decisions); for each, the
convincing wrong source and the record that beats it, with who wrote each, when and with what authority; the miss
changes a weight-5 row (status, number, inclusion or write, not a comment); every alias, invoice ID or build number
maps back through persona-visible records; rules live in the records and the prompt only points at a natural start.

`python3 -B Task_Authoring/tools/hardness_v2_check.py --task-dir Task_Authoring/task_inputs` (`--design` at the
scenario stage) answers the self-checks from the manifest, SQL, gradable surface and prompt:

| Check | v2 | Fires when |
|---|---|---|
| SAME_PLACE | Part 7 same-place; trap 2 | the newest version record shares a container with a superseded one (`same_container`), sits in an anchor's container including its thread replies (`first_read`), or sits in the container of a record that delegates to a superseded one (`on_delegation_path`) |
| DONE_CHECK | Part 7 done check; trap 1 | no A24 rule, chain root or `done_gap` trap |
| TWO_DECISIONS | Part 5 rule 1 | fewer than two portfolio rules spanning ≥ 2 services that decide different requirements |
| DECISION_FLIP | Part 7 decision flip; Part 5 rule 3 | a portfolio rule can flip no weight-5 slot |
| INPUT_CHECK | Part 7 input check; trap 8 | a weight-5 aggregate slot no rule or mutant can move |
| FILTER_CHECK | Part 7 filter check; trap 7 | no `exact_predicate` / `near_miss_mention` trap and no A17 rule |
| RULE_IN_PROMPT | Part 8 | eight consecutive words of a trap resolver appear in the prompt |

A container the tool cannot derive is UNRESOLVED, never clean; declare `version_records[].container` (key format in the
tool's docstring) when a base record holds the correction. The tool is advisory (exit 0; `--strict` for design loops)
and is not a stage-gate check; every FLAG needs a written disposition, and the response is a redesign, never a weaker
fairness link or a raised weight.

### 13.3 Observed on this repo: dd-2024-release-cost rev1 (one Opus 5.5 pre-check, 2026-10-31)

One unhinted Opus 5.5 run solved the task completely (495 of 495 ticket lines, every total, every write; /hardness FAIL
score 1, "too easy"). Every trap was settled on its first read — the v2 failure mode exactly:
- the pool amendment (T1) was a reply in Ines's own thread, the thread that delegates to the method doc; reading the
  thread returned the original and the amendment together (`on_delegation_path`);
- both train-map versions and "the December version stands" came back in one Trello card read (`same_container`, T3);
- the board-model sheet that held the slot count was an anchor (`first_read`, T4); two cancelled calendar slots were
  visible in one `gcal_list_events` call; archived tickets came with the first `includeArchived` listing;
- decoys were never on its path; per-ticket pick notes were brute-forced (897 `linear_list_comments` across six
  subagents, 1,002 calls, $22). Volume bought calls, not failures.
`hardness_v2_check` flags T1, T3 and T4 on that revision. One run is an observation, not a rate.

### 13.4 If the run comes back too easy (Part 8)

Look at which heavy rows passed 6/6 — those are what Opus finds easy; don't add more of them. Move a correction out of
the obvious place (thread reply, comment, review, another service); add a done source with a missing piece, or a
completion note somewhere else; move one or two in-scope items outside the obvious filter; put the deciding fact behind
an alias a contact or history record resolves. Don't add rows, items or steps, and don't spell the rule out in the
prompt. Routing: `playbooks/12_Difficulty.md`, `playbooks/01a_Hardening.md` MODE B.


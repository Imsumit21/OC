# H3 — Review-blocker clause: necessity audit + companion-mirror leak audit

Task: Julia Lawson, ZM3D beta live-ops calendar — synth-cut, clock 2025-10-01 00:00 PT (07:00Z).
Scope: the 22 merged live-ops match3d PRs (`harmonygames-Games/match3d#<n>`: 353 356 357 360 364 370 384 394
396 397 400 403 420 438 454 456 459 465 468 470 472 475).
Sources (read-only): `research/raw/github.json` (`pull_requests`, `reviews`, `review_comments`,
`pull_request_comments`, `timeline_events`, `users`); `research/raw/slack_C093LEZGF6J_2025-09.json` (665 msgs,
base INT-01 mirror corpus); `research/R_B_spine_facts.md` §4; `research/R_D_coherence_audit.md`;
`research/R_C_carriers_ids.md` §1/§6; `research/S7_backend_config_and_gh_tools.md` §3;
`Task_Authoring/references/universe_kb/by_universe/synthcut/integrations.json` (INT-01 / INT-12 / INT-13);
`Evals/references/persona/acl.md`; `Evals/references/tools/catalog.json`.

Clock test used throughout: `submitted_at < 2025-10-01T00:00:00Z`. All review rows in scope are Aug–Sep 2025.

---

## 1. Review-state census of the 22 merged PRs

All 22 are `state=closed`, `merged=true`. Review rows are the `reviews` object
(`id = <pr>#rev_N`); author names resolved via `github.json.users`.

| PR | merged_at (Z) | reviews (submitted_at · state · author) | #rev |
|---|---|---|---|
| #353 | 2025-08-02T20:12:29 | 08-02T20:09:52 · APPROVED · Arthur Blake | 1 |
| #356 | 2025-08-03T03:39:22 | **none** | 0 |
| #357 | 2025-08-05T16:01:19 | 08-05T15:01:02 · APPROVED · Arthur Blake | 1 |
| #360 | 2025-08-06T01:03:15 | **none** | 0 |
| #364 | 2025-08-06T13:40:56 | 08-06T13:40:51 · APPROVED · Arthur Blake | 1 |
| #370 | 2025-08-13T16:12:18 | **none** | 0 |
| #384 | 2025-08-19T13:35:35 | 08-18T14:02:18 · COMMENTED · CodeRabbit (org) | 1 |
| #394 | 2025-08-21T17:47:34 | 08-20T14:58:06 · COMMENTED · CodeRabbit; 08-21T17:47:29 · APPROVED · Arthur Blake | 2 |
| #396 | 2025-08-22T13:39:18 | **none** | 0 |
| #397 | 2025-08-22T15:10:54 | **none** | 0 |
| #400 | 2025-08-26T00:41:27 | 08-26T00:41:20 · APPROVED · Arthur Blake | 1 |
| #403 | 2025-08-26T18:51:03 | 08-26T16:00:16 · COMMENTED · CodeRabbit; 08-26T18:50:58 · APPROVED · Arthur Blake | 2 |
| #420 | 2025-09-08T15:26:59 | **none** | 0 |
| #438 | 2025-09-15T23:09:34 | 22:42:53 · COMMENTED · CodeRabbit; 22:44:05 · COMMENTED · CodeRabbit; 23:08:36 · COMMENTED · CodeRabbit | 3 |
| #454 | 2025-09-19T17:50:52 | 09-19T17:50:45 · APPROVED · Calvin Price | 1 |
| #456 | 2025-09-24T14:30:39 | 09-22T16:04:21 · COMMENTED · CodeRabbit; 09-22T17:58:01 · COMMENTED · CodeRabbit; 09-23T23:31:02 · APPROVED · Oliver Brooks | 3 |
| #459 | 2025-09-24T23:06:25 | 09-23T23:40:50 · COMMENTED · CodeRabbit; 09-24T18:10:23 · COMMENTED · CodeRabbit; 09-24T22:36:13 · COMMENTED · CodeRabbit | 3 |
| #465 | 2025-09-25T22:15:51 | 09-25T18:43:41 · COMMENTED · CodeRabbit; 09-25T21:43:05 · COMMENTED · CodeRabbit | 2 |
| #468 | 2025-09-29T16:13:50 | 09-26T20:29:29 · COMMENTED · CodeRabbit; 09-26T21:54:00 · COMMENTED · CodeRabbit | 2 |
| #470 | 2025-09-30T15:51:15 | 09-29T21:28:59 · COMMENTED · CodeRabbit; 09-30T02:32:37 · COMMENTED · CodeRabbit; 02:43:00 · COMMENTED · Owen Baker (self); 02:43:24 · COMMENTED · CodeRabbit; 02:50:56 · COMMENTED · Owen Baker (self); 02:51:12 · COMMENTED · CodeRabbit; 03:26:28 · COMMENTED · CodeRabbit; 03:44:37 · COMMENTED · CodeRabbit; 15:51:06 · APPROVED · Arthur Blake | 9 |
| #472 | 2025-09-30T15:53:04 | 15:52:58 · APPROVED · Arthur Blake | 1 |
| #475 | 2025-09-30T16:09:15 | 16:09:09 · APPROVED · Arthur Blake | 1 |

Totals in scope: **34 review rows** across 22 PRs (16 PRs have ≥1 review, **6 have none**: #356 #360 #370
#396 #397 #420). State distribution: **APPROVED 11**, **COMMENTED 23**, **CHANGES_REQUESTED 0**,
**DISMISSED 0**, PENDING/REQUEST_CHANGES 0. By author: CodeRabbit (org) **21**, Arthur Blake **9**,
Owen Baker **2** (self-reviews), Calvin Price **1**, Oliver Brooks **1**.

### Answer: does ANY of the 22 carry an unresolved/open CHANGES_REQUESTED at the clock?

**No — none.** `CHANGES_REQUESTED` does not occur even once in the 22-PR cohort, and no PR in the cohort is
`state=open` or `draft`. The clause is therefore a **clean certify-absence check**: reading the reviews of
each of the 22 confirms "no blocker", so **no beat is ever held by this clause**. The reads are necessary
(you cannot certify absence without looking) but they **add no graded hold** and must not be scored as one.

Boundary rails this census establishes:

1. **#303 is the only `CHANGES_REQUESTED` in match3d and it is a decoy, not a hit.**
   `match3d#303` ("Samuel/zom 349", merged 2025-07-16, `merged=true`) carries
   `2025-07-16T03:49:49Z · CHANGES_REQUESTED · CodeRabbit` that is never dismissed and never cleared by
   CodeRabbit itself (only a later `2025-07-16T17:07:30Z · APPROVED · Arthur Blake`). It is **not one of the
   22**. If the clause is scoped by *beat* ("weekly leaderboard / quest chest tooltips") rather than by the
   22-PR cohort, #303 becomes a spurious blocker and wrongly holds the weekly-leaderboard and quests beats.
   **Injection constraint C-0: scope the clause explicitly to the 22 cohort PR ids, not to a beat or a
   date range.**
2. **The clause is narrower than "merged with review".** #438, #459, #465 merged with **zero human review**
   (CodeRabbit `COMMENTED` only) and #384/#468 merged with **no APPROVED at all**. Under a
   "no open CHANGES_REQUESTED" test all of them **pass**. If the design ever wants a hold for "merged without
   any human approval", that is a different clause (a separate, non-absence test) and must be introduced
   deliberately — do not let the reviewer read be repurposed for it.
3. **Bot-authored reviews are the majority (21 of 34).** A clause keyed on reviewer identity
   (e.g. "human CHANGES_REQUESTED") would silently exclude the only base blocker in the repo (#303, bot).
   Keep the clause author-agnostic and let the cohort scope (#1) do the exclusion work.

---

## 2. Necessity of the review read

**Verdict: YES, required — the review `state` exists in exactly one object and is reachable by exactly one
tool.**

The three GitHub read surfaces are disjoint (confirmed against `github.json` fields and
`Evals/references/tools/catalog.json`):

| surface | tool (`catalog.json`) | key fields present | carries `state`? | carries body text? |
|---|---|---|---|---|
| review containers | `github_get_pull_request_reviews(owner, repo, pullNumber)` (:1764) | `id, pr_id, author_login, state, body, submitted_at, commit_id` | **yes** | usually not the deciding text |
| inline review comments | `github_get_pull_request_comments(owner, repo, pullNumber)` (:1705) | `id, pr_id, author_login, body, path, diff_hunk, line, position, commit_id, in_reply_to_id` | **no** | yes |
| conversation comments | `github_get_issue_comments(owner, repo, issue_number, limit, offset)` (:1611) | `id, pr_id, author_login, body, created_at, updated_at` | **no** | yes |
| timeline events | (not a read tool) | `id, pr_id, event, actor_login, created_at, data{commit_id}` | **no** | no |

Base shapes, verbatim from `github.json`:

```
# reviews[0]
{"id":"harmonygames-Games/GameOfDominoes#1#rev_1","pr_id":"harmonygames-Games/GameOfDominoes#1",
 "author_login":"EMPLOYEE_0025_GITHUB_USERNAME","state":"CHANGES_REQUESTED","body":"",
 "submitted_at":"2023-04-12T15:59:38Z","commit_id":null}

# review_comments[0]
{"id":"harmonygames-Games/GameOfDominoes#1#rc_1","pr_id":"harmonygames-Games/GameOfDominoes#1",
 "author_login":"EMPLOYEE_0025_GITHUB_USERNAME","body":"How is a marking that is empty work? …",
 "path":"Assets/GoD/Scripts/DominoGameplay/DominoSide.cs","diff_hunk":"@@ -0,0 +1,62 @@ …",
 "line":null,"position":null,"commit_id":null,"in_reply_to_id":null, …}
```

Four independent proofs that the review read cannot be replaced:

1. **`state` is not a field of any comment object.** `review_comments` and `pull_request_comments` rows carry
   no state key at all (schemas above). A reviewer can write "this is wrong, don't ship it" as an inline
   comment and GitHub records its container state separately; conversely a review can be
   `CHANGES_REQUESTED` with an **empty body** (`rev_1` above: `"state":"CHANGES_REQUESTED","body":""`).
   Text and state are orthogonal, so neither object implies the other.
2. **The reciprocal case is live in the cohort.** On #470, Owen Baker's two reviews are
   `{02:43:00 COMMENTED, body:""}` and `{02:50:56 COMMENTED, body:""}` — **empty bodies** — while his two
   inline comments (`#rc_3` "You want me to check for each manager on every update?", `#rc_5` "Waiting for
   one frame solve the timing issue, thanks.") carry the text and **no state**. Reading comments shows the
   words but cannot tell you whether the review was an approval or a change request; reading reviews shows
   the verdict but an empty body. Both reads are needed.
3. **The timeline cannot substitute.** All 2,116 `reviewed` timeline events in base are
   `created_at: null` and `actor_login: ""`, carrying only `data.commit_id` — e.g.
   `{"id":"harmonygames-Games/match3d#470#ev_2","event":"reviewed","actor_login":"","created_at":null,
   "data":{"commit_id":…}}`. They also **under-enumerate**: #470 has 8 timeline events of which 5 are
   `reviewed`, but **9** review rows exist. (This is R_D finding T01: never date or attribute a review from
   the timeline.) So a solver cannot even recover *how many* reviews exist, let alone their state, from any
   other call.
4. **Absence cannot be inferred from silence.** For the 6 zero-review PRs (#356 #360 #370 #396 #397 #420),
   "no reviews" is only provable by a review read returning an empty list; zero inline comments and zero
   conversation comments are consistent with *both* "no reviews" and "reviews whose bodies live elsewhere"
   (#384, #459 are exactly that pattern — a review exists with zero inline comments and only a
   `walkthrough` conversation comment). Comment silence is not evidence of review silence.

**Call accounting.** Certifying the clause costs exactly **22 `github_get_pull_request_reviews` calls**
(one per cohort PR), of which 6 return an empty set. `github_get_pull_request_comments` returns 0 or more
rows but never the state, and #438/#459/#465/#384 need a review read to prove that their many
`COMMENTED` reviews are not blockers. Grounding: `R_A_gate_contract.md:128` already binds this clause to the
`github_get_pull_request_reviews` surface, and `S7_backend_config_and_gh_tools.md:258` verifies the tool's
params — the read is genuinely necessary and genuinely sufficient.

**Non-leak corollary (important for §3).** Reading the reviews does **not** surface the design's seeded
deciding inline text: CodeRabbit review bodies are only the summary header
`"**Actionable comments posted: N**\n\n<details>…"` and human review bodies in the cohort are empty. So the
seeded inline comments stay visible only through `github_get_pull_request_comments`, and the 22 review reads
give state without giving the sentence.

---

## 3. Companion-mirror leak audit (sets an injection constraint)

### 3.1 INT-01 — GitHub → Slack `#zombie-prs` (C093LEZGF6J)

KB shape (`integrations.json` INT-01, `per_kind["Comment on pull request"]`):
`user = SLACK_BOT_0004_SLACK_ID`, `text = ""`, and `attachments[0].text = "comment/review body (comments,
reviews)"`, `pretext = "<Comment> on pull request by <login>"`, `title = "<…#N PR title>"`.

**Answer: the mirror carries the FULL comment body verbatim** (only Slack's ~3 kB attachment cap truncates
very long CodeRabbit analyses). Proof from base, matched 1:1 against `github.json`:

*Full-body inline-comment mirror, human author — the deciding-comment case.* Base Slack message
`C093LEZGF6J/1759200182.966249`:

```
ts            1759200182.966249
thread_ts     1759180973.545069      (under the "#470 Collect And Win minor bugs fixes" opened parent)
user          SLACK_BOT_0004_SLACK_ID
text          ""
attachments[0].fallback  "[harmonygames-Games/match3d] Comment on #470"
attachments[0].pretext   "<https://github.com/harmonygames-Games/match3d/pull/470#discussion_r2389703296|Comment>
                          on pull request by <https://github.com/owen.baker|owen.baker>"
attachments[0].title     "<https://github.com/harmonygames-Games/match3d/pull/470|#470 Collect And Win minor bugs fixes>"
attachments[0].text      "You want me to check for each manager on every update?"
```

and the source row `github.json review_comments`:
`{"id":"harmonygames-Games/match3d#470#rc_3","author_login":"PERSON_5877_GITHUB_USERNAME",
"created_at":"2025-09-30T02:43:00Z","path":"Assets/Scripts/UI/CollectAndWin/CollectAndWinTokenManager.cs",
"body":"You want me to check for each manager on every update?"}` — **byte-identical text**.

*Full-body conversation-comment mirror.* Base `C093LEZGF6J/1758301178.050609` (the #454 PR's own
CodeRabbit comment) carries the whole `"## Walkthrough\n\nAdds main menu icon animations in Unity: …"`
body as `attachments[0].text`, matching `pull_request_comments#454#c_1`.

*Review-body mirror (for completeness).* `per_kind["Reviewed and changes requested"].example_shape`
carries `attachments[0].text = "Streak stuff looks good. Just some coding consistency stuff."` — i.e. the
**review body** is mirrored verbatim too.

**Coverage is deterministic, not occasional.** In `slack_C093LEZGF6J_2025-09.json` there are **265 distinct
`discussion_r<id>` links** against **264 match3d `review_comments` created in Sept 2025** → effectively
**100 %** of that month's inline review comments got a full-body Slack mirror. (The KB field
`base_rates.comment_and_review_copy_rates["match3d/human"] = {github_records: 2, with_slack_copy: 0,
rate: 0.0}` is **wrong** for these two records — both Owen Baker comments are mirrored, as quoted above.
Do not rely on that rate.) KB `seeding_rule` is therefore binding in practice: *"A seeded PR
comment/review/merge inside a repo's `window` needs its Slack copy, threaded under the PR's 'opened' parent,
using the real login."* match3d window: `2025-06-30T21:35:55Z → 2025-09-30T22:33:40Z`.

### 3.2 INT-12 — GitHub → Gmail `svc_0248` (Julia CC'd / mailbox-bearing)

KB shape: `subject = "[harmonygames-Games/<repo>] <PR title> (PR #<n>)"`,
`body_first_line = "'@<login> approved this pull request.' / '<person> requested your review on: …' /
'<person> pushed N commits'"`, `message_id = "<harmonygames-Games/<repo>/pull/<n>/…@github.com>"`.
Base sample verbatim (`integrations.json` → `gmail_samples.github_notification`, mailbox
`vincent.parker@harmonygames.co`, subject `Re: [[SOURCE_ORG_0001]-Games/match3d] [PERSON_NAME_0050]/fix
effectpopups (PR #441)`):

```
body_head: "Merged #441 into main.\r\n\r\n-- \r\nReply to this email directly or view it on github:\r\n
            https://github.com/[SOURCE_ORG_0001]-Games/match3d/pull/441#event-19724818322\r\n
            You are receiving this because you authored the thread.\r\n\r\nMessage ID: <…ma"
```

**Answer: notification only — action line + link, NEVER the comment body.** Compared with INT-01 this is the
opposite shape: `attachments[0].text` (full body) exists only in Slack; the mail carries the one-line action
and a deep link. Julia's mailbox is **persona-scoped and reachable by her** (`acl.md:36-38`), so this is the
one companion where a body leak would actually be solver-visible — and the base shape does not leak.

### 3.3 Conclusion and the injection constraint

**Would a seeded mirror of the deciding comment leak its text?**

- **INT-01 (Slack `#zombie-prs`): YES, verbatim** — the mirror is defined as the body text and is written
  ~100 % of the time. A seeded deciding inline comment on #470/#370/#438, or the seeded conversation comment
  on #454, would appear **as that exact sentence** in `#zombie-prs`, threaded under the PR's opened parent.
  #454 is the sharpest case: its `c_1` mirror (`1758301178.050609`) already exists, so a new deciding
  conversation comment on #454 would sit alongside a live full-body mirror of its sibling.
  **Mitigation that already exists and must be kept:** Julia (`EMPLOYEE_0005_SLACK_ID`) is **not** a member
  of `C093LEZGF6J` (12 members: 0003, 0004, 0006, 0012, 0021, 0025, 0026, 0031, 0032, PERSON_6075,
  SLACK_BOT_0004, U04V95A7C80), and Slack reads are persona-scoped — `acl.md:79-95` ("Search operations
  search only within that visible set and do not reveal inaccessible matches"; a by-ID read "does not
  bypass the ACL") and `acl.md:103-108` ("Author god-mode … does not make author-visible evidence in any of
  the seven scoped services reachable by the Agent or verifier"). So the mirrored sentence is **inert to
  Julia and to every verifier** — but it is **not** inert to the design's own reach accounting.
- **INT-12 (Gmail): NO** — link + action line only.

**Injection constraints (bindable as rails):**

- **C-1 (must).** Do **not** seed an INT-01 `#zombie-prs` mirror for any of the three deciding inline
  comments (#470/#370/#438) or for the #454 conversation comment. Rationale to record in the manifest: base
  parity would reproduce the sentence verbatim, so suppression is the only way to keep the deciding text
  single-path. Because Julia is not a member, the omitted mirror is *invisible* to the solver, so the
  deviation is unobservable and cannot be gamed. For **#470 and #454** the deviation is additionally
  defensible on the window boundary (match3d mirrors stop at `2025-09-30T22:33:40Z`; a comment dated after
  that gets no mirror) — prefer timestamps after that instant, or state the suppression explicitly for
  #370/#438, which are inside the window.
- **C-2 (must).** Do **not** "fix" the INT-01 shape into a link-only mirror. A `pretext`-only bot post with
  an empty `attachments[0].text` contradicts the base shape (`text` = body) and would itself be a tell.
  Suppress the row; never re-shape it.
- **C-3 (must).** Never count `#zombie-prs` as a reach path for any graded fact. `R_C_carriers_ids.md` §6
  already marks `can-see` **UNVERIFIED** and calls the mirror "a companion, never evidence"; keep that
  status. A rubric may not cite a `#zombie-prs` message as its deciding source.
- **C-4 (may).** INT-12 Gmail notification mails are safe to seed for any cohort PR (they leak only the PR
  title and an action verb) and are a legitimate *extra* path for "which PRs merged and when" — but they
  must never be seeded with a body, and they must not be the sole path for any graded value.
- **C-5 (must).** The seeded deciding inline comments must land in `review_comments` (visible only via
  `github_get_pull_request_comments`), not in `reviews.body` — review bodies are read by the 22
  `github_get_pull_request_reviews` calls, so putting the deciding sentence there would collapse the
  review read and the deciding read into one call and destroy the §2 necessity.
- **C-6 (must).** The #454 conversation comment must be a `#c_N` **above** `#c_1`'s collision range — see
  `R_C_carriers_ids.md` §1: on #470 the `#c_N` suffix collides with `pull_request_commits` ids
  `#c_0…#c_5`. If the deciding conversation comment goes on #454, use `#c_2` and record the overlap; every
  `#c_N` needs its `#ev_N` `commented` timeline event (884/884 in base) and a bumped PR `updated_at`.

**Net answer for the design:** (a) **none** of the 22 carries an unresolved CHANGES_REQUESTED → the clause
is a clean certify-absence check that grades *coverage of 22 review reads*, not any held beat; (b) the
review read is **necessary** (state lives only there, timeline is null-dated and under-enumerating, comments
carry no state); (c) **INT-01 mirrors carry full bodies verbatim, INT-12 mails do not** → seed no Slack
mirror for any deciding comment, and rely on Julia's non-membership only as a second line of defence,
never as the primary one.

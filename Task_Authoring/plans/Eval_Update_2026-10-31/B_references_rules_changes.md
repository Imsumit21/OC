# B — references/ rules, schema, persona: changes from current to new

Scope: `Evals/references/**` (OLD) vs `Eval-new/Evals/references/**` (NEW). Read-only
comparison by `cmp`, `diff -u`, `shasum -a 256`, and `python3 -c` JSON comparison keyed by
case id / file path / column name. Index blobs (`search_indexes/`, `id_indexes/`) ignored
per scope; only their routing keys are reported. `Evals/tools/**`, top-level `Evals/*.md`
and `claude/` are another agent's scope.

## Summary

1. **Two universes and two clocks (headline).** NEW `universes/{normal,synthcut}/` replaces
   the single `universe_manifest.json` + `source_layout.json` + indexes. Normal = Feb 14 2026
   `00:00 UTC`; SynthCut = Oct 1 2025 `00:00 PT` (`07:00 UTC`). Every reference that stated
   one fixed clock now states "the task's clock" — authors must pick the date first.
2. **Linear injection is stricter and gained a required column.** `linear_issues.state_history_json`
   is NOT NULL with no default (`[]`), and every Linear timestamp/date column now documents a
   strict text format; `::timestamptz`/`now()`/`+00:00` break the Linear load.
3. **Two columns are database-generated.** `gmail.gmail_messages.body_text_fts` and
   `slack.slack_messages.text_fts` must be omitted from INSERT lists and never UPDATEd.
4. **NEW `schema/id_contracts.json`.** Gmail `history_id` must be digits-or-NULL; Drive
   `content_path` must be `<owner_email>/<path>` with no leading `/` and no `root/` prefix.
   Enforced by `hg_injection_lint.py` Check A.
5. **Overly Broad flips Moderate → Major** in every rule file (rubric severity, Overall
   Quality, Specificity boundary, common_errors counts table). One broad row now fails a rubric.
6. **Narrow non-fail bands are restored for rubric scoring:** Minor 5–10% = NON-FAIL 3;
   weights ≤10% one level off = NON-FAIL 4; exactly one missing ordering check = NON-FAIL 3;
   "The Agent's …" titles ≤10% = NON-FAIL 3.
7. **Do-nothing rows now fail Negative Criteria.** Any row an idle Agent passes
   ("leaves X as found", "keeps X off Y") fails, however worded; it must become a count/scope
   condition on a required write, or a requirement inside a required artifact.
8. **Rubric scoring record format 4 → 5:** adds per-row `valid_case` and `do_nothing_case`,
   a set-level `final_reply_test`, source `reachability`, and `oe_cross_check` with OE-conflict
   routing (`FIX_ROW` / `FIX_OE` / `oe_send_back`).
9. **Prompt Contrived failures expanded and one flag removed:** staged typos, trap hints/riddles,
   hidden destinations, audit/compliance form wording and long if-chains now FAIL; the
   "AI-text uniform capitalisation" flag is **removed** — clean, correctly spelled writing is
   not a defect.
10. **`BOTH_FAIR_FIGURE` is a new narrow UGT PASS** for one differing reported figure when all
    five authority checks stay unsettled and decision/writes/destinations are identical.
11. **OE review gains an `expected_values` value ledger** covering every value and absence word
    on an `Expected:` line, plus 2 calibration cases (#7 wrong event key, #47 refuted absence).
12. **Persona ACL: Gmail and Slack attachments return no readable content.** Evidence that exists
    only inside a Gmail/Slack attachment is not reachable; Linear/Drive/Trello(42/106) do ship bytes.

## Change log

### B-01 Two universes selected by task date, each with its own clock
- Files: `Eval-new/Evals/references/universes/README.md:1-41`; `YOUR NEW universes/normal/universe_manifest.json:4-6`; `Eval-new/Evals/references/universes/normal/universe_manifest.json:4-7`; `universes/synthcut/universe_manifest.json:4-10`; `Eval-new/Evals/references/README.md:7,12` (`Evals/references/README.md:7-12`); `rules/manifest.json:121-122` (`rules/manifest.json:120`)
- Category: universe-date
- Old → New: one undifferentiated universe at `2026-02-14 00:00`. New: `normal/` = `2026-02-14 00:00 UTC` (`Universe_Normal/`, `hg4-2026-08-31-v37` v37, 16.5 GB archive); `synthcut/` = `2025-10-01 07:00 UTC (2025-10-01 00:00 PT)` (`Universe_SynthCut/`, `hg4-synth-sep30cut` v16). A new `dual-universe-v1` adaptation says the date is "asked first and saved as the `universe` input (no default)". Reports show a Clock line.
- Authoring impact: **scenario** — the design must pin one universe/date up front and every date, deadline, cutoff, "today/yesterday" and shutdown premise follows that clock; the Feb 11 2026 shutdown premise applies to Feb 14 tasks only, departed people (Victor, April 2025) apply to both, and on Oct 1 nothing after `2025-09-30 23:59:59 PT` may exist. **injection** — every inserted timestamp must sit before the chosen clock and inside the chosen archive's coverage. **reference-files** — pick the matching universe folder. **prompt / humantime / oracle-events / rubric / allfail / difficulty / hardening** — read the clock from the saved input, not from a constant; a Feb-14-only storyline drafted for an Oct-1 task (or vice versa) is a pre-run FAIL, not a 3.
- Severity: BLOCKING

### B-02 Per-universe references move; collection routing is unchanged
- Files: `Eval-new/Evals/references/README.md:12-14` (`Evals/references/README.md:11-13`); `Eval-new/Evals/references/universes/README.md:15-26`; OLD `Evals/references/universe_manifest.json`, `Evals/references/source_layout.json` no longer exist
- Category: universe-date
- Old → New: `references/{universe_manifest.json,source_layout.json,search_indexes/,id_indexes/}` → `references/universes/{normal,synthcut}/{universe_manifest.json,source_layout.json,search_indexes/,id_indexes/}`. Service export filenames and array pointers are **identical** between OLD and NEW-normal and between normal and synthcut (all 13 services, 17 entries checked): `github data.json` with `/users,/repositories,…,/issues`; `gmail users.json|labels.json|threads/*.json(/messages)`; `slack emojis|channels|users|files.json|messages/*.json`; `trello data.json` 10 pointers; `confluence confluence_working.json` 7 pointers; `snowflake snowflake.json` `/databases,/schemas,/tables,/query_history`; `gsheets data.json` `/sheets_spreadsheets`. `hg_reference.py routes` therefore still resolves the same way; only the folder root and the SHA-256 pins changed. `packaging` and the large `internal_metadata` block (universe id, 76 scenarios, artifact counts) were dropped from `universe_manifest.json`.
- Authoring impact: **scenario / injection** — any hardcoded `Evals/references/source_layout.json`, `references/search_indexes/...` or `references/universe_manifest.json` path in a design note, dossier, manifest or solver must be rewritten to `references/universes/<universe>/...`. **reference-files** — the flat folder must ship the chosen universe's indexes, not the old ones. The export filenames and array pointers an author relies on did not change, so no route redesign is needed.
- Severity: BLOCKING

### B-03 Gmail thread `shape_sample` routing hint changed to a placeholder
- Files: `Eval-new/Evals/references/universes/normal/source_layout.json:89` (`Evals/references/source_layout.json:87`); `universes/synthcut/source_layout.json:89`
- Category: universe-date
- Old → New: `"shape_sample": "threads/marcus@harmonygames.co_1808827352855849383.json"` → `"shape_sample": "threads/00000000.json"`. Thread file naming, `threads/*.json` glob and `array_pointers: ["/messages"]` are unchanged; only the example path changed. Slack's `messages/*.json` sample stayed `messages/D07GGG4M3DK/2024-08.json`. I did not verify whether `threads/00000000.json` exists in the new archive (data folders out of scope), so treat it as a placeholder hint, not a record to open.
- Authoring impact: **oracle-events / reference-files** — any OE step or solver that copied the OLD sample thread filename as a concrete target must re-select the real record from search; do not cite `threads/00000000.json` as evidence.
- Severity: MINOR

### B-04 `linear_issues.state_history_json` is a new required NOT NULL column
- Files: `Eval-new/Evals/references/schema/injection.json:2957-2964` (OLD had no such column; `linear_issues` ended at `position: 26`)
- Category: injection
- Old → New: `linear_issues` had 26 columns; NEW adds `"type": "text", "column": "state_history_json", "default": null, "nullable": "NO", "position": 27` with `"note": "Required by the live platform database (missing from the original schema dump; added 2026-10-22 after platform errors \"null value in column state_history_json violates not-null constraint\"). JSON array text; use '[]' for a new issue."`.
- Authoring impact: **injection** — every `INSERT INTO linear.linear_issues` must name `state_history_json` with `'[]'` (or a real history array) or the load fails with a NOT NULL violation; `/injection` lint and the solver must include it. **oracle-events** — any OE step creating a Linear issue must be able to satisfy the column; do not design a create-issue path that omits it.
- Severity: BLOCKING

### B-05 Linear text timestamps and dates must be written in one exact format
- Files: `Eval-new/Evals/references/schema/injection.json:2743,2752` (`linear_comments`), `2865,2874,2883,2892,2901` (`linear_issues`), `3033,3042,3065,3074` (`linear_projects`), `3110` (`linear_team_memberships`), `3160,3169` (`linear_teams`), `3226,3235` (`linear_users`)
- Category: injection
- Old → New: nullable/position metadata only → adds `"format": "iso_utc"` on `created_at`/`updated_at`/`started_at`/`completed_at`/`canceled_at`/`archived_at` and `"format": "date"` on `due_date`/`start_date`/`target_date`, each with a note: "write exactly `YYYY-MM-DDTHH:MM:SSZ` in UTC (e.g. `2025-09-30T14:12:09Z`) … Any other form (a space, `+00`, `+00:00`, milliseconds, a `::timestamptz` cast or `now()`) is stored as written and the agent run then fails to load Linear (`cannot parse timestamp`)". Dates: "write exactly `YYYY-MM-DD` (e.g. `2025-10-03`) … anything else fails the Linear load."
- Authoring impact: **injection** — ban `now()`, `::timestamptz`, `+00:00`, fractional seconds and bare dates in timestamp columns; emit literal `2025-09-30T14:12:09Z`-shaped text. Note the synergy with B-01: the example literal is pre-Oct-1, so synthcut inserts must stay ≤ `2025-09-30T23:59:59Z`. **oracle-events** — any expected Linear value must match the stored text exactly, including the `Z`.
- Severity: BLOCKING

### B-06 FTS columns are generated: omit from INSERT and never UPDATE
- Files: `Eval-new/Evals/references/schema/injection.json:2242-2247` (`gmail.gmail_messages.body_text_fts`, NEW `:2246`), `:3787-3792` (`slack.slack_messages.text_fts`, NEW `:3791`)
- Category: injection
- Old → New: plain nullable column with a position → adds `"generated": "always"` and `"note": "computed by the database from the message body; leave it out of INSERT column lists and never UPDATE it (it fills itself)"` (Slack: "computed by the database from text").
- Authoring impact: **injection** — injected Gmail messages and Slack messages must not list `body_text_fts`/`text_fts` in column lists and must not set them in UPDATEs; relying on them for search after injection is also unsafe (the DB fills them, so do not assert their value). **oracle-events** — do not grade the FTS column value.
- Severity: IMPORTANT

### B-07 NEW `id_contracts.json`: Gmail `history_id` and Drive `content_path`
- Files: `Eval-new/Evals/references/schema/id_contracts.json:1-28` (new file); registered at `Eval-new/Evals/references/schema/README.md:10`; pinned in `prompt_rubric_release.json:101`
- Category: injection
- Old → New: no such file. NEW defines two supported ID contracts, "Enforced statically by `Evals/tools/hg_injection_lint.py` (check id_contract)": (a) `gmail_history_id` — tables `gmail.gmail_messages/gmail_threads/gmail_users`, column `history_id`, `allow_null: true`, `pattern: "^[0-9]+$"`; "labels such as `hf_pf_reg_1` break Gmail search", with failure evidence from task `6aa8272b1b7a2df0fc0fea7b` where every Gmail search errored. (b) `drive_content_path` — `gdrive.drive_files.content_path`, `allow_null: true`, `pattern: "^(?!/)(?!root/)[^/]+/.+$"`, `first_segment_equals: "owner_email"`; "NULL means the file has no bytes"; failure evidence from `6abd857f96a9f77c7e518348` where a `root/...` path returned 404. Fields not listed keep the older "numbering gap or few examples is not an invalid-ID finding" rule.
- Authoring impact: **injection** — if a task injects a Gmail `history_id` at all it must be digits only; injected `gdrive.drive_files.content_path` must be `<that row's owner_email>/<path>`, never `/...` or `root/...`. `sql_lint`/`base_check` will not catch this; `hg_injection_lint.py` check `id_contract` will. **reference-files / oracle-events** — a reference attachment or OE step that expects the agent to open a Drive file must point at a path of that shape, or the read 404s and the step is infeasible. **scenario** — do not design a trap that depends on a malformed ID; it now fails lint rather than trapping the agent.
- Severity: BLOCKING

### B-08 Injection schema manifest re-pinned; table count unchanged
- Files: `Eval-new/Evals/references/schema/manifest.json:15` (`Evals/references/schema/manifest.json:15`)
- Category: injection
- Old → New: `sha256` `885982066ac6…` → `01ef57923621…` (matches the new `injection.json`, verified with `shasum -a 256`). `table_count: 58`, the schema list, `snowflake` `column_count: 454` and all limitation strings are unchanged, even though `linear_issues` gained a column. `snowflake.json` is byte-identical.
- Authoring impact: none new — the manifest is bookkeeping. Do not read `58 tables` as "column set unchanged": use `injection.json` for columns (see B-04).
- Severity: NONE

### B-09 Overly Broad is now Major, not Moderate
- Files: `Eval-new/Evals/references/rules/qc_rubric_v10.md:16-17` (`:16`); `rules/qc_rubric_v10.md:104-107,177` (`:99-101,167`); `rules/scoring.json:204` (`:204`), `:278` (`:278`); `rules/review_scoring.md:86` (`:70`); `rules/scoring_notes.md:168` (`:168`); `rules/common_errors.md:243` (`:240`)
- Category: rubric
- Old → New: "Overly Broad is Moderate." → "Overly Broad is Major (2026-10-17), the same level as Overly Specific. Never repair an overly broad row with a count, format or phrasing; name the value." Moved from the Moderate severity list to the Major list in `qc_rubric_v10.md`, and the counts table row changed to `Overly broad | 45 | Major (2026-10-17)`. The plausible-path exception is preserved.
- Authoring impact: **rubric** — a single broad row (a plausible wrong answer can pass) now **fails** the rubric outright instead of costing one Moderate; every acceptance rule must name the exact value/set, and an "or similar" style escape hatch is a FAIL. **create-rubric-writing** weight/acceptance plan should treat broadness as its top acceptance risk after Overly Specific. **hardening** — an attributed `overly_broad` finding is now a hard FAIL, not a band-3 deduction.
- Severity: IMPORTANT

### B-10 Narrow NON-FAIL bands restored for rubric quality, weights, process and Agent-centric
- Files: `Eval-new/Evals/references/rules/scoring.json:206,213,227,234` (`:206,212,227,234`); `rules/qc_rubric_v10.md:137-149` (`:129-140`); `rules/review_scoring.md:68-75` (`:56-61`); `rules/common_errors.md:17,229-231,249-257` (`:17,227-229,246-253`)
- Category: scoring-thresholds
- Old → New: "N/A (2026-10-05). … fails / Any weight disagreement / One invalid Process row … fails / A nonstandard Agent form fails" → four explicit bands: (a) Overall Quality "Minor issues on 5-10% of rows are NON-FAIL 3; any Major or Moderate, or Minor on more than 10% of rows, fails"; (b) Criteria Weights "NON-FAIL 4 only when 10% or fewer rows are one level off and none are two levels off"; (c) Process "exactly one genuinely missing ordering check is NON-FAIL 3; two or more, or any invalid Process row, fails"; (d) Agent-Centric "off-pattern but agent-centric titles on 10% or fewer rows are NON-FAIL 3". `common_errors.md` now lists the narrower cases as bands instead of hard fails.
- Authoring impact: **rubric** — small slips (a handful of one-level-off weights, one missing ordering row, a few "The Agent's …" titles) cost 3/4 rather than a FAIL, so effort should go to the zero-tolerance items instead: any Major, any Moderate, two predicted all-fail rows, zero Outcome rows, an invalid Process row, a non-Agent subject, a tool name, or any do-nothing/prohibition row. **difficulty / hardening** — a rubric that lands 3 on these bands is still a pass gate; do not treat them as automatic rework.
- Severity: IMPORTANT

### B-11 Do-nothing rows fail Negative Criteria; prohibition rewrites must target a write
- Files: `Eval-new/Evals/references/rules/rubric_checks.md:157-166,184-186`; `rules/qc_rubric_v10.md:20-22,69-75` (`:19-21`); `rules/scoring.json:239-240` (`:239`); `rules/common_errors.md:88,326-334` (`:86,319-327`); `rules/rubric_flow_v2.md:32-35,105-109,124-125`; `rules/rubric_qc_examples.md:84`
- Category: rubric
- Old → New: rewrite guidance was "rewrite it as a preserved state (The Agent leaves ENG-123 open) or scope boundary" → "rewrite it as a condition on a write the Agent must make (an exact count or scope), or a requirement inside a required artifact. Never a standalone row an Agent passes by doing nothing." NEW `do_nothing_case: {result, reason, quote}` must REJECT, with `quote` the exact title text of a write an idle Agent never produces ("records the close-out total of $1,570.00 on ENG-2558"); an ACCEPT is classified `negative: PROHIBITION` and fails. The worked example flipped: BAD "The Agent does not close ENG-123" and also "The Agent leaves ENG-123 open"; GOOD "The Agent closes exactly three of the leftover reviews." Calibration: task `…eccb` C26 ("leaves Arthur's Close-out chores spreadsheet … as found") and C52 failed; C47 and C32 are valid because an idle Agent fails them.
- Authoring impact: **rubric** — every preserved-state row ("leaves X open", "keeps X off Y", "does not touch Z") must become a count/scope condition on the required write or a required-artifact requirement, and the row must name a concrete produced value. This is the single most common rewrite in the new bundle. **create-rubric-writing** must plan a `do_nothing_case` per row, and **rubric check** must reject a `do_nothing_case` ACCEPT. **hardening** — an idle-agent-passable row is a hard Negative Criteria FAIL, so a hardening pass should hunt these first.
- Severity: BLOCKING

### B-12 Rubric scoring record format 4 → 5 with new required fields
- Files: `Eval-new/Evals/references/rules/review_scoring.md:10-11,19-20,43-52` (`:10,18-19`); `rules/rubric_checks.md:3,13-21,147-186` (`:3,13-16,122`); `rules/rubric_review_record.md:7-8`; `rules/rubric_flow_v2.md:19,32-35`
- Category: report-format
- Old → New: `format_version: 4` → `5`, described as "2026-10-17: per-row `valid_case` and `do_nothing_case`, `final_reply_test`, source `reachability` and `oe_cross_check`". New required pieces: `checks.sources[].reachability` ∈ `PROMPT_LINKED|TRASH|ATTACHMENT_ONLY|UNLINKED` (a non-`PROMPT_LINKED` source leaves the claim unresolved and needs an `unobservable` issue); `valid_case` (`{example,result,reason}` built from what the prompt actually asks — "keep it short" allows any line count; REJECT requires `overly_specific`, `incorrect` or `unauthorized`); `final_reply_test` (`{example,authority,result,rejecting_rows,reason}`); `oe_cross_check` (`oe_present`, `steps`, `rows[].oe_step_ids` with `oe_unmapped` → `unmapped: {resolution: ROW_DEFECT|OE_GAP|UNRESOLVED}`, and `conflicts[]` with `resolution: FIX_ROW|FIX_OE|UNRESOLVED`; `OE_GAP`/`FIX_OE` return as `oe_send_back`). A stale pre-2026-10-17 ledger forces `FULL` mode.
- Authoring impact: **rubric** — the rubric author must be able to answer, for every row, a valid alternate answer the prompt allows, an idle-agent result, and which OE step reaches the row; a row with no OE step is an `oe_unmapped`/`ROW_DEFECT` defect. **oracle-events** — step labels become a cross-checked contract: a rubric row that references a step the OE does not have is reported back as an OE gap, so OE step ids must be stable and complete. **hardening / difficulty** — an old-format ledger cannot be reused; expect a full re-review.
- Severity: IMPORTANT

### B-13 `valid_case` punishes over-narrow "format lock" rows; `pt_or_utc_date` and anonymized tokens bind to LITERAL
- Files: `Eval-new/Evals/references/rules/rubric_checks.md:147-150`; `rules/rubric_factual_checks.md:31-34,86-107,122-131` (`:31,86-95,108-115`); `rules/rubric_qc_examples.md:85-86`; `rules/deep_recheck.md:85-88`
- Category: rubric
- Old → New: NEW `DATE` variant `pt_or_utc_date` — "matches the source instant's UTC day or its America/Los_Angeles day. When those days differ, the row must state both (one claim per day on the same selection); stating only one is `overly_specific`". NEW rule that "ID-shaped title tokens (snake_case event or field keys such as `quest_completed`, prefixed record IDs, ticket keys, Slack-style and long hexadecimal IDs) and anonymized tokens are treated like numbers: each needs a LITERAL claim … SEMANTIC cannot bind them." NEW anonymized-token rule: a LITERAL quote of a real name against a source showing `[PERSON_NAME_0854]` is `anonymized_token` → `overly_specific` or `incorrect`. Calibration: `…df2ec` R2 ("at most five other lines") rejected a valid compact reply; `…fea7a` "276 MB on November 17, 2025" is 2025-11-16 16:58 PT, so a one-day row is `overly_specific`; `…fea90` `quest_completion` vs `quest_completed` is `incorrect`.
- Authoring impact: **rubric** — (a) do not lock line counts, sentence counts or formatting the prompt does not state (that is now a demonstrable `overly_specific` FAIL); (b) a date the answer reports for an instant must accept both the PT and the UTC day when they differ; (c) every event key, ticket key and long hex ID in a title needs an exact LITERAL source quote, and any name the tools show as a token must be accepted as the token. **oracle-events / scenario** — prefer record values whose PT and UTC days agree, or design the accepted set to carry both; avoid anonymized tokens as the deciding value unless a persona-visible mapping exists.
- Severity: IMPORTANT

### B-14 Prompt Contrived failures expanded; AI-text capitalisation flag removed
- Files: `Eval-new/Evals/references/rules/scoring.json:89-90,164-167` (`:89,164`); `rules/common_errors.md:17,49,68,150-155,171-175,204,278-281` (`:17,45,64,146-152,168-172,204,244-247`); `rules/deep_recheck.md:12-14,259-266,274-281` (`:12,234,242-245`); `rules/prompt_qc_examples.md:17-21,67-78`
- Category: prompt
- Old → New: "An LLM-sounding prompt (uniform capitalisation and punctuation, document formatting, enumerated deliverable specs) is scored here" → the capitalisation half is **deleted**; NEW read: "An LLM-sounding prompt (document formatting, enumerated deliverable specs) is scored here. Clean, correctly spelled writing is not a defect (2026-10-17). Staged typos, made-up emoji or deliberately broken punctuation, a hint or riddle aimed at the trap, a hidden destination the persona would know, audit or compliance-form wording, and long if / but-not / then-also chains are contrived (2026-10-17)." Two worked examples flipped: the GOOD "If a leftover review already has an owner, comment on it and leave it open. If it never shipped …" is now BAD ("A chain of if / but-not / then-also clauses in the prompt fails Contrived"), replaced by "Can you sort out the leftover reviews before Friday? Arthur posted how he wants each kind handled."; the GOOD "If my date or channel is off, use the message that is actually there" is now BAD ("A line telling the agent the prompt may be off hints at the trap").
- Authoring impact: **prompt** — write one plain request in the persona's own voice: no staged misspellings or fake emoji, no sentence that points at the trap ("the thing that actually bites us is not on anybody's list"), name the destination the persona would know (`#winddown`) instead of "wherever that's been asked for", put per-case rules in a seeded record instead of an if-chain, and drop audit verbs ("apply it to the cohort, reconcile, classify, rank, complete the review artifacts"). Do not add plausibility hedges that let the record correct the prompt. Correct spelling is now safe, so do not add fake errors for realism. **humantime** — the persona-voice transcript must match this style. **hardening** — these are new FAIL classes with calibration cases.
- Severity: BLOCKING

### B-15 `BOTH_FAIR_FIGURE` is the only PASS for an unsettled single-figure fork
- Files: `Eval-new/Evals/references/rules/prompt_rubric_reliability.md:168-181`; `rules/scoring.json:57` (`:57`); `rules/deep_recheck.md:113-118,171,197-206` (`:101-110,153,182-190`); `rules/common_errors.md:47-50`; `rules/prompt_qc_cases.json:755-775`
- Category: prompt
- Old → New: no such outcome. NEW `BOTH_FAIR_FIGURE` "is the only PASS for a fork no source settles" and needs decision, writes and destinations `SAME` in both readings, contents `DIFFERENT`, no `authority_chain`, `delegation_basis: NOT_CLAIMED`, and a `figure` object: `kind` ∈ `AMOUNT|COUNT|RATE|DATE`, one fork per `label`, exactly two `values` (leading reading first) each with `reading_id, value, evidence, derivation` where `evidence` quotes a visible primary record other than the prompt and `derivation` is required when no quote contains the value, plus `checks` with all five checks set `{settles: false, reason}` and `asks_completed`/`next_step_unchanged`. The rendered report prints `Rubric must accept: X or Y`. Calibration #50: 32.8% vs 28.5%, recorded `BOTH_FAIR_FIGURE`, "Rubric must accept: 32.8% or 28.5%"; calibration #49 shows the label is **rejected** when a newer source settles the figure.
- Authoring impact: **prompt** — a prompt may leave exactly one reported figure open only if every other element (set, recipients, writes, destinations) is identical; it must not add a "go with the most recent" sentence, which settles the fork and forbids the label. **oracle-events / rubric** — the OE must record both values and their records, and the rubric must accept either; a single-value criterion on a both-fair figure is `overly_specific`. **hardening** — do not convert a genuine both-fair figure into a UGT finding.
- Severity: IMPORTANT

### B-16 Prompt truthfulness: Feb 11 shutdown and departed-person premises
- Files: `Eval-new/Evals/references/rules/deep_recheck.md:259-266` (`:234-241`); `rules/common_errors.md:204` (`:204`); `rules/prompt_qc_cases.json:739-753`
- Category: prompt
- Old → New: "Nothing the prompt treats as already done sits after 2026-02-14 00:00 UTC" → task clock, plus NEW premise rules: "On a Feb 14 task, a premise that the company still runs normally after the February 11, 2026 shutdown announcement is a false premise. On either date, a premise that a person who has left reviews, approves or replies is a false premise (Victor left in April 2025). On an Oct 1 task, a premise that relies on anything first appearing after 2025-09-30 23:59:59 PT is false; business as usual is not." Calibration #43 fails for "Victor said his current art-canon handoff control has the review rules."
- Authoring impact: **scenario / prompt** — do not stage a departed person (Victor, April 2025) as an active reviewer/approver, and on a Feb 14 task do not stage business-as-usual work after 2026-02-11 without acknowledging the wind-down; on an Oct 1 task, nothing may presuppose post-2025-09-30 content. **injection** — no post-clock activity for a departed person. A single loose factual slip is a FAIL, not a 3.
- Severity: IMPORTANT

### B-17 OE review gains an `expected_values` ledger for Expected lines
- Files: `Eval-new/Evals/references/rules/oracle_events.md:81-99`; `rules/oracle_events_qc_examples.md:39-57`
- Category: oracle-events
- Old → New: no such ledger. NEW `expected_values` is "the value ledger for Eval 2 §2.4 (golden-audit G3, ported)": an Expected line is the text after `Expected:` or after "The agent finds" when unlabelled, up to a blank line / heading / next label; each entry has `step_id`, `oe_quote` (covers every value inside it), `reason`, plus `not_a_claim: true` or a result: `VERIFIED` (`source_ids` whose anchors hold every ID, event name, field value, channel, SHA and version character for character; figures match once thousands separators are dropped or a `calculation` is recorded; absence wording "none/never/nothing/no later commit" needs an ABSENCE `evidence_check` unless the quote repeats a record's own three-plus words), `INACCURATE`/`MINOR` (`source_value` or `counterexample`; INACCURATE = `WRONG_EXPECTED_DATA` and fails Accuracy), `UNRESOLVED`. "The validator lists every value and absence word on Expected lines. Any that no entry covers is unresolved." Registered rubric/golden/OE files are never sources.
- Authoring impact: **oracle-events** — every number, count, date, ID, channel, SHA and version on an `Expected:` line must be quotable character-for-character from a cited source, or carry a recorded calculation/derivation; an absence claim ("none of the 33 …", "no later commit") needs a scoped ABSENCE evidence check or a record's own wording, or it is unresolved and the review cannot score. Prefer repeating the record's own words. **rubric** — a criterion value that the OE cannot ledger is an OE gap, not a rubric pass.
- Severity: IMPORTANT

### B-18 OE calibration cases added (#7 wrong event key, #47 refuted absence)
- Files: `Eval-new/Evals/references/rules/oracle_events_qc_cases.json:715-733,734-753` (`footer` did not exist; `cases` had 39 flags); `rules/oracle_events_qc_examples.md:39-57` (`:36-46`)
- Category: oracle-events
- Old → New: the 39 historical flags (31 tasks, 32 pairs, 30 accuracy / 9 completeness) are **byte-identical** and `counts` is unchanged. NEW adds `calibration_source` (Kelvin task-quality review, 2026-10-17, with file SHA pins) and exactly 2 `calibration_cases`: #7 `EXPECTED_DATA` — Expected says a quest logs `quest_completion`; the handler that fires logs `quest_completed` (`AnalyticsManager.cs:849-856`), the declaring method has no caller → INACCURATE with `source_value quest_completed`, Accuracy FAIL 2, "Quote the call site, not the declaration." #47 `ABSENCE_AND_DESIGN` — "none of the 33 flagged pull requests shows a later commit …" is refuted (24 of 99 Critical comments end "✅ Addressed in commit X"; `b254afcc` fixes Combo-Fighters #18) → INACCURATE with a counterexample; a DIRECT quote of the injected register policy is rejected.
- Authoring impact: **oracle-events** — never derive an expected value from a declaration, config or policy document when a call site or live record exists; for an absence claim, search the whole population first, including attachment-borne evidence where readable (see B-19), and record the counterexample scope. Two identical failure modes are now regression-tested.
- Severity: IMPORTANT

### B-19 Persona ACL: Gmail and Slack attachments return no readable content
- Files: `Eval-new/Evals/references/persona/acl.md:52-62` (`:49`); visibility rows `acl.md:38-39` (`:38-39`)
- Category: persona-acl
- Old → New: Gmail "…and attachments" → "…and attachment names and metadata"; Slack "…files, and related records" → "…file names and metadata, and related records". NEW note (2026-10-17): "Gmail attachment reads return no bytes (`no_attachment_root_configured` in the HarmonyGames runs), although the local export keeps the files under `root/attachments/`. Slack file records carry no content (`content_path` and `content_inline` are null on all 53,422 records). Linear attachments (2,027 files) and Drive-family files ship real content; Trello ships bytes for 42 of its 106 attachments. Evidence that exists only inside a Gmail or Slack attachment is not readable by the Agent as content." `roster.json` (17 personas) and `persona/manifest.json` are byte-identical.
- Authoring impact: **scenario / injection / reference-files** — never put a deciding fact only inside a Gmail or Slack attachment; if a trap needs an unreadable-but-visible artefact, make it a decoy, not the answer. Drive/Linear attachments remain valid evidence; Trello attachment reads are unreliable (40 of 106 have no bytes). **rubric** — a criterion citing a Gmail/Slack attachment is `ATTACHMENT_ONLY` reachability → `unobservable` (see B-12). **oracle-events** — an OE step that reads a Gmail/Slack attachment is infeasible.
- Severity: BLOCKING

### B-20 Stale `persona/manifest.json` ACL hash
- Files: `Eval-new/Evals/references/persona/manifest.json:15-17` (unchanged from OLD; OLD `:15-17`); compare `Eval-new/Evals/references/prompt_rubric_release.json:14`
- Category: other
- Old → New: `persona/manifest.json` still records `"path": "acl.md", "bundled_sha256": "19f0609f4974c001cf3e9d652d581486ca647e666b5be4037711292a02953dfb"`, which is the **OLD** `acl.md`. The NEW file hashes to `e9bca2b35f98d5ef5f64d745996a5ce81856230b442c9c38e0114aeb04468c9f` (`shasum -a 256`), and `prompt_rubric_release.json:14` correctly pins the new value. `source_sha256` (`d63ca664…`) and `updated_at_utc` (2026-09-29) were also not refreshed.
- Authoring impact: none directly — task authoring reads `acl.md`, and the operative pin is the release file. Flag for bundle maintenance: a validator that recomputes `bundled_sha256` would report the persona manifest stale; if two files pin the same source, they disagree in this bundle. Not something authoring can fix inside its own artifacts.
- Severity: MINOR

### B-21 Reference package README and schema README re-pointed to universes
- Files: `Eval-new/Evals/references/README.md:7,12-14,53` (`:7,11-13,51`); `Eval-new/Evals/references/schema/README.md:10` (`:7-9`)
- Category: other
- Old → New: `source_layout.json` / `search_indexes/manifest.json` rows → `universes/<normal|synthcut>/` plus `universes/*/source_layout.json` and `universes/*/search_indexes/` and `id_indexes/` rows, with "Tools pick the folder from the saved task date (`tools/hg_universe.py`)". "…use `../SEARCH.md` for local search commands and `universe_manifest.json` for archive provenance" → "…the task universe's `universe_manifest.json`". `schema/README.md` gains the `id_contracts.json` row.
- Authoring impact: **scenario / injection / rubric** — any doc, dossier or manifest that cites these reference paths must use the universes form (see B-02). Nothing else changes.
- Severity: MINOR

### B-22 Tools reference README clock follows the task date
- Files: `Eval-new/Evals/references/tools/README.md:35-36` (`:35`)
- Category: tooling-cli
- Old → New: "The fixed evaluation clock remains `2026-02-14 00:00 UTC`." → "The fixed evaluation clock is the task date's: `2026-02-14 00:00 UTC` for Feb 14 tasks, `2025-10-01 00:00 PT` for Oct 1 tasks (`../../ENVIRONMENT.md`)." All 15 `*-tools.json` catalogs and `tools/catalog.json` / `tools/manifest.json` are byte-identical, so the tool surface an author plans against is unchanged.
- Authoring impact: **scenario / oracle-events** — plan tool calls against the same catalog as before; only the clock reasoning in this README changed. No new or removed tool, parameter or service.
- Severity: MINOR

### B-23 Scoring notes and the rubric rubric-quality note now cite the Local Overrides
- Files: `Eval-new/Evals/references/rules/scoring_notes.md:86,168` (`:84,167`); `rules/qc_rubric_v10.md:137-149` (`:129-140`); `rules/review_scoring.md:68-75` (`:56-61`); `rules/rubric_review_record.md:7-8`
- Category: scoring-thresholds
- Old → New: the fixed date paragraph, the Overly Broad severity and the "no non-fail band" statements now point at the task clock and at "the rubric-flow-v2 bands in the Eval 3 Local Overrides (2026-10-09)". `rubric_review_record.md` (a disabled CREATE writer) notes its per-row `valid_case` and whole-set `final_reply` test "now live in the format-5 scoring record".
- Authoring impact: **rubric** — when a band question comes up, the authority is the Local Overrides text quoted in `qc_rubric_v10.md` / `review_scoring.md`, not the older "no band" prose. No separate action beyond B-10 and B-12.
- Severity: MINOR

### B-24 Prompt calibration cases added (15) and rubric calibration table added
- Files: `Eval-new/Evals/references/rules/prompt_qc_cases.json:545-793` (OLD file ended at `cases`; `:1-539`); `rules/prompt_qc_examples.md:17-21,67-78`; `rules/rubric_qc_examples.md:77-88`
- Category: prompt
- Old → New: the 25 historical prompt cards (24 tasks, 29 criterion flags, 10 fail flags) are **byte-identical** and `counts` is unchanged. NEW adds two source pins (`Kelvin Task Quality Flags 2026-10-17/ANALYSIS.html`, `…/task_quality_lessons_v2_with_run_links.html`) plus `calibration_scope` and 15 `calibration_cases` (9 TASK/FAIL, 6 CONTROL/PASS, 9 distinct tasks) keyed by `rule`: `staged_errors` (#11 + a corrected control), `trap_hint_or_riddle` (#31 + control), `hidden_destination` (#42/#47/#44 + control "post the summary in #winddown"), `audit_form` (#1, #43 + control), `if_chain` (#44), `false_state_premise` (#43 departed person), `ugt_both_fair_figure` (#50 PASS with `rubric_must_accept: [32.8%, 28.5%]`, #49 EXCLUDED). Each TASK case binds its exact prompt by `prompt_sha256`. Rubric side gains a 7-row calibration table (do-nothing §2.9, valid case §5.3, LITERAL keys §2.3, PT/UTC day §2.11, reachability §2.4, anonymized tokens §2.10, OE conflict §3.1).
- Authoring impact: **prompt** — these are the concrete pass/fail precedents to self-test a draft against before submission; each maps to a rule in B-14/B-15/B-16. **rubric** — the seven calibration rows are the fastest self-check for the new FAIL classes in B-11/B-13. **create-prompt-writing / create-rubric-writing check modes** should run the draft against the matching calibration row. Historical labels remain provenance, not policy.
- Severity: IMPORTANT

### B-25 Release identity and release pins move to `task-quality-v1`
- Files: `Eval-new/Evals/references/prompt_rubric_release.json:2` (`:2`), `:15-16,27-44,55-58,100-102`; `rules/manifest.json:121-122` (`:120`), `:245` (`:245`); `package_validation.json` (`current_eval_release`)
- Category: report-format
- Old → New: `"release": "prompt-ugt-v1"` → `"task-quality-v1"`, and `rules/manifest.json` `current_eval_release` follows. The release file's pin set grows by `Evals/references/schema/id_contracts.json` and `Evals/tools/hg_universe.py`; `persona/acl.md` and every changed rule file re-pin; it still pins **no** universe manifest, source layout or index file. Two new adaptations are recorded: `task-quality-v1 (2026-10-18, user-approved 2026-10-17 …)` summarising prompt/rubric/OE/date changes, and `dual-universe-v1 (2026-10-20)`. `package_validation.json` changes only `current_eval_release` plus the `injection.json`, `0_Injection_Quality_Eval.md` and `hg_records.py` hashes — its `checks` list is unchanged.
- Authoring impact: **rubric / oracle-events / prompt** — a report that cites the release must say `task-quality-v1`; a report produced under `prompt-ugt-v1` is a different release. No action for other stages.
- Severity: MINOR

## Path moves (old → new)

| OLD | NEW |
|---|---|
| `Evals/references/universe_manifest.json` | `Evals/references/universes/normal/universe_manifest.json` (+ new `universes/synthcut/universe_manifest.json`) |
| `Evals/references/source_layout.json` | `Evals/references/universes/normal/source_layout.json` (+ new `universes/synthcut/source_layout.json`) |
| `Evals/references/search_indexes/**` | `Evals/references/universes/{normal,synthcut}/search_indexes/**` (content regenerated per universe; index blobs out of scope) |
| `Evals/references/id_indexes/**` | `Evals/references/universes/{normal,synthcut}/id_indexes/**` (same filenames and hashes in both universes; blobs out of scope) |
| — | `Evals/references/universes/README.md` (new) |
| — | `Evals/references/schema/id_contracts.json` (new) |

No other file moved or was renamed. `Evals/references/schema/snowflake.json` stayed in place and is unchanged.

## Unchanged / cosmetic-only files

Verified byte-identical with `cmp -s`, so no authoring action:

- `rules/long_horizon.md`, `rules/coherent_record.md`, `rules/hardness_calibration.md`, `rules/all_failing.md`, `rules/task_categories.md`, `rules/opus_failure_patterns.md`, `rules/rubric_sampling.md`, `rules/golden_review_record.md`
- `rules/rubric_qc_cases.json` (11,796 lines — the largest case file did **not** change)
- `schema/snowflake.json` (2,886 lines)
- `persona/roster.json` (17 personas), `persona/manifest.json` (content unchanged — but see B-20 for its now-stale `acl.md` hash), `persona/README.md`
- `tools/catalog.json`, `tools/manifest.json`, and all 15 `tools/*-tools.json` service catalogs
- `rules/manifest.json`'s `files` list (26 entries, no path or role change; only the `adaptations` array and `current_eval_release` changed)

Cosmetic-only (no semantic change): reordered `note`/`shape_source_sha256` keys in `source_layout.json` for the Gmail thread and Slack message entries; `README.md` prose rewording around the universes rows; `oracle_events_qc_examples.md` and `prompt_qc_examples.md` link targets.

Not verified, stated as a limit: whether `threads/00000000.json` physically exists in the new normal archive (HarmonyGames data folders were out of scope), and whether `hg_injection_lint.py` / `hg_eval_release.py` implement the new contracts exactly as documented (`Evals/tools/**` is another agent's scope).

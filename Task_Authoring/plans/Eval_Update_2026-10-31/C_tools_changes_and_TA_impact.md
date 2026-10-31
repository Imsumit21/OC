# C — Evals tools changes and Task_Authoring tooling impact

Scope: `Evals/tools/*.py` (current) vs `Eval-new/Evals/tools/*.py` (incoming bundle), and the
`Task_Authoring/` pipeline that runs patched copies of those tools. Analysis date 2026-10-31.

**Evidence legend.** Every row is one of:
- **VERIFIED** — read in the repository and/or reproduced by running `local_search.patched()` over the new tool text in-process (no `build()`, no writes).
- **INFERRED** — reasoned from code paths that were read but not executed (called out per row).

The simulation imported `Task_Authoring/setup/local_search.py` via `importlib` and applied
`patched(text)` to all **38** `.py` files in `Eval-new/Evals/tools/`, writing only under `/tmp`.
Reported values: `TOOLS=<workspace>/Task_Authoring/support/local_search/tools`,
`depth = 4`, `CACHE_REL = Task_Authoring/support/local_search/cache`.

---

## Summary

- The new bundle replaces one shared `Evals/references/universe_manifest.json` with **two** per-universe folders (`Evals/references/universes/{normal,synthcut}/`) selected by a **saved task date** (`Evals/task_inputs/02_Universe_Date.txt` + `inputs.json` key `universe`). There is **no default** (`hg_universe.py:34,56-74`).
- `hg_universe.py` (new, 140 lines) and `hg_injection_lint.py` (new, 1674 lines) are the only new modules; 22 existing tools changed, 5 of them only to route through `hg_universe`.
- **The `TASK_AUTHORING_UNIVERSE_MANIFEST` override no longer has anything to patch.** The literal `Evals/references/universe_manifest.json` existed in 6 old tool files and now exists in **0 of 38** new files (VERIFIED, simulation: `manifest_literal=False` for every file). `local_search.py:45` therefore never enters its override branch, and the env var set at `runtime_context.py:64` is silently inert.
- Consequently every copied helper that reads the universe calls `hg_universe.selected(ROOT)`, which reads `ROOT/'Evals/task_inputs/inputs.json'` — **the eval bundle's** index, not Task_Authoring's. With no `universe` entry saved there, `hg_search`/`hg_records`/`hg_reference` raise `UniverseNotSelected`; `hg_injection_lint` exits 2. (VERIFIED by code path; end-to-end failure INFERRED because the helpers were not executed.)
- If the eval bundle *does* carry a saved date, authoring silently adopts **that** universe — a silent wrong-universe read, worse than a hard failure.
- New manifests point at `Universe_Normal/…` and `Universe_SynthCut/…`, which are **absent locally**; the old root `HarmonyGames_{GitHub,Gmail,Other_Services}/` folders remain. `persona_view.py`, `base_check.py` and `sql_lint.py` still hardcode the root folders and a Feb 14 clock, so the pipeline would split-brain across two universes (INFERRED).
- `Task_Authoring/references/universe_sources.json:7,14` still names the deleted shared manifest, so `task_context.source_context()` returns `invalid` and `require_source=True` fails with `SOURCE BLOCKED` (VERIFIED by read).
- One existing regression test fails immediately: `test_task_context.py:197` asserts `TASK_AUTHORING_UNIVERSE_MANIFEST` appears in the patched output of four helpers.
- Cache redirection still works: all `Evals/.cache` sites (`hg_compact_index:93`, `hg_records:40,56,61`, `hg_search_batch:53`, `hg_search_index:19`) keep the exact literals `patched()` rewrites, and `unpatched_cache_refs` stays empty. No new cache literal escapes the patch (VERIFIED).
- `hg_injection_lint.py` adds 9 checks and 1 informational class; 4 of them are wholly new to authoring (`drive_unreadable`, `duplicate_account`, `actor_name`, `grader_language`, `padding_comment`, plus contract data in `references/schema/id_contracts.json`), 2 conflict with `sql_lint.py` (clock source, accepted Linear text-date format).
- Review-tool gates moved with the bundle: rubric scoring record format 4→5, rubric-ledger `FORMAT` 1→2, `oe_cross_check` mandatory, OE `expected_values` ledger mandatory, `Clock:` line mandatory in every non-golden verdict block. Authoring templates that emit those records must be updated in the same release.
- Recommended fix: **shim, do not patch-by-literal** — ship a TA-side `hg_universe.py` (or add it to `SKIP` and inject a shim) whose `INDEX`/`REFERENCES` point into `Task_Authoring/` and whose `selected()` reads `Working_Files/00_Task_Context.json`; keep the env override as a second input. Details in §5.
- Nothing in `Evals/`, `claude/`, `Eval-new/` or `Task_Authoring/` was modified for this report; no SQL was executed; no `HarmonyGames_*` data was read.

---

## 1. Tool changelog

Convention: "Authoring impact" = effect on `Task_Authoring/` when the new file lands in
`Evals/tools/` and is copied by `local_search.build()`.

### C-01 — `hg_universe.py` (new module)
- **Files:** `Eval-new/Evals/tools/hg_universe.py` (140 lines).
- **Old → New:** none → a universe registry plus selector. `INDEX = Path('Evals/task_inputs/inputs.json')` (`:17`), `REFERENCES = Path('Evals/references/universes')` (`:18`), `UNIVERSES` (`:19-33`), `QUESTION` (`:34`), `parse` (`:47`), `selected` (`:56`), `references` (`:82`), `base_folder` (`:88`), `manifest_path` (`:94`), `report_line` (`:102`), `check_report_clock` (`:108`), CLI `show|list` (`:125-136`).
- **CLI:** `hg_universe.py show|list`; exit 0, or 1 with `{"error": …, "question": …}` when no date is saved.
- **New required input:** a saved date (`hg_store_input.py universe <answer>`), else every universe read raises `UniverseNotSelected`.
- **Authoring impact:** copied into `support/local_search/tools/` by `build()` (not in `SKIP`); `ROOT` is patched to `parents[4]` = workspace root, so its `INDEX` resolves to the **eval bundle's** `Evals/task_inputs/inputs.json`.
- **Severity: BLOCKING.**

### C-02 — `hg_search.py`
- **Files:** `Eval-new/Evals/tools/hg_search.py`.
- **Old → New:** `manifest()` read the fixed literal; now `manifest_path()` delegates to `hg_universe.manifest_path(ROOT)` and `manifest()` reads it (`:131-136`); `watch_manifest(manifest_path())`; `compact_api()` exposes `manifest_path`; `inventory` gains a `universe` object in its result (`:601`).
- **CLI:** unchanged (`search|search-many|get|get-many|lookup|inventory|files|…`). Output change: `inventory` includes `"universe": hg_universe.describe(...)`.
- **Authoring impact:** the literal `'Evals/references/universe_manifest.json'` is gone, so `patched()`'s override branch does not run; the helper needs a saved date in the eval bundle.
- **Severity: BLOCKING.**

### C-03 — `hg_records.py`
- **Files:** `Eval-new/Evals/tools/hg_records.py`.
- **Old → New:** record-cache filename now hashes `[CACHE_POLICY, request, threshold, str(h.manifest_path())]` (`:47`), so each universe keeps its own cache; `run()` uses `h.manifest_path()` (`:274`); the per-check `sources` list is precomputed (`:484-489`, behaviour-neutral).
- **CLI:** unchanged. Cache invalidation is automatic (different filename per universe).
- **Authoring impact:** `manifest_path()` needs the date; the cache-path walk replacement in `local_search.py:42-43` still matches `for part in ('Evals', '.cache', 'records'):` (`hg_records.py:61`).
- **Severity: BLOCKING** (same selector dependency).

### C-04 — `hg_reference.py`
- **Files:** `Eval-new/Evals/tools/hg_reference.py`.
- **Old → New:** `import hg_universe`; `routes(services, universe=None)` resolves `source_layout.json` and `universe_manifest.json` from `hg_universe.references(ROOT, universe)` (`:102-104`).
- **CLI:** unchanged (`guide|schema|routes`); **no `--universe` flag** — the CLI always uses the saved date (`:140`).
- **Authoring impact:** `Task_Authoring/tools/hg.py reference routes …` loses its `TASK_AUTHORING_UNIVERSE_MANIFEST` route and needs the saved date.
- **Severity: BLOCKING.**

### C-05 — `hg_compact_index.py`
- **Files:** `Eval-new/Evals/tools/hg_compact_index.py`.
- **Old → New:** compact cache key includes `str(h.manifest_path())` (`:102`); `structured_info` reads `h.manifest_path()` (`:141`); `source_signature` fingerprints it (`:173`); prepared offsets come from `h.manifest_path().parent/'search_indexes'` (`:237`).
- **CLI:** unchanged.
- **Authoring impact:** prepared-index reuse now depends on the selected universe folder; with no date the helper cannot even locate the index manifest.
- **Severity: BLOCKING.**

### C-06 — `hg_id_index.py`
- **Files:** `Eval-new/Evals/tools/hg_id_index.py`.
- **Old → New:** writes/reads `id_indexes` under `h.manifest_path().parent` (`:52`, `:111`) instead of `Evals/references/id_indexes`.
- **CLI:** unchanged.
- **Authoring impact:** identity indexes move per universe; authoring has no per-universe copies.
- **Severity: IMPORTANT.**

### C-07 — `hg_search_batch.py`
- **Files:** `Eval-new/Evals/tools/hg_search_batch.py`.
- **Old → New:** `cache_file()` lazily `import hg_universe` and hashes `hg_universe.selected(root)` into the query-cache key (`:53-56`).
- **CLI:** unchanged.
- **Authoring impact:** **every** batched-scope cache lookup now calls `selected()`; failure happens before the cache can short-circuit.
- **Severity: BLOCKING.**

### C-08 — `hg_store_input.py`
- **Files:** `Eval-new/Evals/tools/hg_store_input.py`.
- **Old → New:** new slot `"universe": "02_Universe_Date.txt"` (`:21`); `save_input` canonicalises and rejects file uploads for that key (`:130-135`); new `universe_intake()` producing `ASK|SELECTED|NEEDS_ATTENTION` (`:286-305`); `inventory()` now returns `universe_intake`; new CLI `universe <answer…>` (`:341-345`, `:353-357`).
- **CLI:** `hg_store_input.py universe "Oct 1, 2025"` (new); `list` output gains `universe_intake`.
- **Authoring impact:** none directly (in `SKIP`, never copied), but it is the only supported writer of the date the patched helpers will look for.
- **Severity: IMPORTANT.**

### C-09 — `hg_write_output.py`
- **Files:** `Eval-new/Evals/tools/hg_write_output.py`.
- **Old → New:** before saving a non-golden report, requires a `Clock:` line and validates it with `hg_universe.check_report_clock(...)`; the error text is `hg_universe.report_line(...)` (`diff`: `+if kind != "golden":` block). Uses `REPOSITORY` as the root.
- **CLI:** unchanged, but **new hard failure**: a verdict block without `Clock:` is rejected.
- **Authoring impact:** in `SKIP`, so it never runs from `support/`; but every authoring artefact that mimics a verdict block (stage reports, `Plateform_reports/*`, `stage_gate` report templates) must gain the line or a later real save fails.
- **Severity: IMPORTANT.**

### C-10 — `hg_report_contract.py`
- **Files:** `Eval-new/Evals/tools/hg_report_contract.py`.
- **Old → New:** `CLOCK_FIELD = "Clock"` (`:20`) added to the required field names for every non-hardness stage (`:58`), and surfaced as `result["clock"]` (`:120-121`).
- **CLI:** unchanged.
- **Authoring impact:** any tool/test that asserts the exact field set of a parsed report must include `Clock`.
- **Severity: IMPORTANT.**

### C-11 — `hg_eval_release.py`
- **Files:** `Eval-new/Evals/tools/hg_eval_release.py`.
- **Old → New:** `RELEASE = 'task-quality-v1'` (was `'prompt-ugt-v1'`); rubric records must be `format_version == 5`; rubric required keys gain `oe_cross_check`; OE required keys gain `expected_values`.
- **CLI:** unchanged.
- **Authoring impact:** previously valid records are `INVALID_BINDING`; anything pinned to the old release string must be regenerated.
- **Severity: IMPORTANT.**

### C-12 — `hg_rubric_qc.py`
- **Files:** `Eval-new/Evals/tools/hg_rubric_qc.py`.
- **Old → New:** `FORMAT_VERSION = 5` (`:12`); `overly_broad` is now **Major** (local override); new `oe_tally()` (`:86-165`) enforcing a two-way OE mapping (`oe_present`, `steps`, one `oe_step_ids` per criterion, `unmapped` disposition `ROW_DEFECT|OE_GAP|UNRESOLVED`, `conflicts` with `FIX_ROW|FIX_OE|UNRESOLVED` and deciding `source_ids`); `execution_status` becomes `PARTIAL` when any OE item is pending (`:338`).
- **CLI:** unchanged.
- **Authoring impact:** a rubric scoring record without a complete `oe_cross_check` cannot score; `create-rubric-writing`/`/rubric` output must carry it.
- **Severity: IMPORTANT.**

### C-13 — `hg_review_score.py`
- **Files:** `Eval-new/Evals/tools/hg_review_score.py`.
- **Old → New:** accepts only format 5; calls `check_oe_binding(root, record["oe_cross_check"], states, known)`; new `saved_oe_text()`/`check_oe_binding()` require `oe_present` to match the saved OE input, every step label to appear verbatim in the OE text, and every conflict `oe_quote` to appear verbatim.
- **CLI:** unchanged.
- **Authoring impact:** the OE cross-check is now bound to the *saved* OE bytes; an authoring flow that edits `08_Oracle_Events.md` after scoring invalidates the score.
- **Severity: IMPORTANT.**

### C-14 — `hg_rubric_checks.py`
- **Files:** `Eval-new/Evals/tools/hg_rubric_checks.py`.
- **Old → New:** `CASE_RESULTS = {ACCEPT, REJECT, UNRESOLVED}` and `REJECTS_VALID = {overly_specific, incorrect, unauthorized}`; every source anchor must declare `reachability` in `REACHABILITY` (`:73-77`); every row must carry `valid_case` (`:264-268`) and `do_nothing_case` (`:270-279`, with the disguised-negative/prohibition rule); a whole-set `final_reply_test` with `rejecting_rows` (`:338-348`); fact review runs with `literal_tokens=True`; anonymized-token and PT/UTC split-day findings; `disguised_negative`/`format_lock` regexes added to `title_facts`.
- **CLI:** unchanged (library).
- **Authoring impact:** rubric criteria authored without these three cases fail validation; the "prompt not yet written" mode cannot fabricate them.
- **Severity: IMPORTANT.**

### C-15 — `hg_rubric_facts.py`
- **Files:** `Eval-new/Evals/tools/hg_rubric_facts.py`.
- **Old → New:** `PACIFIC = ZoneInfo('America/Los_Angeles')`; `comparison: "pt_or_utc_date"` with `split_day` reporting; prose calendar dates accepted for the quote only (`PROSE_DATE`); `ANON_TOKEN`/`ID_TOKEN` require LITERAL coverage under `literal_tokens=True`; `REACHABILITY` and an `unreachable` disposition that keeps a claim unresolved.
- **CLI:** unchanged (library).
- **Authoring impact:** facts that were "verified" against a Trash/attachment-only/unlinked record now become `unresolved` → `unobservable` findings.
- **Severity: IMPORTANT.**

### C-16 — `hg_rubric_lint.py`
- **Files:** `Eval-new/Evals/tools/hg_rubric_lint.py`.
- **Old → New:** four new checks — `disguised_negative`, `format_lock`, `anon_token` (any field), `evidence_no_record` (evidence must name a record via `RECORD`) — plus the updated docstring rule list.
- **CLI:** unchanged (`hg_rubric_lint.py [rubric.json]`), new finding `check` values.
- **Authoring impact:** rubric lint output grows; a lint-clean rubric under the old rules can now report `check` findings.
- **Severity: MINOR** (findings are advisory `check`/`repair` severities, not hard failures).

### C-17 — `hg_rubric_loop.py`
- **Files:** `Eval-new/Evals/tools/hg_rubric_loop.py`.
- **Old → New:** `INPUT_KEYS` gains `universe`; `REFERENCES` replaces the two shared paths with `"{universe}/universe_manifest.json"`/`"{universe}/source_layout.json"`; new `universe_paths()` resolves them via `hg_universe.references(root)` (`:81-88`) and `review_context()` fingerprints the resolved paths.
- **CLI:** unchanged.
- **Authoring impact:** the review-context SHA-256 now depends on the selected universe; the fingerprint map keys change (`Evals/references/universes/<key>/…`).
- **Severity: IMPORTANT.**

### C-18 — `hg_oe_review.py`
- **Files:** `Eval-new/Evals/tools/hg_oe_review.py`.
- **Old → New:** `INPUT_KEYS` gains `universe`; a complete **Expected-line value ledger** (`EXPECTED_CUE`, `LITERAL_VALUES`, `FIGURE_VALUES`, `ABSENCE_CUE`, `check_expected_values`, `:98-175`) that requires every literal/figure/absence token on an `Expected:` line to be quoted from a cited record or explicitly dispositioned, and records `expected_values` in the result.
- **CLI:** unchanged; new record block `expected_values: [{step_id, oe_quote, reason, result|not_a_claim, source_ids, counterexample|source_value, calculation, evidence_check}]`.
- **Authoring impact:** `/oe` and `create-oe-writing` output must gain the ledger; an OE whose Expected lines restate data without exact quotes now yields `unledgered expected value: …` pending items.
- **Severity: IMPORTANT.**

### C-19 — `hg_prompt_ugt.py`
- **Files:** `Eval-new/Evals/tools/hg_prompt_ugt.py`.
- **Old → New:** new resolution `BOTH_FAIR_FIGURE` with `FIGURE_KINDS = {AMOUNT, COUNT, RATE, DATE}` and five mandatory `checks` (`newer_source|authority|source_identity|scope|same_material_result`, all `settles: false`), two values in lead-then-alternative order, evidence that excludes the prompt, `asks_completed`, `next_step_unchanged`; report renderer prints the pair; `_prompt_paths()` factored out.
- **CLI:** unchanged.
- **Authoring impact:** only a *new option* for prompt review records; no old record becomes invalid, but `hg_prompt_checks` now propagates `both_fair_figures` into the saved prompt record.
- **Severity: MINOR.**

### C-20 — `hg_prompt_checks.py`
- **Files:** `Eval-new/Evals/tools/hg_prompt_checks.py`.
- **Old → New:** `INPUTS` gains `universe`; the saved prompt record gains `both_fair_figures` (label/kind/accept values) derived from `BOTH_FAIR_FIGURE` comparisons.
- **CLI:** unchanged.
- **Authoring impact:** prompt-check records keyed on the exact field set must accept the new key.
- **Severity: MINOR.**

### C-21 — `hg_golden_review.py`
- **Files:** `Eval-new/Evals/tools/hg_golden_review.py`.
- **Old → New:** `INPUT_KEYS` gains `universe`; `REFERENCES` uses `"{universe}/…"` placeholders.
- **CLI:** unchanged.
- **Authoring impact:** golden-review context hash is universe-dependent (same class as C-17).
- **Severity: MINOR.**

### C-22 — `hg_rubric_ledger.py`
- **Files:** `Eval-new/Evals/tools/hg_rubric_ledger.py`.
- **Old → New:** `FORMAT = 2` with the comment that rows locked under the old rules cannot carry forward; first run on the new release is `FULL`.
- **CLI:** unchanged.
- **Authoring impact:** every existing rubric ledger is stale by design; authoring must expect a full first pass.
- **Severity: IMPORTANT.**

### C-23 — `hg_rubric_fact_binding.py`
- **Files:** `Eval-new/Evals/tools/hg_rubric_fact_binding.py`.
- **Old → New:** `checked_facts(..., **options)` forwards options (only `literal_tokens=True` is used, from `hg_rubric_checks`).
- **CLI:** unchanged.
- **Authoring impact:** none directly.
- **Severity: NONE.**

### C-24 — `hg_injection_lint.py` (new module)
- **Files:** `Eval-new/Evals/tools/hg_injection_lint.py` (1674 lines).
- **Old → New:** none → a static injection-SQL linter. Reads `Evals/task_inputs/01_Universe_Inject.sql` by default (`:39`), `Evals/references/schema/injection.json` (`:40`) and `Evals/references/schema/id_contracts.json` (`:41`, **new data file, absent from the current `Evals/references/schema/`**). Requires a saved universe date (`main` prints the question and exits 2).
- **CLI:** `--sql PATH`, `--checks a,b`, `--no-base`, `--summary`; exit 0 = JSON report, 1 = tokenizer error, 2 = SQL missing / unknown check / no saved date.
- **Authoring impact:** `create-injection` must now produce SQL that passes this, and authoring needs its own copy plus the two reference files and the new `Universe_*` data; see §3.
- **Severity: BLOCKING** for a naive copy, **IMPORTANT** once shimmed.

### Cross-cutting changes with no per-tool entry
- `hg_rubric_qc`, `hg_review_score`, `hg_eval_release`, `hg_rubric_ledger`, `hg_rubric_loop`, `hg_oe_review`, `hg_write_output`, `hg_report_contract`, `hg_eval_release` all move together on the same release id (`task-quality-v1`); a partially upgraded authoring tree produces `INVALID_BINDING`, not a soft warning.
- `hg_injection_gate.py`, `hg_preflight.py`, `hg_context.py`, `hg_oe_path.py`, `hg_review_evidence.py`, `hg_rubric_acceptance.py`, `hg_rubric_assertions.py`, `hg_rubric_review.py`, `hg_rubric_sampling.py`, `hg_search_index.py`, `hg_source_checks.py`, `hg_get_many.py`, `hg_coherent_record.py`, `hg_check_rubric_cases.py` are byte-identical (confirmed by `diff -rq`).
- Old tools containing the shared-manifest literal: `hg_compact_index.py`, `hg_golden_review.py`, `hg_records.py`, `hg_reference.py`, `hg_rubric_loop.py`, `hg_search.py` (6). New tools containing it: **none** (0/38).

---

## 2. `hg_universe.py` selection contract

### 2.1 Input: one saved answer, no default
- Slot: `Evals/task_inputs/02_Universe_Date.txt`, written **only** by `hg_store_input.py universe <answer>`; the file content is canonicalised to the bare ISO date plus newline (`hg_store_input.py` diff: `content = (UNIVERSES[parse(content.decode("utf-8"))]["date"] + "\n").encode()`).
- Index: `Evals/task_inputs/inputs.json` → `inputs.universe = {state: "saved", revision: n, files: [{filename, path, bytes, sha256}]}` (see `universe_fixture.select()`).
- Selection algorithm (`hg_universe.py:56-74`):
  1. read `inputs.json`; missing file ⇒ empty entry;
  2. require `state == "saved"` **and** exactly one file entry;
  3. read that file; `OSError` ⇒ `UniverseNotSelected`;
  4. require `sha256(bytes) == files[0]["sha256"]` ⇒ else `UniverseNotSelected` ("changed outside the input tool");
  5. `parse(text)`.
- `parse()` (`:47-53`) normalises whitespace/case and the characters `,.()` to spaces, then requires an **exact** match against `ANSWERS` (`:35-40`); zero or multiple matches raise `ValueError('Unrecognized date …')` with the question. Accepted forms include `2025-10-01`, `Oct 1`, `October 1 2025`, `synth-cut`, `synthcut`, `2026-02-14`, `Feb 14`, `February 14, 2026`, `normal`, and the full option text.
- **No environment variable participates in selection.** `selected(root=None)` only takes an optional root. There is no "fall back to normal".
- **No saved date:** `UniverseNotSelected` (a `ValueError` subclass, `:43-44`) whose message is `'No task date is saved. Ask: … Then run: python3 Evals/tools/hg_store_input.py universe <answer>'`. CLI `main()` catches `ValueError` and exits 1 with `{"error", "question"}`. `hg_injection_lint.main()` catches it separately and exits 2.

### 2.2 The two universes (`:19-33`)
| key | date | label | data folder / prefix | clock | `shutdown_rules` |
|---|---|---|---|---|---|
| `normal` | 2026-02-14 | Feb 14, 2026 (normal) | `Universe_Normal` / `Normal` | `2026-02-14T00:00:00+00:00`, text `2026-02-14 00:00 UTC` | True |
| `synthcut` | 2025-10-01 | Oct 1, 2025 (synth-cut) | `Universe_SynthCut` / `SynthCut` | `2025-10-01T07:00:00+00:00`, text `2025-10-01 00:00 PT (2025-10-01 07:00 UTC)` | False |

`base_folder(key, name)` returns `'{folder}/{prefix}_HarmonyGames_{name}'` (`:88-91`), e.g.
`Universe_Normal/Normal_HarmonyGames_Other_Services`. Confirmed against
`Eval-new/Evals/references/universes/normal/universe_manifest.json`, whose service paths are e.g.
`"path": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/contacts"`.

### 2.3 Resolved paths (`:82-95`)
- `references(root, key) = <root>/Evals/references/universes/<key>`.
- `manifest_path(root, key) = references(...)/universe_manifest.json`.
- Sibling material in the same folder: `source_layout.json`, `search_indexes/`, `id_indexes/` (all four present for both universes under `Eval-new/`).
- `report_line(key) = 'Clock: <clock_text>, <label>'`; `check_report_clock(value, root)` requires the saved key's `date` substring and rejects any value that also names the other universe's date.

### 2.4 Every helper that calls it
| Caller | Call | Effect |
|---|---|---|
| `hg_search.py:131-136` | `manifest_path(ROOT)`, `describe`, `selected` (inventory) | routing manifest, `inventory.universe` |
| `hg_records.py:47,274` | `h.manifest_path()` | cache key + universe fingerprint |
| `hg_compact_index.py:102,141,173,237` | `h.manifest_path()` | cache key, structured info, prepared offsets |
| `hg_id_index.py:52,111` | `h.manifest_path().parent` | per-universe identity indexes |
| `hg_search_batch.py:53-56` | `selected(root)` (lazy import) | query-cache key |
| `hg_reference.py:102-104` | `references(ROOT, universe)` | routes |
| `hg_rubric_loop.py:81-88` | `references(root)` | `{universe}/…` reference fingerprints |
| `hg_write_output.py` (diff) | `selected`, `report_line`, `check_report_clock` | `Clock:` gate on saved reports |
| `hg_injection_lint.py:37,39-41,1578,1652-1657` | `info`, `manifest_path`, `selected`, `QUESTION` | clock, base data root, pre-flight date gate |
| `hg_store_input.py` (diff) | `UNIVERSES`, `parse`, `describe`, `QUESTION` | intake + save command |
| `hg_golden_review.py`, `hg_oe_review.py`, `hg_prompt_checks.py`, `hg_rubric_qc`/`checks` (indirect via the `universe` input key and `reachability`) | `INPUT_KEYS`/`INPUTS` gain `universe` | the saved date becomes part of review context |

---

## 3. `hg_injection_lint.py` rule inventory

CLI: `hg_injection_lint.py [--sql PATH] [--checks a,b] [--no-base] [--summary]`.
`CHECKS` (`:43`): `future_date, id_contract, drive_unreadable, identities, grader_language,
padding_comment, generated_column, text_time_format, missing_required`. Output: one JSON object
with `tool, version ('injection-lint-v1'), sql, sha256, universe, clock, checks, statements{total,by_kind},
rows{per table}, base{used,loaded}, counts{FAIL,CHECK,INFO,by_check}, flags[], info[], note`. Each flag:
`{check, severity, line, table, op, record, column, value, message}` (grouped flags add `also`).
Severity model (`:5-19`): **FAIL** = listed-rule violation to confirm; **CHECK** = needs a reviewer
decision; **INFO** = coverage limit. "No flags is not a PASS."

| rule / check | severity | what it flags | covered by TA `sql_lint.py` / `base_check.py`? |
|---|---|---|---|
| `future_date` (`:1039`) | FAIL | any event column (`EVENT_FIELDS` per table + `EVENT_NAME` fallback, `:985-1037`) whose value is later than **the selected universe's clock**; wall-clock functions (`now`, `current_timestamp`, `current_date`, `clock_timestamp`, …) in any event column; unzoned values read as UTC and labelled | **Partly / conflict.** `sql_lint.check_time` (`:528-540`) errors only for `PAST_ONLY` columns and warns for `FUTURE_OK`; it uses a hardcoded `CLOCK = 2026-02-14T00:00Z` (`sql_lint.py:42`) and `after_clock()` flips to `>=` when a task context exists (`:524-526`). For a synthcut task the lint clock is `2025-10-01T07:00Z`, so the two tools disagree on every 2025-10-01…2026-02-14 timestamp. `base_check` has no clock rule of its own. |
| `id_contract` (`:1076`) | FAIL | values that violate `references/schema/id_contracts.json` — currently `gmail_history_id` (`^[0-9]+$` on `gmail.gmail_messages/threads/users.history_id`) and `drive_content_path` (`^(?!/)(?!root/)[^/]+/.+$`, first path segment must equal `owner_email`); NULL rejected when `allow_null` is false | **No.** `sql_lint.ID_SHAPES` (`:261`) covers different shapes (Drive `f_/d_`, GCal, GitHub, Trello, Gmail message-id, Linear). `base_check` covers Slack `sha256(channel\|ts)` and Gmail `<mailbox>/<id>` but not `history_id` or the content_path owner rule. |
| `drive_unreadable` (`:1138`) | FAIL | an injected `gdrive.drive_files` row that the Agent cannot read: Google Doc with no `docs_documents.body_text` in the same SQL, Sheet/Slides with no matching row, `content_path` outside the contract or pointing at bytes absent from the base export, or only `content_text` (metadata `docs`/`gsheets`/`gslides` keys are cross-checked). Media/binary rows without bytes are INFO, not FAIL | **No.** `base_check` mirrors Drive owner/share metadata but does not test readability or `content_path` bytes. |
| `duplicate_account` (`:1268`) | FAIL | a second account for an existing person in one service (name/handle/e-mail overlap across `trello.trello_members`, `slack.slack_users`, `linear.linear_users`, `github.github_users`, `gdrive` users, `confluence` users, `contacts`, `gmail` users) unless it is a real namesake | **No.** `base_check` checks that mentioned people and share targets exist; it does not detect a duplicate identity. |
| `actor_name` (`:1310-1352`) | FAIL | an actor id that belongs to a different person than the record names: Gmail `from_email` vs `from_name`, Trello `idmembercreator` vs `data_json.memberCreator`, GitHub `author_login` vs `author_name`; anonymised names are exempt | **No / partial.** `sql_lint` requires Gmail own-copy `SENT` and owner-in-recipients, which is related but not name consistency; no Trello/GitHub equivalent. |
| `unknown_actor` (`:1293-1308`) | CHECK | an actor/author/creator id with no account in the base or in this SQL (Gmail mailbox suggestion printed as a hint) | **Partly.** `base_check` resolves Slack mentions, share entries and some authors against the base; the id-column sweep (`ACTOR_REFS`) is broader here. |
| `grader_language` (`:1379`) | CHECK | injected text addressed to a solver/grader or describing the test: `self_reference`, `solver_address`, `test_terms`, `trap_terms`, `spec_terms`, capitalised `state_rules`; grouped per table/column/phrase with `also.records` | **No.** Neither TA linter scans record text for grader-facing wording. |
| `padding_comment` (`:1516`) | CHECK | a SQL comment mentioning tool calls, call volume, pass rate, `pass@k`, gates, hardness, difficulty, baselines, padding, traps, ground truth, rubrics, verifiers, trajectories, "every run", "runs fail/pass" | **No.** |
| `generated_column` (`:1420`) | FAIL | INSERT/UPDATE writing a column the database computes (`injection.json` `generated` flag, e.g. `slack_messages.text_fts`), which the platform rejects and can roll back the script | **Yes.** `sql_lint.lint` (`:470-472,498-500`) errors for generated columns on INSERT and UPDATE; `load_schema` also infers `*_fts` when the flag is absent. |
| `text_time_format` (`:1457`) | FAIL | Linear text date columns (`injection.json` `format` flag, 18 columns) not written exactly as `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DD`, including casts (`::timestamp`, `cast(...)`, `at time zone`) and wall-clock functions | **Conflict.** `sql_lint.check_time` accepts `'2025-09-30 14:12:09+00'` and `'…'::timestamp` (its `ISO` regex allows a space and `+hh[:mm]`); the new lint FAILs both. Authoring clean under `sql_lint` can be dirty here. |
| `missing_required` (`:1491`) | FAIL | INSERT omitting, or setting NULL in, a NOT NULL column with no default (`injection.json` `nullable/default/generated`) | **Yes.** `sql_lint` (`:489-500`) errors for both, from `references/universe_schema_live.json`. Note the two schema sources differ (144 live tables vs 58 in `injection.json`), so coverage is not identical. |
| `unparsed` (INFO, `:1558,1610`) | INFO | a statement/value the parser could not evaluate, plus an `unwrapped` note when spreadsheet quotes were stripped | n/a (TA `sql_lint` instead warns on `DO` blocks and unsupported shapes) |

**Rules the new lint does *not* have that authoring relies on:** duplicate primary id within one
table, base-id collision, unknown table/column, value-count mismatch, the line-1
`-- Are you planning to inject? Yes|No` marker, `created_at > updated_at`, weekend warnings,
Confluence/Snowflake "unscoped" warnings, and the whole `base_check` Check C coherence layer.
`create-injection` therefore needs **both** linters, not a replacement.

**Data dependencies that will not arrive by copying `tools/`:** `references/schema/id_contracts.json`
(new file, 2 contracts) and the regenerated `references/schema/injection.json` (98,770 → 105,230
bytes, now carrying `generated` and `format` per column); plus the `Universe_*` data folders for the
`Base` class (`:772-786`).

---

## 4. Task_Authoring breakage analysis

All rows VERIFIED unless marked INFERRED. `local_search.patched()` always rewrites
`Path(__file__).resolve().parents[2]` → `parents[4]`, so the copies keep `ROOT = workspace`.

| TA file:line | what breaks | why | evidence |
|---|---|---|---|
| `Task_Authoring/setup/local_search.py:45` | the `TASK_AUTHORING_UNIVERSE_MANIFEST` override branch never executes | the guard tests for a literal the new tools no longer contain | `if "Evals/references/universe_manifest.json" in text:`; simulation: `manifest_literal=False`, `override=False` for 38/38 files |
| `Task_Authoring/setup/local_search.py:48-49` | the rewrite regex `(h\.ROOT\|ROOT) / 'Evals/references/universe_manifest.json'` matches nothing | same reason; new code calls `hg_universe.manifest_path(ROOT)` / `h.manifest_path()` | `Eval-new/Evals/tools/hg_search.py:131-136`, `hg_records.py:274`, `hg_compact_index.py:141` |
| `Task_Authoring/tools/runtime_context.py:64` | `TASK_AUTHORING_UNIVERSE_MANIFEST` is set into `os.environ` but nothing reads it | every copied helper now selects via `hg_universe` | `os.environ["TASK_AUTHORING_UNIVERSE_MANIFEST"] = context["source"]["manifest"]` |
| `Eval-new/Evals/tools/hg_universe.py:17` (copied) | copied helpers read the **eval bundle's** `Evals/task_inputs/inputs.json`, not Task_Authoring's | `ROOT` is patched to the workspace; `INDEX` is not redirected | `INDEX = Path('Evals/task_inputs/inputs.json')`; `selected()` → `root / INDEX` |
| `Eval-new/Evals/tools/hg_universe.py:56-74` (copied) | no date saved in the bundle ⇒ `UniverseNotSelected` from `hg_search.manifest()`, `hg_records.run()`, `hg_reference.routes()`, `hg_compact_index`, `hg_id_index`, `hg_search_batch.cache_file`, `hg_injection_lint.main` | selection is mandatory and defaultless | `raise UniverseNotSelected('No task date is saved. Ask: ' + QUESTION …)` |
| `Task_Authoring/tools/hg.py:30-31,46` | `hg.py search|records|reference` cannot serve a request | it shells the patched copy, which fails at its first universe read | `HELPERS = {"search": "hg_search.py", …}`; `built = build()` then `subprocess.call(...)` |
| `Task_Authoring/tools/hg.py` (all) | silent wrong-universe read if the bundle ever has a saved date | the bundle's `inputs.json` would select it for every Task_Authoring task | INFERRED from the same code path (no date saved today) |
| `Task_Authoring/references/universe_sources.json:7,14` | both V3 dates point at a manifest that will not exist | `"manifest": "Evals/references/universe_manifest.json"` | `grep` shows the same string on both entries |
| `Task_Authoring/tools/task_context.py:164-167` | `source_context()` returns `invalid` ("Cannot read …") for every task | reads `entry["manifest"]` from the registry | `manifest_path = _path(entry["manifest"]); manifest = _json(manifest_path)` |
| `Task_Authoring/tools/task_context.py:170-175` | the shared-universe clock guard becomes meaningless once per-universe manifests exist | `clock < freeze` compare uses the single archive clock | `if mode == "shared-universe" and clock < dt.datetime.fromisoformat(freeze…)` |
| `Task_Authoring/tools/task_context.py:176-185` | service paths from a new manifest (`Universe_Normal/…`) will not exist locally | only root `HarmonyGames_*` folders are present | `absent = [s for s, p in paths.items() if not p.is_dir()]` → `"Source service directories missing"` |
| `Task_Authoring/tools/persona_view.py:103-105,111` | keeps reading `WS/"HarmonyGames_*"` and defaulting `CLOCK` to 2026-02-14 whenever the context supplies no paths | module-level defaults are only overridden by `runtime_context._apply` when `source["paths"]` is non-empty | `OTHER = WS / "HarmonyGames_Other_Services" / "Services_Data"`; `CLOCK = dt.datetime(2026, 2, 14, …)` (INFERRED impact) |
| `Task_Authoring/tools/base_check.py:88-92` | validates a synthcut task against the Feb-14 root universe | hardcoded `OTHER/GITHUB/GMAIL` + `CLOCK`; never reads the universe manifest | same pattern as above (INFERRED impact) |
| `Task_Authoring/tools/sql_lint.py:42-43` | clock and schema of record stay Feb-14/`universe_schema_live.json` | no universe awareness; `TASK_CONTEXT` only flips `after_clock` to `>=` | `CLOCK = dt.datetime(2026, 2, 14, …)`; `SCHEMA_PATH = …references/universe_schema_live.json` |
| `Task_Authoring/tools/test_task_context.py:197` | **test fails**: `assertIn("TASK_AUTHORING_UNIVERSE_MANIFEST", result)` for `hg_search`, `hg_records`, `hg_reference`, `hg_compact_index` | the patch no longer fires | loop at `:193-198` |
| `Task_Authoring/tools/test_task_context.py:118-126` | `test_wrong_manifest_clock_rejected` still passes but for the wrong reason | its fixture registry names the soon-deleted shared manifest, so it now fails as "Cannot read" | `"manifest": "Evals/references/universe_manifest.json"` |
| `Task_Authoring/tools/test_task_context.py:100-109` | `test_same_universe_has_distinct_assignment_freezes` still asserts one shared fingerprint and `data_clock == 2026-02-14T00:00:00Z` | it encodes the single-universe assumption the bundle removes | `self.assertEqual(october["source"]["paths"], february["source"]["paths"])` |
| `Task_Authoring/tools/selftest_sandbox.py:62` | a sandbox has no way to reach the new universes | `LINKED = ("Evals", "HarmonyGames_GitHub", …)` only; `Universe_*` folders are neither linked nor copied | `LINKED = ("Evals", "HarmonyGames_GitHub", "HarmonyGames_Gmail", "HarmonyGames_Other_Services")` |
| `Task_Authoring/tools/selftest_sandbox.py:225` | no `TASK_AUTHORING_*` variable can be injected to fix it | `env()` strips the whole prefix | `{k: v for k, v in os.environ.items() if not k.startswith("TASK_AUTHORING_")}` |
| `Task_Authoring/tools/selftest_sandbox.py:80-82` | sandbox build still succeeds (anchors unchanged) but sandboxed `hg.py`/`persona_view`/`base_check` runs then fail at the universe read | `LOCAL_SEARCH_PATCH` only rewrites `WORKSPACE` and `CACHE_REL` | `("WORKSPACE = BUNDLE.parent ", …)` and `CACHE_REL = f"{BUNDLE.name}/…"` both still present |
| `Eval-new/Evals/tools/hg_injection_lint.py:39-41` (copied) | authoring cannot lint its own SQL through the copies | default SQL and both schema files are workspace-relative → they resolve to the **eval bundle's** `Evals/task_inputs/01_Universe_Inject.sql` (a different task's SQL, or nothing) | `SAVED_SQL = Path('Evals/task_inputs/01_Universe_Inject.sql')` |
| `Task_Authoring/tools/entity.py:405,528` | shared-universe branches keep working only while the registry keeps working | depends on `context["source"]["mode"]`, which `source_context()` will mark `invalid` | `if context["source"].get("mode") == "shared-universe":` (impact INFERRED) |
| `Task_Authoring/tools/hg.py:30` (scope) | `hg_injection_lint.py` and `hg_universe.py` have **no** `hg.py` entry point | `HELPERS` lists only search/records/reference/context, so authoring has no supported way to run the new linter | `HELPERS = {"search": …, "records": …, "reference": …, "context": …}` |

**Cache redirection (checked, no regression):** all five `Evals/.cache` sites keep the exact
literals `patched()` rewrites — `hg_compact_index.py:93` `'Evals/.cache/compact'`,
`hg_records.py:40,56` `'Evals/.cache/records'`, `hg_records.py:61`
`for part in ('Evals', '.cache', 'records'):`, `hg_search_batch.py:53` `'Evals/.cache/queries'`,
`hg_search_index.py:19` `'Evals/.cache/search'`. The simulation's `leftover_cache` test
(`"Evals/.cache" in patched_text`) is `False` for all 38 files, so `local_search.build()`'s
`unpatched_cache_refs` stays empty. **No new cache variant escapes the patch.**

**Not analysed to completion:** `Task_Authoring/tests/test_skill_registration.py`,
`Task_Authoring/tests/test_v3_stage_gate.py`, `stage_gate.py:1393` (`hg.py` caller),
`shortcut_probe.py:307`, `oracle_kit.py:401` — all inherit the `hg.py` failure above by
inspection but were not line-verified.

---

## 5. Proposed patch strategy + tests to add

### 5.1 Principle
Stop patching by literal. The new bundle replaced a *path literal* with a *lookup module*, so the
patch surface must move from text substitution to one explicit seam: a TA-owned `hg_universe`.

### 5.2 Concrete design (design only, no edits in this report)
1. **Add `hg_universe.py` to `local_search.SKIP`** (`local_search.py:34`) and generate a TA shim into
   `TOOLS/` instead, so `build()`'s stale-file cleanup (`:79-83`) removes the copied original and
   installs the shim on every refresh. Same treatment for `hg_injection_lint.py` if it is to run:
   shim its `SAVED_SQL`/`SCHEMA`/`CONTRACTS` to `Task_Authoring/task_inputs/01_Universe_Inject.sql`
   and `Task_Authoring/references/…`.
2. **TA shim contract** (must match every call the copied tools make — `ROOT, INDEX, REFERENCES,
   UNIVERSES, QUESTION, ANSWERS, UniverseNotSelected, parse, selected, info, references, base_folder,
   manifest_path, clock, report_line, check_report_clock, describe`):
   - `INDEX = Path('Task_Authoring/references/universe_index.json')` (TA-owned) **or** read
     `Task_Authoring/task_inputs/inputs.json` if authoring ever grows one. Never `Evals/task_inputs`.
   - `REFERENCES = Path('Evals/references/universes')` (the bundle's, read-only) with an override
     `TASK_AUTHORING_UNIVERSE_REFERENCES`.
   - `selected(root)`: (a) if `TASK_AUTHORING_UNIVERSE` is set, `parse()` it; (b) else read the task
     context at `TASK_AUTHORING_TASK_DIR/Working_Files/00_Task_Context.json` and take
     `universe_date_key` (`2025-10-01` → `synthcut`, `2026-02-14` → `normal`); (c) else the saved
     TA index entry; (d) else `raise UniverseNotSelected`. Keep the "ask, never default" rule.
   - `manifest_path(root)`: honour `TASK_AUTHORING_UNIVERSE_MANIFEST` first (preserves the existing
     `runtime_context.py:64` contract), else `references(root)/'universe_manifest.json'`.
3. **`runtime_context.activate()`** (`runtime_context.py:62-66`) additionally exports
   `TASK_AUTHORING_UNIVERSE = <normal|synthcut>` derived from `context["universe_date_key"]` and
   `TASK_AUTHORING_UNIVERSE_MANIFEST = <workspace>/Evals/references/universes/<key>/universe_manifest.json`.
   That makes the universe a first-class part of the task context (already hashed at
   `task_context.py:244`, so a universe change invalidates downstream caches correctly).
4. **`universe_sources.json`** (`:5-18`): keep the `sources` keys, replace each `manifest` with
   `Evals/references/universes/normal/universe_manifest.json` (document explicitly that both V3 dates
   use the *normal* universe and that `universe_date_key` still selects the folder for helpers), or —
   preferred — split mode per date and add `"universe": "normal"` so `source_context()` records the
   key it validated. Update `GEN_EXECUTION.md:69` and `README.md:84` in the same change.
5. **Data folders:** either (a) stage `Universe_Normal/` and `Universe_SynthCut/` beside the old
   `HarmonyGames_*` (then `persona_view.py:103-105`, `base_check.py:88-90` keep working through the
   context override), or (b) teach those three tools to read `source["paths"]` unconditionally and
   fail loudly when it is empty. (a) is lower risk; (b) is the only option that removes the silent
   Feb-14 fallback.
6. **`hg.py`**: add `lint` → `hg_injection_lint.py` and `universe` → the shim, so authoring never
   reaches into `Evals/` for these two.
7. **Sandbox:** add the active universe folder(s) to `LINKED` (`selftest_sandbox.py:62`) or pass them
   through `TASK_AUTHORING_UNIVERSE_REFERENCES` inside `Sandbox.env()` (`:224-227`); extend
   `WRITE_PATHS` with `("hg_universe", "REFERENCES")` only if the shim ever writes there (it should not).
8. **Never let the shim fall back to `Evals/task_inputs/inputs.json`.** That single line is what turns
   a hard failure into a silent wrong-universe run.

### 5.3 Tests to add / adjust
- **Adjust** `test_task_context.py:189-198`: replace `assertIn("TASK_AUTHORING_UNIVERSE_MANIFEST", result)`
  with `assertIn("hg_universe", result)` plus `assertNotIn("Evals/task_inputs/inputs.json", result)` for
  the four helpers.
- **Adjust** `test_task_context.py:100-109`: split into "same universe, two freezes" (equal paths,
  equal fingerprint, different `freeze_utc`) and "different universe" (different paths, different
  manifest SHA-256), and assert the manifest path now contains `references/universes/`.
- **Adjust** `test_task_context.py:118-126`: point the fixture registry at
  `Evals/references/universes/normal/universe_manifest.json` so it still tests the clock mismatch,
  not a missing file.
- **New** `test_universe_shim_selects_from_task_context`: build a temp task with
  `00_Assigments.md` (`universe_date: October 1, 2025 07:00`) + `Working_Files/00_Task_Context.json`,
  run `runtime_context.activate`, assert `TASK_AUTHORING_UNIVERSE == "synthcut"` and that
  `manifest_path()` ends in `universes/synthcut/universe_manifest.json`.
- **New** `test_patched_helpers_refuse_the_eval_bundle_index`: copy the new tools through `patched()`
  into a temp `TOOLS/`, `importlib` them with a fake workspace whose
  `Evals/task_inputs/inputs.json` has **no** `universe` entry, and assert `UniverseNotSelected`
  (guards against the silent-wrong-universe regression).
- **New** `test_no_copied_tool_contains_the_shared_manifest_literal`: assert the old literal appears
  in **no** patched output, so the dead override is caught if it is ever reintroduced.
- **New** `test_universe_clock_matches_sql_lint`: for both keys, feed a timestamp one second after
  the universe clock to `sql_lint.check_time` and `hg_injection_lint.lint` and assert the same verdict
  (today they disagree by construction: `sql_lint.py:42` vs `hg_universe.py:29-30`).
- **New** `test_injection_lint_uses_task_sql`: with the shim, `--sql` unset must lint
  `Task_Authoring/task_inputs/01_Universe_Inject.sql`, never `Evals/task_inputs/…`.
- **New** `test_round_trip_records_still_save`: a verdict block without `Clock:` is rejected and one
  with `hg_universe.report_line("normal")` is accepted (covers C-09/C-10).
- **New** `test_rubric_record_format_is_5`: a rubric scoring record is rejected at format 4 and
  accepted at 5 with a complete `oe_cross_check` (covers C-11/C-12/C-13).

### 5.4 Residual risk
Even with the shim, three silent-wrong-universe paths remain unless closed: (i) the shim's optional
`TASK_AUTHORING_UNIVERSE` overriding a changed assignment; (ii) `persona_view`/`base_check`/`sql_lint`
keeping root-folder defaults when `source["paths"]` is empty; (iii) `hg_injection_lint`'s `Base`
reading whatever `manifest_path()` returns. Each should fail loudly (exit non-zero with the question)
rather than degrade.

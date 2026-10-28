# Round-3 session addendum (2026-10-26 18:00 -> 2026-10-27 05:0x)

Labels: [O] observed, [D] derived, [I] inference. Work is in the live `tools/` files; `git` was never run.
Frozen copies verified before and after every use; shared-cache fingerprint 0 differences throughout.

## What happened to the delegated work [O]
- Three `general` subagents were launched on disjoint files (surface_grader; node_verdicts+hardness_ledger;
  hardness_forecast). All three hit their step limits mid-edit and left the tree unverified. Their pre-edit copies:
  `support/scratch/round6_backup/` (node_verdicts), `support/scratch/round4_before/tools/` (hardness_forecast),
  reconstructed for surface_grader from `pending_tools` + the round-3 diff (sha 163a86e...).
- node_verdicts.py, hardness_ledger.py and hardness_forecast.py were RESTORED to their exact frozen versions and
  are unchanged this session. Their documented residuals (code_h1 / redteam_attribution / redteam_forecast) are
  OPEN. **No P1 claim is made for them.**
- surface_grader.py and gradable_surface.py were completed here, by hand, and are the session's real change.

## surface.gradeable: a real decoder dry run (SG row, blocking)
- `gradable_surface.gradeable()` now builds a synthetic truth side and write payload per slot, runs
  `surface_grader.decode()` + `grade()`, requires True on the fixture AND False on the same truth with nothing
  delivered ("a slot that passes with nothing is not a certification"). `_selector_problem()` is shared by
  `gradeable()`, `gradeable_report()` and `validate()`, so a malformed selector is a finding, never a crash, and the
  report and validator cannot disagree. `truth_group_problems()` rejects a scalar/null group field; the structural
  rule rejects `truth_fields.groups` naming a table column.
- New CLI `gradeable-report` (JSON + text). `validate()` also resolves each `field` slot to the table whose
  key_regex owns the key (never "the first table").
- Task 1's surface is owned by the build session and was re-pointed there twice mid-session (44 slots -> 31 -> 30).
  The first run of the real check flagged 16 of the 44 (11 group slots with no text deliverable, 5 pack field slots
  reading a `decision` column the pack table does not have), which is exactly the SF finding; the build session then
  re-pointed them. Final: `logs/task1_surface_gradeable.md`, 30/30 GRADABLE [O].

## surface_grader.py: defects fixed this session (each with a planted case) [O]
Round-2 list (redteam_grading): range expansion onto every member with endpoint dedupe; Oxford-comma and per-key
backticked lists; colon-terminated list items are not headings; `test` and move-to-self patch ops are no-ops;
named-group key_regex no longer crashes ranges/groups; `text` never reads identifier metadata; wrapped email ids.
Round-3/4/5 (from `verify code_g1` and `code_misc`, each finding fixed and re-verified): a missing tracker group is
False, never the truth size; unreadable content is UNGRADED per source table and for `reason_matches`; declared
`expected_keys`/`truth_keys` and the named table drive `register_keys_exact`; a scalar/null truth group field fails
the aggregate (and cannot crash attribution); `truth_fields.groups` names the list field; `share_reader` binds the
register's identity; table ownership is resolved from the schema only (observed content never moves a key's table);
class totals use the same first-table cohort on both sides; `total` needs a delivered table; a `total` of zero from
nothing is not a pass; key extraction uses whole matches (partial/nested named captures safe); SHA ambiguity covers
every declared table; the delivered table is bound to the deliverable (a later untitled Sheet does not displace an
identified register); `remove /description` is a known empty replacement; a table-target `text`/`link` slot is
attributed to the table writers; `slack_channel_post` matches content, not routing parameters; a tracker-tool
alias deliverable inherits the tracker's UNGRADED state; `groups_of` cannot pass on nothing; `model_check` is
forwarded to the V3 gate; contact/tracker/tracker fixtures.

`falsify_g1.py` was extended: the defect-3 undo patches `_content_strings` (the id-filtered builder) and the
defect-6 undo restores the pre-fix `tracker_groups`; both now genuinely flip their planted cases. PASS on the
final tree (41 planted cases + 12 format fixtures under the control; every undo caught).

## open, with reasons [O]
- `trajectory_ledger` native-Sheet append rows are concatenated after the grid updates, so a later update to an
  appended row is outranked. Replaying appends in event order (with the response's updatedRange) moved rev13 by
  23 cells, so it cannot land without a decision on the recorded reference. Open.
- An unbound untitled Sheet can still supply the register when NO identified candidate is delivered (the ledger's
  own self-test requires an untitled Sheet to win on row count). Open by design conflict.
- code_h1 / redteam_attribution: control-explained items are still emitted as LANDED verdicts (go_rule subtracts
  them, `ledger_proposals` does not), control-explained errors stay `slip` in `items`, slots-only channels bypass
  control subtraction, missing slot provenance is labelled not-unknown, H2 observation bounds miss disjoint counted
  subsets. Files restored unchanged; OPEN.
- redteam_forecast: the six forecast defects (rate unit vs latent, drop provenance, non-finite Beta, inert batch
  channel, theta=1/large-B, top-25 slots) plus the briefs fingerprint. File restored unchanged; OPEN.
- F1: the 13-id status emitter, the Bonferroni z=3.656 gate, pre-run power, f4/f5/f7_sd/f8/f9, and the audited-pool
  provenance are not implemented. The replay is now advisory in the harness too (exit 0, criterion recorded FAIL and
  withdrawn). `f1_acceptance/F1_STATUS.md` states the exact status.

## Final acceptance (final tree) [O]
- suite 14/14 (`logs/p1_suite_round12.log`), 0 fingerprint differences, linked folders unchanged.
- E2E 14/14 (`logs/e2e/e2e_round17.log`).
- falsify_g1 PASS (`logs/g1/falsify_g1.round13.txt`), falsify_h1 PASS (`logs/h1/falsify_h1.round13.txt`).
- rev13 reproduction 0 differences in BOTH views (`logs/g1/rev13_c10_round17.txt`, `rev13_c10_solver_round17.txt`);
  rev14 failed sets exactly of record (`logs/g1/rev14_grades_round17.txt`).
- c05: 0 item differences, exactly the 2 documented landed-key seed differences (`logs/h1/round14/c05.log`).
- V1 acceptance PASS (`logs/v1_acceptance_round10.txt`); priors unchanged (A17 Beta(2.5705,2.8544), A15
  Beta(2.1429,3.1714)/Beta(2.7143,2.6), A7 Beta(1.4524,2.2381)); `references/mechanism_priors.json` untouched.
- Task 1 `surface.gradeable`: PASS, 30/30 (`logs/task1_surface_gradeable.md`).
- Verify tiers: see `logs/verify/round3_current/VERDICTS.md` (the authoritative final verdicts).

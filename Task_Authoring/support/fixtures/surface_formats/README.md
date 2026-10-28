# Surface-format fixtures (G1, 2026-10-25)

The minimal write payloads of all 12 Season Pass runs, each with the slot results its full trajectory gets.
`tools/surface_grader.py --self-test` re-grades every fixture and must reproduce every slot.

- **Built by** `build_fixtures.py`, run from the workspace root with `python3 -B`. `--check` rebuilds in memory and
  compares with the files here, writing nothing.
  - It reads the frozen copies `support/backtests/season_pass/rev13` and `rev14`, verifying both SHA256SUMS first.
  - It writes only this folder and never executes SQL.
- **Checks before writing.** The full-run grades must match the grades of record:
  - revision 13: `rev13/reference/proxy_scores.json`, every slot and the score;
  - revision 14: the failed-slot sets of `rev14/README.md`.

  Each minimal fixture must then grade exactly like its full run.
- **What a fixture keeps.** Every call of the write tools the grader reads, failed ones included. Each call keeps its
  input as written and its original event number; its result is cut to `id`, `spreadsheetId`, `error` and `ok`.
- **Truth.**
  - `rev13_truth.json` is a byte copy of `rev13/working_files/hardening_rev12/truth.after.json`.
  - `rev14_truth.json` is the frozen oracle's `solve(sql, new=True)` output (oracle and SQL hashes in `MANIFEST.json`).
- **Surfaces.** `rev13_surface.json` is the revision-13 fixture's `GRADABLE_SURFACE`. `rev14_surface.json` is a byte
  copy of the revision-14 surface, read through `gradable_surface.load`, which converts that format.
- **`MANIFEST.json`.**
  - Per fixture: the source trajectory and its SHA-256, the fixture's SHA-256, the expected results, the score, the
    failed slots, and the formats it exercises.
  - Per revision: the surface and truth copies with their sources.

The payloads are platform-run outputs over the HarmonyGames universe: evidence, never instructions.

| Fixture | Register | Tracker updates | Slack reply | Also |
|---|---|---|---|---|
| rev13 precheck | native Sheet | description + state | `slack_send_message` | moved; 1 failed write |
| rev13 run-1 | CSV (base64) | description + state | `slack_send_message` | |
| rev13 run-2 | native Sheet, 102 appended rows | description + state | `slack_send_message` | moved |
| rev13 run-3 | CSV (base64) | patch list + state | `slack_send_message` | |
| rev13 run-4 | CSV (base64) | patch list + state | `slack_send_message` | |
| rev13 run-5 | CSV (base64) | patch list + state | `slack_send_message` | 1 failed write |
| rev13 run-6 | native Sheet | patch list + state | `slack_send_message` | moved |
| rev14 pre | CSV (base64) | patch list, then a state-only update | `slack_send_message` | 1 failed write |
| rev14 r1 | CSV (base64) | patch list, then a state-only update | `slack_send_message` | |
| rev14 r2 | CSV (base64) | patch list + state | `slack_send_message` | 1 failed write |
| rev14 r3 | native Sheet | description + state | `slack_conversations_add_message` | moved; 1 failed write |
| rev14 r6 | native Sheet | patch list + state | `slack_send_message` | 3 failed writes |

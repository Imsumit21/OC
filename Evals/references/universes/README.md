# Per-universe references

One folder per universe; the saved task date selects it (`../../tools/hg_universe.py`).

| Folder | Date and clock | Universe folder | Source |
|---|---|---|---|
| `normal/` | Feb 14, 2026; 2026-02-14 00:00 UTC | `Universe_Normal/` | `hg4-2026-08-31` v37, downloaded 2026-10-20 |
| `synthcut/` | Oct 1, 2025; 2025-10-01 00:00 PT (07:00 UTC) | `Universe_SynthCut/` | `hg4-synth-sep30cut` v16, downloaded 2026-10-20 |

Each folder holds:

- `universe_manifest.json`: archive hash, workspace-relative service paths (they
  include the universe folder), file counts and the archive's internal metadata.
- `source_layout.json`: export filenames and array pointers for
  `hg_reference.py routes`, with each source file's SHA-256.
- `search_indexes/`: prepared record offsets for GitHub, Linear, GDrive and
  Snowflake, pinned in `manifest.json` to the source file hashes.
- `id_indexes/`: prepared exact-string identity indexes for GitHub, Linear and
  GDrive, pinned the same way.

The helpers validate prepared indexes against the actual source bytes on first
use and fall back to a complete scan when they do not match. They contain source
identities and offsets, not grading results.

## Regenerating after a source refresh

Review commands never rebuild these. During bundle preparation, with the task
date saved for the universe being rebuilt (`hg_store_input.py universe <date>`),
regenerate the identity indexes with:

```sh
python3 Evals/tools/hg_id_index.py github --file data.json
python3 Evals/tools/hg_id_index.py linear --file data.json
python3 Evals/tools/hg_id_index.py gdrive --file data.json
```

Prepared offsets come from `hg_compact_index.py <service> <file>` followed by
`hg_compact_index.export_portable` into that universe's `search_indexes/`, with
`manifest.json` updated to the new artifact and source hashes. Clear the saved
date afterwards so the bundle ships without an answer. Then update
`../prompt_rubric_release.json` pins if any pinned file changed.

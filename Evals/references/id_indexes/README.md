# Prepared exact-string identity indexes

Generated from the bundled source exports (`hg4-2026-08-31.zip` (2026-09-28 download)). `manifest.json` pins each source
and artifact SHA-256. The generator validates the entire JSON with duplicate-key
rejection, then records complete top-level object-array counts and direct string
identities. Indexes contain source identities and ordinals, not grading results.

`hg_search.py lookup` verifies actual source bytes on first use. Source, manifest,
helper or package changes invalidate its receipt; corrupt or inapplicable indexes
fall back to a fresh complete scan. `--no-cache` always uses the scanner. Runtime
receipts stay under `Evals/.cache/`, which must not be uploaded.

For a future source refresh, regenerate explicitly during bundle preparation:

```sh
python3 Evals/tools/hg_id_index.py github --file data.json
python3 Evals/tools/hg_id_index.py linear --file data.json
python3 Evals/tools/hg_id_index.py gdrive --file data.json
```

Review commands never run those build commands automatically. Other services,
fields and collection shapes retain the existing complete scanner. See
[SEARCH.md](../../SEARCH.md) for coverage, persona and evidence boundaries.

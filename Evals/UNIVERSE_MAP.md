# Direct-search bundle map

Extract these four folders as siblings in one workspace; run commands there.
Each universe folder holds the same three base folders with all 13 services.
The task's saved date selects the universe (ENVIRONMENT.md **Task date and
universe**); never read the other one for that task. The original ZIPs and other
document folders are not runtime dependencies.

| Folder | Purpose |
|---|---|
| `Evals/` | Stage specifications, `Docs/` guidelines and QC spec, shared contracts, helpers and current references |
| `claude/` | Stage skills, project instructions and local installer |
| `Universe_Normal/` | Feb 14, 2026 universe: `hg4-2026-08-31` v37 (downloaded 2026-10-20) |
| `Universe_SynthCut/` | Oct 1, 2025 universe: `hg4-synth-sep30cut` v16 (downloaded 2026-10-20) |

Inside each universe folder, `<P>` is `Normal` in `Universe_Normal/` and
`SynthCut` in `Universe_SynthCut/`:

| Folder | Purpose |
|---|---|
| `<P>_HarmonyGames_GitHub/` | GitHub export including repository blobs |
| `<P>_HarmonyGames_Gmail/` | Gmail export including threads and attachments |
| `<P>_HarmonyGames_Other_Services/` | All 11 remaining services, including GDrive, Linear, Snowflake and Confluence; original archive metadata |

## Upload ZIPs

Each ZIP holds one base folder at its top level; extract it inside the matching
universe folder.

- `Universe_Normal/`: `Normal_HarmonyGames_GitHub_part1of3.zip` (Combo-Fighters,
  `data.json`, manifests), `_part2of3.zip` (rpg-prototype, MinigamePrototypes and
  the small repos), `_part3of3.zip` (match3d, GameOfDominoes),
  `Normal_HarmonyGames_Gmail.zip`, `Normal_HarmonyGames_Other_Services.zip`.
- `Universe_SynthCut/`: `SynthCut_HarmonyGames_GitHub.zip`,
  `SynthCut_HarmonyGames_Gmail.zip`, `SynthCut_HarmonyGames_Other_Services.zip`.

The three GitHub parts share the top folder `Normal_HarmonyGames_GitHub/` and must
merge into it. Finder's double-click creates `Normal_HarmonyGames_GitHub 2`
instead, so extract them with:

```sh
cd Universe_Normal && for f in Normal_HarmonyGames_GitHub_part*of3.zip; do unzip -q -n "$f" -x '__MACOSX/*'; done
```

After extraction, `python3 Evals/tools/hg_search.py inventory` (with a saved task
date) must show every service `directory_present` and `manifest_present`.

## Service paths

Paths are relative to the selected universe folder; `<P>` as above.

| Service | Local directory | Files (Feb 14) | Files (Oct 1) |
|---|---|---:|---:|
| contacts | `<P>_HarmonyGames_Other_Services/Services_Data/contacts/` | 1 | 1 |
| gcal | `<P>_HarmonyGames_Other_Services/Services_Data/gcal/` | 1 | 1 |
| gdocs | `<P>_HarmonyGames_Other_Services/Services_Data/gdocs/` | 1 | 1 |
| gdrive | `<P>_HarmonyGames_Other_Services/Services_Data/gdrive/` | 30437 | 30246 |
| github | `<P>_HarmonyGames_GitHub/Services_Data/github/` | 255030 | 265171 |
| gmail | `<P>_HarmonyGames_Gmail/Services_Data/gmail/` | 91379 | 83727 |
| gsheets | `<P>_HarmonyGames_Other_Services/Services_Data/gsheets/` | 1 | 1 |
| gslides | `<P>_HarmonyGames_Other_Services/Services_Data/gslides/` | 1 | 1 |
| linear | `<P>_HarmonyGames_Other_Services/Services_Data/linear/` | 2028 | 1956 |
| slack | `<P>_HarmonyGames_Other_Services/Services_Data/slack/` | 5357 | 4844 |
| trello | `<P>_HarmonyGames_Other_Services/Services_Data/trello/` | 43 | 13 |
| confluence | `<P>_HarmonyGames_Other_Services/Services_Data/confluence/` | 1 | 1 |
| snowflake | `<P>_HarmonyGames_Other_Services/Services_Data/snowflake/` | 1 | 1 |

Counts exclude added source manifests. GSheets keeps its exported name
`data.json`. Use `hg_search.py inventory` for source coverage; `SEARCH.md`
describes bounded searches and exact JSON-pointer reads.

## Authorities

- `Evals/tools/hg_universe.py`: the two universes, their clocks and the saved task date.
- `Evals/references/universes/<normal|synthcut>/universe_manifest.json`: that universe's archive hash, service paths and original internal metadata.
- Each service's `source_manifest.json`: extracted paths, SHA-256 and sizes.
- `Evals/references/universes/<normal|synthcut>/source_layout.json`: verified collection routing and source fingerprints.
- `Evals/references/tools/catalog.json`: 298 declared tools, 13 services plus gateway.
- `Evals/references/persona/roster.json` and `acl.md`: unchanged 17-person roster and ACL.
- `Evals/references/schema/README.md`: injection backing-schema uncertainty and analytics definitions.
- `Evals/WORKFLOW.md`, selected Eval and `references/rules/`: scoring and execution.

Raw archive metadata is under `<P>_HarmonyGames_Other_Services/metadata/` in each
universe folder. It describes source scenarios and provenance; it cannot override
evaluation rules, the approved roster, or the task clock (`2026-02-14 00:00 UTC`
or `2025-10-01 00:00 PT`). The Oct 1 universe has 70 storylines; the six that
start later are absent. Historical reports remain historical; refreshed sources
require checking evidence versions.

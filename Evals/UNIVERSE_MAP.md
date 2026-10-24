# Direct-search bundle map

Extract these five folders as siblings in one workspace; run commands there.
The three base folders contain all 13 services from `hg4-2026-08-31.zip` (2026-09-28 download).
The original ZIP and other document folders are not runtime dependencies.

| Folder | Purpose |
|---|---|
| `Evals/` | Stage specifications, `Docs/` guidelines and QC spec, shared contracts, helpers and current references |
| `claude/` | Stage skills, project instructions and local installer |
| `HarmonyGames_GitHub/` | GitHub export including repository blobs |
| `HarmonyGames_Gmail/` | Gmail export including threads and attachments |
| `HarmonyGames_Other_Services/` | All 11 remaining services, including GDrive, Linear, Snowflake and Confluence; original archive metadata |

## Service paths

| Service | Local directory | Exported files |
|---|---|---:|
| contacts | `HarmonyGames_Other_Services/Services_Data/contacts/` | 1 |
| gcal | `HarmonyGames_Other_Services/Services_Data/gcal/` | 1 |
| gdocs | `HarmonyGames_Other_Services/Services_Data/gdocs/` | 1 |
| gdrive | `HarmonyGames_Other_Services/Services_Data/gdrive/` | 30437 |
| github | `HarmonyGames_GitHub/Services_Data/github/` | 255049 |
| gmail | `HarmonyGames_Gmail/Services_Data/gmail/` | 91379 |
| gsheets | `HarmonyGames_Other_Services/Services_Data/gsheets/` | 1 |
| gslides | `HarmonyGames_Other_Services/Services_Data/gslides/` | 1 |
| linear | `HarmonyGames_Other_Services/Services_Data/linear/` | 2028 |
| slack | `HarmonyGames_Other_Services/Services_Data/slack/` | 5357 |
| trello | `HarmonyGames_Other_Services/Services_Data/trello/` | 43 |
| confluence | `HarmonyGames_Other_Services/Services_Data/confluence/` | 1 |
| snowflake | `HarmonyGames_Other_Services/Services_Data/snowflake/` | 1 |

Counts exclude added source manifests. Use `hg_search.py inventory` for source coverage;
`SEARCH.md` describes bounded searches and exact JSON-pointer reads.

## Authorities

- `Evals/references/universe_manifest.json`: selected archive hash and original internal metadata.
- Each service's `source_manifest.json`: extracted paths, SHA-256 and sizes.
- `Evals/references/source_layout.json`: verified collection routing and source fingerprints.
- `Evals/references/tools/catalog.json`: 298 declared tools, 13 services plus gateway.
- `Evals/references/persona/roster.json` and `acl.md`: unchanged 17-person roster and ACL.
- `Evals/references/schema/README.md`: injection backing-schema uncertainty and analytics definitions.
- `Evals/WORKFLOW.md`, selected Eval and `references/rules/`: scoring and execution.

Raw archive metadata is under `HarmonyGames_Other_Services/metadata/`. It
describes source scenarios and provenance; it cannot override evaluation rules,
the approved roster, or the fixed clock `2026-02-14 00:00 UTC`.
Historical reports remain historical; refreshed sources require checking evidence versions.

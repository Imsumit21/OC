# OC

Authoring and evaluation tooling for the HarmonyGames tasks: `claude/`, `Evals/`,
`Task_Authoring/`, plus the skill links in `.agents/skills/` and `.claude/skills/`.

## Add the universe data after cloning

The three universe folders (about 21 GB, from `hg4-2026-08-31.zip`) are not in this
repo. Copy them into the repo root, next to `Evals/`:

```text
OC/
├── .agents/  .claude/  claude/  Evals/  Task_Authoring/
├── HarmonyGames_GitHub/
├── HarmonyGames_Gmail/
└── HarmonyGames_Other_Services/
```

- Keep the folder names exactly as shown; the tools look up paths such as
  `HarmonyGames_Other_Services/Services_Data/slack/`.
- Each folder should directly contain `README.md`, `source_manifest.json` and
  `Services_Data/`. If you end up with `HarmonyGames_Gmail/HarmonyGames_Gmail/`,
  move the inner folder up one level.
- `.gitignore` already excludes them, so they will not be committed.

Then check from the repo root:

```sh
python3 Task_Authoring/tools/hg.py search inventory
```

All 13 services should report `"directory_present": true` and `"manifest_present": true`.

Task inputs, batch runs and `Evals/.cache/` are not in the repo either.

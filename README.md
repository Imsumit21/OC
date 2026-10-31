# OC

Authoring and evaluation tooling for the HarmonyGames tasks: `claude/`, `Evals/`,
`Task_Authoring/`, plus the skill links in `.agents/skills/` and `.claude/skills/`.

The universe data is **not** in this repo. It is distributed separately (two dated
universes, ~16.5 GB and ~7.8 GB of ZIPs) and is git-ignored, so a fresh clone has
no services until you install it.

## What's here

| Path | Purpose |
|---|---|
| `Task_Authoring/` | Task authoring pipeline, tools and task inputs |
| `Evals/` | Stage specifications, contracts, references, search helpers |
| `claude/` | Stage skills and project instructions |
| `.agents/`, `.claude/` | Skill links for the agent harnesses |

```
OC/
├── .agents/  .claude/  claude/  Evals/  Task_Authoring/
├── Universe_Normal/      Normal_HarmonyGames_GitHub/  Normal_HarmonyGames_Gmail/  Normal_HarmonyGames_Other_Services/
└── Universe_SynthCut/    SynthCut_HarmonyGames_GitHub/  SynthCut_HarmonyGames_Gmail/  SynthCut_HarmonyGames_Other_Services/
```

| Universe | Task date | Source | ZIPs |
|---|---|---|---|
| `Universe_Normal/` | Feb 14, 2026 | `hg4-2026-08-31` v37 | `Normal_HarmonyGames_GitHub_part1of3.zip`, `_part2of3.zip`, `_part3of3.zip`, `Normal_HarmonyGames_Gmail.zip`, `Normal_HarmonyGames_Other_Services.zip` (~16.5 GB total) |
| `Universe_SynthCut/` | Oct 1, 2025 | `hg4-synth-sep30cut` v16 | `SynthCut_HarmonyGames_GitHub.zip`, `SynthCut_HarmonyGames_Gmail.zip`, `SynthCut_HarmonyGames_Other_Services.zip` (~7.8 GB total) |

Each universe holds the same 13 services; each `<P>_HarmonyGames_*` folder
contains `Services_Data/<service>/source_manifest.json`. The exact paths each
universe expects are `services.<name>.path` in
`Evals/references/universes/<normal|synthcut>/universe_manifest.json`.

## Install the universe data

`Evals/UNIVERSE_MAP.md` is the authority for archive names, contents and
extraction. Each ZIP holds one base folder at its top level; extract it inside the
matching universe folder. The three GitHub parts share the top folder
`Normal_HarmonyGames_GitHub/` and must merge into it.

Create `Universe_Normal/` and `Universe_SynthCut/` at the repo root, put each ZIP
into its universe folder, then run from the repo root (each line runs in a subshell,
so the block can be pasted as is):

```sh
(cd Universe_Normal && for f in Normal_HarmonyGames_GitHub_part*of3.zip Normal_HarmonyGames_Gmail.zip Normal_HarmonyGames_Other_Services.zip; do unzip -q -n "$f" -x '__MACOSX/*'; done)
(cd Universe_SynthCut && for f in SynthCut_HarmonyGames_GitHub.zip SynthCut_HarmonyGames_Gmail.zip SynthCut_HarmonyGames_Other_Services.zip; do unzip -q -n "$f" -x '__MACOSX/*'; done)
```

The ZIPs can be deleted once the check below reports `ALL OK`. The extracted data
is about 27.3 GB (normal) + 12.9 GB (synth-cut), roughly 770k files, so keep about
65 GB free while the ZIPs are still there.

Use the command line, not Finder. Double-clicking the GitHub parts creates
`Normal_HarmonyGames_GitHub 2` (and ` 3`) instead of merging, and an archive
extracted into a folder of its own name ends up nested twice (`X/X/`). If that
already happened, follow the next section.

### Already unzipped? Move, merge and store the data

If you extracted the ZIPs somewhere else (Finder, `~/Downloads`, another disk),
move the folders into the repo instead of extracting again. Run everything from the
repo root; the examples assume the folders are in `~/Downloads`.

1. **Move** every base folder into its universe folder. On the same disk `mv` is
   instant; from another disk it copies first, so the repo's disk needs the space.

   ```sh
   mkdir -p Universe_Normal Universe_SynthCut
   for d in ~/Downloads/Normal_HarmonyGames_*; do [ -d "$d" ] && mv "$d" Universe_Normal/; done
   for d in ~/Downloads/SynthCut_HarmonyGames_*; do [ -d "$d" ] && mv "$d" Universe_SynthCut/; done
   ```

2. **Merge split folders.** The three GitHub parts hold different files under the
   same top folder. Copy each extra part into the main folder without overwriting
   anything (`-n`):

   ```sh
   (cd Universe_Normal && cp -Rn "Normal_HarmonyGames_GitHub 2/." Normal_HarmonyGames_GitHub/)
   (cd Universe_Normal && cp -Rn "Normal_HarmonyGames_GitHub 3/." Normal_HarmonyGames_GitHub/)
   ```

3. **Undo double nesting.** If a base folder sits inside a folder of the same name
   (for example `Universe_Normal/Normal_HarmonyGames_Gmail/Normal_HarmonyGames_Gmail/`),
   lift the inner one:

   ```sh
   cd Universe_Normal                  # the universe folder that holds it
   X=Normal_HarmonyGames_Gmail         # the doubly nested base folder
   mv "$X" "$X.outer" && mv "$X.outer/$X" . && ls -A "$X.outer"
   rm -r "$X.outer"                    # only once that listing shows nothing but .DS_Store / __MACOSX
   cd ..
   ```

4. **Check, then clean up.** Run the check in [Verify](#verify). Every service must
   be `OK`; the `… 2`/`… 3` folders are still reported as split extractions. Delete
   them (`rm -r "Universe_Normal/Normal_HarmonyGames_GitHub 2" "Universe_Normal/Normal_HarmonyGames_GitHub 3"`),
   run the check again until it prints `ALL OK`, and only then delete the ZIPs. A
   `missing`, `size_mismatch` or `hash_mismatch` result means an incomplete
   extraction: delete that base folder and extract its ZIP(s) again with the
   commands above.

**Where the data lives.** Keep `Universe_Normal/` and `Universe_SynthCut/` as real
folders at the repo root. Tools resolve every service path and refuse one outside
the repo, so a symlink to another disk does not work; to use a bigger disk, move
the whole repo there. Never edit, rename or add files inside them: the tools only
read them, and every file is pinned by its `source_manifest.json` (`--sha256`
re-checks the contents). If a check ever fails, extract the affected ZIP again.

`.gitignore` is whitelist-style — it ignores everything at the repo root and
re-includes only the tooling — so `Universe_Normal/` and `Universe_SynthCut/`
are never committed (`git check-ignore -v Universe_Normal` confirms).

## Verify

```sh
python3 -B Task_Authoring/tools/verify_universe_data.py
```

It is read-only. It compares every service folder with its `source_manifest.json`
(presence and sizes, a few minutes; add `--sha256` to hash every file, about 6–8
minutes), reports split "X 2"/"X 3" folders, base folders left at the repo root,
doubly nested folders, links or other non-files at listed paths, and exits 0 only
when both universes are good. Restrict it with `--universe normal|synthcut`. Then
run a task-scoped check:

```sh
python3 -B Task_Authoring/tools/hg.py search inventory --task-dir <task_dir>
```

That needs a task folder with a filled `00_Assigments.md`; the universe is chosen
by the assignment date, and there is no default.

## Start authoring

- `Task_Authoring/Guide/00_Start_Here.md` — start a task here.
- `Task_Authoring/README.md` — the authoring pipeline.
- `claude/CLAUDE.md` and `Evals/` — review skills and stage contracts.

Task inputs, batch runs and `Evals/.cache/` are not in the repo either.

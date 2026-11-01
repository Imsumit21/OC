# generators — shared injection emitters (Phase 1: Linear)

Plan: `Task_Authoring/plans/Generators_Reuse_Plan.md`. A task writes a **spec** (what to seed, with the origin of every
value); the library expands it into SQL operations, writes them in a restricted grammar, checks the result
independently and publishes only files whose bytes changed. It lives outside `tools/` so it never changes
`__gate_policy__`: the stage gates stay authoritative and certify the artifacts, not this library.

```
python3 Task_Authoring/generators/render.py validate   --task-dir T     # everything in memory, no writes
python3 Task_Authoring/generators/render.py render     --task-dir T [--prune] [--accept-upgrade]
python3 Task_Authoring/generators/render.py check      --task-dir T     # regenerate in memory, diff, never write
python3 Task_Authoring/generators/render.py parse-back --task-dir T [--sql 01_Universe_Inject.sql]   # relative: under T
python3 Task_Authoring/generators/render.py provenance --task-dir T
python3 Task_Authoring/generators/render.py explain    --task-dir T --row linear.linear_comments:<id>
python3 Task_Authoring/generators/render.py store-revision --task-dir T --rev rev4
python3 Task_Authoring/generators/render.py --self-test                # = python3 -B generators/tests/run_tests.py
```

Inputs: `T/00_Assigments.md` (the V3 context is recomputed on every run with `tools/task_context.py`) and
`T/Working_Files/spec/` (`spec.json` + `texts/`). Outputs: `T/Working_Files/build/parts/<service>.sql`,
`provenance.json`, `build_record.json` (no timestamps), and an append-only `upgrades.jsonl`. The task's own assembler
splices the parts into `01_Universe_Inject.sql`; `sql_lint`, `base_check`, `hg.py lint`, `fact_check` and the gates then
run unchanged. SQL is never executed.

## Spec v1 (`spec/load.py`)

Every leaf value is an object with `origin` (`base` | `authored`) and `construction` (`literal` | `reference` |
`transform`); bare values are refused.

| Form | Example |
|---|---|
| base reference | `{"origin":"base","construction":"reference","base":{"service":"linear","collection":"issues","record":"ENG-2366","field":"/priority"}}` |
| authored literal | `{"origin":"authored","construction":"literal","value":"Todo"}` |
| authored text file | `{"origin":"authored","construction":"literal","text":"texts/C1.txt","sha256":"…"}` (bytes hashed, strict UTF-8, no normalisation) |
| reference to another spec field | `{"origin":"authored","construction":"reference","ref":"I1/created_at"}` (`"I1"` = its id; only authored targets) |
| transform | `{"origin":"authored","construction":"transform","fn":"linear.comment_uuid/1","inputs":{…}}` |

Optional on any value: `after` (locators the value must be strictly later than), `cites` (locators whose value must
occur verbatim in the text), `claims` (need a `census` entry: `census/<name>.json` pinned by sha256). Locators:
`base:linear:issues/ENG-2366/created_at`, `spec:I1/created_at`. Top level: `task` (must equal the recomputed context,
incl. `context_hash`), `library.emitters` (pinned versions), `snapshot` (each export file pinned by sha256 and checked
against its `source_manifest.json`), `overrides` (required for an `unverified` convention), `census`, `records`.

Linear kinds, fields and derived columns: docstring of `services/linear.py`. Conventions and their evidence:
`conventions/conventions.json` (`base-verified`, `platform-verified`, `unverified`).

A claim's census file (`census/<name>.json`, format `hg-gen-census/1`) needs the claim id, the scope (entity and
aliases), every service searched with its query, query/result sha256, pages and `complete: true`, the hits classified
(`supports`, `contradicts`, `superseded`, `irrelevant`) and a reviewer disposition whose verdict is `holds`. The checker
cannot tell a wrong census from a right one; it only refuses an incomplete one. Every spec input (spec.json, texts,
census) must lie inside the task folder with no symlink in any path component, and each file is read once: a census
file belongs to one claim, and a text file has one pin and one spelling (names are compared without case, as APFS
does).

## Independent checks (`validate/`)

On the rendered bytes, never on the emitter's data: restricted grammar; parse-back with the eval's tokenizer
(`Evals/tools/hg_injection_lint.py`, sha-pinned, wrapped to fail closed; identifiers matched exactly as PostgreSQL
resolves them); column types, integer ranges and varchar lengths against the live schema (`coltypes.py`); ordered,
typed comparison with the intended operations; overlay on the pinned base export; Linear invariants L1–L12 (FAIL blocks
publication, WARN is recorded — L7 "closed with later activity" and the cross-team parent of L12 are warnings because
the base has them; L1 wants real calendar dates and times); an INSERT must write every NOT NULL column without a
default and nothing may write a generated column; `tools/sql_lint.py` run in its own process in the task's context (a
run that cannot start, takes longer than 900 s — it is then stopped — or does not finish with a report is a blocking
error, shown next to the other findings); and a parser-agreement report listing values the local tools
(`base_check.parse_sql`) read differently from the run (E'' escapes, until plan Phase 2). Un-cited amounts, dates and
ticket ids in authored prose are flagged in the provenance report, not failed (a Phase 1b decision). Early schema/row
checks (`core/emitter.check_op`) only make errors arrive with the record key.

## The code a render runs is the code its record pins

What this guards against: other sessions editing files while a command runs (an edit undone before the end
included), stale `__pycache__` bytecode, and a process that loaded code earlier than the disk now describes. It is a
correctness check for a shared workspace, not a security boundary: a local process that deliberately substitutes code
— swapping whole directories, planting crafted bytecode, installing its own import hooks — could as well edit the
library itself.

The library's own modules (`generators/__init__.py`) and the `tools/` modules it runs in-process (`task_context`,
`runtime_context`, `sql_lint`, `base_check` and what they import from `tools/`; `core/context.py`) are executed from
the bytes read once, hashed and stamped as they load — never from `__pycache__` bytecode, and with each file's own
`__future__` flags — and those hashes are what the build record pins. `render` and `check` refuse to start, and fail
before they conclude, while the process may be running library or `tools/` code the disk no longer holds (`LIBRARY
CHANGED` / `TOOLS CHANGED`: run the command again):
- a file whose bytes changed since it loaded, or that was modified at all since (its stamp moved — device, inode,
  size, mtime, ctime — even if the old bytes were put back), or that the process ran from two different contents;
- a module below the package that another loader loaded, or that was executed again (`importlib.reload`, a
  re-import after its removal from `sys.modules`, or the finder running a module another loader had run first);
- a module whose own functions or classes were replaced by new ones of the same module, or a function or class one
  library module took from another (`from .x import f`) that is no longer that module's own — the traces any re-run
  of a module leaves, whatever the route (a reload by another loader, a loader called directly);
- a pinned `tools/` module replaced in `sys.modules`, reloaded through another loader, or whose own functions or
  classes are no longer those its pinned bytes defined; a module named like one of the closure that was already
  imported (from anywhere); a `tools/` module loaded outside the closure;
- a bytecode cache anywhere under the library.

A module re-run from its pinned bytes without replacing any function or class it defines (an empty package
`__init__.py`, say) is not reported: nothing different runs.

The `tools/` closure files and the data files validation and `tools/` read (`core/context.DEPENDENCY_FILES`: the live
schema and constraints, both `injection.json`, the eval tokenizer and `hg_universe.py`, `conventions.json`) are
stamped before the closure is imported (`sql_lint` reads two of them at import); any later modification refuses the
process the same way, so an edit to them — even one undone — while the `sql_lint` subprocess (which loads `tools/`
from disk itself) runs is caught. A dependency file absent when the closure loads is watched through its nearest
existing folder: a file created there and removed again moves the folder's stamp (adding or removing an entry does;
editing a file in place does not). A metadata change (`chmod`, an extended attribute) also moves ctime: it refuses a
run that did not need refusing, never the other way round. The library is meant to run one command per process; a
long-lived process refuses once any of these files changes.

Not covered: a whole directory (say `tools/`) renamed away and back while a command runs leaves every file's stamp
unchanged; replacing an attribute of a loaded library module with a function from outside the library
(`mock.patch`, as the tests do) leaves no trace these checks look for; and `generators/__init__.py` and `render.py` are
compiled by Python itself before the finder exists (each is hashed and stamped from a read made as it starts) —
`render.py` and `tests/run_tests.py` import the package with bytecode reading disabled, and any other importer must do
the same (`sys.pycache_prefix` or `PYTHONPYCACHEPREFIX`), because a cache crafted for the bootstrap would run before
any check could.

## Publication (`core/output.py`)

Per-file write-if-changed (unchanged files keep their mtime) under a per-task lock. Just before acting on a target,
`publish` re-hashes it, the unchanged ones included, and refuses one that changed since the plan. Before publishing,
`render` re-checks everything the build read — the spec files, the assignment, the pinned base exports and their
source manifests, the task context recomputed from scratch and the pinned dependencies — and publishes nothing if any
changed. Other processes' edits can be detected, not prevented, so the same check runs again after the outputs are
replaced and after the build record is written: a change found there fails the render and leaves the record
disagreeing with the disk, and `check` (which re-checks the same at its end) fails for as long as the two disagree (a
disagreement that begins while a check runs is reported by the next one). Any error raised once the outputs are
published — whatever its kind, an interrupt included — carries a note listing the files already published (the build
record too, once written), and the CLI prints it; cleaning up a staging folder never raises.
Inputs, base exports and manifests are compared by content: each is read once or checked against its pin whenever it
is read, so the build used exactly the bytes the record pins; the code and dependency files above are compared by stamp
as well. An accepted upgrade is logged in `upgrades.jsonl` just
before the record is written, and a line equal to the log's last line is not added again, so a render repeated after a
failure in between logs it once. `--prune` removes only files an earlier build wrote and nobody edited (an unpruned stale
file stays owned in `stale_outputs`); the previous build record must have the shape this library writes — every
output it lists is `Working_Files/build/provenance.json` or `Working_Files/build/parts/<service>.sql`, spelled
canonically — so a hand-edited record cannot point a prune anywhere else. Stored revisions under
`Working_Files/run_forensics/` are written only by `store-revision`, which never overwrites one (no-clobber link, under
the lock); nothing else here can stage, replace, append to, prune or delete a path there — refused by name wherever a
`Working_Files/run_forensics` folder appears in the absolute path, the task folder included (each component compared
after Unicode compatibility and case folding), and by the folder's device and inode; `store-revision` refuses a task
folder that lies inside one, and clearing a staging folder keeps a stored-revision folder found inside it (the build
then refuses, naming it). Nothing is written into an existing file: a new file replaces it, so a hard link to the
old file keeps its bytes. A command resolves `--task-dir` once, where it starts, and locks, builds and publishes that
one path; the library never resolves it again: every folder from `/` down to it must be a real folder, and every read
and write of a task file walks from `/` to its folder one level at a time with `O_NOFOLLOW` and acts on that folder's
descriptor. The lock also pins the task folder's device and inode, and while it is held every walk checks that the
folder at the task path is still that one. So a task folder replaced — by a symlink or by another real folder — is
refused before anything inside it is touched, and nothing is written into another task: a replacement before
publication starts publishes nothing, and one while files are being published stops the publication, with the error
listing what was already written into the original folder (its own outputs, through descriptors opened before the
swap). Out of reach of any check made in user space: another process moving a folder the library holds open (for
example into a stored-revision folder) between the check and the next system call on that folder's descriptor; the
library refuses symlinks and re-checks names and identities at every step, but cannot lock the folder tree against
moves. The `tools/` code the library calls resolves
the path itself: the task context it computes in-process must equal the spec's pinned `context_hash` and is recomputed
before publishing, but the `sql_lint` subprocess reads the context on its own, so a task folder swapped for another
task's and put back while that subprocess starts is not detected (Linear's freeze bound is also enforced by the
library's own invariants, with the pinned context). Drift refusal: if a pinned dependency changed
since the last build — the library, conventions, the schema and constraint files validation reads (an absent optional
file is pinned as absent), the eval parser, the `tools/` closure above, emitter versions — `render` refuses without
`--accept-upgrade` and `check` fails. Not a bundle transaction: a crash between two replaces leaves a mixed state that
`check` reports.

## Tests

`python3 -B Task_Authoring/generators/tests/run_tests.py [-k PATTERN] [-v]` from the workspace root. Temp folders live
under `Task_Authoring/support/scratch/` and are removed; nothing is written under `Evals/`, `tools/` or the universes.

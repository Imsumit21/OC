# Archived task workspaces

Each folder is a byte-for-byte archive of a task workspace, copied before a new
task replaced `Task_Authoring/task_inputs/`. Archives are read-only evidence:
do not edit them, run `git` inside them, or execute their SQL.

| Folder | Task | Status | Archived | Files | Verification |
|---|---|---|---|---|---|
| `dd-q4-claims-register_skipped_2026-10-30/` | dd-q4-claims-register — Julia Lawson / Product Management / Retrieval | Skipped by the user after the platform `/prompt` FAIL (score 2); no repair applied | 2026-10-30 | 39 + `ARCHIVE_MANIFEST.tsv` | Source and archive hashed file-by-file; identical; symlinks preserved (none present) |

Notes:
- The task was skipped, not completed. Its platform reports under
  `plateform_reports/` are the evidence for the FAIL; the archive preserves
  them unchanged.
- The proposed repair in the final turn was not applied. Independent
  methodology verification was unavailable (Claude rate limit), so the work
  stopped rather than self-verify.
- Task-specific inputs and findings in an archive do not carry into a new task.
  See `/Users/sumitkumar/Source/Outlier/OC/learnings` for the cross-task lessons.
- `ARCHIVE_MANIFEST.tsv` lists size and SHA-256 for every archived file. To
  re-verify, hash the archive contents and compare against that manifest.

# surface.gradeable on task 1's current surface (read-only; real decoder dry run)

Surface: `Task_Authoring/task_inputs/Working_Files/01_Gradable_Surface.json` — never edited by this session (the build session owns it). Current sha256 `da9d2233e513d725303fb016664fbbbee278767ee6cce557c1067d4cc68b5635`.
Result: **PASS** — 30 gradable, 0 ungradable.

Command: `python3 -B Task_Authoring/tools/gradable_surface.py gradeable-report --task-dir Task_Authoring/task_inputs`

Each slot is dry-run: a synthetic truth side and write payload are built for its selector class, decoded by
`surface_grader.decode()` and graded by `surface_grader.grade()`; the slot must read True, and the same truth with
nothing delivered must read False (a slot that passes with nothing is not a certification).

| slot id | weight | ungradable reason |
|---|---:|---|
| — | — | none: every selector class reads on a fixture built for it |

Certified (30): REG-SHIP, REG-HOLD, REG-DROP, REG-VOL, REG-R1, REG-R2, REG-F2, REG-A1, REG-C1, REG-TICKET, REG-TICKET2, REG-FMT, REG-DATE, PACK-VOL, PACK-US, PACK-FR, PACK-IT, PACK-JA, PACK-DE, PACK-LOCALE, PACK-FMT, PACK-SLOTS, PACK-W1, PACK-W2, MAIL-W1LINE, W-TICKETS, W-MAIL, W-MAIL-SUBJ, W-TRELLO, W-SUMMARY-DEST

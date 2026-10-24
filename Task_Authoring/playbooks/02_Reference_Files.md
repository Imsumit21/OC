# 02 — Reference Files (Playbook) — HarmonyGames · Spec V2

> Command: `/create-reference-files` (optional step) · Writes: `task_inputs/02_Reference_Files/` + `task_inputs/Working_Files/02_Reference_Files_Manifest.md` · Paired eval: none of its own. `/prompt`, `/hardness`, `/oe` and `/rubric` all take the files the prompt uses (`Evals/WORKFLOW.md` "Reference files used by the prompt") · Gate: **`tools/stage_gate.py reference-files` (blocking)** · Read first: `setup/GEN_EXECUTION.md`

## Purpose

Author the files the persona "attaches" to the request. Use them only when the scenario
needs an attachment the agent has to read (`2_Overall Task Flow - V2.md` §4). If the universe
alone carries the task, write `Reference files: none`, leave the folder **empty** and skip
both upload screens.

A good file reads like the persona's own local copy (an export, a download, a working
sheet). It gives the agent inputs, never the answer. It carries either evidence the task
needs, or a framed non-authoritative starting point that the agent must reconcile against
the system of record.

## How the agent meets the files (`references/Taxonomy_V2_Step_Map.md` Screens 17–20 + the agent system prompt)

- **Upload.** One folder (`maxFolders: 1`) goes to Upload Reference Files. The same files go to Re-Upload as individual attachments (allowed: CSV, XLSX/XLS, DOCX/DOC, PDF, TXT, JSON, XML, HTML, MD, images, ZIP, code, YAML, PPT/PPTX, RTF). So keep the folder **flat**.
- **Mount.** The files are mounted for every agent run at `/app/artifact`. The system prompt (the `system_prompt` column of the platform task-upload CSVs) tells the agent: "Attached or uploaded files are mounted at /app/artifact … When the user names a file, list that directory first rather than guessing the filename, real names often carry timestamps." The agent looks only when the prompt refers to an attachment. Native timestamped names are expected.
- **Reading.** The agent reads files with its own runtime (Read, Bash, python3), not with MCP tools. A large file is read in chunks (oversized results spill to a file the agent pages through). Which extraction tools exist in the container (DOCX/XLSX/PPTX, `jq`) is unverified — confirm in the pre-check before a fact depends on one.

  V1 evidence (V1 HarmonyGames task 2, the prompt referred to both files naturally). In 6 of 6 rollouts:
  - the agent's first move was `ls -la /app/artifact`;
  - it read the PDF with the native Read tool;
  - it read the CSV with Read or `cat`.

  Only PDF and CSV are proven.
- **Verification.** The same system prompt says "check primary data sources directly rather than relying solely on secondhand references". The agent is primed to verify a file against the systems of record. A stale attachment on its own does not make Opus fail, so it is not a hardness mechanism (`Hardness_Mastery.md` §10). In the same V1 task the attached tracker listed a reverted font change as shipped, and all 6 final responses discussed the revert.

## Inputs / Output

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`
and read `Working_Files/00_Task_Context.json` (GEN_EXECUTION § 0). Use all eight
assignment fields, the assigned freeze and the context's registered universe/KB source.
Both freeze dates use the same local universe data. Check each relied-on fact at
the assigned freeze; shared KB summaries are leads, not a separate dataset gate.
V3 changed-topic rules take
precedence over older Evals/V2 references; local authorship and hardness-profile
exceptions remain as recorded in GEN_EXECUTION § 2 and § 3a.

Inputs
- `00_Assigments.md`, `01_Grounding_Dossier.md`, `01_Universe_Inject.sql`, `01_Hardness_Manifest.json`, `03_Error_Async_Config.txt` (async targets the files must not name).
- `references/Native_Artifact_Anatomy.md` (§M for upload shapes; the service sections for the source record).
- The universe, through `tools/hg.py search`. Every fact in a file is grounded and cited.

Output
- `task_inputs/02_Reference_Files/`: the flat upload folder, with the template `README.md` **deleted**.
- `task_inputs/Working_Files/02_Reference_Files_Manifest.md`: kept **outside** the folder, never uploaded. It includes a Self-review section.

## Hard gates

1. **Earns its place.** Each file carries evidence the task needs or a deliberate, framed non-authoritative input. No decorative files and no minimum count. A file that copies a universe record verbatim short-circuits discovery, so it does not earn its place.
2. **Nothing but task files is uploaded.** Delete the template `README.md`; anything left in the folder is visible to the agent at `/app/artifact`. Upload no manifest, no notes and no subfolders. If there are no files, skip both screens.
3. **Readable by the agent.** Prefer csv, md, txt, json, or pdf with a text layer. No zip archives (an extra unpacking step, unproven, and it hides files from the listing). Use docx, xlsx or pptx only when the native kind demands it, and then confirm in the Opus pre-check that the agent listed `/app/artifact` and extracted the content. An unreadable required file fails Feasibility.
4. **Native fidelity.** Mirror the export or download shape of the source system (`Native_Artifact_Anatomy.md` §M). Open 2–3 real sibling records and match their layout, length band, naming, date idioms and the universe's redaction tokens (`PERSON_####_NAME`, `SVC_####_EMAIL`…). Ship no Drive `-info.json` sidecar. No QC row scores file realism directly, but a planted-looking file invites a Pre-solved or Coherence finding.
5. **Grounded and truthful.** Every fact traces to a real or seeded record, cited in the manifest. The only permitted "errors" are staleness, omission and rough hand-kept numbers. Each one is deliberate, recorded, and overturned by an authoritative source the persona can read. An unrecorded disagreement fails Cross-service Coherence.
6. **Fair outcomes and clear references.** Each attachment reference must identify an accessible file. Record competing fair interpretations and accept all of them in brief §4b and the rubric. A non-authoritative attachment may be stale only when a useful evidence path reaches the governing source; do not use a file to conceal the deciding evidence.
7. **Not pre-solving.** No file contains the finished deliverable, states the conclusion, or names the target an async wait or a search chain depends on (Investigation = **Fail – Pre-solved**). The Evals accept a file only when it "supplies instructions or context rather than a precomputed answer".
8. **Incorporation decides what is graded.** A rule or instruction inside a file becomes a requirement only if the prompt clearly directs the agent to follow that file (`Evals/WORKFLOW.md` `prompt-incorporation-v1`). Otherwise it is context, and any criterion built on it is unauthorized. Record in the manifest which files are incorporated and through which prompt reference.
9. **Assigned freeze.** Both dates use the same local data. Seeded timestamps and dated claims in files/filenames must fit the assigned freeze and must not imply completed events after it; later deadlines or scheduled events may be future. Establish earlier mutable content from dated history or independent earlier evidence. Use Pacific plus UTC when days differ. Do not rely on file-system dates.
10. **Natural reference is a prompt constraint, not prompt text.** Record how the persona would refer to each file (what it is, from whom, why they have it) and the words the prompt must avoid: paths, `/app/artifact`, IDs, "File Artifact Universe", opaque or generated filenames (Contrived). The human writes the sentence.
11. **Gradable.** Each file supports at least one "Facts for the human" entry: a locator (page/sheet/row/section) and its value. The human can then write an Oracle Event that reads the file and an Outcome that fails an agent who ignores or over-trusts it.
12. **Identical and frozen.** Upload the same files on both screens. Record the run-time listing (the pre-check's `ls /app/artifact`) in the manifest: it is the only proof of what the agent had. *(V1 Task2: the run-time mount held 2 files. The task folder now holds 9, seven added hours after the baseline, including an xlsx and a zip, and the manifest describes 2. The record copy no longer matches the task.)* A change after the prompt exists means the human re-checks the prompt. A change after a run invalidates the downstream work (`Evals/WORKFLOW.md`): re-run `/prompt`, the pre-check and `/hardness`, the OE and rubric checks, and the baseline.

## Procedure (checklist)

- [ ] Decide whether an attachment genuinely belongs. If not, write the manifest with `Reference files: none`, empty the folder (README included) and stop after the Self-review.
- [ ] Per file: choose the native kind and its export shape (§M), open the sibling records, and build the file from cited facts. Bury the signal at a realistic depth and place any staleness where the authoritative source overturns it.
- [ ] Check gates 5–9 against the dossier, the manifest traps, the async targets and the clock.
- [ ] Write the manifest (spec below), then the Self-review.

## Manifest spec (`02_Reference_Files_Manifest.md`)

Per file:
- **File:** exact name, format, size.
- **Role:** evidence, or non-authoritative starting point.
- **Native model:** kind, export shape, and the sibling records mirrored (cited).
- **Grounded in:** the records it draws on (cited).
- **Deliberate inaccuracies:** each one, with the authoritative source that overturns it.
- **Incorporated?** Through which prompt reference, or "context only".
- **How the persona would refer to it:** a description only.
- **Must not appear in the prompt.**
- **Facts for the human:** locator → value.

Footer:
- Folder listing (README removed: yes).
- Readability check: the pre-check showed `/app/artifact` listed and each file read, yes/no, with the run-time `ls` output pasted.
- Files to supply with `/prompt`, `/hardness`, `/oe` and `/rubric`.

## Self-review (GEN_EXECUTION §6a, record it in the manifest)

1. **Walk the checks in order.** Read `Evals/WORKFLOW.md` "Reference files used by the prompt" and "Task requirement authority", then `Evals/1_Prompt_Eval.md` "Requirements Incorporated from Reference Files", Feasibility §2.2 B and Phase 3 coherence. Walk them against each file and the manifest.
2. **Counter-readings.**
   - Read only the files and try to reach a wrong final state, or the answer itself. If you can, the authoritative source is too weak, or the file pre-solves.
   - Try to find a second file that fits a prompt reference.
   - Try to find an unrecorded disagreement with the universe.
   - Check whether any design note counts the file's staleness as a difficulty mechanism. It is not one (V1: 6 of 6 rollouts caught the stale row). Move the difficulty into the universe.
   - For `none`, ask whether the prompt implies an attachment ("the sheet I sent you"). If it does, none is wrong.
3. **Re-verify** every cited fact through `hg.py` under the persona's ACL, not from the dossier.
4. **Mechanics.** List the folder: task files only, flat, allowed types, README gone. After the pre-check, diff the folder against the run-time `ls`: they must be identical.
5. **Record** each verdict with its evidence, each counter-reading and how it was resolved, and anything left unresolved (gate minimum: one evidenced counter-reading per file and at least five; two for `none`).

## Deliver

Run `python3 Task_Authoring/tools/stage_gate.py reference-files Task_Authoring/task_inputs --paste`; handoff is blocked until it prints `STAGE GATE reference-files: PASS`, and `--paste` writes that output into the Self-review of `02_Reference_Files_Manifest.md` (the next stage's gate refuses an upstream artifact without a current PASS block). The gate checks the flat folder (no README, subfolder or zip), that every file is described, every per-file field, and that each `Grounded in:` line cites a record.

Report the file list (format, role, incorporated or not), the deliberate inaccuracies and what
overturns each, the prompt constraints for the brief, and the upload reminders:
- the same flat folder on both screens, with the README deleted;
- supply the files with `/prompt`, `/hardness`, `/oe` and `/rubric`.

Next: `/create-prompt-writing`.

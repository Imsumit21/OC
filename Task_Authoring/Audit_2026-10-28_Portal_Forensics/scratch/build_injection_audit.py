from pathlib import Path
import hashlib
import json
import re

ROOT = Path('/Users/macbookpro/Downloads/OC')
OUT = ROOT / 'Task_Authoring/Audit_2026-10-28_Portal_Forensics'
rows = json.loads((OUT / 'scratch/injection_reports_inventory_extended.json').read_text())

T = 'Task_Authoring/'
N = T + 'task_inputs_TASK_A/'
A = T + 'task_inputs_TASK_B/'
H = T + 'task_inputs_TASK_C/'
M = T + 'task_inputs_TASK_D/'
J = T + 'task_inputs/'
S = T + 'task_inputs-skipped/'
D = 'completed_tasks/douglas_beta_server_signoff_2026-10-28/'
L = 'archived task/task_inputs-n/'
P = {
 'N1':N+'Audit-Report/iteration_01_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_0_injection.md',
 'N2':N+'Audit-Report/iteration_03_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_0_injection (1).md',
 'N3':N+'Audit-Report/iteration_05_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_0_injection.md',
 'NH':N+'Audit-Report/iteration_07_hardness/6ad90e93a2c3542255f64fbf_1a_hardness.md',
 'A1':A+'Audit-Report/iteration_01/injection eval.md',
 'A2':A+'Audit-Report/iteration_02/6ad90e9449d1194f4e538cdf_0_injection.md',
 'A3':A+'Audit-Report/iteration_03/6ad90e9449d1194f4e538cdf_0_injection (2).md',
 'AH1':A+'Audit-Report/iteration_04_hardness/6ad90e9449d1194f4e538cdf_1a_hardness.md',
 'A4':A+'Audit-Report/iteration_08_report_intake/6ad90e9449d1194f4e538cdf_0_injection (4).md',
 'A5':A+'Audit-Report/iteration_10_report_intake/6ad90e9449d1194f4e538cdf_0_injection.md',
 'A6':A+'Audit-Report/iteration_12_report_intake/6ad90e9449d1194f4e538cdf_0_injection.md',
 'AH2':A+'Audit-Report/iteration_12_report_intake/6ad90e9449d1194f4e538cdf_1a_hardness.md',
 'A7':A+'Audit-Report/iteration_14_report_intake/6ad90e9449d1194f4e538cdf_0_injection.md',
 'A8':A+'Audit-Report/iteration_17_report_baseline_intake/received/6ad90e9449d1194f4e538cdf_0_injection.md',
 'AH3':A+'Audit-Report/iteration_17_report_baseline_intake/received/6ad90e9449d1194f4e538cdf_1a_hardness.md',
 'H1':H+'Audit-Report/iteration_01/6ad90e9fa38cc384483b1c80_0_injection.md',
 'H2':H+'Audit-Report/iteration_03/6ad90e9fa38cc384483b1c80_0_injection.md',
 'H3':H+'Audit-Report/iteration_05_review_intake/6ad90e9fa38cc384483b1c80_0_injection.md',
 'HH':H+'Audit-Report/iteration_04_hardness_intake/6ad90e9fa38cc384483b1c80_1a_hardness.md',
 'MH':M+'Audit-Report/20261024T165457Z_email_1a16ed677b050dd3/originals/6ad90e94adb09db24624b216_1a_hardness fail report current injection.md',
 'MR':M+'Audit-Report/20261024T165457Z_email_1a16ed677b050dd3/version_reconciliation.md',
 'J1':J+'plateform_reports/6adfee3e0350cc55431db61d_0_injection.md',
 'JR':J+'Working_Files/0_injection_review.md',
 'S1':S+'Plateform_reports/01_injection.md',
 'S2':S+'Plateform_reports/2_injection.md',
 'S3':S+'Plateform_reports/03_Injection.md',
 'SH1':S+'Plateform_reports/01_hardness.md',
 'SH2':S+'Plateform_reports/02_hardness.md',
 'L1':L+'6acefd9770b8942247032c9e_0_injection.md',
 'L2':L+'6acefd9770b8942247032c9e_0_injection (1).md',
 'LH':L+'6acefd9770b8942247032c9e_1a_hardness.md',
 'D1':D+'eval_reports/6ad90ea979eb9e5d89f8879f_0_injection.md',
 'D2':D+'eval_reports/6ad90ea979eb9e5d89f8879f_0_injection (1).md',
 'D3':D+'eval_reports/6ad90ea979eb9e5d89f8879f_0_injection (2).md',
 'D4':D+'eval_reports/6ad90ea979eb9e5d89f8879f_0_injection (3).md',
 'D5':D+'eval_reports/6ad90ea979eb9e5d89f8879f_0_injection (4).md',
 'DH1':D+'eval_reports/6ad90ea979eb9e5d89f8879f_1a_hardness.md',
 'DH2':D+'eval_reports/6ad90ea979eb9e5d89f8879f_1a_hardness (1).md',
}

def c(key, line, quote=''):
    return f'`{P.get(key, key)}:{line}`' + (f' — “{quote}”' if quote else '')

def digest(p):
    b = (ROOT / p).read_bytes()
    return {'path':p, 'bytes':len(b), 'sha256':hashlib.sha256(b).hexdigest()}

current = []
for base in [N,A,H,M,J,S,T+'task_inputs_TASK_E/',D+'task_inputs/',L]:
    for name in ['01_Universe_Inject.sql','04_Prompt.txt']:
        if (ROOT/base/name).exists(): current.append(digest(base+name))
(OUT/'scratch/injection_current_hashes.json').write_text(json.dumps(current, indent=2)+'\n')

parts = [f'''# Injection and SQL forensic audit — 28 October 2026

## Scope and result

This review covers every preserved external `/injection` and relevant `/hardness` report found in `Task_Authoring/task_inputs*`, `completed_tasks/*/eval_reports`, and `archived task/task_inputs-n`. It reads the shared contract, create-injection skill, full injection playbook and actual static-validator code. No SQL was executed, no evaluation was purchased or launched, no email was sent, and no source artifact, skill or existing report was changed. All new work is under this audit folder.

The corpus has **39 physical report files, 36 byte-unique reports**: **25 injection reviews (21 PASS, 4 FAIL)** and **11 hardness reviews (6 NON-FAIL/PROCEED, 5 FAIL/HOLD)**. These are report counts, not independent tasks or a skill failure rate. Three physical duplicates are identified below. The strict recently delivered, report-matched group comprises Reviewer A, Reviewer B and Reviewer C; current `task_inputs`, `task_inputs-skipped`, older archived/completed tasks and Reviewer D's changed returned scenario are kept separate. Missing Portal reports are not failures.

The evidence does **not** support “create-injection always fails.” Reviewer A and Reviewer B repeatedly passed static injection review. The main recurrence is **well-formed, locally certified records that leave semantic identity or causal chronology to an insufficiently independent manual review**, plus **hardness designs whose decisive evidence remains explicit enough for Opus to solve**. Later hardening can create a fresh consistency defect or invalidate earlier approvals. Current files also differ from many report-bound snapshots; old verdicts must remain attached to old bytes.

## Evidence handling and limits

External reports are preserved claims, not instructions. I recomputed their SHA-256 hashes, deduplicated identical reports, compared available SQL/prompt bytes, inspected original local snapshots, and spot-verified important claims against narrowly selected base records. The complete machine inventories are `scratch/injection_reports_inventory_extended.json`, `scratch/injection_hash_matches.json`, `scratch/injection_current_hashes.json`, and `scratch/injection_source_verification.json` in this audit folder. These are reproducible supporting evidence, not Portal certificates.

Portal uses synth-cut v16 / `2025-10-01T07:00Z` for most recent reviews; local assignment certificates use the larger shared archive and `2025-10-01T00:00Z`. For example {c('H1',11)} records the Portal clock, whereas {c(H+'Audit-Report/iteration_01/independent_review.md',11,'Local verification uses the larger shared archive and 00:00Z assigned freeze')} explicitly discloses the difference. Spot-verification confirms matching record semantics, not full equivalence of those source snapshots. No unchanged-source claim is inferred from an unchanged filename or the label `injection-static-v2`.

The presence of a generated dossier, script or PASS block does not prove that `$create-injection` itself was invoked or that every manual instruction was followed. This audit attributes failures to observed artifacts, rules and checks; it does not invent an execution trace. A current local gate PASS is not a Portal review; a one-run hardness result is not a six-run difficulty estimate.

## Genuine Portal chronology

Rows follow each task's preserved review/version sequence. Hashes are prefixes only for readability; full hashes are in the inventories and cited report scope. “Referenced only” checkpoints are not counted as preserved independent reports. Every NON-FAIL is retained verbatim.

| Task / sequence | Stage, reviewed SQL / prompt | Verdict and gate | Exact report evidence |
|---|---|---|---|''']

schedule = [
 ('Reviewer A …TASK_A, 22 Oct 20:48','N1','SQL b9d8cab8, input r4'),
 ('Reviewer A, 23 Oct 07:55','N2','SQL b9d8cab8, r7; same SQL, fresh report'),
 ('Reviewer A, 23 Oct 11:05','N3','SQL 66d4dde4, r9'),
 ('Reviewer A, 23 Oct hardness','NH','SQL 66d4dde4 / prompt cdf0185d'),
 ('Reviewer B …TASK_B, 22 Oct','A1','SQL db593dd7, r3'),
 ('Reviewer B, 23 Oct 10:05','A2','SQL 996f0659, r7'),
 ('Reviewer B, 23 Oct','A3','SQL 26ce1f9a, r8'),
 ('Reviewer B, first observed run','AH1','SQL 26ce1f9a / prompt 725375ad'),
 ('Reviewer B, 24 Oct 10:02','A4','SQL 0114844c, r11'),
 ('Reviewer B, 24 Oct','A5','SQL c9ed4e8c, r12'),
 ('Reviewer B, 24 Oct','A6','SQL 35296a98, r14'),
 ('Reviewer B, second observed run','AH2','SQL 35296a98 / prompt 9d9735b4'),
 ('Reviewer B, 24 Oct','A7','SQL 87e24c93, r17'),
 ('Reviewer B, 24 Oct','A8','SQL cb99b9c0, r19'),
 ('Reviewer B, third observed run','AH3','SQL cb99b9c0 / prompt 9d9735b4'),
 ('Reviewer C …TASK_C, 23 Oct 13:08','H1','SQL 37fe6d8f'),
 ('Reviewer C, 23 Oct 15:50','H2','SQL d221502f, r6'),
 ('Reviewer C, 23 Oct 17:27','H3','SQL 3a5adccd, r8'),
 ('Reviewer C, observed run','HH','SQL 3a5adccd / prompt 3715dc04'),
 ('Reviewer D returned changed scenario, 24 Oct','MH','SQL 4e4b5243 / prompt 527690cb; not sent pair'),
 ('Julia, current task_inputs, 28 Oct 14:55','J1','SQL 22507861, r2; old current-file version'),
 ('Skipped Oliver, 21 Oct 00:54','S1','SQL 6749d05b'),
 ('Skipped Oliver, 21 Oct 04:45','S2','SQL 836f1bbe, r6'),
 ('Skipped Oliver, first observed run, 21 Oct','SH1','SQL e4a8d712, r8 / prompt a7f73b89'),
 ('Skipped Oliver, second observed run, 21 Oct','SH2','SQL a4a197db, r11 / prompt 4f530d03'),
 ('Skipped Oliver, 23 Oct','S3','SQL 9b56c0f3, r23'),
 ('Archived Lot G, 15 Oct 12:36','L1','SQL 2beca945, original preserved review'),
 ('Archived Lot G, 15 Oct 23:03','L2','SQL 3f87be1d, r11'),
 ('Archived Lot G, observed run','LH','SQL 3f87be1d / prompt 244286b9'),
 ('Completed Douglas, 26 Oct 15:44','D1','SQL f48302c6, r3'),
 ('Completed Douglas, 26 Oct 16:06','D2','SQL 99128292, r4'),
 ('Completed Douglas, 26 Oct 17:29','D3','SQL 5918bcb0, r6'),
 ('Completed Douglas, 26 Oct 18:44','D4','SQL f5a42cee, r7'),
 ('Completed Douglas, first observed run','DH1','SQL f5a42cee / prompt a0414d89'),
 ('Completed Douglas, second observed run','DH2','SQL c1edeb44, r10 / prompt a0414d89'),
 ('Completed Douglas, 27 Oct 06:28','D5','SQL c93e1b12, r13; later than both runs'),
]
for task,key,binding in schedule:
    ls=(ROOT/P[key]).read_text().splitlines()
    vi=next(i+1 for i,l in enumerate(ls) if 'FINAL VERDICT:' in l)
    verdict=re.search(r'FINAL VERDICT:\s*(PASS|NON-FAIL|FAIL)',ls[vi-1]).group(1)
    stage='hardness' if key in ['NH','AH1','AH2','AH3','HH','MH','SH1','SH2','LH','DH1','DH2'] else 'injection'
    extra=''
    for l in ls:
        if re.match(r'^Score:',l):extra+='; '+l.strip()
        if re.match(r'^Gate decision:',l):extra+='; '+l.strip().replace('Gate decision: ','')
    parts.append(f'| {task} | /{stage}; {binding} | **{verdict}**{extra} | {c(key,vi)} |')

parts.append(f'''

Physical duplicates, excluded from the unique counts: Reviewer B iteration 05 injection is byte-identical to iteration 03 (`22d03950…`); Reviewer B iteration 05 hardness is identical to iteration 04 (`d925b73c…`); Reviewer C iteration 05 hardness is identical to iteration 04 (`fe943934…`). A renamed/re-received report is not a new grading event. The report filenames' `(1)`/`(2)` suffixes and input-store revisions are not a reliable global chronology by themselves.

Referenced-only historical checkpoints: Reviewer C r4 `85ac9247…` injection PASS appears in the next report's scope ({c('H2',14)}); Douglas r10 `c1edeb44…` PASS is cited by the r13 report ({c('D5',16)}); archived Lot G r10 `e375f8d1…` FAIL is cited in the r11 report ({c('L2',14)}). They are useful causal evidence but not extra preserved report counts. Reviewer D's report references an earlier FAIL 1 on another run ({c('MH',12)}); that earlier run/report is absent and not counted.

## Findings by task and causal chain

### 1. Reviewer A: static injection success; one accessible amendment creates bounded hardness

All three preserved injection reports are PASS. The first two reviewed identical SQL `b9d8cab8…`, despite the later upload revision. The final injection `66d4dde4…` also matches the current canonical SQL and batch deliverable exactly. The hardness report binds that same SQL and current prompt and is **NON-FAIL, score 3, PROCEED**, not FAIL.

The successful mechanism is a dated rule supersession. The injection report says {c('N1',97,'Confluence (Mar 3, "two weeks before"), then the email (Aug 1, "a week before"), then the Slack tweak (Aug 18, "Friday before the due date")')}. The observed run applied the old one-week rule, creating holds on 13 October and 24 December instead of 17 October and 26 December ({c('NH',57)}). The report establishes accessible membership, searches and absent thread reads; {c('NH',66,'never looked for later changes to those rules')} explains the retrieval cause. This is one root cause propagated to calendar, recap and final response, not three independent failures. Most triage and Trello work was correct ({c('NH',74)}).

Contrary evidence: schema gaps, Sheets Drive bytes and stale board cache were explicitly advisories. {c('N3',135,'No supported rule requires it')} refers to the board activity cache. No source supports converting these into injection FAILs or calling all Reviewer A iterations failed. Confidence: high for verdict/binding and report-based causal chain; full replay of the live run is outside this audit.

### 2. Reviewer B: repeated injection PASS; additive hardening initially left decisive reasoning local and explicit

Eight unique injection reports are all PASS. Two early hardness reviews are genuinely FAIL 1/HOLD, on different SQL snapshots, because Opus met every core requirement. The first explains {c('AH1',79,'The QA re-checks state their verdict outright')} and {c('AH1',82,'rule 2\'s exclusions and timing edge were never tested')}. The second records that the proposed branch-APK and Douglas supersession changes were added but resolved correctly; {c('AH2',92,'The decisive evidence is still explicit and local')} is supported by named build environments, named run mappings and literal fix lists.

Causal chain: new decoys/supersessions → more records to inspect → still one-source, explicit decisions → correct Opus result → hardness FAIL. This is a design-hardness limitation, not SQL integrity failure or proof of an evaluator contradiction. The final report is **NON-FAIL 3/PROCEED**: one canvas item `/48` was wrongly marked open when the incorporated fallback rule plus PR #468 commits made it in beta ({c('AH3',62)}). {c('AH3',73,'Dropping a pass leaves the item with no applicable re-check. It does not make the item open.')} identifies a real inference/retrieval miss. It propagates into three outputs but remains one material cause. The same report notes that the previous run resolved this fork correctly ({c('AH3',141)}): the success is evidence of one observed failure, not reliable hardness across runs.

A recurrence/regression did occur during revision: r17 introduced a chronology tension when playthrough notes at 10:42:11 preceded their own claim at 10:42:35 and ending snapshot at 10:43:10 ({c('A7',365)}). This was **non-blocking advice in a PASS report**. r19 retimed the notes to 10:43:41 and fixed their permalink; {c('A8',331,'C-1: resolved in revision 19')} verifies the repair. Current canonical `cb99b9c0…` matches the final injection report and hardness input. Confidence: high for chronology, exact bytes and the difference between static PASS and observed hardness.

### 3. Reviewer C: semantic identity defect, then repaired PASS; later hardness and local-profile blockers are different issues

The first injection review genuinely FAILed on introducing `PERSON_6112` as the existing Transcend partner. The original dossier had expressly decided {c(H+'Audit-Report/iteration_01/before/canonical/Working_Files/01_Grounding_Dossier.md',54,'different people; the 2023 thread is not cited')}. Thus an entity table and an evidence pointer existed; the semantic resolution was wrong. The defect was not an SQL key collision. The Portal report connects the seeded "last time" outreach to the base Shanti history ({c('H1',103)} and {c('H1',104)}). Narrow verification of `HarmonyGames_Gmail/Services_Data/gmail/threads/00000031.json` confirms `PERSON_5404_EMAIL` is the Transcend meeting organizer; `00000029.json:282` contains the Shanti-signed reply. The exact source fingerprints/pointers are preserved in the audit scratch verification file.

The repair made only 29 token substitutions, `PERSON_6112` → `PERSON_5404`, across the intended rows; the independent review confirms this ({c(H+'Audit-Report/iteration_01/independent_review.md',4)}). The next preserved injection review `d221502f…` is PASS, as is final reviewed `3a5adccd…`. Do not describe the initial identity FAIL as an unresolved failure on either later reviewed snapshot.

The observed hardness result is separately **FAIL 2/HOLD**. Opus met the analytic core; the only counted model defect was To-vs-Cc placement. The required Bridge 2025 destination was read-only, and the run got a 403, so that failure was correctly excluded as an environment/capability defect ({c('HH',65)}; {c('HH',89)}). Counting the folder failure to make the task seem harder would be invalid.

Current canonical SQL `8b23be80…` is a still-later candidate and does **not** match any preserved Portal PASS. Its status explicitly says {c(H+'Working_Files/BATCH_STATUS.json',1,'BLOCKED MODE B candidate')} with injection/hardening/prompt gates FAIL, truthful per-record calls below 300 and unconditional work below 500. This is a local Long→extreme feasibility issue after revision, not a retroactive Portal rejection of `3a5adccd…`. Confidence: high for identity repair, capability attribution and version separation; current full release feasibility remains intentionally unresolved in the task's own record.

### 4. Reviewer D: exact returned bytes match the report; original-task attribution is unresolved

The returned hardness report genuinely says FAIL 1/HOLD, but its assignment is {c('MH',21,'Claire Morgan, Art Lead; Design; Marketing and GTM; Actions; normal; medium')}. Its work is a 43-item screenshot clearance task, and {c('MH',99,'Every output is usable as written.')} explains why it was too easy. It is not evidence that the original PlayableX restart kit failed.

I recomputed returned SQL `4e4b5243…` (151,802 bytes) and prompt `527690cb…` (538 bytes): both match the report exactly. The preserved sent snapshot instead hashes SQL `2decd123…` and prompt `177495c3…`. The file comparison records {c('MR',39,'zero overlap')} in parsed INSERT identities; outputs, requester, cohort and services differ ({c('MR',28)}). That establishes a replaced scenario, not whose mistake caused the replacement. The report explicitly withholds the task ID; its `6ad90e94…` is an attempt ID ({c('MH',5)}).

No original trajectory, matching injection review or prompt review is preserved for this returned pair ({c('MR',43)}; {c('MR',45)}). Its 98-call/43-of-43 claims remain report evidence, not independently replayed trajectory results here. Task identity, active assignment/difficulty and clock confirmation remain pending in the preserved reconciliation. No additional message was sent. Confidence: high for mismatch and exact report binding; low for attribution to original Reviewer D task or the reason for the replacement.

### 5. Reviewer E …TASK_E: no preserved Portal verdict to diagnose

The task has a local injection PASS block, bound to `72ca392990ba…`, and a CLEAN batch status ({c(T+'task_inputs_TASK_E/Working_Files/BATCH_STATUS.json',7)}). Its dossier even enumerates manual timing counter-readings and local tool reruns ({c(T+'task_inputs_TASK_E/Working_Files/01_Grounding_Dossier.md',1246)}; {c(T+'task_inputs_TASK_E/Working_Files/01_Grounding_Dossier.md',1290)}). The Audit-Report directory contains no preserved Portal report. This is **no returned evaluation evidence**, not PASS or FAIL at Portal, and certainly not evidence that create-injection repeatedly failed for Reviewer E. No skill invocation is inferred from the dossier. Confidence: high for preserved-file absence; it cannot prove no remote evaluation ever happened.

### 6. Current Julia task_inputs: six historical causal chronology defects, already repaired locally

Portal FAIL `22507861…` documents six introduced Check C problems ({c('J1',123)} through {c('J1',173)}):

| Fault on reviewed bytes | Why structural checks could still pass | Current repair evidence |
|---|---|---|
| F1: invented old version/submission history (`0.3.40` in August; `0.3.47` Sep 15) | IDs/JSON/timestamps valid, but contradict before-freeze release messages | August `0.3.24`, Sep 22 `0.3.40`, remove `0.3.47`; current SQL lines 98,130,143–147 |
| F2: 16:40 Slack says build log updated; v2 dated 17:05 | Independent records each have ordered own fields | v2 retimed 16:30; current SQL 143,147 |
| F3: 19:24 Slack cites mail sent 19:26 | Both before freeze and valid thread relationships | mail retimed 19:20 across all copies; current SQL 26,30,34 |
| F4: v2 declares release/submission completed before events happened | Embedded prose dates/tense not compared with external chronology | planned/future wording in current SQL 143,147 |
| F5: date-moved calendar event unchanged since Sep 24 | created≤updated holds, but lifecycle contradicts later move | updated to Sep 29, sequence 1; local repair review confirms |
| F6: notes describe September pass, created/modified months earlier and before folder | Local row fields internally valid | eleven notes moved into September; current SQL 100–126 |

Independent source check: raw `HarmonyGames_Other_Services/Services_Data/slack/messages/C0880U9751A/2025-09.json:1`, JSON pointer `/463`, says “I just released 0.3.49 on IOS” at 2025-09-29T21:55:08.627389Z. This corroborates the core F4 impossibility on the old 17:05 v2. Source SHA and excerpt are in `scratch/injection_source_verification.json`; this is the larger local archive, not an assertion of byte identity with Portal's source snapshot.

Current canonical SQL is `477bed62…` (60,622 bytes), with all six targeted repairs visible. The local review records {c('JR',65,'Each was verified against raw exports before repair')} and the change list ({c('JR',67)}). It also rejects Portal advisory A4: the alleged `updated_at` was actually `created_at`, so applying that advice would move the issue timestamp backwards ({c('JR',69)}). Advisory A5's processing-after-submission ordering is plausible, not an impossible chronology ({c('JR',71)}). These are explicit contrary examples to blind report obedience.

This is **historical Portal FAIL → local repairs/current local PASS**. No new Portal PASS for `477bed62…` was located. The local report's independent revisions are not extra Portal attempts, and the earlier local static PASS does not make the Portal FAIL spurious. Confidence: high for the demonstrated causal failures, current visible repairs and advisory rejection; full Portal-equivalent source replay remains unavailable.

### 7. Skipped Oliver: legacy language FAIL fixed, later hardening regressed a derived parent field

First injection `6749d05b…` FAILs on “mailbox filename” solver instructions and `page_sp_scope_decoy` IDs ({c('S1',93)}; {c('S1',100)}). These were actual historical verdicts under a then-current policy. They are **not SQL syntax faults** and should not be reclassified as current evaluator requirements without the matching rule snapshot. Revised `836f1bbe…` is a genuine preserved injection PASS. The intermediate `9ae0a76d…` PASS is referenced in the next report ({c('S2',25)}) and exists in local sandbox history, but is not counted as another preserved external report here.

Hardness goes from FAIL 1 on r8 to **NON-FAIL 4/PROCEED** on r11. The latter run used the old formula for four remapped issues despite accessible redirects, causing wrong rows and aggregate values; it also missed a tracking-issue comment ({c('SH2',66)}; {c('SH2',70)}). This is a real multi-source update failure, with 124 of 128 rows otherwise exact—not evidence the whole injected task is broken.

Later r23 `9b56c0f3…` injection FAIL is a new regression: hardening added comments and bumped card activity to Feb 13 19:40 while the explicitly written board activity stayed Feb 12 18:05 ({c('S3',111)}; {c('S3',113,'Revision 23 bumped the card but not the board')}). The current canonical `08641123…` differs again, so neither the older PASS nor r23 FAIL is automatically the current Portal verdict. The report also flags test-role batch names as advisories only ({c('S3',128)}). Confidence: high for versioned regression; board-cache severity has evaluator-policy uncertainty discussed below.

### 8. Archived Lot G: a repair attempt created cross-source people-date inconsistency, then reverted it

Two preserved injection reports are PASS. The second explicitly records a missing intermediate r10 FAIL: moving Claire/Julia termination letters to January 31, 2026 contradicted the base DM's “end of December 25” and acknowledgements ({c('L2',114)}). r11 removes those six UPDATEs, preserving coherent base letters, DM and acknowledgements ({c('L2',117)}). A separate Owen correction is justified with identity and payroll-row evidence ({c('L2',122)}). This is a repair introducing a new inconsistency, followed by a scoped reversal—not the exact same bug repeatedly surviving a fix.

Hardness is **NON-FAIL 4/PROCEED**: missed confirmatory coverage and independent aggregation errors ({c('LH',44)}; {c('LH',121)}). The original report explicitly calls unchanged board cache a semantics limit rather than a defect ({c('L1',160)}). Current SQL `a568e484…` differs from reviewed `3f87be1d…` even at the same byte length; a current verdict must not be inferred without resolving that difference. Confidence: high for preserved chronology, lower for an intermediate FAIL whose original report is absent.

### 9. Completed Douglas: strong contrary evidence, with freshness limits after later edits

Five preserved injection reviews are all PASS across SQL r3/r4/r6/r7/r13. Both preserved hardness reviews are **NON-FAIL/PROCEED**, score 3 then score 4. The second identifies three accessible retrieval misses: Arthur's email reply, the DM reply needing the correct channel ID after a failed attempt, and a Confluence comment ({c('DH2',57)} through {c('DH2',68)}). The result is four wrong register rows, a wrong 10/8 count instead of 6/10, and missed required Linear transitions. It is substantive hardness attributable to the solver, with successful write capabilities and substantial correct work ({c('DH2',81)}).

The final injection r13 moves the ZOM-537 economy-import fact from Slack reply to an inline PR review comment ({c('D5',122)}). The report explicitly warns the earlier hardness run no longer matches that revised data ({c('D5',566)}). Current canonical SQL `2131bbef…` is later again. A folder named completed_tasks is not proof that every present byte has a current external PASS or that a past score 4 survives moving the decisive evidence to another service. Confidence: high for historical success and freshness boundary; current source-matched hardness requires fresh evidence.

## Why the current create-injection workflow can certify these artifacts

1. **The contract already names the semantic work; it is not missing from the prose.** The skill requires grounded entity, date and companion checks, manual A–C self-review and blocking local gates. {c(T+'playbooks/01_Universe_Injection.md',138,'dates written in text')} and lines 139–144 explicitly put chronology-in-prose, real entity identity, cross-service figures, lifecycle and planted-looking text in the manual column. The shared contract forbids SQL execution ({c(T+'setup/GEN_EXECUTION.md',94)}) and separates Portal from local preparation. The skill/playbook are current expectations, not proof of how older artifacts were authored.

2. **Mechanical PASS is real but narrower than its broad labels suggest.** `sql_lint.py:8–24` enumerates types, JSON, IDs, per-row timestamps and metadata; it cannot infer that “already updated” must postdate another record's change. `base_check.py:20–58` handles many actual cross-row links, counts, mirrors, lifecycle and known hazards, but not arbitrary narrative causality. `fact_check.py:12–25` validates author-declared facts; superseded versions are explicitly exempt. A fact omitted from the manifest or a false identity decision can escape this declarative check. None of these is a general semantic proof engine.

3. **The self-review gate measures document shape, not whether its argument is true.** {c(T+'tools/stage_gate.py',630,'evid = [(i, t) for i, t in counters if RX_EVID.search(t)]')} and lines 631–638 count evidence-shaped rows and required regex topics. The injection stage does rerun the real tools ({c(T+'tools/stage_gate.py',1970)}; lines 1977–2002) and enforce provenance; that is useful protection. But a confidently wrong Transcend row can satisfy the entity/evidence/self-review checks. The observed defect is a false semantic resolution with adequate-looking paperwork, not proof all certificates were forged.

4. **Hardness design thresholds are proxies, not observations.** `hardness_gate.py:23–33` checks literal delegation quotes, surface requirements, conditional budgets and supersession timestamps; `hardness_gate.py:69–84` enforces service/row/call/trap counts. It does not demonstrate that a strong model will miss the facts. Reviewer B's two FAIL 1 runs directly show explicit QA labels, named environments and literal fix lists defeating additive trap count. Reviewer A and Douglas show why accessible later updates in already-reached containers can create real retrieval failures. The two gates answer different questions, even when both use “hardness” in their name.

5. **A parent-derived activity invariant is missing from the local checker.** `base_check.py:886–926` validates card badges and comments; it has no Trello-board `dateLastActivity` propagation check. r23's stale explicitly written board field is thus outside the implemented relation checks. The recommendation is a supported, snapshot-aware lower-bound check for an explicitly supplied parent activity field, not blind enforcement of equality or speculative cached formulas.

6. **Version and source drift create false success/failure stories.** Current canonical SQL matches final Portal review bytes for Reviewer A and Reviewer B, but not Julia, Reviewer C, skipped Oliver, archived Lot G, Douglas or Reviewer D's returned-original task. The exact current hashes are in `scratch/injection_current_hashes.json`. Current local certificates, existing reports and Portal input stores have different lifecycles. Fixing text while leaving a trajectory bound to the prior overlay does not establish a new hardness outcome.

## Evaluator inconsistency and advice requiring caution

**Confirmed policy drift under unchanged version label.** The skipped r23 review records that Eval 0 changed from `c9265a38…` to `b1ea752a…`, while still calling itself `injection-static-v2` ({c('S3',18)}). Current `Evals/0_Injection_Quality_Eval.md:42–46` explicitly excludes voice matching, decoy counts and answer leakage from injection scope. Therefore the older skipped “decoy ID” FAIL is a genuine historical verdict under earlier policy, not an evergreen data-integrity theorem. Pin evaluator hashes and classify legacy findings separately. Schema mismatch alone remains advisory under current `Evals/0_Injection_Quality_Eval.md:154–158`; deleting live-supported columns just because an unverified snapshot lacks them is not a justified automatic repair.

**Uneven board-cache evidence standard, with a meaningful distinction.** Reviewer A's report says {c('N2',135,'No supported rule requires it')} even though base board activity equals latest card activity. Archived Lot G calls the same unchanged-cache pattern a semantics limit ({c('L1',160)}). Skipped r23 instead FAILs using a five-board empirical equality ({c('S3',113)}). An explicit UPDATE to a demonstrably stale parent value is a stronger introduced contradiction than leaving an undocumented base cache untouched, and rule/source snapshots differ. This is evidence of unstable severity/evidence thresholds, not a proved same-input contradictory verdict. A robust workflow should seek/record the field contract or use an appropriately narrow manual disposition.

**Confirmed bad advice, not a failing verdict reversal.** Julia A4 mistakes `created_at` for `updated_at` ({c('J1',180)} versus {c('JR',69)}); A5 suggests treating normal later processing as a chronology problem ({c('J1',181)} versus {c('JR',71)}). Reject these on evidence. Similarly, Reviewer B's playthrough timing was advisory throughout; its later repair does not transform the earlier injection PASS into FAIL. No same-SQL/evaluator/source pair in this corpus proves a PASS/FAIL contradiction merely because another stage later found a different issue.

## Prioritized recommendations — no implementation performed

| Priority | Proposed test/gate/skill change | Failure it targets | Acceptance and limits |
|---|---|---|---|
| P0 | Immutable evaluated-bundle receipt: task ID, attempt ID, persona/assignment, prompt/SQL/trajectory hashes, source-manifest and evaluator hashes, clock, delivered-v-returned mapping | Reviewer D attribution, stale PASS inheritance, changed evaluator under same label | Reject mismatched identity/bytes before causal repair. Preserve old verdict; do not require paid evaluation to produce the receipt. |
| P0 | Structured causal timeline: claim record, claimed event/version, event actual or planned, source timestamp, asserted-before constraint | Julia F1–F6; Reviewer B r17; repaired Lot G dates | Static pure-data fixtures cover positive planned future events, dated stale claims, source-edited-after-freeze and impossible “already” assertions. Independent reviewer must resolve ambiguous semantics; no SQL execution. |
| P0 | Cross-service entity-resolution ledger with negative search coverage and explicit same/different-person evidence | Reviewer C's Transcend duplicate semantic identity | Preserve candidates and conflicting evidence. Search absence in one persona mailbox does not justify minting an identity; a name/pronoun mismatch alone cannot prove distinct people. |
| P1 | Regression dependency closure for every changed seed: derived fields, mailbox copies, linked timestamps, page versions, IDs/permalinks and affected run bindings | Skipped board/card activity; Julia mail timing and Confluence v2; Reviewer B retimed message link | Fixtures assert card activity lower bound on explicitly written parent field where semantics are supported; planned/cache counterexamples must remain accepted or advisory. |
| P1 | Replace generic semantic PASS attestations with independent, source-backed challenge rows; treat a gate's row count as completeness only | Evidence-shaped but wrong dossier resolution | Reviewer must re-read deciding record and source pointer, record strongest contrary source and why it loses; do not infer independence from a model name printed in a dossier. |
| P1 | Distinguish “design compliance” from “observed hardness” in output and handoff gates; preserve actual early-exit shortcuts | Reviewer B explicit/local evidence, overclaimed necessary calls, Reviewer C local extreme feasibility | A local design PASS cannot clear Portal hardness. A single NON-FAIL 3 permits its defined continuation but makes no pass-rate/reliability claim. |
| P1 | Hardening must test a necessary inference or independent discovery that changes an output, with a valid incorporated rule and no answer labels | Repeated additive traps that Opus solved directly | Pre-register the decision; if a normal bulk call or literal description resolves it, revise the mechanism rather than adding more equivalent rows. Keep fairness and capability attribution. |
| P2 | Evaluate historical regression fixtures under pinned evaluator snapshots; maintain separate “historical verdict” and “current-rule applicability” columns | Legacy grader-language FAILs, board-cache drift, schema advice | Never silently rewrite a genuine historical FAIL, or promote optional snapshot/realism advice into a current blocking rule. |

## Remaining blockers and confidence

No audit action was denied or left with an uncertain execution outcome. The remaining gaps are evidentiary: Reviewer D original-task attribution and original trajectory are pending; several current canonical versions have no matching fresh Portal report/run; exact historical evaluator/source snapshots are not fully preserved; Reviewer E has no returned Portal evidence. None authorizes a new evaluation, SQL execution, correspondence or task edit in this audit.

Overall confidence is **high** in preserved verdict chronology, deduplication, exact local file hashes and the distinction between structural assurance and semantic review; **moderate** in complete live-run causal reconstruction when supported only by a report; **low** for original-task attribution of Reviewer D's returned scenario and universal claims about every create skill. The strongest conclusion is targeted: improve causal/identity review, regression closure and immutable version binding, while preserving the many real injection PASS and NON-FAIL hardness outcomes.
''')

target = OUT/'INJECTION.md'
if target.exists():
    raise SystemExit('Refusing to overwrite existing INJECTION.md')
target.write_text('\n'.join(parts)+'\n')
print(target)
print(f'{len(target.read_text().splitlines())} lines; {target.stat().st_size} bytes')

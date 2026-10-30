# Delivery and external FAIL provenance

Read-only mailbox audit supplied by the parent audit thread on 2026-10-28. The parent independently inspected Gmail message bodies, MIME attachments and the complete qualifying reports. This local audit reconciles those findings with preserved repository report bytes. No messages were sent or modified for this audit.

## Count definition and result

**Three confirmed distinct sent task IDs returned an attributable external FAIL: Reviewer A, Reviewer B and Reviewer C.** Four reviewers returned genuine FAIL reports when Reviewer D's changed-scenario return is included, but his returned artifact has not been bound to the task originally sent. Thus it is not a fourth confirmed failed sent task.

Five task IDs were delivered in the October 22–23 batch. This is not an all-time sent-task total. Earlier folder deliveries are documented below; they cannot be deduplicated reliably against all later task IDs. NON-FAIL, local check FAILs and repeated report copies do not add qualifying tasks.

## Verified delivery and first qualifying return

| Sent canonical task ID | Reviewer | Verified SENT | Returned original report | Qualification |
|---|---|---|---|---|
| `TASK_A` | Reviewer A | [1a1651bb5faa35cc](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a1651bb5faa35cc), October 22 19:34:36 UTC, named ZIP | [1a165886cf553937](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a165886cf553937), October 22 21:33:08 UTC, `6ad90e93a2c3542255f64fbf_1_prompt.md` | FINAL VERDICT FAIL, score 2, COMPLETE; unresolved closed/no-card and installment write sets. Counts. |
| `TASK_B` | Reviewer B | [1a1651d8ff7b6ec0](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a1651d8ff7b6ec0), October 22 19:36:37 UTC, corrected-address resend | [1a16801780280b16](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a16801780280b16), October 23 09:06:06 UTC, `prompt eval.md` | FINAL VERDICT FAIL, score 2, COMPLETE; canvas/PR ambiguity and source coherence. Counts. |
| `TASK_C` | Reviewer C | [1a168c1b9bd234c8](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a168c1b9bd234c8), October 23 12:34:48 UTC, named task ZIP | [1a168e821077954f](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a168e821077954f), October 23 13:16:32 UTC, `6ad90e9fa38cc384483b1c80_0_injection.md` | FINAL VERDICT FAIL, COMPLETE; duplicate Transcend partner identity PERSON_6112 vs existing PERSON_5404. Counts. |
| `TASK_D` | Reviewer D | [1a1651bb5faa35cc](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a1651bb5faa35cc), named Reviewer D ZIP | [1a16ed677b050dd3](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a16ed677b050dd3), October 24 16:54:57 UTC, `6ad90e94adb09db24624b216_1a_hardness fail report current injection.md` | Genuine FAIL 1, COMPLETE, Too easy/HOLD. Report withholds task ID; screenshot-refresh scenario differs from sent PlayableX. Excluded from strict matched count. |
| `TASK_E` | Reviewer E | [1a165b1d2f04e149](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a165b1d2f04e149), October 22 22:18:34 UTC, separate ZIP | No returned report found | Cancellation notes say initial reports pending. No incoming mail from exact sender in searched period; no preserved external report in task's Audit-Report. Excluded. |

The first Reviewer B address bounced. The corrected-address SENT above establishes resend; a SENT record does not establish whether the recipient read it.

## Exact fingerprints independently read from qualifying reports

- Reviewer A SQL `b9d8cab8b6e6985c39334ac29743958d824c26cd23147bfcea555817cd3b9614`; prompt `cdf0185da882a7b7063aebd66c585138b0ec88b252ce23ad573eee32bef1dec3`.
- Reviewer B SQL `db593dd7e608dbd43a6deef98c9b85332e99909b09afb6b4aca120d453d641c3`; prompt `9d9735b4cb1493d429c4a54def93f2fa9a937e91fc48a5ed9febbfb2ac923b3a`.
- Reviewer D returned SQL `4e4b5243e220b9e589cace13dc58ec01cc927d54142b94a3a1a70bfa28d101f4` (151,802 bytes); prompt `527690cbc023ad5d68330b302257e231acf2e64b67a69b82e7fbe91da751ac3b` (538 bytes). Trace hash `8d817a7fcf97c6df3c68a59b45f13570aca9060f36d20e25ec7038cc0cd6f190` is cited in report but trace not attached. Attempt `6ad90e94adb09db24624b216` is not proof of canonical task identity.
- Preserved Reviewer D comparison records original 117 versus returned 239 SQL mutations with no shared inserted IDs, Hard→Medium and a seven-hour freeze difference. Clarification requests [1a16eeec5114a639](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a16eeec5114a639) and [1a16ef6b49dfa321](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a16ef6b49dfa321) remained unanswered in exact-sender search. No new outreach was performed.

## Historical coverage and limits

The parent read the entire eight-message Batch-Rage thread `1a143f2c626cadd8`. Six earlier file deliveries on October 16 were located:

| Reviewer | SQL delivery | Prompt delivery |
|---|---|---|
| Reviewer F | [1a14666e33e8cd1a](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a14666e33e8cd1a) | [1a146b834a208dac](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a146b834a208dac) |
| Reviewer G | [1a146b3c5a5846b6](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a146b3c5a5846b6) | [1a14704ffe0bbead](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a14704ffe0bbead) |
| Reviewer C | [1a146c217158d3a4](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a146c217158d3a4) | [1a146f86b875b999](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a146f86b875b999) |

Only inbound [1a146c6f8ce5d69b](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a146c6f8ce5d69b) from Reviewer G says “Received, thank you”; it has no report. Exact-sender searches before October 29 for Reviewer F, Reviewer G, Reviewer C, Reviewer H and Reviewer I found only that receipt and six current Reviewer C messages, without further pages. An October 17 four-folder archive send [1a149134bc809de9](https://mail.google.com/mail/u/?authuser=audit-owner%40example.invalid#all/1a149134bc809de9) to Reviewer E establishes packaging, not a failed return. October 20–28 exact-sender searches for Reviewer E, Reviewer D and Reviewer C returned seven messages: no Reviewer E, one Reviewer D, six Reviewer C.

These findings support three confirmed failures across the located delivery histories. They do not establish that every unknown historical task or communication channel has been discovered. Other report-bearing local groups are audited for failure causes but remain outside the strict contributor-delivery count without send/identity proof.

The parent observed 139 unique mail records in discovery. That is a message inventory, not 139 reports and not a count of independently read verdicts. This report includes the directly verified messages necessary to reproduce the count; local report hashes and verdict lines are in `report_manifest.json`.

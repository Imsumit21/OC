# Per-task and per-stage verdict history

Source: immutable report exports indexed in `evidence/report_manifest.json`. Only the final overall verdict is shown; findings inside a PASS do not change that verdict. Byte-identical copies count once. These are **84 unique report documents**, not necessarily 84 independent review executions. Reports with PARTIAL status remain visibly PARTIAL.

Ordering uses explicit iteration numbers, or report filename revision suffixes where no iteration folder exists. It is the preserved local sequence, not an invented exact review timestamp. Full reviewed-input hashes and matching local artifact paths are retained in the machine manifest. Report dates, policy versions and clocks remain as stated by the report; inconsistent source clocks are not silently normalized.

## Delivery-qualified count

Three canonical tasks qualify: Reviewer A `...TASK_A`, Reviewer B `...TASK_B`, Reviewer C `...TASK_C`. Reviewer D's different-scenario FAIL stays unbound; Reviewer E has no preserved returned report. Other local report groups have no verified contributor-delivery mapping in this audit. See [mailbox evidence](evidence/MAILBOX_PROVENANCE.md).

## archived task/task_inputs-n

External report exists locally, contributor delivery/canonical ID mapping not verified.

| Stage | Preserved sequence of overall verdicts |
|---|---|
| injection | PASS → PASS |
| prompt | FAIL → NON-FAIL |
| hardness | NON-FAIL |
| oe | No original external report preserved |
| rubrics | No original external report preserved |

| Order / stage | Overall verdict | Execution status / score as reported | Original evidence | SHA-256 |
|---|---|---|---|---|
| filename revision base / hardness | NON-FAIL | COMPLETE / 4 | `archived task/task_inputs-n/6acefd9770b8942247032c9e_1a_hardness.md:140` | `4520e946ada6` |
| filename revision base / injection | PASS | COMPLETE / not stated in final block | `archived task/task_inputs-n/6acefd9770b8942247032c9e_0_injection.md:176` | `444afad55f9d` |
| filename revision 1 / injection | PASS | COMPLETE / not stated in final block | `archived task/task_inputs-n/6acefd9770b8942247032c9e_0_injection (1).md:170` | `dc35ad41a850` |
| filename revision base / prompt | FAIL | COMPLETE / 2 | `archived task/task_inputs-n/6acefd9770b8942247032c9e_1_prompt.md:435` | `16f32034ecc5` |
| filename revision 3 / prompt | NON-FAIL | COMPLETE / 3 | `archived task/task_inputs-n/6acefd9770b8942247032c9e_1_prompt (3).md:531` | `9d72a55293f5` |

## completed_tasks/douglas_beta_server_signoff_2026-10-28

External report exists locally, contributor delivery/canonical ID mapping not verified.

| Stage | Preserved sequence of overall verdicts |
|---|---|
| injection | PASS → PASS → PASS → PASS → PASS |
| prompt | NON-FAIL → FAIL → PASS → PASS |
| hardness | NON-FAIL → NON-FAIL |
| oe | NON-FAIL (PARTIAL) → PASS |
| rubrics | FAIL → PASS |

| Order / stage | Overall verdict | Execution status / score as reported | Original evidence | SHA-256 |
|---|---|---|---|---|
| filename revision base / hardness | NON-FAIL | COMPLETE / 3 | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1a_hardness.md:113` | `621966f1e339` |
| filename revision 1 / hardness | NON-FAIL | COMPLETE / 4 | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1a_hardness (1).md:97` | `cd1d55b8e9c0` |
| filename revision base / injection | PASS | COMPLETE / not stated in final block | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_0_injection.md:555` | `c318666fc6f8` |
| filename revision 1 / injection | PASS | COMPLETE / not stated in final block | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_0_injection (1).md:567` | `7612661f4c2b` |
| filename revision 2 / injection | PASS | COMPLETE / not stated in final block | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_0_injection (2).md:622` | `0f3928d70a90` |
| filename revision 3 / injection | PASS | COMPLETE / not stated in final block | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_0_injection (3).md:589` | `63ce014b440b` |
| filename revision 4 / injection | PASS | COMPLETE / not stated in final block | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_0_injection (4).md:568` | `ca4cb95b8183` |
| filename revision base / oe | NON-FAIL | PARTIAL / not stated in final block | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_2_oe.md:137` | `9a9455f20733` |
| filename revision 1 / oe | PASS | COMPLETE / 5 | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_2_oe (1).md:126` | `3507f980bb2f` |
| filename revision base / prompt | NON-FAIL | COMPLETE / 3 | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1_prompt.md:377` | `106262692401` |
| filename revision 1 / prompt | FAIL | COMPLETE / 2 | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1_prompt (1).md:371` | `bc3d2c5e4d68` |
| filename revision 2 / prompt | PASS | COMPLETE / 5 | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1_prompt (2).md:420` | `412ca701caed` |
| filename revision 3 / prompt | PASS | COMPLETE / 5 | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1_prompt (3).md:566` | `9cd788e16625` |
| filename revision base / rubrics | FAIL | COMPLETE / 1 | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_3_rubric.md:223` | `1394b5327493` |
| filename revision 1 / rubrics | PASS | COMPLETE / 5 | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_3_rubric (1).md:151` | `d440a207c622` |

## task_inputs

External report exists locally, contributor delivery/canonical ID mapping not verified.

| Stage | Preserved sequence of overall verdicts |
|---|---|
| injection | FAIL |
| prompt | No original external report preserved |
| hardness | No original external report preserved |
| oe | No original external report preserved |
| rubrics | No original external report preserved |

| Order / stage | Overall verdict | Execution status / score as reported | Original evidence | SHA-256 |
|---|---|---|---|---|
| filename revision base / injection | FAIL | COMPLETE / not stated in final block | `Task_Authoring/task_inputs/plateform_reports/6adfee3e0350cc55431db61d_0_injection.md:212` | `a49bdc3f66ac` |

## task_inputs-skipped

External report exists locally, contributor delivery/canonical ID mapping not verified.

| Stage | Preserved sequence of overall verdicts |
|---|---|
| injection | FAIL → PASS → FAIL |
| prompt | FAIL → FAIL |
| hardness | FAIL → NON-FAIL |
| oe | PASS |
| rubrics | FAIL → FAIL → FAIL → FAIL |

| Order / stage | Overall verdict | Execution status / score as reported | Original evidence | SHA-256 |
|---|---|---|---|---|
| filename revision base / hardness | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs-skipped/Plateform_reports/01_hardness.md:90` | `a7f1fad768b4` |
| filename revision base / hardness | NON-FAIL | COMPLETE / 4 | `Task_Authoring/task_inputs-skipped/Plateform_reports/02_hardness.md:147` | `f7d7fd9ce495` |
| filename revision base / injection | FAIL | COMPLETE / not stated in final block | `Task_Authoring/task_inputs-skipped/Plateform_reports/01_injection.md:125` | `4ac9782dbdd5` |
| filename revision base / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs-skipped/Plateform_reports/2_injection.md:134` | `4ef66c8a1b2d` |
| filename revision base / injection | FAIL | COMPLETE / not stated in final block | `Task_Authoring/task_inputs-skipped/Plateform_reports/03_Injection.md:140` | `41a855cdb7f1` |
| filename revision base / oe | PASS | COMPLETE / 5 | `Task_Authoring/task_inputs-skipped/Plateform_reports/01_OE_Report.md:118` | `1a2d73b3c5a3` |
| filename revision base / prompt | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs-skipped/Plateform_reports/01_prompt.md:374` | `af23fa5a5820` |
| filename revision base / prompt | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs-skipped/Plateform_reports/02_Prompt.md:460` | `9934f381c0cc` |
| filename revision base / rubrics | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs-skipped/Plateform_reports/01_Rubrics.md:328` | `67f08b2a1175` |
| filename revision base / rubrics | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs-skipped/Plateform_reports/02_Rubric.md:189` | `14548b65e562` |
| filename revision base / rubrics | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs-skipped/Plateform_reports/03_Rubric.md:169` | `bfbc3ac6d62d` |
| filename revision base / rubrics | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs-skipped/Plateform_reports/04_Rubric.md:153` | `aaf1e863f891` |

## task_inputs_TASK_B

Corrected-address send and matched original prompt FAIL.

| Stage | Preserved sequence of overall verdicts |
|---|---|
| injection | PASS → PASS → PASS → PASS → PASS → PASS → PASS → PASS |
| prompt | FAIL → FAIL → PASS → FAIL → FAIL → PASS → NON-FAIL → PASS |
| hardness | FAIL → FAIL → NON-FAIL |
| oe | NON-FAIL → PASS |
| rubrics | FAIL → FAIL → FAIL → FAIL → FAIL → FAIL |

| Order / stage | Overall verdict | Execution status / score as reported | Original evidence | SHA-256 |
|---|---|---|---|---|
| iteration 4 / hardness | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_04_hardness/6ad90e9449d1194f4e538cdf_1a_hardness.md:98` | `d925b73c4ca7` |
| iteration 12 / hardness | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_12_report_intake/6ad90e9449d1194f4e538cdf_1a_hardness.md:109` | `ad513daef793` |
| iteration 17 / hardness | NON-FAIL | COMPLETE / 3 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_17_report_baseline_intake/received/6ad90e9449d1194f4e538cdf_1a_hardness.md:147` | `8d312c4ae9de` |
| iteration 1 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_01/injection eval.md:199` | `6b86741fac82` |
| iteration 2 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_02/6ad90e9449d1194f4e538cdf_0_injection.md:363` | `ab653d4f7729` |
| iteration 3 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_03/6ad90e9449d1194f4e538cdf_0_injection (2).md:365` | `22d0395015ad` |
| iteration 8 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_08_report_intake/6ad90e9449d1194f4e538cdf_0_injection (4).md:435` | `6eb31ee6ede1` |
| iteration 10 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_10_report_intake/6ad90e9449d1194f4e538cdf_0_injection.md:441` | `da6dcb842b14` |
| iteration 12 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_12_report_intake/6ad90e9449d1194f4e538cdf_0_injection.md:485` | `12c5f855c9cb` |
| iteration 14 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_14_report_intake/6ad90e9449d1194f4e538cdf_0_injection.md:447` | `63722c2b83ca` |
| iteration 17 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_17_report_baseline_intake/received/6ad90e9449d1194f4e538cdf_0_injection.md:447` | `4f190ad267af` |
| iteration 20 / oe | NON-FAIL | COMPLETE / 3 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_20_oe_report_reconciliation/received/6ad90e9449d1194f4e538cdf_2_oe.md:155` | `33c45b40ff33` |
| iteration 21 / oe | PASS | COMPLETE / 5 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_21_oe_pass_report_reconciliation/received/6ad90e9449d1194f4e538cdf_2_oe (1).md:147` | `8eb9b05c203c` |
| iteration 1 / prompt | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_01/prompt eval.md:451` | `e3ad958a09b2` |
| iteration 2 / prompt | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_02/6ad90e9449d1194f4e538cdf_1_prompt.md:353` | `a047869e2baa` |
| iteration 3 / prompt | PASS | COMPLETE / 5 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_03/6ad90e9449d1194f4e538cdf_1_prompt (2).md:401` | `f8f56661c71a` |
| iteration 8 / prompt | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_08_report_intake/6ad90e9449d1194f4e538cdf_1_prompt (4).md:482` | `a9cdc22ab568` |
| iteration 10 / prompt | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_10_report_intake/6ad90e9449d1194f4e538cdf_1_prompt.md:468` | `6668cfe83ef0` |
| iteration 12 / prompt | PASS | COMPLETE / 5 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_12_report_intake/6ad90e9449d1194f4e538cdf_1_prompt.md:573` | `51569108c3c0` |
| iteration 14 / prompt | NON-FAIL | COMPLETE / 3 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_14_report_intake/6ad90e9449d1194f4e538cdf_1_prompt.md:668` | `3f706250ace1` |
| iteration 17 / prompt | PASS | COMPLETE / 5 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_17_report_baseline_intake/received/6ad90e9449d1194f4e538cdf_1_prompt.md:644` | `c86f258edd1c` |
| iteration 23 / rubrics | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_23_external_rubric_intake/received/6ad90e9449d1194f4e538cdf_3_rubric (3).md:149` | `2fcf37e70c36` |
| iteration 26 / rubrics | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_26_latest_rubric_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (6).md:180` | `0a26ffd2d199` |
| iteration 26 / rubrics | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_26_latest_rubric_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (7).md:194` | `d7ef5a30f900` |
| iteration 27 / rubrics | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_27_rubric_scope_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (8).md:192` | `1df8947d7f77` |
| iteration 28 / rubrics | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_28_rubric_semantic_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (10).md:182` | `dd432e1e5267` |
| iteration 30 / rubrics | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_30_rubric_alias_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (11).md:180` | `934e103b9a0e` |

## task_inputs_TASK_D

Genuine returned hardness FAIL belongs to changed scenario; no confirmed reassignment/task binding.

| Stage | Preserved sequence of overall verdicts |
|---|---|
| injection | No original external report preserved |
| prompt | No original external report preserved |
| hardness | FAIL |
| oe | No original external report preserved |
| rubrics | No original external report preserved |

| Order / stage | Overall verdict | Execution status / score as reported | Original evidence | SHA-256 |
|---|---|---|---|---|
| filename revision base / hardness | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs_TASK_D/Audit-Report/20261024T165457Z_email_1a16ed677b050dd3/originals/6ad90e94adb09db24624b216_1a_hardness fail report current injection.md:122` | `c21b66ad2ca8` |

## task_inputs_TASK_A

Named sent ZIP and matched original prompt FAIL.

| Stage | Preserved sequence of overall verdicts |
|---|---|
| injection | PASS → PASS → PASS |
| prompt | FAIL → FAIL → FAIL → NON-FAIL |
| hardness | NON-FAIL |
| oe | NON-FAIL → PASS |
| rubrics | FAIL → FAIL → FAIL → PASS → FAIL (PARTIAL) → PASS |

| Order / stage | Overall verdict | Execution status / score as reported | Original evidence | SHA-256 |
|---|---|---|---|---|
| iteration 7 / hardness | NON-FAIL | COMPLETE / 3 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_07_hardness/6ad90e93a2c3542255f64fbf_1a_hardness.md:93` | `f422e99dbaf1` |
| iteration 1 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_01_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_0_injection.md:125` | `bc4c36a448d1` |
| iteration 3 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_03_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_0_injection (1).md:146` | `0383ca237e25` |
| iteration 5 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_05_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_0_injection.md:146` | `abf2ebc55de1` |
| iteration 9 / oe | NON-FAIL | COMPLETE / 3 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_09_oe_portal/6ad90e93a2c3542255f64fbf_2_oe.md:143` | `caa1f34b339b` |
| iteration 11 / oe | PASS | COMPLETE / 5 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_11_oe_v2_pass/6ad90e93a2c3542255f64fbf_2_oe (1).md:143` | `2f4934516210` |
| iteration 1 / prompt | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_01_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_1_prompt.md:377` | `7743fee5d4af` |
| iteration 2 / prompt | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_02_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_1_prompt (1).md:405` | `ea68cd7f9995` |
| iteration 3 / prompt | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_03_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_1_prompt (2).md:456` | `c86a9124098c` |
| iteration 5 / prompt | NON-FAIL | COMPLETE / 3 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_05_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_1_prompt.md:539` | `5376eaf6f1ef` |
| iteration 12 / rubrics | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_12_rubric_portal_20261025/6ad90e93a2c3542255f64fbf_3_rubric.md:187` | `f83fa6e15837` |
| iteration 13 / rubrics | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_13_rubric_portal_r2_20261025/6ad90e93a2c3542255f64fbf_3_rubric (1).md:143` | `3fd0e213042a` |
| iteration 14 / rubrics | FAIL | COMPLETE / 1 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_14_rubric_portal_r3_20261025/6ad90e93a2c3542255f64fbf_3_rubric (2).md:124` | `07da306f688a` |
| iteration 15 / rubrics | PASS | COMPLETE / 5 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_15_rubric_portal_r4_pass_20261025/6ad90e93a2c3542255f64fbf_3_rubric (3).md:131` | `d8542cdd1ec2` |
| iteration 16 / rubrics | FAIL | PARTIAL / 2 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_16_rubric_portal_r5_20261026/6ad90e93a2c3542255f64fbf_3_rubric (4).md:120` | `3d55dcfdf711` |
| iteration 18 / rubrics | PASS | COMPLETE / 5 | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_18_verifier_intake_20261027/6ad90e93a2c3542255f64fbf_3_rubric (6).md:117` | `4fd8cddfc60b` |

## task_inputs_TASK_C

Named sent ZIP and matched original injection FAIL.

| Stage | Preserved sequence of overall verdicts |
|---|---|
| injection | FAIL → PASS → PASS |
| prompt | FAIL → FAIL → PASS |
| hardness | FAIL |
| oe | No original external report preserved |
| rubrics | No original external report preserved |

| Order / stage | Overall verdict | Execution status / score as reported | Original evidence | SHA-256 |
|---|---|---|---|---|
| iteration 4 / hardness | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_05_review_intake/6ad90e9fa38cc384483b1c80_1a_hardness.md:93` | `fe94393479c3` |
| iteration 1 / injection | FAIL | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_01/6ad90e9fa38cc384483b1c80_0_injection.md:308` | `f6209f142f3f` |
| iteration 3 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_03/6ad90e9fa38cc384483b1c80_0_injection.md:319` | `fa8938c8b378` |
| iteration 5 / injection | PASS | COMPLETE / not stated in final block | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_05_review_intake/6ad90e9fa38cc384483b1c80_0_injection.md:326` | `3721036cd9fa` |
| iteration 2 / prompt | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_02/6ad90e9fa38cc384483b1c80_1_prompt.md:324` | `4f20380b9bbb` |
| iteration 3 / prompt | FAIL | COMPLETE / 2 | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_03/6ad90e9fa38cc384483b1c80_1_prompt.md:314` | `4c243957f2d6` |
| iteration 5 / prompt | PASS | COMPLETE / 5 | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_05_review_intake/6ad90e9fa38cc384483b1c80_1_prompt.md:403` | `2716e8814a0d` |

## task_inputs_TASK_E

Delivered; no returned external report found; active loop cancelled.

| Stage | Preserved sequence of overall verdicts |
|---|---|
| injection | No original external report preserved |
| prompt | No original external report preserved |
| hardness | No original external report preserved |
| oe | No original external report preserved |
| rubrics | No original external report preserved |


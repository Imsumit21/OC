# Imported Portal report inventory

Counts below are report documents after byte deduplication, not distinct task deliveries.

| Stage | PASS | NON-FAIL | FAIL |
|---|---:|---:|---:|
| injection | 21 | 0 | 4 |
| prompt | 6 | 4 | 13 |
| hardness | 0 | 6 | 5 |
| oe | 4 | 3 | 0 |
| rubrics | 3 | 0 | 15 |

Imported source files: 91. Unique full SHA-256 reports: 84. Named artifact versions hashed: 446.

| Container | Stage | Verdict | Evidence | Report SHA-256 |
|---|---|---|---|---|
| archived task/task_inputs-n | hardness | NON-FAIL | `archived task/task_inputs-n/6acefd9770b8942247032c9e_1a_hardness.md:140` | `4520e946ada6b00968f425085dc3810b93ab378cdc7ee4f9b1dba0bfae986afa` |
| archived task/task_inputs-n | injection | PASS | `archived task/task_inputs-n/6acefd9770b8942247032c9e_0_injection (1).md:170` | `dc35ad41a85012b97084eab682dc0fe831638c244834ad21ae39070c43b2d7f4` |
| archived task/task_inputs-n | injection | PASS | `archived task/task_inputs-n/6acefd9770b8942247032c9e_0_injection.md:176` | `444afad55f9d2bcc8068f53a068d0ac1eea7b7ba581781f650245d6412364ba2` |
| archived task/task_inputs-n | prompt | NON-FAIL | `archived task/task_inputs-n/6acefd9770b8942247032c9e_1_prompt (3).md:531` | `9d72a55293f51aa04a9c74984f248384ec1ed888c286132b542d272bf0f06839` |
| archived task/task_inputs-n | prompt | FAIL | `archived task/task_inputs-n/6acefd9770b8942247032c9e_1_prompt.md:435` | `16f32034ecc53bb8350c7bf83b95fbff776c253db2740773eed6b83cae86f304` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | hardness | NON-FAIL | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1a_hardness (1).md:97` | `cd1d55b8e9c02b4eb6fdeb16e4b56e8168a63624045784ec2f9092c1aae81be5` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | hardness | NON-FAIL | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1a_hardness.md:113` | `621966f1e339aac0ee20fc85a07e4c111d0d859a8d49244ce9c48772674c15c9` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | injection | PASS | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_0_injection (1).md:567` | `7612661f4c2b8be0f1b955a10920c4223b50a58e1089e58c70cc635e552d3b37` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | injection | PASS | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_0_injection (2).md:622` | `0f3928d70a905eedbbdb4706299c7aeb8d6e7efceff918f07d38f0cb8956af0d` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | injection | PASS | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_0_injection (3).md:589` | `63ce014b440b6c633b9c4c1f279e22e66daa1ae25586788bcc0c38ce207a73db` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | injection | PASS | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_0_injection (4).md:568` | `ca4cb95b8183456fe65825e3d82d91411199c315d63feec878eb3977f186f8b0` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | injection | PASS | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_0_injection.md:555` | `c318666fc6f8f09b8983d99e6d9ea5f25c2092844966a0e7e3a7ab5ba86e89d2` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | oe | PASS | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_2_oe (1).md:126` | `3507f980bb2f0cdcd5c4622d8aa434a2e634c6fb48f907b952f53721915bca4f` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | oe | NON-FAIL | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_2_oe.md:137` | `9a9455f2073360ee6ed276717d57c8d6df7e50f8c9ce3a72ae1e849a5b86f37a` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | prompt | FAIL | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1_prompt (1).md:371` | `bc3d2c5e4d68cda189421fb5361a96f2d2c26efe5c712dda946b885ac16bece5` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | prompt | PASS | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1_prompt (2).md:420` | `412ca701caed87b3cf50da254749b60dfdad2687417b55a06ec171da03eb3cdf` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | prompt | PASS | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1_prompt (3).md:566` | `9cd788e1662549e40fe8135a08878615f4b6180443ca1871f1eaabf282c0017e` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | prompt | NON-FAIL | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_1_prompt.md:377` | `106262692401fd35b76c062ad85952b8fb8946d3b8aa89c06980b863d2a7fd2c` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | rubrics | PASS | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_3_rubric (1).md:151` | `d440a207c6227bd6cf6f39e36f83da7bed92c36bb1b3edad077f3a0364d6b36a` |
| completed_tasks/douglas_beta_server_signoff_2026-10-28 | rubrics | FAIL | `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_3_rubric.md:223` | `1394b532749316979b2c86a879e8532675c8f5a3dc0414e6e9d7c4e1b464a75d` |
| task_inputs | injection | FAIL | `Task_Authoring/task_inputs/plateform_reports/6adfee3e0350cc55431db61d_0_injection.md:212` | `a49bdc3f66ac15a32cc6ea72796e960f1f5b22bff2e4e7843a6729ec8f6689c2` |
| task_inputs-skipped | hardness | FAIL | `Task_Authoring/task_inputs-skipped/Plateform_reports/01_hardness.md:90` | `a7f1fad768b43ac9a56a3f36158e797320f79ff37d5da450b8aad8c5e01423ae` |
| task_inputs-skipped | hardness | NON-FAIL | `Task_Authoring/task_inputs-skipped/Plateform_reports/02_hardness.md:147` | `f7d7fd9ce4956c9f45a358e555b74c8c4ccb0972795380267057096b8c9e9467` |
| task_inputs-skipped | injection | FAIL | `Task_Authoring/task_inputs-skipped/Plateform_reports/01_injection.md:125` | `4ac9782dbdd5fcae943004ade6325015bcda5df2434560a1af5aaff1e2da10f0` |
| task_inputs-skipped | injection | FAIL | `Task_Authoring/task_inputs-skipped/Plateform_reports/03_Injection.md:140` | `41a855cdb7f1537b771fa5cd707a43a461bdcb26fdf59c0727dc167d4dac9b62` |
| task_inputs-skipped | injection | PASS | `Task_Authoring/task_inputs-skipped/Plateform_reports/2_injection.md:134` | `4ef66c8a1b2db2f900796035ded5cbdec627714e70c2d90b2f16e98d4ea910ff` |
| task_inputs-skipped | oe | PASS | `Task_Authoring/task_inputs-skipped/Plateform_reports/01_OE_Report.md:118` | `1a2d73b3c5a34ffaaccab1f71f9c90024d7a6ce631df78efd50b5b5cbfa412fd` |
| task_inputs-skipped | prompt | FAIL | `Task_Authoring/task_inputs-skipped/Plateform_reports/01_prompt.md:374` | `af23fa5a5820cada842787593014f6bd2ced90c6504cea1fef3efe7f8920af94` |
| task_inputs-skipped | prompt | FAIL | `Task_Authoring/task_inputs-skipped/Plateform_reports/02_Prompt.md:460` | `9934f381c0cc4ab815e271858f0170ac7ed558574d093d03c5950e1ca8b34818` |
| task_inputs-skipped | rubrics | FAIL | `Task_Authoring/task_inputs-skipped/Plateform_reports/01_Rubrics.md:328` | `67f08b2a1175f3e6b906c71860a0135566f2eca33139bd03be2adcca7622b380` |
| task_inputs-skipped | rubrics | FAIL | `Task_Authoring/task_inputs-skipped/Plateform_reports/02_Rubric.md:189` | `14548b65e5625ed53146a3f30725cd1165bb02de04e4337b1d6527775d2d222f` |
| task_inputs-skipped | rubrics | FAIL | `Task_Authoring/task_inputs-skipped/Plateform_reports/03_Rubric.md:169` | `bfbc3ac6d62df41a5e5f06683e7808c680e9d01ec3692277a90b5d52b3833e08` |
| task_inputs-skipped | rubrics | FAIL | `Task_Authoring/task_inputs-skipped/Plateform_reports/04_Rubric.md:153` | `aaf1e863f891c8bdae884aafc258221fe98797c6166de71f2ad47d28d5955dcb` |
| task_inputs_TASK_B | hardness | FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_04_hardness/6ad90e9449d1194f4e538cdf_1a_hardness.md:98` | `d925b73c4ca71868b1e642ba16fb2f2949ea4d818071bb5757bf1b4353400ee2` |
| task_inputs_TASK_B | hardness | FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_12_report_intake/6ad90e9449d1194f4e538cdf_1a_hardness.md:109` | `ad513daef793bd11364b87719b6c70911ea53a19ebae5144b4fa6463c6897115` |
| task_inputs_TASK_B | hardness | NON-FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_17_report_baseline_intake/received/6ad90e9449d1194f4e538cdf_1a_hardness.md:147` | `8d312c4ae9de086f3936e2d1360445884f9b5b94b40999d959ca408b1cb685eb` |
| task_inputs_TASK_B | injection | PASS | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_01/injection eval.md:199` | `6b86741fac820fb8e46a0ce4b5cb6d209773f57a55b8a95961cf256bc80613e5` |
| task_inputs_TASK_B | injection | PASS | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_02/6ad90e9449d1194f4e538cdf_0_injection.md:363` | `ab653d4f7729699b8d21d1a8d41c7ad2a6d89d8d193c3a0600fc3520d910c1a0` |
| task_inputs_TASK_B | injection | PASS | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_03/6ad90e9449d1194f4e538cdf_0_injection (2).md:365` | `22d0395015adec57bed10a6f8250bf02854a625ff285de1e7be3392db59ac63d` |
| task_inputs_TASK_B | injection | PASS | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_08_report_intake/6ad90e9449d1194f4e538cdf_0_injection (4).md:435` | `6eb31ee6ede1980794b26579fcd9dcd5d533327ec5013dc53cbd0b16b561ada5` |
| task_inputs_TASK_B | injection | PASS | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_10_report_intake/6ad90e9449d1194f4e538cdf_0_injection.md:441` | `da6dcb842b1494211667f26f289c63a11e3f41bb85213bc7abf6833d92b8c3b1` |
| task_inputs_TASK_B | injection | PASS | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_12_report_intake/6ad90e9449d1194f4e538cdf_0_injection.md:485` | `12c5f855c9cb71d67d950e39f9a28db60f97dae89047e12201277d944bf64917` |
| task_inputs_TASK_B | injection | PASS | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_14_report_intake/6ad90e9449d1194f4e538cdf_0_injection.md:447` | `63722c2b83ca9196e3a880f2dc01289b458e856698f6cbc5a5048802b3408acb` |
| task_inputs_TASK_B | injection | PASS | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_17_report_baseline_intake/received/6ad90e9449d1194f4e538cdf_0_injection.md:447` | `4f190ad267afdc45b9776873480f8e691ac4b8d3afbbdc6be455ef6f43b82fcf` |
| task_inputs_TASK_B | oe | NON-FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_20_oe_report_reconciliation/received/6ad90e9449d1194f4e538cdf_2_oe.md:155` | `33c45b40ff33fe8dcd2efcd87ce9b7cd10b3a74bb63b640f39a6dc4839785205` |
| task_inputs_TASK_B | oe | PASS | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_21_oe_pass_report_reconciliation/received/6ad90e9449d1194f4e538cdf_2_oe (1).md:147` | `8eb9b05c203cb0505d6d94bf9590f03082e88303b7f1fe5bc9535ce9637abf0e` |
| task_inputs_TASK_B | prompt | FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_01/prompt eval.md:451` | `e3ad958a09b2a1bd790ba41af5acfd53846fd03d225b75c1545bd82dc3525297` |
| task_inputs_TASK_B | prompt | FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_02/6ad90e9449d1194f4e538cdf_1_prompt.md:353` | `a047869e2baa9d6340531fa519fff20ed15f0bc5d2333c2078ea7ee516106f10` |
| task_inputs_TASK_B | prompt | PASS | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_03/6ad90e9449d1194f4e538cdf_1_prompt (2).md:401` | `f8f56661c71a7410afc37e8e9881a7b5c36b0981504ef231578b491b5008cf1e` |
| task_inputs_TASK_B | prompt | FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_08_report_intake/6ad90e9449d1194f4e538cdf_1_prompt (4).md:482` | `a9cdc22ab568f549e1c44bd33737cbb52e5845d8b3c193b477806ce7d495b9e2` |
| task_inputs_TASK_B | prompt | FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_10_report_intake/6ad90e9449d1194f4e538cdf_1_prompt.md:468` | `6668cfe83ef0ff50158c8c2aba93ebf370fd6f68153d8b55736be86dfb9e8f38` |
| task_inputs_TASK_B | prompt | PASS | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_12_report_intake/6ad90e9449d1194f4e538cdf_1_prompt.md:573` | `51569108c3c0529c26a3e46fb3595b41ecb2c763c6ba1dde501ff5d38e84c64f` |
| task_inputs_TASK_B | prompt | NON-FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_14_report_intake/6ad90e9449d1194f4e538cdf_1_prompt.md:668` | `3f706250ace1adc560e8a8939ad9859c2372af5b276e15b1a02b5683446b97bd` |
| task_inputs_TASK_B | prompt | PASS | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_17_report_baseline_intake/received/6ad90e9449d1194f4e538cdf_1_prompt.md:644` | `c86f258edd1c2a2ce90036c0a724ffc426e40b4b24069ca0094621859f288b1a` |
| task_inputs_TASK_B | rubrics | FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_23_external_rubric_intake/received/6ad90e9449d1194f4e538cdf_3_rubric (3).md:149` | `2fcf37e70c368c2d703697759a37cdb48bd076ea07bb9c680c1d3604fd4b70f8` |
| task_inputs_TASK_B | rubrics | FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_26_latest_rubric_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (6).md:180` | `0a26ffd2d199befab06b8ce1b0292cc68bb6ef0ef765bc0d383e625f8a8c23bd` |
| task_inputs_TASK_B | rubrics | FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_26_latest_rubric_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (7).md:194` | `d7ef5a30f900b5cb0dbde3bd3a15f6efa7faedd91ddd94763a1e3521b5c0a12c` |
| task_inputs_TASK_B | rubrics | FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_27_rubric_scope_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (8).md:192` | `1df8947d7f77835e2845855cc8d182cda939c054a565b3ed9535fae76ff4a045` |
| task_inputs_TASK_B | rubrics | FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_28_rubric_semantic_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (10).md:182` | `dd432e1e52675c560071c21e05b9a7c4a53b2ef85415e722afa4f4b287ca7894` |
| task_inputs_TASK_B | rubrics | FAIL | `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_30_rubric_alias_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (11).md:180` | `934e103b9a0e8597306a98db7ef5691aa1545bb9bfa209bafd89677a15a9d1fa` |
| task_inputs_TASK_D | hardness | FAIL | `Task_Authoring/task_inputs_TASK_D/Audit-Report/20261024T165457Z_email_1a16ed677b050dd3/originals/6ad90e94adb09db24624b216_1a_hardness fail report current injection.md:122` | `c21b66ad2ca8100f90e031a6bc742e708daa3d5346718a1c27490dbd148b3157` |
| task_inputs_TASK_A | hardness | NON-FAIL | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_07_hardness/6ad90e93a2c3542255f64fbf_1a_hardness.md:93` | `f422e99dbaf1897bbf624000ddc8a48f759207fc73eba03fdf376ca8c97b94f5` |
| task_inputs_TASK_A | injection | PASS | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_01_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_0_injection.md:125` | `bc4c36a448d18f9f75e4ba59c22ec9658f1dc0f3af0b6c150a9520aef00207b2` |
| task_inputs_TASK_A | injection | PASS | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_03_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_0_injection (1).md:146` | `0383ca237e25606dbc0bd0865f46805acd66ad67089a0c34bd5c2f4d391dffdc` |
| task_inputs_TASK_A | injection | PASS | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_05_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_0_injection.md:146` | `abf2ebc55de1f2bed83a7aa3ea46cee2e26349e4894638e590213a68669a8de1` |
| task_inputs_TASK_A | oe | NON-FAIL | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_09_oe_portal/6ad90e93a2c3542255f64fbf_2_oe.md:143` | `caa1f34b339b3fba955d6988c3c6b81ce2bfea4b599f2ef0721f75a271408a49` |
| task_inputs_TASK_A | oe | PASS | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_11_oe_v2_pass/6ad90e93a2c3542255f64fbf_2_oe (1).md:143` | `2f493451621077165619921fa42b081b48a0c03824a4a95712971e635a60fda3` |
| task_inputs_TASK_A | prompt | FAIL | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_01_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_1_prompt.md:377` | `7743fee5d4afc1a07a9e60da099cc84557afe6c0344945322b403eded19d2e84` |
| task_inputs_TASK_A | prompt | FAIL | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_02_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_1_prompt (1).md:405` | `ea68cd7f999512ecb71c008fe880effb74fb1ac716365970d8b0d230be04b31f` |
| task_inputs_TASK_A | prompt | FAIL | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_03_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_1_prompt (2).md:456` | `c86a9124098cc9679370e5894525999cfc619262c15d86f77cde4a493921d0f5` |
| task_inputs_TASK_A | prompt | NON-FAIL | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_05_portal_6ad90e93a2c3542255f64fbf/6ad90e93a2c3542255f64fbf_1_prompt.md:539` | `5376eaf6f1ef0efe2edc5ed2c96db10d0625f0fd61d284391ea37e6d814cc94a` |
| task_inputs_TASK_A | rubrics | FAIL | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_12_rubric_portal_20261025/6ad90e93a2c3542255f64fbf_3_rubric.md:187` | `f83fa6e15837b08fdf316a4c18a674ffd26185a22d6fa9780edd15ecdd92ce2e` |
| task_inputs_TASK_A | rubrics | FAIL | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_13_rubric_portal_r2_20261025/6ad90e93a2c3542255f64fbf_3_rubric (1).md:143` | `3fd0e213042a0515d21a02393105875c6c1e94d24f5cb2d7dd480d41f609a9b2` |
| task_inputs_TASK_A | rubrics | FAIL | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_14_rubric_portal_r3_20261025/6ad90e93a2c3542255f64fbf_3_rubric (2).md:124` | `07da306f688a5dc630a1f08c5876aee6125c40599283095e050b1bc725ab48a9` |
| task_inputs_TASK_A | rubrics | PASS | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_15_rubric_portal_r4_pass_20261025/6ad90e93a2c3542255f64fbf_3_rubric (3).md:131` | `d8542cdd1ec26287278041bcf7ff4ef3464c6e6182b77164068b0d437bd45f1a` |
| task_inputs_TASK_A | rubrics | FAIL | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_16_rubric_portal_r5_20261026/6ad90e93a2c3542255f64fbf_3_rubric (4).md:120` | `3d55dcfdf711cfc5c33203f250e31852a1fa7303176d41d2727df6589b9f0bcd` |
| task_inputs_TASK_A | rubrics | PASS | `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_18_verifier_intake_20261027/6ad90e93a2c3542255f64fbf_3_rubric (6).md:117` | `4fd8cddfc60bfd6b0075c1d9315f50c584dba40a17f363243fa209a3392292df` |
| task_inputs_TASK_C | hardness | FAIL | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_05_review_intake/6ad90e9fa38cc384483b1c80_1a_hardness.md:93` | `fe94393479c37f1a7e2025c0d21ee59e618be52228e547c02615a48736e1428d` |
| task_inputs_TASK_C | injection | FAIL | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_01/6ad90e9fa38cc384483b1c80_0_injection.md:308` | `f6209f142f3f32fa86dbb9538f5385a6c154c82e1f7b29112b0f9485af098d03` |
| task_inputs_TASK_C | injection | PASS | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_03/6ad90e9fa38cc384483b1c80_0_injection.md:319` | `fa8938c8b378f71486e13bf62eb7d585d6931dda01d48458eb514fc95107f927` |
| task_inputs_TASK_C | injection | PASS | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_05_review_intake/6ad90e9fa38cc384483b1c80_0_injection.md:326` | `3721036cd9faf1166c131304a816c4243f629077e577a80e73e3c425a4af5d99` |
| task_inputs_TASK_C | prompt | FAIL | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_02/6ad90e9fa38cc384483b1c80_1_prompt.md:324` | `4f20380b9bbb338c756bb3f36ed55e591399fb331b7f6e6edea3f30bef8f5898` |
| task_inputs_TASK_C | prompt | FAIL | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_03/6ad90e9fa38cc384483b1c80_1_prompt.md:314` | `4c243957f2d6da09c8abc96da0d43e605976d294103a7605bd814a53b48c60de` |
| task_inputs_TASK_C | prompt | PASS | `Task_Authoring/task_inputs_TASK_C/Audit-Report/iteration_05_review_intake/6ad90e9fa38cc384483b1c80_1_prompt.md:403` | `2716e8814a0d64f5f4b67f4bd2584909f744df2fc041d2f4f858e6e0b3f5cce6` |

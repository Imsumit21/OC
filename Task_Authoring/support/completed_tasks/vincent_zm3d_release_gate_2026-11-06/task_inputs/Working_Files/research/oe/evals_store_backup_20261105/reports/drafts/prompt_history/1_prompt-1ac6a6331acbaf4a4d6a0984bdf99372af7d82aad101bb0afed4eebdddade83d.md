# Prompt evaluation — dd-q4-storefront-pack (rev7)

**Review version:** `prompt-source-checks-v2`
**Eval:** `task-quality-v1` / `prompt-ugt-v1` (local package)
**Clock:** 2025-10-01T00:00:00Z (2025-10-01 07:00 UTC)
**Evaluator model:** DeepSeek V4.1 Flash (deepseek-flash), high effort

| Field | Value |
|---|---|
| Persona | Claire Morgan — Art Lead (Design), `claire.morgan@harmonygames.co` |
| Business function | Design |
| Competency | Marketing and GTM |
| Task skill | Actions |
| Horizon | long-horizon |
| Prompt | `Evals/task_inputs/04_Prompt.txt`, 933 bytes, sha256 `2d70402938fd81a4a8c41f42466a77b72e16c84e56827874204511fab6ebd095` |
| Injection | `Evals/task_inputs/01_Universe_Inject.sql`, 201,848 bytes, sha256 `6e9811fa4b513d97d9699f132c3e71f8a738439b46d985c3f9bc9627d48f3d98` |

## Injection Gate

- State: **CURRENT**
- Reviewed SQL: `6e9811fa4b513d97d9699f132c3e71f8a738439b46d985c3f9bc9627d48f3d98`
- Eval 0: **PASS** (`injection-static-v2`, COMPLETE; `Evals/task_inputs/reports/0_injection.md`)

## Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Pick up the brief and close out the pack | Trello card `68cd29a0360c3a795cc9a432` and its two comments | Trello search/get | Trello reads | Unscoped | Window, floor, claims, duplicate, scope, destination and ticket rules |
| Reconcile every submission | `ART-793` and its 68 children; `DES-313`–`DES-372` | Linear get/list comments/attachments | Linear reads | Unscoped | Per-submission decision |
| Apply build floor | Gmail floor memo; 2.0 floor decoy | Gmail search/get | Gmail read | Claire's mailbox | Floor holds; two regimes |
| Apply claims pass | Claims doc; August Slack decoy | GDocs read | GDocs read | Shared | Claim holds |
| Apply delivery/FR/ES | Martin 24/26 Sep | Gmail | Gmail read | Claire's mailbox | ES in; FR r2 supersedes r1 |
| Storefront scope/waves/slots | Q4 plan; deck; Confluence policy | Sheets/Slides/Confluence | Reads | Shared/unscoped | 34 storefronts, 14/20, 184/168/16 |
| Register on `Q4 pack` | Tab `Q4 pack` | Sheets | `gsheets_values_update` | Writer | 60 rows, one per asset |
| Storefront table on `Storefronts` | Tab `Storefronts` | Sheets | `gsheets_values_update` | Writer | 34 rows a1–a6 |
| Re-capture tickets on the Art board | `ART-793` comment | Linear | `linear_create_issue` | Unscoped write | 8 tickets, floor/claim only |
| Pack note to Marcus cc Robert | Frederick 27 Sep; Contacts | Gmail/Contacts | `gmail_send_message` | Writes unscoped | `marcus.lee@`, cc `robert@`, subject |
| Counts in `#artstyle_themes` | `C083AEASRPC` | Slack | `slack_conversations_add_message` | Member | Register, storefront and slot totals |
| Handoff comment on the brief card | Card 41 | Trello | `trello_add_comment` | Unscoped | Comment with counts and ticket count |

## Phase 1 — Structure and persona

| Dimension | Score | Basis |
|---|---|---|
| Persona | 5 | Art Lead owns the pack (`ART-721`, `ART-777`, the art channel, the shared capture sheet) |
| Business function | 5 | Design: storefront creative review and pack closure |
| Competency | 5 | Marketing and GTM: store listing refresh, UA handoff |
| Task skill | 5 | Actions: six writes over five services |
| Horizon / complexity | 5 | Long-horizon; 10 services; three load-bearing dimensions |

## Phase 2 — Depth

Unique Ground Truth: Score 5. The brief card now fixes the decision vocabulary (`SHIP`, `HOLD`, `DROP`), says a capture whose locale has no matching storefront is not held for an overlay, says a cut-level capture still gets a `DROP` row, and the claims doc says a superseded overlay does not clear a claim hold. The plan note defines storefront totals and the wave-two slots; Frederick's note asks for the wave-one counts. The KO, out-of-scope storefront, locale-DE and slot-count forks are closed by visible records.

Clarity & Specificity: 5. The prompt names both tabs, the Art board in Linear, the recipient and cc, the art channel, the brief card and the three slot counts. The plan note defines the totals and the register note defines the sort key.

Contrived / Unnatural: 5. Ordinary first-person handoff; no opaque ids, timestamps, riddles or format rules.

Alignment with Today's Date: 5. "2 October 2025" is a future deadline after the 1 October clock; no post-clock event is described as done.

Truthfulness: 5. The brief card, the empty pack tab, the two tabs, the Art board, the UA recipient, Robert, `#artstyle_themes`, the 2 October window and the record volume all resolve; no phantom identifier.

Tool Use & Cross-service: 5. Linear comments/attachments, Gmail floor/delivery/recipient, Sheets plan/register/pack, Slides deck, Confluence policy, Trello card, Slack channel and Contacts recipient are scattered and reconciled.

Investigation + Action: 5. The six writes depend on membership, floor, claims, duplicate, scope, join, delivery and counts.

Coherence: 5. One pack close and one handoff; no bolt-on.

Originality: N/A, no samples supplied.

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: The brief, the plan, the Confluence page and the claims record settle the forks: the KO captures clear with no storefront, PENDING storefronts are out, locale DE has no English fallback, the decision vocabulary and dropped-row rule fix the register classes, a superseded overlay does not clear a claim hold, and the slot counts are planned, filled and short.

Alternative selection: The strongest alternative is the KO reading: it is the only fork where a missing overlay could plausibly turn clears into holds and change both the register and the storefront cells. The other forks are settled by explicit plan or policy wording.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | The pack is the 60 in-pack Domino Delights submissions. The four KO captures clear with no storefront because the KO storefronts carry locale EN; the KO storefronts take the EN master; only floor and claim holds get tickets. | 38 SHIP, 18 HOLD (6 floor, 2 claim, 10 alternate), 4 DROP; ART-849/851/852/853 SHIP with no storefront; ART-850 HOLD claim with a ticket. | 60 register rows; 34 storefront rows; 8 re-capture tickets; one pack note; one Slack post; one brief-card comment. | Q4 pack tab and Storefronts tab in the same workbook; art board for tickets; \#artstyle\_themes; brief card. | register totals 38/18/4; 34 storefronts (14 wave-1, 20 wave-2); 184 planned / 168 filled / 16 short; 8 tickets; KO rows SHIP and KO storefronts use EN. | CARD\_CLEAR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 325-325): "A capture whose locale has no matching storefront in the pack is not held for an overlay; it clears with no storefront, gets a register row, and its decision is SHIP."; PLAN\_KO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 385-385): "\["KO/ios","KO","ios","EN","2","LIVE","wave 2"\]"; EPIC\_TICKET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 321-321): "Only a capture held for the build floor or for a claim needs one; an alternate or a capture held only for an overlay does not."; CARD\_CLAIM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 325-325): "A capture whose overlay text fails the claims pass is held with decision HOLD and gets a ticket whether or not its locale has a storefront."; CARD\_DECISION (Evals/task\_inputs/01\_Universe\_Inject.sql lines 325-325): "The decision column uses SHIP, HOLD and DROP."; CARD\_DROP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 325-325): "A capture of a level that is not in the Q4 build is dropped: it still gets a register row with decision DROP."; CLAIMS\_SUPERSEDE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 377-377): "A superseded overlay does not clear a claim hold; the capture stays held until its overlay text is claims-clean."; PLAN\_TOTALS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 385-385): "Storefront totals are the count of in-pack storefronts, split by wave."; PLAN\_WAVE2 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 385-385): "Wave 2 uses slots 1-5; a6 stays empty." |
| B | The four KO captures are held for the undelivered KO overlay, and the KO storefronts are their intended recipients; the register therefore has fewer clears and more holds, and the KO storefront cells change. | 34 SHIP, 22 HOLD (6 floor, 2 claim, 10 alternate, 4 KO overlay), 4 DROP; ART-849/851/852/853 HOLD for the missing KO overlay; ART-850 HOLD claim with a ticket. | 60 register rows; 34 storefront rows; 12 re-capture tickets; one pack note; one Slack post; one brief-card comment. | Q4 pack tab and Storefronts tab in the same workbook; art board for tickets; \#artstyle\_themes; brief card. | register totals 34/22/4; 34 storefronts (14 wave-1, 20 wave-2); 184 planned / 168 filled / 16 short; 12 tickets; KO storefronts take the KO captures, not the EN master. | PLAN\_KO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 385-385): "\["KO/ios","KO","ios","EN","2","LIVE","wave 2"\]"; MAIL\_ES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 341-341): "The ES overlays are still with the glyph fix."; MAIL\_CORR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 344-344): "Correction: the ES glyph fix landed on the 25th, so the ES overlays are in this wave." |

Explicit option inventory: The prompt asks for one pack and one set of destinations; it contains no explicit option list to choose from.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "The brief and the records have what we agreed."

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. The card says a capture whose locale has no matching storefront is not held for an overlay and records SHIP; the plan's KO rows carry locale EN; the four KO captures therefore clear with no storefront. The claims rule still holds ART-850, and the decision vocabulary keeps the register at 38 SHIP / 18 HOLD / 4 DROP, so the alternative's 34/22/4 and 12 tickets do not stand.
Resolution evidence: CARD\_CLEAR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 325-325): "A capture whose locale has no matching storefront in the pack is not held for an overlay; it clears with no storefront, gets a register row, and its decision is SHIP."; PLAN\_KO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 385-385): "\["KO/ios","KO","ios","EN","2","LIVE","wave 2"\]"; EPIC\_TICKET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 321-321): "Only a capture held for the build floor or for a claim needs one; an alternate or a capture held only for an overlay does not."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | The KO captures are SHIP in the lead reading and HOLD for the missing overlay in the alternative; the class totals are 38/18/4 vs 34/22/4. |
| writes | DIFFERENT | The alternative adds four tickets and changes four register decisions. |
| destinations | SAME | Both readings write the same destinations: Q4 pack tab, Storefronts tab, art board, Marcus note, \#artstyle\_themes and brief card. |
| contents | DIFFERENT | The posted and emailed counts and the KO storefront cells differ. |

Authority chain: P → CARD\_SCOPE → CARD\_CLEAR → PLAN\_KO

Resolution relevance challenge: The card's clearing rule and the plan's KO locale are direct evidence on the exact fork: they decide what happens to a capture with no storefront.
Delegation challenge: NOT_CLAIMED. No record delegates the KO decision; the brief and the plan settle it directly.
Challenge evidence: CARD\_CLEAR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 325-325): "A capture whose locale has no matching storefront in the pack is not held for an overlay; it clears with no storefront, gets a register row, and its decision is SHIP."; PLAN\_KO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 385-385): "\["KO/ios","KO","ios","EN","2","LIVE","wave 2"\]"

Strongest-alternative challenge (B): A missing KO overlay is a real delivery gap in the thread, so holding the KO captures is the most plausible non-truth reading; it changes four decisions, four tickets and the KO storefront cells.
Challenge evidence: CARD\_CLEAR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 325-325): "A capture whose locale has no matching storefront in the pack is not held for an overlay; it clears with no storefront, gets a register row, and its decision is SHIP."; PLAN\_KO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 385-385): "\["KO/ios","KO","ios","EN","2","LIVE","wave 2"\]"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

## Phase 3 — Universe feasibility

| Dimension | Score | Basis |
|---|---|---|
| Data Exists | 5 | 11/11 asserted entities verified; 60 in-pack captures, 60 levels, 40 plan rows, 34 storefronts, 8 tickets, 7 overlay files |
| Cross-Service Coherence | 5 | 29-of-33 and 26-more reconcile; ART-793 postdates ART-792; the 2.0 freeze is below the August captures; the ES correction corrects the 24 Sep mail; the plan, deck and Confluence agree on scope and locale DE |

## Phase 4 — Final evaluation

| Dimension | Score |
|---|---|
| Prompt — Unique Ground Truth | 5 |
| Prompt — Feasibility | 5 |
| Prompt — Persona ACL Reachability | 5 |
| Prompt — Explicit Tool Mention | 5 |
| Prompt — Clarity & Specificity | 5 |
| Prompt — Contrived / Unnatural | 5 |
| Prompt — Alignment with Today's Date | 5 |
| Prompt — Truthfulness | 5 |
| Prompt — Tool Use & Cross-service | 5 |
| Prompt — Investigation + Action | 5 |
| Prompt — Coherence | 5 |
| Prompt — Persona | 5 |
| Prompt — Business Function | 5 |
| Prompt — Competency | 5 |
| Prompt — Task Skill | 5 |
| Prompt — Complexity & Seeding | 5 |
| Universe — Data Exists | 5 |
| Universe — Cross-Service Coherence | 5 |
| Originality / Sample Similarity | N/A |

Final score: 5

## Deep Recheck

Passes P1–P4 were run on the saved prompt and SQL; every finding below was checked against the cited record.

**Final rev7 rerun.** P1, P3 and P4 returned no fail-level finding on the final text. P1 confirmed all seven forks are settled by the card, plan note, claims doc and mail. P3 confirmed the Linear Art board, the handoff comment, the planned/filled/short definitions, the storefront-total definition, `#artstyle_themes` membership, the Marcus Lee contact and both tab names. P4 found the rev7 wording natural and the terms defined. P2 confirmed the attachment sequence, ART-793 ordering, the 2.0 freeze, the JA/KO explanation, the 29/33 and 26-more arithmetic, and the 38/18/4 split; its remaining items are the advisories below.

| Finding | Pass | Disposition | Settling record |
|---|---|---|---|
| KO captures clear or held for the absent KO overlay | P1 | CONFIRMED then fixed | Card: "A capture whose locale has no matching storefront in the pack is not held for an overlay; it clears with no storefront, gets a register row, and its decision is SHIP." Plan KO rows carry locale EN |
| Decision buckets 34+4 clear vs 38 SHIP | P1 | CONFIRMED then fixed | Card: "The decision column uses SHIP, HOLD and DROP." |
| ART-808 claim vs FR r2 supersession | P1 | CONFIRMED then fixed | Claims doc: "A superseded overlay does not clear a claim hold; the capture stays held until its overlay text is claims-clean." |
| Dropped captures 56 vs 60 register rows | P1/P2 | CONFIRMED then fixed | Card: "A capture of a level that is not in the Q4 build is dropped: it still gets a register row with decision DROP." |
| "Storefront totals" undefined | P1/P4 | CONFIRMED then fixed | Plan note: "Storefront totals are the count of in-pack storefronts, split by wave." |
| Mail wave-1 vs pack counts | P1 | CONFIRMED then fixed | Frederick 27 Sep: "the wave-1 planned, filled and short slot counts" |
| Wave-2 slots could be any five of six | P1 | CONFIRMED then fixed | Plan note: "Wave 2 uses slots 1-5; a6 stays empty." |
| Handoff artifact undefined | P1/P4 | CONFIRMED then fixed | Prompt: "leave a handoff comment on the brief card." |
| "Art board" could be a Trello board | P4 | CONFIRMED then fixed | Prompt: "The re-capture tickets go on the Art board in Linear." |
| Pack tab described as populated | P4 | CONFIRMED then fixed | Prompt: "the pack tab hasn't caught up with the board"; the tab is header-only |
| 26-more count is 27 in-pack | P1/P2 | REJECTED | 26 children were created after the 22 Sep brief note, but 6 are out-of-scope; 33 in-pack before + 20 in-pack after + 7 late = 60 |
| `#artstyle_themes` name/membership | P2 | VERIFIED, no change | `channels.json` `/102` is `artstyle_themes`; Claire is `EMPLOYEE_0009_SLACK_ID` in `members` |
| Marcus on the UA side | P2 | VERIFIED, no change | `contacts.json` `/contacts/164` is Marcus Lee, `User Acquisition Manager`, `marcus.lee@harmonygames.co` |
| Attachments r1 vs folder r3/r2 | P2 | ADVISORY | Martin 24 Sep: "The r1 overlays went out on the 10th"; 26 Sep: a superseded overlay needs the new file dropped in. No graded value reads the filename |
| JA/KO country codes | P2 | ADVISORY | Plan note: "JA and KO are the internal country codes for Japan and Korea." JA rows carry locale JA; KO rows carry locale EN |
| ART-806 ticket when slot 6 is filled | P2 | ADVISORY | Card: below-floor capture is "held for re-capture"; epic: "one ticket per asset". Truth keeps 8 tickets |
| 60 filenames unique after the r1 rename | P2 | REJECTED as a defect; ADVISORY | The 60 attachments share 8 distinct `overlay_<locale>_r1.png` names; the unique key is the attachment `id`. `rev7_binding.json` shows the solver output hash is identical across rev5/rev6/rev7 and no truth key reads a filename |
| Mail "capture still clears" vs claims doc | P2 | ADVISORY | The claims doc's specific sentence controls a claim hold; the mail's sentence is about a superseded overlay with no other defect |
| Write paths, tabs, channel, card | P3 | VERIFIED, no fail | `gsheets_values_update`, `linear_create_issue`, `gmail_send_message`, `slack_conversations_add_message`, `trello_add_comment`; all destination records exist |

No confirmed fail-level finding remains in the final rerun. The four platform forks (KO, PENDING, locale DE, slot totals) are settled by the brief card, plan note, Confluence page and mail thread; the additional local forks (claim/supersession, dropped rows, wave-1 mail counts, wave-2 slots, handoff artifact, Linear Art board) are settled by the claims doc, card, plan note and prompt. The only P2 advisories are the shared attachment filenames (the key is the attachment id, and the solver output hash is identical across rev5/rev6/rev7) and the claims-doc/mail wording, where the specific claims rule controls.

### FINAL VERDICT: PASS

Score: 5

Execution status: COMPLETE

Evaluator model: DeepSeek V4.1 Flash (deepseek-flash), high effort

Eval version: prompt-ugt-v1

Eval release SHA-256: 7fe4811a20427b65fb906ee4133d57ec598dc6a6b11e4f53301eaaae79c80358

Reviewed prompt SHA-256: 2d70402938fd81a4a8c41f42466a77b72e16c84e56827874204511fab6ebd095

Review context SHA-256: 3b7a2ec6ce04cc69c210e2b5a556c6386c2368f37e28177c627b924b5c30593a

Prompt record SHA-256: 0e371e3881cd13e8711c47dd739ac6b744ce0536a0aacb6376c032009363bf1c

Next action: The local `/prompt` review is PASS 5; rerun the platform pair on SQL `6e9811fa4b513d97d9699f132c3e71f8a738439b46d985c3f9bc9627d48f3d98` and prompt `2d70402938fd81a4a8c41f42466a77b72e16c84e56827874204511fab6ebd095`.

Evidence limits: static review only; no SQL executed. The Slack and Contacts reads are local file exports. Live deployment and Agent behaviour are not certified. The injection schema snapshot is unverified.

# Grounding dossier — dd-q4-claims-register

Task: Julia Lawson (Product Manager) certifies 13 named Domino Delights product claims for the Q4 pack at the freeze 2025-10-01T00:00:00Z. Injection: `01_Universe_Inject.sql` (69 INSERT rows, 6 UPDATE companions), 10 schemas, 11 services carrying weight.

## 1.A Structural

Live schema read from `Task_Authoring/references/universe_schema_live.json`; every table below is one of the 144 live tables. Base counts and three sample ids are from the registered exports through `Task_Authoring/tools/hg.py`.

| Table | NOT NULL columns used | Base rows | Three base sample ids | Timestamp form |
|---|---|---|---|---|
| slack.slack_messages | id, ts, channel_id, text, reply_count, reply_users_count, is_activity_message, created_at, metadata_json | 300k+ | `C1CB3D58E38B/1760634904.108679`, `C050WGU41HR/1733805873.196519`, `C05H8KVNU67/1720808060.487089` | ts epoch.seq, created_at tstz |
| slack.slack_channels | id, is_channel, is_private, is_im, is_mpim, is_archived, is_general, num_members, members_json | 985 | `C1CB3D58E38B`, `C050WGU41HR`, `C05H8KVNU67` | created_ts double |
| gmail.gmail_threads / gmail_messages | id, thread_id, user_email | 304 Julia threads | `julia.lawson@harmonygames.co/1772613993035255867`, `julia.lawson@harmonygames.co/1860000000000000001`, `leonard.hayes@harmonygames.co/1860000000000000003` | date offset ISO, internal_date ms |
| gcal.gcal_events | event_id, calendar_id | 11,233 | `evt_001f6c4b17b3693d58f251`, `evt_5c1a7e93b2d04f61a8e7b8`, `evt_7d2b8f04c3e15a69b8d1c3` | tstz / start_json |
| gdrive.drive_files | id, name, mime_type | 53,866 | `f_023c7331d7e34900bd226f`, `f_5a1b2c3d4e5f60718293a4`, `f_6b2c3d4e5f60718293a4b5` | tstz |
| gdocs.docs_documents | document_id, title | 633 | `f_023c7331d7e34900bd226f`, `f_5a1b2c3d4e5f60718293a4`, `f_5a1b2c3d4e5f60718293a5` | tstz |
| gsheets.sheets_spreadsheets / sheets_sheets | spreadsheet_id, title, sheet_id | 600+ | `f_095d4389be482e9ac502b5/0`, `f_6b2c3d4e5f60718293a4b5/0`, `f_7c3d4e5f60718293a4b5c6/0` | tstz |
| linear.linear_issues / comments | id, title, priority, labels_json, links_json, relations_json, is_archived, created_at, updated_at | 3,852 issues; 0 comments | `ENG-2136`, `ENG-2323`, `DES-313` | varchar ISO-Z |
| github.github_pull_requests / pr_comments / timeline_events | id, pr_id, event | 2,629 PRs; 884 comments | `harmonygames-Games/GameOfDominoes#1755`, `#1838`, `#503` | tstz |
| trello.trello_cards / actions | id, name, idBoard, idList | 803 cards | `67ec1f6021f4291d45f9c21e`, `65eb4ec525346c8070ca63e3`, `641f7190800a4c4ac7031494` | tstz; id prefix epoch |
| confluence.confluence_pages / page_versions | id, space_id, title, body, body_format, status, version | 31 pages; 78 versions | `page_domino_gdd`, `page_live_ops_engine`, `page_q4_product_claims` | ISO-Z strings |

## 1.B Entity

| Entity | Canonical spelling | Services and value | Verdict |
|---|---|---|---|
| Julia Lawson | Julia Lawson / julia.lawson@harmonygames.co | Slack `EMPLOYEE_0005_SLACK_ID`, Gmail `julia.lawson@`, Linear `usr_8140f09bf9f1b94c`, Trello `793af7ca6940bf18eb516c75` | AGREE |
| Leonard Hayes | Leonard Hayes / leonard.hayes@harmonygames.co | Slack `EMPLOYEE_0038_SLACK_ID`, Gmail `leonard.hayes@`, Linear `usr_63fffeb4fab5233e`, Confluence `user_EMPLOYEE_0038` | AGREE |
| Brian Foster | Brian Foster / brian.foster@harmonygames.co | Slack `EMPLOYEE_0026_SLACK_ID`, Linear `usr_fc22d5941b2aeb5c`, GitHub `PERSON_0180_GITHUB_USERNAME` | AGREE |
| Calvin Price | Calvin Price / calvin.price@harmonygames.co | Slack `EMPLOYEE_0006_SLACK_ID`, Linear `usr_49b9dfa5208d400d` | AGREE |
| Samuel Turner | Samuel Turner / samuel.turner@harmonygames.co | Linear `usr_caafeec2804b3a67`, Slack `EMPLOYEE_0004_SLACK_ID` | AGREE |
| Domino Delights | Domino Delights; internal codename Game of Dominoes / GoD | `confluence:page_domino_gdd`, `linear:ENG-2136`, `github:harmonygames-Games/GameOfDominoes#1755` | AGREE (dual naming is deliberate and stated in the GDD) |
| DD Product Roadmap | DD Product Roadmap | `trello:65eb4ec525346c8070ca638f`, cards `68daad004f5e6d7a8b9c0d10`, `68d672304f5e6d7a8b9c0d11`, `680222a04f5e6d7a8b9c0d13` | AGREE |
| Harmony Games board | Harmony Games | `trello:640643a3fd8f3ca308d9318e`, decoy card `68d6735c4f5e6d7a8b9c0d12` | AGREE |
| Leadership mpim | mpdm-leonard.hayes--julia.lawson--brian.foster-1 | `slack:C1CB3D58E38B`, members Julia/Leonard/Brian | AGREE |
| Q4 claims draft | Q4 Product Claims | `gdocs:f_5a1b2c3d4e5f60718293a4`; stale copy `gdocs:f_5a1b2c3d4e5f60718293a5` | AGREE (current vs September copy by modified_time) |
| Q4 claims register | Q4 Product Claims Register | `gsheets:f_6b2c3d4e5f60718293a4b5` tabs Register / Old register | AGREE |
| Q4 review event | Q4 product claims review | `gcal:evt_5c1a7e93b2d04f61a8e7b8` (Julia), `evt_7d2b8f04c3e15a69b8d1c3` (Leonard), `evt_8e3c9a15d4f26b7ac9e2d4` (Brian) | AGREE (same ical_uid) |
| Season Pass | Season Pass | `linear:ENG-2136`, `github:harmonygames-Games/GameOfDominoes#1755`, `gdocs:f_c57724584820a26f3bbe54` | AGREE on the entity; designed status conflict below |
| Live-ops engine | Live-Ops Event Engine | `confluence:page_live_ops_engine`, `linear:ENG-2370` | AGREE |

## 1.C Voice

`activity_record_verification_required` is the literal status the shared context supplies for this freeze; each line also cites the dated base evidence that the person was active before 2025-10-01. Voice bands and hours follow `references/universe_kb/conventions.json` keys `slack.per_person_hours_and_style`, `slack.length_chars_by_channel_type`, `gmail.internal_subject_len_chars`, `linear.title_prefixes_by_team`.

| Speaker | Identity | status_at_clock | Dated activity evidence | Voice |
|---|---|---|---|---|
| Julia Lawson | julia.lawson@harmonygames.co | activity_record_verification_required | `slack:C090N54TG79/1758689839.300009` (2025-09-24) | short declarative product notes, 90–220 chars |
| Leonard Hayes | leonard.hayes@harmonygames.co | activity_record_verification_required | `gmail:leonard.hayes@harmonygames.co_1843554280387239889` (2025-09-17) | imperative, one ask per paragraph |
| Brian Foster | brian.foster@harmonygames.co | activity_record_verification_required | `slack:C0880U9751A/1758031982.956109` (2025-09-16) | terse engineering facts |
| Calvin Price | calvin.price@harmonygames.co | activity_record_verification_required | `linear:ZOM-554` (2025-09-19) | short bug-report voice |
| Samuel Turner | samuel.turner@harmonygames.co | activity_record_verification_required | `linear:ZOM-436` (2025-09-17) | numbered checklist voice |
| Arthur Blake | arthur.blake@harmonygames.co | activity_record_verification_required | `github:harmonygames-Games/GameOfDominoes#1755` (2025-03-29) | short approval notes |
| Robert | robert@harmonygames.co | activity_record_verification_required | `confluence:page_domino_gdd` (2025-09-15) | design-doc voice |

## 1.D Keyword

| Term | Hit count and pointer | Role |
|---|---|---|
| Season Pass | `linear:ENG-2136`, `github:harmonygames-Games/GameOfDominoes#1755`, `confluence:page_domino_gdd` | claim C06 and trap T5 |
| Collectibles | `trello:67ec1f6021f4291d45f9c21e`, `slack:C1CB3D58E38B/1759251600.000400` | claim C07 and boundary T13 |
| Hero Offers | `linear:ENG-2323`, `github:harmonygames-Games/GameOfDominoes#1838` | claim C10 and T3 |
| live-claim standard | NEW TERM — introduced in `trello:68daad004f5e6d7a8b9c0d10`, reached via A1 | H1 |
| external wording | NEW TERM — introduced in `trello:68d672304f5e6d7a8b9c0d11`, reached via A1 | H2 |
| player-facing claims only | NEW TERM — introduced in `gmail:julia.lawson@harmonygames.co/1860000000000000001`, reached via A1 | H3 |
| Q4 product claims review | NEW TERM — introduced in `gcal:evt_5c1a7e93b2d04f61a8e7b8`, reached via A1 | meeting record |

## 1.E Persona reach

Command: `python3 Task_Authoring/tools/persona_view.py check-sql julia_lawson Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing /tmp/lb2.txt`.

```
CHECK-SQL as julia_lawson <julia.lawson@harmonygames.co>
[YES LB] L25 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CAFQ4claims9x2m1@mail.gmail.com> - row user_email is the persona
[YES LB] L34 gmail.gmail_messages insert julia.lawson@harmonygames.co/<calendar-5c1a7e93b2d04f61a8e7b8@google.com> - row user_email is the persona
[YES LB] L64 gcal.gcal_events insert evt_5c1a7e93b2d04f61a8e7b8 - event is on the persona's own calendar
[YES LB] L69 gcal.gcal_events insert evt_7d2b8f04c3e15a69b8d1c3 - persona is an attendee and holds a copy
[YES LB] L71 gcal.gcal_events insert evt_8e3c9a15d4f26b7ac9e2d4 - persona is an attendee and holds a copy
[YES LB] L73 gdrive.drive_files insert f_5a1b2c3d4e5f60718293a4 - persona owns the file
[YES LB] L77 gdrive.drive_files insert f_5a1b2c3d4e5f60718293a5 - persona owns the file
[YES LB] L111 gdrive.drive_files insert f_6b2c3d4e5f60718293a4b5 - persona owns the file
[YES LB] L115 gdrive.drive_files insert f_7c3d4e5f60718293a4b5c6 - persona owns the file
[YES LB] L116 gsheets.sheets_spreadsheets insert f_6b2c3d4e5f60718293a4b5 - persona owns the file
[YES LB] L118 gsheets.sheets_spreadsheets insert f_7c3d4e5f60718293a4b5c6 - persona owns the file
verdict: PASS (0 load-bearing rows not visible)
```

| Record | Service | Visibility path | Verdict |
|---|---|---|---|
| `f_5a1b2c3d4e5f60718293a4` | gdocs | Julia owner | YES |
| `f_6b2c3d4e5f60718293a4b5` | gsheets | Julia owner | YES |
| `evt_5c1a7e93b2d04f61a8e7b8` | gcal | Julia own copy, self:true | YES |
| `julia.lawson@harmonygames.co/1860000000000000001` | gmail | Julia INBOX copy | YES |
| `C1CB3D58E38B` | slack | Julia a member of the 3-person mpim | YES |
| `68daad004f5e6d7a8b9c0d10` | trello | unscoped | YES |
| `page_domino_gdd` | confluence | unscoped | YES |
| `67ec1f6021f4291d45f9c21e` | trello | unscoped | YES |

## 1.F Collision

Identity header tokens: the only new tokens are the seeded Google ids, Slack message hashes, GCal evt ids and Trello card ids. No new person token is minted; all authors reuse existing `EMPLOYEE_*_SLACK_ID` / `usr_*` ids.

| Minted id | Service | Lookup command | Result |
|---|---|---|---|
| `f_5a1b2c3d4e5f60718293a4` | gdrive/gdocs | `hg.py search lookup gdrive --ids-file` | 0 hits, scan_complete |
| `f_6b2c3d4e5f60718293a4b5` | gdrive/gsheets | lookup | 0 hits |
| `f_7c3d4e5f60718293a4b5c6` | gdrive/gsheets | lookup | 0 hits |
| `68daad004f5e6d7a8b9c0d10` | trello | lookup | 0 hits |
| `68d672304f5e6d7a8b9c0d11` | trello | lookup | 0 hits |
| `68d6735c4f5e6d7a8b9c0d12` | trello | lookup | 0 hits |
| `680222a04f5e6d7a8b9c0d13` | trello | lookup | 0 hits |
| `ENG-2369`–`ENG-2375` | linear | identifier lookup | 0 hits |
| `DES-313` | linear | identifier lookup | 0 hits |
| `evt_5c1a7e93b2d04f61a8e7b8` | gcal | id lookup | 0 hits |

Formats match the base: `f_` + 22 hex, Trello 24-hex with an epoch prefix, Linear team key + number, `evt_` + 22 hex, `ical_uid` 32 hex + `@hg4`.

## Record ledger

| # | Service | Table | Id | Manifest element | Carrier | Reach | Discovery role |
|---|---|---|---|---|---|---|---|
| 1 | slack | slack_messages | `b5387eae230f3570dc45a9d9462e06f5` | A1 | ● | mpim member | first link |
| 2 | slack | slack_messages | `947998e5e46050c865a2641549310128` | K2/T5/T8 | ● | mpim member | overturning |
| 3 | slack | slack_messages | `dce0ca4cfe773cf514fdda4b59176f73` | T13 | ● | mpim member | boundary |
| 4 | slack | slack_messages | `f763054444e387abf007eeb3e40248ce` | T9 | ● | mpim member | distractor |
| 5 | slack | slack_messages | `a4ff3b737a01e59bc8ee451c3de68924` | T1 | ● | mpim member | claim met first |
| 6-7 | slack | slack_messages | `a189120e4644d11fa3a15f3b882b212e` / `5e6ac22357bcf4105c4ab8d7081f67a9` | C1/C2 mirrors | ● | #engineering-bots | connecting |
| 8-17 | gmail | gmail_threads/messages | `julia.lawson@harmonygames.co/1860000000000000001` | K4/H3 | ● | Julia mailbox | first link |
| 12-14 | gcal | gcal_events | `evt_5c1a7e93b2d04f61a8e7b8` (+2 copies) | meeting | ● | Julia own copy | connecting |
| 15-16 | gdrive/gdocs | drive_files/docs_documents | `f_5a1b2c3d4e5f60718293a4` | A2 | ● | owner | first link |
| 17 | gdrive/gdocs | drive_files/docs_documents | `f_5a1b2c3d4e5f60718293a5` | T12 | ● | owner | decoy |
| 18-19 | gdrive/gsheets | drive_files/sheets_spreadsheets | `f_6b2c3d4e5f60718293a4b5` | K6/D1 | ● | owner | write target |
| 20 | gdrive/gsheets | drive_files/sheets_spreadsheets | `f_7c3d4e5f60718293a4b5c6` | C12 | ● | owner | connecting |
| 21-28 | linear | linear_issues | `ENG-2369`–`ENG-2375`, `DES-313` | K7/C2/C6/C9/C11/C12 | ● | unscoped | evidence |
| 29-39 | linear | linear_comments | `cmt_eng2369_1` … `cmt_des313_1` | cohort | ● | unscoped | per-record evidence |
| 40-43 | github | pr_comments/timeline | `harmonygames-Games/GameOfDominoes#1755#c_9`, `#1838#c_4` | T5/C10 | ● | unscoped | overturning |
| 44-48 | trello | trello_cards | `68daad004f5e6d7a8b9c0d10`, `68d672304f5e6d7a8b9c0d11`, `68d6735c4f5e6d7a8b9c0d12`, `680222a04f5e6d7a8b9c0d13` | H1/H2/T6 | ● | unscoped | authority/decoy |
| 49 | trello | trello_actions | `680222a04f5e6d7a8b9c0e13` | T6 | ● | unscoped | connecting |
| 50-54 | confluence | pages/versions | `page_release_status_definitions`, `page_external_messaging_guide`, `page_q4_product_narrative`, `page_q4_claims_conflict_format`, `page_q4_product_claims` | T2/T3/H3/K8/D3 | ● | unscoped | authority/decoy/write target |

## Findability

| Record | Likely query | Term present | Competing hits | Chain position |
|---|---|---|---|---|
| H1 `trello:68daad004f5e6d7a8b9c0d10` | `trello search "live-claim standard"` | "Q4 live-claim standard" card | other Q4 cards; the card is first by name | first link |
| H2 `trello:68d672304f5e6d7a8b9c0d11` | `trello search "external wording"` | "External wording - product claims" | HG decoy `68d6735c4f5e6d7a8b9c0d12` | first link |
| H3 `gmail:julia.lawson@harmonygames.co/1860000000000000001` | `gmail search "player-facing"` | subject "Q4 pack - Domino Delights only" | one thread | first link |
| T5 `github:harmonygames-Games/GameOfDominoes#1755` | `github list PR comments #1755` | comment body "default remains false" | base PR comments | overturning |
| T8 `slack:C1CB3D58E38B/1759255200.000200` | `slack thread C1CB3D58E38B 1759248600.000100` | reply "Two corrections" | none | overturning |
| T13 `trello:67ec1f6021f4291d45f9c21e` | `trello search "Collectibles"` | card "Collectibles (1 month)" | October list | boundary |
| D3 `confluence:page_q4_product_claims` | `confluence search "Q4 Product Claims"` | page title | four decoy pages | write target |

## Self-validation

| QC category | Tool-enforced | Manual evidence |
|---|---|---|
| Missing Universe Data | sql_lint, base_check | every record resolves; Julia owns the drive/sheets/gmail records |
| Temporal Field | sql_lint, base_check | all seeded dates ≤ 2025-09-30; GCal start < end; Linear comments after issues; no record cites a later record |
| Cross-service Referential | base_check | people, channels, issues, cards, pages and event copies resolve; the H1 card is cited by A1 and K3 |
| Quantitative / Reconciliation | sql_lint, base_check | reply counters 1/1; Trello badges comments=1; level manifest 4755+245=5000 |
| State / Lifecycle | base_check | comments after Done are neutral config notes (warning dispositioned); no state changed by a comment |
| Identifier / Format | sql_lint | all minted ids match the base schemes; no second naming scheme |
| Semantic / Category | manual | the claims are labelled by feature; "Season Pass" is a feature, not a document; the H1 card is a standard, not a spec |
| Other | manual | voice bands match conventions; no record states a classification |

## Integrations and companions

| Service | INT id | Companion decision |
|---|---|---|
| slack | INT-06, INT-22 | no Jenkins post and no Slack e-mail notification for the claims thread; human posts only |
| gmail | INT-11 | the GCal review event seeds invitation mails in Julia, Leonard and Brian mailboxes; the scope note exists in Julia's INBOX and Leonard's SENT, one RFC Message-ID |
| gcal | INT-11 | three attendee copies with self:true on each owner and one ical_uid |
| github | INT-01, INT-02, INT-03 | the two seeded PR comments have Slack app mirrors in #engineering-bots; no linear[bot] comment because the PRs predate the mention |
| linear | INT-05 | no Linear e-mail digest; issues and comments are complete |
| trello | INT-21 | Trello has no Slack integration in this universe; no companion |
| confluence | none | Confluence has no integration source in `integrations.json`; no companion |
| gdrive | INT-13 | no share DM; the files carry their sharing lists |
| gdocs | INT-13 | no share DM |
| gsheets | INT-13 | no share DM |
| snowflake | INT-18 | no Metabase chart; the task reads the tables directly |

## Touched-data census and coherence hazards

Scope: the claims draft and its September copy, the register workbook and Old register, the 13 claims, the Linear comments and issues, the two PR threads, the H1/H2/H3 cards/pages/thread, the review event and invitations, the GDD and the live-ops page, and the level manifest. Walked against `Task_Authoring/references/universe_kb/coherence_hazards.json`.

| Category | Hazard id | Records in scope | Disposition |
|---|---|---|---|
| temporal | T04 | `linear:ENG-2136`, `github:harmonygames-Games/GameOfDominoes#1755`, `gdocs:f_c57724584820a26f3bbe54` | no ticket/PR pair in scope is out of order; the readiness doc postdates the merge and is a dated claim |
| semantic | S08 | `confluence:page_q4_claims_conflict_format`, `page_external_messaging_guide`, `page_release_status_definitions` | the pages are deliberately same-purpose, different scope (team); the authority wins on issuer and scope; this is the designed decoy, not a contradiction |
| cross-service referential | none in scope: no base Slack citation of a missing Linear key is touched | no base Slack citations of missing Linear keys are touched; the new ENG keys (2373/2374/2369/2371/2372) are created by the SQL | R01 avoided by construction |
| quantitative | none in scope: reply counters and badges are consistent | reply counters are 1/1/latest; Trello badges comments=1; the level manifest sums 4755+245 | no counter mismatch |
| state/lifecycle | none in scope: no state field is changed by a comment | `linear:ENG-2136` Done + PR merged; comments are neutral config notes | the base_check warning is dispositioned below |
| identifier/format | I03 | `gmail:julia.lawson@harmonygames.co/1860000000000000001` | the `jlawson@` export alias is the mailbox filename; the row user_email is Julia |
| other | none in scope: no silent field contradiction | no silent system-field contradiction; both designed disagreements are dated text claims | the conflict column records both sources |

**Explicit category lines.** temporal: T04. semantic: S08. cross-service referential: none in scope. quantitative: none in scope. state/lifecycle: none in scope. identifier/format: I03. other: none in scope.

**Base_check warning disposition (Closed with later activity).** Four comments sit on base issues that were already Done: `ENG-1385`, `ENG-1874`, `ENG-2136`, `ENG-2323`. Each is a neutral production-config note, not a status change; the issue remains Done and the comment does not promise a reopen. The QC appendix permits neutral notes. No state field is changed. The seven seeded tickets carry their comments before their own completion, so they raise no warning.

**Sql_lint warning dispositions.** warn: confluence statement — unscoped and rarely opened — disposition: Confluence is unscoped per the ACL; the H1/H2/H3 homes are named by role in A1 and the decoys are reached by the same search terms; the pages are not load-bearing without a pointer. warn: weekend business message — disposition: engineering config comments and GitHub mirrors on 2025-09-28 are release-weekend activity; the mirror follows the PR comment time by design.

Nine weekend timestamps: the engineering config comments and the GitHub mirrors are release-weekend activity on 2025-09-28; the mirror time follows the PR comment time by design. Ten Confluence unscoped warnings: Confluence is unscoped per the ACL; the H1/H2/H3 homes are named by role in A1 and the decoys are reached by the same search terms; the pages are not load-bearing without a pointer.

## Intended disagreements

| # | Disagreement | Why realistic | Resolver |
|---|---|---|---|
| 1 | C06 claims "Season Pass is live"; the readiness P0 removes it from the out-of-moves screen; the config comment says the flag is default-off with no SKU | a feature can be code-complete and never enabled; launch readiness often pulls a surface late | H1 (100% enablement + production surface); the config comment is the later record; the conflict column states both |
| 2 | C13 claims 14 April; the readiness doc says 23 April; the GDD says US 11 April and worldwide 6 May | launch dates are repeatedly restated in different documents | H3 fixes the GDD dates; the conflict column reports all values; the claims draft's 14 April is unsupported |

## Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Leonard's Q4 claims note | `slack:C1CB3D58E38B/1759248600.000100` |
| A2 | my Q4 claims draft | `gdrive:f_5a1b2c3d4e5f60718293a4` |

Must never be named: the authority locations (Trello card, Gmail thread, calendar event), the ticket/PR ids, the number of live claims, the classification of C06/C07/C10/C11, the counts, the root cause, or the register contents. The prompt may name the deliverables (register, summary counts, corrected page, follow-up ticket) and the deadline.

## Facts for the human

| Locator | Base/seeded | Fact | Reach | Role | Re-verify |
|---|---|---|---|---|---|
| `gdocs:f_5a1b2c3d4e5f60718293a4` | seeded | 13 numbered claims, all marked live in the header | Julia owner | claim set met first | no |
| `gdocs:f_5a1b2c3d4e5f60718293a5` | seeded | 9-claim September copy | Julia owner | decoy | no |
| `gsheets:f_6b2c3d4e5f60718293a4b5` | seeded | Register tab headers; Old register 9 rows | Julia owner | write target | no |
| `gsheets:f_7c3d4e5f60718293a4b5c6` | seeded | level manifest 4755 active, 245 planned | Julia owner | evidence | no |
| `trello:68daad004f5e6d7a8b9c0d10` | seeded | live-claim standard | unscoped | H1 authority | no |
| `trello:68d672304f5e6d7a8b9c0d11` | seeded | external wording rules | unscoped | H2 authority | no |
| `trello:68d6735c4f5e6d7a8b9c0d12` | seeded | Engineering release wording decoy | unscoped | decoy | no |
| `trello:680222a04f5e6d7a8b9c0d13` | seeded | April five-bundle card | unscoped | superseded claim | no |
| `trello:67ec1f6021f4291d45f9c21e` | base | Collectibles card, no build | unscoped | boundary | no |
| `gmail:julia.lawson@harmonygames.co/1860000000000000001` | seeded | player-facing scope and GDD dates | Julia INBOX | H3 authority | no |
| `gcal:evt_5c1a7e93b2d04f61a8e7b8` | seeded | review meeting 2025-09-29 | Julia own copy | meeting record | no |
| `linear:ENG-2136` | base | Season Pass Done 2025-05-05 | unscoped | claim C06 | no |
| `linear:ENG-2323` | base | Hero Offers Done 2025-05-13 | unscoped | claim C10 | no |
| `linear:ENG-1385` / `ENG-1874` / `ENG-2136` / `ENG-2323` | base | Win & Collect, leaderboards, Season Pass, Hero Offers | unscoped | claims C02, C03, C06, C10 | no |
| `linear:ENG-2369`–`ENG-2375` | seeded | quest schedule, live-ops engine, SKU list, ads, River Rush, event cadence, claims review | unscoped | evidence / K7 | no |
| `linear:DES-313` | seeded | level manifest ticket | unscoped | evidence | no |
| `github:harmonygames-Games/GameOfDominoes#1755` | base | Season Pass merged 2025-03-29 | unscoped | overturning | no |
| `github:harmonygames-Games/GameOfDominoes#1838` | base | Hero Offers merged 2025-05-08 | unscoped | overturning | no |
| `gdocs:f_c57724584820a26f3bbe54` | base | readiness P0 and global release date | Julia shared | overturning | no |
| `confluence:page_domino_gdd` | base | soft launch 11 April; worldwide 6 May; ~4,755 levels | unscoped | evidence | no |
| `confluence:page_live_ops_engine` | base | internal live-ops engine | unscoped | C11 scope evidence | no |
| `confluence:page_q4_product_claims` | seeded | "All 13 product claims are live" | unscoped | page to correct | no |

**Platform-review corrections applied.** C05 now cites EVT-0525 (Axe Arena, 2025-09-28) and EVT-0526 (Streak Fever, 2025-09-28); the comment and ENG-2374 are dated 2025-09-29T17:10Z. C04 cites EVT-0531 on the seeded ENG-2373, dated 2025-09-30T10:30Z. The September list status date is 12 September; the claims page is dated 2025-09-29T10:00Z.

**Round-2 review corrections applied (report 6adfee3e, on the pre-fix hash).** F1: `"references"` and the Trello camelCase/`"desc"` identifiers are quoted in all ten affected statements (five Gmail messages, four cards, one action). F2/F6: the event-cadence and River Rush facts cite real warehouse runs (EVT-0525/EVT-0526, EVT-0531) and are dated after those runs. F3: the live-claim standard card `68daad004f5e6d7a8b9c0d10` is created at 2025-09-29T16:00Z, after the review ended, and the event description is an agenda line with no pointer claim. F4: the claims page and its version are dated 2025-09-29T10:00Z. F5: the September list reports 12 September. V4: the seeded tickets run ENG-2369 to ENG-2375 in creation order. V5: C01 and C04 no longer sit on issues archived before the freeze (ENG-645, ENG-2065); the remaining commented base issues are live at the freeze (ENG-2136 archives on 2025-11-06). V8: the Old register holds the nine September claims. V10: the scope note has a SENT copy in Leonard's mailbox, dated 2025-09-30T14:05Z, the morning of the request.

## Fact sheet

Manifest facts: `claim count = 13` (`gdocs:f_5a1b2c3d4e5f60718293a4`); `level manifest active = 4755` (`gsheets:f_7c3d4e5f60718293a4b5c6`).

```
FACT CHECK: PASS — 62 text-bearing rows, 2 declared facts, 3 declared superseded records
Errors: none
```

## Platform follow-ups

- The GCal event description is an agenda line only (it makes no pointer claim, so it cannot refer to a card created after the meeting); the H1 standard lives on a Trello card description (●). No load-bearing fact depends on gcal `description`.
- The two seeded PR comments have Slack app mirrors; the mirror attachment text matches the GitHub body. Confirm the mirror renders in the first trajectory.
- Confluence and Snowflake figures are unscoped; the GDD and level manifest were re-read at the freeze. Re-verify after any data regeneration.
- No ○ carrier holds a load-bearing fact: GCal description is a pointer, Slides/Contacts/Drive content_text/Slack file content are unused.

## Self-review

| Category / test | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |
|---|---|---|---|
| temporal | The readiness doc says 23 April, the GDD says 11 April / 6 May, the claim says 14 April; a run could pick any | `gdocs:f_c57724584820a26f3bbe54`, `confluence:page_domino_gdd`; H3 fixes the GDD dates; the conflict column reports all | PASS (designed) |
| semantic | The "live-ops engine" is a real live system, so C11 could be kept | `confluence:page_live_ops_engine`; H3 limits the pack to player-facing claims; C11 is out of scope | PASS |
| cross-service referential | The claims draft cites `ENG-2136` and `#1755`, which could point to a different issue/PR | `linear:ENG-2136` title "Season Pass"; `github:harmonygames-Games/GameOfDominoes#1755` title "Season Pass"; both match | PASS |
| quantitative | "Five coin bundles" in the April card could be right if one SKU was delisted | `snowflake.IAP_TRANSACTIONS` lists four coin SKUs; `linear:ENG-2371` comment lists the same four; no fifth | PASS |
| state/lifecycle | Four base-issue comments after Done look like reopened work | the comments are neutral config notes; the issues remain Done; no state field changes | PASS (warning dispositioned) |
| identifier/format | `jlawson@` thread filename looks like another mailbox | `gmail:julia.lawson@harmonygames.co/1860000000000000001` is Julia's thread; `user_email` is Julia | PASS |
| other | The register and the summary could disagree | both read the solver truth; the summary counts come from the same rows | PASS |
| Checks A–C walk | Check A/B/C could find an unlisted insert or a broken reference | inventory: 69 INSERT + 6 UPDATE; A/B/C PASS in `base_check`; no generated columns written | PASS |
| touched-data census | A pre-existing inconsistency in the touched data could fail coherence | the census lists T04, S08, I03 and "none in scope" for R/Q/L; every row dispositioned | PASS |
| C06 status | A run may think the merged PR is enough | `linear:ENG-2136` comment: flag default-off, no SKU, no run; H1 excludes merge state | NOT_LIVE |
| C10 status | A run may think the offers are live | `linear:ENG-2323` comment: 10% cohort; the 48-hour rotation is the enabled behaviour; H1 says a positive subset is testing | TESTING |
| C11 scope | A run may keep a live internal tool | `confluence:page_live_ops_engine`; H3 says player-facing only | OUT_OF_SCOPE |
| C13 date | A run may use the readiness 23 April | H3 names the GDD; `confluence:page_domino_gdd` gives 11 April and 6 May; the conflict column reports the rest | QUALIFY |

### Tool outputs (verbatim)

```
slack 7 · gmail 10 · gcal 3 · gdrive 4 · gdocs 2 · gsheets 5 · linear 23 · github 6 · trello 5 · confluence 10 · total rows 75
errors: 0  warnings: 18
```

```
BASE CHECK (/injection A + C, static): PASS  — 69 inserts, 6 updates
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
Warnings (1):
  line 145: linear.linear_comments: 4 comment(s) dated after their issue closed — neutral config notes, dispositioned above
```

```
HARDNESS GATE (normal): PASS
  [ok] assignment_context · effective_profile · sql_lint_clean · base_consistency · services_injected (10) · rows (69)
  [ok] services_carrying_weight (11) · anchors (2) · ask_fragments (7) · incorporation_chains · requirement_coverage
  [ok] authority_incorporation · cohort_size (13) · evidence_surfaces (2) · surface_requirements · per_record_calls (25)
  [ok] call_budget (67) · traps (14/9) · supersession (2) · distractors (4) · chains (5) · mechanism_portfolio (7)
  [ok] hidden_authorities (3) · decoy_scope · rarely_opened_evidence · facts · writes (4)
```

```
FACT CHECK: PASS — 62 text-bearing rows, 2 declared facts, 3 declared superseded records
Errors: none
```

**Unresolved:** none. The only advisory items are the UNPARAMETERIZED forecast channels (declared and disclosed in `01c_Forecast.json`) and the three platform follow-ups above.

```
STAGE GATE injection: PASS — Task_Authoring/task_inputs · 01_Universe_Inject.sql#bc3abbdfb1d8 · 01_Hardness_Manifest.json#cc9e8fdd561f · 01_Grounding_Dossier.md#3a92d7fdeb22 · solver/solver.py#880e65cd119b · 01c_Dispositions.json#7d660f2eb68c · 01c_Preflight_Report.json#52985489dbc4 · 00_Assigments.md#f8550b78dd9d · 01_Scenario_Design.md#5aefb2d5ce41 · 01_Hardness_Manifest.draft.json#81b53550b53a · 01_Gradable_Surface.json#ed7f0476e12c · __context__#fee9c0ab9e8c · __assignment__#3f9540413be0 · __policy__#dc4ab5df3cdd · __gate_policy__#bf8e231eb5d9 · __review__#0519e1000740 · blocking 0 · warnings 0 · checks 37
[PASS] assignment.v3_context: Julia Lawson / Product Manager; hard cap <70%; freeze 2025-10-01T00:00:00Z; shared source available; record dates and freeze-state evidence checked separately
[PASS] structure.outputs: 6 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md, solver/solver.py, 01c_Dispositions.json, 01c_Preflight_Report.json
[PASS] structure.inputs: 4 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#5aefb2d5ce41, 01_Hardness_Manifest.draft.json#81b53550b53a, 01_Gradable_Surface.json#ed7f0476e12c, 00_Assigments.md#f8550b78dd9d, __context__#fee9c0ab9e8c, __assignment__#3f9540413be0, __policy__#dc4ab5df3cdd, __gate_policy__#bf8e231eb5d9, __review__#73fa568faaa0)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 14/14 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 7/7 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 8/8 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 18/18 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 22/22 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 18, rows 75
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (weekend×8, confluence statement — unscoped and rare×10)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 39 draft ids
[PASS] structure.preflight: 01c_Preflight_Report.json bound by sha256 to the current SQL, solver, surface, manifest and dispositions
[PASS] solver.contract: solver contract re-run PASS
[PASS] mutation.dispositions: 34 mutation and intervention results each carry a written disposition (01c_Dispositions.json)
[PASS] geometry.upper_bound: U 0.851 (86/101) vs 1 - cap 0.30 (V3 hard): UNVERIFIED (bound PASS); re-run U 0.851 UNVERIFIED (bound PASS)
[PASS] geometry.margin: L_max 0.4752475247524752 vs (1 - cap) + 0.10: OK (advisory: the margin is a judgment, not a proof)
[PASS] liveness.dispositions: every liveness flag dispositioned (11 flag(s))
[PASS] forecast.preregistered: forecast hev_7aa2091757a26297 pre-registered in the ledger (UNCALIBRATED)
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 8 scoped load-bearing ids YES for julia_lawson
[PASS] structure.facts_declared: manifest declares 2 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 4 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 7 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (10 INT ids, services ['confluence', 'gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 4 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 10 evidenced counter-readings (of 13 found; need ≥ 9) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```













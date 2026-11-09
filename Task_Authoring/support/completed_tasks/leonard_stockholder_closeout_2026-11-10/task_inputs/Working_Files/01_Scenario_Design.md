# Scenario Design — leonard_stockholder_closeout · design only · contains no prompt, OE or criterion text

Leonard Hayes · Executive · Finance · Authoring · Long Horizon · medium (platform cap < 85 %; requester aim under 70 %, 62 % a stretch) · Feb 14, 2026 (normal). Written 2026-11-07 by `/create-scenario` (Claude Opus 5.5) from `plan/build_scenario.py` and `plan/assemble_design.py`. Research: `research/s1_signed_pdfs.md`, `s2_option_notice_state.md`, `s3_coherence_audit.md`, `s4_carrier_formats.md`; census in `00_PreScenario/census/`.

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe | key `normal`, label Feb 14, 2026 (normal), `Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)`, seed bound `freeze_utc` 2026-02-14T00:00:00Z, `shutdown_rules_apply` true |
| Assignment | Executive · Leonard Hayes (Role: Co-founder & Creative Director, leonard.hayes@harmonygames.co) · Finance · Authoring · long-horizon · medium · February 14, 2026 00:00 |
| Evals category | Executive (Founders / Exec / Strategy): a founder's investor close-out, cap table and audit confirmation, inside Finance |
| Loss budget | V3 Medium cap < 85 %, design target E[avg] <= 77 % (cap - 8). Requester aim, recorded verbatim: 'assignemt is medium but we have to target hard difficulty'; then 'go with your recommendations on all six' (aim under 70 %, 62 % a stretch). The assignment value is unchanged |
| Effective profile | `horizon: Long Horizon` -> `effective_profile: extreme`, with requester-confirmed `volume_exception {call_budget_floor 130, per_record_floor 85}` and `cohort_exception {cohort_floor 26}` (§2, §9) |
| Theme screen | holders and money; no bio-adjacent theme in the storyline. Seeded text says ZM |
| Source | task_context.py --require-source: ready, KB bound, context_hash 0f9314599d48…; last tools commit c16c7a1 |
| Role note | every signed record shows Leonard as CEO; the roster says Creative Director. The assigned role stands and the prompt will state no title. Persona_Briefs: the primary operator who owns the financial model and runway narrative |

Remit, before-freeze sources: his promise D04UC0UEN2V/1770665186.368229; his list C0ADGSZKR3R/1770934638.035469; the draft C0ADGSZKR3R/1770664700.848759; Task List row in `f_31115ddb6ed866f2b10d60`; his KPMG replies leonard.hayes@harmonygames.co/1817557789846606177.

Persona reach census (`persona_view.py reach leonard_hayes --top 12`), verbatim:

```
REACH  Leonard Hayes <leonard.hayes@harmonygames.co>  Co-founder & Creative Director / Executive
clock 2026-02-14

SLACK  user=EMPLOYEE_0038_SLACK_ID  visible channels=293 {'mpim': 110, 'private': 94, 'public': 38, 'im': 51}  messages=410569  public-not-member (UNVERIFIED)=32
  persona posts=143292 last post=2026-02-13  last activity in visible channels=2026-02-13
  C05433XK267    builds                                 public  mem=31  msgs=41107  2023-04-20..2026-02-12
  C04UTBZL6AX    founders                               private mem=7   msgs=40552  2023-03-20..2025-10-06
  C07C2866011    executives                             private mem=9   msgs=28266  2024-07-11..2026-02-13
  D04UP2L3E3S    D04UP2L3E3S                            im      mem=5   msgs=27517  2023-03-15..2026-02-12
  C05H8KVNU67    game-design                            private mem=27  msgs=22751  2023-07-16..2025-10-06 archived
  C050WGU41HR    engineering-bots                       private mem=35  msgs=20306  2023-03-29..2026-02-11
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16889  2023-10-07..2026-02-11
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16773  2025-01-09..2026-02-11
  C06FF10MMAM    [SOURCE_ORG_0001]-monkey               public  mem=6   msgs=15116  2024-01-22..2026-02-12
  C09UHHN6PFZ    prototype                              private mem=18  msgs=12172  2025-11-24..2026-02-12
  C04UEQVDVB7    admin_foundersonly                     private mem=7   msgs=11086  2023-03-17..2026-02-11
  D04UGG61DUM    D04UGG61DUM                            im      mem=5   msgs=11026  2023-03-20..2026-02-12

GMAIL  mailbox=leonard.hayes@harmonygames.co threads=17635 messages=22648 range=2023-03-15..2026-02-13
  threads by last-message month (recent): {'2025-09': 372, '2025-10': 571, '2025-11': 354, '2025-12': 399, '2026-01': 656, '2026-02': 335}
  top correspondents: SVC_0107_EMAIL (6157), SVC_4131_EMAIL (2273), robert@harmonygames.co (1990), arthur.blake@harmonygames.co (1533), benjamin.clark@harmonygames.co (618), SVC_2398_EMAIL (550), SVC_0325_EMAIL (490), frederick.stone@harmonygames.co (479), julia.lawson@harmonygames.co (417), SVC_0143_EMAIL (362), SVC_4249_EMAIL (330), SVC_1302_EMAIL (290)

GCAL  own=['leonard.hayes@harmonygames.co'] shared=[] events=1512 (distinct ical_uid 823, cancelled 159)
  last event before clock=2026-02-12T16:30:00Z  next after clock=None
  by month: 2023-03:11 2023-04:33 2023-05:37 2023-06:27 2023-07:28 2023-08:68 2023-09:45 2023-10:57 2023-11:42 2023-12:36 2024-01:67 2024-02:35 2024-03:28 2024-04:32 2024-05:44 2024-06:47 2024-07:63 2024-08:52 2024-09:95 2024-10:50 2024-11:48 2024-12:45 2025-01:65 2025-02:36 2025-03:23 2025-04:46 2025-05:68 2025-06:48 2025-07:45 2025-08:21 2025-09:38 2025-10:59 2025-11:32 2025-12:20 2026-01:17 2026-02:4

DRIVE  owned=817 {'application/vnd.google-apps.document': 201, 'application/json': 156, 'application/vnd.google-apps.spreadsheet': 141, 'application/pdf': 108, 'text/csv': 98, 'folder': 46, 'text/plain': 37, 'application/vnd.google-apps.presentation': 28, 'application/msword': 2}
  shared-with=413 {'application/pdf': 115, 'application/vnd.google-apps.document': 108, 'application/vnd.google-apps.presentation': 73, 'application/vnd.google-apps.spreadsheet': 51, 'text/plain': 41, 'application/json': 22, 'text/csv': 2, 'application/msword': 1}
  shared by owner: {'Resource: 7240535625619857401': 252, 'Resource: -6481757892984311338': 102, 'robert@harmonygames.co': 24, 'arthur.blake@harmonygames.co': 15, 'frederick.stone@harmonygames.co': 9, 'marcus.bennett@harmonygames.co': 3, 'thomas@harmonygames.co': 2, 'julia.lawson@harmonygames.co': 2, 'brian.foster@harmonygames.co': 2, 'calvin.price@harmonygames.co': 1, 'samuel.turner@harmonygames.co': 1}
  native visible: {'gdocs': 309, 'gsheets': 192, 'gslides': 101}  last modified visible=2026-02-11T23:22:39Z
  UNVERIFIED (domain/anyone, not owned/shared)=101 {'application/vnd.google-apps.document': 41, 'application/vnd.google-apps.spreadsheet': 32, 'application/json': 11, 'application/pdf': 9, 'application/vnd.google-apps.presentation': 8}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2026-02-13 (1d), slack_visible_channels=2026-02-13 (1d), gmail=2026-02-13 (1d), gcal_last_event_before_clock=2026-02-12 (2d), drive_last_modified_visible=2026-02-11 (3d)
```

## 1 Storyline

**The stockholder close-out.** Leonard owes the holders three things he has not done: the personal outreach he promised, the investor letter he drafted, and an honest holder picture for Sunset and for Griffin's auditors. His own records say parts of this are finished. They are not.

**Why it is real.** Nine stock lines have no record of being told. No live option holder has a last day in writing on any record Leonard can read (research/s2_option_notice_state.md section B). Six letters exist against eight Feb 12 Carta entries, so ES-14 and ES-18 have none, though C0ADGSZKR3R/1770841239.761999 says all were sent. ES-14 is Vincent Parker: he resigned in November, was never told of the closing, and his window ends Feb 21.

**Closed answer set.** 29 holders on Carta, 26 of them non-founders, tied exactly to 3,051,879, 762,880 and 268,772 (`verified_anchors.txt`, re-computed from raw records). The signed Schedule of Purchasers confirms every line (research/s1_signed_pdfs.md section D).

**Anchors per service.** Slack C0ADGSZKR3R/1770664700.848759, C0ADGSZKR3R/1770934638.035469; Gmail leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv>; Linear ENG-2438 to ENG-2463 in project ec2ea957-fc8e-4958-b809-0fb735b1e916; Docs `f_6a37227593d0977fdbdd7a`, `f_11040fe5d66821bd6951aa`; Sheets `f_31115ddb6ed866f2b10d60`; Drive d_601064334a0b493022fe83; Snowflake FINANCE_LEDGER financing rows (FIN-000041, FIN-000061).

**Universe KB placement** (`universe_kb/timeline.md`, cohorts.json, trap_catalog.json):

`timeline.md` rows have no ids, so each is cited by date with its evidence id. Spine rows that apply:

| Date | Row | Evidence ids | Use |
|---|---|---|---|
| 2025-07-16 | board/funding: Q3 board meeting | `gcal:evt_771fc850b4096bad7ea8b2`, `drive:f_7793bb93e59e9c0dee5129` | BOARD: Matthew attends after resigning |
| 2025-10-14 | board/funding: Q4 board meeting | `gcal:evt_4ee450f276f468e9ce95cf`, `drive:f_d03044b385b94f24b21ff4` | Deck sent to Tor Nov 4 |
| 2025-10-24 | layoffs | `gmail:leonard@harmonygames.co_1847333347700620793.json` | Four Oct leavers, lapsed rows |
| 2026-01-14 | board/funding: Q1 board meeting | `gcal:evt_8cdcb12b7b4e1346db999d` | Last board meeting |
| 2026-01-23 | funding: recap proposed | `gmail:leonard@harmonygames.co_1855133803855213163.json`, `drive:f_11040fe5d66821bd6951aa` | Term sheet snapshot, Jan 22 |
| 2026-02-09 | wind-down: shutdown decided | `slack:C0ADGSZKR3R:1770663250.160009` | Draft and promise |
| 2026-02-11 | wind-down: letters, Sunset call, Gemini notes | `gmail:leonard@harmonygames.co_1856860994291529096.json`, `gcal:evt_212e50fb5a53ea8016ce29` | Option holders told |
| 2026-02-12 | wind-down: Sunset signed | `slack:C0ADGSZKR3R:1770931777.561519` | Seeds follow this |

Storyline beats:
- `fundraising-finance-legal-harmonygames-builds-its-advisor-equity-program-v` b06 (2024-02-07): ADV. · research/s3_coherence_audit.md line 813
- `fundraising-finance-legal-harmonygames--quarterly-board-cadence-and-invest` b03 (2024-04-12), b05 (2024-09-04): investor reporting, BOARD. · research/s3_coherence_audit.md line 814
- `fundraising-finance-legal-2025-fundraising--the-crownfall-crypto-pivot-and` b04, b05, b06: only as background to the angels' last contact. · research/s3_coherence_audit.md line 815

Beats are orientation only. The prelude's "$3M Series Seed at $10M post" agrees with the price: $10,000,000 ÷ 10,172,940 = $0.983.

**cohorts.json: no fit — the cohort is 26 non-founder holders on Carta records, and no cohort id selects cap-table holders.** Nearest ids, none usable as the spine:
- `SF-LEDGER`: 704 ledger rows, 11 financing, one query returns all. Support only. · research/s3_coherence_audit.md line 820
- `DOC-harmony`: 91 docs by title family, the charter, IRA and side letter copies among them. Support only. · research/s3_coherence_audit.md line 821
- `TR-d93197`: Trello Done list, holds `/cards/801`. Its `hazards_inside` are incomplete checklists (L12 family, 4 cards) and actions later than `dateLastActivity` (T06 family, 5 cards); `/cards/801` is in neither. Not used. · research/s3_coherence_audit.md line 822

`hazards_inside`: none to drop, because no cohort id is taken.

**trap_catalog.json ids:**
| Id | Applies to |
|---|---|
| D02 | Docs with identical bodies. `f_b0e408e1d051cec9dc7183` is listed, so the charter copies are a catalogued trap |
| D01 | Same title under different owners: Arthur's and Leonard's charter, SPA and IRA copies · research/s3_coherence_audit.md line 830 |
| D05 | Version markers: "draft 28 August", "(final).pdf" · research/s3_coherence_audit.md line 831 |
| D03 | BoD deck family: `Harmony Games BoD Oct 14 2025` · research/s3_coherence_audit.md line 832 |
| C04 | Human claim against record: LIST "adds to 100%", letter 34,409, DD 0.038 %, "bod members" · research/s3_coherence_audit.md line 833 |
| P01 | Shared first names: Marcus, Claire, Martin · research/s3_coherence_audit.md line 834 |
| P02 | Shared surnames: Baker, Bennett, Brooks, Price · research/s3_coherence_audit.md line 835 |
| X01 | Redaction tokens across services · research/s3_coherence_audit.md line 836 |
| X02 | EMPLOYEE_0032 and `PERSON_3083_NAME` · research/s3_coherence_audit.md line 837 |
| X04 | Uneven masks between copies of one mail · research/s3_coherence_audit.md line 838 |
| D07 | Trello stale against reality: `/cards/801` · research/s3_coherence_audit.md line 839 |

## 1a Coherence audit

Source: `coherence_hazards.json` walked in full, the seven QC categories, the sibling sweep and every NB card; `research/s3_coherence_audit.md` is the working record. This audit ran before the PDF read, so corrections come first.

**Corrections since the audit** (research/s1_signed_pdfs.md; all read from the signed PDFs under decision 6):

| Audit said | Now | Evidence |
|---|---|---|
| Segerstrale's route rests on an unread PDF; the party may be Menlo capital LLC | He is a full party in his own name and signed | leonard.hayes@harmonygames.co/1777587701740700050, research/s1_signed_pdfs.md section B |
| Every clause is a draft | The filed charter and final-form IRA and Voting match the drafts on every clause used here | `f_90c029015fc474199cf736`, research/s1_signed_pdfs.md section D |
| §1a table says NB-32 is not touched | ENG-2454 is Douglas: touched, and H1's Carta rule settles it; his end date is never graded | leonard.hayes@harmonygames.co/1847333395311994879 |
| Hazard S06 cites /contacts/170 and /108, /139 | Dead pointers from the hazard file; the real rows are /169 (Leonard) and /138 (Frederick) | research/sweeps/coherence_sweep.md line 195 |
| Tor 'no contact since May 2024', Nebojsa Sep 2025 | Tor Nov 4, 2025, D09R59580EM/1762285888.654689; Nebojsa Oct 24, 2025 in C7442B7CD94B | research/sweeps/coherence_sweep.md line 89 |
| Sunset's fee quoted three ways | $12,363 in the signed set; no row grades it | leonard.hayes@harmonygames.co/1856956483320787350, hazard Q07 excluded |
| Pro rata dropped | Clause 3 keeps a right of first offer for both side letter investors; off the graded path | leonard.hayes@harmonygames.co/1777587701740700050 |

Source: `by_universe/normal/coherence_hazards.json`, all 68 ids. Scope here is the list in the job, plus the records a correct run reaches from it (`D09R59580EM`, `f_414596b0a9d698267dd1e1`, the Carta consent notices).

Terms used in the resolution column:
- **excluded**: per the playbook, the hazard's records are neither modified by the SQL nor cited by the design. · research/s3_coherence_audit.md line 46
- **dated_claim**: an attributed, dated text claim that a later named record overturns. · research/s3_coherence_audit.md line 47
- **repaired**: not used. No L01–L07 record is in scope. · research/s3_coherence_audit.md line 48
- **class-touch**: the record belongs to the hazard's class and the design will cite it, but it is not in the hazard's example list. No verified resolution fits by meaning. Writing `excluded` would pass the gate and still be untrue, so write no acknowledgement and handle it by the stated rule. The category is not L or R, so the gate needs none. · research/s3_coherence_audit.md line 49

Token test, run with `base_check.hazard_index()` and `id_tokens()` over about 55 scope ids: the only hit is `f_0c37bb7235683d73569903` (S07, Q07). No scope id hits an L or R example token, so `hazard_scope` will not fire unless the manifest cites one. The L and R acknowledgements below are still needed, because the job and the QC standard are about presence, not the token test.

#### Temporal
| Id | Records | Why it touches | Resolution | Why safe |
|---|---|---|---|---|
| T02 | All 12 multi-message scope threads, e.g. `leonard@harmonygames.co_1856958794180374704.json`, `leonard@harmonygames.co_1817557789846606177.json`, `leonard@harmonygames.co_1775636449493308689.json` | Measured: every one is stored newest-first (`asc False, desc True`), so `[0]` is the latest message | class-touch | Each message's own date is correct and thread order is uniform. Rule: order by `date_parsed`, never by array index. Seeded replies are dated after their parent |

Checked, not touched: T03 (0 bad dates across 13 threads), T01, T04, T05, T06 (`/cards/801` is not an example; bump `dateLastActivity` only if a comment is ever seeded there), T07, T08.

#### Semantic
| Id | Records | Why it touches | Resolution | Why safe |
|---|---|---|---|---|
| S06 | Contacts `/contacts/170`, `/108`, `/139`. Text: LIST signature "CEO", `#winddown` idx 21, 42 | Leonard signs CEO; the assigned role is Creative Director | excluded | Do not cite those Contacts rows. The prompt states no title. The signatures are dated text and carry no graded fact · research/s3_coherence_audit.md line 63 |
| S07 | `f_0c37bb7235683d73569903` (Gemini notes, Feb 11) | "the entity name is Robert Incorporated". The doc also holds the only base sentence on "board and stockholder consents" | excluded, **only if the manifest does not cite this doc** | No entity-name row. See §3 D: this doc is tempting as a BOARD source. Citing it hits S07 and Q07 |
| S05 | `PAYROLL_ROSTER` EMPLOYEE_0032 | Tempts a run to name ES-16 "Josh Dempsey" | excluded | Key by ES id, never by roster name · research/s3_coherence_audit.md line 65 |
| S02, S03 | Seeded Linear rows only | Cross-team parents, label sprawl | excluded | No cross-team parent and no new sprint-style label on seeded issues · research/s3_coherence_audit.md line 66 |

Checked, not touched: S01, S04, S08.

#### Cross-service referential (acknowledgement needed)
| Id | Records | Why it touches | Resolution | Why safe |
|---|---|---|---|---|
| R04 | `#winddown` idx 22 (the hazard's own example, the folder link). Same class: `#admin_foundersonly` 2023-08 idx 504, 721, 856, "Harmony Games Cap Table" | Slack carries Google-native ids. The cap table sheet is **in no export**: gsheets "Cap Table" 0 hits, gdrive 0 hits, both scan_complete | excluded | Cite neither link. Name Drive files by title. Any seeded link uses a Google-native id with an exact title. A run that follows "our final cap table" hits a dead end, which is fair as long as no row needs that sheet · research/s3_coherence_audit.md line 73 |
| R08 | Any seeded GCal copy or invitation mail | Mail and calendars only partly agree (0.879) | excluded | No base invitation is cited. A seeded invitation mail gets its GCal rows (INT-11) |

Checked, not touched: R01 (seeded text must name no Linear key that does not exist), R02, R03, R05, R06, R07, R09.

#### Quantitative
| Id | Records | Why it touches | Resolution | Why safe |
|---|---|---|---|---|
| Q07 | Same family as the examples: `D04UC0UEN2V` idx 24 "$12K", `#winddown` idx 151 "$11700", Gemini notes | Sunset's fee, quoted three ways in records a run opens | excluded | No fee is graded. DM idx 1 is cited, idx 24 is not. Scope already keeps Sunset's fee out |
| Q05 | `FIN-000061` (-35,500, 2023-09-13) | 2023-09 burn 99,107 against ledger outflow 134,607. The gap of 35,500 is exactly this row | class-touch | Not a true conflict: a note repayment is not burn. Use the row only for "founders are not note creditors". Grade no burn figure · research/s3_coherence_audit.md line 82 |
| Q10 | LIST: `leonard@…_1816809274978043917` and `blake@…_1816806726955267951` | Same RFC message, different tokens | class-touch | Measured: all 27 share and percent pairs are identical across Leonard's copy, Arthur's copy and Slack idx 55. Only the name tokens differ. Key by figure and id · research/s3_coherence_audit.md line 83 |

Checked, not touched: Q01–Q04 (`#winddown` parent idx 158 has reply_count 1 and its reply idx 202; 0 raw-shaped rows in the four scope Slack files), Q06 (only if a letter quotes cash), Q08, Q09, Q11.

#### State / lifecycle (acknowledgement needed)
| Id | Records | Why it touches | Resolution | Why safe |
|---|---|---|---|---|
| L13 | Hazard examples are `Combo-Fighters#37` and `slack:C05KNDCHAAG:1770842137.835489` | The storyline sits on the shutdown. "Everything stopped on Feb 9" is false | excluded | Neither record is cited. The design's cut-off is the clock, and no row claims work stopped |
| L08 | Seeded Linear holder issues | 64 open base issues sit with quiet or departed assignees; a seeded issue could join them | excluded | Assign seeded issues only to Leonard, Robert or Arthur (`active_feb_2026`). Never assign a holder · research/s3_coherence_audit.md line 91 |
| L11, L12 | `/cards/801` is in neither list | Trello is a seeded service | excluded | Base cards stay untouched, and any new card goes in an open list · research/s3_coherence_audit.md line 92 |

Checked, not touched: L01–L07 (no base Linear issue is in scope; `repaired` is unused), L09, L10, L14.

#### Identifier / format
| Id | Records | Why it touches | Resolution | Why safe |
|---|---|---|---|---|
| I03 | All Leonard threads, stored as `leonard@harmonygames.co_<id>` with `user_email` `leonard.hayes@…` | Universe-wide alias | class-touch | Cite by thread id. The seeded thread file convention follows the mailbox · research/s3_coherence_audit.md line 99 |
| I04 | Leonard's mailbox uses RFC-2822 dates; `threads/00001958` etc. use ISO-Z | Mixed date formats inside the Carta consent sweep | class-touch | Parse `date_parsed`. A seed follows its own mailbox's format · research/s3_coherence_audit.md line 100 |
| I14 | `f_31115ddb6ed866f2b10d60` Task List, `f_105b20100113e6d6cccbf6` Termination Notices, folder `d_e5caf6a8c630421942ee59` | Owner is `Resource: 7240535625619857401` | class-touch | Both files are shared with Leonard, and persona_view says YES. The folder itself has empty sharing |
| I15 | `Due Diligence Disclosures.docx` against its Doc title; truncated titles (`…Amended and Restated Cert(1)`, `Reset Financing Term Sheet (Washout Recap + Pay-to`) | Drive name differs from Docs title | class-touch | Name files by the Docs title or id. Never grade a filename · research/s3_coherence_audit.md line 102 |
| I10 | Seeded Linear rows | Malformed ids such as `usr_Victor Barnes` | excluded | Use `usr_63fffeb4fab5233e` for Leonard |
| I11, I12, I13 | Base board meetings (§3 D) | Rows and copies can differ per calendar | excluded | Used for the audit only, kept out of the manifest. Count by `(ical_uid, start)` if ever needed · research/s3_coherence_audit.md line 104 |

Checked, not touched: I01 and I02 (0 raw-shaped, 0 id mismatches in the four scope Slack files), I05, I06 (0 in 13 threads), I07, I08, I09, I16, I17, I18 (no struck-through text in `#winddown` or the DM).

**QC seven-category walk.**

Format: record · category · fields · evidence pointer · hazard id · disposition (avoid / fold into design / designed claim + overturning record). Gmail ids are Leonard's threads and `[n]` is the message index. "LIST" is the owner list. All rows were re-read in this session except those marked lead.

**Temporal**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| `f_bc574824d936285e308cff` side letter copy | Title "draft 28 August(1)"; created 2023-06-29, modified 2023-07-25 | gdocs `/docs_documents/474` | none | **Avoid.** Cite `f_6201c7027d02997bfb2c84`, and never a Drive date on these files |
| `f_6201c7027d02997bfb2c84` | created 22:17:15Z is after modified 22:12:51Z, same day | gdocs `/docs_documents/238` | none | Avoid: no row on its timestamps |
| Carta ES-7, 12, 13, 18 against the Feb 11 letters | "as of Jan. 30, 2026" against "January 31, 2026" | `leonard@harmonygames.co_1856960351896429942.json`, `leonard@harmonygames.co_1856861323365646598.json` | none | **Avoid.** Grade "Last day to exercise" only, never an end date |
| ES-12 letter | "January 31, 2025" | `leonard@harmonygames.co_1856860994291529096.json` | NB-22 | Avoid: the Carta notice carries ES-12 |
| ES-17 exercise window | Carta "Jan. 28, 2026"; same-date leavers Jan 24; letter "window ends January 22, 2026" | `leonard@harmonygames.co_1847333272519888206.json`, `leonard@harmonygames.co_1847333318158821452.json`, `leonard@harmonygames.co_1847335165884050330.json` | none | **Designed claim + overturning record:** the letter says "Carta will show the exact numbers". All three dates precede the clock, so the state is unchanged. No row on the exact date |
| ES-14 | Terminated Nov 21, 2025; entered Feb 12, 2026; last day Feb 21, 2026 | `leonard@harmonygames.co_1856960478782792748.json` | none | Fold into design (ASOF) |
| KPMG as-of date | FY23 "as of December 31, 2023"; FY24 "as of September 30, 2024"; both under "year ended December 31" | `leonard@harmonygames.co_1788910618703813283.json`[0], `leonard@harmonygames.co_1817557789846606177.json`[2] | none | **Fold.** Both real bodies are boilerplate and the terms sit in an unread PDF. The seed must state its as-of date in the body, which is a departure from pattern |
| Tor wire | Value date Sep 21 [4], "didn't hit" Sep 22 [2], ledger Sep 21 | `leonard@harmonygames.co_1777052222643175480.json`, `FIN-000060` | none | Avoid wire dates |
| Investor draft | "runway of less than a month"; written Feb 9, before Feb 12's signing, resignation and Carta entries | `C0ADGSZKR3R` idx 7 | NB-3 | Fold: the deliverable rewrites it. No cash figure graded |

**Semantic**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| LIST | "Owners", "shares" for stock and options alike; Griffin one line | `leonard@harmonygames.co_1816809274978043917.json`[0] | none | Fold (ADV, OPT) |
| The "29 holders" cohort | 6 of the 14 option lines hold nothing at the clock; ES-2 is not on LIST | §3 B | none | **Fold, and close the rule.** See §0 item 6 · research/s3_coherence_audit.md line 129 |
| Contacts Matthew | job "Independent Director (investor/advisor, not an employee)", undated | `/contacts/159` | none | **Fold.** See §0 item 2 and §3 D. This is an undated system field, so it cannot be a dated claim. Reconciling it must be the stated job · research/s3_coherence_audit.md line 130 |
| Contacts Michelle, Thomas Baker | "General Counsel" against "My paralegal michelle" | `/contacts/142`, `/154`, `leonard@harmonygames.co_1777052222643175480.json`[19] | none | Avoid: no row on counsel titles |
| Contacts Patrick | "Business Development / Partnerships Manager" at `patrick@`; the same address is a Disli holder and Bergmann | `/contacts/144`, `leonard@harmonygames.co_1781310711617833275.json`[5], `leonard@harmonygames.co_1836075678772806708.json` | X02 family | Avoid: never grade an address. §6 |
| Solsten titles | "Arthur/Patrick - They are COO/CEO" against signature "CEO / Co-founder" | `leonard@harmonygames.co_1775636449493308689.json`[22], `leonard@harmonygames.co_1847629332615617366.json`[0] | none | Avoid titles for the Solsten pair |
| Due Diligence Disclosures | "intends to enter into advisory agreements", dated Jul 10, 2023. A statement of intent | gdocs `/docs_documents/262` | none | **Fold, with care.** It is the ADV overturning record, so cite it as "planned 103,764", and let the subtraction and the tie carry the proof · research/s3_coherence_audit.md line 134 |
| Update wording | "our first investor update" (May 2024) against an earlier board deck to Tor (Oct 17, 2023) | `leonard@harmonygames.co_1799418746420547240.json`[2], `C05TPHZA52P` 2023-10 idx 0 | none | Avoid "first" and "only": §3 |
| Gemini notes | "board consists of themselves and Griffin" | `f_0c37bb7235683d73569903` | S07, Q07 | Avoid citing |

**Cross-service referential**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| "Harmony Games Cap Table" | Slack link; no such sheet in the export | `C04UEQVDVB7` 2023-08 idx 504, 721, 856 | R04 | Avoid: no row needs it |
| Oct 31, 2023 closing mail | "Attached, please find a complete set" with `attachments=[]` on [6] | `leonard@harmonygames.co_1781310711617833275.json`[6] | none | Avoid: rely on the BCC list only. The closing binder is cited as an attachment of `leonard@harmonygames.co_1788910618703813283.json`[0], UNREAD |
| Carta cap table exports | Leonard sent KPMG "excel file that I generated from Carta" and "Cap tabled from Carta as of 12-17-2024". Metadata lists `att_0001.xlsx` on both, **but neither file is in the export** (`files`: no non-PDF attachment in either thread; 0 paths with the listed prefix) | `leonard@harmonygames.co_1788910618703813283.json`[0], `leonard@harmonygames.co_1817557789846606177.json`[2] | none | **Fold.** The authority exists in the story and cannot be opened. A run may say so. No shortcut, and no seed may contradict what it would show |
| Advisor agreements | Referred to by the DD table; visible to no persona | `f_c2c881ccc407fbdaeaa362` etc. (C2, lead) | none | Avoid citing them. ES-8 and ES-10 stay unnamed |
| Tokens across copies | `[PERSON_NAME_0801]` in Slack and `PERSON_1287_NAME` in mail for one line | Slack idx 55, Gmail [0] | X04 | Key by figure and id · research/s3_coherence_audit.md line 145 |
| Side letter, final text | "Side Letter TLAS(final).pdf" | `leonard@harmonygames.co_1777571840372992861.json`, `leonard@harmonygames.co_1777052222643175480.json`[7] | none | **UNREAD. See §0 item 7** |
| Side letter party | Segerstrale may be party through "Menlo capital LLC", new to the census; he invested personally | `leonard@harmonygames.co_1774541878774535160.json`[3], [2], [9] | none | **Fold:** grade "Segerstrale's side is a party", never the entity |
| Segerstrale dollars | "$100K", "giving up $25K" against $50,000 | `C04UM32UWKD` 2023-06 idx 492, 535; `D04UC0UEN2V` 2023-06 idx 59; LIST; DD | none | Designed claim + overturning record: Jun 2023 plans, overturned by 81,383 − 30,518 and the floor test |
| Tor's last contact | C2 says May 19, 2024. **Wrong:** Nov 4, 2025 Slack DM | `D09R59580EM` 2025-11 idx 0–2 | none | **Fold. See §0 item 1** |
| Nebojsa's last contact | C2 says Sep 15, 2025. Slack mpdm runs to Oct 24, 2025 | `C7442B7CD94B` 2025-10 | none | Correct the census; no row depends on it |
| Contacts coverage | No row for Sunset, KPMG, TLAS, Bergmann, Eren or the Griffin VP Finance | contacts search, 0 hits each, scan_complete | none | Fold: a Contacts seed must not imply these exist · research/s3_coherence_audit.md line 151 |

**Quantitative**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| LIST total | 27 lines sum to 94.129 % but say "adds to 100%" | Gmail [0], Slack idx 55 | none | **Designed claim + overturning record:** `f_414596b0a9d698267dd1e1` adds "Shares Available under 2023 Stock Plan - 5.874%", total 100.003 % |
| Fully diluted base | 10,172,940; 10,172,939; 10,069,176 (implied); 10,062,267. Griffin 27.278 %, 27.3 %, ~27.0 % | `f_a267353f7f351df0a2dc29` (no Leonard reach), `C07C2866011` 2026-01 idx 727, LIST, `C04UTBZL6AX` 2025-07 idx 5 | none | **Avoid.** Grade counts only |
| Option reserve | 1,017,294 against 1,121,058 | LIST base 6,000,000 + 3,051,882 + 1,017,294 = 10,069,176 exactly; idx 727 | none | **Avoid.** Both are internally consistent. $10M post ÷ 10,172,940 = $0.983, so the priced base puts advisors on top of the pool (reserve 1,121,058). LIST's base puts them inside it. No reserve row · research/s3_coherence_audit.md line 158 |
| Preferred count | 3,051,879 issued; 3,051,881 quoted; 3,051,882 designated | `f_11040fe5d66821bd6951aa`, idx 727, disclosure schedule | none | Fold: the 12-line sum settles 3,051,879 |
| ES-17 vested | Carta 34,439 against letter "34,409" | `leonard@harmonygames.co_1847333272519888206.json`, `leonard@harmonygames.co_1847335165884050330.json` | none | **Designed claim + overturning record:** only 34,439 ties to 54,529 |
| Claire Morgan | DD "0.038%" verbal against LIST 0.076 % (7,630), Carta ES-4 7,630 | gdocs `/262`, `leonard@harmonygames.co_1856960410709778333.json` | none | Designed claim + overturning record: Jul 2023 verbal, overturned by the Nov 2023 grant |
| Griffin dollars | $2,616,996.67 / $83,002.56 (SOP); $2,616,996.66 / $83,002.55 (Leonard to KPMG); $2,700,000 ledger | `leonard@harmonygames.co_1771880236343640719.json`, `leonard@harmonygames.co_1788910618703813283.json`[0], `FIN-000026` | none | **Avoid cents.** Grade shares |
| Angel ledger rows | Aug 200,000; Sep 50,000; Oct 50,000 against P&L Sep 75,000, Oct 25,000 (P&L: C2, lead). Rows of $25,600 and $24,400 match no holder | `FIN-000041` to `FIN-000078` | none | Avoid: only the $300,000 total is safe · research/s3_coherence_audit.md line 163 |
| Stakeholder count | "17 stakeholders" against 15 stock lines | `C04UEQVDVB7` 2023-08 idx 663 | none | Avoid |
| Seed price | Disclosure schedule "$1.0173" against $0.983 | `f_a267353f7f351df0a2dc29` (Leonard NO) | none | Out of reach; never cite |
| Term sheet options | 268,772 at Jan 22 against 159,706 at the clock | gdocs `/40`, 14 notices | none | Designed claim + overturning record · research/s3_coherence_audit.md line 166 |

**State / lifecycle**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| Trello "Existing Investor Update" | `closed:false`, list Done, moved there Nov 12, 2025; no sent record. **The analysis's "is closed" is wrong** | `/cards/801`, `/actions/5221`, `/5282` | none | Avoid: do not cite it. Correct the analysis · research/s3_coherence_audit.md line 171 |
| Task List | Every Status False, last modified Feb 10, though Helpshift was cancelled by Feb 11 | `/sheets_spreadsheets/76`, `C0ADGSZKR3R` idx 57 | I14 | Fold: cite only row 2 "Send email to investors", with idx 197 |
| Terminated yet active | Carta and letters end ES-4 and ES-15 at Dec 31, 2025; `activity.json` has Claire and Brian `active_feb_2026` (ES-15 = Brian is INFERENCE from the letter's "brian") | `leonard@harmonygames.co_1856960410709778333.json`, `leonard@harmonygames.co_1856861400116562076.json` | NB-1 family | Avoid: no row on who worked when |
| ES-16 exercise | Holder said they were trying to exercise; Leonard: "if you want to move forward we can surely figure it out". Notice shows 0 at Oct 29 | `leonard@harmonygames.co_1847333990408253969.json`[1], [0] | none | **Fold. See §0 item 5** |
| ES-9 after resignation | Matthew left the board May 1, 2025; no Carta termination | `leonard@harmonygames.co_1830959847543474636.json`, no notice in the census | none | **Fold:** the method record must state that an award with no termination stays live |
| Matthew's accounts | Confluence `is_active` False; Linear True; Slack `deleted` False | entity.py §6 | none | Avoid · research/s3_coherence_audit.md line 176 |
| Frederick on board invites | The Jan 14, 2026 invite lists him after his Oct 24 exit, `needsAction` (created Sep 17, 2025) | gcal `evt_8cdcb12b7b4e1346db999d` family | I13 | Avoid: stale invite, not attendance |
| Reset term sheet | Unsigned; no record supersedes it | `f_11040fe5d66821bd6951aa` | none | Fold: "proposed, never adopted" |

**Identifier / format**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| SSP-06, SSP-08, ES-8, ES-10 | Never named in any notice | C2 §2, digests | none | Never grade which is which · research/s3_coherence_audit.md line 183 |
| ES-1, 2, 5, 14, 15 names | Tokens only | Notices | NB-12 | Key by ES id. ES-12 is now named: `f_414596b0a9d698267dd1e1` "Owen Baker – 0.162%" |
| `PERSON_3083_NAME` | Solsten's Schaeppi, and also the signature on Arthur Blake's own mail | `leonard@harmonygames.co_1816809274978043917.json`[1] | X02 family | Avoid: §6 |
| Two addresses, one person | PERSON_3336 and PERSON_3335; PERSON_3935 and PERSON_3941 | §6 | none | Never grade an address · research/s3_coherence_audit.md line 186 |

**Other**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| `#winddown` idx 105–106 | A live-looking OAuth credential in plain text. Not reproduced here | `C0ADGSZKR3R` | none | Avoid quoting. No seed repeats it |
| `#winddown` idx 192 | "from [Phil]" is an image; idx 193–194 react to it | `C0ADGSZKR3R` | none | UNREAD. It sits right beside the board resignation, so do not build on it |

**Sibling-defect sweep.**

Method: literal sweeps over gdocs, gsheets, gdrive, contacts, confluence and Slack (`messages/*/*.json`), Leonard's mailbox, and all mailboxes for Carta board mail. Every zero below is `scan_complete`, with a positive control in the same request (for example `2,746,693` hits in the same Slack scan where `268,772` hits nothing).

**A. A stale option total (designed: term sheet 268,772)**
| Sibling | Value | Verdict | Action |
|---|---|---|---|
| Sum of grants | 334,284 (CALC, on no record) | Fair decoy | Keep · research/s3_coherence_audit.md line 201 |
| `C07C2866011` 2026-01 idx 727, 728 | Reserve 1,121,058 | **Actual conflict** with LIST's 1,017,294 base | No reserve row |
| `C04UTBZL6AX` 2025-07 idx 5 | FD 10,062,267, "Other investors & advisors ~1,315,574" | Modelling text, not a record | Avoid |
| `f_414596b0a9d698267dd1e1` | 5.874 % available = 591,454 of 10,069,176 | **Fair, and useful.** New. Closes the LIST gap | Fold |
| `leonard@harmonygames.co_1847335165884050330.json` | 34,409 vested | **Actual typo,** self-disclaimed | Fold as a decoy; the row pins Carta |
| Disclosure schedule | Pool 1,017,294 + Advisors 103,764 = 10,172,940 | Out of Leonard's reach | Never cite · research/s3_coherence_audit.md line 206 |

`268,772` appears only on gdocs `/40`. It has 0 hits in Slack and gsheets.

**B. A merged line (designed: LIST)**
| Sibling | What is merged | Verdict | Action |
|---|---|---|---|
| Griffin line on LIST | Two funds in 2,746,693 | Fair: floor test 686,660 needs two | Keep · research/s3_coherence_audit.md line 213 |
| Four advisor lines | Stock + options: 86,470, 81,383, 31,536 ×2 | Fair (ADV) | Keep · research/s3_coherence_audit.md line 214 |
| `f_414596b0a9d698267dd1e1` | Same 27 lines, percent only | Fair; a third copy of LIST | **Add to the shortcut audit** |
| `FIN-000044` $75,000; `FIN-000042` $50,000 | Disli family; two angels | Ledger rows do not map to holders | Avoid · research/s3_coherence_audit.md line 216 |
| `D04UC0UEN2V` 2023-06 idx 59 | "(Libra) $75K", "(Solsten) $25K" | Jun 2023 plan; it sits in the same DM a run opens | Fair decoy |
| Term sheet "Series Seed (all non-founder investors)" | One line of 3,051,879 | Fair | Keep · research/s3_coherence_audit.md line 218 |
| Option-only lines on LIST | Lapsed and live alike; ES-2 absent | **The "29 holders" problem** | §0 item 6 · research/s3_coherence_audit.md line 219 |

**C. A draft read as signed (designed: the side letter)**
| Sibling | State | Verdict | Action |
|---|---|---|---|
| Both Drive side letters | Unsigned; Tor-only; lack the effective-on-funding change. They differ only in masks | Fair | Cite one id · research/s3_coherence_audit.md line 224 |
| Charter ×4 (Leonard) | Jun 21, 2023. Measured: differ only in masks and `[____]` blanks | Fair, but **no filed text exists** | State "draft" · research/s3_coherence_audit.md line 225 |
| IRA ×4 (Leonard) | Differ in masks, plus "all future employees" against "all current and future employees" | Real wording difference, off-path | Avoid that clause · research/s3_coherence_audit.md line 226 |
| SPA, Voting, ROFR copies | Same pattern (C2, lead) | Fair | Avoid · research/s3_coherence_audit.md line 227 |
| Reset term sheet, framework | "for discussion", unsigned | Fair | Keep as decoy · research/s3_coherence_audit.md line 228 |
| `#winddown` idx 7 | Unsent | **Designed** | Keep · research/s3_coherence_audit.md line 229 |
| `#winddown` idx 5 | Sent as `leonard@harmonygames.co_1856675475513544349.json`[13] | Fair: a draft that **was** sent, a good contrast | Keep |
| `#winddown` idx 24, 174, 175 | Vendor drafts, not checked for sending | Off-path | Avoid · research/s3_coherence_audit.md line 231 |
| LIST versions | `f_414596…` Nov 5, Slack idx 55 Nov 26 18:38Z, mail 18:47Z. Slack is the draft of the mail | Fair: same figures | Key to the mail · research/s3_coherence_audit.md line 232 |
| IRA notice clause | A copy to Orrick "if notice is given to Stockholders" | **Unflagged by census.** A rule built on the IRA drags this in | Avoid, or state it · research/s3_coherence_audit.md line 233 |

**D. An out-of-date board list (designed: Matthew still listed)**
| Sibling | What it shows | Verdict | Action |
|---|---|---|---|
| `/contacts/159` | "Independent Director", undated | **Actual stale system field** | §0 item 2 · research/s3_coherence_audit.md line 238 |
| SPA drafts | "shall be 4 … Matthew Collins, [0509], [0357], and" | Fair: "As of the Initial Closing" | Keep · research/s3_coherence_audit.md line 239 |
| `leonard@harmonygames.co_1775636449493308689.json`[22] | "he is on our board" (Aug 2023) | Fair, dated | Keep |
| Jul 16, 2025 GCal | Matthew `accepted`, after resigning | **Fair:** his own mail says "very happy to join the board meetings etc going forward". A strong trap, no defect | Fold · research/s3_coherence_audit.md line 241 |
| Oct 14, 2025 and Jan 14, 2026 GCal | No Matthew; Arthur and Frederick invited; Griffin on neither | Attendance list, not a board list | Avoid · research/s3_coherence_audit.md line 242 |
| `leonard@harmonygames.co_1808816811200364470.json` (Aug 30, 2024) | Consent to Phil, Matthew, Leonard, Robert | Fair | Keep |
| **`leonard@harmonygames.co_1838216168984971198.json` (Jul 21, 2025)** | Consent to **Phil, Leonard, Robert only** | **System-side overturning record, new.** Carta shows the exit | **Cite for BOARD** |
| `leonard@harmonygames.co_1782198867266535233.json` (Nov 10, 2023) | Also lists `michelle.carter@` | Consent recipients are not exactly directors | Do not define directors as recipients of this one |
| "added you as a board director", "sent you a Board Consent", "Board consent approved" | All mailboxes, subject search, scan_complete: hits only in Leonard's and Robert's mail, none in `blake@…` | **Arthur has no director record anywhere** | §0 item 3 · research/s3_coherence_audit.md line 246 |
| `#winddown` idx 25 | "we are personally liable as bod members" to `@here` | Loose human claim | Designed claim + overturning record, or avoid · research/s3_coherence_audit.md line 247 |
| Gemini notes | "themselves and Griffin" | AI summary, S07 | Avoid citing · research/s3_coherence_audit.md line 248 |

Also swept with zero relevant hits: Confluence "Matthew Collins" (user row only), "board of directors" 0.

**Known issues touched** (`references/known_data_issues/normal.md`).

All 33 cards were walked against the scope. A card's "Don't grade" value is never relied on.

| Card | Touched by | Disposition |
|---|---|---|
| NB-1 Slack access after Feb 11 | `#winddown` idx 88–95 itself describes the guest change | Seeded Slack only from Leonard, Robert or Arthur, in founder channels or DMs. No row on who can read what · research/s3_coherence_audit.md line 258 |
| NB-3 Cash at Dec 31 / Jan 31 | Draft idx 7 "runway of less than a month"; `D04UC0UEN2V` idx 24 | No cash figure in any row. Percentages of preferred only |
| NB-4 February payments | Sunset's fee, `leonard@harmonygames.co_1856956473569789052.json` "Your payment" | No row on whether Sunset was paid |
| NB-5, NB-8 Helpshift | `#winddown` idx 18, 57. In the channel a run reads, off-path | Avoid; the letter must not cite a vendor balance · research/s3_coherence_audit.md line 261 |
| NB-6 Slack after Feb 13 10:03 UTC | Every seeded Slack row | Seed window for outreach state: Feb 12 22:17 to Feb 13 10:03 UTC. No reference to later Slack · research/s3_coherence_audit.md line 262 |
| NB-12 Token-only names | ES-1, 2, 5, 14, 15; DD names; Task List rows 8, 9 | Key by id. Accepted name forms include the token · research/s3_coherence_audit.md line 263 |
| NB-15 Employee or contractor | LIST mail: "one Washington-based employee"; `#winddown` idx 42: "no US employees"; Feb 11 letters: "independent contractor" | Dated and compatible: the 2024 marketing hire left Oct 2025 (INFERENCE, ES-17). No row on status · research/s3_coherence_audit.md line 264 |
| NB-20 Board marketing figure | Only if a board deck is opened (Tor received `Harmony Games BoD Oct 14 2025 (1).pdf`) | Avoid: UNREAD and off-path · research/s3_coherence_audit.md line 265 |
| NB-22 Letter date | ES-12's letter `leonard@harmonygames.co_1856860994291529096.json` says January 31, 2025. The card's "00016874" is the file `threads/00016874.json`, another mailbox's copy of the same letter | Grade ES-12 from its Carta notice |
| NB-24 No Linear comments | Measured: `/comments` is `[]`. Seeded comments would be the first in the export | **Fold.** Allowed, but see §0 item 8 · research/s3_coherence_audit.md line 267 |
| NB-29 Decision date | `#winddown` opens Feb 9 | No decision date as a window start. The told-state rule runs from a written record, not this date · research/s3_coherence_audit.md line 268 |
| NB-31 DM member lists | `D04UC0UEN2V` lists 5 members, `D09R59580EM` lists 4 | Never argue who saw a DM from members. Told state rests on authored messages |

Not touched: NB-2, 7, 9, 10, 11, 13, 14, 16, 17, 18, 19, 21, 23, 25, 26, 27, 28, 30, 32, 33. Keep NB-9 and NB-26 out of the letter: the draft mentions Combo Fighter, so a rewrite that adds platform or sales claims would walk into them.

## 1b Active speakers

`activity.json` status at the clock. External people have no `activity.json` entry, so the last-authored date stands in. Seeded voices are the three founders, PERSON_3088 (KPMG) and PERSON_2888 (Sunset) only.

| Person | Email | status_at_clock | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_feb_2026 | project, notes, comments, Slack origin post |
| Robert | robert@harmonygames.co | active_feb_2026 | reply to Nebojsa; comments |
| Arthur Blake | arthur.blake@harmonygames.co | active_feb_2026 | comments; DM reply |
| KPMG associate | PERSON_3088_EMAIL | not in activity.json; last authored 2024-12-18, leonard@harmonygames.co_1817557789846606177.json | FY25 request |
| Sunset Head of Partnerships | PERSON_2888_EMAIL | not in activity.json; last authored 2026-02-11, leonard@harmonygames.co_1856872398290956689.json | Company Information request |
| Griffin VP Finance | PERSON_2847_EMAIL | not in activity.json; cc 2026-02-12 | cc only, no seeded voice |
| Vincent Parker | vincent.parker@harmonygames.co | quiet_since_2025-12 | holder only; must stay untold, no seed may speak for him |
| Frederick Stone | frederick.stone@harmonygames.co | quiet_since_2025-10 | holder only, no voice |
| Victor Barnes | victor.barnes@harmonygames.co | quiet_since_2025-04 | holder only; cannot act (playbook S1) |
| Calvin Price | calvin.price@harmonygames.co | quiet_since_2025-10 | holder only |

## 1c Identity traps

Commands: `~/.local/bin/python3.12 -B Task_Authoring/tools/entity.py collisions` and `... resolve <name>`, default task, run from the workspace root. Output below is verbatim.

**Bottom line.** entity.py cannot resolve any external holder by name. "Philip Sanderson", "Kristian Segerstrale", "Bastian Bergmann", "Tor", "Patrick Lewis" and every Disli name return no exact match. Several PERSON tokens exist only as Contacts rows with a blank name. The pins below come from mail and Carta, not from the tool.

#### Pins: correct entity against lookalikes
| Correct entity | Lookalike | How to separate them | Rule |
|---|---|---|---|
| Leonard Hayes, `leonard.hayes@…`, Slack `EMPLOYEE_0038_SLACK_ID`, Linear `usr_63fffeb4fab5233e`, Trello `PERSON_6094_TRELLO_USER_ID` | Thread alias `leonard@…`; Drive copy of LIST shows `leonard@harmonygames.co` | Same person, I03 | Cite the id, state no title |
| Robert, `robert@…`, Slack `EMPLOYEE_0016_SLACK_ID` | Tokens [0054], [0055], [0174]; "Robert Incorporated" in the Gemini notes | Token aliases per C2; the entity name is a notes error | No row on an entity name · research/s3_coherence_audit.md line 314 |
| Arthur Blake, `arthur.blake@…`, Slack `EMPLOYEE_0025_SLACK_ID` | **Arthur Schaeppi** (Solsten, SSP-04). `PERSON_3083_NAME` also signs Blake's own mail (`leonard@harmonygames.co_1816809274978043917.json`[1]). "Blake" and "my CTO Blake" appear in mail | Surname always. Holder is keyed SSP-04 | Never write "Arthur" alone |
| Griffin partner PERSON_4337 = Philip Sanderson (name seen in Carta `leonard@harmonygames.co_1774928765255297348.json`) = "Phil" = [1999] (INFERENCE, C2) | [PERSON_NAME_2000] is the firm; PERSON_2717 is another Griffin investor (`leonard@harmonygames.co_1843007315645862923.json`[2]) | Signature "Senior Partner & Co-Founder" | Holder lines are the two funds, not the person |
| Griffin II SSP-01 and Side Fund SSP-02 | "GRIFFIN GAMING PARTNERS" as one line | Floor test | Two holders · research/s3_coherence_audit.md line 317 |
| Segerstrale: PERSON_3336 mail, PERSON_3335 mail and Slack; [0089] [25152], [0090], [6550], [6407], [6201]; "Kris", "Christian" | Menlo capital LLC; Tor's [0128]; [PERSON_NAME_6423], a third party in the same DM | `D04UC0UEN2V` idx 3, 12 show [6423] is someone else | Keyed SSP-03 |
| Tor: TOR Capital Limited (SSP-11) | Principal PERSON_5275 = [0128], [0129]; directors' signers PERSON_5137, PERSON_0711; counsel PERSON_5593 | Holder is the company: "cap table should have TOR Capital Ltd vs my name" (`leonard@harmonygames.co_1775636449493308689.json`[20]) | Note goes to the principal, holder line is the company |
| Patrick Lewis (mail, Turkish) = Patrick Haktan Disli, a Disli brother | **Bergmann** ("patrick" in 2025 mail, Solsten, `leonard@harmonygames.co_1836075678772806708.json`, `leonard@harmonygames.co_1833542911997635888.json`), and Contacts `/144` "Patrick", staff title | Mask collapses both onto `patrick@harmonygames.co`. Oct 31, 2023 BCC carries PERSON_0693 and `patrick@` as two people | Never grade an address. Bergmann keyed SSP-05 |
| Schaeppi SSP-04: PERSON_3063 personal, PERSON_3083 work | Arthur Blake; Slack "Joe Schaeppi" (C2) | §2 | Surname · research/s3_coherence_audit.md line 321 |
| Nebojsa ES-11, SSP-09: PERSON_3941, PERSON_3935, Slack `PERSON_3935_SLACK_ID` | entity.py flags `PERSON_3935` as an unjoined token_link. Slack user is a marketing voice in mpdm `C7442B7CD94B` to Oct 24, 2025; `leonard@harmonygames.co_1796464517368805372.json` and `leonard@harmonygames.co_1796465341448589349.json` show both addresses in one marketing sync. "IKE LOA LLC" (`leonard@harmonygames.co_1770577968081445872.json`) | INFERENCE: same person | Keep holder-of-record off the graded path |
| Deepak SSP-12: PERSON_1287, [2950], [0801] | ES-8 or ES-10 unnamed | DD and LIST by token | Never grade which ES · research/s3_coherence_audit.md line 323 |
| Matthew Collins `matthew.collins@…` = "Akin", Husnu Matthew Collins, [11362] | Mail signature "akin" | Carta SSP-10, ES-9 | Keyed SSP-10 · research/s3_coherence_audit.md line 324 |
| ES-12 Owen Baker | Thomas Baker (General Counsel in Contacts) | `f_414596b0a9d698267dd1e1` "Owen Baker – 0.162%" | ES id; P02 |
| ES-7 Marcus Bennett | Marcus Lee, Oscar Bennett, GitHub and Trello "Marcus" | Carta names him | ES id; P01, P02 · research/s3_coherence_audit.md line 326 |
| ES-3 Calvin Price | Nathan Price; two GitHub logins | Carta names him | ES id; P02 · research/s3_coherence_audit.md line 327 |
| ES-13 Martin Walsh | Martin Lewis; Carta adds a middle-name token | Letter `PERSON_4363_EMAIL`, "Hi Martin" | ES id; P01 · research/s3_coherence_audit.md line 328 |
| ES-18 Oliver Brooks | Lauren Brooks. **No Feb 11 letter exists for him:** a subject search of all mailboxes gives six recipients, none his | Carta names [0022] [2763] (C2 alias) | ES id; P02 · research/s3_coherence_audit.md line 329 |
| ES-4 Claire Morgan | GitHub "Claire", `PERSON_2360` | Letter to `PERSON_2360_EMAIL` | ES id; P01 · research/s3_coherence_audit.md line 330 |
| ES-16 EMPLOYEE_0032 | Josh Dempsey (`PAYROLL_ROSTER`, a separate entity with no activity); `cameron@harmonygames.co` (`leonard@harmonygames.co_1847333990408253969.json`) | INFERENCE that `cameron@` is ES-16: consulting-agreement exit Oct 24, Oct 2024 grant cohort, onboarding with Oliver. X02 | Never state a name |
| ES-17 [0038] = Frederick Stone | Letter addressed "ryan" `PERSON_2314_EMAIL` (S04) | Confirmed: the other-mailbox copy `threads/00015796.json` shows `"ryan" <frederick.stone@harmonygames.co>` | ES id · research/s3_coherence_audit.md line 332 |
| ES-15 [2769] [0093], "Omer" | "brian" `PERSON_4243_EMAIL` in the Feb 11 letter | INFERENCE only | ES id, no persona link · research/s3_coherence_audit.md line 333 |
| KPMG PERSON_3088, PERSON_4416 | PERSON_0467, PERSON_3710 (FY23 cc), PERSON_2322 (FY24 cc) | Signatures "Audit Associate" | Sender from the pattern only · research/s3_coherence_audit.md line 334 |
| Sunset PERSON_0767 (CEO), PERSON_2888 (Head of Partnerships), PERSON_3131 (CTO) | The Gemini notes spell "Jackie Alfenas", a raw name | Signatures | Keep the raw name out of seeds · research/s3_coherence_audit.md line 335 |

#### Output: collisions
```text

SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>', 'Marcus <trello:c48a210d5c5a4b59231c6873>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']

SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']

LOOKALIKE_HANDLES_AND_ALIASES (15)
  - Gmail thread files of arthur.blake@harmonygames.co are named 'blake@harmonygames.co_*' · research/s3_coherence_audit.md line 354
  - Gmail thread files of brian.foster@harmonygames.co are named 'brian@harmonygames.co_*' · research/s3_coherence_audit.md line 355
  - Gmail thread files of calvin.price@harmonygames.co are named 'calvin@harmonygames.co_*' · research/s3_coherence_audit.md line 356
  - Gmail thread files of claire.morgan@harmonygames.co are named 'claire@harmonygames.co_*' · research/s3_coherence_audit.md line 357
  - Gmail thread files of frederick.stone@harmonygames.co are named 'frederick@harmonygames.co_*' · research/s3_coherence_audit.md line 358
  - Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*' · research/s3_coherence_audit.md line 359
  - Gmail thread files of leonard.hayes@harmonygames.co are named 'leonard@harmonygames.co_*' · research/s3_coherence_audit.md line 360
  - Gmail thread files of oliver.brooks@harmonygames.co are named 'oliver@harmonygames.co_*' · research/s3_coherence_audit.md line 361
  - Gmail thread files of owen.baker@harmonygames.co are named 'owen@harmonygames.co_*' · research/s3_coherence_audit.md line 362
  - Gmail thread files of samuel.turner@harmonygames.co are named 'samuel@harmonygames.co_*' · research/s3_coherence_audit.md line 363
  - Gmail thread files of simon.walker@harmonygames.co are named 'simon@harmonygames.co_*' · research/s3_coherence_audit.md line 364
  - Gmail thread files of vincent.parker@harmonygames.co are named 'vincent@harmonygames.co_*' · research/s3_coherence_audit.md line 365
  - Gmail thread files of felix.young@harmonygames.co are named 'felixyoung@harmonygames.co_*' · research/s3_coherence_audit.md line 366
  - Gmail thread files of oscar.bennett@harmonygames.co are named 'oscar@harmonygames.co_*' · research/s3_coherence_audit.md line 367
  - Slack handle 'thomas' (U05F0A0D12F) belongs to Thomas Baker <thomas.baker@harmonygames.co> but equals the mailbox local part of Thomas <thomas@harmonygames.co> [persona thomas] · research/s3_coherence_audit.md line 368

LOOKALIKE_EMAIL_LOCAL_PARTS (2)
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>'] · research/s3_coherence_audit.md line 371
  - 'thomas@' vs 'thomaslee@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['? <thomaslee@harmonygames.co>'] · research/s3_coherence_audit.md line 372

TOKENS_MAPPING_TO_SEVERAL_ENTITIES (9)
  EMPLOYEE_0024: {'entities': ['scott <employee_0024@harmonygames.co>', '? <slack:EMPLOYEE_0024_SLACK_ID>', '? <trello:3d36d70154e6a715614e0d75>'], 'records': ['gcal.calendar_id=employee_0024@harmonygames.co', 'gcal.owner_email=employee_0024@harmonygames.co', 'linear.id=usr_EMPLOYEE_0024', 'linear.email=employee_0024@harmonygames.co', 'contacts.email=employee_0024@harmonygames.co', 'email.email=employee_0024@harmonygames.co', 'slack.id=EMPLOYEE_0024_SLACK_ID', 'trello.username=employee_0024']}
  EMPLOYEE_0032: {'entities': ['? <EMPLOYEE_0032_EMAIL>', 'Josh Dempsey <josh.dempsey@harmonygames.co>', '? <github:EMPLOYEE_0032_GITHUB_USERNAME>', '? <slack:EMPLOYEE_0032_SLACK_ID>'], 'records': ['confluence.id=user_EMPLOYEE_0032', 'gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME', 'slack.id=EMPLOYEE_0032_SLACK_ID']}
  PERSON_2218: {'entities': ['? <PERSON_2218_EMAIL>', '? <github:PERSON_2218_GITHUB_USERNAME>'], 'records': ['linear.id=usr_PERSON_2218', 'linear.email=PERSON_2218_EMAIL', 'contacts.email=PERSON_2218_EMAIL', 'email.email=PERSON_2218_EMAIL', 'github.login=PERSON_2218_GITHUB_USERNAME']}
  PERSON_2360: {'entities': ['? <PERSON_2360_EMAIL>', 'Claire <github:PERSON_2360_GITHUB_USERNAME>'], 'records': ['github.login=PERSON_2360_GITHUB_USERNAME', 'email.email=PERSON_2360_EMAIL']}
  PERSON_3233: {'entities': ['? <PERSON_3233_EMAIL>', '? <github:PERSON_3233_GITHUB_USERNAME>', '? <slack:PERSON_3233_SLACK_ID>'], 'records': ['linear.id=usr_PERSON_3233', 'linear.email=PERSON_3233_EMAIL', 'contacts.email=PERSON_3233_EMAIL', 'email.email=PERSON_3233_EMAIL', 'github.login=PERSON_3233_GITHUB_USERNAME', 'slack.id=PERSON_3233_SLACK_ID']}
  PERSON_3335: {'entities': ['? <PERSON_3335_EMAIL>', '? <slack:PERSON_3335_SLACK_ID>'], 'records': ['contacts.email=PERSON_3335_EMAIL', 'email.email=PERSON_3335_EMAIL', 'slack.id=PERSON_3335_SLACK_ID']}
  PERSON_3935: {'entities': ['? <PERSON_3935_EMAIL>', '? <slack:PERSON_3935_SLACK_ID>'], 'records': ['email.email=PERSON_3935_EMAIL', 'slack.id=PERSON_3935_SLACK_ID']}
  PERSON_5275: {'entities': ['? <PERSON_5275_EMAIL>', '? <slack:PERSON_5275_SLACK_ID>'], 'records': ['contacts.email=PERSON_5275_EMAIL', 'email.email=PERSON_5275_EMAIL', 'slack.id=PERSON_5275_SLACK_ID']}
  PERSON_5360: {'entities': ['? <PERSON_5360_EMAIL>', '? <slack:PERSON_5360_SLACK_ID>'], 'records': ['email.email=PERSON_5360_EMAIL', 'slack.id=PERSON_5360_SLACK_ID']}

SEVERAL_IDS_IN_ONE_SERVICE (1)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: 2 github identities ['PERSON_0003_GITHUB_USERNAME', 'PERSON_2137_GITHUB_USERNAME'] (joins: ['exact_email', 'exact_name']) · research/s3_coherence_audit.md line 386

PERSONA_ROLE_VS_CONTACTS_JOB (5)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: roster role 'Game Engineer (Unity VFX)' vs Contacts job 'Game Engineer (Unity/VFX)' · research/s3_coherence_audit.md line 386
  - Frederick Stone <frederick.stone@harmonygames.co> [persona frederick_stone]: roster role 'Co-founder' vs Contacts job 'Commercial Lead, Marketing & Business Development' · research/s3_coherence_audit.md line 390
  - Leonard Hayes <leonard.hayes@harmonygames.co> [persona leonard_hayes]: roster role 'Co-founder & Creative Director' vs Contacts job 'Co-founder & CEO' · research/s3_coherence_audit.md line 391
  - Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]: roster role 'Artist' vs Contacts job 'Artist (VFX & Animation)' · research/s3_coherence_audit.md line 392
  - Robert <robert@harmonygames.co> [persona robert]: roster role 'Co-Founder & Creative Director' vs Contacts job 'Co-founder & Chief Product Officer' · research/s3_coherence_audit.md line 393

SHARED_CONTACT_JOB_TITLES (5)
  Game Designer: ['Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]', 'Samuel Turner <samuel.turner@harmonygames.co> [persona samuel_turner]']
  Game Developer: ['Thomas <thomas@harmonygames.co> [persona thomas]', 'Lucas <lucas@harmonygames.co>']
  Game Engineer: ['Brian Foster <brian.foster@harmonygames.co> [persona brian_foster]', 'Victor Barnes <victor.barnes@harmonygames.co> [persona victor_barnes]']
  General Counsel: ['Michelle Carter <michelle.carter@harmonygames.co>', 'Thomas Baker <thomas.baker@harmonygames.co>']
  User Acquisition Manager: ['George Miller <george.miller@harmonygames.co>', 'Megan Wilson <megan.wilson@harmonygames.co>', 'Victoria Lane <victoria.lane@harmonygames.co>']

UNRESOLVED (12)
  [ambiguous_name] github: mononym 'Marcus' is an exact name of (none) and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  [ambiguous_name] github: mononym 'Claire' is an exact name of (none) and the first name of ['email:claire.morgan@harmonygames.co'] -> candidates ['email:claire.morgan@harmonygames.co']
  [ambiguous_name] trello: mononym 'Marcus' is an exact name of ['github:PERSON_0396_GITHUB_USERNAME'] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co', 'github:PERSON_0396_GITHUB_USERNAME']
  [token_link] EMPLOYEE_0024: same token number across services but no shared exact email/name: not joined -> candidates ['email:employee_0024@harmonygames.co', 'slack:EMPLOYEE_0024_SLACK_ID', 'trello:3d36d70154e6a715614e0d75']
  [token_link] EMPLOYEE_0032: same token number across services but no shared exact email/name: not joined -> candidates ['email:EMPLOYEE_0032_EMAIL', 'email:josh.dempsey@harmonygames.co', 'github:EMPLOYEE_0032_GITHUB_USERNAME', 'slack:EMPLOYEE_0032_SLACK_ID']
  [token_link] PERSON_2218: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2218_EMAIL', 'github:PERSON_2218_GITHUB_USERNAME']
  [token_link] PERSON_2360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2360_EMAIL', 'github:PERSON_2360_GITHUB_USERNAME']
  [token_link] PERSON_3233: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3233_EMAIL', 'github:PERSON_3233_GITHUB_USERNAME', 'slack:PERSON_3233_SLACK_ID']
  [token_link] PERSON_3335: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3335_EMAIL', 'slack:PERSON_3335_SLACK_ID']
  [token_link] PERSON_3935: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3935_EMAIL', 'slack:PERSON_3935_SLACK_ID']
  [token_link] PERSON_5275: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5275_EMAIL', 'slack:PERSON_5275_SLACK_ID']
  [token_link] PERSON_5360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5360_EMAIL', 'slack:PERSON_5360_SLACK_ID']

INTEGRITY FLAGS (2)
  {'type': 'id_with_space', 'service': 'linear', 'id': 'usr_Victor Barnes'}
  {'type': 'name_mismatch_on_email_join', 'service': 'github', 'id': 'PERSON_2314_GITHUB_USERNAME', 'detail': "GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frederick Stone)"}
```

#### Output: resolve
```text
#### resolve: Leonard Hayes
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=143292, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
  gmail      mailbox=leonard.hayes@harmonygames.co, threads=17635, messages=22648, first=2023-03-15, last=2026-02-13, thread_filename_alias=['leonard@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=leonard.hayes@harmonygames.co, owner_email=leonard.hayes@harmonygames.co, summary=Leonard Hayes — primary, events=1512, last_event_before_clock=2026-02-12   [join: exact_email]
  gdrive     id=user_63fffeb4fab5, email=leonard.hayes@harmonygames.co, display_name=leonard.hayes@harmonygames.co, root_folders=['d_63fffeb4fab5233ed5bb73'], owned_items=817, last_modified=2026-02-11, files_shared_with=413   [join: exact_email]
  linear     id=usr_63fffeb4fab5233e, email=leonard.hayes@harmonygames.co, name=leonard.hayes@harmonygames.co, is_active=True, last_activity=2026-01-28   [join: exact_email]
  trello     id=PERSON_6094_TRELLO_USER_ID, username=leonard.hayes, fullName=Leonard Hayes, last_activity=2025-11-13   [join: exact_name]
  confluence id=user_EMPLOYEE_0038, account_id=acct_EMPLOYEE_0038, email=leonard.hayes@harmonygames.co, display_name=Leonard Hayes, is_active=True, last_activity=2026-02-09   [join: exact_email]
  contacts   contact_id=63fffeb4fab5233ed5bb73bf, name=Leonard Hayes, email=leonard.hayes@harmonygames.co, job=Co-founder & CEO, is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2026-02-13', 'gmail': '2026-02-13', 'gcal': '2026-02-12', 'gdrive': '2026-02-11', 'linear': '2026-01-28', 'trello': '2025-11-13', 'confluence': '2026-02-09'}
#### resolve: Robert
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=129939, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
  gmail      mailbox=robert@harmonygames.co, threads=16233, messages=19169, first=2023-03-15, last=2026-02-13   [join: exact_email]
  gcal       calendar_id=robert@harmonygames.co, owner_email=robert@harmonygames.co, summary=Robert — primary, events=1229, last_event_before_clock=2026-02-12   [join: exact_email]
  gdrive     id=user_9f7ba94f7526, email=robert@harmonygames.co, display_name=Robert, root_folders=['d_9f7ba94f7526d54d8482ba'], owned_items=223, last_modified=2026-02-12, files_shared_with=464   [join: exact_email]
  linear     id=usr_Robert, email=robert@harmonygames.co, name=Robert, is_active=True, last_activity=2025-10-27   [join: exact_email]
  github     login=EMPLOYEE_0016_GITHUB_USERNAME, name=Robert, email=robert@harmonygames.co, type=User, last_activity=2026-01-16   [join: exact_email]
  trello     id=3d06b73654d0c8940792514c, username=robert, fullName=Robert   [join: exact_name]
  confluence id=user_EMPLOYEE_0016, account_id=acct_EMPLOYEE_0016, email=robert@harmonygames.co, display_name=Robert, is_active=True, last_activity=2026-02-12   [join: exact_email]
  contacts   contact_id=5f647df33ba6e92fbd56b05b, name=Robert, email=robert@harmonygames.co, job=Co-founder & Chief Product Officer, is_user=True   [join: exact_email]
  last activity: {'slack': '2026-02-13', 'gmail': '2026-02-13', 'gcal': '2026-02-12', 'gdrive': '2026-02-12', 'linear': '2025-10-27', 'github': '2026-01-16', 'confluence': '2026-02-12'}
#### resolve: Arthur Blake
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=38591, first_post=2023-03-20, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=arthur.blake@harmonygames.co, threads=4721, messages=6876, first=2023-03-23, last=2026-02-13, thread_filename_alias=['blake@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=arthur.blake@harmonygames.co, owner_email=arthur.blake@harmonygames.co, summary=Arthur Blake — primary, events=824, last_event_before_clock=2026-02-12   [join: exact_email]
  gdrive     id=user_cc3e90160f49, email=arthur.blake@harmonygames.co, display_name=arthur.blake@harmonygames.co, root_folders=['d_cc3e90160f490686039986'], owned_items=269, last_modified=2026-01-15, files_shared_with=456   [join: exact_email]
  linear     id=usr_cc3e90160f490686, email=arthur.blake@harmonygames.co, name=arthur.blake@harmonygames.co, is_active=True, last_activity=2026-01-28   [join: exact_email]
  github     login=EMPLOYEE_0025_GITHUB_USERNAME, name=Arthur Blake, email=arthur.blake@harmonygames.co, type=User, last_activity=2026-02-13   [join: exact_email]
  trello     id=2162c1ba310341bf318f48b7, username=arthur.blake, fullName=Arthur Blake   [join: exact_name]
  confluence id=user_EMPLOYEE_0025, account_id=acct_EMPLOYEE_0025, email=arthur.blake@harmonygames.co, display_name=Arthur Blake, is_active=True, last_activity=2026-02-11   [join: exact_email]
  contacts   contact_id=cc3e90160f49068603998654, name=Arthur Blake, email=arthur.blake@harmonygames.co, job=Co-founder & CTO, is_user=False   [join: exact_email]
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-13', 'gcal': '2026-02-12', 'gdrive': '2026-01-15', 'linear': '2026-01-28', 'github': '2026-02-13', 'confluence': '2026-02-11'}
#### resolve: Philip Sanderson
no exact match for 'Philip Sanderson'
#### resolve: PERSON_4337
ENTITY email:PERSON_4337_EMAIL  name=None  kind=unidentified  emails=['PERSON_4337_EMAIL']
  gdrive     share_recipient=PERSON_4337_EMAIL, files_shared_with=1   [join: exact_email]
  contacts   contact_id=3cb768c4ca8515702d29b703, name=PERSON_4337, email=PERSON_4337_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence
  last activity: -
#### resolve: PERSON_2847
no exact match for 'PERSON_2847'
#### resolve: PERSON_3088
no exact match for 'PERSON_3088'
#### resolve: PERSON_4416
no exact match for 'PERSON_4416'
#### resolve: PERSON_0767
no exact match for 'PERSON_0767'
#### resolve: PERSON_2888
no exact match for 'PERSON_2888'
#### resolve: PERSON_5593
no exact match for 'PERSON_5593'
#### resolve: PERSON_5275
ENTITY email:PERSON_5275_EMAIL  name=None  kind=unidentified  emails=['PERSON_5275_EMAIL']
  contacts   contact_id=82103c829a5708060fb0b37b, name=PERSON_5275, email=PERSON_5275_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, gdrive, linear, github, trello, confluence
  last activity: -
  UNRESOLVED (token_link): same token number across services but no shared exact email/name: not joined  records=['contacts.email=PERSON_5275_EMAIL', 'email.email=PERSON_5275_EMAIL', 'slack.id=PERSON_5275_SLACK_ID']
#### resolve: PERSON_3336
ENTITY email:PERSON_3336_EMAIL  name=None  kind=unidentified  emails=['PERSON_3336_EMAIL']
  gdrive     share_recipient=PERSON_3336_EMAIL, files_shared_with=20   [join: exact_email]
  contacts   contact_id=ca57f88d55376b4341c5b6d4, name=PERSON_3336, email=PERSON_3336_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence
  last activity: -
#### resolve: PERSON_3335
ENTITY email:PERSON_3335_EMAIL  name=None  kind=unidentified  emails=['PERSON_3335_EMAIL']
  contacts   contact_id=1673c82fc650e0c42ab440d8, name=PERSON_3335, email=PERSON_3335_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, gdrive, linear, github, trello, confluence
  last activity: -
  UNRESOLVED (token_link): same token number across services but no shared exact email/name: not joined  records=['contacts.email=PERSON_3335_EMAIL', 'email.email=PERSON_3335_EMAIL', 'slack.id=PERSON_3335_SLACK_ID']
#### resolve: PERSON_0693
no exact match for 'PERSON_0693'
#### resolve: PERSON_3063
no exact match for 'PERSON_3063'
#### resolve: PERSON_3083
ENTITY email:PERSON_3083_EMAIL  name=None  kind=unidentified  emails=['PERSON_3083_EMAIL']
  gdrive     share_recipient=PERSON_3083_EMAIL, files_shared_with=1   [join: exact_email]
  contacts   contact_id=aaf48372feabcf6490f30d7c, name=PERSON_3083, email=PERSON_3083_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence
  last activity: -
#### resolve: PERSON_2275
no exact match for 'PERSON_2275'
#### resolve: PERSON_2260
ENTITY email:PERSON_2260_EMAIL  name=None  kind=unidentified  emails=['PERSON_2260_EMAIL']
  gdrive     share_recipient=PERSON_2260_EMAIL, files_shared_with=1   [join: exact_email]
  contacts   contact_id=9498fdeb61155487c7a2eb59, name=PERSON_2260, email=PERSON_2260_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence
  last activity: -
#### resolve: PERSON_3935
no exact match for 'PERSON_3935'
  candidate: email:PERSON_3935_EMAIL  None  ['PERSON_3935_EMAIL']
  candidate: slack:PERSON_3935_SLACK_ID  None  (none)
#### resolve: PERSON_3941
ENTITY email:PERSON_3941_EMAIL  name=None  kind=unidentified  emails=['PERSON_3941_EMAIL']
  gdrive     share_recipient=PERSON_3941_EMAIL, files_shared_with=9   [join: exact_email]
  contacts   contact_id=a65131d8d9f49c59825ffdaa, name=PERSON_3941, email=PERSON_3941_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence
  last activity: -
#### resolve: PERSON_1287
ENTITY email:PERSON_1287_EMAIL  name=None  kind=unidentified  emails=['PERSON_1287_EMAIL']
  contacts   contact_id=46aabf1857b0733da86c4649, name=PERSON_1287, email=PERSON_1287_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, gdrive, linear, github, trello, confluence
  last activity: -
#### resolve: Matthew Collins
ENTITY email:matthew.collins@harmonygames.co  name=Matthew Collins  kind=person  emails=['matthew.collins@harmonygames.co']
  slack      id=UEC7997064E, name=matthew, real_name=Matthew Collins, email=matthew.collins@harmonygames.co, is_bot=False, deleted=False, messages=0   [join: exact_email]
  gcal       calendar_id=matthew.collins@harmonygames.co, owner_email=matthew.collins@harmonygames.co, summary=Matthew Collins — primary, events=13, last_event_before_clock=2025-07-16   [join: exact_email]
  gdrive     share_recipient=matthew.collins@harmonygames.co, files_shared_with=6   [join: exact_email]
  linear     id=usr_ec7997064e6cfa96, email=matthew.collins@harmonygames.co, name=matthew.collins@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=6fe425fec235c058aff716f7, username=matthew.collins, fullName=Matthew Collins   [join: exact_name]
  confluence id=user_STAFF_4, account_id=acct_STAFF_4, email=matthew.collins@harmonygames.co, display_name=Matthew Collins, is_active=False   [join: exact_email]
  contacts   contact_id=db57e559500151d6b3991b62, name=Matthew Collins, email=matthew.collins@harmonygames.co, job=Independent Director (investor/advisor, not an employee), is_user=False   [join: exact_email]
  absent from: gmail, github
  last activity: {'gcal': '2025-07-16'}
#### resolve: Patrick Lewis
no exact match for 'Patrick Lewis'
#### resolve: Patrick
ENTITY email:patrick@harmonygames.co  name=Patrick  kind=person  emails=['patrick@harmonygames.co']
  names seen: ['Patrick', 'patrick']
  slack      id=U23DDDA4810, name=patrick, real_name=patrick, email=patrick@harmonygames.co, is_bot=False, deleted=False, messages=0   [join: exact_email]
  gcal       calendar_id=patrick@harmonygames.co, owner_email=patrick@harmonygames.co, summary=Patrick — primary, events=0   [join: exact_email]
  linear     id=usr_23ddda4810068cc4, email=patrick@harmonygames.co, name=patrick@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=e759439b43589abac5ec723a, username=patrick, fullName=Patrick   [join: exact_name]
  confluence id=user_STAFF_12, account_id=acct_STAFF_12, email=patrick@harmonygames.co, display_name=Patrick, is_active=True   [join: exact_email]
  contacts   contact_id=e704baa2167b3624a98b3352, name=Patrick, email=patrick@harmonygames.co, job=Business Development / Partnerships Manager, is_user=False   [join: exact_email]
  absent from: gmail, gdrive, github
  last activity: -
#### resolve: Kristian Segerstrale
no exact match for 'Kristian Segerstrale'
#### resolve: Bastian Bergmann
no exact match for 'Bastian Bergmann'
#### resolve: Tor
no exact match for 'Tor'
  candidate: email:victor.barnes@harmonygames.co  Victor Barnes  ['victor.barnes@harmonygames.co']
  candidate: email:victoria.lane@harmonygames.co  Victoria Lane  ['victoria.lane@harmonygames.co']
#### resolve: Calvin Price
ENTITY email:calvin.price@harmonygames.co  name=Calvin Price  kind=person  emails=['calvin.price@harmonygames.co']
  persona: calvin_price - Game Engineer (Unity VFX) / Engineering
  slack      id=EMPLOYEE_0006_SLACK_ID, name=Calvin Price, real_name=Calvin Price, email=calvin.price@harmonygames.co, is_bot=False, deleted=False, messages=12359, first_post=2023-03-29, last_post=2025-10-24   [join: exact_email]
  gmail      mailbox=calvin.price@harmonygames.co, threads=8213, messages=9971, first=2023-03-29, last=2025-11-13, thread_filename_alias=['calvin@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=calvin.price@harmonygames.co, owner_email=calvin.price@harmonygames.co, summary=Calvin Price — primary, events=455, last_event_before_clock=2025-10-24   [join: exact_email]
  gdrive     id=user_49b9dfa5208d, email=calvin.price@harmonygames.co, display_name=calvin.price@harmonygames.co, root_folders=['d_49b9dfa5208d400d9b3937'], owned_items=1918, last_modified=2025-02-14, files_shared_with=132   [join: exact_email]
  linear     id=usr_49b9dfa5208d400d, email=calvin.price@harmonygames.co, name=calvin.price@harmonygames.co, is_active=True, last_activity=2026-01-01   [join: exact_email]
  github     login=PERSON_0003_GITHUB_USERNAME, name=Calvin Price, email=calvin.price@harmonygames.co, type=User, last_activity=2025-10-22   [join: exact_email]
  github     login=PERSON_2137_GITHUB_USERNAME, name=Calvin Price, type=User, last_activity=2025-10-09   [join: exact_name]
  trello     id=ca5bb4c09fbf2a437f04531e, username=calvin.price, fullName=Calvin Price   [join: exact_name]
  confluence id=user_STAFF_19, account_id=acct_STAFF_19, email=calvin.price@harmonygames.co, display_name=Calvin Price, is_active=True   [join: exact_email]
  contacts   contact_id=49b9dfa5208d400d9b3937ca, name=Calvin Price, email=calvin.price@harmonygames.co, job=Game Engineer (Unity/VFX), is_user=False   [join: exact_email]
  last activity: {'slack': '2025-10-24', 'gmail': '2025-11-13', 'gcal': '2025-10-24', 'gdrive': '2025-02-14', 'linear': '2026-01-01', 'github': '2025-10-22'}
#### resolve: Claire Morgan
ENTITY email:claire.morgan@harmonygames.co  name=Claire Morgan  kind=person  emails=['claire.morgan@harmonygames.co']
  persona: claire_morgan - Art Lead / Design
  slack      id=EMPLOYEE_0009_SLACK_ID, name=Claire Morgan, real_name=Claire Morgan, email=claire.morgan@harmonygames.co, is_bot=False, deleted=False, messages=10447, first_post=2023-03-22, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=claire.morgan@harmonygames.co, threads=980, messages=1065, first=2023-03-30, last=2026-02-12, thread_filename_alias=['claire@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=claire.morgan@harmonygames.co, owner_email=claire.morgan@harmonygames.co, summary=Claire Morgan — primary, events=594, last_event_before_clock=2026-01-19   [join: exact_email]
  gdrive     id=user_7fe31e7ec819, email=claire.morgan@harmonygames.co, display_name=claire.morgan@harmonygames.co, root_folders=['d_7fe31e7ec81996189e1f14'], owned_items=69, last_modified=2024-07-08, files_shared_with=119   [join: exact_email]
  linear     id=usr_7fe31e7ec8199618, email=claire.morgan@harmonygames.co, name=claire.morgan@harmonygames.co, is_active=True, last_activity=2025-10-23   [join: exact_email]
  github     login=EMPLOYEE_0009_GITHUB_USERNAME, name=Claire Morgan, email=claire.morgan@harmonygames.co, type=User, last_activity=2025-10-15   [join: exact_email]
  trello     id=4bc5d398e54226f344ad3abc, username=claire.morgan, fullName=Claire Morgan   [join: exact_name]
  confluence id=user_EMPLOYEE_0009, account_id=acct_EMPLOYEE_0009, email=claire.morgan@harmonygames.co, display_name=Claire Morgan, is_active=True   [join: exact_email]
  contacts   contact_id=7fe31e7ec81996189e1f14d6, name=Claire Morgan, email=claire.morgan@harmonygames.co, job=Art Lead, is_user=False   [join: exact_email]
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-12', 'gcal': '2026-01-19', 'gdrive': '2024-07-08', 'linear': '2025-10-23', 'github': '2025-10-15'}
  UNRESOLVED (ambiguous_name): mononym 'Claire' is an exact name of (none) and the first name of ['email:claire.morgan@harmonygames.co']
#### resolve: Marcus Bennett
ENTITY email:marcus.bennett@harmonygames.co  name=Marcus Bennett  kind=person  emails=['marcus.bennett@harmonygames.co']
  persona: marcus_bennett - Artist / Design
  slack      id=EMPLOYEE_0002_SLACK_ID, name=Marcus Bennett, real_name=Marcus Bennett, email=marcus.bennett@harmonygames.co, is_bot=False, deleted=False, messages=29373, first_post=2023-09-28, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=marcus.bennett@harmonygames.co, threads=4329, messages=4355, first=2023-09-28, last=2026-02-11, thread_filename_alias=['marcus.bennett@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=marcus.bennett@harmonygames.co, owner_email=marcus.bennett@harmonygames.co, summary=Marcus Bennett — primary, events=663, last_event_before_clock=2026-02-03   [join: exact_email]
  gdrive     id=user_c77c50cc15c5, email=marcus.bennett@harmonygames.co, display_name=marcus.bennett@harmonygames.co, root_folders=['d_c77c50cc15c5342d638ebb'], owned_items=47335, last_modified=2025-09-10, files_shared_with=137   [join: exact_email]
  linear     id=usr_c77c50cc15c5342d, email=marcus.bennett@harmonygames.co, name=marcus.bennett@harmonygames.co, is_active=True, last_activity=2025-12-03   [join: exact_email]
  trello     id=7a20445f698bc5871ffd17f5, username=marcus.bennett, fullName=Marcus Bennett   [join: exact_name]
  confluence id=user_EMPLOYEE_0002, account_id=acct_EMPLOYEE_0002, email=marcus.bennett@harmonygames.co, display_name=Marcus Bennett, is_active=True   [join: exact_email]
  contacts   contact_id=c77c50cc15c5342d638ebb21, name=Marcus Bennett, email=marcus.bennett@harmonygames.co, job=Artist (VFX & Animation), is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-11', 'gcal': '2026-02-03', 'gdrive': '2025-09-10', 'linear': '2025-12-03'}
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of (none) and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of ['github:PERSON_0396_GITHUB_USERNAME'] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
#### resolve: Martin Walsh
ENTITY email:martin.walsh@harmonygames.co  name=Martin Walsh  kind=person  emails=['martin.walsh@harmonygames.co']
  persona: martin_walsh - Game Designer / Design
  slack      id=EMPLOYEE_0033_SLACK_ID, name=Martin Walsh, real_name=Martin Walsh, email=martin.walsh@harmonygames.co, is_bot=False, deleted=False, messages=9492, first_post=2023-08-28, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=martin.walsh@harmonygames.co, threads=4543, messages=4868, first=2023-08-27, last=2026-02-13, thread_filename_alias=['martin.walsh@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=martin.walsh@harmonygames.co, owner_email=martin.walsh@harmonygames.co, summary=Martin Walsh — primary, events=631, last_event_before_clock=2026-01-14   [join: exact_email]
  gdrive     id=user_51f5f16d46e8, email=martin.walsh@harmonygames.co, display_name=martin.walsh@harmonygames.co, root_folders=['d_51f5f16d46e8cf55f5ee33'], owned_items=30, last_modified=2024-02-16, files_shared_with=144   [join: exact_email]
  linear     id=usr_51f5f16d46e8cf55, email=martin.walsh@harmonygames.co, name=martin.walsh@harmonygames.co, is_active=True, last_activity=2026-01-10   [join: exact_email]
  trello     id=ba9cc333cefad99228d6757d, username=martin.walsh, fullName=Martin Walsh   [join: exact_name]
  confluence id=user_EMPLOYEE_0033, account_id=acct_EMPLOYEE_0033, email=martin.walsh@harmonygames.co, display_name=Martin Walsh, is_active=True   [join: exact_email]
  contacts   contact_id=51f5f16d46e8cf55f5ee337b, name=Martin Walsh, email=martin.walsh@harmonygames.co, job=Game Designer, is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-13', 'gcal': '2026-01-14', 'gdrive': '2024-02-16', 'linear': '2026-01-10'}
#### resolve: Oliver Brooks
ENTITY email:oliver.brooks@harmonygames.co  name=Oliver Brooks  kind=person  emails=['oliver.brooks@harmonygames.co']
  persona: oliver_brooks - Senior Game Engineer / Engineering
  slack      id=EMPLOYEE_0003_SLACK_ID, name=Oliver Brooks, real_name=Oliver Brooks, email=oliver.brooks@harmonygames.co, is_bot=False, deleted=False, messages=23993, first_post=2024-08-12, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=oliver.brooks@harmonygames.co, threads=1687, messages=2445, first=2024-08-08, last=2026-02-12, thread_filename_alias=['oliver@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=oliver.brooks@harmonygames.co, owner_email=oliver.brooks@harmonygames.co, summary=Oliver Brooks — primary, events=315, last_event_before_clock=2026-01-01   [join: exact_email]
  gdrive     id=user_bdf01b53c6a9, email=oliver.brooks@harmonygames.co, display_name=oliver.brooks@harmonygames.co, root_folders=['d_bdf01b53c6a92c5e167c65'], owned_items=8, last_modified=2025-09-01, files_shared_with=112   [join: exact_email]
  linear     id=usr_bdf01b53c6a92c5e, email=oliver.brooks@harmonygames.co, name=oliver.brooks@harmonygames.co, is_active=True, last_activity=2025-11-20   [join: exact_email]
  github     login=EMPLOYEE_0003_GITHUB_USERNAME, name=Oliver Brooks, email=oliver.brooks@harmonygames.co, type=User, last_activity=2026-02-13   [join: exact_email]
  trello     id=12c4a9dcd2d37a25a8d3b557, username=oliver.brooks, fullName=Oliver Brooks   [join: exact_name]
  confluence id=user_EMPLOYEE_0003, account_id=acct_EMPLOYEE_0003, email=oliver.brooks@harmonygames.co, display_name=Oliver Brooks, is_active=True, last_activity=2025-10-01   [join: exact_email]
  contacts   contact_id=bdf01b53c6a92c5e167c658c, name=Oliver Brooks, email=oliver.brooks@harmonygames.co, job=Senior Game Engineer, is_user=False   [join: exact_email]
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-12', 'gcal': '2026-01-01', 'gdrive': '2025-09-01', 'linear': '2025-11-20', 'github': '2026-02-13', 'confluence': '2025-10-01'}
#### resolve: Owen Baker
ENTITY email:owen.baker@harmonygames.co  name=Owen Baker  kind=person  emails=['owen.baker@harmonygames.co']
  persona: owen_baker - Game Engineer (Unity) / Engineering
  slack      id=EMPLOYEE_0021_SLACK_ID, name=Owen Baker, real_name=Owen Baker, email=owen.baker@harmonygames.co, is_bot=False, deleted=False, messages=16295, first_post=2023-09-15, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=owen.baker@harmonygames.co, threads=1595, messages=1633, first=2023-09-14, last=2026-02-10, thread_filename_alias=['owen@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=owen.baker@harmonygames.co, owner_email=owen.baker@harmonygames.co, summary=Owen Baker — primary, events=511, last_event_before_clock=2026-01-01   [join: exact_email]
  gdrive     id=user_4e13bd40cc73, email=owen.baker@harmonygames.co, display_name=owen.baker@harmonygames.co, root_folders=['d_4e13bd40cc73d0fc76f87c'], owned_items=10, last_modified=2025-08-25, files_shared_with=134   [join: exact_email]
  linear     id=usr_4e13bd40cc73d0fc, email=owen.baker@harmonygames.co, name=owen.baker@harmonygames.co, is_active=True, last_activity=2025-11-19   [join: exact_email]
  github     login=PERSON_5877_GITHUB_USERNAME, name=Owen Baker, email=owen.baker@harmonygames.co, type=User, last_activity=2026-02-13   [join: exact_email]
  trello     id=919ee44a0d5157b7839f66a8, username=owen.baker, fullName=Owen Baker   [join: exact_name]
  confluence id=user_EMPLOYEE_0021, account_id=acct_EMPLOYEE_0021, email=owen.baker@harmonygames.co, display_name=Owen Baker, is_active=True   [join: exact_email]
  contacts   contact_id=4e13bd40cc73d0fc76f87c7d, name=Owen Baker, email=owen.baker@harmonygames.co, job=Game Engineer (Unity), is_user=False   [join: exact_email]
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-10', 'gcal': '2026-01-01', 'gdrive': '2025-08-25', 'linear': '2025-11-19', 'github': '2026-02-13'}
#### resolve: Victor Barnes
ENTITY email:victor.barnes@harmonygames.co  name=Victor Barnes  kind=person  emails=['victor.barnes@harmonygames.co']
  persona: victor_barnes - Game Engineer / Engineering
  slack      id=EMPLOYEE_0030_SLACK_ID, name=Victor Barnes, real_name=Victor Barnes, email=victor.barnes@harmonygames.co, is_bot=False, deleted=False, messages=6499, first_post=2023-05-11, last_post=2025-04-15   [join: exact_email]
  gmail      mailbox=victor.barnes@harmonygames.co, threads=4286, messages=4370, first=2023-05-11, last=2025-04-15   [join: exact_email]
  gcal       calendar_id=victor.barnes@harmonygames.co, owner_email=victor.barnes@harmonygames.co, summary=Victor Barnes — primary, events=642, last_event_before_clock=2025-07-23   [join: exact_email]
  gdrive     id=user_7c929dfbe0e1, email=victor.barnes@harmonygames.co, display_name=Victor Barnes, root_folders=['d_7c929dfbe0e1b0c0d2c7ca'], owned_items=28, last_modified=2024-02-22, files_shared_with=145   [join: exact_email]
  linear     id=usr_Victor Barnes, email=victor.barnes@harmonygames.co, name=Victor Barnes, is_active=True, last_activity=2025-03-06   [join: exact_email]
  trello     id=904fe5def35c5dddd2037d69, username=victor.barnes, fullName=Victor Barnes   [join: exact_name]
  confluence id=user_EMPLOYEE_0030, account_id=acct_EMPLOYEE_0030, email=victor.barnes@harmonygames.co, display_name=Victor Barnes, is_active=False   [join: exact_email]
  contacts   contact_id=20d3b9e691397554ea110e60, name=Victor Barnes, email=victor.barnes@harmonygames.co, job=Game Engineer, is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2025-04-15', 'gmail': '2025-04-15', 'gcal': '2025-07-23', 'gdrive': '2024-02-22', 'linear': '2025-03-06'}
#### resolve: Frederick Stone
ENTITY email:frederick.stone@harmonygames.co  name=Frederick Stone  kind=person  emails=['frederick.stone@harmonygames.co']
  persona: frederick_stone - Co-founder / Executive
  slack      id=EMPLOYEE_0008_SLACK_ID, name=Frederick Stone, real_name=Frederick Stone, email=frederick.stone@harmonygames.co, is_bot=False, deleted=False, messages=4841, first_post=2023-09-15, last_post=2025-10-24   [join: exact_email]
  gmail      mailbox=frederick.stone@harmonygames.co, threads=5009, messages=5891, first=2024-06-25, last=2025-11-13, thread_filename_alias=['frederick@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=frederick.stone@harmonygames.co, owner_email=frederick.stone@harmonygames.co, summary=Frederick Stone — primary, events=336, last_event_before_clock=2026-01-14   [join: exact_email]
  gdrive     id=user_175c0d7bc72e, email=frederick.stone@harmonygames.co, display_name=frederick.stone@harmonygames.co, root_folders=['d_175c0d7bc72ed244b944cb'], owned_items=46, last_modified=2025-09-24, files_shared_with=223   [join: exact_email]
  linear     id=usr_175c0d7bc72ed244, email=frederick.stone@harmonygames.co, name=frederick.stone@harmonygames.co, is_active=True, last_activity=2026-01-10   [join: exact_email]
  github     login=PERSON_2314_GITHUB_USERNAME, name=Ryan, email=frederick.stone@harmonygames.co, type=User, last_activity=2025-03-25   [join: exact_email]
  trello     id=4b4a68fc0fec0b254e4f9d8e, username=frederick.stone, fullName=Frederick Stone   [join: exact_name]
  confluence id=user_EMPLOYEE_0008, account_id=acct_EMPLOYEE_0008, email=frederick.stone@harmonygames.co, display_name=Frederick Stone, is_active=False, last_activity=2025-09-01   [join: exact_email]
  contacts   contact_id=175c0d7bc72ed244b944cb90, name=Frederick Stone, email=frederick.stone@harmonygames.co, job=Commercial Lead, Marketing & Business Development, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-10-24', 'gmail': '2025-11-13', 'gcal': '2026-01-14', 'gdrive': '2025-09-24', 'linear': '2026-01-10', 'github': '2025-03-25', 'confluence': '2025-09-01'}
  FLAG: GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frederick Stone)
#### resolve: Josh Dempsey
ENTITY email:josh.dempsey@harmonygames.co  name=Josh Dempsey  kind=person  emails=['josh.dempsey@harmonygames.co']
  slack      id=U7BFD5AC06F, name=josh, real_name=Josh Dempsey, email=josh.dempsey@harmonygames.co, is_bot=False, deleted=False, messages=0   [join: exact_email]
  gcal       calendar_id=josh.dempsey@harmonygames.co, owner_email=josh.dempsey@harmonygames.co, summary=Josh Dempsey — primary, events=1, last_event_before_clock=2023-06-08   [join: exact_email]
  linear     id=usr_7bfd5ac06fb6817f, email=josh.dempsey@harmonygames.co, name=josh.dempsey@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=75d14522897507b149b56a95, username=josh.dempsey, fullName=Josh Dempsey   [join: exact_name]
  confluence id=user_EMPLOYEE_0032, account_id=acct_EMPLOYEE_0032, email=josh.dempsey@harmonygames.co, display_name=Josh Dempsey, is_active=False   [join: exact_email]
  contacts   contact_id=a43a60d9fe7083014e2f455e, name=Josh Dempsey, email=josh.dempsey@harmonygames.co, job=Business Development Manager, is_user=False   [join: exact_email]
  absent from: gmail, gdrive, github
  last activity: {'gcal': '2023-06-08'}
  UNRESOLVED (token_link): same token number across services but no shared exact email/name: not joined  records=['gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'confluence.id=user_EMPLOYEE_0032', 'slack.id=EMPLOYEE_0032_SLACK_ID', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME']
#### resolve: Benjamin Clark
ENTITY email:benjamin.clark@harmonygames.co  name=Benjamin Clark  kind=person  emails=['benjamin.clark@harmonygames.co']
  slack      id=U5ADC6415B4, name=benjamin, real_name=Benjamin Clark, email=benjamin.clark@harmonygames.co, is_bot=False, deleted=False, messages=0   [join: exact_email]
  gcal       calendar_id=benjamin.clark@harmonygames.co, owner_email=benjamin.clark@harmonygames.co, summary=Benjamin Clark — primary, events=8, last_event_before_clock=2023-08-29   [join: exact_email]
  gdrive     share_recipient=benjamin.clark@harmonygames.co, files_shared_with=8   [join: exact_email]
  linear     id=usr_5adc6415b4ccdf3c, email=benjamin.clark@harmonygames.co, name=benjamin.clark@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=e200ff66e793f0d2aab53879, username=benjamin.clark, fullName=Benjamin Clark   [join: exact_name]
  confluence id=user_STAFF_8, account_id=acct_STAFF_8, email=benjamin.clark@harmonygames.co, display_name=Benjamin Clark, is_active=True   [join: exact_email]
  contacts   contact_id=160683a33e80876b5e3ca6b3, name=Benjamin Clark, email=benjamin.clark@harmonygames.co, job=Outside Counsel, Company Formation (not an employee), is_user=False   [join: exact_email]
  absent from: gmail, github
  last activity: {'gcal': '2023-08-29'}
#### resolve: Michelle Carter
ENTITY email:michelle.carter@harmonygames.co  name=Michelle Carter  kind=person  emails=['michelle.carter@harmonygames.co']
  slack      id=U1E2A024076, name=michelle, real_name=Michelle Carter, email=michelle.carter@harmonygames.co, is_bot=False, deleted=False, messages=0   [join: exact_email]
  gcal       calendar_id=michelle.carter@harmonygames.co, owner_email=michelle.carter@harmonygames.co, summary=Michelle Carter — primary, events=0   [join: exact_email]
  linear     id=usr_1e2a0240767eb09b, email=michelle.carter@harmonygames.co, name=michelle.carter@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=b7b148237a358f0eaf845a6d, username=michelle.carter, fullName=Michelle Carter   [join: exact_name]
  confluence id=user_STAFF_9, account_id=acct_STAFF_9, email=michelle.carter@harmonygames.co, display_name=Michelle Carter, is_active=True   [join: exact_email]
  contacts   contact_id=84ae5ae20147349f7ef89b77, name=Michelle Carter, email=michelle.carter@harmonygames.co, job=General Counsel, is_user=False   [join: exact_email]
  absent from: gmail, gdrive, github
  last activity: -
#### resolve: Segerstrale
no exact match for 'Segerstrale'
#### resolve: Schaeppi
no exact match for 'Schaeppi'
#### resolve: Arthur Schaeppi
no exact match for 'Arthur Schaeppi'
#### resolve: Sadik Enes Disli
no exact match for 'Sadik Enes Disli'
#### resolve: Enes
no exact match for 'Enes'
#### resolve: Eren Disli
no exact match for 'Eren Disli'
#### resolve: Haktan
no exact match for 'Haktan'
#### resolve: Disli
no exact match for 'Disli'
#### resolve: Nebojsa
no exact match for 'Nebojsa'
#### resolve: Deepak
no exact match for 'Deepak'
#### resolve: TOR Capital Limited
no exact match for 'TOR Capital Limited'
#### resolve: Griffin
no exact match for 'Griffin'
#### resolve: PERSON_3131
no exact match for 'PERSON_3131'
#### resolve: PERSON_2322
no exact match for 'PERSON_2322'
#### resolve: PERSON_3077
no exact match for 'PERSON_3077'
#### resolve: PERSON_5137
no exact match for 'PERSON_5137'
#### resolve: PERSON_0711
no exact match for 'PERSON_0711'
#### resolve: Julia Lawson
ENTITY email:julia.lawson@harmonygames.co  name=Julia Lawson  kind=person  emails=['julia.lawson@harmonygames.co']
  persona: julia_lawson - Product Manager / Product
  slack      id=EMPLOYEE_0005_SLACK_ID, name=Julia Lawson, real_name=Julia Lawson, email=julia.lawson@harmonygames.co, is_bot=False, deleted=False, messages=34047, first_post=2023-07-16, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=julia.lawson@harmonygames.co, threads=304, messages=359, first=2023-07-16, last=2026-02-13, thread_filename_alias=['jlawson@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=julia.lawson@harmonygames.co, owner_email=julia.lawson@harmonygames.co, summary=Julia Lawson — primary, events=792, last_event_before_clock=2026-01-16   [join: exact_email]
  gdrive     id=user_8140f09bf9f1, email=julia.lawson@harmonygames.co, display_name=julia.lawson@harmonygames.co, root_folders=['d_8140f09bf9f1b94cb8ee2d'], owned_items=45, last_modified=2025-12-09, files_shared_with=169   [join: exact_email]
  linear     id=usr_8140f09bf9f1b94c, email=julia.lawson@harmonygames.co, name=julia.lawson@harmonygames.co, is_active=True, last_activity=2025-11-05   [join: exact_email]
  github     login=PERSON_0005_GITHUB_USERNAME, name=Julia Lawson, email=julia.lawson@harmonygames.co, type=User, last_activity=2025-12-31   [join: exact_email]
  trello     id=793af7ca6940bf18eb516c75, username=julia.lawson, fullName=Julia Lawson   [join: exact_name]
  confluence id=user_EMPLOYEE_0005, account_id=acct_EMPLOYEE_0005, email=julia.lawson@harmonygames.co, display_name=Julia Lawson, is_active=True, last_activity=2025-09-21   [join: exact_email]
  contacts   contact_id=8140f09bf9f1b94cb8ee2dd7, name=Julia Lawson, email=julia.lawson@harmonygames.co, job=Product Manager, is_user=False   [join: exact_email]
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-13', 'gcal': '2026-01-16', 'gdrive': '2025-12-09', 'linear': '2025-11-05', 'github': '2025-12-31', 'confluence': '2025-09-21'}
#### resolve: Brian Foster
ENTITY email:brian.foster@harmonygames.co  name=Brian Foster  kind=person  emails=['brian.foster@harmonygames.co']
  persona: brian_foster - Game Engineer / Engineering
  slack      id=EMPLOYEE_0026_SLACK_ID, name=Brian Foster, real_name=Brian Foster, email=brian.foster@harmonygames.co, is_bot=False, deleted=False, messages=33142, first_post=2024-06-06, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=brian.foster@harmonygames.co, threads=362, messages=384, first=2024-06-05, last=2026-02-06, thread_filename_alias=['brian@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=brian.foster@harmonygames.co, owner_email=brian.foster@harmonygames.co, summary=Brian Foster — primary, events=455, last_event_before_clock=2025-12-29   [join: exact_email]
  gdrive     id=user_fc22d5941b2a, email=brian.foster@harmonygames.co, display_name=brian.foster@harmonygames.co, root_folders=['d_fc22d5941b2aeb5c03ad32'], owned_items=116, last_modified=2026-01-06, files_shared_with=135   [join: exact_email]
  linear     id=usr_fc22d5941b2aeb5c, email=brian.foster@harmonygames.co, name=brian.foster@harmonygames.co, is_active=True, last_activity=2025-12-03   [join: exact_email]
  github     login=PERSON_0180_GITHUB_USERNAME, name=Brian Foster, email=brian.foster@harmonygames.co, type=User, last_activity=2025-12-11   [join: exact_email]
  trello     id=d1cd0fef645a6c978ae1f068, username=brian.foster, fullName=Brian Foster   [join: exact_name]
  confluence id=user_EMPLOYEE_0026, account_id=acct_EMPLOYEE_0026, email=brian.foster@harmonygames.co, display_name=Brian Foster, is_active=True   [join: exact_email]
  contacts   contact_id=fc22d5941b2aeb5c03ad32fa, name=Brian Foster, email=brian.foster@harmonygames.co, job=Game Engineer, is_user=False   [join: exact_email]
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-06', 'gcal': '2025-12-29', 'gdrive': '2026-01-06', 'linear': '2025-12-03', 'github': '2025-12-11'}
#### resolve: EMPLOYEE_0032
ENTITY email:EMPLOYEE_0032_EMAIL  name=None  kind=unidentified  emails=['EMPLOYEE_0032_EMAIL']
  gmail      mailbox=EMPLOYEE_0032_EMAIL, threads=3, messages=3, first=2024-08-20, last=2025-10-24   [join: exact_email]
  gdrive     id=user_9cc553d0ac03, email=EMPLOYEE_0032_EMAIL, display_name=EMPLOYEE_0032_EMAIL, root_folders=['d_9cc553d0ac034a53de5e27'], owned_items=2, last_modified=2024-12-19, files_shared_with=117   [join: exact_email]
  linear     id=usr_EMPLOYEE_0032, email=EMPLOYEE_0032_EMAIL, name=EMPLOYEE_0032_NAME, is_active=True, last_activity=2025-10-24   [join: exact_email]
  contacts   contact_id=d4a339f7f6aafffdc2dabb9a, name=EMPLOYEE_0032, email=EMPLOYEE_0032_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gcal, github, trello, confluence
  last activity: {'gmail': '2025-10-24', 'gdrive': '2024-12-19', 'linear': '2025-10-24'}
  FLAG: tokenized Gmail mailbox: the data does not prove which person owns it
  UNRESOLVED (token_link): same token number across services but no shared exact email/name: not joined  records=['gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'confluence.id=user_EMPLOYEE_0032', 'slack.id=EMPLOYEE_0032_SLACK_ID', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME']
#### resolve: cameron@harmonygames.co
ENTITY email:cameron@harmonygames.co  name=None  kind=person  emails=['cameron@harmonygames.co']
  gdrive     share_recipient=cameron@harmonygames.co, files_shared_with=1   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence, contacts
  last activity: -
#### resolve: PERSON_2314
no exact match for 'PERSON_2314'
  candidate: email:frederick.stone@harmonygames.co  Frederick Stone  ['frederick.stone@harmonygames.co']
#### resolve: Thomas Baker
ENTITY email:thomas.baker@harmonygames.co  name=Thomas Baker  kind=person  emails=['thomas.baker@harmonygames.co']
  slack      id=U05F0A0D12F, name=thomas, real_name=Thomas Baker, email=thomas.baker@harmonygames.co, is_bot=False, deleted=False, messages=0   [join: exact_email]
  gcal       calendar_id=thomas.baker@harmonygames.co, owner_email=thomas.baker@harmonygames.co, summary=Thomas Baker — primary, events=1, last_event_before_clock=2023-06-12   [join: exact_email]
  gdrive     share_recipient=thomas.baker@harmonygames.co, files_shared_with=4   [join: exact_email]
  linear     id=usr_05f0a0d12f2ad71f, email=thomas.baker@harmonygames.co, name=thomas.baker@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=41044d46bbac2b9a1aedede6, username=thomas.baker, fullName=Thomas Baker   [join: exact_name]
  confluence id=user_STAFF_10, account_id=acct_STAFF_10, email=thomas.baker@harmonygames.co, display_name=Thomas Baker, is_active=True   [join: exact_email]
  contacts   contact_id=cnt_05f0a0d12f2a, name=Thomas Baker, email=thomas.baker@harmonygames.co, job=General Counsel, is_user=False   [join: exact_email]
  absent from: gmail, github
  last activity: {'gcal': '2023-06-12'}
```

## 2 Cohort spine

**Rule.** every holder on a Carta record, live or lapsed, other than the three founders: 12 Series Seed lines and 14 option-only lines, one project issue each. Key: holder issue. Size 26. Requester-confirmed `cohort_exception`: the company has 29 holders on Carta, 26 of them non-founders; no honest cohort of 40 exists and padding one fails on its own.

| Surface | Tool | Per record | Records | Requirement | Why no bulk / short circuit |
|---|---|---|---|---|---|
| linear | linear_list_comments | 1.0 | 26 | R5 | linear_list_issues returns titles and states but no comments; each issue's notes need their own read / each issue's notes carry that holder's own contact history; skipping the read leaves the row's last contact and any stale claim unchecked |
| gmail | gmail_search_messages (per holder address) | 1.0 | 12 | R4 | gmail_search_messages returns ids only and no mail lists who was told; each address needs its own search / only a per-address search finds a personal message; the Feb 12 list and the letters cover different people |
| gmail | gmail_get_thread (notice, letter, last contact) | 1.0 | 26 | R2 | the notices are one per thread and the date is only in the body; the owner list has no dates / the last day exists nowhere else, so the notice cannot be skipped for an option line |
| slack | slack_search_public_and_private (per holder name) | 1.0 | 12 | R4 | no channel holds every holder's contact; DMs need a name search / a personal DM counts as told and shows up nowhere else |
| gdocs | gdocs_get_document_text (agreement or consent) | 1.0 | 14 | R3 | agreements and consents are separate documents with no index / the grant size on an agreement separates a holder's stock from options where the owner list merges them |

Sum of per-record calls 90.0, above the 85 floor. Linear comments buy calls, not misses: they are read every time (research/s4_carrier_formats.md section A), so no deciding fact sits only there. They carry neutral contact history, and stale figures met first.

**Classification predicate (closed).** Wording is neutral on purpose: the first draft read as a trap index (run_sim LEAK-1), so no sentence names a case or a carrier, and the rule is split across records. Carried by H1 f_a37b403d5200d4f0a31d31 unless marked:
- Carta is the record. If a line's last day has passed, it holds nothing.
- One row per issue on the sheet and at most one note per person. The three of us get no row, only the totals.
- Told means a written message about the closing, sent to them directly and delivered, from one of the three of us (a post in a channel doesn't count); for a fund, its partner.
- Everyone still holding something gets what they are owed: the closing if they have not been told, their last day if they have one. Whoever's last day comes first goes first.
- Anything they asked about their holding that we never answered gets answered in their note.
- Family (Leonard's reply under his Feb 12 list, C0ADGSZKR3R/1770949310.220519, not H1): one note to whoever has always handled it for a family covers the rest of the family's lines, which need no note of their own.
- States (project description ec2ea957-fc8e-4958-b809-0fb735b1e916, ENG-2438): Canceled where the line holds nothing; otherwise Todo where its own note is waiting for Leonard, and Done where it isn't. On every issue with no note of its own, Canceled included, say why.

Labels in the holder sheet: H1 gives Nothing, Already told, Closing (First note here), Last day (Date note), Closing and last day (Full note); the reply adds Covered.

**Applied to all 26.** Titles use the forms the owner list shows, so no surname links the family: [PERSON_NAME_52949] is Enes Disli, [PERSON_NAME_27652] is Eren Disli.

| Issue | Holder | Carta id | Owed |
|---|---|---|---|
| ENG-2438 | Griffin Gaming Partners II, L.P. | SSP-01 | Already told |
| ENG-2439 | Griffin Gaming Partners II Side Fund, L.P. | SSP-02 | Already told |
| ENG-2440 | Segerstråle | SSP-03 | Already told |
| ENG-2441 | Schaeppi | SSP-04 | First note |
| ENG-2442 | Bergmann | SSP-05 | First note |
| ENG-2443 | [PERSON_NAME_52949] | SSP-06/08 | First note |
| ENG-2444 | Patrick Lewis | SSP-06/08 | Covered |
| ENG-2445 | [PERSON_NAME_27652] | SSP-07 | Covered |
| ENG-2446 | Nebojsa | SSP-09 | Already told |
| ENG-2447 | Matthew Collins | SSP-10 | Already told |
| ENG-2448 | TOR Capital Limited | SSP-11 | First note |
| ENG-2449 | Deepak | SSP-12 | First note |
| ENG-2450 | Julia Lawson | ES-1 | Date note |
| ENG-2451 | [PERSON_NAME_0100] | ES-2 | Nothing |
| ENG-2452 | Calvin Price | ES-3 | Full note |
| ENG-2453 | Claire Morgan | ES-4 | Date note |
| ENG-2454 | Douglas | ES-5 | Nothing |
| ENG-2455 | Victor Barnes | ES-6 | Nothing |
| ENG-2456 | Marcus Bennett | ES-7 | Date note |
| ENG-2457 | Owen Baker | ES-12 | Full note |
| ENG-2458 | Martin Walsh | ES-13 | Date note |
| ENG-2459 | Vincent Parker | ES-14 | Full note |
| ENG-2460 | Brian Foster | ES-15 | Date note |
| ENG-2461 | [PERSON_NAME_2768] [PERSON_NAME_0011] | ES-16 | Nothing |
| ENG-2462 | Frederick Stone | ES-17 | Nothing |
| ENG-2463 | Oliver Brooks | ES-18 | Full note |

Counts: Already told 4, First note 6, Covered 2, Date note 6, Full note 2, Nothing 6 = 26. Notes written: 6 First + 6 Date + 2 Full = 14. Reason comments: 4 + 2 + 6 = 12. States: Canceled 6, Todo 14, Done 6. Issues are keyed by Linear id because SSP-06 and SSP-08 cannot be told apart on the record. Holder-of-record names on three lines differ between Carta and the signed schedule, so legal names are never graded (research/s1_signed_pdfs.md section D).

**Shortcut audit.** The owner list leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com> hands 27 lines in one read, in three copies including `f_414596b0a9d698267dd1e1`, so difficulty never rests on the census. `Termination details` returns the 14 notices in one search, and the batch read collapses them. Neither reaches told state, the letter join, the family link or the as-of date.

**Boundary records.** ES-14 (a last day 7 days out, no letter); ES-18 (no letter, a channel post); ES-17 (the largest non-Griffin line, holds nothing); ES-1, 4, 15 (terminated exactly on the as-of date).

## 3 Hidden authorities

| Id | Authority | Home | Governs | Decoy | Decoy scope | Findability |
|---|---|---|---|---|---|---|
| H1 | my close-out notes | gdocs f_a37b403d5200d4f0a31d31 | R4, R5, R12 | earlier notes f_762c60832854d3e7a7f7df (same service) | older version in T18's version_records | Drive search 'close-out notes' (planned) |
| H2 | Carta's termination details | gmail leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv> and 13 siblings | R2 | term sheet f_11040fe5d66821bd6951aa | older version in T3's version_records | gmail search 'Termination details', 14 hits |
| H4 | KPMG's FY25 request | gmail leonard.hayes@harmonygames.co/1857029474983245439 | R8 | FY24 request leonard.hayes@harmonygames.co/<LV3PR19MB8524A7F34357829DDCA90153CA302@LV3PR19MB8524.namprd19.prod.outlook.com> (same service) | fiscal year: FY24 as of Sep 30, 2024 against FY25 | gmail search 'Audit Request' (planned) |

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| AN1 | the investor email draft in #winddown | C0ADGSZKR3R/1770664700.848759 |
| AN2 | the holder project in Linear | ec2ea957-fc8e-4958-b809-0fb735b1e916 (issues ENG-2438 to ENG-2463) |
| AN3 | KPMG's audit request for Griffin | leonard.hayes@harmonygames.co/1857029474983245439 |

**Hub.** The project description ec2ea957-fc8e-4958-b809-0fb735b1e916, in Leonard's voice, delegates by role: his close-out notes, what Sunset asked for. It names no location. H2 is found by search. Origin of the project is stated in C0ADGSZKR3R/1770938120.410229, on the base line 'linear we keep during transition' (C0ADGSZKR3R/1770933601.686309).

**Amendment.** K14 C0ADGSZKR3R/1770949310.220519: in a reply under his Feb 12 list, after the notes doc, Leonard adds Arthur to the sharing and gives the family sentence; the rest stands. H1 names that message twice ('where I left things today', 'reply under my list in #winddown') and every run must write there.

**Non-authoritative distractors.** The Feb 12 list read as a to-do (T6), the deck (T19), the draft sheet (T20), the Done card (T21).

| Id | Service | Container | Kind | Chain | Delegated by | Delegation quote (verbatim) | Requirements |
|---|---|---|---|---|---|---|---|
| K1 | slack | C0ADGSZKR3R/1770664700.848759 | requirement | AN1 | C0ADGSZKR3R/1770664700.848759 | "I will send periodic updates as we complete the major steps" | R10 |
| K2 | slack | C0ADGSZKR3R/1770664924.520089 | requirement | AN2 > K6 > K7 | f_a37b403d5200d4f0a31d31 | "the reach-out I promised" | R6 |
| K4 | slack | C0ADGSZKR3R/1770934638.035469 | requirement | AN2 > K6 > K7 | f_a37b403d5200d4f0a31d31 | "where I left things today" | R4 |
| K5 | gsheets | f_31115ddb6ed866f2b10d60 | requirement | AN2 > K6 > K7 | f_a37b403d5200d4f0a31d31 | "the investor email on the Task List" | R10 |
| K6 | linear | linear:project/ec2ea957-fc8e-4958-b809-0fb735b1e916 | delegation | AN2 | ec2ea957-fc8e-4958-b809-0fb735b1e916 | "one issue per holder on Carta, live or lapsed" | R1, R11 (ENG-2438) |
| K7 | gdocs | f_a37b403d5200d4f0a31d31 | requirement | AN2 > K6 | ec2ea957-fc8e-4958-b809-0fb735b1e916 | "my close-out notes have how each holder gets handled" | R4, R5, R12 (ENG-2438) |
| K8 | gmail | leonard.hayes@harmonygames.co/1857034369525983506 | requirement | AN2 > K6 | ec2ea957-fc8e-4958-b809-0fb735b1e916 | "what Sunset asked for" | R1, R2, R3, R9 (ENG-2438) |
| K9 | gmail | leonard.hayes@harmonygames.co/1857029474983245439 | requirement | AN3 | leonard.hayes@harmonygames.co/1857029474983245439 | "as of December 31, 2025" | R8 |
| K10 | trello | 698e5a10c3f24b7e9d16a0e4 | destination | AN2 > K6 > K7 | f_a37b403d5200d4f0a31d31 | "the holder sheet comes first" | R13 |
| K11 | gcal | evt_6f1a2c9e4b7d3a58c0e1d2 | requirement | AN2 > K6 > K7 | f_a37b403d5200d4f0a31d31 | "notes ready for me by Tuesday" | R6 |
| K12 | gslides | f_75dddccabb26eeea4842c8 | format | AN2 > K6 > K7 | f_a37b403d5200d4f0a31d31 | "the update outline" | R10 |
| K13 | gdrive | d_601064334a0b493022fe83 | destination | AN2 > K6 > K7 | f_a37b403d5200d4f0a31d31 | "everything goes in the close-out folder" | R13 |
| K14 | slack | C0ADGSZKR3R/1770949310.220519 | amendment | AN2 > K6 > K7 | f_a37b403d5200d4f0a31d31 | "reply under my list in #winddown" | R6, R13 |
| K15 | slack | C0ADGSZKR3R/1770938120.410229 | delegation | AN2 > K6 | ec2ea957-fc8e-4958-b809-0fb735b1e916 | "as I said in #winddown" | R11 (ENG-2438) |

## 5 Chains and trap register

| Chain | Root cause | Ends in | Hops |
|---|---|---|---|
| C1 | A17 | R3 | gmail leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com>: owner list: 86,470, 81,383, 31,536 twice > gdocs f_6a37227593d0977fdbdd7a: advisor table: 61,038, 30,518, 6,104, 6,104 > gdocs f_11040fe5d66821bd6951aa: term sheet total 3,051,879 ties only after subtracting > gmail leonard.hayes@harmonygames.co/1782897835407336831: Carta: option grants ES-9 and ES-11 (NEW digest of Nov 20, 2023: ES-8 and ES-10 accepted) |
| C2 | A24 | R5 | slack C0ADGSZKR3R/1770841239.761999: Leonard: all termination letters are sent > gmail leonard.hayes@harmonygames.co/<CAPBs_a68Agj+37mZ6abeW5KEKTh00he+mgOpLP2FrpDjeO-37Q@mail.gmail.com>: six letters to six recipients > gmail leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv>: eight Carta entries on Feb 12 > gmail leonard.hayes@harmonygames.co/<CAEH8bLxfNq9vp7-VSMQdpetPWQxBhv2pcPE=xj=oX9c8MxNFtA@mail.gmail.com>: ES-14 resigned in November, before any letter |
| C3 | A25 | R4 | slack C0ADGSZKR3R/1770934638.035469: angels still to do on Feb 12 > slack D04UC0UEN2V/1770664988.379119: Feb 9 DM told Segerstrale > gmail leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>: NEW Robert told Nebojsa on Feb 12 |
| C4 | A19 | R8 | gmail leonard.hayes@harmonygames.co/1857029474983245439: NEW as-of date Dec 31, 2025 > gmail leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv>: effective Nov 21, entered Feb 12 > gmail leonard.hayes@harmonygames.co/<177093559600.10.6851662374290149851@notifications-email-sending-worker-5fc9459db-b2dtx>: effective Jan 30: full grant still held at Dec 31 > gdocs f_6a37227593d0977fdbdd7a: advisor grants count at every date |
| C5 | A11 | R9 | gdocs f_966445655f653d26dc8537: board of four in the financing documents > gmail leonard.hayes@harmonygames.co/<CAMy0Hx1va3q4zH2HyPiqfm8Je2fm5A=JHKf8LrXWb12z2FHr6w@mail.gmail.com>: Matthew resigned May 1, 2025 > gmail leonard.hayes@harmonygames.co/<BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com>: Griffin's director resigned Feb 12, 2026 |
| C7 | A7 | R6 | gmail leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com>: three lines, no shared surname > gmail leonard.hayes@harmonygames.co/<A658306E-3D13-458C-A311-95454D575822@librasoftworks.com>: Enes supplies all three addresses > gmail leonard.hayes@harmonygames.co/<0CDD5A07-0BE6-4909-8188-93E10FBF4E16@librasoftworks.com>: all three brothers wired > linear ENG-2444: the project shows a name with no link to the family |
| C9 | A24 | R4 | slack C0ADGSZKR3R/1770841239.761999: Leonard: all termination letters are sent > gmail leonard.hayes@harmonygames.co/<CAPBs_a5HKTOGV3nwn6iyxz8GhwLGRaF_Gs-uii3x7tVQ9eTfQQ@mail.gmail.com>: Owen's letter went to his personal address > gmail leonard.hayes@harmonygames.co/<698ce305.050a0220.3b7f1c.9d2e.GMR@mx.google.com>: NEW the mail system: that address is inactive, not delivered |
| C10 | A11 | R2 | linear ENG-2452: Calvin's issue: his address, 'No mail with that address before Feb' > gmail leonard.hayes@harmonygames.co/<176175436721.10.9685252272573766647@notifications-email-sending-worker-6b65bf6cf7-dg8x2>: Carta: ES-3 last day Jan 24, 2026 > gmail leonard.hayes@harmonygames.co/<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz@mail.gmail.com>: NEW from the issue's address on Feb 3: Carta's Jan 23 update moved the last day to Feb 20, 2026 |
| C11 | A7 | R4 | linear ENG-2447: Husnu Matthew Collins at his work address; last mail Oct 28, 2025 > gmail leonard.hayes@harmonygames.co/<CAPBs_aLeDrdRoqOb0LrQ1AfGvbpmR-YdoG8A6PGmPay5Sc-ng=@mail.gmail.com>: NEW Feb 12: Leonard tells 'Akin' at a personal address that the company is closing > gmail leonard.hayes@harmonygames.co/<CAMy0Hx2S+a4q+PUkFZM1ifrcEKv-y7AWWtQHrEsWg2qRxvFo3Q@mail.gmail.com>: Matthew Collins signs his own mail 'akin' |
| C8 | A9 | R12 | slack C51ECE5102ED/1770903714.600249: Claire asks about equity > slack C51ECE5102ED/1770906363.694689: Leonard's replies answer the deletion question only > gmail leonard.hayes@harmonygames.co/<CAPBs_a68Agj+37mZ6abeW5KEKTh00he+mgOpLP2FrpDjeO-37Q@mail.gmail.com>: the letter's equity paragraph gives no date |

| Trap | Family | Req | Records | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | exact_predicate | R3 | leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com>, gdocs:data.json /docs_documents/262 | the owner list's 86,470, 81,383 and 31,536 lines are stock, so Series Seed sums too high or the difference goes unnoticed | Due Diligence Disclosures' advisor table: four angels also hold advisor options, 103,764 in all, and only the subtraction ties to the term sheet's 3,051,879 | the owner list is one read and carries every line; the advisor table is a 2023 doc with no holder word in its title |
| T2 | stale_summary | R1 | leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com>, C04UEQVDVB7/1732646280.941869 | the Nov 2024 owner list is the current holder list, with option grants as shares and Griffin as one line | Carta's certificates and awards: option lines are not stock, and Griffin is two fund lines | a search on any holder figure returns the owner list first |
| T3 | superseding | R2 | gdocs:data.json /docs_documents/40, leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv> | options outstanding are the term sheet's 268,772 | the term sheet is a Jan 22 snapshot: the October windows closed Jan 24-28 (ES-3's was moved to Feb 20) and the Feb 12 entries cut unvested grants, leaving 164,114 live at the clock | - |
| T4 | done_gap | R5 | C0ADGSZKR3R/1770841239.761999, C07C2866011/1770837454.464209, leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv>, leonard.hayes@harmonygames.co/<CAPBs_a68Agj+37mZ6abeW5KEKTh00he+mgOpLP2FrpDjeO-37Q@mail.gmail.com> | 'All termination letters are sent' means every Carta termination has a letter, so ES-14 and ES-18 were told like the others | Six letters exist against eight Feb 12 Carta entries; matching letter recipients to Carta addresses leaves ES-14 and ES-18 with no letter | Leonard's own #winddown line says the letters are done; the gap shows only by joining recipients to Carta |
| T5 | conclusion_stop | R6 | C0ADGSZKR3R/1770935621.095649, leonard.hayes@harmonygames.co/<CAPBs_a68Agj+37mZ6abeW5KEKTh00he+mgOpLP2FrpDjeO-37Q@mail.gmail.com> | 'Carta terminations are done' closes the option side, so nothing more is owed to live holders | The letters only promise a Carta mail; no holder-facing record gives any live holder a last day, so a date note is still owed | - |
| T6 | completion_elsewhere | R4 | C0ADGSZKR3R/1770934638.035469, D04UC0UEN2V/1770664988.379119 | Leonard's Feb 12 list says the angels are still to do, so Segerstråle gets a first note | Leonard's Feb 9 DM told him personally | #winddown is read first; the DM is off every channel listing |
| T7 | completion_elsewhere | R4 | leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>, C0ADGSZKR3R/1770934638.035469 | no angel but Segerstråle has been told, so Nebojsa gets a first note | NEW Robert's Feb 12 reply on his old thread with Nebojsa, Leonard copied, tells him about the closing | a reply on a 2023 thread about a wire, with no holder word in its subject |
| T8 | near_miss_mention | R5 | D09R59580EM/1762285888.654689 | Tor was told in November, so he needs nothing | The Nov 4 DM warned of about three months of runway; nothing says the company is closing, so Tor still gets a first note | - |
| T10 | superseding | R9 | gdocs:data.json /docs_documents/381, leonard.hayes@harmonygames.co/<CAMy0Hx1va3q4zH2HyPiqfm8Je2fm5A=JHKf8LrXWb12z2FHr6w@mail.gmail.com>, leonard.hayes@harmonygames.co/<BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com> | the board is the four named in the financing documents | Matthew's May 1, 2025 mail and Phil's Feb 12, 2026 mail leave Leonard and Robert | - |
| T11 | authority | R9 | leonard.hayes@harmonygames.co/<BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com>, gdocs:data.json /docs_documents/360 | Griffin's director resigned, so Griffin has nothing left to sign | The charter's protective provision is a vote of the preferred, not a board seat; Griffin holds 90.0 % of the preferred | - |
| T12 | effective_date | R8 | leonard.hayes@harmonygames.co/1857029474983245439, leonard.hayes@harmonygames.co/<LV3PR19MB8524A7F34357829DDCA90153CA302@LV3PR19MB8524.namprd19.prod.outlook.com>, leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv> | KPMG gets today's holdings, or last year's as-of date | NEW FY25 request fixes Dec 31, 2025 and a generic cut-off regardless of when things were recorded; entries made in February carry earlier effective dates | - |
| T13 | entity_collision | R6 | C0ADGSZKR3R/1770949310.220519, leonard.hayes@harmonygames.co/<A658306E-3D13-458C-A311-95454D575822@librasoftworks.com>, leonard.hayes@harmonygames.co/<0CDD5A07-0BE6-4909-8188-93E10FBF4E16@librasoftworks.com> | three record holders mean three separate first notes | Enes has handled everything for the three Disli lines; NEW Leonard's reply under his Feb 12 list says one note to whoever has always handled it for a family covers the rest | neither the owner list nor the issue titles show a shared surname: 'Patrick Lewis' reads as unrelated |
| T14 | scope_alias | R1 | leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com> | 'Patrick' is one person | The wires and owner list separate Bergmann from the Disli line | - |
| T15 | distractor (lookalike_entity) | R2 | leonard.hayes@harmonygames.co/<176175429549.10.8466995912642267217@notifications-email-sending-worker-6b65bf6cf7-gcpxf> | the roster's co-founder holds a founder's stake | ES-17 is an option line that lapsed; Frederick Stone holds nothing at the clock | - |
| T16 | distractor (near_duplicate_record) | R2 | leonard.hayes@harmonygames.co/<CAPBs_a6mwZj_4JRyPpidJCWgK9auo+34NVhirFGhKMHi3d5OmA@mail.gmail.com>, leonard.hayes@harmonygames.co/<176175429549.10.8466995912642267217@notifications-email-sending-worker-6b65bf6cf7-gcpxf> | ES-17's letter figures (34,409, Jan 22) are the record | The letter itself says Carta shows the exact numbers: 34,439 and Jan 28, both before the clock | - |
| T17 | synthesis_omission | R12 | C51ECE5102ED/1770903714.600249 | Claire's note only needs her date | Her Feb 12 group-DM question about equity was never answered, and the closed rule says an open question on a live line is answered in the note | the group DM is not a channel; Leonard's reply in it answers a different question |
| T18 | superseding | R5 | f_762c60832854d3e7a7f7df, f_a37b403d5200d4f0a31d31 | the earlier notes doc still governs | NEW the later close-out notes replace it | - |
| T19 | distractor (stale_summary) | R10 | f_75dddccabb26eeea4842c8 | the outline deck's holder count is current | NEW deck quotes the Nov 2024 owner list, attributed and dated | - |
| T20 | distractor (partial_listing) | R1 | f_5ecaa967db3adcfa440b09 | the draft sheet is the holder list | NEW partial sheet dated before the Carta entries | - |
| T21 | distractor (already_done) | R10 | 68c5a49e8491a9d7faf869d0 | the investor update is done because its card sits in Done | the card has no description and no update followed it | - |
| T22 | distractor (scope_adjacent) | R8 | leonard.hayes@harmonygames.co/<LV3PR19MB8524A7F34357829DDCA90153CA302@LV3PR19MB8524.namprd19.prod.outlook.com> | last year's as-of date applies | FY24 was Sep 30, 2024; the FY25 request names its own date | - |
| T23 | done_gap | R4 | leonard.hayes@harmonygames.co/<698ce305.050a0220.3b7f1c.9d2e.GMR@mx.google.com>, C0ADGSZKR3R/1770841239.761999, leonard.hayes@harmonygames.co/<CAPBs_a5HKTOGV3nwn6iyxz8GhwLGRaF_Gs-uii3x7tVQ9eTfQQ@mail.gmail.com> | 'All termination letters are sent' and Owen's Feb 11 letter mean Owen was told, so his note gives his date only | NEW a delivery failure came back on Owen's letter nine seconds after it went: it never reached him, so he is untold and is owed the closing and his last day | the letters are single-message threads read by message id; the failure is the second message in Owen's thread, from the mail system, with no holder word in its subject |
| T25 | scope_alias | R4 | leonard.hayes@harmonygames.co/<CAPBs_aLeDrdRoqOb0LrQ1AfGvbpmR-YdoG8A6PGmPay5Sc-ng=@mail.gmail.com>, leonard.hayes@harmonygames.co/<CAMy0Hx2S+a4q+PUkFZM1ifrcEKv-y7AWWtQHrEsWg2qRxvFo3Q@mail.gmail.com> | no mail went to Collins's address after the closing, so he is untold and gets a first note | NEW Leonard's Feb 12 mail to 'Husnu Akin' at a personal address tells him about the closing; Carta's SSP-10 holder is Husnu Matthew Collins and he signs his own mail 'akin', so he is already told | the mail names only 'Akin' and an address on no other record; the issue carries Collins's work address and its comment shows no mail since Oct 28 |
| T24 | superseding | R2 | leonard.hayes@harmonygames.co/<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz@mail.gmail.com>, leonard.hayes@harmonygames.co/<176175436721.10.9685252272573766647@notifications-email-sending-worker-6b65bf6cf7-dg8x2> | Carta's Oct 29 termination notice gives ES-3's last day as Jan 24, so the line holds nothing | NEW Calvin forwarded Carta's Jan 23 update to Leonard on Feb 3: the last day moved to Feb 20, so the line is live, he is owed the closing and his date, and he goes first | a holder's forward in its own thread with no Carta sender or message id; the obvious Carta search returns Carta's own notices |

**Hardness v2 selection** (`Hardness_Mastery.md` §13, guide Part 5). Trap 1, proving done: LETTER, wrong source C0ADGSZKR3R/1770841239.761999 (Leonard, Feb 11), beaten by six letters joined to eight entries (leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv>); flips C_ES14, C_ES18, N_Vincent. Trap 9, work already done: TOLD, wrong source C0ADGSZKR3R/1770934638.035469, beaten by D04UC0UEN2V/1770664988.379119 and NEW leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>; flips C_SEG, C_NEB. Trap 7 and 8: ADV. Trap 4 and 8: ASOF. Trap 6: FAM. Trap 5: SIDE. Trap 2: BOARD. Trap 3: ASK.

### Mechanism portfolio (S5a)

Grounded candidates considered (16), with ledger priors (`hardness_ledger.py priors --model claude-opus-5-5`; this machine's ledger holds one record per family, n_eff 1):

| Candidate | Anchor record | Coupling | Prior (Opus 5.5) | Findability term | Slots / reason |
|---|---|---|---|---|---|
| ADV (kept) | leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com> > f_6a37227593d0977fdbdd7a | merged line > stock count > total and every note | A17 Beta(1,2) mean 0.33 | owner list figure, 'advisor' | K1, K4-K8, P1 |
| LETTER (kept) | C0ADGSZKR3R/1770841239.761999 > six letters > eight Carta entries | a founder's done line > who is told > class, note and order | A24 Beta(1,2) mean 0.33 | 'Termination details', recipients | C_ES14, C_ES18, N_Vincent, D6 |
| TOLD (kept) | C0ADGSZKR3R/1770934638.035469 > D04UC0UEN2V/1770664988.379119; NEW leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com> | list says open > a personal record elsewhere > class and note count | A25 Beta(1,2) mean 0.33 | holder address, name | C_SEG, C_NEB, TC_SEG |
| ASOF (kept) | NEW leonard.hayes@harmonygames.co/1857029474983245439 > leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv> | as-of date > effective dates > every option line | A19 Beta(1,1), no record | 'Audit Request' | A1, A2, AL_* |
| FAM (kept) | leonard.hayes@harmonygames.co/<A658306E-3D13-458C-A311-95454D575822@librasoftworks.com> > leonard.hayes@harmonygames.co/<0CDD5A07-0BE6-4909-8188-93E10FBF4E16@librasoftworks.com> | one contact > three lines change call | A7 Beta(1,1), no record | 'brothers' | F1-F5; the rule sits in a DM, not the notes |
| SIDE (retired at injection: the close-out notes name the side letter's holders) | f_6201c7027d02997bfb2c84 > leonard.hayes@harmonygames.co/<CAPBs_a46H9SCR=PBn1EP4RvCL+HO3XqOma4mTNu0WdnWv17ZuA@mail.gmail.com> | Drive copy > signed chain > route for a second holder | A15 Beta(1,2) mean 0.33 | 'side letter' | S3 only: Tor's route is on the Drive copy, so S1 and S2 are plain reads |
| BOARD (kept) | f_966445655f653d26dc8537 > leonard.hayes@harmonygames.co/<CAMy0Hx1va3q4zH2HyPiqfm8Je2fm5A=JHKf8LrXWb12z2FHr6w@mail.gmail.com> > leonard.hayes@harmonygames.co/<BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com> | document list > resignations > directors and the vote | A11 Beta(1,2) mean 0.33 | 'board' | B1, L6, G2 |
| ASK (kept) | C51ECE5102ED/1770903714.600249 | unanswered question > note content | A9 Beta(1,1), no record | 'equity' | Q1 |
| BOUNCE (rev2, new) | C0ADGSZKR3R/1770841239.761999 > leonard.hayes@harmonygames.co/<CAPBs_a5HKTOGV3nwn6iyxz8GhwLGRaF_Gs-uii3x7tVQ9eTfQQ@mail.gmail.com> > NEW leonard.hayes@harmonygames.co/<698ce305.050a0220.3b7f1c.9d2e.GMR@mx.google.com> | a done line and a sent letter > the mail system's failure notice in the letter's thread > told, class, note | A24 (prior from the ledger) | 'Delivery Status Notification', Owen's address | C_ES12, TC_ES12, C_DATE |
| ALIAS (rev2, new) | ENG-2447 > NEW leonard.hayes@harmonygames.co/<CAPBs_aLeDrdRoqOb0LrQ1AfGvbpmR-YdoG8A6PGmPay5Sc-ng=@mail.gmail.com> > leonard.hayes@harmonygames.co/<CAMy0Hx2S+a4q+PUkFZM1ifrcEKv-y7AWWtQHrEsWg2qRxvFo3Q@mail.gmail.com> | the issue's work address shows no mail > a founder's mail to 'Akin' at a personal address > Collins signs 'akin' | A7 (prior from the ledger) | 'Akin', Collins's names | C_COL, TC_COL, LC_Col, C_FIRST |
| EXT (rev2, new) | leonard.hayes@harmonygames.co/<176175436721.10.9685252272573766647@notifications-email-sending-worker-6b65bf6cf7-dg8x2> > NEW leonard.hayes@harmonygames.co/<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz@mail.gmail.com> | Carta's termination notice > Carta's later update, forwarded by the holder from his issue address > live line, note, who goes first | A11 (prior from the ledger) | Calvin's issue address, 'option grant' | C_ES3, TC_ES3, P_first, N_Calvin, D6, P1 |
| OPT (kept as channel CH-LIVE, not a rule) | C0ADGSZKR3R/1770934638.035469 names Carta > 14 notices | pointed: Leonard's own list says 'Carta terminations', and C5 shows pointed traps caught 6 of 6 | none: complexity channel | 'Termination details' | P_lapsed_*, P_FRED |
| CAP (rejected) | seeded TLAS request; D09R59580EM/1762285888.654689 | Tor's cap table on request; the smallest modelled effect, and a planted look; Tor's Nov 4 DM (T8) replaces it as a free base fact | none | - | - |
| WATERFALL (rejected) | f_11040fe5d66821bd6951aa and f_90c029015fc474199cf736 | dollars per holder need residual cash, which NB-3 and NB-4 block | none | - | - |
| FD PERCENT (rejected) | leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com> | four fully diluted bases and two reserves in the base, two of them self-consistent: a fork with no settling record, so counts only | none | - | - |
| ROUTE to work address (rejected) | leonard.hayes@harmonygames.co/1856861323365646598 | ES-7's letter went to a mailbox archived by Feb 15, but no personal address is on record and addresses are never graded | none | - | - |

Selected, one per future solver rule (10, inside the k <= 8 engine limit):

| Rule | Mechanism | Nodes | Anchor record | Natural reading | Controls | Over-application | Decides |
|---|---|---|---|---|---|---|---|
| ADV | A17 | T1, T2, C1 | f_6a37227593d0977fdbdd7a | the owner list's figure is the holder's stock | ENG-2441; ENG-2442 | adv_over: subtracts an advisor grant from a plain $25,000 line | K1, K4, K5, K6, K7, K8 |
| LETTER | A24 | T4, T5, C2 | C0ADGSZKR3R/1770841239.761999 | every Carta termination had a letter, so every live option holder has been told | ENG-2450; ENG-2460 | letter_over: treats a holder with a real letter as untold | C_ES14, C_ES18, C_DATE, TC_ES14, TC_ES18, N_Vincent |
| TOLD | A25 | T6, T7, T8, C3 | D04UC0UEN2V/1770664988.379119 | the Feb 12 list means no angel has been told | ENG-2448 | told_over: treats Tor's November runway warning as being told | C_SEG, C_NEB, C_FIRST, TC_SEG, TC_NEB, LC_Seg |
| ASOF | A19 | T12, C4 | leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv> | the confirmation reports today's option count or the term sheet's | ENG-2455 | asof_over: counts a line that lapsed before the as-of date as still open at it | A1, A2 |
| FAM | A7 | T13, T14, C7 | leonard.hayes@harmonygames.co/<0CDD5A07-0BE6-4909-8188-93E10FBF4E16@librasoftworks.com> | three record holders get three notes | ENG-2441; ENG-2442 | fam_over: folds the Solsten pair into one note | F1, F2, F3, F4, F5, N_COUNT |
| BOARD | A11 | T10, T11, C5 | f_966445655f653d26dc8537 | the document board list stands and Griffin has nothing left to do | SUMMARY | board_over: drops Robert with the outside directors | B1, B2, L6, G2 |
| ASK | A9 | T17, C8 | C51ECE5102ED/1770903714.600249 | Claire's note only needs her date | ENG-2461 | ask_over: writes to a lapsed holder because they once asked | Q1 |
| BOUNCE | A24 | T23, C9 | leonard.hayes@harmonygames.co/<698ce305.050a0220.3b7f1c.9d2e.GMR@mx.google.com> | a sent letter told its holder, so Owen gets his date only | ENG-2456 | bounce_over: treats Marcus's delivered letter as bounced | C_ES12, TC_ES12, C_DATE |
| ALIAS | A7 | T25, C11 | leonard.hayes@harmonygames.co/<CAPBs_aLeDrdRoqOb0LrQ1AfGvbpmR-YdoG8A6PGmPay5Sc-ng=@mail.gmail.com> | no mail to Collins's address after the closing, so he is untold and gets a first note | ENG-2449 | alias_over: takes the Akin mail as telling Deepak too | C_COL, TC_COL, LC_Col, C_FIRST |
| EXT | A11 | T24, C10 | leonard.hayes@harmonygames.co/<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz@mail.gmail.com> | Carta's Oct 29 termination notice gives ES-3's last day, Jan 24, so the line holds nothing | ENG-2454 | ext_over: extends ES-5's window with Calvin's | C_ES3, TC_ES3, P_first, N_Calvin, D6, P1 |

Per node, the four checks. Incorporated: every rule's chain runs from AN2 or AN3 (§4). Survives complete retrieval: ADV needs a subtraction, ASOF a date computation, BOARD a rule read correctly; TOLD, LETTER and FAM are retrieval-shaped, and census C5 says reading decides those. Tool-surface proof: each deciding record is returned by a natural call (§10). Graded weight: §6.

**Budget arithmetic.** See §6: expected miss weight about 0.21 against about 0.38 for 62 %. The medium target (<= 77 %) sits at the edge of the central estimate; the requester's aim of under 70 % is not supported.

### Liveness flags (S5b)

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · DESIGN (no SQL: record text unavailable, only manifest-structure flags can fire) · on the Season Pass backtests these are development fixtures, not validation
  hub ec2ea957-fc8e-4958-b809-0fb735b1e916 · direct delegations 4 · rule placement: SKIP for every node: the mechanism_portfolio declares no A15 node
  T1   exact_predicate    breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T2   stale_summary      breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T3   superseding        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T4   done_gap           -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T5   conclusion_stop    -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T6   completion_elsewhe -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T7   completion_elsewhe -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T8   near_miss_mention  -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T10  superseding        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T11  authority          breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T12  effective_date     -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T13  entity_collision   -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T14  scope_alias        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T15  distractor         breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T16  distractor         breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T17  synthesis_omission -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T18  superseding        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T19  distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T20  distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T21  distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T22  distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T23  done_gap           -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T25  scope_alias        -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T24  superseding        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  dispositions: 0/10 recorded
```

| Flag | Trap | Disposition |
|---|---|---|
| breadcrumb | T1, T2, T3 | wrong source met first by design; the correction sits in a different record; leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com> |
| breadcrumb | T10, T11 | the query words reach both versions, which is fair; the deciding text differs; leonard.hayes@harmonygames.co/<BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com> |
| breadcrumb | T14, T15, T16 | names are searchable by design; the join is the work; leonard.hayes@harmonygames.co/<176175429549.10.8466995912642267217@notifications-email-sending-worker-6b65bf6cf7-gcpxf> |
| breadcrumb | T18 | both notes docs share terms by design (H1 and its older version); f_a37b403d5200d4f0a31d31 |

`hardness_v2_check.py --design`:

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      7 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 8 requirements: {'R3': ['ADV'], 'R5': ['LETTER'], 'R4': ['TOLD', 'BOUNCE', 'ALIAS'], 'R8': ['ASOF'], 'R6': ['FAM'], 'R9': ['BOARD'], 'R12': ['ASK'], 'R2': ['EXT']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   10 of 10 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Every check that can run is CLEAN. RULE_IN_PROMPT runs once a prompt exists.

## 6 Failure-diversity plan

`plan/policy_scores.py` on the real surface, UNCALIBRATED, verbatim:

```
UNCALIBRATED · 102 slots, weight 262, tagged to a rule 190 (72.5%), weight-5 rows 20
  ADV     weight  44 16.8%  design miss 0.55
  LETTER  weight  30 11.5%  design miss 0.15
  TOLD    weight  28 10.7%  design miss 0.15
  ASOF    weight  25  9.5%  design miss 0.10
  FAM     weight  20  7.6%  design miss 0.15
  BOARD   weight  14  5.3%  design miss 0.10
  ASK     weight   5  1.9%  design miss 0.10
  BOUNCE  weight  11  4.2%  design miss 0.50
  EXT     weight  27 10.3%  design miss 0.55
  ALIAS   weight  14  5.3%  design miss 0.30
expected miss weight (share x miss x Q) ~ 0.198; the requester aims under 70 %

Whole policies
  100.0%  Perfect
   27.5%  Owner list and the Carta search only
   88.5%  Thorough, trusts the founders' 'done' lines
   83.2%  Thorough, trusts the owner list's share column
   90.5%  Thorough, answers KPMG with today's holdings
   92.4%  Thorough except mail older than 2025
   65.3%  The pre-check's path (bulk pulls, letters by id, Carta-sender mail only, no alias lookup)
   95.8%  Thorough, reads letters by message id
   89.7%  Thorough, reads Carta's own notices only
   94.7%  Thorough, never asks who Akin is
   87.4%  Thorough except DMs and recent mail
   94.7%  Thorough, keeps the board list in the documents

Single misses (every row of the trap)
  ADV 83.2%  LETTER 88.5%  TOLD 89.3%  ASOF 90.5%  FAM 92.4%  BOARD 94.7%  ASK 98.1%  BOUNCE 95.8%  EXT 89.7%  ALIAS 94.7%

P(one run catches every trap) ~ 0.032; traps landing per run at design rates 2.65

Six-run Monte Carlo  (scale multiplies every miss rate)
  scale  rho   E[avg]  mean SD  P(<70)  P(<=62)  P(<85)  P(SD)  P(patterns)  P(all, platform)  P(all, hard bar)
  1.00  0.15   79.8%    0.098    0.02     0.00    0.87   0.46         1.00              0.43              0.01
  1.00  0.35   80.1%    0.117    0.04     0.00    0.82   0.68         1.00              0.60              0.03
  0.85  0.15   82.6%    0.097    0.00     0.00    0.70   0.44         1.00              0.36              0.00
  0.85  0.35   82.8%    0.114    0.01     0.00    0.65   0.64         1.00              0.48              0.01
  0.70  0.15   85.3%    0.093    0.00     0.00    0.44   0.39         1.00              0.24              0.00
  0.70  0.35   85.5%    0.108    0.00     0.00    0.44   0.56         1.00              0.34              0.00
  0.50  0.15   89.0%    0.083    0.00     0.00    0.16   0.26         1.00              0.09              0.00
```

**Reading it.** Four heavy channels, ADV, LETTER, TOLD and ASOF, sit on different records and habits: a tie-out, a recipient join, a per-address search and a date computation. A run strong on one is not thereby strong on another. FAM adds a fifth at 8.2 %. SIDE, BOARD and ASK are small and add little spread. A1 and A2 need both ASOF and ADV, because the count includes the advisor grants.

**Honest position.** My first model said 71.6 %. A cold adversary reading the same design put a first baseline at 76 to 82 %, and found why: the rule doc pointed at traps, about 27 weight never flipped when its trap landed, and my own volume plan defeated T7. The fixes are in, and rates here are the adversary's, moved only where a pointer was removed. Central estimate 78 %. Against the bars: platform < 85 % likely; medium design target <= 77 % at the edge; requester's aim under 70 % not supported (P about 0.1); 62 % not supported. SD is the gate at risk: P(SD in band) 0.67 to 0.83. /rubric row multiplication has cost 6.5 to 15 points on past tasks; this surface already plans per-target rows, but the risk stands. Only the pre-check can test any of this, and C5 recommends proving catch rates before the baseline.

## 7 Deliverables and dependent writes

| Deliverable | Service | Depends on | Requirement |
|---|---|---|---|
| Holder schedule, one row per project issue, plus a short summary | gsheets, moved to d_601064334a0b493022fe83 | C1, C2, C3, T3 | R1-R5, R9 |
| Investor letter, updated from C0ADGSZKR3R/1770664700.848759 | gdocs, moved to d_601064334a0b493022fe83 | C5, K1 | R10 |
| 14 personal notes as drafts | gmail | C2, C3, C7, C8 | R6, R12 |
| Reply to KPMG, to all recipients on leonard.hayes@harmonygames.co/1857029474983245439 | gmail | C4 | R8 |
| Heads-up to Griffin in thread leonard.hayes@harmonygames.co/1856958794180374704. Sunset drafts and sends the consents, so this stops short of the instrument | gmail | C5 | R9 |
| State move on ENG-2438 to ENG-2463; reason comment on the 12 issues with no note | linear | C2, C3 | R11 |
| Shares to Robert and Arthur; reply to the founders in C0ADGSZKR3R | gdrive, slack | K13, K14, C2 | R13 |

Reuse versus create: the deliverables are new; the draft sheet f_5ecaa967db3adcfa440b09 is partial and stale, so it is a layout source only.

## 8 Service role map

| Service | Role | Load-bearing fact or write | Carrier |
|---|---|---|---|
| slack | the draft, Leonard's promise and list, the done claims, DMs that decide who was told | the ask, the wrong sources and the records that beat them; the founders' reply | ● |
| gmail | Carta notices, letters, the owner list, side letter chain, resignations, KPMG and Sunset requests | every line's live state and the as-of date live here; notes and replies go here | ● |
| gcal | the Tuesday hold | the date the notes are due | ● |
| gdrive | the close-out folder | the destination of both files | ● |
| gdocs | close-out notes, advisor table, term sheet, charter and side letter drafts | the closed rule and the subtraction that ties the stock lines | ● |
| gsheets | Task List, draft holder sheet, the deliverable | the schedule itself | ● |
| gslides | the update outline | the letter's section order, supporting only | ● |
| contacts | Bergmann's and Eren's name-to-address rows | separates Bergmann from the Patrick line; Eren's row gives an address and nothing else | ● |
| linear | the holder project | the cohort, per-holder notes, states and reason comments | ● |
| trello | Leonard's close-out card | the order: the holder sheet comes first | ● |
| snowflake | FINANCE_LEDGER financing rows | confirms no new financing since 2023 for the KPMG reply, and Segerstrale's $50,000 | ● |
| github | not used | no honest job in a stockholder close-out | n/a |
| confluence | not used | never seeded; no fact rests on it | n/a |

## 9 Call budget

| Phase | Service | Calls | Necessity reason |
|---|---|---|---|
| discovery | slack | 8 | the draft, #winddown pages, the Feb 12 list, the founder DMs |
| discovery | gmail | 6 | Sunset's request, KPMG's request and recent mail |
| discovery | linear | 3 | project, issue list, status list |
| discovery | gdrive | 3 | the close-out folder and Leonard's Drive listing |
| rules | gdocs | 6 | close-out notes, earlier notes, charter, IRA, side letter draft, term sheet |
| rules | gsheets | 2 | Task List and the draft holder sheet |
| rules | gslides | 1 | the update outline deck |
| rules | trello | 2 | the founders' close-out card and its comment |
| rules | gcal | 1 | the Tuesday hold, found by a keyword search because lists spill |
| rules | contacts | 2 | holders with no name in the mail: Bergmann and Eren |
| per-record | linear | 26 | each holder's issue notes need their own linear_list_comments; list_issues returns no comments |
| per-record | gmail | 12 | one search per stock holder address for the told column; search returns ids only |
| per-record | gmail | 14 | termination notices and letters read per option line; a batch at full format is capped at 10 ids |
| per-record | slack | 12 | name search per stock holder across DMs for any message about the closing |
| reconciliation | snowflake | 2 | FINANCE_LEDGER financing rows: dollars and no new money since 2023 |
| reconciliation | gdocs | 2 | Due Diligence advisor table and the term sheet tie-out |
| reconciliation | gmail | 4 | side letter chain and the board resignations |
| writes | gsheets | 4 | create the schedule, fill it, read it back |
| writes | gdocs | 3 | the letter |
| writes | gdrive | 6 | move both files, share each with Robert and Arthur |
| writes | linear | 26 | one state move per holder issue; no bulk form |
| writes | linear | 12 | a reason comment on each issue where no note goes |
| writes | gmail | 2 | Griffin heads-up and the KPMG reply |
| writes | slack | 1 | the founders' thread reply |
| writes | gmail | 14 | one personal note per target; gmail_create_draft ran 14 times in the platform pre-check (run_forensics/rev1p/precheck/precheck/calls.jsonl) |

Unconditional floor 174; planned total 174. Note writes are conditional until the pre-check proves `gmail_create_draft`, which has never run in a stored baseline. The ≥ 500 floor is not honestly reachable: 26 holders, and mail reads batch. `volume_exception`: 26 non-founder holders; mail reads batch, so about 145 honest calls per run; reaching 500 would need padding, which fails on its own. Golden-run note: a correct run needs these per-holder reads, because told state exists nowhere in bulk.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by |
|---|---|---|---|
| Who counts as a holder | everyone on a Carta record, live or lapsed: 26 non-founder lines, one project issue each | only people holding something today: 20 lines | project ec2ea957-fc8e-4958-b809-0fb735b1e916 (ENG-2438 to ENG-2463) states the cohort; the schedule shows Nothing for the six; leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv> is one such record |
| Is a past last day lapsed, or could the option have been exercised | lapsed: H1 makes Carta the record and a line past its last day holds nothing | ES-16's holder was trying to exercise (leonard@harmonygames.co_1847333990408253969.json) | H1 f_a37b403d5200d4f0a31d31 closes it by rule, not by evidence of no exercise; the October notices predate those windows |
| Someone with stock and an open grant | one row and at most one note per person; advisor grants have no last day, so the note is on the closing | the grant is a live option line that fires its own note | H1 f_a37b403d5200d4f0a31d31: one row and at most one note per person; Carta's digests name all four grants (ES-9, ES-11 in leonard.hayes@harmonygames.co/1782897835407336831; ES-8, ES-10 in the seeded Nov 20, 2023 digest) and no termination, and Carta is the record |
| Does a channel post count as told | no: told means a message sent to the person directly and delivered | Oliver replied in the channel, so he knows (C05KNDCHAAG/1770839984.194409) | H1 f_a37b403d5200d4f0a31d31: sent to them directly and delivered; a `<!here>` post is not |
| ES-14's channel membership | not told: he left in November | a listed member of #company-internal | H1 sent-directly-and-delivered rule; NB-31; his exit leonard.hayes@harmonygames.co/<CAEH8bLxfNq9vp7-VSMQdpetPWQxBhv2pcPE=xj=oX9c8MxNFtA@mail.gmail.com> |
| Who may do the telling | Leonard, Robert or Arthur | only Leonard, who promised to personally reach out | H1 f_a37b403d5200d4f0a31d31: from one of the three of us; leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>; the promise D04UC0UEN2V/1770665186.368229 |
| Is Griffin told through its partner | yes: one mail to the partner reaches both funds | per-line, and no mail names the Side Fund | H1 for a fund, its partner; leonard.hayes@harmonygames.co/1856675475513544349 message 13; one signer for both funds leonard.hayes@harmonygames.co/1774928765255297348 |
| Was Tor told in November | no: a runway warning, not the closing | he heard about three months of runway (D09R59580EM/1762285888.654689) | the DM never says the company is closing; H1's told rule names the closing |
| Does a Slack DM count for Segerstråle | yes for told: written and sent to him directly | it is not a side letter notice | told and route are separate columns; D04UC0UEN2V/1770664988.379119 |
| Family contact | one note to Enes covers the other two lines, which need no note of their own | they hold individually, so three notes | C0ADGSZKR3R/1770949310.220519 overrides leonard.hayes@harmonygames.co/1774211155651873582 ('holding shares individually'); Enes's own line stays First note |
| Does the family rule reach the Solsten pair | no: colleagues, not family | two holders at one company | 'all three Disli brothers' leonard.hayes@harmonygames.co/<0CDD5A07-0BE6-4909-8188-93E10FBF4E16@librasoftworks.com>; the Solsten pair sign as CEO and COO, leonard.hayes@harmonygames.co/1770053656612413311 |
| Awards ending exactly on the as-of date | reflected: vested only, 243,757 options | still whole on that day: 266,436 | NEW leonard.hayes@harmonygames.co/1857029474983245439: each effective date as Carta shows it, regardless of when recorded |
| Effective dates entered late or chosen on Feb 11 | use the effective date as Carta shows it | an audit should not use backdated entries (C07C2866011/1770827616.441769): 268,772 | NEW leonard.hayes@harmonygames.co/1857029474983245439: each effective date as Carta shows it. A run that also flags the backdating must not lose a row |
| What 'fully diluted' means | not asked: KPMG asks for counts | four bases exist in the base | NEW leonard.hayes@harmonygames.co/1857029474983245439 asks shares, options and their total; no percent of the whole is graded; leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com> |
| Is a personal note a notice | no: formal notices are a separate step; route is a column for those | the note to Tor must copy TLAS | NEW leonard.hayes@harmonygames.co/1857034369525983506 says formal notices are a separate step legal will walk him through later; no row fails if a run copies TLAS; f_0c37bb7235683d73569903 is the visible base line |
| Does Griffin still have to act | yes: its vote as a holder is separate from the board seat | it resigned, so nothing is left | charter draft f_90c029015fc474199cf736, Requisite Holders and 3.3.5 |
| Could Griffin's waiver remove the notice duty | out of scope: no notice deadline is graded | Fourth B 8 lets the Requisite Holders waive class rights | no row grades a notice deadline; f_90c029015fc474199cf736 |
| Who is on the board | Leonard and Robert | all three founders ('it's just us and Griffin', Feb 11), or Leonard alone | C04UEQVDVB7/1752517647.842649 fits two founders against Phil; Carta consents leonard.hayes@harmonygames.co/1838216168984971198; leonard.hayes@harmonygames.co/<CAMy0Hx1va3q4zH2HyPiqfm8Je2fm5A=JHKf8LrXWb12z2FHr6w@mail.gmail.com>; leonard.hayes@harmonygames.co/<BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com> |
| ES-17's date | lapsed on either date | letter Jan 22 against Carta Jan 28 | both precede the clock; no row grades the exact date; leonard.hayes@harmonygames.co/<176175429549.10.8466995912642267217@notifications-email-sending-worker-6b65bf6cf7-gcpxf> |
| ES-5's end date | lapsed by Carta | ledger pays him to Dec 31, so he could be live (NB-32) | H1: Carta is the record; never grade his end date; leonard.hayes@harmonygames.co/1847333395311994879 |
| Who goes first | whoever's last day comes first: ES-3 (Feb 20, from Carta's Jan 23 update), then ES-14 (Feb 21) | Griffin first, per Leonard's Feb 9 line; or the sheet first; or ES-14 on Carta's Oct 29 date for ES-3 | H1 f_a37b403d5200d4f0a31d31; the sheet-first card 698e5a10c3f24b7e9d16a0e4 is about the work order, not the notes; D04UC0UEN2V/1770665186.368229; leonard.hayes@harmonygames.co/<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz@mail.gmail.com> |
| Is 'Akin' Matthew Collins | yes: Collins signs his own mail 'akin' and board mail greets him as Akin, so Leonard's Feb 12 mail told him | Akin is someone else, or a personal address is not his | leonard.hayes@harmonygames.co/<CAMy0Hx2S+a4q+PUkFZM1ifrcEKv-y7AWWtQHrEsWg2qRxvFo3Q@mail.gmail.com> ('best / akin' from matthew.collins@harmonygames.co); leonard.hayes@harmonygames.co/<CAPBs_aLeDrdRoqOb0LrQ1AfGvbpmR-YdoG8A6PGmPay5Sc-ng=@mail.gmail.com> |
| Does a letter that bounced count as told | no: the mail system says it was not delivered, so the closing never reached Owen | it was sent, and the rule's word is the message, not its delivery | leonard.hayes@harmonygames.co/<698ce305.050a0220.3b7f1c.9d2e.GMR@mx.google.com> (550 5.2.1 inactive, nine seconds after the letter); H1's told line |
| Which Carta date governs ES-3 | Carta's Jan 23 update: Feb 20, 2026, after the clock, so the line is live | Carta's Oct 29 termination notice: Jan 24, so it holds nothing | H1 'Carta is the record'; leonard.hayes@harmonygames.co/<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz@mail.gmail.com> carries Carta's own later notice with the old date beside the new one; leonard.hayes@harmonygames.co/<176175436721.10.9685252272573766647@notifications-email-sending-worker-6b65bf6cf7-dg8x2> |
| Issue state by class | Canceled where the line holds nothing; otherwise Todo where its own note waits, and Done where it does not | a Covered line stays Todo with the family note | project ec2ea957-fc8e-4958-b809-0fb735b1e916 description; ENG-2438 |

### Reach table (load-bearing records)

Every scoped base record below is YES for Leonard (`persona_view.py can-see leonard_hayes …`); planned seeds are checked by `check-sql` at injection. Not reachable, and so never relied on: the advisor agreements (visible to no persona), all PDFs and Gmail attachments, and the 2023 Bridge Round sheet.

```
base:draft | leonard_hayes slack C0ADGSZKR3R/1770664700.848759: YES
base:one by one | leonard_hayes slack C0ADGSZKR3R/1770664924.520089: YES
base:letters claim | leonard_hayes slack C0ADGSZKR3R/1770841239.761999: YES
base:Feb 12 list | leonard_hayes slack C0ADGSZKR3R/1770934638.035469: YES
base:Carta claim | leonard_hayes slack C0ADGSZKR3R/1770935621.095649: YES
base:promise | leonard_hayes slack D04UC0UEN2V/1770665186.368229: YES
base:Segerstrale told | leonard_hayes slack D04UC0UEN2V/1770664988.379119: YES
base:Claire's question | leonard_hayes slack C51ECE5102ED/1770903714.600249: YES
base:Tor warned | leonard_hayes slack D09R59580EM/1762285888.654689: YES
base:Vincent exit | leonard_hayes slack D05PX3R13QF/1763665854.644329: YES
base:owner list Slack copy | leonard_hayes slack C04UEQVDVB7/1732646280.941869: YES
base:owner list | leonard_hayes gmail leonard.hayes@harmonygames.co/1816809274978043917: YES
base:Matthew resigns | leonard_hayes gmail leonard.hayes@harmonygames.co/1830959847543474636: YES
base:Griffin resigns | leonard_hayes gmail leonard.hayes@harmonygames.co/1856958794180374704: YES
base:side letter chain | leonard_hayes gmail leonard.hayes@harmonygames.co/1775602109531090463: YES
base:side letter signed | leonard_hayes gmail leonard.hayes@harmonygames.co/1777052222643175480: YES
base:KPMG FY24 | leonard_hayes gmail leonard.hayes@harmonygames.co/1817557789846606177: YES
base:KPMG FY23 | leonard_hayes gmail leonard.hayes@harmonygames.co/1788910618703813283: YES
base:Enes addresses | leonard_hayes gmail leonard.hayes@harmonygames.co/1770141224265557526: YES
base:brothers wired | leonard_hayes gmail leonard.hayes@harmonygames.co/1774211155651873582: YES
base:Vincent resigns | leonard_hayes gmail leonard.hayes@harmonygames.co/1849344928983425627: YES
base:letter ES-4 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856858053929740799: YES
base:letter ES-12 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856860994291529096: YES
base:letter ES-13 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856861229984402233: YES
base:letter ES-7 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856861323365646598: YES
base:letter ES-15 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856861400116562076: YES
base:letter ES-1 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856861462411533365: YES
base:notice ES-17 letter | leonard_hayes gmail leonard.hayes@harmonygames.co/1847335165884050330: YES
base:Carta ES-2 | leonard_hayes gmail leonard.hayes@harmonygames.co/1808666480668498098: YES
base:Carta ES-6 | leonard_hayes gmail leonard.hayes@harmonygames.co/1830952527208439510: YES
base:Carta ES-17 | leonard_hayes gmail leonard.hayes@harmonygames.co/1847333272519888206: YES
base:Carta ES-16 | leonard_hayes gmail leonard.hayes@harmonygames.co/1847333318158821452: YES
base:Carta ES-3 | leonard_hayes gmail leonard.hayes@harmonygames.co/1847333347700620793: YES
base:Carta ES-5 | leonard_hayes gmail leonard.hayes@harmonygames.co/1847333395311994879: YES
base:Carta ES-7 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856960351896429942: YES
base:Carta ES-18 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856960382677662910: YES
base:Carta ES-4 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856960410709778333: YES
base:Carta ES-1 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856960433624350836: YES
base:Carta ES-14 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856960478782792748: YES
base:Carta ES-12 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856960504234892536: YES
base:Carta ES-15 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856960532806250145: YES
base:Carta ES-13 | leonard_hayes gmail leonard.hayes@harmonygames.co/1856960563574318616: YES
base:advisor table | leonard_hayes gdocs f_6a37227593d0977fdbdd7a: YES
base:term sheet | leonard_hayes gdocs f_11040fe5d66821bd6951aa: YES
base:side letter draft | leonard_hayes gdocs f_6201c7027d02997bfb2c84: YES
base:financing draft | leonard_hayes gdocs f_966445655f653d26dc8537: YES
base:charter draft | leonard_hayes gdocs f_90c029015fc474199cf736: YES
base:owner list Drive copy | leonard_hayes gdocs f_414596b0a9d698267dd1e1: YES
base:Task List | leonard_hayes gsheets f_31115ddb6ed866f2b10d60: YES
```

**Feasibility.** Every write is in `Evals/references/tools/catalog.json` (research/s4_carrier_formats.md section H). Leonard will own every target. `gmail_create_draft` is unproven and falls back to sends. Slack's catalog names `channel, text`; stored calls use `channel_id, message`. Nothing is asked that needs a Doc comment, an attachment or a Cc on a reply.

**Precedence.** Load-bearing facts sit only in ● carriers. Linear comments are ● under Ask_Carriers §6b. Slides, Contacts and GCal hold supporting detail only, and no graded fact sits only there.

**Prompt naturalness.** The prompt will name the three anchors and the deliverable kinds. It must not name the rule, the classes, the carriers, any holder's state, who goes first, or the Tuesday date. Rules live in the records.

**Grading devices.** Exact totals (3,051,879; 159,706; 243,757; 9,295,636). No row may penalise a run that flags the backdated entries. The answer to Claire's question is required on ES-4 only, with no penalty for telling ES-1 or ES-15 too. ≤ 5 samples per group plus a volume row. One row per write where the content differs. Accepted name forms in row titles, tokens included. The notes are graded by a bare count, never by exclusion. Addresses are never graded.

### Coherence rail

- Every audit row in §1a is dispositioned; designed disagreements are dated human claims with a named later record: C0ADGSZKR3R/1770841239.761999 against leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv>; C0ADGSZKR3R/1770935621.095649 against leonard.hayes@harmonygames.co/<CAPBs_a68Agj+37mZ6abeW5KEKTh00he+mgOpLP2FrpDjeO-37Q@mail.gmail.com>.
- Companions for every seeded record are planned in §11, with `integrations.json` entries cited, for example INT-04.
- Id schemes follow the base: ENG-2438, leonard.hayes@harmonygames.co/1857029474983245439, d_601064334a0b493022fe83.
- No claim about git is made, so `base_claims.py` has nothing to test; ENG-2438 names no branch.

## 11 Record plan for /create-injection

Row floor: ≥ 120 INSERTs, not lowered by the exceptions. Estimate about 118: Linear 1 + 26 + about 56 comments, Gmail 8 (KPMG root, its follow-up, Leonard's holding reply, Sunset, Robert's reply, thread rows), Slack 8 (two short founder bursts), GCal 1, Drive 6, Docs 2, Sheets 2, Slides 7, Contacts 1, Trello 3. A third comment goes only where it is true. Count this at injection: padding fails on its own.

| Service | Planned id | Record | Timestamp (UTC) | Role |
|---|---|---|---|---|
| linear | ec2ea957-fc8e-4958-b809-0fb735b1e916 | project 'Holder records', team_ENG, lead Leonard; neutral name and titles, because team ENG includes the holders (ENG-2438) | created 2026-02-12T23:24:12Z; updated after leonard.hayes@harmonygames.co/1857034369525983506 | hub, AN2 |
| linear | ENG-2438 to ENG-2463 | 26 issues, Backlog; assignee a named founder or none; titles in owner-list forms; no instrument, no state | from 2026-02-12T23:25:03Z | cohort |
| linear | comment ids minted at SQL time | quoted, dated figures ('Nov 2024 owner list: 127,162'), never present tense; one dated last contact before February on all 26, ENG-2438 to ENG-2463, so no gap marks a told line; values only where a record backs them | before leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>'s time | per-holder surface; wrong source met first |
| gmail | leonard.hayes@harmonygames.co/1857029474983245439 | PERSON_3088 to Leonard, cc PERSON_4416, PERSON_2322, PERSON_2847; financials covered by leonard.hayes@harmonygames.co/1856787396431935562; asks shares, each option line by holder, and their total, as of Dec 31, 2025, using each effective date as Carta shows it, regardless of when recorded; reply to all | 2026-02-13T16:48:33Z | AN3, H4 |
| gmail | leonard.hayes@harmonygames.co/1857034369525983506 | PERSON_2888 to Leonard, relaying legal: what the intake needs on stockholders: one line per holder, shares and options outstanding, count by what is owed, directors, and any special terms; says formal notices come from Sunset later | 2026-02-13T18:06:21Z | K8 |
| gmail | leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com> | Robert's reply on base thread leonard.hayes@harmonygames.co/1773963101399472184 to Nebojsa, Leonard copied; says the company is closing, and that he wanted him to hear it from a friend; promises nothing further. Copy in Robert's mailbox too (robert@harmonygames.co/1773963101279916523). Update `gmail_threads.snippet` | 2026-02-12T23:41:12Z | T7 |
| gdocs+gdrive | f_a37b403d5200d4f0a31d31 | close-out notes, owner Leonard. Includes one line tying Tuesday to C0ADGSZKR3R/1770933601.686309 and one on why this folder and not the Wind Down one | 2026-02-13T01:05:41Z | H1 |
| gdocs+gdrive | f_762c60832854d3e7a7f7df | earlier notes, owner Leonard; must not name Sunset, the letters or Carta entries | 2026-02-10T17:41:09Z | H1 decoy |
| gdrive | d_601064334a0b493022fe83 | close-out folder, owner Leonard, in root d_63fffeb4fab5233ed5bb73 | 2026-02-12T23:20:37Z | destination |
| gsheets+gdrive | f_5ecaa967db3adcfa440b09 | partial draft sheet, figures marked as copied from the Nov 2024 list | 2026-02-10T18:12:26Z | T20 |
| gslides+gdrive | f_75dddccabb26eeea4842c8 | update outline, 5 pages; '27 holders on the Nov 2024 owner list'; must not name Sunset | 2026-02-10T18:33:52Z | T19, K12 |
| slack | C0ADGSZKR3R/1770938120.410229 | Leonard's short burst in #winddown: why the holders sit in Linear | 2026-02-12T23:15:20Z | K15 |
| slack | C0ADGSZKR3R/1770949310.220519 | Leonard's replies under his Feb 12 list C0ADGSZKR3R/1770934638.035469: the family sentence, the Covered label, the sheet going to Arthur too; Arthur's one-line reply; parent counters updated | 2026-02-13T02:21:50Z | K14, FAM rule |
| gcal | evt_6f1a2c9e4b7d3a58c0e1d2 | hold, Leonard sole attendee; the date lives here and not in the prompt | created 2026-02-13, start 2026-02-17 | K11 |
| trello | 698e5a10c3f24b7e9d16a0e4 | To Do card, list 640643a3fd8f3ca308d93195, written by Leonard, with his comment after Sunset's mail; bump the card's activity | 2026-02-12T22:54:08Z | K10 |
| contacts | minted at SQL time | Bergmann and Eren, token and email only, no date field | n/a | name to address |

**Must not.** Move a share figure, a Carta notice date or the two historic mailings. Seed a list with figures or states, or a Carta export. Say Leonard told an angel, or that ES-14 or ES-18 got a letter or a date. Write $11,700. Quote a real name from a PDF signature page. Name Sunsets HQ Corp., Sutter Law or Stable Rock. Name Sunset before its first base mention. Touch Trello card 68c5a49e8491a9d7faf869d0. Say anything about the closing in the project name or issue titles. Name three founders by count, in seeded text: name them.

### Integrations and companions

From `integrations.json`. The gate (`kb_integrations`) accepts an INT id, or `<service> none` with a reason, for each seeded service whose schema is a source. Only `linear`, `gcal`, `slack`, `trello`, `google_drive` have sources here.

| Service | INT entries | Base rate and rule | Companion needed |
|---|---|---|---|
| slack | INT-22 (Slack → Gmail, optional), INT-17 (Slack Connect notices, churn signal) | 603 mails, "Optional; never load-bearing" | None required. A reply into an existing thread needs the parent's `reply_count`, `latest_reply` updated (base_check). No Slack seed after Feb 13 10:03 UTC |
| gmail | Destination of INT-05, INT-11, INT-22; source of none | | `gmail`: none, no integration has Gmail as source. Own companions: thread file, message headers, `in_reply_to` in the same mailbox, RFC-2822 dates in Leonard's mailbox, a copy per mailbox only where the base keeps one |
| gcal | INT-11 → Gmail | Invites only partly match (0.879). The rule says "A seeded meeting does not need an invitation mail", but base_check warns at this rate | One GCal copy per attendee calendar, same `ical_uid`, copies agree. Invitation mail if the rate rule fires, or an `integration_exceptions` entry with `no_notify` |
| linear | INT-04 → Slack; INT-05 → Gmail (INT-03 needs a PR, not applicable) | INT-04 window ends 2026-01-28: "a seeded Linear state change does not require a Slack notice". INT-05: "a seeded Linear comment does not need a mail" | No mirror. Own companions: project and issue stamps, `updated_at` not older than its comments, lifecycle fields. **A seeded INT-04 notice would fall after the mirror's last base date, so add none** |
| gdocs, gdrive, gsheets, gslides | INT-13 (Drive → Slack DM) | 760 messages, to 2026-01-19. "DM-only; seeded doc comments need not have one" | No mirror. Own companions: `drive_files` row with the same owner and sharing. Leonard's root `d_63fffeb4fab5233ed5bb73`, never the `Resource:` folder |
| contacts | none in the catalogue | | `contacts`: none, no integration. A new row must not imply a Sunset or KPMG record the base lacks · research/s3_coherence_audit.md line 852 |
| trello | INT-21: no integration exists | "Do not seed Trello bot notifications in Slack"; `shortLink` is null on every card | No mirror. Own companions: `dateLastActivity`, badges, actions. Avoid `/cards/801`: it is open, in Done, and any new action would reopen a stale state |

**Two tight points.**
- Exactly 10 schemas are planned. `contacts` and `trello` have no base investor content worth seeding, so both risk being padding. Sunset and KPMG people have no Contacts rows at all, so a Contacts seed adds identities rather than facts. · research/s3_coherence_audit.md line 856
- Slack is the one service whose seed window is narrow: 11 h 46 min between Leonard's Feb 12 22:17 UTC list and the export's end. · research/s3_coherence_audit.md line 857

## 12 Self-test results

`hardness_gate.py --design`, verbatim:

```
HARDNESS GATE (extreme (design)): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: skipped (--design: no SQL yet)
  [ok] base_consistency: skipped (--design: no SQL yet)
  [ok] services_injected: skipped (--design: no SQL yet)
  [ok] rows: skipped (--design: no SQL yet)
  [ok] services_carrying_weight: 11 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: skipped (--design: no SQL yet)
  [ok] seeded_ids_exist_in_sql: skipped (--design: no SQL yet)
  [ok] anchors: 3 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 14 fragments; need ≥ 12
  [ok] ask_fragment_services: 9 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 14 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 12 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 26; need ≥ 26 (source-defined: True) (requester-confirmed cohort_exception)
  [ok] evidence_surfaces: 5 surfaces over 4 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 90; need ≥ 85
  [ok] call_budget: unconditional (verified) floor 174 of 174 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 130 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 11 services in budget; largest share outside the per-record phase 37% (≤ 50%)
  [ok] traps: 24 traps across 13 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 10 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 5 supersessions (2 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 6 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 10 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 10 chains with 7 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 10 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 21 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 12 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 8 writes over 6 services; each must depend on findings
  [note] volume_exception: call-budget floor 130 and per-record floor 85 replace 500 and 300; every other extreme target applies except the cohort floor below — reason: 26 non-founder holders; mail reads batch, so about 145 honest calls per run; rea; requester confirmation: requester, Claude Code chat 2026-11-07: 'go with your recommendations on all six
  [note] cohort_exception: cohort floor 26 replaces 40; surfaces, surface services, why_no_bulk and short_circuit still apply — reason: the company has 29 holders on Carta, 26 of them non-founders; no honest cohort o; requester confirmation: requester, Claude Code chat 2026-11-07: 'go with your recommendations on all six
```

`gradable_surface.py validate`:

```
GRADABLE SURFACE (01_Gradable_Surface.json): PASS · 102 slots · weight 262 · mechanism share 72.5% (reported, not gated) · weight by class {'write_content': 138, 'direct': 109, 'delivery': 15}
```

`gradable_surface.py gradeable-report`:

```
SURFACE.GRADEABLE PASS · 102 slot(s) · {'GRADABLE': 102}
```

**Lazy-solver pass.** One broad search per service, first hits, no thread opens. It gets the owner list and the letter draft, so it scores stock on plain lines and the delivery rows (`plan/policy_scores_output.txt`) and misses every trap. Leaks found and fixed: issue titles showed the family surname and holder ids; rows now key by issue. The full leak list is in §13.

**Literal-value sweep.** 243,757 and 9,295,636 appear in no base record, and no seed may carry them. 164,114 likewise. 3,051,879 appears in the term sheet only, on purpose (rev2 removed it from KPMG's follow-up and from Leonard's #executives note).

**Wording sweep.** H1's rule words must not appear in the deciding records: 'told' and 'closing' are absent from D04UC0UEN2V/1770664988.379119's own text, which says 'shut down'. H1 quotes no base sentence (K3 removed: 'every angel investor' was one Slack hit from the Segerstråle record). To re-run on the SQL.

**'The rest stands' check.** K14 adds to the sharing and carries the family sentence; no later record re-asserts or contradicts it.

**S9b forecast.** Pre-registered ledger id hev_3fc40962f70b1d59. UNCALIBRATED.

```
hardness_forecast: DISCLOSED OVERRIDE: --max-k 10 above the default 8 (--allow-max-k 10): exact enumeration of up to 2^10 configurations per record, not the plan's default (§5)
HARDNESS FORECAST · UNCALIBRATED · advisory · DESIGN (declared attributions) · model claude-opus-5-5 · design · model outputs, not measurements; the Season Pass backtests are development fixtures, not validation
  rule:ADV                                     family A17                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:LETTER                                  family A24                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:TOLD                                    family A25                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:ASOF                                    family A19                                      Beta(1.0, 1.0) mean 0.50 n_eff 0.0 records 0
  rule:FAM                                     family A7                                       Beta(1.0, 1.0) mean 0.50 n_eff 0.0 records 0
  rule:BOARD                                   family A11                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:ASK                                     family A9                                       Beta(1.0, 1.0) mean 0.50 n_eff 0.0 records 0
  rule:BOUNCE                                  family A24                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:EXT                                     family A11                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:ALIAS                                   family A7                                       Beta(1.0, 1.0) mean 0.50 n_eff 0.0 records 0
  independent whole    V3 E[avg] 0.699 [0.598, 0.800] P(all) 0.378
  source      whole    V3 E[avg] 0.699 [0.598, 0.800] P(all) 0.378
  correlated  whole    V3 E[avg] 0.708 [0.557, 0.855] P(all) 0.668
  V3: P(all four difficulty gates) 0.378-0.668 across scenarios; value of information (first scenario): ['rule:ADV', 'rule:LETTER', 'rule:TOLD']
  slots most at risk (independent whole; P(fail) / P(fails all six) - all-fail justification workload, never a block): N_COUNT 0.85/0.50, A1 0.67/0.25, C_FIRST 0.66/0.25, P1 0.56/0.13, B2 0.55/0.12, C_DATE 0.55/0.12, Q1 0.51/0.15, A2 0.50/0.15
  ledger: forecast record {'id': 'hev_3fc40962f70b1d59', 'added': True, 'present': False, 'rejected': (none)}
```

### Self-review

Re-read Evals/1_Prompt_Eval.md §2.1 (Unique Ground Truth), §2.2 (Feasibility), §3.2 (Cross-Service Coherence) and Evals/0_Injection_Quality_Eval.md Check C in order.

| Area | Counter-reading (strongest argument it fails) | Resolution (evidence) |
|---|---|---|
| temporal | the project description cites records dated after it | project updated_at is after leonard.hayes@harmonygames.co/1857034369525983506; created_at stays earlier, ENG-2438 |
| temporal | Robert's reply contradicts the Feb 12 list | it is dated after C0ADGSZKR3R/1770934638.035469, so the list was true when written; leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com> |
| temporal | a Tuesday deadline sits after 'archive by Feb 15' | C0ADGSZKR3R/1770933601.686309 keeps accounts until the data is extracted; the notes say so, f_a37b403d5200d4f0a31d31 |
| semantic | 'told' could mean heard about it | H1 f_a37b403d5200d4f0a31d31 defines it; T8 tests the boundary on D09R59580EM/1762285888.654689 |
| semantic | 'Nothing' reads as if the holder never held anything | the column is what is owed now; leonard.hayes@harmonygames.co/<176175429549.10.8466995912642267217@notifications-email-sending-worker-6b65bf6cf7-gcpxf> |
| cross-service referential | the project cites a Sunset request that must exist | seeded in the same revision, leonard.hayes@harmonygames.co/1857034369525983506, after leonard.hayes@harmonygames.co/1856675475513544349 |
| cross-service referential | a seed names a Sunset entity first seen in a PDF | seeds use the mail's own 'Sunset' form only; research/s1_signed_pdfs.md section C item 6 |
| quantitative | 3,051,879 against 3,051,881 and 3,051,882 | #executives idx 727 says 3,051,881 issued, but the newer term sheet and the sum of lines settle it, /docs_documents/40; only 3,051,879 is graded |
| quantitative | the owner list claims to add to 100 % | true on its own base, f_414596b0a9d698267dd1e1 adds the unissued pool; no percent of the whole is graded (hazard Q10) |
| quantitative | a comment repeats an owner-list figure as fact | every such comment quotes it as the Nov 2024 owner list, dated, never in the present tense; leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com> |
| state/lifecycle | a closed Linear issue gets a later comment | seeded comments predate any close; states are moved by the run, ENG-2438 to ENG-2463 |
| state/lifecycle | Trello card 801 reads as closed | it is open in the Done list and stays untouched: 68c5a49e8491a9d7faf869d0 |
| identifier/format | ENG keys could collide | research/s4_carrier_formats.md: 0 collisions, max ENG 2437, ENG-2438 |
| identifier/format | Gmail thread ids off the base scale | (ms << 20) rule, leonard.hayes@harmonygames.co/1857029474983245439; Robert's reply sits in base thread leonard.hayes@harmonygames.co/1773963101399472184 |
| other | Linear is a product tracker with no investor project | origin stated by Leonard in C0ADGSZKR3R/1770938120.410229, and 'linear we keep during transition' at C0ADGSZKR3R/1770933601.686309 |
| other | the KPMG body lists its items where base bodies do not | forced: attachments return no bytes; the body says why, and that the financials are covered by leonard.hayes@harmonygames.co/1856787396431935562 |
| other | Robert has shown little interest in the shutdown | D04UGG61DUM says so, but he and Nebojsa are ex-coworkers with real traffic, and the reply gives its reason: leonard.hayes@harmonygames.co/1773963101399472184 |
| decision point: Who counts as a holder | only people holding something today: 20 lines is fair | project ec2ea957-fc8e-4958-b809-0fb735b1e916 (ENG-2438 to ENG-2463) states the cohort; the schedule shows Nothing for the six; leonard.hayes@harmonygames.co/<177093551461.10.12358585394423780893@notifications-email-sending-worker-5fc9459db-km7pv> is one such record |
| decision point: Is a past last day lapsed, or could the option have been exercised | ES-16's holder was trying to exercise (leonard@harmonygames.co_1847333990408253969.json) is fair | H1 f_a37b403d5200d4f0a31d31 closes it by rule, not by evidence of no exercise; the October notices predate those windows |
| decision point: Someone with stock and an open grant | the grant is a live option line that fires its own note is fair | H1 f_a37b403d5200d4f0a31d31: one row and at most one note per person; Carta's digests name all four grants (ES-9, ES-11 in leonard.hayes@harmonygames.co/1782897835407336831; ES-8, ES-10 in the seeded Nov 20, 2023 digest) and no termination, and Carta is the record |
| decision point: Does a channel post count as told | Oliver replied in the channel, so he knows (C05KNDCHAAG/1770839984.194409) is fair | H1 f_a37b403d5200d4f0a31d31: sent to them directly and delivered; a `<!here>` post is not |
| decision point: ES-14's channel membership | a listed member of #company-internal is fair | H1 sent-directly-and-delivered rule; NB-31; his exit leonard.hayes@harmonygames.co/<CAEH8bLxfNq9vp7-VSMQdpetPWQxBhv2pcPE=xj=oX9c8MxNFtA@mail.gmail.com> |
| decision point: Who may do the telling | only Leonard, who promised to personally reach out is fair | H1 f_a37b403d5200d4f0a31d31: from one of the three of us; leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>; the promise D04UC0UEN2V/1770665186.368229 |
| decision point: Is Griffin told through its partner | per-line, and no mail names the Side Fund is fair | H1 for a fund, its partner; leonard.hayes@harmonygames.co/1856675475513544349 message 13; one signer for both funds leonard.hayes@harmonygames.co/1774928765255297348 |
| decision point: Was Tor told in November | he heard about three months of runway (D09R59580EM/1762285888.654689) is fair | the DM never says the company is closing; H1's told rule names the closing |
| decision point: Does a Slack DM count for Segerstråle | it is not a side letter notice is fair | told and route are separate columns; D04UC0UEN2V/1770664988.379119 |
| decision point: Family contact | they hold individually, so three notes is fair | C0ADGSZKR3R/1770949310.220519 overrides leonard.hayes@harmonygames.co/1774211155651873582 ('holding shares individually'); Enes's own line stays First note |
| decision point: Does the family rule reach the Solsten pair | two holders at one company is fair | 'all three Disli brothers' leonard.hayes@harmonygames.co/<0CDD5A07-0BE6-4909-8188-93E10FBF4E16@librasoftworks.com>; the Solsten pair sign as CEO and COO, leonard.hayes@harmonygames.co/1770053656612413311 |
| decision point: Awards ending exactly on the as-of date | still whole on that day: 266,436 is fair | NEW leonard.hayes@harmonygames.co/1857029474983245439: each effective date as Carta shows it, regardless of when recorded |
| decision point: Effective dates entered late or chosen on Feb 11 | an audit should not use backdated entries (C07C2866011/1770827616.441769): 268,772 is fair | NEW leonard.hayes@harmonygames.co/1857029474983245439: each effective date as Carta shows it. A run that also flags the backdating must not lose a row |
| decision point: What 'fully diluted' means | four bases exist in the base is fair | NEW leonard.hayes@harmonygames.co/1857029474983245439 asks shares, options and their total; no percent of the whole is graded; leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com> |
| decision point: Is a personal note a notice | the note to Tor must copy TLAS is fair | NEW leonard.hayes@harmonygames.co/1857034369525983506 says formal notices are a separate step legal will walk him through later; no row fails if a run copies TLAS; f_0c37bb7235683d73569903 is the visible base line |
| decision point: Does Griffin still have to act | it resigned, so nothing is left is fair | charter draft f_90c029015fc474199cf736, Requisite Holders and 3.3.5 |
| decision point: Could Griffin's waiver remove the notice duty | Fourth B 8 lets the Requisite Holders waive class rights is fair | no row grades a notice deadline; f_90c029015fc474199cf736 |
| decision point: Who is on the board | all three founders ('it's just us and Griffin', Feb 11), or Leonard alone is fair | C04UEQVDVB7/1752517647.842649 fits two founders against Phil; Carta consents leonard.hayes@harmonygames.co/1838216168984971198; leonard.hayes@harmonygames.co/<CAMy0Hx1va3q4zH2HyPiqfm8Je2fm5A=JHKf8LrXWb12z2FHr6w@mail.gmail.com>; leonard.hayes@harmonygames.co/<BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com> |
| decision point: ES-17's date | letter Jan 22 against Carta Jan 28 is fair | both precede the clock; no row grades the exact date; leonard.hayes@harmonygames.co/<176175429549.10.8466995912642267217@notifications-email-sending-worker-6b65bf6cf7-gcpxf> |
| decision point: ES-5's end date | ledger pays him to Dec 31, so he could be live (NB-32) is fair | H1: Carta is the record; never grade his end date; leonard.hayes@harmonygames.co/1847333395311994879 |
| decision point: Who goes first | Griffin first, per Leonard's Feb 9 line; or the sheet first; or ES-14 on Carta's Oct 29 date for ES-3 is fair | H1 f_a37b403d5200d4f0a31d31; the sheet-first card 698e5a10c3f24b7e9d16a0e4 is about the work order, not the notes; D04UC0UEN2V/1770665186.368229; leonard.hayes@harmonygames.co/<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz@mail.gmail.com> |
| decision point: Is 'Akin' Matthew Collins | Akin is someone else, or a personal address is not his is fair | leonard.hayes@harmonygames.co/<CAMy0Hx2S+a4q+PUkFZM1ifrcEKv-y7AWWtQHrEsWg2qRxvFo3Q@mail.gmail.com> ('best / akin' from matthew.collins@harmonygames.co); leonard.hayes@harmonygames.co/<CAPBs_aLeDrdRoqOb0LrQ1AfGvbpmR-YdoG8A6PGmPay5Sc-ng=@mail.gmail.com> |
| decision point: Does a letter that bounced count as told | it was sent, and the rule's word is the message, not its delivery is fair | leonard.hayes@harmonygames.co/<698ce305.050a0220.3b7f1c.9d2e.GMR@mx.google.com> (550 5.2.1 inactive, nine seconds after the letter); H1's told line |
| decision point: Which Carta date governs ES-3 | Carta's Oct 29 termination notice: Jan 24, so it holds nothing is fair | H1 'Carta is the record'; leonard.hayes@harmonygames.co/<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz@mail.gmail.com> carries Carta's own later notice with the old date beside the new one; leonard.hayes@harmonygames.co/<176175436721.10.9685252272573766647@notifications-email-sending-worker-6b65bf6cf7-dg8x2> |
| decision point: Issue state by class | a Covered line stays Todo with the family note is fair | project ec2ea957-fc8e-4958-b809-0fb735b1e916 description; ENG-2438 |

Load-bearing base values re-read this session through hg.py: `00_PreScenario/verified_anchors.txt`, and independently recomputed by the fork sweep (research/sweeps/fork_sweep.md section 4).

`hardness_gate.py --design` result: HARDNESS GATE (extreme (design)): PASS

Unresolved: no dual red team (REDTEAM_* unset; fallback in §13). The platform pre-check proved gmail_create_draft (14 drafts), so the draft slots are live. The new rules' miss rates (BOUNCE about 50 %, EXT 55-60 %, ALIAS about 30 %, ADV 50-65 % after un-pointing) are cold estimates, UNCALIBRATED. All six runs clearing 130 calls is about even: low runs land near 139 and the platform's 100 is safe. Row floor about 118 against 120. ES-16's identity is by id only. Catch rates come from other personas. The under-70 aim and 62 % stretch are not supported. The Sunset request's fit with SOW page 7 (absent from the export) is unverified.

## 13 Red team (dual)

RED TEAM FALLBACK (rev2): REDTEAM_* is still unset (0 variables), so tools/redteam_review.py --dual cannot reach a reviewer. In its place, on the requester's instruction of 2026-11-08 ("use many subagents in parallel"), cold Claude subagents reviewed the rev2 design: four census scouts (research/rev2/census_a_bounce.md, census_b_carta.md, census_c_alias.md, census_d_adv.md), a leak audit (leak_audit.md), a cold coherence attack barred from the census files (attack_coherence.md) and a cold UGT attack barred from them (attack_ugt.md). They are not the dual red team, and this stays in every Unresolved line.

| Finding | Source file | Disposition with evidence |
|---|---|---|
| AC-N1a BLOCKING the told rule said "sent", and a bounced letter was sent | attack_coherence.md | Fixed: the notes say "a written message about the closing that reached them directly" |
| AC-N1b low "inactive" is the base's line for suspended work accounts | attack_coherence.md | Fixed: the 550 line now reads "is disabled. Learn more at ...", as the base's personal-address bounce (leonard.hayes@harmonygames.co/1768008486819265505) |
| AC-N2a low the Jan 23 change left no Carta admin trace | attack_coherence.md | Accepted as the single low item: a holder-side notice is how Carta tells the holder; an admin copy in Leonard's Carta stream would put the correction on the run's bulk Carta path (census_b V1, 20-25 % landing) |
| AC-N2b advisory no recorded reason for the extension | attack_coherence.md | Fixed: Calvin writes "Thanks for sorting out the extra weeks I asked for" |
| AC-N2c cosmetic thread id at .000 ms | attack_coherence.md | Fixed: thread 1856121753612004097 (.542 ms) |
| AC-N3 low a Feb 10 told-mail clashes with Leonard's Feb 10 notes and Feb 12 list | attack_coherence.md | Fixed: the mail goes Feb 12 22:52Z, after the list and before Robert's 23:41Z angel mail |
| LA-1..5 the prompt-round fixes hand over answers | leak_audit.md | Kept: BOARD, ASOF and the Griffin ask passed on the platform-era data without them; removing them reopens fail-level forks |
| CD-1 the #executives note and KPMG's item-1 sentence state the advisor split | census_d_adv.md | Fixed: numberless "go by the ledger" reply; KPMG's item-1 sentence removed |

RED TEAM UNAVAILABLE: REDTEAM_* is unset (0 variables), so tools/redteam_review.py --dual cannot reach a reviewer.

RED TEAM FALLBACK: four independent cold Claude agents (general-purpose subagents, no prior context, hg.py searches, told to break the design) reviewed it in place of the dual red team, on the requester's instruction of 2026-11-07 ('go with your recommendations on all six'): a fork sweep as the /prompt evaluator, a coherence sweep as the /injection evaluator, a run simulation as an Opus 5.5 adversary, and a delta review of the rewritten rule by a reviewer barred from the earlier reports. Reports: research/sweeps/fork_sweep.md, coherence_sweep.md, run_sim.md, delta_review.md. They are not the dual red team, and this stays in every Unresolved line until something covers it.

Summary: 5 blockers and 13 majors in the first three, then 3 blockers and 3 majors in the delta, all in sentences the first fixes had just written. No base record flatly contradicts the plan, every graded number recomputed, and the censuses found no other told holder, open equity question, family contact or option line. Every finding was weighed against the base before changing the design.

| Finding | Source file | Disposition with evidence |
|---|---|---|
| FS-01 BLOCKER four holders get two classes | fork_sweep.md | Fixed. H1: one row and one note per person, handled on their stock; §2, two-reading row. Avoids naming advisors, per LEAK-1 |
| FS-02 BLOCKER 'personal' has no sender | fork_sweep.md | Fixed. H1: from any of the three of us; two-reading row |
| FS-03 BLOCKER no class-to-state map | fork_sweep.md | Fixed. States in the project description, ENG-2438 |
| FS-04 BLOCKER no record says who goes first | fork_sweep.md | Fixed. H1: whoever's last day comes first |
| CS-01 BLOCKER project cites later records | coherence_sweep.md | Fixed. project updated_at follows the Sunset mail; created_at stays, §11 |
| FS-05 family sentence covers Enes | fork_sweep.md | Fixed. 'the rest of the family's lines, which need no note of their own' |
| FS-06 backdated dates | fork_sweep.md | Fixed. KPMG: regardless of when recorded; rows must not penalise a run that flags it |
| FS-07 graded totals have no ask | fork_sweep.md | Fixed. KPMG asks each option line and the total; Sunset asks the totals and counts |
| FS-08 newest board record omitted | fork_sweep.md | Fixed. two-reading row cites C04UEQVDVB7/1752517647.842649 |
| FS-09 comment count | fork_sweep.md | Fixed. 12, §2, §7, §9 |
| FS-10 resolvers not visible | fork_sweep.md | Fixed. seed says formal notices come later; research file no longer a resolver |
| FS-11 to FS-16, FS-18 | fork_sweep.md | Fixed in the two-reading and self-review rows, C07C2866011/1770837454.464209 added to T4 |
| FS-17, CS-06 Robert reads as planted | both | Fixed. Moved to Nebojsa, his ex-coworker; reply on their own thread leonard.hayes@harmonygames.co/1773963101399472184 with a reason in its first line |
| CS-02 'counts only' against FY24 | coherence_sweep.md | Fixed. body cites the Standard Metrics submission leonard.hayes@harmonygames.co/1856787396431935562 |
| CS-03 bare figures in comments | coherence_sweep.md | Fixed. quoted and dated, §11 rule |
| CS-04 last-contact values | coherence_sweep.md | Fixed. values from §1a; stamped before Robert's reply |
| CS-05 Tuesday against Feb 15 | coherence_sweep.md | Fixed. one line in H1 tying it to C0ADGSZKR3R/1770933601.686309 |
| CS-07 T3 resolver false | coherence_sweep.md | Fixed. T3 rewritten; deck attributes its figure |
| CS-08 Arthur has no Trello actions | coherence_sweep.md | Fixed. Leonard writes the card and comment; list id corrected to 640643a3fd8f3ca308d93195 |
| CS-09 to CS-22 | coherence_sweep.md | Fixed in §1a corrections, §11 and the Must-not list. CS-18: T9's Drive timestamp stays manifest-only, no row uses it |
| LEAK-1 rule doc as a trap index | run_sim.md | Fixed. neutral sentences; family moved to a DM; no sentence names a case |
| LEAK-2 'every angel investor' | run_sim.md | Fixed. K3 removed; H1 quotes no base sentence |
| LEAK-3 T7 caught by the plan's calls | run_sim.md | Fixed in part. reply sits on a 2023 thread dated Feb 12; address searches cut from 26 to 12. A run that searches his address still finds it, which is fair |
| LEAK-4 'board position' returns both | run_sim.md | Accepted. Base records; BOARD is not counted as a hard trap |
| LEAK-5 titles show the surname | run_sim.md | Fixed. owner-list forms; no Eren contact row |
| LEAK-6 ASK rows pass on a date note | run_sim.md | Fixed. Q1 needs an answer to the question; Q2 is now a date sample |
| LEAK-7 last contact leaks told state | run_sim.md | Fixed. none on ENG-2440, ENG-2446, ENG-2459 |
| LEAK-8 to LEAK-11 | run_sim.md | Fixed. 'any special terms'; Arthur row added; figures required. LEAK-9 accepted, T22 not counted |
| OH-1, OH-2 ASOF rows | run_sim.md | Fixed. selector accepts ES-16 or 35,605; KPMG asks each option line |
| OH-3 ASCII spelling | run_sim.md | Fixed. title uses Segerstråle, the base spelling |
| OH-4 weight on drafts | run_sim.md | Open. Pre-check proves it first; fallback is sends. In Unresolved |
| OH-5, OH-6 | run_sim.md | Fixed. B1 accepts either order; board row cites the call |
| Row tagging: 27 weight never flipped | run_sim.md | Fixed. K2, K3, A3, S1, S2 and the Tor rows untagged; lookups cut to weight 1 |
| Forecast: baseline 76 to 82 % | run_sim.md | Accepted. §6 now states 78 % central and that under 70 % is not supported |
| Delta F1, F2 BLOCKER state sentence decides 18 of 26 | delta_review.md | Fixed word for word: Canceled where the line holds nothing; otherwise Todo where its own note is waiting, Done where it isn't; ENG-2444 |
| Delta F3 BLOCKER 'addressed to them' lets `<!here>` in | delta_review.md | Fixed. 'sent to them directly'; ENG-2463 |
| Delta F4 Robert's line promised a note | delta_review.md | Fixed. line removed; promises nothing further; ENG-2446 |
| Delta F5, F15 KPMG wording | delta_review.md | Fixed. 'each effective date as Carta shows it'; closes ES-1, ES-4, ES-15 and Collins; leonard.hayes@harmonygames.co/1830959847543474636 |
| Delta F6 dangling pointer to the family rule | delta_review.md | Fixed. At injection the line moved to a reply under the Feb 12 list, which H1 names twice and every run must write under |
| Delta F7 to F14, F16 | delta_review.md | Fixed. §4 amendment names the family sentence; 'at most one note'; Robert copy row robert@harmonygames.co/1773963101279916523; a dated last contact on all 26 removes the gap (ENG-2440); 'their total'; ES-4 only |
| Delta: reason comments had no carrier | delta_review.md | Fixed. the state sentence now requires them; ENG-2452 |

## 14 Revision intake (S0r)

Verdicts consumed: run_forensics/rev1p/precheck.node_verdicts.json, from `/create-hardening` MODE B (`Working_Files/01a_Hardening_Report.md`, gate PASS pasted). `node_verdicts.py` refused the run (binding AMBIGUOUS), so the file holds no proposed rule verdicts. Every node below was dispositioned by hand from a full read of all 237 calls (`research/rev2/forensics_nodes.md`) and every write payload (`research/rev2/surface_handdiff.md`, hand score 79.5 %, one root cause).

Revision binding: the pre-check export precheck is historical. It ran on the platform SQL bc72db9c (input-store revision 3, not stored locally; nearest copy `run_forensics/rev1p/`, 6f3b18994e1a), so it binds by the platform hash only and certifies no revision. rev2 is built on the local rev1 (fd51afbf63aa, `run_forensics/rev1/`).

| Node | Runs | Proposed (by hand) | Disposition | Evidence |
|---|---|---|---|---|
| ADV | precheck (historical) | LANDED (fair: the sizes mail was one fetch away) | rebuild: un-point it. Delete the Jan 14 #executives sentence that states the split and KPMG's item-1 sentence that gives 3,051,879; leave the Due Diligence advisor table and the term-sheet ledger as the deciding records, with a numberless "go by the ledger" reply under the ChatGPT post as the only bridge. A2 leaves ADV (it is the same under both readings). | precheck event 502 fetched thread 1773160163779741845 metadata-only; precheck event 562 read the 3,051,881 total and precheck event 835 explained it away; writes at precheck event 783 and 944 |
| LETTER | precheck (historical) | LEAKED (bulk) | keep as a gradable fact; the new BOUNCE rule adds the missing piece the letters hide | the done line at precheck event 35, six letters in one batch at precheck event 394, all eight Carta entries at precheck event 250 |
| TOLD | precheck (historical) | LEAKED (bulk) | keep | the Feb 9 DM at precheck event 523 from the after:2026-02-08 search at precheck event 414; Robert's reply at precheck event 314 |
| ASOF | precheck (historical) | LEAKED (same container) | keep; the vested-only sentence settles a fail-level fork (leak audit item 1) | the request and its clarification in one thread at precheck event 61 |
| FAM | precheck (historical) | LEAKED (first read) | keep | the rule at precheck event 28; Enes's mail at precheck event 540 |
| BOARD | precheck (historical) | BYPASSED | keep as a gradable fact (B1); count it for no difficulty | resolver ids only at precheck event 59 and 609; the board came from Carta consent lists at precheck event 250 |
| ASK | precheck (historical) | LEAKED (bulk) | keep | the question at precheck event 419 |
| BOUNCE (new) | none yet | — | rebuild (new rule, v2 trap 1): a delivery failure in Owen's Feb 11 letter thread makes ES-12 untold | the run read the letters by message id at precheck event 394 and never opened their threads |
| EXT (new) | none yet | — | rebuild (new rule, v2 trap 2): Calvin forwards Carta's Jan 23 update (ES-3 last day Feb 20) from his issue address on Feb 3 | the run fetched only Carta message ids from its carta results (precheck event 207 to 237); its date windows began Feb 8 (precheck event 294, 381) |
| T3, T8, T15, T16, T21, T22 | precheck (historical) | decoys never on the path | keep (they settle forks); count for nothing | ids only or never surfaced: precheck event 58, 71, 72, 92 |

Routing: universe changes (ADV, BOUNCE, EXT) go to `/create-injection` rev2 from S5a; prompt-side defects: none, `04_Prompt.txt` stays byte-identical; OE and rubric notes (advisor options graded as the outstanding grant; Owen's draft address not graded; ES-8/ES-10 graded per holder) wait for `/create-oe-writing` and `/create-rubric-writing`. Candidate (c), Collins told as "Akin", is held pending the cold UGT and coherence attacks (`research/rev2/attack_ugt.md`, `attack_coherence.md`).


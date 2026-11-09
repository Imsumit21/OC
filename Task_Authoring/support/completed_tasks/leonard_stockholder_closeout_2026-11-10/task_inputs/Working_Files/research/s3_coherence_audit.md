# S3 coherence audit: active-speaker, identity and storyline inputs (Leonard stockholder close-out)

Facts and locators only. No prompt, Oracle Event or rubric text. Written 2026-11-07, universe normal, clock 2026-02-14 00:00 UTC. Status: COMPLETE.

Short names: LIST is the owner list (`1816809274978043917`[0], Slack `C04UEQVDVB7` 2024-11 idx 55). DD is Due Diligence Disclosures (`f_6a37227593d0977fdbdd7a`). C2 is `00_PreScenario/census/census_C2_holders.md`. ADV, OPT, TOLD, SIDE, BOARD, ASOF, FAM, ALIAS and CAP are the channels in `00_Pre_Scenario_Analysis.md` §5.

## 0. Verdict and what should change the design

**Verdict.** Storyline A survives. Nothing in the base blocks it, and the spine holds:
- All 14 Carta notices and the certificate digests re-read and match C2.
- LIST is identical across Leonard's mail, Arthur's mail and Slack.
- The four charter copies differ only in masks.
- No scope id hits an L or R hazard token.

But the audit found one census error that changes a holder's call, two errors in the analysis, and several forks the sketch does not close. Twelve items follow, most important first. Items 1 to 3 change the design. Items 4 to 9 tighten it. Items 10 to 12 are corrections.

1. **Tor is not "no contact since May 2024". Fix C2 and use it.** On Nov 4, 2025 Tor's principal asked in `D09R59580EM`: "Do you send out any investor updates?… TOR has an end of year sync on investments." Leonard answered "running very low on cash", "about ~3 months of runway", and sent the Oct 14 board deck. Tor was warned, not told. It's free hardness: an unpointed base DM that changes Tor's note, with no seed. It may replace the planned CAP seed, whose modelled share is the smallest (97.9 % single-miss).

2. **`/contacts/159` cannot be handled as designed.** "Independent Director" is an undated system field. It is not a dated claim, `repaired` is unavailable (L01–L07 only), and a run that opens it has touched it. Either keep Contacts off the required path, or make correcting the board list an explicit, incorporated job. Don't rely on it as a decoy.

3. **The board at the clock is Leonard and Robert. Arthur is not a director in any system record.** "added you as a board director" reached only Leonard and Robert (all mailboxes). Consent approvals went to Phil, Matthew, Leonard, Robert (Aug 2024), then to **Phil, Leonard, Robert** (`1838216168984971198`, Jul 21, 2025). That last mail is a system-side record of Matthew's exit, better than his own mail for a non-owner voice. Against it: `#winddown` idx 25 tells all three founders "we are personally liable as bod members", and the Gemini notes say "themselves and Griffin". The BOARD channel needs this as a closed rule. A row that says "three founders" would be wrong.

4. **Drop every fully diluted percent and any option reserve figure.** The base has four bases and two reserves, and two of them are each internally consistent: $10M ÷ 10,172,940 = $0.983 with advisors on top of the pool, while LIST's 10,069,176 = 6,000,000 + 3,051,882 + 1,017,294 puts them inside it. A seed can only pick one. KPMG's seed should ask for share counts.

5. **"Exercised 0" is a snapshot at the notice date, not at the clock.** All six "lapsed" notices were sent before their window closed. ES-16's holder wrote on Oct 29 that they were trying to exercise, and Leonard answered "if you want to move forward we can surely figure it out" (`1847333990408253969`; INFERENCE that this is ES-16). "Lapsed" rests on the absence of any notice and on the Jan 22 tie, which stops two days before Jan 24. Put it in the method record as a closed rule and test it on all 14. The same rule must keep ES-9 live despite Matthew's resignation.

6. **"29 holders" and "cohort 26" depend on a rule the sketch has not stated.** Six of the 26 hold nothing at the clock, and ES-2 was never on LIST. A cold reviewer reads 20 live non-founder lines. State "everyone on a Carta record, live or lapsed", or the count is a two-reading fork.

7. **SIDE is weaker than modelled.** Segerstrale's route ("two holders") rests entirely on the unread PDF. The Drive text binds only Tor. The Aug 29 draft added pro rata, later dropped at Leonard's request on Sep 8. New to the census: the party may be his entity, "Menlo capital LLC" (`1774541878774535160`[3]). Without decision 6, cut SIDE to Tor's route and "Segerstrale's side is a party".

8. **The Linear holder project has no precedent.** Linear has five product teams, two projects and zero comments, and its last issue is Nov 7, 2025. Leonard last authored there on 2025-11-01. The only base support is `#winddown` idx 188, "linear we keep during transition". Twenty-six issues plus the first comments in the export need a stated origin in a record, or the horizon carrier will read as invented.

9. **Sunset's method record collides with Sunset's own order.** Its flow is intake, then legal review, then Plan of Dissolution, then kickoff with a customer success manager. At Feb 12 22:34 UTC onboarding was still to do (idx 197, 200). No legal or success person exists in the base. Gemini notes also say Sunset "will provide investor notices". So the seed should be a pre-intake request from PERSON_2888 or PERSON_0767, and it must leave the formal notice with Sunset and the personal note with Leonard.

10. **LIST has a third copy, and it removes a trap.** `f_414596b0a9d698267dd1e1`, Leonard's Drive, Nov 2024, adds "Shares Available under 2023 Stock Plan - 5.874%", so "adds to 100%" is true (100.003). Trap D1's "LIST sums to 94.13 %" must not be framed as a false claim. The doc also names Owen Baker, so ES-12 moves to FULL. Add it to the shortcut audit.

11. **KPMG seed specifics.** Sender PERSON_3088; cc PERSON_4416, PERSON_2322, PERSON_2847; **not** PERSON_3077 ("[Deactivated]"). Real bodies are boilerplate with terms in a PDF, so the as-of date must sit in the body. FY24's own wording was Sep 30. Sep 30, 2025 avoids the Dec 31 fork (291,557 + 103,764 = 395,321 options) but loses ES-14's back-dating, which is ASOF's carrier. Dec 31 keeps it and needs the tie stated (266,436 or 243,757). Grade shares: Griffin's dollars have three values.

12. **Two corrections to the analysis.** `/cards/801` is **not** closed: `closed:false`, in Done, on an open board. And "the only investor update ever" is too strong: Tor got a board deck on Oct 17, 2023 and Nov 4, 2025, and a "March 25 Investor Update" deck exists (a GDC pitch deck, per `C07C2866011` 2025-03 idx 624). Say "the only update mailed to the holder group".

## 1. Hazard walk (six categories)

Source: `by_universe/normal/coherence_hazards.json`, all 68 ids. Scope here is the list in the job, plus the records a correct run reaches from it (`D09R59580EM`, `f_414596b0a9d698267dd1e1`, the Carta consent notices).

Terms used in the resolution column:
- **excluded**: per the playbook, the hazard's records are neither modified by the SQL nor cited by the design.
- **dated_claim**: an attributed, dated text claim that a later named record overturns.
- **repaired**: not used. No L01–L07 record is in scope.
- **class-touch**: the record belongs to the hazard's class and the design will cite it, but it is not in the hazard's example list. No verified resolution fits by meaning. Writing `excluded` would pass the gate and still be untrue, so write no acknowledgement and handle it by the stated rule. The category is not L or R, so the gate needs none.

Token test, run with `base_check.hazard_index()` and `id_tokens()` over about 55 scope ids: the only hit is `f_0c37bb7235683d73569903` (S07, Q07). No scope id hits an L or R example token, so `hazard_scope` will not fire unless the manifest cites one. The L and R acknowledgements below are still needed, because the job and the QC standard are about presence, not the token test.

### Temporal
| Id | Records | Why it touches | Resolution | Why safe |
|---|---|---|---|---|
| T02 | All 12 multi-message scope threads, e.g. `1856958794180374704`, `1817557789846606177`, `1775636449493308689` | Measured: every one is stored newest-first (`asc False, desc True`), so `[0]` is the latest message | class-touch | Each message's own date is correct and thread order is uniform. Rule: order by `date_parsed`, never by array index. Seeded replies are dated after their parent |

Checked, not touched: T03 (0 bad dates across 13 threads), T01, T04, T05, T06 (`/cards/801` is not an example; bump `dateLastActivity` only if a comment is ever seeded there), T07, T08.

### Semantic
| Id | Records | Why it touches | Resolution | Why safe |
|---|---|---|---|---|
| S06 | Contacts `/contacts/170`, `/108`, `/139`. Text: LIST signature "CEO", `#winddown` idx 21, 42 | Leonard signs CEO; the assigned role is Creative Director | excluded | Do not cite those Contacts rows. The prompt states no title. The signatures are dated text and carry no graded fact |
| S07 | `f_0c37bb7235683d73569903` (Gemini notes, Feb 11) | "the entity name is Robert Incorporated". The doc also holds the only base sentence on "board and stockholder consents" | excluded, **only if the manifest does not cite this doc** | No entity-name row. See §3 D: this doc is tempting as a BOARD source. Citing it hits S07 and Q07 |
| S05 | `PAYROLL_ROSTER` EMPLOYEE_0032 | Tempts a run to name ES-16 "Josh Dempsey" | excluded | Key by ES id, never by roster name |
| S02, S03 | Seeded Linear rows only | Cross-team parents, label sprawl | excluded | No cross-team parent and no new sprint-style label on seeded issues |

Checked, not touched: S01, S04, S08.

### Cross-service referential (acknowledgement needed)
| Id | Records | Why it touches | Resolution | Why safe |
|---|---|---|---|---|
| R04 | `#winddown` idx 22 (the hazard's own example, the folder link). Same class: `#admin_foundersonly` 2023-08 idx 504, 721, 856, "Harmony Games Cap Table" | Slack carries Google-native ids. The cap table sheet is **in no export**: gsheets "Cap Table" 0 hits, gdrive 0 hits, both scan_complete | excluded | Cite neither link. Name Drive files by title. Any seeded link uses a Google-native id with an exact title. A run that follows "our final cap table" hits a dead end, which is fair as long as no row needs that sheet |
| R08 | Any seeded GCal copy or invitation mail | Mail and calendars only partly agree (0.879) | excluded | No base invitation is cited. A seeded invitation mail gets its GCal rows (INT-11) |

Checked, not touched: R01 (seeded text must name no Linear key that does not exist), R02, R03, R05, R06, R07, R09.

### Quantitative
| Id | Records | Why it touches | Resolution | Why safe |
|---|---|---|---|---|
| Q07 | Same family as the examples: `D04UC0UEN2V` idx 24 "$12K", `#winddown` idx 151 "$11700", Gemini notes | Sunset's fee, quoted three ways in records a run opens | excluded | No fee is graded. DM idx 1 is cited, idx 24 is not. Scope already keeps Sunset's fee out |
| Q05 | `FIN-000061` (-35,500, 2023-09-13) | 2023-09 burn 99,107 against ledger outflow 134,607. The gap of 35,500 is exactly this row | class-touch | Not a true conflict: a note repayment is not burn. Use the row only for "founders are not note creditors". Grade no burn figure |
| Q10 | LIST: `leonard@…_1816809274978043917` and `blake@…_1816806726955267951` | Same RFC message, different tokens | class-touch | Measured: all 27 share and percent pairs are identical across Leonard's copy, Arthur's copy and Slack idx 55. Only the name tokens differ. Key by figure and id |

Checked, not touched: Q01–Q04 (`#winddown` parent idx 158 has reply_count 1 and its reply idx 202; 0 raw-shaped rows in the four scope Slack files), Q06 (only if a letter quotes cash), Q08, Q09, Q11.

### State / lifecycle (acknowledgement needed)
| Id | Records | Why it touches | Resolution | Why safe |
|---|---|---|---|---|
| L13 | Hazard examples are `Combo-Fighters#37` and `slack:C05KNDCHAAG:1770842137.835489` | The storyline sits on the shutdown. "Everything stopped on Feb 9" is false | excluded | Neither record is cited. The design's cut-off is the clock, and no row claims work stopped |
| L08 | Seeded Linear holder issues | 64 open base issues sit with quiet or departed assignees; a seeded issue could join them | excluded | Assign seeded issues only to Leonard, Robert or Arthur (`active_feb_2026`). Never assign a holder |
| L11, L12 | `/cards/801` is in neither list | Trello is a seeded service | excluded | Base cards stay untouched, and any new card goes in an open list |

Checked, not touched: L01–L07 (no base Linear issue is in scope; `repaired` is unused), L09, L10, L14.

### Identifier / format
| Id | Records | Why it touches | Resolution | Why safe |
|---|---|---|---|---|
| I03 | All Leonard threads, stored as `leonard@harmonygames.co_<id>` with `user_email` `leonard.hayes@…` | Universe-wide alias | class-touch | Cite by thread id. The seeded thread file convention follows the mailbox |
| I04 | Leonard's mailbox uses RFC-2822 dates; `threads/00001958` etc. use ISO-Z | Mixed date formats inside the Carta consent sweep | class-touch | Parse `date_parsed`. A seed follows its own mailbox's format |
| I14 | `f_31115ddb6ed866f2b10d60` Task List, `f_105b20100113e6d6cccbf6` Termination Notices, folder `d_e5caf6a8c630421942ee59` | Owner is `Resource: 7240535625619857401` | class-touch | Both files are shared with Leonard, and persona_view says YES. The folder itself has empty sharing |
| I15 | `Due Diligence Disclosures.docx` against its Doc title; truncated titles (`…Amended and Restated Cert(1)`, `Reset Financing Term Sheet (Washout Recap + Pay-to`) | Drive name differs from Docs title | class-touch | Name files by the Docs title or id. Never grade a filename |
| I10 | Seeded Linear rows | Malformed ids such as `usr_Victor Barnes` | excluded | Use `usr_63fffeb4fab5233e` for Leonard |
| I11, I12, I13 | Base board meetings (§3 D) | Rows and copies can differ per calendar | excluded | Used for the audit only, kept out of the manifest. Count by `(ical_uid, start)` if ever needed |

Checked, not touched: I01 and I02 (0 raw-shaped, 0 id mismatches in the four scope Slack files), I05, I06 (0 in 13 threads), I07, I08, I09, I16, I17, I18 (no struck-through text in `#winddown` or the DM).

## 2. QC seven-category walk

Format: record · category · fields · evidence pointer · hazard id · disposition (avoid / fold into design / designed claim + overturning record). Gmail ids are Leonard's threads and `[n]` is the message index. "LIST" is the owner list. All rows were re-read in this session except those marked lead.

**Temporal**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| `f_bc574824d936285e308cff` side letter copy | Title "draft 28 August(1)"; created 2023-06-29, modified 2023-07-25 | gdocs `/docs_documents/474` | none | **Avoid.** Cite `f_6201c7027d02997bfb2c84`, and never a Drive date on these files |
| `f_6201c7027d02997bfb2c84` | created 22:17:15Z is after modified 22:12:51Z, same day | gdocs `/docs_documents/238` | none | Avoid: no row on its timestamps |
| Carta ES-7, 12, 13, 18 against the Feb 11 letters | "as of Jan. 30, 2026" against "January 31, 2026" | `1856960351896429942`, `1856861323365646598` | none | **Avoid.** Grade "Last day to exercise" only, never an end date |
| ES-12 letter | "January 31, 2025" | `1856860994291529096` | NB-22 | Avoid: the Carta notice carries ES-12 |
| ES-17 exercise window | Carta "Jan. 28, 2026"; same-date leavers Jan 24; letter "window ends January 22, 2026" | `1847333272519888206`, `1847333318158821452`, `1847335165884050330` | none | **Designed claim + overturning record:** the letter says "Carta will show the exact numbers". All three dates precede the clock, so the state is unchanged. No row on the exact date |
| ES-14 | Terminated Nov 21, 2025; entered Feb 12, 2026; last day Feb 21, 2026 | `1856960478782792748` | none | Fold into design (ASOF) |
| KPMG as-of date | FY23 "as of December 31, 2023"; FY24 "as of September 30, 2024"; both under "year ended December 31" | `1788910618703813283`[0], `1817557789846606177`[2] | none | **Fold.** Both real bodies are boilerplate and the terms sit in an unread PDF. The seed must state its as-of date in the body, which is a departure from pattern |
| Tor wire | Value date Sep 21 [4], "didn't hit" Sep 22 [2], ledger Sep 21 | `1777052222643175480`, `FIN-000060` | none | Avoid wire dates |
| Investor draft | "runway of less than a month"; written Feb 9, before Feb 12's signing, resignation and Carta entries | `C0ADGSZKR3R` idx 7 | NB-3 | Fold: the deliverable rewrites it. No cash figure graded |

**Semantic**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| LIST | "Owners", "shares" for stock and options alike; Griffin one line | `1816809274978043917`[0] | none | Fold (ADV, OPT) |
| The "29 holders" cohort | 6 of the 14 option lines hold nothing at the clock; ES-2 is not on LIST | §3 B | none | **Fold, and close the rule.** See §0 item 6 |
| Contacts Matthew | job "Independent Director (investor/advisor, not an employee)", undated | `/contacts/159` | none | **Fold.** See §0 item 2 and §3 D. This is an undated system field, so it cannot be a dated claim. Reconciling it must be the stated job |
| Contacts Michelle, Thomas Baker | "General Counsel" against "My paralegal michelle" | `/contacts/142`, `/154`, `1777052222643175480`[19] | none | Avoid: no row on counsel titles |
| Contacts Patrick | "Business Development / Partnerships Manager" at `patrick@`; the same address is a Disli holder and Bergmann | `/contacts/144`, `1781310711617833275`[5], `1836075678772806708` | X02 family | Avoid: never grade an address. §6 |
| Solsten titles | "Arthur/Patrick - They are COO/CEO" against signature "CEO / Co-founder" | `1775636449493308689`[22], `1847629332615617366`[0] | none | Avoid titles for the Solsten pair |
| Due Diligence Disclosures | "intends to enter into advisory agreements", dated Jul 10, 2023. A statement of intent | gdocs `/docs_documents/262` | none | **Fold, with care.** It is the ADV overturning record, so cite it as "planned 103,764", and let the subtraction and the tie carry the proof |
| Update wording | "our first investor update" (May 2024) against an earlier board deck to Tor (Oct 17, 2023) | `1799418746420547240`[2], `C05TPHZA52P` 2023-10 idx 0 | none | Avoid "first" and "only": §3 |
| Gemini notes | "board consists of themselves and Griffin" | `f_0c37bb7235683d73569903` | S07, Q07 | Avoid citing |

**Cross-service referential**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| "Harmony Games Cap Table" | Slack link; no such sheet in the export | `C04UEQVDVB7` 2023-08 idx 504, 721, 856 | R04 | Avoid: no row needs it |
| Oct 31, 2023 closing mail | "Attached, please find a complete set" with `attachments=[]` on [6] | `1781310711617833275`[6] | none | Avoid: rely on the BCC list only. The closing binder is cited as an attachment of `1788910618703813283`[0], UNREAD |
| Carta cap table exports | Leonard sent KPMG "excel file that I generated from Carta" and "Cap tabled from Carta as of 12-17-2024". Metadata lists `att_0001.xlsx` on both, **but neither file is in the export** (`files`: no non-PDF attachment in either thread; 0 paths with the listed prefix) | `1788910618703813283`[0], `1817557789846606177`[2] | none | **Fold.** The authority exists in the story and cannot be opened. A run may say so. No shortcut, and no seed may contradict what it would show |
| Advisor agreements | Referred to by the DD table; visible to no persona | `f_c2c881ccc407fbdaeaa362` etc. (C2, lead) | none | Avoid citing them. ES-8 and ES-10 stay unnamed |
| Tokens across copies | `[PERSON_NAME_0801]` in Slack and `PERSON_1287_NAME` in mail for one line | Slack idx 55, Gmail [0] | X04 | Key by figure and id |
| Side letter, final text | "Side Letter TLAS(final).pdf" | `1777571840372992861`, `1777052222643175480`[7] | none | **UNREAD. See §0 item 7** |
| Side letter party | Segerstrale may be party through "Menlo capital LLC", new to the census; he invested personally | `1774541878774535160`[3], [2], [9] | none | **Fold:** grade "Segerstrale's side is a party", never the entity |
| Segerstrale dollars | "$100K", "giving up $25K" against $50,000 | `C04UM32UWKD` 2023-06 idx 492, 535; `D04UC0UEN2V` 2023-06 idx 59; LIST; DD | none | Designed claim + overturning record: Jun 2023 plans, overturned by 81,383 − 30,518 and the floor test |
| Tor's last contact | C2 says May 19, 2024. **Wrong:** Nov 4, 2025 Slack DM | `D09R59580EM` 2025-11 idx 0–2 | none | **Fold. See §0 item 1** |
| Nebojsa's last contact | C2 says Sep 15, 2025. Slack mpdm runs to Oct 24, 2025 | `C7442B7CD94B` 2025-10 | none | Correct the census; no row depends on it |
| Contacts coverage | No row for Sunset, KPMG, TLAS, Bergmann, Eren or the Griffin VP Finance | contacts search, 0 hits each, scan_complete | none | Fold: a Contacts seed must not imply these exist |

**Quantitative**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| LIST total | 27 lines sum to 94.129 % but say "adds to 100%" | Gmail [0], Slack idx 55 | none | **Designed claim + overturning record:** `f_414596b0a9d698267dd1e1` adds "Shares Available under 2023 Stock Plan - 5.874%", total 100.003 % |
| Fully diluted base | 10,172,940; 10,172,939; 10,069,176 (implied); 10,062,267. Griffin 27.278 %, 27.3 %, ~27.0 % | `f_a267353f7f351df0a2dc29` (no Leonard reach), `C07C2866011` 2026-01 idx 727, LIST, `C04UTBZL6AX` 2025-07 idx 5 | none | **Avoid.** Grade counts only |
| Option reserve | 1,017,294 against 1,121,058 | LIST base 6,000,000 + 3,051,882 + 1,017,294 = 10,069,176 exactly; idx 727 | none | **Avoid.** Both are internally consistent. $10M post ÷ 10,172,940 = $0.983, so the priced base puts advisors on top of the pool (reserve 1,121,058). LIST's base puts them inside it. No reserve row |
| Preferred count | 3,051,879 issued; 3,051,881 quoted; 3,051,882 designated | `f_11040fe5d66821bd6951aa`, idx 727, disclosure schedule | none | Fold: the 12-line sum settles 3,051,879 |
| ES-17 vested | Carta 34,439 against letter "34,409" | `1847333272519888206`, `1847335165884050330` | none | **Designed claim + overturning record:** only 34,439 ties to 54,529 |
| Claire Morgan | DD "0.038%" verbal against LIST 0.076 % (7,630), Carta ES-4 7,630 | gdocs `/262`, `1856960410709778333` | none | Designed claim + overturning record: Jul 2023 verbal, overturned by the Nov 2023 grant |
| Griffin dollars | $2,616,996.67 / $83,002.56 (SOP); $2,616,996.66 / $83,002.55 (Leonard to KPMG); $2,700,000 ledger | `1771880236343640719`, `1788910618703813283`[0], `FIN-000026` | none | **Avoid cents.** Grade shares |
| Angel ledger rows | Aug 200,000; Sep 50,000; Oct 50,000 against P&L Sep 75,000, Oct 25,000 (P&L: C2, lead). Rows of $25,600 and $24,400 match no holder | `FIN-000041` to `FIN-000078` | none | Avoid: only the $300,000 total is safe |
| Stakeholder count | "17 stakeholders" against 15 stock lines | `C04UEQVDVB7` 2023-08 idx 663 | none | Avoid |
| Seed price | Disclosure schedule "$1.0173" against $0.983 | `f_a267353f7f351df0a2dc29` (Leonard NO) | none | Out of reach; never cite |
| Term sheet options | 268,772 at Jan 22 against 159,706 at the clock | gdocs `/40`, 14 notices | none | Designed claim + overturning record |

**State / lifecycle**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| Trello "Existing Investor Update" | `closed:false`, list Done, moved there Nov 12, 2025; no sent record. **The analysis's "is closed" is wrong** | `/cards/801`, `/actions/5221`, `/5282` | none | Avoid: do not cite it. Correct the analysis |
| Task List | Every Status False, last modified Feb 10, though Helpshift was cancelled by Feb 11 | `/sheets_spreadsheets/76`, `C0ADGSZKR3R` idx 57 | I14 | Fold: cite only row 2 "Send email to investors", with idx 197 |
| Terminated yet active | Carta and letters end ES-4 and ES-15 at Dec 31, 2025; `activity.json` has Claire and Brian `active_feb_2026` (ES-15 = Brian is INFERENCE from the letter's "brian") | `1856960410709778333`, `1856861400116562076` | NB-1 family | Avoid: no row on who worked when |
| ES-16 exercise | Holder said they were trying to exercise; Leonard: "if you want to move forward we can surely figure it out". Notice shows 0 at Oct 29 | `1847333990408253969`[1], [0] | none | **Fold. See §0 item 5** |
| ES-9 after resignation | Matthew left the board May 1, 2025; no Carta termination | `1830959847543474636`, no notice in the census | none | **Fold:** the method record must state that an award with no termination stays live |
| Matthew's accounts | Confluence `is_active` False; Linear True; Slack `deleted` False | entity.py §6 | none | Avoid |
| Frederick on board invites | The Jan 14, 2026 invite lists him after his Oct 24 exit, `needsAction` (created Sep 17, 2025) | gcal `evt_8cdcb12b7b4e1346db999d` family | I13 | Avoid: stale invite, not attendance |
| Reset term sheet | Unsigned; no record supersedes it | `f_11040fe5d66821bd6951aa` | none | Fold: "proposed, never adopted" |

**Identifier / format**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| SSP-06, SSP-08, ES-8, ES-10 | Never named in any notice | C2 §2, digests | none | Never grade which is which |
| ES-1, 2, 5, 14, 15 names | Tokens only | Notices | NB-12 | Key by ES id. ES-12 is now named: `f_414596b0a9d698267dd1e1` "Owen Baker – 0.162%" |
| `PERSON_3083_NAME` | Solsten's Schaeppi, and also the signature on Arthur Blake's own mail | `1816809274978043917`[1] | X02 family | Avoid: §6 |
| Two addresses, one person | PERSON_3336 and PERSON_3335; PERSON_3935 and PERSON_3941 | §6 | none | Never grade an address |

**Other**
| Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|
| `#winddown` idx 105–106 | A live-looking OAuth credential in plain text. Not reproduced here | `C0ADGSZKR3R` | none | Avoid quoting. No seed repeats it |
| `#winddown` idx 192 | "from [Phil]" is an image; idx 193–194 react to it | `C0ADGSZKR3R` | none | UNREAD. It sits right beside the board resignation, so do not build on it |

## 3. Sibling-defect sweep

Method: literal sweeps over gdocs, gsheets, gdrive, contacts, confluence and Slack (`messages/*/*.json`), Leonard's mailbox, and all mailboxes for Carta board mail. Every zero below is `scan_complete`, with a positive control in the same request (for example `2,746,693` hits in the same Slack scan where `268,772` hits nothing).

**A. A stale option total (designed: term sheet 268,772)**
| Sibling | Value | Verdict | Action |
|---|---|---|---|
| Sum of grants | 334,284 (CALC, on no record) | Fair decoy | Keep |
| `C07C2866011` 2026-01 idx 727, 728 | Reserve 1,121,058 | **Actual conflict** with LIST's 1,017,294 base | No reserve row |
| `C04UTBZL6AX` 2025-07 idx 5 | FD 10,062,267, "Other investors & advisors ~1,315,574" | Modelling text, not a record | Avoid |
| `f_414596b0a9d698267dd1e1` | 5.874 % available = 591,454 of 10,069,176 | **Fair, and useful.** New. Closes the LIST gap | Fold |
| `1847335165884050330` | 34,409 vested | **Actual typo,** self-disclaimed | Fold as a decoy; the row pins Carta |
| Disclosure schedule | Pool 1,017,294 + Advisors 103,764 = 10,172,940 | Out of Leonard's reach | Never cite |

`268,772` appears only on gdocs `/40`. It has 0 hits in Slack and gsheets.

**B. A merged line (designed: LIST)**
| Sibling | What is merged | Verdict | Action |
|---|---|---|---|
| Griffin line on LIST | Two funds in 2,746,693 | Fair: floor test 686,660 needs two | Keep |
| Four advisor lines | Stock + options: 86,470, 81,383, 31,536 ×2 | Fair (ADV) | Keep |
| `f_414596b0a9d698267dd1e1` | Same 27 lines, percent only | Fair; a third copy of LIST | **Add to the shortcut audit** |
| `FIN-000044` $75,000; `FIN-000042` $50,000 | Disli family; two angels | Ledger rows do not map to holders | Avoid |
| `D04UC0UEN2V` 2023-06 idx 59 | "(Libra) $75K", "(Solsten) $25K" | Jun 2023 plan; it sits in the same DM a run opens | Fair decoy |
| Term sheet "Series Seed (all non-founder investors)" | One line of 3,051,879 | Fair | Keep |
| Option-only lines on LIST | Lapsed and live alike; ES-2 absent | **The "29 holders" problem** | §0 item 6 |

**C. A draft read as signed (designed: the side letter)**
| Sibling | State | Verdict | Action |
|---|---|---|---|
| Both Drive side letters | Unsigned; Tor-only; lack the effective-on-funding change. They differ only in masks | Fair | Cite one id |
| Charter ×4 (Leonard) | Jun 21, 2023. Measured: differ only in masks and `[____]` blanks | Fair, but **no filed text exists** | State "draft" |
| IRA ×4 (Leonard) | Differ in masks, plus "all future employees" against "all current and future employees" | Real wording difference, off-path | Avoid that clause |
| SPA, Voting, ROFR copies | Same pattern (C2, lead) | Fair | Avoid |
| Reset term sheet, framework | "for discussion", unsigned | Fair | Keep as decoy |
| `#winddown` idx 7 | Unsent | **Designed** | Keep |
| `#winddown` idx 5 | Sent as `1856675475513544349`[13] | Fair: a draft that **was** sent, a good contrast | Keep |
| `#winddown` idx 24, 174, 175 | Vendor drafts, not checked for sending | Off-path | Avoid |
| LIST versions | `f_414596…` Nov 5, Slack idx 55 Nov 26 18:38Z, mail 18:47Z. Slack is the draft of the mail | Fair: same figures | Key to the mail |
| IRA notice clause | A copy to Orrick "if notice is given to Stockholders" | **Unflagged by census.** A rule built on the IRA drags this in | Avoid, or state it |

**D. An out-of-date board list (designed: Matthew still listed)**
| Sibling | What it shows | Verdict | Action |
|---|---|---|---|
| `/contacts/159` | "Independent Director", undated | **Actual stale system field** | §0 item 2 |
| SPA drafts | "shall be 4 … Matthew Collins, [0509], [0357], and" | Fair: "As of the Initial Closing" | Keep |
| `1775636449493308689`[22] | "he is on our board" (Aug 2023) | Fair, dated | Keep |
| Jul 16, 2025 GCal | Matthew `accepted`, after resigning | **Fair:** his own mail says "very happy to join the board meetings etc going forward". A strong trap, no defect | Fold |
| Oct 14, 2025 and Jan 14, 2026 GCal | No Matthew; Arthur and Frederick invited; Griffin on neither | Attendance list, not a board list | Avoid |
| `1808816811200364470` (Aug 30, 2024) | Consent to Phil, Matthew, Leonard, Robert | Fair | Keep |
| **`1838216168984971198` (Jul 21, 2025)** | Consent to **Phil, Leonard, Robert only** | **System-side overturning record, new.** Carta shows the exit | **Cite for BOARD** |
| `1782198867266535233` (Nov 10, 2023) | Also lists `michelle.carter@` | Consent recipients are not exactly directors | Do not define directors as recipients of this one |
| "added you as a board director", "sent you a Board Consent", "Board consent approved" | All mailboxes, subject search, scan_complete: hits only in Leonard's and Robert's mail, none in `blake@…` | **Arthur has no director record anywhere** | §0 item 3 |
| `#winddown` idx 25 | "we are personally liable as bod members" to `@here` | Loose human claim | Designed claim + overturning record, or avoid |
| Gemini notes | "themselves and Griffin" | AI summary, S07 | Avoid citing |

Also swept with zero relevant hits: Confluence "Matthew Collins" (user row only), "board of directors" 0.

## 4. Known issues touched

All 33 cards were walked against the scope. A card's "Don't grade" value is never relied on.

| Card | Touched by | Disposition |
|---|---|---|
| NB-1 Slack access after Feb 11 | `#winddown` idx 88–95 itself describes the guest change | Seeded Slack only from Leonard, Robert or Arthur, in founder channels or DMs. No row on who can read what |
| NB-3 Cash at Dec 31 / Jan 31 | Draft idx 7 "runway of less than a month"; `D04UC0UEN2V` idx 24 | No cash figure in any row. Percentages of preferred only |
| NB-4 February payments | Sunset's fee, `1856956473569789052` "Your payment" | No row on whether Sunset was paid |
| NB-5, NB-8 Helpshift | `#winddown` idx 18, 57. In the channel a run reads, off-path | Avoid; the letter must not cite a vendor balance |
| NB-6 Slack after Feb 13 10:03 UTC | Every seeded Slack row | Seed window for outreach state: Feb 12 22:17 to Feb 13 10:03 UTC. No reference to later Slack |
| NB-12 Token-only names | ES-1, 2, 5, 14, 15; DD names; Task List rows 8, 9 | Key by id. Accepted name forms include the token |
| NB-15 Employee or contractor | LIST mail: "one Washington-based employee"; `#winddown` idx 42: "no US employees"; Feb 11 letters: "independent contractor" | Dated and compatible: the 2024 marketing hire left Oct 2025 (INFERENCE, ES-17). No row on status |
| NB-20 Board marketing figure | Only if a board deck is opened (Tor received `Harmony Games BoD Oct 14 2025 (1).pdf`) | Avoid: UNREAD and off-path |
| NB-22 Letter date | ES-12's letter `1856860994291529096` says January 31, 2025. The card's "00016874" is the file `threads/00016874.json`, another mailbox's copy of the same letter | Grade ES-12 from its Carta notice |
| NB-24 No Linear comments | Measured: `/comments` is `[]`. Seeded comments would be the first in the export | **Fold.** Allowed, but see §0 item 8 |
| NB-29 Decision date | `#winddown` opens Feb 9 | No decision date as a window start. The told-state rule runs from a written record, not this date |
| NB-31 DM member lists | `D04UC0UEN2V` lists 5 members, `D09R59580EM` lists 4 | Never argue who saw a DM from members. Told state rests on authored messages |

Not touched: NB-2, 7, 9, 10, 11, 13, 14, 16, 17, 18, 19, 21, 23, 25, 26, 27, 28, 30, 32, 33. Keep NB-9 and NB-26 out of the letter: the draft mentions Combo Fighter, so a rewrite that adds platform or sales claims would walk into them.

## 5. Active speakers

`activity.json` has 40 people, all `@harmonygames.co`. **None of the eight external people below has a `status_at_clock`, and none is in `people`.** The value here reads "not in activity.json". `stage_gate.kb_activity_rows` skips unresolved rows and `base_check.Activity.judge` returns None for them, so the gates pass silently and the check below is the only proof. "Last authored" comes from a complete `from`/`to`/`cc`/`bcc` census of Leonard's mailbox, this session.

Person · email · status_at_clock:

- Leonard Hayes · leonard.hayes@harmonygames.co · active_feb_2026 (last Slack 2026-02-13, last Gmail sent 2026-02-12, last Linear 2025-11-01)
- Robert · robert@harmonygames.co · active_feb_2026 (last Slack 2026-02-13, last Gmail sent 2025-11-18, last Linear 2025-10-20)
- Arthur Blake · arthur.blake@harmonygames.co · active_feb_2026 (last Slack 2026-02-12, last Gmail sent 2026-02-04, last Linear 2025-10-27)
- Griffin partner PERSON_4337 ("Phil", Senior Partner & Co-Founder) · PERSON_4337_EMAIL · not in activity.json · last authored 2026-02-12T22:05Z, `1856958794180374704`[1]
- Griffin VP Finance PERSON_2847 · PERSON_2847_EMAIL · not in activity.json · last authored 2024-12-17, `1817557789846606177`[3]; last cc 2026-02-12
- KPMG PERSON_3088 · PERSON_3088_EMAIL · not in activity.json · last authored 2024-12-18, `1817557789846606177`[1]
- KPMG PERSON_4416 · PERSON_4416_EMAIL · not in activity.json · last authored 2024-01-23, `1788910618703813283`[1]; last cc 2024-12-18
- Sunset CEO PERSON_0767 · PERSON_0767_EMAIL · not in activity.json · last authored 2026-02-12T22:22:58Z, `1856675475513544349`[1]
- Sunset Head of Partnerships PERSON_2888 · PERSON_2888_EMAIL · not in activity.json · last authored 2026-02-11T23:11:52Z, `1856872398290956689`[2]; last cc 2026-02-12
- TLAS PERSON_5593 · PERSON_5593_EMAIL · not in activity.json · last authored 2025-07-26, `1838482551095945310`[0]
- Tor principal PERSON_5275 · PERSON_5275_EMAIL · not in activity.json `people`; `slack_only_ids.PERSON_5275_SLACK_ID` last 2025-11-04T21:24:19Z, 20 messages; last mail 2024-05-19, `1799418746420547240`[0]

Others a design may touch:

- Matthew Collins · matthew.collins@harmonygames.co · no_authored_activity. This is a keying artefact: he has no mailbox, yet he wrote `1830959847543474636`[3] and `1847258343060233599`[0] (Oct 28, 2025). A seed from him draws a voice-realism warning
- Segerstrale · PERSON_3336_EMAIL, PERSON_3335_EMAIL · not in `people`; `slack_only_ids.PERSON_3335_SLACK_ID` last 2026-02-12T20:27:04Z, 504 messages
- Victor Barnes · victor.barnes@harmonygames.co · quiet_since_2025-04. ES-6 holder: a cohort row only. He cannot review, approve or reply (playbook S1)
- Frederick Stone, Calvin Price · quiet_since_2025-10. Holders only, no voice

Seeding notes:
- **KPMG.** Use PERSON_3088 as sender on the FY24 pattern, with cc PERSON_4416, PERSON_2322, PERSON_2847. **Drop PERSON_3077:** PERSON_2847's Dec 17, 2024 header shows "[Deactivated]". Leonard's FY24 line "I missed the previous one" supports a reminder pattern.
- **Sunset.** No legal or customer-success person exists in the base. A method record from one would be a new external identity. Base voices are PERSON_0767, PERSON_2888 and PERSON_3131 (Sunset CTO, cc only, never authored). Sunset's own flow is intake, then legal review, then Plan of Dissolution: see §0 item 9.
- **PERSON_5593** has been quiet on this company since July 2025 and declined the counsel role then (`1838482551095945310`). A seeded TLAS voice on Tor's behalf is plausible only as a reply to something.
- **PERSON_4337** is live and non-owner, and is the strongest voice for a consent-side record.

## 6. Identity

Commands: `~/.local/bin/python3.12 -B Task_Authoring/tools/entity.py collisions` and `... resolve <name>`, default task, run from the workspace root. Output below is verbatim.

**Bottom line.** entity.py cannot resolve any external holder by name. "Philip Sanderson", "Kristian Segerstrale", "Bastian Bergmann", "Tor", "Patrick Lewis" and every Disli name return no exact match. Several PERSON tokens exist only as Contacts rows with a blank name. The pins below come from mail and Carta, not from the tool.

### Pins: correct entity against lookalikes
| Correct entity | Lookalike | How to separate them | Rule |
|---|---|---|---|
| Leonard Hayes, `leonard.hayes@…`, Slack `EMPLOYEE_0038_SLACK_ID`, Linear `usr_63fffeb4fab5233e`, Trello `PERSON_6094_TRELLO_USER_ID` | Thread alias `leonard@…`; Drive copy of LIST shows `leonard@harmonygames.co` | Same person, I03 | Cite the id, state no title |
| Robert, `robert@…`, Slack `EMPLOYEE_0016_SLACK_ID` | Tokens [0054], [0055], [0174]; "Robert Incorporated" in the Gemini notes | Token aliases per C2; the entity name is a notes error | No row on an entity name |
| Arthur Blake, `arthur.blake@…`, Slack `EMPLOYEE_0025_SLACK_ID` | **Arthur Schaeppi** (Solsten, SSP-04). `PERSON_3083_NAME` also signs Blake's own mail (`1816809274978043917`[1]). "Blake" and "my CTO Blake" appear in mail | Surname always. Holder is keyed SSP-04 | Never write "Arthur" alone |
| Griffin partner PERSON_4337 = Philip Sanderson (name seen in Carta `1774928765255297348`) = "Phil" = [1999] (INFERENCE, C2) | [PERSON_NAME_2000] is the firm; PERSON_2717 is another Griffin investor (`1843007315645862923`[2]) | Signature "Senior Partner & Co-Founder" | Holder lines are the two funds, not the person |
| Griffin II SSP-01 and Side Fund SSP-02 | "GRIFFIN GAMING PARTNERS" as one line | Floor test | Two holders |
| Segerstrale: PERSON_3336 mail, PERSON_3335 mail and Slack; [0089] [25152], [0090], [6550], [6407], [6201]; "Kris", "Christian" | Menlo capital LLC; Tor's [0128]; [PERSON_NAME_6423], a third party in the same DM | `D04UC0UEN2V` idx 3, 12 show [6423] is someone else | Keyed SSP-03 |
| Tor: TOR Capital Limited (SSP-11) | Principal PERSON_5275 = [0128], [0129]; directors' signers PERSON_5137, PERSON_0711; counsel PERSON_5593 | Holder is the company: "cap table should have TOR Capital Ltd vs my name" (`1775636449493308689`[20]) | Note goes to the principal, holder line is the company |
| Patrick Lewis (mail, Turkish) = Patrick Haktan Disli, a Disli brother | **Bergmann** ("patrick" in 2025 mail, Solsten, `1836075678772806708`, `1833542911997635888`), and Contacts `/144` "Patrick", staff title | Mask collapses both onto `patrick@harmonygames.co`. Oct 31, 2023 BCC carries PERSON_0693 and `patrick@` as two people | Never grade an address. Bergmann keyed SSP-05 |
| Schaeppi SSP-04: PERSON_3063 personal, PERSON_3083 work | Arthur Blake; Slack "Joe Schaeppi" (C2) | §2 | Surname |
| Nebojsa ES-11, SSP-09: PERSON_3941, PERSON_3935, Slack `PERSON_3935_SLACK_ID` | entity.py flags `PERSON_3935` as an unjoined token_link. Slack user is a marketing voice in mpdm `C7442B7CD94B` to Oct 24, 2025; `1796464517368805372` and `1796465341448589349` show both addresses in one marketing sync. "IKE LOA LLC" (`1770577968081445872`) | INFERENCE: same person | Keep holder-of-record off the graded path |
| Deepak SSP-12: PERSON_1287, [2950], [0801] | ES-8 or ES-10 unnamed | DD and LIST by token | Never grade which ES |
| Matthew Collins `matthew.collins@…` = "Akin", Husnu Matthew Collins, [11362] | Mail signature "akin" | Carta SSP-10, ES-9 | Keyed SSP-10 |
| ES-12 Owen Baker | Thomas Baker (General Counsel in Contacts) | `f_414596b0a9d698267dd1e1` "Owen Baker – 0.162%" | ES id; P02 |
| ES-7 Marcus Bennett | Marcus Lee, Oscar Bennett, GitHub and Trello "Marcus" | Carta names him | ES id; P01, P02 |
| ES-3 Calvin Price | Nathan Price; two GitHub logins | Carta names him | ES id; P02 |
| ES-13 Martin Walsh | Martin Lewis; Carta adds a middle-name token | Letter `PERSON_4363_EMAIL`, "Hi Martin" | ES id; P01 |
| ES-18 Oliver Brooks | Lauren Brooks. **No Feb 11 letter exists for him:** a subject search of all mailboxes gives six recipients, none his | Carta names [0022] [2763] (C2 alias) | ES id; P02 |
| ES-4 Claire Morgan | GitHub "Claire", `PERSON_2360` | Letter to `PERSON_2360_EMAIL` | ES id; P01 |
| ES-16 EMPLOYEE_0032 | Josh Dempsey (`PAYROLL_ROSTER`, a separate entity with no activity); `cameron@harmonygames.co` (`1847333990408253969`) | INFERENCE that `cameron@` is ES-16: consulting-agreement exit Oct 24, Oct 2024 grant cohort, onboarding with Oliver. X02 | Never state a name |
| ES-17 [0038] = Frederick Stone | Letter addressed "ryan" `PERSON_2314_EMAIL` (S04) | Confirmed: the other-mailbox copy `threads/00015796.json` shows `"ryan" <frederick.stone@harmonygames.co>` | ES id |
| ES-15 [2769] [0093], "Omer" | "brian" `PERSON_4243_EMAIL` in the Feb 11 letter | INFERENCE only | ES id, no persona link |
| KPMG PERSON_3088, PERSON_4416 | PERSON_0467, PERSON_3710 (FY23 cc), PERSON_2322 (FY24 cc) | Signatures "Audit Associate" | Sender from the pattern only |
| Sunset PERSON_0767 (CEO), PERSON_2888 (Head of Partnerships), PERSON_3131 (CTO) | The Gemini notes spell "Jackie Alfenas", a raw name | Signatures | Keep the raw name out of seeds |

### Output: collisions
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
  - Gmail thread files of arthur.blake@harmonygames.co are named 'blake@harmonygames.co_*'
  - Gmail thread files of brian.foster@harmonygames.co are named 'brian@harmonygames.co_*'
  - Gmail thread files of calvin.price@harmonygames.co are named 'calvin@harmonygames.co_*'
  - Gmail thread files of claire.morgan@harmonygames.co are named 'claire@harmonygames.co_*'
  - Gmail thread files of frederick.stone@harmonygames.co are named 'frederick@harmonygames.co_*'
  - Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*'
  - Gmail thread files of leonard.hayes@harmonygames.co are named 'leonard@harmonygames.co_*'
  - Gmail thread files of oliver.brooks@harmonygames.co are named 'oliver@harmonygames.co_*'
  - Gmail thread files of owen.baker@harmonygames.co are named 'owen@harmonygames.co_*'
  - Gmail thread files of samuel.turner@harmonygames.co are named 'samuel@harmonygames.co_*'
  - Gmail thread files of simon.walker@harmonygames.co are named 'simon@harmonygames.co_*'
  - Gmail thread files of vincent.parker@harmonygames.co are named 'vincent@harmonygames.co_*'
  - Gmail thread files of felix.young@harmonygames.co are named 'felixyoung@harmonygames.co_*'
  - Gmail thread files of oscar.bennett@harmonygames.co are named 'oscar@harmonygames.co_*'
  - Slack handle 'thomas' (U05F0A0D12F) belongs to Thomas Baker <thomas.baker@harmonygames.co> but equals the mailbox local part of Thomas <thomas@harmonygames.co> [persona thomas]

LOOKALIKE_EMAIL_LOCAL_PARTS (2)
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>']
  - 'thomas@' vs 'thomaslee@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['? <thomaslee@harmonygames.co>']

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
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: 2 github identities ['PERSON_0003_GITHUB_USERNAME', 'PERSON_2137_GITHUB_USERNAME'] (joins: ['exact_email', 'exact_name'])

PERSONA_ROLE_VS_CONTACTS_JOB (5)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: roster role 'Game Engineer (Unity VFX)' vs Contacts job 'Game Engineer (Unity/VFX)'
  - Frederick Stone <frederick.stone@harmonygames.co> [persona frederick_stone]: roster role 'Co-founder' vs Contacts job 'Commercial Lead, Marketing & Business Development'
  - Leonard Hayes <leonard.hayes@harmonygames.co> [persona leonard_hayes]: roster role 'Co-founder & Creative Director' vs Contacts job 'Co-founder & CEO'
  - Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]: roster role 'Artist' vs Contacts job 'Artist (VFX & Animation)'
  - Robert <robert@harmonygames.co> [persona robert]: roster role 'Co-Founder & Creative Director' vs Contacts job 'Co-founder & Chief Product Officer'

SHARED_CONTACT_JOB_TITLES (5)
  Game Designer: ['Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]', 'Samuel Turner <samuel.turner@harmonygames.co> [persona samuel_turner]']
  Game Developer: ['Thomas <thomas@harmonygames.co> [persona thomas]', 'Lucas <lucas@harmonygames.co>']
  Game Engineer: ['Brian Foster <brian.foster@harmonygames.co> [persona brian_foster]', 'Victor Barnes <victor.barnes@harmonygames.co> [persona victor_barnes]']
  General Counsel: ['Michelle Carter <michelle.carter@harmonygames.co>', 'Thomas Baker <thomas.baker@harmonygames.co>']
  User Acquisition Manager: ['George Miller <george.miller@harmonygames.co>', 'Megan Wilson <megan.wilson@harmonygames.co>', 'Victoria Lane <victoria.lane@harmonygames.co>']

UNRESOLVED (12)
  [ambiguous_name] github: mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  [ambiguous_name] github: mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co'] -> candidates ['email:claire.morgan@harmonygames.co']
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

### Output: resolve
```text
### resolve: Leonard Hayes
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
### resolve: Robert
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
### resolve: Arthur Blake
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
### resolve: Philip Sanderson
no exact match for 'Philip Sanderson'
### resolve: PERSON_4337
ENTITY email:PERSON_4337_EMAIL  name=None  kind=unidentified  emails=['PERSON_4337_EMAIL']
  gdrive     share_recipient=PERSON_4337_EMAIL, files_shared_with=1   [join: exact_email]
  contacts   contact_id=3cb768c4ca8515702d29b703, name=PERSON_4337, email=PERSON_4337_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence
  last activity: -
### resolve: PERSON_2847
no exact match for 'PERSON_2847'
### resolve: PERSON_3088
no exact match for 'PERSON_3088'
### resolve: PERSON_4416
no exact match for 'PERSON_4416'
### resolve: PERSON_0767
no exact match for 'PERSON_0767'
### resolve: PERSON_2888
no exact match for 'PERSON_2888'
### resolve: PERSON_5593
no exact match for 'PERSON_5593'
### resolve: PERSON_5275
ENTITY email:PERSON_5275_EMAIL  name=None  kind=unidentified  emails=['PERSON_5275_EMAIL']
  contacts   contact_id=82103c829a5708060fb0b37b, name=PERSON_5275, email=PERSON_5275_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, gdrive, linear, github, trello, confluence
  last activity: -
  UNRESOLVED (token_link): same token number across services but no shared exact email/name: not joined  records=['contacts.email=PERSON_5275_EMAIL', 'email.email=PERSON_5275_EMAIL', 'slack.id=PERSON_5275_SLACK_ID']
### resolve: PERSON_3336
ENTITY email:PERSON_3336_EMAIL  name=None  kind=unidentified  emails=['PERSON_3336_EMAIL']
  gdrive     share_recipient=PERSON_3336_EMAIL, files_shared_with=20   [join: exact_email]
  contacts   contact_id=ca57f88d55376b4341c5b6d4, name=PERSON_3336, email=PERSON_3336_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence
  last activity: -
### resolve: PERSON_3335
ENTITY email:PERSON_3335_EMAIL  name=None  kind=unidentified  emails=['PERSON_3335_EMAIL']
  contacts   contact_id=1673c82fc650e0c42ab440d8, name=PERSON_3335, email=PERSON_3335_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, gdrive, linear, github, trello, confluence
  last activity: -
  UNRESOLVED (token_link): same token number across services but no shared exact email/name: not joined  records=['contacts.email=PERSON_3335_EMAIL', 'email.email=PERSON_3335_EMAIL', 'slack.id=PERSON_3335_SLACK_ID']
### resolve: PERSON_0693
no exact match for 'PERSON_0693'
### resolve: PERSON_3063
no exact match for 'PERSON_3063'
### resolve: PERSON_3083
ENTITY email:PERSON_3083_EMAIL  name=None  kind=unidentified  emails=['PERSON_3083_EMAIL']
  gdrive     share_recipient=PERSON_3083_EMAIL, files_shared_with=1   [join: exact_email]
  contacts   contact_id=aaf48372feabcf6490f30d7c, name=PERSON_3083, email=PERSON_3083_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence
  last activity: -
### resolve: PERSON_2275
no exact match for 'PERSON_2275'
### resolve: PERSON_2260
ENTITY email:PERSON_2260_EMAIL  name=None  kind=unidentified  emails=['PERSON_2260_EMAIL']
  gdrive     share_recipient=PERSON_2260_EMAIL, files_shared_with=1   [join: exact_email]
  contacts   contact_id=9498fdeb61155487c7a2eb59, name=PERSON_2260, email=PERSON_2260_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence
  last activity: -
### resolve: PERSON_3935
no exact match for 'PERSON_3935'
  candidate: email:PERSON_3935_EMAIL  None  ['PERSON_3935_EMAIL']
  candidate: slack:PERSON_3935_SLACK_ID  None  []
### resolve: PERSON_3941
ENTITY email:PERSON_3941_EMAIL  name=None  kind=unidentified  emails=['PERSON_3941_EMAIL']
  gdrive     share_recipient=PERSON_3941_EMAIL, files_shared_with=9   [join: exact_email]
  contacts   contact_id=a65131d8d9f49c59825ffdaa, name=PERSON_3941, email=PERSON_3941_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence
  last activity: -
### resolve: PERSON_1287
ENTITY email:PERSON_1287_EMAIL  name=None  kind=unidentified  emails=['PERSON_1287_EMAIL']
  contacts   contact_id=46aabf1857b0733da86c4649, name=PERSON_1287, email=PERSON_1287_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, gdrive, linear, github, trello, confluence
  last activity: -
### resolve: Matthew Collins
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
### resolve: Patrick Lewis
no exact match for 'Patrick Lewis'
### resolve: Patrick
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
### resolve: Kristian Segerstrale
no exact match for 'Kristian Segerstrale'
### resolve: Bastian Bergmann
no exact match for 'Bastian Bergmann'
### resolve: Tor
no exact match for 'Tor'
  candidate: email:victor.barnes@harmonygames.co  Victor Barnes  ['victor.barnes@harmonygames.co']
  candidate: email:victoria.lane@harmonygames.co  Victoria Lane  ['victoria.lane@harmonygames.co']
### resolve: Calvin Price
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
### resolve: Claire Morgan
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
  UNRESOLVED (ambiguous_name): mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co']
### resolve: Marcus Bennett
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
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of ['github:PERSON_0396_GITHUB_USERNAME'] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
### resolve: Martin Walsh
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
### resolve: Oliver Brooks
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
### resolve: Owen Baker
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
### resolve: Victor Barnes
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
### resolve: Frederick Stone
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
### resolve: Josh Dempsey
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
### resolve: Benjamin Clark
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
### resolve: Michelle Carter
ENTITY email:michelle.carter@harmonygames.co  name=Michelle Carter  kind=person  emails=['michelle.carter@harmonygames.co']
  slack      id=U1E2A024076, name=michelle, real_name=Michelle Carter, email=michelle.carter@harmonygames.co, is_bot=False, deleted=False, messages=0   [join: exact_email]
  gcal       calendar_id=michelle.carter@harmonygames.co, owner_email=michelle.carter@harmonygames.co, summary=Michelle Carter — primary, events=0   [join: exact_email]
  linear     id=usr_1e2a0240767eb09b, email=michelle.carter@harmonygames.co, name=michelle.carter@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=b7b148237a358f0eaf845a6d, username=michelle.carter, fullName=Michelle Carter   [join: exact_name]
  confluence id=user_STAFF_9, account_id=acct_STAFF_9, email=michelle.carter@harmonygames.co, display_name=Michelle Carter, is_active=True   [join: exact_email]
  contacts   contact_id=84ae5ae20147349f7ef89b77, name=Michelle Carter, email=michelle.carter@harmonygames.co, job=General Counsel, is_user=False   [join: exact_email]
  absent from: gmail, gdrive, github
  last activity: -
### resolve: Segerstrale
no exact match for 'Segerstrale'
### resolve: Schaeppi
no exact match for 'Schaeppi'
### resolve: Arthur Schaeppi
no exact match for 'Arthur Schaeppi'
### resolve: Sadik Enes Disli
no exact match for 'Sadik Enes Disli'
### resolve: Enes
no exact match for 'Enes'
### resolve: Eren Disli
no exact match for 'Eren Disli'
### resolve: Haktan
no exact match for 'Haktan'
### resolve: Disli
no exact match for 'Disli'
### resolve: Nebojsa
no exact match for 'Nebojsa'
### resolve: Deepak
no exact match for 'Deepak'
### resolve: TOR Capital Limited
no exact match for 'TOR Capital Limited'
### resolve: Griffin
no exact match for 'Griffin'
### resolve: PERSON_3131
no exact match for 'PERSON_3131'
### resolve: PERSON_2322
no exact match for 'PERSON_2322'
### resolve: PERSON_3077
no exact match for 'PERSON_3077'
### resolve: PERSON_5137
no exact match for 'PERSON_5137'
### resolve: PERSON_0711
no exact match for 'PERSON_0711'
### resolve: Julia Lawson
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
### resolve: Brian Foster
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
### resolve: EMPLOYEE_0032
ENTITY email:EMPLOYEE_0032_EMAIL  name=None  kind=unidentified  emails=['EMPLOYEE_0032_EMAIL']
  gmail      mailbox=EMPLOYEE_0032_EMAIL, threads=3, messages=3, first=2024-08-20, last=2025-10-24   [join: exact_email]
  gdrive     id=user_9cc553d0ac03, email=EMPLOYEE_0032_EMAIL, display_name=EMPLOYEE_0032_EMAIL, root_folders=['d_9cc553d0ac034a53de5e27'], owned_items=2, last_modified=2024-12-19, files_shared_with=117   [join: exact_email]
  linear     id=usr_EMPLOYEE_0032, email=EMPLOYEE_0032_EMAIL, name=EMPLOYEE_0032_NAME, is_active=True, last_activity=2025-10-24   [join: exact_email]
  contacts   contact_id=d4a339f7f6aafffdc2dabb9a, name=EMPLOYEE_0032, email=EMPLOYEE_0032_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gcal, github, trello, confluence
  last activity: {'gmail': '2025-10-24', 'gdrive': '2024-12-19', 'linear': '2025-10-24'}
  FLAG: tokenized Gmail mailbox: the data does not prove which person owns it
  UNRESOLVED (token_link): same token number across services but no shared exact email/name: not joined  records=['gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'confluence.id=user_EMPLOYEE_0032', 'slack.id=EMPLOYEE_0032_SLACK_ID', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME']
### resolve: cameron@harmonygames.co
ENTITY email:cameron@harmonygames.co  name=None  kind=person  emails=['cameron@harmonygames.co']
  gdrive     share_recipient=cameron@harmonygames.co, files_shared_with=1   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence, contacts
  last activity: -
### resolve: PERSON_2314
no exact match for 'PERSON_2314'
  candidate: email:frederick.stone@harmonygames.co  Frederick Stone  ['frederick.stone@harmonygames.co']
### resolve: Thomas Baker
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

## 7. Storyline placement

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
- `fundraising-finance-legal-harmonygames-builds-its-advisor-equity-program-v` b06 (2024-02-07): ADV.
- `fundraising-finance-legal-harmonygames--quarterly-board-cadence-and-invest` b03 (2024-04-12), b05 (2024-09-04): investor reporting, BOARD.
- `fundraising-finance-legal-2025-fundraising--the-crownfall-crypto-pivot-and` b04, b05, b06: only as background to the angels' last contact.

Beats are orientation only. The prelude's "$3M Series Seed at $10M post" agrees with the price: $10,000,000 ÷ 10,172,940 = $0.983.

**cohorts.json: no fit — the cohort is 26 non-founder holders on Carta records, and no cohort id selects cap-table holders.** Nearest ids, none usable as the spine:
- `SF-LEDGER`: 704 ledger rows, 11 financing, one query returns all. Support only.
- `DOC-harmony`: 91 docs by title family, the charter, IRA and side letter copies among them. Support only.
- `TR-d93197`: Trello Done list, holds `/cards/801`. Its `hazards_inside` are incomplete checklists (L12 family, 4 cards) and actions later than `dateLastActivity` (T06 family, 5 cards); `/cards/801` is in neither. Not used.

`hazards_inside`: none to drop, because no cohort id is taken.

**trap_catalog.json ids:**
| Id | Applies to |
|---|---|
| D02 | Docs with identical bodies. `f_b0e408e1d051cec9dc7183` is listed, so the charter copies are a catalogued trap |
| D01 | Same title under different owners: Arthur's and Leonard's charter, SPA and IRA copies |
| D05 | Version markers: "draft 28 August", "(final).pdf" |
| D03 | BoD deck family: `Harmony Games BoD Oct 14 2025` |
| C04 | Human claim against record: LIST "adds to 100%", letter 34,409, DD 0.038 %, "bod members" |
| P01 | Shared first names: Marcus, Claire, Martin |
| P02 | Shared surnames: Baker, Bennett, Brooks, Price |
| X01 | Redaction tokens across services |
| X02 | EMPLOYEE_0032 and `PERSON_3083_NAME` |
| X04 | Uneven masks between copies of one mail |
| D07 | Trello stale against reality: `/cards/801` |

## 8. Integrations and companions

From `integrations.json`. The gate (`kb_integrations`) accepts an INT id, or `<service> none` with a reason, for each seeded service whose schema is a source. Only `linear`, `gcal`, `slack`, `trello`, `google_drive` have sources here.

| Service | INT entries | Base rate and rule | Companion needed |
|---|---|---|---|
| slack | INT-22 (Slack → Gmail, optional), INT-17 (Slack Connect notices, churn signal) | 603 mails, "Optional; never load-bearing" | None required. A reply into an existing thread needs the parent's `reply_count`, `latest_reply` updated (base_check). No Slack seed after Feb 13 10:03 UTC |
| gmail | Destination of INT-05, INT-11, INT-22; source of none | | `gmail`: none, no integration has Gmail as source. Own companions: thread file, message headers, `in_reply_to` in the same mailbox, RFC-2822 dates in Leonard's mailbox, a copy per mailbox only where the base keeps one |
| gcal | INT-11 → Gmail | Invites only partly match (0.879). The rule says "A seeded meeting does not need an invitation mail", but base_check warns at this rate | One GCal copy per attendee calendar, same `ical_uid`, copies agree. Invitation mail if the rate rule fires, or an `integration_exceptions` entry with `no_notify` |
| linear | INT-04 → Slack; INT-05 → Gmail (INT-03 needs a PR, not applicable) | INT-04 window ends 2026-01-28: "a seeded Linear state change does not require a Slack notice". INT-05: "a seeded Linear comment does not need a mail" | No mirror. Own companions: project and issue stamps, `updated_at` not older than its comments, lifecycle fields. **A seeded INT-04 notice would fall after the mirror's last base date, so add none** |
| gdocs, gdrive, gsheets, gslides | INT-13 (Drive → Slack DM) | 760 messages, to 2026-01-19. "DM-only; seeded doc comments need not have one" | No mirror. Own companions: `drive_files` row with the same owner and sharing. Leonard's root `d_63fffeb4fab5233ed5bb73`, never the `Resource:` folder |
| contacts | none in the catalogue | | `contacts`: none, no integration. A new row must not imply a Sunset or KPMG record the base lacks |
| trello | INT-21: no integration exists | "Do not seed Trello bot notifications in Slack"; `shortLink` is null on every card | No mirror. Own companions: `dateLastActivity`, badges, actions. Avoid `/cards/801`: it is open, in Done, and any new action would reopen a stale state |

**Two tight points.**
- Exactly 10 schemas are planned. `contacts` and `trello` have no base investor content worth seeding, so both risk being padding. Sunset and KPMG people have no Contacts rows at all, so a Contacts seed adds identities rather than facts.
- Slack is the one service whose seed window is narrow: 11 h 46 min between Leonard's Feb 12 22:17 UTC list and the export's end.

## 9. Not read / not done

**UNREAD by rule.** Gmail attachments and PDFs were not opened, and decision 6 is still open: the signed side letter (`1777052222643175480`[7], `1777571840372992861`), the Sunset SOW, the board decks, KPMG's confirmation PDFs. Slack images were not read, including `#winddown` idx 192 ("from [Phil]"). Any claim touching these is marked.

**Not in the export.** Both Carta `att_0001.xlsx` files, the closing binder zip, the "Harmony Games Cap Table" sheet, the `Shut_Down_List` canvas body. I checked these by file name only.

**Not re-read this session; leads from census C2.** SPA, Voting and ROFR copies beyond the board clause in `f_1be142fdb7a3bfe62f534b`; P&L monthly investor cash; the advisor agreements (no persona can see them); "Joe Schaeppi" in Slack; the wire threads.

**Scope limits on the sweeps.**
- Holder last-contact census: Leonard's mailbox by `from`/`to`/`cc`/`bcc`, complete for the 27 addresses listed. Other mailboxes were searched only for Carta board mail and termination letters.
- The hazard token test uses `examples`, which are capped lists for some hazards (T02 lists 10 of 3,144). "Class-touch" comes from measuring scope records directly.
- Q10 was measured on LIST only, not on every scope thread.
- ES-16 = `cameron@`, ES-15 = Brian, Nebojsa = Slack `PERSON_3935_SLACK_ID`, and `[PERSON_NAME_6408]` = Nebojsa are INFERENCE.

**Not run.** `stage_gate.py`, `hardness_gate.py` and `base_check.py` on a design: no manifest or SQL exists yet. Only their logic was read, and `hazard_index()` was called directly.

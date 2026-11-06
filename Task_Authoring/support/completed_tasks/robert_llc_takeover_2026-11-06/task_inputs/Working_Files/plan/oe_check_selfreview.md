## Self-review

**1. Re-read as the eval** (2_Oracle_Events_Eval.md, in order, against this report):
- **Phase 1.2 inventory.** All 104 segments are STEP. There are no headers, notes, response descriptions or non-actions.
- **Phase 1.3 five fields.** Every read names its service, what it reads and its search or pointer. Every decision step (OEs 20–23) cites the OEs it uses; its tool is not applicable. Every write names its target, its fields and the tool family, listed in the sign-off with its catalog parameters.
- **HARD GATE.** No event says what the agent refrains from doing or what the final answer says.
- **Phase 2.1–2.6.**
  - Service: every value is read where it lives, and the January revenue is Snowflake-only.
  - Tools: all are cataloged (Evals/references/tools/catalog.json).
  - Parameters: thread_ts 1770961200.890407; users /users/26, /users/13, /users/35; contacts /contacts/169 and /168.
  - Expected data: re-read below.
  - Clock: every record time is at or before 2026-02-14T00:00:00Z. Feb 28, Mar 1, Mar 3, May 31 and Monday's call are semantic future dates, and none is expected as done.
  - Act-vs-defer: ledger §C, no hold.
- **Phase 2.7 format.** One action per event, numbered, with a service; no arrows and no JSON.
- **Phase 3.1–3.6.** R1–R10 are covered by route. Each dependency is cited by OE number. After the fixes, no value is used before an earlier event or the prompt produces it: every search term comes from the prompt or an earlier event, as the Findings show.
- **Phase 4.0** is the 8-row sweep above.

**2. Counter-readings** (one per Coverage row, one per Finding, plus the value judgements the prediction rests on):

| Judgement | Counter-reading (strongest case against) | Resolution (evidence) |
|---|---|---|
| R1 covered (OE 1) | The best case it is missing: the agent reads another DM with Leonard, or an older message. | D04UP2L3E3S has exactly Robert (EMPLOYEE_0016) and Leonard (EMPLOYEE_0038), per hg.py slack channels.json /414. The message is Thursday night, ts 1770961200.890407 (SQL L54). Holds. |
| R2 covered | The best case it is partial: the DM also asks "what the LLC takes if Sunset can't sell it" and "we decide on Monday's call". | The take question is answered by the calls (OEs 20–22) under SQL L15's "only through Sunset's sale". "We decide on Monday's call" asks for no write (F8). Holds. |
| R3 covered (OEs 2–4) | The best case it is missing: comments read for only some issues. | OE 4 reads all 37, one call each. SQL L145–L289 hold exactly one comment per issue (counted). Holds. |
| R4 covered | The best case it is partial: a superseded figure (the draft's ~1000 and ~300, ENG-2441's $1k, ENG-2445's $95) is used. | OE 21 names the governing figure and dates the one it replaces: F10 SQL L51 at 03:10Z after SQL L157; F14 SQL L92 at 04:20Z after SQL L173 at 00:58Z; F12 SQL L68 after SQL L181. Holds. |
| R5 covered (OEs 25–62) | The best case it is missing: the new VO issue gets no call, or a comment states only a label. | OE 25 comments on the new issue. Each comment in OEs 26–62 states the call and its reason (F29–F66). "Leave the call" needs no more. Holds. |
| R6 covered (OEs 100–101) | The best case it is partial: the sheet lands outside Robert's own Drive, or the shares are missing. | OE 100 puts it at the top level of Robert's Drive (d_9f7ba94f7526d54d8482ba, hg.py gdrive data.json /drive_files/14368). OE 101 writes the shares per month, as SQL L80 asks. Holds. |
| R7 covered (OEs 102–103) | The best case it is missing: "both of them" could mean someone other than Arthur Blake. | The prompt and the DM say "Blake". Contacts give Arthur Blake, Co-founder & CTO (hg.py contacts.json /contacts/168), and Leonard at /contacts/169. Holds. |
| R8 covered (OEs 24, 63–99) | The best case it is missing: the VO line on the sheet has no issue, so the project cannot match. | OE 24 creates it, with Todo and Leonard under the SQL L140 rule (F66). Holds. |
| R9 covered (OE 104) | The best case it is missing: the reply goes to the channel top level, not "that DM thread". | OE 104 carries thread_ts 1770961200.890407 (SQL L54), and slack_send_message accepts thread_ts (catalog). Holds. |
| R10 covered (constraint) | The best case it needs a step: the agent must check the call time. | No write depends on it. The call starts 2026-02-16T18:00:00Z (evt_f5f279f282d20ec86bb8e5, SQL L121), after the clock, and every write runs now. Holds. |
| X1 OE 14 | The best case it was never a defect: "VO campaign" is a plain search phrase. | The blind reviewer found no earlier record on the path that names it, so it could fail §3.2. The new term "my card" traces to OE 8 and OE 12. Its target is the newest hit: hg.py search slack "my card" returns 31 base hits, none after 2025-10. Fixed. |
| X2 OE 12 | The best case it was fine: Robert received the mail, so he would know its subject. | The OE path is read as the agent, which learns the subject only from the mail itself. "metabase" ranks 1 of 17 by date (persona_view). Fixed. |
| X3 OE 11 | The best case it was fine: "prod account" is generic. | The first draft used the target's own possessive phrasing. "AWS bill" comes from SQL L165 and L173, and its only Robert-visible Slack hit is SQL L51. Fixed. |
| X4 OE 6 | The best case it was fine: Trello is unscoped and has few cards. | The title was still supplied before any event gave it. "LLC" finds two cards, and the other is closed (hg.py trello /cards/248). Fixed. |
| X5 OE 7 | The best case it was fine: the DM's "my draft" plus a Drive search reaches it anyway. | Agreed it was reachable. The fix names the natural query, and Drive shows three LLC files (SQL L6, L9, L11). Fixed. |
| X6 OE 8 | The best case it was fine: "LLC money" is built from DM words. | Arguable either way. "split" is the DM's own word, rank 1 of 135 by date (SQL L80 newest). Fixed. |
| X7 OE 2 | The best case it was fine: listing projects finds it at once. | True, but "from OE 1" claimed a name OE 1 does not give. Now it says to search, with one match (SQL L140; hg.py search linear "LLC"). Fixed. |
| X8 OE 17 | The best case it was fine: the short quote is verbatim. | Verbatim, but it reads as intent. The longer quote shows the subsidiary was set up (hg.py slack messages/C04UEQVDVB7/2023-12.json /501). Fixed. |
| X9 OE 9 | The best case it was MINOR: the quote is right and only its post is implied. | The Minor test treats a date or record attribution the universe contradicts as INACCURATE. /190 is ts 1770933903.645709, not /188. Fixed, with its own time. |
| X10 OE 7 | The best case it was fine: "?" sits after the item name. | It could be read as Game. The blank cell is now explicit (SQL L23). Fixed. |
| X11 OE 101 | The best case it was fine: VO has no deadline of its own. | The card's "everything else moves by March 1" (SQL L56) applies, and the reply says "from March" (SQL L45). By Mar 1 is now stated. Fixed. |
| X12 OE 101 | The best case it was fine: "by Feb 28" vs "before Feb 28th" is representational. | It is one day looser than the record (SQL L237; hg.py /57). It now uses the record's wording. Fixed. |
| X13 OE 16 | The best case it was fine: ENG-2462 is in OE 4 already. | It was there, but the event did not say why it searches mail, or that the target is the newest of 4,165 hits. Both are now stated (SQL L100). Fixed. |
| OE 10 figures | The best case they are wrong: another revenue table, or revenue net of the store cut. | The doc names "the warehouse's daily revenue table" (SQL L15), which is REVENUE_DAILY. The blind reviewer found REVENUE_DAILY_V2 gives the same sums, and DD net of a 30% IAP cut is 162.46, still above 140. 0.00 holds because total_revenue_usd is NUMBER(38,2) (Evals/references/schema/snowflake.json). Holds. |
| OE 21 CF at 62 | The best case it is wrong: ENG-2445's "about $95" governs because the calls live in Linear. | The ground rules cost each item "at what it bills now, going by whoever runs it" (SQL L15). Arthur's mail (SQL L92, 04:20Z) is later than his comment (SQL L173, 00:58Z) and gives the reason: the extra backend copy is shut down. Holds. |
| OE 21 VO at 3,000 | The best case it is wrong: $100/day × 31 days in March is 3,100. | SQL L45 says "capped at $3,000 a month, and that's what it runs at from March". Holds. |
| OE 23 base 3,450 | The best case it is wrong: the shares are on what the LLC pays, 3,202. | SQL L80 says "including what one of us already pays for it". Arthur's 248 counts toward his third. Holds. |
| OE 22 Calm Play to HG | The best case is LLC: Leonard's 3:41 PM comment, "Calm Play could just be our LLC" (SQL L281). | The doc, changed at 3:46 PM (SQL L6, L15), says "The LLC is the new one Blake and I are setting up". Calm Play is HG's subsidiary (hg.py /501). Holds. |
| OE 22 Figma to HG | The best case is LLC: the draft's Figma row says LLC (SQL L23). | ENG-2453 (SQL L205) and Robert's #winddown post (hg.py /134) say HG prepaid it to Sep 11 and it stays HG's. The draft is the older record. Holds. |
| OE 22 ENG-2462 Todo | The best case is Done: Arthur says "done" (SQL L241, 01:30Z). | App Review rejected the build later, at 07:30Z (SQL L100), so something is still to do: Todo, with Arthur. Holds. |
| OE 22 Deel, Gusto and Intuit to HG | The best case is Founder: Leonard's "under mine" suggests he pays them. | The post (hg.py /188) keeps them under HG for the shutdown, and #winddown decisions stay decided (SQL L15). No founder pays them through May. Holds. |
| OEs 63–99 state names | The best case they are wrong: team ENG uses other state names. | hg.py linear data.json /issues/204, /0 and /40 carry Todo, Done and Canceled, and the project rule (SQL L140) names those three. Holds. |
| OE 24 is authorised | The best case it is unauthorised: the prompt never says to create an issue. | "When you're done, the project should match the sheet", and the VO is its own line on the sheet (SQL L45; F66). Holds. |
| Visibility | The best case a read is hidden from Robert. | persona_view check-sql shows PASS, with 0 load-bearing rows hidden (37 YES / 18 NO, the NO rows being other people's mailboxes). can-see YES for winddown, admin_foundersonly, prototype and d_9f7ba94f7526d54d8482ba. Holds. |

**3. Re-verify.**
- **Base records.** Every expected value was re-verified in this run. plan/oe_reads.py re-read all base records through tools/hg.py (lookup, then get-many). They match the earlier read key for key: slack, ptr, revenue_rows, revenue_table, misc, linear_state_hits.
- **Seeded records.** These were parsed from 01_Universe_Inject.sql as text.
- **Rebuild.** plan/assemble_oe_events.py rebuilt the file from those reads and asserted 96 quoted substrings against their own records before writing.
- **New reads in this check:**
  - channel records /154, /151, /15, /414 and /420;
  - the Trello board name and card /248;
  - the REVENUE_DAILY column types;
  - the catalog entries for the seven write tools;
  - the persona search ranks in plan/oe_locator_ranks.py.
- **Recomputed.** 183.11, 0.0 and 7.36 over rows 2044–2229; 62 rows per game; 3,450, 1,150, 902 and 3,202.

**4. Fixes.** Every corrected span in the Findings table was grounded in a record re-read this run (the pointers are in its Evidence column). The events file was rewritten only through the builder, so the 96 quote asserts held after every edit.

**5. Blind reviewer.** An independent agent read only the prompt, the events, the SQL and the eval rules. It verified values through hg.py and persona_view, with Working_Files/, the baselines and the rubric closed to it. It reported:
- no INACCURATE value;
- one INCOMPLETE locator (X1);
- four MINOR items (X9–X12).
All are fixed above. Every other value it re-derived matched: all quotes, times, authors, recipients, the Snowflake sums, the 7 / 3 / 28 split, the owners and the totals.

**6. Record.**
- **Prediction:** Completeness 5 (no INCOMPLETE item remains, and no non-action or final-response event); Accuracy 5 (no INACCURATE, MINOR or format item remains); /oe PASS 5; Path feasibility SUPPORTED; Task solvability SUPPORTED_BY_OE.
- **Residual risk (not a finding):** /oe may still judge a search term unnatural. Every term now comes from the prompt or an earlier event.
- **File:** 08_Oracle_Events.md sha256 @@OESHA@@, 104 events, @@OECHARS@@ characters. Type it into the platform exactly as written.
- **Unresolved: none.**

# Fork sweep (cold, blind) — Leonard Hayes holder close-out, rev2

Status: COMPLETE. Clock 2026-02-14 00:00 UTC, normal universe. I read only Leonard-reachable records:
his mailbox (`threads/leonard@harmonygames.co_*`), Slack channels/DMs he is in, his Drive/Docs (plus shared-drive
docs shared to him), Linear, and the SQL overlay. No answer key was opened.

Slack IDs: EMPLOYEE_0038 = Leonard, EMPLOYEE_0016 = Robert, EMPLOYEE_0025 = Arthur Blake (users.json).

## 1. Independent solve

### Deciding records (short cites)
- **Rules**: SQL gdocs `f_a37b...` "Stockholder close-out notes" (Feb 13). It replaces "Holder outreach notes" (Feb 10). Linear project "Holder records" description gives the states. The SQL #winddown thread under Leonard's Feb 12 22:17 list ("next things for me are …") adds the family/Covered rule and "the sheet goes to you [Arthur] as well as Robert, the rest of my notes stands".
- **Carta lines** (Leonard's mailbox, "Termination details for …", Carta sender): ES-1 [0043] vested 17,802, term Dec 31 2025, LDE Mar 31 2026; ES-2 [0100] LDE Nov 1 2024; ES-3 Calvin 4,408, LDE Jan 24 2026, **extended to Feb 20 2026** (SQL: Calvin's Feb 3 forward of a Carta update); ES-4 Claire 4,450, term Dec 31, LDE Mar 31; ES-5 [0612] 5,298, LDE Jan 24 2026; ES-6 Victor 12,716, LDE Jul 16 2025; ES-7 Marcus 22,889 granted, 12,875 vested, term Jan 30 2026, LDE Apr 30; ES-12 [0068] 16,277/8,477, term Jan 30, LDE Apr 30; ES-13 Martin 3,866/2,013, Apr 30; ES-14 [0051] 3,866/1,530, term Nov 21 2025, LDE Feb 21 2026; ES-15 (Brian Foster; "Ömer [0093]") 10,173/3,391, term Dec 31, LDE Mar 31; ES-16 [2768] 10,384, LDE Jan 24 2026; ES-17 [0038] 34,439, LDE Jan 28 2026; ES-18 [0022] (Oliver Brooks, per the Board Consent Q4 2024 exhibit) 15,259/5,404, term Jan 30, LDE Apr 30. Exercised 0 on every line.
- **Ledger totals**: gdocs /docs_documents/40 (Leonard-owned "Reset Financing Term Sheet", Jan 22 2026). "Inputs from ledger: Founder common 6,000,000; Series Seed Preferred 3,051,879; Options outstanding 268,772". The 2023 closing email (thread 1773160052067710033) says "(3,051,882 vs 3,051,879)". SQL #executives reply: "chatgpt has the other seed investors a couple of shares off … go by the ledger" (ChatGPT used 3,051,881).
- **Griffin split**: #executives Jan 14 2026: "2,662,255 Seed shares and the Side Fund has 84,438, total 2,746,693".
- **Advisor options** (gdocs advisor agreements, Jul 21 2023): Collins 61,038 (doc 490); [0127]/PERSON_3941 6,104 (doc 160); PERSON_1287 6,104 (doc 295); Segerstråle ([0089][25152]) 30,518 (doc 570). Carta digest Nov 17 2023 shows ES-9 for Collins and ES-11 for PERSON_3941. Seed and options are lumped together on the Nov 2024 list (Linear "Nov 2024 owner list" comments). Subtracting gives 25,432 Seed for Collins, PERSON_3941 and PERSON_1287, and 50,865 Seed for [0089]. Check: non-Griffin Seed comes to 305,186 (= 3,051,879 − 2,746,693), and options at Jan 22 come to 268,772. Both match exactly.
- **Told evidence**:
  - Griffin: Leonard's Feb 9 "Combo Fighter Data and … Shut-Down" sent To PERSON_4337 (partner); the partner replied Feb 11.
  - Feb 11 contractor letters ("The company is shutting down") went to PERSON_2361 [0043], PERSON_2360 Claire, marcus.bennett, PERSON_4363 Martin, PERSON_4243 Brian and PERSON_3140 [0068]. **[0068]'s letter bounced** (SQL DSN: "account … disabled").
  - Robert's Feb 12 "we're closing the company" went To PERSON_3941 (SQL).
  - Leonard's Feb 12 "Harmony" went To "Akin <PERSON_8862_EMAIL>" (SQL). Collins signs "akin" (May 2025 board email).
  - Slack DM D04UC0UEN2V, Feb 9: Leonard told PERSON_3335 "shut down the company we decided" (see Fork 1).
- **Family**: thread 1774211155651873582 says "all three Disli brothers" and "You and your brothers". Thread 1770141224265557526: PERSON_2260 ([52949]) sent the details for Patrick Lewis, [52949] and [27652]. So [52949] is the handler, and Patrick and [27652] are Covered.
- **Directors**: SQL Robert reply on "Board position": "That leaves Leonard and me on the board". Collins left in May 2025 (thread 1830959847543474636). The Griffin partner resigned Feb 12.

### Per-issue table (my reading: email/letter "told"; Collins told)
| Issue | Holder | Instrument | Shares now | Options now | Last day | Told | Sheet | Linear | Note |
|---|---|---|---|---|---|---|---|---|---|
| 2438 | Griffin II | Series Seed | 2,662,255 | – | – | Yes | Already told | Done + why | none (heads-up separate) |
| 2439 | Griffin Side Fund | Series Seed | 84,438 | – | – | Yes | Already told | Done + why | none |
| 2440 | [0089][25152] | Seed + adv. opt | 50,865 | 30,518 | – | No* | Closing | Todo | closing + holdings |
| 2441 | Arthur P3083 | Seed | 25,432 | – | – | No | Closing | Todo | yes |
| 2442 | [4468] | Seed | 25,432 | – | – | No | Closing | Todo | yes |
| 2443 | [52949] (handler) | Seed | 25,432 | – | – | No | Closing | Todo | yes, lists Patrick and [27652] at 25,432 each |
| 2444 | Patrick Lewis | Seed | 25,432 | – | – | No | Covered | Done + why | none |
| 2445 | [27652] | Seed | 25,432 | – | – | No | Covered | Done + why | none |
| 2446 | PERSON_3941 [0127] | Seed + ES-11 | 25,432 | 6,104 | – | Yes | Already told | Done + why | none |
| 2447 | Husnu Matthew Collins | Seed + ES-9 | 25,432 | 61,038 | – | Yes* | Already told | Done + why | none |
| 2448 | TOR Capital | Seed | 50,865 | – | – | No | Closing | Todo | yes |
| 2449 | PERSON_1287 | Seed + adv. opt | 25,432 | 6,104 | – | No | Closing | Todo | yes |
| 2450 | [0043] | ES-1 | – | 17,802 | Mar 31 2026 | Yes | Last day | Todo | yes |
| 2451 | [0100] | ES-2 lapsed | – | 0 | passed | – | Nothing | Canceled + why | none |
| 2452 | Calvin Price | ES-3 | – | 4,408 | **Feb 20 2026** | No | Closing and last day | Todo | yes, **goes first** |
| 2453 | Claire Morgan | ES-4 | – | 4,450 | Mar 31 | Yes | Last day | Todo | yes |
| 2454 | [0612] | ES-5 lapsed | – | 0 | passed | – | Nothing | Canceled | none |
| 2455 | Victor | ES-6 lapsed | – | 0 | passed | – | Nothing | Canceled | none |
| 2456 | Marcus Bennett | ES-7 | – | 12,875 | Apr 30 | Yes | Last day | Todo | yes |
| 2457 | [0068] | ES-12 | – | 8,477 | Apr 30 | No (bounce) | Closing and last day | Todo | yes, to the disabled issue address |
| 2458 | Martin Walsh | ES-13 | – | 2,013 | Apr 30 | Yes | Last day | Todo | yes |
| 2459 | [0051] | ES-14 | – | 1,530 | Feb 21 2026 | No | Closing and last day | Todo | yes |
| 2460 | Brian Foster | ES-15 | – | 3,391 | Mar 31 | Yes | Last day | Todo | yes |
| 2461 | [2768] | ES-16 lapsed | – | 0 | passed | – | Nothing | Canceled | none |
| 2462 | [0038] | ES-17 lapsed | – | 0 | passed | – | Nothing | Canceled | none |
| 2463 | [0022] Oliver Brooks | ES-18 | – | 5,404 | Apr 30 | No | Closing and last day | Todo | yes |
*See Forks 1 and 2.

**Counts (rows)**: Nothing 5, Already told 4, Covered 2, Closing 6, Last day 5, Closing and last day 4 (total 26). That gives 15 notes, and Linear Todo 15 / Done 6 / Canceled 5. 11 issues need a "why" comment.

### Key figures
- Common 6,000,000 (2,000,000 each for Leonard, Robert and Arthur). Series Seed 3,051,879. Shares outstanding 9,051,879.
- Options outstanding today (live and vested): **164,114**. Shares plus options today: 9,215,993.
- Options at Dec 31 2025 (lines terminated on or before Dec 31 count vested only; Jan 30 terminations count the full grant): **243,757**.
  - Lines: ES-1 17,802; ES-3 4,408; ES-4 4,450; ES-5 5,298; ES-7 22,889; advisors 30,518 + 61,038 + 6,104 + 6,104; ES-12 16,277; ES-13 3,866; ES-14 1,530; ES-15 3,391; ES-16 10,384; ES-17 34,439; ES-18 15,259.
  - Cross-check: 268,772 − 12,717 − 3,180 − 6,782 − 2,336 = 243,757.
- KPMG shares plus options: **9,295,636**.
- Griffin share of the preferred: 2,746,693 / 3,051,879 = **90.0%**.
- Directors: **Leonard and Robert**. Griffin holds the preferred vote.
- Who goes first: **Calvin Price (Feb 20)**, then [0051] (Feb 21).

### Deliverables
- **Griffin heads-up** (send, after the sheet): reply-all on PERSON_4337's own Feb 12 "Board position" mail (To PERSON_4337, Cc PERSON_2847). It asks for Griffin's vote, as preferred holders (2,662,255 + 84,438, about 90% of the Series Seed), on the dissolution.
- **KPMG** (send, after the sheet): reply-all on the Feb 13 thread (To PERSON_3088; Cc PERSON_4416, PERSON_2322, PERSON_2847). Content: (1) by class: common 6,000,000; Series Seed 3,051,879, with Fund II 2,662,255 and Side Fund 84,438. (2) The Dec 31 option lines and the 243,757 total. (3) 9,295,636. (4) No new financing; the company is winding down (Sunset engaged, dissolution pending).
- **#winddown**: reply in the thread under Leonard's Feb 12 22:17 list. It says the sheet is ready and Calvin goes first.
- **Sheet and letter**: in the "Stockholder close-out" folder (d_6010…, not Wind Down). Share the sheet with Robert and Arthur, and the letter with Robert. Do not send to Sunset ("I'll pass it to Sunset myself").
- **Letter**: worked up from the Feb 9 #winddown draft, using the "February 26 Update" outline sections. Holder figures come from Carta, not the Nov 2024 list.
- **Notes**: Gmail drafts to each issue's email.

## 2. Fork list
1. **FAIL: [0089][25152] told via Slack DM.** On Feb 9 (D04UC0UEN2V) Leonard wrote to PERSON_3335: "Metrics didn't improve … shut down the company we decided". At 19:26 #winddown says "pinged [PERSON_NAME_6550] to get guidance on how to wind down". In the Jan 8 intro mail Leonard writes "Thank you [PERSON_NAME_6550]" to PERSON_3336, which is ENG-2440's email. The DM is a "written message … sent to them directly and delivered". This could flip the row to Already told (Done, no note), and the counts to 5/5 and 14 notes. But the Slack profile is null, the identity chain runs only through tokens, and NB-31 covers DM member lists. The Linear "Last mail…" comment points only to email. *Settle:* a Linear comment on ENG-2440 or a notes line stating whether that DM counts, or a Slack profile email linking PERSON_3335 to PERSON_3336_EMAIL.
2. **FAIL: Collins told via "Akin <PERSON_8862_EMAIL>".** That address appears nowhere else in Leonard-reachable data; only the nickname "akin" links it to Collins. Reading it as not told gives Closing, Todo and a 16th note. *Settle:* a contact record or a prior mail from PERSON_8862_EMAIL signed Matthew Collins/Akin.
3. **FAIL: advisor instrument split and line identity.** No Carta record gives ES-8/ES-10 (holder or size) or the sizes of ES-9/ES-11. The split relies on July 2023 draft advisor agreements: three of the four sit in a shared drive with shared_with [], so reachability is uncertain. The agreement says "[stock purchase agreement][option]". A solver can defensibly book 86,470 / 31,536 / 31,536 / 81,383 as shares. That changes per-holder "shares/options now", every note's holdings, and KPMG item 2's lines. The totals are still settled by the term sheet. *Settle:* Carta "Equity awards" records (or a ledger export) for ES-8 to ES-11.
4. Minor: advisor options vested now. Vesting start (Jul 21 vs Nov 10 2023) and whether Collins's May 2025 board exit ended service are open. Either way they are fully vested, unless a solver applies forfeiture.
5. Minor: Seed total 3,051,879 vs 3,051,881 vs 3,051,882. "The ledger" is named only inside a ChatGPT-generated doc, and "these" has no clear referent. Corroborated by the 2023 closing email and the per-holder sum.
6. Minor: whether termination letters count as "told". They say "company is shutting down"; reading them otherwise flips 5 rows from Last day to Closing and last day.
7. Minor: Calvin's last day. The extension arrives as the holder's forward of a Carta mail, while the earlier Carta notice says Jan 24 (lapsed, so Canceled). This decides who goes first.
8. Minor: the [0068] note goes to a disabled address, because the rule says to use the issue email.
9. Minor: heads-up recipients (PERSON_4337 + PERSON_2847, or also Robert/Arthur). Also whether the heads-up is sent or held as a draft: Griffin is a holder, and "only the holder messages wait for me".
10. Minor: new sheet vs editing "Holder list (draft)".
11. Minor: KPMG item 4 scope (data-licence sale, director resignation).
12. Minor: token collisions. "Arthur PERSON_3083_NAME" shares Arthur Blake's signature token, which risks the "three of us" exclusion. patrick@ mail is signed "[PERSON_NAME_4468]" (ENG-2442's name).
13. SILENCE: I found no unanswered holder question about a holding in reachable records. If the key expects one, it is unsupported.

## 3. Staged hints / riddles / traps / false premises
- **Planted index**: all 26 Linear issues carry "Last mail with that address before Feb: <date>" and "Nov 2024 owner list: N". The "before Feb" phrasing is contrived and reads like a riddle pointer; it also steers away from the Feb letters and the DM. The Nov 2024 figures are a decoy that lumps options with shares.
- **Staged hint**: the #executives reply "chatgpt has the other seed investors a couple of shares off in these, go by the ledger" (vague referent). The draft sheet note "percentages leave out the option pool … about 94%" is also a hint.
- **Planted traps**:
  - Slides outline "Holders, per the Nov 2024 owner list" contradicts "Carta is the record".
  - Collins's alternate-address "told" mail.
  - Calvin's "extra weeks I asked for".
  - The [0068] bounce.
  - Sunset's sheet request, against "I'll pass it to Sunset myself".
- **Staged answers**: Robert's "Leonard and me on the board" and the contact "left the board May 2025" hand over the directors answer. The SQL injected that contact update, but the base record still reads "Independent Director".
- **No false premise found**: KPMG's mail is Feb 13, which is "yesterday". The #winddown draft (Feb 9), the close-out folder and the notes all exist. The injected Slack posts (Feb 13 02:21 UTC) fall before the NB-6 cutoff.

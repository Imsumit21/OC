# Census (c): alias-gated deciding fact

Status: COMPLETE (scout, read-only; no SQL executed, nothing written outside this file)
Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
Verdict: **GO (conditional)**. Holder ENG-2447 (SSP-10, "Husnu Matthew Collins"), alias **"Akin"**. Carrier: one new Feb 10 email in Leonard's mailbox to "Akin" at a personal address. Cold landing estimate about 30% (range 20 to 40%).

## 1. Question and rule (Hardness v2 3.6)

- 3.6 asks for a real alias or a person-to-company link. The mapping has to live in contacts or an earlier conversation, with no spelling tricks. Part 5.4: every alias has to map back through records the persona can see. Part 5.2: name the convincing wrong source and the record that beats it.
- The rule it has to work through is the notes doc `f_a37b403d5200d4f0a31d31`: "Told means a written message about the closing, sent to them directly, from one of the three of us; for a fund, its partner." "The three of us" means Leonard, Robert and Arthur Blake (#winddown 1770938131.882339). The rule does not say which address a message must go to. The line "Messages go to the email on each holder's issue" covers only our outgoing notes.
- In the current design, each Linear issue's `Email:` line is the address that every existing told-message was sent to. That shortcut is why the told traps fell: a run matches the recipient address to the issue and is done.

## 2. Natural path of the solved run (rev1p precheck)

Sources: `run_forensics/rev1p/precheck/precheck/calls.jsonl` and `06_PreCheck_Trajectory/trajectory.json`.

- **Contacts:** called once, `contacts_get_contacts {"limit":250}` (ev 371). It returned all 172 rows. The run printed name, email, job and description for each (ev 373), then wrote: "Directory is heavily anonymized; I'll determine 'told' status from the actual Feb 9–13 messages" (ev 380). So Contacts is on the path but is not trusted. Base Contacts rows have no descriptions, and most are bare `PERSON_NNNN` rows.
- **Told scan:** coverage of founder-sent mail is complete.
  - ev 294: `gmail_list_messages after:2026/02/08` (200 max, includes spam).
  - ev 381: `after:2026/02/08 (from:me OR from:robert@ OR from:arthur.blake@)`, then ev 386 fetched metadata (To, Subject) for the 14 unread messages and ev 394 fetched full bodies for 8.
  - Slack DMs: ev 416 (after Feb 8, im/mpim) and ev 646 (from Leonard).
  - It found Robert's Feb 12 reply to Nebojsa on a revived 2023 thread (ev 313/319), so burying a message in an old thread does not hide it.
- **Collins-specific checks:**
  - ev 559: "[11362] identity/told status".
  - ev 607: `Collins (resign OR board OR options)`.
  - ev 608: Slack search "Collins".
  - ev 648: `after:2026/02/08 (... collins ...)`, which returned 0.
  - ev 724: `from:matthew.collins@ after:2025/06/01`.
  - It never searched "Akin". It did decode the Oct 28, 2025 intro thread 1847258343060233599 (ev 474–479), which carries the header "Re: Akin <> Joe Intro" and Collins's own sign-off "best / akin".
- **Calibration warning:** Segerstrale (ENG-2440) is already alias-gated. His issue email is PERSON_3336, but the Feb 9 told-message went over a Slack DM to PERSON_3335 (his entity is SEMC). The run solved it ("SEMC investor was told Feb 9", ev 530). Adjacent token numbers (3335 and 3336) probably helped.

## 3. 26-holder alias census

The table lists the names and addresses that base data uses for each holder, the told value in truth.json, and whether an alias can gate that holder's deciding fact.

| Issue | Holder (Linear title) / issue email | Other base names and addresses | Real alias in base? | Told (truth) | Gate value |
|---|---|---|---|---|---|
| 2438 | Griffin II / PERSON_4337 (partner) | Partner "Phil" = [1999]; firm [PERSON_NAME_2000]; colleague PERSON_2717 | Fund to partner, but the issue email is already the partner's | Yes | None (shortcut) |
| 2439 | Side Fund / PERSON_4337 | Same as 2438 | Same | Yes | None |
| 2440 | Segerstrale / PERSON_3336 | PERSON_3335 (mail and Slack DM D04UC0UEN2V); "Kris"; [6550], [0090]; SEMC | Yes, and already used | Yes | Already gated, and it was solved |
| 2441 | Schaeppi "Arthur PERSON_3083_NAME" / PERSON_3063 | PERSON_3083 (Solsten work address); "Joe"; Slack "Joe Schaeppi"; first name collides with Arthur Blake (X02) | Yes, but the 3083 token sits in the issue title | No | Weak (token shortcut) |
| 2442 | Bergmann [4468] / PERSON_0693 | "patrick" signature; masking collapses him onto patrick@ (shared with Patrick Lewis and the staff Patrick) | Ambiguous | No | NO-GO (UGT) |
| 2443 | Enes [52949] / PERSON_2260 | Libra CEO, "Enes" | Family head | No | Taken by FAM |
| 2444 | Patrick Lewis / patrick@ | Patrick Haktan Dişli | Masking collapse | Covered | Taken by FAM |
| 2445 | Eren [27652] / PERSON_2275 | "Eren Dişli" (Carta) | Name only | Covered | Taken by FAM |
| 2446 | Nebojsa / PERSON_3941 | [0112], [0127]; PERSON_3935 (mail and Slack); "IKE LOA LLC" (INFERENCE) | Yes | Yes (Robert to PERSON_3941) | Moving the told-message to PERSON_3935 rests on INFERENCE |
| **2447** | **Husnu Matthew Collins / matthew.collins@** | **"Akin" in 55 Leonard-mailbox threads; "best / akin" from Matthew Collins (1847258343060233599); "Akin Babayigit viewed … Board Consent" (DocuSign, for example 1799104494540606747) paired with the consent requests sent to Matthew Collins (1799069283659406996); "Hi PERSON_4337_NAME and Akin" board mail; [11362] on the owner list; Slack #executives "pinged Akin"** | **Yes, strong and multi-record** | **No** | **BEST** |
| 2448 | TOR Capital Limited / PERSON_5275 (principal) | [0128], [0129]; directors PERSON_5137, PERSON_0711; counsel PERSON_5593; "cap table should have TOR Capital Ltd vs my name" | Person to company, but the issue email is the principal's, and there is already a runway-warning decoy (TC_TOR) | No | Second choice, redundant |
| 2449 | Deepak PERSON_1287_NAME / PERSON_1287 | [2950] appears only through uneven masking; "Deepak" raw in Slack | The link is a masking artefact | No | NO-GO (spelling-trick-adjacent) |
| 2450 | ES-1 [0043] / PERSON_2361 | julia.lawson@, jlawson@; her Feb 11 letter greets [0040], the same token as Claire's letter | Address alias | Yes (letter) | NO-GO: the letter's effective date (Dec 31) settles it by elimination |
| 2451, 2452, 2454, 2455, 2461, 2462 | Lapsed lines | ES-16 cameron@ is INFERENCE; ES-17 is "ryan" PERSON_2314 | n/a | n/a (Nothing) | Out of scope |
| 2453 | Claire / PERSON_2360 | GitHub "Claire"; letter greets [0040] | Weak | Yes | Taken by Q1 |
| 2456 | Marcus / work address | Lookalikes Marcus Lee and Oscar Bennett | Lookalike, not an alias | Yes | None |
| 2457 | ES-12 [0068] / PERSON_3140 | "[0068]'s email address is PERSON_3140" (1789011705438137160) | Address alias, but the letter greeting [0068] equals the title token | Yes | None (shortcut) |
| 2458 | Martin / PERSON_4363 | martin.walsh@; lookalike Martin Lewis | Greets "Martin" | Yes | None |
| 2459 | ES-14 Vincent / PERSON_2684 | vincent@ | n/a | No | Taken by LETTER |
| 2460 | Brian / PERSON_4243 | Letter goes to "brian"; "Omer" [2769][0093] | First name only | Yes | None |
| 2463 | ES-18 Oliver / PERSON_1174 | oliver@; lookalike Lauren Brooks | n/a | No | Taken by LETTER |

## 4. Candidates ranked

1. **ENG-2447 Collins as "Akin" (GO).** This is a real nickname that base data uses everywhere in Leonard's own mailbox. The deciding fact flips in the most valuable direction: a stock holder who looks like he still needs a first note was in fact already told.
2. **TOR person-to-company (NO-GO).** The issue email is already the principal's, so the token links it directly. TOR's told status already carries the runway-warning decoy.
3. **ES-1 address swap (NO-GO).** It needs no new rows: change ENG-2450's issue email to julia.lawson@. But the Feb 11 letter's effective date of Dec 31 matches only ES-1 among the three option holders who have no matched letter. A run solves it by elimination, and the swap can also disturb the C_ES14/C_ES18 LETTER trap.

## 5. Chosen design: carrier, natural-path view, slot flips, weights

**Carrier.** One new Gmail thread row and one message row in leonard.hayes@'s mailbox.
- Date: about 2026-02-10 18:40Z, after the Feb 9 decision and before the Feb 13 notes doc.
- From Leonard; To `Akin <PERSON_NNNN_EMAIL>`, a personal address token that does not exist in base. Check it with `lookup` at /injection. No cc.
- Subject: neutral, for example "Harmony".
- Body: the closing, in writing, direct, in Leonard's voice (for example "wanted you to have it from me in writing: we're closing Harmony…"). It must not state holdings, ask questions, or contain the strings "Matthew" or "Collins".
- Optional third row: a Contacts row `first_name 'Akin', job 'Investor', email PERSON_NNNN_EMAIL`, matching the two seeded Investor rows. It grounds the new address. The tie to Collins still comes from old mail.

**Convincing wrong source.** Two records point the wrong way:
- The ENG-2447 comment "Last mail with that address before Feb: Oct 28, 2025". It stays true.
- No mail to matthew.collins@ after Feb 8 (the run's ev 648 returned 0).

The record that beats them is the Feb 10 "Akin" email together with the old-mail mapping.

**What the run sees.** The email surfaces in the ev 381-style founder-sent scan. A run only gets the flip right if it asks "who is Akin?" and follows one Gmail "Akin" search to "best / akin" from Matthew Collins, or to the board-consent and DocuSign pairings.

**Truth changes for ENG-2447:** Told No → Yes; Owed First note → Already told; State Todo → Done.

**Rows a run fails if it misses the email** (surface total is 234):

| Slot | Change | Weight |
|---|---|---|
| C_COL (new) | ENG-2447 Owed = Already told | 5 |
| TC_COL (new) | Told = Yes | 3 |
| C_FIRST | "first notes total" moves from six to five; re-key the regex | 3 |
| N_COUNT | Note count moves from 14 to 13 | 3 |
| LC_Col (new, optional) | Reason comment on ENG-2447 | 3 |
| NC_Collins | Retire: no note goes to Collins | was 3 |
| LS_vol | ENG-2447 state Done | 1 |

A miss costs 14 to 17 points, about 6 to 7% of the score. K4 and K8 (Collins's stock and options) are unchanged.

## 6. UGT / fairness risks

- **Raw name.** "Akin" is the unmasked name of a real public person ("Akin Babayigit", Tripledot), and base data leaks it widely. The design's own rule says "Keep the raw name out of seeds" (§1c, written for "Jackie Alfenas"), though the SQL already seeds "Husnu". This is the author's call. Mitigation: use the first name only and never the surname.
- **The link rests partly on masking.** Some copies of the same thread show "Akin" in the header and "Matthew Collins" in the body. A cold reviewer could call that a masking artefact. The rebuttal is that 55 Leonard-mailbox threads use "Akin" as the board advisor and investor, and Collins signs "akin". Cite at least three of them in the dossier.
- **Personal address.** The told rule never names an address, so the risk is low. State it in the dossier.
- **Coherence.** Leonard's Feb 12 #winddown list still says "Reaching out to our angels properly". This is consistent: Griffin and SEMC were also told informally on Feb 9.
- **No base contradiction.** No Slack or mail record after Feb 8 mentions Akin or Matthew.

## 7. Dependencies on other new candidates (bounce, Carta lapse)

- **Bounced termination letter.** There is no data dependency, because it touches different holders (option letters). It does share the TOLD mechanism. Keep it off ES-9 and off Collins.
- **Carta notice extending a lapsed line.** This turns a Nothing line live, which adds one note to N_COUNT, while (c) removes one. If both ship, a run that misses both still lands on 14 by luck. Grade per holder and treat N_COUNT as a guard only. It must not touch ES-9 (Collins's advisor options, which have no termination).

## 8. Landing-rate estimate and verdict

| Step | Estimate |
|---|---|
| P(the run reads the email) | about 0.85 |
| P(the run maps "Akin" to ENG-2447, given it read the email) | about 0.75 (Opus resolved [0051] and SEMC in the precheck) |
| P(the trap lands, meaning the run gets it wrong) | about 0.30 (range 0.20 to 0.40) |

Verdict: **GO (conditional)**, provided the author accepts the raw-name point and adds 2 or 3 rows.

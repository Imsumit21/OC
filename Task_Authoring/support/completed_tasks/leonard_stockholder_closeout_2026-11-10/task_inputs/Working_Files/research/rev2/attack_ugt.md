# rev2 cold UGT attack (N1-N4)

Reviewer: cold adversarial UGT pass. Did not read census_*.md, leak_audit.md or generator_map.md.
Base: SQL fd51afbf63aa + rev2_change_spec.md. Searches via `hg.py search` (base data only); SQL read as overlay.
Bar: a fork is open unless a quoted record Leonard can reach rules out the other reading. SILENCE = open.

## Rules as written (notes doc f_a37b403d5200d4f0a31d31; Linear project ec2ea957)
- "Carta is the record, over any date in the letters. If a line's last day has passed, it holds nothing."
- "Told means a written message about the closing, sent to them directly, from one of the three of us; for a fund, its partner."
- "Everyone still holding something gets what they are owed: the closing if they have not been told, their last day if they have one. Whoever's last day comes first goes first."
- "Messages go to the email on each holder's issue."
- Linear: "Canceled where the line holds nothing; otherwise Todo where its own note is waiting for me, and Done where it isn't."

---

## N1 BOUNCE (Owen, ES-12, ENG-2457)

Facts checked:
- Letter: Leonard's mailbox, thread 1856860994291529096, Feb 11 2026 12:13:48 -0800, To PERSON_3140_EMAIL (= ENG-2457 issue email), cc Robert, Arthur; body "The company is shutting down". Copies also in Robert's (00016874) and Arthur's (blake@...1856861205341126331) mailboxes; a DSN would only be in Leonard's copy (fine).
- Owen's Carta: "Termination details for [PERSON_NAME_0068] ... as of Jan. 30, 2026 ... ID ES-12 ... Granted 16,277 Vested 8,477 ... Last day to exercise April 30, 2026" (thread 1856960504234892536). So Owed = Closing and last day if not told.
- No other direct written closing message to Owen from the three: Leonard-Owen DM D05SDEQEK61 Feb 11 16:35 is only "will you be joining? / I have some announcements to make / if not I can catch up with you in person later"; Arthur-Owen DM D05S1S2AB5M and Robert-Owen DM D05SJRKTUMS (Feb 2026) are work chat only.
- **Owen +1'd Leonard's #team channel post** C05KNDCHAAG ts 1770839984.194409 (Feb 11 19:59Z): "<!here> per our conversation we'll be shutting down the company. I'll archive everyone's Google Account's by Feb 15 ..." reactions `[{"name":"+1","users":["EMPLOYEE_0021_SLACK_ID"]}]` (EMPLOYEE_0021 = Owen Baker, users.json /11). Owen left the channel at 20:41.
- Base DSN precedent: the exact 550 5.2.1 "inactive" text exists in base (victor.barnes@harmonygames.co, 5 standalone DSN threads in Leonard's mailbox, May 2025, e.g. 1832296006757696403). Note: the spec's "every base bounce sits in the original's thread" is not true; many base DSNs are standalone threads (Victor's), some are in-thread (1766170577680361145). Either placement is base-consistent.
- Leonard's own done-source: #winddown "I'll create this for all contractors and will send them to their personal accounts" (1770838364.606739) and "All termination letters are sent" (1770841239.761999).
- Other Feb 11 letters (Martin PERSON_4363, Marcus marcus.bennett@, Brian PERSON_4243, [PERSON_NAME_0043] PERSON_2361): no DSN for any of them; no base DSN for any holder issue address except victor.barnes@ (Victor's line ES-6 lapsed Jul 16 2025, so Victor gets no draft).

Second readings and verdict:
| Decision | Reading A (truth) | Reading B | Ruled out by a reachable record? |
|---|---|---|---|
| Told, wording "sent to them directly" | bounced, not told | the letter was sent directly, so told (literal text) | NO. The rule says "sent"; Leonard's own "All termination letters are sent" agrees. The truth is the non-literal reading. **OPEN (fail-level)** |
| Told, wording "that reached them directly" | bounced, not told | the Feb 11 @here "we'll be shutting down the company" from Leonard reached Owen (his +1 proves receipt) and reached him directly (Leonard's own words, no intermediary), so told | NO. "reached them directly" loses the one-to-one sense that "sent to them" carried. **OPEN (fail-level)** |
| Draft To | issue email PERSON_3140_EMAIL | owen.baker@harmonygames.co (Slack profile) or "flag, don't draft" | Notes say "Messages go to the email on each holder's issue"; no record gives a working alternative (company Google accounts are archived after Feb 15). Ungraded per spec, so OPEN (minor). Keep Owen out of any global "To = issue email" row. |
| Draft content | closing as news + last day Apr 30 2026 + 8,477 vested options | also resend the termination-letter content (property return by Feb 15, Carta email) | Not graded; OPEN (minor), don't grade absence/presence of termination content. |
| Counts | Last day 6->5, Closing and last day +1 | | follow from Told; settled once Told is settled |

Wording judgement:
- "sent" leaves the fork, and the literal reading points the wrong way.
- "reached" closes the bounce fork but opens the @here fork, and a reviewer would read "reached" as a pointer at delivery (mild staged hint).
- Minimal fix that leaves no fork: keep "sent to them directly" (which excludes the channel post) and add delivery:
  "Told means a written message about the closing, sent to them directly and delivered, from one of the three of us; for a fund, its partner."
  ("delivered" is ordinary wording. In Gmail it is presumed unless a DSN exists, so it does not create proof-of-receipt forks for the other told holders. Checked: no other told holder has a DSN.) Avoid "received/got" (these invite a demand for proof of receipt on every email-told holder, e.g. Robert's Feb 12 mail to PERSON_3941, which has no reply).
- Hint level of "and delivered": low-moderate; acceptable. Do not add "a bounced mail doesn't count" (a flat pointer).

## N2 EXT (Calvin, ES-3, ENG-2452)

Facts checked:
- Base Carta admin notice (Leonard inbox, 1847333347700620793, 2025-10-29): "terminated ... as of Oct. 24, 2025 ... ID ES-3 ... Granted 8,138 Vested 4,408 ... Last day to exercise Jan. 24, 2026". Only Carta record for ES-3 after 2023 (ES-3 census complete). No expiry/cancel notice exists. The Nov 2023 digest lists ES-3 "for [PERSON_NAME_0029] [PERSON_NAME_0047]" (pseudonym noise; the 2025 notice names Calvin).
- No base record carries "Feb. 20, 2026"/"February 20, 2026" in Carta context (census complete), and no company record of granting an extension (SILENCE; acceptable, since the forward carries its own authority).
- [EMAIL_0801] is Calvin's address in base (2023 team list "Calvin Price: [EMAIL_0801]"), consistent with the issue email. ENG-2452's "No mail with that address before Feb" stays literally true (forward is Feb 3).
- All other last days: ES-14 (Vincent, [PERSON_NAME_0051]) Feb. 21, 2026; ES-1, ES-4, ES-15 Mar 31; ES-7, ES-12, ES-13, ES-18 Apr 30; lapsed: ES-2, ES-5, ES-6, ES-16, ES-17.

| Decision | Truth | Second reading | Ruled out? |
|---|---|---|---|
| Last day | Feb 20 2026 (live) | Jan 24 2026 per Carta's own Oct 29 notice; the forward is "a letter" or an unverified holder copy, so lapsed (Nothing/Canceled) | YES, if the forward visibly is Carta's notice: its own text "Last day to exercise Feb. 20, 2026 (previously Jan. 24, 2026)" supersedes the Oct 29 figure, is later, and "the letters" in the notes are Leonard's termination letters, not Carta mail. **CLOSED** provided the build keeps the forwarded header block (From: Carta SVC_0077 address, Date Jan 23 2026, Subject) and Carta's footer ("eShares, Inc. DBA Carta, Inc."), and uses Carta's date style "Feb. 20, 2026" / "Jan. 24, 2026" (spec text drops the periods). |
| Told | No | Calvin "knows" (he forwarded something) | Rule needs a message from the three; none. CLOSED. |
| Owed / State | Closing and last day; Todo; one draft | | CLOSED. |
| Who goes first | Calvin (Feb 20) | Vincent (Feb 21) if the forward is rejected | Same dependency as Last day. CLOSED with the above. No other live line earlier than Feb 20. |
| KPMG item 2 | 4,408 at Dec 31 either way | | CLOSED (unchanged). |
| Options now / note content | 4,408 vested; Feb 20 | | CLOSED. Calvin asks nothing, so no Q&A obligation. |

Minor: the 1-day gap (Feb 20 vs Feb 21) is a neat flip; a reviewer may note it, but it is not a fork.

## N3 ALIAS (Husnu Matthew Collins, ENG-2447, matthew.collins@harmonygames.co)

Identity links Leonard can reach (all in his mailbox/workspace):
1. Thread 1847258343060233599 (Oct 28 2025 — the very mail ENG-2447's comment "Last mail with that address before Feb: Oct 28, 2025" points to): from Matthew Collins <matthew.collins@harmonygames.co>, signed "best / akin". (Rendered subject is "Re: Matthew Collins <> PERSON_3083_NAME", not the spec's "Re: Akin <> Joe Intro"; fix the spec reference.)
2. Thread 1767980387254277674 (2023): the same sentence appears in quoted copies as "both [PERSON_NAME_6550] and Akin are happy with 0.5% each vesting over 2 years" and as "both [PERSON_NAME_6550] and Matthew Collins are happy with 0.5% each ..." (also "catch up with Akin and he will top-up the angel allocation with $25K" / "...Matthew Collins and he will top-up..."). Direct equivalence.
3. Slack C04UTBZL6AX 2023-06 "so Akin, 1% - Kris 0.5%, Deepak 0.1%, [PERSON_NAME_0112] 0.1%, total 1.7%" ties to the advisor table "Matthew Collins | Board member | 1% | 61,038 shares".
4. Term sheet "one outside director (initially to Akin Babayigit)" ties to contact db57e559 "Independent Director (investor/advisor ...)" (SQL updates the job to "Investor and advisor (left the board May 2025)").
- "Akin" census (slack, gdocs, gsheets, contacts, linear, gcal): every mention resolves to one person (Akin Babayigit: Tripledot, investor, advisor, director nominee). No second Akin, no Akin contact today.

| Decision | Truth | Second reading | Ruled out? |
|---|---|---|---|
| Akin = Collins | yes | Akin is a different person (separate investor or Griffin observer per an early term-sheet draft) | Links 1-2 rule it out. **CLOSED** |
| Feb 10 mail to a never-seen personal address is to him | yes | unknown address, can't be sure it's him | Name "Akin" plus the identity links; no other Akin. CLOSED (minor risk). Cheap hardening: one Akin-specific line in the body that names neither Matthew nor Collins (e.g. "you were there from the seed round and on the board with us"). |
| Told | Yes (Feb 10, direct, from Leonard) | Leonard's Feb 12 #winddown list ("Reaching out to our angels properly") and the notes ("the angels are what's open") imply angels incl. Collins are untold | The rule defines Told by the message; rev1 already has the same pattern (Robert's Feb 12 mail to PERSON_3941). CLOSED (minor). The mail must carry the SENT label (not a draft). |
| Owed | Already told (no last day) | Collins left the board May 2025, so ES-9 ended and has a last day | No Carta termination for ES-9 (Carta census: none); contact says still "advisor". "Carta is the record" means no last day. CLOSED. |
| State / note | Done, no note, comment why | | CLOSED. |
- Optional Contacts row "Akin / Investor": skip it. A second contact with a different job reads as a second person and adds nothing the mail links don't already settle.

## N4 ADV un-pointed

Series Seed total candidates found in reach: 3,051,881 (ChatGPT, #executives 1768416262.426129 / 1768417784.194359), **3,051,882** (disclosure schedule in gdocs, a candidate the spec doesn't list), 3,155,643 (owner-list seed entries incl. advisor options), 3,051,879.
Settling records (no numbers needed from the deleted note):
- Term sheet gdocs docs_documents/40 "Inputs from ledger (pre-recap) / Founder common: 6,000,000 / Series Seed Preferred (all non-founder investors): 3,051,879 / Options outstanding: 268,772". It is the only "ledger" with share counts (census of "ledger" in gdocs, gsheets, Slack).
- Leonard, Aug 10 2023 (thread 1773160052067710033 msg 10): "the number of shares for small investors don't perfectly add up to what we have at disclosure schedule (3,051,882 vs 3,051,879). It looks like a small rounding error". So the per-investor sum is 3,051,879.
- New reply "go by the ledger".
Verdict: total **CLOSED** (3,051,879).
(Census, complete over gmail/slack/gdocs/gsheets/gdrive: 3,051,879 only in the two records above; 3,051,881 / 305,188 only in the ChatGPT posts; 3,155,643 / 3,155,645 / 305,186 / 408,950 / 408,952 / 9,295,636 nowhere in base. No gdrive hits.)

Per-holder split (owner list minus advisor table; stock sums to the ledger's 305,186 non-Griffin):
- Collins 86,470 = 25,432 + 61,038: advisor table names "Matthew Collins" in both copies; Carta digest 1782897835407336831 "option grant ES-9 for Husnu Matthew Collins". CLOSED.
- PERSON_3941 (ENG-2446) 31,536 = 25,432 + 6,104: Gmail table copy (1773160163779741845) names "PERSON_3941_NAME [PERSON_NAME_0127] | Advisor | 0.1% | 6,104"; Carta "ES-11 for PERSON_3941_NAME [PERSON_NAME_0127]". CLOSED.
- PERSON_1287 (ENG-2449) 31,536 = 25,432 + 6,104: Gmail table copy names "PERSON_1287_NAME | Advisor | 0.1% | 6,104" (no Carta grant id). CLOSED.
- ENG-2440 "[PERSON_NAME_0089] [PERSON_NAME_25152]" 81,383 = 50,865 + 30,518: the 0.5% advisor is only "[PERSON_NAME_0090]" (Gmail) / "[PERSON_NAME_6201]" (gdocs). Neither token matches the issue title, and no Carta record names an ES grant for this holder (option-grant census: ES-1, 6, 9, 12, 13, 14, 15, 16, 17, 18 named; not ES-8/ES-10). Settled only by inference: 81,383 - 30,518 = 50,865 (the $50K seed figure TOR also holds); a 2023 mail (1761857065113737556) calls "[PERSON_NAME_0089] [PERSON_NAME_0132]" "advisor/investor'imiz"; and the ledger's 305,186 reconciles only if 30,518 comes out of a person-held seed entry. Competing reading: the 0.5% advisor is [PERSON_NAME_0043] (ES-1, 30,519) or Victor (ES-6, 30,519). Ruled out because those are Carta employee grants with their own notices, and that reading leaves ENG-2440 at 81,383 stock, so seed would be 3,082,397, not 3,051,879. Verdict: **CLOSED (thin; arithmetic-only identity)**. A cold reviewer could still call it OPEN (minor). Cheap settler that does not state the split: a base-style Carta daily digest line "Arthur Blake signed option grant ES-8 for [PERSON_NAME_0089] [PERSON_NAME_25152]" (and ES-10 for PERSON_1287_NAME), dated Nov 2023 like 1782897835407336831.
- Advisor "what's vested": "0.5% each vesting over 2 years with standard advisory shares" (1767980387254277674, 2023). With grants signed Nov 2023 they are fully vested by Feb 2026, and there's no Carta termination for any advisor line. CLOSED (minor: vesting start date never stated, but any 2023 start is fully vested by the clock).

KPMG item 1 after deleting the prior-year sentence:
- Common 6,000,000: the ledger says "Founder common"; certificates CS-01..CS-03 are founders only; every option line shows "Exercised 0"; no RSA issuance found. CLOSED.
- Series Seed 3,051,879: as above. CLOSED.
- Per fund 2,662,255 / 84,438: the only source in Leonard's reach is the ChatGPT post ("from the seed docs"). Griffin's own sign-off mail with the split is only in Robert's (00001194) and Arthur's mailboxes. The new reply says "chatgpt has the seed count a couple of shares off in these", which casts doubt on the only reachable split. The split sums to 2,746,693 = owner list / Linear "both funds on one line", so the 2-share error has to sit in "Other Seed investors 305,188". **OPEN (minor)**. Fix the reply wording: "fyi chatgpt has the other seed investors a couple of shares off in these, go by the ledger" (localizes the error, still numberless).
- Item 3 / A2 9,295,636: unchanged by N4.

Build notes (leaks if missed):
- The KPMG follow-up snippet appears twice: `UPDATE gmail.gmail_threads SET snippet = 'Thank you Leonard. Three clarifications on our side. For item 1, our prior-year file has 6,000,000 common and 3,051,879 Series Seed; if noth'` (SQL line 84) **and** the message row's own snippet (line 86). Both must be rewritten, or the deleted figures survive in search results and thread lists. Also adjust size_estimate.
- Deleting 846a70ba... (Jan 14 note) is clean. The new reply needs parent counters on 1768416262.426129 (base row), i.e. an UPDATE like the one at line 67.

## Cross-effects
- N1 + N3: with "sent ... and delivered", Leonard's Feb 10 Akin mail (no DSN) is delivered. No conflict. With "reached", also fine for Akin, but the @here fork reopens Owen.
- N1 wording vs other told holders: Julia/Claire/Brian (MPDM C51ECE5102ED; Julia, EMPLOYEE_0005, even writes "Mailler ulaştı" = the mails arrived), Martin (DM D05Q3QAH2QZ), Marcus and [PERSON_NAME_0043] (Feb 11 letters, no DSN), PERSON_3941 (Robert Feb 12): none flips under "delivered". Under "reached" a channel-post reading could also be argued for Marcus/Martin (both in C05KNDCHAAG), but they are told anyway.
- Counts: N1 +1 Closing-and-last-day / -1 Last day; N2 +1 Closing-and-last-day and live; N3 -1 note (+1 Already told). Notes 14 -> 15 -> 14 consistent with the spec. The Covered/family rule is untouched.
- Sheet order and #winddown reply: Calvin first (N2). Owen's last day Apr 30 doesn't move the order.
- KPMG reply: item 2 unchanged (Calvin 4,408 either way); item 1 relies on the ledger plus ChatGPT's split (see the N4 minor).
- Draft-address checks: Owen's issue address is dead (by design), and Victor's issue address is dead in base (but Victor gets no draft). Any rubric row "every draft goes to the issue email" must exclude Owen or accept either address.
- State mapping: no change in rule; Owen Todo, Calvin Todo, Collins Done.

## Hint / contrived / false-premise flags
- "reached them directly": reads as a delivery pointer (mild staged hint) and opens a fork; don't use it.
- "and delivered": low hint; acceptable.
- N2 forward: Calvin's one-liner "Thanks for the extra four weeks" plus a CEO with no other trace of granting the extension is slightly contrived but plausible (Carta holder notices go to holders). Not a false premise.
- N3: "Harmony" subject + no holdings is fine; a body with zero context could read as staged. Add one investor/board-specific clause.
- N4 reply: "a couple of shares off" is natural.
- Spec inaccuracies to fix: the subject of 1847258343060233599 is "Re: Matthew Collins <> PERSON_3083_NAME"; the "every base bounce sits in the original's thread" claim is false (harmless); the spec omits the 3,051,882 candidate.
- Prompt (04_Prompt.txt) has no premise broken by N1-N4.

## Summary
- N1: OPEN (fail-level) under both wordings ("sent" = literal told; "reached" = Owen's +1 on Leonard's @here). Fix: "sent to them directly and delivered". Keep Owen's To ungraded.
- N2: CLOSED if the forward keeps Carta's header/footer and date style "Feb. 20, 2026 (previously Jan. 24, 2026)". Calvin goes first.
- N3: CLOSED (links: "best / akin" from matthew.collins@; 1767980387254277674 renders the same sentence with "Akin" and "Matthew Collins"). Skip the contacts row; add one board/seed clause; SENT label.
- N4: Series Seed total and advisor-angels CLOSED (ENG-2440 thin, arithmetic-only; optional Carta digest line for ES-8/ES-10). KPMG per-fund split OPEN (minor): reword the reply to "the other seed investors a couple of shares off". Rewrite both KPMG snippets.

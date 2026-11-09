# Census (b): a later Carta notice that extends one lapsed line's exercise window

Scout: census/design (read-only). Universe: Feb 14 2026 normal, clock 2026-02-14 00:00 UTC. Persona Leonard Hayes.
Base read only through `hg.py search` (search, search-many, get, get-many, files). Overlay read as text from `01_Universe_Inject.sql`. The run read from `run_forensics/rev1p/precheck/precheck/calls.jsonl` and `06_PreCheck_Trajectory/trajectory.json`.
Gmail thread ids are shortened to the number; the files are `threads/leonard@harmonygames.co_<id>.json`.

Status: COMPLETE.

## 0. Verdict summary

**GO, on ES-3 Calvin Price (ENG-2452), with the out-of-the-way carrier (V2).** The obvious Carta-stream carrier (V1) is a weak trap. Its landing rate is only about 20-25%.

- **Line.** ES-3 is the cleanest flip of the six:
  - its window lapsed after Dec 31 (Jan 24, 2026), so KPMG's as-of figures do not move;
  - there is no termination letter, no open question, no NB decoy and no redaction;
  - its name is plain on Carta;
  - no record says the line is gone.
- **V1, the Carta admin stream** (a board consent, its approval and an activity digest from SVC_0077 in Leonard's mailbox). The formats match the base exactly, but the rev1p run would have read it:
  - it fetched every Carta-generated message except login alerts, 59 in all;
  - it decoded them into one chronological dump and read the whole dump.
- **V2, recommended.** Calvin forwards Carta's holder-side "option grant updated" notice to Leonard on Feb 3, 2026, from the address on his issue.
  - Carta's own text sits inside a forward in a new thread, with a subject other than "Termination details".
  - The rev1p run would have missed it. It fetched only Carta-generated Message-IDs from its "carta" result lists, and its date listing started at Feb 8.
  - Estimated landing rate: about 55-60%.
- **Flips.** The line becomes live with 4,408 vested, last day Apr 24, 2026, Told = No, Owed = Full note ("Closing and last day"), Linear Canceled → Todo. It gets a new draft note. Options now go from 159,706 to 164,114, and the note count from 14 to 15.
- **No flip.** KPMG items 2 and 3 (243,757 and 9,295,636) and the #winddown first-goer (Vincent, Feb 21) stay as they are.

## 1. The six lapsed lines

Carta notices were read in full (from SVC_0077, To Leonard only, labels INBOX / Opened (`Label_b19fb8d1b3`) / CATEGORY_UPDATES). The vested count is the number Carta shows at termination.

| ES / issue | Holder (title) | Granted | Vested | Termination effective | Last day | Carta thread, subject, sent (UTC) | At Dec 31 (truth) |
|---|---|---|---|---|---|---|---|
| ES-2 / ENG-2451 | [PERSON_NAME_0100] | 12,208 | 3,052 | Aug 1, 2024 | Nov 1, 2024 | 1808666480668498098, "Termination details for [PERSON_NAME_0100]", 2024-08-28 20:59:28 | 0 |
| ES-3 / ENG-2452 | Calvin Price | 8,138 | 4,408 | Oct 24, 2025 | Jan 24, 2026 | 1847333347700620793, "Termination details for Calvin Price", 2025-10-29 16:12:47 | 4,408 |
| ES-5 / ENG-2454 | [PERSON_NAME_0612] (Douglas) | 10,173 | 5,298 | Oct 24, 2025 | Jan 24, 2026 | 1847333395311994879, "Termination details for [PERSON_NAME_0612]", 2025-10-29 16:13:32 | 5,298 |
| ES-6 / ENG-2455 | Victor [2770] [0086] (Victor Barnes) | 30,519 | 12,716 | Apr 16, 2025 | Jul 16, 2025 | 1830952527208439510, "Termination details for Victor [PERSON_NAME_2770] [PERSON_NAME_0086]", 2025-05-01 20:46:38 | 0 |
| ES-16 / ENG-2461 | [2768] [0011] (EMPLOYEE_0032) | 35,605 | 10,384 | Oct 24, 2025 | Jan 24, 2026 | 1847333318158821452, "Termination details for [PERSON_NAME_2768] [PERSON_NAME_0011]", 2025-10-29 16:12:19 | 10,384 |
| ES-17 / ENG-2462 | [PERSON_NAME_0038] (Frederick Stone) | 127,162 | 34,439 | Oct 24, 2025 | Jan 28, 2026 | 1847333272519888206, "Termination details for [PERSON_NAME_0038]", 2025-10-29 16:11:35 | 34,439 |

### Letters, DMs and told state

"Told" here means told of the closing in writing, sent directly. The sources are s2 (the option and notice state) and g2 (the holder facts), each re-checked where cited.

- **ES-2.**
  - No letter.
  - The last message on file is Jun 16, 2024: a thread with Robert in #engineering-bots, C050WGU41HR/1718567051.806159.
  - Arthur was asked to reach out (#admin 2024-10 idx 193-195). Arthur later wrote: "I reached out to him and he didn't respond" (2024-11 idx 21).
  - Leonard wrote "in Carta it looks like it's forfeited already" (#admin_foundersonly ts 1730757796.947649, Nov 4, 2024). **An extension would contradict this. Excluded.**
  - Not told.
- **ES-3 Calvin.**
  - No letter. A search for "changing direction" or "post-termination" finds no letter for him.
  - DM D050GG6KZT9: the last message is Oct 16, 2025, about a cancelled 1:1. It does not mention equity.
  - #admin thread ts 1761701823.672399, idx 490-492: "[0029] * 0.16 = $705", and 4,408 × 0.16 = 705.28.
  - Digest 1782897835407336831 says "Arthur Blake signed option grant ES-3 … for [PERSON_NAME_0029] [PERSON_NAME_0047]", so [0029] is Calvin.
  - His Google account was archived in Nov 2025 (#admin 2025-11 idx 47-52).
  - Issue email: [EMAIL_0801]. A header scan of Leonard's whole mailbox finds 0 messages from, to or cc that address; it appears only in the Nov 2023 option-issuance body, 1782034095239486005. The Linear comment "No mail with that address before Feb" is accurate.
  - Not told.
- **ES-5 Douglas.**
  - No letter.
  - Last contact Oct 22, 2025: Robert tags him in #zombie-bugs, C08R27X0EAH/1761099441.660419.
  - **NB-32 decoy:** the ledger pays him to Dec 31 (FIN-000683), which would give a window to Mar 31. Not told.
- **ES-6 Victor.**
  - No letter.
  - Last contact Apr 14, 2025 (#zombie-match3d, C0880U9751A/1744648055.209429).
  - Payroll runs to Oct 2025. Not told.
- **ES-16.**
  - Letter 1847333990408253969 (Oct 29, 2025): termination for breach. It gives a "window of 90 days" with no date.
  - Open exercise exchange: he wrote "it says I cannot exercise online in the app" ([1]); Leonard replied "we can surely figure it out" ([0], Oct 30).
  - Cap-table access request, 1847340974854472487.
  - Not told of the closing.
- **ES-17 Frederick.**
  - Letter 1847335165884050330 (Oct 29) gives 34,409 vested and Jan 22, 2026. Carta gives 34,439 and Jan 28. That gap is already the "Carta over letters" case.
  - His inbound mail of Feb 2, 2026 (1856036107053480877) says "Hope you and the team are doing well!".
  - Leonard's Feb 4 reply, 1856226460086133468, is redacted.
  - Not told, as far as the readable record shows.

### Which line flips cleanest

| Line | Window lapsed after Dec 31? | Blockers | Verdict |
|---|---|---|---|
| ES-2 | No (Nov 2024) | Leonard's own "forfeited already". KPMG would change | NO |
| ES-6 | No (Jul 2025) | A 9-month extension made in 2025 would be odd. KPMG would change (Dec 31 holding 0 → 12,716). The payroll mismatch muddies it | NO |
| ES-5 | Yes | It collides with the NB-32 ledger decoy (pay to Dec 31 → Mar 31). The decoy and the truth would both read "live", which wrecks that existing trap | NO |
| ES-16 | Yes | A breach termination makes a goodwill extension less natural. The open exercise thread brings in the "answer anything they asked" rule (O1), which adds content rows and UGT risk | Second choice |
| ES-17 | Yes | It already carries the letter-vs-Carta trap (P_FRED w3). The redacted Feb 4 reply makes Told undecidable. It is the largest line, and the roster calls him a "co-founder" | NO |
| **ES-3** | **Yes (Jan 24, 2026)** | None: no letter, no question, no decoy, no redaction, a plain name on Carta | **CHOSEN** |

### KPMG interaction for ES-3: none

- **Item 2 effective-date wording** ("using each effective date as Carta shows it, regardless of when recorded"). This governs termination effective dates. ES-3's stays Oct 24, 2025, and the extension is dated Jan 22-23, 2026, after the as-of date.
- **Follow-up vested-only rule** ("a line terminated on or before the as-of date counts only what had vested by its termination date"). ES-3 counts 4,408 at Dec 31 with or without the extension. The original window was still open on Dec 31.
- A1 (243,757) and A2 (9,295,636) do not change. Truth already has ENG-2452 "Options at Dec 31": 4408.
- **Guard.** The carrier must restate "Termination date Oct. 24, 2025", so no solver reads the extension as a new termination.

## 2. Base Carta mail formats and approval realism

### Sender census (Leonard's mailbox, scan_complete)

| Sender | Messages | Subjects |
|---|---|---|
| SVC_0077 (notifications) | 75 | "Termination details for <name>" ×14; "Carta activity for <Mon>. <D>, <YYYY>" ×26 (the last is Dec 24, 2024: **no digests at all in 2025-2026**); "<ORG> sent you a Board Consent" ×2 and "[Action required] <ORG> sent you a board consent to sign" ×1; "Board consent approved for <ORG>" ×3; "Carta Alert: Login attempt …" ×15; "You have a certificate to sign" ×3; "<ORG> received 1 new information request …" ×3; "<name> requests access to your cap table" ×1; 409A, onboarding and contract mails |
| SVC_0493 | 13 | 409A review, board approval, "board has approved your valuation" |
| SVC_5822 | 5 | 409A request and expiry |
| SVC_4490 | 5 | Renewal and payment |
| SVC_5909 | 4 | Activation, "12 securities to sign" |
| PERSON_3928, PERSON_2898 | 14, 2 | Carta staff: onboarding thread, 409A follow-up |

- **Not in the base:** any "modified", "amended", "updated" or "extended" option notice; any exercise notice ("Exercised 0" everywhere); any holder-side Carta notice in any mailbox (s2: none of the holder mailboxes on the export holds an SVC_0077 termination mail).
- **Body shapes.**
  - Termination: "= X has been terminated. = / X has been terminated by [SOURCE_ORG_0001] Games Inc. as of <date>. Current holdings and overview of the changes summarized below: / Equity awards ID ES-n Acceptance status Accepted Granted … Vested … Exercised 0 Grant date … Last day to exercise …", then the standard footer.
  - Consent request: "A new Board Consent from … has been sent to you for review and signature. / Additional message from [SOURCE_ORG_0001] Games Inc. <free text, e.g. 'Best, Leonard'> / Company … Consent name <name> - MM/DD/YYYY / Review Board Consent <link>".
  - Consent approval: "= A board consent was approved for … = / All required signatories have approved the following board consent: / Company … Consent name … Approval date <ISO>". To: PERSON_4337_EMAIL, leonard, robert (2025-07-21).
  - Digest: "Activity for … <actor> signed option grant ES-3 <https://app.Carta.com/options/list/3048065/?open=18258522> for [0029] [0047]" (1782897835407336831). No field values ever appear in a digest line.
- **Robert's mailbox** holds copies of both consents: 00006398/00006425 (2024) and 00014657/00014725 (2025).

### Is an extension notice realistic in Carta's own voice?

Yes. Carta supports modifying the post-termination exercise period, and holders are notified when a grant changes. There is no exact base template, so the closest model is the termination notice's "Equity awards" block, which V2 reuses with "Last day to exercise" changed and the old date shown.

### Who would approve it, and when

- **Who.** The board, or the plan administrator. Board consents in the base go to the directors. In Jan 2026 those were Leonard, Robert and Griffin's PERSON_4337, who resigned Feb 12 (1856958794180374704). Collins left May 2025.
- **When.** It must be on or before Jan 23, 2026. After Jan 24 the option has expired and cannot be extended. In Feb 2026 an extension would be unnatural (the company was closing) and legally impossible.
- **Natural anchors in the base:**
  - the Jan 14, 2026 Board Meeting (GCal /events/6127, Leonard organiser, Robert, Arthur, Frederick);
  - Leonard's Carta login on Jan 22, 2026 at 3:26 PM PST (alert 1855061354643750087).
- **Is it plausible in Jan 2026?** Yes. The company was still operating and fundraising (#executives 2026-01 idx 623 and later), and the options were underwater ($0.16 strike against the Jul 2025 409A of $0.10, consent 1837647301438738144). That makes an extension a free courtesy.
- **No base record of such a decision.** The carrier must supply it (V1) or imply it (V2: "thanks for sorting out the extra time").
- **Contradiction scan:**
  - Slack Oct 2025-Feb 2026 for lapsed, expired, forfeit, extend, window, exercis, Calvin and [0029]: no statement that ES-3 is gone. The only "forfeited" is ES-2, in 2024.
  - #winddown "Carta terminations are done" (idx 198) refers to the 8 Feb 12 entries.
  - Linear ENG-2452 comments are neutral.
  - The close-out doc rule ("If a line's last day has passed, it holds nothing") is consistent with an extended last day.
  - The draft holder sheet f_5ecaa967db3adcfa440b09 and the slides do not mention ES-3.

## 3. Run path (rev1p pre-check): Carta searches and reads

| Event | Call | What came back | What it meant for a new Carta record |
|---|---|---|---|
| 45 | gdrive_search fullText "Carta" (50) | 6,406 chars | Only reaches a Drive carrier |
| 69 → 72 | gmail_search "carta", max 100 | 100 ids, 72 threads, newest first, **ids only, no snippets** | A Jan 22-24 or Feb 3 message ranks near the top |
| 78 | get_messages_batch | the 8 Feb 12 terminations | — |
| 124 → 125 | gmail_search "from:SVC_0077_EMAIL", max 500 | all 75 | **Any new SVC_0077 mail is listed** |
| 127 | metadata batch (Subject, Date) | 38 | The model sees subjects |
| 206 / 213 | model text: "pull all 75 Carta notification emails in full and decode them locally" | | |
| 207 → 208 | gmail_search "carta -from:SVC_0077_EMAIL -from:me", max 500 | 192 messages, 82 threads | Only 19 of the 192 were fetched: those whose Message-ID is Carta-generated (`notifications-worker`, `@carta.com`). Positions 0-23, which include gmail.com forwards and outlook mail, were **not fetched** except one SVC_0077 copy |
| 216-236 | 9 full batches (216 failed; 221 retried) | 78 unique messages | Every SVC_0077 message was fetched **except the 15 login alerts and "Your 409A expires in 30 days"** |
| 238 | Bash: decode everything into /tmp/carta.txt, sorted by date | 73,849 chars, 78 entries | A Jan 2026 SVC_0077 mail would land between the Oct 29, 2025 block (lines ~991-1023) and the Feb 12 block (~1034) |
| 240 / 244 / 249 | sed 1-400, 436-740, 740-1110 | the whole dump | **Read in full, digests and consents included** |
| 268 | grep for headers other than activity, termination, login, onboarding, consent or 409A | | A skim pass that drops consents and digests (they were already read in 249) |
| 133 → 135 | slack_search "carta" (50) | newest first, included replies | Any Slack correction containing "Carta" would be returned |
| 294 / 381 | list after:2026/02/08 | | A Feb 3 mail is outside this listing |
| 921-931 | linear comments "Per Carta, option ES-3 (4,408 vested of 8,138) had its last day on Jan 24, 2026, and it has lapsed" | | The run keyed lines by ES id |

**V1 (a new SVC_0077 mail with a subject other than "Termination details")** would have come back in events 69, 124 and 127, been fetched in 216-236, and been read in 249. That is plain view. Where the same sender stream sits next to Calvin's termination in a single dump, the "Same-place check" in v2 Part 7 fails.

- P(read) is about 0.95 for this run class and about 0.6 for a run that filters by subject.
- P(applies, given read) is about 0.8. The consent text names ES-3 and Apr 24.
- **Landing rate (the run misses it): about 20-25%.**

**V2 (a forward from Calvin's address, Feb 3)** would be returned by events 69 and 207, but only as an id. The run did not fetch non-Carta Message-IDs, and its date listings began at Feb 8. **The rev1p run would have missed it.**

## 4. Exact flips and gradable-surface slots

### Truth changes (ENG-2452 and SUMMARY)

| Field | Now | After |
|---|---|---|
| Owed (label) | Nothing | **Full note ("Closing and last day")** |
| Told | null | **No** (no direct written closing message; DM ends Oct 16, 2025; no letter; the #company-internal `<!here>` is not "sent to them directly") |
| Last day | null | **2026-04-24** (Jan 24 + 90 days = Apr 24 = three calendar months, so both readings agree) |
| Options now | 0 | **4,408** |
| Options at Dec 31 | 4,408 | 4,408 (unchanged) |
| Linear state | Canceled | **Todo** (its own note waits for Leonard) |
| Reason comment | required ("lapsed") | **not required** (it has a note) |
| New draft | — | **To [EMAIL_0801]: closing + 4,408 vested under ES-3 + last day Apr 24, 2026** |
| SUMMARY options now | 159,706 | **164,114** |
| Notes (drafts) | 14 | **15** |
| Labels count | Full 2, Nothing 6 | **Full 3, Nothing 5** (Sunset's "count of holders by what each still needs") |
| KPMG item 2 / 3 | 243,757 / 9,295,636 | unchanged (Calvin stays in item 2 at 4,408) |
| Note order / #winddown first-goer | Vincent Feb 21 first | unchanged. Calvin slots between the Mar 31 group and the Apr 30 group |

### Gradable surface (`01_Gradable_Surface.json`, total weight 234, 96 slots)

| Slot | Weight | Effect |
|---|---|---|
| P1 "live options at the clock" | 5 | **Flips**: regex 159,?706 → 164,?114. It is also ADV-gated, so it now depends on two traps |
| P_lapsed_ES3 "ES3 holds nothing" (ENG-2452 Owed) | 1 | **Flips** to Full note. Retitle "ES-3 owed a full note". Recommend w5 core, mechanism CARTA_EXT, as the trap row |
| LC_ES-3 "reason comment on ES-3's issue" (`ENG-2452\|lapsed`) | 1 | **Inverts.** A "lapsed" comment becomes wrong. Remove it, and move the sample to ENG-2461 (ES-16) so the row count stays the same |
| LS_ES-3 "state of ES-3's issue" | 1 | **Flips** to Todo. Recommend w3 |
| N_COUNT "bare count of notes" | 3 | **Flips** to 15 |
| LC_vol / LS_vol | 1 / 1 | Membership changes: 12 → 11 issues need a reason; Canceled 6 → 5 |
| C_DATE (6), C_FIRST (6), D6 (Vincent), A1, A2, AL_*, K16, P_lapsed_ES2/5/6/16, P_FRED | — | Unchanged |
| New, net zero (swap for LC_ES-3) | suggest 5 | N_Calvin: `(Calvin\|ENG-2452)[…]{0,160}(Apr[a-z]*\.? ?24\|2026-04-24\|4/24)`. Optional field rows: ENG-2452 Last day, Told |

- **Exposure per miss at current weights:** 5 + 1 + 1 + 1 + 3 = 11 (4.7%).
- **With the recommended reweights** (P_ES3 w5, LS w3, N_Calvin w5 in place of LC_ES-3): about 21 of about 245 (8.6%).
- **No new holders or rows.** One existing line flips, and one draft is added, within the requester's limit.

## 5. Drafted carrier and landing estimate

### V2 (recommended): Calvin forwards Carta's holder notice, in a new thread

Placed after Feb 1, so Leonard's Feb 12 comment "No mail with that address before Feb" stays literally true. Placed before the Feb 9-11 closing, so it says nothing about the closing.

```
gmail.gmail_threads
  id          'leonard.hayes@harmonygames.co/1856121753043675905'   -- (ms 1770135644000 << 20) + 731905; no collision (files check)
  user_email  'leonard.hayes@harmonygames.co'
  snippet     'Fyi, this came through from Carta. Thanks for sorting out the extra time. Calvin ---------- Forwarded message ---------'
  history_id  NULL
gmail.gmail_messages
  id            'leonard.hayes@harmonygames.co/<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0Ws@mail.gmail.com>'
  thread_id     (above)
  label_ids_json '["INBOX", "IMPORTANT", "Label_b19fb8d1b3", "CATEGORY_PERSONAL"]'   -- Label_b19fb8d1b3 = "Opened"
  internal_date 1770135644000 ; date '2026-02-03T16:20:44Z'
  subject       'Fwd: Your option grant at [SOURCE_ORG_0001] Games Inc. has been updated'
  from_email    '[EMAIL_0801]' ; from_name 'Calvin Price'      -- the address on ENG-2452
  to_json       '["leonard hayes <leonard.hayes@harmonygames.co>"]' ; cc/bcc/reply_to '[]'
  body_text:
    Fyi, this came through from Carta. Thanks for sorting out the extra time.\r\n\r\nCalvin\r\n\r\n
    ---------- Forwarded message ---------\r\nFrom: SVC_0077_NAME <SVC_0077_EMAIL>\r\n
    Date: Fri, Jan 23, 2026 at 10:05 AM\r\nSubject: Your option grant at [SOURCE_ORG_0001] Games Inc. has been updated\r\n
    To: <[EMAIL_0801]>\r\n\r\n
    = Your option grant has been updated. =\r\n\r\n
      [SOURCE_ORG_0001] Games Inc. has extended the post-termination exercise period on your\r\n
    option grant. Current holdings and overview of the changes summarized below: \r\n\r\n
     Equity awards     ID ES-3   Acceptance status Accepted   Granted 8,138  \r\n
    Vested 4,408   Exercised 0   Grant date Nov. 10, 2023   Termination date\r\n
    Oct. 24, 2025   Last day to exercise Apr. 24, 2026 (previously Jan. 24, 2026)    \r\n\r\n
      View your holdings on Carta <https://app.Carta.com/portfolio/> \r\n\r\n
    [then the base SVC_0077 footer, verbatim from 1847333347700620793: "Learn more about Carta …" through "333 Bush Street … San Francisco, CA 94104"]
  headers_json  From / To / Subject / Date "Tue, 3 Feb 2026 08:20:44 -0800" / Message-ID / MIME-Version, in base gmail.com shape
  in_reply_to '' ; references '' ; mbox_from '1856121753043675905@xxx Tue Feb 03 16:20:44 +0000 2026' ; attachments '[]'
```

Wording constraints:

- No question in Calvin's text, so the open-question rule is not triggered.
- No "closing" in the text, so Told stays No.
- Only ES-3 is named, so the extension is not applied to ES-5 or ES-16.
- The old date appears in the text, which links the correction to the original (v2 Part 3.2).
- The termination date is restated (KPMG guard).

Coherence (evaluator-only, optional):

- No Carta digest is needed: the base has none after Dec 2024.
- No admin notice to Leonard is needed if Robert or Arthur entered the change; Arthur signs grants in Carta (1782897835407336831).
- Optional: one Robert-mailbox admin row for the lifecycle. It does not change persona reach.

### V1 (the Carta admin stream, documented only: in plain view)

1. "[SOURCE_ORG_0001] Games Inc. sent you a Board Consent"
   - From SVC_0077, 2026-01-22T23:41:37Z (15 minutes after Leonard's base login alert), thread 1855062327427686213, To Leonard.
   - Additional message: "Hi all,\n\nThis gives Calvin another 90 days on his options (ES-3), so his last day to exercise moves from January 24 to April 24, 2026.\n\nBest,\nLeonard"
   - Consent name: "Post-Termination Exercise Period Extension - ES-3 - 01/22/2026".
2. "Board consent approved for [SOURCE_ORG_0001] Games Inc."
   - 2026-01-23T17:52:06Z, thread 1855130934706564871.
   - To "PERSON_4337_EMAIL, leonard.hayes@harmonygames.co, robert@harmonygames.co".
   - "Approval date 2026-01-23T17:52:05.418207".
3. Optional digest, "Carta activity for Jan. 23, 2026": 2026-01-24T10:31:12Z, thread 1855193792643974477, line "Leonard Hayes modified  option grant ES-3 <https://app.Carta.com/options/list/3048065/?open=18258522> for Calvin Price".
4. Robert copies of rows 1 and 2.

The Message-IDs follow `<{epoch_centiseconds}.10.{19-digit}@notifications-email-sending-worker-{hash}-{5}>`. All thread ids were checked: no collisions.

### Landing estimate (cold, for an Opus 5.5 run that reads broadly)

- **V1: about 20-25%.** It is read with the Carta sweep, and Opus reconciles a later Carta date (it already reconciled ES-17's letter against Carta).
- **V2: about 55-60%.**
  - Ways a run finds it: opening every "carta" hit, which rev1p did not do; listing all mail since Feb 1, about 30-40% of runs; or checking each lapsed holder's issue email, which is rare, because Told is moot for lapsed lines.
  - Once seen, about 0.9 apply it.
  - Expected result: about 3-4 of 6 baseline runs miss it.

## 6. UGT risks and independence

UGT risks and mitigations:

1. **Expiry timing.** The extension is dated Jan 23, before the Jan 24 lapse. Never date it Jan 24 or later.
2. **"Is the holder notice the Carta record?"** It is Carta's own text, and it is later than the termination notice. It states the old date, and the close-out rule says Carta governs over letters. Keep the full "Equity awards" block.
3. **Told.** Inbound mail from Calvin; Leonard never replied; nothing about the closing. Told is No on every reading.
4. **Linear comment.** "No mail with that address before Feb" stays true (the forward is Feb 3). Do not edit the comment; any edit would point straight at the forward.
5. **Over-application.** ES-5 and ES-16 have the same Jan 24 date. The carrier names only ES-3, and the guard rows P_lapsed_ES5 and ES16 stay.
6. **NB-32 (Douglas) untouched.**
7. **Order rule.** Calvin's Apr 24 is unique, so there is no tie. Vincent stays first.
8. **ES-3 name forms.** Carta uses "Calvin Price"; the 2023 digest and Slack use [0029] [0047]. The issue title "Calvin Price" matches the forward's sender name.
9. **Underwater options.** Strike $0.16 against a 409A of $0.10. No record may claim value, and the note should not urge exercise. This matches the letters' "exercising is not recommended".

Independence from the other candidates:

- **(a) Bounced Feb 11 letter.**
  - It targets one of ES-1/4/7/12/13/15 (told → not told, Date → Full note). It is a separate record and a separate holder, so the two are independent.
  - Shared cells: the Full-note count (2 → 3 with (b), → 4 with both) and the labels-count line. Do not grade a combined Full-note count as a single row.
  - (a) moves C_DATE (6 → 5) and leaves N_COUNT alone; (b) moves N_COUNT and leaves C_DATE alone.
- **(c) Contacts-only alias.** Keep it off ENG-2452. The V2 carrier comes from Calvin's issue address, so an alias on Calvin would couple the two traps.
- **(d) ADV.** P1 becomes double-gated (ADV and CARTA_EXT). Put the weight-5 trap row on ENG-2452 itself (Owed or N_Calvin), not on P1 alone.

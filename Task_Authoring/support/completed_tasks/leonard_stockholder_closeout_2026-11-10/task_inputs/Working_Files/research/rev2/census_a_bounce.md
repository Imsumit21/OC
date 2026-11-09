# Census (a): bounced termination letter ("a done source with a missing piece")

Status: COMPLETE. Read-only scout. Base = Feb 14 2026 normal universe through `hg.py search`; overlay = `01_Universe_Inject.sql` read as text. Clock 2026-02-14 00:00 UTC. No SQL executed.

**Verdict: GO, conditional.** Holder: **Owen Baker, ENG-2457 (ES-12)**. Placement: a Gmail "Delivery Status Notification (Failure)" **inside Owen's own letter thread** `leonard.hayes@harmonygames.co/1856860994291529096`. Base convention requires that placement; an off-thread notice would be unrealistic. Flips: Told Yes -> No, Owed Last day -> Closing and last day, date-note count 6 -> 5, full-note count 2 -> 3. Cold landing estimate (an Opus 5.5 run misses it): about 50% (range 35-65%). The graded weight is modest: 8 to 11 points. Marcus (ENG-2456) also qualifies on structure, but realism rules him out. No other holder qualifies.

## 1. The six Feb 11 letters and every other "told" record per holder

All six are base, single-message threads in Leonard's mailbox, labels `ARCHIVED, SENT`, cc Robert and Arthur. Robert's and Arthur's copies (threads/0001687x.json, blake@...) land in their INBOX. Times are UTC.

| # | Leonard thread | Message-ID | Sent | To | Holder | Effective in letter | Other written, direct telling (Leonard-visible) | Qualifies? |
|---|---|---|---|---|---|---|---|---|
| 1 | 1856858053929740799 | CAPBs_a6Yybo-pYW3AcD9pbRjE-5M9PF6Br-x4eHycGmTT_kvBw | 20:10:30 | PERSON_2360_EMAIL | ENG-2453 Claire Morgan (ES-4); subject "Notice of Involuntary Termination at [SOURCE_ORG_0001]" | Dec 31, 2025 | Group DM C51ECE5102ED idx 0 (1770837657.515519, Leonard: "Harmony Games'i officially kapatiyoruz"). **Receipt:** idx 1 (1770903714.600249) "mailde öyle birşey gördüm" (she saw the deletion clause in the mail) | NO, told twice and receipt proven |
| 2 | 1856860994291529096 | CAPBs_a5HKTOGV3nwn6iyxz8GhwLGRaF_Gs-uii3x7tVQ9eTfQQ | 20:13:48 | PERSON_3140_EMAIL | **ENG-2457 Owen Baker (ES-12)** | "January 31, 2025" (year typo, NB-22) | **None.** D05SDEQEK61 Feb 11: "I have some announcements to make" / "Yes, joining" (verbal meeting, no content). #company-internal C05KNDCHAAG idx 40 is a `<!here>` channel post, not direct. #prototype has no closing statement | **YES** |
| 3 | 1856861229984402233 | CAPBs_a7PEUhJxyDkK6zqmr_6ip4Aa-NoxCxXV=Y445iiYeqtFw | 20:15:32 | PERSON_4363_EMAIL | ENG-2458 Martin Walsh (ES-13) | Jan 31, 2026 | DM D05Q3QAH2QZ idx 2 (1770824780.548099, 15:46): "we will be shutting down harmonygames ... send Everyone official termination letters" | NO, told by DM |
| 4 | 1856861323365646598 | CAPBs_a68cKP-7WXJ64u6bGrkYWVnTNN6wY-Gv_ubOi7MzWUg6g | 20:16:46 | marcus.bennett@harmonygames.co (work) | ENG-2456 Marcus Bennett (ES-7) | Jan 31, 2026 | None Leonard-visible: DM D05UDNCCYKC Feb has only his Feb 1 invoice thanks; #company-internal idx 40 is a channel post | Yes on structure; **rejected on realism** (sections 3, 7) |
| 5 | 1856861400116562076 | CAPBs_a68Agj+37mZ6abeW5KEKTh00he+mgOpLP2FrpDjeO-37Q | 20:17:49 | PERSON_4243_EMAIL ("brian") | ENG-2460 Brian Foster (ES-15) | Dec 31, 2025 | C51ECE5102ED idx 0; he answers in idx 3. DM D076PSEBC4D Feb 12 idx 6-12: "Harmony Games kapansa da ..." | NO |
| 6 | 1856861462411533365 | CAPBs_a6eEJzbqr9Lvu=6zTwV1ezqBb=CbBQP5BCq=yiC4PrLTA | 20:18:37 | PERSON_2361_EMAIL | ENG-2450 Julia Lawson (ES-1) | Dec 31, 2025 | C51ECE5102ED idx 0. **Receipt:** idx 2 (1770905067.492509) "Mailler ulaştı abi" (the mails arrived) | NO, receipt proven |

The mapping is confirmed against the issue emails in the SQL: ENG-2450 PERSON_2361, ENG-2453 PERSON_2360, ENG-2456 marcus.bennett@, ENG-2457 PERSON_3140, ENG-2458 PERSON_4363, ENG-2460 PERSON_4243. Each letter address equals the issue address.

**Qualifying holders, told by the letter alone: ENG-2457 Owen and ENG-2456 Marcus.** The other four have a second written, direct message (three of them through the group DM, Martin through his own DM), and two have receipts on record.

Evaluator-only (Leonard cannot see these): Owen's Feb DMs with Arthur (D05S1S2AB5M, Feb 2-12, work only) and with Robert (D05SJRKTUMS, Feb 3, work only) never mention the closing. Marcus's DM with Robert (D05UDNCCFEW, Feb 12) reads "thoughts and plans on next steps / What's your situation like?", and Marcus answers "Updating my CV". He knows, but the message does not tell him.

## 2. How the base represents delivery failures (DSN conventions)

Searches over all of base Gmail, all with `scan_complete` true: "Address not found" 235 files, "wasn't delivered" 237, "Delivery Status Notification" (limit reached; all numbered files), "Undeliverable" 3 (1 Leonard, an Outlook forward and not a DSN), "mailer-daemon" 0 and "postmaster" 0 (the sender is anonymised), "Message not delivered" 2, "Delivery incomplete"/"(Delay)" 2 threads, "Message blocked" 6, "is disabled/inactive" 18, over-quota/"storage space" 0 DSNs.

- **Sender:** `PERSON_3555_NAME <PERSON_3555_EMAIL>` (Mail Delivery Subsystem) in every case; `Return-Path: <>`, `Auto-Submitted: auto-replied`, `X-Failed-Recipients: <address>`, `Content-Type: multipart/report; report-type=delivery-status`.
- **Subject:** `Delivery Status Notification (Failure)`; also `(Delay)`.
- **Labels (Leonard):** `["INBOX", "IMPORTANT", "Label_b19fb8d1b3", "CATEGORY_UPDATES"]`. The DSN goes to the Updates tab, which explains why Leonard never saw it. Leonard's base messages never carry UNREAD.
- **Message-ID:** `<{8 hex = epoch seconds}.{xx}0a0220.{5-6 hex}.{4 hex}.GMR@mx.google.com>`, e.g. `<67eacf9d.050a0220.2fc69.b0cd.GMR@mx.google.com>` (0x67eacf9d = 1743441821, equal to internal ms / 1000).
- **Body shapes, verbatim families:** "** Address not found **\n\nYour message wasn't delivered to X because the address couldn't be found, or is unable to receive mail.\n\nLearn more here: https://support.google.com/mail/?p=NoSuchUser|DisabledUser\n\nThe response was:\n\n550 5.1.1 The email account that you tried to reach does not exist. ..." or "550 5.2.1 The email account that you tried to reach is disabled|inactive. ...". The latter is Leonard 1829704071676306712, victor.barnes@, a departed holder. Other families: "** Message not delivered ** There was a problem delivering your message to X ..." (timeout), "** Delivery incomplete ** ... Gmail will retry for N more hours", "** Message blocked ** ... 550 5.7.1". The body does not quote the original.
- **Threading:**
  - When the original sits in the mailbox, the DSN shares its thread. In_reply_to and References both equal the original Message-ID.
    - Robert 1769337688765186323 (threads/00001116.json): send at [0], DSN [1] arrives 9 s later, then Robert resends to a corrected address [2] ("typo in the first email address").
    - Leonard 1810030685221873164: his reply [4], Delay notices [3] and [2], then Failure [1], all in the thread.
    - Leonard 1828131137010192802: the send [1] is followed 15 s later by the "Message blocked" DSN [0].
  - DSNs stand alone only when the original is not in the mailbox: the 19 standalone Leonard DSNs all answer `<calendar-...@google.com>` invites.
- **Ids:** thread id = Gmail id of the first message; `id >> 20` is about the ms timestamp (1856860994291529096 >> 20 = 1770840639392, the draft start 3 min before the send). DSN Gmail id example: (1770840837000 << 20) + r, about 1856861201498524345. The SQL sets mbox_from to NULL.
- **SQL convention for adding to an existing thread:** INSERT the message, then `UPDATE gmail.gmail_threads SET snippet = <new message's snippet>`. Snippet = first 140 chars of the whitespace-collapsed body (SQL lines 103-106 do this for Robert's reply on a 2023 thread).

**Realistic placement: inside the letter's own thread.** An off-thread notice contradicts base convention.

## 3. Coherence: later records showing receipt

**Owen, no contradiction found.**
- The letter's Message-ID exists only in Leonard's, Robert's and Arthur's copies; no Owen mailbox holds it.
- Owen's work mailbox (owen@harmonygames.co_*, 1,595 threads) ends Feb 10 17:19 UTC.
- Owen's Feb Slack (14 channel events, 4 DMs) is work talk and leave events. Nothing mentions a letter, a mail, termination or the 2025 typo.
- The Carta notice 1856960504234892536 (to Leonard; "Acceptance status Accepted", last day April 30, 2026) makes no delivery claim.
- The address came from Owen himself in Sept 2023 ("Personal email: PERSON_3140_EMAIL", group DM C05UX5SCEF2, via his work-mailbox Slack digest owen@..._1778237314398120322 [3]).
- The seeded ENG-2457 comment reads "No mail with that address before Feb". An inactive account fits all of this.

**Marcus, rejected.**
- Leonard's #company-internal idx 40 (Feb 11 19:59) says Google accounts are archived "by Feb 15", so Marcus's account was alive at 20:16.
- His mailbox has a delivered mail at Feb 11 16:55 UTC (marcus.bennett@..._1856848739436182339).
- His Slack is active.
- A Workspace bounce on an internal address that day contradicts all three. His issue email is the same address, so any note route is also dead.

## 4. Run path (rev1p pre-check, run 6aed9d01a1cb8067d8ac7dee)

Gmail calls from calls.jsonl, events: 56/57 searches (KPMG, Board position); 60/62 thread reads; 69, 114, 124, 207 Carta searches with batch reads 78, 127, 216-236; **294 `gmail_list_messages` "after:2026/02/08" include_spam_trash, result 295: 194 ids + threadIds, no snippets, complete**; 303-313 thread reads (Sunset, KPMG, 1841635707568607753, 1856861681308161749, 1856872398290956689, Nebojsa); **381 list "after:2026/02/08 (from:me OR robert OR arthur)" (38)**; **386 metadata batch on those**; **394 `get_messages_batch` full on the six letter Message-IDs plus two others** (spilled, decoded at 396/407); ev 412 decision "Termination letters explicitly say 'The company is shutting down' — those count as told"; 685/686 per-address searches for PERSON_2360/2361 only, with `-after:2026/02/01`; 455/494/724 searches on angel addresses; 814-852 drafts. In the decoded results the letter threads sit at positions 80-85 in 295 and 18-23 in 382.

Would an in-thread DSN have come back?
- 295: **yes, but only as an opaque id** (`<698ce305...GMR@mx.google.com>`) whose threadId equals Owen's letter thread. The run picked threads from this list by id pattern (event 302) and did not open letter threads.
- 381/386: no, because the DSN is not from me.
- 394: no. Reads by message id never return a sibling.
- No `gmail_get_thread` on any letter thread (24 thread reads, none of the six).
- No search on PERSON_3140.
- No `gmail_list_threads`, which would have shown the updated thread snippet.

**In this run's path the DSN would not have been read, so it would very likely have landed.** It is SAME_PLACE only for a run that opens the letter thread, or that reads the ids from a bare-address search on PERSON_3140 (the body and X-Failed-Recipients carry the address). A `to:PERSON_3140_EMAIL` search returns only the letter.

## 5. Exact flips and gradable-surface slots

Truth ENG-2457 changes:
- Told Yes -> **No**.
- Owed "Date note" (sheet: Last day) -> **"Full note" (Closing and last day)**.
- State Todo, unchanged. Options 8,477 now / 16,277 at Dec 31, unchanged. Last day 2026-04-30.

Counts:
- Already told 4, Closing 6, Covered 2, Last day **5** (was 6), Closing and last day **3** (was 2), Nothing 6 = 26.
- Notes still 14 (6 + 5 + 3). Told Yes count 10 -> 9.

Draft: Owen's note must tell him the company is closing, as news. The rev1p date note ("Following up on the closing news and the termination letter I sent on February 11", ev 824) becomes wrong. It still says he holds 8,477 vested options and that his last day is April 30, 2026.

Linear: no state or comment change, because he still gets a note. #winddown "who goes first": Vincent (Feb 21) still first; the Apr 30 group now has two untold holders, Owen and Oliver. D6 is unchanged.

Slots (current total weight 234):
- Flips: **C_DATE** (w3): the requirement changes from "6" to "5". Caveat: its regex `(Date note|Last day).{0,160}(6|six)` is loose. The "Last day" header followed by any digit (for example 25,432) can satisfy it, so it may not discriminate today either.
- New: **C_ES12** `["field","ENG-2457","Owed"]` w5, mechanism BOUNCE.
- New: **TC_ES12** `["field","ENG-2457","Told"]` w3.
- Do not add a note regex like N_Oliver's `(Owen|0068).{0,160}(clos|shut|wind)`: the rev1p date note passes it. If the note is graded at all, use a judged rubric row ("tells him about the closing as news").
- No flip: ND_ES-12 (w1; still has "Apr", so regroup it as a full note), LS_ES-12, AL_ES-12, P_live_ES-12, N_COUNT, D6.
- Discriminating weight: 8 new (+3 if C_DATE is fixed), out of about 242.

Solver change:
- Add `BOUNCED = {"ENG-2457"}`; told = letter and not bounced.
- New rule BOUNCE: decides Told, Owed; controls ENG-2456 and ENG-2458 (same-day letters delivered).
- Natural reading: "the Feb 11 letter told him".
- over_application `bounce_over`: treats a delivered letter as bounced.
- ch_bounce: "the delivery failure is not found: the member counts as told".

## 6. Drafted carrier (base conventions; text only)

```sql
INSERT INTO gmail.gmail_messages (id, thread_id, user_email, label_ids_json, snippet, internal_date, date, size_estimate, subject, from_email, from_name, to_json, cc_json, bcc_json, reply_to_json, body_text, body_html, headers_json, in_reply_to, "references", mbox_from, attachments_meta_json)
VALUES ('leonard.hayes@harmonygames.co/<698ce305.050a0220.3b7f1c.9d2e.GMR@mx.google.com>', 'leonard.hayes@harmonygames.co/1856860994291529096', 'leonard.hayes@harmonygames.co', '["INBOX", "IMPORTANT", "Label_b19fb8d1b3", "CATEGORY_UPDATES"]', '** Address not found ** Your message wasn''t delivered to PERSON_3140_EMAIL because the address couldn''t be found, or is unable to receive ma', 1770840837000, '2026-02-11T20:13:57Z', 7486, 'Delivery Status Notification (Failure)', 'PERSON_3555_EMAIL', 'PERSON_3555_NAME', '["leonard.hayes@harmonygames.co"]', '[]', '[]', '[]', E'** Address not found **\r\n\r\nYour message wasn''t delivered to PERSON_3140_EMAIL because the address couldn''t be found, or is unable to receive mail.\r\n\r\nLearn more here: https://support.google.com/mail/?p=DisabledUser\r\n\r\nThe response was:\r\n\r\n550 5.2.1 The email account that you tried to reach is inactive. For more information, go to https://support.google.com/mail/?p=DisabledUser 5b1f17b1804b1-4835a1f7e2csor2210417f8f.11 - gsmtp', NULL, '[{"name": "Message-ID", "value": "<698ce305.050a0220.3b7f1c.9d2e.GMR@mx.google.com>"}, {"name": "Date", "value": "Wed, 11 Feb 2026 12:13:57 -0800 (PST)"}, {"name": "Subject", "value": "Delivery Status Notification (Failure)"}, {"name": "From", "value": "PERSON_3555_NAME <PERSON_3555_EMAIL>"}, {"name": "To", "value": "leonard.hayes@harmonygames.co"}, {"name": "Auto-Submitted", "value": "auto-replied"}, {"name": "In-Reply-To", "value": "<CAPBs_a5HKTOGV3nwn6iyxz8GhwLGRaF_Gs-uii3x7tVQ9eTfQQ@mail.gmail.com>"}, {"name": "References", "value": "<CAPBs_a5HKTOGV3nwn6iyxz8GhwLGRaF_Gs-uii3x7tVQ9eTfQQ@mail.gmail.com>"}, {"name": "X-Failed-Recipients", "value": "PERSON_3140_EMAIL"}]', '<CAPBs_a5HKTOGV3nwn6iyxz8GhwLGRaF_Gs-uii3x7tVQ9eTfQQ@mail.gmail.com>', '<CAPBs_a5HKTOGV3nwn6iyxz8GhwLGRaF_Gs-uii3x7tVQ9eTfQQ@mail.gmail.com>', NULL, '[]');
UPDATE gmail.gmail_threads SET snippet = '** Address not found ** Your message wasn''t delivered to PERSON_3140_EMAIL because the address couldn''t be found, or is unable to receive ma' WHERE id = 'leonard.hayes@harmonygames.co/1856860994291529096';
```

Notes on the carrier:
- 9 s after the send (base precedent 9-15 s).
- 0x698ce305 = 1770840837.
- The id "698ce305" has 0 hits in base Gmail.
- It arrives 6.5 min before Leonard's "All termination letters are sent" (#winddown 1770841239.761999), so his done line was written without noticing it.
- I chose "inactive" (DisabledUser) over "does not exist" because Owen gave this address himself in 2023 and accepted his Carta grant (granted Jan 2024).
- Do not touch the issue, the notes doc or the prompt.

**Landing (miss) estimate: about 50%.** Path weights:
- Path A, as in rev1p (find the sends, batch-read them by id): P about 0.5, miss about 0.8. The catch chance is triage of the Feb list by metadata, or noticing the GMR id.
- Path B (search "termination", then read): P about 0.3, miss about 0.45 (about half use `get_thread`).
- Path C (per-address told search, invited by the seeded "No mail with that address before Feb" comment): P about 0.2, miss about 0.3, almost entirely when the search uses `to:`.
- A `gmail_list_threads` call exposes the snippet (rare).

Hardness v2 Part 2 warns that same-thread corrections are usually caught. This one survives only because these letters are single-message threads that agents read by message id. Expected loss is about 0.5 x 8-11, roughly 4-5.5 weight per run, about 2 points of score. It is a modest lever on its own.

## 7. UGT risks and independence

**UGT risks:**
1. "Sent" literalism, low-moderate. The notes say "a written message ... sent to them directly", and a bounced letter was sent. The DSN's "wasn't delivered" makes "not told" the natural reading. Do not reword the notes: "reached them" would point at the trap.
2. Verbal knowledge, low. Owen joined the Feb 11 meeting (D05SDEQEK61) and kept working. The written-and-direct rule excludes this, and the design's precedent agrees (Oliver: a channel post with a reply is not told).
3. **Note address.** "Messages go to the email on each holder's issue" points to PERSON_3140, the dead address. A strong run may draft to it and flag the bounce, or use owen.baker@ (alive until Feb 15). The rubric and Oracle Events must not grade Owen's To, and must accept a flag. This is the main second reading to neutralise.
4. Use Failure, not Delay. A Delay notice before the clock would leave delivery open.
5. "Mailler ulaştı" (Julia, C51ECE5102ED idx 2) is first-person plural in a group DM Owen is not in. A run might overgeneralise it; that is not a rubric risk.

**Independence:**
- (b) Carta extension of a lapsed line: different holder; it changes Nothing -> Closing and last day, not Last day, so C_DATE (5) is unaffected and both traps raise the note count. Mild positive correlation: a run that triages Feb mail by subject sees both a "Delivery Status Notification (Failure)" and a Feb Carta notice.
- (c) Contacts alias: must not use ENG-2457 or PERSON_3140. A run chasing Owen's dead address may open Contacts looking for another address, which would couple (c) to (a) if (c) is an option holder. Keep (c) on a stock holder.
- LETTER and ASK are unaffected. The LETTER controls ENG-2450/2460 have receipts, so over-applying the bounce to them is detectable.

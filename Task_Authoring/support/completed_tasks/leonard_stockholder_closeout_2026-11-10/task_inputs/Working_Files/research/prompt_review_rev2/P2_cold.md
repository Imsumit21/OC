# P2 cold pass (Cross-Service Coherence and Feasibility), second independent run

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
Prompt sha256 45766344a3e4; SQL sha256 78af8ace66a9 (read as text, never executed).
Pass ID: P2. Angle: for every injected record, the nearest base records (same thread, same sender,
same day, same person in other services) and the base conventions it must imitate.
Searches: `Task_Authoring/tools/hg.py search` only (base universe), persona view applied by hand
(Leonard Hayes, leonard.hayes@harmonygames.co; acl.md).

## Findings (deep_recheck format)

`DR# | pass | checklist section | quote | record path, id and quoted value | Eval dimension | proposed score or severity`

none — 0 scored findings. Checked: 1 prompt paragraph (7 sentences), 130 INSERT + 15 UPDATE
statements (every injected record), 25 holder addresses re-derived against Leonard's mailbox,
14 base Carta termination notices, 3 Slack parents, 2 Gmail cross-mailbox copies.

No State/Lifecycle defect and no low-impact item that changes a graded value, set, order,
recipient or destination. The items below are advisories under the deep_recheck main-session
rule (they name records the answer never reads for a graded value), listed so the main session
can overrule if it counts them differently.

## Advisories (not scored; main session may re-grade)

| A# | Injected record | Nearest base record(s) and quoted value | Why it is an advisory, not a finding |
|---|---|---|---|
| A1 | Date headers of the injected sent mails: Leonard `<CAPBs_a7Tq2LmV9x…>` "Fri, 13 Feb 2026 17:12:40 +0000", `<CAPBs_a5Wn3RvK8y…>` "Fri, 13 Feb 2026 18:19:02 +0000", `<CAPBs_aLeDrdRoqOb…>` "Thu, 12 Feb 2026 22:52:17 +0000"; Robert `<CAGkro_Tn7wQ2xLp…>` and `<CAGkro_PbX4mT7nQe…>` "+0000" | Every base sent message from these senders carries a local offset: Leonard `<CAPBs_a5B01FzMbH…>` (threads/leonard@harmonygames.co_1856958794180374704.json /messages/0) "Thu, 12 Feb 2026 14:14:52 -0800"; Leonard `<CAPBs_a5HKTOGV3n…>` "Wed, 11 Feb 2026 12:13:48 -0800"; Robert `<CAGkro_P4BDkj2Xc…>` "Wed, 21 Jun 2023 11:28:44 -0700". The injected quote lines themselves say "On Fri, Feb 13, 2026 at 8:48 AM" (Pacific). | Header-only convention; the ISO `date` column is right and no graded value reads the offset. Eval 0 style advisory. |
| A2 | Superhuman Message-ID `<mlkq74xd.3f9e2c1a-…@we.are.superhuman.com>` on the Sunset mail sent 2026-02-13T18:06:21Z | Base Superhuman ids encode draft time in base36 ms 2–38 min before send: `mlimxple` → 2026-02-11T23:02:34Z (sent 23:05:00), `mljzlvsh` → 21:45:04Z (sent 22:22:58). `mlkq74xd` → 2026-02-13T10:09:25Z, about 8 h before send (02:09 PST). | Shape is right; the timing quirk is invisible to the agent. Cosmetic. |
| A3 | Contact update `db57e559500151d6b3991b62` job "Investor and advisor (left the board May 2025)", updated_at 2025-05-02 | Base: contacts.json /contacts/159 "Matthew Collins … Independent Director (investor/advisor, not an employee)"; Slack #admin_foundersonly C04UEQVDVB7/2025-05 /49 (2025-05-01) "[PERSON_NAME_36604] is resigning from the board"; but gcal /events/5193 and /events/6444 "[SOURCE_ORG_0001] July 2025 Board Meeting" 2025-07-16, organiser Leonard, attendee matthew.collins@harmonygames.co "responseStatus": "accepted", updated 2025-07-11T19:05:53Z. Oct 2025 and Jan 2026 board invites (/events/5269, /events/9484) drop him. | The base Slack grounds the May 2025 date; the July invite is a stale series instance. Directors in office now rest on Robert's injected Feb 12 mail ("That leaves Leonard and me on the board"), which agrees with the Oct 2025/Jan 2026 invites and with base Slack C04UEQVDVB7/2025-07 /73 "now we have the majority of the board seats". No graded value changes. A stricter reviewer could call it one minor inconsistency. |
| A4 | UPDATE of base mail `<CAPBs_a6zM=or+nDw0…>` body (Leonard and Arthur copies, 2024-11-26 owner list): removes the line "(Total ownership percentage adds to 100%)." | The pre-send ChatGPT draft in Slack C04UEQVDVB7/2024-11 /55 (Leonard-visible) still ends "(Total ownership percentage adds to 100%)". The listed percentages sum to 94.129% (computed), matching the injected sheet note "the list's percentages … only add to about 94%". | A sent mail differing from its chat draft is normal; the edit is applied to both mailbox copies and no reply quotes the removed line. History rewrite with no graded effect. |
| A5 | KPMG 2025 request `<LV3PR19MB8524F1C07D3A…>` item 2: "using each effective date as Carta shows it, regardless of when recorded" | Same associate's base 2024 request `<LV3PR19MB8524A7F34357…>` (threads/leonard@harmonygames.co_1817557789846606177.json /messages/6) is a generic "Please see the attached confirmation"; Message-ID host, sender, signature, subject pattern and Cc list (minus the "[Deactivated]" PERSON_3077) all match. | Realistic edit of a real yearly request; the Carta-specific phrasing reads as tuned to the trap, a P4-type naturalness note on a record, not a coherence defect. |

## Neighbour checks that passed (evidence)

**Gmail delivery-failure notice** `<698ce305.050a0220.3b7f1c.9d2e.GMR@mx.google.com>` in thread
leonard.hayes@harmonygames.co/1856860994291529096. The parent is base Leonard's "Termination of
Independent Contractor Agreement" to PERSON_3140_EMAIL, 2026-02-11 12:13:48 -0800; the DSN arrives
9 s later. It matches the base DSN in Robert's mailbox (threads/00003106.json): sender
PERSON_3555, labels INBOX/IMPORTANT/Opened/CATEGORY_UPDATES, `Auto-Submitted: auto-replied`,
`X-Failed-Recipients`, Date with "(PST)", In-Reply-To = the letter. The GMR hex prefix 698ce305
decodes to 2026-02-11T20:13:57Z, the same as its own date (base 64934165 also decodes to its own
date). Sibling letters to PERSON_2361, PERSON_4363, PERSON_4243 and PERSON_2360 on Feb 11 have no
bounce. No later reply from PERSON_3140 exists. Robert's copy of the same letter (threads/00016874.json)
is the NB-22 letter ("effective January 31, 2025"); see the cards below.

**A holder forwarding a Carta notice** `<CAJr7mPx2QwF8nVb…>` from Calvin Price `[EMAIL_0801]`,
2026-02-03. The base admin notice (threads/leonard@harmonygames.co_1847333347700620793.json,
2025-10-29) gives "ES-3 … Granted 8,138 Vested 4,408 … Last day to exercise Jan. 24, 2026". The
forward quotes "Termination date Oct. 24, 2025 Last day to exercise Feb. 20, 2026 (previously Jan.
24, 2026)", dated Jan 23 (before the old last day). `[EMAIL_0801]` is Calvin's base address
(threads/leonard@harmonygames.co_1782034095239486005.json "Calvin Price: [EMAIL_0801]"). The base
Oct 29, 2025 Slack thread C04UEQVDVB7/2025-10 /492 computes his 4,408 × $0.16 = "$705". The
Carta-template body matches base notices. Thread id 1856121753612004097 >> 20 = 2026-02-03T16:20:44Z.

**A founder mailing an investor under a nickname.**
- Robert's "Hey [PERSON_NAME_0112]" `<CAGkro_PbX4mT7nQe…>` replies in the base 2023 Funds Transfer
  thread. In-Reply-To is the base `<CAGkro_Ox2wP8TQ…>`, and its quote "On Fri, Aug 11, 2023 at 1:00 PM
  … > Thanks!!!" matches base 13:00:43 -0700. Copies sit in Leonard's thread (cc) and Robert's
  (threads/00001367.json). The nickname is grounded in base threads/00000046.json: "Kris, Patrick,
  Arthur and [PERSON_NAME_0112] paid up".
- Leonard's "Hi Akin" `<CAPBs_aLeDrdRoqOb…>` goes to PERSON_8862_EMAIL, which appears nowhere in
  base. Akin = Matthew Collins is grounded in records Leonard can see: the mail
  "Accepted: Akin <> [SOURCE_ORG_0001] @ Tue Apr 4, 2023 8am" (threads/leonard@harmonygames.co_1761837015370484134.json)
  and the gcal event "Matthew Collins <> [SOURCE_ORG_0001]" 2023-04-04T15:00Z on Leonard's
  calendar. "on the board and since" fits base Slack C04UEQVDVB7/2025-05 /49–51 ("resigning from
  the board … still gonna support us for fundraising") and Trello card 454 "…/Akin for referrals"
  (Nov 2025).

**Slack thread replies.**
- #executives reply 846a70ba… is posted under Leonard's own ChatGPT paste b658ec71… (base
  reply_count 0 → set 1/1/latest 1768418331.402719, correct). Its claim "chatgpt has the other seed
  investors a couple of shares off … go by the ledger" checks out. The paste has Seed 3,051,881
  (other investors 305,188). The base ledger in gdocs /docs_documents/40 (Leonard-owned) has "Series
  Seed Preferred (all non-founder investors): 3,051,879", so others = 305,186, 2 shares off.
- The ledger also reconciles with the line items. Non-Griffin seed = TOR 50,865 + [PERSON_NAME_0089]
  50,865 + 8 × 25,432 = 305,186. The base advisor grants (threads/leonard@harmonygames.co_1773160163779741845.json
  /messages/1: 30,518 / 61,038 / 6,104 / 6,104 = 103,764) plus the 14 Carta-notice lines give
  exactly the ledger's "Options outstanding: 268,772" (165,008 + 103,764).
- #winddown replies under e3e198cc… (base reply_count 0 → set 4/2/latest 1770949437.902269,
  correct). Authors Leonard and Arthur are both in C0ADGSZKR3R members. All injected Slack
  timestamps fall before 2026-02-13T10:03Z, and every Slack `ts` decodes to its created_at. The top-level posts at
  23:15 Feb 12 follow the last base post (23:04 ":+1:") and match base msg 188 "linear we keep
  during transition".

**Linear comments on every issue.** ENG-2438…2463 continue the base maximum ENG-2437 (created
2025-11-07). The creator usr_63fffeb4fab5233e = Leonard, and state names are base values. Base
Linear has zero comments (NB-24). Every "Nov 2024 owner list: N" equals the base owner list
(threads/leonard@harmonygames.co_1816809274978043917.json). Every "Last mail with that address
before Feb" was re-derived from Leonard's mailbox; 25 of 25 addresses match. The checks include Jan 24, 2026 = 2026-01-25T00:40Z (PST date), Claire's
May 1, 2023 Reply-To mail, and the "No mail" for PERSON_3641, [EMAIL_0801] and PERSON_3140.

**Other injected records.**
- Robert's "Re: Board position" exists in all three mailboxes its recipients hold; the Robert and
  Arthur thread ids are base (threads/00016903.json, blake@…_1856959418725253571.json).
- Gmail thread ids decode to first-message time (KPMG 16:48:35, Sunset 18:06:22, Akin 22:52:17).
- Thread snippets equal the latest message's snippet. Labels match same-sender base messages, and
  the KPMG Outlook host LV3PR19MB8524 matches the 2024 request.
- Trello card idShort 456 follows the base max 455. Ids 698e5a10/698f6a03 decode to their action
  dates, PERSON_6094 = "leonard.hayes", and the URL pattern matches the base.
- The Drive root d_63fffeb4fab5233ed5bb73 is Leonard's.
- The gcal ical_uid "…@hg4" matches the base; Feb 17, 2026 is a Tuesday.
- The base Task List sheet has the row "Send email to investors".

No hidden-record coherence problem: every record the answer needs is in Leonard's mailbox, his
Drive, channels he belongs to, or the unscoped services (Linear/Trello/Contacts). No injected
record sits after the clock.

## Known-issue cards touched

- NB-22 (letter 00016874, "January 31, 2025"). The DSN is threaded onto this exact letter. It is
  neutralised for grading: the notes doc says "Carta is the record, over any date in the letters",
  and the Carta notice (threads/leonard@harmonygames.co_1856960504234892536.json) gives
  [PERSON_NAME_0068] "as of Jan. 30, 2026 … Last day to exercise April 30, 2026". Watch only that
  the answer key never uses the letter date.
- NB-24 (Linear has no comments). The injected comments are the only Linear comments, which is
  fine because they are task-owned.
- NB-1 / NB-6 (Slack access after Feb 11 / export end Feb 13 10:03Z). Not triggered: the authors
  never left C0ADGSZKR3R, and the latest injected ts is 02:23:57Z.
- NB-29 (shutdown decision date). The Akin mail says "we let the team know yesterday" (Feb 11),
  which does not set any graded window.
- NB-12 (token vendor names). Sunset is "[USERNAME_26907]" in Slack but spelled out in the
  injected and base Gmail, so the answer can use Gmail.

## Notes for other passes (outside P2, not scored here)

- P1: [PERSON_NAME_11362]/Husnu Matthew Collins holds SSP-10 (25,432 seed) plus ES-9 (61,038
  advisor options) with no Carta termination notice. The injected contact says he "left the board
  May 2025", so whether ES-9 is still outstanding at Dec 31, 2025 (KPMG item 2) rests on "Carta is
  the record". The same "Carta is silent" question covers the option lines of [PERSON_NAME_0089]
  (30,518), PERSON_1287 (6,104) and PERSON_3941 (6,104, ES-11).

## Checked

- Prompt: 7 sentences.
- SQL: 145 statements (every INSERT/UPDATE), all 10 schemas.
- Last-mail re-derivation: 25 addresses, 25 of 25 match. Victor matches "Jul 11, 2025"
  (2025-07-11T19:06Z). Marcus matches "Dec 29, 2025" (2025-12-29T18:30Z,
  threads/leonard@harmonygames.co_1852868408136317821.json).
- No base DSN exists in Leonard's mailbox for 2025-26 (threads/leonard@harmonygames.co_185*,
  subject search, complete scan).

Effect on verdict (this pass): none. Scoring per brief: 0 State/Lifecycle items, 0 scored
low-impact items → no P2 fail; if the main session promotes A3 alone it is one minor
inconsistency (NON-FAIL), and A1/A2/A4/A5 do not touch graded values.

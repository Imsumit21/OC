# Cross-Service Coherence audit (rev2), cold pass

Universe: normal. Clock: 2026-02-14 00:00 UTC. The company shut down Feb 11; Leonard, Robert and Arthur are on America/Los_Angeles (slack users.json).
Scope read: inputs/ (SQL 130 INSERT + 15 UPDATE, header count verified; prompt; assignment), delta_rev1_rev2.diff, base through `hg.py search` (gmail Leonard/Robert/Arthur mailboxes, slack, linear, trello, gdrive, gsheets, gcal, contacts, snowflake), known_data_issues/normal.md. SQL was not executed.

## Delta rev1 -> rev2 (checked first)
| Change | Result |
|---|---|
| Notes doc: "sent to them directly **and delivered**"; NORMAL_TEXT run end 2032->2046 | OK. The body is now 2046 chars (+14) |
| Jan 14 #executives reply (846a70ba) rewritten as "a couple of shares off ... go by the ledger" and threaded under 6a3713ea; parent UPDATE rc=1/ruc=1/latest | OK. The base parent had rc=0 and thread_ts null. The ts matches created_at. The explicit 3,051,879 / 305,186 figures were dropped, so nothing contradicts the base (disclosure schedule 3,051,879 vs sheet 3,051,882 vs chatgpt 3,051,881) |
| KPMG 2nd reply: item 1 dropped, "Two clarifications"; size 1460->1326; thread snippet | OK. The size is body+900, the same as the other rows. The snippet is the body prefix |
| NEW DSN in thread 1856860994291529096 (bounce of Leonard's Feb 11 termination letter to PERSON_3140) | OK. In-Reply-To/References = base Message-ID <CAPBs_a5HKTOGV3...>. The letter was sent 20:13:48 and the DSN arrived 9 s later. The Message-ID hex 698ce305 = 20:13:57. Labels and the "(PST)" Date form match base DSNs (e.g. 68b075db...GMR). No later mail from or to that address in the Leonard, Robert or Arthur mailboxes |
| NEW Calvin Carta forward (thread 1856121753612004097) | OK. It matches base Carta "Termination details for Calvin Price" (Oct 29, 2025): ES-3, 8,138 granted, 4,408 vested, grant Nov 10 2023, terminated Oct 24 2025, last day Jan 24 2026 = "previously". SVC_0077 sender and template match. Jan 23 2026 was a Friday. Thread id >>20 = +0.5 s |
| NEW Leonard -> "Akin <PERSON_8862_EMAIL>" (thread 1856961760270377901) | OK. Akin = Matthew Collins in base ("best akin" Oct 28 2025; "Yes sounds good Akin" May 1 2025). "We told the team yesterday" fits the base #general <!here> of Feb 11 19:59. Thread id >>20 = +0.3 s. Labels SENT+Opened |

## Findings by category
### Temporal
- All Gmail thread ids >>20 are within 0.3–2.1 s of the first message (KPMG, Sunset, Calvin, Akin). The internal_date ms values equal the ISO dates. Quoted attributions are in PT ("8:48 AM", "10:06 AM", "2:14 PM", "Aug 11, 2023 at 1:00 PM") and match base senders' local time.
- Slack ts values equal created_at. Replies come after their parents. Everything falls before the NB-6 cutoff (Feb 13 10:03).
- Trello ids 698e5a10 / 698f6a03 decode to the action dates.
- Gcal Feb 17 is a Tuesday ("by Tuesday").
- The ordering holds: Slack 23:15 -> folder 23:20 -> Linear 23:24–00:03 -> doc 01:05 -> gcal 01:12 -> thread 02:21. Project and Trello updates come after the Sunset mail (18:06) and the KPMG mail (16:48).
- Advisory (not counted): the sheet and slides (Feb 10) sit in a folder created Feb 12. Base rate: 25,679 of 52,623 base files predate their parent folder, so this is normal in this universe.
### Semantic
- Board: base Nov 2023 directors are the Griffin partner, Matthew Collins, Robert and Leonard. Collins resigned May 1, 2025 (thread 1830959847543474636), which matches the contact UPDATE (updated 2025-05-02). The partner resigned Feb 12. So Robert's "Leonard and me on the board" is consistent.
- The Task List has a "Send email to investors" row. The #winddown Feb 9 base has "reach out to investors one by one", the "archive google after Feb 15 … until the data is extracted" line, and "linear we keep during transition". The base #winddown list (e3e198cc) supports "the angels are what's open". All consistent.
- No prior Griffin dissolution vote exists in the base.
### Cross-service referential
- The 26 "Nov 2024 owner list" comments match the (updated) LNI list.
- 24 of the 25 "Last mail with that address before Feb" comments match the latest header (to/from/cc/bcc) mail in Leonard's mailbox, in PT. Griffin's is Jan 24 16:40 PT (Jan 25 UTC).
- **L1 (low impact):** ENG-2453 Claire Morgan says "No mail with that address before Feb". Base `threads/leonard@…_1764717974138707720` (May 1, 2023) is a Google share request with `Reply-To: claire <PERSON_2360_EMAIL>`, and its body reads "PERSON_2360_EMAIL requests access". **Fix:** change the comment to "Last mail with that address before Feb: May 1, 2023", or reword it to "No mail to or from that address before Feb".
- Robert's mailbox threads (00016903, 00001367) and Arthur's (blake@…_1856959418725253571) exist. The LNI owner-list edit (removing the "(Total ownership percentage adds to 100%)" line) is applied in both copies and is not quoted anywhere else.
### Quantitative
- The owner list sums to 9,477,719 shares / 94.129%, which matches the sheet note "about 94%".
- The sheet rows equal the list. The Calvin figures equal Carta. The header counts are correct.
### State / lifecycle
- None found. Every actor is active at their timestamp (Calvin writes from a personal address after termination). The Trello board/list are open. Linear team_ENG is kept, with all 3 founders as members. ENG-2438..2463 follow the base max of ENG-2437. Trello idShort 456 follows the max of 455.
### Identifier / format
- These match base shapes: Message-IDs (LV3PR19MB8524 KPMG tenant, CAPBs_ Leonard, CAGkro_ Robert, Superhuman, GMR DSN), labels (Label_b19fb8d1b3 = "Opened"; Robert SENT only), [PERSON_NAME_0112] = PERSON_3941's first name, Robert's "[PERSON_NAME_0054]" sign-off, and EMPLOYEE_0025 = Arthur.
- There are no id collisions (gdrive and Slack id lookups, Trello, Linear, contacts).
- Cosmetic, not counted:
  - Injected Leonard/Robert sent mail uses `+0000` Date headers, where the base uses `-0800`.
  - The Superhuman id prefix `mlkq74xd` decodes to 10:09 UTC, while the mail was sent at 18:06.
### Other
- Base token collision (not overlay): PERSON_3083_NAME is used for Arthur Blake's sign-off, for the surname of holder ENG-2441, and for a Solsten contact.

## Known-data-issue cards touched
- NB-22: the DSN joins this letter's thread. Robert's copy is file 00016874. The letter says Jan 31 2025, Carta says Jan 30 2026, and the notes doc's "Carta is the record" neutralises the difference.
- NB-24: Linear comments are injected where the base has none.
- NB-1: posts are by Leonard and Arthur only.
- NB-6: everything is before the cutoff.
- NB-12: the doc says "Sunset" where the base #winddown masks it as [USERNAME_26907]. Low risk.
- NB-29: the "team told Feb 11" line matches the base.

## Verdict
No state/lifecycle items, and one low-impact item (L1). Result: **NON-FAIL**.

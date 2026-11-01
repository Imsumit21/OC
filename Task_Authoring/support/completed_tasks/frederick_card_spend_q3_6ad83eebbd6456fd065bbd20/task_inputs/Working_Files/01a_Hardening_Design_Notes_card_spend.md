# Card-spend hardening — design notes (SUPERSEDED 2026-10-23: implemented, see 01a_Hardening_Report.md)

Not the 01a report. The SQL is unchanged (cf06db49ab71); 01a_Hardening_Report.md on disk is the old paid-UA report.

## Baseline facts (local scoring of the 6 runs against the draft 09_Rubrics.json, full write payloads)
- Runs 1–5: 123/128 = 96.1% (fail only criterion 24, recipients). Run 6: 118/128 = 92.2% (24 and 32, Sensor Tower). Average 95.4%.
- 10_Baseline_Verifier_Results.md and 12_Difficulty_Stats.txt are empty or missing, so these are local numbers, not platform numbers.
- Every run replied with gmail_reply_to_message reply_all:false and never read any Slack DM (D05S58U4SAK). No run used Calendar, Confluence or Contacts.
- Slack reads were only the #executives cut-list thread. Run 6 read it after writing the card, which caused its Sensor Tower error.
- Every run scripted all 496 sheets; every number is exact. Feed-number traps will leak, because the tie-out to the ledger self-checks.

## Candidate mechanisms (each changes values the deliverables already carry)
| # | Mechanism | Records to change | Value change | Est. miss |
|---|---|---|---|---|
| A | Robert in the DM (existing) | — | — | ~100% |
| B | Heroic downgrade unconfirmed: ENG-2370 comment cmt_a37dfbf75e0965ec75d6 (L3315) reworded to "requested, $420 if they approve"; Heroic vendor card comment "downgrade requested"; cut-list item Heroic set to incomplete | L3315, Heroic card comment, #481 checklist | Heroic run-rate 600.00, not 420.00; ENG-2370 Heroic still at 600 | ~40–50% |
| C | 1Password 3 seats: new Leonard comment Sep 29 on the 1Password vendor card 678167bdc481ee214e69886d (L3181) ("3 seats, not 4 — QA vault seat goes too; $23.97 from the Oct bill"), later than Arthur's Sep 25 #481 comment | new trello_actions commentCard | 1Password 23.97, not 31.96 | ~45% |
| E | Griffin conference passes: a line added to the forwarded note (L3040), "I'll confirm where conference passes go before the Q3 submission", plus a new Sep 30 Griffin email in Frederick's mailbox moving GDC passes to Marketing (non-UA) | L3037–3040 + new gmail thread/message | Informa GDC (2,398.00 on Feb 5, −399.00 refund on Mar 4) moves Travel → Marketing; totals and month cells change | ~60–70% |
| D | REJECTED: AppMagic charge on the Sep 29 sheet. Rules 6 and 8 put Sep 29 outside the window, so it is unfair | — | — | — |
| D2 | Option: relabel an existing in-window Sep 26–28 row as a charge after a cancellation (no ledger impact). The Sep 27 and 28 sheets are "no postings", so a new row needs an offset; still open | — | — | — |

Run-rate total after B + C: 3,334.78 − 420.00 + 600.00 − 31.96 + 23.97 = 3,506.79.

## Honest prediction
Even with A, B, C and E landing at the rates above, about 100 of the ~145 rubric weight sits on mechanical rows Opus aces. Predicted average ≈ 80–84%. Below 80% probably needs 2–3 more independent mechanisms of the B/C/E kind, with multi-source rows at weight 5. Gate 4 forbids cutting rubric samples to move the number.

## Remaining steps
1. Grounding checks: Griffin's address and thread (L3037–3040); the Heroic vendor card comment line; the #481 Heroic checklist item; Leonard's Trello member id PERSON_6094.
2. Write the SQL edits (backup first to pre_hardening/), then run sql_lint.py and base_check.py.
3. Write the 01a report (MODE B, register with run · event citations) and run stage_gate hardening.
4. Re-run /injection, then /prompt; update the OEs (OE 13, 20, 21, 34, 2, 12, 30, 35) and the rubric values; run new baselines.

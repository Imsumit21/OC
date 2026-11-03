# Rev9 notes for Oracle Events, rubric and the next platform runs

Rev9 is bound to SQL `a34c7de38601`; the prompt `b5ea6f0ff28c` is unchanged since rev7. The truth is solver/truth.json, sha256 f3dd0b9de6e2d3f8. Everything in `run_forensics/rev8/platform/downstream_notes.md` still applies to the sheet and the reply; the values there are unchanged. Rev9 adds the Trello work below.

## Why rev9 exists (rev8 baseline)
- Counted calls per run were 82, 60, 70, 72, 69 and 83, an average of 72.7. Long Horizon needs 100 or more, and a 100% rollout's own count is the one used.
- The estimated pass rate was about 82%: four runs put SciPlay In talks, and run 4 also had Anton at $40K. Runs 3 and 5 scored 100%.
- Rev9 adds 50 single-object Trello writes asked for by Leonard's Sep 29 card comment (68db03b86054eff7e8e92474). The projected count is about 110-135 counted calls per run.

## Trello truth
- **Checklists**: card 68c5a49e8491a9d7faf869d0 (Existing Investor Update) gets four checklists, one per group, with one item per firm or angel (26 items):
  - Keep warm: London Venture Partners, Hiro Capital, Sciplay.
  - New investor: Anton Bernstein.
  - In talks: the 8.
  - Awaiting reply: the 14.
  - The card has no checklists in the base, so Keep warm is created too.
- **Follow-up cards**: 19 cards in To Do (640643a3fd8f3ca308d93195): Paul Heydon, GFR Fund, Andreessen Horowitz, T-accelerate, Homa, Brightwater Games Fund, Initial Capital, BITKRAFT Ventures, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital.
- **NCsoft**: a comment on Leonard's open To Do card 68c99e98737744bd966aed24 ("F/up with Anel after the engine deep dive") and no new NCsoft card. Anel Ceman is NCsoft's Partner on the 2025 list (row 79). This is trap DUP.
- **No card**:
  - Dentsu Ventures: base meeting evt_3671b9a924ccba550e51fa on Wed Oct 1.
  - Makers Fund: seeded call evt_6b2e94d0c17a3f58e9d2b1 "Michael Cheung and Leonard Hayes" on Wed Oct 8. Michael Cheung is Makers' Partner on list row 34.
  - This is trap BOOKED. Both stay in their groups: Dentsu In talks, Makers Awaiting reply.
- **Settled non-exceptions**: GFR's Sep 30 10:30am PT call is not after Sep 30, so GFR gets a card. Brightwater's "second meeting next week" is not on the calendar, so it gets a card. Homa's base card in Doing is not in To Do, so Homa gets a card.

## Rubric guidance (from the blind check)
1. Grade card names as "F/up with" (or a clear follow-up wording) plus the firm or angel. Accept short forms such as a16z, LVP, T-Accelerate, SciPlay and HOMA. Never require an exact string.
2. Leave checklist titles (any close variant of the group name), item wording, the NCsoft comment's text and due dates ungraded beyond presence.
3. Grade the follow-up set as one positive criterion that a do-nothing run fails: exactly these 19 cards, a comment on the Anel card, and no card for NCsoft, Dentsu Ventures or Makers Fund.
4. Keep a separate criterion for each checklist's membership, so a SciPlay or Hiro miss shows on the checklists as well as on the sheet.
5. Expected failure patterns:
   - CORR: SciPlay In talks, plus its checklist placement and an extra card.
   - DUP: a new NCsoft card.
   - BOOKED: cards for Dentsu or Makers.
   - INPUT: Anton at $40K.

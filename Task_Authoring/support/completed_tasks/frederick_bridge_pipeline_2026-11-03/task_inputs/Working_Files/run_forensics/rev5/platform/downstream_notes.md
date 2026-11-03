# Rev5 platform PASS: notes for Oracle Events and rubric

Bound to SQL `3ba2b413458f` and prompt `cecfad824fd8`. The platform passed `/injection` (injection_report5) and `/prompt` (prompt_report3) on 2026-11-02.

## Rubric and Oracle Event notes (from prompt_report3, Recommended Improvements and DR1/DR2)
1. **Reply:** accept a plain reply or a reply-all on Leonard's "Oct 14 board pre-read - fundraising section" thread. Robert and Arthur are cc'd and no record picks either (F37).
2. **Build access:** grade it only for firms in talks. For firms not in talks, blank, "none" and "n/a" are all acceptable, so don't grade those cells (F38). Angels are left blank.
3. **Firm count:** count distinct names (77 list names + Brightwater Games Fund + Homa = 79). Don't count by the list's "No." column, which skips 56–64 and runs to 89.
4. **Mattel:** keep criteria and Oracle Events off Tim Steudler's identity (known base issue SC-24). Mattel's row is decided by the bridge-outreach rule only.

## The platform's derived answers (they match solver truth.json 33d88dacdb04ab89)
- Passed (8): Play Ventures, March Gaming Fund, [PERSON_NAME_5402], Grishin Robotics, Lakestar Ventures, London Venture Partners, Hiro Capital, Sciplay.
- In talks (9): Andreessen Horowitz, NCsoft, T-accelerate, Dentsu Ventures, GFR Fund, Homa, Brightwater Games Fund, Anton Bernstein, Paul Heydon.
- Awaiting reply (14), including Initial Capital and Treo VC. Not contacted this round: the remaining 48 rows.
- Build access: T-accelerate iOS and Android; Dentsu iOS only; the other firms in talks none; angels blank.
- Money: committed $25,000 (Anton), soft-circled $50,000 (Paul).
- Keep warm checklist on card 455: London Venture Partners, Hiro Capital, Sciplay.
- Sheet "Fundraising - Oct 14 board" in folder `d_5e8a1c3f9b07d2e64a1b93`. Reply: 79 firms, $25,000, $50,000.

## Eval 0 advisory (not acted on)
The four columns missing from the schema snapshot are `slides_pages.notes`, `slides_page_elements.table_json` and `.ordinal`, and `linear_comments.sequence`. They are left in on purpose: completed_tasks/frederick_card_spend_q3 and julia_zm_difficulty_baseline used the same columns and their baselines loaded.

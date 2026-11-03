# Rev8 platform PASS: notes for Oracle Events, rubric and the Opus pre-check

Bound to SQL `4895577edea8` (rev8) and prompt `b5ea6f0ff28c`. The platform passed `/injection` (injection_report8) and `/prompt` (prompt_report6, score 5) on 2026-11-02. Every content dimension scored 5. Dataset similarity was 0.762 ("same scenario", under the 0.80 duplicate line). The deep recheck found 26 forks and none open.

## Answers (solver truth 7387d2e47df27b1c; they match the platform's derived outcome)
- **Send list**: one Google Sheet (a Google Doc is also accepted) named "Q4 update - send list", in folder `d_5e8a1c3f9b07d2e64a1b93` ("Q4 2025 investor update"). It has 26 rows: firm, group, amount, build access.
  - **New investor (1)**: Anton Bernstein, $25,000. Leonard's DM D05S58U4SAK/1758731100.281734 and D05S58U4SAK/1758914100.640218, plus the DocuSign Completed notice of Sep 26.
  - **In talks (8)**:
    - Paul Heydon, $50,000, unsigned; build access blank.
    - GFR Fund, Andreessen Horowitz, NCsoft, Homa and Brightwater Games Fund; build access none.
    - Dentsu Ventures and T-accelerate; build access iOS only (Arthur's post C0880U9751A/1759274400.518306).
  - **Awaiting reply (14)**: Initial Capital, BITKRAFT Ventures, Makers Fund, Raine Ventures, General Catalyst, BBQ Capital, Treo VC, Superplay, Sony Mobile, Revo Capital, e2vc, Triptyq, Turkven, Harlem Capital.
  - **Keep warm (3)**: London Venture Partners, Hiro Capital, Sciplay.
  - **Off the list**: the 5 email-only passes (Play Ventures, March Gaming Fund, Grishin Robotics, Lakestar Ventures, [PERSON_NAME_5402]) and the 48 firms not contacted.
- **Trello**: a "Keep warm" checklist on card 68c5a49e8491a9d7faf869d0, with London Venture Partners, Hiro Capital and Sciplay.
- **Reply** on Leonard's thread "Q4 investor update - send list": New investor 1, In talks 8, Awaiting reply 14, Keep warm 3.

## Rubric and OE notes (prompt_report6, Recommended Improvements 1)
1. Accept a Google Sheet or a Google Doc named "Q4 update - send list" (the README allows both).
2. Accept a reply or a reply-all on Leonard's thread (Robert and Arthur are cc'd).
3. Accept the counts per group either as one number per group or split into firms and angels (In talks: 7 firms + 1 angel).
4. Don't grade build access for anyone outside In talks, or for Paul.
5. Keep rows off row 82's firm label "Superplay" vs "Supercell" (SC-34) and off the list's repeated names: count Acterra, BITKRAFT and Progression once (SC-33).
6. For Homa, accept the name as the records show it ("[PERSON_NAME_0854]" in mail, "HOMA" in Fred's Slack).
7. If a row ever needs LVP's meeting date, use Sep 9 (fixed by rev8 SQL line 31).

## Hardness advisory (prompt_report6, Recommended Improvements 3)
The reviewer notes that the send-list doc spells out the base-data edge rules: the speedrun decision, the advisor's read, the Griffin no, and calls not on Fred's calendar. These rules settle forks for /prompt and do not point at the planted corrections. The corrections meant to catch Opus sit where the rev5 Opus run never looked:
- **INPUT**: Anton's amount, in Leonard's DM.
- **CORR**: SciPlay's pass, in Robert's reply in an #executives thread.
- **DONE2**: the Android access gap, in Arthur's #zombie-match3d post.

DONE1, ALIAS, FILT and FOLLOW all leaked in rev5 and remain as coverage. One pre-check run is one sample.

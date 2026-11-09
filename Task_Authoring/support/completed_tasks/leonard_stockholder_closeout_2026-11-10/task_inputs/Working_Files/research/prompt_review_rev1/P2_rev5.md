# Deep Recheck P2: SQL revision 5 delta

SQL: inputs_rev5/01_Universe_Inject.sql, sha256 ee52cd4c2582f906ddf7009c8e3c4cad93897fbefcc48b3f7fb8c64bab580b66.
Diff against rev3: two rows changed, the notes doc (line 19) and ENG-2448 (line 182). The notes body is 2234 characters, matching its style-run end of 2234. ENG-2448's timestamps are unchanged.

## DR6: closed

- ENG-2448's description is now "Email: PERSON_5275_EMAIL" plus "Legal notices: [EMAIL_15398]". This matches TOR's own designation and the side letter:
  - TOR's mail of 14 Jun 2023 (leonard.hayes@…/<CAMx_T-qLCuT+xT8prz_+yQyvLXa4MDkOGau7FH=8pc63aHtV=Q@mail.gmail.com>): "For legal notices: [EMAIL_15398]".
  - The side letter (gdocs /238 and /474, owned by Leonard): "Attn: [EMAIL_15398]".
- The notes now read "Notice route: the legal-notice address on their issue where it gives one, otherwise their email." That routes TOR to [EMAIL_15398].
- ENG-2448 is the only issue that carries a legal-notice address.
- Griffin's notice address in the IRA Schedule A (gdocs /525) is PERSON_4337_EMAIL, which equals its issue email.

## The two sentences

**1. "Griffin's partner gets a heads-up as a reply to all on their own Board position mail from Feb 12, asking for their vote as preferred holders on the dissolution."** No issue.
- The target exists in Leonard's mailbox: PERSON_4337's "Board position" (<BYAPR02MB435880CCF501BE0AE906AFFDC460A@…>, 2026-02-12 22:05:07Z, to Leonard, cc PERSON_2847), in thread leonard.hayes/1856958794180374704.
- Reply-all from it goes to PERSON_4337 with PERSON_2847 in cc.
- The preferred-vote ask stays consistent: Griffin holds 2,746,693 of 3,051,879 Series Seed (90.0%), and the #executives post 2524e876 says Preferred approval is needed for "M&A / liquidation".

**2. "… The only extra is for Tor and Segerstrale, who are both on Tor's side letter: a copy to Tor's lawyers."** This opens DR7.
- The phrase "only extra" says there are no other notice terms. Base says otherwise. This wording has been present since rev2 ("The only extra is Tor's side letter"); I missed it in the earlier rounds.
- Segerstrale's own address raises nothing. No record gives Segerstrale a legal-notice address, so the rule gives him PERSON_3336 plus the copy to Tor's lawyers.
- His signature on the final side letter is supported by the DocuSign notice "[PERSON_NAME_0089] Segerstråle viewed Complete with docusign: … Side Letter TLAS(final)" (…_1777587623652753593).
- The final side letter is not readable. The draft names only TOR as "the Investor". Whether its notice terms cover Segerstrale's own line is therefore left to Leonard's statement; nothing contradicts it. This is a possible P1 question, not a coherence defect.

## DR7 | P2 | §3.2 Cross-record / Semantic | FAIL

- **Prompt sentence:** "my close-out notes doc has how each holder gets handled". This feeds Sunset's ask, "How each holder gets formal notice, including any special terms".
- **Injected side:** the notes say "The only extra is for Tor and Segerstrale … a copy to Tor's lawyers".
- **Base side:** the Financing Documents (Leonard's copies) each require a copy to Griffin's counsel, Orrick, Herrington & Sutcliffe, when notice goes to the investors:
  - IRA (gdocs /525) §6.5: "if notice is given to Stockholders, a copy (which copy shall not constitute notice) shall also be given to Orrick, Herrington & Sutcliffe, 405 [LOCATION_0652], San Francisco".
  - Voting Agreement (/207) §7.7: the same Orrick copy, "Attn: [PERSON_NAME_0505]".
  - ROFR (/57) §6.5: "if notice is given to the Investors, a copy … shall also be given to Orrick, Herrington & Sutcliffe, 405 Howard Street".
  - SPA (/381) §6.6: the same Orrick copy.
  - IRA Schedule A lists GRIFFIN GAMING PARTNERS II, L.P. and GRIFFIN GAMING PARTNERS II Side Fund, L.P., both at PERSON_4337_EMAIL, plus one blank placeholder row.
  - Orrick is Griffin's counsel in the Jul 2023 "Revised SPA and Certificate" thread (…_1771880236343640719, orrick.com sender).
- **Effect:** the injected note denies a notice term that four documents Leonard can read state. It changes the special-terms value for at least the two Griffin funds, so it is not low-impact. It is also a UGT fork for P1.
- **Smallest fix (verifiable against Schedule A):** replace the sentence with: "Notice route: the legal-notice address on their issue where it gives one, otherwise their email. Two extras: for Griffin's two funds, a copy to Orrick, Herrington & Sutcliffe, as our investor agreements require; for Tor and Segerstrale, who are both on Tor's side letter, a copy to Tor's lawyers."
  - Caveat: these agreements cover whoever is party to them. If the angels signed on as additional purchasers (Leonard, 1 Aug 2023: "The paperwork for angel investors is finally ready"), the Orrick copy may reach them too. No record Leonard can read lists those parties.
  - Option A: the fix names only the Griffin funds; then the rubric should accept the Orrick copy on other investors' lines.
  - Option B: remove "only"/"two extras" and let the documents decide. P1 would then need to settle who is a party.

## Status

| DR | Status |
|---|---|
| DR1–DR4 | Closed |
| DR5 | Conditional (unchanged) |
| DR6 | **Closed** |
| DR7 | **New FAIL: the Orrick copy under the IRA, Voting Agreement, ROFR and SPA** |

Proposed scores: Cross-Service Coherence FAIL (DR7); Feasibility, Persona ACL, Data Exists and Tool Use PASS.

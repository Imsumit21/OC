# Blind fork sweep: DD publishing (Frederick Stone, clock Oct 1, 2025)

Seeded records came from `seeded_records.md` only. Base data came through `hg.py search` and `persona_view.py`. The seeded overlay cannot be searched, so "complete" below means complete over the base plus a full read of the seeded file. No answer key was opened. Process notes are at the end.

## Step 1. The solve on paper

**First pick: Copperleaf Games. 12-month value $67,200. Q4 cash $32,000 (net 30 from Nov 14 lands Dec 14). Banked so far $0. Keep value $12,723.96.**

Census: 26 publishers. **Live 7, Withdrawn 1, Out on rights 2, Passed 6, Waiting on us 3, No reply 7.**

Who's in: the 24 sheet rows (`f_fd467bd2ae0c6d4f3bd2bc`), plus Copperleaf Games (came to Robert) and Redwood Arcade (came to Arthur). Slack `EMPLOYEE_0016` is Robert and `EMPLOYEE_0025` is Arthur (users.json). Linear `usr_cc3e90160f490686` is Arthur.

### Live offers (gross = installs x 12 x $0.50; signature Nov 14)

| Publisher | Share | Advance | Installs/mo | Gross | Our share | 12-month | Advance lands | Q4 cash | Respond | Deciding records |
|---|---|---|---|---|---|---|---|---|---|---|
| Copperleaf Games | 28% | $32,000 | 40,000 | $240,000 | $67,200 | **$67,200** | Dec 14 | $32,000 | Oct 17 | Slack #executives reply `495d71a7` (Robert, Sep 26) |
| Redwood Arcade | 24% | $25,000 | 40,000 | $240,000 | $57,600 | $57,600 | Dec 29 | $25,000 | Oct 31 | Linear `lc_674982ff` on ENG-2362; pointer in #analytics `e6460689` |
| Sunfold Mobile | 30% | $20,000 | 30,000 | $180,000 | $54,000 | $54,000 | Dec 29 | $20,000 | Oct 31 | `f_8ddfb990`; Trello comment on `68d59838` (Sep 30, 50,000 to 30,000) |
| Tallwater Games | 25% | $40,000 | 30,000 | $180,000 | $45,000 | $45,000 | Dec 14 | $40,000 | Oct 17 | `f_e8cb875d`; notes on `evt_43fda04c` ($60,000 to $40,000) |
| Oakline Games | 30% | $30,000 | 20,000 | $120,000 | $36,000 | $36,000 | $10K next week, $20K Dec 14 | $30,000 | Oct 24 | `f_27cac0ee`; Marek Sep 29; #executives `0230b2df` (Arthur, Sep 30) |
| Harbor Lane Games | 20% | $25,000 | 25,000 | $150,000 | $30,000 | $30,000 | Jan 13, 2026 | $0 | Oct 24 | `f_d72e8b34`; `evt_d6905d9d` (no change) |
| Wavecrest Play | 22% | $15,000 | 15,000 | $90,000 | $19,800 | $19,800 | Jan 13, 2026 | $0 | Oct 31 | `f_a6a5647f`; `evt_48e63a8c` (no change) |

In all seven, our share beats the advance. Stale inputs would flip the order: Sunfold at 50,000 installs gives $90,000, Tallwater at $60,000 gives $60,000, Northglow would be $126,000, Pinegrove $81,000, Moonrail $54,600.

### Not Live

| Publisher | Status | Deciding record |
|---|---|---|
| Moonrail Studios | Withdrawn | `f_464839da`; #executives `e44da6a4` (Robert, Kestrel freeze, Sep 29); Anika's signature "a Kestrel Group studio"; contact `5373edb5` |
| Northglow Publishing | Out on rights | `f_3eccf6e0` (exclusive incl. PC and web) vs Leonard, #executives Aug 25 `8b9a4248` and Exec Sync doc `f_26e1f9a8`: "retain code, IP and non-mobile distribution rights" |
| Pinegrove Games | Out on rights | `f_5f3ef4a4` (source code and build pipeline pass) vs the same position |
| Fernhollow, Quietbay, Slatewood, Ironbridge, Tidewell, Marlin Play | Passed | "we'll pass" in threads ...912178 (May 13), ...894896 (May 15), ...167383 (Sep 17), ...812534 (Sep 19), ...727407 (Sep 29), ...060205 (Sep 30) |
| Appodeal | Waiting on us | Base thread `1830012626042968381`, last message theirs May 21, no share or advance; complete "Appodeal" scan shows nothing later |
| Rayking Game | Waiting on us | Sep 4 mail via Leonard's forward; Fred's "Hi ..." reply carries the Drafts label (`Label_f592e6a4db`), so it was never sent; DM `bda432db` "we still owe them an answer" |
| Kitebridge Games | Waiting on us | Thread ...167536: Ivo asked for D7 by country Sep 26, no reply from us |
| Orchard Lane, Silverlake, Cedarbrook, Foxglove, Riverstone, Bellwether | No reply | Sent-only threads |
| Summit Mobile | No reply | Auto-reply only, from noreply@ (thread ...746195) |

### Looked at and left out

- Homa, NCsoft, Tilting Point's form: named in the rules. Tilting Point's mail is a form acknowledgement, Sep 5.
- PERSON_5173 (Sep 17 to 26 thread): co-dev talk, the Sep 18 call that the Slack points to as Homa.
- PERSON_2173: investor.
- Tamatem: a name an employee passed along in June; no contact from them.
- Publishing Partners doc names (Tilting Point, Jam City, Huuuge, Lion/AppLovin, Peak): not approached, per the sheet's note row. No DD approach appears in the complete Gmail "Domino Delights" scan.
- QPLAZE: two generic pitches (May 8, Jun 21) to a shared inbox; never names DD, not to a founder, not reachable by Fred.
- Prodege, UAjam, the Apr 21 recruiter, ad and creative vendors: not publishers.

### Keep value

`ANALYTICS.MONETIZATION.REVENUE_DAILY`, `domino_delights`, sum of `total_revenue_usd`: Jul $2,078.33, Aug $721.55, Sep $381.11. Total $3,180.99, average $1,060.33, x 12 = **$12,723.96**. All 92 days present, no duplicate keys, iap + ad = total on every row. `REVENUE_DAILY_V2` gives the same figures.

### Writes implied (82 objects)

| Write | Count | Detail |
|---|---|---|
| Google Sheet | 1 | "DD publishing model" in folder `d_6fc54be6...`. Tab Publishers: 26 rows, figures on the 7 Live rows only. Tab Summary: 3 values |
| Contacts | 14 | Marek Sobol, Paola Duarte, Diego Reyes, Sofia Lindqvist, Callum Ross, Elena Petrova, Jonas Weber, Mei Tanaka, Rhys Morgan, Nadia Haddad, Yuki Sato, Tessa Hale, Omar Khalil, Greta Holm. Skip Lena Fischer and Anika Rao |
| Trello checklists | 6 | On card `68dab660`, one per status |
| Checklist items | 26 | 7 + 1 + 2 + 6 + 3 + 7 |
| New F/up cards | 15 | BD Follow Up list: Tallwater, Harbor Lane, Wavecrest, Copperleaf, Redwood, Appodeal, Rayking, Kitebridge, and the 7 No reply publishers |
| Card comments | 2 | "Live" on F/up with Marek (Oakline) and F/up with Lena (Sunfold) |
| Calendar reminders | 7 | Fred's calendar. Oct 17: Tallwater, Copperleaf. Oct 24: Oakline, Harbor Lane. Oct 31: Sunfold, Wavecrest, Redwood |
| Gmail drafts, nudges | 7 | partnerships@ for Orchard Lane, Summit (not noreply@), Silverlake, Cedarbrook, Foxglove, Riverstone, Bellwether |
| Gmail drafts, organic note | 3 | Paola, Diego, Sofia, each with $0.50 D30 ARPI (see F1, F3, F4) |
| Reply | 1 | Thread `frederick.stone@harmonygames.co/1844732284109533347`, to Leonard |

No Linear write, no edit to the Oct 6 event, no edit to the outreach sheet.

## Step 2. Forks

### Genuine forks (5)

None of the five moves the first pick, its 12-month value, its Q4 cash, or Banked.

**F1. Where the organic notes live (write surface).** Leonard, Sep 25: "one short note each as a draft and I'll read them first."
- Reading A: three Gmail drafts in Fred's mailbox.
- Reading B: text Leonard can actually open (Doc, Slack, or the reply), because he cannot see Fred's drafts.
- Changes: a check on Gmail drafts fails B, and a check anywhere else fails A. Neither the Slack note nor the card says new message or reply on the old thread, so no thread can be asserted for the 3 notes or the 7 nudges.
- Fix: "leave them in your Gmail drafts and tell me they're there", and do not grade threading.

**F2. "That guy from Sep 24 I said I'd chase."** The source is the DM, Sep 24 18:00Z: "There was a dude from [USERNAME_34104] looking for games" / "I'll reach out to him". The company token is scrubbed and appears once in Slack (Apr to Sep 2025). A Gmail search for "looking for games" and for hypercasual leads found nothing that identifies him either.
- Reading A: an off-sheet lead, so the line is a no-op and Kitebridge stays.
- Reading B: Ivo Novak, the only man with an open thread among the sheet's Sep 24 rows, so Kitebridge drops.
- Changes under B: Waiting on us 3 to 2, census 26 to 25, checklist items 26 to 25, new cards 15 to 14.
- I land on A: Leonard said he himself would chase, and Fred wrote Ivo at 20:25Z as his own tranche. But no record proves the dude is not at one of the six Sep 24 rows.
- Fix: name a company in the email, or add "he's not on your sheet".

**F3. "Still Live" predates the word.** Leonard's note is dated Sep 25 16:20Z, but the doc defining Live is dated Sep 29. At that minute only Harbor Lane among the one-pager recipients had sent terms (Wavecrest 16:30Z, Moonrail 17:00Z, Tallwater Sep 26).
- Reading A: the doc's status, so 3 notes.
- Reading B: the plain sense on Sep 25, still in play, which adds Orchard Lane and Summit Mobile (No reply, both got the one-pager). That makes 5 notes.
- I land on A, because the doc's last line carries the note forward and the capital L matches.
- Fix: reword to "anyone who got it and still has terms with us".

**F4. "Before we sit down with them" has already passed.** Fred's calendar shows all three calls after the note: Wavecrest Sep 25 18:00Z, Harbor Lane Sep 26 19:00Z, Tallwater Sep 29 18:30Z. No record shows the figure went out.
- Reading A: still owed, since the doc says it "still applies". 3 drafts.
- Reading B: the trigger has lapsed. 0 drafts, or a different kind of note.
- I land on A.
- Fix: "before we go any further with them".

**F5. Reminders: per offer or per date.** "One on Fred's calendar on each Live offer's response date." Seven offers share three dates.
- Reading A: 7 events.
- Reading B: 3 events, each naming its offers.
- I land on A.
- Fix: "one per Live offer, named for the publisher, on its response date".

### Settled, I'm confident

- **Who's in.** Copperleaf "emailed me out of the blue" is came-to-us, not a passed-along name. Redwood's deep-link question is not engine talk, and the pasted note is a publishing offer. Kestrel is Moonrail's parent, not a 27th publisher.
- **"Their note pasted in by one of us".** Admits Robert's Slack paste and Arthur's Linear paste: both carry a share and an advance, and both founders are "one of us". Leonard's calendar note and Fred's Trello comment are not "their note", and they don't need to be: the term sheets make those two Live, and "latest terms ... wherever they are" moves the numbers.
- **First that fits.** The four May "nothing right now" replies gave terms later, and Live sits above Passed. Rights offers stop above Live. Kitebridge fits only Waiting on us, because its reply is "they wrote to us" and is the last message.
- **Banked.** $0. Marek's mail and Fred's Trello comment say sent, Arthur says it never hit, and the doc defines Banked as in the SVB account. "That $10K first-look" names no publisher, but only Oakline has one.
- **Oakline Q4 $30,000.** This is the weakest settled call. The resend is a promise, but next week is October and the rule asks what lands in Q4. A cautious reader might show $20,000. It touches one sheet cell only.
- **Oakline Advance.** $30,000 total, per "the total advance".
- **Signing date.** Nov 14: ESG Law gives the date and Leonard confirms it. Net 60 falls to Jan 13, so Harbor Lane and Wavecrest are $0. Net 45 is Dec 29, still in Q4.
- **Reply wording.** "It" is the first pick, so $32,000, not a Q4 total across offers.
- **Already in Contacts.** Lena and Anika only: all 17 names, the publisher domains and company names return no base hits. Anika's job says Kestrel, not Moonrail, but "skip anyone who's already there" settles it.
- **Contacts scope.** Appodeal, Rayking, Kitebridge and the No reply rows gave neither terms nor a no. Withdrawn and rights-out people did give terms. Jonas and Mei count.
- **Cards.** The list's base cards (Netflix, SciPlay, Ares, Mattel) do not overlap. Marek maps to Oakline and Lena to Sunfold through the sheet. Withdrawn, Out on rights and Passed get no card.
- **Who gets what.** Moonrail gets no note or reminder. Northglow and Pinegrove get no reminder despite their respond dates. Copperleaf and Redwood get no note, since nothing was sent to them. Orchard Lane and Summit get a nudge only (subject to F3).
- **Linear.** ENG-2362 is read-only evidence; nothing asks for a write.
- **Keep value.** The table is named, and the months are complete.

## Step 3. Reach, gaps, contrivance

**Reach.** Every deciding record is reachable as Frederick.
- YES by `can-see`: #executives, #bridge-pitch, #analytics, DM `D05S58U4SAK`, Exec Sync doc, Publishing Partners doc, Appodeal and Rayking threads.
- Unscoped: Trello, Linear, Snowflake, Contacts.
- `can-see` returns UNVERIFIED for seeded Drive ids. I did not run `check-sql` because it needs the SQL file. By the seeded metadata, the rules doc and all 8 term sheets are shared with Fred, and the folder and sheet are his.
- The rules doc's parent folder is Leonard's and not visible to Fred (NO on `d_63fffeb4`), so he reaches the doc by the direct share only.
- Leonard's copy of the Rayking mail and the shared-inbox originals are NO, and not needed.

**Rule needs with no record.**
- The Sep 24 lead's company (F2).
- An exact resend date for the $10K; only "next week" exists.
- A recorded outcome for the August sync: the Aug 28 notes hold Leonard's agenda sentence, no decision. The doc adopts it, so nothing changes.
- What "respond by" means when every date precedes the Nov 14 signature. No value effect, but the Copperleaf and Tallwater respond dates fall four weeks before signing.
- What the first-look buys, and what happens to the $10K if Oakline is not picked. Per-offer columns keep this out of the numbers.

**Contrived, or unlike a real founder.**
- Fourteen outside people share templated text: 8 identical "shared our term sheet" replies, 6 identical pass lines, 4 identical "ping me then". All term sheets and both pasted notes are one sentence in the same clause order.
- A tech lead quoting rev share, advance and a respond date inside a deep-link email is the least believable record.
- Arthur leaves that offer on an engineering ticket and tells #analytics only "a publisher", with no name. A CTO at a company out of runway would tell the founders.
- Robert's $32,000 offer as "Off topic" in a retention rant is also forced. So are Arthur's SVB line on a three-week-old banker thread and Leonard's rule on an eight-day-old thread about Matthew.
- "Live" in the Sep 25 Slack is an anachronism (F3).
- "Hi Marek, following up from Harmony Games" is a first contact.
- "Notes: nothing changes on their side" twice reads as decoy filler.
- Leonard addressing Fred inside a reply to outside counsel is odd but passable.
- His "get serious about the DD publishing idea" sits badly with his own Sep 29 Tallwater call and eight term sheets in hand.
- Term sheets owned by outsiders sit in a folder shared only with Leonard.

## Process notes

- `hg.py records` was used once for ENG-2362 and the Linear user. It is not on the allowed list, so both were re-read through `hg.py search get` with the same result. `hg.py search inventory` and `hg.py reference routes/schema` were used for navigation only.
- `Evals/SEARCH.md` was read directly for tool usage.
- Temporary request and output files were written to a session scratchpad subfolder, outside the workspace, and deleted at the end.
- That scratchpad also held other sessions' files. They appeared in one directory listing and were not opened.

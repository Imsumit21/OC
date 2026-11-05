#!/usr/bin/env python3
"""Builds task_inputs/01_Universe_Inject.sql for frederick_q4_commitments (rev1).
Read-only on the base; writes only under Task_Authoring/task_inputs. Never executes SQL.
Shapes follow base records and the bridge task's accepted injection (row helpers adapted)."""
import base64, datetime as D, email.utils, hashlib, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TI = HERE.parents[1]
sys.path.insert(0, str(HERE))
import build_scenario as B  # noqa: E402

FRED, LEO, ART, ROB = ('frederick.stone@harmonygames.co', 'leonard.hayes@harmonygames.co',
                       'arthur.blake@harmonygames.co', 'robert@harmonygames.co')
NAMES = {FRED: 'Frederick Stone', LEO: 'Leonard Hayes', ART: 'Arthur Blake', ROB: 'Robert'}
LOWER = {FRED: 'frederick stone', LEO: 'leonard hayes', ART: 'arthur blake', ROB: 'robert'}
ROOT_FRED = 'd_175c0d7bc72ed244b944cb'
SLACK_U = {LEO: 'EMPLOYEE_0038_SLACK_ID', ART: 'EMPLOYEE_0025_SLACK_ID', ROB: 'EMPLOYEE_0016_SLACK_ID'}
TR_ART = '2162c1ba310341bf318f48b7'
HG_BOARD = {'id': '640643a3fd8f3ca308d9318e', 'name': 'Harmony Games', 'shortLink': 'f4LGcmuh'}
DOING = {'id': '640643a3fd8f3ca308d93196', 'name': 'Doing'}
LIN_ART = 'usr_cc3e90160f490686'
ESG_P = ('PERSON_2694_EMAIL', 'PERSON_2694_NAME')        # ESG Law partner (base engagement thread 1841636073974841484)
ESG_G = ('PERSON_2599_EMAIL', 'PERSON_2599_NAME')        # ESG Law group intake address (same thread)
I, T, Q = B.IDS, B.T, B.Q


def h(seed, n):
    return hashlib.sha256((B.SALT + seed).encode()).hexdigest()[:n]


def dt(iso):
    return D.datetime.fromisoformat(iso.replace('Z', '+00:00'))


def q(v):
    if v is None:
        return 'NULL'
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, (int, float)):
        return repr(v)
    s = str(v)
    if '\n' in s or '\\' in s or '\r' in s:
        return "E'" + s.replace('\\', '\\\\').replace("'", "''").replace('\r', '\\r').replace('\n', '\\n') + "'"
    return "'" + s.replace("'", "''") + "'"


def js(x):
    return json.dumps(x, ensure_ascii=False)


OUT, ROWS, IDS = {}, {}, {}


def ins(table, cols, vals, key):
    svc = table.split('.')[0]
    OUT.setdefault(svc, []).append(f"INSERT INTO {table} ({', '.join(cols)})\nVALUES ({', '.join(q(v) for v in vals)});")
    ROWS.setdefault(table, []).append(key)


def upd(table, sets, key_col, key):
    svc = table.split('.')[0]
    OUT.setdefault(svc, []).append(f"UPDATE {table} SET {', '.join(f'{k} = {q(v)}' for k, v in sets.items())} "
                                   f"WHERE {key_col} = {q(key)};")
    ROWS.setdefault(table + ' (UPDATE)', []).append(key)


def trello_id(at, seed):
    return f"{int(dt(at).timestamp()):08x}" + h(seed, 16)


def thread_num(at, seed):
    return str((int(dt(at).timestamp() * 1000) << 20) + (int(h(seed, 8), 16) & 0xFFFFF))


# ============================================================ people (seeded external tokens: PERSON_97NN, unused in base)
PEOPLE = {}
_n = 9701
for m in B.M:
    if m['person'] and not m['base'] and m['decision'] != 'out':
        PEOPLE[m['key']] = (f"PERSON_{_n}_EMAIL", f"{m['person'][0]} {m['person'][1]}")
        _n += 1
PEOPLE['Nova Rewards'] = (f"PERSON_{_n}_EMAIL", 'Ruth Calloway'); _n += 1
PAYLANE = ('SVC_9701_EMAIL', 'Paylane')                  # payments partner for UGC Studio (automated, unused SVC token)

# ============================================================ texts: authorities, hub, notes (planned wording; claims, no conclusions)
HUB_SUBJ = "Vendor and partner stuff while I'm in LA"
HUB_BODY = f"""Fred,

I'm in LA from tomorrow for Dentsu and the Griffin AGM, so can you take over the vendor and partner backlog this week? That's {Q['hub_scope']}: a call, a reply, a sign-up or paper. {Q['hub_cold']}, and so do the ad networks, PlayableX, Craftsman+ and Singular (they all stay on the UA budget call), the investors, and Mattel, which I'm keeping.

{Q['hub_guardrails']}, {Q['hub_amend']}. {Q['hub_esg']}.

{Q['hub_answer']}. {Q['hub_contacts']}.

Log it all in a sheet in the Q4 commitments folder, {Q['hub_readme']}. Then {Q['hub_report']}.

Thanks,
Leonard"""

# rev2 (platform /injection C-adv 1): the doc (Sep 26) predates the review event (Sep 29), so it announces the review
DOC_REVIEW = "comes back at the January commitments review I'll put on our calendars"
GUARD_TITLE = 'Runway guardrails - Q4 commitments'
GUARD_BODY = GUARD_TITLE + f"""
Leonard, Sep 26. Until we know where the raise lands, this is how we handle anything outside the investor work that wants money, a signature or an answer from us.
How to decide
Go top to bottom and stop at the first one that fits.
1. Already answered. If one of us has already given them an answer, don't write to them again. Note who answered and when. If the answer was "later", it {DOC_REVIEW} too.
2. Cash test. Anything that would cost us cash between Oct 1 and Dec 31 ends now: say no, or cancel it in writing the way their paper or notice asks. A trial or pilot that turns into a paid plan inside that window counts as cash, and so does an offer we would have to take up and pay for before January. Travel and event costs count only when we book them ourselves.
3. Keep. The cash test has one exception: {Q['doc_keep']}, even if it costs money. Tell them we're staying.
4. Sign. If it costs nothing before January but taking it means someone has to accept terms or sign for the company, it goes the way ESG's note says. Tell them it's with Leonard or Arthur to sign, and with our lawyers first when ESG has to see it.
5. Park. Everything else that's free until January, including offers we could still take up after that. Tell them we'll pick it up in January; it {DOC_REVIEW} (first week of January).
Answers
Everyone who is waiting to hear from us gets a written answer. Portals and no-reply notices don't need one."""

UA_TITLE = 'UA spend buckets (Q4)'
UA_BODY = UA_TITLE + """
Fred, Sep 16, after Monday's exec chat.
Fundraising bucket: incent spend that moves the D1/D7 numbers investors ask about. Adjoe for now. This is the only UA spend that runs until the raise.
Real UA bucket: Unity, Meta, playables. Budgets set week by week until we know about the raise; playables count here, not in the fundraising bucket.
Review the split at the exec sync every Monday."""

ESG_SUBJ = 'Signing and review for Harmony Games agreements'
ESG_BODY = f"""Hi Leonard,

Following up on our call today, here's how we'd like agreements handled from now on while you're raising:

- Only an officer, you or Arthur, accepts terms or signs for Harmony Games, whatever the amount. That includes click-through terms and portal NDAs.
- Anything with an automatic renewal, exclusivity, a licence of your IP or a term over 12 months comes to us before anyone signs. Send each one to {Q['esg_intake']}, one email per agreement, so we can open a matter for it.
- Mutual NDAs on our template don't need review, whatever their term. An officer can sign them.

Best,
PERSON_2694_NAME
PARTNER, ESG Law"""
ESG_ACK = f"""Agreed. This replaces what I said in July about Fred signing small stuff himself.

Fred, Arthur: anything waiting on Arthur or me to sign, put it on our founders' board To Do list with the company's name in the card title, including the ones that go to ESG. For the intake emails, {Q['esg_checklist']}.

Leonard"""

CHECK_TITLE = 'ESG Law - agreement intake checklist'
CHECK_BODY = CHECK_TITLE + """
From ESG's call with Leonard, Sep 24. One email per agreement to ESG Law intake.
Include
- the company and what the agreement is
- the term and any automatic renewal
- any exclusivity or licence of our IP
- what it costs us, if anything
- the date they need it by
- who would sign it (Leonard or Arthur)"""

README_TITLE = 'README - Q4 commitments'
README_BODY = README_TITLE + f"""
Leonard, Sep 30. One sheet for the vendor and partner backlog, one row per company on it. Name it "Q4 commitments log"; to start, {Q['readme_template']}.
Columns
Company · Contact · What's waiting · Decision · Answered by · What we told them · Next date
Decision is one of: Answered, End, Keep, Sign, Park (the guardrails doc says which).
Answered by: who on our side already answered them, for Answered rows.
Next date: for End, the last day to cancel or say no; for Park and for "later" answers, the January review; for Keep, when it next bills; for Sign, the date they need it by, if any.
Contacts
Put the company in the job field, and only add a person who isn't in Contacts already (portals and no-reply senders don't get one)."""

TRACKER_TITLE = 'Vendor & partner tracker'
TRACKER_GRID = [['Company', 'What', 'Status (Jul 31)', 'Notes'],
                ['Clipforge', 'UGC Studio pilot', 'pilot running', 'free through Jan 15 per the pilot agreement'],
                ['Pixel Harbor Events', 'booth, Bay Area Indie Showcase Oct 24', 'quote in', 'deposit due Oct 10 if we go'],
                ['Playtestcloud', 'player tests', 'running', 'Leonard owns'],
                ['Solsten', 'audience data', 'paused', 'paused in May'],
                ['Singular', 'attribution', 'renewal', 'Leonard asked them for quarterly billing on Jul 17']]

S_JULY = "fred for small stuff under $500 a year you can just accept the terms yourself, no need to wait for me"
S_ROBERT = "honestly we should just cancel every marketing tool we pay for, all of it, until we know about the raise"
S_AMEND = ("one change to the runway guardrails doc: travel and event costs count as cash even when a partner books them "
           "and bills us. it all comes out of the same bank account")
# rev4 (01a_Hardening_Report.md §10 M1/M2): the corrections name the company's contact, never the company or the rev3
# pre-check's search words ('told', 'vendor'); planned wording in build_scenario.Q
S_WAIVER = B.Q["framewell_waiver_v4"]
S_DM = B.Q["lanternfly_note_v4"]
LIN_TITLE = 'Switch: order dev kits'
LIN_DESC = ("Fred registered us on the Nintendo developer portal on Sep 4. Next step is ordering dev kits "
            "($400-500 per kit per the portal) so we can try a Zombie Match 3D port.")
LIN_CMT = ("Tried to order the kits today. The portal won't take an order yet: the Global ToS and NDA still needs our "
           "agreement approver to accept it, and that has to be a company officer from their own login. Fred is only set "
           "up as administrator, so the 'NDA Effective 09/04' on his registration mail is just the start date it will "
           "carry. It's Nintendo's standard click-through: no fee, no fixed term, no exclusivity, nothing about our IP, and either side "
           "can end it. It has to be accepted by Oct 15 or the request lapses. The kits can wait until after the raise; "
           "leaving the acceptance for Leonard or me.")
KEEP_NAME = "Keep-running list (don't cut)"
KEEP_DESC = "Stuff the live game needs to keep running. Ask me before cancelling any of it."
KEEP_ITEMS = ['Vaultline nightly DB backups', 'Certwell SSL cert for the API domain',
              'the night pager for backend outages (whatever wakes me up at 3am)', 'App Store and Google Play developer accounts']

# ============================================================ member threads and papers
# per member: subject, [(at, who, body)], paper (kind, title, body or slides, at)   who: 'V' rep, 'F' Frederick, other email
MT = {
 'Framewell': ("Framewell Pro for Harmony Games", [
   ('2025-09-18T16:00:00Z', 'V', "Hi Frederick,\n\nThanks for the call on Tuesday. As promised, the order form for Pro is attached: 4 seats, unlimited template and stock-clip downloads. Pro starts Nov 1 at $149/month, billed monthly, and you keep the free seat until then.\n\nCan you let me know by mid-October if we should set it up?\n\nBest,\nMaren")],
   ('gdocs', 'Framewell - Order Form - Harmony Games', "Framewell - Order Form - Harmony Games\nPlan: Pro, 4 seats\nPrice: $149/month, billed monthly\nBilling starts: Nov 1, 2025\nTerm: month to month, cancel any time before the next billing date\nIncludes: unlimited template and stock-clip downloads, brand kit, 2 TB storage\nFree seat: stays active until Nov 1", '2025-09-18T16:20:00Z')),
 'Pingwise': ("Your Pingwise Starter tier ends Oct 31", [
   ('2025-09-24T15:00:00Z', 'V', "Hi Frederick,\n\nHeads-up that the free Starter tier on your account ends on Oct 31. From Nov 1 the account moves to Team ($29/month) under your existing agreement, so phone and SMS paging keep working for your on-call rota. If you'd rather drop back to the free plan, reply and I'll downgrade you before then. Free has email alerts only, no paging.\n\nCan you confirm either way?\n\nDana Whitfield\nCustomer Success, Pingwise")],
   ('gdocs', 'Pingwise - Team plan terms', "Pingwise - Team plan terms\nService: uptime monitoring and on-call alerting for your API and backend endpoints (1-minute checks, phone and SMS paging)\nPrice: $29/month from Nov 1, 2025, billed monthly\nContinues under your existing agreement unless you downgrade; nothing new to sign\nDowngrade: reply to your account manager before Oct 31", '2025-09-24T15:30:00Z')),
 'Clipforge': ("Clipforge UGC Studio pilot - welcome", [
   ('2025-07-08T18:00:00Z', 'V', "Hi Frederick,\n\nWelcome aboard! Your UGC Studio pilot workspace is set up (HG-2291) and the pilot agreement is attached. Looking forward to the kickoff on Monday the 14th, bring a couple of briefs if you have them.\n\nPriya"),
   ('2025-09-22T17:30:00Z', 'V', "Hi Frederick,\n\nHope the pilot videos are working out. Want me to line up the next brief? If you're not carrying on after the pilot, let me know here too so I can plan the team's time.\n\nPriya")],
   ('gdocs', 'Clipforge - Pilot Agreement - Harmony Games', "Clipforge - Pilot Agreement - Harmony Games\nProduct: UGC Studio (creator video ads)\nWorkspace: HG-2291\nPilot: no charge through Jan 15, 2026, up to 20 delivered videos\nIf the 20-video cap is reached early, the pilot ends at the end of that cycle and the Studio plan starts the next day\nStudio plan after the pilot: $1,800/month, billed by our payments partner\nCancel in writing to the billing address on your notice before the Studio plan starts", '2025-07-08T18:30:00Z')),
 'Pixel Harbor Events': ("Booth hold - Bay Area Indie Showcase, Oct 24", [
   ('2025-06-18T17:30:00Z', 'V', "Hi Frederick,\n\nGreat to meet you at the mixer. As discussed, I'm holding a 10x10 booth for Harmony Games at the Bay Area Indie Showcase on Oct 24. Quote attached: $4,800, with a $2,400 deposit due by Oct 10 to keep the hold. Just say the word and I'll send the invoice.\n\nTeodor"),
   ('2025-06-19T16:10:00Z', 'F', "Thanks Teodor, I'll come back to you on this.\n\nFrederick")],
   ('gdocs', 'Pixel Harbor Events - Booth Quote - Harmony Games', "Pixel Harbor Events - Booth Quote - Harmony Games\nEvent: Bay Area Indie Showcase, Oct 24, 2025\nBooth: 10x10 standard, two exhibitor passes\nPrice: $4,800; deposit $2,400 due by Oct 10, 2025 to hold the booth; balance by Oct 20\nCancellation: free before the deposit is paid", '2025-06-18T17:45:00Z')),
 'Lanternfly Publishing': ("Lanternfly x Harmony Games: Southeast Asia publishing", [
   ('2025-09-09T15:30:00Z', 'V', "Hi Frederick,\n\nThanks for taking my call last week. I've sent over our proposal deck for publishing Domino Delights in Southeast Asia: we handle localization, store featuring and UA in the region on a revenue share, no upfront fee. Happy to walk your team through it.\n\nWen Halvorsen\nPartnerships, Lanternfly Publishing"),
   ('2025-09-10T17:05:00Z', 'F', "Thanks Wen, we'll take a look and get back to you.\n\nFrederick"),
   ('2025-09-22T08:40:00Z', 'V', "Hi Frederick,\n\nAny news on the proposal? We're planning our Q4 slate and would love to include Domino Delights.\n\nWen Halvorsen\nLanternfly Publishing")],
   ('gslides', 'Lanternfly Publishing - Southeast Asia publishing proposal', [("Lanternfly Publishing x Harmony Games", "Publishing Domino Delights in Southeast Asia"), ("What we do", "Localization, store featuring and UA across Indonesia, Thailand, Vietnam and the Philippines"), ("Terms", "Revenue share 70/30 after store fees\nNo upfront fee\n2-year term, exclusive for Southeast Asia")], '2025-09-09T15:45:00Z')),
 'Brightlane Studio': ("Brightlane x Harmony Games - creative retainer", [
   ('2025-08-29T17:00:00Z', 'V', "Hi Frederick,\n\nGreat talking yesterday. Our proposal for a monthly creative retainer (statics, video edits, store screenshots) is attached. We could start Oct 1.\n\nInes"),
   ('2025-09-26T16:20:00Z', 'V', "Hi Frederick, checking in on the retainer. Can you confirm by Oct 1 so I can book the team for October?\n\nInes")],
   ('gdocs', 'Brightlane Studio - Creative Retainer Proposal', "Brightlane Studio - Creative Retainer Proposal\nScope: up to 20 statics, 6 video edits and 4 store screenshot sets a month\nFee: $3,500/month, invoiced on the 1st\nStart: Oct 1, 2025; 3-month minimum\nTo start: reply to confirm", '2025-08-29T17:10:00Z')),
 'Soundvault': ("Music licence for Zombie Match 3D trailers", [
   ('2025-09-08T18:00:00Z', 'F', "Hi Rafael,\n\nCould you send pricing for the trailer music pack we talked about? Annual licence, all platforms.\n\nThanks,\nFrederick"),
   ('2025-09-09T15:00:00Z', 'V', "Hi Frederick,\n\nHere's the quote for the trailer pack (attached): annual licence, all platforms, $1,188 paid up front when you sign. The quote holds until Oct 15.\n\nRafael"),
   ('2025-09-25T16:00:00Z', 'V', "Hi Frederick, just a reminder the trailer pack quote runs out on Oct 15. Want me to send the licence for signature?\n\nRafael")],
   ('gdocs', 'Soundvault - Licence Quote - Harmony Games', "Soundvault - Licence Quote - Harmony Games\nTrailer music pack (40 tracks), annual licence, all platforms\nPrice: $1,188, paid in full on signature\nQuote valid until Oct 15, 2025", '2025-09-09T15:10:00Z')),
 'Reviewly': ("Your Reviewly trial has started", [
   ('2025-09-19T17:00:00Z', 'V', "Hi Frederick,\n\nYour free 30-day trial of Reviewly is live, with Zombie Match 3D's iOS and Android reviews connected. I'm Hana, your onboarding contact, so just reply here with any questions.\n\nHana"),
   ('2025-09-29T15:30:00Z', 'V', "Hi Frederick, how's the trial going? Happy to do a 20-minute walkthrough of reply templates this week if useful.\n\nHana")],
   ('gdocs', 'Reviewly - Trial Terms', "Reviewly - Trial Terms\nFree trial: 30 days from sign-up (Sep 19, 2025)\nAfter the trial the account moves to Growth at $79/month on Oct 20, 2025 unless cancelled by Oct 19, 2025\nCancel: in the app or by email to your onboarding contact", '2025-09-19T17:10:00Z')),
 'Streamcast Talent': ("Creator campaign for Zombie Match 3D - November", [
   ('2025-09-11T20:00:00Z', 'V', "Hi Frederick,\n\nFollowing our call, here's the proposal for a November creator campaign with 8 mid-tier TikTok and YouTube creators. We take a 50% deposit when you book, and bookings close Oct 31 for the November slots.\n\nKofi"),
   ('2025-09-24T18:00:00Z', 'V', "Hi Frederick, want me to pencil in the November slot?\n\nKofi")],
   ('gdocs', 'Streamcast Talent - Creator Campaign Proposal', "Streamcast Talent - Creator Campaign Proposal\nCampaign: November 2025, 8 creators, TikTok and YouTube Shorts\nBudget: $8,000; 50% deposit ($4,000) on booking, balance on delivery\nBook by Oct 31, 2025", '2025-09-11T20:15:00Z')),
 'Lingora': ("Store listing localization quote", [
   ('2025-09-02T16:00:00Z', 'F', "Hi Elena,\n\nCould you quote localizing the Zombie Match 3D store listings (iOS and Google Play) into your 12-language pack?\n\nThanks,\nFrederick"),
   ('2025-09-03T09:00:00Z', 'V', "Hi Frederick,\n\nQuote attached: 12 languages for $2,640, delivered two weeks after the PO and invoiced on delivery. The price holds until Oct 3.\n\nElena"),
   ('2025-09-23T08:30:00Z', 'V', "Hi Frederick, any update? Send the PO and we can start Monday.\n\nElena")],
   ('gdocs', 'Lingora - Quote - Store Listing Localization', "Lingora - Quote - Store Listing Localization\nScope: iOS and Google Play listings for Zombie Match 3D, 12 languages\nPrice: $2,640, invoiced on delivery\nDelivery: two weeks from the PO\nQuote valid until Oct 3, 2025", '2025-09-03T09:10:00Z')),
 'Panelpulse': ("Player panel for Zombie Match 3D", [
   ('2025-09-04T17:00:00Z', 'V', "Hi Frederick,\n\nGood speaking yesterday. Order form attached for a 12-player moderated panel on Oct 14. It's $1,200 prepaid, and I need your confirmation by Oct 6 to recruit.\n\nArjun"),
   ('2025-09-26T15:00:00Z', 'V', "Hi Frederick, still keen on the Oct 14 panel? Recruiting closes Oct 6.\n\nArjun")],
   ('gdocs', 'Panelpulse - Order Form - Moderated Player Panel', "Panelpulse - Order Form - Moderated Player Panel\nPanel: 12 players (mobile puzzle, 25-54), 90 minutes, Oct 14, 2025\nPrice: $1,200, prepaid on confirmation\nConfirm by Oct 6, 2025", '2025-09-04T17:10:00Z')),
 'Ascendo': ("ASO retainer proposal", [
   ('2025-08-21T16:00:00Z', 'V', "Hi Frederick,\n\nThanks for the call. Proposal attached for monthly ASO on Zombie Match 3D (keywords, screenshots, A/B tests), $900/month starting Oct 1.\n\nLucia"),
   ('2025-09-25T17:00:00Z', 'V', "Hi Frederick, can you confirm by Oct 1 so we can kick off? I'll send the contract over once you do.\n\nLucia")],
   ('gdocs', 'Ascendo - ASO Retainer Proposal', "Ascendo - ASO Retainer Proposal\nScope: keyword research, screenshot sets, two store A/B tests a month\nFee: $900/month from Oct 1, 2025, month to month after a 3-month start\nContract to follow on confirmation", '2025-08-21T16:10:00Z')),
 'Wishwave': ("Seattle Indie Expo - pre-registration push", [
   ('2025-09-17T19:00:00Z', 'V', "Hi Frederick,\n\nGreat chatting. Proposal attached for a pre-registration push at the Seattle Indie Expo on Nov 7: we cover the stand and two passes, you cover travel for two. We'll book the flights and hotel and invoice you at cost.\n\nSven"),
   ('2025-09-26T18:30:00Z', 'V', "Hi Frederick, can you confirm by Oct 17 so I can book travel while fares are low?\n\nSven")],
   ('gdocs', 'Wishwave - Pre-registration Push Proposal', "Wishwave - Pre-registration Push Proposal\nEvent: Seattle Indie Expo, Nov 7, 2025\nWishwave covers: stand, two exhibitor passes, pre-registration landing page\nHarmony Games covers: travel and hotel for two, booked by Wishwave and invoiced at cost (about $1,600)\nConfirm by Oct 17, 2025", '2025-09-17T19:10:00Z')),
 'Vaultline': ("Vaultline Standard renewal - Oct 12", [
   ('2025-09-22T16:00:00Z', 'V', "Hi Frederick,\n\nQuick one: we're retiring the old Starter tier, so your nightly database backups move to Standard ($19/month) when the plan renews on Oct 12. Can you confirm you want to keep them running? If not, I'll stop the backups at renewal.\n\nMila")],
   ('gdocs', 'Vaultline - Standard Plan', "Vaultline - Standard Plan\nNightly backups of your game database, 30-day retention\nPrice: $19/month, renews Oct 12, 2025\nThe existing terms carry over; nothing new to sign", '2025-09-22T16:10:00Z')),
 'Certwell': ("Certificate renewal for your API domain", [
   ('2025-09-23T15:00:00Z', 'V', "Hi Frederick,\n\nThe SSL certificate on your game API domain expires on Oct 20. The renewal is $89 for the year. Reply to confirm and we'll reissue it; otherwise it lapses on the 20th.\n\nJonas")],
   ('gdocs', 'Certwell - Renewal Notice', "Certwell - Renewal Notice\nCertificate: OV SSL for the game API domain\nRenewal: $89/year, due Oct 20, 2025\nSame terms as the current certificate; nothing new to sign", '2025-09-23T15:10:00Z')),
 'Kinetic Arcade': ("Kinetic Arcade - publishing LOI for Zombie Match 3D", [
   ('2025-09-10T16:30:00Z', 'V', "Hi Frederick,\n\nFollowing our call, the letter of intent is attached: we'd publish Zombie Match 3D in Japan and Korea on a revenue share, at no cost to you. It includes 12 months' exclusivity for those markets while we prepare the launch. We'd need it signed by Oct 20.\n\nNoor"),
   ('2025-09-29T17:00:00Z', 'V', "Hi Frederick, any thoughts on the LOI? Oct 20 is our internal deadline.\n\nNoor")],
   ('gdocs', 'Kinetic Arcade - Letter of Intent', "Kinetic Arcade - Letter of Intent\nTerritories: Japan and Korea\nModel: revenue share, no fees to Harmony Games\nExclusivity: 12 months from signature for those territories\nSignature needed by Oct 20, 2025", '2025-09-10T16:40:00Z')),
 'Lumencloud': ("Lumencloud Startup Program - $25k credits", [
   ('2025-09-11T18:00:00Z', 'V', "Hi Frederick,\n\nThanks for applying to the Lumencloud Startup Program. Good news, Harmony Games qualifies for $25,000 in Lumencloud credits. The program agreement is attached; it's a 36-month term and the credits start once it's signed. Applications for this cohort close Oct 31.\n\nAiden"),
   ('2025-09-30T16:00:00Z', 'V', "Hi Frederick, just checking you saw this one, the cohort closes Oct 31.\n\nAiden")],
   ('gdocs', 'Lumencloud - Startup Program Agreement', "Lumencloud - Startup Program Agreement\nCredits: $25,000, usable over 36 months\nTerm: 36 months from signature\nNo charges while credits last\nSign by Oct 31, 2025 (cohort closes)", '2025-09-11T18:10:00Z')),
 'Bundlehouse': ("Bundlehouse holiday bundle - Domino Delights?", [
   ('2025-09-16T17:30:00Z', 'V', "Hi Frederick,\n\nThanks for the chat. I've sent our deck for the holiday puzzle bundle: no cost to join, and it includes a licence to use Domino Delights' name and art in the bundle marketing. Submissions close Nov 1.\n\nFreya"),
   ('2025-09-26T16:00:00Z', 'V', "Hi Frederick, do you want me to hold a spot in the bundle? The participation agreement needs signing by Nov 1.\n\nFreya")],
   ('gslides', 'Bundlehouse - Holiday Puzzle Bundle', [("Bundlehouse Holiday Puzzle Bundle", "Proposal for Harmony Games"), ("How it works", "No cost to join\nRevenue share on bundle sales"), ("Licence", "Bundlehouse may use your game's name, logo and art in bundle marketing for 18 months"), ("Timing", "Sign the participation agreement (it carries the licence) by Nov 1, 2025")], '2025-09-16T17:40:00Z')),
 'Orbit Store': ("Orbit Store featuring - Zombie Match 3D", [
   ('2025-09-19T16:00:00Z', 'V', "Hi Frederick,\n\nThanks for the call on Wednesday. We'd like to feature Zombie Match 3D in our November puzzle week. The featuring agreement has to be accepted in our partner portal by an authorised signatory of the company. No fees. Could that happen by Oct 24?\n\nMateo"),
   ('2025-09-30T15:30:00Z', 'V', "Hi Frederick, gentle nudge on the featuring agreement, Oct 24 is the cut-off.\n\nMateo")],
   ('gdocs', 'Orbit Store - Featuring Agreement (summary)', "Orbit Store - Featuring Agreement (summary)\nPromotion: November puzzle week feature\nFees: none\nTerm: the promotion only\nAcceptance: by an authorised signatory in the Orbit partner portal by Oct 24, 2025", '2025-09-19T16:10:00Z')),
 'Markward': ("Markward free tier - brand monitoring", [
   ('2025-09-09T16:00:00Z', 'V', "Hi Frederick,\n\nAs discussed, the free tier covers alerts for 'Zombie Match 3D' and 'Harmony Games' on the app stores and socials. To switch it on, accept the terms in the dashboard and you're set. Nothing to pay.\n\nLeah"),
   ('2025-09-23T16:30:00Z', 'V', "Hi Frederick, the free tier is ready whenever you accept the terms in the dashboard. Shall I keep the setup on hold for you?\n\nLeah")],
   ('gdocs', 'Markward - Free Tier Terms', "Markward - Free Tier Terms (click-through)\nMonitoring: 2 brand names across app stores and social platforms\nPrice: free, no payment details\nTerm: none, switch it off any time\nActivation: accept the terms in the Markward dashboard", '2025-09-09T16:10:00Z')),
 'Playfuse': ("Playfuse bundle partnership - NDA", [
   ('2025-09-25T17:00:00Z', 'V', "Hi Frederick,\n\nBefore our Oct 8 call we'd like to share our 2026 bundle roadmap. Could someone on your side sign a mutual NDA? Happy to use your lawyers' template.\n\nIris")],
   ('gdocs', 'Playfuse - Mutual NDA', "Playfuse - Mutual NDA (ESG Law mutual NDA template)\nParties: Harmony Games Inc. and Playfuse\nPurpose: discuss a 2026 bundle partnership\nTerm: 2 years\nSignature: an officer of each party, by Oct 8, 2025 (before our call that day)", '2025-09-25T17:10:00Z')),
 'Hootline': ("Your Hootline promo", [   # rev4 (M4/WIN): both messages before mid-August; terms in the body, no filed paper
   ('2025-08-05T16:00:00Z', 'V', "Hi Frederick,\n\nWelcome to Hootline! Your three social profiles are connected and the startup promo keeps the account free until Jan 31, 2026. After that it's $39/month unless you cancel.\n\nGemma"),
   ('2025-08-12T16:30:00Z', 'V', "Hi Frederick,\n\nNow that your profiles are set up, a quick planning question: when the startup promo ends on Jan 31, would you like to keep the scheduler after that?\n\nGemma")],
   None),
 'Glyphworks': ("Font licence quote - Zombie Match 3D", [
   ('2025-09-15T17:00:00Z', 'F', "Hi Tomas,\n\nCould you quote an app embedding licence for the two display fonts we use in Zombie Match 3D?\n\nThanks,\nFrederick"),
   ('2025-09-16T08:30:00Z', 'V', "Hi Frederick,\n\nThe app embedding licence for both fonts is $640. The quote is valid until Jan 31 and nothing is owed until you order.\n\nTomas"),
   ('2025-09-30T08:00:00Z', 'V', "Hi Frederick, any decision on the fonts?\n\nTomas")],
   ('gdocs', 'Glyphworks - Quote - App Embedding Licence', "Glyphworks - Quote - App Embedding Licence\nFonts: two display families, app embedding\nPrice: $640, payable when ordered\nQuote valid until Jan 31, 2026", '2025-09-16T08:40:00Z')),
 'Cloudlark': ("Cloudlark credits reserved for Harmony Games", [
   ('2025-09-12T17:00:00Z', 'V', "Hi Frederick,\n\nFollowing up on our chat, we've reserved $10,000 of Cloudlark credits for Harmony Games and will hold them until Feb 28. Nothing to do until you want to activate them. Would you like to activate now or later?\n\nYara")],
   ('gdocs', 'Cloudlark - Credit Reservation', "Cloudlark - Credit Reservation\nCredits: $10,000 reserved for Harmony Games\nHeld until Feb 28, 2026\nActivation: when you're ready; nothing owed", '2025-09-12T17:10:00Z')),
 'Echohall': ("Echohall Pro for your community", [
   ('2025-08-26T17:00:00Z', 'V', "Hi Frederick,\n\nThanks for setting up the Zombie Match 3D community on Echohall. You're on the free plan.\n\nBruno"),
   ('2025-09-18T17:00:00Z', 'V', "Hi Frederick, proposal attached for Pro ($49/month) whenever you want the moderation tools. The free plan carries on as it is until then. Let me know what you think.\n\nBruno")],
   ('gdocs', 'Echohall - Pro Upgrade Proposal', "Echohall - Pro Upgrade Proposal\nPro: $49/month from the day you upgrade\nFree plan: continues as it is until you choose to upgrade", '2025-09-18T17:10:00Z')),
 'Pressbeam': ("Pressbeam launch package", [
   ('2025-09-11T16:00:00Z', 'V', "Hi Frederick,\n\nGood to talk yesterday. Here's the launch package for your 2026 release: newswire distribution plus 40 targeted outlets, $1,200 when you book. No travel, all remote, and you can book any time before launch. Let me know if you'd like to go ahead.\n\nAva")],
   ('gdocs', 'Pressbeam - Launch Package', "Pressbeam - Launch Package\nNewswire distribution plus 40 targeted gaming outlets\nPrice: $1,200, paid when booked\nNo travel; book any time before launch", '2025-09-11T16:10:00Z')),
 'Retainly': ("Welcome to Retainly", [
   ('2025-09-15T16:00:00Z', 'V', "Hi Frederick,\n\nYour startup trial is live. It runs free until Jan 12, then Growth is $99/month. Could you let me know whether you plan to stay on after the trial?\n\nOmar")],
   ('gdocs', 'Retainly - Trial Terms', "Retainly - Trial Terms\nExtended startup trial: free until Jan 12, 2026\nAfter the trial: Growth at $99/month unless cancelled before Jan 12, 2026", '2025-09-15T16:10:00Z')),
 'Quillcraft': ("Quillcraft beta", [
   ('2025-09-03T17:00:00Z', 'V', "Hi Frederick,\n\nYou're in the Quillcraft beta. It's free through January, and pricing starts in February.\n\nNadia"),
   ('2025-09-29T16:00:00Z', 'V', "Hi Frederick, would you join a 30-minute feedback call next week?\n\nNadia")],
   ('gdocs', 'Quillcraft - Beta Terms', "Quillcraft - Beta Terms\nBeta: free through January 31, 2026\nPaid plans from February 2026", '2025-09-03T17:10:00Z')),
 'Tilecast': ("Tilecast pilot slot", [
   ('2025-09-19T16:00:00Z', 'V', "Hi Frederick,\n\nThanks for the call yesterday. We can offer a free pilot slot in February for the interactive demo widget on your website. Want me to hold it?\n\nKenji")],
   ('gdocs', 'Tilecast - Pilot Offer', "Tilecast - Pilot Offer\nInteractive demo widget for your website\nFree pilot slot: February 2026\nNo cost during the pilot", '2025-09-19T16:10:00Z')),
 'Benchmarkly': ("Benchmarkly sample report", [
   ('2025-09-22T17:00:00Z', 'F', "Hi Clara,\n\nCould you send the sample benchmark report for puzzle games?\n\nThanks,\nFrederick"),
   ('2025-09-23T16:00:00Z', 'V', "Hi Frederick,\n\nSample report attached, free. The full set is a $300/month subscription from February if you want it. Let me know if you'd like to subscribe.\n\nClara")],
   ('gdocs', 'Benchmarkly - Subscription Offer', "Benchmarkly - Subscription Offer\nSample report: free\nFull benchmark set: $300/month, starting February 2026 if you subscribe", '2025-09-23T16:10:00Z')),
 'Loopnote': ("Your Loopnote trial", [
   ('2025-09-08T16:00:00Z', 'V', "Hi Frederick,\n\nWelcome to Loopnote. Your team trial is free until Feb 1.\n\nPavel"),
   ('2025-09-26T16:00:00Z', 'V', "Hi Frederick, want me to add the rest of your team to the trial?\n\nPavel")],
   ('gdocs', 'Loopnote - Trial Terms', "Loopnote - Trial Terms\nTeam trial: free until Feb 1, 2026\nAfter the trial: $8 per user per month if you continue", '2025-09-08T16:10:00Z')),
 'Driftwood Audio': ("Voice-over quote", [
   ('2025-09-24T17:00:00Z', 'F', "Hi Sofia,\n\nCould you quote voice-over for a 30-second trailer?\n\nThanks,\nFrederick"),
   ('2025-09-25T16:00:00Z', 'V', "Hi Frederick,\n\n$950 for the trailer VO, paid when you book a session. The quote is good until Feb 28. Let me know if you'd like to book.\n\nSofia")],
   ('gdocs', 'Driftwood Audio - Voice-over Quote', "Driftwood Audio - Voice-over Quote\n30-second trailer voice-over\nPrice: $950, paid when you book a session\nQuote valid until Feb 28, 2026", '2025-09-25T16:10:00Z')),
 'Motive Forge': ("Motive Forge - 3D art quote", [
   ('2025-09-15T16:00:00Z', 'V', "Hi Frederick, hi Arthur,\n\nQuote attached for 12 rigged monster models for Zombie Match 3D: $6,400, four weeks from kickoff.\n\nHugo"),
   ('2025-09-19T17:45:00Z', ART, "Thanks Hugo, we're keeping the art in-house, so we'll pass on this one.\n\nArthur")],
   ('gdocs', 'Motive Forge - 3D Art Quote', "Motive Forge - 3D Art Quote\n12 rigged monster models\nPrice: $6,400, 50% on kickoff\nDelivery: four weeks from kickoff", '2025-09-15T16:10:00Z')),
 'Spotlight Fest': ("Spotlight Fest - showcase slot, Dec 5", [
   ('2025-09-08T16:00:00Z', 'V', "Hi Frederick,\n\nWe'd love Zombie Match 3D in the Spotlight Fest indie showcase on Dec 5. The stand fee is $750. Could we set up a quick call?\n\nRina")],
   ('gdocs', 'Spotlight Fest - Showcase Terms', "Spotlight Fest - Showcase Terms\nIndie showcase, Dec 5, 2025\nStand fee: $750", '2025-09-08T16:10:00Z')),
 'Nova Rewards': ("Nova Rewards partnership", [
   ('2025-09-03T15:00:00Z', 'V', "Hi Frederick,\n\nWe'd like to offer a rewarded-survey partnership for Zombie Match 3D on a revenue share. Happy to set up a call.\n\nRuth"),
   ('2025-09-23T16:00:00Z', 'V', "Hi Frederick,\n\nAn update from our side: we're pausing new partnerships for the rest of the year, so I'm withdrawing this offer for now. Sorry to pull it.\n\nRuth")], None),
}

# ============================================================ Drive / Docs / Sheets / Slides
DF_COLS = ['id', 'name', 'mime_type', 'parents_json', 'owner_email', 'shared_with_emails_json', 'shared_roles_json',
           'visibility', 'owners_json', 'modified_time', 'created_time', 'trashed', 'starred']
FOLDER_MT, DOC_MT, SLIDE_MT, SHEET_MT = ('application/vnd.google-apps.folder', 'application/vnd.google-apps.document',
                                         'application/vnd.google-apps.presentation', 'application/vnd.google-apps.spreadsheet')


def drive(fid, name, mime, parent, owner, shares, created, modified):
    ins('gdrive.drive_files', DF_COLS,
        [fid, name, mime, js([parent]), owner, js([e for e, _ in shares]),
         js([{'email': e, 'role': r} for e, r in shares]), 'private', js([owner]), modified, created, False, False], fid)


def doc(fid, title, body, parent, owner, shares, created, modified, heads=()):
    drive(fid, title, DOC_MT, parent, owner, shares, created, modified)
    first = len(body.split('\n', 1)[0])        # rev2 (C-adv 4): the TITLE run covers the whole first line
    runs, pos = [{'start': 0, 'end': first + 1, 'named_style': 'TITLE', 'list_id': None, 'list_nesting': 0}], first + 1
    for hd in heads:
        i = body.index('\n' + hd + '\n', pos - 1) + 1
        if i > pos:
            runs.append({'start': pos, 'end': i, 'named_style': 'NORMAL_TEXT', 'list_id': None, 'list_nesting': 0})
        runs.append({'start': i, 'end': i + len(hd) + 1, 'named_style': 'HEADING_2', 'list_id': None, 'list_nesting': 0})
        pos = i + len(hd) + 1
    runs.append({'start': pos, 'end': len(body), 'named_style': 'NORMAL_TEXT', 'list_id': None, 'list_nesting': 0})
    ins('gdocs.docs_documents', ['document_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility', 'body_text',
                                 'style_runs_json', 'revision_id', 'drive_file_id', 'created_time', 'modified_time'],
        [fid, title, owner, js([e for e, _ in shares]), 'private', body, js(runs), h('rev' + fid, 10), fid, created,
         modified], fid)


def sheet(fid, title, grid, tab, parent, owner, shares, created, modified):
    drive(fid, title, SHEET_MT, parent, owner, shares, created, modified)
    ins('gsheets.sheets_spreadsheets', ['spreadsheet_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility',
                                        'drive_file_id', 'created_time', 'modified_time'],
        [fid, title, owner, js([e for e, _ in shares]), 'private', fid, created, modified], fid)
    ins('gsheets.sheets_sheets', ['spreadsheet_id', 'sheet_id', 'title', '"index"', 'row_count', 'column_count', 'grid_json'],
        [fid, 0, tab, 0, 1000, 26, js(grid)], f"{fid}#0")


def deck(fid, title, slides, parent, owner, shares, created, modified):
    drive(fid, title, SLIDE_MT, parent, owner, shares, created, modified)
    ins('gslides.slides_presentations', ['presentation_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility',
                                         'drive_file_id', 'revision_id', 'created_time', 'modified_time'],
        [fid, title, owner, js([e for e, _ in shares]), 'private', fid, h('rev' + fid, 10), created, modified], fid)
    for i, (head, body) in enumerate(slides):
        sid = 'slide_' + h(fid + 's' + str(i), 12)
        ins('gslides.slides_pages', ['presentation_id', 'object_id', '"index"', 'layout', 'notes'], [fid, sid, i, 'TITLE_AND_BODY', None], f"{fid}#{sid}")
        for oid, ph, text, ordn, y, hgt in [('el_' + h(fid + 'e' + str(i), 12), 'TITLE', head, 0, 457200, 1143000),
                                             ('el_' + h(fid + 'b' + str(i), 12), 'BODY', body, 1, 1600200, 3200400)]:
            ins('gslides.slides_page_elements', ['presentation_id', 'page_object_id', 'object_id', 'kind', 'text',
                                                 'placeholder_type', 'x_emu', 'y_emu', 'width_emu', 'height_emu', 'table_json',
                                                 'ordinal'],
                [fid, sid, oid, 'SHAPE', text, ph, 457200, y, 8229600, hgt, None, ordn], f"{fid}#{oid}")


FOUNDERS = [(ROB, 'reader'), (ART, 'reader'), (FRED, 'reader')]
doc(I['guardrails_doc'], GUARD_TITLE, GUARD_BODY, 'd_63fffeb4fab5233ed5bb73', LEO, FOUNDERS, T['guardrails'], '2025-09-26T18:00:00Z',
    ['How to decide', 'Answers'])
doc(I['ua_buckets_doc'], UA_TITLE, UA_BODY, ROOT_FRED, FRED, [(LEO, 'reader')], T['ua_buckets_doc'], T['ua_buckets_doc'])
doc(I['esg_checklist_doc'], CHECK_TITLE, CHECK_BODY, 'd_63fffeb4fab5233ed5bb73', LEO, FOUNDERS, '2025-09-25T16:20:00Z',
    '2025-09-25T16:20:00Z', ['Include'])
drive(I['q4_folder'], 'Q4 commitments', FOLDER_MT, ROOT_FRED, FRED, [(LEO, 'writer')], T['folder'], T['readme'])
doc(I['readme_doc'], README_TITLE, README_BODY, I['q4_folder'], LEO, [(FRED, 'writer')], T['readme'], T['readme'],
    ['Columns', 'Contacts'])
sheet(I['template_sheet'], 'Q4 commitments - template', [["Company", "Contact", "What's waiting", "Decision", "Answered by",
                                                           "What we told them", "Next date"]], 'Log', I['q4_folder'], LEO,
      [(FRED, 'writer')], T['template'], T['template'])
sheet(I['tracker_sheet'], TRACKER_TITLE, TRACKER_GRID, 'Tracker', ROOT_FRED, FRED, [], T['tracker'], T['tracker'])
PAPERS = 'd_' + h('paperwork_folder', 22)
IDS['paperwork_folder'] = PAPERS
drive(PAPERS, 'Vendor & partner paperwork', FOLDER_MT, ROOT_FRED, FRED, [], '2025-06-18T17:40:00Z', '2025-09-25T17:10:00Z')
PAPER_IDS = {}
for key, (subj, msgs, paper) in MT.items():
    if not paper:
        continue
    kind, title, body, at = paper
    fid = I['lanternfly_deck'] if key == 'Lanternfly Publishing' else B.drive('paper:' + key)
    PAPER_IDS[key] = fid
    if kind == 'gslides':
        deck(fid, title, body, PAPERS, FRED, [], at, at)
    else:
        doc(fid, title, body, PAPERS, FRED, [], at, at)

# ============================================================ Slack
SL_COLS = ['id', 'ts', 'channel_id', 'type', 'user_id', 'text', 'thread_parent_id', 'thread_ts_legacy', 'reply_count',
           'reply_users_count', 'latest_reply', 'is_activity_message', 'subtype', 'reactions_json', 'files_json',
           'attachments_json', 'created_at', 'metadata_json']


def slack(chan_ts, user, text, at, parent=None):
    ch, ts = chan_ts.split('/')
    mid = hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]
    ins('slack.slack_messages', SL_COLS, [mid, ts, ch, 'message', user, text, parent[0] if parent else None,
                                          parent[1] if parent else None, 0, 0, None, False, None, '[]', '[]', '[]',
                                          D.datetime.fromtimestamp(float(ts), D.UTC).strftime('%Y-%m-%dT%H:%M:%S.%fZ'), '{}'],
        chan_ts)
    return mid


IDS['slack_mid'] = {}
IDS['slack_mid']['july_sign_note'] = slack(I['july_sign_note'], SLACK_U[LEO], S_JULY, T['july_sign_note'])
IDS['slack_mid']['robert_cancel_all'] = slack(I['robert_cancel_all'], SLACK_U[ROB], S_ROBERT, T['robert_cancel_all'])
# Robert's note after the Sep 17 Spotlight Fest call: the answer's load-bearing (●) carrier; the event description
# repeats it as supporting detail (GCal description is ○, unverified rendering: Ask_Carriers §5)
SPOT_AT = '2025-09-17T18:41:00Z'
I['spotlight_note'] = f"{B.EXEC}/{B.slack_ts('spotlight_note', SPOT_AT)}"
S_SPOT = B.Q["spotlight_note_v4"]     # rev4 (M3): names the Dec 5 indie showcase and Rina, not the fest
IDS['slack_mid']['spotlight_note'] = slack(I['spotlight_note'], SLACK_U[ROB], S_SPOT, SPOT_AT)
IDS['spotlight_note'] = I['spotlight_note']
IDS['slack_mid']['amendment_root'] = slack(I['amendment_root'], SLACK_U[LEO], S_AMEND, T['amendment'])
PT_ROOT = ('c41d37178fca394c135408d2b38e0879', '1758513190.847889')    # base: Leonard, Sep 22, Playtestcloud results (no replies)
IDS['slack_mid']['framewell_waiver_reply'] = slack(I['framewell_waiver_reply'], SLACK_U[LEO], S_WAIVER, T['framewell_waiver'], parent=PT_ROOT)
upd('slack.slack_messages', {'reply_count': 1, 'reply_users_count': 1, 'latest_reply': I['framewell_waiver_reply'].split('/')[1],
                             'thread_ts_legacy': PT_ROOT[1]}, 'id', PT_ROOT[0])
# rev4 (M2): Leonard's answer is a thread reply in the 1:1 DM under his own Sep 17 root "we have no localization though"
DM_ROOT = ('c148cae9de21cd26027d8bbc89bb127c', '1758151772.570449')   # base: Leonard, Sep 17, no replies
IDS['slack_mid']['lanternfly_dm'] = slack(I['lanternfly_dm'], SLACK_U[LEO], S_DM, T['lanternfly_dm'], parent=DM_ROOT)
upd('slack.slack_messages', {'reply_count': 1, 'reply_users_count': 1, 'latest_reply': I['lanternfly_dm'].split('/')[1],
                             'thread_ts_legacy': DM_ROOT[1]}, 'id', DM_ROOT[0])

# ============================================================ Trello (Arthur's keep-running card, Doing list)
TA_COLS = ['id', 'type', 'date', '"idMemberCreator"', '"idBoard"', '"idCard"', 'data_json']
TC_COLS = ['id', 'name', '"idBoard"', '"idList"', '"desc"', 'pos', 'closed', 'due', '"dueComplete"', '"idMembers_json"',
           '"idLabels_json"', '"idShort"', '"shortLink"', '"shortUrl"', 'url', '"dateLastActivity"', 'cover_json',
           'badges_json']


def badges(comments, description, items, checked):
    return {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": items,
            "checkItemsChecked": checked, "checkItemsEarliestDue": None, "comments": comments, "description": description,
            "due": None, "dueComplete": False, "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False,
            "location": False, "maliciousAttachments": 0, "start": None, "votes": 0}


KC = {'id': I['keep_card'], 'idShort': 456, 'name': KEEP_NAME, 'shortLink': 'Kp7rNw3Q'}
ins('trello.trello_cards', TC_COLS, [KC['id'], KEEP_NAME, HG_BOARD['id'], DOING['id'], KEEP_DESC, 140737488429056, False, None,
                                     False, js([TR_ART]), '[]', 456, None, None,
                                     'https://PERSON_6092_TRELLO_USERNAME.com/c/Kp7rNw3Q/456-keep-running-list-dont-cut',
                                     T['keep_card'], None, js(badges(0, True, len(KEEP_ITEMS), 0))], KC['id'])
IDS['keep_card_create'] = trello_id(T['keep_card'], 'keep-card-create')
ins('trello.trello_actions', TA_COLS, [IDS['keep_card_create'], 'createCard', T['keep_card'], TR_ART, HG_BOARD['id'], KC['id'],
                                       js({"board": HG_BOARD, "card": KC, "list": DOING})], IDS['keep_card_create'])
CL_AT = '2025-08-12T16:07:00Z'
IDS['keep_checklist'] = trello_id(CL_AT, 'keep-checklist')
ins('trello.trello_checklists', ['id', 'name', '"idCard"', '"idBoard"', 'pos'], [IDS['keep_checklist'], 'Keep running', KC['id'],
                                                                              HG_BOARD['id'], 16384.0], IDS['keep_checklist'])
IDS['keep_items'] = []
for n, item in enumerate(KEEP_ITEMS):
    iid = trello_id(CL_AT, f'keep-item-{n}')
    IDS['keep_items'].append(iid)
    ins('trello.trello_check_items', ['id', 'name', 'state', '"idChecklist"', 'pos', 'due', '"idMember"'],
        [iid, item, 'incomplete', IDS['keep_checklist'], 16384.0 * (n + 1), None, None], iid)
IDS['keep_checklist_action'] = trello_id(CL_AT, 'keep-checklist-action')
ins('trello.trello_actions', TA_COLS, [IDS['keep_checklist_action'], 'addChecklistToCard', CL_AT, TR_ART, HG_BOARD['id'], KC['id'],
                                       js({"board": HG_BOARD, "card": KC, "checklist": {"id": IDS['keep_checklist'],
                                                                                         "name": 'Keep running'}})],
    IDS['keep_checklist_action'])

# ============================================================ Gmail
GM_COLS = ['id', 'thread_id', 'user_email', 'label_ids_json', 'snippet', 'internal_date', 'date', 'size_estimate', 'subject',
           'from_email', 'from_name', 'to_json', 'cc_json', 'bcc_json', 'reply_to_json', 'body_text', 'body_html',
           'headers_json', 'in_reply_to', '"references"', 'mbox_from', 'attachments_meta_json']
INBOX = ["INBOX", "CATEGORY_PERSONAL"]
THREADS = {}


def addr(e, n):
    return f"{n} <{e}>"


def msgid_for(key, domain='mail.gmail.com'):
    return '<CA' + base64.b64encode(hashlib.sha256((B.SALT + key).encode()).digest()).decode()[:38].replace('/', '_').replace('+', '-') + f'@{domain}>'


def mail(key, at, subject, body, frm, to, cc, boxes, thread=None, parent=None, labels_for=None, tid=None, domain='mail.gmail.com'):
    """frm/to/cc: (email, name); boxes: mailboxes holding a copy (sender copy labelled SENT); tid: thread id for Fred's copy."""
    d0 = dt(at)
    ms = int(d0.timestamp() * 1000)
    msgid = msgid_for(key, domain)
    body_r = body.replace('\r\n', '\n').replace('\n', '\r\n')
    snippet = ' '.join(body.split())[:140]
    hdrs = [{"name": "Message-ID", "value": msgid}, {"name": "Date", "value": email.utils.format_datetime(d0)},
            {"name": "Subject", "value": subject}, {"name": "From", "value": addr(*frm)},
            {"name": "To", "value": ', '.join(addr(*x) for x in to)}]
    if cc:
        hdrs.append({"name": "Cc", "value": ', '.join(addr(*x) for x in cc)})
    pid = None
    if parent:
        pid = THREADS[parent]['last_msgid']
        hdrs += [{"name": "In-Reply-To", "value": pid}, {"name": "References", "value": THREADS[parent]['refs'] + [pid]}]
        hdrs[-1]["value"] = ' '.join(hdrs[-1]["value"])
    root = thread or key
    if root not in THREADS:
        THREADS[root] = {'boxes': {}, 'refs': [], 'last_msgid': None}
    for box in boxes:
        if box in THREADS[root]['boxes']:
            tref = THREADS[root]['boxes'][box]
            upd('gmail.gmail_threads', {'snippet': snippet}, 'id', tref)
        else:
            num = tid.split('/')[1] if (tid and box == FRED) else thread_num(at, f"{root}|{box}")
            tref = f"{box}/{num}"
            ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [tref, box, snippet, None], tref)
            THREADS[root]['boxes'][box] = tref
        labels = ["SENT"] if box == frm[0] else (labels_for or INBOX)
        ins('gmail.gmail_messages', GM_COLS,
            [f"{box}/{msgid}", tref, box, js(labels), snippet, ms, at, len(body_r) + 900, subject, frm[0], frm[1],
             js([addr(*x) for x in to]), js([addr(*x) for x in cc]), '[]', '[]', body_r, None, js(hdrs), pid,
             (' '.join(THREADS[root]['refs'] + [pid]) if pid else None), None, '[]'], f"{box}/{msgid}")
    if pid:
        THREADS[root]['refs'].append(pid)
    THREADS[root]['last_msgid'] = msgid
    return THREADS[root]['boxes'].get(FRED), f"{FRED}/{msgid}"


P = lambda e: (e, NAMES[e])
IDS['msg'] = {}
_, IDS['msg']['hub'] = mail('hub', T['hub'], HUB_SUBJ, HUB_BODY, P(LEO), [P(FRED)], [], [FRED, LEO], tid=I['hub_thread'])
_, IDS['msg']['esg_note'] = mail('esg_note', T['esg_note'], ESG_SUBJ, ESG_BODY, ESG_P, [P(LEO)], [P(FRED), P(ROB), P(ART)],
                                 [FRED, LEO, ROB, ART], tid=I['esg_thread'], thread='esg')
_, IDS['msg']['esg_ack'] = mail('esg_ack', T['esg_ack'], 'Re: ' + ESG_SUBJ, ESG_ACK, P(LEO), [ESG_P], [P(FRED), P(ROB), P(ART)],
                                [FRED, LEO, ROB, ART], thread='esg', parent='esg')
# Clipforge's payments-partner notice (automated, no Clipforge name in it)
NOTICE_BODY = ("Hello,\n\nThe pilot on workspace HG-2291 (UGC Studio) has reached its 20-video cap. Under your agreement the pilot "
               "now ends on Oct 15, 2025 and the Studio plan starts on Oct 16 at $1,800/month.\n\nTo cancel before the plan "
               "starts, write to billing@paylane.io by Oct 15. Replies to this email aren't monitored.\n\nPaylane, payments for UGC Studio")
_, IDS['msg']['clipforge_notice'] = mail('clipforge_notice', T['clipforge_notice'], 'Workspace HG-2291: your pilot is ending',
                                         NOTICE_BODY, PAYLANE, [P(FRED)], [], [FRED], tid=I['clipforge_notice_thread'],
                                         labels_for=["INBOX", "CATEGORY_UPDATES"], domain='paylane.io')
TID = {'Framewell': I['framewell_thread'], 'Pingwise': I['pingwise_thread'], 'Clipforge': I['clipforge_thread'],
       'Pixel Harbor Events': I['pixel_thread'], 'Lanternfly Publishing': I['lanternfly_thread'], 'Motive Forge': I['motive_thread'],
       'Spotlight Fest': I['spotlight_thread'], 'Nova Rewards': I['nova_thread']}
THREAD_IDS = {}
for key, (subj, msgs, paper) in MT.items():
    rep = PEOPLE[key]
    first = msgs[0][0]
    tid = TID.get(key) or f"{FRED}/{thread_num(first, 'member:' + key)}"
    for n, (at, who, body) in enumerate(msgs):
        s = subj if n == 0 else 'Re: ' + subj
        if who == 'V':
            frm, to, cc, boxes = rep, [P(FRED)], ([P(ART)] if key == 'Motive Forge' else []), ([FRED, ART] if key == 'Motive Forge' else [FRED])
        elif who == 'F':
            frm, to, cc, boxes = P(FRED), [rep], [], [FRED]
        else:
            frm, to, cc, boxes = P(who), [rep], [P(FRED)], [FRED, who]
        th, mid = mail(f"m:{key}:{n}", at, s, body, frm, to, cc, boxes, thread='t:' + key, parent=('t:' + key) if n else None, tid=tid)
        IDS['msg'][f"{key}:{n}"] = mid
    THREAD_IDS[key] = THREADS['t:' + key]['boxes'][FRED]

# ============================================================ Calendar (+ INT-11 invitation mails)
GC_COLS = ['event_id', 'calendar_id', 'summary', 'description', 'location', 'start_ts', 'end_ts', 'start_json', 'end_json',
           'organizer_email', 'creator_email', 'attendees_json', 'status', 'visibility', 'transparency', 'rrule_json',
           'recurring_event_id', 'original_start_json', 'sequence', 'created', 'updated', 'hangout_link', 'ical_uid']


def event(key, summary, desc, start, end, organizer, attendees, cals, created, updated, first_id, hangout, rsvp):
    uid = h('uid' + key, 32) + '@hg4'
    ids = {}
    for cal in cals:
        eid = first_id if cal == FRED else 'evt_' + h(key + cal, 22)
        att = []
        for e in attendees:
            a = {"email": e, "organizer": e == organizer, "responseStatus": rsvp.get(e, "needsAction")}
            if e == cal:
                a["self"] = True
            att.append(a)
        ins('gcal.gcal_events', GC_COLS, [eid, cal, summary, desc, None, start, end, js({"dateTime": start}), js({"dateTime": end}),
                                          organizer, organizer, js(att), 'confirmed', None, 'opaque', '[]', None, None, 0,
                                          created, updated, hangout, uid], eid)
        ids[cal] = eid
    return ids


IDS['evt'] = {}
IDS['evt']['review'] = event('review', 'Q4 commitments review', 'Everything we parked comes back here.', '2026-01-05T17:00:00Z',
                             '2026-01-05T17:45:00Z', LEO, [ART, FRED, LEO, ROB], [FRED, LEO, ROB, ART], T['review_event'],
                             T['review_event'], I['review_event'], 'https://meet.google.com/qfd-mcwr-tzh?hs=224', {LEO: 'accepted'})
PRIYA, RINA = PEOPLE['Clipforge'][0], PEOPLE['Spotlight Fest'][0]
IDS['evt']['clipforge'] = event('clipforge_kickoff', 'UGC Studio kickoff (workspace HG-2291)', None, T['clipforge_kickoff'],
                                '2025-07-14T16:30:00Z', FRED, [FRED, PRIYA], [FRED], '2025-07-08T18:10:00Z', '2025-07-08T18:10:00Z',
                                I['clipforge_kickoff'], 'https://meet.google.com/vkr-pxdn-gwa?hs=224', {FRED: 'accepted', PRIYA: 'accepted'})
IDS['evt']['spotlight'] = event('spotlight_call', 'Spotlight Fest showcase call', B.Q["spotlight_desc_v4"],
                                T['spotlight_call'], '2025-09-17T18:30:00Z', ROB, [FRED, ROB, RINA], [FRED, ROB],
                                '2025-09-12T16:00:00Z', '2025-09-17T18:40:00Z', I['spotlight_call'],
                                'https://meet.google.com/hzt-wnbe-ruk?hs=224', {ROB: 'accepted'})


def invitation(key, at, summary, when_hdr, when_body, meet, organizer, guests, boxes, eastern=None):
    d0 = dt(at)
    ms = int(d0.timestamp() * 1000)
    for box in boxes:
        tz_line, wh, wb = "Pacific Time - Los Angeles", when_hdr, when_body
        if box == ART and eastern:
            wh, wb = eastern
            tz_line = "Eastern Time - New York"
        mid = f"<calendar-{h(key + box, 8)}-{h(key + box + '1', 4)}-{h(key + box + '2', 4)}-{h(key + box + '3', 4)}-{h(key + box + '4', 12)}@google.com>"
        subject = f"Invitation: {summary} @ {wh} ({box})"
        body = (f"{summary}\r\n{wb}\r\n{tz_line}\r\n\r\nJoin with Google Meet\r\n{meet}\r\n\r\n"
                + f"Organizer\r\n{NAMES[organizer]}\r\n{organizer}\r\n\r\nGuests\r\n{NAMES[organizer]} - organizer\r\n"
                + "\r\n".join(guests) + "\r\n")
        tref = f"{box}/{thread_num(at, key + box)}"
        snippet = ' '.join(body.split())[:140]
        ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [tref, box, snippet, None], tref)
        hdrs = [{"name": "Message-ID", "value": mid}, {"name": "Date", "value": email.utils.format_datetime(d0)},
                {"name": "Subject", "value": subject}, {"name": "From", "value": f"{LOWER[organizer]} <{organizer}>"},
                {"name": "To", "value": ', '.join(guests)}]
        ins('gmail.gmail_messages', GM_COLS,
            [f"{box}/{mid}", tref, box, js(["INBOX", "CATEGORY_PERSONAL"]), snippet, ms, at, len(body) + 3000, subject,
             organizer, LOWER[organizer], js(guests), '[]', '[]', js([f"{LOWER[organizer]} <{organizer}>"]), body, None, js(hdrs),
             None, None, None, '[]'], f"{box}/{mid}")
        IDS.setdefault('invites', {})[f"{key}:{box}"] = tref


invitation('inv_review', T['review_event'], 'Q4 commitments review', 'Mon Jan 5, 2026 9am - 9:45am (PST)',
           'Monday Jan 5, 2026 \u22c5 9am \u2013 9:45am', 'https://meet.google.com/qfd-mcwr-tzh?hs=224', LEO, [FRED, ROB, ART],
           [FRED, ROB, ART], eastern=('Mon Jan 5, 2026 12pm - 12:45pm (EST)', 'Monday Jan 5, 2026 \u22c5 12pm \u2013 12:45pm'))
invitation('inv_spotlight', '2025-09-12T16:00:00Z', 'Spotlight Fest showcase call', 'Wed Sep 17, 2025 11am - 11:30am (PDT)',
           'Wednesday Sep 17, 2025 \u22c5 11am \u2013 11:30am', 'https://meet.google.com/hzt-wnbe-ruk?hs=224', ROB, [FRED, RINA], [FRED])

# ============================================================ Linear (Nintendo dev-kit ticket; the finding sits in the comment)
ins('linear.linear_issues', ['id', 'project_id', 'team_id', 'parent_id', 'assignee_id', 'creator_id', 'state_id', 'cycle_id',
                             'identifier', 'number', 'title', 'description', 'priority', 'estimate', 'due_date', 'started_at',
                             'completed_at', 'canceled_at', 'archived_at', 'time_in_status_minutes', 'labels_json',
                             'links_json', 'relations_json', 'state_history_json', 'is_archived', 'created_at', 'updated_at'],
    ['ZOM-567', None, 'team_ZOM', None, None, LIN_ART, 'Todo', None, 'ZOM-567', 567, LIN_TITLE, LIN_DESC, 3, None, None,
     None, None, None, None, None, '[]', '[]', '[]', '[]', False, T['zom567'], T['zom567_cmt']], 'ZOM-567')
ins('linear.linear_comments', ['id', 'issue_id', 'author_id', 'parent_id', 'body', 'is_edited', 'created_at', 'updated_at', 'sequence'],
    [I['zom567_cmt'], 'ZOM-567', LIN_ART, None, LIN_CMT, False, T['zom567_cmt'], T['zom567_cmt'], 1], I['zom567_cmt'])

# ============================================================ Contacts (ESG intake; three counterparties already present)
CT_COLS = ['contact_id', 'first_name', 'last_name', 'is_user', 'gender', 'status', 'job', 'email']
ins('contacts.contacts', CT_COLS, [I['esg_intake_contact'], 'ESG Law', 'intake', False, 'Unknown', 'Unknown',
                                   'Outside counsel - agreement intake', ESG_G[0]], I['esg_intake_contact'])
IDS['existing_contacts'] = {}
for key in ('Kinetic Arcade', 'Lumencloud', 'Markward'):
    cid = B.contact('existing:' + key)
    fn, ln = PEOPLE[key][1].split(' ', 1)
    ins('contacts.contacts', CT_COLS, [cid, fn, ln, False, 'Unknown', 'Unknown', key, PEOPLE[key][0]], cid)
    IDS['existing_contacts'][key] = cid

# ============================================================ write
order = ['gdrive', 'gdocs', 'gsheets', 'gslides', 'slack', 'trello', 'gmail', 'gcal', 'linear', 'contacts']
n_ins = sum(1 for s in OUT for x in OUT[s] if x.startswith('INSERT'))
n_upd = sum(1 for s in OUT for x in OUT[s] if x.startswith('UPDATE'))
head = ['-- Are you planning to inject? Yes',
        f'-- HarmonyGames injection - persona Frederick Stone <{FRED}> (Co-founder), Long Horizon.',
        f'-- Services: {", ".join(order)}. Statements: {n_ins} INSERT (one row each), {n_upd} UPDATE.',
        '-- Literal values only; parents before children; re-apply this exact SQL before every agent run.', 'BEGIN;']
body = []
for s in order:
    body.append(f'-- {s}')
    body += OUT.get(s, [])
(TI / '01_Universe_Inject.sql').write_text('\n'.join(head + body + ['COMMIT;']) + '\n')
IDS['threads'] = THREAD_IDS
IDS['papers'] = PAPER_IDS
IDS['people'] = PEOPLE
json.dump({'ids': IDS, 'rows': ROWS}, open(HERE / 'sql_ids.json', 'w'), indent=1)
print(n_ins, 'INSERT', n_upd, 'UPDATE', {k: len(v) for k, v in ROWS.items()})

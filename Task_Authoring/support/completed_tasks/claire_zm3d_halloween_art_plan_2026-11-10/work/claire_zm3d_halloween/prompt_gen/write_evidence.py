#!/usr/bin/env python3
"""Record the prompt-stage V3 reviews in Working_Files/00_V3_Authoring_Evidence.json (Guide schema): outcome_reviews for
prompt-writing (bound to the brief) and prompt-check (bound to 04_Prompt.txt), and role_reviews["prompt-check"].
The artifact hashes use stage_gate.file_digest (gate output lines excluded). Re-run after any change to the brief or
the prompt.

    python3 -B Task_Authoring/task_inputsN2/Working_Files/prompt_gen/write_evidence.py [prompt-writing|prompt-check]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
sys.path.insert(0, str(TASK.parents[1] / "Task_Authoring" / "tools"))
from stage_gate import file_digest  # noqa: E402

ACCEPTED = [
    "Plan doc: a new Google Doc owned by claire.morgan@harmonygames.co (any title naming Halloween or the plan, any folder of hers or Leonard's d_272d849cde40c35980a433), shared with the six review attendees of evt_d947bf7cd910549b674b1f (leonard.hayes, frederick.stone, martin.walsh, marcus.bennett, robert, arthur.blake @harmonygames.co) as commenter or writer, extra harmonygames.co people allowed (Julia Lawson included); it gives calls by surface type, store and icon pieces by the Thu Oct 16 12:00 PT merge cut, ads on Android US phone with Frederick by Fri Oct 10, every other working ad by Wed Oct 15, ads that run only on Android US tablet skipped, reuse of the iPhone 6.5\" and Play sets, owners Martin (icon, store art), Julia (ad statics) and Marcus (video, end cards); any wording and structure; the KayKit pack may be mentioned or not (ungraded since rev3)",
    "Tracker: a separate new spreadsheet owned by Claire whose title names Halloween, shared with the same six; exactly the 62 serving surfaces of solver/truth.json (no Archive row), keyed by the sheet's or the ticket title's creative name; call HALLOWEEN VERSION 14 / REFRESH FIRST 36 / REUSE 2 / SKIP 10 in any case ('Skip October' = Skip); owner Martin Walsh for the icon and store sets, Julia Lawson for the 6 working ad statics, Marcus Bennett for video and end cards (Skip rows may be blank); due Fri Oct 10 (an earlier internal date from Oct 6 allowed) for the 30 working ads on Android US phone, Wed Oct 15 (Oct 11-15 accepted) for the 18 other working ads, blank for Skip, by Thu Oct 16 12:00 PT (or earlier) for the icon and the iPad set, Oct 16 or blank for the iPhone set, blank / 'any day' / any October date leaving the 1-day review before the store pages go Halloween (e.g. Oct 21) for the Play set; any column names, order, extra columns, date format, Pacific or UTC day",
    "Ticket comments: one comment on each of the 58 serving library tickets ART-793 ... ART-854 (none needed on ART-836 ... ART-839) with that ad's call and due date (Skip: no date); any wording, a reason may be added, a second comment allowed; setting the ticket's due-date field is allowed in addition, never instead",
    "Assignments: exactly the 48 Halloween version / Refresh first ad tickets get their maker (42 Marcus Bennett usr_c77c50cc15c5342d, 6 Julia Lawson usr_8140f09bf9f1b94c), by id, name or email; the 10 Skip ad tickets stay unassigned",
    "New store-art tickets in Linear team ART: the Halloween app icon and the Halloween iPad 12.9\" set (one ticket each, or one ticket naming both); owner Martin, a due date by the Oct 16 cut and a description are optional; no ticket for the exported iPhone or Play sets",
    "Reply: a thread reply under C06DJBJL798/1759269913.882683 carrying both links (doc and tracker); also sending it to the channel is allowed; a summary may be added",
]
ALTERNATIVES = [
    "The app icon as Reuse of Martin's Sep 17 concept C08R8CHB0QL/1758121809.236839 (no icon ticket): rejected, Robert's thread reply C08R8CHB0QL/1758127951.679146 turns it down for the app icon; the icon is a Halloween version",
    "The icon around Oct 24 (Leonard's question): rejected, Arthur's calendar f_fdd6d2d2f4a4d2f5b908fb merges anything that ships in the build by Thu Oct 16 12:00 PT and lists the icon in the Nov 6 clean-up",
    "Only the sheet's rows as scope: rejected, Frederick's Trello comment 68dc65a0f2d7fb28743f5860 (Julia's 4:5 static) and his note cmt_art831_2 on ART-831 (still running, not on the sheet yet) add two serving creatives",
    "The four archived creatives as Skip rows: rejected, the Read me moves paused creatives to Archive and the ask scopes 'everything that's live today'",
    "Ads due Fri Oct 17 on four campaigns (Sep 12 draft): rejected, the Sep 30 changes mail is newer and says Wed Oct 15, not the 17th, and ends the Android US tablet campaign Oct 12",
    "Every working ad due Wed Oct 15 (the changes mail, rev3 move 1): rejected, Frederick's later reply C0880U9751A/1759275738.984915 says any new ad going on Android US phone has to be with him by Fri Oct 10, not the 15th",
    "Every working ad due Fri Oct 10 to be safe: rejected, the same reply keeps iOS UK on the 15th",
    "An ad on both iOS UK phone and Android US phone due Oct 15: rejected, the reply applies to any new ad going on Android US phone; the ticket carries one date",
    "Skip every cut that touches the Android US tablet campaign: rejected, the mail skips only what runs nothing but that campaign; couch alpha 50 16:9 (cmt_art823_1) and balloons alpha 50 (1) 16:9 (cmt_art854_2) also run on iOS UK tablet",
    "squirrelfail landscape and mrfluffernot landscape Refresh first on iOS UK tablet (rev3 move 5): rejected, Frederick's restart mail claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com> left both off iOS UK tablet on Sep 29, so they run only on Android US tablet: Skip",
    "cheer fastcouch 9:16 and 16:9 as Reuse (rev3 move 3): rejected, Robert's review C08R8CHB0QL/1759248337.170599 says the test sits on the July capture and cannot ship, and Marcus agrees to redo both C08R8CHB0QL/1759249269.380507",
    "cheer fastcouch 9:16 and 16:9 as Refresh first: rejected, their tickets already carry the Sep 16 re-capture (cmt_art808_2, cmt_art816_2); the deck's newest-capture rule makes them current art, so the call is Halloween version from that capture",
    "couch alpha 50, barrel marketing2 4:5 and balloons alpha 50 (1) Refresh first on their April tickets (rev3 move 2): rejected, Marcus's note C09ATAJ220H/1758823964.738872 records current-build re-captures and the deck says the newest capture counts",
    "Marcus's note covers couch alpha 50 16:9 as well: rejected, the note counts three cuts by name and that ticket's capture is Android #456 (cmt_art823_1); it stays Refresh first",
    "The working ad statics stay with Martin (rev3 move 4): rejected, his post C05KNDCHAAG/1759243286.478812 hands them to Julia for Oct 6-15 and Leonard's later reply C05KNDCHAAG/1759275107.322377 agrees; the icon and store art stay with Martin",
    "End card 001 and its three cuts as Halloween version on Android #1529 (rev3 move 6): rejected, Frederick's comment 68d6cff0c6568da5d9c8e81f on card 68768a1501ae552dbee94b8a says they still show the old zombies on the packs and need a re-render; the deck's Refresh first covers a re-render",
    "Buy the quoted Halloween Bits bundle: a plain distractor since rev3 (no graded row); no purchase is asked and the pack is already in the match3d repo ('we have the Halloween pack', C0880U9751A/1738109783.735889)",
    "Skip ads assigned to a maker: rejected, the ask assigns 'the ones that need new work'",
    "end card template 16:9 owned by Martin (ART-832 'Made by Martin Walsh'): rejected, the ask's split gives end cards to Marcus",
    "The tracker as a table inside the plan doc, or the reply as a top-level post / DM: rejected, the ask and the prompt ask for a plan doc plus a tracker and a reply in Leonard's thread",
    "Share without Leonard because his post C05KNDCHAAG/1759279503.256079 says he won't attend internal meetings Thursday: rejected, the prompt names the review, the invite still lists him as accepted organizer and its description says he dials in from LA for this one",
    "Share view-only: rejected, the ask says 'a plan doc we can comment on' and the prompt 'so they can comment'; commenter or writer accepted",
]
ROLE_SOURCES = ["slack:C06DJBJL798/1759269913.882683", "gcal:evt_d947bf7cd910549b674b1f", "slack:C08R8CHB0QL/1758121809.236839",
                "slack:C08R8CHB0QL/1758127951.679146", "slack:C08R8CHB0QL/1759245641.309714", "slack:D05V2N6PZNU/1759166437.080255",
                "slack:C06DJBJL798/1756914854.743319", "gsheets:f_02b1968f5e882366fbb883", "gdocs:f_fdd6d2d2f4a4d2f5b908fb",
                "gslides:f_5ebf55ad29e815d46243c8",
                "gmail:claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>",
                "gmail:claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>",
                "slack:C0880U9751A/1759275738.984915", "slack:C09ATAJ220H/1758823964.738872", "slack:C08R8CHB0QL/1759248337.170599",
                "slack:C05KNDCHAAG/1759243286.478812", "slack:C05KNDCHAAG/1759275107.322377",
                "linear:ART-793", "linear:ART-831", "trello:68dc65a0f2d7fb28743f5860", "trello:68d6cff0c6568da5d9c8e81f"]


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "prompt-writing"
    p = WF / "00_V3_Authoring_Evidence.json"
    data = json.loads(p.read_text())
    data.setdefault("outcome_reviews", {})
    data.setdefault("role_reviews", {})
    if stage == "prompt-writing":
        data["outcome_reviews"]["prompt-writing"] = {
            "reviewer": "Claude (build lane), prompt-writing stage",
            "rationale": ("The brief pins six deliverables named by Leonard's ask C06DJBJL798/1759269913.882683 and the planned "
                          "prompt: the plan doc and the tracker in Claire's Drive shared with the review attendees, a comment "
                          "on each serving ad ticket, the maker assignments, the new store-art tickets and the thread reply, on rev3's "
                          "truth (36 Refresh first, 12 Halloween version, 10 Skip, 0 Reuse among 58 ads; 42 Marcus, 6 Julia; "
                          "Fri Oct 10 for 30 working ads, Wed Oct 15 for 18). Each strongest alternative, including one per rev3 "
                          "move, was tested against the record that settles it (Frederick's date reply, Marcus's re-capture "
                          "note, Robert's test review, Martin's post with Leonard's reply, the restart mail, the packs comment, "
                          "Arthur's calendar, Frederick's changes mail, his Trello comment and ART-831 note); an independent "
                          "re-derivation from the records (prompt_eval/rederive_rev3.py) matches solver/truth.json; "
                          "representational variants are accepted in §4b."),
            "artifact": "04_Prompt_Writing_Brief.md", "artifact_hash": file_digest(WF / "04_Prompt_Writing_Brief.md"),
            "accepted_outcomes": ACCEPTED, "alternatives_considered": ALTERNATIVES}
    else:
        h = file_digest(TASK / "04_Prompt.txt")
        data["outcome_reviews"]["prompt-check"] = {
            "reviewer": "Claude (build lane), prompt-check stage",
            "rationale": ("Checked 04_Prompt.txt against the brief: each deliverable has one destination the persona knows "
                          "(her Drive, everyone on Thursday's review, each ad's ART ticket, ART for new store art, Leonard's "
                          "thread); the strongest alternative per deliverable and per rev3 move is settled by a dated, Claire-visible "
                          "record under the newer-source, authority and scope checks, or accepted as representational (§4b)."),
            "artifact": "04_Prompt.txt", "artifact_hash": h,
            "accepted_outcomes": ACCEPTED, "alternatives_considered": ALTERNATIVES}
        data["role_reviews"]["prompt-check"] = {
            "reviewer": "Claude (build lane), prompt-check stage",
            "rationale": ("Claire Morgan is the Art Lead over Zombie Match 3D's marketing art (Martin Walsh: icon and store art; "
                          "Marcus Bennett: UA video and end cards; Julia Lawson: the ad statics while Martin is out) and already "
                          "reacted to Martin's "
                          "Halloween icon concept in #zombie-art. Leonard, the CEO, asked her by name in #zombie_marketing to own "
                          "the art side of the Halloween push and put her on Thursday's review to walk the team through it. "
                          "Delegating to an assistant the per-surface Halloween calls, makers and dates, a plan doc and tracker "
                          "in her own Drive, the follow-through on the ART library tickets and the reply in Leonard's thread is "
                          "her own planning and authoring work for a seasonal go-to-market push, inside her remit at the clock: "
                          "every relied-on record is dated before 2025-10-01T00:00Z, every scoped read is visible to her, the "
                          "rev3 records in #zm-animations, #company-internal and #zombie-match3d included (check-sql PASS, base "
                          "records can-see YES), she owns the doc and sheet she creates, Linear is unscoped and she is on the "
                          "ART team, and she replies in a channel she is in."),
            "artifact": "04_Prompt.txt", "artifact_hash": h, "persona_role": "Art Lead", "source_ids": ROLE_SOURCES}
    p.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    print("evidence:", stage, "bound to", (data["outcome_reviews"][stage]["artifact"], data["outcome_reviews"][stage]["artifact_hash"]))


if __name__ == "__main__":
    main()

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
    "Plan doc: a new Google Doc owned by claire.morgan@harmonygames.co (any title naming Halloween or the plan, any folder of hers or Leonard's d_272d849cde40c35980a433), shared with the six review attendees of evt_d947bf7cd910549b674b1f (leonard.hayes, frederick.stone, martin.walsh, marcus.bennett, robert, arthur.blake @harmonygames.co) as commenter or writer, extra harmonygames.co people allowed; it gives calls by surface type, store and icon pieces by the Thu Oct 16 12:00 PT merge cut, ads with Frederick by Wed Oct 15, Android-US-tablet-only ads skipped, reuse of the two cheer fastcouch cuts, the iPhone 6.5\" and Play sets and the owned KayKit Halloween Bits pack (no purchase), owners Martin (icon, store, stills) and Marcus (video, end cards); any wording and structure",
    "Tracker: a separate new spreadsheet owned by Claire whose title names Halloween, shared with the same six; exactly the 62 serving surfaces of solver/truth.json (no Archive row), keyed by the sheet's or the ticket title's creative name; call HALLOWEEN VERSION 16 / REFRESH FIRST 34 / REUSE 4 / SKIP 8 in any case ('Skip October' = Skip); owner Martin Walsh or Marcus Bennett by the ask's split (Skip rows may be blank); due Wed Oct 15 (or earlier) for ads that need new work, Oct 15 or 'already made' with no date for Reuse ads, blank for Skip, by Thu Oct 16 12:00 PT (or earlier) for the icon and the iPad set, Oct 16 or blank for the iPhone set, blank / 'any day' / any date before Oct 18 for the Play set; any column names, order, extra columns, date format, Pacific or UTC day",
    "Ticket comments: one comment on each of the 58 serving library tickets ART-793 ... ART-854 (none needed on ART-836 ... ART-839) with that ad's call and due date (Skip: no date); any wording, a reason may be added, a second comment allowed; setting the ticket's due-date field is allowed in addition, never instead",
    "Assignments: exactly the 48 Halloween version / Refresh first ad tickets get their maker (42 Marcus Bennett usr_c77c50cc15c5342d, 6 Martin Walsh usr_51f5f16d46e8cf55), by id, name or email; the 2 Reuse and 8 Skip ad tickets stay unassigned",
    "New store-art tickets in Linear team ART: the Halloween app icon and the Halloween iPad 12.9\" set (one ticket each, or one ticket naming both); owner Martin, a due date by the Oct 16 cut and a description are optional; no ticket for the reused iPhone or Play sets",
    "Reply: a thread reply under C06DJBJL798/1759269913.882683 carrying both links (doc and tracker); also sending it to the channel is allowed; a summary may be added",
]
ALTERNATIVES = [
    "The app icon as Reuse of Martin's Sep 17 concept C08R8CHB0QL/1758121809.236839 (no icon ticket): rejected, Robert's thread reply C08R8CHB0QL/1758127951.679146 turns it down for the app icon; the icon is a Halloween version (revision 03 fix PW1)",
    "The icon around Oct 24 (Leonard's question): rejected, Arthur's calendar f_fdd6d2d2f4a4d2f5b908fb merges anything that ships in the build by Thu Oct 16 12:00 PT and lists the icon in the Nov 6 clean-up",
    "Only the sheet's rows as scope: rejected, Frederick's Trello comment 68dc65a0f2d7fb28743f5860 (Julia's 4:5 static) and his note cmt_art831_2 on ART-831 (still running, not on the sheet yet) add two serving creatives (revision 03 fix PW2 for the end card)",
    "The four archived creatives as Skip rows: rejected, the Read me moves paused creatives to Archive and the ask scopes 'everything that's live today'",
    "Ads due Fri Oct 17 on four campaigns (Sep 12 draft): rejected, the Sep 30 changes mail is newer and says Wed Oct 15, not the 17th, and ends the Android US tablet campaign Oct 12",
    "Skip every cut that touches the Android US tablet campaign: rejected, the mail skips only what runs nothing but that campaign; couch alpha 50 16:9 (cmt_art823_1) and balloons alpha 50 (1) 16:9 (cmt_art854_2) also run on iOS UK tablet",
    "Reuse for every cheer fastcouch export, the 4:5 too: rejected, Marcus's reply D05V2N6PZNU/1759166437.080255 names both 9:16 and 16:9 and UA masters holds those two only",
    "Buy the quoted Halloween Bits bundle: rejected, the sender is KayKit's founder (contact 6b350edd259a8b4499a9e625) and the pack is already in the match3d repo ('we have the Halloween pack', C0880U9751A/1738109783.735889)",
    "Reuse ads assigned to their maker: rejected, the ask assigns 'the ones that need new work'",
    "Reuse ads with no due date in the comment and tracker: accepted alongside Wed Oct 15 (nothing left to make; the mail's 'every Halloween ad needs to be with me by Wed Oct 15' supports either)",
    "The tracker as a table inside the plan doc, or the reply as a top-level post / DM: rejected, the ask and the prompt ask for a plan doc plus a tracker and a reply in Leonard's thread",
    "Share view-only: rejected, the ask says 'a plan doc we can comment on' and the prompt 'so they can comment'; commenter or writer accepted",
]
ROLE_SOURCES = ["slack:C06DJBJL798/1759269913.882683", "gcal:evt_d947bf7cd910549b674b1f", "slack:C08R8CHB0QL/1758121809.236839",
                "slack:C08R8CHB0QL/1758127951.679146", "slack:C08R8CHB0QL/1759245641.309714", "slack:D05V2N6PZNU/1759166437.080255",
                "slack:C06DJBJL798/1756914854.743319", "gsheets:f_02b1968f5e882366fbb883", "gdocs:f_fdd6d2d2f4a4d2f5b908fb",
                "gslides:f_5ebf55ad29e815d46243c8",
                "gmail:claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>",
                "linear:ART-793", "linear:ART-831", "trello:68dc65a0f2d7fb28743f5860"]


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
                          "on each serving ad ticket, the maker assignments, the new store-art tickets and the thread reply. "
                          "Each strongest alternative was tested against the record that settles it (Robert's reply, Arthur's "
                          "calendar, Frederick's changes mail, his Trello comment and ART-831 note, Marcus's IM reply, the "
                          "KayKit contact); two forks found while writing the brief were fixed upstream (revision 03); "
                          "representational variants and the Reuse due-date reading are accepted in §4b."),
            "artifact": "04_Prompt_Writing_Brief.md", "artifact_hash": file_digest(WF / "04_Prompt_Writing_Brief.md"),
            "accepted_outcomes": ACCEPTED, "alternatives_considered": ALTERNATIVES}
    else:
        h = file_digest(TASK / "04_Prompt.txt")
        data["outcome_reviews"]["prompt-check"] = {
            "reviewer": "Claude (build lane), prompt-check stage",
            "rationale": ("Checked 04_Prompt.txt against the brief: each deliverable has one destination the persona knows "
                          "(her Drive, everyone on Thursday's review, each ad's ART ticket, ART for new store art, Leonard's "
                          "thread); the strongest alternative per deliverable is settled by a dated record (revision 03 fixes "
                          "included) or accepted as representational (§4b)."),
            "artifact": "04_Prompt.txt", "artifact_hash": h,
            "accepted_outcomes": ACCEPTED, "alternatives_considered": ALTERNATIVES}
        data["role_reviews"]["prompt-check"] = {
            "reviewer": "Claude (build lane), prompt-check stage",
            "rationale": ("Claire Morgan is the Art Lead whose artists make Zombie Match 3D's marketing art (Martin Walsh: icon, "
                          "store screens, stills; Marcus Bennett: UA video and end cards) and who already reacted to Martin's "
                          "Halloween icon concept in #zombie-art. Leonard, the CEO, asked her by name in #zombie_marketing to own "
                          "the art side of the Halloween push and put her on Thursday's review to walk the team through it. "
                          "Delegating to an assistant the per-surface Halloween calls, makers and dates, a plan doc and tracker "
                          "in her own Drive, the follow-through on the ART library tickets and the reply in Leonard's thread is "
                          "her own planning and authoring work for a seasonal go-to-market push, inside her remit at the clock: "
                          "every relied-on record is dated before 2025-10-01T00:00Z, every scoped read is visible to her "
                          "(check-sql PASS, base records can-see YES), she owns the doc and sheet she creates, Linear is "
                          "unscoped and she is on the ART team, and she replies in a channel she is in."),
            "artifact": "04_Prompt.txt", "artifact_hash": h, "persona_role": "Art Lead", "source_ids": ROLE_SOURCES}
    p.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    print("evidence:", stage, "bound to", (data["outcome_reviews"][stage]["artifact"], data["outcome_reviews"][stage]["artifact_hash"]))


if __name__ == "__main__":
    main()

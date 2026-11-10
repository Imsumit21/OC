# P4 deep recheck: review_rev7

Pass: P4 (wording). Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut).

**Result: none. 0 findings, 6 of 6 sentences checked.**

## Findings

`DR# | pass | checklist section | quote | record | dimension | severity`

none

## Sentences checked

| # | Sentence | Words | Result |
|---|---|---|---|
| S1 | Frederick messaged me yesterday asking for the live-ops and push calendar for the Zombie Match 3D beta, the four buy weeks that start Monday the 6th. | 26 | Clean |
| S2 | Can you take it on for me? | 7 | Clean |
| S3 | What he wants in it is in his message, and his working rules for building it are in the brief he shared with me. | 24 | Clean |
| S4 | It goes in my live-ops calendar sheet. | 7 | Clean |
| S5 | If a beat ends up held, leave a note on its ticket so the owner picks it up. | 18 | Clean |
| S6 | Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for. | 18 | Clean |

## Topic lines

- **Tool names, MCP, "tool" wording: no finding.** `linear_`, `gmail_`, `slack_`, `MCP` and `tool` all return 0 hits, case-insensitive. None of the 298 names in `catalog.json` appears. The prompt names no service at all.
- **First / then / finally list: no finding.** `First`, `Then` and `Finally` return 0 hits. S6's "Once the sheet's done" is one real dependency, since a sheet cannot be linked before it exists. Nothing prescribes how to investigate.
- **Bolt-on: no finding.** S1 to S3 carry the request and its sources, and S2 has no referent without S1. S4 names the destination. S5 is triggered by the calendar's hold result. S6 is the only sentence that delegates the link and the recommendation, because S3's "what he wants in it" covers contents only. See closest calls 1 and 2.
- **Opaque id or exact timestamp: no finding.** The prompt has neither. "Monday the 6th" is the human-readable start of the span.
- **Named cause (6.7): no finding.** No cause or symptom is stated. The prompt is silent on the Oct 8 release, the Halloween retraction, Brian's date and the leaderboard failure.
- **Trap hint or riddle: no finding.** S5 is the only candidate. "If a beat ends up held" names no beat and adds nothing beyond Frederick's own "if anything is held and until when" (Slack `D05SD5QLG94`, message `bca784379e7dbca9e64e79a64dfefbba`, SQL line 11). It has none of the pointing of K31's "the thing that actually bites us is not on anybody's list".
- **Hidden destination: no finding.** Every place resolves as follows.

| Write | Prompt wording | Resolves to | Why it is not hidden |
|---|---|---|---|
| Calendar | "my live-ops calendar sheet" | Sheet `f_e4a17c90b3d25f6a8c1d73` "ZM3D Beta Live-Ops Calendar", owner Julia (SQL lines 130-133) | Named. "my" rules out `LiveOps Event Calendar.xlsx` and Leonard's `Live Ops Planning.xlsx`. |
| Link | "the calendar ticket" | ZOM-78 "Event Calendar For Zombie Match 3D" | Named in Frederick's own words: "link it on the calendar ticket". His comment `cmt_zom78_1` (author `usr_175c0d7bc72ed244`, frederick.stone) says "Let us use this ticket for the ZM3D beta live-ops calendar ... Link the sheet here when it is ready." (SQL line 191). That also rules out ENG-2240 "Web interface for the liveops calendar". |
| Recommendation | "send Frederick" | Julia and Frederick's DM `D05SD5QLG94`; Julia (`EMPLOYEE_0005_SLACK_ID`) is a member | Recipient named. His message says "send me your recommendation back here". |
| Held-beat note | "its ticket" | ZOM-429 "Leaderboard next session doesn't start without killing the app", Backlog, assignee douglas | Julia cannot name it in advance, because finding the held beat is the task (Eval 1 §1.5). Linear is unscoped, and the ticket's title and description match the failure in Vincent's re-test (Slack `C0880U9751A`, `b5f2955c2e154efc6835946ecfe1758e`, SQL line 19). |
| Reply to Brian (not in the prompt) | none | Julia's copy of Brian's Sep 26 mail, `julia.lawson@harmonygames.co/<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>` (SQL lines 65-72) | See closest call 4. |

- **Audit or compliance form: no finding.** The prompt reads as one person asking for help ("Can you take it on for me?"), close to the passing control "Arthur wants the merge-review stuff sorted before the next push, can you check what's still open and close it out?". It has none of the "reconcile", "classify", "in-scope cohort" or "handoff it requires" register of K1 and K43.
- **If-chain: no finding.** The prompt has one "If", with one condition, one action and no carve-out. K44's failing sentence carries a "not ..." exclusion, an "or" and a hidden destination. The brief's many per-case rules stay in the seeded record, where §2.7 wants them.
- **Staged errors: no finding.** The text is all ASCII, with no misspellings, emoji or broken punctuation.
- **Plain read and LLM voice: no finding.** There are no headings, bullets, bold or polished connectives. Sentence lengths are uneven (26, 7, 24, 7, 18, 18) and the wording has natural shortcuts ("the sheet's done", "take it on", "picks it up"). Spec-sheet register triggers: 0 of 4. "Beat", "held" and "buy weeks" come from Frederick's message and brief. That fits `long_horizon.md`: the agent reads the record to learn the vocabulary.

## Closest calls

These are all no finding, but they are the judgments most worth a second look.

1. **S5 under the deletion test.** Delete S5 and the rest still reads fine, so §1.3.2's literal test is met. I did not call it a bolt-on because §1.2 defines a bolt-on as an unrelated ask, and S5 fires only from the calendar's hold result on the same beats. It also carries a write that no record states, so it has to be in the prompt.
2. **S4 repeats Frederick's message** ("Put it in the calendar sheet in your ZM Live Ops folder"). It is redundant with a record, not unrelated, and §1.5 wants a destination the persona knows to be named.
3. **"the calendar ticket" instead of ZOM-78.** K47's reason was that a person would simply name the place. I read this as a direct name, not an indirection: it is Frederick's own phrase, it matches the ticket title, and QC guidance accepts a natural business name when it is unambiguous.
4. **The reply to Brian is live but unnamed in the prompt.** Confluence `page_season_pass_spec` (`/pages/20/body`) says "locked 24h before each season opens", which gives a lock of Oct 31 00:00 UTC. Brian's "Fri Oct 31, 10:00 Istanbul time" is 07:00 UTC, so it misses by 7 hours. The brief supplies the place ("a reply on the mail where they committed to it") and Brian's mail says "reply on this mail". Julia cannot know about the miss at request time, and naming it would itself hint at the trap, so leaving it to the records is right. Unlike K44, a record leads to it. Whether it can be missed because S5 and S6 list the other writes is a P1 question, not a wording one.

## Limits

- I did not solve the full held set. I checked it only far enough to test "its ticket":
  - The change-request hold route is empty: since Aug 1, reviews on match3d, match3d-backend, liveops and match3d-quests are 103 COMMENTED and 45 APPROVED; there are no change-request timeline events on those repos; and an exact-wording search of the #zombie-prs mirror for Aug-Sep has 0 hits.
  - For a Slack-only failure with no ticket, I ran a keyword scan of five channels (zombie-bugs, zombie-match3d, zombie-ops, zombie-design, executives) over Sep 15-30. It returned 2 hits, both Vincent's Sep 15-16 bug lists, read in excerpt only.
  - If another beat proves held without a ticket, "its ticket" needs re-testing.
- Injection SQL was read only, never executed.

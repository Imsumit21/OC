# Independent red team of the rev4 changes (fallback reviewer)

**Reviewer.** A fresh Claude general-purpose subagent, run 2026-11-05. It searched with `Task_Authoring/tools/hg.py` only, could read the rev3 SQL and the prompt, and had no access to `Working_Files/`, the solver or the brief. It reviewed the six rev4 changes and the EXC purge the way `/injection` and `/prompt` would. REDTEAM_* is unset, so `redteam_review.py --dual` could not run. Its findings are summarized below. Pointers are its own, re-checked where they decide a disposition.

| # | Change | Finding | Base evidence | Severity | Suggested fix |
|---|---|---|---|---|---|
| 1 | VO status | "from March it's on the three of us" no longer says the bill moves. Leonard runs Meta ads on his own card because FB refused the company card. Under the split email's personal-cost clause, a solver could keep the campaign on Leonard's card (Founder), which is a coherent second answer for Paid by and the shares. | slack messages/C09UHHN6PFZ/2025-12.json /3123 ("FB didn't accept SVB credit card so I sacrificed my own") | major | Restore the billing move without the project word |
| 2 | project description + VO status | Under the Done clause, the campaign is "one of us already carries it" (it is on Leonard's card today), or "nothing is left to do". The intended state is Todo/Leonard. | same | major | "Done if one of us pays it himself through May"; plus fix 1 |
| 3 | VO status | "meta is barely billing it" clashes with the costing rule's "what it bills now", which rev4 relies on for $62 over $95. It invites about $0 for the campaign. | ground-rules doc; seeded reply | minor to major | Drop "barely billing" |
| 4 | project description | The clause order puts Canceled ("stays with HG") first. GitHub's org stays HG's until the data is out (Arthur's mail; #winddown keep list), so Canceled is a fair reading. It drops $48 from the total. | slack messages/C0ADGSZKR3R/2026-02.json /190, /187; messages/C05KNDCHAAG/2026-02.json /46 | major | Test who pays first, or "even if HG still owns it" |
| 5 | Jenkins email | Jenkins now runs on Arthur's machine, which invites Done ("one of us carries it") for the build machines. | slack messages/C05433XK267/2026-02.json /95–/129 | minor | Say the boxes stay HG's |
| 6 | layer.ai reply | Owner rivals: Leonard (he cancelled it; the card's "whoever runs it") and Martin Walsh (tagged on the parent). Canceled issues get no assignee under the description. | slack messages/C09UHHN6PFZ/2026-02.json /575, /604, /705 | minor to major | Ask Robert to do it himself; grade the Owner only on the sheet |
| 7 | layer.ai reply | The parent /575 has thread_ts null and reply_count 0. Without an UPDATE the reply is orphaned. | slack messages/C09UHHN6PFZ/2026-02.json /575 | blocker if missing | UPDATE the parent's thread fields at injection |
| 8 | layer.ai reply | "Source art only lives in layer" overclaims: CF's characters are 3D models, and every earlier layer.ai use is ZM. | slack messages/C09UHHN6PFZ/2025-12.json /508, /516; messages/C0880U9751A/2025-02.json /1074, /1182 | minor | "concept art" |
| 9 | layer.ai reply | Robert posts in #prototype at 17:24Z, 14 minutes after a 17:10Z mention, without acknowledging it. | slack messages/C09UHHN6PFZ/2026-02.json /709, /726 | minor | Move it after 19:08Z |
| 10 | layer.ai reply | "access until March 3rd" plus "before then" reads as Mar 3 or Mar 2. | /575 | minor | Rubric accepts by/before Mar 3 |
| 11 | Jenkins email | The Jan 31 us-east-1 deploy also has a Nakama stack, so "just the auth and backend stacks" leaves one out. | slack messages/D04UY3DQJE5/2026-01.json /18–/26 | minor | "just its live stacks" |
| 12 | Jenkins email | Consistent: the Feb 11 liquidation line is hedged; Arthur is on Eastern time, so 04:20Z is "tonight"; $95 to $62 is plausible. | slack messages/C07C2866011/2026-02.json /389, /412, /424 | none | To Robert, cc Leonard |
| 13 | EXC purge | Calm Play stays uniquely HG/Canceled: it is a wholly owned subsidiary, and its Singular org only serves the CF links AppsFlyer replaces. | slack messages/C04UEQVDVB7/2023-11.json /672, 2023-12.json /501; messages/C09UHHN6PFZ/2026-02.json /569, /573 | none | none |
| 14 | ENG-2445 and ENG-2454 notes | No base conflicts; the base has no Linear VO/Meta issue, so the new issue stays needed. | linear data.json (0 hits "VO campaign") | none | none |

**Forks it could not close:**
- Whether Meta accepts a company card. Settled by fix 1, which records Leonard's own statement.
- Assignees on Canceled issues. These are never graded.
- CF owner (Robert or Leonard), DD owner (Leonard or Arthur), and DD support By (Feb 28 or Mar 1). All three are rev3 forks the rev3 `/prompt` scored as settled (brief §4b assignee row; the Trello card's own-deadline rule).

**False difficulty:** none strictly unfair. The Jenkins email's clause decides several money values at once (concentration). The layer.ai reply is fair: Robert is @-mentioned, and it sits under the item's own post.

**Findability guesses** (careful Opus run):
- VO status: likely ("card" search, Robert's deck, #executives).
- Jenkins email: maybe. A co-founder email stands out in a mostly vendor inbox, but its snippet stops in the first paragraph.
- layer.ai reply: unlikely. It needs a "layer.ai" search (plain "layer" is swamped by "player") and a thread open.

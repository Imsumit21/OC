# 00 Route Hunt: every way to reach K3, K1, K5, K4, F (synth-cut, clock Oct 1, 2025)

Analysis only. Tags: [V] checked in base exports or the 30 stored runs; [U] unknown; odds are my judgement for one thorough run, not measured. "Rank" is newest-first position; Slack search was newest-first in 45 of 45 multi-hit results [V]. Ranks use base rows only, so seeded rows push them deeper.
## Facts that change the design
- **Julia is not a member of `#zombie-prs`** (public, 12 members) [V]. Whether a non-member can read it is [U]; 3 stored non-member hits were canvas pseudo-channels, which settles nothing. Plan as if readable.
- **`github_get_pull_request_comments` is the inline endpoint**: it returns `#rc_N` ids. Conversation comments come from `github_get_issue_comments` [V]. This resolves the [U] in Ask_Carriers 2.9, and Hardness_Mastery line 255 labels it wrongly. Stored use: reviews 613, issue comments 135, PR comments 26.
- **Julia's mailbox has no base mail after Sep 17** (304 messages) [V]. Every mail after that date is seeded, so a bare listing shows only forms, K1 and the panel forward.
- **`github_pull_request_read(method=get_review_comments)` worked in J r1** but is not in catalog.json [V]. It is a second inline route.
- **No tool** gives unread threads, mentions or an activity inbox [V, catalog]. `include_activity_messages` and `filter_threads_only` have no stored use.
- **Linear attachments carry no PR mirror**: all 297 ZOM ones have no URL, and `links` is empty [V].
- **Slack mirrors keep the comment in `attachments`, with `text` empty** [V]. Keyword search gave 0 empty-text hits in 764 and never returned `#zombie-prs`. That is confounded by non-membership, so attachment indexing stays [U].
## K3: inline comment on #463 plus its `#zombie-prs` mirror
| # | Route | Odds | Fair change |
|---|---|---|---|
| 1 | `github_get_pull_request_comments(463)` | .35-.45 | None. This is the working path |
| 2 | `github_pull_request_read(get_review_comments)` | .05 | None; same path |
| 3 | `slack_read_thread(C093LEZGF6J, 1758818922.529299)` | .03 | Needs the root ts and channel; no ticket should name either |
| 4 | Filter-only search with `filter_in_channel` = `#zombie-prs` | .03 | A Sep 30 16:30+ date is rank <=39, page 1. Sep 27-29 is rank about 94, page 2. Needs an earlier ticket close (below) |
| 5 | Keyword search on Samsung or device words hitting the mirror | .05 [U] | Test it live; do not add the word to any `text` field |
| 6 | `github_search_pull_requests` with `in:comments` | ~0 | `"not tiers" in:comments` returned 0, and `tiers in:comments` omitted #271, which holds an inline `not tiers` [V]. Keep it inline; a conversation comment would be searchable |
| 7 | `get_pull_request`, timeline, reviews | 0 text | No inline count field; `reviewed` events are empty [V]. Don't add a review row: it needs its own mirror and is a new row |
| 8 | GitHub notification mail (INT-12), Linear attachment | 0 if unseeded | Both optional. Don't seed, and don't @-mention Julia |

- **Biggest leak is not a tool, it's who reviewed.** #463 has one human review: Owen Baker, APPROVED, empty body [V]. A ticket citing a QA owner's notes makes `reviews(463)` look empty if that owner is someone else, and the natural next call is route 1.
- **Fix:** make Owen the person whose pass the ticket cites. His approval then satisfies the read, with no new row. He is a Game Engineer, not QA [V], so call him the engineer who ran the pass, not QA owner.
- **Date:** the ID floor puts a new ticket after Sep 30 16:26Z, which puts the comment and mirror at the top of the feed. One out-of-order ticket close around Sep 26 allows a Sep 27-29 comment (base tolerates a few), or host the citation on an existing Done ticket. Keep the mirror non-broadcast (0 % for comments), so it never enters `#zombie-prs` history.
- Base mirrored 0 of 2 human match3d comments [V]; INT-01 still applies, so keep the mirror.
## K1: mail among routine form mails
| # | Route | Odds | Fair change |
|---|---|---|---|
| 1 | `gmail_search_messages after:2025/09/2x`, or `gmail_list_messages` / `list_threads` | .45 list, .25 opened | Listing can't be closed and shouldn't be: this is the working path. Give it an ordinary subject, no fact in the subject or first lines |
| 2 | `playtest OR beta`, `session`, `form` search matching K1 | .70 if any word is shared | Keep all these words, plus the section 2 coaching terms, out of subject and body. Refer to the gathering by host and day. Run the collision test on body text, as Gmail search matches bodies |
| 3 | `get_messages_batch` on every form hit | .50 if K1 is in the hit set | Closed by row 2's vocabulary. Tickets already carry the form date, so no required fact sends a run into the mail |
| 4 | `from:<host>` | .20 | Keep. The careful route: 13 sessions, one host, one date is visible in the log |
| 5 | Slack mail notice (INT-22), `gmail_list_drafts`, attachment | 0 | Optional or unreadable; don't seed |

- Odds of opening K1 fall from about .75 to about .40 only if the vocabulary fix holds. Volume won't do it: about 17 mails on one page, with no paging.
- **Keep K1 a separate thread**, not a reply in the form thread (57 % against 33 % missed).
## K5: thread reply under an unnamed parent in `#zombie-design`
| # | Route | Odds | Fair change |
|---|---|---|---|
| 1 | `slack_read_channel`, spot `reply_count`, `slack_read_thread` | .35 | Working path; 19 window threads, so opening all is 19 calls |
| 2 | Search the build id from the forms | .35 | See below. Largest leak |
| 3 | `#builds` Jenkins post shows the id is not a store build | .25 | Bypasses K5 entirely. Use an id whose base posts don't label it dev, or accept two fair paths and rate K5 accordingly |
| 4 | `filter_users_from` the author | .15 | Author sets the rank (below) |
| 5 | `filter_threads_only` + `filter_in_channel` | .05 | Sep 25 is rank 56+, Sep 24 rank 64+: page 2. Fine |
| 6 | `filter_date_on` the day | .03 | Sep 24 has 239 visible messages, Sep 25 has 139. Never Sep 27 or 28 (13 and 16) |

- **Author.** Rank at Sep 25 in the author's feed: Vincent 17, Arthur 10, Marcus 38 (all page 1); Leonard 69 (page 2, but 39 with the channel filter); Robert 287 (page 6). Use Robert, or Leonard as second choice. He also holds F, but in a different container and date.
- **Parent.** Root #3 "kick of joy" holds real friend feedback and Julia's quote, so anyone reading friend reactions opens it. Better: Robert's "New Item Thread" `1758757016.553559` (Sep 24 23:36Z, 13 replies, 90 parents after it). A build mention is plausible in a new-items thread and needs no new row, but I did not read its replies, so check that it fits.
- **Build id.** If only K5's batch shows an odd id, the odd id is the pointer. Sessions should carry two or three ordinary ids in the existing form field, so the id alone isn't a flag.
- Bump `reply_count`, `reply_users_count` and `latest_reply`, or the marker lies. The marker is also the fair signal.
## K4: Turkish line in the Julia-Brian DM
| # | Route | Odds | Fair change |
|---|---|---|---|
| 1 | `slack_read_channel(D076RBM29JS)` | .40 | Working path. All 37 window messages fit one page, so K4 is page 1 |
| 2 | `filter_users_from` Brian, or `from:` query | .15 | Stored runs used this filter 0 of 7 and `from:` in only 4 queries, but the blind plan names it. Sep 23 onward is rank <=49, page 1; only before Sep 22 19:47Z is rank 52, page 2 |
| 3 | `filter_in_im_or_mpim` or `filter_users_with` Brian | .05 | Same as route 1 |
| 4 | Keyword search | .05 | Keep English loanwords out: test, beta, playtest, build, RPG, casual, session, tester. Base has `oyun` once, not in this DM [V]. Name the batch by a Turkish day or group word, not a label copied from the form |
| 5 | `gdrive_list_recent_files`, gdocs search | 0 text | Finds Brian's form Doc only: a pointer to Brian, which is fair. No DM copy, no Doc comment |

- **The DM's real activity is Sep 23 (23 messages) and Sep 29 (14)** [V]. A Sep 29 line is rank <=14 and top of page 1. Prefer late Sep 23, inside the real conversation. A Sep 22 date buys one page of margin, but needs Brian's form dated earlier that same day and sits in a silent stretch; I wouldn't pay that.
- **Base hook `1758570425.654109` sits in `#zombie-design`, not this DM** [V]. Don't cite it as K4's DM anchor. The DM has no Sep 22 messages [V].
- The export lists 5 members on this IM (Julia, Brian, 3 aliases) [V]; 37 of 37 window messages are from the two of them.
## F: Robert's reply
| # | Route | Odds | Fair change |
|---|---|---|---|
| 1 | Search on the delegated topic | .55 | Keep: the seeded ask delegates to Robert, so one sensible query must hit. Avoid words shared with K4 or K5 |
| 2 | `filter_in_im_or_mpim` Robert + `filter_threads_only` | .10 | Only 11 replies in the window: one call. Keep as the fair fallback |
| 3 | `slack_read_channel(D05GU6L0XFH)` + thread | .10 | Root #1 is 253 parents back, root #2 is 106. Prefer #1, but both rely on route 1 for fairness |
| 4 | `from:robert after:...` | .10 | J r2 ran this exact shape and it spilled at 55,973 chars. Sep 26 is rank 255: page 6 |
## Calls that reveal two or more records
| Call | Reveals | Fix |
|---|---|---|
| One shared word in `slack_search_public_and_private` | K5 + F, or K4 + F | Disjoint vocabulary across the three; test all blind queries |
| `from:robert` feed if K5 and F are close in date | K5 + F | K5 Sep 25, F Sep 26; both are past page 5 |
| `filter_date_on` one day | Any two on the same day | One record per day: K4 Sep 23, K5 Sep 25, F Sep 26 (384 messages) |
| `filter_threads_only`, date floor, no channel | K5 + F (+ mirror if readable) | 199 replies after Sep 25: page 4+. Used 0 times in stored runs |
| Bare Gmail listing | K1 + panel forward | Only one is hidden; acceptable |

No call reaches K3's inline text together with any other record.
## Ranking after fixes (surfaced in a thorough run; judgement)
1. **F** about .70, easiest, and it should be: it is a delegated obligation.
2. **K4** about .45 surfaced, about .40 applied (join by the form's "work friends" field).
3. **K1** about .40, or .75 if the vocabulary leaks.
4. **K5** about .40, or .55 if build ids stay distinctive.
5. **K3** about .35-.40, hardest, and one direct call away from any run that opens the right endpoint.

K3's .60-.65 miss matches the wall prior of .65, but one direct call beats it. It can still fail 6 of 6; don't count on that.
## Where this crosses the line
- **Unfair:** K5 by both removing build ids from forms and hiding the reply; there would then be no join. Keep the id on the form.
- **Unfair:** K1 with no host and day reference. Vocabulary removal has to stop before the mail stops being clearly about those sessions.
- **Unfair:** depending on Julia's `#zombie-prs` read or on the mirror missing search. Neither is load-bearing here; K3's path is GitHub only.
- **Unfair:** F without the delegation chain (review M1), or with wording no topic query can hit.
- **Risky:** the ticket must imply review text, or a K3 miss earns no credit. "Pass noted on the PR" is fine; a bare PR link isn't.
- **Risky:** Owen as a QA pass holder must not contradict base roles or SC cards. Check before seeding.
- **Risky:** the out-of-order ticket counts against the base's few tolerated rows; `/injection` must accept it.
- **Not tested:** K1, K5, K4 and F wording, because no seeded text exists yet. Re-run all blind queries on final seeds, plus one live check of attachment search and non-member reads.

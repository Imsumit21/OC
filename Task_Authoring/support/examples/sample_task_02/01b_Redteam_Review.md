## Bottom line

**The 491 Linear comment reads are plausible under the stated no-bulk contract. The “565 honest calls, floor 565, zero conditional” claim is not established.** More importantly, the supplied delegation chain does not establish that the **424-ticket change list is part of the anchored assignment**.

The design’s main weakness is not missing volume; it is that most added volume is straightforward transcription from seeded, per-ticket conclusions.

## 1. Shortcuts and answer leakage

- **Both cohorts, tiers and grouping are bulk-computable.** `linear_list_issues` returns state, labels, priority, `parent_id`, relations and descriptions. ENG-2280/ENG-2128 folding does not require individual issue reads. Neither does excluding ENG-1411/1877, ART-695/696 or EPI-25.
- **The PR-comment challenge has collapsed to Slack enumeration.** The seven decisive comment-only references—including backend#79, match3d#527/#542 and GameOfDominoes#1907—have GitHub-app copies. One channel/date sweep substitutes for the intended PR-by-PR examination. This is correctly acknowledged in §16.
- **Authority discovery remains nearly direct.** Dossier §1.D documents unique or nearly unique terms:
  - Trello’s only 2026 card activity identifies `698e523f59165a3daa4028f5`.
  - Sheets search identifies `f_5a83f7de3271d0ddcb28b5`.
  - Calendar “technical intake cut-off” identifies Arthur’s current event.
  - Gmail “change list” identifies K14.
  
  Sharing a term with a decoy **in another service** does not meaningfully contaminate these service-specific searches.
- **Whole-container reads discharge several supposed discoveries simultaneously.** H1’s two messages arrive in one thread fetch; H3’s Index and Notes can arrive together; one Trello comments fetch returns Robert’s amendment and Arthur’s acceptance. Those are not separate amendment hunts.
- **The release-audit notes are seeded answers in prose.**
  - ENG-1852, `cmt_565ae532282401ba19d5`: “Jun 7 store update … still in the current build” directly supplies both output fields.
  - ENG-2292, `cmt_40988e2dfc3a2b06f094`: kept out of every store build directly supplies NOT RELEASED.
  - ENG-2135, `cmt_59103a5a5b44a89995fd`: subsequent updates went out without it directly supplies ROLLED BACK.
  - ENG-2199, `cmt_5a54559f642bd4f0d2bd`: shipped, disabled, then enabled directly supplies RELEASED and its first date.
  
  Avoiding the exact enum strings does not remove conclusion leakage. There is little independent release-history reconciliation.
- **A remaining conditional bulk bypass is not closed:** Dossier §9 leaves `linear_list_issues(query)` matching comment text unverified. Even if results omit comment bodies, query membership can act as an oracle. The small store-date vocabulary and phrases such as “shipped Jul 11,” “backed out,” or “back on” could recover groups of dates/statuses without fetching every comment. This is a risk to test, not a demonstrated complete bypass.
- **Several evidence hunts are unnecessary.** ENG-2277’s positive retest already establishes reproduction; its DM is redundant. ZOM-608’s Regression state settles reproduction. ZOM-359’s report is irrelevant once its fix is excluded by the window. C1’s human claims/retraction need not be read to apply the PR-reference rule.
- **Partial-credit defaults remain strong:** ordinary Linear priority gives most defect tiers; RELEASED gives 344/424 change statuses correctly. These do not solve exact totals, but make most individual rows easy.
- **Contacts is genuinely optional.** H1’s forward already identifies `PERSON_9823`; visiting the CEO lookalike adds no necessary information.

The local `work/*truth.json` files are not demonstrated MCP-accessible sources; they should not be counted as available answer leaks.

## 2. Traps a careful reader defeats cheaply

| Traps | Why they are weak |
|---|---|
| **T1/T1a–c; T17/T17a** | Literal predicates applied to bulk issue fields defeat AB, wrong-team, Regression, May-scope and archive distractors. The Feb 11 audit assignment and H5’s buyer list describe different populations, not an unresolved conflict. |
| **T2** | H2 explicitly specifies parent grouping, maximum severity and parent fix status; bulk `parent_id` supplies the join. ENG-2242’s fix is not required evidence for the parent’s output status. |
| **T3/T3a** | One comments fetch supplies the complete accepted amendment. Vincent’s older launch scale has the wrong issuer and purpose. |
| **T4** | Slack mirrors defeat the per-PR tool-surface trap. |
| **T5** | H1 explicitly requires a merged PR that fixes/addresses the ID. Unmerged branches, unnamed #1876 and “mentions but does not fix” comments are straightforward negative matches. |
| **T6** | ENG-2277’s already-required retest makes the supposedly decisive DM optional. |
| **T8; much of T9** | Both platforms and subsequent corrections now arrive in the **same Linear comment-list response**. “Stop before the later reply” no longer requires overcoming a second retrieval boundary. C8’s description as “two services” is stale. |
| **T10/T10a** | The hub explicitly says the current invite governs. Read the current event; do not investigate PDFs or reconcile stale invitation emails. The final email and invitation are the same Friday version, not three distinct cutoff values. |
| **T11** | The complete H1 thread includes the Web amendment. The asset schedule independently warns that Web belongs to no lot. |
| **T12** | H3 supplies owner-qualified destination information. Robert’s `Technical` is not even the same subfolder name as Arthur’s `04 Technical`. |
| **T13/T13a** | H3 Notes explicitly gives file—not folder—sharing, viewer access, recipient, cc and link-only delivery. The forward eliminates the Contacts ambiguity. |
| **T14/T15** | ENG-2439 explicitly states its end state; the hub explicitly demands recomputed slide totals. Neither a different ticket title nor “19 open bugs” is competing authority. |
| **T16** | A date filter rejects ENG-1866’s and ZOM-359’s old fixes before their comments need examination. |
| **T18/T19** | The re-enable event or actual shipping date is in the same short audit note as the misleading earlier event. This is ordinary complete-sentence reading. |
| **T20** | Aggregating the statuses already extracted is not an independent evidence-discovery mechanism. |
| **T21** | If incorporated, K14 expressly adds `Changes` to the same file. This is an explicit additive amendment, not a difficult conflict. |

**Still substantive:** ZOM-611’s report-between-merges join and ENG-1854’s build-identity check. Those are better mechanisms than the many “read the whole returned record” traps.

## 3. Unique-ground-truth and completeness risks

- **Feature deployment versus binary inclusion is underspecified.** Dossier §13 says ZOM-289 and ZOM-372 have shipped code but a feature flag never enabled. Ground truth gives NOT RELEASED and an empty store-update date. Yet H5 describes the first store update the change “went out in” and status against the build in stores. Binary inclusion and user-visible activation support different answers unless the actual rule expressly distinguishes them. The same problem affects kill-switch ROLLED BACK rows whose code remains present.
- **First update across platforms is unspecified.** H5 asks for one date, while the task explicitly distinguishes iOS and Android elsewhere. No supplied definition resolves staggered store releases, unless every affected note demonstrably establishes a common date.
- **The task clock is not supplied.** Dossier §4 assumes `2026-02-14T00:00Z`; the records require a snapshot after ENG-2440’s creation and the final Feb 13 retests. “At send time” and “in stores now” are not equivalent to a fixed February snapshot without an actual runtime clock contract.
- **The fix-evidence repository universe is not proved complete.** Dossier §8.1 lists seven repositories, including `liveops`, `liveops-dashboard-buddy` and `match3d-quests`. The 73-PR census in Design §15 enumerates only four. Establish that the other three have no qualifying PRs; otherwise NO FIX classifications may omit authorized evidence.
- **Slack mirrors are demonstrably incomplete.** GameOfDominoes#1886#c_2 has no copy, and its base comment is also unmirrored. It happens to be a near-miss, but a solver cannot infer that without reading it. “All decisive seeds are mirrored” is not a discoverable completeness guarantee for the PR corpus.
- **The Slack date sweep uses comment time, while H1 uses merge time.** Comments posted before Oct 13 on PRs merged after Oct 13 would be omitted. No supplied census proves this cannot occur.
- **NO FIX / UNVERIFIED require bounded negative evidence.** H1 permits written reports; the budget searches only Slack for four unresolved tickets. Earlier design text explicitly contemplated Gmail too. The permitted report universe and its completeness are not established.
- **R1 does not exclude archived defects; R15 does.** If Linear defaults to hiding archived issues, the defect census requires an explicit check for archived ENG/ZOM tickets still satisfying R1.
- **Author-side truth inconsistencies remain:**
  - Dossier §8.2 calls Lot A’s reproducing total **34**, but `10+2+10+11 = 33`, also `39−6 = 33`.
  - Design §14 says 12 NOT REPRODUCED rows while listing 13.
  - The claimed shipping-date variant is inconsistent with the prose: 396 RELEASED/ROLLED BACK June-cohort rows must qualify if shipping always follows completion. A total of 412 leaves only 16 qualifying May tickets—not “most” of the 80 May tickets shipping in June.

These arithmetic conflicts need regeneration from actual records, not another narrative assertion that the gates pass.

## 4. Delegation and unauthorized requirements

- **No actual user prompt is supplied.** The material establishes intended incorporation, not that a future prompt actually incorporates A1 and its delegated actions.
- **K14/H5 lacks a demonstrated incoming delegation edge.** Its manifest says `incorporated_via: [A1, K2]`, but neither the described hub nor H1 points to the separate change-list forward. Leonard’s later message referring back to “the defects schedule” does not itself show that an anchor-only assignment incorporates every later related request.
  
  Therefore **R15–R17 and the fourth tab are not established as authorized requirements**. This is the largest issue: 424 of the 565 budgeted calls depend on that extension.
- **Manifest labels cannot supply authority.** K13’s kickoff can validly supply factual build identities; it need not become an instruction source merely because the manifest calls it a requirement. Likewise, H2’s grouping rules need the actual incorporated wording—not just the assertion that they describe normal presentation practice.
- **Resolved, subject to actual prompt incorporation:** K7 authorizes file-level external sharing; K10 explicitly delegates the tracking-ticket end state; the hub explicitly requests slide totals and a Confluence comparison. Those are not inherently unauthorized anymore.

## 5. Feasibility and ACL risks

- **The new essential Slack channels lack a reach proof.** The census verifies bug channels and DMs, not `#zombie-prs` or `#engineering-bots`. Dossier §13’s sample is `C093LEZGF6J`; Arthur’s membership is not shown. If inaccessible, the cheap PR path disappears.
- **Several write-critical behaviors remain `[U]`:** `shared_roles_json`, external `gdrive_share_file`, native Sheets/Drive synchronization, `addSheet`, Gmail address serialization and external-organizer calendar rendering. Gate PASS is not an execution test.
- **ENG’s “In Review” state is not demonstrated.** The supplied natural states include PR and In Validation. Confirm an actual valid state for ENG-2439 rather than relying on a free-text end-state description.
- **Slack attachment rendering matters.** Mirror messages have empty `text`; the entire evidence path depends on search results exposing attachments faithfully. The absence of attachment-only text-search hits does not prove the required filter-only response shape.
- **Comment timestamp behavior remains unverified.** Dossier §9 still marks automatic issue `updated_at` changes `[U]`, despite using them to justify skipped reads.
- **Non-ACL-governed sandbox writes do not establish real permissions.** Arthur’s ownership resolves the destination-folder issue, but writer-role rendering and deck editing still need end-to-end checks.

## 6. Where the call budget collapses—or understates work

- **491 is the defensible candidate per-issue core**, assuming H5 is authorized and comment-search membership cannot substitute. Open and Done cohorts are disjoint, so caching does not eliminate those reads.
- **565 is an execution estimate, not a floor.** Original invitation reads, claim/retraction DMs, optional verification and separate searches for already-returned metadata can be omitted.
- **The four report searches are bulkable.** An OR query over ENG-2400, ZOM-610, ZOM-611 and ZOM-614 can replace four searches, subject to supported query syntax and pagination.
- **Fixed 50-result pages are not shown to be a tool maximum.** Larger supported page sizes reduce the 14-call Slack sweep and issue enumeration. Four tab writes may also be batchable. Test the actual catalog.
- **Done enumeration is undercounted.** At 50/page, the 504 audited non-archived tickets require at least 11 pages, not ten, before unrelated recently updated Done tickets.
- **Sorting by `updatedAt` cannot justify stopping on an old completion.** All 504 notes reset update times to Feb 11–12. The pass is ZOM first, then ENG; descending update order can encounter May ENG completions before relevant ZOM tickets.
- **The six “pre-kickoff” omissions are not all pre-kickoff.** ENG-2440 was created at Feb 13 20:31, after the kickoff. Its absence of comments is not established by the stated timestamp shortcut.
- **Mirror completeness adds omitted work.** At minimum #1886 needs attention if completeness is being certified. Loss of both mirror channels replaces the 14-call sweep with roughly 73 PR-comment reads.
- **Without incorporated H5, approximately 424 calls disappear immediately**, leaving roughly 141 before further savings.
- **Parallelizing the 491 reads reduces latency, not tool-call count.** Conversely, reading superseded decoys merely to encounter every planned trap is padding, not necessary task work.

## 7. Three highest-leverage changes

1. **Replace release-audit conclusions with deterministic event joins.** Keep the existing tickets and call count, but make notes supply build/commit or deployment-event references rather than “still in current build.” Join those to an authoritative release history to determine first shipment, rollback and re-enable status. ENG-2135, ENG-2199 and ZOM-210 are natural cases. Explicitly resolve feature activation versus binary inclusion and platform timing.

2. **Expand interacting defect cases within the existing evidence responses.** Use more ZOM-611/ENG-1854-style combinations: qualifying versus wrong-build retests, corrections affecting only one platform, reports around multiple fixes, and children with different tier/fix/retest implications. Keep deterministic precedence and all necessary facts observable. This increases reasoning difficulty without adding read-only filler.

3. **Make authority selection a real same-service scope/version join.** The current unique-term searches and cross-service decoys are too easy. Use a small number of genuinely adjacent, same-issuer artifacts distinguished by explicit lot, purpose or effective scope, with narrow amendments rather than conspicuously obsolete alternatives. **First establish the actual A1→H5 incorporation edge.** Difficulty should come from applying the correct scoped amendment—not uncertainty about whether the change list is authorized.


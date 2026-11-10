# Base records for Oracle Events (task_inputsN2)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Source `hg4-synth-sep30cut` v16. Persona: Claire Morgan, Art Lead (`claire_morgan`, Slack `EMPLOYEE_0009_SLACK_ID`).

## How to read this

- Every quote below is generated from the JSON returned by `hg.py search`, never retyped. Keep Slack mention tokens, `[PERSON_NAME_*]` placeholders, curly apostrophes (U+2019) and HTML entities such as `&amp;` exactly as shown.
- Slack paths are relative to `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/`. Trello and Linear paths are `data.json` under their service folders. Pacific is America/Los_Angeles (PDT on every date here).
- Placeholder identities: Trello card 68768a1501ae552dbee94b8a has name `Marketing Video Refresh (Marcus/[PERSON_NAME_0036])` and URL slug `45-marketing-video-refresh-marcus.bennett-frederick.stone`, so `[PERSON_NAME_0036]` is Frederick Stone. The unfurl in item 3 has `author_id` `EMPLOYEE_0016_SLACK_ID` (Robert) with `author_name` `[PERSON_NAME_0055]` and fallback name `[PERSON_NAME_0054]`, so both tokens read as Robert. That is inference from tokens, so quote the token, not the name.

### Scope notes

- Reads went through `hg.py search` (`lookup`, `search-many`, `get`, `get-many`) and `persona_view.py`. No SQL was executed and git was not run.
- Linear reads went slightly past the brief, in three places. The user lookup also returned Claire Morgan (`/users/17`). The contiguous read of `/issues/578`-`/issues/593` also returned array neighbours ART-78, ART-95 and ART-96. The state pass used a `state_id` lookup over all teams and then kept only ART pointers. `ART-793`-`ART-1199` were checked on `identifier` only. No comments, projects or other teams' tickets were opened.
- Because Linear reads were limited, creator id `usr_175c0d7bc72ed244` (on ART-774/790/792 and on the overlay ART rows) was not resolved to a person.

## 1. Aug 13 "30 s cut" thread in #zombie_marketing

Coverage: `lookup --key thread_ts` over all 4,840 message files, `scan_complete` true, returned the parent and 15 replies, matching `reply_count` 15.

### Lines to quote

Baked-in line (parent, Frederick Stone):

```text
Here's a 30 second cut for UA. I can't really cut and paste different video segments as the background music is baked in. But if this performs well compared to our current ads, we should iterate with different RPG elements.
```

No-music lines, in order:

- `/24` Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`): `any easy way to remove the backend music <@EMPLOYEE_0002_SLACK_ID>?`
- `/25` Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`): `one lesson is to specifically record all our in-game videos with SFX but without music baked in it sounds like`
- `/28` Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`): `I can get back to the office and 3xport it without the music but with the fx intact`
- `/30` Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`): `I think [PERSON_NAME_0036] can start with this video and we’ll do others without music so that we can do different cuts`
- `/33` Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`): `<@EMPLOYEE_0038_SLACK_ID> <@EMPLOYEE_0008_SLACK_ID> Two variants, one with no music but with sfx, and another one with no music but with sfx and no video transitions (just cuts between the scenes)`

### Which creatives it covers

- The thread names one UA creative: the file on the parent, `marcus.bennett_9-16_blur-VEED.mp4` (`F09AMU1LSN5`, 30,030 ms, 9:16). Overlay ART-809 `marcus.bennett 9:16 (9:16 video)` points here. Its comment gives no master type and defers to this thread: `Captured from Android #1630 on Aug 13. Master notes are in Frederick's Aug 13 thread in #zombie_marketing. Unity: iOS UK phone, Android US phone.`
- The baked-in statement is about that cut only.
- The no-music exports are not of that cut. Marcus attached two zips of the investor video, `InvestorFacing_Seq3_NoMusic.zip` (`F09A3UM7F43`) and `InvestorFacing_Seq3_NoMusic_NoTransitions.zip` (`F09A9NUF3RQ`). By name they are variants of `InvestorFacing_Seq3.zip` (`F09AATG5BTQ`, channel post `/21`), which is the source video, not the 30 s cut.
- Leonard frames them as material for later work: `I think [PERSON_NAME_0036] can start with this video and we’ll do others without music so that we can do different cuts`.
- The thread never says the 9:16 was re-cut from a no-music file, and it never mentions 16:9, 4:5 or 1:1. Overlay ART-817/818/819 carry their own `Master: SFX only, no music.`, so the thread determines ART-809 alone.

**Risk for the OE:** a reader could fairly take `Two variants, one with no music but with sfx` as a no-music master for ART-809 itself. The evidence that it is not rests on the zip names and on the parent's baked-in line. The OE should state that reasoning rather than treat it as self-evident.

### Records

#### `C06DJBJL798/1755110573.319349` (channel post just before the thread, not part of it)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/21`. Message id: `394789823fe584a898a402b165bb5878`.
- Author: Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
- Time: 2025-08-13 18:42:53.319349 UTC | Wed 2025-08-13 11:42:53.319349 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: 
  - `F09AATG5BTQ` name `InvestorFacing_Seq3.zip`, title `InvestorFacing_Seq3.zip`, zip, 566545691 bytes, uploader Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)

Verbatim text:

```text
<@EMPLOYEE_0008_SLACK_ID> <@EMPLOYEE_0038_SLACK_ID> Investor Facing Video. Final version :slightly_smiling_face:
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755110573.319349: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755114007.441789` (parent)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/22`. Message id: `10f56448f20117fae02a355d9c553a58`.
- Author: Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)
- Time: 2025-08-13 19:40:07.441789 UTC | Wed 2025-08-13 12:40:07.441789 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 15, reply_users_count 4, latest_reply `1755119208.328719`
- Reactions: :+1: x1 (Robert (`EMPLOYEE_0016_SLACK_ID`)); :heart: x1 (Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`))
- Files: 
  - `F09AMU1LSN5` name `marcus.bennett_9-16_blur-VEED.mp4`, title `[USERNAME_34876]-VEED.mp4`, mp4, 30030 ms, 15693882 bytes, uploader Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)

Verbatim text:

```text
Here's a 30 second cut for UA. I can't really cut and paste different video segments as the background music is baked in. But if this performs well compared to our current ads, we should iterate with different RPG elements.
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755114007.441789: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755116175.203269` (reply 1 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/23`. Message id: `61bc4a79e497534c2aad339ce17ced18`.
- Author: Robert (`EMPLOYEE_0016_SLACK_ID`)
- Time: 2025-08-13 20:16:15.203269 UTC | Wed 2025-08-13 13:16:15.203269 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Damn it cuts fast
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755116175.203269: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755116729.872799` (reply 2 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/24`. Message id: `df95f3c027cc5490275c0fd6232b3e1b`.
- Author: Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
- Time: 2025-08-13 20:25:29.872799 UTC | Wed 2025-08-13 13:25:29.872799 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
any easy way to remove the backend music <@EMPLOYEE_0002_SLACK_ID>?
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755116729.872799: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755116786.755519` (reply 3 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/25`. Message id: `d77f71df6645ea3c999f20f4e7eb7274`.
- Author: Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
- Time: 2025-08-13 20:26:26.755519 UTC | Wed 2025-08-13 13:26:26.755519 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
one lesson is to specifically record all our in-game videos with SFX but without music baked in it sounds like
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755116786.755519: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755116797.214309` (reply 4 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/26`. Message id: `f518f520464c2ffb89eeb72aafec1cae`.
- Author: Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
- Time: 2025-08-13 20:26:37.214309 UTC | Wed 2025-08-13 13:26:37.214309 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
this is likely my/[PERSON_NAME_0036]’s fault
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755116797.214309: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755117445.981559` (reply 5 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/27`. Message id: `e76715f38af913734a718e2fa4a7c6aa`.
- Author: Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
- Time: 2025-08-13 20:37:25.981559 UTC | Wed 2025-08-13 13:37:25.981559 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Music separated track
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755117445.981559: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755117466.265859` (reply 6 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/28`. Message id: `a51797264526f26bc53945cd2fd4a388`.
- Author: Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
- Time: 2025-08-13 20:37:46.265859 UTC | Wed 2025-08-13 13:37:46.265859 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :partying_face: x1 (Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`))
- Files: none

Verbatim text:

```text
I can get back to the office and 3xport it without the music but with the fx intact
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755117466.265859: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755117508.640379` (reply 7 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/29`. Message id: `b947b8df1c18860ea8f5db8967ce005e`.
- Author: Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
- Time: 2025-08-13 20:38:28.640379 UTC | Wed 2025-08-13 13:38:28.640379 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
if it’s too late for today please do it tomorrow
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755117508.640379: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755117538.514179` (reply 8 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/30`. Message id: `8889e63be854c8554446d7aacece83d4`.
- Author: Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
- Time: 2025-08-13 20:38:58.514179 UTC | Wed 2025-08-13 13:38:58.514179 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
I think [PERSON_NAME_0036] can start with this video and we’ll do others without music so that we can do different cuts
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755117538.514179: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755117547.496169` (reply 9 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/31`. Message id: `d7074b11ad1bddd9a0404bf08e613b37`.
- Author: Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
- Time: 2025-08-13 20:39:07.496169 UTC | Wed 2025-08-13 13:39:07.496169 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :pray: x1 (Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`))
- Files: none

Verbatim text:

```text
hands look good, thank you!!!
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755117547.496169: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755117586.513579` (reply 10 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/32`. Message id: `9c64c5675a4e14feabbde7578fd3a251`.
- Author: Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
- Time: 2025-08-13 20:39:46.513579 UTC | Wed 2025-08-13 13:39:46.513579 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
It takes me 6 min lol or so. I'm already in the office.
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755117586.513579: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755118817.302199` (reply 11 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/33`. Message id: `2951a78f9c48fa95d8bd740426e083ff`.
- Author: Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
- Time: 2025-08-13 21:00:17.302199 UTC | Wed 2025-08-13 14:00:17.302199 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :heart: x1 (Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`))
- Files: 
  - `F09A3UM7F43` name `InvestorFacing_Seq3_NoMusic.zip`, title `[USERNAME_43625].zip`, zip, 803597214 bytes, uploader Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
  - `F09A9NUF3RQ` name `InvestorFacing_Seq3_NoMusic_NoTransitions.zip`, title `InvestorFacing_Seq3_NoMusic_NoTransitions.zip`, zip, 632895337 bytes, uploader Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)

Verbatim text:

```text
<@EMPLOYEE_0038_SLACK_ID> <@EMPLOYEE_0008_SLACK_ID> Two variants, one with no music but with sfx, and another one with no music but with sfx and no video transitions (just cuts between the scenes)
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755118817.302199: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755119139.663979` (reply 12 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/34`. Message id: `2b47ff0a6b138840afe2f82041f91339`.
- Author: Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
- Time: 2025-08-13 21:05:39.663979 UTC | Wed 2025-08-13 14:05:39.663979 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Thank you - <@EMPLOYEE_0008_SLACK_ID> - I think you have what you need now, right?
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755119139.663979: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755119161.298729` (reply 13 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/35`. Message id: `ed1e162b71569d1d371fdf82970338bc`.
- Author: Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)
- Time: 2025-08-13 21:06:01.298729 UTC | Wed 2025-08-13 14:06:01.298729 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
still unzipping
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755119161.298729: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755119181.113009` (reply 14 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/36`. Message id: `2c0ab87b7b6c898de9caf2188d309b44`.
- Author: Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)
- Time: 2025-08-13 21:06:21.113009 UTC | Wed 2025-08-13 14:06:21.113009 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Will probably need the audio file as well -- the background music.
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755119181.113009: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

#### `C06DJBJL798/1755119208.328719` (reply 15 of 15)

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-08.json` `/37`. Message id: `3c3243b9f72b5b218cfb5ea24bdec544`.
- Author: Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
- Time: 2025-08-13 21:06:48.328719 UTC | Wed 2025-08-13 14:06:48.328719 PDT
- Thread fields: thread_ts `1755114007.441789`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :pray: x2 (Frederick Stone (`EMPLOYEE_0008_SLACK_ID`), Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`))
- Files: none

Verbatim text:

```text
the audio i got it from company-internal, [PERSON_NAME_0029] put two songs over There
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1755119208.328719: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

File visibility:

```text
claire_morgan slack F09AMU1LSN5: YES
  reason:   file inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing; metadata only — content not served (Evals/references/persona/acl.md, 2026-10-17)
```
```text
claire_morgan slack F09A3UM7F43: YES
  reason:   file inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing; metadata only — content not served (Evals/references/persona/acl.md, 2026-10-17)
```
```text
claire_morgan slack F09A9NUF3RQ: YES
  reason:   file inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing; metadata only — content not served (Evals/references/persona/acl.md, 2026-10-17)
```
```text
claire_morgan slack F09AATG5BTQ: YES
  reason:   file inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing; metadata only — content not served (Evals/references/persona/acl.md, 2026-10-17)
```

### Related no-music records Claire cannot see

A complete search of all Aug-Sep 2025 message files for `no music`, `without music`, `without the music`, `NoMusic`, `baked in` and file names containing `VEED` found these outside the thread. They are context for you only and must not be load-bearing for Claire.

#### `D05UDNHAPL2/1754491812.803639` (Marcus asks for no-music recordings)

- Service: slack. File + pointer: `messages/D05UDNHAPL2/2025-08.json` `/29`. Message id: `820e8f8af46ce32e97f1705bed0f7224`.
- Author: Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
- Time: 2025-08-06 14:50:12.803639 UTC | Wed 2025-08-06 07:50:12.803639 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
we need the recordings with no music
```

persona_view:

```text
claire_morgan slack D05UDNHAPL2/1754491812.803639: NO
  reason:   message inherits channel: im conversation D05UDNHAPL2: persona EMPLOYEE_0009_SLACK_ID is not a member
```

#### `D05UDNHAPL2/1754492022.836459` (Frederick agrees)

- Service: slack. File + pointer: `messages/D05UDNHAPL2/2025-08.json` `/38`. Message id: `f07b7371a437e00060ed936f2b5b0504`.
- Author: Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)
- Time: 2025-08-06 14:53:42.836459 UTC | Wed 2025-08-06 07:53:42.836459 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
I can re-record without music. But will take awhile. Probably have it done by end of my day today.
```

persona_view:

```text
claire_morgan slack D05UDNHAPL2/1754492022.836459: NO
  reason:   message inherits channel: im conversation D05UDNHAPL2: persona EMPLOYEE_0009_SLACK_ID is not a member
```

#### `D05UDNHAPL2/1754505715.929299` (Frederick shares a no-music Drive subfolder)

- Service: slack. File + pointer: `messages/D05UDNHAPL2/2025-08.json` `/43`. Message id: `62db40a3cfafc720572c259255592ed9`.
- Author: Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)
- Time: 2025-08-06 18:41:55.929299 UTC | Wed 2025-08-06 11:41:55.929299 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :ok_hand: x1 (Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`))
- Files: none

Verbatim text:

```text
Created a subfolder here for no music recordings. <https://drive.google.com/drive/u/0/folders/1LkqJqOQ-fL0gHjh9z22vyP-dkJN9eVHu>
```

persona_view:

```text
claire_morgan slack D05UDNHAPL2/1754505715.929299: NO
  reason:   message inherits channel: im conversation D05UDNHAPL2: persona EMPLOYEE_0009_SLACK_ID is not a member
```

#### `D05UDNHAPL2/1755105510.411229` (Frederick plans the 30 s cuts)

- Service: slack. File + pointer: `messages/D05UDNHAPL2/2025-08.json` `/44`. Message id: `c463da561f77629a3e28581a57f12dee`.
- Author: Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)
- Time: 2025-08-13 17:18:30.411229 UTC | Wed 2025-08-13 10:18:30.411229 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Yo, I'm gonna try to slice up your video for investors to make a few 30 second UA ads. Are you still adding the hand animation?
```

persona_view:

```text
claire_morgan slack D05UDNHAPL2/1755105510.411229: NO
  reason:   message inherits channel: im conversation D05UDNHAPL2: persona EMPLOYEE_0009_SLACK_ID is not a member
```

#### `D05S58U4SAK/1755470278.730069` (same 30,030 ms length as the thread cut, different file name, nothing about music)

- Service: slack. File + pointer: `messages/D05S58U4SAK/2025-08.json` `/55`. Message id: `517f7c92325fedf28858878bccbb9d0d`.
- Author: Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)
- Time: 2025-08-17 22:37:58.730069 UTC | Sun 2025-08-17 15:37:58.730069 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :+1: x1 (Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`))
- Files: 
  - `F09BJBG8J5N` name `marcus_9-16_blur-VEED (1).mp4`, title `[USERNAME_34876]-VEED (1).mp4`, mp4, 30030 ms, 15743738 bytes, uploader Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)

Verbatim text:

```text

```

persona_view:

```text
claire_morgan slack D05S58U4SAK/1755470278.730069: NO
  reason:   message inherits channel: im conversation D05S58U4SAK: persona EMPLOYEE_0009_SLACK_ID is not a member
```

#### `D05S58U4SAK/1755470196.580519` (sibling 30 s cut `alin2`, nothing about music)

- Service: slack. File + pointer: `messages/D05S58U4SAK/2025-08.json` `/54`. Message id: `3bf32718dc123a3862ee29c5caa4ebc4`.
- Author: Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)
- Time: 2025-08-17 22:36:36.580519 UTC | Sun 2025-08-17 15:36:36.580519 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :+1: x1 (Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`))
- Files: 
  - `F09B4C125TK` name `alin2_9-16_blur-VEED (1).mp4`, title `[USERNAME_34875]-VEED (1).mp4`, mp4, 30030 ms, 11116588 bytes, uploader Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)

Verbatim text:

```text

```

persona_view:

```text
claire_morgan slack D05S58U4SAK/1755470196.580519: NO
  reason:   message inherits channel: im conversation D05S58U4SAK: persona EMPLOYEE_0009_SLACK_ID is not a member
```

File visibility:

```text
claire_morgan slack F09BJBG8J5N: NO
  reason:   file inherits channel: im conversation D05S58U4SAK: persona EMPLOYEE_0009_SLACK_ID is not a member; metadata only — content not served (Evals/references/persona/acl.md, 2026-10-17)
```
```text
claire_morgan slack F09B4C125TK: NO
  reason:   file inherits channel: im conversation D05S58U4SAK: persona EMPLOYEE_0009_SLACK_ID is not a member; metadata only — content not served (Evals/references/persona/acl.md, 2026-10-17)
```

## 2. Martin's Sep 17 icon concept in #zombie-art

Base: `reply_count` 0, `thread_ts` null, no replies (complete `thread_ts` lookup). Claire herself reacted (:ghost: and :jack_o_lantern:).

#### `C08R8CHB0QL/1758121809.236839`

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-09.json` `/121`. Message id: `9025d428af1f551a20e303c3acbc545b`.
- Author: Martin Walsh (`EMPLOYEE_0033_SLACK_ID`)
- Time: 2025-09-17 15:10:09.236839 UTC | Wed 2025-09-17 08:10:09.236839 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :heart_eyes: x1 (Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)); :ghost: x2 (Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`), Claire Morgan (`EMPLOYEE_0009_SLACK_ID`)); :jack_o_lantern: x2 (Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`), Claire Morgan (`EMPLOYEE_0009_SLACK_ID`)); :heart: x1 (Julia Lawson (`EMPLOYEE_0005_SLACK_ID`))
- Files: 
  - `F09FN3SLD9T` name `AppIconHalloween.png`, title `AppIconHalloween.png`, png 2048x2048, 3761277 bytes, uploader Martin Walsh (`EMPLOYEE_0033_SLACK_ID`)
  - `F09FN3YJ7D3` name `image 11.png`, title `image 11.png`, png 1921x751, 1002671 bytes, uploader Martin Walsh (`EMPLOYEE_0033_SLACK_ID`)

Verbatim text:

```text
*Halloween theme* for an app icon or an event: <@EMPLOYEE_0016_SLACK_ID> <@EMPLOYEE_0038_SLACK_ID> <@EMPLOYEE_0005_SLACK_ID>
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1758121809.236839: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

File visibility:

```text
claire_morgan slack F09FN3SLD9T: YES
  reason:   file inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art; metadata only — content not served (Evals/references/persona/acl.md, 2026-10-17)
```
```text
claire_morgan slack F09FN3YJ7D3: YES
  reason:   file inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art; metadata only — content not served (Evals/references/persona/acl.md, 2026-10-17)
```

### Seeded reply `C08R8CHB0QL/1758127951.679146` (overlay only)

- Not in base: the `lookup --key ts` over all message files returned no match. Overlay SQL line 27. Id `8ce7e9eec2958c799a1aa11e4249cddd`.
- Author: Robert (`EMPLOYEE_0016_SLACK_ID`). Time: 2025-09-17 16:52:31.679146 UTC | Wed 2025-09-17 09:52:31.679146 PDT.
- Overlay line 29 updates the parent: `thread_ts_legacy` `1758121809.236839`, `reply_count` 1, `reply_users_count` 1, `latest_reply` `1758127951.679146`.

Verbatim overlay text:

```text
Nice for an event, but not for the app icon, it gets too busy at that size. A Halloween icon should stay as simple as the one we have
```

persona_view (UNVERIFIED is expected for an overlay row, and the channel verdict is YES):

```text
claire_morgan slack C08R8CHB0QL/1758127951.679146: UNVERIFIED
  reason:   ts 1758127951.679146 not found in channel C08R8CHB0QL shards (U4); channel verdict YES
```

## 3. Fake-installs thread in #zombie-match3d

| Field | Base | After overlay |
|---|---|---|
| reply_count | 4 | 5 (SQL line 32) |
| latest_reply | `1759248267.162909` | `1759275738.984915` (SQL line 32) |
| reply_users_count | 2 | 2 (not updated; Frederick and Robert already reply) |

Coverage: the `thread_ts` lookup returned the parent plus 4 replies, matching base `reply_count` 4. Pointer `/468` sits between them but is a Linear-bot message in a different thread.

#### `C0880U9751A/1759211437.306779` (parent)

- Service: slack. File + pointer: `messages/C0880U9751A/2025-09.json` `/467`. Message id: `cd68a603aef386cb7ad0f7cf9a363f04`.
- Author: Robert (`EMPLOYEE_0016_SLACK_ID`)
- Time: 2025-09-30 05:50:37.306779 UTC | Mon 2025-09-29 22:50:37.306779 PDT
- Thread fields: thread_ts `1759211437.306779`, reply_count 4, reply_users_count 2, latest_reply `1759248267.162909`
- Reactions: none
- Files: none

Verbatim text:

```text
<@EMPLOYEE_0008_SLACK_ID> Unity is sending us a lot of bot installs or fake installs piloted by "real" people.
```

persona_view:

```text
claire_morgan slack C0880U9751A/1759211437.306779: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
```

The parent also carries an unfurl of a Robert post from #zombie-design (`C090N54TG79`):

- `from_url`: `https://harmonygamesgroup.slack.com/archives/C090N54TG79/p1759207989371869?thread_ts=1759207989.371869&cid=C090N54TG79`
- `author_id` `EMPLOYEE_0016_SLACK_ID`, `author_name` `[PERSON_NAME_0055]`, `ts` `1759207989.371869` (2025-09-30 04:53:09.371869 UTC | Mon 2025-09-29 21:53:09.371869 PDT)

Unfurl `text`:

```text
I looked more at the user logs... I'm 99% certain that we have quite significant number of bots.
```

Unfurl `fallback`:

```text
[September 29th, 2025 9:53 PM] [PERSON_NAME_0054]: I looked more at the user logs... I'm 99% certain that we have quite significant number of bots.
```

Claire can read the unfurl here but cannot open the source post:

```text
claire_morgan slack C090N54TG79/1759207989.371869: NO
  reason:   message inherits channel: private conversation zombie-design: persona EMPLOYEE_0009_SLACK_ID is not a member
```

#### `C0880U9751A/1759240715.635619` (reply 1 of 4)

- Service: slack. File + pointer: `messages/C0880U9751A/2025-09.json` `/469`. Message id: `375880168c67865c5203b23a3a3c7f3d`.
- Author: Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)
- Time: 2025-09-30 13:58:35.635619 UTC | Tue 2025-09-30 06:58:35.635619 PDT
- Thread fields: thread_ts `1759211437.306779`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
1. Both platforms, or one more than the other?
2. I'm not surprised that pubs would do this to juice their CPMs. We get a pretty wide distribution of installs by pub from Unity. Are we able to tie this behavior to a specific subset of pubs? 
```

persona_view:

```text
claire_morgan slack C0880U9751A/1759240715.635619: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
```

#### `C0880U9751A/1759248076.284779` (reply 2 of 4)

- Service: slack. File + pointer: `messages/C0880U9751A/2025-09.json` `/470`. Message id: `2828fa6ae3ff9bc327e76bb13455628e`.
- Author: Robert (`EMPLOYEE_0016_SLACK_ID`)
- Time: 2025-09-30 16:01:16.284779 UTC | Tue 2025-09-30 09:01:16.284779 PDT
- Thread fields: thread_ts `1759211437.306779`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Android
```

persona_view:

```text
claire_morgan slack C0880U9751A/1759248076.284779: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
```

#### `C0880U9751A/1759248130.580729` (reply 3 of 4)

- Service: slack. File + pointer: `messages/C0880U9751A/2025-09.json` `/471`. Message id: `9180eb57544630480cb47d869080ffb0`.
- Author: Robert (`EMPLOYEE_0016_SLACK_ID`)
- Time: 2025-09-30 16:02:10.580729 UTC | Tue 2025-09-30 09:02:10.580729 PDT
- Thread fields: thread_ts `1759211437.306779`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
I didn't look at it by pubs.
```

persona_view:

```text
claire_morgan slack C0880U9751A/1759248130.580729: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
```

#### `C0880U9751A/1759248267.162909` (reply 4 of 4)

- Service: slack. File + pointer: `messages/C0880U9751A/2025-09.json` `/472`. Message id: `46ccc5759c2216f40d9e9ae8c7fd249e`.
- Author: Frederick Stone (`EMPLOYEE_0008_SLACK_ID`)
- Time: 2025-09-30 16:04:27.162909 UTC | Tue 2025-09-30 09:04:27.162909 PDT
- Thread fields: thread_ts `1759211437.306779`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
We are only running the retention campaigns. So it kind of makes sense the fraudsters are showing some piloted engagement.
```

persona_view:

```text
claire_morgan slack C0880U9751A/1759248267.162909: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
```

### Seeded reply (overlay only)

Overlay SQL line 30, Frederick Stone (`EMPLOYEE_0008_SLACK_ID`), 2025-09-30 23:42:18.984915 UTC | Tue 2025-09-30 16:42:18.984915 PDT:

```text
Spoke to our Unity rep about this today. They're putting every new Android creative through manual review for the next few weeks, about 5 days each. So any new ad going on Android US phone has to be with me by Fri Oct 10, not the 15th. iOS UK stays on the 15th.
```

## 4. Leonard's post about Thursday in #company-internal

#### `C05KNDCHAAG/1759279503.256079`

- Service: slack. File + pointer: `messages/C05KNDCHAAG/2025-10.json` `/0`. Message id: `247b1a9ed1507a2ca41ff7477a3a6e67`.
- Author: Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
- Time: 2025-10-01 00:45:03.256079 UTC | Tue 2025-09-30 17:45:03.256079 PDT
- Thread fields: thread_ts `1759279503.256079`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :+1: x5 (Robert (`EMPLOYEE_0016_SLACK_ID`), Claire Morgan (`EMPLOYEE_0009_SLACK_ID`), `EMPLOYEE_0032_SLACK_ID`, Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`), Vincent Parker (`EMPLOYEE_0012_SLACK_ID`)); :saluting_face: x3 (Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`), Julia Lawson (`EMPLOYEE_0005_SLACK_ID`), Brian Foster (`EMPLOYEE_0026_SLACK_ID`))
- Files: none

Verbatim text:

```text
I’m flying to LA to meet with investors and won’t attend internal meeting tomorrow and Thu. I’m flying back home Friday morning so will miss All hands as well.
```

persona_view:

```text
claire_morgan slack C05KNDCHAAG/1759279503.256079: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private company-internal
```

- This is Tue Sep 30 in Pacific but Wed Oct 1 in UTC, so it is stored in the `2025-10.json` shard. It precedes the clock.
- In Leonard's frame `tomorrow` is Wed Oct 1, `Thu` is Oct 2 and `Friday morning` is Oct 3.
- `thread_ts` equals its own ts with `reply_count` 0. The lookup confirms no replies.
- Tension to settle in the OE: this says he `won’t attend internal meeting tomorrow and Thu`, while overlay event `ZM3D Halloween review` (Thu Oct 2) says `I'm in LA Thursday so I'll dial in for this one.` They read as compatible only as a stated exception.

## 5. #builds Android #1452, near miss #1450, Robert's iOS 1232

#### `C05433XK267/1753820674.990309` (Android #1452 result, the requested record)

- Service: slack. File + pointer: `messages/C05433XK267/2025-07.json` `/1672`. Message id: `3af3d6241f322c1d51b7803faf4f6b25`.
- Author: (no `user` value), subtype `bot_message`
- Time: 2025-07-29 20:24:34.990309 UTC | Tue 2025-07-29 13:24:34.990309 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Match3D Android - #1452 - [PERSON_NAME_0054]/ZombieSwap Success after 6 min 0 sec (<http://blake.tplinkdns.com:9009/job/Match3D%20Android/1452/display/redirect|Open>)
No Changes.
```

persona_view:

```text
claire_morgan slack C05433XK267/1753820674.990309: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public builds
```

`text` is empty. The quote is `attachments[0].fallback`, which is identical to `attachments[0].fields[0].value`.

#### `C05433XK267/1753820323.971319` (Android #1452 start)

- Service: slack. File + pointer: `messages/C05433XK267/2025-07.json` `/1671`. Message id: `f15aa93a24f165efaaa3c417a4dce257`.
- Author: (no `user` value), subtype `bot_message`
- Time: 2025-07-29 20:18:43.971319 UTC | Tue 2025-07-29 13:18:43.971319 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Match3D Android - #1452 Started by user [PERSON_NAME_0055] (<http://blake.tplinkdns.com:9009/job/Match3D%20Android/1452/display/redirect|Open>)
```

persona_view:

```text
claire_morgan slack C05433XK267/1753820323.971319: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public builds
```

`text` is empty. The quote is `attachments[0].fallback`, which is identical to `attachments[0].fields[0].value`.

#### `C05433XK267/1753789877.590639` (near miss, Android #1450 result)

- Service: slack. File + pointer: `messages/C05433XK267/2025-07.json` `/1664`. Message id: `a86a85f032a91a42090ece6685a29a43`.
- Author: (no `user` value), subtype `bot_message`
- Time: 2025-07-29 11:51:17.590639 UTC | Tue 2025-07-29 04:51:17.590639 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Match3D Android - #1450 - main Success after 3 min 57 sec (<http://blake.tplinkdns.com:9009/job/Match3D%20Android/1450/display/redirect|Open>)
Match3D Android - #1450 - main Changes:
- New Background and light/reflection rebake [Marcus.[PERSON_NAME_0004]]
```

persona_view:

```text
claire_morgan slack C05433XK267/1753789877.590639: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public builds
```

`text` is empty. The quote is `attachments[0].fallback`, which is identical to `attachments[0].fields[0].value`.

#### `C05433XK267/1753789651.805099` (near miss, Android #1450 start)

- Service: slack. File + pointer: `messages/C05433XK267/2025-07.json` `/1662`. Message id: `ba94f9bc21c3bc147bdd27c60bac116b`.
- Author: (no `user` value), subtype `bot_message`
- Time: 2025-07-29 11:47:31.805099 UTC | Tue 2025-07-29 04:47:31.805099 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Match3D Android - #1450 Started by changes from Marcus.[PERSON_NAME_0004] (16 file(s) changed) (<http://blake.tplinkdns.com:9009/job/Match3D%20Android/1450/display/redirect|Open>)
```

persona_view:

```text
claire_morgan slack C05433XK267/1753789651.805099: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public builds
```

`text` is empty. The quote is `attachments[0].fallback`, which is identical to `attachments[0].fields[0].value`.

#### `C05433XK267/1753820679.865049` (iOS #1232 result, posted 5 s after Android #1452)

- Service: slack. File + pointer: `messages/C05433XK267/2025-07.json` `/1673`. Message id: `97b1dda313beab22e05aaaa1eeee52cf`.
- Author: `SLACK_BOT_0005_SLACK_ID`
- Time: 2025-07-29 20:24:39.865049 UTC | Tue 2025-07-29 13:24:39.865049 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Match 3D iOS Internal - #1232 - [PERSON_NAME_0054]/ZombieSwap Success after 6 min 24 sec (<http://blake.tplinkdns.com:9009/job/Match%203D%20iOS%20Internal/1232/display/redirect|Open>)
No Changes.
```

persona_view:

```text
claire_morgan slack C05433XK267/1753820679.865049: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public builds
```

#### `C0880U9751A/1753820524.488479` (Robert's iOS 1232 post, #zombie-match3d)

- Service: slack. File + pointer: `messages/C0880U9751A/2025-07.json` `/903`. Message id: `394cb840ca860a121848108566e253ae`.
- Author: Robert (`EMPLOYEE_0016_SLACK_ID`)
- Time: 2025-07-29 20:22:04.488479 UTC | Tue 2025-07-29 13:22:04.488479 PDT
- Thread fields: thread_ts `1753820524.488479`, reply_count 1, reply_users_count 1, latest_reply `1753821510.674109`
- Reactions: :+1: x1 (Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`))
- Files: none

Verbatim text:

```text
<@EMPLOYEE_0038_SLACK_ID> iOS build 1232, please give it a go.
• MF 35 levels zombie swap completed with new background
• Up to level 11 can be completed with 50 CPM and 0 win streak
• Up to level 35 can be completed with 60 CPM and 0 win streak, but some levels you WILL take damage, especially level 25+
• Basic monster "punk" (Now called party girl) moves slower, 60 seconds across the battlefield, instead of original 45) this should put "less pressure" on players
• First 35 levels only uses chef boss, mayor boss, party girl, [PERSON_NAME_35423] and mailman. most levels can be completed if you go straight for boss buster. this is similar to MF where most levels end in less than 30 seconds if you just match objectives.
• Try not to blunder, it is still punitive. Currently +100% speed and damage. I'm debating on reducing this to 50-70%
```

persona_view:

```text
claire_morgan slack C0880U9751A/1753820524.488479: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
```

#### `C0880U9751A/1753821510.674109` (the only reply)

- Service: slack. File + pointer: `messages/C0880U9751A/2025-07.json` `/911`. Message id: `0ea59f90ed91f059a382f43429b6d64c`.
- Author: Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
- Time: 2025-07-29 20:38:30.674109 UTC | Tue 2025-07-29 13:38:30.674109 PDT
- Thread fields: thread_ts `1753820524.488479`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
testing shortly
```

persona_view:

```text
claire_morgan slack C0880U9751A/1753821510.674109: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
```

Reading these together:

- #1450 is a `main` build with the change `New Background and light/reflection rebake`. #1452 is a `[PERSON_NAME_0054]/ZombieSwap` branch build with `No Changes.`
- Robert names iOS 1232 only. The `zombie swap completed with new background` claim is in his post, not in any #builds record. Tying it to Android #1452 relies on the shared branch and on #1452 starting 21 s after iOS #1232 (`1753820323.971319` vs `1753820302.497999`).
- Robert posted about 2.5 minutes before Jenkins reported iOS #1232 finished (`1753820524` vs `1753820679`).
- Overlay ART-831 cites `Android #1450 footage (Jul 29)`. Jul 29 holds in both UTC and Pacific for #1450.

## 6. "1.3.38 is out!"

#### `C0880U9751A/1758141269.804779`

- Service: slack. File + pointer: `messages/C0880U9751A/2025-09.json` `/286`. Message id: `bb5668298bc42b5e8ce3de50bfc1db09`.
- Author: Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
- Time: 2025-09-17 20:34:29.804779 UTC | Wed 2025-09-17 13:34:29.804779 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: 
  - `F09FC42QJDV` name `image.png`, title `image.png`, png 3090x1872, 1710538 bytes, uploader Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)

Verbatim text:

```text
1.3.38 is out!
```

persona_view:

```text
claire_morgan slack C0880U9751A/1758141269.804779: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
```

File visibility:

```text
claire_morgan slack F09FC42QJDV: YES
  reason:   file inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d; metadata only — content not served (Evals/references/persona/acl.md, 2026-10-17)
```

## 7. Leonard's Sep 3 export ask

#### `C06DJBJL798/1756914854.743319`

- Service: slack. File + pointer: `messages/C06DJBJL798/2025-09.json` `/0`. Message id: `985d2d8d816cdd742272eec19a321ffc`.
- Author: Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
- Time: 2025-09-03 15:54:14.743319 UTC | Wed 2025-09-03 08:54:14.743319 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
<@EMPLOYEE_0033_SLACK_ID> can you export the app store assets with the right asset size for both iphone/ipad/gp?
```

persona_view:

```text
claire_morgan slack C06DJBJL798/1756914854.743319: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

No replies: `thread_ts` null, `reply_count` 0, and the lookup found nothing.

## 8. Old zombies on the packs

`1754310794.907609` is a reply inside the thread on `1754077274.101399`, not a top-level post, so the parent and the rest of that thread follow it.

#### `C08R8CHB0QL/1754310794.907609` (requested record)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/45`. Message id: `78563407099158b2aea926368d3a3c2d`.
- Author: Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
- Time: 2025-08-04 12:33:14.907609 UTC | Mon 2025-08-04 05:33:14.907609 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :heart: x1 (Julia Lawson (`EMPLOYEE_0005_SLACK_ID`))
- Files: 
  - `F098VNHS1RS` name `EndCard001.mp4`, title `EndCard001.mp4`, mp4, 9242 ms, 113860537 bytes, uploader Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)

Verbatim text:

```text
<@EMPLOYEE_0005_SLACK_ID> <@EMPLOYEE_0033_SLACK_ID> i've replaced the zombie at the you lose screen, now , i would like to change the artwork on the packs as they have the old zombies on it
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754310794.907609: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

File visibility:

```text
claire_morgan slack F098VNHS1RS: YES
  reason:   file inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art; metadata only — content not served (Evals/references/persona/acl.md, 2026-10-17)
```

#### `C08R8CHB0QL/1754316299.381419` (requested record)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/64`. Message id: `387a698e8583d486db1599b61b3d4bc8`.
- Author: Martin Walsh (`EMPLOYEE_0033_SLACK_ID`)
- Time: 2025-08-04 14:04:59.381419 UTC | Mon 2025-08-04 07:04:59.381419 PDT
- Thread fields: thread_ts `1754316299.381419`, reply_count 1, reply_users_count 1, latest_reply `1754322742.581179`
- Reactions: :+1: x3 (`EMPLOYEE_0032_SLACK_ID`, Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`), Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`))
- Files: 
  - `F098W8JDC4U` name `image.png`, title `image.png`, png 1920x1200, 2743240 bytes, uploader Martin Walsh (`EMPLOYEE_0033_SLACK_ID`)

Verbatim text:

```text
<@EMPLOYEE_0016_SLACK_ID> <@EMPLOYEE_0038_SLACK_ID> <@EMPLOYEE_0005_SLACK_ID> I did new packs to replace the old ones. If you guys want something different we need to generate some zombie art and to choose something new. But I think <@EMPLOYEE_0002_SLACK_ID> can replace the existing ones with this ones for now 100%. They are in the items page in Figma.
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754316299.381419: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

File visibility:

```text
claire_morgan slack F098W8JDC4U: YES
  reason:   file inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art; metadata only — content not served (Evals/references/persona/acl.md, 2026-10-17)
```

#### `C08R8CHB0QL/1754322742.581179` (the only reply to the packs post)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/65`. Message id: `aca0199d95e6113c93b835eeabe10cf1`.
- Author: Robert (`EMPLOYEE_0016_SLACK_ID`)
- Time: 2025-08-04 15:52:22.581179 UTC | Mon 2025-08-04 08:52:22.581179 PDT
- Thread fields: thread_ts `1754316299.381419`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :+1: x1 (Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`))
- Files: none

Verbatim text:

```text
This will do for now
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754322742.581179: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

### Lineage context

#### `C08R8CHB0QL/1754077212.060209` (top-level post before the thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/41`. Message id: `0c5a0bbdc7c48ae2f8e6c450a6923f15`.
- Author: Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
- Time: 2025-08-01 19:40:12.060209 UTC | Fri 2025-08-01 12:40:12.060209 PDT
- Thread fields: thread_ts `None`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :+1: x3 (Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`), Julia Lawson (`EMPLOYEE_0005_SLACK_ID`), Martin Walsh (`EMPLOYEE_0033_SLACK_ID`))
- Files: none

Verbatim text:

```text
Now that we got all zombies I need to know wich one we replacing at the end of the game where you buy with 500 coins the Push to back zombies. Right now we still have the old punk zombie with the arm. We need one of the new zombies in There
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754077212.060209: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754077274.101399` (thread parent)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/42`. Message id: `a1b034f409efe9b6d4694e97eb8897f2`.
- Author: Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
- Time: 2025-08-01 19:41:14.101399 UTC | Fri 2025-08-01 12:41:14.101399 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 14, reply_users_count 4, latest_reply `1754313930.347939`
- Reactions: :+1: x2 (Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`), Julia Lawson (`EMPLOYEE_0005_SLACK_ID`))
- Files: none

Verbatim text:

```text
I feel that the best candidate for this is like the plumber guy. Cuz looks like a construction worker.  And it fits with the metal arm etc...
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754077274.101399: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754078709.206949` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/43`. Message id: `1fdc42f72227c05ed6c8406b95ee4ba2`.
- Author: Leonard Hayes (`EMPLOYEE_0038_SLACK_ID`)
- Time: 2025-08-01 20:05:09.206949 UTC | Fri 2025-08-01 13:05:09.206949 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :+1: x1 (Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`))
- Files: none

Verbatim text:

```text
I’m good with that call but as our chief world builder double check with <@EMPLOYEE_0005_SLACK_ID> 
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754078709.206949: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754310908.401429` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/46`. Message id: `4a5854ead3d2f26d0b29abfabe4a1573`.
- Author: Martin Walsh (`EMPLOYEE_0033_SLACK_ID`)
- Time: 2025-08-04 12:35:08.401429 UTC | Mon 2025-08-04 05:35:08.401429 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
this is so fast and nervous.
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754310908.401429: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754310912.013599` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/47`. Message id: `41d0e265fcc1e99eb8d19006d656c597`.
- Author: Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
- Time: 2025-08-04 12:35:12.013599 UTC | Mon 2025-08-04 05:35:12.013599 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :+1: x1 (Martin Walsh (`EMPLOYEE_0033_SLACK_ID`))
- Files: none

Verbatim text:

```text
yah the arm doesnt move that fast , its just the recording, cuz i recorded it ith 60 fps or something
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754310912.013599: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754311014.750619` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/48`. Message id: `9ac9453926885e2ab426ffad3f41dd17`.
- Author: Martin Walsh (`EMPLOYEE_0033_SLACK_ID`)
- Time: 2025-08-04 12:36:54.750619 UTC | Mon 2025-08-04 05:36:54.750619 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
About the packs. <@EMPLOYEE_0005_SLACK_ID> when you can generate some zombie? I'll touch and replace the elements for the assets needed for the animation
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754311014.750619: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754313296.572289` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/49`. Message id: `46341bf4924f0127a1062af35d7ceae6`.
- Author: Julia Lawson (`EMPLOYEE_0005_SLACK_ID`)
- Time: 2025-08-04 13:14:56.572289 UTC | Mon 2025-08-04 06:14:56.572289 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
I did the avatars this weekend, the packs are up next. [PERSON_NAME_0054] didn't like the initial concepts so I'm doing something different
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754313296.572289: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754313329.695369` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/50`. Message id: `a2723be7c125faea64a4e25e58144140`.
- Author: Martin Walsh (`EMPLOYEE_0033_SLACK_ID`)
- Time: 2025-08-04 13:15:29.695369 UTC | Mon 2025-08-04 06:15:29.695369 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: :heart: x1 (Julia Lawson (`EMPLOYEE_0005_SLACK_ID`))
- Files: none

Verbatim text:

```text
OK I'm trying something else too
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754313329.695369: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754313337.376159` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/51`. Message id: `9d7fa386c463e94cea6a38680ab9abce`.
- Author: Julia Lawson (`EMPLOYEE_0005_SLACK_ID`)
- Time: 2025-08-04 13:15:37.376159 UTC | Mon 2025-08-04 06:15:37.376159 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
The animation looks good Marcus, I guess we need to make this UI more pretty and adjust the animation speed too
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754313337.376159: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754313428.981219` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/52`. Message id: `43306b29b75d538aef633327670178f5`.
- Author: Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`)
- Time: 2025-08-04 13:17:08.981219 UTC | Mon 2025-08-04 06:17:08.981219 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
<@EMPLOYEE_0005_SLACK_ID> this its not the speed, i recorded it at 60 fps i dont know why recorded so fast, but its the same speed it was in the game with the punk one. so its has the good animation dont worry. Right now i'm looking to change the packs as they got the old artwork
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754313428.981219: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754313565.241859` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/54`. Message id: `1ad7e6907aebfe0bdcfff02c3582b133`.
- Author: Julia Lawson (`EMPLOYEE_0005_SLACK_ID`)
- Time: 2025-08-04 13:19:25.241859 UTC | Mon 2025-08-04 06:19:25.241859 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
The UI itself looks messy and unpolished though. We should revamp this. <@EMPLOYEE_0033_SLACK_ID> Any ideas?
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754313565.241859: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754313708.160879` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/59`. Message id: `d185115932456db203f57cb9124b7319`.
- Author: Martin Walsh (`EMPLOYEE_0033_SLACK_ID`)
- Time: 2025-08-04 13:21:48.160879 UTC | Mon 2025-08-04 06:21:48.160879 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Improving is always possible. Priority in time?
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754313708.160879: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754313748.470579` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/60`. Message id: `7684d6bd86a5ccfc39ea37cd6f8ee681`.
- Author: Martin Walsh (`EMPLOYEE_0033_SLACK_ID`)
- Time: 2025-08-04 13:22:28.470579 UTC | Mon 2025-08-04 06:22:28.470579 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
Now I'm working on the Collect and win and packs too
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754313748.470579: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754313918.430379` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/61`. Message id: `17a7dfa59d02029239b618ae4a053a18`.
- Author: Julia Lawson (`EMPLOYEE_0005_SLACK_ID`)
- Time: 2025-08-04 13:25:18.430379 UTC | Mon 2025-08-04 06:25:18.430379 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
medium, I guess. We don't even have that font shadow in anywhere else in the game.
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754313918.430379: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

#### `C08R8CHB0QL/1754313930.347939` (reply in the same thread)

- Service: slack. File + pointer: `messages/C08R8CHB0QL/2025-08.json` `/62`. Message id: `b6c2e1f7e0b7bf9bd76989957ee4492b`.
- Author: Martin Walsh (`EMPLOYEE_0033_SLACK_ID`)
- Time: 2025-08-04 13:25:30.347939 UTC | Mon 2025-08-04 06:25:30.347939 PDT
- Thread fields: thread_ts `1754077274.101399`, reply_count 0, reply_users_count 0, latest_reply `None`
- Reactions: none
- Files: none

Verbatim text:

```text
True
```

persona_view:

```text
claire_morgan slack C08R8CHB0QL/1754313930.347939: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

## 9. Trello

Board, pointer `/boards/4`: id `6851a6569f3bf818760632ab`, name `ZM ROADMAP`, closed `false`, dateLastActivity `2025-09-30T17:09:07Z` (overlay line 324 sets `2025-09-30T23:20:00Z`).

```text
claire_morgan trello 6851a6569f3bf818760632ab: YES
  reason:   trello is unscoped: every persona reads it (acl.md access matrix); existence not checked
```

Lists, in `pos` order:

| Pointer | List id | Name | pos | closed |
|---|---|---|---|---|
| `/lists/44` | `6851a6f765421ccbd3cbbe53` | `Jun 18th` | 8192.0 | false |
| `/lists/39` | `6851a6608b76856437112e45` | `Jun 30th` | 16384.0 | false |
| `/lists/40` | `6851a669fb9904d6d136b037` | `July 18` | 32768.0 | false |
| `/lists/45` | `6876878e769a212c7eb16c36` | `Jul 24` | 40960.0 | false |
| `/lists/41` | `6851a66dee906874db0e9764` | `July 30` | 49152.0 | false |
| `/lists/42` | `6851a674975da1fe76e70d93` | `BETA: Oct 10` | 65536.0 | false |
| `/lists/43` | `6851a677e090018224fb8c7f` | `Oct 21` | 81920.0 | false |
| `/lists/46` | `68c451221ebabaf255a7d16b` | `Backlog` | 98304.0 | false |

Every list returns the same unscoped YES. Sample:

```text
claire_morgan trello 6851a6f765421ccbd3cbbe53: YES
  reason:   trello is unscoped: every persona reads it (acl.md access matrix); existence not checked
```

Card, pointer `/cards/750`:

- id `68768a1501ae552dbee94b8a`, idShort 45
- name `Marketing Video Refresh (Marcus/[PERSON_NAME_0036])`
- list `Jul 24` (`6876878e769a212c7eb16c36`)
- closed `false`, due `None`, dueComplete `true`, badges.dueComplete `true`
- members `idMembers` []: nobody is assigned, the two people appear only in the title
- url `https://PERSON_6092_TRELLO_USERNAME.com/c/1yOhGIcw/45-marketing-video-refresh-marcus.bennett-frederick.stone`, dateLastActivity `2025-08-20T16:38:52Z` (overlay line 323 sets `2025-09-26T17:40:00Z` and badges.comments 1)

```text
claire_morgan trello 68768a1501ae552dbee94b8a: YES
  reason:   trello is unscoped: every persona reads it (acl.md access matrix); existence not checked
```

## 10. Linear

Team, pointer `/teams/0`: id `team_ART`, name `Art`, key `ART`.

```text
claire_morgan linear team_ART: YES
  reason:   linear is unscoped: every persona reads it (acl.md access matrix); existence not checked
```

### ART workflow states

The export has no workflow-state collection (`/workflow_states`, `/states`, `/workflowStates`, `/team_states` all return `JSON pointer not found`). States exist only as the plain string `state_id` on each issue. Distinct values over all 597 `team_ART` issues, with full coverage (597 of 597):

| state_id | ART issues |
|---|---|
| `Done` | 488 |
| `Canceled` | 77 |
| `Todo` | 12 |
| `In Review` | 11 |
| `Team Epic` | 4 |
| `Backlog` | 3 |
| `Duplicate` | 2 |

`In Progress` exists on other teams but has 0 ART issues. The overlay's `Done` and `Canceled` are both valid ART values.

### Users

| Person | Pointer | id | email | name field | is_active |
|---|---|---|---|---|---|
| Marcus Bennett | `/users/33` | `usr_c77c50cc15c5342d` | `marcus.bennett@harmonygames.co` | `marcus.bennett@harmonygames.co` | true |
| Julia Lawson | `/users/18` | `usr_8140f09bf9f1b94c` | `julia.lawson@harmonygames.co` | `julia.lawson@harmonygames.co` | true |
| Martin Walsh | `/users/9` | `usr_51f5f16d46e8cf55` | `martin.walsh@harmonygames.co` | `martin.walsh@harmonygames.co` | true |

The `name` and `display_name` fields hold the email address, so there is no human-readable name in Linear. Sample visibility:

```text
claire_morgan linear usr_c77c50cc15c5342d: YES
  reason:   linear is unscoped: every persona reads it (acl.md access matrix); existence not checked
```

### Tickets near ART-774 and ART-790..792

| Pointer | id | Title | state_id | assignee_id | created_at | completed_at |
|---|---|---|---|---|---|---|
| `/issues/578` | `ART-770` | River Rush VFXs and Animations | `Done` | `usr_c77c50cc15c5342d` | 2025-01-30T13:50:54Z | 2025-05-12T09:11:57Z |
| `/issues/579` | `ART-771` | New Tile concept - win streak booster and the pre-level wildcard booster should be a little different from each other | `Done` | `usr_51f5f16d46e8cf55` | 2025-02-20T17:00:06Z | 2025-03-11T08:50:00Z |
| `/issues/580` | `ART-772` | Zombie match 3D - Art and assets for the parallax effect of the backgro | `Done` | `usr_51f5f16d46e8cf55` | 2025-02-21T16:47:44Z | 2025-04-15T13:19:04Z |
| `/issues/581` | `ART-773` | Teams Feature | `Done` | `usr_51f5f16d46e8cf55` | 2025-02-27T17:49:38Z | 2025-04-15T13:18:53Z |
| `/issues/582` | `ART-774` | Zombie Match 3D - Marketing Screenshots | `Done` | `usr_51f5f16d46e8cf55` | 2025-03-10T20:16:34Z | 2025-04-15T13:21:51Z |
| `/issues/583` | `ART-775` | Zombie Match 3D - Leaderboards | `Done` | `usr_51f5f16d46e8cf55` | 2025-03-28T10:00:40Z | 2025-04-15T13:18:36Z |
| `/issues/584` | `ART-776` | Zombie Match 3D - Profile feature | `Done` | `usr_51f5f16d46e8cf55` | 2025-03-28T10:01:06Z | 2025-04-15T13:18:27Z |
| `/issues/585` | `ART-777` | Domino Delights - Marketing Localization Screens | `Done` | `usr_51f5f16d46e8cf55` | 2025-04-02T11:56:16Z | 2025-04-15T13:19:24Z |
| `/issues/586` | `ART-778` | Unlocked in-Game boosters screens | `Done` | `usr_51f5f16d46e8cf55` | 2025-04-15T13:22:43Z | 2025-04-15T13:22:43Z |
| `/issues/587` | `ART-779` | In-game boosters - Locked & states | `Done` | `usr_51f5f16d46e8cf55` | 2025-04-15T13:23:57Z | 2025-04-15T13:23:57Z |
| `/issues/589` | `ART-780` | Pre-Level - Locked  Win-streak and boosters | `Done` | `usr_51f5f16d46e8cf55` | 2025-04-15T13:25:33Z | 2025-04-15T13:25:33Z |
| `/issues/590` | `ART-790` | Updated ZM Marketing Screenshots | `Todo` | `usr_51f5f16d46e8cf55` | 2025-07-09T18:53:42Z | None |
| `/issues/591` | `ART-792` | ZM3D - Marketing Screenshots round 3 | `Team Epic` | `usr_51f5f16d46e8cf55` | 2025-08-26T18:57:06Z | None |

**Note:** the base is thin and almost all Done above ART-770, with no ART-781..789 and no ART-791, and ART-792 is the highest number, so overlay ART-793 onward continues it without collision.

- `id` equals `identifier`. There is no separate UUID in the export. Array order is string-sorted (`ART-78` sits between ART-779 and ART-780).
- ART-790 is `Todo` and ART-792 is `Team Epic`, both assigned to Martin Walsh with no `completed_at`. ART-774 is `Done`, created by `usr_175c0d7bc72ed244`.
- SC-16 describes ART-790/792 as `still Todo/In Progress`, but ART-792's actual value is `Team Epic`. Quote the record, not the card.

`ART-774` `Zombie Match 3D - Marketing Screenshots` description, pointer `/issues/582/description`:

```text
As part of launch readiness, can we get screenshots for Zombie Match 3D? For reference, I shared Match Factory's screen shots and a simple mock up here: [https://www.figma.com/design/TvRw8na5iGd3NynbSRUGFy/Zombie-Match-3D?node-id=13-6&p=f&t=Jqf5xVlUah8L7XRr-0](https://www.figma.com/design/TvRw8na5iGd3NynbSRUGFy/Zombie-Match-3D?node-id=13-6&p=f&t=Jqf5xVlUah8L7XRr-0)

Specs:

### **Google Play Store Screenshot Sizes**

* **Phone Screenshots**:
  * **Minimum size**: 1080 x 1920 pixels
  * **Aspect ratio**: 16:9 or 9:16
  * **Maximum size**: 3840 x 2160 pixels
* **Tablet Screenshots**:
  * **Minimum size**: 1920 x 1080 pixels
  * **Aspect ratio**: 16:9 or 9:16
  * **Maximum size**: 3840 x 2160 pixels
* **Other Requirements**:
  * Up to **8 screenshots** allowed
  * JPEG or 24-bit PNG (no transparency)

### **Apple App Store Screenshot Sizes**

* **iPhone Screenshots**:
  * **6.5-inch Display (iPhone 14 Pro Max, 13 Pro Max, etc.)**:
    * 1284 × 2778 pixels
  * **5.5-inch Display (iPhone 8 Plus, etc.)**:
    * 1242 × 2208 pixels
* **iPad Screenshots**:
  * **12.9-inch iPad Pro**:
    * 2048 × 2732 pixels
  * **10.5-inch iPad Pro**:
    * 1668 × 2224 pixels
  * **8.3-inch iPad mini**:
    * 1488 × 2266 pixels
* **Other Requirements**:
  * At least **one screenshot per required display size**
  * Up to **10 screenshots per device**
  * JPEG or 24-bit PNG (no transparency)
```

```text
claire_morgan linear ART-774: YES
  reason:   linear is unscoped: every persona reads it (acl.md access matrix); existence not checked
```

`ART-790` `Updated ZM Marketing Screenshots` description, pointer `/issues/590/description`:

```text
Can we get updated Marketing Screenshots that reflect our new zombies and show the larger play area? For zombies, I'd suggest we go with mailman, karen, kid, and Chef as shown here. I'm not sure who took the original screenshots of the play area. If we can get those showing the larger size and newer zombies, that would be ideal. [https://www.figma.com/design/TvRw8na5iGd3NynbSRUGFy/Zombie-Match-3D?node-id=13-6&p=f&t=Jqf5xVlUah8L7XRr-0](https://www.figma.com/design/TvRw8na5iGd3NynbSRUGFy/Zombie-Match-3D?node-id=13-6&p=f&t=Jqf5xVlUah8L7XRr-0)
```

```text
claire_morgan linear ART-790: YES
  reason:   linear is unscoped: every persona reads it (acl.md access matrix); existence not checked
```

`ART-792` `ZM3D - Marketing Screenshots round 3` description, pointer `/issues/591/description`:

```text
Can you use your eye for composition to mock up a new set of potential screenshots to A/B test against our current set? Feel free to completely re-envision the theme. That is, don't feel like you need to follow any of the current design choices — such as limited the matching items to a single color, keeping the matching area the same size as it currently is, or even displaying the matching area at all.
```

```text
claire_morgan linear ART-792: YES
  reason:   linear is unscoped: every persona reads it (acl.md access matrix); existence not checked
```

## 11. Slack channels

| Channel | id | Pointer | Private | Archived | num_members | Claire in `members` |
|---|---|---|---|---|---|---|
| #zombie_marketing | `C06DJBJL798` | `channels.json` `/57` | true | false | 17 | yes |
| #zombie-art | `C08R8CHB0QL` | `channels.json` `/129` | false | false | 23 | yes |
| #zombie-match3d | `C0880U9751A` | `channels.json` `/108` | true | false | 25 | yes |
| #zm-animations | `C09ATAJ220H` | `channels.json` `/139` | true | false | 14 | yes |
| #company-internal | `C05KNDCHAAG` | `channels.json` `/38` | true | false | 38 | yes |
| #builds | `C05433XK267` | `channels.json` `/25` | false | false | 31 | yes |
| Claire's IM | `D05V2N6PZNU` | `channels.json` `/590` | false | false | 5 | yes |

`#zombie-art` and `#builds` are public, the others private. Note SC-7: membership lists are not a safe grading basis, so use these only for reach.

`D05V2N6PZNU` has `is_im` true but lists 5 members: `EMPLOYEE_0002_SLACK_ID`, `EMPLOYEE_0009_SLACK_ID`, `PERSON_6089_SLACK_ID`, `U0506EUH4M7`, `U05UDKGFX0B`. Marcus (`EMPLOYEE_0002_SLACK_ID`) and Claire are two of them. The other three were not resolved.

persona_view:

```text
claire_morgan slack C06DJBJL798: YES
  reason:   persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
```

```text
claire_morgan slack C08R8CHB0QL: YES
  reason:   persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
```

```text
claire_morgan slack C0880U9751A: YES
  reason:   persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
```

```text
claire_morgan slack C09ATAJ220H: YES
  reason:   persona EMPLOYEE_0009_SLACK_ID is in members of private zm-animations
```

```text
claire_morgan slack C05KNDCHAAG: YES
  reason:   persona EMPLOYEE_0009_SLACK_ID is in members of private company-internal
```

```text
claire_morgan slack C05433XK267: YES
  reason:   persona EMPLOYEE_0009_SLACK_ID is in members of public builds
```

```text
claire_morgan slack D05V2N6PZNU: YES
  reason:   persona EMPLOYEE_0009_SLACK_ID is in members of im D05V2N6PZNU
```

## 12. Base calendar and Gmail lookalikes

### Calendar: no other Halloween review

- `Halloween` appears 0 times anywhere in gcal `data.json` (`scan_complete` true). `ZM3D` appears in 0 event summaries. The overlay's `ZM3D Halloween review` is unique.
- `2025-10-02` appears in 0 event values, so no base event instance sits on that date.
- Claire has 553 events on `claire.morgan@harmonygames.co`. Her only `review`-named one is `Bug Review` (`/events/5852`, weekly Tuesdays). Her latest instances are `POD: PROTOTYPE` Sep 29 (`/events/1697`) and `(Wednesday) Mid Week Art Sync` Oct 1 (`/events/8858`).
- Caveat: recurring masters without `UNTIL` could still expand onto Thu Oct 2. `POD: PROTOTYPE` (`/events/134` and `/events/6900`, `RRULE:FREQ=WEEKLY;BYDAY=MO,TU,TH`, 16:00-16:30Z) has the same slot as the seeded review (16:00-16:30Z, 09:00-09:30 PDT). `Ops-timus Prime Catchup` (`/events/967`, 16:30Z, and `/events/9400`, `/events/5216`, 16:45Z) and others follow it. These are not named like the review, but a solver expanding recurrences would see an overlap.

### Gmail: nothing that looks like an October UA plan

Searched all 81,404 thread files, every query `scan_complete` true after raising limits.

| Query | Scope | Hits | Outcome |
|---|---|---|---|
| `October UA` | all fields | 0 |  |
| `October plan` | all fields | 0 |  |
| `plan for October` | all fields | 0 |  |
| `UA for October` | all fields | 0 |  |
| `October budget` | all fields | 0 |  |
| `retention restart` | all fields | 0 |  |
| `Halloween flight` | all fields | 0 |  |
| `creatives to me` | all fields | 0 |  |
| `UA plan` | all fields | 2 | Liftoff newsletter item `UA Planning: ...`, Leonard and Martin mailboxes |
| `Q4 UA` | all fields | 4 | Vendor newsletter text plus one header-hash false match |
| `Unity only` | all fields | 2 | Conference mail and a code-review note, unrelated |
| `UA` | subject, case-sensitive | 75 | Vendor mail, 2024 sync invites, `UA video assets` notices, and the Tilting Point item below |
| `October` | subject | 96 | Admin, board and vendor mail. None about UA planning |
| `Halloween` | subject | 2 | 2024 music newsletter and a 2023 costume social |
| `Unity` | subject | 908 | Filtered for plan, flight, budget, UA, retention, creative: only `Unity Performance by Creative Pack` (Nov 2024 Singular support thread on the Unity Ads connector), vendor pitches and Unity Pro notices |
| `campaign` | subject | 66 | Same filter, no UA plan |
| `Oct 20` | body | 209 | Firebase test results and unrelated mail |

Closest by title, and still not a plan: `threads/frederick@harmonygames.co_1842443183462721250.json` `/messages/0`, subject `'UA Funding request`, Fri 05 Sep 2025 16:45:42 +0000, in Frederick's mailbox. It is a Tilting Point auto-acknowledgement:

```text
Thank you for submitting your application. We have successfully received  
your request and will review the details carefully.
If your game aligns with our criteria for funding, our team will reach out  
to you shortly to discuss next steps.
We appreciate your interest in working with us and will be in touch if we  
can move forward.

Tilting Point
```

The overlay mails `October UA plan (draft)` and `October UA plan - changes` therefore have no base competitor.

## 13. SC cards in `Task_Authoring/references/known_data_issues/synthcut.md`

### Unity spend or CPI

| Card | Title | Why it matters | Don't grade |
|---|---|---|---|
| SC-11 | Unity spend is $0 in Snowflake | direct | Unity spend, CPI or total UA spend from Snowflake. |
| SC-12 | Meta spend missing from Snowflake | adjacent: ZM3D paid UA spend | Meta/Facebook spend or ZM3D paid UA spend. |
| SC-23 | AppLovin spend dates and countries | adjacent: other Snowflake UA spend | AppLovin spend, geos or campaign dates from Snowflake. |

### ART tickets

| Card | Title | Why it matters | Don't grade |
|---|---|---|---|
| SC-16 | Linear tickets still open after work shipped | direct: names ART-790/792 | Linear status as proof of whether work shipped (ZOM-564, ZOM-513/514, ZOM-563, ART-790/792). |
| SC-22 | time_in_status_minutes runs past the clock | any ticket; ART-792 has 246277 and overlay line 171 nulls it | Ticket durations from Linear's time_in_status_minutes. |
| SC-32 | 'In Review' tickets with completion dates | 11 of the 12 In Review tickets are ART | 'In Review' tickets as open or done. |
| SC-30 | Done parent tickets with open children | any parent ticket | A parent ticket's status implying its children's. |

### App icon or store listing dates

| Card | Title | Why it matters | Don't grade |
|---|---|---|---|
| SC-19 | Telemetry app versions vs Slack builds | no card names the icon or listing; this one covers store-build versions, 0.3.x vs 1.3.x, and so 1.3.38 | Matching RAW_EVENTS app versions to a store build in Slack. |
| SC-16 | Linear tickets still open after work shipped | ART-790/792 are marketing-screenshot tickets | Linear status as proof of whether work shipped (ZOM-564, ZOM-513/514, ZOM-563, ART-790/792). |

### ZM3D release dates

| Card | Title | Why it matters | Don't grade |
|---|---|---|---|
| SC-13 | ZM3D beta date in Trello list name | direct | The ZM3D beta date from the Trello list name. |
| SC-14 | Beta cards' two 'complete' flags disagree | beta cards on the same board | Which Trello beta cards are 'complete' (cards 54/56/58/67). |
| SC-19 | Telemetry app versions vs Slack builds | build matching | Matching RAW_EVENTS app versions to a store build in Slack. |
| SC-38 | Season Pass ship date and analytics | ship date | Season Pass ship date or analytics status. |
| SC-67 | Build #1621 post lists #1620 | #builds number | Which build contained PR #439, from the #builds post. |
| SC-68 | Boss Arena on prod before its code | prod date | When Boss Arena reached prod. |
| SC-28 | Product OKRs page numbers vs Snowflake | launch claims | The Confluence Product OKRs numbers. |

### Slack timezones

| Card | Title | Why it matters | Don't grade |
|---|---|---|---|
| SC-70 | Slack timezones all Los Angeles | direct | A person's timezone from Slack. |

### Trello list names

| Card | Title | Why it matters | Don't grade |
|---|---|---|---|
| SC-13 | ZM3D beta date in Trello list name | direct: `BETA: Oct 10` | The ZM3D beta date from the Trello list name. |

### Linear states

| Card | Title | Why it matters | Don't grade |
|---|---|---|---|
| SC-16 | Linear tickets still open after work shipped | state vs shipped | Linear status as proof of whether work shipped (ZOM-564, ZOM-513/514, ZOM-563, ART-790/792). |
| SC-30 | Done parent tickets with open children | parent vs child | A parent ticket's status implying its children's. |
| SC-32 | 'In Review' tickets with completion dates | In Review | 'In Review' tickets as open or done. |
| SC-8 | ZOM-475 glass crash: fixed or not | ZOM-475 Todo | Whether the ZOM-475 glass crash is fixed. |
| SC-15 | ZOM-521 checklist ticked, children still open | ZOM-521 children | What is left on the ZOM-521 VFX master ticket. |
| SC-38 | Season Pass ship date and analytics | ZOM-552 In Progress | Season Pass ship date or analytics status. |

### Claire Morgan, Marcus Bennett, Julia Lawson, Martin Walsh

| Card | Title | Why it matters | Don't grade |
|---|---|---|---|
| SC-7 | People who left channels still listed | none of the four is named in any card (grep confirmed); this is generic, channel membership | Channel membership (who is in a channel). |
| SC-36 | Victor Barnes still on invites and channels | generic: invite lists from membership | Invite/share lists built from channel or calendar membership. |
| SC-70 | Slack timezones all Los Angeles | generic: every Slack user | A person's timezone from Slack. |
| SC-25 | PAYROLL_ROSTER vs who actually works there | generic: roster vs current staff | Who is on payroll or current staff from PAYROLL_ROSTER. |

Also relevant to the records above: SC-56 (`Exact-case commit title matches between GitHub and #builds.`) applies when quoting #1450's change line against GitHub.

Card 68768a1501ae552dbee94b8a is idShort 45, outside SC-14's cards 54/56/58/67, and its two `dueComplete` flags agree (both true).

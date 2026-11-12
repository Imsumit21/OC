# Base fact pack for design D2 — synth-cut universe (frozen 2025-10-01 00:00 UTC)

Read-only. Every base fact below was read through `Task_Authoring/tools/hg.py search` (`files`, `get`, `get-many`, `search`, `search-many`, `lookup`) with `TASK_AUTHORING_TASK_DIR` set, plus `persona_view.py can-see`, `entity.py resolve` and `references/universe_kb/by_universe/synthcut/activity.json`. Times are UTC. A Slack pointer is `<channel>/<ts>`. Quotes are verbatim, including the export's masking tokens and its capitalised `There` / `Push`. Anything I could not settle is marked UNVERIFIED with the reason. Companion file: `research/object_categories.csv`.

## 0 Things that will change the rebuild

1. **`[PERSON_NAME_0040]` stands for two people.** It is Julia in `D05SD5QLG94/1758220925.518329` (Frederick to Julia: "Hey [PERSON_NAME_0040], PlayableX is looking for these assets") and in `C08H78VJG80/1742063341.276529` (vendor: "[PERSON_NAME_0040], thank you so much for this detailed brief"). It is Claire in `C0880U9751A/1741339853.288969` (Marcus: "[PERSON_NAME_0040] would have to export an fbx of the same model with different uv for each color … But it will be more work on <@EMPLOYEE_0009_SLACK_ID>") and in `D05SD5QLG94/1756235286.918989` (Julia: "[PERSON_NAME_0040] and Marcus loves tickets"). So `D07G5QWN3TM/1758712928.567529` (Brian, 24 Sep 11:22: "I talked with [PERSON_NAME_0040] about items, but I need the other elements") is ambiguous; Claire is the likelier reading because Brian was in his DM with her at 11:19–11:28. UNVERIFIED which.
2. **Other tokens, each fixed by a record.** `[PERSON_NAME_0092]` = Brian (`D05SD5QLG94/1758221343.478869`). `[PERSON_NAME_0036]` = Frederick (same message: "Hey, [PERSON_NAME_0036]."). `[PERSON_NAME_0054]` = Robert (`D050QE3CXRU/1755016886.325179`, Calvin to Robert: "Hey [PERSON_NAME_0054].. I may have bandwidth today to help you out on the SFX"; PR `match3d#47` head `[PERSON_NAME_0054]/LevelEdit` by `EMPLOYEE_0016`). `[PERSON_NAME_0120]` = EMPLOYEE_0032 (PR `match3d#461` head `[PERSON_NAME_0120]/monster-bar-thickness`, author `EMPLOYEE_0032_GITHUB_USERNAME`). `[PERSON_NAME_0029]` = Calvin (PR `match3d#381` "[PERSON_NAME_0029]/test game music", shown in `C093LEZGF6J/1755208790.707609` as "calvin.price's pull request"). `[PERSON_NAME_0050]` = Vincent Parker (`C0880U9751A/1753894796.414599`). `[PERSON_NAME_0019]` = Julia's branch prefix (`D076RBM29JS/1758637712.721729`: "```[PERSON_NAME_0019]/playablelevels```").
3. **Claire's per-object tickets are in ZOM, not ART.** `ZOM-97` "REVISION FOR ITEMS" has 51 children titled with object names; Claire has touched no ART ticket since September 2024 (§7).
4. **The six objects Robert "added" in D1 come from a base thread about the bounce effect**, and Robert says the two balls have "no color variants" (§9).
5. **Base contradicts "match scale cut from a bought pack".** The combo scale was pitched by Calvin from a sample Robert posted whose file name carries the same `11L-` prefix as Calvin's ElevenLabs outputs; the August soundtrack is "AI generated"; Robert calls the laptop error and shutdown sounds a copyright problem in Julia's own DM (§4).
6. **The repository tree is a late-September snapshot** and shows that Dart Board, Candy, the sushi set, Abacus and the other new objects have models and prefabs but no entry under `Assets/Data/Objects/` (§1).
7. **Robert asked for the 2x monster health bar on 24 Sep 05:21**, seven hours before the zip (`C0880U9751A/1758691270.557429`); PR `#461` merged at 16:37.
8. **The vendor's scenario document is not in base** (0 hits in Docs and Drive for its id); the four scenarios exist only as four one-line bullets (§8).
9. **One base record holds a login and password in clear text** (`D05UDNCCFEW/1757008285.488349`). It is cited below without the credential; do not copy it into seeded text.

## 1 Object tree — `harmonygames-Games/match3d` `Assets/Data/Objects/`

**How it was read.** `hg.py search files github "match3d/Assets/Data/Objects/" --limit 12000` returned 10,093 paths, `truncated: false`, all under `root/harmonygames-Games/match3d/`. An object is a second-level folder that holds at least one file (`<category>/<object>/<file>`). File contents are not readable through the helper (the repository is git packs and blobs, not JSON), so nothing about what an asset contains is verified.

**CSV.** `object_categories.csv` has 246 rows over 25 categories. 242 rows are object folders. Two categories hold loose asset files instead of folders; for them the `object` column is the file name: `CollectAndWin` (`CollectAndWinItem.asset`) and `OneClickPowerUps` (`Air_Strike_Rocket.asset`, `PowerUp GlueBucket Revised 01.asset`, `PowerUp Trampoline Revised 01.asset`). Not in the CSV: the top-level files `DefaultPhysicsMaterial.physicMaterial` and `ObjectsData_MainBuildMaster.asset`.

| Category | Objects | Category | Objects |
|---|---|---|---|
| Baked Goods | 7 | Kitchen | 25 |
| Bathroom | 13 | Living Room | 10 |
| Bedroom | 2 | Music Instruments | 14 |
| Beverages | 7 | OneClickPowerUps | 3 (files) |
| Breakfast | 5 | Personal Care | 9 |
| CollectAndWin | 1 (file) | Personal Electronics | 11 |
| Dining Room | 15 | PowerUp | 1 |
| FTUE Objects | 7 | Sports | 19 |
| Fast Food | 9 | Survival | 14 |
| Fruit | 14 | Sweets | 4 |
| Garden | 13 | Tools | 1 |
| | | Toys | 25 |
| | | Travel | 3 |
| | | Vegetables | 14 |

**Categories that matter for the rebuild (exact names).**
- Bathroom (13): Bathroom Scale, Bathtub, Cabinet Sink, Flip Flops, Iron, Ironing Board, Plunger, Rubber Ducky, Slippers, Toilet, Toilet Paper, Wash Basin, Washing Machine.
- Personal Care (9): Curling Iron, Flat Comb, Hair Dryer, Hair Straightener, Hair Trimmer, Hairbrush, Long Comb, Shampoo, Wooden Hairbrush.
- Music Instruments (14): Acoustic Guitar, Cello, Clef, Cymbals, Electric Guitar, Grand Piano, Harp, Maracas, Music Keyboard, Music Note 1, Music Note 2, Tambourine, Trumpet, Xylophone.
- Living Room (10): Alarm Clock, Armchair, Couch, Couch and Pillow, Desk Lamp, Fly Zapper, Indoor Plant, Record Player, Retro TV, Small Lamp.
- Survival (14): Chainsaw, Cute Axe, Cute Hammer, Dynamite, Fire Extinguisher, First Aid Kit, Flashlight, Gas Can, Grenade, Helmet, Propane Tank, Saber, Safe, Shuriken.
- Toys (25): Badge, Beach Ball, Bicycle, Bow, Cone, Dice, Easel, Gift Box, Letter, Pencil, Plushie Bunny, Plushie Chick, Plushie Dog, Plushie Whale, Scooter, Toy Airplane, Toy Boat, Toy Car, Toy Drum, Toy Hammer, Toy Train, Toy Truck, Toy Xylophone, Whistle, Wooden Tower.
- Garden (13): Barrel, Bench, Cactus Plant, Carrot Box, Flower Pot, Garden Hand Rake, Garden Shears, Garden Trowel, Seedling Bag, Watering Can, Wheelbarrow, Wooden Bucket, Wooden Crate.
- Sports (19): American Football, Baseball, Baseball Bat, Basketball, Bowling Ball, Bowling Pins, Boxing Gloves, Dumbbell Big, Golf Club, Kettlebell, Ping Pong Paddle, Pool Ball, Pool Cue Stick, Shuttlecock, Soccer Ball, Surf Board, Tennis Ball, Tennis Racket, Volley Ball.

**Colour variants (count of variant `.asset` files per object folder).** 143 objects have 29, 5 have 28, and 73 have exactly one. Single-variant objects include: Plushie Chick (`Plushie Chick Medium Yellow2`), Plushie Bunny (`Plushie Bunny Medium Pink1`), Soccer Ball (`Soccer Ball Medium White1`), Basketball (`Basketball Medium Orange2`), Cactus Plant (`Cactus Plant Medium Orange2`), Chainsaw (`Chainsaw Medium Yellow2`), Cone (`Cone Medium Orange2`), Rubber Ducky, Toilet Paper, Paper Towel, Rolling Pin, Desk Lamp, Cello, Dynamite, Milk Carton, Plate. With 29: Grenade, Couch, Couch and Pillow, Armchair, Iron, Bow, Shuriken, Cute Axe, Cute Hammer, Gift Box, Toy Drum, Scooter, Bicycle, Toy Hammer, Kettlebell, Grand Piano, Retro TV, Barrel, Cabinet Sink, Hair Trimmer. Folders with no `…CardData.asset`: Grenade, Dynamite, Letter, Toy Xylophone, AtomicBomb.

**Names: July export (`research/base_object_roster.csv`, 151) against the tree.** In the roster but not in the tree under that spelling: Checkered Round Table, Electric Hair Trimmer (tree: Hair Trimmer), Fancy Egg (tree: Egg On Plate), GrandPiano (Grand Piano), Large Barrel (Barrel), Pepperoni Pizza Slice (Pizza Slice), Rectangle Dining Table (Rectangle Table), RetroTV (Retro TV), Sheriff Badge (Badge), Volleyball (Volley Ball), Wash Basin Cabinet (Cabinet Sink), Wooden Kitchen Chair (Wooden Chair). The bracketed matches are my reading of the names, not a base statement.

**Not in `Assets/Data/Objects/` at all:** Dart Board, Candy, Traffic Cone (the tree has `Toys/Cone`), Abacus, Atom, DNA, Protractor, Blackboard, HandSaw, Chopstick, any sushi, Arrow, Rocking Chair. Prefabs or models do exist for several: `Assets/Prefabs/Objects/Toys/Dart Board Medium Blue2.prefab`, `…/Toys/Abacus Medium Brown2.prefab`, `…/Fast Food/Chopstick Pair Small Red3.prefab`, `Assets/MyAssets/3dModels/SmoothedModels/Food/Candy_1.fbx` and `Candy_2.fbx`. No path matches `Prefabs/Objects/Toys/Arrow` or `…/Rocking`.

**Snapshot date.** UNVERIFIED exactly (git metadata is not readable through the helper). It is after `match3d#462` (merged 2025-09-25T23:15:41Z), because the tree holds the prefabs that PR lists. It also holds `Assets/Data/Objects/CollectAndWin/CollectAndWinItem.asset`; PR `#468` "Collect And Win" merged 2025-09-29T16:13:50Z (tying that file to `#468` is inference). A branch log `marcus.bennett/EndlessMode_Vfx_NewUnity` exists under `.git/logs/refs/heads/`.

## 2 `#zm-animations` (`C09ATAJ220H`), 24–30 Sep

Julia can-see: YES. The September file has 203 messages (last `1759271121.716799`, 30 Sep 22:25). There is no message on 24 Sep. Zombie-pack timeline, all 26 Sep:

| UTC | Id | Who | Text |
|---|---|---|---|
| 10:11 | `1758881478.985769` (root, 1 reply) | Brian | "<@EMPLOYEE_0002_SLACK_ID> I’m trying to export the zombies as a Unity package for the playable team. Can you help me with this? When I export and open it in a new project, it looks like this. We’ll only be using the zombies for animations." |
| 10:11 | `1758881484.400909` | Brian | file `image.png`, no text |
| 10:12 | `1758881579.188609` | Brian | "I need these zombies' animations ⏎ • PartyGirl ⏎ • Plumber ⏎ • [PERSON_NAME_38021] ⏎ • [PERSON_NAME_35423] ⏎ • Magician ⏎ • [PERSON_NAME_49914] ⏎ • [PERSON_NAME_59157] ⏎ • [PERSON_NAME_1974] ⏎ • Footballplayer" |
| 10:24 | `1758882297.431829` | Marcus | "The zombies animated work only in Unity with 2d animation package. If they wana do it external they gona just need the psb files or we bake the animations into 2d sprite atlases but that takes time" |
| 10:46 | `1758883570.104439` (reply to 10:11) | Marcus | "yah alright i can export them zombies!" |
| 13:24 | `1758893054.650499` (root, 4 replies) | Brian | "We’ll provide the assets as a Unity package including PSDs, animations, etc. They’ll use these assets to re-animate in Spine and upload to their platform, so we don’t need to handle that part. We just need to share the existing assets as a Unity package with all components included, making sure everything works properly when opened in a clean Unity project <@EMPLOYEE_0002_SLACK_ID>" |
| 14:42 | `1758897723.082899` | Marcus | "ok, is it ok monday?" |
| 14:43 | `1758897837.509989` | Brian | "We're already running late, so it would be great if you could take care of it today. Since you know the system well, I think you can handle it easily" |
| 16:53 | `1758905604.787929` | Marcus | file `zombies_Characters_UnityPack.zip`; "<@EMPLOYEE_0026_SLACK_ID> i've included packages, an instalation text with what you need to do. and a video on how to play the animations. I've tested it in an empty project myself and thats how i recorded the video." |
| 16:56 | `1758905816.794149` | Brian | "Great! Thank you!" |

- **Who made the pack:** Marcus Bennett (`EMPLOYEE_0002_SLACK_ID`). Brian forwarded it to the vendor four minutes later (`C08H78VJG80/1758906043.375719`, 17:00: "Sorry, it took a little while, I had to get help from our animator"). Marcus to Calvin, `D05U73FNDDL/1758905679.456409` (16:54): "because i had to give to [PERSON_NAME_0092] the zombie characters so the guys who build the playable ads have them so they can start working on it".
- **What was tested:** only Marcus's sentence above ("tested it in an empty project myself"). Brian's first attempt failed in a new project (10:11). The vendor had asked for exactly this on 25 Sep (`C08H78VJG80/1758808234.045839`: "test the package in a blank Unity project before sending it over").
- **Zombie names visible unmasked:** PartyGirl, Plumber, Magician, Footballplayer. Five are masked. Brian's earlier list to EMPLOYEE_0032 (`D07G5QWN3TM/1758712833.442809`, 24 Sep 11:20, not visible to Julia) has nine entries, eight masked as `[USERNAME_60256]` … `[USERNAME_53499]` and the last "VarC-FootballPlayer".
- **Other zombie names base attests** (audio file names under `Assets/MyAssets/Audio/`): ZombieBoxerDeath, ZombieChefDeath, ZombieDeathCheerleader, ZombieDeathKaren, ZombieFootballPlayerDeath, ZombieKidDeath, ZombieMagicianDeath, ZombieMailmanDeath, ZombieMayorDeath, ZombiePartyGirlDeath, ZombiePlumberDeath. `[PERSON_NAME_35423]` is a female zombie (`C08R8CHB0QL/2025-07.json#/618`: "[PERSON_NAME_35423] is female, football player has a the helmet"). Which five names are masked is UNVERIFIED.
- **29–30 Sep in the channel:** card VFX (`1759161289.051769`), the Win&Collect queue manager (`1759183318.447139`), the tap-shot effect (`1759247492.619029`), a better "enraged" effect (`1759256190.810199`). Nothing about the playable.

## 3 `#zombie-design` 25–30 Sep and `#zombie-art` 24–30 Sep

### `#zombie-design` (`C090N54TG79`) — 145 messages in the window (25 Sep 37, 26 Sep 1, 27 Sep 2, 29 Sep 89, 30 Sep 16)

| UTC | Id | Who | Gist or quote |
|---|---|---|---|
| 24 Sep 23:36 | `1758757016.553559` (root, 13 replies) | Robert | "New Item Thread, in ( ) is the item cloned from" |
| 24 Sep 23:37 – 25 Sep 00:28 | replies `1758757026.873959`, `1758757641.634929`, `1758757881.264889`, `1758758037.503059`, `1758758503.319859`, `1758758672.742539`, `1758759314.143939`, `1758759686.056119`, `1758760095.485329` | Robert | clones, each with a video: "Protractor (Pencil) and Blackboard (wooden bench)"; "Abacus (wooden tower), DNA Helix (Badge), Atomic Molecule (Badge)"; "Handsaw (scissor)"; "Ice Cream Cone (Soft serve)"; "Various lollipops (Kiwi)"; "Corndog (hotdog), Sandwich (hamburger), sushi (garlic)"; "Book (desk lamp - lightning), coffee table (bench)"; "Chopstick (spatula) I might add a blind for this item because it pokes zombies in the eye" |
| 25 Sep 00:21 | `1758759698.849929` | Robert | "<@EMPLOYEE_0009_SLACK_ID> I think the table from the underside is really hard to tell what color it is.. we might need a creative solution for this" |
| 25 Sep 00:24 | `1758759845.447389`, `1758759858.109419` | Robert | a "classroom" collection: "protractors/pencil/ruler/blackboard/atomic molecule/book/abacus" |
| 25 Sep 10:39 | `1758796774.595819` | Vincent | "This isn’t what you wanted when you say increase thickness right?" (HP bar) |
| 25 Sep 10:40 | `1758796815.758229` (root, 9 replies) | Vincent | image; replies: Robert `1758822289.405049` "Too thick? I asked for 2x, do you think that's too much?"; `1758822305.162149` "That bar is as thick as the bike kid's head lol"; Julia `1758825258.755199` "I like it" |
| 25 Sep 19:51 | `1758829860.473499` | Leonard | "I still think Zombie Match’s monetization vector with 5 upgrades per item and you bringing many items to the battle is gonna be very shallow" |
| 29 Sep 02:48 | `1759114097.776589` | Leonard | "For the playable - should we pause the effort if they haven’t started yet?" |
| 29 Sep 02:48 | `1759114127.213749` (root, 3 replies) | Leonard | "I’m worried that we pivot the core game and then playable dev money will be wasted. It’s not nothing" |
| 29 Sep 10:30 | `1759141833.339099` | Brian | "Makes sense, I sent them the assets, but as far as I know, they haven’t started yet" |
| 29 Sep 10:31 | `1759141909.436389`, `1759141916.767179` | Brian | "But if we are going to stop the process, we should say it asap"; "because today they asked me another question about rigging related to the animations" |
| 29 Sep 18:52 | `1759171957.791499` | Robert | "we decided to YOLO and move up card introduction earlier … the ice cream bar level will have to move up as well" |
| 29 Sep 18:55 | `1759172119.133819` (root, 9 replies) | Julia | "Okay, I'll simplify it and make a level from just 2 ice-creams. …" |
| 29 Sep 18:56–18:57 | `1759172166.547199`, `1759172239.701249` | Robert | "So we were thinking just replace the broom tutorial with the first freeze item that was originally at level 17. So 17 -&gt; level 5"; "Yeah I said just drop the broom tutorial, it's such a useless item that no one is gonna shed a tear" |
| 29 Sep 19:06 | `1759172801.164409` | Leonard | "we can simplify it and make blunder = death" |
| 29 Sep 19:08 | `1759172937.229039` (root, 4 replies) | Julia | "I turned the level into this. This is just enough icecream to kill the chef. …" |
| 29 Sep 19:13 | `1759173180.192809` | Julia | "<@EMPLOYEE_0026_SLACK_ID> You can work on  the tutorial level is There `[PERSON_NAME_0019]/sep30levels`" |
| 29 Sep 19:21 | `1759173697.534529` | Robert | "so something where you're hunting a grenade, or something that counter the monster" |
| 29 Sep 23:44 | `1759189466.554739` | Robert | file `20250929-2343-06.3663619.mp4`; "<@EMPLOYEE_0005_SLACK_ID> Got new colored version of cactus, chainsaw and cones that can probably come in handy:" |

Nothing in the window names picks for the playable, the bow, an arrow or the iron. The rest of 29–30 Sep is the casual-versus-hardcore argument and Robert's bot-install analysis (`1759207989.371869`). Last message: `1759260933.283799`, 30 Sep 19:35.

Context just before the window (same channel, the playable thread of 22 Sep, root `1758567201.262949`): Brian `1758568735.563539` asks Julia for a test level; Julia `1758569824.148029` "Do you want to try a cute level with lots of grenades and shruiken then? Total guy focus"; Robert `1758569872.578829` "Doesn't really matter", `1758569885.985319` "I think we should remain as is". No message in that thread names eight objects.

### `#zombie-art` (`C08R8CHB0QL`)

| UTC | Id | Who | Gist or quote |
|---|---|---|---|
| 23 Sep 16:03 | `1758643407.813359` | Claire | image; "New sushi set and blackboard texture <@EMPLOYEE_0016_SLACK_ID>" |
| 24 Sep 22:15 | `1758752145.583769` (root, 5 replies) | Robert | "<@EMPLOYEE_0009_SLACK_ID> Hey here is a quick win, can we make a colorized version of the cactus plant? Let's just have different pot colors:" |
| 24 Sep 22:16–22:17 | `1758752162.419659`, `1758752175.984189`, `1758752194.726809`, `1758752201.202089`, `1758752230.530009` | Robert | "It's good because our flower pot has the same orange vase with different flower color"; "It would be nice to have a plant where the plant is the same color but in a different colored vase"; "Feel free to make the pot more "ceramic" feel like the shiny toilet"; "so slightly glossy"; "Like our "indoor plant" item" |
| 24 Sep 22:28 | `1758752921.740419` | Robert | "Candy 1 has texture atlas issues, I think it's got sushi texture:" |
| 24 Sep 23:01 | `1758754866.994649` | Robert | "Let's also get a colorized versions of the cone:" |
| 24 Sep 23:01 | `1758754916.837729` (root, 1 reply) | Robert | "I would like to use the dartboard but currently There is no way we can tell the color apart only from the rim of the board:" |
| 24 Sep 23:02 | `1758754934.453469` | Robert | "So we'll have to get creative and apply some coloring some how from all sides without it looking weird." |
| 25 Sep 05:38 | `1758778684.416629` | Marcus | "The trafic cone is always white and orange or full yellow" |
| 25 Sep 14:02 | `1758808937.107229` | Claire | "<@EMPLOYEE_0016_SLACK_ID> I pushed the changes you mentioned above in new pr. " |
| 26 Sep 16:27 | `1758904025.123869` (root; `reply_count` 1, `latest_reply` `1758904103.894649`) | Julia | "<@EMPLOYEE_0009_SLACK_ID> Can we have arrow to go with the bow?" |
| 26 Sep 16:27 | `1758904033.633169` | Julia | empty text, no file |
| 26 Sep 16:28 | `1758904103.894649` | Claire | "Of course" |
| 29 Sep 15:30 | `1759159849.386619` (root, 3 replies) | Martin | desert theme for Endless Mode (background, not objects) |
| 29 Sep 23:59 | `1759190391.487809` (root, 6 replies) | Robert | "<@EMPLOYEE_0009_SLACK_ID> The rocking chair probably does not have enough color to distinguish from one to another:" |
| 30 Sep 06:48–06:49 | `1759214935.006959`, `1759214972.260789` | Claire | "do you mean it's hard to select the color variant in game?"; "What do you prefer, I can add some extra parts to change colors or you want to use this as only 1 color object?" |
| 30 Sep 07:35 | `1759217718.139879`, `1759217724.530939` | Robert | "Probably have to think of ways to add extra parts"; "But I'm not sure how.." |
| 30 Sep 07:39 | `1759217971.911279` | Claire | "I can try to add more cloth to top/back area, and maybe add some soft pads to bottom part maybe" |
| 30 Sep 12:17 | `1759234636.683949` | Claire | two images; "I added these parts as color changable parts, I hope this wont look weird" |
| 30 Sep 15:53 | `1759247618.321069` | Claire | image; "<!here> Progress on new objects." |
| 30 Sep 16:07 | `1759248458.722989` (root, 1 reply) | Julia | "Oh, I can see so many possibilities of cancer levels with those pigs and mixing mugs with the frizbees" |
| 30 Sep 16:27 | `1759249627.370789` | Martin | "*Port theme* to have more variants to choose for Endless or Main gameplay mode" |

### Robert's posting hours, September 2025 (UTC hour: count)

- `#zombie-design` (336 posts): 00:13, 01:1, 02:4, 04:6, 05:16, 06:2, 14:18, 15:39, 16:7, 17:38, 18:31, 19:51, 20:11, 21:10, 22:66, 23:23. None at 03 or 07–13.
- `#zombie-art` (144 posts): 00:4, 02:4, 03:2, 04:1, 05:4, 07:2, 14:5, 15:17, 16:58, 17:3, 18:3, 19:3, 20:4, 21:16, 22:13, 23:5. None at 01, 06 or 08–13.
- All channels (3,119 posts): 00:158, 01:140, 02:79, 03:27, 04:144, 05:154, 06:22, 07:60, 08:3, 13:1, 14:79, 15:223, 16:235, 17:472, 18:351, 19:219, 20:194, 21:148, 22:166, 23:244. None at 09–12.

## 4 Sound

`#zombie-sfx` (`C09A7PDFYCV`, public, 7 members, Julia can-see YES) has one month file, 2025-08, 66 messages, 13–18 Aug; posters Calvin, Robert, Julia, Leonard, Marcus. It covers the soundtrack and the endless-mode combo-meter sound only. The other cues are attested by file names in the repository tree (`Assets/MyAssets/Audio/`, 277 audio files) and by other channels.

| Vendor's item | Base name | Who | Statements on where it came from |
|---|---|---|---|
| Matching sound (combo meter, endless mode) | `Assets/Scripts/EndlessMode/SFX/RPG_item_collecting_1` … `_15` (14 `.wav`, #7 `.mp3`) | Calvin, from Robert's sample | `D050QE3CXRU/1755030591.532519` (Robert to Calvin, 12 Aug): "First one is in endless mode, each time as the combo meter goes up, it needs to make a sound, and the higher the combo meter, the higher pitch". `D050QE3CXRU/1755103670.235929` (Robert, 13 Aug): file `11L-RPG_item_collecting_-1755103543181.mp3`, then `1755103679.389789` "Like if we had this, but in scale". `C09A7PDFYCV/1755458431.125029` (Calvin, 17 Aug): files `RPG_item_collecting_1.wav` … `_10.wav`. `C09A7PDFYCV/1755464752.078539` (Calvin): "I used the sample you gave me and increased and lower the pitch, would you need more or 10 are okay?". `C09A7PDFYCV/1755545686.750969` (Calvin): "Reaper is a good tool to normalize sounds btw.. I used to lower the pitch on the sample you gave me and create the scale. ⏎  ⏎ then you just export it as .wav". `C09A7PDFYCV/1755553677.150799` (Calvin): `RPG_item.rar`, "here are 15 in total." Robert `1755555277.111889`: "Perfect". Calvin's own ElevenLabs outputs carry the same prefix: `11L-Clean_game_combo_sou-1755040905997.mp3` (`D050QE3CXRU/1755041023.729229`, "I'm trying to generate a prompt for elevenlabs for the sound effect"), `11L-Arcade_coin_pickup,_-1755218307800.mp3` (`C09A7PDFYCV/1755218493.186069`). That Robert's sample was generated with ElevenLabs is inference from the file name; no message says so in words. |
| Matching sound (main game) | UNVERIFIED which clip. Candidates by name: `Merge.wav`, `Merge_old.wav`, `ItemMatchNoTarget.wav`, `multiplierFlip.wav` | — | no statement found |
| Rocket / cannon sound | `Artillery Cannon Firing Sound.mp3` | Robert names it | `C0880U9751A/1741825912.931869` (Robert, 13 Mar): "The sound file is "artillery cannon firing sound"". `C09A7PDFYCV/1755541416.578719` (Robert): "Please keep in mind this will play simultaneously as the cannon sound, so it needs to be bold". Source: no statement found. |
| Explosion | `Explosion_Deep.wav`, `Explosion_HighPitch.wav`, `GasCanExplosion.wav`, `GasCanExplosion2.wav`, `Distant Nuke Explosion Long.wav`, `fireworxExp.mp3` | Marcus added one for the bike kid | `C08R8CHB0QL/2025-08.json#/40` (Marcus): "also added explosion sound for him". `C08R27X0EAH/2025-05.json#/50`: "Also added a temp explosion sound for propane tanks". Which clip is the grenade's, and any source, UNVERIFIED. |
| Success | `Win.wav`, `Win_old.wav` | — | no statement found |
| Failure | UNVERIFIED. No audio file in the tree matches Lose, Fail, Defeat or LevelFail; `Retry.wav` exists. | — | — |
| Background music | `InGameSoundTrack1.mp3`, `InGameSoundTrack2.mp3`; also `zombie-256804.mp3` and `puzzle-game-bright-casual-video-game-music-249202.mp3` | Leonard (March), Calvin (August) | `C0880U9751A/1741750574.673919` (Leonard, 12 Mar): file `zombie-256804.mp3`, "core game music"; `1741750585.124639`: file `puzzle-game-bright-casual-video-game-music-249202.mp3`, "main menu music"; `1741750645.173869`: "unless you guys hate them these 2 will do". Source of those two: no statement (the name-plus-number pattern is a library-download pattern; that is inference). `C0880U9751A/1754615791.696679` (Robert, 8 Aug): "<@EMPLOYEE_0006_SLACK_ID> Can you find me a soundtrack for in-game that match our game and it doesn't over power our sound effects?". `C0880U9751A/1754633160.681069` (Calvin): files `zombie-1.mp3`, `zombie-2.mp3`. `C05KNDCHAAG/1755195783.942099` (Calvin, 14 Aug, `#company-internal`): "which soundtrack you think fits better for endless mode? ⏎ I'm open for any suggestions, it's AI generated". `C05KNDCHAAG/1755265832.789579` (Calvin): "basically these 2 songs were a cover of the 1st version". `C093LEZGF6J/1755216157.646209`: commit by calvin.price "Added soundtrack extended version". |

**Licence and ownership statements.**
- The Soundly record: `D05UDNCCFEW/1757003624.797399` (Marcus to Robert, 4 Sep 2025 16:33): "is your Soundly licence app its locked on ip or something? cant u make like a funky password on it and give me so i can get sounds as well". Robert: `1757008065.541269` "it's google single sign on", then `1757008285.488349` shares a login (credential in the record, not reproduced), `1757008437.587099` "pw shared". Marcus `1757009502.777599`: "I probably gona need it with any effect that I do". Julia can-see: not checked for this DM; she is not one of its two posters.
- Robert's sources: `C05UQKDLGAU/1724968883.174899` (29 Aug 2024, `#god-vfx`): "and I got a subscription for Soundly so I can get lots of good audio for all sorts of stuff". `C05V5FNLB9V/1727497485.933839` (28 Sep 2024): "pond 5, Soundly, and all the Unity asset packs I bought"; `1727497617.465029`: "I have the paid version so you just tell me what you like". `C07JYF2CFFU/1737054449.137119` (16 Jan 2025, `#god-sfx`): "I use Soundly"; `1737054470.440019`: "I also have a bunch of Unity asset packs with sounds"; `1737054601.692709`: "This is one of the packs that I have, among others: <https://assetstore.Unity.com/packages/audio/sound-fx/universal-sound-fx-17256>". Leonard in the same thread, `1737052440.229129`: "then we either buy or if non-licensed just get it for free".
- Marcus: `C0880U9751A/1754632671.128919` (8 Aug 2025): "I need a Soundly pro account. I wasted a lot of time when I did the vfx to try to combine some sfx cuz I couldn't get the pro ones."
- **In Julia's own DM with Robert** (`D05GU6L0XFH`, can-see YES), 10 Sep 2025: Julia `1757518996.091879` "By the way, tablets have Microsoft sound. Isn't that a copyright violation thing?"; Robert `1757519014.168949` "yes", `1757519016.342059` "not the tablet", `1757519019.927939` "the laptop error", `1757519060.984519` "and yes will swap out the laptop sound, it's the 2 sounds that needs to be swapped, the windows error sound + shutdown", `1757519110.188779` "the tablet sound I believe is generic, the "whoooop"", `1757519486.469369` "It was from one of those copyright free websites". Tree file names that fit: `ComputerError.mp3`, `ComputerBootup.mp3`, `WifiError.wav`, `TabletMessage1.wav`, `TabletMessage2.wav`. Whether the swap happened is UNVERIFIED.
- CodeRabbit on Calvin's music PR `match3d#381`, mirrored at `C093LEZGF6J/1755208790.707609` (14 Aug): "*Confirm licensing/source attribution for the audio* … The filename suggests it was edited with mp3cut; ensure you have the right to distribute this audio (commercially, if applicable) and that attribution/records are stored in the repo". The file is `Assets/MyAssets/Audio/zombie-1 (mp3cut.net).mp3`.
- Fonts: `D05TZ6N23F1/1744034203.976219` (Marcus to Martin, 7 Apr): "but always keep copyright document for them fonts if they are commercial free if not just buy"; Martin `1744034225.113789`: "There are a lot of sites but I think google fonts is most reliable".
- First playable: `C06DJBJL798/1743772532.567359` (Julia, 4 Apr, `#zombie_marketing`): "Do you guys want to use in game SFX and soundtrack for the playable ad or should we explore something more dramatic for the ad experience?"; Frederick `1743832581.671159`: "I like that it'll be editable. But I vote we rely on the vender's expertise and go with ad appropriate soundtrack for our first version."; Julia `1743839448.589949`: "Okay, I will look at some royalty free music this weekend." Brian then sent the game's sounds to the vendor with no ownership check on record: `C08H78VJG80/1744059855.381899`, file `DominoDelight-harmonygames-Sounds.zip`.
- Leonard's Pixabay links of 7 Apr (`C0880U9751A/1744058252.892289` and the four after it) are for a marketing video, not the game.
- Searches with no hit over `messages/*/202[45]-*.json`, scan complete: "sound library", "epidemic sound", "InGameSoundTrack", "merge sound".

## 5 People

| Slack id | Name | Roster role | Status at clock |
|---|---|---|---|
| `EMPLOYEE_0032_SLACK_ID` | unidentified. `entity.py`: "kind=unidentified", Slack only; token-linked, not joined, to Linear `usr_EMPLOYEE_0032`, GitHub `EMPLOYEE_0032_GITHUB_USERNAME`, Confluence `user_EMPLOYEE_0032`. Addressed in base as `[PERSON_NAME_0120]`. Card SC-60. | none on the roster. In base he acts as a Unity engineer (PRs `#452`, `#453`, `#457`, `#461`, `#469`). | no `status_at_clock` (listed under `slack_only_ids`); last Slack 2025-09-30T16:04:07Z, last GitHub 2025-09-30T15:37:03Z |
| `EMPLOYEE_0002_SLACK_ID` | Marcus Bennett | Artist / Design (Contacts: "Artist (VFX & Animation)") | `active_sep_2025_quiet_in_oct` |
| `EMPLOYEE_0012_SLACK_ID` | Vincent Parker | Game Systems Engineer / Engineering | `active_sep_2025_quiet_in_oct` |
| `EMPLOYEE_0004_SLACK_ID` | Samuel Turner | Game Designer / Design | `active_sep_2025_quiet_in_oct` (last Slack 2025-09-29) |
| `EMPLOYEE_0025_SLACK_ID` | Arthur Blake | Co-founder & CTO / Executive | `active_sep_2025_quiet_in_oct` |

Also resolved on the way: `EMPLOYEE_0033` Martin Walsh (Game Designer; in base he posts the UI art), `EMPLOYEE_0003` Oliver Brooks (Senior Game Engineer).

**September 2025, all 149 channel-month files read (21,657 messages); system messages excluded.** DM partners are the other poster in the September file.

| Person | Posts | Top five containers (posts) | UTC hours with posts |
|---|---|---|---|
| Arthur Blake | 602 | `#executives` `C07C2866011` (113); DM Leonard `D04UGG61DUM` (92); DM Vincent `D06477JGUKT` (92); DM Samuel `D06KV30TPL4` (48); `#zombie-bugs` (36) | 11–03; none at 04–10. Peak 16 (99), 20 (78). Calendar zone America/New_York. |
| Marcus Bennett | 1,049 | DM Martin `D05TZ6N23F1` (313); DM EMPLOYEE_0032 `D07FZ9EH13Q` (165); DM Calvin `D05U73FNDDL` (105); DM Vincent `D070FDB7GM8` (102); DM Oliver `D07G4S4CVM5` (84) | 04–20; 97 % inside 08–17 |
| EMPLOYEE_0032 | 890 | DM Vincent `D07GJJBFHA5` (515); DM Marcus `D07FZ9EH13Q` (149); DM Oliver `D07GGG4M3DK` (48); `#zombie-match3d` (41); DM Arthur `D07GJJBLGFK` (40) | 07–18, one at 22 |
| Claire Morgan | 117 | DM Julia `D05HMBQUC8Z` (29); `#zombie-art` (25); DM Marcus `D05V2N6PZNU` (23); DM Brian `D076Y0SDV18` (21); DM Robert `D0506EUNTPB` (8) | 06–18. Calendar zone UTC+03:00. |
| Brian Foster | 2,607 | DM Vincent `D0770ET1HV2` (1,667); DM Calvin `D0770ET6WBW` (146); DM Oliver `D07GK9QQG7M` (106); DM Robert `D077ALC9VK3` (95); DM Leonard `D076PSEBC4D` (94) | 06–21. Calendar zone UTC+03:00. |
| Frederick Stone | 173 | `#executives` (73); DM Leonard `D05S58U4SAK` (70); `#bridge-pitch` `C096HFA5Z8W` (9); vendor channel (5); `#zombie-match3d` (4) | 13–23, plus 01 (2), 04 (7), 05 (1). Peak 18 (37). Calendar zone America/Los_Angeles. |
| Calvin Price | 589 | DM Oliver `D07GCPNJPSA` (179); DM Brian `D0770ET6WBW` (121); DM Vincent `D06UPGF5PQV` (74); DM Owen Baker `D05S1S2H55M` (61); `#zm-animations` (42) | 13–01, strays at 02, 04, 06, 07. Calendar zone America/El_Salvador. |
| Leonard Hayes | 2,842 | `#executives` (733); DM Robert `D04UP2L3E3S` (490); `#bridge-pitch` (286); `#zombie-bugs` (252); `#zombie-design` (240) | 14–07, strays at 12–13; none at 08–11. Calendar zone America/Los_Angeles. |

## 6 Two of Julia's DMs

### Julia–Claire, `D05HMBQUC8Z` (can-see YES)

Turkish throughout. August: 15 records (Claire 8, Julia 5, two empty posts by `PERSON_6089_SLACK_ID`). September: 55 (Claire 29, Julia 26). **Last base message:** `1758732588.831919`, 24 Sep 2025 16:49:48, Claire: "aa o da güzel fikirmiş bak aşlskdaşlkds".

Words in Aug–Sep: `banyo` 0, `bathroom` 0, `UV` 0, `unwrap` 0. `texture` appears three times: `1758302436.361369` (Julia, 19 Sep: "[USERNAME_25073] varolan texturelardan"), `1758306058.744639` (Claire), `1758555266.534569` (Claire).

Claire, verbatim:
1. `1754557631.780369` (7 Aug 09:07) "Dün attım kuzum noldu"
2. `1754557981.895689` (7 Aug 09:13) "Kuzum sportsun altında Pool balls var bir de pool cue stick, beverages da sodalar var bir de cola, bir de miscellaneous diye bir klasör açtım yeni orada da harfler var. "
3. `1754558047.993609` (7 Aug 09:14) "Dün aslında [PERSON_NAME_0120] merge lemişti main e "
4. `1754558310.218619` (7 Aug 09:18) "Hııı anladım kuzum "
5. `1756900105.397889` (3 Sep 11:48) "dinlen bol bol uyumaya çalış"
6. `1756914190.014889` (3 Sep 15:43) "Tamam kuzum sevindim :heart: oyalamıyım seni daha fazla dinlen güzel güzel :[USERNAME_50319]: "
7. `1758300559.154229` (19 Sep 16:49) "Kuzum yaparım tabi, pazartesi onu eklerim"
8. `1758300701.692859` (19 Sep 16:51) "Sen denk gelirsen bana match factory de sushi ekran görüntüsü atarsan süper olur"
9. `1758301775.790279` (19 Sep 17:09) "benim için aşırı kolay oyuncular için aşırı zor obje "
10. `1758306058.744639` (19 Sep 18:20) "Belli olmaz mı sence kullanışmış texture lar? "
11. `1758555266.534569` (22 Sep 15:34, with `image.png`) "Daha texture'lar final değil ama senin seti hazırlıyorum"
12. `1758556705.136469` (22 Sep 15:58) "yok kuzum almaz, 2li [PERSON_NAME_0027] bi chopstick istiyorsun değil mi"
13. `1758732040.478809` (24 Sep 16:40, with `image.png`) "şundan da yapayım bence ne dersin senin dediğine ayrıca"
14. `1758732129.660379` (24 Sep 16:42) "Ama o tırnak gibi algılandığı için arada kaynadı ldklskdlk"

Register: lower-case, short, "kuzum" in most messages, English nouns dropped into Turkish (texture, merge, main, chopstick, pool balls), emoji, keyboard laughter. None of her Aug–Sep messages is longer than message 2. In channels she writes English (`#zombie-art`, §3).

### Julia–Frederick, `D05SD5QLG94` (can-see YES)

English. July 14 records, August 18, September 4. **Last base message:** `1758221424.223519`, 18 Sep 2025 18:50:24, Julia: "Last time we didn't give them access, we just put what they needed in a zip file and sent it over." Frederick's last: `1758220925.518329`, 18 Sep 18:42:05. **Nothing on 29–30 Sep** (no record after 18 Sep; no October file).

Frederick, verbatim (all of his Aug–Sep messages):
1. `1756230709.970659` (26 Aug 17:51) "There are needs related to video ads. But if we are just talking statics, I can't think of anything other than potentially refreshing the screenshots."
2. `1756232330.990849` (18:18) "Do you think it's fair to ask him to mock up screenshots he thinks could outperform our current set?"
3. `1756232394.993239` (18:19) "I'm not the most artistic or creative guy. So I might not be the best guy to give him the vision of what the screenshots should look like."
4. `1756232453.612999` (18:20) "It's pretty easy to A/B test new screenshots on Google and see if a new theme improves performance. So low risk to test if we get another set of screenshots."
5. `1756234644.700299` (18:57) "I issued him a ticket. <https://linear.app/harmonygames-games/issue/ART-792/zm3d-marketing-screenshots-round-3>"
6. `1756235226.664869` (19:07) "Oh man. First time I’ve ever been scolded for writing a ticket. It’s always been the other way around for me. :rolling_on_the_floor_laughing: "
7. `1756235320.793439` (19:08) "I'll ping him directly now"
8. `1758220925.518329` (18 Sep 18:42) "Hey [PERSON_NAME_0040], PlayableX is looking for these assets to build the ZM3D playable. Can I ask who the best person would be to grant them access? ⏎ • *3D assets*: .fbx, .glb, or .blend (when exporting .fbx, please make sure it’s exported in *Binary format*, not ASCII) ⏎ • *2D assets*: .png (for 2D animations, character parts need to be separated into pieces) ⏎ • *Font*: .ttf or .woff2 ⏎ • *Sound*: .mp3 or .wav"

Julia's three replies on 18 Sep: `1758221343.478869` "Hey, [PERSON_NAME_0036]. [PERSON_NAME_0092] fished out the assets for the Domino playable before so I think he's your guy."; `1758221397.722469` "I would also ask Marcus if you're going to use 2D zombie animations because he'd made them with bones."; and the last message above. Frederick opens with her nickname (masked), writes American English ("PlayableX is looking"), full sentences.

## 7 Linear

- **Workflow states.** The export has no workflow-state collection (`data.json` arrays: `/users`, `/teams`, `/projects`, `/issues`, `/comments`, `/team_memberships`, `/attachments`). `state_id` holds the state's name. State ids and types are therefore UNVERIFIED. Names in use on the 597 ART issues: Done 488, Canceled 77, Todo 12, In Review 11, Team Epic 4, Backlog 3, Duplicate 2. `/comments` is `[]`.
- **`ART-790`** (full record): `{"id":"ART-790","project_id":null,"team_id":"team_ART","parent_id":null,"assignee_id":"usr_51f5f16d46e8cf55","creator_id":"usr_175c0d7bc72ed244","state_id":"Todo","cycle_id":null,"identifier":"ART-790","number":790,"title":"Updated ZM Marketing Screenshots","description":"Can we get updated Marketing Screenshots that reflect our new zombies and show the larger play area? For zombies, I'd suggest we go with mailman, karen, kid, and Chef as shown here. I'm not sure who took the original screenshots of the play area. If we can get those showing the larger size and newer zombies, that would be ideal. [https://www.figma.com/design/TvRw8na5iGd3NynbSRUGFy/Zombie-Match-3D?node-id=13-6&p=f&t=Jqf5xVlUah8L7XRr-0](https://www.figma.com/design/TvRw8na5iGd3NynbSRUGFy/Zombie-Match-3D?node-id=13-6&p=f&t=Jqf5xVlUah8L7XRr-0)","priority":0,"estimate":null,"due_date":null,"started_at":null,"completed_at":null,"canceled_at":null,"archived_at":null,"time_in_status_minutes":null,"labels":[],"links":[],"relations":[],"is_archived":false,"created_at":"2025-07-09T18:53:42Z","updated_at":"2025-07-09T18:53:42Z"}`. Creator Frederick, assignee Martin Walsh. No children.
- **`ART-792`** (full record): `{"id":"ART-792","project_id":null,"team_id":"team_ART","parent_id":null,"assignee_id":"usr_51f5f16d46e8cf55","creator_id":"usr_175c0d7bc72ed244","state_id":"Team Epic","cycle_id":null,"identifier":"ART-792","number":792,"title":"ZM3D - Marketing Screenshots round 3","description":"Can you use your eye for composition to mock up a new set of potential screenshots to A/B test against our current set? Feel free to completely re-envision the theme. That is, don't feel like you need to follow any of the current design choices — such as limited the matching items to a single color, keeping the matching area the same size as it currently is, or even displaying the matching area at all.","priority":0,"estimate":null,"due_date":null,"started_at":null,"completed_at":null,"canceled_at":null,"archived_at":null,"time_in_status_minutes":246277,"labels":[],"links":[],"relations":[],"is_archived":false,"created_at":"2025-08-26T18:57:06Z","updated_at":"2025-08-26T18:57:06Z"}`. No children.
- **Do ART issues have children?** Yes. 332 ART issues carry a `parent_id`, under 111 distinct parents (87 in ART, 24 in other teams). Largest: `ART-386` GAMEPLAY BETA (13 children, Canceled), `ART-501` QUEST Feature (12, Done), `ART-78` ART GAMEPLAY (11, Done), `ART-146` ART SAGA MAP (11, Done). The only parent in state Team Epic with children is `ART-683` POLISH (9 children: Canceled 5, Done 3, Team Epic 1), created by `usr_Victor Barnes` on 2024-09-04.
- **Claire's ART tickets.** She created 36, between 2023-08-17 and 2024-08-01; 51 are assigned to her, the newest created 2024-09-24 (`ART-714`). Examples:

| Key | Title | State | Parent |
|---|---|---|---|
| `ART-272` | Sculpting | Done | `ART-266` |
| `ART-273` | Topology/Low Poly Model | Done | `ART-266` |
| `ART-274` | Baking Details / Texturing | Done | `ART-266` |
| `ART-275` | Look Dev / Shaders | Done | `ART-266` |
| `ART-276` | Optimizing / Shaders | Done | `ART-241` |
| `ART-277` | Optimizing Mega Tiles | Done | `ART-200` |
| `ART-278` | Marketing Images For Sophie | Done | none |
| `ART-651` | Train Backgrounds | Canceled | none |
| `ART-652` | Desert Zone BG Modeling | Canceled | `ART-651` |
| `ART-655` | Objects Implementation to Game | In Review | `ART-609` |
| `ART-656` | Concept ART | Done | `ART-639` |
| `ART-657` | Modeling & Texturing | Done | `ART-639` |

- **ART activity in 2025.** The last twelve ART issues: `ART-771` to `ART-780` (Feb–Apr 2025, all by Martin Walsh except `ART-774` "Zombie Match 3D - Marketing Screenshots" by Frederick), then `ART-790` and `ART-792` by Frederick. Brian created one ART issue ever, `ART-754` "New Loading Screen Visuals" (Done, assignee Martin, completed 2025-01-17).
- **Where object work is ticketed now.** All 55 issues created in September 2025 are in `team_ZOM` (creators: Vincent 22, Robert 15, Brian 13, Marcus 4, Leonard 1). 82 of Claire's 136 assigned issues are ZOM. `ZOM-97`: title "REVISION FOR ITEMS", description "Create subtickets for items to change/improve", creator Claire, assignee `usr_Robert`, state Todo, labels ["3D Art","Improvement"], created 2025-04-25T11:41:49Z, updated 2025-07-03T09:33:21Z. It has 51 children (Done 46, Todo 4, Backlog 1), all assigned to Claire, 48 created by her, 3 by Robert. Titles are object names: `ZOM-98` Bathroom Scale, `ZOM-101` Washing Machine, `ZOM-102` Barrel, `ZOM-103` Bath Tub, `ZOM-105` Iron, `ZOM-128` Safe, `ZOM-129` Hair Dryer, `ZOM-176` "3. Wash Basin Cabinet", `ZOM-179` "6. Coffee Machine and Ice Cream Machine", `ZOM-241` "16. Oven", `ZOM-264` Toaster Improvement, `ZOM-329` Rolling Pin, `ZOM-330` Slippers, `ZOM-332` Bathtub, `ZOM-333` Toilet, `ZOM-335` Record Player, `ZOM-342` Indoor Plant (Todo), `ZOM-343` Watering Can. Descriptions are one line, e.g. `ZOM-241` "make it rounder so it will match with other objects like fridge", `ZOM-267` "texture improvement". Newer object requests are single ZOM tickets raised from Slack: `ZOM-513` "Convert Maracas into multi-color variant-enabled" and `ZOM-514` "Request to add motorcycle helmet as a survival item" (both by Robert, 2 Sep 2025, In Progress, assignee Claire, no parent). ZOM state names seen: Done, Todo, In Progress, Canceled, In Validation, Duplicate, Backlog, Regression.

## 8 Vendor channel: the scenarios and the Scenario 1 thread

The scenarios as the vendor described them — `C08H78VJG80/1756393065.804409` (PERSON_6078, 28 Aug 14:57:45, root with 1 reply):

> Hello <@EMPLOYEE_0038_SLACK_ID>,
> You can find the ideas we've been working on for this playable at the <https://docs.google.com/document/d/179Od87P5qUTLYyrJylt5Jo7E-i15V8WuoWwCnuvIRv0/edit?tab=t.0|link> below.
> • *Scenario 1:* This is based on the core game mechanics.
> • *Scenario 2:* This is built around the bomb mechanic on the in-game board.
> • *Scenario 3:* This was inspired by high-interaction playables from games like <https://x-ad-assets.s3.amazonaws.com/media_asset/80eaaee61e35a8b9/media|Royal Match> and <https://x-ad-assets.s3.amazonaws.com/media_asset/d021f374efd00f69/index.html|Ma[USERNAME_30464]>.
> • *Scenario 4:* This is a new scenario created as a combination of the previous ones.
> We can start discussing and planning the project based on the scenario you choose.

The linked document is not in base (0 hits for `179Od87P5q` in Docs and Drive, scan complete). Reactions that day: Leonard `1756399976.644599` "^ let’s review the scenarios together"; Julia `1756402043.104259` "I like the Match Factory one"; Vincent `1756404056.404979` "I also liked the third option, but my only concern is that it might not be as exciting as the other two since we don't have an avatar to associate with."

Vendor, `1756452358.461719` (29 Aug 07:25:58):

> Hello <!here>, thank you for your valuable feedback! As <@EMPLOYEE_0012_SLACK_ID> mentioned, if we use a character it will strengthen all scenarios and help players build an emotional connection. If you already have a character, we can integrate it into all scenarios.
>
> If you have a preferred scenario in mind, we’re happy to consider that as well. Our suggestion, however, is to move forward with *Scenario 1 and highlight the basic gameplay*. Presenting the game in its simplest and most authentic form allows players to clearly understand the core mechanic. This way, they can evaluate the game more accurately, and your first tests will deliver much cleaner results.
>
> In short, *a simple playable = strong first impression + clear mechanic focus + lower drop-off*, which ultimately means more reliable test outcomes.

**Thread root `C08H78VJG80/1757695108.506159`** (Frederick, 12 Sep 16:38:28, `reply_count` 4):

> Hi <@PERSON_6078_SLACK_ID>, the way I see it, playables can be good for optimizing for CPIs (fun casual playable but unrelated to core game), optimizing for retention (filter out users that are not going to like your game), or somewhere in the middle. I think Scenario 1 is a good bet for filtering out the players that won't like our game, while remaining true to our core game play.
>
> For Scenario 1, would the user be able to select any items they want and make several matches (if they are good enough)? I like that idea -- but will call out it seems a lot more sophisticated than the Domino Delights playable where the user is essentially on rails and only makes a few matches before the playable ends.

Reply `1757928654.905219` (PERSON_6078, 15 Sep 09:30:54):

> Hi <@EMPLOYEE_0008_SLACK_ID>,
> Thanks for your feedback and thoughts! I agree with your perspective on Scenario 1 being a good way to filter players who might not enjoy the game while staying true to our core gameplay.
> Regarding your question: yes, the idea is that the user can select items freely and make multiple matches if they are skilled enough.

Reply `1757956024.883249` (Frederick, 15 Sep 17:07:04):

> <@PERSON_6078_SLACK_ID> lets go with Scenario 1. From a design standpoint, I think the main elements to figure out are 1) what items are on the board, and 2) what zombies are being smashed.
>
> For items, we want to highlight that different items have different abilities and choose items that might be especially entertaining to the users. I think grenade (powerful), couch (splash damage), plush doll (weak but potentially funny), would be a good start.
>
> For zombies, we have quite a few at this point. Probably best to use a variety.
>
> What are next steps for us to Push this project forward?

Reply `1758022459.227279` (PERSON_6078, 16 Sep 11:34:19):

> Hello <@EMPLOYEE_0008_SLACK_ID>,
> We are planning to start this project on *September 29*. If you can share the assets with us before that date, we’ll be able to start the optimization and animation processes in advance.
> For the items on the board, we can make them editable. This way, aside from the 8-item set that you will provide for the board, you can also test any additional items you’d like to try in the game.
>  For the zombies, we will proceed with animations in Spine. You can select which zombies from the platform you’d like to use in the game. Depending on the overall game size, we can finalize the number of zombies during the project.
> Here are the asset formats we can work with:
> • *3D assets*: .fbx, .glb, or .blend (when exporting .fbx, please make sure it’s exported in *Binary format*, not ASCII)
> • *2D assets*: .png (for 2D animations, character parts need to be separated into pieces)
> • *Font*: .ttf or .woff2
> • *Sound*: .mp3 or .wav

The fourth reply is after 16 Sep: `1758209344.355659` (PERSON_6078, 18 Sep 15:29:04) "hi <@EMPLOYEE_0008_SLACK_ID> Do you have an idea of when you’ll be able to share the assets with us?"

## 9 The 2 Sep thread that names the six objects

`#zombie-art`, 2 Sep 2025. The subject is which items show the "bounce" effect (formerly ricochet) on Martin's item-intro screens.

- `C08R8CHB0QL/1756812767.329279` (Julia, 11:32): "<@EMPLOYEE_0012_SLACK_ID> This table is the latest right? Are we calling ricochet bounce now? <@EMPLOYEE_0033_SLACK_ID>"
- `1756812951.274939` (Martin, 11:35): "Ok but Scissors in the art is not ok for me. Any other bounce items?"
- **Root `1756813716.024339`** (Vincent, 11:48, 8 replies): "There aren't much options other than spiky items. ⏎ round pans ⏎ ladle, ⏎ spatula ⏎ Electric Hair Trimmer ⏎ hairbrush ⏎ Donut With Chocolate Chips"
- Reply `1756813808.942329` (Vincent, 11:50): "Bicycle ⏎ Scooter ⏎ Toy Drum ⏎ Toy Hammer"
- Reply `1756823493.283329` (Robert, 14:31): "All the balls have it"; `1756823496.901819`: "Soccer ball"; `1756823499.214739`: "Basketball"; `1756823509.659399`: "But no color variants"
- Follow-up in Martin's thread `1756826172.817549`: Vincent `1756826422.428419` "if we're giving every item here like iron, ice cream bar, whistle etc. We cannot use soccerball"; Robert `1756826780.516849` "Should we use the soccer ball? <@EMPLOYEE_0012_SLACK_ID> I mean it's the most intuitive in terms of "bounce""

| Object | In the tree | Category | Variant assets |
|---|---|---|---|
| Soccer Ball | yes | Sports | 1 (`Soccer Ball Medium White1`) |
| Basketball | yes | Sports | 1 (`Basketball Medium Orange2`) |
| Toy Drum | yes | Toys | 29 |
| Scooter | yes | Toys | 29 |
| Bicycle | yes | Toys | 29 |
| Toy Hammer | yes | Toys | 29 |

The same thread also names Round Pan, Ladle, Spatula, Hair Trimmer, Hairbrush and Donut With Chocolate Chips (all in the tree). The word "round" in that day's channel belongs to another message: `1756837838.489519` (Robert, on a motorcycle helmet): "Easy to texture, colorize and looks good, also round object".

## 10 Candidate containers for a note about a bad export

| | `#zombie-match3d` `C0880U9751A` | `#zombie-bugs` `C08R27X0EAH` |
|---|---|---|
| Kind, members | private, 25 | private, 23 |
| Julia | can-see YES; 6 posts in the window | can-see YES; 0 posts in the window |
| Messages 24–30 Sep | 64 (33 roots) | 156 (77 roots) |
| By day | 24 Sep 3, 25 Sep 3, 26 Sep 35, 28 Sep 11, 29 Sep 6, 30 Sep 6 | 24 Sep 99, 25 Sep 17, 26 Sep 33, 29 Sep 1, 30 Sep 6; none on 27–28 Sep |
| Posters | Robert 27, Leonard 12, Marcus 7, Julia 6, Arthur 4, EMPLOYEE_0032 2, Oliver 2, Frederick 2, Vincent 1, Linear bot 1 | Oliver 63, Robert 54, Vincent 12, Leonard 10, Arthur 7, EMPLOYEE_0032 6, Marcus 2, `PERSON_6089` 2 (empty posts) |
| Content | the HP-bar request, heating tests, Julia's level PR and her zombie-count warning, Unity 6 render settings, zombie HP scaling, user logs, the Unity upgrade notice, the 0.3.49 iOS release, bot installs | the tutorial-highlight bug and user logs (24 Sep), a Samsung audio bug, double colliders, the addressables and memory thread (`1758905363.341129`, Arthur, 25 replies), a skip-tutorial fix, a shader issue after the Unity upgrade (30 Sep) |

**Is a post about Unity package exports in character there?**
- **Marcus: yes, and `#zombie-match3d` or `#zm-animations` fits better than `#zombie-bugs`.** He built the zombie package and already posts about exports and broken assets:
  - `C0880U9751A/1743528017.706819` (1 Apr): "bypas icons they were looking dark because of a setting, i re-exported them and modified the light in that snapshot scene. … it was a setting on the exported file, they should not be sRGB to look like in the game"
  - `C0880U9751A/1755024352.768559` (12 Aug): "<@EMPLOYEE_0003_SLACK_ID> oups i can see that it has the alpha map but the color map /main tex its having that pink missing map issue"
  - `C0880U9751A/1738678859.796159` (4 Feb): "all of our objects when we export them from our editing app will need to fit inside of 1m cube, and the fbx export seetings need to be set on meters."
  - `C08R27X0EAH/1759250924.694619` (30 Sep 16:48, in a thread): "<@EMPLOYEE_0012_SLACK_ID> now i can see why you asked if this is Unity version problem, <@EMPLOYEE_0003_SLACK_ID> we have here the same issue like with the zombies. them old shaders dont deform no more the sprites with bones, so i had There a lightSweep Box Variant material that has a shader that used to work before now it doesnt deform the mesh no more :disappointed:. The material added a lightsweep across the gold edges part of the box making it more bling bling."
- **Arthur: partly.** In `#zombie-match3d` he posts short project-level notices: `1759175129.233219` (29 Sep 19:45) "<!here> can all Unity users please download this Unity version. We will be upgrading the project shortly."; `1751307531.930769` (30 Jun) "Saw some mobile performance gains and solved some issues with package dependencies."; `1744156602.153749` (8 Apr) "<@EMPLOYEE_0016_SLACK_ID> here is another missing asset". No base post of his is about exporting assets for an outside party. He left `#zombie-design` on 2025-09-11 (`activity.json`).
- **EMPLOYEE_0032: no precedent in either channel.** His "export" posts there are about JSON from Google Sheets (`C0880U9751A/1749655837.457589`: "i will export json from google"). His asset guidance to Brian is in a DM (`D07G5QWN3TM`, 24 Sep: `1758713828.175019` "what u wrote an animation in fbx format, we do not use it, we use Unity animations and they work only in Unity"; `1758713951.054939` "each prefab uses psb file and animation"; `1758714038.422669` "Assets/MyAssets/Audio/... ⏎ for example here").
- Base fact on colours that any export note must respect: Marcus, `C0880U9751A/1741339853.288969` (7 Mar): "The method of changing color of some parts in Unity to create prefab variants should be cool. … The color in Unity it's the fastest one."; Claire to Brian, `D076Y0SDV18/1758713188.374029` (24 Sep): "Şimdi şöyle bunların renklerini Unity de veriyoruz".

## 11 `match3d#460` and `match3d#462`

Both are by Claire (`EMPLOYEE_0009_GITHUB_USERNAME`), merged by Robert, with an empty PR body apart from CodeRabbit's summary on `#460`. The CodeRabbit comments are authored by `PERSON_6026_GITHUB_USERNAME`. Omitted below from each comment: the poem, the sequence diagram of `#462`, the "Agentic pre-merge checks" announcement, the "Summarized by CodeRabbit Free" note and the encoded internal-state block.

### `#460` "New Objects" — created 2025-09-24T08:32:43Z, merged 21:51:38Z; +3093 −11, 49 files; head `claire.morgan_NewObjects_10`

Comment `harmonygames-Games/match3d#460#c_1` (2025-09-24T08:32:53Z):

> ## Walkthrough
> Adds Unity .meta files for new FBX models and prefabs. The FBX metas include full ModelImporter configurations (materials, animations, meshes, tangent space, humanoid/avatar). The prefab metas include PrefabImporter stubs with GUIDs. No code or runtime logic changes.

Files ignored due to path filters (28):
- `Assets/MyAssets/3dModels/SmoothedModels/Food/Chopstick_Pair.fbx`, `…/Food/Chopstick_Single.fbx`, `…/Food/Salmon_sushi.fbx`, `…/Food/Sashimi.fbx`, `…/Food/Veggie_sushi.fbx`
- `…/Fruits/Strawberry.fbx`
- `…/Tool/HandSaw.fbx`
- `…/Toys/Abacus.fbx`, `…/Toys/Atom.fbx`, `…/Toys/DNA.fbx`, `…/Toys/Protractor.fbx`, `…/Toys/Toy_Truck.fbx`, `…/Toys/blackboard.fbx`
- `Assets/MyAssets/3dModels/SmoothedModels/match3dModels_Texture_01.png`, `…/match3dModels_Texture_02.png`
- `Assets/Prefabs/Objects/Fast Food/Chopstick Pair Small Red3.prefab`, `…/Chopstick Single Small Red3.prefab`, `…/Sushi Salmon Small Gray3.prefab`, `…/Sushi Veggie Small Gray3.prefab`
- `Assets/Prefabs/Objects/Miscellaneous/Clef Sign Small Gray3.prefab`, `…/Music Note1 Small Gray3.prefab`, `…/Music Note2 Small Gray3.prefab`
- `Assets/Prefabs/Objects/Tools/HandSaw Medium Blue2.prefab`
- `Assets/Prefabs/Objects/Toys/Abacus Medium Brown2.prefab`, `…/Atom Medium Orange2.prefab`, `…/Blackboard Large Brown2.prefab`, `…/DNA Small Blue2.prefab`, `…/Protractor Small Purple2.prefab`

Files selected for processing (21): the `.fbx.meta` of the five Food models, of `HandSaw.fbx` and of the five Toys models (Abacus, Atom, DNA, Protractor, blackboard), and the `.prefab.meta` of the four Fast Food prefabs, of `HandSaw Medium Blue2` and of the five Toys prefabs. 28 + 21 = 49, so every changed file is listed.

**Does `#460` name an existing object as changed?** Not in words; the comment speaks only of additions. Seven listed files have no new `.meta` in the PR, which in a Unity repository means the file already existed: `Fruits/Strawberry.fbx`, `Toys/Toy_Truck.fbx`, the two shared atlases `match3dModels_Texture_01.png` and `_02.png`, and the three `Miscellaneous` prefabs (Clef Sign, Music Note1, Music Note2). Strawberry, Toy Truck, Clef, Music Note 1 and Music Note 2 are existing objects in the tree. That these seven were modified rather than added is inference from the missing `.meta` files and the 11 deleted lines. Claire had posted "New sushi set and blackboard texture" the day before (`C08R8CHB0QL/1758643407.813359`), and she put `match3dModels_Texture_01.png` in the zip for Brian at 12:12 on 24 Sep (`D076Y0SDV18/1758715927.943809`), before this PR merged.

### `#462` "Objects Revisions and Changes" — created 2025-09-25T11:43:06Z, merged 23:15:41Z; +77 −18, 13 files; head `claire.morgan_ObjectRevisions_08`

Comment `harmonygames-Games/match3d#462#c_1` (2025-09-25T11:43:14Z):

> ## Walkthrough
> Material import mode updated from 0 to 2 in two Unity FBX .meta files, and rigImportErrors/rigImportWarnings fields were removed from their animations sections.
>
> ## Changes
> | Cohort / File(s) | Summary |
> |---|---|
> | **Unity FBX meta import settings**<br>`Assets/MyAssets/3dModels/SmoothedModels/Garden/ChainSaw_smooth.fbx.meta`, `Assets/MyAssets/3dModels/SmoothedModels/Garden/cactus_medium_B_smooth.fbx.meta` | Set ModelImporter.materials.materialImportMode to 2 (from 0). Removed ModelImporter.animations.rigImportErrors and rigImportWarnings entries. |

Files ignored due to path filters (10):
- `Assets/MyAssets/3dModels/SmoothedModels/Food/Candy_1.fbx`
- `Assets/MyAssets/3dModels/SmoothedModels/Garden/ChainSaw_smooth.fbx`
- `Assets/MyAssets/3dModels/SmoothedModels/Garden/cactus_medium_B_smooth.fbx`
- `Assets/MyAssets/3dModels/SmoothedModels/Outdoor/Room_8_Cone_1_Smoothed.fbx`
- `Assets/MyAssets/3dModels/SmoothedModels/Toys/dart.fbx`
- `Assets/Prefabs/Objects/Garden/Cactus Plant Medium Orange2.prefab`
- `Assets/Prefabs/Objects/Sports/Kettlebell Medium Blue3.prefab`
- `Assets/Prefabs/Objects/Tools/Chainsaw Medium Orange2.prefab`
- `Assets/Prefabs/Objects/Toys/Cone Medium Orange2.prefab`
- `Assets/Prefabs/Objects/Toys/Dart Board Medium Blue2.prefab`

Files selected for processing (2): `…/Garden/ChainSaw_smooth.fbx.meta`, `…/Garden/cactus_medium_B_smooth.fbx.meta`.

- 10 + 2 = 12 of 13 changed files; the thirteenth is UNVERIFIED.
- Objects touched: Candy 1, Chainsaw, Cactus Plant, Cone, Dart Board, Kettlebell.
- No new `.meta` appears for any of the ten binary files, so all ten look like existing files that were modified (inference, same reasoning as above). The data tree's only Chainsaw variant is `Chainsaw Medium Yellow2`, while the prefab touched here is `Chainsaw Medium Orange2`; I could not reconcile the two names.
- The export has no per-PR file collection; this comment, its Slack mirror in `#zombie-prs` (`C093LEZGF6J/2025-09.json#/488`; Julia can-see UNVERIFIED, public channel, not a member) and the commit title are the only base text that names the changed objects. Timeline of `#462`: review requested from Robert and EMPLOYEE_0032 at 11:43:07Z, CodeRabbit comment 11:43:14Z, merged and closed by Robert 23:15:41Z.

## Not verified

- The contents of any zip, model, prefab, audio or image file (binary; only names and paths were read).
- The exact commit and date of the repository tree snapshot.
- Which five zombie names sit behind the masks in the 26 Sep list.
- Which audio clip the game plays for a match in the main mode, for the grenade explosion and for a lost level, and the source of every cue except the combo scale, the two March music files' names and the August soundtrack.
- Linear workflow-state ids and types.
- Whether `[PERSON_NAME_0040]` in `D07G5QWN3TM/1758712928.567529` is Julia or Claire.
- Marcus's calendar time zone (not read).

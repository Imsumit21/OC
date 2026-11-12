# Census A — design-side Slack channels (read-only)

Universe: synth-cut, clock 2025-10-01 07:00 UTC. Read only through `research/slk.py` (which calls `Task_Authoring/tools/hg.py search get slack --file messages/<channel>/<month>.json`).
All times UTC. Pointer = `<channel_id>/<ts>`. Quotes are verbatim from the export, including its anonymiser artefacts (`[PERSON_NAME_nnnn]`, `[USERNAME_nnnn]`, capitalised `There` / `Push` / `Apple`, `&amp;`). `⏎` = line break inside a message.
Channel ids: `C090N54TG79` #zombie-design · `C08H78VJG80` PlayableX vendor channel · `C09ATAJ220H` #zm-animations · `C09A7PDFYCV` #zombie-sfx.

## 0 Coverage (channel, months read, message counts, date of last message)

| Channel | Month files that exist (messages) | Months probed and MISSING | Read in full | Last message |
|---|---|---|---|---|
| `C090N54TG79` #zombie-design | 2025-06 (37), 2025-07 (1221), 2025-08 (621), 2025-09 (830) | 2025-02..05, **2025-10** | Requested window 2025-09-15 → end: **457 messages, every one read**. Bonus: 2025-09-01 → 09-14 (373 messages) also read in full (needed for item D "Sept 2025"). 2025-06..08 NOT read; keyword sample only, marked "outside window". | 2025-09-30 19:35 `C090N54TG79/1759260933.283799` |
| `C08H78VJG80` PlayableX vendor | 2025-03 (76), 2025-04 (43), 2025-06 (3), 2025-08 (50), 2025-09 (26) = **198** | 2025-02, 05, 07, **2025-10** | All 198, long messages re-pulled untruncated | 2025-09-30 09:59 `C08H78VJG80/1759226395.551469` |
| `C09ATAJ220H` #zm-animations | 2025-08 (43), 2025-09 (81) = **124** | 2025-02..07, **2025-10** | All 124 | 2025-09-10 00:40 `C09ATAJ220H/1757464811.241579` |
| `C09A7PDFYCV` #zombie-sfx | 2025-08 (66) | 2025-02..07, 2025-09, **2025-10** | All 66 | 2025-08-18 22:14 `C09A7PDFYCV/1755555277.111889` |

Per-day counts in the #zombie-design window: 09-15 91 · 09-16 6 · 09-17 26 · 09-18 13 · 09-19 25 · 09-21 2 · 09-22 125 · 09-23 12 · 09-24 12 · 09-25 37 · 09-26 1 · 09-27 2 · 09-29 89 · 09-30 16. No messages on 09-20 or 09-28.

## A Board objects and items

### A1 Items named for the playable

| Name | What is said (verbatim) | Level | Pointer · speaker · date |
|---|---|---|---|
| grenade | "For items, we want to highlight that different items have different abilities and choose items that might be especially entertaining to the users. I think grenade (powerful), couch (splash damage), plush doll (weak but potentially funny), would be a good start." | not stated | `C08H78VJG80/1757956024.883249` · E0008 · 2025-09-15 |
| couch | same message: "couch (splash damage)". Also a clone source: "the surfboards are cloned off couch"; "bed/wardrobe are just couch clones" | not stated | same; `C090N54TG79/1758063803.640359` E0016 09-16; `C090N54TG79/1757397477.968089` E0016 09-09 |
| plush doll / plushie / duck | same message: "plush doll (weak but potentially funny)". Vendor: "At this stage, the only missing piece seems to be the duck asset used in the reference. Could you also provide that?" Reply carries file `Plushie-and-zombies.zip`: "Sure, I’m sending the files. Thanks for the update" | not stated | `C08H78VJG80/1757956024.883249`; `C08H78VJG80/1758723504.085039` P6078 09-24; `C08H78VJG80/1758729487.922339` E0026 09-24 |
| grenades + shuriken (alternative idea) | "Do you want to try a cute level with lots of grenades and shruiken then? Total guy focus" → answer "Doesn't really matter" / "I think we should remain as is" | — | `C090N54TG79/1758569824.148029` E0005 09-22; `C090N54TG79/1758569872.578829`, `C090N54TG79/1758569885.985319` E0016 09-22 |
| "8-item set" (count, not names) | "aside from the 8-item set that you will provide for the board, you can also test any additional items you’d like to try in the game" | — | `C08H78VJG80/1758022459.227279` P6078 09-16 |
| rocket launcher, projectile (vendor's wording for the weapon) | "*3D Assets:* Zombie models + animations, rocket launcher, projectile, board items (the specific objects you’d like to be used on the board)" | — | `C08H78VJG80/1758283671.878269` P6078 09-19 |
| cannon (HG's wording) | "This way we can have items that increase cannon HP, and have cannon abilities like reflect damage…"; sound "will play simultaneously as the cannon sound" | — | `C090N54TG79/1758667484.394299` E0016 09-23; `C09A7PDFYCV/1755541416.578719` E0016 08-18 |

The final list of items and zombies chosen for the playable is **not stated in any of the four channels** (see B, 09-22 thread: it ends on a hardcore/casual argument, not a list).

### A2 Effects, cards / equipment, and where they sit in the level order

| Name | What is said (verbatim) | Level | Pointer · speaker · date |
|---|---|---|---|
| ice cream bar (freeze item) | "I'm going to increase the ice cream bar size, it's too small in the level introducing it" | "the level introducing it" (number not given here) | `C090N54TG79/1757464517.784799` E0016 09-10; reply "That's be good I think" `C090N54TG79/1757486907.060689` E0005 |
| ice cream bar level | "we decided to YOLO and move up card introduction earlier. <@EMPLOYEE_0026_SLACK_ID> will make the changes in the tutorial, but we have to align on the level design itself since we need to shuffle the levels for the effects to the right place. So the ice cream bar level will have to move up as well, and maybe adjusted if we think it's too difficult." | moves up | `C090N54TG79/1759171957.791499` E0016 09-29 18:52 |
| first freeze item | "So we were thinking just replace the broom tutorial with the first freeze item that was originally at level 17. So 17 -&gt; level 5" · "And then everything else just moves up" | **17 → 5** | `C090N54TG79/1759172166.547199`, `C090N54TG79/1759172172.666169` E0016 09-29 |
| ice-creams (level content) | "Okay, I'll simplify it and make a level from just 2 ice-creams. What level did you decide to put it?" | — | `C090N54TG79/1759172119.133819` E0005 09-29 |
| white icecream (equipped-card look) | "I turned the level into this. This is just enough icecream to kill the chef. The level doesn't have the white icecream, I put it There to show how it look when the card is equipped and level is entered." (image.png) → "Is this okay?" / "Yeah I think that's fine?" / "Okay sending it the level design branch" | — | `C090N54TG79/1759172937.229039` E0005; `C090N54TG79/1759173085.757379`; `C090N54TG79/1759173105.948699` E0016; `C090N54TG79/1759173139.940419` E0005 — all 09-29 |
| ice cream (hit VFX) | "What would have cooler is obviously the ice cube around the head forming after ice cream hits the zombie but we can do it when we have more resources" · "I like the snow floating around" · "Can you try making it more of a throw instead of touching with a wand?" (on `ObjectEfect007.mp4`) | — | `C09ATAJ220H/1756912811.188649` E0002 09-03 (video); `C09ATAJ220H/1756913710.782539`, `C09ATAJ220H/1756913716.800579` E0038; `C09ATAJ220H/1756913816.320139` E0005 |
| broom | "Yeah I said just drop the broom tutorial, it's such a useless item that no one is gonna shed a tear" · "And go \"oh man There was this broom?? Where were you all this time???\"" · "Because blunder != instant loss, [USERNAME_3114] loses the value anyways" | my inference, not stated outright: the broom tutorial sat at level 5, where the freeze item now goes | `C090N54TG79/1759172239.701249`, `C090N54TG79/1759172254.244829`, `C090N54TG79/1759172271.010919` E0016 09-29 |
| card / first item unlock | "We can put the card reward to lvl10 in Zombie lane and unlock the event at17" · "Even if we place the effect at level 10, the Card tutorial would still start at level 17." · "But the actual FTUE leading them to collecting their first item and equipping it will remain unchanged right? (Level 18 I believe)" · "yes, I do think level 18 is too late for item unlock" · "I also think we should give item intro another chance and don’t wait until level 15 - I think we can try something like level 7-10" | card tutorial 17; first equip 18 (before the 09-29 move) | `C090N54TG79/1758180431.930239` E0012 09-18; `C090N54TG79/1758191312.370309` E0026 09-18; `C090N54TG79/1758207259.584079` E0016 09-18; `C090N54TG79/1758207348.326809` E0038 09-18; `C090N54TG79/1758147731.194789` E0038 09-17 |
| effects order (ice, poison) | "OK so if we want to bring effects forward, for example ice at level 12, poison at 15, etc. then we're gonna have to involve <@EMPLOYEE_0005_SLACK_ID> because we have to reshuffle the levels, and put them in a different variant like Variant C v2" · "the first item effect(freeze)" | hypothetical 12 / 15 | `C090N54TG79/1758207220.027239` E0016 09-18; `C090N54TG79/1758207623.333509` E0012 09-18 |
| glue, ice (effects stack) | "\"hmm does glue and ice effect stack?\" And they proceed to test it out and go \"yep\"" | — | `C090N54TG79/1758581234.991559` E0016 09-22 |
| equipped items (insertion rule) | "New rule is that, whatever you equipped comes extra onto your pile" · "I think 2-3 pairs from each slot will do nicely." · "Single pair 100% won't work" · 4 equip slots: "if you have all 4 slots equipped a total of 8 pairs" | — | `C090N54TG79/1757338977.703459` E0005 09-08; `C090N54TG79/1757346584.480749` E0005; `C090N54TG79/1757346830.237929` E0016; `C090N54TG79/1757345691.316079` E0038 |
| shuriken | "You'll encounter the scenario where 3 sets of shuriken demolishes an entire horde, leaving like 15 sets+ on the board when the level ends" | — | `C090N54TG79/1757346964.661209` E0016 09-08 |
| epic gift | "when I’m getting a single pair of let’s say an epic gift that works 50% of the time, I’m annoyed" | — | `C090N54TG79/1757345732.494829` E0038 09-08 |
| bowling ball (rare) | "considering how a level 5 bowling ball rare item deals 152 damage" · "and a level 3 bowling ball deals 80 damage" | — | `C090N54TG79/1758667708.954609`, `C090N54TG79/1758667717.189149` E0016 09-23 |
| iron (uncommon) | "Level 5 uncommon iron deals 100 damage" | — | `C090N54TG79/1758668039.541069` E0016 09-23 |
| item power by rarity | "a common level 0 item has power ~20, and a level 5 has 136. Uncommon level 0 is 30, and level 5 is 200+" · "A level 5 legendary has 100x the power of a level 0 common." | — | `C090N54TG79/1758667286.925349` E0016 09-23 |
| carrot (poison) | "That's not okay, it needs to be a small orange item. We can put orange in instead if the carrot is broken" · "OK, [PERSON_NAME_0050] cacn you disable carrot poison at level 0 then?" · "I thought we agreed on not doing zombie poison in very early levels because of the stutter issues" | level 2 | `C090N54TG79/1756753330.834719` E0005 09-01; `C090N54TG79/1756754548.259429` E0016 09-01; `C090N54TG79/1756751276.912539` E0038 09-01 |
| wine bottle (poison intro) | "Ideally yes, since we aren't introducing them until.. forgot what you put down, wine bottle" | later than level 2 | `C090N54TG79/1756753840.827159` E0016 09-01 |
| level-0 effects switched off | "DOT disabled for level 0 items. Burn/poison/shock only. Critical, _some_ splash and bounce remains." | — | `C090N54TG79/1756846085.656109` E0016 09-02 |
| garlic (multishot) | "I just noticed the garlic on level 6 has multishot, we'll have to disable it." | 6 | `C090N54TG79/1757463859.620729` E0016 09-10 |
| flip flops (multishot) | "Level 32 - has flip flops that has multi shot at level 0, it was fun to play." → "I'd say leave as is… Multishot gets introduced much later anyway" | 32 | `C090N54TG79/1757468174.976609` E0016 09-10; `C090N54TG79/1757486959.759649` E0005 |
| round pans / scissors | "Also, Level 47 should have round pans not scissors because the introduced item changed to that." | 47 | `C090N54TG79/1757337659.125719` E0012 09-08 |
| trumpet | "can we use an item like trumpet in an earlier level? is your progression just a gate for cards that can be obtained, but they can still appear in levels?" → "Yes only as cards, board objects are fine" | — | `C090N54TG79/1756754594.855669` E0016; `C090N54TG79/1756754955.796139` E0012 09-01 |
| card packs | "premium pack", "placeholder legendary pack", "bones pack", "basic packs"; "We see 10 cards on the screen." | — | `C090N54TG79/1756730298.517369` E0012 09-01; `C090N54TG79/1757001097.983639` E0012 09-04; `C090N54TG79/1757477950.880459` E0038 09-10; `C09ATAJ220H/1756997390.649369` E0026 09-04 |

### A3 Item catalogue additions (distinct names; "( )" = item it was cloned from)

| Names | What is said | Pointer · speaker · date |
|---|---|---|
| bowling ball/pins, canned food, boxing gloves | "I added some new items for us to play with… I think we'll need it to Push it to level 200+" | `C090N54TG79/1756772897.827709` E0016 09-02 |
| ping pong paddle, baseball, shuttlecock, saber, golf club | "Added rest of the stuff we have" (colour variants: "Yes") | `C090N54TG79/1756790033.712779`, `C090N54TG79/1756823554.480639` E0016 09-02 |
| flip flops, pineapple mug, scooper, toy truck, toy airplane, toy car, toy boat, new maracas, wardrobe, bed, soda, packpack | "New items: …" · "I put them all under collection 11 for now" · "they are usually clones of existing items, like soda can = canned food" · "bed/wardrobe are just couch clones. None of these are activated in the pool" | `C090N54TG79/1757394475.801429`, `C090N54TG79/1757397456.396079`, `C090N54TG79/1757397464.679759`, `C090N54TG79/1757397477.968089` E0016 09-09 |
| surfboards (4 kinds), music notes (2 types), clef symbol; whistle | "None of them works right now and I'm waiting for Blake to fix the objects not getting converted to box colliders… the surfboards are cloned off couch, the symbols and music notes are cloned off whistle." · "per usual, I put them under collection 11 for the time being" | `C090N54TG79/1758063803.640359`, `C090N54TG79/1758063859.325879` E0016 09-16 |
| letter items | "letter items were in the whistle category" (fixed in a PR) | `C090N54TG79/1757355103.109279` E0012 09-08 |
| Protractor (Pencil), Blackboard (wooden bench) | "New Item Thread, in ( ) is the item cloned from" | `C090N54TG79/1758757016.553559` (root), `C090N54TG79/1758757026.873959` E0016 09-24 |
| Abacus (wooden tower), DNA Helix (Badge), Atomic Molecule (Badge) | "this one is.. ehh.. noisy:" | `C090N54TG79/1758757641.634929` E0016 09-24 |
| Handsaw (scissor) | — | `C090N54TG79/1758757881.264889` E0016 09-24 |
| Ice Cream Cone (Soft serve) | "this one is pretty good:" | `C090N54TG79/1758758037.503059` E0016 09-24 |
| lollipops (Kiwi) | "Various lollipops (Kiwi):" | `C090N54TG79/1758758503.319859` E0016 09-25 |
| [USERNAME_36211] ([USERNAME_36210]) — name redacted; chocolate | "[USERNAME_36211] is pretty great ([USERNAME_36210])" · "Maybe we could use a impact VFX that's organic splash but without the liquid, so in this case we have the chocolate pieces but not water droplets" | `C090N54TG79/1758758672.742539`, `C090N54TG79/1758758695.130369` E0016 09-25 |
| Corndog (hotdog), Sandwich (hamburger), sushi (garlic) | — | `C090N54TG79/1758759314.143939` E0016 09-25 |
| Book (desk lamp - lightning), coffee table (bench) | "I think the table from the underside is really hard to tell what color it is.. we might need a creative solution for this" (to E0009) | `C090N54TG79/1758759686.056119`, `C090N54TG79/1758759698.849929` E0016 09-25 |
| "classroom" collection: protractors/pencil/ruler/blackboard/atomic molecule/book/abacus | "I think we might have the right items to do a \"classroom\" collection" | `C090N54TG79/1758759845.447389`, `C090N54TG79/1758759858.109419` E0016 09-25 |
| Chopstick (spatula) | "I might add a blind for this item because it pokes zombies in the eye:" | `C090N54TG79/1758760095.485329` E0016 09-25 |
| cactus, chainsaw, cones | "Got new colored version of cactus, chainsaw and cones that can probably come in handy:" (video) | `C090N54TG79/1759189466.554739` E0016 09-29 23:44 |
| musical items, bowling items | "Some musical items and bowling related items are super bouncy. Please fix" | `C090N54TG79/1757479643.204289` E0038 09-10 |
| bread/cookie, gift box (VFX wanted) | "1. Bread/cookie (So brown crumbs) ⏎ 2. Confetti/paper (Gift box)" | `C09ATAJ220H/1757464811.241579` E0016 09-10 |
| tea kettles | "He said \"two different TEA kettles\"" (playtest transcript) | `C090N54TG79/1758582710.757669` E0016 09-22 |

### A4 Fruit / vegetables on the early board (level 4 and level 2)

| Names | What is said | Level | Pointer · speaker · date |
|---|---|---|---|
| apples, oranges, grapes, pears, small lemons | "it’s so easy to mix up Apple with oranges and grapes with pears, and then we also have small lemons you accidentally pick" · "I think this is a great level 10 rather than level 4" | 4 | `C090N54TG79/1757714589.705049`, `C090N54TG79/1757714600.720319` E0038 09-12 |
| oranges → tomatoes | "Replace oranges with more tomatoes and we will be good to go" | 4 | `C090N54TG79/1757948020.978869` E0038 09-15 |
| apple / orange | "That level is supposed to teach two item can be different colors so I want to keep the Apple orange thing." | 4 | `C090N54TG79/1757948120.358159` E0005 09-15 |
| tomato, bell peppers | "I'll make a version with tomato and bell peppers instead of round shape." · "The point of this level is to have 2 colors of the same item. So bell peppers are good for that." | 4 | `C090N54TG79/1757949251.650129`, `C090N54TG79/1757959520.347449` E0005 09-15 |
| cherries (asked, absent), strawberries, grape | "we don’t have cheeries or any other red item?" · "I can put some strawberries I guess, one second" · "yeah, please add in strawberries, then I think the level will work" · "Bellpeppers still get the job done and enough texture from grape and strawberry to avoid blunder" → PR made | 4 | `C090N54TG79/1757959462.125359` E0038; `C090N54TG79/1757959550.965969` E0005; `C090N54TG79/1757959588.782559` E0038; `C090N54TG79/1757959702.204739`, `C090N54TG79/1757959992.127429` E0005 — 09-15 |
| orange, bat | "I thought bat was the closest I can find to a \"stick\" shaped orange ish item" | 2 | `C090N54TG79/1756753765.311669` E0016 09-01 |

"berries" as a word: only strawberry/strawberries (above). Outside window, 2025-07-22: "the level 0 often doesn't follow the power curve, for example strawberry" `C090N54TG79/1753177225.290379` E0016.

### A5 Boosters and board-level tools

| Name | What is said | Pointer · speaker · date |
|---|---|---|
| nuke | "After the items were matched, I got the regular_level nuke… I think we should disable the nuke for this game mode" (Boss arena) · "A good player should be able to launch 1-3 nukes per play" · nuke levels list "level 6 … Level 78" | `C090N54TG79/1758123985.139489` E0038 09-17; `C090N54TG79/1757615317.492109` E0016 09-11; `C090N54TG79/1757337659.125719` E0012 09-08 |
| rapid fire | "I filled my rapid fire up to 3 secs and used it" · "I was going to shorten the rapid fire max duration to maybe 3 seconds" | `C090N54TG79/1758123985.139489`; `C090N54TG79/1757611354.128839` E0016 09-11 |
| airstrike | "air strike in endless mode" (not explained to players) · "airstrike freeze" on Samsung | `C090N54TG79/1758583438.427779` E0016 09-22; `C090N54TG79/1758564051.199019` E0012 09-22 |
| freeze (booster vs item effect) | "I think we should do an a/b test and do freeze etc before we teach boosters." | `C090N54TG79/1757998419.856959` E0038 09-16 |
| glue (booster icon) | "the glue one starts from other place" | `C09ATAJ220H/1755196994.837929` E0002 08-14 |
| bypass item | "remove bypass item from algo levels" | `C090N54TG79/1757355103.109279` E0012 09-08 |

### A6 Enemies named in the window (for the "which zombies" question)

| Name | Quote | Pointer |
|---|---|---|
| chef | "This is just enough icecream to kill the chef." | `C090N54TG79/1759172937.229039` E0005 09-29 |
| bike kid | "we have the bike kid at level 17 before his introduction so I fixed that too… And level 79 won't be an immediate bike kid death now." · "That bar is as thick as the bike kid's head lol" | `C090N54TG79/1757367863.578979` E0005 09-08; `C090N54TG79/1758822305.162149` E0016 09-25 |
| boxer | "I recommend setting a FIXED spawn track of something buff, like a boxer, maybe 3-4 of them." | `C090N54TG79/1757053197.193219` E0016 09-05 |
| mayor (boss) | "I feel like even 2x or 3x mayor boss HP to 500 or 750 for example, isn't all that much" · "especially mayor type monsters would need 500+ hp" | `C090N54TG79/1758667669.909829` E0016 09-23; `C090N54TG79/1758695671.265169` E0012 09-24 |
| no new zombies | "I don’t think we can afford to add new zombies right now. Let’s be creative and figure out how we can reuse the same zombies but strongers versions of them" | `C090N54TG79/1757488355.886209` E0038 09-10 |

### A7 Outside the requested window (keyword sample of 2025-06..08 only — not a full read)

- grenade / dynamite: "we wouldn't convert dynamite and grenade into cards right <@EMPLOYEE_0016_SLACK_ID>?" `C090N54TG79/1752230344.088959` E0012 2025-07-11 (thread root, 82 replies, not read).
- "prop" levels: "they are \"prop\" levels, like grenades and other fancy stuff where the level is meant to be played as is" `C090N54TG79/1752015700.894119` E0016 2025-07-08.
- shuriken: "so you can't just shuriken your way through everything, just 90% of the time" `C090N54TG79/1752234561.582109` E0016 2025-07-11; "a player who luckily get shuriken can upgrade it in a 3 day at most." `C090N54TG79/1753281244.186259` E0012 2025-07-23.
- broom: "broom tutorial triggered twice in the same level (just like the problem before)" `C090N54TG79/1753736892.052389` E0012 2025-07-28.
- "plush", "duck", "doll": zero hits in #zombie-design 2025-06 → 2025-09 (the plush/duck appears only in the vendor channel).

## B The playable (chronological)

### B1 Domino Delights round, March–June 2025 (vendor channel, in full)

| UTC | Pointer | Who | What (verbatim) |
|---|---|---|---|
| 03-06 18:08 | `C08H78VJG80/1741284538.488439` | E0038 | "we’ll be working with the playableX team to make some good looking playables. For the first playable, we’ll focus on Domino Delights. If we get the desired outcome and happy with the work, we’ll be extending the effort to our Match 3D prototype - that’s TBD. I added you to the channel to help us with assets and ensure we can give high quality art feedback" (said to the Art Director, E0030) |
| 03-06 18:10 | `C08H78VJG80/1741284639.327009` | E0038 | "finally, adding our CTO Blake for his awareness" |
| 03-10 09:56 | `C08H78VJG80/1741600570.171389` | P3937 | "1. Could you share the names of games you consider your competitors? … 2. Additionally, we’d love to get a detailed brief from you to fully understand the concept you have in mind. After that, we can follow up regarding assets." |
| 03-10 16:17 | `C08H78VJG80/1741623438.266309` | E0008 | "We'd appreciate your suggestions on the brief, based on what you see working for other clients. We are prioritizing highly retained users. So we probably want to err on the side of a longer playable that is a good representation of our game." |
| 03-11 14:59 | `C08H78VJG80/1741705164.913899` | P6073 | "even if the gameplay is long (approaching three minutes), complex mechanics are never introduced; at most, one very obvious mechanic is included in the top-performing playables we’ve seen." · "one long level (which you can shorten if you want by triggering the endcard/market redirection after 6-7 moves)" |
| 03-11 17:18 | `C08H78VJG80/1741713510.061479` | E0008 | "My gut says we want a playable that is less on rails and the user can make decisions which impact how the level proceeds." · "We could do something similar with a special tile like bomb tile -- where it clears the entire board in the playable." |
| 03-12 16:20 | `C08H78VJG80/1741796408.361009` | E0038 | "please meet <@EMPLOYEE_0005_SLACK_ID> and <@EMPLOYEE_0026_SLACK_ID> - our lead designer and Product Manager respectively. They both live in Turkey." |
| 03-14 14:45 | `C08H78VJG80/1741963515.221549` | E0005 (files image.png, playable1.mp4) | "Yesterday we finalized our storyboard for the ad… 1. We allow the player to match 4 tiles.  ⏎ 2. When these two tiles are matched 2 things happen: a) a bomb tile is revelaed b) sophie grants tiles to the deck. ⏎ 3. We force the player to draw a tile.  ⏎ 4. We force the player to click on the bomb and clear out the level.  ⏎ Below are a simple wireframe storyboard [PERSON_NAME_0092] created and a video we shot" |
| 03-14 14:47 | `C08H78VJG80/1741963632.469869` | E0005 | "If you guys think those will perform better, we can iterate." (options: zoom-out, chain reaction) |
| 03-15 18:23 | `C08H78VJG80/1742063032.441019` | E0038 | "Knowing that we want to be done in 3 weeks, it might be awesome if we pick up the pace early next week." |
| 03-17 14:09 | `C08H78VJG80/1742220596.626279` | P6073 | "we need the following assets (but please send anything else if you think we’d need it): ⏎ domino tiles, ⏎ character assets, ⏎ ui elements (2d elements like buttons, indicators etc.) ⏎ background assets (I imagine it would be 2d?) ⏎  ⏎ also, please tell us what you’d prefer to be editable from our platform (like tile assets, background, market redirection conditions etc.)" |
| 03-17 14:13 | `C08H78VJG80/1742220833.723329` | P6073 | "we need fbx file format for 3d assets. you can directly zip the assets and send them through here" |
| 03-18 15:49 / 16:04 | `C08H78VJG80/1742312985.835989`, `C08H78VJG80/1742313883.827439` | E0005 / P6073 | "Can you please ask your developer if they want the 3D model or the prefab?" → "both are OK as long as the file type is fbx" |
| 03-18 16:36 | `C08H78VJG80/1742315789.059509` (root, 25 replies) | E0005 (file playablex_harmonygames.zip) | "Here are the assets you have required. The editable portions should be our backgrounds and characters. I'm extending the prefabs of the characters but I can send the animations and the animation controller as well if needed." |
| 03-19 13:16 / 13:23 | `C08H78VJG80/1742390204.551519`, `C08H78VJG80/1742390620.342179` | E0026 (CharacterAnimationsWithControllers.zip) | "Here's the character animators and animations" · "I am also adding which specific animation in the controllers to trigger for each character when users complete 4-streak" (Sophie_Cast_To_Hand_Fast, Nathan_Bomb_Throw_Deck_Sequence, Julius_Cast_Magic_To_Hand, Leqi_Cast_Magic) |
| 03-20 16:27 | `C08H78VJG80/1742488034.212469` | E0038 | "We are aiming for April 3rd to have all assets and campaigns ready to go. Do we believe we can have the playable ready by that date?" |
| 03-20 16:31 | `C08H78VJG80/1742488293.399959` | P6073 | "it is a bit tricky now with the ramadan eid upcoming and the team will be off a few days" |
| 03-21 16:23–16:44 | `C08H78VJG80/1742574189.871769`, `C08H78VJG80/1742574237.537009`, `C08H78VJG80/1742575239.039089` | P6073 / E0005 / P6073 | "team says we need fbx export of everything" → "The fbxs are in the prefabs, they can use it from There. Is There an issue with that?" → "yes, we can’t open prefabs, we directly need the fbx exports" |
| 03-21 17:39 | `C08H78VJG80/1742578785.786919` | E0026 (Chacters-Animations.zip) | "You can find fbx files, animations, animators and textures here." |
| 03-24 14:40 | `C08H78VJG80/1742827212.606159` | P6073 | "our estimation is that we can deliver this 7-8th of April" |
| 03-25 08:56 | `C08H78VJG80/1742892985.601399` | P6073 | "we need everything in fbx format, including the animations. the animations seem to not present in fbx files. we cannot open/work with other file formats you’ve sent. ⏎  ⏎ we also need the fbx files for domino tiles" |
| 03-25 09:08 / 10:44 | `C08H78VJG80/1742893713.382609`, `C08H78VJG80/1742899453.589669` | E0005 / P6073 | "Can you connect us with your developer, please?" → "our dev says that we need the animation embedded with the character models in the fbx file, rather than being separate files" |
| 03-25 12:40 | `C08H78VJG80/1742906430.444969`, `C08H78VJG80/1742906450.038149` | E0026 | "the character and animations were outsourced and added to the project a long time ago. Right now, the animations are in a separate folder within the project, just as I sent" · "We could reach out to the outsource team again… but do you have a quicker solution" |
| 03-25 13:21 | `C08H78VJG80/1742908901.847459` | P6073 | "we’ll try to handle the animations from the files you’ve sent. we still need the domino tiles though" |
| 03-26 14:39 | `C08H78VJG80/1742999995.831099` | E0026 (tile&bombTile.zip) | "Previously, [PERSON_NAME_0040] sent you the prefab versions of the tile and bomb tile. In this file, you can find the tile and bomb tile in FBX format" |
| 04-01 15:22 | `C08H78VJG80/1743520926.156489` | E0038 | "planning to go live in the US on April 10th or before. This 1 week delay should have bought you guys some time as well. Any chance we can see the progress and give feedback?" |
| 04-02 08:18 / 12:38 | `C08H78VJG80/1743581929.137479`, `C08H78VJG80/1743597491.420419` | P6073 / E0025 | "could you give one of our devs test access from google play store if possible?" → "you should be good to go" (internal-test link) |
| 04-04 11:38 | `C08H78VJG80/1743766705.396069` (root, 7 replies) | P6073 | "could you send the sound/music assets relevant for playable?" |
| 04-04 13:14 / 13:15 / 13:16 | `C08H78VJG80/1743772445.340109`, `C08H78VJG80/1743772540.927359`, `C08H78VJG80/1743772583.996939` | E0005 / P6073 / E0005 | "Sure, I need to talk to the marketing team about music. Do we want the sound of the actual game or ad appropriate soundtrack?… For SFXs, I'll collect them today" → "ad appropriate would be better, we will make it editable anyway so you can iterate them later" → "I also asked [PERSON_NAME_0036] and Leonard about their preference" |
| 04-07 13:21 / 13:27 | `C08H78VJG80/1744032108.252119`, `C08H78VJG80/1744032425.146979` | P6073 / E0026 | "any progress about the sounds?" → "I was going to take care of it, but it slipped my mind" |
| 04-07 21:04 | `C08H78VJG80/1744059855.381899` | E0026 (DominoDelight-harmonygames-Sounds.zip) | Sound list with which are "*remotely changeable*": Match Sounds ("Should play sequentially each time a new tile is matched."), Bomb Tile Sound, Background Sound ("Should be *remotely changeable.*"), Adding Tile to Deck (remotely changeable), Streak Sound - Incredible (remotely changeable), dominoes fly-in at level start, Draw Tile from Deck, Level Complete, Level Fail |
| 04-08 08:06 | `C08H78VJG80/1744099586.260219` | P6073 | "a little demo of the playable here, and we are planning to finish it today" |
| 04-08 14:54 | `C08H78VJG80/1744124056.550469` | P6073 | account e-mail + "password: [PASSWORD_6001]" + `https://app.playablex.ai/panel/` posted in channel |
| 04-08 14:58 | `C08H78VJG80/1744124307.798299` | P6073 | "we have finalized the game and uploaded it to our platform… You can think of projects as folders, and variations in them as playable files. You can create an unlimited number of projects and variations… you can edit the playable and get exports for available networks… You can change characters, backgrounds etc. You can also add custom backgrounds, logos, endcard visuals etc." |
| 04-09 17:34 | `C08H78VJG80/1744220092.359649` | E0008 | "I think we need to change the bomb domino to have a 5 on top instead of a 2." |
| 04-09 20:55 | `C08H78VJG80/1744232118.081379` | E0038 (file "Playable Feedback") | "Overall, we are close to be done with the base animation. Please find our feedback here: <google doc> ⏎  ⏎ The critical items are P0(s) and P1s." |
| 04-14 13:27 | `C08H78VJG80/1744637266.363689` | P6073 | "p0: ⏎ the tile is now 5-5" · "we are limited to what you send us for animations at the end of the day" · "scale, position and rotation settings was added for the characters" · "draw pile size was reduced to 2" · "music has to start after first click as a rule. as for the timer, if we start it immediately, the playable will preload while the video ad is still playing, and it will run out before the user can see it" · "simulations in our platform are a bit buggy right now especially in some browsers, it should be OK in real life" |
| 04-25 05:25 | `C08H78VJG80/1745558744.209509` | E0038 | "I finally had a chance to review the playables - they look fantastic!" (11 days after delivery of fixes) |
| 04-25 06:56 | `C08H78VJG80/1745564189.196279` | P6073 | "as we create that UI custom for each game, There is no documentation, but hovering over the “i” icons can show some information about the control." · "as for the ios and android links, you need to fill in your app store and play store links." |
| 04-25 18:02 | `C08H78VJG80/1745604179.036989` | E0008 | "let's make sure we understand how to properly export the playables and add them to our various UA campaigns. The priority to understand would be i) Unity (both Playable and video + playable end card), ii) Facebook, iii) AppLovin." |
| 04-28 | `C08H78VJG80/1745853339.515739` | P6073 | walkthrough call held ("changed the meeting time") |
| 06-25 14:05 / 15:05 | `C08H78VJG80/1750860354.615759`, `C08H78VJG80/1750863929.654149` | P3937 / E0008 | "just wanted to check if you’ve had a chance to try out the playable?" → "We just went live with Applovin two days ago, so very limited data at this point." |

### B2 Zombie Match 3D round, 26 Aug → 30 Sep 2025 (vendor channel + #zombie-design)

| UTC | Pointer | Who | What (verbatim) |
|---|---|---|---|
| 08-26 15:53 | `C08H78VJG80/1756223629.429589` | E0038 | "we need your help with our next playable for Zombie Match 3D game! Domino Delights didn’t work out from CPI &amp; LTV perspective so we’ll grow that game either with a publisher or organically." |
| 08-26 15:56 | `C08H78VJG80/1756223785.608099` | E0038 | "What would be most helpful is if you guys play the game up until level 40 - it should take less than hour end to end" |
| 08-26 15:58 | `C08H78VJG80/1756223892.790609` | E0038 | competitor: "Match Factory [USERNAME_18759]" |
| 08-26 15:59 | `C08H78VJG80/1756223949.995939`, `C08H78VJG80/1756223954.141059` | E0038 | "I think this brief would help" + image.png (content of the image not readable) |
| 08-26 15:59 | `C08H78VJG80/1756223999.412739` | P3937 | "This is the playable we created" (preview link for "a game in a similar genre") |
| 08-26 16:00 | `C08H78VJG80/1756224039.537749` | E0038 (InvestorFacing_Seq3.mp4) | "And here is investor-facing long-form video" |
| 08-26 16:03–16:04 | `C08H78VJG80/1756224224.394469`, `C08H78VJG80/1756224240.230179` | E0038 | "items do matter, the order you match them against different types of zombies" · "but the core mechanic is pretty much the same as [USERNAME_46303]" |
| 08-26 19:41 | `C08H78VJG80/1756237263.529979`, `C08H78VJG80/1756237277.915139` | E0038 | "it’s great that we have a template to take care of the core game already" · "we need to figure out how to bring in zombies under 5mb :slightly_smiling_face:" (**the only size figure in the four channels**) |
| 08-27 16:54 | `C08H78VJG80/1756313677.542959` | E0038 | "testflight build is approved" |
| 08-27 19:10 | `C08H78VJG80/1756321837.876699` | P3937 | "Once we’ve compiled our notes, <@PERSON_6078_SLACK_ID> our product manager will be leading the process." |
| 08-28 09:30 / 09:34 | `C08H78VJG80/1756373440.934409`, `C08H78VJG80/1756373673.416449` | P6078 (bug.mp4) | "In the second level, when I first played it, the *zombie was still alive even though There were no more items left on the board to throw*." · "My device is an *iPhone 16*… the game started to *lag*… the *endless level* feature was particularly difficult." |
| 08-28 14:33–14:38 | `C08H78VJG80/1756391616.026279`, `C08H78VJG80/1756391634.106759`, `C08H78VJG80/1756391684.632219`, `C08H78VJG80/1756391911.500069` | E0038 | "We must have intro’ed a bug for level 2 when we were making a custom testflight build for you guys." · "We are aware of the stutters - team is working on a fix" · "Fwiw the game economy is also super off." · "It’s fair to say that we are a month away from beta. Still lacking tons of polish vfx etc too" |
| 08-28 14:57 | `C08H78VJG80/1756393065.804409` | P6078 | Four scenarios in a Google doc (link in message): "*Scenario 1:* This is based on the core game mechanics." · "*Scenario 2:* This is built around the bomb mechanic on the in-game board." · "*Scenario 3:* This was inspired by high-interaction playables from games like" [linked: Royal Match] and [linked: Ma[USERNAME_30464]] · "*Scenario 4:* This is a new scenario created as a combination of the previous ones." · "We can start discussing and planning the project based on the scenario you choose." |
| 08-28 16:52 | `C08H78VJG80/1756399976.644599` | E0038 | "<@EMPLOYEE_0005_SLACK_ID> <@EMPLOYEE_0008_SLACK_ID> <@EMPLOYEE_0016_SLACK_ID> <@EMPLOYEE_0012_SLACK_ID> ^ let’s review the scenarios together" |
| 08-28 17:27 / 18:00 | `C08H78VJG80/1756402043.104259`, `C08H78VJG80/1756404056.404979` | E0005 / E0012 | "I like the Match Factory one" · "I also liked the third option, but my only concern is that it might not be as exciting as the other two since we don't have an avatar to associate with." |
| 08-29 07:25 | `C08H78VJG80/1756452358.461719` | P6078 | "Our suggestion, however, is to move forward with *Scenario 1 and highlight the basic gameplay*… *a simple playable = strong first impression + clear mechanic focus + lower drop-off*" |
| 09-01 → 09-03 | `C08H78VJG80/1756735324.206019`, `C08H78VJG80/1756748818.259249`, `C08H78VJG80/1756925213.271559` | P6078 / E0038 | vendor chases; "some product work took priority" |
| 09-12 16:38 | `C08H78VJG80/1757695108.506159` | E0008 | "I think Scenario 1 is a good bet for filtering out the players that won't like our game, while remaining true to our core game play. ⏎  ⏎ For Scenario 1, would the user be able to select any items they want and make several matches (if they are good enough)?" |
| 09-15 09:30 | `C08H78VJG80/1757928654.905219` | P6078 | "yes, the idea is that the user can select items freely and make multiple matches if they are skilled enough." |
| 09-15 17:07 | `C08H78VJG80/1757956024.883249` | E0008 | "lets go with Scenario 1. From a design standpoint, I think the main elements to figure out are 1) what items are on the board, and 2) what zombies are being smashed." · "I think grenade (powerful), couch (splash damage), plush doll (weak but potentially funny), would be a good start." · "For zombies, we have quite a few at this point. Probably best to use a variety." |
| 09-16 11:34 | `C08H78VJG80/1758022459.227279` | P6078 | "We are planning to start this project on *September 29*. If you can share the assets with us before that date, we’ll be able to start the optimization and animation processes in advance. ⏎ For the items on the board, we can make them editable. This way, aside from the 8-item set that you will provide for the board, you can also test any additional items… ⏎  For the zombies, we will proceed with animations in Spine. You can select which zombies from the platform you’d like to use in the game. Depending on the overall game size, we can finalize the number of zombies during the project. ⏎ … *3D assets*: .fbx, .glb, or .blend (when exporting .fbx, please make sure it’s exported in *Binary format*, not ASCII) ⏎ • *2D assets*: .png (for 2D animations, character parts need to be separated into pieces) ⏎ • *Font*: .ttf or .woff2 ⏎ • *Sound*: .mp3 or .wav" |
| 09-18 20:28 | `C08H78VJG80/1758227288.370029` (root, 15 replies) | E0008 | "<@EMPLOYEE_0026_SLACK_ID> can you help package up assets? <@PERSON_6078_SLACK_ID> can you help [PERSON_NAME_0092] narrow down what is needed?" |
| 09-19 12:07 | `C08H78VJG80/1758283671.878269` | P6078 (image.png) | "*3D Assets:* Zombie models + animations, rocket launcher, projectile, board items (the specific objects you’d like to be used on the board) ⏎  *2D Assets:* Item visuals, UI elements, background ⏎  *Audio:* Matching sound, rocket sound, explosion sound, success/failure sounds, background music ⏎  *Text:* Fonts" · "Regarding the board assets, depending on the project size, we can provide a system where you can directly upload and test the assets on the board yourself." |
| 09-22 14:55 | `C08H78VJG80/1758552921.729409` | E0026 | "I will send all the assets by Wednesday at the latest. First, we need to finalize which items and zombies will be used on the Design side. After that, I will gather the assets and zip them" |
| 09-22 18:53 | `C090N54TG79/1758567201.262949` (root, 26 replies) | E0026 | "Are you okay with this version for the playable ad scenario?  Do you think the item type works, or would you suggest something different?  For example, could you point out something like “let’s use these items and those zombies”? ⏎ I’ll start gathering the assets based on the final decision" |
| 09-22 18:53 / 19:11 | `C090N54TG79/1758567231.993159`, `C090N54TG79/1758568261.546739` | E0016 / E0005 | "I am OK with it because it attracts more hardcore users" → "It attracts more hardcore users to a currently casual funnel. What is the benefit in that?" |
| 09-22 19:18 | `C090N54TG79/1758568698.895379`, `C090N54TG79/1758568735.563539` | E0026 | "We can request replaceable versions of items and zombies from the Playable team. But I’m not sure if they can also add different item properties" · "<@EMPLOYEE_0005_SLACK_ID> Based on the final decision, could you prepare a test level as a reference for both the Playable team and myself? That way, I can directly use the item and zombie files from There" |
| 09-22 19:23 / 19:28 | `C090N54TG79/1758568988.777449`, `C090N54TG79/1758569313.660759`, `C090N54TG79/1758569323.919359` | E0005 / E0026 | "Yep, I'll make your level ASAP when the guys make their decision. What exactly do you need?" → "I need a classic level. Items and zombies. I can directly share the zombie visuals and items There with the playable team" · "If you’d like, we can create 2 different levels for hardcore and casual players. Some items would be shared, while the zombies could be similar or the same. We would also ask the team to upload all the objects." |
| 09-22 19:31–19:41 | `C090N54TG79/1758569491.223089`, `C090N54TG79/1758569629.722849`, `C090N54TG79/1758569655.409719`, `C090N54TG79/1758569707.508219`, `C090N54TG79/1758569824.148029`, `C090N54TG79/1758569885.985319`, `C090N54TG79/1758570038.885309`, `C090N54TG79/1758570117.998139` | E0005 / E0016 | E0005: "So going generic in the playable will perform better in terms of retention." → E0016: "But the idea is to test the current form and audience fit, not what the game can tailored to become" → E0005: "Oh.. Yeah in that case, let's do a more hardcore friendly playable and see how they do with the funnel." → E0005: "Do you want to try a cute level with lots of grenades and shruiken then? Total guy focus" → E0016: "I think we should remain as is" → E0016: "If we were to quickly make changes to tailor \"hardcore audience\" better, and have another casual version out There to entertain the casual audience, then we won't be able to answer #1 and #4 very well" → E0005 (last reply): "I think the game is at least a solid 6 in terms of complexity." **Thread ends without an item/zombie list.** |
| 09-24 08:18 | `C08H78VJG80/1758701898.919999` | P6078 | "due to a delay in receiving the assets, we need to update the project start date. Normally, before starting we optimize and review the assets to make sure everything runs smoothly. Because of this, we’ll be able to kick off your project on *October 6th*." |
| 09-24 12:39 | `C08H78VJG80/1758717576.077489` | E0026 (Playable-assets-harmonygames-games.zip) | "You can access the game assets here. Since our zombies are made with 2D Unity animations, I’ve included the PSD files along with the animation and prefab files. Please let me know if you find any missing or problematic assets" |
| 09-24 12:40 | `C08H78VJG80/1758717625.209649` | E0026 (20250923-1936-36.8420811.mp4) | "We’ve also prepared a sample level as a reference. The fail condition in the game is when zombies reach us and deplete our HP, while the win condition is eliminating all the zombies on screen" (level number not stated) |
| 09-24 12:41 | `C08H78VJG80/1758717701.940139` | E0026 | "we’re planning to add different items and zombie types later on for testing. Also, having control over the number of zombies and items placed on the board will give us a lot of flexibility" |
| 09-24 14:18 | `C08H78VJG80/1758723504.085039` | P6078 | "At this stage, the only missing piece seems to be the duck asset used in the reference. Could you also provide that? In addition, it would be great if you could share the zombie assets in *Unity package* format along with their animations. ⏎ We’ll be re-animating the selected zombies in Spine… If There are no size limitations, we can also upload the zombies to the platform in a way that allows you to select and use them directly. As for the upload compatibility, we’ll clarify this later in the project" |
| 09-24 15:58 | `C08H78VJG80/1758729487.922339` | E0026 (Plushie-and-zombies.zip) | "Sure, I’m sending the files. Thanks for the update" |
| 09-24 19:24 | `C08H78VJG80/1758741842.638619` | E0008 | "noted on revised kick off time." |
| 09-25 13:50 | `C08H78VJG80/1758808234.045839` | P6078 | "it looks like the package wasn’t exported correctly. Only the prefabs were included, but the actual assets are missing. In order to view the prefabs properly, we also need all the related .png files to be part of the package… it would be great if you could test the package in a blank Unity project before sending it over." |
| 09-26 17:00 | `C08H78VJG80/1758906043.375719` | E0026 (zombies_Characters_UnityPack.zip) | "Sorry, it took a little while, I had to get help from our animator" |
| 09-29 02:48 | `C090N54TG79/1759114097.776589`, `C090N54TG79/1759114127.213749` (root, 3 replies) | E0038 | "For the playable - should we pause the effort if they haven’t started yet?" · "I’m worried that we pivot the core game and then playable dev money will be wasted. It’s not nothing" |
| 09-29 07:28 | `C08H78VJG80/1759130898.184939` | P6078 | "We’ll review the assets and let you know if we encounter any issues." |
| 09-29 10:16 | `C08H78VJG80/1759140968.965099` | P6078 | "Since we don’t use Unity to develop the playables, we need to adapt the characters you provided to our pipeline. To do this, we will re-rig the characters in Spine and extract the keyframes from the Unity animations via script… we kindly ask you to: ⏎ • Select the primary animation you want us to use (attack, idle, die, or walk), and ⏎ • Specify the 4 zombie characters to which this animation should be applied. ⏎ Depending on the project scope and size, we can increase the number of zombies in later stages. For now, 4 characters seem to be the most suitable option in terms of both time and size." **No reply to this in the channel before the clock.** |
| 09-29 10:30–10:31 | `C090N54TG79/1759141833.339099`, `C090N54TG79/1759141909.436389`, `C090N54TG79/1759141916.767179` | E0026 | "Makes sense, I sent them the assets, but as far as I know, they haven’t started yet" · "But if we are going to stop the process, we should say it asap" · "because today they asked me another question about rigging related to the animations" |
| 09-29 19:42 | `C08H78VJG80/1759174925.309129` | E0008 | "we are considering a pretty substantial pivot in core game play for Zombie Match. I think we should pause development of the playable for a month or so to make sure we aren't building something that doesn't align with the game's ultimate aesthetic or core game play. Does that work on your end?" |
| 09-30 09:59 | `C08H78VJG80/1759226395.551469` | P6078 | "Hi <@EMPLOYEE_0008_SLACK_ID>, of course! We’re planning the new start date for the game on November 3rd." (last message in the channel) |

### B3 Summary of what the base fixes (each from the rows above)

- Start dates: 29 Sep → 6 Oct → 3 Nov 2025. Pause asked by E0008 on 09-29 ("for a month or so").
- Scenario: Scenario 1 (core mechanics, free item selection, multiple matches). Chosen by E0008 on 09-15.
- Items: E0008's starting three (grenade, couch, plush doll); vendor expects an "8-item set"; final list not recorded.
- Zombies: vendor wants 4 zombies + one primary animation (attack / idle / die / walk) — unanswered. HG zombies are 2D Unity animations with PSD sources; vendor re-rigs in Spine.
- Assets sent: `Playable-assets-harmonygames-games.zip` (09-24), sample-level video `20250923-1936-36.8420811.mp4` (09-24), `Plushie-and-zombies.zip` (09-24), `zombies_Characters_UnityPack.zip` (09-26). Missing / not confirmed received: audio (matching, rocket, explosion, success/failure, music), fonts, the 4-zombie choice.
- Formats: 3D .fbx (Binary) / .glb / .blend; 2D .png with parts separated; fonts .ttf / .woff2; sound .mp3 / .wav; zombies also as a Unity package that must include the .png files.
- Size: only "under 5mb" for zombies (E0038, 08-26); vendor ties zombie count to "overall game size" but gives no number.
- Editable: board items editable / uploadable by HG on the platform; zombies selectable "If There are no size limitations".
- Money: no amount, quote, invoice or contract term in any of the four channels. Only "playable dev money will be wasted. It’s not nothing" (`C090N54TG79/1759114127.213749`).
- Owners: E0038 opened the engagement; E0008 picks scenario and runs the vendor thread; E0026 packages assets and answers the vendor; E0005 builds the reference level; item/zombie choice sits with "the Design side" (E0038, E0016, E0005 were the three asked).

## C Art status

| Statement (verbatim) | Pointer · speaker · date |
|---|---|
| "It’s fair to say that we are a month away from beta. Still lacking tons of polish vfx etc too" | `C08H78VJG80/1756391911.500069` E0038 08-28 |
| "Since our zombies are made with 2D Unity animations, I’ve included the PSD files along with the animation and prefab files." | `C08H78VJG80/1758717576.077489` E0026 09-24 |
| "Sorry, it took a little while, I had to get help from our animator" (Unity pack of zombies) | `C08H78VJG80/1758906043.375719` E0026 09-26 |
| "We’ll be re-animating the selected zombies in Spine" / "we will re-rig the characters in Spine" (vendor redoes the animation) | `C08H78VJG80/1758723504.085039`, `C08H78VJG80/1759140968.965099` P6078 |
| "the character and animations were outsourced and added to the project a long time ago" (Domino Delights) | `C08H78VJG80/1742906430.444969` E0026 03-25 |
| "I don’t think we can afford to add new zombies right now." · "if we have budget we can generate and send them to that outsource team asap, my AI generation funnel is pretty solid." · "I'll talk with Marcus about the cost of color change and adding some accesories that don't require more bones… we can talk about the cost in the art meeting today" | `C090N54TG79/1757488355.886209` E0038; `C090N54TG79/1757487035.104699`, `C090N54TG79/1757490903.394599` E0005 — 09-10 |
| New item clones not live: "None of them works right now" (surfboards, music notes, clef) · "None of these are activated in the pool" (flip flops … packpack) | `C090N54TG79/1758063803.640359` 09-16; `C090N54TG79/1757397477.968089` 09-09 — E0016 |
| Item looks: "this one is.. ehh.. noisy" (Abacus / DNA Helix / Atomic Molecule) · "this one is pretty good" (Ice Cream Cone) · table underside colour "might need a creative solution" (addressed to E0009, Art Lead) | `C090N54TG79/1758757641.634929`, `C090N54TG79/1758758037.503059`, `C090N54TG79/1758759698.849929` E0016 09-24/25 |
| "I'm going to increase the ice cream bar size, it's too small in the level introducing it" | `C090N54TG79/1757464517.784799` E0016 09-10 |
| "Got new colored version of cactus, chainsaw and cones" | `C090N54TG79/1759189466.554739` E0016 09-29 |
| Zombie HP bar thickness: "Too thick? I asked for 2x" · "OK if you guys are happy with the look, go for it" · "usability first" · "I like it" | `C090N54TG79/1758796815.758229` (root, IMG_4606.png) E0012; `C090N54TG79/1758822289.405049`, `C090N54TG79/1758822619.851629`, `C090N54TG79/1758822627.839059` E0016; `C090N54TG79/1758825258.755199` E0005 — 09-25 |
| Static images for the Zombie lane: "images were not ready, [PERSON_NAME_0022] integrated the wrong ones" | `C090N54TG79/1757617127.228699` E0038 09-11 |
| VFX: "and the VFX is still quite lacking" (boss arena) | `C090N54TG79/1757613004.807479` E0016 09-11 |
| Placeholder: "Added a placeholder legendary pack for better drop rates just to test how it feels" | `C090N54TG79/1756730298.517369` E0012 09-01 |
| Ice-cream effect: "we can do it when we have more resources" (ice cube forming) | `C09ATAJ220H/1756913710.782539` E0038 09-03 |
| VFX ownership: "Quick update: On Marcus’s side, we’ve wrapped up about 90% of the P0 tasks." · "From here on, all P0 VFX stuff will be handled by <@EMPLOYEE_0006_SLACK_ID>." | `C09ATAJ220H/1755760241.870729` E0026 08-21 |
| Trail colour: "But of course, this is more of an art-related feedback." | `C09ATAJ220H/1755270755.833129` E0026 08-15 |

- Who signs off art: **no sentence in these four channels names an art approver or an art sign-off step.** Closest facts: the Art Director was added to the vendor channel "to help us with assets and ensure we can give high quality art feedback" (`C08H78VJG80/1741284538.488439`, March 2025; that account, E0030, last posts 2025-04-15); E0009 (Art Lead) is tagged once on an item-colour problem (`C090N54TG79/1758759698.849929`); an "art meeting" exists (`C090N54TG79/1757490903.394599`).
- "final" as an art status, "not allowed to be shared", licence / NDA wording: **none found** in the windows read (regex `licen|royalt|copyright|sign.?off` = 0 hits in the three smaller channels in full and in #zombie-design September; `approv` only = app-store / TestFlight approval).
- Removed objects: "Since many objects are removed from the pool or they will bu unlocked later, it will create issues for the existing users." `C090N54TG79/1756730298.517369` E0012 09-01 (no object names given).

## D Builds and levels

### D1 Build numbers and names (September 2025)

| Build / name | What is said (verbatim) | Pointer · speaker · date |
|---|---|---|
| iOS 1513 / android 1766 | "About the card progression and effect unlock, I ve triggered a build for you to test. iOS 1513, android 1766." | `C090N54TG79/1756730298.517369` E0012 09-01 |
| production build ("lawson40", "MF 40") | "the build in production has some issues" · "in lawson40 level2 is fucked - I think <@EMPLOYEE_0025_SLACK_ID> accidentally merged some zombie balance changes to MF 40 which fucked the balance. We need to submit a fix ASAP" · "this happened to me too on the prod (what people download today)" · "every investor will hit that level" | `C090N54TG79/1756751110.305629`, `C090N54TG79/1756751169.213249`, `C090N54TG79/1756751203.655369`, `C090N54TG79/1756751332.578819` E0038 09-01 |
| 0.3.29 (TestFlight) | "I’m testing 0.3.29 on testflight" · "I got stuck at level 5" → "I think I missed that commit." / "Adding back in" | `C090N54TG79/1756916415.831859`, `C090N54TG79/1756916425.153339` E0038; `C090N54TG79/1756916731.499639`, `C090N54TG79/1756916734.924559` E0025 — 09-03 |
| investor-facing build | "Considering that today’s release will be an investor-facing build, I think it’s too risky to include Season Pass in this one. If you’re okay with it, we should add Season Pass to next week’s release instead" | `C090N54TG79/1757104901.003829` E0026 09-05 |
| Match3D Android #1801 | "Match3D Android - #1801 <!here> new build" | `C09ATAJ220H/1757432313.643809` E0006 09-09 |
| Match 3D iOS Internal #1555 | "Match 3D iOS Internal - #1555 , couldn't trigger Android build for now" | `C09ATAJ220H/1757438624.657599` E0006 09-09 |
| submission build / submission list | "Hey, about the submission list…" · "I suggested that we merge it into main after the submission build. Adding this feature directly into the submission build could be risky" | `C090N54TG79/1757445676.961159` E0012 09-09; `C090N54TG79/1757534327.502209` E0026 09-10 |
| Collect & Win test build | "I'm still waiting for a Collect&amp;Win test build" | `C090N54TG79/1757447742.666159` E0026 09-09 |
| "this build" (to buy users on) | "if <@EMPLOYEE_0016_SLACK_ID> is happy with Zombie lane, this build is great to buy" · "I’m looking forward to buying users for this build… I think this build is also a good candidate for Playtestcloud but maybe we wait for the next release" | `C090N54TG79/1757555503.873679`, `C090N54TG79/1757555584.845899` E0038 09-11 |
| 0.3.36 | "Also I updated the dashboard for 0.3.36" · "looks like level 4 is too hard" | `C090N54TG79/1757705346.424419`, `C090N54TG79/1757705360.848489` E0038 09-12 |
| 09-15 release | "Will we include the Effects Panels in today’s release?" → "Let's ask [PERSON_NAME_0022] at prod" | `C090N54TG79/1757951755.976749` E0026; `C090N54TG79/1757951958.746669` E0016 |
| 09-19 release | "we don’t think it will reach a shippable level by the end of today" (Collect & Win) → "In that case let’s do new levels and analytics for today’s release." | `C090N54TG79/1758292083.627299` E0026; `C090N54TG79/1758292221.963019` E0038 |
| beta | "Fix tech issues first. Axe Arena is descoped… Beta must be tech stable, no excuses." · "Once we have clean data from a tech-stable beta in 15-20 days, we’ll decide: either iterate or pivot the core game." | `C090N54TG79/1758517286.431379` E0038 09-22 05:01 |
| September 30 release / `sep30levels` | "I will stop level making at 300 which I'm close to. But I want to have more content for September 30 release just in case" · "You can work on  the tutorial level is There `[PERSON_NAME_0019]/sep30levels`" | `C090N54TG79/1758689839.300009` E0005 09-24; `C090N54TG79/1759173180.192809` E0005 09-29 |
| 0.3.22 | "I think we should think about what 0.3.22 had and what we're keeping." | `C090N54TG79/1759176983.189479` E0016 09-29 |
| custom TestFlight build for the vendor | "testflight build is approved" · "We must have intro’ed a bug for level 2 when we were making a custom testflight build for you guys." | `C08H78VJG80/1756313677.542959` 08-27; `C08H78VJG80/1756391616.026279` 08-28 — E0038 |
| branch | "If you want to test it's on this branch: `[PERSON_NAME_0029]/VFX_Implementation`" | `C09ATAJ220H/1757347571.207859` E0006 09-08 |

No message in these channels labels a specific number as "the beta build" or "the store build". No build number is posted after 0.3.36 (09-12).

### D2 Performance fixes that touch objects

| Statement | Pointer · speaker · date |
|---|---|
| "it's all in pool resizing still" · "it cannot be merged from the poolresizing branch" · "Since many objects are removed from the pool or they will bu unlocked later" | `C090N54TG79/1756754708.934369` E0016; `C090N54TG79/1756753434.723599`, `C090N54TG79/1756730298.517369` E0012 — 09-01 |
| "I thought we agreed on not doing zombie poison in very early levels because of the stutter issues" | `C090N54TG79/1756751276.912539` E0038 09-01 |
| [link text "Hard crash", Linear ZOM-475] "bug on Android after consecutive glass VFX/SFX" · "it's still happens for samsung devices, that's why I couldn't repro." · "The faulty second collider should be fixed in order to reduce jiggling items and increase perf a little." · "and those are in Blake's PR" | `C090N54TG79/1757539474.366249` E0012 09-10 |
| "jiggly items PR to be merged (it needs <@EMPLOYEE_0025_SLACK_ID>’s input because it's basically reverting what he's changed on physics material)" | `C090N54TG79/1757355103.109279` E0012 09-08 |
| "Then maybe objects should be selected carefully. Since it has only 1 enemy we should make it the least stuttering as possible" · "Goodlooking low poly objects might be better" (boss arena) | `C090N54TG79/1757613527.445949`, `C090N54TG79/1757613571.437419` E0012 09-11 |
| "I also updated the endless mode so There are lots of monsters for performance reasons" · "Changed all flight time of objects to be much quicker, hopefully reduces more weird strange issues" | `C090N54TG79/1757965299.265779`, `C090N54TG79/1757965327.801519` E0016 09-15 |
| "I think older devices, we need to change their settings to medium on IOS" | `C090N54TG79/1758293856.539659` E0038 09-19 |
| "I think we have problems specific to Samsung devices. Just like glass vfx issues, I haven’t experienced the airstrike freeze, notification muting the game." | `C090N54TG79/1758564051.199019` E0012 09-22 |
| Playtest: "Hard crash x1 ⏎ • Phone heat up had to stop playing x1 ⏎ • Audio glitch x1" · "The app froze hard for a user at end of level 21" | `C090N54TG79/1758583438.427779`, `C090N54TG79/1758582162.055749` E0016 09-22 |
| "[USERNAME_49455] has performance issues" · "I went up to 530 zombie kills and I had a lot of lag and performance issues" | `C090N54TG79/1757726374.792569`, `C090N54TG79/1757726396.383519` E0038 09-13 |

The word "memory" does not occur in #zombie-design in September, nor in the other three channels.

### D3 Level counts and reordering

| Statement | Pointer · speaker · date |
|---|---|
| "The zombie lane rewards until lvl 150 is done… after lvl150, it repeats until lvl 290." | `C090N54TG79/1756730298.517369` E0012 09-01 |
| "Finished all 150" · "Algo level 151 was very hard damn" → "Lvl 151 &amp;152 are not algo levels, lnstead they are levels called c_201 c_202" → "Doh, they are supposed to be disabled. That's the old level 101 and 102" → "level 200+ disabled" | `C090N54TG79/1757483290.502629`, `C090N54TG79/1757483515.418369` E0038; `C090N54TG79/1757496724.329169` E0012; `C090N54TG79/1757513008.579639`, `C090N54TG79/1757539495.229289` E0016 — 09-10 |
| "unlock quest after level 16" | `C090N54TG79/1757355103.109279` E0012 09-08 |
| Level 4: simplified 09-15 and PR'd; "Also should I revert the level 4 then?" / "I can revert it to my first difficulty iteration." — no decision recorded | `C090N54TG79/1757959383.428889`, `C090N54TG79/1757959992.127429`; `C090N54TG79/1758302543.832289`, `C090N54TG79/1758302682.866369` E0005 |
| "Do you want me to go through your 200-230 or wrap up to 250?" · "I also made up to 235" · "I will stop level making at 300" · "Needless to mention, I have 300 casual levels and nothing geared to midcore play" | `C090N54TG79/1758302465.958889`, `C090N54TG79/1758302752.063689`, `C090N54TG79/1758689839.300009`, `C090N54TG79/1759173561.454829` E0005 |
| VariantC: "since we simplified the funnel with VariantC" · canvas "VariantC" shared | `C090N54TG79/1758569491.223089` 09-22; `C090N54TG79/1757006744.946909` 09-04 — E0005 |
| A/B of bringing effects forward (09-17/18): "the big idea There is swapping zombie effect tutorials with boosters tutorials" → "Let’s use the past method then" | `C090N54TG79/1758147660.077929`, `C090N54TG79/1758203788.854539` E0038 |
| **09-29 reorder**: "we decided to YOLO and move up card introduction earlier" · "17 -&gt; level 5" · "And then everything else just moves up" · "oki doki, I'll make the Push now" | `C090N54TG79/1759171957.791499`, `C090N54TG79/1759172166.547199`, `C090N54TG79/1759172172.666169` E0016; `C090N54TG79/1759172197.310709` E0005 |
| Objection on record: "throwing that mechanic will not do anything for the funnel and most likely affect it very negatively." · "This is a massive design mistake but I'll love to be Proven wrong" | `C090N54TG79/1759172119.133819`, `C090N54TG79/1759172367.979939` E0005 09-29 |
| Rationale: "For me the differentiating factor of this game comes in too late" · "the order I think should be ⏎  1-kill zombies with items ⏎ 2 - different items hit zombie differently ⏎ 3- items are upgradable ⏎ 4- Booster ⏎ 5- Liveops" | `C090N54TG79/1759172198.547719`, `C090N54TG79/1759172695.000449` E0038 09-29 |
| Cost: "If you're confident we should yolo, it's just one test and one level swap, cheaper then A/B" · "Also, you need to make the level ordering again. Before I did it manually but now we probably need some sort of script for it." | `C090N54TG79/1759173632.306909`, `C090N54TG79/1759173247.603649` E0005 09-29 |
| "unfortunately the build debug option cant help to play algo levels. It’s upto 200 levels. It needs engineering help" | `C090N54TG79/1759255127.258329` E0012 09-30 |
| Pivot options on the table: "1. Auto-play boosters for zombie moments (small pivot) ⏎ 2. Turn based fights (bigger pivot) ⏎ 3. Full auto-play ( massive pivot Capybara-style, potentially even do rogue-lite) ⏎ 4. Pure match-3D without zombies on the top (massive pivot but very little tech work)" | `C090N54TG79/1758517286.431379` E0038 09-22 |

## E Sound

| Cue / asset | Status and who (verbatim) | Pointer · speaker · date |
|---|---|---|
| Soundtrack, normal mode vs endless mode | "I was wondering if I can add the other soundtrack for endless mode" → "Sure" · "I like the main game mode sountrack better, not completely sold on the endless one" · "Okay so I let the same for endless mode then?" → "For now sure" | `C09A7PDFYCV/1755186072.841979` E0006; `C09A7PDFYCV/1755186096.448679`, `C09A7PDFYCV/1755191845.964119` E0016; `C09A7PDFYCV/1755192510.576759`, `C09A7PDFYCV/1755192529.748409` — 08-14 |
| Third endless track | file `zombie-2 endless.mp3`; "guitar is overpowering"; "Should I create a poll in Company Internal for the 3 soundtracks on endless mode?" (no answer) | `C09A7PDFYCV/1755192541.855179`, `C09A7PDFYCV/1755193793.520619` E0006; `C09A7PDFYCV/1755192737.637309` E0016 |
| SFX loudness | "There are also some SFX  too loud, not sure if we can normalize their levels." · "that could be something else for polish I guess." | `C09A7PDFYCV/1755186871.892609`, `C09A7PDFYCV/1755207533.121739` E0006 08-14 |
| Combo meter / multiplier tick | "you find any good sound for the combo meter?" → "we could try using a place holder for now" (ten `food match 3d*.m4a`) · "I'm trying to generate them from elevenlabs but it sucks at generating scales" · ten `RPG_item_collecting_*.wav` → "This one is decent" · "This is when the multipleir is ticking up" · "Please keep in mind this will play simultaneously as the cannon sound, so it needs to be bold" · "I like [PERSON_NAME_0029]'s, either of one of the first three." · "can you add maybe 3-5 more scale?… it's common that someone gets to 15x multiplier" → `RPG_item.rar` "here are 15 in total." → "Perfect" | `C09A7PDFYCV/1755216428.549579` E0016; `C09A7PDFYCV/1755216739.663689`, `C09A7PDFYCV/1755295688.205619`, `C09A7PDFYCV/1755458431.125029` E0006; `C09A7PDFYCV/1755464963.472759`, `C09A7PDFYCV/1755540777.438779`, `C09A7PDFYCV/1755541416.578719` E0016; `C09A7PDFYCV/1755541899.564639` E0005; `C09A7PDFYCV/1755551413.008099` E0016; `C09A7PDFYCV/1755553677.150799` E0006; `C09A7PDFYCV/1755555277.111889` E0016 — 08-15 → 08-18 |
| E0016's alternative sets | files "Games, Video, Menu UI, Notification 03 S…" (10) and "01-…05-User Interface, Alert, Notification" (5) | `C09A7PDFYCV/1755540715.665829`, `C09A7PDFYCV/1755541013.388699` E0016 08-18 |
| Hand-off | "It seems like yours is good, should we clean it up and ship it to [PERSON_NAME_0120] to implement?" · "We can ship this over to [PERSON_NAME_0120] when it's done" | `C09A7PDFYCV/1755545399.193319`, `C09A7PDFYCV/1755551424.360159` E0016 08-18 |
| Format | "I'm seeing Unity helps compress those files... .wav is recommended instead of mp3… Is no crucial, just recommended." · "Reaper is a good tool to normalize sounds btw" | `C09A7PDFYCV/1755545560.145149`, `C09A7PDFYCV/1755545686.750969` E0006 08-18 |
| Cannon sound | exists (referred to, see above) | `C09A7PDFYCV/1755541416.578719` |
| Glass impact SFX | [Linear ZOM-475 "consecutive-glass-impact-sfxvfx-causes-crash-on-android"] "bug on Android after consecutive glass VFX/SFX" | `C090N54TG79/1757539474.366249` E0012 09-10 |
| Reward / UI animation SFX | "I need to add sounds to this things so i can give to the engeneers" · file `rewardsWithSfx001.mp4` · "i probably gona add some sfx to it" (object effect) | `C09ATAJ220H/1755267688.073039` E0002 08-15; `C09ATAJ220H/1755760241.870729` E0026 08-21; `C09ATAJ220H/1756912811.188649` E0002 09-03 |
| Player reaction | "And There were numerous compliments on the sound" | `C090N54TG79/1758582200.575879` E0016 09-22 |
| Sound-mute bug | "And also the muting problem when the game is in background." → "It's just permanently off" / "Until reset of the app" | `C090N54TG79/1758564414.759259` E0012; `C090N54TG79/1758564828.024939`, `C090N54TG79/1758564830.848329` E0016 09-22 |
| What the vendor wants for the ZM3D playable | "*Audio:* Matching sound, rocket sound, explosion sound, success/failure sounds, background music" · "Sound: .mp3 or .wav" | `C08H78VJG80/1758283671.878269` P6078 09-19 |
| Vendor's music rules (DD round) | "ad appropriate would be better, we will make it editable anyway so you can iterate them later" · "music has to start after first click as a rule." | `C08H78VJG80/1743772540.927359`, `C08H78VJG80/1744637266.363689` P6073 |
| DD sound pack as precedent | list in `C08H78VJG80/1744059855.381899` (see B1): three cues "Should be *remotely changeable*" | E0026 04-07 |

- Who makes sound: E0006 (Calvin Price) sources / generates / pitch-shifts; E0016 (Robert) directs and picks; E0002 (Marcus Bennett) adds SFX to his animations; implementation goes to "[PERSON_NAME_0120]".
- Temp / licensed / final labels: only "place holder" (combo meter, 08-15) and "For now sure" (endless track). **No message states that any cue is licensed, final, or cleared for outside use.** No ZM3D audio was sent to the vendor in the channel.

## F House rules

Sentences that state how something must be done. (No sentence of the form "anything sent outside needs…" or "a pass stands until…" exists in these four channels.)

| Rule (verbatim) | Pointer · speaker · date |
|---|---|
| "Let’s be super clear on who owns what and the product owner is responsible to deliver end-to-end. IF you can’t own something give it to someone else but please be explicit." | `C090N54TG79/1757617127.228699` E0038 09-11 |
| "I know everyone is busy - let’s overcommunicate and tell people if your plate is full" | `C090N54TG79/1757617186.873019` E0038 09-11 |
| "please don’t add people to this channel" · "we should be able to talk to each other with no worrying about what other team would say/think" · "he is not in this channel and please don’t add him here" (about E0025) | `C090N54TG79/1757612648.292579`, `C090N54TG79/1757612685.736369` 09-11; `C090N54TG79/1758148782.438299` 09-17 — E0038 |
| "can you thread please?" · "otherwise we’ll have 100s of messages lol" | `C090N54TG79/1758583050.535509`, `C090N54TG79/1758583063.198579` E0038 09-22 |
| "Don't use Domino Delights documents for Zombie Match features, please." · "Engineers struggle when documents are incomplete in quantity… please make sure your documents are completed in this regard before you kickoff a feature." · "We did remind him we expect documents to be a guide of its own without additional tickets." | `C090N54TG79/1756838780.659279` E0005 09-02 |
| "New rule is that, whatever you equipped comes extra onto your pile" | `C090N54TG79/1757338977.703459` E0005 09-08 |
| "Whatever you do should be pr’ed" | `C090N54TG79/1757448632.756159` E0012 09-09 |
| "I suggested that we merge it into main after the submission build. Adding this feature directly into the submission build could be risky" | `C090N54TG79/1757534327.502209` E0026 09-10 |
| "and Blake (or I) shouldn’t have released it without QA check" | `C090N54TG79/1756751373.593569` E0038 09-01 |
| "even if we want to fix it it will take us 3 days and approvals from app stores to fix it" · "that’s why we need to be able to do this remote config" | `C090N54TG79/1757713193.398699`, `C090N54TG79/1757713175.441999` E0038 09-12 |
| "Beta must be tech stable, no excuses." · "Everyone: get real-life feedback from 25–45 casual and/or RPG gamer friends (not kids). No coaching, just observe and collect honest reactions." | `C090N54TG79/1758517286.431379` E0038 09-22 |
| "Let's ask [PERSON_NAME_0022] at prod" (what goes in a release) | `C090N54TG79/1757951958.746669` E0016 09-15 |
| "no one enrages in level 1 or level 2 by design" · "make sure the level can be beaten if you enrage 3 times in a row please" (contested: "It's the wrong kind of safety valve") | `C090N54TG79/1757958276.942089`, `C090N54TG79/1757958047.215619` E0038; `C090N54TG79/1757959175.695419` E0005 — 09-15 |
| "Yes only as cards, board objects are fine" (progression gates cards, not board appearance) | `C090N54TG79/1756754955.796139` E0012 09-01 |
| "Guys, when the first wave is like this, meaning There can and cannot be a monster before the prewarm, the level will \"sometimes\" end prematurely. Let's avoid this situation." | `C090N54TG79/1756990809.900749` E0005 09-04 |
| New items: "per usual, I put them under collection 11 for the time being" · "New Item Thread, in ( ) is the item cloned from" | `C090N54TG79/1758063859.325879`, `C090N54TG79/1758757016.553559` E0016 |
| "usability first" | `C090N54TG79/1758822627.839059` E0016 09-25 |
| "First, we need to finalize which items and zombies will be used on the Design side. After that, I will gather the assets and zip them" | `C08H78VJG80/1758552921.729409` E0026 09-22 |
| "But if we are going to stop the process, we should say it asap" | `C090N54TG79/1759141909.436389` E0026 09-29 |
| "Let’s add this swap to your to do list on Trello" | `C090N54TG79/1757732339.266519` E0038 09-13 |
| Animation rules: "these animations should be skippable by tapping the screen" · "This animation should not be skippable" · "the animation must always be at the final frame in order to return to the main menu" · "Developers definitely need to provide guidance during the implementation process of these animations. Because every animation we add has to be connected in some way to the code and the game flow." · "the chest need to open first and then the rewards come out" | `C09ATAJ220H/1755195675.261079`, `C09ATAJ220H/1755195840.336029`, `C09ATAJ220H/1757009266.906409`, `C09ATAJ220H/1755263226.656319` E0026; `C09ATAJ220H/1757407592.479399` E0002 |
| Vendor standing rules: "we need fbx file format for 3d assets. you can directly zip the assets and send them through here" · "we can’t open prefabs, we directly need the fbx exports" · "we need the animation embedded with the character models in the fbx file, rather than being separate files" · "when exporting .fbx, please make sure it’s exported in *Binary format*, not ASCII" · "for 2D animations, character parts need to be separated into pieces" · "music has to start after first click as a rule" · "we are limited to what you send us for animations at the end of the day" · "Normally, before starting we optimize and review the assets to make sure everything runs smoothly." · "Since we don’t use Unity to develop the playables, we need to adapt the characters you provided to our pipeline." · "as we create that UI custom for each game, There is no documentation" · "at most, one very obvious mechanic is included in the top-performing playables we’ve seen" | pointers in B1 / B2 |
| HG feedback convention to the vendor: "The critical items are P0(s) and P1s." | `C08H78VJG80/1744232118.081379` E0038 04-09 |
| HG on music: "I need to talk to the marketing team about music." | `C08H78VJG80/1743772445.340109` E0005 04-04 |
| Outside window (2025-07-25, keyword hit): "When we ship the a/b test build it will be using main and not a parallel forever branch." | `C090N54TG79/1753458838.723249` E0025 |

## G Records dated 2025-10-01 00:00–07:00 UTC

**None found in any of the four channels.** No `2025-10` month file exists for `C090N54TG79`, `C08H78VJG80`, `C09ATAJ220H` or `C09A7PDFYCV` (helper prints MISSING), and the last timestamps in the September files are 2025-09-30 19:35 (`C090N54TG79/1759260933.283799`) and 2025-09-30 09:59 (`C08H78VJG80/1759226395.551469`).

## H People resolved

Resolved with `Task_Authoring/tools/entity.py resolve`.

| Id | Name | Role in registry | Seen in | Note |
|---|---|---|---|---|
| E0002 | Marcus Bennett | Artist / Design | #zm-animations, #zombie-design, #zombie-sfx (member) | Called "Marcus" in text. Left #zombie-design 2025-09-11 (`C090N54TG79/1757612613.847149`; "I kicked out Marcus and [PERSON_NAME_23645]" `C090N54TG79/1757612639.935649`) |
| E0003 | Oliver Brooks | Senior Game Engineer / Engineering | #zm-animations (joined, tagged) | "will bring over the DD system while implementing Season Pass and Axe Arena" `C09ATAJ220H/1755760241.870729` |
| E0006 | Calvin Price | Game Engineer (Unity VFX) / Engineering | #zm-animations, #zombie-sfx | Makes sound scales and VFX integration; posts build numbers |
| E0021 | Owen Baker | Game Engineer (Unity) / Engineering | #zm-animations | Collect & Win animation |
| E0025 | Arthur Blake | Co-founder & CTO / Executive | vendor channel, #zombie-design | "our CTO Blake"; left #zombie-design 2025-09-11 (`C090N54TG79/1757612621.967839`) |
| E0030 | Victor Barnes | Game Engineer / Engineering (registry) | vendor channel 2025-03-06 | Slack text introduces this account as "our Art Director [PERSON_NAME_0116]" (`C08H78VJG80/1741284418.429369`, join `C08H78VJG80/1741284426.648909`). Registry role and Slack text disagree. Last Slack post 2025-04-15 |
| E0033 | Martin Walsh | Game Designer / Design | #zm-animations 09-03 | one comment on title animation |
| P6089 | unidentified (no name) | — | all channels | System-like account: "*Harmony Games* has joined this channel by invitation from *PlayableX*." `C08H78VJG80/1741284204.238979`; empty-text posts elsewhere |
| P6078 | unidentified (no name) | PlayableX — "our product manager will be leading the process" (`C08H78VJG80/1756321837.876699`) | vendor channel | 18 Slack messages in total, all in this channel; first 2025-08-26, last 2025-09-30 |
| P3937 | unidentified (no name) | PlayableX — account contact | vendor channel | Registry: last Slack post 2025-09-24, but last post in this channel is 2025-08-27 → posts exist elsewhere |
| P6073 | unidentified (no name) | PlayableX — delivery contact in the DD round | vendor channel | Registry: last Slack post 2025-05-21; last here 2025-04-28 → posts exist elsewhere |

Known ids, registry role vs what Slack says (worth knowing before writing new records):

| Id | Registry | Slack text |
|---|---|---|
| E0005 Julia Lawson | Product Manager / Product | "our lead designer" (`C08H78VJG80/1741796408.361009`); builds levels |
| E0026 Brian Foster | Game Engineer / Engineering | "Product Manager" (same message); owns tutorials, QA of features, asset packaging |
| E0008 Frederick Stone | Co-founder / Executive | runs UA / the vendor thread |
| E0038 Leonard Hayes | Co-founder & Creative Director / Executive | called "Leonard"; sets priorities |
| E0016 Robert | Co-Founder & Creative Director / Executive | builds levels and items |
| E0012 Vincent Parker | Game Systems Engineer / Engineering | card progression, zombie lane economy |
| E0009 Claire Morgan | Art Lead / Design | tagged once, never posts in these windows |

Name tokens — my inference from reply patterns, not a registry lookup: `[PERSON_NAME_0092]` = Brian Foster (E0026); `[PERSON_NAME_0036]` = Frederick Stone (E0008); `[PERSON_NAME_0040]` and `[PERSON_NAME_0019]` both = Julia Lawson (E0005); `[PERSON_NAME_0050]` = Vincent Parker (E0012); `[PERSON_NAME_0029]` = Calvin Price (E0006); `[PERSON_NAME_0022]` ≈ Oliver Brooks (E0003; Season Pass / Axe Arena engineer); `[PERSON_NAME_0067]` ≈ Owen Baker (E0021; Collect & Win); `[PERSON_NAME_0116]` = the Art Director account E0030. Unresolved: `[PERSON_NAME_0120]` (senior engineer who implements sounds), `[PERSON_NAME_0054]` (E0038's "[PERSON_NAME_0054] and I had a long convo"), "Douglas" (data / backend, appears un-redacted).

## I #zombie-design thread roots from 2025-09-22

Declared reply count = replies present in the export for every root below.

| UTC | Root pointer | By | Replies | Topic |
|---|---|---|---|---|
| 09-22 18:06 | `C090N54TG79/1758564414.759259` | E0012 | 4 | Sound mutes after app is backgrounded; cannot reproduce |
| 09-22 18:42 | `C090N54TG79/1758566578.126569` | E0026 | 4 | Competitor gossip (YouTube link, Cypher Games) |
| 09-22 18:53 | `C090N54TG79/1758567201.262949` | E0026 | **26** | **Playable ad scenario: which items / zombies; hardcore vs casual; reference level** |
| 09-22 22:54 | `C090N54TG79/1758581651.167799` | E0005 | 15 | Why playtesters get no "kick of joy"; star ratings |
| 09-22 23:11 | `C090N54TG79/1758582703.744009` | E0016 | 2 | Bad AI transcript of playtest |
| 09-23 22:41 | `C090N54TG79/1758667286.925349` | E0016 | 11 | Monster HP scaling 2% per 10 levels; item damage figures |
| 09-24 05:23 | `C090N54TG79/1758691397.679889` | E0016 | 2 | Playtestcloud audience definition |
| 09-24 23:36 | `C090N54TG79/1758757016.553559` | E0016 | 13 | **New Item Thread** (clones, with videos) |
| 09-25 10:40 | `C090N54TG79/1758796815.758229` | E0012 | 9 | Zombie HP bar thickness (IMG_4606.png) |
| 09-25 19:50 | `C090N54TG79/1758829814.098939` | E0038 | 3 | Copy an existing game's balance; level templates; player level |
| 09-29 02:48 | `C090N54TG79/1759114127.213749` | E0038 | 3 | **Pause the playable; dev money** |
| 09-29 18:55 | `C090N54TG79/1759172119.133819` | E0005 | 9 | **Ice-cream level simplified; objection; replies are about bots and blunder rates** |
| 09-29 19:08 | `C090N54TG79/1759172937.229039` | E0005 | 4 | **Ice-cream level screenshot approved, pushed to level design branch** |
| 09-29 19:19 | `C090N54TG79/1759173561.454829` | E0005 | 4 | "300 casual levels and nothing geared to midcore play" |
| 09-29 19:20 | `C090N54TG79/1759173637.851689` | E0038 | 3 | What a hardcore level is ("hunting a grenade") |
| 09-29 19:21 | `C090N54TG79/1759173698.236239` | E0005 | 2 | Deck-building blocks in levels |
| 09-29 19:22 | `C090N54TG79/1759173778.362129` | E0005 | 1 | Ignoring "too hard" complaints; dynamic difficulty |
| 09-29 20:16 | `C090N54TG79/1759176983.189479` | E0016 | 1 | What 0.3.22 had and what is kept; leaning hardcore |
| 09-30 04:53 | `C090N54TG79/1759207989.371869` | E0016 | 8 | Bots in user logs (Begin1NoLeft5Bots.csv) |

Densest stretch outside threads: 09-29 18:52 → 19:23, 57 top-level messages on the card reorder and hardcore/casual direction (`C090N54TG79/1759171957.791499` → `C090N54TG79/1759173807.722729`). For reference, the largest thread just before the window: `C090N54TG79/1757338977.703459` (09-08, 32 replies, equipped-item insertion rule) and `C090N54TG79/1757610123.816419` (09-11, 27 replies, boss arena).

## Z Things I could not read or was unsure about

1. **Attachments are names only.** I could not open any file: the vendor's scenario Google doc (`C08H78VJG80/1756393065.804409`), the "brief" image (`C08H78VJG80/1756223954.141059`), the reference-level video `20250923-1936-36.8420811.mp4`, the three zips, the ice-cream level screenshot (`C090N54TG79/1759172937.229039`), the DD "Playable Feedback" doc. So the content of Scenario 1, the items in the reference level, and the level number of the reference level are unknown from these channels.
2. **"this version"** in E0026's 09-22 question (`C090N54TG79/1758567201.262949`) has no attachment in the export; I do not know what version it points to.
3. **Missing replies:** `C09ATAJ220H/1757464811.241579` (E0016, 2025-09-10, VFX for bread/cookie and gift box) declares 8 replies; none are in the export. It is also the last message of that channel.
4. **Redacted names:** one item pair in the New Item Thread is `[USERNAME_36211]` / `[USERNAME_36210]` (chocolate-related); a booster is `[USERNAME_3114]`; a game mode is `[USERNAME_49455]` / `[USERNAME_15751]`; competitor names are tokens. Person tokens in H are inference.
5. **Registry vs Slack roles** disagree for E0005, E0026 and E0030 (see H). I did not resolve which is intended.
6. **Other places the vendor posts:** P3937 and P6073 have Slack activity later than their last message in `C08H78VJG80` (per `entity.py`), so another channel or DM with PlayableX staff exists. Not searched (outside scope).
7. **#zombie-design June–August 2025** (1,879 messages) was not read; only the keyword hits in A7 / F. The 82-reply thread `C090N54TG79/1752230344.088959` (dynamite / grenade as cards) is likely relevant to what the grenade does and is unread.
8. **Typos kept as written** ("shruiken", "cheeries", "packpack", "revelaed"); `C090N54TG79/1757965299.265779` says "lots of monsters for performance reasons" where "less" may have been meant.
9. **No money figures, contract terms, size limit from the vendor, or final item list** exist in these four channels; if the task needs them they must come from another source (mail, Drive, Linear) or be new.
10. The helper sorts by `ts` and shows `user`, files and text only; reactions, edits and message subtypes are not shown, so an approval given by emoji would be invisible to me.

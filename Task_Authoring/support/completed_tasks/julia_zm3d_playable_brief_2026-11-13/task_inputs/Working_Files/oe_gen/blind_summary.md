Blind passes, local rehearsal (tools/blind_review.py; LOCAL REHEARSAL, not a platform verdict). round2 (full, 130 event(s) in scope): O1 PASS, O2 NON-FAIL (OE 130 missing_dependency Minor), O3 61 inventory item(s) · round3 (changed, 1 event(s) in scope): O1 PASS, O2 PASS · round4 (changed, 9 event(s) in scope): O1 PASS, O2 NON-FAIL (OE 130 missing_dependency Minor) · round5 (changed, 1 event(s) in scope): O1 PASS, O2 PASS. Platform /oe round 1 (eval_reports/6aea4c201e1fa1ddfdd0a25d_2_oe.md, FAIL 2) found OE 20's purpose accepted a walked-back alternative and OE 10 left out the walk-back; both fixed (OE 10 now reads Robert's 'Doesn't really matter' and 'I think we should remain as is', OE 20 carries one purpose). Each Minor dependency finding on OE 130 is fixed: it now depends on the file writes OE 20 to OE 22 and the eight shares OE 23 to OE 30. O3 inventory (round2, carried): 61 item(s), each matched below to the reads that see both sides and the writes that make the fix (60 matched, 1 UNSURE resolved, 0 unmatched).

| Item | Line or field | Reads (both sides) | Writes (the fix) | Result |
|---|---|---|---|---|
| I1 | DES-316 Alarm Clock (Owed, Brian) | OE 3, OE 5, OE 12 | OE 22, OE 31, OE 32 | matched |
| I2 | DES-317 Record Player (Owed, Brian) | OE 3, OE 5, OE 12 | OE 22, OE 33, OE 34 | matched |
| I3 | DES-318 Retro TV (Owed, Brian) | OE 3, OE 5, OE 12 | OE 22, OE 35, OE 36 | matched |
| I4 | DES-361 Coffee Machine (Owed, Brian) | OE 3, OE 5, OE 12 | OE 22, OE 73, OE 74 | matched |
| I5 | DES-362 Cooler (Owed, Brian) | OE 3, OE 5, OE 12 | OE 22, OE 75, OE 76 | matched |
| I6 | DES-363 Ice Cream Machine (Owed, Brian) | OE 3, OE 5, OE 12 | OE 22, OE 77, OE 78 | matched |
| I7 | DES-364 Kitchen Mixer (Owed, Brian) | OE 3, OE 5, OE 12 | OE 22, OE 79, OE 80 | matched |
| I8 | DES-365 Microwave (Owed, Brian) | OE 3, OE 5, OE 12 | OE 22, OE 81, OE 82 | matched |
| I9 | DES-366 Oven (Owed, Brian) | OE 3, OE 5, OE 12 | OE 22, OE 83, OE 84 | matched |
| I10 | DES-367 Refrigerator (Owed, Brian) | OE 3, OE 5, OE 12 | OE 22, OE 85, OE 86 | matched |
| I11 | DES-368 Stove (Owed, Brian) | OE 3, OE 5, OE 12 | OE 22, OE 87, OE 88 | matched |
| I12 | DES-369 Toaster (Owed, Brian) | OE 3, OE 5, OE 12 | OE 22, OE 89, OE 90 | matched |
| I13 | DES-348 Bathroom Scale (Owed, Claire) | OE 3, OE 5, OE 13 | OE 22, OE 47, OE 48 | matched |
| I14 | DES-349 Bathtub (Owed, Claire) | OE 3, OE 5, OE 13 | OE 22, OE 49, OE 50 | matched |
| I15 | DES-350 Cabinet Sink (Owed, Claire) | OE 3, OE 5, OE 13 | OE 22, OE 51, OE 52 | matched |
| I16 | DES-351 Flip Flops (Owed, Claire) | OE 3, OE 5, OE 13 | OE 22, OE 53, OE 54 | matched |
| I17 | DES-352 Iron (Owed, Claire) | OE 3, OE 5, OE 13 | OE 22, OE 55, OE 56 | matched |
| I18 | DES-353 Ironing Board (Owed, Claire) | OE 3, OE 5, OE 13 | OE 22, OE 57, OE 58 | matched |
| I19 | DES-354 Plunger (Owed, Claire) | OE 3, OE 5, OE 13 | OE 22, OE 59, OE 60 | matched |
| I20 | DES-355 Slippers (Owed, Claire) | OE 3, OE 5, OE 13 | OE 22, OE 61, OE 62 | matched |
| I21 | DES-356 Toilet (Owed, Claire) | OE 3, OE 5, OE 13 | OE 22, OE 63, OE 64 | matched |
| I22 | DES-357 Toilet Paper (Owed, Claire) | OE 3, OE 5, OE 13 | OE 22, OE 65, OE 66 | matched |
| I23 | DES-358 Wash Basin (Owed, Claire) | OE 3, OE 5, OE 13 | OE 22, OE 67, OE 68 | matched |
| I24 | DES-359 Washing Machine (Owed, Claire) | OE 3, OE 5, OE 13 | OE 22, OE 69, OE 70 | matched |
| I25 | DES-379 Acoustic Guitar (Owed, Brian) | OE 3, OE 5, OE 14 | OE 22, OE 95, OE 96 | matched |
| I26 | DES-380 Cello (Owed, Brian) | OE 3, OE 5, OE 14 | OE 22, OE 97, OE 98 | matched |
| I27 | DES-381 Cymbals (Owed, Brian) | OE 3, OE 5, OE 14 | OE 22, OE 99, OE 100 | matched |
| I28 | DES-382 Electric Guitar (Owed, Brian) | OE 3, OE 5, OE 14 | OE 22, OE 101, OE 102 | matched |
| I29 | DES-383 Harp (Owed, Brian) | OE 3, OE 5, OE 14 | OE 22, OE 103, OE 104 | matched |
| I30 | DES-384 Tambourine (Owed, Brian) | OE 3, OE 5, OE 14 | OE 22, OE 105, OE 106 | matched |
| I31 | DES-385 Trumpet (Owed, Brian) | OE 3, OE 5, OE 14 | OE 22, OE 107, OE 108 | matched |
| I32 | DES-386 Xylophone (Owed, Brian) | OE 3, OE 5, OE 14 | OE 22, OE 109, OE 110 | matched |
| I33 | DES-402 Rocket sound (Owed, Calvin) | OE 3, OE 5, OE 15 | OE 22, OE 117, OE 118 | matched |
| I34 | DES-403 Explosion sound (Owed, Calvin) | OE 3, OE 5, OE 15 | OE 22, OE 119, OE 120 | matched |
| I35 | DES-323 Chainsaw (Ready) | OE 3, OE 5, OE 10, OE 14 | OE 22 | matched |
| I36 | DES-336 Cone (Ready) | OE 3, OE 5, OE 10, OE 14 | OE 22 | matched |
| I37 | DES-389 Cactus Plant (Ready) | OE 3, OE 5, OE 10, OE 11, OE 14 | OE 22 | matched |
| I38 | DES-326 Dynamite (Ready) | OE 3, OE 5, OE 10, OE 11 | OE 22 | matched |
| I39 | DES-335 Bow (Ready) | OE 3, OE 5, OE 11 | OE 22 | matched |
| I40 | DES-315 Couch and Pillow (Delivered) | OE 3, OE 4, OE 5, OE 7, OE 16 | OE 22 | matched |
| I41 | DES-333 Plushie Bunny (Delivered) | OE 3, OE 4, OE 5, OE 7, OE 16 | OE 22 | matched |
| I42 | Brief, board field | — | OE 20 | matched |
| I43 | Brief, zombies field | — | OE 20 | matched |
| I44 | Brief, start date field | — | OE 20 | matched |
| I45 | Brief, tray field | — | OE 20 | matched |
| I46 | DES-321 Fly Zapper (Owed, Claire) | OE 3, OE 5 | OE 22, OE 37, OE 38 | matched |
| I47 | DES-331 Fire Extinguisher (Owed, Claire) | OE 3, OE 5 | OE 22, OE 39, OE 40 | matched |
| I48 | DES-332 Propane Tank (Owed, Brian) | OE 3, OE 5 | OE 22, OE 41, OE 42 | matched |
| I49 | DES-346 Toy Train (Owed, Brian) | OE 3, OE 5 | OE 22, OE 43, OE 44 | matched |
| I50 | DES-347 Beach Ball (Owed, Claire) | OE 3, OE 5 | OE 22, OE 45, OE 46 | matched |
| I51 | DES-360 Rubber Ducky (Owed, Claire) | OE 3, OE 5 | OE 22, OE 71, OE 72 | matched |
| I52 | DES-377 Small Kettle (Owed, Brian) | OE 3, OE 5 | OE 22, OE 91, OE 92 | matched |
| I53 | DES-378 Tall Kettle (Owed, Brian) | OE 3, OE 5 | OE 22, OE 93, OE 94 | matched |
| I54 | DES-388 Grand Piano (Owed, Claire) | OE 3, OE 5 | OE 22, OE 111, OE 112 | matched |
| I55 | DES-396 Wheelbarrow (Owed, Claire) | OE 3, OE 5 | OE 22, OE 113, OE 114 | matched |
| I56 | DES-397 Wooden Crate (Owed, Brian) | OE 3, OE 5 | OE 22, OE 115, OE 116 | matched |
| I57 | DES-406 Background music (Owed, Calvin) | OE 3, OE 5, OE 15 | OE 22, OE 121, OE 122 | matched |
| I58 | DES-407 Item visuals (Owed, Brian) | OE 3, OE 5 | OE 22, OE 123, OE 124 | matched |
| I59 | DES-408 UI elements (Owed, Brian) | OE 3, OE 5 | OE 22, OE 125, OE 126 | matched |
| I60 | DES-409 Fonts (Owed, Martin) | OE 3, OE 5 | OE 22, OE 127, OE 128 | matched |
| I61 | DES-325 Cute Hammer (Ready) | OE 3, OE 5 | OE 22 | resolved: no change (ledger T19); stays Ready |

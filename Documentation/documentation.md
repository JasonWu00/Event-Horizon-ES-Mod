# Documentation

Faction distances

Faction | Min distance to appear | ID
--- | --- | ---
Merchant Alliance | 0 | 201
Pirates | 50 | 202
Syndicated Systems | 100 | 203
Confederation of Free Worlds | 150 | 204
Marauder Pirates | 175 | 219
Republic of Earth | 200 | 205
Hai | 250 | 206
Trisolar Coalition | 250 | 218
Sheragi | 275 | 217
Remnant | 300 | 207
Korath Exiles | 300 | 209
Bunrodea | 325 | 221
Wanderers | 350 | 211
Ka'het | 350 | 210
Kaltheim | 375 | 220
Mereti Collective | 400 | 212
Sestor Federation | 400 | 213
Heliarchs Security Forces | 450 | 208
Quarg | 500 | 214
Pug | 500 | 216
Drak | 750 | 215

Special ships and encounter distances

Ship | Minimum | Maximum
--- | --- | ---
Arfecta | 500 | 1000
Republic Navy Battleship | 350 | 500
Emerald Sword | 250 | 500
Heron | 350 | 500
Kestrel | 150 | 300
KIV 750 | 400 | 600
Marauder Bactrian | 300 | 500
Model 1024 | 400 | 600
Modified Boxwing | 100 | 250
Modified Vanguard | 200 | 350
Shooting Star | 350 | 500
Ursa Polaris | 350 | 500
Lycosidae | 300 | 450

Ammunition, Bullet Prefab, and Impact Effect IDs will take the IDs of the weapon.

Special ships:

Ship Name | Ship ID | Build IDs
--- | --- | ---
Super Kestrel | 1000 | 10000
Kestrel | 1001 | 10001
Star Fortress | 2000 | 20000
Heron | 3000 | 30000
Emerald Sword | 4000 | 40000
Modified Boxwing | 5001 | 5001
Modified Vanguard | 5003 | 5003
Marauder Bactrian | 5004 | 5004
Ursa Polaris | 5005 | 5005
Black Diamond | 3024
Shooting Star | 5006
Navy Battleship | 5007 | 5007
Lycosidae | 5008 | 5008
Model 1024 Infected | 5009 | 5009
Marauder Carrier (Giftbringer) | 5010 | 5010

First unusued quest ID for special ships:

Vanilla-ish items:

Item Name | Item, Stat, Tech IDs
--- | ---
4x4 Titanium | 2100
Heavy Vamp Ray tech | 2101
AI Heavy Vamp Ray tech | 2102
Infesticore | 2103, 2103-2105 
4x4 Shield | 2104
4x4 Reactive | 2105
4x4 Fuel | 2106
4x4 Armored Fuel | 2107
High Energy Focus m3 | 2108
Automated Reloader m3 | 2109
Inertial Neutralizer | 2110

Effects also take the ID of their weapon.

Model sizes:   
1 for drones   
2 for frigates   
3 for destroyers   
4 for cruisers   
5 for battleships   
6 for caps   
12+ for super-capital ships (Heron, Bactrian, Kestrel Tester)   
Add (tier-1) to the model size for appropriate factions.   

Conventions for stat conversions:

Note: Since weapons can now deal separate hull and shield damage, set hull and shield damage separately but using the same rules.

Weapon type | Damage conversion
--- | ---
Projectile weapons | (Shield + Hull) / 10
Beam weapons | (Shield + Hull) / 15
Missiles, torpedoes | (Shield + Hull) / 20 (and / 2 for high damage)
Ion damage | Ion / 20 (or / 50 for high damage)
Push force | (Push / 2.5) * power of 10
Slowing force | Slow / 500
Superweapons | Converted damage / 100

Other weapon stats | Conversion
--- | ---
Energy costs | Cost (/ 10 for high costs)
Projectile, beam, torpedo, rocket range | Range / 10
Missile range | Range / 50
Missile, torpedo reload | Reload / 5 (and / 2.25 for pods)
Cannon reload | Reload / 2
Scanner range | ???
Anti-missile range | Range * 0.2 (Put the value in "Size" field)

Non-weapon stats | Conversion
--- | ---
Battery energy storage | (Energy / space) * 10 (and * 2 for Syscores and Sun Reactors)
Alternate battery energy storage | (Energy / space) / 40 (or /20)
Reactor energy output | Power output / space
Engine thrust | (Thrust / size) / (ion engine thrust / size)
Engine steering | (Steering / size) / (ion engine thrust / size)
Module heat production | Heat / size / 250
Module cooling | Cooling / size / 500 (or / 250 for active cooling)
Active cooling energy cost | Energy / size / 2.5 (or 5?)
Shield health | (Generation / size) * 5
Shield generation | Shield health / 10
Shield gen energy cost | (Shield energy + energy consumption, per second) / size
Hull regeneration | Regen / size
Pug ship stat blocks | Shield, health / 25; 5% shield -> regen

Determining stats:

== Engines ==   

Calculating engine thrust: ((thrust + steering) / (sum of outfit sizes)) / scaler   
Scaler is in the range of (2000, 1500) inclusive and decreases as the "size scale" of the engine increases   
1x1 engines have a scaler of 2000 while Vector Engines have a scaler of 1500   
Afterburners have a scaler of 1000.

Calculating engine power consumption: [(thrust energy + steering energy) / (sum of outfit sizes)] / 10   
Afterburners may or may not experience the division by 10 on a case by case basis.   
For afterburners, add fuel usage * 25 to the top of the inner division.

Afterburner cooldown: heat / size / 10

For referencing values directly from the data files:   
Multiply turn by 60 and thrust by 3600.   
Multiply energy consumption and cooling by 60.   
Multiply shield generation by 60.   

== Pug stats ==   
Divide the numbers in the data files by 25.   
Numbers still too big are then halved.   
Numbers too small are increased by 33%.   

Ship IDs start at 300. Component IDs start at 1000.   
Ship build IDs are equal to Ship ID * 10 + rating.    
Some early build IDs have a trailing 1 to avoid conflict with drone IDs.    
Explosion ammo starts at 5000 and correspond to their parent munition in IDs.   
Gun version of turret weapons start at 2000 and correspond to their turret variant.   
Submunitions for weapons start at 3000 and correspond to their weapon.   

Merchants

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Shuttle | 301 | 3010-3012
Sparrow | 302 | 3020-3022
Star Barge | 303 | 3030-3032
Heavy Shuttle | 304 | 3040-3042
Berserker | 305 | 3050-3052
Flivver | 306 | 3060-3062
Fury | 307 | 3070-3072
Hawk | 308 | 3080-3082
Wasp | 309 | 3090-3092
Clipper | 310 | 3100-3102
Argosy | 311 | 3110-3112
Freighter | 312 | 3120-3122
Hauler 1 | 313 | 3130-3132
Arrow | 314 | 3140-3142
Blackbird | 315 | 3150-3152
Bounder | 316 | 3160-3162
Scout | 317 | 3170-3172
Star Queen | 318 | 3180-3182
Hauler 2 | 319 | 3190-3192
Hauler 3 | 320 | 3200-3202
Behemoth | 321 | 3210-3212
Bulk Freighter | 322 | 3220-3222
nGVF-AA Fuel Cell | 1001
nGVF-BB Fuel Cell | 1002
nGVF-CC Fuel Cell | 1003
nGVF-DD Fuel Cell | 1004
nGVF-EE Fuel Cell | 1005
Bactrian | 323 | 3230-3232
LP036a Battery Pack | 1006
LP072a Battery Pack | 1007
LP144a Battery Pack | 1008
LP288a Battery Pack | 1009
LP576a Battery Pack | 1010
X1050 Ion Engines | 1021
X1700 Ion Thruster | 1011
X1200 Ion Steering | 1012
X2700 Ion Thruster | 1013
X2200 Ion Steering | 1014
X3700 Ion Thruster | 1015
X3200 Ion Steering | 1016
X4700 Ion Thruster | 1017
X4200 Ion Steering | 1018
X5700 Ion Thruster | 1019
X5200 Ion Steering | 1020
Boxwing | 3004
Cooling Vent | 1077
Asteroid Scanner | 1305
KP-6 Photovoltaic Panel | 1412
PK-6 Photovoltaic Array | 1413
Volcano Afterburner | 1409
Hauler 6 | 517 | 5170-5172

Pirates

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Marauder Arrow | 324 | 3240-3242
Marauder Bounder | 326 | 3260-3262
Quad Blaster | 1022
Modified Blaster Turret | 1023
Modified Blaster | 2023
Laser Turret | 1024
Heavy Laser Turret | 1025
Modified Argosy | 327 | 3270-3272
Raven | 328 | 3280-3282
Marauder Fury | 329 | 3290-3292
Meteor Missile Launcher | 1026 (Pod 2026)
Sidewinder Missile Launcher | 1027 (Pod 2027)
Javelin Rocket Launcher | 1028 (Pod 2028)
Gatling Gun | 1029
Falcon | 352 | 3520-3522
Leviathan | 353 | 3530-3532
Hogshead | 477 | 4770-4772
Gunbarge | 511 | 5110-5112
Pirate Freighter | 512 | 5120-5122
Blaster | 2022
Blaster Turret | 4022
Laser Beam | 2024
Heavy Laser | 2025
Gatling Turret | 2029
Javelin Turret | 1274
Barrage Turret | 1275
Twin Blaster | 1296
Twin Mod Blaster | 1297
Cargo Scanner | 1306
Small Interference Plating | 1312
Medium Interference Plating | 1313
Large Interference Plating | 1314
Extra Large Interference Plating | 1315
Small Radar Jammer | 1321
Jackal | 527 | 5270-5272
Monitor | 528 | 5280-5282

Marauder Pirates

Item Name | Item ID | Build ID (if applicable)
--- | --- | ---
Marauder Quicksilver | 436 | 4360-4362
Marauder Raven | 437 | 4370-4372
Marauder Manta | 438 | 4380-4382
Marauder Firebird | 439 | 4390-4392
Marauder Splinter | 440 | 4400-4402
Marauder Leviathan | 441 | 4410-4412
Marauder Falcon | 442 | 4420-4422
Scrapper | 443 | 4430-4432
Nighthawk | 444 | 4440-4442
Cutthroat | 445 | 4450-4452
Bulwark | 446 | 4460-4462
Valkyrie | 447 | 4470-4472
Mammoth | 448 | 4480-4482
RT-II Radiothermal | 1319
Accurate Gatling | 1320
Large Radar Jammer | 1322
Enforcer | 476 | 4760-4762
Saber | 478 | 4780-4782
Heavy Blaster Turret | 1393 (gun 2393)
Overcharged Heavy Blaster | 1430

Syndicate

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Headhunter | 325 | 3250-3252
Quicksilver | 330 | 3300-3302
Corvette | 331 | 3310-3312
Manta | 332 | 3320-3322
Splinter | 333 | 3330-3332
Vanguard | 334 | 3340-3342
Class C Freighter | 335 | 3350-3352
Protector | 336 | 3360-3362
Barb | 3001
RT-I Radiothermal | 1030
NT200 Nucleiovoltaic | 103
S1 Thermionic | 1032
Dwarf Core | 1033
Proton Turret | 1034
Torpedo Launcher | 1035 (Pod 2035)
Nuclear Missile | 1036
Ionic Afterburner | 1037
S270 Regenerator | 1038
S970 Regenerator | 1039
Proton Gun | 2034
Water Cooling System | 1078
Anti-Missile Turret | 1081
Outfit Scanner | 1307
Prong | 3036
Sentinel Reactor | 1414
Covalent Proton Turret | 1415
Meteor Turret | 1421
Sidewinder VLS Rack | 1422
Torpedo Launch Rack | 1423
Harbinger | 535 | 5350-5352
Proton Cascader | 1436

FW

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Firebird | 337 | 3370-3372
Aerie | 338 | 3380-3382
Bastion | 339 | 3390-3392
Mule | 340 | 3400-3402
Osprey | 341 | 3410-3412
Nest | 342 | 3420-3422
Roost | 343 | 3430-3432
Skein | 344 | 3440-3442
Dreadnought | 345 | 3450-3452
Dagger | 3002
Finch | 3003
Chipmunk Plasma Thruster | 1040
Chipmunk Plasma Steering | 1041
Greyhound Plasma Thruster | 1042
Greyhound Plasma Steering | 1043
Impala Plasma Thruster | 1044
Impala Plasma Steering | 1045
Orca Plasma Thruster | 1046
Orca Plasma Steering | 1047
Tyrant Plasma Thruster | 1048
Tyrant Plasma Steering | 1049
Heavy Rocket | 1050 (Pod 2050)
Plasma Turret | 1051 (gun 2051)
Fission Reactor | 1052
Breeder Reactor | 1053
Stack Core | 1054
Flamethrower | 1055 (turret 2055)
D14-RN | 1056
D23-QP | 1057
D41-HY | 1058
Liquid Nitrogen Cooling | 1079
Plasma Repeater | 1084
Quad Plasma Turret | 1246
Capybara Plasma Engines | 1302
Tactical Scanner | 1308
Heavy Rocket Turret | 1378
Caldera Afterburner | 1410
Proton Punt Gun | 1394
Proton Punt Cannon | 1395

Republic

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Rainmaker | 346 | 3460-3462
Gunboat | 347 | 3470-3472
Frigate | 348 | 3480-3482
Cruiser | 349 | 3490-3492
Carrier | 350 | 3500-3502
Auxiliary C | 351 | 3510-3512
Auxiliary H | 3511 | 11511-11513
Auxiliary T | 3512 | 11514-11516
Lance | 3005
Dropship | 3006
Combat Drone | 3007
AR120 Atomic Engines | 1059
A120 Atomic Thruster | 1060
A125 Atomic Steering | 1061
A250 Atomic Thruster | 1062
A255 Atomic Steering | 1063
A370 Atomic Thruster | 1064
A375 Atomic Steering | 1065
A520 Atomic Thruster | 1066
A525 Atomic Steering | 1067
A860 Atomic Thruster | 1068
A865 Atomic Steering | 1069
D67-TM | 1070
D94-YV | 1071
Particle Turret | 1072
Electron Beam Turret | 1073
Typhoon Torpedo | 1074 (Pod 2074)
Fusion Reactor | 1075
Armageddon Core | 1076
Particle Cannon | 2072
Electron Beam | 2073
Liquid Helium Cooling | 1080
Heavy Anti-Missile Turret | 1082
Fusion Cannon | 1298
Ion Beam Turret | 1301 (gun 2301)
Surveillance Pod | 1309
Dual Particle Turret | 1416
R0152 | 1417
R0234 | 1418
R0376 | 1419
R0518 | 1420
Battlecruiser | 514 | 5140-5142
Typhoon Torpedo VLS Rack | 1424

Hai

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Aphid | 354 | 3540-3542
Grasshopper | 355 | 3550-3552
Lightning Bug | 356 | 3560-3562
Water Bug | 357 | 3570-3572
Centipede | 358 | 3580-3582
Geocoris | 359 | 3590-3592
Shield Beetle | 360 | 3600-3602
Solifuge | 361 | 3610-3612
Pond Strider | 362 | 3620-3622
Flea | 3008
Violin Spider | 3009
Chasm Battery | 1083
Fissure Battery | 1085
Gorge Battery | 1086
Ravine Battery | 1087
Valley Battery | 1088
Sand Cell | 1089
Pebble Core | 1090
Geode Reactor | 1091
Boulder Reactor | 1092
Corundum Regenerator | 1093
Diamond Regenerator | 1094
Williwaw Cooling | 1095
Bullfrog Anti-missile | 1096
Chameleon Anti-missile | 1097
Pulse Cannon | 2098
Pulse Turret | 1098
Ion Cannon | 1099
Tracker Pod | 1100
Railgun | 1101
Baellie Atomic Engines | 1102
Basrem Atomic Thruster | 1103
Basrem Atomic Steering | 1104
Benga Atomic Thruster | 1105
Benga Atomic Steering | 1106
Biroo Atomic Thruster | 1107
Biroo Atomic Steering | 1108
Bondir Atomic Thruster | 1109
Bondir Atomic Steering | 1110
Bufaer Atomic Thruster | 1111
Bufaer Atomic Steering | 1112
Sea Scorpion | 425 | 4250-4252
Ionic Blaster | 2245
Ionic Turret | 1245
Tri-pulse Shredder | 1293
Penta Pulser | 2293
Harasser Quad Railgun | 2101
Octa-pulse Annihilator | 3293
Monolith | 1351
Ruby Regenerator | 1352
Predator Engine | 1353
Locust | 3031 | 3031
Tarantula | 467 | 4670-4672
Phrynus | 468 | 4680-4682
Quartz Regenerator | 1411
Tracker Vertical Pod | 1425
Antlion | 524 | 5240-5242
Sea Dragon | 525 | 5250-5252
Anomalocaris | 534 | 5340-5342
Scarab | 536 | 5360-5362
Cicada | 537 | 5370-5372

Remnant

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Starling | 363 | 3630-3632
Gull | 364 | 3640-3642
Ibis | 365 | 3650-3652
Peregrine | 366 | 3660-3662
Pelican | 367 | 3670-3672
Albatross | 368 | 3680-3682
Petrel | 3010
Tern | 3011
Crystal Capacitor | 1114
Point Defense Turret | 1115
Thermoelectric Cooler | 1116
Bellows Afterburner | 1117
Millennium Cell | 1118
Epoch Cell | 1119
Aeon Cell | 1120
Anvil Engines | 1121
Crucible Thruster | 1122
Crucible Steering | 1123
Forge Thruster | 1124
Forge Steering | 1125
Smelter Thruster | 1126
Smelter Steering | 1127
Thrasher Cannon | 2128
Thrasher Turret | 1128
Inhibitor Cannon | 2129
Inhibitor Turret | 1129
EMP Torpedo Bay | 1130 (Pod 2130)
Penguin | 369 | 3690-3692
Ember Tear | 1278
Research Laboratory | 1317
Smew | 3035 | 3035
Swan | 481 | 4810-4812
Swan Alt | 482 | 4820-4822
Robin | 483 | 4830-4832
Merganser | 484 | 4840-4842
Hobby | 513 | 5130-5132
EMP Torpedo Rack | 1426

Coalition

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Arach Courier | 370 | 3700-3702
Arach Transport | 371 | 3710-3712
Arach Freighter | 372 | 3720-3722
Arach Spindle | 373 | 3730-3732
Arach Hulk | 374 | 3740-3742
Kimek Thorn | 375 | 3750-3752
Kimek Briar | 376 | 3760-3762
Kimek Thistle | 377 | 3770-3772
Kimek Spire | 378 | 3780-3782
Saryd Runabout | 379 | 3790-3792
Saryd Visitor | 380 | 3800-3802
Saryd Traveler | 381 | 3810-3812
Saryd Sojourner | 382 | 3820-3822
Small Collector Module | 1131
Large Collector Module | 1132
Small Cogeneration Module | 1133
Large Cogeneration Module | 1134
Cooling Module | 1135
Small Battery Module | 1136
Large Battery Module | 1137
Small Thruster Module | 1138
Small Steering Module | 1139
Large Thruster Module | 1140
Large Steering Module | 1141
Small Shield Module | 1142
Large Shield Module | 1143
Small Repair Module | 1144
Large Repair Module | 1145
Ion Rain Gun | 2154
Ion Hail Turret | 1154

Heliarchs

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Breacher | 383 | 3830-3832
Neutralizer | 384 | 3840-3842
Hunter | 385 | 3850-3852
Interdictor | 386 | 3860-3862
Judicator | 387 | 3870-3872
Punisher | 388 | 3880-3882
Pursuer | 3012
Rover | 3013
Stalker | 3014
Overclocked Repair Module | 1146
Overcharged Shield Module | 1147
Attractor | 1148
Repulsor | 1149
Small Reactor Module | 1150
Large Reactor Module | 1151
Finisher Pod | 1152
Bombardment Cannon | 2153
Bombardment Turret | 1153
Finisher Maegrolain | 1277
Small Recovery Module | 1391
Finisher VLS Pod | 1429

Korath Exiles

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Raider | 389 | 3890-3892
Dredger | 390 | 3900-3902
World-ship | 391 | 3910-3912
Lor'kas Ik 577 | 3911 | 12711-12713
Ra'gru Ik 618 | 3912 | 12721-12723
Kas'lor Ik 582 | 3913 | 12731-12733
Lor'nag Ik 590 | 3914 | 12741-12743
Ra'at Ik 621 | 3915 | 12751-12753
Kasichara A'awoj | 3916 | 12761-12763
Chaser | 3015
Fire-lance | 1155
Small Heat Shunt | 1156
Large Heat Shunt | 1157
Candle-class | 1158
Furnace-class | 1159
Inferno-class | 1160
Plasma Core | 1161
Double Plasma Core | 1162
Triple Plasma Core | 1163
Small Systems Core | 1164
Medium Systems Core | 1165
Large Systems Core | 1166
Grab-strike | 1167
Warder | 1168
Banisher | 1169
Asteroid Thruster | 1186
Asteroid Steering | 1187
Comet Thruster | 1188
Comet Steering | 1189
Lunar Thruster | 1190
Lunar Steering | 1191
Planetary Thruster | 1192
Planetary Steering | 1193
Stellar Thruster | 1194
Stellar Steering | 1195
Reality Vector Engine | 1196
Pillager | 395 | 3950-3952
Marauder Raider | 430 | 4300-4302
Firelight Missile Launcher | 1276
Blaze-Pike | 1289
Inferno | 1290
'nra'ret | 432 | 4320-4322
Liquid Sodium Cooler | 1291
Tiny Systems Core | 1292
Expeller | 1294
Firestorm Battery | 1295
Lagrange Heaver | 1299
Shipper | 433 | 4330-4332
Courier | 434 | 4340-4342
Command Center | 1316
Charm-Scallop | 485 | 4850-4852
Arch-Carrack | 486 | 4860-4862
Echo-Galleon | 487 | 4870-4872
Seedship | 488 | 4880-4882
Firelight Rack | 1427
Firestorm Pop-up Launcher | 1428
KIT 7 | 3038
Fuel Processor | 1435

Bunrodea

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Kaiken | 3033 | 3033
Sasumata | 469 | 4690-4692
Tanto | 470 | 4700-4702
Ararebo | 471 | 4710-4712
Tekkan | 472 | 4720-4722
Kunai | 473 | 4730-4732
Kama | 474 | 4740-4742
Chigiriki | 475 | 4750-4752
Nami Rift Thruster | 1354
Nami Rift Steering | 1355
Ookii Rift Thruster | 1356
Ookii Rift Steering | 1357
Subarashii Rift Thruster | 1358
Subarashii Rift Steering | 1359
Thorax Cannon | 1360
Locust Blaster | 1361 (turret 2361)
Mandible Cannon | 1362
Swarm Pod | 1363
Small Shield Relay | 1364
Large Shield Relay | 1365
Small Nanite Fabricator | 1366
Large Nanite Fabricator | 1367
Quark Reactor | 1368
Electroweak Reactor | 1369
Dark Reactor | 1370
Chiisana Rift Thruster | 1371
Chiisana Rift Steering | 1372
Solar Battery | 1373
Solar Cell | 1374

Ka'het

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Maeri'het | 392 | 3920-3922
Telis'het | 393 | 3930-3932
Vareti'het | 394 | 3940-3942
Faes'mar | 3016
Selii'mar | 3017
Fetri'sei | 449 | 4490-4492
MHD Generator | 1170
Reserve Accumulator | 1171
Shield Restorer | 1172
Grand Restorer | 1173
Compact Engine | 1174
Sustainer Nacelles | 1175
Maeri Engine Nacelles | 1176
Telis Engine Nacelles | 1177
Vareti Engine Block | 1178
Support Cooling | 1179
Primary Cooling | 1180
Annihilator Turret | 1181 (Gun 2181)
Ravager Turret | 1182 (Gun 2182)
EMP Deployer | 1183
MHD Deployer | 1184
Nullifier | 1185

Kaltheim

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Bulkort 2-V | 3030 | 3030
Holzst'nak 11-P | 450 | 4500-4502
Kru'urlin 89-P | 451 | 4510-4512
Lenmig'sraor 52-T | 452 | 4520-4522
Tyar'linhalf 67-G | 453 | 4530-4532
Polar Battery | 1323
Tundra Shield Generator | 1324
Glacial Shield Generator | 1325
Boreal Shield Generator | 1326
Floe Reactor | 1327
Iceberg Reactor | 1328
Engine Destabilizer Turret | 1329 (gun 2329)
Hyperborean Anti-Missile | 1330
Kelvin Beam Turret | 1331 (gun 2331)
Phase Missile Launcher | 1332
Slush Beam | 1333

Wanderers

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Earth Shaper | 396 | 3960-3962
Deep River | 397 | 3970-3972
Riptide | 398 | 3980-3982
Summer Leaf | 399 | 3990-3992
Autumn Leaf | 400 | 4000-4002
Winter Gale | 401 | 4010-4012
Strong Wind | 402 | 4020-4022
Tempest | 403 | 4030-4032
Derecho | 404 | 4040-4042
Hurricane | 405 | 4050-4052
Flycatcher | 3018
Cool Breeze | 3019
Scud | 3020
Small Biochemical Cell | 1197
Large Biochemical Cell | 1198
Bright Cloud | 1199
Dark Storm | 1200
Red Sun | 1201
Yellow Sun | 1202
White Sun | 1203
Blue Sun | 1204
Wanderer Heat Sink | 1205
Wanderer Large Heat Sink | 1206
Sunbeam Turret | 1207 (gun 2207)
Thunderhead Launcher | 1208 (fragment 3208)
Wanderer AM | 1209
Wanderer Heavy AM | 1210
Type 0 Radiant Engines | 1211
Type 1 Radiant Thruster | 1212
Type 1 Radiant Steering | 1213
Type 2 Radiant Thruster | 1214
Type 2 Radiant Steering | 1215
Type 3 Radiant Thruster | 1216
Type 3 Radiant Steering | 1217
Type 4 Radiant Thruster | 1218
Type 4 Radiant Steering | 1219
Type 5 Radiant Thruster | 1220
Type 5 Radiant Steering | 1221
Moonbeam | 1222 (Gun 2222)
Blizzard | 435 | 4350-4352
Heavy Gust | 515 | 5150-5152
Abyssal Stream | 516 | 5160-5162
Squall | 526 | 5260-5262
Hailstone | 3037

Sestor Federation

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
MPT 53 | 406 | 4060-4062
TF 71-L | 407 | 4070-4072
TF 78-O | 408 | 4080-4082
TF 109 | 409 | 4090-4092
FET 243 | 410 | 4100-4102
KIV 349 | 411 | 4110-4112
KIV 750 | 412 | 4120-4122
FL 14 | 3021
FO 27 | 3022
Repeater Turret | 1223 (Gun 2223)
Heavy Repeater Turret | 1224 (Gun 2224)
Detainer Turret | 1225 (Gun 2225)
Piercer Launcher | 1226
Plasma Packet Cannon | 1227
Control Transceiver | 1303
Screener | 3027
FO Detainer | 3028
FO Ionizer | 3029
Ionizer | 1318
TOR 681 | 531 | 5310-5312
MIP 43 | 532 | 5320-5322
NPT 103 | 533 | 5330-5332
MPT 41 | 3039

Mereti Collective

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Model 8 | 413 | 4130-4132
Model 16 | 414 | 4140-4142
Model 32 | 415 | 4150-4152
Model 64 | 416 | 4160-4162
Model 128 | 417 | 4170-4172
Model 256 | 418 | 4180-4182
Model 512 | 419 | 4190-4192
Model 1024 | 420 | 4200-4202
Minelayer | 1228 (submunition | 3228)
Slicer Turret | 1229 (Gun 2229)
Disruptor Turret | 1230 (Gun 2230)
Super Minelayer | 1233
Infected Minelayer | 12331
Reasoning Node | 1304
Model 192 | 489 | 4890-4892
Model 2 | 3034 | 3034
Model 128 Surveyor | 510 | 5100-5102
Model 256 Greenhouse | 529 | 5290-5292
Model 512 Greenhouse | 530 | 5300-5302

Quarg

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Skylark | 421 | 4210-4212
Wardragon | 422 | 4220-4222
Empyrealdragon | 423 | 4230-4232
Elderdragon | 424 | 4240-4242
Battledrake | 3023
Quantum Vacuum Battery | 1234
Ergosphere Core | 1235
Quantum Shield Generator | 1236
Small Graviton Thruster | 1237
Small Graviton Steering | 1238
Medium Graviton Thruster | 1239
Medium Graviton Steering | 1240
Large Graviton Thruster | 1241
Large Graviton Steering | 1242
Skylance | 1243
Stratospear | 1244
New outfits | ...
Fluxion Shield Generator | 1382
Infimum Shield Generator | 1383
Peripheral Repair Hub | 1384
Central Repair Hub | 1385
Gravitational Device | 1386
Antimatter Core | 1387
Blazar Core | 1388
Wardragon-style civilian ships | ...
Drake | 497 | 4970-4972
Hydra Precursor | 498 | 4980-4982
Amphithere | 499 | 4990-4992
Slibinas | 500 | 5000-5002
Kaukas | 501 | 5010-5012
Skylark-style crystal ships | ...
Tarasque | 502 | 5020-5022
Fafnir | 503 | 5030-5032
Superheavy ships (unused) | ...
Gtuhanai | 504 | 5040-5042
Psuchawrl | 505 | 5050-5052
Ancient Quarg ships (unused) | ...
Kalisto | 506 | 5060-5062
Skylark Alt | 502 | 5020-5022
Smaug | 507 | 5070-5072
Zilant | 508 | 5080-5082
Glaurun | 509 | 5090-5092
New ships | ...
Wardrake | 518 | 5180-5182
Guivre | 519 | 5190-5192
Hydra | 520 | 5200-5202
Lindwyrm | 521 | 5210-5212
Improved Wardragon | 522 | 5220-5222
Wyvern | 523 | 5230-5232
Weapons | ...
Skydagger | 1401
Skypiercer (Edenshard sprite) | 1402
Elysian Ranseur | 1403
Cataclist | 1404
Edenshard (Starpilum) | 1405
Turver (Skywrath) | 1406
Doomscythe (Prismatic Shards) | 1407
Celestial Culverin | 1431
Astral Ribault | 1432
Slipstream Projector | 1437

Starbases

Item Name | Item ID
--- | ---
Merchant | 2201 (size 30)
Pirates | 2202
Syndicate | 2203
FW | 2204
Republic | 2205
Hai | 2206 (size 32)
Remnant | 2207 (size 35)
Heliarchs | 2208 (size 42)
Korath Exiles | 2209 (size 35)
Ka'het | 2210
Wanderers | 2211 (size 40)
Mereti | 2212
Sestor | 2213
Quarg | 2214 (size 45)
Coalition | 2215 (size 33)
Marauder Pirates | 2216 (size 20)

Exclusive items (no technology files)

Item Name | Item / Stat / Device ID
--- | ---
Huge Systems Core | 1231
Quad Plasma Core | 1232
Reality Vector Engines | 1196
Dead Ringer | 5000
Nuke on a Cart | 6000
Organ Bomb | 6001
Jump Drive | 7000
Organ Drive | 7001
Hyperdrive | 7002
Scram Drive | 7003
Shooting Star explosion device | 8000
Cloaking Device | 9000
HIPC | 1375
Spatial Inversion Chamber | 1433

Pug

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Zibruka | 426 | 4260-4262
Enfolta | 427 | 4270-4272
Maboro | 428 | 4280-4282
Arfecta | 429 | 4290-4292
Gridfire | 1247
Tier | 3 AM | 1248
Zapper | 1249 (turret 2249)
Seeker | 1250
Tier | 1 AM | 1251
Akfar Thruster | 1252
Akfar Steering | 1253
Cormet Thruster | 1254
Cormet Steering | 1255
Lohmar Thruster | 1256
Lohmar Steering | 1257
Zibruka Stats | 1258
Enfolta Stats | 1259
Maboro Stats | 1260
Arfecta Stats | 1261
Zubera | 431 | 4310-4312
Zubera Stats | 1280
Zambor | 3025
Zambor Stats | 1281
Zalgi | 3026
Zalgi Stats | 1282
Tulikaa | 490 | 4900-4902
Tulikaa Stats | 1392

Drak
Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Void Sprite | 462 | 4620-4622
Void Sprite Infant | 463 | 4630-4632
Embershade | 464 | 4640-4642
Astral Cetacean | 465 | 4650-4652
Ember Waste Node | 454 | 4540-4542
Jje | 455 | 4550-4552
Ayym | 456 | 4560-4562
Embersylph | 457 | 4570-4572
Embersylph 2 | 458 | 4580-4582
Squid | 459 | 4590-4592
Boomerang | 460 | 4600-4602
Plankton | 461 | 4610-4612
Archon | 5000 | 50000
Antimatter Cannon | 1349
AM Field | 1350
Distancer | 1334
Draining Field | 1335
Drak Turret | 1336
Mouthparts | 1337 (big version 2337)
Bio-tractor-beam | 1338
Bioroid Mine Launcher | 1339 (gun 2339)
Absorption Organ | 1340
Antimatter Thruster | 1341
Antimatter Steering | 1342
Short Bio-tractor-beam | 1343
Siphon Ray | 1344 (gun 2344)
Acid Sprayer | 1345
Drak Acid Cloud | 1346
Plankton Siphon Beam | 1347
Astral Cetacean Beam | 1348

Sheragi

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Emerald Sword | 4000
Black Diamond | 3024
Large Hybrid Cooling | 1262
Small Hybrid Cooling | 1263
Large EM Battery | 1264
Small EM Battery | 1265
Fission Drive | 1266
Fusion Drive | 1267
Particle Waveform | 1269
Heavy Ion Cyclotron | 1270
Shard Fabricator | 1271
Dragonflame Cannon | 1272
Sheragi AM | 1273
Fission Core | 1376
Fusion Core | 1377
Small Fusion Drive | 1379
Large Fission Drive | 1380
Medium Hybrid Cooling | 1381
Kinetic Spear Launcher | 1397
Pulse Beam Turret | 1398 (gun 2398)
Particle Waveform Gun | 2269
Solar Intake | 1399
Medium EM Battery | 1396
Fusion Afterburner | 1400
Bronze Edge | 491 | 4910-4912
Ruby Hammer | 492 | 4920-4922
White Brand | 493 | 4930-4932
Gold Shield | 494 | 4940-4942
Platinum Spear | 495 | 4950-4952
Opal Glaive (NOT ADDED) | 496 | 4960-4962
Fusion Power Converter | 1408

Shooting Star

Item Name | Item and Build ID
--- | ---
Crystal Projector | 1283
Floating Crystal | 1284
Crystalline Formation | 1285
Hexagonal Crystal | 1286
Tree Skeleton Key Stone | 1287

First unused IDs:

.json file type | ID
--- | ---
Component | 1439
Ship | 537
Drone | 3040
Quest | 1049

Some ships have baked-in stat boosts or debuffs based on lore reasons.

Ship | Stats | Reason
Model 256 Greenhouse, Model 512 Greenhouse | -40% HP | The greenhouse is a giant weak point
Kas'lor Ik 582 | +100% Energy | It literally hauls fuel (which abstracts to energy)

Some outfits deviate from the "convert ES stats to EH stats as closely as possible, following the conversion conventions" rule. A list of them and differneces are listed below.

Item Name | Differences
--- | ---
Firestorm | -90% energy cost and energy storage
Firelight | -90% energy cost, +100% range, uses the torpedo/rocket equation
Heaver | -50% fire rate, energy cost = firing energy + firing fuel
Detainer, Inhibitor | (Pending)
Bombardment, Thrasher, Thunderhead | +100% projectile speed
Torpedo, Typhoon Torpedo, EMP Torpedo, EMP Deployer, Teciimach Torpedo, Javelin Rocket, Firestorm Missile | +100% projectile speed
Finisher Torpedo | +50% projectile speed
Locust Blaster | +300% projectile speed
Ion Hail, Ion Rain | +33% speed
Javelin Rocket | +100% energy cost
Korath Piercer Missile | -33% projectile mass
Ruby Regenerator | +100% energy cost, +50% heat generation
Monolith Core | +10% energy generation
Dragonflame Cannon | +300% energy cost, +400% damage
Fusion Cannon | +100% energy cost and damage 
Solar Battery | -80% energy storage
Predator Engine | +30% thrust, steering
Heavy Blaster | -50% damage
Large Fission Drive | +100% energy regen
Ranseur | Uses custom damage calculation: source file damage / 5
Turver | +100% projectile speed
Doomscythe | removed direct damage portion
Fission Drive, Large Fission Drive | +150% thrust and steering
Fusion Power Converter | stats are arbitrarily made up
Baellie Engines | -25% thrust and turn
Type 5 Radiant Engines | +57% thrust and turn (to match the engine buffs in [6686](https://github.com/endless-sky/endless-sky/pull/6686) and [9616](https://github.com/endless-sky/endless-sky/pull/9616))
Sentinel Reactor | -10% reactor output
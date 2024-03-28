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
Remnants | 300 | 207
Korath Exiles | 300 | 209
Bunrodea | 325 | 221
Wanderers | 350 | 211
Ka'het | 350 | 210
Kaltheim | 375 | 220
Korath Mereti | 400 | 212
Korath Sestor | 400 | 213
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
Scanner range | ???
Anti-missile range | Range / 25 (Put the value in "Size" field)

Non-weapon stats | Conversion
--- | ---
Battery energy storage | (Energy / space) * 10 (and * 2 for Syscores and Sun Reactors)
Alternate battery energy storage | (Energy / space) / 40?
Reactor energy output | Power output / space 
Engine thrust | (Thrust / size) / (ion engine thrust / size)
Engine steering | (Steering / size) / (ion engine thrust / size)
Module heat production | Heat / size / 250
Module cooling | Cooling / size / 500 (or / 250 for active cooling)
Active cooling energy cost | Energy / size / 2.5
Shield health | (Generation / size) * 5
Shield generation | Shield health / 10
Shield gen energy cost | (Shield energy + energy consumption, per second) / size
Hull regeneration | Regen / size

Determining stats:

== Engines ==   
Ion Engines have arbitrarily determined stats and serve as a baseline.   
For every engine other than Ionics:   
1: Calculate its thrust/turn per unit of outfit space.  
2: Calculate the thrust/turn per unit of the corresponding ion engine (e.g. A860/865 -> X5200/5700).
3: Divide the result of Step 1 by Step 2.   
4: Multiply the value of Step 3 by the in-mod arbitrary stats of the corresponding ion engine.

NOTE: Due to changes to the ion engine stats in base ES, it is important to use the values provided below (sourced from the Endless Sky GitHub repo before 16 April 2022) for the above calculations. These values will be obsoleted in a future update that adjusts all engines to match these changes.

To see all the changes in the 16 April 2022 update: inspect this link: https://github.com/endless-sky/endless-sky/commit/8a503d9bd5e062054549056aa4a730813def8977#diff-7429a26a7e995048c3b962ee40092f520add3a2cad1af48e67e1b46a2bd8f9f3

Engine | Thrust | Turn | Outfit space
--- | --- | --- | ---
X1050 | 14400 | 6600 | 20
X1700 | 21600 | - | 16
X2700 | 41400| - | 27
X3700 | 79560 | - | 46
X4700 | 153000 | - | 79
X5700 | 293400 | - | 134
X1200 | - | 9600 | 12
X2200 | - | 12420 | 20
X3200 | - | 35400 | 35
X4200 | - | 67920 | 59
X5200 | - | 130440 | 89

Calculating engine power consumption:   
1: calculate power per unit of outfit space for desired single or pair of engine(s).   
2: calculate power per unit of corresponding ion engine(s).   
3: divide 1 by 2.   
4: multiply value by the power consumption of the corresponding ion engine.   

For referencing values directly from the data files:   
Multiply turn by 3600 and thrust by 60.   
Multiply energy consumption and cooling by 60.   
Multiply shield generation by 60.   

== Pug stats ==   
Divide the numbers in the data files by 25.   
Numbers still too big are then halved.   
Numbers too small are increased by 33%.   

Ship IDs start at 300. Component IDs start at 1000.   
Explosion ammo starts at 5000 and correspond to their parent munition in IDs.   
Gun version of turret weapons start at 2000 and correspond to their turret variant.   
Submunitions for weapons start at 3000 and correspond to their weapon.   

Merchants

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Shuttle | 301 | 1001-1003
Sparrow | 302 | 1004-1006
Star Barge | 303 | 1007-1007
Heavy Shuttle | 304 | 1010-1012
Berserker | 305 | 1013-1015
Flivver | 306 | 1016-1018
Fury | 307 | 1019-1021
Hawk | 308 | 1022-1024
Wasp | 309 | 1025-1027
Clipper | 310 | 1028-1030
Argosy | 311 | 1031-1033
Freighter | 312 | 1034-1036
Hauler 1 | 313 | 1037-1039
Arrow | 314 | 1040-1042
Blackbird | 315 | 1043-1045
Bounder | 316 | 1046-1048
Scout | 317 | 1049-1051
Star Queen | 318 | 1052-1054
Hauler 2 | 319 | 1055-1057
Hauler 3 | 320 | 1058-1060
Behemoth | 321 | 1061-1063
Bulk Freighter | 322 | 1064-1066
nGVF-AA Fuel Cell | 1001
nGVF-BB Fuel Cell | 1002
nGVF-CC Fuel Cell | 1003
nGVF-DD Fuel Cell | 1004
nGVF-EE Fuel Cell | 1005
Bactrian | 323 | 1067-1069
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

Pirates

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Marauder Arrow | 324 | 1070-1072
Marauder Bounder | 326 | 1076-1078
Quad Blaster | 1022
Modified Blaster Turret | 1023
Modified Blaster | 2023
Laser Turret | 1024
Heavy Laser Turret | 1025
Modified Argosy | 327 | 1079-1081
Raven | 328 | 1082-1084
Marauder Fury | 329 | 1085-1087
Meteor Missile Launcher | 1026 (Pod 2026)
Sidewinder Missile Launcher | 1027 (Pod 2027)
Javelin Rocket Launcher | 1028 (Pod 2028)
Gatling Gun | 1029
Falcon | 352 | 1154-1156
Leviathan | 353 | 1157-1159
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

Marauder Pirates

Item Name | Item ID | Build ID (if applicable)
--- | --- | ---
Marauder Quicksilver | 436 | 1422-1424
Marauder Raven | 437 | 1425-1427
Marauder Manta | 438 | 1428-1430
Marauder Firebird | 439 | 1431-1433
Marauder Splinter | 440 | 1434-1436
Marauder Leviathan | 441 | 1437-1439
Marauder Falcon | 442 | 1440-1442
Scrapper | 443 | 1443-1445
Nighthawk | 444 | 1446-1448
Cutthroat | 445 | 1449-1451
Bulwark | 446 | 1452-1454
Valkyrie | 447 | 1455-1457
Mammoth | 448 | 1458-1460
RT-II Radiothermal | 1319
Accurate Gatling | 1320
Large Radar Jammer | 1322
Enforcer | 476 | 1542-1544
Hogshead | 477 | 1545-1547
Saber | 478 | 1548-1560

Syndicate

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Headhunter | 325 | 1073-1075
Quicksilver | 330 | 1088-1090
Corvette | 331 | 1091-1093
Manta | 332 | 1094-1096
Splinter | 333 | 1097-1099
Vanguard | 334 | 1101-1103
Class C Freighter | 335 | 1103-1105
Protector | 336 | 1106-1108
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

FW

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Firebird | 337 | 1109-1111
Aerie | 338 | 1112-1114
Bastion | 339 | 1115-1117
Mule | 340 | 1118-1120
Osprey | 341 | 1121-1123
Nest | 342 | 1124-1126
Roost | 343 | 1127-1129
Skein | 344 | 1130-1132
Dreadnought | 345 | 1133-1135
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

Republic

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Rainmaker | 346 | 1136-1138
Gunboat | 347 | 1139-1141
Frigate | 348 | 1142-1144
Cruiser | 349 | 1145-1147
Carrier | 350 | 1148-1150
Auxiliary C | 351 | 1151-1153
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

Hai

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Aphid | 354 | 1160-1162
Grasshopper | 355 | 1163-1165
Lightning Bug | 356 | 1166-1168
Water Bug | 357 | 1169-1171
Centipede | 358 | 1172-1174
Geocoris | 359 | 1175-1177
Shield Beetle | 360 | 1178-1180
Solifuge | 361 | 1181-1183
Pond Strider | 362 | 1184-1186
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
Sea Scorpion | 425 | 1373-1375
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
Tarantula | 467 | 1515-1517
Phrynus | 468 | 1518-1520

Remnant

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Starling | 363 | 1187-1189
Gull | 364 | 1190-1192
Ibis | 365 | 1193-1195
Peregrine | 366 | 1196-1198
Pelican | 367 | 1199-1201
Albatross | 368 | 1202-1204
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
Penguin | 369 | 1205-1207
Ember Tear | 1278
Research Laboratory | 1317

Coalition

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Arach Courier | 370 | 1208-1210
Arach Transport | 371 | 1211-1213
Arach Freighter | 372 | 1214-1216
Arach Spindle | 373 | 1217-1219
Arach Hulk | 374 | 1220-1222
Kimek Thorn | 375 | 1223-1225
Kimek Briar | 376 | 1226-1228
Kimek Thistle | 377 | 1229-1231
Kimek Spire | 378 | 1232-1234
Saryd Runabout | 379 | 1235-1237
Saryd Visitor | 380 | 1238-1240
Saryd Traveler | 381 | 1241-1243
Saryd Sojourner | 382 | 1244-1246
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
Breacher | 383 | 1247-1249
Neutralizer | 384 | 1250-1252
Hunter | 385 | 1253-1255
Interdictor | 386 | 1256-1258
Judicator | 387 | 1259-1261
Punisher | 388 | 1262-1264
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

Korath Exiles

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Raider | 389 | 1265-1267
Dredger | 390 | 1268-1270
World-ship | 391 | 1271-1273
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
Pillager | 395 | 1283-1285
Marauder Raider | 430 | 1388-1390
Firelight Missile Launcher | 1276
Blaze-Pike | 1289
Inferno | 1290
'nra'ret | 432 | 1394-1396
Liquid Sodium Cooler | 1291
Tiny Systems Core | 1292
Expeller | 1294
Firestorm Battery | 1295
Lagrange Heaver | 1299
Shipper | 433 | 1397-1399
Courier | 434 | 1400-1402
Command Center | 1316

Bunrodea

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Kaiken | 3033 | 3033
Sasumata | 469 | 1521-1523
Tanto | 470 | 1524-1526
Ararebo | 471 | 1527-1529
Tekkan | 472 | 1530-1532
Kunai | 473 | 1533-1535
Kama | 474 | 1536-1538
Chigiriki | 475 | 1539-1541
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
Maeri'het | 392 | 1274-1276
Telis'het | 393 | 1277-1279
Vareti'het | 394 | 1280-1282
Faes'mar | 3016
Selii'mar | 3017
Fetri'sei | 449 | 1461-1463
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
Holzst'nak 11-P | 450 | 1473-1475
Kru'urlin 89-P | 451 | 1464-1466
Lenmig'sraor 52-T | 452 | 1467-1469
Tyar'linhalf 67-G | 453 | 1470-1472
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
Earth Shaper | 396 | 1286-1288
Deep River | 397 | 1289-1291
Riptide | 398 | 1292-1294
Summer Leaf | 399 | 1295-1297
Autumn Leaf | 400 | 1298-1300
Winter Gale | 401 | 1301-1303
Strong Wind | 402 | 1304-1306
Tempest | 403 | 1307-1309
Derecho | 404 | 1310-1312
Hurricane | 405 | 1313-1315
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
Blizzard | 435 | 1419-1421

Kor Sestor

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
MPT 53 | 406 | 1316-1318
TF 71-L | 407 | 1319-1321
TF 78-O | 408 | 1322-1324
TF 109 | 409 | 1325-1327
FET 243 | 410 | 1328-1330
KIV 349 | 411 | 1331-1333
KIV 750 | 412 | 1334-1336
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

Kor Mereti

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Model 8 | 413 | 1337-1339
Model 16 | 414 | 1340-1342
Model 32 | 415 | 1343-1345
Model 64 | 416 | 1346-1348
Model 128 | 417 | 1349-1351
Model 256 | 418 | 1352-1354
Model 512 | 419 | 1355-1357
Model 1024 | 420 | 1358-1360
Minelayer | 1228 (submunition | 3228)
Slicer Turret | 1229 (Gun 2229)
Disruptor Turret | 1230 (Gun 2230)
Super Minelayer | 1233
Reasoning Node | 1304

Quarg

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Skylark | 421 | 1361-1363
Wardragon | 422 | 1364-1366
Empyrealdragon | 423 | 1367-1369
Elderdragon | 424 | 1370-1372
Battledrake | 3023
Nanotech Battery | 1234
Antimatter Core | 1235
Quantum Shield Generator | 1236
Small Graviton Thruster | 1237
Small Graviton Steering | 1238
Medium Graviton Thruster | 1239
Medium Graviton Steering | 1240
Large Graviton Thruster | 1241
Large Graviton Steering | 1242
Skylance | 1243
Quarg Antimissile | 1244

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

Pug

Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Zibruka | 426 | 1376-1378
Enfolta | 427 | 1379-1381
Maboro | 428 | 1382-1384
Arfecta | 429 | 1385-1387
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
Zubera | 431 | 1391-1393
Zubera Stats | 1280
Zambor | 3025
Zambor Stats | 1281
Zalgi | 3026
Zalgi Stats | 1282

Drak
Item Name | Item ID | Build IDs (if applicable)
--- | --- | ---
Void Sprite | 462 | 1476-1478
Void Sprite Infant | 463 | 1479-1481
Embershade | 464 | 1482-1484
Astral Cetacean | 465 | 1485-1487
Ember Waste Node | 454 | 1488-1490
Jje | 455 | 1491-1493
Ayym | 456 | 1494-1496
Embersylph | 457 | 1497-1499
Embersylph 2 | 458 | 1500-1502
Squid | 459 | 1503-1505
Boomerang | 460 | 1506-1508
Plankton | 461 | 1509-1511
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

Squid, Boomerang, Plankton, Jje -> Embersylph -> Void Sprite Infant, Embershade -> Void Sprite -> Ayym -> Astral Cetacean -> Ember Waste Node -> Archon

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
Component | 1376
Ship | 479
Build | 1561
Drone | 3034
Quest | 1049

Some outfits deviate from the "convert ES stats to EH stats as closely as possible, following the conversion conventions" rule. A list of them and differneces are listed below.

Item Name | Differences
--- | ---
Firestorm | -90% energy cost and energy storage
Firelight | -90% energy cost, +100% range, uses the torpedo/rocket equation
Heaver | -50% fire rate, energy cost = firing energy + firing fuel
Point defenses | 10x energy cost
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
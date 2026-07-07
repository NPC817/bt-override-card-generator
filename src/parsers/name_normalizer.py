from __future__ import annotations
import os
import re
from ..utils.paths import resource_path

_DATA_DIR = str(resource_path("data"))

# ── Direct name maps (exact string match) ────────────────────────────────────

_WEAPON_MAP: dict[str, str] = {
    # Autocannons
    "Autocannon/2": "ac2",   "AC/2": "ac2",
    "Autocannon/5": "ac5",   "AC/5": "ac5",
    "Autocannon/10": "ac10", "AC/10": "ac10",
    "Autocannon/20": "ac20", "AC/20": "ac20",
    # LB-X
    "LB 2-X AC": "lb2x", "LB 5-X AC": "lb5x",
    "LB 10-X AC": "lb10x", "LB 20-X AC": "lb20x",
    # Ultra AC
    "Ultra AC/2": "uac2", "Ultra AC/5": "uac5",
    "Ultra AC/10": "uac10", "Ultra AC/20": "uac20",
    # Rotary AC
    "Rotary AC/2": "rac2", "Rotary AC/5": "rac5",
    # Machine Guns
    "Machine Gun": "mg", "Light Machine Gun": "lmg", "Heavy Machine Gun": "hmg",
    # Gauss
    "Gauss Rifle": "gauss", "Light Gauss Rifle": "lgauss",
    "Heavy Gauss Rifle": "hgauss",
    # Lasers (IS)
    "Small Laser": "slas", "Medium Laser": "mlas", "Large Laser": "llas",
    "ER Small Laser": "erslas", "ER Medium Laser": "ermlas", "ER Large Laser": "erllas",
    "Small Pulse Laser": "splas", "Medium Pulse Laser": "mplas", "Large Pulse Laser": "lplas",
    # Clan lasers
    "CLSmall Laser": "cerslas",  "Clan Small Laser": "cerslas",
    "CLMedium Laser": "cermlas", "Clan Medium Laser": "cermlas",
    "CLLarge Laser": "cerllas",  "Clan Large Laser": "cerllas",
    "CLER Small Laser": "cerslas", "Clan ER Small Laser": "cerslas",
    "CLER Medium Laser": "cermlas","Clan ER Medium Laser": "cermlas",
    "CLER Large Laser": "cerllas", "Clan ER Large Laser": "cerllas",
    "CLSmall Pulse Laser": "csplas", "CLMedium Pulse Laser": "cmplas",
    "CLLarge Pulse Laser": "clplas",
    # PPC
    "PPC": "ppc", "ER PPC": "erppc", "Light PPC": "lppc",
    "Heavy PPC": "hppc", "Snub-Nose PPC": "snppc", "CLERPPC": "cerppc",
    # Missiles
    "SRM 2": "srm2", "SRM 4": "srm4", "SRM 6": "srm6",
    "Streak SRM 2": "ssrm2", "Streak SRM 4": "ssrm4", "Streak SRM 6": "ssrm6",
    "LRM 5": "lrm5", "LRM 10": "lrm10", "LRM 15": "lrm15", "LRM 20": "lrm20",
    "Streak LRM 5": "slrm5", "Streak LRM 10": "slrm10",
    "Streak LRM 15": "slrm15", "Streak LRM 20": "slrm20",
    "MRM 10": "mrm10", "MRM 20": "mrm20", "MRM 30": "mrm30", "MRM 40": "mrm40",
    # Flamers
    "Flamer": "flamer", "ER Flamer": "erflamer",
    # Melee
    "Hatchet": "hatchet", "Sword": "sword", "Mace": "mace",
    "Claws": "claws", "Lance": "lance",
    # Artillery
    "Long Tom": "longtom", "Sniper": "sniper", "Thumper": "thumper",
    # Rocket Launchers
    "Rocket Launcher 10": "rl10", "Rocket Launcher 15": "rl15", "Rocket Launcher 20": "rl20",
    # Thunderbolt
    "Thunderbolt 5": "tbolt5",  "Thunderbolt 10": "tbolt10",
    "Thunderbolt 15": "tbolt15", "Thunderbolt 20": "tbolt20",
    # HAG
    "HAG 20": "chag20", "HAG 30": "chag30", "HAG 40": "chag40",
    # Plasma
    "Plasma Rifle": "plasrifle",
    # HVAC
    "HV AC/2": "hvac2", "HV AC/5": "hvac5", "HV AC/10": "hvac10",
    # MML
    "MML 3": "mml3", "MML 5": "mml5", "MML 7": "mml7", "MML 9": "mml9",
    # NARC
    "Narc": "narc", "iNarc": "inarc",
    # ATM
    "ATM 3": "atm3", "ATM 6": "atm6", "ATM 9": "atm9", "ATM 12": "atm12",
    # LB-X clan
    "CLLB2XAC": "clb2x", "CLLB5XAC": "clb5x", "CLLB10XAC": "clb10x", "CLLB20XAC": "clb20x",
    # Clan Gauss
    "CLGauss Rifle": "cgauss", "CLAPGaussRifle": "capgauss",
    # Clan SRM/LRM
    "CLSRM2": "csrm2", "CLSRM4": "csrm4", "CLSRM6": "csrm6",
    "CLLRM5": "clrm5", "CLLRM10": "clrm10", "CLLRM15": "clrm15", "CLLRM20": "clrm20",
    # Clan Ultra AC
    "CLUltraAC2": "cuac2", "CLUltraAC5": "cuac5",
    "CLUltraAC10": "cuac10", "CLUltraAC20": "cuac20",
    # Clan Machine Guns
    "CLLightMG": "clmg", "CLMG": "cmg", "CLHeavyMG": "chmg",
    # Clan ER Pulse
    "CLERLargePulseLaser": "cerlplas", "CLERMediumPulseLaser": "cermplas",
    # Clan Heavy Lasers
    "CLHeavyMediumLaser": "chmlas", "CLHeavySmallLaser": "chslas",
    "CLHeavyLargeLaser": "chllas",
    # Clan Flamer
    "CLFlamer": "cflamer",
    # Clan Rotary
    "CLRotaryAC2": "crac2", "CLRotaryAC5": "crac5",
    # IS Enhanced/Extended LRMs
    "Enhanced LRM 5": "nlrm5",  "Enhanced LRM 10": "nlrm10",
    "Enhanced LRM 15": "nlrm15", "Enhanced LRM 20": "nlrm20",
    "Extended LRM 5": "elrm5",  "Extended LRM 10": "elrm10",
    "Extended LRM 15": "elrm15", "Extended LRM 20": "elrm20",
    # Torpedoes
    "SRT 2": "srt2", "SRT 4": "srt4", "SRT 6": "srt6",
    "LRT 5": "lrt5", "LRT 10": "lrt10", "LRT 15": "lrt15", "LRT 20": "lrt20",
    # IS Variable Speed Lasers
    "Large VSP Laser": "vslplas", "Medium VSP Laser": "vsmplas", "Small VSP Laser": "vssplas",
    # Clan Heavy Flamer
    "CLHeavyFlamer": "chflamer",
    # Clan Plasma Cannon
    "CLPlasmaCannon": "cplascannon",
    # Silver Bullet Gauss
    "Silver Bullet Gauss": "sbgauss",
    # IS Re-engineered Lasers
    "Large Re-engineered Laser": "rellas", "Medium Re-engineered Laser": "remlas",
    "Small Re-engineered Laser": "reslas",
    # Binary Laser
    "Binary Laser Cannon": "blazer",
    # MagShot
    "MagShot": "magshot",
    # LAC
    "Light AC/2": "lac2", "Light AC/5": "lac5",
    # Improved Heavy Gauss
    "Improved Heavy Gauss Rifle": "ihgauss",
    # ProtoMech AC (Clan)
    "CLProtoMechAC2": "cpmac2", "CLProtoMechAC4": "cpmac4", "CLProtoMechAC8": "cpmac8",
    # AP Gauss
    "AP Gauss Rifle": "capgauss",
    # Arrow IV
    "Arrow IV": "arrowiv",
    # Sniper/Thumper/Long Tom Cannon
    "Sniper Cannon": "snipercannon", "Thumper Cannon": "thumpercannon",
    "Long Tom Cannon": "longtomcannon",
    # Chemical Lasers (Clan)
    "CLLargeChemicalLaser": "cchemllas", "CLMediumChemicalLaser": "cchemmlas",
    "CLSmallChemicalLaser": "cchemslas",
    # Improved ATM
    "iATM 3": "ciatm3", "iATM 6": "ciatm6", "iATM 9": "ciatm9", "iATM 12": "ciatm12",
    # Improved Heavy Lasers (Clan)
    "CLImprovedHeavyLargeLaser": "cihllas", "CLImprovedHeavyMediumLaser": "cihmlas",
    "CLImprovedHeavySmallLaser": "cihslas",
    # Nail/Rivet
    "Nail Rivet Gun": "nailrivet",
    # TSEMP
    "TSEMP Cannon": "tsemp",
    # Clan ER Micro
    "CLERMicroLaser": "cermiclas",
    # Clan Micro Pulse
    "CLMicroPulseLaser": "cmicplas",
    # Clan Advanced SRM
    "CLAdvancedSRM2": "casrm2", "CLAdvancedSRM3": "casrm3",
    "CLAdvancedSRM4": "casrm4", "CLAdvancedSRM5": "casrm5", "CLAdvancedSRM6": "casrm6",
    # Equipment appearing in weapon slots
    "TAG": "tag", "Light TAG": "ltag", "Clan TAG": "tag",
    "Anti-Missile System": "ams", "AMS": "ams",
    "Laser AMS": "lams", "Laser Anti-Missile System": "lams",
    "M-Pod": "mpod",
    # Clan heavy laser text names
    "Heavy Medium Laser": "chmlas", "Heavy Large Laser": "chllas",
    "Heavy Small Laser": "chslas",
    "Improved Heavy Medium Laser": "cihmlas", "Improved Heavy Large Laser": "cihllas",
    "Improved Heavy Small Laser": "cihslas",
    # ER pulse / micro (bare names)
    "ER Micro Laser": "cermiclas",
    "ER Medium Pulse Laser": "cermplas", "ER Large Pulse Laser": "cerlplas",
    "ER Small Pulse Laser": "cersplas",
    # ProtoMech AC (bare names)
    "ProtoMech AC/2": "cpmac2", "ProtoMech AC/4": "cpmac4", "ProtoMech AC/8": "cpmac8",
    # Misc
    "Primitive Prototype PPC": "ppc",
    "TSEMP One-Shot": "tsemp",
    "Vehicle Flamer": "flamer",
    # Rocket launchers (short form)
    "RL 10": "rl10", "RL 15": "rl15", "RL 20": "rl20",
    "RL10": "rl10", "RL15": "rl15", "RL20": "rl20",
    # LB-X / Ultra / Rotary alternate formats
    "LB 2-X": "lb2x", "LB 5-X": "lb5x", "LB 10-X": "lb10x", "LB 20-X": "lb20x",
    "Ultra AC/2": "uac2", "Ultra AC/5": "uac5", "Ultra AC/10": "uac10", "Ultra AC/20": "uac20",
    "Rotary AC/2": "rac2", "Rotary AC/5": "rac5",
    # ATM alternate names
    "ATM 3": "catm3", "ATM 6": "catm6", "ATM 9": "catm9", "ATM 12": "catm12",
    # Clan SRM/LRM alternate
    "Clan SRM 2": "csrm2", "Clan SRM 4": "csrm4", "Clan SRM 6": "csrm6",
    "Clan LRM 5": "clrm5", "Clan LRM 10": "clrm10", "Clan LRM 15": "clrm15", "Clan LRM 20": "clrm20",
    # Clan streak
    "Clan Streak SRM 2": "cssrm2", "Clan Streak SRM 4": "cssrm4", "Clan Streak SRM 6": "cssrm6",
    "Clan Streak LRM 5": "cslrm5", "Clan Streak LRM 10": "cslrm10",
    "Clan Streak LRM 15": "cslrm15", "Clan Streak LRM 20": "cslrm20",
    # Nail Rivet Gun alternate
    "Nail Gun": "nailrivet", "Rivet Gun": "nailrivet",
    # Light auto cannon
    "Light Auto Cannon/2": "lac2", "Light Auto Cannon/5": "lac5",
    # Hyper velocity
    "Hyper Velocity Auto Cannon/2": "hvac2",
    "Hyper Velocity Auto Cannon/5": "hvac5",
    "Hyper Velocity Auto Cannon/10": "hvac10",
    # Silver Bullet
    "Silver Bullet Gauss Rifle": "sbgauss",
    # iATM alternate
    "iATM 3": "ciatm3", "iATM 6": "ciatm6", "iATM 9": "ciatm9", "iATM 12": "ciatm12",
    # Support weapons / misc vehicle weapons
    "Support Laser (Semi-Portable)": "slas",
    "Autocannon (Semi-Portable)": "ac2",
    "SRM Launcher (Light)": "srm2",
    # BA rocket launchers (plain compact forms from equipment sections)
    "RL1": "rl1", "RL 1": "rl1",
    "RL2": "rl2", "RL 2": "rl2",
    "RL3": "rl3", "RL 3": "rl3",
    "RL4": "rl4", "RL 4": "rl4",
    "RL5": "rl5", "RL 5": "rl5",
    # Primitive PPC/AC variants
    "PPCp": "ppc", "AC/2p": "ac2", "AC/5p": "ac5", "AC/10p": "ac10", "AC/20p": "ac20",
}

_EQUIPMENT_MAP: dict[str, str] = {
    "CASE": "case", "CASE II": "case2",
    "Anti-Missile System": "ams", "Laser Anti-Missile System": "lams",
    "Artemis IV FCS": "aiv", "Artemis V FCS": "av", "Apollo FCS": "apollo",
    "Beagle Active Probe": "probe", "Bloodhound Active Probe": "bhprobe",
    "Guardian ECM Suite": "ecm", "Angel ECM Suite": "aecm",
    "C3 Slave": "c3s", "C3 Master": "c3m",
    "TAG": "tag", "Light TAG": "ltag",
    "Targeting Computer": "tc",
    "Jump Jets": "jump", "Improved Jump Jets": "ijump",
    "MASC": "masc", "Supercharger": "supercharger",
    "Triple Strength Myomer": "tsm",
    "XL Engine": "xle", "Clan XL Engine": "cxle",
    "Light Engine": "lfe",
    "XXL Engine": "xxle", "Clan XXL Engine": "cxxle",
    "Stealth Armor": "stealth",
    "Laser-Reflective Armor": "lasrefl",
    "Reactive Armor": "reactive",
    "Ballistic-Reinforced Armor": "ballreinf",
    "Hardened Armor": "hardened",
    "Ferro-Lamellor Armor": "ferolam",
    "Composite Internal Structure": "composite",
    "Reinforced Internal Structure": "reinforced",
    "PPC Capacitor": "ppccapacitor",
    "Small Cockpit": "smcp", "Torso-Mounted Cockpit": "tmcp",
    "Coolant Pods": "cpod",
    "Anti-Personnel Pod": "apod", "Anti-BattleMech Pod": "bpod",
    "Anti-BattleArmor Pod": "mpod",
    "Partial Wing": "partwing",
    "Armored Components": "armcomp",
    "Heavy-Duty Gyro": "hdgyro",
    "CLActiveProbe": "cprobe", "Clan Active Probe": "cprobe",
    "CLLightProbe": "clprobe", "CLLightActiveProbe": "clprobe",
    "ISLightProbe": "lprobe", "Light Active Probe": "lprobe",
    "CLECM": "cecm", "CLECMSuite": "cecm", "Clan ECM Suite": "cecm",
    "CLAngelECM": "aecm", "CLAngelECMSuite": "aecm",
    "CLWatchdogECMSuite": "cews",
    "CLLaserAMS": "lams", "Clan Laser AMS": "lams",
    "CLLightTAG": "ltag", "C3 Boosted Master": "c3bm", "C3 Boosted Slave": "c3bs",
    "Improved C3 CPU": "c3i",
    "CLTAG": "tag", "Clan TAG": "tag",
    "CLSupercharger": "supercharger",
    "CLMASC": "masc", "Clan MASC": "masc",
    "CLTSM": "tsm", "Clan TSM": "tsm",
    "CLPartialWing": "partwing",
    "CLCoolantPod": "cpod",
    "CLPPCCapacitor": "ppccapacitor",
    "UMU": "umu", "CLUMU": "umu",
    "Mechanical Jump Booster": "mechjumpbooster",
    "CLMechanicalJumpBooster": "mechjumpbooster",
    "Quad Turret": "turret", "Head Turret": "turret", "Shoulder Turret": "turret",
    "TroopSpace": "troopspace",
    "CargoBay": "cargobay", "1stClassQuarters": "1stclassquarters",
    "2ndClassQuarters": "2ndclassquarters", "CrewQuarters": "crewquarters",
    "SteerageQuarters": "steeragequarters", "SmallCraftBay": "smallcraftbay",
    "DockingCollar": "dockingcollar", "MekBay": "mekbay",
    "ASFBay": "asfbay", "DropShuttleBay": "dropshuttlebay",
    "NavalRepairPressurized": "navalrepairpressurized",
    "NavalRepairUnpressurized": "navalrepairunpressurized",
    "InfantryBay": "infantrybay", "EjectionSeats": "ejectionseats",
    "ISBAFireResistantArmor": "bafireresist",
    "ISBAMimeticArmor": "bamimetic",
    "ISBAStealthArmor": "bastealth",
    "ISBAReactiveArmor": "bareactive",
    "ISBAReflectiveArmor": "bareflective",
    "CLArmoredMotiveSystem": "armmotivesys",
    # MegaMek internal vehicle/chassis equipment
    "VehicleJumpJet": "jump",
    "SponsonTurret": "turret", "PintleTurret": "turret",
    "BattleArmorHandles": "troopspace",
    "Advanced Fire Control": "tc",
    "Armored Chassis": "armcomp",
    "Hitch": "trailerhitch", "Tractor": "trailerhitch", "Trailer": "trailerhitch",
    "OmniChassisMod": "omni",
    "STOLChassisMod": "stol",
    "BicycleChassisMod": "bicycle",
    "MonocycleChassisMod": "monocycle",
    "AmphibiousChassis": "amphibious",
    "SubmersibleChassisMod": "submersible",
    "UltraLightChassisMod": "ultralight",
    "OffRoadChassis": "offroad",
    "ISOffRoadChassis": "offroad",
    "ISFullyAmphibiousChassis": "amphibious",
    "ISLimitedAmphibiousChassis": "amphibious",
    "ISVTOLJetBooster": "vtoljet",
    "IS Vehicular Stealth": "stealth",
    "ISVehicularMineDispenser": "minedispenser",
    "ISMineSweeper": "minesweeper",
    "Lift Hoist/Arresting Hoist": "lifthoist",
    "Manipulator [Non-Mech/Non-Battle Armor]": "manipulator",
    "RemoteSensorDispenser": "remotesensor",
    "Searchlight": "searchlight",
    "Communications Equipment": "comequip",
    "MASH Equipment": "mash",
    "ISTankCockpitCommandConsole": "cmdconsole",
    "ISLMGA": "lmga",
    "standardseats": "standardseats",
    "pillionseats": "pillionseats",
    "InfantryStandardSRM": "infantrysrm",
    # Missing equipment name forms
    "JumpBooster": "jumpbooster",
    "ISSponsonTurret": "turret",
    "CLVTOLJetBooster": "vtoljet",
    "ISOffRoad": "offroad",
    "ISMinesweeper": "minesweeper",
    "ISFlotationHull": "amphibious",
    "ClanLimitedAmphibiousChassis": "amphibious",
    "VSTOLChassisMod": "stol",
    "Manipulator": "manipulator",
    "Manipulator (Non-Mech/Non-Battle Armor)": "manipulator",
    "Clan Light TAG": "ltag",
    "SV Chassis Mod [Tractor]": "trailerhitch",
    "SV Chassis Mod [Trailer]": "trailerhitch",
    "Lift Hoist": "lifthoist",
    "HHSearchlight": "searchlight",
    "IS Reflective": "lasrefl",
    "Clan Reflective": "lasrefl",
    "Clan Ferro-Lamellor": "ferolam",
    "Clan AMS": "ams",
    "IS BattleArmor C3i": "c3i",
    "ISC3MasterBoostedSystemUnit": "c3bm",
    "CommsGear": "comequip",
}

# ── Ammo name prefixes ─────────────────────────────────────────────────────

_AMMO_PREFIXES: list[tuple[str, str, str]] = [
    ("IS Ammo AC/", "ammo", "AC"),           ("Clan Ammo AC/", "ammo", "AC"),
    ("IS Ammo LBX AC/", "ammo", "LBX"),      ("Clan Ammo LBX AC/", "ammo", "LBX"),
    ("IS Ammo Ultra AC/", "ammo", "UAC"),    ("Clan Ammo Ultra AC/", "ammo", "UAC"),
    ("IS Ultra AC/", "ammo", "UAC"),         ("Clan Ultra AC/", "ammo", "UAC"),
    ("IS Rotary AC/", "ammo", "RAC"),        ("ISRotaryAC", "ammo", "RAC"),
    ("IS Ammo LRM-", "ammo", "LRM"),         ("Clan Ammo LRM-", "ammo", "LRM"),
    ("ISLRM", "ammo", "LRM"),                ("CLLRM", "ammo", "LRM"),
    ("IS Ammo SRM-", "ammo", "SRM"),         ("Clan Ammo SRM-", "ammo", "SRM"),
    ("ISSRM", "ammo", "SRM"),                ("CLSRM", "ammo", "SRM"),
    ("IS Ammo Streak SRM-", "ammo", "SSRM"), ("Clan Ammo Streak SRM-", "ammo", "SSRM"),
    ("IS Streak SRM ", "ammo", "SSRM"),      ("Clan Streak SRM ", "ammo", "SSRM"),
    ("ISStreakSRM", "ammo", "SSRM"),         ("CLStreakSRM", "ammo", "SSRM"),
    ("IS Ammo Streak LRM-", "ammo", "SLRM"), ("Clan Streak LRM ", "ammo", "SLRM"),
    ("ISStreakLRM", "ammo", "SLRM"),         ("CLStreakLRM", "ammo", "SLRM"),
    ("BA-SRM", "ammo", "SRM"),
    ("IS Ammo MRM-", "ammo", "MRM"),
    ("IS Ammo Narc", "narc_ammo", "Narc"),
    ("IS Ammo Gauss Rifle", "gauss_ammo", "Gauss"), ("Clan Ammo Gauss", "gauss_ammo", "Gauss"),
    ("IS Gauss Ammo", "gauss_ammo", "Gauss"),       ("ISGauss Ammo", "gauss_ammo", "Gauss"),
    ("IS Light Gauss Ammo", "lgauss_ammo", "Gauss"), ("ISLightGauss Ammo", "lgauss_ammo", "Gauss"),
    ("Clan Gauss Ammo", "gauss_ammo", "Gauss"),
    ("IS Ammo MG", "mg_ammo", "MG"),             ("Clan Ammo MG", "mg_ammo", "MG"),
    ("IS Machine Gun Ammo", "mg_ammo", "MG"),    ("Clan Machine Gun Ammo", "mg_ammo", "MG"),
    ("ISMG Ammo", "mg_ammo", "MG"),
    ("IS Light Machine Gun Ammo", "lmg_ammo", "MG"), ("Clan Light Machine Gun Ammo", "lmg_ammo", "MG"),
    ("ISLightMG Ammo", "lmg_ammo", "MG"),
    ("IS Ammo Flamer", "flamer_ammo", "Flamer"),     ("IS Vehicle Flamer Ammo", "flamer_ammo", "Flamer"),
    ("Ammo Vehicle Flamer", "flamer_ammo", "Flamer"),
    ("IS Ammo Arrow IV", "arrowiv_ammo", "ArrowIV"),  ("ISArrowIV Ammo", "arrowiv_ammo", "ArrowIV"),
    ("IS Arrow IV Ammo", "arrowiv_ammo", "ArrowIV"),
    ("ISArrowIV Homing Ammo", "arrowiv_ammo", "ArrowIV"),
    ("IS Ammo Thunderbolt", "ammo", "TBolt"),
    ("IS Ammo ATM", "ammo", "ATM"),           ("Clan Ammo ATM", "ammo", "ATM"),
    ("CLATM", "ammo", "ATM"),
    ("IS Ammo LRT-", "ammo", "LRT"),          ("Clan Ammo LRT-", "ammo", "LRT"),
    ("IS Ammo SRT-", "ammo", "SRT"),          ("Clan Ammo SRT-", "ammo", "SRT"),
    ("IS Ammo SRTorpedo-", "ammo", "SRT"),    ("IS Ammo LRTorpedo-", "ammo", "LRT"),
    ("Clan Ammo LRTorpedo-", "ammo", "LRT"), ("Clan Ammo SRTorpedo-", "ammo", "SRT"),
    ("IS Ammo MML-", "ammo", "MML"),          ("Clan Ammo MML-", "ammo", "MML"),
    ("ISMML", "ammo", "MML"),
    ("IS Ammo iATM-", "ammo", "iATM"),        ("Clan Ammo iATM-", "ammo", "iATM"),
    ("IS Ammo ELRM-", "ammo", "ELRM"),
    ("IS Ammo HAG", "ammo", "HAG"),           ("Clan Ammo HAG", "ammo", "HAG"),
    ("CLHAG", "ammo", "HAG"),
    ("IS Ammo LAC/", "ammo", "AC"),           ("ISLAC", "ammo", "AC"),
    ("IS Ammo HVAC/", "ammo", "AC"),          ("ISHVAC", "ammo", "AC"),
    ("IS LB 10-X AC Ammo", "ammo", "LBX"),    ("IS LB 10-X Cluster Ammo", "ammo", "LBX"),
    ("IS LB 5-X AC Ammo", "ammo", "LBX"),     ("IS LB 5-X Cluster Ammo", "ammo", "LBX"),
    ("IS LB 20-X AC Ammo", "ammo", "LBX"),    ("IS LB 20-X Cluster Ammo", "ammo", "LBX"),
    ("Clan LB 10-X AC Ammo", "ammo", "LBX"),  ("Clan LB 10-X Cluster Ammo", "ammo", "LBX"),
    ("ISLBXAC10 Ammo", "ammo", "LBX"),        ("ISLBXAC10 CL Ammo", "ammo", "LBX"),
    ("ISAMS Ammo", "ams_ammo", "AMSAmmo"),
    ("IS AMS Ammo", "ams_ammo", "AMSAmmo"),
    ("CLAMS Ammo", "ams_ammo", "AMSAmmo"),
    ("ISMagshotGR Ammo", "gauss_ammo", "Gauss"),
    ("IS Ammo LAC/5", "ammo", "AC"),
    ("CLLongTomCannonAmmo", "artillery_ammo", "Artillery"),
    ("CLAPGaussRifle Ammo", "apgauss_ammo", "Gauss"),
    ("CLMediumChemLaserAmmo", "chemlaser_ammo", "ChemLaser"),
    ("IS Ammo ELRM-", "ammo", "ELRM"),
    ("IS Ammo Enhanced LRM-", "ammo", "LRM"),
    ("IS Ammo Extended LRM-", "ammo", "ELRM"),
    # Arrow IV (compact no-space forms)
    ("ISArrowIVAmmo", "arrowiv_ammo", "ArrowIV"),
    ("CLArrowIVAmmo", "arrowiv_ammo", "ArrowIV"),
    ("ISArrowIVHomingAmmo", "arrowiv_ammo", "ArrowIV"),
    ("CLArrowIVHomingAmmo", "arrowiv_ammo", "ArrowIV"),
    ("ISArrowIVClusterAmmo", "arrowiv_ammo", "ArrowIV"),
    ("CLArrowIV Homing Ammo", "arrowiv_ammo", "ArrowIV"),
    # Artillery (compact no-space forms)
    ("ISThumperAmmo", "artillery_ammo", "Artillery"),
    ("CLThumperAmmo", "artillery_ammo", "Artillery"),
    ("ISSniperAmmo", "artillery_ammo", "Artillery"),
    ("CLSniperAmmo", "artillery_ammo", "Artillery"),
    ("ISLongTomAmmo", "artillery_ammo", "Artillery"),
    ("ISLongTomCannonAmmo", "artillery_ammo", "Artillery"),
    ("ISThumperCannonAmmo", "artillery_ammo", "Artillery"),
    ("ISSniperCannonAmmo", "artillery_ammo", "Artillery"),
    ("ISBATubeArtilleryAmmo", "artillery_ammo", "Artillery"),
    ("ISArmorPiercingMortarAmmo", "artillery_ammo", "Artillery"),
    # HAG without IS/CL prefix
    ("HAG/", "ammo", "HAG"),
    ("Hyper-Assault Gauss", "ammo", "HAG"),
    # Plasma
    ("ISPlasmaRifleAmmo", "plasrifle_ammo", "PlasmaRifle"),
    ("CLPlasmaCannonAmmo", "plascannon_ammo", "PlasmaCannon"),
    # Silver Bullet Gauss
    ("Silver Bullet Gauss Ammo", "gauss_ammo", "Gauss"),
    # LBX CL Ammo variants
    ("ISLBXAC20 CL Ammo", "ammo", "LBX"),
    ("ISLBXAC10 CL Ammo", "ammo", "LBX"),
    ("ISLBXAC5 CL Ammo", "ammo", "LBX"),
    ("ISLBXAC2 CL Ammo", "ammo", "LBX"),
    ("CLLBXAC20 CL Ammo", "ammo", "LBX"),
    ("CLLBXAC10 CL Ammo", "ammo", "LBX"),
    ("CLLBXAC5 CL Ammo", "ammo", "LBX"),
    # Chem laser
    ("CLLargeChemLaserAmmo", "chemlaser_ammo", "ChemLaser"),
    # SRM/LRM without IS/CL prefix
    ("SRM1 Ammo", "ammo", "SRM"),
    ("SRM2 Ammo", "ammo", "SRM"),
    ("SRM3 Ammo", "ammo", "SRM"),
    ("SRM4 Ammo", "ammo", "SRM"),
    ("SRM5 Ammo", "ammo", "SRM"),
    ("SRM6 Ammo", "ammo", "SRM"),
    # Extended LRM (no-space compact form)
    ("ISExtended LRM", "ammo", "ELRM"),
    # Primitive AC ammo
    ("ISAC20p Ammo", "ammo", "AC"),
    ("ISAC10p Ammo", "ammo", "AC"),
    ("ISAC5p Ammo", "ammo", "AC"),
    ("ISAC2p Ammo", "ammo", "AC"),
    # Clan improved LRM ammo
    ("ClanImprovedLRM", "ammo", "LRM"),
    ("CLImpAmmoSRM", "ammo", "SRM"),
    # Cruise missile ammo
    ("ISCruiseMissile50Ammo", "ammo", "LRM"),
    # Light AC ammo (no IS prefix)
    ("Light AC/", "ammo", "AC"),
    # Taser ammo
    ("Taser Ammo", "ammo", "AC"),
    # Heavy flamer
    ("CL Heavy Flamer Ammo", "hflamer_ammo", "Flamer"),
    ("CLHeavyFlamer Ammo", "hflamer_ammo", "Flamer"),
]

# ── JS-style alias map (card_gen.js:14663-15337) ────────────────────────────

def _munge(name: str) -> str:
    """Strip parentheticals and non-word chars, lowercase — matches JS getCrit()."""
    return re.sub(r"[\W_]+", "", re.sub(r"\s*\([^)]*\)\s*", "", name)).lower()


_ALIAS_MAP: dict[str, str] = {
    # ── WeaponAlias (card_gen.js:14693) ──
    "isac2": "ac2", "isautocannon2": "ac2", "isac5": "ac5", "isautocannon5": "ac5",
    "isac10": "ac10", "isautocannon10": "ac10", "isac20": "ac20", "isautocannon20": "ac20",
    "islightgaussrifle": "lgauss", "islightgauss": "lgauss",
    "isgaussrifle": "gauss", "isgauss": "gauss",
    "isheavygaussrifle": "hgauss", "isheavygauss": "hgauss",
    "isimpheavygaussrifle": "ihgauss", "isimpheavygauss": "ihgauss",
    "isimprovedheavygaussrifle": "ihgauss", "isimprovedheavygauss": "ihgauss",
    "ismagshot": "magshot", "ismagshotgr": "magshot",
    "issbgr": "sbgauss", "issilverbulletgauss": "sbgauss", "issilverbulletgaussrifle": "sbgauss",
    "ishvac2": "hvac2", "ishypervelocityautocannon2": "hvac2",
    "ishvac5": "hvac5", "ishypervelocityautocannon5": "hvac5",
    "ishvac10": "hvac10", "ishypervelocityautocannon10": "hvac10",
    "islb2xac": "lb2x", "islb2x": "lb2x", "islbxac2": "lb2x",
    "islb5xac": "lb5x", "islb5x": "lb5x", "islbxac5": "lb5x",
    "islb10xac": "lb10x", "islb10x": "lb10x", "islbxac10": "lb10x",
    "islb20xac": "lb20x", "islb20x": "lb20x", "islbxac20": "lb20x",
    "islac2": "lac2", "islightac2": "lac2", "islightautocannon2": "lac2",
    "islac5": "lac5", "islightac5": "lac5", "islightautocannon5": "lac5",
    "islightmachinegun": "lmg", "islightmg": "lmg",
    "ismachinegun": "mg", "ismg": "mg",
    "isheavymachinegun": "hmg", "isheavymg": "hmg",
    "isnailrivet": "nailrivet", "isnailrivetgun": "nailrivet", "isnailgun": "nailrivet", "isrivetgun": "nailrivet",
    "isrotaryac2": "rac2", "isrotaryassaultcannon2": "rac2",
    "isrotaryac5": "rac5", "isrotaryassaultcannon5": "rac5",
    "isultraac2": "uac2", "isultraac5": "uac5", "isultraac10": "uac10", "isultraac20": "uac20",
    "iserlargelaser": "erllas", "isermediumlaser": "ermlas", "isersmalllaser": "erslas",
    "isflamer": "flamer", "isvehicleflamer": "flamer",
    "iserflamer": "erflamer", "isheavyflamer": "hflamer",
    "islargelaser": "llas", "ismediumlaser": "mlas", "issmalllaser": "slas",
    "isplasmarifle": "plasrifle",
    "islightppc": "lppc", "islppc": "lppc",
    "isppc": "ppc", "isparticlecannon": "ppc",
    "isheavyppc": "hppc", "ishppc": "hppc",
    "iserppc": "erppc",
    "issnubnoseppc": "snppc", "issnppc": "snppc", "issnubnosedppc": "snppc",
    "islargepulselaser": "lplas", "ispulselargelaser": "lplas",
    "ismediumpulselaser": "mplas", "ispulsemedlaser": "mplas",
    "issmallpulselaser": "splas", "ispulsesmalllaser": "splas",
    "islargexpulselaser": "lxplas", "isxpulselargelaser": "lxplas",
    "ismediumxpulselaser": "mxplas", "isxpulsemedlaser": "mxplas",
    "issmallxpulselaser": "sxplas", "isxpulsesmalllaser": "sxplas",
    "islargevsplaser": "vslplas", "islvspl": "vslplas",
    "islargevariablespeedlaser": "vslplas", "islargevsp": "vslplas",
    "ismediumvsplaser": "vsmplas", "ismvspl": "vsmplas",
    "ismediumvariablespeedlaser": "vsmplas", "ismediumvsp": "vsmplas",
    "issmallvsplaser": "vssplas", "issvspl": "vssplas",
    "issmallvariablespeedlaser": "vssplas", "issmallvsp": "vssplas",
    "islargereengineeredlaser": "rellas", "islargerelaser": "rellas",
    "ismediumreengineeredlaser": "remlas", "ismediumrelaser": "remlas",
    "issmallreengineeredlaser": "reslas", "issmallrelaser": "reslas",
    "isbinarylaserblazercannon": "blazer", "isbinarylasercannon": "blazer",
    "isblazer": "blazer", "isbinarylaser": "blazer", "isblazercannon": "blazer",
    "islrm5": "lrm5", "islrm10": "lrm10", "islrm15": "lrm15", "islrm20": "lrm20",
    "islrt5": "lrt5", "islrtorpedo5": "lrt5",
    "islrt10": "lrt10", "islrtorped10": "lrt10",
    "islrt15": "lrt15", "islrtorpedo15": "lrt15",
    "islrt20": "lrt20", "islrtorpedo20": "lrt20",
    "isenhancedlrm5": "nlrm5", "isenhancedlrm10": "nlrm10",
    "isenhancedlrm15": "nlrm15", "isenhancedlrm20": "nlrm20",
    "isextendedlrm5": "elrm5", "iselrm5": "elrm5",
    "isextendedlrm10": "elrm10", "iselrm10": "elrm10",
    "isextendedlrm15": "elrm15", "iselrm15": "elrm15",
    "isextendedlrm20": "elrm20", "iselrm20": "elrm20",
    "ismml3": "mml3", "ismml5": "mml5", "ismml7": "mml7", "ismml9": "mml9",
    "ismrm10": "mrm10", "ismrm20": "mrm20", "ismrm30": "mrm30", "ismrm40": "mrm40",
    "isnarc": "narc", "isnarcbeacon": "narc", "isnarcmissilebeacon": "narc",
    "isimprovednarc": "inarc", "isinarcbeacon": "inarc", "isinarcmissilebeacon": "inarc",
    "isrocketlauncher10": "rl10", "isrl10": "rl10", "isrlauncher10": "rl10",
    "isrocketlauncher15": "rl15", "isrl15": "rl15", "isrlauncher15": "rl15",
    "isrocketlauncher20": "rl20", "isrl20": "rl20", "isrlauncher20": "rl20",
    "issrm2": "srm2", "issrm4": "srm4", "issrm6": "srm6",
    "issrt2": "srt2", "issrtorpedo2": "srt2",
    "issrt4": "srt4", "issrtorpedo4": "srt4",
    "issrt6": "srt6", "issrtorpedo6": "srt6",
    "isstreaksrm2": "ssrm2", "isstreaksrm4": "ssrm4", "isstreaksrm6": "ssrm6",
    "isthunderbolt5": "tbolt5", "isthunderbolt10": "tbolt10",
    "isthunderbolt15": "tbolt15", "isthunderbolt20": "tbolt20",
    "isarrowiv": "arrowiv", "isarrowivsystem": "arrowiv", "isarrowivmissilesystem": "arrowiv",
    "islongtom": "longtom", "islongtomartillery": "longtom",
    "islongtomcannon": "longtomcannon", "islongtomartillerycannon": "longtomcannon",
    "issniper": "sniper", "issniperartillery": "sniper",
    "issnipercannon": "snipercannon", "issniperartillerycannon": "snipercannon",
    "isthumper": "thumper", "isthumperartillery": "thumper",
    "isthumpercannon": "thumpercannon", "isthumperartillerycannon": "thumpercannon",
    # Clan weapons
    "cllb2x": "clb2x", "cllb2xac": "clb2x", "cllbxac2": "clb2x",
    "cllb5x": "clb5x", "cllb5xac": "clb5x", "cllbxac5": "clb5x",
    "cllb10x": "clb10x", "cllb10xac": "clb10x", "cllbxac10": "clb10x",
    "cllb20x": "clb20x", "cllb20xac": "clb20x", "cllbxac20": "clb20x",
    "clapgaussrifle": "capgauss", "clapgauss": "capgauss",
    "clgaussrifle": "cgauss", "clgauss": "cgauss",
    "clhag20": "chag20", "clhyperassaultgaussrifle20": "chag20",
    "clhag30": "chag30", "clhyperassaultgaussrifle30": "chag30",
    "clhag40": "chag40", "clhyperassaultgaussrifle40": "chag40",
    "cllightmachinegun": "clmg", "cllightmg": "clmg",
    "clmachinegun": "cmg", "clmg": "cmg",
    "clheavymachinegun": "chmg", "clheavymg": "chmg",
    "clprotomechac2": "cpmac2", "clprotomechac4": "cpmac4", "clprotomechac8": "cpmac8",
    "clnailrivet": "cnailrivet", "clnailrivetgun": "cnailrivet",
    "clnailgun": "cnailrivet", "clrivetgun": "cnailrivet",
    "clrotaryac2": "crac2", "clrotaryassaultcannon2": "crac2",
    "clrotaryac5": "crac5", "clrotaryassaultcannon5": "crac5",
    "clultraac2": "cuac2", "clultraac5": "cuac5",
    "clultraac10": "cuac10", "clultraac20": "cuac20", "clanultraac20": "cuac20",
    "clerlargelaser": "cerllas", "clermediumlaser": "cermlas", "clersmalllaser": "cerslas",
    "clermicrolaser": "cermiclas",
    "clsmalllaser": "slas",
    "clflamer": "cflamer", "clvehicleflamer": "cflamer",
    "clerflamer": "cerflamer", "clheavyflamer": "chflamer",
    "clheavylargelaser": "chllas", "cllargeheavylaser": "chllas",
    "clheavymediumlaser": "chmlas", "clmediumheavylaser": "chmlas",
    "clheavysmalllaser": "chslas", "clsmallheavylaser": "chslas",
    "climpheavylargelaser": "cihllas", "climprovedheavylargelaser": "cihllas",
    "climprovedlargeheavylaser": "cihllas",
    "climpheavymediumlaser": "cihmlas", "climprovedheavymediumlaser": "cihmlas",
    "climprovedmediumheavylaser": "cihmlas",
    "climpheavysmalllaser": "cihslas", "climprovedheavysmalllaser": "cihslas",
    "climprovedsmallheavylaser": "cihslas",
    "clplasmacannon": "cplascannon",
    "clerppc": "cerppc",
    "cllargepulselaser": "clplas", "clpulselargelaser": "clplas",
    "clmediumpulselaser": "cmplas", "clpulsemedlaser": "cmplas",
    "clsmallpulselaser": "csplas", "clpulsesmalllaser": "csplas",
    "clmicropulselaser": "cmicplas",
    "clerlargepulselaser": "cerlplas", "clerpulselargelaser": "cerlplas",
    "clermediumpulselaser": "cermplas", "clerpulsemedlaser": "cermplas",
    "clerpulsemediumlaser": "cermplas",
    "clersmallpulselaser": "cersplas", "clerpulsesmalllaser": "cersplas",
    "cllargechemlaser": "cchemllas", "cllargechemicallaser": "cchemllas",
    "clmediumchemlaser": "cchemmlas", "clmediumchemicallaser": "cchemmlas",
    "clsmallchemlaser": "cchemslas", "clsmallchemicallaser": "cchemslas",
    "clatm3": "catm3", "clatm6": "catm6", "clatm9": "catm9", "clatm12": "catm12",
    "cliatm3": "ciatm3", "cliatm6": "ciatm6", "cliatm9": "ciatm9", "cliatm12": "ciatm12",
    "clnarc": "cnarc", "clnarcbeacon": "cnarc", "clnarcmissilebeacon": "cnarc",
    "cllrm5": "clrm5", "cllrm10": "clrm10", "cllrm15": "clrm15", "cllrm20": "clrm20",
    "cllrt5": "clrt5", "cllrtorpedo5": "clrt5",
    "cllrt10": "clrt10", "cllrtorpedo10": "clrt10",
    "cllrt15": "clrt15", "cllrtorpedo15": "clrt15",
    "cllrt20": "clrt20", "cllrtorpedo20": "clrt20",
    "clstreaklrm5": "cslrm5", "clstreaklrm10": "cslrm10",
    "clstreaklrm15": "cslrm15", "clstreaklrm20": "cslrm20",
    "clsrm2": "csrm2", "clsrm4": "csrm4", "clsrm6": "csrm6",
    "clsrt2": "csrt2", "clsrtorpedo2": "csrt2",
    "clsrt4": "csrt4", "clsrtorpedo4": "csrt4",
    "clsrt6": "csrt6", "clsrtorpedo6": "csrt6",
    "clstreaksrm2": "cssrm2", "clstreaksrm4": "cssrm4", "clstreaksrm6": "cssrm6",
    "clarrowiv": "carrowiv", "clarrowivsystem": "carrowiv", "clarrowivmissilesystem": "carrowiv",
    "cllongtom": "longtom", "cllongtomartillery": "longtom",
    "cllongtomcannon": "longtomcannon", "cllongtomartillerycannon": "longtomcannon",
    "clsniper": "sniper", "clsniperartillery": "sniper",
    "clsnipercannon": "snipercannon", "clsniperartillerycannon": "snipercannon",
    "clthumper": "thumper", "clthumperartillery": "thumper",
    "clthumpercannon": "thumpercannon", "clthumperartillerycannon": "thumpercannon",
    # Melee
    "ishatchet": "hatchet", "clhatchet": "hatchet",
    "issword": "sword", "clsword": "sword",
    "ismace": "mace", "clmace": "mace",
    "isflail": "flail", "clflail": "flail",
    "isclaw": "claws", "clclaw": "claws",
    "islance": "lance", "cllance": "lance",
    # BA weapons
    "isbalightmachinegun": "lmg", "isbalightmg": "lmg",
    "isbamachinegun": "mg", "isbamg": "mg",
    "isbaheavymachinegun": "hmg", "isbaheavymg": "hmg",
    "isbafiredrakeneedler": "firedrake", "isbafiredrakeincendiaryneedler": "firedrake",
    "isbadavidlightgaussrifle": "david", "isbakingdavidlightgaussrifle": "kdavid",
    "isbagrandmaulergausscannon": "gmauler", "isbagrandmauler": "gmauler",
    "isbamagshot": "magshot", "isbamagshotgr": "magshot",
    "isbatsunamiheavygaussrifle": "tsunami",
    "isbamicrogrenadelauncher": "mgrenade",
    "isbagrenadelauncher": "hgrenade", "isbaheavygrenadelauncher": "hgrenade",
    "isbaheavygl": "hgrenade", "isbaheavybagrenadelauncher": "hgrenade",
    "isbaautogl": "hgrenade",
    "isbalightmortar": "lmortar", "isbaheavymortar": "hmortar",
    "isbalightrecoillessrifle": "lrecoil", "islightrecoillessrifle": "lrecoil",
    "isbamediumrecoillessrifle": "mrecoil", "ismediumrecoillessrifle": "mrecoil",
    "isbaheavyrecoillessrifle": "hrecoil", "isheavyrecoillessrifle": "hrecoil",
    "isbamediumlaser": "mlas", "isbasmalllaser": "slas",
    "isbaermediumlaser": "ermlas", "isbaersmalllaser": "erslas",
    "isbamediumpulselaser": "mplas", "isbapulsemedlaser": "mplas",
    "isbasmallpulselaser": "splas", "isbapulsesmalllaser": "splas",
    "isbaflamer": "flamer", "isbaheavyflamer": "hflamer",
    "isbaplasmarifle": "mpplasrifle",
    "isbasupportppc": "sppc",
    "isbacompactnarc": "compactnarc",
    "isbalrm1": "lrm1", "isbalrm2": "lrm2", "isbalrm3": "lrm3",
    "isbalrm4": "lrm4", "isbalrm5": "lrm5",
    "isbamrm1": "mrm1", "isbamrm2": "mrm2", "isbamrm3": "mrm3",
    "isbamrm4": "mrm4", "isbamrm5": "mrm5",
    "isbarl1": "rl1", "isbarlauncher1": "rl1", "isbarocketlauncher1": "rl1",
    "isbarl2": "rl2", "isbarlauncher2": "rl2", "isbarocketlauncher2": "rl2",
    "isbarl3": "rl3", "isbarlauncher3": "rl3", "isbarocketlauncher3": "rl3",
    "isbarl4": "rl4", "isbarlauncher4": "rl4", "isbarocketlauncher4": "rl4",
    "isbarl5": "rl5", "isbarlauncher5": "rl5", "isbarocketlauncher5": "rl5",
    "isbasrm1": "srm1", "isbasrm2": "srm2", "isbasrm3": "srm3",
    "isbasrm4": "srm4", "isbasrm5": "srm5", "isbasrm6": "srm6",
    "isbaminelauncher": "popmine", "isbataser": "taser",
    "isbamediumvsplaser": "vsmplas", "isbamvspl": "vsmplas",
    "isbamediumvariablespeedlaser": "vsmplas", "isbamediumvsp": "vsmplas",
    "isbasmallvsplaser": "vssplas", "isbasvspl": "vssplas",
    "isbasmallvariablespeedlaser": "vssplas", "isbasmallvsp": "vssplas",
    # Clan BA weapons
    "clbaapgaussrifle": "capgauss", "clbaapgauss": "capgauss",
    "clbalbx": "clbx", "clbearhuntersuperheavyac": "bearhunt",
    "clbabearhuntersuperheavyac": "bearhunt",
    "clbalightmachinegun": "clmg", "clbalightmg": "clmg",
    "clbamachinegun": "cmg", "clbamg": "cmg",
    "clbaheavymachinegun": "chmg", "clbaheavymg": "chmg",
    "clbamicrogrenadelauncher": "mgrenade",
    "clbagrenadelauncher": "hgrenade", "clbaheavygrenadelauncher": "hgrenade",
    "clbaheavygl": "hgrenade", "clbaheavybagrenadelauncher": "hgrenade",
    "clbaautogl": "hgrenade",
    "clbalightmortar": "lmortar", "clbaheavymortar": "hmortar",
    "clbalightrecoillessrifle": "lrecoil", "cllightrecoillessrifle": "lrecoil",
    "clbamediumrecoillessrifle": "mrecoil", "clmediumrecoillessrifle": "mrecoil",
    "clbaheavyrecoillessrifle": "hrecoil", "clheavyrecoillessrifle": "hrecoil",
    "clbamediumlaser": "cermlas", "clbaermediumlaser": "cermlas",
    "clbasmalllaser": "slas", "clbaersmalllaser": "cerslas",
    "clbaermicrolaser": "cermiclas",
    "clbamediumpulselaser": "cmplas", "clbapulsemedlaser": "cmplas",
    "clbasmallpulselaser": "csplas", "clbapulsesmalllaser": "csplas",
    "clbamicropulselaser": "cmicplas",
    "clbaermediumpulselaser": "cermplas", "clbaerpulsemedlaser": "cermplas",
    "clbaerpulsemediumlaser": "cermplas",
    "clbaersmallpulselaser": "cersplas", "clbaerpulsesmalllaser": "cersplas",
    "clbaheavymediumlaser": "chmlas", "clbamediumheavylaser": "chmlas",
    "clbaheavysmalllaser": "chslas", "clbasmallheavylaser": "chslas",
    "clbaflamer": "cflamer", "clbaheavyflamer": "chflamer",
    "clbasupportppc": "csppc", "clbacompactnarc": "compactnarc",
    "clbalrm1": "clrm1", "clbalrm2": "clrm2", "clbalrm3": "clrm3",
    "clbalrm4": "clrm4", "clbalrm5": "clrm5",
    "clbasrm1": "csrm1", "clbasrm2": "csrm2", "clbasrm3": "csrm3",
    "clbasrm4": "csrm4", "clbasrm5": "csrm5", "clbasrm6": "csrm6",
    "clbaadvancedsrm1": "casrm1", "clbaadvancedsrm2": "casrm2",
    "clbaadvancedsrm3": "casrm3", "clbaadvancedsrm4": "casrm4",
    "clbaadvancedsrm5": "casrm5", "clbaadvancedsrm6": "casrm6",
    "cladvancedsrm1": "casrm1", "cladvancedsrm2": "casrm2",
    "cladvancedsrm3": "casrm3", "cladvancedsrm4": "casrm4",
    "clanadvancedsrm1": "casrm1", "clanadvancedsrm2": "casrm2",
    "clanadvancedsrm3": "casrm3", "clanadvancedsrm4": "casrm4",
    "clanadvancedsrm5": "casrm5", "clanadvancedsrm6": "casrm6",
    "isbaadvancedsrm1": "casrm1", "isbaadvancedsrm2": "casrm2",
    "isbaadvancedsrm3": "casrm3", "isbaadvancedsrm4": "casrm4",
    "isbaadvancedsrm5": "casrm5", "isbaadvancedsrm6": "casrm6",
    "isadvancedsrm1": "casrm1", "isadvancedsrm2": "casrm2",
    "isadvancedsrm3": "casrm3", "isadvancedsrm4": "casrm4",
    "isadvancedsrm5": "casrm5", "isadvancedsrm6": "casrm6",
    "cladvancedsrm5": "casrm5", "cladvancedsrm6": "casrm6",
    "clbamicrobomb": "cbombrack",

    # ── EquipmentAlias (card_gen.js:15204) ──
    "isantipersonnelpod": "apod", "clantipersonnelpod": "apod",
    "isapod": "apod", "clapod": "apod",
    "isbpod": "bpod", "clbpod": "bpod",
    "ismpod": "mpod", "clmpod": "mpod",
    "isams": "ams", "clams": "ams",
    "isantimissilesystem": "ams", "clantimissilesystem": "ams", "clantimissilesys": "ams",
    "cllaserantimissilesys": "lams",
    "islaserams": "lams", "cllaserams": "lams",
    "islaserantimissilesystem": "lams", "cllaserantimissilesystem": "lams",
    "isartemisiv": "aiv", "clartemisiv": "aiv",
    "clartemisv": "av", "isartemisv": "av",
    "isapollo": "apollo", "isaes": "aes",
    "isbeagleactiveprobe": "probe", "isbloodhoundactiveprobe": "bhprobe",
    "clactiveprobe": "cprobe",
    "islightprobe": "lprobe", "islightactiveprobe": "lprobe",
    "cllightprobe": "clprobe", "cllightactiveprobe": "clprobe",
    "isc3mastercomputer": "c3m", "isc3masterunit": "c3m", "isc3master": "c3m",
    "isc3slavecomputer": "c3s", "isc3slaveunit": "c3s", "isc3slave": "c3s",
    "isc3masterboosteddystemunit": "c3bm",
    "isc3boostedsystemslave": "c3bs", "isc3boostedsystemslaveunit": "c3bs",
    "isc3iunit": "c3i", "isimprovedc3cpu": "c3i", "isc3icomputer": "c3i",
    "iscase": "case", "clcase": "case",
    "iscaseii": "case2", "clcaseii": "case2",
    "isecm": "ecm", "clecm": "cecm",
    "isguardianecmsuite": "ecm", "isguardianecm": "ecm", "isecmsuite": "ecm",
    "clecmsuite": "cecm",
    "isangelecmsuite": "aecm", "clangelecmsuite": "aecm",
    "isangelecm": "aecm", "clangelecm": "aecm",
    "isjumpjet": "jump", "cljumpjet": "jump",
    "improvedjumpjet": "ijump", "isimprovedjumpjet": "ijump", "climprovedjumpjet": "ijump",
    "ismasc": "masc", "clmasc": "masc",
    "istag": "tag", "cltag": "tag",
    "islighttag": "ltag", "cllighttag": "ltag",
    "istargetingcomputer": "tc", "cltargetingcomputer": "tc",
    "istsm": "tsm", "cltsm": "tsm",
    "istriplestrengthmyomer": "tsm", "cltriplestrengthmyomer": "tsm",
    "issupercharger": "supercharger", "clsupercharger": "supercharger",
    "clwatchdogecmsuite": "cews",
    "heavydutygyro": "hdgyro",
    "ispartialwing": "partwing", "clpartialwing": "partwing",
    "iscoolantpod": "cpod", "clcoolantpod": "cpod",
    "isppccapacitor": "ppccapacitor", "clppccapacitor": "ppccapacitor",
    "smallcockpit": "smcp", "torsomountedcockpit": "tmcp",
    "isumu": "umu", "clumu": "umu",
    "ismechanicaljumpbooster": "mechjumpbooster", "clmechanicaljumpbooster": "mechjumpbooster",
    "isquadturret": "turret", "clquadturret": "turret",
    "isheadturret": "turret", "clheadturret": "turret",
    "isshoulderturret": "turret", "clshoulderturret": "turret",
    "troopspace": "troopspace",
    "cargobay": "cargobay", "1stclassquarters": "1stclassquarters",
    "2ndclassquarters": "2ndclassquarters", "crewquarters": "crewquarters",
    "steeragequarters": "steeragequarters", "smallcraftbay": "smallcraftbay",
    "dockingcollar": "dockingcollar", "mekbay": "mekbay",
    "asfbay": "asfbay", "dropshuttlebay": "dropshuttlebay",
    "navalrepairpressurized": "navalrepairpressurized",
    "navalrepairunpressurized": "navalrepairunpressurized",
    "infantrybay": "infantrybay", "ejectionseats": "ejectionseats",
    "isbaturret": "turret", "clbaturret": "turret",
    "isdetachableweaponpack": "dwp", "cldetachableweaponpack": "dwp",
    "isbajumpbooster": "jumpbooster", "clbajumpbooster": "jumpbooster",
    "isbamechanicaljumpbooster": "jumpbooster", "clbamechanicaljumpbooster": "jumpbooster",
    "isbapartialwing": "partwing", "clbapartialwing": "partwing",
    "isbalprobe": "lprobe", "clbalprobe": "lprobe",
    "isbalighttag": "ltag", "clbalighttag": "ltag",
    "isbaapds": "apds", "clbaapds": "apds",
    "clarmoredmotivesystem": "armmotivesys",
    "clbamyomerbooster": "myomerboost", "clbamb": "myomerboost",
    "isbaecm": "ecm", "clbaecm": "cecm",
    "isbaguardianecmsuite": "ecm", "isbaguardianecm": "ecm", "isbaecmsuite": "ecm",
    "clbaecmsuite": "cecm",
    "isbaangelecmsuite": "aecm", "clbaangelecmsuite": "aecm",
    "isbaangelecm": "aecm", "clbaangelecm": "aecm",
    "isbasinglehexecm": "ecm", "clbasinglehexecm": "cecm",
    "isbac3": "c3s", "isbc3": "c3s",
    "isbac3i": "c3i", "isbc3i": "c3i",
    # BA armor variants
    "isbamimetic": "bamimetic",
    "isbastealth": "bastealth",
    "isbareflective": "bareflective",
    "isbareactive": "bareactive",
    "isbafireresistant": "bafireresist",
    # Clan BA armor variants (spaced MegaMek names)
    "clanbareactive": "bareactive", "clanbafireresistant": "bafireresist",
    "clanbastealthstandard": "bastealth", "clanbastealth": "bastealth",
    "clbamimetic": "bamimetic", "clbareflective": "bareflective",
    "clbareactive": "bareactive", "clbafireresistant": "bafireresist",
    "clbastealth": "bastealth",
    # Clan BA equipment (clba prefix)
    "clbaspaceoperationsadaptation": "spaceopsadaptation",
    "clbaextendedlifesupport": "extendedlifesupport",
    # BA weapons with OS suffix
    "isbasrm4os": "srm4",
    # BA equipment remappings
    "babasicmanipulator": "manipulator", "basicmanipulator": "manipulator",
    "baarmoredglove": "armoredglove", "armoredglove": "armoredglove",
    "babattleclaw": "battleclaw", "battleclaw": "battleclaw",
    "baheavybattleclaw": "heavybattleclaw", "heavybattleclaw": "heavybattleclaw",
    "babattleclawvibro": "vibrobattleclaw",
    "basalvagearm": "salvagearm", "salvagearm": "salvagearm",
    "baapmount": "apmount", "apmount": "apmount",
    "bacargolifter": "cargolifter", "cargolifter": "cargolifter",
    "bcuttingtorch": "cuttingtorch", "bascuttingtorch": "cuttingtorch",
    "cuttingtorch": "cuttingtorch",
    "isbaextendedlifesupport": "extendedlifesupport", "extendedlifesupport": "extendedlifesupport",
    "isbaspaceoperationsadaptation": "spaceopsadaptation", "spaceopsadaptation": "spaceopsadaptation",
    "isbaimprovedsensors": "improvedsensors", "isimprovedsensors": "improvedsensors",
    "improvedsensors": "improvedsensors",
    "missionequipmentstorage": "missionequipment",
    "bamissionequipmentstorage": "missionequipment",
    # Remaining BA
    "isbaremotesensordispenser": "remotesensor",
    "basearchlight": "searchlight",
    "bacuttingtorch": "cuttingtorch", "bcuttingtorch": "cuttingtorch",
    "camosystem": "camosystem",
    # BA weapons — stripped BA prefix forms
    "davidlightgaussrifle": "david",
    "minelauncher": "popmine", "baminelauncher": "popmine",
    # BA claws — vibro variants
    "battleclawvibro": "vibrobattleclaw",
    "heavybattleclawvibro": "vibrobattleclaw", "baheavybattleclawvibro": "vibrobattleclaw",
    # BA C3 / sensor aliases
    "battlearmorc3": "c3s",
    "isbaheatsensor": "improvedsensors", "baheatsensor": "improvedsensors", "heatsensor": "improvedsensors",
    # Clan BA armor (spaced name forms after parenthetical strip)
    "clanbalaserreflective": "bareflective",
    "clanbalaserfireresistant": "bafireresist",
    # BA Magnetic Clamp variants
    "bamagneticclamp": "magclamp", "magneticclamp": "magclamp",
    "battleclawmagnets": "magclamp",
    # HarJel
    "baharjel": "harjel", "harjel": "harjel",
    # BA LB-X AC (IS variant)
    "battlearmorlbxac": "balb2",

    # ── Transporter name normalization (lowercase BLK forms) ─────────────────
    "liquidcargobay": "cargobay",
    "insulatedcargobay": "cargobay",
    "refrigeratedcargobay": "cargobay",
    "lightvehiclebay": "cargobay",
    "livestockcargobay": "cargobay",
    "battlearmorbay": "infantrybay",

    # ── Clan BA Laser Reflective — double-r: "laser" + "reflective" ─────────
    # _munge("Clan BA Laser Reflective") = "clanbalaserreflective"
    "clanbalaserreflective": "bareflective",

    # ── Missing equipment name aliases ────────────────────────────────────────
    "jumpbooster": "jumpbooster",
    "isarmoredmotivesystem": "armmotivesys",
    "clanams": "ams",
    "svchassismod": "trailerhitch",
    "hhsearchlight": "searchlight",
    "lifthoist": "lifthoist",
    "c3computer": "c3m",
    "c3boostedsystem": "c3bm",
    "c3masterwithtag": "c3m",
    "c3masterboostedwithtag": "c3bm",
    "clanlighttag": "ltag",
    "clanbamachinegun": "cmg",
    "clanbalightmachinegun": "clmg",
    "isapds": "apds",
    "clanferrolamellor": "ferolam",
    "isreflective": "lasrefl",
    "clanreflective": "lasrefl",
    "commsgear": "comequip",
    "isc3sensors": "c3s",
    "isbaactiveprobe": "lprobe",
    "clbaimprovedsensors": "improvedsensors",
    "isbattlearmorc3i": "c3i",
    "novacews": "cews",
    "isc3masterboostedsystemunit": "c3bm",
    "clanlimitedamphibiouschassis": "amphibious",
    "isflotationhull": "amphibious",
    "vstolchassismod": "stol",

    # ── Inferno/One-Shot SRM variants (after BA parser strips OS → I suffix) ─
    "issrm2ios": "srm2", "issrm2i": "srm2", "issrm2os": "srm2",
    "issrm4ios": "srm4", "issrm4i": "srm4", "issrm4os": "srm4",
    "issrm6ios": "srm6", "issrm6i": "srm6", "issrm6os": "srm6",
    "clsrm2ios": "csrm2", "clsrm2i": "csrm2", "clsrm2os": "csrm2",
    "clsrm4ios": "csrm4", "clsrm4i": "csrm4", "clsrm4os": "csrm4",
    "clsrm6ios": "csrm6", "clsrm6i": "csrm6", "clsrm6os": "csrm6",
}


def _strip_parens(name: str) -> str:
    """Remove parenthetical groups: 'SRM 2 (I-OS)' → 'SRM 2'."""
    return re.sub(r"\s*\([^)]*\)\s*", " ", name).strip()


def _clean_name(name: str) -> str:
    """Strip common MegaMek suffixes/prefixes that block lookup.
    Handles: leading quantity, :OMNI, (ST), (PT), :SIZE:..., - troopers, - Half, [Non-Mech/...]."""
    name = re.sub(r"^\d+\s*", "", name)                     # "1 ISMediumLaser" → "ISMediumLaser"
    name = re.sub(r":OMNI\b", "", name, flags=re.IGNORECASE)  # ":OMNI"
    name = re.sub(r"\s*\(ST\)", "", name)                    # "Machine Gun(ST)" → "Machine Gun"
    name = re.sub(r"\s*\(PT\)", "", name)                    # "Machine Gun(PT)" → "Machine Gun"
    name = re.sub(r":SIZE:[\d.]+", "", name)                # "InfantryStandardSRM:SIZE:1.0"
    name = re.sub(r"IOS$", "", name)                        # "ISSRM2IOS" → "ISSRM2" (inferno one-shot)
    name = re.sub(r":\d+$", "", name)                       # "CommsGear:1" → "CommsGear"
    name = re.sub(r"\s*-+\s*(troopers|Half).*", "", name, flags=re.IGNORECASE)
    name = re.sub(r"\s*\[[^\]]*\]\s*", " ", name)           # [Non-Mech/...]
    name = re.sub(r"\s+", " ", name).strip()
    return name


def _lookup_alias(name: str) -> str | None:
    """Try JS-style alias lookup: munge the name and search _ALIAS_MAP."""
    key = _munge(name)
    if key in _ALIAS_MAP:
        return _ALIAS_MAP[key]
    # Try stripping known tech prefixes (cl, is)
    if key.startswith("cl") and key[2:] in _ALIAS_MAP:
        return _ALIAS_MAP[key[2:]]
    if key.startswith("is") and key[2:] in _ALIAS_MAP:
        return _ALIAS_MAP[key[2:]]
    # Try ADDING tech prefixes (for bare names like "Heavy Medium Laser")
    for prefix in ("cl", "is"):
        prefixed = prefix + key
        if prefixed in _ALIAS_MAP:
            return _ALIAS_MAP[prefixed]
    return None


def _normalize_name(name: str, direct_map: dict[str, str],
                    extra_valid_keys: set[str] | None = None) -> str | None:
    """Core lookup: direct → strip-parens-direct → strip-suffixes-direct → alias."""
    if not name:
        return None
    # 1. Direct lookup
    if name in direct_map:
        return direct_map[name]
    # 2. Strip parentheticals, retry direct
    stripped = _strip_parens(name)
    if stripped != name and stripped in direct_map:
        return direct_map[stripped]
    # 3. Clean suffixes, retry direct
    cleaned = _clean_name(name)
    if cleaned != name and cleaned in direct_map:
        return direct_map[cleaned]
    # 4. Both strip + clean, retry direct
    if stripped != name:
        cleaned_stripped = _clean_name(stripped)
        if cleaned_stripped != stripped and cleaned_stripped in direct_map:
            return direct_map[cleaned_stripped]
    # 5. Alias fallback — try cleaned forms first (munge doesn't strip digits/suffixes)
    valid_keys = set(direct_map.values())
    if extra_valid_keys:
        valid_keys |= extra_valid_keys
    for alias_candidate in (cleaned, stripped, name):
        result = _lookup_alias(alias_candidate)
        if result and result in valid_keys:
            return result
    return None


# Lazy-loaded YAML keys for alias validation
_WEAPON_YAML_KEYS: set[str] | None = None
_EQUIPMENT_YAML_KEYS: set[str] | None = None


def _load_yaml_keys(path: str) -> set[str]:
    import yaml
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return {k for k in data if isinstance(data[k], dict)}


def normalize_weapon(megamek_name: str) -> str | None:
    """Return the weapons.yaml key for a MegaMek weapon name, or None if unknown."""
    global _WEAPON_YAML_KEYS
    if _WEAPON_YAML_KEYS is None:
        _WEAPON_YAML_KEYS = _load_yaml_keys(os.path.join(_DATA_DIR, "weapons.yaml"))
    name = megamek_name.strip()
    result = _normalize_name(name, _WEAPON_MAP, extra_valid_keys=_WEAPON_YAML_KEYS)
    if result:
        return result
    # 6. Fall back to equipment map (TAG, AMS, etc. in weapon slots)
    return _normalize_name(name, _EQUIPMENT_MAP)


def normalize_equipment(megamek_name: str) -> str | None:
    """Return the equipment.yaml key for a MegaMek equipment name, or None if unknown."""
    global _EQUIPMENT_YAML_KEYS
    if _EQUIPMENT_YAML_KEYS is None:
        _EQUIPMENT_YAML_KEYS = _load_yaml_keys(os.path.join(_DATA_DIR, "equipment.yaml"))
    name = megamek_name.strip()
    return _normalize_name(name, _EQUIPMENT_MAP, extra_valid_keys=_EQUIPMENT_YAML_KEYS)


# Ammo regex patterns: (regex, eq_key, subtype)
_AMMO_REGEXES: list[tuple[str, str, str]] = [
    # "BA-Advanced SRM-2 Ammo", "BA-SRM5 Ammo"
    (r"BA[- ](?:Advanced\s+)?(\S+?)\s+Ammo\b", "ammo", None),
    # "IS LRM 20 Ammo", "IS LRM 20 Ammo Artemis-capable"
    (r"(?:IS|Clan)\s+(.+?)\s+Ammo\b", "ammo", None),
    # "ISLRM20 Ammo Artemis-capable", "CLATM9 ER Ammo", "CLHAG30 Ammo"
    (r"(?:IS|CL|Clan)([A-Za-z]+\d*)\s+Ammo\b", "ammo", None),
    # "Ammo Vehicle Flamer" (reversed)
    (r"Ammo\s+(?:IS|Clan)?\s*(.+)$", "ammo", None),
]

# Map raw caliber strings to subtype names
_CALIBER_TO_SUBTYPE: dict[str, str] = {
    "ac": "AC", "lbx": "LBX", "uac": "UAC", "rac": "RAC",
    "lrm": "LRM", "clrm": "LRM", "srm": "SRM", "csrm": "SRM",
    "ssrm": "SSRM", "slrm": "SLRM", "mrm": "MRM",
    "mml": "MML", "lrt": "LRT", "srt": "SRT",
    "hag": "HAG", "atm": "ATM", "iatm": "iATM",
    "gauss": "Gauss", "mg": "MG", "flamer": "Flamer",
    "arrowiv": "ArrowIV", "narc": "Narc", "tbolt": "TBolt",
    "elrm": "ELRM", "nlrm": "LRM",
    "lac": "AC", "hvac": "AC",
    "ams": "AMSAmmo", "magshot": "Gauss",
    "longtomcannon": "Artillery", "snipercannon": "Artillery",
    "thumpercannon": "Artillery", "longtom": "Artillery",
    "sniper": "Artillery", "thumper": "Artillery",
    "apgauss": "Gauss", "chemLaser": "ChemLaser",
    "chemMediumLaser": "ChemLaser",
}


def _resolve_ammo_subtype(raw: str) -> str | None:
    """Extract a known ammo subtype from a raw caliber string."""
    cleaned = _munge(raw)
    # Try stripping leading cl/is
    for prefix in ("cl", "is"):
        if cleaned.startswith(prefix):
            base = cleaned[len(prefix):]
            if base in _CALIBER_TO_SUBTYPE:
                return _CALIBER_TO_SUBTYPE[base]
    if cleaned in _CALIBER_TO_SUBTYPE:
        return _CALIBER_TO_SUBTYPE[cleaned]
    # Try to match known suffixes
    for key in sorted(_CALIBER_TO_SUBTYPE, key=lambda k: -len(k)):
        if cleaned.endswith(key):
            return _CALIBER_TO_SUBTYPE[key]
    return None


_AMMO_EXACT: dict[str, tuple[str, str]] = {
    "ISNarc Pods": ("ammo", "Narc"),
    "ISiNarc Pods": ("ammo", "Narc"),
    "CLNarc Pods": ("ammo", "Narc"),
}


def _extract_ammo_variant(subtype: str, name: str, prefix: str) -> str | None:
    """Extract a weapon-size digit from an ammo name after prefix match.

    Returns e.g. "20", "10", "6" or None if no size digit found.
    """
    # Try the remainder after the prefix
    if name.startswith(prefix):
        remainder = name[len(prefix):].strip()
    else:
        cleaned = _clean_name(name)
        if cleaned.startswith(prefix):
            remainder = cleaned[len(prefix):].strip()
        else:
            remainder = ""
    # Search for digits in the remainder
    m = re.search(r'(\d+)', remainder)
    if m:
        return m.group(1)
    # Search for digits in the prefix itself (handles "SRM6 Ammo" style)
    m = re.search(r'(\d+)', prefix)
    if m:
        return m.group(1)
    return None


def normalize_ammo(megamek_name: str) -> tuple[str, str] | None:
    """Return (equipment_key, subtype) if this is an ammo entry, else None.

    equipment_key is weapon-specific when a size digit can be extracted
    (e.g. "lrm20_ammo", "ac5_ammo"), or generic "ammo" for untracked types.
    """
    name = megamek_name.strip()
    if not name:
        return None
    # Exact match for non-"ammo"-suffix ammo items (Narc Pods etc.)
    cleaned_for_exact = _clean_name(name)
    if name in _AMMO_EXACT:
        eq_key, subtype = _AMMO_EXACT[name]
        return eq_key, subtype
    if cleaned_for_exact in _AMMO_EXACT:
        eq_key, subtype = _AMMO_EXACT[cleaned_for_exact]
        return eq_key, subtype
    if "ammo" not in name.lower():
        return None
    # Strip suffixes that block prefix matching
    cleaned = _clean_name(name)
    # 1. Prefix table
    for prefix, eq_key, subtype in _AMMO_PREFIXES:
        if name.startswith(prefix) or cleaned.startswith(prefix):
            size_digit = _extract_ammo_variant(subtype, name, prefix)
            if size_digit:
                eq_key = f"{subtype.lower()}{size_digit}_ammo"
            return eq_key, subtype
    # 2. Regex fallback
    for pattern, eq_key, _subtype in _AMMO_REGEXES:
        m = re.search(pattern, name, re.IGNORECASE)
        if m:
            raw_caliber = m.group(1).strip()
            # Strip trailing digits for subtype lookup (handles "MRM 20" → "MRM")
            caliber_no_digit = re.sub(r'\s*\d+$', '', raw_caliber).strip()
            subtype = (_resolve_ammo_subtype(raw_caliber)
                       or _resolve_ammo_subtype(caliber_no_digit)
                       or raw_caliber.upper())
            # Extract size digit and build eq_key, stripping any digit from subtype
            digit_m = re.search(r'(\d+)', raw_caliber)
            subtype_clean = re.sub(r'[\s\d]+', '', subtype)
            if digit_m:
                eq_key = f"{subtype_clean.lower()}{digit_m.group(1)}_ammo"
            return eq_key, subtype
    return None

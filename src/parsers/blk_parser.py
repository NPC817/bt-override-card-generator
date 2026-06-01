from __future__ import annotations
import math
import re
from dataclasses import dataclass, field
from ..models.vehicle import CombatVehicle
from ..models.battle_armor import BattleArmor
from ..models.aero import AeroSpaceFighter
from ..models.infantry import Infantry
from ..models.unit import UnitWeapon, UnitEquipment
from .name_normalizer import normalize_weapon, normalize_equipment, normalize_ammo


@dataclass
class ParseResult:
    unit: CombatVehicle | BattleArmor | AeroSpaceFighter | Infantry
    warnings: list[str] = field(default_factory=list)


def _link_fcs_to_weapon(weapons: list, loc: str, fcs: str) -> None:
    """Link FCS equipment to a weapon at the same location that supports it."""
    from ..models.data_store import DataStore
    for w in reversed(weapons):
        if w.location != loc:
            continue
        try:
            wdef = DataStore.weapon(w.weapon_key)
        except KeyError:
            continue
        if wdef.useFCS and fcs in wdef.useFCS:
            w.fcs = fcs
            return


def _tag(content: str, name: str) -> str | None:
    m = re.search(rf"<{re.escape(name)}>\s*(.*?)\s*</{re.escape(name)}>",
                  content, re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else None


def _tag_lines(content: str, name: str) -> list[str]:
    val = _tag(content, name)
    return [ln.strip() for ln in val.splitlines() if ln.strip()] if val else []


def parse_blk(path: str) -> ParseResult:
    with open(path, encoding="utf-8", errors="replace") as f:
        content = f.read()

    warnings: list[str] = []
    tag       = lambda n: _tag(content, n)
    tag_lines = lambda n: _tag_lines(content, n)

    unit_type_raw = (tag("UnitType") or "Tank").lower()

    if "battle armor" in unit_type_raw or "battlearmor" in unit_type_raw:
        return _parse_ba(content, warnings)

    if "aero" in unit_type_raw:
        return _parse_aero(content, warnings)

    if "convfighter" in unit_type_raw:
        result = _parse_aero(content, warnings)
        result.unit.motive_type = AeroSpaceFighter.CONVENTIONAL
        return result

    if "infantry" in unit_type_raw:
        return _parse_infantry(content, warnings)

    vehicle = CombatVehicle()

    vehicle.chassis = tag("Name") or ""
    vehicle.variant = tag("Model") or ""

    tonnage_str = tag("tonnage") or "50"
    try:
        vehicle.tonnage = float(tonnage_str)
    except ValueError:
        warnings.append(f"Invalid tonnage: {tonnage_str!r}")

    motion_raw = (tag("motion_type") or "Tracked").lower()
    _motion_map = {
        "tracked": CombatVehicle.TRACKED,
        "wheeled": CombatVehicle.WHEELED,
        "hover": CombatVehicle.HOVER,
        "vtol": CombatVehicle.VTOL,
        "wige": CombatVehicle.HOVER,
    }
    vehicle.motive_type = _motion_map.get(motion_raw, CombatVehicle.TRACKED)

    cruise_str = tag("cruiseMP") or "4"
    try:
        vehicle.cruise_mp = int(cruise_str)
    except ValueError:
        warnings.append(f"Invalid cruiseMP: {cruise_str!r}")

    tech_raw = (tag("type") or "IS Level 1").lower()
    if "clan" in tech_raw:
        vehicle.tech = "Clan"
        vehicle.equipment.append(UnitEquipment(equipment_key="freecase", location="All"))
    elif "mixed" in tech_raw:
        vehicle.tech = "Mixed"
    else:
        vehicle.tech = "IS"

    # Armor type (numeric per card_gen.js getArmorType)
    _VEH_ARMOR_TYPE_MAP = {
        2: "reactive", 3: "lasrefl", 4: "hardened", 16: "ferolam", 22: "stealth",
    }
    try:
        at_val = int(tag("armor_type") or "0")
        if at_val in _VEH_ARMOR_TYPE_MAP:
            vehicle.equipment.append(UnitEquipment(
                equipment_key=_VEH_ARMOR_TYPE_MAP[at_val],
            ))
    except ValueError:
        pass

    # Armor block: values are in order FR LS RS RR [TU] [RO]
    armor_lines = tag_lines("armor")
    armor_keys = ["FR", "LS", "RS", "RR", "TU", "RO"]
    for i, val_str in enumerate(armor_lines[:6]):
        try:
            vehicle.armor[armor_keys[i]] = int(val_str)
        except ValueError:
            pass

    # Determine if turret is present
    turret_eq = tag("Turret Equipment") or ""
    vehicle.has_turret = bool(turret_eq.strip())

    # Parse transporters (infantry bays, cargo, mech bays, quarters, etc.)
    transporter_lines = tag_lines("transporters")
    transporter_uses: dict[str, float] = {}
    for line in transporter_lines:
        parts = line.split(":")
        if len(parts) < 2:
            continue
        name = parts[0].strip()
        try:
            amount = float(parts[1])
        except ValueError:
            continue
        if amount <= 0:
            continue  # MegaMek sentinel values (-1 = no limit), not real capacity
        ekey = normalize_equipment(name)
        if ekey:
            transporter_uses[ekey] = transporter_uses.get(ekey, 0.0) + amount
        else:
            warnings.append(f"Unknown transporter: {name!r}")

    for ekey, amount in transporter_uses.items():
        vehicle.equipment.append(UnitEquipment(equipment_key=ekey, uses=amount))

    # Parse all equipment sections
    eq_section_names = [
        "Front Equipment", "Left Equipment", "Right Equipment",
        "Rear Equipment", "Turret Equipment", "Body Equipment",
    ]
    loc_map = {
        "Front Equipment": "FR", "Left Equipment": "LS",
        "Right Equipment": "RS", "Rear Equipment": "RR",
        "Turret Equipment": "TU", "Body Equipment": "",
    }

    for section_name in eq_section_names:
        loc = loc_map[section_name]
        for item_name in tag_lines(section_name):
            ammo = normalize_ammo(item_name)
            if ammo:
                eq_key, subtype = ammo
                vehicle.equipment.append(UnitEquipment(equipment_key=eq_key, subtype=subtype, location=loc))
                continue
            wkey = normalize_weapon(item_name)
            if wkey:
                from ..models.data_store import DataStore
                try:
                    DataStore.weapon(wkey)
                    vehicle.weapons.append(UnitWeapon(weapon_key=wkey, location=loc))
                    continue
                except KeyError:
                    pass  # not a real weapon, fall through to equipment
            ekey = normalize_equipment(item_name)
            if ekey:
                vehicle.equipment.append(UnitEquipment(equipment_key=ekey, location=loc))
                if ekey in ("aiv", "av"):
                    _link_fcs_to_weapon(vehicle.weapons, loc, ekey)
                continue
            if item_name and item_name.lower() not in ("-empty-", ""):
                warnings.append(f"Unknown item in {section_name}: {item_name!r}")

    # Deduplicate equipment by (key, location, subtype)
    seen: set[tuple[str, str, str]] = set()
    deduped: list[UnitEquipment] = []
    for e in vehicle.equipment:
        sig = (e.equipment_key, e.location, e.subtype)
        if sig not in seen:
            seen.add(sig)
            deduped.append(e)
    vehicle.equipment = deduped

    return ParseResult(unit=vehicle, warnings=warnings)


def _parse_ba(content: str, warnings: list[str]) -> ParseResult:
    tag       = lambda n: _tag(content, n)
    tag_lines = lambda n: _tag_lines(content, n)

    ba = BattleArmor()
    ba.chassis = tag("Name") or ""
    ba.variant = tag("Model") or ""

    # Weight class (numeric per card_gen.js: 0=PAL, 1=Light, 2=Medium, 3=Heavy, 4=Assault)
    wc_map = {0: BattleArmor.PAL, 1: BattleArmor.LIGHT, 2: BattleArmor.MEDIUM,
              3: BattleArmor.HEAVY, 4: BattleArmor.ASSAULT}
    try:
        wc_num = int(tag("weightclass") or "3")
        ba.weight_class = wc_map.get(wc_num, BattleArmor.MEDIUM)
    except ValueError:
        pass

    # Squad size
    try:
        ba.squad_size = int(tag("Trooper Count") or "4")
    except ValueError:
        pass

    # Ground MP
    try:
        ba.ground_mp = int(tag("cruiseMP") or "1")
    except ValueError:
        pass

    # Armor per trooper
    try:
        ba.armor_per_trooper = int(tag("Armor") or "4")
    except ValueError:
        pass

    # Armor type (numeric per card_gen.js getArmorType: 2=reactive, 3=lasrefl,
    # 4=hardened, 16=ferolam, 22=stealth, 31-34=bastealth, 35=bafireresist,
    # 36=bamimetic, 37=bareflective, 38=bareactive)
    _BA_ARMOR_TYPE_MAP = {
        2: "reactive", 3: "lasrefl", 4: "hardened", 16: "ferolam",
        22: "stealth",
        31: "bastealth", 32: "bastealth", 33: "bastealth", 34: "bastealth",
        35: "bafireresist", 36: "bamimetic", 37: "bareflective", 38: "bareactive",
    }
    try:
        at_val = int(tag("armor_type") or "0")
        if at_val in _BA_ARMOR_TYPE_MAP:
            ba.equipment.append(UnitEquipment(
                equipment_key=_BA_ARMOR_TYPE_MAP[at_val],
            ))
    except ValueError:
        pass

    # Tech base
    tech_raw = (tag("type") or "IS").lower()
    if "clan" in tech_raw:
        ba.tech = "Clan"
        ba.equipment.append(UnitEquipment(equipment_key="freecase", location="All"))
    elif "mixed" in tech_raw:
        ba.tech = "Mixed"
    else:
        ba.tech = "IS"

    # Motive type
    chassis_raw = (tag("chassis") or "").lower()
    if "quad" in chassis_raw:
        ba.motive_type = BattleArmor.QUAD
    else:
        ba.motive_type = BattleArmor.BIPED

    # Motion type → other motive
    motion_raw = (tag("motion_type") or "").lower()
    if motion_raw == "jump":
        ba.other_motive_type = BattleArmor.OTHER_JUMP
    elif motion_raw == "vtol":
        ba.other_motive_type = BattleArmor.OTHER_VTOL
    elif motion_raw == "umu":
        ba.other_motive_type = BattleArmor.OTHER_UMU
    else:
        ba.other_motive_type = BattleArmor.OTHER_NONE

    # Other MP (from jumpMP, vtolMP, or umuMP tags)
    mp_tag_map = {
        BattleArmor.OTHER_JUMP: "jumpingMP",
        BattleArmor.OTHER_VTOL: "vtolMP",
        BattleArmor.OTHER_UMU: "umuMP",
    }
    mp_tag = mp_tag_map.get(ba.other_motive_type)
    if mp_tag:
        try:
            ba.other_mp = int(tag(mp_tag) or "0")
        except ValueError:
            pass

    # Weapons & Equipment from Squad Equipment or Point Equipment section
    _BA_SKIP = {"SwarmMek", "SwarmWeaponMek", "StopSwarm", "LegAttack",
                "InfantryAssaultRifle", "Auto-Rifle",
                # Standard BA armor — no Override equipment equivalent
                "IS BA Advanced", "BA Advanced",
                # Non-combat mobility / support equipment
                "Parafoil", "BAParafoil",
                # Infantry-scale weapons not representable in Override
                "Infantry Auto Rifle"}

    def _parse_ba_equipment(equip_lines: list[str]) -> None:
        for line in equip_lines:
            parts = [p.strip() for p in line.split(":")]
            if not parts or not parts[0]:
                continue
            item_name = parts[0]
            location = parts[1] if len(parts) > 1 else ""
            subtype = parts[2] if len(parts) > 2 else ""

            # Skip BA tactical abilities + infantry-scale weapons
            if item_name in _BA_SKIP:
                continue
            if item_name.startswith("Auto-Rifle"):
                continue
            # Skip infantry-scale rifles and placeholder items
            if item_name.startswith("Laser Rifle"):
                continue
            if item_name in ("BABattleMechNIU",):
                continue

            # Detect One-Shot suffix — parenthetical or embedded (e.g. ISBASRM4OS)
            one_shot = "(OS)" in item_name
            if one_shot:
                item_name = item_name.replace("(OS)", "").strip()
            elif re.search(r'OS$', item_name, re.IGNORECASE):
                one_shot = True
                item_name = item_name[:-2].strip()

            # Strip BA prefix (e.g. BACLERMediumPulseLaser → CLERMediumPulseLaser)
            if re.match(r'^BA[A-Z]', item_name):
                item_name = item_name[2:]

            # Try as ammo
            ammo = normalize_ammo(item_name)
            if ammo:
                eq_key, ammo_subtype = ammo
                subtype = ammo_subtype or subtype
                ba.equipment.append(UnitEquipment(equipment_key=eq_key, subtype=subtype, location=location))
                continue

            # Try as equipment first (BA armor variants like bastealth/bamimetic are
            # equipment items, not weapons — normalize_weapon's equipment fallback
            # would mis-classify them)
            ekey = normalize_equipment(item_name)
            if ekey:
                ba.equipment.append(UnitEquipment(equipment_key=ekey, location=location))
                continue

            # Try as weapon (must exist in weapons YAML, not just equipment)
            wkey = normalize_weapon(item_name)
            if wkey:
                from ..models.data_store import DataStore
                try:
                    DataStore.weapon(wkey)
                    ba.weapons.append(UnitWeapon(weapon_key=wkey, location=location, one_shot=one_shot))
                    continue
                except KeyError:
                    pass  # resolved to equipment key via fallback — skip
            if ekey:
                ba.equipment.append(UnitEquipment(equipment_key=ekey, location=location))
                continue

            if item_name and item_name.lower() != "-empty-":
                warnings.append(f"Unknown BA item: {item_name!r}")

    eq_lines = tag_lines("Squad Equipment")
    if not eq_lines:
        eq_lines = tag_lines("Point Equipment")
    _parse_ba_equipment(eq_lines)

    # Deduplicate equipment by key+subtype only (BA doesn't track location on card)
    seen: set[tuple[str, str]] = set()
    deduped: list[UnitEquipment] = []
    for e in ba.equipment:
        sig = (e.equipment_key, e.subtype)
        if sig not in seen:
            seen.add(sig)
            # Clear location since BA doesn't display it
            e.location = ""
            deduped.append(e)
    ba.equipment = deduped

    return ParseResult(unit=ba, warnings=warnings)


def _parse_aero(content: str, warnings: list[str]) -> ParseResult:
    tag       = lambda n: _tag(content, n)
    tag_lines = lambda n: _tag_lines(content, n)

    aero = AeroSpaceFighter()

    aero.chassis = tag("Name") or ""
    aero.variant = tag("Model") or ""

    tonnage_str = tag("tonnage") or "50"
    try:
        aero.tonnage = int(float(tonnage_str))
    except ValueError:
        warnings.append(f"Invalid tonnage: {tonnage_str!r}")

    try:
        aero.safe_thrust = int(tag("SafeThrust") or "5")
    except ValueError:
        pass

    aero.max_thrust = int(math.ceil(aero.safe_thrust * 1.5))

    try:
        aero.sinks = int(tag("heatsinks") or "10")
    except ValueError:
        pass

    try:
        sink_type_val = int(tag("sink_type") or "0")
        aero.has_dhs = (sink_type_val == 1)
    except ValueError:
        pass

    tech_raw = (tag("type") or "IS Level 1").lower()
    if "clan" in tech_raw:
        aero.tech = "Clan"
        aero.equipment.append(UnitEquipment(equipment_key="freecase", location="All"))
    elif "mixed" in tech_raw:
        aero.tech = "Mixed"
    else:
        aero.tech = "IS"

    armor_lines = tag_lines("armor")
    armor_keys = ["N", "LW", "RW", "A"]
    for i, val_str in enumerate(armor_lines[:4]):
        try:
            aero.armor[armor_keys[i]] = int(val_str)
        except ValueError:
            pass

    eq_section_names = [
        "Nose Equipment", "Left Wing Equipment", "Right Wing Equipment",
        "Aft Equipment", "Wings Equipment", "Fuselage Equipment",
    ]
    loc_map = {
        "Nose Equipment": "N", "Left Wing Equipment": "LW",
        "Right Wing Equipment": "RW", "Aft Equipment": "A",
        "Wings Equipment": "", "Fuselage Equipment": "",
    }

    for section_name in eq_section_names:
        loc = loc_map[section_name]
        for item_name in tag_lines(section_name):
            ammo = normalize_ammo(item_name)
            if ammo:
                eq_key, subtype = ammo
                aero.equipment.append(UnitEquipment(equipment_key=eq_key, subtype=subtype, location=loc))
                continue
            wkey = normalize_weapon(item_name)
            if wkey:
                from ..models.data_store import DataStore
                try:
                    DataStore.weapon(wkey)
                    aero.weapons.append(UnitWeapon(weapon_key=wkey, location=loc))
                    continue
                except KeyError:
                    pass
            ekey = normalize_equipment(item_name)
            if ekey:
                aero.equipment.append(UnitEquipment(equipment_key=ekey, location=loc))
                if ekey in ("aiv", "av"):
                    _link_fcs_to_weapon(aero.weapons, loc, ekey)
                continue
            if item_name and item_name.lower() not in ("-empty-", ""):
                warnings.append(f"Unknown item in {section_name}: {item_name!r}")

    seen: set[tuple[str, str, str]] = set()
    deduped: list[UnitEquipment] = []
    for e in aero.equipment:
        sig = (e.equipment_key, e.location, e.subtype)
        if sig not in seen:
            seen.add(sig)
            deduped.append(e)
    aero.equipment = deduped

    return ParseResult(unit=aero, warnings=warnings)


def _map_inf_weapon(name: str) -> str:
    """Map a BLK Primary weapon name to one of the 6 Override infantry weapon keys."""
    n = name.lower().replace(" ", "").replace("-", "")
    if "laser" in n:
        return "laser"
    if "flamer" in n or "inferno" in n:
        return "flamer"
    if "lrm" in n:
        return "lrm"
    if "srm" in n:
        return "srm"
    if "machinegun" in n:
        return "mg"
    return "ballistic"


def _parse_infantry(content: str, warnings: list[str]) -> ParseResult:
    tag       = lambda n: _tag(content, n)
    tag_lines = lambda n: _tag_lines(content, n)

    inf = Infantry()
    inf.chassis = tag("Name") or ""
    inf.variant = tag("Model") or ""

    try:
        inf.squad_size = int(tag("squad_size") or "7")
    except ValueError:
        warnings.append("Invalid squad_size")

    try:
        inf.squad_count = int(tag("squadn") or "4")
    except ValueError:
        warnings.append("Invalid squadn")

    # motion_type → motive key
    motion_raw = (tag("motion_type") or "Leg").strip().lower()
    _MOTION_MAP = {
        "leg": "Foot",
        "motorized": "Motorized",
        "jump": "Jump",
        "hover": "Mechanized Hover",
        "tracked": "Mechanized Tracked",
        "wheeled": "Mechanized Wheeled",
    }
    if motion_raw.startswith("beast"):
        inf.motion_type_key = "Foot"
    else:
        inf.motion_type_key = _MOTION_MAP.get(motion_raw, "Foot")

    # Primary weapon → weapon type key
    primary_raw = tag("Primary") or ""
    inf.weapon_type = _map_inf_weapon(primary_raw)

    # Tech base
    tech_raw = (tag("type") or "IS Level 1").lower()
    if "clan" in tech_raw:
        inf.tech = "Clan"
    elif "mixed" in tech_raw:
        inf.tech = "Mixed"
    else:
        inf.tech = "IS"

    # Equipment fields (stored as plain text, displayed in Equipment section)
    inf.armor_kit = tag("armorKit") or ""
    trooper_eq_lines = tag_lines("Troopers Equipment")
    inf.trooper_equipment = ", ".join(trooper_eq_lines) if trooper_eq_lines else ""
    inf.field_guns = tag_lines("Field Guns Equipment")

    return ParseResult(unit=inf, warnings=warnings)

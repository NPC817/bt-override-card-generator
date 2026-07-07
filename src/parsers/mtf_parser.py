from __future__ import annotations
from dataclasses import dataclass, field
from ..models.mech import BattleMech
from ..models.unit import UnitWeapon, UnitEquipment
from .name_normalizer import normalize_weapon, normalize_equipment, normalize_ammo


@dataclass
class ParseResult:
    unit: BattleMech
    warnings: list[str] = field(default_factory=list)


def parse_mtf(path: str) -> ParseResult:
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    mech = BattleMech()
    warnings: list[str] = []

    # Map MTF tech base strings → internal
    _tech_map = {
        "inner sphere": "IS",
        "clan": "Clan",
        "mixed (is chassis)": "Mixed",
        "mixed (clan chassis)": "Mixed",
    }

    # Armor location mappings (MTF key → internal key)
    _armor_map = {
        "la": "LA", "ra": "RA",
        "lt": "LT", "rt": "RT", "ct": "CT",
        "hd": "HD", "ll": "LL", "rl": "RL",
        "fll": "FLL", "frl": "FRL", "rll": "RLL", "rrl": "RRL",
        "rtl": "LTR", "rtr": "RTR", "rtc": "CTR",
    }

    in_weapons_section = False
    weapons_remaining = 0
    current_crit_loc = ""

    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        lower = line.lower()

        # ── Crit-section header ───────────────────────────────────────────
        if not in_weapons_section:
            crit_loc = _is_crit_header(line)
            if crit_loc:
                current_crit_loc = crit_loc
                continue

        # ── Simple key: value fields ──────────────────────────────────────
        if ":" in line and not in_weapons_section:
            key, _, value = line.partition(":")
            key = key.strip().lower()
            value = value.strip()

            if key == "chassis":
                mech.chassis = value
            elif key == "model":
                mech.variant = value
            elif key == "mass":
                try:
                    mech.tonnage = int(value)
                except ValueError:
                    warnings.append(f"Invalid mass: {value!r}")
            elif key == "config":
                val_lower = value.lower()
                mech.motive_type = BattleMech.QUAD if "quad" in val_lower else BattleMech.BIPED
                if "omnimech" in val_lower:
                    mech.omni = True
            elif key == "techbase":
                mech.tech = _tech_map.get(value.lower(), "IS")
                if mech.tech == "Clan":
                    mech.equipment.append(UnitEquipment(equipment_key="freecase", location="All"))
            elif key == "walk mp":
                try:
                    mech.walk_mp = int(value)
                except ValueError:
                    warnings.append(f"Invalid walk mp: {value!r}")
            elif key == "jump mp":
                try:
                    mech.jump_mp = int(value)
                except ValueError:
                    pass
            elif key == "heat sinks":
                parts = value.split()
                try:
                    mech.sinks = int(parts[0])
                except (ValueError, IndexError):
                    warnings.append(f"Invalid heat sinks: {value!r}")
                mech.has_dhs = len(parts) > 1 and "double" in value.lower()
            elif key == "omnimech":
                mech.omni = value.lower() == "true"
            elif key in ("armor", "engine", "structure", "myomer"):
                ekey = _mtf_special_equip(value, key)
                if ekey:
                    mech.equipment.append(UnitEquipment(equipment_key=ekey))
            elif lower.startswith("weapons:"):
                try:
                    weapons_remaining = int(value)
                    in_weapons_section = True
                except ValueError:
                    pass
            else:
                # Armor fields: "LA armor", "CT armor", "RTL armor", etc.
                stripped = key.replace(" armor", "").strip()
                loc_key = _armor_map.get(stripped)
                if loc_key is not None:
                    try:
                        mech.armor[loc_key] = int(value)
                    except ValueError:
                        pass

        # ── Weapons section ───────────────────────────────────────────────
        elif in_weapons_section and weapons_remaining > 0:
            # Format: "2 Medium Laser, Left Arm"  (quantity prefix optional)
            import re as _re
            parts = [p.strip() for p in line.split(",")]
            if len(parts) >= 2:
                wname = parts[0]
                # Extract leading quantity: "2 ISLRM5" → qty=2, name="ISLRM5"
                qty_match = _re.match(r"^(\d+)\s+", wname)
                qty = int(qty_match.group(1)) if qty_match else 1
                loc_raw = parts[1].lower()
                loc = _map_location(loc_raw)
                key = normalize_weapon(wname)
                if key:
                    from ..models.data_store import DataStore
                    try:
                        DataStore.weapon(key)
                        is_os = "(OS)" in wname.upper()
                        for _ in range(qty):
                            mech.weapons.append(UnitWeapon(weapon_key=key, location=loc, one_shot=is_os))
                    except KeyError:
                        pass  # resolves to equipment key, not a weapon
                else:
                    warnings.append(f"Unknown weapon: {wname!r}")
                weapons_remaining -= 1
                if weapons_remaining == 0:
                    in_weapons_section = False

        # ── Ammo/equipment in crit sections ───────────────────────────────
        elif not in_weapons_section:
            # Detect rear-mounted weapons: "Medium Laser (R)" → update weapon location
            rear = False
            item_name = line
            if line.endswith("(R)") and len(line) > 4:
                rear = True
                item_name = line[:-3].strip()

            ammo = normalize_ammo(item_name)
            if ammo:
                eq_key, subtype = ammo
                mech.equipment.append(UnitEquipment(
                    equipment_key=eq_key, subtype=subtype, location=current_crit_loc,
                ))
            else:
                eq_key = normalize_equipment(item_name)
                if eq_key:
                    mech.equipment.append(UnitEquipment(
                        equipment_key=eq_key, location=current_crit_loc,
                    ))
                    # Link FCS to a weapon at this location that supports it
                    if eq_key in ("aiv", "av"):
                        from ..models.data_store import DataStore as _DS
                        for _w in reversed(mech.weapons):
                            if _w.location != current_crit_loc:
                                continue
                            try:
                                _wd = _DS.weapon(_w.weapon_key)
                            except KeyError:
                                continue
                            if _wd.useFCS and eq_key in _wd.useFCS:
                                _w.fcs = eq_key
                                break

            # Upgrade weapons from Weapons section when crit slot has Clan prefix.
            # Weapons section lists generic name ("ER Medium Laser" → ermlas IS),
            # crit slot has actual item ("CLERMediumLaser" → cermlas Clan).
            wkey = normalize_weapon(item_name)
            if wkey and wkey.startswith("c"):
                base_key = wkey[1:]  # strip 'c' prefix to get IS-equivalent key
                for w in mech.weapons:
                    if w.weapon_key == base_key and w.location == current_crit_loc:
                        w.weapon_key = wkey
                        if "(OS)" in item_name.upper():
                            w.one_shot = True
                        break

            # If rear-mounted weapon, update the matching weapon's location
            if rear:
                wkey = normalize_weapon(item_name)
                if wkey:
                    rear_loc = _REAR_LOC_MAP.get(current_crit_loc)
                    if rear_loc:
                        for w in mech.weapons:
                            if w.weapon_key == wkey and w.location == current_crit_loc:
                                w.location = rear_loc
                                break

    # Deduplicate equipment by (key, location, subtype).
    # For ammo entries, count tons into the `uses` field instead of dropping.
    _AMMO_KEYS = frozenset({"ammo", "ammolimited"})
    seen: set[tuple[str, str, str]] = set()
    deduped: list[UnitEquipment] = []
    ammo_counts: dict[tuple[str, str, str], int] = {}
    for e in mech.equipment:
        is_ammo = e.equipment_key in _AMMO_KEYS or e.equipment_key.endswith("_ammo")
        if is_ammo:
            sig = (e.equipment_key, e.location, e.subtype)
            ammo_counts[sig] = ammo_counts.get(sig, 0) + 1
            if sig not in seen:
                seen.add(sig)
                deduped.append(e)
        else:
            sig = (e.equipment_key, e.location, e.subtype)
            if sig not in seen:
                seen.add(sig)
                deduped.append(e)
    # Set uses = ton count for ammo entries
    for e in deduped:
        sig = (e.equipment_key, e.location, e.subtype)
        if sig in ammo_counts:
            e.uses = float(ammo_counts[sig])
    mech.equipment = deduped

    return ParseResult(unit=mech, warnings=warnings)


def _mtf_special_equip(value: str, category: str) -> str | None:
    """Parse MTF armor/engine/structure/myomer type into an equipment key.

    Values are MegaMek MTF header strings like "Stealth(Inner Sphere)",
    "340 Light Engine(IS)", "IS Standard", "Triple Strength".
    Strips rating numbers, tech-base qualifiers, and maps to the
    full names that normalize_equipment expects.
    """
    import re
    # Detect Clan tech base from parenthetical qualifier before stripping
    is_clan = bool(re.search(r"\(Clan\)", value, re.IGNORECASE))
    cleaned = re.sub(r"\([^)]*\)", "", value).strip()
    cleaned = re.sub(r"^\d+\s*", "", cleaned).strip()
    cleaned = re.sub(r"^(IS|Clan)\s+", "", cleaned, flags=re.IGNORECASE)
    if cleaned.lower() in ("standard", "none", ""):
        return None

    _SUFFIXES = {
        "armor": [" Armor"],
        "engine": [" Engine"],
        "structure": [" Internal Structure"],
        "myomer": [" Myomer"],
    }
    suffixes = [""] + _SUFFIXES.get(category, [])

    # Try Clan-prefixed name first when tech base is Clan
    if is_clan:
        for suffix in suffixes:
            ekey = normalize_equipment("Clan " + cleaned + suffix)
            if ekey:
                return ekey

    for suffix in suffixes:
        ekey = normalize_equipment(cleaned + suffix)
        if ekey:
            return ekey

    return None


def _map_location(loc_raw: str) -> str:
    _map = {
        "left arm": "LA", "right arm": "RA",
        "left torso": "T", "right torso": "T", "center torso": "T",
        "head": "HD", "left leg": "LL", "right leg": "RL",
        "left torso (r)": "(R) T", "right torso (r)": "(R) T", "center torso (r)": "(R) T",
        "head (r)": "(R) HD", "left leg (r)": "(R) LL", "right leg (r)": "(R) RL",
    }
    return _map.get(loc_raw.lower(), loc_raw.upper())


# Crit section location → rear-mounted weapon location
_REAR_LOC_MAP: dict[str, str] = {
    "T": "(R) T", "HD": "(R) HD", "LL": "(R) LL", "RL": "(R) RL",
}

# Crit section headers → specific location codes (separate from weapon loc mapping)
_CRIT_LOC_MAP: dict[str, str] = {
    "left arm": "LA", "right arm": "RA",
    "left torso": "T", "right torso": "T", "center torso": "T",
    "head": "HD", "left leg": "LL", "right leg": "RL",
}


def _is_crit_header(line: str) -> str | None:
    """Return location code if line is a crit-section header, else None."""
    stripped = line.strip().rstrip(":")
    lower = stripped.lower()
    return _CRIT_LOC_MAP.get(lower)

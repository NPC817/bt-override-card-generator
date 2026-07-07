from __future__ import annotations
import math
from collections import defaultdict
from dataclasses import dataclass, field
from ..models.unit import AbstractUnit, UnitWeapon
from ..models.data_store import DataStore
from ..models.weapon import Weapon
from ..engine.conversion import ConversionEngine

# ── Arc constants ─────────────────────────────────────────────────────────────

ARC_FRONT = "Front"
ARC_REAR  = "Rear"
ARC_LEFT  = "Left"
ARC_RIGHT = "Right"
ARC_ANY   = "Any"

_REAR_LOCS  = {"CTR", "LTR", "RTR", "AFT", "(R) T", "(R) LL", "(R) RL", "(R) HD"}
_LEFT_LOCS  = {"LS", "LW"}
_RIGHT_LOCS = {"RS", "RW"}
_ANY_LOCS   = {"TU"}

_OPPOSITE_LOCS: dict[str, str] = {
    "LA": "RA", "RA": "LA",
    "LL": "RL", "RL": "LL",
    "LS": "RS", "RS": "LS",
    "LW": "RW", "RW": "LW",
}


def _fmt_rng(val: int) -> str:
    """Format a range bracket: ≥9→'—', <0→'-N', else '+N'."""
    if val >= 9:
        return "—"
    if val < 0:
        return str(val)
    return f"+{val}"


def _location_arc(location: str) -> str:
    loc = location.upper()
    if loc in _REAR_LOCS:  return ARC_REAR
    if loc in _LEFT_LOCS:  return ARC_LEFT
    if loc in _RIGHT_LOCS: return ARC_RIGHT
    if loc in _ANY_LOCS:   return ARC_ANY
    return ARC_FRONT


# ── Shared damage formatting ────────────────────────────────────────────────────

def _format_damage_tic(
    total_d: float,
    *,
    is_var: bool = False,
    var_pbs: float = 0,
    var_m: float = 0,
    var_lx: float = 0,
    damage_m: int = 0,
    damage_adj: int = 0,
    shift_m: int = 0,
    use_c: int = 0,
    use_h: int = 0,
    use_m_val: int | None = None,
    hag_base: int = 0,
    return_float: bool = False,
) -> str | float:
    """Format Override damage display for a weapon or TIC group.

    Mirrors card_gen.js groupData() logic.  All callers pass pre-aggregated
    numeric values — this function only does the formatting math.
    """
    # Variable damage (Gauss, HAG, etc.)
    # var values carry full Classic damage per bracket; base damage already
    # baked in (JS accumulation doesn't add to n.damage for var weapons)
    if is_var:
        # HAG: cluster-var weapons — format as {hagBase}+C{pbs}|{m}|{lx}
        if use_c > 0:
            pb = math.ceil(var_pbs / 3) - use_c
            m_val = math.ceil(var_m / 3) - use_c
            lx = math.ceil(var_lx / 3) - use_c
            base = hag_base if hag_base > 0 else use_c
            if return_float:
                return float(base + pb)
            return f"{base}+C{pb}|{m_val}|{lx}"

        pb = math.ceil(var_pbs / 3)
        m_val = math.ceil(var_m / 3)
        lx = math.ceil(var_lx / 3)
        if return_float:
            if damage_m > 0:
                return float(math.ceil((total_d + damage_adj) / 3))
            return float(max(pb, m_val, lx))
        result = f"{pb}|{m_val}|{lx}"

        # Missile-var weapons (MML, ATM, eLRM): append M dice suffix
        if damage_m > 0:
            damage_max = total_d + damage_adj
            if use_m_val is not None and use_m_val > 0:
                result += f"+M{use_m_val} ({math.ceil(damage_max / 3)})"
            else:
                a = math.ceil(damage_max / 3) - damage_m
                use_m = math.ceil(a / 3) + shift_m
                if use_m > 0:
                    result += f"+M{use_m} ({math.ceil(damage_max / 3)})"

        return result

    # Missile weapons (SRM, LRM, ATM, etc.) — use_m_val computed per-weapon by caller
    if damage_m > 0:
        damage_max = total_d + damage_adj
        base = damage_m - shift_m
        if return_float:
            return float(math.ceil(damage_max / 3))
        if use_m_val is not None and use_m_val > 0:
            return f"{base}+M{use_m_val} ({math.ceil(damage_max / 3)})"
        return str(base)

    # Cluster weapons (LB-X ACs)
    if use_c > 0:
        damage_c = math.ceil(total_d / 3) - use_c
        if return_float:
            return float(use_c + damage_c)
        return f"{use_c}+C{damage_c}"

    # Heat weapons (Flamers)
    if use_h > 0:
        h_val = max(int(use_h / 5 + 0.5), 1)
        base = math.ceil(total_d / 3) if total_d else 0
        if return_float:
            return float(base + h_val)
        return f"{base}+H{h_val}" if base else f"+H{h_val}"

    # Standard weapon
    ceil_val = math.ceil(total_d / 3)
    if return_float:
        return float(ceil_val)
    return str(ceil_val)


# ── ResolvedWeapon ────────────────────────────────────────────────────────────

@dataclass
class ResolvedWeapon:
    unit_weapon: UnitWeapon
    weapon: Weapon
    tic: int
    location: str
    ammo_type: str
    one_shot: bool
    count: int = 1
    tonnage: int = 0
    fcs: str | None = None  # "aiv", "av", or None
    tc: bool = False        # Targeting Computer active for this weapon

    @property
    def arc(self) -> str:
        return _location_arc(self.location)

    @property
    def display_name(self) -> str:
        prefix = f"×{self.count} " if self.count > 1 else ""
        name = f"{prefix}{self.weapon.name}"
        if self.fcs == "aiv":
            name += " (AIV)"
        elif self.fcs == "av":
            name += " (AV)"
        if int(self.weapon.useR or 0) > 0:
            name += " (RF)"
        return name

    def _tc_range(self, raw: int) -> int:
        return max(raw - 1, -1) if self.tc and raw != 9 else raw

    @property
    def damage_display(self) -> int:
        return self.weapon.damage_value(self.tonnage)

    @property
    def damage_str(self) -> str:
        w = self.weapon
        d = w.damage_value(self.tonnage)
        use_c = int(w.useC) if w.useC else 0
        use_h = int(w.useH) if w.useH else 0
        hag_base = (2 if w.has_special("hag20") else
                    3 if w.has_special("hag30") else
                    4 if w.has_special("hag40") else 0)
        return _format_damage_tic(
            total_d=d,
            is_var=w.has_special("var"),
            var_pbs=w.varPBSdamage, var_m=w.varMdamage, var_lx=w.varLXdamage,
            damage_m=w.damageM, damage_adj=w.damageAdj, shift_m=w.shiftM,
            use_c=use_c, use_h=use_h,
            hag_base=hag_base,
        )

    @property
    def heat_str(self) -> str:
        h = self.weapon.heat_value()
        return str(h) if h else "—"

    def _rng(self, val: int) -> str:
        return _fmt_rng(val)

    @property
    def range_pb(self) -> str: return self._rng(self._tc_range(self.weapon.rangePB))
    @property
    def range_s(self)  -> str: return self._rng(self._tc_range(self.weapon.rangeS))
    @property
    def range_m(self)  -> str: return self._rng(self._tc_range(self.weapon.rangeM))
    @property
    def range_l(self)  -> str: return self._rng(self._tc_range(self.weapon.rangeL))
    @property
    def range_x(self)  -> str: return self._rng(self._tc_range(self.weapon.rangeX))


# ── TicGroup accumulator ──────────────────────────────────────────────────────

@dataclass
class TicGroup:
    """Mirrors the JS `x` class: accumulates weapons for one TIC slot."""
    weapons: list[ResolvedWeapon] = field(default_factory=list)

    @property
    def used(self) -> bool:
        return len(self.weapons) > 0

    @property
    def damage(self) -> float:
        """Raw damage sum: non-missile weapons + varPBS for var weapons."""
        total = 0.0
        for rw in self.weapons:
            w = rw.weapon
            if w.damageM > 0:
                if w.has_special("var"):
                    total += w.varPBSdamage
            else:
                total += w.damage_value(rw.tonnage)
        return total

    @property
    def damage_m(self) -> int:
        """Sum of raw damageM for missile weapons (shiftM subtraction
        happens in _format_damage_tic)."""
        return sum(
            rw.weapon.damageM
            for rw in self.weapons
            if rw.weapon.damageM > 0 and not rw.weapon.has_special("var")
        )

    @property
    def heat(self) -> int:
        return sum(rw.weapon.heat_value() for rw in self.weapons)

    def _max_range(self, attr: str) -> int:
        if not self.weapons:
            return 0
        vals = []
        for rw in self.weapons:
            v = getattr(rw.weapon, attr)
            if rw.tc and v != 9:
                v = max(v - 1, -1)
            vals.append(v)
        return max(vals)

    @property
    def range_pb(self) -> int: return self._max_range("rangePB")
    @property
    def range_s(self)  -> int: return self._max_range("rangeS")
    @property
    def range_m(self)  -> int: return self._max_range("rangeM")
    @property
    def range_l(self)  -> int: return self._max_range("rangeL")
    @property
    def range_x(self)  -> int: return self._max_range("rangeX")

    @property
    def arcs(self) -> list[str]:
        seen: list[str] = []
        for rw in self.weapons:
            a = rw.arc
            if a not in seen:
                seen.append(a)
        return seen

    def _all(self, fn) -> bool:
        return bool(self.weapons) and all(fn(rw) for rw in self.weapons)

    # use_tc: special check (useTC field, not has_special)
    @property
    def use_tc(self) -> bool: return self._all(lambda r: bool(r.weapon.useTC))

    # use_os: checks one_shot on the resolved weapon, not the weapon definition
    @property
    def use_os(self) -> bool: return self._all(lambda r: r.one_shot)

    def __getattr__(self, name: str):
        """Dynamic use_<flag> checks for missile/special weapon flags."""
        if name.startswith("use_"):
            flag = name[4:]
            if flag in _SPECIAL_FLAGS:
                return self._all(lambda r: r.weapon.has_special(flag))
        raise AttributeError(f"'{type(self).__name__}' has no attribute {name!r}")

    @property
    def use_r(self) -> int:
        total = 0
        for rw in self.weapons:
            if rw.weapon.damageM <= 0:
                try:
                    total += int(rw.weapon.useR)
                except (ValueError, TypeError):
                    pass
        return total

    def _var_damage_parts(self) -> tuple:
        """Shared variable-damage computation for damage_str and sort_damage."""
        use_var_c = sum(int(r.weapon.useC) for r in self.weapons if r.weapon.useC)
        hag_base = 0
        for r in self.weapons:
            w = r.weapon
            if w.has_special("hag20"):
                hag_base = 2
            elif w.has_special("hag30"):
                hag_base = 3
            elif w.has_special("hag40"):
                hag_base = 4
            if hag_base:
                break
        var_m_weapons = [r for r in self.weapons if r.weapon.damageM > 0]
        use_m = 0
        damage_m_sum = 0
        damage_adj_sum = 0
        shift_m_sum = 0
        for r in var_m_weapons:
            w = r.weapon
            dmg_max = w.damage_value(r.tonnage) + w.damageAdj
            a = math.ceil(dmg_max / 3) - w.damageM
            use_m += math.ceil(a / 3) + w.shiftM
            damage_m_sum += w.damageM
            damage_adj_sum += w.damageAdj
            shift_m_sum += w.shiftM
        return (use_var_c, hag_base, damage_m_sum, damage_adj_sum, shift_m_sum, use_m)

    def _compute_damage(self, return_float: bool = False):
        """Shared damage computation for damage_str and sort_damage."""
        # Variable damage (Gauss, HAG)
        if self._all(lambda r: r.weapon.has_special("var")):
            use_var_c, hag_base, damage_m_sum, damage_adj_sum, shift_m_sum, use_m = self._var_damage_parts()
            return _format_damage_tic(
                total_d=sum(r.weapon.damage_value(r.tonnage) for r in self.weapons),
                is_var=True,
                var_pbs=sum(r.weapon.varPBSdamage for r in self.weapons),
                var_m=sum(r.weapon.varMdamage for r in self.weapons),
                var_lx=sum(r.weapon.varLXdamage for r in self.weapons),
                damage_m=damage_m_sum,
                damage_adj=damage_adj_sum,
                shift_m=shift_m_sum,
                use_c=use_var_c,
                hag_base=hag_base,
                use_m_val=use_m if use_m > 0 else None,
                return_float=return_float,
            )

        # Missile weapons (SRM, LRM, ATM, ...)
        if self.damage_m > 0:
            mws = [r for r in self.weapons if r.weapon.damageM > 0 and not r.weapon.has_special("var")]
            # Compute useM per-weapon then sum (matching JS groupData lines 4869-4872)
            use_m = 0
            for r in mws:
                w = r.weapon
                dmg_max = w.damage_value(r.tonnage) + w.damageAdj
                a = math.ceil(dmg_max / 3) - w.damageM
                use_m += math.ceil(a / 3) + w.shiftM
            return _format_damage_tic(
                total_d=sum(r.weapon.damage_value(r.tonnage) for r in mws),
                damage_m=self.damage_m,
                damage_adj=sum(r.weapon.damageAdj for r in mws),
                shift_m=sum(r.weapon.shiftM for r in mws),
                use_m_val=use_m,
                return_float=return_float,
            )

        # Cluster weapons (LB-X ACs)
        total_use_c = sum(int(r.weapon.useC) for r in self.weapons if r.weapon.useC)
        if total_use_c > 0:
            return _format_damage_tic(
                total_d=sum(r.weapon.damage_value(r.tonnage) for r in self.weapons),
                use_c=total_use_c,
                return_float=return_float,
            )

        # Heat weapons (Flamers)
        total_use_h = sum(int(r.weapon.useH) for r in self.weapons if r.weapon.useH)
        if total_use_h > 0:
            return _format_damage_tic(
                total_d=sum(r.weapon.damage_value(r.tonnage) for r in self.weapons),
                use_h=total_use_h,
                return_float=return_float,
            )

        # Standard
        return _format_damage_tic(
            total_d=sum(r.weapon.damage_value(r.tonnage) for r in self.weapons),
            return_float=return_float,
        )

    @property
    def damage_str(self) -> str:
        """Combined damage display for all weapons in this TIC group."""
        if not self.weapons:
            return "—"
        return self._compute_damage(return_float=False)

    @property
    def sort_damage(self) -> float:
        """Max Override damage value for sorting TICs high-to-low."""
        if not self.weapons:
            return 0.0
        return self._compute_damage(return_float=True)


# ── Scoring ───────────────────────────────────────────────────────────────────

_SPECIAL_FLAGS = (
    "ssrm", "slrm", "srm", "lrm", "mrm",
    "atm", "rl", "srt", "lrt", "hag", "sbg",
)


def _score_weapon_for_tic(rw: ResolvedWeapon, tig: TicGroup, tic_idx: int) -> float:
    """Score `rw` against TIC slot `tig`; mirrors JS _scoreWeaponForTicV5."""
    score = 100.0 - tic_idx

    if not tig.used:
        return score          # any weapon can start an empty TIC

    w   = rw.weapon
    arc = rw.arc

    # Arc compatibility: rear/side weapons can't share a front TIC
    if arc == ARC_REAR  and ARC_REAR  not in tig.arcs: return 0.0
    if arc == ARC_LEFT  and ARC_LEFT  not in tig.arcs: return 0.0
    if arc == ARC_RIGHT and ARC_RIGHT not in tig.arcs: return 0.0

    # Missile type compatibility: all weapons in a TIC must share missile type
    for flag in _SPECIAL_FLAGS:
        if w.has_special(flag) != getattr(tig, f"use_{flag}"):
            return 0.0

    # RAC compatibility
    rw_use_r = int(w.useR) if w.useR else 0
    if (rw_use_r > 0) != (tig.use_r > 0):
        return 0.0

    # One-shot compatibility
    if rw.one_shot != tig.use_os:
        return 0.0

    # Physical weapons never share a TIC
    if w.type == "P":
        return 0.0

    # Damage budget ≤ 5
    if w.damageM > 0:
        combined = math.ceil(tig.damage / 3) + tig.damage_m + w.damageM
    else:
        combined = math.ceil((tig.damage + w.damage_value(rw.tonnage)) / 3) + tig.damage_m
    if combined > 5:
        return 0.0

    # Arc multiplier
    if arc not in tig.arcs:
        score *= 0.6

    # Range matching multipliers (X mismatch is worst, S is least bad)
    if tig.range_x != w.rangeX: score *= 0.1
    if tig.range_l != w.rangeL: score *= 0.2
    if tig.range_m != w.rangeM: score *= 0.4
    if tig.range_s != w.rangeS: score *= 0.8

    return score


def _sort_key_v5(rw: ResolvedWeapon) -> tuple:
    """Pre-sort matching JS sortV5: longer-range weapons first."""
    w = rw.weapon
    rx = w.rangeX if w.rangeX != 0 else 9
    rl = w.rangeL if w.rangeL != 0 else 9
    rm = w.rangeM if w.rangeM != 0 else 9
    rs = w.rangeS if w.rangeS != 0 else 9
    loc_pri = 0 if rw.location == "LA" else (1 if rw.location == "RA" else 2)
    is_rear = 1 if rw.arc == ARC_REAR else 0
    return (
        rw.tic,
        rx, rl, rm, rs,
        -(w.damage_value(rw.tonnage) + w.damageAdj),   # descending damageMax
        w.heat_value(),
        loc_pri,
        w.name.lower(),
        is_rear,
    )


# ── TIC rule catalogue ────────────────────────────────────────────────────────

TIC_RULES: dict[int, str] = {
    1:  "A single TIC with multiple weapons cannot deal more than 5 points of damage "
        "(or 14 points of max missile damage).",
    2:  "Rear-facing weapons can only be grouped with other rear-facing weapons.",
    3:  "Side-facing weapons can only be grouped with other same-side-facing weapons.",
    4:  "Missiles equipped with an Artemis Fire Control System cannot be grouped "
        "with non-Artemis missiles.",
    5:  "Streak missiles can only be grouped with other Streak missiles of the same type.",
    6:  "Missile launchers can only be grouped with other launchers of the same type.",
    7:  "Torpedo launchers can only be grouped with other launchers of the same type.",
    8:  "Rapid fire weapons can only be grouped with other rapid fire weapons.",
    9:  "Hyper-Assault Gauss can only be grouped with other Hyper-Assault Gauss.",
    10: "Silver Bullet Gauss can only be grouped with other Silver Bullet Gauss.",
    11: "One-shot weapons can only be grouped with other one-shot weapons.",
    12: "Physical weapons cannot be grouped with any other weapon.",
    13: "AC/LAC weapons in a TIC cannot use different special ammo types.",
}

_AC_AMMO_TYPES: frozenset[str] = frozenset({"AC", "LBX", "UAC", "RAC"})

_AMMO_SUFFIX: dict[str, str] = {
    "Precision": " (Precision)",
    "AP": " (Armor Piercing)",
    "Flak": " (Flak)",
    "Flechette": " (AI) (Flechette)",
    "Tracer": " (Tracer)",
}


def _group_ammo_type(rws: list[ResolvedWeapon]) -> str:
    """Return unanimous ammo type for AC weapons in TIC; 'Std' if mixed or absent."""
    ac_rws = [rw for rw in rws if rw.weapon.useAmmo == "AC"]
    if not ac_rws:
        return "Std"
    ammo_set = {rw.ammo_type or "Std" for rw in ac_rws}
    return ammo_set.pop() if len(ammo_set) == 1 else "Std"


def _adjust_range(val: int, offset: int) -> int:
    """Apply range offset; skip if val >= 9 (means no range defined)."""
    return val if val >= 9 else val + offset


_FLAG_TO_RULE: dict[str, int] = {
    "ssrm": 5, "slrm": 5,
    "srm": 6, "lrm": 6, "mrm": 6, "atm": 6, "rl": 6,
    "srt": 7, "lrt": 7,
    "hag": 9,
    "sbg": 10,
}


def validate_tic_assignments(resolved: list[ResolvedWeapon]) -> list[str]:
    """
    Validate manual TIC assignments against the 13 grouping rules.
    Returns a list of human-readable violation messages.
    """
    violations: list[str] = []

    tic_map: dict[int, list[ResolvedWeapon]] = {}
    for rw in resolved:
        tic_map.setdefault(rw.tic, []).append(rw)

    for tic_num in sorted(tic_map.keys()):
        weapons = tic_map[tic_num]
        if len(weapons) <= 1:
            continue

        grp = TicGroup(weapons=weapons)
        prefix = f"TIC {tic_num}: "

        # Rule 12 — physical weapons cannot share a TIC
        if any(rw.weapon.type == "P" for rw in weapons):
            violations.append(prefix + TIC_RULES[12])
            continue  # remaining rules are moot for a physically-mixed TIC

        # Rule 2 — rear-facing only with rear-facing
        rear = sum(1 for rw in weapons if rw.arc == ARC_REAR)
        if 0 < rear < len(weapons):
            violations.append(prefix + TIC_RULES[2])

        # Rule 3 — side-facing only with same side
        left  = sum(1 for rw in weapons if rw.arc == ARC_LEFT)
        right = sum(1 for rw in weapons if rw.arc == ARC_RIGHT)
        if 0 < left < len(weapons) or 0 < right < len(weapons):
            violations.append(prefix + TIC_RULES[3])

        # Rule 4 — Artemis missiles cannot mix with non-Artemis missiles
        missile_rws = [rw for rw in weapons if rw.weapon.damageM > 0]
        if len(missile_rws) > 1:
            has_artemis = any(rw.fcs in ("aiv", "av") for rw in missile_rws)
            all_artemis = all(rw.fcs in ("aiv", "av") for rw in missile_rws)
            if has_artemis and not all_artemis:
                violations.append(prefix + TIC_RULES[4])

        # Rules 5, 6, 7, 9, 10 — special-flag compatibility
        reported: set[int] = set()
        for flag, rule_num in _FLAG_TO_RULE.items():
            if rule_num in reported:
                continue
            flag_count = sum(1 for rw in weapons if rw.weapon.has_special(flag))
            if 0 < flag_count < len(weapons):
                violations.append(prefix + TIC_RULES[rule_num])
                reported.add(rule_num)

        # Rule 8 — rapid-fire only with rapid-fire
        rac = sum(1 for rw in weapons if int(rw.weapon.useR or 0) > 0)
        if 0 < rac < len(weapons):
            violations.append(prefix + TIC_RULES[8])

        # Rule 11 — one-shot only with one-shot
        os_count = sum(1 for rw in weapons if rw.one_shot)
        if 0 < os_count < len(weapons):
            violations.append(prefix + TIC_RULES[11])

        # Rule 1 — damage budget ≤ 5 Override points (≤ 14 max missile damage)
        combined = math.ceil(grp.damage / 3) + grp.damage_m
        if combined > 5:
            violations.append(prefix + TIC_RULES[1])
        else:
            # Non-var missile weapons
            missile_ws = [
                rw for rw in weapons
                if rw.weapon.damageM > 0 and not rw.weapon.has_special("var")
            ]
            # Var+missile weapons (MML, ATM, eLRM) — their damageMax
            # is the HE/peak ammo value, not varPBS
            var_missile_ws = [
                rw for rw in weapons
                if rw.weapon.damageM > 0 and rw.weapon.has_special("var")
            ]
            if missile_ws or var_missile_ws:
                max_dmg = sum(
                    rw.weapon.damage_value(rw.tonnage) + rw.weapon.damageAdj
                    for rw in missile_ws
                )
                max_dmg += sum(
                    rw.weapon.damage_value(rw.tonnage) + rw.weapon.damageAdj
                    for rw in var_missile_ws
                )
                if math.ceil(max_dmg / 3) > 14:
                    violations.append(prefix + TIC_RULES[1])

        # Rule 13 — AC/LAC weapons must share the same special ammo type
        ac_rws = [rw for rw in weapons if rw.weapon.useAmmo in _AC_AMMO_TYPES]
        if len(ac_rws) > 1:
            ammo_types = {rw.ammo_type for rw in ac_rws}
            if len(ammo_types) > 1:
                violations.append(prefix + TIC_RULES[13])

    return violations


# ── Public API ────────────────────────────────────────────────────────────────

def resolve_weapons(
    unit: AbstractUnit,
    tonnage: int = 0,
    profile=None,
) -> list[ResolvedWeapon]:
    """Look up weapon definitions and return resolved weapon list.

    FCS (Artemis IV/V) is linked per-weapon by the parsers via UnitWeapon.fcs.
    Targeting Computer (-1 to range brackets) applied to weapons with useTC=1.
    profile: optional ConversionProfile — when provided, weapon_overrides are applied.
    """
    if profile is not None:
        _engine = ConversionEngine(profile)
    else:
        _engine = None

    has_tc = unit.is_equipped_with("tc")
    resolved = []
    for uw in unit.weapons:
        try:
            w = DataStore.weapon(uw.weapon_key)
        except KeyError:
            continue
        if _engine is not None:
            w = _engine.apply_weapon_overrides(w)
        resolved.append(ResolvedWeapon(
            unit_weapon=uw,
            weapon=w,
            tic=uw.tic,
            location=uw.location,
            ammo_type=uw.ammo_type,
            one_shot=uw.one_shot,
            tonnage=tonnage,
            fcs=uw.fcs,
            tc=has_tc and bool(w.useTC),
        ))
    return resolved


def group_weapons(resolved: list[ResolvedWeapon]) -> list[ResolvedWeapon]:
    """Merge identical weapon entries (same key + location + ammo + tic + fcs + tc) into count > 1."""
    seen: dict[tuple, ResolvedWeapon] = {}
    for rw in resolved:
        key = (rw.unit_weapon.weapon_key, rw.location, rw.ammo_type, rw.tic, rw.one_shot, rw.fcs, rw.tc)
        if key in seen:
            seen[key].count += 1
        else:
            seen[key] = ResolvedWeapon(
                unit_weapon=rw.unit_weapon,
                weapon=rw.weapon,
                tic=rw.tic,
                location=rw.location,
                ammo_type=rw.ammo_type,
                one_shot=rw.one_shot,
                count=1,
                tonnage=rw.tonnage,
                fcs=rw.fcs,
                tc=rw.tc,
            )
    return list(seen.values())


_LOCATION_ORDER = [
    "LA", "RA", "T", "HD", "LL", "RL",
    "(R) T", "(R) HD", "(R) LL", "(R) RL",
    "FR", "LS", "RS", "RR", "TU", "RO", "N", "LW", "RW", "AFT",
]


def _loc_priority(loc: str) -> int:
    try:
        return _LOCATION_ORDER.index(loc)
    except ValueError:
        return 99


def sort_weapons(resolved: list[ResolvedWeapon]) -> list[ResolvedWeapon]:
    """Sort weapons for Override display order."""
    def sort_key(rw: ResolvedWeapon):
        w = rw.weapon
        return (
            rw.tic,
            -int(w.rangeX),
            -int(w.rangeL),
            -int(w.rangeM),
            -int(w.rangeS),
            -rw.damage_display,
            w.heat_value(),
            _loc_priority(rw.location),
            w.name,
        )
    return sorted(resolved, key=sort_key)


_TORSO_FRONT_LOCS = frozenset({"CT", "LT", "RT", "T"})
_TORSO_REAR_LOCS  = frozenset({"CTR", "LTR", "RTR", "(R) T"})


def _format_locations(locations: list[str]) -> str:
    """Merge torso zone locations into 'T' / '(R) T'; join others by comma."""
    has_front = False
    has_rear  = False
    other: list[str] = []
    seen: set[str] = set()
    for loc in locations:
        u = loc.upper()
        if u in _TORSO_FRONT_LOCS:
            has_front = True
        elif u in _TORSO_REAR_LOCS:
            has_rear = True
        elif u not in seen:
            other.append(loc)
            seen.add(u)
    parts = other[:]
    if has_front:
        parts.append("T")
    if has_rear:
        parts.append("(R) T")
    return ", ".join(parts)


def _build_tic_name(rws: list[ResolvedWeapon]) -> tuple[str, str]:
    """Build combined weapon name string and ammo type for a TIC group.

    Returns (combined_name, ammo_type).
    """
    # Count weapons and track per-name flags
    name_counts: dict[str, int] = {}
    name_ai: dict[str, bool] = {}
    name_os: dict[str, bool] = {}
    name_rf: dict[str, bool] = {}
    name_tc: dict[str, bool] = {}
    name_fcs: dict[str, str | None] = {}
    for rw in rws:
        n = rw.weapon.name
        name_counts[n] = name_counts.get(n, 0) + 1
        if rw.weapon.has_special("ai"):
            name_ai[n] = True
        if rw.one_shot or rw.weapon.has_special("os"):
            name_os[n] = True
        if int(rw.weapon.useR or 0) > 0:
            name_rf[n] = True
        if rw.tc:
            name_tc[n] = True
        if rw.fcs:
            name_fcs[n] = rw.fcs

    name_parts = []
    for n, cnt in name_counts.items():
        suffix = ""
        if name_fcs.get(n) == "aiv":
            suffix += " (AIV)"
        elif name_fcs.get(n) == "av":
            suffix += " (AV)"
        if name_rf.get(n):
            suffix += " (RF)"
        if name_ai.get(n):
            suffix += " (AI)"
        if name_os.get(n):
            suffix += " (OS)"
        if name_tc.get(n):
            suffix += " (TC)"
        name_parts.append(
            f"×{cnt} {n}{suffix}" if cnt > 1 else f"{n}{suffix}"
        )

    combined_name = ", ".join(name_parts)
    ammo = _group_ammo_type(rws)
    if ammo in _AMMO_SUFFIX:
        combined_name += _AMMO_SUFFIX[ammo]

    return combined_name, ammo


def _build_tic_damage(rws: list[ResolvedWeapon], ammo: str, group: TicGroup) -> str:
    """Compute damage string for a TIC group, handling Flechette special case."""
    if ammo != "Flechette":
        return group.damage_str

    flechette_total = sum(
        math.floor(rw.weapon.damage_value(rw.tonnage) / 2)
        for rw in rws
    )
    flechette_override = math.ceil(flechette_total / 3)
    standard_override = math.ceil(
        sum(rw.weapon.damage_value(rw.tonnage) for rw in rws) / 3
    )
    ai_bonus = standard_override - flechette_override
    if ai_bonus > 0:
        return f"{flechette_override} ({ai_bonus} + AI)"
    return str(flechette_override)


def build_tic_rows(resolved: list[ResolvedWeapon], heat_scale_max: int = 5) -> list[dict]:
    """Produce one row dict per occupied TIC slot (combined damage, heat, locations)."""
    tic_map: dict[int, list[ResolvedWeapon]] = {}
    for rw in resolved:
        tic_map.setdefault(rw.tic, []).append(rw)

    # Build groups and compute damage sort key
    tic_groups: list[tuple[float, int, TicGroup, list[ResolvedWeapon]]] = []
    for tic_num, rws in tic_map.items():
        group = TicGroup(weapons=rws)
        sort_dmg = group.sort_damage
        tic_groups.append((sort_dmg, tic_num, group, rws))

    # Sort descending by damage, ascending by tic_num for ties
    tic_groups.sort(key=lambda x: (-x[0], x[1]))

    rows = []
    divisor = (255 - heat_scale_max) / (7 * heat_scale_max + 15)

    for _sort_dmg, _tic_num, group, rws in tic_groups:
        combined_name, ammo = _build_tic_name(rws)
        damage_str = _build_tic_damage(rws, ammo, group)
        range_offset = -1 if ammo == "Precision" else (1 if ammo == "AP" else 0)
        total_heat = group.heat
        heat_display = str(int(total_heat / divisor + 0.5)) if total_heat else "—"

        rows.append({
            "name":     combined_name,
            "damage":   damage_str,
            "_raw_damage": group.damage,
            "heat":     heat_display,
            "location": _format_locations([rw.location for rw in rws]),
            "rangePB":  _fmt_rng(_adjust_range(group.range_pb, range_offset)),
            "rangeS":   _fmt_rng(_adjust_range(group.range_s,  range_offset)),
            "rangeM":   _fmt_rng(_adjust_range(group.range_m,  range_offset)),
            "rangeL":   _fmt_rng(_adjust_range(group.range_l,  range_offset)),
            "rangeX":   _fmt_rng(_adjust_range(group.range_x,  range_offset)),
        })

    return rows


def ba_squad_damage_strs(resolved: list[ResolvedWeapon], squad_size: int) -> list[str]:
    """Return per-trooper-count damage display strings for BA TIC groups.

    Mirrors JS destinyWeapons (lines 9040-9057):
      For each trooper count N..1, create a temporary TicGroup with N copies
      of each weapon, then compute the damage display string via TIC grouping rules.
    Returns list [damage@N, damage@N-1, ..., damage@1].
    """
    tic_map: dict[int, list[ResolvedWeapon]] = {}
    for rw in resolved:
        tic_map.setdefault(rw.tic, []).append(rw)

    tic_damages: list[list[str]] = []
    for tic_num in sorted(tic_map):
        rws = tic_map[tic_num]
        strs = []
        for n in range(squad_size, 0, -1):
            copies: list[ResolvedWeapon] = []
            for rw in rws:
                for _ in range(n):
                    copies.append(rw)
            temp = TicGroup(weapons=copies)
            strs.append(temp.damage_str)
        tic_damages.append(strs)

    # Sort by damage (same order as build_tic_rows: descending by sort_damage)
    group_sort = []
    for i, tic_num in enumerate(sorted(tic_map)):
        raw_group = TicGroup(weapons=tic_map[tic_num])
        group_sort.append((raw_group.sort_damage, i))
    group_sort.sort(key=lambda x: -x[0])

    return [tic_damages[idx] for _, idx in group_sort]


# ── Location-aware pre-grouping (Rules 1-3) ────────────────────────────────────


def _override_damage_single(rw: ResolvedWeapon) -> int:
    """Per-weapon Override damage when alone in a TIC. Used by Rule 2."""
    w = rw.weapon
    d = w.damage_value(rw.tonnage)
    if w.has_special("var"):
        return math.ceil(w.varPBSdamage / 3)
    if w.damageM > 0:
        return w.damageM - w.shiftM
    return math.ceil(d / 3)


def _chunk_fits(chunk: list[ResolvedWeapon]) -> bool:
    """Check if homogeneous chunk fits the TIC damage budget.

    Rule 1: combined Override damage <= 5, and max missile damage <= 14.
    """
    grp = TicGroup(weapons=list(chunk))
    combined = math.ceil(grp.damage / 3) + grp.damage_m
    if combined > 5:
        return False

    # Check max missile damage for var+missile weapons (MML, ATM, eLRM)
    max_dmg = sum(
        rw.weapon.damage_value(rw.tonnage) + rw.weapon.damageAdj
        for rw in chunk
        if rw.weapon.damageM > 0
    )
    if max_dmg > 0 and math.ceil(max_dmg / 3) > 14:
        return False

    return True


def _split_into_even_groups(weapons: list[ResolvedWeapon]) -> list[list[ResolvedWeapon]]:
    """Rule 3: split N identical weapons into fewest even-sized groups.

    Prefers exactly equal groups (N % G == 0). Falls back to size diff <= 1
    when the only equal split gives all singletons (N is prime and cap-limited).
    """
    if not weapons:
        return []

    N = len(weapons)

    # Pass 1: exactly equal groups (fewest G first)
    for G in range(1, N + 1):
        if N % G != 0:
            continue
        size = N // G
        if _chunk_fits(weapons[:size]):
            result = [weapons[i:i + size] for i in range(0, N, size)]
            # If only equal split is all singletons, try uneven below
            if size == 1 and N > 1:
                break
            return result

    # Pass 2: allow size diff <= 1 (fewest G first)
    for G in range(1, N + 1):
        base = N // G
        rem = N % G
        sizes = [base + 1] * rem + [base] * (G - rem)
        if not _chunk_fits(weapons[:sizes[0]]):
            continue
        chunks = []
        idx = 0
        for sz in sizes:
            chunks.append(weapons[idx:idx + sz])
            idx += sz
        return chunks

    return [[w] for w in weapons]


def _pre_assign_location_groups(
    resolved: list[ResolvedWeapon],
) -> list[list[ResolvedWeapon]]:
    """Pre-assign weapons into TIC chunks based on location grouping rules.

    Step A: group by (weapon.key, location, ammo_type, one_shot).
    Step B: split each group evenly (Rule 3, Rule 1 implicit).
    Step C: merge eligible chunks from opposite locations (Rule 2).
    """
    # Step A: group identical weapons by location
    groups: dict[tuple, list[ResolvedWeapon]] = defaultdict(list)
    for rw in resolved:
        w = rw.weapon
        if w.type == "P":
            continue  # physical weapons handled by greedy
        key = (w.key, rw.location, rw.ammo_type, rw.one_shot)
        groups[key].append(rw)

    # Step B: split each group into even chunks
    all_chunks: list[list[ResolvedWeapon]] = []
    for weapons in groups.values():
        all_chunks.extend(_split_into_even_groups(weapons))

    if not all_chunks:
        return []

    # Step C: cross-location merging (Rule 2)
    # Separate into merge-eligible (per-weapon Override <= 2) and ineligible
    eligible: list[list[ResolvedWeapon]] = []
    ineligible: list[list[ResolvedWeapon]] = []

    for chunk in all_chunks:
        if chunk and _override_damage_single(chunk[0]) <= 2:
            eligible.append(chunk)
        else:
            ineligible.append(chunk)

    # Group eligible chunks by (weapon_key, chunk_size, ammo_type, one_shot)
    eligible_groups: dict[tuple, dict[str, list[list[ResolvedWeapon]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for chunk in eligible:
        rw = chunk[0]
        group_key = (rw.weapon.key, len(chunk), rw.ammo_type, rw.one_shot)
        eligible_groups[group_key][rw.location].append(chunk)

    merged: list[list[ResolvedWeapon]] = []
    used: set[int] = set()  # track merged chunks by id

    for group_key, loc_chunks in eligible_groups.items():
        locations = list(loc_chunks.keys())
        paired: set[str] = set()

        for loc in locations:
            if loc in paired:
                continue
            # LS↔RS and LW↔RW are vehicle/fighter side locations — never group across sides
            if loc in _LEFT_LOCS or loc in _RIGHT_LOCS:
                continue
            opp = _OPPOSITE_LOCS.get(loc, "")
            if opp not in loc_chunks:
                continue

            # Try to pair one chunk from each location
            chunks_a = [c for i, c in enumerate(loc_chunks[loc]) if id(c) not in used]
            chunks_b = [c for i, c in enumerate(loc_chunks[opp]) if id(c) not in used]

            while chunks_a and chunks_b:
                ca, cb = chunks_a[0], chunks_b[0]
                candidate = ca + cb
                if _chunk_fits(candidate):
                    merged.append(candidate)
                    used.add(id(ca))
                    used.add(id(cb))
                    chunks_a.pop(0)
                    chunks_b.pop(0)
                else:
                    break

            paired.add(loc)
            paired.add(opp)

    # Collect unmerged eligible chunks
    for chunk in eligible:
        if id(chunk) not in used:
            merged.append(chunk)

    return merged + ineligible


def auto_assign_tics(
    resolved: list[ResolvedWeapon],
    is_ba: bool = False,
) -> list[ResolvedWeapon]:
    """
    Auto-assign TIC values.

    Phase 1: Pre-assign location-based groups (Rules 1-3).
    Phase 2: Greedy assignment for remaining weapons using the scoring
             algorithm from card_gen.js autoGroupWeapons / _scoreWeaponForTicV5.

    For Battle Armor (is_ba=True), each weapon gets its own TIC — no grouping.
    """
    if is_ba:
        for i, rw in enumerate(resolved):
            rw.tic = i + 1
            rw.unit_weapon.tic = rw.tic
        return resolved

    NUM_TICS = 9
    tics = [TicGroup() for _ in range(NUM_TICS)]

    # Phase 1: Pre-assign location-based groups
    chunks = _pre_assign_location_groups(resolved)
    pre_assigned: set[int] = set()

    for tic_idx, chunk in enumerate(chunks):
        if tic_idx >= NUM_TICS:
            break
        for rw in chunk:
            rw.tic = tic_idx + 1
            rw.unit_weapon.tic = rw.tic
            tics[tic_idx].weapons.append(rw)
            pre_assigned.add(id(rw))

    # Phase 2: Greedy on remaining weapons (all TICs available including pre-filled)
    remaining = [rw for rw in resolved if id(rw) not in pre_assigned]
    if remaining:
        ordered = sorted(remaining, key=_sort_key_v5)

        for rw in ordered:
            scores = [_score_weapon_for_tic(rw, tics[i], i) for i in range(NUM_TICS)]
            best = scores.index(max(scores))
            rw.tic = best + 1
            tics[best].weapons.append(rw)
            rw.unit_weapon.tic = rw.tic

    return resolved

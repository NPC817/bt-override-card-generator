from __future__ import annotations
import dataclasses
import math
from ..models.weapon import Weapon
from ..settings.profile import ConversionProfile
from ..utils.math import _r


class ConversionEngine:
    def __init__(self, profile: ConversionProfile | None = None):
        self.profile = profile or ConversionProfile.default()

    # ── Armor ────────────────────────────────────────────────────────────────

    def convert_armor(self, raw: int, divisor: float | None = None) -> int:
        d = divisor if divisor is not None else self.profile.mech_armor_divisor
        return max(_r(raw / d), 1)

    def convert_mech_torso_armor(self, ct: int, lt: int, rt: int) -> int:
        """Combined torso zone displayed on card (CT+LT+RT ÷ 6)."""
        return max(_r((ct + lt + rt) / (self.profile.mech_armor_divisor * 2)), 1)

    def convert_mech_torso_rear_armor(self, ctr: int, ltr: int, rtr: int) -> int:
        return max(_r((ctr + ltr + rtr) / (self.profile.mech_armor_divisor * 2)), 1)

    def convert_head_armor(self, raw: int) -> int:
        """Stepped head armor scale (default Override behavior)."""
        if raw <= 2:
            return 1
        if raw <= 5:
            return 2
        if raw <= 7:
            return 3
        return 4

    def convert_vehicle_armor(self, raw: int) -> int:
        return max(_r(raw / self.profile.vehicle_armor_divisor), 1)

    # ── Structure ─────────────────────────────────────────────────────────────

    def convert_structure(self, raw: int) -> int:
        return max(_r(raw / 3), 1)

    def convert_vehicle_structure(self, tonnage: float) -> int:
        return max(_r(math.ceil(tonnage / 10) / 3), 1)

    # ── Heat ─────────────────────────────────────────────────────────────────

    def convert_heat_sinks(self, sinks: int, is_dhs: bool = False) -> int:
        effective = sinks * 2 if is_dhs else sinks
        return max(_r(effective / self.profile.heat_sink_divisor), 0)

    def convert_jump_heat(self) -> int:
        """Classic BT minimum jump heat (3) scaled by the heat divisor."""
        return max(_r(3 / self.profile.heat_sink_divisor), 1)

    def heat_scale_pips(self, heat_value: int) -> int:
        """Map a weapon heat value to pip count on the scaled heat track."""
        if self.profile.heat_scale_max <= 0:
            return 0
        pips = _r(heat_value * 5 / self.profile.heat_scale_max)
        return max(0, min(pips, 5))

    # ── Movement ─────────────────────────────────────────────────────────────

    def convert_move(self, mp: int) -> int:
        return max(_r(mp * self.profile.move_scale_multiplier), 0)

    # ── Weapons ──────────────────────────────────────────────────────────────

    def apply_weapon_overrides(self, weapon: Weapon) -> Weapon:
        """Return a copy of the weapon with profile overrides applied."""
        overrides = self.profile.weapon_overrides.get(weapon.key, {})
        if not overrides:
            return weapon
        fields = {f.name for f in dataclasses.fields(weapon)}
        updates = {k: v for k, v in overrides.items() if k in fields}
        return dataclasses.replace(weapon, **updates)

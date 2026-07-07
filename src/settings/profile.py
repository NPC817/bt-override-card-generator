from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class ConversionProfile:
    name: str = "Default"
    mech_armor_divisor: float = 3.0
    vehicle_armor_divisor: float = 4.0
    aero_armor_divisor: float = 4.0
    heat_scale_max: int = 5          # pips on heat track (1-30)
    move_scale_multiplier: float = 1.0
    weapon_overrides: dict = field(default_factory=dict)  # {weapon_key: {field: value}}
    track_ammo: bool = False      # enable ammo shot-count display on cards
    show_tracking_pips: bool = True  # show hex pips inline (when track_ammo enabled)

    def __post_init__(self) -> None:
        """Clamp heat_scale_max to valid range 1-30."""
        self.heat_scale_max = max(1, min(30, self.heat_scale_max))

    @property
    def heat_sink_divisor(self) -> float:
        # Rational curve through (5,5),(15,2),(30,1): exact ÷5 at scale=5, ÷1 at scale=30
        return (255 - self.heat_scale_max) / (7 * self.heat_scale_max + 15)

    def is_default(self) -> bool:
        return self.name == "Default"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "mech_armor_divisor": self.mech_armor_divisor,
            "vehicle_armor_divisor": self.vehicle_armor_divisor,
            "aero_armor_divisor": self.aero_armor_divisor,
            "heat_scale_max": self.heat_scale_max,
            "move_scale_multiplier": self.move_scale_multiplier,
            "weapon_overrides": dict(self.weapon_overrides),
            "track_ammo": self.track_ammo,
            "show_tracking_pips": self.show_tracking_pips,
        }

    @classmethod
    def from_dict(cls, data: dict) -> ConversionProfile:
        return cls(
            name=data.get("name", "Custom"),
            mech_armor_divisor=float(data.get("mech_armor_divisor", 3.0)),
            vehicle_armor_divisor=float(data.get("vehicle_armor_divisor", 4.0)),
            aero_armor_divisor=float(data.get("aero_armor_divisor", 4.0)),
            heat_scale_max=int(data.get("heat_scale_max", 5)),
            move_scale_multiplier=float(data.get("move_scale_multiplier", 1.0)),
            weapon_overrides=dict(data.get("weapon_overrides", {})),
            track_ammo=bool(data.get("track_ammo", False)),
            show_tracking_pips=bool(data.get("show_tracking_pips", True)),
        )

    @classmethod
    def default(cls) -> ConversionProfile:
        return cls(name="Default")

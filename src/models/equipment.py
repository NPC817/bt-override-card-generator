from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Equipment:
    key: str
    name: str
    fullname: str
    tech: str = "Mixed"
    hasLoc: bool = False
    omit: bool = False
    isLimited: bool = False
    fixedLocation: str = ""
    subtypes: dict = field(default_factory=dict)  # subtype_key -> display_name
    specific_subtype: str = ""   # e.g. "LRM20", "AC5" for ammo
    shots_per_ton: int = 0       # shots per ton of ammo (0 = untracked)

    @classmethod
    def from_dict(cls, key: str, data: dict) -> Equipment:
        return cls(
            key=key,
            name=data["name"],
            fullname=data.get("fullname", data["name"]),
            tech=data.get("tech", "Mixed"),
            hasLoc=bool(data.get("hasLoc", False)),
            omit=bool(data.get("omit", False)),
            isLimited=bool(data.get("isLimited", False)),
            fixedLocation=data.get("fixedLocation", ""),
            subtypes=dict(data.get("subtypes", {})),
            specific_subtype=data.get("specific_subtype", ""),
            shots_per_ton=int(data.get("shots_per_ton", 0)),
        )

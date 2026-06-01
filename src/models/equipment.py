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
        )

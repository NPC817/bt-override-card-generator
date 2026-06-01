from __future__ import annotations
from dataclasses import dataclass
from math import ceil
from typing import Any


@dataclass
class Weapon:
    key: str
    name: str
    fullname: str
    tech: str          # "IS", "Clan", "Mixed"
    type: str          # "B", "E", "M", "P"
    damage: Any        # int or callable(tonnage) -> int
    heat: Any          # int or str "0"
    crits: Any         # int or callable(tonnage) -> int
    rangePB: int = 0
    rangeS: int = 0
    rangeM: int = 0
    rangeL: int = 0
    rangeX: int = 9

    # Optional fields
    damageAdj: int = 0
    damageM: int = 0
    shiftM: int = 0
    varPBSdamage: int = 0
    varMdamage: int = 0
    varLXdamage: int = 0

    useH: Any = 0      # heat factor override
    useC: Any = 0      # cluster/flechette capable
    useR: Any = 0      # ROF for RAC
    useM: int = 0      # medium range damage type
    useTC: int = 0     # targeting computer compatible
    useAmmo: str = ""  # ammo category key
    useFCS: str = ""   # fire control: "aiv", "av", "apollo"
    useLOS: bool = False
    specials: str = ""  # comma-separated special flags
    baOnly: bool = False

    def damage_value(self, tonnage: int = 0) -> int:
        if callable(self.damage):
            return self.damage(tonnage)
        return int(self.damage)

    def crits_value(self, tonnage: int = 0) -> int:
        if callable(self.crits):
            return self.crits(tonnage)
        return int(self.crits)

    def heat_value(self) -> int:
        try:
            return int(self.heat)
        except (ValueError, TypeError):
            return 0

    def damage_max(self, tonnage: int = 0) -> int:
        return self.damage_value(tonnage) + self.damageAdj

    _SPECIAL_TOKENS = {"ai", "var", "sbg", "os"}

    def has_special(self, flag: str) -> bool:
        if not self.specials:
            return False
        # Try comma-separated first
        if flag in self.specials.split(","):
            return True
        # Handle concatenated tokens (e.g. "varai" = var + ai)
        remaining = self.specials
        for token in sorted(self._SPECIAL_TOKENS, key=len, reverse=True):
            if token in remaining:
                if token == flag:
                    return True
                remaining = remaining.replace(token, "", 1)
        return False

    @classmethod
    def from_dict(cls, key: str, data: dict) -> Weapon:
        damage_raw: Any = data.get("damage", 0)
        if "damageTonnageDiv" in data:
            div = float(data["damageTonnageDiv"])
            damage_raw = lambda t, d=div: max(ceil((t or 0) / d), 1)
        crits_raw: Any = data.get("crits", 1)
        if "critsTonnageDiv" in data:
            div = float(data["critsTonnageDiv"])
            crits_raw = lambda t, d=div: max(ceil((t or 0) / d), 1)

        return cls(
            key=key,
            name=data["name"],
            fullname=data.get("fullname", data["name"]),
            tech=data.get("tech", "Mixed"),
            type=data.get("type", "E"),
            damage=damage_raw,
            heat=data.get("heat", 0),
            crits=crits_raw,
            rangePB=int(data.get("rangePB", 0)),
            rangeS=int(data.get("rangeS", 0)),
            rangeM=int(data.get("rangeM", 0)),
            rangeL=int(data.get("rangeL", 0)),
            rangeX=int(data.get("rangeX", 9)),
            damageAdj=int(data.get("damageAdj", 0)),
            damageM=int(data.get("damageM", 0)),
            shiftM=int(data.get("shiftM", 0)),
            varPBSdamage=int(data.get("varPBSdamage", 0)),
            varMdamage=int(data.get("varMdamage", 0)),
            varLXdamage=int(data.get("varLXdamage", 0)),
            useH=data.get("useH", 0),
            useC=data.get("useC", 0),
            useR=data.get("useR", 0),
            useM=int(data.get("useM", 0)),
            useTC=int(data.get("useTC", 0)),
            useAmmo=data.get("useAmmo", ""),
            useFCS=data.get("useFCS", ""),
            useLOS=bool(data.get("useLOS", False)),
            specials=data.get("specials", ""),
            baOnly=bool(data.get("baOnly", False)),
        )

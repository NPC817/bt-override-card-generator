from __future__ import annotations


def _r(v: float) -> int:
    """Round half-up (0.5 always rounds up), avoiding Python's banker's round."""
    return int(v + 0.5)


def _tmm(mp: int, is_vtol: bool = False) -> int:
    """Override TMM formula: double the MP then threshold (per card_gen.js).

    VTOL units get +1 to their TMM value.
    """
    a = 2 * mp
    base = 0 if a < 5 else 1 if a < 9 else 2 if a < 13 else 3 if a < 19 else 4 if a < 35 else 5
    return base + (1 if is_vtol else 0)

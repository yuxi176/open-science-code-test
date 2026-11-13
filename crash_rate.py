"""Calculate crash rates using vehicle miles traveled as exposure."""

import math


def crash_rate_per_million_vmt(crashes: int, vehicle_miles_traveled: float) -> float:
    """Return crashes per million vehicle miles traveled.

    Crashes must be a nonnegative integer; exposure must be positive and finite.
    """
    if isinstance(crashes, bool) or not isinstance(crashes, int) or crashes < 0:
        raise ValueError("crashes must be a nonnegative integer")
    if not math.isfinite(vehicle_miles_traveled) or vehicle_miles_traveled <= 0:
        raise ValueError("vehicle miles traveled must be positive and finite")
    return crashes / vehicle_miles_traveled * 1_000_000

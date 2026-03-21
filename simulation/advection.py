import numpy as np
import math


def apply_advection(grid, wind_speed_kmh, wind_direction_deg):
    """
    Moves oil in wind direction with guaranteed minimum drift.
    Prevents zero-movement cases for shallow angles.
    """

    # Convert wind direction to radians
    direction = math.radians(wind_direction_deg)

    # Continuous components
    dx_cont = math.cos(direction)
    dy_cont = math.sin(direction)

    # 🔧 FIX: enforce minimum drift
    dx = int(math.copysign(1, dx_cont)) if abs(dx_cont) > 0.1 else 1
    dy = int(math.copysign(1, dy_cont)) if abs(dy_cont) > 0.1 else 1

    # Apply directional shift
    shifted = np.roll(grid, shift=dx, axis=1)
    shifted = np.roll(shifted, shift=dy, axis=0)

    # Scale advection effect (kept simple & explainable)
    speed_factor = min(wind_speed_kmh / 40, 1.0)

    return shifted * speed_factor

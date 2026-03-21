import numpy as np
from simulation.grid import OceanGrid
from simulation.diffusion import apply_diffusion
from simulation.advection import apply_advection
from simulation.timestep import SimulationClock


class OilSpillSimulation:
    def __init__(self, wind_speed_kmh=20, wind_direction_deg=45):
        self.grid = OceanGrid()
        self.clock = SimulationClock()
        self.wind_speed = wind_speed_kmh
        self.wind_direction = wind_direction_deg

        # Initialize spill at center
        c = self.grid.center_index()
        self.grid.grid[c, c] = 100.0

    def step(self):
        self.grid.grid = apply_diffusion(self.grid.grid)
        self.grid.grid = apply_advection(
            self.grid.grid,
            self.wind_speed,
            self.wind_direction
        )
        time = self.clock.tick()
        return time

    def spread_radius_km(self):
        """
        Approximate spread radius based on diffused oil cells.
        Lower threshold ensures spread does not stall.
        """
        # 🔧 FIX: lowered threshold from >1 to >0.05
        non_zero = np.argwhere(self.grid.grid > 0.05)

        if len(non_zero) == 0:
            return 0.0

        c = self.grid.center_index()
        max_dist = max(
            ((i - c) ** 2 + (j - c) ** 2) ** 0.5
            for i, j in non_zero
        )

        return round(max_dist * self.grid.resolution_km, 2)

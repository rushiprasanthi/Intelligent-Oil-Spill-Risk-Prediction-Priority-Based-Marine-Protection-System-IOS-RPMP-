# simulation/grid.py

import numpy as np

class OceanGrid:
    def __init__(self, size_km=200, resolution_km=2):
        """
        size_km: total grid size (square)
        resolution_km: size of each cell
        """
        self.size_km = size_km
        self.resolution_km = resolution_km
        self.cells = int(size_km / resolution_km)

        # Oil concentration grid
        self.grid = np.zeros((self.cells, self.cells))

    def center_index(self):
        return self.cells // 2

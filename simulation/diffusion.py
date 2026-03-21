# simulation/diffusion.py

import numpy as np

def apply_diffusion(grid, diffusion_rate=0.15):
    """
    Simple diffusion: spreads oil to neighboring cells.
    """
    new_grid = grid.copy()

    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            spread = diffusion_rate * grid[i, j]
            new_grid[i, j] -= spread
            new_grid[i+1, j] += spread / 4
            new_grid[i-1, j] += spread / 4
            new_grid[i, j+1] += spread / 4
            new_grid[i, j-1] += spread / 4

    return new_grid

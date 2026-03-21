from simulation.spread_model import OilSpillSimulation

sim = OilSpillSimulation(
    wind_speed_kmh=30,
    wind_direction_deg=60
)

for step in range(5):
    t = sim.step()
    radius = sim.spread_radius_km()
    print(f"Hour {t}: Spread radius ≈ {radius} km")

print("Drift direction (deg):", sim.wind_direction)

from simulation.spread_model import OilSpillSimulation

def test_spread_increases():
    sim = OilSpillSimulation(
        wind_speed_kmh=20,
        wind_direction_deg=45
    )

    r1 = sim.spread_radius_km()
    sim.step()
    r2 = sim.spread_radius_km()

    assert r2 > r1

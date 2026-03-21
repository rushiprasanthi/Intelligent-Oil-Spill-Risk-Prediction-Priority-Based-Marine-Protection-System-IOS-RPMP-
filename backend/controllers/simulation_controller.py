from simulation.spread_model import OilSpillSimulation


def run_simulation(spill):
    """
    Run oil spill simulation long enough
    to allow interaction with sensitive zones.

    This is a decision-support simulation,
    not a full ocean physics model.
    """

    # Fixed environmental conditions for demo stability
    wind_speed_kmh = 30
    wind_direction_deg = 60

    sim = OilSpillSimulation(
        wind_speed_kmh=wind_speed_kmh,
        wind_direction_deg=wind_direction_deg
    )

    # Run simulation for 8 hours
    for _ in range(8):
        sim.step()

    spread_radius = sim.spread_radius_km()

    return {
        "spread_radius_km": spread_radius,
        "wind_speed": wind_speed_kmh,
        "wind_direction": wind_direction_deg,

        # ✅ FIX: frontend expects this field
        # Containment direction approximated as wind direction
        "projected_direction_deg": wind_direction_deg,

        "time_hours": 8
    }

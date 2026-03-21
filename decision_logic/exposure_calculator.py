# decision_logic/exposure_calculator.py

import math

def calculate_exposure(spill_lat, spill_lng, zone_lat, zone_lng, spread_radius_km):
    """
    Returns exposure probability (0–1) based on distance between spill and zone.
    """

    # Haversine distance (km)
    R = 6371
    lat1, lon1 = math.radians(spill_lat), math.radians(spill_lng)
    lat2, lon2 = math.radians(zone_lat), math.radians(zone_lng)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    distance = 2 * R * math.asin(math.sqrt(a))

    if distance > spread_radius_km:
        return 0.0

    exposure = max(0.0, 1 - (distance / spread_radius_km))
    return round(exposure, 3)

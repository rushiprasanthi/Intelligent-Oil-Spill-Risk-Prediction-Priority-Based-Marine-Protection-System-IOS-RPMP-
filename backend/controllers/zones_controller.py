import math
from decision_logic.exposure_calculator import calculate_exposure
from backend.controllers.zones_loader import get_cleaned_zones


# Use the cleaned zones loaded at startup
_ZONES_CACHE = get_cleaned_zones()


def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0) ** 2
    dist = 2 * R * math.asin(math.sqrt(a))
    return round(dist, 2)


def _proximity_level(distance_km):
    if distance_km <= 50:
        return "Critical Near"
    if distance_km <= 150:
        return "High Risk Near"
    if distance_km <= 300:
        return "Moderate Near"
    return "Distant"


def evaluate_zones(spill_lat, spill_lng, simulation_output, risk_output):
    """
    Evaluate cleaned zones relative to the spill origin.

    Applies 5000 km filter and hotspot rules. Returns list of zone analysis dicts
    (only zones within 5000 km).
    """
    results = []

    spread_radius = None
    try:
        spread_radius = simulation_output.get("spread_radius_km")
    except Exception:
        spread_radius = None

    for z in _ZONES_CACHE:
        zid = z.get("zone_id")
        name = z.get("name")
        country = z.get("country")
        zlat = z.get("lat")
        zlon = z.get("lng")
        sensitivity = z.get("sensitivity", 5)

        if zlat is None or zlon is None:
            continue

        distance_km = haversine_km(spill_lat, spill_lng, zlat, zlon)

        # 5000 km filter: skip far-away zones
        if distance_km > 5000:
            continue

        proximity = _proximity_level(distance_km)

        # Use existing exposure calculator if spread_radius known
        exposure_prob = 0.0
        try:
            if spread_radius:
                exposure_prob = calculate_exposure(spill_lat, spill_lng, zlat, zlon, spread_radius)
        except Exception:
            exposure_prob = 0.0

        # Hotspot rules (updated): priority == P1 OR exposure >= 0.6 OR (distance <=150 and sensitivity >=8)
        is_hotspot = False
        try:
            if risk_output and risk_output.get("priority") == "P1":
                is_hotspot = True
            if exposure_prob >= 0.6:
                is_hotspot = True
            if distance_km <= 150 and sensitivity >= 8:
                is_hotspot = True
        except Exception:
            is_hotspot = False

        results.append({
            "zone_id": zid,
            "name": name,
            "country": country,
            "lat": zlat,
            "lng": zlon,
            "sensitivity": sensitivity,
            "distance_km": distance_km,
            "proximity_level": proximity,
            "is_hotspot": bool(is_hotspot),
            "exposure_probability": exposure_prob
        })

    return results

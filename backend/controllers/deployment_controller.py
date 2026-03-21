import json
import math

PORTS_FILE = "data/ports/global_ports.json"
SHIP_SPEED_KMH = 30


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (
        math.sin(dlat / 2) ** 2 +
        math.cos(math.radians(lat1)) *
        math.cos(math.radians(lat2)) *
        math.sin(dlon / 2) ** 2
    )
    return 2 * R * math.asin(math.sqrt(a))


def run_deployment(spill, risk):
    with open(PORTS_FILE, "r") as f:
        ports = json.load(f)

    nearest = min(
        ports,
        key=lambda p: haversine(spill.lat, spill.lng, p["lat"], p["lng"])
    )

    distance_km = haversine(
        spill.lat, spill.lng,
        nearest["lat"], nearest["lng"]
    )

    eta_hours = round(distance_km / SHIP_SPEED_KMH, 2)

    # Ship allocation rule
    if risk["risk_score"] >= 4:
        ships = 3
    elif risk["risk_score"] >= 1.5:
        ships = 2
    else:
        ships = 1

    return {
        "nearest_port": {
            "name": nearest["name"],
            "distance_km": round(distance_km, 2)
        },
        "eta_hours": eta_hours,
        "ships_required": ships
    }

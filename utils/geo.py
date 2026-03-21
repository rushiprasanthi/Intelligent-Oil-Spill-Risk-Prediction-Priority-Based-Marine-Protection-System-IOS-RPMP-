import math

EARTH_RADIUS_KM = 6371


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate great-circle distance between two points.
    """
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.asin(math.sqrt(a))
    return EARTH_RADIUS_KM * c

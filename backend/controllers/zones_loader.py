import json
from pathlib import Path
from typing import List, Dict


def _load_raw_zones() -> List[Dict]:
    base = Path(__file__).resolve().parents[2]
    zones_file = base / "data" / "zones" / "full_zones.json"
    try:
        with open(zones_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("zones_loader: failed to load full_zones.json:", e)
        return []


def _deduplicate(zones: List[Dict]) -> List[Dict]:
    seen_ids = set()
    seen_coords = set()
    seen_names = set()
    cleaned = []

    for z in zones:
        zid = z.get("zone_id")
        name = (z.get("name") or "").strip().lower()
        lat = z.get("lat")
        lng = z.get("lng")

        coord_key = None
        if isinstance(lat, (int, float)) and isinstance(lng, (int, float)):
            coord_key = (round(float(lat), 6), round(float(lng), 6))

        duplicate = False
        if zid and zid in seen_ids:
            print(f"zones_loader: duplicate zone_id removed: {zid}")
            duplicate = True
        if coord_key and coord_key in seen_coords:
            print(f"zones_loader: duplicate coords removed: {coord_key} for {zid or name}")
            duplicate = True
        if name and name in seen_names:
            print(f"zones_loader: duplicate name removed: {name}")
            duplicate = True

        if duplicate:
            continue

        if zid:
            seen_ids.add(zid)
        if coord_key:
            seen_coords.add(coord_key)
        if name:
            seen_names.add(name)

        cleaned.append(z)

    return cleaned


_RAW = _load_raw_zones()
_CLEANED_ZONES = _deduplicate(_RAW)


def get_cleaned_zones():
    return _CLEANED_ZONES

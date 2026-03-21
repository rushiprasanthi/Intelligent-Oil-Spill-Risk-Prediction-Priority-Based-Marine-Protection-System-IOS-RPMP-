from decision_logic.exposure_calculator import calculate_exposure
from decision_logic.risk_calculator import calculate_risk
from decision_logic.priority_classifier import classify_priority
from decision_logic.explanation_engine import generate_explanation


def get_virtual_zone_near_spill(lat, lng):
    """
    Simplified proxy zone for early-stage decision support.
    """
    return {
        "lat": lat + 0.08,
        "lng": lng + 0.08,
        "sensitivity": 9
    }


def run_risk_analysis(spill, sim):
    # Base hazard (always non-zero)
    base_hazard = spill.spill_size * (sim["wind_speed"] / 10)

    zone = get_virtual_zone_near_spill(spill.lat, spill.lng)

    exposure = calculate_exposure(
        spill.lat,
        spill.lng,
        zone["lat"],
        zone["lng"],
        sim["spread_radius_km"]
    )

    # 🔧 FIX: safety floor to avoid false zero-risk
    if exposure < 0.05:
        exposure = 0.05

    zone_risk = calculate_risk(
        zone["sensitivity"],
        sim["wind_speed"] / 10,
        exposure,
        sim["time_hours"]
    )

    total_risk = round(base_hazard + zone_risk, 3)

    priority_code = classify_priority(total_risk)

    priority_labels = {
        "P1": "Immediate Protection",
        "P2": "Secondary Defense",
        "P3": "Monitoring"
    }

    explanation_text = generate_explanation(
        total_risk,
        priority_code,
        zone["sensitivity"],
        exposure,
        sim["wind_speed"]
    )

    return {
        "exposure": round(exposure, 3),
        "risk_score": total_risk,
        "priority": priority_code,
        "priority_label": priority_labels[priority_code],
        "explanation": {
            "summary": explanation_text,
            "factors": [
                "High ecological sensitivity",
                "Strong wind accelerating spread"
            ]
        }
    }

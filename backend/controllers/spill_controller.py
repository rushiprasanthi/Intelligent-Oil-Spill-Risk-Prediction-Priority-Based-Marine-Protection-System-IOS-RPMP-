from datetime import datetime

from backend.controllers.simulation_controller import run_simulation
from backend.controllers.risk_controller import run_risk_analysis
from backend.controllers.deployment_controller import run_deployment
from backend.controllers.zones_controller import evaluate_zones

# ✅ NEW: import email service
from backend.services.email_service import send_spill_email


def handle_spill(spill):
    # ─────────────────────────────────────────────
    # Run core engines
    # ─────────────────────────────────────────────
    simulation_output = run_simulation(spill)
    risk_output = run_risk_analysis(spill, simulation_output)
    deployment_output = run_deployment(spill, risk_output)

    # Extract simulation values
    time_hours = simulation_output["time_hours"]
    spread_radius = simulation_output["spread_radius_km"]
    exposure = risk_output["exposure"]
    risk_score = risk_output["risk_score"]

    # ─────────────────────────────────────────────
    # DERIVED DEMO-SAFE METRICS (TIME-BASED)
    # ─────────────────────────────────────────────

    # 1️⃣ Damage Controlled (%)
    damage_controlled = min(90, 40 + (time_hours * 3))

    # 2️⃣ Ecosystem Impact (%)
    ecosystem_impact = round(min(100, exposure * 100 + time_hours * 2), 1)

    # 3️⃣ Economic Loss (Million USD)
    economic_loss_musd = round(risk_score * time_hours * 2.5, 2)

    # 4️⃣ Fishery Area Affected (sq km)
    fishery_area_sqkm = round(3.14 * (spread_radius ** 2), 1)

    # 5️⃣ Alert Status
    alert_status = (
        "🚨 Emergency alert sent to response teams"
        if risk_output["priority"] == "P1"
        else "ℹ Monitoring only — no alert issued"
    )

    # ─────────────────────────────────────────────
    # FINAL RESPONSE (SINGLE SOURCE OF TRUTH)
    # ─────────────────────────────────────────────
    final_response = {
        "meta": {
            "simulation_id": "SIM-001",
            "timestamp_utc": datetime.utcnow().isoformat() + "Z",
            "mode": "decision-support-prototype"
        },

        "simulation": simulation_output,

        "risk": risk_output,

        "deployment": deployment_output,

        "damage_control": {
            "estimated_control_percent": damage_controlled,
            "damage_controlled_percent": damage_controlled,
            "ecosystem_impact_percent": ecosystem_impact,
            "fishery_area_sqkm": fishery_area_sqkm
        },

        "economic_loss_musd": economic_loss_musd,

        "alert": {
            "status": alert_status
        }
    }

    # ─────────────────────────────────────────────
    # ZONES ANALYSIS (HOTSPOT EVALUATION)
    # ─────────────────────────────────────────────
    try:
        zones_analysis = evaluate_zones(spill.lat, spill.lng, simulation_output, risk_output)
    except Exception as e:
        print("zones evaluation failed:", e)
        zones_analysis = []

    final_response["zones_analysis"] = zones_analysis
    # Number of zones evaluated after 5000km filter
    try:
        final_response["zones_evaluated_count"] = len(zones_analysis)
    except Exception:
        final_response["zones_evaluated_count"] = 0

    # ─────────────────────────────────────────────
    # 🔔 AUTO EMAIL FOR CRITICAL EVENTS (P1 ONLY)
    # ─────────────────────────────────────────────
    if risk_output["priority"] == "P1":
        try:
            send_spill_email(
                receiver_email="yourmail@gmail.com",  # 🔴 CHANGE THIS
                data=final_response
            )
        except Exception as e:
            # Email failure should NEVER break the system
            print("Email sending failed:", e)

    return final_response

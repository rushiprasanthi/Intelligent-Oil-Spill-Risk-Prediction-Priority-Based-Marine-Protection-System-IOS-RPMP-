# decision_logic/risk_calculator.py

def calculate_risk(sensitivity, spread_speed, exposure, time_to_impact_hours):
    """
    Computes environmental risk score.
    """

    if time_to_impact_hours <= 0:
        time_to_impact_hours = 0.1  # avoid division by zero

    risk = (sensitivity * spread_speed * exposure) / time_to_impact_hours
    return round(risk, 3)

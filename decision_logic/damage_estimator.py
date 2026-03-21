# decision_logic/damage_estimator.py

def estimate_damage_control(exposure, response_eta_hours, impact_eta_hours):
    """
    Estimates percentage of damage that can be controlled.
    """

    base_control = (1 - exposure) * 100

    if response_eta_hours < impact_eta_hours:
        base_control += 10
    else:
        base_control -= 15

    return round(max(0, min(100, base_control)), 1)

# decision_logic/explanation_engine.py

def generate_explanation(risk, priority, sensitivity, exposure, wind_speed):
    """
    Produces a structured, human-readable explanation.
    """

    factors = []

    if sensitivity >= 8:
        factors.append("High ecological sensitivity")

    if exposure >= 0.4:
        factors.append("Significant spill exposure probability")

    if wind_speed >= 25:
        factors.append("Strong wind accelerating spill spread")

    if not factors:
        factors.append("Moderate environmental conditions")

    summary = (
        f"Risk score of {risk} resulted in priority {priority} "
        f"based on current environmental and exposure conditions."
    )

    return {
        "summary": summary,
        "factors": factors
    }

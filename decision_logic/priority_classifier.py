# decision_logic/priority_classifier.py

def classify_priority(risk_score):
    """
    Converts risk score into priority code.
    """

    if risk_score >= 3.0:
        return "P1"
    elif risk_score >= 1.5:
        return "P2"
    else:
        return "P3"

from decision_logic.priority_classifier import classify_priority

def test_priority_classification():
    assert classify_priority(0.2).startswith("P3")
    assert classify_priority(2.0).startswith("P2")
    assert classify_priority(5.0).startswith("P1")

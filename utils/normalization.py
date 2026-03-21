def normalize(value, min_val, max_val):
    """
    Normalize a value to range [0, 1].
    """
    if max_val == min_val:
        return 0.0

    return max(0.0, min(1.0, (value - min_val) / (max_val - min_val)))


def clamp(value, min_val, max_val):
    """
    Clamp value within bounds.
    """
    return max(min_val, min(value, max_val))

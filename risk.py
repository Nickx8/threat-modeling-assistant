def calculate_risk(likelihood, impact):
    """
    Calculate risk score using:

    Risk Score = Likelihood × Impact
    """

    if not isinstance(likelihood, int) or not isinstance(impact, int):
        raise ValueError("Likelihood and impact must be integers.")

    if likelihood < 1 or likelihood > 5:
        raise ValueError("Likelihood must be between 1 and 5.")

    if impact < 1 or impact > 5:
        raise ValueError("Impact must be between 1 and 5.")

    score = likelihood * impact

    if score >= 17:
        level = "Critical"
    elif score >= 10:
        level = "High"
    elif score >= 5:
        level = "Medium"
    else:
        level = "Low"

    return score, level
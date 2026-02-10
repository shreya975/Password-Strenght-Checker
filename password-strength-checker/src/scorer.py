def calculate_score(validation_result: dict) -> tuple:
    """
    Calculate password strength score and label.
    Returns (score, strength).
    """

    score = 0

    if validation_result.get("length"):
        score += 25
    if validation_result.get("uppercase"):
        score += 15
    if validation_result.get("lowercase"):
        score += 15
    if validation_result.get("digit"):
        score += 20
    if validation_result.get("special"):
        score += 25

    # Strength classification
    if score <= 30:
        strength = "Weak"
    elif score <= 60:
        strength = "Medium"
    elif score <= 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength

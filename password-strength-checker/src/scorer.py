def calculate_score(validation_result: dict, pattern_result: dict = None) -> tuple:
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

    # Pattern penalties
    if pattern_result:
        if pattern_result.get("common_password"):
            score -= 40
        if pattern_result.get("repeated_chars"):
            score -= 20
        if pattern_result.get("sequential_chars"):
            score -= 20

    score = max(score, 0)

    if score <= 30:
        strength = "Weak"
    elif score <= 60:
        strength = "Medium"
    elif score <= 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength

def estimate_crack_time(password: str) -> str:
    """
    Estimate time to crack password using brute force.
    Returns human-readable time.
    """

    if not password:
        return "Instantly"

    charset_size = 0

    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(not c.isalnum() for c in password):
        charset_size += 32  # special characters

    length = len(password)

    combinations = charset_size ** length
    guesses_per_second = 10_000_000_000  # 10 billion

    seconds = combinations / guesses_per_second

    return _format_time(seconds)

def _format_time(seconds: float) -> str:
    if seconds < 1:
        return "Less than a second"
    elif seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds // 60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds // 86400)} days"
    elif seconds < 315360000:
        return f"{int(seconds // 31536000)} years"
    else:
        return "Centuries"

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

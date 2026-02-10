def generate_suggestions(validation_result: dict) -> list:
    """
    Generate improvement suggestions based on failed validation rules.
    """

    suggestions = []

    if not validation_result.get("length"):
        suggestions.append("Increase password length to at least 8 characters.")

    if not validation_result.get("uppercase"):
        suggestions.append("Add at least one uppercase letter (A-Z).")

    if not validation_result.get("lowercase"):
        suggestions.append("Add at least one lowercase letter (a-z).")

    if not validation_result.get("digit"):
        suggestions.append("Include at least one number (0-9).")

    if not validation_result.get("special"):
        suggestions.append("Use at least one special character (e.g., @, #, $, !).")

    if not suggestions:
        suggestions.append("Your password is strong. No improvements needed.")

    return suggestions

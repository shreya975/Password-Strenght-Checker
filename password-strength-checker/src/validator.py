import re

MIN_LENGTH = 8

def validate_password(password: str) -> dict:
    """
    Validates a password against basic security rules.
    """

    if not password:
        return {
            "length": False,
            "uppercase": False,
            "lowercase": False,
            "digit": False,
            "special": False
        }

    return {
        "length": len(password) >= MIN_LENGTH,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"[0-9]", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

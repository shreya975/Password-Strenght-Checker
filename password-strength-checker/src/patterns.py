import re

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "admin",
    "welcome", "abc123", "letmein"
}

def detect_patterns(password: str) -> dict:
    """
    Detect weak password patterns.
    Returns a dictionary of detected issues.
    """

    issues = {
        "common_password": False,
        "repeated_chars": False,
        "sequential_chars": False
    }

    if not password:
        return issues

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        issues["common_password"] = True

    # Repeated characters (aaa, 111)
    if re.search(r"(.)\1{2,}", password):
        issues["repeated_chars"] = True

    # Sequential characters (abc, 123)
    sequences = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"

    for i in range(len(password) - 2):
        part = password[i:i+3].lower()
        if part in sequences or part in numbers:
            issues["sequential_chars"] = True
            break

    return issues

import re
import os


def load_common_passwords() -> set:
    """
    Load common passwords from data/common_passwords.txt
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data", "common_passwords.txt")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return {line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        return set()


COMMON_PASSWORDS = load_common_passwords()


def detect_patterns(password: str) -> dict:
    """
    Detect weak password patterns.
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

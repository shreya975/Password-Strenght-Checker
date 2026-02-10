from src.validator import validate_password
from src.scorer import calculate_score, estimate_crack_time
from src.suggestions import generate_suggestions
from src.patterns import detect_patterns


def main():
    password = input("Enter your password: ")

    # Core analysis
    validation_result = validate_password(password)
    pattern_result = detect_patterns(password)
    score, strength = calculate_score(validation_result, pattern_result)
    crack_time = estimate_crack_time(password)
    suggestions = generate_suggestions(validation_result)

    # Output section
    print("\nValidation Result:")
    for rule, passed in validation_result.items():
        status = "PASS" if passed else "FAIL"
        print(f"{rule:<10} : {status}")

    print("\nPattern Issues:")
    found_issue = False
    for issue, detected in pattern_result.items():
        if detected:
            print(f"- {issue.replace('_', ' ').title()}")
            found_issue = True
    if not found_issue:
        print("None")

    print("\nPassword Score :", score)
    print("Password Strength :", strength)
    print("Estimated Crack Time :", crack_time)

    print("\nSuggestions:")
    for i, s in enumerate(suggestions, 1):
        print(f"{i}. {s}")


if __name__ == "__main__":
    main()

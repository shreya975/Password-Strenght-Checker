from src.validator import validate_password
from src.scorer import calculate_score
from src.suggestions import generate_suggestions

def main():
    password = input("Enter your password: ")

    validation_result = validate_password(password)
    score, strength = calculate_score(validation_result)
    suggestions = generate_suggestions(validation_result)

    print("\nValidation Result:")
    for rule, passed in validation_result.items():
        status = "PASS" if passed else "FAIL"
        print(f"{rule:<10} : {status}")

    print("\nPassword Score :", score)
    print("Password Strength :", strength)

    print("\nSuggestions:")
    for idx, suggestion in enumerate(suggestions, start=1):
        print(f"{idx}. {suggestion}")

if __name__ == "__main__":
    main()
